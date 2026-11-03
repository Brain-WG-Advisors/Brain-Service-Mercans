# -*- coding: utf-8 -*-
"""US research oracle for the country suite (run_suite.py, C37).

expected(case) -> {line: value} recomputed from the facts files (_research/*-facts.json).
Federal cases are an independent re-implementation of IRS Pub. 15-T 2026 Worksheet 1A (STANDARD
schedules), FICA (OASDI base per employer, Additional Medicare threshold), FUTA and the supplemental
rates; nothing is imported from the CCG example calculator. State oracle cases read the CCG
calculator's re-derivation (01-ccg/_examples/out/results.json), see suite.json _limitations.
compare(o, e) -> [(line, research, reference)] for lines that differ by more than half a cent.
"""
import glob
import json
import os
from decimal import Decimal, ROUND_HALF_UP

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
FACTS = {}
for _fp in glob.glob(os.path.join(BASE, "_research", "*-facts.json")):
    for _f in json.load(open(_fp, encoding="utf-8")).get("facts", []):
        FACTS.setdefault(_f["key"], []).append(_f)
ON = "2026-06-30"


def V(key, on=ON):
    es = FACTS[key]
    for f in es:
        if (f.get("effective_from") or "0000") <= on <= (f.get("effective_to") or "9999"):
            return Decimal(str(f["value"]))
    return Decimal(str(es[0]["value"]))


def r2(x):
    return Decimal(x).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def r0(x):
    return Decimal(x).quantize(Decimal("1"), rounding=ROUND_HALF_UP)


def fit_ws1a(wage, periods, status="single", nra=False):
    w = Decimal(str(wage))
    if nra:
        w += V("fed.fit.nra.addon.table2.weekly")       # weekly case only (suite inputs)
    annual = r2(w * periods)
    l1g = V("fed.fit.worksheet1a.line1g.mfj" if status == "mfj" else "fed.fit.worksheet1a.line1g.other")
    adj = annual - l1g
    b = 1
    for n in range(1, 9):
        k = f"fed.fit.standard.{status}.bracket.{n}.floor"
        if k in FACTS and adj >= V(k):
            b = n
    pre = f"fed.fit.standard.{status}.bracket.{b}."
    tax = V(pre + "cumulative_tax") + (adj - V(pre + "floor")) * V(pre + "rate") / 100
    return max(Decimal(0), r2(tax / periods))


def fica(wage, ytd):
    wage, ytd = Decimal(str(wage)), Decimal(str(ytd))
    base = V("fed.fica.oasdi.wage_base")
    oasdi = r2(min(max(Decimal(0), base - ytd), wage) * V("fed.fica.oasdi.rate.employee") / 100)
    med = r2(wage * V("fed.fica.medicare.rate.employee") / 100)
    thr = V("fed.fica.addl_medicare.withholding_threshold")
    over = max(Decimal(0), ytd + wage - max(thr, ytd))
    addl = r2(over * V("fed.fica.addl_medicare.rate") / 100)
    return oasdi, med, addl


def futa(wage, ytd):
    base = max(Decimal(0), min(Decimal(str(wage)), V("fed.futa.wage_base") - Decimal(str(ytd))))
    return r2(base * V("fed.futa.rate.net") / 100)


_RES = None


def _results():
    global _RES
    if _RES is None:
        _RES = json.load(open(os.path.join(BASE, "01-ccg", "_examples", "out", "results.json"), encoding="utf-8"))
    return _RES


def expected(c):
    cid = c["id"]
    if cid in ("US-M12-A", "US-M12-C", "US-M06-EX1", "US-M06-EX2"):
        w, ytd = Decimal(str(c["wage"])), c["ytd"]
        fit = fit_ws1a(w, c["periods"], c["status"], c.get("nra", False))
        oasdi, med, addl = fica(w, ytd)
        out = {"fit": fit, "oasdi": oasdi, "medicare": med, "net": w - fit - oasdi - med - addl}
        if cid.startswith("US-M12"):
            out.update(addl_medicare=addl, futa=futa(w, ytd))
        return {k: float(v) for k, v in out.items()}
    if cid == "US-M12-E":
        # 401(k) deferral: each base is reduced only where the fed.base.401k_deferral.<base> fact says 'excluded'
        w, d = Decimal(str(c["wage"])), Decimal(str(c["deferral"]))
        red = {b: (d if str(FACTS[f"fed.base.401k_deferral.{b}"][0]["value"]).lower().startswith("excluded") else Decimal(0))
               for b in ("fit", "fica", "futa")}
        fit = fit_ws1a(w - red["fit"], c["periods"], c["status"])
        oasdi, med, addl = fica(w - red["fica"], c["ytd"])
        return {k: float(v) for k, v in dict(fit=fit, oasdi=oasdi, medicare=med, net=w - d - fit - oasdi - med - addl,
                                             futa=futa(w - red["futa"], c["ytd"])).items()}
    if cid == "US-M12-B":
        w = Decimal(c["hours"]) * V(c["hourly_key"])
        fit = fit_ws1a(w, c["periods"], c["status"])
        oasdi, med, addl = fica(w, c["ytd"])
        return {k: float(v) for k, v in dict(fit=fit, oasdi=oasdi, medicare=med,
                                             net=w - fit - oasdi - med - addl, futa=futa(w, c["ytd"])).items()}
    if cid == "US-M12-D":
        b = Decimal(c["bonus"])
        fit = r2(b * V("fed.fit.supplemental.mandatory_rate") / 100)
        med = r2(b * V("fed.fica.medicare.rate.employee") / 100)
        addl = r2(b * V("fed.fica.addl_medicare.rate") / 100)      # wages already above the threshold
        return {k: float(v) for k, v in dict(fit=fit, medicare=med, addl_medicare=addl, net=b - fit - med - addl).items()}
    if c.get("flat"):
        a = Decimal(str(c["amount"]))
        fit = r2(a * V("fed.fit.supplemental.flat_rate") / 100)
        oasdi, med, addl = fica(a, c["ytd"])
        return {k: float(v) for k, v in dict(fit=fit, oasdi=oasdi, medicare=med, net=a - fit - oasdi - med - addl).items()}
    if cid == "US-M04-OT":
        rate, h = Decimal(str(c["rate"])), Decimal(c["hours"])
        thr = V("fed.overtime.weekly_threshold_hours")
        return {"gross": float(r2(thr * rate + (h - thr) * rate * V("fed.overtime.premium.multiplier")))}
    if cid == "US-M04-PRORATION":
        return {"gross": float(r2(Decimal(c["monthly"]) * c["in_service"] / c["days"]))}
    if c.get("calc") == "ct_table":
        # r3: independent lookup in the keyed DRS per-period table rows (configuration decision: tables)
        cols = [x.strip() for x in str(FACTS["ct.wh.tables.columns"][0]["value"]).split("(")[0].split("|")]
        ci = cols.index(c["code"])
        w = Decimal(str(c["wage"]))
        for k, fs in FACTS.items():
            if k.startswith(f"ct.wh.table.{c['period']}.row."):
                v = str(fs[0]["value"]).split("|")
                if Decimal(v[0]) < w <= Decimal(v[1]):
                    return {"withholding": float(Decimal(v[ci]))}
        raise KeyError(f"no CT {c['period']} band for {w}")
    if c["kind"] == "official_example" and c.get("calc") == "annex_DC-MA":
        # r3: annex example calculator re-derivation (01-ccg/_scratch/annex-DC-MA/examples_results.json)
        rows = json.load(open(os.path.join(BASE, "01-ccg", "_scratch", "annex-DC-MA", "examples_results.json"),
                              encoding="utf-8"))
        row = next(r for r in rows if len(r) >= 6 and r[5] == c["oracle_key"] and r[1] == c.get("example"))
        return {"withholding": float(Decimal(str(row[2]).replace(",", "")))}
    if c["kind"] == "official_example":
        ok_ = c.get("same_as") or c["oracle_key"]
        comp = Decimal(_results()[ok_]["computed"])
        ref = str(_results()[ok_]["fact"])
        return {"withholding": float(r0(comp) if "." not in ref else r2(comp))}
    if c["kind"] == "parameter":
        return {"value": float(V(c["key"], c.get("on") or ON))}
    raise KeyError(cid)


def compare(o, e):
    out = []
    for k, x in o.items():
        y = e.get(k)
        if y is None or abs(float(x) - float(y)) > 0.005:
            out.append((k, x, y))
    return out

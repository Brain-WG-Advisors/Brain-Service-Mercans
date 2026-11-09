# -*- coding: utf-8 -*-
"""Worked examples for CCG modules m04 and m06 (US build), computed from the facts (C38).

Every rate, threshold and table value is read from _research/CCG-*-facts.json by key; no number
of the law is typed here. Inputs that are scenario choices (wage, hours, days) are declared as
SCENARIO constants. Rounding: half-up to the cent for every displayed amount (build rule, CCG
m01 §1.5); full precision is carried internally and each displayed expression recomputes within
one cent. Output: m01_m07_examples.json (rows with [[FACT:]] tags) + printed tables.

Run: python build_examples_m01_m07.py
"""
import glob
import json
import os
from decimal import Decimal, ROUND_HALF_UP

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
FACTS = {}
for fp in sorted(glob.glob(os.path.join(BASE, "_research", "CCG-*-facts.json"))):
    for f in json.load(open(fp, encoding="utf-8")).get("facts", []):
        FACTS.setdefault(f["key"], []).append(f)


def fact(key, on="2026-06-30"):
    fs = [f for f in FACTS[key] if (f.get("effective_from") or "0000") <= on <= (f.get("effective_to") or "9999")]
    vals = {json.dumps(f["value"]) for f in fs}
    assert len(vals) == 1, (key, on, vals)
    return fs[0]["value"]


def D(x):
    return Decimal(str(x))


def c(x):
    return D(x).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def m(x):
    return f"{c(x):,.2f}"


def n(x):
    """integer-valued fact as written in the facts (thousands separator)."""
    v = D(x)
    return f"{int(v):,}" if v == v.to_integral_value() else f"{v:,}"


def tag(key, on="2026-06-30", money=False):
    v = fact(key, on)
    if isinstance(v, (int, float)) and float(v).is_integer() and not money:
        s = f"{int(v):,}"
    elif money:
        s = f"{float(v):,.2f}"
    else:
        s = repr(v)
    return f"[[FACT:{key}={s}]]"


OUT = {}

# ------------------------------------------------------------- m04 proration (configuration choice)
SC_SALARY, SC_DAYS_PERIOD, SC_DAYS_SERVED = D("6300.00"), 22, 10
pr = SC_SALARY * SC_DAYS_SERVED / SC_DAYS_PERIOD
OUT["proration"] = [
    ["Scenario: monthly salary 6,300.00; 22 working days in the month; hired on working day 13 (10 working days in service)", ""],
    [f"{m(SC_SALARY)} × {SC_DAYS_SERVED} ÷ {SC_DAYS_PERIOD}", m(pr)],
]

# ------------------------------------------------------------- m04 overtime (FLSA)
SC_RATE, SC_HOURS = D("26.50"), 46
thr = fact("fed.overtime.weekly_threshold_hours")
mult = D(fact("fed.overtime.premium.multiplier"))
reg = D(thr) * SC_RATE
oth = SC_HOURS - thr
otp = D(oth) * SC_RATE * mult
OUT["overtime"] = [
    ["Scenario: non-exempt employee, USD 26.50 an hour, 46 hours in the workweek, no State daily overtime", ""],
    [f"{tag('fed.overtime.weekly_threshold_hours')} × {m(SC_RATE)}", m(reg)],
    [f"{SC_HOURS} − {tag('fed.overtime.weekly_threshold_hours')}", f"{oth}"],
    [f"{oth} × {m(SC_RATE)} × {tag('fed.overtime.premium.multiplier')}", m(otp)],
    [f"{m(reg)} + {m(otp)}", m(reg + otp)],
]

# ------------------------------------------------------------- m06 federal income tax, Worksheet 1A


def bracket(status, adj):
    rows = []
    for i in range(1, 9):
        rows.append((i, D(fact(f"fed.fit.standard.{status}.bracket.{i}.floor")),
                     D(fact(f"fed.fit.standard.{status}.bracket.{i}.rate")),
                     D(fact(f"fed.fit.standard.{status}.bracket.{i}.cumulative_tax"))))
    sel = [r for r in rows if adj >= r[1]][-1]
    return sel


def worksheet(label, wages_period, periods, status, line1g_key, addon_key=None):
    rows = []
    w = D(wages_period)
    if addon_key:
        add = D(fact(addon_key))
        rows.append(["1a. Wages for the computation, including the NRA add-on (Table 2, weekly)", f"{m(w)} + {tag(addon_key, money=True)}", m(w + add)])
        w = w + add
    ann = w * periods
    rows.append(["1c. Annualised wages", f"{m(w)} × {periods}", m(ann)])
    g = D(fact(line1g_key))
    adj = ann - g
    rows.append(["1i. Adjusted annual wage (line 1g subtracted, Step 2 not checked)", f"{m(ann)} − {tag(line1g_key)}", m(adj)])
    i, floor, rate, cum = bracket(status, adj)
    k = f"fed.fit.standard.{status}.bracket.{i}"
    exc = adj - floor
    rows.append([f"2e. Excess over the bracket floor (STANDARD {status.upper()} row {i})", f"{m(adj)} − {tag(k + '.floor')}", m(exc)])
    pct = exc * rate / 100
    rows.append(["2f. Excess × bracket rate", f"{m(exc)} × {tag(k + '.rate')}%", m(pct)])
    tent = cum + c(pct)
    rows.append(["2g. Tentative annual withholding", f"{tag(k + '.cumulative_tax')} + {m(pct)}", m(tent)])
    per = tent / periods
    rows.append(["2h. Withholding for the period", f"{m(tent)} ÷ {periods}", m(per)])
    return rows, c(per)


def fica(wages):
    w = D(wages)
    oa = w * D(fact("fed.fica.oasdi.rate.employee")) / 100
    me = w * D(fact("fed.fica.medicare.rate.employee")) / 100
    rows = [["OASDI employee", m(w), f"{tag('fed.fica.oasdi.rate.employee')}%", m(oa)],
            ["Medicare employee", m(w), f"{tag('fed.fica.medicare.rate.employee')}%", m(me)]]
    return rows, c(oa), c(me)


SC_WEEKLY = D("1640.00")
r1, fit1 = worksheet("resident", SC_WEEKLY, 52, "single", "fed.fit.worksheet1a.line1g.other")
f1, oa1, me1 = fica(SC_WEEKLY)
OUT["ex1"] = {"scenario": "Resident employee, Form W-4 (2026): Single, Step 2 not checked, no Step 3 or Step 4 entries; weekly wages USD 1,640.00; no pre-tax deductions; year-to-date wages below every cap.",
              "fit": r1, "fica": f1,
              "net": [["Net pay", f"{m(SC_WEEKLY)} − {m(fit1)} − {m(oa1)} − {m(me1)}", m(SC_WEEKLY - fit1 - oa1 - me1)]]}

r2, fit2 = worksheet("nra", SC_WEEKLY, 52, "single", "fed.fit.worksheet1a.line1g.other",
                     addon_key="fed.fit.nra.addon.table2.weekly")
f2, oa2, me2 = fica(SC_WEEKLY)
OUT["ex2"] = {"scenario": "Nonresident alien employee, Form W-4 (2026) completed per Notice 1392 (Single, NRA, Step 2 not checked); weekly wages USD 1,640.00; first paid in 2026 (Table 2 add-on); no treaty exemption.",
              "fit": r2, "fica": f2,
              "net": [["Net pay (the add-on is not paid and not reported)", f"{m(SC_WEEKLY)} − {m(fit2)} − {m(oa2)} − {m(me2)}", m(SC_WEEKLY - fit2 - oa2 - me2)]]}

SC_BONUS = D("12400.00")
flat = D(fact("fed.fit.supplemental.flat_rate"))
fit3 = SC_BONUS * flat / 100
f3, oa3, me3 = fica(SC_BONUS)
OUT["ex3"] = {"scenario": "Irregular payment: annual bonus USD 12,400.00 paid separately from regular wages to a resident employee whose 2026 supplemental wages stay below the mandatory-rate threshold and whose year-to-date wages are below the OASDI base and the Additional Medicare threshold; the employer uses the optional flat rate.",
              "fit": [["Federal income tax (flat supplemental rate)", m(SC_BONUS), f"{tag('fed.fit.supplemental.flat_rate')}%", m(fit3)]],
              "fica": f3,
              "net": [["Net bonus", f"{m(SC_BONUS)} − {m(fit3)} − {m(oa3)} − {m(me3)}", m(SC_BONUS - c(fit3) - oa3 - me3)]]}

json.dump(OUT, open(os.path.join(HERE, "m01_m07_examples.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
for k, v in OUT.items():
    print("==", k)
    print(json.dumps(v, indent=1, ensure_ascii=False))

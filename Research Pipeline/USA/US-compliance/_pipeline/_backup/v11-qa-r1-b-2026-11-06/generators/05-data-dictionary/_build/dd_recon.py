# -*- coding: utf-8 -*-
"""RSPEC x DD reconciliation (both directions), written to checks/rspec_dd_recon.csv.

Direction 1  every field row of the 20 Report Specs -> a DD element, or a recorded disposition
             (a spec row whose mapping cites the Data Dictionary and has no DD element = UNMAPPED = FAIL).
Direction 2  every DD element -> used by a Report Spec row, a Report Spec cell that carries the element's fact,
             or the payroll calculation / notice template named by the element's facts.
"""
import csv
import glob
import os
import re
from collections import defaultdict

from openpyxl import load_workbook

import dd_common as D
import dd_rules as RU

TAGRX = re.compile(r"\[\[FACT:\s*([A-Za-z0-9_.]+)\s*=")

CONS_MAP = {   # fact consumer token -> Report Spec ids that carry that report family
    "new_hire": ["US-SDNH-001"], "ui_qtr": ["US-UI-001"], "w2_state": ["US-DOR-002"], "wh_return": ["US-DOR-001"],
    "pfml_ltc_qtr": ["US-PFML-001"], "pfml_qtr": ["US-PFML-001"], "pfml": ["US-PFML-001"], "oq": ["US-PFML-001", "US-DOR-004"],
    "local": ["US-LOC-001"], "eit_lst": ["US-LOC-001"], "school_district": ["US-LOC-001"], "municipal": ["US-LOC-001"],
    "w2": ["US-SSA-001"], "aca": ["US-IRS-007"], "nys45": ["US-DOR-002"], "mctmt": ["US-DOR-004"],
}


def spec_fact_tags():
    """key -> set(spec ids) for every [[FACT:key=...]] tag in the 20 approved Report Specs."""
    out = defaultdict(set)
    for p in sorted(glob.glob(os.path.join(D.SPECS, "*-Spec.xlsx"))):
        sid = D.spec_id(p)
        wb = load_workbook(p, read_only=True)
        for ws in wb.worksheets:
            for row in ws.iter_rows(values_only=True):
                for v in row:
                    if isinstance(v, str) and "[[FACT:" in v:
                        for m in TAGRX.finditer(v):
                            out[m.group(1)].add(sid)
    return out


def spec_class(r):
    vt = str(r["valtype"] or "")
    m = re.search(r"\((.*?)\)", vt)
    k = (m.group(1) if m else vt).lower()
    if "identifier" in k or k == "text":
        return "text"
    if k == "code":
        return "code"
    if k == "flag":
        return "flag"
    if k == "count":
        return "integer"
    if k == "amount":
        return "decimal"
    return None


COMPAT = {"text": {"text", "code"}, "code": {"code", "text", "flag"}, "flag": {"flag", "code", "text"},
          "integer": {"integer", "decimal"}, "decimal": {"decimal", "integer"}, "date": {"date", "text"}}


def element_format(el):
    """Pre-Defined Format written for an element (spec cell J when fmt_from is set)."""
    if el.get("fmt_from"):
        sp, row = el["fmt_from"]
        return str(D.spec_row(sp, row)["fmt"])
    return el.get("fmt", "")


def compute(elements):
    by_id = {e["id"]: e for e in elements}
    RU.NAMES.clear()
    RU.NAMES.update({e["name"]: e["id"] for e in elements})
    tags = spec_fact_tags()
    recs = []
    used = defaultdict(list)       # element id -> [(spec, fid, row)]
    for r in D.spec_rows():
        claims = r["mapping"].startswith(D.DD_ID)
        rec = dict(spec=r["spec"], row=r["row"], fid=r["fid"], name=r["name"], spec_mapping=r["mapping"][:160],
                   spec_format=str(r["fmt"] or ""), spec_value_type=str(r["valtype"] or ""),
                   dd_sheet="", dd_elements="", dd_type="", dd_format="", name_check="", type_check="", format_check="",
                   status="", reason="")
        if not claims:
            rec["status"] = "NOT-DD"
            rec["reason"] = RU.disposition(r)
            recs.append(rec)
            continue
        m = RU.match_rule(r)
        if m is None:
            rec["status"] = "UNMAPPED"
            rec["reason"] = "no DD element for a row that cites the Data Dictionary"
            recs.append(rec)
            continue
        els, exc = m
        if exc:
            rec["status"] = "EXCEPTION"
            rec["reason"] = exc
            recs.append(rec)
            continue
        missing = [e for e in els if e not in by_id]
        if missing:
            rec["status"] = "UNMAPPED"
            rec["reason"] = f"rule names element(s) not in the catalogue: {missing}"
            recs.append(rec)
            continue
        for e in els:
            used[e].append((r["spec"], r["fid"], r["row"]))
        prim = by_id[els[0]]
        rec["status"] = "MAPPED"
        rec["dd_elements"] = " | ".join(by_id[e]["name"] for e in els)
        rec["dd_sheet"] = " | ".join(sorted({"ID Information" if by_id[e]["sheet"] == "ID" else "Country Fields" for e in els}))
        rec["dd_type"] = " | ".join(f"{by_id[e]['ftype']}/{by_id[e]['tcls']}" for e in els)
        rec["dd_format"] = element_format(prim)
        sl = str(r["label"] or "").strip().lower()
        if any(r["name"].strip().lower() == by_id[e]["name"].strip().lower() for e in els):
            rec["name_check"] = "identical name"
        elif any(sl and sl == str(by_id[e]["label"] or by_id[e]["name"]).strip().lower() for e in els):
            rec["name_check"] = "identical authority label"
        else:
            rec["name_check"] = "same concept (mapping rule)"
        sc = spec_class(r)
        if els[0] == "er.state_efile_threshold":
            rec["type_check"] = ("n/a (the spec row describes the threshold amount, a jurisdiction constant tagged in the spec; "
                                 "the DD holds the employer flag that the threshold is reached)")
        elif sc is None:
            rec["type_check"] = "n/a (spec leaves the type to the DD)"
        elif any(sc in COMPAT.get(by_id[e]["tcls"], {by_id[e]["tcls"]}) for e in els):
            rec["type_check"] = "match"
        else:
            rec["type_check"] = f"MISMATCH spec={sc} dd={[by_id[e]['tcls'] for e in els]}"
        sf, df = str(r["fmt"] or ""), element_format(prim)
        if df and sf == df:
            rec["format_check"] = "identical"
        elif df and re.search(r"[NAX9]{2,}|\(\d+\)|YYYY", sf):
            rec["format_check"] = f"differs: spec '{sf}' vs DD '{df}' (file layout vs display format)"
        else:
            rec["format_check"] = "n/a (spec names a type, not a format)"
        recs.append(rec)

    # direction 2: DD element -> use
    cons_specs = defaultdict(set)
    cons_calc = defaultdict(set)
    for e in elements:
        keys = list(e["facts"]) + ([k for k in D.DD_KEYS if k.startswith("dd.state.w4.")]
                                   if e["om"] == "State withholding certificate" else [])
        for k in keys:
            f = D.fact(k)
            for tok in str(f.get("_consumers") or "").split(";"):
                tok = tok.strip()
                if tok.startswith("calc:"):
                    cons_calc[e["id"]].add(tok[5:].strip())
                elif tok.startswith("rspec."):
                    last = tok.split(".")[-1]
                    for s in CONS_MAP.get(last, []):
                        cons_specs[e["id"]].add(s)
                elif tok:
                    cons_calc[e["id"]].add(tok)
            for s in tags.get(k, ()):
                cons_specs[e["id"]].add(s)
        for c_ in e.get("consumers", []):
            cons_calc[e["id"]].add(c_)
    usage = {}
    for e in elements:
        rows = used.get(e["id"], [])
        specs_direct = sorted({s for s, _, _ in rows})
        ev = []
        if rows:
            ev.append(f"{len(rows)} spec row(s)")
        if cons_specs.get(e["id"]):
            ev.append("spec cells citing its facts: " + ", ".join(sorted(cons_specs[e["id"]])))
        if cons_calc.get(e["id"]):
            ev.append("calculation / template: " + "; ".join(sorted(cons_calc[e["id"]])))
        usage[e["id"]] = dict(rows=rows, specs=sorted(set(specs_direct) | cons_specs.get(e["id"], set())),
                              calc=sorted(cons_calc.get(e["id"], [])), evidence="; ".join(ev), used=bool(ev))
    # group rule: the State and programme qualifiers are the keys of the account number; they carry its consumers
    for q in ("er.state_account_state", "er.state_account_programme"):
        if q in usage and "er.state_account_ids" in usage:
            g = usage["er.state_account_ids"]
            usage[q] = dict(rows=list(g["rows"]), specs=list(g["specs"]), calc=list(g["calc"]),
                            evidence=g["evidence"] + " (key of the State employer account number group)", used=g["used"])
    return recs, usage


def used_by_text(eid, usage):
    u = usage[eid]
    parts = []
    byspec = defaultdict(list)
    for s, fid, _ in u["rows"]:
        byspec[s].append(str(fid))
    for s in sorted(byspec):
        ids = byspec[s]
        shown = ", ".join(ids[:4]) + (f", +{len(ids) - 4} more" if len(ids) > 4 else "")
        parts.append(f"{s} v{D.PKG} ({shown})")
    others = [s for s in u["specs"] if s not in byspec]
    if others:
        parts.append("spec cells that cite its facts: " + ", ".join(f"{s} v{D.PKG}" for s in others))
    if u["calc"]:
        parts.append("payroll calculation / template: " + "; ".join(u["calc"]))
    return "Used by: " + ("; ".join(parts) if parts else "no consumer recorded") + "."


def write_csv(recs, path):
    cols = ["spec", "row", "fid", "name", "spec_mapping", "spec_format", "spec_value_type", "status", "dd_sheet",
            "dd_elements", "dd_type", "dd_format", "name_check", "type_check", "format_check", "reason"]
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        for r in recs:
            w.writerow(r)


def write_usage_csv(elements, usage, path):
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["dd_sheet", "dd_element", "level", "spec_rows", "spec_ids_citing", "calculation_or_template", "used"])
        for e in elements:
            u = usage[e["id"]]
            w.writerow(["ID Information" if e["sheet"] == "ID" else "Country Fields", e["name"], e["lvl"], len(u["rows"]),
                        "; ".join(u["specs"]), "; ".join(u["calc"]), "yes" if u["used"] else "NO"])

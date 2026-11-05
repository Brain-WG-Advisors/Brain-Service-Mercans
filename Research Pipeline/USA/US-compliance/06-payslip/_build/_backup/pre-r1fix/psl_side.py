# -*- coding: utf-8 -*-
"""Side files of the PSL build: bindings csv, research request, gaps.json entries (C70), legal items (C57), reconciliation."""
import csv
import datetime as dt
import json
import os

import psl_common as S
import psl_content as K

TODAY = dt.date.today().isoformat()


def new_key_ok(key):
    import re
    return re.match(r"^[a-z][a-z0-9_]*(\.[a-z0-9_]+)+$", key) is not None


def write_bindings():
    rows = []
    for (key, ef), locs in sorted(S.USED.items(), key=lambda x: (x[0][0], str(x[0][1]))):
        f = S.fact(key, ef) if S.has(key) else None
        if not f:
            continue
        for loc in sorted(locs):
            rows.append([loc, key, f["register_id"], ";".join(S.rids(f)[1:]), f.get("effective_from"), f["_file"]])
    with open(os.path.join(S.BASE, "_pipeline", "PSL-bindings.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["location", "key", "register_id", "also_register_ids", "effective_from", "facts_file"])
        w.writerows(rows)
    return len(rows)


def write_requests(REQ):
    fn = f"06-payslip/{S.FILENAME}"
    reqs = []
    for key, r in sorted(REQ.items(), key=lambda x: x[1]["gid"]):
        reason = ("open question recorded with the facts" if key in S.UNRESOLVED else
                  "text not proven in the saved source" if r["why"] == "f44" else "no source recorded")
        reqs.append({"id": r["rq"], "key": key if new_key_ok(key) else "psl.unspecified.missing",
                     "location": f"{fn}!Field Option!{r['gid']}",
                     "question": r["question"] if len(r["question"]) >= 20 else r["question"] + " (see the cell)",
                     "why_blocking": f"The cell {r['gid']} cannot state the rule ({reason}).",
                     "domain": "payslip_statute", "acceptable_tier": "A.2", "attempted_by_requester": r["searched"],
                     "severity": "minor", "expected_shape": "the statement with the register row that carries it; effective date",
                     "_gap_id": r["gid"], "_cells": r["locations"][:6], "_jurisdictions": r["jurs"]})
    doc = {"schema_version": "1.4.0", "artifact": "PSL", "unit": "8_sheets", "requested_by": "artifact-builder", "round": 1,
           "created_on": TODAY,
           "_note": "Requests of the PSL build, round 1. Every request is non-blocking; each has a cell reading "
                    "'Not configured in this release [[GAP:PSL-RQ-nn]]' and an entry in _research/gaps.json.",
           "requests": reqs}
    json.dump(doc, open(os.path.join(S.RESEARCH, "PSL-research-request.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    gp = os.path.join(S.RESEARCH, "gaps.json")
    g = json.load(open(gp, encoding="utf-8"))
    g["gaps"] = [x for x in g["gaps"] if not str(x.get("id", "")).startswith("PSL-RQ-")]
    for key, r in sorted(REQ.items(), key=lambda x: x[1]["gid"]):
        g["gaps"].append({"id": r["gid"], "key": key, "subject": f"{r['gid']} - {r['question_short']}",
                          "location": f"{fn}!Field Option!{r['gid']}", "research_request_id": r["rq"], "blocking": False,
                          "severity": "minor", "searched": r["searched"], "searched_on": TODAY,
                          "what_would_close_it": r["closes"], "status": "open", "artifact": "PSL"})
    json.dump(g, open(gp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    json.dump({k: {**v, "locations": v["locations"][:20]} for k, v in REQ.items()},
              open(os.path.join(S.CHECKS, "psl_requests.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)


LEGAL = [  # id, label, match text on the payslip, register id
    ("gross", "Gross earnings (CA 226(a))", ["Gross Earning"], "US-CAS5-005"),
    ("net", "Net wages / net pay", ["Net Pay"], "US-CAS5-005"),
    ("hours", "Total hours worked", ["Regular Hours"], "US-CAS5-005"),
    ("rate_hours", "Every rate with its hours", ["Rate of Pay"], "US-CAS5-005"),
    ("piece", "Piece-rate units and rate", ["Piece-Rate Units"], "US-CAS5-005"),
    ("period", "Pay-period dates", ["Pay Period"], "US-CAS5-005"),
    ("name_ssn_id", "Employee name and last 4 SSN or employee ID", ["Employee ID", "Social Security Number"], "US-CAS5-005"),
    ("employer_name_addr", "Employer legal name and address", ["Employer Legal Name", "Employer Address"], "US-CAS5-005"),
    ("deductions", "Itemised deductions", ["Deduction Line"], "US-DES5-002"),
    ("pay_date", "Pay date", ["Pay Date"], "US-DCS5-010"),
    ("gratuities", "Gratuities on a separate line", ["Tips and Gratuities"], "US-DCS5-010"),
    ("employer_phone", "Employer phone", ["Employer Phone"], "US-MDP51-005"),
    ("overtime_sep", "Straight-time and overtime pay separately", ["Overtime Hours"], "US-CTP51-005"),
    ("mw_allowance", "Allowances toward minimum wage", ["Allowances Credited toward Minimum Wage"], "US-HIP52-001"),
    ("employee_address", "Employee address", ["Employee Home Address"], "US-OHP51-001"),
    ("employer_id", "Employer registry or identification number", ["Employer Identification Number"], "US-ORS5-026"),
    ("sick_balance", "Paid sick leave balance", ["Paid Sick Leave Available"], "US-WAS5-005"),
    ("fit", "Federal income tax withheld", ["Federal Income Tax Withholding"], "US-FEDS5-001"),
    ("oasdi", "Social security tax", ["Social Security Tax"], "US-FEDS5-005"),
    ("medicare", "Medicare tax", ["Medicare Tax"], "US-FEDS5-005"),
    ("addl_medicare", "Additional Medicare Tax", ["Additional Medicare Tax"], "US-FEDS5-005"),
    ("pretax", "Pre-tax elective deferrals", ["Pre-tax Deduction Lines"], "US-FEDS5-029"),
]


def write_legal(LINES):
    for _i, _l, _m, rid in LEGAL:
        assert rid in S.REG, f"legal item register id {rid} not in the register"
    ln = LINES["United States (EN)"]
    terms = [{"cell": x["cell"], "sign": x["sign"], "code": x["code"]} for x in ln["lines"] if x["sign"] != 0]
    doc = {"items": [{"id": i, "label": l, "match": m, "register_id": r} for i, l, m, r in LEGAL],
           "reconciliation": {"sheet": "United States (EN)", "net": ln["net"], "terms": terms, "tolerance": 0.01}}
    json.dump(doc, open(os.path.join(S.RESEARCH, "PSL-legal-items.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)


def write_recon(LINES, specs):
    rows = []
    unmapped = 0

    def add(kind, ident, sheet, cell, code, label, dd, hrp, why=""):
        nonlocal unmapped
        in_wtc = (code in K.WTC) if code else None
        dd_ok = all(n in K.DD for n in dd) if dd else None
        status = "MAPPED"
        if code and not in_wtc:
            status = "UNMAPPED_WTC"
        elif dd and not dd_ok:
            status = "UNMAPPED_DD"
        elif kind == "SPEC_FIELD" and not dd and not hrp:
            status = "UNMAPPED_NO_SOURCE"
        elif not dd and why:
            status = "MAPPED_NO_DD_FIELD"
        if status.startswith("UNMAPPED"):
            unmapped += 1
        rows.append([kind, ident, sheet, cell, code or "", label, "Y" if in_wtc else ("" if in_wtc is None else "N"),
                     "; ".join(dd), ("Y" if dd_ok else "" if dd_ok is None else "N"), hrp, why, status])

    for sh, info in LINES.items():
        for x in info["lines"]:
            lab = K.CW[x["code"]]["label"]
            side = K.CW.get(x["code"], {}).get("side", "NONE")
            dd, why = K.dd_for(x["code"], lab, side)
            add("EXAMPLE_LINE", f"{sh}!{x['cell']}", sh, x["cell"], x["code"], lab, dd, "$payroll.line." + x["code"], why)
    for code, label, sec, side in K.catalogue():
        dd, why = K.dd_for(code, label, side)
        add("CATALOGUE_LINE", f"Field Option!PAYSLIP_LINE {code}", "Field Option", "", code, label, dd, "$payroll.line." + code, why)
    for f in specs:
        add("SPEC_FIELD", f"Payslip Spec!{f['en']}", "Payslip Spec", "", f.get("wtc") or "", f["en"], f["dd"], f["hrp"],
            "" if f["dd"] else "system or payroll-calculated field; not a DD master-data field")
    with open(os.path.join(S.CHECKS, "psl_recon.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["kind", "id", "sheet", "cell", "wtc_code", "label", "in_wtc", "dd_fields", "dd_found", "hrp_mapping", "note", "status"])
        w.writerows(rows)
    import collections
    cnt = collections.Counter((r[0], r[-1]) for r in rows)
    print("recon rows", len(rows), dict(cnt), "UNMAPPED", unmapped)
    return unmapped


def write_all(info, REQ, LINES, wb, out):
    n = write_bindings()
    write_requests(REQ)
    write_legal(LINES)
    um = write_recon(LINES, info["specs"])
    print("bindings", n, "requests", len(REQ), "unmapped", um)

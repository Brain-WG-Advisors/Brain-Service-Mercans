# -*- coding: utf-8 -*-
"""Writes _research/RSPEC-research-request.json (contract research-request 1.4.0) from the
builder's open points (RSPEC-RQ-nn tags found in the workbooks) and 04-reports-spec/_build/
filing_crosswalk.json. usage: python write_requests.py

The file is merged, never overwritten: requests answered by agent 2 keep their _status /
_closed_* / _resolution_note fields; a closed request whose tag is still written in a workbook
stops the script; a documented limitation keeps its tag (location refreshed); a tag with no
request yet becomes a new request."""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import us_common as C  # noqa: E402
from openpyxl import load_workbook  # noqa: E402
from c44_mapped import CROSSWALK  # noqa: E402

G = re.compile(r"\[\[GAP:(RSPEC-RQ-\d+)\]\]")
REQ = {
    "RSPEC-RQ-01": ("rspec.fed.form941.line_map",
                    "What are the line numbers and line labels of the 2026 Form 941 and Form 944 (including the monthly / semiweekly liability detail and Schedule B), per the IRS 2026 forms and instructions?",
                    "US-IRS-001 / US-IRS-002 name the amounts of the field model but cannot cite the form lines; the provider mapping and the C38 recomputation of a full return depend on it",
                    "major", "a table line -> label -> amount definition, with register rows for the 2026 forms"),
    "RSPEC-RQ-02": ("rspec.fed.efw2.ra_rw_rt.layout_ty2026",
                    "What are the positions, lengths and formats of every field of the RA, RW and RT records, and the code lists of RE Kind of Employer, Employment Code, Tax Jurisdiction Code and Third-Party Sick Pay Indicator, in SSA Publication 42-007 for tax year 2026?",
                    "US-SSA-001 rows W2-003 and W2-007 to W2-019 have no positions or code lists; the EFW2 file cannot be generated field by field (the held PDF already carries them)",
                    "major", "one fact per record with 'field start-end' entries and one fact per code list"),
    "RSPEC-RQ-03": ("rspec.fed.w2.box_map",
                    "Which Form W-2 box carries each amount (wages, FIT, social security wages and tax, Medicare wages and tax, tips) and what is the Treasury Tipped Occupation Code list, per the 2026 General Instructions for Forms W-2 and W-3?",
                    "US-SSA-001 rows W2-014 to W2-021 cannot name the box; the option list of box 14b is empty",
                    "major", "box -> amount table and the code list, with register rows"),
    "RSPEC-RQ-04": ("rspec.fed.form943.line_map_due",
                    "What are the lines and the due date of the 2026 Form 943 (agricultural employees), per the IRS 2026 Form 943 and instructions?",
                    "US-IRS-003 carries no due date and no line map", "major", "due date + line table with register rows"),
    "RSPEC-RQ-05": ("rspec.fed.form1042s.wage_codes",
                    "Which income code, exemption code and treaty-article boxes of the 2026 Form 1042-S apply to treaty-exempt wages of nonresident alien employees, per the 2026 Instructions for Form 1042-S?",
                    "US-IRS-006 row F1042S-006 has no codes", "major", "code list per box with register rows"),
    "RSPEC-RQ-06": ("rspec.fed.aca.form1095c.line_codes",
                    "What are the 2026 Form 1095-C line 14 / 15 / 16 codes and the 1094-C lines, per the 2026 Instructions for Forms 1094-C and 1095-C?",
                    "US-IRS-007 row ACA-007 has no codes", "major", "code list per line with register rows"),
    "RSPEC-RQ-07": ("rspec.fed.form941x.line_map",
                    "What are the lines of the 2026 Form 941-X and how does the employer choose between the adjustment process and the claim process, per the IRS 2026 Form 941-X instructions?",
                    "US-IRS-008 cannot name lines or the process choice", "major", "line table + process rule with register rows"),
    "RSPEC-RQ-08": ("rspec.fed.form940.line_map_credit_reduction",
                    "What are the lines of the 2026 Form 940 and Schedule A, and which States are credit-reduction States for 2026 with which reduction, per the IRS and the U.S. Department of Labor?",
                    "US-IRS-004 rows F940-006 and F940-009 cannot apply a credit reduction", "major",
                    "line table + list of States with reduction percentage and effective year"),
    "RSPEC-RQ-09": ("rspec.fed.schedule_h.employer_statement",
                    "What annual amounts must be handed to a household employer for Schedule H (FICA wages, FUTA wages, FIT withheld), per IRS Publication 926 (2026)?",
                    "US-IRS-005 row SCHH-005 has no statement content", "minor", "list of statement amounts with register row"),
    "RSPEC-RQ-11": ("rspec.wv.local.service_fee_returns",
                    "Which West Virginia municipalities levy a municipal service fee collected through payroll, and what are the return form, channel and due dates of each, per the municipal ordinances?",
                    "US-LOC-001 WV section has only the Charleston weekly fee; no return parameters", "major",
                    "one fact per municipality: fee, return, channel, due date"),
    "RSPEC-RQ-12": ("rspec.pa.local.pittsburgh_payroll_expense.return",
                    "What are the form, channel and due dates of the City of Pittsburgh payroll expense tax return, per the City of Pittsburgh Department of Finance?",
                    "US-LOC-002 PA section has the rate only", "major", "form + channel + due dates with register rows"),
    "RSPEC-RQ-13": ("rspec.wa.local.seattle.base_thresholds_due",
                    "What are the 2026 base, thresholds and quarterly due dates of the Seattle Payroll Expense Tax and the Social Housing Tax, per SMC 5.38 and the City of Seattle FAS pages?",
                    "US-LOC-003 rows SEA-C-001 and SEA-C-002 cannot compute the taxes; due dates absent", "major",
                    "thresholds (USD) and rates per tier with effective_from, plus due dates"),
    "RSPEC-RQ-14": ("rspec.ny.mctmt.rates_lines",
                    "What are the 2026 MCTMT rates by zone and payroll band and the lines of Form MTA-305, per the NY DTF instructions?",
                    "US-DOR-004 NY section cannot compute the MCTMT", "major", "rate table by zone and band with effective_from"),
    "RSPEC-RQ-15": ("rspec.fed.efw2.ro_ru.layout_ty2026",
                    "What are the positions, lengths and formats of every field of the RO (employee optional) and RU (total optional) records of SSA Publication 42-007 for tax year 2026, beyond the tax-year 2026 money fields and allocated tips already carried?",
                    "US-SSA-001 rows W2-RO-900 and W2-RU-900: the RO / RU records cannot be generated field by field for box 12 codes outside the 2026 split fields (the held PDF carries them)",
                    "minor", "one fact per record with 'start-end name' entries covering positions 1-512, as for RA / RE / RW / RT"),
}


def main():
    locs = {}
    for p in sorted(glob.glob(os.path.join(C.SPECS, "*-Spec.xlsx"))):
        wb = load_workbook(p)
        for ws in wb.worksheets:
            for row in ws.iter_rows():
                for c in row:
                    if isinstance(c.value, str):
                        for g in G.findall(c.value):
                            locs.setdefault(g, f"04-reports-spec/{os.path.basename(p)}!{ws.title}!{c.coordinate}")
    # merged, never overwritten: answered requests keep agent 2's _status / _closed_* / _resolution_note
    path = os.path.join(C.RESEARCH, "RSPEC-research-request.json")
    old = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else {}
    have = {q["id"]: q for q in old.get("requests", [])}
    reqs = []
    for rq in sorted(set(have) | {"RQ-" + g.split("-")[-1] for g in locs}):
        g = "RSPEC-RQ-" + rq.split("-")[-1]
        q = have.get(rq)
        if q is not None:
            if q.get("_status") == "closed" and g in locs:
                raise SystemExit(f"{g} is closed by agent 2 but still written at {locs[g]}")
            if g in locs:
                q = dict(q, location=locs[g])
            reqs.append(q)
            continue
        if g not in REQ:
            raise SystemExit(f"open point {g} has no request text")
        key, qq, why, sev, shape = REQ[g]
        reqs.append({"id": rq, "key": key, "location": locs[g], "question": qq, "why_blocking": why,
                     "domain": "statutory_reporting", "acceptable_tier": "A.2", "severity": sev, "expected_shape": shape,
                     "attempted_by_requester": [f"_research/RSPEC-facts.json (all {len(set(C.RSPEC_KEYS))} keys read)",
                                                "_research/RSPEC-research-pack.md",
                                                "other _research/*-facts.json files searched by key and value"],
                     "_deliverable_tag": f"[[GAP:{g}]]"})
    out = dict(old) if old else {"schema_version": "1.4.0", "artifact": "RSPEC", "requested_by": "artifact-builder",
                                 "round": 1, "created_on": "2026-11-03"}
    out["_note"] = ("Non-blocking open points of the RSPEC build round 1, rebuilt on 2026-11-03 with the RQ facts. Closed "
                    "requests keep agent 2's resolution fields; the documented limitations RQ-08, RQ-11 and RQ-12 stay cited "
                    "in the workbooks for their open part; RQ-15 (RO / RU layouts) is new. The limitations recorded in "
                    "gaps.json -> RSPEC are cited by their RSPEC-GAP ids and are not repeated here.")
    out["requests"] = reqs
    json.dump(out, open(path, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    sm = C.SCOPE["authority_filings"]["in_scope"]
    cw = [{"filing_id": f["filing_id"], "spec_doc_id": d,
           "spec_file": next(os.path.basename(p) for p in glob.glob(os.path.join(C.SPECS, f"{d}-*-Spec.xlsx")))}
          for f, d in zip(sm, CROSSWALK)]
    json.dump({"_note": "One Report Specification per in-scope filing of scope_manifest.json (same order).", "crosswalk": cw},
              open(os.path.join(HERE, "filing_crosswalk.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(len(reqs), "requests;", len(cw), "crosswalk rows")


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""Writes the DESIGN limitations: entries DESIGN-RQ-nn in _research/gaps.json (idempotent) and
_research/DESIGN-research-request.json. Run after build_design.py (reads checks/design_refs.json)."""
import json
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import design_common as C  # noqa: E402

refs = json.load(open(os.path.join(C.CHECKS, "design_refs.json"), encoding="utf-8"))
sts = ", ".join(refs["new_employer_gap_states"])
LOC = f"09-design/{C.FILENAME}"
SEARCHED = ["_research/*-facts.json (every key of the jurisdiction or topic)",
            "01-ccg/modules and annexes (text of the CCG)", "05-data-dictionary/US-DD-001-v1.0.xlsx (field list)"]
ITEMS = [
    ("DESIGN-RQ-01", "design.ut.wh.table_before_2026_04_01", "income_tax", "minor",
     "Utah withholding table for payment dates before 2026-04-01: the research carries the table in force from that date only",
     f"{LOC}!Part 1!flag 58421, Part 6 item 1",
     "Utah State Tax Commission withholding publication in force for January to March of the build year, entered as dated facts with a register row"),
    ("DESIGN-RQ-02", "design.fed.w4.pre2020_and_nra_table1", "income_tax", "major",
     "Federal withholding for an employee on a Form W-4 before the 2020 revision (allowance method and nonresident alien Table 1): the Data Dictionary has no field for the form revision or the allowance count",
     f"{LOC}!Part 4!9840024 and 9840021, Part 6 item 2",
     "Owner decision to add the form-revision and allowance fields to the Data Dictionary; the values are already in the facts"),
    ("DESIGN-RQ-05", "design.fed.employee_abroad.statement", "income_tax", "minor",
     "Statement that stops federal income tax withholding for a citizen working abroad: the Data Dictionary has no field for the statement",
     f"{LOC}!Part 4!9840021, Part 6 item 5",
     "Owner decision to add the statement indicator and its date to the Data Dictionary"),
    ("DESIGN-RQ-06", "design.sui.new_employer_rate.single_number", "social_security", "minor",
     f"New-employer unemployment rate carried as one number for each State: not available for {sts}",
     f"{LOC}!Part 4.4!jurisdiction register, Part 6 item 6",
     "State agency rate notice or the State's new-employer rule for each listed State, entered as dated facts with a register row"),
    ("DESIGN-RQ-07", "design.programme_rows_without_parameter", "social_security", "minor",
     "Wyoming workers' compensation (employer-specific rate), New York MCTMT rate and the Iowa school district tax: the research carries no value and the catalogue has no Iowa school district row",
     f"{LOC}!Part 4!9840053 and 9840061, Part 6 item 12",
     "Wyoming workers' compensation rate rule, the New York MCTMT rate table and the Iowa school district rate page, entered as dated facts with register rows; an Iowa school district catalogue row for the owner to add"),
    ("DESIGN-RQ-08", "design.programme_parameters_without_2027_value", "social_security", "minor",
     "State programme parameters with no entry for 2027 (" + ", ".join(refs.get("no_2027_parameters", [])) + ")",
     f"{LOC}!Part 4!9840053, Part 6 item 13",
     "The 2027 rate or cap of each listed programme from the State agency, entered as dated facts with a register row"),
]
gp = os.path.join(C.RESEARCH, "gaps.json")
g = json.load(open(gp, encoding="utf-8"))
g["gaps"] = [x for x in g["gaps"] if not x["id"].startswith("DESIGN-RQ-")]
DDCR = {"DESIGN-RQ-02": {"dd_change_request_1_1": "Add to the Data Dictionary 1.1: Form W-4 revision (before 2020 or 2020 and later) and the number of allowances, on the employee; the allowance value and Table 1 amounts are already carried by the research", "fallback": "Employees first paid before 2020 with no 2020 or later Form W-4 are handled manually in package 1.0"},
        "DESIGN-RQ-05": {"dd_change_request_1_1": "Add to the Data Dictionary 1.1: Form 673 statement indicator and its effective dates, on the employee", "fallback": "A citizen abroad who holds a Form 673 statement is withheld normally in package 1.0"}}
for cid, why, keys in (("DESIGN-RQ-03", "Supplemental wage withholding method election: the Data Dictionary now carries the legal-entity field and the design derives flag 58414 with a default rule", ["fed.fit.supplemental.aggregate_method"]),
                       ("DESIGN-RQ-04", "State-assigned unemployment insurance rate: the Data Dictionary now carries the legal-entity field, read by 9840052 through flag 58429; the notification mechanism per State stays in DD-RQ-11", ["fed.fit.supplemental.aggregate_method"])):
    g["gaps"].append({"id": cid, "key": "design.closed." + cid.lower(), "subject": f"{cid} - {why}", "location": f"{LOC}!Part 6!items 3 and 4",
                      "research_request_id": cid, "blocking": False, "severity": "minor", "searched": SEARCHED, "searched_on": "2026-11-04",
                      "what_would_close_it": why, "status": "closed", "closed_on": "2026-11-04", "closed_by_keys": keys,
                      "closed_by_register_ids": ["US-FEDS5-003"], "closure_source": why, "decided_by": "DESIGN fix round 1"})
for rid, key, dom, sev, subj, loc, close in ITEMS:
    g["gaps"].append({
        "id": rid, "key": key, "subject": f"{rid} - {subj}", "location": loc, "research_request_id": rid,
        "blocking": False, "severity": sev, "searched": SEARCHED, "searched_on": "2026-11-04",
        "what_would_close_it": close, "status": "documented_limitation",
        "reason": "not carried by the research facts or the approved Data Dictionary at the build date",
        "closure_source": close, "decided_by": "DESIGN build", **DDCR.get(rid, {})})
cnt = {}
for x in g["gaps"]:
    cnt[x["status"]] = cnt.get(x["status"], 0) + 1
cnt["total"] = len(g["gaps"])
g["counts"] = cnt
json.dump(g, open(gp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)

req = {"schema_version": "1.4.0", "artifact": "DESIGN", "unit": "regulation_design", "requested_by": "artifact-builder",
       "round": 1, "created_on": "2026-11-04",
       "_note": "Open points of the design build. None blocks the design; each is a documented limitation written 'Not configured in this release [[GAP:DESIGN-RQ-nn]]'.",
       "requests": []}
for rid, key, dom, sev, subj, loc, close in ITEMS:
    req["requests"].append({
        "id": rid.replace("DESIGN-", ""), "key": key, "location": loc, "question": f"What closes the limitation: {subj}?",
        "why_blocking": "Documented limitation: the design states it in the neutral wording 'Not configured in this release' and writes no value.",
        "domain": dom, "acceptable_tier": "A.2", "attempted_by_requester": SEARCHED, "severity": sev if sev != "major" else "major",
        "expected_shape": close})
json.dump(req, open(os.path.join(C.RESEARCH, "DESIGN-research-request.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("gaps:", cnt, "requests:", len(req["requests"]))

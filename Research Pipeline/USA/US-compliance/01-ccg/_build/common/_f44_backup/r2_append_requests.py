# -*- coding: utf-8 -*-
"""Round 2 (QA r1): append research requests for RESEARCH-GAP markers the rebuilt CCG carries
without a request (new unresolved[] items added by agent 2 in its r1 pass). Idempotent by key.
gaps.json is agent 2's file and is NOT edited here; the new ids are routed to agent 2 so it adds
their gaps.json entries (C70).
usage: python r2_append_requests.py <BASE>"""
import json
import os
import sys

BASE = sys.argv[1]
P = os.path.join(BASE, "_research", "CCG-research-request.json")
doc = json.load(open(P, encoding="utf-8"))
have = {q["key"] for q in doc["requests"]}
nxt = max(int(q["id"].split("-")[1]) for q in doc["requests"]) + 1
NEW = [
    {"key": "fed.equity.nra.sourcing_period",
     "location": "01-ccg/annexes/annex_FED.md!FED.2b",
     "question": "What grant-to-vest (or other) period does 26 CFR 1.861-4(b)(2)(ii)(F) prescribe for the time-basis "
                 "sourcing of stock-option and RSU compensation of a nonresident alien employee, and how is it applied "
                 "for 2026 withholding?",
     "why_blocking": "Annex FED (FED.2b) states the time-basis sourcing rule from Pub. 515 but cannot state the period "
                     "for equity compensation; non-blocking, the matrix cell is written from fed.equity.withholding_treatment.nonresident.",
     "domain": "income_tax", "acceptable_tier": "A.1",
     "attempted_by_requester": ["_research/CCG-annex_FED-facts.json unresolved[] (fed.equity.nra.sourcing_period)"],
     "severity": "minor",
     "expected_shape": "rule text with the CFR paragraph, an active A.1 register row and verified_on",
     "_raised_by_unit": "annex_FED", "_origin": "unresolved[] item added by agent 2 in QA r1 (no request yet)",
     "_status": "open",
     "_what_would_close_it": "Full text of 26 CFR 1.861-4(b)(2)(ii)(F) on ecfr.gov or the govinfo CFR annual edition, title 26 vol. 9."},
    {"key": "vt.pit.wh.lower_brackets",
     "location": "01-ccg/annexes/annex_VT.md!VT.2",
     "question": "What are the 2026 Vermont withholding schedule bracket rates and base amounts below the top bracket "
                 "(single and married annual schedules of the 2026 withholding guide), as separate values?",
     "why_blocking": "Annex VT shows the bracket thresholds and the top rate as facts; the lower bracket rates and "
                     "base amounts were carried only inside a fact note, without keys (QA r1 C46 percent scan).",
     "domain": "income_tax", "acceptable_tier": "A.2",
     "attempted_by_requester": ["_research/CCG-annex_VT-facts.json facts[] (vt.pit.wh.single.thresholds note)"],
     "severity": "minor",
     "expected_shape": "one keyed fact per bracket rate and base amount, with unit, effective_from and an active register row",
     "_raised_by_unit": "annex_VT", "_origin": "round 2 rebuild: unkeyed percentages in a fact note",
     "_status": "open",
     "_what_would_close_it": "Vermont Department of Taxes 2026 withholding guide (annual percentage-method schedules)."},
    {"key": "in.oracle.dn1.example.county_rate",
     "location": "01-ccg/annexes/annex_IN.md!IN.14",
     "question": "Key the county rate used as the input of the Indiana Departmental Notice 1 (2026-10-01) worked example "
                 "as a fact, so the example's input is bound like its published results.",
     "why_blocking": "Annex IN reproduces the DN1 example; its results are keyed (in.oracle.dn1.example.*) but the "
                     "example county rate input is written as a number without a key.",
     "domain": "income_tax", "acceptable_tier": "A.2",
     "attempted_by_requester": ["_research/CCG-annex_IN-facts.json facts[] (in.oracle.dn1.example.*)"],
     "severity": "minor",
     "expected_shape": "in.oracle.dn1.example.county_rate in percent, register row of Departmental Notice 1",
     "_raised_by_unit": "annex_IN", "_origin": "round 2 rebuild: unkeyed example input (QA r1 C46 percent scan)",
     "_status": "open",
     "_what_would_close_it": "Indiana DOR Departmental Notice 1 (rev. 2026-10-01) example section."},
    {"key": "wa.leave.seattle_psst",
     "location": "01-ccg/annexes/annex_WA.md!WA.6",
     "question": "What do the Seattle Paid Sick and Safe Time ordinance (SMC 14.16) and its 2026 rules require of "
                 "payroll (accrual rate, carry-over, pay-statement balance, employer-size tiers)?",
     "why_blocking": "Annex WA (WA.6) states that the Seattle Paid Sick and Safe Time rules were not obtained; "
                     "the statement had no research request (QA r1 C70).",
     "domain": "leave", "acceptable_tier": "A.2",
     "attempted_by_requester": ["_research/CCG-annex_WA-research-pack.md (leave section)"],
     "severity": "minor",
     "expected_shape": "keyed facts per rule with an active register row",
     "_raised_by_unit": "annex_WA", "_origin": "round 2 rebuild: source-gap statement without a request",
     "_status": "open",
     "_what_would_close_it": "Seattle Office of Labor Standards PSST ordinance page and rules (seattle.gov)."},
]
# generic: every unresolved[] item of a CCG facts file whose key has no research request yet (items
# added by agent 2 or a parallel worker after the round-1 requests were written)
import glob  # noqa: E402
import re  # noqa: E402
# unresolved items the round-2 build answers or points elsewhere (no separate request):
#   fl/wy.no_wage_tax: answered by the annex facts fl.pit.exists / wy.pit.exists (m01 table)
#   state.holidays.legal: same question as RQ-555 (multi.holidays.state_2026)
#   fed.futa.credit_reduction.potential_2026: same question as RQ-402 / RQ-403 (Annex FED)
#   multi.*.remaining_states: one request per State already exists in Annex MULTI (RQ-412..442)
HANDLED = {"fl.no_wage_tax", "wy.no_wage_tax", "state.holidays.legal", "fed.futa.credit_reduction.potential_2026",
           "multi.sui.other_state_wage_credit.remaining_states", "multi.pfml.coverage_test.remaining_states"}
DOMAINS = {"income_tax", "social_security", "labour_code", "leave", "reporting", "benefits_in_kind",
           "deductions", "termination", "data_protection"}
for fp in sorted(glob.glob(os.path.join(BASE, "_research", "CCG-*-facts.json"))):
    unit = re.match(r"CCG-(.+)-facts\.json", os.path.basename(fp)).group(1)
    if unit == "coverage":
        continue
    loc = (f"01-ccg/annexes/{unit}.md" if unit.startswith("annex_") else f"01-ccg/modules/{unit}.md") + "!open research points"
    for u in json.load(open(fp, encoding="utf-8")).get("unresolved", []):
        if u["key"] in have or u["key"] in HANDLED or any(n["key"] == u["key"] for n in NEW):
            continue
        dom = next((d for d in DOMAINS if d.split("_")[0] in u["key"]), "labour_code")
        NEW.append({"key": u["key"], "location": loc,
                    "question": f"What does the official source establish for `{u['key']}` for 2026 (and 2027 where "
                                f"published)? Context: {u.get('why', '')}",
                    "why_blocking": f"{unit} writes this item as a RESEARCH-GAP marker (unresolved[] item without "
                                    "a research request).",
                    "domain": dom, "acceptable_tier": "A.2",
                    "attempted_by_requester": [f"_research/{os.path.basename(fp)} unresolved[] ({u['key']})"],
                    "severity": "blocker" if u.get("blocking") else "minor",
                    "expected_shape": "keyed value(s) with unit, effective_from and an active register row",
                    "_raised_by_unit": unit, "_origin": "round 2 rebuild: unresolved[] item without a request",
                    "_status": "open", "_blocking": bool(u.get("blocking")),
                    "_what_would_close_it": u.get("what_would_close_it", "")})
added = []
for q in NEW:
    if q["key"] in have:
        continue
    q = dict(q, id=f"RQ-{nxt:03d}")
    nxt += 1
    doc["requests"].append(q)
    added.append(q["id"] + " " + q["key"])
if added:
    json.dump(doc, open(P, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("added:", added)

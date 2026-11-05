# Run-close re-check (2026-11-04, after the B1/B2/B3 fixes): targeted reviews of the post-PASS rebuilds.
import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = "2026-11-04"
R = "compliance-qa-auditor (independent, run-close re-check)"
EV = "07-qa-crosscheck/_runclose/out/c41_c70_diff.txt; _runclose/c41_keys_verify.py; _runclose/sir_diff2.py"
loc = lambda f, s, c: {"file": f, "sheet_or_section": s, "cell_or_line": c}
reg_find = {"pattern": None, "severity": "major", "pass": "P2",
            "location": loc("00-official-sources/legal-basis-register.csv", "row US-RIS5-008", "effective_from / instrument_name / status"),
            "problem": "Row names 'RIGL 28-14-12 (version effective until 2026-01-01)' but the C41/C70 fix set effective_from 2026-11-02 (retrieval) and cleared effective_to, so the row now claims the old version is in force from 2026-11-02. Same pattern, without the false start date, on US-OHR3C-001 (true end 2026-06-15) and US-OHP52-001 (true end 2026-07-31): end dates moved into verification_method text only.",
            "expected": "Keep the true period on closed-period sources (US-RIS5-008 to 2025-12-31 with the version start from the copy or blank+basis; OHR3C-001 to 2026-06-15; OHP52-001 to 2026-07-31) with status 'historical', and have the shared C41 skip 'historical' like 'superseded' (C70 already ignores it). Until then the active+cleared workaround is accepted only because the facts carry the correct periods (period-aware C46 0 mismatches). US-FEDS5-013, US-CAS5-020 and US-INP51-001 are correctly active (current authority for TY2025 / no successor notice).",
            "register_id": "US-RIS5-008", "action": "routed_to_source_hunter"}
ccg = {"schema_version": "1.4.0", "artifact": "CCG", "round": 3, "verdict": "PASS", "reviewed_on": D,
 "_file_round": "r6 = run-close targeted re-check of the C41 rebuild (m10 'Changes during 2026'); schema caps round at 3",
 "_reviewed_file": "01-ccg/US-CCG-001-v1.0.docx md5 2bdf6f88ebcaa31c6ee743f0ba458096 (vs pre-c41 copy: 11 added lines, all in the m10 table; vs pre-c70 copy: 0 text changes)",
 "_reviewer": R,
 "findings": [reg_find,
  {"pattern": None, "severity": "minor", "pass": "P2", "location": loc("01-ccg/US-CCG-001-v1.0.docx", "Module 6 and Module 13, SC practice row", "Sources cell"),
   "problem": "Still cites only [US-SCS5-004] for the IL 26-20 schedule (carried from CCG-review-r5).", "expected": "[US-SCS5-004; US-SCS5-005] at the next CCG build.",
   "register_id": "US-SCS5-005", "action": "routed_to_builder"}],
 "checks_run": ["C29", "C38", "C40", "C41", "C46", "C69", "C70"], "_checks_run_other": ["F44", "G-DERIVE", "G-PROP"],
 "numeric_verification": {"facts_total": 6, "facts_verified": 6, "unverified_keys": [],
  "method": "m10 table keys checked in the registered copies: futa.credit_reduction 2025 CA 1.2 / VI 4.5 in US-FEDS6-009 (Schedule A 2025); 941ME in US-MEP52-002; M-5008-R (6/26) in US-NJR3-004; D-2848 in US-DCP51-014; C-42 in US-TXP52-008; Form 940 TY2025 'February 2, 2026' / 'February 10' in US-FEDS5-031. Successor period re-derived (G-DERIVE): Jan 31 2027 is a Sunday -> February 1, 2027; Feb 10 2027 is a Wednesday; labelled low-confidence carry-forward."},
 "_evidence": EV}
rspec = {"schema_version": "1.4.0", "artifact": "RSPEC", "round": 3, "verdict": "PASS", "reviewed_on": D,
 "_file_round": "r3d = run-close targeted re-check of DOR-001 and IRS-004 (C41 rebuild)", "_reviewer": R,
 "_reviewed_file": "04-reports-spec/US-DOR-001 (3 cells: ME 941ME '(from 2026-04-14)') and US-IRS-004 (7 cells: Form 940 successor rule, credit-reduction labelled 'wages of 2025'); other 18 workbooks 0 text changes; md5 22/22 = md5_final; C71 0 differences",
 "findings": [{"pattern": "F27", "severity": "major", "pass": "P5",
   "location": loc("04-reports-spec/US-IRS-004-Form940-Spec.xlsx", "Report Matrix", "B11 / F27"),
   "problem": "The RSPEC prints the TY2026 Form 940 due rule (successor period, 'February 1, 2027 ... per the 2025 instructions' rule', low confidence), while the SIR row US-IRS-004 now prints 'Not configured in this release' for the same return because its F44 self-check finds that wording absent from the 2025 copy. Same fact, two treatments.",
   "expected": "One treatment in both: either both print the labelled carry-forward (derivation is correct: Jan 31 2027 Sunday -> Feb 1) or both print the gap; align at the next SIR/RSPEC build and mirror the same day (F27).",
   "register_id": "US-FEDS5-031", "action": "routed_to_builder"}],
 "checks_run": ["C29", "C46", "C53", "C56", "C71"],
 "numeric_verification": {"facts_total": 3, "facts_verified": 3, "unverified_keys": [], "method": "Same keys as CCG-review-r6 (form940.due x2 periods, futa.credit_reduction.states, me.wh_return.form); copies checked by c41_keys_verify.py."},
 "_evidence": EV}
sir = {"schema_version": "1.4.0", "artifact": "SIR", "round": 3, "verdict": "PASS", "reviewed_on": D,
 "_file_round": "r4 = run-close targeted re-check of the C41/C70 SIR rebuild", "_reviewer": R,
 "_reviewed_file": "03-statutory-integrations/US-SIR-INDEX-001-v1.0.docx (22/22 = md5_final). 218 raw changed lines = SIR-RQ ids renumbered +2 (two new requests at the front); with ids masked, 22 changed lines: NJ/DC/TX '(from date)', Form 940 rule -> gap, Ohio school district code -> gap (US-OHS5-019 2025 list now superseded), new DD element row (supplemental method), source-list rows. gaps.json and the skill use the new numbering consistently (SIR-RQ-29 = provider selection).",
 "findings": [{"pattern": None, "severity": "minor", "pass": "P4", "location": loc("03-statutory-integrations/US-SIR-INDEX-001-v1.0.docx", "Section 8 DD element table", "Ohio school district code"),
   "problem": "SIR now shows the Ohio code as a gap (SIR-RQ-02) while DD W96 and RSPEC still print the 4-digit/9999 rule with the DD limitation note; consistent in substance, different in form.",
   "expected": "Keep; at the next SIR build print the DD limitation wording instead of a bare gap so the three artifacts read the same.", "register_id": "US-OHB5-401", "action": "routed_to_builder"}],
 "checks_run": ["C29", "C46", "C53", "C70"],
 "numeric_verification": {"facts_total": 4, "facts_verified": 4, "unverified_keys": [], "method": "NJ/DC/TX authorisation forms and form940.due checked in the registered copies (c41_keys_verify.py)."},
 "_evidence": EV}
skill = {"schema_version": "1.4.0", "artifact": "SKILL", "round": 3, "verdict": "PASS", "reviewed_on": D,
 "_file_round": "r5 = targeted F28 re-check after the human-approved regeneration (round 5 in SKILL-build-log)", "_reviewer": R,
 "_reviewed_file": "../skills-build/payroll-compliance-united-states/ 99/99 = _pipeline/SKILL-md5.txt; built 14:57 after CCG 2bdf6f88 (14:47), DD (14:47), SIR (14:52)",
 "findings": [],
 "checks_run": ["C29"], "_checks_run_other": ["F28"],
 "numeric_verification": {"facts_total": 7, "facts_verified": 7, "unverified_keys": [],
  "method": "SKILL-review-r4 items: old practice wording (OPB report / up to 0.48/period / statute flat 2.75 / Use WH-1603 tables) 0 hits in 01-ccg/m06_tax.md, m13_practices.md, 13-gotchas.md; GA new wording 2; DD elements 'Supplemental wage withholding method election' 1 and 'State-assigned unemployment insurance rate' 1; MA 'wages earned on or after January 1' 2; m10 'Changes during 2026' present. Skill selfcheck (C29/WORD/PATH/NOTES/NUM 0) and selfcheck_strict (10,485 rows, VAL/PERIOD/HAND 0) re-run by the auditor; outputs identical to the builder's."}}
for name, doc in [("CCG-review-r6", ccg), ("RSPEC-review-r3d", rspec), ("SIR-review-r4", sir), ("SKILL-review-r5", skill)]:
    json.dump(doc, open(os.path.join(BASE, "_qa", name + ".json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("ok")

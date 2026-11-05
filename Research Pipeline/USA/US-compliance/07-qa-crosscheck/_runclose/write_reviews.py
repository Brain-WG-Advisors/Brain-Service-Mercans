# Run-close review files (compliance-qa-auditor, 2026-11-04): CCG targeted re-check of the post-design rebuild, SKILL F28 re-sync.
import json, os
HERE = os.path.dirname(os.path.abspath(__file__)); BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
D = "2026-11-04"
ccg = {
 "schema_version": "1.4.0", "artifact": "CCG", "round": 3, "verdict": "PASS", "reviewed_on": D,
 "_file_round": "r5 = run-close targeted re-check of the CCG rebuilt after the DESIGN fact re-sync (no review existed for this build); schema caps round at 3",
 "_reviewed_file": "01-ccg/US-CCG-001-v1.0.docx (md5 b9de40ce69edefd94c76439261c3318b; previous reviewed builds bbdcf053 (r4) -> ffa24c2e (SKILL r4 annex_LA))",
 "_reviewer": "compliance-qa-auditor (independent, run close)",
 "findings": [
  {"pattern": None, "severity": "minor", "pass": "P2",
   "location": {"file": "01-ccg/US-CCG-001-v1.0.docx", "sheet_or_section": "Module 6 practice table (row SC) and Module 13 13.1 (row SC)", "cell_or_line": "Sources cell of the practice.sc.withholding_rates_2026 row"},
   "problem": "The row now prints the Act 110 2026 schedule '1.99% (0-29,999) / 5.21% minus 966 (30,000+)' taken from SCDOR Information Letter #26-20, but its Sources cell cites only [US-SCS5-004] (WH-1603 tables), whose local copy does not contain 1.99 or 5.21. The fact carries _also_register_ids US-SCS5-005 (IL 26-20, local copy contains 1.99, 5.21, 966, 29,999, 30,000).",
   "expected": "Sources cell reads [US-SCS5-004; US-SCS5-005] (generator: print _also_register_ids for practice rows). Fix at the next CCG build; no value changes.",
   "register_id": "US-SCS5-005", "action": "routed_to_builder"}
 ],
 "checks_run": ["C11", "C29", "C38", "C40", "C46", "C69", "C70"], "_checks_run_other": ["F44", "G-PROP", "G-SPOT"],
 "numeric_verification": {"facts_total": 6, "facts_verified": 6, "unverified_keys": [],
  "method": "Docx text diff vs _pipeline/_backup/pre-m13-2026-11-04 (ffa24c2e): 23 changed lines, all tags of 6 keys (practice.ga/sc/ne/oh/ct + ma.pfml.rate.selection_basis), no other text. Each value checked in the registered local copy by 07-qa-crosscheck/_runclose/ccg_r5_verify.py: GA 4.99/5.19/0.125/3.99 in US-GAS5-009 (HB 463); NE 2.26/4.60/4.55 in US-NES5-010; OH 2.99/3.4/1.6 in US-OH-006 (cited inline) and 2.75 in US-OHS5-007; CT quote in US-CTS5-010 (TPG-211); MA 'January 1' in US-MAS5-012; SC 1.99/5.21/966 in US-SCS5-005 (_also id; see minor finding). tag_sync 0 stale (7,924 CCG tags); period-aware C46 0 mismatches."},
 "cross_checks": [
  {"name": "Docx diff vs pre-m13 copy", "result": "pass", "note": "Only the declared fact-bound lines (m06 practice table, m12 SC row note, m13, annex_MA new row) changed; matches _research/design-fix/CCG-READY.md."},
  {"name": "C38 worked examples (--module all, facts, specs)", "result": "pass", "note": "927 tables, 55 results recomputed, 0 mismatches"},
  {"name": "Tier verdict wording", "result": "pass", "note": "build-manifest tier.rationale == scope_manifest tier.verdict_verbatim and is present verbatim in the CCG docx (3,373 characters)"}
 ],
 "propagation": [
  {"fact": "practice.ga.rate_change_2026", "consumed_by": ["CCG/m06_tax", "CCG/m13_practices", "DESIGN", "SKILL"], "resynced": False},
  {"fact": "ma.pfml.rate.selection_basis", "consumed_by": ["CCG/annex_MA", "DESIGN", "SKILL"], "resynced": False}
 ],
 "_propagation_note": "CCG and DESIGN carry the current values; SKILL references do not (see SKILL-review-r4.json).",
 "_next_action": "none for the CCG this run (minor fixed at the next CCG build)"
}
skill = {
 "schema_version": "1.4.0", "artifact": "SKILL", "round": 3, "verdict": "FAIL", "reviewed_on": D,
 "_file_round": "r4 = run-close F28 re-check after upstream changes (CCG b9de40ce, DD f65dc9bc) made after SKILL r3b PASS; schema caps round at 3",
 "_reviewed_file": "../skills-build/payroll-compliance-united-states/ (99 files = _pipeline/SKILL-md5.txt, all match; built 2026-11-04 12:30)",
 "_reviewer": "compliance-qa-auditor (independent, run close)",
 "findings": [
  {"pattern": "F28", "severity": "blocker", "pass": "P5",
   "location": {"file": "../skills-build/payroll-compliance-united-states/references/01-ccg/m13_practices.md", "sheet_or_section": "13.1 practice table and fact index", "cell_or_line": "lines 23, 30, 31, 34, 84, 88, 94, 96"},
   "problem": "Skill references still print the superseded practice wording for SC, CT, OH, GA (and NE): e.g. GA '2027 0.125-point step conditional on OPB report of 2026-12-01', CT 'results differ up to 0.48/period', OH 'statute flat 2.75% but withholding tables graduated to 3.4%'. The CCG was rebuilt at 13:29 (md5 b9de40ce) with the re-synced facts; the skill was built at 12:30 from the earlier CCG (ffa24c2e). Same stale lines in references/01-ccg/m06_tax.md (258, 272, 276, 279, 645, 649, 654, 656) and references/13-gotchas.md (23, 28, 86, 90).",
   "expected": "references/ hold the latest artifact versions verbatim: re-run the skill generator from CCG b9de40ce, then selfcheck/selfcheck_strict and refresh _pipeline/SKILL-md5.txt and references/07-qa-report.md.",
   "register_id": "US-GAS5-009", "action": "escalated_to_human"},
  {"pattern": "F28", "severity": "blocker", "pass": "P5",
   "location": {"file": "../skills-build/payroll-compliance-united-states/references/05-data-dictionary.md", "sheet_or_section": "ID Information", "cell_or_line": "whole file (0 hits for the two new elements)"},
   "problem": "The DD gained two legal-entity elements after the skill build (DD md5 f65dc9bc, 13:15): 'Supplemental wage withholding method election' and 'State-assigned unemployment insurance rate' (DD-RQ-11). The skill's DD reference has neither, and references/12-states/MA.md lacks ma.pfml.rate.selection_basis.",
   "expected": "Regenerate references/05-data-dictionary.md and 12-states/MA.md from the current DD and CCG in the same rebuild.",
   "register_id": "US-MAS5-012", "action": "escalated_to_human"}
 ],
 "checks_run": ["C29"], "_checks_run_other": ["F28", "G-PROP", "G-SPOT"],
 "numeric_verification": {"facts_total": 0, "facts_verified": 0, "unverified_keys": [], "method": "No new number in the skill; the defect is staleness against approved artifacts."},
 "escalation": {
  "reason": "The SKILL already used its three rounds (r1, r2, r3/r3b PASS). These defects come from upstream changes after its PASS, so a fourth round is not allowed; a mechanical regeneration needs a human go-ahead.",
  "decision_needed": "Approve one bounded regeneration of the skill from the current CCG/DD (no research, no value change) followed by a targeted F28 check outside the round count, as was done for RSPEC r3b/r3c.",
  "_recommendation": "Approve. Builder re-runs build_skill.py + selfcheck + selfcheck_strict, refreshes SKILL-md5.txt; auditor checks the diff equals the CCG/DD diff."
 },
 "_next_action": "human decision, then artifact-builder skill regeneration and a targeted F28 re-check"
}
json.dump(ccg, open(os.path.join(BASE, "_qa", "CCG-review-r5.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump(skill, open(os.path.join(BASE, "_qa", "SKILL-review-r4.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("written")

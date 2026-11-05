# Run-close re-check 3 (2026-11-04): F27 + minor fixes (pre-f27 copy), skill round 6 (pre-skill-b4 copy).
import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
D = "2026-11-04"; R = "compliance-qa-auditor (independent, run-close re-check 3)"
loc = lambda f, s, c: {"file": f, "sheet_or_section": s, "cell_or_line": c}
lim = {"pattern": None, "severity": "minor", "pass": "P2",
       "location": loc("03-statutory-integrations/_build/f44_lib.py", "LIMITATION_KEYS", "lines 228-252"),
       "problem": "The F44 self-check skips ALL elements of rspec.fed.form940.due and dd.oh.school_district_code, whatever their value. Today the skip is safe: the auditor found the verifiable elements in the cited copies (US-FEDS5-031: 'February 2, 2026', 'February 10'; US-OHS5-019: '9999'), the derived TY2026 dates re-derive (Jan 31 2027 Sunday -> Feb 1; Feb 10 2027 Wednesday), and both printed values carry their limitation wording. But a later change of either value would pass F44 unchecked.",
       "expected": "Accepted for package 1.0. At the next SIR build, pin the skip to the current value (key + value hash) or skip only the derived elements, so any new wording is checked again.",
       "register_id": "US-FEDS5-031", "action": "routed_to_builder"}
sir = {"schema_version": "1.4.0", "artifact": "SIR", "round": 3, "verdict": "PASS", "reviewed_on": D,
 "_file_round": "r5 = targeted re-check of the F27/minor fix (RC-4, RC-6) against _pipeline/_backup/pre-f27-2026-11-04/", "_reviewer": R,
 "_reviewed_file": "03-statutory-integrations/US-SIR-INDEX-001-v1.0.docx (22/22 = md5_final). 208 raw changed lines = SIR-RQ ids renumbered -2 (the two F44 gaps removed); ids masked: 12 lines, all mapped: Form 940 rows print [[FACT:rspec.fed.form940.due]] (same text as RSPEC IRS-004), OH school district prints the fact + the DD limitation sentence, 4 source-list rows, 2 gap rows removed. gaps.json (39 SIR-RQ) and skill 14-known-gaps agree id by id (0 mismatches).",
 "findings": [lim], "checks_run": ["C29", "C46", "C53", "C70"],
 "numeric_verification": {"facts_total": 2, "facts_verified": 2, "unverified_keys": [], "method": "Both tags checked by hand in the registered copies and by G-DERIVE (see finding). SIR f44_self: 409 tags, 0 misses."},
 "_closes": ["RC-4 (F27 RSPEC x SIR Form 940): closed", "RC-6 (SIR Ohio school district wording): closed"]}
ccg = {"schema_version": "1.4.0", "artifact": "CCG", "round": 3, "verdict": "PASS", "reviewed_on": D,
 "_file_round": "r7 = targeted re-check of the citation fix (RC-1) against pre-f27 copy", "_reviewer": R,
 "_reviewed_file": "01-ccg/US-CCG-001-v1.0.docx md5 333e8ee60a3d97a9b229b859c4f5da7c. 24 changed lines, citation cells only (tag text unchanged): practice rows SC, WI, NE, OH, CT, MA in m06 and m13 now cite their _also rows; m05 MA PFML decision line cites US-MAS5-012; US-MAS5-026.",
 "findings": [], "checks_run": ["C29", "C38", "C41", "C46", "C70"],
 "numeric_verification": {"facts_total": 6, "facts_verified": 6, "unverified_keys": [],
  "method": "Each newly cited row holds the elements it is cited for: US-SCS5-005 1.99/5.21; US-WIS5-011 (W-166) 3.54/4.65/5.30/7.65 while US-WIS5-010 (statute) holds 3.50/4.40 - the WI row was under-cited before; US-NES5-018 4.55; US-MAS5-026 s.45; OH and CT already cited inline. tag_sync 0 stale; C46 period-aware 0 mismatches."},
 "_closes": ["RC-1 (SC citation): closed; WI under-citation found and closed by the same fix"]}
skill = {"schema_version": "1.4.0", "artifact": "SKILL", "round": 3, "verdict": "PASS", "reviewed_on": D,
 "_file_round": "r6 = F28 re-check of skill round 6 against _pipeline/_backup/pre-skill-b4-2026-11-04/", "_reviewer": R,
 "_reviewed_file": "../skills-build/payroll-compliance-united-states/ 99/99 = SKILL-md5.txt; 6 files changed: 01-ccg/m05, m06, m13 (same citation changes as the CCG), 03-sir.md (same SIR changes + id renumbering), 07-qa-report.md (review ids r6/r3d), 14-known-gaps.md (counts 586 open, SIR-RQ renumbering)",
 "findings": [], "checks_run": ["C29"], "_checks_run_other": ["F28"],
 "numeric_verification": {"facts_total": 0, "facts_verified": 0, "unverified_keys": [], "method": "No new number; selfcheck (C29/WORD/PATH/NOTES/NUM 0) and selfcheck_strict (VAL/PERIOD/HAND 0) re-run by the auditor."}}
for n, d in [("SIR-review-r5", sir), ("CCG-review-r7", ccg), ("SKILL-review-r6", skill)]:
    json.dump(d, open(os.path.join(BASE, "_qa", n + ".json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("ok")

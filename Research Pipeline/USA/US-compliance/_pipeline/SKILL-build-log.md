# SKILL - build log
Artifact: SKILL | Country: US | Round: 1 | Built: 2026-11-04
Manifest: _pipeline/build-manifest.json (USD, minor units 2, package 1.0). Output: ../skills-build/payroll-compliance-united-states/ (relative to BASE; not installed).
Build script: skills-build/payroll-compliance-united-states/_build/build_skill.py (+ core_text.py for SKILL.md, 13-gotchas.md, 07-qa-report.md). Re-run: `python -I build_skill.py`.

## Precedent inspection (L1)
payroll-compliance-germany opened (read-only, ~/mercans-pipeline/skills-build): SKILL.md (front matter name/description, router intro, design clarifications, routing) + references/01-ccg ... 07-qa-report. payroll-compliance-canada folder is empty. No payroll-compliance skill exists under ~/.claude/skills. Template numbering 01-07 kept; US additions: 10-federal, 11-multistate, 12-states/, 13-gotchas, 14-known-gaps, 15-sources.
Sources read at their latest present version: CCG modules (13 + coverage), annexes FED, MULTI and 51 jurisdictions, US-WTC-001-v1.0, US-DD-001-v1.0, US-SIR-INDEX-001-v1.0, 20 US-*-Spec workbooks, US_Compliance_Payslip_Generator, legal-basis-register.csv, gaps.json, _qa review files.

## Layout
SKILL.md 5.3 KB. references: 01-ccg.md + 01-ccg/ (14 files), 02-wtc, 03-sir, 04-reports-spec.md + 20 files, 05-data-dictionary, 06-payslip, 07-qa-report, 10-federal, 11-multistate, 12-states.md + 51 files, 13-gotchas, 14-known-gaps, 15-sources. 99 md files, 6.3 MB.

## Fact bindings
Generated references are the approved text with every [[FACT:key=value]] tag rendered as its value; each file ends with a Fact index (key, value, effective period, register id) built from the facts files: 8,092 index rows. Gotchas and SKILL.md values are tags bound to keys (e.g. fed.fica.oasdi.wage_base 184,500 / 192,300 [US-FEDS5-005 / US-FEDB5-401]; ut.pit.base_allowance.single.annual 485 from 2026-04-01 [US-UTPIT-003]; ma.pfml.family.rate 0.18 (2026) / 0.7 (2027) [US-MAS5-012]; practice.* traps).

## Deviations
1. Regenerated after the CCG rebuild (m10 psl.* re-synced, annex_LA now "LWC online services"): the former deviations on m10 and LAWATS are closed at the source and removed. 0 tags print a substituted value.
2. Pipeline wording in the source text is rewritten by regex rules in build_skill.py (RULES); fact keys are never renamed. The LA UI-file gap RQ-240 wording is neutralised the same way.
3. 14-known-gaps.md prints US-OWN-001..011 with internal plan/file references replaced by "owner plan".
4. 13-gotchas keeps the LAWATS trap (power-of-attorney portal only, US-LAP52-005; UI wage-report channel is an open gap RQ-240).

## Round 2 (2026-11-04, SKILL-review-r1 builder items 1-4, 6-10)
- Facts ready (_research/skill-fix/FACTS-READY.md COMPLETE). CCG rebuilt with its own generators (rebuild_all); copy and md5 before: _pipeline/_backup/pre-skill-r1-2026-11-04/ (docx abcf0e13...); docx md5 after: a5f4db8ffc483f3e254368724657d42f. Cells changed: annex_DC configuration warning ("the the" fixed in the annex_DC-MA override), annex_LA (RQ-240 gap line removed, closed), annex_MS (ms.payslip.statute.exists table replaced by gap PSL-RQ-14), m10 (MS row without "statute exists: no"). tag_sync_check: 0 stale tags in all six artifacts.
- 1 LA gotcha and SKILL.md item 4 now state the LWC online services channel [US-LAS5-007]; RQ-240 removed from the open list. 2 DC aligned with DC.md (Notice 2022-08, inference flagged, gap RQ-138). 3 selection rule: payment date for tax and contribution values, hours worked for minimum wage (DC 17.95/18.40), earning date for MA PFML. 4 pipeline wording neutralised in 14-known-gaps (rules in build_skill.py; selfcheck WORD list extended with build lead, owner plan, Step-4, P9-, stage-1, C-ids, checker, table rNcN, orchestrator, merge worker, register_id, annex workers, ledger). 6 07-qa-report re-sync line added, stale sentence dropped. 7 fact-index claim narrowed. 8 raw True/False and the MA PFML duplicate clause removed. 9 LA override and the LAWATS regex removed from build_skill.py. 10 ledger line 128 corrected (11 psl.* tags), m04 HI and CCG rebuild lines added. Not done by the builder: gaps.json counts (agent 2 refreshed them).
- Item 5 resolved by the source hunter (MS gap PSL-RQ-14; UT note: revision dated April 2026, effective date not stated; period start 2026-04-01 kept as the register period).

## Round 3 (2026-11-04, SKILL-review-r2)
- annex_UT rebuilt with the CCG generator (build.py in _build-annex-NY-WY, 5 note cells now "Period start 2026-04-01; Pub. 14 Rev. 04/26 (revision dated April 2026); effective date not stated."). Copy and md5 before: _pipeline/_backup/pre-skill-r2-2026-11-04/ (docx a5f4db8ffc483f3e254368724657d42f); after 2568a947e023fd50e856ad1781eaf068. Diff: annex_UT only (5 lines); no other module or annex changed. tag_sync_check: 0 stale tags.
- FACTS-READY-2 COMPLETE: 14-known-gaps now lists RQ-597 (open) and the TN limitation; counts 586 open / 125 limitations.

## Round 4 (2026-11-04, SKILL r3 open item, option a)
- annex_LA (LA.5) now prints "Not configured in this release [[GAP:RQ-597]]: UI quarterly form name and upload layout" next to the LWC channel: the stale unresolved item la.report.sui.format in CCG-annex_LA-facts.json was re-keyed to la.report.sui.form_layout (copy in _pipeline/_backup/pre-skill-r3-2026-11-04/research/; file re-serialised, content otherwise unchanged). gaps.json: the RQ-240 residual now points to RQ-597. CCG rebuilt with rebuild_all; diff vs copy: annex_LA only (1 line); docx md5 a... 2568a947e023fd50e856ad1781eaf068 -> ffa24c2e3089eb58627ace5ca8811acf. tag_sync_check 0 stale.

## Round 5 (2026-11-04, run-close item B3, F28)
- Regenerated after _research/c41-fix/C70-READY.md COMPLETE (CCG md5 2bdf6f88ebcaa31c6ee743f0ba458096, 0 stale tags in tag_sync_check). Copy of the previous skill: _pipeline/_backup/pre-skill-b3-2026-11-04/. Changed reference files (13 plus the QA report line): 01-ccg/m06_tax, m10_reporting, m12_worked_examples, m13_practices; 03-sir; 04-reports-spec/US-DOR-001 and US-IRS-004; 05-data-dictionary; 12-states/MA; 13-gotchas (5 practice notes re-read from the current facts); 14-known-gaps; 15-sources; 07-qa-report. Design not referenced by the skill.
- Handwritten tags are now refreshed to the key's current value at build time (refresh() in build_skill.py), so no substitution is recorded.

## Round 6 (2026-11-04)
- Regenerated after the CCG/SIR citation rebuild (F27). Copy of the previous skill: _pipeline/_backup/pre-skill-b4-2026-11-04/. Changed: 01-ccg/m05_social_security, m06_tax, m13_practices; 03-sir; 14-known-gaps; 07-qa-report. tag_sync_check 0 stale; all self-checks 0; validate PASS.

## Checks (all run after the last build)
- validate_contract --all BASE: PASS (103 files). No contract exists for a skill.
- _build/selfcheck.py: C29 0, WORD 0, PATH 0, NOTES 0 (note_vocab_lint RX, PIPELINE_WORDS and PATH_RX copied from the run's lints), NUM 0 (every number in the skill exists in the facts or approved artifacts).
- _build/selfcheck_strict.py: 10,472 keyed rows; 8,866 value checks, 13,788 period checks, 117 handwritten numbers; 0 misses (a value must be a value of its key, a date an effective date of its key).
- Tag resolution at build: 0 misses (12 substitutions, above).

## Open items (named limitations)
| Item | What closes it |
|---|---|
| US-OWN-009 prevailing-wage flag still awaits owner confirmation | owner |
| 586 open gaps, 125 documented limitations (incl. RQ-597 LA UI form/layout and the TN UI statute limitation) (14-known-gaps.md); TY2025-labelled federal items listed there | source hunter, per gap |
| 04-reports-spec and 06-payslip reflect the workbooks as cell dumps (formulas shown as formulas) | none; structure is in the workbooks |
| 07-qa-report.md must receive a dated line whenever any source artifact changes (F28) | whoever edits a source |
| SKILL status in build-manifest.json left at scaffolded; not edited by the builder | orchestrator, after QA |

## Accuracy
About 85%. Content is the approved artifacts verbatim (no new research), so it inherits their stated accuracy (CCG about 89% core, 75-85% per State; RSPEC 78%; SIR 75-85%). It is not 100% because of the open gaps above and the unconfirmed owner decision US-OWN-009. Not installed under ~/.claude/skills.

## md5
md5 of the 99 skill files (excluding _build): _pipeline/SKILL-md5.txt (written last).

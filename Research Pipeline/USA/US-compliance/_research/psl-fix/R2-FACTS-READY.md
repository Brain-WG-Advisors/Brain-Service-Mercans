# PSL fix R2 - facts ready (2026-11-04)
Source: `_qa/PSL-review-r1.json` -> `_batch_fix_list` (source-hunter group). Backups: `_research/psl-fix/_backup2/` (MD5-BEFORE.txt). `_research/facts.lock` taken and released. No web fetch needed; all texts read in saved copies. R1 F44 work not redone. Workbooks untouched.

## Done
- QA1-09: `psl.mn.statement.content` re-issued with the full 181.032(b) 12-item list (read in MN_stat-181.032_revisor_2026-10-30.html), register US-MNP6-001.
- QA1-11: new fact `psl.ca.statement.household_exclusion` (Lab. Code 226(d), US-CAS5-005, level: employer payslip-content duty, California only). Builder: C12 cites it, drop psl.va.statement.content from C13.
- QA1-14: reworded, no number changed: `psl.in.statement.scope` (dropped "build emits ..."), `psl.nc.ssn.rule` (dropped "safe build = truncated SSN"), `psl.multi.reach.default` ("researched" -> "identified").
- QA1-20: PSL/8_sheets added to consumed_by of US-FEDS5-001, US-FEDS5-029, US-FEDS5-030.
- QA1-21: register row US-OWN-011 added (20 columns, active, consumed_by WTC;CCG;PSL), pattern of US-OWN-010.
- Ledger: 2 lines in PROPAGATION-LEDGER.md. `validate_contract --all`: see final line.

## For the owner of build-manifest.json (not edited by me)
Replace the generic URLs in validation_exemptions:
- C49 `source` (https://www.ksrevenue.gov/) -> register row **US-KSS5-001** (KW-100 Kansas Withholding Tax Guide, https://www.ksrevenue.gov/kw100.html).
- C50 `source` (https://dol.georgia.gov/) -> register row **US-GAS5-006** (GDOL Employer Handbook DOL-224, section 125 premiums not wages, https://dol.georgia.gov/document/unemployment-tax/employer-handbook/download).
- C48 `source` already specific (iw2w3); register row US-FEDS5-007 named in its reason.

## Open
None for the source hunter. Builder items QA1-01..08, 10, 12-19, 22 are not mine.

STATUS: COMPLETE

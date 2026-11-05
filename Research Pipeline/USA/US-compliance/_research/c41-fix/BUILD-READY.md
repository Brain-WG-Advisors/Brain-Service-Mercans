# C41 build ready (2026-11-04)
Copies: _pipeline/_backup/pre-c41-2026-11-04/ (ccg, rspec, sir, design, dd, wtc).
Result: shared C41 PASS, C40 PASS, tag_sync_check 0 stale in CCG, SIR, RSPEC, DD, WTC, PSL, vocab lint 0, C71 0 (RSPEC, DD, WTC, SIR), C45 design PASS (design rebuilt, identical; it prints none of the six keys), validate_contract --all PASS (112 files).

## Rebuilt artifacts and changed lines
- CCG (md5 dea716d4c6cd4f0c9032d29148d8fa9f): m10_reporting section 10.5, new table "Changes during 2026" (8 rows): rspec.fed.form940.due (both periods, 2026-01-01 to 2026-02-10 and from 2026-02-11), rspec.fed.futa.credit_reduction.states (2025 list = wages of 2025, reported on the 2025 Form 940; 2026 list = gap RQ-402), rspec.me.wh_return.form from 2026-04-14, sir.nj.withholding.agent_authorization from 2026-06-09, sir.dc.withholding.agent_authorization from 2026-09-16, sir.tx.ui.agent_authorization from 2026-03-13.
- RSPEC: US-DOR-001 3 cells (Maine form, "(from 2026-04-14)"); US-IRS-004 7 cells (Form 940 due: the successor period in force from 2026-02-11; 2025 credit-reduction list worded as wages of 2025, "(until 2026-02-10)"; K15, M15, M5, C10, C17, B11, F27). Tag helper prints the change date after the tag for the six keys.
- SIR (md5 88dea8e2b93586ce79ab7945ba86ff26): change dates printed after the tags of the same keys (NJ, DC, TX forms; Form 940 successor period, now a gap cell because the successor wording is not in the saved copy); two DD elements dispositioned (supplemental wage method election in section 8; State-assigned UI rate via inbound register 1.2); gap numbers renumbered by the source-hunter closures.
- DD, WTC, design: rebuilt, 0 cells changed.

## Open (not mine to fix)
- Shared C70 FAIL, 23 hits (22 CCG, 1 WTC): text cites register rows the register batch closed as superseded: US-INP51-001 (Indiana Departmental Notice #1; 16), US-RIS5-008 (RIGL 28-14-12; 2), US-OHR3C-001 (ORC 4141.23; 2), US-FEDS5-013, US-OHP52-001 (successor US-OHS5-001), US-CAS5-020. Needs the source hunter to re-bind those facts to the successor rows; then CCG and WTC rebuild.
- Package-wide C46 still FAIL with multi-period hits only (537, plus 235 unbound fact values; CCG period-aware 0 mismatches, 120 unbound as before).

STATUS: COMPLETE

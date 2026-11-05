# Skill fix (SKILL-review-r1 item 5) - facts ready 2026-11-04
Backups: _research/skill-fix/_backup/ (MD5-BEFORE.txt). facts.lock taken and released. 3 ledger lines. validate_contract --all PASS.
Changed:
- MS (CCG-annex_MS-facts.json): fact ms.payslip.statute.exists REMOVED (false was unproven; US-MSP9L-001 is a posters page); now unresolved[] ms.payslip.statute.exists with the PSL-RQ-14 wording. No other MS fact says "no statute" (final-pay "not located" is an unresolved, unchanged). Builder: print as open gap PSL-RQ-14 in m10, annex_MS, skill MS.md.
- UT (CCG-annex_UT-facts.json): Pub 14 copy (US-UTPIT-003) re-read: Rev. 04/26, no effective date stated. Notes on ut.pit.base_allowance.single.annual, .married.annual, ut.pit.phaseout_threshold.single.annual, .married.annual, ut.pit.phaseout.rate now read "Pub. 14 Rev. 04/26 (revision dated April 2026); effective date not stated"; effective_from 2026-04-01 kept (register period start). gaps.json RQ-343 (limitation) and RQ-596 (open) carry matching notes.
- LA (gaps.json): RQ-240 closed 2026-11-04 (US-LAS5-007).
- gaps.json counts refreshed: open 585, documented_limitation 124, closed 30 (incl. RQ-240), check_existing_fact 1, no_status_field 1 (R3C-TN-UI-STATUTE), total 741.

STATUS: COMPLETE

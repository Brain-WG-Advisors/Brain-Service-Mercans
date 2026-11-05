# R1-FACTS-READY (source hunter, 2026-11-03)

Facts file: `_research/DD-8_sheets-facts.json`. Register: `00-official-sources/legal-basis-register.csv`. Backups: `_research/dd-fix/backup/*.20261103-r1`. validate_contract facts PASS; `--all` PASS (88 files). Web fetches: 1 search + 1 download (a duplicate of a copy already held, not kept). Workbooks not touched.

## Keys changed

| Key | Change | DD cell to regenerate |
|---|---|---|
| dd.state.w4.mt | Re-bound US-MTP51-002 -> **US-MTS5-005** (also US-MTP51-002). **Value reworded** to `MW-4 (employer submits exemption-claim forms on TAP)` | **E299** |
| dd.oh.school_district_code | Primary now **US-OHB5-401** (2026, effective_from 2026-01-01, no effective_to). Also US-OHB5-001 (full TY2026 list, already registered), US-OHS5-018 (delta), US-OHS5-019 (2025 list, source of 9999). Value unchanged | **W96**: drop the "2025 list" sentence; the 9999 rule rests on the 2025 booklet list (no 2026 restatement found) |
| dd.state.w4.nd | +also US-NDS5-002. Value unchanged | none (C46 only) |
| dd.multi.transport_worker_type | +also US-MULTIS5-001/002/004. Value unchanged | none (C46 only) |
| dd.state.w4.oh | Primary now **US-OHP51-002** (set `active`), also US-OH-002. effective_from 2026-01-01. Value unchanged | none |
| dd.ct.ui.occupation_hours_zip | US-CTP10-001 dropped; `_figure_located` is the CGS quote. Value unchanged | none |

Register: US-OHP51-002 status superseded -> active. DD added to consumed_by of US-FEDS6-006, US-FEDS5-004, US-FEDS6-011 (finding 13) and DD/8_sheets to every row now cited by these keys. No new row was needed: the full 2026 Ohio list is US-OHB5-001 (md5 1d690d04..., same file as dam.assets.ohio.gov `sdit_list.pdf`).

## Quotes (copies)

- **MT** US-MTS5-005 (Employer-Agent-Guide-V4-Nov2025 p.2): "Employers with employees claiming an exemption from Montana wage withholding must submit the employee's Form MW-4 by the last day of the payroll period of when the form was submitted to the employer. The exemption must be renewed annually by January 31. The Form MW-4 must be filed on TAP; this requires an active TAP login." p.1: "Employee's Withholding Allowance and Exemption Certificate (Form MW-4)"; "TransAction Portal (TAP)". US-MTP51-002 supports only "Form MW-4". Note that the guide says the **employer submits** the form, not that the employee sends it to DOR; do not write "sent to DOR".
- **ND** US-NDS5-002: "provided the employee completes and gives a Form NDW-R, Reciprocity Exemption From Withholding For Qualifying Minnesota and Montana Residents Working in North Dakota, to the employer".
- **Transport** US-MULTIS5-001 (49 USC 14503): "No part of the compensation paid by a motor carrier providing transportation subject to jurisdiction under subchapter I of chapter 135 or by a motor private carrier to an employee who performs regularly assigned duties in 2 or more States". US-MULTIS5-002 (49 USC 11502): "No part of the compensation paid by a rail carrier providing transportation subject to the jurisdiction of the Board under this part to an employee who performs regularly assigned duties as such an employee on a rail...". US-MULTIS5-004 (46 USC 11108): "Wages due or accruing to a master or seaman on a vessel in the foreign, coastwise, intercoastal, interstate, or noncontiguous trade". US-MULTIS5-003: air carrier (40116(f)).
- **OH SD** US-OHB5-401: "School districts and the corresponding four-digit codes can be verified using The Finder". US-OHB5-001 p.2: "School Districts With an Income Tax as of January 2026 ... School District Number ... Tax Year 2026 Rate". US-OHS5-018: "When creating W-2s for your employees, identify the school district by its four-digit code." US-OHS5-019: "Full-year nonresidents of Ohio should enter 9999".
- **OH IT 4** US-OHP51-002 p.1: "the employer must withhold tax based on the employee claiming zero exemptions"; "current IT 4 revised 12/2020".
- **CT** US-CTS5-018 (CGS 31-225a(j)(1)(B)): "Commencing with the third calendar quarter of 2026, any employer subject to this chapter may include in the quarterly filing ... (i) Such employee's occupation, (ii) such employee's hours worked, and (iii) the zip code of such employee's primary worksite."

## Still open (non-blocking)
dd.oh.school_district.codes: the 2026 list is held but is a two-column PDF; number-to-name pairing is not reliable (unresolved[] updated). Closes with the Finder file download. DD-RQ-01..05: state unchanged since `DD-FACTS-FIX.md`.

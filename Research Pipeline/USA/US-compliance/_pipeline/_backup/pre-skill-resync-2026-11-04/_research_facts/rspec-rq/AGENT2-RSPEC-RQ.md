# Agent 2: RSPEC research requests RQ-01 to RQ-14 (2026-11-03)

Scope: `_research/RSPEC-research-request.json` (artifact-builder, round 1; no RQ-10 was issued), worked before QA round 1, plus the NJ base-week citation fix. I wrote nothing under `04-reports-spec/` or `~/mercans-pipeline`. Backups taken before this pass are in `_research/rspec-rq/_backup/`: the register, RSPEC facts, pack, gaps.json, the request file and SOURCE-REGISTER.md.

Budget: about 60 network calls (curl to irs.gov, tax.ny.gov, seattle.gov, city sites and the Wayback Machine, plus 2 web searches). I stopped acquiring when the WV and Pittsburgh city sites returned 403.

## Result per request
| RQ | Status | Register | Keys (main) |
|---|---|---|---|
| 01 Form 941/944 lines | closed | US-FEDS6-001/-002/-003 | rspec.fed.form941.line_map, .schedule_b.structure, rspec.fed.form944.line_map, .due |
| 02 EFW2 RA/RE/RW/RT + RE codes | closed | US-FEDS5-032 (held PDF) | rspec.fed.efw2.{ra,re,rw,rt}.layout, .money_field.format, rspec.fed.efw2.re.{agent_indicator,kind_of_employer,employment_code,tax_jurisdiction,third_party_sick_pay}.codes |
| 03 W-2 box map + TTOC | closed | US-FEDS5-007, US-FEDS6-011 | rspec.fed.w2.box_map, .box14b.rule, .box14b.ttoc_codes (71 + 000), .box14b.ttoc_count |
| 04 Form 943 | closed (2026 draft) | US-FEDS6-004 | rspec.fed.form943.line_map, .due |
| 05 1042-S wage codes | closed | US-FEDS6-005 | rspec.fed.form1042s.wage_codes (+3 component keys) |
| 06 1094-C/1095-C | closed (2026 draft) | US-FEDS6-006 | rspec.fed.aca.form1095c.line14/15/16/17, form1094c.line_map, affordability_pct 9.96, ty2026_due |
| 07 941-X | closed | US-FEDS6-007 | rspec.fed.form941x.line_map, .process_rule, .deadlines |
| 08 Form 940 + credit reduction | documented_limitation | US-FEDS6-008/-009, US-FEDS5-009 | rspec.fed.form940.line_map, .schedule_a.structure, futa.credit_reduction.states (2025 final CA 1.2 %, VI 4.5 %); open: states_2026 |
| 09 Schedule H statement | closed | US-FEDS6-010 | rspec.fed.schedule_h.employer_statement, .due, household thresholds 3,000 / 1,000 |
| 11 WV service fees | documented_limitation | US-WVS6-001/-002 | charleston / morgantown service_fee_return; open: other_municipal_service_fees |
| 12 Pittsburgh PET return | documented_limitation | US-PAS6-001/-002 | pittsburgh_payroll_expense.return (ET-1, May 31 / Aug 31 / Nov 30 / Feb 28); open: form_2026 |
| 13 Seattle PET/SHT | closed | US-WAS6-001/-002 | seattle.base_thresholds_due + 5 numeric thresholds, sht.rate / excess_comp_threshold / due |
| 14 NY MCTMT | closed | US-NYS6-001 | rspec.ny.mctmt.rates_lines, quarterly_threshold 312,500, band ceilings, zone rates |

**NJ fix.** The 2026 `rspec.nj.ui_qtr.base_week_amount` (310) now cites US-NJS5-011, with effective_to 2026-12-31. A new 2027 object (319) cites US-NJS5-010. RSPEC was added to the `consumed_by` of US-NJS5-011.

## Gates
- **G-NUMBER.** Every number comes from the IRS, SSA, NY DTF or city page or form, held locally, with md5 in the register. No tier-B row is cited.
- **G-SPOT.** The EFW2 layouts were checked by script: each record covers positions 1-512 with no gap or overlap. The 71 TTOC codes were parsed from the HTML table rows, not inferred from examples. The 2025 credit-reduction list rests on two authorities (IRS Schedule A 2025 and the DOL table).
- **G-DERIVE.** Every Seattle 2026 threshold divided by its 2025 value gives 1.02683, a single CPI-U step under SMC 5.38.070.
- **Drafts.** The IRS 2026 drafts for Forms 940, Schedule A, 943, 944, 1094-C/1095-C and Schedule H are A.2 but not final. Their facts are confidence `medium` and noted "re-verify against the final 2026 revision".

## Files
- **Register.** 2,676 rows before, 2,694 after: 18 new (US-FEDS6-001..011, US-NYS6-001, US-WAS6-001/002, US-PAS6-001/002, US-WVS6-001/002), all with 20 columns. The round trip before the edit was byte-identical. `verified_on` 2026-11-03 was stamped on US-FEDS5-032, US-FEDS5-007, US-NJS5-010 and US-NJS5-011.
- **`RSPEC-facts.json`.**
  - 425 facts before, 493 after: 68 new, including the NJ 2027 object.
  - `rspec.fed.form940.due` already existed, so I extended its note instead of adding a duplicate.
  - 46 unresolved, 0 blocking. That is 3 new documented limitations; the 940 and ACA TY2026 items are narrowed.
  - `validate_contract.py facts` gives PASS, and `--all` gives PASS on 83 files.
  - Every fact resolves to a register row whose `consumed_by` includes RSPEC; none cites a tier-B or superseded row.
- **`RSPEC-research-request.json`.** Each request now carries `_status`, `_closed_on`, `_closed_by_register_ids`, `_closed_by_keys` and `_resolution_note` (underscore keys, so the schema still passes).
- **`gaps.json` → `RSPEC`.** 13 new entries RSPEC-RQ-01..14: 10 closed, 3 documented_limitation. Block counts: 14 closed, 21 documented_limitation, 25 open_non_blocking.
- **`RSPEC-research-pack.md`.** New section "RSPEC-RQ close (2026-11-03, agent 2)", organised by report spec. The Open questions block was regenerated from `unresolved[]`.
- **`SOURCE-REGISTER.md`.** RSPEC-RQ block appended.
- **New sources.** 29 files in `00-official-sources/spec-sources/{FED,NY,WA,PA,WV}/`, 10.1 MB in total, none over 5 MB. The `spec-sources/` folder is now 11.0 MB.

## Open (what would close it)
- `rspec.fed.futa.credit_reduction.states_2026`: the DOL final 2026 list (after 2026-11-10) and the final Schedule A (Form 940) for 2026.
- `rspec.wv.local.other_municipal_service_fees`: the ordinances and return forms of Huntington, Wheeling, Parkersburg, Fairmont, Weirton and others, through a Chrome pass. The lookups are independent per city and can run in parallel.
- `rspec.pa.local.pittsburgh_payroll_expense.form_2026`: the 2026 ET-1 PDF from pittsburghpa.gov through a Chrome pass, or a confirmation from the City Finance office.
- Final IRS 2026 revisions to replace the drafts, normally released in December.
- A builder note: `rspec.fed.efw2.re.layout` (full record) and the earlier `rspec.fed.efw2.re.layout_ty2026` (partial) agree on every position. Both keys are kept.

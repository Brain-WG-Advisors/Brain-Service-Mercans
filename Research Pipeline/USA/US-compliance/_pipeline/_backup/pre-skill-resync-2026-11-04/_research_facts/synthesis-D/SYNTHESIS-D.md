# Synthesis D — US build (2026-11-02)

Scope: merge browser-pass shards S5B-P1 (20 rows) and S5B-P2 (18 rows) into the register, add owner row US-OWN-008, close the fact keys the new rows prove, read SSA EFW2 TY2026 (US-FEDS5-032) and close the EFW2 blocking items. No fetching. MANDATE.md, build-manifest.json and SKELETON-MANIFEST.md not touched. Every rewritten file is backed up under `_research/synthesis-D/_backup/` (same relative path). Logs: `_research/synthesis-D/_work/` (register-log.csv, facts-log.json, consumed_by-appended.json, packs-report.json, blocking.json, validator.txt).

## 1. Register merge

- `legal-basis-register.csv`: 2,533 → 2,572 rows (+38 shard rows, +1 US-OWN-008). 20 columns on every row, ids unique, tiers in {A.1, A.2, A.3, B, C, owner}, status in the existing set, every new `local_file` exists. A CSV round-trip of the old file was byte-identical before writing, so existing rows were not requoted.
- Shard `supersedes` values checked against `_research/stage5/ID-RENAME-MAP.csv`: none used an old id (all already in the new form).
- **US-COB5-002** (proposed 2027 PAY CALC Order): status `proposed` is not in the register's status set → **`provisional`**. Its `supersedes` cell (US-COS5-011) was **cleared**: a proposed rule does not supersede, and US-COS5-011 also carries Denver 2027 / Edgewater / Boulder leads that stay open. The intent is recorded in both rows' figure text. It is never a fact value until adopted.
- Normalised on the new rows: `verification_method` now starts with one of the three methods (`quoted from authority page` / `inspected directly`), and the browser-pass wording is kept in brackets. `local_file` is reduced to the path; md5 and companion files moved into `verification_method`. Shard placeholder `consumed_by` values (e.g. `CCG/WTC`, `SIR/Report Specs`) were cleared and rebuilt from the facts actually emitted.
- Enriched from the local files (inspected directly): US-WAB5-003 (toolkit pp.22-24: due dates, per-employee fields, channels) and US-CTB5-001 (p.11: employee-level records excluded from return files since July 2025).
- **US-FEDS5-032** (EFW2 TY2026): `local_file` prefixed `00-official-sources/`, `verified_on` 2026-11-02, method `inspected directly` (pdftotext; md5 5cf1352109d305bb6d28b39b1b4a8d7b; header dated 9/14/2026). Record positions are transcribed into the figure.
- **US-OWN-008** appended (tier `owner`, domain governance, local_file `00-official-sources/MANDATE.md`, consumed_by `MANDATE`): employers = private sector; workers = common-law employees; independent contractors / Form 1099-NEC OUT OF SCOPE. MANDATE.md line 22 still carries the TODO to cite it; that edit is the scaffolder's.

New rows: US-OWN-008, US-DCB5-001, US-DCB5-002, US-UTB5-001, US-UTB5-002, US-UTB5-003, US-UTB5-004, US-OHB5-001, US-OHB5-002, US-WAB5-001, US-WAB5-002, US-WAB5-003, US-WAB5-004, US-FEDB5-001, US-NYB5-001, US-NYB5-002, US-NYB5-003, US-CTB5-001, US-MAB5-001, US-MIB5-001, US-WYB5-001, US-AZB5-001, US-AZB5-002, US-AZB5-003, US-AZB5-004, US-AZB5-005, US-AZB5-006, US-COB5-001, US-COB5-002, US-COB5-003, US-TNB5-001, US-TNB5-002, US-VTB5-001, US-VTB5-002, US-VTB5-003, US-PAB5-001, US-NMB5-001, US-NMB5-002, US-ARB5-001.

### Supersessions applied

| Old row | Old status | New status / effective_to | Superseded by | consumed_by of the old row (re-sync list) |
|---|---|---|---|---|
| US-OHS5-023 | partial | superseded / 2026-11-02 | US-OHB5-002 | DD |
| US-NYS5-022 | MANUAL | superseded / 2026-11-02 | US-NYB5-001 | CCG;WTC |
| US-NYS5-023 | MANUAL | superseded / 2026-11-02 | US-NYB5-003 | PSL;CCG |
| US-MIS5-026 | partial | superseded / 2026-11-02 | US-MIB5-001 | CCG;RSPEC;SIR |
| US-AZS5-028 | MANUAL | superseded / 2026-11-02 | US-AZB5-001 (2026 part) + US-AZB5-002 (2027 part) | CCG;WTC |

After this pass, no fact in any `_research/*-facts.json` cites a superseded, MANUAL or provisional row (checked: 0 hits). The old rows were leads or partials, so no fact value changed through them. The listed `consumed_by` artifacts only need re-pointing if their prose quotes those ids.

Not applied: US-COS5-011 ← US-COB5-002 (provisional; see above).

## 2. Facts added / changed per file

| File | Added | Changed | Renamed | Unresolved closed | Unresolved added | Unresolved updated |
|---|---|---|---|---|---|---|
| CCG-annex_AZ-facts.json | 12 | 0 | 0 | 3 | 1 | 0 |
| RSPEC-facts.json | 29 | 1 | 0 | 4 | 2 | 1 |
| SIR-facts.json | 6 | 1 | 0 | 2 | 0 | 2 |
| CCG-annex_CO-facts.json | 9 | 6 | 2 | 0 | 1 | 2 |
| WTC-country_specific-facts.json | 14 | 3 | 0 | 3 | 0 | 8 |
| CCG-annex_TN-facts.json | 6 | 0 | 0 | 2 | 0 | 0 |
| CCG-annex_VT-facts.json | 4 | 1 | 0 | 1 | 1 | 1 |
| CCG-annex_PA-facts.json | 6 | 0 | 0 | 1 | 0 | 0 |
| CCG-annex_NM-facts.json | 5 | 0 | 0 | 0 | 0 | 1 |
| CCG-annex_AR-facts.json | 3 | 0 | 0 | 0 | 0 | 1 |
| CCG-annex_OH-facts.json | 12 | 0 | 0 | 2 | 1 | 0 |
| DD-8_sheets-facts.json | 3 | 0 | 0 | 1 | 0 | 0 |
| CCG-annex_NY-facts.json | 10 | 0 | 0 | 3 | 0 | 0 |
| PSL-facts.json | 1 | 0 | 0 | 1 | 0 | 0 |
| CCG-annex_CT-facts.json | 2 | 0 | 0 | 1 | 0 | 0 |
| CCG-annex_WA-facts.json | 6 | 0 | 0 | 1 | 0 | 1 |
| CCG-annex_MA-facts.json | 3 | 0 | 0 | 0 | 0 | 0 |
| CCG-annex_UT-facts.json | 1 | 0 | 0 | 1 | 0 | 2 |
| CCG-annex_MI-facts.json | 4 | 0 | 0 | 0 | 0 | 1 |
| CCG-annex_FED-facts.json | 8 | 0 | 0 | 1 | 0 | 0 |
| CCG-annex_MULTI-facts.json | 0 | 0 | 0 | 0 | 0 | 1 |
| CCG-m10_reporting-facts.json | 2 | 0 | 0 | 1 | 0 | 1 |
| CCG-annex_DC-facts.json | 0 | 0 | 0 | 0 | 0 | 1 |
| CCG-m12_worked_examples-facts.json | 0 | 0 | 0 | 0 | 0 | 1 |
| CCG-annex_WY-facts.json | 0 | 0 | 0 | 0 | 0 | 2 |

Totals: 146 facts added, 12 fact edits, 2 key renames, 28 unresolved closed, 6 added (narrowed remainders), 26 updated.

**CCG-annex_AZ-facts.json**
- added: `az.minwage.hourly` = 15.15 (2026-01-01, US-AZB5-001); `az.minwage.hourly` = 15.65 (2027-01-01, US-AZB5-002); `az.minwage.tipped.cash_wage` = 12.15 (2026-01-01, US-AZB5-001); `az.minwage.tipped.cash_wage` = 12.65 (2027-01-01, US-AZB5-002); `az.local_minwage.flagstaff.hourly` = 18.35 (2026-01-01, US-AZB5-003); `az.local_minwage.flagstaff.hourly` = 18.95 (2027-01-01, US-AZB5-003); `az.local_minwage.flagstaff.tip_credit.applies` = False (2026-01-01, US-AZB5-003); `az.local_minwage.flagstaff.coverage_min_hours_per_year` = 25 (2026-01-01, US-AZB5-003); `az.report.sui.quarterly` = UC-018 Unemployment Tax and Wage Report (cont… (2026-01-01, US-AZB5-005); `az.report.sui.due_dates` = Apr 30 / Jul 31 / Oct 31 / Jan 31 (next busin… (2026-01-01, US-AZB5-004); `az.report.sui.late_penalty` = late report: 0.1% of total quarterly wages, m… (2026-01-01, US-AZB5-004); `az.report.sui.uiof_line` = From CY2027 experience-rated employers pay 3.… (2027-01-01, US-AZB5-006)

**RSPEC-facts.json**
- added: `rspec.az.ui_qtr.form` = UC-018 quarterly Unemployment Tax and Wage Re… (2026-01-01, US-AZB5-005); `rspec.az.ui_qtr.due` = Apr 30 / Jul 31 / Oct 31 / Jan 31, next busin… (2026-01-01, US-AZB5-004); `rspec.az.ui_qtr.late_penalty` = 0.1% of quarterly wages, min 35 USD, max 200 … (2026-01-01, US-AZB5-004); `rspec.az.ui_qtr.uiof_line` = From 2027: UIOF line (3.15% of UI liability) … (2027-01-01, US-AZB5-006); `rspec.oh.municipal.rate_table` = Per-municipality withholding rate by work-loc… (2026-01-01, US-OHB5-002); `rspec.oh.school_district.list` = 4-digit SD numbers and TY2026 rates for SD 10… (2026-01-01, US-OHB5-001); `rspec.ct.pfml_qtr.file_spec` = CT Paid Leave File Specification Toolkit v2.1… (2026-10-05, US-CTB5-001); `rspec.ct.pfml_qtr.return_elements` = FEIN, StateTaxID, ReportingQuarter, Reporting… (2026-10-05, US-CTB5-001); `rspec.ct.pfml_qtr.employee_records` = Not allowed: employee-level records must not … (2026-10-05, US-CTB5-001); `rspec.wa.pfml_ltc_qtr.fields` = Combined Paid Leave + WA Cares quarterly repo… (2026-06-26, US-WAB5-003); `rspec.wa.pfml_ltc_qtr.due` = Last day of the month after each quarter: Apr… (2026-06-26, US-WAB5-003); `rspec.wa.pfml_ltc_qtr.no_payroll_report` = True (2026-06-26, US-WAB5-003); `rspec.wa.pfml_ltc_qtr.channels` = Manual entry (up to 50 employees), single CSV… (2026-06-26, US-WAB5-003); `rspec.wa.pfml_ltc_qtr.penalties_from` = 2026-08-01 (2026-08-01, US-WAB5-002); `rspec.wa.ui_qtr.penalties` = Late tax/wage report 25 USD per report; incom… (2022-11-17, US-WAB5-004); `rspec.mi.new_hire.deadline_days` = 20 (2026-01-01, US-MIB5-001); `rspec.mi.new_hire.fields` = Employee SSN, name, address, date of birth (o… (2026-01-01, US-MIB5-001); `rspec.fed.new_hire.electronic_interval` = two monthly transmissions 12-16 days apart (e… (1997-10-01, US-FEDB5-001); `rspec.fed.new_hire.state_penalty_cap` = 25 USD per new hire; 500 USD where the failur… (1997-10-01, US-FEDB5-001); `rspec.fed.efw2.edition` = SSA Publication No. 42-007, EFW2 Tax Year 202… (2026-01-01, US-FEDS5-032); `rspec.fed.efw2.record_length` = 512 (2026-01-01, US-FEDS5-032); `rspec.fed.efw2.records` = 512-byte records in order RA, RE, RW, [RO], [… (2026-01-01, US-FEDS5-032); `rspec.fed.efw2.ty2026_changes` = TY2026 changes: RE adds Employer Signature PI… (2026-01-01, US-FEDS5-032); `rspec.fed.efw2.re.layout_ty2026` = RE: EIN 8-16; Establishment Number 27-30; Oth… (2026-01-01, US-FEDS5-032); `rspec.fed.efw2.rw.tipped_occupation_code` = RW: Primary Treasury Tipped Occupation Code 4… (2026-01-01, US-FEDS5-032); `rspec.fed.efw2.ro.ty2026_money_fields` = RO money fields (11 bytes): combined Codes A+… (2026-01-01, US-FEDS5-032); `rspec.fed.efw2.ru.ty2026_money_fields` = RU totals (15 bytes): combined A+B 25-39; Cod… (2026-01-01, US-FEDS5-032); `rspec.fed.efw2.rs.layout` = RS (optional, state/local-defined): state cod… (2026-01-01, US-FEDS5-032); `rspec.fed.efw2.rv_rf.layout` = RV (optional): supplemental data 3-512, user/… (2026-01-01, US-FEDS5-032)
- changed: `rspec.mi.new_hire.channel` (2024-01-01): value, register_id, tier, verification_method, confidence

**SIR-facts.json**
- added: `sir.az.ui.wage_report` = UC-018 quarterly via DES Tax and Wage System … (2026-01-01, US-AZB5-005); `sir.ct.paid_leave.bulk_format` = Batch XML (XSD) or CSV via SFTP per File Spec… (2026-10-05, US-CTB5-001); `sir.mi.new_hire.days` = 20 (2026-01-01, US-MIB5-001); `sir.fed.efw2.layout_ty2026` = SSA Publication No. 42-007, EFW2 Tax Year 202… (2026-01-01, US-FEDS5-032); `sir.fed.efw2.state_records` = Provider must build RS per state spec on the … (2026-01-01, US-FEDS5-032); `sir.fed.efw2.employer_signature_pin` = Optional RE 319-328 Employer Signature PIN (S… (2026-01-01, US-FEDS5-032)
- changed: `sir.fed.w2.format` (2026-01-01): note

**CCG-annex_CO-facts.json**
- added: `co.minwage.minor.hourly` = 12.89 (2026-01-01, US-COB5-001); `co.exempt.salary.weekly_min` = 1111.23 (2026-01-01, US-COB5-001); `co.exempt.highly_technical_computer.hourly_min` = 34.85 (2026-01-01, US-COB5-001); `co.exempt.highly_compensated.annual_min` = 130014 (2026-01-01, US-COB5-001); `co.wage_claim.max_amount` = 7500 (2026-01-01, US-COB5-001); `co.wage_claim.max_amount` = 13000 (2026-07-01, US-COB5-001); `co.famli.employee.rate` = 0.44 (2026-01-01, US-COB5-003); `co.famli.employer.rate` = 0.44 (2026-01-01, US-COB5-003); `co.famli.small_employer.max_employees` = 9 (2026-01-01, US-COB5-003)
- changed: `co.minwage.hourly` (2026-01-01): register_id, tier, verification_method, note_append; `co.minwage.tip_credit.max` (2026-01-01): register_id, tier, verification_method, note_append; `co.minwage.tipped.cash_wage` (2026-01-01): register_id, tier, verification_method, note_append; `co.exempt.salary.annual_min` (2026-01-01): register_id, tier, verification_method, note_append; `co.minwage.hourly` (2026-01-01): note; `co.minwage.tipped.cash_wage` (2026-01-01): note
- renamed: `co.famli.rate.total.2026` → `co.famli.total.rate` (2026-01-01); `co.famli.rate.total` → `co.famli.total.rate` (2027-01-01)

**WTC-country_specific-facts.json**
- added: `co.famli.employee.rate` = 0.44 (2026-01-01, US-COB5-003); `co.famli.employer.rate` = 0.44 (2026-01-01, US-COB5-003); `co.famli.small_employer.max_employees` = 9 (2026-01-01, US-COB5-003); `oh.local.municipal.rate_table` = The Finder OHMuniRateTable.csv (Ohio Departme… (2026-01-01, US-OHB5-002); `oh.local.school_district.full_list` = ODT 'A list of Ohio's School District Income … (2026-01-01, US-OHB5-001); `oh.local.school_district.count` = 214 (2026-01-01, US-OHB5-001); `ny.pfl.employee.rate` = 0.452 (2027-01-01, US-NYB5-001); `ny.pfl.employee.annual_max` = 451.81 (2027-01-01, US-NYB5-001); `ct.pfml.base.definition` = CTPL wages = total wages; for FICA-covered em… (2026-10-05, US-CTB5-001); `wa.pfml.wage_cap` = 184500 (2026-01-01, US-WAB5-002); `wa.cares.base.same_as_pfml` = True (2026-06-26, US-WAB5-003); `ma.sui.rate_schedule.selection` = Schedule A-G by Unemployment Compensation Fun… (2015-01-01, US-MAB5-001); `ma.sui.rate_schedule.table` = 45 account-reserve rows x 7 schedules (positi… (2015-01-01, US-MAB5-001); `ma.sui.rate_schedule.in_force` = E (2026-01-01, US-MAB5-001)
- changed: `vt.sui.wage_base` (2026-01-01): note; `ar.sit.rate.top` (2026-01-01): note_append; `ny.pfl.employee.annual_max` (2026-01-01): effective_to

**CCG-annex_TN-facts.json**
- added: `tn.wc.benefit.ttd.weekly_max` = 1488.3 (2026-07-01, US-TNB5-001); `tn.wc.benefit.ppd.weekly_max` = 1353.0 (2026-07-01, US-TNB5-001); `tn.wc.benefit.weekly_min` = 202.95 (2026-07-01, US-TNB5-001); `tn.live.bwc_2026` = 2026 workers' compensation acts (PC 705, 845,… (2026-07-01, US-TNB5-001); `tn.labour.child_labour.hours` = Ages 14-15: school in session max 3 h/day and… (2026-01-01, US-TNB5-002); `tn.labour.child_labour.break_minutes` = 30 (2026-01-01, US-TNB5-002)

**CCG-annex_VT-facts.json**
- added: `vt.bik.vt_saves.employer_threshold_w2_employees` = 2 (2026-01-01, US-VTB5-003); `vt.bik.vt_saves.rule` = Vermont Saves state auto-IRA (Roth IRA defaul… (2026-01-01, US-VTB5-003); `vt.bik.vt_saves.penalty.max_per_employee` = 20 (2026-01-01, US-VTB5-003); `vt.bik.vt_saves.penalty.max_per_employee` = 75 (2026-10-01, US-VTB5-003)
- changed: `vt.sui.wage_base` (2026-01-01): note_append

**CCG-annex_PA-facts.json**
- added: `pa.leave.pittsburgh.accrual.hours_worked_per_hour` = 30 (2026-01-01, US-PAB5-001); `pa.leave.pittsburgh.annual_cap_hours.15plus` = 72 (2026-01-01, US-PAB5-001); `pa.leave.pittsburgh.annual_cap_hours.under15` = 48 (2026-01-01, US-PAB5-001); `pa.leave.pittsburgh.waiting_period_days` = 90 (2026-01-01, US-PAB5-001); `pa.leave.pittsburgh.payout_at_separation` = False (2026-01-01, US-PAB5-001); `pa.leave.pittsburgh.rule` = Carryover required unless the employer front-… (2026-01-01, US-PAB5-001)

**CCG-annex_NM-facts.json**
- added: `nm.labour.minwage.local.las_cruces.hourly` = 13.01 (2026-01-01, US-NMB5-001); `nm.labour.minwage.local.las_cruces.hourly` = 13.47 (2027-01-01, US-NMB5-001); `nm.labour.minwage.local.las_cruces.tipped.hourly` = 5.2 (2026-01-01, US-NMB5-001); `nm.labour.minwage.local.las_cruces.tipped.hourly` = 5.39 (2027-01-01, US-NMB5-001); `nm.labour.minwage.local.bernalillo_county.hourly` = 10.95 (2026-01-01, US-NMB5-002)

**CCG-annex_AR-facts.json**
- added: `ar.pit.rate.top` = 3.7 (2026-01-01, US-ARB5-001); `ar.pit.high_income.threshold` = 94700 (2026-01-01, US-ARB5-001); `ar.pit.statute.tables` = Net income <= 94,700: 0-5,599 0%; 5,600-11,19… (2026-01-01, US-ARB5-001)

**CCG-annex_OH-facts.json**
- added: `oh.pit.school_district.full_list` = ODT 'A list of Ohio's School District Income … (2026-01-01, US-OHB5-001); `oh.pit.school_district.count` = 214 (2026-01-01, US-OHB5-001); `oh.pit.school_district.earned_income_base.count` = 68 (2026-01-01, US-OHB5-001); `oh.pit.municipal.rate_table` = The Finder OHMuniRateTable.csv (Ohio Departme… (2026-01-01, US-OHB5-002); `oh.pit.municipal.count_in_force` = 678 (2026-11-01, US-OHB5-002); `oh.pit.municipal.columbus.rate` = 2.5 (2009-10-01, US-OHB5-002); `oh.pit.municipal.cleveland.rate` = 2.5 (2017-01-01, US-OHB5-002); `oh.pit.municipal.cincinnati.rate` = 1.8 (2020-10-01, US-OHB5-002); `oh.pit.municipal.dayton.rate` = 2.5 (2017-01-01, US-OHB5-002); `oh.pit.municipal.toledo.rate` = 2.5 (2021-01-01, US-OHB5-002); `oh.pit.municipal.akron.rate` = 2.5 (2018-01-01, US-OHB5-002); `oh.pit.municipal.youngstown.rate` = 2.75 (2003-01-01, US-OHB5-002)

**DD-8_sheets-facts.json**
- added: `dd.oh.municipal_rate_table` = Ohio municipality of work carried as the 5-di… (2026-01-01, US-OHB5-002); `dd.ct.pfml.employee_level_data` = none: the CT Paid Leave return carries employ… (2026-10-05, US-CTB5-001); `dd.wa.pfml_ltc.employee_fields` = Per employee for the Paid Leave/WA Cares repo… (2026-06-26, US-WAB5-003)

**CCG-annex_NY-facts.json**
- added: `ny.pfl.employee.rate` = 0.452 (2027-01-01, US-NYB5-001); `ny.pfl.employee.max_annual` = 451.81 (2027-01-01, US-NYB5-001); `ny.pfl.nysaww` = 1833.63 (2026-01-01, US-NYB5-002); `ny.pfl.benefit.max_weekly` = 1228.53 (2026-01-01, US-NYB5-002); `ny.pfl.benefit.rate_of_aww` = 67 (2026-01-01, US-NYB5-002); `ny.leave.nyc_pto.unpaid_hours_immediate` = 32 (2026-02-22, US-NYB5-003); `ny.leave.nyc_pto.paid_hours.max.under100` = 40 (2026-02-22, US-NYB5-003); `ny.leave.nyc_pto.paid_hours.max.100plus` = 56 (2026-02-22, US-NYB5-003); `ny.leave.nyc_pto.prenatal_paid_hours` = 20 (2026-02-22, US-NYB5-003); `ny.leave.nyc_pto.pay_statement_items` = Each pay period, on the pay statement or othe… (2026-02-22, US-NYB5-003)

**PSL-facts.json**
- added: `psl.nyc.pto.on_statement` = NYC Earned Safe and Sick Time (Protected Time… (2026-02-22, US-NYB5-003)

**CCG-annex_CT-facts.json**
- added: `ct.report.pfml.file_spec` = CT Paid Leave File Specification Toolkit v2.1… (2026-10-05, US-CTB5-001); `ct.pfml.wages.fica_basis` = For FICA-covered employees, CTPL wages exclud… (2026-10-05, US-CTB5-001)

**CCG-annex_WA-facts.json**
- added: `wa.report.pfml_ltc.fields` = Combined Paid Leave + WA Cares quarterly repo… (2026-06-26, US-WAB5-003); `wa.report.pfml_ltc.due` = Last day of the month after each quarter: Apr… (2026-06-26, US-WAB5-003); `wa.report.pfml_ltc.no_payroll_report` = True (2026-06-26, US-WAB5-003); `wa.report.pfml_ltc.channels` = Manual entry (up to 50 employees), single CSV… (2026-06-26, US-WAB5-003); `wa.pfml.penalties.from` = 2026-08-01 (2026-08-01, US-WAB5-002); `wa.cares.base.same_as_pfml` = True (2026-06-26, US-WAB5-003)

**CCG-annex_MA-facts.json**
- added: `ma.sui.rate_schedule.selection` = Schedule A-G by Unemployment Compensation Fun… (2015-01-01, US-MAB5-001); `ma.sui.rate_schedule.table` = 45 account-reserve rows x 7 schedules (positi… (2015-01-01, US-MAB5-001); `ma.sui.rate_schedule.in_force` = E (2026-01-01, US-MAB5-001)

**CCG-annex_UT-facts.json**
- added: `ut.sdi_pfml.exists` = False (2026-01-01, US-UTB5-003)

**CCG-annex_MI-facts.json**
- added: `mi.newhire.report_days` = 20 (2026-01-01, US-MIB5-001); `mi.newhire.fields` = Employee SSN, name, address, date of birth (o… (2026-01-01, US-MIB5-001); `mi.newhire.channels` = Michigan New Hires Operation Center (MDHHS Ch… (2026-01-01, US-MIB5-001); `mi.newhire.rehire_gap_days` = 60 (2026-01-01, US-MIB5-001)

**CCG-annex_FED-facts.json**
- added: `fed.newhire.electronic_interval` = Electronic/magnetic filers: two monthly trans… (1997-10-01, US-FEDB5-001); `fed.newhire.state_penalty.max_per_hire` = 25 (1997-10-01, US-FEDB5-001); `fed.newhire.state_penalty.conspiracy.max_per_hire` = 500 (1997-10-01, US-FEDB5-001); `fed.newhire.form` = W-4 copy or an equivalent form; seven federal… (1997-10-01, US-FEDB5-001); `fed.efw2.edition` = SSA Publication No. 42-007, EFW2 Tax Year 202… (2026-01-01, US-FEDS5-032); `fed.efw2.record_length` = 512 (2026-01-01, US-FEDS5-032); `fed.efw2.records` = 512-byte records in order RA, RE, RW, [RO], [… (2026-01-01, US-FEDS5-032); `fed.efw2.ty2026_changes` = TY2026 changes: RE adds Employer Signature PI… (2026-01-01, US-FEDS5-032)

**CCG-m10_reporting-facts.json**
- added: `fed.efw2.ty2026_changes` = TY2026 changes: RE adds Employer Signature PI… (2026-01-01, US-FEDS5-032); `fed.efw2.record_length` = 512 (2026-01-01, US-FEDS5-032)

### Decisions taken in this pass

1. **FAMLI duplicate key.** Kept `co.famli.total.rate`, the WTC/m05 convention (`{st}.pfml.total.rate`, `md.famli.total.rate`); it has no year in the key. In CCG-annex_CO, both `co.famli.rate.total.2026` (2026, 0.88) and `co.famli.rate.total` (2027, 0.86) were renamed to `co.famli.total.rate`. No alias was kept, and the pack text was updated. A grep of BASE found no deliverable outside `_research/` that cites either old key. **Residual convention split, not fixed here:** the CCG annexes use `{st}.pfml.rate.total` (DE, MD, MN, OR, WA; MA `.25_plus/.under_25`; ME `.15_plus/.under_15`), while WTC/m05 use `{st}.pfml.total.rate` for the same concepts. Agent 4 or the orchestrator has to choose one convention.
2. **CO PAY CALC 2026** (US-COB5-001, A.1): co.minwage.hourly 15.16, tip credit 3.02, tipped 12.14 and EAP 57,784/yr were re-pointed from the COMPS poster to the Order (`second independent authority`). New: minors 12.89, EAP weekly 1,111.23, computer 34.85/h, highly compensated 130,014, wage-claim ceiling 7,500 → 13,000 from 2026-07-01. FAMLI 2026 split 0.44/0.44 plus the 9-or-fewer rule (US-COB5-003) is in annex_CO and WTC. The 2027 values stay out of facts (`co.minwage.hourly.next_year`, non-blocking).
3. **WA deferrals** (medium confidence): recorded as a `_decision_note` on `wa.ui_pfml_ltc.deferrals` (annex_WA) and on `wa.base.125_401k.ui_pfml_cares` (WTC). It is **not a fact**. The reading: treat employee 125/401(k)/HSA elective deferrals as INCLUDED in PFML and WA Cares wages, because WAC 192-510-025 and toolkit v25.1 give no exclusion; only employer plan payments are excluded. Both entries are now **blocking=false**, since the builder has a rule. UI wages stay silent. Set them back to blocking if the build should wait for an explicit ESD statement.
4. **MA UI schedule** (G-DERIVE): the 2026 published min 0.94 / max 14.37 (US-MAS5-020) match only column E of schedules A-G (US-MAB5-001), so `ma.sui.rate_schedule.in_force` = E (2026), `derived arithmetically` (annex_MA and WTC).
5. **Ohio** (G-SPOT): OHMuniRateTable.csv counts re-run locally: 1,083 rows; 678 FIPS in force on 2026-11-01; Columbus 2.50, Cleveland 2.50, Cincinnati 1.80, Dayton 2.50, Toledo 2.50, Akron 2.50, Youngstown 2.75; max Bedford 3.00. Resident credit and collector remain open (`oh.pit.municipal.resident_credit_and_collector`, non-blocking).
6. **Narrowed rather than closed** where the new row covers only part of the gap: `co.local_minwage.other_cities` (still blocking); `nm.labour.minwage.local.other` (now Santa Fe County only, still blocking); `az.report.sui.quarterly` → `az.ui.separation_notice_and_domestic_threshold`; `rspec.az.ui_qtr.form_due_format` → `rspec.az.ui_qtr.efile_mandate`; `rspec.wa.pfml_ltc_qtr.fields_due` → `rspec.wa.lni_wc_qtr.report` (blocking: the L&I quarterly report was not obtained).
7. Facts on rows without a register `effective_from` use 2026-01-01 with `_effective_from_basis` (the SIR convention). Twelve new active rows have no `effective_from`: US-DCB5-002, UTB5-001..004, FEDB5-001, MIB5-001, AZB5-004/-005, TNB5-002, VTB5-002/-003 (page or procedure rows). This is a C41 point for the scaffolder or auditor; no date was invented here.
8. Upgrades of existing facts by second sources: AR top rate 3.7 now also has the statute (US-ARB5-001, A.1); the VT UI base 15,400 is restated on the live VDOL page (US-VTB5-001); `rspec.mi.new_hire.channel` is re-pointed from US-FED-017 to US-MIB5-001. The NY PFL 2026 max weekly benefit is 1,228.53 as quoted (1,833.63 × 0.67), not the earlier derived 1,228.54.

## 3. EFW2 TY2026 (US-FEDS5-032)

Read from the local PDF (pdftotext -layout), cross-checking the record grids, the field specifications and the Appendix mapping. Records are 512 bytes. RA, RE, RW, RT and RF are required; RO, RS, RU and RV are optional, and SSA/IRS do not process RS/RV. TY2026 changes and positions:

- **RE:** Employer Signature PIN at 319-328 (S-XXXXXX-Y, Luhn check digit; blanks if none).
- **RW:** Primary/Secondary Treasury Tipped Occupation Code at 490-492 / 493-495. One summary table extracted from the PDF is shifted by one field (it shows 493-495 as Primary). The record grid, the field specification and the Appendix mapping all give 490-492 / 493-495.
- **RO:** Code A 155-165, B 166-176, J 177-187, K 188-198, L 199-209, P 210-220, TA 221-231, TP 232-242, TT 243-253. The combined A+B field at 23-33 is valid for TY1978-2025 only.
- **RU:** A 205-219, B 220-234, J 235-249, K 250-264, L 265-279, P 280-294, TA 295-309, TP 310-324, TT 325-339.
- **RS** (full state layout): state account 248-267, state code 274-275, wages/tax 276-297, other state data 298-307, tax type 308 (C/D/E/F), local 309-330, supplemental 338-487.
- **RV:** 3-512. **RF:** RW count at 8-16.

Facts: `fed.efw2.*` (annex_FED, m10), `rspec.fed.efw2.*` (10 keys), `sir.fed.efw2.*` (3 keys). Closed: `rspec.fed.efw2.ty2026_spec` (blocking), `sir.fed.efw2.layout_ty2026` (blocking), `fed.efw2.layout` (annex_FED and m10).

## 4. Unresolved closed (removed from facts and from the packs' Open questions)

- CCG-annex_AZ-facts.json: `az.minwage.hourly`, `az.local_minwage.flagstaff.hourly`, `az.report.sui.quarterly`
- RSPEC-facts.json: `rspec.ct.pfml_qtr.file_spec`, `rspec.wa.pfml_ltc_qtr.fields_due`, `rspec.fed.efw2.ty2026_spec`, `rspec.az.ui_qtr.form_due_format`
- SIR-facts.json: `sir.fed.efw2.layout_ty2026`, `sir.ct.paid_leave.file_spec`
- WTC-country_specific-facts.json: `oh.local.municipal.rate_table`, `oh.local.school_district.full_list_2026`, `ny.pfl.employee.rate.2027`
- CCG-annex_TN-facts.json: `tn.live.bwc_2026`, `tn.labour.child_labour`
- CCG-annex_VT-facts.json: `vt.bik.vt_saves`
- CCG-annex_PA-facts.json: `pa.leave.pittsburgh.accrual`
- CCG-annex_OH-facts.json: `oh.pit.municipal.rate_table`, `oh.pit.school_district.full_list`
- DD-8_sheets-facts.json: `dd.oh.municipal_rate_table`
- CCG-annex_NY-facts.json: `ny.pfl.employee.rate.next_year`, `ny.pfl.benefit.max_weekly`, `ny.leave.nyc_pto`
- PSL-facts.json: `psl.nyc.pto.on_statement`
- CCG-annex_CT-facts.json: `ct.report.pfml.file_spec`
- CCG-annex_WA-facts.json: `wa.report.pfml_ltc.fields`
- CCG-annex_UT-facts.json: `ut.sdi_pfml.exists`
- CCG-annex_FED-facts.json: `fed.efw2.layout`
- CCG-m10_reporting-facts.json: `fed.efw2.layout`

Unresolved added (narrowed remainders or new gaps): `az.ui.separation_notice_and_domestic_threshold` (CCG-annex_AZ-facts.json, non-blocking); `rspec.wa.lni_wc_qtr.report` (RSPEC-facts.json, blocking); `rspec.az.ui_qtr.efile_mandate` (RSPEC-facts.json, non-blocking); `co.minwage.hourly.next_year` (CCG-annex_CO-facts.json, non-blocking); `vt.bik.vt_saves.default_contribution_rate` (CCG-annex_VT-facts.json, non-blocking); `oh.pit.municipal.resident_credit_and_collector` (CCG-annex_OH-facts.json, non-blocking).

New attempts recorded on still-open items, none closed: ut.pit.schedule.effective_date / ut.pit.supplemental (+ WTC ut.sit.*); dc.wh.method / dc.sit.method.2026 / dc.oracle.method_2026 / sir.w2.state_specs_ty2026; wy.ui.rates.2026_values / wy.report.file_formats / wy.sui.rates.2026; mi.newhire.statute / rspec.mi.new_hire.statute / sir.mi.new_hire.statute; multi.newhire(.multistate)_registration_channel; ar.wh.formula.switch_date / ar.sit.table_switch_date; co.famli.split.next_year / co.famli.split.2027; vt.ui.schedule.rate_year_2026_07 / vt.sui.schedule.2026_07.

Packs: each touched pack has a new `## Synthesis D additions (2026-11-02)` section before `## Open questions`. Closed lines were removed, and narrowed or new lines appended. Mirror check after the edit: in all 24 touched packs, the Open-questions keys equal the facts file's `unresolved[]` keys (0 missing, 0 extra).

## 5. consumed_by appended

US-ARB5-001: CCG/annex_AR; US-ARS5-001: WTC/country_specific; US-AZB5-001: CCG/annex_AZ; US-AZB5-002: CCG/annex_AZ; US-AZB5-003: CCG/annex_AZ; US-AZB5-004: CCG/annex_AZ, RSPEC; US-AZB5-005: CCG/annex_AZ, RSPEC, SIR/third_party_provider_handoff; US-AZB5-006: CCG/annex_AZ, RSPEC; US-COB5-001: CCG/annex_CO; US-COB5-003: CCG/annex_CO, WTC/country_specific; US-CTB5-001: CCG/annex_CT, DD/8_sheets, RSPEC, SIR/third_party_provider_handoff, WTC/country_specific; US-FEDB5-001: CCG/annex_FED, RSPEC; US-FEDS5-032: CCG/annex_FED, CCG/m10_reporting, RSPEC, SIR/third_party_provider_handoff; US-FIL-002: SIR/third_party_provider_handoff; US-MAB5-001: CCG/annex_MA, WTC/country_specific; US-MIB5-001: CCG/annex_MI, RSPEC, SIR/third_party_provider_handoff; US-NMB5-001: CCG/annex_NM; US-NMB5-002: CCG/annex_NM; US-NYB5-001: CCG/annex_NY, WTC/country_specific; US-NYB5-002: CCG/annex_NY; US-NYB5-003: CCG/annex_NY, PSL/8_sheets; US-NYP8-001: WTC/country_specific; US-OHB5-001: CCG/annex_OH, RSPEC, WTC/country_specific; US-OHB5-002: CCG/annex_OH, DD/8_sheets, RSPEC, WTC/country_specific; US-PAB5-001: CCG/annex_PA; US-TNB5-001: CCG/annex_TN; US-TNB5-002: CCG/annex_TN; US-UTB5-003: CCG/annex_UT; US-VTB5-003: CCG/annex_VT; US-VTS5-004: CCG/annex_VT, WTC/country_specific; US-WAB5-002: CCG/annex_WA, RSPEC, WTC/country_specific; US-WAB5-003: CCG/annex_WA, DD/8_sheets, RSPEC, WTC/country_specific; US-WAB5-004: RSPEC.

New rows cited by no fact (consumed_by left empty on purpose; cited only in `attempted[]`, or provisional): US-DCB5-001, US-DCB5-002, US-UTB5-001, US-UTB5-002, US-UTB5-004, US-WAB5-001, US-WYB5-001, US-COB5-002, US-VTB5-001, US-VTB5-002.

## 6. Remaining blocking unresolved per artifact

- **CCG** (42 blocking of 510 open): `al.local.occupational_tax.census` (CCG-annex_AL), `ar.wh.formula.switch_date` (CCG-annex_AR), `ca.local_minwage.hourly` (CCG-annex_CA), `ca.industry_minwage.fast_food_health_care` (CCG-annex_CA), `co.famli.split.next_year` (CCG-annex_CO), `co.local_minwage.other_cities` (CCG-annex_CO), `ct.wh.tables.per_period` (CCG-annex_CT), `dc.wh.method` (CCG-annex_DC), `dc.live.fy2027_bsa_permanent` (CCG-annex_DC), `de.wh.w4_2020_mapping` (CCG-annex_DE), `fl.sui.wages.401k_deferral` (CCG-annex_FL), `ga.report.w2.rs_layout.current` (CCG-annex_GA), `ga.pit.rate.next_year` (CCG-annex_GA), `hi.wh.bracket.next_year` (CCG-annex_HI), `id.wh.certificate.current_edition` (CCG-annex_ID), `il.leave.chicago.paid_leave.payout` (CCG-annex_IL), `il.leave.cook.paid_leave` (CCG-annex_IL), `ky.local.occupational_tax.census` (CCG-annex_KY), `la.nonres.mobile_workforce.catch_up` (CCG-annex_LA), `la.pit.conformity` (CCG-annex_LA), `ma.report.w2.due_date_conflict` (CCG-annex_MA), `ma.pit.conformity.items` (CCG-annex_MA), `me.sui.upaf.rate.conflict` (CCG-annex_ME), `mi.local.cities.rates` (CCG-annex_MI), `mt.minwage.hourly.next_year` (CCG-annex_MT), `nc.pit.rate.next_year` (CCG-annex_NC), `ne.minwage.hourly.next_year` (CCG-annex_NE), `nm.labour.minwage.local.other` (CCG-annex_NM), `ny.pit.supplemental.local_rates` (CCG-annex_NY), `or.pit.local.multnomah_pfa.step_year` (CCG-annex_OR), `ri.records.2026_version` (CCG-annex_RI), `sc.pit.tables.post_act110` (CCG-annex_SC), `tx.report.ui.enhanced_fields_layout` (CCG-annex_TX), `ut.pit.schedule.effective_date` (CCG-annex_UT), `va.pit.formula.next_year` (CCG-annex_VA), `va.ui.pool_cost_and_new_employer` (CCG-annex_VA), `vt.minwage.hourly.next_year` (CCG-annex_VT), `wa.labour.minwage.local.next_year` (CCG-annex_WA), `wv.pit.tables.start_date` (CCG-annex_WV), `wv.pit.local.service_fees` (CCG-annex_WV), `wv.ui.sb1053_fee` (CCG-annex_WV), `wy.ui.rates.2026_values` (CCG-annex_WY)
- **RSPEC** (22 blocking of 47 open): `rspec.ca.ui_qtr.de9c_file_spec` (RSPEC), `rspec.co.ui_qtr.format_due` (RSPEC), `rspec.de.ui_qtr.file_format` (RSPEC), `rspec.ga.w2_state.ty2026_layout` (RSPEC), `rspec.ia.ui_qtr.wage_detail_layout` (RSPEC), `rspec.id.w2_state.state_record_spec` (RSPEC), `rspec.il.w2_state.idr986_spec` (RSPEC), `rspec.in.wh_return.xml_schema` (RSPEC), `rspec.ky.w2_state.rs_spec` (RSPEC), `rspec.la.w2_state.lawage_format` (RSPEC), `rspec.me.w2_state.bulk_spec` (RSPEC), `rspec.mn.ui_qtr.due_format` (RSPEC), `rspec.mt.ui_qtr.efiling_handbook` (RSPEC), `rspec.nc.w2_state.ty2026_spec` (RSPEC), `rspec.nm.tap.bulk_schema` (RSPEC), `rspec.oh.ui_qtr.channel_format` (RSPEC), `rspec.ok.ui_qtr.due_date` (RSPEC), `rspec.tx.ui_qtr.due_date` (RSPEC), `rspec.tx.ui_qtr.enhanced_layout` (RSPEC), `rspec.ut.ui_qtr.wage_file_layout` (RSPEC), `rspec.vt.w2_state.format` (RSPEC), `rspec.wa.lni_wc_qtr.report` (RSPEC)
- **WTC** (2 blocking of 73 open): `dc.sit.method.2026` (WTC-country_specific), `ut.sit.schedule.effective_date` (WTC-country_specific)
- **DD**: 0 blocking (2 open, all non-blocking)
- **PSL**: 0 blocking (11 open, all non-blocking)
- **SIR**: 0 blocking (13 open, all non-blocking)

## 7. Validator

`python ~/mercans-pipeline/shared/schemas/validate_contract.py facts <file>` on every facts file touched (25 files, 25 PASS):

```
CCG-annex_AR-facts.json: PASS  (1 file)
CCG-annex_AZ-facts.json: PASS  (1 file)
CCG-annex_CO-facts.json: PASS  (1 file)
CCG-annex_CT-facts.json: PASS  (1 file)
CCG-annex_DC-facts.json: PASS  (1 file)
CCG-annex_FED-facts.json: PASS  (1 file)
CCG-annex_MA-facts.json: PASS  (1 file)
CCG-annex_MI-facts.json: PASS  (1 file)
CCG-annex_MULTI-facts.json: PASS  (1 file)
CCG-annex_NM-facts.json: PASS  (1 file)
CCG-annex_NY-facts.json: PASS  (1 file)
CCG-annex_OH-facts.json: PASS  (1 file)
CCG-annex_PA-facts.json: PASS  (1 file)
CCG-annex_TN-facts.json: PASS  (1 file)
CCG-annex_UT-facts.json: PASS  (1 file)
CCG-annex_VT-facts.json: PASS  (1 file)
CCG-annex_WA-facts.json: PASS  (1 file)
CCG-annex_WY-facts.json: PASS  (1 file)
CCG-m10_reporting-facts.json: PASS  (1 file)
CCG-m12_worked_examples-facts.json: PASS  (1 file)
DD-8_sheets-facts.json: PASS  (1 file)
PSL-facts.json: PASS  (1 file)
RSPEC-facts.json: PASS  (1 file)
SIR-facts.json: PASS  (1 file)
WTC-country_specific-facts.json: PASS  (1 file)
```

## 8. Shape of the remaining work

The CO, NM, WA and AZ remainders are independent per-jurisdiction browser reads (coloradolaborlaw.gov + Denver Labor; Santa Fe County; lni.wa.gov; the DES e-file rule) and can run in parallel. The blocking state file-spec items in RSPEC are about 20 independent lookups; several hosts (ME, TX, LA, HI, MO, SC) need a US exit IP per browser pass P2.

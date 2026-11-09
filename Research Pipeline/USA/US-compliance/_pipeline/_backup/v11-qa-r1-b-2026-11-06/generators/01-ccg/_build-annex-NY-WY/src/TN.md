## @labour
- **Minimum wage:** no state minimum-wage law (exists: {{tn.labour.minwage.state.exists}}); FLSA-covered employers pay the federal rate (Annex FED) [US-TNS5-011]. Local minimum wages are reported as preempted (T.C.A. 7-51-1802) on secondary sources only; not modelled as a rule.
- **Overtime:** {{tn.labour.overtime.state_rule}} [US-TNS5-001].
- **Pay frequency and timing (T.C.A. 50-2-103(a)) [US-TNS5-001]:** {{tn.pay_frequency.rule}}, with statutory due dates for wages earned in the first and second half of the month. Piece-work and commission timing from 2026-07-01 (PC 617): open point below.
- **Meal break (50-2-103(h)):** {{tn.labour.meal_break.minutes}} minutes unpaid for a scheduled run of consecutive hours, unless the business gives ample chance to rest [US-TNS5-001].
- **Minors [US-TNB5-002]:** hours: {{tn.labour.child_labour.hours}} Unpaid break of {{tn.labour.child_labour.break_minutes}} minutes for minors on the statutory schedule (50-5-115); no waiver.
- **Method of payment:** not read (open point below).

## @income_tax
- **No state tax on wages and no withholding** (income tax exists: {{tn.pit.exists}}); the Hall tax on interest and dividends was repealed from 2021-01-01; no state W-4, supplemental rate or state W-2 [US-TN-001, US-TNP51-001].
- **No local wage tax** (exists: {{tn.local_wage_tax.exists}}) [US-TNP52-001].
- **Resident and nonresident matrix.** Nothing is withheld for Tennessee for any income type; a Tennessee resident working in a wage-taxing state is withheld for that state (Annex MULTI).

## @social
- **Unemployment insurance (DLWD) [US-TNS5-002, US-TNS5-003, US-TNS5-004].** Taxable wage base {{tn.sui.wage_base}} USD (set by the Trust Fund level, not by an index). Rate table in force: {{tn.ui.rate_table.in_effect}} (the Trust Fund balance on June 30 and December 31 decides the table for the next six months, T.C.A. 50-7-403). Range {{tn.sui.employer.rate.min}} % to {{tn.sui.employer.rate.max}} %. New employer {{tn.sui.new_employer.rate}} % (manufacturing sectors use a sector rate); experience rating after the statutory qualifying period. Employee contribution {{tn.sui.employee.rate}} % [US-TNR3-003].
- **Liability thresholds** (FUTA-liable employers, quarterly wage and 20-week tests, domestic, agricultural, nonprofit and government rules) and PEO reporting per client: US-TNS5-013.
- **No SDI, TDI, PFML, LTC, transit or workforce levy** (exists: {{tn.sdi_pfml.exists}}) [US-TNR3-003, US-TNP52-001].
- **Workers' compensation (benefit side, not payroll) [US-TNB5-001]:** for injuries from 2026-07-01 to 2027-06-30, maximum weekly temporary total disability benefit {{tn.wc.benefit.ttd.weekly_max}} USD, maximum weekly permanent partial disability benefit {{tn.wc.benefit.ppd.weekly_max}} USD, minimum weekly benefit {{tn.wc.benefit.weekly_min}} USD. These are insurer benefits, not payroll deductions.

## @payslip
- **No itemised pay-statement statute** (exists: {{tn.payslip.statute.exists}}) [US-TNP51-003, US-TNS5-001]; federal recordkeeping applies. Retention beyond UI records: open point below.

## @reporting
- **No state withholding return or state W-2.**
- **Quarterly UI report [US-TNS5-005, US-TNS5-007, US-TNS5-014]:** Wage Report LB-0851 and Premium Report LB-0456, due {{tn.report.ui.quarterly_due}}; filed in Employer e-Services (manual entry, abbreviated ICESA, short text file or full ICESA).
- **New hire [US-TNS5-008, US-TNS5-009]:** within {{tn.newhire.report_days}} days of hire, to TN DHS (not the UI system).
- **Registration and TPA access:** Employer e-Services; no POA needed since 2025-05-27 [US-TNS5-005, US-TNR3-002].

## @leave
- **No mandatory paid sick leave, vacation or PFML** (sick leave statute exists: {{tn.leave.sick.state_statute.exists}}) [US-TNS5-001].
- **Jury duty (T.C.A. 22-4-108):** the employer pays wages during jury service less the court's pay (paid: {{tn.leave.jury_duty.paid}}) [US-TNS5-012].
- **Voting and parental leave:** protected; the pay rules rest on leads only (open point below) [US-TNS5-012]. Military leave protected (8-33-101 ff.).

## @termination
- **Final pay (50-2-103(g)) [US-TNS5-001]:** {{tn.final_pay.rule}}, for discharge and resignation alike.
- **Accrued vacation:** {{tn.term.vacation.payout}} (50-2-103(a)(3)).
- **Separation Notice LB-0489 [US-TNS5-007]:** handed or mailed to the employee within {{tn.term.separation_notice.hours}} hours of separation (Rule 0800-09-01-.02), except very short employment or a short recall. The form reports severance pay, wages in lieu of notice and vacation pay on temporary layoff, so payroll must supply those amounts.
- **Tennessee WARN:** notice duty at {{tn.term.warn.employee_threshold}} or more full-time employees [US-TNS5-006]. IWO terminations reported to the child-support office [US-TNS5-009].

## @bik
- **Income tax:** not applicable (no state wage tax). UI wage exclusions not read (open point below) [US-TNP51-001].

## @deductions
- **Wage deductions (50-2-110(a)(2)):** an offset for amounts the employee owes needs a prior signed written agreement [US-TNS5-001].
- **Ordinary garnishment (T.C.A. 26-2-404(b)) [US-TNS5-010]:** withhold the lesser of {{tn.garn.creditor.max_percent}} % of disposable earnings or disposable earnings above thirty times the federal minimum wage per week (CCPA, Annex FED); then subtract {{tn.garn.consumer.child_reduction.weekly}} USD per week for each dependent child under 16 living in Tennessee (prorated for longer pay periods). Tennessee departs from the CCPA through this child reduction.
- **Child support and alimony:** CCPA support percentages or the ordered amount if lower [US-TNS5-010]. **IWO:** remit to the Tennessee SDU within {{tn.garn.iwo.remit_days}} days of payday; report lump sums [US-TNS5-009]. Fee and priority: open point below.

## @cba
- **Prevailing Wage Act (T.C.A. 12-4-401 ff.) [US-TNP51-002]:** scope {{tn.prevailing_wage.scope}}; 2026 craft rates, for example unskilled laborer {{tn.prevailing_wage.unskilled_laborer.hourly}} USD per hour. Certified payroll format: open point below.

## @indexation
- **SUI wage base and rate table:** set by the Trust Fund level, reset every six months [US-TNS5-002]. No minimum wage to index; prevailing highway rates re-surveyed yearly [US-TNP51-002].

## @data
- No SSN-truncation rule for pay statements located on an A-tier source; SSN display rules and the employee-data scope of the Tennessee Information Protection Act are open (below).

## @live
- **2026-07-01:** PC 617 piece-work and commission timing (not configured in this release; see the open point below). Workers' compensation acts of 2026: {{tn.live.bwc_2026}} [US-TNB5-001].
- **2025-05-27:** UI tax system moved to Employer e-Services [US-TNS5-005, US-TNR3-002].
- **2026 SUI:** no change [US-TNS5-002]. No 2027 enactment located (sweep incomplete).

## @special
| Population | Tennessee rule | Register id |
|---|---|---|
| Domestic / household | UI coverage above a quarterly cash test; household employers register | US-TNS5-013, US-TNS5-005 |
| Agricultural | UI coverage tests | US-TNS5-013 |
| Minors | Child Labor Act hours and break rules (Section 1); no state minor wage rate | US-TNB5-002 |
| Tipped | No state rule; FLSA only | US-TNS5-011 |
| Clergy / religious | No state rule beyond federal; UI exclusion not read | - |
| Students | No state rule beyond federal located; UI exclusions not read | - |
| Nonresident aliens | No state withholding, no state effect | US-TNP51-001 |
| Statutory employees | No state rule beyond federal | US-TNP51-001 |
| Government employees | UI liability covers all state and local government units | US-TNS5-013 |
| Seasonal employers | Seasonal election with notice to workers | US-TNS5-013 |
| PEO clients | Separate reports per client, aggregate rate, joint liability unless bonded | US-TNS5-013 |

## @gaps
- tn.ui.wage_definition :: The SUI wage exclusions (cafeteria plans, retirement deferrals, tips, students, clergy, corporate officers) were not read. :: T.C.A. 50-7-207, 50-7-213 or the DLWD employer handbook.

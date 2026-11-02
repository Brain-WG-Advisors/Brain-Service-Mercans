## @labour
- **Minimum wage [US-WVS5-007, US-WVS5-005]:** {{wv.minwage.hourly}} USD per hour since 2016-01-01; no 2026 change and no 2027 rate (HB 5485 died in committee) [US-WVS5-017]. The state law applies where at least {{wv.labour.minwage.coverage_min_employees_at_location}} non-exempt employees work at one distinct permanent location (counted per location; home and client sites count where the work is done); otherwise the federal minimum applies (Annex FED). Exclusions in 21-5C-1(f).
- **Tipped employees [US-WVS5-007]:** cash wage {{wv.minwage.tipped.cash_wage}} USD per hour with written tip records; tip pools only among tip-eligible staff. Meal credit {{wv.labour.meal_credit.daily}} USD per day.
- **Overtime [US-WVS5-004, US-WVS5-005]:** {{wv.overtime.premium.multiplier}} times the regular rate over {{wv.overtime.weekly_threshold_hours}} hours per workweek; no daily overtime; state overtime does not apply where most of the workforce is FLSA-covered, so most employers apply the state minimum wage and federal overtime.
- **Local minimum wages:** none found (open point below).
- **Pay frequency (21-5-3; 42 CSR 5 s.7) [US-WVS5-009, US-WVS5-008]:** {{wv.pay_frequency.rule}}; a payday on a closed day moves to the preceding open day.
- **Method of payment [US-WVS5-009]:** {{wv.payment.method}}; the employer must offer direct deposit.
- **Notices:** rate, payday and place at hire; written notice of changes one full pay period ahead [US-WVS5-008, US-WVS5-009].

## @income_tax
- **Method (IT-100.2A, March 2026) [US-WVP51-005]:** {{wv.wh.method}}. Exemption {{wv.pit.exemption.annual}} USD per year. Certificate: {{wv.wh.certificate}} [US-WVS5-011]; the one-earner box on the IT-104 selects the optional table.
- **Two tables.**

| Table | Annual bracket thresholds (USD) | Rates (%) | Register id |
|---|---|---|---|
| Two earner / two or more jobs (default) | {{wv.pit.wh.two_earner.thresholds}} | same rate ladder as the statute | US-WVP51-005 |
| Optional one earner / one job (= statutory brackets) | {{wv.pit.statutory.thresholds}} | {{wv.pit.statutory.rates}} | US-WVS5-012 |

  Top statutory rate {{wv.pit.statutory.rate.top}} % (SB 392 of 2026: rate cut retroactive to 2026-01-01; married filing separately brackets are half) [US-WVS5-012]. The date from which employers must apply the March 2026 tables is not stated (blocking open point below).
- **Supplemental wages and rounding:** no flat rate; supplemental pay runs through the annual table by the aggregate method (partial source); no rounding rule found (open point below) [US-WVP52-007].
- **Wages subject to withholding** follow the federal definition, including bonuses, vacation allowances, back pay, tips and retroactive increases [US-WVS5-010].
- **Residents and nonresidents [US-WVPIT-001, US-WVS5-010, US-WVS5-011]:** residents and nonresidents are withheld, by resident and nonresident employers alike. Exceptions: reciprocity {{wv.reciprocity.states}}; nonresidents whose West Virginia duties last {{wv.pit.nonresident.days_rule}} days or less across several states (not athletes, entertainers or public figures); nonresident Armed Forces members and MSRRA spouses. Allocation by time records or the employee's written statement. Nonresident credit only under a written interstate agreement [US-WVP51-002].
- **Local:** no local income tax (exists: {{wv.pit.local.income_tax.exists}}) [US-WVR3-001]. Municipal weekly **service fees** (W. Va. Code 8-13-13) are withheld from employees and remitted to the city (T4 layer): Charleston {{wv.pit.local.charleston.service_fee.weekly}} USD per week [US-WVR3-002]. Fees of other cities rest on tier-B leads and are not stated (blocking open point below).
- **Resident and nonresident matrix.**

| Income type | West Virginia resident | Nonresident |
|---|---|---|
| Regular salary | IT-100.2A two-earner table (or one-earner table if elected) | Same tables on West Virginia wages, unless reciprocity (IT-104NR), the short-duty rule or a military exemption applies |
| Bonus / supplemental | Aggregate method through the annual table | Same, West Virginia share |
| Municipal service fee | By work location in a fee city | Same |
| Severance, equity, benefits in kind | Follow federal wages | West Virginia share |

## @social
- **Unemployment compensation (WorkForce WV) [US-WVS5-001, US-WVS5-002, US-WVS5-015].** Taxable wage base {{wv.sui.wage_base}} USD per employee per year since 2024-07-01 (SB 841); wages on which contributions were paid in another state count toward it: {{wv.sui.wage_base.other_state_credit}}. New employer {{wv.sui.new_employer.rate}} %; foreign construction-trade entities {{wv.ui.rate.foreign_construction}} % (statutory rate plus surtax); maximum rate {{wv.sui.employer.rate.max}} % through 2026-06-30. The 2026 solvency column is not confirmed on an agency page.
- **SB 1053 (from 2026-07-01) [US-WVS5-002]:** contribution rates reduced by {{wv.ui.rate.reduction.sb1053}} %; an annual employer-only automation and administration fee applies, whose base is ambiguous between the statute's literal text and the design (blocking open point below). No employee deduction.
- **UI wages include employee retirement deferrals and cafeteria-plan deductions:** {{wv.ui.wages.401k_section125_included}} [US-WVS5-016].
- **Employee contribution:** {{wv.sui.employee.rate}} % [US-WVP52-004]. **SDI, TDI, PFML:** none (exists: {{wv.sdi_pfml.exists}}) [US-WIR3-004].

## @payslip
- **Content (42 CSR 5 s.7.3) [US-WVS5-008]:** an itemised statement of earnings on the payday: {{wv.payslip.items}}; 21-5-9(4) requires itemised deductions [US-WVS5-009]. Paper, or electronic where the employee has direct, convenient access; no separate consent rule.
- **Retention:** at least {{wv.records.retention_years}} years [US-WVS5-008]. The pay-statement duty follows work performed in West Virginia (21-5-1(n)).

## @reporting
- **Withholding [US-WVS5-010, US-WVS5-014]:** remit by the 15th of the following month; IT-101Q due {{wv.report.it101q.due}}, even with nil activity; small and certain household employers file annually (IT-101A).
- **Year end [US-WVS5-010, US-WVS5-013]:** IT-103 reconciliation and W-2 copies due {{wv.report.it103.due}}; upload via MyTaxes after a Letter of Intent. The 2026 edition of the W-2 specification is not yet out (open point below).
- **E-file mandate:** employers filing for {{wv.report.efile_threshold.employees}} or more employees, or using a payroll service (statute text conflict: open point below).
- **UI quarterly wage report [US-WVUI-001]:** due {{wv.report.ui.quarterly_due}} via the UC Employer System; name, SSN, gross wages, SOC or job title, county and monthly counts.
- **New hire [US-WVS5-016]:** to the WV New Hire Reporting Center within {{wv.newhire.report_days}} days of hire, regardless of hours; rehires after the statutory gap.
- **Registration and agents:** business4wv.gov; WV-2848 (tax), WorkForce WV POA (UI) [US-WVS5-016, US-WVP51-006, US-WVP52-006].

## @leave
- **No private-sector paid sick leave statute found** in the instruments read (open point below); employers must post their vacation and sick-leave policies (21-5-9(3)) [US-WVS5-009].
- **Accrued fringe benefits** (vacation, sick leave, holidays) are wages for final pay when calculable and payable directly under the agreement ({{wv.leave.accrued.wages_for_final_pay}}) [US-WVS5-009]. No PFML.

## @termination
- **Final pay [US-WVS5-003]:** {{wv.final_pay.rule}}; by mail on request; liquidated damages for failure.
- **Accrued vacation:** payable if calculable and payable directly under policy or agreement [US-WVS5-003, US-WVS5-009].
- **Unreturned property:** a deduction for property worth more than {{wv.term.unreturned_property.deduction_threshold}} USD only with a signed itemised agreement, written demand, a return window and escrow on objection; not under CBAs [US-WVS5-003].
- **UI separation information:** returned to WorkForce WV on request within the statutory days [US-WVS5-016].

## @bik
- **Withholding base** follows federal wages, so federal exclusions carry over [US-WVS5-010].
- **UI base differs:** employee deferrals and cafeteria-plan deductions included; employer match and insurance excluded; required on-site meals and lodging included above a share of compensation [US-WVS5-016, US-WVS5-001].

## @deductions
- **Authorised deductions [US-WVS5-009, US-WVS5-008]:** required by law, or written authorisations for listed purposes; other deductions need a written wage assignment valid for a limited period, with {{wv.deduction.wage_assignment.exempt_net}} % of net wages exempt; public employees: no union-dues deduction except grandfathered municipal CBAs.
- **Creditor garnishment (suggestee execution, 38-5A-3) [US-WVS5-006]:** {{wv.garn.consumer.max_rate_net}} % of wages after taxes, only where weekly net pay exceeds fifty times the federal minimum wage ({{wv.garn.consumer.floor.weekly}} USD per week), never reducing pay below that floor; one execution at a time. Stricter than the CCPA. Child-support IWO specifics: open point below.

## @cba
- **No state prevailing-wage law** (exists: {{wv.prevailing_wage.exists}}): repealed in 2016 [US-WVP51-009]. Federal Davis-Bacon only.

## @indexation
- **Not indexed:** minimum wage; SUI wage base (moves only if the FUTA base exceeds it) [US-WVS5-001]; PIT brackets (changed by statute) [US-WVS5-012]; exemption [US-WVPIT-001]. The garnishment floor follows the federal minimum wage [US-WVS5-006]. The UI solvency column is set yearly by the fund level [US-WVS5-015].

## @data
- No West Virginia rule on SSN truncation on pay statements found; records may use an identifying number instead of the name [US-WVS5-008]. Not researched further (open point below).

## @live
- **SB 392 (signed 2026-03-31, codified 2026-06-12):** PIT rate cut retroactive to 2026-01-01; new IT-100.2A tables (start date open) [US-WVS5-012].
- **SB 1053 (effective 2026-07-01):** UI rate reduction and new fee (base ambiguous) [US-WVS5-002].
- **Died in committee:** HB 5485 (minimum wage), HB 4401 (UI wage base) [US-WVS5-017, US-WVS5-018]. Full 2026 enrolled-acts sweep not done (open point below).

## @special
| Population | West Virginia rule | Register id |
|---|---|---|
| Domestic / household | UI registration not required below a quarterly cash test per worker; annual withholding filing permitted; minimum wage only where the location test is met; family excluded | US-WVS5-016, US-WVS5-010, US-WVS5-005 |
| Agricultural | Excluded from the state minimum wage and overtime; non-cash agricultural pay not UI wages | US-WVS5-005, US-WVS5-001 |
| Minors | Child-labour law not read; records keep the date of birth of minors | US-WVS5-008, US-WVS5-007 |
| Tipped | Cash wage per Section 1; reported tips above a monthly test are UI wages | US-WVS5-007, US-WVS5-001 |
| Clergy / religious | No state rule beyond federal | US-WVS5-010 |
| Students | Part-time students excluded from the state minimum wage; enrolled student workers excluded from UI | US-WVS5-005, US-WVS5-016 |
| Nonresident aliens | Follows the federal wage definition | US-WVS5-010 |
| Statutory employees | No state rule beyond federal located | US-WVS5-010 |
| Government employees | Employers under the minimum-wage law; union-dues restriction; overpayment assignment allowed; UI reimbursable option | US-WVS5-005, US-WVS5-009, US-WVS5-008, US-WVS5-016 |
| Seniors on Social Security | Excluded from the state minimum-wage law above the statutory age | US-WVS5-005 |
| Military / military spouses | Nonresident Armed Forces members not withheld; MSRRA spouses via IT-104NR | US-WVS5-010, US-WVS5-011 |

## @gaps
- wv.pit.tables.start_date :: The WV Tax Division does not state from which pay date employers must apply the March 2026 IT-100.2A tables that implement the retroactive SB 392 rate cut. :: WV Tax Division employer notice on SB 392 withholding.
- wv.pit.local.service_fees :: Municipal service fees of cities other than Charleston rest on tier-B leads only; no fee amount is stated for them. :: Each city's ordinance or finance-office page (parallel lookups).
- wv.ui.sb1053_fee :: The SB 1053 automation and administration fee is written as a percentage of taxable wages in the statute but designed as a shift of contributions; its base and net effect are unclear, so no fee figure is modelled. :: WorkForce WV employer notice or March 2027 fee invoice instructions.
- wv.report.efile_threshold.statute :: The current text of W. Va. Code 11-21-74 (an archived copy shows different employee thresholds from the agency documents) was not read. :: Current 11-21-74 text (US exit) or amending session law.

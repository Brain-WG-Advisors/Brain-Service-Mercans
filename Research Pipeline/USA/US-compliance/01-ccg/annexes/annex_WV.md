# Annex WV: West Virginia


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T4 - local layer remitted to the locality on its own return** (build manifest, tier rationale). Municipal service fees withheld and remitted to the city, W. Va. Code 8-13-13 [US-WVR3-001], Charleston [US-WVR3-002].

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## WV.1 Employment and labour code

- **Minimum wage [US-WVS5-007, US-WVS5-005]:** [[FACT:wv.minwage.hourly=8.75]] USD per hour since 2016-01-01; no 2026 change and no 2027 rate (HB 5485 died in committee) [US-WVS5-017]. The state law applies where at least [[FACT:wv.labour.minwage.coverage_min_employees_at_location=6]] non-exempt employees work at one distinct permanent location (counted per location; home and client sites count where the work is done); otherwise the federal minimum applies (Annex FED). Exclusions in 21-5C-1(f).
- **Tipped employees [US-WVS5-007]:** cash wage [[FACT:wv.minwage.tipped.cash_wage=2.62]] USD per hour with written tip records; tip pools only among tip-eligible staff. Meal credit [[FACT:wv.labour.meal_credit.daily=4.00]] USD per day.
- **Overtime [US-WVS5-004, US-WVS5-005]:** [[FACT:wv.overtime.premium.multiplier=1.5]] times the regular rate over [[FACT:wv.overtime.weekly_threshold_hours=40]] hours per workweek; no daily overtime; state overtime does not apply where most of the workforce is FLSA-covered, so most employers apply the state minimum wage and federal overtime.
- **Local minimum wages:** none found (open point below).
- **Pay frequency (21-5-3; 42 CSR 5 s.7) [US-WVS5-009, US-WVS5-008]:** [[FACT:wv.pay_frequency.rule=at least twice a month, max 19 days between paydays; wages earned to 12th day before payday]]; a payday on a closed day moves to the preceding open day.
- **Method of payment [US-WVS5-009]:** [[FACT:wv.payment.method=cash, check, money order, direct deposit; payroll card if no account given (fee disclosure, one free withdrawal)]]; the employer must offer direct deposit.
- **Notices:** rate, payday and place at hire; written notice of changes one full pay period ahead [US-WVS5-008, US-WVS5-009].

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wv.minwage.hourly` | [[FACT:wv.minwage.hourly=8.75]] | USD | from 2016-01-01 | US-WVS5-007 | DOL FAQ (A.2); statute 21-5C-2 not verified; HB 5485 died 2026-02-13 (US-WVS5-017) |
| `wv.labour.minwage.coverage_min_employees_at_location` | [[FACT:wv.labour.minwage.coverage_min_employees_at_location=6]] |  | from 2015-01-01 | US-WVS5-005 |  |
| `wv.minwage.tipped.cash_wage` | [[FACT:wv.minwage.tipped.cash_wage=2.62]] | USD | from 2016-01-01 | US-WVS5-007 | 70% tip credit with written tip records |
| `wv.labour.meal_credit.daily` | [[FACT:wv.labour.meal_credit.daily=4.00]] | USD | from 2016-01-01 | US-WVS5-007 |  |
| `wv.overtime.weekly_threshold_hours` | [[FACT:wv.overtime.weekly_threshold_hours=40]] | hours | from 1980-07-01 | US-WVS5-004 | no daily OT; state OT not applicable where 80%+ of workforce FLSA-covered |
| `wv.overtime.premium.multiplier` | [[FACT:wv.overtime.premium.multiplier=1.5]] | ratio | from 1980-07-01 | US-WVS5-004 |  |
| `wv.pay_frequency.rule` | [[FACT:wv.pay_frequency.rule=at least twice a month, max 19 days between paydays; wages earned to 12th day before payday]] |  | from 2026-01-01 | US-WVS5-009 | monthly only by Commissioner-approved agreement |
| `wv.payment.method` | [[FACT:wv.payment.method=cash, check, money order, direct deposit; payroll card if no account given (fee disclosure, one free withdrawal)]] |  | from 2026-01-01 | US-WVS5-009 | 21-5-3 |

## WV.2 Income tax withholding

- **Method (IT-100.2A, March 2026) [US-WVP51-005]:** [[FACT:wv.wh.method=IT-100.2A (March 2026): gross - 2,000 per exemption; two-earner default table or optional one-earner table]]. Exemption [[FACT:wv.pit.exemption.annual=2000]] USD per year. Certificate: [[FACT:wv.wh.certificate=WV IT-104 (Rev. 03/2023); federal W-4 not used]] [US-WVS5-011]; the one-earner box on the IT-104 selects the optional table.
- **Two tables.**

| Table | Annual bracket thresholds (USD) | Rates (%) | Register id |
|---|---|---|---|
| Two earner / two or more jobs (default) | [[FACT:wv.pit.wh.two_earner.thresholds=7500;18750;30000;45000]] | same rate ladder as the statute | US-WVP51-005 |
| Optional one earner / one job (= statutory brackets) | [[FACT:wv.pit.statutory.thresholds=10000;25000;40000;60000]] | [[FACT:wv.pit.statutory.rates=2.11;2.81;3.16;4.22;4.58]] | US-WVS5-012 |

  Top statutory rate [[FACT:wv.pit.statutory.rate.top=4.58]] % (SB 392 of 2026: rate cut retroactive to 2026-01-01; married filing separately brackets are half) [US-WVS5-012]. The date from which employers must apply the March 2026 tables is not stated (blocking open point below).
- **Supplemental wages and rounding:** no flat rate; supplemental pay runs through the annual table by the aggregate method (partial source); no rounding rule found (open point below) [US-WVP52-007].
- **Wages subject to withholding** follow the federal definition, including bonuses, vacation allowances, back pay, tips and retroactive increases [US-WVS5-010].
- **Residents and nonresidents [US-WVPIT-001, US-WVS5-010, US-WVS5-011]:** residents and nonresidents are withheld, by resident and nonresident employers alike. Exceptions: reciprocity [[FACT:wv.reciprocity.states=KY;MD;OH;PA;VA (IT-104NR)]]; nonresidents whose West Virginia duties last [[FACT:wv.pit.nonresident.days_rule=30]] days or less across several states (not athletes, entertainers or public figures); nonresident Armed Forces members and MSRRA spouses. Allocation by time records or the employee's written statement. Nonresident credit only under a written interstate agreement [US-WVP51-002].
- **Local:** no local income tax (exists: [[FACT:wv.pit.local.income_tax.exists=False]]) [US-WVR3-001]. Municipal weekly **service fees** (W. Va. Code 8-13-13) are withheld from employees and remitted to the city (T4 layer): Charleston [[FACT:wv.pit.local.charleston.service_fee.weekly=3.00]] USD per week [US-WVR3-002]. Fees of other cities rest on secondary sources and are not stated (blocking open point below).
- **Resident and nonresident matrix.**

| Income type | West Virginia resident | Nonresident |
|---|---|---|
| Regular salary | IT-100.2A two-earner table (or one-earner table if elected) | Same tables on West Virginia wages, unless reciprocity (IT-104NR), the short-duty rule or a military exemption applies |
| Bonus / supplemental | Aggregate method through the annual table | Same, West Virginia share |
| Municipal service fee | By work location in a fee city | Same |
| Severance, equity, benefits in kind | Follow federal wages | West Virginia share |

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wv.pit.statutory.thresholds` | [[FACT:wv.pit.statutory.thresholds=10000;25000;40000;60000]] |  | from 2026-01-01 | US-WVS5-012 | = optional one-earner table; cumulative 211.00/632.50/1,106.50/1,950.50 |
| `wv.pit.statutory.rates` | [[FACT:wv.pit.statutory.rates=2.11;2.81;3.16;4.22;4.58]] |  | from 2026-01-01 | US-WVS5-012 | percent; SB 392 5% cut retroactive to 2026-01-01 |
| `wv.pit.statutory.rate.top` | [[FACT:wv.pit.statutory.rate.top=4.58]] | % | from 2026-01-01 | US-WVS5-012 |  |
| `wv.wh.certificate` | [[FACT:wv.wh.certificate=WV IT-104 (Rev. 03/2023); federal W-4 not used]] |  | from 2023-03-01 | US-WVS5-011 | IT-104NR nonresidence on p.2 |
| `wv.reciprocity.states` | [[FACT:wv.reciprocity.states=KY;MD;OH;PA;VA (IT-104NR)]] |  | from 2025-01-01 | US-WVS5-010 |  |
| `wv.pit.nonresident.days_rule` | [[FACT:wv.pit.nonresident.days_rule=30]] | days | from 2025-01-01 | US-WVS5-010 | duties 30 days or less in more than one state; not athletes/entertainers |
| `wv.pit.local.income_tax.exists` | [[FACT:wv.pit.local.income_tax.exists=False]] |  | from 2025-04-23 | US-WVR3-001 | municipal weekly service fees withheld instead |
| `wv.pit.local.charleston.service_fee.weekly` | [[FACT:wv.pit.local.charleston.service_fee.weekly=3.00]] | USD | from 2018-01-15 | US-WVR3-002 | city document dated 12/2022 |
| `wv.wh.method` | [[FACT:wv.wh.method=IT-100.2A (March 2026): gross - 2,000 per exemption; two-earner default table or optional one-earner table]] |  | from 2026-01-01 | US-WVP51-005 |  |
| `wv.pit.exemption.annual` | [[FACT:wv.pit.exemption.annual=2000]] | USD | from 2026-06-12 | US-WVP51-005 | weekly 38.46; biweekly 76.92; semimonthly 83.33; monthly 166.67 |
| `wv.pit.wh.two_earner.thresholds` | [[FACT:wv.pit.wh.two_earner.thresholds=7500;18750;30000;45000]] |  | from 2026-01-01 | US-WVP51-005 | default table; cumulative 158.25/474.38/829.88/1,462.88 |
| `wv.pit.rate_cut.sb392` | [[FACT:wv.pit.rate_cut.sb392=SB 392 signed 2026-03-31; W. Va. Code 11-21-4j effective 2026-06-12 with a 5% rate cut retroactive to 2026-01-01; the Tax Division updated the 2026 withholding tables (IT-100.2A/B dated March 2026).]] |  | from 2026-01-01 | US-WVB5-301 | Neither the Tax Division page nor IT-100.2A states the date employers must switch to the March 2026 tables, nor whether Jan-May over-withholding must be refunded or caught up (see unresolved wv.pit.tables.start_date). |

**Open research points**

- Not configured in this release [[GAP:RQ-388]]: The WV Tax Division does not state from which pay date employers must apply the March 2026 IT-100.2A tables that implement the retroactive SB 392 rate cut.
- Not configured in this release [[GAP:RQ-389]]: Not established from an official source.
- Not configured in this release [[GAP:RQ-390]]: Municipal service fees of cities other than Charleston rest on secondary sources only; no fee amount is stated for them.

## WV.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in WV.2.

## WV.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in WV.2.

## WV.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Unemployment compensation (WorkForce WV) [US-WVS5-001, US-WVS5-002, US-WVS5-015].** Taxable wage base [[FACT:wv.sui.wage_base=9500]] USD per employee per year since 2024-07-01 (SB 841); wages on which contributions were paid in another state count toward it: [[FACT:wv.sui.wage_base.other_state_credit=True]]. New employer [[FACT:wv.sui.new_employer.rate=2.7]] %; foreign construction-trade entities [[FACT:wv.ui.rate.foreign_construction=8.5]] % (statutory rate plus surtax); maximum rate [[FACT:wv.sui.employer.rate.max=8.5]] % through 2026-06-30. The 2026 solvency column is not confirmed on an agency page.
- **SB 1053 (from 2026-07-01) [US-WVS5-002]:** contribution rates reduced by [[FACT:wv.ui.rate.reduction.sb1053=7]] %; an annual employer-only automation and administration fee applies, whose base is ambiguous between the statute's literal text and the design (blocking open point below). No employee deduction.
- **UI wages include employee retirement deferrals and cafeteria-plan deductions:** [[FACT:wv.ui.wages.401k_section125_included=True]] [US-WVS5-016].
- **Employee contribution:** [[FACT:wv.sui.employee.rate=0]] % [US-WVP52-004]. **SDI, TDI, PFML:** none (exists: [[FACT:wv.sdi_pfml.exists=False]]) [US-WIR3-004].

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wv.sui.wage_base` | [[FACT:wv.sui.wage_base=9500]] | USD | from 2024-07-01 | US-WVS5-001 | SB 841 fixed; HB 4401 died (US-WVS5-018) |
| `wv.ui.rate.foreign_construction` | [[FACT:wv.ui.rate.foreign_construction=8.5]] | % | from 1981-07-01 | US-WVP52-004 |  |
| `wv.sui.employer.rate.max` | [[FACT:wv.sui.employer.rate.max=8.5]] | % | 1981-07-01 to 2026-06-30 | US-WVS5-015 | Debit-balance rates 5.5/6.5/7.5 + 1% surtax (21A-5-10); the fund-solvency column applied for 2026 is not published on the agency pages. |
| `wv.ui.rate.reduction.sb1053` | [[FACT:wv.ui.rate.reduction.sb1053=7]] | % | 2026-07-01 to 2031-07-01 | US-WVS5-002 | contribution rate reduced by 7% from 2026-07-01 |
| `wv.sui.wage_base.other_state_credit` | [[FACT:wv.sui.wage_base.other_state_credit=True]] |  | from 2024-07-01 | US-WVS5-001 |  |
| `wv.ui.wages.401k_section125_included` | [[FACT:wv.ui.wages.401k_section125_included=True]] |  | from 2024-06-01 | US-WVS5-016 | employer match and insurance excluded |
| `wv.sdi_pfml.exists` | [[FACT:wv.sdi_pfml.exists=False]] |  | from 2024-03-01 | US-WIR3-004 | DOL PFML list (row filed under WI id) - WV absent |
| `wv.sui.employee.rate` | [[FACT:wv.sui.employee.rate=0]] | % | from 2024-01-01 | US-WVR3C-001 | W. Va. Code 21A-5-14: an employer shall not deduct UI payments, in whole or in part, from the wages of an employee. |
| `wv.sui.new_employer.rate` | [[FACT:wv.sui.new_employer.rate=2.7]] | % | 2026-01-01 to 2031-07-01 | US-WVP52-004 | 36 months |

**Open research points**

- Not configured in this release [[GAP:RQ-391]]: The SB 1053 automation and administration fee is written as a percentage of taxable wages in the statute but designed as a shift of contributions; its base and net effect are unclear, so no fee figure is modelled.

## WV.4 Pay statement

- **Content (42 CSR 5 s.7.3) [US-WVS5-008]:** an itemised statement of earnings on the payday: [[FACT:wv.payslip.items=hourly rate or salary, hours paid, overtime rate, bonus/incentive, itemized deductions]]; 21-5-9(4) requires itemised deductions [US-WVS5-009]. Paper, or electronic where the employee has direct, convenient access; no separate consent rule.
- **Retention:** at least [[FACT:wv.records.retention_years=5]] years [US-WVS5-008]. The pay-statement duty follows work performed in West Virginia (21-5-1(n)).

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wv.payslip.items` | [[FACT:wv.payslip.items=hourly rate or salary, hours paid, overtime rate, bonus/incentive, itemized deductions]] |  | 2019-07-01 to 2029-07-01 | US-WVS5-008 | 42 CSR 5 s.7.3; electronic if direct access. |
| `wv.records.retention_years` | [[FACT:wv.records.retention_years=5]] | years | 2019-07-01 to 2029-07-01 | US-WVS5-008 | available within 72 business hours |

## WV.5 Statutory reporting

- **Withholding [US-WVS5-010, US-WVS5-014]:** remit by the 15th of the following month; IT-101Q due [[FACT:wv.report.it101q.due=last day of month after quarter (remit by 15th of following month)]], even with nil activity; small and certain household employers file annually (IT-101A).
- **Year end [US-WVS5-010, US-WVS5-013]:** IT-103 reconciliation and W-2 copies due [[FACT:wv.report.it103.due=January 31 with W-2 EFW2 (RS state code 54 + WV RV record)]]; upload via MyTaxes after a Letter of Intent. The 2026 edition of the W-2 specification is not yet out (open point below).
- **E-file mandate:** employers filing for [[FACT:wv.report.efile_threshold.employees=10]] or more employees, or using a payroll service (statute text conflict: open point below).
- **UI quarterly wage report [US-WVUI-001]:** due [[FACT:wv.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] via the UC Employer System; name, SSN, gross wages, SOC or job title, county and monthly counts.
- **New hire [US-WVS5-016]:** to the WV New Hire Reporting Center within [[FACT:wv.newhire.report_days=14]] days of hire, regardless of hours; rehires after the statutory gap.
- **Registration and agents:** business4wv.gov; WV-2848 (tax), WorkForce WV POA (UI) [US-WVS5-016, US-WVP51-006, US-WVP52-006].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wv.report.it101q.due` | [[FACT:wv.report.it101q.due=last day of month after quarter (remit by 15th of following month)]] |  | from 2025-01-01 | US-WVS5-010 | annual IT-101A if <600/yr |
| `wv.report.it103.due` | [[FACT:wv.report.it103.due=January 31 with W-2 EFW2 (RS state code 54 + WV RV record)]] |  | from 2025-01-01 | US-WVS5-013 | MyTaxes after Letter of Intent |
| `wv.report.efile_threshold.employees` | [[FACT:wv.report.efile_threshold.employees=10]] |  | from 2025-01-01 | US-WVS5-010 | Or payroll service; an older archived page says 25/50 (may be out of date). |
| `wv.newhire.report_days` | [[FACT:wv.newhire.report_days=14]] | days | from 2024-06-01 | US-WVS5-016 | regardless of hours |
| `wv.report.ui.quarterly_due` | [[FACT:wv.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] |  | from 2026-01-01 | US-WVUI-001 | SOC/job title, county, monthly counts |

**Open research points**

- Not configured in this release [[GAP:RQ-393]]: IT-105 2026 W-2 spec not listed.
- Not configured in this release [[GAP:RQ-394]]: The current text of W. Va. Code 11-21-74 (an archived copy shows different employee thresholds from the agency documents) was not verified against the official source.

## WV.6 Leave

- **No private-sector paid sick leave statute found** in the instruments read (open point below); employers must post their vacation and sick-leave policies (21-5-9(3)) [US-WVS5-009].
- **Accrued fringe benefits** (vacation, sick leave, holidays) are wages for final pay when calculable and payable directly under the agreement ([[FACT:wv.leave.accrued.wages_for_final_pay=True]]) [US-WVS5-009]. No PFML.

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wv.leave.accrued.wages_for_final_pay` | [[FACT:wv.leave.accrued.wages_for_final_pay=True]] |  | from 2026-01-01 | US-WVS5-009 | accrued vacation/sick/holiday are wages per agreement; no paid-sick statute found |

**Open research points**

- Not configured in this release [[GAP:RQ-392]]: Absence of private paid sick leave and local minimum wages rests on instruments read.

## WV.7 Termination and final pay

- **Final pay [US-WVS5-003]:** [[FACT:wv.final_pay.rule=next regular payday (discharge and resignation)]]; by mail on request; liquidated damages for failure.
- **Accrued vacation:** payable if calculable and payable directly under policy or agreement [US-WVS5-003, US-WVS5-009].
- **Unreturned property:** a deduction for property worth more than [[FACT:wv.term.unreturned_property.deduction_threshold=100]] USD only with a signed itemised agreement, written demand, a return window and escrow on objection; not under CBAs [US-WVS5-003].
- **UI separation information:** returned to WorkForce WV on request within the statutory days [US-WVS5-016].

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wv.final_pay.rule` | [[FACT:wv.final_pay.rule=next regular payday (discharge and resignation)]] |  | from 2026-01-01 | US-WVS5-003 | liquidated damages 2x |
| `wv.term.unreturned_property.deduction_threshold` | [[FACT:wv.term.unreturned_property.deduction_threshold=100]] | USD | from 2026-01-01 | US-WVS5-003 | signed agreement, written demand, 10 business days |

## WV.8 Benefits in kind and taxable wages

- **Withholding base** follows federal wages, so federal exclusions carry over [US-WVS5-010].
- **UI base differs:** employee deferrals and cafeteria-plan deductions included; employer match and insurance excluded; required on-site meals and lodging included above a share of compensation [US-WVS5-016, US-WVS5-001].

## WV.9 Deductions and garnishments

- **Authorised deductions [US-WVS5-009, US-WVS5-008]:** required by law, or written authorisations for listed purposes; other deductions need a written wage assignment valid for a limited period, with [[FACT:wv.deduction.wage_assignment.exempt_net=75]] % of net wages exempt; public employees: no union-dues deduction except grandfathered municipal CBAs.
- **Creditor garnishment (suggestee execution, 38-5A-3) [US-WVS5-006]:** [[FACT:wv.garn.consumer.max_rate_net=20]] % of wages after taxes, only where weekly net pay exceeds fifty times the federal minimum wage ([[FACT:wv.garn.consumer.floor.weekly=362.50]] USD per week), never reducing pay below that floor; one execution at a time. Stricter than the CCPA. Child-support IWO specifics: open point below.

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wv.garn.consumer.max_rate_net` | [[FACT:wv.garn.consumer.max_rate_net=20]] | % | from 2026-01-01 | US-WVS5-006 | of wages after taxes; only if weekly net > 50x FMW |
| `wv.garn.consumer.floor.weekly` | [[FACT:wv.garn.consumer.floor.weekly=362.50]] | USD | from 2026-01-01 | US-WVS5-006 |  |
| `wv.deduction.wage_assignment.exempt_net` | [[FACT:wv.deduction.wage_assignment.exempt_net=75]] | % | from 2026-01-01 | US-WVS5-008 | max 1 year |

**Open research points**

- Not configured in this release [[GAP:RQ-395]]: Child-support IWO fee, priority and 48-14 limits not verified against the official source.

## WV.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

- **No state prevailing-wage law** (exists: [[FACT:wv.prevailing_wage.exists=False]]): repealed in 2016 [US-WVP51-009]. Federal Davis-Bacon only.

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wv.prevailing_wage.exists` | [[FACT:wv.prevailing_wage.exists=False]] |  | from 2016-01-01 | US-WVP51-009 | 21-5A repealed 2016 |

## WV.11 Indexation

- **Not indexed:** minimum wage; SUI wage base (moves only if the FUTA base exceeds it) [US-WVS5-001]; PIT brackets (changed by statute) [US-WVS5-012]; exemption [US-WVPIT-001]. The garnishment floor follows the federal minimum wage [US-WVS5-006]. The UI solvency column is set yearly by the fund level [US-WVS5-015].

## WV.12 Payroll data protection and records

- No West Virginia rule on SSN truncation on pay statements found; records may use an identifying number instead of the name [US-WVS5-008].

**Open research points**

- Not configured in this release [[GAP:RQ-396]]: SSN truncation and payroll-record privacy rules not established from an official source.

## WV.13 Live legal change

- **SB 392 (signed 2026-03-31, codified 2026-06-12):** PIT rate cut retroactive to 2026-01-01; new IT-100.2A tables (start date open) [US-WVS5-012].
- **SB 1053 (effective 2026-07-01):** UI rate reduction and new fee (base ambiguous) [US-WVS5-002].
- **Died in committee:** HB 5485 (minimum wage), HB 4401 (UI wage base) [US-WVS5-017, US-WVS5-018]. Full 2026 enrolled-acts sweep not done (open point below).

**Open research points**

- Not configured in this release [[GAP:RQ-397]]: Full 2026 enrolled-acts sweep not done.

## WV.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## WV.15 Special populations

| Population | West Virginia rule | Register id |
|---|---|---|
| Domestic / household | UI registration not required below a quarterly cash test per worker; annual withholding filing permitted; minimum wage only where the location test is met; family excluded | US-WVS5-016, US-WVS5-010, US-WVS5-005 |
| Agricultural | Excluded from the state minimum wage and overtime; non-cash agricultural pay not UI wages | US-WVS5-005, US-WVS5-001 |
| Minors | Child-labour law not verified against the official source; records keep the date of birth of minors | US-WVS5-008, US-WVS5-007 |
| Tipped | Cash wage per Section 1; reported tips above a monthly test are UI wages | US-WVS5-007, US-WVS5-001 |
| Clergy / religious | No state rule beyond federal | US-WVS5-010 |
| Students | Part-time students excluded from the state minimum wage; enrolled student workers excluded from UI | US-WVS5-005, US-WVS5-016 |
| Nonresident aliens | Follows the federal wage definition | US-WVS5-010 |
| Statutory employees | No state rule beyond federal located | US-WVS5-010 |
| Government employees | Employers under the minimum-wage law; union-dues restriction; overpayment assignment allowed; UI reimbursable option | US-WVS5-005, US-WVS5-009, US-WVS5-008, US-WVS5-016 |
| Seniors on Social Security | Excluded from the state minimum-wage law above the statutory age | US-WVS5-005 |
| Military / military spouses | Nonresident Armed Forces members not withheld; MSRRA spouses via IT-104NR | US-WVS5-010, US-WVS5-011 |

## WV.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## WV.S Sources

Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file. Authorities:

- Build lead (Claude) under owner delegation (Wallisson Gomes): US-OWN-006
- City of Charleston, Office of the City Collector: US-WVR3-002
- Owner (Wallisson Gomes): US-OWN-008
- US DOL Women's Bureau: US-WIR3-004
- West Virginia Division of Labor: US-WVS5-008
- West Virginia Division of Labor (publishing the W. Va. Code text): US-WVS5-009
- West Virginia Division of Labor, Wage & Hour Section: US-WVS5-007
- West Virginia Legislature: US-WVP51-002, US-WVP51-009, US-WVPIT-001, US-WVR3-001, US-WVR3C-001, US-WVS5-001, US-WVS5-002, US-WVS5-017, US-WVS5-018
- West Virginia Legislature (code.wvlegislature.gov: US-WVS5-003, US-WVS5-004, US-WVS5-005, US-WVS5-006, US-WVS5-015
- West Virginia State Tax Department: US-WVP51-005, US-WVP51-006, US-WVP52-007
- West Virginia Tax Division: US-WVB5-301, US-WVS5-010, US-WVS5-011, US-WVS5-012, US-WVS5-013, US-WVS5-014
- WorkForce West Virginia: US-WVP52-004, US-WVS5-016, US-WVUI-001
- WorkForce West Virginia Unemployment Compensation Division: US-WVP52-006

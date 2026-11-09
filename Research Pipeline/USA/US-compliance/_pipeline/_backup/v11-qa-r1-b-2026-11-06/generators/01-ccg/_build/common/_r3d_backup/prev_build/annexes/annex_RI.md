# Annex RI: Rhode Island


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T3 - state withholding; local layer absent or piggybacked on the state return** (build manifest, tier rationale).

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## RI.1 Employment and labour code

- **Minimum wage (RIGL 28-12-3) [US-RIS5-001].** Fixed statutory steps, not indexed:

| From | Rate |
|---|---|
| 2026-01-01 | [[FACT:ri.minwage.hourly=16.00]] USD |
| 2027-01-01 (enacted, P.L. 2025 ch. 222/223) | [[FACT:ri.minwage.hourly=17.00]] USD |

- **Local minimum wages:** none located (municipalities cannot levy income-based taxes and no municipal wage ordinance was found; this rests on absence of a find) [US-RIP52-001].
- **Minors and students [US-RIS5-002]:** minors aged 14-15 at least [[FACT:ri.labour.minwage.minor_14_15.ratio=75]] % of the minimum (full minimum in weeks above the statutory hours) (28-12-3.1); full-time students working for nonprofit religious, educational, library or community-service employers at least [[FACT:ri.labour.minwage.student_nonprofit.ratio=90]] % (28-12-5(f)).
- **Tipped employees [US-RIS5-002]:** cash wage at least [[FACT:ri.minwage.tipped.cash_wage=3.89]] USD per hour (not taxicabs); the tip credit is the minimum wage minus the cash wage.
- **Overtime (28-12-4.1 ff.) [US-RIS5-003]:** [[FACT:ri.overtime.premium.multiplier=1.5]] times the regular rate above [[FACT:ri.overtime.weekly_threshold_hours=40]] hours a week; no daily overtime; fluctuating workweek barred for delivery drivers and sales merchandisers; retail Sunday and holiday premium hours (5-23-2) excluded from the weekly count; exemptions in 28-12-4.3.
- **Pay frequency (28-14-2.2) [US-RIS5-004]:** [[FACT:ri.pay_frequency.rule=weekly (unless fixed at biweekly/semi-monthly/monthly/yearly rate); payday within 9 days of period end]]; DLT may approve less-than-weekly pay on petition with a surety bond; payday changes need advance notice.
- **Method of payment [US-RIS5-005]:** [[FACT:ri.payment.method=direct deposit or payroll card only at employee written/electronic request; one free full withdrawal per period]]; free balance inquiry.
- **Deduction remittance [US-RIS5-007]:** payroll deductions paid over within [[FACT:ri.deduction.remittance_days=21]] days after the end of the month in which they were taken.

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ri.minwage.hourly` | [[FACT:ri.minwage.hourly=16.00]] | USD | 2026-01-01 to 2026-12-31 | US-RIS5-001 | fixed statutory step; not indexed |
| `ri.minwage.hourly` | [[FACT:ri.minwage.hourly=17.00]] | USD | from 2027-01-01 | US-RIS5-001 | enacted P.L. 2025 ch. 222/223 |
| `ri.labour.minwage.minor_14_15.ratio` | [[FACT:ri.labour.minwage.minor_14_15.ratio=75]] | % | from 2017-01-01 | US-RIS5-002 | full minimum in weeks over 24 hours |
| `ri.labour.minwage.student_nonprofit.ratio` | [[FACT:ri.labour.minwage.student_nonprofit.ratio=90]] | % | from 2017-01-01 | US-RIS5-002 | full-time students under 19 at nonprofits |
| `ri.minwage.tipped.cash_wage` | [[FACT:ri.minwage.tipped.cash_wage=3.89]] | USD | from 2017-01-01 | US-RIS5-002 | max tip credit 12.11 (2026) / 13.11 (2027) derived; not taxicabs |
| `ri.overtime.weekly_threshold_hours` | [[FACT:ri.overtime.weekly_threshold_hours=40]] | hours | from 2019-01-01 | US-RIS5-003 | no daily OT |
| `ri.overtime.premium.multiplier` | [[FACT:ri.overtime.premium.multiplier=1.5]] | ratio | from 2019-01-01 | US-RIS5-003 |  |
| `ri.pay_frequency.rule` | [[FACT:ri.pay_frequency.rule=weekly (unless fixed at biweekly/semi-monthly/monthly/yearly rate); payday within 9 days of period end]] |  | from 2013-01-01 | US-RIS5-004 | 28-14-2.2; DLT may approve less frequent |
| `ri.payment.method` | [[FACT:ri.payment.method=direct deposit or payroll card only at employee written/electronic request; one free full withdrawal per period]] |  | from 2015-01-01 | US-RIS5-005 |  |

## RI.2 Income tax withholding

- **Method (2026 booklet) [US-RIS5-019]:** [[FACT:ri.wh.method=percentage method or wage-bracket tables, same for all filing statuses]].

| Annual taxable wages | Withholding |
|---|---|
| up to [[FACT:ri.pit.bracket.1.ceiling=82,050]] USD | [[FACT:ri.pit.bracket.1.rate=3.75]] % |
| above that, up to [[FACT:ri.pit.bracket.2.ceiling=186,450]] USD | [[FACT:ri.pit.bracket.2.base_tax=3,076.88]] USD + [[FACT:ri.pit.bracket.2.rate=4.75]] % of the excess over the first ceiling |
| above the second ceiling | [[FACT:ri.pit.bracket.3.base_tax=8,035.88]] USD + [[FACT:ri.pit.bracket.3.rate=5.99]] % of the excess over the second ceiling |

  Per-period tables are the annual table divided by the number of periods (published in the booklet).
- **Exemption allowance:** [[FACT:ri.pit.exemption.annual=1000]] USD per year per exemption, falling to zero when annualised wages exceed [[FACT:ri.pit.exemption.cliff.annual_wages=290,800]] USD (a cliff, not a phase-out) [US-RIS5-019].
- **Oracle:** booklet worked example (weekly, one exemption): [[FACT:ri.oracle.weekly_2195.withholding=87.57]] USD, reproduced exactly. Recomputation in Module 12.
- **Certificate:** [[FACT:ri.wh.certificate=RI W-4 (2026) mandatory in addition to federal W-4; max 10 allowances; EXEMPT renewed yearly]] [US-RIS5-019].
- **Supplemental wages:** flat [[FACT:ri.wh.supplemental.rate=5.99]] % (booklet instruction 12) or the aggregate method; [US-RIS5-019].
- **Rounding:** no rule stated; the tables work to the cent.
- **Who withholds [US-RIP52-003, US-RIS5-019]:** wages subject to federal withholding where any part is for services in Rhode Island; nonresidents working in Rhode Island; out-of-state employers may withhold for residents as a convenience. Reciprocity: [[FACT:ri.reciprocity.states=none]]; no day or dollar threshold; no convenience-of-employer rule found. Residents claim a credit for tax paid to another state on Schedule II [US-RIP52-002].
- **Local income taxes:** none (exists: [[FACT:ri.local_wage_tax.exists=False]]) [US-RIP52-001].
- **Conformity:** RI starts from federal AGI with Schedule M modifications and decoupled from federal H.R. 1 in the FY2026 budget; the 2026 withholding method is unchanged by that decoupling [US-RIS5-023].
- **Resident and nonresident matrix.**

| Income type | Rhode Island resident | Nonresident |
|---|---|---|
| Regular salary | Booklet tables, all wages subject to federal withholding | Booklet tables on wages for services in Rhode Island |
| Bonus / supplemental | Flat [[FACT:ri.wh.supplemental.rate=5.99]] % or aggregate | Same, Rhode Island share |
| Severance, equity, benefits in kind | Follow federal wages (RI withholds where federal withholding applies) | Same, Rhode Island share |
| Military spouse | EXEMPT-MS on the RI W-4 (renewed yearly) | Same |

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ri.wh.method` | [[FACT:ri.wh.method=percentage method or wage-bracket tables, same for all filing statuses]] |  | 2026-01-01 to 2026-12-31 | US-RIS5-019 | 2026 booklet |
| `ri.pit.bracket.1.ceiling` | [[FACT:ri.pit.bracket.1.ceiling=82,050]] | USD | 2026-01-01 to 2026-12-31 | US-RIS5-019 | annual; [[FACT:ri.pit.bracket.1.rate=3.75]]% |
| `ri.pit.bracket.1.rate` | [[FACT:ri.pit.bracket.1.rate=3.75]] | % | 2026-01-01 to 2026-12-31 | US-RIS5-019 |  |
| `ri.pit.bracket.2.ceiling` | [[FACT:ri.pit.bracket.2.ceiling=186,450]] | USD | 2026-01-01 to 2026-12-31 | US-RIS5-019 |  |
| `ri.pit.bracket.2.rate` | [[FACT:ri.pit.bracket.2.rate=4.75]] | % | 2026-01-01 to 2026-12-31 | US-RIS5-019 |  |
| `ri.pit.bracket.2.base_tax` | [[FACT:ri.pit.bracket.2.base_tax=3,076.88]] | USD | 2026-01-01 to 2026-12-31 | US-RIS5-019 |  |
| `ri.pit.bracket.3.rate` | [[FACT:ri.pit.bracket.3.rate=5.99]] | % | 2026-01-01 to 2026-12-31 | US-RIS5-019 |  |
| `ri.pit.bracket.3.base_tax` | [[FACT:ri.pit.bracket.3.base_tax=8,035.88]] | USD | 2026-01-01 to 2026-12-31 | US-RIS5-019 |  |
| `ri.pit.exemption.annual` | [[FACT:ri.pit.exemption.annual=1000]] | USD | 2026-01-01 to 2026-12-31 | US-RIS5-019 | weekly 19.23 etc. |
| `ri.pit.exemption.cliff.annual_wages` | [[FACT:ri.pit.exemption.cliff.annual_wages=290,800]] | USD | 2026-01-01 to 2026-12-31 | US-RIS5-019 | exemption zero above (cliff, not phase-out); weekly 5,592.31 |
| `ri.wh.certificate` | [[FACT:ri.wh.certificate=RI W-4 (2026) mandatory in addition to federal W-4; max 10 allowances; EXEMPT renewed yearly]] |  | 2020-01-01 to 2026-12-31 | US-RIS5-019 |  |
| `ri.wh.supplemental.rate` | [[FACT:ri.wh.supplemental.rate=5.99]] | % | 2026-01-01 to 2026-12-31 | US-RIS5-019 | Or aggregate method. |
| `ri.reciprocity.states` | [[FACT:ri.reciprocity.states=none]] |  | from 2026-01-01 | US-RIP52-003 | no day/dollar threshold |
| `ri.local_wage_tax.exists` | [[FACT:ri.local_wage_tax.exists=False]] |  | from 2026-01-01 | US-RIP52-001 | municipalities barred |

**Open research points**

- Not configured in this release [[GAP:RQ-310]]: Not established from an official source.

## RI.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in RI.2.

## RI.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in RI.2.

## RI.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Unemployment insurance (DLT Employer Tax Unit) [US-RIP9V-001, US-RIB5-401].** 2026 taxable wage base [[FACT:ri.sui.wage_base=30,800]] USD; employers at the highest rate pay on [[FACT:ri.ui.wage_base.highest_rate=32,300]] USD. Experience range [[FACT:ri.sui.employer.rate.min=0.9]] % to [[FACT:ri.sui.employer.rate.max=9.4]] %, each reduced to offset the employer Job Development Assessment of [[FACT:ri.ui.jda.rate=0.21]] %. New employer [[FACT:ri.sui.new_employer.rate=1.21]] % (JDA included). Employee UI contribution [[FACT:ri.sui.employee.rate=0]] %.
- **Wage-base indexation (28-43) [US-RIS5-014]:** a share of the prior-year average annual wage, rounded up; the highest-rate base adds a fixed statutory amount.
- **Other-state wages count toward the base:** [[FACT:ri.sui.wage_base.other_state_credit=True]] [US-RIS5-013].
- **TDI / TCI (employee-only) [US-RIP9V-001, US-RIS5-015]:** 2026 rate [[FACT:ri.tdi.employee.rate=1.1]] % on wages up to [[FACT:ri.tdi.wage_base.annual=100,000]] USD, so the annual maximum is [[FACT:ri.tdi.employee.max_annual=1,100.00]] USD. Coverage test: [[FACT:ri.tdi.coverage_test=follows UI localization]] [US-RIS5-016]. TDI not deducted on time is recoverable from later pay: [[FACT:ri.tdi.late_deduction.recoverable=False]]; the employer becomes liable (28-40-4) [US-RIS5-017].
- **UI and TDI wages exclude employee 401(k) and cafeteria-plan contributions:** [[FACT:ri.ui_tdi.wages.401k_section125_excluded=True]] [US-RIS5-017]. This departs from FUTA (Annex FED).
- **No separate PFML programme** beyond TCI; no other levy beyond JDA and TDI [US-RIP9V-002, US-OWN-007].

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ri.sui.wage_base` | [[FACT:ri.sui.wage_base=30,800]] | USD | 2026-01-01 to 2026-12-31 | US-RIP9V-001 | 46.5% of avg annual wage rounded up to 200 |
| `ri.ui.wage_base.highest_rate` | [[FACT:ri.ui.wage_base.highest_rate=32,300]] | USD | 2026-01-01 to 2026-12-31 | US-RIP9V-001 |  |
| `ri.sui.employer.rate.min` | [[FACT:ri.sui.employer.rate.min=0.9]] | % | 2026-01-01 to 2026-12-31 | US-RIP9V-001 | Schedule F 0.9-9.4, each reduced 0.21 for JDA |
| `ri.sui.employer.rate.max` | [[FACT:ri.sui.employer.rate.max=9.4]] | % | 2026-01-01 to 2026-12-31 | US-RIP9V-001 |  |
| `ri.sui.new_employer.rate` | [[FACT:ri.sui.new_employer.rate=1.21]] | % | 2026-01-01 to 2026-12-31 | US-RIP9V-001 | JDA included |
| `ri.ui.jda.rate` | [[FACT:ri.ui.jda.rate=0.21]] | % | 2026-01-01 to 2026-12-31 | US-RIB5-401 | Job Development Assessment |
| `ri.sui.employee.rate` | [[FACT:ri.sui.employee.rate=0]] | % | from 2026-01-01 | US-RIP9V-001 |  |
| `ri.sui.wage_base.other_state_credit` | [[FACT:ri.sui.wage_base.other_state_credit=True]] |  | from 2026-01-01 | US-RIS5-013 |  |
| `ri.tdi.employee.rate` | [[FACT:ri.tdi.employee.rate=1.1]] | % | 2026-01-01 to 2026-12-31 | US-RIP9V-001 | employee-only;  |
| `ri.tdi.wage_base.annual` | [[FACT:ri.tdi.wage_base.annual=100,000]] | USD | 2026-01-01 to 2026-12-31 | US-RIP9V-001 |  |
| `ri.tdi.employee.max_annual` | [[FACT:ri.tdi.employee.max_annual=1,100.00]] | USD | 2026-01-01 to 2026-12-31 | US-RIP9V-001 |  |
| `ri.tdi.coverage_test` | [[FACT:ri.tdi.coverage_test=follows UI localization]] |  | from 2026-01-01 | US-RIS5-016 |  |
| `ri.tdi.late_deduction.recoverable` | [[FACT:ri.tdi.late_deduction.recoverable=False]] |  | from 2022-04-11 | US-RIS5-017 | employer liable if not deducted on time (28-40-4) |
| `ri.ui_tdi.wages.401k_section125_excluded` | [[FACT:ri.ui_tdi.wages.401k_section125_excluded=True]] |  | from 2022-04-11 | US-RIS5-017 | departs from FUTA |

**Open research points**

- Not configured in this release [[GAP:RQ-314]]: 2027 booklet and DLT 2027 UI/TDI release not published.

## RI.4 Pay statement

- **Content (28-14-2.1) [US-RIP51-002]:** [[FACT:ri.payslip.items=hours worked (non-exempt), every deduction with explanation; regular hourly rate in commercial construction]]. Electronic statement allowed; free printed copy on written request; no language clause [US-RIL-001].
- **Records:** the record-keeping section was replaced from 2026-01-01; the new text and retention period are unconfirmed (blocking open point below) [US-RIS5-008].
- **Reach:** no territorial clause; default applies to employees working in Rhode Island.

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ri.payslip.items` | [[FACT:ri.payslip.items=hours worked (non-exempt), every deduction with explanation; regular hourly rate in commercial construction]] |  | from 2026-01-01 | US-RIP51-002 | 28-14-2.1; electronic allowed, printed copy on written request |

**Open research points**

- Not yet published [[GAP:RQ-308]]: The new record-keeping and hiring-notice section 28-14-12 (effective 2026-01-01) was not read; the 2026 retention period and notice fields are unconfirmed.

## RI.5 Statutory reporting

- **Two institutions, two portals [US-RIS5-024]:** the Division of Taxation (withholding) and DLT (UI, TDI, JDA). Do not mix them.
- **Division of Taxation [US-RIS5-018, US-RIS5-019]:** weekly electronic deposits once withholding reaches [[FACT:ri.report.wh.weekly_threshold.monthly=600]] USD a month (smaller employers deposit monthly or quarterly); RI-941 quarterly return due [[FACT:ri.report.ri941.due=last day of month after quarter]]; RI W-3 annual reconciliation due [[FACT:ri.report.w3.due=31 January]]; W-2 to Rhode Island in EFW2 through the Tax Portal, mandatory electronic for employers that e-file with SSA and have [[FACT:ri.report.w2.efile_threshold=25]] or more RI employees or claim an RI credit.
- **DLT Employer Tax Unit [US-RIS5-017]:** TX-17 Quarterly Tax and Wage Report (one report and payment for UI, TDI and JDA) due [[FACT:ri.report.tx17.due=Jan 31; Apr 30; Jul 31; Oct 31]]; zero report required; electronic wage data mandatory above the employee threshold; registration on the BAR form; PEOs and common paymasters not recognised.
- **New hire [US-RIS5-010, US-RIS5-011]:** within [[FACT:ri.newhire.report_days=14]] days of hire or rehire to the RI State Directory of New Hires; multistate employers may designate one state. Statutory field list: open point below.
- **Power of attorney:** RI-2848 [US-RIP51-004].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ri.report.wh.weekly_threshold.monthly` | [[FACT:ri.report.wh.weekly_threshold.monthly=600]] | USD | from 2026-01-01 | US-RIS5-018 | >=600/month weekly deposits; 50-599 monthly (20th); <50 quarterly |
| `ri.report.ri941.due` | [[FACT:ri.report.ri941.due=last day of month after quarter]] |  | from 2026-01-01 | US-RIS5-018 |  |
| `ri.report.w3.due` | [[FACT:ri.report.w3.due=31 January]] |  | 2026-01-01 to 2026-12-31 | US-RIS5-019 | W-2 EFW2 via Tax Portal; electronic mandatory at 25+ RI employees |
| `ri.report.w2.efile_threshold` | [[FACT:ri.report.w2.efile_threshold=25]] |  | 2026-01-01 to 2026-12-31 | US-RIS5-018 | RI employees |
| `ri.report.tx17.due` | [[FACT:ri.report.tx17.due=Jan 31; Apr 30; Jul 31; Oct 31]] |  | from 2022-04-11 | US-RIS5-017 | UI/TDI/JDA combined; electronic wage data at 25+ employees |
| `ri.newhire.report_days` | [[FACT:ri.newhire.report_days=14]] | days | from 1997-10-01 | US-RIS5-010 |  |

**Open research points**

- Not configured in this release [[GAP:RQ-311]]: 15-24-5 statutory field list not read.

## RI.6 Leave

- **Paid sick and safe leave (RIGL 28-57) [US-RIS5-009]:** employers with [[FACT:ri.leave.paid_sick.employer_threshold=18]] or more employees in Rhode Island; accrual one hour per [[FACT:ri.leave.paid_sick.accrual_ratio_hours_worked=35]] hours worked, up to [[FACT:ri.leave.paid_sick.annual_cap_hours=40]] hours a year (accrual and use). Carry-over or year-end payout with front-loading; statutory waiting periods; payout at separation: [[FACT:ri.leave.sick.payout_on_separation=False]]; reinstatement on rehire within the statutory period. Smaller employers owe the same hours unpaid. Municipal and state employees excluded.
- **TCI (insurance-paid family leave) [US-RIS5-021]:** job restoration and continued health benefits; the week cap is unsettled (open point below); it affects benefits only, not the payroll deduction.

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ri.leave.paid_sick.employer_threshold` | [[FACT:ri.leave.paid_sick.employer_threshold=18]] |  | from 2020-01-01 | US-RIS5-009 | RIGL 28-57; <18: 40 h unpaid protected |
| `ri.leave.paid_sick.accrual_ratio_hours_worked` | [[FACT:ri.leave.paid_sick.accrual_ratio_hours_worked=35]] | hours | from 2020-01-01 | US-RIS5-009 | max 40 h/yr |
| `ri.leave.paid_sick.annual_cap_hours` | [[FACT:ri.leave.paid_sick.annual_cap_hours=40]] | hours | from 2020-01-01 | US-RIS5-009 |  |
| `ri.leave.sick.payout_on_separation` | [[FACT:ri.leave.sick.payout_on_separation=False]] |  | from 2020-01-01 | US-RIS5-009 |  |

**Open research points**

- Not configured in this release [[GAP:RQ-309]]: The TCI maximum number of weeks is not settled at tier A (sources disagree).

## RI.7 Termination and final pay

- **Final pay (28-14-4) [US-RIS5-006]:** [[FACT:ri.final_pay.rule=next regular payday; within 24 hours on liquidation/merger/sale/move out of state]].
- **Accrued vacation:** payable at separation after [[FACT:ri.term.vacation.payout_after_years=1]] year of service if accrued or awarded under a CBA, policy or agreement. Paid sick leave is not paid out [US-RIS5-009]. Public-employee comp time is paid at termination [US-RIS5-003].

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ri.final_pay.rule` | [[FACT:ri.final_pay.rule=next regular payday; within 24 hours on liquidation/merger/sale/move out of state]] |  | from 2004-01-01 | US-RIS5-006 | 28-14-4 |
| `ri.term.vacation.payout_after_years` | [[FACT:ri.term.vacation.payout_after_years=1]] | years | from 2004-01-01 | US-RIS5-006 | accrued vacation payable after 1 year of service |

## RI.8 Benefits in kind and taxable wages

- **Income tax:** federal exclusions carry through from federal AGI; no Schedule M addition found for them; H.R. 1 decoupling items not itemised (open point below) [US-RIP52-002, US-RIS5-023].
- **UI and TDI:** employee contributions to retirement, medical and disability plans and cafeteria plans are excluded from UI and TDI wages (Section 3) [US-RIS5-017].

**Open research points**

- Not configured in this release [[GAP:RQ-312]]: H.R. 1 decoupling items for individuals not itemised.

## RI.9 Deductions and garnishments

- **Wage exemption (9-26-4(8)) [US-RIS5-012]:** the state exempt amount for ordinary wages is [[FACT:ri.garn.consumer.state_exempt_amount=50]] USD, less protective than the CCPA, so the federal limits govern ordinary garnishment (Annex FED); debtors on public relief are fully exempt for a period after relief ends.
- **Child support:** e-IWO accepted; fees and priority not read (open point below).

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ri.deduction.remittance_days` | [[FACT:ri.deduction.remittance_days=21]] | days | from 1990-01-01 | US-RIS5-007 | after end of month deducted |
| `ri.garn.consumer.state_exempt_amount` | [[FACT:ri.garn.consumer.state_exempt_amount=50]] | USD | from 2025-06-10 | US-RIS5-012 | only 50 exempt under state law: CCPA governs (US-FED-011); relief recipients fully exempt |

**Open research points**

- Not configured in this release [[GAP:RQ-313]]: IWO fee/priority, 28-14-3.2 deduction authorisation, UI separation notice and state tax levy not established from an official source.

## RI.10 Collective agreements and prevailing wage

- **Prevailing wage [US-RIP51-003, US-RIP51-005]:** public works contracts above [[FACT:ri.prevailing_wage.threshold=1000]] USD must state the prevailing wages set by the DLT director, paid weekly. Certified-payroll mechanics not read.

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ri.prevailing_wage.threshold` | [[FACT:ri.prevailing_wage.threshold=1000]] | USD | from 2026-01-01 | US-RIP51-003 | public works; paid weekly |

## RI.11 Indexation

- **Minimum wage:** fixed statutory steps, not indexed [US-RIS5-001].
- **UI wage base:** share of the prior-year average annual wage, rounded up, published each December [US-RIS5-014].
- **TDI wage base and rate:** formula base and fund cost rate set by 15 November [US-RIS5-015].
- **PIT brackets and exemption cut-off:** annual booklet [US-RIS5-019]. **Tipped cash wage:** fixed since 2017 [US-RIS5-002]. The 2027 booklet and DLT release are not yet published (open point below).

## RI.12 Payroll data protection and records

- **SSN (6-48-8) [US-RIS5-020]:** no part of an SSN on material mailed to the individual unless law requires it ([[FACT:ri.data.ssn.mailed_prohibited=True]]); no public display; no requirement over an unsecured connection. A mailed pay statement carries no part of the SSN.

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ri.data.ssn.mailed_prohibited` | [[FACT:ri.data.ssn.mailed_prohibited=True]] |  | from 2008-01-01 | US-RIS5-020 | no part of SSN on mailed materials |

## RI.13 Live legal change

- **2026-01-01:** minimum wage step; new record-keeping / hiring-notice section 28-14-12 (text unread); TDI rate and base, UI base and schedule change [US-RIS5-001, US-RIS5-008, US-RIP9V-001].
- **2025-12-15:** PIT emergency regulation 280-RICR-20-55-16; RI decoupled from H.R. 1 [US-RIS5-023].
- **2027-01-01 (enacted):** minimum wage step [US-RIS5-001].
- **Sweep limit:** DLT news and the 2026 public laws were not read (rilegislature.gov unreachable).

**Parameters (live legal change)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ri.oracle.weekly_2195.withholding` | [[FACT:ri.oracle.weekly_2195.withholding=87.57]] | USD | 2026-01-01 to 2026-12-31 | US-RIS5-019 |  |

## RI.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## RI.15 Special populations

| Population | Rhode Island rule | Register id |
|---|---|---|
| Domestic / household | UI and TDI above a quarterly cash test; minimum wage applies | US-RIS5-022, US-RIS5-017 |
| Agricultural | Exempt from state overtime (28-12-4.3(a)(9)); UI coverage of farm work not confirmed | US-RIS5-003, US-RIS5-022 |
| Minors | Sub-minimum per Section 1; a minor child employed by a parent sole proprietor is excluded from UI and TDI | US-RIS5-002, US-RIS5-022 |
| Tipped | Cash wage [[FACT:ri.minwage.tipped.cash_wage=3.89]] USD; tip credit up to the minimum | US-RIS5-002 |
| Clergy / religious | Churches, ministers and religious orders excluded from UI and TDI; income tax follows federal withholding | US-RIS5-022, US-RIS5-019 |
| Students | Co-op students in credit programmes excluded from UI and TDI; nonprofit student sub-minimum per Section 1 | US-RIS5-022, US-RIS5-002 |
| Nonresident aliens | RI withholding applies where federal withholding applies | US-RIS5-019 |
| Statutory employees | No state rule beyond federal; commission-only real-estate and insurance agents excluded from UI and TDI | US-RIS5-022 |
| Government employees | Federal and other-state employment excluded from RI UI; state and municipal employees excluded from paid sick leave and the weekly-pay rule | US-RIS5-022, US-RIS5-009, US-RIS5-004, US-RIS5-003 |

## RI.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## RI.S Sources

Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file. Authorities:

- Build lead (Claude) under owner delegation (Wallisson Gomes): US-OWN-006, US-OWN-007
- Owner (Wallisson Gomes): US-OWN-008
- RI Department of Human Services, Office of Child Support Services: US-RIS5-011
- RI Department of Labor and Training, Employer Tax Unit: US-RIS5-017
- RI Division of Taxation: US-RIP51-004, US-RIP52-002, US-RIP52-003, US-RIS5-018, US-RIS5-019, US-RIS5-023, US-RIS5-024
- RI General Assembly: US-RIP51-002, US-RIP51-003
- RI House Fiscal Advisory Staff (General Assembly): US-RIP52-001
- RI official authority: US-RIB5-401
- Rhode Island Department of Labor and Training: US-RIP9V-001
- Rhode Island Division of Taxation: US-RIP9V-002
- Rhode Island General Assembly: US-RIL-001, US-RIS5-001, US-RIS5-002, US-RIS5-003, US-RIS5-004, US-RIS5-005, US-RIS5-006, US-RIS5-007, US-RIS5-008, US-RIS5-009, US-RIS5-010, US-RIS5-012, US-RIS5-013, US-RIS5-014, US-RIS5-015, US-RIS5-016, US-RIS5-020, US-RIS5-021, US-RIS5-022
- US Congress (GovInfo US Code 2024): US-FED-011
- US Department of Labor Wage and Hour Division: US-RIP51-005

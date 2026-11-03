# Annex NH: New Hampshire


United States Country Configuration Guide, jurisdiction annex NH. Tax year 2026; currency USD (two decimal places).

**Scope of this annex.**

This annex holds the New Hampshire layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in Annex FED, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register, with the authority and address listed in section NH.S (the source address is held in the register row). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

**Jurisdiction layer.**

| Item | Value |
|---|---|
| Annex tier | T1 (verified) |
| Basis | DRA list of administered taxes carries no wage/withholding tax [US-NH-006] |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

**Configuration decisions.**

- New Hampshire has no state wage tax ([[FACT:nh.pit.exists=False]]): no withholding, no state certificate and no annual reconciliation (tier T1).
- Final pay on discharge is due within [[FACT:nh.term.final_pay.discharge.hours=72]] hours.
- Wage garnishment on New Hampshire judgments exempts [[FACT:nh.garn.consumer.exempt_multiple_fmw=50]] times the federal minimum wage, [[FACT:nh.garn.consumer.exempt.weekly=362.5]] USD a week.
- Parental medical leave is not configured (non-blocking gap in section NH.6).

## NH.1 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nh.labour.minwage.state.follows_federal` | [[FACT:nh.labour.minwage.state.follows_federal=True]] | 2011-08-21 | open | US-NHS5-003 (A.1, NH General Court) | federal minimum "as amended" ([[FACT:fed.minwage.hourly=7.25]] in 2026, Annex FED); no NH figure of its own |
| `nh.labour.tip_credit.cash_wage.min_ratio` | [[FACT:nh.labour.tip_credit.cash_wage.min_ratio=45]] percent | 2011-08-21 | open | US-NHS5-003 (A.1, NH General Court) | base at least 45% of minimum = [[FACT:nh.minwage.tipped.cash_wage=3.27]]; >30 USD/month in tips |
| `nh.minwage.tipped.cash_wage` | [[FACT:nh.minwage.tipped.cash_wage=3.27]] USD | 2011-08-21 | open | US-NHS5-003 (A.1, NH General Court) | never below [[FACT:nh.minwage.tipped.cash_wage=3.27]] |
| `nh.labour.minwage.learner_youth.ratio` | [[FACT:nh.labour.minwage.learner_youth.ratio=75]] percent | 2011-08-21 | open | US-NHS5-003 (A.1, NH General Court) | learners <6 months; persons aged 16 or under |
| `nh.labour.meal_credit.full_board_room.weekly` | [[FACT:nh.labour.meal_credit.full_board_room.weekly=45.0]] USD | 2011-08-21 | open | US-NHS5-003 (A.1, NH General Court) | hotel/restaurant only; 6.45/day; meals 39.45/week or 1.88/meal; lodging 10.88/week or 1.80/day |
| `nh.overtime.weekly_threshold_hours` | [[FACT:nh.overtime.weekly_threshold_hours=40]] hours | 2011-08-21 | open | US-NHS5-003 (A.1, NH General Court) | NH rule only for non-FLSA employers |
| `nh.overtime.premium.multiplier` | [[FACT:nh.overtime.premium.multiplier=1.5]] ratio | 2011-08-21 | open | US-NHS5-003 (A.1, NH General Court) | - |
| `nh.labour.pay_timing.weekly_days` | [[FACT:nh.labour.pay_timing.weekly_days=8]] days | 2026-01-01 | open | US-NHS5-001 (A.1, NH General Court) | weekly pay within 8 days after workweek; biweekly within 15 days; semimonthly/monthly needs Commissioner permission |
| `nh.labour.pay_timing.biweekly_days` | [[FACT:nh.labour.pay_timing.biweekly_days=15]] days | 2026-01-01 | open | US-NHS5-001 (A.1, NH General Court) | - |
| `nh.payment.method` | [[FACT:nh.payment.method=cash, EFT, direct deposit (written authorization), payroll card (voluntary consent, fees disclosed, one free withdrawal), or check; check must be offered]] | 2026-01-01 | open | US-NHS5-001 (A.1, NH General Court) | 275:43 I-II |
| `nh.labour.reporting_pay.hours` | [[FACT:nh.labour.reporting_pay.hours=2]] hours | 2026-01-01 | open | US-NHS5-011 (A.1, NH General Court) | not counties/municipalities |
| `nh.labour.meal_break.minutes` | [[FACT:nh.labour.meal_break.minutes=30]] minutes | 2026-01-01 | open | US-NHS5-011 (A.1, NH General Court) | after 5 consecutive hours |
| `nh.labour.expense_reimbursement.days` | [[FACT:nh.labour.expense_reimbursement.days=30]] days | 2026-01-01 | open | US-NHS5-011 (A.1, NH General Court) | 275:57 |

Rules:

- The employer must make up any shortfall to the minimum wage for each pay period.
- The fluctuating-workweek method is barred for delivery drivers and sales merchandisers.
- Paydays must be regular and designated in advance.
- Semi-monthly or monthly pay needs the Labor Commissioner's written permission and must still be at least monthly.
- An employer that uses EFT, direct deposit or cards must also offer payment by check.

## NH.2 Income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nh.pit.exists` | [[FACT:nh.pit.exists=False]] | 2026-01-01 | open | US-NH-006 (A.2, NH Department of Revenue Administration) | no withholding, no state W-4, no reconciliation; I&D tax repealed from 2025-01-01 (US-NH-001) |

## NH.2b Non-resident regime and reciprocity

No New Hampshire rule is configured in this domain; the federal treatment in Annex FED applies.

## NH.2c Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nh.local_wage_tax.exists` | [[FACT:nh.local_wage_tax.exists=False]] | 2026-01-01 | open | US-NH-006 (A.2, NH Department of Revenue Administration) | - |

## NH.3 Social insurance: unemployment, disability, paid leave and payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nh.sui.wage_base` | [[FACT:nh.sui.wage_base=14000]] USD | 2026-01-01 | open | US-NHS5-007 (A.1, NH General Court) | 282-A:69 I fixed, not indexed; other-state wages count |
| `nh.sui.wage_base.other_state_credit` | [[FACT:nh.sui.wage_base.other_state_credit=True]] | 2026-01-01 | open | US-NHS5-007 (A.1, NH General Court) | - |
| `nh.ui.rate.statutory` | [[FACT:nh.ui.rate.statutory=2.7]] percent | 2026-01-01 | open | US-NHS5-007 (A.1, NH General Court) | subject to experience rating |
| `nh.ui.fund_balance_reduction.rate` | [[FACT:nh.ui.fund_balance_reduction.rate=1.0]] percent | 2026-01-01 | 2026-12-31 | US-NHP9W-001 (A.2, New Hampshire Employment Security) | Q1-Q4 2026 |
| `nh.sui.new_employer.rate` | [[FACT:nh.sui.new_employer.rate=1.7]] percent | 2026-01-01 | 2026-12-31 | US-NHP9W-001 (A.2, New Hampshire Employment Security) | 2.7 (statutory, US-NH-005 rule "[[FACT:nh.ui.rate.statutory=2.7]]% minus any FBR") - 1.00 FBR (US-NHP9W-001) = 1.7 |
| `nh.ui.inverse_surcharge.rate` | [[FACT:nh.ui.inverse_surcharge.rate=0.5]] percent | 2026-01-01 | 2026-12-31 | US-NHP9W-001 (A.2, New Hampshire Employment Security) | negative-rated employers |
| `nh.ui.emergency_surcharge.rate` | [[FACT:nh.ui.emergency_surcharge.rate=0.0]] percent | 2026-01-01 | 2026-12-31 | US-NHP9W-001 (A.2, New Hampshire Employment Security) | - |
| `nh.ui.admin_contribution.range` | [[FACT:nh.ui.admin_contribution.range=0.1-0.4% carved out of the rate]] | 2026-01-01 | open | US-NHP7-001 (A.2, NH official authority) | not added |
| `nh.sui.employee.rate` | [[FACT:nh.sui.employee.rate=0]] percent | 2026-01-01 | open | US-NHS5-007 (A.1, NH General Court) | shall not be deducted |
| `nh.sdi_pfml.exists` | [[FACT:nh.sdi_pfml.exists=False]] | 2026-01-01 | open | US-NH-006 (A.2, NH Department of Revenue Administration) | absence on DRA list; FED list of TDI states |
| `nh.pfml.mandatory` | [[FACT:nh.pfml.mandatory=False]] | 2021-07-01 | open | US-NHS5-015 (A.1, NH General Court) | Granite State Paid Family Leave voluntary; employers >50 may sponsor; individual pool premium max 5/week |

Rules:

- The Granite State Paid Family Leave Plan offers FMLI through the state carrier.

- Not configured in this release [[GAP:RQ-097]]: The new-employer rate of [[FACT:nh.sui.new_employer.rate=1.7]] percent is derived from the statutory rate less the fund-balance reduction, not stated on an authority page.
- Not configured in this release [[GAP:RQ-098]]: The treatment of 401(k) deferrals and cafeteria-plan reductions in New Hampshire unemployment wages is not settled (RSA 282-A:15 is silent).

## NH.4 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nh.payslip.hire_notice` | [[FACT:nh.payslip.hire_notice=written notice at hire and before change of rate, basis, payday/place, computation method; fringe-benefit policy]] | 2020-03-05 | open | US-NHS5-004 (A.1, NH Department of Labor / Office of Legislative Services) | Lab 803.03 |
| `nh.payslip.items` | [[FACT:nh.payslip.items=statement of deductions each pay period a deduction is made; monthly itemized accounting for 275:48 I(d) deductions]] | 2026-01-01 | open | US-NHP51-001 (A.1, NH General Court) | no itemized pay-statement content list |

Rules:

- NH has no itemized pay-statement content list.
- At hire and before any change, the employer must give written notice of: the rate, the pay basis, the day and place of payment, and the method of computing wages.
- A written or posted fringe-benefit policy is also required (vacation, holiday, sick, bonus, severance, expenses, pension).
- No statute or rule read addresses electronic delivery of the deduction statement.
- Language: English; no second-language rule for the payslip. (US-NHL-001, US-NHP9L-002)

- Not configured in this release [[GAP:RQ-099]]: Electronic pay statements not addressed in RSA 275:49 IV or Lab 803.03.
- Not configured in this release [[GAP:RQ-100]]: No territorial clause in RSA 275 for out-of-state work.

## NH.5 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nh.report.ui.quarterly_due` | [[FACT:nh.report.ui.quarterly_due=last day of month following quarter]] | 2026-01-01 | open | US-NHS5-013 (A.3, New Hampshire Employment Security (NHES)) | 2016 Handbook (A.3); WebTax +2 days; late 10% min 25 |
| `nh.newhire.report_days` | [[FACT:nh.newhire.report_days=20]] days | 2026-01-01 | open | US-NHS5-006 (A.1, NH General Court) | 282-A:117-a |
| `nh.report.new_hire.contractor_threshold` | [[FACT:nh.report.new_hire.contractor_threshold=2500]] USD | 2026-01-01 | open | US-NHS5-006 (A.1, NH General Court) | non-casual independent contractors also reported |

Rules:

- State withholding return / state W-2: none. There is no state wage tax. (US-NH-006)
- Quarterly Employer Tax and Wage Report (NHES). (US-NHS5-013, US-NH-005)
- Gross wages of all employees must be reported.
- A W-4 copy is accepted.
- Multistate employers may designate one state and notify HHS.
- Registration and TPA access through NHUIS. (US-NHP8-003, US-NHP9-001)
- The Unemployment Notice poster is mandatory. (US-NHS5-013)

- Not configured in this release [[GAP:RQ-101]]: The quarterly due date, late fee and interest come from the agency's older employer handbook; the current rule Emp 303.02 was not available.

## NH.6 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nh.leave.sick.state_statute.exists` | [[FACT:nh.leave.sick.state_statute.exists=False]] | 2026-01-01 | open | US-NHS5-011 (A.1, NH General Court) | policy-based only; then wages (275:43 V) |
| `nh.leave.lactation.min_employees` | [[FACT:nh.leave.lactation.min_employees=6]] | 2025-07-01 | open | US-NHS5-011 (A.1, NH General Court) | unpaid ~30 min per 3 h for 1 year |

Rules:

- Paid sick leave: NH has no statute.
- A written policy must be made available at hire.
- No make-up time may be required.
- Pay impact is limited to handling unpaid absence.

- Not configured in this release [[GAP:RQ-102]]: Parental medical leave under RSA 275:37-f rests on a source that cannot be used as a primary source; the statute was not read.

## NH.7 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nh.term.final_pay.discharge.hours` | [[FACT:nh.term.final_pay.discharge.hours=72]] hours | 1967-09-01 | open | US-NHS5-002 (A.1, NH General Court) | 275:44 |
| `nh.term.final_pay.resignation` | [[FACT:nh.term.final_pay.resignation=next regular payday, or 72 hours if one pay period's notice]] | 1967-09-01 | open | US-NHS5-002 (A.1, NH General Court) | - |
| `nh.term.vacation.payout` | [[FACT:nh.term.vacation.payout=per written policy (no statutory duty); accrued benefits do not lapse on policy change]] | 2020-03-05 | open | US-NHS5-004 (A.1, NH Department of Labor / Office of Legislative Services) | - |

Rules:

- There is no statutory duty to pay out unused vacation.
- No UI separation notice to the employee is required by any source read.
- NHES sends a "Request to Employer for Separation Information" when a claim is filed. (US-NHS5-013)

## NH.8 Benefits in kind and taxable wages

No New Hampshire rule is configured in this domain; the federal treatment in Annex FED applies.

## NH.9 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nh.garn.consumer.exempt_multiple_fmw` | [[FACT:nh.garn.consumer.exempt_multiple_fmw=50]] | 2026-01-01 | open | US-NHS5-009 (A.1, NH General Court) | 50x FLSA minimum per week exempt |
| `nh.garn.consumer.exempt.weekly` | [[FACT:nh.garn.consumer.exempt.weekly=362.5]] USD | 2026-01-01 | open | US-NHS5-009 (A.1, NH General Court) | 50 x [[FACT:fed.minwage.hourly=7.25]] FLSA minimum (US-NHS5-009 rule) = [[FACT:nh.garn.consumer.exempt.weekly=362.50]] |
| `nh.garn.support.employer_fee.per_withholding` | [[FACT:nh.garn.support.employer_fee.per_withholding=1.0]] USD | 2010-07-23 | open | US-NHS5-008 (A.1, NH General Court) | remit same day as pay; notify within 15 days of termination |

Rules:

- A deduction may not offset items the employee needs to do the job.
- Wages for work done after the writ is served are exempt.
- Wages earned before service are exempt, except on a debt on an NH court judgment.
- Remit on the same day the employee is paid.
- Support withholding has priority over other state process.
- Lump sums (severance, accumulated sick or vacation pay, bonuses, commissions) can be taken up to the arrears when the obligor is non-compliant.

## NH.10 Collective agreements and prevailing wage

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nh.prevailing_wage.exists` | [[FACT:nh.prevailing_wage.exists=False]] | 2026-01-01 | open | US-NHP8-001 (A.1, New Hampshire General Court (gc.nh.gov)) | RSA 280 repealed |

Rules:

- Federal Davis-Bacon applies only to federally assisted work.
- No state certified-payroll duty exists.

## NH.11 Indexation

Rules:

- Nothing is indexed by NH statute.
- The minimum wage is pegged to the federal minimum. (US-NHS5-003)
- Experience rates are set for July–June. (US-NHP9W-002)

## NH.12 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nh.records.retention_years` | [[FACT:nh.records.retention_years=3]] years | 2011-08-21 | open | US-NHS5-003 (A.1, NH General Court) | 279:27; 275:49 VI |
| `nh.data.breach_notice.exists` | [[FACT:nh.data.breach_notice.exists=True]] | 2007-01-01 | open | US-NHS5-010 (A.1, NH General Court) | 359-C:19-20 |

Rules:

- Covers name plus unencrypted SSN, driver's licence or government ID, or a financial account number with its access code.
- Notify affected individuals as soon as possible, and notify the NH Attorney General or the primary regulator.
- A payroll processor holding the data must notify the data owner immediately.

- Not configured in this release [[GAP:RQ-103]]: RSA 507-H employee-data exemption not read.

## NH.13 Live legal change

No New Hampshire rule is configured in this domain; the federal treatment in Annex FED applies.

- Not configured in this release [[GAP:RQ-104]]: The final status of HB 1484 (minimum wage) and SB 416 (tips) rests on secondary sources only.

## NH.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## NH.15 Special populations

- Agricultural: Farm labor exempt from the NH minimum wage; under-16 farm work needs no certificate. (US-NHS5-003, US-NHS5-005, US-NHS5-007, US-NHS5-014)
- Tipped: tip credit with make-up; tips are the employee's property. (US-NHS5-003)
- Clergy/religious: No wage-tax angle. (US-NHS5-007)
- Nonresident aliens: No state withholding. (US-NHS5-007)
- Statutory employees: No NH rule beyond federal. (US-NHS5-005, US-NHS5-007)
- Not configured in this release [[GAP:RQ-105]]: Thresholds, amounts or conditions for these populations are stated in the sources read without a confirmed value record and are not configured from this annex: Domestic/household; Agricultural; Minors; Tipped; Clergy/religious; Students; Nonresident aliens; Statutory employees; Government employees; Family employees.

## NH.16 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## NH.S Sources

| Source | Authority |
|---|---|
| US-NH-006 | NH Department of Revenue Administration |
| US-NHP51-001 | NH General Court |
| US-NHP7-001 | NH official authority |
| US-NHP8-001 | New Hampshire General Court (gc.nh.gov) |
| US-NHP9W-001 | New Hampshire Employment Security |
| US-NHS5-001 | NH General Court |
| US-NHS5-002 | NH General Court |
| US-NHS5-003 | NH General Court |
| US-NHS5-004 | NH Department of Labor / Office of Legislative Services |
| US-NHS5-006 | NH General Court |
| US-NHS5-007 | NH General Court |
| US-NHS5-008 | NH General Court |
| US-NHS5-009 | NH General Court |
| US-NHS5-010 | NH General Court |
| US-NHS5-011 | NH General Court |
| US-NHS5-013 | New Hampshire Employment Security (NHES) |
| US-NHS5-015 | NH General Court |

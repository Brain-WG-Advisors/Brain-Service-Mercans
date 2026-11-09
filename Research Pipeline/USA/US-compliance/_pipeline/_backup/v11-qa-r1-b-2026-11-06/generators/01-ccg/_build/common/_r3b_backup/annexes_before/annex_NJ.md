# Annex NJ: New Jersey


United States Country Configuration Guide, jurisdiction annex NJ. Tax year 2026; currency USD (two decimal places).

**Scope of this annex.**

This annex holds the New Jersey layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in Annex FED, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register, with the authority and address listed in section NJ.S (the source address is held in the register row). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

**Jurisdiction layer.**

| Item | Value |
|---|---|
| Annex tier | T4 (verified, attempt 5) |
| Basis | State withholding [US-NJP51-001]; Jersey City employer payroll tax of [[FACT:nj.pit.local.jersey_city.employer_payroll_tax.rate=1]] percent, quarterly returns to the City (city ordinance) [US-NJP6-001]; Newark employer payroll tax of [[FACT:nj.pit.local.newark.employer_payroll_tax.rate=1]] percent (a reduced rate applies where most of the workforce lives in Newark), quarterly returns to the City [US-NJP6-002]: employer-only city calculation and city return |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

**Configuration decisions.**

- Values published for 2027 (minimum wages, unemployment, disability and family-leave rates and wage bases) are listed with a 2027-01-01 start; configure them as dated rows, not as 2026 values.
- The state gross income tax base differs from the federal base: 403(b) and 457 deferrals are taxable ([[FACT:nj.bik.nj.403b_457.taxable=True]]), HSA contributions are not excluded ([[FACT:nj.bik.nj.hsa.excluded=False]]) and dependent-care assistance is taxable ([[FACT:nj.bik.nj.dependent_care_129.taxable=True]]). The unemployment, disability and family-leave base includes 401(k) deferrals ([[FACT:nj.sui.wages.401k_included=True]]) and cafeteria-plan salary reductions ([[FACT:nj.sui.wages.section125_included=True]]).
- The Newark and Jersey City payroll taxes ([[FACT:nj.pit.local.newark.employer_payroll_tax.rate=1]] and [[FACT:nj.pit.local.jersey_city.employer_payroll_tax.rate=1]] percent) are paid by the employer and may not be deducted from employee pay; they are filed with the city (tier T4).
- Quarterly wage reports: build to the stricter Department of Labor rule, with no weekend or holiday extension (`nj.report.wr30.due`).

## NJ.1 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nj.minwage.hourly` | [[FACT:nj.minwage.hourly=15.92]] USD | 2026-01-01 | 2026-12-31 | US-NJS5-009 (A.2, NJ Department of Labor and Workforce Development) | most employees |
| `nj.minwage.hourly` | [[FACT:nj.minwage.hourly=16.48]] USD | 2027-01-01 | 2027-12-31 | US-NJS5-008 (A.2, NJ Department of Labor and Workforce Development) | published 2026-09-29 |
| `nj.labour.minwage.small_seasonal.hourly` | [[FACT:nj.labour.minwage.small_seasonal.hourly=15.23]] USD | 2026-01-01 | 2026-12-31 | US-NJS5-009 (A.2, NJ Department of Labor and Workforce Development) | fewer than 6 employees or seasonal |
| `nj.labour.minwage.small_seasonal.hourly` | [[FACT:nj.labour.minwage.small_seasonal.hourly=16.25]] USD | 2027-01-01 | 2027-12-31 | US-NJS5-008 (A.2, NJ Department of Labor and Workforce Development) | - |
| `nj.labour.minwage.farm.hourly` | [[FACT:nj.labour.minwage.farm.hourly=14.2]] USD | 2026-01-01 | 2026-12-31 | US-NJS5-009 (A.2, NJ Department of Labor and Workforce Development) | hourly or piece-rate |
| `nj.labour.minwage.farm.hourly` | [[FACT:nj.labour.minwage.farm.hourly=15.0]] USD | 2027-01-01 | 2027-12-31 | US-NJS5-008 (A.2, NJ Department of Labor and Workforce Development) | - |
| `nj.labour.minwage.ltc_direct_care.hourly` | [[FACT:nj.labour.minwage.ltc_direct_care.hourly=18.92]] USD | 2026-01-01 | 2026-12-31 | US-NJS5-009 (A.2, NJ Department of Labor and Workforce Development) | general + 3.00 |
| `nj.labour.minwage.ltc_direct_care.hourly` | [[FACT:nj.labour.minwage.ltc_direct_care.hourly=19.48]] USD | 2027-01-01 | 2027-12-31 | US-NJS5-008 (A.2, NJ Department of Labor and Workforce Development) | - |
| `nj.minwage.tipped.cash_wage` | [[FACT:nj.minwage.tipped.cash_wage=6.05]] USD | 2026-01-01 | 2026-12-31 | US-NJS5-009 (A.2, NJ Department of Labor and Workforce Development) | [[FACT:nj.minwage.tipped.cash_wage=6.05]] + [[FACT:nj.labour.tip_credit.max.hourly=9.87]] = [[FACT:nj.minwage.hourly=15.92]] |
| `nj.minwage.tipped.cash_wage` | [[FACT:nj.minwage.tipped.cash_wage=6.61]] USD | 2027-01-01 | 2027-12-31 | US-NJS5-008 (A.2, NJ Department of Labor and Workforce Development) | [[FACT:nj.minwage.tipped.cash_wage=6.61]] + [[FACT:nj.labour.tip_credit.max.hourly=9.87]] = [[FACT:nj.minwage.hourly=16.48]] |
| `nj.labour.tip_credit.max.hourly` | [[FACT:nj.labour.tip_credit.max.hourly=9.87]] USD | 2026-01-01 | 2026-12-31 | US-NJS5-009 (A.2, NJ Department of Labor and Workforce Development) | fixed; stays [[FACT:nj.labour.tip_credit.max.hourly=9.87]] in 2027 |
| `nj.overtime.weekly_threshold_hours` | [[FACT:nj.overtime.weekly_threshold_hours=40]] hours | 2026-01-01 | open | US-NJS5-012 (A.3, NJ Department of Labor and Workforce Development, Wage and Hour Compliance) | 7-day workweek; no daily OT |
| `nj.overtime.premium.multiplier` | [[FACT:nj.overtime.premium.multiplier=1.5]] ratio | 2026-01-01 | open | US-NJS5-025 (A.2, NJ Department of Labor and Workforce Development) | - |
| `nj.pay_frequency.rule` | [[FACT:nj.pay_frequency.rule=at least twice each calendar month; period ends max 10 working days before payday]] | 1965-01-01 | open | US-NJS5-001 (A.1, NJ Legislature (text as published by NJ DOL Wage and Hour Compliance, Selected NJ State Labor Laws)) | exempt classes may be monthly |
| `nj.labour.direct_deposit.consent_required` | [[FACT:nj.labour.direct_deposit.consent_required=True]] | 1965-01-01 | open | US-NJS5-001 (A.1, NJ Legislature (text as published by NJ DOL Wage and Hour Compliance, Selected NJ State Labor Laws)) | written uncoerced, revocable; paycard same plus fee disclosure, one free withdrawal, opt-out |

- Not configured in this release [[GAP:RQ-106]]: DWBR chapter number and rule adoption status unconfirmed.
- Not configured in this release [[GAP:RQ-107]]: Minor hour limits not read.

## NJ.2 Income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nj.wh.certificate` | [[FACT:nj.wh.certificate=NJ-W4 (1-21); federal W-4 may not be used]] | 2026-01-01 | open | US-NJS5-024 (A.2, NJ Division of Taxation) | - |
| `nj.wh.method` | [[FACT:nj.wh.method=NJ-WT percentage method (Rate A-E by NJ-W4); tables unchanged since 2020-10-01]] | 2020-10-01 | open | US-NJP51-002 (A.2, NJ Division of Taxation) | NJ-WT Sept 2025 current |
| `nj.pit.allowance.annual` | [[FACT:nj.pit.allowance.annual=1000]] USD | 2026-01-01 | open | US-NJP51-001 (A.2, NJ Division of Taxation) | weekly 19.20, biweekly 38.40, semimonthly 41.60, monthly 83.30 |
| `nj.pit.supplemental.method` | [[FACT:nj.pit.supplemental.method=combined with regular wages, or without allowances if separate; no flat rate]] | 2026-01-01 | open | US-NJP51-001 (A.2, NJ Division of Taxation) | accumulated sick/vacation payouts supplemental |

## NJ.2b Non-resident regime and reciprocity

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nj.reciprocity.states` | [[FACT:nj.reciprocity.states=PA (Form NJ-165)]] | 2026-01-01 | open | US-NJP51-001 (A.2, NJ Division of Taxation) | does not cover PA local wage taxes; NJ-165 also for military spouses |
| `nj.pit.resident.other_state_rule` | [[FACT:nj.pit.resident.other_state_rule=withhold all wages; reduce by other state's withholding; none if other state's withholding at least as high]] | 2026-01-01 | open | US-NJP51-001 (A.2, NJ Division of Taxation) | convenience test since TY2023 for residents of states using one |

## NJ.2c Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nj.pit.local.employee_tax.exists` | [[FACT:nj.pit.local.employee_tax.exists=False]] | 2026-01-01 | open | US-NJP6-001 (A.2, City of Jersey City (Tax Collector)) | no local tax withheld from employees |
| `nj.pit.local.newark.employer_payroll_tax.rate` | [[FACT:nj.pit.local.newark.employer_payroll_tax.rate=1]] percent | 2026-01-01 | open | US-NJP6-001 (A.2, City of Jersey City (Tax Collector)) | employer-paid; no deduction from pay; quarterly |
| `nj.pit.local.jersey_city.employer_payroll_tax.rate` | [[FACT:nj.pit.local.jersey_city.employer_payroll_tax.rate=1]] percent | 2026-01-01 | open | US-NJP6-002 (A.2, City of Newark, Division of Tax Abatement and Special Taxes) | employer-paid; quarterly |

- Not configured in this release [[GAP:RQ-108]]: The chapter number and approval date of S.B. 4219 rest on secondary sources only.

## NJ.3 Social insurance: unemployment, disability, paid leave and payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nj.sui.employee.rate` | [[FACT:nj.sui.employee.rate=0.3825]] percent | 2026-01-01 | open | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | same in 2027 |
| `nj.ui.employee.wf_swf.rate` | [[FACT:nj.ui.employee.wf_swf.rate=0.0425]] percent | 2026-01-01 | open | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | same in 2027 |
| `nj.tdi.employee.rate` | [[FACT:nj.tdi.employee.rate=0.19]] percent | 2026-01-01 | 2026-12-31 | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | - |
| `nj.tdi.employee.rate` | [[FACT:nj.tdi.employee.rate=0.24]] percent | 2027-01-01 | open | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | published |
| `nj.fli.employee.rate` | [[FACT:nj.fli.employee.rate=0.23]] percent | 2026-01-01 | 2026-12-31 | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | - |
| `nj.fli.employee.rate` | [[FACT:nj.fli.employee.rate=0.24]] percent | 2027-01-01 | open | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | published |
| `nj.ui.employee.governmental_reimbursable.rate` | [[FACT:nj.ui.employee.governmental_reimbursable.rate=0.0825]] percent | 2026-01-01 | open | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | - |
| `nj.sui.wage_base` | [[FACT:nj.sui.wage_base=44800]] USD | 2026-01-01 | 2026-12-31 | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | UI + WF/SWF and TDI employer; 28 x SAWW [[FACT:nj.ui.saww.caliber=1,598.66]] rounded up to 100 (inferred multiplier) |
| `nj.sui.wage_base` | [[FACT:nj.sui.wage_base=46400]] USD | 2027-01-01 | open | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | - |
| `nj.tdi_fli.employee.wage_base.annual` | [[FACT:nj.tdi_fli.employee.wage_base.annual=171100]] USD | 2026-01-01 | 2026-12-31 | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | 107 x SAWW rounded up to 100 (inferred) |
| `nj.tdi_fli.employee.wage_base.annual` | [[FACT:nj.tdi_fli.employee.wage_base.annual=177100]] USD | 2027-01-01 | open | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | - |
| `nj.sui.new_employer.rate` | [[FACT:nj.sui.new_employer.rate=2.6825]] percent | 2025-07-01 | open | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | FY2025-26 and 2026-27; DI 0.50, WF/SWF 0.1175, FLI 0 |
| `nj.tdi.employer.new_employer.rate` | [[FACT:nj.tdi.employer.new_employer.rate=0.5]] percent | 2025-07-01 | open | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | - |
| `nj.ui.employer.wf_swf.new_employer.rate` | [[FACT:nj.ui.employer.wf_swf.new_employer.rate=0.1175]] percent | 2025-07-01 | open | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | - |
| `nj.ui.rate.employer_total.min` | [[FACT:nj.ui.rate.employer_total.min=0.5]] percent | 2026-07-01 | 2027-06-30 | US-NJS5-023 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | Table C FY2026-27 total 0.5-5.8 |
| `nj.ui.rate.employer_total.max` | [[FACT:nj.ui.rate.employer_total.max=5.8]] percent | 2026-07-01 | 2027-06-30 | US-NJS5-023 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | UI part 0.3825-5.6825 |
| `nj.ui.saww.caliber` | [[FACT:nj.ui.saww.caliber=1598.66]] USD | 2026-01-01 | 2026-12-31 | US-NJS5-011 (A.2, NJ Department of Labor and Workforce Development) | 2024 SAWW (second preceding year) drives 2026 bases and maxima |
| `nj.ui.base_week.amount` | [[FACT:nj.ui.base_week.amount=310]] USD | 2026-01-01 | 2026-12-31 | US-NJS5-011 (A.2, NJ Department of Labor and Workforce Development) | 20 x 15.49 rounded up |
| `nj.ui.base_week.amount` | [[FACT:nj.ui.base_week.amount=319]] USD | 2027-01-01 | open | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | 20 x [[FACT:nj.minwage.hourly=15.92]] rounded up |
| `nj.sui.wages.401k_included` | [[FACT:nj.sui.wages.401k_included=True]] | 2026-01-01 | open | US-NJS5-017 (A.3, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | 401(k) deferrals and cafeteria-plan reductions are included where cash is electable; dependent-care assistance and personal use of a company car are also included. |
| `nj.sui.wages.section125_included` | [[FACT:nj.sui.wages.section125_included=True]] | 2026-01-01 | open | US-NJS5-017 (A.3, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | - |
| `nj.ui.in_kind.room_board.weekly` | [[FACT:nj.ui.in_kind.room_board.weekly=301.5]] USD | 2026-01-01 | 2026-12-31 | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | only when employer assigns no value; lodging [[FACT:nj.bik.lodging.weekly=129.20]]/week; meals [[FACT:nj.bik.meals.daily=34.50]]/day |
| `nj.ui.in_kind.room_board.weekly` | [[FACT:nj.ui.in_kind.room_board.weekly=312.3]] USD | 2027-01-01 | open | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | lodging 133.90; meals 35.70 |
| `nj.tdi.max_weekly_benefit` | [[FACT:nj.tdi.max_weekly_benefit=1119]] USD | 2026-01-01 | 2026-12-31 | US-NJS5-010 (A.2, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | 70% x SAWW |
| `nj.ui.employee.max_annual` | [[FACT:nj.ui.employee.max_annual=190.4]] USD | 2026-01-01 | 2026-12-31 | US-NJP51-004 (A.2, NJ Division of Taxation) | 0.425% x [[FACT:nj.sui.wage_base=44,800]] (Treasury M-6025, second authority) |
| `nj.tdi.employee.max_annual` | [[FACT:nj.tdi.employee.max_annual=325.09]] USD | 2026-01-01 | 2026-12-31 | US-NJP51-004 (A.2, NJ Division of Taxation) | [[FACT:nj.tdi.employee.rate=0.19]]% x [[FACT:nj.tdi_fli.employee.wage_base.annual=171,100]] |
| `nj.fli.employee.max_annual` | [[FACT:nj.fli.employee.max_annual=393.53]] USD | 2026-01-01 | 2026-12-31 | US-NJP51-004 (A.2, NJ Division of Taxation) | [[FACT:nj.fli.employee.rate=0.23]]% x [[FACT:nj.tdi_fli.employee.wage_base.annual=171,100]] |

- Not configured in this release [[GAP:RQ-109]]: The multiples of the state average weekly wage and the rounding used to set the unemployment, disability and family-leave wage bases were inferred from the published figures, not read in the statute.

## NJ.4 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nj.payslip.items` | [[FACT:nj.payslip.items=deductions statement; employers 10+ add gross, net, rate and hours]] | 2026-01-01 | open | US-NJP8-001 (A.2, NJ Department of Labor and Workforce Development, Wage and Hour (nj.gov/labor)) | 34:11-4.6(c); electronic unless employee asks paper |
| `nj.payslip.full_content.employer_threshold` | [[FACT:nj.payslip.full_content.employer_threshold=10]] | 2026-01-01 | open | US-NJP8-001 (A.2, NJ Department of Labor and Workforce Development, Wage and Hour (nj.gov/labor)) | - |

## NJ.5 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nj.report.wr30.due` | [[FACT:nj.report.wr30.due=30th of month after quarter, no weekend/holiday extension]] | 2026-01-01 | open | US-NJS5-017 (A.3, NJ Department of Labor and Workforce Development, Division of Employer Accounts) | SSN, name, gross wages, base weeks |
| `nj.newhire.report_days` | [[FACT:nj.newhire.report_days=20]] days | 2026-01-01 | open | US-NJS5-018 (A.2, NJ Department of Human Services, Division of Family Development (New Jersey Child Support Employer Services Portal)) | incl. independent contractors; DOB and hire date required |
| `nj.report.nj927.due` | [[FACT:nj.report.nj927.due=30th of month after quarter (electronic)]] | 2026-01-01 | open | US-NJP51-001 (A.2, NJ Division of Taxation) | DOL says no weekend extension - build to stricter rule |
| `nj.report.nj500.threshold` | [[FACT:nj.report.nj500.threshold=500]] USD | 2026-01-01 | open | US-NJP51-001 (A.2, NJ Division of Taxation) | withheld in month 1 or 2 of quarter; due 15th |
| `nj.report.nj927w.threshold` | [[FACT:nj.report.nj927w.threshold=10000]] USD | 2026-01-01 | open | US-NJP51-001 (A.2, NJ Division of Taxation) | prior-year liability; weekly payer |
| `nj.report.njw3.due` | [[FACT:nj.report.njw3.due=February 15]] | 2026-01-01 | open | US-NJP51-001 (A.2, NJ Division of Taxation) | electronic mandatory since TY2020 |

Rules:

- Local: Newark and Jersey City quarterly employer payroll tax returns. (US-NJP6-001, US-NJS5-013)

- Not configured in this release [[GAP:RQ-110]]: NJ-WT next-business-day vs DOL no-extension conflict for NJ-927/WR-30.

## NJ.6 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nj.leave.esl.accrual_ratio_hours_worked` | [[FACT:nj.leave.esl.accrual_ratio_hours_worked=30]] hours | 2018-10-29 | open | US-NJS5-007 (A.2, NJ Department of Labor and Workforce Development) | all employers; max 40 h/benefit year; usable from day 120 |
| `nj.leave.esl.annual_cap_hours` | [[FACT:nj.leave.esl.annual_cap_hours=40]] hours | 2018-10-29 | open | US-NJS5-007 (A.2, NJ Department of Labor and Workforce Development) | - |

Rules:

- Vacation and holiday pay are not required by NJ law; if offered, the policy is enforceable. Jury duty: unpaid time off is protected. (US-NJS5-012)

- Not configured in this release [[GAP:RQ-111]]: ESL carry-over cap and treatment at termination not read in statute.

## NJ.7 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nj.term.separation_notice.form` | [[FACT:nj.term.separation_notice.form=BC-10 at every separation]] | 2026-01-01 | open | US-NJS5-015 (A.2, NJ Department of Labor and Workforce Development, Division of Unemployment Insurance) | - |
| `nj.final_pay.rule` | [[FACT:nj.final_pay.rule=regular payday for the period in which employment ended]] | 2026-01-01 | open | US-NJS5-003 (A.1, NJ Legislature / NJ DOL (text as published by NJ DOL)) | discharge, layoff, resignation |
| `nj.term.warn.severance.weeks_per_year` | [[FACT:nj.term.warn.severance.weeks_per_year=1]] | 2023-04-10 | open | US-NJS5-020 (A.2, NJ Department of Labor and Workforce Development (Rapid Response)) | 100+ employees; mass layoff 50+ in 30 days; +4 weeks if notice <90 days; DOL form restatement |

Rules:

- Deductions from final pay for unreturned property: prohibited. (US-NJS5-012)

- Not configured in this release [[GAP:RQ-112]]: Whether employers must also send the Department of Labor an electronic copy of Form BC-10 rests on secondary sources only.
- Not configured in this release [[GAP:RQ-113]]: NJ WARN statute text and severance payment timing not read.

## NJ.8 Benefits in kind and taxable wages

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nj.bik.nj.403b_457.taxable` | [[FACT:nj.bik.nj.403b_457.taxable=True]] | 2025-09-01 | open | US-NJS5-006 (A.2, NJ Division of Taxation) | 401(k) excluded; 403(b), 457 taxable when contributed |
| `nj.bik.nj.hsa.excluded` | [[FACT:nj.bik.nj.hsa.excluded=False]] | 2025-09-01 | open | US-NJS5-006 (A.2, NJ Division of Taxation) | A2634 conformity not enacted |
| `nj.bik.nj.dependent_care_129.taxable` | [[FACT:nj.bik.nj.dependent_care_129.taxable=True]] | 2025-09-01 | open | US-NJS5-006 (A.2, NJ Division of Taxation) | also IRC 137 adoption |
| `nj.bik.nj.section125.excluded` | [[FACT:nj.bik.nj.section125.excluded=only plans requiring minimum medical/life/LTD purchase or listed cash-option cases]] | 2025-09-01 | open | US-NJS5-006 (A.2, NJ Division of Taxation) | other cafeteria contributions taxable |

## NJ.9 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nj.garn.consumer.max_rate_of_gross` | [[FACT:nj.garn.consumer.max_rate_of_gross=10]] percent | 2022-07-01 | open | US-NJS5-021 (A.2, New Jersey Judiciary (Superior Court Clerk)) | lesser of 10% gross, 25% disposable, excess over [[FACT:nj.garn.consumer.floor.weekly=217.50]]/week; one execution at a time |
| `nj.garn.consumer.floor.weekly` | [[FACT:nj.garn.consumer.floor.weekly=217.5]] USD | 2022-07-01 | open | US-NJS5-021 (A.2, New Jersey Judiciary (Superior Court Clerk)) | 30 x [[FACT:fed.minwage.hourly=7.25]] |
| `nj.deduction.political.weekly_max` | [[FACT:nj.deduction.political.weekly_max=5]] USD | 2026-01-01 | open | US-NJS5-004 (A.1, NJ Legislature / NJ DOL (text as published by NJ DOL)) | one committee |

- Not configured in this release [[GAP:RQ-114]]: 2A:17-56 above-10% orders and NJ child-support IWO fee/priority not read.

## NJ.10 Collective agreements and prevailing wage

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nj.prevailing_wage.exists` | [[FACT:nj.prevailing_wage.exists=True]] | 2026-01-01 | open | US-NJP51-007 (A.2, NJ Dept of Labor and Workforce Development) | certified payroll via NJ Wage Hub within 10 days of payment |

## NJ.11 Indexation

Indexation of each value is stated in the note of the value concerned.

## NJ.12 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nj.records.wage_hour.retention_years` | [[FACT:nj.records.wage_hour.retention_years=6]] years | 2026-01-01 | open | US-NJS5-022 (A.1, NJ Department of Labor and Workforce Development (text as published, Selected NJ State Labor Laws)) | UI/TDI current + 4 prior years; ESL 5 years |

- Not configured in this release [[GAP:RQ-115]]: SSN truncation/printing limits on pay statements (C.56:8-164) not obtained.

## NJ.13 Live legal change

No New Jersey rule is configured in this domain; the federal treatment in Annex FED applies.

- Not configured in this release [[GAP:RQ-116]]: The 2026 bulletin indexes of the Treasury and the Department of Labor returned errors, and the 2027 contribution-rate notice was not seen.

## NJ.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## NJ.15 Special populations

- Domestic / household: NJ GIT withheld only where federal withholding applies. (US-NJS5-017, US-NJP51-001, US-NJS5-025)
- Agricultural: crew-leader rule. (US-NJS5-009, US-NJS5-008, US-NJS5-017)
- Minors: Birth date recorded. (US-NJS5-012, US-NJS5-022)
- Tipped: Tips are UI wages if reported in writing; service charges are remuneration. (US-NJS5-009, US-NJS5-008, US-NJS5-017)
- Clergy / religious: Church service exempt from NJ UI. No NJ GIT rule beyond federal (NJ-WT read; none found). (US-NJS5-017, US-NJP51-001)
- Students: Service by a student at their own school is exempt from UI. ESL and minimum wage apply (no student sub-minimum in NJ). (US-NJS5-017, US-NJS5-012)
- Nonresident aliens: No NJ-specific NRA withholding rule found in NJ-WT (contrast NC); Wages of aliens are UI-taxable under a valid SSN. (US-NJP51-001, US-NJS5-017)
- Statutory employees: No state rule beyond federal found; Home-to-home commission salespersons are exempt from UI. (US-NJS5-017)
- PA residents, military spouses: No NJ withholding with Form NJ-165 on file. (US-NJP51-001)
- Not configured in this release [[GAP:RQ-117]]: Thresholds, amounts or conditions for these populations are stated in the sources read without a confirmed value record and are not configured from this annex: Domestic / household; Agricultural; Minors; Tipped; Government employees; Long-term care direct care staff; Small/seasonal employers (< 6 employees); ---.

## NJ.16 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## NJ.S Sources

| Source | Authority |
|---|---|
| US-NJP51-001 | NJ Division of Taxation |
| US-NJP51-002 | NJ Division of Taxation |
| US-NJP51-004 | NJ Division of Taxation |
| US-NJP51-007 | NJ Dept of Labor and Workforce Development |
| US-NJP6-001 | City of Jersey City (Tax Collector) |
| US-NJP6-002 | City of Newark, Division of Tax Abatement and Special Taxes |
| US-NJP8-001 | NJ Department of Labor and Workforce Development, Wage and Hour (nj.gov/labor) |
| US-NJS5-001 | NJ Legislature (text as published by NJ DOL Wage and Hour Compliance, Selected NJ State Labor Laws) |
| US-NJS5-003 | NJ Legislature / NJ DOL (text as published by NJ DOL) |
| US-NJS5-004 | NJ Legislature / NJ DOL (text as published by NJ DOL) |
| US-NJS5-006 | NJ Division of Taxation |
| US-NJS5-007 | NJ Department of Labor and Workforce Development |
| US-NJS5-008 | NJ Department of Labor and Workforce Development |
| US-NJS5-009 | NJ Department of Labor and Workforce Development |
| US-NJS5-010 | NJ Department of Labor and Workforce Development, Division of Employer Accounts |
| US-NJS5-011 | NJ Department of Labor and Workforce Development |
| US-NJS5-012 | NJ Department of Labor and Workforce Development, Wage and Hour Compliance |
| US-NJS5-015 | NJ Department of Labor and Workforce Development, Division of Unemployment Insurance |
| US-NJS5-017 | NJ Department of Labor and Workforce Development, Division of Employer Accounts |
| US-NJS5-018 | NJ Department of Human Services, Division of Family Development (New Jersey Child Support Employer Services Portal) |
| US-NJS5-020 | NJ Department of Labor and Workforce Development (Rapid Response) |
| US-NJS5-021 | New Jersey Judiciary (Superior Court Clerk) |
| US-NJS5-022 | NJ Department of Labor and Workforce Development (text as published, Selected NJ State Labor Laws) |
| US-NJS5-023 | NJ Department of Labor and Workforce Development, Division of Employer Accounts |
| US-NJS5-024 | NJ Division of Taxation |
| US-NJS5-025 | NJ Department of Labor and Workforce Development |

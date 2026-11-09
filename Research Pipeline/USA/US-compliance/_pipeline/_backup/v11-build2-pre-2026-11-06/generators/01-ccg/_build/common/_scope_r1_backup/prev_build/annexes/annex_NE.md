# Annex NE: Nebraska


United States Country Configuration Guide, jurisdiction annex NE. Tax year 2026; currency USD (two decimal places).

**Scope of this annex.**

This annex holds the Nebraska layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in Annex FED, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register, with the authority and address listed in section NE.S (the source address is held in the register row). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

**Jurisdiction layer.**

| Item | Value |
|---|---|
| Annex tier | T3 (verified) |
| Basis | Circular EN 2026, W-4N [US-NEP51-001]; no local wage tax in the circular |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

**Configuration decisions.**

- The withholding rates of Circular EN ([[FACT:ne.pit.wh.rate.1=2.26]] to [[FACT:ne.pit.wh.rate.6=4.6]] percent) are not the statutory income-tax rates (top statutory rate [[FACT:ne.pit.statutory.top_rate=4.55]] percent in 2026). Configure withholding from Circular EN only; the statutory rates apply at assessment.
- Employers with more than [[FACT:ne.pit.min_withholding.employee_threshold=24]] employees must withhold at least [[FACT:ne.pit.min_withholding.rate=1.5]] percent of taxable wages.
- Paid sick time applies only to employers with at least [[FACT:ne.leave.paid_sick.coverage_min_employees=11]] employees.
- The 2027 minimum wage is not confirmed and is not configured [[GAP:RQ-089]] (see NE.1).

## NE.1 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ne.minwage.hourly` | [[FACT:ne.minwage.hourly=15.0]] USD | 2026-01-01 | 2026-12-31 | US-NES5-001 (A.1, Nebraska Legislature) | 48-1203(1)(e) |
| `ne.minwage.indexation` | [[FACT:ne.minwage.indexation=fixed +1.75% each 1 Jan from 2027-01-01 (LB258); NDOL publishes by 15 Oct]] | 2026-07-18 | 2026-12-31 | US-NES5-001 (A.1, Nebraska Legislature) | replaces Initiative 433 CPI indexation; no adult rounding rule in statute |
| `ne.labour.minwage.youth.hourly` | [[FACT:ne.labour.minwage.youth.hourly=13.5]] USD | 2026-07-18 | 2026-12-31 | US-NES5-001 (A.1, Nebraska Legislature) | ages 14-15 not emancipated; periodic statutory increase from 2030-01-01 |
| `ne.minwage.tipped.cash_wage` | [[FACT:ne.minwage.tipped.cash_wage=2.13]] USD | 2026-01-01 | 2026-12-31 | US-NES5-001 (A.1, Nebraska Legislature) | wages plus tips must reach minimum |
| `ne.labour.minwage.student_learner.min_ratio` | [[FACT:ne.labour.minwage.student_learner.min_ratio=75]] percent | 2026-01-01 | 2026-12-31 | US-NES5-001 (A.1, Nebraska Legislature) | of applicable minimum |
| `ne.labour.minwage.training.min_ratio_of_federal` | [[FACT:ne.labour.minwage.training.min_ratio_of_federal=75]] percent | 2007-01-01 | open | US-NES5-002 (A.1, Nebraska Legislature) | under 20, 90 days (+90 OJT); max one-fourth of hours paid |
| `ne.labour.wage_hour_act.coverage_min_employees` | [[FACT:ne.labour.wage_hour_act.coverage_min_employees=4]] | 1993-01-01 | open | US-NES5-003 (A.1, Nebraska Legislature) | excludes agriculture, private-home babysitters, EAP, government, family |
| `ne.labour.overtime.state_rule` | [[FACT:ne.labour.overtime.state_rule=none located (FLSA applies)]] | 1993-01-01 | open | US-NES5-003 (A.1, Nebraska Legislature) | full art. 12 index not read |
| `ne.pay_frequency.rule` | [[FACT:ne.pay_frequency.rule=regular paydays set by employer or agreement; no statutory minimum frequency; 30 days notice to change]] | 2014-01-01 | open | US-NES5-006 (A.1, Nebraska Legislature) | 48-1230(1) |
| `ne.labour.paycard.rules` | [[FACT:ne.labour.paycard.rules=1693k compulsory-use bar; one free withdrawal per pay period; no card fees to employee]] | 2014-01-01 | open | US-NES5-006 (A.1, Nebraska Legislature) | 48-1230(3) |

- Not configured in this release [[GAP:RQ-089]]: The 2027 adult minimum wage would be derived from the 2026 rate and the statutory step, but the statute has no rounding rule and the Department of Labor publication was not read. The 2027 rate is not written and must not be configured.
- Not configured in this release [[GAP:RQ-090]]: Absence of state overtime rule and of local minimum wages/preemption not verified against the full article.

## NE.2 Income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ne.wh.method` | [[FACT:ne.wh.method=Circular EN 2026 percentage method or wage-bracket tables; NE taxable wages = federal taxable wages]] | 2026-01-01 | 2026-12-31 | US-NES5-010 (A.2, Nebraska Department of Revenue) | - |
| `ne.wh.certificate` | [[FACT:ne.wh.certificate=W-4N; post-2019 federal W-4 without W-4N = single, zero allowances]] | 2026-01-01 | 2026-12-31 | US-NES5-010 (A.2, Nebraska Department of Revenue) | exempt status renewed by 15 Feb |
| `ne.pit.allowance.annual` | [[FACT:ne.pit.allowance.annual=2440]] USD | 2026-01-01 | 2026-12-31 | US-NES5-010 (A.2, Nebraska Department of Revenue) | weekly 46.92... monthly 203.33 |
| `ne.pit.wh.rate.1` | [[FACT:ne.pit.wh.rate.1=2.26]] percent | 2026-01-01 | 2026-12-31 | US-NES5-010 (A.2, Nebraska Department of Revenue) | withholding-table rates (DOR-designed) - not the statutory rates |
| `ne.pit.wh.rate.2` | [[FACT:ne.pit.wh.rate.2=3.22]] percent | 2026-01-01 | 2026-12-31 | US-NES5-010 (A.2, Nebraska Department of Revenue) | - |
| `ne.pit.wh.rate.3` | [[FACT:ne.pit.wh.rate.3=4.21]] percent | 2026-01-01 | 2026-12-31 | US-NES5-010 (A.2, Nebraska Department of Revenue) | - |
| `ne.pit.wh.rate.4` | [[FACT:ne.pit.wh.rate.4=4.35]] percent | 2026-01-01 | 2026-12-31 | US-NES5-010 (A.2, Nebraska Department of Revenue) | - |
| `ne.pit.wh.rate.5` | [[FACT:ne.pit.wh.rate.5=4.48]] percent | 2026-01-01 | 2026-12-31 | US-NES5-010 (A.2, Nebraska Department of Revenue) | - |
| `ne.pit.wh.rate.6` | [[FACT:ne.pit.wh.rate.6=4.6]] percent | 2026-01-01 | 2026-12-31 | US-NES5-010 (A.2, Nebraska Department of Revenue) | - |
| `ne.pit.wh.single.thresholds` | [[FACT:ne.pit.wh.single.thresholds=3430;6710;21810;31610;40130;75370]] | 2026-01-01 | 2026-12-31 | US-NES5-010 (A.2, Nebraska Department of Revenue) | annual; cumulative 74.13/560.35/972.93/1,343.55/2,922.30 reproduced |
| `ne.pit.wh.married.thresholds` | [[FACT:ne.pit.wh.married.thresholds=8190;13010;32400;50400;62530;82920]] | 2026-01-01 | 2026-12-31 | US-NES5-010 (A.2, Nebraska Department of Revenue) | cumulative 108.93/733.29/1,491.09/2,018.75 (DOR half-up of 2,018.745)/2,932.22 |
| `ne.pit.statutory.top_rate` | [[FACT:ne.pit.statutory.top_rate=4.55]] percent | 2026-01-01 | 2026-12-31 | US-NES5-018 (A.1, Nebraska Legislature) | assessment level; lower brackets 2.46/3.51 |
| `ne.pit.statutory.top_rate` | [[FACT:ne.pit.statutory.top_rate=3.99]] percent | 2027-01-01 | open | US-NES5-018 (A.1, Nebraska Legislature) | LB754 enacted; assessment level; 2027 withholding tables not read |
| `ne.pit.min_withholding.rate` | [[FACT:ne.pit.min_withholding.rate=1.5]] percent | 2026-01-01 | 2026-12-31 | US-NES5-010 (A.2, Nebraska Department of Revenue) | employers with more than 24 employees, unless lower liability documented |
| `ne.pit.min_withholding.employee_threshold` | [[FACT:ne.pit.min_withholding.employee_threshold=24]] | 2026-01-01 | 2026-12-31 | US-NES5-010 (A.2, Nebraska Department of Revenue) | more than 24 |
| `ne.wh.supplemental.rate` | [[FACT:ne.wh.supplemental.rate=3.5]] percent | 2026-01-01 | open | US-NEP51-001 (A.2, Nebraska Department of Revenue) | or aggregate |

- Not configured in this release [[GAP:RQ-091]]: The 2027 edition of Circular EN was not obtained.

## NE.2b Non-resident regime and reciprocity

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ne.reciprocity.states` | [[FACT:ne.reciprocity.states=none]] | 2025-01-01 | open | US-NEP51-002 (A.2, Nebraska Department of Revenue) | - |
| `ne.pit.nonresident.duty_days` | [[FACT:ne.pit.nonresident.duty_days=7]] days | 2025-01-01 | open | US-NEP51-002 (A.2, Nebraska Department of Revenue) | LB1023; conference rule 7 days and <=5,000; convenience rule 77-2733(8)(c) |

## NE.2c Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ne.local_wage_tax.exists` | [[FACT:ne.local_wage_tax.exists=False]] | 2026-01-01 | open | US-NEP51-001 (A.2, Nebraska Department of Revenue) | occupation taxes are local business taxes only |

## NE.3 Social insurance: unemployment, disability, paid leave and payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ne.sui.employee.rate` | [[FACT:ne.sui.employee.rate=0]] percent | 2025-09-11 | open | US-NER3C-001 (A.1, Nebraska Legislature) | Neb. Rev. Stat. 48-648(1): the combined UI tax shall not be deducted, in whole or in part, from employees' wages. |
| `ne.sui.wage_base.other_state_credit` | [[FACT:ne.sui.wage_base.other_state_credit=True]] | 2025-09-11 | open | US-NES5-011 (A.3, Nebraska Department of Labor) | 48-648.02. |
| `ne.sui.wages.401k_included` | [[FACT:ne.sui.wages.401k_included=True]] | 2025-09-11 | open | US-NES5-019 (A.3, Nebraska Department of Labor) | NAC 220 ch.2. |
| `ne.sui.wage_base` | [[FACT:ne.sui.wage_base=9000]] USD | 2026-01-01 | 2026-12-31 | US-NEP51-003 (A.2, Nebraska Department of Labor) | categories 1-19; other-state wages count (48-648.02) |
| `ne.ui.wage_base.category20` | [[FACT:ne.ui.wage_base.category20=24000]] USD | 2026-01-01 | 2026-12-31 | US-NEP51-003 (A.2, Nebraska Department of Labor) | category 20 at [[FACT:ne.sui.employer.rate.max=5.40]]% |
| `ne.sui.new_employer.rate` | [[FACT:ne.sui.new_employer.rate=1.25]] percent | 2026-01-01 | 2026-12-31 | US-NEP51-003 (A.2, Nebraska Department of Labor) | construction 5.40 |
| `ne.ui.rate.new_employer.construction` | [[FACT:ne.ui.rate.new_employer.construction=5.4]] percent | 2026-01-01 | 2026-12-31 | US-NEP51-003 (A.2, Nebraska Department of Labor) | - |
| `ne.sui.employer.rate.max` | [[FACT:ne.sui.employer.rate.max=5.4]] percent | 2026-01-01 | 2026-12-31 | US-NEP51-003 (A.2, Nebraska Department of Labor) | range 0.00-5.40; average 0.55 |
| `ne.sdi_pfml.exists` | [[FACT:ne.sdi_pfml.exists=False]] | 2026-01-01 | open | US-NEP52-001 (A.2, Nebraska Department of Revenue) | no SDI/TDI/PFML/transit/workforce levy |

## NE.4 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ne.payslip.items` | [[FACT:ne.payslip.items=employer identity, hours paid, wages earned, deductions each regular payday]] | 2026-01-01 | open | US-NEP51-004 (A.1, Nebraska Legislature; Nebraska Department of Revenue) | 48-1230(2); hours not required for exempt employees; mail, electronic or at workplace. |

## NE.5 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ne.report.941n.due` | [[FACT:ne.report.941n.due=Apr 30; Jul 31; Oct 31; Jan 31]] | 2026-01-01 | 2026-12-31 | US-NES5-010 (A.2, Nebraska Department of Revenue) | 501N deposit by 15th when >500 withheld in month 1 or 2; EFT if prior-year >5,000 |
| `ne.report.w3n.due` | [[FACT:ne.report.w3n.due=31 January]] | 2025-11-01 | open | US-NES5-017 (A.2, Nebraska Department of Revenue) | >50 forms e-file via NebFile; EFW2 with NE RS (state code 31) and RV |
| `ne.report.w2.efile_threshold` | [[FACT:ne.report.w2.efile_threshold=50]] | 2025-11-01 | open | US-NES5-017 (A.2, Nebraska Department of Revenue) | more than 50 |
| `ne.report.ui.quarterly_due` | [[FACT:ne.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] | 2025-09-11 | open | US-NES5-011 (A.3, Nebraska Department of Labor) | A late-report charge applies (a percentage of gross wages with a minimum and a maximum); its amounts are not configured in this release. |
| `ne.newhire.report_days` | [[FACT:ne.newhire.report_days=20]] days | 2004-01-01 | open | US-NES5-014 (A.1, Nebraska Legislature) | - |

- Not configured in this release [[GAP:RQ-092]]: Withholding registration form name and the NEworks FTP wage-file spec not read.

## NE.6 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ne.leave.paid_sick.coverage_min_employees` | [[FACT:ne.leave.paid_sick.coverage_min_employees=11]] | 2025-09-03 | open | US-NES5-009 (A.1, Nebraska Legislature) | LB415; small business 11-19; excludes <80 h/yr in NE, under 16, seasonal ag, government |
| `ne.leave.paid_sick.accrual_ratio_hours_worked` | [[FACT:ne.leave.paid_sick.accrual_ratio_hours_worked=30]] hours | 2025-10-01 | open | US-NES5-007 (A.1, Nebraska Legislature) | after 80 consecutive hours |
| `ne.leave.paid_sick.annual_cap.small_hours` | [[FACT:ne.leave.paid_sick.annual_cap.small_hours=40]] hours | 2025-10-01 | open | US-NES5-007 (A.1, Nebraska Legislature) | 11-19 employees |
| `ne.leave.paid_sick.annual_cap.other_hours` | [[FACT:ne.leave.paid_sick.annual_cap.other_hours=56]] hours | 2025-10-01 | open | US-NES5-007 (A.1, Nebraska Legislature) | - |
| `ne.leave.sick.payout_on_separation` | [[FACT:ne.leave.sick.payout_on_separation=False]] | 2025-10-01 | open | US-NES5-007 (A.1, Nebraska Legislature) | 48-3803(10) |

- Not configured in this release [[GAP:RQ-093]]: Jury-duty and voting-leave pay rules and child-labour hours not read.

## NE.7 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ne.final_pay.rule` | [[FACT:ne.final_pay.rule=next regular payday or within two weeks, whichever sooner]] | 2014-01-01 | open | US-NES5-006 (A.1, Nebraska Legislature) | 48-1230(4)(a) |
| `ne.term.vacation.payout` | [[FACT:ne.term.vacation.payout=True]] | 2026-01-01 | open | US-NES5-004 (A.1, Nebraska Legislature) | earned unused vacation is wages (48-1229(6)) |

## NE.8 Benefits in kind and taxable wages

No Nebraska rule is configured in this domain; the federal treatment in Annex FED applies.

## NE.9 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ne.garn.creditor.max_percent` | [[FACT:ne.garn.creditor.max_percent=25]] percent | 2001-01-01 | open | US-NES5-012 (A.1, Nebraska Legislature) | or excess over 30x FMW; head of family 15% |
| `ne.garn.consumer.head_of_family.max_rate` | [[FACT:ne.garn.consumer.head_of_family.max_rate=15]] percent | 2001-01-01 | open | US-NES5-012 (A.1, Nebraska Legislature) | - |

- Not configured in this release [[GAP:RQ-094]]: The child-support employer fee, priority and maximum (Neb. Rev. Stat. 43-1720 to 43-1724) were not read.

## NE.10 Collective agreements and prevailing wage

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ne.prevailing_wage.exists` | [[FACT:ne.prevailing_wage.exists=False]] | 2026-01-01 | open | US-NEP52-002 (A.1, Nebraska Legislature) | ch. 73 fair-labour-standards statement only |

## NE.11 Indexation

Indexation of each value is stated in the note of the value concerned.

## NE.12 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ne.data.ssn.max_digits_displayed` | [[FACT:ne.data.ssn.max_digits_displayed=4]] | 2026-01-01 | open | US-NES5-013 (A.1, Nebraska Legislature) | 48-237 |

- Not configured in this release [[GAP:RQ-095]]: NE payroll-record retention period (UI and wage-hour) not read.

## NE.13 Live legal change

No Nebraska rule is configured in this domain; the federal treatment in Annex FED applies.

## NE.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## NE.15 Special populations

- Domestic/household: Baby-sitters in private homes are outside the Wage and Hour Act (FLSA governs). (US-NES5-011, US-NES5-003, US-NES5-009)
- Agricultural: Outside the Wage and Hour Act (federal FLSA only). (US-NES5-003, US-NES5-011, US-NES5-009)
- Clergy/religious: UI-exempt (ministers, church service); Withholding follows federal taxable wages. (US-NES5-019, US-NEP51-001)
- Students: Students working for their school, and academic-credit work, are UI-exempt. (US-NES5-001, US-NES5-019)
- Nonresident aliens: Wages follow federal taxable wages; Treaty-exempt NRA personal-services payments: no NE withholding with a statement. (US-NES5-010)
- Statutory employees: No state rule beyond federal (Circular EN read). (US-NEP51-001)
- Government employees: Outside the Wage and Hour Act and the paid-sick-time Act; Separate final-pay timing for political subdivisions; UI reimbursable option. (US-NES5-003, US-NES5-009, US-NES5-006, US-NES5-011)
- Commission-only real-estate/insurance agents: UI-exempt. (US-NES5-019)
- Not configured in this release [[GAP:RQ-096]]: Thresholds, amounts or conditions for these populations are stated in the sources read without a confirmed value record and are not configured from this annex: Domestic/household; Agricultural; Minors; Tipped; Students.

## NE.16 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## NE.S Sources

| Source | Authority |
|---|---|
| US-NEP51-001 | Nebraska Department of Revenue |
| US-NEP51-002 | Nebraska Department of Revenue |
| US-NEP51-003 | Nebraska Department of Labor |
| US-NEP51-004 | Nebraska Legislature; Nebraska Department of Revenue |
| US-NEP52-001 | Nebraska Department of Revenue |
| US-NEP52-002 | Nebraska Legislature |
| US-NER3C-001 | Nebraska Legislature |
| US-NES5-001 | Nebraska Legislature |
| US-NES5-002 | Nebraska Legislature |
| US-NES5-003 | Nebraska Legislature |
| US-NES5-004 | Nebraska Legislature |
| US-NES5-006 | Nebraska Legislature |
| US-NES5-007 | Nebraska Legislature |
| US-NES5-009 | Nebraska Legislature |
| US-NES5-010 | Nebraska Department of Revenue |
| US-NES5-011 | Nebraska Department of Labor |
| US-NES5-012 | Nebraska Legislature |
| US-NES5-013 | Nebraska Legislature |
| US-NES5-014 | Nebraska Legislature |
| US-NES5-017 | Nebraska Department of Revenue |
| US-NES5-018 | Nebraska Legislature |
| US-NES5-019 | Nebraska Department of Labor |

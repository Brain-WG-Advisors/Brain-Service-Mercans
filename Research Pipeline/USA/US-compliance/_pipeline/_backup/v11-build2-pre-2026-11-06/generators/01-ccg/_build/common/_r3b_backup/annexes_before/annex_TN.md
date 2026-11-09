# Annex TN: Tennessee


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T1 - no state wage tax; SUI and levies only** (build manifest, tier rationale).

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## TN.1 Employment and labour code

- **Minimum wage:** no state minimum-wage law (exists: [[FACT:tn.labour.minwage.state.exists=False]]); FLSA-covered employers pay the federal rate (Annex FED) [US-TNS5-011]. Local minimum wages are reported as preempted (T.C.A. 7-51-1802) on secondary sources only; not modelled as a rule.
- **Overtime:** [[FACT:tn.labour.overtime.state_rule=none (FLSA only)]] [US-TNS5-001].
- **Pay frequency and timing (T.C.A. 50-2-103(a)) [US-TNS5-001]:** [[FACT:tn.pay_frequency.rule=employers with 5+ employees: regular paydays at least monthly]], with statutory due dates for wages earned in the first and second half of the month. Piece-work and commission timing from 2026-07-01 (PC 617): open point below.
- **Meal break (50-2-103(h)):** [[FACT:tn.labour.meal_break.minutes=30]] minutes unpaid for a scheduled run of consecutive hours, unless the business gives ample chance to rest [US-TNS5-001].
- **Minors [US-TNB5-002]:** hours: [[FACT:tn.labour.child_labour.hours=Ages 14-15: school in session max 3 h/day and 18 h/week, 7am-7pm; not in session max 8 h/day and 40 h/week, 6am-9pm. Ages 16-17: not during required class hours; not 10pm-6am Sun-Thu before a school day (until midnight max 3 nights/week with a Parental Consent Form, T.C.A. 50-5-105). Stricter of state or federal rule applies.]] Unpaid break of [[FACT:tn.labour.child_labour.break_minutes=30]] minutes for minors on the statutory schedule (50-5-115); no waiver.
- **Method of payment:** not read (open point below).

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tn.labour.minwage.state.exists` | [[FACT:tn.labour.minwage.state.exists=False]] |  | from 2026-01-01 | US-TNS5-011 |  |
| `tn.labour.overtime.state_rule` | [[FACT:tn.labour.overtime.state_rule=none (FLSA only)]] |  | from 2026-01-01 | US-TNS5-001 |  |
| `tn.pay_frequency.rule` | [[FACT:tn.pay_frequency.rule=employers with 5+ employees: regular paydays at least monthly]] |  | from 2026-01-01 | US-TNS5-001 | monthly payers by 5th of next month; 2+ periods: by 20th / 5th |
| `tn.labour.meal_break.minutes` | [[FACT:tn.labour.meal_break.minutes=30]] | minutes | from 2026-01-01 | US-TNS5-001 | unpaid; scheduled 6 consecutive hours |
| `tn.labour.child_labour.hours` | [[FACT:tn.labour.child_labour.hours=Ages 14-15: school in session max 3 h/day and 18 h/week, 7am-7pm; not in session max 8 h/day and 40 h/week, 6am-9pm. Ages 16-17: not during required class hours; not 10pm-6am Sun-Thu before a school day (until midnight max 3 nights/week with a Parental Consent Form, T.C.A. 50-5-105). Stricter of state or federal rule applies.]] |  | from 2026-01-01 | US-TNB5-002 |  |
| `tn.labour.child_labour.break_minutes` | [[FACT:tn.labour.child_labour.break_minutes=30]] | minutes | from 2026-01-01 | US-TNB5-002 | Unpaid break if scheduled 6 consecutive hours, not in or before the first hour (T.C.A. 50-5-115); no waiver under 18. |

**Open research points**

- Not configured in this release [[GAP:RQ-328]]: Direct deposit / paycard consent rule not read (Lexis-only T.C.A.).

## TN.2 Income tax withholding

- **No state tax on wages and no withholding** (income tax exists: [[FACT:tn.pit.exists=False]]); the Hall tax on interest and dividends was repealed from 2021-01-01; no state W-4, supplemental rate or state W-2 [US-TN-001, US-TNP51-001].
- **No local wage tax** (exists: [[FACT:tn.local_wage_tax.exists=False]]) [US-TNP52-001].
- **Resident and nonresident matrix.** Nothing is withheld for Tennessee for any income type; a Tennessee resident working in a wage-taxing state is withheld for that state (Annex MULTI).

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tn.pit.exists` | [[FACT:tn.pit.exists=False]] |  | from 2021-01-01 | US-TN-001 | Hall tax repealed 2021-01-01; no withholding, W-4, W-2 filing |
| `tn.local_wage_tax.exists` | [[FACT:tn.local_wage_tax.exists=False]] |  | from 2026-01-01 | US-TNP52-001 |  |

## TN.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in TN.2.

## TN.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in TN.2.

## TN.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Unemployment insurance (DLWD) [US-TNS5-002, US-TNS5-003, US-TNS5-004].** Taxable wage base [[FACT:tn.sui.wage_base=7000]] USD (set by the Trust Fund level, not by an index). Rate table in force: [[FACT:tn.ui.rate_table.in_effect=Premium Rate Table 6]] (the Trust Fund balance on June 30 and December 31 decides the table for the next six months, T.C.A. 50-7-403). Range [[FACT:tn.sui.employer.rate.min=0.01]] % to [[FACT:tn.sui.employer.rate.max=10]] %. New employer [[FACT:tn.sui.new_employer.rate=2.7]] % (manufacturing sectors use a sector rate); experience rating after the statutory qualifying period. Employee contribution [[FACT:tn.sui.employee.rate=0]] % [US-TNR3-003].
- **Liability thresholds** (FUTA-liable employers, quarterly wage and 20-week tests, domestic, agricultural, nonprofit and government rules) and PEO reporting per client: US-TNS5-013.
- **No SDI, TDI, PFML, LTC, transit or workforce levy** (exists: [[FACT:tn.sdi_pfml.exists=False]]) [US-TNR3-003, US-TNP52-001].
- **Workers' compensation (benefit side, not payroll) [US-TNB5-001]:** for injuries from 2026-07-01 to 2027-06-30, maximum weekly temporary total disability benefit [[FACT:tn.wc.benefit.ttd.weekly_max=1,488.30]] USD, maximum weekly permanent partial disability benefit [[FACT:tn.wc.benefit.ppd.weekly_max=1,353.00]] USD, minimum weekly benefit [[FACT:tn.wc.benefit.weekly_min=202.95]] USD. These are insurer benefits, not payroll deductions.

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tn.sui.wage_base` | [[FACT:tn.sui.wage_base=7000]] | USD | 2018-01-01 to 2026-12-31 | US-TNS5-002 | set by Trust Fund level (8,000 2016-17; 9,000 2014-15) |
| `tn.ui.rate_table.in_effect` | [[FACT:tn.ui.rate_table.in_effect=Premium Rate Table 6]] |  | 2026-01-01 to 2026-12-31 | US-TNS5-002 | both half-years 2026; in force since 2015-07-01 |
| `tn.sui.employer.rate.min` | [[FACT:tn.sui.employer.rate.min=0.01]] | % | 2026-01-01 to 2026-12-31 | US-TNS5-003 | Table 6; reserve ratio 20.0+ |
| `tn.sui.employer.rate.max` | [[FACT:tn.sui.employer.rate.max=10]] | % | 2026-01-01 to 2026-12-31 | US-TNS5-003 | negative reserve ratios 5.00-10.00 |
| `tn.sui.new_employer.rate` | [[FACT:tn.sui.new_employer.rate=2.7]] | % | from 2026-01-01 | US-TNS5-004 | manufacturing NAICS 31-33 sector rate; experience-rated after 36 months |
| `tn.sui.employee.rate` | [[FACT:tn.sui.employee.rate=0]] | % | from 2026-01-01 | US-TNR3-003 |  |
| `tn.sdi_pfml.exists` | [[FACT:tn.sdi_pfml.exists=False]] |  | from 2026-01-01 | US-TNR3-003 | no SDI/PFML/transit levy |
| `tn.wc.benefit.ttd.weekly_max` | [[FACT:tn.wc.benefit.ttd.weekly_max=1,488.30]] | USD | 2026-07-01 to 2027-06-30 | US-TNB5-001 | 110% of SAWW; injuries in the period. |
| `tn.wc.benefit.ppd.weekly_max` | [[FACT:tn.wc.benefit.ppd.weekly_max=1,353.00]] | USD | 2026-07-01 to 2027-06-30 | US-TNB5-001 | 100% of SAWW. |
| `tn.wc.benefit.weekly_min` | [[FACT:tn.wc.benefit.weekly_min=202.95]] | USD | 2026-07-01 to 2027-06-30 | US-TNB5-001 |  |

**Open research points**

- Not configured in this release [[GAP:RQ-332]]: The SUI wage exclusions (cafeteria plans, retirement deferrals, tips, students, clergy, corporate officers) were not read.

## TN.4 Pay statement

- **No itemised pay-statement statute** (exists: [[FACT:tn.payslip.statute.exists=False]]) [US-TNP51-003, US-TNS5-001]; federal recordkeeping applies. Retention beyond UI records: open point below.

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tn.payslip.statute.exists` | [[FACT:tn.payslip.statute.exists=False]] |  | from 2026-01-01 | US-TNS5-001 | absence via DLWD index; T.C.A. text not read |

**Open research points**

- Not configured in this release [[GAP:RQ-331]]: State payroll record retention not located.

## TN.5 Statutory reporting

- **No state withholding return or state W-2.**
- **Quarterly UI report [US-TNS5-005, US-TNS5-007, US-TNS5-014]:** Wage Report LB-0851 and Premium Report LB-0456, due [[FACT:tn.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]]; filed in Employer e-Services (manual entry, abbreviated ICESA, short text file or full ICESA).
- **New hire [US-TNS5-008, US-TNS5-009]:** within [[FACT:tn.newhire.report_days=20]] days of hire, to TN DHS (not the UI system).
- **Registration and TPA access:** Employer e-Services; no POA needed since 2025-05-27 [US-TNS5-005, US-TNR3-002].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tn.report.ui.quarterly_due` | [[FACT:tn.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] |  | from 2025-05-27 | US-TNS5-005 | LB-0851 + LB-0456 in Employer e-Services; ICESA or 58-char text |
| `tn.newhire.report_days` | [[FACT:tn.newhire.report_days=20]] | days | from 2026-01-01 | US-TNS5-008 | TN DHS |

## TN.6 Leave

- **No mandatory paid sick leave, vacation or PFML** (sick leave statute exists: [[FACT:tn.leave.sick.state_statute.exists=False]]) [US-TNS5-001].
- **Jury duty (T.C.A. 22-4-108):** the employer pays wages during jury service less the court's pay (paid: [[FACT:tn.leave.jury_duty.paid=True]]) [US-TNS5-012].
- **Voting and parental leave:** protected; the pay rules rest on leads only (open point below) [US-TNS5-012]. Military leave protected (8-33-101 ff.).

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tn.leave.sick.state_statute.exists` | [[FACT:tn.leave.sick.state_statute.exists=False]] |  | from 2026-01-01 | US-TNS5-001 | policy-based |
| `tn.leave.jury_duty.paid` | [[FACT:tn.leave.jury_duty.paid=True]] |  | from 2026-01-01 | US-TNS5-012 | wages less court pay (22-4-108) |

**Open research points**

- Not configured in this release [[GAP:RQ-335]]: Not established from an official source.

## TN.7 Termination and final pay

- **Final pay (50-2-103(g)) [US-TNS5-001]:** [[FACT:tn.final_pay.rule=later of next regular payday or 21 days after separation]], for discharge and resignation alike.
- **Accrued vacation:** [[FACT:tn.term.vacation.payout=only if policy or labour agreement requires]] (50-2-103(a)(3)).
- **Separation Notice LB-0489 [US-TNS5-007]:** handed or mailed to the employee within [[FACT:tn.term.separation_notice.hours=24]] hours of separation (Rule 0800-09-01-.02), except very short employment or a short recall. The form reports severance pay, wages in lieu of notice and vacation pay on temporary layoff, so payroll must supply those amounts.
- **Tennessee WARN:** notice duty at [[FACT:tn.term.warn.employee_threshold=50]] or more full-time employees [US-TNS5-006]. IWO terminations reported to the child-support office [US-TNS5-009].

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tn.final_pay.rule` | [[FACT:tn.final_pay.rule=later of next regular payday or 21 days after separation]] |  | from 2026-01-01 | US-TNS5-001 | 50-2-103(g); discharge and resignation |
| `tn.term.vacation.payout` | [[FACT:tn.term.vacation.payout=only if policy or labour agreement requires]] |  | from 2026-01-01 | US-TNS5-001 |  |
| `tn.term.separation_notice.hours` | [[FACT:tn.term.separation_notice.hours=24]] | hours | from 2026-01-01 | US-TNS5-007 | LB-0489 handed/mailed within 24 h; reports severance, wages in lieu, vacation pay |
| `tn.term.warn.employee_threshold` | [[FACT:tn.term.warn.employee_threshold=50]] |  | from 2026-01-01 | US-TNS5-006 | TN WARN notice only (A.3) |

## TN.8 Benefits in kind and taxable wages

- **Income tax:** not applicable (no state wage tax). UI wage exclusions not read (open point below) [US-TNP51-001].

## TN.9 Deductions and garnishments

- **Wage deductions (50-2-110(a)(2)):** an offset for amounts the employee owes needs a prior signed written agreement [US-TNS5-001].
- **Ordinary garnishment (T.C.A. 26-2-404(b)) [US-TNS5-010]:** withhold the lesser of [[FACT:tn.garn.creditor.max_percent=25]] % of disposable earnings or disposable earnings above thirty times the federal minimum wage per week (CCPA, Annex FED); then subtract [[FACT:tn.garn.consumer.child_reduction.weekly=2.50]] USD per week for each dependent child under 16 living in Tennessee (prorated for longer pay periods). Tennessee departs from the CCPA through this child reduction.
- **Child support and alimony:** CCPA support percentages or the ordered amount if lower [US-TNS5-010]. **IWO:** remit to the Tennessee SDU within [[FACT:tn.garn.iwo.remit_days=7]] days of payday; report lump sums [US-TNS5-009]. Fee and priority: open point below.

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tn.garn.creditor.max_percent` | [[FACT:tn.garn.creditor.max_percent=25]] | % | from 2026-01-01 | US-TNS5-010 | or disposable - 30x FMW; then minus 2.50/week per dependent child under 16 in TN |
| `tn.garn.consumer.child_reduction.weekly` | [[FACT:tn.garn.consumer.child_reduction.weekly=2.50]] | USD | from 2026-01-01 | US-TNS5-010 | biweekly 5.00; semimonthly 5.42; monthly 10.83 |
| `tn.garn.iwo.remit_days` | [[FACT:tn.garn.iwo.remit_days=7]] | days | from 2026-01-01 | US-TNS5-009 | A.3 |

**Open research points**

- Not configured in this release [[GAP:RQ-330]]: IWO employer fee and priority not located on A source.

## TN.10 Collective agreements and prevailing wage

- **Prevailing Wage Act (T.C.A. 12-4-401 ff.) [US-TNP51-002]:** scope [[FACT:tn.prevailing_wage.scope=state-funded highway construction only]]; 2026 craft rates, for example unskilled laborer [[FACT:tn.prevailing_wage.unskilled_laborer.hourly=23.52]] USD per hour. Certified payroll format: open point below.

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tn.prevailing_wage.scope` | [[FACT:tn.prevailing_wage.scope=state-funded highway construction only]] |  | from 2026-01-01 | US-TNP51-002 |  |
| `tn.prevailing_wage.unskilled_laborer.hourly` | [[FACT:tn.prevailing_wage.unskilled_laborer.hourly=23.52]] | USD | from 2026-01-01 | US-TNP51-002 |  |

**Open research points**

- Not configured in this release [[GAP:RQ-333]]: State highway certified payroll format not read.

## TN.11 Indexation

- **SUI wage base and rate table:** set by the Trust Fund level, reset every six months [US-TNS5-002]. No minimum wage to index; prevailing highway rates re-surveyed yearly [US-TNP51-002].

## TN.12 Payroll data protection and records

- No SSN-truncation rule for pay statements located on an A-tier source; SSN display rules and the employee-data scope of the Tennessee Information Protection Act are open (below).

**Open research points**

- Not configured in this release [[GAP:RQ-334]]: SSN display (47-18-2110) and TIPA employee-data exclusion not verified.

## TN.13 Live legal change

- **2026-07-01:** PC 617 piece-work and commission timing (not configured in this release; see the open point below). Workers' compensation acts of 2026: [[FACT:tn.live.bwc_2026=2026 workers' compensation acts (PC 705, 845, 950, 789, 721, 600, 942) change claims, administration and drug-testing rules only; no employer payroll withholding or contribution change]] [US-TNB5-001].
- **2025-05-27:** UI tax system moved to Employer e-Services [US-TNS5-005, US-TNR3-002].
- **2026 SUI:** no change [US-TNS5-002]. No 2027 enactment located (sweep incomplete).

**Parameters (live legal change)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `tn.live.bwc_2026` | [[FACT:tn.live.bwc_2026=2026 workers' compensation acts (PC 705, 845, 950, 789, 721, 600, 942) change claims, administration and drug-testing rules only; no employer payroll withholding or contribution change]] |  | from 2026-07-01 | US-TNB5-001 |  |

**Open research points**

- Not configured in this release [[GAP:RQ-329]]: Not established from an official source.

## TN.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## TN.15 Special populations

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

## TN.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## TN.S Sources

Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file. Authorities:

- Davidson County Circuit Court Clerk (Nashville): US-TNS5-010
- Tennessee Department of Human Services: US-TNS5-009
- Tennessee Department of Labor and Workforce Development: US-TNS5-001, US-TNS5-002, US-TNS5-003, US-TNS5-004, US-TNS5-005, US-TNS5-006, US-TNS5-007, US-TNS5-008, US-TNS5-012
- Tennessee Department of Labor and Workforce Development, Bureau of Workers' Compensation: US-TNB5-001
- Tennessee Department of Labor and Workforce Development, Labor Standards Unit: US-TNB5-002
- Tennessee Department of Revenue: US-TN-001, US-TNP52-001
- Tennessee Dept of Labor and Workforce Development: US-TNP51-002, US-TNR3-003
- U.S. Department of Labor Wage and Hour Division: US-TNS5-011

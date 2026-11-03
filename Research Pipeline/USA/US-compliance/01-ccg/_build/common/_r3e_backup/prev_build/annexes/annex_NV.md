# Annex NV: Nevada


United States Country Configuration Guide, jurisdiction annex NV. Tax year 2026; currency USD (two decimal places).

**Scope of this annex.**

This annex holds the Nevada layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in Annex FED, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register, with the authority and address listed in section NV.S (the source address is held in the register row). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

**Jurisdiction layer.**

| Item | Value |
|---|---|
| Annex tier | T1 (verified) |
| Basis | No state income tax on individuals (salaries/wages), Dept of Taxation page [US-NV-001] |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

**Configuration decisions.**

- Nevada has no wage tax ([[FACT:nv.pit.exists=False]], tier T1). The Modified Business Tax is an employer tax of [[FACT:nv.mbt.general.rate=1.17]] percent on unemployment-insurance wages above [[FACT:nv.mbt.general.quarterly_threshold=50000]] USD a quarter; the wages on the tax return must equal the gross wages reported for unemployment insurance in the same quarter.
- Daily overtime after [[FACT:nv.overtime.daily_threshold_hours=8]] hours applies only to employees paid less than [[FACT:nv.overtime.daily_threshold_wage=18.0]] USD an hour (period from 2026-07-01).
- The 2027 unemployment wage base [[FACT:nv.sui.wage_base=45400]] USD is derived from the agency's published average wage by the statutory rule; confirm it against the 2027 rate notice before use.
- There is no tip credit ([[FACT:nv.minwage.tip_credit.allowed=False]]); do not model the two-tier minimum wage of the statute, which the state constitution overrides.

## NV.1 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nv.minwage.hourly` | [[FACT:nv.minwage.hourly=12.0]] USD | 2024-07-01 | open | US-NVS5-013 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | Const. art. 15 s. 16(1); single tier; no indexation; NRS 608.250 two-tier text overridden (do not model) |
| `nv.minwage.tip_credit.allowed` | [[FACT:nv.minwage.tip_credit.allowed=False]] | 2024-07-01 | open | US-NVS5-013 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | - |
| `nv.overtime.daily_threshold_hours` | [[FACT:nv.overtime.daily_threshold_hours=8]] hours | 2025-10-01 | open | US-NVS5-001 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | daily OT only for employees earning < 1.5x minimum; 4x10 by agreement excepted |
| `nv.overtime.daily_threshold_wage` | [[FACT:nv.overtime.daily_threshold_wage=18.0]] USD | 2026-07-01 | 2027-06-30 | US-NVS5-003 (A.2, Nevada Office of the Labor Commissioner) | 12.00 x 1.5 |
| `nv.overtime.weekly_threshold_hours` | [[FACT:nv.overtime.weekly_threshold_hours=40]] hours | 2025-10-01 | open | US-NVS5-001 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | - |
| `nv.overtime.premium.multiplier` | [[FACT:nv.overtime.premium.multiplier=1.5]] ratio | 2025-10-01 | open | US-NVS5-001 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | - |
| `nv.pay_frequency.rule` | [[FACT:nv.pay_frequency.rule=at least semimonthly (by 15th / last day of month)]] | 2025-10-01 | open | US-NVS5-001 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | 608.060; monthly for exempt staff of out-of-state payroll employers |
| `nv.payment.method` | [[FACT:nv.payment.method=cash or negotiable check unless employee agrees in writing to another disposition]] | 2025-10-01 | open | US-NVS5-001 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | 608.120 |
| `nv.labour.lodging_credit.weekly_multiple_of_minwage` | [[FACT:nv.labour.lodging_credit.weekly_multiple_of_minwage=5]] | 2025-10-01 | open | US-NVS5-001 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | meals max 100% of hourly minimum per day; by agreement |

- Not configured in this release [[GAP:RQ-129]]: Paycard rules beyond 608.120 written consent not read.

## NV.2 Income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nv.pit.exists` | [[FACT:nv.pit.exists=False]] | 2026-01-01 | open | US-NVS5-014 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | Const. art. 10 s. 1(9); no withholding, W-4, reconciliation or state W-2 |

Rules:

- No local income or wage tax. The constitutional bar covers all levels of government. (US-NVS5-014)

## NV.2b Non-resident regime and reciprocity

No Nevada rule is configured in this domain; the federal treatment in Annex FED applies.

## NV.2c Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nv.local_wage_tax.exists` | [[FACT:nv.local_wage_tax.exists=False]] | 2026-01-01 | open | US-NVS5-014 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | constitutional bar covers all levels |

## NV.3 Social insurance: unemployment, disability, paid leave and payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nv.sui.wage_base` | [[FACT:nv.sui.wage_base=43700]] USD | 2026-01-01 | 2026-12-31 | US-NVP51-001 (A.2, NV Dept of Employment, Training and Rehabilitation) | 66 2/3% of prior-year average annual wage (612.545) |
| `nv.sui.wage_base` | [[FACT:nv.sui.wage_base=45400]] USD | 2027-01-01 | 2027-12-31 | US-NVS5-019 (A.2, Nevada DETR (Research & Analysis Bureau, for the Employment Security Division)) | derived: 93,841,589,718 / 1,377,412 = 68,128.92 (DETR R&A memo 2026-06-01) x 2/3 = 45,419.28 -> [[FACT:nv.sui.wage_base=45,400]]; DETR 2027 rate notice not yet read |
| `nv.sui.new_employer.rate` | [[FACT:nv.sui.new_employer.rate=2.95]] percent | 2026-01-01 | open | US-NVS5-006 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | NRS 612.540; 14-17 quarters |
| `nv.ui.cep.rate` | [[FACT:nv.ui.cep.rate=0.05]] percent | 2026-01-01 | open | US-NVS5-006 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | Career Enhancement Program on UI base; not for [[FACT:nv.sui.employer.rate.max=5.4]]%-rated or reimbursing employers |
| `nv.sui.wage_base.other_state_credit` | [[FACT:nv.sui.wage_base.other_state_credit=True]] | 2026-01-01 | open | US-NVS5-006 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | 612.545(2)(b) |
| `nv.sui.wages.401k_included` | [[FACT:nv.sui.wages.401k_included=True]] | 2026-01-01 | open | US-NVS5-006 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | not listed as excluded in 612.190 (matches FUTA) |
| `nv.mbt.general.rate` | [[FACT:nv.mbt.general.rate=1.17]] percent | 2026-01-01 | open | US-NVP51-002 (A.2, NV Department of Taxation) | quarterly wages above 50,000; frozen by 360.203(4) (US-NVS5-012); employer-only |
| `nv.mbt.general.quarterly_threshold` | [[FACT:nv.mbt.general.quarterly_threshold=50000]] USD | 2026-01-01 | open | US-NVS5-011 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | - |
| `nv.mbt.financial_mining.rate` | [[FACT:nv.mbt.financial_mining.rate=1.554]] percent | 2026-01-01 | open | US-NVP51-002 (A.2, NV Department of Taxation) | all wages |
| `nv.mbt.base` | [[FACT:nv.mbt.base=UI gross wages + tips as reported to ESD less employer-paid health benefits]] | 2026-01-01 | open | US-NVS5-011 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | 363B.115; MBT/ESD wage comparison each quarter from 2026-01-01 (US-NVS5-009) |
| `nv.sui.employer.rate.min` | [[FACT:nv.sui.employer.rate.min=0.25]] percent | 2026-01-01 | 2026-12-31 | US-NVP51-001 (A.2, NV Dept of Employment, Training and Rehabilitation) | 18 rates |
| `nv.sui.employer.rate.max` | [[FACT:nv.sui.employer.rate.max=5.4]] percent | 2026-01-01 | 2026-12-31 | US-NVP51-001 (A.2, NV Dept of Employment, Training and Rehabilitation) | - |
| `nv.sui.employee.rate` | [[FACT:nv.sui.employee.rate=0]] percent | 2026-01-01 | open | US-NVS5-006 (A.1, Nevada Legislature) | - |
| `nv.sdi_pfml.exists` | [[FACT:nv.sdi_pfml.exists=False]] | 2023-07-01 | open | US-NVP51-002 (A.2, NV Department of Taxation) | - |

- Not configured in this release [[GAP:RQ-130]]: Cafeteria-plan salary reductions in unemployment and Modified Business Tax wages are not addressed in NRS 612.190.

## NV.4 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nv.payslip.items` | [[FACT:nv.payslip.items=itemized deductions each payment; available paid-leave hours each payday (50+ NV employees)]] | 2025-10-01 | open | US-NVS5-001 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | 608.110(2), 608.0197(1)(h) |

Rules:

- Language: English. NV has no language rule. (US-NVL-001, US-OWN-006)

- Not configured in this release [[GAP:RQ-131]]: Electronic pay-statement delivery not addressed.

## NV.5 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nv.report.ui.quarterly_due` | [[FACT:nv.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31 (received)]] | 2026-01-01 | open | US-NVS5-008 (A.3, Nevada DETR Employment Security Division) | ESS; SFTP EFW2 or CSV; 2023 handbook |
| `nv.report.mbt.due` | [[FACT:nv.report.mbt.due=last day of month after quarter (file even if no tax)]] | 2025-12-02 | open | US-NVS5-010 (A.3, Nevada Department of Taxation) | Form TAX-F003, 2026 edition. |
| `nv.newhire.report_days` | [[FACT:nv.newhire.report_days=20]] days | 2026-01-01 | open | US-NVS5-007 (A.1, Nevada Legislature; Nevada DETR Employment Security Division) | rehire after 60+ days |
| `nv.report.ui.registration_threshold.quarterly` | [[FACT:nv.report.ui.registration_threshold.quarterly=225]] USD | 2026-01-01 | open | US-NVP51-001 (A.2, NV Dept of Employment, Training and Rehabilitation) | - |

Rules:

- Agent access: ESS external user. (US-NVR3-003)

- Not configured in this release [[GAP:RQ-132]]: The unemployment report form identities in the 2023 employer handbook (RPT3795, NEW0098) differ from the Department of Taxation's form NUCS 4072; the current form set is not confirmed.

## NV.6 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nv.leave.paid.coverage_min_employees` | [[FACT:nv.leave.paid.coverage_min_employees=50]] | 2025-10-01 | open | US-NVS5-001 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | 608.0197; exempt first 2 years of operation |
| `nv.leave.paid.accrual_per_hour_worked` | [[FACT:nv.leave.paid.accrual_per_hour_worked=0.01923]] hours | 2025-10-01 | open | US-NVS5-001 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | about 40 h/yr; use from day 90; caps 40 h |
| `nv.leave.paid.payout_at_separation` | [[FACT:nv.leave.paid.payout_at_separation=False]] | 2025-10-01 | open | US-NVS5-001 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | reinstated on rehire within 90 days after involuntary separation |
| `nv.leave.dv_sa.hours_per_12_months` | [[FACT:nv.leave.dv_sa.hours_per_12_months=160]] hours | 2025-10-01 | open | US-NVS5-001 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | 608.0198; paid or unpaid |

- Not configured in this release [[GAP:RQ-133]]: AB 388 (2025) state family leave enactment not verified.
- Not configured in this release [[GAP:RQ-134]]: 608.0197 coverage of employees working partly in NV not addressed.

## NV.7 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nv.final_pay.discharge` | [[FACT:nv.final_pay.discharge=immediately]] | 2025-10-01 | open | US-NVS5-001 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | 608.020; also temporary layoff |
| `nv.term.final_pay.resignation` | [[FACT:nv.term.final_pay.resignation=earlier of regular payday or 7 days]] | 2025-10-01 | open | US-NVS5-001 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | 608.030; penalty max 30 days |

- Not configured in this release [[GAP:RQ-135]]: No statute on vacation/PTO payout outside 608.0197.

## NV.8 Benefits in kind and taxable wages

No Nevada rule is configured in this domain; the federal treatment in Annex FED applies.

## NV.9 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nv.garn.consumer.low_wage.max_rate` | [[FACT:nv.garn.consumer.low_wage.max_rate=18]] percent | 2026-01-01 | open | US-NVS5-004 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | if gross weekly <= 770; 25% above; or excess over 50x FMW, lesser |
| `nv.garn.creditor.max_percent` | [[FACT:nv.garn.creditor.max_percent=25]] percent | 2026-01-01 | open | US-NVS5-004 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | - |
| `nv.garn.consumer.low_wage.weekly_threshold` | [[FACT:nv.garn.consumer.low_wage.weekly_threshold=770]] USD | 2026-01-01 | open | US-NVS5-004 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | - |
| `nv.garn.consumer.employer_fee.per_period` | [[FACT:nv.garn.consumer.employer_fee.per_period=3]] USD | 2026-01-01 | open | US-NVS5-004 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | max 12/month; not first period |
| `nv.garn.support.treasurer_fee.per_withholding` | [[FACT:nv.garn.support.treasurer_fee.per_withholding=2]] USD | 2026-01-01 | open | US-NVS5-005 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | max 2/month; employer may also deduct 3 per withholding |
| `nv.garn.iwo.remit_days` | [[FACT:nv.garn.iwo.remit_days=7]] days | 2026-01-01 | open | US-NVS5-005 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | - |

## NV.10 Collective agreements and prevailing wage

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nv.prevailing_wage.exists` | [[FACT:nv.prevailing_wage.exists=True]] | 2026-01-01 | open | US-NVR3-002 (A.1, NV Legislature; US DOL Wage and Hour Division) | NRS 338.020 |

## NV.11 Indexation

Indexation of each value is stated in the note of the value concerned.

## NV.12 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nv.records.retention_years` | [[FACT:nv.records.retention_years=2]] years | 2025-10-01 | open | US-NVS5-001 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | 608.115; paid-leave records 1 year |
| `nv.data.pi.ssn_last4_excluded` | [[FACT:nv.data.pi.ssn_last4_excluded=True]] | 2026-01-01 | open | US-NVS5-017 (A.1, Nevada Legislature (Legislative Counsel Bureau)) | NRS 603A; no pay-statement truncation mandate |

## NV.13 Live legal change

No Nevada rule is configured in this domain; the federal treatment in Annex FED applies.

- Not configured in this release [[GAP:RQ-136]]: The AB 307 posting and the related domestic-violence and sexual-assault leave bulletin were not read (the site blocked automated access).

## NV.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## NV.15 Special populations

- Domestic / household: Household-only employers are exempt from MBT. (US-NVS5-016, US-NVS5-001, US-NVS5-006, US-NVS5-009)
- Agricultural: Meal/lodging credit caps do not apply; Non-cash agricultural pay is not UI wages. (US-NVS5-001, US-NVS5-006)
- Minors: Minimum wage applies, except under-18s at a nonprofit in after-school or summer jobs (Const.). (US-NVS5-015, US-NVS5-013, US-NVS5-006)
- Tipped: Tips belong to employees, and pooling among employees is allowed; Reported tips are UI wages and MBT wages. (US-NVS5-013, US-NVS5-018, US-NVS5-006, US-NVS5-009)
- Clergy / religious: No wage tax. (US-NVS5-006, US-NVS5-009)
- Nonresident aliens: No state rule beyond federal (no wage tax; UI by localization). (US-NVS5-014, US-NVS5-006)
- Government: Out of private scope; MBT exempts political subdivisions. (US-NVS5-009, US-NVS5-006, US-NVS5-001)
- Not configured in this release [[GAP:RQ-137]]: Thresholds, amounts or conditions for these populations are stated in the sources read without a confirmed value record and are not configured from this annex: Domestic / household; Agricultural; Minors; Tipped; Clergy / religious; Students; Statutory employees; Government.

## NV.16 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## NV.S Sources

| Source | Authority |
|---|---|
| US-NVP51-001 | NV Dept of Employment, Training and Rehabilitation |
| US-NVP51-002 | NV Department of Taxation |
| US-NVR3-002 | NV Legislature; US DOL Wage and Hour Division |
| US-NVS5-001 | Nevada Legislature (Legislative Counsel Bureau) |
| US-NVS5-003 | Nevada Office of the Labor Commissioner |
| US-NVS5-004 | Nevada Legislature (Legislative Counsel Bureau) |
| US-NVS5-005 | Nevada Legislature (Legislative Counsel Bureau) |
| US-NVS5-006 | Nevada Legislature (Legislative Counsel Bureau) |
| US-NVS5-007 | Nevada Legislature; Nevada DETR Employment Security Division |
| US-NVS5-008 | Nevada DETR Employment Security Division |
| US-NVS5-010 | Nevada Department of Taxation |
| US-NVS5-011 | Nevada Legislature (Legislative Counsel Bureau) |
| US-NVS5-013 | Nevada Legislature (Legislative Counsel Bureau) |
| US-NVS5-014 | Nevada Legislature (Legislative Counsel Bureau) |
| US-NVS5-017 | Nevada Legislature (Legislative Counsel Bureau) |
| US-NVS5-019 | Nevada DETR (Research & Analysis Bureau, for the Employment Security Division) |

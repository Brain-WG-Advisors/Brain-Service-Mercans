# Annex MN: Minnesota


United States Country Configuration Guide, jurisdiction annex MN. Tax year 2026; currency USD (two decimal places).

**Scope of this annex.**

This annex holds the Minnesota layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in Annex FED, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register, with the authority and address listed in section MN.S (the source address is held in the register row). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

**Jurisdiction layer.**

| Item | Value |
|---|---|
| Annex tier | T3 |
| Basis | State withholding verified [US-MNPIT-001] |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

**Configuration decisions.**

- Minnesota overtime applies after [[FACT:mn.overtime.weekly_threshold_hours=48]] hours a week; employers covered by the federal Fair Labor Standards Act still pay overtime after the federal weekly threshold (Annex FED). Do not configure the state threshold as the only overtime rule.
- Minnesota does not follow the 2025 federal changes: the federal tips and overtime deductions and the later federal fringe-benefit changes do not reduce Minnesota withholding. The state follows the Internal Revenue Code as of [[FACT:mn.pit.conformity.irc_date=2023-05-01]].
- Paid Leave contributions start in 2026 at [[FACT:mn.pfml.rate.total=0.88]] percent of wages up to [[FACT:mn.pfml.wage_cap.annual=185000]] USD; the employee may bear at most [[FACT:mn.pfml.employee.max_share.rate=0.44]] percent.
- No tip credit is allowed: [[FACT:mn.minwage.tip_credit.allowed=False]].
- The pay statement shows the earned sick and safe time balance: [[FACT:mn.payslip.esst_balance.required=True]].

## MN.1 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mn.minwage.hourly` | [[FACT:mn.minwage.hourly=11.41]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-002 (A.2, Minnesota Department of Labor and Industry) | all employers |
| `mn.minwage.hourly` | [[FACT:mn.minwage.hourly=11.87]] USD | 2027-01-01 | open | US-MNS5-002 (A.2, Minnesota Department of Labor and Industry) | published 2027 rate |
| `mn.labour.minwage.training.hourly` | [[FACT:mn.labour.minwage.training.hourly=9.31]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-002 (A.2, Minnesota Department of Labor and Industry) | 90-day training wage, employees under 20 |
| `mn.labour.minwage.training.hourly` | [[FACT:mn.labour.minwage.training.hourly=9.68]] USD | 2027-01-01 | open | US-MNS5-002 (A.2, Minnesota Department of Labor and Industry) | published 2027 rate |
| `mn.labour.minwage.indexation.cap` | [[FACT:mn.labour.minwage.indexation.cap=5]] percent | 2018-01-01 | open | US-MNS5-001 (A.1, Minnesota Office of the Revisor of Statutes) | 12-month PCE implicit price deflator, capped at 5%, set by Aug 31, effective Jan 1 |
| `mn.minwage.tip_credit.allowed` | [[FACT:mn.minwage.tip_credit.allowed=False]] | 2018-01-01 | open | US-MNS5-001 (A.1, Minnesota Office of the Revisor of Statutes) | no tip credit; tips belong to the employee |
| `mn.labour.minwage.local.minneapolis.hourly` | [[FACT:mn.labour.minwage.local.minneapolis.hourly=16.37]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-008 (A.2, City of Minneapolis, Labor Standards Enforcement Division) | all employer sizes |
| `mn.labour.minwage.local.minneapolis.hourly` | [[FACT:mn.labour.minwage.local.minneapolis.hourly=17.02]] USD | 2027-01-01 | open | US-MNS5-008 (A.2, City of Minneapolis, Labor Standards Enforcement Division) | published 2027 rate |
| `mn.labour.minwage.local.st_paul.macro_large.hourly` | [[FACT:mn.labour.minwage.local.st_paul.macro_large.hourly=16.37]] USD | 2026-01-01 | open | US-MNS5-009 (A.2, City of Saint Paul, Department of Human Rights and Equal Economic Opportunity, Labor Standards) | macro (10,001+), large (101-10,000) and the City |
| `mn.labour.minwage.local.st_paul.small.hourly` | [[FACT:mn.labour.minwage.local.st_paul.small.hourly=15.0]] USD | 2025-07-01 | 2026-06-30 | US-MNS5-009 (A.2, City of Saint Paul, Department of Human Rights and Equal Economic Opportunity, Labor Standards) | small (6-100) |
| `mn.labour.minwage.local.st_paul.small.hourly` | [[FACT:mn.labour.minwage.local.st_paul.small.hourly=16.37]] USD | 2026-07-01 | open | US-MNS5-009 (A.2, City of Saint Paul, Department of Human Rights and Equal Economic Opportunity, Labor Standards) | small (6-100) |
| `mn.labour.minwage.local.st_paul.micro.hourly` | [[FACT:mn.labour.minwage.local.st_paul.micro.hourly=14.25]] USD | 2026-07-01 | 2027-06-30 | US-MNS5-009 (A.2, City of Saint Paul, Department of Human Rights and Equal Economic Opportunity, Labor Standards) | micro (5 or fewer) |
| `mn.labour.minwage.local.st_paul.micro.hourly` | [[FACT:mn.labour.minwage.local.st_paul.micro.hourly=15.0]] USD | 2027-07-01 | open | US-MNS5-009 (A.2, City of Saint Paul, Department of Human Rights and Equal Economic Opportunity, Labor Standards) | micro; indexed city rate from 2028-07-01 |
| `mn.labour.minwage.local.st_paul.youth.hourly` | [[FACT:mn.labour.minwage.local.st_paul.youth.hourly=13.95]] USD | 2026-07-01 | open | US-MNS5-009 (A.2, City of Saint Paul, Department of Human Rights and Equal Economic Opportunity, Labor Standards) | youth/training rate; city minimum applies from 18th birthday |
| `mn.overtime.weekly_threshold_hours` | [[FACT:mn.overtime.weekly_threshold_hours=48]] hours | 2026-01-01 | open | US-MNS5-003 (A.1, Minnesota Office of the Revisor of Statutes) | state rule 1.5x over 48 h; FLSA 40 h binds FLSA-covered employers |
| `mn.overtime.premium.multiplier` | [[FACT:mn.overtime.premium.multiplier=1.5]] ratio | 2026-01-01 | open | US-MNS5-003 (A.1, Minnesota Office of the Revisor of Statutes) | - |
| `mn.labour.pay_frequency.max_days` | [[FACT:mn.labour.pay_frequency.max_days=31]] days | 2026-01-01 | open | US-MNS5-005 (A.1, Minnesota Office of the Revisor of Statutes) | commissions at least every 3 months |

- Not configured in this release [[GAP:RQ-037]]: The direct deposit and paycard consent rule was not read.
- Not configured in this release [[GAP:RQ-038]]: St. Paul next-year indexed city rate for macro/large/small is not on the page read.

## MN.2 Income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mn.wh.method` | [[FACT:mn.wh.method=annualised formula: wages x periods - allowances x 5300, chart, / periods]] | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | DOR booklet 2026 computer formula p.34 |
| `mn.pit.allowance.amount` | [[FACT:mn.pit.allowance.amount=5300]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | per W-4MN allowance, annual |
| `mn.pit.wh.single.1.floor` | [[FACT:mn.pit.wh.single.1.floor=4700]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | annual taxable band start, [[FACT:mn.pit.wh.single.1.rate=5.35]]% |
| `mn.pit.wh.single.1.rate` | [[FACT:mn.pit.wh.single.1.rate=5.35]] percent | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.single.2.floor` | [[FACT:mn.pit.wh.single.2.floor=38010]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | add [[FACT:mn.pit.wh.single.2.base_tax=1,782.09]] |
| `mn.pit.wh.single.2.rate` | [[FACT:mn.pit.wh.single.2.rate=6.8]] percent | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.single.2.base_tax` | [[FACT:mn.pit.wh.single.2.base_tax=1782.09]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | cumulative add reproduced |
| `mn.pit.wh.single.3.floor` | [[FACT:mn.pit.wh.single.3.floor=114130]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.single.3.rate` | [[FACT:mn.pit.wh.single.3.rate=7.85]] percent | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.single.3.base_tax` | [[FACT:mn.pit.wh.single.3.base_tax=6958.25]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.single.4.floor` | [[FACT:mn.pit.wh.single.4.floor=207850]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.single.4.rate` | [[FACT:mn.pit.wh.single.4.rate=9.85]] percent | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.single.4.base_tax` | [[FACT:mn.pit.wh.single.4.base_tax=14315.27]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.married.1.floor` | [[FACT:mn.pit.wh.married.1.floor=14700]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.married.1.rate` | [[FACT:mn.pit.wh.married.1.rate=5.35]] percent | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.married.2.floor` | [[FACT:mn.pit.wh.married.2.floor=63400]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.married.2.rate` | [[FACT:mn.pit.wh.married.2.rate=6.8]] percent | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.married.2.base_tax` | [[FACT:mn.pit.wh.married.2.base_tax=2605.45]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.married.3.floor` | [[FACT:mn.pit.wh.married.3.floor=208180]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.married.3.rate` | [[FACT:mn.pit.wh.married.3.rate=7.85]] percent | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.married.3.base_tax` | [[FACT:mn.pit.wh.married.3.base_tax=12450.49]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.married.4.floor` | [[FACT:mn.pit.wh.married.4.floor=352630]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.married.4.rate` | [[FACT:mn.pit.wh.married.4.rate=9.85]] percent | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.pit.wh.married.4.base_tax` | [[FACT:mn.pit.wh.married.4.base_tax=23789.82]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | - |
| `mn.wh.supplemental.rate` | [[FACT:mn.wh.supplemental.rate=6.25]] percent | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | Method 2; Method 1 aggregate mandatory when not separately listed |
| `mn.pit.backup_withholding.rate` | [[FACT:mn.pit.backup_withholding.rate=9.85]] percent | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | personal-service payments without valid TIN |
| `mn.pit.oracle.example_1.withholding` | [[FACT:mn.pit.oracle.example_1.withholding=91.27]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | Derived from the MN Withholding Tax Instructions 2026 computer formula (p.34): biweekly 2,000.00, single, 1 allowance: 2,000 x 26 = 52,000; 52,000 - 5,300 = 46,700; [[FACT:mn.pit.wh.single.2.base_tax=1,782.09]] + (46,700 - [[FACT:mn.pit.wh.single.2.floor=38,010]]) x [[FACT:mn.pit.wh.single.2.rate=6.80]]% = 2,373.01; 2,373.01 / 26 = [[FACT:mn.pit.oracle.example_1.withholding=91.27]] (91 if rounded). No published page carries [[FACT:mn.pit.oracle.example_1.withholding=91.27]]. Official engine: DOR Withholding Tax Calculator [US-MNR3-002]. |
| `mn.pit.rounding` | [[FACT:mn.pit.rounding=nearest dollar permitted]] | 2026-01-01 | open | US-MNP51-001 (A.1, Minnesota Office of the Revisor) | 290.92 subd. 2a; formula step 6. |
| `mn.wh.certificate` | [[FACT:mn.wh.certificate=W-4MN absent: single, 0 allowances]] | 2026-01-01 | open | US-MNPIT-001 (A.2, Minnesota Department of Revenue) | - |

## MN.2b Non-resident regime and reciprocity

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mn.pit.nonresident.threshold.annual` | [[FACT:mn.pit.nonresident.threshold.annual=15300]] USD | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | no MN withholding on nonresident below expected [[FACT:mn.pit.nonresident.threshold.annual=15,300]] |
| `mn.reciprocity.states` | [[FACT:mn.reciprocity.states=MI;ND (Form MWR)]] | 2026-01-01 | open | US-MNPIT-001 (A.2, Minnesota Department of Revenue) | - |

## MN.2c Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mn.local_wage_tax.exists` | [[FACT:mn.local_wage_tax.exists=False]] | 2026-01-01 | open | US-MNR3-001 (A.2, Minnesota House Research Department and Fiscal Analysis Department) | general law prohibits local income taxes |

## MN.3 Social insurance: unemployment, disability, paid leave and payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mn.ui.additional_assessment.rate` | [[FACT:mn.ui.additional_assessment.rate=14.0]] percent | 2026-01-01 | 2026-12-31 | US-MNP52-001 (A.2, Minnesota Department of Employment and Economic Development) | of the UI tax |
| `mn.ui.special_assessment.rate` | [[FACT:mn.ui.special_assessment.rate=0.0]] percent | 2026-01-01 | 2026-12-31 | US-MNB5-402 (A.2, MN official authority) | - |
| `mn.ui.workforce_fee.rate` | [[FACT:mn.ui.workforce_fee.rate=0.1]] percent | 2026-01-01 | open | US-MNB5-401 (A.2, MN official authority) | of taxable wages; reimbursing employers exempt |
| `mn.pfml.employer_share.min` | [[FACT:mn.pfml.employer_share.min=50]] percent | 2026-01-01 | open | US-MNS5-018 (A.1, Minnesota Office of the Revisor of Statutes) | - |
| `mn.sui.wage_base` | [[FACT:mn.sui.wage_base=44000]] USD | 2026-01-01 | 2026-12-31 | US-MNP52-001 (A.2, Minnesota Department of Employment and Economic Development) | 60% of state average annual wage rounded to 1,000 (US-MNS5-017) |
| `mn.ui.rate.base` | [[FACT:mn.ui.rate.base=0.4]] percent | 2026-01-01 | 2026-12-31 | US-MNP52-001 (A.2, Minnesota Department of Employment and Economic Development) | - |
| `mn.sui.employer.rate.max` | [[FACT:mn.sui.employer.rate.max=8.9]] percent | 2026-01-01 | 2026-12-31 | US-MNP52-001 (A.2, Minnesota Department of Employment and Economic Development) | - |
| `mn.sui.employee.rate` | [[FACT:mn.sui.employee.rate=0]] percent | 2026-01-01 | open | US-MNP52-001 (A.2, Minnesota Department of Employment and Economic Development) | no employee UI contribution |
| `mn.pfml.rate.total` | [[FACT:mn.pfml.rate.total=0.88]] percent | 2026-01-01 | 2027-12-31 | US-MNP52-003 (A.2, Minnesota DEED (Paid Leave)) | family 0.27 + medical 0.61; statutory base rate adjusted by the commissioner (US-MNS5-018) |
| `mn.pfml.rate.family` | [[FACT:mn.pfml.rate.family=0.27]] percent | 2026-01-01 | 2027-12-31 | US-MNP52-003 (A.2, Minnesota DEED (Paid Leave)) | - |
| `mn.pfml.rate.medical` | [[FACT:mn.pfml.rate.medical=0.61]] percent | 2026-01-01 | 2027-12-31 | US-MNP52-003 (A.2, Minnesota DEED (Paid Leave)) | - |
| `mn.pfml.employee.max_share.rate` | [[FACT:mn.pfml.employee.max_share.rate=0.44]] percent | 2026-01-01 | 2027-12-31 | US-MNP52-003 (A.2, Minnesota DEED (Paid Leave)) | employer pays at least 50% (268B.14, US-MNS5-018) |
| `mn.pfml.small_employer.rate` | [[FACT:mn.pfml.small_employer.rate=0.66]] percent | 2026-01-01 | 2027-12-31 | US-MNP52-003 (A.2, Minnesota DEED (Paid Leave)) | - |
| `mn.pfml.wage_cap.annual` | [[FACT:mn.pfml.wage_cap.annual=185000]] USD | 2026-01-01 | 2026-12-31 | US-MNP52-003 (A.2, Minnesota DEED (Paid Leave)) | cap = OASDI base; 2027 cap follows the 2027 OASDI base (Annex FED) |
| `mn.sdi.exists` | [[FACT:mn.sdi.exists=False]] | 2026-01-01 | open | US-MNP52-003 (A.2, Minnesota DEED (Paid Leave)) | No SDI/TDI program in Minnesota. |

- Not configured in this release [[GAP:RQ-039]]: The due dates and file format of the quarterly unemployment wage-detail report are not in Minn. Stat. 268.044, and the agency site was unreachable.
- Not configured in this release [[GAP:RQ-040]]: 2027 UI wage base not yet published.

## MN.4 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mn.payslip.frequency` | [[FACT:mn.payslip.frequency=each pay period, written or electronic]] | 2026-01-01 | open | US-MNP6-001 (A.1, Minnesota Office of the Revisor of Statutes) | 181.032, 12 content items; electronic needs employer computer access and 3-year availability |
| `mn.payslip.esst_balance.required` | [[FACT:mn.payslip.esst_balance.required=True]] | 2024-01-01 | open | US-MNS5-011 (A.1, Minnesota Office of the Revisor of Statutes) | hours available and used, each pay period |

## MN.5 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mn.report.wh.quarterly_due` | [[FACT:mn.report.wh.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | e-Services; annual filers (<=500 USD prior year) by Jan 31 |
| `mn.report.w2.due` | [[FACT:mn.report.w2.due=Jan 31 (employees and DOR)]] | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | e-Services mandatory above 10 W-2+1099 |
| `mn.report.ui.wage_detail.fields` | [[FACT:mn.report.ui.wage_detail.fields=name; SSN; total wages; total paid hours worked]] | 2026-01-01 | open | US-MNS5-015 (A.1, Minnesota Office of the Revisor of Statutes) | exempt full-time reported at 40 h/week; zero report required |
| `mn.newhire.report_days` | [[FACT:mn.newhire.report_days=20]] days | 2026-01-01 | open | US-MNS5-016 (A.1, Minnesota Office of the Revisor of Statutes) | rehire after 60+ days separation |

Rules:

- POA / agents: REV184b (DOR); UI Agent Self-Service ID. (US-MNP52-005, US-MNP6-003)

- Not configured in this release [[GAP:RQ-041]]: W-2 e-file method changed; DOR Fact Sheets 2 and 2a not read.

## MN.6 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mn.leave.esst.accrual_ratio_hours_worked` | [[FACT:mn.leave.esst.accrual_ratio_hours_worked=30]] hours | 2024-01-01 | open | US-MNS5-011 (A.1, Minnesota Office of the Revisor of Statutes) | 1 h per 30 h worked |
| `mn.leave.esst.annual_accrual_cap_hours` | [[FACT:mn.leave.esst.annual_accrual_cap_hours=48]] hours | 2024-01-01 | open | US-MNS5-011 (A.1, Minnesota Office of the Revisor of Statutes) | - |
| `mn.leave.esst.balance_cap_hours` | [[FACT:mn.leave.esst.balance_cap_hours=80]] hours | 2024-01-01 | open | US-MNS5-011 (A.1, Minnesota Office of the Revisor of Statutes) | - |
| `mn.leave.esst.payout_at_separation` | [[FACT:mn.leave.esst.payout_at_separation=False]] | 2024-01-01 | open | US-MNS5-011 (A.1, Minnesota Office of the Revisor of Statutes) | - |

- Not configured in this release [[GAP:RQ-042]]: Minneapolis / St. Paul / Duluth / Bloomington ESST ordinances not read.

## MN.7 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mn.final_pay.discharge` | [[FACT:mn.final_pay.discharge=within 24 hours after written demand]] | 2026-01-01 | open | US-MNS5-006 (A.1, Minnesota Office of the Revisor of Statutes) | penalty up to 15 days average daily earnings |
| `mn.term.final_pay.resignation` | [[FACT:mn.term.final_pay.resignation=next regular payday; max 20 calendar days]] | 2026-01-01 | open | US-MNS5-007 (A.1, Minnesota Office of the Revisor of Statutes) | second payday if next is <5 days after last day |
| `mn.term.ui_separation_notice.required` | [[FACT:mn.term.ui_separation_notice.required=False]] | 2026-01-01 | open | US-MNS5-021 (A.1, Minnesota Office of the Revisor of Statutes) | posting only (268.068) |

- Not configured in this release [[GAP:RQ-043]]: No DLI statement confirming vacation payout follows the employer's policy (inferred from 181.13/181.14 wording).

## MN.8 Benefits in kind and taxable wages

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mn.pit.conformity.irc_date` | [[FACT:mn.pit.conformity.irc_date=2023-05-01]] | 2026-01-01 | 2026-12-31 | US-MNS5-010 (A.2, Minnesota Department of Revenue) | MN has not adopted H.R. 1 (2025) withholding changes |

- Not configured in this release [[GAP:RQ-044]]: Full MN-vs-federal departures for fringe exclusions after 2023-05-01 not inventoried.

## MN.9 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mn.garn.creditor.max_percent` | [[FACT:mn.garn.creditor.max_percent=25]] percent | 2026-01-01 | open | US-MNS5-013 (A.1, Minnesota Office of the Revisor of Statutes) | tiers 25/15/10% by weekly income vs hourly minimum x80/60/40, or excess over 40x minimum, lesser |
| `mn.garn.support.max_rate` | [[FACT:mn.garn.support.max_rate=65]] percent | 2026-01-01 | open | US-MNS5-013 (A.1, Minnesota Office of the Revisor of Statutes) | 50/55/60/65% |
| `mn.garn.iwo.remit_business_days` | [[FACT:mn.garn.iwo.remit_business_days=7]] days | 2026-01-01 | open | US-MNS5-014 (A.1, Minnesota Office of the Revisor of Statutes) | Partly confirmed by the published source. |
| `mn.deduction.uniform.max` | [[FACT:mn.deduction.uniform.max=50]] USD | 2018-01-01 | open | US-MNS5-001 (A.1, Minnesota Office of the Revisor of Statutes) | may not reduce pay below minimum wage |

- Not configured in this release [[GAP:RQ-045]]: Employer fee for processing an IWO not located (US-MNS5-014 partial).
- Not configured in this release [[GAP:RQ-046]]: State tax levy on wages not read.

## MN.10 Collective agreements and prevailing wage

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mn.prevailing_wage.exists` | [[FACT:mn.prevailing_wage.exists=True]] | 2026-01-01 | open | US-MNP6-002 (A.1, Minnesota Office of the Revisor of Statutes) | 177.41-177.44 state-funded projects |

## MN.11 Indexation

Indexation of each value is stated in the note of the value concerned.

## MN.12 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mn.records.retention_years` | [[FACT:mn.records.retention_years=3]] years | 2026-01-01 | open | US-MNS5-020 (A.1, Minnesota Office of the Revisor of Statutes) | 177.30 |
| `mn.data.ssn.public_display_prohibited` | [[FACT:mn.data.ssn.public_display_prohibited=True]] | 2026-01-01 | open | US-MNS5-019 (A.1, Minnesota Office of the Revisor of Statutes) | 325E.59 |

## MN.13 Live legal change

No Minnesota rule is configured in this domain; the federal treatment in Annex FED applies.

## MN.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## MN.15 Special populations

- Domestic / household: excluded from new-hire reporting; sole-practitioner babysitters outside the MFLSA. (US-MNS5-017, US-MNS5-016, US-MNS5-004)
- Agricultural: MFLSA excludes small salaried farm groups and some farm minors; H-2A not covered. (US-MNS5-004, US-MNS5-017, US-MNS5-005)
- Tipped: No tip credit at state level. (US-MNS5-001, US-MNS5-002)
- Clergy / religious: Excluded from the MFLSA; church and minister employment not UI-covered. (US-MNS5-004, US-MNS5-017)
- Students: Students employed by their school, full-time credit students, J-1 summer work travel and student nurses not UI-covered. (US-MNS5-017)
- Nonresident aliens: No state rule beyond federal found in the booklet. (US-MNS5-010)
- Statutory employees: No state rule found beyond federal (booklet read). (US-MNS5-010)
- Government employees: MFLSA excludes elected officials, police/fire and some PERA-ineligible staff; public-employer comp time; public employers report contractors as new hires. (US-MNS5-004, US-MNS5-003, US-MNS5-006, US-MNS5-016)
- Family employment: Spouse, child or parent employment not UI-covered. (US-MNS5-017)
- Not configured in this release [[GAP:RQ-047]]: Thresholds, amounts or conditions for these populations are stated in the sources read without a confirmed value record and are not configured from this annex: Domestic / household; Agricultural; Minors; Nonresident aliens; Government employees.

## MN.16 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## MN.S Sources

| Source | Authority |
|---|---|
| US-MNB5-401 | MN official authority |
| US-MNB5-402 | MN official authority |
| US-MNP51-001 | Minnesota Office of the Revisor |
| US-MNP52-001 | Minnesota Department of Employment and Economic Development |
| US-MNP52-003 | Minnesota DEED (Paid Leave) |
| US-MNP6-001 | Minnesota Office of the Revisor of Statutes |
| US-MNP6-002 | Minnesota Office of the Revisor of Statutes |
| US-MNPIT-001 | Minnesota Department of Revenue |
| US-MNR3-001 | Minnesota House Research Department and Fiscal Analysis Department |
| US-MNS5-001 | Minnesota Office of the Revisor of Statutes |
| US-MNS5-002 | Minnesota Department of Labor and Industry |
| US-MNS5-003 | Minnesota Office of the Revisor of Statutes |
| US-MNS5-005 | Minnesota Office of the Revisor of Statutes |
| US-MNS5-006 | Minnesota Office of the Revisor of Statutes |
| US-MNS5-007 | Minnesota Office of the Revisor of Statutes |
| US-MNS5-008 | City of Minneapolis, Labor Standards Enforcement Division |
| US-MNS5-009 | City of Saint Paul, Department of Human Rights and Equal Economic Opportunity, Labor Standards |
| US-MNS5-010 | Minnesota Department of Revenue |
| US-MNS5-011 | Minnesota Office of the Revisor of Statutes |
| US-MNS5-013 | Minnesota Office of the Revisor of Statutes |
| US-MNS5-014 | Minnesota Office of the Revisor of Statutes |
| US-MNS5-015 | Minnesota Office of the Revisor of Statutes |
| US-MNS5-016 | Minnesota Office of the Revisor of Statutes |
| US-MNS5-018 | Minnesota Office of the Revisor of Statutes |
| US-MNS5-019 | Minnesota Office of the Revisor of Statutes |
| US-MNS5-020 | Minnesota Office of the Revisor of Statutes |
| US-MNS5-021 | Minnesota Office of the Revisor of Statutes |

# Annex ND: North Dakota


United States Country Configuration Guide, jurisdiction annex ND. Tax year 2026; currency USD (two decimal places).

**Scope of this annex.**

This annex holds the North Dakota layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in Annex FED, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register, with the authority and address listed in section ND.S (the source address is held in the register row). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

**Jurisdiction layer.**

| Item | Value |
|---|---|
| Annex tier | T3 |
| Basis | State withholding verified [US-ND-001/-002] |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

**Configuration decisions.**

- The worked example in the 2026 withholding booklet does not reproduce from the 2026 table. Use the table and formula; the reference result is [[FACT:nd.pit.oracle.example_1.withholding=13]] USD.
- A pay statement content rule exists (`nd.payslip.items`).
- North Dakota uses the federal Form W-4 (no state certificate, `nd.wh.certificate`); supplemental wages are withheld at [[FACT:nd.wh.supplemental.rate=1.5]] percent.

## ND.1 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nd.minwage.hourly` | [[FACT:nd.minwage.hourly=7.25]] USD | 2009-07-24 | open | US-NDS5-006 (A.1, ND Legislative Council) | not indexed; no 2027 change |
| `nd.local_mandates.preempted` | [[FACT:nd.local_mandates.preempted=True]] | 2009-07-24 | open | US-NDS5-006 (A.1, ND Legislative Council) | 34-06-23 |
| `nd.overtime.weekly_threshold_hours` | [[FACT:nd.overtime.weekly_threshold_hours=40]] hours | 2012-10-01 | open | US-NDS5-007 (A.1, ND Legislative Council (NDAC; Department of Labor and Human Rights rule)) | weekly, no averaging; taxicab 50 h; 8/80 by agreement for hospitals |
| `nd.overtime.premium.multiplier` | [[FACT:nd.overtime.premium.multiplier=1.5]] ratio | 2012-10-01 | open | US-NDS5-007 (A.1, ND Legislative Council (NDAC; Department of Labor and Human Rights rule)) | - |
| `nd.labour.overtime.computer_professional_threshold.hourly` | [[FACT:nd.labour.overtime.computer_professional_threshold.hourly=27.63]] USD | 2012-10-01 | open | US-NDS5-007 (A.1, ND Legislative Council (NDAC; Department of Labor and Human Rights rule)) | - |
| `nd.labour.meal_period.minutes` | [[FACT:nd.labour.meal_period.minutes=30]] minutes | 2012-10-01 | open | US-NDS5-007 (A.1, ND Legislative Council (NDAC; Department of Labor and Human Rights rule)) | shifts over 5 h with 2+ employees on duty; waivable |
| `nd.pay_frequency.rule` | [[FACT:nd.pay_frequency.rule=at least once each calendar month on regular paydays]] | 2026-01-01 | open | US-NDS5-005 (A.1, ND Legislative Council) | 34-14-02 |
| `nd.payment.method` | [[FACT:nd.payment.method=cash, check, direct deposit to employee-chosen institution; paycard only at employee election]] | 2026-01-01 | open | US-NDS5-005 (A.1, ND Legislative Council) | - |
| `nd.labour.board_lodging_credit.daily_max` | [[FACT:nd.labour.board_lodging_credit.daily_max=18.0]] USD | 2012-10-01 | open | US-NDS5-007 (A.1, ND Legislative Council (NDAC; Department of Labor and Human Rights rule)) | written voluntary agreement |
| `nd.labour.tip_credit.max_ratio` | [[FACT:nd.labour.tip_credit.max_ratio=33]] percent | 2012-10-01 | open | US-NDS5-007 (A.1, ND Legislative Council (NDAC; Department of Labor and Human Rights rule)) | - |
| `nd.minwage.tipped.cash_wage` | [[FACT:nd.minwage.tipped.cash_wage=4.86]] USD | 2012-10-01 | open | US-NDS5-007 (A.1, ND Legislative Council (NDAC; Department of Labor and Human Rights rule)) | [[FACT:nd.minwage.hourly=7.25]] x (1 - 0.33) = 4.8575 -> [[FACT:nd.minwage.tipped.cash_wage=4.86]] (NDAC 46-02-07-03: tip credit of thirty-three percent of the minimum wage). |

## ND.2 Income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nd.wh.certificate` | [[FACT:nd.wh.certificate=federal Form W-4 (no state certificate); none on file = single]] | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | - |
| `nd.wh.method` | [[FACT:nd.wh.method=annual percentage method on federal W-4 (tables route under 57-38-59(3))]] | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | - |
| `nd.pit.wh.single.1.ceiling` | [[FACT:nd.pit.wh.single.1.ceiling=57625]] USD | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | 0% up to |
| `nd.pit.wh.single.2.rate` | [[FACT:nd.pit.wh.single.2.rate=1.95]] percent | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | [[FACT:nd.pit.wh.single.1.ceiling=57,625]]-[[FACT:nd.pit.wh.single.2.ceiling=258,450]] |
| `nd.pit.wh.single.2.ceiling` | [[FACT:nd.pit.wh.single.2.ceiling=258450]] USD | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | - |
| `nd.pit.wh.single.3.base_tax` | [[FACT:nd.pit.wh.single.3.base_tax=3916.09]] USD | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) |  reproduced |
| `nd.pit.wh.single.3.rate` | [[FACT:nd.pit.wh.single.3.rate=2.5]] percent | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | - |
| `nd.pit.wh.mfj.1.ceiling` | [[FACT:nd.pit.wh.mfj.1.ceiling=57500]] USD | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | - |
| `nd.pit.wh.mfj.2.ceiling` | [[FACT:nd.pit.wh.mfj.2.ceiling=168525]] USD | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | - |
| `nd.pit.wh.mfj.3.base_tax` | [[FACT:nd.pit.wh.mfj.3.base_tax=2164.99]] USD | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | - |
| `nd.pit.wh.hoh.1.ceiling` | [[FACT:nd.pit.wh.hoh.1.ceiling=78475]] USD | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | - |
| `nd.pit.wh.hoh.2.ceiling` | [[FACT:nd.pit.wh.hoh.2.ceiling=289675]] USD | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | - |
| `nd.pit.wh.hoh.3.base_tax` | [[FACT:nd.pit.wh.hoh.3.base_tax=4118.4]] USD | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | - |
| `nd.pit.allowance.annual.pre2020_w4` | [[FACT:nd.pit.allowance.annual.pre2020_w4=5050]] USD | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | weekly 97, biweekly 194, semimonthly 210, monthly 420 |
| `nd.pit.rounding` | [[FACT:nd.pit.rounding=nearest whole dollar; under 1.00 need not be withheld]] | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | - |
| `nd.wh.supplemental.rate` | [[FACT:nd.wh.supplemental.rate=1.5]] percent | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | or aggregate |
| `nd.pit.oracle.example_1.withholding` | [[FACT:nd.pit.oracle.example_1.withholding=13]] USD | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | weekly 1,800 single (2020+ W-4): (93,600-[[FACT:nd.pit.wh.single.1.ceiling=57,625]]) x [[FACT:nd.pit.wh.single.2.rate=1.95]]% = 701.51; /52 = 13.49 -> 13. Booklet prints [[FACT:nd.oracle.section2_booklet.withholding=734]]/14 (stale example; do NOT use); weekly bracket table shows 14 (midpoint basis, 1.00 residual) |
| `nd.pit.oracle.example_2.withholding` | [[FACT:nd.pit.oracle.example_2.withholding=10]] USD | 2026-01-01 | 2026-12-31 | US-NDS5-001 (A.2, ND Office of State Tax Commissioner) | Section 1 weekly 1,800 single 2 allowances: (1,606-1,108) x [[FACT:nd.pit.wh.single.2.rate=1.95]]% = 9.71 -> 10, as printed |
| `nd.pit.agricultural.withholding_required` | [[FACT:nd.pit.agricultural.withholding_required=False]] | 2026-01-01 | open | US-NDS5-002 (A.2, ND Office of State Tax Commissioner) | farmer/rancher wages |

- Not configured in this release [[GAP:RQ-083]]: The Section 2 example of the 2026 withholding booklet does not reproduce from the 2026 table; the table and formula result ([[FACT:nd.pit.oracle.example_1.withholding=13]] USD) is used instead, and the defect is not yet confirmed with the authority.

## ND.2b Non-resident regime and reciprocity

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nd.reciprocity.states` | [[FACT:nd.reciprocity.states=MN;MT (Form NDW-R, renewed by Feb 28)]] | 2026-01-01 | open | US-NDS5-002 (A.2, ND Office of State Tax Commissioner) | - |
| `nd.pit.nonresident.mobile_workforce.days` | [[FACT:nd.pit.nonresident.mobile_workforce.days=20]] days | 2026-01-01 | open | US-NDS5-004 (A.1, ND Legislative Council) | 57-38-59.3; home state reciprocal or no income tax; excludes athletes, entertainers, construction, key employees |
| `nd.pit.nra.certificate` | [[FACT:nd.pit.nra.certificate=separate W-4 marked North Dakota only - nonresident alien; Single; Exempt not allowed]] | 2026-01-01 | open | US-NDS5-002 (A.2, ND Office of State Tax Commissioner) | treaty ignored unless it covers states |

## ND.2c Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nd.local_wage_tax.exists` | [[FACT:nd.local_wage_tax.exists=False]] | 2026-01-01 | open | US-NDP52-001 (A.1, ND Legislative Council) | - |

## ND.3 Social insurance: unemployment, disability, paid leave and payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nd.sui.wage_base` | [[FACT:nd.sui.wage_base=46600]] USD | 2026-01-01 | 2026-12-31 | US-NDS5-012 (A.2, Job Service North Dakota) | 70% of statewide average annual wage, nearest 100; not derivable (average not published) |
| `nd.ui.rate.new_employer.positive` | [[FACT:nd.ui.rate.new_employer.positive=1.0]] percent | 2026-01-01 | 2026-12-31 | US-NDS5-012 (A.2, Job Service North Dakota) | negative balance [[FACT:nd.ui.rate.new_employer.negative=6.07]]; construction [[FACT:nd.ui.rate.new_employer.construction=9.67]] |
| `nd.ui.rate.new_employer.negative` | [[FACT:nd.ui.rate.new_employer.negative=6.07]] percent | 2026-01-01 | 2026-12-31 | US-NDS5-012 (A.2, Job Service North Dakota) | - |
| `nd.ui.rate.new_employer.construction` | [[FACT:nd.ui.rate.new_employer.construction=9.67]] percent | 2026-01-01 | 2026-12-31 | US-NDS5-012 (A.2, Job Service North Dakota) | - |
| `nd.ui.rate.positive.min` | [[FACT:nd.ui.rate.positive.min=0.07]] percent | 2026-01-01 | 2026-12-31 | US-NDS5-012 (A.2, Job Service North Dakota) | positive schedule 0.07-1.10 |
| `nd.ui.rate.positive.max` | [[FACT:nd.ui.rate.positive.max=1.1]] percent | 2026-01-01 | 2026-12-31 | US-NDS5-012 (A.2, Job Service North Dakota) | - |
| `nd.ui.rate.negative.max` | [[FACT:nd.ui.rate.negative.max=9.67]] percent | 2026-01-01 | 2026-12-31 | US-NDS5-012 (A.2, Job Service North Dakota) | negative schedule [[FACT:nd.ui.rate.new_employer.negative=6.07]]-[[FACT:nd.ui.rate.negative.max=9.67]] |
| `nd.sui.employee.rate` | [[FACT:nd.sui.employee.rate=0]] percent | 2026-01-01 | open | US-NDS5-009 (A.1, ND Legislative Council) | may not be deducted |
| `nd.sui.wage_base.other_state_credit` | [[FACT:nd.sui.wage_base.other_state_credit=True]] | 2026-01-01 | open | US-NDS5-009 (A.1, ND Legislative Council) | same employer; 52-04-03(1); no worked example |
| `nd.sdi_pfml.exists` | [[FACT:nd.sdi_pfml.exists=False]] | 2026-01-01 | open | US-NDP52-002 (A.1, ND Legislative Council) | 34-01-15.1 bars local mandates |

- Not configured in this release [[GAP:RQ-084]]: The 2027 unemployment wage base and rates and the 2027 withholding booklet are not yet published.

## ND.4 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nd.payslip.items` | [[FACT:nd.payslip.items=check stub or pay voucher each pay period: hours worked, rate, required state/federal deductions, authorized deductions]] | 2012-10-01 | open | US-NDS5-007 (A.1, ND Legislative Council (NDAC; Department of Labor and Human Rights rule)) | NDAC 46-02-07-02(10); supersedes the "no provision" reading in US-ND-003 / US-MQ-48 part 6 |

- Not configured in this release [[GAP:RQ-085]]: No ND rule found on electronic pay-statement delivery or payroll record retention.

## ND.5 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nd.report.form306.due` | [[FACT:nd.report.form306.due=Apr 30; Jul 31; Oct 31; Jan 31 (zero returns required)]] | 2026-01-01 | open | US-NDS5-002 (A.2, ND Office of State Tax Commissioner) | annual option if prior-year < 1,000 |
| `nd.report.wh.efile_threshold` | [[FACT:nd.report.wh.efile_threshold=1000]] USD | 2026-01-01 | open | US-NDS5-002 (A.2, ND Office of State Tax Commissioner) | prior-year withholding |
| `nd.report.form307.due` | [[FACT:nd.report.form307.due=Jan 31; W-2 e-file mandatory (EFW2)]] | 2026-01-01 | open | US-NDS5-002 (A.2, ND Office of State Tax Commissioner) | - |
| `nd.newhire.report_days` | [[FACT:nd.newhire.report_days=20]] days | 2026-01-01 | open | US-NDS5-013 (A.2, ND Department of Health and Human Services (Child Support)) | incl. health insurance offered |

## ND.6 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nd.leave.pto.payout_at_separation` | [[FACT:nd.leave.pto.payout_at_separation=True]] | 2012-10-01 | open | US-NDS5-007 (A.1, ND Legislative Council (NDAC; Department of Labor and Human Rights rule)) | withholdable on quit only with notice at hire + <1 year service + <5 days notice (US-NDS5-005) |
| `nd.leave.sick.state_statute.exists` | [[FACT:nd.leave.sick.state_statute.exists=False]] | 2026-01-01 | open | US-NDP52-002 (A.1, ND Legislative Council) | - |

## ND.7 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nd.final_pay.rule` | [[FACT:nd.final_pay.rule=next regular payday (discharge, resignation, suspension)]] | 2026-01-01 | open | US-NDS5-005 (A.1, ND Legislative Council) | penalty daily wage up to 30 days |
| `nd.term.iwo.notice_days` | [[FACT:nd.term.iwo.notice_days=7]] days | 2026-01-01 | open | US-NDS5-016 (A.3, ND Department of Health and Human Services (Child Support)) | - |

- Not configured in this release [[GAP:RQ-086]]: UI separation notice, state WARN and child-labour hours (34-07) not established from an official source.

## ND.8 Benefits in kind and taxable wages

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nd.bik.conformity` | [[FACT:nd.bik.conformity=ND taxable income = federal; withholding wages = IRC 3401]] | 2026-01-01 | open | US-NDS5-004 (A.1, ND Legislative Council) | - |

## ND.9 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nd.garn.creditor.max_percent` | [[FACT:nd.garn.creditor.max_percent=25]] percent | 2026-01-01 | open | US-NDS5-008 (A.1, ND Legislative Council) | or excess over 40x FMW (290.00/week); minus 20.00/week per resident dependent |
| `nd.garn.consumer.dependent_reduction.weekly` | [[FACT:nd.garn.consumer.dependent_reduction.weekly=20.0]] USD | 2026-01-01 | open | US-NDS5-008 (A.1, ND Legislative Council) | - |
| `nd.garn.iwo.employer_fee.monthly` | [[FACT:nd.garn.iwo.employer_fee.monthly=3.0]] USD | 2026-01-01 | open | US-NDS5-014 (A.3, ND Department of Health and Human Services (Child Support)) | remit within 7 business days |
| `nd.garn.iwo.lump_sum.threshold` | [[FACT:nd.garn.iwo.lump_sum.threshold=1000]] USD | 2026-01-01 | open | US-NDS5-015 (A.3, ND Department of Health and Human Services (Child Support)) | notify Child Support; release half, hold half 30 days |

## ND.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nd.prevailing_wage.exists` | [[FACT:nd.prevailing_wage.exists=False]] | 2026-01-01 | open | US-NDP51-003 (A.2, US Department of Labor Wage and Hour Division) | U.S. DOL state prevailing wage table. |

Rules:

- No state prevailing-wage law. Federal Davis-Bacon applies to federal projects. (US-NDP51-003)

- Not configured in this release [[GAP:RQ-087]]: The absence of a state prevailing-wage law rests on a summary of the US Department of Labor state table only.

## ND.11 Indexation

Indexation of each value is stated in the note of the value concerned.

## ND.12 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `nd.data.breach.ag_threshold` | [[FACT:nd.data.breach.ag_threshold=250]] | 2026-01-01 | open | US-NDS5-017 (A.1, ND Legislative Council) | persons affected |

Rules:

- No pay-statement SSN-truncation rule was found.

## ND.13 Live legal change

No North Dakota rule is configured in this domain; the federal treatment in Annex FED applies.

## ND.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## ND.15 Special populations

- Domestic / household: Casual babysitters exempt from minimum wage. (US-NDS5-002, US-NDS5-011, US-NDS5-007)
- Agricultural: Overtime exempt. (US-NDS5-002, US-NDS5-011, US-NDS5-007)
- Minors: Same minimum wage, no youth subminimum. (US-NDS5-007, US-NDS5-010)
- Tipped: Advance notice and records required; Tip pool by vote of tipped employees. (US-NDS5-007)
- Clergy / religious: UI excludes ministers, religious orders and church organisations; Withholding follows federal (no state rule beyond federal). (US-NDS5-010, US-NDS5-002)
- Nonresident aliens: ND withholding on a separate W-4 (Single, no Exempt); Treaty exemption ignored unless it covers states. (US-NDS5-002)
- Statutory employees: UI excludes commission-only insurance, real estate and securities agents; Otherwise no state rule beyond federal. (US-NDS5-010)
- Government employees: Covered by minimum wage and withholding (the state is an "employer"). (US-NDS5-006, US-NDS5-007, US-NDS5-002)
- Military spouses / military pay: NDW-M exemption; No withholding on deductible military pay unless requested. (US-NDS5-002, US-NDS5-004)
- Tribal members: Exempt when enrolled, living on a reservation and working there. (US-NDS5-002)
- Not configured in this release [[GAP:RQ-088]]: Thresholds, amounts or conditions for these populations are stated in the sources read without a confirmed value record and are not configured from this annex: Domestic / household; Agricultural; Minors; Tipped; Students; Government employees.

## ND.16 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## ND.S Sources

| Source | Authority |
|---|---|
| US-NDP51-003 | US Department of Labor Wage and Hour Division |
| US-NDP52-001 | ND Legislative Council |
| US-NDP52-002 | ND Legislative Council |
| US-NDS5-001 | ND Office of State Tax Commissioner |
| US-NDS5-002 | ND Office of State Tax Commissioner |
| US-NDS5-004 | ND Legislative Council |
| US-NDS5-005 | ND Legislative Council |
| US-NDS5-006 | ND Legislative Council |
| US-NDS5-007 | ND Legislative Council (NDAC; Department of Labor and Human Rights rule) |
| US-NDS5-008 | ND Legislative Council |
| US-NDS5-009 | ND Legislative Council |
| US-NDS5-012 | Job Service North Dakota |
| US-NDS5-013 | ND Department of Health and Human Services (Child Support) |
| US-NDS5-014 | ND Department of Health and Human Services (Child Support) |
| US-NDS5-015 | ND Department of Health and Human Services (Child Support) |
| US-NDS5-016 | ND Department of Health and Human Services (Child Support) |
| US-NDS5-017 | ND Legislative Council |

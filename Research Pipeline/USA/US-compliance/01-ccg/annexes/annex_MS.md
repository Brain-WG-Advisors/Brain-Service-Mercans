# Annex MS: Mississippi

United States Country Configuration Guide, jurisdiction annex MS. Tax year 2026; currency USD (two decimal places).

## MS.0 Scope of this annex

This annex holds the Mississippi layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in Annex FED, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and Form 1099-NEC are out of scope. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register (00-official-sources/legal-basis-register.csv), with the authority and address listed in section MS.20 (the source address is held in the register row). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

## MS.1 Jurisdiction layer

| Item | Value |
|---|---|
| Annex tier | T3 |
| Basis | State withholding verified [US-MSPIT-001/-002] |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

## MS.2 Configuration decisions

- Mississippi has no state minimum wage ([[FACT:ms.labour.minwage.state.exists=False]]) and no state overtime rule, and it pre-empts local wage and leave mandates ([[FACT:ms.local_mandates.preempted=True]]); federal rules apply (Annex FED).
- The 2026 withholding rate is [[FACT:ms.pit.rate.flat=4.0]] percent. The [[FACT:ms.pit.rate.flat=3.75]] percent rate from 2027 is enacted for the annual liability only; do not apply it to withholding until the Department of Revenue publishes the 2027 tables.
- Residents are withheld on all wages except to the extent another state withholds (`ms.pit.resident.other_state_rule`).
- The formula and the wage-bracket table are both authorised and can differ by rounding.

## MS.3 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ms.labour.minwage.state.exists` | [[FACT:ms.labour.minwage.state.exists=False]] | 2009-07-24 | open | US-MSS5-010 (A.2, U.S. Department of Labor Wage and Hour Division) | no state law; FLSA [[FACT:fed.minwage.hourly=7.25]] for covered employers (Annex FED) |
| `ms.local_mandates.preempted` | [[FACT:ms.local_mandates.preempted=True]] | 2013-07-01 | open | US-MSS5-009 (A.1, Mississippi Legislature) | 17-1-51 bars local minimum/living wage and local paid-leave mandates |
| `ms.labour.overtime.state_rule` | [[FACT:ms.labour.overtime.state_rule=none (FLSA only)]] | 2026-01-01 | open | US-MSS5-016 (A.1, Mississippi Legislature) | negative rests on DOL table and measure sweep; Code full text not searched |
| `ms.labour.pay_frequency.scope` | [[FACT:ms.labour.pay_frequency.scope=manufacturers 50+ employing public labor: biweekly or semimonthly; public service corporations: semimonthly]] | 2026-01-01 | open | US-MSS5-015 (A.2, U.S. Department of Labor Wage and Hour Division) | 71-1-35 via DOL WHD summary; statute text not read |

## MS.4 State income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ms.pit.rate.zero_band.ceiling` | [[FACT:ms.pit.rate.zero_band.ceiling=10000]] USD | 2026-01-01 | 2026-12-31 | US-MSS5-001 (A.1, Mississippi Legislature) | 0% on first 10,000 of taxable income |
| `ms.pit.rate.flat` | [[FACT:ms.pit.rate.flat=4.0]] percent | 2026-01-01 | 2026-12-31 | US-MSS5-001 (A.1, Mississippi Legislature) | above 10,000; 3.75% enacted for 2027 (2025 HB 1) but withholding tables not published |
| `ms.pit.rate.flat` | [[FACT:ms.pit.rate.flat=3.75]] percent | 2027-01-01 | open | US-MSS5-001 (A.1, Mississippi Legislature) | enacted liability rate; withholding change waits for DOR 2027 tables (not published) |
| `ms.wh.method` | [[FACT:ms.wh.method=AGP=pay x periods; TI=AGP-(EX+STDED); TAX=(TI-10,000) x 4%; PWT=TAX/periods rounded to whole dollar]] | 2026-01-01 | 2026-12-31 | US-MSS5-003 (A.2, Mississippi Department of Revenue) | formula = oracle; tables built at bracket upper bound; formula vs table may differ by 1 USD, both authorised (US-MSS5-004) |
| `ms.pit.std_deduction.single` | [[FACT:ms.pit.std_deduction.single=2300]] USD | 2026-01-01 | open | US-MSS5-003 (A.2, Mississippi Department of Revenue) | statutory, unchanged since 2000 |
| `ms.pit.std_deduction.head_of_family` | [[FACT:ms.pit.std_deduction.head_of_family=3400]] USD | 2026-01-01 | open | US-MSS5-003 (A.2, Mississippi Department of Revenue) | - |
| `ms.pit.std_deduction.married` | [[FACT:ms.pit.std_deduction.married=4600]] USD | 2026-01-01 | open | US-MSS5-003 (A.2, Mississippi Department of Revenue) | B (married both working) 2,300 |
| `ms.pit.exemption.single` | [[FACT:ms.pit.exemption.single=6000]] USD | 2026-01-01 | open | US-MSS5-002 (A.2, Mississippi Department of Revenue) | Form 89-350 |
| `ms.pit.exemption.married` | [[FACT:ms.pit.exemption.married=12000]] USD | 2026-01-01 | open | US-MSS5-002 (A.2, Mississippi Department of Revenue) | split in 500 multiples when both employed |
| `ms.pit.exemption.head_of_family` | [[FACT:ms.pit.exemption.head_of_family=9500]] USD | 2026-01-01 | open | US-MSS5-002 (A.2, Mississippi Department of Revenue) | - |
| `ms.pit.exemption.dependent` | [[FACT:ms.pit.exemption.dependent=1500]] USD | 2026-01-01 | open | US-MSS5-002 (A.2, Mississippi Department of Revenue) | also each age-65 or blind exemption |
| `ms.wh.certificate` | [[FACT:ms.wh.certificate=no 89-350: single, zero exemption]] | 2026-01-01 | open | US-MSS5-002 (A.2, Mississippi Department of Revenue) | federal W-4 not accepted |
| `ms.pit.oracle.example_1.withholding` | [[FACT:ms.pit.oracle.example_1.withholding=9]] USD | 2026-01-01 | 2026-12-31 | US-MSS5-003 (A.2, Mississippi Department of Revenue) | Table A single weekly 450-460, 0 exemption: (460x52-2,300-10,000)x4%/52=[[FACT:ms.oracle.weekly_460_0ex.withholding=8.94]] -> 9; 8/8 test rows matched at upper bound |
| `ms.pit.supplemental.method` | [[FACT:ms.pit.supplemental.method=aggregate; no fixed flat rate (top rate 4% allowed where aggregation over-withholds)]] | 2026-01-01 | 2026-12-31 | US-MSS5-002 (A.2, Mississippi Department of Revenue) | - |

- ⚠️ RESEARCH-GAP (non-blocking, `ms.pit.tables.next_year`): The 2027 withholding tables and formula at the [[FACT:ms.pit.rate.flat=3.75]] percent rate are not yet published. To close: DOR withholding page listing Pub 89-700 for 2027 and the "Computer Payroll Accounting - For Periods in 2027" flowchart (re-check December 2026).

## MS.5 Non-residents, residents working elsewhere and reciprocity

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ms.pit.nonresident.threshold` | [[FACT:ms.pit.nonresident.threshold=none if annual MS earnings below the filing-status standard deduction]] | 2026-01-01 | open | US-MSS5-019 (A.3, Mississippi Department of Revenue) | earnings-ratio split from day 1 |
| `ms.pit.resident.other_state_rule` | [[FACT:ms.pit.resident.other_state_rule=withhold MS on all wages except to the extent another state withholds]] | 2026-01-01 | open | US-MSS5-004 (A.1, Mississippi Department of Revenue (filed with Secretary of State)) | commuter to no-tax state: MS on all wages; correction to MULTI 2.2 |
| `ms.reciprocity.states` | [[FACT:ms.reciprocity.states=none]] | 2026-01-01 | open | US-MSS5-019 (A.3, Mississippi Department of Revenue) | MULTI matrix |

## MS.6 Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ms.local_wage_tax.exists` | [[FACT:ms.local_wage_tax.exists=False]] | 2026-01-01 | open | US-MSP10-001 (A.2, Mississippi Department of Revenue) | - |

## MS.7 Unemployment insurance, disability and paid-leave contributions, other payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ms.sui.wage_base` | [[FACT:ms.sui.wage_base=14000]] USD | 2011-01-01 | open | US-MSS5-011 (A.1, Mississippi Department of Employment Security (compilation of statute)) | fixed in statute; other-state UC wages count (71-5-353(4)) |
| `ms.sui.wage_base.other_state_credit` | [[FACT:ms.sui.wage_base.other_state_credit=True]] | 2011-01-01 | open | US-MSS5-011 (A.1, Mississippi Department of Employment Security (compilation of statute)) | - |
| `ms.ui.rate.new_employer.year1` | [[FACT:ms.ui.rate.new_employer.year1=1.0]] percent | 2011-01-01 | open | US-MSS5-011 (A.1, Mississippi Department of Employment Security (compilation of statute)) | 1.10 year 2, 1.20 from year 3 |
| `ms.ui.rate.new_employer.year2` | [[FACT:ms.ui.rate.new_employer.year2=1.1]] percent | 2011-01-01 | open | US-MSS5-011 (A.1, Mississippi Department of Employment Security (compilation of statute)) | - |
| `ms.ui.rate.new_employer.year3` | [[FACT:ms.ui.rate.new_employer.year3=1.2]] percent | 2011-01-01 | open | US-MSS5-011 (A.1, Mississippi Department of Employment Security (compilation of statute)) | - |
| `ms.sui.employer.rate.max` | [[FACT:ms.sui.employer.rate.max=5.4]] percent | 2011-01-01 | open | US-MSS5-011 (A.1, Mississippi Department of Employment Security (compilation of statute)) | range 0.0-5.4 |
| `ms.sui.employee.rate` | [[FACT:ms.sui.employee.rate=0]] percent | 2011-01-01 | open | US-MSS5-011 (A.1, Mississippi Department of Employment Security (compilation of statute)) | may not be deducted from wages |
| `ms.ui.workforce_training.rate` | [[FACT:ms.ui.workforce_training.rate=0.2]] percent | 2017-01-01 | open | US-MSP51-004 (A.1, Mississippi Department of Employment Security) | WET 0.15+OWD 0.01+MS Works 0.04; 2026 application NOT confirmed |

- ⚠️ RESEARCH-GAP (non-blocking, `ms.ui.workforce_training.applies`): Whether the Workforce Investment and Training contribution applies in 2026 is not confirmed; the agency says it 'might be applicable'. To close: MDES 2026 rate notice (UI-1/rate letter) or the 71-5-355 trigger text in a post-2023 Code edition.
- ⚠️ RESEARCH-GAP (non-blocking, `ms.sdi_pfml.exists`): The statement that Mississippi has no disability or paid-family-leave contribution rests on a source that cannot be used as a primary source; no verified source carries it. To close: An A.1/A.2 source (MDES or DOL TDI/PFML state list) registered as active.

## MS.8 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ms.payslip.statute.exists` | [[FACT:ms.payslip.statute.exists=False]] | 2026-01-01 | open | US-MSP9L-001 (A.3, Mississippi Department of Employment Security) | no MS pay-statement statute located (full-text Code search not possible) |

Rules:

- No MS statute requires a pay statement or itemised deductions. (US-OWN-006, US-MSP52-004)

## MS.9 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ms.report.wh.monthly_threshold.monthly_avg` | [[FACT:ms.report.wh.monthly_threshold.monthly_avg=300]] USD | 2026-01-01 | open | US-MSS5-019 (A.3, Mississippi Department of Revenue) | else quarterly; due 15th of following month |
| `ms.report.wh.efile_threshold` | [[FACT:ms.report.wh.efile_threshold=20000]] USD | 2026-01-01 | open | US-MSS5-019 (A.3, Mississippi Department of Revenue) | e-file/e-pay mandatory at 20,000 liability in any period |
| `ms.report.w2.due` | [[FACT:ms.report.w2.due=Jan 31; no extensions]] | 2026-01-01 | open | US-MSS5-005 (A.2, Mississippi Department of Revenue) | EFW2 RS record state code 28; mandatory electronic for 10+ W-2 |
| `ms.report.w2.efile_threshold` | [[FACT:ms.report.w2.efile_threshold=10]] | 2026-01-01 | open | US-MSS5-005 (A.2, Mississippi Department of Revenue) | - |
| `ms.report.ui.quarterly_due` | [[FACT:ms.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] | 2026-01-01 | open | US-MSS5-012 (A.2, Mississippi Department of Employment Security) | UI-2/UI-3; zero report required |
| `ms.newhire.report_days` | [[FACT:ms.newhire.report_days=15]] days | 1998-10-01 | open | US-MSS5-006 (A.3, Mississippi Department of Human Services (State Directory of New Hires)) | rehire after 60+ days; DOB, gender, salary, pay frequency, medical-insurance eligibility |

- ⚠️ RESEARCH-GAP (non-blocking, `ms.report.w2.spec.next_year`): Pub 89-145 for TY2026 (filed January 2027) not yet seen; Rev 10/25 on file. To close: Pub 89-145 Rev. 10/26.

## MS.10 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ms.leave.sick.state_statute.exists` | [[FACT:ms.leave.sick.state_statute.exists=False]] | 2013-07-01 | open | US-MSS5-009 (A.1, Mississippi Legislature) | local mandates preempted |

Rules:

- Sick pay under a wage-continuation plan is wages for withholding. (US-MSS5-002)

## MS.11 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ms.term.w2_after_termination.days` | [[FACT:ms.term.w2_after_termination.days=30]] days | 2026-01-01 | open | US-MSS5-004 (A.1, Mississippi Department of Revenue (filed with Secretary of State)) | - |

- ⚠️ RESEARCH-GAP (non-blocking, `ms.term.final_pay.timing`): No MS final-pay statute located; Code full-text search not possible. To close: Official Code text (Lexis public access) search for final wages.

## MS.12 Taxable wages and benefits in kind

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ms.bik.section125.excluded` | [[FACT:ms.bik.section125.excluded=True]] | 2026-01-01 | open | US-MSS5-004 (A.1, Mississippi Department of Revenue (filed with Secretary of State)) | also 127, 129; 401(k)/403(b)/457 deferrals excluded |
| `ms.bik.work_and_save_roth` | [[FACT:ms.bik.work_and_save_roth=voluntary employer payroll-deduction Roth IRA (HB 4073)]] | 2026-07-01 | open | US-MSS5-017 (A.1, Mississippi Legislature) | auto-enrol with opt-out, escalation to 8%; start by 2028-08-01; post-tax, opt-in employers only |

- ⚠️ RESEARCH-GAP (non-blocking, `ms.bik.conformity.hsa_transit_gtl`): HSA, transit (132(f)) and group-term life MS treatment not confirmed. To close: Miss. Code 27-7-15 / 27-7-17 current text or MDOR Form 80-100 instructions (2025).

## MS.13 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ms.garn.iwo.employer_fee.monthly` | [[FACT:ms.garn.iwo.employer_fee.monthly=2.0]] USD | 2026-01-01 | open | US-MSS5-008 (A.3, Mississippi Department of Human Services, Division of Child Support Enforcement) | plus 5.00 administrative fee withheld and sent to SDU; guide dated 2020 |
| `ms.garn.iwo.remit_working_days` | [[FACT:ms.garn.iwo.remit_working_days=7]] days | 2026-01-01 | open | US-MSS5-008 (A.3, Mississippi Department of Human Services, Division of Child Support Enforcement) | - |
| `ms.garn.iwo.lump_sum.notice_threshold` | [[FACT:ms.garn.iwo.lump_sum.notice_threshold=500]] USD | 2026-01-01 | open | US-MSS5-008 (A.3, Mississippi Department of Human Services, Division of Child Support Enforcement) | notify MDHS 45 days before; hold up to 30 days |

Rules:

- Under-collected withholding may be recovered from later wages. (US-MSS5-004)

- ⚠️ RESEARCH-GAP (non-blocking, `ms.garn.consumer.limits`): Creditor garnishment 85-3-4 text not read (Lexis-only Code); secondary lead only. To close: Official Code text via the Lexis public-access URL in a browser pass.

## MS.14 Prevailing wage and collective agreements

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ms.prevailing_wage.exists` | [[FACT:ms.prevailing_wage.exists=False]] | 2023-01-01 | open | US-MSP51-001 (A.2, US Department of Labor, Wage and Hour Division) | Davis-Bacon on federal work only |

## MS.15 Indexation

Rules:

- Nothing in MS payroll law is indexed annually.
- The only annual variables are each employer's SUI experience rate and the workforce levy decision (rate notice).

## MS.16 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `ms.records.retention_years` | [[FACT:ms.records.retention_years=3]] years | 2026-01-01 | open | US-MSS5-019 (A.3, Mississippi Department of Revenue) | DOR |
| `ms.data.breach_notice.exists` | [[FACT:ms.data.breach_notice.exists=True]] | 2011-07-01 | open | US-MSS5-018 (A.1, Mississippi Legislature) | - |

Rules:

- No MS rule truncates the SSN on pay statements; the full SSN is required on the W-2. (US-MSS5-002)

## MS.17 Legal change in force or enacted

No Mississippi rule is configured in this domain; the federal treatment in Annex FED applies.

## MS.18 Special populations

- Domestic / household workers: Exempt from MS income-tax withholding (voluntary by agreement). (US-MSS5-004, US-MSS5-019, US-MSS5-011)
- Agricultural: Exempt from MS withholding (voluntary). (US-MSS5-004, US-MSS5-011)
- Tipped employees: Federal tip credit only (no state minimum wage); Tips paid directly by customers: no MS withholding; Tips paid through the employer: withheld. (US-MSS5-010, US-MSS5-019)
- Clergy / religious: Ministers' pay is exempt from MS withholding and excluded from UI. Parsonage rental allowance is excludable. (US-MSS5-004, US-MSS5-011)
- Students: UI excludes students employed by their own school. (US-MSS5-011, US-MSS5-004)
- Statutory employees: No state rule beyond federal (DOR follows federal employee/contractor rules). (US-MSS5-019)
- Government employees: State, counties and cities are withholding employers; PERS contributions are excluded from income. (US-MSS5-002, US-MSS5-004, US-MSS5-001)
- Corporate officers: Employees for withholding. (US-MSS5-019)
- ⚠️ RESEARCH-GAP (non-blocking, `ms.special_populations.thresholds`): thresholds, amounts or conditions for these populations are stated in the research without a confirmed value record and are not configured from this annex: Domestic / household workers; Agricultural; Minors; Students; Nonresident aliens; Government employees; Native Americans on a reservation. To close: one confirmed value per threshold, with its source row.

## MS.19 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## MS.20 Sources

| Source | Authority |
|---|---|
| US-MSP10-001 | Mississippi Department of Revenue |
| US-MSP51-001 | US Department of Labor, Wage and Hour Division |
| US-MSP51-004 | Mississippi Department of Employment Security |
| US-MSP9L-001 | Mississippi Department of Employment Security |
| US-MSS5-001 | Mississippi Legislature |
| US-MSS5-002 | Mississippi Department of Revenue |
| US-MSS5-003 | Mississippi Department of Revenue |
| US-MSS5-004 | Mississippi Department of Revenue (filed with Secretary of State) |
| US-MSS5-005 | Mississippi Department of Revenue |
| US-MSS5-006 | Mississippi Department of Human Services (State Directory of New Hires) |
| US-MSS5-008 | Mississippi Department of Human Services, Division of Child Support Enforcement |
| US-MSS5-009 | Mississippi Legislature |
| US-MSS5-010 | U.S. Department of Labor Wage and Hour Division |
| US-MSS5-011 | Mississippi Department of Employment Security (compilation of statute) |
| US-MSS5-012 | Mississippi Department of Employment Security |
| US-MSS5-015 | U.S. Department of Labor Wage and Hour Division |
| US-MSS5-016 | Mississippi Legislature |
| US-MSS5-017 | Mississippi Legislature |
| US-MSS5-018 | Mississippi Legislature |
| US-MSS5-019 | Mississippi Department of Revenue |

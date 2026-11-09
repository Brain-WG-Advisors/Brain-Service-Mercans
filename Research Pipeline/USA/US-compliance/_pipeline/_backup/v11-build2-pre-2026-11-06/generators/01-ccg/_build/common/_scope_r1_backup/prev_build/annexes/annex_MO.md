# Annex MO: Missouri


United States Country Configuration Guide, jurisdiction annex MO. Tax year 2026; currency USD (two decimal places).

**Scope of this annex.**

This annex holds the Missouri layer only. The federal layer (federal income tax withholding, Social Security and Medicare, federal unemployment tax, Forms W-4, W-2, 941 and 940) is in Annex FED, and the rules for employees who live and work in different jurisdictions (sourcing, resident credits, reciprocity mechanics) are in Annex MULTI. Neither is repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. The pay statement is issued in English.

In every table, *Valid from* and *Valid to* give the period in which the value applies (*open* means no end date has been published), and *Source* is the identifier of the row in the legal-basis register, with the authority and address listed in section MO.S (the source address is held in the register row). Items marked as a research gap are not yet confirmed and must not be configured from this annex.

**Jurisdiction layer.**

| Item | Value |
|---|---|
| Annex tier | T4 (verified) |
| Basis | Form 4282 Rev. 03-2026 [US-MOPIT-001]; St. Louis City 1% earnings tax withheld by the employer, Kansas City 1% earnings tax [US-MOP52-006/-007] |

Tier key: T1 = no state wage tax (unemployment insurance and levies only); T3 = state withholding with no local layer remitted separately; T4 = a local layer remitted to a separate local authority on its own return.

**Configuration decisions.**

- There is no state paid sick leave in 2026 ([[FACT:mo.leave.sick.state_statute.exists=False]]); the earlier ballot measure was repealed. Do not model an accrual.
- The minimum wage [[FACT:mo.minwage.hourly=15.0]] USD has no annual index step ([[FACT:mo.labour.minwage.indexation.active=False]]); only a federal increase can change it.
- Unemployment wages include 401(k) deferrals ([[FACT:mo.sui.wages.401k_included=True]]) and exclude cafeteria-plan salary reductions, which differs from the state income-tax base.
- Local layer (tier T4): the St. Louis and Kansas City earnings taxes ([[FACT:mo.pit.local.st_louis.earnings_tax.rate=1]] and [[FACT:mo.pit.local.kansas_city.earnings_tax.rate=1]] percent) are filed with the cities, separately from the state return.
- A constitutional ballot measure of November 2026 is not enacted law and has no withholding effect for 2026 or 2027.

## MO.1 Employment and labour code

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mo.minwage.hourly` | [[FACT:mo.minwage.hourly=15.0]] USD | 2026-01-01 | open | US-MOS5-002 (A.1, Missouri Revisor of Statutes) | or federal rate if higher; no indexation after 2026 (H.B. 567); second document family US-MOS5-010 |
| `mo.labour.minwage.indexation.active` | [[FACT:mo.labour.minwage.indexation.active=False]] | 2026-01-01 | open | US-MOS5-002 (A.1, Missouri Revisor of Statutes) | indexation stopped 2024-12-31; no 2027 step enacted |
| `mo.labour.tip_credit.cash_wage.min_ratio` | [[FACT:mo.labour.tip_credit.cash_wage.min_ratio=50]] percent | 2006-12-07 | open | US-MOS5-005 (A.1, Missouri Revisor of Statutes) | employer pays at least 50% of minimum (7.50 in 2026) and tops up to 15.00 |
| `mo.minwage.tipped.cash_wage` | [[FACT:mo.minwage.tipped.cash_wage=7.5]] USD | 2026-01-01 | 2026-12-31 | US-MOS5-010 (A.2, Missouri Department of Labor and Industrial Relations, Division of Labor Standards) | 15.00 x 0.5 |
| `mo.labour.minwage.small_retail_exemption.gross_volume` | [[FACT:mo.labour.minwage.small_retail_exemption.gross_volume=500000]] USD | 2006-12-07 | open | US-MOS5-010 (A.2, Missouri Department of Labor and Industrial Relations, Division of Labor Standards) | retail/service businesses under 500,000 annual gross volume excluded |
| `mo.overtime.weekly_threshold_hours` | [[FACT:mo.overtime.weekly_threshold_hours=40]] hours | 2008-08-28 | open | US-MOS5-022 (A.3, Missouri Department of Labor and Industrial Relations, Division of Labor Standards) | 1.5x; amusement/recreation 52 h; no daily overtime |
| `mo.overtime.premium.multiplier` | [[FACT:mo.overtime.premium.multiplier=1.5]] ratio | 2008-08-28 | open | US-MOS5-011 (A.1, Missouri Revisor of Statutes) | - |
| `mo.labour.pay_frequency.corporations` | [[FACT:mo.labour.pay_frequency.corporations=at least semimonthly, within 16 days of period close]] | 1955-08-28 | open | US-MOP52-002 (A.1, Missouri Revisor of Statutes) | 290.080 |

- Not configured in this release [[GAP:RQ-048]]: No Missouri direct-deposit/paycard consent or electronic pay-statement rule located.
- Not configured in this release [[GAP:RQ-049]]: Child-labour hours and work certificates not read.

## MO.2 Income tax withholding

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mo.wh.method` | [[FACT:mo.wh.method=annualise; minus standard deduction; 8 brackets of 1,348; / periods; round to whole dollar]] | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | Form 4282 Rev. 03-2026 |
| `mo.pit.std_deduction.single` | [[FACT:mo.pit.std_deduction.single=16100]] USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | also married with working spouse and MFS |
| `mo.pit.std_deduction.married_nonworking_spouse` | [[FACT:mo.pit.std_deduction.married_nonworking_spouse=32200]] USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | MO W-4 line 1 check box |
| `mo.pit.std_deduction.head_of_household` | [[FACT:mo.pit.std_deduction.head_of_household=24150]] USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | - |
| `mo.pit.bracket.width` | [[FACT:mo.pit.bracket.width=1348]] USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | CPI-indexed (143.011(5)); 1,000 x 1.348 |
| `mo.pit.bracket.1.rate` | [[FACT:mo.pit.bracket.1.rate=0]] percent | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | 0-[[FACT:mo.pit.bracket.width=1,348]] |
| `mo.pit.bracket.2.rate` | [[FACT:mo.pit.bracket.2.rate=2]] percent | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | [[FACT:mo.pit.bracket.width=1,348]]-2,696 |
| `mo.pit.bracket.3.rate` | [[FACT:mo.pit.bracket.3.rate=2.5]] percent | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | 2,696-4,044 |
| `mo.pit.bracket.4.rate` | [[FACT:mo.pit.bracket.4.rate=3]] percent | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | 4,044-5,392 |
| `mo.pit.bracket.5.rate` | [[FACT:mo.pit.bracket.5.rate=3.5]] percent | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | 5,392-6,740 |
| `mo.pit.bracket.6.rate` | [[FACT:mo.pit.bracket.6.rate=4]] percent | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | 6,740-8,088 |
| `mo.pit.bracket.7.rate` | [[FACT:mo.pit.bracket.7.rate=4.5]] percent | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | 8,088-[[FACT:mo.pit.bracket.8.floor=9,436]] |
| `mo.pit.bracket.8.rate` | [[FACT:mo.pit.bracket.8.rate=4.7]] percent | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | Applies over [[FACT:mo.pit.bracket.8.floor=9,436]]; reconciles to the statutory top rate after the two statutory reductions (US-MOS5-018). |
| `mo.pit.bracket.8.floor` | [[FACT:mo.pit.bracket.8.floor=9436]] USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | - |
| `mo.pit.rounding` | [[FACT:mo.pit.rounding=per-period tax rounded to whole dollar (49c down, 50c up)]] | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | - |
| `mo.wh.certificate` | [[FACT:mo.wh.certificate=no MO W-4: withhold at Single]] | 2025-01-01 | open | US-MOS5-020 (A.2, Missouri Department of Revenue) | MO W-4 Rev. 12-2024, no allowances |
| `mo.wh.supplemental.rate` | [[FACT:mo.wh.supplemental.rate=4.7]] percent | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | only when paid separately; aggregate if no tax withheld from regular wages |
| `mo.pit.household.withholding_required` | [[FACT:mo.pit.household.withholding_required=False]] | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | voluntary by agreement |
| `mo.pit.oracle.example_1.annual_tax` | [[FACT:mo.pit.oracle.example_1.annual_tax=707.81]] USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | Department of Revenue example, married, spouse works, wages 35,000: taxable income 18,900; the Department's rounded tax on the lower brackets plus 9,464 x [[FACT:mo.pit.bracket.8.rate=4.7]]% gives [[FACT:mo.pit.oracle.example_1.annual_tax=707.81]] a year and 59 a month. Unrounded lower brackets give 707.67; the annual residual disappears in period rounding. |
| `mo.pit.oracle.example_1.monthly_withholding` | [[FACT:mo.pit.oracle.example_1.monthly_withholding=59]] USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | - |

- Not configured in this release [[GAP:RQ-050]]: 2027 top rate and brackets not published (revenue trigger 143.011(4)).
- Not configured in this release [[GAP:RQ-051]]: Tie of the standard deductions to the federal amounts (143.131) not read.

## MO.2b Non-resident regime and reciprocity

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mo.reciprocity.states` | [[FACT:mo.reciprocity.states=none]] | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | - |

## MO.2c Local wage taxes

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mo.pit.local.st_louis.earnings_tax.rate` | [[FACT:mo.pit.local.st_louis.earnings_tax.rate=1]] percent | 2026-01-01 | open | US-MOP52-006 (A.2, City of St. Louis Collector of Revenue) | employees living or working in the City; renewal-vote status open |
| `mo.pit.local.st_louis.payroll_expense_tax.rate` | [[FACT:mo.pit.local.st_louis.payroll_expense_tax.rate=0.5]] percent | 2026-01-01 | open | US-MOP52-006 (A.2, City of St. Louis Collector of Revenue) | employer-paid |
| `mo.pit.local.kansas_city.earnings_tax.rate` | [[FACT:mo.pit.local.kansas_city.earnings_tax.rate=1]] percent | 2026-01-01 | open | US-MOP9W-001 (A.2, City of Kansas City, Missouri - Revenue Division) | Residents and nonresidents for work in KC; KC earnings tax page (1%). |

- Not configured in this release [[GAP:RQ-052]]: St. Louis and Kansas City earnings-tax April 2026 renewal votes not verified; RSMo 92.105-92.125 not read.

## MO.3 Social insurance: unemployment, disability, paid leave and payroll levies

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mo.sui.employee.rate` | [[FACT:mo.sui.employee.rate=0]] percent | 2026-01-01 | open | US-MOS5-013 (A.3, Missouri Department of Labor and Industrial Relations, Division of Employment Security) | no deduction from pay |
| `mo.sui.wages.401k_included` | [[FACT:mo.sui.wages.401k_included=True]] | 2026-01-01 | open | US-MOS5-013 (A.3, Missouri Department of Labor and Industrial Relations, Division of Employment Security) | 401(k) deferrals are unemployment wages; cafeteria-plan salary reductions are not. |
| `mo.sdi_pfml.exists` | [[FACT:mo.sdi_pfml.exists=False]] | 2026-01-01 | open | US-MOR3-001 (A.2, US Department of Labor, Women's Bureau) | no SDI/TDI/PFML |
| `mo.sui.wage_base` | [[FACT:mo.sui.wage_base=9000]] USD | 2026-01-01 | 2026-12-31 | US-MOP9W-002 (A.2, Missouri Department of Labor and Industrial Relations, Division of Employment Security) | 9,500-500 (>=650M branch of 288.036(2)), derived in US-MOS5-012 |
| `mo.sui.new_employer.rate` | [[FACT:mo.sui.new_employer.rate=2.376]] percent | 2026-01-01 | 2026-12-31 | US-MOB5-403 (A.2, Missouri DOLIR, Division of Employment Security) | a separate rate for 501(c)(3) employers; CRA -12% derived [[FACT:mo.sui.new_employer.rate=2.376]]/2.7 |
| `mo.sui.employer.rate.max` | [[FACT:mo.sui.employer.rate.max=6.0]] percent | 2026-01-01 | 2026-12-31 | US-MOP9W-002 (A.2, Missouri Department of Labor and Industrial Relations, Division of Employment Security) | plus CRA and max-rate surcharge (in steps, up to a statutory maximum) |

Rules:

- Agency: DOLIR Division of Employment Security (DES).

- Not configured in this release [[GAP:RQ-053]]: 288.036 text read has no wage-base credit for wages reported to another state; DES guide silent.

## MO.4 Pay statement

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mo.payslip.deduction_statement` | [[FACT:mo.payslip.deduction_statement=statement of total deductions at least monthly]] | 1955-08-28 | open | US-MOP52-002 (A.1, Missouri Revisor of Statutes) | 290.080; no itemised pay-statement statute |

## MO.5 Statutory reporting

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mo.report.mo941.monthly_threshold` | [[FACT:mo.report.mo941.monthly_threshold=500]] USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | in 2 of prior 12 months |
| `mo.report.mo941.quarter_monthly_threshold` | [[FACT:mo.report.mo941.quarter_monthly_threshold=9000]] USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | electronic within 3 banking days |
| `mo.report.w2.efile_threshold` | [[FACT:mo.report.w2.efile_threshold=250]] | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | EFW2 with RV record; due last day of January electronic |
| `mo.report.ui.quarterly_due` | [[FACT:mo.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] | 2026-01-01 | open | US-MOS5-013 (A.3, Missouri Department of Labor and Industrial Relations, Division of Employment Security) | MODES-4 on UInteract |
| `mo.newhire.report_days` | [[FACT:mo.newhire.report_days=20]] days | 2026-01-01 | 2026-12-31 | US-MOS5-001 (A.2, Missouri Department of Revenue) | to MO DOR; fields per 285.304 (US-MOS5-008) |

## MO.6 Leave

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mo.leave.sick.state_statute.exists` | [[FACT:mo.leave.sick.state_statute.exists=False]] | 2025-08-28 | open | US-MOS5-003 (A.1, Missouri Revisor of Statutes) | Prop A repealed by H.B. 567 |

Rules:

- Missouri has no PFML benefit program. (US-MOR3-001)
- No state job-protected illness leave exists beyond the federal FMLA. (US-MOS5-022)

## MO.7 Termination and final pay

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mo.final_pay.discharge` | [[FACT:mo.final_pay.discharge=day of discharge; penalty wages up to 60 days after 7-day written request]] | 1972-08-28 | open | US-MOS5-004 (A.1, Missouri Revisor of Statutes) | 290.110 |
| `mo.term.service_letter.days` | [[FACT:mo.term.service_letter.days=45]] days | 1982-08-28 | open | US-MOS5-009 (A.1, Missouri Revisor of Statutes) | corporations 7+ employees; 90+ days service |

## MO.8 Benefits in kind and taxable wages

No Missouri rule is configured in this domain; the federal treatment in Annex FED applies.

## MO.9 Deductions and garnishments

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mo.garn.creditor.max_percent` | [[FACT:mo.garn.creditor.max_percent=25]] percent | 1979-01-02 | open | US-MOS5-007 (A.1, Missouri Revisor of Statutes) | or excess over 30x FMW; 10% for Missouri-resident head of family |
| `mo.garn.consumer.head_of_family.max_rate` | [[FACT:mo.garn.consumer.head_of_family.max_rate=10]] percent | 1979-01-02 | open | US-MOS5-007 (A.1, Missouri Revisor of Statutes) | - |
| `mo.garn.iwo.employer_fee.monthly` | [[FACT:mo.garn.iwo.employer_fee.monthly=6]] USD | 2014-08-28 | open | US-MOS5-017 (A.1, Missouri Revisor of Statutes) | - |
| `mo.garn.iwo.remit_business_days` | [[FACT:mo.garn.iwo.remit_business_days=7]] days | 2014-08-28 | open | US-MOS5-017 (A.1, Missouri Revisor of Statutes) | - |

## MO.10 Collective agreements and prevailing wage

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mo.prevailing_wage.threshold` | [[FACT:mo.prevailing_wage.threshold=75000]] USD | 2018-08-28 | open | US-MOB5-401 (A.1, Missouri Revisor of Statutes) | projects of 75,000 or less excluded |

- Not configured in this release [[GAP:RQ-054]]: Certified-payroll form and filing (290.290) and current annual wage order not read.

## MO.11 Indexation

Indexation of each value is stated in the note of the value concerned.

## MO.12 Payroll data protection and records

| Item | Value | Valid from | Valid to | Source | Note |
|---|---|---|---|---|---|
| `mo.data.ssn.employee_number_prohibited` | [[FACT:mo.data.ssn.employee_number_prohibited=True]] | 2012-08-28 | open | US-MOS5-016 (A.1, Missouri Revisor of Statutes) | 407.1355 |
| `mo.records.retention_years` | [[FACT:mo.records.retention_years=3]] years | 2006-12-07 | open | US-MOB5-402 (A.1, Missouri Revisor of Statutes) | 290.520 |

## MO.13 Live legal change

No Missouri rule is configured in this domain; the federal treatment in Annex FED applies.

- Not configured in this release [[GAP:RQ-055]]: DOR/DES/DOLIR news pages 403; bulletin sweep partial.

## MO.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## MO.15 Special populations

- Domestic / household: Income-tax withholding not required (voluntary by agreement). (US-MOS5-001, US-MOS5-013, US-MOS5-014, US-MOS5-006)
- Agricultural: cash wages only. (US-MOS5-013, US-MOS5-014, US-MOS5-006)
- Minors: Entertainment-industry youth break rules apply. (US-MOS5-006, US-MOS5-022)
- Clergy / religious: UI excludes church employment and ministers in their ministry; Withholding follows federal (ministers' wages exempt from mandatory withholding under federal rules; no Missouri override found). (US-MOS5-014, US-MOS5-001)
- Students: Minimum wage excludes tuition-offset work. (US-MOS5-014, US-MOS5-006)
- Nonresident aliens: Withholding on Missouri-source work. (US-MOS5-001)
- Nonresidents (US): Fully withheld if all work is in MO. Partial work: MO W-4A percentage; No reciprocity. (US-MOS5-001)
- Military / military spouses: Active-duty income is exempt from withholding; MSRRA spouse exemption requires verification. (US-MOS5-001, US-MOS5-020)
- Statutory employees: No state rule beyond federal (wage definition follows federal). (US-MOS5-001)
- Not configured in this release [[GAP:RQ-056]]: Thresholds, amounts or conditions for these populations are stated in the sources read without a confirmed value record and are not configured from this annex: Domestic / household; Agricultural; Minors; Tipped; Students; Nonresident aliens; Government employees; Transport (rail, motor, air).

## MO.16 Language

- The pay statement and all filings are in English (owner decision US-OWN-006).

## MO.S Sources

| Source | Authority |
|---|---|
| US-MOB5-401 | Missouri Revisor of Statutes |
| US-MOB5-402 | Missouri Revisor of Statutes |
| US-MOB5-403 | Missouri DOLIR, Division of Employment Security |
| US-MOP52-002 | Missouri Revisor of Statutes |
| US-MOP52-006 | City of St. Louis Collector of Revenue |
| US-MOP9W-001 | City of Kansas City, Missouri - Revenue Division |
| US-MOP9W-002 | Missouri Department of Labor and Industrial Relations, Division of Employment Security |
| US-MOR3-001 | US Department of Labor, Women's Bureau |
| US-MOS5-001 | Missouri Department of Revenue |
| US-MOS5-002 | Missouri Revisor of Statutes |
| US-MOS5-003 | Missouri Revisor of Statutes |
| US-MOS5-004 | Missouri Revisor of Statutes |
| US-MOS5-005 | Missouri Revisor of Statutes |
| US-MOS5-007 | Missouri Revisor of Statutes |
| US-MOS5-009 | Missouri Revisor of Statutes |
| US-MOS5-010 | Missouri Department of Labor and Industrial Relations, Division of Labor Standards |
| US-MOS5-011 | Missouri Revisor of Statutes |
| US-MOS5-013 | Missouri Department of Labor and Industrial Relations, Division of Employment Security |
| US-MOS5-016 | Missouri Revisor of Statutes |
| US-MOS5-017 | Missouri Revisor of Statutes |
| US-MOS5-020 | Missouri Department of Revenue |
| US-MOS5-022 | Missouri Department of Labor and Industrial Relations, Division of Labor Standards |

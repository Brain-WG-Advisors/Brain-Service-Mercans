# Annex OH: Ohio


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T4 - local layer remitted to the locality on its own return** (build manifest, tier rationale). Ohio municipal income tax, ORC 718.03 [US-OHP52-003].

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## OH.1 Employment and labour code

- **Minimum wage (Ohio Const. art. II s.34a) [US-OHS5-005, US-OHS5-004].** 2026: [[FACT:oh.minwage.hourly=11.00]] USD per hour non-tipped; tipped cash wage [[FACT:oh.minwage.tipped.cash_wage=5.50]] USD. Employers grossing under [[FACT:oh.labour.minwage.small_employer.gross_threshold=405,000]] USD a year, and employees under 16, are paid the federal minimum wage (Annex FED). 2027 (published): [[FACT:oh.minwage.hourly=11.40]] USD and [[FACT:oh.minwage.tipped.cash_wage=5.70]] USD; small-employer threshold [[FACT:oh.labour.minwage.small_employer.gross_threshold=419,000]] USD.
- **No local minimum wages.** Local regulation of hours, scheduling and benefits for private employers is preempted (ORC 4113.85): [[FACT:oh.local_mandates.preempted=True]] [US-OHS5-012]. No city minimum wage was located; the minimum-wage preemption text itself (ORC 4111.02) was not read.
- **Overtime (ORC 4111.03) [US-OHS5-003].** [[FACT:oh.overtime.premium.multiplier=1.5]] times the regular rate over [[FACT:oh.overtime.weekly_threshold_hours=40]] hours per workweek, following FLSA exemptions; no daily overtime. Small employers below the poster's gross-receipts test are outside the state overtime duty [US-OHS5-004, US-OHS5-005].
- **Pay frequency and pay day (ORC 4113.15) [US-OHS5-015, US-OH-004]:** [[FACT:oh.pay_frequency.rule=at least semimonthly (1-15 by 1st of next month; 16-end by 15th)]]. Daily or weekly pay is allowed, as is a longer customary or contractual lapse; liquidated damages accrue on wages left unpaid beyond the statutory period.
- **Method of payment** (direct deposit or paycard consent): no Ohio statute read (open point below).
- **Records:** name, address, occupation, rate, pay per period, hours per day and week, kept [[FACT:oh.records.wage_hour.retention_years=3]] years [US-OHS5-005].

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `oh.minwage.hourly` | [[FACT:oh.minwage.hourly=11.00]] | USD | 2026-01-01 to 2026-12-31 | US-OHS5-005 |  |
| `oh.minwage.hourly` | [[FACT:oh.minwage.hourly=11.40]] | USD | 2027-01-01 to 2027-12-31 | US-OHS5-004 |  |
| `oh.minwage.tipped.cash_wage` | [[FACT:oh.minwage.tipped.cash_wage=5.50]] | USD | 2026-01-01 to 2026-12-31 | US-OHS5-005 | 50% of minimum; >30 USD/month tips |
| `oh.minwage.tipped.cash_wage` | [[FACT:oh.minwage.tipped.cash_wage=5.70]] | USD | 2027-01-01 to 2027-12-31 | US-OHS5-004 |  |
| `oh.labour.minwage.small_employer.gross_threshold` | [[FACT:oh.labour.minwage.small_employer.gross_threshold=405,000]] | USD | 2026-01-01 to 2026-12-31 | US-OHS5-005 |  |
| `oh.labour.minwage.small_employer.gross_threshold` | [[FACT:oh.labour.minwage.small_employer.gross_threshold=419,000]] | USD | 2027-01-01 to 2027-12-31 | US-OHS5-004 |  |
| `oh.minwage.indexation` | [[FACT:oh.minwage.indexation=CPI-W 12 months to September, each 1 January, rounded to 0.05]] |  | from 2007-01-01 | US-OHS5-006 | Ohio Const. art. II s.34a |
| `oh.local_mandates.preempted` | [[FACT:oh.local_mandates.preempted=True]] |  | from 2017-03-21 | US-OHS5-012 | 4113.85 covers benefits/scheduling; 4111.02 not read |
| `oh.overtime.weekly_threshold_hours` | [[FACT:oh.overtime.weekly_threshold_hours=40]] | hours | from 2022-07-06 | US-OHS5-004 | FLSA exemptions; employers under 150,000 gross excluded |
| `oh.overtime.premium.multiplier` | [[FACT:oh.overtime.premium.multiplier=1.5]] | ratio | from 2022-07-06 | US-OHS5-003 |  |
| `oh.pay_frequency.rule` | [[FACT:oh.pay_frequency.rule=at least semimonthly (1-15 by 1st of next month; 16-end by 15th)]] |  | from 2019-03-20 | US-OHS5-015 | 4113.15; liquidated damages after 30 days |

**Open research points**

- Not configured in this release [[GAP:RQ-273]]: Direct deposit / paycard consent: no statute read.

## OH.2 Income tax withholding

- **Statutory rate (HB 96, ORC 5747.02(A)(3), effective 2025-09-30) [US-OHS5-007].** From tax year 2026 a flat [[FACT:oh.pit.statutory.rate=2.75]] % on Ohio taxable income above a zero bracket of [[FACT:oh.pit.statutory.zero_bracket=26,050]] USD.
- **Withholding schedule is not the statutory rate.** The commissioner's withholding tables and formula (ORC 5747.06) still graduate above the statutory flat rate. The two instruments are both correct for their level: the payroll engine withholds under the tables (5747.06); the flat rate (5747.02) applies at assessment. Never replace the withholding schedule with the statutory rate.
- **Mid-year change: two withholding editions in 2026.**

| Pay dates | Rate band 1 | Band 2 | Band 3 | Breakpoints | Base tax at band 2 / band 3 | Register id |
|---|---|---|---|---|---|---|
| 2025-10-01 to 2026-07-31 | [[FACT:oh.pit.wh.rate.1=1.775]] % | [[FACT:oh.pit.wh.rate.2=2.99]] % | [[FACT:oh.pit.wh.rate.3=3.64]] % | [[FACT:oh.pit.wh.break.1=26,050]] / [[FACT:oh.pit.wh.break.2=100,000]] USD | [[FACT:oh.pit.wh.base_tax.2=462.39]] / [[FACT:oh.pit.wh.base_tax.3=2,673.50]] USD | US-OHP52-001 |
| from 2026-08-01 | [[FACT:oh.pit.wh.rate.1=1.6]] % | [[FACT:oh.pit.wh.rate.2=2.99]] % | [[FACT:oh.pit.wh.rate.3=3.4]] % | [[FACT:oh.pit.wh.break.1=26,050]] / [[FACT:oh.pit.wh.break.2=100,000]] USD | [[FACT:oh.pit.wh.base_tax.2=416.80]] / [[FACT:oh.pit.wh.base_tax.3=2,627.91]] USD | US-OHS5-001 |

- **Formula (annualised).** Taxable wages TW = pay x pay periods - [[FACT:oh.pit.wh.exemption.annual=650]] USD x exemptions; tax = base tax of the band + band rate x (TW - lower breakpoint); withholding = tax / pay periods. Edition text: earlier period [[FACT:oh.pit.wh.method.period_a=formula: TW=pay x PP-650 x exemptions; 1.775% to 26,050; 462.39+2.990% to 100,000; 2,673.50+3.640% above; no rounding instruction]]; from 2026-08-01 [[FACT:oh.pit.wh.method.period_b=formula: TW=pay x PP-650 x exemptions; 1.6% to 26,050; 416.80+2.99% to 100,000; 2,627.91+3.4% above; / PP]]. Percentage tables per pay frequency are published with each edition [US-OH-006, US-OH-002].
- **Oracle:** biweekly pay, one exemption, paid on or after 2026-08-01: withholding [[FACT:oh.pit.oracle.example_1.withholding=45.13]] USD (table and formula agree) [US-OHS5-001]. Recomputation is in Module 12 and the validation suite.
- **Rounding:** no rounding instruction in the tables or the formula; whole-dollar rounding (ORC 718.25) is optional on municipal returns only [US-OHP52-002].
- **Supplemental wages (OAC 5703-7-10, from 2026-01-01):** withheld at the highest statutory rate of the year, OAC 5703-7-10 [US-OHS5-017]; that rate is [[FACT:oh.wh.supplemental.rate=2.75]] %, ORC 5747.02(A)(3)(c) [US-OHS5-007].
- **Certificate:** [[FACT:oh.wh.certificate=IT 4; none on file = zero exemptions]] [US-OHP52-006].
- **Exemptions from withholding (5747.06) [US-OHS5-008]:** agricultural labour, domestic service, service in a quarter with cash pay under [[FACT:oh.pit.exempt.quarterly_cash_threshold=300]] USD, foreign government service, newspaper carriers who are minors.
- **Reciprocity:** no Ohio withholding for residents of [[FACT:oh.reciprocity.states=IN;KY;MI;PA;WV]] working in Ohio [US-MULTI-005, US-OHP52-006]; resident credit via IT RC, none for wages from reciprocity states [US-OHP52-004].
- **School district income tax (ORC ch. 5748):** [[FACT:oh.pit.school_district.basis=withheld for employees residing in a taxing district]], even where the employer has no operations in the district [US-OH-002, US-OHS5-017]. Districts with the tax in 2026: [[FACT:oh.pit.school_district.count=214]], of which [[FACT:oh.pit.school_district.earned_income_base.count=68]] on the earned-income-only base. Source list: [[FACT:oh.pit.school_district.full_list=ODT 'A list of Ohio's School District Income Tax Levies, effective January 2026': 214 school districts with income tax, 68 on the earned-income-only base; per district county, 4-digit SD number, IRN, TY2026 rate, first year.]] [US-OHB5-001].
- **Municipal income tax (ORC ch. 718), T4 layer.** Basis: [[FACT:oh.pit.municipal.basis=work-location; qualifying wages = Medicare wages less section 125 (401(k) deferrals taxable)]] [US-OHS5-013]. The employer withholds qualifying wages times the municipal rate and remits to the municipality or its collector [US-OHP52-003, US-OH-010]. Occasional-entrant rule: [[FACT:oh.pit.municipal.occasional_entrant_days=20]] days [US-OH-008]. Rates above [[FACT:oh.pit.municipal.rate_cap_without_vote=1]] % need voter approval [US-OHB5-402]. Rate source: The Finder municipal rate table of the Ohio Department of Taxation (OHMuniRateTable.csv: begin date, end date, municipal FIPS code, name and rate per municipality; rates only, no resident credit and no collector) [US-OHB5-002]; municipalities with a rate in force on 2026-11-01: [[FACT:oh.pit.municipal.count_in_force=678]].

| Municipality | Rate | Register id |
|---|---|---|
| Columbus | [[FACT:oh.pit.municipal.columbus.rate=2.5]] % | US-OHB5-002 |
| Cleveland | [[FACT:oh.pit.municipal.cleveland.rate=2.5]] % | US-OHB5-002 |
| Cincinnati | [[FACT:oh.pit.municipal.cincinnati.rate=1.8]] % | US-OHB5-002 |
| Dayton | [[FACT:oh.pit.municipal.dayton.rate=2.5]] % | US-OHB5-002 |
| Toledo | [[FACT:oh.pit.municipal.toledo.rate=2.5]] % | US-OHB5-002 |
| Akron | [[FACT:oh.pit.municipal.akron.rate=2.5]] % | US-OHB5-002 |
| Youngstown | [[FACT:oh.pit.municipal.youngstown.rate=2.75]] % | US-OHB5-002 |

- **Resident and nonresident matrix.**

| Income type | Ohio resident | Nonresident |
|---|---|---|
| Regular salary | State withholding under the tables; school district tax if resident in a taxing district; municipal tax of the work location | State withholding under the same tables (5747.06 covers nonresidents), unless resident of a reciprocity state; municipal tax of the work location; no school district tax |
| Bonus / supplemental | Supplemental rate [[FACT:oh.wh.supplemental.rate=2.75]] % | Same, unless reciprocity applies |
| 401(k) deferrals | Excluded at state level (follows federal) | Same |
| Municipal base | Medicare wages less cafeteria-plan contributions: elective deferrals taxable | Same, at the work location |
| Severance, equity, benefits in kind | Follow federal wages at state level; municipal treatment of NQDC and stock options depends on the ordinance | Same, work-location sourcing |

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `oh.pit.statutory.rate` | [[FACT:oh.pit.statutory.rate=2.75]] | % | from 2026-01-01 | US-OHS5-007 |  |
| `oh.pit.statutory.zero_bracket` | [[FACT:oh.pit.statutory.zero_bracket=26,050]] | USD | from 2026-01-01 | US-OHS5-007 |  |
| `oh.pit.wh.method.period_b` | [[FACT:oh.pit.wh.method.period_b=formula: TW=pay x PP-650 x exemptions; 1.6% to 26,050; 416.80+2.99% to 100,000; 2,627.91+3.4% above; / PP]] |  | from 2026-08-01 | US-OHS5-001 |  |
| `oh.pit.wh.exemption.annual` | [[FACT:oh.pit.wh.exemption.annual=650]] | USD | from 2025-10-01 | US-OHS5-001 | weekly table 12.50 per exemption |
| `oh.pit.wh.rate.1` | [[FACT:oh.pit.wh.rate.1=1.6]] | % | from 2026-08-01 | US-OH-006 |  |
| `oh.pit.wh.rate.2` | [[FACT:oh.pit.wh.rate.2=2.99]] | % | from 2026-08-01 | US-OH-006 |  |
| `oh.pit.wh.rate.3` | [[FACT:oh.pit.wh.rate.3=3.4]] | % | from 2026-08-01 | US-OH-006 | withholding schedule graduates to [[FACT:oh.pit.wh.rate.3=3.4]]% although statutory rate is flat [[FACT:oh.pit.statutory.rate=2.75]]% |
| `oh.pit.wh.break.1` | [[FACT:oh.pit.wh.break.1=26,050]] | USD | from 2026-08-01 | US-OHS5-001 |  |
| `oh.pit.wh.break.2` | [[FACT:oh.pit.wh.break.2=100,000]] | USD | from 2026-08-01 | US-OHS5-001 |  |
| `oh.pit.wh.base_tax.2` | [[FACT:oh.pit.wh.base_tax.2=416.80]] | USD | from 2026-08-01 | US-OHS5-001 |  |
| `oh.pit.wh.base_tax.3` | [[FACT:oh.pit.wh.base_tax.3=2,627.91]] | USD | from 2026-08-01 | US-OHS5-001 |  |
| `oh.pit.oracle.example_1.withholding` | [[FACT:oh.pit.oracle.example_1.withholding=45.13]] | USD | from 2026-08-01 | US-OHS5-001 |  |
| `oh.wh.supplemental.rate` | [[FACT:oh.wh.supplemental.rate=2.75]] | % | 2026-01-01 to 2026-12-31 | US-OHS5-007 |  |
| `oh.reciprocity.states` | [[FACT:oh.reciprocity.states=IN;KY;MI;PA;WV]] |  | from 2026-01-01 | US-MULTI-005 |  |
| `oh.pit.exempt.quarterly_cash_threshold` | [[FACT:oh.pit.exempt.quarterly_cash_threshold=300]] | USD | from 2019-10-17 | US-OHS5-008 | service in a quarter with cash pay under 300; also agricultural, domestic, newspaper carriers under 18 |
| `oh.pit.school_district.basis` | [[FACT:oh.pit.school_district.basis=withheld for employees residing in a taxing district]] |  | from 2026-08-01 | US-OH-002 | 2026 changes: 6 new districts, 2 expired, 3 rate changes (US-OHS5-018) |
| `oh.pit.municipal.basis` | [[FACT:oh.pit.municipal.basis=work-location; qualifying wages = Medicare wages less section 125 (401(k) deferrals taxable)]] |  | from 2025-09-30 | US-OHS5-013 |  |
| `oh.pit.municipal.occasional_entrant_days` | [[FACT:oh.pit.municipal.occasional_entrant_days=20]] | days | from 2015-03-23 | US-OH-008 |  |
| `oh.pit.municipal.rate_cap_without_vote` | [[FACT:oh.pit.municipal.rate_cap_without_vote=1]] | % | from 2026-01-01 | US-OHB5-402 |  |
| `oh.wh.certificate` | [[FACT:oh.wh.certificate=IT 4; none on file = zero exemptions]] |  | from 2026-10-29 | US-OHP52-006 | keep 4 years |
| `oh.pit.wh.method.period_a` | [[FACT:oh.pit.wh.method.period_a=formula: TW=pay x PP-650 x exemptions; 1.775% to 26,050; 462.39+2.990% to 100,000; 2,673.50+3.640% above; no rounding instruction]] |  | 2025-10-01 to 2026-07-31 | US-OHP52-001 | Optional Computer Formula eff. 2025-10-01: governs pay dates 2025-10-01..2026-07-31 (closed period; retro corrections); replaced by US-OHS5-001 from 2026-08-01. |
| `oh.pit.wh.rate.1` | [[FACT:oh.pit.wh.rate.1=1.775]] | % | 2025-10-01 to 2026-07-31 | US-OHP52-001 | Optional Computer Formula eff. 2025-10-01: governs pay dates 2025-10-01..2026-07-31 (closed period; retro corrections); replaced by US-OHS5-001 from 2026-08-01. |
| `oh.pit.wh.rate.2` | [[FACT:oh.pit.wh.rate.2=2.99]] | % | 2025-10-01 to 2026-07-31 | US-OH-006 | Optional Computer Formula eff. 2025-10-01: governs pay dates 2025-10-01..2026-07-31 (closed period; retro corrections); replaced by US-OHS5-001 from 2026-08-01. |
| `oh.pit.wh.rate.3` | [[FACT:oh.pit.wh.rate.3=3.64]] | % | 2025-10-01 to 2026-07-31 | US-OHP52-001 | Optional Computer Formula eff. 2025-10-01: governs pay dates 2025-10-01..2026-07-31 (closed period; retro corrections); replaced by US-OHS5-001 from 2026-08-01. |
| `oh.pit.wh.break.1` | [[FACT:oh.pit.wh.break.1=26,050]] | USD | 2025-10-01 to 2026-07-31 | US-OHP52-001 | Optional Computer Formula eff. 2025-10-01: governs pay dates 2025-10-01..2026-07-31 (closed period; retro corrections); replaced by US-OHS5-001 from 2026-08-01. |
| `oh.pit.wh.break.2` | [[FACT:oh.pit.wh.break.2=100,000]] | USD | 2025-10-01 to 2026-07-31 | US-OHP52-001 | Optional Computer Formula eff. 2025-10-01: governs pay dates 2025-10-01..2026-07-31 (closed period; retro corrections); replaced by US-OHS5-001 from 2026-08-01. |
| `oh.pit.wh.base_tax.2` | [[FACT:oh.pit.wh.base_tax.2=462.39]] | USD | 2025-10-01 to 2026-07-31 | US-OHP52-001 | Optional Computer Formula eff. 2025-10-01: governs pay dates 2025-10-01..2026-07-31 (closed period; retro corrections); replaced by US-OHS5-001 from 2026-08-01. |
| `oh.pit.wh.base_tax.3` | [[FACT:oh.pit.wh.base_tax.3=2,673.50]] | USD | 2025-10-01 to 2026-07-31 | US-OHP52-001 | Optional Computer Formula eff. 2025-10-01: governs pay dates 2025-10-01..2026-07-31 (closed period; retro corrections); replaced by US-OHS5-001 from 2026-08-01. |
| `oh.pit.school_district.full_list` | [[FACT:oh.pit.school_district.full_list=ODT 'A list of Ohio's School District Income Tax Levies, effective January 2026': 214 school districts with income tax, 68 on the earned-income-only base; per district county, 4-digit SD number, IRN, TY2026 rate, first year.]] |  | from 2026-01-01 | US-OHB5-001 |  |
| `oh.pit.school_district.count` | [[FACT:oh.pit.school_district.count=214]] |  | 2026-01-01 to 2026-12-31 | US-OHB5-001 |  |
| `oh.pit.school_district.earned_income_base.count` | [[FACT:oh.pit.school_district.earned_income_base.count=68]] |  | 2026-01-01 to 2026-12-31 | US-OHB5-001 |  |
| `oh.pit.municipal.rate_table` | The Finder municipal rate table of the Ohio Department of Taxation (OHMuniRateTable.csv: begin date, end date, municipal FIPS code, name and rate per municipality; rates only, no resident credit and no collector) |  | from 2026-01-01 | US-OHB5-002 |  |
| `oh.pit.municipal.count_in_force` | [[FACT:oh.pit.municipal.count_in_force=678]] |  | from 2026-11-01 | US-OHB5-002 | Distinct municipal FIPS with begin <= 2026-11-01 <= end in OHMuniRateTable.csv. |
| `oh.pit.municipal.columbus.rate` | [[FACT:oh.pit.municipal.columbus.rate=2.5]] | % | from 2009-10-01 | US-OHB5-002 | Row in force on 2026-11-01 in OHMuniRateTable.csv (begin date = effective_from). |
| `oh.pit.municipal.cleveland.rate` | [[FACT:oh.pit.municipal.cleveland.rate=2.5]] | % | from 2017-01-01 | US-OHB5-002 | Row in force on 2026-11-01 in OHMuniRateTable.csv (begin date = effective_from). |
| `oh.pit.municipal.cincinnati.rate` | [[FACT:oh.pit.municipal.cincinnati.rate=1.8]] | % | from 2020-10-01 | US-OHB5-002 | Row in force on 2026-11-01 in OHMuniRateTable.csv (begin date = effective_from). |
| `oh.pit.municipal.dayton.rate` | [[FACT:oh.pit.municipal.dayton.rate=2.5]] | % | from 2017-01-01 | US-OHB5-002 | Row in force on 2026-11-01 in OHMuniRateTable.csv (begin date = effective_from). |
| `oh.pit.municipal.toledo.rate` | [[FACT:oh.pit.municipal.toledo.rate=2.5]] | % | from 2021-01-01 | US-OHB5-002 | Row in force on 2026-11-01 in OHMuniRateTable.csv (begin date = effective_from). |
| `oh.pit.municipal.akron.rate` | [[FACT:oh.pit.municipal.akron.rate=2.5]] | % | from 2018-01-01 | US-OHB5-002 | Row in force on 2026-11-01 in OHMuniRateTable.csv (begin date = effective_from). |
| `oh.pit.municipal.youngstown.rate` | [[FACT:oh.pit.municipal.youngstown.rate=2.75]] | % | from 2003-01-01 | US-OHB5-002 | Row in force on 2026-11-01 in OHMuniRateTable.csv (begin date = effective_from). |

**Open research points**

- Not configured in this release [[GAP:RQ-280]]: 2027 withholding tables, ODJFS rates and SD changes not published.
- Not configured in this release [[GAP:RQ-282]]: OHMuniRateTable.csv carries rates only: the resident credit (rate and limit) and the collector (RITA, CCA or the city itself) are not in the table.

## OH.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in OH.2.

## OH.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in OH.2.

## OH.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Unemployment insurance (ODJFS rate year 2026) [US-OHS5-002, US-OH-005].** Taxable wage base [[FACT:oh.sui.wage_base=9000]] USD. New employer [[FACT:oh.sui.new_employer.rate=2.85]] % (including the Technology and Customer Service Fee); construction new employer [[FACT:oh.ui.rate.new_employer.construction=5.85]] %. Experienced range, fee included: [[FACT:oh.ui.rate.min_total=0.55]] % to [[FACT:oh.ui.rate.max_total=10.25]] %. Technology and Customer Service Fee [[FACT:oh.ui.tcsf.rate=0.15]] % (ORC 4141.251) [US-OHP7-003]. Employee contribution [[FACT:oh.sui.employee.rate=0]] %.
- **No SDI, TDI or PFML** (open point below on the evidence level) and no transit or workforce levy on wages [US-OHL-002].

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `oh.sui.wage_base` | [[FACT:oh.sui.wage_base=9000]] | USD | 2026-01-01 to 2026-12-31 | US-OHS5-002 | indexation rule (4141.01) not read |
| `oh.sui.new_employer.rate` | [[FACT:oh.sui.new_employer.rate=2.85]] | % | 2026-01-01 to 2026-12-31 | US-OHS5-002 |  |
| `oh.ui.rate.new_employer.construction` | [[FACT:oh.ui.rate.new_employer.construction=5.85]] | % | 2026-01-01 to 2026-12-31 | US-OHS5-002 |  |
| `oh.ui.rate.min_total` | [[FACT:oh.ui.rate.min_total=0.55]] | % | 2026-01-01 to 2026-12-31 | US-OHS5-002 | 0.4-10.1 before fee |
| `oh.ui.rate.max_total` | [[FACT:oh.ui.rate.max_total=10.25]] | % | 2026-01-01 to 2026-12-31 | US-OHS5-002 |  |
| `oh.ui.tcsf.rate` | [[FACT:oh.ui.tcsf.rate=0.15]] | % | 2026-01-01 to 2026-12-31 | US-OHS5-002 | ORC 4141.251 |
| `oh.sui.employee.rate` | [[FACT:oh.sui.employee.rate=0]] | % | 2026-01-01 to 2026-06-15 | US-OHR3C-001 | Ohio Rev. Code 4141.23(A): UI contributions are paid by the employer and shall not be deducted, in whole or in part, from employees' remuneration. |
| `oh.sui.employee.rate` | [[FACT:oh.sui.employee.rate=0]] | % | 2026-06-16 to 2026-12-31 | US-OHR3D-001 | Ohio Rev. Code 4141.23(A), version effective 2026-06-16 (Sub. S.B. 101, 136th GA): contributions are paid by the employer 'and shall not be deducted, in whole or in part, from the remuneration of individuals in the employer's employ.' Division (A) is unchanged from the prior version. |

**Open research points**

- Not configured in this release [[GAP:RQ-274]]: The SUI wage base is read as statutory and fixed (ORC 4141.01(G)); the text was not read.
- Not configured in this release [[GAP:RQ-281]]: Not established from an official source.

## OH.4 Pay statement

- **Content (ORC 4113.14, Pay Stub Protection Act, effective 2025-04-09) [US-OHP51-001, US-OHL-001]:** a written or electronic statement every pay period: [[FACT:oh.payslip.items=name and address; employer name; gross and net; each addition and deduction; pay date and period; hours and rate (hourly)]]. No language clause; the SSN is not required.
- **Retention:** wage and hour records [[FACT:oh.records.wage_hour.retention_years=3]] years [US-OHS5-005]; withholding records per the ODT Filing Guidelines.

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `oh.records.wage_hour.retention_years` | [[FACT:oh.records.wage_hour.retention_years=3]] | years | 2026-01-01 to 2027-12-31 | US-OHS5-005 | Records kept 3 years: 2026 poster (US-OHS5-005, 2026-01-01..2026-12-31); the same rule is restated on the 2027 poster (US-OHS5-004, 2027-01-01..2027-12-31). One value for both years. |
| `oh.payslip.items` | [[FACT:oh.payslip.items=name and address; employer name; gross and net; each addition and deduction; pay date and period; hours and rate (hourly)]] |  | from 2025-04-09 | US-OHP51-001 | ORC 4113.14 Pay Stub Protection Act; written or electronic |

## OH.5 Statutory reporting

- **State withholding [US-OHB5-401].** IT 501 payments filed electronically. Frequency by look-back: quarterly up to [[FACT:oh.report.it501.quarterly_threshold=2000]] USD; monthly above it; partial-weekly EFT at [[FACT:oh.report.it501.partial_weekly_threshold=84,000]] USD or more. Annual reconciliation IT 941 due [[FACT:oh.report.it941.due=January 31]]; W-2 upload through OH|TAX by the same date, with the school district code [US-OHS5-018].
- **School district:** SD 101 (periodic) and SD 141 (annual); bulk filing in FSET XML [US-FIL-012]; agent authorisation WT 8655 [US-FIL-011].
- **Municipal:** returns to each municipality or its collector under 718.03 thresholds; a municipality may require semimonthly remittance [US-OHP52-003, US-OH-010].
- **UI quarterly report (ORC 4141.20):** due [[FACT:oh.report.ui.quarterly_due=last day of month after quarter]]; total and taxable remuneration, per-employee name, SSN, wages and weeks paid [US-OHS5-020]. Portal channel: open point below.
- **New hire (ORC 3121.891-.893):** to ODJFS within [[FACT:oh.newhire.report_days=20]] days; contractors are also reported; multistate employers may designate one state [US-OHS5-009, US-OHS5-014].
- **Representatives:** TBOR 1 [US-OHP52-005]; JFS-20106 for UI [US-OHR3-001].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `oh.report.it501.quarterly_threshold` | [[FACT:oh.report.it501.quarterly_threshold=2000]] | USD | from 2026-01-01 | US-OHB5-401 | <=2,000 quarterly; >2,000 and <84,000 monthly; >=100,000 per period next banking day |
| `oh.report.it501.partial_weekly_threshold` | [[FACT:oh.report.it501.partial_weekly_threshold=84,000]] | USD | from 2026-01-01 | US-OHB5-401 |  |
| `oh.report.it941.due` | [[FACT:oh.report.it941.due=January 31]] |  | from 2026-01-01 | US-OHB5-401 | W-2 upload via OH/TAX by Jan 31 with 4-digit SD code |
| `oh.report.ui.quarterly_due` | [[FACT:oh.report.ui.quarterly_due=last day of month after quarter]] |  | from 2014-09-15 | US-OHS5-020 | late forfeiture on remuneration, with a statutory minimum and maximum |
| `oh.newhire.report_days` | [[FACT:oh.newhire.report_days=20]] | days | from 2013-09-29 | US-OHS5-014 | contractors also reported |

**Open research points**

- Not configured in this release [[GAP:RQ-278]]: UI quarterly report channel/format not read.

## OH.6 Leave

- **No state paid sick leave statute** (exists: [[FACT:oh.leave.sick.state_statute.exists=False]]); leave and fringe benefits are employer policy or agreement, and local mandates are preempted (ORC 4113.85) [US-OHS5-012]. No PFML. Other statutory leave with pay impact: open point below.

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `oh.leave.sick.state_statute.exists` | [[FACT:oh.leave.sick.state_statute.exists=False]] |  | from 2017-03-21 | US-OHS5-012 | local mandates preempted |

**Open research points**

- Not configured in this release [[GAP:RQ-275]]: Jury duty, military and voting leave with pay impact not read.

## OH.7 Termination and final pay

- **Final pay:** [[FACT:oh.final_pay.rule=next regular payday under 4113.15 schedule]] [US-OHS5-015]. Accrued vacation and separation pay follow employer policy (4113.85) [US-OHS5-012].
- **Mass layoff (ORC 4141.28(C)):** for a mass layoff for lack of work, notify the director [[FACT:oh.term.mass_layoff.notice_working_days=3]] working days ahead and give each worker the eligibility information [US-OHS5-016]. No state WARN law; federal WARN applies. Individual separation notice: open point below.

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `oh.final_pay.rule` | [[FACT:oh.final_pay.rule=next regular payday under 4113.15 schedule]] |  | from 2019-03-20 | US-OHS5-015 | no dedicated final-pay statute |
| `oh.term.mass_layoff.notice_working_days` | [[FACT:oh.term.mass_layoff.notice_working_days=3]] | days | from 2023-10-03 | US-OHS5-016 | 50+ in 7 days for lack of work |

**Open research points**

- Not configured in this release [[GAP:RQ-279]]: Individual UI separation notice under OAC 4141 not read.

## OH.8 Benefits in kind and taxable wages

- **State tax** starts from federal AGI (ORC 5747.01(A), amended by SB 9 effective 2026-03-05); the add-backs read do not touch retirement deferrals, cafeteria plans, HSA, transit or group-term life, so the state follows the federal exclusions [US-OHS5-022].
- **Municipal tax departs from federal:** IRC 3121(a) wage base; elective deferrals taxable, cafeteria plans excluded; NQDC and stock options per pre-2016 ordinance [US-OHS5-013].
- **School district tax** follows the district base: traditional or earned income [US-OHS5-019].

## OH.9 Deductions and garnishments

- **Creditor garnishment (ORC 2329.66(A)(13)) [US-OHS5-011]:** the exempt amount is the greater of the CCPA percentage of disposable earnings or [[FACT:oh.garn.consumer.exempt_multiple_fmw.weekly=30]] times the federal minimum wage per week (with the corresponding multiples for longer pay periods). This matches the CCPA (Annex FED).
- **Child support IWO fee (ORC 3121.18):** the employer may deduct a fee of at least [[FACT:oh.garn.iwo.employer_fee.min=2]] USD per withholding, within the statutory percentage of the amount withheld [US-OHS5-010]. Deduction authorisation rules and support priority: open point below.

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `oh.garn.consumer.exempt_multiple_fmw.weekly` | [[FACT:oh.garn.consumer.exempt_multiple_fmw.weekly=30]] |  | from 2025-09-30 | US-OHS5-011 | greater of 75% disposable or 30x/60x/65x/130x FMW |
| `oh.garn.iwo.employer_fee.min` | [[FACT:oh.garn.iwo.employer_fee.min=2]] | USD | from 2001-03-22 | US-OHS5-010 | greater of 2 USD or up to 1% of amount withheld |

**Open research points**

- Not configured in this release [[GAP:RQ-276]]: Deduction authorisation rules and IWO priority not read.

## OH.10 Collective agreements and prevailing wage

- **Prevailing wage (ORC ch. 4115):** rates set by the Director of Commerce (4115.04); new-construction threshold [[FACT:oh.prevailing_wage.threshold.new_construction=250,000]] USD, with other thresholds for remodelling and road work, adjusted biennially (4115.034) [US-OHR3-002, US-OHR3-003, US-OHP51-003]. Certified payroll: open point below.

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `oh.prevailing_wage.threshold.new_construction` | [[FACT:oh.prevailing_wage.threshold.new_construction=250,000]] | USD | from 2026-01-01 | US-OHP51-003 | remodeling 75,000; road/sewer/bridge 78,258/23,447; biennial adjustment date unconfirmed |

**Open research points**

- Not configured in this release [[GAP:RQ-277]]: 4115.071 certified payroll and 2026 threshold adjustment date not read.

## OH.11 Indexation

- **Minimum wage:** [[FACT:oh.minwage.indexation=CPI-W 12 months to September, each 1 January, rounded to 0.05]] [US-OHS5-006]. The small-employer threshold uses the same index; the tipped wage is half the minimum wage. The 2026 and 2027 published values follow from the index (derivation in the research pack; values in Section 1).
- **SUI wage base:** statutory, read as not indexed (open point below).
- **Withholding tables:** republished after a rate change (OAC 5703-7-10) [US-OHS5-017], hence the 2026-08-01 edition.
- **Prevailing-wage thresholds:** biennial (4115.034). **School district rates:** annual change list each January [US-OHS5-018].

## OH.12 Payroll data protection and records

- **Breach notice (ORC 1349.19):** to affected Ohio residents within [[FACT:oh.data.breach_notice.days=45]] days of discovery; personal information includes a name combined with an SSN or account number [US-OHS5-021]. No SSN-truncation rule for pay statements; 4113.14 does not require the SSN [US-OHP51-001].

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `oh.data.breach_notice.days` | [[FACT:oh.data.breach_notice.days=45]] | days | from 2007-03-30 | US-OHS5-021 |  |

## OH.13 Live legal change

- **HB 96:** flat statutory rate from tax year 2026 [US-OHS5-007]; municipal 718.01 amendments and 2329.66 amendments effective 2025-09-30 [US-OHP52-003, US-OHS5-011].
- **2026-01-01:** supplemental rule OAC 5703-7-10 [US-OHS5-017]; school district changes [US-OHS5-018].
- **2026-03-05:** ORC 5747.01 amended by SB 9 (substance not analysed) [US-OHS5-022].
- **2026-08-01:** new withholding tables and formula [US-OH-006, US-OHS5-001].
- **2027-01-01 (enacted):** minimum wage and tipped wage per Section 1 [US-OHS5-004]. Not yet published: 2027 withholding tables, ODJFS rates and school district changes (open point in Section 2).

## OH.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## OH.15 Special populations

| Population | Ohio rule | Register id |
|---|---|---|
| Domestic / household | No Ohio withholding on domestic service in a private home (5747.06(A)(2)); babysitters in the employer's home and live-in companions are exempt from the minimum wage | US-OHS5-008, US-OHS5-005 |
| Agricultural | No Ohio withholding on agricultural labour | US-OHS5-008 |
| Minors | Under 16: federal minimum wage; newspaper carriers who are minors: no withholding; Minor Labor Law (ORC 4109) not read | US-OHS5-005, US-OHS5-008 |
| Tipped | Cash wage per Section 1; tip credit up to the full minimum | US-OHS5-005, US-OHS5-004 |
| Clergy / religious | No state rule beyond federal located | US-OHS5-008, US-OHS5-022 |
| Students | No state withholding rule located; UI exclusions in 4141.01(B)(3) not read | - |
| Nonresident aliens | No state rule beyond federal; Ohio withholds on nonresidents generally | US-OHS5-008 |
| Statutory employees | No state rule beyond federal located | US-OHS5-022 |
| Government employees | State and political subdivisions must withhold (5747.06(A)); public employers are outside the 4113.85 definition | US-OHS5-008, US-OHS5-012, US-OHS5-005 |
| Reciprocity-state residents | No Ohio withholding (Section 2); nonresident military spouse: no withholding | US-MULTI-005, US-OHP52-006 |
| Small employers | Below the gross-receipts threshold: federal minimum wage | US-OHS5-005 |

## OH.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## OH.S Sources

Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file. Authorities:

- Build lead (Claude) under owner delegation (Wallisson Gomes): US-OWN-006
- CCA Municipal Income Tax: US-OH-010
- OH official authority: US-OHB5-402, US-OHP7-003
- Ohio Department of Commerce, Wage & Hour: US-OHS5-004, US-OHS5-005
- Ohio Department of Job and Family Services: US-OHR3-001
- Ohio Department of Job and Family Services (ODJFS): US-OHS5-002
- Ohio Department of Taxation: US-FIL-011, US-FIL-012, US-OH-002, US-OH-006, US-OHB5-401, US-OHB5-001, US-OHB5-002, US-OHL-002, US-OHP52-001, US-OHP52-004, US-OHP52-005, US-OHP52-006, US-OHS5-001, US-OHS5-018, US-OHS5-019
- Ohio Department of Taxation (codes.ohio.gov): US-OHS5-017
- Ohio Dept of Commerce / General Assembly: US-OH-004
- Ohio Dept of Job and Family Services: US-OH-005
- Ohio Dept of Taxation: US-MULTI-005
- Ohio General Assembly (136th GA), Sub. S.B. 101 as enrolled: US-OHR3D-001
- Ohio General Assembly (codes.ohio.gov): US-OH-008, US-OHP52-002, US-OHP52-003
- Ohio General Assembly / LSC: US-OHS5-014
- Ohio General Assembly / LSC (codes.ohio.gov): US-OHS5-003, US-OHS5-007, US-OHS5-008, US-OHS5-009, US-OHS5-010, US-OHS5-011, US-OHS5-012, US-OHS5-015, US-OHS5-016, US-OHS5-020, US-OHS5-021, US-OHS5-022
- (authority named in the register): US-OHS5-013
- Ohio Legislative Service Commission: US-OHL-001, US-OHR3-002, US-OHR3C-001
- Ohio Revised Code (Legislative Service Commission): US-OHP51-001
- Owner (Wallisson Gomes): US-OWN-008
- State of Ohio (codes.ohio.gov): US-OHS5-006
- US DOL Wage and Hour Division: US-OHR3-003
- US Department of Labor Wage and Hour Division: US-OHP51-003

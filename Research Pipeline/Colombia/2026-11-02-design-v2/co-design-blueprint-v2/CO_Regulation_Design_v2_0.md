# CO — Colombia Payroll — Regulation Design v2.0

**Country:** Colombia (CO) · ISO 3166-1 numeric 170 · Currency **COP** · **Tax year:** 2026 (calendar year)
**Regulation IDs:** `9170000 + ordinal`, the convention of the development team's draft regulation for Colombia (`9170132` "CO Income Tax Flat", ordinal 132).
**Design basis:** CO-CCG-001 v1.7, CO-WTC-001 v1.9 (*Wage Type Catalogue*, columns N–X and V), CO-DD-001 v1.6, CO-SIR-001 v1.4, Payslip Generator v1.3 and the report specifications (CO-DIAN-004 v1.3; CO-DIAN-001, CO-DIAN-005, CO-PILA-003, CO-CESANTIAS-006 v1.2; CO-DIAN-002, CO-PILA-007 v1.1), issue of 2 November 2026.
**Machine-readable form:** `co_design_v2.json` (same schema as the development team's regulation export: ordinal, taxGroup, taxRuleGroup, taxationType, assertion, bands with formula and debit / credit accounts, taxabilityRules per wage type). Every formula below is the formula in that file.
**Executable validation:** the regulations are executed by an engine that reads the JSON (79 regulations; engine semantics in `ASSUMPTIONS.md`). Results: order check 0 defects; 112 cases / 2293 values of an independent calculation written from the statutes - with that calculation's rounding convention, 12 differences, each explained; with this design's rounding (one per contributor and fund) and non-taxable income (contributions withheld), the further differences are only those two causes (`VALIDATION.md`); 20 design checks exact; sweep of the 298 active WTC rows through the engine: 0 differences; column-O check 0; employee / employer coding check 0.
**Method:** clean-room — built from the research artifacts and the primary sources they cite.

---

## PART 0 — Special categories (CCG sweep)

| Category | Disposition (v2.0 regulation) |
|---|---|
| All-inclusive salary | `9170009` posts the salary to R303; IBC and levy base 70% (`9170045`, `9170047`; Law 100 of 1993 art. 18; Labour Code art. 132); the Law 1393 excess is added without the 70% (CE SU 25185 of 2021); no transport allowance, no service bonus or severance savings (R303 column W = No). |
| Pacted non-salary payments | `9170042`–`9170044`: only payments desalarised by written pact enter the 40% test (Law 1393 of 2010 art. 30; CE SU 25185 rule 3); payments non-salary by nature stay out. |
| Art. 114-1 exoneration | `9170048`: salary payments of the month < 10 SMMLV **and** IBC < 10 SMMLV; removes employer health, SENA and ICBF only (employer band of `9170056`, `9170062`, `9170063`). |
| Apprentices | `9170011` (support 75% classroom / 100% practical, Labour Code art. 81); IBC never below 1 SMMLV (the floor of `9170045`); classroom phase: no transport allowance (`9170013`), no pension (`RESEARCH_GAPS.md` R2: phase field and the practical-phase split). |
| Employed old-age pensioners | Gate `58209` in the pension and solidarity-fund regulations (`9170057`–`9170059`). |
| High-risk pension activity | `9170054` employer pension rate 22% when `58212 = 1` (Decree-Law 2090 of 2003). |
| Foreign national not affiliated to pension | Gate `58211` in the pension and solidarity-fund regulations. |
| Non-residents | `9170132` "CO Income Tax Flat": 20% on WTC column P (Tax Code art. 408; DIAN Concepto 011108 of 2026 item 10); severance savings and interest outside (Law 100 of 1993 art. 135 par. 3 for every payer, Constitutional Court C-397 of 1994; Decree 1625 art. 1.2.4.1.11). A non-resident who must file applies the art. 206 exemptions in the return (DIAN Concepto 577 of 2020). |
| Contributor type 51 | `9170052`, `9170064`–`9170066` (weekly quarters of the minimum wage; occupational risk on 1 SMMLV; PILA Technical Annex 2 v30). |

## PART 1 — Inputs, flags and constants

| Account | Meaning | Source |
|---|---|---|
| 64992 | Contractual monthly salary | $hr.salary (DD) |
| 58295 | Contributory days (30-day convention) | $actual_prorata_days |
| 58201 | All-inclusive salary 1 / ordinary 2 | DD All-Inclusive Salary Flag |
| 58203 | Employer eligible for art. 114-1: 1 / 2 | DD legal-entity field |
| 58204 | Occupational-risk class 1-5 | DD Work Centre Occupational Risk Class |
| 64552 | Tax residence 1 resident / 2 non-resident | DD Tax Residence Status, in the account the development team reads in 9170132 |
| 58259 | Months of service in the 12 months before termination (1-12) | history read |
| 58206 | Withholding procedure 1 / 2 | DD Withholding Procedure |
| 58207 | Number of dependants | DD |
| 58208 | Apprentice phase 0 / 1 classroom / 2 practical | DD Contract Type 4 + phase field (RESEARCH_GAPS R2) |
| 58209 | Employed pensioner 1 / 2 | DD Worker Sub-Type 01 |
| 58211 | Foreign national not affiliated to pension 1 / 2 | DD |
| 58212 | High-risk pension activity 1 / 2 | DD |
| 58213 | Requested higher withholding rate (%) | DD |
| 58214 | Sub-30-day projection option 1 / 2 (default 2) | entity option |
| 58216 | Contributor type 51 1 / 2 | DD Contributor Type |
| 58220 | Dismissal without just cause, indefinite-term contract 1 / 2 | termination record |
| 58250 | Procedure 2 fixed percentage | computed in June / December (RESEARCH_GAPS R3) |
| 58254 | Prepaid health paid (month) | certificate |
| 58255 | Taxable labour payments of the 12 months before termination | history read (RESEARCH_GAPS R3) |
| 58256 | Mortgage interest paid (month) | certificate |
| 58257 | Voluntary pension / AFC contribution (month) | payroll deduction |
| 58258 | Voluntary RAIS contribution (month) | payroll deduction |
| 58288 | Service days 360 (inclusive) | DAYS360($hr.contract_start_date;$employee.last_working_date) [ASSUMED function] |
| 58290 | Illness incapacity days (from day 1) | novelty |
| 58291 | Maternity leave 1 / 2 | novelty |
| 58292 | Vacation business days taken | novelty |
| 58293 | Vacation days compensated in cash | novelty |
| 58294 | Days without vacation at termination | termination record |
| 58297 | Days of the semester for the service bonus (0 outside June / December / termination) | payroll calendar |
| 58298 | Days of the year for severance savings (0 outside December / termination) | payroll calendar |
| 58299 | Separation flag 1 / 2 | DD |

| Constant | Value | Source |
|---|---|---|
| 52501 SMMLV 2026 | 1750905 | Decree 1469 of 29 Dec 2025 art. 1 (provisional suspension revoked by the Consejo de Estado, Section Two, order of 9 July 2026; Decree 0159 of 2026 left without effect by ordinal 3 of the same order) |
| 52502 UVT 2026 | 52374 | Resolution DIAN 000238 of 15 Dec 2025 art. 1 |
| 52503 Transport allowance 2026 | 249095 | Decree 1470 of 2025 art. 1; Law 15 of 1959 art. 2 |
| 52504 Monthly hours divisor (by the date worked) | 220 from 2025-07-15; 210 from 2026-07-15 | Law 2101 of 2021 art. 3; Labour Code art. 161 (Law 2466 of 2025 art. 11) |
| 52505 Rest-day / holiday surcharge (by the date worked) | 0.80 from 2025-07-01; 0.90 from 2026-07-01; 1.00 from 2027-07-01 | Labour Code art. 179 transitional paragraph (Law 2466 of 2025 art. 14) |
| 52542 Maternity leave, weeks | 18 | Labour Code art. 236 num. 1 (Law 2114 of 2021) |
| (in formulas) | rates and limits written as literals: health 4% / 8.5%, pension 4% / 12% (+10 high risk), solidarity fund 0.5% + 0.5% (+0.2 … +1.0 by band, from 4 SMMLV), occupational-risk class rates 0.522 / 1.044 / 2.436 / 4.350 / 6.960%, CCF 4%, SENA 2%, ICBF 3%, 790 / 1,340 / 3,800 / 2,500 UVT, 25% / 30% / 40%, 32 / 16 / 100 UVT, 204 UVT, art. 383 table | each regulation cites its source in Part 4 |

## PART 2 — Account register

| Account | Posted by | Read by |
|---|---|---|
| `R156` | 9170019 | 9170040, 9170047, 9170072, 9170132 |
| `R302` | 9170010 | 9170014, 9170020, 9170040, 9170041, 9170045, 9170047, 9170049, 9170050, 9170051, 9170072, 9170132 |
| `R303` | 9170009 | 9170014, 9170040, 9170041, 9170045, 9170047, 9170049, 9170050, 9170051, 9170072, 9170132 |
| `R304` | 9170013 | 9170020, 9170040, 9170072, 9170132 |
| `R306` | 9170012 | 9170020, 9170040, 9170041, 9170045, 9170047, 9170049, 9170050, 9170051, 9170072, 9170132 |
| `R307` | 9170012 | 9170020, 9170040, 9170041, 9170045, 9170047, 9170049, 9170050, 9170051, 9170072, 9170132 |
| `R308` | 9170012 | 9170014, 9170020, 9170040, 9170041, 9170045, 9170047, 9170049, 9170050, 9170051, 9170072, 9170132 |
| `R309` | 9170012 | 9170020, 9170040, 9170041, 9170045, 9170047, 9170049, 9170050, 9170051, 9170072, 9170132 |
| `R310` | 9170012 | 9170020, 9170040, 9170041, 9170045, 9170047, 9170049, 9170050, 9170051, 9170072, 9170132 |
| `R311` | 9170012 | 9170020, 9170040, 9170041, 9170045, 9170047, 9170049, 9170050, 9170051, 9170072, 9170132 |
| `R312` | 9170012 | 9170020, 9170040, 9170041, 9170045, 9170047, 9170049, 9170050, 9170051, 9170072, 9170132 |
| `R320` | 9170021 | 9170040, 9170073, 9170091, 9170092, 9170093, 9170132 |
| `R321` | 9170022 | 9170039 |
| `R322` | 9170023 | 9170039 |
| `R323` | 9170016 | 9170020, 9170040, 9170041, 9170045, 9170047, 9170049, 9170050, 9170072, 9170132 |
| `R324` | 9170017 | 9170040, 9170047, 9170072, 9170132 |
| `R326` | 9170024 | 9170040, 9170045, 9170049, 9170050, 9170072, 9170132 |
| `R327` | 9170025, 9170026 | 9170040, 9170045, 9170049, 9170050, 9170072, 9170132 |
| `R330` | 9170029 | 9170040, 9170045, 9170049, 9170050, 9170072, 9170132 |
| `R338` | 9170011 | 9170040, 9170045, 9170051, 9170072, 9170132 |
| `R339` | 9170032 | 9170040, 9170089, 9170132 |
| `52515` | 9170053 | payslip / reports |
| `52516` | 9170054 | 9170057 |
| `52519` | 9170055 | payslip / reports |
| `58100` | 9170039, 9170040 | 9170141 |
| `58101` | 9170041 | 9170043, 9170048 |
| `58102` | 9170042 | 9170043, 9170044 |
| `58103` | 9170043 | 9170044 |
| `58104` | 9170044 | 9170045, 9170049, 9170050, 9170051 |
| `58106` | 9170045 | 9170046, 9170048, 9170056 |
| `58107` | 9170046 | 9170053, 9170058, 9170059 |
| `58108` | 9170047 | 9170061, 9170062, 9170063 |
| `58112` | 9170049 | 9170057 |
| `58113` | 9170050 | 9170058, 9170059 |
| `58114` | 9170051 | 9170060 |
| `58121` | 9170056 | 9170067, 9170075 |
| `58122` | 9170057 | 9170067, 9170075 |
| `58123` | 9170058 | 9170067, 9170075 |
| `58124` | 9170059 | 9170067, 9170075 |
| `58127` | 9170064 | 9170067 |
| `58129` | 9170067 | 9170141 |
| `58137` | 9170064 | 9170068 |
| `58138` | 9170065 | 9170068 |
| `58139` | 9170066 | 9170068 |
| `58141` | 9170056 | 9170068 |
| `58142` | 9170057 | 9170068 |
| `58143` | 9170060 | 9170068 |
| `58144` | 9170061 | 9170068 |
| `58145` | 9170062 | 9170068 |
| `58146` | 9170063 | 9170068 |
| `58149` | 9170068 | payslip / reports |
| `58150` | 9170072, 9170073 | 9170075, 9170076, 9170077, 9170080, 9170139 |
| `58151` | 9170075 | 9170076 |
| `58152` | 9170076 | 9170081, 9170082, 9170084 |
| `58153` | 9170077 | 9170081, 9170083 |
| `58154` | 9170078 | 9170081, 9170083 |
| `58155` | 9170079 | 9170081, 9170083 |
| `58156` | 9170080 | 9170080, 9170081, 9170083 |
| `58157` | 9170081 | 9170081, 9170083, 9170091 |
| `58158` | 9170082 | 9170083 |
| `58159` | 9170083 | 9170082, 9170084, 9170092 |
| `58160` | 9170084 | 9170085, 9170087 |
| `58161` | 9170086 | 9170139 |
| `58162` | 9170087 | 9170139 |
| `58163` | 9170132 | 9170139 |
| `58164` | 9170089 | 9170139 |
| `58165` | 9170093 | 9170139 |
| `58166` | 9170091 | 9170081, 9170091, 9170092 |
| `58167` | 9170092 | 9170082, 9170092, 9170093 |
| `58168` | 9170090 | 9170139 |
| `58169` | 9170139 | 9170141 |
| `58170` | 9170141 | payslip / reports |
| `58171` | 9170020 | 9170021, 9170022, 9170023 |
| `58175` | 9170014 | 9170015, 9170016, 9170017, 9170019 |
| `58178` | 9170015 | payslip / reports |
| `58189` | 9170031 | 9170032 |
| `58194` | 9170030 | payslip / reports |
| `58195` | 9170028 | payslip / reports |
| `58196` | 9170027 | payslip / reports |
| `58197` | 9170052 | 9170064, 9170066 |
| `58198` | 9170052 | 9170065 |
| `58215` | 9170048 | 9170056, 9170062, 9170063 |
| `58217` | 9170018 | payslip / reports |
| `58240` | 9170074 | 9170075, 9170076, 9170077, 9170080, 9170085 |
| `58242` | 9170085 | 9170086 |
| `58243` | 9170088 | 9170089, 9170090 |

`_raw` = the band amount before the post formula (contributions before the COP 100 rounding feed the non-taxable income); `_ytd` = sum over the prior periods of the calendar year (annual UVT caps).

## PART 3 — Regulation sequence

| Ord | ID | Name | Tax group | Tax rule group | Taxation type |
|---|---|---|---|---|---|
| 9 | 9170009 | CO All-inclusive Salary for the Period | social_security | `retro_simple_tax_post_formula` | formula |
| 10 | 9170010 | CO Basic Salary for the Period | social_security | `retro_simple_tax_post_formula` | formula |
| 11 | 9170011 | CO Apprentice Maintenance Support | social_security | `retro_simple_tax_post_formula` | formula |
| 12 | 9170012 | CO Overtime and Premium Hours | social_security | `retro_simple_tax_post_formula` | formula |
| 13 | 9170013 | CO Transport Allowance | social_security | `retro_simple_tax_post_formula` | formula |
| 14 | 9170014 | CO Vacation Base | social_security | `retro_simple_tax_post_formula` | flat |
| 15 | 9170015 | CO Vacation Daily Value | social_security | `retro_simple_tax_post_formula` | formula |
| 16 | 9170016 | CO Vacation Taken | social_security | `retro_simple_tax_post_formula` | formula |
| 17 | 9170017 | CO Vacation Compensated in Cash | social_security | `retro_simple_tax_post_formula` | formula |
| 18 | 9170018 | CO Vacation Compensation Above Half (block flag) | social_security | `retro_simple_tax_post_formula` | formula |
| 19 | 9170019 | CO Vacation Paid on Termination | social_security | `retro_simple_tax_post_formula` | formula |
| 20 | 9170020 | CO Statutory-Benefit Base | social_security | `retro_simple_tax_post_formula` | flat |
| 21 | 9170021 | CO Service Bonus | social_security | `retro_simple_tax_post_formula` | flat |
| 22 | 9170022 | CO Severance Savings | social_security | `retro_simple_tax_post_formula` | flat |
| 23 | 9170023 | CO Interest on Severance Savings | social_security | `retro_simple_tax_post_formula` | flat |
| 24 | 9170024 | CO Illness Benefit Days 1-2 (employer) | social_security | `retro_simple_tax_post_formula` | formula |
| 25 | 9170025 | CO Illness Benefit Days 3-90 (health insurer) | social_security | `retro_simple_tax_post_formula` | formula |
| 26 | 9170026 | CO Illness Benefit Days 91-180 (health insurer) | social_security | `retro_simple_tax_post_formula` | formula |
| 27 | 9170027 | CO Illness Benefit Total | social_security | `retro_simple_tax_post_formula` | formula |
| 28 | 9170028 | CO Contribution Base of the Illness Days | social_security | `retro_simple_tax_post_formula` | formula |
| 29 | 9170029 | CO Maternity Leave Pay | social_security | `retro_simple_tax_post_formula` | formula |
| 30 | 9170030 | CO Contribution Base of the Maternity Leave | social_security | `retro_simple_tax_post_formula` | formula |
| 31 | 9170031 | CO Art. 64 Indemnity Days | social_security | `retro_simple_tax_post_formula` | formula |
| 32 | 9170032 | CO Art. 64 Indemnity | social_security | `retro_simple_tax_post_formula` | formula |
| 39 | 9170039 | CO Severance Savings Paid on Termination | social_security | `retro_simple_tax_post_formula` | formula |
| 40 | 9170040 | CO Gross Earnings | social_security | `retro_simple_tax` | flat |
| 41 | 9170041 | CO Salary Payments of the Month | social_security | `retro_simple_tax` | flat |
| 42 | 9170042 | CO Pacted Non-Salary Payments | social_security | `retro_simple_tax` | flat |
| 43 | 9170043 | CO Total Remuneration (Law 1393 test) | social_security | `retro_simple_tax_post_formula` | formula |
| 44 | 9170044 | CO Law 1393 Excess | social_security | `retro_simple_tax_post_formula` | formula |
| 45 | 9170045 | CO Contribution Base (IBC) - Health | social_security | `retro_simple_tax_post_formula` | flat |
| 46 | 9170046 | CO IBC in Minimum Wages | social_security | `retro_simple_tax_post_formula` | formula |
| 47 | 9170047 | CO Payroll-Levy Base | social_security | `retro_simple_tax_post_formula` | flat |
| 48 | 9170048 | CO Art. 114-1 Exoneration Test | social_security | `retro_simple_tax_post_formula` | formula |
| 49 | 9170049 | CO IBC - Pension | social_security | `retro_simple_tax_post_formula` | flat |
| 50 | 9170050 | CO IBC - Solidarity Fund | social_security | `retro_simple_tax_post_formula` | flat |
| 51 | 9170051 | CO IBC - Occupational Risk | social_security | `retro_simple_tax_post_formula` | flat |
| 52 | 9170052 | CO Contributor Type 51 Bases | social_security | `retro_simple_tax_post_formula` | formula |
| 53 | 9170053 | CO Solidarity Fund Subsistence Rate | social_security | `retro_simple_tax_post_formula` | formula |
| 54 | 9170054 | CO Employer Pension Rate | social_security | `retro_simple_tax_post_formula` | formula |
| 55 | 9170055 | CO Occupational-Risk Rate | social_security | `retro_simple_tax_post_formula` | formula |
| 56 | 9170056 | CO Health Contribution (EE and ER) | social_security | `retro_simple_tax_post_formula` | flat |
| 57 | 9170057 | CO Pension Contribution (EE and ER) | social_security | `retro_simple_tax_post_formula` | flat |
| 58 | 9170058 | CO Solidarity Fund - Solidarity (EE) | social_security | `retro_simple_tax_post_formula` | flat |
| 59 | 9170059 | CO Solidarity Fund - Subsistence (EE) | social_security | `retro_simple_tax_post_formula` | flat |
| 60 | 9170060 | CO Occupational Risk (ER) | social_security | `retro_simple_tax_post_formula` | flat |
| 61 | 9170061 | CO Family Compensation Fund (ER) 4% | social_security | `retro_simple_tax_post_formula` | flat |
| 62 | 9170062 | CO SENA (ER) 2% | social_security | `retro_simple_tax_post_formula` | flat |
| 63 | 9170063 | CO ICBF (ER) 3% | social_security | `retro_simple_tax_post_formula` | flat |
| 64 | 9170064 | CO Contributor Type 51 Pension (EE and ER) | social_security | `retro_simple_tax_post_formula` | flat |
| 65 | 9170065 | CO Contributor Type 51 Occupational Risk (ER) | social_security | `retro_simple_tax_post_formula` | flat |
| 66 | 9170066 | CO Contributor Type 51 Family Compensation Fund (ER) | social_security | `retro_simple_tax_post_formula` | flat |
| 67 | 9170067 | CO Total Employee Contributions | social_security | `retro_simple_tax_post_formula` | formula |
| 68 | 9170068 | CO Total Employer Contributions and Levies | social_security | `retro_simple_tax_post_formula` | formula |
| 72 | 9170072 | CO Taxable Labour Payments (monthly read) | income_tax | `simple_tax` | flat |
| 73 | 9170073 | CO Service Bonus in the Procedure 2 Base | income_tax | `simple_tax` | flat |
| 74 | 9170074 | CO Projection Factor for Periods Shorter than 30 Days | income_tax | `simple_tax_post_formula` | formula |
| 75 | 9170075 | CO Non-taxable Income (contributions and voluntary RAIS) | income_tax | `simple_tax_post_formula` | formula |
| 76 | 9170076 | CO Net Income | income_tax | `simple_tax_post_formula` | formula |
| 77 | 9170077 | CO Dependants Deduction | income_tax | `simple_tax_post_formula` | formula |
| 78 | 9170078 | CO Prepaid Health Deduction | income_tax | `simple_tax_post_formula` | formula |
| 79 | 9170079 | CO Mortgage Interest Deduction | income_tax | `simple_tax_post_formula` | formula |
| 80 | 9170080 | CO Voluntary Pension / AFC Exempt | income_tax | `simple_tax_post_formula` | formula |
| 81 | 9170081 | CO 25% Exempt Labour Income (computed last) | income_tax | `simple_tax_post_formula` | formula |
| 82 | 9170082 | CO 40% / 1,340 UVT Cap | income_tax | `simple_tax_post_formula` | formula |
| 83 | 9170083 | CO Reliefs Applied within the Cap | income_tax | `simple_tax_post_formula` | formula |
| 84 | 9170084 | CO Taxable Base | income_tax | `simple_tax_post_formula` | formula |
| 85 | 9170085 | CO Procedure 1 Tax before Rounding | income_tax | `simple_tax_post_formula` | formula |
| 86 | 9170086 | CO Withholding - Procedure 1 | income_tax | `simple_tax_post_formula` | formula |
| 87 | 9170087 | CO Withholding - Procedure 2 | income_tax | `simple_tax_post_formula` | formula |
| 88 | 9170088 | CO Termination Withholding Percentage (12-month average) | income_tax | `simple_tax_post_formula` | formula |
| 89 | 9170089 | CO Withholding - Indemnities | income_tax | `simple_tax_post_formula` | flat |
| 90 | 9170090 | CO Withholding - Retirement Bonus | income_tax | `simple_tax_post_formula` | flat |
| 91 | 9170091 | CO Service Bonus Exempt 25% | income_tax | `simple_tax_post_formula` | flat |
| 92 | 9170092 | CO Service Bonus Reliefs within the Cap | income_tax | `simple_tax_post_formula` | flat |
| 93 | 9170093 | CO Withholding - Service Bonus (Procedure 1) | income_tax | `simple_tax_post_formula` | flat |
| 132 | 9170132 | CO Income Tax Flat | income_tax | `simple_tax_post_formula` | flat |
| 139 | 9170139 | CO Total Withholding | income_tax | `simple_tax_post_formula` | formula |
| 141 | 9170141 | CO Net Pay | income_tax | `simple_tax_post_formula` | formula |

**79 regulations.** Order rule (checked mechanically): every account a regulation reads is an input, a flag, a constant, or is posted by a lower ordinal. Earnings and payments that feed the bases (vacation, service bonus, severance savings, illness and leave benefits, indemnity) therefore run **before** the bases (ordinals 9–32); the withholding chain runs after the contributions it deducts; the non-resident flat tax keeps the development team's ordinal 132, and the totals follow it (139, 141).

**Contributions.** One regulation per fund, with an employee band (`employeeRate`) and an employer band (`employerRate`), as the development team codes them. The contribution of each contributor and fund is rounded once, up to the next COP 100 (Decree 780 of 2016 art. 3.2.1.5 num. 2: "El valor de los aportes liquidados por cada cotizante … deberá aproximarse al múltiplo de 100 superior más cercano"; PILA AT2 v30 field 47 = IBC × total rate); employee share rounded up, employer share = rounded total − employee share. The non-taxable income uses the contributions withheld from the employee (Tax Code arts. 55, 56: "los aportes obligatorios que efectúen los trabajadores").

**Rule groups.** Income-tax regulations have no `retro_`, as the development team's draft 9170132: Procedure 1 applies the table to the payments made in the month (Decree 1625 of 2016 art. 1.2.4.1.3). Social-security regulations, and the earnings and benefits that feed them, keep `retro_` — **Deliberate divergence (law)**: contributions belong to the period earned, and a retroactive correction is re-filed for that period (PILA Technical Annex 2 v30, planilla N: record A original, record C corrected IBC).

## PART 4 — Regulation detail

> Days follow the 30-day convention (Labour Code art. 134). `ROUND` = to the peso, half up; `CEILING(x;1)` = up to the peso; contributions `MULTIPLY(CEILING(DIVIDE($band_amount_raw;100);1);100)` = up to the next COP 100 per contributor and fund (Decree 780 of 2016 art. 3.2.1.5, as substituted by Decree 1990 of 2016 art. 1). No `EQUALS(...;0)` anywhere.

### 9170009 — CO All-inclusive Salary for the Period (ordinal 9)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `LESS($58201;2)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `R303`** : `MULTIPLY($64992;DIVIDE($58295;30))`
- **Law:** Labour Code art. 132; 30-day month (art. 134)
- **Deliberate divergence (law)** (see Part 3).

### 9170010 — CO Basic Salary for the Period (ordinal 10)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `AND(GREATER($58201;1);LESS($58208;1))`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `R302`** : `MULTIPLY($64992;DIVIDE($58295;30))`
- **Law:** 30-day month (Labour Code art. 134; CCG Mod. 4.3)
- **Deliberate divergence (law)** (see Part 3).

### 9170011 — CO Apprentice Maintenance Support (ordinal 11)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `GREATER($58208;0)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `R338`** : `MULTIPLY(MULTIPLY($52501;IF(LESS($58208;2);0.75;1));DIVIDE($58295;30))`
- **Law:** Labour Code art. 81 (Law 2466 of 2025 art. 21)
- **Deliberate divergence (law)** (see Part 3).

### 9170012 — CO Overtime and Premium Hours (ordinal 12)

`social_security` · `retro_simple_tax_post_formula` · formula

- **Wage types / accounts:** none (formula reads accounts)
- **→ `R308`** per hours line `H308` · : `MULTIPLY(MULTIPLY($hours;DIVIDE($64992;$52504));0.35)`
- **→ `R306`** per hours line `H306` · : `MULTIPLY(MULTIPLY($hours;DIVIDE($64992;$52504));1.25)`
- **→ `R307`** per hours line `H307` · : `MULTIPLY(MULTIPLY($hours;DIVIDE($64992;$52504));1.75)`
- **→ `R309`** per hours line `H309` · : `MULTIPLY(MULTIPLY($hours;DIVIDE($64992;$52504));ADD(1;$52505))`
- **→ `R312`** per hours line `H312` · : `MULTIPLY(MULTIPLY($hours;DIVIDE($64992;$52504));ADD(1.35;$52505))`
- **→ `R310`** per hours line `H310` · : `MULTIPLY(MULTIPLY($hours;DIVIDE($64992;$52504));ADD(1.25;$52505))`
- **→ `R311`** per hours line `H311` · : `MULTIPLY(MULTIPLY($hours;DIVIDE($64992;$52504));ADD(1.75;$52505))`
- **Law:** Labour Code arts. 168, 179; hours divisor Law 2101 of 2021 art. 3 (by the date worked)
- **Deliberate divergence (law)** (see Part 3).

### 9170013 — CO Transport Allowance (ordinal 13)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `AND(GREATER($58201;1);NOT(EQUALS($58208;1)))`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `R304`** : `IF(LTE($64992;MULTIPLY($52501;2));MULTIPLY($52503;DIVIDE($58295;30));0)`
- **Law:** Decree 1258 of 1959 art. 5; Law 15 of 1959 art. 2; Decree 1470 of 2025
- **Deliberate divergence (law)** (see Part 3).

### 9170014 — CO Vacation Base (ordinal 14)

`social_security` · `retro_simple_tax_post_formula` · flat

- **Wage types / accounts:** WTC column X: 119 rows true, 155 false (`CO_Taxability_Matrices_v2_0.md`)
- **→ `58175`** rate 100%
- **Law:** Labour Code art. 192 num. 1 (WTC column X)
- **Deliberate divergence (law)** (see Part 3).

### 9170015 — CO Vacation Daily Value (ordinal 15)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `GREATER($58175;0)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58178`** : `ROUND(DIVIDE($58175;30))`
- **Deliberate divergence (law)** (see Part 3).

### 9170016 — CO Vacation Taken (ordinal 16)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `AND(GREATER($58175;0);GREATER($58292;0))`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `R323`** : `ROUND(MULTIPLY(DIVIDE($58175;30);$58292))`
- **Law:** Labour Code arts. 186, 192
- **Deliberate divergence (law)** (see Part 3).

### 9170017 — CO Vacation Compensated in Cash (ordinal 17)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `AND(AND(GREATER($58175;0);GREATER($58293;0));LTE($58293;7.5))`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `R324`** : `ROUND(MULTIPLY(DIVIDE($58175;30);$58293))`
- **Law:** Labour Code art. 189 num. 1 (at most half of the 15 days)
- **Deliberate divergence (law)** (see Part 3).

### 9170018 — CO Vacation Compensation Above Half (block flag) (ordinal 18)

`social_security` · `retro_simple_tax_post_formula` · formula

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58217`** : `IF(GREATER($58293;7.5);1;2)`
- **Law:** Labour Code art. 189 num. 1
- **Note:** 1 = request above half the entitlement: blocked, no payment (17 does not run)
- **Deliberate divergence (law)** (see Part 3).

### 9170019 — CO Vacation Paid on Termination (ordinal 19)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `AND(GREATER($58175;0);GREATER($58294;0))`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `R156`** : `ROUND(DIVIDE(MULTIPLY($58175;$58294);720))`
- **Law:** Labour Code art. 189 num. 2 (proportional, days / 720)
- **Deliberate divergence (law)** (see Part 3).

### 9170020 — CO Statutory-Benefit Base (ordinal 20)

`social_security` · `retro_simple_tax_post_formula` · flat

- **Wage types / accounts:** WTC column W: 168 rows true, 111 false (`CO_Taxability_Matrices_v2_0.md`)
- **→ `58171`** rate 100%
- **Law:** Labour Code art. 253; transport allowance in the base (Law 1 of 1963 art. 7) through WTC row R304 (column W = Yes)
- **Note:** v2: the transport allowance enters only through its WTC row (W = Yes); v1.2 added 52503 again by formula
- **Deliberate divergence (law)** (see Part 3).

### 9170021 — CO Service Bonus (ordinal 21)

`social_security` · `retro_simple_tax_post_formula` · flat · assertion `GREATER($58297;0)`

- **Wage types / accounts:** `58171`
- **→ `R320`** rate 100%: `ROUND(DIVIDE(MULTIPLY($band_amount_raw;$58297);360))`
- **Law:** Labour Code art. 306
- **Deliberate divergence (law)** (see Part 3).

### 9170022 — CO Severance Savings (ordinal 22)

`social_security` · `retro_simple_tax_post_formula` · flat · assertion `GREATER($58298;0)`

- **Wage types / accounts:** `58171`
- **→ `R321`** rate 100%: `ROUND(DIVIDE(MULTIPLY($band_amount_raw;$58298);360))`
- **Law:** Labour Code art. 249; Law 50 of 1990 art. 99
- **Deliberate divergence (law)** (see Part 3).

### 9170023 — CO Interest on Severance Savings (ordinal 23)

`social_security` · `retro_simple_tax_post_formula` · flat · assertion `GREATER($58298;0)`

- **Wage types / accounts:** `58171`
- **→ `R322`** rate 100%: `ROUND(DIVIDE(MULTIPLY(MULTIPLY(DIVIDE(MULTIPLY($band_amount_raw;$58298);360);$58298);0.12);360))`
- **Law:** Law 50 of 1990 art. 99 num. 2; Law 52 of 1975 art. 1
- **Deliberate divergence (law)** (see Part 3).

### 9170024 — CO Illness Benefit Days 1-2 (employer) (ordinal 24)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `GREATER($58290;0)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `R326`** : `ROUND(MULTIPLY(MAX(MULTIPLY(DIVIDE($64992;30);DIVIDE(2;3));DIVIDE($52501;30));MIN($58290;2)))`
- **Law:** Labour Code art. 227 (two thirds); Decree 780 of 2016 art. 3.2.1.10 par. 1; Constitutional Court C-543 of 2007 (resolutive part: the art. 227 benefit "no podrá ser inferior al salario mínimo legal vigente"), applied per day to every segment
- **Deliberate divergence (law)** (see Part 3).

### 9170025 — CO Illness Benefit Days 3-90 (health insurer) (ordinal 25)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `GREATER($58290;2)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `R327`** : `ROUND(MULTIPLY(MAX(MULTIPLY(DIVIDE($64992;30);DIVIDE(2;3));DIVIDE($52501;30));MAX(SUBTRACT(MIN($58290;90);2);0)))`
- **Law:** Labour Code art. 227; Constitutional Court C-543 of 2007 (resolutive part: the art. 227 benefit "no podrá ser inferior al salario mínimo legal vigente"), applied per day to every segment
- **Deliberate divergence (law)** (see Part 3).

### 9170026 — CO Illness Benefit Days 91-180 (health insurer) (ordinal 26)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `GREATER($58290;90)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `R327`** : `ROUND(MULTIPLY(MAX(MULTIPLY(DIVIDE($64992;30);0.5);DIVIDE($52501;30));MAX(SUBTRACT(MIN($58290;180);90);0)))`
- **Law:** Labour Code art. 227 (one half from day 91); Constitutional Court C-543 of 2007 (resolutive part: the art. 227 benefit "no podrá ser inferior al salario mínimo legal vigente"), applied per day to every segment
- **Note:** v2: the minimum-wage floor binds here for salaries below 2 SMMLV (half the daily salary < SMMLV / 30)
- **Deliberate divergence (law)** (see Part 3).

### 9170027 — CO Illness Benefit Total (ordinal 27)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `GREATER($58290;0)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58196`** : `ROUND(ADD(ADD(MULTIPLY(MAX(MULTIPLY(DIVIDE($64992;30);DIVIDE(2;3));DIVIDE($52501;30));MIN($58290;2));MULTIPLY(MAX(MULTIPLY(DIVIDE($64992;30);DIVIDE(2;3));DIVIDE($52501;30));MAX(SUBTRACT(MIN($58290;90);2);0)));MULTIPLY(MAX(MULTIPLY(DIVIDE($64992;30);0.5);DIVIDE($52501;30));MAX(SUBTRACT(MIN($58290;180);90);0))))`
- **Deliberate divergence (law)** (see Part 3).

### 9170028 — CO Contribution Base of the Illness Days (ordinal 28)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `GREATER($58290;0)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58195`** : `ROUND(MAX(ADD(ADD(MULTIPLY(MAX(MULTIPLY(DIVIDE($64992;30);DIVIDE(2;3));DIVIDE($52501;30));MIN($58290;2));MULTIPLY(MAX(MULTIPLY(DIVIDE($64992;30);DIVIDE(2;3));DIVIDE($52501;30));MAX(SUBTRACT(MIN($58290;90);2);0)));MULTIPLY(MAX(MULTIPLY(DIVIDE($64992;30);0.5);DIVIDE($52501;30));MAX(SUBTRACT(MIN($58290;180);90);0)));MULTIPLY($52501;DIVIDE($58290;30))))`
- **Law:** Decree 780 of 2016 art. 3.2.1.10 (IBC = benefit value, never below the minimum wage)
- **Deliberate divergence (law)** (see Part 3).

### 9170029 — CO Maternity Leave Pay (ordinal 29)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `EQUALS($58291;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `R330`** : `ROUND(MULTIPLY(DIVIDE($64992;30);MULTIPLY($52542;7)))`
- **Law:** Labour Code art. 236 num. 1 (18 weeks, Law 2114 of 2021)
- **Deliberate divergence (law)** (see Part 3).

### 9170030 — CO Contribution Base of the Maternity Leave (ordinal 30)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `EQUALS($58291;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58194`** : `ROUND(MAX(MULTIPLY(DIVIDE($64992;30);MULTIPLY($52542;7));MULTIPLY(DIVIDE($52501;30);MULTIPLY($52542;7))))`
- **Deliberate divergence (law)** (see Part 3).

### 9170031 — CO Art. 64 Indemnity Days (ordinal 31)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `AND(EQUALS($58299;1);EQUALS($58220;1))`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58189`** : `IF(LTE($58288;360);IF(GTE($64992;MULTIPLY($52501;10));20;30);ADD(IF(GTE($64992;MULTIPLY($52501;10));20;30);DIVIDE(MULTIPLY(IF(GTE($64992;MULTIPLY($52501;10));15;20);SUBTRACT($58288;360));360)))`
- **Law:** Labour Code art. 64 (Law 789 of 2002 art. 28): fraction prorated
- **Deliberate divergence (law)** (see Part 3).

### 9170032 — CO Art. 64 Indemnity (ordinal 32)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `AND(EQUALS($58299;1);EQUALS($58220;1))`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `R339`** : `ROUND(MULTIPLY(DIVIDE($64992;30);$58189))`
- **Law:** Labour Code art. 64; base = art. 127 salary (SL1659-2025)
- **Deliberate divergence (law)** (see Part 3).

### 9170039 — CO Severance Savings Paid on Termination (ordinal 39)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `EQUALS($58299;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58100`** : `ADD($R321;$R322)`
- **Law:** Labour Code art. 249; Law 50 of 1990 art. 99 num. 3 (deposited to the fund by 14 February; paid to the employee only on termination)
- **Deliberate divergence (law)** (see Part 3).

### 9170040 — CO Gross Earnings (ordinal 40)

`social_security` · `retro_simple_tax` · flat

- **Wage types / accounts:** WTC column every active row: 296 rows true, 2 false (`CO_Taxability_Matrices_v2_0.md`)
- **→ `58100`** rate 100%
- **Law:** every earning row of the WTC (total devengado); deduction rows carry negative amounts (S18); severance savings and interest deposited to the fund are not paid (9170039 adds them on termination)
- **Deliberate divergence (law)** (see Part 3).

### 9170041 — CO Salary Payments of the Month (ordinal 41)

`social_security` · `retro_simple_tax` · flat

- **Wage types / accounts:** WTC column V = Salary: 160 rows true, 138 false (`CO_Taxability_Matrices_v2_0.md`)
- **→ `58101`** rate 100%
- **Law:** Labour Code art. 127 (WTC column V = Salary)
- **Deliberate divergence (law)** (see Part 3).

### 9170042 — CO Pacted Non-Salary Payments (ordinal 42)

`social_security` · `retro_simple_tax` · flat

- **Wage types / accounts:** WTC column V = Non-Salary - pacted: 54 rows true, 244 false (`CO_Taxability_Matrices_v2_0.md`)
- **→ `58102`** rate 100%
- **Law:** Labour Code art. 128 (written pact); Law 1393 of 2010 art. 30
- **Deliberate divergence (law)** (see Part 3).

### 9170043 — CO Total Remuneration (Law 1393 test) (ordinal 43)

`social_security` · `retro_simple_tax_post_formula` · formula

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58103`** : `ADD($58101;$58102)`
- **Deliberate divergence (law)** (see Part 3).

### 9170044 — CO Law 1393 Excess (ordinal 44)

`social_security` · `retro_simple_tax_post_formula` · formula

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58104`** : `MAX(SUBTRACT($58102;MULTIPLY(0.40;$58103));0)`
- **Law:** Law 1393 of 2010 art. 30; CE SU exp. 25185 of 2021 rule 3
- **Deliberate divergence (law)** (see Part 3).

### 9170045 — CO Contribution Base (IBC) - Health (ordinal 45)

`social_security` · `retro_simple_tax_post_formula` · flat

- **Wage types / accounts:** WTC column Q: 168 rows true, 122 false (`CO_Taxability_Matrices_v2_0.md`)
- **→ `58106`** rate 100%: `CEILING(MIN(MAX(ADD(MULTIPLY($band_amount_raw;IF(LESS($58201;2);0.70;1));$58104);MULTIPLY($52501;DIVIDE($58295;30)));MULTIPLY(MULTIPLY($52501;25);DIVIDE($58295;30)));1)`
- **Law:** Law 100 of 1993 arts. 18, 204 (floor 1 / ceiling 25 SMMLV prorated); all-inclusive 70% (art. 18; Labour Code art. 132); Decree 780 art. 3.2.1.5 num. 1 (up to the peso)
- **Deliberate divergence (law)** (see Part 3).

### 9170046 — CO IBC in Minimum Wages (ordinal 46)

`social_security` · `retro_simple_tax_post_formula` · formula

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58107`** : `DIVIDE($58106;MULTIPLY($52501;DIVIDE($58295;30)))`
- **Deliberate divergence (law)** (see Part 3).

### 9170047 — CO Payroll-Levy Base (ordinal 47)

`social_security` · `retro_simple_tax_post_formula` · flat

- **Wage types / accounts:** WTC column T: 160 rows true, 130 false (`CO_Taxability_Matrices_v2_0.md`)
- **→ `58108`** rate 100%: `MULTIPLY($band_amount_raw;IF(LESS($58201;2);0.70;1))`
- **Law:** Law 21 of 1982 art. 17 (no floor, no ceiling, no Law 1393 excess); Labour Code art. 132 num. 3 (70%)
- **Deliberate divergence (law)** (see Part 3).

### 9170048 — CO Art. 114-1 Exoneration Test (ordinal 48)

`social_security` · `retro_simple_tax_post_formula` · formula

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58215`** : `IF(AND(AND(LESS($58203;2);LESS($58101;MULTIPLY($52501;10)));LESS($58106;MULTIPLY($52501;10)));1;2)`
- **Law:** Tax Code art. 114-1; DIAN Conceptos 8380 of 2024, 7196 of 2025; AT2 v30 field 76
- **Deliberate divergence (law)** (see Part 3).

### 9170049 — CO IBC - Pension (ordinal 49)

`social_security` · `retro_simple_tax_post_formula` · flat

- **Wage types / accounts:** WTC column U: 167 rows true, 123 false (`CO_Taxability_Matrices_v2_0.md`)
- **→ `58112`** rate 100%: `CEILING(MIN(MAX(ADD(MULTIPLY($band_amount_raw;IF(LESS($58201;2);0.70;1));$58104);MULTIPLY($52501;DIVIDE($58295;30)));MULTIPLY(MULTIPLY($52501;25);DIVIDE($58295;30)));1)`
- **Law:** Law 100 of 1993 arts. 18, 204 (floor 1 / ceiling 25 SMMLV prorated); all-inclusive 70% (art. 18; Labour Code art. 132); Decree 780 art. 3.2.1.5 num. 1 (up to the peso)
- **Deliberate divergence (law)** (see Part 3).

### 9170050 — CO IBC - Solidarity Fund (ordinal 50)

`social_security` · `retro_simple_tax_post_formula` · flat

- **Wage types / accounts:** WTC column R: 167 rows true, 123 false (`CO_Taxability_Matrices_v2_0.md`)
- **→ `58113`** rate 100%: `CEILING(MIN(MAX(ADD(MULTIPLY($band_amount_raw;IF(LESS($58201;2);0.70;1));$58104);MULTIPLY($52501;DIVIDE($58295;30)));MULTIPLY(MULTIPLY($52501;25);DIVIDE($58295;30)));1)`
- **Law:** Law 100 of 1993 arts. 18, 204 (floor 1 / ceiling 25 SMMLV prorated); all-inclusive 70% (art. 18; Labour Code art. 132); Decree 780 art. 3.2.1.5 num. 1 (up to the peso)
- **Deliberate divergence (law)** (see Part 3).

### 9170051 — CO IBC - Occupational Risk (ordinal 51)

`social_security` · `retro_simple_tax_post_formula` · flat

- **Wage types / accounts:** WTC column S: 156 rows true, 134 false (`CO_Taxability_Matrices_v2_0.md`)
- **→ `58114`** rate 100%: `CEILING(MIN(MAX(ADD(MULTIPLY($band_amount_raw;IF(LESS($58201;2);0.70;1));$58104);MULTIPLY($52501;DIVIDE($58295;30)));MULTIPLY(MULTIPLY($52501;25);DIVIDE($58295;30)));1)`
- **Law:** Law 100 of 1993 arts. 18, 204 (floor 1 / ceiling 25 SMMLV prorated); all-inclusive 70% (art. 18; Labour Code art. 132); Decree 780 art. 3.2.1.5 num. 1 (up to the peso); no occupational risk on vacation, incapacity and leave days (Decree 1072 of 2015 art. 2.2.4.2.1.6)
- **Deliberate divergence (law)** (see Part 3).

### 9170052 — CO Contributor Type 51 Bases (ordinal 52)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `EQUALS($58216;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58197`** : `MULTIPLY($52501;DIVIDE(IF(LTE($58295;7);1;IF(LTE($58295;14);2;IF(LTE($58295;21);3;4)));4))`
- **→ `58198`** : `$52501`
- **Law:** PILA Technical Annex 2 v30, contributor type 51 (weekly quarters of the minimum wage)
- **Deliberate divergence (law)** (see Part 3).

### 9170053 — CO Solidarity Fund Subsistence Rate (ordinal 53)

`social_security` · `retro_simple_tax_post_formula` · formula · assertion `GTE($58107;4)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `52515`** : `ADD(0.5;IF(AND(GTE($58107;16);LTE($58107;17));0.2;IF(AND(GREATER($58107;17);LTE($58107;18));0.4;IF(AND(GREATER($58107;18);LTE($58107;19));0.6;IF(AND(GREATER($58107;19);LTE($58107;20));0.8;IF(GREATER($58107;20);1;0))))))`
- **Law:** Law 100 of 1993 arts. 20 and 27 (Law 797 of 2003 arts. 7 and 8)
- **Deliberate divergence (law)** (see Part 3).

### 9170054 — CO Employer Pension Rate (ordinal 54)

`social_security` · `retro_simple_tax_post_formula` · formula

- **Wage types / accounts:** none (formula reads accounts)
- **→ `52516`** : `IF(EQUALS($58212;1);22;12)`
- **Law:** Law 100 of 1993 art. 20; Decree-Law 2090 of 2003 (+10 points, high risk)
- **Deliberate divergence (law)** (see Part 3).

### 9170055 — CO Occupational-Risk Rate (ordinal 55)

`social_security` · `retro_simple_tax_post_formula` · formula

- **Wage types / accounts:** none (formula reads accounts)
- **→ `52519`** : `IF(EQUALS($58204;1);0.522;IF(EQUALS($58204;2);1.044;IF(EQUALS($58204;3);2.436;IF(EQUALS($58204;4);4.35;6.96))))`
- **Law:** Decree 1772 of 1994 art. 13; Decree 1072 of 2015 art. 2.2.4.3.5 (class initial rate; insurer rate per work centre overrides, RESEARCH_GAPS R5)
- **Deliberate divergence (law)** (see Part 3).

### 9170056 — CO Health Contribution (EE and ER) (ordinal 56)

`social_security` · `retro_simple_tax_post_formula` · flat · assertion `GREATER($58216;1)`

- **Wage types / accounts:** `58106`
- **→ `58121`** rate 4%: `IF(GREATER($58215;1);ROUND($band_amount_raw);MULTIPLY(CEILING(DIVIDE($band_amount_raw;100);1);100))`
- **→ `58141`** : `SUBTRACT(MULTIPLY(CEILING(DIVIDE(MULTIPLY($58106;0.125);100);1);100);ROUND(MULTIPLY($58106;0.04)))`
- **Law:** Law 100 art. 204 (4% + 8.5%); Tax Code art. 114-1 (employer share exonerated); Decree 780 of 2016 art. 3.2.1.5 num. 2 (Decree 1990 of 2016 art. 1): the contribution of each contributor and fund up to the next COP 100; PILA AT2 v30 field 47 (IBC x total rate)
- **Deliberate divergence (law)** (see Part 3).

### 9170057 — CO Pension Contribution (EE and ER) (ordinal 57)

`social_security` · `retro_simple_tax_post_formula` · flat · assertion `AND(AND(GREATER($58209;1);GREATER($58211;1));GREATER($58216;1))`

- **Wage types / accounts:** `58112`
- **→ `58122`** rate 4%: `ROUND($band_amount_raw)`
- **→ `58142`** : `SUBTRACT(MULTIPLY(CEILING(DIVIDE(MULTIPLY($58112;DIVIDE(ADD(4;$52516);100));100);1);100);ROUND(MULTIPLY($58112;0.04)))`
- **Law:** Law 100 art. 20 (4% + 12%; +10 high risk, Decree-Law 2090 of 2003); Decree 780 of 2016 art. 3.2.1.5 num. 2 (Decree 1990 of 2016 art. 1): the contribution of each contributor and fund up to the next COP 100; PILA AT2 v30 field 47 (IBC x total rate)
- **Deliberate divergence (law)** (see Part 3).

### 9170058 — CO Solidarity Fund - Solidarity (EE) (ordinal 58)

`social_security` · `retro_simple_tax_post_formula` · flat · assertion `AND(AND(AND(GREATER($58209;1);GREATER($58211;1));GREATER($58216;1));GTE($58107;4))`

- **Wage types / accounts:** `58113`
- **→ `58123`** rate 0.5%: `MULTIPLY(CEILING(DIVIDE($band_amount_raw;100);1);100)`
- **Law:** Law 100 art. 27; Decree 780 of 2016 art. 3.2.1.5 num. 2 (Decree 1990 of 2016 art. 1): the contribution of each contributor and fund up to the next COP 100; PILA AT2 v30 field 47 (IBC x total rate)
- **Deliberate divergence (law)** (see Part 3).

### 9170059 — CO Solidarity Fund - Subsistence (EE) (ordinal 59)

`social_security` · `retro_simple_tax_post_formula` · flat · assertion `AND(AND(AND(GREATER($58209;1);GREATER($58211;1));GREATER($58216;1));GTE($58107;4))`

- **Wage types / accounts:** `58113`
- **→ `58124`** rate from `52515`: `MULTIPLY(CEILING(DIVIDE($band_amount_raw;100);1);100)`
- **Law:** Law 100 art. 27; Decree 780 of 2016 art. 3.2.1.5 num. 2 (Decree 1990 of 2016 art. 1): the contribution of each contributor and fund up to the next COP 100; PILA AT2 v30 field 47 (IBC x total rate)
- **Deliberate divergence (law)** (see Part 3).

### 9170060 — CO Occupational Risk (ER) (ordinal 60)

`social_security` · `retro_simple_tax_post_formula` · flat · assertion `GREATER($58216;1)`

- **Wage types / accounts:** `58114`
- **→ `58143`** : `MULTIPLY(CEILING(DIVIDE($band_amount_raw;100);1);100)`
- **Law:** Decree 1772 of 1994 art. 13; Decree 780 of 2016 art. 3.2.1.5 num. 2 (Decree 1990 of 2016 art. 1): the contribution of each contributor and fund up to the next COP 100; PILA AT2 v30 field 47 (IBC x total rate)
- **Deliberate divergence (law)** (see Part 3).

### 9170061 — CO Family Compensation Fund (ER) 4% (ordinal 61)

`social_security` · `retro_simple_tax_post_formula` · flat · assertion `GREATER($58216;1)`

- **Wage types / accounts:** `58108`
- **→ `58144`** : `MULTIPLY(CEILING(DIVIDE($band_amount_raw;100);1);100)`
- **Law:** Law 21 of 1982 arts. 12, 17 (never exonerated); Decree 780 of 2016 art. 3.2.1.5 num. 2 (Decree 1990 of 2016 art. 1): the contribution of each contributor and fund up to the next COP 100; PILA AT2 v30 field 47 (IBC x total rate)
- **Deliberate divergence (law)** (see Part 3).

### 9170062 — CO SENA (ER) 2% (ordinal 62)

`social_security` · `retro_simple_tax_post_formula` · flat · assertion `AND(GREATER($58215;1);GREATER($58216;1))`

- **Wage types / accounts:** `58108`
- **→ `58145`** : `MULTIPLY(CEILING(DIVIDE($band_amount_raw;100);1);100)`
- **Law:** Law 21 of 1982 art. 12; Tax Code art. 114-1; Decree 780 of 2016 art. 3.2.1.5 num. 2 (Decree 1990 of 2016 art. 1): the contribution of each contributor and fund up to the next COP 100; PILA AT2 v30 field 47 (IBC x total rate)
- **Deliberate divergence (law)** (see Part 3).

### 9170063 — CO ICBF (ER) 3% (ordinal 63)

`social_security` · `retro_simple_tax_post_formula` · flat · assertion `AND(GREATER($58215;1);GREATER($58216;1))`

- **Wage types / accounts:** `58108`
- **→ `58146`** : `MULTIPLY(CEILING(DIVIDE($band_amount_raw;100);1);100)`
- **Law:** Law 89 of 1988 art. 1; Tax Code art. 114-1; Decree 780 of 2016 art. 3.2.1.5 num. 2 (Decree 1990 of 2016 art. 1): the contribution of each contributor and fund up to the next COP 100; PILA AT2 v30 field 47 (IBC x total rate)
- **Deliberate divergence (law)** (see Part 3).

### 9170064 — CO Contributor Type 51 Pension (EE and ER) (ordinal 64)

`social_security` · `retro_simple_tax_post_formula` · flat · assertion `EQUALS($58216;1)`

- **Wage types / accounts:** `58197`
- **→ `58127`** rate 4%: `ROUND($band_amount_raw)`
- **→ `58137`** : `SUBTRACT(ROUND(MULTIPLY($58197;0.16));ROUND(MULTIPLY($58197;0.04)))`
- **Law:** PILA AT2 v30 contributor type 51 (amounts to the peso, as the annex examples; field 47 = IBC x 16%, rounded once)
- **Deliberate divergence (law)** (see Part 3).

### 9170065 — CO Contributor Type 51 Occupational Risk (ER) (ordinal 65)

`social_security` · `retro_simple_tax_post_formula` · flat · assertion `EQUALS($58216;1)`

- **Wage types / accounts:** `58198`
- **→ `58138`** : `ROUND($band_amount_raw)`
- **Law:** PILA AT2 v30 type 51: occupational risk always on 1 SMMLV
- **Deliberate divergence (law)** (see Part 3).

### 9170066 — CO Contributor Type 51 Family Compensation Fund (ER) (ordinal 66)

`social_security` · `retro_simple_tax_post_formula` · flat · assertion `EQUALS($58216;1)`

- **Wage types / accounts:** `58197`
- **→ `58139`** : `ROUND($band_amount_raw)`
- **Deliberate divergence (law)** (see Part 3).

### 9170067 — CO Total Employee Contributions (ordinal 67)

`social_security` · `retro_simple_tax_post_formula` · formula

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58129`** : `ADD(ADD(ADD($58121;$58122);ADD($58123;$58124));$58127)`
- **Deliberate divergence (law)** (see Part 3).

### 9170068 — CO Total Employer Contributions and Levies (ordinal 68)

`social_security` · `retro_simple_tax_post_formula` · formula

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58149`** : `ADD(ADD(ADD(ADD($58141;$58142);ADD($58143;$58144));ADD($58145;$58146));ADD(ADD($58137;$58138);$58139))`
- **Deliberate divergence (law)** (see Part 3).

### 9170072 — CO Taxable Labour Payments (monthly read) (ordinal 72)

`income_tax` · `simple_tax` · flat

- **Wage types / accounts:** WTC column N, with R320, R339, R340, R343, R344, R345 false (read by their own regulations): 257 rows true, 41 false (`CO_Taxability_Matrices_v2_0.md`)
- **→ `58150`** rate 100%
- **Law:** Tax Code arts. 103, 383, 388; Decree 1625 art. 1.2.4.1.3 (service bonus read separately under Procedure 1); arts. 1.2.4.1.8 and 1.2.4.1.13 (indemnities and retirement bonus withheld outside the monthly base)
- **Note:** R320 (service bonus), R339 / R340 / R343 / R344 (indemnities) and R345 (retirement bonus) are false here; R320 enters 58150 under Procedure 2 through 9170073

### 9170073 — CO Service Bonus in the Procedure 2 Base (ordinal 73)

`income_tax` · `simple_tax` · flat · assertion `AND(EQUALS($64552;1);EQUALS($58206;2))`

- **Wage types / accounts:** `R320`
- **→ `58150`** rate 100%
- **Law:** Decree 1625 art. 1.2.4.1.3, Procedure 2: the fixed percentage applies to "la totalidad de tales pagos gravables" other than severance savings and their interest; CCG v1.7 Module 6: "Under Procedure 2 ... the service bonus is folded into the ordinary monthly base"

### 9170074 — CO Projection Factor for Periods Shorter than 30 Days (ordinal 74)

`income_tax` · `simple_tax_post_formula` · formula · assertion `EQUALS($64552;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58240`** : `IF(AND(AND(EQUALS($58206;1);LESS($58214;2));AND(GREATER($58295;0);LESS($58295;30)));DIVIDE(30;$58295);1)`
- **Law:** Decree 1625 of 2016 art. 1.2.4.1.3 Procedure 1 lits. a-b ("podrá"): payments / days x 30 -> table percentage -> applied to the real payments; Procedure 1 only (factor 1 under Procedure 2)
- **Note:** option flag 58214 (1 = project, 2 = not; default 2)

### 9170075 — CO Non-taxable Income (contributions and voluntary RAIS) (ordinal 75)

`income_tax` · `simple_tax_post_formula` · formula · assertion `EQUALS($64552;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58151`** : `ADD(MULTIPLY(ADD(ADD($58121;$58122);ADD($58123;$58124));$58240);MIN($58258;MIN(MULTIPLY(0.25;$58150);MAX(SUBTRACT(MULTIPLY(2500;$52502);$58258_ytd);0))))`
- **Law:** Tax Code arts. 55, 56: "Los aportes obligatorios que efectúen los trabajadores ... no harán parte de la base para aplicar la retención" - the contributions withheld from the employee (58121-58124, rounded); voluntary RAIS 2,500 UVT a year tracked year-to-date

### 9170076 — CO Net Income (ordinal 76)

`income_tax` · `simple_tax_post_formula` · formula · assertion `EQUALS($64552;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58152`** : `SUBTRACT(MULTIPLY($58150;$58240);$58151)`

### 9170077 — CO Dependants Deduction (ordinal 77)

`income_tax` · `simple_tax_post_formula` · formula · assertion `EQUALS($64552;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58153`** : `IF(GREATER($58207;0);MIN(MULTIPLY(0.10;MULTIPLY($58150;$58240));MULTIPLY(32;$52502));0)`
- **Law:** Tax Code art. 387; Decree 1625 art. 1.2.4.1.6 num. 4.3 (the 72 UVT of art. 336 num. 3 belong to the annual return: DIAN Concepto 011383 of 2024 IV.2)

### 9170078 — CO Prepaid Health Deduction (ordinal 78)

`income_tax` · `simple_tax_post_formula` · formula · assertion `EQUALS($64552;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58154`** : `MIN($58254;MULTIPLY(16;$52502))`
- **Law:** Tax Code art. 387

### 9170079 — CO Mortgage Interest Deduction (ordinal 79)

`income_tax` · `simple_tax_post_formula` · formula · assertion `EQUALS($64552;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58155`** : `MIN($58256;MULTIPLY(100;$52502))`
- **Law:** Tax Code art. 119; Decree 1625 art. 1.2.4.1.27

### 9170080 — CO Voluntary Pension / AFC Exempt (ordinal 80)

`income_tax` · `simple_tax_post_formula` · formula · assertion `EQUALS($64552;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58156`** : `MIN($58257;MIN(MULTIPLY(0.30;MULTIPLY($58150;$58240));MAX(SUBTRACT(MULTIPLY(3800;$52502);$58156_ytd);0)))`
- **Law:** Tax Code arts. 126-1, 126-4; Decree 1625 art. 1.2.1.22.43 (3,800 UVT a year, tracked year-to-date)

### 9170081 — CO 25% Exempt Labour Income (computed last) (ordinal 81)

`income_tax` · `simple_tax_post_formula` · formula · assertion `EQUALS($64552;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58157`** : `MIN(MULTIPLY(0.25;MAX(SUBTRACT(SUBTRACT($58152;ADD(ADD($58153;$58154);$58155));$58156);0));MAX(SUBTRACT(SUBTRACT(MULTIPLY(790;$52502);$58157_ytd);$58166_ytd);0))`
- **Law:** Tax Code art. 206 num. 10 (790 UVT a year); Consejo de Estado S4 rad. 24047 of 2021

### 9170082 — CO 40% / 1,340 UVT Cap (ordinal 82)

`income_tax` · `simple_tax_post_formula` · formula · assertion `EQUALS($64552;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58158`** : `MIN(MULTIPLY(0.40;$58152);MAX(SUBTRACT(SUBTRACT(MULTIPLY(1340;$52502);$58159_ytd);$58167_ytd);0))`
- **Law:** Tax Code art. 336 num. 3; Decree 1625 art. 1.2.4.1.6 par. 3 (Decree 2231 of 2023 art. 9); CE S4 rad. 24047 of 2021

### 9170083 — CO Reliefs Applied within the Cap (ordinal 83)

`income_tax` · `simple_tax_post_formula` · formula · assertion `EQUALS($64552;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58159`** : `MIN(ADD(ADD(ADD($58153;$58154);ADD($58155;$58156));$58157);MAX($58158;0))`

### 9170084 — CO Taxable Base (ordinal 84)

`income_tax` · `simple_tax_post_formula` · formula · assertion `EQUALS($64552;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58160`** : `MAX(SUBTRACT($58152;$58159);0)`

### 9170085 — CO Procedure 1 Tax before Rounding (ordinal 85)

`income_tax` · `simple_tax_post_formula` · formula · assertion `AND(EQUALS($64552;1);EQUALS($58206;1))`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58242`** : `DIVIDE(MULTIPLY(IF(LTE(DIVIDE($58160;$52502);95);0;IF(LTE(DIVIDE($58160;$52502);150);MULTIPLY(SUBTRACT(DIVIDE($58160;$52502);95);0.19);IF(LTE(DIVIDE($58160;$52502);360);ADD(MULTIPLY(SUBTRACT(DIVIDE($58160;$52502);150);0.28);10);IF(LTE(DIVIDE($58160;$52502);640);ADD(MULTIPLY(SUBTRACT(DIVIDE($58160;$52502);360);0.33);69);IF(LTE(DIVIDE($58160;$52502);945);ADD(MULTIPLY(SUBTRACT(DIVIDE($58160;$52502);640);0.35);162);IF(LTE(DIVIDE($58160;$52502);2300);ADD(MULTIPLY(SUBTRACT(DIVIDE($58160;$52502);945);0.37);268);ADD(MULTIPLY(SUBTRACT(DIVIDE($58160;$52502);2300);0.39);770)))))));$52502);$58240)`
- **Law:** Tax Code art. 383 (table in UVT, flat lookup per band, open on the left)

### 9170086 — CO Withholding - Procedure 1 (ordinal 86)

`income_tax` · `simple_tax_post_formula` · formula · assertion `AND(EQUALS($64552;1);EQUALS($58206;1))`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58161`** : `ROUND($58242)`
- **Law:** Tax Code art. 383; rounded to the peso

### 9170087 — CO Withholding - Procedure 2 (ordinal 87)

`income_tax` · `simple_tax_post_formula` · formula · assertion `AND(EQUALS($64552;1);EQUALS($58206;2))`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58162`** : `ROUND(MULTIPLY($58160;DIVIDE($58250;100)))`
- **Law:** Tax Code art. 386; Decree 1625 arts. 1.2.4.1.3 and 1.2.4.1.4 (fixed percentage 58250, recomputed in June and December, applied to the month's taxable payments, service bonus included)

### 9170088 — CO Termination Withholding Percentage (12-month average) (ordinal 88)

`income_tax` · `simple_tax_post_formula` · formula · assertion `EQUALS($64552;1)`

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58243`** : `IF(GREATER(DIVIDE(DIVIDE($58255;MIN(12;MAX($58259;1)));$52502);0);DIVIDE(IF(LTE(DIVIDE(DIVIDE($58255;MIN(12;MAX($58259;1)));$52502);95);0;IF(LTE(DIVIDE(DIVIDE($58255;MIN(12;MAX($58259;1)));$52502);150);MULTIPLY(SUBTRACT(DIVIDE(DIVIDE($58255;MIN(12;MAX($58259;1)));$52502);95);0.19);IF(LTE(DIVIDE(DIVIDE($58255;MIN(12;MAX($58259;1)));$52502);360);ADD(MULTIPLY(SUBTRACT(DIVIDE(DIVIDE($58255;MIN(12;MAX($58259;1)));$52502);150);0.28);10);IF(LTE(DIVIDE(DIVIDE($58255;MIN(12;MAX($58259;1)));$52502);640);ADD(MULTIPLY(SUBTRACT(DIVIDE(DIVIDE($58255;MIN(12;MAX($58259;1)));$52502);360);0.33);69);IF(LTE(DIVIDE(DIVIDE($58255;MIN(12;MAX($58259;1)));$52502);945);ADD(MULTIPLY(SUBTRACT(DIVIDE(DIVIDE($58255;MIN(12;MAX($58259;1)));$52502);640);0.35);162);IF(LTE(DIVIDE(DIVIDE($58255;MIN(12;MAX($58259;1)));$52502);2300);ADD(MULTIPLY(SUBTRACT(DIVIDE(DIVIDE($58255;MIN(12;MAX($58259;1)));$52502);945);0.37);268);ADD(MULTIPLY(SUBTRACT(DIVIDE(DIVIDE($58255;MIN(12;MAX($58259;1)));$52502);2300);0.39);770)))))));DIVIDE(DIVIDE($58255;MIN(12;MAX($58259;1)));$52502));0)`
- **Law:** Decree 1625 art. 1.2.4.1.8 lits. a-b: taxable payments of the 12 months before the termination "dividiendo por doce (12), o por el número de meses de vinculación si es inferior a doce (12)"; table percentage of that average

### 9170089 — CO Withholding - Indemnities (ordinal 89)

`income_tax` · `simple_tax_post_formula` · flat · assertion `EQUALS($64552;1)`

- **Wage types / accounts:** `R339`, `R340`, `R343`, `R344`
- **→ `58164`** rate 100%: `ROUND(MULTIPLY($band_amount_raw;IF(GREATER(DIVIDE($64992;$52502);204);0.20;$58243)))`
- **Law:** Tax Code art. 401-3 and Decree 1625 art. 1.2.4.1.13 ("las indemnizaciones derivadas de una relación laboral": 20% where the worker earns more than 204 UVT); otherwise Decree 1625 art. 1.2.4.1.8. The 204-UVT test reads the monthly salary, as the CCG v1.7 worked example (Module 9: 4,500,000 = 85.92 UVT; the termination payments stay out)
- **Note:** base: R339 (art. 64), R340 (Labour Code art. 65, "como indemnización"), R343, R344

### 9170090 — CO Withholding - Retirement Bonus (ordinal 90)

`income_tax` · `simple_tax_post_formula` · flat · assertion `EQUALS($64552;1)`

- **Wage types / accounts:** `R345`
- **→ `58168`** rate 100%: `ROUND(MULTIPLY($band_amount_raw;$58243))`
- **Law:** Decree 1625 art. 1.2.4.1.8 ("bonificaciones por retiro definitivo del trabajador": table percentage of the 12-month average applied to the bonus); the 20% of Tax Code art. 401-3 covers indemnities only

### 9170091 — CO Service Bonus Exempt 25% (ordinal 91)

`income_tax` · `simple_tax_post_formula` · flat · assertion `AND(EQUALS($64552;1);EQUALS($58206;1))`

- **Wage types / accounts:** `R320`
- **→ `58166`** rate 100%: `MIN(MULTIPLY(0.25;$band_amount_raw);MAX(SUBTRACT(MAX(SUBTRACT(SUBTRACT(MULTIPLY(790;$52502);$58157_ytd);$58166_ytd);0);$58157);0))`
- **Law:** Tax Code art. 206 num. 10; Decree 1625 art. 1.2.4.1.3 Procedure 1 (own table read of the service bonus)

### 9170092 — CO Service Bonus Reliefs within the Cap (ordinal 92)

`income_tax` · `simple_tax_post_formula` · flat · assertion `AND(EQUALS($64552;1);EQUALS($58206;1))`

- **Wage types / accounts:** `R320`
- **→ `58167`** rate 100%: `MIN($58166;MIN(MULTIPLY(0.40;$band_amount_raw);MAX(SUBTRACT(MAX(SUBTRACT(SUBTRACT(MULTIPLY(1340;$52502);$58159_ytd);$58167_ytd);0);$58159);0)))`

### 9170093 — CO Withholding - Service Bonus (Procedure 1) (ordinal 93)

`income_tax` · `simple_tax_post_formula` · flat · assertion `AND(EQUALS($64552;1);EQUALS($58206;1))`

- **Wage types / accounts:** `R320`
- **→ `58165`** rate 100%: `ROUND(MULTIPLY(IF(LTE(DIVIDE(SUBTRACT($band_amount_raw;$58167);$52502);95);0;IF(LTE(DIVIDE(SUBTRACT($band_amount_raw;$58167);$52502);150);MULTIPLY(SUBTRACT(DIVIDE(SUBTRACT($band_amount_raw;$58167);$52502);95);0.19);IF(LTE(DIVIDE(SUBTRACT($band_amount_raw;$58167);$52502);360);ADD(MULTIPLY(SUBTRACT(DIVIDE(SUBTRACT($band_amount_raw;$58167);$52502);150);0.28);10);IF(LTE(DIVIDE(SUBTRACT($band_amount_raw;$58167);$52502);640);ADD(MULTIPLY(SUBTRACT(DIVIDE(SUBTRACT($band_amount_raw;$58167);$52502);360);0.33);69);IF(LTE(DIVIDE(SUBTRACT($band_amount_raw;$58167);$52502);945);ADD(MULTIPLY(SUBTRACT(DIVIDE(SUBTRACT($band_amount_raw;$58167);$52502);640);0.35);162);IF(LTE(DIVIDE(SUBTRACT($band_amount_raw;$58167);$52502);2300);ADD(MULTIPLY(SUBTRACT(DIVIDE(SUBTRACT($band_amount_raw;$58167);$52502);945);0.37);268);ADD(MULTIPLY(SUBTRACT(DIVIDE(SUBTRACT($band_amount_raw;$58167);$52502);2300);0.39);770)))))));$52502))`
- **Law:** Decree 1625 art. 1.2.4.1.3 Procedure 1: "el valor a retener es el que figure frente al intervalo al cual corresponda la respectiva prima"

### 9170132 — CO Income Tax Flat (ordinal 132)

`income_tax` · `simple_tax_post_formula` · flat · assertion `EQUALS($64552;2)`

- **Wage types / accounts:** WTC column P: 275 rows true, 23 false (`CO_Taxability_Matrices_v2_0.md`)
- **→ `58163`** rate 20%: `ROUND($band_amount_raw)`
- **Law:** Tax Code art. 408; DIAN Concepto 011108 of 29 June 2026 item 10; severance savings and interest outside the base (Law 100 of 1993 art. 135 par. 3, every payer: Constitutional Court C-397 of 1994; Decree 1625 art. 1.2.4.1.11)
- **Note:** ID, name, taxation type, tax group, rule group, assertion and ordinal of the development team's draft (CO Draft Regulations, 9170132); base = WTC column P

### 9170139 — CO Total Withholding (ordinal 139)

`income_tax` · `simple_tax_post_formula` · formula

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58169`** : `MAX(ADD(ADD(ADD($58161;$58162);ADD($58163;$58164));ADD($58165;$58168));MULTIPLY($58150;DIVIDE($58213;100)))`
- **Law:** Tax Code art. 383 par. 3 (higher rate requested in writing)

### 9170141 — CO Net Pay (ordinal 141)

`income_tax` · `simple_tax_post_formula` · formula

- **Wage types / accounts:** none (formula reads accounts)
- **→ `58170`** : `SUBTRACT(SUBTRACT(SUBTRACT(SUBTRACT($58100;$R319);$58129);$58169);ADD($58257;$58258))`
- **Law:** arithmetic residue in cash: gross less salary in kind, employee contributions, withholding and the voluntary pension / AFC / RAIS deductions; Labour Code art. 149

## PART 5 — Taxability matrices

Built mechanically from WTC v1.9 columns N–X (`CO_Taxability_Matrices_v2_0.md`, `CO_Taxability_Perimeters_Extract_v2_0.csv`; 405 rows, 298 active). The WTC has no Mercans codes yet, so every rule is an exact wage-type rule keyed by the WTC row (`R302`); re-key one to one when codes are assigned.
- `Yes/No` has no third state. **Pacted** non-salary rows (54) are false in the IBC matrices and reach the IBC only through the Law 1393 excess (`9170044`) — the sweep confirms the excess for every pacted row. The other **21** `Yes/No` rows (R6, R37, R227, R241–R248, R282, R284–R286, R338, R346 withholding, R349, R350, R353, R358) need a wage-type split at configuration (exempt part / subject part); they are false here.
- **Routing (law):** the statutory service bonus R320 is withheld on its own table read under Procedure 1 and folded into the monthly base under Procedure 2 (`9170073`) (Decree 1625 art. 1.2.4.1.3); the indemnities R339, R340, R343, R344 by Tax Code art. 401-3 / Decree 1625 art. 1.2.4.1.8 (`9170089`) and the retirement bonus R345 by Decree 1625 art. 1.2.4.1.8 (`9170090`); all are false in the monthly read `9170072`. Deduction wage types (R6, R37) carry negative amounts.
- Report-side points (no regulation impact): electronic payroll element of pacted rows AuxilioNS (NIE142) where the pact holds, otherwise AuxilioS (NIE141) (WTC v1.9 column Y); payment method 46 (Transferencia Débito Interbancario) is account-based like 47 where a client adds it to the DD mapper (DD v1.6); PILA occupational-risk rate written as a decimal (`0.0052200`).

## PART 6 — Open items

See `RESEARCH_GAPS.md` (statutory and data gaps) and `ASSUMPTIONS.md` (engine semantics to confirm in the production engine).

## PART 7 — Self-review

- Order check: 0 defects (the v1.2 order had 47: vacation, illness, maternity, service bonus, severance, indemnity and type-51 results read before they were posted).
- Independent calculation: 112 cases, 2293 values; 12 differences with its rounding convention (C-543 floor on days 91–180; one-peso type-51 pension total; one-cent annual-cap consumption); with this design's rounding the added differences are the employer residue and the non-taxable income only (`VALIDATION.md`).
- Sweep: 298 rows × 9 bases = 2,682 checks, 0 differences.
- Design checks (hand calculation from the law): 20 / 20 exact, including the four CCG v1.7 worked examples with the annual caps tracked year-to-date and the Procedure 2, retirement-bonus, short-service, projection, 204-UVT, rounding and gross / net checks.
- Employee / employer coding: 0 errors; a copy with the employer health band coded as employee is caught. Column O (table read): 0 findings.

**Change log.** v2.0 (2 November 2026): rules of v1.2 rewritten in the development team's schema and executed; finals of 2 November 2026 (CCG v1.7, WTC v1.9, DD v1.6, SIR v1.4); regulation-by-regulation table in `CHANGELOG.md`.

# CO — Colombia Payroll — Clean-Room Regulation Design v1.0

**Country:** Colombia (CO) · ISO 3166-1 numeric **170** · Currency **COP** (no minor unit in practice; amounts rounded to the peso)
**Tax year:** 2026 (calendar year) · **Regulation ID prefix:** `9170` (9 + ISO 170)
**Design basis:** `CO-CCG-001` v1.5 (14 modules, read directly), `CO-WTC-001` v1.7 (*Wage Type Catalogue*, columns N–X), `CO-DD-001` v1.4, `CO-SIR-001` v1.2, Payslip Generator v1.2, and the report specifications v1.1 (`CO-PILA-003`, `CO-PILA-007`, `CO-DIAN-001` electronic payroll, `CO-DIAN-002` Form 350, `CO-DIAN-004` Form 220, `CO-DIAN-005` Format 2276, `CO-CESANTIAS-006`) — report detail only, not regulation logic.
**Validation basis:** `CO_Simulation_2026_10_30_V1.0.xlsx` and `Tax Simulations - Colombia.xlsx` (`final/simulations`): every formula of Part 4 is reproduced there as a live Excel formula and agrees, line by line, with an independent calculation written from the statutes (2,137 compared lines, 0 differences). Worked checks below cite the case IDs of those workbooks.
**Method:** clean-room — built from the research artifacts and the primary sources they cite. No production design has been read.
**Scope of this layer (core):** the monthly statutory chain — earnings that the law defines (proration, overtime and rest-day premiums, transport allowance), the three bases (contribution base, payroll-levy base, withholding base), employee and employer contributions and levies with the art. 114-1 exoneration, withholding tax under Procedure 1 with the full depuration, the net-pay chain, the statutory benefits (service bonus, severance savings and interest, vacation), the art. 64 indemnity and the general-illness and maternity amounts. Procedure 2, the non-resident flat rate, indemnity withholding, apprentices, employed pensioners and contributor type 51 are specified as separate routed regulations. Garnishments, benefits in kind, voluntary plans beyond their withholding effect, and annual returns are outside this layer.

---

## PART 0 — CCG special-category sweep (before writing regulations)

Two sweeps run against the CCG in full: a known-term sweep (apprentice, pensioner, all-inclusive, non-resident, director, high-risk, foreign, part-time, multi-employer) and a term-independent sweep for any rule that treats a subset of employees differently. Colombia has **nine real special categories**. Naming each with a disposition is the point of this part: "checked and deferred" is a different claim from "not looked at".

| Category | CCG source | Disposition |
|---|---|---|
| **All-inclusive salary (salario integral)** | Mod. 3 Step 2; Mod. 4.6; Mod. 5.1.1 | **In core.** Flag `58201`. Contribution base and payroll-levy base = 70% of the all-inclusive salary (Law 100 of 1993 art. 18; Labour Code art. 132 num. 3); the Law 1393 excess is added **without** the 70% reduction (Consejo de Estado SU exp. 25185 of 2021; exp. 25907 of 2022). No transport allowance, no service bonus, no severance savings (the 30% benefit factor is inside the salary). Minimum 13 minimum wages (`9170020`, `9170021`). |
| **Pacted non-salary payments** | Mod. 3 Step 2; Mod. 5.1.1 | **In core.** Flag `58202` + WTC column V. The 40% test of Law 1393 of 2010 art. 30 applies only to payments desalarised by written pact; payments non-salary by nature are outside the test (`9170017`–`9170019`). |
| **Art. 114-1 exoneration** | Mod. 5.1, 5.3 | **In core.** Employer flag `58203` + monthly test `9170025`: salary payments of the month < 10 minimum wages **and** IBC < 10 minimum wages. Removes employer health 8.5%, SENA 2% and ICBF 3%; never pension, occupational risk or the family compensation fund. |
| **Apprentices (SENA)** | Mod. 4.1, 4.2, 5.2 | **In core** (`9170096`). Maintenance support 75% (classroom) / 100% (practical or dual) of the minimum wage (Labour Code art. 81, Law 2466 of 2025 art. 21); contribution base never below 1 minimum wage (Decree 0223 of 2026 art. 2.2.6.3.3.4 par. 2). Classroom phase: health and occupational risk only; practical phase: all rights of an employment contract. Flag `58208`. |
| **Employed old-age pensioners** | Mod. 5.2 | **In core as a gate.** Worker Sub-Type `01` (`58209`): pension 4% + 12% and the solidarity fund are not due; health, occupational risk and levies continue (`9170032`–`9170034`, `9170042`). |
| **High-risk pension activity** | Mod. 5.1.1 | **In core as a rate.** Flag `58212`: employer pension +10 points (26% total) under Decree-Law 2090 of 2003 (`9170042`). |
| **Foreign national not covered by a pension regime** | Mod. 2.2 | **In core as a gate.** Flag `58211`: pension affiliation voluntary (Law 100 of 1993 art. 15 num. 2, Law 797 of 2003 art. 3); when not affiliated, pension and the solidarity fund are not due. |
| **Non-residents** | Mod. 2.2, 6.2 | **Routed.** Flag `58205`: flat 20% on the gross payment (Tax Code arts. 408–415; DIAN Concepto 011108 of 29 June 2026 item 10) instead of the art. 383 table (`9170063`). Social security unchanged. |
| **Part-time by days (contributor type 51)** | Mod. 5.2 | **Routed** (`9170097`). Bases in weekly quarters of the minimum wage; occupational risk always on 1 minimum wage (PILA Technical Annex 2, contributor type 51). Outside standard corporate payroll in practice (Law 2466 of 2025 art. 34). |

**Layer 2 (named, not built):** directors paid by fees only (independent-worker contributions on 40% of the fee — not an employment relationship, outside payroll scope per the CCG); multi-employer employees (each employer contributes on its own pay, the 25-minimum-wage ceiling is shared — flag `58210` reported, cap coordination not modelled, Part 6 item 9).

**Confirmed NOT special (no branch needed):** gender (no rate, base or trigger varies by gender); age, except that 15–17-year-olds work restricted hours (a base effect, not a rate); nationality as such (only the pension-coverage case above); weekly pay frequency (same rules on the period's payments; the CCG warns only that the art. 114-1 test can flip in a single week).

---

## PART 1 — Flags and HR fields

> The engine reads numbers only; string interpretation lives in flags, never inside a regulation band. Encodings avoid `EQUALS(...;0)` throughout.

| Account | Flag / field | Definition | Values |
|---|---|---|---|
| 58201 | All-inclusive salary | `$hr.all_inclusive_salary_flag::key` **[DERIVED]** — DD "All-Inclusive Salary Flag" | 1 = all-inclusive, 2 = ordinary |
| 58202 | Non-salary pact on file | `$hr.non_salary_pact_flag::key` **[DERIVED]** — DD "Non-Salary Pact Flag" | 1 = written pact, 2 = none. Used only to validate that WTC rows of class *Non-Salary - pacted* may be paid |
| 58203 | Employer eligible for art. 114-1 | `$legal_entity_hr.exonerated_health_sena_icbf::key` **[DERIVED]** — DD legal-entity field "Exonerated from Health, SENA and ICBF (art. 114-1)" | 1 = eligible (legal-person income-tax filer, or natural person with 2+ employees), 2 = not |
| 58204 | Occupational-risk class | `$legal_entity_hr.work_centre_risk_class::key` **[DERIVED]** — DD "Work Centre Occupational Risk Class" | 1–5 (class I–V) |
| 58205 | Tax residence | `$hr.tax_residence_status::key` **[DERIVED]** — DD "Tax Residence Status" (with effective date) | 1 = resident, 2 = non-resident |
| 58206 | Withholding procedure | `$hr.withholding_procedure::key` **[DERIVED]** — DD "Withholding Procedure" | 1 = Procedure 1, 2 = Procedure 2 |
| 58207 | Dependants declared | `$hr.number_of_dependants` **[DERIVED]** — DD "Number of Dependants" | numeric 0–n; > 0 opens the art. 387 deduction |
| 58208 | Apprentice phase | `IF(EQUALS($hr.contract_type::key;'4');$hr.apprentice_phase::key;0)` **[DERIVED — phase field: Part 6 item 7]** — DD "Contract Type" 4 = apprenticeship | 0 = not an apprentice, 1 = classroom, 2 = practical / dual |
| 58209 | Employed pensioner | `IF(EQUALS($hr.worker_sub_type::key;'01');1;2)` **[DERIVED]** — DD "Worker Sub-Type" | 1 = pensioner in active service, 2 = not |
| 58210 | Multi-employer | `$hr.concurrent_employer_flag::key` **[DERIVED]** — DD "Concurrent Employer (Multi-Employer) Flag" | 1 = yes, 2 = no (reporting only in this layer) |
| 58211 | Pension not compulsory (foreign national) | `$hr.foreign_national_not_liable_to_pension::key` **[DERIVED]** — DD field of the same name | 1 = not affiliated, 2 = affiliated |
| 58212 | High-risk pension activity | `$hr.high_risk_pension_activity_flag::key` **[DERIVED]** — DD field of the same name | 1 = high-risk, 2 = not |
| 58213 | Requested withholding rate | `$hr.employee_requested_withholding_rate` **[DERIVED]** — DD "Employee-Requested Withholding Rate" | rate, blank unless requested in writing (applies only if higher) |
| 58215 | Art. 114-1 test result | produced by `9170025` | 1 = exonerated this period, 2 = not |
| 58295 | Contributory days | `$actual_prorata_days` on the 30-day convention | 1–30 |
| 58296 | Weekly contracted hours | `$hr.weekly_contracted_hours` **[DERIVED]** — DD "Weekly Contracted Hours" | numeric (42 from 15 July 2026 for full time) |
| 58299 | Separation flag | `IF(IS_NULL($employee.last_working_date);2;IF(LTE(DATE_FORMAT($employee.last_working_date;'yyyyMMdd');DATE_FORMAT($period.end_date;'yyyyMMdd'));1;2))` | 1 = leaver this period, 2 = not |

**Constants and rate accounts (52xxx)** — values of 2026; each carries its effective date and primary source:

| Account | Name | Value | Source |
|---|---|---|---|
| 52501 | Legal monthly minimum wage (SMMLV) | 1,750,905 | Decree 1469 of 29 Dec 2025 art. 1 (suspension lifted 9 Jul 2026; Decree 0159 of 2026 set the same value meanwhile) |
| 52502 | Tax value unit (UVT) | 52,374 | Resolution DIAN 000238 of 15 Dec 2025 art. 1 |
| 52503 | Transport allowance | 249,095 / month, up to 2 SMMLV inclusive | Decree 1470 of 2025 art. 1; Law 15 of 1959 art. 2 |
| 52504 | Monthly hours divisor | 220 to 14 Jul 2026; **210 from 15 Jul 2026** | Law 2101 of 2021 art. 3; Labour Code art. 161 (Law 2466 of 2025 art. 11) |
| 52505 | Rest-day / holiday surcharge | 80% from 1 Jul 2025; **90% from 1 Jul 2026**; 100% from 1 Jul 2027 | Labour Code art. 179 transitional paragraph (Law 2466 of 2025 art. 14) |
| 52506 / 52507 / 52508 | Night premium / daytime overtime / night overtime | 35% / 25% / 75% | Labour Code art. 168 nums. 1–3 |
| 52510 / 52511 | Health employee / employer | 4.0% / 8.5% | Law 100 of 1993 art. 204 (Law 1122 of 2007 art. 10) |
| 52512 | Pension total, employer share | 16%, 75% (12% / 4%) | Law 100 of 1993 art. 20 (Law 797 of 2003 art. 7) |
| 52513 | High-risk additional employer pension | 10 points | Decree-Law 2090 of 2003 |
| 52514 | Solidarity fund: solidarity / subsistence / bands | 0.5% / 0.5% from 4 SMMLV; +0.2/0.4/0.6/0.8/1.0% at [16,17], (17,18], (18,19], (19,20], > 20 | Law 100 of 1993 arts. 20 and 27 (Law 797 of 2003 arts. 7 and 8: art. 7 sets the additional 1% and the surcharges, art. 8 splits it between the two sub-accounts); PILA Technical Annex 2 v30 fields 51–52 |
| 52520 | Occupational-risk initial rates I–V | 0.522% / 1.044% / 2.436% / 4.350% / 6.960% | Decree 1772 of 1994 art. 13; Decree 1072 of 2015 art. 2.2.4.3.5 |
| 52521 / 52522 / 52523 | CCF / SENA / ICBF | 4% / 2% / 3% | Law 21 of 1982 arts. 12, 17; Law 89 of 1988 art. 1 |
| 52525 | Exoneration limit | 10 SMMLV (strictly below) | Tax Code art. 114-1 |
| 52526 / 52527 | IBC floor / ceiling | 1 / 25 SMMLV, prorated to contributory days | Law 100 of 1993 art. 18 (Law 797 of 2003 art. 5) |
| 52528 | All-inclusive factor; minimum | 70%; 13 SMMLV | Law 100 art. 18; Labour Code art. 132 |
| 52529 | Pacted non-salary limit | 40% of total remuneration | Law 1393 of 2010 art. 30 |
| 52530 | Dependants deduction | 10% of gross labour income, max 32 UVT / month | Tax Code art. 387; Decree 1625 of 2016 art. 1.2.4.1.6 num. 4.3 |
| 52531 | Prepaid health deduction | max 16 UVT / month | Tax Code art. 387; Decree 1625 art. 1.2.4.1.6 num. 4.2 |
| 52532 | Mortgage interest deduction | max 100 UVT / month | Tax Code art. 119; Decree 1625 art. 1.2.4.1.23 |
| 52533 | Voluntary pension / AFC exempt | 30% of labour income, 3,800 UVT / year | Tax Code arts. 126-1, 126-4 |
| 52534 | Exempt labour income | 25%, 790 UVT / year | Tax Code art. 206 num. 10 (Law 2277 of 2022 art. 2) |
| 52535 | Cap on deductions + exempt income | 40% of net income, 1,340 UVT / year | Tax Code art. 336 num. 3; Decree 1625 art. 1.2.4.1.6 par. 3 (Decree 2231 of 2023) |
| 52536 | Indemnity withholding | 20% where income > 204 UVT | Tax Code art. 401-3; Decree 1625 art. 1.2.4.1.13 |
| 52537 | Non-resident withholding | 20% flat | Tax Code art. 408 |
| 52538 | Voluntary contributions to the mandatory individual pension account (RAIS) | non-taxable up to 25% of labour income and 2,500 UVT / year; **outside** the 40% / 1,340 UVT cap | Tax Code art. 55 |
| 52544 | Illness benefit floor | 1 SMMLV equivalent (daily: SMMLV / 30) | Constitutional Court C-543 of 2007 (resolutive part) |
| 52540 | Interest on severance savings | 12% / year | Law 50 of 1990 art. 99 num. 2; Law 52 of 1975 art. 1 |
| 52541 | Apprentice support | 75% classroom / 100% practical, of SMMLV | Labour Code art. 81 (Law 2466 of 2025 art. 21) |
| 52542 | Maternity leave | 18 weeks | Labour Code art. 236 num. 1 (Law 2114 of 2021) |
| 52543 | Art. 64 indemnity days | < 10 SMMLV: 30 + 20 / year; ≥ 10 SMMLV: 20 + 15 / year, pro rata | Labour Code art. 64 (Law 789 of 2002 art. 28) |

---

## PART 2 — Account register

> `58100` gross · `581xx` intermediates and bases · `582xx` flags · `52xxx` constants and rates. Never used interchangeably.

### Bases and core intermediates

| Account | Type | Produced by | Consumed by | Purpose |
|---|---|---|---|---|
| 58100 | Base | 9170015 | payslip, NE | Gross earnings of the month (*total devengado*) |
| 58101 | Base | 9170016 | 18, 20, 25 | Salary payments of the month (matrix K = Salary) |
| 58102 | Base | 9170017 | 18, 19 | Pacted non-salary payments (matrix K = Non-Salary - pacted) |
| 58103 | Intermediate | 9170018 | 19 | Total remuneration for the 40% test (58101 + 58102) |
| 58104 | Intermediate | 9170019 | 21, 26, 27, 28 | Law 1393 excess |
| 58105 | Intermediate | 9170020 | 21, 23 | Salary base after the all-inclusive factor |
| 58106 | Base | 9170021 | 22, 25, 31, 41, 52 | **IBC — health** (matrix D) |
| 58107 | Intermediate | 9170022 | 33, 34 | IBC in minimum wages (FSP bands) |
| 58108 | Base | 9170023 | 44, 45, 46 | Payroll-levy base (matrix G; no floor, no ceiling, no Law 1393 excess) |
| 58109 | Base | 9170013 | 15, 51, 81 | Transport allowance |
| 58112 | Base | 9170026 | 32, 42, 52 | IBC — pension (matrix H) |
| 58113 | Base | 9170027 | 33, 34, 52 | IBC — solidarity fund (matrix E) |
| 58114 | Base | 9170028 | 43 | IBC — occupational risk (matrix F; excludes vacation, incapacity and leave days) |
| 58121–58124 | Intermediate | 9170031–34 | 39, 52 | Employee health, pension, FSP solidarity, FSP subsistence |
| 58129 | Base | 9170039 | 69, 71 | Total employee contributions |
| 58141–58146 | Intermediate | 9170041–46 | 49 | Employer health, pension, ARL, CCF, SENA, ICBF |
| 58149 | Base | 9170049 | payslip, cost | Total employer contributions and levies |
| 58150 | Base | 9170051 | 52–61 | Taxable labour payments of the month (matrix A) |
| 58151 | Intermediate | 9170052 | 53 | Non-taxable income: mandatory employee contributions + voluntary RAIS contributions within the art. 55 limit |
| 58152 | Intermediate | 9170053 | 58, 59, 60 | Net income |
| 58153–58156 | Intermediate | 9170054–57 | 58, 59 | Dependants, prepaid health, mortgage interest, AFC/AVP exempt |
| 58157 | Intermediate | 9170058 | 59 | 25% exempt labour income |
| 58158 / 58159 | Intermediate | 9170059 | 60 | Cap; reliefs applied within the cap |
| 58160 | Base | 9170060 | 61, 62 | Taxable base |
| 58161–58165 | Intermediate | 9170061–65 | 69 | Withholding by route (Procedure 1, Procedure 2, non-resident, indemnity, service-bonus read) |
| 58169 | Base | 9170069 | 71 | Total withholding |
| 58170 | Base | 9170071 | payslip, NE | Net pay |
| 58171 | Base | 9170081 | 82, 83 | Statutory-benefit base (matrix I + transport allowance) |
| 58172–58174 | Intermediate | 9170082–84 | payslip, accrual | Service bonus, severance savings, interest |
| 58175 | Base | 9170085 | 85, 86 | Vacation base (matrix J) |
| 58176 / 58177 | Intermediate | 9170085 / 86 | payslip | Vacation pay (taken or compensated) / on termination |
| 58180 | Intermediate | 9170012 | 16 | Overtime and premium hours (one sub-account per type, 58181–58187) |
| 58191 | Intermediate | 9170091 | 64 | Art. 64 indemnity |
| 58192 / 58193 | Intermediate | 9170093 | payslip | Illness: employer days 1–2 / insurer days (information) |
| 58194 | Intermediate | 9170094 | 21 | Maternity leave pay |

**Accumulation.** Colombian contributions are settled month by month with **no year-end true-up** (CCG Mod. 5.2): no regulation in this layer cumulates contribution bases. Three figures do need history and are read with `_ytm`-type reads of the prior periods: the 12-month taxable payments for the Procedure 2 percentage (`9170062`), the 12-month taxable payments for the indemnity percentage (`9170064`), and the six-month average income for the severance-savings exemption (Part 6 item 4).

---

## PART 3 — Regulation sequence

| Ord | Reg ID | Name | Tax Group | Tax Rule Group | Taxation Type |
|---|---|---|---|---|---|
| 10 | 9170010 | CO Basic Salary for the Period | social_security | `retro_simple_tax_post_formula` | Formula |
| 12 | 9170012 | CO Overtime and Premium Hours | social_security | `retro_simple_tax_post_formula` | Formula |
| 13 | 9170013 | CO Transport Allowance | social_security | `retro_simple_tax_post_formula` | Formula |
| 15 | 9170015 | CO Gross Earnings | social_security | `retro_simple_tax` | Flat |
| 16 | 9170016 | CO Salary Payments of the Month | social_security | `retro_simple_tax` | Flat |
| 17 | 9170017 | CO Pacted Non-Salary Payments | social_security | `retro_simple_tax` | Flat |
| 18 | 9170018 | CO Total Remuneration (Law 1393 test) | social_security | `retro_simple_tax_post_formula` | Formula |
| 19 | 9170019 | CO Law 1393 Excess | social_security | `retro_simple_tax_post_formula` | Formula |
| 20 | 9170020 | CO Salary Base after All-inclusive Factor | social_security | `retro_simple_tax_post_formula` | Formula |
| 21 | 9170021 | CO Contribution Base (IBC) — Health | social_security | `retro_simple_tax_post_formula` | Formula |
| 22 | 9170022 | CO IBC in Minimum Wages | social_security | `retro_simple_tax_post_formula` | Formula |
| 23 | 9170023 | CO Payroll-Levy Base | social_security | `retro_simple_tax_post_formula` | Formula |
| 25 | 9170025 | CO Art. 114-1 Exoneration Test | social_security | `retro_simple_tax_post_formula` | Formula |
| 26 | 9170026 | CO IBC — Pension | social_security | `retro_simple_tax_post_formula` | Formula |
| 27 | 9170027 | CO IBC — Solidarity Fund | social_security | `retro_simple_tax_post_formula` | Formula |
| 28 | 9170028 | CO IBC — Occupational Risk | social_security | `retro_simple_tax_post_formula` | Formula |
| 31 | 9170031 | CO Health (EE) 4% | social_security | `retro_simple_tax_post_formula` | Formula |
| 32 | 9170032 | CO Pension (EE) 4% | social_security | `retro_simple_tax_post_formula` | Formula |
| 33 | 9170033 | CO Solidarity Fund — Solidarity (EE) | social_security | `retro_simple_tax_post_formula` | Formula |
| 34 | 9170034 | CO Solidarity Fund — Subsistence (EE) | social_security | `retro_simple_tax_post_formula` | Formula |
| 39 | 9170039 | CO Total Employee Contributions | social_security | `retro_simple_tax_post_formula` | Formula |
| 41 | 9170041 | CO Health (ER) 8.5% | social_security | `retro_simple_tax_post_formula` | Formula |
| 42 | 9170042 | CO Pension (ER) 12% (+10 high-risk) | social_security | `retro_simple_tax_post_formula` | Formula |
| 43 | 9170043 | CO Occupational Risk (ER) | social_security | `retro_simple_tax_post_formula` | Formula |
| 44 | 9170044 | CO Family Compensation Fund (ER) 4% | social_security | `retro_simple_tax_post_formula` | Formula |
| 45 | 9170045 | CO SENA (ER) 2% | social_security | `retro_simple_tax_post_formula` | Formula |
| 46 | 9170046 | CO ICBF (ER) 3% | social_security | `retro_simple_tax_post_formula` | Formula |
| 49 | 9170049 | CO Total Employer Contributions and Levies | social_security | `retro_simple_tax_post_formula` | Formula |
| 51 | 9170051 | CO Taxable Labour Payments | income_tax | `retro_simple_tax` | Flat |
| 52 | 9170052 | CO Non-taxable Income (mandatory + voluntary RAIS contributions) | income_tax | `retro_simple_tax_post_formula` | Formula |
| 53 | 9170053 | CO Net Income | income_tax | `retro_simple_tax_post_formula` | Formula |
| 54 | 9170054 | CO Dependants Deduction | income_tax | `retro_simple_tax_post_formula` | Formula |
| 55 | 9170055 | CO Prepaid Health Deduction | income_tax | `retro_simple_tax_post_formula` | Formula |
| 56 | 9170056 | CO Mortgage Interest Deduction | income_tax | `retro_simple_tax_post_formula` | Formula |
| 57 | 9170057 | CO Voluntary Pension / AFC Exempt | income_tax | `retro_simple_tax_post_formula` | Formula |
| 58 | 9170058 | CO 25% Exempt Labour Income (computed last) | income_tax | `retro_simple_tax_post_formula` | Formula |
| 59 | 9170059 | CO 40% / 1,340 UVT Cap and Reliefs Applied | income_tax | `retro_simple_tax_post_formula` | Formula |
| 60 | 9170060 | CO Taxable Base | income_tax | `retro_simple_tax_post_formula` | Formula |
| 61 | 9170061 | CO Withholding — Procedure 1 (art. 383 table) | income_tax | `retro_simple_tax_post_formula` | Formula (banded, see Part 4) |
| 62 | 9170062 | CO Withholding — Procedure 2 (fixed percentage) | income_tax | `retro_simple_tax_post_formula` | Formula |
| 63 | 9170063 | CO Withholding — Non-resident 20% | income_tax | `retro_simple_tax` | Flat |
| 64 | 9170064 | CO Withholding — Dismissal Indemnity | income_tax | `retro_simple_tax_post_formula` | Formula |
| 65 | 9170065 | CO Withholding — Service Bonus Separate Read | income_tax | `retro_simple_tax_post_formula` | Formula |
| 69 | 9170069 | CO Total Withholding | income_tax | `retro_simple_tax_post_formula` | Formula |
| 71 | 9170071 | CO Net Pay | income_tax | `retro_simple_tax_post_formula` | Formula |
| 81 | 9170081 | CO Statutory-Benefit Base | social_security | `retro_simple_tax_post_formula` | Formula |
| 82 | 9170082 | CO Service Bonus (prima de servicios) | social_security | `retro_simple_tax_post_formula` | Formula |
| 83 | 9170083 | CO Severance Savings (cesantías) | social_security | `retro_simple_tax_post_formula` | Formula |
| 84 | 9170084 | CO Interest on Severance Savings | social_security | `retro_simple_tax_post_formula` | Formula |
| 85 | 9170085 | CO Vacation Pay (taken / compensated) | social_security | `retro_simple_tax_post_formula` | Formula |
| 86 | 9170086 | CO Vacation on Termination | social_security | `retro_simple_tax_post_formula` | Formula |
| 91 | 9170091 | CO Art. 64 Indemnity | social_security | `retro_simple_tax_post_formula` | Formula |
| 93 | 9170093 | CO General Illness Benefit | social_security | `retro_simple_tax_post_formula` | Formula |
| 94 | 9170094 | CO Maternity Leave Pay | social_security | `retro_simple_tax_post_formula` | Formula |
| 96 | 9170096 | CO Apprentice Support and Contribution Floor | social_security | `retro_simple_tax_post_formula` | Formula |
| 97 | 9170097 | CO Contributor Type 51 Bases | social_security | `retro_simple_tax_post_formula` | Formula |

**57 regulations**, prefix `9170`.

**Table conventions.**
- **Tax Group has two values**, `income_tax` and `social_security`. An employee who is not a contributor (e.g. a non-resident seconded under a totalisation agreement — not modelled) would suppress every `social_security` regulation; the earnings and benefit regulations are filed under `social_security` because they feed its bases.
- **Contributions are `Formula`, not `Flat`**, because each one is rounded **up to the next COP 100 per contributor and fund** (Decree 780 of 2016 art. 3.2.1.5 num. 2, as substituted by Decree 1990 of 2016 art. 1), which a flat rate × base does not do. `CEILING` is `[ASSUMED]` in the engine vocabulary (Part 6 item 1).
- **No `_ytd` regulation** is needed for social security (Part 2, Accumulation).

---

## PART 4 — Regulation detail

> Values inside formula columns are in their natural (monthly) period and never auto-divided. Days follow the 30-day convention (Labour Code art. 134; CCG Mod. 4.3). No `EQUALS(...;0)` anywhere.

### 9170010 — CO Basic Salary for the Period
`DIVIDE(MULTIPLY($band_amount_raw;$58295);30)` · matrix: the contractual salary wage type. Every month counts 30 days; a hire on the 14th of a 31-day month earns 17 days (CCG Mod. 4.3). Check: C05 (17 days at 1 SMMLV) = 992,179.50 ✓.

### 9170012 — CO Overtime and Premium Hours
Hourly value = monthly salary ÷ `52504` of the **date worked**; amount = hours × hourly value × factor:

| Type | Factor | Source |
|---|---|---|
| Night premium, ordinary hours | 0.35 | Labour Code art. 168 num. 1 |
| Daytime overtime | 1.25 | art. 168 num. 2 |
| Night overtime | 1.75 | art. 168 num. 3 |
| Rest-day / holiday ordinary hours | 1 + `52505` | art. 179 (Law 2466 of 2025 art. 14) |
| Night premium on a rest day | 1 + 0.35 + `52505` | arts. 168, 179 |
| Daytime / night overtime on a rest day | 1 + 0.25 / 0.75 + `52505` | arts. 168, 179 |

**Rules.** (1) The divisor follows the weekly hours in force on the date worked: 220 (44 h) to 14 July 2026, **210 (42 h) from 15 July 2026** (Law 2101 of 2021 art. 3) — a July payroll can carry both (H04: 10 h on 14 July = 170,454.55; 10 h on 15 July = 178,571.43 ✓). (2) The rest-day surcharge steps on **1 July 2026** from 80% to **90%** (H03 Sunday 28 June at 80%; H05 Sunday 5 July at 90% ✓). The two dates differ by two weeks; they must be two separate effective-dated constants. (3) Night hours run from 19:00 to 06:00 (Labour Code art. 160, Law 2466 of 2025 art. 10) — a time-classification input, not a formula. (4) All types are salary (Labour Code art. 127) and enter the IBC and the levy base; they are **excluded from the vacation base** (art. 192 num. 1; matrix J).

### 9170013 — CO Transport Allowance
`IF(AND(GREATER($58201;1);LTE($64992;MULTIPLY(52501;2)));DIVIDE(MULTIPLY(52503;$58295);30);0)`
Due when the contractual salary is **up to 2 minimum wages inclusive** (C02 at exactly 3,501,810 receives it; C03 at +1 COP does not ✓), never with an all-inclusive salary, prorated to the days worked (Decree 1258 of 1959 art. 5; Law 15 of 1959 art. 2). Non-salary by law: **out** of the IBC and the levy base, **in** the statutory-benefit base (Part 4, 9170081) and in taxable payments.

### 9170015 / 9170016 / 9170017 — Gross, salary and pacted non-salary
Flat sums over matrix K: `58100` = all earnings; `58101` = rows of class *Salary* (+ overtime `58180` and commissions); `58102` = rows of class *Non-Salary - pacted*. Rows *Non-Salary - non-remunerative* (transport allowance, occasional per diem, tools, work clothing, liberality payments) are in `58100` only. *Paid Rest* (vacation paid in cash) is in `58100` and the levy base, never in the IBC.

### 9170018 / 9170019 — Law 1393 test
```
58103 = ADD($58101;$58102)
58104 = MAX(SUBTRACT($58102;MULTIPLY(0.40;$58103));0)
```
**Rules (Law 1393 of 2010 art. 30; CE SU exp. 25185 of 9 Dec 2021, rule 3; UGPP ABC Empleadores 2025).** (1) Only **pacted** non-salary payments are tested; payments non-salary by nature are outside the numerator **and** the total (D03: salary 5,000,000 + 4,000,000 by nature → IBC 5,000,000 ✓). (2) The total is salary + pacted non-salary; vacation pay, indemnities, incapacities and social benefits are not in it. (3) The excess goes to health, pension (Law 100 arts. 18 and 204) and occupational risk (Decree-Law 1295 of 1994 art. 17) — **never** to the levy base. Check: D01 (official UGPP example) 5,000,000 + 4,000,000 → excess 400,000, IBC 5,400,000, CCF base 5,000,000 ✓; C24 exactly 40% → 0; C25 at 40% + 1 COP → 0.60 ✓.

### 9170020 / 9170021 — Contribution base (IBC)
```
58105 = IF(LESS($58201;2);MULTIPLY($58101;0.70);$58101)
58106 = CEILING(MIN(MAX(ADD($58105;$58104);DIVIDE(MULTIPLY(52501;$58295);30));DIVIDE(MULTIPLY(MULTIPLY(52501;25);$58295);30));1)
```
**Order (CCG Mod. 3 Step 2):** salary-only sum → Law 1393 excess → 70% for all-inclusive (the excess is **not** reduced) → floor 1 SMMLV prorated to days → ceiling 25 SMMLV prorated → **round up to the whole peso** (Decree 780 of 2016 art. 3.2.1.5 num. 1). Applying the ceiling before the 40% clamp gives a different and wrong answer. Checks: C19 25 SMMLV → 43,772,625; C21 30 SMMLV → capped 43,772,625; C22 all-inclusive 13 SMMLV → 15,933,236 (15,933,235.50 rounded up); C23 40 SMMLV all-inclusive → 70% = 49,025,340 → capped 43,772,625; D02 all-inclusive 30,000,000 + pacted 25,000,000 → 21,000,000 + 3,000,000 = **24,000,000** ✓.

### 9170022 — IBC in minimum wages
`DIVIDE($58106;DIVIDE(MULTIPLY(52501;$58295);30))` — feeds the solidarity-fund thresholds. Boundaries are tested on the exact quotient (C08 exactly 4 → FSP due; C07 4 SMMLV − 1 COP → not due ✓).

### 9170023 — Payroll-levy base
`MAX(ADD($58105;$58197_paid_rest);0)` — salary elements plus statutory and contractual paid rest days (vacation taken, compensated in cash or paid on termination: matrix G), **70% for all-inclusive** (Labour Code art. 132 num. 3), **no floor, no ceiling, no Law 1393 excess** (Law 21 of 1982 art. 17). C23: 49,025,340 × 4% = 1,961,013.60 → 1,961,100 (no 25-SMMLV cap on the levy base) ✓. *Note:* the levy base has no statutory floor; no case of a salary below the prorated minimum exists in the validation set, so the floor question is not tested (Part 6 item 3).

### 9170025 — Art. 114-1 exoneration test
`IF(AND(AND(LESS($58203;2);LESS($58101;MULTIPLY(52501;10)));LESS($58106;MULTIPLY(52501;10)));1;2)` → `58215`.
**Rules.** (1) Only the **salary payments of the month** count; non-salary payments, vacation pay, social benefits and indemnities are left out (DIAN Conceptos 8380 of 2024 and 7196 of 2025; Consejo de Estado Sección Cuarta exp. 25302 of 2022). (2) Even with salary below 10 SMMLV, an **IBC ≥ 10 SMMLV** (salary + Law 1393 excess) blocks the exoneration, because the contribution return rejects the exonerated mark at that base (PILA Technical Annex 2 v30 field 76). D04: salary 17,000,000 + pacted 20,000,000 → IBC 22,200,000 → not exonerated; D05: 17,000,000 alone → exonerated ✓. (3) Strictly below 10 SMMLV: C16 at 10 SMMLV − 1 COP exonerated, C17 at exactly 10 not ✓. (4) The test is monthly; a variable-pay employee can be exonerated one month and not the next.

### 9170026 / 9170027 / 9170028 — IBC by fund
Same expression as `9170021`, summing matrices H (pension), E (solidarity fund) and F (occupational risk) instead of D. In a month without leave the four are equal. They differ in a month with vacation taken, incapacity or licence: occupational risk is **not** due on those days (Decree 1072 of 2015 art. 2.2.4.2.1.6 num. 1.3; WTC column S = No for R123, R154, R155, R323, R326–R331), while health and pension are paid on the IBC reported before the absence (Decree 780 of 2016 art. 3.2.5.1). The IBC of the absence days is Part 6 item 5.

### 9170031–9170034 — Employee contributions

| Ord | Base | Rate | Gate | Debit | Check C08 (7,003,620) |
|---|---|---|---|---|---|
| 31 | 58106 | 4.0% | — | 58121 | 280,200 |
| 32 | 58112 | 4.0% | `GREATER($58209;1)` and `GREATER($58211;1)` (not a pensioner; affiliated) | 58122 | 280,200 |
| 33 | 58113 | 0.5% | `58107 ≥ 4` | 58123 | 35,100 |
| 34 | 58113 | 0.5% + band (0.2% at [16,17]; 0.4% (17,18]; 0.6% (18,19]; 0.8% (19,20]; 1.0% > 20) | `58107 ≥ 4` | 58124 | 35,100 |

Each line: `MULTIPLY(CEILING(DIVIDE(MULTIPLY($base;rate);100);1);100)` — up to the next COP 100. **The solidarity fund is employee-only and is never merged into the pension line** (separate NE element). Band edges: C10 exactly 16 → +0.2%; C11 exactly 17 → still +0.2%; C12 17 + 1 COP → +0.4%; C14 exactly 20 → +0.8%; C15 20 + 1 COP → +1.0% ✓. `9170039` (`58129`) = `SUM(58121:58124)`.

### 9170041–9170046 — Employer contributions and levies

| Ord | Base | Rate | Gate | Debit |
|---|---|---|---|---|
| 41 | 58106 | 8.5% | `GREATER($58215;1)` — not exonerated | 58141 |
| 42 | 58112 | 12% (+10 points when `58212 = 1`) | not pensioner; affiliated | 58142 |
| 43 | 58114 | `52520` by `58204` | — | 58143 |
| 44 | 58108 | 4% | — (never exonerated) | 58144 |
| 45 | 58108 | 2% | `GREATER($58215;1)` | 58145 |
| 46 | 58108 | 3% | `GREATER($58215;1)` | 58146 |

All rounded up to COP 100. Check C22 (all-inclusive 13 SMMLV, not exonerated because salary ≥ 10 SMMLV): health 1,354,400; pension 1,912,000; ARL 83,200; CCF 637,400; SENA 318,700; ICBF 478,000 ✓. `9170049` (`58149`) = `SUM(58141:58146)`.
**Occupational-risk rate.** `52520` holds the class **initial** rate; the insurer can set a rate within the class range (0.348%–8.700%, Decree 1772 of 1994 art. 13). The employer's notified rate per work centre must override the initial rate (Part 6 item 6).

### 9170051–9170060 — Withholding depuration (Procedure 1)
```
58150 = SUM(matrix A)                                        Tax Code arts. 103, 388
58151 = ADD(ADD(ADD($58121_raw;$58122_raw);ADD($58123_raw;$58124_raw));MIN($rais_voluntary;MIN(MULTIPLY(0.25;$58150);DIVIDE(MULTIPLY(2500;52502);12))))   Tax Code arts. 55, 56
58152 = SUBTRACT($58150;$58151)
58153 = IF(GREATER($58207;0);MIN(MULTIPLY(0.10;$58150);MULTIPLY(32;52502));0)      art. 387
58154 = MIN($prepaid_health;MULTIPLY(16;52502))                                      art. 387
58155 = MIN($mortgage_interest;MULTIPLY(100;52502))                                  art. 119
58156 = MIN($afc_avp;MIN(MULTIPLY(0.30;$58150);DIVIDE(MULTIPLY(3800;52502);12)))      arts. 126-1, 126-4
58157 = MIN(MULTIPLY(0.25;MAX(SUBTRACT(SUBTRACT($58152;ADD(ADD($58153;$58154);$58155));$58156);0));DIVIDE(MULTIPLY(790;52502);12))   art. 206 num. 10
58158 = MIN(MULTIPLY(0.40;$58152);DIVIDE(MULTIPLY(1340;52502);12))                   art. 336 num. 3; Decree 1625 art. 1.2.4.1.6 par. 3
58159 = MIN(ADD(ADD(ADD($58153;$58154);ADD($58155;$58156));$58157);$58158)
58160 = MAX(SUBTRACT($58152;$58159);0)
```
**Rules.**
1. **The 25% is computed last**, on the residue after non-taxable income, deductions and other exempt income (art. 206 num. 10, literal). R03: AFC 1,500,000 reduces the 25% to 1,445,000 ✓.
2. **The 40% / 1,340 UVT cap applies in the monthly withholding** (Decree 1625 of 2016 art. 1.2.4.1.6 par. 3, as modified by Decree 2231 of 2023). R06: reliefs 7,581,538 capped at 3,640,000 ✓; R07: capped at 1,340 × 52,374 / 12 = 5,848,430 ✓.
3. **The 72 UVT per dependant (art. 336 num. 3) is not a withholding factor**: art. 388 refers to art. 387, not art. 336 (DIAN Concepto 011383 of 2024 IV.2). It belongs to the annual return only. RC03 (two dependants): base 4,368,000, withholding 0, with 628,488 shown as information only ✓.
4. **Annual limits applied monthly as 1/12** (790 → 3,447,955; 1,340 → 5,848,430; 3,800 → 16,585,100) — no regulation prescribes the apportionment; it is an operating convention and must stay a parameter (Part 6 item 8).
5. **Non-taxable income uses the contributions before PILA rounding** (validation convention; Part 6 item 2).
6. **Voluntary contributions to the mandatory individual pension account (RAIS)** are non-taxable income under Tax Code art. 55 (up to 25% of labour income and 2,500 UVT a year) and sit **outside** the 40% / 1,340 UVT cap, unlike the voluntary-pension / AFC exempt income of arts. 126-1 and 126-4, which is inside it (`58156`).

### 9170061 — Withholding, Procedure 1 (Tax Code art. 383)
Table in UVT, intervals **open on the left** (a base exactly on a bound stays in the lower band):

| Base (UVT) | Tax (UVT) |
|---|---|
| > 0 to 95 | 0 |
| > 95 to 150 | (base − 95) × 19% |
| > 150 to 360 | (base − 150) × 28% + 10 |
| > 360 to 640 | (base − 360) × 33% + 69 |
| > 640 to 945 | (base − 640) × 35% + 162 |
| > 945 to 2,300 | (base − 945) × 37% + 268 |
| > 2,300 | (base − 2,300) × 39% + 770 |

```
58161 = IF(LESS($58206;2);ROUND(MULTIPLY(<table>(DIVIDE($58160;52502));52502));0)
```
**🔴 The table is not a pure marginal scale.** The fixed amounts are rounded: the tax just below 150 UVT is 10.45 UVT, just above it 10.00 UVT (T04: 547,308 for 149.99998 UVT; T06: 523,740 for 150.00002 UVT ✓). The same happens at 360, 640, 945 and 2,300 UVT. A native *Differential* band construct that accumulates the marginal tax of lower bands would therefore give **different results** on every base above 150 UVT; the table must be built as a flat lookup per band (fixed UVT + rate × excess over the lower bound), with the base converted to UVT first. Rounded to the peso. 18 boundary cases T01–T18 ✓.
**Requested higher rate.** Where the employee requested a higher rate in writing (`58213`), withhold the higher of the two, from the month after the request (Tax Code art. 383 par. 3).

### 9170062 — Withholding, Procedure 2
Fixed percentage recomputed in June and December: taxable payments of the previous 12 months (fewer if fewer months of service), divided by 13, depurated as above, table tax ÷ that base (Tax Code art. 386; Decree 1625 of 2016 art. 1.2.4.1.4). Applied to the monthly base `58160`. Under Procedure 2 the service bonus is folded into the monthly base. Built as a routed regulation (`LESS($58206;2)` false); the 12-month read is a `_ytm` read of `58150` (Part 6 item 4).

### 9170063 — Withholding, non-resident
`IF(GREATER($58205;1);ROUND(MULTIPLY($58150;0.20));0)` — flat 20% on the gross payment, no depuration, until the employee acquires tax residence (Tax Code art. 408; DIAN Concepto 011108 of 29 June 2026 item 10). Mutually exclusive with 9170061/62. Severance savings of a non-resident: Part 6 item 10.

### 9170064 — Withholding on the dismissal indemnity
Outside the ordinary monthly base:
```
58164 = ROUND(MULTIPLY($58191;IF(GREATER(DIVIDE($58150;52502);204);0.20;<table %>(DIVIDE($12m_taxable;12)))))
```
**Rules (Tax Code art. 401-3; Decree 1625 of 2016 arts. 1.2.4.1.8 and 1.2.4.1.13).** (1) Monthly income above 204 UVT (COP 10,684,296): 20% of the indemnity. T-B: salary 20,000,000 = 381.87 UVT → 20% × 28,083,333 = **5,616,667**. (2) Otherwise: taxable payments of the 12 months before termination ÷ 12 (or by months of service), table percentage of that average, applied to the indemnity. TI (research worked example): 58,500,000 ÷ 12 = 4,875,000 = 93.08 UVT ≤ 95 → 0%. (3) The 204-UVT test on the monthly income is a reading of the research (premise stated in CCG Mod. 6.3), not a statutory definition (Part 6 item 11).

### 9170065 — Service bonus, separate table read (Procedure 1)
Under Procedure 1 the statutory service bonus is withheld on its own table read, with its own 25% exempt income and cap (Decree 1625 of 2016 art. 1.2.4.1.3; CCG Mod. 3 Step 5). PB: 750,000 − 25% = 562,500 = 10.74 UVT → 0 ✓. How the monthly 790-UVT figure is shared between the salary read and the bonus read is Part 6 item 8.

### 9170069 / 9170071 — Total withholding and net pay
`58169 = SUM(58161:58165)`, then `MAX(58169; MULTIPLY($58150;$58213))` when a higher rate was requested. `58170 = SUBTRACT(SUBTRACT($58100;$58129);$58169)` less post-tax deductions. **Net pay is the arithmetic residue** and is not separately rounded; no deduction may bring pay below the minimum wage or into the non-attachable portion without a court order (Labour Code art. 149 num. 2).

### 9170081–9170084 — Statutory benefits
```
58171 = ADD(SUM(matrix I);IF(LTE($64992;MULTIPLY(52501;2));52503;0))     (not for all-inclusive salary)
58172 = ROUND(DIVIDE(MULTIPLY($58171;$days_in_half_year);360))           Labour Code art. 306
58173 = ROUND(DIVIDE(MULTIPLY($58171;$days_in_year);360))                Labour Code art. 249; Law 50 of 1990 art. 99
58174 = ROUND(DIVIDE(MULTIPLY(MULTIPLY($58173_raw;$days_in_year);0.12);360))   Law 50 of 1990 art. 99 num. 2
```
**Base (Labour Code art. 253):** the last monthly salary if it has not varied in the last 3 months; otherwise, and for variable salaries, the average of the last year (whole period if shorter); the service bonus on the semester average. The employer's sickness days 1–2 count as days but their amount is left out of the average (Supreme Court SL1659-2025, single instance ruling). **Rules.** (1) The transport allowance is in the base of the service bonus and of the severance savings (P02: 1,750,905 + 249,095 = 2,000,000 → 1,000,000 for 180 days ✓). (2) Vacation compensated in cash is **out** of the base (Labour Code arts. 189, 253, 306; WTC W156, W324). (3) Service bonus: 15 days by 30 June and 15 days by 20 December; severance savings settled at 31 December and deposited by 14 February; interest paid to the employee in January. (4) Monthly accruals 8.3333% / 8.3333% / 1.0000% are for the employer cost only. Checks P01–P06 ✓.

### 9170085 / 9170086 — Vacation
Base `58175` = ordinary salary, excluding overtime and rest-day work (Labour Code art. 192 num. 1; matrix J), and the transport allowance.
- **Taken:** `ROUND(MULTIPLY(DIVIDE($58175;30);$business_days))` — 15 business days per year (art. 186). V01: 3,000,000 / 30 × 15 = 1,500,000 ✓.
- **Compensated in cash during employment:** same formula, **at most half** of the entitlement (art. 189 num. 1); a request above 7.5 days must be blocked (V03 ✓). Not ÷ 720.
- **On termination:** `ROUND(DIVIDE(MULTIPLY($58175;$days_without_vacation);720))` (V05: 360 days → 1,500,000 ✓).
- Vacation **taken**: health and pension on the IBC before the vacation, no occupational risk (Part 4, 9170028). Vacation **paid in cash**: out of the IBC (CE S4 exp. 26941 of 2024; SU 25185 rule 1) but **in the levy base** (Law 21 of 1982 art. 17).

### 9170091 — Art. 64 indemnity (indefinite-term contract, dismissal without just cause)
```
days360 = (Y2−Y1)×360 + (M2−M1)×30 + (MIN(D2;30) − MIN(D1;30)) + 1
days    = IF(days360 ≤ 360; first; first + additional × (days360 − 360) / 360)
first / additional = 30 / 20 when salary < 10 SMMLV; 20 / 15 when ≥ 10 SMMLV
58191   = ROUND(salary / 30 × days)
```
**Base:** the salary of Labour Code art. 127, variable parts included — fixed salary: the last salary; variable salary: the average actually earned in the last year of effective service, suspension periods excluded (art. 253 by analogy; Supreme Court, Labour Chamber, SL1659-2025). The **transport allowance is not in the base** (not salary: arts. 64 and 127). The same base selects the tier. **Rules (Labour Code art. 64, Law 789 of 2002 art. 28).** The fraction of a year is **prorated, not truncated** ("proporcionalmente por fracción"). T-A (4 years 6½ months, < 10 SMMLV): 1,636 days → 100.889 days → 16,814,815 ✓; T-D / T-E switch tiers exactly at 10 SMMLV ✓. Fixed-term contracts (salaries for the remaining term), the probation period, and the transitional table for employees with 10+ years at 27 Dec 2002 are not in this regulation (Part 6 item 12). The Law 789 transitional scale (Law 50 of 1990 art. 6 lits. b–d) for employees with 10+ years at its entry into force is a research rule not yet built (Part 6 item 12).

### 9170093 — General illness benefit
Days 1–2 paid by the employer, from day 3 by the health insurer; 2/3 of the daily salary for days 1–90 and 1/2 for days 91–180 (Labour Code art. 227; Decree 780 of 2016 art. 3.2.1.10 par. 1). I03 (100 days, 3,000,000): 133,333 + 5,866,667 + 500,000 = 6,500,000 ✓. IBC for the incapacity days = the benefit value, never below the prorated minimum wage (Decree 780 art. 3.2.1.10; I04: 10,505,430 ✓). **Floor:** the benefit never falls below the minimum-wage equivalent (`52544`; Constitutional Court C-543 of 2007; Concepto MinSalud 202311602174531 of 20 October 2023 confirms 2/3 for the employer's days 1–2): `MAX(salary / 30 × rate; SMMLV / 30) × days`, default on, configurable. No validation case triggers it (all at 3,000,000: 66,667 > 58,364 a day). A client paying 100% is lawful (more favourable, Labour Code art. 13): 66.67% is a configurable default. The benefit amount is outside the salary average for prima, cesantías and vacation (SL1659-2025) and outside the levy base (Law 21 of 1982 art. 17; Consejo de Estado exp. 23856 of 2021).

### 9170094 — Maternity leave
18 weeks = 126 days at the salary earned at the start of the leave (Labour Code art. 236 num. 1). M01: 12,600,000 ✓. IBC = leave value, floored at the minimum wage. Occupational risk not due on leave days (WTC S330 = No).

### 9170096 — Apprentice
```
support = MULTIPLY(52501; IF(LESS($58208;2);0.75;1.00))          Labour Code art. 81
58106   = CEILING(MAX(support; 52501);1)                          Decree 0223 of 2026 art. 2.2.6.3.3.4 par. 2
```
Classroom phase (`58208 = 1`): health and occupational risk only, employee deductions on the 1-SMMLV base (AP1: health 70,100, ARL 9,200; pension and levies 0). Practical / dual phase (`58208 = 2`): all contributions and levies as for an employee (AP2: pension 70,100 / 210,200; ARL 9,200; CCF 70,100; SENA and ICBF exonerated). Practical phase: the apprentice is entitled to "all the benefits, allowances and other rights proper to an employment contract" (art. 81) — the transport allowance is due on the general rule (<= 2 SMMLV; AP2: 249,095, outside the contribution base). Classroom phase: not stated; not paid by this design.

### 9170097 — Contributor type 51 (part-time by days)
Pension and family compensation fund on quarters of the minimum wage: 1–7 days ¼, 8–14 ½, 15–21 ¾, 22–30 1 SMMLV; occupational risk always on 1 SMMLV (PILA Technical Annex 2 v30, contributor type 51). L08 (8 days): pension base 875,453; pension 140,072 (105,054 / 35,018); ARL 9,140; CCF 35,018 ✓. Amounts rounded to the peso as in the Annex examples.

---

## PART 5 — Taxability matrices

All ten matrices are built in `CO_Taxability_Matrices_v1_0.md`, with `CO_Taxability_Perimeters_Extract_v1_0.csv` as the raw extraction, both derived mechanically from WTC v1.7 columns N–X (405 rows; 298 active, 107 `NA` in every perimeter).

**What does not condense.** WTC v1.7 has no Mercans codes in column A, so prefix wildcards are impossible: matrices are keyed by WTC row and must be re-keyed when codes are assigned.

**The one structural point.** `Yes/No` rows (N 22, O 13, P 2, Q 57, R 58, S 55, T 4, U 57, W 3, X 3) have no third state in an engine matrix. For the social-security perimeters, 58 rows carry `Yes/No`; **53 are pacted non-salary rows**: they are `No` in matrices D/E/F/H and reach the IBC only through the Law 1393 excess (`9170019`), which reproduces `Yes/No` exactly with two binary matrices. The other 5 social-security `Yes/No` rows (R6, R37, R227, R338, R358), and all 22 withholding `Yes/No` rows, need a wage-type split at configuration (Part 6 item 15).

**Divergence worth knowing.** The four IBC perimeters agree except on leave rows: occupational risk (S) is `No` for vacation taken, incapacity, maternity, paternity and parental leave, where health and pension (Q, U) are `Yes`; pension (U) and the solidarity fund (R) differ on six rows (R37, R260–R264). Each fund therefore has its own IBC account (`58106`, `58112`, `58113`, `58114`).

---

## PART 6 — Open items

| # | Item | Severity | Detail |
|---|---|---|---|
| 1 | `CEILING` unconfirmed | 🔴 Blocking | The IBC rounds **up** to the peso and each contribution **up** to COP 100 (Decree 780 art. 3.2.1.5). `CEILING` is `[ASSUMED]`; if absent, an equivalent (e.g. `ROUND(x + 0.4999999)`) must be confirmed on boundary values (C05: 992,179.50 → 992,180). |
| 2 | Split of the PILA-rounded total between employee and employer | 🟡 | Decree 780 art. 3.2.1.5 num. 2 rounds the contribution **per contributor and fund** (employee + employer together). No source read states how the rounded total is split between the payslip deduction and the employer cost. This design rounds each share separately (as the payslip and the contribution return show them); the net-pay difference is at most COP 100 per fund. |
| 3 | Levy base floor | ✅ Closed | The research is explicit: levy base with no floor and no ceiling (CCG Mod. 5.2 Step 2; Law 21 of 1982 art. 17). `58108` has no floor. |
| 4 | History reads | 🟡 | Procedure 2 percentage (12 months, art. 386), indemnity percentage (12 months, Decree 1625 art. 1.2.4.1.8) and the severance-savings exemption (exempt in full when the average monthly labour income of the last 6 months is ≤ 350 UVT, tapered above, art. 206 num. 4) need `_ytm`-type reads over 6 or 12 prior periods. Mechanism to confirm. |
| 5 | IBC of absence days | 🟡 | Vacation taken: health and pension on the IBC before the vacation (Decree 780 art. 3.2.5.1); incapacity / licence: IBC = benefit value; unpaid licence: contributory-day reduction with the PILA rate variants. Requires a per-novelty day split (PILA novelty fields), not a single monthly base. |
| 6 | Occupational-risk rate by work centre | 🟡 | `52520` carries the class initial rate. The insurer-notified rate per work centre (within 0.348%–8.700%) must override it; the DD field links the class to the work centre, not yet to the employee (contribution report finding on class mismatches). |
| 7 | Apprentice phase field and transport allowance | 🟡 | The DD carries Contract Type 4 but no phase field; `58208` needs one. Transport allowance: due in the practical phase (art. 81; closed); classroom phase not stated. |
| 8 | Monthly apportionment of annual UVT limits | 🟡 | 790, 1,340 and 3,800 UVT are annual; the 1/12 monthly apportionment is an operating convention. If the tax authority accepts a cumulative test, high-pay months could exceed the monthly figure. Also open: how the 25% budget is shared between the salary read and the service-bonus read in the same month. Keep as parameters. |
| 9 | Multi-employer ceiling | 🟡 | Each employer contributes on its own pay; the 25-SMMLV ceiling applies to the sum across employers. Not modelled (flag `58210` reporting only). |
| 10 | Non-resident severance savings | 🟡 | 20% on the nominal amount (Tax Code art. 408) is the research position; there is no DIAN doctrine on severance savings of a non-resident. |
| 11 | 204-UVT test basis | 🟡 | The indemnity 20% test is applied to the monthly income (research premise). The provision does not define the income measured. |
| 12 | Indemnity variants | 🟡 | Fixed-term (salaries for the remaining term), contract for a specific work, probation period (Labour Code arts. 76–80), Law 789 of 2002 art. 28 transitional table (10+ years at 27 Dec 2002). Not in `9170091`. |
| 13 | Variable pay in the indemnity base | ✅ Closed | Research position: art. 127 salary with variable parts; variable salary → average of the last year (art. 253 by analogy; SL1659-2025); transport allowance excluded. Written into `9170091`. Needs a 12-month history read (item 4). |
| 14 | Illness floor of 1 daily minimum wage | ✅ Closed | Constitutional Court C-543 of 2007 (floor); Concepto MinSalud 202311602174531 of 2023 (2/3 for days 1–2). Floor applied by default, configurable (`9170093`). |
| 15 | `Yes/No` split wage types | 🟡 | 5 social-security rows (R6, R37, R227, R338, R358; the 53 pacted rows are handled by the Law 1393 excess) and 22 withholding rows need an exempt / subject split at configuration (matrices file, structural finding). |
| 16 | Solidarity fund under Law 2381 of 2024 | 🟡 | The new bands of Law 2381 of 2024 art. 20 enter into force on 1 April 2027 (Constitutional Court C-264 of 2026). The contribution-return annex already carries both regimes. Not a 2026 rule; effective-date the band table. |
| 17 | Pension of a high-risk employee | 🟡 | The +10 points come from the contribution-return rate table (26% total) and Decree-Law 2090 of 2003; the employer bears them. Confirm the split with the dev team's PILA configuration. |

---

## PART 7 — Self-review

**Implicit engine behaviours interrogated up front:**
- ✅ No annual band field is used for contributions; every contribution is a formula with its own rounding, so no auto-division applies.
- ⚠ The art. 383 table: if built with band fields, they must be stated **annually** (base and bounds × 12) and the construct must be a **flat lookup with a fixed amount**, not a marginal Differential (Part 4, 9170061). Stated here in UVT inside a formula to avoid both traps.
- ✅ `EQUALS(...;0)` avoided; `LESS` / `GREATER` / `LTE` for every gate.
- ✅ Matrix zero-clamp: every perimeter has `Yes` on the basic-salary rows, so no base can silently fall to zero.

**Boundary traces (all reproduced in the simulation workbooks):**
- ✅ Transport allowance at 2 SMMLV inclusive (C02 / C03 / C04).
- ✅ Solidarity fund at 4 SMMLV inclusive and the five bands (C07–C15).
- ✅ Art. 114-1 at 10 SMMLV strictly below, and the IBC lock (C16, C17, D04, D05).
- ✅ IBC ceiling at 25 SMMLV and the all-inclusive 70% under and above it (C19–C23).
- ✅ Law 1393 at exactly 40% and 40% + 1 COP (C24, C25).
- ✅ Art. 383 table on, below and above each bound (T01–T18), including the downward steps.
- ✅ Hours divisor on 14 / 15 July 2026 and rest-day surcharge on 30 June / 1 July 2026 (H03–H05).
- ✅ Art. 64 tier at 10 SMMLV and the first-year rule (T-C, T-D, T-E).

**Truth tables enumerated:**
- ✅ `58203` × salary test × IBC test → `58215`: only (eligible, < 10, < 10) exonerates.
- ✅ `58205` × `58206`: non-resident → 9170063 only; resident × 1 → 9170061; resident × 2 → 9170062. Exactly one route per employee.
- ✅ `58201` × matrix K class: all-inclusive applies 70% to salary only, never to the Law 1393 excess.
- 🟡 `58209` × `58211` × `58212` (pensioner × pension-optional foreigner × high-risk) not walked cell by cell; each gate is independent in Part 4.

---

**Change log.** v1.0 (30 October 2026): first release, derived from the final CCG v1.5, WTC v1.7, DD v1.4, SIR v1.2, Payslip v1.2 and specs v1.1 (including the final-review corrections of 30 October 2026).

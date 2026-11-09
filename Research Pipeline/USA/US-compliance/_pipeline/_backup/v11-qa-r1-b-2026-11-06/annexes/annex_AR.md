# Annex AR: Arkansas


This annex sets out the Arkansas payroll rules for the 2026 build year. Read with Annex FED (the federal layer every employee carries) and Annex MULTI (which routes an employee to this State by work location, residence or UI localization). Every value is shown with its effective dates and its source (list at the end of the annex). Federal values are not repeated here.

Classification: T3. Separate State withholding and UI; no local wage tax.

## AR.1 Employment and labour code

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Minimum wage hourly | USD [[FACT:ar.minwage.hourly=11]] | from 2021-01-01 |  | S1 | 2018 Initiated Act (Issue 5); employers with 4+ employees; higher of state/FLSA. No 2027 increase enacted; 2026-11-03 ballot carries no initiative. |
| Minimum wage employer size min | [[FACT:ar.minwage.employer_size_min=4]] employees | from 2021-01-01 |  | S1 |  |
| Minimum wage tipped cash wage | USD [[FACT:ar.minwage.tipped.cash_wage=2.63]] | from 2021-01-01 |  | S1 | Tip credit up to minimum wage; written notice each time the tip-credit amount changes (11 CAR 11). |
| Overtime weekly threshold hours | [[FACT:ar.overtime.weekly_threshold_hours=40]] hours | from 2026-01-01 |  | S1 | 1.5x over [[FACT:ar.overtime.weekly_threshold_hours=40]]/week (11-4-211); no daily OT; agricultural and FLSA-exempt excluded. |
| Paycard free withdrawals per load | [[FACT:ar.paycard.free_withdrawals_per_load=1]] count | from 2019-07-24 |  | S2 | 11-4-403(f) (Act 853 of 2019): direct deposit or preloaded card lawful; no employee-consent clause in the text. |
| Pay frequency rule | [[FACT:ar.pay_frequency.rule=corporations pay semimonthly; corporations with gross income >= 500,000 may pay FLSA-exempt managers earning > 25,000 at least monthly (11-4-401)]] | from 2026-01-01 |  | S3 | 2008 compilation; later amendment not checked. |

## AR.2 Income tax withholding

**Method.** [[FACT:ar.wh.method=DFA Formula Method 2026: annualise; less standard deduction; band midpoint (USD 50) below 100,001; bracket formula; round annual tax to dollar; less 29 per exemption; divide by periods]]. Certificate: [[FACT:ar.wh.certificate.form=AR4EC (R 12/04/2025); federal W-4 not used; no certificate = zero exemptions; decrease reported within 10 days]].

```
annual_wages = period_wages x pay_periods
net_taxable  = annual_wages - ar_std_deduction
if net_taxable is in the band-midpoint range of the formula: net_taxable = midpoint of its 100-dollar band
annual_tax   = round_to_dollar(net_taxable x bracket.rate - bracket.subtract)   # table below
annual_tax  -= exemptions x ar_personal_credit
period_tax   = max(0, annual_tax) / pay_periods
```

Standard deduction USD [[FACT:ar.wh.std_deduction=2,470]]; personal credit USD [[FACT:ar.wh.personal_credit.per_exemption=29]] per exemption. The subtraction column was recomputed from the ceilings and rates (each row = previous subtraction + previous ceiling x rate step); every row agrees. Above the high-income threshold (USD [[FACT:ar.pit.high_income.threshold=94,700]]) the statute applies a two-band table: [[FACT:ar.pit.statute.tables=Net income <= 94,700: 0-5,599 0%; 5,600-11,199 2%; 11,200-15,999 3%; 16,000-26,399 3.4%; 26,400-94,700 3.7%. Net income > 94,700: 0-4,700 2%; 4,701+ 3.7%; bracket adjustment 290 at 94,701-94,800, stepping down 10 per 100, 0 from 97,601; tables indexed annually under 26-51-201(d)]].

**Rate change in 2026.** The top rate is [[FACT:ar.pit.rate.top=3.7]] % for tax years from 2026-01-01 (Act 1 of the 2026 First Extraordinary Session, [[FACT:ar.live.act1_2026_ex_sess.status=in force retroactive 2026-01-01 (signed week of 2026-05-04); level assessment + withholding]]). The date from which employers had to apply the reissued formula is not in the research: blocking gap below. Until it is closed, the engine cannot decide which formula applies to pay dates before the switch.

**Supplemental pay:** [[FACT:ar.wh.supplemental.rate=3.7]] %. **Texarkana:** [[FACT:ar.wh.texarkana.exemption=Texarkana AR residents exempt on all income; Texarkana TX residents exempt on wages earned in Texarkana AR (26-52-604); AR-TX-4EC; AR-3Q-TEX due 28 Feb]].

**PIT bracket: bracket table**

| Bracket | ceiling | rate | subtract | Effective | Source |
|---|---|---|---|---|---|
| 1 | USD [[FACT:ar.pit.bracket.1.ceiling=5,599]] | — | — | from 2026-01-01 | S4 |
| 2 | USD [[FACT:ar.pit.bracket.2.ceiling=11,199]] | [[FACT:ar.pit.bracket.2.rate=2]] % | USD [[FACT:ar.pit.bracket.2.subtract=111.98]] | from 2026-01-01 | S4 |
| 3 | USD [[FACT:ar.pit.bracket.3.ceiling=15,999]] | [[FACT:ar.pit.bracket.3.rate=3]] % | USD [[FACT:ar.pit.bracket.3.subtract=223.97]] | from 2026-01-01 | S4 |
| 4 | USD [[FACT:ar.pit.bracket.4.ceiling=26,399]] | [[FACT:ar.pit.bracket.4.rate=3.4]] % | USD [[FACT:ar.pit.bracket.4.subtract=287.97]] | from 2026-01-01 | S4 |
| 5 | USD [[FACT:ar.pit.bracket.5.ceiling=94,700]] | [[FACT:ar.pit.bracket.5.rate=3.7]] % | USD [[FACT:ar.pit.bracket.5.subtract=367.16]] | from 2026-01-01 | S4 |
| top | — | — | USD [[FACT:ar.pit.bracket.top.subtract=79.90]] | from 2026-01-01 | S4 |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Withholding method | [[FACT:ar.wh.method=DFA Formula Method 2026: annualise; less standard deduction; band midpoint (USD 50) below 100,001; bracket formula; round annual tax to dollar; less 29 per exemption; divide by periods]] | from 2026-01-01 |  | S4 |  |
| Withholding standard deduction | USD [[FACT:ar.wh.std_deduction=2,470]] | from 2026-01-01 |  | S4 |  |
| Withholding personal credit per exemption | USD [[FACT:ar.wh.personal_credit.per_exemption=29]] | from 2026-01-01 |  | S4 |  |
| PIT top rate | [[FACT:ar.pit.top_rate=3.7]] % | from 2026-01-01 |  | S5 | Act 1 of 2026 1st Ex. Sess. (HB 1001 = SB 1), signed week of 2026-05-04, retroactive to 2026-01-01; operating level assessment for all 2026 and withholding via the reissued formula. Table switch date open. |
| Withholding low income tables single weekly zero to | USD [[FACT:ar.wh.low_income_tables.single_weekly_zero_to=281.60]] | from 2026-01-01 |  | S6 | Separate table-only method for AR4EC line 5; 281.60x52 = 14,643.20 consistent with the AR4ECSP ceiling. |
| Withholding certificate form | [[FACT:ar.wh.certificate.form=AR4EC (R 12/04/2025); federal W-4 not used; no certificate = zero exemptions; decrease reported within 10 days]] | from 2025-12-04 |  | S7 |  |
| Withholding exemption certificate ar4ecsp ceiling single | USD [[FACT:ar.wh.exemption_certificate.ar4ecsp.ceiling.single=14,643]] | from 2026-01-01 |  | S8 | AR4ECSP 2026 ceilings [[FACT:ar.wh.exemption_certificate.ar4ecsp.ceiling.single=14,643]] / 24,695 / 29,722 / 20,820 / 24,818 (statuses per form). |
| Withholding supplemental rate | [[FACT:ar.wh.supplemental.rate=3.7]] % | from 2026-01-01 |  | S9 | Bonus/commission with regular wages; vacation pay in addition to regular pay treated as supplemental. |
| Withholding texarkana exemption | [[FACT:ar.wh.texarkana.exemption=Texarkana AR residents exempt on all income; Texarkana TX residents exempt on wages earned in Texarkana AR (26-52-604); AR-TX-4EC; AR-3Q-TEX due 28 Feb]] | from 2026-01-01 |  | S9 |  |
| PIT rate top | [[FACT:ar.pit.rate.top=3.7]] % | from 2026-01-01 |  | S5 | Act 1 of the 2026 First Extraordinary Session (HB 1001), approved 2026-05-06, A.C.A. 26-51-201(a)(4)/(a)(5); tax years beginning on/after 2026-01-01. wh.formula.switch_date). |
| PIT high income threshold | USD [[FACT:ar.pit.high_income.threshold=94,700]] | from 2026-01-01 |  | S5 | Above [[FACT:ar.pit.high_income.threshold=94,700]] net income the two-band table applies (0-4,700 2%; 4,701+ [[FACT:ar.pit.rate.top=3.7]] %). |
| PIT statute tables | [[FACT:ar.pit.statute.tables=Net income <= 94,700: 0-5,599 0%; 5,600-11,199 2%; 11,200-15,999 3%; 16,000-26,399 3.4%; 26,400-94,700 3.7%. Net income > 94,700: 0-4,700 2%; 4,701+ 3.7%; bracket adjustment 290 at 94,701-94,800, stepping down 10 per 100, 0 from 97,601; tables indexed annually under 26-51-201(d)]] | from 2026-01-01 |  | S5 | Ceilings agree with ar.pit.bracket.1-5. |

Not configured in this release [[GAP:RQ-463]]: Withholding formula switch date: not established from an official source.

## AR.2b Non-resident regime and reciprocity

No reciprocity. Sourcing: [[FACT:ar.nonres.sourcing=physical presence: work performed in AR when physically located in AR (convenience rule ended for tax years from 2021); apportion by AR working days / total working days]].

**Resident / non-resident matrix (Arkansas income tax)**

| Income type | Resident | Non-resident |
|---|---|---|
| Regular salary | Formula method (AR.2) on all wages | Formula method on wages for work physically performed in Arkansas, apportioned by Arkansas working days |
| Annual bonus / supplemental pay | [[FACT:ar.wh.supplemental.rate=3.7]] % | [[FACT:ar.wh.supplemental.rate=3.7]] % on the Arkansas portion |
| Severance | Not configured in this release [[GAP:RQ-507]]: No Arkansas-specific treatment in the sources read. | Same gap |
| Equity | Supplemental-pay treatment; federal classification of equity income in Annex FED (FED.2b) | Same, on the Arkansas portion |
| Benefits in kind | Withholding wages; cafeteria-plan exclusion ([[FACT:ar.sui.wages.section125_excluded=True]] for UI); HSA, transit and group-term life open (AR.8) | Same, on the Arkansas portion |
| Contractor pay | Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008] | Same |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Non-resident sourcing | [[FACT:ar.nonres.sourcing=physical presence: work performed in AR when physically located in AR (convenience rule ended for tax years from 2021); apportion by AR working days / total working days]] | from 2021-01-01 |  | S10 | Act 1019 of 2021, 26-51-202(c), 504(a)(1), 902(5); level assessment and withholding. No day/dollar threshold (HB1116 of 2025 died). |

## AR.2c Local wage taxes

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Local wage tax exists | [[FACT:ar.local_wage_tax.exists=False]] | from 2026-01-01 |  | S11 |  |

## AR.3 Social insurance: unemployment, disability, paid leave and payroll levies

Employer-only UI ([[FACT:ar.sui.employee.rate=0]] % employee) on wages up to the base, plus the administrative assessment. No SDI, TDI, PFML, long-term-care or transit levy.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| SUI wage base | USD [[FACT:ar.sui.wage_base=7,000]] | from 2026-01-01 |  | S12 | 11-10-215; credit for wages paid toward the former state base when an employee permanently moves with the same employer. |
| SUI new employer rate | [[FACT:ar.sui.new_employer.rate=2]] % | 2026-01-01 to 2026-12-31 |  | S13 |  |
| SUI employer rate min | [[FACT:ar.sui.employer.rate.min=0.2]] % | 2026-01-01 to 2026-12-31 |  | S13 | 0.2-[[FACT:ar.sui.employer.rate.max=5.1]]% experienced; deficit 6.1/8.1/10.1%; includes [[FACT:ar.sui.admin_assessment.rate=0.1]] % Administrative Assessment; conditional [[FACT:ar.sui.employer.rate.min=0.2]] % advance interest and [[FACT:ar.sui.admin_assessment.rate=0.1]] % extended benefit. |
| SUI employer rate max | [[FACT:ar.sui.employer.rate.max=5.1]] % | 2026-01-01 to 2026-12-31 |  | S13 |  |
| SUI admin assessment rate | [[FACT:ar.sui.admin_assessment.rate=0.1]] % | 2026-01-01 to 2026-12-31 |  | S13 |  |
| SUI employee rate | [[FACT:ar.sui.employee.rate=0]] % | from 2026-01-01 |  | S12 |  |
| SUI wages section125 excluded | [[FACT:ar.sui.wages.section125_excluded=True]] | from 2026-01-01 |  | S12 |  |

## AR.4 Pay statement

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Payslip state statute exists | [[FACT:ar.payslip.state_statute.exists=False]] | from 2026-07-21 |  | S14 | 11 CAR 11 compilation 2026-07-21; tip-credit change notice in writing. |

## AR.5 Statutory reporting

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Report SUI quarterly | [[FACT:ar.report.sui.quarterly=Tax21 online or paper DWS-ARK-209B/209BR/209BS; due 30 Apr, 31 Jul, 31 Oct, 31 Jan, also when no wages]] | from 2026-01-01 |  | S12 |  |
| Newhire report days | [[FACT:ar.newhire.report_days=20]] days | from 2026-01-01 |  | S12 | Via Tax21; all employees living or working in AR. |
| Child support verification response days | [[FACT:ar.child_support.verification_response_days=30]] days | from 2026-01-01 |  | S15 |  |
| Report withholding monthly | [[FACT:ar.report.wh.monthly=AR941M by the 15th of following month (zero voucher if nil); annual AR941A by 31 Jan when deposits under 1,000; EFT mandatory at average 20,000+/month; AR3MAR due 28 Feb]] | from 2026-01-01 |  | S9 |  |
| Report W-2 efile threshold employees | [[FACT:ar.report.w2.efile_threshold_employees=125]] employees | from 2026-01-01 |  | S9 | EFW2 via ATAP; RA, RE, RW, RS, RT, RF, RCS required; RV not allowed. |

Not configured in this release [[GAP:RQ-590]]: the employee count above which Arkansas UI wage reports must be filed electronically is not established from an official source.

## AR.6 Leave

No paid-sick-leave statute and no PFML in the research; vacation is a matter of written policy. Jury, voting and military leave are open (gap below).

Not configured in this release [[GAP:RQ-467]]: Leave mandated leave: not established from an official source.

## AR.7 Termination and final pay

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Final pay discharge | [[FACT:ar.final_pay.discharge=next regular payday; double wages if unpaid within 7 days of that payday]] | from 2019-07-24 |  | S2 | 11-4-405 (Act 853 of 2019). Resignation deadline not located. Vacation payout only if policy promises it. |
| Final pay double wages after days | [[FACT:ar.final_pay.double_wages_after_days=7]] days | from 2019-07-24 |  | S2 |  |

Not configured in this release [[GAP:RQ-464]]: Final pay resignation: not established from an official source.

## AR.8 Benefits in kind and taxable wages

Arkansas withholding wages exclude the federal exclusions for combat pay, cafeteria plans, IRAs and 401(k), 403(b), 408(k), 408(p) and 457 deferrals; non-cash wages are valued at fair market value; reported tips are wages. Employer HSA contributions outside a cafeteria plan, transit benefits and group-term life are open (gap below).

Not configured in this release [[GAP:RQ-465]]: PIT wages HSA transit GTL: not established from an official source.

## AR.9 Deductions and garnishments

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Deductions nonstandard below minimum wage | [[FACT:ar.deductions.nonstandard_below_minwage=False]] | from 2026-01-01 |  | S1 | Breakage/shortages/fines may not reduce pay below minimum wage; court orders, assignments, board/lodging/apparel may. |
| Garnishment child support arrears addon percent | [[FACT:ar.garn.child_support.arrears_addon.percent=10]] % | from 2026-01-01 |  | S16 | Usually [[FACT:ar.garn.child_support.arrears_addon.percent=10]] % of current support toward arrears, now 20% in some cases; CCPA cap; Arkansas Child Support Clearinghouse; OCSE MyWorkers. |

Not configured in this release [[GAP:RQ-466]]: Garnishment IWO employer fee: not established from an official source.

Not configured in this release [[GAP:RQ-470]]: Garnishment creditor exempt weekly: not established from an official source.

## AR.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Prevailing wage state law exists | [[FACT:ar.prevailing_wage.state_law.exists=False]] | from 2017-01-01 |  | S17 | Repealed 2017; Davis-Bacon only. |

## AR.11 Indexation

The minimum wage is not indexed; the UI base is fixed in statute; withholding amounts are republished by legislation without an index factor.

## AR.12 Payroll data protection and records

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Records wage hour retention years | [[FACT:ar.records.wage_hour.retention_years=3]] years | from 2026-01-01 |  | S18 | 11-4-217. |
| Records withholding retention years | [[FACT:ar.records.withholding.retention_years=6]] years | from 2026-01-01 |  | S9 | Including AR4EC copies. |

Not configured in this release [[GAP:RQ-468]]: Data protection SSN paystub: not established from an official source.

## AR.13 Live legal change

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Live act1 2026 ex sess status | [[FACT:ar.live.act1_2026_ex_sess.status=in force retroactive 2026-01-01 (signed week of 2026-05-04); level assessment + withholding]] | from 2026-01-01 |  | S19 |  |

Not configured in this release [[GAP:RQ-469]]: Live bulletin sweep: not established from an official source.

## AR.14 Authority worked examples (oracle values)

Authority example (DFA Formula Method 2026), recomputed line by line from the keyed parameters. Rounding: annual tax half-up to the dollar (formula step), period amount half-up to the cent.

Input: [[FACT:ar.oracle.example.1.input=monthly 2,127.00, 2 exemptions (Formula Method 2026)]].

| Line | Calculation | Result |
|---|---|---|
| Annual wages | 2,127.00 x 12 | 25,524.00 |
| Net taxable | 25,524.00 - USD [[FACT:ar.wh.std_deduction=2,470]] | 23,054.00 |
| Band midpoint | 100-dollar band of 23,054.00 | 23,050.00 |
| Bracket 4 tax | 23,050.00 x [[FACT:ar.pit.bracket.4.rate=3.4]] % - USD [[FACT:ar.pit.bracket.4.subtract=287.97]] | 783.70 - [[FACT:ar.pit.bracket.4.subtract=287.97]] = 495.73 |
| Rounded to the dollar | — | 496.00 |
| Less personal credits | 496.00 - 2 x USD [[FACT:ar.wh.personal_credit.per_exemption=29]] | 438.00 |
| Monthly withholding | 438.00 / 12 | USD [[FACT:ar.oracle.example.1.withholding=36.50]] |

The computed monthly withholding equals the published value.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Oracle example 1 input | [[FACT:ar.oracle.example.1.input=monthly 2,127.00, 2 exemptions (Formula Method 2026)]] | from 2026-01-01 |  | S4 |  |
| Oracle example 1 withholding | USD [[FACT:ar.oracle.example.1.withholding=36.50]] | from 2026-01-01 |  | S4 | Recomputed 25,524 - [[FACT:ar.wh.std_deduction=2,470]] = 23,054 -> midpoint 23,050 x [[FACT:ar.pit.bracket.4.rate=3.4]] % - [[FACT:ar.pit.bracket.4.subtract=287.97]] = 495.73 -> 496 - 58 = 438 / 12 = [[FACT:ar.oracle.example.1.withholding=36.50]]. |

## AR.15 Special populations

- Domestic workers: exempt from Arkansas withholding; UI above the quarterly cash-wage threshold.
- Agricultural workers: withholding required above the agricultural headcount threshold; no State overtime; UI above the agricultural thresholds.
- Tipped employees: cash wage USD [[FACT:ar.minwage.tipped.cash_wage=2.63]]; written tip-credit notice; reported tips are withheld.
- Clergy: ministers exempt from Arkansas withholding.
- Students: sub-minimum wage only with a Department of Labor certificate (11-4-210(b)); UI excludes students at their own school.
- Non-resident aliens: no Arkansas rule beyond the federal one. Commission agents excluded from UI.
- Government and non-profit: covered by withholding; UI reimbursable option.
- Military: active-duty pay exempt (Act 1408 of 2013); spouses file ARW-4MS yearly.
- Small employers below [[FACT:ar.minwage.employer_size_min=4]] employees: outside the State minimum-wage act.
- Minors: Not configured in this release [[GAP:RQ-467]]: Child-labour hour limits not in the sources read (AR.6).

Not configured in this release [[GAP:RQ-512]]: The coverage thresholds that apply to these populations (quarterly cash-wage and headcount thresholds for UI coverage of domestic, agricultural and non-profit employment) are cited by statute only and are not established as values; the engine must not hard-code them until they are established.

## AR.16 Language

No language rule for pay records. Payslip and filings in English.

## AR.S Sources

| Ref | Instrument | Article / section | Authority |
|---|---|---|---|
| S1 | Arkansas DOLL Minimum Wage and Overtime page | Minimum wage; Tipped employees; Deductions from Minimum Wage; Overtime; Compensatory time | Arkansas Department of Labor and Licensing (Labor Standards) |
| S2 | Arkansas Act 853 of 2019 (HB1751) amending the Minimum Wage Act and Ark. Code 11-4-403, 11-4-405 | Sec. 2 (11-4-213), Sec. 5 (11-4-218(g)), Sec. 6 (11-4-403(f)), Sec. 7 (11-4-405) | Arkansas General Assembly |
| S3 | Arkansas Dept of Labor - Statutes Regulating Wages and Hours (revised Oct 2008) | 11-4-217 records; Payment of Wages | Arkansas Department of Labor and Licensing |
| S4 | Arkansas Withholding Tax Formula Method (Tax Year 2026) | Formula steps 1-6; bracket table; Example (Gary) | Arkansas DFA Revenue Division |
| S5 | Arkansas Act 1 of the First Extraordinary Session 2026 (HB 1001), approved 2026-05-06 | Sections 1-3 (A.C.A. 26-51-201(a)(4), (a)(5); 26-51-205(a)(6), (b)(6)) | Arkansas General Assembly |
| S6 | Arkansas Withholding Tax Low Income Tax Tables (effective 01/01/2026) | 23 pages; weekly/bi-weekly/... by filing status and 0-6 dependents | Arkansas DFA Revenue Division |
| S7 | Arkansas Form AR4EC Employee's Withholding Exemption Certificate (R 12/04/2025) | Lines 1a-1c (1 or 2 exemptions); line 2 dependents; line 3 total; line 4 additional amount; line 5 low-income rates; instructions | Arkansas DFA Withholding Tax Section |
| S8 | Arkansas Form AR4ECSP Employee's Special Withholding Exemption Certificate (R 12/04/2025) | Check boxes (5 categories) | Arkansas DFA Withholding Tax Section |
| S9 | Arkansas DFA Withholding Tax Employer's Instructions (Effective 01/01/2026, Revised 4/27/26) | Introduction; Supplemental Wages; Nonresident Employees; Texarkana Residents | Arkansas Department of Finance and Administration |
| S10 | Arkansas Act 1019 of 2021 (SB 484): allocation of nonresident income by physical location | Sec. 2 (26-51-202(c)), Sec. 3 (26-51-504(a)(1)), Sec. 4 (26-51-902(5)), Sec. 5-6 | Arkansas General Assembly |
| S11 | Arkansas DFA Taxes page (absence basis, revenue side) | Tax Division menu | Arkansas Department of Finance and Administration |
| S12 | Arkansas DWS Employer Handbook: additional UI taxes (Advance Interest, Extended Benefit, Administrative Assessment) | Unemployment Tax Calculation pp.14-17; A.C.A. 11-10-706, 11-10-708, 11-10-540 | Arkansas Division of Workforce Services / Division of Reemployment |
| S13 | Arkansas Division of Reemployment employer UI page: 2026 Tax Rates | 2026 Tax Rates box | Arkansas Division of Reemployment |
| S14 | Arkansas 11 CAR Part 11 Minimum Wage (compilation dated 07/21/2026) - record-keeping section | 11 CAR 11-101 and following (records) | Arkansas Department of Labor and Licensing |
| S15 | Arkansas DFA OCSE - OCSE Partners (Employers) page | Employers; Employer New Hire Reporting; Verification of Employment | Arkansas DFA Office of Child Support Enforcement |
| S16 | Arkansas DFA OCSE - Paying Child Support FAQ | Q: amount billed for income withholding does not match the court order; Q: paying through the Clerk of Court | Arkansas DFA Office of Child Support Enforcement |
| S17 | US DOL WHD - State Prevailing Wage Laws (page dated 2023-01-01) | List of states without prevailing wage laws (24 states) | US Department of Labor, Wage and Hour Division |
| S18 | Arkansas Dept of Labor - Statutes Regulating Wages and Hours (11-4-201 to 11-4-405 etc.) | Ark. Code 11-4-216 (posting), 11-4-217 (records), 11-4-401 to 11-4-405 (payment) | Arkansas Department of Labor |
| S19 | Arkansas Senate news: Special Session to Lower State Income Tax (95th GA, First Extraordinary Session 2026; SB 1 / HB 1001) | Proclamation of 2026-04-30; SB 1 and identical HB 1001 | Arkansas Senate |

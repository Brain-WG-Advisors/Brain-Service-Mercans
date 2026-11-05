# Annex AL: Alabama


This annex sets out the Alabama payroll rules for the 2026 build year. Read with the federal reference (the federal layer every employee carries) and the multistate reference (which routes an employee to this State by work location, residence or UI localization). Every value is shown with its effective dates and its source (list at the end of the annex). Federal values are not repeated here.

Classification: T4. Besides State withholding, municipal and county occupational taxes are withheld by the employer and remitted to the locality on its own return.

## AL.1 Employment and labour code

Alabama has no State minimum-wage, overtime, pay-frequency, payment-method or paycard statute; the federal floor applies (the federal reference). Local wage and leave mandates are pre-empted.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Minimum wage state exists | False | from 2016-02-25 |  | S1 |  |
| Local wage leave mandates preempted | True | from 2016-02-25 |  | S1 |  |
| Equal pay wage history refusal protected | True | from 2026-01-01 |  | S2 | Clarke-Figures Equal Pay Act, 25-1-30 (sex and race). |

## AL.2 Income tax withholding

**Method.** annualise; subtract standard deduction (phase-out by GI), annualised federal FIT withheld, personal exemption, dependents; apply 2/4/5% brackets; divide by pay periods. The federal income tax withheld is deductible, so the federal computation runs first. Certificate: A4 REV. 4/2025 (federal W-4 not accepted; no A4 = zero exemptions; A4-MS military spouse).

```
annual_wages  = period_wages x pay_periods
taxable       = annual_wages - std_deduction(status, annual_wages) - annual_FIT_withheld
                - personal_exemption(status) - dependents x dependent_amount(annual_wages)
annual_tax    = brackets(status)(taxable)       # rates and ceilings below
period_tax    = annual_tax / pay_periods
```

Standard deduction by status: single maximum USD 3,000, minimum USD 2,500; married maximum USD 8,500, minimum USD 5,000; married filing separately maximum USD 4,250; head of family maximum USD 5,200. Personal exemption: single USD 1,500, married USD 3,000. Dependent amount by gross income band: USD 1,000, USD 500, USD 300.

**Standard-deduction phase-out** (booklet rev. 01/2026 p.6 formula and p.7 schedule): Standard deduction by Alabama-certificate status: 0/S 3,000 up to GI 25,999, less 25 per 500 (or part) above 25,999, 2,500 from 35,500; MS 4,250 up to 12,999, less 88 per 250 above, 2,500 from 17,750; M 8,500 up to 25,999, less 175 per 500 above, 5,000 from 35,500; H 5,200 up to 25,999, less 135 per 500 above, 2,500 from 35,500.

```
if GI <= start_gi:        std = max_deduction
elif GI >= floor_from_gi: std = min_deduction
else:                     std = max_deduction - reduction_per_step x ceil((GI - start_gi) / step_size)
```

| Status | Maximum | Phase-out starts above GI | Reduction per step | Step size | Minimum deduction | Minimum applies from GI |
|---|---|---|---|---|---|---|
| Single (0/S) | USD 3,000 | USD 25,999 | USD 25 | USD 500 | USD 2,500 | USD 35,500 |
| Married filing separately (MS) | USD 4,250 | USD 12,999 | USD 88 | USD 250 | USD 2,500 | USD 17,750 |
| Married (M) | USD 8,500 | USD 25,999 | USD 175 | USD 500 | USD 5,000 | USD 35,500 |
| Head of family (H) | USD 5,200 | USD 25,999 | USD 135 | USD 500 | USD 2,500 | USD 35,500 |

**Supplemental pay:** may be withheld at 5 %. **Overtime:** the 2026 overtime-premium deduction (up to USD 1,000) operates at **assessment** level only; it changes neither wages nor withholding (W-2 box 12 code TT is informational). Do not build it as a payroll deduction.

**PIT bracket single: bracket table**

| Bracket | ceiling | Effective | Source |
|---|---|---|---|
| 1 | USD 500 | from 2026-01-01 | S3 |
| 2 | USD 3,000 | from 2026-01-01 | S3 |

**PIT bracket married: bracket table**

| Bracket | ceiling | Effective | Source |
|---|---|---|---|
| 1 | USD 1,000 | from 2026-01-01 | S3 |
| 2 | USD 6,000 | from 2026-01-01 | S3 |

**PIT bracket: bracket table**

| Bracket | rate | Effective | Source |
|---|---|---|---|
| 1 | 2 % | from 2026-01-01 | S3 |
| 2 | 4 % | from 2026-01-01 | S3 |
| 3 | 5 % | from 2026-01-01 | S3 |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Withholding method | annualise; subtract standard deduction (phase-out by GI), annualised federal FIT withheld, personal exemption, dependents; apply 2/4/5% brackets; divide by pay periods | from 2026-01-01 |  | S3 | Booklet rev. 01/2026 p. 6; Ala. Code 40-18-71/-74. Order FIT before AL SIT. |
| Withholding federal FIT deductible | True | from 2026-01-01 |  | S4 | 40-18-71(a). |
| Withholding standard deduction single max | USD 3,000 | from 2026-01-01 |  | S3 | Phase-out by gross income: see the standard-deduction table in AL.2. |
| Withholding standard deduction single min | USD 2,500 | from 2026-01-01 |  | S3 |  |
| Withholding standard deduction married max | USD 8,500 | from 2026-01-01 |  | S3 | Phase-out by gross income: see the standard-deduction table in AL.2. |
| Withholding standard deduction married min | USD 5,000 | from 2026-01-01 |  | S3 |  |
| Withholding standard deduction married separate max | USD 4,250 | from 2026-01-01 |  | S3 | Phase-out by gross income: see the standard-deduction table in AL.2. |
| Withholding standard deduction married separate min | USD 2,500 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, Formula For Computing Alabama Withholding Tax, step 2A (printed page 7): Employee claims 'Married Filing Separately (MS)' exemption: 'GI of $17,750 or more deduct $2,500'. Minimum deduction per status: single 2,500 / married filing separately 2,500 / married filing jointly 5,000 / head of family 2,500. |
| Withholding standard deduction head of family max | USD 5,200 | from 2026-01-01 |  | S3 | Phase-out by gross income: see the standard-deduction table in AL.2. |
| Withholding standard deduction head of family min | USD 2,500 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, Formula For Computing Alabama Withholding Tax, step 2A (printed page 7): Employee claims 'Head of Family (H)' exemption: 'GI of $35,500 or more deduct $2,500'. Minimum deduction per status: single 2,500 / married filing separately 2,500 / married filing jointly 5,000 / head of family 2,500. |
| Withholding personal exemption single | USD 1,500 | from 2026-01-01 |  | S3 | Status 0: no exemption; single and married filing separately: this amount; married and head of family: 3,000. |
| Withholding personal exemption married | USD 3,000 | from 2026-01-01 |  | S3 |  |
| Withholding dependent gi to 50000 | USD 1,000 | from 2026-01-01 |  | S3 | Per dependent, by the employee's gross-income band (amounts in the next two rows). |
| Withholding dependent gi to 100000 | USD 500 | from 2026-01-01 |  | S3 |  |
| Withholding dependent gi above 100000 | USD 300 | from 2026-01-01 |  | S3 |  |
| Withholding supplemental rate | 5 % | from 2026-01-01 |  | S3 | May be withheld at 5 %. |
| Withholding certificate form | A4 REV. 4/2025 (federal W-4 not accepted; no A4 = zero exemptions; A4-MS military spouse) | from 2025-04-01 |  | S5 |  |
| Withholding certificate inflated penalty | USD 500 | from 2025-04-01 |  | S5 |  |
| Withholding severance exempt max | USD 50,000 | from 2026-01-01 |  | S3 | Severance/downsizing pay exempt up to 50,000 with prior ADOR approval. |
| PIT overtime premium deduction max | USD 1,000 | 2026-01-01 to 2028-12-31 |  | S6 | Act 2026-604, operating level ASSESSMENT only: no change to wages, withholding or tax; W-2 box 12 code TT informational; total OT stays in box 16. Prior withholding-level exemption (Acts 2023-421/2024-437) shown as previous by ADOR. |
| Withholding standard deduction single phaseout start gi | USD 25,999 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts |
| Withholding standard deduction single phaseout reduction per STEP | USD 25 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts |
| Withholding standard deduction single phaseout STEP size | USD 500 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts ("for each 500 increment or part thereof of GI above 25,999") |
| Withholding standard deduction single phaseout floor from gi | USD 35,500 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts; at GI of 35,500 or more the deduction is 2,500; last stepped value 2,525 |
| Withholding standard deduction married separate phaseout start gi | USD 12,999 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts |
| Withholding standard deduction married separate phaseout reduction per STEP | USD 88 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts |
| Withholding standard deduction married separate phaseout STEP size | USD 250 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts ("for each 250 increment or part thereof of GI above 12,999") |
| Withholding standard deduction married separate phaseout floor from gi | USD 17,750 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts; at GI of 17,750 or more the deduction is 2,500; last stepped value 2,578 |
| Withholding standard deduction married phaseout start gi | USD 25,999 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts |
| Withholding standard deduction married phaseout reduction per STEP | USD 175 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts |
| Withholding standard deduction married phaseout STEP size | USD 500 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts ("for each 500 increment or part thereof of GI above 25,999") |
| Withholding standard deduction married phaseout floor from gi | USD 35,500 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts; at GI of 35,500 or more the deduction is 5,000; last stepped value 5,175 |
| Withholding standard deduction head of family phaseout start gi | USD 25,999 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts |
| Withholding standard deduction head of family phaseout reduction per STEP | USD 135 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts |
| Withholding standard deduction head of family phaseout STEP size | USD 500 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts ("for each 500 increment or part thereof of GI above 25,999") |
| Withholding standard deduction head of family phaseout floor from gi | USD 35,500 | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts; at GI of 35,500 or more the deduction is 2,500; last stepped value 2,635 |
| Withholding standard deduction phaseout steps | Standard deduction by Alabama-certificate status: 0/S 3,000 up to GI 25,999, less 25 per 500 (or part) above 25,999, 2,500 from 35,500; MS 4,250 up to 12,999, less 88 per 250 above, 2,500 from 17,750; M 8,500 up to 25,999, less 175 per 500 above, 5,000 from 35,500; H 5,200 up to 25,999, less 135 per 500 above, 2,500 from 35,500. | from 2026-01-01 |  | S3 | ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A; p.7 Schedule of Standard Deduction Amounts |

## AL.2b Non-resident regime and reciprocity

No reciprocity agreement. Residents are withheld on all wages wherever earned except when the employer withholds for the work State; non-residents only on Alabama wages. The non-resident safe harbour (30 days, Act 2025-334) operates at withholding level.

**Resident / non-resident matrix (Alabama income tax)**

| Income type | Resident | Non-resident |
|---|---|---|
| Regular salary | Formula method (AL.2) on all wages, unless the employer withholds for the work State | Formula method on Alabama wages only, after the 30-day safe harbour where the home State qualifies |
| Annual bonus / supplemental pay | 5 % or the formula on the aggregate | Same, on the Alabama portion |
| Severance | Downsizing severance exempt up to USD 50,000 with prior ADOR approval; otherwise supplemental pay | Same, on the Alabama portion |
| Equity | Supplemental-pay treatment; federal classification of equity income in the federal reference (FED.2b) | Same, on the Alabama portion |
| Benefits in kind | Included in withholding wages; HSA treatment conforms; transit and group-term life open (AL.8) | Same, on the Alabama portion |
| Contractor pay | Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008] | Same |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Non-resident safe harbor days | 30 days | from 2026-01-01 |  | S7 | Act 2025-334, operating level WITHHOLDING: nonresidents with <=30 AL days working in more than one state whose home state has a similar exclusion or no PIT (list as of 2026-10-01: AK, FL, GA, IL, IN, LA, MT, NV, NH, SD, TN, TX, WA, WV, WY). At 31+ days all AL income of the year taxable. Athletes/entertainers/public figures excluded. |
| Reciprocity exists | False | from 2026-01-01 |  | S3 | Booklet lists no agreement. Residents withheld wherever they work except when the employer withholds for the work state; nonresidents only on AL-earned wages. |

Not configured in this release (open gap RQ-461): Non-resident safe harbor day counting guidance: not established from an official source.

## AL.2c Local wage taxes

Municipal and county occupational taxes are withheld by the employer and remitted to the city or county on its own return; the Department of Revenue does not administer them. The only rate in the research is Leeds (table). The State keeps no list of levying localities (blocking gap below): the engine needs a locality table before any Alabama employee can be paid.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Local occupational tax exists | True | from 2026-01-01 |  | S3 | Municipal/county occupational taxes withheld by the employer, remitted to the city/county; ADOR does not administer them. No state census. |
| Local leeds rate | 1 % | from 2026-01-01 |  | S8 | City of Leeds: 1 % of gross earnings, monthly return to Avenu, annual reconciliation, show on pay stub, records 5 years. A Birmingham occupational tax rate is not confirmed by an official source. |

Not yet published (open gap RQ-458): Local occupational tax census: not established from an official source.

## AL.3 Social insurance: unemployment, disability, paid leave and payroll levies

Employer-only UI (0 % employee) on wages up to the base, plus the Employment Security Assessment. No SDI, TDI or PFML.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| SUI wage base | USD 8,000 | from 2026-01-01 |  | S9 | 25-4-16(b)(1), fixed in statute; other-state UC wages count toward it. |
| SUI new employer rate | 2.7 % | from 2026-01-01 |  | S10 |  |
| SUI employer rate min | 0.2 % | from 2026-01-01 |  | S10 | Range 0.20%-6.80% incl. 0.06 % ESA across schedules A-D plus shared cost; 2026 schedule letter/shared cost not located. |
| SUI employer rate max | 6.8 % | from 2026-01-01 |  | S10 |  |
| SUI esa rate | 0.06 % | from 2026-01-01 |  | S10 | Employment Security Enhancement Assessment inside the UC rate; no FUTA credit for it. |
| SUI employee rate | 0 % | from 2026-01-01 |  | S11 | No UC tax withheld from employees. |
| SUI wages cafeteria cash option included | True | from 2026-01-01 |  | S10 | Cafeteria plan reductions with a cash option are UC wages (departs from income tax). |
| SDI PFML exists | False | from 2026-01-01 |  | S10 |  |

Not configured in this release (open gap RQ-457): SUI rate schedule current: not established from an official source.

## AL.4 Pay statement

Alabama has no pay-statement statute; local rules may require a pay-stub line (Leeds, AL.2c).

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Payslip state statute exists | False | from 2026-01-01 |  | S10 | Agency: no state wage-hour laws; 29 CFR 516 applies. Leeds asks occupational tax to be shown on the pay stub. |

## AL.5 Statutory reporting

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Report withholding monthly a6 threshold | USD 1,000 | from 2026-01-01 |  | S3 | A-6 monthly if more than 1,000 withheld in month 1 or 2 of the quarter; due 15th of next month; e-file/EFT mandatory for single payment >= 750. |
| Report withholding eft mandatory payment | USD 750 | from 2026-01-01 |  | S3 |  |
| Report withholding quarterly form | A-1 due last day of month after quarter; file when nil | from 2026-01-01 |  | S3 |  |
| Report annual a3 | A-3 + W-2s due 31 January; EFW2 RS record only, 512 bytes; e-file mandatory for 10+ statements (Form 10, 8/24); RS cols 298-307 carry federal FIT withheld | from 2026-01-01 |  | S12 |  |
| Report W-2 efile threshold | 10 statements | from 2026-01-01 |  | S12 |  |
| Report W-2 furnish threshold | USD 1,500 | from 2026-01-01 |  | S3 | W-2 to every employee paid 1,500+ AL wages or with AL tax withheld. |
| Report SUI quarterly | Quarterly Contribution and Wage Report via eGov only (online_form or file_upload); due last day of month after quarter; corrections UC-10C | from 2026-01-01 |  | S10 |  |
| Newhire report days | 7 days | from 2026-01-01 |  | S13 | From hire or recall; electronic twice a month 12-16 days apart; electronic mandatory for 5+ employees. |

## AL.6 Leave

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Leave sick state statute exists | False | from 2026-01-01 |  | S1 | Local sick-leave mandates barred (25-7-41). |
| Leave jury full time usual compensation | True | from 2026-01-01 |  | S14 | 12-16-8(c), 12-16-8.1: full-time employee entitled to usual compensation; cannot be forced to use leave. |
| Leave voting hours | 1 hours | from 2026-01-01 |  | S14 | 17-1-5; silent on pay. |

## AL.7 Termination and final pay

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| UI separation info return working days | 6 working days | from 2026-01-01 |  | S11 | BEN-241 on a claim. No state final-pay statute (federal + policy). |

## AL.8 Benefits in kind and taxable wages

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| HSA conforms | True | from 2026-01-01 |  | S15 |  |

Not configured in this release (open gap RQ-459): PIT wages transit group term life: not established from an official source.

## AL.9 Deductions and garnishments

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Garnishment exempt percent | 75 % | from 2026-01-01 |  | S16 | 6-10-7: 75 % of resident wages exempt; apply with CCPA disposable-earnings limit, more protective governs. Garnishee pays in after 30 days, then monthly. |
| Garnishment child support remit business days | 7 business days | from 2026-01-01 |  | S16 | 30-3-61/-67/-70: IWO priority over garnishments; current before arrears. |
| Garnishment termination report days | 15 days | from 2026-01-01 |  | S16 |  |

Not configured in this release (open gap RQ-460): Garnishment IWO employer fee: not established from an official source.

## AL.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

No State prevailing-wage law; federal Davis-Bacon only (the federal reference). Ala. Code 25-7-42 bars local labour-peace and project-labour-agreement mandates.

## AL.11 Indexation

Nothing is indexed: the UI base is fixed in statute, withholding amounts are statutory and there is no State minimum wage. Only the yearly UC rate schedule and shared-cost rate change (25-4-54), notified per employer on UC-216.

## AL.12 Payroll data protection and records

Data Breach Notification Act of 2018 (ch. 8-38). No statute requiring SSN truncation on pay statements was found in the research.

## AL.13 Live legal change

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Live act 2025 334 status | in force 2026-01-01; operating level withholding + filing | from 2026-01-01 |  | S7 |  |
| Live act 2026 604 status | in force 2026-01-01 to 2028-12-31; operating level assessment (W-2 box 12 TT information) | 2026-01-01 to 2028-12-31 |  | S6 |  |
| Live hurricane isaias relief | individual returns to 2027-02-04; withholding relief case by case (notice 2026-10-15) | from 2026-10-15 |  | S17 |  |

Not configured in this release (open gap RQ-462): Live overtime withholding exemption end date: not established from an official source.

## AL.14 Authority worked examples (oracle values)

Authority example (ADOR withholding booklet, rev. 01/2026), recomputed line by line from the keyed parameters. Rounding: half-up to the cent at each line.

Input: M-2, weekly 850.00, federal withholding 35.19. Married status, two dependents, gross income in the lowest dependent band and above the standard-deduction phase-out range (so the minimum deduction applies).

| Line | Base | Rate | Amount |
|---|---|---|---|
| Annual wages | 850.00 x 52 | — | 44,200.00 |
| Standard deduction (married, minimum) | — | — | USD 5,000 |
| Annual federal income tax withheld | 35.19 x 52 | — | 1,829.88 |
| Personal exemption (married) | — | — | USD 3,000 |
| Dependents | 2 x USD 1,000 | — | 2,000.00 |
| Taxable income | 44,200.00 - 5,000.00 - 1,829.88 - 3,000.00 - 2,000.00 | — | 32,370.12 |
| Band 1 | USD 1,000 | 2 % | 20.00 |
| Band 2 | 6,000.00 - 1,000.00 = 5,000.00 | 4 % | 200.00 |
| Band 3 | 32,370.12 - 6,000.00 = 26,370.12 | 5 % | 1,318.51 |
| Annual tax | 20.00 + 200.00 + 1,318.51 | — | 1,538.51 |
| Weekly withholding | 1,538.51 / 52 | — | USD 29.59 |

The computed weekly withholding equals the published value. If the employer rounds the period tax to the whole dollar, the weekly amount is the rounded figure.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Oracle example 1 input | M-2, weekly 850.00, federal withholding 35.19 | from 2026-01-01 |  | S3 |  |
| Oracle example 1 withholding | USD 29.59 | from 2026-01-01 |  | S3 | Booklet example Recomputed: 850 x 52 = 44,200; deductions 5,000 + 1,830 + 3,000 + 2,000 = 11,830 (the booklet rounds 35.19 x 52 = 1,829.88 to 1,830); taxable 44,200 - 11,830 = 32,370; tax 20 + 200 + 1,318.50 = 1,538.50 a year (26,370 x 5% = 1,318.50); /52 = 29.59 (30 if rounded to dollar). |

## AL.15 Special populations

- Domestic and household workers: exempt from Alabama withholding; UC-covered above the quarterly cash-wage threshold.
- Agricultural workers: exempt from withholding (Alabama does not follow the federal rule); UC above the agricultural thresholds.
- Minors: child-labour limits; no youth wage.
- Tipped employees: federal tip credit; tips are UC wages.
- Clergy: ministers exempt from Alabama withholding; church employment not UC-covered.
- Students, non-resident aliens, statutory employees: no Alabama rule beyond the federal one.
- Other-State workers: non-resident safe harbour (AL.2b); federal carrier carve-outs (the multistate reference).
- Government and non-profit: 501(c)(3) employers UC-covered above the size threshold; the pre-emption rule does not cover public employees.
- Military spouses: certificate A4-MS.
- Downsizing severance: exempt up to USD 50,000 with ADOR approval.

Not configured in this release (open gap RQ-511): The coverage thresholds that apply to these populations (quarterly cash-wage and headcount thresholds for UI coverage of domestic, agricultural and non-profit employment) are cited by statute only and are not established as values; the engine must not hard-code them until they are established.

## AL.16 Language

English. A Spanish version of the A4 exists (optional seam). Payslip and filings in English.

## AL.S Sources

| Ref | Instrument | Article / section | Authority |
|---|---|---|---|
| S1 | Code of Alabama Sec. 25-7-41 (Act 2016-18): local governments barred from wage, leave, benefit or schedule mandates | 25-7-41(b),(c); 25-7-43 exceptions | Alabama Legislature (ALISON Code of Alabama) |
| S2 | Code of Alabama Sec. 25-1-30 Clarke-Figures Equal Pay Act (Act 2019-519) | 25-1-30(b),(c) | Alabama Legislature (ALISON Code of Alabama) |
| S3 | Alabama Withholding Tax Tables and Instructions for Employers and Withholding Agents, revised January 2026 (whbooklet_0126) - formula, standard deduction … | pp.1-7 (formula p.6, standard deduction schedule p.7) | Alabama Department of Revenue, Withholding Tax Section |
| S4 | Code of Alabama Sec. 40-18-71 (withholding tax) and 40-18-74 (payment of amounts withheld) | 40-18-71(a)-(e); 40-18-74(a) | Alabama Legislature (ALISON Code of Alabama) |
| S5 | Form A4 Employee Withholding Tax Exemption Certificate (REV. 4/2025) | Parts I-II | Alabama Department of Revenue |
| S6 | ADOR Overtime Premium Deduction (Act 2026-604) page | whole page | Alabama Department of Revenue |
| S7 | ADOR 30-Day Safe Harbor Rule page (Act 2025-334) | whole page | Alabama Department of Revenue |
| S8 | City of Leeds Employer's Withholding Guide for Occupational Tax | sections 1-9 (3 pp.) | City of Leeds, Alabama (revenue examiner; remittance via Avenu) |
| S9 | Code of Alabama 1975 Sec. 25-4-16 (wages, 8,000 USD taxable base, other-state employment counted) and Sec. 25-4-54 (experience-rated contributions, shared cost) | 25-4-16(b)(1); 25-4-54(a),(f) | Alabama Legislature (ALISON Code of Alabama) |
| S10 | Workforce Alabama Employer FAQ (UC liability, new account rate, rate range, quarterly report, wage base, other-state wages, cafeteria plans) | FAQ (Employer Registration & Taxes; Tax Rates; Quarterly Reports & Wages) | Alabama Department of Workforce, Unemployment Compensation |
| S11 | Alabama UC Employer Handbook (2020 edition per its cover; the official file name says 'rev_2021') | ch. 2 Taxes, Contribution and Wage Reports (handbook p. 18); handbook p. 67 No UC taxes paid by employee | Alabama Dept of Labor (now Dept of Workforce) |
| S12 | ADOR Form 10 Specifications for filing Wage and Tax Information electronically (8/24) | W-2 Electronic Filing Specifications | Alabama Department of Revenue |
| S13 | Workforce Alabama New Hires page | whole page incl. FAQ | Alabama Department of Workforce, New-Hire Unit |
| S14 | Code of Alabama Sec. 12-16-8 and 12-16-8.1 (jury duty) and 17-1-5 (time off to vote) | 12-16-8(a)-(c); 12-16-8.1; 17-1-5 | Alabama Legislature (ALISON Code of Alabama) |
| S15 | Code of Alabama Sec. 40-18-15.6 (health savings account contributions) | 40-18-15.6(a),(b) | Alabama Legislature (ALISON Code of Alabama) |
| S16 | Code of Alabama Sec. 6-10-7 (wage garnishment exemption) and 30-3-61, 30-3-67, 30-3-70 (child-support income withholding) | 6-10-7(a),(b); 30-3-61; 30-3-67; 30-3-70 | Alabama Legislature (ALISON Code of Alabama) |
| S17 | ADOR news: Additional Relief for Taxpayers Affected by Hurricane Isaias (2026-10-15) | whole notice | Alabama Department of Revenue |


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `al.equal_pay.wage_history_refusal_protected` | True | from 2026-01-01 | US-ALS5-015 |
| `al.garn.child_support.remit_business_days` | 7 | from 2026-01-01 | US-ALS5-013 |
| `al.garn.exempt.percent` | 75 | from 2026-01-01 | US-ALS5-013 |
| `al.garn.termination_report_days` | 15 | from 2026-01-01 | US-ALS5-013 |
| `al.hsa.conforms` | True | from 2026-01-01 | US-ALS5-020 |
| `al.leave.jury.full_time_usual_compensation` | True | from 2026-01-01 | US-ALS5-012 |
| `al.leave.sick.state_statute.exists` | False | from 2026-01-01 | US-ALS5-010 |
| `al.leave.voting.hours` | 1 | from 2026-01-01 | US-ALS5-012 |
| `al.live.act_2025_334.status` | in force 2026-01-01; operating level withholding + filing | from 2026-01-01 | US-ALS5-003 |
| `al.live.act_2026_604.status` | in force 2026-01-01 to 2028-12-31; operating level assessment (W-2 box 12 TT information) | from 2026-01-01 to 2028-12-31 | US-ALS5-004 |
| `al.live.hurricane_isaias_relief` | individual returns to 2027-02-04; withholding relief case by case (notice 2026-10-15) | from 2026-10-15 | US-ALS5-019 |
| `al.local.leeds.rate` | 1 | from 2026-01-01 | US-ALS5-017 |
| `al.local.occupational_tax.exists` | True | from 2026-01-01 | US-ALS5-001 |
| `al.local_wage_leave_mandates.preempted` | True | from 2016-02-25 | US-ALS5-010 |
| `al.minwage.state.exists` | False | from 2016-02-25 | US-ALS5-010 |
| `al.newhire.report_days` | 7 | from 2026-01-01 | US-ALS5-008 |
| `al.nonres.safe_harbor.days` | 30 | from 2026-01-01 | US-ALS5-003 |
| `al.oracle.example.1.input` | M-2, weekly 850.00, federal withholding 35.19 | from 2026-01-01 | US-ALS5-001 |
| `al.oracle.example.1.withholding` | 29.59 | from 2026-01-01 | US-ALS5-001 |
| `al.payslip.state_statute.exists` | False | from 2026-01-01 | US-ALS5-007 |
| `al.pit.bracket.1.rate` | 2 | from 2026-01-01 | US-ALS5-001 |
| `al.pit.bracket.2.rate` | 4 | from 2026-01-01 | US-ALS5-001 |
| `al.pit.bracket.3.rate` | 5 | from 2026-01-01 | US-ALS5-001 |
| `al.pit.bracket.married.1.ceiling` | 1,000 | from 2026-01-01 | US-ALS5-001 |
| `al.pit.bracket.married.2.ceiling` | 6,000 | from 2026-01-01 | US-ALS5-001 |
| `al.pit.bracket.single.1.ceiling` | 500 | from 2026-01-01 | US-ALS5-001 |
| `al.pit.bracket.single.2.ceiling` | 3,000 | from 2026-01-01 | US-ALS5-001 |
| `al.pit.overtime_premium_deduction.max` | 1,000 | from 2026-01-01 to 2028-12-31 | US-ALS5-004 |
| `al.reciprocity.exists` | False | from 2026-01-01 | US-ALS5-001 |
| `al.report.annual.a3` | A-3 + W-2s due 31 January; EFW2 RS record only, 512 bytes; e-file mandatory for 10+ statements (Form 10, 8/24); RS cols 298-307 carry federal FIT withheld | from 2026-01-01 | US-ALS5-006 |
| `al.report.sui.quarterly` | Quarterly Contribution and Wage Report via eGov only (online_form or file_upload); due last day of month after quarter; corrections UC-10C | from 2026-01-01 | US-ALS5-007 |
| `al.report.w2.efile_threshold` | 10 | from 2026-01-01 | US-ALS5-006 |
| `al.report.w2.furnish_threshold` | 1,500 | from 2026-01-01 | US-ALS5-001 |
| `al.report.wh.eft_mandatory_payment` | 750 | from 2026-01-01 | US-ALS5-001 |
| `al.report.wh.monthly.a6.threshold` | 1,000 | from 2026-01-01 | US-ALS5-001 |
| `al.report.wh.quarterly.form` | A-1 due last day of month after quarter; file when nil | from 2026-01-01 | US-ALS5-001 |
| `al.sdi_pfml.exists` | False | from 2026-01-01 | US-ALS5-007 |
| `al.sui.employee.rate` | 0 | from 2026-01-01 | US-ALR3-001 |
| `al.sui.employer.rate.max` | 6.8 | from 2026-01-01 | US-ALS5-007 |
| `al.sui.employer.rate.max` | 6.80 | from 2026-01-01 | US-ALS5-007 |
| `al.sui.employer.rate.min` | 0.2 | from 2026-01-01 | US-ALS5-007 |
| `al.sui.employer.rate.min` | 0.20 | from 2026-01-01 | US-ALS5-007 |
| `al.sui.esa.rate` | 0.06 | from 2026-01-01 | US-ALS5-007 |
| `al.sui.new_employer.rate` | 2.7 | from 2026-01-01 | US-ALS5-007 |
| `al.sui.wage_base` | 8,000 | from 2026-01-01 | US-ALS5-009 |
| `al.sui.wages.cafeteria_cash_option_included` | True | from 2026-01-01 | US-ALS5-007 |
| `al.ui.separation_info.return_working_days` | 6 | from 2026-01-01 | US-ALR3-001 |
| `al.wh.certificate.form` | A4 REV. 4/2025 (federal W-4 not accepted; no A4 = zero exemptions; A4-MS military spouse) | from 2025-04-01 | US-ALS5-005 |
| `al.wh.certificate.inflated_penalty` | 500 | from 2025-04-01 | US-ALS5-005 |
| `al.wh.dependent.gi_above_100000` | 300 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.dependent.gi_to_100000` | 500 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.dependent.gi_to_50000` | 1,000 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.federal_fit_deductible` | True | from 2026-01-01 | US-ALS5-011 |
| `al.wh.method` | annualise; subtract standard deduction (phase-out by GI), annualised federal FIT withheld, personal exemption, dependents; apply 2/4/5% brackets; divide by pay periods | from 2026-01-01 | US-ALS5-001 |
| `al.wh.personal_exemption.married` | 3,000 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.personal_exemption.single` | 1,500 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.severance.exempt_max` | 50,000 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.head_of_family.max` | 5,200 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.head_of_family.min` | 2,500 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.head_of_family.phaseout.floor_from_gi` | 35,500 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.head_of_family.phaseout.reduction_per_step` | 135 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.head_of_family.phaseout.start_gi` | 25,999 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.head_of_family.phaseout.step_size` | 500 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.married.max` | 8,500 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.married.min` | 5,000 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.married.phaseout.floor_from_gi` | 35,500 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.married.phaseout.reduction_per_step` | 175 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.married.phaseout.start_gi` | 25,999 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.married.phaseout.step_size` | 500 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.married_separate.max` | 4,250 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.married_separate.min` | 2,500 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.married_separate.phaseout.floor_from_gi` | 17,750 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.married_separate.phaseout.reduction_per_step` | 88 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.married_separate.phaseout.start_gi` | 12,999 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.married_separate.phaseout.step_size` | 250 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.phaseout_steps` | Standard deduction by Alabama-certificate status: 0/S 3,000 up to GI 25,999, less 25 per 500 (or part) above 25,999, 2,500 from 35,500; MS 4,250 up to 12,999, less 88 per 250 above, 2,500 from 17,750; M 8,500 up to 25,999, less 175 per 500 above, 5,000 from 35,500; H 5,200 up to 25,999, less 135 per 500 above, 2,500 from 35,500. | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.single.max` | 3,000 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.single.min` | 2,500 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.single.phaseout.floor_from_gi` | 35,500 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.single.phaseout.reduction_per_step` | 25 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.single.phaseout.start_gi` | 25,999 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.std_deduction.single.phaseout.step_size` | 500 | from 2026-01-01 | US-ALS5-001 |
| `al.wh.supplemental.rate` | 5 | from 2026-01-01 | US-ALS5-001 |

# Annex CA: California

This annex sets out the California payroll rules for the 2026 build year. Read with Annex FED (the federal layer every employee carries) and Annex MULTI (which routes an employee to this State by work location, residence or UI localization). Every value is shown with its effective dates and its source (list at the end of the annex). Federal values are not repeated here.

Classification: T3. Separate State withholding (PIT) and payroll taxes (UI, ETT, SDI) on one EDD return set; no local wage tax; local minimum wages exist.

## CA.1 Employment and labour code

State minimum wage USD [[FACT:ca.minwage.hourly=16.90]] for 2026 and USD [[FACT:ca.minwage.hourly=17.40]] for 2027. Overtime: [[FACT:ca.overtime.rule=1.5x over 8 h/day, over 40 h/week and first 8 h of 7th consecutive day; 2x over 12 h/day and over 8 h on 7th day (Lab. Code 510); alternative workweek exceptions]]. No tip credit ([[FACT:ca.deductions.tip_credit.allowed=False]]). Cities and counties may set higher minimum wages and some industries have their own minimums: both are blocking gaps below, so a California work location cannot be paid at the State rate without first checking the locality and the industry.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Minimum wage hourly | USD [[FACT:ca.minwage.hourly=16.90]] | 2026-01-01 to 2026-12-31 |  | S1 | All employers; learners 85% for first 160 hours. |
| Minimum wage hourly | USD [[FACT:ca.minwage.hourly=17.40]] | from 2027-01-01 |  | S2 | DOF certified 2026-07-31 (+2.99%); DIR News 2026-66 + Governor release. Check [[FACT:ca.minwage.hourly=16.90]] x 1.0299 = 17.405 -> [[FACT:ca.minwage.hourly=17.40]]. |
| Minimum wage learner percent | [[FACT:ca.minwage.learner.percent=85]] % | from 2026-01-01 |  | S1 | First 160 hours of employment. |
| Exempt salary annual min | USD [[FACT:ca.exempt.salary.annual_min=70,304]] | 2026-01-01 to 2026-12-31 |  | S1 | 2 x [[FACT:ca.minwage.hourly=16.90]] x 2,080. |
| Exempt salary annual min | USD [[FACT:ca.exempt.salary.annual_min=72,384]] | from 2027-01-01 |  | S2 | Quoted by DIR (= 2 x [[FACT:ca.minwage.hourly=17.40]] x 2,080). |
| Overtime rule | [[FACT:ca.overtime.rule=1.5x over 8 h/day, over 40 h/week and first 8 h of 7th consecutive day; 2x over 12 h/day and over 8 h on 7th day (Lab. Code 510); alternative workweek exceptions]] | from 2026-01-01 |  | S3 |  |
| Overtime daily threshold hours | [[FACT:ca.overtime.daily_threshold_hours=8]] hours | from 2026-01-01 |  | S3 |  |
| Overtime double time daily threshold hours | [[FACT:ca.overtime.double_time_daily_threshold_hours=12]] hours | from 2026-01-01 |  | S3 |  |
| Pay frequency rule | [[FACT:ca.pay_frequency.rule=twice a month: 1st-15th paid 16th-26th; 16th-end paid 1st-10th next month; EAP monthly by 26th; weekly/biweekly/semimonthly within 7 days of period close; OT by next regular payday (Lab. Code 204)]] | from 2026-01-01 |  | S4 |  |
| Direct deposit requires voluntary authorisation | [[FACT:ca.direct_deposit.requires_voluntary_authorisation=True]] | from 2026-01-01 |  | S4 | Lab. Code 213(d). |

⚠️ RESEARCH-GAP (blocking): Local minimum wage hourly: not established by the research. Source that would close it: each city labour-standards office bulletin for the 2026-07-01 and 2027-01-01 rates

⚠️ RESEARCH-GAP (blocking): Industry minimum wage fast food health care: not established by the research. Source that would close it: DIR fast-food and health-care minimum wage FAQ pages.

⚠️ RESEARCH-GAP (non-blocking): Payslip electronic consent: not established by the research. Source that would close it: DLSE opinion letter or DIR paydays FAQ on electronic wage statements.

⚠️ RESEARCH-GAP (non-blocking): Overtime agricultural phase in: not established by the research. Source that would close it: Lab. Code 860-864 text and DIR agricultural overtime FAQ.

## CA.2 Income tax withholding

**Method.** [[FACT:ca.wh.method=Method A (wage-bracket tables, wages < 1M) or Method B (exact calculation), DE 44 Rev. 52 (4-26)]]. Certificate: [[FACT:ca.wh.certificate.form=DE 4 Rev. 56 (1-26); federal W-4 for FIT only since 2020; no valid DE 4 = Single 0 allowances; exempt status renewed by Feb 15]]. Method B, per pay period:

```
annual_wages = period_wages x pay_periods
if annual_wages <= low_income_exemption(status, allowances): tax = 0
taxable      = annual_wages - estimated_deduction x additional_allowances - std_deduction(status, allowances)
annual_tax   = brackets(status)(taxable) - allowance_credit x allowances
period_tax   = max(0, annual_tax) / pay_periods
```

Married and head-of-household ceilings are carried as one value each: married [[FACT:ca.pit.brackets.married.ceilings=22,158 / 52,528 / 82,904 / 115,084 / 145,448 / 742,958 / 891,542 / 1,000,000 / 1,485,906; 14.63% over; base 164,228.58]]; head of household [[FACT:ca.pit.brackets.hoh.ceilings=22,173 / 52,530 / 67,716 / 83,805 / 98,990 / 505,208 / 606,251 / 1,000,000 / 1,010,417; base 107,334.77]]. The rate attached to each married band around the million-dollar point is read from the DE 44 Method B married table.

⚠️ RESEARCH-GAP (non-blocking): the married and head-of-household schedules carry their band ceilings as one value each and no per-band rate keys; an engine needs per-band rate keys for both schedules (research request raised).

**Supplemental pay** paid separately: bonuses and stock options [[FACT:ca.wh.supplemental.rate.bonus_stock_options=10.23]] %; other supplemental pay (overtime, commissions, severance, vacation pay) [[FACT:ca.wh.supplemental.rate.other=6.6]] %. Household employees: withholding only by agreement ([[FACT:ca.wh.household.by_agreement_only=True]]).

California does not conform to the federal P.L. 119-21 deductions ([[FACT:ca.obbba.conforms=False]]) and taxes employer HSA contributions ([[FACT:ca.hsa.conforms=False]]); see CA.8.

**PIT bracket single: bracket table**

| Bracket | rate | ceiling | Effective | Source |
|---|---|---|---|---|
| 1 | [[FACT:ca.pit.bracket.single.1.rate=1.1]] % | USD [[FACT:ca.pit.bracket.single.1.ceiling=11,079]] | 2026-01-01 to 2026-12-31 | S5 |
| 2 | [[FACT:ca.pit.bracket.single.2.rate=2.2]] % | USD [[FACT:ca.pit.bracket.single.2.ceiling=26,264]] | 2026-01-01 to 2026-12-31 | S5 |
| 3 | [[FACT:ca.pit.bracket.single.3.rate=4.4]] % | USD [[FACT:ca.pit.bracket.single.3.ceiling=41,452]] | 2026-01-01 to 2026-12-31 | S5 |
| 4 | [[FACT:ca.pit.bracket.single.4.rate=6.6]] % | USD [[FACT:ca.pit.bracket.single.4.ceiling=57,542]] | 2026-01-01 to 2026-12-31 | S5 |
| 5 | [[FACT:ca.pit.bracket.single.5.rate=8.8]] % | USD [[FACT:ca.pit.bracket.single.5.ceiling=72,724]] | 2026-01-01 to 2026-12-31 | S5 |
| 6 | [[FACT:ca.pit.bracket.single.6.rate=10.23]] % | USD [[FACT:ca.pit.bracket.single.6.ceiling=371,479]] | 2026-01-01 to 2026-12-31 | S5 |
| 7 | [[FACT:ca.pit.bracket.single.7.rate=11.33]] % | USD [[FACT:ca.pit.bracket.single.7.ceiling=445,771]] | 2026-01-01 to 2026-12-31 | S5 |
| 8 | [[FACT:ca.pit.bracket.single.8.rate=12.43]] % | USD [[FACT:ca.pit.bracket.single.8.ceiling=742,953]] | 2026-01-01 to 2026-12-31 | S5 |
| 9 | [[FACT:ca.pit.bracket.single.9.rate=13.53]] % | USD [[FACT:ca.pit.bracket.single.9.ceiling=1,000,000]] | 2026-01-01 to 2026-12-31 | S5 |
| 10 | [[FACT:ca.pit.bracket.single.10.rate=14.63]] % | — | 2026-01-01 to 2026-12-31 | S5 |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Withholding certificate form | [[FACT:ca.wh.certificate.form=DE 4 Rev. 56 (1-26); federal W-4 for FIT only since 2020; no valid DE 4 = Single 0 allowances; exempt status renewed by Feb 15]] | from 2026-01-01 |  | S6 |  |
| Withholding method | [[FACT:ca.wh.method=Method A (wage-bracket tables, wages < 1M) or Method B (exact calculation), DE 44 Rev. 52 (4-26)]] | from 2026-01-01 |  | S5 |  |
| Withholding low income exemption single | USD [[FACT:ca.wh.low_income_exemption.single=18,896]] | 2026-01-01 to 2026-12-31 |  | S5 | Single / Married 0-1 allowances; Married 2+ / HoH [[FACT:ca.wh.low_income_exemption.married_2plus_hoh=37,791]]. |
| Withholding low income exemption married 2plus HoH | USD [[FACT:ca.wh.low_income_exemption.married_2plus_hoh=37,791]] | 2026-01-01 to 2026-12-31 |  | S5 |  |
| Withholding standard deduction single | USD [[FACT:ca.wh.std_deduction.single=5,706]] | 2026-01-01 to 2026-12-31 |  | S5 |  |
| Withholding standard deduction married 2plus HoH | USD [[FACT:ca.wh.std_deduction.married_2plus_hoh=11,412]] | 2026-01-01 to 2026-12-31 |  | S5 |  |
| Withholding allowance credit per allowance | USD [[FACT:ca.wh.allowance_credit.per_allowance=168.30]] | 2026-01-01 to 2026-12-31 |  | S5 |  |
| Withholding estimated deduction per allowance | USD [[FACT:ca.wh.estimated_deduction.per_allowance=1,000]] | 2026-01-01 to 2026-12-31 |  | S5 |  |
| PIT brackets married ceilings | [[FACT:ca.pit.brackets.married.ceilings=22,158 / 52,528 / 82,904 / 115,084 / 145,448 / 742,958 / 891,542 / 1,000,000 / 1,485,906; 14.63% over; base 164,228.58]] | 2026-01-01 to 2026-12-31 |  | S5 | Rates per DE 44 Method B Married table (read the table, not this summary, for the rate attached to each band around the 1,000,000 kink). |
| PIT brackets HoH ceilings | [[FACT:ca.pit.brackets.hoh.ceilings=22,173 / 52,530 / 67,716 / 83,805 / 98,990 / 505,208 / 606,251 / 1,000,000 / 1,010,417; base 107,334.77]] | 2026-01-01 to 2026-12-31 |  | S5 | Rates per DE 44 Method B HoH table. |
| Withholding supplemental rate bonus stock options | [[FACT:ca.wh.supplemental.rate.bonus_stock_options=10.23]] % | from 2026-01-01 |  | S7 | When paid separately: aggregate or flat; with regular wages: aggregate. |
| Withholding supplemental rate other | [[FACT:ca.wh.supplemental.rate.other=6.6]] % | from 2026-01-01 |  | S7 | Overtime, commissions, severance, vacation pay etc. paid separately. |
| Withholding household by agreement only | [[FACT:ca.wh.household.by_agreement_only=True]] | from 2026-01-01 |  | S7 |  |

## CA.2b Non-resident regime and reciprocity

Sourcing: [[FACT:ca.nonres.sourcing=residents: all wages with credit for other-state withholding (withhold excess only); nonresidents wholly in CA: all wages; split-state: CA working days / total working days (volume ratio for commissions); military spouse exclusion on DE 4]].

**Resident / non-resident matrix (California PIT)**

| Income type | Resident | Non-resident |
|---|---|---|
| Regular salary | Method A or B on all wages; where another State withholds, withhold only the excess | Method A or B on California wages: all wages if working wholly in California; otherwise California working days / total working days (volume ratio for commissions) |
| Annual bonus / supplemental pay | [[FACT:ca.wh.supplemental.rate.bonus_stock_options=10.23]] % (bonus) or aggregate | Same, on the California portion |
| Severance | [[FACT:ca.wh.supplemental.rate.other=6.6]] % when paid separately, or aggregate | Same, on the California portion |
| Equity (stock options) | [[FACT:ca.wh.supplemental.rate.bonus_stock_options=10.23]] % when paid separately, or aggregate | Same, on the California portion |
| Benefits in kind | PIT wages per CA.8 (HSA taxable; group-term life above the excluded coverage reportable, not withheld) | Same, on the California portion |
| Contractor pay | Out of scope | Out of scope |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Non-resident sourcing | [[FACT:ca.nonres.sourcing=residents: all wages with credit for other-state withholding (withhold excess only); nonresidents wholly in CA: all wages; split-state: CA working days / total working days (volume ratio for commissions); military spouse exclusion on DE 4]] | from 2026-01-01 |  | S7 | No reciprocity agreement and no local wage tax in the full DE 44 scan. |

## CA.3 Social insurance: unemployment, disability, paid leave and payroll levies

Employer: UI on wages up to USD [[FACT:ca.sui.wage_base=7,000]] plus the Employment Training Tax ([[FACT:ca.ett.rate=0.1]] %). Employee: State Disability Insurance (SDI, which funds disability and paid family leave) at [[FACT:ca.sdi.employee.rate=1.3]] % on all wages, with no wage cap ([[FACT:ca.sdi.wage_cap.exists=False]]). A voluntary plan replaces SDI where approved (W-2 box 14 label [[FACT:ca.sdi.voluntary_plan.w2_box14_label=VPDI]]).

```
ca_sdi = period_SDI_wages x ca_sdi_employee_rate          # no annual cap
```

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| SUI wage base | USD [[FACT:ca.sui.wage_base=7,000]] | from 2026-01-01 |  | S8 | Kept for 2027. |
| SUI new employer rate | [[FACT:ca.sui.new_employer.rate=3.4]] % | from 2026-01-01 |  | S8 | 2-3 years; range 1.5%-6.2%; employer only; max [[FACT:ca.sui.max_per_employee=434]]/employee. |
| SUI employer rate min | [[FACT:ca.sui.employer.rate.min=1.5]] % | 2026-01-01 to 2026-12-31 |  | S9 |  |
| SUI employer rate max | [[FACT:ca.sui.employer.rate.max=6.2]] % | 2026-01-01 to 2026-12-31 |  | S9 |  |
| ETT rate | [[FACT:ca.ett.rate=0.1]] % | from 2026-01-01 |  | S10 | On first 7,000 (max 7/employee); same 2027. |
| SDI employee rate | [[FACT:ca.sdi.employee.rate=1.3]] % | 2026-01-01 to 2026-12-31 |  | S11 | Includes PFL; no wage cap since 2024-01-01 (SB 951); no employer share. A WebFetch summary saying 1.4% is WRONG. 2027 rate unpublished (open). |
| SDI wage cap exists | [[FACT:ca.sdi.wage_cap.exists=False]] | from 2024-01-01 |  | S11 |  |
| SDI voluntary plan W-2 box14 label | [[FACT:ca.sdi.voluntary_plan.w2_box14_label=VPDI]] | from 2026-01-01 |  | S12 |  |

⚠️ RESEARCH-GAP (non-blocking): SDI employee rate next year: not established by the research. Source that would close it: EDD Rates and Withholding page or DE 44 2027 (normally December 2026).

⚠️ RESEARCH-GAP (non-blocking): SDI benefit weekly max: not established by the research. Source that would close it: EDD Quick Statistics page.

## CA.4 Pay statement

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Payslip items | [[FACT:ca.payslip.items=gross wages; total hours (not salaried exempt); piece-rate units and rates; deductions; net wages; pay-period dates; employee name + last 4 SSN or employee ID; employer legal name and address; every hourly rate with hours]] | from 2026-01-01 |  | S13 | Lab. Code 226(a); semimonthly or with each payment; household excluded (226(d)); public employers only SSN rule (226(i)). |
| Payslip sick leave balance required | [[FACT:ca.payslip.sick_leave_balance.required=True]] | from 2026-01-01 |  | S14 | On the statement or a separate writing each payday (Lab. Code 246(i)). |
| Payslip inspection response days | [[FACT:ca.payslip.inspection_response_days=21]] days | from 2026-01-01 |  | S13 |  |
| Payslip penalty max | USD [[FACT:ca.payslip.penalty.max=4,000]] | from 2026-01-01 |  | S13 | 50 first / 100 subsequent per violation up to [[FACT:ca.payslip.penalty.max=4,000]]; 750 for failing an inspection request. |

## CA.5 Statutory reporting

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Registration de1 trigger | USD [[FACT:ca.registration.de1.trigger=100]] | from 2026-01-01 |  | S15 | DE 1 within 15 days after paying more than [[FACT:ca.registration.de1.trigger=100]] in wages in a quarter; DE 1P PIT-only. |
| Report deposit de88 | [[FACT:ca.report.deposit.de88=follows federal schedule: next-day if accumulated PIT > 400; semi-weekly; monthly by 15th if >= 350; quarterly if < 350; EFT by 3rd business day; 15% failure-to-deposit penalty]] | from 2026-01-01 |  | S15 |  |
| Report quarterly de9 DE 9C | [[FACT:ca.report.quarterly.de9_de9c=DE 9 + DE 9C electronic only, zero returns filed; due Apr 1/Jul 1/Oct 1/Jan 1, delinquent after Apr 30, Jul 31, Nov 2 2026, Feb 1 2027; DE 9C per employee subject wages, PIT wages, PIT withheld; corrections DE 9ADJ]] | from 2026-01-01 |  | S15 |  |
| Report W-2 filed with state | [[FACT:ca.report.w2.filed_with_state=False]] | from 2026-01-01 |  | S12 | W-2 to employees by 2027-02-01: box 14 CASDI, 16 CA PIT wages, 17 CA PIT withheld; not filed with EDD/FTB. No separate annual reconciliation. |
| Newhire report days | [[FACT:ca.newhire.report_days=20]] days | from 2026-01-01 |  | S12 | DE 34 from start-of-work date; rehire after separation of 60+ days; contractors DE 542 at 600+. |

⚠️ RESEARCH-GAP (non-blocking): Report DE 9C file format: not established by the research. Source that would close it: EDD e-Services for Business File Transfer spec / DE 9C and DE 34 layouts.

## CA.6 Leave

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Leave sick accrual hours worked per hour | [[FACT:ca.leave.sick.accrual.hours_worked_per_hour=30]] hours | from 2024-01-01 |  | S14 | Lab. Code 246 (SB 616): eligible after [[FACT:ca.leave.sick.accrual.hours_worked_per_hour=30]] days; alternative 24 h by day 120 and 40 h by day 200; use from day 90; usage cap 40 h/5 days; balance cap 80 h/10 days; front-load 40 h; reinstated on rehire within 1 year; regular rate or 90-day average; increment max 2 h. |
| Leave sick usage cap hours | [[FACT:ca.leave.sick.usage_cap_hours=40]] hours | from 2024-01-01 |  | S14 |  |
| Leave sick accrual cap hours | [[FACT:ca.leave.sick.accrual_cap_hours=80]] hours | from 2024-01-01 |  | S14 |  |
| Leave sick payout on separation | [[FACT:ca.leave.sick.payout_on_separation=False]] | from 2024-01-01 |  | S14 |  |

## CA.7 Termination and final pay

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Final pay discharge | [[FACT:ca.final_pay.discharge=immediately (72 h for seasonal perishable-food layoffs); quit: within 72 h or last day with 72 h notice; waiting-time penalty 1 day wages per day up to 30 days]] | from 2026-01-01 |  | S16 |  |
| Final pay waiting time penalty max days | [[FACT:ca.final_pay.waiting_time_penalty_max_days=30]] days | from 2026-01-01 |  | S16 |  |
| Final pay vested vacation payout | [[FACT:ca.final_pay.vested_vacation_payout=True]] | from 2026-01-01 |  | S16 | Lab. Code 227.3: paid at final rate; forfeiture prohibited. |
| Separation notice | [[FACT:ca.separation_notice=CUIC 1089 Notice to Employee as to Change in Relationship + DE 2320 at discharge, layoff or leave; email only with opt-in]] | from 2026-01-01 |  | S12 |  |
| Warn notice days | [[FACT:ca.warn.notice_days=60]] days | from 2026-01-01 |  | S12 | Cal-WARN Lab. Code 1400-1408; 75-employee threshold not quoted (open). |

⚠️ RESEARCH-GAP (non-blocking): Warn employer threshold: not established by the research. Source that would close it: Lab. Code 1400 text or EDD WARN employer page.

## CA.8 Benefits in kind and taxable wages

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| HSA conforms | [[FACT:ca.hsa.conforms=False]] | from 2026-01-01 |  | S17 | Employer and employee HSA contributions subject to UI/ETT, SDI and PIT (not UI/SDI via cafeteria plan); employer HSA (W-2 code W) added back for PIT. |
| Wages 401k deferrals | [[FACT:ca.wages.401k_deferrals=UI/SDI subject; PIT not subject]] | from 2026-01-01 |  | S17 |  |
| Wages GTL over 50k | [[FACT:ca.wages.gtl_over_50k=UI/SDI not subject; PIT not withheld but reportable]] | from 2026-01-01 |  | S17 |  |
| Obbba conforms | [[FACT:ca.obbba.conforms=False]] | from 2026-01-01 |  | S18 | No state tips or overtime deduction. |
| Meals value per day | USD [[FACT:ca.meals.value.per_day=15.85]] | 2026-01-01 to 2026-12-31 |  | S19 | Breakfast [[FACT:ca.meals.value.breakfast=3.25]], lunch 4.90, dinner 7.70, unidentified 5.70. |
| Meals value breakfast | USD [[FACT:ca.meals.value.breakfast=3.25]] | 2026-01-01 to 2026-12-31 |  | S19 |  |
| Meals value lunch | USD [[FACT:ca.meals.value.lunch=4.90]] | 2026-01-01 to 2026-12-31 |  | S19 |  |
| Meals value dinner | USD [[FACT:ca.meals.value.dinner=7.70]] | 2026-01-01 to 2026-12-31 |  | S19 |  |
| Lodging value min weekly | USD [[FACT:ca.lodging.value.min_weekly=66.10]] | 2026-01-01 to 2026-12-31 |  | S19 | 66 2/3% of rental value, min [[FACT:ca.lodging.value.min_weekly=66.10]]/week, max [[FACT:ca.lodging.value.max_monthly=2,038]]/month. |
| Lodging value max monthly | USD [[FACT:ca.lodging.value.max_monthly=2,038]] | 2026-01-01 to 2026-12-31 |  | S19 |  |

⚠️ RESEARCH-GAP (non-blocking): HSA conformity 2026: not established by the research. Source that would close it: Enacted bill on leginfo, FTB 2026 Schedule CA instructions or FTB What's New.

## CA.9 Deductions and garnishments

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Garnishment creditor max percent | [[FACT:ca.garn.creditor.max_percent=20]] % | from 2026-01-01 |  | S20 | WG-002 Rev. 2026-01-01: lesser of [[FACT:ca.garn.creditor.max_percent=20]] % of disposable earnings or 40% of disposable earnings above minimum wage x 48 (weekly) / 96 (biweekly) / 104 (semimonthly) / 208 (monthly); local MW if higher; support first. |
| Garnishment creditor excess percent | [[FACT:ca.garn.creditor.excess_percent=40]] % | from 2026-01-01 |  | S20 |  |
| Garnishment creditor minimum wage multiple weekly | [[FACT:ca.garn.creditor.minwage_multiple.weekly=48]] ratio | from 2026-01-01 |  | S20 |  |
| Garnishment child support cap percent | [[FACT:ca.garn.child_support.cap_percent=50]] % | from 2026-01-01 |  | S21 | [[FACT:ca.garn.child_support.cap_percent=50]] % after taxes; remit to SDU within 7 business days of pay date electronically (Fam. Code 17309.5); IWO kept 1 year after separation. |
| Garnishment child support remit business days | [[FACT:ca.garn.child_support.remit_business_days=7]] business days | from 2026-01-01 |  | S21 |  |
| Deductions tip credit allowed | [[FACT:ca.deductions.tip_credit.allowed=False]] | from 2026-01-01 |  | S22 | Lab. Code 224, 351: deductions only if required by law or authorised in writing; no tip credit; card tips without processing fees. |

⚠️ RESEARCH-GAP (non-blocking): Garnishment child support employer fee: not established by the research. Source that would close it: Family Code 5235 text and FTB "Earnings Withholding Order for Taxes" employer instructions.

## CA.10 Collective agreements and prevailing wage

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Prevailing wage certified payroll | [[FACT:ca.prevailing_wage.certified_payroll=electronic to Labor Commissioner via DIR eCPR (XML upload spec available)]] | from 2026-01-01 |  | S23 | [partial row] |

⚠️ RESEARCH-GAP (non-blocking): Prevailing wage thresholds: not established by the research. Source that would close it: Lab. Code 1725.5 / 1771 / 1773.3 text or DIR registration FAQ.

## CA.11 Indexation

The minimum wage is CPI-indexed (the Department of Finance certifies by 1 August, Lab. Code 1182.12(d)); the exempt-salary threshold follows the minimum wage by statutory multiple; the PIT tables are indexed yearly in DE 44; the UI base is fixed in statute (USD [[FACT:ca.sui.wage_base=7,000]]); the SDI rate is set yearly; meal and lodging values are set yearly.

## CA.12 Payroll data protection and records

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Records wage statement retention years | [[FACT:ca.records.wage_statement.retention_years=3]] years | from 2026-01-01 |  | S13 |  |
| Records edd payroll retention years | [[FACT:ca.records.edd_payroll.retention_years=4]] years | from 2026-01-01 |  | S19 | 8 years for non-employee payments. |
| CCPA request response days | [[FACT:ca.ccpa.request_response_days=45]] days | from 2023-01-01 |  | S24 | Extendable to 90; employee data in scope since 2023-01-01 (A.3). |

## CA.13 Live legal change

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Live ab1514 manicurists | [[FACT:ca.live.ab1514_manicurists=Borello test reinstated for licensed manicurists 2026-01-01 to 2028-12-31; commercial-fisher exception extended]] | 2026-01-01 to 2028-12-31 |  | S8 |  |
| Delinquent tax interest rate | [[FACT:ca.delinquent_tax.interest_rate=7]] % | 2026-01-01 to 2026-12-31 |  | S8 |  |

## CA.14 Authority worked examples (oracle values)

Oracle suite: [[FACT:ca.oracle.suite=DE 44 Rev. 52 (4-26) Method B examples A-F]]. Example F is recomputed below from the keyed parameters (married, annual payroll expressed monthly). The married schedule is carried as one ceiling string; the first two married bands carry the single-schedule rates, as the published example shows. Rounding: half-up to the cent.

| Line | Calculation | Result |
|---|---|---|
| Annual wages | example input | 57,000.00 |
| Low-income exemption test | 57,000.00 > USD [[FACT:ca.wh.low_income_exemption.married_2plus_hoh=37,791]] | taxable |
| Taxable income | 57,000.00 - USD [[FACT:ca.wh.std_deduction.married_2plus_hoh=11,412]] | 45,588.00 |
| Band 1 tax | 22,158.00 x [[FACT:ca.pit.bracket.single.1.rate=1.1]] % | 243.74 |
| Band 2 tax | (45,588.00 - 22,158.00) x [[FACT:ca.pit.bracket.single.2.rate=2.2]] % = 23,430.00 x rate | 515.46 |
| Gross annual tax | 243.74 + 515.46 | 759.20 |
| Allowance credits | 4 x USD [[FACT:ca.wh.allowance_credit.per_allowance=168.30]] | 673.20 |
| Annual tax | 759.20 - 673.20 | 86.00 |
| Monthly withholding | 86.00 / 12 | USD [[FACT:ca.oracle.de44.example_f.withholding_monthly=7.17]] |

The computed monthly withholding equals the published value. Example E (semi-monthly) published value: USD [[FACT:ca.oracle.de44.example_e.withholding_semimonthly=4.13]]; its inputs are not keyed, so it is reproduced in Module 12 rather than here.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Oracle DE 44 example f withholding monthly | USD [[FACT:ca.oracle.de44.example_f.withholding_monthly=7.17]] | 2026-01-01 to 2026-12-31 |  | S5 | DE 44 Method B example F: annual 57,000 married 4 allowances; 57,000 - [[FACT:ca.wh.std_deduction.married_2plus_hoh=11,412]] = 45,588 -> 243.74 + [[FACT:ca.pit.bracket.single.2.rate=2.2]] % x 23,430 = 759.20 - 673.20 = 86.00/yr = [[FACT:ca.oracle.de44.example_f.withholding_monthly=7.17]]/month. Recomputed |
| Oracle DE 44 example e withholding semimonthly | USD [[FACT:ca.oracle.de44.example_e.withholding_semimonthly=4.13]] | 2026-01-01 to 2026-12-31 |  | S5 | DE 44 Method B example E, Recomputed Single cumulative bases also re-derive (121.87... 114,220.27); 34,084.81 derives as 34,084.80 (intermediate rounding residual 0.01). |
| Oracle suite | [[FACT:ca.oracle.suite=DE 44 Rev. 52 (4-26) Method B examples A-F]] | 2026-01-01 to 2026-12-31 |  | S5 |  |

## CA.15 Special populations

- Domestic and household workers: UI and ETT above the quarterly cash-wage threshold; SDI above its own quarterly threshold; PIT only by agreement; the Lab. Code 226 statement does not apply.
- Agricultural workers: UI, ETT and SDI apply; PIT withholding not required but PIT wages reportable (H-2A the same); overtime phase-in open (CA.1).
- Minors: learner rate ([[FACT:ca.minwage.learner.percent=85]] % of minimum wage, any age); newspaper carriers under 18 excluded from UI, SDI and PIT.
- Tipped employees: no tip credit.
- Clergy: ministers and religious orders not subject to UI and SDI (elective) and PIT withholding not required; church employees not subject to UI and SDI, subject to PIT.
- Students: own-school students, student nurses, young work-study students and organised-camp students not subject to UI and SDI, subject to PIT.
- Non-resident aliens on F, J, M or Q visas: excluded from UI and SDI (CUIC 608); PIT subject unless a treaty covers State taxes.
- Statutory employees: UI and SDI per DE 231TE/SE; commissioned authors no PIT withholding.
- Government: UI subject; SDI only by election; PIT subject; elected officials, judiciary and National Guard not subject to UI and SDI.

⚠️ RESEARCH-GAP (non-blocking): the coverage thresholds that apply to these populations (quarterly cash-wage and headcount thresholds for UI coverage of domestic, agricultural and non-profit employment) are cited by statute only and carry no facts key; the engine must not hard-code them until they are keyed.

## CA.16 Language

The Lab. Code 2810.5 hire notice must be in the language the employer normally uses with the employee; the payslip is in English.

## CA.S Sources

| Ref | Instrument | Article / section | Authority |
|---|---|---|---|
| S1 | DIR Labor Commissioner FAQ Minimum Wage (MW-2026), Wayback 2026-10-31 | Minimum Wage Order MW-2026; Labor Code 1182.12 | California Department of Industrial Relations / Labor Commissioner |
| S2 | DIR News 2026-66 (ICYMI) and Governor press release 2026-07-31: statewide minimum wage [[FACT:ca.minwage.hourly=17.40]] from 2027-01-01 | Labor Code 1182.12(d) annual CPI adjustment, DOF certification 2026-07-31 | California DIR Labor Commissioner; Office of the Governor (DOF certification … |
| S3 | California Labor Code section 510 (daily and weekly overtime), leginfo via Wayback 2026-01-02 | Lab. Code 510(a); amended Stats. 1999 ch.134 | California Legislative Counsel |
| S4 | California Labor Code section 204 (paydays) and 213(d) (direct deposit by voluntary authorization), leginfo via Wayback | Lab. Code 204 (amended Stats. 2019 ch.508, SB 698, eff. 2020-01-01; snapshot 2026-08-31); Lab. Code 213(d) (amended Stats. 2005 ch.149; snapshot 2022-10-15) | California Legislative Counsel |
| S5 | EDD DE 44 California Employer Guide 2026 (Rev. 52 4-26): Method B Exact Calculation tables 1-28 and worked examples A-F | DE 44 pp.20, 43-51 (PDF pp.53-60): Method B Tables 1-10 | California Employment Development Department (EDD); tables prepared with … |
| S6 | EDD DE 4 Employee's Withholding Allowance Certificate (Rev. 56 1-26) | DE 4 Rev. 56 (1-26) | California EDD |
| S7 | EDD DE 44 2026: DE 4 rules, supplemental wages, residents/nonresidents withholding | DE 44 pp.16-19 | California EDD |
| S8 | EDD California Employer News and Updates (page read 2026-11-02) | News items Nov 2025 - Oct 2026 | California EDD |
| S9 | UI Schedule F+ emergency surcharge (15% on Schedule F) | EDD UI rate for 2026 | CA official authority |
| S10 | Employment Training Tax (ETT) | CA UI Code (ETT) | CA official authority |
| S11 | State Disability Insurance (SDI incl. PFL) | SB 951; DE 44 | CA official authority |
| S12 | EDD DE 44 2026: Form W-2 state boxes, no state W-2 filing, DE 9C content, new-hire DE 34 fields, WARN, UI reciprocal coverage | DE 44 pp.56-57, 65, 70-71, 73, 79 | California EDD |
| S13 | California Labor Code section 226 (itemized wage statement), leginfo text via Wayback 2026-08-31 | Lab. Code 226(a)-(j); amended Stats. 2023 ch.866 (SB 332) eff. 2023-10-13 | California Legislative Counsel (leginfo.legislature.ca.gov) |
| S14 | California Labor Code section 246 (paid sick leave), leginfo via Wayback 2025-01-23 | Lab. Code 246(a)-(l) as amended by SB 616 (2023), operative 2024-01-01 | California Legislative Counsel |
| S15 | EDD DE 44 2026: Forms and Due Dates, California Deposit Requirements, DE 9/DE 9C due dates, registration, new hire DE 34, DE 542 | DE 44 p.5 (PDF p.13), pp.56-66 | California EDD |
| S16 | California Labor Code sections 201, 202, 203 (final pay and waiting-time penalty) and 227.3 (vested vacation payout), leginfo via Wayback 2025 | Lab. Code 201(a) (Stats. 2018 ch.903); 202(a) (Stats. 2018 ch.903); 203(a) (Stats. 2019 ch.700, SB 286); 227.3 (Stats. 1976 ch.1041) | California Legislative Counsel |
| S17 | EDD Information Sheet DE 231EB Taxability of Employee Benefits (Rev. 12 6-17) | DE 231EB pp.2-4 (UI/ETT, SDI, PIT withholding columns) | California EDD |
| S18 | FTB 2025 Instructions for Schedule CA (540), revised 04/2026: HSA nonconformity and OBBBA nonconformity | Line 1h (employer HSA contribution, W-2 box 12 code W), line 13; Federal Tax Changes under OBBBA | California Franchise Tax Board |
| S19 | EDD DE 44 2026: Meals and lodging values; subject wages vs PIT wages; recordkeeping | DE 44 pp.12, 14-15 | California EDD |
| S20 | Judicial Council of California form WG-002 Earnings Withholding Order (Rev. January 1, 2026), employer computation instructions (CCP 706.050) | WG-002 page 1, Instructions to Employer (A)-(C), Steps 1-5 | Judicial Council of California |
| S21 | California Child Support Services PUB 307 California Employers and the SDU (06/2026) and IWO Employer Fact Sheet (09/2019) | PUB 307 (2026-06-22); IWO Fact Sheet; Family Code 17309.5 | California Department of Child Support Services |
| S22 | California Labor Code section 224 (authorised deductions) and 351 (gratuities), leginfo via Wayback 2025 | Lab. Code 224 (Stats. 1968 ch.559); Lab. Code 351 (Stats. 2000 ch.876) | California Legislative Counsel |
| S23 | DIR Certified Payroll Reports page (Public Works), Wayback 2026 | Lab. Code 1776 (CPR); eCPR XML guidelines | California DIR / Labor Commissioner |
| S24 | California Privacy Protection Agency FAQ (CCPA as amended by CPRA): employee and job applicant data | FAQ: consumers include employees and job applicants; Civil Code 1798.145(m)-(n) exemptions expired 2022-12-31 | California Privacy Protection Agency |

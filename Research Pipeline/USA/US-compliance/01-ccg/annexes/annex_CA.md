# Annex CA: California


This annex sets out the California payroll rules for the 2026 build year. Read with Annex FED (the federal layer every employee carries) and Annex MULTI (which routes an employee to this State by work location, residence or UI localization). Every value is shown with its effective dates and its source (list at the end of the annex). Federal values are not repeated here.

Classification: T3. Separate State withholding (PIT) and payroll taxes (UI, ETT, SDI) on one EDD return set; no local wage tax; local minimum wages exist.

## CA.1 Employment and labour code

State minimum wage USD [[FACT:ca.minwage.hourly=16.90]] for 2026 and USD [[FACT:ca.minwage.hourly=17.40]] for 2027. Overtime: [[FACT:ca.overtime.rule=1.5x over 8 h/day, over 40 h/week and first 8 h of 7th consecutive day; 2x over 12 h/day and over 8 h on 7th day (Lab. Code 510); alternative workweek exceptions]]. No tip credit ([[FACT:ca.deductions.tip_credit.allowed=False]]). Cities and counties may set higher minimum wages and some industries have their own minimums: both are blocking gaps below, so a California work location cannot be paid at the State rate without first checking the locality and the industry.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Minimum wage hourly | USD [[FACT:ca.minwage.hourly=16.90]] | 2026-01-01 to 2026-12-31 |  | S1 | All employers; learners 85% for first 160 hours. |
| Minimum wage hourly | USD [[FACT:ca.minwage.hourly=17.40]] | from 2027-01-01 |  | S2 | DOF certified 2026-07-31; DIR News 2026-66 + Governor release. Check [[FACT:ca.minwage.hourly=16.90]] x 1.0299 = 17.405 -> [[FACT:ca.minwage.hourly=17.40]]. |
| Minimum wage learner percent | [[FACT:ca.minwage.learner.percent=85]] % | from 2026-01-01 |  | S1 | First 160 hours of employment. |
| Exempt salary annual min | USD [[FACT:ca.exempt.salary.annual_min=70,304]] | 2026-01-01 to 2026-12-31 |  | S1 | 2 x [[FACT:ca.minwage.hourly=16.90]] x 2,080. |
| Exempt salary annual min | USD [[FACT:ca.exempt.salary.annual_min=72,384]] | from 2027-01-01 |  | S2 | Quoted by DIR (= 2 x [[FACT:ca.minwage.hourly=17.40]] x 2,080). |
| Overtime rule | [[FACT:ca.overtime.rule=1.5x over 8 h/day, over 40 h/week and first 8 h of 7th consecutive day; 2x over 12 h/day and over 8 h on 7th day (Lab. Code 510); alternative workweek exceptions]] | from 2026-01-01 |  | S3 |  |
| Overtime daily threshold hours | [[FACT:ca.overtime.daily_threshold_hours=8]] hours | from 2026-01-01 |  | S3 |  |
| Overtime double time daily threshold hours | [[FACT:ca.overtime.double_time_daily_threshold_hours=12]] hours | from 2026-01-01 |  | S3 |  |
| Pay frequency rule | [[FACT:ca.pay_frequency.rule=twice a month: 1st-15th paid 16th-26th; 16th-end paid 1st-10th next month; EAP monthly by 26th; weekly/biweekly/semimonthly within 7 days of period close; OT by next regular payday (Lab. Code 204)]] | from 2026-01-01 |  | S4 |  |
| Direct deposit requires voluntary authorisation | [[FACT:ca.direct_deposit.requires_voluntary_authorisation=True]] | from 2026-01-01 |  | S4 | Lab. Code 213(d). |
| Minimum wage fast food hourly | USD [[FACT:ca.minwage.fast_food.hourly=20]] | from 2024-04-01 |  | S5 | Fast-food restaurant employees (Lab. Code 1474, AB 1228). The DIR Minimum Wage page and Fast Food FAQ read 2026-11-02 show no Fast Food Council increase after 2024-04-01. Exempt-salary test for these employees: 2 x [[FACT:ca.minwage.fast_food.hourly=20]] x 40 x 52 = 83,200 (FAQ). |
| Minimum wage health care large system hourly | USD [[FACT:ca.minwage.health_care.large_system.hourly=24]] | 2025-07-01 to 2026-06-30 |  | S6 | Hospital or integrated health system with 10,000+ FTE (incl. SNFs they operate). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care large system hourly | USD [[FACT:ca.minwage.health_care.large_system.hourly=25]] | 2026-07-01 to 2027-12-31 |  | S6 | Hospital or integrated health system with 10,000+ FTE (incl. SNFs they operate). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care dialysis clinic hourly | USD [[FACT:ca.minwage.health_care.dialysis_clinic.hourly=24]] | 2025-07-01 to 2026-06-30 |  | S6 | Dialysis clinics. SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care dialysis clinic hourly | USD [[FACT:ca.minwage.health_care.dialysis_clinic.hourly=25]] | 2026-07-01 to 2027-12-31 |  | S6 | Dialysis clinics. SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care safety net hospital hourly | USD [[FACT:ca.minwage.health_care.safety_net_hospital.hourly=18.63]] | 2025-07-01 to 2026-06-30 |  | S6 | Safety-net hospitals (FAQ 14). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care safety net hospital hourly | USD [[FACT:ca.minwage.health_care.safety_net_hospital.hourly=19.28]] | 2026-07-01 to 2027-06-30 |  | S6 | Safety-net hospitals (FAQ 14). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care safety net hospital hourly | USD [[FACT:ca.minwage.health_care.safety_net_hospital.hourly=19.95]] | 2027-07-01 to 2028-06-30 |  | S6 | Safety-net hospitals (FAQ 14). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care safety net hospital hourly | USD [[FACT:ca.minwage.health_care.safety_net_hospital.hourly=20.65]] | 2028-07-01 to 2029-06-30 |  | S6 | Safety-net hospitals (FAQ 14). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care safety net hospital hourly | USD [[FACT:ca.minwage.health_care.safety_net_hospital.hourly=21.37]] | 2029-07-01 to 2030-06-30 |  | S6 | Safety-net hospitals (FAQ 14). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care safety net hospital hourly | USD [[FACT:ca.minwage.health_care.safety_net_hospital.hourly=22.12]] | 2030-07-01 to 2031-06-30 |  | S6 | Safety-net hospitals (FAQ 14). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care safety net hospital hourly | USD [[FACT:ca.minwage.health_care.safety_net_hospital.hourly=22.89]] | 2031-07-01 to 2032-06-30 |  | S6 | Safety-net hospitals (FAQ 14). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care safety net hospital hourly | USD [[FACT:ca.minwage.health_care.safety_net_hospital.hourly=25]] | 2033-07-01 to 2034-12-31 |  | S6 | Safety-net hospitals (FAQ 14). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. The FAQ table lists no safety-net step for 2032-07-01..2033-06-30 (the small-county column lists [[FACT:ca.minwage.health_care.county_small.hourly=23.69]] there); transcribed as printed. |
| Minimum wage health care clinic hourly | USD [[FACT:ca.minwage.health_care.clinic.hourly=21]] | 2024-10-16 to 2026-06-30 |  | S6 | Intermittent, community or rural health clinics and associated urgent care. SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care clinic hourly | USD [[FACT:ca.minwage.health_care.clinic.hourly=22]] | 2026-07-01 to 2027-06-30 |  | S6 | Intermittent, community or rural health clinics and associated urgent care. SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care clinic hourly | USD [[FACT:ca.minwage.health_care.clinic.hourly=25]] | 2027-07-01 to 2028-12-31 |  | S6 | Intermittent, community or rural health clinics and associated urgent care. SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care other facility hourly | USD [[FACT:ca.minwage.health_care.other_facility.hourly=21]] | 2024-10-16 to 2026-06-30 |  | S6 | All other covered health care facilities not run by counties. SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care other facility hourly | USD [[FACT:ca.minwage.health_care.other_facility.hourly=23]] | 2026-07-01 to 2028-06-30 |  | S6 | All other covered health care facilities not run by counties. SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care other facility hourly | USD [[FACT:ca.minwage.health_care.other_facility.hourly=25]] | 2028-07-01 to 2029-12-31 |  | S6 | All other covered health care facilities not run by counties. SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care county large hourly | USD [[FACT:ca.minwage.health_care.county_large.hourly=24]] | 2025-07-01 to 2026-06-30 |  | S6 | Covered facilities run by large counties (>5 million people at 2023-01-01). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care county large hourly | USD [[FACT:ca.minwage.health_care.county_large.hourly=25]] | 2026-07-01 to 2027-12-31 |  | S6 | Covered facilities run by large counties (>5 million people at 2023-01-01). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care county medium hourly | USD [[FACT:ca.minwage.health_care.county_medium.hourly=21]] | 2025-01-01 to 2026-06-30 |  | S6 | Covered facilities run by medium counties (250,000-5 million). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care county medium hourly | USD [[FACT:ca.minwage.health_care.county_medium.hourly=23]] | 2026-07-01 to 2028-06-30 |  | S6 | Covered facilities run by medium counties (250,000-5 million). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care county medium hourly | USD [[FACT:ca.minwage.health_care.county_medium.hourly=25]] | 2028-07-01 to 2029-12-31 |  | S6 | Covered facilities run by medium counties (250,000-5 million). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care county small hourly | USD [[FACT:ca.minwage.health_care.county_small.hourly=18.63]] | 2025-07-01 to 2026-06-30 |  | S6 | Covered facilities run by small counties (<250,000). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care county small hourly | USD [[FACT:ca.minwage.health_care.county_small.hourly=19.28]] | 2026-07-01 to 2027-06-30 |  | S6 | Covered facilities run by small counties (<250,000). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care county small hourly | USD [[FACT:ca.minwage.health_care.county_small.hourly=19.95]] | 2027-07-01 to 2028-06-30 |  | S6 | Covered facilities run by small counties (<250,000). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care county small hourly | USD [[FACT:ca.minwage.health_care.county_small.hourly=20.65]] | 2028-07-01 to 2029-06-30 |  | S6 | Covered facilities run by small counties (<250,000). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care county small hourly | USD [[FACT:ca.minwage.health_care.county_small.hourly=21.37]] | 2029-07-01 to 2030-06-30 |  | S6 | Covered facilities run by small counties (<250,000). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care county small hourly | USD [[FACT:ca.minwage.health_care.county_small.hourly=22.12]] | 2030-07-01 to 2031-06-30 |  | S6 | Covered facilities run by small counties (<250,000). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care county small hourly | USD [[FACT:ca.minwage.health_care.county_small.hourly=22.89]] | 2031-07-01 to 2032-06-30 |  | S6 | Covered facilities run by small counties (<250,000). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care county small hourly | USD [[FACT:ca.minwage.health_care.county_small.hourly=23.69]] | 2032-07-01 to 2033-06-30 |  | S6 | Covered facilities run by small counties (<250,000). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care county small hourly | USD [[FACT:ca.minwage.health_care.county_small.hourly=25]] | 2033-07-01 to 2034-12-31 |  | S6 | Covered facilities run by small counties (<250,000). SB 525 / Lab. Code 1182.14-1182.16 schedule as shown in the DIR Labor Commissioner FAQ. |
| Minimum wage health care indexation | [[FACT:ca.minwage.health_care.indexation=CPI adjustment each January 1 after the last scheduled step (large systems, dialysis and large counties from 2028-01-01; clinics 2029-01-01; other facilities and medium counties 2030-01-01; safety-net and small counties 2035-01-01). Skilled nursing facilities outside a hospital/system: schedule applies only once a patient-care minimum spending requirement is passed.]] | from 2024-10-16 |  | S6 |  |
| Overtime agricultural phase in | [[FACT:ca.overtime.agricultural_phase_in=Fully phased in: >8h/day or >40h/week at 1.5x commencing 2022-01-01 for employers with 26+ employees; commencing 2025-01-01 for employers with 25 or fewer (earlier steps 9.5/55 from 2019, 9/50 from 2020, 8.5/45 from 2021, with +3 years for small employers)]] | from 2025-01-01 |  | S7 | |

Not configured in this release [[GAP:RQ-478]]: Local minimum wage hourly: not established from an official source.

Not configured in this release [[GAP:RQ-481]]: Payslip electronic consent: not established from an official source.

## CA.2 Income tax withholding

**Method.** [[FACT:ca.wh.method=Method A (wage-bracket tables, wages < 1M) or Method B (exact calculation), DE 44 Rev. 52 (4-26)]]. Certificate: [[FACT:ca.wh.certificate.form=DE 4 Rev. 56 (1-26); federal W-4 for FIT only since 2020; no valid DE 4 = Single 0 allowances; exempt status renewed by Feb 15]]. Method B, per pay period:

```
annual_wages = period_wages x pay_periods
if annual_wages <= low_income_exemption(status, allowances): tax = 0
taxable      = annual_wages - estimated_deduction x additional_allowances - std_deduction(status, allowances)
annual_tax   = brackets(status)(taxable) - allowance_credit x allowances
period_tax   = max(0, annual_tax) / pay_periods
```

**Which table applies to which DE 4 status.** [[FACT:ca.wh.status_table_map=DE 4 filing status -> DE 44 Method B table: 'Single or Married (with two or more incomes)' -> Table 5 'Single Persons, Dual Income Married or Married with Multiple Employers'; 'Married (one income)' -> Table 6 'Married Persons'; 'Head of Household' -> Table 7 'Unmarried/Head of Household' (annual payroll period; the same three-way order repeats for every payroll period in Tables 8-28). Table 1 (low income exemption) and Table 3 (standard deduction): 'Single or Married (with two or more incomes)' -> column 'Single, Dual Income Married or Married with Multiple Employers'; 'Married (one income)' -> column 'Married' for '0' or '1' allowances, or column 'Married' for '2' or more allowances (allowances on DE 4 or Form W-4); 'Head of Household' -> column 'Unmarried Head of Household'. No DE 4 on file -> Single with zero allowances.]]

Bands by status: the single band table in this section is DE 44 (2026) Method B Table 5 (annual), the married band table is Table 6 (Married, one income) and the head-of-household band table is Table 7; each gives the rate, the ceiling and the tax at the bottom of each band (base). A married employee who checks 'Single or Married (with two or more incomes)' is withheld on the single table, never on the married table. The same status mapping selects the column of the low-income exemption and standard deduction tables. Married ceilings: [[FACT:ca.pit.brackets.married.ceilings=22,158 / 52,528 / 82,904 / 115,084 / 145,448 / 742,958 / 891,542 / 1,000,000 / 1,485,906; 14.63% over; base 164,228.58]]; head of household ceilings: [[FACT:ca.pit.brackets.hoh.ceilings=22,173 / 52,530 / 67,716 / 83,805 / 98,990 / 505,208 / 606,251 / 1,000,000 / 1,010,417; base 107,334.77]].

**Supplemental pay** paid separately: bonuses and stock options [[FACT:ca.wh.supplemental.rate.bonus_stock_options=10.23]] %; other supplemental pay (overtime, commissions, severance, vacation pay) [[FACT:ca.wh.supplemental.rate.other=6.6]] %. Household employees: withholding only by agreement ([[FACT:ca.wh.household.by_agreement_only=True]]).

California does not conform to the federal P.L. 119-21 deductions ([[FACT:ca.obbba.conforms=False]]) and taxes employer HSA contributions ([[FACT:ca.hsa.conforms=False]]); see CA.8.

**PIT bracket single: bracket table**

| Bracket | rate | ceiling | Effective | Source |
|---|---|---|---|---|
| 1 | [[FACT:ca.pit.bracket.single.1.rate=1.1]] % | USD [[FACT:ca.pit.bracket.single.1.ceiling=11,079]] | 2026-01-01 to 2026-12-31 | S8 |
| 2 | [[FACT:ca.pit.bracket.single.2.rate=2.2]] % | USD [[FACT:ca.pit.bracket.single.2.ceiling=26,264]] | 2026-01-01 to 2026-12-31 | S8 |
| 3 | [[FACT:ca.pit.bracket.single.3.rate=4.4]] % | USD [[FACT:ca.pit.bracket.single.3.ceiling=41,452]] | 2026-01-01 to 2026-12-31 | S8 |
| 4 | [[FACT:ca.pit.bracket.single.4.rate=6.6]] % | USD [[FACT:ca.pit.bracket.single.4.ceiling=57,542]] | 2026-01-01 to 2026-12-31 | S8 |
| 5 | [[FACT:ca.pit.bracket.single.5.rate=8.8]] % | USD [[FACT:ca.pit.bracket.single.5.ceiling=72,724]] | 2026-01-01 to 2026-12-31 | S8 |
| 6 | [[FACT:ca.pit.bracket.single.6.rate=10.23]] % | USD [[FACT:ca.pit.bracket.single.6.ceiling=371,479]] | 2026-01-01 to 2026-12-31 | S8 |
| 7 | [[FACT:ca.pit.bracket.single.7.rate=11.33]] % | USD [[FACT:ca.pit.bracket.single.7.ceiling=445,771]] | 2026-01-01 to 2026-12-31 | S8 |
| 8 | [[FACT:ca.pit.bracket.single.8.rate=12.43]] % | USD [[FACT:ca.pit.bracket.single.8.ceiling=742,953]] | 2026-01-01 to 2026-12-31 | S8 |
| 9 | [[FACT:ca.pit.bracket.single.9.rate=13.53]] % | USD [[FACT:ca.pit.bracket.single.9.ceiling=1,000,000]] | 2026-01-01 to 2026-12-31 | S8 |
| 10 | [[FACT:ca.pit.bracket.single.10.rate=14.63]] % | — | 2026-01-01 to 2026-12-31 | S8 |

**PIT bracket married: bracket table**

| Bracket | rate | ceiling | base | Effective | Source |
|---|---|---|---|---|---|
| 1 | [[FACT:ca.pit.bracket.married.1.rate=1.1]] % | USD [[FACT:ca.pit.bracket.married.1.ceiling=22,158]] | USD [[FACT:ca.pit.bracket.married.1.base=0]] | 2026-01-01 to 2026-12-31 | S8 |
| 2 | [[FACT:ca.pit.bracket.married.2.rate=2.2]] % | USD [[FACT:ca.pit.bracket.married.2.ceiling=52,528]] | USD [[FACT:ca.pit.bracket.married.2.base=243.74]] | 2026-01-01 to 2026-12-31 | S8 |
| 3 | [[FACT:ca.pit.bracket.married.3.rate=4.4]] % | USD [[FACT:ca.pit.bracket.married.3.ceiling=82,904]] | USD [[FACT:ca.pit.bracket.married.3.base=911.88]] | 2026-01-01 to 2026-12-31 | S8 |
| 4 | [[FACT:ca.pit.bracket.married.4.rate=6.6]] % | USD [[FACT:ca.pit.bracket.married.4.ceiling=115,084]] | USD [[FACT:ca.pit.bracket.married.4.base=2,248.42]] | 2026-01-01 to 2026-12-31 | S8 |
| 5 | [[FACT:ca.pit.bracket.married.5.rate=8.8]] % | USD [[FACT:ca.pit.bracket.married.5.ceiling=145,448]] | USD [[FACT:ca.pit.bracket.married.5.base=4,372.30]] | 2026-01-01 to 2026-12-31 | S8 |
| 6 | [[FACT:ca.pit.bracket.married.6.rate=10.23]] % | USD [[FACT:ca.pit.bracket.married.6.ceiling=742,958]] | USD [[FACT:ca.pit.bracket.married.6.base=7,044.33]] | 2026-01-01 to 2026-12-31 | S8 |
| 7 | [[FACT:ca.pit.bracket.married.7.rate=11.33]] % | USD [[FACT:ca.pit.bracket.married.7.ceiling=891,542]] | USD [[FACT:ca.pit.bracket.married.7.base=68,169.60]] | 2026-01-01 to 2026-12-31 | S8 |
| 8 | [[FACT:ca.pit.bracket.married.8.rate=12.43]] % | USD [[FACT:ca.pit.bracket.married.8.ceiling=1,000,000]] | USD [[FACT:ca.pit.bracket.married.8.base=85,004.17]] | 2026-01-01 to 2026-12-31 | S8 |
| 9 | [[FACT:ca.pit.bracket.married.9.rate=13.53]] % | USD [[FACT:ca.pit.bracket.married.9.ceiling=1,485,906]] | USD [[FACT:ca.pit.bracket.married.9.base=98,485.50]] | 2026-01-01 to 2026-12-31 | S8 |
| 10 | [[FACT:ca.pit.bracket.married.10.rate=14.63]] % | — | USD [[FACT:ca.pit.bracket.married.10.base=164,228.58]] | 2026-01-01 to 2026-12-31 | S8 |

**PIT bracket HoH: bracket table**

| Bracket | rate | ceiling | base | Effective | Source |
|---|---|---|---|---|---|
| 1 | [[FACT:ca.pit.bracket.hoh.1.rate=1.1]] % | USD [[FACT:ca.pit.bracket.hoh.1.ceiling=22,173]] | USD [[FACT:ca.pit.bracket.hoh.1.base=0]] | 2026-01-01 to 2026-12-31 | S8 |
| 2 | [[FACT:ca.pit.bracket.hoh.2.rate=2.2]] % | USD [[FACT:ca.pit.bracket.hoh.2.ceiling=52,530]] | USD [[FACT:ca.pit.bracket.hoh.2.base=243.90]] | 2026-01-01 to 2026-12-31 | S8 |
| 3 | [[FACT:ca.pit.bracket.hoh.3.rate=4.4]] % | USD [[FACT:ca.pit.bracket.hoh.3.ceiling=67,716]] | USD [[FACT:ca.pit.bracket.hoh.3.base=911.75]] | 2026-01-01 to 2026-12-31 | S8 |
| 4 | [[FACT:ca.pit.bracket.hoh.4.rate=6.6]] % | USD [[FACT:ca.pit.bracket.hoh.4.ceiling=83,805]] | USD [[FACT:ca.pit.bracket.hoh.4.base=1,579.93]] | 2026-01-01 to 2026-12-31 | S8 |
| 5 | [[FACT:ca.pit.bracket.hoh.5.rate=8.8]] % | USD [[FACT:ca.pit.bracket.hoh.5.ceiling=98,990]] | USD [[FACT:ca.pit.bracket.hoh.5.base=2,641.80]] | 2026-01-01 to 2026-12-31 | S8 |
| 6 | [[FACT:ca.pit.bracket.hoh.6.rate=10.23]] % | USD [[FACT:ca.pit.bracket.hoh.6.ceiling=505,208]] | USD [[FACT:ca.pit.bracket.hoh.6.base=3,978.08]] | 2026-01-01 to 2026-12-31 | S8 |
| 7 | [[FACT:ca.pit.bracket.hoh.7.rate=11.33]] % | USD [[FACT:ca.pit.bracket.hoh.7.ceiling=606,251]] | USD [[FACT:ca.pit.bracket.hoh.7.base=45,534.18]] | 2026-01-01 to 2026-12-31 | S8 |
| 8 | [[FACT:ca.pit.bracket.hoh.8.rate=12.43]] % | USD [[FACT:ca.pit.bracket.hoh.8.ceiling=1,000,000]] | USD [[FACT:ca.pit.bracket.hoh.8.base=56,982.35]] | 2026-01-01 to 2026-12-31 | S8 |
| 9 | [[FACT:ca.pit.bracket.hoh.9.rate=13.53]] % | USD [[FACT:ca.pit.bracket.hoh.9.ceiling=1,010,417]] | USD [[FACT:ca.pit.bracket.hoh.9.base=105,925.35]] | 2026-01-01 to 2026-12-31 | S8 |
| 10 | [[FACT:ca.pit.bracket.hoh.10.rate=14.63]] % | — | USD [[FACT:ca.pit.bracket.hoh.10.base=107,334.77]] | 2026-01-01 to 2026-12-31 | S8 |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Withholding certificate form | [[FACT:ca.wh.certificate.form=DE 4 Rev. 56 (1-26); federal W-4 for FIT only since 2020; no valid DE 4 = Single 0 allowances; exempt status renewed by Feb 15]] | from 2026-01-01 |  | S9 |  |
| Withholding method | [[FACT:ca.wh.method=Method A (wage-bracket tables, wages < 1M) or Method B (exact calculation), DE 44 Rev. 52 (4-26)]] | from 2026-01-01 |  | S8 |  |
| Withholding low income exemption single | USD [[FACT:ca.wh.low_income_exemption.single=18,896]] | 2026-01-01 to 2026-12-31 |  | S8 | Single / Married 0-1 allowances; Married 2+ / HoH [[FACT:ca.wh.low_income_exemption.married_2plus_hoh=37,791]]. |
| Withholding low income exemption married 2plus HoH | USD [[FACT:ca.wh.low_income_exemption.married_2plus_hoh=37,791]] | 2026-01-01 to 2026-12-31 |  | S8 |  |
| Withholding standard deduction single | USD [[FACT:ca.wh.std_deduction.single=5,706]] | 2026-01-01 to 2026-12-31 |  | S8 |  |
| Withholding standard deduction married 2plus HoH | USD [[FACT:ca.wh.std_deduction.married_2plus_hoh=11,412]] | 2026-01-01 to 2026-12-31 |  | S8 |  |
| Withholding allowance credit per allowance | USD [[FACT:ca.wh.allowance_credit.per_allowance=168.30]] | 2026-01-01 to 2026-12-31 |  | S8 |  |
| Withholding estimated deduction per allowance | USD [[FACT:ca.wh.estimated_deduction.per_allowance=1,000]] | 2026-01-01 to 2026-12-31 |  | S8 |  |
| PIT brackets married ceilings | [[FACT:ca.pit.brackets.married.ceilings=22,158 / 52,528 / 82,904 / 115,084 / 145,448 / 742,958 / 891,542 / 1,000,000 / 1,485,906; 14.63% over; base 164,228.58]] | 2026-01-01 to 2026-12-31 |  | S8 | Rates per DE 44 Method B Married table (read the table, not this summary, for the rate attached to each band around the 1,000,000 kink). |
| PIT brackets HoH ceilings | [[FACT:ca.pit.brackets.hoh.ceilings=22,173 / 52,530 / 67,716 / 83,805 / 98,990 / 505,208 / 606,251 / 1,000,000 / 1,010,417; base 107,334.77]] | 2026-01-01 to 2026-12-31 |  | S8 | Rates per DE 44 Method B HoH table. |
| Withholding supplemental rate bonus stock options | [[FACT:ca.wh.supplemental.rate.bonus_stock_options=10.23]] % | from 2026-01-01 |  | S10 | When paid separately: aggregate or flat; with regular wages: aggregate. |
| Withholding supplemental rate other | [[FACT:ca.wh.supplemental.rate.other=6.6]] % | from 2026-01-01 |  | S10 | Overtime, commissions, severance, vacation pay etc. paid separately. |
| Withholding household by agreement only | [[FACT:ca.wh.household.by_agreement_only=True]] | from 2026-01-01 |  | S10 |  |
| PIT bracket married rates | [[FACT:ca.pit.bracket.married.rates=1.1 / 2.2 / 4.4 / 6.6 / 8.8 / 10.23 / 11.33 / 12.43 / 13.53 / 14.63 percent, bands per ca.pit.bracket.married.N.ceiling]] | 2026-01-01 to 2026-12-31 |  | S8 | DE 44 (2026) Method B Table 6 (annual); same rates in Table 7 for head of household (ca.pit.bracket.hoh.N.rate). |
| Withholding status table map | [[FACT:ca.wh.status_table_map=DE 4 filing status -> DE 44 Method B table: 'Single or Married (with two or more incomes)' -> Table 5 'Single Persons, Dual Income Married or Married with Multiple Employers'; 'Married (one income)' -> Table 6 'Married Persons'; 'Head of Household' -> Table 7 'Unmarried/Head of Household' (annual payroll period; the same three-way order repeats for every payroll period in Tables 8-28). Table 1 (low income exemption) and Table 3 (standard deduction): 'Single or Married (with two or more incomes)' -> column 'Single, Dual Income Married or Married with Multiple Employers'; 'Married (one income)' -> column 'Married' for '0' or '1' allowances, or column 'Married' for '2' or more allowances (allowances on DE 4 or Form W-4); 'Head of Household' -> column 'Unmarried Head of Household'. No DE 4 on file -> Single with zero allowances.]] | 2026-01-01 to 2026-12-31 |  | S8 | Table titles in DE 44 Rev. 52 (4-26): PDF p.56 'Annual Payroll Period Tax Rate Tables', Method B Tables 5, 6, 7; PDF p.54 Method B Table 1 and PDF p.55 Method B Table 3 column headings; PDF p.24: no existing withholding certificate -> 'Single with Zero withholding allowance'. DE 4 status wording from DE 4 (Rev. 56 1-26) p.1 'Filing Status'. Consequence: a married employee who checks 'Single or Married (with two or more incomes)' is withheld on the single table (Table 5), never on Table 6. |
| Withholding method b annual prorate option | [[FACT:ca.wh.method_b.annual_prorate_option=Employers may determine the amount of income tax to be withheld for an annual payroll period and prorate the tax back to the payroll period (DE 44, Method B). Design choice: annualise and prorate, or compute per payroll period.]] | from 2026-01-01 | withholding | S8 | Open Design choice (validation V-07). |

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
| Contractor pay | Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008] | Same |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Non-resident sourcing | [[FACT:ca.nonres.sourcing=residents: all wages with credit for other-state withholding (withhold excess only); nonresidents wholly in CA: all wages; split-state: CA working days / total working days (volume ratio for commissions); military spouse exclusion on DE 4]] | from 2026-01-01 |  | S10 | No reciprocity agreement and no local wage tax in the full DE 44 scan. |

## CA.2c Local wage taxes

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Local minimum wage los angeles city hourly | USD [[FACT:ca.local_minwage.los_angeles_city.hourly=17.87]] | 2025-07-01 to 2026-06-30 |  | S11 | City of Los Angeles, all employers (LAMC 187.02; CPI-W LA each July 1, announced Feb 1). |
| Local minimum wage los angeles city hourly | USD [[FACT:ca.local_minwage.los_angeles_city.hourly=18.42]] | from 2026-07-01 |  | S11 | City of Los Angeles, all employers (LAMC 187.02; CPI-W LA each July 1, announced Feb 1). |
| Local minimum wage los angeles county unincorporated hourly | USD [[FACT:ca.local_minwage.los_angeles_county_unincorporated.hourly=17.81]] | 2025-07-01 to 2026-06-30 |  | S12 | Unincorporated LA County (County Code 8.100.040). Derivation: [[FACT:ca.local_minwage.los_angeles_county_unincorporated.hourly=17.81]] x 1.037 = 18.469 -> [[FACT:ca.local_minwage.los_angeles_county_unincorporated.hourly=18.47]] (the notice states a 3.7% CPI increase); 17.27 x 1.031 = 17.805 -> [[FACT:ca.local_minwage.los_angeles_county_unincorporated.hourly=17.81]] (FY2025-26 notice, 3.1%). |
| Local minimum wage los angeles county unincorporated hourly | USD [[FACT:ca.local_minwage.los_angeles_county_unincorporated.hourly=18.47]] | from 2026-07-01 |  | S12 | Unincorporated LA County (County Code 8.100.040). Derivation: [[FACT:ca.local_minwage.los_angeles_county_unincorporated.hourly=17.81]] x 1.037 = 18.469 -> [[FACT:ca.local_minwage.los_angeles_county_unincorporated.hourly=18.47]] (the notice states a 3.7% CPI increase); 17.27 x 1.031 = 17.805 -> [[FACT:ca.local_minwage.los_angeles_county_unincorporated.hourly=17.81]] (FY2025-26 notice, 3.1%). |
| Local minimum wage san francisco hourly | USD [[FACT:ca.local_minwage.san_francisco.hourly=19.18]] | 2025-07-01 to 2026-06-30 |  | S13 | SF Minimum Wage Ordinance (L.E.C. Art. 1.4), CPI each July 1. |
| Local minimum wage san francisco hourly | USD [[FACT:ca.local_minwage.san_francisco.hourly=19.61]] | from 2026-07-01 |  | S13 | SF Minimum Wage Ordinance (L.E.C. Art. 1.4), CPI each July 1. |
| Local minimum wage san diego hourly | USD [[FACT:ca.local_minwage.san_diego.hourly=17.75]] | 2026-01-01 to 2026-12-31 |  | S14 | Employees working 2+ hours a week in the City; tips do not count (SDMC ch. 3 art. 9 div. 1). |
| Local minimum wage san diego hourly | USD [[FACT:ca.local_minwage.san_diego.hourly=18.35]] | from 2027-01-01 |  | S14 | Employees working 2+ hours a week in the City; tips do not count (SDMC ch. 3 art. 9 div. 1). |
| Local minimum wage berkeley hourly | USD [[FACT:ca.local_minwage.berkeley.hourly=19.18]] | 2025-07-01 to 2026-06-30 |  | S15 | Employees working 2+ hours in Berkeley; the City Living Wage (20.01 / 23.33 from 2026-07-01) binds city contractors only and is not a general minimum. |
| Local minimum wage berkeley hourly | USD [[FACT:ca.local_minwage.berkeley.hourly=19.61]] | from 2026-07-01 |  | S15 | Employees working 2+ hours in Berkeley; the City Living Wage (20.01 / 23.33 from 2026-07-01) binds city contractors only and is not a general minimum. |
| Local minimum wage oakland hourly | USD [[FACT:ca.local_minwage.oakland.hourly=17.34]] | from 2026-01-01 |  | S16 | OMC ch. 5.92, employees working 2+ hours a week; 2027 rate not yet published on the city page. |
| Local minimum wage san francisco government supported hourly | USD [[FACT:ca.local_minwage.san_francisco.government_supported.hourly=17.35]] | from 2026-07-01 |  | S13 | Government Supported Employees rate (SF OLSE historical rates, 2026). |

## CA.3 Social insurance: unemployment, disability, paid leave and payroll levies

Employer: UI on wages up to USD [[FACT:ca.sui.wage_base=7,000]] plus the Employment Training Tax ([[FACT:ca.ett.rate=0.1]] %). Employee: State Disability Insurance (SDI, which funds disability and paid family leave) at [[FACT:ca.sdi.employee.rate=1.3]] % on all wages, with no wage cap ([[FACT:ca.sdi.wage_cap.exists=False]]). A voluntary plan replaces SDI where approved (W-2 box 14 label [[FACT:ca.sdi.voluntary_plan.w2_box14_label=VPDI]]).

```
ca_sdi = period_SDI_wages x ca_sdi_employee_rate          # no annual cap
```

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| SUI wage base | USD [[FACT:ca.sui.wage_base=7,000]] | from 2026-01-01 |  | S17 | Kept for 2027. |
| SUI new employer rate | [[FACT:ca.sui.new_employer.rate=3.4]] % | from 2026-01-01 |  | S18 | 2-3 years; range [[FACT:ca.sui.employer.rate.min=1.5]]%-[[FACT:ca.sui.employer.rate.max=6.2]]%; employer only; max [[FACT:ca.sui.max_per_employee=434]]/employee. |
| SUI employer rate min | [[FACT:ca.sui.employer.rate.min=1.5]] % | 2026-01-01 to 2026-12-31 |  | S19 |  |
| SUI employer rate max | [[FACT:ca.sui.employer.rate.max=6.2]] % | 2026-01-01 to 2026-12-31 |  | S19 |  |
| ETT rate | [[FACT:ca.ett.rate=0.1]] % | from 2026-01-01 |  | S20 | On first 7,000 (max 7/employee); same 2027. |
| SDI employee rate | [[FACT:ca.sdi.employee.rate=1.3]] % | 2026-01-01 to 2026-12-31 |  | S21 | Includes PFL; no wage cap since 2024-01-01 (SB 951); no employer share. 2027 rate: [[FACT:ca.sdi.employee.rate=1.4]] % (EDD Rates and Withholding page). |
| SDI employee rate | [[FACT:ca.sdi.employee.rate=1.4]] % | from 2027-01-01 |  | S21 | EDD Rates and Withholding page: 'The SDI withholding rate for 2027 is [[FACT:ca.sdi.employee.rate=1.4]] percent.' Includes PFL; no wage cap; no employer share. Second read on the EDD tax-rated-employers page 2026-11-06. |
| SDI wage cap exists | [[FACT:ca.sdi.wage_cap.exists=False]] | from 2024-01-01 |  | S21 |  |
| SDI voluntary plan W-2 box14 label | [[FACT:ca.sdi.voluntary_plan.w2_box14_label=VPDI]] | from 2026-01-01 |  | S22 |  |
| SDI benefit weekly max | USD [[FACT:ca.sdi.benefit.weekly_max=1,765]] | 2026-01-01 to 2026-12-31 |  | S23 | Maximum benefit 91,780 = [[FACT:ca.sdi.benefit.weekly_max=1,765]] x 52 (checked). |

## CA.4 Pay statement

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Payslip items | [[FACT:ca.payslip.items=gross wages; total hours (not salaried exempt); piece-rate units and rates; deductions; net wages; pay-period dates; employee name + last 4 SSN or employee ID; employer legal name and address; every hourly rate with hours]] | from 2026-01-01 |  | S24 | Lab. Code 226(a); semimonthly or with each payment; household excluded (226(d)); public employers only SSN rule (226(i)). |
| Payslip sick leave balance required | [[FACT:ca.payslip.sick_leave_balance.required=True]] | from 2026-01-01 |  | S25 | On the statement or a separate writing each payday (Lab. Code 246(i)). |
| Payslip inspection response days | [[FACT:ca.payslip.inspection_response_days=21]] days | from 2026-01-01 |  | S24 |  |
| Payslip penalty max | USD [[FACT:ca.payslip.penalty.max=4,000]] | from 2026-01-01 |  | S24 | 50 first / 100 subsequent per violation up to [[FACT:ca.payslip.penalty.max=4,000]]; 750 for failing an inspection request. |

## CA.5 Statutory reporting

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Registration de1 trigger | USD [[FACT:ca.registration.de1.trigger=100]] | from 2026-01-01 |  | S26 | DE 1 within 15 days after paying more than [[FACT:ca.registration.de1.trigger=100]] in wages in a quarter; DE 1P PIT-only. |
| Report deposit de88 | [[FACT:ca.report.deposit.de88=follows federal schedule: next-day if accumulated PIT > 400; semi-weekly; monthly by 15th if >= 350; quarterly if < 350; EFT by 3rd business day; 15% failure-to-deposit penalty]] | from 2026-01-01 |  | S26 |  |
| Report quarterly de9 DE 9C | [[FACT:ca.report.quarterly.de9_de9c=DE 9 + DE 9C electronic only, zero returns filed; due Apr 1/Jul 1/Oct 1/Jan 1, delinquent after Apr 30, Jul 31, Nov 2 2026, Feb 1 2027; DE 9C per employee subject wages, PIT wages, PIT withheld; corrections DE 9ADJ]] | from 2026-01-01 |  | S26 |  |
| Report W-2 filed with state | [[FACT:ca.report.w2.filed_with_state=False]] | from 2026-01-01 |  | S22 | W-2 to employees by 2027-02-01: box 14 CASDI, 16 CA PIT wages, 17 CA PIT withheld; not filed with EDD/FTB. No separate annual reconciliation. |
| Newhire report days | [[FACT:ca.newhire.report_days=20]] days | from 2026-01-01 |  | S22 | DE 34 from start-of-work date; rehire after separation of 60+ days; contractors DE 542 at 600+. |
| Report DE 9C file format | [[FACT:ca.report.de9c.file_format=Bulk DE 9C return file accepted as XML (App. B), ICESA (App. C/D no-payroll) or MMREF-1 (RE/RS/RST records); DE 8300 Rev. 12 (7-24), the edition published by EDD as of 2026-11-06.]] | from 2024-07-01 |  | S27 | |

## CA.6 Leave

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Leave sick accrual hours worked per hour | [[FACT:ca.leave.sick.accrual.hours_worked_per_hour=30]] hours | from 2024-01-01 |  | S25 | Lab. Code 246 (SB 616): eligible after [[FACT:ca.leave.sick.accrual.hours_worked_per_hour=30]] days; alternative 24 h by day 120 and 40 h by day 200; use from day 90; usage cap 40 h/5 days; balance cap 80 h/10 days; front-load 40 h; reinstated on rehire within 1 year; regular rate or 90-day average; increment max 2 h. |
| Leave sick usage cap hours | [[FACT:ca.leave.sick.usage_cap_hours=40]] hours | from 2024-01-01 |  | S25 |  |
| Leave sick accrual cap hours | [[FACT:ca.leave.sick.accrual_cap_hours=80]] hours | from 2024-01-01 |  | S25 |  |
| Leave sick payout on separation | [[FACT:ca.leave.sick.payout_on_separation=False]] | from 2024-01-01 |  | S25 |  |

## CA.7 Termination and final pay

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Final pay discharge | [[FACT:ca.final_pay.discharge=immediately (72 h for seasonal perishable-food layoffs); quit: within 72 h or last day with 72 h notice; waiting-time penalty 1 day wages per day up to 30 days]] | from 2026-01-01 |  | S28 |  |
| Final pay waiting time penalty max days | [[FACT:ca.final_pay.waiting_time_penalty_max_days=30]] days | from 2026-01-01 |  | S28 |  |
| Final pay vested vacation payout | [[FACT:ca.final_pay.vested_vacation_payout=True]] | from 2026-01-01 |  | S28 | Lab. Code 227.3: paid at final rate; forfeiture prohibited. |
| Separation notice | [[FACT:ca.separation_notice=CUIC 1089 Notice to Employee as to Change in Relationship + DE 2320 at discharge, layoff or leave; email only with opt-in]] | from 2026-01-01 |  | S22 |  |
| Warn notice days | [[FACT:ca.warn.notice_days=60]] days | from 2026-01-01 |  | S22 | Cal-WARN Lab. Code 1400-1408; 75-employee threshold not quoted (open). |
| Warn employer threshold | [[FACT:ca.warn.employer_threshold=Covered establishment = 75 or more persons employed (incl. within preceding 12 months); mass layoff = 50 or more employees in any 30-day period at a covered establishment]] | from 2023-01-01 |  | S29 | |

## CA.8 Benefits in kind and taxable wages

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| HSA conforms | [[FACT:ca.hsa.conforms=False]] | from 2026-01-01 |  | S30 | Employer and employee HSA contributions subject to UI/ETT, SDI and PIT (not UI/SDI via cafeteria plan); employer HSA (W-2 code W) added back for PIT. |
| Wages 401k deferrals | [[FACT:ca.wages.401k_deferrals=UI/SDI subject; PIT not subject]] | from 2026-01-01 |  | S30 |  |
| Wages GTL over 50k | [[FACT:ca.wages.gtl_over_50k=UI/SDI not subject; PIT not withheld but reportable]] | from 2026-01-01 |  | S30 |  |
| Obbba conforms | [[FACT:ca.obbba.conforms=False]] | from 2026-01-01 |  | S31 | No state tips or overtime deduction. |
| Meals value per day | USD [[FACT:ca.meals.value.per_day=15.85]] | 2026-01-01 to 2026-12-31 |  | S32 | Breakfast [[FACT:ca.meals.value.breakfast=3.25]], lunch 4.90, dinner 7.70, unidentified 5.70. |
| Meals value breakfast | USD [[FACT:ca.meals.value.breakfast=3.25]] | 2026-01-01 to 2026-12-31 |  | S32 |  |
| Meals value lunch | USD [[FACT:ca.meals.value.lunch=4.90]] | 2026-01-01 to 2026-12-31 |  | S32 |  |
| Meals value dinner | USD [[FACT:ca.meals.value.dinner=7.70]] | 2026-01-01 to 2026-12-31 |  | S32 |  |
| Lodging value min weekly | USD [[FACT:ca.lodging.value.min_weekly=66.10]] | 2026-01-01 to 2026-12-31 |  | S32 | 66 2/3% of rental value, min [[FACT:ca.lodging.value.min_weekly=66.10]]/week, max [[FACT:ca.lodging.value.max_monthly=2,038]]/month. |
| Lodging value max monthly | USD [[FACT:ca.lodging.value.max_monthly=2,038]] | 2026-01-01 to 2026-12-31 |  | S32 |  |
| HSA conformity 2026 | [[FACT:ca.hsa.conformity_2026=Not enacted: AB 781 (DeMaio) is an Inactive Bill - Died 2026-01-31 pursuant to Art. IV Sec 10(c); hearing canceled 2025-04-21. No other enacted HSA-conformity act was located (only this bill checked); FTB 2026 Schedule CA instructions not verified. Level: assessment]] | historical source, not confirmed in force (dated 2026-01-31) |  | S33 | |

## CA.9 Deductions and garnishments

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Garnishment creditor max percent | [[FACT:ca.garn.creditor.max_percent=20]] % | from 2026-01-01 |  | S34 | WG-002 Rev. 2026-01-01: lesser of [[FACT:ca.garn.creditor.max_percent=20]] % of disposable earnings or 40% of disposable earnings above minimum wage x 48 (weekly) / 96 (biweekly) / 104 (semimonthly) / 208 (monthly); local MW if higher; support first. |
| Garnishment creditor excess percent | [[FACT:ca.garn.creditor.excess_percent=40]] % | from 2026-01-01 |  | S34 |  |
| Garnishment creditor minimum wage multiple weekly | [[FACT:ca.garn.creditor.minwage_multiple.weekly=48]] ratio | from 2026-01-01 |  | S34 |  |
| Garnishment child support cap percent | [[FACT:ca.garn.child_support.cap_percent=50]] % | from 2026-01-01 |  | S35 | [[FACT:ca.garn.child_support.cap_percent=50]] % after taxes; remit to SDU within 7 business days of pay date electronically (Fam. Code 17309.5); IWO kept 1 year after separation. |
| Garnishment child support remit business days | [[FACT:ca.garn.child_support.remit_business_days=7]] business days | from 2026-01-01 |  | S35 |  |
| Deductions tip credit allowed | [[FACT:ca.deductions.tip_credit.allowed=False]] | from 2026-01-01 |  | S36 | Lab. Code 224, 351: deductions only if required by law or authorised in writing; no tip credit; card tips without processing fees. |
| Garnishment child support employer fee | [[FACT:ca.garn.child_support.employer_fee=Employer may deduct 1.50 USD per payment made under the order; SDU remittance once operational; substitution of payee forwarded within 10 days]] | from 2005-01-01 |  | S37 | |

## CA.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Prevailing wage certified payroll | [[FACT:ca.prevailing_wage.certified_payroll=electronic to Labor Commissioner via DIR eCPR (XML upload spec available)]] | from 2026-01-01 |  | S38 | [partial row] |
| Prevailing wage thresholds | [[FACT:ca.prevailing_wage.thresholds=DIR contractor registration not required for public works projects of 25,000 USD or less (construction/alteration/demolition/installation/repair) or 15,000 USD or less (maintenance); registration/renewal fee up to 800 USD set by DIR]] | from 2026-07-01 |  | S39 | Text of LAB 1725.5 operative from 2026-07-01; the version in force before that date is not covered by this source. |

## CA.11 Indexation

The minimum wage is CPI-indexed (the Department of Finance certifies by 1 August, Lab. Code 1182.12(d)); the exempt-salary threshold follows the minimum wage by statutory multiple; the PIT tables are indexed yearly in DE 44; the UI base is fixed in statute (USD [[FACT:ca.sui.wage_base=7,000]]); the SDI rate is set yearly; meal and lodging values are set yearly.

## CA.12 Payroll data protection and records

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Records wage statement retention years | [[FACT:ca.records.wage_statement.retention_years=3]] years | from 2026-01-01 |  | S24 |  |
| Records edd payroll retention years | [[FACT:ca.records.edd_payroll.retention_years=4]] years | from 2026-01-01 |  | S32 | 8 years for non-employee payments. |
| CCPA request response days | [[FACT:ca.ccpa.request_response_days=45]] days | from 2023-01-01 |  | S40 | Extendable to 90; employee data in scope since 2023-01-01 (A.3). |

## CA.13 Live legal change

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Live ab1514 manicurists | [[FACT:ca.live.ab1514_manicurists=Borello test reinstated for licensed manicurists 2026-01-01 to 2028-12-31; commercial-fisher exception extended]] | 2026-01-01 to 2028-12-31 |  | S17 |  |
| Delinquent tax interest rate | [[FACT:ca.delinquent_tax.interest_rate=7]] % | 2026-01-01 to 2026-12-31 |  | S17 |  |
| Special populations UI coverage thresholds | [[FACT:ca.special_populations.ui_coverage_thresholds=General employer: 1+ employee and wages over 100 USD in any calendar quarter (current or preceding year); domestic service in private home/college club: cash wages of 1,000 USD or more in any quarter (current or preceding year). Agricultural (UIC 678) and nonprofit thresholds not verified]] | from 2006-01-01 |  | S41 | |

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
| Monthly withholding | 86.00 / 12 | USD [[FACT:ca.oracle.de44_f.monthly.withholding=7.17]] |

The computed monthly withholding equals the published value. Example E (semi-monthly) published value: USD [[FACT:ca.oracle.de44.example_e.withholding_semimonthly=4.13]]; its inputs are not keyed, so it is reproduced in Module 12 rather than here.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Oracle DE 44 f monthly withholding | USD [[FACT:ca.oracle.de44_f.monthly.withholding=7.17]] | 2026-01-01 to 2026-12-31 |  | S8 | DE 44 Method B example F: annual 57,000 married 4 allowances; 57,000 - [[FACT:ca.wh.std_deduction.married_2plus_hoh=11,412]] = 45,588 -> [[FACT:ca.pit.bracket.married.2.base=243.74]] + [[FACT:ca.pit.bracket.single.2.rate=2.2]] % x 23,430 = 759.20 - 673.20 = 86.00/yr = [[FACT:ca.oracle.de44_f.monthly.withholding=7.17]]/month. Recomputed |
| Oracle DE 44 example e withholding semimonthly | USD [[FACT:ca.oracle.de44.example_e.withholding_semimonthly=4.13]] | 2026-01-01 to 2026-12-31 |  | S8 | DE 44 Method B example E, Recomputed Single cumulative bases also re-derive (121.87... 114,220.27); 34,084.81 derives as 34,084.80 (intermediate rounding residual 0.01). |
| Oracle suite | [[FACT:ca.oracle.suite=DE 44 Rev. 52 (4-26) Method B examples A-F]] | 2026-01-01 to 2026-12-31 |  | S8 |  |

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



## CA.16 Language

The Lab. Code 2810.5 hire notice must be in the language the employer normally uses with the employee; the payslip is in English.

## CA.S Sources

| Ref | Instrument | Article / section | Authority |
|---|---|---|---|
| S1 | DIR Labor Commissioner FAQ Minimum Wage (MW-2026), Wayback 2026-10-31 | Minimum Wage Order MW-2026; Labor Code 1182.12 | California Department of Industrial Relations / Labor Commissioner |
| S2 | DIR News 2026-66 (ICYMI) and Governor press release 2026-07-31: statewide minimum wage [[FACT:ca.minwage.hourly=17.40]] from 2027-01-01 | Labor Code 1182.12(d) annual CPI adjustment, DOF certification 2026-07-31 | California DIR Labor Commissioner; Office of the Governor (DOF certification … |
| S3 | California Labor Code section 510 (daily and weekly overtime), leginfo via Wayback 2026-01-02 | Lab. Code 510(a); amended Stats. 1999 ch.134 | California Legislative Counsel |
| S4 | California Labor Code section 204 (paydays) and 213(d) (direct deposit by voluntary authorization), leginfo via Wayback | Lab. Code 204 (amended Stats. 2019 ch.508, SB 698, eff. 2020-01-01; snapshot 2026-08-31); Lab. Code 213(d) (amended Stats. 2005 ch.149; snapshot 2022-10-15) | California Legislative Counsel |
| S5 | DIR Minimum Wage page and Fast Food Minimum Wage FAQ (Lab. Code 1474 / AB 1228) | Minimum Wage page; Fast Food FAQ 'When does the minimum wage increase in AB 1228 take effect?' | California Department of Industrial Relations - Labor Commissioner |
| S6 | DIR Labor Commissioner - Health Care Worker Minimum Wage FAQ (Lab. Code 1182.14-1182.16; SB 525, SB 828, SB 159) | FAQ 1-2 schedule table | California Department of Industrial Relations - Labor Commissioner |
| S7 | Labor Code 860 agricultural overtime phase-in (AB 1066) | LAB 860(a)-(d) | California Legislative Counsel (leginfo.legislature.ca.gov) |
| S8 | EDD DE 44 California Employer Guide 2026 (Rev. 52 4-26): Method B Exact Calculation tables 1-28 and worked examples A-F | DE 44 pp.20, 43-51 (PDF pp.53-60): Method B Tables 1-10 | California Employment Development Department (EDD); tables prepared with … |
| S9 | EDD DE 4 Employee's Withholding Allowance Certificate (Rev. 56 1-26) | DE 4 Rev. 56 (1-26) | California EDD |
| S10 | EDD DE 44 2026: DE 4 rules, supplemental wages, residents/nonresidents withholding | DE 44 pp.16-19 | California EDD |
| S11 | City of Los Angeles Office of Wage Standards - Minimum Wage Ordinance rates | Minimum Wage chart (All Employers) | City of Los Angeles, Bureau of Contract Administration, Office of Wage Standards |
| S12 | Los Angeles County DCBA - Minimum Wage (County Code 8.100.040) notice | Notice under County Code 8.100.040 | Los Angeles County Department of Consumer and Business Affairs / Chief … |
| S13 | San Francisco OLSE - Minimum Wage Ordinance page and Historical San Francisco Minimum Wage Rates (2026) | Minimum wage; historical rates PDF | City and County of San Francisco, Office of Labor Standards Enforcement |
| S14 | City of San Diego OLSE - Minimum Wage Historical Rates (09.2026) | San Diego Municipal Code ch. 3 art. 9 div. 1; rate table | City of San Diego, Office of Labor Standards and Enforcement |
| S15 | City of Berkeley - Workforce Standards and Enforcement (Minimum Wage Ordinance) | Minimum wage posters | City of Berkeley |
| S16 | City of Oakland Workplace and Employment Standards - Oakland Minimum Wage, Sick Leave and Other Labor Laws (OMC ch. 5.92) | City Minimum Wage | City of Oakland, Department of Workplace and Employment Standards |
| S17 | EDD California Employer News and Updates (page read 2026-11-02) | News items Nov 2025 - Oct 2026 | California EDD |
| S18 | California DE 44 Employer Guide 2026 (Rev. 52 4-26): PIT withholding, nonresident, no local wage tax | DE 44 p.17 (PIT), p.18 (supplemental), p.27 (nonresidents) | California EDD |
| S19 | UI Schedule F+ emergency surcharge (15% on Schedule F) | EDD UI rate for 2026 | CA official authority |
| S20 | Employment Training Tax (ETT) | CA UI Code (ETT) | CA official authority |
| S21 | State Disability Insurance (SDI incl. PFL) | SB 951; DE 44 | CA official authority |
| S22 | EDD DE 44 2026: Form W-2 state boxes, no state W-2 filing, DE 9C content, new-hire DE 34 fields, WARN, UI reciprocal coverage | DE 44 pp.56-57, 65, 70-71, 73, 79 | California EDD |
| S23 | EDD DI Contribution Rates and Benefit Amounts (2026) | 2026 Voluntary Plan table | California EDD |
| S24 | California Labor Code section 226 (itemized wage statement), leginfo text via Wayback 2026-08-31 | Lab. Code 226(a)-(j); amended Stats. 2023 ch.866 (SB 332) eff. 2023-10-13 | California Legislative Counsel (leginfo.legislature.ca.gov) |
| S25 | California Labor Code section 246 (paid sick leave), leginfo via Wayback 2025-01-23 | Lab. Code 246(a)-(l) as amended by SB 616 (2023), operative 2024-01-01 | California Legislative Counsel |
| S26 | EDD DE 44 2026: Forms and Due Dates, California Deposit Requirements, DE 9/DE 9C due dates, registration, new hire DE 34, DE 542 | DE 44 p.5 (PDF p.13), pp.56-66 | California EDD |
| S27 | EDD DE 8300 Electronic Filing Guide for the Quarterly Wage and Withholding Program (Rev. 12, 7-24) | Appendices B, C, D, E/F (TOC) | California EDD |
| S28 | California Labor Code sections 201, 202, 203 (final pay and waiting-time penalty) and 227.3 (vested vacation payout), leginfo via Wayback 2025 | Lab. Code 201(a) (Stats. 2018 ch.903); 202(a) (Stats. 2018 ch.903); 203(a) (Stats. 2019 ch.700, SB 286); 227.3 (Stats. 1976 ch.1041) | California Legislative Counsel |
| S29 | Labor Code 1400.5 Cal/WARN definitions | LAB 1400.5(a),(d) | California Legislative Counsel (leginfo.legislature.ca.gov) |
| S30 | EDD Information Sheet DE 231EB Taxability of Employee Benefits (Rev. 12 6-17) | DE 231EB pp.2-4 (UI/ETT, SDI, PIT withholding columns) | California EDD |
| S31 | FTB 2025 Instructions for Schedule CA (540), revised 04/2026: HSA nonconformity and OBBBA nonconformity | Line 1h (employer HSA contribution, W-2 box 12 code W), line 13; Federal Tax Changes under OBBBA | California Franchise Tax Board |
| S32 | EDD DE 44 2026: Meals and lodging values; subject wages vs PIT wages; recordkeeping | DE 44 pp.12, 14-15 | California EDD |
| S33 | AB 781 (2025-26) HSA conformity bill status | AB 781 status/history | California Legislative Counsel (leginfo.legislature.ca.gov) |
| S34 | Judicial Council of California form WG-002 Earnings Withholding Order (Rev. January 1, 2026), employer computation instructions (CCP 706.050) | WG-002 page 1, Instructions to Employer (A)-(C), Steps 1-5 | Judicial Council of California |
| S35 | California Child Support Services PUB 307 California Employers and the SDU (06/2026) and IWO Employer Fact Sheet (09/2019) | PUB 307 (2026-06-22); IWO Fact Sheet; Family Code 17309.5 | California Department of Child Support Services |
| S36 | California Labor Code section 224 (authorised deductions) and 351 (gratuities), leginfo via Wayback 2025 | Lab. Code 224 (Stats. 1968 ch.559); Lab. Code 351 (Stats. 2000 ch.876) | California Legislative Counsel |
| S37 | Family Code 5235(d) employer fee on earnings assignment order | FAM 5235(a)-(e) | California Legislative Counsel (leginfo.legislature.ca.gov) |
| S38 | DIR Certified Payroll Reports page (Public Works), Wayback 2026 | Lab. Code 1776 (CPR); eCPR XML guidelines | California DIR / Labor Commissioner |
| S39 | Labor Code 1725.5(f) public works registration de minimis thresholds | LAB 1725.5(f) | California Legislative Counsel (leginfo.legislature.ca.gov) |
| S40 | California Privacy Protection Agency FAQ (CCPA as amended by CPRA): employee and job applicant data | FAQ: consumers include employees and job applicants; Civil Code 1798.145(m)-(n) exemptions expired 2022-12-31 | California Privacy Protection Agency |
| S41 | UIC s.675 and s.682 CA UI employer thresholds (general, domestic) | UIC s.675; UIC s.682(a) | California Legislative Counsel (leginfo.legislature.ca.gov) |

# Annex NY: New York


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T3 - state withholding; local layer absent or piggybacked on the state return** (build manifest, tier rationale). NYC and Yonkers taxes are piggybacked on NYS-1 / NYS-45 [US-NY-008].

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## NY.1 Employment and labour code

- **Minimum wage (Labor Law 652(1-a)) [US-NYS5-002].** Two regions in 2026: New York City, Nassau, Suffolk and Westchester at [[FACT:ny.labour.minwage.nyc_li_westchester.hourly=17.00]] USD per hour; the rest of the state at [[FACT:ny.labour.minwage.rest_of_state.hourly=16.00]] USD per hour. No municipal minimum-wage ordinance applies: the regions are set by the state law itself.
- **2027.** No increase on 2027-01-01: [[FACT:ny.labour.minwage.next_year_change=none on 2027-01-01 (off-ramp met)]] [US-NYS5-001]. Home care aides from 2027-01-01: [[FACT:ny.labour.minwage.home_care_aide.nyc_li_westchester.hourly=20.00]] USD (NYC, Long Island, Westchester) and [[FACT:ny.labour.minwage.home_care_aide.rest_of_state.hourly=19.00]] USD (rest of state). A proposal to change the off-ramps is not enacted and is not modelled.
- **Overtime (12 NYCRR 142-2.2) [US-NYS5-011].** [[FACT:ny.overtime.premium.multiplier=1.5]] times the regular rate after [[FACT:ny.overtime.weekly_threshold_hours=40]] hours per week; residential employees have a higher weekly threshold (state rule, not modelled as a separate value here). FLSA 13(a)(2)/(4) exemptions are not applied in New York; FLSA-exempt employees other than executive, administrative and professional staff receive overtime at the premium multiple of the minimum rate.
- **Call-in pay and spread of hours.** Call-in pay of [[FACT:ny.labour.call_in_pay.hours=4]] hours, or the scheduled shift if shorter. Where the spread of hours exceeds [[FACT:ny.labour.spread_of_hours.threshold_hours=10]] hours, or on a split shift, one extra hour at the minimum rate is due [US-NYS5-011].
- **Exempt salary thresholds from 2026-01-01** (executive and administrative): [[FACT:ny.labour.exempt_salary.nyc_li_westchester.weekly=1,275.00]] USD per week in NYC, Long Island and Westchester; [[FACT:ny.labour.exempt_salary.rest_of_state.weekly=1,199.10]] USD per week in the rest of the state [US-NYS5-011].
- **Farm workers.** Overtime after [[FACT:ny.labour.overtime.farm.threshold_hours=52]] hours per week from 2026-01-01; the threshold steps down in later years under the phase-in [US-NYS5-012]. Domestic workers: overtime threshold per US-NYS5-013 (higher for live-in workers).
- **Pay frequency (Labor Law 191) [US-NYS5-003].** Manual workers: [[FACT:ny.labour.pay_frequency.manual=weekly, max 7 days after week end]]; semi-monthly only with commissioner authorisation or for nonprofits. Clerical and other workers: at least semi-monthly on regular paydays fixed in advance. Commission salespersons: at least monthly under a written agreement. Damages for a first manual-worker frequency violation are limited to lost interest where pay was at least semi-monthly (198, revision of 2025-05-16) [US-NYS5-021].
- **Method of payment (192).** Direct deposit requires the employee's advance written consent (consent required: [[FACT:ny.labour.direct_deposit.consent_required=True]]); higher-paid executive, administrative and professional staff and farm workers are exempt from the consent rule [US-NYS5-004]. Deposit consent and pay cards: [[FACT:ny.labour.paycard=No employer may deposit net wage in a bank/financial institution without the employee's advance written consent (exempt: executive/admin/professional earning over 1,300 USD/week; farm workers). 12 NYCRR Part 192 (paycard rules) NOT read]] [US-NYV6-005].
- **Tipped employees (hospitality only) [US-NYS5-001].** Minimum cash wage, service employees: [[FACT:ny.labour.tip_credit.service.nyc_li_westchester.cash_wage=14.15]] USD (NYC/LI/Westchester), [[FACT:ny.labour.tip_credit.service.rest_of_state.cash_wage=13.30]] USD (rest of state). Food-service workers: [[FACT:ny.labour.tip_credit.food_service.nyc_li_westchester.cash_wage=11.35]] USD and [[FACT:ny.labour.tip_credit.food_service.rest_of_state.cash_wage=10.70]] USD. The tip credit is the regional minimum wage minus the cash wage.
- **Meal credit toward the minimum wage:** [[FACT:ny.labour.meal_credit.nyc_li_westchester.per_meal=5.80]] USD per meal in NYC/LI/Westchester [US-NYS5-011]. Lodging and uniform-maintenance credits for 2026 are listed in Minimum Wage Order Part 142 (US-NYS5-011); they are not carried as facts and are not modelled.

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.labour.minwage.nyc_li_westchester.hourly` | [[FACT:ny.labour.minwage.nyc_li_westchester.hourly=17.00]] | USD | from 2026-01-01 | US-NYS5-002 | Labor Law 652(1-a); 2027 frozen by off-ramp (US-NYS5-001) |
| `ny.labour.minwage.rest_of_state.hourly` | [[FACT:ny.labour.minwage.rest_of_state.hourly=16.00]] | USD | from 2026-01-01 | US-NYS5-002 | 2027 frozen by off-ramp |
| `ny.labour.minwage.next_year_change` | [[FACT:ny.labour.minwage.next_year_change=none on 2027-01-01 (off-ramp met)]] |  | from 2027-01-01 | US-NYS5-001 | DOL statement |
| `ny.labour.minwage.home_care_aide.nyc_li_westchester.hourly` | [[FACT:ny.labour.minwage.home_care_aide.nyc_li_westchester.hourly=20.00]] | USD | from 2027-01-01 | US-NYS5-001 |  |
| `ny.labour.minwage.home_care_aide.rest_of_state.hourly` | [[FACT:ny.labour.minwage.home_care_aide.rest_of_state.hourly=19.00]] | USD | from 2027-01-01 | US-NYS5-001 |  |
| `ny.overtime.weekly_threshold_hours` | [[FACT:ny.overtime.weekly_threshold_hours=40]] | hours | from 2026-01-01 | US-NYS5-011 | 44 for residential employees; FLSA-exempt non-EAP get 1.5x minimum |
| `ny.overtime.premium.multiplier` | [[FACT:ny.overtime.premium.multiplier=1.5]] | ratio | from 2026-01-01 | US-NYS5-011 |  |
| `ny.labour.call_in_pay.hours` | [[FACT:ny.labour.call_in_pay.hours=4]] | hours | from 2026-01-01 | US-NYS5-011 | or scheduled shift if shorter |
| `ny.labour.spread_of_hours.threshold_hours` | [[FACT:ny.labour.spread_of_hours.threshold_hours=10]] | hours | from 2026-01-01 | US-NYS5-011 | +1 h at minimum rate (also split shift) |
| `ny.labour.exempt_salary.nyc_li_westchester.weekly` | [[FACT:ny.labour.exempt_salary.nyc_li_westchester.weekly=1,275.00]] | USD | from 2026-01-01 | US-NYS5-011 | exec/admin |
| `ny.labour.exempt_salary.rest_of_state.weekly` | [[FACT:ny.labour.exempt_salary.rest_of_state.weekly=1,199.10]] | USD | from 2026-01-01 | US-NYS5-011 |  |
| `ny.labour.overtime.farm.threshold_hours` | [[FACT:ny.labour.overtime.farm.threshold_hours=52]] | hours | 2026-01-01 to 2027-12-31 | US-NYS5-012 | 48 (2028), 44 (2030), 40 (2032) |
| `ny.labour.pay_frequency.manual` | [[FACT:ny.labour.pay_frequency.manual=weekly, max 7 days after week end]] |  | from 2026-01-01 | US-NYS5-003 | semi-monthly only with authorisation or nonprofits; clerical at least semi-monthly |
| `ny.labour.direct_deposit.consent_required` | [[FACT:ny.labour.direct_deposit.consent_required=True]] |  | from 2026-01-01 | US-NYS5-004 | exempt: EAP over 1,300/week and farm workers |
| `ny.labour.tip_credit.service.nyc_li_westchester.cash_wage` | [[FACT:ny.labour.tip_credit.service.nyc_li_westchester.cash_wage=14.15]] | USD | from 2026-01-01 | US-NYS5-001 |  |
| `ny.labour.tip_credit.service.rest_of_state.cash_wage` | [[FACT:ny.labour.tip_credit.service.rest_of_state.cash_wage=13.30]] | USD | from 2026-01-01 | US-NYS5-001 | tip credit 2.70 |
| `ny.labour.tip_credit.food_service.nyc_li_westchester.cash_wage` | [[FACT:ny.labour.tip_credit.food_service.nyc_li_westchester.cash_wage=11.35]] | USD | from 2026-01-01 | US-NYS5-001 |  |
| `ny.labour.tip_credit.food_service.rest_of_state.cash_wage` | [[FACT:ny.labour.tip_credit.food_service.rest_of_state.cash_wage=10.70]] | USD | from 2026-01-01 | US-NYS5-001 | tip credit 5.30 |
| `ny.labour.meal_credit.nyc_li_westchester.per_meal` | [[FACT:ny.labour.meal_credit.nyc_li_westchester.per_meal=5.80]] | USD | from 2026-01-01 | US-NYS5-011 |  |
| `ny.labour.paycard` | [[FACT:ny.labour.paycard=No employer may deposit net wage in a bank/financial institution without the employee's advance written consent (exempt: executive/admin/professional earning over 1,300 USD/week; farm workers). 12 NYCRR Part 192 (paycard rules) NOT read]] |  | from 2026-01-01 | US-NYV6-005 | Register: US-NYV6-005 |

## NY.2 Income tax withholding

- **Withholding method [US-NY-001].** [[FACT:ny.wh.method=NYS-50-T-NYS (1/26): Method I tables, Method II exact calculation, Method III top income]]. Method III (top income) applies when annualised net wages reach [[FACT:ny.pit.top_income.threshold.annual=1,077,550]] USD.
- **Withholding schedules are not statutory brackets.** The Method II rate schedules (single and married, with recapture bands) are withholding schedules published in NYS-50-T-NYS; the build uses the publication's tables and formula, never the statutory brackets of Tax Law 601. The WTC references NYS-50-T-NYS only.
- **Certificate [US-NYS5-010].** [[FACT:ny.wh.certificate=IT-2104; 2020+ W-4 without IT-2104 = zero allowances]]. An exempt certificate is available under Tax Law 671(a)(3) (minors, older employees and full-time students with no liability).
- **Exemption allowance:** [[FACT:ny.pit.exemption.annual=1000]] USD per year per allowance [US-NY-001].
- **Supplemental wages.** New York State supplemental rate [[FACT:ny.pit.supplemental.nys.rate=11.7]] %, or the aggregate method [US-NY-001, US-NYS5-010]. Local supplemental rates (method (a); or the aggregate method): New York City [[FACT:ny.local.nyc.supplemental.rate=4.25]] %, Yonkers resident [[FACT:ny.local.yonkers.resident.supplemental.rate=1.95975]] %, Yonkers nonresident [[FACT:ny.local.yonkers.nonresident.supplemental.rate=0.5]] % [US-NYB5-301, US-NYB5-302].
- **Rounding:** [[FACT:ny.pit.rounding=to the cent per tables or formula]] [US-NY-001]. Oracle (NYS-50-T-NYS Method II worked examples): example 1 = [[FACT:ny.pit.oracle.example_1.withholding=8.01]] USD; example 3 = [[FACT:ny.pit.oracle.example_3.withholding=3,576.63]] USD; example 4 = [[FACT:ny.pit.oracle.example_4.withholding=44.10]] USD, all reproduced exactly. Example 2 is printed as [[FACT:ny.pit.oracle.example_2.withholding=258.51]] USD; half-up rounding gives one cent less (open point below). Recomputation of the examples belongs to Module 12 and the validation suite.
- **Method II exact calculation, New York State [US-NYV7-001].** [[FACT:ny.wh.method2.annualisation=Method II: net wages = wages - Table A allowance for the payroll period; apply the per-period table (weekly/biweekly/semimonthly/monthly/daily) or the Annual Tax Rate Schedule for annual payrolls: (net - col3) x col4 + col5. Annualised net wages (net x payroll periods) are used only to test the Method III threshold. Other periods: convert via a factor to a common period, apply its table, convert the result back (p.23).]] Allowances: deduction allowance [[FACT:ny.wh.method2.single.deduction_allowance=7400]] USD (single) or [[FACT:ny.wh.method2.married.deduction_allowance=7950]] USD (married) per year, plus [[FACT:ny.wh.method2.exemption_allowance=1000]] USD per year for each exemption claimed (Tables A and B; per-period amounts are printed in the publication). Annual Tax Rate Schedules (Table C), applied as (net wages - column 3) x column 4 + column 5:

**NYS Method II annual schedule, single**

| Line | Net wages at least (column 3) | Rate (column 4) | Add (column 5) |
|---|---|---|---|
| 1 | USD [[FACT:ny.wh.method2.single.bracket.1.floor=0]] | [[FACT:ny.wh.method2.single.bracket.1.rate=3.9]] % | USD [[FACT:ny.wh.method2.single.bracket.1.base=0]] |
| 2 | USD [[FACT:ny.wh.method2.single.bracket.2.floor=8500]] | [[FACT:ny.wh.method2.single.bracket.2.rate=4.4]] % | USD [[FACT:ny.wh.method2.single.bracket.2.base=332]] |
| 3 | USD [[FACT:ny.wh.method2.single.bracket.3.floor=11,700]] | [[FACT:ny.wh.method2.single.bracket.3.rate=5.15]] % | USD [[FACT:ny.wh.method2.single.bracket.3.base=472]] |
| 4 | USD [[FACT:ny.wh.method2.single.bracket.4.floor=13,900]] | [[FACT:ny.wh.method2.single.bracket.4.rate=5.4]] % | USD [[FACT:ny.wh.method2.single.bracket.4.base=586]] |
| 5 | USD [[FACT:ny.wh.method2.single.bracket.5.floor=80,650]] | [[FACT:ny.wh.method2.single.bracket.5.rate=5.9]] % | USD [[FACT:ny.wh.method2.single.bracket.5.base=4190]] |
| 6 | USD [[FACT:ny.wh.method2.single.bracket.6.floor=96,800]] | [[FACT:ny.wh.method2.single.bracket.6.rate=7.03]] % | USD [[FACT:ny.wh.method2.single.bracket.6.base=5143]] |
| 7 | USD [[FACT:ny.wh.method2.single.bracket.7.floor=107,650]] | [[FACT:ny.wh.method2.single.bracket.7.rate=7.53]] % | USD [[FACT:ny.wh.method2.single.bracket.7.base=5906]] |
| 8 | USD [[FACT:ny.wh.method2.single.bracket.8.floor=157,650]] | [[FACT:ny.wh.method2.single.bracket.8.rate=6.4]] % | USD [[FACT:ny.wh.method2.single.bracket.8.base=9673]] |
| 9 | USD [[FACT:ny.wh.method2.single.bracket.9.floor=215,400]] | [[FACT:ny.wh.method2.single.bracket.9.rate=11.44]] % | USD [[FACT:ny.wh.method2.single.bracket.9.base=13,369]] |
| 10 | USD [[FACT:ny.wh.method2.single.bracket.10.floor=265,400]] | [[FACT:ny.wh.method2.single.bracket.10.rate=7.35]] % | USD [[FACT:ny.wh.method2.single.bracket.10.base=19,091]] |

**NYS Method II annual schedule, married**

| Line | Net wages at least (column 3) | Rate (column 4) | Add (column 5) |
|---|---|---|---|
| 1 | USD [[FACT:ny.wh.method2.married.bracket.1.floor=0]] | [[FACT:ny.wh.method2.married.bracket.1.rate=3.9]] % | USD [[FACT:ny.wh.method2.married.bracket.1.base=0]] |
| 2 | USD [[FACT:ny.wh.method2.married.bracket.2.floor=8500]] | [[FACT:ny.wh.method2.married.bracket.2.rate=4.4]] % | USD [[FACT:ny.wh.method2.married.bracket.2.base=332]] |
| 3 | USD [[FACT:ny.wh.method2.married.bracket.3.floor=11,700]] | [[FACT:ny.wh.method2.married.bracket.3.rate=5.15]] % | USD [[FACT:ny.wh.method2.married.bracket.3.base=472]] |
| 4 | USD [[FACT:ny.wh.method2.married.bracket.4.floor=13,900]] | [[FACT:ny.wh.method2.married.bracket.4.rate=5.4]] % | USD [[FACT:ny.wh.method2.married.bracket.4.base=586]] |
| 5 | USD [[FACT:ny.wh.method2.married.bracket.5.floor=80,650]] | [[FACT:ny.wh.method2.married.bracket.5.rate=5.9]] % | USD [[FACT:ny.wh.method2.married.bracket.5.base=4190]] |
| 6 | USD [[FACT:ny.wh.method2.married.bracket.6.floor=96,800]] | [[FACT:ny.wh.method2.married.bracket.6.rate=6.57]] % | USD [[FACT:ny.wh.method2.married.bracket.6.base=5143]] |
| 7 | USD [[FACT:ny.wh.method2.married.bracket.7.floor=107,650]] | [[FACT:ny.wh.method2.married.bracket.7.rate=7.07]] % | USD [[FACT:ny.wh.method2.married.bracket.7.base=5855]] |
| 8 | USD [[FACT:ny.wh.method2.married.bracket.8.floor=157,650]] | [[FACT:ny.wh.method2.married.bracket.8.rate=8.01]] % | USD [[FACT:ny.wh.method2.married.bracket.8.base=9388]] |
| 9 | USD [[FACT:ny.wh.method2.married.bracket.9.floor=211,550]] | [[FACT:ny.wh.method2.married.bracket.9.rate=6.4]] % | USD [[FACT:ny.wh.method2.married.bracket.9.base=13,708]] |
| 10 | USD [[FACT:ny.wh.method2.married.bracket.10.floor=323,200]] | [[FACT:ny.wh.method2.married.bracket.10.rate=13.49]] % | USD [[FACT:ny.wh.method2.married.bracket.10.base=20,854]] |
| 11 | USD [[FACT:ny.wh.method2.married.bracket.11.floor=373,200]] | [[FACT:ny.wh.method2.married.bracket.11.rate=7.35]] % | USD [[FACT:ny.wh.method2.married.bracket.11.base=27,600]] |
| 12 | USD [[FACT:ny.wh.method2.married.bracket.12.floor=1,077,550]] | [[FACT:ny.wh.method2.married.bracket.12.rate=7.65]] % | USD [[FACT:ny.wh.method2.married.bracket.12.base=79,369]] |

- **Method III, top income [US-NYV7-001].** [[FACT:ny.wh.method3.annualisation=Method III: annualized wages = Method II net wages x payroll periods per year (e.g. 52, 26, 24, 12); x column 3 rate; / payroll periods = amount to withhold.]] Method III applies when annualised Method II net wages are at least [[FACT:ny.wh.method3.single.threshold=1,077,550]] USD (single) or [[FACT:ny.wh.method3.married.threshold=2,155,350]] USD (married). Rates (column 3):

| Status | Annualised net wages at least | Rate |
|---|---|---|
| Single | USD [[FACT:ny.wh.method3.single.bracket.1.floor=1,077,550]] | [[FACT:ny.wh.method3.single.bracket.1.rate=10.45]] % |
| Single | USD [[FACT:ny.wh.method3.single.bracket.2.floor=5,000,000]] | [[FACT:ny.wh.method3.single.bracket.2.rate=11.1]] % |
| Single | USD [[FACT:ny.wh.method3.single.bracket.3.floor=25,000,000]] | [[FACT:ny.wh.method3.single.bracket.3.rate=11.7]] % |
| Married | USD [[FACT:ny.wh.method3.married.bracket.1.floor=2,155,350]] | [[FACT:ny.wh.method3.married.bracket.1.rate=10.45]] % |
| Married | USD [[FACT:ny.wh.method3.married.bracket.2.floor=5,000,000]] | [[FACT:ny.wh.method3.married.bracket.2.rate=11.1]] % |
| Married | USD [[FACT:ny.wh.method3.married.bracket.3.floor=25,000,000]] | [[FACT:ny.wh.method3.married.bracket.3.rate=11.7]] % |

- **New York City resident withholding, Method II [US-NYV7-002].** [[FACT:ny.local.nyc.method2.annualisation=Same steps as NYS Method II with the NYC Tables A-C and NYC schedules; NYC has no Method III and no top-income switch (top line 60,000 and over at 0.0425).]] Allowances: [[FACT:ny.local.nyc.method2.single.deduction_allowance=5000]] USD (single) or [[FACT:ny.local.nyc.method2.married.deduction_allowance=5500]] USD (married) per year, plus [[FACT:ny.local.nyc.method2.exemption_allowance=1000]] USD per exemption. NYC annual schedules, same formula:

| Line | Single: net wages at least | Single: rate | Single: add | Married: net wages at least | Married: rate | Married: add |
|---|---|---|---|---|---|---|
| 1 | USD [[FACT:ny.local.nyc.method2.single.bracket.1.floor=0]] | [[FACT:ny.local.nyc.method2.single.bracket.1.rate=2.05]] % | USD [[FACT:ny.local.nyc.method2.single.bracket.1.base=0]] | USD [[FACT:ny.local.nyc.method2.married.bracket.1.floor=0]] | [[FACT:ny.local.nyc.method2.married.bracket.1.rate=2.05]] % | USD [[FACT:ny.local.nyc.method2.married.bracket.1.base=0]] |
| 2 | USD [[FACT:ny.local.nyc.method2.single.bracket.2.floor=8000]] | [[FACT:ny.local.nyc.method2.single.bracket.2.rate=2.8]] % | USD [[FACT:ny.local.nyc.method2.single.bracket.2.base=164]] | USD [[FACT:ny.local.nyc.method2.married.bracket.2.floor=8000]] | [[FACT:ny.local.nyc.method2.married.bracket.2.rate=2.8]] % | USD [[FACT:ny.local.nyc.method2.married.bracket.2.base=164]] |
| 3 | USD [[FACT:ny.local.nyc.method2.single.bracket.3.floor=8700]] | [[FACT:ny.local.nyc.method2.single.bracket.3.rate=3.25]] % | USD [[FACT:ny.local.nyc.method2.single.bracket.3.base=184]] | USD [[FACT:ny.local.nyc.method2.married.bracket.3.floor=8700]] | [[FACT:ny.local.nyc.method2.married.bracket.3.rate=3.25]] % | USD [[FACT:ny.local.nyc.method2.married.bracket.3.base=184]] |
| 4 | USD [[FACT:ny.local.nyc.method2.single.bracket.4.floor=15,000]] | [[FACT:ny.local.nyc.method2.single.bracket.4.rate=3.95]] % | USD [[FACT:ny.local.nyc.method2.single.bracket.4.base=388]] | USD [[FACT:ny.local.nyc.method2.married.bracket.4.floor=15,000]] | [[FACT:ny.local.nyc.method2.married.bracket.4.rate=3.95]] % | USD [[FACT:ny.local.nyc.method2.married.bracket.4.base=388]] |
| 5 | USD [[FACT:ny.local.nyc.method2.single.bracket.5.floor=25,000]] | [[FACT:ny.local.nyc.method2.single.bracket.5.rate=4.15]] % | USD [[FACT:ny.local.nyc.method2.single.bracket.5.base=783]] | USD [[FACT:ny.local.nyc.method2.married.bracket.5.floor=25,000]] | [[FACT:ny.local.nyc.method2.married.bracket.5.rate=4.15]] % | USD [[FACT:ny.local.nyc.method2.married.bracket.5.base=783]] |
| 6 | USD [[FACT:ny.local.nyc.method2.single.bracket.6.floor=60,000]] | [[FACT:ny.local.nyc.method2.single.bracket.6.rate=4.25]] % | USD [[FACT:ny.local.nyc.method2.single.bracket.6.base=2236]] | USD [[FACT:ny.local.nyc.method2.married.bracket.6.floor=60,000]] | [[FACT:ny.local.nyc.method2.married.bracket.6.rate=4.25]] % | USD [[FACT:ny.local.nyc.method2.married.bracket.6.base=2236]] |

- **Yonkers resident surcharge [US-NYV7-003].** [[FACT:ny.local.yonkers.resident.surcharge.method=Compute the New York State withholding with NYS Method II (NYS Tables A-C and NYS annual schedules, reprinted in NYS-50-T-Y) or Method III above the NYS threshold; multiply that amount by 16.75%; withhold the product.]] Rate: [[FACT:ny.local.yonkers.resident.surcharge.rate=16.75]] % of the New York State amount withheld.
- **Yonkers nonresident earnings tax [US-NYV7-003].** [[FACT:ny.local.yonkers.nonresident.earnings_tax.method=Method VII per-period exclusion tables, or Method VIII: annualize gross wages (x 260/52/26/24/12), find the exclusion line, subtract the exclusion, x 0.50%, / same factor.]] Rate [[FACT:ny.local.yonkers.nonresident.earnings_tax.rate=0.5]] %; no withholding where Yonkers wages are expected to be below [[FACT:ny.local.yonkers.nonresident.no_withholding.below=4000]] USD. Method VIII exclusion table (annualised gross wages):

| Line | Annualised wages at least | Exclusion |
|---|---|---|
| 1 | USD [[FACT:ny.local.yonkers.nonresident.method8.bracket.1.floor=0]] | no withholding (see the threshold above) |
| 2 | USD [[FACT:ny.local.yonkers.nonresident.method8.bracket.2.floor=3,999.99]] | USD [[FACT:ny.local.yonkers.nonresident.method8.bracket.2.exclusion=3000]] |
| 3 | USD [[FACT:ny.local.yonkers.nonresident.method8.bracket.3.floor=10,000]] | USD [[FACT:ny.local.yonkers.nonresident.method8.bracket.3.exclusion=2000]] |
| 4 | USD [[FACT:ny.local.yonkers.nonresident.method8.bracket.4.floor=20,000]] | USD [[FACT:ny.local.yonkers.nonresident.method8.bracket.4.exclusion=1000]] |
| 5 | USD [[FACT:ny.local.yonkers.nonresident.method8.bracket.5.floor=30,000]] | USD [[FACT:ny.local.yonkers.nonresident.method8.bracket.5.exclusion=0]] |

- **Method II rounding.** The Method II steps end at the sum to withhold and print no rounding instruction; amounts are carried to the cent, but the rounding convention for the last cent is an open research point (below), and no convention is assumed in this guide.
- **Local income taxes (T3 piggyback) [US-NY-008, US-NYS5-010].** NYC: [[FACT:ny.pit.local.nyc.basis=resident tax, withheld regardless of work location; on NYS-1/NYS-45]]. Yonkers: resident surcharge, and nonresident earnings tax on work performed in Yonkers; no Yonkers nonresident withholding is needed where Yonkers wages are expected to be [[FACT:ny.pit.local.yonkers.nonresident_threshold=3000]] USD or less. The NYC tables did not change for 2026; the NYS and Yonkers tables did [US-NYS5-020].
- **Resident and nonresident matrix.**

| Income type | Resident of New York | Nonresident |
|---|---|---|
| Regular salary | Withheld on all wages wherever earned, NYS-50-T-NYS | Withheld on New York-source wages only, allocated on IT-2104.1; convenience-of-employer rule applies [US-NY-013, US-NYP52-002, US-NY-009] |
| Bonus / supplemental | NYS supplemental rate [[FACT:ny.pit.supplemental.nys.rate=11.7]] % or aggregate | Same rate on the New York-source share |
| NYC tax | Withheld if NYC resident, regardless of work location | Not withheld (no NYC nonresident tax) |
| Yonkers | Resident surcharge | Nonresident earnings tax on Yonkers work, subject to the threshold above |
| Severance, equity, benefits in kind | Taxed as wages under the federal wage definition (NYS-50 uses federal wages) | New York-source share only, allocation per IT-2104.1 |

- **Reciprocity:** [[FACT:ny.reciprocity.states=none]] [US-NY-013].

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.wh.method` | [[FACT:ny.wh.method=NYS-50-T-NYS (1/26): Method I tables, Method II exact calculation, Method III top income]] |  | 2026-01-01 to 2026-12-31 | US-NY-001 | NYC tables unchanged for 2026 (US-NYS5-020) |
| `ny.pit.top_income.threshold.annual` | [[FACT:ny.pit.top_income.threshold.annual=1,077,550]] | USD | 2026-01-01 to 2026-12-31 | US-NY-001 | Method III |
| `ny.wh.certificate` | [[FACT:ny.wh.certificate=IT-2104; 2020+ W-4 without IT-2104 = zero allowances]] |  | from 2026-01-01 | US-NYS5-010 |  |
| `ny.pit.exemption.annual` | [[FACT:ny.pit.exemption.annual=1000]] | USD | 2026-01-01 to 2026-12-31 | US-NY-001 | weekly 19.25; monthly 83.30 |
| `ny.pit.supplemental.nys.rate` | [[FACT:ny.pit.supplemental.nys.rate=11.7]] | % | 2026-01-01 to 2026-12-31 | US-NY-001 | or aggregate |
| `ny.pit.local.nyc.basis` | [[FACT:ny.pit.local.nyc.basis=resident tax, withheld regardless of work location; on NYS-1/NYS-45]] |  | from 2026-01-01 | US-NY-008 |  |
| `ny.pit.local.yonkers.nonresident_threshold` | [[FACT:ny.pit.local.yonkers.nonresident_threshold=3000]] | USD | from 2026-01-01 | US-NYS5-010 | no Yonkers withholding if Yonkers wages expected <= 3,000 |
| `ny.reciprocity.states` | [[FACT:ny.reciprocity.states=none]] |  | from 2026-01-01 | US-NY-013 | convenience-of-employer rule applies |
| `ny.pit.rounding` | [[FACT:ny.pit.rounding=to the cent per tables or formula]] |  | 2026-01-01 to 2026-12-31 | US-NY-001 |  |
| `ny.pit.oracle.example_1.withholding` | [[FACT:ny.pit.oracle.example_1.withholding=8.01]] | USD | 2026-01-01 to 2026-12-31 | US-NY-001 |  |
| `ny.pit.oracle.example_3.withholding` | [[FACT:ny.pit.oracle.example_3.withholding=3,576.63]] | USD | 2026-01-01 to 2026-12-31 | US-NY-001 | example 3 reproduced exactly |
| `ny.pit.oracle.example_4.withholding` | [[FACT:ny.pit.oracle.example_4.withholding=44.10]] | USD | 2026-01-01 to 2026-12-31 | US-NY-001 | example 4 reproduced exactly |
| `ny.pit.oracle.example_2.withholding` | [[FACT:ny.pit.oracle.example_2.withholding=258.51]] | USD | 2026-01-01 to 2026-12-31 | US-NY-001 |  |
| `ny.local.nyc.supplemental.rate` | [[FACT:ny.local.nyc.supplemental.rate=4.25]] | % | 2026-01-01 to 2026-12-31 | US-NYB5-301 | NYS-50-T-NYC (1/26) p. 3, method (a); or (b) aggregate with the latest regular wages minus tax already withheld. If no tax was withheld from regular wages, only (b). |
| `ny.local.yonkers.resident.supplemental.rate` | [[FACT:ny.local.yonkers.resident.supplemental.rate=1.95975]] | % | 2026-01-01 to 2026-12-31 | US-NYB5-302 | NYS-50-T-Y (1/26) p. 3, method (a); or (b) aggregate. If no tax was withheld from regular wages, only (b). |
| `ny.local.yonkers.nonresident.supplemental.rate` | [[FACT:ny.local.yonkers.nonresident.supplemental.rate=0.5]] | % | 2026-01-01 to 2026-12-31 | US-NYB5-302 | NYS-50-T-Y (1/26) p. 3, method (a); or (b) aggregate. |
| `ny.wh.method2.single.bracket.1.floor` | [[FACT:ny.wh.method2.single.bracket.1.floor=0]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 | NYS-50-T-NYS (1/26) p.17 Annual Tax Rate Schedule line 1: at least 0 but less than 8,500; column 4 0.0390; column 5 0.00 |
| `ny.wh.method2.single.bracket.1.rate` | [[FACT:ny.wh.method2.single.bracket.1.rate=3.9]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 | NYS-50-T-NYS (1/26) p.17 Annual Tax Rate Schedule line 1: at least 0 but less than 8,500; column 4 0.0390; column 5 0.00 (decimal as printed; value in percent) |
| `ny.wh.method2.single.bracket.1.base` | [[FACT:ny.wh.method2.single.bracket.1.base=0]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 | NYS-50-T-NYS (1/26) p.17 Annual Tax Rate Schedule line 1: at least 0 but less than 8,500; column 4 0.0390; column 5 0.00 (column 5; the sum is the annualized tax) |
| `ny.wh.method2.single.bracket.2.floor` | [[FACT:ny.wh.method2.single.bracket.2.floor=8500]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.2.rate` | [[FACT:ny.wh.method2.single.bracket.2.rate=4.4]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.2.base` | [[FACT:ny.wh.method2.single.bracket.2.base=332]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.3.floor` | [[FACT:ny.wh.method2.single.bracket.3.floor=11,700]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.3.rate` | [[FACT:ny.wh.method2.single.bracket.3.rate=5.15]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.3.base` | [[FACT:ny.wh.method2.single.bracket.3.base=472]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.4.floor` | [[FACT:ny.wh.method2.single.bracket.4.floor=13,900]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.4.rate` | [[FACT:ny.wh.method2.single.bracket.4.rate=5.4]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.4.base` | [[FACT:ny.wh.method2.single.bracket.4.base=586]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.5.floor` | [[FACT:ny.wh.method2.single.bracket.5.floor=80,650]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.5.rate` | [[FACT:ny.wh.method2.single.bracket.5.rate=5.9]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.5.base` | [[FACT:ny.wh.method2.single.bracket.5.base=4190]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.6.floor` | [[FACT:ny.wh.method2.single.bracket.6.floor=96,800]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.6.rate` | [[FACT:ny.wh.method2.single.bracket.6.rate=7.03]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.6.base` | [[FACT:ny.wh.method2.single.bracket.6.base=5143]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.7.floor` | [[FACT:ny.wh.method2.single.bracket.7.floor=107,650]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.7.rate` | [[FACT:ny.wh.method2.single.bracket.7.rate=7.53]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.7.base` | [[FACT:ny.wh.method2.single.bracket.7.base=5906]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.8.floor` | [[FACT:ny.wh.method2.single.bracket.8.floor=157,650]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.8.rate` | [[FACT:ny.wh.method2.single.bracket.8.rate=6.4]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.8.base` | [[FACT:ny.wh.method2.single.bracket.8.base=9673]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.9.floor` | [[FACT:ny.wh.method2.single.bracket.9.floor=215,400]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.9.rate` | [[FACT:ny.wh.method2.single.bracket.9.rate=11.44]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.9.base` | [[FACT:ny.wh.method2.single.bracket.9.base=13,369]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.10.floor` | [[FACT:ny.wh.method2.single.bracket.10.floor=265,400]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.10.rate` | [[FACT:ny.wh.method2.single.bracket.10.rate=7.35]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.bracket.10.base` | [[FACT:ny.wh.method2.single.bracket.10.base=19,091]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.single.deduction_allowance` | [[FACT:ny.wh.method2.single.deduction_allowance=7400]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Table B annual deduction allowance (p.14); per period: daily 28.45/30.60, weekly 142.30/152.90, biweekly 284.60/305.80, semimonthly 308.35/331.25, monthly 616.70/662.50 (single/married). Same value as ny.sit.deduction_allowance.{single,married}.annual where that key exists: same mechanism, two keys. |
| `ny.wh.method3.single.threshold` | [[FACT:ny.wh.method3.single.threshold=1,077,550]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method3.single.bracket.1.floor` | [[FACT:ny.wh.method3.single.bracket.1.floor=1,077,550]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Method III single table line 1 (p.22) |
| `ny.wh.method3.single.bracket.1.rate` | [[FACT:ny.wh.method3.single.bracket.1.rate=10.45]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Method III single table line 1 (p.22): multiply annualized wages by 0.1045 (flat on the whole annualized amount, not marginal) |
| `ny.wh.method3.single.bracket.2.floor` | [[FACT:ny.wh.method3.single.bracket.2.floor=5,000,000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Method III single table line 2 (p.22) |
| `ny.wh.method3.single.bracket.2.rate` | [[FACT:ny.wh.method3.single.bracket.2.rate=11.1]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Method III single table line 2 (p.22): multiply annualized wages by 0.1110 (flat on the whole annualized amount, not marginal) |
| `ny.wh.method3.single.bracket.3.floor` | [[FACT:ny.wh.method3.single.bracket.3.floor=25,000,000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Method III single table line 3 (p.22) |
| `ny.wh.method3.single.bracket.3.rate` | [[FACT:ny.wh.method3.single.bracket.3.rate=11.7]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Method III single table line 3 (p.22): multiply annualized wages by 0.1170 (flat on the whole annualized amount, not marginal) |
| `ny.wh.method2.married.bracket.1.floor` | [[FACT:ny.wh.method2.married.bracket.1.floor=0]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 | NYS-50-T-NYS (1/26) p.19 Annual Tax Rate Schedule line 1: at least 0 but less than 8,500; column 4 0.0390; column 5 0.00 |
| `ny.wh.method2.married.bracket.1.rate` | [[FACT:ny.wh.method2.married.bracket.1.rate=3.9]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 | NYS-50-T-NYS (1/26) p.19 Annual Tax Rate Schedule line 1: at least 0 but less than 8,500; column 4 0.0390; column 5 0.00 (decimal as printed; value in percent) |
| `ny.wh.method2.married.bracket.1.base` | [[FACT:ny.wh.method2.married.bracket.1.base=0]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 | NYS-50-T-NYS (1/26) p.19 Annual Tax Rate Schedule line 1: at least 0 but less than 8,500; column 4 0.0390; column 5 0.00 (column 5; the sum is the annualized tax) |
| `ny.wh.method2.married.bracket.2.floor` | [[FACT:ny.wh.method2.married.bracket.2.floor=8500]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.2.rate` | [[FACT:ny.wh.method2.married.bracket.2.rate=4.4]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.2.base` | [[FACT:ny.wh.method2.married.bracket.2.base=332]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.3.floor` | [[FACT:ny.wh.method2.married.bracket.3.floor=11,700]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.3.rate` | [[FACT:ny.wh.method2.married.bracket.3.rate=5.15]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.3.base` | [[FACT:ny.wh.method2.married.bracket.3.base=472]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.4.floor` | [[FACT:ny.wh.method2.married.bracket.4.floor=13,900]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.4.rate` | [[FACT:ny.wh.method2.married.bracket.4.rate=5.4]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.4.base` | [[FACT:ny.wh.method2.married.bracket.4.base=586]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.5.floor` | [[FACT:ny.wh.method2.married.bracket.5.floor=80,650]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.5.rate` | [[FACT:ny.wh.method2.married.bracket.5.rate=5.9]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.5.base` | [[FACT:ny.wh.method2.married.bracket.5.base=4190]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.6.floor` | [[FACT:ny.wh.method2.married.bracket.6.floor=96,800]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.6.rate` | [[FACT:ny.wh.method2.married.bracket.6.rate=6.57]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.6.base` | [[FACT:ny.wh.method2.married.bracket.6.base=5143]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.7.floor` | [[FACT:ny.wh.method2.married.bracket.7.floor=107,650]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.7.rate` | [[FACT:ny.wh.method2.married.bracket.7.rate=7.07]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.7.base` | [[FACT:ny.wh.method2.married.bracket.7.base=5855]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.8.floor` | [[FACT:ny.wh.method2.married.bracket.8.floor=157,650]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.8.rate` | [[FACT:ny.wh.method2.married.bracket.8.rate=8.01]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.8.base` | [[FACT:ny.wh.method2.married.bracket.8.base=9388]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.9.floor` | [[FACT:ny.wh.method2.married.bracket.9.floor=211,550]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.9.rate` | [[FACT:ny.wh.method2.married.bracket.9.rate=6.4]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.9.base` | [[FACT:ny.wh.method2.married.bracket.9.base=13,708]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.10.floor` | [[FACT:ny.wh.method2.married.bracket.10.floor=323,200]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.10.rate` | [[FACT:ny.wh.method2.married.bracket.10.rate=13.49]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.10.base` | [[FACT:ny.wh.method2.married.bracket.10.base=20,854]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.11.floor` | [[FACT:ny.wh.method2.married.bracket.11.floor=373,200]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.11.rate` | [[FACT:ny.wh.method2.married.bracket.11.rate=7.35]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.11.base` | [[FACT:ny.wh.method2.married.bracket.11.base=27,600]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.12.floor` | [[FACT:ny.wh.method2.married.bracket.12.floor=1,077,550]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.12.rate` | [[FACT:ny.wh.method2.married.bracket.12.rate=7.65]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.bracket.12.base` | [[FACT:ny.wh.method2.married.bracket.12.base=79,369]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method2.married.deduction_allowance` | [[FACT:ny.wh.method2.married.deduction_allowance=7950]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Table B annual deduction allowance (p.14); per period: daily 28.45/30.60, weekly 142.30/152.90, biweekly 284.60/305.80, semimonthly 308.35/331.25, monthly 616.70/662.50 (single/married). Same value as ny.sit.deduction_allowance.{single,married}.annual where that key exists: same mechanism, two keys. |
| `ny.wh.method3.married.threshold` | [[FACT:ny.wh.method3.married.threshold=2,155,350]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method3.married.bracket.1.floor` | [[FACT:ny.wh.method3.married.bracket.1.floor=2,155,350]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Method III married table line 1 (p.22) |
| `ny.wh.method3.married.bracket.1.rate` | [[FACT:ny.wh.method3.married.bracket.1.rate=10.45]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Method III married table line 1 (p.22): multiply annualized wages by 0.1045 (flat on the whole annualized amount, not marginal) |
| `ny.wh.method3.married.bracket.2.floor` | [[FACT:ny.wh.method3.married.bracket.2.floor=5,000,000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Method III married table line 2 (p.22) |
| `ny.wh.method3.married.bracket.2.rate` | [[FACT:ny.wh.method3.married.bracket.2.rate=11.1]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Method III married table line 2 (p.22): multiply annualized wages by 0.1110 (flat on the whole annualized amount, not marginal) |
| `ny.wh.method3.married.bracket.3.floor` | [[FACT:ny.wh.method3.married.bracket.3.floor=25,000,000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Method III married table line 3 (p.22) |
| `ny.wh.method3.married.bracket.3.rate` | [[FACT:ny.wh.method3.married.bracket.3.rate=11.7]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Method III married table line 3 (p.22): multiply annualized wages by 0.1170 (flat on the whole annualized amount, not marginal) |
| `ny.wh.method2.exemption_allowance` | [[FACT:ny.wh.method2.exemption_allowance=1000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-001 | Table C value of one exemption, full year 1,000 (daily 3.85, weekly 19.25, biweekly 38.50, semimonthly 41.65, monthly 83.30). Table A = Table B + n x Table C for n <= 10; use B + C beyond 10. |
| `ny.wh.method2.annualisation` | [[FACT:ny.wh.method2.annualisation=Method II: net wages = wages - Table A allowance for the payroll period; apply the per-period table (weekly/biweekly/semimonthly/monthly/daily) or the Annual Tax Rate Schedule for annual payrolls: (net - col3) x col4 + col5. Annualised net wages (net x payroll periods) are used only to test the Method III threshold. Other periods: convert via a factor to a common period, apply its table, convert the result back (p.23).]] |  | 2026-01-01 to 2026-12-31 | US-NYV7-001 |  |
| `ny.wh.method3.annualisation` | [[FACT:ny.wh.method3.annualisation=Method III: annualized wages = Method II net wages x payroll periods per year (e.g. 52, 26, 24, 12); x column 3 rate; / payroll periods = amount to withhold.]] |  | 2026-01-01 to 2026-12-31 | US-NYV7-001 | NYS-50-T-NYS (1/26) p.22 Steps 1-4. |
| `ny.local.nyc.method2.single.bracket.1.floor` | [[FACT:ny.local.nyc.method2.single.bracket.1.floor=0]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 1: at least 0 but less than 8,000; column 4 0.0205; column 5 0.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.single.bracket.1.rate` | [[FACT:ny.local.nyc.method2.single.bracket.1.rate=2.05]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 1: at least 0 but less than 8,000; column 4 0.0205; column 5 0.00. Single and married schedules are identical. (decimal as printed; value in percent) |
| `ny.local.nyc.method2.single.bracket.1.base` | [[FACT:ny.local.nyc.method2.single.bracket.1.base=0]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 1: at least 0 but less than 8,000; column 4 0.0205; column 5 0.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.single.bracket.2.floor` | [[FACT:ny.local.nyc.method2.single.bracket.2.floor=8000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 2: at least 8,000 but less than 8,700; column 4 0.0280; column 5 164.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.single.bracket.2.rate` | [[FACT:ny.local.nyc.method2.single.bracket.2.rate=2.8]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 2: at least 8,000 but less than 8,700; column 4 0.0280; column 5 164.00. Single and married schedules are identical. (decimal as printed; value in percent) |
| `ny.local.nyc.method2.single.bracket.2.base` | [[FACT:ny.local.nyc.method2.single.bracket.2.base=164]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 2: at least 8,000 but less than 8,700; column 4 0.0280; column 5 164.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.single.bracket.3.floor` | [[FACT:ny.local.nyc.method2.single.bracket.3.floor=8700]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 3: at least 8,700 but less than 15,000; column 4 0.0325; column 5 184.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.single.bracket.3.rate` | [[FACT:ny.local.nyc.method2.single.bracket.3.rate=3.25]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 3: at least 8,700 but less than 15,000; column 4 0.0325; column 5 184.00. Single and married schedules are identical. (decimal as printed; value in percent) |
| `ny.local.nyc.method2.single.bracket.3.base` | [[FACT:ny.local.nyc.method2.single.bracket.3.base=184]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 3: at least 8,700 but less than 15,000; column 4 0.0325; column 5 184.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.single.bracket.4.floor` | [[FACT:ny.local.nyc.method2.single.bracket.4.floor=15,000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 4: at least 15,000 but less than 25,000; column 4 0.0395; column 5 388.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.single.bracket.4.rate` | [[FACT:ny.local.nyc.method2.single.bracket.4.rate=3.95]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 4: at least 15,000 but less than 25,000; column 4 0.0395; column 5 388.00. Single and married schedules are identical. (decimal as printed; value in percent) |
| `ny.local.nyc.method2.single.bracket.4.base` | [[FACT:ny.local.nyc.method2.single.bracket.4.base=388]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 4: at least 15,000 but less than 25,000; column 4 0.0395; column 5 388.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.single.bracket.5.floor` | [[FACT:ny.local.nyc.method2.single.bracket.5.floor=25,000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 5: at least 25,000 but less than 60,000; column 4 0.0415; column 5 783.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.single.bracket.5.rate` | [[FACT:ny.local.nyc.method2.single.bracket.5.rate=4.15]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 5: at least 25,000 but less than 60,000; column 4 0.0415; column 5 783.00. Single and married schedules are identical. (decimal as printed; value in percent) |
| `ny.local.nyc.method2.single.bracket.5.base` | [[FACT:ny.local.nyc.method2.single.bracket.5.base=783]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.25 Annual Tax Rate Schedule line 5: at least 25,000 but less than 60,000; column 4 0.0415; column 5 783.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.single.bracket.6.floor` | [[FACT:ny.local.nyc.method2.single.bracket.6.floor=60,000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 |  |
| `ny.local.nyc.method2.single.bracket.6.rate` | [[FACT:ny.local.nyc.method2.single.bracket.6.rate=4.25]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-002 |  |
| `ny.local.nyc.method2.single.bracket.6.base` | [[FACT:ny.local.nyc.method2.single.bracket.6.base=2236]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 |  |
| `ny.local.nyc.method2.single.deduction_allowance` | [[FACT:ny.local.nyc.method2.single.deduction_allowance=5000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | Table B annual (p.24); semimonthly 208.35/229.15, monthly 416.70/458.30 (single/married). |
| `ny.local.nyc.method2.married.bracket.1.floor` | [[FACT:ny.local.nyc.method2.married.bracket.1.floor=0]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 1: at least 0 but less than 8,000; column 4 0.0205; column 5 0.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.married.bracket.1.rate` | [[FACT:ny.local.nyc.method2.married.bracket.1.rate=2.05]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 1: at least 0 but less than 8,000; column 4 0.0205; column 5 0.00. Single and married schedules are identical. (decimal as printed; value in percent) |
| `ny.local.nyc.method2.married.bracket.1.base` | [[FACT:ny.local.nyc.method2.married.bracket.1.base=0]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 1: at least 0 but less than 8,000; column 4 0.0205; column 5 0.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.married.bracket.2.floor` | [[FACT:ny.local.nyc.method2.married.bracket.2.floor=8000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 2: at least 8,000 but less than 8,700; column 4 0.0280; column 5 164.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.married.bracket.2.rate` | [[FACT:ny.local.nyc.method2.married.bracket.2.rate=2.8]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 2: at least 8,000 but less than 8,700; column 4 0.0280; column 5 164.00. Single and married schedules are identical. (decimal as printed; value in percent) |
| `ny.local.nyc.method2.married.bracket.2.base` | [[FACT:ny.local.nyc.method2.married.bracket.2.base=164]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 2: at least 8,000 but less than 8,700; column 4 0.0280; column 5 164.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.married.bracket.3.floor` | [[FACT:ny.local.nyc.method2.married.bracket.3.floor=8700]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 3: at least 8,700 but less than 15,000; column 4 0.0325; column 5 184.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.married.bracket.3.rate` | [[FACT:ny.local.nyc.method2.married.bracket.3.rate=3.25]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 3: at least 8,700 but less than 15,000; column 4 0.0325; column 5 184.00. Single and married schedules are identical. (decimal as printed; value in percent) |
| `ny.local.nyc.method2.married.bracket.3.base` | [[FACT:ny.local.nyc.method2.married.bracket.3.base=184]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 3: at least 8,700 but less than 15,000; column 4 0.0325; column 5 184.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.married.bracket.4.floor` | [[FACT:ny.local.nyc.method2.married.bracket.4.floor=15,000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 4: at least 15,000 but less than 25,000; column 4 0.0395; column 5 388.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.married.bracket.4.rate` | [[FACT:ny.local.nyc.method2.married.bracket.4.rate=3.95]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 4: at least 15,000 but less than 25,000; column 4 0.0395; column 5 388.00. Single and married schedules are identical. (decimal as printed; value in percent) |
| `ny.local.nyc.method2.married.bracket.4.base` | [[FACT:ny.local.nyc.method2.married.bracket.4.base=388]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 4: at least 15,000 but less than 25,000; column 4 0.0395; column 5 388.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.married.bracket.5.floor` | [[FACT:ny.local.nyc.method2.married.bracket.5.floor=25,000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 5: at least 25,000 but less than 60,000; column 4 0.0415; column 5 783.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.married.bracket.5.rate` | [[FACT:ny.local.nyc.method2.married.bracket.5.rate=4.15]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 5: at least 25,000 but less than 60,000; column 4 0.0415; column 5 783.00. Single and married schedules are identical. (decimal as printed; value in percent) |
| `ny.local.nyc.method2.married.bracket.5.base` | [[FACT:ny.local.nyc.method2.married.bracket.5.base=783]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | NYS-50-T-NYC (1/26) p.26 Annual Tax Rate Schedule line 5: at least 25,000 but less than 60,000; column 4 0.0415; column 5 783.00. Single and married schedules are identical. |
| `ny.local.nyc.method2.married.bracket.6.floor` | [[FACT:ny.local.nyc.method2.married.bracket.6.floor=60,000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 |  |
| `ny.local.nyc.method2.married.bracket.6.rate` | [[FACT:ny.local.nyc.method2.married.bracket.6.rate=4.25]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-002 |  |
| `ny.local.nyc.method2.married.bracket.6.base` | [[FACT:ny.local.nyc.method2.married.bracket.6.base=2236]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 |  |
| `ny.local.nyc.method2.married.deduction_allowance` | [[FACT:ny.local.nyc.method2.married.deduction_allowance=5500]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | Table B annual (p.24); semimonthly 208.35/229.15, monthly 416.70/458.30 (single/married). |
| `ny.local.nyc.method2.exemption_allowance` | [[FACT:ny.local.nyc.method2.exemption_allowance=1000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-002 | Table C full-year exemption 1,000 (daily 3.85, weekly 19.25, biweekly 38.50, semimonthly 41.65, monthly 83.30). |
| `ny.local.nyc.method2.annualisation` | [[FACT:ny.local.nyc.method2.annualisation=Same steps as NYS Method II with the NYC Tables A-C and NYC schedules; NYC has no Method III and no top-income switch (top line 60,000 and over at 0.0425).]] |  | 2026-01-01 to 2026-12-31 | US-NYV7-002 |  |
| `ny.local.yonkers.resident.surcharge.rate` | [[FACT:ny.local.yonkers.resident.surcharge.rate=16.75]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-003 | NYS-50-T-Y (1/26) Method II Step 5 and Method III Step 4: 'Multiply the result by [[FACT:ny.local.yonkers.resident.surcharge.rate=16.75]]% (0.1675).' |
| `ny.local.yonkers.resident.surcharge.method` | [[FACT:ny.local.yonkers.resident.surcharge.method=Compute the New York State withholding with NYS Method II (NYS Tables A-C and NYS annual schedules, reprinted in NYS-50-T-Y) or Method III above the NYS threshold; multiply that amount by 16.75%; withhold the product.]] |  | 2026-01-01 to 2026-12-31 | US-NYV7-003 |  |
| `ny.local.yonkers.nonresident.earnings_tax.rate` | [[FACT:ny.local.yonkers.nonresident.earnings_tax.rate=0.5]] | % | 2026-01-01 to 2026-12-31 | US-NYV7-003 | NYS-50-T-Y (1/26) Methods VI-VIII: [[FACT:ny.local.yonkers.nonresident.earnings_tax.rate=0.5]]% (0.0050) of wages after the exclusion; rate unchanged for 2026 (p.3). |
| `ny.local.yonkers.nonresident.earnings_tax.method` | [[FACT:ny.local.yonkers.nonresident.earnings_tax.method=Method VII per-period exclusion tables, or Method VIII: annualize gross wages (x 260/52/26/24/12), find the exclusion line, subtract the exclusion, x 0.50%, / same factor.]] |  | 2026-01-01 to 2026-12-31 | US-NYV7-003 | p.24 Method VII; p.25 Method VIII. Applies to nonresidents earning wages in Yonkers paid by an employer with an office or business in New York State. |
| `ny.local.yonkers.nonresident.method8.bracket.1.floor` | [[FACT:ny.local.yonkers.nonresident.method8.bracket.1.floor=0]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-003 |  |
| `ny.local.yonkers.nonresident.method8.bracket.2.floor` | [[FACT:ny.local.yonkers.nonresident.method8.bracket.2.floor=3,999.99]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-003 |  |
| `ny.local.yonkers.nonresident.method8.bracket.2.exclusion` | [[FACT:ny.local.yonkers.nonresident.method8.bracket.2.exclusion=3000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-003 |  |
| `ny.local.yonkers.nonresident.method8.bracket.3.floor` | [[FACT:ny.local.yonkers.nonresident.method8.bracket.3.floor=10,000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-003 | Method VIII annual schedule line 3: over 10,000 not over 20,000 |
| `ny.local.yonkers.nonresident.method8.bracket.3.exclusion` | [[FACT:ny.local.yonkers.nonresident.method8.bracket.3.exclusion=2000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-003 | Method VIII annual schedule line 3: over 10,000 not over 20,000; annualized exclusion |
| `ny.local.yonkers.nonresident.method8.bracket.4.floor` | [[FACT:ny.local.yonkers.nonresident.method8.bracket.4.floor=20,000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-003 | Method VIII annual schedule line 4: over 20,000 not over 30,000 |
| `ny.local.yonkers.nonresident.method8.bracket.4.exclusion` | [[FACT:ny.local.yonkers.nonresident.method8.bracket.4.exclusion=1000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-003 | Method VIII annual schedule line 4: over 20,000 not over 30,000; annualized exclusion |
| `ny.local.yonkers.nonresident.method8.bracket.5.floor` | [[FACT:ny.local.yonkers.nonresident.method8.bracket.5.floor=30,000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-003 | Method VIII annual schedule line 5: over 30,000 |
| `ny.local.yonkers.nonresident.method8.bracket.5.exclusion` | [[FACT:ny.local.yonkers.nonresident.method8.bracket.5.exclusion=0]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-003 | Method VIII annual schedule line 5: over 30,000; annualized exclusion |
| `ny.local.yonkers.nonresident.no_withholding.below` | [[FACT:ny.local.yonkers.nonresident.no_withholding.below=4000]] | USD | 2026-01-01 to 2026-12-31 | US-NYV7-003 | Method VIII: 'Withholding is not required for annualized pay that is less than $4,000.' |

**Open research points**

- Not configured in this release [[GAP:RQ-263]]: NYS-50-T-NYS Method II example 2 is printed as [[FACT:ny.pit.oracle.example_2.withholding=258.51]] USD; half-up rounding of the intermediate rate product gives one cent less, so the booklet's rounding convention is not established.
- Not configured in this release [[GAP:RQ-263]]: NYS-50-T-NYS, NYS-50-T-NYC and NYS-50-T-Y (1/26) print no rounding instruction for Method II, and Example 2 is printed one cent above the half-up result; this is the same open point as the example 2 residual. No rounding convention is assumed in this guide.

## NY.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in NY.2.

## NY.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in NY.2.

## NY.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **State unemployment insurance [US-NYS5-010, US-NYP9V-001].** 2026 taxable wage base [[FACT:ny.sui.wage_base=17,600]] USD (from 2026 indexed to a share of the state average annual wage and never reduced, US-NY-007). New-employer rate [[FACT:ny.sui.new_employer.rate=4.025]] % (normal plus subsidiary), plus the Re-employment Service Fund [[FACT:ny.ui.rsf.rate=0.075]] %. Experience range [[FACT:ny.sui.employer.rate.min=1.625]] % to [[FACT:ny.sui.employer.rate.max=9.425]] %. Employee UI contribution: [[FACT:ny.sui.employee.rate=0]] %. The state UI loan was repaid in the FY2026 budget; the FUTA credit-reduction effect is in Annex FED / MULTI.
- **Paid Family Leave (PFL) [US-NYP8-001, US-NYB5-001].** Employee-paid. 2026: [[FACT:ny.pfl.employee.rate=0.432]] % of wages, annual employee maximum [[FACT:ny.pfl.employee.max_annual=411.91]] USD. 2027 (DFS decision of 2026-08-31): [[FACT:ny.pfl.employee.rate=0.452]] %, maximum [[FACT:ny.pfl.employee.max_annual=451.81]] USD. Benefit [[FACT:ny.pfl.benefit.rate_of_aww=67]] % of the employee's average weekly wage, capped at the same share of the NYSAWW ([[FACT:ny.pfl.nysaww=1,833.63]] USD for 2026), i.e. a 2026 maximum weekly benefit of [[FACT:ny.pfl.benefit.max_weekly=1,228.53]] USD [US-NYB5-002]. Calendar-year accumulator: [[FACT:ny.pfl.employee.max_annual.accumulation=calendar-year accumulator per employee: apply the PFL rate to wages each pay period until year-to-date employee contributions reach ny.pfl.employee.max_annual; no further contribution for that calendar year]] [US-NYP8-001, US-NYB5-001].
- **Disability benefits (DBL) [US-NYB5-401].** Employee [[FACT:ny.dbl.employee.rate=0.5]] % of wages, capped at [[FACT:ny.dbl.employee.max_weekly=0.60]] USD per week; the employer pays the remaining cost.
- **Employer levies.** MCTMT (MTA-305, quarterly) and the Re-employment Service Fund per the levy census [US-NYP7-001, US-NYP7-004, US-OWN-007]; no MCTMT rate is carried in this annex's facts.

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.sui.wage_base` | [[FACT:ny.sui.wage_base=17,600]] | USD | 2026-01-01 to 2026-12-31 | US-NYS5-010 | 18% of state average annual wage rounded up to 100, never reduced |
| `ny.sui.new_employer.rate` | [[FACT:ny.sui.new_employer.rate=4.025]] | % | 2026-01-01 to 2026-12-31 | US-NYP9V-001 | 3.4 normal + 0.625 subsidiary; + RSF 0.075 = 4.1 |
| `ny.ui.rsf.rate` | [[FACT:ny.ui.rsf.rate=0.075]] | % | 2026-01-01 to 2026-12-31 | US-NYP9V-001 | Re-employment Service Fund |
| `ny.sui.employer.rate.min` | [[FACT:ny.sui.employer.rate.min=1.625]] | % | 2026-01-01 to 2026-12-31 | US-NYP9V-001 |  |
| `ny.sui.employer.rate.max` | [[FACT:ny.sui.employer.rate.max=9.425]] | % | 2026-01-01 to 2026-12-31 | US-NYP9V-001 |  |
| `ny.sui.employee.rate` | [[FACT:ny.sui.employee.rate=0]] | % | from 2026-01-01 | US-NYR3C-001 | N.Y. Labor Law 570(6): no agreement by an employee to pay any part of the employer's UI contribution is valid, and no employer may deduct it from the employee's remuneration. |
| `ny.pfl.employee.rate` | [[FACT:ny.pfl.employee.rate=0.432]] | % | 2026-01-01 to 2026-12-31 | US-NYP8-001 |  |
| `ny.pfl.employee.max_annual` | [[FACT:ny.pfl.employee.max_annual=411.91]] | USD | 2026-01-01 to 2026-12-31 | US-NYP8-001 |  |
| `ny.dbl.employee.rate` | [[FACT:ny.dbl.employee.rate=0.5]] | % | from 2026-01-01 | US-NYB5-401 | Max 0.60/week; employer pays the rest. WCL 209(3)(a): "one-half of one per centum of the employee's wages ... but not in excess of sixty cents per week". |
| `ny.dbl.employee.max_weekly` | [[FACT:ny.dbl.employee.max_weekly=0.60]] | USD | from 2026-01-01 | US-NYB5-401 | WCL 209(3)(a): "one-half of one per centum of the employee's wages ... but not in excess of sixty cents per week". |
| `ny.pfl.employee.rate` | [[FACT:ny.pfl.employee.rate=0.452]] | % | from 2027-01-01 | US-NYB5-001 |  |
| `ny.pfl.employee.max_annual` | [[FACT:ny.pfl.employee.max_annual=451.81]] | USD | from 2027-01-01 | US-NYB5-001 |  |
| `ny.pfl.nysaww` | [[FACT:ny.pfl.nysaww=1,833.63]] | USD | 2026-01-01 to 2026-12-31 | US-NYB5-002 | New York State Average Weekly Wage used for 2026 PFL benefits; 2027 NYSAWW +4.83% (amount not stated). |
| `ny.pfl.benefit.max_weekly` | [[FACT:ny.pfl.benefit.max_weekly=1,228.53]] | USD | 2026-01-01 to 2026-12-31 | US-NYB5-002 |  |
| `ny.pfl.benefit.rate_of_aww` | [[FACT:ny.pfl.benefit.rate_of_aww=67]] | % | from 2026-01-01 | US-NYB5-002 |  |
| `ny.pfl.employee.max_annual.accumulation` | [[FACT:ny.pfl.employee.max_annual.accumulation=calendar-year accumulator per employee: apply the PFL rate to wages each pay period until year-to-date employee contributions reach ny.pfl.employee.max_annual; no further contribution for that calendar year]] |  | 2026-01-01 to 2026-12-31 | US-NYP8-001 |  |
| `ny.pfl.employee.max_annual.accumulation` | [[FACT:ny.pfl.employee.max_annual.accumulation=calendar-year accumulator per employee: apply the PFL rate to wages each pay period until year-to-date employee contributions reach ny.pfl.employee.max_annual; no further contribution for that calendar year]] |  | from 2027-01-01 | US-NYB5-001 |  |

**Open research points**

- Not yet published [[GAP:RQ-264]]: The 2027 New York UI wage base (the state average annual wage, rounded up to the next hundred dollars) is expected in December 2026.

## NY.4 Pay statement

- **Content (Labor Law 195(3)), with every payment [US-NYS5-006]:** [[FACT:ny.payslip.items=dates of work; names; employer address/phone; rates and basis; gross; deductions; allowances; net; regular and OT rates and hours (non-exempt); piece rates]]. Prevailing-wage supplements and allowances claimed toward the minimum wage are shown where they apply.
- **NYC Protected Time Off statement** (from 2026-02-22): [[FACT:ny.leave.nyc_pto.pay_statement_items=Each pay period, on the pay statement or other written documentation: PTO accrued in the period; paid and unpaid PTO used in the period; unpaid immediately available hours available in the calendar year; accrued PTO available for use in the calendar year]] [US-NYB5-003].
- **Electronic statements:** [[FACT:ny.payslip.electronic=Employer must furnish each employee a statement with every payment of wages; the section text contains no occurrence of 'electronic' (inspected directly), so electronic delivery rests on DOL guidance which was not obtained]] [[GAP:RQ-267]] [US-NYV6-006].
- **Retention:** payroll records [[FACT:ny.records.retention_years=6]] years (195(4)); tax records per DTF rules [US-NYS5-010].
- **Hire notice** in English and the employee's primary language (195(1)) [US-NYP51-003]; the payslip itself is in English (US-OWN-006).

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.payslip.items` | [[FACT:ny.payslip.items=dates of work; names; employer address/phone; rates and basis; gross; deductions; allowances; net; regular and OT rates and hours (non-exempt); piece rates]] |  | from 2026-01-01 | US-NYS5-006 | Labor Law 195(3) with every payment |
| `ny.records.retention_years` | [[FACT:ny.records.retention_years=6]] | years | from 2026-01-01 | US-NYS5-006 | 195(4); tax records 4 years |
| `ny.payslip.electronic` | [[FACT:ny.payslip.electronic=Employer must furnish each employee a statement with every payment of wages; the section text contains no occurrence of 'electronic' (inspected directly), so electronic delivery rests on DOL guidance which was not obtained]] [[GAP:RQ-267]] |  | from 2026-01-01 | US-NYV6-006 | Register: US-NYV6-006 |

## NY.5 Statutory reporting

- **NYS-45** (quarterly, combined withholding, wage reporting and UI), due [[FACT:ny.report.nys45.due=Apr 30; Jul 31; Oct 31; Jan 31]]; Parts A, B and C mandatory; e-file and electronic payment mandatory [US-NYS5-010]. Upload specification Pub 72.5 [US-FIL-007]. Annual reconciliation: [[FACT:ny.report.nys45_annual=NYS-45 is a quarterly combined return (Parts A UI, B withholding reconciliation, C employee wage detail) due last day of month after quarter end; no separate annual NYS-45 reconciliation found in the instructions; annual UI items go on IA7/IA7A; Q4 withholding overpayment is refunded automatically]] [US-NYV6-001].
- **NYS-1 withholding deposit:** due within a few business days of the payroll that brings quarter-to-date withholding to [[FACT:ny.report.nys1.threshold=700]] USD or more; below it, pay with the NYS-45 [US-NYS5-010].
- **Form W-2:** no copy is filed with New York; NYS-45 Part C (quarterly wage reporting) replaces it. State wages box = federal box 1 for residents and for nonresidents with any New York service; the NYC box = box 1 for full-year residents [US-NYS5-010].
- **New hire:** report to DTF within [[FACT:ny.newhire.report_days=20]] calendar days, including rehires after a long separation; for a nonresident alien the period runs from SSN issue [US-NYS5-010].
- **Registration:** NY Business Express for UI, wage reporting and withholding [US-NYS5-010]. **MCTMT:** MTA-305, quarterly [US-NY-003].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.report.nys45.due` | [[FACT:ny.report.nys45.due=Apr 30; Jul 31; Oct 31; Jan 31]] |  | from 2026-01-01 | US-NYS5-010 | combined withholding + wage reporting + UI; e-file mandatory; no annual W-2 copy to NY |
| `ny.report.nys1.threshold` | [[FACT:ny.report.nys1.threshold=700]] | USD | from 2026-01-01 | US-NYS5-010 | deposit within 3 business days (if 15,000+ two years prior) or 5 business days |
| `ny.newhire.report_days` | [[FACT:ny.newhire.report_days=20]] | days | from 2026-01-01 | US-NYS5-010 | to DTF; includes dependent health insurance availability |
| `ny.report.nys45_annual` | [[FACT:ny.report.nys45_annual=NYS-45 is a quarterly combined return (Parts A UI, B withholding reconciliation, C employee wage detail) due last day of month after quarter end; no separate annual NYS-45 reconciliation found in the instructions; annual UI items go on IA7/IA7A; Q4 withholding overpayment is refunded automatically]] |  | from 2026-01-01 | US-NYV6-001 | Register: US-NYV6-001 |

## NY.6 Leave

- **State paid sick leave (Labor Law 196-b) [US-NYS5-007].** Medium employers (band `5_99` of the key): [[FACT:ny.leave.paid_sick.annual_hours.5_99=40]] hours paid; large employers (band `100plus`): [[FACT:ny.leave.paid_sick.annual_hours.100plus=56]] hours paid; the smallest employers owe unpaid leave unless net income exceeds the statutory amount (196-b). Accrual one hour per [[FACT:ny.leave.paid_sick.accrual_ratio_hours_worked=30]] hours worked; front-loading allowed; paid at the regular rate (or minimum wage if higher); carry-over required, use may be capped; no payout at separation.
- **Paid prenatal leave:** [[FACT:ny.leave.prenatal.hours_per_52_weeks=20]] hours per rolling year, paid at the regular rate, no payout [US-NYS5-007].
- **NYC Protected Time Off (from 2026-02-22) [US-NYB5-003].** Paid PTO up to [[FACT:ny.leave.nyc_pto.paid_hours.max.under100=40]] hours (employers below the large-employer band) or [[FACT:ny.leave.nyc_pto.paid_hours.max.100plus=56]] hours (large employers); plus [[FACT:ny.leave.nyc_pto.unpaid_hours_immediate=32]] hours of unpaid PTO available at hire and on the first day of each calendar year (no proration, no carry-over required); plus [[FACT:ny.leave.nyc_pto.prenatal_paid_hours=20]] hours of paid prenatal leave per rolling year.
- **PFL benefits** are paid by the insurer, not by the employer as wages (see Section 3).

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.leave.paid_sick.annual_hours.5_99` | [[FACT:ny.leave.paid_sick.annual_hours.5_99=40]] | hours | from 2025-01-01 | US-NYS5-007 | 196-b; 4 or fewer: 40 unpaid (paid if net income >1M); 100+: 56 paid |
| `ny.leave.paid_sick.annual_hours.100plus` | [[FACT:ny.leave.paid_sick.annual_hours.100plus=56]] | hours | from 2025-01-01 | US-NYS5-007 |  |
| `ny.leave.paid_sick.accrual_ratio_hours_worked` | [[FACT:ny.leave.paid_sick.accrual_ratio_hours_worked=30]] | hours | from 2025-01-01 | US-NYB5-003 | no payout at separation |
| `ny.leave.prenatal.hours_per_52_weeks` | [[FACT:ny.leave.prenatal.hours_per_52_weeks=20]] | hours | from 2025-01-01 | US-NYB5-003 | paid; no payout |
| `ny.leave.nyc_pto.unpaid_hours_immediate` | [[FACT:ny.leave.nyc_pto.unpaid_hours_immediate=32]] | hours | from 2026-02-22 | US-NYB5-003 | Available at hire and again on the first day of each calendar year; no proration, no carryover required. |
| `ny.leave.nyc_pto.paid_hours.max.under100` | [[FACT:ny.leave.nyc_pto.paid_hours.max.under100=40]] | hours | from 2026-02-22 | US-NYB5-003 | Employers with 99 or fewer employees. |
| `ny.leave.nyc_pto.paid_hours.max.100plus` | [[FACT:ny.leave.nyc_pto.paid_hours.max.100plus=56]] | hours | from 2026-02-22 | US-NYB5-003 |  |
| `ny.leave.nyc_pto.prenatal_paid_hours` | [[FACT:ny.leave.nyc_pto.prenatal_paid_hours=20]] | hours | from 2026-02-22 | US-NYB5-003 | Per 52 weeks, no accrual (separate from PTO). |
| `ny.leave.nyc_pto.pay_statement_items` | [[FACT:ny.leave.nyc_pto.pay_statement_items=Each pay period, on the pay statement or other written documentation: PTO accrued in the period; paid and unpaid PTO used in the period; unpaid immediately available hours available in the calendar year; accrued PTO available for use in the calendar year]] |  | from 2026-02-22 | US-NYB5-003 |  |

## NY.7 Termination and final pay

- **Final pay:** [[FACT:ny.final_pay.rule=next regular payday (discharge and resignation)]]; by mail on request (191(3)) [US-NYS5-003].
- **Written termination notice** stating the exact termination date and the benefits cancellation date within [[FACT:ny.term.notice.working_days=5]] working days (195(6)) [US-NYS5-006].
- **UI separation notice:** [[FACT:ny.term.ui_notice.form=IA 12.3 to every separated worker or hours cut to 30 or fewer]] [US-NYS5-017]; timing: [[FACT:ny.term.ia12_3.timing=Timing is statutory: Labor Law 590(2) requires the written notice at the time of each permanent or indefinite separation, reduction in hours, temporary separation and other interruption causing total or partial unemployment. DOL page (A.2): notice required for employees whose hours drop to 30 or less per week or who go off payroll; content: employer name, registration number, FEIN, payroll-records mailing address, claim instructions. The 12 NYCRR 472.8 text itself was not read (govt.westlaw.com not tried); dol.ny.gov/notice-eligibility-ui-benefits still returns Access denied (not bypassed).]] [US-NYV6B-001].
- **Accrued vacation:** no statutory payout; a "wage supplement" under 198-c payable per policy or agreement [US-NYS5-008]. Unused sick and prenatal leave: no payout [US-NYS5-007]. NY WARN is not a payroll calculation and is not covered.

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.final_pay.rule` | [[FACT:ny.final_pay.rule=next regular payday (discharge and resignation)]] |  | from 2026-01-01 | US-NYS5-003 | 191(3) |
| `ny.term.notice.working_days` | [[FACT:ny.term.notice.working_days=5]] | days | from 2026-01-01 | US-NYS5-006 | written notice of termination date and benefits cancellation (195(6)) |
| `ny.term.ui_notice.form` | [[FACT:ny.term.ui_notice.form=IA 12.3 to every separated worker or hours cut to 30 or fewer]] |  | from 2026-01-01 | US-NYS5-017 |  |
| `ny.term.ia12_3.timing` | [[FACT:ny.term.ia12_3.timing=Timing is statutory: Labor Law 590(2) requires the written notice at the time of each permanent or indefinite separation, reduction in hours, temporary separation and other interruption causing total or partial unemployment. DOL page (A.2): notice required for employees whose hours drop to 30 or less per week or who go off payroll; content: employer name, registration number, FEIN, payroll-records mailing address, claim instructions. The 12 NYCRR 472.8 text itself was not read (govt.westlaw.com not tried); dol.ny.gov/notice-eligibility-ui-benefits still returns Access denied (not bypassed).]] |  | from 2026-01-01 | US-NYV6B-001 | Register: US-NYV6B-001, US-NYV6B-002 |

## NY.8 Benefits in kind and taxable wages

- **Conformity.** The New York return starts from federal wages (W-2 box 1), so the federal exclusions (401(k), 403(b), 457, cafeteria plans, HSA, transit, group-term life) carry over.
- **Departure:** 414(h) contributions of New York public employees are added back (addback applies: [[FACT:ny.bik.414h.addback=True]]) [US-NYS5-019]. New York City flexible benefits: [[FACT:ny.bik.nyc_flex125_addback=A-101 New York City flexible benefits program (IRC 125): amount deducted/deferred under an NYC (or certain other NYC public employer) flexible benefits program shown on W-2 is an ADDITION modification on IT-201/IT-203/IT-204. Edition read is (2025); level: assessment]] [US-NYV6-004]. UI remuneration includes the reasonable value of meals and lodging, and tips [US-NYS5-010].

**Parameters (benefits in kind and the taxable base)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.bik.414h.addback` | [[FACT:ny.bik.414h.addback=True]] |  | from 2025-01-01 | US-NYS5-019 | NY public employees |
| `ny.bik.nyc_flex125_addback` | [[FACT:ny.bik.nyc_flex125_addback=A-101 New York City flexible benefits program (IRC 125): amount deducted/deferred under an NYC (or certain other NYC public employer) flexible benefits program shown on W-2 is an ADDITION modification on IT-201/IT-203/IT-204. Edition read is (2025); level: assessment]] |  | from 2026-01-01 | US-NYV6-004 |  |

## NY.9 Deductions and garnishments

- **Authorised deductions (Labor Law 193) [US-NYS5-005].** Only deductions required by law or voluntarily authorised in writing within the listed categories; authorisations kept for the employment plus the retention period; overpayment and advance recovery follow DOL regulations. The expanded text carries a sunset of 2028-11-06.
- **Creditor income execution (CPLR 5231) [US-NYS5-015].** At most [[FACT:ny.garn.consumer.max_rate_of_gross=10]] % of gross, never more than the federal disposable-earnings cap; the deduction may not reduce weekly disposable earnings below the statutory floor ([[FACT:ny.garn.consumer.floor_region=Nothing withheld unless weekly disposable earnings exceed the GREATER of 30x the federal minimum hourly wage or 30x the state minimum hourly wage in Labor Law 652 (so the state minimum applies when higher); cap is the lesser of 25% of disposable earnings or the excess over that floor; 10% of gross for the 10% execution. The clause as read does not name a Labor Law 652 region]] [US-NYV6-002]). No income execution for medical-debt judgments.
- **Support (CPLR 5241) [US-NYS5-016].** Start no later than the first pay period after service; remit to the SDU within [[FACT:ny.garn.support.remit_business_days=7]] business days of payday; CCPA percentage limits (Annex FED); support takes priority; multiple orders prorated; order current support, health premium, arrears; notify the issuer on termination.
- **State tax levy (income execution) [US-NYV6-003]:** [[FACT:ny.garn.state_tax_levy=DTF issues a warrant after notice and demand; once filed with the county clerk it is a judgment and the sheriff/DTF officer executes it 'in the same manner prescribed by law in respect to executions issued against' property, i.e. CPLR 5231 income-execution limits apply to wages (not separately read per DTF forms)]].

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.garn.consumer.max_rate_of_gross` | [[FACT:ny.garn.consumer.max_rate_of_gross=10]] | % | from 2026-01-01 | US-NYS5-015 | CPLR 5231; never >25% disposable; floor 30x greater of federal or NY minimum |
| `ny.garn.support.remit_business_days` | [[FACT:ny.garn.support.remit_business_days=7]] | days | from 2026-01-01 | US-NYS5-016 | CPLR 5241 |
| `ny.garn.consumer.floor_region` | [[FACT:ny.garn.consumer.floor_region=Nothing withheld unless weekly disposable earnings exceed the GREATER of 30x the federal minimum hourly wage or 30x the state minimum hourly wage in Labor Law 652 (so the state minimum applies when higher); cap is the lesser of 25% of disposable earnings or the excess over that floor; 10% of gross for the 10% execution. The clause as read does not name a Labor Law 652 region]] |  | from 2026-01-01 | US-NYV6-002 | Register: US-NYV6-002 |
| `ny.garn.state_tax_levy` | [[FACT:ny.garn.state_tax_levy=DTF issues a warrant after notice and demand; once filed with the county clerk it is a judgment and the sheriff/DTF officer executes it 'in the same manner prescribed by law in respect to executions issued against' property, i.e. CPLR 5231 income-execution limits apply to wages (not separately read per DTF forms)]] |  | from 2026-01-01 | US-NYV6-003 | Register: US-NYV6-003 |

## NY.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

- **Prevailing wage:** exists ([[FACT:ny.prevailing_wage.exists=True]]); Labor Law 220 public-work rates and supplements [US-NYP51-002]. The pay statement must identify prevailing-wage supplements [US-NYS5-006]. Certified-payroll mechanics are not modelled.

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.prevailing_wage.exists` | [[FACT:ny.prevailing_wage.exists=True]] |  | from 2026-01-01 | US-NYP51-002 | Labor Law 220 |

## NY.11 Indexation

- **Minimum wage:** from 2027 indexed to the three-year average of the August-July CPI-W Northeast, subject to off-ramps; published by October 1 [US-NYS5-002]. For 2027 the off-ramp was met (no increase) [US-NYS5-001].
- **Exempt thresholds and meal/lodging credits** move with the minimum-wage orders (652(2)) [US-NYS5-011].
- **UI wage base:** indexed to the state average annual wage [US-NYS5-010]; 2027 value open (Section 3).
- **PFL:** DFS publishes the rate and cap by September 1 each year [US-NYP8-001].
- **Withholding tables:** republished as the law changes; no 2027 change announced [US-NYS5-020].

## NY.12 Payroll data protection and records

- **Labor Law 203-d [US-NYS5-009]:** public display of SSNs prohibited ([[FACT:ny.data.ssn.public_display_prohibited=True]]); no SSN on badges or time cards; no SSN in unrestricted files. The SSN is not a required pay-statement item. UI information is confidential under UI Law 537 [US-NYS5-010].

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.data.ssn.public_display_prohibited` | [[FACT:ny.data.ssn.public_display_prohibited=True]] |  | from 2026-01-01 | US-NYS5-009 | Labor Law 203-d |

## NY.13 Live legal change

- **2026-01-01:** new NYS and Yonkers withholding tables (NYC unchanged) [US-NYS5-020]; minimum wage and exempt thresholds per Section 1; farm overtime step; UI base under the new formula; PFL 2026 rate and cap.
- **2026-02-22:** NYC Protected Time Off (unpaid immediate hours, prenatal leave, pay-statement items) [US-NYB5-003].
- **2026-07-03:** Labor Law 193 revision published; 2028-11-06 sunset visible [US-NYS5-005].
- **2027-01-01:** minimum wage frozen by off-ramp; home care aide rates; PFL 2027 rate and cap [US-NYS5-001, US-NYB5-001]. No 2027 withholding change announced [US-NYS5-020].

## NY.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## NY.15 Special populations

| Population | New York rule | Register id |
|---|---|---|
| Domestic / household | Overtime threshold for domestic workers (higher for live-in); UI and wage reporting above a quarterly cash-wage test; income tax withholding voluntary; registration via NYBE | US-NYS5-013, US-NYS5-010 |
| Agricultural | Farm minimum wage per region; overtime threshold [[FACT:ny.labour.overtime.farm.threshold_hours=52]] hours in 2026; H-2A excluded from UI; direct-deposit consent rule does not apply | US-NYS5-012, US-NYS5-010, US-NYS5-004 |
| Minors | Employment certificate for 16-17 year olds; no youth minimum wage found; withholding exemption if no liability (671(a)(3)); daytime school students excluded from UI except nonprofit and government employers | US-NYS5-014, US-NYS5-010 |
| Tipped | Cash wages per Section 1 (hospitality only); tips are UI remuneration | US-NYS5-001, US-NYS5-010 |
| Clergy / religious | Ministers and religious-order members excluded from UI for nonprofits; income tax follows the federal wage definition | US-NYS5-010 |
| Students | 671(a)(3) exemption for full-time students with no liability; UI exclusions for own-school employment, work-study and camp students | US-NYS5-010 |
| Nonresident aliens | Treaty-exempt under IRS rules = exempt for NYS, NYC and Yonkers with no extra form; new-hire report runs from SSN issue | US-NYS5-010 |
| Statutory employees | No state rule beyond the federal one; the business directing the work is liable for UI on misclassified workers | US-NYS5-010 |
| Government employees | 414(h) addback; nonprofit and government employers may use the UI reimbursement option | US-NYS5-019, US-NYS5-010 |

## NY.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## NY.S Sources

Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file. Authorities:

- Build lead (Claude) under owner delegation (Wallisson Gomes): US-OWN-006, US-OWN-007
- NY Department of Labor / DTF: US-NY-007
- NY Department of Taxation and Finance: US-NY-001, US-NY-003, US-NY-008, US-NY-009, US-NY-013, US-NYP52-002, US-NYS5-019, US-NYS5-020, US-NYV6-001, US-NYV6-004, US-NYV7-001, US-NYV7-002, US-NYV7-003
- NY Department of Taxation and Finance / NY Department of Labor: US-NYS5-010
- NY Senate (consolidated laws): US-NYB5-401
- NY State Senate (consolidated laws): US-NYS5-002, US-NYS5-003, US-NYS5-004, US-NYS5-005, US-NYS5-006, US-NYS5-007, US-NYS5-008, US-NYS5-009, US-NYS5-013, US-NYS5-014, US-NYS5-015, US-NYS5-016, US-NYS5-021
- NY State Senate (official): US-NYP51-002, US-NYP51-003
- NY official authority: US-NYP7-001, US-NYP7-004
- NYC Department of Consumer and Worker Protection: US-NYB5-003
- NYS Dept of Taxation and Finance: US-FIL-007
- New York State Department of Financial Services: US-NYB5-001, US-NYP8-001
- New York State Department of Labor: US-NYP9V-001, US-NYS5-001, US-NYS5-011, US-NYS5-012, US-NYS5-017, US-NYV6B-002
- New York State Department of Taxation and Finance: US-NYB5-301, US-NYB5-302
- New York State Paid Family Leave (Workers' Compensation Board / DFS program site): US-NYB5-002
- New York State Senate: US-NYR3C-001
- New York State Senate (Consolidated Laws of New York, official host): US-NYV6-002, US-NYV6-003, US-NYV6-005, US-NYV6-006, US-NYV6B-001
- Owner (Wallisson Gomes): US-OWN-008

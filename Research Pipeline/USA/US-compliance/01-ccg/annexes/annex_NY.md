# Annex NY - New York

Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T3 - state withholding; local layer absent or piggybacked on the state return** (build manifest, tier rationale). NYC and Yonkers taxes are piggybacked on NYS-1 / NYS-45 [US-NY-008].

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC are out of scope (MANDATE, US-OWN-001). Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a key of `_research/CCG-annex_NY-facts.json` and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. `RESEARCH-GAP` marks a point the research has not closed; it is not filled with an estimate.

## 1. Labour code and pay rules

- **Minimum wage (Labor Law 652(1-a)) [US-NYS5-002].** Two regions in 2026: New York City, Nassau, Suffolk and Westchester at [[FACT:ny.labour.minwage.nyc_li_westchester.hourly=17.00]] USD per hour; the rest of the state at [[FACT:ny.labour.minwage.rest_of_state.hourly=16.00]] USD per hour. No municipal minimum-wage ordinance applies: the regions are set by the state law itself.
- **2027.** No increase on 2027-01-01: [[FACT:ny.labour.minwage.next_year_change=none on 2027-01-01 (off-ramp met)]] [US-NYS5-001]. Home care aides from 2027-01-01: [[FACT:ny.labour.minwage.home_care_aide.nyc_li_westchester.hourly=20.00]] USD (NYC, Long Island, Westchester) and [[FACT:ny.labour.minwage.home_care_aide.rest_of_state.hourly=19.00]] USD (rest of state). A proposal to change the off-ramps is not enacted and is not modelled.
- **Overtime (12 NYCRR 142-2.2) [US-NYS5-011].** [[FACT:ny.overtime.premium.multiplier=1.5]] times the regular rate after [[FACT:ny.overtime.weekly_threshold_hours=40]] hours per week; residential employees have a higher weekly threshold (state rule, not modelled as a separate value here). FLSA 13(a)(2)/(4) exemptions are not applied in New York; FLSA-exempt employees other than executive, administrative and professional staff receive overtime at the premium multiple of the minimum rate.
- **Call-in pay and spread of hours.** Call-in pay of [[FACT:ny.labour.call_in_pay.hours=4]] hours, or the scheduled shift if shorter. Where the spread of hours exceeds [[FACT:ny.labour.spread_of_hours.threshold_hours=10]] hours, or on a split shift, one extra hour at the minimum rate is due [US-NYS5-011].
- **Exempt salary thresholds from 2026-01-01** (executive and administrative): [[FACT:ny.labour.exempt_salary.nyc_li_westchester.weekly=1,275.00]] USD per week in NYC, Long Island and Westchester; [[FACT:ny.labour.exempt_salary.rest_of_state.weekly=1,199.10]] USD per week in the rest of the state [US-NYS5-011].
- **Farm workers.** Overtime after [[FACT:ny.labour.overtime.farm.threshold_hours=52]] hours per week from 2026-01-01; the threshold steps down in later years under the phase-in [US-NYS5-012]. Domestic workers: overtime threshold per US-NYS5-013 (higher for live-in workers).
- **Pay frequency (Labor Law 191) [US-NYS5-003].** Manual workers: [[FACT:ny.labour.pay_frequency.manual=weekly, max 7 days after week end]]; semi-monthly only with commissioner authorisation or for nonprofits. Clerical and other workers: at least semi-monthly on regular paydays fixed in advance. Commission salespersons: at least monthly under a written agreement. Damages for a first manual-worker frequency violation are limited to lost interest where pay was at least semi-monthly (198, revision of 2025-05-16) [US-NYS5-021].
- **Method of payment (192).** Direct deposit requires the employee's advance written consent (consent required: [[FACT:ny.labour.direct_deposit.consent_required=True]]); higher-paid executive, administrative and professional staff and farm workers are exempt from the consent rule [US-NYS5-004]. Pay-card rules: see the open point below.
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

**Open research points**

- ⚠️ RESEARCH-GAP: `ny.labour.paycard` (non-blocking; research request filed under this key) - 12 NYCRR Part 192 not read. Closes with: DOL CR 192 copy.

## 2. Income tax withholding (state and local)

- **Withholding method [US-NY-001].** [[FACT:ny.wh.method=NYS-50-T-NYS (1/26): Method I tables, Method II exact calculation, Method III top income]]. Method III (top income) applies when annualised net wages reach [[FACT:ny.pit.top_income.threshold.annual=1,077,550]] USD.
- **Withholding schedules are not statutory brackets.** The Method II rate schedules (single and married, with recapture bands) are withholding schedules published in NYS-50-T-NYS; the build uses the publication's tables and formula, never the statutory brackets of Tax Law 601. The WTC references NYS-50-T-NYS only.
- **Certificate [US-NYS5-010].** [[FACT:ny.wh.certificate=IT-2104; 2020+ W-4 without IT-2104 = zero allowances]]. An exempt certificate is available under Tax Law 671(a)(3) (minors, older employees and full-time students with no liability).
- **Exemption allowance:** [[FACT:ny.pit.exemption.annual=1000]] USD per year per allowance [US-NY-001].
- **Supplemental wages.** New York State supplemental rate [[FACT:ny.pit.supplemental.nys.rate=11.7]] %, or the aggregate method [US-NY-001, US-NYS5-010]. The NYC and Yonkers supplemental rates are not stated here (open point below).
- **Rounding:** [[FACT:ny.pit.rounding=to the cent per tables or formula]] [US-NY-001]. Oracle (NYS-50-T-NYS Method II worked examples): example 1 = [[FACT:ny.pit.oracle.example_1.withholding=8.01]] USD; example 3 = [[FACT:ny.pit.oracle.example_3.withholding=3,576.63]] USD; example 4 = [[FACT:ny.pit.oracle.example_4.withholding=44.10]] USD, all reproduced exactly. Example 2 is printed as [[FACT:ny.pit.oracle.example_2.withholding=258.51]] USD; half-up rounding gives one cent less (open point below). Recomputation of the examples belongs to Module 12 and the validation suite.
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
| `ny.pit.oracle.example_1.withholding` | [[FACT:ny.pit.oracle.example_1.withholding=8.01]] | USD | 2026-01-01 to 2026-12-31 | US-NY-001 | NYS-50-T-NYS Method II example 1 reproduced exactly (Python Decimal half-up) |
| `ny.pit.oracle.example_3.withholding` | [[FACT:ny.pit.oracle.example_3.withholding=3,576.63]] | USD | 2026-01-01 to 2026-12-31 | US-NY-001 | example 3 reproduced exactly |
| `ny.pit.oracle.example_4.withholding` | [[FACT:ny.pit.oracle.example_4.withholding=44.10]] | USD | 2026-01-01 to 2026-12-31 | US-NY-001 | example 4 reproduced exactly |
| `ny.pit.oracle.example_2.withholding` | [[FACT:ny.pit.oracle.example_2.withholding=258.51]] | USD | 2026-01-01 to 2026-12-31 | US-NY-001 |  |

**Open research points**

- ⚠️ RESEARCH-GAP: `ny.pit.oracle.example2_residual` (non-blocking; research request filed under this key) - NYS-50-T-NYS Method II example 2 is printed as [[FACT:ny.pit.oracle.example_2.withholding=258.51]] USD; half-up rounding of the intermediate rate product gives one cent less, so the booklet's rounding convention is not established. Closes with: DTF statement of the rounding convention, or the DTF withholding calculator result for the same case.
- ⚠️ RESEARCH-GAP: `ny.pit.supplemental.local_rates` (blocking; research request filed under this key) - The NYC resident, Yonkers resident and Yonkers nonresident supplemental withholding rates have no active register row (the row that carried them is superseded and its successor carries only the rounding finding). No local supplemental rate is stated in this annex. Closes with: Re-register the supplemental-rate lines of NYS-50-T-NYC and NYS-50-T-Y (1/26) as an active A.2 row.

## 3. Social insurance and payroll levies

- **State unemployment insurance [US-NYS5-010, US-NYP9V-001].** 2026 taxable wage base [[FACT:ny.sui.wage_base=17,600]] USD (from 2026 indexed to a share of the state average annual wage and never reduced, US-NY-007). New-employer rate [[FACT:ny.sui.new_employer.rate=4.025]] % (normal plus subsidiary), plus the Re-employment Service Fund [[FACT:ny.ui.rsf.rate=0.075]] %. Experience range [[FACT:ny.sui.employer.rate.min=1.625]] % to [[FACT:ny.sui.employer.rate.max=9.425]] %. Employee UI contribution: [[FACT:ny.sui.employee.rate=0]] %. The state UI loan was repaid in the FY2026 budget; the FUTA credit-reduction effect is in Annex FED / MULTI.
- **Paid Family Leave (PFL) [US-NYP8-001, US-NYB5-001].** Employee-paid. 2026: [[FACT:ny.pfl.employee.rate=0.432]] % of wages, annual employee maximum [[FACT:ny.pfl.employee.max_annual=411.91]] USD. 2027 (DFS decision of 2026-08-31): [[FACT:ny.pfl.employee.rate=0.452]] %, maximum [[FACT:ny.pfl.employee.max_annual=451.81]] USD. Benefit [[FACT:ny.pfl.benefit.rate_of_aww=67]] % of the employee's average weekly wage, capped at the same share of the NYSAWW ([[FACT:ny.pfl.nysaww=1,833.63]] USD for 2026), i.e. a 2026 maximum weekly benefit of [[FACT:ny.pfl.benefit.max_weekly=1,228.53]] USD [US-NYB5-002].
- **Disability benefits (DBL) [US-NY-010].** Employee [[FACT:ny.dbl.employee.rate=0.5]] % of wages, capped at [[FACT:ny.dbl.employee.max_weekly=0.60]] USD per week; the employer pays the remaining cost.
- **Employer levies.** MCTMT (MTA-305, quarterly) and the Re-employment Service Fund per the levy census [US-NYP7-001, US-NYP7-004, US-OWN-007]; no MCTMT rate is carried in this annex's facts.

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.sui.wage_base` | [[FACT:ny.sui.wage_base=17,600]] | USD | 2026-01-01 to 2026-12-31 | US-NYS5-010 | 18% of state average annual wage rounded up to 100, never reduced |
| `ny.sui.new_employer.rate` | [[FACT:ny.sui.new_employer.rate=4.025]] | % | 2026-01-01 to 2026-12-31 | US-NYP9V-001 | 3.4 normal + 0.625 subsidiary; + RSF 0.075 = 4.1 |
| `ny.ui.rsf.rate` | [[FACT:ny.ui.rsf.rate=0.075]] | % | 2026-01-01 to 2026-12-31 | US-NYP9V-001 | Re-employment Service Fund |
| `ny.sui.employer.rate.min` | [[FACT:ny.sui.employer.rate.min=1.625]] | % | 2026-01-01 to 2026-12-31 | US-NYP9V-001 |  |
| `ny.sui.employer.rate.max` | [[FACT:ny.sui.employer.rate.max=9.425]] | % | 2026-01-01 to 2026-12-31 | US-NYP9V-001 |  |
| `ny.sui.employee.rate` | [[FACT:ny.sui.employee.rate=0]] | % | from 2026-01-01 | US-NYP9V-001 |  |
| `ny.pfl.employee.rate` | [[FACT:ny.pfl.employee.rate=0.432]] | % | 2026-01-01 to 2026-12-31 | US-NYP8-001 |  |
| `ny.pfl.employee.max_annual` | [[FACT:ny.pfl.employee.max_annual=411.91]] | USD | 2026-01-01 to 2026-12-31 | US-NYP8-001 |  |
| `ny.dbl.employee.rate` | [[FACT:ny.dbl.employee.rate=0.5]] | % | from 2026-01-01 | US-NY-010 | max 0.60/week; employer pays rest |
| `ny.dbl.employee.max_weekly` | [[FACT:ny.dbl.employee.max_weekly=0.60]] | USD | from 2026-01-01 | US-NY-010 |  |
| `ny.pfl.employee.rate` | [[FACT:ny.pfl.employee.rate=0.452]] | % | from 2027-01-01 | US-NYB5-001 |  |
| `ny.pfl.employee.max_annual` | [[FACT:ny.pfl.employee.max_annual=451.81]] | USD | from 2027-01-01 | US-NYB5-001 |  |
| `ny.pfl.nysaww` | [[FACT:ny.pfl.nysaww=1,833.63]] | USD | 2026-01-01 to 2026-12-31 | US-NYB5-002 | New York State Average Weekly Wage used for 2026 PFL benefits; 2027 NYSAWW +4.83% (amount not stated). |
| `ny.pfl.benefit.max_weekly` | [[FACT:ny.pfl.benefit.max_weekly=1,228.53]] | USD | 2026-01-01 to 2026-12-31 | US-NYB5-002 |  |
| `ny.pfl.benefit.rate_of_aww` | [[FACT:ny.pfl.benefit.rate_of_aww=67]] | % | from 2026-01-01 | US-NYB5-002 |  |

**Open research points**

- ⚠️ RESEARCH-GAP: `ny.sui.wage_base.next_year` (non-blocking; research request filed under this key) - 2027 UI base not yet published. Closes with: DOL UI rate page or NYS-50 2027 edition (December 2026).

## 4. Payslip statute and payroll records

- **Content (Labor Law 195(3)), with every payment [US-NYS5-006]:** [[FACT:ny.payslip.items=dates of work; names; employer address/phone; rates and basis; gross; deductions; allowances; net; regular and OT rates and hours (non-exempt); piece rates]]. Prevailing-wage supplements and allowances claimed toward the minimum wage are shown where they apply.
- **NYC Protected Time Off statement** (from 2026-02-22): [[FACT:ny.leave.nyc_pto.pay_statement_items=Each pay period, on the pay statement or other written documentation: PTO accrued in the period; paid and unpaid PTO used in the period; unpaid immediately available hours available in the calendar year; accrued PTO available for use in the calendar year]] [US-NYB5-003].
- **Retention:** payroll records [[FACT:ny.records.retention_years=6]] years (195(4)); tax records per DTF rules [US-NYS5-010].
- **Hire notice** in English and the employee's primary language (195(1)) [US-NYP51-003]; the payslip itself is in English (US-OWN-006).

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.payslip.items` | [[FACT:ny.payslip.items=dates of work; names; employer address/phone; rates and basis; gross; deductions; allowances; net; regular and OT rates and hours (non-exempt); piece rates]] |  | from 2026-01-01 | US-NYS5-006 | Labor Law 195(3) with every payment |
| `ny.records.retention_years` | [[FACT:ny.records.retention_years=6]] | years | from 2026-01-01 | US-NYS5-006 | 195(4); tax records 4 years |

**Open research points**

- ⚠️ RESEARCH-GAP: `ny.payslip.electronic` (non-blocking; research request filed under this key) - DOL position on electronic wage statements not read. Closes with: DOL wage-statement FAQ.

## 5. Statutory reporting

- **NYS-45** (quarterly, combined withholding, wage reporting and UI), due [[FACT:ny.report.nys45.due=Apr 30; Jul 31; Oct 31; Jan 31]]; Parts A, B and C mandatory; e-file and electronic payment mandatory [US-NYS5-010]. Upload specification Pub 72.5 [US-FIL-007].
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

**Open research points**

- ⚠️ RESEARCH-GAP: `ny.report.nys45_annual` (non-blocking; research request filed under this key) - Q4 NYS-45 annual reconciliation mechanics not read. Closes with: NYS-45-I instructions (DTF).

## 6. Leave

- **State paid sick leave (Labor Law 196-b) [US-NYS5-007].** Medium employers (band `5_99` of the key): [[FACT:ny.leave.paid_sick.annual_hours.5_99=40]] hours paid; large employers (band `100plus`): [[FACT:ny.leave.paid_sick.annual_hours.100plus=56]] hours paid; the smallest employers owe unpaid leave unless net income exceeds the statutory amount (196-b). Accrual one hour per [[FACT:ny.leave.paid_sick.accrual_ratio_hours_worked=30]] hours worked; front-loading allowed; paid at the regular rate (or minimum wage if higher); carry-over required, use may be capped; no payout at separation.
- **Paid prenatal leave:** [[FACT:ny.leave.prenatal.hours_per_52_weeks=20]] hours per rolling year, paid at the regular rate, no payout [US-NYS5-007].
- **NYC Protected Time Off (from 2026-02-22) [US-NYB5-003].** Paid PTO up to [[FACT:ny.leave.nyc_pto.paid_hours.max.under100=40]] hours (employers below the large-employer band) or [[FACT:ny.leave.nyc_pto.paid_hours.max.100plus=56]] hours (large employers); plus [[FACT:ny.leave.nyc_pto.unpaid_hours_immediate=32]] hours of unpaid PTO available at hire and on the first day of each calendar year (no proration, no carry-over required); plus [[FACT:ny.leave.nyc_pto.prenatal_paid_hours=20]] hours of paid prenatal leave per rolling year.
- **PFL benefits** are paid by the insurer, not by the employer as wages (see Section 3).

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.leave.paid_sick.annual_hours.5_99` | [[FACT:ny.leave.paid_sick.annual_hours.5_99=40]] | hours | from 2025-01-01 | US-NYS5-007 | 196-b; 4 or fewer: 40 unpaid (paid if net income >1M); 100+: 56 paid |
| `ny.leave.paid_sick.annual_hours.100plus` | [[FACT:ny.leave.paid_sick.annual_hours.100plus=56]] | hours | from 2025-01-01 | US-NYS5-007 |  |
| `ny.leave.paid_sick.accrual_ratio_hours_worked` | [[FACT:ny.leave.paid_sick.accrual_ratio_hours_worked=30]] | hours | from 2025-01-01 | US-NYS5-007 | no payout at separation |
| `ny.leave.prenatal.hours_per_52_weeks` | [[FACT:ny.leave.prenatal.hours_per_52_weeks=20]] | hours | from 2025-01-01 | US-NYS5-007 | paid; no payout |
| `ny.leave.nyc_pto.unpaid_hours_immediate` | [[FACT:ny.leave.nyc_pto.unpaid_hours_immediate=32]] | hours | from 2026-02-22 | US-NYB5-003 | Available at hire and again on the first day of each calendar year; no proration, no carryover required. |
| `ny.leave.nyc_pto.paid_hours.max.under100` | [[FACT:ny.leave.nyc_pto.paid_hours.max.under100=40]] | hours | from 2026-02-22 | US-NYB5-003 | Employers with 99 or fewer employees. |
| `ny.leave.nyc_pto.paid_hours.max.100plus` | [[FACT:ny.leave.nyc_pto.paid_hours.max.100plus=56]] | hours | from 2026-02-22 | US-NYB5-003 |  |
| `ny.leave.nyc_pto.prenatal_paid_hours` | [[FACT:ny.leave.nyc_pto.prenatal_paid_hours=20]] | hours | from 2026-02-22 | US-NYB5-003 | Per 52 weeks, no accrual (separate from PTO). |
| `ny.leave.nyc_pto.pay_statement_items` | [[FACT:ny.leave.nyc_pto.pay_statement_items=Each pay period, on the pay statement or other written documentation: PTO accrued in the period; paid and unpaid PTO used in the period; unpaid immediately available hours available in the calendar year; accrued PTO available for use in the calendar year]] |  | from 2026-02-22 | US-NYB5-003 |  |

## 7. Termination

- **Final pay:** [[FACT:ny.final_pay.rule=next regular payday (discharge and resignation)]]; by mail on request (191(3)) [US-NYS5-003].
- **Written termination notice** stating the exact termination date and the benefits cancellation date within [[FACT:ny.term.notice.working_days=5]] working days (195(6)) [US-NYS5-006].
- **UI separation notice:** [[FACT:ny.term.ui_notice.form=IA 12.3 to every separated worker or hours cut to 30 or fewer]] [US-NYS5-017]; timing rule open (below).
- **Accrued vacation:** no statutory payout; a "wage supplement" under 198-c payable per policy or agreement [US-NYS5-008]. Unused sick and prenatal leave: no payout [US-NYS5-007]. NY WARN is not a payroll calculation and is not covered.

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.final_pay.rule` | [[FACT:ny.final_pay.rule=next regular payday (discharge and resignation)]] |  | from 2026-01-01 | US-NYS5-003 | 191(3) |
| `ny.term.notice.working_days` | [[FACT:ny.term.notice.working_days=5]] | days | from 2026-01-01 | US-NYS5-006 | written notice of termination date and benefits cancellation (195(6)) |
| `ny.term.ui_notice.form` | [[FACT:ny.term.ui_notice.form=IA 12.3 to every separated worker or hours cut to 30 or fewer]] |  | from 2026-01-01 | US-NYS5-017 |  |

**Open research points**

- ⚠️ RESEARCH-GAP: `ny.term.ia12_3.timing` (non-blocking; research request filed under this key) - The timing rule for the UI separation notice named in `ny.term.ui_notice.form` (12 NYCRR 472.8) was not read. Closes with: Text of 12 NYCRR 472.8.

## 8. Benefits in kind and the taxable base

- **Conformity.** The New York return starts from federal wages (W-2 box 1), so the federal exclusions (401(k), 403(b), 457, cafeteria plans, HSA, transit, group-term life) carry over.
- **Departure:** 414(h) contributions of New York public employees are added back (addback applies: [[FACT:ny.bik.414h.addback=True]]) [US-NYS5-019]. UI remuneration includes the reasonable value of meals and lodging, and tips [US-NYS5-010].

**Parameters (benefits in kind and the taxable base)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.bik.414h.addback` | [[FACT:ny.bik.414h.addback=True]] |  | from 2025-01-01 | US-NYS5-019 | NY public employees |

**Open research points**

- ⚠️ RESEARCH-GAP: `ny.bik.nyc_flex125_addback` (non-blocking; research request filed under this key) - The NYC flexible-benefits (cafeteria plan) addback for NYC employees was not read. Closes with: DTF addback-modification instructions for New York City flexible benefits.

## 9. Deductions and garnishments

- **Authorised deductions (Labor Law 193) [US-NYS5-005].** Only deductions required by law or voluntarily authorised in writing within the listed categories; authorisations kept for the employment plus the retention period; overpayment and advance recovery follow DOL regulations. The expanded text carries a sunset of 2028-11-06.
- **Creditor income execution (CPLR 5231) [US-NYS5-015].** At most [[FACT:ny.garn.consumer.max_rate_of_gross=10]] % of gross, never more than the federal disposable-earnings cap; the deduction may not reduce weekly disposable earnings below the statutory floor (thirty times the higher of the federal or New York minimum wage; regional rate open, below). No income execution for medical-debt judgments.
- **Support (CPLR 5241) [US-NYS5-016].** Start no later than the first pay period after service; remit to the SDU within [[FACT:ny.garn.support.remit_business_days=7]] business days of payday; CCPA percentage limits (Annex FED); support takes priority; multiple orders prorated; order current support, health premium, arrears; notify the issuer on termination.

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.garn.consumer.max_rate_of_gross` | [[FACT:ny.garn.consumer.max_rate_of_gross=10]] | % | from 2026-01-01 | US-NYS5-015 | CPLR 5231; never >25% disposable; floor 30x greater of federal or NY minimum |
| `ny.garn.support.remit_business_days` | [[FACT:ny.garn.support.remit_business_days=7]] | days | from 2026-01-01 | US-NYS5-016 | CPLR 5241 |

**Open research points**

- ⚠️ RESEARCH-GAP: `ny.garn.consumer.floor_region` (non-blocking; research request filed under this key) - Whether the CPLR 5231 floor uses the regional Labor Law 652 rate or the rest-of-state rate is not established. Closes with: DOL or court guidance, or the income execution form text.
- ⚠️ RESEARCH-GAP: `ny.garn.state_tax_levy` (non-blocking; research request filed under this key) - DTF income execution for tax warrants not researched. Closes with: Tax Law 692 / CPLR 5231 guidance.

## 10. Collective agreements and prevailing wage

- **Prevailing wage:** exists ([[FACT:ny.prevailing_wage.exists=True]]); Labor Law 220 public-work rates and supplements [US-NYP51-002]. The pay statement must identify prevailing-wage supplements [US-NYS5-006]. Certified-payroll mechanics are not modelled.

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.prevailing_wage.exists` | [[FACT:ny.prevailing_wage.exists=True]] |  | from 2026-01-01 | US-NYP51-002 | Labor Law 220 |

## 11. Indexation

- **Minimum wage:** from 2027 indexed to the three-year average of the August-July CPI-W Northeast, subject to off-ramps; published by October 1 [US-NYS5-002]. For 2027 the off-ramp was met (no increase) [US-NYS5-001].
- **Exempt thresholds and meal/lodging credits** move with the minimum-wage orders (652(2)) [US-NYS5-011].
- **UI wage base:** indexed to the state average annual wage [US-NYS5-010]; 2027 value open (Section 3).
- **PFL:** DFS publishes the rate and cap by September 1 each year [US-NYP8-001].
- **Withholding tables:** reissued as the law changes; no 2027 change announced [US-NYS5-020].

## 12. Payroll data protection

- **Labor Law 203-d [US-NYS5-009]:** public display of SSNs prohibited ([[FACT:ny.data.ssn.public_display_prohibited=True]]); no SSN on badges or time cards; no SSN in unrestricted files. The SSN is not a required pay-statement item. UI information is confidential under UI Law 537 [US-NYS5-010].

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ny.data.ssn.public_display_prohibited` | [[FACT:ny.data.ssn.public_display_prohibited=True]] |  | from 2026-01-01 | US-NYS5-009 | Labor Law 203-d |

## 13. Live legal change

- **2026-01-01:** new NYS and Yonkers withholding tables (NYC unchanged) [US-NYS5-020]; minimum wage and exempt thresholds per Section 1; farm overtime step; UI base under the new formula; PFL 2026 rate and cap.
- **2026-02-22:** NYC Protected Time Off (unpaid immediate hours, prenatal leave, pay-statement items) [US-NYB5-003].
- **2026-07-03:** Labor Law 193 revision published; 2028-11-06 sunset visible [US-NYS5-005].
- **2027-01-01:** minimum wage frozen by off-ramp; home care aide rates; PFL 2027 rate and cap [US-NYS5-001, US-NYB5-001]. No 2027 withholding change announced [US-NYS5-020].

## 14. Special populations

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

## 15. Sources

Register ids cited in this annex resolve to `00-official-sources/legal-basis-register.csv`; the URL of each value is in the facts file. Authorities:

- NY Department of Taxation and Finance: US-NY-001, US-NY-008, US-NY-013, US-NYS5-019
- NY Department of Taxation and Finance / NY Department of Labor: US-NYS5-010
- NY Senate (consolidated laws): US-NY-010
- NY State Senate (consolidated laws): US-NYS5-002, US-NYS5-003, US-NYS5-004, US-NYS5-006, US-NYS5-007, US-NYS5-009, US-NYS5-015, US-NYS5-016
- NY State Senate (official): US-NYP51-002
- NYC Department of Consumer and Worker Protection: US-NYB5-003
- New York State Department of Financial Services: US-NYB5-001, US-NYP8-001
- New York State Department of Labor: US-NYP9V-001, US-NYS5-001, US-NYS5-011, US-NYS5-012, US-NYS5-017
- New York State Paid Family Leave (Workers' Compensation Board / DFS program site): US-NYB5-002

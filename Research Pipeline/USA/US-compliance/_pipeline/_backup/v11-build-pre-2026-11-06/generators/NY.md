## @labour
- **Minimum wage (Labor Law 652(1-a)) [US-NYS5-002].** Two regions in 2026: New York City, Nassau, Suffolk and Westchester at {{ny.labour.minwage.nyc_li_westchester.hourly}} USD per hour; the rest of the state at {{ny.labour.minwage.rest_of_state.hourly}} USD per hour. No municipal minimum-wage ordinance applies: the regions are set by the state law itself.
- **2027.** No increase on 2027-01-01: {{ny.labour.minwage.next_year_change}} [US-NYS5-001]. Home care aides from 2027-01-01: {{ny.labour.minwage.home_care_aide.nyc_li_westchester.hourly}} USD (NYC, Long Island, Westchester) and {{ny.labour.minwage.home_care_aide.rest_of_state.hourly}} USD (rest of state). A proposal to change the off-ramps is not enacted and is not modelled.
- **Overtime (12 NYCRR 142-2.2) [US-NYS5-011].** {{ny.overtime.premium.multiplier}} times the regular rate after {{ny.overtime.weekly_threshold_hours}} hours per week; residential employees have a higher weekly threshold (state rule, not modelled as a separate value here). FLSA 13(a)(2)/(4) exemptions are not applied in New York; FLSA-exempt employees other than executive, administrative and professional staff receive overtime at the premium multiple of the minimum rate.
- **Call-in pay and spread of hours.** Call-in pay of {{ny.labour.call_in_pay.hours}} hours, or the scheduled shift if shorter. Where the spread of hours exceeds {{ny.labour.spread_of_hours.threshold_hours}} hours, or on a split shift, one extra hour at the minimum rate is due [US-NYS5-011].
- **Exempt salary thresholds from 2026-01-01** (executive and administrative): {{ny.labour.exempt_salary.nyc_li_westchester.weekly}} USD per week in NYC, Long Island and Westchester; {{ny.labour.exempt_salary.rest_of_state.weekly}} USD per week in the rest of the state [US-NYS5-011].
- **Farm workers.** Overtime after {{ny.labour.overtime.farm.threshold_hours}} hours per week from 2026-01-01; the threshold steps down in later years under the phase-in [US-NYS5-012]. Domestic workers: overtime threshold per US-NYS5-013 (higher for live-in workers).
- **Pay frequency (Labor Law 191) [US-NYS5-003].** Manual workers: {{ny.labour.pay_frequency.manual}}; semi-monthly only with commissioner authorisation or for nonprofits. Clerical and other workers: at least semi-monthly on regular paydays fixed in advance. Commission salespersons: at least monthly under a written agreement. Damages for a first manual-worker frequency violation are limited to lost interest where pay was at least semi-monthly (198, revision of 2025-05-16) [US-NYS5-021].
- **Method of payment (192).** Direct deposit requires the employee's advance written consent (consent required: {{ny.labour.direct_deposit.consent_required}}); higher-paid executive, administrative and professional staff and farm workers are exempt from the consent rule [US-NYS5-004]. Pay-card rules: see the open point below.
- **Tipped employees (hospitality only) [US-NYS5-001].** Minimum cash wage, service employees: {{ny.labour.tip_credit.service.nyc_li_westchester.cash_wage}} USD (NYC/LI/Westchester), {{ny.labour.tip_credit.service.rest_of_state.cash_wage}} USD (rest of state). Food-service workers: {{ny.labour.tip_credit.food_service.nyc_li_westchester.cash_wage}} USD and {{ny.labour.tip_credit.food_service.rest_of_state.cash_wage}} USD. The tip credit is the regional minimum wage minus the cash wage.
- **Meal credit toward the minimum wage:** {{ny.labour.meal_credit.nyc_li_westchester.per_meal}} USD per meal in NYC/LI/Westchester [US-NYS5-011]. Lodging and uniform-maintenance credits for 2026 are listed in Minimum Wage Order Part 142 (US-NYS5-011); they are not carried as facts and are not modelled.

## @income_tax
- **Withholding method [US-NY-001].** {{ny.wh.method}}. Method III (top income) applies when annualised net wages reach {{ny.pit.top_income.threshold.annual}} USD.
- **Withholding schedules are not statutory brackets.** The Method II rate schedules (single and married, with recapture bands) are withholding schedules published in NYS-50-T-NYS; the build uses the publication's tables and formula, never the statutory brackets of Tax Law 601. The WTC references NYS-50-T-NYS only.
- **Certificate [US-NYS5-010].** {{ny.wh.certificate}}. An exempt certificate is available under Tax Law 671(a)(3) (minors, older employees and full-time students with no liability).
- **Exemption allowance:** {{ny.pit.exemption.annual}} USD per year per allowance [US-NY-001].
- **Supplemental wages.** New York State supplemental rate {{ny.pit.supplemental.nys.rate}} %, or the aggregate method [US-NY-001, US-NYS5-010]. Local supplemental rates (method (a); or the aggregate method): New York City {{ny.local.nyc.supplemental.rate}} %, Yonkers resident {{ny.local.yonkers.resident.supplemental.rate}} %, Yonkers nonresident {{ny.local.yonkers.nonresident.supplemental.rate}} % [US-NYB5-301, US-NYB5-302].
- **Rounding:** {{ny.pit.rounding}} [US-NY-001]. Oracle (NYS-50-T-NYS Method II worked examples): example 1 = {{ny.pit.oracle.example_1.withholding}} USD; example 3 = {{ny.pit.oracle.example_3.withholding}} USD; example 4 = {{ny.pit.oracle.example_4.withholding}} USD, all reproduced exactly. Example 2 is printed as {{ny.pit.oracle.example_2.withholding}} USD; half-up rounding gives one cent less (open point below). Recomputation of the examples belongs to Module 12 and the validation suite.
- **Method II exact calculation, New York State [US-NYV7-001].** {{ny.wh.method2.annualisation}} Allowances: deduction allowance {{ny.wh.method2.single.deduction_allowance}} USD (single) or {{ny.wh.method2.married.deduction_allowance}} USD (married) per year, plus {{ny.wh.method2.exemption_allowance}} USD per year for each exemption claimed (Tables A and B; per-period amounts are printed in the publication). Annual Tax Rate Schedules (Table C), applied as (net wages - column 3) x column 4 + column 5:

**NYS Method II annual schedule, single**

| Line | Net wages at least (column 3) | Rate (column 4) | Add (column 5) |
|---|---|---|---|
| 1 | USD {{ny.wh.method2.single.bracket.1.floor}} | {{ny.wh.method2.single.bracket.1.rate}} % | USD {{ny.wh.method2.single.bracket.1.base}} |
| 2 | USD {{ny.wh.method2.single.bracket.2.floor}} | {{ny.wh.method2.single.bracket.2.rate}} % | USD {{ny.wh.method2.single.bracket.2.base}} |
| 3 | USD {{ny.wh.method2.single.bracket.3.floor}} | {{ny.wh.method2.single.bracket.3.rate}} % | USD {{ny.wh.method2.single.bracket.3.base}} |
| 4 | USD {{ny.wh.method2.single.bracket.4.floor}} | {{ny.wh.method2.single.bracket.4.rate}} % | USD {{ny.wh.method2.single.bracket.4.base}} |
| 5 | USD {{ny.wh.method2.single.bracket.5.floor}} | {{ny.wh.method2.single.bracket.5.rate}} % | USD {{ny.wh.method2.single.bracket.5.base}} |
| 6 | USD {{ny.wh.method2.single.bracket.6.floor}} | {{ny.wh.method2.single.bracket.6.rate}} % | USD {{ny.wh.method2.single.bracket.6.base}} |
| 7 | USD {{ny.wh.method2.single.bracket.7.floor}} | {{ny.wh.method2.single.bracket.7.rate}} % | USD {{ny.wh.method2.single.bracket.7.base}} |
| 8 | USD {{ny.wh.method2.single.bracket.8.floor}} | {{ny.wh.method2.single.bracket.8.rate}} % | USD {{ny.wh.method2.single.bracket.8.base}} |
| 9 | USD {{ny.wh.method2.single.bracket.9.floor}} | {{ny.wh.method2.single.bracket.9.rate}} % | USD {{ny.wh.method2.single.bracket.9.base}} |
| 10 | USD {{ny.wh.method2.single.bracket.10.floor}} | {{ny.wh.method2.single.bracket.10.rate}} % | USD {{ny.wh.method2.single.bracket.10.base}} |

**NYS Method II annual schedule, married**

| Line | Net wages at least (column 3) | Rate (column 4) | Add (column 5) |
|---|---|---|---|
| 1 | USD {{ny.wh.method2.married.bracket.1.floor}} | {{ny.wh.method2.married.bracket.1.rate}} % | USD {{ny.wh.method2.married.bracket.1.base}} |
| 2 | USD {{ny.wh.method2.married.bracket.2.floor}} | {{ny.wh.method2.married.bracket.2.rate}} % | USD {{ny.wh.method2.married.bracket.2.base}} |
| 3 | USD {{ny.wh.method2.married.bracket.3.floor}} | {{ny.wh.method2.married.bracket.3.rate}} % | USD {{ny.wh.method2.married.bracket.3.base}} |
| 4 | USD {{ny.wh.method2.married.bracket.4.floor}} | {{ny.wh.method2.married.bracket.4.rate}} % | USD {{ny.wh.method2.married.bracket.4.base}} |
| 5 | USD {{ny.wh.method2.married.bracket.5.floor}} | {{ny.wh.method2.married.bracket.5.rate}} % | USD {{ny.wh.method2.married.bracket.5.base}} |
| 6 | USD {{ny.wh.method2.married.bracket.6.floor}} | {{ny.wh.method2.married.bracket.6.rate}} % | USD {{ny.wh.method2.married.bracket.6.base}} |
| 7 | USD {{ny.wh.method2.married.bracket.7.floor}} | {{ny.wh.method2.married.bracket.7.rate}} % | USD {{ny.wh.method2.married.bracket.7.base}} |
| 8 | USD {{ny.wh.method2.married.bracket.8.floor}} | {{ny.wh.method2.married.bracket.8.rate}} % | USD {{ny.wh.method2.married.bracket.8.base}} |
| 9 | USD {{ny.wh.method2.married.bracket.9.floor}} | {{ny.wh.method2.married.bracket.9.rate}} % | USD {{ny.wh.method2.married.bracket.9.base}} |
| 10 | USD {{ny.wh.method2.married.bracket.10.floor}} | {{ny.wh.method2.married.bracket.10.rate}} % | USD {{ny.wh.method2.married.bracket.10.base}} |
| 11 | USD {{ny.wh.method2.married.bracket.11.floor}} | {{ny.wh.method2.married.bracket.11.rate}} % | USD {{ny.wh.method2.married.bracket.11.base}} |
| 12 | USD {{ny.wh.method2.married.bracket.12.floor}} | {{ny.wh.method2.married.bracket.12.rate}} % | USD {{ny.wh.method2.married.bracket.12.base}} |

- **Method III, top income [US-NYV7-001].** {{ny.wh.method3.annualisation}} Method III applies when annualised Method II net wages are at least {{ny.wh.method3.single.threshold}} USD (single) or {{ny.wh.method3.married.threshold}} USD (married). Rates (column 3):

| Status | Annualised net wages at least | Rate |
|---|---|---|
| Single | USD {{ny.wh.method3.single.bracket.1.floor}} | {{ny.wh.method3.single.bracket.1.rate}} % |
| Single | USD {{ny.wh.method3.single.bracket.2.floor}} | {{ny.wh.method3.single.bracket.2.rate}} % |
| Single | USD {{ny.wh.method3.single.bracket.3.floor}} | {{ny.wh.method3.single.bracket.3.rate}} % |
| Married | USD {{ny.wh.method3.married.bracket.1.floor}} | {{ny.wh.method3.married.bracket.1.rate}} % |
| Married | USD {{ny.wh.method3.married.bracket.2.floor}} | {{ny.wh.method3.married.bracket.2.rate}} % |
| Married | USD {{ny.wh.method3.married.bracket.3.floor}} | {{ny.wh.method3.married.bracket.3.rate}} % |

- **New York City resident withholding, Method II [US-NYV7-002].** {{ny.local.nyc.method2.annualisation}} Allowances: {{ny.local.nyc.method2.single.deduction_allowance}} USD (single) or {{ny.local.nyc.method2.married.deduction_allowance}} USD (married) per year, plus {{ny.local.nyc.method2.exemption_allowance}} USD per exemption. NYC annual schedules, same formula:

| Line | Single: net wages at least | Single: rate | Single: add | Married: net wages at least | Married: rate | Married: add |
|---|---|---|---|---|---|---|
| 1 | USD {{ny.local.nyc.method2.single.bracket.1.floor}} | {{ny.local.nyc.method2.single.bracket.1.rate}} % | USD {{ny.local.nyc.method2.single.bracket.1.base}} | USD {{ny.local.nyc.method2.married.bracket.1.floor}} | {{ny.local.nyc.method2.married.bracket.1.rate}} % | USD {{ny.local.nyc.method2.married.bracket.1.base}} |
| 2 | USD {{ny.local.nyc.method2.single.bracket.2.floor}} | {{ny.local.nyc.method2.single.bracket.2.rate}} % | USD {{ny.local.nyc.method2.single.bracket.2.base}} | USD {{ny.local.nyc.method2.married.bracket.2.floor}} | {{ny.local.nyc.method2.married.bracket.2.rate}} % | USD {{ny.local.nyc.method2.married.bracket.2.base}} |
| 3 | USD {{ny.local.nyc.method2.single.bracket.3.floor}} | {{ny.local.nyc.method2.single.bracket.3.rate}} % | USD {{ny.local.nyc.method2.single.bracket.3.base}} | USD {{ny.local.nyc.method2.married.bracket.3.floor}} | {{ny.local.nyc.method2.married.bracket.3.rate}} % | USD {{ny.local.nyc.method2.married.bracket.3.base}} |
| 4 | USD {{ny.local.nyc.method2.single.bracket.4.floor}} | {{ny.local.nyc.method2.single.bracket.4.rate}} % | USD {{ny.local.nyc.method2.single.bracket.4.base}} | USD {{ny.local.nyc.method2.married.bracket.4.floor}} | {{ny.local.nyc.method2.married.bracket.4.rate}} % | USD {{ny.local.nyc.method2.married.bracket.4.base}} |
| 5 | USD {{ny.local.nyc.method2.single.bracket.5.floor}} | {{ny.local.nyc.method2.single.bracket.5.rate}} % | USD {{ny.local.nyc.method2.single.bracket.5.base}} | USD {{ny.local.nyc.method2.married.bracket.5.floor}} | {{ny.local.nyc.method2.married.bracket.5.rate}} % | USD {{ny.local.nyc.method2.married.bracket.5.base}} |
| 6 | USD {{ny.local.nyc.method2.single.bracket.6.floor}} | {{ny.local.nyc.method2.single.bracket.6.rate}} % | USD {{ny.local.nyc.method2.single.bracket.6.base}} | USD {{ny.local.nyc.method2.married.bracket.6.floor}} | {{ny.local.nyc.method2.married.bracket.6.rate}} % | USD {{ny.local.nyc.method2.married.bracket.6.base}} |

- **Yonkers resident surcharge [US-NYV7-003].** {{ny.local.yonkers.resident.surcharge.method}} Rate: {{ny.local.yonkers.resident.surcharge.rate}} % of the New York State amount withheld.
- **Yonkers nonresident earnings tax [US-NYV7-003].** {{ny.local.yonkers.nonresident.earnings_tax.method}} Rate {{ny.local.yonkers.nonresident.earnings_tax.rate}} %; no withholding where Yonkers wages are expected to be below {{ny.local.yonkers.nonresident.no_withholding.below}} USD. Method VIII exclusion table (annualised gross wages):

| Line | Annualised wages at least | Exclusion |
|---|---|---|
| 1 | USD {{ny.local.yonkers.nonresident.method8.bracket.1.floor}} | no withholding (see the threshold above) |
| 2 | USD {{ny.local.yonkers.nonresident.method8.bracket.2.floor}} | USD {{ny.local.yonkers.nonresident.method8.bracket.2.exclusion}} |
| 3 | USD {{ny.local.yonkers.nonresident.method8.bracket.3.floor}} | USD {{ny.local.yonkers.nonresident.method8.bracket.3.exclusion}} |
| 4 | USD {{ny.local.yonkers.nonresident.method8.bracket.4.floor}} | USD {{ny.local.yonkers.nonresident.method8.bracket.4.exclusion}} |
| 5 | USD {{ny.local.yonkers.nonresident.method8.bracket.5.floor}} | USD {{ny.local.yonkers.nonresident.method8.bracket.5.exclusion}} |

- **Method II rounding.** The Method II steps end at the sum to withhold and print no rounding instruction; amounts are carried to the cent, but the rounding convention for the last cent is an open research point (below), and no convention is assumed in this guide.
- **Local income taxes (T3 piggyback) [US-NY-008, US-NYS5-010].** NYC: {{ny.pit.local.nyc.basis}}. Yonkers: resident surcharge, and nonresident earnings tax on work performed in Yonkers; no Yonkers nonresident withholding is needed where Yonkers wages are expected to be {{ny.pit.local.yonkers.nonresident_threshold}} USD or less. The NYC tables did not change for 2026; the NYS and Yonkers tables did [US-NYS5-020].
- **Resident and nonresident matrix.**

| Income type | Resident of New York | Nonresident |
|---|---|---|
| Regular salary | Withheld on all wages wherever earned, NYS-50-T-NYS | Withheld on New York-source wages only, allocated on IT-2104.1; convenience-of-employer rule applies [US-NY-013, US-NYP52-002, US-NY-009] |
| Bonus / supplemental | NYS supplemental rate {{ny.pit.supplemental.nys.rate}} % or aggregate | Same rate on the New York-source share |
| NYC tax | Withheld if NYC resident, regardless of work location | Not withheld (no NYC nonresident tax) |
| Yonkers | Resident surcharge | Nonresident earnings tax on Yonkers work, subject to the threshold above |
| Severance, equity, benefits in kind | Taxed as wages under the federal wage definition (NYS-50 uses federal wages) | New York-source share only, allocation per IT-2104.1 |

- **Reciprocity:** {{ny.reciprocity.states}} [US-NY-013].

## @social
- **State unemployment insurance [US-NYS5-010, US-NYP9V-001].** 2026 taxable wage base {{ny.sui.wage_base}} USD (from 2026 indexed to a share of the state average annual wage and never reduced, US-NY-007). New-employer rate {{ny.sui.new_employer.rate}} % (normal plus subsidiary), plus the Re-employment Service Fund {{ny.ui.rsf.rate}} %. Experience range {{ny.sui.employer.rate.min}} % to {{ny.sui.employer.rate.max}} %. Employee UI contribution: {{ny.sui.employee.rate}} %. The state UI loan was repaid in the FY2026 budget; the FUTA credit-reduction effect is in Annex FED / MULTI.
- **Paid Family Leave (PFL) [US-NYP8-001, US-NYB5-001].** Employee-paid. 2026: {{ny.pfl.employee.rate@2026-01-01}} % of wages, annual employee maximum {{ny.pfl.employee.max_annual@2026-01-01}} USD. 2027 (DFS decision of 2026-08-31): {{ny.pfl.employee.rate@2027-01-01}} %, maximum {{ny.pfl.employee.max_annual@2027-01-01}} USD. Benefit {{ny.pfl.benefit.rate_of_aww}} % of the employee's average weekly wage, capped at the same share of the NYSAWW ({{ny.pfl.nysaww}} USD for 2026), i.e. a 2026 maximum weekly benefit of {{ny.pfl.benefit.max_weekly}} USD [US-NYB5-002]. Calendar-year accumulator: {{ny.pfl.employee.max_annual.accumulation}} [US-NYP8-001, US-NYB5-001].
- **Disability benefits (DBL) [US-NY-010].** Employee {{ny.dbl.employee.rate}} % of wages, capped at {{ny.dbl.employee.max_weekly}} USD per week; the employer pays the remaining cost.
- **Employer levies.** MCTMT (MTA-305, quarterly) and the Re-employment Service Fund per the levy census [US-NYP7-001, US-NYP7-004, US-OWN-007]; no MCTMT rate is carried in this annex's facts.

## @payslip
- **Content (Labor Law 195(3)), with every payment [US-NYS5-006]:** {{ny.payslip.items}}. Prevailing-wage supplements and allowances claimed toward the minimum wage are shown where they apply.
- **NYC Protected Time Off statement** (from 2026-02-22): {{ny.leave.nyc_pto.pay_statement_items}} [US-NYB5-003].
- **Retention:** payroll records {{ny.records.retention_years}} years (195(4)); tax records per DTF rules [US-NYS5-010].
- **Hire notice** in English and the employee's primary language (195(1)) [US-NYP51-003]; the payslip itself is in English (US-OWN-006).

## @reporting
- **NYS-45** (quarterly, combined withholding, wage reporting and UI), due {{ny.report.nys45.due}}; Parts A, B and C mandatory; e-file and electronic payment mandatory [US-NYS5-010]. Upload specification Pub 72.5 [US-FIL-007].
- **NYS-1 withholding deposit:** due within a few business days of the payroll that brings quarter-to-date withholding to {{ny.report.nys1.threshold}} USD or more; below it, pay with the NYS-45 [US-NYS5-010].
- **Form W-2:** no copy is filed with New York; NYS-45 Part C (quarterly wage reporting) replaces it. State wages box = federal box 1 for residents and for nonresidents with any New York service; the NYC box = box 1 for full-year residents [US-NYS5-010].
- **New hire:** report to DTF within {{ny.newhire.report_days}} calendar days, including rehires after a long separation; for a nonresident alien the period runs from SSN issue [US-NYS5-010].
- **Registration:** NY Business Express for UI, wage reporting and withholding [US-NYS5-010]. **MCTMT:** MTA-305, quarterly [US-NY-003].

## @leave
- **State paid sick leave (Labor Law 196-b) [US-NYS5-007].** Medium employers (band `5_99` of the key): {{ny.leave.paid_sick.annual_hours.5_99}} hours paid; large employers (band `100plus`): {{ny.leave.paid_sick.annual_hours.100plus}} hours paid; the smallest employers owe unpaid leave unless net income exceeds the statutory amount (196-b). Accrual one hour per {{ny.leave.paid_sick.accrual_ratio_hours_worked}} hours worked; front-loading allowed; paid at the regular rate (or minimum wage if higher); carry-over required, use may be capped; no payout at separation.
- **Paid prenatal leave:** {{ny.leave.prenatal.hours_per_52_weeks}} hours per rolling year, paid at the regular rate, no payout [US-NYS5-007].
- **NYC Protected Time Off (from 2026-02-22) [US-NYB5-003].** Paid PTO up to {{ny.leave.nyc_pto.paid_hours.max.under100}} hours (employers below the large-employer band) or {{ny.leave.nyc_pto.paid_hours.max.100plus}} hours (large employers); plus {{ny.leave.nyc_pto.unpaid_hours_immediate}} hours of unpaid PTO available at hire and on the first day of each calendar year (no proration, no carry-over required); plus {{ny.leave.nyc_pto.prenatal_paid_hours}} hours of paid prenatal leave per rolling year.
- **PFL benefits** are paid by the insurer, not by the employer as wages (see Section 3).

## @termination
- **Final pay:** {{ny.final_pay.rule}}; by mail on request (191(3)) [US-NYS5-003].
- **Written termination notice** stating the exact termination date and the benefits cancellation date within {{ny.term.notice.working_days}} working days (195(6)) [US-NYS5-006].
- **UI separation notice:** {{ny.term.ui_notice.form}} [US-NYS5-017]; timing rule open (below).
- **Accrued vacation:** no statutory payout; a "wage supplement" under 198-c payable per policy or agreement [US-NYS5-008]. Unused sick and prenatal leave: no payout [US-NYS5-007]. NY WARN is not a payroll calculation and is not covered.

## @bik
- **Conformity.** The New York return starts from federal wages (W-2 box 1), so the federal exclusions (401(k), 403(b), 457, cafeteria plans, HSA, transit, group-term life) carry over.
- **Departure:** 414(h) contributions of New York public employees are added back (addback applies: {{ny.bik.414h.addback}}) [US-NYS5-019]. UI remuneration includes the reasonable value of meals and lodging, and tips [US-NYS5-010].

## @deductions
- **Authorised deductions (Labor Law 193) [US-NYS5-005].** Only deductions required by law or voluntarily authorised in writing within the listed categories; authorisations kept for the employment plus the retention period; overpayment and advance recovery follow DOL regulations. The expanded text carries a sunset of 2028-11-06.
- **Creditor income execution (CPLR 5231) [US-NYS5-015].** At most {{ny.garn.consumer.max_rate_of_gross}} % of gross, never more than the federal disposable-earnings cap; the deduction may not reduce weekly disposable earnings below the statutory floor (thirty times the higher of the federal or New York minimum wage; regional rate open, below). No income execution for medical-debt judgments.
- **Support (CPLR 5241) [US-NYS5-016].** Start no later than the first pay period after service; remit to the SDU within {{ny.garn.support.remit_business_days}} business days of payday; CCPA percentage limits (Annex FED); support takes priority; multiple orders prorated; order current support, health premium, arrears; notify the issuer on termination.

## @cba
- **Prevailing wage:** exists ({{ny.prevailing_wage.exists}}); Labor Law 220 public-work rates and supplements [US-NYP51-002]. The pay statement must identify prevailing-wage supplements [US-NYS5-006]. Certified-payroll mechanics are not modelled.

## @indexation
- **Minimum wage:** from 2027 indexed to the three-year average of the August-July CPI-W Northeast, subject to off-ramps; published by October 1 [US-NYS5-002]. For 2027 the off-ramp was met (no increase) [US-NYS5-001].
- **Exempt thresholds and meal/lodging credits** move with the minimum-wage orders (652(2)) [US-NYS5-011].
- **UI wage base:** indexed to the state average annual wage [US-NYS5-010]; 2027 value open (Section 3).
- **PFL:** DFS publishes the rate and cap by September 1 each year [US-NYP8-001].
- **Withholding tables:** republished as the law changes; no 2027 change announced [US-NYS5-020].

## @data
- **Labor Law 203-d [US-NYS5-009]:** public display of SSNs prohibited ({{ny.data.ssn.public_display_prohibited}}); no SSN on badges or time cards; no SSN in unrestricted files. The SSN is not a required pay-statement item. UI information is confidential under UI Law 537 [US-NYS5-010].

## @live
- **2026-01-01:** new NYS and Yonkers withholding tables (NYC unchanged) [US-NYS5-020]; minimum wage and exempt thresholds per Section 1; farm overtime step; UI base under the new formula; PFL 2026 rate and cap.
- **2026-02-22:** NYC Protected Time Off (unpaid immediate hours, prenatal leave, pay-statement items) [US-NYB5-003].
- **2026-07-03:** Labor Law 193 revision published; 2028-11-06 sunset visible [US-NYS5-005].
- **2027-01-01:** minimum wage frozen by off-ramp; home care aide rates; PFL 2027 rate and cap [US-NYS5-001, US-NYB5-001]. No 2027 withholding change announced [US-NYS5-020].

## @special
| Population | New York rule | Register id |
|---|---|---|
| Domestic / household | Overtime threshold for domestic workers (higher for live-in); UI and wage reporting above a quarterly cash-wage test; income tax withholding voluntary; registration via NYBE | US-NYS5-013, US-NYS5-010 |
| Agricultural | Farm minimum wage per region; overtime threshold {{ny.labour.overtime.farm.threshold_hours}} hours in 2026; H-2A excluded from UI; direct-deposit consent rule does not apply | US-NYS5-012, US-NYS5-010, US-NYS5-004 |
| Minors | Employment certificate for 16-17 year olds; no youth minimum wage found; withholding exemption if no liability (671(a)(3)); daytime school students excluded from UI except nonprofit and government employers | US-NYS5-014, US-NYS5-010 |
| Tipped | Cash wages per Section 1 (hospitality only); tips are UI remuneration | US-NYS5-001, US-NYS5-010 |
| Clergy / religious | Ministers and religious-order members excluded from UI for nonprofits; income tax follows the federal wage definition | US-NYS5-010 |
| Students | 671(a)(3) exemption for full-time students with no liability; UI exclusions for own-school employment, work-study and camp students | US-NYS5-010 |
| Nonresident aliens | Treaty-exempt under IRS rules = exempt for NYS, NYC and Yonkers with no extra form; new-hire report runs from SSN issue | US-NYS5-010 |
| Statutory employees | No state rule beyond the federal one; the business directing the work is liable for UI on misclassified workers | US-NYS5-010 |
| Government employees | 414(h) addback; nonprofit and government employers may use the UI reimbursement option | US-NYS5-019, US-NYS5-010 |

## @gaps
- ny.pit.oracle.example2_residual :: NYS-50-T-NYS Method II example 2 is printed as {{ny.pit.oracle.example_2.withholding}} USD; half-up rounding of the intermediate rate product gives one cent less, so the booklet's rounding convention is not established. :: DTF statement of the rounding convention, or the DTF withholding calculator result for the same case.
- ny.pit.supplemental.local_rates :: The NYC resident, Yonkers resident and Yonkers nonresident supplemental withholding rates have no active register row (the source that carried them is no longer current; the current source carries only the rounding finding). No local supplemental rate is stated in this annex. :: Re-register the supplemental-rate lines of NYS-50-T-NYC and NYS-50-T-Y (1/26) as an active A.2 row.
- ny.term.ia12_3.timing :: The timing rule for the UI separation notice named in `ny.term.ui_notice.form` (12 NYCRR 472.8) was not read. :: Text of 12 NYCRR 472.8.
- ny.bik.nyc_flex125_addback :: The NYC flexible-benefits (cafeteria plan) addback for NYC employees was not read. :: DTF addback-modification instructions for New York City flexible benefits.
- ny.garn.consumer.floor_region :: Whether the CPLR 5231 floor uses the regional Labor Law 652 rate or the rest-of-state rate is not established. :: DOL or court guidance, or the income execution form text.
- ny.wh.method2.rounding :: NYS-50-T-NYS, NYS-50-T-NYC and NYS-50-T-Y (1/26) print no rounding instruction for Method II, and Example 2 is printed one cent above the half-up result (same open point as `ny.pit.oracle.example2_residual`). No rounding convention is assumed in this guide. :: a DTF statement of the Method II rounding convention, or the DTF result for the Example 2 inputs.

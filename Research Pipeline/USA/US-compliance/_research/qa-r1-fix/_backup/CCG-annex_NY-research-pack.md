# CCG research pack - annex_NY (New York)

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_NY` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_NY-facts.json` (58 facts, 1 pending on the register_id pattern defect, 14 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/NY.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- NYS withholding schedules (3.90% ... 11.44% recapture bands) are WITHHOLDING schedules, not statutory brackets - WTC uses NYS-50-T-NYS only.
- Oracle: NYS-50-T-NYS Method II examples 1/3/4 reproduce (8.01 / 3,576.63 / 44.10); example 2 has a 0.01 residual (258.51 printed vs 258.50).
- NY has no annual W-2 filing; NYS-45 Part C quarterly replaces it.
- 2027 PFL 0.452% is MANUAL (tier-B lead) - not a fact.

## 0.2 Register status check of the ids cited in the findings

These ids appear in the findings but are not plain `active`; do not cite them for a number:

- US-NY-011: superseded
- US-NYS5-018: partial
- US-NYS5-022: MANUAL
- US-NYS5-023: MANUAL

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `ny.labour.minwage.nyc_li_westchester.hourly` | 17.0 USD | 2026-01-01 |  | US-NYS5-002 | high |
| `ny.labour.minwage.rest_of_state.hourly` | 16.0 USD | 2026-01-01 |  | US-NYS5-002 | high |
| `ny.labour.minwage.next_year_change` | none on 2027-01-01 (off-ramp met) | 2027-01-01 |  | US-NYS5-001 | high |
| `ny.labour.minwage.home_care_aide.nyc_li_westchester.hourly` | 20.0 USD | 2027-01-01 |  | US-NYS5-001 | high |
| `ny.labour.minwage.home_care_aide.rest_of_state.hourly` | 19.0 USD | 2027-01-01 |  | US-NYS5-001 | high |
| `ny.overtime.weekly_threshold_hours` | 40 hours | 2026-01-01 |  | US-NYS5-011 | high |
| `ny.overtime.premium.multiplier` | 1.5 ratio | 2026-01-01 |  | US-NYS5-011 | high |
| `ny.labour.call_in_pay.hours` | 4 hours | 2026-01-01 |  | US-NYS5-011 | high |
| `ny.labour.spread_of_hours.threshold_hours` | 10 hours | 2026-01-01 |  | US-NYS5-011 | high |
| `ny.labour.exempt_salary.nyc_li_westchester.weekly` | 1275.0 USD | 2026-01-01 |  | US-NYS5-011 | high |
| `ny.labour.exempt_salary.rest_of_state.weekly` | 1199.1 USD | 2026-01-01 |  | US-NYS5-011 | high |
| `ny.labour.overtime.farm.threshold_hours` | 52 hours | 2026-01-01 | 2027-12-31 | US-NYS5-012 | high |
| `ny.labour.pay_frequency.manual` | weekly, max 7 days after week end | 2026-01-01 |  | US-NYS5-003 | high |
| `ny.labour.direct_deposit.consent_required` | True | 2026-01-01 |  | US-NYS5-004 | high |
| `ny.labour.tip_credit.service.nyc_li_westchester.cash_wage` | 14.15 USD | 2026-01-01 |  | US-NYS5-001 | high |
| `ny.labour.tip_credit.service.rest_of_state.cash_wage` | 13.3 USD | 2026-01-01 |  | US-NYS5-001 | high |
| `ny.labour.tip_credit.food_service.nyc_li_westchester.cash_wage` | 11.35 USD | 2026-01-01 |  | US-NYS5-001 | high |
| `ny.labour.tip_credit.food_service.rest_of_state.cash_wage` | 10.7 USD | 2026-01-01 |  | US-NYS5-001 | high |
| `ny.labour.meal_credit.nyc_li_westchester.per_meal` | 5.8 USD | 2026-01-01 |  | US-NYS5-011 | high |
| `ny.wh.method` | NYS-50-T-NYS (1/26): Method I tables, Method II exact calculation, Method III top income | 2026-01-01 | 2026-12-31 | US-NY-001 | high |
| `ny.pit.top_income.threshold.annual` | 1077550 USD | 2026-01-01 | 2026-12-31 | US-NY-001 | high |
| `ny.wh.certificate` | IT-2104; 2020+ W-4 without IT-2104 = zero allowances | 2026-01-01 |  | US-NYS5-010 | high |
| `ny.pit.exemption.annual` | 1000 USD | 2026-01-01 | 2026-12-31 | US-NY-001 | high |
| `ny.pit.supplemental.nys.rate` | 11.7 % | 2026-01-01 | 2026-12-31 | US-NY-001 | high |
| `ny.pit.local.nyc.basis` | resident tax, withheld regardless of work location; on NYS-1/NYS-45 | 2026-01-01 |  | US-NY-008 | high |
| `ny.pit.local.yonkers.nonresident_threshold` | 3000 USD | 2026-01-01 |  | US-NYS5-010 | high |
| `ny.reciprocity.states` | none | 2026-01-01 |  | US-NY-013 | high |
| `ny.pit.rounding` | to the cent per tables or formula | 2026-01-01 | 2026-12-31 | US-NY-001 | high |
| `ny.pit.oracle.example_1.withholding` | 8.01 USD | 2026-01-01 | 2026-12-31 | US-NY-001 | high |
| `ny.pit.oracle.example_3.withholding` | 3576.63 USD | 2026-01-01 | 2026-12-31 | US-NY-001 | high |
| `ny.pit.oracle.example_4.withholding` | 44.1 USD | 2026-01-01 | 2026-12-31 | US-NY-001 | high |
| `ny.pit.oracle.example_2.withholding` | 258.51 USD | 2026-01-01 | 2026-12-31 | US-NY-001 | medium |
| `ny.sui.wage_base` | 17600 USD | 2026-01-01 | 2026-12-31 | US-NYS5-010 | high |
| `ny.sui.new_employer.rate` | 4.025 % | 2026-01-01 | 2026-12-31 | US-NYP9V-001 | high |
| `ny.ui.rsf.rate` | 0.075 % | 2026-01-01 | 2026-12-31 | US-NYP9V-001 | high |
| `ny.sui.employer.rate.min` | 1.625 % | 2026-01-01 | 2026-12-31 | US-NYP9V-001 | high |
| `ny.sui.employer.rate.max` | 9.425 % | 2026-01-01 | 2026-12-31 | US-NYP9V-001 | high |
| `ny.sui.employee.rate` | 0 % | 2026-01-01 |  | US-NYP9V-001 | high |
| `ny.pfl.employee.rate` | 0.432 % | 2026-01-01 | 2026-12-31 | US-NYP8-001 | high |
| `ny.pfl.employee.max_annual` | 411.91 USD | 2026-01-01 | 2026-12-31 | US-NYP8-001 | high |
| `ny.dbl.employee.rate` | 0.5 % | 2026-01-01 |  | US-NY-010 | high |
| `ny.dbl.employee.max_weekly` | 0.6 USD | 2026-01-01 |  | US-NY-010 | high |
| `ny.payslip.items` | dates of work; names; employer address/phone; rates and basis; gross; deductions; allowances; net; regular and OT rates and hours (non-exempt); piece rates | 2026-01-01 |  | US-NYS5-006 | high |
| `ny.records.retention_years` | 6 years | 2026-01-01 |  | US-NYS5-006 | high |
| `ny.report.nys45.due` | Apr 30; Jul 31; Oct 31; Jan 31 | 2026-01-01 |  | US-NYS5-010 | high |
| `ny.report.nys1.threshold` | 700 USD | 2026-01-01 |  | US-NYS5-010 | high |
| `ny.newhire.report_days` | 20 days | 2026-01-01 |  | US-NYS5-010 | high |
| `ny.leave.paid_sick.annual_hours.5_99` | 40 hours | 2025-01-01 |  | US-NYS5-007 | high |
| `ny.leave.paid_sick.annual_hours.100plus` | 56 hours | 2025-01-01 |  | US-NYS5-007 | high |
| `ny.leave.paid_sick.accrual_ratio_hours_worked` | 30 hours | 2025-01-01 |  | US-NYS5-007 | high |
| `ny.leave.prenatal.hours_per_52_weeks` | 20 hours | 2025-01-01 |  | US-NYS5-007 | high |
| `ny.final_pay.rule` | next regular payday (discharge and resignation) | 2026-01-01 |  | US-NYS5-003 | high |
| `ny.term.notice.working_days` | 5 days | 2026-01-01 |  | US-NYS5-006 | high |
| `ny.term.ui_notice.form` | IA 12.3 to every separated worker or hours cut to 30 or fewer | 2026-01-01 |  | US-NYS5-017 | high |
| `ny.bik.414h.addback` | True | 2025-01-01 |  | US-NYS5-019 | high |
| `ny.garn.consumer.max_rate_of_gross` | 10 % | 2026-01-01 |  | US-NYS5-015 | high |
| `ny.garn.support.remit_business_days` | 7 days | 2026-01-01 |  | US-NYS5-016 | high |
| `ny.data.ssn.public_display_prohibited` | True | 2026-01-01 |  | US-NYS5-009 | high |
| `ny.prevailing_wage.exists` | True | 2026-01-01 |  | US-NYP51-002 (promoted, Synthesis C) | high |

# Findings by domain (stage 5)

## 1. labour_code
- **Minimum wage.** From 2026-01-01: **17.00** per hour in NYC, Nassau, Suffolk and Westchester; **16.00** in the rest of the state (Labor Law 652(1-a)) [US-NYS5-002, A.1].
  - **2027.** No increase on 2027-01-01. DOL states that an off-ramp condition of 652(1-b)(d) was met. Rates stay 17.00 / 16.00 [US-NYS5-001, A.2].
  - Home care aides from 2027-01-01: 20.00 / 19.00 [US-NYS5-001].
  - Governor's proposal to change the off-ramps: a proposal only, not enacted.
- **Local minimum wages.** None by ordinance. The state law itself sets the regions (NYC; Nassau/Suffolk/Westchester; remainder) [US-NYS5-002].
- **Overtime (12 NYCRR 142-2.2).**
  - 1.5 × regular rate after 40 h per week, or 44 h for residential employees.
  - FLSA 13(a)(2)/(4) exemptions are not applied.
  - FLSA-exempt employees other than exec/admin/professional get 1.5 × the minimum rate.
  - Call-in pay: 4 h, or the scheduled shift if shorter.
  - Spread of hours over 10 h, or a split shift: +1 h at the minimum rate.
  - Exec/admin salary threshold from 2026-01-01: **1,275.00 per week** in NYC/LI/Westchester and **1,199.10 per week** in the rest of the state [US-NYS5-011, A.1, CR 142 (12/25)].
  - Farm workers: overtime after **52 h from 2026-01-01**, then 48 (2028), 44 (2030), 40 (2032) [US-NYS5-012].
  - Domestic workers: 40 h, or 44 h if live-in [US-NYS5-013].
- **Pay frequency (Labor Law 191).**
  - Manual workers: weekly, at most 7 days after the week ends. Semi-monthly only with commissioner authorisation (1,000+ NY employees) or for nonprofits.
  - Clerical and other workers: at least semi-monthly, on regular paydays fixed in advance.
  - Commission salespersons: at least monthly, with a written agreement kept for 3 years [US-NYS5-003].
  - Damages for manual-worker frequency violations are limited to lost interest on a first violation, where pay was at least semi-monthly (198, revision 2025-05-16) [US-NYS5-021].
- **Method of payment.** Direct deposit only with the employee's advance written consent (192). Exempt: exec/admin/professional earning over 1,300 per week, and farm workers [US-NYS5-004]. Pay-card rules (12 NYCRR Part 192) were not read (open question).
- **Confidence:** High.

## 2. income_tax
- **Withholding method.**
  - Tables: NYS-50-T-NYS (1/26), effective 2026-01-01 to 2026-12-31. Method I uses wage-bracket tables; Method II is exact calculation; Method III (top income) applies when annualised net wages are 1,077,550 or more [US-NY-001, US-NYP52-001].
  - Certificate: IT-2104 (2026). An employee with a 2020+ W-4 and no IT-2104 is treated as zero allowances [US-NYS5-010].
  - Change notice: DTF page of 2025-12-02. The NYS and Yonkers tables changed for 2026; the NYC tables did not. No 2027 change is announced [US-NYS5-020].
- **Method II parameters, 2026.** The oracle is the official worked examples [US-NYP52-001].
  - Deduction allowance (Table B), single / married: weekly 142.30 / 152.90; biweekly 284.60 / 305.80; semimonthly 308.35 / 331.25; monthly 616.70 / 662.50; annual 7,400 / 7,950.
  - Exemption: 1,000 per year (weekly 19.25; monthly 83.30).
  - Single annual schedule: 3.90% to 8,500; 4.40% to 11,700; 5.15% to 13,900; 5.40% to 80,650; 5.90% to 96,800; 7.03% to 107,650; 7.53% to 157,650; 6.40% to 215,400; 11.44% to 265,400; 7.35% to 1,077,550.
  - Married annual schedule: identical up to 96,800; then 6.57%, 7.07%, 8.01% to 211,550; 6.40% to 323,200; 13.49% to 373,200; 7.35% to 1,077,550; 7.65% above.
  - These are withholding schedules with recapture bands, not the statutory brackets.
- **G-DERIVE on the official examples** (Python, Decimal, ROUND_HALF_UP).
  - Table A = Table B + n × Table C, reproduced exactly (200.05, 866.60, 350.00, 36.15).
  - Examples 1, 3 and 4 reproduce exactly: 8.01, 3,576.63, 44.10.
  - **Example 2 does not reproduce:** 165.00 × 0.0753 = 12.4245, which rounds to 12.42, giving **258.50**. The booklet prints 12.43 and **258.51**. This one-cent residual is recorded as an oracle open question.
- **Supplemental rates.** NYS 11.70%; NYC resident 4.25%; Yonkers resident 1.95975%; Yonkers nonresident 0.50% [US-NY-001, US-NY-011]. Alternatively use the aggregate method [US-NYS5-010].
- **Rounding.** The tax does not fix a rounding rule. Withhold to the cent per the tables or the formula [US-NYP52-001].
- **Exempt certificate.** Tax Law 671(a)(3): under 18, over 65, or full-time student under 25 with no prior-year and no expected liability [US-NYS5-010].
- **Local income taxes.**
  - NYC resident tax: residence-based, withheld regardless of work location.
  - Yonkers resident surcharge, and Yonkers nonresident earnings tax on work in Yonkers. No Yonkers withholding is needed where Yonkers wages are expected to be 3,000 or less.
  - All of these are withheld and filed on the NYS-1 / NYS-45 (T3 piggyback) [US-NY-008, US-NYS5-010].
  - The NYC tables did not change for 2026 [US-NYS5-020].
- **Resident and nonresident.**
  - Residents: all wages are withheld, wherever earned.
  - Nonresidents: NY-source wages only, allocated on IT-2104.1. TSB-M-12(5)I covers the 14-day rule.
  - Convenience-of-employer rule applies [US-NY-013, US-NYP52-002, US-NY-009].
  - No reciprocity agreements [US-NYP52-002].
- **Confidence:** High for state. Medium-High for NYC/Yonkers, which rest on existing rows.

## 3. social_security
- **SUI.**
  - 2026 wage base **17,600**. From 2026 the base is 18% of the state average annual wage, rounded up to 100, and is never reduced [US-NYS5-010; US-NY-007].
  - The 2027 base was not published on the pages read as of 2026-11-01 [US-NYP9V-001].
  - New employer: 4.025% total (3.4% normal + 0.625% subsidiary), plus RSF 0.075%, which gives 4.1%. Range 1.625% to 9.425% [US-NYP9V-001].
  - No employee UI contribution.
  - The FY2026 budget paid off the UI loan. Relevant to FUTA credit reduction; see the FED/MULTI units [US-NYP9V-001 page text].
- **PFL.**
  - 2026: 0.432% of wages, annual employee maximum 411.91 [US-NYP8-001]. The benefit is 67% of the employee's average weekly wage, capped at 67% of the NYSAWW, for up to 12 weeks [US-NYP8-001 text].
  - Derivation, not an authority figure: 411.91 / 0.00432 = 95,349.54, which implies an NYSAWW of 1,833.64 and a maximum benefit of 1,228.54. Not used as a fact.
  - **2027: lead only.** 0.452%, maximum 451.81 [US-NYS5-022, MANUAL]. The DFS page is blocked to curl.
- **DBL.** Employee 0.5% of wages, at most 0.60 per week; the employer pays the rest [US-NY-010].
- **Employer levies.** MCTMT and RSF, per the P7/P9 list [US-NYP7-001, US-NYP7-004]. Not redone.
- **Confidence:** High for 2026. Low for 2027 PFL until the DFS page is read.

## 4. payslip_statute
- **Content (Labor Law 195(3)), with every payment.**
  - Dates of work; employee name; employer name, address and phone.
  - Rate(s) and basis; gross; deductions; allowances claimed toward minimum wage; home-care aide benefits; prevailing-wage supplements; net.
  - Non-exempt employees: regular and overtime rates, and regular and overtime hours.
  - Piece-rate employees: piece rates and counts [US-NYS5-006].
- **Electronic delivery.** The statute is silent. The DOL guidance on electronic statements was not read (open question).
- **Retention.** Payroll records: 6 years (195(4)). Hire-notice acknowledgement: 6 years [US-NYS5-006]. Tax records: 4 years [US-NYS5-010].
- **Hire notice.** In English and in the employee's primary language (195(1)) [US-NYP51-003].
- **NYC PTO.** Lead only: the accrued, used and balance figures on each pay statement [US-NYS5-023, MANUAL].
- **Confidence:** High for state. NYC pay-statement item still open.

## 5. reporting_instruments
- **NYS-45** (quarterly, combined withholding + wage reporting + UI): due 30 Apr, 31 Jul, 31 Oct, 31 Jan. Parts A, B and C are all mandatory. E-file and ACH are mandatory, with a 50 USD penalty per paper document or payment [US-NYS5-010]. Upload spec: Pub 72.5 [US-FIL-007].
- **NYS-1 deposit.** Due within 3 business days (if 15,000+ was withheld in the year before the previous year) or 5 business days after the payroll that takes quarter-to-date withholding to 700 or more. Below 700, pay with the NYS-45. New employers use 5 days [US-NYS5-010].
- **W-2.** No copy is filed with NY. Quarterly NYS-45 Part C replaces it.
  - State wages box = federal box 1, for residents and for nonresidents with any NY service.
  - NYC local box = box 1 for full-year residents, and resident-period wages for part-year residents.
  - Yonkers follows the NYS rule [US-NYS5-010].
  - The separate annual-reconciliation mechanics in the Q4 NYS-45 instructions (NYS-45-I) were not read (open question).
- **New hire.** Report to DTF within **20 calendar days**. This includes rehires after 60+ days of separation. Electronic reporting: two monthly submissions 12 to 16 days apart. Fields: name, address, SSN, hire date, employer name and address, EIN, dependent health insurance availability and date. For a nonresident alien, the 20 days run from SSN issue [US-NYS5-010].
- **Registration.** NY Business Express (NYBE) for UI, wage reporting and withholding [US-NYS5-010].
- **MCTMT.** MTA-305, quarterly [US-NY-003].
- **Confidence:** High.

## 6. leave
- **State paid sick leave (196-b).**
  - Entitlement by employer size: 4 or fewer employees, 40 h unpaid (paid if net income over 1M); 5 to 99 employees, 40 h paid; 100 or more, 56 h paid.
  - Accrual: 1 h per 30 h worked; front-loading allowed.
  - Paid at the regular rate, or the minimum wage if higher. Maximum use increment 4 h.
  - Carryover required, but use may be capped. No payout at separation [US-NYS5-007].
- **Paid prenatal leave.** 20 h per 52 weeks from 2025-01-01, paid at the regular rate, no payout [US-NYS5-007].
- **NYC Protected Time Off.** Paid 40 or 56 h, plus **32 h unpaid** from the start of employment, plus 20 h paid prenatal leave [US-NYS5-018, partial, wayback copy]. Start date and rule details are leads only [US-NYS5-023].
- **PFL benefit-side payroll interaction.** Benefit 67% of AAWW, capped at 67% of NYSAWW, for 12 weeks [US-NYP8-001]. Paid by the insurer, so not wages from the employer. Taxability was not researched.
- **Confidence:** High for state. Medium for NYC.

## 7. termination
- **Final pay.** By the next regular payday for the period in which termination occurred, for both discharge and resignation; by mail on request (191(3)) [US-NYS5-003].
- **Termination notice.** Written notice of the exact termination date and the benefits cancellation date, within 5 working days (195(6)) [US-NYS5-006].
- **Accrued vacation.**
  - No statutory payout. It is a "wage supplement" under 198-c, payable per the policy or agreement [US-NYS5-008].
  - The forfeiture-notice rule comes from DOL guidance and case law and was not read.
  - Unused sick leave and prenatal leave: no payout [US-NYS5-007].
- **UI separation notice.** Form **IA 12.3** goes to every worker who is laid off, discharged or quits, or whose hours are cut to 30 or fewer per week [US-NYS5-017]. The timing rule (12 NYCRR 472.8) was not read.
- **NY WARN.** Not researched (not payroll-calculating).
- **Confidence:** High for timing. Medium for vacation.

## 8. benefits_in_kind
- **Conformity.** The NY return starts from federal wages (W-2 box 1), so the federal exclusions for 401(k), 403(b), 457, 125, HSA, transit and group-term life carry over.
- **Departures.** 414(h) contributions of NY public employees are added back (IT-201 line 21) [US-NYS5-019]. NYC flexible-benefits (IRC 125) addback for NYC employees via IT-225: not read (open question).
- **UI.** UI remuneration includes the reasonable value of meals and lodging, and tips [US-NYS5-010].
- **Minimum-wage credits, 2026 (Part 142).**
  - Meals: 5.80 per meal (NYC/LI/Westchester) and 5.50 (rest of state).
  - Lodging: 7.15 and 6.75 per day.
  - Uniform maintenance, weekly: 21.10 / 16.75 / 10.10 (NYC/LI/Westchester) and 19.85 / 15.80 / 9.55 (rest of state) [US-NYS5-011].
- **Confidence:** Medium-High.

## 9. deductions_garnishments
- **Authorised deductions (193).**
  - Allowed only if required by law, or authorised voluntarily in writing within the listed categories. Authorisations are kept for the period of employment plus 6 years.
  - Overpayment and advance recovery follow DOL regulations.
  - Revocation takes effect within 4 pay periods or 8 weeks.
  - The expanded text is marked effective until **2028-11-06**; the site's latest revision is dated 2026-07-03 [US-NYS5-005].
- **Creditor income execution (CPLR 5231).**
  - Up to **10% of gross**, and never more than 25% of disposable earnings.
  - The withholding must not reduce weekly disposable earnings below the greater of 30 × the federal minimum wage or 30 × the NY 652 minimum wage. Derived floor: 30 × 17.00 = **510.00** (NYC/LI/Westchester) and 30 × 16.00 = **480.00** (rest of state). Which regional rate applies is an open question.
  - When support is also withheld, the creditor's share is capped at 25% of disposable minus the support deducted.
  - No income execution for medical-debt judgments [US-NYS5-015].
- **Support (CPLR 5241).**
  - Start no later than the first pay period 14 days after service; remit to the SDU within 7 business days of payday.
  - Limits 50% / 60% of disposable, or 55% / 65% with arrears over 12 weeks.
  - Support takes priority over any other process. Multiple support orders are prorated. Order: current support, then health premium, then arrears.
  - Notify the issuer on termination [US-NYS5-016]. The employer fee amount is not in the section read.
- **State tax levies.** Not researched (open).
- **Confidence:** High.

## 10. collective_agreements (prevailing wage)
- **Labor Law 220.** Public-work prevailing rates and supplements [US-NYP51-002].
- **Pay statement.** Must identify prevailing-wage supplements (195(3)) [US-NYS5-006].
- Certified payroll mechanics and thresholds were not re-researched (P5/P6 rows reused).
- **Confidence:** Medium.

## 11. indexation
- **Minimum wage.** From 2027, current rate × change in the 3-year average of August-to-July CPI-W Northeast, rounded to 0.05. Off-ramps limited to 2 consecutive years; published by October 1 [US-NYS5-002]. 2027 result: no increase [US-NYS5-001].
- **Exempt salary thresholds and meal/lodging credits.** Move with the minimum-wage orders (652(2)) [US-NYS5-002, US-NYS5-011].
- **UI wage base.** 18% of the state average annual wage, rounded up to 100 [US-NYS5-010].
- **PFL.** DFS rate and cap published by September 1 each year [US-NYP8-001].
- **Withholding tables.** Reissued as the law changes [US-NYS5-020].
- **Derivation line.** 2027 minimum wage = 17.00 / 16.00 (off-ramp, no step). PFL cap derivation in §3.

## 12. data_protection
- **Labor Law 203-d.** No public display of SSNs, no SSN on badges or time cards, no SSN in unrestricted files, no disclosure of employee personal information to the public. Penalty up to 500 USD [US-NYS5-009].
- **SSN on payslips.** Not a required pay-statement field. No truncation rule found.
- **UI information.** Confidential under UI Law 537 [US-NYS5-010].
- **Confidence:** High. General Business Law 399-ddd was not read.

## 13. live_legal_change (2026-01-01 to 2026-11-02, and enacted for 2027)
- **2026-01-01.**
  - New NYS and Yonkers withholding tables (NYC unchanged) [US-NYS5-020].
  - Minimum wage 17.00 / 16.00 [US-NYS5-002].
  - Exempt thresholds 1,275 / 1,199.10 [US-NYS5-011].
  - Farm overtime threshold 52 h [US-NYS5-012].
  - UI wage base 17,600 under the new formula [US-NYS5-010].
  - PFL 0.432% / 411.91 [US-NYP8-001].
- **2026-02-22 / 2026-07-23 (lead).** NYC Protected Time Off: 32 h unpaid, and the rules [US-NYS5-023 MANUAL; US-NYS5-018].
- **2026-07-03.** Labor Law 193 revision on the official site; the 2028-11-06 sunset is visible [US-NYS5-005].
- **2027-01-01.** Minimum wage frozen by off-ramp [US-NYS5-001]. Home care aides 20.00 / 19.00 [US-NYS5-001]. PFL 2027 lead [US-NYS5-022 MANUAL].
- **No 2027 withholding change announced** [US-NYS5-020].
- **2025 (in force).** Pay-frequency damages limitation (198) [US-NYS5-021]. Prenatal leave [US-NYS5-007].

---

## Special populations (state round, US-OWN-005)
| Population | NY rule | register_id |
|---|---|---|
| Domestic/household | Overtime after 40 h (44 live-in). UI and wage reporting if cash wages of 500+ in a quarter. Income tax withholding voluntary. Babysitters under 18 excluded from UI. Registration via NYBE. | US-NYS5-013, US-NYS5-010 |
| Agricultural | Farm minimum wage 17 / 16. Overtime after 52 h (2026), then 48 (2028). UI liability at 20,000 cash wages in a quarter or 10+ workers on a day in 20 weeks. H-2A excluded from UI. Direct-deposit consent rule does not apply. | US-NYS5-012, US-NYS5-010, US-NYS5-004 |
| Minors | Employment certificate for ages 16-17 (exceptions listed). No youth minimum wage found. Withholding exemption under 18 if no liability (671(a)(3)). Daytime school students excluded from UI (except nonprofit/government employers). | US-NYS5-014, US-NYS5-010 |
| Tipped | Cash wage / tip credit 2026-27: service employees 14.15 / 2.85 (NYC/LI/Westchester), 13.30 / 2.70 (rest of state); food service 11.35 / 5.65 and 10.70 / 5.30. Hospitality employers only. Tips are UI remuneration. | US-NYS5-001, US-NYS5-010 |
| Clergy/religious | Ordained ministers and religious-order members excluded from UI for nonprofits. Income tax: no state rule beyond federal wage definition (NYS-50 uses federal wages). | US-NYS5-010 |
| Students | Tax Law 671(a)(3) exemption: full-time under 25 with no liability. UI exclusions: own-school student employment, work-study, camp students. College students generally covered. | US-NYS5-010 |
| Nonresident aliens | Treaty-exempt under IRS rules = exempt for NYS/NYC/Yonkers with no extra form. New-hire report due 20 days after SSN issue. | US-NYS5-010 |
| Statutory employees | No state rule beyond federal located (NYS-50 read). Misclassification: the business directing the work is liable for UI. | US-NYS5-010 |
| Government employees | 414(h) addback in NY income. Nonprofit/government/tribe: UI via the reimbursement option, and student wages are covered. | US-NYS5-019, US-NYS5-010 |

---

## ACCESS gaps (exact URLs; for the orchestrator's browser pass)
1. `https://www.dfs.ny.gov/apps-and-licensing/health-insurers/pfl-rate-decision-2027-page`: HTTP 403 (curl). `https://web.archive.org/web/2026id_/…pfl-rate-decision-2027-page`: 404. Needed for PFL 2027 rate and cap (US-NYS5-022).
2. `https://paidfamilyleave.ny.gov/2026`: 403. Wayback 2026id_: 403. Needed for the PFL 2026 maximum weekly benefit as an authority figure.
3. `https://www.nyc.gov/site/dca/about/paid-sick-leave-law.page`: 403 (wayback copy used). The DCWP FAQ (02/2026) PDF and NYC Admin. Code 20-911 ff. were not reached (US-NYS5-023).
4. `https://dol.ny.gov/overtime-0` and `https://dol.ny.gov/overtime-frequently-asked-questions`: 404 (overtime covered instead by CR 142).
5. `https://www.tax.ny.gov/pdf/publications/withholding/nys50.pdf`: 404. The guide now exists only as HTML (`/forms/publications/wt/nys50.htm`, used).

## Synthesis D additions (2026-11-02)

Source: browser-pass rows S5B-P1 / S5B-P2 merged into `legal-basis-register.csv` and SSA EFW2 TY2026 (US-FEDS5-032) read locally. Every claim below carries its register_id; the facts file is authoritative. Full log: `_research/synthesis-D/SYNTHESIS-D.md`.

Facts added:
- `ny.pfl.employee.rate` = **0.452** percent (2027-01-01 → open) [A.2, US-NYB5-001, quoted from authority page, conf high] — DFS decision 2026-08-31 (Insurance Law 4235(n)(1); WCL 209(3)(b)); implied cap wage 451.81 / 0.00452 = 99,957.96.
- `ny.pfl.employee.max_annual` = **451.81** USD (2027-01-01 → open) [A.2, US-NYB5-001, quoted from authority page, conf high]
- `ny.pfl.nysaww` = **1833.63** USD (2026-01-01 → 2026-12-31) [A.2, US-NYB5-002, quoted from authority page, conf high] — New York State Average Weekly Wage used for 2026 PFL benefits; 2027 NYSAWW +4.83% (amount not stated).
- `ny.pfl.benefit.max_weekly` = **1228.53** USD (2026-01-01 → 2026-12-31) [A.2, US-NYB5-002, quoted from authority page, conf high] — 67% of NYSAWW: 1,833.63 x 0.67 = 1,228.5321 -> 1,228.53 (quoted on the PFL 2026 page; arithmetic re-done). The earlier derived 1,228.54 was a rounding error.
- `ny.pfl.benefit.rate_of_aww` = **67** percent (2026-01-01 → open) [A.2, US-NYB5-002, quoted from authority page, conf high]
- `ny.leave.nyc_pto.unpaid_hours_immediate` = **32** hours (2026-02-22 → open) [A.3, US-NYB5-003, direct artifact inspection, conf high] — Available at hire and again on the first day of each calendar year; no proration, no carryover required.
- `ny.leave.nyc_pto.paid_hours.max.under100` = **40** hours (2026-02-22 → open) [A.3, US-NYB5-003, direct artifact inspection, conf high] — Employers with 99 or fewer employees.
- `ny.leave.nyc_pto.paid_hours.max.100plus` = **56** hours (2026-02-22 → open) [A.3, US-NYB5-003, direct artifact inspection, conf high]
- `ny.leave.nyc_pto.prenatal_paid_hours` = **20** hours (2026-02-22 → open) [A.3, US-NYB5-003, direct artifact inspection, conf high] — Per 52 weeks, no accrual (separate from PTO).
- `ny.leave.nyc_pto.pay_statement_items` = **Each pay period, on the pay statement or other written documentation: PTO accrued in the period; paid and unpaid PTO used in the period; unpaid immediately available hours available in the calendar year; accrued PTO available for use in the calendar year** (2026-02-22 → open) [A.3, US-NYB5-003, direct artifact inspection, conf high]

Open questions closed: `ny.pfl.employee.rate.next_year`, `ny.pfl.benefit.max_weekly`, `ny.leave.nyc_pto`.

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **ny.pit.oracle.example2_residual** (non-blocking): NYS-50-T-NYS Method II Example 2 prints 12.43 / 258.51; half-up gives 12.42 / 258.50. What would close it: DTF statement of the rounding convention or the DTF withholding calculator result for the same case.
- **ny.sui.wage_base.next_year** (non-blocking): 2027 UI base not yet published. What would close it: DOL UI rate page or NYS-50 2027 edition (December 2026).
- **ny.garn.consumer.floor_region** (non-blocking): Whether 5231 floor uses the regional 652 rate (510 vs 480/week). What would close it: DOL or court guidance, or the income execution form text.
- **ny.labour.paycard** (non-blocking): 12 NYCRR Part 192 not read. What would close it: DOL CR 192 copy.
- **ny.payslip.electronic** (non-blocking): DOL position on electronic wage statements not read. What would close it: DOL wage-statement FAQ.
- **ny.report.nys45_annual** (non-blocking): Q4 NYS-45 annual reconciliation mechanics not read. What would close it: NYS-45-I instructions (DTF).
- **ny.bik.nyc_flex125_addback** (non-blocking): NYC flexible benefits 125 addback not read. What would close it: IT-225-I (DTF).
- **ny.term.ia12_3.timing** (non-blocking): IA 12.3 timing rule not read. What would close it: 12 NYCRR 472.8 text.
- **ny.garn.state_tax_levy** (non-blocking): DTF income execution for tax warrants not researched. What would close it: Tax Law 692 / CPLR 5231 guidance.
- **ny.pit.supplemental.local_rates** (blocking): NYC resident 4.25%, Yonkers resident 1.95975% and Yonkers nonresident 0.50% supplemental rates sat on US-NY-011, now superseded by US-NYP52-001 (which carries only the rounding finding); no active row carries the local supplemental rates. What would close it: Re-register the NYS-50-T-NYC (1/26) and NYS-50-T-Y (1/26) supplemental-rate lines as an active A.2 row.

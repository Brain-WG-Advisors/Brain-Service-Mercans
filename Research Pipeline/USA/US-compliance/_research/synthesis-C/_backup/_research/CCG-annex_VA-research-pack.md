# CCG research pack - annex_VA (Virginia)

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_VA` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_VA-facts.json` (48 facts, 1 pending on the register_id pattern defect, 8 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/VA.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- VA 2027 standard deduction: STATUTE (9,200/18,400) prevails over guide (3,000 reversion) - but it is assessment-level; do not model 2027 withholding until Virginia Tax publishes the 2027 formula.
- PFML: no contribution before 2028-04-01; benefits from 2028-12-01 (corrects US-VA-P5-1-004).
- Paid sick leave: home health only in 2026; general law phases in from 2027-07-01 (50+).
- Garnishment floor 40x the greater of federal or state minimum (510.80/week in 2026).

## 0.2 Register status check of the ids cited in the findings

These ids appear in the findings but are not plain `active`; do not cite them for a number:

- US-VAP9W-001: partial

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `va.minwage.hourly` | 12.77 USD | 2026-01-01 | 2026-12-31 | US-VAS5-001 | high |
| `va.minwage.hourly` | 13.75 USD | 2027-01-01 | 2027-12-31 | US-VAS5-001 | high |
| `va.minwage.hourly` | 15.0 USD | 2028-01-01 |  | US-VAS5-001 | high |
| `va.labour.minwage.trainee.ratio` | 75 % | 2026-01-01 |  | US-VAS5-001 | high |
| `va.labour.minwage.farm_laborers_covered_from` | 2027-01-01 | 2027-01-01 |  | US-VAS5-002 | high |
| `va.overtime.weekly_threshold_hours` | 40 hours | 2022-07-01 |  | US-VAS5-004 | high |
| `va.overtime.premium.multiplier` | 1.5 ratio | 2022-07-01 |  | US-VAS5-004 | high |
| `va.pay_frequency.rule` | salaried at least monthly; hourly at least biweekly or twice a month | 2026-07-01 |  | US-VAS5-003 | high |
| `va.payment.method` | cash, check, direct deposit to designated account, paycard with consent (one free withdrawal) | 2026-07-01 |  | US-VAS5-003 | high |
| `va.minwage.tipped.cash_wage` | 2.13 USD | 2026-01-01 |  | US-VAS5-015 | high |
| `va.wh.method` | annualised T = G x P - [8,750 + 930 x E1 + 800 x E2]; 2% to 3,000; 60+3% to 5,000; 120+5% to 17,000; 720+5.75% above; / P | 2025-07-01 |  | US-VAS5-013 | high |
| `va.pit.std_deduction.single` | 8750 USD | 2025-01-01 | 2026-12-31 | US-VAS5-018 | high |
| `va.pit.std_deduction.married` | 17500 USD | 2025-01-01 | 2026-12-31 | US-VAS5-018 | high |
| `va.pit.std_deduction.single` | 9200 USD | 2027-01-01 | 2027-12-31 | US-VAS5-018 | high |
| `va.pit.std_deduction.married` | 18400 USD | 2027-01-01 | 2027-12-31 | US-VAS5-018 | high |
| `va.pit.exemption.personal` | 930 USD | 2025-01-01 |  | US-VAS5-018 | high |
| `va.pit.exemption.aged_blind` | 800 USD | 2025-01-01 |  | US-VAS5-018 | high |
| `va.pit.bracket.1.ceiling` | 3000 USD | 2025-07-01 |  | US-VAS5-013 | high |
| `va.pit.bracket.2.ceiling` | 5000 USD | 2025-07-01 |  | US-VAS5-013 | high |
| `va.pit.bracket.3.ceiling` | 17000 USD | 2025-07-01 |  | US-VAS5-013 | high |
| `va.pit.bracket.4.rate` | 5.75 % | 2025-07-01 |  | US-VAS5-013 | high |
| `va.wh.certificate` | VA-4 mandatory (federal W-4 not accepted); none = zero exemptions | 2026-04-01 |  | US-VAS5-021 | high |
| `va.wh.supplemental.rate` | 5.75 % | 2025-07-01 |  | US-VAS5-013 | high |
| `va.reciprocity.states` | KY;DC (daily commuters); MD;PA;WV (<183 days, wage-only, taxed at home) | 2025-07-01 |  | US-VAS5-013 | high |
| `va.local_wage_tax.exists` | False | 2013-01-01 |  | US-VAR3-001 | high |
| `va.bik.conformity.irc_date` | 2025-12-31 | 2026-01-01 |  | US-VAS5-011 | high |
| `va.sui.new_employer.rate` | 2.5 % | 2026-01-01 |  | US-VAR3-002 | medium |
| `va.sui.employer.rate.min` | 0.1 % | 2026-01-01 |  | US-VAS5-014 | high |
| `va.sui.employer.rate.max` | 6.2 % | 2026-01-01 |  | US-VAS5-014 | high |
| `va.ui.fund_building.rate` | 0.2 % | 2026-01-01 |  | US-VAR3-003 | high |
| `va.sui.employee.rate` | 0 % | 2026-01-01 |  | US-VAR3-002 | high |
| `va.sui.wages.section125_included` | False | 2026-01-01 |  | US-VAS5-014 | high |
| `va.sui.wages.401k_included` | True | 2026-01-01 |  | US-VAS5-014 | high |
| `va.pfml.contributions_start` | 2028-04-01 | 2028-04-01 |  | US-VAS5-016 | high |
| `va.payslip.items` | employer name/address; hours (hourly and below-FLSA-salary); rate; gross; each deduction amount and purpose | 2026-07-01 |  | US-VAS5-003 | high |
| `va.report.wh.semiweekly_threshold.monthly` | 1000 USD | 2025-07-01 |  | US-VAS5-013 | high |
| `va.report.va6.due` | January 31 (or 30 days after last wages) | 2025-07-01 |  | US-VAS5-013 | high |
| `va.report.ui.quarterly_due` | last day of month after quarter | 2026-01-01 |  | US-VAS5-014 | high |
| `va.newhire.report_days` | 20 days | 2020-07-01 |  | US-VAS5-006 | high |
| `va.leave.paid_sick.home_health_only` | True | 2026-01-01 | 2027-06-30 | US-VAS5-005 | high |
| `va.leave.paid_sick.general.start` | 2027-07-01 (50+); 2028-01-01 (25+); 2029-01-01 (all) | 2027-07-01 |  | US-VAS5-022 | high |
| `va.leave.paid_sick.accrual_ratio_hours_worked` | 30 hours | 2027-07-01 |  | US-VAS5-022 | high |
| `va.final_pay.rule` | next regular payday (discharge and resignation) | 2026-07-01 |  | US-VAS5-003 | high |
| `va.garn.creditor.max_percent` | 25 % | 2021-07-01 |  | US-VAS5-007 | high |
| `va.garn.consumer.floor.weekly` | 510.8 USD | 2026-01-01 | 2026-12-31 | US-VAS5-007 | high |
| `va.garn.iwo.employer_fee.per_remittance` | 5 USD | 2026-01-01 |  | US-VAS5-010 | high |
| `va.prevailing_wage.threshold` | 250000 USD | 2026-07-01 |  | US-VAS5-019 | high |
| `va.data.ssn.mailed_visible_prohibited` | True | 2008-07-01 |  | US-VAS5-008 | high |
| `va.sui.wage_base` | 8000 USD | 2026-01-01 |  | US-VA-SUI-001 (PENDING id pattern) | high |

# Findings by domain (stage 5)

## 1. labour_code
- **Minimum wage:** **12.77 USD/h** from 2026-01-01 to 2027-01-01. Then **13.75 USD/h** from 2027-01-01, **15.00 USD/h** from 2028-01-01, and CPI-U indexation from 2029-01-01 (the Commissioner publishes each new rate by October 1, starting in 2028; an adjustment is never below zero). These rates come from 2026 cc.350/351 and are confirmed in the statute text [US-VAS5-001] and on the DOLI page [US-VAS5-015]. Each year's rate is the greater of the state rate and the federal rate. On-the-job trainees (up to 90 days) get the greater of the federal minimum or 75% of the state rate: 12.77 × 0.75 = 9.5775, so 9.58 USD/h. I ran the arithmetic; the statute does not say how to round [US-VAS5-001].
- **G-DERIVE:** none is needed for 2026–2028, because the statute fixes those amounts. Indexation starts in 2029.
- **Coverage exclusions** (40.1-28.9) [US-VAS5-002]: farm laborers (excluded only until 2027-01-01; covered from that date, 2026 cc.357/358, confirmed by DOLI [US-VAS5-015]), under-16s, under-18s employed by a parent, full-time students under 18 working 20 h/week or less, work-study students, babysitters under 10 h/week, au pairs, H-2 workers, summer camps, golf caddies, outside salespeople, taxi drivers, inmates and volunteers.
- **Local minimum wages:** none. Va. Code 40.1-28.10 sets one statewide rate, and no local wage provision was found in the 2026 Title 40.1 update list [US-VAS5-025]. The register holds no explicit preemption section, so this rests on the absence of any local authority, not on an express statement (open question Q4).
- **Overtime:** follows the FLSA (1.5× over 40 h/week, no daily overtime), enforced through state remedies [US-VAS5-004]. A separate state overtime rule covers derivative air-carrier employees and home-care direct-support workers. It uses the state regular-rate formula [US-VAS5-023].
- **Pay frequency and payday:** salaried employees at least monthly; hourly employees at least every two weeks or twice a month. Monthly pay is allowed for work-study students, and by agreement for employees earning more than 150% of the state average weekly wage [US-VAS5-003].
- **Method of payment:** cash, check, direct deposit to an account the employee designates, or a paycard with full fee disclosure and the employee's consent. A paycard is allowed without consent only for employees hired after 2010-01-01 who did not designate an account, and the card must give one free withdrawal per pay period [US-VAS5-003].
- **Remedies:** liquidated damages equal to the unpaid wages plus 8% interest; treble damages for knowing violations. From 2026-07-01 there is a good-faith defense if the employer cures within 14 days [US-VAS5-003].
- Confidence: 95%.

## 2. income_tax
- **Method:** statute Va. Code 58.1-461 [US-VA-PIT-002]; guide 2614086 Rev. 10/26 [US-VAS5-013, US-VA-P5-1-001]. Formula for wages paid after 2025-07-01:
  - Annualised taxable income: T = G×P − [8,750 + 930×E1 + 800×E2].
  - Tax brackets: 2% up to 3,000; 60 + 3% from 3,000 to 5,000; 120 + 5% from 5,000 to 17,000; 720 + 5.75% above 17,000.
  - Per-period tax: W ÷ P.
  - The tables are rounded to the nearest dollar; the formula gives the exact amount.
- **Statute amounts** [US-VAS5-018]: personal exemption 930; aged/blind exemption 800; standard deduction 8,750 single / 17,500 married for TY2025–2026.
- **CONFLICT FOUND (live change):** the Rev. 10/26 guide says the 8,750 deduction sunsets after TY2026 and reverts to 3,000. The current statute (amended by 2026 c.7 and 2026 Sp.Sess.I c.1) says otherwise:
  - TY2027: **9,200 / 18,400**
  - TY2028–2029: **9,300 / 18,600**
  - from TY2030: 3,000 / 6,000

  The statute is A.1 and prevails over the guide. The 2027 withholding formula will therefore probably use 9,200, but Virginia Tax has not published a 2027 formula. The build must not take 3,000 from the guide (open question Q1).
- **Withholding certificate:** VA-4 (2601064 Rev. 04/26) is mandatory; a federal W-4 cannot be used instead. If no VA-4 is filed, withhold with zero exemptions. Fields: personal exemptions, age/blind exemptions, additional withholding, exempt, and SCRA/MSRRA exempt. Electronic VA-4s are allowed [US-VAS5-021, US-VAS5-013].
- **Supplemental wages:**
  - Paid with regular wages: aggregate them.
  - Paid separately: use the aggregate method, or a flat 5.75% if tax was withheld from regular wages.
  - Nonperiodic pension payments: 4% [US-VAS5-013].
- **Wages subject to withholding:** Virginia follows the federal definition. Exempt payments include IRA/SEP distributions, nonresident rail/motor/water carrier employees, merchant seamen and short-stay film crews [US-VAS5-013].
- **Local income tax:** none. Va. Code 58.1-300 bars it [US-VAR3-001].
- **Residents and nonresidents:** residents are taxed on all wages; nonresidents on wages for services performed in Virginia. Reciprocity:
  - KY and DC: daily commuters are exempt.
  - MD, PA and WV: exempt if the employee lives in Virginia less than 183 days, has only wage income from Virginia, and that income is taxed by the home state.
  - The exemption is claimed on the VA-4.
  - TN, NC and all other states: withhold [US-VAS5-013, US-VA-PIT-004].
- Confidence: 90%. The withholding formula for 2026 is A.2 and current. The 2027 formula is not published.

## 3. social_security
- **SUI (VEC):**
  - Wage base **8,000 USD** per employee per year [US-VA-SUI-001, US-VAS5-014].
  - New employer 2.5% (60.2-526(B)) "plus add-ons" [US-VAR3-002, US-VAS5-014].
  - Base rates 0.1%–6.2%. Assigned 6.2% for: no taxable payroll in 4 years, out-of-state construction contractors, delinquent employers.
  - Add-ons: fund-building charge 0.2% when the trust fund is at 50% or less [US-VAR3-003], and a pool cost charge set yearly.
  - No employee contribution [US-VAR3-002].
- **2026 pool-cost percentage:** NOT obtained at tier A. The only source is a search summary (0.03%, tier B, not used). The same summary says the 2.5% new-employer rate already *includes* the add-ons, which contradicts the VEC FAQ wording "2.5% plus add-ons" (open question Q2).
- **0.05% budget item:** HB30 2026 Item 359 [US-VAP7-003, existing row].
- **UI liability:** FUTA-liable employers, or quarterly payroll of 1,500 USD or more, or an employee in 20 weeks [US-VAS5-014].
  - Domestic employers: 1,000 USD in a quarter.
  - Agricultural employers: 20,000 USD in a quarter, or 10 or more workers in 20 weeks (H-2A excluded but counted toward the threshold) [US-VAS5-020].
  - Nonprofits: 4 or more employees in 20 weeks.
  - Churches and ministers are excluded [US-VAS5-012].
- **UI gross wages:** after section 125 deductions, before 401(k)/403(b) deductions [US-VAS5-014].
- **SDI/TDI:** none.
- **PFML** (Title 60.2 Chapter 8, 2026 cc.981/1093) [US-VAS5-016, US-VAS5-017, US-VA-P5-1-004]:
  - **No contribution in 2026 or 2027.** Contributions start **2028-04-01**; the rate is fixed by 2027-10-01.
  - Employers with more than 10 employees deduct up to 50% from the employee and remit 100%. Employers with 10 or fewer remit only the 50% employee share.
  - Wage cap = the Social Security wage base.
  - Benefits start **2028-12-01**, per the VEC FAQ. This corrects the "benefits 2028-04-01" wording of US-VA-P5-1-004.
- **Other levies:** see the P7/P9 list (US-VAP7-002/-003, US-VAP9W-001/-002). I did not redo it.
- Confidence: 80%. The pool-cost percentage and the add-on composition of the new-employer rate are open.

## 4. payslip_statute
- On each regular pay date, a written statement by paystub or online accounting showing:
  - employer name and address;
  - hours worked (for hourly employees, and for salaried employees below the FLSA salary level);
  - rate of pay;
  - gross wages;
  - the amount and purpose of each deduction;
  - enough detail to work out gross and net pay.
- Keep pay statements for 3 years. Agricultural employers provide one only on request [US-VAS5-003, US-VA-P5-1-005].
- Electronic delivery: "online accounting" is expressly allowed; no separate consent rule.
- No language clause [US-VAL-001].
- Confidence: 95%.

## 5. reporting_instruments
- **Withholding (Virginia Tax):** monthly liability under 100 USD files quarterly VA-5; 100 to 999 USD files monthly VA-5 (by the 25th); 1,000 USD or more pays semi-weekly on VA-15 (within 3 banking days of the federal cutoff) and reconciles quarterly on VA-16. Annual VA-6 is due January 31, or within 30 days after the last wages. Returns are required even with no tax due, and all filing and payment is electronic [US-VA-PIT-003, US-VAR3-004, US-VAS5-013, US-VAS5-009].
- **State W-2:** due January 31 through Web Upload (SSA **EFW2** / Pub 1220 format, state code **51**) or eForms. W-2C uses the new layout. Uploading W-2s does NOT create the VA-6, which is filed separately. Penalties: 6% per month, maximum 30%, minimum 10 USD [US-VAS5-013, US-VAS5-009].
- **UI quarterly report (VEC):** due the last day of the month after quarter end, via ESS, eForm or Web Upload. Web Upload accepts Excel, MMREF/EFW2, ICESA or delimited files. Amendments go on FC-34. Late filing costs 100 USD per report [US-VAS5-014]. ESS access needs ID.me from 2026-08-01 [US-VAP6-001].
- **New hire:** report to the Virginia New Hire Reporting Center within **20 days** of hire (independent contractors within 20 days of the contract), with the 42 USC 653a fields. Electronic reporters send two monthly transmissions 12–16 days apart. A multistate employer may designate one state [US-VAS5-006].
- **Registration:** R-1 / online; R-1H for household employers [US-VAS5-013]; VEC registration [US-VAS5-014].
- **Power of attorney:** PAR 101 for Virginia Tax [US-VA-P5-1-007]; ESS TPA invitation for VEC [US-VAP6-001].
- Confidence: 90%.

## 6. leave
- **Paid sick leave in force in 2026:** home health workers only (40.1-33.3) [US-VAS5-005].
- **ENACTED for 2027-07-01** (2026 cc.1128/1129), the general paid sick leave article 40.1-33.6:1–:7 [US-VAS5-022]:
  - Phase-in by employer size: 50 or more employees from 2027-07-01; 25 or more from 2028-01-01; all employers from 2029-01-01.
  - Accrual: 1 hour per 30 hours worked, 40-hour cap on accrual and on use, carry-over allowed. Exempt employees are deemed to work 40 hours. Front-loading is allowed, and a PTO policy that meets the standard counts.
  - No payout at separation; balances reinstated on rehire within 12 months.
  - Paid at the 40.1-29.3(B) regular rate, never below minimum wage with no tip credit.
  - Increments of 4 hours or less; records kept 3 years.
- **PFML:** benefit-side interaction starts in 2028 (§3).
- Confidence: 90%.

## 7. termination
- **Final pay:** all wages are due on or before the next regular payday, whether the employee was discharged or resigned. Virginia makes no distinction between the two [US-VAS5-003].
- **Accrued vacation payout:** I found no Virginia statute requiring it. 40.1-29(A) defines "wages" without naming vacation pay, so payout depends on employer policy. This is a negative finding from the statute and the DOLI page [US-VAS5-003, US-VAS5-015], with no affirmative statement from an authority (open question Q3).
- **Sick leave from 2027:** no payout required [US-VAS5-022].
- **UI separation notice:** VEC sends the Report of Separation and Wage Information to the last 30-day/240-hour employer only when a claim is filed. I found no employer-initiated separation notice [US-VAS5-014].
- **W-2 on termination:** the statute requires the wage statement on the day of the last payment of remuneration [US-VAS5-009].
- **State WARN:** not read (not payroll-relevant; the VA WARN Act was not checked).
- Confidence: 80%.

## 8. benefits_in_kind
- Fixed-date conformity to the IRC as of **2025-12-31** (58.1-301, 2026 c.7). None of the listed exceptions touches employee exclusions, so Virginia follows the federal treatment for 401(k), section 125, HSA, transit and group-term life [US-VAS5-011].
- Withholding follows the federal definition of wages [US-VAS5-013].
- UI wages: section 125 is excluded, 401(k) is included, and group-term life over 50,000 USD is treated differently [US-VAS5-014].
- Open: how Virginia treats the federal P.L. 119-21 deductions for tips and overtime (below-the-line deductions, not exclusions), see Q5.
- Confidence: 80%.

## 9. deductions_garnishments
- **Deductions:** none without the employee's written, signed authorization, except taxes or deductions required by law [US-VAS5-003].
- **Garnishment** (34-29) [US-VAS5-007]: the lesser of 25% of disposable earnings, or the amount above **40× the greater of the federal or state minimum wage**. In 2026 that protects 510.80 USD/week (40 × 12.77; arithmetic run). This is stricter than the CCPA's 30×.
- **Support orders:** 50%/60%, rising to 55%/65% when arrears exceed 12 weeks.
- **State tax debts:** outside the limits until 2027-07-01; within them after that date (2026 c.396).
- **Child-support income withholding** (20-79.3) [US-VAS5-010]: the lesser of the ordered amount or the 34-29 maximum. Employer fee up to 5 USD per remittance. Support has priority over other state liens, with proration across orders. Remit on payday, or by EFT within 4 days. EFT is mandatory for employers with 100 or more employees and payroll firms with 50 or more clients. Notify DCSE on termination. Fine of 1,000 USD for retaliation.
- Confidence: 90%.

## 10. collective_agreements (prevailing wage)
- Applies to public works for state agencies and covered institutions, and for localities that adopt an ordinance. Contracts of **250,000 USD or less are excluded**. The rate is never below Davis-Bacon [US-VAS5-019, US-VA-P5-1-006].
- Certified payroll duties: keep wage/hour records and a classification schedule for 6 years; produce them within 10 days; certify that they are accurate; post the rates on site and certify the posting within 10 days. Underpayment carries 8% interest and debarment.
- Confidence: 90%.

## 11. indexation
- **Minimum wage:** fixed by statute through 2028; CPI-U from 2029, published by DOLI by October 1 [US-VAS5-001].
- **UI wage base:** fixed at 8,000 in statute, not indexed [US-VA-SUI-001].
- **PFML:** wage cap tied to the Social Security wage base; the rate is set by 2027-10-01 [US-VAS5-016].
- **Income tax:** brackets and exemptions are not indexed; the standard deduction is fixed by statute for each year [US-VAS5-018].
- **Garnishment:** the protected floor moves with the minimum wage [US-VAS5-007].

## 12. data_protection
- The SSN may not be visible on or through a mailed envelope, published to the public, or embedded in documents [US-VAS5-008].
- No Virginia rule requires SSN truncation on the pay statement, and 40.1-29(D) does not list the SSN as a required item.
- The W-2 must carry the SSN [US-VAS5-009].
- Withholding records: 3 years [US-VAS5-013].
- Paid sick leave health information is confidential from 2027 [US-VAS5-022].
- Confidence: 75% (the general Virginia consumer data protection law was not checked for an employee-data exemption).

## 13. live_legal_change
Sweep source: the 2026 Updates indexes of Code Titles 40.1, 58.1 and 60.2 on law.lis.virginia.gov (2026 Acts, 2026-01-01 to 2026-11-02) [US-VAS5-025]. Payroll-relevant changes, every one enacted (none pending):

| Change | Effective | Level | Register |
|---|---|---|---|
| Minimum wage 13.75 / 15.00, CPI from 2029 (cc.350/351) | 2027-01-01 / 2028-01-01 / 2029-01-01 | payroll rate | US-VAS5-001 |
| Farm laborers covered by the state minimum wage (cc.357/358) | 2027-01-01 | payroll rate | US-VAS5-002 |
| Good-faith defense, 40.1-29(P) (c.1040) | 2026-07-01 | employer liability | US-VAS5-003 |
| General paid sick leave, 40.1-33.6:1–:7 (cc.1128/1129) | 2027-07-01 phase-in | leave accrual | US-VAS5-022 |
| Pay transparency, 40.1-28.7:12 (cc.996/1063) | 2026-07-01 (default date assumed) | HR, not payroll | US-VAS5-024 |
| Standard deduction 9,200 (2027), 9,300 (2028–29) (c.7; Sp.Sess.I c.1) | TY2027 | withholding (formula not yet republished) | US-VAS5-018 |
| IRC conformity to 2025-12-31 (c.7) | TY2026 | withholding / assessment | US-VAS5-011 |
| PFML Chapter 8 (cc.981/1093): contributions | 2028-04-01 | payroll deduction | US-VAS5-016 |
| Garnishment: state tax debts brought within the limits (c.396) | 2027-07-01 | garnishment | US-VAS5-007 |
| Prevailing wage amendments (cc.1014/1040/1060) | 2026-07-01 | certified payroll | US-VAS5-019 |

Not read (listed only): 40.1-28.7:7 misclassification, 40.1-28.7:8 non-competes, 40.1-44.2 heat illness, 40.1-100 child labor, 58.1-332 credit for taxes paid to other states (could affect resident credit), 58.1-339.8.
The next-year (2027) formula and tables from Virginia Tax are not published as of 2026-11-02.

---

## Special populations

| Population | VA rule | Register |
|---|---|---|
| Domestic/household workers | Covered by the minimum wage. UI when domestic cash wages reach 1,000 USD or more in a quarter (annual ESS filing possible below 5,000 USD/quarter). Withholding registration on R-1H, annual VA-6H with electronic W-2. Babysitters under 10 h/week and au pairs are excluded from the minimum wage. | US-VAS5-002, US-VAS5-014, US-VAS5-013 |
| Agricultural | Excluded from the minimum wage until 2027-01-01, covered after. No paystub unless requested. UI at 20,000 USD in a quarter or 10 or more workers in 20 weeks; H-2A excluded but counted toward the threshold. | US-VAS5-002, US-VAS5-003, US-VAS5-020 |
| Minors | Under 16 excluded from the minimum wage; under-18 full-time students working 20 h/week or less excluded; child of the employer under 21 excluded from UI. Child-labor hours rules (40.1-100, amended 2026) not read. | US-VAS5-002, US-VAS5-020 |
| Tipped | More than 30 USD/month in tips. Cash wage at least 2.13 USD/h with the FLSA tip credit, and cash wage plus tips must reach 12.77. Sick pay from 2027 without tip credit. | US-VAS5-002, US-VAS5-015, US-VAS5-022 |
| Clergy/religious | Excluded from UI (churches, ministers, religious orders). Withholding follows federal rules (minister wages are not subject to federal withholding, so no Virginia withholding). | US-VAS5-012, US-VAS5-013 |
| Students | Excluded from the minimum wage (bona fide programmes, work-study, full-time under-18 students working 20 h/week or less). Excluded from UI when employed by their own school, as student nurses or interns, or as full-time students at camps. Work-study students may be paid monthly. | US-VAS5-002, US-VAS5-020, US-VAS5-003 |
| Nonresident aliens | No Virginia-specific rule found. Withholding follows federal wages and Form VA-4. Temporary foreign workers (20 CFR 655) are excluded from the minimum wage. | US-VAS5-013, US-VAS5-002 |
| Statutory employees | No state rule beyond federal for withholding. UI excludes commission-only insurance agents, real estate agents, direct sellers and drivers excluded from FUTA. | US-VAS5-020 |
| Government employees | Covered by the state minimum wage (not federal employees). UI covers state and local service, with exclusions for elected and policymaking posts. Paid sick leave from 2027 includes the Commonwealth. | US-VAS5-015, US-VAS5-012, US-VAS5-022 |
| Home health / home care | Paid sick leave in force today (40.1-33.3). State overtime regular-rate rule for direct support workers. | US-VAS5-005, US-VAS5-023 |

## ACCESS gaps
- `https://www.vec.virginia.gov/sites/default/files/2026-04/PFML%20FAQ%204.22.26.pdf`: F5 403 to curl on 2026-11-02 (support ID 3c5d96ef…). Obtained through `web.archive.org/web/2026id_/…` instead.
- `https://www.vec.virginia.gov/pfml-news`: F5 403 on 2026-11-02. Not retried.
- `https://legacylis.virginia.gov/cgi-bin/legp604.exe?261+ful+CHAP0981`: connection returned 000 (no response). The chapter text was replaced by the codified 60.2-806.
- `https://www.tax.virginia.gov/legislative-summaries`: 404.
- `https://www.doli.virginia.gov/labor-law/minimum-wage/` redirects to a 2021 article (file deleted). The current figures were read on `doli.virginia.gov/programs/labor-law/payment-of-wage/`.
- 2026 VEC pool-cost charge: no VEC page carrying the 2026 percentage was reached. The VEC host is intermittently blocked by F5; the FAQ page was readable at 07:31 and blocked by 07:33.

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **va.meta.register_id_pattern** (blocking): 1 facts rest on active register rows whose ids (US-VA-SUI-001) do not match the facts-schema register_id pattern ^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$ (multi-hyphen legacy ids). They are carried in full in _facts_pending_register_id_pattern and are NOT yet consumable facts. What would close it: Orchestrator decision: a PATCH of facts.schema.json loosening the register_id pattern (e.g. ^[A-Z]{2}-[A-Z0-9-]{2,16}-[0-9]{3,4}$), or register alias ids; then run _research/synthesis-B/_work-MN-WY/promote.py to move the pending facts into facts[].
- **va.pit.formula.next_year** (blocking): 2027 withholding formula not published; guide says 3,000 reversion but statute sets 9,200/18,400 for TY2027. What would close it: 2026 c.7 / Sp.Sess.I c.1 enacting clauses and Virginia Tax 2027 guide 2614086.
- **va.ui.pool_cost_and_new_employer** (blocking): 2026 pool-cost charge not obtained at tier A (0.03% tier-B only); whether 2.5% includes add-ons is contradictory. What would close it: VEC 2026 tax-rate notice (ESS) or VEC 2026 rate release (Chrome pass).
- **va.term.vacation.payout** (non-blocking): No statute on accrued vacation payout (negative finding). What would close it: DOLI Payment of Wage FAQ entry or AG opinion.
- **va.labour.minwage.local_preemption** (non-blocking): Express local preemption not found (only single statewide rate). What would close it: Express Code provision or DOLI statement.
- **va.bik.pl119_21_deductions** (non-blocking): Virginia treatment of federal tips/overtime deductions (P.L. 119-21) not established. What would close it: Virginia Tax 2026 conformity guidance or tax bulletin.
- **va.data.cdpa_employee_exemption** (non-blocking): CDPA employee-data exemption not read. What would close it: Va. Code 59.1-575 et seq.
- **va.live.unread_amendments** (non-blocking): 2026 amendments to 58.1-332 and 40.1-100 listed but not read. What would close it: Those sections on law.lis.virginia.gov.

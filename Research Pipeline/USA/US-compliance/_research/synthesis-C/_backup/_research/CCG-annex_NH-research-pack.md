# CCG research pack - annex_NH (New Hampshire)

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_NH` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_NH-facts.json` (41 facts, 1 pending on the register_id pattern defect, 9 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/NH.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- NH has NO state wage tax: no withholding, no state W-4, no reconciliation (T1).
- Final pay on discharge within 72 HOURS [US-NHS5-002].
- Garnishment exemption 50x FMW (362.50/week) on pre-service wages on NH judgments; post-service wages fully exempt.
- Parental medical leave (US-NHS5-012) is MANUAL - do not cite.

## 0.2 Register status check of the ids cited in the findings

These ids appear in the findings but are not plain `active`; do not cite them for a number:

- US-NHS5-012: MANUAL

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `nh.labour.minwage.state.follows_federal` | True | 2011-08-21 |  | US-NHS5-003 | high |
| `nh.labour.tip_credit.cash_wage.min_ratio` | 45 % | 2011-08-21 |  | US-NHS5-003 | high |
| `nh.minwage.tipped.cash_wage` | 3.27 USD | 2011-08-21 |  | US-NHS5-003 | high |
| `nh.labour.minwage.learner_youth.ratio` | 75 % | 2011-08-21 |  | US-NHS5-003 | high |
| `nh.labour.meal_credit.full_board_room.weekly` | 45.0 USD | 2011-08-21 |  | US-NHS5-003 | high |
| `nh.overtime.weekly_threshold_hours` | 40 hours | 2011-08-21 |  | US-NHS5-003 | high |
| `nh.overtime.premium.multiplier` | 1.5 ratio | 2011-08-21 |  | US-NHS5-003 | high |
| `nh.labour.pay_timing.weekly_days` | 8 days | 2026-01-01 |  | US-NHS5-001 | high |
| `nh.labour.pay_timing.biweekly_days` | 15 days | 2026-01-01 |  | US-NHS5-001 | high |
| `nh.payment.method` | cash, EFT, direct deposit (written authorization), payroll card (voluntary consent, fees disclosed, one free withdrawal), or check; check must be offered | 2026-01-01 |  | US-NHS5-001 | high |
| `nh.labour.reporting_pay.hours` | 2 hours | 2026-01-01 |  | US-NHS5-011 | high |
| `nh.labour.meal_break.minutes` | 30 minutes | 2026-01-01 |  | US-NHS5-011 | high |
| `nh.labour.expense_reimbursement.days` | 30 days | 2026-01-01 |  | US-NHS5-011 | high |
| `nh.pit.exists` | False | 2026-01-01 |  | US-NH-006 | high |
| `nh.local_wage_tax.exists` | False | 2026-01-01 |  | US-NH-006 | high |
| `nh.sui.wage_base` | 14000 USD | 2026-01-01 |  | US-NHS5-007 | high |
| `nh.sui.wage_base.other_state_credit` | True | 2026-01-01 |  | US-NHS5-007 | high |
| `nh.ui.rate.statutory` | 2.7 % | 2026-01-01 |  | US-NHS5-007 | high |
| `nh.ui.fund_balance_reduction.rate` | 1.0 % | 2026-01-01 | 2026-12-31 | US-NHP9W-001 | high |
| `nh.sui.new_employer.rate` | 1.7 % | 2026-01-01 | 2026-12-31 | US-NHP9W-001 | high |
| `nh.ui.inverse_surcharge.rate` | 0.5 % | 2026-01-01 | 2026-12-31 | US-NHP9W-001 | high |
| `nh.ui.emergency_surcharge.rate` | 0.0 % | 2026-01-01 | 2026-12-31 | US-NHP9W-001 | high |
| `nh.ui.admin_contribution.range` | 0.1-0.4% carved out of the rate | 2026-01-01 |  | US-NHP7-001 | high |
| `nh.sui.employee.rate` | 0 % | 2026-01-01 |  | US-NHS5-007 | high |
| `nh.sdi_pfml.exists` | False | 2026-01-01 |  | US-NH-006 | medium |
| `nh.pfml.mandatory` | False | 2021-07-01 |  | US-NHS5-015 | high |
| `nh.payslip.hire_notice` | written notice at hire and before change of rate, basis, payday/place, computation method; fringe-benefit policy | 2020-03-05 |  | US-NHS5-004 | high |
| `nh.records.retention_years` | 3 years | 2011-08-21 |  | US-NHS5-003 | high |
| `nh.report.ui.quarterly_due` | last day of month following quarter | 2026-01-01 |  | US-NHS5-013 | medium |
| `nh.newhire.report_days` | 20 days | 2026-01-01 |  | US-NHS5-006 | high |
| `nh.report.new_hire.contractor_threshold` | 2500 USD | 2026-01-01 |  | US-NHS5-006 | high |
| `nh.leave.sick.state_statute.exists` | False | 2026-01-01 |  | US-NHS5-011 | high |
| `nh.leave.lactation.min_employees` | 6 | 2025-07-01 |  | US-NHS5-011 | high |
| `nh.term.final_pay.discharge.hours` | 72 hours | 1967-09-01 |  | US-NHS5-002 | high |
| `nh.term.final_pay.resignation` | next regular payday, or 72 hours if one pay period's notice | 1967-09-01 |  | US-NHS5-002 | high |
| `nh.term.vacation.payout` | per written policy (no statutory duty); accrued benefits do not lapse on policy change | 2020-03-05 |  | US-NHS5-004 | high |
| `nh.garn.consumer.exempt_multiple_fmw` | 50 | 2026-01-01 |  | US-NHS5-009 | high |
| `nh.garn.consumer.exempt.weekly` | 362.5 USD | 2026-01-01 |  | US-NHS5-009 | high |
| `nh.garn.support.employer_fee.per_withholding` | 1.0 USD | 2010-07-23 |  | US-NHS5-008 | high |
| `nh.prevailing_wage.exists` | False | 2026-01-01 |  | US-NHP8-001 | high |
| `nh.data.breach_notice.exists` | True | 2007-01-01 |  | US-NHS5-010 | high |
| `nh.payslip.items` | statement of deductions each pay period a deduction is made; monthly itemized accounting for 275:48 I(d) deductions | 2026-01-01 |  | US-NH-P5-1-001 (PENDING id pattern) | high |

# Findings by domain (stage 5)

## 1 — labour_code
**Minimum wage**
- The NH minimum wage is the federal minimum wage "as amended", so it is USD 7.25/hour in 2026 [US-NHS5-003, A.1, high; federal figure US-FEDS5-017]. NH has no figure of its own.
- No NH increase is enacted for 2027. HB 1484 (2026, a separate state floor) is a lead only and was not enacted per leads; see live change.
- No local minimum wages exist. The state rate is a single statewide rule (RSA 279:21), and no municipal wage ordinance was found. The preemption point was not read separately.

**Tipped employees** [US-NHS5-003, high]
- Covers restaurant, cigar bar, hotel, motel, inn, cabin and ballroom staff who receive more than USD 30/month in tips.
- The base wage is at least 45% of the minimum, which is USD 3.27.
- The text in force says that once the federal minimum rises above its 2021-07-23 level, the base becomes the federal minimum direct wage, but never below USD 3.27.
- The employer must make up any shortfall to the minimum wage for each pay period.
- Tips are the employee's property. Tip pools must be voluntary (279:26-b).

**Subminimum rates** [US-NHS5-003]
- 75% of the minimum for learners with less than 6 months' experience (employer files with the Commissioner within 10 days).
- 75% for persons aged 16 or under.
- Meal and lodging credits (hotel/restaurant only, RSA 279:21-a): full board and room USD 45.00/week or 6.45/day; meals 39.45/week or 1.88/meal; lodging 10.88/week or 1.80/day.

**Overtime** [US-NHS5-003, high]
- 1.5x for hours over 40 in a week.
- RSA 279:21 VIII(b) takes employees of FLSA-covered employers out of the NH overtime rule, so the FLSA governs them.
- The fluctuating-workweek method is barred for delivery drivers and sales merchandisers.
- The NH rule therefore bites only on employers not covered by the FLSA.

**Pay frequency and timing** (RSA 275:43 I and IV; Lab 803.01) [US-NHS5-001, US-NHS5-004, high]
- Weekly pay is due within 8 days after the workweek ends; biweekly pay within 15 days.
- Paydays must be regular and designated in advance.
- Semi-monthly or monthly pay needs the Labor Commissioner's written permission and must still be at least monthly.

**Method of payment** (275:43 I-II) [US-NHS5-001, high]
- Allowed: cash, EFT, direct deposit (written authorization, bank of the employee's choice), payroll card, or check.
- An employer that uses EFT, direct deposit or cards must also offer payment by check.
- Payroll card conditions:
  - written voluntary consent, which cannot be a condition of hire;
  - plain-language disclosure of all fees;
  - one free full withdrawal per pay period;
  - no card expiry without a free replacement;
  - written notice and new assent before fee changes;
  - the employee may opt out at any time.

**Other wage-payment rules** [US-NHS5-011, US-NHS5-004, high; meal break also in DOL FAQ US-NH-P5-2-001]
- Reporting pay: at least 2 hours at the regular rate (275:43-a; not counties or municipalities).
- Meal break: 30 minutes after 5 consecutive hours (275:30-a).
- Business expenses: reimbursed within 30 days of proof (275:57).
- Wages of a deceased employee up to USD 3,000 may be paid without probate (275:47, amended 2024-09-10).

**Coverage of the wage-payment chapter** [US-NHS5-005]
- Excludes domestic labor in the employer's home and farm employers with fewer than 5 employees.
- Defines employee status with a 7-criterion independent-contractor test.

## 2 — income_tax
- **No state tax on wages; no employer withholding; no state W-4; no supplemental rate; no reconciliation return.** The DRA list of administered taxes has no wage or withholding tax [US-NH-006, US-NHP9W-003, A.2]. The Interest and Dividends Tax is repealed for periods from 2025-01-01 [US-NH-001].
- **Local income taxes:** none. The DRA list shows no local wage or earned-income tax [US-NH-006].
- **Reciprocity:** not applicable, because NH has no wage tax to reciprocate. NH residents working in a wage-taxing state (e.g. MA, ME, VT) are withheld by that state. That routing belongs to the MULTI unit.
- **Resident/nonresident:** not applicable.
- **Oracle:** none. There is no state withholding calculator because there is no state withholding.

Confidence: high.

## 3 — social_security
**SUI (NHES; RSA 282-A)** [US-NHS5-007, A.1; US-NH-005; US-NHP9W-001/-002]
- Wage base: USD 14,000 per employee per calendar year. It is a fixed statutory figure (282-A:69 I) and is not indexed.
- Statutory rate: 2.7%, subject to experience rating.
- Employee contribution: none. 282-A:69 I says contributions "shall not be deducted, in whole or in part, from the wages."
- New-employer rate 2026: 2.7% minus the quarterly Fund Balance Reduction. The FBR is 1.00% for Q1–Q4 2026 [US-NHP9W-001], so the effective new-employer rate is **1.7%**. This is derived arithmetically: 2.7 − 1.0 = 1.7. Confidence is medium-high, because NHES states the "2.7% minus any FBR" rule for new employers [US-NH-005] and the FBR table gives 1.00% [US-NHP9W-001].
- Other 2026 rate elements:
  - inverse surcharge 0.50% for negative-rated employers (Schedules II/III);
  - emergency surcharge 0.00%;
  - Administrative Contribution 0.1–0.4%, carved out of the rate, not added to it [US-NHP7-001, US-NHP9W-002];
  - highest earned rate 7.0% (Handbook [US-NHS5-013]);
  - rates run on a July–June year, and determination letters were mailed 2026-08-27.
- **Wage-base credit for other-state wages (MULTI hand-off): YES.** For the USD 14,000 base, wages "include service subject to contribution under any employment security law of another state" (282-A:69 I) [US-NHS5-007, high].
- Localization test: base of operations, then direction and control (282-A:9 I) [US-NHS5-007].
- UI wages (282-A:15):
  - included: bonuses, commissions, board, lodging and payment in kind;
  - excluded: employer plan payments for retirement, third-party sickness/disability, medical/hospitalization, SUB and death benefits, and employer-paid FICA;
  - employee elective deferrals (401(k), section 125): no express exclusion in 282-A:15, so treatment is open (see Open questions).

**SDI/TDI:** none in NH [US-NH-006 absence; FED list US-FED-P5-2-007 names CA, HI, NJ, NY, RI only].

**PFML: voluntary, no mandatory levy** [US-NHS5-015, A.1; US-NH-004]
- The Granite State Paid Family Leave Plan offers FMLI through the state carrier.
- Employers with more than 50 employees may sponsor coverage (contributory, partially contributory or non-contributory). Payroll deduction and remittance procedures are set by the DAS commissioner.
- Individuals can buy cover through the NHES purchasing pool: premium capped at USD 5/week, 7-month waiting period, 1-week elimination period.
- Benefit level (from the FAQ): 60% wage replacement for up to 6 weeks [US-NH-004].
- Sponsoring employers get a BET credit of 50% of the premium (RSA 77-E:3-e). This is an entity-level item and not part of payroll [US-NHS5-016, A.2].
- Job restoration and continued health insurance apply for sponsoring employers with 50+ employees (275:37-d) [US-NHS5-011].
- 2025 HB 517 was introduced to repeal the plan. As enacted (eff. 2025-07-13, per leads) it only repealed the state's outreach and marketing duties. This is a lead only; the chaptered law was not read.
- **MULTI hand-off:** PFML coverage of multistate workers is not applicable, because the plan is voluntary.

**Other levies:** only what the P7/P9 list holds (AC, FBR and surcharges). The BET is excluded under US-OWN-007.

## 4 — payslip_statute
**Required content** [US-NH-P5-1-001, US-NHS5-004, A.1, high]
- NH has no itemized pay-statement content list.
- RSA 275:49 IV requires a statement of the deductions made each pay period a deduction is made.
- Deductions taken at the employee's written request under 275:48 I(d) (section 125/132 plans and similar) need a written itemized accounting at least monthly [US-NHP6-002].

**Hire and change notices** [US-NHS5-004]
- At hire and before any change, the employer must give written notice of: the rate, the pay basis, the day and place of payment, and the method of computing wages.
- A written or posted fringe-benefit policy is also required (vacation, holiday, sick, bonus, severance, expenses, pension).
- A signed copy of these notices must be kept on file (Lab 803.03(a)-(c), (f)(6)).

**Delivery**
- No statute or rule read addresses electronic delivery of the deduction statement.
- RSA 279:27 allows *records* to be made and retained electronically [US-NHS5-003].
- Electronic pay statements are therefore an open question.

**Retention** [US-NHS5-003, US-NHS5-004, US-NH-P5-1-001]
- 3 years for hours and wage records (279:27; 275:49 VI; Lab 803.03(g)).

**Language:** English; no second-language rule for the payslip [US-NHL-001, US-NHP9L-002].

**MULTI hand-off (pay-statement reach):** RSA 275 has no explicit territorial clause. Coverage follows "employer … employing any person" (275:42 I). No rule on out-of-state work was found, so this stays open.

## 5 — reporting_instruments
**State withholding return / state W-2:** none. There is no state wage tax [US-NH-006].

**Quarterly Employer Tax and Wage Report (NHES)** [US-NHS5-013, A.3, medium-high; NHES page US-NH-005]
- Part 1 is the tax report; Part 2 is the wage report.
- It must be filed every quarter, even with no employment.
- Gross wages of all employees must be reported.
- Report and payment are due on the **last day of the month following the quarter** (Q1 due April 30). WebTax filers have 2 extra days.
- A 30-day filing extension is available on application with a USD 50 fee, paid before the due date. It covers the filing only, not the payment.
- Late filing: 10% of the tax due, minimum USD 25. Late payment: interest of 1% per month.
- Channel: WebTax/NHUIS online with optional EFT, or electronic wage reporting per NHES 0047, or paper.
- These figures come from the 2016 Handbook. NHES lists it as current, but the figures were not re-checked against Emp 303.02: the Emp 300 rules were not archived (see ACCESS gaps).

**New-hire reporting (RSA 282-A:117-a)** [US-NHS5-006, A.1, high]
- Report to NHES within 20 days of hire or rehire.
- Electronic filers may instead send 2 transmissions a month, 12 to 16 days apart.
- Fields: employee name, address, SSN and first day of work; employer name, address, FEIN and state ID.
- A W-4 copy is accepted.
- **NH-specific:** independent contractors (non-casual) must also be reported when payment is expected to exceed USD 2,500. The W-9 is accepted for this.
- Multistate employers may designate one state and notify HHS.

**Other reports and duties**
- Registration and TPA access through NHUIS [US-NHP8-003, US-NHP9-001].
- Preliminary Mass Layoff Notice to NHES when 25+ people are laid off in a week for 7+ days [US-NHS5-013].
- The Unemployment Notice poster is mandatory [US-NHS5-013].

## 6 — leave
**Paid sick leave:** NH has no statute.
- The RSA 275 chapter index (Wayback 2026-03-19) shows no sick-leave subdivision [US-NHS5-011].
- Sick and vacation pay exist only by employer policy, and are then wages (275:43 V) [US-NHS5-001].
- MULTI hand-off: there is no NH paid-sick-leave coverage rule for multistate workers, because there is no statute.

**PFML:** voluntary (section 3).

**Lactation** (RSA 275:78-83, eff. 2025-07-01) [US-NHS5-011, high]
- Applies to employers with 6+ employees in NH.
- Unpaid break of about 30 minutes per 3 hours worked, for 1 year after birth.
- A written policy must be made available at hire.
- No make-up time may be required.

**Parental medical leave (eff. 2026-01-01, reported as RSA 275:37-f, 2025 HB 2)** [US-NHS5-012, B, MANUAL]
- Up to 25 hours of UNPAID leave for 20+ employers.
- The statute was not read: 403, and the Wayback copy is the 403 page.
- Pay impact is limited to handling unpaid absence.

## 7 — termination
**Final pay** (RSA 275:44; Lab 803.01(e)) [US-NHS5-002, US-NHS5-004, high]
- Discharge: within **72 hours**, in person or by mail at the employee's choice.
- Resignation: by the next regular payday, or within 72 hours if the employee gave at least one pay period's notice.
- Layoff or suspension in a labor dispute: by the next regular payday.
- Willful failure: liquidated damages of 10% of the unpaid wages per day, capped at the unpaid amount.

**Accrued vacation payout** [US-NHS5-001, US-NHS5-004, high]
- There is no statutory duty to pay out unused vacation.
- Vacation, severance, holiday and sick pay are wages when due under the employer's practice or policy (275:43 V), so payout follows the written policy.
- Benefits accrued before a policy change do not lapse (Lab 803.03(d)).

**Separation notices**
- No UI separation notice to the employee is required by any source read.
- NHES sends a "Request to Employer for Separation Information" when a claim is filed [US-NHS5-013].

**Mass layoff**
- The NHES preliminary notice applies (section 5).
- The NH WARN-type statute (RSA 275-F) was not read. It is not payroll-calculating.

## 8 — benefits_in_kind
- **Income tax conformity:** not applicable, because there is no wage tax.
- **UI wages** (282-A:15) [US-NHS5-007]:
  - include the reasonable value of board, lodging and payment in kind;
  - exclude employer contributions to retirement, medical and death-benefit plans;
  - elective deferrals are open (Open questions).
- **Section 125:** small employers (2+ NH employees with no employer health plan) may set up a premium-only section 125 plan for employees working more than 15 hours/week (275:43-c) [US-NHS5-011].
- **Meal and lodging credits** against the minimum wage: see section 1.

## 9 — deductions_garnishments
**Deduction authorization** (RSA 275:48) [US-NHP6-002, US-NH-P5-1-001, A.1, high]
- Deductions are allowed only when required by law, or with written authorization for the 12 listed purposes or other purposes that give the employer no financial advantage.
- A deduction may not offset items the employee needs to do the job.
- Deductions at the employee's request (section 125/132 and similar) need a monthly itemized accounting.

**Creditor garnishment (trustee process, RSA 512:21)** [US-NHS5-009, A.1, high]
- Wages for work done after the writ is served are exempt.
- Wages earned before service are exempt, except on a debt on an NH court judgment.
- In that case **50 x the FLSA minimum hourly wage per week** is exempt. Derived arithmetically: 50 x 7.25 = **USD 362.50/week**.
- This is more protective than the CCPA (30x = 217.50).
- On RSA 399-A loan contracts the exemption is USD 50/week.

**Child and spousal support (RSA 458-B)** [US-NHS5-008, A.1, high]
- Start no later than the first pay period that falls 14 days after the notice was mailed.
- Remit on the same day the employee is paid.
- Arrears add-on: at least 20% of current support.
- Total withholding is capped at the CCPA limit, 15 U.S.C. 1673(b).
- Priority: current support, then health insurance or cash medical support, then arrears, then other.
- Support withholding has priority over other state process.
- The employer may deduct a **fee of USD 1.00 per withholding**.
- Lump sums (severance, accumulated sick or vacation pay, bonuses, commissions) can be taken up to the arrears when the obligor is non-compliant.
- The employer must notify the state within 15 days of termination.
- Penalties: administrative fine of USD 100 per pay period for willful failure; misdemeanor (up to USD 1,000) for retaliating against the employee.

**State tax levies:** no wage tax. NHES collection powers (liens, warrants) are against the employer [US-NHS5-013].

## 10 — collective_agreements
- **Prevailing wage:** none. RSA 280 (public-works minimum wages) is repealed [US-NHP8-001, US-NHP8-002, A.1].
- Federal Davis-Bacon applies only to federally assisted work.
- No state certified-payroll duty exists.
- High confidence.

## 11 — indexation
**Nothing is indexed by NH statute.**
- The minimum wage is pegged to the federal minimum [US-NHS5-003].
- The SUI wage base is a fixed USD 14,000 [US-NHS5-007].
- The garnishment exemption floats with the FLSA minimum (50x) [US-NHS5-009].
- The UI Fund Balance Reduction and surcharges change **quarterly** by trust-fund thresholds (RSA 282-A:82/82-a). They are published on the NHES Tax Rate Chart [US-NHP9W-001/-002].
- Experience rates are set for July–June [US-NHP9W-002].
- No G-DERIVE chain is needed beyond the two derivations above: 1.7% and USD 362.50.

## 12 — data_protection
**Breach notification** (RSA 359-C:19-20) [US-NHS5-010, A.1, high]
- Covers name plus unencrypted SSN, driver's licence or government ID, or a financial account number with its access code.
- Notify affected individuals as soon as possible, and notify the NH Attorney General or the primary regulator.
- A payroll processor holding the data must notify the data owner immediately.

**Other rules**
- No NH rule requiring SSN truncation on pay statements was found in RSA 359-C or RSA 275.
- Personnel-file access on request (275:56) [US-NHS5-011].
- The NH comprehensive privacy act (RSA 507-H, 2025) was not read. Leads say employee data is outside its scope. Open.

## 13 — live_legal_change (2026-01-01 to 2026-11-02)
- **In force 2026-01-01:** unpaid parental medical leave of 25 hours for 20+ employers [US-NHS5-012, MANUAL]. Statute not read.
- **In force 2025-07-01:** lactation breaks [US-NHS5-011].
- **UI 2026:** FBR 1.00%, inverse surcharge 0.50% and emergency surcharge 0.00% in every quarter [US-NHP9W-001].
- **Not enacted (leads only, no register row):**
  - HB 1484 (2026): a state minimum wage floor with steps from 2026-07-01;
  - SB 416 (2026): tip pooling, sent to interim study.
- No 2027 change was found.
- Status rests on search leads. The gc.nh.gov bill-status pages were not reachable (403 without VPN).

## Special populations (state round, US-OWN-005)
| Population | NH rule | register_id |
|---|---|---|
| Domestic/household | Exempt from the NH minimum wage (279:21 I) and from the wage-payment chapter when in the employer's home (275:42 I). UI covers domestic service only if cash wages reach USD 1,000+ in a quarter (282-A:9). | US-NHS5-003, US-NHS5-005, US-NHS5-007 |
| Agricultural | Farm labor exempt from the NH minimum wage; wage-payment chapter excludes farm employers with fewer than 5 employees; UI follows FUTA 3306(c)(1); under-16 farm work needs no certificate. | US-NHS5-003, US-NHS5-005, US-NHS5-007, US-NHS5-014 |
| Minors | Under 16: certificate and hour limits. 16-17 in school: 35 h/week cap and signed parental permission. Pay: 75% of the minimum for ages 16 and under. Children under 21 employed by a parent are excluded from UI. | US-NHS5-014, US-NHS5-003, US-NHS5-007 |
| Tipped | Base 45% of the minimum = USD 3.27; tip credit with make-up; tips are the employee's property. | US-NHS5-003 |
| Clergy/religious | Ministers and members of religious orders, and church organizations, are excluded from UI (282-A:9). No wage-tax angle. | US-NHS5-007 |
| Students | Students working for their own school, college or hospital are excluded from UI. Subminimum or no wage only for approved programs (279:22-aa, Lab 805). | US-NHS5-007, US-NHS5-004 |
| Nonresident aliens | UI wages exclude payments to aliens not lawfully present (282-A:15 II(a)). No state withholding. | US-NHS5-007 |
| Statutory employees | No NH rule beyond federal. UI follows "employment" in 282-A:9 plus FUTA. Wage-payment uses the 7-criterion contractor test. | US-NHS5-005, US-NHS5-007 |
| Government employees | Reporting-pay rule does not apply to counties or municipalities (275:43-a). Compensatory time rules for public sector (275:43 VII). Elected county/municipal officials are not "employees" (Lab 803.05). | US-NHS5-011, US-NHS5-001, US-NHS5-004 |
| Family employees | Child employed by a parent or grandparent who provides maintenance is outside the minimum-wage chapter (279:26-a). Spouse or parent employed by a child, and a child under 21 employed by a parent, are outside UI. | US-NHS5-003, US-NHS5-007 |

## ACCESS gaps (exact URLs)
1. All nh.gov hosts returned HTTP 403 to curl from a non-US IP (VPN off), so the work went through Wayback. Hosts: https://gc.nh.gov/, https://www.gencourt.state.nh.us/, https://www.nhes.nh.gov/, https://www.dol.nh.gov/, https://www.revenue.nh.gov/, https://www.paidfamilymedicalleave.nh.gov/
2. https://gc.nh.gov/rules/state_agencies/emp300.html (NHES Emp 300 rules, incl. Emp 303.02 due dates): not in Wayback for 2024, 2025 or 2026, on either host.
3. https://www.gc.nh.gov/rsa/html/XXIII/275/275-37-f.htm (parental medical leave): direct 403, and the Wayback copy of 2026-06-17 is the 403 page.
4. https://www.nhes.nh.gov/employers/new-hire-reporting: 403. The statute was read instead.
5. NHES 0047 Electronic Wage Reporting instructions (file format for the quarterly wage file): not fetched. Wayback was rate-limiting (HTTP 429) during the run.

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **nh.meta.register_id_pattern** (blocking): 1 facts rest on active register rows whose ids (US-NH-P5-1-001) do not match the facts-schema register_id pattern ^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$ (multi-hyphen legacy ids). They are carried in full in _facts_pending_register_id_pattern and are NOT yet consumable facts. What would close it: Orchestrator decision: a PATCH of facts.schema.json loosening the register_id pattern (e.g. ^[A-Z]{2}-[A-Z0-9-]{2,16}-[0-9]{3,4}$), or register alias ids; then run _research/synthesis-B/_work-MN-WY/promote.py to move the pending facts into facts[].
- **nh.ui.rate.new_employer.confirm** (non-blocking): 1.7% new-employer rate is derived (2.7 - FBR 1.00), not stated on a page. What would close it: NHES Tax Rate Chart footnote or Emp 300 rule (NHES Employer Accounts).
- **nh.ui.wages.elective_deferrals** (non-blocking): 401(k)/section 125 treatment in NH UI wages is open (282-A:15 silent). What would close it: Emp 300 wage-definition rule or an NHES written answer.
- **nh.payslip.electronic** (non-blocking): Electronic pay statements not addressed in RSA 275:49 IV or Lab 803.03. What would close it: An NH DOL written opinion or FAQ.
- **nh.report.ui.due_and_penalties** (non-blocking): Quarterly due date, late fee and interest from the 2016 Handbook (A.3); Emp 303.02 not archived. What would close it: Emp 303.02 text via US IP or Chrome.
- **nh.leave.parental_medical** (non-blocking): RSA 275:37-f parental medical leave (25 h unpaid, 20+ employers) rests on MANUAL row US-NHS5-012; statute not read. What would close it: gc.nh.gov page read with US IP or Chrome, or 2025 HB 2 chaptered text.
- **nh.live.session_bills** (non-blocking): Final status of HB 1484 (minimum wage) and SB 416 (tips) rests on leads. What would close it: gc.nh.gov bill status pages (US IP).
- **nh.payslip.reach** (non-blocking): No territorial clause in RSA 275 for out-of-state work. What would close it: An NH DOL position.
- **nh.data.privacy_act** (non-blocking): RSA 507-H employee-data exemption not read. What would close it: RSA 507-H text.

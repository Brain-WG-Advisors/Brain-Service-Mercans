# CCG research pack - annex_MO (Missouri)

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_MO` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_MO-facts.json` (45 facts, 11 pending on the register_id pattern defect, 9 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/MO.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- Paid sick leave: NONE in 2026 - Prop A repealed by H.B. 567 effective 2025-08-28 [US-MOS5-003]. Do not model an accrual.
- Minimum wage 15.00 is frozen from 2026 (no CPI step); only a federal increase could change it [US-MOS5-002].
- UI wages: 401(k) deferrals INCLUDED, Section 125 EXCLUDED - differs from the state income-tax base [US-MOS5-012/-013].
- Oracle: MO 707.81/yr = 59/month (DOR example, married spouse works, 35,000). WTC uses DOR rounded bracket amounts (263).
- Amendment 7 (2026-11-03 ballot) is NOT enacted and has no 2026-2027 withholding effect [US-MOS5-021].

## 0.2 Register status check of the ids cited in the findings

These ids appear in the findings but are not plain `active`; do not cite them for a number:

- US-MOS5-014: partial

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `mo.minwage.hourly` | 13.75 USD | 2025-01-01 | 2025-12-31 | US-MOS5-002 | high |
| `mo.minwage.hourly` | 15.0 USD | 2026-01-01 |  | US-MOS5-002 | high |
| `mo.labour.minwage.indexation.active` | False | 2026-01-01 |  | US-MOS5-002 | high |
| `mo.labour.tip_credit.cash_wage.min_ratio` | 50 % | 2006-12-07 |  | US-MOS5-005 | high |
| `mo.minwage.tipped.cash_wage` | 7.5 USD | 2026-01-01 | 2026-12-31 | US-MOS5-010 | high |
| `mo.labour.minwage.small_retail_exemption.gross_volume` | 500000 USD | 2006-12-07 |  | US-MOS5-006 | high |
| `mo.overtime.weekly_threshold_hours` | 40 hours | 2008-08-28 |  | US-MOS5-011 | high |
| `mo.overtime.premium.multiplier` | 1.5 ratio | 2008-08-28 |  | US-MOS5-011 | high |
| `mo.wh.method` | annualise; minus standard deduction; 8 brackets of 1,348; / periods; round to whole dollar | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.std_deduction.single` | 16100 USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.std_deduction.married_nonworking_spouse` | 32200 USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.std_deduction.head_of_household` | 24150 USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.bracket.width` | 1348 USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.bracket.1.rate` | 0 % | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.bracket.2.rate` | 2 % | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.bracket.3.rate` | 2.5 % | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.bracket.4.rate` | 3 % | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.bracket.5.rate` | 3.5 % | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.bracket.6.rate` | 4 % | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.bracket.7.rate` | 4.5 % | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.bracket.8.rate` | 4.7 % | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.bracket.8.floor` | 9436 USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.rounding` | per-period tax rounded to whole dollar (49c down, 50c up) | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.wh.certificate` | no MO W-4: withhold at Single | 2025-01-01 |  | US-MOS5-020 | high |
| `mo.wh.supplemental.rate` | 4.7 % | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.reciprocity.states` | none | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.household.withholding_required` | False | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.oracle.example_1.annual_tax` | 707.81 USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.pit.oracle.example_1.monthly_withholding` | 59 USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.sui.employee.rate` | 0 % | 2026-01-01 |  | US-MOS5-013 | high |
| `mo.sui.wages.401k_included` | True | 2026-01-01 |  | US-MOS5-013 | high |
| `mo.sdi_pfml.exists` | False | 2026-01-01 |  | US-MOR3-001 | high |
| `mo.report.mo941.monthly_threshold` | 500 USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.report.mo941.quarter_monthly_threshold` | 9000 USD | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.report.w2.efile_threshold` | 250 | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.report.ui.quarterly_due` | Apr 30; Jul 31; Oct 31; Jan 31 | 2026-01-01 |  | US-MOS5-013 | high |
| `mo.newhire.report_days` | 20 days | 2026-01-01 | 2026-12-31 | US-MOS5-001 | high |
| `mo.leave.sick.state_statute.exists` | False | 2025-08-28 |  | US-MOS5-003 | high |
| `mo.final_pay.discharge` | day of discharge; penalty wages up to 60 days after 7-day written request | 1972-08-28 |  | US-MOS5-004 | high |
| `mo.term.service_letter.days` | 45 days | 1982-08-28 |  | US-MOS5-009 | high |
| `mo.garn.creditor.max_percent` | 25 % | 1979-01-02 |  | US-MOS5-007 | high |
| `mo.garn.consumer.head_of_family.max_rate` | 10 % | 1979-01-02 |  | US-MOS5-007 | high |
| `mo.garn.iwo.employer_fee.monthly` | 6 USD | 2014-08-28 |  | US-MOS5-017 | high |
| `mo.garn.iwo.remit_business_days` | 7 days | 2014-08-28 |  | US-MOS5-017 | high |
| `mo.data.ssn.employee_number_prohibited` | True | 2012-08-28 |  | US-MOS5-016 | high |
| `mo.labour.pay_frequency.corporations` | at least semimonthly, within 16 days of period close | 1955-08-28 |  | US-MOP52-002 (promoted, Synthesis C) | high |
| `mo.pit.local.st_louis.earnings_tax.rate` | 1 % | 2026-01-01 |  | US-MOP52-006 (promoted, Synthesis C) | medium |
| `mo.pit.local.st_louis.payroll_expense_tax.rate` | 0.5 % | 2026-01-01 |  | US-MOP52-006 (promoted, Synthesis C) | medium |
| `mo.pit.local.kansas_city.earnings_tax.rate` | 1 % | 2026-01-01 |  | US-MOP52-006 (promoted, Synthesis C) | medium |
| `mo.sui.wage_base` | 9000 USD | 2026-01-01 | 2026-12-31 | US-MOB5-403 (promoted, Synthesis C) | high |
| `mo.sui.wage_base` | 9500 USD | 2025-01-01 | 2025-12-31 | US-MOB5-403 (promoted, Synthesis C) | high |
| `mo.sui.new_employer.rate` | 2.376 % | 2026-01-01 | 2026-12-31 | US-MOB5-403 (promoted, Synthesis C) | high |
| `mo.sui.employer.rate.max` | 6.0 % | 2026-01-01 | 2026-12-31 | US-MOB5-403 (promoted, Synthesis C) | high |
| `mo.payslip.deduction_statement` | statement of total deductions at least monthly | 1955-08-28 |  | US-MOP52-002 (promoted, Synthesis C) | high |
| `mo.records.retention_years` | 3 years | 2006-12-07 |  | US-MOB5-402 (promoted, Synthesis C) | high |
| `mo.prevailing_wage.threshold` | 75000 USD | 2018-08-28 |  | US-MOB5-401 (promoted, Synthesis C) | high |

# Findings by domain (stage 5)

## 1 — labour_code
- **Minimum wage:**
  - USD 13.75 from 2025-01-01, then **USD 15.00 from 2026-01-01**, or the federal rate if it is higher (290.502(3)). [US-MOS5-002, A.1]
  - The DOLIR minimum-wage page shows the same USD 15.00 for 2026. It is a second independent document family. [US-MOS5-010, A.2]
  - Since 2025-08-28 the law also covers public employers (290.502(4)).
  - **2027:** no increase is enacted. Indexation in subs. 2 stopped on 2024-12-31, and the H.B. 567 text has no CPI step. The rate stays USD 15.00 unless the federal rate rises above it. Confidence: high.
- **Local minimum wages:** none appear in the statute or on the DOLIR page. 290.502 is statewide. Confidence: medium, because no explicit preemption section was read (RSMo 67.1571 was not fetched).
- **Exclusions (290.500(3)):** these workers are not "employees" under the minimum-wage law [US-MOS5-006]:
  - bona fide executive, administrative or professional (EAP) employees;
  - retail or service businesses with annual gross volume under USD 500,000. DOLIR repeats this. [US-MOS5-010]
  - occasional work at a private residence of 6 hours or less;
  - casual babysitting;
  - government positions under 29 USC 203(e)(2)(C);
  - workers covered by 29 USC 213(a)(8);
  - commission salespeople whose hours and place of work the employer does not control;
  - students whose work offsets tuition;
  - offenders.

  Learners and apprentices: under age 20, for at most 3 months (6 months by exception).
- **Tipped employees:** the employer pays at least 50% of the minimum wage, which is **USD 7.50 in 2026** (15.00 x 0.5), and tops up total pay to USD 15.00 (290.512). [US-MOS5-005, US-MOS5-010]
- **Overtime:** 1.5x the regular rate above 40 hours a week. Amusement and recreation businesses (29 USC 213(a)(3)) pay overtime above 52 hours. Anyone exempt under the FLSA is exempt. There is no daily overtime (290.505; DOLIR page). [US-MOS5-011, US-MOS5-022, high]
- **Pay frequency:** corporations pay at least semimonthly, within 16 days of the close of the pay period (290.080). [US-MOP52-002, already registered]
- **Wage reduction:** needs 30 days' advance written notice. The penalty is USD 50 per affected person. [US-MOS5-022, A.3; the underlying statute, RSMo 290.100, was not fetched]
- **Method of payment** (direct deposit or paycard consent): no Missouri provision was located in the sources read. Open question MO-OQ-4.
- **Breaks:** none are required for adults. Youth in the entertainment industry get a meal break before 5.5 hours and a 15-minute rest every 2 hours. [US-MOS5-022]

## 2 — income_tax
- **Method for 2026** (Form 4282 Rev. 03-2026, published December 2025) [US-MOS5-001, A.2; formula also in US-MOPIT-001]:
  - Annualise wages: x260 daily, x52 weekly, x26 biweekly, x24 semimonthly, x12 monthly.
  - Subtract the standard deduction:
    - Single, Married with a working spouse, and Married filing separately: **16,100**;
    - Married with a non-working spouse: **32,200** (a check box on MO W-4 line 1, not a separate filing status);
    - Head of household: **24,150**.
  - Apply the annual brackets, each **1,348** wide:

    | Missouri taxable income (annual) | Rate |
    |---|---|
    | 0 – 1,348 | 0% |
    | 1,348 – 2,696 | 2% |
    | 2,696 – 4,044 | 2.5% |
    | 4,044 – 5,392 | 3% |
    | 5,392 – 6,740 | 3.5% |
    | 6,740 – 8,088 | 4% |
    | 8,088 – 9,436 | 4.5% |
    | over 9,436 | **4.7%** |

  - Divide by the number of pay periods and **round to the nearest whole dollar** (49 cents down, 50 cents up).
- **G-DERIVE:**
  - The DOR example (married, spouse works, wages 35,000): taxable income 18,900. The lower brackets give 27 + 34 + 40 + 47 + 54 + 61 = 263. The excess is 9,464 x 4.7% = 444.81. Total 707.81 a year, or **59 a month**. Re-computed in Python: 707.808, matching.
  - The DOR example rounds each lower-bracket amount to whole dollars (263). Unrounded, the lower brackets give 1,348 x 19.5% = 262.86, for a total of 707.67 instead of 707.81. The difference (0.14 a year) disappears in the per-period rounding. The WTC should use the DOR table amounts.
  - The 4.7% rate itself also reconciles: 4.95 (2023) - 0.15 (subs. 3) - 0.10 (one subs. 4 step) = **4.70** (RSMo 143.011). [US-MOS5-018]
  - The bracket width is CPI-indexed (143.011(5)): 1,348 = 1,000 x 1.348.
  - The standard deductions equal the 2026 federal amounts. RSMo 143.131 was not read, so this tie is a residual.
- **Certificate:** Form **MO W-4 Rev. 12-2024** [US-MOS5-020]:
  - Line 1: filing status. Line 2: additional amount. Line 3: a fixed amount that replaces the standard calculation. Line 4: EXEMPT (renewed every year; MSRRA military spouse; active-duty military pay).
  - There is no allowance count.
  - With no MO W-4 on file, withhold at Single.
  - Nonresidents use MO W-4A (Missouri percentage of the table amount). A resident working in a lower-rate state has the difference withheld unless they file the MO W-4C affidavit. [US-MOS5-001]
- **Supplemental wages:**
  - Paid with regular wages: aggregate method.
  - Paid separately: a flat **4.7%** or the aggregate method.
  - If no tax was withheld from regular wages: aggregate method only.
  - Tips follow the supplemental options. Vacation pay paid in addition to regular pay counts as supplemental. [US-MOS5-001]
- **Wages** have the same meaning as for federal withholding (4282 s.4). Household employers are **not required** to withhold; withholding is voluntary by agreement. [US-MOS5-001]
- **Reciprocity:** none with any state. [US-MOS5-001, US-MOP51-001]
- **Local income taxes (T4)** [US-MOP52-006, US-MOP7-001/-002, US-MOP9W-001, already registered A.2]:
  - **St. Louis City earnings tax:** 1%, withheld from employees who live or work in the city.
  - **St. Louis payroll expense tax:** 0.5%, paid by the employer.
  - Both are filed quarterly on W-10/P-10 to the Collector of Revenue.
  - **Kansas City earnings tax:** 1% on residents and on nonresidents for work done in KC. Employers in KC withhold. Nonresident businesses may register to withhold (RD-100), and then must withhold. Remitted to the KC Revenue Division at the state withholding frequency.
  - Both are separate from the state return.
  - Not re-fetched this round (rule: reuse active A.2 rows). See MO-OQ-1 on the April 2026 renewal votes.
- **Interstate transport employees:** 49 USC 11502/14503/40116 apply (residence-state rule; for air and water carriers, the more-than-50% state). [US-MOS5-001]

## 3 — social_security (SUI; no SDI/PFML)
- **Agency:** DOLIR Division of Employment Security (DES).
- **2026 wage base: USD 9,000** (2025: 9,500; 2024: 10,000). [US-MOB5-403, A.2; US-MOS5-013, A.3]
  - Mechanism (288.036(2)): based on the 4-quarter average trust-fund balance. At or below 350M the base rises by 1,000; at or above 650M it falls by 500. The floor is 7,000 and the cap 13,000.
  - **G-DERIVE:** 9,500 - 500 = 9,000, which is the >=650M branch. [US-MOS5-012]
  - Caveat: the Revisor flags the displayed H.B. 150 (2015) version of 288.036 as declared unconstitutional (*Pestka v. State*, SC95369, 2016). The DES guide restates the same wage-base rule.
- **New-employer rate 2026: 2.376%** (all others, mining, construction); 1.00% for 501(c)(3) organisations.
  - Experience rates run 0.0% to 6.0%, plus the CRA and the maximum-rate surcharge (0.25% steps, at most 1.5%).
  - The 2026 CRA is a **12% reduction**, derived: 2.376 / 2.7 = 0.88.
  - The automation-fund redirect is at most 0.020%, with no extra tax.
  - Missouri is **not** a FUTA credit-reduction state, and no federal interest assessment is expected for 2026.

  [US-MOB5-403, US-MOP9W-002, already registered]
- **Employee contribution:** none. No part of the UI tax may be deducted from pay. [US-MOS5-013]
- **Wages for UI** (288.036(1)):
  - Included: commissions, bonuses, non-cash pay, FUTA-reportable tips, and 401(k) elective deferrals (the DES guide says these are reportable).
  - Excluded: employer plan payments for sickness, medical costs or death; 401(a) and 404(a)(2) payments; Section 125 cafeteria-plan payments that are not FUTA wages.
  - Domestic and agricultural workers: cash wages only.

  [US-MOS5-012, US-MOS5-013]
- **Coverage thresholds:** USD 1,500 in a quarter or one worker in 20 weeks; domestic USD 1,000 cash in a quarter; agricultural 10 or more workers in 20 weeks or USD 20,000 cash in a quarter; governments, any worker. [US-MOS5-013, US-MOS5-014]
- **SDI/TDI/PFML:** none. Missouri is absent from the DOL TDI and PFML lists. [US-MOR3-001, US-FEDP52-007, already registered]
- **Other employer levies:** the P7/P9 list stands (St. Louis payroll expense tax 0.5%; UI surcharge and CRA). Not redone.
- **MULTI hand-off (UI credit for wages reported to another state):** the 288.036 text read does **not** contain a wage-base credit for wages reported to another state. The DES guide covers localization (localized, base of operations, direction and control, residence, plus the Interstate Reciprocal Coverage election) but not that credit. Status: open (MO-OQ-2).

## 4 — payslip_statute
- **Required content:** a statement of total deductions at least once a month, with the check or separately (290.080). Breach is a misdemeanour with a fine of USD 50–500. [US-MOP52-002]
- No itemised pay-statement statute exists in ch. 290 (index read). [US-MOP52-004]
- **Records:** kept 3 years: name, address, occupation, rate, amount paid each period, and hours per day and per week (290.520). [US-MOB5-402]
- **Electronic delivery:** no rule located.
- **Language:** none required (290.080). [US-MOL-001]
- **Multistate reach** (MULTI hand-off): 290.080 binds "corporations" with no territorial test in the text. Default: the work-location rule.

## 5 — reporting_instruments
- **Withholding return MO-941** (frequency assigned by DOR) [US-MOS5-001, A.2]:

  | Frequency | Applies when | Due |
  |---|---|---|
  | Monthly | USD 500 or more in 2 of the prior 12 months | 15th of the next month; for quarter-end months, the last day of the next month (2026 table: Feb 17, Mar 16, Apr 30, May 15, Jun 15, Jul 31, Aug 17, Sep 15, Nov 2, Nov 16, Dec 15; Feb 1, 2027) |
  | Quarterly | USD 100 or more in any quarter | Apr 30, Jul 31, Nov 2, Feb 1 2027 |
  | Annual | under USD 100 in every quarter | Feb 1, 2027 |

  - **Quarter-monthly payments:** required at USD 9,000 or more in each of 2 months of the prior 12. Periods are days 1–7, 8–15, 16–22 and 23–end. Pay within 3 banking days, electronically. Safe harbour: 90%.
  - File a zero return even when nothing was withheld.
  - Timely-filing compensation deduction: 2% / 1% / 0.5% by year-to-date tax (0–5,000 / 5,001–10,000 / over 10,000).
  - 2026 interest rate: 7%.
- **State W-2:** W-2s and 1099-R with the **MO W-3** by the last day of January if filed electronically, or by the end of February on paper.
  - Employers with **250 or more W-2s must file electronically in EFW2** (with the RV record carrying the MO W-3 data).
  - The fourth-quarter MO-941 is filed separately.
  - 1099s go through the CF/SF program.

  [US-MOS5-001]
- **Quarterly UI report: Contribution and Wage Report MODES-4** (instructions MODES-4-5) [US-MOS5-013]:
  - Contents: name, SSN, quarterly wages, separation dates, and probationary flag "P" with dates (28 days or less).
  - Due the last day of the month after the quarter: Apr 30, Jul 31, Oct 31, Jan 31.
  - Filed on **UInteract** (Method B upload; payroll services use NASWA/ICESA). Employers with 50 or more employees who file W-2s electronically with SSA must file this report electronically. Specification: M-INF-368.
  - Penalty: the greater of 10% or USD 100.
- **New hire:** report within **20 days** of hire to the Missouri DOR, as a copy of the MO W-4 or an equivalent (P.O. Box 3340 or fax 573-526-8079) (4282 s.8).
  - Minimum fields (285.304): employee name, address, SSN and first day of work; employer name, address and FEIN; plus the signature or hire date if a non-W-4 form is used.

  [US-MOS5-001, US-MOS5-008]
- **Registration:**
  - DOR: Form 2643 or the online MyTax Missouri portal.
  - DES: UInteract / MODES-2699.
  - Newly liable employers get a 30-day extension.

  [US-MOS5-001, US-MOS5-013]

## 6 — leave
- **Paid sick leave:** **none in 2026.** Proposition A (2024) earned paid sick time was repealed by H.B. 567, effective 2025-08-28; 290.600 shows "(Repealed L. 2025 H.B. 567, et al.)". DOLIR confirms that paid sick leave and vacation are at the employer's discretion. [US-MOS5-003, A.1; US-MOS5-022]
- Missouri has no PFML benefit program. [US-MOR3-001]
- No state job-protected illness leave exists beyond the federal FMLA. [US-MOS5-022]
- **MULTI hand-off (sick-leave coverage of employees working partly in the state):** not applicable, because there is no statute.

## 7 — termination
- **Discharge** (290.110) [US-MOS5-004, A.1; US-MOS5-022]:
  - Wages are due **on the day of discharge**.
  - If they are unpaid 7 days after the employee's written request, penalty wages run at the same rate up to **60 days**.
  - Commission employees whose pay needs an audit are excepted.
- **Resignation:** no statutory deadline; pay falls due on the regular payday. The ch. 290 index shows no such section.
- **Accrued vacation payout:** not required by statute; the employer's policy or contract governs. [US-MOS5-022]
- **Service letter** (290.140): corporations with 7 or more employees; the employee has 90 or more days of service and sends a request by certified mail within 1 year; the letter is due within 45 days. [US-MOS5-009]
- **IWO employees:** notify the Family Support Division within 10 days of termination. [US-MOS5-017]
- No state WARN act was located (not searched further; not payroll-relevant).

## 8 — benefits_in_kind
- Missouri AGI for residents = federal AGI with listed modifications (143.121). No addition-back exists for 401(k), Section 125, HSA, transit or group-term life. Withholding wages follow the federal definition. **Missouri conforms** to the federal exclusions. [US-MOS5-015, US-MOS5-001]
- **UI difference:** 401(k) elective deferrals **are** UI wages, while Section 125 payments are not. [US-MOS5-012, US-MOS5-013]
- Minimum-wage credit for goods and services: fair market value, computed weekly (290.512(2)). [US-MOS5-005]

## 9 — deductions_garnishments
- **Creditor garnishment** (525.030): the least of 25%, the excess over 30x the federal minimum wage, or **10% if the employee is head of a family and a Missouri resident**. This is stricter than the CCPA. [US-MOS5-007, A.1]
  - The limits do not apply to support orders, Chapter XIII orders or tax debts.
  - Conversions: a month = 4 1/3 weeks; a semimonthly period = 2 1/6 weeks.
  - No discharge for a single garnishment.
- **Child support IWO** (454.505) [US-MOS5-017, A.1]:
  - Binding 2 weeks after service.
  - **Employer fee up to USD 6 a month**, within the CCPA limits.
  - Remit **within 7 business days** of payday.
  - Takes priority over other state process; concurrent support orders are paid pro rata.
  - Report termination within 10 days.
  - Anti-retaliation, with a 30-day presumption.
  - Out-of-state orders follow the law of the principal place of employment.
- **Wage deductions:** allowed for shortages or damage as long as pay stays at or above minimum wage. [US-MOS5-022]

## 10 — collective_agreements (prevailing wage)
- RSMo 290.210–290.340 [US-MOB5-401, already registered]:
  - Prevailing hourly rate on public works.
  - Overtime 1.5x above 10 hours a day or 40 hours a week; 2x on Sundays and holidays.
  - Does not apply to projects of USD 75,000 or less.
- Certified-payroll form and filing were not re-read this round (MO-OQ-5).

## 11 — indexation
- **Minimum wage:** no longer indexed after 2026 (H.B. 567). [US-MOS5-002]
- **Income-tax brackets:** CPI-U indexed every year (143.011(5)). DOR publishes the new brackets from October 1 and puts them in Form 4282 (2026 width: 1,348). [US-MOS5-018]
- **Top rate:** revenue-triggered 0.1-point cuts; up to two more remain (4.6%, then 4.5%). [US-MOS5-018]
- **SUI wage base:** set by the trust-fund balance (+1,000 / -500), published on the DES tax-rates page. [US-MOS5-012, US-MOB5-403]
- **New-employer rate:** carries the annual CRA (derived at -12% for 2026).

## 12 — data_protection
- **SSN** (407.1355): an SSN may not be publicly displayed to the public or to co-workers, nor used (or, since 2016, its last four digits) as an employee number. It may not be sent over the internet unless the connection is secure. There is **no explicit pay-statement truncation rule**; apply the federal or W-2 truncation practice. [US-MOS5-016]
- **Breach notice** (407.1500): "redacted" means no more than 5 SSN digits are visible. Notify affected residents without unreasonable delay; also notify the Attorney General and the credit-reporting agencies when more than 1,000 residents are affected. Civil penalty up to USD 150,000. [US-MOS5-019]

## 13 — live_legal_change
- **H.B. 567 (2025), in force 2025-08-28:**
  - Paid sick leave repealed (operates at the leave/payroll accrual level).
  - Minimum-wage indexation after 2026 removed (rate level).
  - Public employers brought under the minimum wage.

  [US-MOS5-002, US-MOS5-003]
- **Amendment 7** (SS SCS SJR 95; endowment fund aimed at eventually ending state taxes) [US-MOS5-021]:
  - Status: proposed constitutional amendment on the **2026-11-03** ballot, **not enacted**.
  - The fair ballot language says it has no immediate tax impact.
  - Level: none for 2026–2027 withholding.
- **2027 income-tax rate:** not yet published. A cut to 4.6% depends on the 143.011(4) revenue trigger, and the 2027 Form 4282 is not out. [US-MOS5-018] (MO-OQ-3)
- No other 2026 change was found in the sources read. **Limit:** the DOR, DES and DOLIR news pages were not swept (403), so the bulletin sweep for MO is **partial**.

## Special populations (state level)
| Population | Missouri rule | register_id |
|---|---|---|
| Domestic / household | Income-tax withholding not required (voluntary by agreement). UI covered at USD 1,000 cash in a quarter, cash wages only. Minimum wage excludes occasional private-residence work of 6 h or less and casual babysitting. | US-MOS5-001, US-MOS5-013, US-MOS5-014, US-MOS5-006 |
| Agricultural | UI covered at 10+ workers in 20 weeks or USD 20,000 cash in a quarter; cash wages only. Minimum wage excludes 29 USC 213(a)(8) small farms. | US-MOS5-013, US-MOS5-014, US-MOS5-006 |
| Minors | Minimum wage applies (learners under 20 have time limits). Child-labour hours (RSMo ch. 294) not fetched. Entertainment-industry youth break rules apply. | US-MOS5-006, US-MOS5-022 |
| Tipped | Cash wage at least 50% (USD 7.50 in 2026) plus a top-up to USD 15.00. Withholding on reported tips uses the supplemental options. | US-MOS5-005, US-MOS5-001 |
| Clergy / religious | UI excludes church employment and ministers in their ministry. Withholding follows federal (ministers' wages exempt from mandatory withholding under federal rules; no Missouri override found). | US-MOS5-014, US-MOS5-001 |
| Students | UI excludes students working for their own school, credited work-study, and full-time students at summer camps under 13 weeks. Minimum wage excludes tuition-offset work. | US-MOS5-014, US-MOS5-006 |
| Nonresident aliens | No state rule beyond federal (wages defined federally, 4282 s.4). Withholding on Missouri-source work. | US-MOS5-001 |
| Nonresidents (US) | Fully withheld if all work is in MO. Partial work: MO W-4A percentage. No reciprocity. | US-MOS5-001 |
| Military / military spouses | Active-duty income is exempt from withholding. MSRRA spouse exemption requires verification. | US-MOS5-001, US-MOS5-020 |
| Statutory employees | No state rule beyond federal (wage definition follows federal). | US-MOS5-001 |
| Government employees | Covered by the state minimum wage since 2025-08-28. UI: any worker. Minimum wage excludes 29 USC 203(e)(2)(C) positions. | US-MOS5-002, US-MOS5-013, US-MOS5-006 |
| Transport (rail, motor, air) | Federal residence-state limits (49 USC 11502/14503/40116). | US-MOS5-001 |

## MULTI hand-offs (MO answers)
- **SUI wage-base credit for wages reported to another state:** not found in 288.036 or the DES guide. Open (MO-OQ-2).
- **PFML/SDI coverage:** not applicable; Missouri has no program.
- **Paid-sick-leave coverage:** not applicable; repealed 2025-08-28.
- **Pay-statement reach:** 290.080 has no territorial clause. Default: the work-location state.

## ACCESS gaps (exact URLs)
- `https://revisor.mo.gov/main/OneSection.aspx?section=290.505` (and every section after the 8th direct read): HTTP 000, timeout. Served through Wayback.
- `https://dss.mo.gov/child-support/employers/new-hire-reporting.htm`: 403. The Wayback copy redirects to the generic employers page (2025-06-10), which has no deadline text.
- `https://labor.mo.gov/DLS/MinimumWage`: 403 (Wayback 2026-10-16 used).
- `https://dor.mo.gov/forms/MO%20W-4.pdf`: 403 (Wayback 2026-08-18 used).
- `https://www.sos.mo.gov/elections/petitions/2026BallotMeasures`: 403 (Wayback 2026-09-27 used).
- `https://labor.mo.gov/dls/faqs` and `https://labor.mo.gov/dls/wages-hours-dismissal-rights`: Wayback 404 (the correct page is `/dls/general`, which was used).

## Confidence by domain
labour_code 90% · income_tax 95% (state) / 80% (local, pending MO-OQ-1) · social_security 90% · payslip 85% · reporting 90% · leave 95% · termination 90% · BIK 85% · garnishment 95% · prevailing wage 75% · indexation 90% · data protection 85% · live change 70% (sweep partial).

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **mo.pit.local.renewal_status** (non-blocking): St. Louis and Kansas City earnings-tax April 2026 renewal votes not verified; RSMo 92.105-92.125 not read. What would close it: Certified April 7, 2026 results (St. Louis Board of Election Commissioners, KC Election Board) or Collector of Revenue / KC Revenue Division 2026 pages.
- **mo.sui.wage_base.other_state_credit** (non-blocking): 288.036 text read has no wage-base credit for wages reported to another state; DES guide silent. What would close it: In-force RSMo 288.036 (non-H.B. 150 version), DES MODES-4-5 taxable-wage instructions, or DOL Significant Provisions 2026.
- **mo.pit.bracket.next_year** (non-blocking): 2027 top rate and brackets not published (revenue trigger 143.011(4)). What would close it: DOR 2027 Form 4282 (expected December 2026).
- **mo.payment.method** (non-blocking): No Missouri direct-deposit/paycard consent or electronic pay-statement rule located. What would close it: Revisor full-text search of RSMo ch. 290 and the DOLIR FAQ.
- **mo.prevailing_wage.certified_payroll** (non-blocking): Certified-payroll form and filing (290.290) and current annual wage order not read. What would close it: DLS Prevailing Wage pages (labor.mo.gov/dls/prevailing-wage).
- **mo.labour.child_labour** (non-blocking): Child-labour hours and work certificates not fetched. What would close it: RSMo 294.021-294.030 on the Revisor site.
- **mo.pit.std_deduction.federal_tie** (non-blocking): Tie of the standard deductions to the federal amounts (143.131) not read. What would close it: RSMo 143.131 in-force text.
- **mo.live.bulletin_sweep** (non-blocking): DOR/DES/DOLIR news pages 403; bulletin sweep partial. What would close it: Chrome pass over dor.mo.gov/news and labor.mo.gov/news.

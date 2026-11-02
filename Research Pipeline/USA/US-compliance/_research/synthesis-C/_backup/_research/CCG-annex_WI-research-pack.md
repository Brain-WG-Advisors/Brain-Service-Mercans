# CCG research pack - annex_WI (Wisconsin)

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_WI` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_WI-facts.json` (43 facts, 13 pending on the register_id pattern defect, 7 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/WI.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- W-166 WITHHOLDING TABLES (3.54/4.65/5.30/7.65%) != STATUTORY ASSESSMENT BRACKETS (3.50/4.40/5.30/7.65%) - WTC uses W-166 only.
- Oracle: W-166 examples 7.59 / 14.34 / 22.08 (1-cent annual residual only).
- Garnishment max 20% (stricter than CCPA). Schedule D UI for 2026 and 2027.

## 0.2 Register status check of the ids cited in the findings

These ids appear in the findings but are not plain `active`; do not cite them for a number:

- US-WIR3-005: MANUAL

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `wi.minwage.hourly` | 7.25 USD | 2009-07-24 |  | US-WIS5-001 | high |
| `wi.labour.minwage.opportunity.hourly` | 5.9 USD | 2009-07-24 |  | US-WIS5-001 | high |
| `wi.local_mandates.preempted` | True | 2009-07-24 |  | US-WIS5-001 | high |
| `wi.minwage.tipped.cash_wage` | 2.33 USD | 2009-07-24 |  | US-WIS5-002 | high |
| `wi.labour.lodging_credit.weekly` | 58 USD | 2009-07-24 |  | US-WIS5-001 | high |
| `wi.overtime.weekly_threshold_hours` | 40 hours | 2003-12-01 |  | US-WIS5-003 | high |
| `wi.overtime.premium.multiplier` | 1.5 ratio | 2003-12-01 |  | US-WIS5-003 | high |
| `wi.pay_frequency.rule` | at least monthly, wages to a day max 31 days before payment | 2026-01-01 |  | US-WIS5-004 | high |
| `wi.labour.direct_deposit.employer_may_require` | True | 2026-01-01 |  | US-WIS5-005 | medium |
| `wi.wh.method` | W-166 (1/26) wage-bracket tables or alternate formula | 2022-01-01 |  | US-WIS5-011 | high |
| `wi.pit.statutory.rates` | 3.50;4.40;5.30;7.65 | 2025-01-01 |  | US-WIS5-010 | high |
| `wi.pit.oracle.example_1.withholding` | 7.59 USD | 2022-01-01 |  | US-WIS5-011 | high |
| `wi.pit.oracle.example_2.withholding` | 14.34 USD | 2022-01-01 |  | US-WIS5-011 | high |
| `wi.pit.oracle.example_3.withholding` | 22.08 USD | 2022-01-01 |  | US-WIS5-011 | high |
| `wi.pit.rounding` | none stated | 2026-01-01 |  | US-WIS5-011 | high |
| `wi.wh.certificate` | WT-4; federal W-4 not accepted; none = zero exemptions | 2026-01-01 |  | US-WIS5-011 | high |
| `wi.pit.nonresident.de_minimis` | 1500 USD | 2026-01-01 |  | US-WIS5-011 | high |
| `wi.reciprocity.states` | IL;IN;KY;MI (W-220); MN arrangement | 2026-01-01 |  | US-MULTI-006 | high |
| `wi.local_wage_tax.exists` | False | 2026-01-01 |  | US-WIR3-001 | high |
| `wi.sui.wage_base` | 14000 USD | 2013-01-01 |  | US-WIS5-014 | high |
| `wi.ui.schedule.in_effect` | D | 2026-01-01 | 2027-12-31 | US-WIS5-019 | high |
| `wi.sui.employer.rate.max` | 12.0 % | 2026-01-01 | 2027-12-31 | US-WIS5-019 | high |
| `wi.ui.rate.new_employer.small` | 3.05 % | 2026-01-01 | 2027-12-31 | US-WIS5-019 | high |
| `wi.ui.rate.new_employer.large` | 3.25 % | 2026-01-01 | 2027-12-31 | US-WIS5-019 | high |
| `wi.sui.employee.rate` | 0 % | 2026-03-16 |  | US-WIR3-003 | high |
| `wi.sdi_pfml.exists` | False | 2024-03-01 |  | US-WIR3-004 | high |
| `wi.records.retention_years` | 3 years | 2009-07-24 |  | US-WIS5-002 | high |
| `wi.report.wt7.due` | January 31 (TY2026: February 1, 2027) | 2026-01-01 |  | US-WIS5-016 | high |
| `wi.report.w2.efile_threshold` | 10 | 2026-01-01 |  | US-WIS5-012 | high |
| `wi.report.ui.quarterly_due` | end of month after quarter | 2026-03-16 |  | US-WIS5-013 | high |
| `wi.newhire.report_days` | 20 days | 2026-03-16 |  | US-WIS5-013 | high |
| `wi.leave.sick.state_statute.exists` | False | 2026-01-01 |  | US-WIS5-006 | high |
| `wi.leave.wfmla.employer_threshold` | 50 | 2026-01-01 |  | US-WIS5-006 | high |
| `wi.final_pay.rule` | earlier of next regular payday or 31-day limit (quit and discharge) | 2026-01-01 |  | US-WIS5-004 | high |
| `wi.term.vacation.payout` | payable if written policy with no written forfeiture clause | 2026-01-01 |  | US-WIS5-005 | medium |
| `wi.term.plant_closing.notice_days` | 60 days | 2026-01-01 |  | US-WIS5-004 | high |
| `wi.bik.wi.box16_differences` | IRC 112, 127, 128, 129 (above WI exemption), 132 moving/bicycle | 2026-01-01 |  | US-WIS5-016 | high |
| `wi.bik.transit_parking.monthly` | 340 USD | 2026-01-01 | 2026-12-31 | US-WIS5-016 | high |
| `wi.garn.creditor.max_percent` | 20 % | 2026-01-01 |  | US-WIS5-008 | high |
| `wi.garn.garnishee_fee` | 15 USD | 2026-01-01 |  | US-WIS5-008 | high |
| `wi.garn.iwo.remit_days` | 5 days | 2026-01-01 |  | US-WIS5-009 | high |
| `wi.garn.iwo.employer_fee.per_payment` | 3 USD | 2026-01-01 |  | US-WIS5-009 | high |
| `wi.data.breach.notice_days` | 45 days | 2026-01-01 |  | US-WIS5-018 | high |
| `wi.pit.wh.bracket.1.ceiling` | 12760 USD | 2022-01-01 |  | US-WI-P5-1-001 (PENDING id pattern) | high |
| `wi.pit.wh.bracket.1.rate` | 3.54 % | 2022-01-01 |  | US-WI-P5-1-001 (PENDING id pattern) | high |
| `wi.pit.wh.bracket.2.ceiling` | 25520 USD | 2022-01-01 |  | US-WI-P5-1-001 (PENDING id pattern) | high |
| `wi.pit.wh.bracket.2.rate` | 4.65 % | 2022-01-01 |  | US-WI-P5-1-001 (PENDING id pattern) | high |
| `wi.pit.wh.bracket.3.ceiling` | 280950 USD | 2022-01-01 |  | US-WI-P5-1-001 (PENDING id pattern) | high |
| `wi.pit.wh.bracket.3.rate` | 5.3 % | 2022-01-01 |  | US-WI-P5-1-001 (PENDING id pattern) | high |
| `wi.pit.wh.bracket.4.rate` | 7.65 % | 2022-01-01 |  | US-WI-P5-1-001 (PENDING id pattern) | high |
| `wi.pit.wh.std_deduction.single` | 6702 USD | 2022-01-01 |  | US-WI-P5-1-001 (PENDING id pattern) | high |
| `wi.pit.wh.std_deduction.married` | 9461 USD | 2022-01-01 |  | US-WI-P5-1-001 (PENDING id pattern) | high |
| `wi.pit.wh.exemption` | 400 USD | 2022-01-01 |  | US-WI-P5-1-001 (PENDING id pattern) | high |
| `wi.pit.supplemental.flat_rates` | 3.54 (0-12,760); 4.65 (to 25,520); 5.30 (to 280,950); 7.65 (above) by estimated annual gross | 2022-01-01 |  | US-WI-P5-1-001 (PENDING id pattern) | high |
| `wi.payslip.items` | hours worked, rate, amount and reason for each deduction | 2026-01-01 |  | US-WI-P5-2-001 (PENDING id pattern) | high |
| `wi.prevailing_wage.exists` | False | 2026-01-01 |  | US-WI-P5-2-002 (PENDING id pattern) | medium |

# Findings by domain (stage 5)

## 1. labour_code
- **Minimum wage**: 7.25/h from 2009-07-24, for minors as well (Wis. Stat. 104.035(1)(a),(2)(a)). [US-WIS5-001, A.1]
  - The opportunity employee rate is 5.90/h. It applies to employees under 20 during their first 90 consecutive days (104.035(2m); DWD 272.01(11), 272.03(1)). [US-WIS5-001, US-WIS5-002]
  - No increase is scheduled for 2026 or 2027 in the 10-1-26 text.
- **Local minimum wage: none.** 104.001(2) bars city, village, town or county minimum-wage ordinances, and ordinances in effect on 2005-06-16 are void. [US-WIS5-001]
- **Tipped employees**: the cash wage is 2.33/h (2.13/h for opportunity employees). [US-WIS5-002]
  - The tip credit needs a tip declaration signed by the employee **every pay period**.
  - Payroll records must also show that tips plus wages reach the minimum each week. Otherwise no credit is allowed (DWD 272.03(2)(b)).
- **Meal and lodging credits**: lodging 58/week or 8.30/day; meals 87/week or 4.15/meal (104.035(1)(b)). [US-WIS5-001]
- **Overtime**: 1.5x the regular rate over 40 hours per week, with no daily overtime (DWD 274.03). [US-WIS5-003, A.1]
  - Exemptions are read consistently with the FLSA (274.04).
  - Household domestic service is outside the chapter (274.015).
- **Pay frequency**: at least monthly, covering wages earned up to a day no more than 31 days before payment (Wis. Stat. 109.03(1)). [US-WIS5-004, A.1]
  - Logging and farm labour: at least quarterly.
  - Exceptions: CBAs, school-year staff paid over 12 months, comp time.
- **Method of payment**: the employer may require direct deposit at no cost to the employee. A stub is still due, showing rate, hours and each deduction. [US-WIS5-005, A.3]
  - No paycard-specific rule was located in what was read.
- Confidence: high for minimum wage, overtime and frequency (A.1). The DD and paycard point rests on the DWD page (A.3).

## 2. income_tax
- **Method**: wage-bracket tables, or the alternate formula, from Publication W-166 (1/26). [US-WI-P5-1-001, US-WIS5-011, A.2]
  - Statutory basis: 71.64(1). Any other method needs DOR permission before the payroll period. [US-WIS5-010, A.1]
- **Withholding rates are unchanged for 2026.** DOR Withholding Tax Update 2026-1 (October 2026) says: "no plans to change the withholding tax rates". The current rates stay those of W-166, effective for periods on or after 2022-01-01. [US-WIS5-016, A.2]
  - The withholding schedule is 3.54% up to 12,760; 4.65% up to 25,520; 5.30% up to 280,950; 7.65% above.
  - Derived cumulative amounts: 451.70 / 1,045.04 / 14,582.83.
- **Withholding and assessment differ.** 71.06(1r) (2025 Wis. Act 15) set the **assessment** rates for tax years after 2024. [US-WIS5-010]
  - Single and head of household: 3.50% up to 14,680; 4.40% up to 50,480; 5.30% up to 323,290; 7.65% above.
  - Joint: 19,580 / 67,300 / 431,060. Married filing separately: 9,790 / 33,650.
  - From 2026 the bracket limits are indexed by CPI-U (August vs August 2024) and rounded to 10 (71.06(2e)(bm)).
  - **Builders must not move the assessment brackets into the WTC.** The withholding tables are deliberately not aligned with them.
- **Alternate method (formula)** [US-WI-P5-1-001]:
  - Standard deduction, single: 6,702 below 17,780; reduced by 12% of the excess; 0 at 73,630.
  - Standard deduction, married: 9,461 below 25,727; reduced by 20% of the excess; 0 at 73,032.
  - Exemption: 400 each.
  - Annualise, apply the schedule, then divide by the number of pay periods.
  - **Oracle**: the three W-166 worked examples, re-derived in Python [US-WIS5-011, derived arithmetically]:
    - weekly 350, single, 1 exemption: **7.59**;
    - weekly 500, single, 3 exemptions: **14.34**;
    - biweekly 1,000, married, 3 exemptions: **22.08**.
    - Annual tax 745.79 and 574.17 against the guide's 745.78 and 574.16. The guide rounds the bracket portion separately, so there is a 1-cent difference in the annual figure but none in the per-period result.
  - The DOR calculator is a second oracle [US-WI-PIT-002].
- **Supplemental wages**: aggregate with regular wages, or apply a flat percentage by estimated annual gross [US-WI-P5-1-001]:
  - 0-12,760: 3.54%;
  - 12,760-25,520: 4.65%;
  - 25,520-280,950: 5.30%;
  - 280,950 and over: 7.65%.
- **Rounding**: none in W-166 or the statute (repeats the US-MQ-68 finding).
- **Certificate**: Form WT-4 (with the WT-4A agreement). The federal W-4 cannot be used. [US-WIS5-011, US-WIS5-016]
  - No WT-4 means zero exemptions.
  - An exempt claim is renewed annually by April 30.
  - Copies go to DOR when more than 10 exemptions are claimed, or when exempt is claimed with wages over 200/week.
  - DOR lock-in letters bind the employer.
  - The WT-4 form edition was not retrieved (see Open questions).
- **Who is withheld on** (71.63(2); W-166 3F/3I) [US-WIS5-010, US-WIS5-011]:
  - Residents: on all wages, wherever earned.
  - Nonresidents: only on wages for WI work, split per payroll period.
  - Nonresident exceptions: interstate rail and motor carriers; reciprocity; air carriers (50% rule); expected WI earnings under 1,500 (catch-up once exceeded); military spouse (W-221).
- **Reciprocity**: IL, IN, KY, MI, using Form W-220 [US-MULTI-006, US-WI-P5-1-001].
  - Minnesota special arrangement: no WI withholding for a WI resident whose MN wages are subject to MN withholding.
- **Local income tax: none** [US-WIR3-001; US-MQ-68].
- **Conformity**: Wisconsin's IRC reference is as amended to 2022-12-31 for years after 2022. [US-WIS5-010]
  - This was read in the franchise and corporate definitions; the individual paragraph was not isolated.
  - DOR lists the 2026 box-16 differences in US-WIS5-016 (see section 8).
- Confidence: high.

## 3. social_security
- **UI wage base**: 14,000, fixed in statute for calendar years after 2012 (ch. 108 payroll definition, 10-1-26 text read). [US-WIS5-014, A.1; US-WIS5-019, A.2]
  - It is **not indexed**. It rises only if the FUTA base exceeds it.
- **Rate schedule**: Schedule D in 2026 and 2027 [US-WIS5-019, second independent authority with the 108.18(4) statute text; US-WIS5-020]. Total rate = basic + solvency:
  - payroll under 500,000: 0.00 to 12.00;
  - payroll 500,000 or more: 0.05 to 12.00.
- **New employer**: 3.05 (2.50+0.55) under 500,000 payroll, or 3.25 (2.50+0.75) at 500,000 or more. [US-WIS5-019; US-WIR3-002]
  - Construction: 2.50 / 2.70.
  - The rate holds for the first 3 years.
- **Rate increase cap**: +1 point a year (+2 points with a negative reserve) (108.18(5)). [US-WIS5-014]
- **Employee contribution: none.** UI is financed solely by employers [US-WIR3-003].
- **SDI/TDI/PFML: none** [US-WIR3-004, US-WIR3-005 (MANUAL)].
  - Wisconsin FMLA leave is unpaid (103.10(5)(a)). [US-WIS5-006, A.1]
  - This A.1 row replaces the MANUAL US-WIR3-005 for the unpaid-leave point.
- **Other employer levies**: only the solvency component (P7, US-WIP7-001). No transit or workforce levy [US-WIL-003].
- **Coverage thresholds** [US-WIS5-013]:
  - commercial: 1,500 in a quarter, or 1+ employee in 20 weeks;
  - agricultural: 20,000 in a quarter, or 10+ workers in 20 weeks;
  - domestic: 1,000 in a quarter;
  - 501(c)(3): 4+ employees in 20 weeks.
- Confidence: high.

## 4. payslip_statute
- **Content**: on the paycheck, pay envelope or an accompanying paper. [US-WI-P5-2-001; US-WIS5-002]
  - Required: hours worked, rate of pay, and the amount and reason for each deduction. A coding system is allowed, and personal miscellaneous deductions are excepted (103.457; DWD 272.10).
- **Electronic stub**: allowed if the employee can print it free (DWD wages page, per US-WI-P5-2-001). With direct deposit the stub is still required [US-WIS5-005].
- **Retention**: payroll records for at least 3 years (DWD 272.11; DWD 274.06). [US-WIS5-002, US-WIS5-003]
  - Fields: name, address, date of birth, hire and leave dates, daily start/stop times, meal periods, daily and weekly hours, rate and wages per period, deductions, and output if not paid on time.
- **Language**: none prescribed for the payslip [US-WIL-002].
- Confidence: high.

## 5. reporting_instruments
- **WT-6 withholding deposit report** [US-WIS5-011, US-WIS5-016]:
  - DOR assigns the frequency (annual, quarterly, monthly or semi-monthly). It is re-evaluated every November and notified in writing. **No dollar thresholds are published.**
  - Monthly and quarterly filers: due the last day of the following month.
  - Semi-monthly filers: pay dates 1-15 are due the last day of the month; pay dates 16-end are due the 15th of the next month.
  - A zero report is still filed.
  - Filing is electronic only unless a waiver is granted: My Tax Account, third-party software, TeleFile, e-file, ACH credit. An ACH debit must be in by 4 p.m. CST.
- **WT-7 annual reconciliation**: due January 31 (TY2026: **February 1, 2027**), or 30 days after the account closes. It is rejected until all WT-6s are filed. [US-WIS5-011, US-WIS5-016]
- **State W-2** [US-WIS5-012, US-WIS5-015]:
  - Due January 31 (TY2025 was February 2, 2026; TY2026 is February 1, 2027).
  - 10 or more W-2s must be filed electronically.
  - Format: **SSA EFW2 with RS record** (state code 55 in positions 3-4 and 274-275). 1099s use IRS Pub 1220.
  - Channels: MTA keying or file upload; sFTP; test file optional. No transmittal.
- **Quarterly UI contribution and wage report**: due by the end of the month after the quarter, and filed even when the rate is zero. [US-WIS5-013, US-WIS5-014, US-WIS5-020]
  - Electronic filing is mandatory at 25+ employees (108.205(2)), with a 20 per employee penalty for paper.
  - Late penalty: 50, or the greater of 100 or 20 per employee.
  - File layouts include a modified IRS/SSA E/S record.
  - **DWD stops mailing quarterly reports in 2027**, and a new UI Employer Portal (MyWisconsin ID) arrives in fall 2026.
- **New hire report**: within 20 days of the start date. [US-WIS5-013, US-WIS5-011]
  - Channels: wi-newhire.com (key or file), SFTP, or paper (WT-4, W-4 or a list).
  - Fields: employee name, address, SSN, date of birth; employer name, payroll address, FEIN; date of hire.
  - Multistate employers may elect one state.
- **Registration**: one withholding account per legal entity (W-166 2) [US-WIS5-011]. UI account with DWD.
  - Payroll service providers must register and test their software with DOR [US-WIS5-016].
  - POA: A-222 (DOR) and UCT-8291-E (UI) [US-WI-P5-2-003, US-WI-P5-1-002].
- Confidence: high.

## 6. leave
- **Paid sick leave: no state statute, and locals are preempted** (103.10(1m); 103.12, with ordinances in effect on 2018-04-18 void). [US-WIS5-006, A.1]
- **WFMLA** (103.10) [US-WIS5-006]:
  - Applies to employers with 50+ permanent employees, for employees with 52 weeks of service and 1,000 hours.
  - Family leave up to 6 / 2 / 8 weeks; medical leave 2 weeks per 12 months.
  - Leave is unpaid; employer paid leave may be substituted.
- **Other**: bone marrow and organ donation leave (103.11), unpaid, with substitution allowed. [US-WIS5-006]
- **Vacation and holiday pay**: not mandated. [US-WIS5-005]
- No PFML benefit interaction (none exists).
- Confidence: high.

## 7. termination
- **Final pay**: by the next regular payday or the 31-day limit, whichever is earlier. The same rule applies to quits and discharges (109.03(2)). [US-WIS5-004]
  - Excepted: commission sales agents and written fixed-term contracts.
- **Accrued vacation**: payable if a written policy exists and has no written forfeiture clause. [US-WIS5-005]
- **UI separation**: no notice to the employee is required by the handbook. [US-WIS5-013]
  - The employer answers UCB-16 (Separation Notice), UCB-23 and UCB-719 when DWD requests them.
  - Poster UCB-7-P must be displayed.
- **Plant closing**: 60 days' notice (109.07, employers with 50+ in WI). [US-WIS5-004]
- **Death of employee**: wages are payable on demand to the spouse, children or dependants (109.03(3)). [US-WIS5-004]
  - Accrued wages and vacation paid after death are not subject to WI withholding (W-166 3R).
- Confidence: high.

## 8. benefits_in_kind
- **General rule**: Wisconsin "generally conforms" to the IRC. W-166 section 1 defers to Pub 15 and 15-A. [US-WIS5-011]
  - HSAs follow federal rules from 2011 (only the penalties differ).
  - Third-party sick pay: the third party reports and remits, and issues the W-2.
- **2026 box-16 differences** (WI wages higher than federal) [US-WIS5-016]:
  - IRC 112 (hazardous duty);
  - IRC 127 (student-loan payments);
  - IRC 128 (employer contributions to Trump accounts);
  - IRC 129 (dependent care above the WI exemption);
  - IRC 132 (moving expenses and bicycle commuting).
- **Transit and parking**: 340/month each for 2026, both federal and WI. 2027 is not published.
- **401(k), section 125 and group-term life**: no WI departure stated in W-166 or Update 2026-1 (no text read that names them).
- Confidence: medium-high.

## 9. deductions_garnishments
- **Deductions for damage, loss or faulty work**: need written authorisation, a joint determination or a court finding. A violation costs 2x the amount (103.455). [US-WIS5-007]
- **Creditor garnishment** (812.34) [US-WIS5-008]:
  - Maximum **20%** of disposable earnings (80% exempt), which is stricter than the CCPA's 25%.
  - Earnings are totally exempt below the poverty line or with need-based aid, and garnishment may not push household income below the poverty line.
  - These limits do not apply to support, tax or bankruptcy orders.
  - Garnishee fee: 15, plus 3 per payment after the first, deducted from the creditor's share.
  - No retaliation (812.43).
- **Child support IWO** (767.75) [US-WIS5-009]:
  - Withhold from pay issued more than one week after the notice arrives.
  - Remit within 5 days of payday.
  - Cap: 15 USC 1673(b)(2).
  - The employer may keep up to 3 per payment, from the payer's money.
  - The IWO has priority over every other state-law process.
  - Annual 65 receiving and disbursing fee (767.57(1e)).
- **State tax levies**: DOR wage attachment exists (W-166 4B mentions "Wage Attachment Payments"). Its percentage was not read (see Open questions).
- Confidence: high, except the DOR levy.

## 10. collective_agreements
- **Prevailing wage**: no current state or local regime. Ch. 103 as published 10-1-26 has no 103.49 and no "prevailing wage" text [US-WI-P5-2-002; P5/P6 rows reused].
  - The repealing act itself was not read; confidence is medium.
- **CBAs** may set a different pay frequency (109.03(1)(a)). [US-WIS5-004]

## 11. indexation
- **Indexed**:
  - The PIT assessment brackets (CPI-U) from 2026 (71.06(2e)(bm)). [US-WIS5-010]
  - Several subtractions and credits (CPI).
- **Not indexed**:
  - Minimum wage (fixed in statute).
  - UI wage base (fixed at 14,000) [US-WIS5-014].
  - **The withholding tables**: DOR revises them by publication only and has no plans for 2026 [US-WIS5-016].
- **Derivation**: the withholding schedule's cumulative amounts (451.70 / 1,045.04 / 14,582.83) and the W-166 examples were reproduced in Python [US-WIS5-011].
  - The 2026 indexed assessment bracket values were not fetched. They are not needed for withholding.

## 12. data_protection
- **Breach notification**: 134.98 requires notice within a reasonable time, at most 45 days. Personal information includes SSN, driver's licence, financial account, DNA and biometric data. [US-WIS5-018, A.1]
- **SSN on pay statements**: no Wisconsin statute restricting it was found (keyword scan of ch. 134, plus a search).
  - SSN truncation is allowed on W-2 and 1099 copies given to the employee, but not on copies filed with DOR [US-WIS5-012, US-WIS5-011].
- **Personnel file inspection**: at least twice a year (103.13). [US-WIS5-007]
- Confidence: medium-high. The absence is supported by a scan, not by an index.

## 13. live_legal_change (2026-01-01 to 2026-11-02)
- **DOR Withholding Tax Update 2026-1 (2026-10-30)** [US-WIS5-016]:
  - No change to withholding rates.
  - TY2026 due dates: February 1, 2027.
  - New 2026 box-16 differences under P.L. 119-21 (IRC 128 Trump accounts, among others).
- **4.40% bracket expansion** for tax years after 2024 (71.06(1r), (2)(k), (L) in the 10-1-26 text) and the retirement-plan subtraction for tax years after 2024 (71.05(6)(b)54m.) [US-WIS5-010]. The search lead attributes the bracket change to 2025 Wis. Act 15 (signed 2025-07-03); the act was not read. Both operate at **assessment** level, not withholding.
- **DWD**: Schedule D continues in 2027; quarterly-report mailing ends in 2027; new employer portal in fall 2026; handbook update announced [US-WIS5-020].
- **2025 Wis. Act 145** (workers' compensation, effective 2026-04-01) and **Act 144** (UI administration appropriation, partial veto): no withholding or contribution effect [US-WIS5-021, A.3]. Act texts not read.
- **2025 Wis. Act 118**: repeals obsolete parts of 71.01/71.06 on future dates, per statute NOTEs. A corrective bill is "pending" per the NOTE in 71.06(2e). No payroll effect identified.
- **Minimum wage**: no bill enacted (104.035 unchanged in the 10-1-26 edition).

## Special populations

| Population | WI rule | register_id |
|---|---|---|
| Domestic/household workers | Not "wages" for WI withholding (71.63(6)(c)); W-2 still reported (state ID 036888888888801 if no account). UI coverage only at 1,000 cash wages in a quarter. Outside overtime ch. DWD 274 (274.015). | US-WIS5-010, US-WIS5-011, US-WIS5-013, US-WIS5-003 |
| Agricultural (incl. H-2A) | Not "wages" (71.63(6)(b)): no withholding required, voluntary by agreement; W-2 if 600+ or any withholding. UI only at 20,000 in a quarter or 10 workers in 20 weeks. Farm labour may be paid quarterly (109.03(1)). | US-WIS5-016, US-WIS5-013, US-WIS5-004 |
| Minors | Under 16: work permit (103.70). Minimum wage 7.25; opportunity wage 5.90 for under-20s in the first 90 days. | US-WIS5-022, US-WIS5-001 |
| Tipped | Cash wage 2.33 (2.13 opportunity); signed tip declaration every pay period. | US-WIS5-002 |
| Clergy/religious | Ministers and members of religious orders excluded from "wages" for withholding (71.63(6)(f)). | US-WIS5-010 |
| Students | UI exclusion for credit work-study, student nurses/interns, camp students under 13 weeks; no WI withholding rule beyond federal. | US-WIS5-023 |
| Nonresident aliens | UI exclusion for F, J, M, Q visas; WI withholding follows the general nonresident rule (WI-source wages). No WI-specific NRA withholding add-on found in W-166. | US-WIS5-023, US-WIS5-011 |
| Statutory employees | Direct sellers under IRC 3508 and real-estate agents (452.38) are not employees for withholding (71.63(2)); corporate officers are employees. UI: commission-only insurance/real-estate agents and direct sellers excluded. | US-WIS5-010, US-WIS5-023 |
| Government employees | Included as employees for withholding (71.63(2)); DWD 274.08 has separate public-employee coverage rules; WRS pension not in scope. | US-WIS5-010, US-WIS5-003 |
| Nonresidents / multistate | Reciprocity IL, IN, KY, MI (W-220); MN arrangement; 1,500 de-minimis; military spouse W-221. | US-MULTI-006, US-WIS5-011 |
| Pensioners | Pensions are not wages: withhold only on written request, minimum 5. | US-WIS5-016 |
| Nonresident entertainers | 6% of the contract price unless bonded (WT-11/WT-12). | US-WIS5-016, US-WIS5-011 |

## ACCESS gaps
- `https://docs.legis.wisconsin.gov/statutes/statutes/134/98` and `https://docs.legis.wisconsin.gov/statutes/statutes/134.pdf`: timed out (curl exit 28). The host stopped answering after about 8 requests. Ch. 134 was taken from `https://web.archive.org/web/2026id_/...134.pdf` (edition 10-15-25).
- `https://docs.legis.wisconsin.gov/statutes/statutes/109.pdf`: the 10-1-26 edition was not fetched; the 6-25-25 edition is on disk.
- `https://www.revenue.wi.gov/DORForms/wt-4.pdf` and `https://www.revenue.wi.gov/TaxForms2026/wt-4.pdf`: 404 (guessed paths). The WT-4 URL is not linked from W-166 or Update 2026-1.
- `https://www.revenue.wi.gov/Pages/Businesses/New-Development/home.aspx`: 404 (guessed DOR news path).
- `https://dwd.wisconsin.gov/uitax/rates.htm`: 404 (the right pages are under `/ui/employers/taxrates/`).

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **wi.meta.register_id_pattern** (blocking): 13 facts rest on active register rows whose ids (US-WI-P5-1-001, US-WI-P5-2-001, US-WI-P5-2-002) do not match the facts-schema register_id pattern ^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$ (multi-hyphen legacy ids). They are carried in full in _facts_pending_register_id_pattern and are NOT yet consumable facts. What would close it: Orchestrator decision: a PATCH of facts.schema.json loosening the register_id pattern (e.g. ^[A-Z]{2}-[A-Z0-9-]{2,16}-[0-9]{3,4}$), or register alias ids; then run _research/synthesis-B/_work-MN-WY/promote.py to move the pending facts into facts[].
- **wi.pit.wt4.form_edition** (non-blocking): WT-4 edition and line layout unconfirmed (DOR URLs 404). What would close it: DOR Forms page WT-4 (browser pass).
- **wi.garn.dor_wage_attachment** (non-blocking): DOR wage attachment percentage and priority not read. What would close it: DOR Wage Attachment page and the levy provision it cites.
- **wi.bik.irc_conformity.individual** (non-blocking): Individual IRC conformity paragraph 71.01(6) not isolated. What would close it: 71.01(6) in the on-disk ch. 71 text.
- **wi.prevailing_wage.repeal_act** (non-blocking): Repealing acts (2017 Act 59; 2015 Act 55) not read. What would close it: Act texts on docs.legis.wisconsin.gov.
- **wi.labour.paycard** (non-blocking): No WI paycard rule located. What would close it: DWD Labor Standards FAQ on pay cards.
- **wi.pit.statutory.brackets_2026_indexed** (non-blocking): 2026 CPI-indexed assessment brackets not fetched (assessment only). What would close it: DOR 2026 Form 1 instructions (early 2027).

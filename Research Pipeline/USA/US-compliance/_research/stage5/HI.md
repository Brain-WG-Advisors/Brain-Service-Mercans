# Stage 5 — Hawaii (HI): 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Mandate block: US-MQ-31 (answered at seal attempt 3).
- **Budget:** 60 fetches / 2 h declared. Used about 45 fetch attempts (curl, including failed and Wayback attempts) and about 15 minutes. I stopped acquiring at the 75% fetch mark.
- **Access:** the VPN was OFF (IP in Brazil). The labor.hawaii.gov, tax.hawaii.gov, files.hawaii.gov and ag.hawaii.gov hosts answered directly. capitol.hawaii.gov returns 403, so every HRS section was read from a Wayback `id_` copy; the snapshot date of each is given in the register row.
- **Register shard:** `00-official-sources/_register-shards/S5-HI.csv` holds 31 rows, US-HIS5-001..031: 27 active, 3 partial, 1 gated.
- **New sources:** `00-official-sources/ccg-sources/HI/`, 36 files, 3.7 MB. No file is over 5 MB.

**Active rows reused without a re-fetch.** Their local files were re-read this pass.
- US-HIP51-001 / -002: Booklet A (Rev. 2025), `pdfs/HI/HI-booklet-A-2025_wayback-20260416120033.pdf`, 112 pp. The DOTAX page confirms it is still the current edition on 2026-11-02 [US-HIS5-005].
- US-HI-003 / US-HIP7-002 / -003: DCD 2026 wage-base notice. It was re-read and its numbers were re-derived in US-HIS5-015.
- US-HIP52-001 (HRS 387-6), US-HIP51-003 / US-HIL-001 (HRS 388-7), US-HIP52-002 (HRS 104-2), US-HIP51-004 / US-HIP52-003 (POA), US-HIP9V-001 / -002, US-HIP9L-001 / -002.
- US-HI-001 / US-HI-002 have no local file. Their content is now carried by US-HIS5-004/-005 and by US-HIS5-011 / US-HIP9V-001, which do have local files.

---

## 1. labour_code
- **Minimum wage** [US-HIS5-001 statute, US-HIS5-002 DLIR; the two agree]:
  - **16.00 USD/h** from 2026-01-01.
  - **18.00 USD/h** from 2028-01-01, already enacted (L 2022 c 114).
  - Nothing is scheduled for 2027 (the rate stays 16.00) and there is no indexation.
  - Counties have no local minimum wage. The rate is set only in HRS 387-2, and DLIR lists no county rate.
- **Tip credit** [US-HIS5-001]:
  - 1.25 USD/h below the minimum (cash wage 14.75) from 2024-01-01.
  - 1.50 USD/h below from 2028-01-01.
  - Allowed only if employer wage plus tips is at least the minimum wage + 7.00 USD.
  - A tipped employee is one who customarily receives more than 20 USD/month in tips [US-HIS5-003].
- **Coverage carve-outs in HRS 387-1** [US-HIS5-003]:
  - Guaranteed compensation of **4,000 USD or more a month** (L 2024 c 73).
  - Agriculture with fewer than 20 employees, and coffee harvesting.
  - Casual domestic service and companionship.
- **Overtime** [US-HIS5-003, US-HIS5-002]:
  - 1.5× after 40 h in a workweek. There is no daily overtime, except on public works.
  - Statutory regular-rate divisors for salaried staff:
    - weekly ÷ 40;
    - biweekly ÷ 2 ÷ 40;
    - semimonthly × 24 ÷ 52 ÷ 40;
    - monthly × 12 ÷ 52 ÷ 40.
  - Seasonal agricultural processing: 20 exempt weeks, with overtime after 48 h.
  - Split shifts must fall within 14 consecutive hours.
  - Public works (HRS ch. 104): overtime after 8 h a day and on all Saturday, Sunday and state-holiday hours.
- **Pay frequency and timing** (HRS 388-2) [US-HIS5-007]:
  - At least twice each calendar month, on paydays designated in advance.
  - Monthly pay only by secret-ballot majority election (valid 2 years) or with director permission.
  - Wages are due **within 7 days after the end of the pay period** (15 days with director permission).
- **Method of payment** [US-HIS5-007, US-HIS5-017]:
  - Cash or check.
  - Direct deposit: voluntary written or e-signature consent, free of charge, cancellable, and no discipline for refusing.
  - Pay card (HRS 388-5.7):
    - The employee chooses between direct deposit, check and card; the card can never be a condition of hire.
    - Plain-language disclosure in 10-point font comes before consent.
    - Free: 3 withdrawals per pay period (one for the full net amount), 24/7 balance access, a 60-day transaction history, and one replacement card a year.
    - No overdraft fees and no balance-based fees.
    - The employer must switch the employee to another method within two pay periods of a request.
- Confidence: 95%. The HRS reads are Wayback snapshots from 2025-04 to 2026-09; the DLIR page confirms the wage figures.

## 2. income_tax
- **Instrument:** HRS 235-61 to -69. Booklet A (Rev. 2025), effective for withholding on and after 2026-01-01, was posted on 2025-12-01 and is still current on 2026-11-02 [US-HIP51-001, US-HIS5-004, US-HIS5-005].
- **Method:** wage-bracket tables (Part 3), the annualized formula (Part 1) or the per-period formula (Part 2) [US-HIS5-004].
  - Annual values: allowance **1,144** each, plus an **extra lump-sum allowance of 4,350** for every employee.
  - Weekly values: allowance 22.00 and lump sum 83.65. 1,144/52 = 22.00 and 4,350/52 = 83.65, re-derived.
  - **Single / HoH brackets (annual):**

    | Over | Not over | Tax |
    |---|---|---|
    | 0 | 9,600 | 1.40% |
    | 9,600 | 14,400 | 134 + 3.20% |
    | 14,400 | 19,200 | 288 + 5.50% |
    | 19,200 | 24,000 | 552 + 6.40% |
    | 24,000 | 36,000 | 859 + 6.80% |
    | 36,000 | 48,000 | 1,675 + 7.20% |
    | 48,000 | 125,000 | 2,539 + 7.60% |
    | 125,000 | — | 8,391 + 7.90% |

  - **Married brackets (annual):**

    | Over | Not over | Tax |
    |---|---|---|
    | 0 | 19,200 | 1.40% |
    | 19,200 | 28,800 | 269 + 3.20% |
    | 28,800 | 38,400 | 576 + 5.50% |
    | 38,400 | 48,000 | 1,104 + 6.40% |
    | 48,000 | 72,000 | 1,718 + 6.80% |
    | 72,000 | 96,000 | 3,350 + 7.20% |
    | 96,000 | 250,000 | 5,078 + 7.60% |
    | 250,000 | — | 16,782 + 7.90% |

  - **G-DERIVE (Python):** the cumulative amounts are the exact bracket sums rounded to whole dollars. Examples: 134.40 → 134; 859.20 → 859; 16,782.40 → 16,782.
  - **Oracle seed (C37), Booklet A Part 1 example:** single, 3 allowances, 500/week.
    - Annual base: 26,000 − 3,432 − 4,350 = 18,218.
    - Tax: 288 + 3,818 × 5.5% = 497.99.
    - Weekly: 497.99 / 52 = **9.58**. Re-derived exactly.
- **Brackets versus statute:** withholding stops at 7.90%. The assessment schedule (HRS 235-51, TY2025-2026) continues to 8.25 / 9 / 10 / 11% above 175,000 for a single filer [US-HIS5-027].
- **Certificate: Form HW-4 (Rev. 2022)**, the current edition [US-HIS5-026, US-HIP51-001].
  - The federal W-4 is not accepted.
  - Marital status: Single, Married, Married-but-withhold-at-Single-rate, Certified Disabled, Nonresident Military Spouse. The last two are not subject to withholding.
  - Line 4: allowances. Line 5: additional amount per pay period.
  - **There is no "exempt" status under Hawaii law.**
  - HoH is withheld as Single, with an extra allowance.
  - No HW-4 on file: withhold as Single with 0 allowances.
  - Employer duty: send a copy of the HW-4 to the district Tax Assessor when the employee claims excessive allowances (generally more than 10).
  - A replacement HW-4 takes effect from the first payment on or after the 30th day after it is furnished; the employer may apply it earlier.
- **Supplemental:** there is no flat rate. Supplemental pay is aggregated with regular wages of the current or preceding period, or averaged over the periods it covers (Booklet A s. 14(e)).
- **Rounding and minimums:**
  - No withholding below 0.10 per payment.
  - Pay periods that are multiples of a week: compute on the weekly average × number of weeks.
  - Quarterly, semiannual and annual periods: compute on the monthly average × number of months.
  - There is no cent-rounding rule beyond this.
- **Resident and nonresident** [US-HIP51-002, Booklet A ss. 10, 11, 13]:
  - Resident = domiciled, or present more than 200 days (a rebuttable presumption).
  - Withholding applies to wages for services in Hawaii, and to services outside Hawaii when the regular place of employment is in Hawaii or the wages are paid from a Hawaii office.
  - A nonresident working **60 days or fewer** in Hawaii is exempt if all of these hold: an HW-6 is on file, the employee is paid from outside Hawaii, the regular workplace is outside Hawaii, and the employer does not expect more than 60 days. The employer files HW-7 with the original HW-6.
  - The exemption never applies to construction contractors' employees.
- **Other exclusions:** MSRRA spouses; ministers and members of religious orders; tips under 20 USD a month; casual or domestic service (unless 50 USD or more a quarter and regularly employed); newspaper carriers under 18; interstate crew members; meals and lodging furnished for the employer's convenience.
- **Withholding is required on agricultural and domestic wages** even where federal withholding is not (Booklet A s. 10).
- **Reciprocity:** none. **Local income taxes:** none. Both are mandate answers, re-confirmed in Booklet A. The DOTAX business-tax list shows no wage-based tax other than withholding [US-HIP9V-002].
- **Conformity changes in 2026 (Act 35 SLH 2026)** [US-HIS5-029]. Operating level: assessment.
  - Hawaii conforms to the IRC 224 tips deduction (up to 25,000).
  - Hawaii does **not** conform to the IRC 225 overtime deduction.
- Confidence: 95% for 2026. 2027 is open: see §13 and Q1.

## 3. social_security
- **UI (DLIR UI Division, HRS ch. 383)** [US-HIS5-010, US-HIS5-011, US-HI-002 / US-HIP9V-001]:
  - 2026 values: Schedule C, **taxable wage base 64,500**, **new-employer rate 2.40%**, **maximum 5.60%**, **E&T assessment 0.01%**.
  - 2025 values: 62,000, 2.4%, 0.01%.
  - **Contributions are employer-only.** HRS 383-61(a) forbids deducting them from wages; there is no employee UI.
  - **Wage-base rule (indexation):** the wage base is the average annual wage for the four quarters ending 30 June of the prior year, computed by 30 November and rounded to the nearest 100.
    - **G-DERIVE:** the DCD state average annual wage of 64,471.82 rounds to **64,500** = the DLIR 2026 base (Python).
    - Caliber: both figures are DLIR state averages. They are assumed to be the same caliber.
  - **Experience rating:**
    - Reserve ratio = reserve balance at 31 December ÷ average annual taxable payroll of the last 3 years.
    - Rate notice in March.
    - The DLIR 2026 example gives a ratio of 0.1250 → 0.4% (Schedule C).
    - The new-employer rate is the rate at ratio .0000.
  - **E&T assessment:** paid by employers whose rate is above 0% and below the schedule maximum, on taxable wages. It is not creditable against FUTA.
  - **Minimum rate of Schedule C: not transcribed.** Table 2 is not in the page text (Q2).
- **TDI (DCD, HRS ch. 392)** [US-HIS5-014, US-HIS5-015, US-HI-003]:
  - The employer may withhold half the cost, at most **0.5% of weekly wages**, capped at **7.50 USD a week**. The employer pays the rest.
  - **Max weekly wage base 1,500.21** = 64,471.82 / 52 × 1.21 (re-derived). Maximum weekly benefit: 871.00.
  - No employee deduction unless, in the prior 52 weeks, the employee earned at least 400 and had 14 weeks of 20+ hours.
  - The program is insurer- or self-insurer-funded. There is no state TDI rate and no state TDI return.
- **Prepaid Health Care (HRS ch. 393)** [US-HIS5-015, US-HIS5-016, US-HIP7-003]:
  - Mandatory for regular employees working 20+ h/week and earning at least 86.67 × the minimum wage = **1,387.00/month** in 2026. DCD rounds 86.67 × 16.00 = 1,386.72 up.
  - The employee share is at most half the premium and at most 1.5% of wages.
  - This closes the "86.67× not rechecked" gap on US-HIP7-003.
  - It changes on 2028-01-01, when the minimum wage reaches 18.00: 86.67 × 18 = 1,560.06, a derived value not yet published.
- **PFML:** none. Hawaii has TDI only [US-FEDP51-011].
- **Other employer levies:** only the E&T assessment [US-HIL-003, US-HIP9V-001, US-HIS5-011]. P7 and P9 were not redone.
- Confidence: 92%.

## 4. payslip_statute
- **Contents:** HRS 387-6(c), 14 items [US-HIP52-001]:
  1. employee name;
  2. employer name;
  3. employer address and phone;
  4. total hours;
  5. regular and overtime hours;
  6. straight-time pay;
  7. overtime pay;
  8. other compensation, including allowances counted toward the minimum wage;
  9. gross pay;
  10. amount and purpose of each deduction;
  11. net pay;
  12. pay date;
  13. pay period;
  14. rates and basis, including overtime rates and piece rates with piece counts.
- HRS 388-7(4) has a shorter list [US-HIP51-003].
- **Electronic delivery:** allowed with the employee's written authorization (387-6(c), 388-7(4)). Direct deposit still requires a pay statement [US-HIS5-007].
- **Retention:** the 388-7 record copy is kept at least 6 years [US-HIP51-003]. Withholding records follow the statute of limitations, usually 3 years [Booklet A s. 19].
- **Hire notice:** written notice at hire of the rate and of the day, hour and place of pay [US-HIL-001].
- **Language:** no rule requires a language other than English [US-HIL-001/-002, US-HIP9L-001/-002].
- Confidence: 95%.

## 5. reporting_instruments
- **Withholding (DOTAX)** [US-HIS5-005, US-HIP51-001]:
  - Registration on Form BB-1 or Hawaii Tax Online (HTO), no fee.
  - **HW-14** quarterly, due 15 April / 15 July / 15 October / 15 January. It is filed even when no wages were paid.
  - **Deposits with VP-1:**
    - quarterly if liability is 5,000 or less (by the 15th of the month after the quarter);
    - monthly if 5,000–40,000 (by the 15th of the next month);
    - **semi-weekly** if over 40,000, or if federal deposits are semi-weekly, on the Wednesday/Friday rule with the 3-banking-day rule. Hawaii does not use the federal 4-quarter lookback.
  - EFT is mandatory above 40,000 when the employer is on EFTPS, and above 100,000 once notified. The penalty is 2%.
  - **E-file of HW-14 and W-2** is mandatory above 40,000 liability (TA 2019-11).
  - **W-2 / HW-2:**
    - Copies go to the employee **and** to DOTAX by **31 January** (TA 2021-08).
    - From **2026-01-01**, e-filing is mandatory at **10 or more** forms (TA 2025-05) [US-HIS5-006].
    - Penalty: 25 per form, up to 50 per employee.
    - Channels:
      - HTO Simple File Import, at most 1,000 records per submission (Pub EF-12);
      - manual entry;
      - **SSA EFW2 file upload** on HTO, validated there (Pub EF-10);
      - Hawaii Bulk Filing System, an SFTP ZIP (Pub EF-9).
    - **Format = federal EFW2**, with the Hawaii Tax ID shown. The Pub EF-10 layout notes were not read (Q4).
  - **HW-30** is only the transmittal for paper W-2s. The HW-3 reconciliation was dropped from TY2020; one DOTAX FAQ still mentions it, and that FAQ is stale.
  - **Exempt nonresidents:** HW-7 with HW-6.
- **UI (DLIR)** [US-HIS5-012]:
  - Online registration at uiclaims.hawaii.gov, within **20 days** after the first hire.
  - **UC-B6** quarterly wage, contribution and E&T report, due the **last day of the month after the quarter** (30 April / 31 July / 31 October / 31 January).
    - Filed even with no wages, including by self-financed and 0% employers.
    - Content: name, SSN and total wages per worker; wages are reported when paid.
    - Late report: 30. Late contributions: 10% (minimum 100) + 2/3% a month.
  - Separation information is requested by DLIR (UC-BP-35, within 5 days, penalty 10) or answered through SIDES. **There is no employer-initiated separation notice at termination.**
  - BLS 3020 Multiple Worksite Report applies to employers with 10+ employees at secondary sites.
  - The machine format of UC-B6 (any bulk file spec) was not located (Q5).
- **New hire (CSEA)** [US-HIS5-021]:
  - Every employer reports within **20 days** of the first day of work. Rehires count after a separation of 60 days or more.
  - Data: name, address, SSN, first-day date, employer name, address and FEIN.
  - Channels: a copy of the federal W-4 by fax or mail, or SFTP in the FLO101 fixed-width layout (H4 / W4 / total records). There is no web upload.
  - Penalties: 25, or 500 for conspiracy.
- **TDI and PHC:** coverage is arranged through insurers. There is no wage return to the state [US-HI-003].
- Confidence: 90%.

## 6. leave
- **Paid sick leave:** **no general Hawaii mandate.**
  - The WSD list of laws administered has none, and the HFLL FAQ Q4 says employers need not create a sick-leave plan [US-HIS5-024, US-HIS5-023].
  - This is a negative finding from authority pages; no search of 2026 session law was made on this point.
- **Hawaii Family Leave Law (HRS ch. 398)** [US-HIS5-018, US-HIS5-023]:
  - Covers employers with **100+ employees** in Hawaii, for employees with 6 months of service.
  - **4 weeks** of leave per calendar year, **unpaid**, which may be intermittent.
  - Where the employer provides sick leave, the employee may use up to **10 days** of accrued sick leave (PTO counts) for family leave.
- **Paid leave insurance:** none; TDI pays benefits for the employee's own disability (§3).
- **Payroll interaction:**
  - TDI benefits paid by an insurer are third-party sick pay. They go into HW-2 "Total Wages", or on a separate HW-2 marked as third-party sick pay [Booklet A s. 18].
- **Vacation:** no statutory accrual (see §7).
- Confidence: 85%.

## 7. termination
- **Final pay** (HRS 388-3) [US-HIS5-008]:
  - **Discharge:** pay in full at the time of discharge, or **by the next working day** if immediate payment is impossible.
  - **Resignation:** the next regular payday. If the employee gave at least one pay period's notice, pay at the time of quitting.
  - **Layoff or labor-dispute suspension:** the next regular payday.
- **Accrued vacation:** the Hawaii Supreme Court held that it is **not "wages"** under HRS 388-1 (108 H. 411, 2005), so there is no statutory payout. Payout follows the employer's policy [US-HIS5-008].
- **HW-2 at termination:** furnished within 30 days of a written request, if that falls before 31 January [Booklet A s. 2].
- **UI separation notice:** none at termination. DLIR requests the information after a claim [US-HIS5-012].
- **State WARN (HRS 394B, dislocated workers):** a lead only. The labor-law poster lists the "Dislocated Workers" section [US-HIP9L-001]. It was not read and is not a payroll calculation.
- Confidence: 85%.

## 8. benefits_in_kind
- **Conformity:** HRS 235-2.3 conforms to the IRC as of **2025-12-31** (Act 35 SLH 2026, effective for TY2026) [US-HIS5-029].
  - Exclusions follow federal law; 401(k), 125, HSA and group-term life were not individually confirmed.
  - **IRC 132(f) bicycle-commuting exclusion:** Hawaii now follows the federal suspension; it previously decoupled.
  - **New IRC 128:** employer Trump Account contributions up to 2,500 are excluded for Hawaii purposes too.
  - **HSA:** Hawaii is not named among the decoupled items in TA 2026-06. The full 235-2.3(b) list was not read (Q3).
- **Booklet A withholding specifics** [US-HIP51-001]:
  - Meals and lodging furnished for the employer's convenience are not subject to withholding.
  - Non-cash pay outside the trade or business, and retail-commission non-cash pay, are shown separately on the HW-2.
  - Expense reimbursements are excluded only if they are identified separately or accounted for.
  - The Cost of Living Allowance (COLA) is included in HW-2 wages.
- Confidence: 70%. The full 235-2.3(b) list was not read.

## 9. deductions_garnishments
- **Wage deductions (HRS 388-6)** [US-HIS5-009]:
  - Allowed only when required by statute or court process, or when the employee authorizes them in writing.
  - Never allowed, even with authorization: fines; shared-till shortages; breakage; dishonored checks; losses not caused wilfully; employer-required medical exams (paragraph (6) is ERISA-preempted in part).
- **Creditor garnishment (HRS 652-1)** [US-HIS5-019]:
  - **5% of the first 100 USD a month, 10% of the next 100, 20% above 200** (or the weekly equivalent), on wages after legally required deductions.
  - This is stricter than the CCPA 25% for almost every earner. Apply the lower amount.
- **Child support IWO** [US-HIS5-022]. Source: FEN125, a 2003 guide, tier A.3.
  - The support order has priority over other garnishments.
  - Start by the first pay period within 7 business days after the order is mailed.
  - Remit **within 5 working days** after payday.
  - Employer fee: **2 USD per payment**, taken from income, not from the support amount.
  - CCPA limits: 50/60%, plus 5% when arrears are 12 weeks or more.
  - At termination, report the last known address and the new employer.
  - Retaliation is a misdemeanor.
- **State tax levy on wages (DOTAX):** not researched (Q6).
- Confidence: 80%.

## 10. collective_agreements (prevailing wage)
- **HRS ch. 104** applies to public-works construction contracts over 2,000 [US-HIP52-002].
  - Wages: the prevailing basic rate plus fringe benefits, from the DLIR Wage Rate Schedule.
  - Overtime: after 8 h a day and on weekends and holidays [US-HIS5-002].
- **Certified payroll:** a certified copy of all payrolls plus the fringe-benefit reporting form, **weekly**, to the contracting agency. The general contractor submits for its subcontractors [US-HIS5-020].
  - Records kept 3 years and produced within 10 days of a request.
  - WSD 2017-01 covers certified-payroll requirements. WSD 2026-01 (2026-05-21) covers truck drivers on asphalt paving [US-HIS5-024].
- Confidence: 90%.

## 11. indexation
| Item | Mechanism | Publication carrying the value | 2026 | Next |
|---|---|---|---|---|
| UI taxable wage base | Average annual wage, 4 quarters to 30 June, rounded to the nearest 100 (383-61(b)) | DLIR UI "Tax Rate Schedule" / "Contribution Rates Explained" | 64,500 (derived from 64,471.82) | 2027 not published at 2026-11-02 (expected December) |
| UI rate schedule | Fund ratio picks schedule A–H | Same pages; individual rate notice in March | Schedule C | 2027 not published |
| TDI max weekly wage base | AAW/52 × 1.21 (392-43(b)) | DCD notice in December | 1,500.21 / max deduction 7.50 | 2027 notice not published |
| PHC minimum monthly wage | 86.67 × minimum wage | DCD notice | 1,387.00 | 1,560.06 derived for 2028 (minimum wage 18.00) |
| Minimum wage | Statutory steps, not indexed | HRS 387-2 | 16.00 | 18.00 on 2028-01-01 |
| PIT / withholding | Statutory schedules (Acts 46/2024, 24/2026), not indexed | Booklet A (December) | Rev. 2025 tables | TY2027 tables not published; Act 24 changes the rates (Q1) |

## 12. data_protection
- **HRS 487J-2** [US-HIS5-028]:
  - Prohibited: public display of the full SSN; the full SSN on access cards; transmitting it over an unsecured connection; using the SSN alone as a website login; mailing the full SSN.
  - Exception: employer-to-employee communications and documents required by law may be mailed, but the SSN must never be visible on a postcard or through the envelope.
- **Pay statement:** the SSN is not required on the pay statement (387-6(c)), and no truncation rule exists. Full SSNs are required on UC-B6, new-hire reports and W-2/HW-2 [US-HIS5-012, US-HIS5-021, Booklet A s. 18].
- **Records:** the employer keeps HW-4 and HW-6 on file. HW-4 copies are sent to DOTAX only when allowances look excessive [Booklet A ss. 12, 19].
- Confidence: 85%.

## 13. live_legal_change (2026-01-01 → 2026-11-02)
Sweep: the DOTAX Tax Announcements index (TA 2026-01..10), the DOTAX withholding page, the DLIR UI and WSD pages, and the DCD notice [US-HIS5-029, index saved as `HI-DOTAX-tax-announcements-index_2026-11-02.html`].
1. **Act 24 SLH 2026 (SB 3125 CD2):** **in force** (enacted 2026 session; TA 2026-06 of 2026-07-31).
   - Changes to the TY2027 and TY2029 schedules: 2nd bracket 3.2% → **2.5%**; 3rd bracket 5.5% → **5%**; new **13%** top bracket above 500,000 single / 750,000 HoH / 1,000,000 joint.
   - Level: assessment from TY2027, and **withholding from 2027-01-01** once DOTAX issues the 2027 Booklet A.
   - The Act text was not retrieved (403) [US-HIS5-030, gated]. The HRS 235-51 snapshot's 2027 schedule (Act 46 of 2024) is therefore superseded in part [US-HIS5-027, partial].
2. **Act 35 SLH 2026 (HB 2329):** **in force** since 2026-05-26, for TY2026.
   - IRC conformity as of 2025-12-31.
   - Tips deduction (IRC 224) conformed; overtime deduction (IRC 225) **not conformed**; 132(f) bicycle exclusion suspended; IRC 128 Trump Account exclusion conformed.
   - Level: assessment, plus the W-2 wage exclusion for IRC 128.
3. **Act 118 SLH 2026 (SB 2881):** **in force** since 2026-06-08, for TY2027. Elective Hawaii withholding on 1099-R retirement distributions. Payer level, not wages.
4. **TA 2025-05:** W-2/HW-2 e-file threshold of 10 forms from 2026-01-01 (employer reporting) [US-HIS5-006].
5. **TA 2026-03/-04/-07/-08:** disaster relief (Kona Low, Hurricanes Lala and Lowell). Possible deadline extensions for affected filers; not read.
6. **Minimum wage:** no change in 2026. 18.00 is already enacted for 2028-01-01.
7. **Next year (2027):** none of the 2027 Booklet A, the 2027 UI wage base/schedule or the 2027 DCD notice is published at 2026-11-02.

## Special populations (US-OWN-005, state level)
| Population | Hawaii rule | register_id |
|---|---|---|
| Domestic / household workers | Withholding **is** required on domestic service (unlike federal) unless casual: under 50 USD cash a quarter, or not regularly employed. UI applies once cash pay reaches 1,000 USD in a quarter. Wage-hour law excludes casual domestic service and companionship | Booklet A s. 10-11 [US-HIP51-001]; US-HIS5-013; US-HIS5-003 |
| Agricultural | Withholding required (unlike federal). UI excluded if under 20,000 cash per quarter and 9 or fewer workers / 19 weeks or fewer; H-2A excluded. Minimum wage excludes farms with under 20 employees and coffee harvesting. 20 seasonal overtime-exempt weeks (overtime after 48 h) | Booklet A s. 10; US-HIS5-013; US-HIS5-003 |
| Minors | Work permit to 18: CL-1 Certificate of Employment for ages 14-15 (hour limits); eCL-3 Certificate of Age for 16-17. Newspaper carriers under 18 are outside withholding and UI | US-HIS5-025; Booklet A s. 11(j); US-HIS5-013 |
| Tipped employees | Tip credit 1.25 (1.50 from 2028) only if wage + tips ≥ minimum wage + 7.00. Withholding on tips of 20 USD a month or more that are reported. Act 35 tips deduction (IRC 224) at assessment | US-HIS5-001, Booklet A s. 11(l), US-HIS5-029 |
| Clergy / religious | Ministers and members of religious orders: no withholding (income reportable). Ordained church members outside UI | Booklet A s. 11(r); US-HIS5-013 |
| Students | Students enrolled at the school employing them, school-to-work, student nurses and interns: outside UI. No student minimum-wage rule beyond 387-1 | US-HIS5-013 |
| Nonresident aliens | No specific Hawaii rule read beyond the general nonresident rules (HW-6 / 60 days) and the US-treaty exclusion "income not taxable under US law" | Booklet A s. 11(w), s. 13 |
| Statutory employees | No state rule beyond federal located. Commission-only insurance, real-estate and travel agents and direct sellers (IRC 3508) are outside UI | US-HIS5-013 |
| Government employees | Federal and other-state government service outside UI; the State and counties are outside PHC (393-3). Fees of public officials paid by non-government payers and juror/witness/election fees are not withheld | US-HIS5-013, US-HIS5-016, Booklet A s. 11(h)(i) |
| Certified blind, deaf or disabled | No withholding once the certificate is furnished; still on HW-2 and HW-14 total wages | Booklet A s. 11(g); US-HIS5-026 |
| Military spouses | MSRRA / Veterans Benefits and Transition Act: no withholding (HW-4 box) | Booklet A s. 11(b); US-HIS5-026 |
| Construction contractor employees | No 60-day nonresident exemption; always withheld | Booklet A s. 11 |
| Crew (vessel, interstate airline) | No withholding (voluntary agreement for coastwise crew) | Booklet A s. 11(n) |
| Family employment | Parent, spouse and child under 21 outside UI; elective exclusion for two family owners of 50% or more | US-HIS5-013 |

## MULTI hand-offs (Hawaii answers)
- **MULTI-OQ-2 (SUI wage-base credit):** **yes.** DLIR: "Wages paid by an employer to an employee reported to another state during the calendar year may be combined with Hawaii wages" toward the 64,500 base. Predecessor wages also count [US-HIS5-012, US-HIS5-010]. Confidence 85% (A.3 handbook, consistent with 383-61(e)).
- **MULTI-OQ-3 (TDI coverage of multistate workers):** open. 392-3 defines employment broadly; the localization clause (392-4 / 392-5) was not read [US-HIS5-031]. Recommendation: key TDI to `sui_state` = HI (MULTI default) until it is read.
- **MULTI-OQ-4 (paid sick leave):** not applicable. Hawaii has no general paid-sick-leave law [US-HIS5-024].
- **Pay-statement reach:** 387-6(c) and 388-7 apply to "every employer" for employees employed in Hawaii. There is no explicit extraterritorial clause; out-of-state work was not addressed.

## ACCESS gaps (exact URLs)
- `https://www.capitol.hawaii.gov/hrscurrent/...` → HTTP 403 to curl for every HRS section. All were read from Wayback `id_` snapshots dated 2025-02 to 2026-09 (dates in the register rows). Sections in a snapshot older than 2026 may miss 2025/2026 amendments.
- `https://www.capitol.hawaii.gov/sessions/session2026/bills/SB3125_CD2_.HTM` → 403. The Wayback copy (`/web/20260512230748id_/`) stored the 403. `https://data.capitol.hawaii.gov/sessions/session2026/bills/SB3125_CD2_.HTM` and `.PDF` → 403. Result: the Act 24 SLH 2026 text is not available.
- `https://www.capitol.hawaii.gov/hrscurrent/Vol07_Ch0346-0398/HRS0390/HRS_0390-0002.htm` → 403, and the Wayback copy also 403. The child labor rules come from the DLIR page instead.
- `https://labor.hawaii.gov/ui/employers/` → 404, and no Wayback copy.
- `https://cse.ehawaii.gov/` → connection failed (000), and no Wayback copy.
- DLIR "Contribution Rates Explained" Table 2 (the A–H rate schedules) is not in the HTML text; it is probably an image or a missing element.

## Open questions
- **Q1** `pit.bracket.*` / `pit.withholding.table.*` for 2027-01-01.
  - Need: the exact TY2027 single and married thresholds and cumulative amounts after Act 24 SLH 2026 (2.5% / 5% / 13%), and the 2027 withholding tables.
  - Closes with the DOTAX 2027 Booklet A (expected December 2026 at tax.hawaii.gov/geninfo/a2_b2_4empl_whhold/) or the Act 24 text (a browser pass on capitol.hawaii.gov).
  - Do not derive the figures from TA 2026-06 alone.
- **Q2** `sui.rate.min` / `sui.rate.schedule.c`: the minimum rate and the full Schedule C table.
  - Closes with DLIR Table 2 (the image on labor.hawaii.gov/ui/contribution-rates-explained/) or HRS 383-68 (a Wayback read).
  - Lead only: Schedule C runs from 0.0% to 5.6%.
- **Q3** `bik.conformity.hsa` / `bik.conformity.list`: the full HRS 235-2.3(b) list of non-operative IRC sections after Act 35 SLH 2026.
  - Closes with Act 35 or with HRS 235-2.3 as amended in 2026 (capitol.hawaii.gov, browser pass) or the DOTAX TIR on Act 35, if one is issued.
- **Q4** `reporting.w2.hi.efw2_notes`: the Hawaii-specific EFW2 requirements (RS record, Hawaii Tax ID position).
  - Closes with DOTAX Publication EF-10 (Hawaii SSA File Upload) on tax.hawaii.gov/eservices/.
- **Q5** `reporting.ui.ucb6.format`: the bulk or file format for UC-B6 (if any) beyond online entry.
  - Closes with the DLIR UI employer reporting instructions behind uiclaims.hawaii.gov (gated) or a DLIR wage-file spec.
- **Q6** `garnish.state_tax_levy`: the DOTAX wage levy (HRS 231-25 or similar).
  - Closes with an HRS 231 read or a DOTAX collections page.
- **Q7** `tdi.multistate.coverage`: the HRS 392-4/392-5 localization of employment (MULTI-OQ-3).
  - Closes with a Wayback read of HRS 392-4 and 392-5.
- **Q8** `ui.wage_base.2027`, `tdi.max_weekly_wage_base.2027`: the December 2026 DLIR and DCD notices.
- **Q9** The HFLL employer threshold (100+) comes from the DLIR FAQ. HRS 398-1 was not read; low risk.

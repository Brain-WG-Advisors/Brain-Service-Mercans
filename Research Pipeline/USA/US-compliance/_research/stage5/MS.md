# Stage 5 — Mississippi (MS): findings across the 13 domains

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Mandate block: US-MQ-45 (answered at seal attempt 6; T3).
Budget declared: 60 fetches / 2 h. Used: about 35 fetches (curl + 5 web searches for leads), about 30 minutes. Under the 75% mark.
- Register shard: `00-official-sources/_register-shards/S5-MS.csv`, 19 rows (US-MSS5-001..019), all `active`. Tiers: A.1 ×7, A.2 ×8, A.3 ×4. No tier-B row.
- New files: `00-official-sources/ccg-sources/MS/`, 16 files, 8.8 MB. The largest is the MDHS employer guide at 4.1 MB (under 5 MB, text PDF).
- VPN was off (BR exit IP). Every MS site answered plain curl: dor.ms.gov, mdes.ms.gov, billstatus.ls.state.ms.us, sos.ms.gov, ms-newhire.com and mdhs.ms.gov.

Active rows reused with no re-fetch:
- US-MSPIT-001/-002: Pub 89-700 and the DOR withholding page. The local file is `pdfs/MS/MSDOR-Pub89-700-25-1_rev0725.pdf`; the DOR page copy is dated 2026-11-02.
- US-MSP51-002/-003/-004: MDES law compilation and the rates page.
- US-MSL-002, US-MSP52-002/-003/-005/-006, US-MSP9L-001, US-MSP10-001, US-MSP51-001.

**Headline.**
- **Rate change:** 2025 HB 1 (Build Up Mississippi Act) is **in force**. It cuts the rate on taxable income above 10,000 USD as follows: 4.0% for 2026, **3.75% for 2027**, 3.5% for 2028, 3.25% for 2029 and 3.0% from 2030. Cuts after that depend on revenue triggers [US-MSS5-001].
  - 2026 withholding runs on the Pub 89-700 tables (effective 2026-01-01) or on the DOR "Computer Payroll Accounting – For Periods in 2026" formula [US-MSS5-002, US-MSS5-003].
  - As of 2026-11-02, DOR has published neither 2027 tables nor a 2027 formula. Level: liability is set by the statute; the WTC changes only when DOR republishes.
- **2026 session sweep:** no enacted change to withholding, the minimum wage, the UI base, leave or pay statements. The one payroll-adjacent act is HB 4073 (2026), the Mississippi Work and Save Program. It is a voluntary payroll-deduction Roth IRA, with contributions due by 2028-08-01 [US-MSS5-016, US-MSS5-017].

---

## 1. labour_code
- **Minimum wage:** no state minimum-wage law. Employers covered by the FLSA pay 7.25 USD/h [US-MSS5-010].
  - 2026 bills HB 543 and HB 741 (a 10.00 USD state minimum) **died in committee** on 2026-02-03 [US-MSS5-016]. No 2027 rate exists.
- **Local minimum wages:** prohibited. Miss. Code 17-1-51 (2013 HB 141, effective 2013-07-01) bars counties and municipalities from setting a minimum or living wage, or a minimum number of vacation or sick days, for private employers [US-MSS5-009].
- **Overtime:** FLSA only. No state overtime statute was found, and HB 204 (2026, overtime income exclusion) died [US-MSS5-016].
  - Confidence 80%. This negative rests on the DOL table and the measure sweep; a full-text search of the Code was not possible (Lexis, see ACCESS gaps).
- **Pay frequency:** Miss. Code 71-1-35 reaches only two groups [US-MSS5-015]:
  - (a) manufacturers employing 50 or more and employing public labor: pay every two weeks or twice a month;
  - (b) public service corporations: pay semimonthly, covering wages earned within 15 days of payment.
  - No other private employer has a statutory frequency. The statute text itself was not read; the source is the DOL WHD summary.
- **Method of payment / direct deposit / paycard:** no MS statute located. Confidence 60%.
- Confidence for the domain: 80%.

## 2. income_tax
- **Authority and law:** MDOR administers the tax. The withholding law is Miss. Code 27-7-301 et seq. (Withholding Law of 1968); the regulations are 35 Miss. Admin. Code Pt. III Subpt. 11 [US-MSS5-004, US-MSPIT-002].
- **2026 rates:** 0% on the first 10,000 USD of taxable income and 4.0% above it [US-MSS5-001, US-MSS5-002].
- **Certificate:** Form 89-350 (Rev. 07/25). A federal W-4 is not accepted [US-MSS5-002].
  - No certificate on file: withhold as single with zero exemption [US-MSS5-002, US-MSS5-019].
  - Exemption amounts: single 6,000; married 12,000 (spouses both employed may split it in 500 multiples); head of family 9,500; each dependent, age-65 or blind exemption 1,500.
  - The employer sends DOR a copy of any certificate that claims more than 10 allowances, or claims "exempt" where wages normally exceed 200 USD a week [US-MSS5-019].
  - A no-liability "exempt" certificate is valid through April 30 of the following year [US-MSS5-004].
- **Method (formula = oracle) [US-MSS5-003]:**
  - AGP = period pay × periods (1 / 12 / 24 / 26 / 52 / 260).
  - TI = AGP − (EX + STDED). STDED is S 2,300, H 3,400, M 4,600, B 2,300.
  - TAX = (TI − 10,000) × 4% if TI > 10,000, else 0.
  - PWT = TAX / periods, **rounded to whole dollars**. Any additional amount the employer agrees to is added in whole dollars.
  - Tables: above the table's wage range, add excess × 4% to the largest table figure [US-MSS5-002]. The regulation lets computer formulas be used if their results are consistent with the tables [US-MSS5-004].
  - **G-DERIVE (Python):** Table A, single, weekly reproduces at the bracket's upper bound. Example: 450–460 at 0 exemption gives (460 × 52 − 2,300 − 10,000) × 4% / 52 = 8.94 → 9, which matches the table. All 8 test rows matched.
  - At the midpoint, one row differs (240–250: 0.34 → 0 against the table's 1). The tables are therefore built at the upper bound, and the formula and the tables can differ by 1 USD. Both are authorised.
- **Supplemental wages:**
  - Paid with regular wages: aggregate.
  - Paid separately: aggregate with the current or the last regular period and subtract tax already withheld.
  - If tax was withheld from regular wages, the regulation allows withholding on the supplemental pay "as if no exemption had been claimed" [US-MSS5-004].
  - Pub 89-700 allows the top-bracket rate (4%) where aggregation over-withholds substantially [US-MSS5-002].
  - There is no fixed flat supplemental rate; it follows the year's top rate. Vacation pay paid on top of regular pay counts as supplemental.
- **Not subject to MS withholding** [US-MSS5-004, US-MSS5-019, US-MSS5-002]:
  - domestic service in a private home;
  - agricultural labour;
  - services outside the trade or business;
  - ministers;
  - pensions and annuities;
  - tips paid directly by customers (tips paid through the employer are subject);
  - Native Americans living and working on a reservation (Form 80-340).
- **Resident / nonresident:**
  - **Resident:** withhold on all wages. Wages for work in another state are excluded to the extent that state's tax is withheld. A resident who commutes to a state with no income tax is withheld MS tax on all wages [US-MSS5-004 Ch.09; US-MSS5-019].
  - **Nonresident:** withhold only on wages for MS services, split by earnings ratio. If the base situs or principal place of work is in MS, withhold on all wages unless another state requires withholding [US-MSP52-002, US-MSS5-004].
  - **Nonresident threshold:** none if the MS earnings for the year will be below the standard deduction for the filing status (2,300 / 3,400 / 4,600) [US-MSS5-019].
  - **Credit for tax paid to another state:** at assessment [US-MSP52-003].
  - **Reciprocity:** none (MULTI matrix).
- **Local income taxes:** none [US-MSP10-001].
- Confidence: 95% on the 2026 mechanics; the date of the 2027 tables is unknown.

## 3. social_security (SUI / SDI / PFML / levies)
- **SUI agency:** MDES. Contributions are employer-only and may not be deducted from wages (71-5-351(1)) [US-MSS5-011].
- **Wage base:** 14,000 USD per employee per calendar year since 2011. Fixed in statute, not indexed [US-MSS5-011, US-MSP51-002].
  - Wages paid by a predecessor count toward it.
  - **Wages reported under another state's UC law count** toward the MS base: in 71-5-353(4), "employment" includes service under another state's UC law. This answers the MULTI hand-off for MS.
- **Rates:**
  - New employer: 1.00% in year 1, 1.10% in year 2, 1.20% from year 3.
  - Experience-rated range: 0.0%–5.4%; the standard rate is 5.4%.
  - Rates exclude the Workforce Investment and Training contribution [US-MSP51-003, US-MSS5-011].
  - G-DERIVE: 14,000 × 1% = 140.00 USD of maximum first-year cost per employee.
- **Workforce Investment and Training contribution:** 0.20% of taxable wages, employer-paid (WET 0.15 + OWD 0.01 + MS Works 0.04) [US-MSL-002, US-MSP51-004].
  - Whether it applies in 2026 is **not confirmed**: the MDES rate page says only that it "might be applicable for the rate year".
- **Rounding:** fractions under 0.5 cent are dropped; 0.5 cent or more rounds up [US-MSS5-011].
- **SDI/TDI/PFML/LTC:** none in MS [US-MSP52-006].
- **Coverage thresholds:**
  - agricultural labour: covered at 20,000 USD in a quarter, or 10 or more workers in 20 weeks;
  - domestic service: covered at 1,000 USD in a quarter;
  - excluded: children under 21 employed by a parent, students employed by their own school, ministers, 501(a) organisations paying under 50 USD a quarter, and federal employment [US-MSS5-011].
- **Edition caveat:** the MDES statute compilation is current only through the 2023 session. 2024–2026 amendments to Title 71 ch. 5 were not checked, although the 2026 sweep found none [US-MSS5-016].
- Confidence: 90%. The 2026 status of the workforce levy is open.

## 4. payslip_statute
- No MS statute requires a pay statement or itemised deductions (US-OWN-006 limit; US-MSP52-004 is MANUAL B).
- Default: the federal rules only. No language rule exists [US-MSP9L-001].
- Related duties:
  - SSN must appear on the W-2 [US-MSS5-002].
  - W-2 within 30 days after termination, if requested or on termination [US-MSS5-004 Ch.15].
- Records: keep payroll, employee lists, salaries, SSNs and addresses for 3 years [US-MSS5-019].
- Confidence 75%. This negative is not proven by a full-text search of the Code.

## 5. reporting_instruments
- **Withholding return:** Form 89-105 coupon or TAP, due the 15th of the month after the period [US-MSS5-019, US-MSS5-004].
  - Monthly if average liability is 300 USD a month or more; otherwise quarterly. DOR assigns the frequency.
  - No depository system: payment goes with the return.
  - E-file and e-pay are mandatory at 20,000 USD or more of liability in any period. A zero return is required.
  - Bulk filing goes through FSET.
- **Annual reconciliation:** no separate annual withholding reconciliation. Form 89-140 goes only with paper W-2s or 1099s (fewer than 10) [US-MSS5-002].
- **State W-2:**
  - Due January 31; no extensions.
  - EFW2 with the RS record (state code 28) through TAP upload.
  - Mandatory electronically for 10 or more W-2s, for a single payroll provider all year, and for employee-leasing companies.
  - W-2C is required if MS wages or withholding change [US-MSS5-005, US-MSS5-019].
  - The spec on file is Pub 89-145 Rev 10/25 (2025 season). The TY2026 edition is not yet seen.
- **Quarterly UI report:** UI-2 (tax) and UI-3 (wage detail), due April 30, July 31, October 31 and January 31. A zero report is required [US-MSS5-012, US-MDES UI-2/3 R instructions].
  - File format: ICESA "S" record (275 characters, UIWAGE.TXT), or the EFW2 RS record with these required positions: 1-2, 3-4, 10-18, 19-68, 197-202, 203-213 and 248-267 [US-MSS5-013].
  - Bulk UI-2 by CD is limited to preparers with 25 or more clients [US-MSS5-014].
  - Interest is 1% a month; damages are 10% [MDES UI-2/3 R instructions, local `pdfs/MS/MDES-UI-2-3-R_instructions.pdf`].
- **New hire:** report within **15 days** of hire to the MS State Directory of New Hires (ms-newhire.com; Miss. Code 43-19-46, 93-11-101) [US-MSS5-006, US-MSS5-007].
  - Covers rehires after a break of 60 days or more.
  - Required employee fields: name, address, SSN, hire date, DOB, gender, salary, pay frequency, medical-insurance eligibility.
  - Required employer fields: FEIN (the same as on the UI report), name, address, state EIN.
  - Penalty: 25 USD, or 500 USD where employer and employee conspire.
- **Registration:**
  - DOR withholding account via TAP. Required for employers in MS, for those paying MS residents anywhere, and for those paying nonresidents for MS work. Account number: 8 digits [US-MSS5-019].
  - MDES UI account: online registration.
  - Agent authorisations: MDES J-9 [US-MSP52-005]; DOR Form 21-002 POA, whose text was not read (US-MSP51-006, MANUAL).

## 6. leave
- No state paid sick leave or PFML. Local paid-leave mandates are preempted (17-1-51) [US-MSS5-009, US-MSP52-006].
- Sick pay under a wage-continuation plan is wages for withholding [US-MSS5-002].
- No other state-mandated paid leave with a payroll impact was found. Voting, jury and military leave were not researched (no pay-impact rule known). Confidence 75%.

## 7. termination
- **Final pay timing:** no MS final-pay statute located; the employer's regular payday applies (lead only). Confidence 60%. See the ACCESS gap on the Mississippi Code.
- **Vacation payout:** no statute located; employer policy governs.
  - Severance and dismissal pay are wages subject to withholding [US-MSS5-004 Ch.02(101)(4); US-MSS5-019].
  - Lump sums over 500 USD to an employee under an IWO with arrears: notify MDHS 45 days before payment and hold the money up to 30 days [US-MSS5-008].
- **W-2:** within 30 days of termination [US-MSS5-002, US-MSS5-004].
- **UI separation notice:** none found as an employer duty. MDES runs an online "Report Separation or Refusal of Work" channel (not read).
- **WARN-type state law:** none known (not researched; not payroll-relevant).

## 8. benefits_in_kind (state conformity)
- IRC 125 cafeteria, 127 educational assistance and 129 dependent care: excluded and not subject to MS withholding [US-MSS5-004 35.III.2; US-MSS5-019].
- 401(k)/403(b)/457-type deferrals: excluded from gross income in the year deferred (Miss. Code 27-7-16, per regulation). MS PERS contributions are excluded [US-MSS5-004].
- Employer accident and health contributions: excluded. Meals and lodging for the employer's convenience: excluded [US-MSS5-004].
- **HSA, transit (IRC 132(f)) and group-term life over 50,000: not confirmed.** See Open questions. Default: follow federal.
- Pensions and annuities: not subject to MS withholding [US-MSS5-019].
- **New (2026 HB 4073):** a voluntary state payroll-deduction Roth IRA. Participating employers withhold and remit after-tax employee contributions [US-MSS5-017].
  - Auto-enrolment with opt-out; escalation of up to +1% a year, capped at 8%. Start by 2028-08-01.
  - Payroll level: a post-tax deduction, only for employers that opt in.

## 9. deductions_garnishments
- **Child support IWO** [US-MSS5-008]:
  - Start no later than the first pay period after 14 days.
  - Remit to the SDU within 7 working days.
  - Fees: the employer may take 2.00 USD a month from the employee; an additional 5.00 USD administrative fee is withheld and sent to the SDU.
  - Limits are the CCPA's: 50/60%, or 55/65% with arrears over 12 weeks. Arrears are at least 20% of current support.
  - Priority: child support ranks above all other garnishments; only federal tax liens entered earlier rank ahead. Multiple orders are prorated.
  - Lump-sum hold as in domain 7. Guide dated 2020; current edition unconfirmed.
- **Creditor garnishment (Miss. Code 85-3-4), tier-B lead only, text not read:**
  - Wages are exempt for 30 days after service of the writ.
  - After that, the CCPA 25% limit or the 30 × FMW floor applies.
  - Support and state-tax creditors are exempt from the 30-day wait.
  - Recorded as an ACCESS gap; no register row.
- **Wage-deduction authorisation:** no MS statute located (lead: 71-1-45 assignment of wages; not read).
- **State tax levies:** DOR uses the general levy power (not researched).
- Under-collected withholding may be recovered from later wages [US-MSS5-004 Ch.13].

## 10. collective_agreements (prevailing wage)
- MS has no state prevailing-wage law [US-MSP51-001; DOL page dated 2023-01-01]. Davis-Bacon applies on federal work (FED unit). Confidence 85%.

## 11. indexation
- **Nothing in MS payroll law is indexed annually.**
  - PIT rates follow a fixed statutory schedule (2026 4.0% → 2030 3.0%) [US-MSS5-001].
  - Exemptions and standard deductions are statutory amounts, unchanged since 2000 per Pub 89-700 [US-MSS5-002].
  - The SUI base of 14,000 is fixed [US-MSS5-011]. No state minimum wage exists.
- The only annual variables are each employer's SUI experience rate and the workforce levy decision (rate notice).
- G-DERIVE: the formula and table reconciliation in domain 2.

## 12. data_protection
- Breach notice (2010 HB 583, effective 2011-07-01; tier-B lead codifies it as Miss. Code 75-24-29): notify affected MS residents without unreasonable delay [US-MSS5-018].
  - Covers name plus SSN, driver's licence number or financial account number, which includes payroll data.
- No MS rule truncates the SSN on pay statements; the full SSN is required on the W-2 [US-MSS5-002].
- Record retention: 3 years (DOR) [US-MSS5-019].
- Confidence 80%.

## 13. live_legal_change (2026-01-01 → 2026-11-02)
- **2027 PIT rate 3.75%:** in force (2025 HB 1). Level: liability. The withholding change waits for DOR's 2027 tables and formula, not yet published [US-MSS5-001].
- **2026 session (measure list dated 2026-06-22)** [US-MSS5-016]:
  - Enacted: HB 4073, the Work and Save Program (approved 2026-04-08; Sections 17-18 effective 2026-03-01, the rest 2026-07-01) [US-MSS5-017].
  - Also enacted: SB 2369 (child support out of gaming winnings, not wages) and employer income-tax credits HB 343 (ICHRA), SB 2867 (child care) and SB 3228 (skills training). None of these changes payroll withholding.
  - Died: HB 204 (overtime exclusion), HB 543 and HB 741 (minimum wage).
- **2025 HB 1 PERS:** a new hybrid tier for members joining from 2026-03-01. This affects government-employer payroll only [US-MSS5-001 file, long title].
- Not done: the MDOR news page and the MDES news for 2026 were not swept item by item. The legislative measure list covers statute changes.

## Special populations (US-OWN-005, state round)
| Population | MS rule | register_id |
|---|---|---|
| Domestic / household workers | Exempt from MS income-tax withholding (voluntary by agreement). UI covered at 1,000 USD in a quarter | US-MSS5-004, US-MSS5-019, US-MSS5-011 |
| Agricultural | Exempt from MS withholding (voluntary). UI covered at 20,000 USD in a quarter or 10 workers in 20 weeks | US-MSS5-004, US-MSS5-011 |
| Minors | No minimum wage beyond FLSA. Family members, including children under 18, are subject to withholding. UI excludes a child under 21 employed by a parent. State child-labour hours law not read (lead: Miss. Code 71-1-17..29) | US-MSS5-019, US-MSS5-011 |
| Tipped employees | Federal tip credit only (no state minimum wage). Tips paid directly by customers: no MS withholding. Tips paid through the employer: withheld | US-MSS5-010, US-MSS5-019 |
| Clergy / religious | Ministers' pay is exempt from MS withholding and excluded from UI. Parsonage rental allowance is excludable | US-MSS5-004, US-MSS5-011 |
| Students | UI excludes students employed by their own school. They may file a no-liability exempt certificate (part-year workers) | US-MSS5-011, US-MSS5-004 |
| Nonresident aliens | Withheld like other employees on MS-source wages (Pub 89-700 introduction) | US-MSS5-002 |
| Statutory employees | No state rule beyond federal (DOR follows federal employee/contractor rules) | US-MSS5-019 |
| Government employees | State, counties and cities are withholding employers. PERS contributions are excluded from income. New PERS tier from 2026-03-01 | US-MSS5-002, US-MSS5-004, US-MSS5-001 |
| Corporate officers | Employees for withholding | US-MSS5-019 |
| Native Americans on a reservation | Exempt with Form 80-340 | US-MSS5-019 |

## MULTI hand-offs (MS answers)
- **SUI base credit for wages reported to another state:** YES. 71-5-353(4) counts employment under another state's UC law [US-MSS5-011].
- **PFML/SDI for multistate workers:** not applicable (MS has none).
- **Paid sick leave for workers partly in MS:** not applicable (no state law; local laws preempted).
- **Pay-statement reach:** not applicable (no MS pay-statement statute).
- **Correction for MULTI.md section 2.2:** MS is listed under "Credit at assessment only (no withholding rule)", but MS **has** a resident withholding rule.
  - Withhold MS on all wages, except to the extent another state withholds.
  - A commuter to a state with no income tax is withheld MS on all wages [US-MSS5-004 35.III.11 Ch.09(100); US-MSS5-019].
  - Suggest moving MS to the "home State withholds unless the work State requires withholding" row, while keeping the credit at assessment.
- **Nonresident threshold (MULTI 2.4):** MS starts on day 1 using the earnings ratio, with one exception: no withholding when annual MS earnings are below the standard deduction for the filing status [US-MSS5-019].

## ACCESS gaps
- **Mississippi Code of 1972 (official text):** published only through LexisNexis public access (JS application, not fetched). Sections not read in an official copy:
  - 71-1-35 (pay frequency): DOL summary used instead;
  - 85-3-4 (wage garnishment exemption): tier-B lead only;
  - 71-1-45 (assignment of wages);
  - 71-1-17..29 (child labour);
  - 27-7-16 (deferral exclusion): cited through the regulation;
  - 43-19-46 (new hire): cited through the SDNH page.
  - Closing route: the Lexis public-access URL in a browser pass, or the session law of each section's last amendment on billstatus.ls.state.ms.us.
- `https://mdes.ms.gov/media/231725/filelayout_bulkfilingtable102920.pdf` (UI-2 bulk layout): not fetched; low priority.
- The DOR Form 21-002 POA text was not read (US-MSP51-006 stays MANUAL).

## Open questions
1. **2027 withholding tables and formula** (3.75% rate): not published as of 2026-11-02. What would close it: the DOR withholding page listing Pub 89-700 for 2027 and a "Computer Payroll Accounting – For Periods in 2027" flowchart (re-check in December 2026).
2. **Workforce Investment and Training contribution (0.20%) for 2026:** applied or suspended? What would close it: the MDES 2026 rate notice (UI-1/rate letter), or an MDES statement on the 2026 rate year, or the 71-5-355 trigger text in a post-2023 Code edition.
3. **HSA, transit and group-term life conformity:** MS-specific treatment not confirmed. What would close it: Miss. Code 27-7-15 / 27-7-17 in the current Code, or the MDOR Form 80-100 instructions (2025) on federal adjustments.
4. **Creditor garnishment limits (85-3-4) and final-pay timing:** read the official Code text (see ACCESS gaps).
5. **Pub 89-145 for TY2026** (W-2s filed January 2027): watch for the Rev. 10/26 edition.
6. **MULTI.md section 2.2 classification of MS:** see the hand-off correction above. The MULTI owner should re-bind.

# Stage 5 — FED (federal layer) findings

Worker: Stage 5 FED. Run: 2026-11-02, 07:10–07:40 (about 57 fetches out of a 90 budget). Register shard: `00-official-sources/_register-shards/S5-FED.csv` (rows US-FEDS5-001..032). Source files: `00-official-sources/ccg-sources/FED/` (each file has the date in its name).

Reuse note: rows US-FED-001..030 had **no local file**, and their cited files under `pdfs/FED/` (p15_2026, rp-25-32) are missing on disk. Every IRS 2026 edition was therefore re-acquired and registered as an S5 row that carries a local file. The old rows remain valid citations. The synthesis should point consumers to the S5 row for the local copy.

Supersession for the merge (I cannot edit the main register): **US-FEDS5-028 supersedes US-FEDP6-001**, and it resolves the gated **US-FEDR3-004**. On merge, set US-FEDP6-001 to `superseded` with effective_to 2026-08-25, and close US-FEDR3-004 to point at US-FEDS5-028. US-FEDS5-029 replaces the already-superseded US-FED-029.

---

## 1 — labour_code
- **Minimum wage:** USD 7.25/h, effective 2009-07-24, 29 U.S.C. 206(a)(1)(C). The DOL WHD page confirms it. No federal indexation, and no 2026 or 2027 change has been enacted [US-FEDS5-017]. Employers pay the highest of the federal, state and local rates (state units).
- **Overtime:** 1.5 × the regular rate for hours over 40 in a workweek, 29 U.S.C. 207(a)(1). There is no federal daily overtime [US-FEDS5-018].
- **Tipped employees:** an employee is tipped if they receive more than USD 30/month in tips (203(t)). The minimum cash wage is 2.13 and the maximum tip credit is 5.12 (7.25 − 2.13, re-derived). The employer must give notice before taking the credit and may not keep tips [US-FEDS5-019].
- **EAP exemption salary floor:** USD 684/week (biweekly 1,368, semimonthly 1,482, monthly 2,964). It is 455 in PR/USVI/Guam/CNMI and 380 in American Samoa. This is the current eCFR text [US-FEDS5-020].
- **Pay frequency, pay-day timing and method of payment:** federal law has no rule. The FLSA requires payment by the regular payday. Frequency, timing and direct-deposit/paycard consent are state rules.
- Confidence: high.

## 2 — income_tax (FIT) incl. 2b non-resident
- **Method:** Pub. 15-T (2026), Worksheet 1A, with the Annual Percentage Method tables [US-FEDS5-001].
  - Line 1g is 12,900 for MFJ and 8,600 otherwise, applied when the Step 2 box is not checked. Each pre-2020 W-4 allowance is worth 4,300.
  - STANDARD thresholds:
    - MFJ: 0/19,300/44,100/120,100/230,700/422,850/531,750/788,000
    - Single: 0/7,500/19,900/57,900/113,200/209,275/263,725/648,100
    - HoH: 0/15,550/33,250/83,000/121,250/217,300/271,750/656,150
    - Rates: 0/10/12/22/24/32/35/37%.
  - Step-2-checked thresholds are also in the row.
  - **G-DERIVE:** I recomputed column C for all three STANDARD schedules in Python and it matches (top values 206,583.50 / 192,979.25 / 191,171.00). The zero brackets equal the 2026 standard deduction minus line 1g: 32,200 − 12,900 = 19,300; 16,100 − 8,600 = 7,500; 24,150 − 8,600 = 15,550. The standard deductions were confirmed in a second document family, Rev. Proc. 2025-32 [US-FEDS5-010].
  - Rounding to whole dollars is optional [US-FED-001].
- **W-4 (2026, created 12/8/25):** the input fields are filing status, Step 2 flag, Step 3 amount, 4(a), 4(b) and 4(c). Exemption is now a checkbox below 4(c), and the exemption lapses, so a new W-4 is required for 2027 [US-FEDS5-006].
- **Supplemental wages:** flat 22% is optional. 37% is mandatory on supplemental wages above USD 1,000,000 in the year. Backup withholding is 24% [US-FEDS5-003].
- **2b Non-resident aliens (withholding level):**
  - Pub. 15-T adds an amount to wages for the withholding computation only.
    - Table 2 (2020+ W-4): weekly 309.60, biweekly 619.20, semimonthly 670.80, monthly 1,341.70, annual 16,100.
    - Table 1 (pre-2020): weekly 226.90, annual 11,800.
    - Derived: T2 annual = single standard deduction; T1 = 16,100 − 4,300.
    - The add-on does not apply to 22%/37% supplemental wages [US-FEDS5-002].
  - Notice 1392 (Rev. 1-2020, still the posted edition): the employee checks Single/MFS, writes "NRA" below 4(c), and cannot claim exempt [US-FEDS5-015].
  - Pub. 515 (2026): treaty-exempt wages claimed on Form 8233 are reported on 1042-S, not in W-2 box 1. The commercial-traveler exception is ≤90 days and ≤USD 3,000 with a foreign employer. 2026 1042-S must be filed via IRIS [US-FEDS5-016].
- **Local income tax and reciprocity:** not federal; covered in the MULTI and state units.
- Confidence: high.

## 3 — social_security (FICA, FUTA)
- **FICA:**
  - OASDI is 6.2% employee plus 6.2% employer up to 184,500 (2026).
  - Medicare is 1.45% each, with no cap.
  - Additional Medicare Tax is 0.9%, employee only, on wages over 200,000 in the calendar year regardless of filing status, with no employer match [US-FEDS5-005; base re-derived in US-FED-003].
  - The 2027 base of 192,300 is in US-FED-022, but **I could not re-verify it today (ssa.gov 403)**.
- **FUTA:** 6.0% gross, 0.6% net, on the first 7,000 [US-FED-007, US-FEDS5-031].
  - Credit reductions **final for 2025:** CA 1.2%, USVI 4.5%.
  - **Potential for 2026** (DOL table of 2026-01-15): CA 5.3% (1.5 + BCR 3.8), USVI 4.8%. These become final only if the advance is still outstanding on **2026-11-10** [US-FEDS5-009, status partial].
- **Employer levies:** none at federal level beyond FICA and FUTA.
- Confidence: high, except the 2026 FUTA final, which is a live item.

## 4 — payslip_statute
- No federal law sets pay-stub content or delivery. The FLSA prescribes records only (29 CFR 516.2 [US-FED-010]).
- Payroll records are kept for **3 years** (29 CFR 516.5) [US-FEDS5-021]. IRS employment-tax records are kept for **4 years** [US-FEDS5-003].
- Pay-statement content is state law.
- Confidence: high.

## 5 — reporting_instruments
- **Deposits:** the 2026 lookback period runs 2024-07-01..2025-06-30. Liability of 50,000 or less in the lookback means a monthly depositor (deposit by the 15th of the following month); more than 50,000 means a semiweekly depositor (Wed/Thu/Fri paydays deposit the following Wednesday; Sat–Tue paydays deposit the following Friday). Any day with 100,000 or more accumulated must be deposited the next business day. Holidays follow DC legal holidays [US-FEDS5-004].
- **Form 941:** quarterly, due the last day of the month after the quarter; amounts in cents.
- **Form 944:** annual, only on written IRS notice, for liability of 1,000 or less.
- **Form 940:** annual, due Jan 31 (Feb 10 if all FUTA was deposited); FUTA is deposited when accumulated liability exceeds 500 [US-FEDS5-031]. The 2026 i940 is not yet published; I read the 2025 edition.
- **W-2/W-3 2026:**
  - Due to SSA and employees **2027-02-01**.
  - New Box 12 codes: **TP** (cash tips), **TT** (qualified overtime), **TA** (Trump-account employer contributions). Box 14 is split into 14a and **14b (Treasury Tipped Occupation Code)**.
  - W-2 is required at 2,000+ wages even with no withholding.
  - SSN may be truncated on employee copies only [US-FEDS5-007].
- **EFW2 TY2026:** **ACCESS gap** [US-FEDS5-032, gated].
- **ACA:** ALE members (50+ FT/FTE) file 1094-C/1095-C. For TY2025 these were due 2026-03-02 on paper and 2026-03-31 electronically, with e-filing required at 10+ returns. Furnishing can be done by website notice. The 2026 affordability percentage is **9.96%** [US-FEDS5-012, US-FEDS5-011]. The TY2026 i1094/1095-C is not yet published.
- **New hire:** report name, address, SSN, first-day-of-work, and employer name, address and FEIN within **20 days** of hire. Electronic filers may instead send two monthly transmissions 12–16 days apart. Multistate employers may designate one state [US-FEDS5-024].
- **Reporting-agent authorization:** Form 8655 [US-FED-008/009/028].
- Confidence: high, except EFW2 (not read).

## 6 — leave
- FMLA: 12 workweeks in a 12-month period (26 for a military caregiver). The leave may be unpaid, and the employer may require substitution of accrued paid leave [US-FEDS5-026].
- There is no federal paid sick or annual leave for private employers. Federal contractors fall under EO 13706; the DOL page exists, but I did not transcribe its accrual figures (open).
- State PFML benefits: the employee contribution and any employer voluntary payment are W-2 wages (Rev. Rul. 2025-4, Notice 2026-6, cited in the W-2 instructions) [US-FEDS5-007].
- Confidence: medium-high.

## 7 — termination
- DOL: "Employers are not required by federal law to give former employees their final paycheck immediately." Final-pay timing and vacation payout are state law [US-FEDS5-025].
- WARN requires 60 days' notice before a plant closing or mass layoff; pay in lieu is the payroll touchpoint [US-FEDS5-025].
- Severance is wages for FIT, FICA and FUTA [US-FEDS5-029].
- An early final W-2 can be furnished on request [US-FED-016].
- Confidence: high.

## 8 — benefits_in_kind (federal exclusions, the baseline the states conform to or depart from)
Source: Pub. 15-B (2026) [US-FEDS5-008].
- Parking and transit: 340/month each.
- Health FSA: 3,400 (carryover 680) [US-FEDS5-010].
- Dependent care: **7,500** (raised by P.L. 119-21).
- Educational assistance: 5,250, now permanent.
- Group-term life: coverage above 50,000 is FICA wages, using the Table 2-2 monthly cost per 1,000 by age (0.05 … 2.06).
- Moving-expense and bicycle-commuting exclusions are eliminated.
- 2026 limits for 401(k), HSA and FEIE: US-FED-023, -024, US-FED-P5-2-002.
- Trump-account employer contribution up to 2,500 excluded, from 2026-07-04 [US-FEDS5-030].
- The 2026 cents-per-mile rate was not printed in Pub. 15-B; I did not fetch it (open).
- Confidence: high.

## 9 — deductions_garnishments
- CCPA: the lesser of 25% of disposable earnings or the amount above 30 × 7.25 = **217.50/week**. Support orders: 50/60%, or 55/65% with arrears over 12 weeks [US-FEDS5-023].
- IRS levy exempt amounts 2026 (Pub. 1494), e.g. Single with 0 dependents: weekly 309.62, monthly 1,341.67, plus 101.92/week per dependent. Derived: 16,100/52 and 5,300/52 [US-FEDS5-014].
- IWO priority over other garnishments except an earlier IRS levy [US-FED-P5-1-006].
- **IWO OMB 0970-0154 renewal: approved without change 2026-08-25, now expiring 2029-08-31.** The current form is extended one year while states reprogram for the revised (gig-worker fields) IWO/e-IWO [US-FEDS5-028]. This closes the "renewal pending" modelling of US-OWN-007.
- Confidence: high.

## 10 — collective_agreements
- A CBA binds the certified unit only [US-FED-018].
- Davis-Bacon (federal construction over 2,000) [US-FED-019]: **weekly certified payroll** to the contracting agency; the prime is responsible for subcontractors; optional form WH-347 [US-FEDS5-027].
- Confidence: high.

## 11 — indexation
- C-CPI-U under 26 U.S.C. 1(f)(3) [US-FED-026]. Rev. Proc. 2025-32 covers 2026 [US-FEDS5-010]; the OASDI base is AWI-indexed [US-FED-003].
- The FLSA minimum wage, the CCPA multiplier and the 684 salary floor are **not** indexed. The 2,000 information-return threshold is indexed after 2026.
- **The 2027 Rev. Proc. and the 2027 401(k)/IRA notice were not yet published.** I checked the IRS news-release list for October 2026: IR-2026-117..129 contain neither. Only tier-B projections exist (401(k) 25,500), and they are not used.
- Confidence: high for 2026; 2027 is open.

## 12 — payroll_data_protection
- The SSN may be truncated to a TTIN (XXX-XX-1234) on employee W-2 copies, but never on Copy A, and the EIN is never truncated (26 CFR 301.6109-4) [US-FEDS5-022, US-FEDS5-007].
- No federal statute governs SSN display on pay statements or general payroll privacy for private employers; this is state law.
- Confidence: medium-high. I made no search for an FTC/GLBA payroll-specific rule; not in scope.

## 13 — live_legal_change (2026-01-01 → 2026-11-02)
- **P.L. 119-21 (enacted 2025-07-04, in force)** [US-FEDS5-030]:
  - Tips and overtime deductions operate at **assessment**, reach withholding only through W-4 4(b), and are **employer reporting** via W-2 TP/TT/14b.
  - Trump accounts start 2026-07-04 (W-2 TA).
  - Dependent care exclusion 7,500.
  - Thresholds 2,000.
  - TY2025 penalty relief only (Notice 2025-62) [US-FEDS5-013].
- **FUTA 2026 credit reductions:** final determination on 2026-11-10 (CA, USVI potential) [US-FEDS5-009].
- **IWO renewal approved 2026-08-25** [US-FEDS5-028].
- **2027:**
  - OASDI base 192,300 [US-FED-022] (re-verification blocked).
  - W-4 exemption must be renewed for 2027 [US-FEDS5-006].
  - 2027 Pub. 15-T, Rev. Proc. and plan limits are not yet published.
- IRS proposed regulations of Oct 2026 (IR-2026-121, PTC; IR-2026-117, scholarship credit) do not touch employer payroll.

---

## Special populations (federal layer, US-OWN-005)
| Population | Federal rule | register_id |
|---|---|---|
| Domestic/household | FIT only by agreement; FICA if 3,000+ cash in 2026 (exempt under 18 unless principal occupation); FUTA if 1,000+ in any quarter; Schedule H | US-FEDS5-029, US-FED-005 |
| Agricultural | FICA/FIT at 150 cash per worker or 2,500 total; Form 943; FUTA farm tests | US-FEDR3-006, US-FED-P5-1-002 |
| Minors / family | Child under 18 working for a parent's sole proprietorship or partnership: FICA exempt, FUTA exempt under 21; spouse: FUTA exempt | US-FEDS5-029 |
| Tipped | Cash wage 2.13, tip credit 5.12; tips 20+/month subject to FIT/FICA; W-2 TP/14b | US-FEDS5-019, US-FEDS5-003, US-FEDS5-007 |
| Clergy/religious | Minister: no FIT/FICA withholding (SE tax; voluntary FIT withholding) | US-FED-030 |
| Students | Private school: FICA/FUTA exempt; public school: FICA exempt unless sec. 218; work-experience programs: FICA taxable | US-FEDS5-029 |
| Nonresident aliens | 15-T add-on, Notice 1392 W-4, 8233/1042-S treaty wages, commercial-traveler exception | US-FEDS5-002, US-FEDS5-015, US-FEDS5-016 |
| Statutory employees | FICA yes, FIT no (4 categories) | US-FEDR3-005 |
| Government employees | FIT yes, FUTA no, FICA with sec. 218 / Medicare-only exceptions | US-FEDS5-029 |
| Election workers | FICA at 2,500+ in 2026 | US-FEDS5-003 |

---

## ACCESS gaps (exact URLs, 2026-11-02)
- https://www.ssa.gov/employer/efw/26efw2.pdf returned HTTP 403. The Wayback copy https://web.archive.org/web/2026id_/https://www.ssa.gov/employer/efw/26efw2.pdf returned 404, and the archive.org availability API returned 429. → US-FEDS5-032 (gated)
- https://www.ssa.gov/employer/EFW2&EFW2C.htm returned 403.
- https://www.ssa.gov/oact/cola/cbb.html returned 403, and the Wayback copy returned 403 (blocks re-verification of 2027 OASDI 192,300, US-FED-022).
- https://www.acf.hhs.gov/css/employers/employer-responsibilities/new-hire-reporting returned 202 with an empty body (bot challenge), and its Wayback copy returned 202 with an empty body. The statute 42 U.S.C. 653a is used instead.
- https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title29-section206… returned 404 for all six sections. Replaced by govinfo USCODE-2024; no gap.

## Open questions
1. `futa.credit_reduction.2026` (CA, USVI): final after 2026-11-10. **Closes with** the DOL OUI "FUTA Credit Reductions" page/xlsx update after 2026-11-10, or the 2026 Schedule A (Form 940) instructions.
2. `efw2.ty2026.layout`: **closes with** SSA Pub. 42-007 (TY2026) downloaded via the browser pass or from a non-blocked network.
3. `ss.oasdi.wage_base` 2027 = 192,300: re-verification needed. **Closes with** the SSA 2027 COLA fact sheet or cbb.html read in the browser pass.
4. 2027 federal indexation (Rev. Proc. for TY2027, 401(k)/IRA notice, 2027 Pub. 15-T draft): not published as of 2026-11-02. **Closes with** IRS releases expected Nov–Dec 2026.
5. TY2026 Instructions for Forms 940 and 1094-C/1095-C: not yet issued; the 2025 editions were read. **Closes with** the IRS releases (usually Dec–Jan).
6. EO 13706 contractor paid-sick-leave accrual figures were not transcribed. **Closes with** 29 CFR 13.5 from eCFR (one fetch).
7. 2026 business standard mileage rate (cents-per-mile BIK valuation): not printed in Pub. 15-B. **Closes with** the IRS 2026 mileage notice.
8. State go-live of the revised IWO/e-IWO (gig fields) within the one-year extension: **closes with** an OCSE Action Transmittal implementing ICR 202607-0970-002.

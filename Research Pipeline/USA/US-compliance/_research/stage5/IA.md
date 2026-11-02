# Stage 5 - IA (Iowa) - 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Scope: `_prompts/stage5-brief.md`, JUR = IA. Mandate block US-MQ-32 (answered at attempt 3, re-checked at seal attempt 6) is reused here, not researched again.

**Budget.** Declared 60 fetches and 2 h, working ceiling 45. Used about 43 fetches and 2 web searches (leads only) in about 20 minutes of wall clock. Acquisition stopped at the ceiling.

**Network.** The VPN was off (Brazilian exit IP). legis.iowa.gov, revenue.iowa.gov and workforce.iowa.gov all answered plain curl, so nothing was blocked.

**Register shard.** `00-official-sources/_register-shards/S5-IA.csv` holds rows US-IAS5-001 to US-IAS5-029. All 29 are `active`, with tiers A.1, A.2 and A.3 only. No tier-B row carries a number.

**Files.** New files are in `00-official-sources/ccg-sources/IA/`: 31 source files plus their .txt extractions, 5.6 MB in total. The largest is `IAC-871-ch23_2026-11-02.pdf` at 0.5 MB, and no file is over 5 MB. Statute PDFs are the "Iowa Code 2026" edition (footers dated 10-13 Dec 2025).

**Reused active rows (not fetched again).**
- Withholding: US-IA-001, US-IAP52-002 (422.16, local file in `pdfs/IA/`).
- UI: US-IA-002, US-IAL-002, US-IAP9V-001 (rate computations 2026, local).
- Local surtaxes: US-IAP51-005, US-IAP52-001.
- Pay statement: US-IAP51-002, US-IAL-001 (91A.6, local).
- Prevailing wage: US-IAP51-001.
- POA: US-IAP51-003, US-IAP51-004.
- PFML absence: US-IAP52-004.
- Reciprocity: US-MULTI-018.
- Language: US-IAP9L-001/-002.
- Levy absence: US-IAP9W-001.

---

## CORRECTION FOR THE SYNTHESIS (read first)
**Iowa withholding is computed to the cent, not rounded to the whole dollar.**
- US-IA-001's figure text says "round result to nearest dollar". The MANDATE (US-MQ-01, part 1 and the currency block) lists IA among the whole-dollar rounding states.
- The 2026 sources say otherwise:
  - The formula (US-IAS5-005) contains no rounding instruction, and all ten worked examples carry cents (e.g. 59.26, 38.72, 145.50).
  - The 2026 table instructions state, at Step 5, "The withholding amounts listed in the tables are rounded to the nearest cent" (US-IAS5-015).
- **What the build should model:** compute T4 to 0.01, half-up. I re-derived all six 2024+ IA W-4 examples in Python with that rule and every one matched to the cent.
- **Supersession:** the synthesis should treat the rounding clause of US-IA-001 as superseded by US-IAS5-005/-015. The rest of US-IA-001 stands. Its supplemental clause, marked "search snippet", is now proven A.1 and A.2 (section 2 below).
- Confidence: 95% for 2026. I did not read the 2025 formula, so I cannot say whether whole-dollar rounding ever applied in an earlier year.

---

## 1. labour_code
- **Minimum wage**: 7.25/h from 2008-01-01, or the federal minimum if it is higher (Iowa Code 91D.1(1)(a),(b)). [US-IAS5-001, A.1]
  - During the first 90 calendar days of employment the floor is 6.35/h (91D.1(1)(d)).
  - Enterprises with annual gross volume under 300,000 are exempt. The exemption does not cover laundries, construction, hospitals, care institutions, schools or public agencies (91D.1(2)).
  - Nothing is scheduled for 2026 or 2027 in the Code 2026 text.
- **Local minimum wage: none.** Iowa Code 364.3(12) bars city ordinances on minimum or living wage, any form of employment leave, benefits or scheduling. Ordinances adopted before 2017-03-30 have been void since that date. [US-IAS5-021, A.1]
- **2026 bill not enacted.** HF 2212 would have set a direct-care minimum of 20.00/h (19.10/h in the first 90 days) from 2026-07-01. It was only introduced, on 2026-01-29, and referred to committee. See section 13. [US-IAS5-028]
- **Overtime**: Iowa has no state overtime rule. Chapter 91D adopts the FLSA definitions and exemptions and has no overtime clause, so FLSA 1.5x over 40 applies (federal layer).
  - This is a negative finding from reading 91D.1 in full. The rest of ch. 91D (91D.2 onward) was not fetched.
  - Confidence: 85%.
- **Pay frequency** (91A.3(1)): at least monthly, semimonthly or biweekly, on regular paydays designated in advance. [US-IAS5-002, A.1]
  - Payday may be at most 12 days after the end of the pay period, not counting Sundays and legal holidays.
  - A written agreement may vary these rules.
  - Commissions may be paid as a credit, with a true-up at least every 12 months.
- **Method of payment** (91A.3(2)-(3)): US currency or a negotiable instrument. Payment in kind needs written consent. [US-IAS5-002]
  - Direct deposit may be made a condition of employment for employees hired on or after 2005-07-01. Three exceptions: the account costs would take pay below minimum wage, the employee would pay account fees, or a CBA prohibits it.
  - Wages go by mail on the employee's written request. The employer keeps the request for 2 years after it ends.
  - The employer pays overdraft charges caused by late pay.
  - Expenses are reimbursed in advance or within 30 days of the claim.
  - No paycard-specific rule was located.
- **Liquidated damages for late wages**: 5% of the unpaid wages per day. Sundays, holidays and the first 7 days are excluded, and the total is capped at the unpaid amount (91A.2(6)). [US-IAS5-027]
- **Minors under 16** (92.7): hours 7 a.m. to 9 p.m. (11 p.m. from June 1 to Labor Day). [US-IAS5-014]
  - Limits: 8 h/day and 40 h/week; 6 h/day and 28 h/week while school is in session.
  - A 30-minute break is due for shifts of 5 hours or more.
- Confidence: 95% for minimum wage, frequency and payment method; 85% for "no state overtime".

## 2. income_tax
- **Rate**: a flat 3.8% on residents and nonresidents from tax year 2025 (Iowa Code 422.5(1)(a)). [US-IAS5-006, A.1]
  - Nonresidents are taxed on all income, then multiplied by the Iowa-source fraction (422.5(1)(b)). This happens at **assessment**.
  - Resident credit for tax paid to another state: 422.8(1)(a), at assessment (file `IowaCode-422.8_2026-11-02.pdf`, not registered separately; same level as the MULTI table).
- **2026 withholding formula** (effective 2026-01-01, released November 2025). [US-IAS5-005, A.2; derived arithmetically]
  - Steps: T1 = G - D; T2 = T1 x 3.80%; T3 = T2 - W/P; T4 = T3 + A.
    - G = gross taxable wages for the period; D = the deduction amount below.
    - W = total allowance amount on the IA W-4; P = pay periods per year; A = additional withholding requested.
  - D, annual amounts for a 2024 or later IA W-4:

    | IA W-4 status | Annual D | Per-period D |
    |---|---|---|
    | (A) Other, MFJ whose spouse has earned income, or status missing | 13,000 | weekly 250; biweekly 500; semimonthly 541.67; monthly 1,083.33; daily 50 |
    | (B) Head of Household | 19,500 | biweekly 750; monthly 1,625 |
    | (C) MFJ whose spouse has no earned income, or QSS | 26,000 | biweekly 1,000; monthly 2,166.67 |

  - For an IA W-4 from 2023 or earlier: Single uses 13,000 and Married uses 26,000, and W = number of allowances x 40.
  - Pay periods P: daily 260, weekly 52, biweekly 26, semimonthly 24, monthly 12, annual 1. Any other frequency is annualised.
  - Pre-tax retirement and health contributions are not taxable wages.
  - **Oracle**: the 10 worked examples in the formula PDF. Example 6 (monthly 5,000, Head of Household, W = 160) is printed without its final figure; my derivation gives 114.92.
  - A tables alternative exists (US-IAS5-015). Both methods are acceptable per the IDR FAQ.
- **Withholding certificate**: 2026 IA W-4, form 44-019a (11/13/2025). [US-IAS5-029, US-IAP52-001]
  - Statuses: Other (incl. single), Head of Household, MFJ, QSS, plus "does your spouse also have earned income?".
  - Dependent allowance: 40 each.
  - EXEMPT entry with the year. Nonresidents may not claim it. Exemption thresholds: 13,500 MFJ/HoH and 9,000 single under 65; 32,000 and 24,000 at 65 or over. [US-IAS5-016]
  - Military-spouse exemption box.
  - Due within 15 days of hire. With no IA W-4 on file, withhold at zero allowances (701 IAC 307.3(3)(a)). Keep W-4s for 4 years.
  - A new W-4 is due within 10 days when allowances decrease.
- **Supplemental wages: 3.8%.** [US-IAS5-006 + US-IAP52-002, A.1; US-IAS5-016, A.2]
  - Applies when the employer treats them separately and federal tax is withheld on a flat-rate basis (422.16(2)(e); 701 IAC 307.2(1)(c)).
  - Otherwise, aggregate the supplemental payment with regular wages and use the tables or formula.
- **Rounding**: to the cent. See the CORRECTION above. [US-IAS5-005, US-IAS5-015]
- **Reciprocity**: with IL only. [US-MULTI-018, US-IAS5-016]
  - An IL resident working in Iowa files 44-016, and the employer withholds IL tax.
  - An Iowa resident working in IL files IL-W-5-NR, and the employer withholds Iowa tax.
  - Non-wage income is not covered.
- **Nonresidents working in Iowa** are withheld at the resident rate. Exceptions: [US-IAS5-016]
  - IL residents (reciprocity, above);
  - interstate rail, air and truck employees who work in at least one other state (federal law);
  - nonresident film/TV workers, if an exemption is filed on 44-017;
  - out-of-state disaster-response workers (29C.24).
- **Day or dollar threshold for nonresidents**: none located. Withholding starts with the first day worked in Iowa.
- **Local income taxes**: none are withheld.
  - The school-district surtax and the EMS surtax are settled on the IA 1040 by district of residence. The employee may adjust allowances or line 8 to cover them. [US-IAP51-005, US-IAP52-001, US-IAS5-029]
  - 422.16 carries no surtax withholding. [US-IAP52-002]
- **OBBBA (P.L. 119-21)**: Iowa conforms on tips, overtime, car-loan interest and the senior deduction. [US-IAS5-019, A.2]
  - Tips, overtime and car-loan interest have **no withholding allowance** in 2026. They operate at **assessment**, so payroll withholds on full tips and overtime.
  - The senior deduction (up to 6,000) may be claimed as an IA W-4 allowance.
- **Non-primary jobs and NRA guidance** (IDR, employee-driven line 8 amounts): [US-IAS5-016]
  - non-primary job or NRA, allowances under 80: 15,000 / P x 3.8%;
  - non-primary job, allowances of 80 or more: 30,000 / P x 3.8% (29,200 for NRAs);
  - head of household without a 2025+ W-4: 7,500 / P x 3.8%.
- Confidence: 95%.

## 3. social_security (SUI; no SDI/TDI/PFML)
- **Agency**: Iowa Workforce Development (IWD), UI Tax Bureau. Employer portal: myIowaUI.org. [US-IAL-002, US-IAS5-024]
- **Taxable wage base**: [US-IAS5-008, A.1; US-IAS5-009/-010, A.2, derived arithmetically]
  - CY2025: 39,500.
  - **CY2026: 20,400.**
  - **CY2027: 21,100** (announced 2026-06-30).
  - Formula (Iowa Code 96.1A(36) as amended by SF 607 = 2025 Acts ch 125): one third of the statewide average annual wage, rounded up to the next 100, but never below the FUTA base.
  - Derivations:
    - 61,098.90 / 3 = 20,366.30, rounded up to 20,400 (2026);
    - 63,213.58 / 3 = 21,071.19, rounded up to 21,100 (2027).
- **Rates 2026**: Table D, ranks 1-9, from 0.000% to 5.400%. The maximum rate fell from 9% to 5.4% under SF 607, and the number of tables from 8 to 4. [US-IAP9V-001, US-IAL-002]
  - New non-construction employers: the rank-4 rate but not less than 1.000%, so 1.000% in 2026. This applies until the account has been chargeable for 12 consecutive quarters (96.7(2)(c)). [US-IAS5-011]
  - New construction employers: the rank-9 rate, 5.400%.
  - Rate notices are mailed in November and may be appealed within 30 days.
  - **The 2027 table is not yet published** (open question).
- **Employee contribution: none.** 871 IAC 23.6(2) says the employer may not deduct any part of the contributions from an employee's pay. [US-IAS5-024, A.1]
  - Nonprofit reimbursements are not deductible either (96.7). [US-IAS5-011]
- **Base per employer**: each employer pays up to the base for the same employee (23.6(1)).
  - **Wages reported to another state do NOT count toward the Iowa base**: "Only wages reported to the Iowa unemployment insurance program may be used..." (23.6(3)). This answers the MULTI hand-off.
  - A successor that receives an experience transfer may count the predecessor's wages (23.6(4)).
- **Tips** that the employee reports to the employer are taxable wages for UI (23.5). [US-IAS5-024]
- **SDI/TDI/PFML/LTC: none.** [US-IAP52-004, A.2; mandate answer US-MQ-32 part 4]
- **Employer levies**: none beyond UI on the revenue side. [US-IAP9W-001]
  - The 260E/260F job-training items are **credits that divert withholding**, not extra levies:
    - New Jobs Training Program credit (NJC): 1.5% or 3% of new-employee gross payroll;
    - Supplemental New Jobs credit (SJC): 1.5%;
    - Accelerated Career Education credit (ACE): up to 10%;
    - Targeted Jobs credit (TJC): 3%.
  - They are claimed on the withholding credit schedule of the quarterly return. [US-IAS5-016]
- Confidence: 95%. The 2027 rate table is open.

## 4. payslip_statute
- **Content** (Iowa Code 91A.6(4)): each regular payday, a statement of hours worked, wages earned and deductions made. [US-IAP51-002, US-IAL-001, A.1]
  - Delivery: by mail, secure electronic means, at the workplace, or by access to view. Electronic delivery needs no separate consent.
  - On request, an itemised statement with an explanation of the computation is due within 10 working days (91A.6(3)).
- **Retention**: payroll records for 3 calendar years. This 91A.6(1) duty is triggered by a director notice after a paid claim or a civil penalty. [US-IAP51-002]
  - IA W-4s are kept 4 years. [US-IAS5-016]
- **Reach**: 91A applies to employees "employed in this state" (91A.2(3),(4)). The pay-statement duty follows Iowa work location, not Iowa residence. This answers the MULTI hand-off. [US-IAS5-027]
- **Language**: no rule, and the payslip is in English. [US-IAL-001, US-IAP9L-001/-002]
- Confidence: 90%.

## 5. reporting_instruments
- **Registration**: obtain an FEIN, then register for an Iowa withholding permit on GovConnectIowa. Permits issued since 2021-11-15 have 9 digits (older ones have 12). [US-IAS5-016, US-IAS5-018]
  - UI account: myIowaUI.org. [US-IAL-002]
- **Withholding deposits and return** (422.16(4); IDR page): [US-IAS5-007, A.1; US-IAS5-016, A.2]

  | Filer | Threshold | Deposit due |
  |---|---|---|
  | Quarterly | under 6,000/yr and at most 500/month | with the quarterly return |
  | Monthly | 6,000-120,000/yr | 15th of the following month (3rd month with the quarterly return) |
  | Semimonthly | over 5,000 per semimonthly period | 1st-15th due on the 25th; 16th-end due on the 10th of next month; electronic payment mandatory |
  | Annual (election) | at most 2 employees, with written consent | paid with the Q1 return |

  - Quarterly return due on the **last day of the month after the quarter**, filed electronically via GovConnectIowa.
  - A return is due for every period, even with zero wages.
- **Annual reconciliation: none.** "VSPs are no longer required to be filed." [US-IAS5-017, A.2]
- **State W-2 filing**: e-file through GovConnectIowa by **February 15**, only for W-2s and 1099s carrying Iowa withholding. No paper and no PDF. [US-IAS5-017, US-IAS5-018, A.2]
  - Format: EFW2-based ASCII, 512-byte records. **"The IDR file format is unique to IDR"**: the SSA file is rejected.
  - RS record: state code 19; permit number in positions 248-267; unemployment, local and supplemental fields blank or zero.
  - Iowa-specific **RV** total record: RS count, Iowa wages, Iowa tax.
  - Alternative for small filers: Key & Send manual entry.
  - Payroll providers register as Bulk Filers, which can take up to 4 weeks.
  - Employee copies are due by January 31. A terminated employee who asks gets the W-2 within 30 days of the last payment (422.16(8)). [US-IAS5-007]
  - The spec page is dated 2023-01-09 and covers TY2023-2025 filed during 2026. A TY2026 edition was not seen (open question).
- **Quarterly UI report** (871 IAC 23.8(1)): Employer's Contribution and Payroll Report (65-5300) plus quarterly wage detail by SSN, submitted electronically. [US-IAS5-024, A.1]
  - Due on the last day of the month after the quarter, or the next business day.
  - Late quarters are delinquent and incur the 96.14(2) penalty.
  - The wage-detail file layout (myIowaUI upload spec) was **not acquired** (open question).
- **New hire** (Iowa Code 252G.3): report to the Centralized Employee Registry within **15 days** of hire or rehire, or by electronic transmissions 12-16 days apart. [US-IAS5-012, A.1]
  - Fields: employer name, address and FEIN; employee name, address, SSN and DOB; whether dependent health coverage is available and the date the employee qualifies; the address for IWOs.
  - Means: page 3 of the IA W-4 (44-019d), fax, approved electronic media, or online.
  - Independent contractors are reported too (IDR page).
  - Multistate employers may designate one state.
- **POA**: IA 2848 (14-101a) for IDR; IWD 68-0092 for UI. [US-IAP51-003, US-IAP51-004]
- Confidence: 90%. The UI wage-detail file spec is open.

## 6. leave
- **Paid sick leave: none.** Iowa has no state mandate, and 364.3(12) bars city leave ordinances. [US-IAS5-021]
  - Negative finding. The Code chapters 91A and 91D were read, and no sick-leave statute was located. Confidence: 85%.
- **Vacation, holiday, sick and severance pay** are wages only when due under an agreement or employer policy (91A.2(7)(b)). [US-IAS5-027]
- **PFML benefit-side interaction**: none, because there is no programme.
- **Other mandated leave with pay impact**: none located within budget. Jury and military leave were not researched (open question, low payroll impact).
- Confidence: 80%.

## 7. termination
- **Final pay** (91A.4): by the **next regular payday** for the period in which the wages were earned. There is no discharge/resignation distinction. [US-IAS5-003, A.1]
  - Commission true-up within 30 days.
- **Vacation payout**: only when due under an agreement or a policy of pro-rata accrual, prorated to the fraction of the year worked (91A.4). With no policy, there is no statutory payout.
- **Separation notice to the employee**: no statute located. [US-IAS5-026, A.3]
  - IWD asks employers to report separations through the "Separation Notice Alleging Disqualification" portal form, a claim-protest practice.
  - The Notice of Separation and Wage Request must be answered within 10 days.
- **State WARN**: not researched (payroll impact marginal).
- Confidence: 90%.

## 8. benefits_in_kind
- **Rolling IRC conformity** applies from TY2023, and the starting point is federal taxable income. [US-IAS5-020, A.2]
  - The listed departures are business items only.
  - Withholding applies to "the same wages ... as federal", and employer retirement and health contributions are excluded. [US-IAS5-016]
- **Result**: 401(k), 125, HSA, transit and group-term life follow federal treatment. No Iowa departure was located.
  - Confidence: 85%. An exhaustive Iowa modification list for wage exclusions was not read.
- **Payment in kind** needs written consent (91A.3(2)). [US-IAS5-002]
  - No state meal/lodging credit rule beyond the FLSA was located.

## 9. deductions_garnishments
- **Wage deductions** (91A.5) need a legal requirement, a court order, or written employee authorisation for the employee's benefit. [US-IAS5-004, A.1]
  - Prohibited deductions: shared till shortages (except one 45-day manager agreement), dishonoured checks, breakage or customer default unless wilful, lost property unless it was assigned equipment, gratuities, PPE, and relocation costs over 20 (91E.1 employers).
- **Creditor garnishment** (642.21): the CCPA limits apply, **plus an Iowa annual cap per judgment creditor** by expected annual earnings. [US-IAS5-013, A.1]

  | Expected annual earnings | Annual cap per creditor |
  |---|---|
  | under 12,000 | 250 |
  | 12,000 to under 16,000 | 400 |
  | 16,000 to under 24,000 | 800 |
  | 24,000 to under 35,000 | 1,500 |
  | 35,000 to under 50,000 | 2,000 |
  | 50,000 or more | 10% of expected earnings |

  - The caps do not apply to support.
  - No discharge for garnishment.
- **Child support IWO** (252D.17): the IWO has priority over any garnishment or assignment. [US-IAS5-022, A.1]
  - The employer may deduct a **fee of up to 2 per payment**. Support plus the fee must stay within 15 USC 1673(b).
  - Remit to the Collection Services Center within **7 business days** of payday.
  - Payments for several employees may be combined.
- **State tax levies**: not researched (open question).
- Confidence: 90%.

## 10. collective_agreements (prevailing wage)
- **No state prevailing-wage law.** Iowa appears on the US DOL WHD list of states without one (page dated 2023-01-01). [US-IAP51-001, A.2]
  - Davis-Bacon applies to federal contracts only.
  - No certified-payroll duty at state level.
- Confidence: 80%. The DOL page is from 2023, and no Iowa statute was searched for later enactment.

## 11. indexation
- **UI wage base**: annual, set at one third of the statewide average annual wage (96.1A(36)). IWD announces it in its late-June release with the benefit maxima. [US-IAS5-008/-009/-010]
  - Derivations reproduced for 2026 and 2027 (section 3).
- **UI rate table**: chosen annually by a trust-fund formula, with a November notice. [US-IAL-002]
- **Income tax**: a flat 3.8%, not indexed. The withholding deduction amounts (13,000 / 19,500 / 26,000) are reissued each November with the formula. [US-IAS5-005]
- **Minimum wage**: not indexed.
- **Garnishment brackets** (642.21): fixed in statute, not indexed.

## 12. data_protection
- **Breach notification** (Iowa Code 715C.2): notify consumers without unreasonable delay. A processor must notify the data owner immediately. [US-IAS5-023, A.1]
- **SSN on pay statements**: no Iowa truncation rule was located in the texts read (91A.6 does not require an SSN on the statement).
  - Iowa Code 715A was not read (open question).
- Confidence: 70%.

## 13. live_legal_change (2026-01-01 to 2026-11-02)
- **SF 607 (2025 Acts ch 125)**: in force from CY2026. The UI wage base was halved (one third of the average annual wage), the maximum rate fell to 5.4%, and the tables went from 8 to 4. Level: **employer UI contribution**. [US-IAS5-008, US-IAS5-009]
- **CY2027 UI wage base 21,100**: announced 2026-06-30 and in force from 2027-01-01. Level: employer UI. [US-IAS5-010]
- **2026 withholding formula and IA W-4**: new for 2026 under OBBBA conformity. In force from 2026-01-01. Level: **withholding**. [US-IAS5-005, US-IAS5-029]
- **OBBBA tips, overtime and car-loan deductions**: conformed, in force for TY2026. Level: **assessment only**, with no withholding allowance. [US-IAS5-019]
- **Sports wagering winnings**: 3.8% withholding from 2026-01-01 where federal withholding applies. Non-wage, out of payroll scope. [US-IAS5-016]
- **HF 2212 (91st GA)**: a direct-care minimum wage of 20.00. **NOT ENACTED**: introduced 2026-01-29, referred to House HHS, no further action. Level: minimum wage. Do not model. [US-IAS5-028]
- **Search limits**: the sweep was the IDR withholding guidance and news links plus the IWD releases. A full Iowa Acts 2026 sweep (all enrolled bills) was not done within budget (open question).

---

## Special populations (US-OWN-005, state round)

| Population | Iowa rule | register_id |
|---|---|---|
| Domestic / household workers | Generally excluded from Iowa withholding (estimated payments if liability is 1,000 or more). UI coverage once 1,000 in wages is paid in a quarter | US-IAS5-016, US-IAS5-025 |
| Agricultural workers | Iowa withholding follows federal withholding. UI coverage at 20,000 in quarterly wages or 10+ workers in 20 weeks. Agricultural family members and labour exchanges excluded from ch. 91A | US-IAS5-016, US-IAS5-025, US-IAS5-027 |
| Minors | State minimum wage applies (no youth rate beyond the 90-day rate). Hour limits under 16. UI excludes a child under 18 employed by a parent (unincorporated business) | US-IAS5-001, US-IAS5-014, US-IAS5-025 |
| Tipped employees | Tip credit up to 40% of the minimum (cash wage at least 4.35 on 7.25) for restaurants, hotels, motels, inns and cabins, if the employee receives more than 30/month in tips. Tips reported to the employer are UI wages. OBBBA tip deduction is at assessment only | US-IAS5-001, US-IAS5-024, US-IAS5-019 |
| Clergy / religious | Clergy generally excluded from Iowa withholding. Church and religious-order services excluded from UI | US-IAS5-016, US-IAS5-025 |
| Students | UI excludes students employed by their own school and curricular work. No state withholding rule beyond federal | US-IAS5-025 |
| Nonresident aliens | IDR additional-withholding guidance (15,000 or 29,200 / P x 3.8%, employee-driven via IA W-4 line 8). Nonresidents may not claim EXEMPT | US-IAS5-016, US-IAS5-029 |
| Statutory employees | No state rule beyond federal located (the IDR page says withholding follows federal) | US-IAS5-016 |
| Government employees | The State and its subdivisions are withholding agents (422.4(18) via 422.16). Cities, counties, school districts and community colleges are UI reimbursing employers (may elect contributions). Ch. 91D minimum wage applies to public agencies regardless of volume | US-IAP52-002, US-IAS5-025, US-IAS5-001 |
| Military spouses | Iowa exemption under MSRRA/VBTA (IA W-4 box with state of domicile) | US-IAS5-016, US-IAS5-029 |
| Interstate transport workers | No Iowa withholding for nonresidents of rail, air or truck employers working in 2+ states | US-IAS5-016 |
| New employees (first 90 days) | Minimum wage floor 6.35 | US-IAS5-001 |
| Corporate officers | UI employees if they perform services | US-IAS5-025 |

The cash wage of 4.35 is derived: 7.25 x 0.60 = 4.35. It assumes the maximum 40% credit.

---

## MULTI hand-offs answered for IA
- **SUI wage-base credit for wages reported to another state: NO.** 871 IAC 23.6(3) counts only wages reported to Iowa. Exception: a successor with an experience transfer (23.6(4)). [US-IAS5-024]
- **Multistate UI coverage**: localization, base of operations, then direction and control (871 IAC 23.24). The interstate reciprocal coverage election is in 23.13. [US-IAS5-024]
- **PFML/SDI coverage of multistate workers**: not applicable (no programme). [US-IAP52-004]
- **Paid-sick-leave coverage**: not applicable (no state or local PSL). [US-IAS5-021]
- **Pay-statement reach**: employees "employed in this state", so the rule follows Iowa work location. [US-IAS5-027]
- **Nonresident threshold**: none located. Iowa withholds on nonresidents from the first day worked, except IL residents and the federal transport carve-out. [US-IAS5-016]

---

## ACCESS gaps
None. Every URL attempted returned HTTP 200 over plain curl:
- legis.iowa.gov code and IAC PDFs, and the bill history;
- revenue.iowa.gov guidance and media;
- workforce.iowa.gov handbook pages and releases.

## Open questions
1. `pit.withholding.rounding`
   - Why: US-IA-001 and the MANDATE currency block say whole-dollar; the 2026 formula and tables say nearest cent.
   - Closes with: the synthesis superseding the rounding clause of US-IA-001 by US-IAS5-005/-015. Optionally, IDR's 2025 formula PDF, to see whether whole-dollar ever applied.
2. `sui.rate_table.2027`
   - Why: the table for CY2027 is not yet published.
   - Closes with: IWD "Information on Rate Computations for Private Employers 2027" or the November 2026 rate notices.
3. `sui.wage_report.file_format`
   - Why: the myIowaUI quarterly wage-detail upload layout was not acquired.
   - Closes with: the IWD myIowaUI file specification (employer portal help or the UI Tax Bureau, iwduitax@iwd.iowa.gov).
4. `w2.state_spec.ty2026`
   - Why: the IDR spec page covers TY2023-2025 filed in 2026.
   - Closes with: the IDR TY2026 edition (expected late 2026 on the same URL).
5. `live_change.acts_2026_sweep`
   - Why: a full sweep of enrolled 2026 Acts touching chs. 91A, 91D, 92, 96, 252D, 422 and 642 was not done.
   - Closes with: the Iowa Legislature "Acts and Joint Resolutions 2026" list, or the Iowa Code 2027 supplement (Dec 2026).
6. `ssn.paystatement_truncation`
   - Why: Iowa Code 715A was not read.
   - Closes with: Iowa Code 715A.10 and 715A.8 text.
7. `garnishment.state_tax_levy`
   - Why: the IDR wage-levy procedure was not read.
   - Closes with: Iowa Code 422.26 / 626 levy provisions or the IDR levy page.
8. `labour.overtime.state_rule`
   - Why: the negative rests on 91D.1 only.
   - Closes with: the DIAL Labor Services wage-hour FAQ, or the rest of ch. 91D.
9. `leave.jury_military`
   - Why: not researched.
   - Closes with: Iowa Code 607A.45 (jury) and 29A.43 (military).

# Stage 5 — Georgia (GA): 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Mandate block: US-MQ-30 (answered at seal attempt 3, register check at seal attempt 6).
Budget declared: 60 fetches / 2 h. Used: about 42 fetches (curl and web search) and about 25 minutes, under the 75% mark.
Register shard: `00-official-sources/_register-shards/S5-GA.csv` (23 rows, US-GAS5-001..023). New sources are in `00-official-sources/ccg-sources/GA/` (17 files, 2.3 MB).
Active rows reused without a re-fetch (their local files were re-read in full this pass):
- US-GA-001 / US-GA-P5-2-003: 2026 DOR guide, `pdfs/GA/GA-DOR-2026-Employers-Withholding-Guide_rev-Sept2026_download-2026-10-29.pdf`, 54 pp.
- US-GA-W1B-001: GDOL handbook DOL-224 R-11/24, `pdfs/GA/GDOL-employer-handbook-DOL-224-R-11-24_chrome-2026-10-29.pdf`, 164 pp.
- US-GAP9W-001/-002: SB 160 (2023).
- US-GAP9L-001: SB 88 (2015), O.C.G.A. 34-7-2.
- US-GA-P5-1-002 (prevailing wage), US-GA-P5-1-003 (SDI/PFML), US-GA-W1B-003 (power of attorney).

Corpus note: `pdfs/GA/` holds the same 2026 guide twice (`GA-DOR-employers-tax-guide-2026_download-2026-10-29.pdf` and `GA-DOR-2026-Employers-Withholding-Guide_rev-Sept2026_download-2026-10-29.pdf`, both 3,474,648 bytes). The synthesis should keep only one (F23).

---

## 1. labour_code
- **Minimum wage:** federal 7.25 USD/h, in force since 2009-07-24. The Georgia rate is 5.15 USD/h (O.C.G.A. 34-4-3), but GDOL says the federal rate applies with only "limited exceptions" [US-GAS5-022, US-GAS5-008]. No increase is enacted for 2027 and no indexation exists.
  - Tier-B lead, not read on an official host: the state-rate exclusions (employers with sales of 40,000 USD or less, farm owners, tipped workers).
- **Local minimum wages:** none. O.C.G.A. 34-4-3.1 preempts every local wage, benefit and scheduling mandate on private employers, including through local purchasing and contracting. The current text was read as quoted in HB 1157 (2026). HB 1157 would repeal the preemption; it is an introduced bill and **not enacted** [US-GAS5-017].
- **Overtime:** FLSA only, 1.5× above 40 hours per workweek. There is no daily overtime and no weekend or night premium. No state law requires breaks [US-GAS5-016, US-GAS5-008].
- **Pay frequency:** at least semi-monthly, in "at least two equal" periods per month for covered employees. Officers, superintendents and heads of departments may be paid monthly [US-GAP9L-001, US-GAS5-008].
- **Method of payment:**
  - Allowed: money, check, direct deposit (credit transfer, with the employee's consent) or payroll card. Each payment must be the full net amount.
  - Payroll card: the employer gives a written explanation of fees at hire or 30 days before the card becomes available, and the employee can opt out.
  - At least one way to access wages free of charge (GDOL) [US-GAP9L-001, US-GAS5-008].
- Confidence: 90%. The statutory text of 34-4-3 was not read on an official host.

## 2. income_tax
- **Rate:** flat **4.99%** for taxable years beginning on or after 2026-01-01, down from 5.19% [US-GAS5-009, US-GA-001].
  - Enactment: HB 463, "Georgia Economic Growth and Tax Relief Act of 2026", **in force**. The Governor signed it on 2026-05-11, retroactive to 2026-01-01.
  - The file read on legis.ga.gov has the same md5 as the Governor's "2026 signed legislation" copy [US-GAS5-009].
  - Withholding timing (operating level): employers kept withholding 5.19% until 2026-05-11 and may use 4.99% from 2026-05-11 [US-GA-001].
- **Withholding method:** tax tables (pp. 31–50) or the percentage method (Tables E/F, pp. 51–52) [US-GAS5-001].
  - Percentage method: wages − standard deduction for the period − (dependent allowance × number of allowances), then × 4.99%.
  - Standard deduction, annual: 30,000 MFJ, 15,000 Single/HoH, 15,000 MFS. Married couples where both spouses earn use the MFS column.
  - Dependent allowance: 5,000 per year.
  - Per-period values (weekly, biweekly, semimonthly, monthly, quarterly, semiannual and daily = annual/365) **were re-derived in Python as annual ÷ periods, rounded to the cent. All 21 values match the tables.**
  - Example 1 (MFJ, semimonthly, 2,000, 1 dependent): (2,000 − 1,250 − 208.33) × 0.0499 = 27.029 → **27.03**.
  - The tables use the top of each wage band. Single weekly, band 276–294: (294 − 288.46) × 0.0499 = 0.2764 → 0.28, which is the value printed in the table.
  - The guide gives no rounding rule beyond cents and says tables and formula "differ slightly". These are the oracle seeds (C37) [US-GAS5-001].
- **Certificate:** Form **G-4, Rev. 06/03/26** [US-GAS5-010].
  - Marital-status letters A–D select the table: A Single; B MFS, or MFJ with both spouses working; C MFJ with one spouse working; D HoH.
  - Line 4: dependent allowances. Line 5: Georgia adjustment allowances, from a worksheet: (itemized deductions − standard deduction) + GA adjustments − non-wage income, ÷ 5,000; a remainder over 2,500 rounds up.
  - Line 6: additional withholding. Line 8a: exempt. Line 8b: military-spouse (MSRRA/SCRA) exemption.
  - The employer mails the G-4 to DOR only if it claims more than 14 allowances or exempt.
  - If no G-4 is filed, use the W-4 if it gives enough information; otherwise withhold as Single with zero allowances.
  - An exempt G-4 stays valid until 15 February of the following year. A new G-4 takes effect from the first payroll after the employer receives it [US-GAS5-004].
- **Supplemental:** bonuses are withheld at "the applicable income tax rate in effect at the time the compensation is paid", which is 4.99% from 2026-05-11. No separate supplemental table exists [US-GAS5-004, US-GA-P5-2-003].
- **Residence and nonresidents:**
  - Resident: legal resident, living in Georgia on a regular basis, or present 183 days or more in the 365 days ending 31 December.
  - Nonresidents: withhold when more than 5% of wages, or more than 5,000 USD, is attributable to Georgia.
  - Residents working in another state: no Georgia withholding if that state requires withholding; otherwise withhold for Georgia [US-GAS5-004].
  - No reciprocity agreement and no 23-day rule [US-GA-P5-2-003].
- **Local income taxes:** none [US-GA-P5-2-003 per the mandate answer, guide full text].
- **Overtime and tip subtractions (HB 463):** each up to 1,750 USD. Overtime applies to tax years 2026–2028, for full-time hourly employees; tips apply from 2026.
  - Operating level: **assessment only**. DOR says not to reduce withholding.
  - Reporting: on the W-2 (box 12 TT and TP, box 14b TTOC; RLA employees "GA OT" in box 14a). There are no G-7 fields in 2026; from 2027 the G-7 collects quarterly totals and employee counts [US-GAS5-009, US-GAS5-003].
- **Nonresident aliens:** the employer is liable for Georgia withholding unless the employee is exempt under a filed IRS Form 8233 and a copy of that form has been sent to DOR (Withholding Tax Unit) [US-GAS5-004].
- Confidence: 95%.

## 3. social_security (state layer: SUI, SDI/PFML, levies)
- **SUI wage base:** 9,500 USD, in force since 2013-01-01 (HB 347, 2012). It is not indexed [US-GA-W1B-001].
- **New-employer rate:** 2026 total **2.70%** = 2.64% contribution (34-8-151(d)) + 0.06% administrative assessment (34-8-181).
  - The assessment runs from 2024-01-01 to 2026-12-31. Article 6 is repealed from 2027-01-01 (34-8-185).
  - From 2027 the contribution is 2.7% under 34-8-151(a), so the total stays 2.70% but with no assessment, unless new legislation intervenes; none was located [US-GAS5-013, US-GAP9W-001].
  - Arithmetic: 0.0264 + 0.0006 = 0.0270 (Python).
- **Experience rate:** reserve ratio = (taxes paid − benefits charged) ÷ 3-year average payroll at 30 June, read against the statutory tables. From 2027 the 34-8-155(c) table applies instead of 34-8-155(e) [US-GAS5-013, US-GAS5-006].
  - Rate notice DOL-626: posted on the Employer Portal by 31 December, no longer mailed.
  - The 2026 rate range is NOT on an A-tier source; a tier-B lead says 0.04–8.10%. Open question Q2.
- **Employee contribution:** none. UI is employer-paid and the assessment may not be deducted from wages [US-GA-W1B-001, US-GAS5-013].
- **Covered employment:** private employers become liable at 1 worker in 20 weeks or 1,500 USD of payroll in a quarter.
  - Agricultural: 10 workers in 20 weeks, or 20,000 USD in a quarter. Domestic: 1,000 USD in a quarter. 501(c)(3) organizations: 4 workers in 20 weeks.
  - Corporate officers are employees.
  - Wages include employee 401(k) deferrals, tips (to the FUTA extent) and board and lodging. Section 125 premiums and employer 401(k) contributions are excluded [US-GAS5-006].
- **SDI/TDI/PFML:** none [US-GA-P5-1-003].
- **Employer levies:** only the UI administrative assessment, 0.06% through 2026-12-31. No transit or training levy (P7/P9 result) [US-GAP9W-001, US-GAP9W-003].
- Confidence: 85%. The 2026 rate range is not sourced.

## 4. payslip_statute
- **No Georgia pay-statement content statute.**
  - Read on official hosts: 34-7-2 (payment form, frequency, payroll-card fees, no statement duty) [US-GAP9L-001], and the 164-page GDOL handbook (wage-and-hour chapter, pp. 14–27), which has no pay-stub, itemization or wage-statement rule. Checked by searching the full text.
  - The other sections of 34-7 Part 1 were read only on a mirror [US-GA-P5-2-002, MANUAL].
  - Build rule: the federal layer only (FLSA records, no statement duty).
- **Delivery:** no state rule, so electronic delivery is not restricted by Georgia law.
- **Language:** no clause (US-MQ-03 closed, US-OWN-006).
- **Retention:**
  - DOR payroll records: at least 4 years after the tax is due or paid [US-GAS5-004].
  - GDOL employment records (34-8-121): at least **7 years**. The record must include full name, **full SSN**, hire and separation dates, the reason for separation, and quarterly wages including the value of non-cash pay and tips [US-GAS5-005].
- Confidence: 85%. The absence is read in A-tier documents, but not as a statute-by-statute read on an official host.

## 5. reporting_instruments
- **Registration:** on GTC (gtc.dor.ga.gov), which issues the withholding number and filing frequency within 15 minutes. UI registration is through the GDOL Employer Portal [US-GAS5-002, US-GAS5-005].
- **Withholding deposits and returns** [US-GAS5-002]. Payer status is set from the lookback period, the 12 months ending the previous 30 June.

  | Payer status | Threshold | Payment | Return |
  |---|---|---|---|
  | Semi-weekly | > 50,000 in the lookback | EFT; payday Wed–Fri → next Wednesday; payday Sat–Tue → next Friday | G-7 Schedule B, quarterly |
  | Monthly | > 200 per month | GA-V by the 15th of the following month | G-7 (monthly payer), last day of the month after the quarter |
  | Quarterly | ≤ 200 per month and > 800 per year | with G-7, last day of the month after the quarter | G-7 |
  | Annual | ≤ 800 per year | with G-7 by 31 January (by GTC request) | G-7 |

  - One-day rule: more than 100,000 withheld for one payday must be paid by EFT on the next banking day.
  - A G-7 over 500 makes EFT and e-filing mandatory from then on. The penalty for not paying by EFT is 10%.
  - A zero G-7 is still required.
  - 2026 dates: Q3 G-7 due **2026-11-02**; Q4 due **2027-02-01**.
- **Annual reconciliation (G-1003) and W-2/1099** [US-GAS5-003]:
  - Deadlines: W-2s and 1099-NEC with Georgia withholding are due 31 January (TY2026: 2027-02-01); other 1099s by 28 February (2027-03-01). A W-2 is not required if no Georgia tax was withheld.
  - E-filing is mandatory when the filer must e-file federally or pays by EFT.
  - Channels: GTC manual entry, the G-1003 Excel/CSV template, or the Federal Format.
  - Federal Format: EFW2 plus a Georgia RS record. The only layout posted is **Rev 01/18** [US-GAS5-011]:
    - 248–267 state employer account number; 274–275 state code; 276–286 state taxable wages; 287–297 state income tax withheld; 298–307 period end date; 331–339 withholding number.
    - **The TY2026 layout (with the GA OT field) and the TY2026 template were not yet posted on 2026-11-02** (open question Q1).
  - 1099s go only through IRIS XML; FIRE / Pub. 1220 is no longer accepted.
  - Georgia withholding statements are not accepted through the Combined Federal/State program.
  - A closing business files statements within 30 days after the final wages.
- **Quarterly UI wage report DOL-4N** [US-GAS5-005, US-GAS5-020]:
  - Due 30 April, 31 July, 31 October and 31 January.
  - Electronic filing: required for employers with 25+ employees today. Channels are Portal direct entry (up to 100 employees), CSV/Excel upload (100–15,000) and SFTP (over 15,000 employees, and payroll service providers).
  - Paper is allowed below 25 employees. The June 2026 proposed rule 300-2-2-.02(6) makes electronic filing mandatory for **all** employers; adoption of that limb is unconfirmed (Q3).
  - Domestic-only employers file the annual DOL-4 by 31 January.
  - Corrections on DOL-3C. A Multiple Worksite Report is filed quarterly.
  - New since the October 2026 rules: placeholder SSN 000-00-000n allowed for a missing new-hire SSN; correct within 30 days on DOL-3C [US-GAS5-021].
- **New-hire reporting:** Georgia State Directory of New Hires (DHS), O.C.G.A. 19-11-9.2 [US-GAS5-012].
  - Deadline: within **10 days** of hire. Electronic filers send two monthly transmissions no more than 16 days apart.
  - Fields: FEIN (the same as on the UI wage reports), employer name and address; employee name, address, SSN, date of birth, start date, medical-insurance availability, state of hire.
  - Channels: web, upload, FTP, fax or mail.
- **Third-party filing:** RD-1061/1062/1063 (DOR) and a GDOL power of attorney [US-GA-W1B-003, US-GA-W1B-001]. Payroll providers serving more than 250 employers must pay by EFT [US-GA-P5-2-003].
- Confidence: 85%. The TY2026 W-2 layout is missing.

## 6. leave
- **No paid sick leave or vacation mandate:** "Neither federal nor state law requires" vacation, sick or personal leave [US-GAS5-016].
- **Family Care Act (O.C.G.A. 34-1-10)** [US-GAS5-015, partial]:
  - Applies to employers with 25+ employees that offer sick leave, and to employees working 30+ hours a week.
  - Up to 5 days of earned sick leave per year may be used for immediate family. The Act does not apply to employers with an ESOP.
  - Read in committee-substitute text only; the enacted version and the sunset history are unconfirmed (Q4).
- **No PFML**, so there is no payroll interaction.
- Confidence: 75%.

## 7. termination
- **Final pay timing:** no Georgia statute. GDOL handles unpaid final wages through FLSA and the Magistrate Court [US-GAS5-022]; the handbook has no final-pay rule.
- **Vacation payout:** contractual only [US-GAS5-007, US-GAS5-016].
- **Severance:** contractual. Withhold Georgia tax if the person is a resident when paid; no Georgia withholding if a nonresident at payment [US-GAS5-004].
- **Separation Notice DOL-800 (form R-02-24)** [US-GAS5-007, US-GAS5-020, US-GAS5-021]:
  - Required for every separated worker, stating the reason.
  - Delivered on the last day of work, or within 3 days if the worker is unavailable.
  - Electronic delivery with an e-signature (UETA) is allowed under the October 2026 rules.
- **Mass Separation Notice DOL-402 / 402A:** filed within 48 hours when 25+ workers at one establishment are separated on the same day for the same reason for 7 days or more. A timely DOL-402 replaces the individual DOL-800s [US-GAS5-020, US-GAS5-007].
- **Final G-7:** within 30 days when the business ceases to have employees [US-GAS5-002].
- **Sales representatives:** commissions are due within 30 days after the agreement ends, and the right cannot be waived [US-GAS5-007].
- Confidence: 85%.

## 8. benefits_in_kind
- Georgia starts from federal AGI and conforms to the IRC each year by a conformity act; HB 1199 conforms to the IRC as of 2026-01-01 (per the 2026 guide).
- 401(k)/403(b)/457 deferrals, Section 125, HSA, transit and group-term life (up to 50,000) follow the federal exclusion. W-2 box 16 follows box 1. **No Georgia departure was located** [US-GAS5-023, US-GAS5-004].
- **UI wage base differs from income tax:** employee 401(k) deferrals are UI wages; Section 125 premiums and employer 401(k) contributions are not [US-GAS5-006].
- Confidence: 80%. The DOR conformity page stops at 2024, so the 2026 detail rests on the guide.

## 9. deductions_garnishments
- **Voluntary deductions:** no Georgia law lists them or requires written consent; GDOL recommends written authorization. The FLSA 30× minimum-wage floor applies [US-GAS5-008].
- **Creditor garnishment** (O.C.G.A. 18-4-5, 2016 rewrite, committee-substitute text) [US-GAS5-014, partial]:
  - Limit: the lesser of 25% of disposable earnings, or the amount by which weekly disposable earnings exceed **217.00** (as printed).
  - The CCPA federal floor, 30 × 7.25 = 217.50, is the binding minimum [US-FED-011]. Use 217.50.
  - Continuing garnishment for support: at most 50% of disposable earnings. It is applied first to current support, accrued daily (annual ÷ 365), then to arrears (18-4-53/-54).
  - Garnishee expense deduction: the greater of 50 USD or 10% of the amount paid into court, capped at 100 USD (18-4-14).
  - No discharge for garnishment on one obligation.
- **Child-support income withholding (DCSS):** the employer may charge up to **25 USD** to set up the deduction and **3 USD per deduction**. Payments go to the Family Support Registry [US-GAS5-019].
- **Priority:** generally only one garnishment at a time, but a child-support order and a tax levy may run together [US-GAS5-008].
- **State tax levy:** the DOR wage-levy statute was not read (Q5).
- Confidence: 70%. The enacted garnishment text and later amendments are unread.

## 10. collective_agreements (prevailing wage)
- No state prevailing-wage law (USDOL WHD state table) [US-GA-P5-1-002]. Only federal Davis-Bacon applies (FED unit).
- Georgia is a right-to-work state [US-GAS5-022].
- Confidence: 90%.

## 11. indexation
- **Nothing is CPI-indexed.**
  - SUI wage base: fixed by statute at 9,500.
  - Minimum wage: fixed (5.15 state; the federal rate applies).
- **Statutory step schedule (not indexation), HB 463** [US-GAS5-009]. Every step is conditional: the Office of Planning and Budget (OPB) checks three revenue triggers and reports by 1 December each year.
  - Rate: −0.125 point a year from 2027 down to 3.99% (8 steps).
  - Standard deduction: +750 MFJ / +375 other per year, up to 36,000 / 18,000.
  - Dependent exemption: +125 per year, up to 6,000.
  - Derivation (Python): if no trigger holds, 2027 = **4.865%**, standard deduction **30,750 / 15,375**, dependent **5,125**.
  - **Not published yet:** the OPB report is due 2026-12-01 (Q6). The publication that will carry the values is the DOR 2027 Employer's Withholding Tax Guide.
- Confidence: 90% on the mechanism; the 2027 values are unconfirmed.

## 12. data_protection
- **Full SSN** is required on GDOL wage records and wage reports [US-GAS5-005, US-GAS5-020].
- **No Georgia rule requiring SSN truncation on pay statements was located.**
  - Lead: O.C.G.A. 10-1-393.8 bars publicly posting or displaying an SSN. It was read only through a mirror and a search summary, so the row is tier B / MANUAL [US-GAS5-018] (Q7).
- **G-4 retention:** the employer keeps the G-4; it is mailed to DOR only in the 14+ allowances or exempt case [US-GAS5-004].
- Confidence: 50%.

## 13. live_legal_change (2026-01-01 → 2026-11-02)
Sweep: DOR guide "What's new", legis.ga.gov 2026 documents surfaced by search, and GDOL news/rules.
1. **HB 463 (2026):** in force, signed 2026-05-11, retroactive to 2026-01-01.
   - 4.99% rate; standard deduction 30,000 / 15,000; dependent 5,000 [US-GAS5-009].
   - Withholding at 4.99% from 2026-05-11 [US-GA-001].
   - OT/tip subtractions operate at assessment; W-2 reporting in TY2026; G-7 changes from 2027 [US-GAS5-003].
   - Operating levels: rate = withholding + assessment; subtractions = assessment + employer reporting.
2. **Competing 2026 bills (HB 1370, Senate substitute to HB 229):** OT/tip exclusions with other limits. Draft text only, **not enacted**; HB 463 is the enacted vehicle. Read and not registered.
3. **HB 1157 (2026):** repeal of the local-mandate preemption. Introduced, **not enacted** [US-GAS5-017].
4. **GDOL rules:** proposed 2026-06-15 [US-GAS5-020]; GDOL announced the updated rules on 2026-10-07 [US-GAS5-021]. Covers the placeholder SSN, electronic Separation Notices, electronic posters for remote staff, and the proposed all-employer e-filing of DOL-4N. Adopted text and effective date were not read. Operating level: employer UI reporting.
5. **UI administrative assessment sunset:** 2026-12-31; the new-employer rate becomes 2.7% contribution only from 2027-01-01 [US-GAS5-013].
6. **G-1003 / W-2 TY2026 layouts:** announced for "late October 2026", not posted at 2026-11-02 [US-GAS5-011].
7. **Next year (2027):** the rate and deduction steps depend on the OPB report of 2026-12-01; the 2027 DOR guide and the GDOL 2027 DOL-626 notices are not yet published.

## Special populations (US-OWN-005, state level)
| Population | Georgia rule | register_id |
|---|---|---|
| Domestic / household workers | No Georgia withholding required (voluntary). UI applies at 1,000 USD cash in a quarter, reported annually on DOL-4 by 31 January with quarterly detail | US-GAS5-004, US-GAS5-006, US-GAS5-005 |
| Agricultural | Farm laborers: withholding not required. UI applies at 10 workers in 20 weeks or 20,000 USD in a quarter | US-GAS5-004, US-GAS5-006 |
| Minors | Employment Certificate DOL-4103 (work permit) kept at the work site for all workers under 18. Minors in entertainment need DOL-4101. Under-16s are barred from mills, factories, laundries etc. The most-protective of state and federal law applies. Newspaper carriers under 18 are outside UI | US-GAS5-008, US-GAS5-006 |
| Tipped employees | Federal cash wage 2.13 with tip credit. HB 463 tip subtraction up to 1,750 at assessment only. W-2 box 12 TP + box 14b TTOC. Tips are UI wages to the FUTA extent | US-GAS5-016, US-GAS5-009, US-GAS5-003, US-GAS5-006 |
| Clergy / religious | Ministers: Georgia withholding not required. Employees of a church or religious order are outside UI | US-GAS5-004, US-GAS5-006 |
| Students | Work-study programme students and student nurses are outside UI. No student minimum-wage rule beyond federal (GDOL pages read) | US-GAS5-006, US-GAS5-022 |
| Nonresident aliens | Withhold unless Form 8233 is filed and a copy is sent to DOR. The general nonresident threshold (5% / 5,000) applies to all nonresidents | US-GAS5-004 |
| Statutory employees | No state rule beyond federal located. The UI test differs from the IRS test, but SS-8 determinations are accepted (handbook p. 48) | US-GAS5-006 |
| Government employees | Public employers report quarterly (most reimburse rather than contribute). Elected officials, legislators, judiciary and National Guard are outside UI. Withholding applies to government employers | US-GAS5-006, US-GAS5-004 |
| Military spouses | G-4 line 8b MSRRA exemption; no Georgia wages on the W-2 | US-GAS5-010 |
| Family of a sole proprietor | Parent, spouse or child under 21 of the owner is outside UI | US-GAS5-006 |
| RLA rail employees | "GA OT" in W-2 box 14a and the Georgia RS record field; the tip provision does not apply | US-GAS5-003 |

## ACCESS gaps (exact URLs)
- `https://dor.georgia.gov/withholding-tax` → 404 (2026-11-02).
- `https://dor.georgia.gov/taxes/withholding-tax/withholding-tax-forms-and-information` → 404 (2026-11-02).
- `https://www.ga-newhire.com/faq` → 404; the site redirects to `https://newhire-reporting.com/GA-Newhire/` (read there).
- `https://gov.georgia.gov/document/2016-signed-legislation/sb-255/download` → 404; `https://gov.georgia.gov/document/2017-signed-legislation/sb-201/download` → 404. The enacted garnishment and Family Care Act texts were not located on the Governor's site.
- TY2026 G-1003 Federal Format / CSV / template: not posted at `https://dor.georgia.gov/federal-format-layout` or `https://dor.georgia.gov/documents/withholding-g-1003-tax-template` on 2026-11-02 (Rev 01/18 spec and an undated XLS only).
- The O.C.G.A. text is not available section-by-section on an official host reachable by curl. All statute reads here are from acts or bills on legis.ga.gov.

## Open questions
- **Q1** `reporting.w2.ga.layout.ty2026`: what changed in the TY2026 RS record (GA OT) and in the CSV layout. Closes with the DOR "2026 Federal Format Specifications" and the G-1003 2026 template, expected on dor.georgia.gov from late October 2026. Re-check `https://dor.georgia.gov/federal-format-layout`.
- **Q2** `sui.rate.range` (2026 and 2027): minimum and maximum experience rates. Closes with the text of O.C.G.A. 34-8-155(c) and (e) on an official host, or a GDOL publication of the 2026 and 2027 rate schedules. Tier-B lead only: 0.04–8.10%.
- **Q3** `reporting.ui.efile.threshold`: whether the all-employer electronic DOL-4N mandate (proposed 300-2-2-.02(6)) was adopted, and from when. Closes with the adopted Rule 300-2-2-.02 as filed with the Secretary of State (rules.sos.ga.gov 300-2-2) or the GDOL rules page "amended 2026".
- **Q4** `leave.family_care.status`: the enacted text of 34-1-10 and the status of its sunset (tier-B lead: repealed in 2023). Closes with the enacted Act on legis.ga.gov (SB 201 2017 as passed, and the 2020–2023 extension act).
- **Q5** `garnish.state_tax_levy` and `garnish.creditor.text_enacted`: the DOR wage-levy rules and the enacted 18-4-5 (2016 Act and 2020 SB 443 amendments). Closes with the enacted acts on legis.ga.gov or the Governor's signed-legislation PDFs.
- **Q6** `pit.rate` / `pit.std_deduction` / `pit.dependent` for 2027-01-01. Closes with the OPB determination of 2026-12-01 and the DOR 2027 Employer's Withholding Tax Guide. If no trigger holds: 4.865%, 30,750 / 15,375 and 5,125 (derived).
- **Q7** `privacy.ssn.paystub`: whether O.C.G.A. 10-1-393.8 reaches pay statements. Closes with an official-host read of the enacting act (2006) and of 10-1-393.8 as amended.
- **Q8** `minwage.state.exemptions`: the 34-4-3 text (state 5.15 rate scope). Closes with an official-host read. Low payroll impact, since the federal rate applies to FLSA-covered employers.
- **Q9** `sui.admin_assessment.2027`: no 2026 act extending Article 6 beyond 2026-12-31 was located. Closes with the GDOL 2027 rate release (December 2026), which will show whether the DOL-626 notices carry an assessment.

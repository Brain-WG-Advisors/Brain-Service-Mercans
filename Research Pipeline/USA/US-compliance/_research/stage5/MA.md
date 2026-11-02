# Stage 5 — Massachusetts (MA): 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Mandate block: US-MQ-39 (answered at seal attempt 4).
Budget declared: 60 fetches / 2 h. Used: 44 fetches (curl + 3 web searches), about 1 h 15 min. I stopped acquiring at the 75% mark.
**Access note:** contrary to the 2026-11-01 note, mass.gov answered plain curl with HTTP 200 today (VPN exit Miami US). All mass.gov pages below were saved and read locally; no browser was used. Two official pages still failed (see ACCESS gaps).
Register shard: `00-official-sources/_register-shards/S5-MA.csv` (28 rows, US-MAS5-001..028; 27 active, 1 MANUAL). Sources: `00-official-sources/ccg-sources/MA/` (25 files, 4.2 MB, no file > 5 MB).
Active rows reused, not re-fetched: US-MAP51-003 (Circular M 2026; a fresh download was byte-identical to `pdfs/MA/circularM-2026_wayback-20261018080456.pdf` and was discarded), US-MAP51-005 (c.151A s.14), US-MAP51-008 (c.149 s.148), US-MAP51-009 (c.149 s.26), US-MAR3-001..003, US-MAP7-001/-002, US-MAP9W-001..005, US-MAL-001/-002, US-MAP9M-001.
Rows re-verified with a local file this pass (they had none): US-MAPIT-001 / US-MAP51-001 → US-MAS5-013; US-MAP51-002 → US-MAS5-023; US-MAP51-004 → US-MAS5-022; US-MAP51-006 → US-MAS5-012 (`supersedes` set); US-MAP9W-003 screenshots → US-MAS5-020 (text PDF).

---

## 1. labour_code
- **Minimum wage:** **15.00 USD/h** from 2023-01-01, and never less than 0.50 USD above the federal minimum (7.25 + 0.50 = 7.75, not binding) [US-MAS5-001]. The statute has no indexation. **No 2027 rate is enacted.** The Trial Court Law Library confirms that 2023 was the last step and that any further increase needs the legislature or a ballot vote [US-MAS5-017].
- **Tipped employees (service rate):** **6.75 USD/h** cash wage plus a tip credit up to the full minimum, so the maximum credit is 15.00 − 6.75 = **8.25 USD/h** (derived). The top-up is computed at the end of each shift. The employee must be told about the credit and must keep all tips; pooling among tipped staff is allowed. The rule applies above 20 USD/month in tips [US-MAS5-003].
- **Agricultural workers:** **8.00 USD/h**. This does not apply to children aged 17 or under, or to the employer's immediate family [US-MAS5-004]. Agriculture is also exempt from state overtime [US-MAS5-002].
- **Local minimum wages:** none located. c.151 s.7 lets the *commissioner* set rates by locality, but no local rate was found. Municipalities have no tax power without a General Court grant [US-MAR3-001]. An affirmative statement that no local minimum wage exists was not read (Open question Q6).
- **Overtime:** 1.5× the regular rate above 40 hours per workweek. There is no daily overtime. Commissions, drawing accounts, bonuses and sales/production incentives are excluded from the regular rate. Retail Sunday/holiday hours already paid at 1.5× under c.136 are excluded from the overtime count. Twenty exemption categories apply (e.g. executive/administrative/professional earning more than 80 USD/week, outside sales, seasonal businesses of 120 days or less, fishermen, seamen) [US-MAS5-002].
- **Pay frequency and pay-day timing:** wages are paid weekly or biweekly, within 6 days of the end of the pay period (7 days if the employee works 7 days a week). Casual employees are paid within 7 days. Exempt staff, and salaried staff with a steady weekly schedule, may be paid biweekly or semimonthly, or monthly if the employee chooses. Agricultural workers may be paid monthly. Holiday and vacation pay due under an agreement counts as "wages" [US-MAP51-008].
- **Method of payment (direct deposit / paycard):** not addressed in the s.148 text read. The AG/DLS rule was not located (Open question Q1).
- **Domestic workers (c.149 s.190):** see the special-populations table [US-MAS5-028].
- Confidence: 85% (payment method and local-wage absence still open).

## 2. income_tax
- **Rate:** flat **5.0%**, plus a **4% surtax** on annual income above **1,107,750 USD** (2026). Withholding applies the 9% combined rate above the threshold [US-MAP51-003, US-MAR3-002].
- **Certificate:** **Form M-4**. The federal W-4 is not used for MA exemptions. M-4 lines:
  - line 1, personal exemption: 1, or 2 if aged 65+;
  - line 2, spouse: 4, or 5 if the spouse is 65+;
  - line 3, dependents;
  - line 4, total exemptions;
  - line 5, additional withholding per pay period.

  M-4 boxes:
  - A, head of household;
  - B, blind;
  - C, spouse blind and not subject to withholding;
  - D, full-time student with estimated annual income of **8,000 USD** or less. If D is filled in, the employer **does not withhold**.

  If no M-4 is filed, withhold on zero exemptions. If exemptions decrease, a new M-4 is due within 10 days. Exemptions may be claimed only with the principal employer [US-MAS5-014, US-MAS5-013]. The M-4 edition date is not printed in the extracted text (Q2).
- **Methods:** two methods are allowed, the Circular M wage-bracket tables and the percentage method [US-MAS5-013, US-MAP51-003]. The percentage method works as follows:
  1. Take the period wages.
  2. Subtract FICA, Medicare and MA/US/Railroad retirement contributions, up to **2,000 USD per year**.
  3. Subtract the exemption amount for the pay period:

     | Period | Exemption amount (n = exemptions claimed) |
     |---|---|
     | Daily | 3n + 9 |
     | Weekly | 19n + 66 |
     | Biweekly | 38n + 131 |
     | Semimonthly | 42n + 141 |
     | Monthly | 83n + 284 |
     | Annual | 1,000n + 3,400 |

  4. Multiply by 5%.
  5. Subtract the head-of-household or blind reduction:

     | Period | Head of household | Blind (per person) |
     |---|---|---|
     | Weekly | 2.31 | 2.12 |
     | Biweekly | 4.62 | 4.23 |
     | Semimonthly | 5.00 | 4.58 |
     | Monthly | 10.00 | 9.17 |
     | Daily | 0.33 | 0.30 |

  [US-MAS5-013]
- **G-DERIVE / oracle check:** I re-derived the weekly wage-bracket table in Python (bracket 150–160, midpoint 155, FICA 7.65% = 11.86, exemption = annual factor ÷ 52, × 5%).
  - The results match the table cells exactly: 7.16 / 2.93 / 1.96 / 1.00 for 0–3 exemptions.
  - The percentage method's rounded weekly factor (19n + 66) gives 2.91 and 1.01 instead, a difference of up to 0.02 USD.
  - Conclusion: DOR's two methods are not numerically identical, and both are allowed. The engine must use one method and use it consistently [US-MAS5-024].
- **Supplemental wages:**
  - 5% when annualized regular wages + supplemental payments to date + this payment stay at or under 1,107,750 USD.
  - Above that, the lesser of 9% of the payment or 9% of the excess over the threshold, plus 5% of the remainder.
  - The percentage method excludes supplemental wages [US-MAP51-003].
- **Rounding:** the employer may compute wages to the nearest dollar (830 CMR 62B.2.1(8)) [US-MAS5-023].
- **Residents and nonresidents:**
  - Residents are withheld on all wages, wherever the work is done.
  - Nonresidents are withheld on wages for services performed in MA.
  - A nonresident who does not work in MA is not withheld, even if paid from an MA office.
  - An employer with no MA office or business may withhold for MA residents as a courtesy, on request [US-MAS5-013, US-MAS5-023].
- **Reciprocity:** none located. For an MA resident whose wages are also withheld by another state (or DC, a territory, Canada or a province), MA withholding = the MA amount minus the other jurisdiction's amount (credit method, 830 CMR 62B.2.1(9)(b)) [US-MAS5-023]. A non-MA employer with an MA office withholds the MA amount minus its own state's amount [US-MAS5-013].
- **When there is no federal withholding duty:**
  - No MA withholding is required. Household employers are generally not required to withhold, though they may.
  - MSRRA spouses who file Form M-4-MS: do not withhold [US-MAS5-013, US-MAS5-024].
- **Local income taxes:** none. Cities and towns have no taxing power without a General Court grant, and DOR's tax-rate list shows no local wage tax [US-MAR3-001, US-MAR3-002, US-MAR3-003].
- Confidence: 95%.

## 3. social_security (UI, PFML, levies)
- **SUI (DUA):**
  - Taxable wage base **15,000 USD**, fixed by statute and not indexed [US-MAP51-005].
  - 2026 rates: new employers (under 3 years) **2.42%**; new construction employers **6.08%**. Established employers use **Schedule E**, from 0.94% to 14.37%.
  - There is **no employee UI contribution**: the employer contribution pages read describe only employer contributions [US-MAS5-022].
  - Liability thresholds:
    - 1 employee for 13 weeks, or 1,500 USD in wages in a quarter;
    - agricultural: 40,000 USD in a quarter, or 10 employees for 20 weeks;
    - domestic: 1,000 USD in cash wages in a quarter;
    - out-of-state employers: 200 USD of MA wages in a quarter.
  - Rate notices are issued by Jan 31. Rate reviews must be requested before Jun 20. Up to 34% of Q1–Q2 contributions may be deferred. Late payments carry 12% interest [US-MAS5-022].
- **COVID-19 Recovery Assessment (employer, experience-rated only):** **0.178% to 2.716%** in 2026, on the same 15,000 USD base. The effective combined rate runs from 1.118% to 17.086%. In every band, UI + COVID = effective rate (checked in Python) [US-MAS5-020, US-MAP9W-002].
- **EMAC (employer):**

  | Years subject to UI | EMAC rate |
  |---|---|
  | Years 1–3 | Exempt |
  | Year 4 | **0.12%** |
  | Year 5 | **0.24%** |
  | Year 6 and later | **0.34%** |

  EMAC applies to the first 15,000 USD of each employee's wages. Employers with fewer than 6 employees in a quarter are exempt [US-MAS5-021]. This closes the P7 gap on US-MAP7-002.
- **Workforce Training Fund (employer):** 0.056% on the 15,000 USD base under c.151A s.14L [US-MAP7-001]. The 2026 DUA-published value was not read (Q7).
- **PFML (DFML):**

  | Year / employer size | Family leave | Medical leave | Total |
  |---|---|---|---|
  | 2026, 25+ covered individuals | 0.18% (up to 100% withheld from the employee) | 0.70% (employee up to 40% = 0.28%; employer 0.42%) | **0.88%** |
  | 2026, fewer than 25 | 0.18% | 0.28% (no employer share) | **0.46%** |
  | 2027 (Chapter 101 of the Acts of 2026), 25+ | **0.70%** (employee up to 40% = 0.28%; employer 0.42%) | **0.18%** (up to 100% from the employee) | still **0.88%** |
  | 2027, fewer than 25 | — | — | 0.46% |

  - The 2027 totals were derived in Python.
  - The contribution cap is the Social Security wage base (c.175M s.6(f)) [US-MAS5-012, US-MAS5-010].
  - The PFML maximum weekly benefit (benefit side) is **1,230.39 USD** in 2026 and **1,284.61 USD** in 2027. Each equals 64% of the SAWW (1,922.48 and 2,007.20), re-derived exactly [US-MAS5-025, US-MAS5-011].
- **SDI/TDI:** none in MA. PFML is the only employee-funded leave program, and the DOR business-tax list shows no other wage-based levy [US-MAP9W-004].
- Confidence: 92% (WTF 2026 value; Chapter 101 timing conflict, see §13).

## 4. payslip_statute
- **Content:** each pay must come with a pay slip, check stub or envelope showing the employer name, employee name, date (day/month/year), hours worked, hourly rate, and the deductions or increases for the period (c.149 s.148) [US-MAP51-008]. There is no language clause; payslips are in English (US-OWN-006) [US-MAL-001].
- **Delivery and electronic consent:** not addressed in the s.148 text. The AG rule on electronic pay stubs was not located (Q1).
- **Retention:** 3 years for payroll records (c.151 s.15) [US-MAS5-005] and 3 years for withholding records (DOR) [US-MAS5-013]. Domestic-worker paystubs: 3 years [US-MAS5-028].
- Confidence: 80%.

## 5. reporting_instruments
- **Registration:** MassTaxConnect (DOR) for withholding and PFML; Unemployment Services for Employers (DUA) for UI [US-MAS5-013, US-MAS5-018].
- **Withholding return (Form M-941 / MassTaxConnect)**, by annual withholding amount:

  | Annual withholding | Filing and payment |
  |---|---|
  | 100 USD or less | Annual, due Jan 31 |
  | 101–1,200 USD | Quarterly: Apr 30 / Jul 31 / Oct 31 / Jan 31 |
  | 1,201–25,000 USD | Monthly, by the 15th; the March, June, September and December payments are due on the last day of the following month |
  | More than 25,000 USD | Quarterly return, plus payment within 3 business days whenever 500 USD or more has accumulated by the 7th, 15th, 22nd or last day of the month |

  - E-filing is mandatory for new registrations, payroll service providers, and combined liability of 5,000 USD or more [US-MAS5-013].
- **Annual W-2 to DOR:**
  - Due **by Jan 31** (to the employee, SSA and DOR).
  - 50 or more W-2s must be uploaded electronically through MassTaxConnect or the Bulk File Portal.
  - 49 or fewer may be filed on paper, with **Form M-3**.
  - Corrections are filed on paper only, on federal W-2c [US-MAS5-015].
- **W-2 file format:**
  - SSA EFW2 with RA/RE/RS/RT records.
  - In the RS record, MA wages are at positions 276–286 and MA withholding at 287–297.
  - The RT record must equal the sum of the RS records (DOR reconciles).
  - PDF and CSV are not accepted [US-MAS5-019].
  - **The handbook served is Rev. 20191219**, even though it says it is reissued every year (Q3).
  - **Deadline conflict:** the Withholding Tax Guide (posted Aug 2026) says 50+ employers file by "the last day of March" and paper filers file W-2 + M-3/M-3M by Feb 28 [US-MAS5-013]. The W-2 page (updated 2026-01-30) and the handbook say **Jan 31** [US-MAS5-015, US-MAS5-019]. I recommend Jan 31 (more specific page, aligned with IRS) (Q4).
- **Quarterly wage detail report (DUA):**
  - Due by 3 p.m. on Apr 30 / Jul 31 / Oct 31 / Jan 31.
  - Formats: **CSV, EFW2 or ICESA** upload.
  - Fields: EAN; SSN; full name; hours worked; gross wages; wages subject to withholding; state income tax withheld; work location; 12th-of-month employment; adjustment reason code.
  - Wages are reported when paid [US-MAS5-018].
  - DOR's guide also says "file quarterly wage reports". The DUA report carries the withholding field, so it appears to be the single quarterly wage report. That is not confirmed (Q5).
- **New-hire reporting (DOR Child Support Services):**
  - Due **within 14 days** of the first day of work, for employees and for contractors (600 USD+). Rehires after 30+ days off the payroll are also reported.
  - Fields: FEIN, legal name and payroll address; employee full name, address, employee/contractor status, SSN (no ITIN) and start date.
  - Employers with 25 or more employees must file online (MassTaxConnect, individual or batch text file per the New Hire Record Layout). Smaller employers may use Form NHR by mail or fax.
  - Multistate employers may report everything to MA after registering with OCSE [US-MAS5-016, US-MAS5-008].
  - Note: DOR's guide says "within 2 weeks", which matches the 14 days.
- **PFML return:** filed quarterly in MassTaxConnect; the page that fixes it was not read (Q8).
- **Prevailing wage:** certified payroll is submitted weekly (see §10).
- Confidence: 85%.

## 6. leave
- **Earned sick time (c.149 s.148C):**
  - Accrual of 1 hour per 30 hours worked, usable from day 90.
  - Exempt employees are deemed to work 40 hours a week.
  - Employers with **11 or more employees** give up to **40 hours paid** per year, at the same hourly rate and never below the minimum wage; smaller employers give 40 hours unpaid.
  - Up to 40 hours carry over, but no more than 40 hours may be used in a year.
  - **No payout at separation.**
  - Certification may be required after 24 consecutive scheduled hours of absence.
  - Pregnancy loss is a covered purpose [US-MAS5-006].
- **PFML benefit side:**
  - 7-day waiting period, which the employer's PTO may cover.
  - Benefit is 80% of AWW up to 50% of the SAWW, plus 50% above that, capped at 64% of the SAWW.
  - Annual caps: 20 weeks medical, 12 weeks family, 26 weeks combined.
  - DFML pays the benefit, with optional 5% state / 10% federal withholding. **Benefits do not flow through the employer's payroll** [US-MAS5-011, US-MAS5-025].
  - Note: the Chapter 101 split change was made "to mitigate the impact of recent IRS guidance on the tax treatment of PFML benefits" [US-MAS5-012].
- **Other mandated leave:** not read in this pass: parental leave (c.149 s.105D), small necessities leave (c.149 s.52D), domestic violence leave (c.149 s.52E), jury duty (Q9).
- Confidence: 75%.

## 7. termination
- **Final pay:** an employee who is **discharged** is paid in full **on the day of discharge**. An employee who **resigns** is paid on the next regular payday (or the following Saturday if there is no regular payday) [US-MAP51-008].
- **Vacation:** holiday and vacation payments due under an agreement are "wages" under s.148, so they are payable at termination [US-MAP51-008].
- **Sick time:** no payout [US-MAS5-006].
- **UI separation notice:** the DUA instrument (form number and 430 CMR section) was **not located**. The 430 CMR 5.00 page is an index that links only to a PDF (dated 2010-06-11) (Q10).
- **State WARN-type law:** not researched in this pass (not payroll-relevant unless severance applies).
- Confidence: 70%.

## 8. benefits_in_kind
- **Conformity:**
  - MA follows the Internal Revenue Code as defined in c.62 s.1. **From 2026, c.62C s.90** (Chapter 101 of the Acts of 2026, s.13) decouples MA from any individual IRC amendment in the year it is enacted and in earlier years. A new federal exclusion therefore does not reach MA wages in its enactment year unless the legislature adopts it [US-MAS5-026].
  - Withholding deducts FICA/Medicare/retirement contributions up to 2,000 USD per year [US-MAS5-013].
  - Business expenses reimbursed under an accountable plan are not wages [US-MAS5-013].
- **Item-by-item departures** (401(k), §125, HSA, transit, group-term life) were not read in a DOR source this pass (Q11).
- Domestic workers: meal and lodging deduction caps (see the special-populations table) [US-MAS5-028].
- Confidence: 55%.

## 9. deductions_garnishments
- **Creditor wage attachment (c.246 s.28):**
  - Exempt each week: the greater of **85% of gross wages** or **50 × the higher of the federal or MA minimum wage** = 50 × 15.00 = **750 USD/week** (derived). This is more protective than the CCPA's 25%.
  - For support, alimony and separate-maintenance orders, the federal CCPA limits apply instead [US-MAS5-009].
- **Child support IWO:** DOR Child Support Services receives new-hire reports [US-MAS5-016]. The MA IWO specifics (fees, priority) were not read (Q12).
- **Wage-deduction authorization (c.149 s.150 / AG rules):** not read (Q12).
- Confidence: 65%.

## 10. collective_agreements (prevailing wage)
- **Public works:** wages must be at least the rate set by the commissioner (c.149 s.26) [US-MAP51-009].
- **Certified payroll:**
  - submitted **weekly** to the awarding authority, with a signed statement;
  - a copy of each apprentice's ID is attached each week;
  - records are kept for 3 years after the contract ends;
  - a statement of compliance is filed within 15 days after the work is completed.
  - s.27B sets no dollar threshold [US-MAS5-007].
- Confidence: 85%.

## 11. indexation

| Item | Indexed? | Mechanism / where the new value is published |
|---|---|---|
| Minimum wage 15.00 | No | Statute only [US-MAS5-001, US-MAS5-017] |
| UI wage base 15,000 | No | c.151A s.14 [US-MAP51-005] |
| UI / COVID RA rates | Annually | DUA rate schedule; notice to the employer by Jan 31 [US-MAS5-020, US-MAS5-022] |
| PFML rates | Annually (Jan 1) | c.175M s.7(e); DFML rate page [US-MAS5-010, US-MAS5-012] |
| PFML contribution cap | Yes (federal) | Social Security wage base [US-MAS5-010] |
| PFML maximum weekly benefit | Yes | 64% × SAWW, set by Oct 1, effective Jan 1; 2027: 2,007.20 × 0.64 = 1,284.61 (derived) [US-MAS5-011, US-MAS5-025] |
| Surtax threshold | Yes | 1,107,750 (2026), published in Circular M [US-MAP51-003]; the mechanism (CPI) was not re-read |
| M-4 exemption factors | No | Static since at least the 2026 tables [US-MAS5-013] |

## 12. data_protection
- **Payroll records:** 3-year retention; employees may inspect their own records (c.151 s.15) [US-MAS5-005].
- **SSN on pay statements:** no MA rule was located in this pass. Neither the s.148 content list nor the DOR guide requires or forbids the SSN on the slip [US-MAP51-008, US-MAS5-013]. MGL c.93H / 201 CMR 17.00 (written information security program) were not read (Q13).
- Confidence: 50%.

## 13. live_legal_change (2026-01-01 → 2026-11-02)
- **Chapter 101 of the Acts of 2026** (H.5470, FY2026 supplemental budget, emergency law, **approved 2026-06-12, in force**) [US-MAS5-026]:
  - **ss.25–26 (PFML split):** the employee-deduction caps are swapped (medical 40% → 100%, family 100% → 40%). DFML implements the swap **from 2027-01-01** [US-MAS5-012].
    - Operating level: employer payroll withholding.
    - **Conflict:** s.45 says ss.25–26 apply "for taxable years beginning on or after January 1, 2026". For 2026 payroll, follow DFML's 2026 table (Q14).
  - **s.13, new c.62C s.90:** same-year IRC amendments do not affect MA gross income (from TY2026, s.45). Operating level: definition of MA wages and income (assessment, which flows into withholding).
  - **s.8:** adds a deduction for Pub. L. 119-21 s.70302(f). Its subject matter was not checked; deductions on the return do not affect withholding unless DOR says so (Q15).
- **Initiative Petition 25-18** (rate 5% → 4.67% for 2027, then 4.33% and 4%) [US-MAS5-027, **MANUAL, tier B**]:
  - Secondary sources report that the SJC (**Finfer v. Attorney General, SJC-13885**, art. 48, judgment 2026-06-18) **excluded it from the 2026-11-03 ballot**.
  - Enactment status: not on the ballot, not enacted.
  - Consequence: the 2027 rate stays **5.0% + 4% surtax** unless the General Court acts.
  - The official opinion URL returned 404 (ACCESS gap). **Do not model 4.67%.**
- **PFML 2027 figures** published by DFML (2026-10-01 / 2026-10-09): rates as in §3, maximum benefit 1,284.61 [US-MAS5-012, US-MAS5-025].
- **830 CMR 62B.2.1** page dated 2026-06-05 [US-MAS5-023].
- **Not done:** a systematic sweep of the 2026 DOR TIRs/Directives and the DUA/DLS news. Only these targeted items were checked (Q16).
- Confidence: 70%.

---

## Special populations (state level, US-OWN-005)

| Population | MA rule | register_id |
|---|---|---|
| Domestic/household workers | Minimum wage and overtime apply (incl. au pairs). Written agreement for 16+ h/week; timesheet every 2 weeks; 24 h/48 h rest rules; meal deductions max 1.50 / 2.25; lodging max 35 / 30 / 25 USD per week. UI coverage at 1,000 USD cash wages per quarter. Income-tax withholding not required (optional) | US-MAS5-028, US-MAS5-022, US-MAS5-013 |
| Agricultural | Minimum wage 8.00 (not family or under-18s); exempt from state overtime; may be paid monthly; UI at 40,000 USD per quarter or 10 workers for 20 weeks | US-MAS5-004, US-MAS5-002, US-MAP51-008, US-MAS5-022 |
| Minors | Minimum wage applies (no youth rate in c.151 s.1). Exempt from agricultural minimum wage if 17 or under. UI-exempt when working for a parent. Child-labor hours/permits not read (Q17) | US-MAS5-001, US-MAS5-004, US-MAS5-022 |
| Tipped employees | Service rate 6.75 + tip credit up to 15.00 (8.25 max), reconciled per shift; tips count toward withholding (tips of 20 USD/month or more reported to the employer by the 10th) | US-MAS5-003, US-MAS5-013 |
| Clergy/religious | Members of religious orders are excluded from minimum wage (law library). Work for some religious organizations is UI-exempt. Religious organizations must still withhold | US-MAS5-017, US-MAS5-022, US-MAS5-013 |
| Students | M-4 box D: full-time student, seasonal/part-time/temporary work, income of 8,000 USD or less → no MA withholding. Work-training in nonprofit/public institutions is UI-exempt | US-MAS5-014, US-MAS5-024, US-MAS5-022 |
| Nonresident aliens | No MA-specific rule read. MA withholding follows the federal duty ("if no federal withholding requirement, no MA withholding") | US-MAS5-013 |
| Military spouses (MSRRA) | Form M-4-MS → do not withhold | US-MAS5-024 |
| Statutory employees | No state rule beyond federal located (the DOR guide was read in full) | US-MAS5-013 |
| Government employees | Governmental entities must withhold and report new hires. Municipal employees are excluded from c.151 minimum wage (federal minimum applies). Cities and towns are covered by earned sick time only if they accept it locally. Governmental employers are exempt from the COVID RA | US-MAS5-013, US-MAS5-008, US-MAS5-017, US-MAS5-006, US-MAP9W-002 |
| Interstate motor/rail carriers | Withhold for MA residents, and for nonresidents who perform all their regularly assigned duties in MA | US-MAS5-013 |
| Family employment | UI-exempt: children under 18 working for a parent, spouses, parents working for their children | US-MAS5-022 |

---

## ACCESS gaps (exact URLs)
1. `https://www.mass.gov/doc/finfer-v-attorney-general-sjc-p13885/download`: HTTP 404 (2026-11-02). This is the SJC opinion on Initiative Petition 25-18.
2. `https://www.sec.state.ma.us/divisions/elections/research-and-statistics/2026-Information-for-voters/2026-ballot-question5.htm`: HTTP 302 redirect loop, 0 bytes (2026-11-02). This is the Secretary of the Commonwealth's 2026 ballot questions page.
3. `https://www.mass.gov/info-details/how-pfml-weekly-benefit-amounts-are-calculated-andor-reduced`, `https://www.mass.gov/info-details/new-hire-reporting`, `https://www.mass.gov/info-details/massachusetts-law-about-wages-and-salary`: HTTP 404 (guessed URLs; the replacements used are in the register).
4. `https://www.mass.gov/regulations/430-CMR-500-employer-requirement-series`: an index page only. The regulation text is a PDF that was not fetched (budget). Needed for Q10.
5. Not fetched because of the budget, URLs known: `https://www.mass.gov/info-details/new-hire-record-layout` (new-hire file layout), `https://www.mass.gov/doc/form-m-3-reconciliation-of-massachusetts-income-taxes-withheld-for-employers/download`, and the DUA "Massachusetts UI tax rate schedules, A-G" PDF linked from the employer-contributions page.

## Open questions
- **Q1:** Direct deposit, paycard and electronic pay-stub consent rules (AG Fair Labor Division advisory / 454 CMR 27). *Would close it:* the AG's wage-payment advisory or 454 CMR 27.00 text.
- **Q2:** Form M-4 revision date. *Would close it:* the form footer, or DOR's withholding forms list (`/lists/withholding-tax-forms`).
- **Q3:** W-2 e-file handbook served as Rev. 20191219, although it states it is reissued every tax year. *Would close it:* a TY2026 edition from DOR bulk-file support (bulkfilesupport@dor.state.ma.us).
- **Q4:** Deadline conflict for filing W-2s with DOR: Jan 31 [US-MAS5-015, US-MAS5-019] vs "last day of March" / Feb 28 [US-MAS5-013]. *Would close it:* the DOR Directive or TIR fixing the W-2/M-3 due date (Directives 97-1, 07-2 and 09-8 are cited in the handbook).
- **Q5:** Whether the DUA quarterly employment and wage detail report is the only quarterly wage report (DOR's guide still mentions DOR quarterly wage reports). *Would close it:* the DOR "File quarterly wage reports" page.
- **Q6:** An affirmative statement that no local minimum wage exists in MA. *Would close it:* a DLS/AG page or the c.151 s.7 commissioner orders.
- **Q7:** Workforce Training Fund 2026 rate as published by DUA (statute 0.056% may be adjusted). *Would close it:* the DUA WTF page, or 430 CMR 14.00.
- **Q8:** PFML quarterly return mechanics (MassTaxConnect form, due dates, fields). *Would close it:* the DFML page "Wage contributions & reporting for PFML".
- **Q9:** Other leaves with a pay impact (c.149 ss.52D, 52E, 105D; jury duty c.234A s.48). *Would close it:* the statute texts on malegislature.gov.
- **Q10:** UI separation notice to departing employees (form and rule). *Would close it:* the 430 CMR 4.00/5.00 PDF text, or the DUA employer guide.
- **Q11:** MA conformity, item by item, for 401(k)/403(b) deferrals, §125, HSA, transit and group-term life in MA wages. *Would close it:* DOR's "Massachusetts tax treatment of fringe benefits" guidance, or TIRs.
- **Q12:** Wage-deduction authorization (c.149 s.150, AG rules); MA IWO fees and priority. *Would close it:* the c.149 s.150 text and the DOR Child Support Services employer page.
- **Q13:** Rules on SSN on pay statements / payroll-data security. *Would close it:* the MGL c.93H and 201 CMR 17.00 texts.
- **Q14:** Effective date of the PFML split swap: Chapter 101 s.45 ("taxable years beginning on or after January 1, 2026") vs DFML (2027-01-01). *Would close it:* a DFML/DOR notice or regulation (458 CMR 2.00) on transition. For now the build should use DFML: 2026 split unchanged, 2027 swapped.
- **Q15:** Subject matter of the Pub. L. 119-21 s.70302(f) deduction adopted by Chapter 101 s.8, and whether it affects withholding. *Would close it:* the DOR TIR implementing Chapter 101.
- **Q16:** Full 2026 bulletin sweep (DOR TIRs/Directives, DUA and DFML news) is not done. *Would close it:* the DOR TIR index for 2026 and the DFML/DUA news pages (orchestrator pass).
- **Q17:** Minors: work permits and hour limits (c.149 ss.60–62, 65–66) — not payroll-calculation-critical. *Would close it:* the statute text.
- **Q18:** Initiative Petition 25-18 status rests on tier-B sources (US-MAS5-027 MANUAL). *Would close it:* the SJC opinion SJC-13885 from mass.gov/sjc or the SJC docket, or the Secretary of the Commonwealth's list of 2026 ballot questions.

**Parallelisable remainder:** Q1/Q12/Q13 (AG and DOR guidance pages), Q7/Q8/Q10 (DUA/DFML pages) and Q9/Q17 (statutes) are independent lookups, about 12 fetches. Q14/Q15/Q16 are a single DOR TIR/DFML notice sweep.

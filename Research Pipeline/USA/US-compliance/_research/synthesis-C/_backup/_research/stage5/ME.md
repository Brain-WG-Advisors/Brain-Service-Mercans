# Stage 5 — Maine (ME): 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Mandate block: US-MQ-41 (answered at seal attempt 5).
Budget declared: 60 fetches / 2 h. Used: about 45 fetches (39 curl, 3 Wayback PDFs, 3 web searches used as leads only). I stopped acquiring at the 75% mark.

**Access note.** The VPN was OFF (exit IP in Brazil). maine.gov answered HTTP 403 (CloudFront geo-block) to plain curl. legislature.maine.gov answered 200. All maine.gov documents below come from `web.archive.org/web/2026id_/` copies and were read locally. No browser was used.

Register shard: `00-official-sources/_register-shards/S5-ME.csv`: 28 rows, US-MES5-001..028, all `active`. Sources are in `00-official-sources/ccg-sources/ME/` (34 files, 1.5 MB, no file over 5 MB).

**Active rows reused, not re-fetched:**
- US-ME-P5-2-001 / -002 / -003 / -004 / -005 / -009 (withholding booklet, FAQ, nonresident rules, credit, reciprocity);
- US-ME-P5-1-001 (2026 UI rate array);
- US-MEP6-001 (PFML FAQ);
- US-MEP7-001 / -002 (CSSF/UPAF);
- US-MER3-001 / -002 (no local tax);
- US-MEP9V-001, US-MEP9L-001.

**Re-read without a new fetch:** the local booklet and the PFML FAQ were re-read. Their extra content is carried in US-MES5-011 and US-MES5-025.

**Register corrections to merge:**
- **US-MES5-006** (26 MRSA 665(1)) reverses the "no pay-statement duty" finding in US-ME-P5-1-004 and US-ME-P5-2-006. Maine DOES require a pay statement. Its `supersedes` points at US-ME-P5-2-006. The synthesis should mark that row superseded and re-check every `consumed_by` of US-ME-P5-1-004 / -2-006: the MANDATE US-MQ-41 part 6 text and OWN-006 ("state pay-statement statutes fix content").
- **US-MES5-024** supersedes US-ME-P5-1-002. It is the same statute, now with a local file and full text.
- **US-ME-P5-2-001** says "basic standard deduction single 15,300 / married 30,600". Those are the return-level figures. Withholding uses **12,450 / 27,750** (US-MES5-011). A builder must use the withholding figures.

---

## 1. labour_code
- **State minimum wage:**
  - **15.10 USD/h** from 2026-01-01, agricultural and non-agricultural [US-MES5-002].
  - **15.70 USD/h** from 2027-01-01. The 2027 poster (rev. 9/26) shows it as already published [US-MES5-003].
  - Indexation: each 1 January by the Aug-to-Aug change in CPI-W Northeast, rounded to 0.05. The State rate follows any higher federal rate [US-MES5-001].
  - G-DERIVE: the CPI-W values were not fetched, so the 15.10 → 15.70 step (+3.97%) is not reproduced (see Q3).
- **Local minimum wage, Portland** [US-MES5-012]:
  - Applies to hours worked within city limits.
  - **16.75** from 2026-01-01 (City employees from 2026-07-01), **17.75** from 2027-01-01, **19.00** from 2028-01-01. CPI-U Northeast indexation from 2029.
  - Tip credit at most half the city rate.
  - Work during a declared emergency is paid at 1.5× the minimum.
  - Other municipalities (e.g. Rockland) were not checked (Q4).
  - The State does not preempt local minimum wages: the ordinance cites 26 MRSA 664 and 30-A MRSA 3001. Earned paid leave, by contrast, is expressly preempted (637(9)).
- **Tip credit (State):**
  - Credit at most 50% of the minimum, so the cash wage is at least **7.55** in 2026 (derived: 15.10 × 0.5).
  - The six advance-notice items (A–F) apply.
  - Shortfall is checked over the 7-day workweek.
  - Tips charged to a card are paid by the next regular payday, with no card-fee deduction.
  - Tip pooling is allowed under 664(2-A) [US-MES5-001].
- **Overtime** [US-MES5-001, US-MES5-005]:
  - 1.5× the regular rate above 40 hours per week. There is no daily overtime.
  - The regular rate includes bonuses and commissions; FLSA 207(e) exclusions apply.
  - Exempt groups: auto sales/service staff, mariners, public employees other than State executive/judicial, and the listed agricultural/fish processing.
  - **Salaried-exempt threshold:** annualised pay must exceed 3,000 × the State minimum, or the FLSA level if higher. The poster gives **871.16 USD/week** for 2026 (3,000 × 15.10 / 52 = 871.1538, so 871.16 is the first cent above). For 2027 the poster gives **905.79 USD/week**, but 3,000 × 15.70 / 52 = 905.769, i.e. 905.77. The poster is 0.02 USD off (Q2).
- **Pay frequency and timing** [US-MES5-004]:
  - Pay intervals may not exceed 16 days.
  - Each payment covers wages earned to within 8 days of payday.
  - A payday falling on a closed day moves to the next business day.
  - The established payday must be made known to employees; lengthening the interval needs 30 days' written notice.
  - A rate decrease needs prior notice.
- **Method of payment:** no fee may be charged for direct deposit (621-A(7)). The statute read has no consent or paycard rule (Q5).
- **Pay transparency (622-A):** not read; it is a hiring/posting rule, not payroll.
- Confidence: 90%.

## 2. income_tax
- **Method:** percentage method or tables, 2026 booklet (revised Dec 2025) [US-ME-P5-2-001, US-MES5-011]:
  1. Annualise the wages (factors 52 / 26 / 24 / 12 / 260).
  2. Subtract **5,300 per W-4ME allowance**.
  3. Subtract the withholding standard deduction:
     - **12,450** single if wages are at or below 102,250; reduced linearly as 12,450 × (177,250 − W) / 75,000; zero from 177,250.
     - **27,750** married if wages are at or below 204,550; reduced as 27,750 × (354,550 − W) / 150,000; zero from 354,550.
  4. Apply the schedule:
     - Single: 5.80% below 27,400; 1,589 + 6.75% to 64,850; 4,117 + 7.15% above.
     - Married: 5.80% below 54,850; 3,181 + 6.75% to 129,750; 8,237 + 7.15% above.
  5. Divide by the pay periods and **round to the nearest dollar**.
- **Bracket bases** (derived): 27,400 × 5.8% = 1,589.2; 1,589 + 37,450 × 6.75% = 4,116.875; married 3,181.3 and 8,236.75. All are consistent.
- **Oracle:** booklet Examples 1–3 reproduced in Python as **0 / 33 / 257 USD per week**, all matching [US-MES5-011]. There is no official calculator [US-ME-P5-2-009].
- **Form W-4ME:**
  - Required. Without a valid one, withhold as single with zero allowances.
  - Claiming more allowances needs an MRS Allowance Variance Certificate.
  - Send a copy to MRS when the IRS demands the federal W-4, or when a non-Maine-address employee claims exempt and expects 5,000 USD or more of Maine-source pay.
  - Do not reduce Maine withholding for federal W-4 Step 4(b) deductions [US-MES5-011].
- **Supplemental wages:** aggregated with regular wages, or a flat **5%** when paid separately. Backup withholding is also 5% [US-ME-P5-2-001, US-MES5-011].
- **Local income tax:** none. Title 36 has none and the withholding chapter has no local limb [US-MER3-001, US-MER3-002].
- **Nonresidents:**
  - Taxable only if present in Maine **more than 12 days AND earning more than 3,000 USD** of Maine-source pay in the year. Training, inspection, R&D and project-team days are excluded from the count [US-ME-P5-2-003].
  - Residents get a credit for tax paid to other jurisdictions [US-ME-P5-2-004].
  - No reciprocity agreement is in force; the statute only authorises one [US-ME-P5-2-005].
- **Indexation:** brackets, standard deduction and phase-outs are indexed by chained CPI around 15 September each year [US-MES5-019].
- Confidence: 95%.

## 3. social_security
- **SUI rates (2026)** [US-ME-P5-1-001, US-MES5-020, US-MES5-021]:
  - Taxable wage base **12,000 USD**. It is fixed in statute, not indexed.
  - New employer: **2.23% UI + 0.14% CSSF + 0.17% UPAF = 2.54%**.
  - Experience categories 01–20: **0.31%–6.60% combined**.
  - Employer-only; there is no employee contribution.
  - Reimbursable employers are exempt from CSSF and UPAF.
- **MULTI-OQ-2 (answered for ME):** wages paid by the same legal entity in **any other State** count toward the 12,000 base, and so do predecessor wages (26 MRSA 1043(19)) [US-MES5-020].
- **UPAF conflict.** The rate-year 2026 array gives **0.17%**; the 2026 UC-1 instructions print **0.16%** [US-MES5-021]. The statute sets UPAF as a computed yield, 0.04% × (total ÷ taxable wages), rounded to 0.01% [US-MES5-022]. That makes it rate-year specific, and the employer-specific array is the stronger source. **Use 0.17%** (confidence 80%, Q1).
- **PFML premiums** [US-MES5-024, US-MEP6-001, US-MES5-025]:
  - Combined premium of at most 1.0% of wages from 2025-01-01. For 2025–2027 the FAQ sets **1.0%** (15+ employees) or **0.5%** (fewer than 15).
    - 15+ employees: the employee pays at most 0.5% and the employer remits 1.0%.
    - Under 15: the employer remits 0.5% and may deduct all of it from wages.
  - From 2028 the department sets the rate annually by 1 October.
  - Wage cap = the SSA wage base.
  - Reported and paid quarterly in the PFML portal (separate from UC-1).
  - The employee share is deducted **after tax**: it does not reduce taxable wages.
  - Employer-paid employee share counts as taxable wages.
  - W-2 Box 14 label **"MEPFML"**.
  - Late penalty: 1% of quarterly payroll.
- **G-NUMBER residual:** the 1% / 0.5% split rests on the A.3 FAQ plus the A.1 statute structure. No A.2 rate table exists (Q6).
- **MULTI-OQ-3 (answered for ME):** PFML follows the Maine UI localization test (FAQ 6) [US-MES5-025].
- **No SDI/TDI, no transit levy, no other levy** [US-MEP9V-001, US-OWN-007].
- Confidence: 88%.

## 4. payslip_statute
- **Required pay statement (corrects earlier rows)** [US-MES5-006, US-MES5-002]:
  - Furnished with each payment of wages.
  - Must show the **date of the pay period, hours, total earnings and itemized deductions**.
- **Direct deposit / electronic transfer:**
  - The same record must be provided when the transfer is made.
  - Electronic delivery is allowed only if the employee has ready access and can **print at no cost**.
  - There is no express opt-in consent rule.
- **Records** [US-MES5-006, US-MES5-026]:
  - Hours and wages kept for **at least 3 years** (665(1)).
  - Date and amount paid, plus daily time records except for salaried exempt staff (622).
- **Tip credit:** the employer must be able to show the minimum was met; there is no extra payslip line in the statute.
- **Language:** none required [US-MEL-001, US-MEP9L-001].
- **SSN:** no truncation rule located (see section 12).
- **MULTI-OQ-8 (pay-statement reach to out-of-state work):** no reach rule in 665. Default: employees working in Maine.
- Confidence: 90%.

## 5. reporting_instruments
- **Form 941ME (withholding)** [US-ME-P5-2-002, US-MES5-011]:
  - Quarterly, due the last day of the month after the quarter.
  - Electronic filing is mandatory (Rule 104), even when there is nothing to report.
  - Deposits are **semiweekly** if look-back withholding is 18,000 USD or more, otherwise quarterly with the return. Semiweekly payments must be electronic, and electronic payment is also required when total Maine tax liability is 10,000 USD or more (Rule 102).
  - The 900ME voucher is used for payments.
  - There is no annual W-3ME reconciliation after tax year 2023 [US-ME-P5-2-009].
- **State W-2 / 1099:**
  - Filed **electronically with MRS by 31 January**; paper is not accepted.
  - Format: the "Maine Tax Portal Bulk File Upload Specifications". That document was not fetched, so whether EFW2 is accepted is open (Q7).
  - Penalty: 50 USD per missing statement [US-MES5-011].
- **ME UC-1 (UI):**
  - Quarterly, due the last day of the month after the quarter.
  - Filed in ReEmployME (file-format spec published) or on paper.
  - Includes monthly employment for the payroll period that includes the 12th, gross / excess / taxable wages, UC rate, CSSF and UPAF.
  - Interest 10% from 2026-01-01; late penalties as for 941ME [US-MES5-021].
  - The UC-1 is filed with MRS [US-ME-P5-2-009].
- **PFML:** quarterly wage report and premium in the PFML portal [US-MES5-024, US-MES5-025].
- **New-hire reporting** [US-MES5-016]:
  - To DHHS **within 7 days** of first services; Maine is stricter than the federal 20 days.
  - Covers new hires and rehires after 60 or more days' separation.
  - Fields: employee name, address, SSN, date of birth and start date; employer name, address and UI/UBI number.
  - Independent contractors expected to earn 2,500 USD or more are also reported within 7 days.
- **Registration:**
  - An out-of-state employer with an office in Maine, or transacting business there, must withhold [US-ME-P5-2-002].
  - Payroll processors must hold a Bureau of Consumer Credit Protection licence [US-MES5-011].
- **POA:** Form 2848-ME for withholding [US-ME-P5-1-004]. The UI form UC-28 row is MANUAL: its edition is 09/2013, not 2018 [US-ME-P5-2-008].
- Confidence: 85%.

## 6. leave
- **Earned paid leave (26 MRSA 637)** [US-MES5-008]:
  - Applies to employers with **more than 10 employees** for more than 120 days in the year.
  - Accrual: **1 hour per 40 hours worked**, up to **40 hours per year**, usable for any purpose.
  - Use may be deferred until 120 days of service.
  - Carry-over is required. PL 2025 c.438 adds that carry-over does not reduce the next year's accrual, up to 40 hours or the policy cap.
  - Paid at the base rate.
  - Seasonal industries are excluded; local ordinances are preempted.
  - No payout-on-separation clause.
- **Payout on separation:** earned paid leave counts as paid vacation under 626 if the employer policy treats it as vacation. That is an interpretation, not read in a statute (Q8).
- **MULTI-OQ-4:** 637 uses the UI definition of "employment" (1043(11)), so coverage follows UI localization.
- **PFML benefits:**
  - Payable from 2026-05-01 (FAQ; lead from the search).
  - Benefits are paid by the State fund, not through payroll.
  - Payroll interaction: retroactive deduction of missed employee premiums during leave, and health coverage must continue [US-MES5-025].
  - The benefit start date is not on an A.2 page in this pass.
- **Family sick leave (636):** this is permission to use existing paid leave for family illness. Not read.
- Confidence: 75%.

## 7. termination
- **Final pay:** due **no later than the next established payday**, whether the employee was discharged or resigned. On demand, the earlier of the next payday or 2 weeks [US-MES5-007].
- **Accrued paid vacation:** must be paid at separation for vacation accrued from 2023-01-01. This does not apply to employers with **10 or fewer employees** or to public employers. A CBA overrides the rule.
- **Penalty:** twice the unpaid amount as liquidated damages, plus interest and fees.
- **Deductions from final pay:** overcompensation (635) and loans or advances evidenced in writing and signed by the employee [US-MES5-007].
- **Severance on closing or mass layoff** at an establishment with 100 or more employees [US-MES5-010]:
  - One week's pay per year of service.
  - Paid within one pay period after the last day of work.
  - 90 days' notice.
- **Separation notice:** separating employees must receive the Employment Security Law notice, for example a copy of the poster [US-MES5-021].
- **Written statement of reason for termination (630):** exists on request; not read.
- Confidence: 85%.

## 8. benefits_in_kind
- **Conformity:** Maine conforms to the IRC as of **2025-12-31** (fixed date) [US-MES5-018].
- **No departures found:** 36 MRSA 5122 has no addition for HSA, section 125, transit or 401(k) exclusions. Maine follows the federal wage exclusions [US-MES5-027].
- **Exception:** Maine does not follow the federal W-4 Step 4(b) deductions in withholding [US-MES5-011].
- **Assessment-level subtractions** (not withholding): employer student-loan payments for qualified hospital health-care employees, and FAME programmes [US-MES5-027].
- **UI wages** include non-cash remuneration at reasonable cash value [US-MES5-020].
- Confidence: 75%. The search was by keyword. Whether the 2025–2026 federal "no tax on tips/overtime" deductions are decoupled is open (Q9); those are deductions, not withholding.

## 9. deductions_garnishments
- **Creditor garnishment** [US-MES5-013]:
  - The most that can be taken is the least of: 25% of disposable earnings; the amount above **40 × the higher of the federal or State minimum wage**; or the total.
  - **In 2026, 604.00 USD/week is protected** (40 × 15.10). This is stricter than the CCPA's 30 × 7.25.
- **Employer duties** [US-MES5-014]:
  - Answer within 20 days.
  - May charge **1 USD per check** forwarded.
  - Liable if it fails to answer.
  - May not discharge the employee because of the order.
- **Child support** [US-MES5-015]:
  - The order adds **2 USD/week** to the support amount.
  - Remit within **7 business days** with the case number.
  - Support orders have priority over non-support garnishments.
  - A processing fee is allowed only if set by DHHS rule (not read).
  - The federal CCPA support percentages apply (US-FED-011).
- **Wage-deduction authorisation:** loans and advances need a written, signed statement (626). The general deduction-authorisation section (629) was not read (Q10).
- **State tax levy:** not researched.
- Confidence: 75%.

## 10. collective_agreements (prevailing wage)
- **Scope** [US-MES5-017, supersedes the partial US-ME-P5-2-007]:
  - State-funded **public works with a contract of 50,000 USD or more**. Contracts under 10,000 USD are never "construction".
  - Also State-assisted energy projects of 2 MW or more (bids from 2023).
- **Rate:** the Bureau of Labor Standards determination (1308).
- **Certified payroll:**
  - Records kept at the job site: names, occupations, hours, job title, rate and wages, including independent contractors.
  - Retained 3 years.
  - A copy is **filed monthly** with the contracting authority.
- **Fine:** at least 250 USD per employee, per day.
- Confidence: 85%.

## 11. indexation
- **State minimum wage:** CPI-W Northeast, August to August, rounded to 0.05, effective 1 January. The poster is published in the autumn [US-MES5-001, US-MES5-003].
- **Portland minimum wage:** fixed steps to 2028, then CPI-U Northeast [US-MES5-012].
- **Exempt salary threshold:** follows the minimum wage (3,000 × minimum) [US-MES5-005].
- **Income tax:** brackets, standard deduction and phase-outs by chained CPI around 15 September; published in the next-year booklet [US-MES5-019].
- **UI wage base:** not indexed (12,000) [US-MES5-020].
- **UPAF:** recomputed each rate year [US-MES5-022].
- **PFML:** wage cap = SSA base; rate set by the department from 2028 [US-MES5-024].
- **Garnishment floor:** moves with the minimum wage [US-MES5-013].

## 12. data_protection
- **SSN at hiring:** no SSN may be requested on an application or during the application process [US-MES5-009].
- **Wage records:** the department must keep them confidential (665(1)) [US-MES5-006].
- **Certified payroll:** the contracting authority must protect SSNs in filed copies [US-MES5-017].
- **Not read:** an SSN-truncation rule for pay statements (none located) and the Maine data-breach notice law (10 MRSA 1346 ff.) (Q11).
- Confidence: 55%.

## 13. live_legal_change
- **2027 minimum wage 15.70** (published, poster 9/26) [US-MES5-003], with the 2027 exempt threshold.
- **Portland:** 17.75 in 2027 and 19.00 in 2028, from the 2025-11-04 referendum [US-MES5-012].
- **Earned paid leave:** carry-over amendment PL 2025 c.438 [US-MES5-008].
- **PFML:** benefits from 2026-05-01; the department sets the rate from 2028 [US-MES5-024].
- **IRC conformity date** moved to 2025-12-31 [US-MES5-018].
- **2027 withholding tables:** not yet located. MRS normally publishes them in December (Q12).
- **Not done:** a full sweep of the MRS and MDOL news pages for 2026-01-01 to today (maine.gov is geo-blocked). Leads only; no tier-B number is used.

---

## Special populations (state level)

| Population | Rule | register_id |
|---|---|---|
| Domestic / household workers | UI covers domestic service in a private home when 1,000 USD or more is paid in a quarter. Minimum wage: no exclusion found in 663(3). | US-MES5-020, US-MES5-005 |
| Agricultural | Minimum wage 15.10 applies (poster: "Agriculture and Non-Agriculture"). The 663(3)(A) exclusion covers the overtime/minimum-wage subchapter except farms with over 300,000 laying birds (poster and statute read together: Q13). UI covers agriculture at 20,000 USD in a quarter or 10+ workers in 20 weeks; H-2A excluded from UI. | US-MES5-002, US-MES5-005, US-MES5-020 |
| Minors | Hours limits for under-18s in school (774). Full minimum wage; no youth sub-minimum found in 664. Newspaper delivery under 18 and a child employed by a parent are excluded from UI. | US-MES5-028, US-MES5-020 |
| Tipped | Cash wage at least 50% of the minimum (7.55 in 2026), notice items A–F. Portland: at most half of 16.75. | US-MES5-001, US-MES5-012 |
| Clergy / religious | Ministers and members of religious orders are excluded from UI. Withholding: no State rule beyond federal (booklet read). | US-MES5-020, US-ME-P5-2-001 |
| Students | School co-op/OJT students, student nurses and interns excluded from UI. Camp counselors excluded from the minimum-wage subchapter (663(3)(F)). | US-MES5-020, US-MES5-005 |
| Nonresident aliens | No State rule beyond federal. Nonresident 12-day / 3,000 USD threshold applies. | US-ME-P5-2-003 |
| Statutory employees | No State rule located beyond federal (not specifically searched). | — |
| Government employees | Overtime exemption for public employees except the State executive/judicial branch. Public employers exempt from vacation payout. PFML: public employees under a 2023 CBA are exempt until it expires. | US-MES5-001, US-MES5-007, US-MES5-025 |
| Family members | Family members living with and dependent on the employer are excluded from the minimum-wage subchapter and from the 621-A pay frequency. Service for one's own child or spouse is excluded from UI. | US-MES5-005, US-MES5-004, US-MES5-020 |
| Small employers | 10 or fewer employees: no earned paid leave and no vacation payout. Under 15: PFML 0.5%. | US-MES5-008, US-MES5-007, US-MES5-024 |

## MULTI hand-offs (ME answers)
- **SUI wage-base credit:** YES. Wages from the same legal entity in any State count toward the 12,000 base (1043(19)) [US-MES5-020].
- **PFML coverage of multistate workers:** follows the Maine UI localization test [US-MES5-025].
- **Paid-sick-leave coverage:** 637 uses the UI definition of "employment", so it follows UI localization [US-MES5-008].
- **Pay-statement reach:** 665(1) has no territorial clause. Default: employment in Maine [US-MES5-006].

## ACCESS gaps
- All `https://www.maine.gov/*`: HTTP 403 (CloudFront geo-block, VPN off). The Wayback copies used are noted per row.
- `https://www.maine.gov/revenue/taxes/income-estate-tax/employer-withholding`: Maine Tax Portal Bulk File Upload Specifications (W-2 format). Not fetched (budget).
- `https://www.maine.gov/paidleave/`: no A.2 PFML rate notice or rule (12-702 CMR) located; the FAQ (A.3) is the only rate source.
- `https://www.maine.gov/labor/labor_laws/minimum_wage_faq.html` and the MDOL / MRS news pages for 2026: not fetched (budget; geo-block).
- Portland ordinance: read from the CivicPlus asset host `https://content.civicplus.com/api/assets/3899b6d8-7441-4566-853b-0491ef6bc426`. The link from `https://www.portlandmaine.gov/` was not re-verified.

## Open questions
- **Q1 UPAF 2026:** the rate array says 0.17%, the UC-1 instructions say 0.16%. What would close it: an employer's 2026 MDOL rate notice, or MDOL BUC confirming the rate-year 2026 UPAF predetermined yield (ratio of total to taxable wages for 2024 × 0.04%).
- **Q2 Exempt salary 2027:** the poster says 905.79, the statute formula gives 905.77. What would close it: the MDOL overtime guidance page (`maine.gov/labor/labor_laws/overtime.html`). Safe build rule: the salary must exceed 3,000 × minimum ÷ 52.
- **Q3 G-DERIVE minimum wage:** CPI-W Northeast for Aug 2025 and Aug 2026 (BLS series CWUR0100SA0) is needed to reproduce 15.10 → 15.70.
- **Q4 Other municipal minimum wages** (e.g. Rockland): a municipal ordinance check, or the MDOL minimum-wage FAQ.
- **Q5 Paycard / direct-deposit consent:** an MDOL rule or Bureau of Consumer Credit Protection guidance; no statute located beyond the no-fee rule.
- **Q6 PFML rate on an A.2 instrument:** the PFML rule 12-702 CMR ch. 1 (contributions section), or an MDOL rate notice for 2026. Otherwise accept A.3 FAQ plus A.1 ceiling (already flagged at seal attempt 6).
- **Q7 State W-2 file format** (EFW2 RS or Maine-specific): the Maine Tax Portal Bulk File Upload Specifications (MRS).
- **Q8 Earned-paid-leave payout at separation:** MDOL earned paid leave rule (12-170 CMR ch. 18) or FAQ.
- **Q9 Maine decoupling** from the federal tips/overtime deductions for 2026: 2026 MRS individual income tax instructions or the conformity act.
- **Q10 General wage-deduction authorisation (26 MRSA 629 / 635):** statute read.
- **Q11 SSN on pay statements and the breach law:** 10 MRSA 1346-1350-B and 10 MRSA 1272-B read.
- **Q12 2027 withholding tables:** the MRS 27_wh_tab_instr.pdf when published (December 2026).
- **Q13 Agricultural minimum wage:** the poster says the 15.10 rate covers agriculture, while 663(3)(A) excludes agricultural workers from the subchapter. The legal basis that reconciles the two (likely 26 MRSA 664 as amended, or an agricultural minimum-wage section) was not read. What would close it: the MDOL minimum-wage FAQ or Title 26 ch. 7 sub-ch. 3 read in full.

## Confidence by domain
labour 90 · income tax 95 · social security 88 · payslip 90 · reporting 85 · leave 75 · termination 85 · BIK 75 · garnishment 75 · prevailing wage 85 · indexation 85 · data protection 55 · live change 65. **Overall about 82%.**

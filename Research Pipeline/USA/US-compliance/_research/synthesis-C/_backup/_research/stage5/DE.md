# Stage 5 — Delaware (DE): 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Mandate block: DE — Delaware, US-MQ-28 (answered at seal attempt 3). This pass extends it to all 13 domains.
Budget declared: 60 fetches / 2 h. Used: about 45 fetches (curl and web search) in about 20 minutes. I stopped fetching at the 75% fetch mark.
Network: no VPN at run time (ipinfo showed a Brazil IP). Every DE official host answered plain curl: delcode.delaware.gov, revenue.delaware.gov, revenuefiles.delaware.gov, labor.delaware.gov, industrialaffairs.delaware.gov and legis.delaware.gov. No Wayback copy was needed.
Register shard: `00-official-sources/_register-shards/S5-DE.csv` has 22 rows, US-DES5-001..022, all `active`, tier A.1/A.2/A.3. New sources are in `00-official-sources/ccg-sources/DE/`: 24 files, 2.1 MB, no file over 1 MB.

Active rows reused without a re-fetch (local file re-read this pass):
- US-DE-P5-1-003: the Employer Guide. It was re-fetched live and the text is identical to the Wayback copy, so it is restated in US-DES5-006 with `supersedes`.
- US-DE-P5-2-001: Wilmington EIT Regulations, `pdfs/DE/DE-wilm-doc462.bin`. Not re-read; the row is unchanged.
- US-DE-P5-2-002: DUI Power of Attorney.
- US-DEL-001/002: ch. 37 and ch. 11 Wayback files. I re-read them for leave and pay-statement content, and the rows were restated as US-DES5-012 and US-DES5-002.
- US-DEL-003 and US-DEP9V-001: 19 Del. C. 3350B/E/F levies. Not redone (P7/P9 list).
- US-MULTI-019: no reciprocity.

Rows that the synthesis should close or upgrade:
- US-DE-P5-1-002: the statute row had no local file. Replaced by US-DES5-010, which has a local file and the same figures.
- US-DE-UI-001: the FAQ row carrying the stale 18,500. Restated by US-DES5-011 and US-DES5-022.
- US-DEP7-002: the tier-B Paid Leave rate row. The rate is now proven from statute by US-DES5-012 (19 Del. C. 3705), so it can go from MANUAL to active on the new row.
- US-DE-PL-001: restated by US-DES5-013.

---

## 1. labour_code
- **State minimum wage: 15.00 USD/h from 2025-01-01** [US-DES5-001, 19 Del. C. 902(a)(5)].
  - This is the last statutory step. The statute has no indexation and no 2027 step.
  - If the federal minimum ever exceeds the state rate, the state rate becomes equal to it.
  - The DOL knowledgebase lists no later increase [US-DES5-021].
  - HS 2 for HB 13 is a tax bill, not a wage bill (see 13).
- **Local minimum wages:** none. 19 Del. C. ch. 9 is statewide, and no local wage ordinance was found.
  - Confidence 85%: I found no explicit preemption clause. It is an absence finding from the chapter read.
- **Learners and apprentices:** DOL may set sub-minimum rates by regulation (906). No youth sub-minimum exists in the statute, so minors get 15.00.
- **Exclusions from the minimum wage** (901(3)):
  - agriculture;
  - domestic service in a private home;
  - executive, administrative and professional (EAP) employees and outside sales;
  - US government employees;
  - fishing;
  - under-18 summer-camp counselors;
  - Department of Correction (DOC) inmates;
  - minor-league baseball players covered by a CBA [US-DES5-001].
- **Overtime:** no state overtime premium rule.
  - Ch. 9 (901-914) was read in full: it has no overtime-rate section, and 912 only preserves more favourable standards.
  - So the FLSA rule applies: 1.5× over 40 hours a week. There is no daily overtime.
  - Confidence 85%: the DOL KB overtime answer did not render under curl.
- **Pay frequency:** at least once per calendar month, on paydays designated in advance [US-DES5-002, 1102(a)].
  - Wages are due within 7 days of the close of the pay period.
  - If payday falls on a nonwork day, pay on the preceding workday.
  - Overtime, new hires and variable part-timers may slip to the next period if the pay period is 16 days or less and payday falls within it (1102(b)).
- **Method of payment** (1102(a)):
  - cash, or a check that can be cashed at full value nearby;
  - direct deposit only on the employee's written request.
  - The statute has no paycard rule.
- **Wage theft, 1102A:** these are violations, with a civil penalty of 2,000-20,000 per violation per employee:
  - failing to withhold taxes;
  - failing to forward withheld money within 7 days of the pay period;
  - misclassification [US-DES5-002].
- **Minors:** an employment certificate (work permit) must be on file for every employee under 18 (19 Del. C. 504) [US-DES5-017].
- **Confidence:** 90%.

## 2. income_tax
- **Authority:** Division of Revenue. **Governing law:** 30 Del. C. ch. 11 [US-DES5-003..005].
- **Rates for taxable years after 2013** (1102(a)(14), still in force for 2026):

  | Taxable income (USD) | Rate |
  |---|---|
  | 0 to 2,000 | 0% |
  | 2,000 to 5,000 | 2.2% |
  | 5,000 to 10,000 | 3.9% |
  | 10,000 to 20,000 | 4.8% |
  | 20,000 to 25,000 | 5.2% |
  | 25,000 to 60,000 | 5.55% |
  | over 60,000 | 6.6% |

  - Not indexed.
  - The change bill (HS 2 for HB 13) is in committee and not enacted [US-DES5-018].
- **Withholding duty** (1151(a)): an employer with an office or business in DE withholds on resident and nonresident wages whenever the wages are subject to federal withholding. The Division's rule is "If you withhold Federal tax, then you must withhold State tax" [US-DES5-005, US-DES5-008].
- **Withholding method**, from the Employer Guide, live page, table "Effective January 1, 2025" [US-DES5-006]:
  1. Annualize the gross pay: daily ×300, weekly ×52, biweekly ×26, semi-monthly ×24, monthly ×12.
  2. Subtract the standard deduction: 3,250 single, 6,500 MFJ, 3,250 MFS.
  3. Apply the table: 0 / 66 / 261 / 741 / 1,001 / 2,943.50 plus the marginal rate on the excess.
  4. Subtract 110 × personal exemptions.
  5. Divide by the number of pay periods.
- **Derivation (G-DERIVE), computed in Python:**
  - The table's base amounts reproduce from the statute rates exactly:
    - 3,000 × 2.2% = 66;
    - + 5,000 × 3.9% = 261;
    - + 10,000 × 4.8% = 741;
    - + 5,000 × 5.2% = 1,001;
    - + 35,000 × 5.55% = 2,943.50.
  - Guide example 1 (single, 1 allowance, 25,000): the tax is 832.00 and the weekly withholding is 13.88.
  - Guide example 2 (supplemental, 500/week plus a 5,000 bonus, single, 1 allowance): it reproduces to 269.625. The Guide shows 269.63, so it rounds half-up to the cent.
  - **Oracle:** the Division publishes no calculator. The Guide's worked examples are the oracle for C37 (URL in US-DES5-006).
- **Rounding:** no rule is stated. The examples round to the cent.
- **Certificate:** federal Form W-4 [US-DES5-008].
  - The Guide text still uses pre-2020 allowance wording and the DE worksheets SD/W-4A and W-4NR.
  - The statute ties exemptions to the federal count (1151(b)).
  - Open question: how a 2020+ W-4 maps to "exemptions" for the 110 credit.
  - No certificate: withhold as single with no allowances.
  - Send a copy to the Division within 5 working days if the employee claims 14+ allowances, or claims exempt with wages expected over 168.50 a week.
- **Supplemental wages:**
  - paid together with regular wages: treat as one payment;
  - paid separately: annualized-with minus annualized-without;
  - tips are handled the same way;
  - recommended withholding on deferred compensation: 5% [US-DES5-006, US-DES5-008].
- **Residents** (1103): domiciled in DE, or keeping a place of abode in DE and spending more than 183 days there.
  - A resident gets a credit for tax paid to another state (1111). It works **at assessment only**, not in withholding [US-DES5-003].
- **Nonresidents:** tax is the resident-basis tax less the 110 credits, times DE-source income / DE AGI (1121) [US-DES5-004].
  - The Guide notes that nonresidents may need to adjust their W-4 using the W-4NR worksheet.
- **Convenience of the employer: YES, statutory.** 30 Del. C. 1124(b)(1)b treats compensation as DE-source when it is "attributable to employment in this State and not required to be performed elsewhere" [US-DES5-004]. This answers the MULTI hand-off.
- **Reciprocity:** none with any state. Withholding is required only in the "duty assigned state" [US-DES5-008, US-MULTI-019].
- **Local income tax:** Wilmington only.
  - 22 Del. C. 901-902 allows the tax only in municipalities over 50,000, capped at 1.25%.
  - Wilmington Earned Income Tax: 1.25% on residents wherever they earn, and on nonresidents for work done in the City.
  - The employer withholds and files a separate return and reconciliation with the City Department of Finance, Earned Income Tax Division [US-DE-P5-2-001, existing row].
- **Confidence:** state 95%; W-4 mapping 70%.

## 3. social_security
- **SUI (employer only; no employee contribution):**
  - **Taxable wage base:** 14,500 for 2026, then **16,500 from 2027-01-01** (or the FUTA base if higher) [US-DES5-010, 3302(28)(A)(viii)-(ix); second authority US-DES5-022].
    - The DOL FAQ page still prints 18,500 and 10,500. It is stale [US-DES5-011].
  - **2026 rates:** new employer 1.0%, new construction employer 1.0%, delinquent 6.3%, range 0.3%-5.4% (2025: 1.2% / 6.5% / 0.3-5.4%) [US-DES5-022].
  - **New-employer rate method:** the average rate of all employers over the last five years. Construction employers headquartered elsewhere get the construction average [US-DES5-011].
- **Operations & Technology assessment 0.2%** (0.175% from 2027) [US-DEL-003, US-DEP7-001].
  - New in 2026: it is billed **separately by letter**, not inside the contributory rate. 2026 Q1 was due 2026-08-31 and Q2 2026-09-30. It is paid by check to the "Op & Tech Lockbox" [US-DES5-011].
  - The DD/RSPEC needs a separate payable line.
- **Industry and employer-size assessments** (3350E/F): first payable 2027 [US-DEP9V-001]. Not redone here.
- **Blue Collar training tax** remains an open MANUAL item from P7 [US-DEL-004]; it was not re-hunted.
- **Delaware Paid Leave** (Healthy Delaware Families Act, 19 Del. C. ch. 37) [US-DES5-012, US-DES5-013]:
  - **Rates fixed by statute for 2025 and 2026:** medical 0.40%, family caregiving 0.08%, parental 0.32% (total 0.80%).
  - **From 2027:** set by DOL on actuarial principles, with a 1.00% cap. The 2027 rate was not yet published on 2026-11-02.
  - **Wage base:** FICA wages, so capped at the SS wage base.
  - **Employee share:** the employer may deduct **up to 50%** of each contribution, only in proportion to wages paid. If it fails to deduct, it owes the whole amount.
  - **Employer size:** 10-24 employees means parental leave only (0.32%); 25+ means all three (0.80%); 9 or fewer are exempt (voluntary opt-in).
  - **Also exempt:** federal employers and seasonal operations closed a month or more.
  - **Filing:** remitted quarterly, with a quarterly Hours & Wage Report in Delaware LaborFirst. Waiver forms exist for employees not expected to qualify.
  - **Benefits:** 80% of the average weekly wage, minimum 100, **maximum 900/week in 2026 and 2027**, indexed to CPI-U Philadelphia-Camden-Wilmington after 2027.
- **No SDI/TDI** and no other employee-paid state levy.
- **Confidence:** 95% (SUI and Paid Leave 2026); 2027 Paid Leave rate open.

## 4. payslip_statute
- **Who:** employers with **more than 3 employees** (19 Del. C. 1108) [US-DES5-002].
- **When and how:** at each payment, on the check, a separate slip, or **electronically if the employee can retain it**. The employee may ask for paper.
- **Required content:**
  - wages due;
  - pay period;
  - total deductions, **each separately specified**;
  - total hours for hourly employees.
- **At hire:** written notice of the rate of pay and the day, hour and place of payment (1108(1)).
  - Rate reductions must be notified before they take effect (1108(2)).
  - Vacation and sick-leave policies must be made available (1108(3)).
- **Retention:** 3 years (1108(6); also 907 under the Minimum Wage Act, which adds hours each day and each week) [US-DES5-001].
- **Language:** the statute has none. The paid-leave poster must be in English, Spanish and any first language of 5%+ of the workforce [US-DEL-001].
- **Reach (MULTI hand-off):** ch. 11 covers a "person suffered or permitted to work by an employer **in this State**" (1101(a)(4)). It applies to work performed in DE; no other reach rule was found.
- **Excluded from ch. 11:** State, political-subdivision and federal employees.
- **Confidence:** 90%.

## 5. reporting_instruments
- **Registration:** One Stop Business Licensing and Registration (withholding). There is no cost [US-DES5-008].
- **Withholding returns** (30 Del. C. 1154) [US-DES5-005, US-DES5-007]:
  - **Filing frequency by July-June lookback:**
    - quarterly up to 4,500;
    - monthly 4,500-25,000;
    - eighth-monthly over 25,000.
    - These are the statutory figures, indexed under 30 Del. C. 515. The Guide prints 6,020 and 33,460 [US-DE-P5-1-003]; I did not read the 2026 indexed values (open question).
  - New agents file monthly.
  - **Due dates:**
    - quarterly: last day of the month after the quarter;
    - monthly: the 15th of the next month;
    - eighth-monthly: 3 working days after periods ending on the 3rd, 7th, 11th, 15th, 19th, 22nd, 25th and last day.
  - The 2026 calendar is in US-DES5-007 (tax type 01106).
  - EFT is required if federal EFT is required (with a 1-year lag).
  - Filing and payment go through https://tax.delaware.gov/.
- **Annual reconciliation:** Form **WTH-REC** replaces the W-3 [US-DES5-009, revised 02/03/26; US-DES5-008].
  - Due by the last day of January with the W-2s.
  - Lines: DE wages, form count, tax withheld, tax paid, balance.
  - Employers that e-file federally must e-file. Paper is allowed only for 10 or fewer forms.
  - TY2025 W-2 deadline: 2026-02-02.
- **W-2 format:** **EFW2 with Delaware RS records required**, uploaded to the Delaware Taxpayer Portal.
  - Do not truncate the SSN on Copy 1 or in the RS record.
  - W-2c/W-3c on paper only.
  - 1099-MISC/NEC (DE residents, or nonresidents working in DE) and 1099-R with DE withholding go directly to DE under Pub 1220 (B record positions 663-684) [US-DES5-008].
  - The Delaware W-2 data-file FAQ document sits behind the Taxpayer Portal and was not read (gap).
- **Employee W-2:** by January 31, or within 30 days of the last wage payment on termination (1152) [US-DES5-005].
- **Quarterly UI reports:** UC-8 (tax report) and UC-8A (wage report), due by the end of the month after the quarter [US-DES5-011].
  - Late reports: 1.5%/month interest and 17.50 per late report.
  - Electronic or magnetic media are accepted through the Online Employer Services Portal [US-DES5-022].
  - The exact electronic file format was not read (open question).
- **Paid Leave:** quarterly Hours & Wage Report and contributions in Delaware LaborFirst [US-DES5-013].
- **New hires** (30 Del. C. 1156A) [US-DES5-005]:
  - Report to the State Directory of New Hires (13 Del. C. 2208) within 20 days, or by two monthly electronic transmissions 12-16 days apart. A multistate employer may designate one state.
  - Fields: name, address, SSN, first day of paid work, and the employer's name, address and FEIN, on a W-4 or equivalent.
  - A rehire after 60+ days of separation counts as a new hire.
  - Fine: 25 per failure.
- **Third-party authorisation:** the DUI Power of Attorney covers UI; for withholding, IRS 2848 only [US-DE-P5-2-002].
- **Confidence:** 85%.

## 6. leave
- **Paid sick leave:** **no Delaware private-sector paid-sick-leave mandate.** The DOL KB says: "Delaware law does not require private employers to provide specific days off ... No Delaware statute requiring days off for adult workers" [US-DES5-021]. Title 19 chapters 5, 9, 11, 33 and 37 were read and carry none either.
  - Employers must make their own sick-leave and vacation policies available (1108(3)) [US-DES5-002].
  - Multistate hand-off: not applicable (no DE sick-leave statute).
- **Paid family and medical leave:** see section 3 [US-DES5-012].
  - Leave lengths: 12 weeks parental per application year; 6 weeks medical or caregiving per 24 months.
  - Eligibility: 12 months and 1,250 hours with the employer.
  - The employer approves or denies an application within 5 business days and notifies DOL within 3 business days.
  - First benefit payment within 30 days, then every 2 weeks. Benefits may be taxable and taxes are withheld (3714).
  - Coverage of multistate workers depends on the **primary worksite**: employees primarily reporting to a DE worksite are covered; out-of-state-worksite employees are not, unless the employer elects (3701(6)a). This differs from the UI localization test (answers the MULTI hand-off).
- **Holidays:** none required for private employers [US-DES5-021].
- **Confidence:** 85%.

## 7. termination
- **Final pay** (1103(a)) [US-DES5-002]:
  - Applies on quit, resignation, discharge, suspension or layoff.
  - Due on the **later of** the next regular payday or **3 business days after the last day worked**.
  - Paid through the usual channel, or by mail on the employee's request.
  - Liquidated damages: the lower of 10% per day or the unpaid wages (1103(b)(2)).
- **Accrued vacation payout:** no statute requires payout. Vacation and separation pay are "benefits or wage supplements" due within 30 days under the employer's agreement or policy (1109), and the policy must be made available (1108(3)). So payout follows the written policy.
- **Death:** up to 300 may be paid to family members without probate (1106).
- **UI separation notice / WARN:** not researched in this pass (open question).
- **Confidence:** 85%.

## 8. benefits_in_kind
- **Rolling conformity:** DE taxable income = federal AGI "as the same are or shall become effective" with the ch. 11 modifications (30 Del. C. 1105) [US-DES5-019].
  - Federal exclusions (401(k)/403(b)/457, 125, HSA, transit, group-term life up to 50,000) therefore flow through.
  - No HSA or section 125 add-back was found in 1106.
  - The withholding base is wages subject to federal withholding (1151).
  - Pension and military-pension exclusions operate at assessment only.
- **SUI wages:** retirement, sickness, medical and death-plan payments are excluded (3302(28)(B)) [US-DES5-010].
- **Paid Leave wages:** FICA wages [US-DES5-012].
- **Confidence:** 85%. The rolling-conformity wording was read; individual IRC sections were not traced.

## 9. deductions_garnishments
- **Wage deductions** (1107): only if one of these applies [US-DES5-002]:
  - required by law;
  - for medical care with no benefit to the employer;
  - signed employee authorization for a lawful purpose that benefits the employee.
- **Creditor garnishment:** **85% of wages exempt**, so the maximum is 15% (10 Del. C. 4913) [US-DES5-014].
  - It does not apply to State fines, costs or taxes.
  - Only one attachment at a time, with first-in priority.
  - Payroll applies the lower of the DE 15% (of wages) and the CCPA 25% (of disposable earnings) per payment.
- **Child-support IWO** (13 Del. C. 513) [US-DES5-016]:
  - Not subject to the 85% exemption; capped at CCPA 1673(b).
  - Priority over everything except federal tax liens.
  - Arrears add-on: up to 20% of current support or 20/month.
  - Withholding starts no later than 7 days after the first payday following receipt. Remit at payday, with name and SSN.
  - Employers with 50+ employees must remit by EFT/EDI.
  - The employer may keep a State-set fee unless it waives it. The **fee amount is not in the statute** (open question).
  - For another state's order, use the law of the employee's principal place of employment for the 411(d) factors.
  - On termination, notify the court or DCSS.
- **State tax levies:** not researched.
- **Confidence:** 85%.

## 10. collective_agreements (prevailing wage)
- **Scope:** 29 Del. C. 6960 [US-DES5-015]. It applies to State-funded public works over **500,000** (new construction) or **45,000** (alteration, repair, renovation, demolition).
- **Rates:** set by DOL, with CBA rates adopted where they prevailed 4 of the last 5 years.
- **Payroll obligations:**
  - **weekly** pay;
  - **weekly sworn (certified) payroll** to DOL, kept by DOL for 6 months;
  - posting of the rates.
- **Penalties:** 1,000-5,000 per violation, plus treble damages.
- **Confidence:** 90%.

## 11. indexation

| Item | Indexed? | Publication / source |
|---|---|---|
| Minimum wage | No (fixed 15.00 since 2025-01-01) | 19 Del. C. 902 [US-DES5-001] |
| PIT brackets, standard deduction, 110 credit | No | 30 Del. C. 1102, 1108, 1110 [US-DES5-003] |
| SUI wage base | Statutory steps: 14,500 (2026) and 16,500 (2027+) | 3302(28)(A) [US-DES5-010]; DOL Merit Rate Table [US-DES5-022] |
| SUI rates | Annual; rate notices issued in January | DOL [US-DES5-011, US-DES5-022] |
| Withholding filing thresholds | Annual, under 30 Del. C. 515 | statute [US-DES5-005]; 2026 values not read |
| Paid Leave contribution rate | Statutory 0.80% for 2025-2026; DOL-set from 2027 (cap 1.00%) | 3705 [US-DES5-012] |
| Paid Leave maximum benefit | 900 for 2026-2027; CPI-U Philadelphia-Camden-Wilmington after 2027 | 3704 [US-DES5-012] |
| Paid Leave wage cap | Follows the SS wage base | 3701(24) |

## 12. data_protection
- **Breach law** (6 Del. C. ch. 12B) [US-DES5-020]:
  - Reasonable security procedures for personal information, which includes the SSN.
  - Breach notice within 60 days.
  - Notice to the Attorney General if more than 500 residents are affected.
  - 1 year of free credit monitoring if SSNs were breached.
- **SSN on pay statements:** no DE statute restricts it. None was located (Delaware Code and web, 2026-11-02), and 1108(4) does not require the SSN.
- **SSN where required:** the **full SSN** on the W-2 state copy and in the EFW2 RS record [US-DES5-008], and on IWO remittances [US-DES5-016].
- **Paid Leave reports:** confidential (3705(j)).
- **Confidence:** 75% (an absence finding on SSN display).

## 13. live_legal_change (2026-01-01 to 2026-11-02)
- **SUI:**
  - The wage base rose 12,500 → 14,500 on 2026-01-01, with 16,500 enacted for 2027.
  - The new-employer rate fell 1.2% → 1.0% [US-DES5-010, US-DES5-022].
- **Operations & Technology 0.2%:** separated out of the UI rate and billed by letter from August 2026 (Q1 due 2026-08-31, Q2 due 2026-09-30). It falls to 0.175% from 2027 [US-DES5-011, US-DEL-003].
- **Industry and employer-size assessments:** become part of the earned rate from 2027 [US-DEP9V-001].
- **Delaware Paid Leave:** claims since 2026-01-01. The 2027 contribution rate will be set by DOL and is not yet published [US-DES5-012, US-DES5-013].
- **PIT bill HB 13 / HS 2 for HB 13:**
  - Proposed change: new top brackets (above 150,000 in HS 2) and lower rates under 60,000, for taxable years after 2025.
  - Status: **draft, in House Revenue & Finance Committee since 2025-06-17, NOT enacted**.
  - Level: it would act at assessment and withholding.
  - 30 Del. C. 1102 is unchanged as of 2026-11-02 [US-DES5-018].
- **Wage payment:** 19 Del. C. 1103 (3-business-day final-pay rule) and 1102A (wage theft) are in the current text. The enactment date of the 1103 wording was not identified (85th-volume Laws).
- **Withholding:** 30 Del. C. 1154 was amended by 85 Del. Laws c. 301. The content of that amendment was not identified.
- **Search note:** the agency news feeds were not swept item by item. The 2026 changes above come from the statute pages and agency pages read today.

## Special populations (US-OWN-005, state level)

| Population | DE rule affecting payroll | register_id |
|---|---|---|
| Domestic / household workers | Excluded from the state minimum wage (901(3)b), so FLSA applies. UI covered if 1,000+ cash in a quarter (3302(15)(B)). PIT withholding follows federal (none required for household workers federally, so DE follows) | US-DES5-001, US-DES5-010, US-DES5-005 |
| Agricultural workers | Excluded from the state minimum wage (901(3)a). UI covered only if the employer paid 20,000+ cash in a quarter or had 10+ workers in 20 weeks (3302(15)(A)(vii)) | US-DES5-001, US-DES5-010 |
| Minors | Work permit on file for under-18s (504). Hazardous-occupation and hours limits. No youth sub-minimum wage. Under-18 camp counselors excluded from the minimum wage. A child under 18 working for a parent is excluded from UI | US-DES5-017, US-DES5-001, US-DES5-010 |
| Tipped employees | Cash wage of at least 2.23/h, with a make-up to 15.00. Tips belong to the employee; a mandatory pool is capped at 15%. Service-charge notice rule. Tips are withheld as supplemental wages | US-DES5-001, US-DES5-021, US-DES5-006 |
| Clergy / religious | Religious and 501(c)(3)-type organizations: UI exclusion per 3302(15)(E) (as qualified; reimbursement election exists). Gratuitous volunteers excluded from the minimum wage. PIT follows federal | US-DES5-010, US-DES5-001 |
| Students | Students employed by their own school, and work-study students, are excluded from UI (3302(15)(J)-(K)). No state student minimum wage | US-DES5-010 |
| Nonresident aliens | No state rule beyond federal: DE withholds when wages are subject to federal withholding (1151) | US-DES5-005 |
| Nonresident (other-state) employees | Withhold on DE-source wages. The convenience rule (1124(b)(1)b) applies. No reciprocity | US-DES5-004, US-DES5-008 |
| Statutory employees / commission agents | Commission-only insurance and real-estate agents are excluded from UI (3302(15)(H)). Direct sellers are excluded (15)(N). Independent contractors are excluded from ch. 11 | US-DES5-010, US-DES5-002 |
| Government employees | State and political-subdivision employees are excluded from ch. 11 wage payment and from UI (except per 3302(14)(B)). US employees are excluded from the minimum wage. State-plan employees are excluded from Paid Leave (3701(6)b) | US-DES5-002, US-DES5-010, US-DES5-012 |
| Family employment | Service for one's spouse or child is excluded from UI. Sole-proprietor family wages are excluded (DOL FAQ) | US-DES5-010, US-DES5-011 |
| Small employers | Pay-statement and notice duties apply only above 3 employees. Paid Leave: under 10 exempt; 10-24 parental only | US-DES5-002, US-DES5-012 |

## ACCESS gaps (exact URLs)
None of the official hosts blocked a request. These items could not be read in this pass:
- **Delaware W-2 data-file FAQ document** ("W2/1099 FAQ document located on the Delaware Tax Portal"): it is behind https://tax.delaware.gov/ and is linked only from the portal. I did not try it (no login).
- **DOL Industrial Affairs KB overtime answer:** https://industrialaffairs.delaware.gov/en/knowledgebase-employer/when-are-employers-required-to-pay-overtime-in-delaware. The answer body is script-rendered, and curl returned only the meta description. The fetched file was discarded. A browser pass would settle it, though the statute reading already covers the point.
- **UI quarterly electronic wage-file specification:** the DOL FAQ says to call (302) 761-8484. No public spec was found on https://labor.delaware.gov/divisions/unemployment-insurance/employer-services/.

## Open questions
1. **W-4 2020+ mapping.** How does an employer convert a post-2019 federal W-4 (no allowances) into DE "personal exemptions" for the 110 credit? The Guide still uses allowance wording. *What would close it:* a Division of Revenue memo or FAQ on the 2020+ W-4 (Division of Revenue, Withholding unit, 302-577-8779), or a DE-specific certificate if one exists.
2. **2026 indexed withholding filing thresholds** (statutory 4,500 / 25,000 adjusted under 30 Del. C. 515; the Guide prints 6,020 / 33,460, undated). *What would close it:* the 2026 lookback notice or the 30 Del. C. 515 adjustment table from the Division of Revenue.
3. **2027 Delaware Paid Leave contribution rates** (DOL-set from 2027, cap 1.00%). *What would close it:* a DOL Delaware Paid Leave notice or regulation for 2027 (expected before 2027-01-01).
4. **IWO employer fee amount** ("a fee, established by the State", 13 Del. C. 513(b)(8)a). *What would close it:* the DCSS employer page or regulation stating the fee.
5. **Whether the 2026 SUI range 0.3%-5.4% excludes the separately billed 0.2% Op & Tech.** *What would close it:* a 2026 DOL rate notice (the employer rate letter) or the DOL Employer Handbook.
6. **UI separation notice duty and UI electronic wage-file format** (UC-8A). *What would close it:* the DOL Employer Handbook (linked from the employer-services page; not fetched for budget).
7. **Content of the 85 Del. Laws c. 301 amendment to 30 Del. C. 1154, and the enactment date of the 1103 three-business-day wording.** *What would close it:* the session-law pages on legis.delaware.gov.
8. **Wilmington:** the existing row US-DE-P5-2-001 (regulations rev. 2023) was not re-verified this pass. The 2026 rate is assumed 1.25% (the statutory cap). *What would close it:* the City of Wilmington Finance EIT page or the 2026 employer reconciliation form.

## MULTI hand-offs answered
- **SUI wage-base credit:** YES. 3302(28)(A)(x) counts employment under another state's UI law toward the DE base [US-DES5-010].
- **PFML coverage of multistate workers:** follows the primary DE worksite (3701(6)a), not UI localization [US-DES5-012].
- **Paid sick leave:** not applicable (no state statute) [US-DES5-021].
- **Pay-statement reach:** work performed in DE (1101(a)(4)) [US-DES5-002].
- **Convenience rule:** statutory (30 Del. C. 1124(b)(1)b) [US-DES5-004].

## Parallelism note
Nothing in DE is naturally parallel: one state agency per tax and one city. The open questions are 6 independent single-document lookups that a browser pass or one more worker could close in about 10 fetches.

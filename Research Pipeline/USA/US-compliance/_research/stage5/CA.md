# Stage 5 — California (CA), 13-domain hunt

Worker run 2026-11-02 (07:10–07:35 local). Budget declared: 60 fetches / 2 h; used about 42 fetches (including 5 web searches) and about 25 min. Acquisition stopped near 75% of the fetch budget.
Register shard: `00-official-sources/_register-shards/S5-CA.csv` (22 rows, US-CAS5-001..022, 20 columns each). Source files: `00-official-sources/ccg-sources/CA/` (24 files, about 5.3 MB). The 2026 DE 44 that was already on disk (`00-official-sources/pdfs/CA/de44_wb.pdf`, Rev. 52 4-26, reused, not fetched again) carries most of the EDD figures.
Active rows reused, not fetched again: US-CAEDD-001/-004/-005/-006, US-CALAB-001, US-CAP6-001, US-CAP7-001/-002/-003, US-CAPW-001.

## 1. labour_code
- **Minimum wage.** 16.90/h from 2026-01-01 to 2026-12-31. It applies to all employers with no size distinction, unless a higher industry or local minimum applies. Learners may be paid 85% for their first 160 hours [US-CAS5-006, A.2]. The rate is **17.40/h from 2027-01-01**: DOF certified it on 2026-07-31, an increase of 2.99% [US-CAS5-007, A.2, second independent authority: DIR News 2026-66 + Governor release].
- **Exempt salary threshold.** 70,304/yr in 2026 (2 × 16.90 × 2,080, derived) and 72,384/yr in 2027 (quoted by DIR) [US-CAS5-006/-007].
- **Local minimum wages.** Cities and counties may set higher rates, and the employer applies the most favourable one. DIR does not keep the list; it points to the UC Berkeley Labor Center inventory, which is tier B. **No local rate is registered** (open question 1).
- **Industry minimums.** Fast-food (Lab. Code 1474 ff.) and health-care (SB 525) minimums were not fetched (open question 2).
- **Overtime (Lab. Code 510).** 1.5× for hours over 8 in a day, over 40 in a week, and the first 8 hours of the 7th consecutive day. 2× for hours over 12 in a day and over 8 on the 7th day. Alternative workweek exceptions apply [US-CAS5-008, A.1].
- **Paydays (Lab. Code 204).** Pay is due twice a month: work from the 1st to the 15th is paid between the 16th and the 26th, and work from the 16th to the end of the month is paid between the 1st and the 10th of the next month. FLSA-exempt EAP salaries may be paid monthly by the 26th. Weekly, biweekly and semimonthly payrolls comply if paid within 7 days of the period close. Overtime is paid by the next regular payday [US-CAS5-009, A.1].
- **Method of payment.** Direct deposit needs the employee's voluntary authorisation (Lab. Code 213(d)) [US-CAS5-009]. The 213(d) snapshot dates from 2022-10-15 (last amended 2005).
- Confidence: High (state); Low (local minimum wages).

## 2. income_tax
- **Authority and form.** EDD collects PIT withholding. The form is **DE 4 Rev. 56 (1-26)**; the federal W-4 has been used for FIT only since 2020 [US-CAS5-015, US-CAS5-004]. With no valid DE 4, withhold as Single with 0 allowances. An exempt status lasts one year and must be renewed by Feb 15 [US-CAS5-004].
- **Method.** Method A (wage-bracket tables, wages under 1M) or Method B (exact calculation) [US-CAS5-001, A.2]. Annual values for 2026:
  - low-income exemption: 18,896 (S / M 0–1) and 37,791 (M 2+ / HoH);
  - standard deduction: 5,706 and 11,412;
  - allowance credit: 168.30 each;
  - estimated-deduction allowance: 1,000 each;
  - brackets from 1.1% to 14.63%, with 13.53% up to 1,000,000 and 14.63% above. The full Single, Married and HoH tables are in the row.
- **G-DERIVE / oracle.** I reproduced DE 44 worked examples E and F in Python:
  - F: 57,000 − 11,412 = 45,588 → 243.74 + 2.2% × 23,430 = 759.20 − 673.20 = 86.00/yr = 7.17/month;
  - E: 4.13 semimonthly.
  - Both match exactly.
  - The Single cumulative bases also re-derive: 121.87 / 455.94 / 1,124.21 / 2,186.15 / 3,522.17 / … / 114,220.27.
  - The 34,084.81 base derives as 34,084.80 because of rounding at intermediate steps.
  - **Oracle = DE 44 Method B examples A–F (Rev. 52, 4-26).**
- **Supplemental wages.** Aggregate when paid with regular wages. When paid separately, use aggregate or a flat rate: 10.23% for bonuses and stock options, 6.6% for other supplemental pay [US-CAS5-004 on the 2026 DE 44, which replaces reliance on the MANUAL US-CAEDD-003].
- **Rounding.** Method B carries no rounding rule beyond cents. The examples round per-period tax to cents.
- **Residents and nonresidents.** Residents: CA tax on all wages, with credit for withholding required by another state (withhold only the excess). Nonresidents working wholly in CA: all wages. Nonresidents in split-state work: working-day ratio, or a volume ratio for commission pay. A military spouse can claim an exclusion on the DE 4 [US-CAS5-004, US-CAEDD-005].
- **Local income tax.** None located [US-CAEDD-005, full DE 44 scan]. W-2 box 19 is generic wording only.
- **Reciprocity and convenience-of-employer.** No reciprocity agreement appears in the DE 44. The resident-credit mechanism is the one described above. Convenience-of-employer is left to the MULTI unit.
- **Household employees.** PIT withholding is required only if employer and employee agree [US-CAS5-004].
- Confidence: High.

## 3. social_security
- **UI.** Wage base 7,000 (2026, and kept for **2027**). New-employer rate 3.4% for 2–3 years. Range 1.5%–6.2% (Schedule F+). Maximum 434 per employee. Employer pays only [US-CAEDD-001, DE 44 p.8, US-CAS5-016].
- **ETT.** 0.1% on 7,000, so 7 per employee; the same in 2027 [US-CAP7-001, US-CAS5-016].
- **SDI (including PFL).** Employee pays 1.3% for 2026 with no wage cap since 2024-01-01 (SB 951) and no employer share [US-CAEDD-004, US-CAP7-002; DE 44 p.ii confirms 1.3%]. **The 2027 SDI rate is not published on EDD at read time.** A tier-B search summary says 1.4% projected; it is not used (open question 3).
- **Voluntary Plan (VPDI)** can replace SDI; it is shown as VPDI in W-2 box 14 [US-CAS5-018].
- **Coverage exceptions** for special classes are in US-CAS5-014 (see the populations table).
- Confidence: High (2026); 2027 SDI open.

## 4. payslip_statute
- **Content (Lab. Code 226(a), A.1 text now on disk).** The statement is due semimonthly or with each payment and must show nine items:
  1. gross wages;
  2. total hours (not required for salaried exempt employees);
  3. piece-rate units and rates;
  4. deductions;
  5. net wages;
  6. pay-period dates;
  7. employee name plus the **last 4 SSN digits or an employee ID**;
  8. employer legal name and address;
  9. every hourly rate with the hours at each rate.
- **Retention and penalties.** A copy is kept 3 years. Inspection requests are answered within 21 days. Penalties run 50/100 per violation up to 4,000, plus 750 for failing an inspection request [US-CAS5-005]. This closes the "leginfo text gated, residual" note on US-MQ-24 part 6.
- **Sick leave balance.** The available paid sick leave must appear on the statement or in a separate writing each payday [US-CAS5-011].
- **Overtime corrections** may be itemised on the next paystub [US-CAS5-009].
- **Exclusions.** Household employees are excluded (226(d)). Public employers are excluded except for the SSN rule (226(i)).
- **Electronic delivery.** The statute says "in writing". **No electronic-consent rule was fetched** (open question 4).
- **Language.** English (US-OWN-006). The 2810.5 notice goes in the employer's usual language [US-CAP6-001].
- Confidence: High (content); Medium (e-delivery).

## 5. reporting_instruments
All items from [US-CAS5-002, US-CAS5-018, A.2, DE 44 2026] unless another row is cited.
- **Registration.** DE 1 within 15 days after paying more than 100 in wages in a quarter; DE 1P for employers who withhold PIT only.
- **Deposits (DE 88, PIT + SDI).** They follow the federal schedule:
  - next-day if accumulated PIT is over 400;
  - semi-weekly;
  - monthly (by the 15th) if 350 or more;
  - quarterly if under 350.
  - EFT must settle by the 3rd business day. The failure-to-deposit penalty is 15%.
- **Quarterly return and wage report.** DE 9 + DE 9C, electronic only, filed even with zero payroll. Due Apr 1 / Jul 1 / Oct 1 / Jan 1; delinquent after Apr 30, Jul 31 and Nov 2, 2026 and Feb 1, 2027. The DE 9C carries, per employee, subject wages, PIT wages and PIT withheld. Corrections go on the DE 9ADJ.
- **Annual reconciliation.** There is no separate annual return.
- **W-2.** Given to employees by 2027-02-01. Box 14 = CASDI, box 16 = CA PIT wages, box 17 = CA PIT withheld. **The W-2 is not filed with EDD or FTB.**
- **New hires.** DE 34 within 20 days of the start-of-work date; a rehire is reported after a separation of 60 days or more. Fields:
  - employer: EDD account number, FEIN, name, address, contact;
  - employee: name, SSN, home address, start date.
  - Independent contractors go on the DE 542 (paid or contracted 600 or more, within 20 days).
- **Channel.** e-Services for Business (portal and file upload). POA / third-party agent through the DE 48 [US-CAEDD-006].
- **Format.** The DE 9C file format spec (EDD "e-file" / FSET) was not fetched; this is the Stage-3 gap (open question 5).
- Confidence: High (mechanics); Medium (file spec).

## 6. leave
- **Paid sick leave (Lab. Code 246, SB 616 version).**
  - Eligible after 30 days of work in CA. Accrual is at least 1 hour per 30 hours worked; exempt employees are deemed to work 40 hours a week.
  - Alternative accrual: 24 hours by day 120 and 40 hours by day 200. Use starts on day 90.
  - Usage may be capped at 40 h / 5 days a year and the accrual balance at 80 h / 10 days. Front-loading 40 h / 5 days is allowed.
  - Unused sick leave is not paid out. It is reinstated on rehire within 1 year.
  - Pay rate is the regular rate, or the 90-day average excluding OT premium. The minimum increment is at most 2 hours [US-CAS5-011, A.1].
- **PFL** is a wage-replacement benefit paid by EDD and funded inside the 1.3% SDI. There is no employer payroll calculation beyond withholding. EDD's 2026 DI/PFL benefit amounts were not fetched (open question 6).
- **CFRA** (job-protected leave) was not fetched; it does not affect pay calculation.
- Confidence: High (PSL); Medium (PFL benefit side).

## 7. termination
- **Final pay timing.**
  - Discharge: all wages due immediately (72 hours for seasonal perishable-food layoffs).
  - Quit: within 72 hours, or at the last day if the employee gave 72 hours' notice.
  - Waiting-time penalty for willful failure: one day's wages per day, up to 30 days [US-CAS5-010, A.1].
- **Vested vacation.** Paid at the final rate; forfeiture is prohibited (Lab. Code 227.3) [US-CAS5-010].
- **Sick leave** is not paid out [US-CAS5-011].
- **Separation notices.** "Notice to Employee as to Change in Relationship" (CUIC 1089) plus the DE 2320 pamphlet at discharge, layoff or leave; email only with opt-in [US-CAS5-018].
- **Cal-WARN.** Lab. Code 1400–1408 requires 60 days' notice [US-CAS5-018]. The 75-employee coverage threshold was not quoted from an authority page (open question 7).
- Confidence: High.

## 8. benefits_in_kind
- **HSA.** CA does not conform. Employer and employee HSA contributions are subject to UI/ETT, SDI and PIT (not subject to UI/SDI when made through a cafeteria plan) [US-CAS5-019]. For PIT, the employer HSA contribution (W-2 code W) is added back [US-CAS5-020, second authority FTB].
- **401(k) deferrals.** UI/SDI subject, PIT not subject [US-CAS5-019, US-CAS5-003].
- **Section 125, dependent care, Sec. 127 educational assistance.** Not subject.
- **Transit and parking.** Not subject; for PIT there is no monetary limit [US-CAS5-019].
- **Group-term life over 50k.** UI/SDI not subject; PIT not withheld but reportable [US-CAS5-019].
- **OBBBA.** CA generally does not conform to the 2025-07-04 OBBBA (no state tips or overtime deduction) [US-CAS5-020].
- **Meals and lodging 2026.**
  - Meals: 15.85 per day; breakfast 3.25; lunch 4.90; dinner 7.70; 5.70 for an unidentified meal.
  - Lodging: 66⅔% of rental value, minimum 66.10/week, maximum 2,038/month.
  - Not PIT when provided for the employer's convenience on the premises [US-CAS5-003].
- Confidence: High (2025/2026). One claim was not verified: a search summary said an HSA exclusion applies for 2026–2030 (open question 8).

## 9. deductions_garnishments
- **Wage deductions.** Allowed only when required by law or authorised in writing for insurance, medical or similar items (Lab. Code 224). There is no tip credit and no deduction from tips; card tips are paid without processing fees (Lab. Code 351) [US-CAS5-012, A.1].
- **Creditor garnishment** (Earnings Withholding Order WG-002, Rev. 2026-01-01). The amount withheld is the lesser of:
  - 20% of disposable earnings; or
  - 40% of disposable earnings above minimum wage × 48 (weekly), 96 (biweekly), 104 (semimonthly) or 208 (monthly).
  - The local minimum wage is used where it is higher. Support is deducted first [US-CAS5-013, A.2].
  - This is stricter than the CCPA's 25% / 30×FMW.
  - The CCP 706.050 Wayback copy (2022) was pre-SB 1477 text and was discarded.
- **Child support.**
  - Cap: 50% of income after taxes.
  - Timing: withholding starts by the first pay period after receipt. The employee gets the copies within 10 days. Payment reaches the SDU within 7 business days of the pay date, electronically (Fam. Code 17309.5).
  - Records and reporting: the IWO is kept 1 year after separation, and terminations are reported to the LCSA [US-CAS5-022, A.2].
  - The employer fee was not verified (open question 9).
- **State tax levies** (FTB / EDD orders to withhold) were not fetched (open question 9).
- Confidence: High (EWO, IWO); Medium (fees, levies).

## 10. collective_agreements (prevailing wage)
- **Coverage.** State prevailing wage applies to public works (Lab. Code 1720, 1771) [US-CAPW-001, A.1].
- **Certified payroll.** Submitted electronically to the Labor Commissioner through DIR eCPR, with an XML upload spec available; some project categories are exempt [US-CAS5-017, A.2, status partial].
- **Thresholds.** The project-value thresholds (the 1,000 public-works threshold and the small-project exemptions) were not quoted (open question 10).
- **CBAs.** They can override Lab. Code 204 pay timing, 227.3 vacation and 510 alternative workweeks [US-CAS5-009/-010/-008].
- Confidence: Medium.

## 11. indexation
- **Minimum wage.** Indexed to CPI and certified by DOF by Aug 1 (Lab. Code 1182.12(d)). 2027 = 17.40. Check: 16.90 × 1.0299 = 17.405, published as 17.40 [US-CAS5-007]. The exempt salary threshold follows at 2 × MW × 2,080.
- **PIT brackets, deduction and credit tables** are indexed each year and published in DE 44 / Method B [US-CAS5-001].
- **UI base** is fixed at 7,000 by statute. **SDI rate** is set yearly by law/EDD, with no cap.
- **Meals and lodging values** are set yearly in DE 44 / DE 3395 [US-CAS5-003].
- **EWO thresholds** move with the minimum wage [US-CAS5-013].

## 12. data_protection
- **CCPA/CPRA.** Applies to employee and applicant data since 2023-01-01; the employment exemption expired 2022-12-31. Requests to know, correct or delete are answered within 45 days, extendable to 90 [US-CAS5-021, A.3].
- **Pay statements.** Show only the last 4 SSN digits or an employee ID (Lab. Code 226(a)(7) and 226(i) for public employers) [US-CAS5-005].
- **Retention.**
  - Wage statements: 3 years [US-CAS5-005].
  - EDD payroll records: 4 years, or 8 years for non-employee payments [US-CAS5-003].
  - IWO: 1 year after separation [US-CAS5-022].
- Confidence: High.

## 13. live_legal_change (2026-01-01 → 2026-11-02, and 2027)
- MW 17.40 and the exempt threshold of 72,384 from 2027-01-01 [US-CAS5-007].
- UI/ETT 2027: base 7,000 and ETT 0.1% unchanged; DE 2088 rate notices are mailed by 2026-12-31 [US-CAS5-016].
- 2027 SDI rate not yet published (open question 3).
- 2027 PIT withholding schedules not yet published (normally in December in the DE 44).
- AB 1514: the Borello test is reinstated for licensed manicurists from 2026-01-01 to 2028-12-31, and the commercial-fisher exception is extended (worker classification) [US-CAS5-016].
- DE 4 reissued as Rev. 56 (1-26) [US-CAS5-015].
- Delinquent-tax interest is 7% for both halves of 2026 [US-CAS5-016].
- The 2026 disaster-area filing extensions are listed on the EDD page [US-CAS5-016].
- Status: all of the above are in force or enacted. None is a ruling or a draft bill.

## Special populations (US-OWN-005, state round)
| Population | CA rule | register_id |
|---|---|---|
| Domestic / household | UI/ETT subject once 1,000 cash in a quarter; SDI once 750 in a quarter; PIT withholding only by agreement; Lab. Code 226 pay statement does not apply | US-CAS5-014, US-CAS5-004, US-CAS5-005 |
| Agricultural | UI/ETT/SDI subject; PIT withholding not required, PIT wages reportable; H-2A workers the same. Phased-in ag overtime (AB 1066) not fetched | US-CAS5-014 |
| Minors | No youth subminimum in the MW order pages read; the learner rule (85%, first 160 h) applies at any age. Newspaper carriers under 18 are excluded from UI/SDI/PIT. Child-labour permits not fetched | US-CAS5-006, US-CAS5-014 |
| Tipped employees | No tip credit; minimum wage paid in full; tips are the employee's property; no card-fee deduction | US-CAS5-012, US-CAS5-006 |
| Clergy / religious | Ministers and religious orders: UI/SDI not subject (elective), PIT withholding not required; church employees: UI/SDI not subject, PIT subject | US-CAS5-014, US-CAS5-003 |
| Students | Students working for their own school, student nurses (other hospitals), work-study under 22, full-time organized-camp students: UI/SDI not subject; PIT subject | US-CAS5-014 |
| Nonresident aliens | F/J/M/Q nonimmigrants excluded from UI/SDI (CUIC 608 / IRC 3306(c)(19)); PIT subject unless a treaty expressly covers state taxes | US-CAS5-014 |
| Statutory employees | Artists/authors and similar statutory employees covered for UI/SDI per DE 231TE/DE 231SE; commissioned authors not subject to PIT withholding | US-CAS5-014 |
| Government employees | Public entities: UI subject, SDI not subject unless elective coverage, PIT subject; elected officials, legislators, judiciary, National Guard: UI/SDI not subject; Lab. Code 226 applies only via the SSN rule | US-CAS5-014, US-CAS5-005 |

## ACCESS gaps (exact URLs)
- `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=226`: direct 403 (bot check). The Wayback copies used are dated 2026-08-31 (226, 204), 2026-01-02 (510) and 2025 (201, 202, 203, 227.3, 246, 224, 351). Section 213 is from 2022-10-15.
- `https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=706.050`: 403. Wayback holds only 2022-01-21, which is pre-SB 1477 and was discarded. The current rule is taken from Judicial Council WG-002 (Rev. 2026-01-01).
- `https://www.dir.ca.gov/dlse/faq_minimumwage.htm`, `https://dir.ca.gov/DIRNews/2026/2026-66.html` and `https://www.dir.ca.gov/Public-Works/Certified-Payroll-Reporting.html`: direct curl timed out (000). Wayback (2026) used.
- `https://childsupport.ca.gov/employers/`: 404 directly and on Wayback. PUB 307 and the IWO fact sheet were used instead.
- `https://www.ftb.ca.gov/forms/2025/2025-1001-publication.html`: 404 (guessed URL). The 540 CA instructions were used instead.

## Open questions
1. **Local minimum wages** (LA City/County, SF, San Jose, Oakland, Berkeley, etc.). DIR does not keep them. What would close it: each city's labor-standards office bulletin (e.g. LA OWS, SF OLSE) for the 2026-07-01 and 2027-01-01 rates. This is a natural fan-out across cities.
2. **Industry minimum wages** (fast food 20.00+ under the Fast Food Council; health-care SB 525 tiers). What would close it: the DIR fast-food and health-care minimum wage FAQ pages.
3. **2027 SDI rate.** Not on EDD at read time; tier B claims 1.4%. What would close it: the EDD Rates and Withholding page or the DE 44 2027 edition (normally December 2026).
4. **Electronic pay-statement consent.** What would close it: a DLSE opinion letter or the DIR paydays FAQ on electronic wage statements.
5. **DE 9C electronic file format** (EDD e-file specification). What would close it: the EDD "e-Services for Business – File Transfer" spec or the DE 9C/DE 34 file layouts, for Stage 3.
6. **2026 DI/PFL weekly benefit maximum and replacement rates.** What would close it: EDD Quick Statistics (edd.ca.gov/en/about_edd/quick_statistics).
7. **Cal-WARN coverage threshold (75 employees).** What would close it: Lab. Code 1400 text or the EDD WARN employer page.
8. **HSA conformity from 2026.** A search summary says recent legislation excludes employer HSA contributions for 2026–2030; I did not verify it. What would close it: the enacted bill on leginfo, or the FTB 2026 Schedule CA instructions or an FTB "What's New" entry.
9. **Child-support employer fee per payment; FTB/EDD order-to-withhold (state tax levy) priority.** What would close it: Family Code 5235 text and the FTB "Earnings Withholding Order for Taxes" employer instructions.
10. **Public-works thresholds** (1,000 coverage; DIR registration and eCPR exemption for small projects). What would close it: Lab. Code 1725.5 / 1771 / 1773.3 text or the DIR registration FAQ.
11. **Agricultural overtime phase-in (AB 1066) and child-labour permit rules.** What would close it: Lab. Code 860–864 text and the DIR agricultural overtime FAQ.

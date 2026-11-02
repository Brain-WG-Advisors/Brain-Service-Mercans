# Stage 5 — West Virginia (WV): 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Mandate block: US-MQ-69 (answered at seal attempt 4, tier T4).

**Budget.** I declared 60 fetches and 2 h. I used about 48 fetches: curl, 2 web searches and about 10 Wayback calls. I stopped acquiring at the 75% fetch mark, inside the wall-clock limit.

**Outputs.**
- Register shard: `00-official-sources/_register-shards/S5-WV.csv`, 18 rows (US-WVS5-001..018, 20 columns).
- Sources: `00-official-sources/ccg-sources/WV/`, 29 files, 2.6 MB.

**Access note.**
- The VPN was OFF during this run (exit IP in Brazil).
- `code.wvlegislature.gov` redirects non-US traffic to fbi.gov (302). Every statute copy therefore comes from the Wayback `pdf/` route or from the enrolled bill on `www.wvlegislature.gov`, which is reachable.
- `tax.wv.gov`, `labor.wv.gov` and `workforcewv.org` answered directly.
- **Stale publisher copies.** The Wayback copies of code.wvlegislature.gov can be out of date. The 2025-03-29 copy of 21A-1A-28 still carries the text from before 2024. The enrolled act prevails (see §3).

**Active rows reused, not re-fetched:**
- US-WVPIT-001 (11-21-71)
- US-WVP51-001/-002/-003/-005/-009
- US-WVP52-002/-004/-006
- US-WVR3-001/-002/-004
- US-WVL-001/-002
- US-WVP9L-001
- US-MULTI-015

IT-100.2A was re-downloaded live and is byte-identical to the local file of US-WVP51-005, so that row is re-verified on 2026-11-02.

---

## 1. labour_code
- **Minimum wage.** **8.75 USD/h** since 2016-01-01. The 2026 legislature enacted no change and no 2027 rate:
  - HB 5485 (2026 RS) would have amended 21-5C-2. It died in House Energy and Public Works on 2026-02-13 [US-WVS5-017].
  - The rate is quoted from the DOL FAQ [US-WVS5-007]. The statute text of 21-5C-2 itself was not retrieved because of the geo-block.
- **Coverage test.** The state minimum wage applies where 6 or more non-exempt employees work at one separate, distinct and permanent location, counted per location [US-WVS5-005, US-WVS5-007]:
  - Work done from home or at a client's residence counts at that location.
  - For temporary assignments, the location is where the assignments are issued.
  - Out-of-state employers are covered under the same test.
  - Where the test fails, the federal 7.25 applies.
- **Exclusions (21-5C-1(f)).** The state law excludes [US-WVS5-005]:
  - agriculture (FLSA definition), part-time students, people aged 62+ drawing Social Security, executive/administrative/professional staff, outside salesmen, family members, on-the-job trainees, summer camps, local motorbus employees and DOT-regulated drivers;
  - seasonal whitewater-outfitter and amusement-park staff (overtime only), among others.
- **Overtime.** 1.5× over 40 h per workweek; there is no daily overtime. The regular-rate exclusions mirror the FLSA [US-WVS5-004]. State overtime does not apply where 80% or more of the employer's workforce is FLSA-covered. The DOL says most employers therefore apply the state minimum wage and federal overtime [US-WVS5-005, US-WVS5-007].
- **Local minimum wages.** None found. There is no municipal minimum-wage authority in the sources read; Chapter 8 was not swept, so this rests on absence (open question Q5).
- **Pay frequency.** At least twice a month, with no more than 19 days between paydays (railroads semimonthly). A Commissioner-approved special agreement can allow less than biweekly, but never less than monthly. "Wages due" covers at least the wages earned up to the 12th day before payday. A payday that falls on a closed day moves to the preceding open day [US-WVS5-009, US-WVS5-008 §7.2-7.4].
- **Method of payment** [US-WVS5-009]:
  - Allowed: cash, check or money order, or direct deposit to an account the employee identifies.
  - The employer is not required to use direct deposit. An employee who gives no account details may be paid by payroll card.
  - Payroll card: the employer must give written fee disclosure, one free withdrawal per pay period and free in-network withdrawals, and must offer the direct-deposit option.
- **Notices.** At hire, written notice of the rate, payday and place of payment. Any change in rate, pay period or method needs written notice at least one full pay period before it takes effect [US-WVS5-008 §4, US-WVS5-009 21-5-9].
- Confidence: 90%. The minimum-wage figure is A.2; the statute was not read directly.

## 2. income_tax
- **Method (2026).** WV IT-100.2A, March 2026 [US-WVP51-005, re-verified]:
  - Taxable wage = gross − 2,000 per exemption annualised (weekly 38.46, biweekly 76.92, semimonthly 83.33, monthly 166.67, daily 7.66).
  - Two table sets: "Two earner/two or more jobs" is the default; "Optional one earner/one job" applies if box 5 of IT-104 is checked.
  - The optional annual table equals the statutory brackets: 10,000 / 25,000 / 40,000 / 60,000 at 2.11 / 2.81 / 3.16 / 4.22 / 4.58%.
  - The two-earner annual table is compressed: 7,500 / 18,750 / 30,000 / 45,000.
- **G-DERIVE.** I re-derived the bracket constants in Python [US-WVS5-012]:
  - Statutory/optional table: 211.00, 632.50, 1,106.50, 1,950.50.
  - Two-earner table: 158.25, 474.375 → 474.38, 829.875 → 829.88, 1,462.875 → 1,462.88.
- **Rates (SB 392, 2026).** SB 392 (2026) cut rates by 5% retroactive to 2026-01-01. It was signed on 2026-03-31, and 11-21-4j was codified effective 2026-06-12. Married-filing-separately brackets are half [US-WVS5-012].
  - The agency page does **not** state the date from which employers must apply the March 2026 tables (open question Q1).
- **Certificate.** WV IT-104, Rev. 03/2023, still linked as current for 2026 [US-WVS5-011]:
  - The federal W-4 is not used.
  - Fields: exemptions (self, spouse, dependents), the one-earner/one-job box, and additional withholding per pay period.
  - The IT-104NR certificate of nonresidence is on page 2.
- **Supplemental wages.** No flat rate. Supplemental pay is withheld through the annual table using the aggregate (standard pay × periods) method [US-WVP52-007, status partial]. IT-100.2A and TSD 381 contain no supplemental rate (open question Q2).
- **Rounding.** The tables give cents. No rounding rule was found in IT-100.2A or TSD 381 (open question Q2).
- **Wages subject to withholding.** Anything subject to federal withholding is subject to WV withholding. This includes bonuses, vacation allowances, back pay, tips and retroactive increases [US-WVS5-010].
- **Residents and nonresidents.** Employers must withhold from residents and nonresidents alike, and nonresident employers too [US-WVPIT-001, US-WVS5-010]. The exceptions:
  - **Reciprocity:** residents of KY, MD, OH, PA and VA with IT-104NR on file [US-WVS5-010, US-WVS5-011, US-WVP51-001].
  - **30-day rule:** a nonresident whose WV duties last 30 days or less, are performed in more than one state, and who is not an athlete, entertainer or public figure.
  - **Military:** nonresident Armed Forces members (not National Guard under 32 USC 502), and MSRRA spouses via IT-104NR.
  - **Allocation:** by time-and-attendance system or by the employee's written statement of expected WV days [US-WVS5-010].
  - **Nonresident credit:** only under a written agreement between the states [US-WVP51-002].
- **Local.** There is no local income tax. Municipal per-employee weekly **service fees** under 8-13-13 are withheld by the employer and remitted to the city [US-WVR3-001, US-WVR3-002]:
  - Charleston: 3.00 USD/week, confirmed on a city document dated 12/2022.
  - Other cities appear only at tier B: Huntington 5.00, Wheeling 2.00, Morgantown 3.00, Parkersburg 2.50, Fairmont 2.00, Chester 2.00, Weirton 2.00, Romney 1.00 [US-WVR3-003, US-WVP7-003/-004, MANUAL]. No ordinance was read in this run (open question Q3).
- Confidence: 85%. The method and rates are A.2 and current. Supplemental pay, rounding, the table start date and the city fees remain open.

## 3. social_security
- **SUI wage base.** **9,500 USD** per employee per calendar year, effective 2024-07-01 and unchanged for 2026 [US-WVS5-001]:
  - Fixed by SB 841 (2024), replacing the 2009 indexed "threshold wage", which gave 9,521 in 2024 per the handbook.
  - The 2025 Wayback copy of 21A-1A-28 still shows the old text, which is stale. US-WVS5-001 supersedes US-WVP52-002, which had no local file.
  - HB 4401 (2026) would have modified the base. It died in House Finance on 2026-01-16 [US-WVS5-018].
- **New employer rate.** 2.7% for 36 months [US-WVS5-002].
- **Foreign construction-trade entities.** 7.5% under 21A-5-5(c), **plus a 1% surtax** under 21A-5-10(b), giving **8.5%**. This reconciles the handbook's 8.5% with the statute [US-WVS5-015, derived].
- **Experience rates.**
  - Credit-balance employers: from 0.0% upward, taken from Table II by reserve ratio and fund-solvency column (C–F).
  - Debit-balance employers: 5.5 / 6.5 / 7.5%, plus the 1% surtax.
  - Overall range: 0.0–8.5% before the 2026 reduction.
  - Which solvency column applies in 2026 was not found on an agency page [US-WVS5-015, status partial].
- **2026 change (SB 1053).** From 2026-07-01 the contribution rate is reduced "by seven percent", and an annual automation and administration fee "equal to seven percent of the employer's total taxable wages for the twelve-month period ending the preceding June 30" applies [US-WVS5-002]:
  - The fee is billed by March 31 and capped at 18 million USD a year.
  - It ends at 60 million USD collected or on 2031-07-01.
  - It is employer-only; there is no employee deduction.
  - The literal text (7% of taxable wages) and the design (a 7% shift of contributions) diverge (open question Q4). The net-effect ambiguity in US-WVP7-001 stays.
- **Employee UI contribution.** None [US-WVP52-004].
- **SDI / TDI / PFML.** None. WV is not among the 13 states plus DC with a paid family and medical leave programme [US-WIR3-004]. SB 114 (2026), a paid parental leave pilot, covers state employees only; it comes from a tier-B search summary and was not read.
- **Employer levies.** Use the P7/P9 rows (US-WVP7-001..004, US-WVL-002).
- **MULTI hand-off.** SUI wages paid in another state on which contributions were paid **count toward the WV 9,500**, and so do predecessor wages [US-WVS5-001]. This answers MULTI-OQ-2: YES. MULTI-OQ-3 (PFML) is not applicable.
- Confidence: 85%.

## 4. payslip_statute
- **Content (42 CSR 5 §7.3, effective 2019-07-01, sunset 2029-07-01).** An itemized statement of earnings on the scheduled payday [US-WVS5-008]. It must show:
  - hourly rate or salary;
  - hours paid;
  - overtime rate, if applicable;
  - bonus or incentive pay, if applicable;
  - itemized deductions.
- **Statute.** 21-5-9(4) requires an itemized statement of deductions each pay period [US-WVS5-009, US-WVR3-004].
- **Corrections to earlier rows.**
  - US-WVLAB-001 (MANUAL) attributed the earnings statement to 21-5-3. The correct source is 42 CSR 5 §7.3, so it is superseded by US-WVS5-008.
  - The itemization source that US-WVP51-008 marked "not located" is now found.
- **Delivery.** Paper, or electronic if the employee has direct, immediate and convenient electronic access. No separate consent rule [US-WVS5-008].
- **Retention.** Payroll and employment records are kept at least **5 years**. They hold name or ID, home address, date of birth if under 18, occupation, regular rate, daily and weekly hours, and work-authorization documents. Records must be available to the Division within 72 business hours [US-WVS5-008 §5-6].
- **SSN truncation.** No state rule found (see §12).
- **Reach (MULTI-OQ hand-off).** Article 5 applies to anyone "doing business in this state", meaning having employees actively engaged in WV (21-5-1(n)) [US-WVS5-009]. Pay-statement duties therefore follow work performed in WV.
- Confidence: 90%.

## 5. reporting_instruments
- **Withholding.**
  - Remit by the 15th of the following month.
  - IT-101Q is due on the last day of the month after each quarter, even with nil activity. Its fields are listed in US-WVS5-014.
  - Annual filers (IT-101A, due Jan 31): employers withholding less than 600 USD a year, or certain domestic/household employers [US-WVS5-010, US-WVS5-014].
  - IT-101Q bulk filing via MyTaxes for periods after 2025-12-31.
- **Year end.** IT-103 reconciliation plus the state W-2 copies are due **January 31** [US-WVS5-010, US-WVS5-013]:
  - **Format:** EFW2 only, in 512-byte records with the RS record (state code "54") and a WV-specific **RV** record carrying the IT-103 totals, with money fields that differ from EFW2.
  - **Upload:** via MyTaxes after a Letter of Intent.
  - **Edition:** the IT-105 2025 spec is the latest listed; a 2026 edition is not yet out (open question Q6).
- **E-file mandate.** Employers filing for 10 or more employees, or using a payroll service, for periods after 2024-12-31. The penalty is 25 USD per return [US-WVS5-010, US-WVS5-013].
  - Conflict: the 2025-10-02 Wayback copy of 11-21-74 says 25/50 [US-WVP51-003]. That copy is probably stale, as happened with 21A-1A-28. Use 10, as stated by two agency documents (open question Q7).
  - Separately, anyone remitting any single business tax of 50,000 USD or more in the prior fiscal year must pay and file electronically.
- **UI quarterly wage report.** Due Apr 30, Jul 31, Oct 31 and Jan 31 via the UC Employer System, reporting wages in the quarter paid [US-WVUI-001]. The report carries name, SSN, gross wages, SOC or job title, county and monthly employee counts. US-WVS5-016 lists which wages to include or exclude.
- **New hire.** Report to the WV New Hire Reporting Center **within 14 days** of hire, regardless of hours [US-WVS5-016]:
  - Rehires count if the person was not employed in the prior 60 days.
  - Fields: full name, mailing address, date of birth and SSN. An employee without an SSN must apply within 7 days and give the employer a copy.
  - The employer FEIN and address fields were not listed in the handbook.
- **Registration.** Register via business4wv.gov. Domestic employers paying each worker less than 1,000 USD a quarter need not register [US-WVS5-016].
- **Power of attorney.** WV-2848 for tax [US-WVP51-006]; WorkForce WV POA for UI [US-WVP52-006].
- Confidence: 85%.

## 6. leave
- **Paid sick leave.** No WV private-sector paid-sick-leave statute was found in Ch. 21 Art. 5 or 5C, or in 42 CSR 5. Employers must only post their vacation and sick-leave policies (21-5-9(3)) [US-WVS5-009]. This is a negative finding from the instruments read; no general sweep of Ch. 21 was possible because of the geo-block (open question Q5). MULTI-OQ-4: not applicable unless Q5 finds otherwise.
- **PFML.** None (§3).
- **Accrued leave as wages.** Accrued fringe benefits, including vacation, sick leave and holidays, are "wages" for final pay when they can be calculated and are payable directly, according to the employer-employee agreement [US-WVS5-009].
- **Other paid leave.** SB 114 (2026) paid parental leave pilot for state employees only (tier B, not read). Nothing else with a pay impact was found.
- Confidence: 70%.

## 7. termination
- **Final pay.** For discharge **and** resignation, wages are due **on or before the next regular payday** [US-WVS5-003]:
  - Layoff or suspension due to a labour dispute: also the next regular payday.
  - Payment by mail if the employee requests it; the postmark date counts.
  - Penalty: liquidated damages of 2× the unpaid amount.
- **Vacation payout.** Payable if the accrued benefit can be calculated and is payable directly, per the employer's policy or agreement [US-WVS5-003, US-WVS5-009]. Benefits deferred by agreement follow the agreement.
- **Unreturned property.** A deduction for unreturned employer property worth more than 100 USD is allowed only with all of these [US-WVS5-003]:
  - a signed, itemized agreement;
  - a written demand;
  - a return window of up to 10 business days;
  - escrow if the employee objects.
  - It does not apply under collective bargaining agreements.
- **UI separation notice.** Not located as a mandatory employer notice. The employer must return separation and wage information requests within 4 days [US-WVS5-016].
- **WARN-style law.** Not researched (not payroll-relevant under the brief).
- Confidence: 85%.

## 8. benefits_in_kind
- **Withholding base.** WV withholding follows the federal definition of wages [US-WVS5-010], so the federal exclusions (401(k), §125, HSA, transit, group-term life) carry over for withholding. No WV departure was found in the instruments read.
- **UI base (differs from income tax).**
  - Gross pay **includes** 401(k) and cafeteria-plan deductions.
  - It **excludes** employer-paid 401(k) match and insurance.
  - Required on-site meals and lodging are included if worth 25% or more of total compensation.
  - Sick pay is included for the first 6 months [US-WVS5-016].
  - 21A-1A-28(b)(2)–(10) lists the statutory exclusions (retirement, sickness or accident plan payments, 401(a) trust payments, and others) [US-WVS5-001].
- **Minimum-wage meal credit.** 4.00 USD/day [US-WVS5-007].
- Confidence: 75%. The PIT conformity statute 11-21-12 was not read.

## 9. deductions_garnishments
- **Authorized deductions.** Only those required by law, or written authorizations for union dues, pension, savings, credit union, charity or insurance. Public employees: no union dues, except grandfathered municipal collective bargaining agreements. Anything else needs a written wage assignment [US-WVS5-009, US-WVS5-008 §9]:
  - valid for at most 1 year;
  - accepted by the employer;
  - 75% of net wages exempt;
  - not allowed while a garnishment over 25% of net is in effect.
- **Creditor garnishment (suggestee execution, 38-5A-3).** Stricter than the CCPA [US-WVS5-006]:
  - 20% of wages after taxes.
  - It applies only if weekly net pay exceeds 50× the federal minimum wage (50 × 7.25 = **362.50 USD/week**, derived), and it may never reduce pay below that floor.
  - One execution at a time, in priority order; each lasts up to 1 year.
- **Child-support IWO and state tax levy.** Not read; WV BCSE specifics are an open question (Q8).
- Confidence: 75%.

## 10. collective_agreements / prevailing wage
- The state prevailing-wage law (21-5A) was **repealed in 2016** [US-WVP51-009]. There is no state certified-payroll duty; federal Davis-Bacon applies on federal projects (FED unit).
- Confidence: 90%.

## 11. indexation
- **Minimum wage:** not indexed; 8.75 is fixed.
- **SUI wage base:** fixed at 9,500 since 2024; it moves only if the FUTA base exceeds 9,500 [US-WVS5-001]. The earlier average-wage indexation was repealed by SB 841.
- **PIT brackets:** not indexed. Changes come by statute (SB 392 2026, 5% cut) [US-WVS5-012].
- **Exemption:** 2,000 USD, fixed [US-WVPIT-001].
- **Garnishment floor:** follows the federal minimum wage [US-WVS5-006].
- **UI solvency column:** set yearly by the fund level on January 1 [US-WVS5-015].
- Confidence: 85%.

## 12. data_protection
- No WV rule on SSN truncation on pay statements was found in Art. 5 or 42 CSR 5. The required record content allows an "identifying symbol or number" instead of the name [US-WVS5-008].
- Not researched further (open question Q9).
- Confidence: 50%.

## 13. live_legal_change (sweep 2026-01-01 → 2026-11-02)
| Instrument | Status | Payroll effect | register_id |
|---|---|---|---|
| SB 392 (2026), 11-21-4j | Enacted; signed 2026-03-31; codified 2026-06-12; retroactive to 2026-01-01 | PIT 5% cut; new IT-100.2A (March 2026) | US-WVS5-012 |
| SB 1053 (2026), 21A-5-5(d), 21A-9-10 | Enacted; passed 2026-03-14; effective 2026-07-01 | UI rate −7%; annual fee "7% of taxable wages" (Q4) | US-WVS5-002 |
| HB 5485 (2026) minimum wage | Introduced; died in committee (2026-02-13) | None | US-WVS5-017 |
| HB 4401 (2026) UI wage base | Introduced; died in committee (2026-01-16) | None | US-WVS5-018 |
| SB 114 (2026) paid parental leave pilot | Reported signed 2026-02-28 (tier B, not read) | State employees only | none |

**Sweep scope.**
- Covered: 2 web searches, the tax.wv.gov rate-cut page and forms page, and two bill-status pages.
- Not covered: a full per-bill sweep of the 2026 enrolled acts list, and WorkForce WV news (open question Q10).

## Special populations (US-OWN-005, state round)
| Population | WV rule | register_id |
|---|---|---|
| Domestic / household | UI: no registration if each worker is paid < 1,000 USD per quarter. Withholding: annual filing permitted. Minimum wage: only if 6+ employees at the location; family excluded | US-WVS5-016, US-WVS5-010, US-WVS5-005 |
| Agricultural | Excluded from state minimum wage and overtime (FLSA definition of agriculture). UI: non-cash pay for agricultural labour is not wages | US-WVS5-005, US-WVS5-001 |
| Minors | Child-labour law 21-6 (DOL page exists) not read. Records keep date of birth if under 18. Training wage deferred to federal | US-WVS5-008, US-WVS5-007 |
| Tipped | Cash wage 2.62 USD/h (70% tip credit) with written tip records. Tip pool only among tip-eligible staff. UI: tips of 20 USD or more a month that are reported are wages | US-WVS5-007, US-WVS5-001 |
| Clergy / religious | No state rule beyond federal (WV withholding follows federal withholding) | US-WVS5-010 |
| Students | Part-time students are excluded from state minimum wage. UI excludes enrolled student workers | US-WVS5-005, US-WVS5-016 |
| Nonresident aliens | No state rule beyond federal located; follows federal wage definition | US-WVS5-010 |
| Statutory employees | No state rule beyond federal located | US-WVS5-010 |
| Government employees | The State and political subdivisions are "employers" under the minimum-wage law. Union dues cannot be deducted for public employees (grandfathered municipal CBAs excepted). State-employee overpayment assignment allowed, 25% of net exempt. UI reimbursable option | US-WVS5-005, US-WVS5-009, US-WVS5-008, US-WVS5-016 |
| Seniors 62+ on Social Security | Excluded from the state minimum-wage law | US-WVS5-005 |
| Military / military spouses | Nonresident Armed Forces members are not withheld; MSRRA spouses via IT-104NR | US-WVS5-010, US-WVS5-011 |

## Row status changes proposed for the synthesis
- **US-WVLAB-001 (MANUAL):** superseded by US-WVS5-008. The itemized earnings statement is in 42 CSR 5 §7.3, not 21-5-3.
- **US-WVP52-002:** superseded by US-WVS5-001 (same 9,500, now with the enrolled act held locally).
- **US-WVP52-001 / US-WVP7-001:** the local copy of SB 1053 is now US-WVS5-002, held locally; the ambiguity remains.
- **US-WVP52-003 / US-WVP52-004:** the conflict between 7.5% and 8.5% is resolved: 7.5% plus the 1% surtax (US-WVS5-015).
- **US-WVPIT-002 (MANUAL):** replaced by US-WVS5-011 (IT-104) and US-WVP51-005 (IT-100.2A). IT-100.1A returns 404 live; the current set is IT-100.2.A and IT-100.2.B.
- **US-WVPIT-003:** the local copy is US-WVS5-012.
- **US-WVP51-004 (MANUAL):** the e-file threshold of 10 employees is confirmed by TSD 381 Rev. 09/2025 (US-WVS5-010).

## ACCESS gaps
- `https://code.wvlegislature.gov/*` returns a 302 to `https://www.fbi.gov/investigate/cyber` from a non-US IP (VPN off). Retry with the US exit for:
  - 21-5C-2 (minimum wage);
  - 21-5-1 (current);
  - 21A-5-5 (2026 text);
  - 11-21-74 (current e-file thresholds);
  - 11-21-12 (PIT conformity);
  - 48-14 (income withholding).
- `https://web.archive.org/web/2026id_/https://code.wvlegislature.gov/pdf/21-5C-2/` and `.../pdf/21-5-1/`: timeout (HTTP 000) twice.
- `https://bills.wvlegislature.gov/bill/history/2026/RS/HB5485`: 403, Cloudflare bot check. I used the classic Bill_Status page instead.
- `https://tax.wv.gov/Documents/Withholding/it100.1a.pdf`: 404. The document has been withdrawn; IT-100.2A and IT-100.2B replace it.

## Open questions
- **Q1.** The date from which employers must apply the March 2026 IT-100.2A tables. The tax cut is retroactive to 2026-01-01, but the agency does not say whether employers should adjust withholding retroactively. What would close it: a WV Tax Division employer notice or administrative notice on SB 392 withholding (Tax Division, Legal/Policy).
- **Q2.** Supplemental-wage method and rounding rule. Only US-WVP52-007 (partial, fetch extract) holds the aggregate method. What would close it: a browser read of the Withholding "Help and General Information" page, or 110 CSR 21 (withholding regulation) on apps.sos.wv.gov.
- **Q3.** Municipal service-fee ordinances other than Charleston (Huntington, Wheeling, Morgantown, Parkersburg, Fairmont, Weirton, Chester, Romney): amounts and dates for 2026. What would close it: each city's ordinance or finance-office page. This work is **parallel** — one lookup per city, so it can be fanned out.
- **Q4.** SB 1053, 21A-9-10(c)(1): is the fee 7% of *taxable wages* (literal text) or 7% of *contributions* (design)? And what is the net effect with the 7% rate reduction? What would close it: the WorkForce WV employer notice or March 2027 fee invoice instructions (WorkForce WV Contribution Accounting, uctaxunit@wv.gov).
- **Q5.** Absence of a private-sector paid-sick-leave law and of local minimum wages. This rests on the instruments read. What would close it: a full read of the W. Va. Code Ch. 21 table of contents (code.wvlegislature.gov, US exit), or a DOL statement.
- **Q6.** IT-105 W-2 specification for tax year 2026. Only the 2025 edition is listed. What would close it: tax.wv.gov Withholding Tax Forms page in December 2026 or January 2027.
- **Q7.** The current statutory e-file thresholds in 11-21-74. The Wayback copy says 25/50; TSD 381 and IT-105 say 10 and payroll services. What would close it: the current 11-21-74 text (US exit) or the session law that amended it.
- **Q8.** Child-support IWO specifics: employer fee, priority and the 48-14 limits. What would close it: the WV Bureau for Child Support Enforcement employer page (bcse.wv.gov) and W. Va. Code 48-14-406.
- **Q9.** SSN truncation and payroll-record privacy rules. What would close it: the W. Va. Code 5A-8-22 / 46A-2A data-breach and SSN statutes (US exit).
- **Q10.** The full 2026 enrolled-acts sweep, and any 2027 enacted change. What would close it: the WV Legislature "Bills passed 2026 RS" list filtered on Ch. 11-21, 21, 21A and 38-5A, plus the 2026 first and second extraordinary sessions.

# Stage 5 — KY (Kentucky): findings across the 13 domains

Worker: compliance-source-hunter, 2026-11-02, 07:39–08:10 BRT. Declared budget: 60 fetches / 2 h. Used about 44 network calls (fetches, Wayback retries and 6 web searches) and about 35 minutes. Fetching stopped at the 75% fetch mark.
Shard: `00-official-sources/_register-shards/S5-KY.csv` (US-KYS5-001..026: 25 active, 1 MANUAL). Sources: `00-official-sources/ccg-sources/KY/` (23 files, 532,586 bytes, none over 100 KB).
Reused active rows (not re-fetched): US-KY-001/-002, US-KY-P5-1-001, US-KY-P5-2-001 (withholding guide and 2026 formula), US-KY-003, US-KY-P5-1-002 (UI 2026), US-KY-P5-2-002 (DOR does not administer local taxes), US-KY-P5-2-004 (prevailing wage repealed), US-KYR3-001..003 (no SDI/TDI/PFML), US-KYP7-001, US-KYP9V-001/-002 (levies), US-KYP8-001..003 (pay statement, records, posting), US-KYP9W-001/-002 (Louisville Metro OLT), US-KYP9L-001 (posters), US-MULTI-009 (reciprocity).

**Access finding.** The VPN was off (exit IP in Brazil). `apps.legislature.ky.gov` timed out on every direct call. The Wayback form `https://web.archive.org/web/2026id_/https://apps.legislature.ky.gov/law/statutes/statute.aspx?id={id}` returned the LRC PDF for every statute but one. LRC statute ids change when a section is amended, so an id that still appears in the 10/2026 chapter index means the older capture holds the current text. Chapter indexes are at `chapter.aspx?id=` (141 = 37674, 337 = 38890, 341 = 38902, 405 = 39225, 427 = 39299, 118 = 37589). Other workers can reuse this route.

## 1 — labour_code
- **Minimum wage:** USD 7.25/h from 2009-07-01 (KRS 337.275(1)). It rises automatically with any increase of the federal 29 USC 206(a)(1) rate. No 2027 state increase is enacted. [US-KYS5-001, A.1, high]
  - Tipped employees can be paid the federal tipped cash wage (29 USC 203; the amount is in the FED unit), with records proving tips plus wage reach the minimum (337.275(2)).
  - **The tipped-employee definition changed on 2026-04-10** (2026 Ky. Acts ch. 72; HB 185 per a tier-B lead). A tipped employee must receive more than USD 30/month in tips AND do work that directly supports the tipped service function. [US-KYS5-021, A.1]
- **Local minimum wage:** none in force. The 2016 Kentucky Supreme Court decision that struck down Louisville's ordinance is known only from tier B, so no row was registered. → Q6.
- **Overtime:**
  - 1.5x for hours over 40 in a workweek (KRS 337.285(1)). Exempt: retail selling, restaurant/hotel/motel staff, certain FLSA 213(b) classes, residential child-care, third-party companionship workers. County/city employees and Trooper/CVE R class may take comp time (240/480 h caps; payout at termination at the higher of the 3-year average rate or the final rate). [US-KYS5-002, A.1, high]
  - **KY-specific 7th-day rule:** 1.5x for time worked on the 7th day of a workweek, unless the employee is not allowed to work over 40 h that week. Overtime already paid for the same hours is credited (KRS 337.050). [US-KYS5-003, A.1, high]
- **Pay frequency:** at least semimonthly. Pay covers wages earned up to a day not more than 18 days before payday. An absent employee is paid within 6 days of demand. Exempt executive, administrative and professional staff are excluded (KRS 337.020). [US-KYS5-004]
- **Method of payment:** legal tender, check, direct deposit or payroll card (KRS 337.010(1)(c)1). Payroll cards: no activation fee, and at least one free withdrawal per pay period up to the full balance. The statute has no explicit employee-consent clause for direct deposit. [US-KYS5-006, A.1]
- **Breaks:**
  - Lunch: a reasonable period between the 3rd and 5th hour of the shift (KRS 337.355).
  - Rest: a **paid** 10-minute break per 4 hours worked, with no pay reduction (KRS 337.365). [US-KYS5-015]
- **Tips:** the employer may not keep tips except for required withholding. Tip pools may include tipped employees but not salaried staff, managers or supervisors (KRS 337.065, effective 2026-04-10). [US-KYS5-008]

## 2 — income_tax
- **Rate:** flat 3.5% for taxable years from 2026-01-01 (KRS 141.020(2)(f)). [US-KYS5-009, A.1, high]
  - **2027:** the rate drops only if the State Budget Director's September report finds the reduction conditions met AND the General Assembly acts. Otherwise the department keeps 3.5%.
  - The section's text is dated 2025-06-27. The chapter index ("through the 2026 Regular Session", updated 10/19/2026) shows no later version. HB 152 (2026 RS, graduated rates from 2027) stalled in committee (tier-B lead).
  - **2027 rate = 3.5% on the statute text.** The 2026 Budget Director report was not read. → Q1.
- **Method:** the 2026 formula [US-KY-002 / US-KY-P5-2-001]: (period wage × periods − 3,360) × 3.5% ÷ periods. The 2026 standard deduction (3,360) is indexed under KRS 141.081(2)(a).
- **Formula arithmetic, checked in Python:**
  - Monthly 3,270: 1,255.80 a year, 104.65 a month.
  - Bi-weekly 1,500: (39,000 − 3,360) = 35,640 × 3.5% = 1,247.40 a year. **The "35,730" printed on the sheet is a typo: 35,640 × 3.5% gives the printed 1,247.40, while 35,730 × 3.5% gives 1,250.55.**
  - Per period: 1,247.40 ÷ 26 = 47.98. The sheet shows "47", which no stated rule explains.
  - "Extra 117.60 for more than one W-2" = 3,360 × 3.5% exactly.
  - Verification method: derived arithmetically.
- **Rounding rule:** KRS 141.310(4) lets the employer compute **wages** to the nearest dollar. It sets no rounding for the tax. [US-KYS5-010, A.1]
- **Supplemental:** there is no separate supplemental rate. Bonuses and severance are withheld through the same formula [US-KY-P5-1-001]. Film-incentive companies withhold at the maximum 141.020 rate (141.310(17)).
- **Certificate:** Form K-4 (42A804). It has no allowances and is used only for exemption claims [US-KYS5-013]:
  - no prior-year and no expected current-year liability;
  - Fort Campbell pay of a nonresident;
  - SCRA/MSRRA;
  - residents of the reciprocal states.
- **Withholding treatment by payment type:** the 42A003 chart (33 types). → Domain 8 [US-KYS5-023].
- **Residents and nonresidents:**
  - Nonresidents are taxed only on income from labour performed in KY; part-year residents are split (KRS 141.020(4),(6)) [US-KYS5-009].
  - Out-of-state employers withhold on nonresidents' KY-earned wages, except reciprocal-state residents (103 KAR 18:010(2), quoted in 42A003). They may voluntarily withhold for KY residents working outside KY [US-KYS5-023].
- **Reciprocity:** IL, IN, MI, WV, WI; VA only for daily commuters; OH unless the employee is a 20%+ S-corp shareholder. Nonresidence certificate 42A809 [US-MULTI-009, US-KY-001].
- **Credit for tax paid to other states:** KRS 141.070. It works at **assessment**; the section text was not read. Listed in the chapter index (id 53502).
- **Local occupational license taxes** (work-location based; separate returns to each locality; DOR does not administer them [US-KY-P5-2-002]):
  - **Louisville Metro** [US-KYP9W-001/-002]:
    - All wages earned in Louisville Metro: 1.25% Metro + 0.20% TARC = 1.45%.
    - Residents also pay 0.75% for the school boards: 2.2% in total.
    - Returns: W-1 quarterly, W-1D monthly if more than 3,000 in a quarter, W-3 by Feb 28.
  - **Lexington-Fayette (LFUCG)** [US-KYS5-024, A.2, high]:
    - 2.25% of compensation, withheld by the employer.
    - Form 220-221 quarterly (preprinted forms mailed in January; not available online or by fax); monthly if quarterly withholding exceeds USD 300.
    - Form 222 annual reconciliation.
    - The page's withholding base (e.g. whether Section 125 contributions are included) was not read. The tier-B lead says deferred compensation and 125 contributions are included. → Q4.
  - **Other cities, counties and school districts** levy their own taxes (KOLA list not read; US-KYP7-002 superseded). → Q3. Parallel work, see "Shape of remaining work".

## 3 — social_security
- **SUI 2026** [US-KY-003, US-KY-P5-1-002, US-KYS5-019, A.2, high]:
  - Taxable wage base 12,000.
  - New-employer rate 2.70%, so at most 324 per employee (12,000 × 2.7% = 324, checked).
  - Schedule A in 2026: 0.30%–9.00%.
  - No employee contribution.
  - SCUF 0% in 2026, 0.0115% inside the rate from 2027 [US-KYP7-001].
- **Wage base mechanics:** KRS 341.030(7). 9,000 from 2012, +300 each 1 January, capped at 12,000. Increases are suspended when the trust fund is below 200 million on 30 September.
  - **Derivation:** 11,400 (2024) + 300 = 11,700 (2025) + 300 = 12,000 (2026) = the cap.
  - So the **2027 base = 12,000** unless amended. [US-KYS5-012, A.1, derived arithmetically]
- **Multistate credit (MULTI hand-off):** wages already paid for "covered employment" count toward the KY base, and covered employment includes service covered under another state's UI law (KRS 341.030(7)(a)). **Yes: wages reported to another state count toward the KY 12,000 base, same worker, same year.** [US-KYS5-018, A.1, high]
- **Liability thresholds** [US-KYS5-019]:
  - non-agricultural: 1,500 in a quarter, or 1 worker in 20 weeks;
  - agricultural: 20,000 in a quarter, or 10 workers in 20 weeks;
  - domestic: 1,000 in a quarter;
  - 501(c)(3): 4 workers in 20 weeks.
  - Corporate officers are covered. The proprietor's spouse, parent and child under 21 are not.
- **SDI/TDI/PFML:** none. KRS 304.53 only allows voluntary group paid-family-leave insurance [US-KYR3-001..003]. **So the MULTI PFML/SDI question does not apply to KY.**
- **Workers' compensation:** mandatory private insurance. The premium may not be deducted from wages (KRS 342.630/.650, quoted in 42A003 [US-KYS5-013]).

## 4 — payslip_statute
- Employers with 10 or more employees that make deductions must, at each payment, give a paper or electronic statement of each deduction and its purpose. If the statement is electronic, the employer must provide access to a computer and printer (KRS 337.070, effective 2017-06-29). [US-KYP8-001, A.1, high]
  - No other content is required (gross, hours and rate are not mandated by the state).
  - **Reach to out-of-state work:** the text has no reach rule. Default to the work-location state (MULTI §4).
- **Retention:** pay and hours records kept for at least 1 year (KRS 337.320) [US-KYP8-002].
- **Annual statement:** W-2 by January 31, or on the day of the last wage payment if employment ends earlier (KRS 141.335) [US-KYS5-011].

## 5 — reporting_instruments
- **Withholding returns (MyTaxes, electronic filing and payment, all frequencies)** [US-KYS5-013, A.2, high]:

  | Annual KY tax withheld | Frequency | Return and due date |
  |---|---|---|
  | under 400 | annual | K-3 by Jan 31 |
  | 400–1,999 | quarterly | K-1 by the last day of the month after the quarter; Q4 on K-3 by Jan 31 |
  | 2,000–49,999 | monthly | K-1 by the 15th; December on K-3 by Jan 31 |
  | 50,000 or more | twice-monthly | 1st–15th due on the 25th; 16th–end due on the 10th of the next month |

  - 100,000 or more accumulated in a period: pay within one banking day by EFT (103 KAR 1:060).
  - Zero returns are required.
- **W-2 to DOR** [US-KYS5-013, US-KYS5-011]:
  - Due Jan 31, via MyTaxes (as transmitter) or CD.
  - Format: **SSA EFW2 with a DOR-defined RS record**, or Form K-5. Electronic filing is mandatory at 26 or more statements (103 KAR 18:050(4)).
  - Paper W-2s are not processed. Corrections go on paper W-2c.
  - The RS-record specification itself was not fetched. → Q5.
- **Penalties** [US-KYS5-013]:
  - late filing or payment: 2% per 30 days, up to 20% (minimum 10);
  - W-2 not furnished: 25 each (minimum 100);
  - non-electronic filing: 10 per return.
- **UI quarterly wage report and payment** [US-KYS5-019]:
  - Filed in **KUIP** (replaced KEWES in 2026), due the last day of the month after the quarter. Zero reports are required.
  - Late-report penalties: 25/75 for the first, 125/175 for later ones. Interest: 1.5% a month.
  - The KUIP file-upload format was not read. → Q5.
- **New hire:** within 20 days for each hire, rehire or return from layoff, furlough or leave of an employee who resides or works in KY. Content: name, address, SSN; employer name, address, FEIN and state EIN; first day of work. Medium: a copy of the W-4 or the AG form.
  - **Recipient since 2025-07-01: Office of the Attorney General** (was CHFS; 2023 Ky. Acts ch. 124). [US-KYS5-020, A.1, high]
- **Registration:** combined Form 10A100 or MyTaxes. A withholding account is needed for 1 or more employees under IRC 3401 [US-KYS5-013]. UI registration is in KUIP.
- **Local:** Louisville W-1/W-1D/W-3 [US-KYP9W-002]; Lexington 220-221/222 [US-KYS5-024].

## 6 — leave
- **Paid sick leave:** no KY statute. The KRS 337 index and the Title XXVII chapter list have no sick-leave section [US-KYP8-001 index file, US-KYR3-001]. No local PSL ordinance was found; whether one is preempted was not read. → Q6.
  - **MULTI PSL coverage question: does not apply (no state PSL).**
- **PFML benefit interaction:** none (no programme) [US-KYR3-002].
- **Adoption leave:** up to 6 weeks on written request, for a child under 10. Paid leave and benefits given to birth parents must be matched for adoptive parents (KRS 337.015). [US-KYS5-016]
- **Voting:** at least 4 hours on election day (or to vote absentee at the clerk), applied for in advance; the employer sets the hours. Election officers get a full day. No pay rule in the text (KRS 118.035). [US-KYS5-025]
- **Court appearance:** no discharge for time off required by law (KRS 337.415); no pay rule. [US-KYS5-017]
- Jury (KRS 29A.160) and military leave (KRS 38.238/38.460) were not read. → Q7.

## 7 — termination
- **Final pay:** all wages earned by the later of the next normal payday or 14 days after separation. The same rule applies to discharge and resignation (KRS 337.055). [US-KYS5-005, A.1, high]
- **Vacation:** "wages" include **vested** vacation pay and earned bonuses (KRS 337.010(1)(c)1), so vested vacation is part of final pay under 337.055. Forfeiture-policy case law was not read. [US-KYS5-006, medium-high]
- **Compensatory time** of public employees is paid at termination at the higher of the 3-year average or the final rate (337.285(8)) [US-KYS5-002].
- **Separation notice:** none found. The 2026 OUI Employer Guide describes only the claim-driven UI-412A/UI-412 notices. → Q8.
- **State WARN law:** none located (not searched beyond the KRS 337 index).

## 8 — benefits_in_kind
- **IRC conformity:** the IRC as of 2025-12-31, for taxable years from 2026 (KRS 141.010(21), effective 2026-07-15). This covers P.L. 119-21 (enacted July 2025). KY decoupling in KRS 141.019/141.0101 was not read. [US-KYS5-022, A.1]
- **42A003 withholding chart (2026)** [US-KYS5-023, A.2]:
  - Withholding **not required** on: cafeteria/125 and flexible benefit plans, DCAP, health plans, group-term life*, 401(k)*, SEP*, federal TSP*, IRA, fringe benefits*, meals and lodging*, travel expenses*, pensions (voluntary only).
  - Withholding **required** on: company cars, moving expenses, severance, bonuses, vacation and sick pay*, tips over USD 20/month.
  - KY follows the federal exclusions; no PA/NJ-style departure was found. (* = federal conditions apply.)
- **Local bases may differ:** the Lexington base reportedly includes 125 contributions (tier-B lead). → Q4.

## 9 — deductions_garnishments
- **Wage deductions:** only those required by law, or written-authorised deductions for insurance, medical dues and the like. Union dues need written consent (CBAs from 2017-01-09). **Prohibited, even with consent:** fines, shared-till shortages, breakage, dishonoured checks, and losses from faulty work, theft or customer default unless wilful (KRS 337.060). [US-KYS5-007, A.1, high]
- **Garnishment limit:** the lesser of 25% of disposable earnings or the amount above 30 × federal minimum wage (217.50/week, checked). This is the same as the CCPA. Support orders, Chapter 13 orders and tax debts are outside it (KRS 427.010). [US-KYS5-014, A.1, high]
- **Child-support IWO:** 1 USD fee per payment; lump sums of 150 USD or more must be reported by employers with 20+ employees; termination notice. **Tier-B lead only** [US-KYS5-026, MANUAL]. Administered by the AG Office of Child Support Services since 2025-07-01.
- **State tax levy:** not researched. → Q9.

## 10 — collective_agreements
- State prevailing wage repealed in 2017 (KRS 337.505–.550) [US-KY-P5-2-004]. No state certified-payroll duty. Federal Davis-Bacon applies on federal projects (FED unit).

## 11 — indexation
| Item | Mechanism | 2026 value | Source |
|---|---|---|---|
| Standard deduction | Indexed annually by DOR (KRS 141.081(2)(a)), published on the yearly formula sheet 42A003 (TCF) | 3,360 | US-KY-002 |
| Income-tax rate | Trigger review (Budget Director, Sept 5) + General Assembly action | 3.5% (2027: 3.5% unless acted) | US-KYS5-009 |
| SUI wage base | +300/yr to the 12,000 cap; trust-fund suspension | 12,000 (cap reached) | US-KYS5-012 |
| SUI rate schedule | Trust-fund balance on Sept 30 → schedule A–E | Schedule A | US-KY-003 |
| Minimum wage | Follows the federal rate automatically | 7.25 | US-KYS5-001 |
| Garnishment floor | 30 × federal minimum wage | 217.50/week | US-KYS5-014 |

## 12 — data_protection
- No KY rule on truncating the SSN on pay statements was read. KRS 141.335 lists the employee's SSN as content of the annual statement. → Q10.
- KRS 341.190 (UI records confidentiality) and KRS 337.345 (wage-hour information confidentiality) appear in the indexes but were not read.

## 13 — live_legal_change (2026-01-01 to 2026-11-02)
- **2026 Ky. Acts ch. 72 (HB 185), effective 2026-04-10:** new tipped-employee definition and mandatory tip pools (KRS 337.010, 337.065). Operates on the minimum wage and tip-credit rules. Enacted, in force. [US-KYS5-021, US-KYS5-008]
- **KRS 141.010 amended, effective 2026-07-15:** IRC conformity moved to 2025-12-31. Enacted, in force. [US-KYS5-022]
- **TY2027 rate:** stays 3.5% on the enacted text. HB 152 (2026 RS) did not pass committee (tier-B lead). The Sept 2026 Budget Director report could support a 2028 cut. Operates at withholding. [US-KYS5-009]
- **SCUF returns at 0.0115% (inside the rate, no extra cost) from 2027-01-01**, under SB 129 [US-KYP7-001, US-KYP9V-001].
- **KUIP** replaced KEWES for UI tax in 2026 [US-KY-P5-1-002].
- **New-hire and child-support functions moved to the AG** from 2025-07-01 [US-KYS5-020].
- **Not done:** DOR and OUI news sweeps were not fetched separately (budget).

## Special populations (state level)
| Population | KY rule | register_id |
|---|---|---|
| Domestic / household | Excluded from state minimum wage/overtime unless more than one domestic is regularly employed. KY withholding not required. UI liable at 1,000 cash wages in a quarter | US-KYS5-006, US-KYS5-023, US-KYS5-019 |
| Agricultural | Excluded from state minimum wage/overtime. KY withholding follows the federal IRC 3121(a) test (cash under 150 and labour expense under 2,500 excluded). UI at 20,000 in a quarter or 10 workers in 20 weeks | US-KYS5-006, US-KYS5-023, US-KYS5-019 |
| Minors | Child-labour statute KRS 339 not read. No sub-minimum for minors in KRS 337.275 | Q7 (open) |
| Tipped | Federal tipped cash wage permitted. New definition from 2026-04-10. Tip pools (no managers). Tips over 20/month subject to withholding | US-KYS5-001, US-KYS5-021, US-KYS5-008, US-KYS5-023 |
| Clergy / religious | KY withholding not required. Religious/nonprofit camps operating 210 days or less are excluded from the minimum-wage chapter | US-KYS5-023, US-KYS5-006 |
| Students, learners, apprentices | Sub-minimum only with a commissioner certificate (KRS 337.010(2)(a)5) | US-KYS5-006 |
| Nonresident aliens | "Aliens": withholding required (federal NRA rules in the FED unit) | US-KYS5-023 |
| Statutory employees | Direct sellers (IRC 3508(b)(2)) excluded from the minimum-wage chapter. Withholding on statutory employees follows IRC 3401 (42A003 Q&A) | US-KYS5-006, US-KYS5-013 |
| Government employees | Federal employees and state employees under KRS 7/16/18A/27A/30A excluded from the minimum-wage chapter. County/city comp-time regime under 337.285(4)-(11) | US-KYS5-006, US-KYS5-002 |
| Small retail/service (under 95,000 gross) and family members | Excluded from the state minimum-wage chapter (FLSA may still apply) | US-KYS5-006 |
| Military / Fort Campbell | Nonresident pay at Fort Campbell exempt. SCRA/MSRRA spouses exempt on K-4 | US-KYS5-013 |

## MULTI hand-offs (answered for KY)
1. **SUI wage-base credit for wages reported to another state:** YES, KRS 341.030(7)(a) [US-KYS5-018].
2. **PFML/SDI coverage of multistate workers:** not applicable; KY has no programme [US-KYR3-001..003].
3. **Paid-sick-leave coverage:** not applicable; no KY PSL statute.
4. **Pay-statement reach:** KRS 337.070 has no territorial clause. Default to the work-location state [US-KYP8-001].

## ACCESS gaps (exact URLs)
- `https://apps.legislature.ky.gov/*`: every direct call timed out (VPN off, Brazil exit). Wayback worked except for:
  - `https://web.archive.org/web/2026id_/https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=56574` (KRS 405.465): 404.
  - `https://web.archive.org/web/2026id_/https://apps.legislature.ky.gov/law/kar/titles/040/001/410/` and `https://web.archive.org/web/2026id_/https://apps.legislature.ky.gov/law/kar/downloads/docs/18345/document.engrossed.pdf` (40 KAR 1:410): 404.
- `https://lexingtonky.gov/node/659`, `/node/660`: 404 (stale URLs). The current pages were read instead.

## Open questions
- **Q1** `pit.rate.flat` for TY2027. Statute: 3.5%. Would close it: the Office of State Budget Director 2026-09-05 report to the IJC on Appropriations and Revenue, plus the DOR 2027 formula sheet 42A003 (TCF)(10-2026) when published.
- **Q2** Official per-period rounding of the tax. The formula sheet's bi-weekly result "47" does not match 47.98 (rounded: 48); KRS 141.310(4) rounds only wages. Would close it: a DOR written answer, or a corrected 2026/2027 formula sheet (DOR Withholding Tax section).
- **Q3** Full list of KY local occupational license taxes (cities, counties, school districts) with rates and bases. Would close it: the Kentucky Occupational License Association / DLG local tax-rate list. These are independent per-locality lookups (count not established) and can be fanned out.
- **Q4** Lexington-Fayette withholding base (are 125/deferred contributions taxable?) and the Fayette County Board of Education tax. Would close it: LFUCG License Fee Regulations 5th ed. and Code ch. 13 (linked from the LFUCG page).
- **Q5** KY RS-record specification (EFW2) and the KUIP quarterly wage file layout. Would close it: the DOR Software-Developer page (`https://revenue.ky.gov/Software-Developer/`) and KUIP TPA file specs on ui.ky.gov.
- **Q6** Local minimum-wage / PSL preemption in KY. Would close it: the Kentucky Supreme Court opinion (Kentucky Restaurant Ass'n v. Louisville/Jefferson County Metro Gov't, 2016) on kycourts.gov, and any KRS 65 preemption section.
- **Q7** Jury duty (KRS 29A.160), military leave (KRS 38.238/38.460), child labour (KRS 339 / 803 KAR 1:100). Would close it: the LRC statute texts.
- **Q8** Any KY UI separation notice duty. Would close it: 787 KAR 1 index (OUI regulations).
- **Q9** KY DOR wage levy / garnishment priority. Would close it: KRS 131.500-.510 text.
- **Q10** SSN truncation on pay statements. Would close it: KRS 365.725-.734 / KRS 367 texts (LRC).
- **Q11** KRS 405.465 / 40 KAR 1:410 text (IWO fee 1 USD, lump-sum 150 USD) to lift US-KYS5-026 from MANUAL. Would close it: an LRC read with the US VPN on.

## Shape of remaining work
- Most open items are single LRC statute reads (Q6–Q11). They are cheap once the US VPN is on, since direct LRC access works then.
- Q3 (local occupational taxes) is naturally parallel across localities.

## Confidence
- State withholding, UI, labour code, final pay, garnishment: 90–95%.
- Local taxes: 75%. Two largest localities verified; the rest not listed.
- Reporting formats: 80%. RS-record and KUIP file specs not read.
- Overall KY: about 85%.

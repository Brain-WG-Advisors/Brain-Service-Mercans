# Stage 5 — Colorado (CO), 13-domain hunt

Worker run 2026-11-02, 07:32 to about 08:05 local. Budget declared at the start: 60 fetches / 2 h. Stopped acquiring at about 45 fetches and searches (75%).

- **New rows:** `00-official-sources/_register-shards/S5-CO.csv`, ids US-COS5-001..016 (16 rows: 12 active, 2 partial, 1 MANUAL). There are 15 rows on A.1/A.2/A.3 sources and 1 tier-B row (MANUAL).
- **Reused rows (active in `legal-basis-register.csv`, not re-fetched):**
  - US-CO-WH-001
  - US-CO-P5-1-001..006
  - US-CO-P5-2-001..003
  - US-CO-FAMLI-001
  - US-COL-001..004
  - US-COP7-001..006
  - US-COP9L-001
  - US-MULTI-023
- **Local re-reads (no fetch):** these files already on disk under `00-official-sources/pdfs/CO/` were re-read: Wage Act (rev. 2025-08-06), HFWA (rev. 2023-08-07) and the Wage Withholding Tax Guide (Jan 2026).
- **New source files:** 10 files (2.7 MB) in `00-official-sources/ccg-sources/CO/`.
- **Access:** cdle.colorado.gov, famli.colorado.gov, sos.state.co.us (CCR), coag.gov, childsupport.colorado.gov and content.leg.colorado.gov all return 403, 202-empty or a timeout to curl. denvergov.org returns a bot-rejection page; one release was read through Wayback. The Wayback CDX/availability API returned 429 or "Temporarily Offline" for part of the run. These hosts work: tax.colorado.gov, content.govdelivery.com (CDLE bulletins), coloradojudicial.gov, oui.doleta.gov, greenwoodvillage.com, glendale.co.us.

## 1 labour_code

**Minimum wage, 2026**
- State minimum wage 15.16 USD/h (COMPS Rule 3) [US-COS5-001].
- Tipped: tip credit up to 3.02 USD/h, so the tipped cash wage is 12.14 (15.16 − 3.02, derived). Tips must not be diverted to untipped staff, and service charges are not tips [US-COS5-001].
- Unemancipated minors may be paid 15% less. This does not apply under some local minimum wages [US-COS5-001].
- Vigência 2026-01-01..2026-12-31. The poster says "use new version released by each December".

**Local minimum wages, 2026**
- **Denver:** 19.29 USD/h; tipped food and beverage 16.27 with at least 3.02 in actual tips, from 2026-01-01 (D.R.M.C. ch. 58 art. 16). The rate is indexed by CPI-W Denver-Aurora-Lakewood (H1 vs H1), step 2.56%. G-DERIVE: 18.81 × 1.0256 = 19.2915, which rounds to 19.29; 19.29 − 3.02 = 16.27 [US-COS5-010].
- **Edgewater 18.17, City of Boulder 16.82, unincorporated Boulder County 16.82:** these figures are tier B only [US-COS5-011, MANUAL]. CDLE's PAY CALC Order (7 CCR 1103-14, adopted 2025-12-08, effective 2026-02-01, the official list of local minimum wages) is a 403 page.

**Minimum wage, 2027 (announced, not modelled)**
- State 15.71, tipped 12.69 (CDLE announcement of 2026-08-13, per leads).
- Denver 19.84.
- These are tier B only [US-COS5-011, MANUAL]. Two arithmetic checks are consistent: 15.71 − 3.02 = 12.69, and 15.71 / 15.16 = 1.0363 (the reported 3.6% step).

**Overtime (COMPS Rule 4)**
- 1.5× the regular rate after 40 hours/week, or after 12 hours/day, or after 12 consecutive hours [US-COS5-001].
- No comp time in lieu of overtime, and no averaging across weeks or days.
- Agriculture: overtime after 48 hours (56 at some highly seasonal sites).
- EAP exemption salary threshold 2026: 57,784 USD (updated yearly).
- Meal break: 30 minutes in shifts over 5 hours. Rest: a paid 10 minutes per 4 hours. Rest time not provided must be paid as extra pay [US-COS5-001].

**Pay frequency and pay day**
- Pay period no longer than one calendar month or 30 days, whichever is longer.
- Payday no later than 10 days after the period closes, unless agreed otherwise (C.R.S. 8-4-103(1)(a)). Paydays must be posted (8-4-107) [US-COS5-002].

**Method of payment**
- Checks must be negotiable without discount.
- Direct deposit only with the employee's voluntary authorisation, into the institution of the employee's choice.
- Paycard only with free access to the full net pay once per pay period, or with an alternative means available (8-4-102(1),(2),(2.5)) [US-COS5-002].

**Confidence:** High (state minimum wage, overtime, pay frequency, Denver); Low (other local minimum wages and 2027 values).

## 2 income_tax

**Method (DR 1098, 2026)** [US-CO-P5-1-001]
- Annualise the wages.
- Subtract 5,500 (11,000 MFJ/QSS), or the DR 0004 line 2 amount.
- Multiply by 4.40%, divide by the number of pay periods, and add DR 0004 line 3.
- There is no separate supplemental rate and no rounding rule.

**Certificate: IRS W-4 or the optional DR 0004 (2026 edition, rev. 10/29/25)** [US-COS5-012]
- Table 1 standard allowance by number of jobs:
  - Single/MFS: 14,000 / 7,000 / 4,500 / 3,500
  - Head of household: 22,000 / 11,000 / 7,500 / 5,500
  - MFJ/QSS: 30,000 / 15,000 / 10,000 / 7,500
  - Alignment confirmed on the raw text extraction.
- Worksheet 1 takes the federal qualified-overtime deduction (W-4 Step 4(b) worksheet line 1b) out of the additional deductions. Colorado does not follow the OBBBA overtime exclusion for withholding; the Guide states this too [US-COS5-007].
- If a W-4 claims exempt, pay exceeds 200 USD/week and no DR 0004 is filed, a copy of the W-4 goes to CDOR [US-COS5-006].

**Resident/nonresident** [US-CO-P5-1-002]
- Residents: Colorado tax is withheld on all wages, except wages for services in a state that requires its own withholding.
- Nonresidents: Colorado-source wages, apportioned by days present.
- Nonresident exemptions under federal law: rail, air (≤50% of pay in CO), motor carrier, military, military spouse. Telecommuters are not taxed on work performed outside Colorado [US-COS5-007].

**Reciprocity:** none. The Jan 2026 Guide has no reciprocity text (word search in the local file), and MULTI carries Colorado as "no explicit negative row, no partner lists CO".

**Local taxes (Occupational Privilege Taxes, flat monthly, each on a separate city return = T4)**

| City | Employee | Employer | Trigger | Remittance | Source |
|---|---|---|---|---|---|
| Denver | 5.75/month | 4.00/month | monthly pay ≥ 500 | Denver Treasury | [US-CO-P5-2-001; US-COP7-004/005] (2025 Tax Guide edition; the 2026 edition was not read) |
| Greenwood Village | 2/month | 2/month | ≥ 250 in the month | Xpress Bill Pay; OPT licence for every business in the Village | [US-COS5-015] |
| Glendale | 5/month | 5/month | > 750 in the month | monthly, quarterly and annual returns | [US-COS5-016] |
| Sheridan | 3/month | 3/month | ≥ 500 | — | tier C only [US-COP7-006, MANUAL] |

- Aurora's OPT was repealed in 2025 (corroborated only, per US-COP7-006).
- **Multiple-OPT-city rule (Greenwood Village page):** the tax goes to the city where the employee worked the most, and only the primary employer withholds [US-COS5-015].

**Confidence:** High (state); Medium-High (Denver, GV, Glendale); Low (Sheridan).

## 3 social_security

**State UI (CDLE)**
- Chargeable wage limit: 30,600 for 2026; 32,100 for 2027 [US-CO-P5-1-003].
- New-employer rate 2026: 1.53% + support surcharge 0.17% + solvency surcharge 1.35% = 3.05% (non-construction). Heavy construction 6.285%.
- 2027 new-employer rate: 1.70% combined, no solvency surcharge [US-CO-P5-1-004].
- Experienced-employer support surcharge [US-COL-004, MANUAL; US-COP7-002/003, MANUAL].
- No employee share [US-CO-P5-1-003].

**UI coverage**
- Colorado follows the FUTA thresholds: employer 20 weeks / 1,500; agricultural 10 workers in 20 weeks / 20,000; domestic 1,000 per quarter.
- Excluded: commission insurance and real-estate agents, casual labour, part-time work for tax-exempt nonprofits, and students working for their school.
- Source: DOL Comparison of State UI Laws 2023 [US-COS5-014, partial: 2023 edition].

**FAMLI**
- 2026: 0.88% of wages, 0.44% employer + 0.44% employee, on wages up to the Social Security wage base (184,500 for 2026, from FED). Statutory cap 1.2% [US-CO-FAMLI-001].
- 2027: 0.86% from 2027-01-01, per the CDLE FAMLI Business Brief of 2026-09-30 [US-COS5-008].
- The 2027 split and the under-10-employee exemption from the employer share were not read on a primary page [US-COP7-001, MANUAL].
- Quarterly wage report and premium go through My FAMLI+ Employer, due one month after quarter end (Q3 2026 due 2026-10-31). There are published file and API specifications. ITINs are allowed in bulk files from 2026-10-01 [US-COS5-008].

**Other levies:** P7 list (US-COP7-*); no other state levy.

**Confidence:** High (UI base, new-employer rates, FAMLI rates); Medium (coverage, 2023 edition).

## 4 payslip_statute

**Wage Act** [US-CO-P5-1-005]
- An itemized written statement at least monthly or with each payment.
- Content: gross wages, all withholdings and deductions, net wages, pay-period dates, employee name **or SSN**, employer name and address (C.R.S. 8-4-103(4)).
- Records kept 3 years (4.5). Fine up to 250 USD per employee per month, maximum 7,500.

**COMPS Rule 7 adds more content** [US-COS5-001]
- Per the poster, the statement must show total pay, rate, tips, credits and time worked, kept 3 years.
- The PSL must therefore carry the hourly rate, hours worked, tips and credits in addition to the Wage Act items.

**Electronic delivery:** no Colorado statute or rule on electronic consent was read. Open question.

**Confidence:** High (content); Low (electronic delivery).

## 5 reporting_instruments

**Withholding** [US-COS5-006]
- Account at mybiz.colorado.gov or CR 0100.
- Return frequency by annual withholding:

| Annual withholding | Frequency | Due |
|---|---|---|
| < 7,000 | quarterly | last day of the month after the quarter |
| 7,000–50,000 | monthly | 15th of the following month |
| ≥ 50,000 | weekly (Sat–Fri) | 3rd business day after the Friday; EFT mandatory |

- Zero returns are required for monthly and quarterly filers. Paper return DR 1094.
- Penalty interest 2026: 8% discounted / 11% regular (withholding-tax-guide page, read, not registered).

**W-2** [US-COS5-006, US-COS5-013]
- Due to employees and to CDOR by January 31.
- E-filing to CDOR is mandatory when the employer must e-file federally (10+ W-2s). Upload in Revenue Online as a .txt file, or as the CDOR XLSX template for employers with 10–100 employees (tax year 2026, filed in 2027). The template's field list and validation rules are in the row.
- Paper filers send W-2s with the DR 1093 transmittal. Penalty 5–50 USD per W-2.
- Annual DR 0995 refundable-credit notice to every employee, in English plus the language the employer usually uses.

**UI and FAMLI**
- UI quarterly wage report: not read (CDLE 403). The format and due date stay open. Third-party (TPA) authorisation is in MyUI Employer+ [US-CO-P5-2-003].
- FAMLI quarterly report: see domain 3 [US-COS5-008].

**New hire:** not read (childsupport.colorado.gov timed out twice). The federal default applies: 20 days, under 42 U.S.C. 653a [US-FEDS5-024]. Any Colorado-specific fields or method are open.

**POA:** DR 0145 [US-CO-P5-1-006].

**Confidence:** High (withholding, W-2); Low (UI wage report, new hire).

## 6 leave

**HFWA (C.R.S. 8-13.3-403/-404)** [US-COS5-005, partial: 2023 text]
- Applies to all employers since 2022-01-01.
- Accrual: 1 hour per 30 hours worked, capped at 48 hours a year. Overtime-exempt employees accrue as if working 40 h/week.
- Up to 48 hours carry over, but use may be capped at 48 a year. Front-loading is allowed.
- No payout at separation. Balance reinstated on rehire within 6 months.
- Public health emergency supplement: 80 hours.
- Coverage: "all employees working in Colorado"; railroad (RUIA) employees excluded; the state and its political subdivisions are included; the federal government is excluded (8-13.3-402(4),(5)).
- Amendments from the 2024–2026 sessions were not checked (CDLE 403).

**FAMLI benefit side**
- An employee may top up FAMLI benefits with accrued PTO or sick leave up to the average weekly wage.
- FAMLI runs concurrently with FMLA [US-COS5-008].

**Confidence:** Medium-High.

## 7 termination

**Final pay** [US-COS5-003]
- Discharge: due immediately. If the payroll unit is closed, within 6 hours of its next workday start, or 24 hours if it is off-site.
- Resignation: on the next regular payday.
- An unclaimed check is mailed after 60 days.
- Penalty if unpaid 14 days after a written demand: the greater of 2× the unpaid wages or 1,000 USD.

**Vacation:** accrued vacation earned and determinable must be paid at separation. It counts as wages (8-4-101(14)(a)(III)). COMPS says it is owed even when the employee is fired for cause or quits without notice [US-COS5-001].

**Severance:** not wages [US-COS5-003].

**Sick leave:** not paid out [US-COS5-005].

**Separation notice:** not read.

**Confidence:** High.

## 8 benefits_in_kind

- Colorado withholding follows federal withholding: wages exempt federally are generally exempt in Colorado. The Guide lists no Colorado departure for 401(k), §125, HSA, transit or GTL [US-COS5-007].
- Express departure: OBBBA qualified overtime stays subject to Colorado withholding [US-COS5-007, US-COS5-012].
- COMPS credits: meals at cost or value; lodging 25–100 USD/week; no charges for uniforms or uniform deposits [US-COS5-001].

**Confidence:** Medium-High.

## 9 deductions_garnishments

**Permitted wage deductions (8-4-105)** [US-COS5-004]
- (a) required by law;
- (a.5) auto-enrolment retirement;
- (b) a written agreement for loans, advances, goods or equipment;
- (c) theft after a police report;
- (d) any revocable employee authorisation;
- (e) unreturned property or money of a terminated employee, with notice within 10 days.

**Garnishment (Colorado Judicial Form 26 SC, R 1/22, implementing C.R.S. 13-54-104)** [US-COS5-009]
- **Disposable earnings** also deduct employer-provided health insurance. This is a departure from the CCPA.
- **Exempt amount:** the greater of 80% of disposable earnings or 40× / 80× / 86.67× / 173.3× (weekly / bi-weekly / semi-monthly / monthly) the higher of the state and federal minimum wage. For a weekly payroll in 2026: 40 × 15.16 = 606.40.
- **Priority:** support writs and wage assignments come first.
- **Start:** from the first pay date at least 21 days after service.
- The statute text was not read on an official host; the official CRS host is LexisNexis.

**Child-support IWO specifics** (fees, Colorado priority): not read (childsupport.colorado.gov unreachable).

**Confidence:** High (deductions); Medium-High (garnishment).

## 10 collective_agreements

- State prevailing wage on public projects ≥ 500,000 USD (C.R.S. 24-92-201 ff.). Weekly pay is required [US-CO-P5-2-002].
- Certified-payroll format: not read.

**Confidence:** Medium.

## 11 indexation

- **State minimum wage:** CPI-indexed yearly and published in the PAY CALC Order and the COMPS poster [US-COS5-001; 2027 lead in US-COS5-011].
- **Denver minimum wage:** CPI-W H1/H1, effective 1 January. Derivation 18.81 × 1.0256 = 19.29 [US-COS5-010].
- **EAP salary threshold:** yearly (57,784 in 2026) [US-COS5-001].
- **UI chargeable wage limit:** statutory steps, 27,200 → 30,600 → 32,100 [US-CO-P5-1-003].
- **FAMLI rate:** set yearly by the Division, capped at 1.2% [US-CO-FAMLI-001, US-COS5-008]. The FAMLI wage cap follows the SS base.
- **Income tax:** flat 4.40% (DR 1098 2026). DR 1098 for 2027 is not yet published (the tax.colorado.gov/DR1098 page lists 2024 and current only).
- **OPTs:** fixed amounts, not indexed.

## 12 data_protection

- The pay statement may show the SSN instead of the name (8-4-103(4)(e)). Colorado does not require truncation on the pay statement itself (Wage Act word search for SSN/truncat).
- C.R.S. 6-1-713/-713.5/-716 (PII disposal, security, 30-day breach notice) were not read; coag.gov returned 202-empty. Open question.

**Confidence:** Low.

## 13 live_legal_change (2026-01-01 to 2026-11-02)

- FAMLI 2027 rate 0.86% (A.2) [US-COS5-008].
- UI 2027 wage base 32,100 and new-employer rate 1.70% with no solvency surcharge [US-CO-P5-1-003/-004].
- State minimum wage 2027 15.71 and Denver 2027 19.84 (MANUAL, tier B) [US-COS5-011].
- OBBBA overtime decoupling for withholding (2026 DR 0004 and Guide) [US-COS5-007, US-COS5-012].
- CDOR XLSX W-2 route for tax year 2026 [US-COS5-013].
- FAMLI ITIN bulk files from 2026-10-01 [US-COS5-008].
- Colorado SecureSavings: employers without a plan must register or certify an exemption (mentioned in US-COS5-008; the programme's own page was not read).
- The Wage Act edition of 2025-08-06 is in force [US-COS5-002/003].
- CDLE news and the Colorado Register (SOS) could not be swept (403). The bulletin sweep is therefore incomplete.

## Special populations (state level)

| Population | Colorado rule | register_id |
|---|---|---|
| Domestic/household | UI: FUTA 1,000/quarter threshold (CO not in DOL Table 1-3). COMPS coverage of domestic workers not read here | US-COS5-014 |
| Agricultural | Overtime after 48 h (56 at highly seasonal sites); extra breaks; UI FUTA ag threshold; migratory-laborer disclosures in the worker's language (8-4-117); 5% language rule (Rule 2.3.2(C)(3)) | US-COS5-001, US-COS5-014, US-COL-002, US-COP9L-001 |
| Minors | Unemancipated minors may be paid 15% below the state minimum (not below some local minimums) | US-COS5-001 |
| Tipped | Tip credit max 3.02; state tipped 12.14 (2026); Denver 16.27; tips are the employee's property unless pooling is notified (8-4-103(6)) | US-COS5-001, US-COS5-010, US-COS5-002 |
| Clergy/religious | No state rule beyond federal located (Guide follows federal withholding exemptions) | US-COS5-007 |
| Students | UI: students working for their school excluded (student nurses not) | US-COS5-014 |
| Nonresident aliens | No state rule beyond federal withholding conformity; W-2 template: SSN 999999999 if none, and CO withholding required without a valid TIN; FAMLI accepts ITINs | US-COS5-007, US-COS5-013, US-COS5-008 |
| Statutory employees | No state rule beyond federal located (commission insurance/real-estate agents are excluded from UI) | US-COS5-014 |
| Government employees | The Wage Act's employer definition excludes the state, counties, municipalities and school districts (8-4-101(6)), so pay-statement and final-pay rules do not bind them; HFWA includes them and excludes the federal government | US-COS5-002, US-COS5-005 |
| Military/military spouse | Nonresident military pay and spouse pay exempt; resident active-duty exception | US-COS5-007 |
| Transport workers | Rail, air (≤50% CO pay) and motor carrier interstate exemptions for nonresidents | US-COS5-007 |

## MULTI hand-offs (Colorado)

- **SUI wage-base credit for wages reported to another state:** not answered. The C.R.S. 8-76-102 text and the CDLE premiums page were unreachable. Open (CO-OQ-1).
- **FAMLI coverage of multistate workers:** not answered. The FAMLI rules (7 CCR 2702) and famli.colorado.gov were unreachable. Open (CO-OQ-2).
- **Paid sick leave for employees partly in Colorado:** HFWA covers "all employees working in Colorado", with no hours-in-state threshold in the 2023 text. Accrual is on hours worked, so only Colorado hours would accrue. That last point is my inference; no CDLE INFO read [US-COS5-005].
- **Pay-statement reach to out-of-state work:** no territorial clause in 8-4-103. Open.

## ACCESS gaps (exact URLs)

**CDLE and FAMLI**
- https://cdle.colorado.gov/dlss/labor-laws-rules-resources/minimum-wage — 403; Wayback 404.
- https://cdle.colorado.gov/sites/cdle/files/adopted_2026_pay_calc_order_7_ccr_1103-14_12.8.25.docx — 403; Wayback 404. This is the official 2026 list of local minimum wages.
- https://cdle.colorado.gov/sites/cdle/files/2026_comps_order_poster_english_%5Baccessible%5D.pdf — 403 direct; obtained through Wayback (US-COS5-001).
- https://famli.colorado.gov/employers/premiums — 403; Wayback 404.
- https://famli.colorado.gov/ — 403.

**Other state hosts**
- https://www.sos.state.co.us/CCR/NumericalCCRDocList.do?deptID=9 — 403 (CCR: COMPS 7 CCR 1103-1, PAY CALC 1103-14, FAMLI 7 CCR 2702).
- https://childsupport.colorado.gov/new-hire-reporting — timeout (twice); childsupport.state.co.us — 302 then timeout.
- https://coag.gov/resources/data-protection-laws/ — 202 empty.
- https://content.leg.colorado.gov/sites/default/files/R24-800_Overview%20of%20Minimum%20Wage%20Laws%20Issue%20Brief-accessible.pdf — 202 empty.
- https://leg.colorado.gov/laws/colorado-revised-statutes — the CRS are hosted only on LexisNexis (JS, gated). No official per-section host for C.R.S. 13-54-104, 6-1-716, 8-76-102 or 8-13.3-5xx.

**Local and federal**
- https://www.denvergov.org/... (Denver Labor, Minimum Wage) — bot rejection; the Wayback copy of the Finance news release was used (US-COS5-010). The 2027 release URL guessed on Wayback: 404.
- https://bouldercolorado.gov/minimum-wage — 404.
- https://oui.doleta.gov/unemploy/pdf/uilawcompar/2026/coverage.pdf and /2025/ — 404 (2023 edition used).

**Wayback CDX/availability API:** 429 / Temporarily Offline (shared with parallel workers).

## Open questions

- **CO-OQ-1. SUI wage-base credit for another state's wages.** What would close it: C.R.S. 8-76-102 (chargeable wages) text, or the CDLE Employer Handbook; or the DOL "Significant Provisions of State UI Laws 2026" CO line.
- **CO-OQ-2. FAMLI coverage of multistate workers; 2027 employee/employer split; employer-share exemption below 10 employees.** What would close it: 7 CCR 2702-3 (FAMLI premiums rule) and C.R.S. 8-13.3-507 via famli.colorado.gov or the Colorado Register (browser pass).
- **CO-OQ-3. Local minimum wages other than Denver (Edgewater, City of Boulder, Boulder County) and 2027 state/Denver values.** What would close it: CDLE 2026/2027 PAY CALC Order (7 CCR 1103-14) and Denver Finance's 2026 news release (browser pass on cdle.colorado.gov and denvergov.org).
- **CO-OQ-4. UI quarterly wage report (format, due date) and new-hire reporting specifics.** What would close it: CDLE MyUI Employer+ wage-report guide and the Colorado State Directory of New Hires page.
- **CO-OQ-5. Denver OPT 2026 edition.** What would close it: Denver Tax Guide Topic 61, 2026 revision (Denver Treasury). Also Sheridan OPT on the city's own page.
- **CO-OQ-6. HFWA amendments 2024–2026, and electronic pay-statement consent.** What would close it: CDLE current HFWA text and INFO #6/#13 (browser pass).
- **CO-OQ-7. Data protection (6-1-713/-713.5/-716) and Colorado SecureSavings payroll-deduction duties.** What would close it: coag.gov data-protection page; the SecureSavings employer page (treasury).
- CO-OQ-8 (DR 0004 Table 1 alignment) closed on the raw text extraction, 2026-11-02.

Overall confidence for Colorado: High on state withholding, state minimum wage and overtime, Wage Act rules, Denver minimum wage, FAMLI and UI rates. Medium on garnishment, coverage and OPTs. Low on the UI report, new hire, data protection and non-Denver local minimum wages. Most of the remaining gaps sit behind cdle.colorado.gov, famli.colorado.gov and sos.state.co.us, so the single browser pass on those three hosts would close CO-OQ-1..4 and 6.

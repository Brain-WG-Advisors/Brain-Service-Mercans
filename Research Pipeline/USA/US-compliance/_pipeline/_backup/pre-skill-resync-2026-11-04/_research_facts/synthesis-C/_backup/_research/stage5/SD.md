# Stage 5 — SD (South Dakota): findings across the 13 domains

Worker: compliance-source-hunter, 2026-11-02. Budget declared: 60 fetches / 2 h. Used about 38 network calls (including 2 searches and 1 blocked tier-B probe), well inside budget.
Shard: `00-official-sources/_register-shards/S5-SD.csv` (US-SDS5-001..020; 18 active, 2 partial, 0 MANUAL). Sources: `00-official-sources/ccg-sources/SD/` (21 files, 2,671,413 bytes; largest is the SDCL Title 61 text at 0.33 MB). Statutes are saved as text extracted from the official LRC API, because the HTML is UTF-16 and 1.4 to 3.4 MB.
Reused active rows (not re-fetched): US-SD-001 (no state income tax), US-SD-002 (RA FAQ), US-SD-003 / US-SDL-001 (DLR law compilation: no pay-statement or language clause), US-SDL-002 (DOR business tax list), US-SD-P5-1-001 (RA power of attorney, Rev. 01/2026), US-SD-P5-1-002 (RA employer handbook Rev. 07/2022: no employee contribution), US-SD-P5-1-003 (DOL: no state prevailing wage law), US-SD-P5-2-001 (DOR municipal tax guide 2026-07: no local wage tax), US-SD-P5-2-002 (Titles 60-62 scan: no family leave, TDI or PFML), US-SDP7-001/-002 (admin fee and investment fee), US-SDP9L-001/-002 (posters; official language).

**Access.** The VPN was off (Brazilian exit IP). Even so, sdlegislature.gov (`/api/Statutes/{title or chapter}.html?all=true`, UTF-16) and dlr.sd.gov answered plain curl with HTTP 200. Only a tier-B Yahoo article returned 429, and it was not needed.

**Tier.** T1: no state wage tax and no local wage tax. The state layer is RA (UI) plus the two RA fees, the labour rules, and child support / garnishment.

## 1 — labour_code
- **Minimum wage.** USD 11.85/h from 2026-01-01 and USD 12.30/h from 2027-01-01 (already published). [US-SDS5-003 A.2; US-SDS5-004 posters; high]
  - The statutory base is USD 8.50, indexed every 1 January by the CPI-U (US city average, all items), August over August. The increase is rounded **up** to the nearest 5 cents and the wage never decreases. DLR publishes the new rate by 15 October (SDCL 60-11-3, 60-11-3.2). [US-SDS5-001 A.1]
  - **G-DERIVE (Python, Decimal):**
    - 2027: 11.85 × 334.980 / 323.976 = 12.2525, rounded up to **12.30**. Matches DLR.
    - 2026: 11.50 × 323.976 / 314.796 = 11.8354, rounded up to **11.85**. Matches DLR. The 2025 base of 11.50 is a lead, not registered.
    - CPI-U figures: BLS series CUUR0000SA0. [US-SDS5-005, derived arithmetically]
  - **Tipped employees** (customarily more than USD 35/month in tips): cash wage at least 50% of the minimum wage, i.e. **5.925** (2026) and **6.15** (2027). The employer makes up any shortfall each pay period (60-11-3.1). DLR requires a record of all tips. [US-SDS5-001, -003]
  - **Opportunity wage** for employees under 20, per FLSA s.6 (60-11-4.1). Apprentices, learners and persons with a developmental disability are exempt only with a DLR permit (60-11-5). [US-SDS5-001]
  - **Local minimum wage:** none located. The text of 60-11-3 has **no** preemption clause. A tier-B summary claims 60-11-3 preempts cities; that claim is not borne out by the text read, so it is not registered. See Q1.
- **Overtime:** "South Dakota has no labor laws concerning compensatory (comp) time or overtime". FLSA only. [US-SDS5-012 A.2; Title 60 scan, US-SDS5-001]
- **Breaks and holiday pay:** no state requirement. [US-SDS5-011, US-SDS5-012]
- **Pay frequency and method:** at least once each calendar month, or on regular paydays the employer designates in advance, in lawful US money. Payment by check, cash or direct deposit, unless employer and employee agree another form (60-11-9). [US-SDS5-001 A.1; high]
  - No express consent rule for direct deposit or paycards was located. The statute lists direct deposit as an employer option. See Q2.
- **Scope:** sections 60-11-8 to 60-11-23 cover any employer "employing any person of this state" (60-11-8), and cash wages only (60-11-14). [US-SDS5-001]

## 2 — income_tax
- **No state income tax and no withholding.** There is no state W-4, no supplemental rate, no rounding rule, no state W-2 filing and no reciprocity. [US-SD-001 A.2]
- **No local income tax:** the DOR municipal tax list carries none. [US-SD-P5-2-001 A.2; US-SDL-002]
- **Nonresidents:** nothing to withhold for SD. An SD resident working in a wage-taxing state is withheld for that state (MULTI unit).

## 3 — social_security (Reemployment Assistance = UI)
- **Taxable wage base:** USD 15,000 from 2015-01-01. It is fixed in statute, **not indexed** (61-1-46). [US-SDS5-002 A.1; US-SD-002]
- **New employer:** 1.2% in year 1, then 1.0% while the account balance is positive, until the employer is experience-rated. Construction (NAICS 23) pays 6% then 3% (61-5-24). DLR puts the 1.0% / 3.0% in years 2-3. [US-SDS5-002, US-SDS5-020]
- **Experience-rated employers:** the schedule is set by the average high cost multiplier (AHCM): A below 1.30; B from 1.30 to below 1.50; C at 1.50 or more (61-5-25). The 2026+ table is SL 2025 ch 199 (61-5-25.7):
  - Schedule A: 0.00%–9.39%;
  - Schedule B: 0.00%–9.24%;
  - Schedule C: 0.00%–8.52%.
  - **Schedule C is in effect for 2026** (RAAC minutes, 5 Aug 2025) [US-SDS5-018 A.2]. Under C the rate is 0.00% at a reserve ratio of 0.50% or more, 0.02% at 0.00% to below 0.50%, and 8.52% below −7.00%.
  - The table is printed column-shifted, with the rates before their reserve-ratio label. Each row was mapped by hand. Medium-high on row mapping.
- **Administrative fee:** 0.08% for every experience-rated employer from calendar year 2026. It was 0.02% in 2024-2025, and then only when the reserve ratio was below 2.25% (61-5-28.1 as amended by SL 2025 ch 199). Not applicable to new employers. [US-SDS5-002, US-SDS5-020]
- **Investment fee:** 0.55% for employers not yet rated. Rated employers pay 0.00%–0.53% by reserve ratio, capped at the 1987 rate for accounts with a positive balance (61-5-29). [US-SDS5-002]
  - Neither fee may be deducted from wages.
- **Fund-balance surcharge** (61-5-28): 0.1%–1.5% for all employers if the fund falls below USD 11 m at quarter-end. Dormant since 2010. [US-SDS5-002, US-SDS5-020]
- **Employee contribution:** none. **No SDI, TDI, PFML, LTC or transit levy.** [US-SD-P5-1-002, US-SD-P5-2-002]
- **Conflict:** the DLR wage-reporting page says "maximum tax rate is 9.5 percent". That is a pre-2026 statement; the statute governs (the top rate is 8.52% under Schedule C, plus fees). [US-SDS5-013]
- **Liability thresholds:** 1 worker in 20 weeks, or USD 1,500 in a quarter. Domestic: USD 1,000 in a quarter. Agricultural: USD 20,000 in a quarter, or 10 workers in 20 weeks. 501(c)(3): 4 workers in 20 weeks. [US-SDS5-020; 61-1-17, 61-1-19]
- **Wage definition for UI** [US-SDS5-013]:
  - Included: vacation and sick pay, gifts and awards, employee 401(k)-type deferrals, Section 125 amounts.
  - Excluded: employer 401(k)/403(b)/408(k)/408(p)/457 contributions, and severance that is not legally required.
  - Tips are wages if more than USD 20/month.

## 4 — payslip_statute
- **No SD statute requires a pay statement or fixes its content or delivery.**
  - Title 60 full-text scan [US-SDS5-001].
  - DLR compilation [US-SD-003, US-SDL-001].
  - Federal recordkeeping applies.
- **Retention:** no general state rule in Title 60. The RA handbook lists the records to keep per employee: name and SSN, places of work, hire and termination dates with the reason, hours and wages per pay period, and quarterly totals [US-SD-P5-1-002]. No retention period was read in the statute. See Q3.

## 5 — reporting_instruments
- **No state withholding return, annual reconciliation or state W-2:** SD has no wage tax.
- **Quarterly RA wage report (Form 21)** [US-SDS5-013 A.2; US-SDS5-014 A.2]
  - Due (received by) 30 Apr, 31 Jul, 31 Oct and 31 Jan. Zero reports are required.
  - Channel: the online Internet Quarterly Wage Reporting System, `file_upload` (comma-delimited, DLR format, not obtained), or a CD/DVD ASCII file.
  - CD/DVD layout: 85-byte E (employer) and S (employee) records. The S record carries SSN, names, total and taxable quarterly wages (implied 2 decimals), state code 46 and the DLR account number.
  - Corrections on Form 21C.
  - Penalties: late filing USD 25 per month; late payment USD 25 per month; interest 1.5% per month.
  - Domestic employers may elect to file annually (Forms 21D/21E; Form DE by 31 December). [US-SDS5-020]
- **Registration:** online; the account number and rate are issued immediately. [US-SDS5-020]
- **Agent access:** RA POA Rev. 01/2026 (Tax, Benefits or Limited). [US-SD-P5-1-001]
- **New hire** (25-7A-3.3) [US-SDS5-007 A.1; US-SDS5-015 A.2]
  - Report within 20 days, or by two monthly electronic transmissions 12-16 days apart.
  - Fields: employee name, address and SSN; employer name, address and FEIN. A W-4 or equivalent may be used.
  - Covers rehires and every worker who must give a W-4.
  - Goes to the DLR New Hire Reporting Center. The quarterly report does not count as new-hire reporting.
  - A multistate employer may designate one state.

## 6 — leave
- **No paid sick leave, vacation, holiday or PFML statute.** [US-SDS5-011 A.3; US-SD-P5-2-002]
- **Voting:** 2 consecutive hours off while the polls are open, with **no deduction from wages**, unless the employee already has 2 consecutive off-duty hours. The employer may set the hours (12-3-5). [US-SDS5-008 A.1; WTC: paid time]
- **Jury duty:** protection from discharge or suspension (16-13-41.1). Pay is at the employer's discretion. [US-SDS5-008, -011]
- **Military:** National Guard members on state or federal active duty get SCRA protections (ch. 33A-2, keyword read). No state duty to pay military leave was located. [US-SDS5-009, partial]

## 7 — termination
- **Final pay, on discharge or resignation:** no later than the next regular payday for those hours, or as soon after as the employee returns employer property (60-11-10, 60-11-11). Resignation applies where there is no written fixed-term contract. [US-SDS5-001 A.1; US-SDS5-010]
- **Accrued vacation:** no statutory payout rule; it follows the agreement or policy, including forfeiture for failure to give notice [US-SDS5-011]. Case law on vested vacation was not researched (Q4).
- **Severance:** none required. [US-SDS5-011]
- **Separation notice:** no state UI separation notice was located. Form 238 (Notice to Base Period Employer) is a response form [US-SD-P5-1-002]. There is no state WARN law. [US-SDS5-011]

## 8 — benefits_in_kind
- **Income tax:** not applicable (no PIT), so state conformity to federal exclusions is moot.
- **UI base** follows the DLR list in section 3 [US-SDS5-013]:
  - employee pre-tax deferrals and Section 125 amounts are **included** in RA wages;
  - employer plan contributions are excluded;
  - the cash value of board, lodging and goods is included.

## 9 — deductions_garnishments
- **Wage-deduction authorisation:** no SD statute located. The Title 60 scan finds no deduction section. Federal FLSA limits apply. See Q2.
- **Ordinary garnishment** (21-18-51): the lesser of
  - 20% of weekly disposable earnings, or
  - disposable earnings minus 40 × the minimum wage (state rate if greater, so 40 × 11.85 = 474.00/week in 2026) **minus USD 25/week for each dependent family member** living with the debtor.
  - This is **stricter than the CCPA.**
  - Support orders: 50/60% (55/65% for arrears older than 12 weeks) (21-18-52).
  - The garnishee withholds through the last payroll period ending within 120 days of the summons.
  - [US-SDS5-006 A.1; the 474.00 is derived arithmetically]
- **Child support IWO** [US-SDS5-007 A.1]:
  - cap of 50% of wages (25-7A-32);
  - first deduction from the first pay after service;
  - remit within 7 business days of payday;
  - **employer fee up to USD 3/month** (25-7A-34);
  - current support takes priority across multiple orders (25-7A-35).
- **State tax levies:** not applicable to wages (no PIT). The DOR has no wage levy.

## 10 — collective_agreements / prevailing wage
- **No state prevailing-wage law.** [US-SD-P5-1-003 A.2, medium: DOL table read through a summariser]
- Federal Davis-Bacon only. No certified-payroll duty at state level.

## 11 — indexation
- **Minimum wage:** CPI-U, August over August, rounded up to 5 cents, published by 15 October (60-11-3.2). Proven above. [US-SDS5-001, -005]
- **Tipped wage:** 50% of the minimum wage, so it follows automatically.
- **RA wage base:** not indexed. The **schedule** moves with the AHCM, decided each year from the fund balance at 30 June (61-5-25).
- **Maximum weekly benefit** is indexed (benefit side only): 553 from 2025-07-06 and 575 from 2026-07-05. [US-SDS5-018, -019]

## 12 — data_protection
- **Breach notice** (22-40-19..26): "personal information" includes SSN and employer-assigned ID plus access code or biometrics. Affected residents are notified within 60 days; the Attorney General when more than 250 residents are affected. [US-SDS5-017 A.1]
- **No SSN-truncation rule** for pay statements was located in Titles 60 and 61 or ch. 22-40.

## 13 — live_legal_change (2026-01-01 → 2026-11-02)
- **SL 2025 ch 199**, effective 2026-01-01 (in force):
  - new 2026+ rate table (61-5-25.7);
  - administrative fee 0.08% for all rated employers (61-5-28.1).
  - [US-SDS5-002]
- **SL 2026 ch 205** (in force): investment-fund administration (61-5-29.1..29.7). Payroll-neutral: fee rates are unchanged. [US-SDS5-002]
- **SL 2026 ch 204:** state apprenticeship agency (60-15-1..3).
  - Status: enacted, effective on the date US DOL formally recognises the agency.
  - Payroll-neutral.
  - [US-SDS5-001]
- **2027 minimum wage 12.30 / tipped 6.15:** published under 60-11-3.2. In force from 2027-01-01. [US-SDS5-003]
- **RA Schedule C for 2027** (draft minutes). Schedule B for 2028 is possible if the AHCM falls below 1.5 on 2027-06-30: a projection, not enacted, operating at the employer contribution rate. [US-SDS5-019, partial]
- **Bulletin sweep:**
  - The DLR news page lists 50 releases (May–Oct 2026), none on payroll law.
  - The Title 60/61 text was scanned for SL 2025/2026 source notes; the hits are listed above.
  - The LRC 2026 session-law list itself was not read (Q5).

## Special populations (US-OWN-005, state round)
| Population | SD rule | register_id |
|---|---|---|
| Domestic / household | RA coverage at USD 1,000 cash in a quarter (61-1-19); annual reporting option (Form DE, 21D/21E). Babysitters are excluded from minimum wage (60-11-3) | US-SDS5-002, US-SDS5-020, US-SDS5-001 |
| Agricultural | RA coverage at USD 20,000 in a quarter or 10 workers in 20 weeks; crew-leader rules (61-1-17). No minimum-wage exclusion for agriculture beyond FLSA | US-SDS5-002 |
| Minors | Hours limits for under-16 and under-14 (ch. 60-12); under-20 opportunity wage (60-11-4.1); newspaper delivery under 18 is RA-exempt (61-1-39) | US-SDS5-016, US-SDS5-001, US-SDS5-002 |
| Tipped | Cash wage 50% of minimum (5.925 in 2026, 6.15 in 2027), tips over USD 35/month, make-up each pay period; tips over USD 20/month are RA wages | US-SDS5-001, US-SDS5-003, US-SDS5-013 |
| Clergy / religious | RA-exempt: churches, church-controlled organisations, ministers and religious orders (61-1-36) | US-SDS5-002 |
| Students | RA-exempt: students employed by their school, spouses in financial-aid programmes, credit work-study (61-1-37); student nurses and interns (61-1-38) | US-SDS5-002 |
| Nonresident aliens | No state rule (no PIT); RA follows work localization, not residence or citizenship | US-SD-001, US-SDS5-020 |
| Statutory employees / contractors | RA two-prong test, failing which the worker is covered: free from control AND independently established business (61-1-11). Delivery-facilitation contractors are independent contractors under 60-1-7 (title read, text not extracted). Minimum wage does not apply to independent contractors | US-SDS5-002, US-SDS5-004 |
| Family employment | RA-exempt: service for one's son, daughter or spouse, and a child under 21 working for a parent (61-1-44). Corporations have no family exemption (DLR) | US-SDS5-002, US-SDS5-013 |
| Government employees | State and political subdivisions are covered (61-1-13); elected officials, legislators, judges and National Guard are excluded (61-1-36) | US-SDS5-002 |
| Seasonal amusement / camps | Excluded from minimum wage and tipped wage under the 7-month or 33.3%-receipts test (60-11-3, 3.1) | US-SDS5-001 |

## MULTI hand-offs (answers for SD)
- **SUI wage-base credit:** **YES.** For the 15,000 base, "employment" includes service under another state's UI law (61-1-46, last sentence). Wages already reported to another state in the same year count toward SD's base. [US-SDS5-002 A.1]
- **UI localization:** the standard test (61-1-26, 61-1-27). The DLR administrative rule of thumb: out-of-state employees working in SD for **more than 90 days** are reported to SD, those under 90 days to the home state, and non-localized workers to the state of direction and control. [US-SDS5-020]
  - The 90-day line is DLR guidance, not statute.
- **PFML/SDI coverage of multistate workers:** not applicable (none exists).
- **Paid sick leave reach:** not applicable (none exists).
- **Pay-statement reach:** not applicable (no pay-statement statute). Note that 60-11-8 reaches employers "employing any person of this state" for timing and final pay.

## ACCESS gaps
- `https://www.yahoo.com/news/articles/2026-reemployment-rate-schedule-won-184909006.html`: HTTP 429. Tier-B lead only; superseded by the RAAC minutes (A.2).
- The DLR comma-delimited online upload layout sits behind the Internet Quarterly Wage Reporting System login (`gated`). The public CD/DVD layout was obtained.

## Open questions
- **Q1 local-minwage-preemption:** is there an SD statute preempting local minimum-wage ordinances?
  - 60-11-3 has no such clause. A tier-B lead says otherwise.
  - Closes with: the SDCL home-rule limitations (ch. 6-12) or an LRC/AG opinion.
  - No local ordinance is known, so there is no payroll effect today.
- **Q2 deduction-consent-and-paycard:** is there an SD rule on written authorisation for wage deductions, or consent to paycards or direct deposit?
  - None in Title 60.
  - Closes with: ARSD 47:04 (wage collection) text, or a DLR Wage & Hour statement.
- **Q3 payroll-record-retention:** what retention period applies to RA records?
  - Closes with: ARSD 47:06 (RA records rule) text.
- **Q4 vacation-payout-case-law:** do SD Supreme Court holdings on vested vacation affect final pay?
  - Closes with: a primary-court opinion (ujs.sd.gov). The DLR position is that it is a matter of agreement.
- **Q5 session-laws-2026-sweep:** read the LRC 2026 session-law list for chapters touching Titles 20, 21, 25, 60 and 61 beyond the source notes scanned.
  - Closes with: `https://sdlegislature.gov/Session/Laws/` for the 2026 session.
- **Q6 prevailing-wage-A-tier:** US-SD-P5-1-003 rests on a WebFetch summary of the DOL table (MEDIUM).
  - Closes with: a direct read of the DOL table, or of the SD statute history showing repeal.

**Confidence:** labour, UI, garnishment and new hire 90-95%; leave and termination 85%; data protection 80%; reporting 85% (the online upload format is gated).

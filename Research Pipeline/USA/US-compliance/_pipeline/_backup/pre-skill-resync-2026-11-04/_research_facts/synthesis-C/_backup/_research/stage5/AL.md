# Stage 5 — Alabama (AL): 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Mandate block: US-MQ-21 (answered at seal attempt 4; tier T4, verified).
Budget declared: 60 fetches / 2 h. Used: about 43 fetches (curl, ALISON GraphQL calls, 5 web searches) and about 45 minutes. Acquisition stopped at the 75% fetch mark.
Register shard: `00-official-sources/_register-shards/S5-AL.csv` (21 rows, US-ALS5-001..021). New sources are in `00-official-sources/ccg-sources/AL/` (15 files, 2.2 MB, none over 5 MB).

**Access notes**
- The VPN was **off**: ipinfo showed a BR exit. ADOR, Workforce Alabama, ALISON, Leeds and Birmingham all answered from BR anyway. auburnalabama.org timed out (ACCESS gap below).
- **New access route (for other workers):** the Code of Alabama on ALISON is a Next.js single-page app. Its GraphQL endpoint answers plain POSTs without a key:
  - endpoint: `https://alison.legislature.state.al.us/graphql`;
  - one section: query `codesOfAlabama(where:{type:{eq:Section}} whereAny:[{displayId:{eq:"25-4-16"}}] includeAllVersions:true){data{displayId catchLine content history}}`;
  - full-text search: `fullTextQuery:`.
  - Helper script: `<scratchpad>/AL/code.py`. The JSON responses are saved as the local files.

Active rows reused without a re-fetch (their local files were re-read this pass):
- US-AL-P5-1-001 / US-AL-WH-001: 2026 withholding booklet, `pdfs/AL/whbooklet_0126_webfetch-20261029.pdf`, re-read in full on pp. 1–7. It is now registered again with the formula detail as US-ALS5-001.
- US-ALR3-001: UC Employer Handbook rev. 2021, `pdfs/AL/uc_emp_handbook_rev_2021_wayback-20260113180842.pdf`, chapter 2 and BEN-241 re-read.
- US-AL-P5-2-001 / US-ALL-001: Wage and Hour Info, which says there are no state wage-hour laws. US-AL-P5-2-002: the UC power of attorney. US-ALP9L-001: posters.

Duplication note (F23): `pdfs/AL/` holds `Wage_and_Hour_Info_wayback-20251002165036.pdf` and `AL-wage-hour-info_wayback-20251002.pdf`. Both are 46,739 bytes and are the same snapshot. The synthesis should keep one.
Re-read note: US-ALS5-007 re-reads the page behind US-AL-P5-1-002 (same URL) and carries more of it. Its `supersedes` is left empty because the older row is not wrong, only thinner. The synthesis may close US-AL-P5-1-002 in favour of US-ALS5-007.

---

## 1. labour_code
- **Minimum wage:** none at state level.
  - The agency states that "Alabama does not have any state laws governing wage and hour issues". The federal FLSA applies: 7.25 USD/h since 2009-07-24 (FED unit) [US-AL-P5-2-001, US-ALL-001].
  - No 2027 state rate is enacted. Nothing is indexed.
- **Local minimum wages:** prohibited.
  - Ala. Code 25-7-41(b)-(c) (Act 2016-18): no county, municipality or political subdivision may require an employer to provide any wage, paid or unpaid leave, vacation or work-schedule benefit beyond state or federal law. Such mandates are void.
  - The only exception is public employees (25-7-43) [US-ALS5-010].
- **Overtime:** FLSA only (1.5× over 40 hours a week). There is no state daily overtime [US-AL-P5-2-001].
  - The tax side of overtime is under domain 2 (Act 2026-604).
- **Pay frequency, pay-day timing, method of payment (direct deposit / paycard consent):** no state statute. The agency page says only child labour has state law [US-AL-P5-2-001]. Federal rules apply, and the employer's policy governs.
  - Confidence 85%: the negative rests on the agency statement. A full-text Code search was not run for "pay day".
- **Equal pay:** Clarke-Figures Equal Pay Act, 25-1-30, covers sex and race. An employer may not refuse to hire an applicant for declining to give wage history [US-ALS5-015].
- Confidence: 85%.

## 2. income_tax
- **Instrument:** Ala. Code 40-18-71 and 40-18-74 [US-ALS5-011]. Withholding booklet, revised January 2026 [US-ALS5-001].
- **Method, formula (booklet p. 6):**
  1. Annualise gross wages.
  2. Subtract four items:
     - **(A) standard deduction** (Schedule p. 7, phase-out by annualised gross income, GI):
       - 0/S: 3,000 if GI ≤ 25,999; 25 less for each 500 above 25,999; 2,500 from 35,500.
       - MS: 4,250; 88 less per 250 above 12,999; 2,500 from 17,750.
       - M: 8,500; 175 less per 500; 5,000 from 35,500.
       - H: 5,200; 135 less per 500; 2,500 from 35,500.
     - **(B) annualised federal income tax withheld.** This is a distinctive Alabama feature: federal FIT is a deduction. Statute 40-18-71(a).
     - **(C) personal exemption:** 0; 1,500 for S/MS; 3,000 for M/H.
     - **(D) dependents:** 1,000 each if GI ≤ 50,000; 500 if ≤ 100,000; 300 above 100,000.
  3. Rates:
     - 0/S/H/MS: 2% on the first 500, 4% on the next 2,500, 5% above 3,000.
     - M: 2% on the first 1,000, 4% on the next 5,000, 5% above 6,000.
  4. Divide by the number of pay periods.
  - Rounding: the tables are computed to the nearest dollar. A formula result *may* be rounded to the nearest dollar. Wages may be computed to the nearest dollar (40-18-71(c)).
  - **Oracle seed (C37), re-derived in Python** [US-ALS5-001, verification = derived arithmetically]:
    - Case: M-2, weekly 850.00, federal withholding 35.19.
    - 850 × 52 = 44,200.00.
    - Deductions: 5,000 + 1,830.00 + 3,000 + 2,000 = 11,830.00. The booklet rounds 35.19 × 52 = 1,829.88 to 1,830.00.
    - Taxable: 32,370.00.
    - Tax: 20 + 200 + 26,370 × 5% = 1,538.50 a year, ÷ 52 = **29.59** a week (the booklet value). Rounded to the dollar this would be 30.
  - Dependency: the AL calculation needs federal FIT computed first. The WTC/DD must order FIT before AL SIT.
- **Certificate:** Form **A4, REV. 4/2025** [US-ALS5-005]. The federal W-4 is not accepted. With no A4 on file, withhold at zero exemptions.
  - A4 entries: 0 / S / MS / M / H, number of dependents, and an additional amount per period. Employer's line 6 = table column (e.g. M-2).
  - Penalty for an inflated A4: 500 USD (40-29-75).
  - The employer contacts ADOR at 8 or more dependents or when a claim looks excessive, and withholds at the highest rate until a corrected A4 arrives. A4 forms are kept at least 3 years.
  - A Spanish A4 exists. A4-MS is the military-spouse (MSRRA) exemption.
  - Trap (never-do 6): the ADOR page text still says "Revised March 2014", but the linked PDF prints REV. 4/2025 [US-ALS5-002].
- **Supplemental:** may be withheld at 5% [US-ALS5-001].
- **Exclusions from AL wages (booklet):** IRC 125, 219, 401(k), SIMPLE 401(k), 403(b), 408(k), 408(k)(6), 408(p), 457.
- **Severance:** up to 50,000 USD of severance or downsizing pay may be exempt, with prior ADOR approval [US-ALS5-001].
- **Jobs Act:** the employer credits the job development fee of 41-10-44.7(b) against withholding (40-18-71(a)) [US-ALS5-011]. This only matters for employers holding a Jobs Act incentive.
- **Resident and nonresident rules** [US-ALS5-001, US-AL-P5-1-001]:
  - An AL employer withholds from AL residents wherever they work, except when it withholds for the work state. Booklet examples: a resident working in GA has no AL withholding; a resident working in FL is withheld for AL.
  - Nonresidents are withheld only on wages earned in AL. A nonresident employer withholds on AL-earned wages.
  - Federal mobile-worker carve-outs apply: air carriers (P.L. 91-569), rail and motor carriers (P.L. 101-322), water carriers (P.L. 106-489). Wages earned within 3 miles of the coast are AL wages.
- **Reciprocity:** none. The booklet lists no agreement [US-AL-P5-1-001].
- **30-day safe harbor (Act 2025-334, in force 2026-01-01):** applies to nonresidents with 30 or fewer AL days in the calendar year who work in more than one state, and whose home state has a similar exclusion or no income tax [US-ALS5-003].
  - Qualifying home states as of 2026-10-01: AK, FL, GA, IL, IN, LA, MT, NV, NH, SD, TN, TX, WA, WV, WY.
  - At 31 or more days, all AL income of the year is taxable and withheld. ADOR allows penalty discretion for the catch-up.
  - Professional athletes, entertainers and public figures are excluded.
  - Operating level: **withholding**.
- **Overtime (live change), Act 2026-604:** for 2026–2028, the overtime premium is deductible up to 1,000 USD per taxpayer [US-ALS5-004].
  - Operating level: **assessment only**. W-2 box 12 code TT is information and changes no wages, withholding or tax. Total overtime stays in box 16.
  - The earlier withholding-level overtime exemption (Act 2023-421, amended by Act 2024-437) is shown by ADOR as "previous" and is no longer in force. Its end date (2025-06-30) comes from tier-B leads only.
- **Local income taxes (municipal/county occupational taxes):** withheld by the employer and remitted to the city or county on its own return. ADOR does not administer them [US-ALS5-001]. This is why AL is T4.
  - Exemplar, City of Leeds: 1% of gross earnings, monthly return to Avenu, annual reconciliation, amount shown on the pay stub, records kept 5 years [US-ALS5-017].
  - Birmingham: filed through the HdL portal [US-ALS5-018]. The rate of 1% is tier C only [US-ALP7-001, MANUAL].
  - The tax is work-location based in the exemplars read.
  - **No state list of levying localities exists.** Tier-B leads say about 26 cities (League of Municipalities), including Auburn 1%, Bessemer 1%, Gadsden 2% and Opelika 1% from 2025-04-01 (was 1.5%), and Macon County 1%. None of these is registered as a number.
- Confidence: state 95%; local 55% (two exemplars, no census).

## 3. social_security (SUI; no SDI/PFML)
- **Agency:** Alabama Department of Workforce, UC Division (formerly the Department of Labor).
- **Taxable wage base:** **8,000 USD** per employee per calendar year, set in statute (25-4-16(b)(1)). It is not indexed; it rises only if the federal base exceeds it [US-ALS5-009, US-ALS5-007].
- **New-employer rate:** 2.70% [US-ALS5-007, US-ALR3-001].
- **Experienced rates:** 0.20%–6.80% including the 0.06% Employment Security Enhancement Assessment (ESA), across schedules A–D, plus shared cost. All rates carry the 0.06% ESA reduction except 5.40% [US-ALS5-007; statute 25-4-54, US-ALS5-009].
  - The **2026 schedule letter and shared-cost figure were NOT located** on an official page (Open question AL-OQ-1).
  - The earlier "0.59%–6.19% in 17 steps" [US-AL-UC-001] is one schedule's computed band; do not treat it as the full range.
- **Employee contribution:** none. "No unemployment compensation taxes ... are withheld from employees in Alabama" [US-ALR3-001].
- **ESA and FUTA:** no FUTA credit can be taken for the 0.06% ESA [US-ALR3-001, handbook p. 19].
- **UC wages:** include tips and bonuses. Room and board furnished at the employee's option is valued at no less than 63.00 a week full board, meals 42.00 a week or 2.00 a meal, lodging 21.00 a week or 3.00 a day. Board provided for the employer's convenience is not wages [US-ALR3-001, rev. 2021; values from the handbook, Admin. rule not read].
  - **Cafeteria plans are NOT exempt for UC** where the employee can choose cash [US-ALS5-007, US-ALR3-001]. This departs from the income-tax exclusion.
- **SDI/TDI/PFML/long-term care/transit:** none. Settled at mandate level [US-ALS5-007 programme list, US-ALR3-001..003, US-ALL-002].
- **Employer levies:** only the 0.06% ESA inside UC [US-ALP7-002, US-ALL-002].
- **MULTI-OQ-2, answered for AL:** 25-4-16(b)(1) counts "service constituting employment under any unemployment compensation law of another state" toward the 8,000. Workforce Alabama confirms that wages an AL employer pays for work in another state count toward the base [US-ALS5-009, US-ALS5-007].
- **MULTI-OQ-3:** not applicable (no PFML/SDI).
- Confidence: 90% (2026 shared cost open).

## 4. payslip_statute
- No state pay-statement content statute exists. The agency says there are no state wage-hour laws; federal record-keeping (29 CFR 516) applies [US-AL-P5-2-001, US-ALL-001].
  - Hence no electronic-consent rule and no state retention period for pay statements.
- Local exemplar: Leeds asks employers to inform employees of the occupational-tax withholding, "e.g. on the pay stub" [US-ALS5-017].
- Record retention found:
  - A4 certificates: 3 years [US-ALS5-001].
  - UC employment records: kept and open to inspection [US-ALR3-001].
  - Leeds occupational-tax records: 5 years [US-ALS5-017].
- Language: English. See US-MQ-03 and US-OWN-006.
- **MULTI hand-off (pay-statement reach to out-of-state work):** not applicable; no statute.
- Confidence: 85%.

## 5. reporting_instruments
| Filing | Authority | Frequency / deadline | Format / channel | register_id |
|---|---|---|---|---|
| Registration (withholding account) | ADOR | on hiring | My Alabama Taxes (online) | US-ALS5-001 |
| A-6 monthly return | ADOR | if more than 1,000 USD withheld in month 1 or 2 of the quarter; due the 15th of the next month | MAT online; e-file and EFT mandatory for any single payment ≥ 750 | US-ALS5-001, US-ALS5-011 |
| A-1 quarterly return | ADOR | last day of the month after the quarter; file even when nil | MAT | US-ALS5-001 |
| A-3 annual reconciliation + W-2s (and 1099s with AL tax) | ADOR | 31 January | `file_upload`: EFW2, **RS record only**, 512 bytes; e-file mandatory for 10+ statements (Form 10, 8/24) | US-ALS5-006 |
| 1099s without AL tax | ADOR | 15 March (or the Combined Federal/State program) | paper or CF/SF | US-ALS5-001 |
| Quarterly Contribution and Wage Report | Workforce Alabama UC | last day of the month after the quarter (31 Jan, 30 Apr, 31 Jul, 31 Oct) | `online_form` or `file_upload` via eGov only; computer-generated paper not accepted; corrections on UC-10C | US-ALS5-007, US-ALR3-001 |
| New-hire report | Workforce Alabama New-Hire Unit | 7 days from hire or recall (electronic: twice a month, 12–16 days apart) | online form, fixed-length or CSV/tab file; electronic mandatory for 5+ employees | US-ALS5-008 |
| Municipal occupational tax | each city/county (e.g. Leeds via Avenu; Birmingham via HdL) | Leeds: monthly + annual reconciliation | city portal | US-ALS5-017, US-ALS5-018 |

- **EFW2 RS layout for AL:**
  - account number: columns 248–257;
  - FEIN: columns 258–266;
  - state code AL or 01: columns 274–275;
  - state wages: columns 276–286;
  - state tax: columns 287–297;
  - **federal income tax withheld: columns 298–307** (needed because of the federal deduction);
  - other income: columns 338–348;
  - payment year: columns 393–396 [US-ALS5-006].
- W-2 furnishing duty: every employee paid 1,500 USD or more in AL wages, or with AL tax withheld [US-ALS5-001].
- Penalties: late return, greater of 10% or 50 USD; late payment, 10%; 50 USD per late W-2/1099 [US-ALS5-001].
- New-hire file specifications are obtained from newhire@workforce.alabama.gov; they are not published on the page.
- Confidence: 90%.

## 6. leave
- **Paid sick leave:** no state statute. Local mandates are barred by 25-7-41 [US-ALS5-010, US-AL-P5-2-001].
- **Jury duty (payroll-relevant):** a **full-time employee is entitled to his or her usual compensation** while on jury service.
  - The employee may not be required to use annual, vacation, unpaid or sick leave.
  - Discharge or adverse action for jury service is prohibited (12-16-8(c), 12-16-8.1) [US-ALS5-012].
  - No day cap is stated. Whether juror fees may be offset is not addressed in the text read.
- **Voting:** up to 1 hour on reasonable notice; not available when the shift leaves the stated poll-hour window. The statute is silent on pay (17-1-5) [US-ALS5-012].
- **PFML:** none.
- **MULTI-OQ-4:** not applicable (no state sick-leave law).
- Confidence: 85%.

## 7. termination
- **Final pay timing and accrued vacation payout:** no state statute. Federal law applies and the employer's policy governs [US-AL-P5-2-001].
  - Confidence 80%: an ALISON full-text search for "final paycheck" returned only public-employee sections.
- **UI separation:** no mandatory separation notice at termination was found. On a claim, the employer must return BEN-241 separation information **within 6 working days** of mailing (fax or uisides.org) [US-ALR3-001].
- **Garnishment on termination:** the garnishee reports the termination to the court and pays in sums withheld within 15 days (6-10-7) [US-ALS5-013].
- **Severance:** income-tax exemption up to 50,000 USD with ADOR approval (domain 2).
- **State WARN:** none found (not searched separately).
- Confidence: 75%.

## 8. benefits_in_kind
- AL income tax follows the federal definition of wages unless AL law conflicts. Exclusions listed: IRC 125, 219, 401(k), 403(b), 408(k), 408(p), 457 [US-ALS5-001].
- **HSA:** conforms. Employer contributions are not includible; residents deduct their own contributions up to the IRC 223 maximum (40-18-15.6) [US-ALS5-020].
- **Departures:**
  - Federal income tax is a deduction in the AL withholding base (domain 2).
  - Agricultural cash wages: AL does not follow federal withholding [US-ALS5-001].
  - UC treats cafeteria-plan cash-option reductions as wages [US-ALS5-007].
- Transit (132(f)) and group-term life (79) are **not on the booklet list**. Treatment not confirmed (AL-OQ-3).
- Confidence: 75%.

## 9. deductions_garnishments
- **Wage-deduction authorisation:** no state statute (federal only) [US-AL-P5-2-001].
- **Garnishment (6-10-7):** 75% of an AL resident's wages is exempt; the garnishee retains 25% [US-ALS5-013].
  - Payments into court start after 30 days, then monthly or more often.
  - The statute measures on "wages ... due". Apply the CCPA disposable-earnings limit together with it; the more protective result governs.
- **Child support (30-3-61, -67, -70):** [US-ALS5-013]
  - remit within 7 business days of payday to the court clerk or the DHR designee;
  - an out-of-state IWO follows the law of the obligor's principal place of employment (fee, maximum, timing);
  - an IWO has priority over garnishments and may exceed 6-10-7 up to the CCPA support limits;
  - current support is paid before arrears;
  - no discharge or refusal to hire because of an IWO.
- Employer processing fee: the AL fee amount was **not located** (AL-OQ-4).
- **State tax levies:** not researched (no AL source read).
- Confidence: 80%.

## 10. collective_agreements (prevailing wage)
- No state prevailing-wage law. The agency says there are no state wage-hour laws [US-AL-P5-2-001].
  - Tier-B leads say the law was repealed in 1980. That date was not read in an official source.
- Davis-Bacon applies to federally funded projects (FED unit).
- 25-7-42 bars local labour-peace and project-labour-agreement mandates [statute read in US-ALS5-010's batch; not registered as a separate row].
- Confidence: 80%.

## 11. indexation
- **Nothing is indexed annually in AL payroll law.**
  - SUI base: 8,000, fixed in statute [US-ALS5-009].
  - Withholding brackets, exemptions and the standard-deduction schedule: statutory amounts unchanged in the 2026 booklet [US-ALS5-001, US-ALS5-011].
  - No state minimum wage exists.
- The only annual variable is the UC rate schedule (A–D) and shared cost, set each year from the fund balance on 30 June (25-4-54). These are published on the employer's tax-rate notice (UC-216), not as a public table [US-ALS5-007].
- G-DERIVE: no indexed amount exists to derive. The arithmetic proof is the formula example in domain 2.

## 12. data_protection
- **SSN truncation on pay statements:** no AL statute located.
- **Breach notification:** Alabama Data Breach Notification Act 2018, ch. 8-38. Sensitive personally identifying information includes SSN [US-ALS5-016, partial: definitions only].
- Workforce Alabama rejects invalid SSNs on wage reports. An employee with an invalid SSN is left off the report and added later on UC-10C [US-ALR3-001].
- Confidence: 60%.

## 13. live_legal_change (sweep 2026-01-01 to 2026-11-02)
| Change | Status | Effective | Operating level | register_id |
|---|---|---|---|---|
| Act 2025-334, 30-day nonresident safe harbor | in force | 2026-01-01; qualifying-state list as of 2026-10-01 | withholding + filing | US-ALS5-003 |
| Act 2026-604, overtime premium deduction (≤ 1,000 USD) | in force | 2026-01-01 to 2028-12-31 | assessment (W-2 box 12 TT info only) | US-ALS5-004 |
| Acts 2023-421 / 2024-437, overtime withholding exemption | expired / previous (ADOR) | end date 2025-06-30 per tier-B leads | was withholding | US-ALS5-004 |
| Portable Benefits Act, 25-1-70..72 | in force | 2025-12-31 (tax years after 2025) | independent contractors only; no payroll effect | US-ALS5-021 |
| Hurricane Isaias relief | notice 2026-10-15 | individual returns to 2027-02-04; withholding relief case by case only | filing deadlines | US-ALS5-019 |

- Bulletin read: ADOR news list (pages up to 2026-09-15; local file `ADOR-news_2026-11-02.html`, not a separate row).
- Lead not followed: Bradley, 2026-09, "Alabama DOR issues guidance to employers with remote/traveling workers" (tier B). This may point to an ADOR rule or FAQ on day-counting under Act 2025-334 (AL-OQ-5).
- 2027: no enacted payroll change located.

---

## Special populations (US-OWN-005, state round)
| Population | AL rule | register_id |
|---|---|---|
| Domestic / household workers | Income tax: exempt from AL withholding, as federally. UC: covered when cash wages reach 1,000 USD in a quarter | US-ALS5-001, US-ALS5-007 |
| Agricultural workers | Income tax: exempt from withholding; AL does NOT follow the federal rule withholding on cash wages that are FICA wages. UC: 10+ workers in 20 weeks or 20,000 USD in a quarter. Child labour: under-16 farm work allowed | US-ALS5-001, US-ALS5-007, US-ALS5-014 |
| Minors | Under 16 barred except agricultural work and as the chapter allows; 14–15 outside school hours, not in manufacturing or mechanical work; prohibited-occupation list; no state youth wage | US-ALS5-014 |
| Tipped employees | No state wage rule (federal 2.13/7.25 tip credit, FED unit). Tips are UC wages. Overtime premium deduction is assessment-level; no AL tip deduction located | US-ALR3-001, US-AL-P5-2-001 |
| Clergy / religious | Ministers exempt from AL withholding (federal class). Church and church-controlled organisation employment not UC-covered | US-ALS5-001, US-ALS5-007 |
| Students | No AL rule beyond federal located (booklet and FAQ read) | US-ALS5-001, US-ALS5-007 |
| Nonresident aliens | No AL-specific rule in the booklet; federal treatment (FED unit) plus the AL resident/nonresident sourcing | US-ALS5-001 |
| Nonresident (other-state) workers | 30-day safe harbor; nonresidents withheld on AL-earned wages; carrier carve-outs; military spouses on A4-MS | US-ALS5-003, US-ALS5-001 |
| Statutory employees | Employer/employee status follows the federal test; no AL statutory-employee rule | US-ALS5-001 |
| Government employees | 501(c)(3) entities liable for UC at 4+ workers in 20 weeks; the Act 2016-18 local preemption does not cover public employees (25-7-43) | US-ALS5-007, US-ALS5-010 |
| Military spouses | A4-MS exemption (MSRRA, P.L. 111-97) | US-ALS5-001, US-ALS5-002 |
| Severance recipients (downsizing) | Up to 50,000 USD exempt with ADOR approval | US-ALS5-001 |

---

## ACCESS gaps
- `https://www.auburnalabama.org/finance/business-and-licensing-forms/occupational-license` (and the site root): curl timeout (HTTP 000) from a BR exit, VPN off. Wayback was not tried. Needed for the Auburn rate and return frequency.
- `https://library.municode.com/al/birmingham/codes/code_of_ordinances?nodeId=PT1THCOGEOR_TIT3ARETA_CH2OCTA`: script-rendered (known from US-ALP7-001). The Birmingham rate stays tier C.
- `https://birminghamal.hdlgov.com/Home/Home/Taxes`: not fetched (portal).
- Workforce Alabama 2026 tax-rate schedule and shared cost: no public page found. The FAQ points to the UC-216 notice in eGov (gated per employer).

## Open questions
- **AL-OQ-1.** 2026 UC rate schedule (A–D) and shared-cost percentage. What would close it: the Workforce Alabama 2026 tax-rate announcement or press release (Experience Rating Section, 334-954-4741), or an employer's 2026 UC-216 notice (owner or client).
- **AL-OQ-2.** Census of municipal and county occupational taxes: rates, collectors and frequencies.
  - Only Leeds is A.2. Birmingham is C.
  - What would close it: the Alabama League of Municipalities occupational-tax list, then each city's ordinance or tax page (Birmingham Code Title 3 Ch. 2; Auburn, Bessemer, Gadsden, Opelika, Fairfield, Macon County, etc.).
  - This is naturally parallel: one lookup per locality, which the orchestrator can fan out.
- **AL-OQ-3.** AL income-tax treatment of qualified transit (IRC 132(f)) and group-term life (IRC 79). Neither is on the booklet exclusion list. What would close it: ADOR Admin. Code 810-3-71 or an ADOR FAQ on fringe benefits.
- **AL-OQ-4.** Employer processing fee under an AL child-support IWO. What would close it: 30-3-60..71 read in full via ALISON GraphQL, or the DHR Child Support employer page.
- **AL-OQ-5.** Whether ADOR issued a rule or FAQ in 2026 on day-counting under Act 2025-334 (lead: Bradley, 2026-09). What would close it: the ADOR Rules page (Admin. Code 810-3-71 amendments in the Alabama Administrative Monthly, 2026).
- **AL-OQ-6.** The end date of the Act 2023-421/2024-437 overtime withholding exemption: 2025-06-30, tier B only. What would close it: the ADOR "Overtime Pay Exemption Amended Pursuant to Act 2024-437" page linked from US-ALS5-004.

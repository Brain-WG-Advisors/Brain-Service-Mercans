# Stage 5: ID (Idaho), findings across the 13 domains

Worker: compliance-source-hunter, 2026-11-02, about 08:20 to 09:05 local. Declared budget: 60 fetches and 2 h. Used: about 46 fetches, counting Wayback CDX queries and one web search for leads, in about 45 min.

- **Shard:** `00-official-sources/_register-shards/S5-ID.csv`, rows US-IDS5-001..025 (25 rows).
  - By tier: 16 A.1, 7 A.2, 2 A.3.
  - By status: 23 active, 1 superseded (the 2025 table edition, kept for the mid-year change), 1 partial (the Form ID W-4 edition).
- **Sources:** `00-official-sources/ccg-sources/ID/`, 36 source files plus their `.txt` extracts, 9.7 MB in total.
  - The largest file is the 2026 legislation index HTML, at 3.6 MB.
  - No file is over 5 MB.
- **Reused, not re-fetched:**
  - US-IDP51-001 (63-3035) and US-IDP51-002 (45-609).
  - US-IDP52-001/-002/-003/-004/-005.
  - US-IDR3-001/-002/-003, US-IDP7-001, US-IDP9M-001 and US-KYR3-003.

## Access findings
- **The VPN was off for this run.** ipinfo showed a Brazilian exit. From this network, `tax.idaho.gov`, `labor.idaho.gov` and `legislature.idaho.gov` all time out on direct curl, with HTTP 000.
- **Every source in this shard therefore comes from a Wayback `id_` copy of the official URL.** The snapshot date is in the `authority` column. The content is the agency's or Legislature's own HTML or PDF, so tiers A.1/A.2 are kept.
- Wayback returned "Temporarily Offline" once, for about 1 minute, then recovered.
- **Not archived:**
  - `tax.idaho.gov/.../withholding/information-returns/`: wrong path, replaced by the `filing-information-returns-1099s-w-2s` page.
  - The H0544 (2026) bill PDF.
  - Any 2026 edition of Form ID W-4 (EFO00307). The CDX lists editions up to 04-28-2025 only.

## 1 — labour_code
- **State minimum wage: USD 7.25/h.** The statute says it "shall conform to, and track with, the federal minimum wage" [US-IDS5-001, A.1, 44-1502(1)].
  - Nothing is indexed by the state.
  - 2027: none enacted. H0813 (2026, "Minimum wage") was filed only [US-IDS5-024].
- **Tipped employees:** the direct cash wage must be at least USD 3.35/h, so the tip credit is up to 3.90. The employer makes up any shortfall [US-IDS5-001].
  - Pooled tips that are shared out do not count as tips received.
  - A tipped employee is one who customarily receives more than USD 30 a month in tips [US-IDS5-002].
- **Opportunity wage:** USD 4.25/h for employees under 20, during their first 90 consecutive calendar days. Displacing other workers to use it is prohibited [US-IDS5-001, 44-1502(3)].
- **Local minimum wages: none.** Political subdivisions may not set a higher minimum wage [US-IDS5-001, 44-1502(4)]. H0812 (2026, "minimum wages, cities, counties") was not enacted [US-IDS5-024].
- **Exclusions from the state minimum wage** [US-IDS5-003, 44-1504]:
  - executive, administrative and professional employees (EAP), and outside sales;
  - domestic service;
  - seasonal staff of nonprofit camps;
  - under-16s working part-time, up to 4 h/day;
  - under-18s employed by family;
  - several agricultural cases (family members, piece-rate commuting harvest hands, range livestock).
  - The state "employer" definition excludes the US, the state and political subdivisions [US-IDS5-002]. Government employees therefore fall under the FLSA only.
- **Overtime: no state rule beyond the FLSA.**
  - Chapter 44-15 has no overtime section (index read, 2026-10-24 snapshot).
  - The IDOL guide describes overtime only under the federal act [US-IDS5-025, A.3].
  - There is no daily overtime and no weekend or holiday premium.
- **Pay frequency and pay day** [US-IDS5-004, 45-608]:
  - Pay at least once a calendar month, on regular paydays designated in advance.
  - The pay period must end not more than 15 days before payday.
  - A payday that falls on a nonworkday moves to the preceding workday.
  - Civil penalty: up to USD 500 per pay period for a pattern of late pay.
- **Method of payment:**
  - Lawful money, or checks that can be cashed without charge.
  - Direct deposit only with the employee's voluntary authorization, into an account of the employee's choice. Revoking the authorization restores payment by check or cash [US-IDS5-004].
  - Paycards are not addressed in 45-608. See Open questions.
- **Notices** [US-IDS5-006, 45-610]:
  - At hire: rate of pay and usual payday, in writing on request.
  - Before work is performed: any reduction in wages.
- **Confidence:** 95%.

## 2 — income_tax
- **Rate:** flat 5.3% of Idaho taxable income [US-IDS5-007, A.1, 63-3024].
  - The rate applies above a threshold of USD 2,500 (single) or USD 5,000 (joint). These thresholds are CPI-indexed.
  - The rate has been in force since tax year 2025: 2025 ch. 13 (H 40).
  - The 2026-10-25 snapshot shows no 2026 amendment.
  - H0589, H0782 and H0605 (tips/overtime) were filed in 2026 but not enacted [US-IDS5-024].
- **Withholding duty:** withhold an amount "substantially equivalent" to the tax, using the Commission's tables [US-IDP51-001, 63-3035(a)].
- **Methods** [US-IDS5-008, A.2]:
  - percentage computation, rounded to the nearest whole dollar;
  - annualized wage;
  - wage bracket (EPB00745).
- **Allowance value = 0.** The Idaho Child Tax Credit sunset (63-3029L).
  - S1450 (2026, "child tax credit, permanent") was not enacted [US-IDS5-024].
- **2026 tables changed mid-year (a `mid_year_rate_change` case).**
  - 2026-01-01 to 2026-07-22, EPB00744 edition 04-28-2025 [US-IDS5-012, superseded]: 5.3% over single 15,000 / married 30,000 per year.
  - From 2026-07-23, EPB00744 edition 07-23-2026 [US-IDS5-011, active]: 5.3% over single 16,100 / married 32,200 per year.
  - Per-period thresholds in the 07-23-2026 edition:
    - single: monthly 1,342, semimonthly 671, biweekly 619, weekly 310, daily 62;
    - married: 2,683 / 1,342 / 1,238 / 619 / 124.
  - Tables apply prospectively, with no retro catch-up [US-IDS5-008].
  - **G-DERIVE:** every per-period threshold equals the annual amount divided by 12/24/26/52/260, rounded to a dollar. Example: 16,100/26 = 619.23, published as 619. Both editions were recomputed in Python (`derived arithmetically`).
  - The 2026 annual thresholds (16,100 / 32,200) equal the 2026 federal standard deductions in FED.md [US-FEDS5-010], so the zero bracket is the federal standard deduction. This is an observation; the STC does not state it.
- **Oracle:** the STC worked examples [US-IDS5-008].
  - Single, biweekly 1,212 → 5.3% × (1,212 − 619) = 31.43, rounded to **31**. This matches the 07-23-2026 table.
  - Married, weekly 1,000 → annual 52,000 − 32,000 = 20,000 × 5.3% = 1,060, /52 = 20.38, published as **20**.
  - **Discrepancy:** the page's married annual example uses "over 32,000". That matches neither table (32,200 in 2026; 30,000 in 2025). Exact figures should be taken from EPB00744, not from the example. See Open questions.
- **Supplemental wages:** aggregate with regular wages, or apply a flat 5.3% to a separately issued payment [US-IDS5-008; US-IDP52-001].
- **Certificate:**
  - A federal W-4 must be on file. Form ID W-4 (EFO00307) is "strongly encouraged".
  - Latest edition obtained: 04-28-2025 [US-IDS5-013, status partial; 2026 edition not captured].
  - Statuses: A Single/HoH, B Married, C Married at single rate.
  - Allowances: children aged 16 or under, +2 for HoH. Exempt only if there was no liability last year and none is expected this year (valid one year [US-IDP52-002]).
- **Residents and nonresidents** [US-IDS5-020; US-IDP52-002]:
  - All wages for services physically performed in Idaho are Idaho-source.
  - A nonresident is withheld on once they earn over USD 1,000 in Idaho in the calendar year. All Idaho wages go on the W-2 whether or not tax was withheld.
  - Idaho residents working elsewhere are taxable on all income. Idaho withholding on that pay is optional.
  - Out-of-state employers must withhold for employees physically in Idaho.
- **Reciprocity:** none. The STC exceptions list names no agreement [US-IDP52-002].
- **Local income taxes:** none. The STC tax menu lists no city, county or district wage tax [US-IDP52-003].
- **Confidence:** 95% (the W-4 edition is the only gap).

## 3 — social_security
- **SUI, administered by the Idaho Department of Labor:**
  - 2026 taxable wage base: **USD 58,300**.
  - New-employer (standard) rate: **1.000%** = 0.970% UI + 0.000% administrative + 0.030% workforce development.
  - Positive-balance classes: 0.208% to 0.694%. Deficit classes: 1.250% to 5.400% [US-IDP52-004, US-IDP7-001].
  - No employee contribution.
- **Statutory mechanism** [US-IDS5-014, A.1, 72-1350]:
  - Wage base = average annual covered wage of the penultimate year, rounded to the nearest USD 100, or the FUTA base if higher.
  - Base tax rate = 2.1% × (2 − fund balance ratio / AHCM), between 0.6% and 3.4%. The desired fund size multiplier is 1.2 from 2024.
  - The director sets next-year rates before Dec 31.
  - New employers stay on the standard rate for at least 6 quarters [US-IDS5-021].
- **G-DERIVE: not possible here.** The penultimate-year (2024) average annual covered wage was not obtained, so 58,300 rests on the 2026 rate array alone [US-IDP52-004].
- **2027 wage base: not yet published.** The newest rates-page snapshot is 2026-08-03 and shows no 2027 figure. See Open questions.
- **Coverage** [US-IDS5-022, 72-1315]:
  - general: USD 1,500 in a quarter, or 20 weeks;
  - agricultural: USD 20,000 cash in a quarter, or 10 workers on 20 days. H-2A wages count for coverage but are not taxed [US-IDS5-021];
  - domestic: USD 1,000 cash in a quarter;
  - government and nonprofits: covered;
  - LLC members of an LLC taxed as a corporation: treated as corporate officers.
  - Corporate officers can opt out of UI by a form filed before March 31 [US-IDS5-021].
- **Exempt services:** 21 categories [US-IDS5-023, 72-1316A]. See special populations below.
- **SDI/TDI/PFML/LTC: none.**
  - The 2022 Idaho Paid Family Leave Act (H0447) died in committee [US-IDS5-018].
  - The federal PFML/TDI lists omit Idaho [US-KYR3-003].
  - Employer levies: workforce development is inside the UI rate [US-IDP7-001]; no other levy.
- **Confidence:** 90%.

## 4 — payslip_statute
- **Content required:** only a written statement of the deductions made, for each pay period in which deductions are made [US-IDP51-002, 45-609(2); US-IDS5-025]. Willful failure is a misdemeanor.
  - No full itemised pay-statement statute exists.
  - The CCG should treat hours, rate and gross as best practice plus FLSA records, not as a state mandate.
- **Delivery:** no Idaho rule on electronic delivery or consent was located (none in chapter 45-6, index read [US-IDS5-006 file]).
- **Language:** none required. English and Spanish posters are offered [US-IDP9M-001].
- **Retention:** employment records for 3 years from the last date of service [US-IDS5-006, 45-610(1)]. The IDOL guide lists the record fields [US-IDS5-025].
- **Confidence:** 85% (the negative on electronic delivery rests on the chapter index and guide, not on a search of all statutes).

## 5 — reporting_instruments
- **Withholding registration:** Idaho Business Registration (IBR) at business.idaho.gov, one form for STC and IDOL. File within 6 months of becoming a covered employer (UI), or face a penalty of up to USD 500 [US-IDS5-021].
- **Form 910 (withholding payment/return), filed online in TAP** [US-IDS5-009]:

  | Cycle | Who | Due date |
  |---|---|---|
  | Semimonthly | ≥ 25,000/month or ≥ 300,000 in 12 months | 20th for the 1st–15th; 5th of the next month for the 16th–end |
  | Monthly | < 25,000/month and > 750/quarter, or only one monthly pay period | 20th of the following month |
  | Quarterly | ≤ 750/quarter, or a farmer filing with IDOL | last day of the month after the quarter |
  | Annual | < 750/year, or a farmer not filing with IDOL | last day of January |

  - A zero return is required.
  - Tax is reported by the date wages are paid.
  - The cycle is fixed for the calendar year. Change requests are due by Nov 15.
  - PEOs may file under the PEO EIN.
- **Form 967 annual reconciliation and W-2s** [US-IDS5-010]:
  - Due the last day of January; 1099s with Idaho withholding are due the last day of February.
  - Electronic: an **EFW2** file (SSA Pub. 42-007) plus Idaho state-specific records, uploaded in TAP. The specs are on the STC Software Developers page, which was not fetched. A valid EFW2 file generates the 967 (RV record).
  - W-2s can also be keyed in TAP.
  - Penalty: USD 2 per month per missing W-2/1099, minimum 10, maximum 2,000.
  - Amounts are rounded to the nearest dollar.
- **Quarterly UI report (TX20, plus TX26 continuation; TX20C for amendments)** [US-IDS5-021]:
  - Due the last day of the month after the quarter (72-1311), with no grace period.
  - Online filing in the Employer Portal is mandatory. Paper is allowed only on an approved written request.
  - Zero reports are required.
- **New hire** [US-IDS5-015, 72-1604]:
  - Report to IDOL within **20 calendar days** of hire or rehire. Electronic filers send 2 transmissions a month, 12–16 days apart.
  - Fields: employee name, address and SSN; employer name, address and FEIN; Idaho UI account number; hire date; multistate flag.
  - A copy of the W-4 is accepted.
- **Authorisation:** Form ID-POA (withholding) [US-IDR3-001] and the IDOL Employer Portal Authorization form [US-IDR3-002].
- **Confidence:** 90% (the Idaho EFW2 state-record spec was not fetched).

## 6 — leave
- **No state paid sick leave, vacation, holiday or bereavement mandate** [US-IDS5-025]. H0641 (2026, "use of earned sick leave") FAILED [US-IDS5-024].
- **No PFML** [US-IDS5-018].
- **Military leave:** H0544 (2026) amended the military leave-of-absence provisions; it is LAW, ch. 57 [US-IDS5-024]. The text was not read; the bill page describes leave "from regular duties for military". Payroll impact for private employers is open.
- **Local leave ordinances:** no statute pre-empting local leave was located. The web-search lead "44-2701..2704" turned out to be the non-compete chapter, a tier-B error, and was discarded. No Idaho city leave ordinance was found either. See Open questions.
- **Confidence:** 80%.

## 7 — termination
- **Final pay** [US-IDS5-005, 45-606]:
  - Applies to layoff and to termination by either party; discharge and resignation are treated alike.
  - Deadline: the earlier of the next regular payday or 10 days, excluding weekends and holidays.
  - On the employee's written request: within 48 hours, excluding weekends and holidays.
  - Piece-rate and commission workers get at least minimum wage for the last period within that limit, and the balance by the next payday.
- **Accrued vacation payout:** no statute. The IDOL guide says vacation and severance are "matters for agreement" [US-IDS5-025]. Whether accrued vacation counts as "wages" under 45-601(7) depends on policy; this is open.
- **Separation notice:** not required ("a discharge notice or a reason for discharge" is not required by Idaho law [US-IDS5-025]). No state UI separation notice obligation was located; the IDOL portal has a "Manage Separations" permission [US-IDR3-002].
- **State WARN law:** none located (not searched further).
- **Confidence:** 85%.

## 8 — benefits_in_kind
- **Conformity:** Idaho adopts the IRC as in effect on **2026-01-01** (static conformity, 2026 ch. 1 / H0559) [US-IDS5-019, 63-3004].
  - Federal wage exclusions therefore carry over to Idaho wages: 401(k), 125, HSA, transit, group-term life.
  - 401(k) and cafeteria-plan deferrals follow the IRC [US-IDP52-001].
  - No Idaho departure was located.
- **UI wages:** these include the reasonable cost of board and lodging (a minimum-wage definition) [US-IDS5-002]. For domestic workers, UI tax applies to noncash wages as well [US-IDS5-021].
- **Confidence:** 85%.

## 9 — deductions_garnishments
- **Deduction authorization:** no deduction unless required by law, or authorized in writing by the employee for a lawful purpose [US-IDP51-002, 45-609(1)].
- **Ordinary garnishment:** the lesser of 25% of disposable earnings or the excess over 30 × the federal minimum wage. This mirrors the CCPA [US-IDS5-016, 11-207].
- **Support garnishment (11-207):** 50% if the employee supports another spouse or child, 60% if not; 55%/65% for arrears older than 12 weeks.
- **Child-support IWO** [US-IDS5-017, 32-1210]:
  - **Total cap: 50% of disposable earnings**, which is stricter than the CCPA 60/65%. The cap applies to current support plus arrears, and the fee sits inside it.
  - Answer a court order within 10 days.
  - Remit to Health and Welfare within 7 business days of the pay date.
  - Employer fee: up to **USD 5 per withholding**.
  - Out-of-state orders follow the law of the principal place of employment.
  - Multiple orders: current support first, then pro rata.
  - The snapshot is dated 2025-02-06.
- **State tax levies:** not researched. See Open questions.
- **Confidence:** 85%.

## 10 — collective_agreements (prevailing wage)
- **No state prevailing-wage law** (repealed 1985) [US-IDR3-003, US-INR3-005].
- Idaho Code 44-1001 requires 95% Idaho residents on public works but sets no wage rate [US-IDP52-005].
- No certified-payroll duty at state level. Davis-Bacon applies to federal projects.
- **Confidence:** 90%.

## 11 — indexation
- **Minimum wage:** tracks the federal rate; no state index [US-IDS5-001].
- **SUI wage base:** average annual covered wage of the penultimate year, rounded to USD 100 [US-IDS5-014]. Published each year in the rate class array [US-IDP52-004] and in a notice to employers [US-IDS5-021].
- **PIT thresholds (2,500/5,000):** CPI-U factor set by the STC [US-IDS5-007].
- **Withholding tables:** reissued "as needed, usually partway into a year" [US-IDS5-008], as in EPB00744 07-23-2026 [US-IDS5-011].
- **Confidence:** 85%.

## 12 — data_protection
- **No Idaho rule on SSN truncation on pay statements was located.** The research was limited to the wage chapters 45-6 and 44-15; the chapter 28-51 breach-notice law was not read.
- Form ID W-4 requires the full SSN [US-IDS5-013]. The new-hire report requires the SSN [US-IDS5-015].
- **Confidence:** 50%. See Open questions.

## 13 — live_legal_change (2026-01-01 to today)
- **IRC conformity:** H0559, ch. 1, conforms to the IRC as of 2026-01-01. In force [US-IDS5-019, US-IDS5-024]. Level: withholding and assessment.
- **New withholding table, EPB00744 07-23-2026:** zero bracket 16,100/32,200. In force prospectively from issue [US-IDS5-011]. Level: withholding.
- **Not enacted in 2026:**
  - minimum wage (H0813, H0812);
  - sick leave (H0641, FAILED);
  - income tax bills (H0589, H0782, H0605);
  - permanent child tax credit (S1450) [US-IDS5-024].
- **Military leave:** H0544, ch. 57, enacted. Text not read.
- **2027:** nothing enacted for wages or tax. The 2027 SUI base and rates had not been published as of the 2026-08-03 snapshot.

## Special populations (US-OWN-005, state round)

| Population | Idaho rule | register_id |
|---|---|---|
| Domestic / household | Excluded from the state minimum wage. Income tax: the employer holds an account and files W-2/967, but withholding is **not required**. UI: covered at 1,000 cash in a quarter; tax on cash and noncash wages | US-IDS5-003, US-IDS5-020, US-IDS5-022, US-IDS5-021 |
| Agricultural | Several minimum-wage exclusions. Withhold only where federal withholding applies and the worker earns ≥ 1,000/yr; Form 910 quarterly or annual. UI: 20,000 per quarter or 10 workers/20 days; H-2A not taxed | US-IDS5-003, US-IDS5-020, US-IDP52-002, US-IDS5-022 |
| Minors | Under-20 opportunity wage 4.25 for 90 days; under-16 odd jobs and under-18 family employment excluded from the minimum wage. UI-exempt: under-21 employed by a parent, under-18 newspaper carriers. No state hours rule for 16+; child labour hours are federal | US-IDS5-001, US-IDS5-003, US-IDS5-023, US-IDS5-025 |
| Tipped | Cash wage ≥ 3.35; tipped = more than 30/month in tips; employer makes up any shortfall | US-IDS5-001, US-IDS5-002 |
| Clergy / religious | UI-exempt: churches, church-controlled organisations, seminaries, ministers. Income tax: follows federal (IRC conformity) | US-IDS5-023, US-IDS5-019 |
| Students | UI-exempt: students working for their own school; under-22 work-study students; student nurses and interns | US-IDS5-023 |
| Nonresident aliens | Form ID W-4: status A, 0 allowances, additional 15/31/33/66 per weekly/biweekly/semimonthly/monthly pay (India students 0). This is the 2025 edition; the 2026 edition is unverified | US-IDS5-013 |
| Nonresidents (US) | Withhold once Idaho earnings exceed 1,000 in the year | US-IDS5-020, US-IDP52-002 |
| Statutory employees | No Idaho withholding required | US-IDS5-020 |
| Corporate officers | Employees for withholding; UI reportable, with an opt-out form filed before March 31 | US-IDS5-020, US-IDS5-021 |
| Government employees | Outside the state minimum-wage law (FLSA applies). UI covers governmental entities, but elected officials, legislators, the guard, emergency temps and election workers paid < 1,000 are exempt | US-IDS5-002, US-IDS5-022, US-IDS5-023 |
| Interstate motor/rail/air/water carrier staff | Withhold for the state of residence (air: residence and the state with > 50% of wages) | US-IDP52-002 |
| Tribal members | No withholding for an enrolled member living and earning on the reservation | US-IDP52-002 |

## MULTI hand-offs (answered for ID)
- **SUI wage-base credit (MULTI-OQ-2):** yes, conditionally. Wages paid to the same worker in another state count toward the Idaho base, but only if tax was paid on them to that state (72-1349(1), as stated by IDOL) [US-IDS5-021, A.3]. The text of 72-1349 itself was not read.
- **PFML/SDI coverage of multistate workers (OQ-3):** not applicable; Idaho has no programme [US-IDS5-018].
- **Paid-sick-leave coverage of partial in-state work (OQ-4):** not applicable; there is no state PSL [US-IDS5-025, US-IDS5-024].
- **Pay-statement reach (OQ-8):** the 45-609 deductions statement applies to "employers" under chapter 45-6 with no territorial clause. Default: the work-location rule.
- **Withholding threshold:** nonresidents are withheld on above 1,000 [US-IDS5-020]. No convenience rule; no reciprocity.

## ACCESS gaps
- Direct access fails from this network without the VPN: `https://tax.idaho.gov/`, `https://www.labor.idaho.gov/`, `https://legislature.idaho.gov/` (curl timeout, HTTP 000). Wayback was used for every row.
- Form ID W-4 2026 edition: `https://tax.idaho.gov/document-mngr/forms_EFO00307/`. The Wayback CDX for `tax.idaho.gov/wp-content/uploads/forms/EFO00307*` lists editions only up to `EFO00307_04-28-2025.pdf`.
- H0544 (2026) text: `https://legislature.idaho.gov/wp-content/uploads/sessioninfo/2026/legislation/H0544.pdf`. Not archived (Wayback 404).
- IDOL handbook coverage chart, p.3: an image in `Handbook_Tax-information_Nov.-2025-1.pdf`. Not text-extractable; the thresholds were taken from 72-1315 instead.
- 2027 UI rate array: no `labor.idaho.gov/wp-content/uploads/*Class-array_2027*` in the CDX as of 2026-11-02.

## Open questions
- **ID-OQ-1:** Form ID W-4 2026 edition. Does it carry new nonresident-alien add-on amounts and the 2026 multiple-jobs factor (the 2025 form uses 15,000 and 3,868)? What would close it: EFO00307 at its current edition date from the STC withholding forms page (orchestrator's Chrome pass or the VPN).
- **ID-OQ-2:** The STC computing page's married annualized example uses "over 32,000". This matches neither EPB00744 edition (2026: 32,200; 2025: 30,000). What would close it: the STC's own explanation. Until then, the builder uses EPB00744 07-23-2026 for numbers and treats the example as illustrative.
- **ID-OQ-3:** The 2027 SUI taxable wage base and rate array (IDOL, usually published Nov–Dec). Also the 2024 average annual covered wage, so that 58,300 can be derived. What would close it: the IDOL 2027 Tax rate Class array PDF and the IDOL annual wage-base notice.
- **ID-OQ-4:** The Idaho EFW2 state-specific record layout (RS/RV fields). What would close it: the STC Software Developers page, "W-2 e-file specifications" PDF.
- **ID-OQ-5:** Paycard wage payment, which 45-608 does not address. Is it permitted with consent? What would close it: an IDOL Wage and Hour statement or an IDAPA rule.
- **ID-OQ-6:** Whether accrued vacation is payable at separation when policy is silent (45-601(7) "wages"). What would close it: IDOL Wage and Hour guidance on vacation payout, or an Idaho Supreme Court decision on 45-606.
- **ID-OQ-7:** Whether a statute pre-empts local paid-leave ordinances (the search lead was wrong), and whether any Idaho city has such an ordinance. What would close it: a full-text search of the Idaho Code for "political subdivision" with "leave" (Legislature site).
- **ID-OQ-8:** State tax levy on wages (STC levy and garnishment procedure, 63-3061ff) and its priority against IWOs. What would close it: the STC "wage garnishment" employer page or the statute.
- **ID-OQ-9:** Data protection: Idaho Code 28-51 (breach notice) and any SSN display rule. What would close it: the chapter 28-51 text.
- **ID-OQ-10:** The H0544 (2026) military leave text and whether it reaches private employers. What would close it: the enrolled bill or Session Law ch. 57.

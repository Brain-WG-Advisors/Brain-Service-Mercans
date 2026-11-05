# Stage 5 — Oregon (OR): 13-domain findings

Worker: compliance-source-hunter, 2026-11-02. Brief: `_prompts/stage5-brief.md`. Mandate block: US-MQ-57 (answered; part 5 re-answered 2026-11-02 on US-ORP10-001). Tier T4 (verified): the state layer plus the Metro SHS / Multnomah PFA local layer, which is filed with the City of Portland.

**Budget.** Declared 60 fetches / 2 h. Used about 33 fetches (curl, including 6 web.archive.org statute pulls and 1 BLS API call) plus 3 web searches, in about 50 minutes.

**Register shard.** `00-official-sources/_register-shards/S5-OR.csv` holds 28 rows, US-ORS5-001..028. New files are in `00-official-sources/ccg-sources/OR/` (17 new files, about 5.3 MB in total, none over 5 MB). The ORS chapter HTML files are the largest at 0.3–1.3 MB each.

**Access notes**
- **VPN was off.** ipinfo showed a BR exit (Telefonica). oregon.gov, portland.gov, doj.state.or.us, paidleave.oregon.gov and api.bls.gov all answered from BR.
- **oregonlegislature.gov timed out.** The connection itself failed (HTTP 000), not a 403. All ORS chapters were pulled through `https://web.archive.org/web/2026id_/<url>`:
  - snapshots: ors653 2026-10-24, ors018 2026-10-05, ors646A 2026-10-31, ors657 2026-05-12, ors657B 2026-04-23, ors316 2026-05-13;
  - all are the 2025 Edition. The ors653 page carries the note "amended or repealed during its 2026 regular session".
  - Wayback serves the files gzip-compressed. They were decompressed before saving.
- **Defect found in an earlier file (F23-adjacent):** `00-official-sources/pdfs/OR/ors652.html_wayback-20261013013758.html` is **gzip-compressed** HTML. It reads as binary unless you gunzip it. It was read this pass through a decompressed scratch copy and was not modified (the file is not mine). The synthesis should replace it with a decompressed copy.

**Active rows reused without a re-fetch:**
- US-OR-001 / US-ORP51-002: 150-206-436 (2026). Re-read in full; brackets now carried by US-ORS5-009.
- US-OR-002: 211-155-2 (2026). Re-read; detail now in US-ORS5-010.
- US-ORP10-001: 150-206-692. Re-read.
- US-ORP51-003 / US-ORL-001: ORS 652.610.
- US-ORP51-004: BOLI prevailing wage.
- US-ORP51-005: OR-AUTH-REP and OR-AUTH-INFO.
- US-ORP7-001..006: the levies.
- US-ORP9L-001: posters.

**Rows that can close older rows (for the synthesis):**
- US-ORS5-005 (A.2, Portland Revenue thresholds table) replaces **US-ORP7-007 (tier B, MANUAL)**.
- US-ORS5-004 supersedes US-OR-003. It carries the same facts plus the W-2, XML and penalty detail. Note that US-OR-003's "125k/200k thresholds" are the liability thresholds, not the withholding trigger.
- US-ORS5-011 closes the GAP "Effective date unverified" on US-ORP7-001: the statewide transit tax (STT) has been withheld since 2018-07-01.

---

## 1. labour_code
- **Minimum wage.** ORS 653.025 sets three tiers [US-ORS5-001], with the rates from BOLI [US-ORS5-002]:

  | Period | Standard | Portland metro (inside the urban growth boundary) | Nonurban (the 18 counties in ORS 653.026) |
  |---|---|---|---|
  | 2025-07-01 to 2026-06-30 | 15.05 | 16.30 | 14.05 |
  | 2026-07-01 to 2027-06-30 | 15.55 | 16.80 | 14.55 |
  | from 2027-07-01 | set by April 30, 2027 | standard + 1.25 | standard − 1.00 |

  - **G-DERIVE (done in Python, verification = derived arithmetically) [US-ORS5-023]:**
    - Rule: the standard rate rises by the March-to-March change in CPI-U, rounded to the nearest 0.05.
    - 15.05 × 330.213 / 319.799 = 15.5401, which rounds to **15.55**.
    - Prior year: 14.70 × 319.799 / 312.332 = 15.0514, which rounds to **15.05**.
    - Metro: 15.55 + 1.25 = 16.80. Nonurban: 15.55 − 1.00 = 14.55. Both match BOLI exactly.
  - Rules on the BOLI page:
    - No tip credit (tips cannot count toward the minimum wage). Minors get the same rate.
    - The rate is that of the county where the employee works 50% or more of weekly hours. A work location inside the metro urban growth boundary gives the metro rate.
    - A shift straddling June 30 / July 1 is paid at two rates.
  - **Local minimum wages:** none. The tiers are statewide by location; there is no city ordinance layer.
- **Overtime beyond FLSA** [US-ORS5-008]:
  - **General rule:** 1.5× after 40 hours per workweek (ORS 653.261).
  - **Manufacturing, mills and factories (ORS 652.020):**
    - maximum 10 h/day and 55 h/week (60 with written consent);
    - up to 3 hours beyond the daily limit, paid at 1.5×;
    - sawmills, planing and shingle mills, logging camps: 8 h/day and 48 h/week.
  - **Canneries, driers and packing plants (ORS 653.265):** 10 h/day, 55 h/week.
  - **Agricultural workers (ORS 653.272):** 1.5× above **48 h/week in 2025–2026**, and above **40 h/week from 2027-01-01** (Or Laws 2022 c.115 s.3).
  - **Domestic workers (ORS 653.547):** 1.5× above 40 h (44 h if living in), plus 24 consecutive hours of rest per week.
- **Pay frequency and timing (ORS 652.120)** [US-ORS5-006]:
  - Regular paydays, no more than 35 days apart.
  - An undisputed shortfall below 5% of gross is paid by the next payday; 5% or more within 3 business days of notice.
- **Method of payment (ORS 652.110)** [US-ORS5-006]:
  - Checks must be negotiable without discount.
  - Direct deposit to an Oregon financial institution is allowed.
  - A check must be issued on the employee's request.
  - Paycard or ATM card only by an agreement written in the employer's principal language of communication with the employee, with a free full withdrawal or a free alternative. Revocation takes effect 30 days after notice (10 days for seasonal farm and packing workers).
- **Confidence: 95%.**

## 2. income_tax
- **Instruments:**
  - ORS 316.037, 316.048, 316.162 and 316.167 [US-ORS5-020];
  - DOR 150-206-436 *Withholding Tax Formulas*, effective 2026-01-01, Rev. 12-31-25 [US-ORS5-009; US-OR-001];
  - Form OR-W-4 2026, 150-101-402, Rev. 07-28-25 [US-ORS5-012].
- **Method: annual formula.**
  - **BASE** = wages − federal tax withheld (capped) − standard deduction.
  - **Standard deduction:**
    - 2,910 for single filers, and for single with fewer than 3 allowances;
    - 5,820 for married filers, and for single with 3 or more allowances.
  - **Federal-tax subtraction cap:** 8,750. It phases out:
    - single: 7,000 / 5,250 / 3,500 / 1,750 / 0 for wages of 125k–130k / 130k–135k / 135k–140k / 140k–145k / 145k and over;
    - married: the same steps at 250k–290k.

  | Wages | Status | BASE | Formula |
  |---|---|---|---|
  | < 50,000 | Single | 0–4,550 | 263 + BASE × 0.0475 |
  | | | 4,550–11,400 | 479 + (BASE − 4,550) × 0.0675 |
  | | | 11,400–50,000 | 941 + (BASE − 11,400) × 0.0875 |
  | | Married | 0–9,100 | 263 + BASE × 0.0475 |
  | | | 9,100–22,800 | 695 + (BASE − 9,100) × 0.0675 |
  | | | 22,800–50,000 | 1,620 + (BASE − 22,800) × 0.0875 |
  | ≥ 50,000 | Single | up to 125,000 | 678 + (BASE − 11,400) × 0.0875 |
  | | | over 125,000 | 10,618 + (BASE − 125,000) × 0.099 |
  | | Married | up to 250,000 | 1,357 + (BASE − 22,800) × 0.0875 |
  | | | over 250,000 | 21,237 + (BASE − 250,000) × 0.099 |

  - Then subtract **263 per allowance**. Allowances are 0 for single filers over 100,000 and married filers over 200,000. A negative result is 0.
  - Divide the annual amount by 12 / 24 / 26 / 52 / 260 for the pay period.
  - An employer's own formula needs DOR approval.
- **Arithmetic check** (Python; the constants are cumulative):
  - 263 + 4,550 × 0.0475 = 479.1
  - 479 + 6,850 × 0.0675 = 941.4
  - 263 + 9,100 × 0.0475 = 695.25
  - 695 + 13,700 × 0.0675 = 1,619.75 (table: 1,620)
  - 678 + 113,600 × 0.0875 = 10,618
  - 1,357 + 227,200 × 0.0875 = 21,237
  - **Worked example 1 (oracle seed):** wage 25,000, federal tax withheld 1,000, standard deduction 2,910. BASE = 21,090. Withholding = 941 + 9,690 × 0.0875 = **1,789 a year**; monthly 149, biweekly 69.
- **Defects inside the 2026 DOR publication** (record them; do not "fix" them):
  - (a) The federal cap is stated as **8,500 "in 2025"** on p. 5 and in FAQ 3, but as **8,750** on pp. 6–7 and in FAQ 11.
  - (b) Example 1 prints BASE 21,165 and withholding 1,798, but its own lines compute 21,090 and 1,789.
  - Build on the pp. 6–7 formula (8,750). Flag (a) for the oracle owner.
- **Supplemental wages:** an optional flat 8% when paid at a different time from the regular payday. The **8% default** also applies when no OR-W-4 is on file (HB 2119 (2019)). An exemption expires on February 15 of the following year.
- **Rounding:** rounding to the nearest dollar is permitted, not required [US-ORS5-009].
- **Withholding wages exclude** (ORS 316.162(2)):
  - armed forces pay with no federal withholding;
  - interstate carrier employees protected by 49 U.S.C. 14503 and 40116;
  - domestic service in a private home;
  - casual labour outside the employer's trade;
  - seasonal crop labour paid under 300 a year;
  - ministers and members of religious orders;
  - independent contractors;
  - governmental 457(b) payments.

  For seasonal crop workers, the employer may elect **2% flat** withholding (316.167(1)) [US-ORS5-020].
- **Residence vs work location, and nonresidents** [US-ORS5-025]:
  - A **nonresident working in Oregon** is withheld on Oregon-service wages unless Oregon earnings for the year will be **less than the standard deduction**. 2026 amounts: single/MFS 2,910; head of household 4,685; MFJ 5,820; QSS 5,820 (2026 combined-payroll booklet).
  - An **out-of-state employer of Oregon residents working in Oregon** (including teleworking from home) must withhold, with relief at 300 or less per employee per year.
  - An employer with **no employees working in Oregon** cannot be required to withhold for residents who work elsewhere; withholding is a courtesy only.
  - **Reciprocity: none.** A full-text search of ORS ch. 316, the 211-155-2 (2026) booklet and 150-206-692 for "reciproc" returns no hit.
  - Residents get a **credit for tax paid to another state at assessment** (ORS 316.082), not at withholding.
  - No convenience-of-employer rule was found.
- **Local income taxes (T4 layer)** [US-ORS5-004, US-ORS5-005, US-ORS5-024]. These are administered by the **City of Portland Revenue Division**, on returns separate from the state.
  - **Metro Supportive Housing Services (SHS):** 1%.
    - Liability thresholds (assessment): TY2026 single 128,000 / joint 205,000; TY2027 single 132,000 / joint 211,000; 2021–2025 125,000 / 200,000. Indexed from 2026.
  - **Multnomah County Preschool for All (PFA):** 1.5% over 125,000 / 200,000, plus another 1.5% over 250,000 / 400,000. Not indexed.
    - A **+0.8% rate step is announced, but its year conflicts:** the withholding page says **2027**, the personal-tax page says **2028**. Open question OR-OQ-1.
  - **Withholding trigger:** mandatory for employees who **work** in Metro or Multnomah and earn **200,000 or more** in the calendar year. Withholding is SHS 1% and PFA 1.5%/3% on income above 200,000/400,000. Employees may opt in or out on the jurisdictions' forms.
  - **Work location rules:** a nonresident who teleworks from outside for a Metro/Multnomah employer is not taxable on that work. Work physically performed inside the district is taxable.
  - **W-2 local names:** "METRO" and "MULT".
- **Confidence: 90%.** The open items are the PFA step year and the 8,500/8,750 text conflict.

## 3. social_security (UI, PFML, levies)
- **Unemployment insurance** (OED) [US-ORS5-003, US-ORS5-015]:
  - **2026 taxable wage base: 56,700** (2025: 54,300; +4.4%, ratio 1.04420).
    - Statute: 0.80 × the average annual wage of the second preceding year, rounded to 100, never lower than the prior year (ORS 657.095(1)).
    - The 2024 average annual wage was not fetched, so the base was not re-derived from it (OR-OQ-3).
  - **Rates:**
    - 2026 is **Tax Schedule 3**. The new-employer rate is **2.4%**, confirmed by two independent authorities: the OED release and the statute.
    - New-employer rates by schedule (657.435): I 2.0, II 2.1, III 2.4, IV 2.6, V 2.9, VI 3.1, VII 3.2, VIII 3.3%.
    - Schedule III experience rates (Table A, ORS 657.462): **0.9% to 5.4%**.
    - The special payroll tax 0.00135 is embedded inside the UI rate [US-ORP7-006].
    - Penalty rate: +2%, capped at 5.4%, for delinquent filers [US-ORS5-010].
  - **Employee contribution:** none.
  - **Coverage exclusions** [US-ORS5-028]:
    - agricultural labour, unless the employer paid 20,000 or more in a quarter or had 10 workers on 20 days;
    - domestic service, unless 1,000 or more is paid in a quarter;
    - family employment;
    - student and school services;
    - officer/director family members, and a sole corporate officer who elects out with OED approval (657.044).
- **Paid Leave Oregon (PFML)** [US-ORS5-003, US-ORS5-013, US-ORS5-014, US-ORP7-004]:
  - The rate is 1% in 2026, capped by statute at 1%. Wage cap 184,500 = the Social Security wage base.
  - Split: **employee 60% / employer 40%**. Employers with fewer than 25 employees pay no employer share but still withhold the employee share.
    - Employer size uses the prior year's monthly counts **including out-of-state employees**.
  - A sole corporate officer cannot elect out of Paid Leave (but can elect out of UI) [US-ORS5-010].
  - The employer may pay the employee share as a benefit.
- **Other levies** (already registered under P7; not redone):
  - **Statewide transit tax (STT):** 0.001 withheld from employees [US-ORS5-011];
  - **TriMet:** 0.008237, employer tax;
  - **Lane Transit District:** 0.0080, employer tax;
  - **Workers' Benefit Fund (WBF):** 0.018 per hour, split half and half [US-ORS5-010; US-ORP7-001..006].
  - STT reaches **residents on all wages, wherever the work is performed**, and nonresidents on Oregon-service wages. An out-of-state employer cannot be compelled to withhold it for residents working outside Oregon.
- **Confidence: 92%.**

## 4. payslip_statute
- **Content (ORS 652.610(1)(b))** [US-ORP51-003; US-ORS5-026]:
  - (A) payment date; (B) dates of work covered; (C) employee name; (D) employer name and business registry or identification number; (E) employer address and telephone;
  - (F) pay rate(s); (G) pay basis; (H) gross wages; (I) net wages; (J) each deduction, with amount and purpose; (K) allowances claimed toward the minimum wage;
  - (L) for non-exempt employees: regular and overtime rates, hours and pay;
  - (M) piece rates, piece counts and pay per rate.
- **Delivery:**
  - Electronic only with the employee's **express agreement** and the ability to print or store the statement on receipt (1)(c).
  - The statement may be attached to the pay instrument or delivered separately.
- **New from 2026-01-01 (SB 906)** [US-ORS5-022]:
  - Each new hire must receive a written explanation of earnings and deductions: pay period, every pay-rate type, every deduction and its purpose, minimum-wage allowances, employer contributions and **all payroll codes**.
  - It must be updated by January 1 each year.
  - BOLI publishes a template in English and Spanish; agency duty under 652.610(6) [US-ORL-001].
- **Deductions:** only those required by law, or authorized in writing for the employee's benefit and recorded (652.610(3)).
- **Retention:** at least **2 years** for name, address, occupation and hours per week and per pay period (ORS 653.045) [US-ORS5-019].
- **Reach:** employers "employing, in this state". No out-of-state reach rule was found (MULTI hand-off).
- **Confidence: 90%.**

## 5. reporting_instruments
- **Combined quarterly Form OQ** [US-ORS5-010]:
  - Covers withholding, UI, Paid Leave, WBF, TriMet, Lane Transit, STT.
  - Filed with **Schedule B** (semi-weekly or next-day depositors) and **Form 132** (employee wage and hour detail).
  - Channel: **Frances Online** (OED portal). Payments through **Revenue Online** (DOR; paper voucher OR-OTC-V).
  - **2026 due dates:** Q1 2026-04-30, Q2 2026-07-31, Q3 2026-11-02, Q4 2027-02-01.
  - Deposits follow the federal schedule; new employers deposit monthly.
  - A registered employer files the OQ even with no payroll.
  - Annual filers: Form OA (household employers), Form WA and OR-STT-A (agricultural employers).
- **Annual reconciliation and W-2:**
  - Form OR-WR.
  - W-2s go electronically to DOR through **iWire**, in EFW2 or the DOR template, **by January 31** (ORS 316.202).
- **City of Portland, Metro and Multnomah** [US-ORS5-004, US-ORS5-024]:
  - Quarterly withholding returns and annual reconciliations to Portland Revenue Online, on the same due dates as Oregon's.
  - XML bulk upload: `ReturnBatch` schemaVersion 1.0, with `MetroWithholdingReturn` and `MultnomahWithholdingReturn` nodes. Account IDs: SHW-########## for Metro, MCW-########## for Multnomah.
  - W-2s in **EFW2 via Portland Revenue Online by January 31, no extension**. Penalties: 50 per W-2 (maximum 2,500 per jurisdiction); 100 for a late annual reconciliation.
- **New hire** [US-ORS5-016]:
  - To the **Oregon DOJ Child Support Program within 20 days**, including rehires.
  - Since **2024-01-01**, independent contractors are reported too: those with a W-9 expected to work more than 20 days a year, and re-engagements after 60 days.
  - Channel: Employer Services Portal (bulk spreadsheet or text upload) or form CSF 01 0580 by fax or mail.
  - Fields: FEIN, state ID, address for income withholding orders, dependent health coverage and its waiting period; employee SSN, first work date, date of birth, name, address.
  - The statutory basis cited by DOJ (ORS 25.790, OAR 137-055-4040) was not read.
- **Registration and authorization:** OR-AUTH-REP and OR-AUTH-INFO [US-ORP51-005].
- **Confidence: 90%.** The Portland annual-reconciliation XML guide was not downloaded.

## 6. leave
- **Oregon sick time (ORS 653.601–653.661)** [US-ORS5-007, US-ORS5-027]:
  - Size rule: **paid at 10 or more employees in Oregon**, unpaid below 10.
  - **Accrual:** 1 hour per 30 hours worked (or 1⅓ per 40), from day 1. The employer may cap annual accrual at 40 hours.
  - **Carryover:** up to 40 hours. The employer may cap the balance at 80 hours and use at 40 hours a year.
  - FLSA-exempt employees are presumed to work 40 hours a week. Front-loading 40 hours is an alternative.
  - **No payout at separation** (653.606(7)).
  - New permitted uses: blood donation from 2026-01-01 (SB 1108); events that qualify for Paid Leave [US-ORS5-022].
  - **The state preempts local sick-leave rules** (653.661): no city layer.
- **Paid Leave Oregon benefit side** [US-ORS5-013]:
  - Up to 12 weeks (14 for pregnancy-related) in 52 weeks. Job protection after 90 consecutive days.
  - The employer may limit top-up from accrued leave to 100% wage replacement (ORS 657B.030(2), via SB 69).
- **Confidence: 88%.** The Oregon Family Leave Act (OFLA) has no pay impact and was not researched further.

## 7. termination
- **Final pay** (ORS 652.140) [US-ORS5-006]:
  - Discharge or mutual agreement: **by the end of the first business day**.
  - Resignation with 48 hours' notice (excluding weekends and holidays): **immediately**.
  - Resignation without notice: **within 5 business days or the next payday, whichever is first**. If the employee submits time records, an estimate is paid within 5 days and the balance within 5 days of the records.
  - Termination on a weekend or holiday: by the next business day.
  - **Penalty wage:** 8 hours per day for up to 30 days (652.150).
- **Accrued vacation:** no statutory payout. **An established employer policy or agreement must be honoured** [US-ORS5-021].
- **Sick time:** no payout [US-ORS5-007].
- **UI separation notice and state WARN rules:** not researched (OR-OQ-5).
- **Confidence: 85%.**

## 8. benefits_in_kind (state conformity)
- **The base is federal taxable income with Oregon modifications** (ORS 316.048) [US-ORS5-020].
  - Federal exclusions therefore flow through: 401(k), section 125, HSA, transit, group-term life.
  - Withholding "wages" include non-cash remuneration (316.162(2)).
  - This pass found no Oregon add-back for 401(k), section 125, HSA or transit. A modification list was not read item by item, hence 70%.
- **Confidence: 70%** (OR-OQ-4).

## 9. deductions_garnishments
- **Wage exemption (ORS 18.385)** [US-ORS5-017]. 75% of disposable earnings is exempt, **and** a protected net floor applies:

  | Wages payable | Weekly | Biweekly | Semimonthly | Monthly |
  |---|---|---|---|---|
  | 2025-07-01 to 2026-06-30 | 338 | 675 | 737 | 1,458 |
  | 2026-07-01 to 2027-06-30 | 400 | 832 | 912 | 1,792 |
  | from 2027-07-01 | 30× | 60× | 65× | 130× |

  - From 2027-07-01 the multiples apply to the ORS 653.025(1) standard minimum wage. The State Court Administrator publishes the amounts each July 1.
  - **Support or restitution writs:** floor 254 / 509 / 545 / 1,090.
  - Support withholdings are deducted before a garnishment is applied.
  - Not applicable to federal tax. State-tax garnishments are outside the floor (subsections (2)–(6)).
  - No discharge because of a garnishment.
- **Wage-deduction authorization:** ORS 652.610(3) [US-ORS5-026].
  - Public-employer overpayment recoupment (SB 968, from 2026-01-01): from the prior 364 days, with 10 days' notice, at most 5% of gross per period unless the employee asks for more [US-ORS5-022].
- **Child-support IWO fees and priority beyond 18.385(5):** not researched (OR-OQ-6).
- **Confidence: 85%.**

## 10. collective_agreements (prevailing wage)
- **BOLI prevailing wage** [US-ORP51-004]:
  - Covered public works, generally 50,000 or more with public funds.
  - Base plus fringe rates. Certified payroll on form WH-38.
- **HB 2688:** off-site bespoke fabrication is covered for procurements solicited or contracted **from 2026-07-01** [US-ORS5-022].
- **SB 426 (from 2026-01-01):** owners and direct contractors are liable for unpaid wages of unrepresented employees on construction projects. A subcontractor must provide certified payroll reports on request [US-ORS5-022].
- **Confidence: 80%.**

## 11. indexation

| Item | Mechanism | Publication | Proof |
|---|---|---|---|
| Standard minimum wage | CPI-U March/March, rounded to 0.05, July 1 | BOLI rate schedule | **derived** [US-ORS5-023] |
| Metro / nonurban minimum wage | standard ±1.25 / −1.00 | BOLI | derived |
| UI wage base | 0.80 × AAW(t−2), rounded to 100, floor at prior year | OED November release | ratio checked; AAW not fetched (OR-OQ-3) |
| Paid Leave cap | = SS contribution and benefit base | OED release | equals 184,500 (FED) |
| Withholding brackets / standard deduction / exemption credit | inflation-indexed by DOR | 150-206-436 yearly | constants re-derived |
| Metro SHS thresholds | indexed from TY2026 | Portland Revenue table | read (128k/205k; 132k/211k) |
| PFA thresholds | not indexed | — | — |
| Garnishment floor | minimum wage × multiple from 2027-07-01 | State Court Administrator | statute |

## 12. data_protection
- **ORS 646A.620** [US-ORS5-018]:
  - No SSN on unrequested mail, on access cards or in public display; disposal must render it unreadable.
  - Uses required by law, and internal administrative uses, are allowed.
- **Pay statement:** ORS 652.610 does **not** list an SSN, and no Oregon rule read requires truncation on the statement. Recommended build default: omit or truncate.
- **Records:** retain at least 2 years (653.045).
- **Confidence: 75%.** Neither ORS 646A.622 (data security) nor the BOLI records rule was read.

## 13. live_legal_change (2026-01-01 to today)

**HB 3991 (2025 special session): STT increase from 0.001 to 0.002, NOT in force** [US-ORS5-011].
- Identity: parts of HB 3991 were referred to voters by **Initiative Petition 302**, certified by the Secretary of State on 2025-12-30, as **Measure 120**.
- Status: Measure 120 **did not pass** at the 2026-05-19 primary election. DOR instructs employers to continue withholding at 0.001.
- Level: withholding.

**Enacted changes for 2026, all with employer-level effect** [US-ORS5-022]:
- SB 906: new-hire explanation of earnings and deductions.
- SB 968: public-employer overpayment recoupment.
- HB 3550: exemption for minor-league baseball players under a CBA.
- SB 1108: sick time for blood donation.
- SB 69: sick time and Paid Leave alignment.
- HB 2688: prevailing wage from 2026-07-01.

**Enacted for 2027 or later:**
- Agricultural overtime above 40 hours from 2027-01-01 (ORS 653.272).
- HB 4013: minors' hours from 2027-01-01.
- Or Laws 2025 c.78: amendments to the predictive-scheduling definitions in ORS 653.412, operative 2027-07-01.
- Metro SHS TY2027 thresholds.
- The PFA +0.8% step (2027 or 2028, conflicting).
- Minimum wage 2027-07-01 (formula; not yet published).

**Rates confirmed unchanged for 2026:** UI schedule 3 and Paid Leave 1% [US-ORS5-003]; TriMet 0.008237 and Lane Transit 0.0080 "2026 and beyond" [US-ORS5-010].

**Not checked:** OED and DOR announcements for 2027 rates (normally published in November). The `next_year` entry stays open (OR-OQ-7).

---

## Special populations (US-OWN-005, state round)

| Population | Oregon rule | register_id |
|---|---|---|
| Domestic / household workers | Excluded from Oregon withholding wages (316.162(2)(c)). UI covers them only at 1,000 or more cash in a quarter (657.050). Overtime 1.5× over 40 h (44 h if living in), 24 h rest a week (653.547). Annual Form OA. | US-ORS5-020, US-ORS5-028, US-ORS5-008, US-ORS5-010 |
| Agricultural | Seasonal crop labour under 300 a year excluded from withholding; elective 2% flat (316.167). UI covers at 20,000 a quarter or 10 workers on 20 days. Overtime above 48 h in 2026, above 40 h from 2027. Annual WA / OR-STT-A. | US-ORS5-020, US-ORS5-028, US-ORS5-008 |
| Minors | Same minimum wage as adults; no youth rate. HB 4013 hours rule from 2027. | US-ORS5-002, US-ORS5-022 |
| Tipped employees | No tip credit: full minimum wage plus tips. | US-ORS5-002 |
| Clergy / religious | Excluded from Oregon withholding wages (316.162(2)(i)). UI not checked. | US-ORS5-020 |
| Students | UI excludes students working for their own school and for-credit work-experience students (657.072 area). Sick time excludes work-study participants. | US-ORS5-028, US-ORS5-027 |
| Nonresident aliens | No state rule beyond federal was found. Oregon withholding follows the 316.162 wages definition, and nonresidents are withheld only above the standard deduction. The DOR pages read carry no NRA-specific instruction. | US-ORS5-025 |
| Statutory employees | No state rule found. Independent contractors under ORS 670.600 are excluded from withholding wages; contractors are reportable as new hires since 2024. | US-ORS5-020, US-ORS5-016 |
| Government employees | Federal employees excluded from UI (657.065) and from Paid Leave benefits. Public employers have overtime exceptions (653.269) and the SB 968 recoupment rule. State employees receive pay statements electronically (652.610(2)(b)). | US-ORS5-028, US-ORS5-013, US-ORS5-022, US-ORS5-026 |
| Corporate officers | May elect out of UI (657.044) but **not** out of Paid Leave. | US-ORS5-010, US-ORS5-028 |
| Interstate carrier and airline employees | Withholding barred by 49 U.S.C. 14503 / 40116 (316.162(2)(b)). | US-ORS5-020 |

---

## MULTI hand-offs (answered for OR)
- **SUI wage-base credit for wages reported to another state:**
  - ORS 657.095(2): wages an Oregon employer pays for work in other states, where that work is covered by UI there, "shall be included in payroll". For the same employer they therefore count toward the 56,700 limit, with proof prescribed by OED [US-ORS5-015].
  - Confidence 75%. The OED rule on the form of proof was not read.
- **PFML coverage of multistate workers:**
  - Paid Leave Oregon uses the UI localization test (ORS 657B.175: localized in Oregon / base of operations / direction-control / residence) [US-ORS5-014].
  - Note: employer **size** counts out-of-state employees too [US-ORS5-013]. Answers MULTI-OQ-3 for OR.
- **Paid sick leave for employees working partly in Oregon:**
  - The statute applies to employers with employees "working anywhere in this state". The 10-employee count is of employees working in Oregon [US-ORS5-007, US-ORS5-027].
  - The accrual rule for hours worked outside Oregon (BOLI rule OAR 839-007) was not read (OR-OQ-8).
- **Pay-statement reach:** "employing, in this state" (652.610(1)(a)). No extraterritorial rule was found [US-ORS5-026].

## ACCESS gaps
- `https://www.oregonlegislature.gov/bills_laws/ors/ors653.html` (and every `/bills_laws/ors/` page): the connection failed (curl HTTP 000) from a BR exit with the VPN off. Bypassed via web.archive.org snapshots; not a content gap.
- `https://www.doj.state.or.us/child-support/for-employers/new-hire-reporting/`: 404 (wrong path). The working page is `/report-new-hires/`.
- `https://www.oregon.gov/boli/workers/pages/final-paycheck.aspx`: 404. The vacation and final-pay content came from `holiday-and-vacation-pay.aspx` and ORS 652.140.
- `https://www.oregon.gov/employ/businesses/tax/pages/default.aspx`: 404. The UI rates came from the OED release and ORS 657.

## Open questions
- **OR-OQ-1:** the year of the Multnomah PFA +0.8% rate step. The Portland withholding page says 2027; the personal-tax page says 2028.
  - What would close it: Multnomah County Code ch. 11 (PFA personal income tax), or the county's PFA tax page.
- **OR-OQ-2:** the federal-tax subtraction cap in 150-206-436 (2026), 8,500 vs 8,750 (internal conflict), and Example 1's misprinted 21,165 / 1,798.
  - What would close it: a DOR written answer (payroll.help.dor@dor.oregon.gov), or the DOR online withholding calculator run on Example 1.
  - Build on 8,750 (formula pages).
- **OR-OQ-3:** the average annual wage for 2024 behind the 56,700 base (G-DERIVE incomplete).
  - What would close it: the OED annual average wage publication (Qualityinfo / OED tax-rate notice).
- **OR-OQ-4:** an Oregon add-back for any federal fringe exclusion (HSA, section 125, transit).
  - What would close it: DOR Publication OR-17 (2025/2026), the additions and subtractions list.
- **OR-OQ-5:** whether Oregon requires a separation notice for UI at termination, and whether there is a state WARN-type law.
  - What would close it: OED employer handbook and ORS 657 / OAR 471-030 notice rules.
- **OR-OQ-6:** the employer fee and priority for child-support income withholding orders (beyond ORS 18.385(5)).
  - What would close it: ORS 25.414 and the DOJ Child Support employer handbook.
- **OR-OQ-7:** 2027 OED UI schedule and wage base, Paid Leave rate, and the 2027 DOR withholding formulas (`next_year`).
  - What would close it: the OED November 2026 rate release and DOR 150-206-436 (2027), expected late November to December 2026.
- **OR-OQ-8:** sick-time accrual for hours worked outside Oregon by Oregon-based employees.
  - What would close it: OAR 839-007-0010 / 839-007-0015 (BOLI).

# CCG research pack: core modules m01–m13 + coverage (US build)

> **Synthesis C (2026-11-02).** Register ids normalized (`_research/stage5/ID-RENAME-MAP.csv`); facts formerly blocked by the register_id pattern are promoted; module files re-deduplicated against the final annexes (build.py + finish.py re-run).

Synthesis B, CCG core worker, 2026-11-02. No fetching. Every claim below cites an active or partial row of `00-official-sources/legal-basis-register.csv`. The modules describe the **US system as three layers**: the federal core, the state-layer patterns, and the local layer. State figures appear here only as examples or comparison tables. The per-state detail lives in the annex units (`CCG-annex_XX-research-pack.md` / `-facts.json`, written by the annex workers).

**How to use the facts.** Module facts are in `_research/CCG-{unit}-facts.json`. A key that an annex unit already owns is **not duplicated**; it is listed in that file's `_annex_keys_cited` block, and the module text cites it from the named annex facts file. The namespace is jurisdiction-first: `fed.*`, `multi.*`, `{st}.*`, plus `practice.*` for build rules.

**Special populations (US-OWN-005).** All populations are in scope. The federal treatments are in m11 and the coverage matrix. State treatments are in the annexes.
**Language seams (US-OWN-006, MANDATE US-MQ-03).** The payslip and authority filings are in English. Spanish (`es`) is rank 2: it is required for notices and posters where a statute names it (AZ, CT, DE, FL), and is the primary-language template in NY and DC. No State requires the pay statement itself in another language. The federal English designation binds no private employer [US-FED-020]. Owner rows (tier `owner`) cannot be fact register_ids, so these decisions are cited in prose only.

---

## m01 — Foundational: the three-layer system
- **Federal core.**
  - Income tax withholding: 26 U.S.C. 3402 [US-FED-012].
  - FICA: quarterly return under 26 CFR 31.6011(a)-1 [US-FED-015].
  - FUTA: 6% gross under 3301 [US-FED-013], credited by State UI contributions up to 90% and reduced for States with outstanding Title XII advances [US-FED-014].
  - The tax year is the calendar year (W-2 calendar-year basis) [US-FED-006].
  - The FLSA is a floor. The more protective State or municipal standard of the place whose law applies prevails, under 29 U.S.C. 218(a) [US-MULTIS5-008, key `multi.wage_hour.overlay_rule`].
- **State layer.**
  - 50 States + DC. Each has its own withholding regime (or none), its own UI programme, and in some States SDI/PFML.
  - No wage income tax: AK, FL, NV, NH, SD, TN, TX, WA, WY.
  - Facts emitted: TX [US-TXS5-001], WA [US-WAS5-017], NV [US-NV-001], SD [US-SD-001], TN [US-TN-001], NH [US-NHP9W-003].
  - **WA** has an enacted 9.9% tax on individuals with AGI over USD 1M from 2028-01-01. It operates at assessment and is not modelled for 2026.
  - AK, FL and WY: no schema-valid row (see Open questions).
- **Local layer.** City, county and school-district income taxes exist in PA, OH, MI, IN, MD, KY, NY (NYC/Yonkers) and OR (transit). See m06 §local and the coverage row `local_regimes`.
- **Live federal change.** The Mobile Workforce bills S. 1443 and H.R. 10271 are drafts, not enacted; do not model them [US-MULTIS5-020, US-MULTIS5-025].
- **Oracle.**
  - Pub. 15-T 2026 has only two worked examples (NRA → 31; tribal → 584.09). Stage 9b re-derives from Worksheet 1A and the Annual Percentage Method tables [US-FED-027].
  - The IRS Tax Withholding Estimator is **not** an oracle [US-FED-021].
  - The state oracles are listed in m12.

## m02 — Master data
- **W-4 (2026):**
  - Steps 1(c), 2, 3 and 4(a)–(c).
  - The exempt checkbox lapses: a new W-4 is needed in 2027.
  - A pre-2020 allowance is worth 4,300 [US-FEDS5-006, US-FEDS5-001; annex_FED keys].
  - NRA W-4 per Notice 1392 [US-FEDS5-015].
- **State certificates replace or supplement the W-4.** Two defaults as examples:
  - no CT-W4 → flat 6.99% [US-CTS5-011];
  - no DE 4 → Single, 0 allowances, because the federal W-4 is FIT-only [US-CAS5-004].
  - The other States are in the annexes.
- **Routing keys** (build-manifest `_sub_national_key`):
  - `work_location_jurisdiction`: the place of physical performance, with the exceptions in m06 [US-MULTIS5-023];
  - `residence_jurisdiction`;
  - `sui_state`: the localization test in order — localized → base of operations → direction or control → residence [US-MULTIS5-017; UIPL 20-04 US-MULTIS5-016].
- **New hire.** Report to the State of work within 20 days (shorter in many States). Minimum fields: name, address, SSN, first day; employer name, address, FEIN [US-FEDS5-024]. A multistate employer may designate one State [US-MULTIS5-006].
- **SSN.** It may be truncated (XXX-XX-1234) only on employee W-2 copies [US-FEDS5-022]. Pay-statement SSN rules are state law (e.g. MD forbids SSN on any pay document; NE allows the last 4 digits; see annexes).
- **Records.** FLSA records are kept 3 years [US-FEDS5-021]; IRS employment-tax records 4 years (annex_FED `fed.records.irs.retention_years`).

## m03 — Gross to net
- **Order of operations:**
  1. gross;
  2. pre-tax deductions (federal exclusions; state conformity differs);
  3. FICA (6.2% to 184,500; 1.45%; +0.9% above 200,000 per employer);
  4. FIT (Pub. 15-T Worksheet 1A; line 1g 12,900 MFJ / 8,600 otherwise when Step 2 is not checked);
  5. state income tax;
  6. local tax;
  7. SDI/PFML employee shares;
  8. garnishments on disposable earnings.
  - Keys: annex_FED `fed.fit.worksheet1a.*`, `fed.fica.*`.
- **Order dependencies that change the result:**
  - **AL** deducts the federal tax withheld from the state base, so compute FIT first [US-ALS5-001, `al.wh.fit_before_sit`].
  - **OR** subtracts federal tax withheld, capped at 8,750 (the DOR publication also prints 8,500; use 8,750) [US-ORS5-009, `or.wh.federal_subtraction_cap`].
- **Rounding:**
  - federal rounding to the dollar is optional [US-FED-001];
  - Form 941 is in cents [US-FED-005];
  - Iowa computes to the cent in 2026 [US-IAS5-005];
  - several States round to the dollar (MO, OK, ND, MN optional — see annexes).
- **State conformity of pre-tax items** differs (PA and NJ tax 401(k) deferrals; CA taxes HSA; OH municipal base = Medicare wages less 125 deductions [US-OHS5-001, medium confidence]). The annexes carry each State.

## m04 — Compensation
- **Federal:**
  - minimum wage 7.25, not indexed [US-FEDS5-017];
  - overtime 1.5× over 40 hours in the workweek, no daily overtime [US-FEDS5-018];
  - tipped: over 30/month in tips, cash wage 2.13, maximum tip credit 5.12 [US-FEDS5-019];
  - EAP salary floor 684/week (the 2024 increase was vacated) [US-FEDS5-020].
- **The highest of the federal, state and local minimum applies.**

**State comparison table (examples; full set in the annexes)**

  | State | 2026 | Notes / row |
  |---|---|---|
  | CA | 16.90; 17.40 from 2027-01-01 | annex_CA `ca.minwage.hourly` [US-CAS5-006/-007] |
  | WA | 17.13; 17.73 from 2027 | [US-WAS5-006/-007] |
  | NY | 17.00 NYC/LI/Westchester; 16.00 rest | no 2027 step (off-ramp) [US-NYS5-001] |
  | FL | 15.00 from 2026-09-30 | Fla. Stat. 448.110 still prints 6.15 (stale) [US-FLS5-001] |
  | TX | 7.25 | [US-TXS5-002] |
  | DC | 18.40 from 2026-07-01 | 17.95 before [US-DCS5-011] |
  | OR | 15.55 from 2026-07-01 | metro 16.80 / nonurban 14.55 [US-ORS5-002] |
  | AK | 14.00 from 2026-07-01 | 15.00 from 2027-07-01, no tip credit [US-AKS5-001] |
  | NJ | 15.92 general | [US-NJS5-009] |

- **Daily overtime States** (examples):
  - CA 8h/12h and 7th day [US-CAS5-008];
  - AK over 8h [US-AKS5-001];
  - NV for employees under 18.00/h from 2026-07-01 [US-NVS5-003].
- **P.L. 119-21 qualified overtime and tips.** The deduction is at assessment. Withholding changes only through W-4 Step 4(b). The employer reports W-2 TT/TP. FICA is unchanged [US-FEDS5-030].

## m05 — Social security and payroll levies
- **FICA:**
  - OASDI 6.2% + 6.2% up to 184,500 (2026; second document family: SSA notice US-FED-003);
  - 192,300 for 2027 (SSA published; re-verification blocked, medium confidence) [US-FEDS5-005, US-FED-022];
  - Medicare 1.45% + 1.45%, no cap;
  - Additional Medicare 0.9% above 200,000 per employer, employee only.
- **FUTA:**
  - 6.0% gross, 5.4% maximum credit, 0.6% net, on 7,000 per employer per year [US-FED-007, US-MULTIS5-009];
  - 2025 credit reductions (final): CA 1.2%, USVI 4.5% [US-FEDS5-009, **partial row**];
  - 2026 potential reductions (CA 5.3%, USVI 4.8%) become final only after 2026-11-10 (Open questions).
- **SUI.** One State per employment, chosen by the localization test. Wage bases and rates are per State. Examples:
  - AK 54,200, with a 0.50% employee share [US-AKS5-003];
  - WA 78,200 [US-WAS5-012].
  - Employee UI shares exist only in AK, NJ and PA.
  - Wages reported to another State: credit in CA [US-MULTIS5-010] and in the other States keyed in annex_MULTI.
- **SDI/PFML/LTC (employee or employer shares), examples:**
  - WA PFML 1.13% (2026), 1.2% (2027) [US-WAS5-015];
  - DC PFL 0.75%, employer only, no cap [US-DCS5-020];
  - MA PFML 0.88% total (25+ covered individuals) [US-MAS5-012];
  - CA SDI 1.3%, no cap [US-CAEDD-004]; the key is owned by annex_CA (`ca.sdi.rate`). 2027 rate not published.
- **MA PFML split — decision recorded (journal trap):**
  - **The conflict.** Chapter 101 of the Acts of 2026 swaps the employee-deduction caps (s.25–26). Section 45 makes ss.25–26 "apply for taxable years beginning on or after January 1, 2026" [US-MAS5-026]. DFML implements the swap from **2027-01-01** [US-MAS5-012].
  - **What the held Act text shows.** Section 45 is the tax-year commencement clause shared with the c.62/c.63 tax provisions. c.175M contributions are set per calendar year by DFML under s.7(e). The Act, approved 2026-06-12, gives no mechanism to re-split contributions already withheld. The employee maximum share is 0.46% in both DFML years.
  - **Decision: follow DFML.**
    - 2026: family 0.18% (up to 100% from the employee) + medical 0.70% (employee up to 40%).
    - 2027: family 0.70% (employee up to 40%) + medical 0.18% (up to 100%).
    - Keys: `ma.pfml.split` (two dated fact objects) and `practice.ma.pfml_split`. Residual risk: `ma.pfml.split.effective_date` (non-blocking).
- **Household and agricultural thresholds:** FICA at 3,000 cash, FUTA at 1,000 in a quarter [US-FEDS5-029]; farmworker tests 150 / 2,500 [US-FEDR3-006].

## m06 — Tax
- **FIT 2026.**
  - Pub. 15-T percentage method; the full STANDARD and Step-2 tables are in annex_FED (`fed.fit.standard.*`, `fed.fit.step2.*`) [US-FEDS5-001].
  - Standard deduction 16,100 / 32,200 / 24,150 [US-FEDS5-010].
  - Supplemental: 22% optional; 37% mandatory above 1,000,000. Backup withholding 24% [US-FEDS5-003].
- **Nonresident alien (2b; C31 holds at federal level).**
  - Withholding add-on: Table 2 is 16,100/yr (309.60/wk); Table 1 is 11,800/yr. It is for computation only, not on the W-2, with no FICA/FUTA effect, and is not applied to flat supplemental [US-FEDS5-002].
  - Treaty-exempt wages: Form 8233 → 1042-S, filed via IRIS.
  - Commercial traveler: ≤90 days and ≤3,000 [US-FEDS5-016].
- **State income-tax patterns** (rates are examples; tables are in the annexes):
  - **Flat:** IN 2.95% (2.90% in 2027) plus county [US-INS5-009]; UT 4.45% [US-UTS5-001]; GA 4.99% statutory for TY2026 (`ga.sit.statutory_rate`; withholding-table dating in the GA annex/WTC) [US-GAS5-009]; MI 4.25% plus cities (annex MI).
  - **Graduated:** MD to 6.50% plus county to 3.30% [US-MDS5-001]; CA 1.1–14.63% (annex CA).
  - **Statute ≠ withholding instrument** (see m13): OH, WI, NE, KS, SC.
- **Resident working in another State.** The residence State's own rule applies. It may be:
  - difference withholding (CT, KS, VT);
  - none where the work State withholds (NC, CO, GA);
  - withholding on all wages (OK, OH, NY, LA);
  - a credit at assessment only.
  - The credit is never a payroll deduction. Keys: annex_MULTI `multi.resident_out_of_state.*`.
- **Reciprocity:**
  - 30 bilateral pairs, confirmed from both sides; AZ is unilateral (CA, IN, OR, VA); DC does not tax any nonresident.
  - Keys: annex_MULTI `multi.reciprocity.*` [US-MULTI-004..019].
- **Nonresident thresholds.** Examples: AL 30 days; AZ 60; LA 30 from 2026-01-01 (Act 382; rule LR 52:358); IL 30 working days; WV 30. Keys: annex_MULTI `multi.nonresident.*` [US-MULTI-021, -017, US-MULTIS5-021, -023, US-MULTI-015].
- **Convenience of the employer:** NY [US-MULTIS5-013]; PA [US-MULTIS5-014]; DE [US-MULTIS5-015]; NE; and the retaliatory rules of NJ [US-MULTI-012] and CT [US-MULTI-020].
- **Federal limits:**
  - motor carrier and rail: residence State only;
  - air: residence + the State of >50% of pay;
  - seamen: no State withholding;
  - military spouses: residence election [US-MULTIS5-001..005].
- **Local layer** (examples):
  - Philadelphia 3.735% resident / 3.425% nonresident from 2026-07-01 [US-PAS5-022];
  - IN county rates change in January and October (R47/10-26 from 2026-10-01) [US-INS5-009];
  - Detroit 2.4% / 1.2% [US-MIR3-002].

## m07 — Deductions and garnishments
All federal keys are owned by annex_FED (`fed.ccpa.*`, `fed.levy.*`, `fed.iwo.*`, `fed.retirement.*`, `fed.hsa.*`, `fed.bik.health_fsa.*`).
- **CCPA:** the lesser of 25% or the excess over 217.50/week; support 50/60% (+5 points with arrears over 12 weeks) [US-FEDS5-023].
- **IRS levy exempt amount:** 309.62/week single, plus 101.92 per dependent [US-FEDS5-014].
- **IWO:**
  - priority over other garnishments except an earlier IRS levy;
  - interstate orders follow the law of the obligor's principal place of employment, with remittance to the SDU within 7 business days [US-MULTIS5-007];
  - OMB form approved to 2029-08-31 (the current form is extended one year) [US-FEDS5-028].
- **Plan limits:** 401(k) 24,500, catch-up 8,000 / 11,250 [US-FED-023]; HSA 4,400 / 8,750 [US-FED-024]; FSA 3,400 / carryover 680 [US-FEDS5-010].
- **States stricter than the CCPA** (examples in the annexes): AZ 10%, WA 35×/75%, CO 80%/40×, NH, SD 40× minus 25/dependent.

## m08 — Leave
- **FMLA:** 12 workweeks (26 for a military caregiver), may be unpaid [US-FEDS5-026]. There is no federal paid leave for private employers.
- **State PFML.** Contributions run through payroll; benefits are paid by the State. The employee contribution and any employer voluntary payment are W-2 wages [US-FEDS5-007].
- **MA maximum weekly benefit:** 1,230.39 (2026) and 1,284.61 (2027) [US-MAS5-025].
- **State paid-sick-leave laws** (accrual, paystub display) are in the annexes. Examples: AZ shows sick leave on the paystub; MD shows the balance each pay; MO Prop A sick leave was repealed by H.B. 567/2025; VA paid sick leave for 50+ employees from 2027-07-01.

## m09 — Termination
- **Federal:** no immediate-final-pay rule [US-FEDS5-025]; WARN 60 days; severance is wages for FIT, FICA and FUTA [US-FEDS5-029]; terminated employee's W-2 by Jan 31 or earlier on request [US-FED-016].
- **State final-pay timing** varies (examples): SD next payday [US-SDS5-010]; NH 72 h; UT 24 h on discharge. Vacation payout is required in ME, MT and WY (absent a signed policy). See the annexes.

## m10 — Reporting
- **Deposits:**
  - monthly at 50,000 or less in the lookback; semiweekly above that; next day at 100,000 or more [US-FEDS5-004];
  - Form 941 is quarterly, in cents; Form 940 is annual, due Jan 31 [US-FEDS5-031, **partial**].
- **W-2 TY2026:**
  - due 2027-02-01;
  - new codes TP, TT and TA, and box 14b;
  - required at 2,000 even with no withholding [US-FEDS5-007];
  - two States and two localities per form [US-MULTIS5-011].
- **Other returns:**
  - ACA: ALE at 50, e-file at 10+ [US-FEDS5-012, **partial**];
  - 1042-S via IRIS [US-FEDS5-016];
  - Davis-Bacon weekly certified payroll [US-FEDS5-027];
  - Form 8655 agent authorization [US-FED-008].
- **State returns:**
  - UI quarterly wage report to the `sui_state` only;
  - withholding returns to every State where withholding applies;
  - state W-2 copies per State spec (see the RSPEC/SIR packs).
- **EFW2 TY2026 is gated** (SSA 403) [US-FEDS5-032].

## m11 — Advanced: special populations and benefits in kind
- **Special treatments:**
  - statutory employees: FICA yes, FIT no [US-FEDR3-005];
  - ministers: no withholding, SE tax [US-FED-030];
  - household and family employment [US-FEDS5-029];
  - farmworkers [US-FEDR3-006];
  - US citizens abroad: Form 673 [US-FEDR3-007]; FEIE 132,900 [US-FED-025];
  - students, government employees and election workers are in annex_FED.
- **Fringe exclusions 2026:**
  - parking and transit 340/month each;
  - dependent care 7,500;
  - educational assistance 5,250;
  - group-term life coverage above 50,000 is FICA wages [US-FEDS5-008];
  - Trump-account employer contribution up to 2,500 from 2026-07-04 [US-FEDS5-030];
  - ACA affordability 9.96% [US-FEDS5-011].

## m12 — Worked examples (oracle collection, C37)
Every example the Stage 5 workers reproduced is a fact in `CCG-m12_worked_examples-facts.json`, keyed `{st}.oracle.{case}.withholding`.
- **Quoted in the row** (`quoted from authority page`): CA, GA, IL, IN (13.96 + 4.73), WI, DE, HI, LA, MA, ME, MO, MS, RI, VT, AL, AR, ND (booklet 734, recorded as a **defect**). The federal examples are in annex_FED.
- **Re-derived by the worker on the method row** (`derived arithmetically`):
  - CT: tables 17.65 / 39.97 / 78.82 vs rules 17.79 / 39.86 / 79.30;
  - Detroit 47.45;
  - MN 91.27; OH 45.13; NC 4.44; ND 10; OK 37.00; OR 1,789; IA ex. 6 114.92; ID 31; KS threshold 69; SC 10.58.
- **Residuals carried as Open questions:** NY example 2 (258.50 vs printed 258.51); KY sheet typo and per-period rounding (47.98 vs 47); ND Section 2 stale example; OR publication defects; CT tables vs rules; UT Pub 14 (effective date open); DC (no 2026 method); MD (calculator not run). MI 75.36 (Guide 446) and NM FYI-104 41.80 are now facts (Synthesis C); the MI Treasury calculator was not run.

## m13 — Practices (build traps from the run journal)
Each trap is a `practice.*` fact:
- SC Act 110 is not in 2026 withholding [US-SCS5-004/-005];
- WI W-166 tables ≠ statutory brackets [US-WIS5-010/-011];
- NE Circular EN tables ≠ 4.55% [US-NES5-018];
- KS KW-100 header is stale [US-KSS5-001];
- MI tips/overtime deduction is at assessment only [US-MIS5-017];
- VA 2027 deduction not modelled [US-VAS5-018];
- DC 2026 method unpublished [US-DCS5-021];
- CT tables vs rules [US-CTS5-010];
- OH flat rate vs graduated tables [US-OHS5-007];
- OR cap 8,750 [US-ORS5-009];
- HI 2027 tables pending [US-HIS5-029];
- GA rate change [US-GAS5-009];
- MA PFML split [US-MAS5-012 + US-MAS5-026];
- AL FIT before SIT;
- the estimator is not an oracle;
- the P.L. 119-21 withholding rule.

## Coverage matrix (`CCG-coverage-facts.json`, 18 rows, all `answered`)
- The federal and multistate cut of each population, with its effects on income tax, social security and reporting, and with sources.
- `non_resident_employee` carries both meanings (US nonresident alien; nonresident of a State). Its social_security source is US-FEDS5-002 (no FICA effect of the add-on) plus the localization test US-MULTIS5-017.
- Each row names the annexes that carry the state detail.

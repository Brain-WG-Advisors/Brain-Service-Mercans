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

---

## Key index per unit (generated from the facts files)

**m01_foundational** — own facts (15): `fed.fit.legal_basis.withholding_statute` [US-FED-012], `fed.fica.return_period` [US-FED-015], `fed.futa.legal_basis.rate_statute` [US-FED-013], `fed.futa.legal_basis.state_credit` [US-FED-014], `fed.tax_year.basis` [US-FED-006], `fed.language.official` [US-FED-020], `tx.no_wage_tax` [US-TXS5-001], `wa.no_wage_tax` [US-WAS5-017], `nv.no_wage_tax` [US-NV-001], `sd.no_wage_tax` [US-SD-001], `tn.no_wage_tax` [US-TN-001], `nh.no_wage_tax` [US-NHP9W-003], `fed.oracle.source` [US-FED-027], `fed.oracle.estimator_not_oracle` [US-FED-021], `ak.no_wage_tax` [US-AKWT-002].
  Annex keys cited (2): `multi.wage_hour.overlay_rule` (CCG-annex_MULTI-facts.json (US-MULTIS5-008)), `multi.mobile_workforce_bill.senate` (CCG-annex_MULTI-facts.json (US-MULTIS5-020)).

**m02_master_data** — own facts (3): `multi.sit.work_location.rule` [US-MULTIS5-023], `ct.cert.default_no_certificate` [US-CTS5-011], `ca.cert.default_no_certificate` [US-CAS5-004].
  Annex keys cited (10): `fed.w4.input_fields` (CCG-annex_FED-facts.json (US-FEDS5-006)), `fed.w4.exempt.validity` (CCG-annex_FED-facts.json (US-FEDS5-006)), `fed.fit.nra.w4.rule` (CCG-annex_FED-facts.json (US-FEDS5-015)), `fed.fit.allowance.pre2020_value` (CCG-annex_FED-facts.json (US-FEDS5-001)), `fed.newhire.deadline_days` (CCG-annex_FED-facts.json (US-FEDS5-024)), `fed.newhire.fields` (CCG-annex_FED-facts.json (US-FEDS5-024)), `multi.newhire.designated_state` (CCG-annex_MULTI-facts.json (US-MULTIS5-006)), `fed.ssn.truncation.format` (CCG-annex_FED-facts.json (US-FEDS5-022)), `fed.records.flsa.retention_years` (CCG-annex_FED-facts.json (US-FEDS5-021)), `multi.sui.localization_test` (CCG-annex_MULTI-facts.json (US-MULTIS5-017)).

**m03_gross_to_net** — own facts (4): `fed.form941.amounts_in_cents` [US-FED-005], `al.wh.fit_before_sit` [US-ALS5-001], `or.wh.federal_subtraction_cap` [US-ORS5-009], `oh.local.municipal_base` [US-OHS5-001].
  Annex keys cited (7): `fed.fit.worksheet1a.line1g.mfj` (CCG-annex_FED-facts.json (US-FEDS5-001)), `fed.fit.worksheet1a.line1g.other` (CCG-annex_FED-facts.json (US-FEDS5-001)), `fed.fit.rounding` (CCG-annex_FED-facts.json (US-FED-001)), `ia.wh.rounding` (CCG-annex_IA-facts.json (US-IAS5-005)), `fed.fica.oasdi.rate.employee` (CCG-annex_FED-facts.json (US-FEDS5-005)), `fed.fica.medicare.rate.employee` (CCG-annex_FED-facts.json (US-FEDS5-005)), `fed.fica.addl_medicare.rate` (CCG-annex_FED-facts.json (US-FEDS5-005)).

**m04_compensation** — own facts (7): `ny.minwage.nyc_li_westchester.hourly` [US-NYS5-001], `ny.minwage.rest.hourly` [US-NYS5-001], `tx.minwage.hourly` [US-TXS5-002], `or.minwage.standard.hourly` [US-ORS5-002], `nj.minwage.general.hourly` [US-NJS5-009], `nv.overtime.daily_threshold_wage` [US-NVS5-003], `fed.plaw119_21.qualified_overtime.level` [US-FEDS5-030].
  Annex keys cited (13): `fed.minwage.hourly` (CCG-annex_FED-facts.json (US-FEDS5-017)), `fed.overtime.premium.multiplier` (CCG-annex_FED-facts.json (US-FEDS5-018)), `fed.overtime.weekly_threshold_hours` (CCG-annex_FED-facts.json (US-FEDS5-018)), `fed.tipped.monthly_tips_threshold` (CCG-annex_FED-facts.json (US-FEDS5-019)), `fed.tipped.cash_wage.hourly` (CCG-annex_FED-facts.json (US-FEDS5-019)), `fed.tipped.tip_credit.max_hourly` (CCG-annex_FED-facts.json (US-FEDS5-019)), `fed.exempt.salary_floor.weekly` (CCG-annex_FED-facts.json (US-FEDS5-020)), `ca.minwage.hourly` (CCG-annex_CA-facts.json (US-CAS5-007)), `wa.minwage.hourly` (CCG-annex_WA-facts.json (US-WAS5-007)), `fl.minwage.hourly` (CCG-annex_FL-facts.json (US-FLS5-001)), `dc.minwage.hourly` (CCG-annex_DC-facts.json (US-DCS5-011)), `ak.minwage.hourly` (CCG-annex_AK-facts.json (US-AKS5-001)), `ca.overtime.rule` (CCG-annex_CA-facts.json (US-CAS5-008)).

**m05_social_security** — own facts (6): `wa.pfml.total.rate` [US-WAS5-015], `wa.pfml.total.rate` [US-WAS5-015], `dc.pfml.employer.rate` [US-DCS5-020], `ma.pfml.total.rate` [US-MAS5-012], `ma.pfml.split` [US-MAS5-012], `ma.pfml.split` [US-MAS5-012].
  Annex keys cited (18): `fed.fica.oasdi.wage_base` (CCG-annex_FED-facts.json (US-FED-022)), `fed.fica.oasdi.rate.employer` (CCG-annex_FED-facts.json (US-FEDS5-005)), `fed.fica.medicare.rate.employer` (CCG-annex_FED-facts.json (US-FEDS5-005)), `fed.fica.addl_medicare.withholding_threshold` (CCG-annex_FED-facts.json (US-FEDS5-005)), `fed.futa.rate.gross` (CCG-annex_FED-facts.json (US-FED-007)), `fed.futa.credit.max` (CCG-annex_FED-facts.json (US-FED-007)), `fed.futa.rate.net` (CCG-annex_FED-facts.json (US-FED-007)), `fed.futa.wage_base` (CCG-annex_FED-facts.json (US-MULTIS5-009)), `fed.futa.credit_reduction.ca` (CCG-annex_FED-facts.json (US-FEDS5-009)), `fed.futa.credit_reduction.vi` (CCG-annex_FED-facts.json (US-FEDS5-009)), `multi.sui.other_state_wage_credit.ca` (CCG-annex_MULTI-facts.json (US-MULTIS5-010)), `wa.sui.wage_base` (CCG-annex_WA-facts.json (US-WAS5-012)), `ak.sui.wage_base` (CCG-annex_AK-facts.json (US-AKS5-003)), `ak.sui.employee.rate` (CCG-annex_AK-facts.json (US-AKS5-003)), `fed.household.fica_cash_threshold` (CCG-annex_FED-facts.json (US-FEDS5-029)), `fed.household.futa_quarter_threshold` (CCG-annex_FED-facts.json (US-FEDS5-029)), `fed.pfml.employee_contribution.is_w2_wages` (CCG-annex_FED-facts.json (US-FEDS5-007)), `ca.sdi.employee.rate` (CCG-annex_CA-facts.json (US-CAEDD-004)).

**m06_tax** — own facts (10): `fed.plaw119_21.tips_overtime.level` [US-FEDS5-030], `ga.sit.statutory_rate` [US-GAS5-009], `in.sit.rate` [US-INS5-009], `ut.sit.rate` [US-UTS5-001], `oh.sit.statutory` [US-OHS5-007], `oh.wh.tables.effective_from` [US-OHS5-001], `md.sit.top_rate` [US-MDS5-001], `pa.local.philadelphia.resident.rate` [US-PAS5-022], `pa.local.philadelphia.nonresident.rate` [US-PAS5-022], `in.county.change_dates` [US-INS5-009].
  Annex keys cited (42): `fed.fit.std_deduction.single` (CCG-annex_FED-facts.json (US-FEDS5-010)), `fed.fit.std_deduction.mfj` (CCG-annex_FED-facts.json (US-FEDS5-010)), `fed.fit.std_deduction.hoh` (CCG-annex_FED-facts.json (US-FEDS5-010)), `fed.fit.supplemental.flat_rate` (CCG-annex_FED-facts.json (US-FEDS5-003)), `fed.fit.supplemental.mandatory_rate` (CCG-annex_FED-facts.json (US-FEDS5-003)), `fed.fit.supplemental.mandatory_threshold` (CCG-annex_FED-facts.json (US-FEDS5-003)), `fed.fit.backup_withholding.rate` (CCG-annex_FED-facts.json (US-FEDS5-003)), `fed.fit.nra.addon.table2.annual` (CCG-annex_FED-facts.json (US-FEDS5-002)), `fed.fit.nra.addon.table2.weekly` (CCG-annex_FED-facts.json (US-FEDS5-002)), `fed.fit.nra.addon.table1.annual` (CCG-annex_FED-facts.json (US-FEDS5-002)), `fed.fit.nra.commercial_traveler.max_days` (CCG-annex_FED-facts.json (US-FEDS5-016)), `fed.fit.nra.commercial_traveler.max_pay` (CCG-annex_FED-facts.json (US-FEDS5-016)), `fed.fit.nra.treaty_exempt.reporting` (CCG-annex_FED-facts.json (US-FEDS5-016)), `multi.reciprocity.pa.partners` (CCG-annex_MULTI-facts.json (US-MULTI-007)), `multi.reciprocity.va.partners` (CCG-annex_MULTI-facts.json (US-MULTI-004)), `multi.reciprocity.oh.partners` (CCG-annex_MULTI-facts.json (US-MULTI-005)), `multi.reciprocity.wi.partners` (CCG-annex_MULTI-facts.json (US-MULTI-006)), `multi.reciprocity.md.partners` (CCG-annex_MULTI-facts.json (US-MULTI-008)), `multi.reciprocity.ky.partners` (CCG-annex_MULTI-facts.json (US-MULTI-009)), `multi.reciprocity.mi.partners` (CCG-annex_MULTI-facts.json (US-MULTI-010)), `multi.reciprocity.nj.partners` (CCG-annex_MULTI-facts.json (US-MULTI-011)), `multi.reciprocity.mn.partners` (CCG-annex_MULTI-facts.json (US-MULTI-013)), `multi.reciprocity.nd.partners` (CCG-annex_MULTI-facts.json (US-MULTI-014)), `multi.reciprocity.wv.partners` (CCG-annex_MULTI-facts.json (US-MULTI-015)), `multi.reciprocity.ia.partners` (CCG-annex_MULTI-facts.json (US-MULTI-018)), `multi.reciprocity.de.partners` (CCG-annex_MULTI-facts.json (US-MULTI-019)), `multi.reciprocity.az.unilateral` (CCG-annex_MULTI-facts.json (US-MULTI-017)), `multi.nonresident.az.threshold_days` (CCG-annex_MULTI-facts.json (US-MULTI-017)), `multi.nonresident.al.threshold_days` (CCG-annex_MULTI-facts.json (US-MULTI-021)), `multi.nonresident.la.threshold_days` (CCG-annex_MULTI-facts.json (US-MULTIS5-021)), `multi.nonresident.il.threshold_days` (CCG-annex_MULTI-facts.json (US-MULTIS5-023)), `multi.nonresident.wv.threshold_days` (CCG-annex_MULTI-facts.json (US-MULTI-015)), `multi.convenience.ny.rule` (CCG-annex_MULTI-facts.json (US-MULTIS5-013)), `multi.convenience.pa.rule` (CCG-annex_MULTI-facts.json (US-MULTIS5-014)), `multi.convenience.de.rule` (CCG-annex_MULTI-facts.json (US-MULTIS5-015)), `multi.convenience.nj.rule` (CCG-annex_MULTI-facts.json (US-MULTI-012)), `multi.convenience.ct.rule` (CCG-annex_MULTI-facts.json (US-MULTI-020)), `multi.transport.motor_carrier` (CCG-annex_MULTI-facts.json (US-MULTIS5-001)), `multi.transport.rail` (CCG-annex_MULTI-facts.json (US-MULTIS5-002)), `multi.transport.air_carrier` (CCG-annex_MULTI-facts.json (US-MULTIS5-003)), `multi.transport.seamen` (CCG-annex_MULTI-facts.json (US-MULTIS5-004)), `multi.military_spouse.rule` (CCG-annex_MULTI-facts.json (US-MULTIS5-005)).

**m07_deductions** — own facts (0): none.
  Annex keys cited (15): `fed.ccpa.max_rate` (CCG-annex_FED-facts.json (US-FEDS5-023)), `fed.ccpa.protected_weekly` (CCG-annex_FED-facts.json (US-FEDS5-023)), `fed.ccpa.support.max_rate.with_dependents` (CCG-annex_FED-facts.json (US-FEDS5-023)), `fed.ccpa.support.max_rate.without_dependents` (CCG-annex_FED-facts.json (US-FEDS5-023)), `fed.levy.exempt.single_0dep.weekly` (CCG-annex_FED-facts.json (US-FEDS5-014)), `fed.levy.exempt.per_dependent.weekly` (CCG-annex_FED-facts.json (US-FEDS5-014)), `multi.iwo.governing_law` (CCG-annex_MULTI-facts.json (US-MULTIS5-007)), `fed.iwo.omb_expiry` (CCG-annex_FED-facts.json (US-FEDS5-028)), `fed.retirement.401k.elective_deferral_limit` (CCG-annex_FED-facts.json (US-FED-023)), `fed.retirement.401k.catch_up_50` (CCG-annex_FED-facts.json (US-FED-023)), `fed.retirement.401k.catch_up_60_63` (CCG-annex_FED-facts.json (US-FED-023)), `fed.hsa.limit.self_only` (CCG-annex_FED-facts.json (US-FED-024)), `fed.hsa.limit.family` (CCG-annex_FED-facts.json (US-FED-024)), `fed.bik.health_fsa.salary_reduction_cap` (CCG-annex_FED-facts.json (US-FEDS5-010)), `fed.bik.health_fsa.carryover_max` (CCG-annex_FED-facts.json (US-FEDS5-010)).

**m08_leave** — own facts (2): `ma.pfml.max_weekly_benefit` [US-MAS5-025], `ma.pfml.max_weekly_benefit` [US-MAS5-025].
  Annex keys cited (4): `fed.fmla.weeks` (CCG-annex_FED-facts.json (US-FEDS5-026)), `fed.fmla.military_caregiver.weeks` (CCG-annex_FED-facts.json (US-FEDS5-026)), `fed.paid_leave.private_employers.exists` (CCG-annex_FED-facts.json (US-FEDS5-026)), `fed.pfml.employee_contribution.is_w2_wages` (CCG-annex_FED-facts.json (US-FEDS5-007)).

**m09_termination** — own facts (1): `fed.w2.terminated_employee.furnishing` [US-FED-016].
  Annex keys cited (4): `fed.final_pay.rule` (CCG-annex_FED-facts.json (US-FEDS5-025)), `fed.warn.notice_days` (CCG-annex_FED-facts.json (US-FEDS5-025)), `fed.severance.is_wages` (CCG-annex_FED-facts.json (US-FEDS5-029)), `sd.final_pay.rule` (CCG-annex_SD-facts.json (US-SDS5-010)).

**m10_reporting** — own facts (1): `fed.form1042s.channel` [US-FEDS5-016].
  Annex keys cited (12): `fed.deposit.monthly_max_lookback_liability` (CCG-annex_FED-facts.json (US-FEDS5-004)), `fed.deposit.next_day_threshold` (CCG-annex_FED-facts.json (US-FEDS5-004)), `fed.form941.frequency` (CCG-annex_FED-facts.json (US-FED-015)), `fed.form940.due` (CCG-annex_FED-facts.json (US-FEDS5-031)), `fed.w2.due_date` (CCG-annex_FED-facts.json (US-FEDS5-007)), `fed.w2.no_withholding_threshold` (CCG-annex_FED-facts.json (US-FEDS5-007)), `fed.w2.box12.new_codes` (CCG-annex_FED-facts.json (US-FEDS5-007)), `multi.w2.states_per_form` (CCG-annex_MULTI-facts.json (US-MULTIS5-011)), `fed.aca.ale.fte_threshold` (CCG-annex_FED-facts.json (US-FEDS5-012)), `fed.aca.efile_threshold` (CCG-annex_FED-facts.json (US-FEDS5-012)), `fed.davis_bacon.certified_payroll.frequency` (CCG-annex_FED-facts.json (US-FEDS5-027)), `fed.reporting_agent.authorization` (CCG-annex_FED-facts.json (US-FED-008)).

**m11_advanced** — own facts (1): `fed.citizen_abroad.form673` [US-FEDR3-007].
  Annex keys cited (12): `fed.statutory_employee.treatment` (CCG-annex_FED-facts.json (US-FEDR3-005)), `fed.minister.withholding` (CCG-annex_FED-facts.json (US-FED-030)), `fed.agricultural.per_worker_threshold` (CCG-annex_FED-facts.json (US-FEDR3-006)), `fed.agricultural.total_threshold` (CCG-annex_FED-facts.json (US-FEDR3-006)), `fed.feie.amount` (CCG-annex_FED-facts.json (US-FED-025)), `fed.bik.parking.monthly_exclusion` (CCG-annex_FED-facts.json (US-FEDS5-008)), `fed.bik.transit.monthly_exclusion` (CCG-annex_FED-facts.json (US-FEDS5-008)), `fed.bik.dependent_care.exclusion` (CCG-annex_FED-facts.json (US-FEDS5-008)), `fed.bik.educational_assistance.exclusion` (CCG-annex_FED-facts.json (US-FEDS5-008)), `fed.bik.group_term_life.excluded_coverage` (CCG-annex_FED-facts.json (US-FEDS5-008)), `fed.bik.trump_account.employer_contribution_max` (CCG-annex_FED-facts.json (US-FEDS5-030)), `fed.aca.affordability.rate` (CCG-annex_FED-facts.json (US-FEDS5-011)).

**m12_worked_examples** — own facts (37): `ca.oracle.de44_f.monthly.withholding` [US-CAS5-001], `ga.oracle.mfj_semimonthly.withholding` [US-GAS5-001], `il.oracle.weekly_800.withholding` [US-ILR3-001], `in.oracle.weekly_800.state.withholding` [US-INS5-007], `in.oracle.weekly_800.county.withholding` [US-INS5-007], `wi.oracle.weekly_350_s1.withholding` [US-WIS5-011], `wi.oracle.biweekly_1000_m3.withholding` [US-WIS5-011], `de.oracle.weekly_25000.withholding` [US-DES5-006], `de.oracle.supplemental.withholding` [US-DES5-006], `hi.oracle.weekly_500_s3.withholding` [US-HIS5-004], `la.oracle.weekly_700.withholding` [US-LAS5-001], `la.oracle.biweekly_4600.withholding` [US-LAS5-001], `ma.oracle.weekly_155_0ex.withholding` [US-MAS5-024], `me.oracle.example3.weekly.withholding` [US-MES5-011], `mo.oracle.annual_married.withholding` [US-MOS5-001], `ms.oracle.weekly_460_0ex.withholding` [US-MSS5-003], `ri.oracle.weekly_2195.withholding` [US-RIS5-019], `vt.oracle.weekly_1800_m2.withholding` [US-VTS5-016], `al.oracle.weekly_850_m2.withholding` [US-ALS5-001], `ar.oracle.monthly_2127_2ex.withholding` [US-ARS5-001], `nd.oracle.section2_booklet.withholding` [US-NDS5-001], `ct.oracle.ex8_f_weekly700.withholding` [US-CTS5-010], `ct.oracle.ex9_a_weekly1000.withholding` [US-CTS5-010], `ct.oracle.ex10_b_biweekly2300.withholding` [US-CTS5-010], `mi.oracle.detroit.resident_biweekly_2000.withholding` [US-MIR3-002], `mn.oracle.biweekly_2000_s1.withholding` [US-MNS5-010], `oh.oracle.biweekly_2000_1ex.withholding` [US-OHS5-001], `nc.oracle.weekly_450_s2.withholding` [US-NC-001], `nd.oracle.section1_weekly_1800_s2.withholding` [US-NDS5-001], `nm.oracle.weekly_1000_married.withholding` [US-NMP52-001], `mi.oracle.biweekly_2000_1ex.withholding` [US-MIPIT-001], `ok.oracle.semimonthly_1825_m2.withholding` [US-OK-001], `or.oracle.annual_25000.withholding` [US-ORS5-009], `ia.oracle.example6_monthly_5000_hoh.withholding` [US-IAS5-005], `id.oracle.biweekly_1212_single.withholding` [US-IDS5-008], `sc.oracle.weekly_750_3al.withholding` [US-SCS5-004], `ks.oracle.weekly_threshold_single.withholding` [US-KSS5-001].
  Annex keys cited (2): `fed.oracle.pub15t.nra_example.withholding` (CCG-annex_FED-facts.json (US-FED-027)), `fed.oracle.pub15t.tribal_example.withholding` (CCG-annex_FED-facts.json (US-FED-027)).

**m13_practices** — own facts (16): `practice.sc.withholding_rates_2026` [US-SCS5-004], `practice.wi.use_w166_tables` [US-WIS5-010], `practice.ne.use_circular_en_tables` [US-NES5-018], `practice.ks.kw100_header_stale` [US-KSS5-001], `practice.mi.tips_ot_deduction_level` [US-MIS5-017], `practice.va.std_deduction_2027_not_modelled` [US-VAS5-018], `practice.dc.2026_method_unpublished` [US-DCS5-021], `practice.ct.tables_vs_rules` [US-CTS5-010], `practice.oh.flat_rate_vs_tables` [US-OHS5-007], `practice.or.federal_cap` [US-ORS5-009], `practice.hi.2027_tables_pending` [US-HIS5-029], `practice.ga.rate_change_2026` [US-GAS5-009], `practice.ma.pfml_split` [US-MAS5-012], `practice.al.fit_before_sit` [US-ALS5-001], `practice.fed.estimator_not_oracle` [US-FED-021], `practice.fed.pl119_21_withholding` [US-FEDS5-030].

**coverage** — own facts (0): none.
  coverage_matrix rows: resident_employee, non_resident_employee, fixed_term_contract, part_time, officers_without_employment_contract, apprentices_and_trainees, maternity_paternity_parental, work_accident_occupational_disease, termination_and_final_pay, mid_month_joiner_and_leaver, annual_regularisation, overtime, multiple_employers, local_regimes, employer_type_and_size, mid_year_rate_change, special_pay_cycles, accrual_vs_payment.

## Synthesis D additions (2026-11-02)

Source: browser-pass rows S5B-P1 / S5B-P2 merged into `legal-basis-register.csv` and SSA EFW2 TY2026 (US-FEDS5-032) read locally. Every claim below carries its register_id; the facts file is authoritative. Full log: `_research/synthesis-D/SYNTHESIS-D.md`.

**CCG-m10_reporting-facts.json** (unit `m10_reporting`)

Facts added:
- `fed.efw2.ty2026_changes` = **TY2026 changes: RE adds Employer Signature PIN (319-328); RW adds Box 14b Primary/Secondary Treasury Tipped Occupation Code (490-492 / 493-495); RO/RU split Codes A and B into separate money fields (combined A+B field valid through TY2025 only), add money fields for existing Codes J, K, L, P and new Codes TA, TP, TT; SS wage base 184,500; FIRE replaced by IRIS** (2026-01-01 → open) [A.2, US-FEDS5-032, direct artifact inspection, conf high] — LEVEL: employer reporting. Detail in CCG-annex_FED and RSPEC (rspec.fed.efw2.*).
- `fed.efw2.record_length` = **512** bytes (2026-01-01 → open) [A.2, US-FEDS5-032, direct artifact inspection, conf high]

Open questions closed: `fed.efw2.layout`.

Still open, new attempts recorded in `unresolved[].attempted`: `multi.newhire.registration_channel`.

**CCG-m12_worked_examples-facts.json** (unit `m12_worked_examples`)

Still open, new attempts recorded in `unresolved[].attempted`: `dc.oracle.method_2026`.

## Open questions (mirrors `unresolved[]`; same keys, same wording)

- **`fl.no_wage_tax`** (m01_foundational; blocking=false). Why: No FL register row with a schema-valid id states the absence of a wage income tax (FL findings carry it in prose). What would close it: Annex FL fact citing Fla. Const. art. VII s.5 if a row exists, or a new register row in the merge.
- **`wy.no_wage_tax`** (m01_foundational; blocking=false). Why: No WY register row with a schema-valid id states the absence of a wage income tax. What would close it: Annex WY fact or a register row for the WY DOR statement.
- **`fed.futa.credit_reduction.potential_2026`** (m05_social_security; blocking=false). Why: Potential 2026 credit reductions CA 5.3% (1.5 + BCR 3.8) and USVI 4.8% become final only if advances remain unpaid on 2026-11-10 (US-FEDS5-009 partial). What would close it: DOL OUI FUTA credit-reduction page/xlsx after 2026-11-10, or the 2026 Schedule A (Form 940) instructions.
- **`multi.sui.other_state_wage_credit.remaining_states`** (m05_social_security; blocking=false). Why: SUI wage-base credit for wages reported to another State: annex_MULTI now carries multi.sui.other_state_wage_credit.* for 28 States plus CA; the remaining States (incl. AZ, CO, GA, IL, IN, LA, MA, MD, MN, MO, NJ, NM, NY, OH, PA, TN, TX, UT, VA, WA, WI, DC) are not yet keyed at MULTI level. What would close it: Each remaining State taxable-wage definition (annex rows) or DOL Significant Provisions July 2026.
- **`multi.pfml.coverage_test.remaining_states`** (m05_social_security; blocking=false). Why: PFML/SDI coverage of multistate workers: annex_MULTI keys CT, DC, DE, MD, ME, OR, RI, WA and a default (localization); CA, NJ, NY, MA, CO, MN, VT not keyed at MULTI level (MULTI-OQ-3). What would close it: Each programme coverage definition (annex units).
- **`fed.indexation.publication_2027`** (m06_tax; blocking=false). Why: TY2027 Rev. Proc., 401(k)/IRA notice and 2027 Pub. 15-T not published as of 2026-11-02 (IR-2026-117..129 checked). What would close it: IRS releases expected Nov-Dec 2026.
- **`fed.eo13706.sick_leave.accrual`** (m08_leave; blocking=false). Why: EO 13706 federal-contractor paid sick leave accrual figures were not transcribed (FED OQ 6). What would close it: 29 CFR 13.5 read from eCFR (one fetch).
- **`multi.sick_leave.coverage_threshold`** (m08_leave; blocking=false). Why: Paid-sick-leave coverage of employees working partly in a State is per State and not researched at MULTI level (MULTI-OQ-4). What would close it: Per-state statutes in the annexes.
- **`fed.form940.instructions_current`** (m10_reporting; blocking=false). Why: TY2026 Instructions for Forms 940 and 1094-C/1095-C not yet issued; 2025 editions read. What would close it: IRS releases of the TY2026 instructions (usually Dec-Jan).
- **`multi.newhire.registration_channel`** (m10_reporting; blocking=false). Why: HHS/OCSS multistate employer registration page returned 202 empty (MULTI-OQ-6); statute 42 U.S.C. 653a(b)(1)(B) carries the rule. What would close it: Browser read of the ACF multistate registration page.
- **`fed.iwo.revised_form.state_golive`** (m10_reporting; blocking=false). Why: States go live with the revised (gig-field) IWO/e-IWO within the one-year extension; dates not known (FED OQ 8). What would close it: OCSE Action Transmittal implementing ICR 202607-0970-002.
- **`fed.bik.business_mileage.rate`** (m11_advanced; blocking=false). Why: The 2026 business standard mileage rate is not printed in Pub. 15-B (FED OQ 7). What would close it: IRS 2026 standard mileage notice.
- **`ny.oracle.nys50t.example2.withholding`** (m12_worked_examples; blocking=false). Why: NYS-50-T-NYS Method II examples 1, 3, 4 reproduce (8.01, 3,576.63, 44.10); example 2 prints 12.43/258.51 while half-up arithmetic gives 12.42/258.50. Booklet scan US-NYP52-001 states no rounding rule. What would close it: DTF statement of the rounding convention or the DTF calculator result for the same case.
- **`ky.oracle.biweekly_1500.withholding`** (m12_worked_examples; blocking=false). Why: KY 2026 formula sheet: 1,247.40/26 = 47.98 but sheet shows 47 (no stated rule) and prints 35,730 for 35,640 (row US-KY-002). What would close it: DOR KY confirmation of the per-period rounding.
- **`ut.oracle.pub14.examples.withholding`** (m12_worked_examples; blocking=false). Why: Pub 14 (04/26) six examples reproduce (weekly S 400 -> 12; biweekly S 2,600 -> 116; semimonthly M 1,200 -> 18; monthly M 7,800 -> 347; quarterly S 9,000 -> 367; daily M 175 -> 5) (row US-UTPIT-003); Pub 14 effective date (2026-06-01?) open (UT-OQ-1), so the examples are not emitted as dated facts. What would close it: Utah State Tax Commission statement of the Pub 14 Rev. 04/26 effective date.
- **`dc.oracle.method_2026`** (m12_worked_examples; blocking=false). Why: DC has no published 2026 withholding method: D.C. Act 26-416 (emergency, effective 2026-08-13, max 90 days) revoked personal exemptions; D-4 under review (US-DCS5-021). What would close it: OTR 2026 withholding instructions/tables (otr.cfo.dc.gov, 403 to curl) or the permanent FY2027 BSA act.
- **`md.oracle.calculator`** (m12_worked_examples; blocking=false). Why: MD oracle is the Comptroller withholding calculator and Central Payroll net pay calculator; neither was run. What would close it: One run of the Comptroller calculator for a fixed case in the browser pass.
- **`ma.pfml.split.effective_date`** (m13_practices; blocking=false). Why: Ch. 101/2026 s.45 says ss.25-26 apply for taxable years beginning on or after 2026-01-01; DFML implements the swap from 2027-01-01. Decision taken: follow DFML (rows US-MAS5-026, US-MAS5-012). What would close it: A DFML/DOR notice or 458 CMR 2.00 amendment on the transition (MA Q14).
- **`practice.dol_paid_leave_list`** (m13_practices; blocking=false). Why: DOL WB featured-paid-leave page (19 P9 rows reverted to B/MANUAL) returns 404; the DOL prevailing-wage list still says MI has no law (MI restored 2023). What would close it: Saved copy of the DOL WB paid-leave page; never use the DOL lists for MI.
- **`fed.common_paymaster.rule`** (coverage; blocking=false). Why: Common-paymaster relief for related employers (multiple_employers row) was not researched in the FED unit. What would close it: IRC 3121(s) / Pub. 15-A common paymaster section read into a FED row.
- **`multi.workers_comp.employee_share`** (coverage; blocking=false). Why: Only NM fee and WA employee deduction are known; other States allowing employee workers-comp deductions not swept. What would close it: Annex workers confirm per State (WA L&I rates; NM TRD-41431).

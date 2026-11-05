# CCG annex_AL research pack — Alabama

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B, 2026-11-02. Source: `_research/stage5/AL.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_AL-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** No state minimum wage, overtime, pay-statement, final-pay or sick-leave statute (federal FLSA applies; local mandates pre-empted by Ala. Code 25-7-41). State income tax withheld on the booklet formula with federal FIT as a deduction (FIT must be computed before AL SIT); A4 certificate; municipal occupational taxes (T4, no state census). SUI wage base 8,000, new employer 2.70%, no employee UI, no SDI/PFML. Stage-5 confidence: state 85-95%, local 55%.

## 1 — Employment / labour code
No state minimum wage, overtime, pay-frequency, payment-method or paycard statute; FLSA (7.25, 1.5x over 40) applies (FED unit) [US-ALP52-001, US-ALL-001 — legacy ids, narrative only]. Confidence 85% (negative rests on the agency statement).

- `al.minwage.state.exists` = **False**  (2016-02-25 → open) [A.1, US-ALS5-010, quoted from authority page, conf medium] — Agency states AL has no state wage-hour laws; federal 7.25 applies (FED unit). 25-7-41(b)-(c) voids local wage/leave mandates (public employees excepted, 25-7-43).
- `al.local_wage_leave_mandates.preempted` = **True**  (2016-02-25 → open) [A.1, US-ALS5-010, quoted from authority page, conf high]
- `al.equal_pay.wage_history_refusal_protected` = **True**  (2026-01-01 → open) [A.1, US-ALS5-015, quoted from authority page, conf high] — Clarke-Figures Equal Pay Act, 25-1-30 (sex and race).

## 2 — Income tax (state withholding)
- `al.wh.method` = **annualise; subtract standard deduction (phase-out by GI), annualised federal FIT withheld, personal exemption, dependents; apply 2/4/5% brackets; divide by pay periods**  (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Booklet rev. 01/2026 p. 6; Ala. Code 40-18-71/-74 [US-ALS5-011]. Order FIT before AL SIT.
- `al.wh.federal_fit_deductible` = **True**  (2026-01-01 → open) [A.1, US-ALS5-011, quoted from authority page, conf high] — 40-18-71(a).
- `al.pit.bracket.single.1.ceiling` = **500** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — 0/S/H/MS: 2% first 500, 4% next 2,500, 5% above 3,000.
- `al.pit.bracket.single.2.ceiling` = **3000** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ALS5-001: Formula: annualise gross; deduct (A) standard deduction - 0/S: 3,000 if GI<=25,999, minus 25 per 500 above 25,999, 2,500 if GI>=35,500; MS: 4,250 / minus 88 per 250 above 12,999 / 2,500 at 17,750; M: 8,500 / minus 175 per 500 / 5,000 at 35,500; H: 5,200 / minus 135 per 500 / 2,500 at 35,500; (B) ann
- `al.pit.bracket.married.1.ceiling` = **1000** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — M: 2% first 1,000, 4% next 5,000, 5% above 6,000.
- `al.pit.bracket.married.2.ceiling` = **6000** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ALS5-001: Formula: annualise gross; deduct (A) standard deduction - 0/S: 3,000 if GI<=25,999, minus 25 per 500 above 25,999, 2,500 if GI>=35,500; MS: 4,250 / minus 88 per 250 above 12,999 / 2,500 at 17,750; M: 8,500 / minus 175 per 500 / 5,000 at 35,500; H: 5,200 / minus 135 per 500 / 2,500 at 35,500; (B) ann
- `al.pit.bracket.1.rate` = **2** percent (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ALS5-001: Formula: annualise gross; deduct (A) standard deduction - 0/S: 3,000 if GI<=25,999, minus 25 per 500 above 25,999, 2,500 if GI>=35,500; MS: 4,250 / minus 88 per 250 above 12,999 / 2,500 at 17,750; M: 8,500 / minus 175 per 500 / 5,000 at 35,500; H: 5,200 / minus 135 per 500 / 2,500 at 35,500; (B) ann
- `al.pit.bracket.2.rate` = **4** percent (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ALS5-001: Formula: annualise gross; deduct (A) standard deduction - 0/S: 3,000 if GI<=25,999, minus 25 per 500 above 25,999, 2,500 if GI>=35,500; MS: 4,250 / minus 88 per 250 above 12,999 / 2,500 at 17,750; M: 8,500 / minus 175 per 500 / 5,000 at 35,500; H: 5,200 / minus 135 per 500 / 2,500 at 35,500; (B) ann
- `al.pit.bracket.3.rate` = **5** percent (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ALS5-001: Formula: annualise gross; deduct (A) standard deduction - 0/S: 3,000 if GI<=25,999, minus 25 per 500 above 25,999, 2,500 if GI>=35,500; MS: 4,250 / minus 88 per 250 above 12,999 / 2,500 at 17,750; M: 8,500 / minus 175 per 500 / 5,000 at 35,500; H: 5,200 / minus 135 per 500 / 2,500 at 35,500; (B) ann
- `al.wh.std_deduction.single.max` = **3000** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — 0/S: 3,000 if GI <= 25,999; less 25 per 500 above; floor 2,500 from 35,500.
- `al.wh.std_deduction.single.min` = **2500** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ALS5-001: Formula: annualise gross; deduct (A) standard deduction - 0/S: 3,000 if GI<=25,999, minus 25 per 500 above 25,999, 2,500 if GI>=35,500; MS: 4,250 / minus 88 per 250 above 12,999 / 2,500 at 17,750; M: 8,500 / minus 175 per 500 / 5,000 at 35,500; H: 5,200 / minus 135 per 500 / 2,500 at 35,500; (B) ann
- `al.wh.std_deduction.married.max` = **8500** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — M: 8,500; less 175 per 500 above 25,999; floor 5,000 from 35,500.
- `al.wh.std_deduction.married.min` = **5000** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ALS5-001: Formula: annualise gross; deduct (A) standard deduction - 0/S: 3,000 if GI<=25,999, minus 25 per 500 above 25,999, 2,500 if GI>=35,500; MS: 4,250 / minus 88 per 250 above 12,999 / 2,500 at 17,750; M: 8,500 / minus 175 per 500 / 5,000 at 35,500; H: 5,200 / minus 135 per 500 / 2,500 at 35,500; (B) ann
- `al.wh.std_deduction.married_separate.max` = **4250** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — MS: 4,250; less 88 per 250 above 12,999; floor 2,500 from 17,750.
- `al.wh.std_deduction.head_of_family.max` = **5200** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — H: 5,200; less 135 per 500; floor 2,500 from 35,500.
- `al.wh.personal_exemption.single` = **1500** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — 0 status: 0; S/MS 1,500; M/H 3,000.
- `al.wh.personal_exemption.married` = **3000** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ALS5-001: Formula: annualise gross; deduct (A) standard deduction - 0/S: 3,000 if GI<=25,999, minus 25 per 500 above 25,999, 2,500 if GI>=35,500; MS: 4,250 / minus 88 per 250 above 12,999 / 2,500 at 17,750; M: 8,500 / minus 175 per 500 / 5,000 at 35,500; H: 5,200 / minus 135 per 500 / 2,500 at 35,500; (B) ann
- `al.wh.dependent.gi_to_50000` = **1000** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Per dependent: 1,000 if GI <= 50,000; 500 if <= 100,000; 300 above.
- `al.wh.dependent.gi_to_100000` = **500** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ALS5-001: Formula: annualise gross; deduct (A) standard deduction - 0/S: 3,000 if GI<=25,999, minus 25 per 500 above 25,999, 2,500 if GI>=35,500; MS: 4,250 / minus 88 per 250 above 12,999 / 2,500 at 17,750; M: 8,500 / minus 175 per 500 / 5,000 at 35,500; H: 5,200 / minus 135 per 500 / 2,500 at 35,500; (B) ann
- `al.wh.dependent.gi_above_100000` = **300** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ALS5-001: Formula: annualise gross; deduct (A) standard deduction - 0/S: 3,000 if GI<=25,999, minus 25 per 500 above 25,999, 2,500 if GI>=35,500; MS: 4,250 / minus 88 per 250 above 12,999 / 2,500 at 17,750; M: 8,500 / minus 175 per 500 / 5,000 at 35,500; H: 5,200 / minus 135 per 500 / 2,500 at 35,500; (B) ann
- `al.wh.supplemental.rate` = **5** percent (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — May be withheld at 5%.
- `al.wh.certificate.form` = **A4 REV. 4/2025 (federal W-4 not accepted; no A4 = zero exemptions; A4-MS military spouse)**  (2025-04-01 → open) [A.2, US-ALS5-005, direct artifact inspection, conf high] — ADOR page text still says "Revised March 2014" but the PDF prints REV. 4/2025 [US-ALS5-002] (never-do 6).
- `al.wh.certificate.inflated_penalty` = **500** USD (2025-04-01 → open) [A.2, US-ALS5-005, direct artifact inspection, conf high]
- `al.wh.severance.exempt_max` = **50000** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Severance/downsizing pay exempt up to 50,000 with prior ADOR approval.
- `al.pit.overtime_premium_deduction.max` = **1000** USD (2026-01-01 → 2028-12-31) [A.2, US-ALS5-004, quoted from authority page, conf high] — Act 2026-604, operating level ASSESSMENT only: no change to wages, withholding or tax; W-2 box 12 code TT informational; total OT stays in box 16. Prior withholding-level exemption (Acts 2023-421/2024-437) shown as previous by ADOR.

## 2b — Non-resident regime and reciprocity
- `al.nonres.safe_harbor.days` = **30** days (2026-01-01 → open) [A.2, US-ALS5-003, quoted from authority page, conf high] — Act 2025-334, operating level WITHHOLDING: nonresidents with <=30 AL days working in more than one state whose home state has a similar exclusion or no PIT (list as of 2026-10-01: AK, FL, GA, IL, IN, LA, MT, NV, NH, SD, TN, TX, WA, WV, WY). At 31+ days all AL income of the year taxable. Athletes/entertainers/public figures excluded.
- `al.reciprocity.exists` = **False**  (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Booklet lists no agreement. Residents withheld wherever they work except when the employer withholds for the work state; nonresidents only on AL-earned wages.

## 2c — Local wage taxes
- `al.local.occupational_tax.exists` = **True**  (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Municipal/county occupational taxes withheld by the employer, remitted to the city/county; ADOR does not administer them. No state census (AL-OQ-2).
- `al.local.leeds.rate` = **1** percent (2026-01-01 → open) [A.2, US-ALS5-017, quoted from authority page, conf high] — City of Leeds: 1% of gross earnings, monthly return to Avenu, annual reconciliation, show on pay stub, records 5 years. Birmingham 1% rests only on a tier-C MANUAL lead (see the AL pack) - not a fact.

## 3 — Social insurance (SUI / SDI / PFML / levies)
UC wages include tips and bonuses; room and board at employee option valued (full board 63.00/week; meals 42.00/week or 2.00/meal; lodging 21.00/week or 3.00/day) per handbook rev. 2021 [US-ALR3-001] — admin rule not read, so not emitted as facts. Employer levies: only the 0.06% ESA [US-ALP7-002].

- `al.sui.wage_base` = **8000** USD (2026-01-01 → open) [A.1, US-ALS5-009, quoted from authority page, conf high] — 25-4-16(b)(1), fixed in statute; other-state UC wages count toward it.
- `al.sui.new_employer.rate` = **2.7** percent (2026-01-01 → open) [A.2, US-ALS5-007, quoted from authority page, conf high]
- `al.sui.employer.rate.min` = **0.2** percent (2026-01-01 → open) [A.2, US-ALS5-007, quoted from authority page, conf high] — Range 0.20%-6.80% incl. 0.06% ESA across schedules A-D plus shared cost; 2026 schedule letter/shared cost not located (AL-OQ-1).
- `al.sui.employer.rate.max` = **6.8** percent (2026-01-01 → open) [A.2, US-ALS5-007, quoted from authority page, conf high]
- `al.sui.esa.rate` = **0.06** percent (2026-01-01 → open) [A.2, US-ALS5-007, quoted from authority page, conf high] — Employment Security Enhancement Assessment inside the UC rate; no FUTA credit for it (handbook p. 19, US-ALR3-001).
- `al.sui.employee.rate` = **0** percent (2026-01-01 → open) [A.2, US-ALR3-001, quoted from authority page, conf high] — No UC tax withheld from employees.
- `al.sui.wages.cafeteria_cash_option_included` = **True**  (2026-01-01 → open) [A.2, US-ALS5-007, quoted from authority page, conf high] — Cafeteria plan reductions with a cash option are UC wages (departs from income tax).
- `al.sdi_pfml.exists` = **False**  (2026-01-01 → open) [A.2, US-ALS5-007, quoted from authority page, conf high]

## 4 — Payslip statute
- `al.payslip.state_statute.exists` = **False**  (2026-01-01 → open) [A.2, US-ALS5-007, quoted from authority page, conf medium] — Agency: no state wage-hour laws [US-ALP52-001, legacy id]; 29 CFR 516 applies. Leeds asks occupational tax to be shown on the pay stub [US-ALS5-017].

## 5 — Statutory reporting instruments
ADOR registration and filings through My Alabama Taxes. Penalties: late return greater of 10% or 50; late payment 10%; 50 per late W-2/1099 [US-ALS5-001]. New-hire file specs from newhire@workforce.alabama.gov. Municipal occupational tax returns per city (Leeds/Avenu, Birmingham/HdL) [US-ALS5-017, US-ALS5-018].

- `al.report.wh.monthly.a6.threshold` = **1000** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — A-6 monthly if more than 1,000 withheld in month 1 or 2 of the quarter; due 15th of next month; e-file/EFT mandatory for single payment >= 750.
- `al.report.wh.eft_mandatory_payment` = **750** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf medium] — Derivation recorded in register row US-ALS5-001: Formula: annualise gross; deduct (A) standard deduction - 0/S: 3,000 if GI<=25,999, minus 25 per 500 above 25,999, 2,500 if GI>=35,500; MS: 4,250 / minus 88 per 250 above 12,999 / 2,500 at 17,750; M: 8,500 / minus 175 per 500 / 5,000 at 35,500; H: 5,200 / minus 135 per 500 / 2,500 at 35,500; (B) ann
- `al.report.wh.quarterly.form` = **A-1 due last day of month after quarter; file when nil**  (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ALS5-001: Formula: annualise gross; deduct (A) standard deduction - 0/S: 3,000 if GI<=25,999, minus 25 per 500 above 25,999, 2,500 if GI>=35,500; MS: 4,250 / minus 88 per 250 above 12,999 / 2,500 at 17,750; M: 8,500 / minus 175 per 500 / 5,000 at 35,500; H: 5,200 / minus 135 per 500 / 2,500 at 35,500; (B) ann
- `al.report.annual.a3` = **A-3 + W-2s due 31 January; EFW2 RS record only, 512 bytes; e-file mandatory for 10+ statements (Form 10, 8/24); RS cols 298-307 carry federal FIT withheld**  (2026-01-01 → open) [A.2, US-ALS5-006, direct artifact inspection, conf high]
- `al.report.w2.efile_threshold` = **10** statements (2026-01-01 → open) [A.2, US-ALS5-006, direct artifact inspection, conf high]
- `al.report.w2.furnish_threshold` = **1500** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — W-2 to every employee paid 1,500+ AL wages or with AL tax withheld.
- `al.report.sui.quarterly` = **Quarterly Contribution and Wage Report via eGov only (online_form or file_upload); due last day of month after quarter; corrections UC-10C**  (2026-01-01 → open) [A.2, US-ALS5-007, quoted from authority page, conf high]
- `al.newhire.report_days` = **7** days (2026-01-01 → open) [A.2, US-ALS5-008, quoted from authority page, conf high] — From hire or recall; electronic twice a month 12-16 days apart; electronic mandatory for 5+ employees.

## 6 — Leave
- `al.leave.sick.state_statute.exists` = **False**  (2026-01-01 → open) [A.1, US-ALS5-010, quoted from authority page, conf high] — Local sick-leave mandates barred (25-7-41).
- `al.leave.jury.full_time_usual_compensation` = **True**  (2026-01-01 → open) [A.1, US-ALS5-012, quoted from authority page, conf high] — 12-16-8(c), 12-16-8.1: full-time employee entitled to usual compensation; cannot be forced to use leave.
- `al.leave.voting.hours` = **1** hours (2026-01-01 → open) [A.1, US-ALS5-012, quoted from authority page, conf high] — 17-1-5; silent on pay.

## 7 — Termination and final pay
No final-pay or vacation-payout statute (confidence 80%); no state WARN found.

- `al.ui.separation_info.return_working_days` = **6** working days (2026-01-01 → open) [A.2, US-ALR3-001, quoted from authority page, conf high] — BEN-241 on a claim. No state final-pay statute (federal + policy).

## 8 — Benefits in kind / taxable wages
AL wages follow federal unless AL law conflicts; excluded IRC 125, 219, 401(k), 403(b), 408(k), 408(p), 457 [US-ALS5-001]. Transit 132(f) and group-term life 79 not listed (AL-OQ-3). Agricultural cash wages not withheld.

- `al.hsa.conforms` = **True**  (2026-01-01 → open) [A.1, US-ALS5-020, quoted from authority page, conf high]

## 9 — Deductions and garnishments
- `al.garn.exempt.percent` = **75** percent (2026-01-01 → open) [A.1, US-ALS5-013, quoted from authority page, conf high] — 6-10-7: 75% of resident wages exempt; apply with CCPA disposable-earnings limit, more protective governs. Garnishee pays in after 30 days, then monthly.
- `al.garn.child_support.remit_business_days` = **7** business days (2026-01-01 → open) [A.1, US-ALS5-013, quoted from authority page, conf high] — 30-3-61/-67/-70: IWO priority over garnishments; current before arrears.
- `al.garn.termination_report_days` = **15** days (2026-01-01 → open) [A.1, US-ALS5-013, quoted from authority page, conf high]

## 10 — Collective agreements / prevailing wage
No state prevailing-wage law; Davis-Bacon only (FED). 25-7-42 bars local labour-peace/PLA mandates.


## 11 — Indexation
Nothing indexed: SUI base fixed in statute; withholding amounts statutory; no state minimum wage. Only the annual UC schedule A-D/shared cost (25-4-54), published per employer on UC-216.


## 12 — Payroll data protection / records
Data Breach Notification Act 2018 ch. 8-38 [US-ALS5-016, partial: definitions only]; no SSN truncation statute located.


## 13 — Live legal change
- `al.live.act_2025_334.status` = **in force 2026-01-01; operating level withholding + filing**  (2026-01-01 → open) [A.2, US-ALS5-003, quoted from authority page, conf high]
- `al.live.act_2026_604.status` = **in force 2026-01-01 to 2028-12-31; operating level assessment (W-2 box 12 TT information)**  (2026-01-01 → 2028-12-31) [A.2, US-ALS5-004, quoted from authority page, conf high]
- `al.live.hurricane_isaias_relief` = **individual returns to 2027-02-04; withholding relief case by case (notice 2026-10-15)**  (2026-10-15 → open) [A.2, US-ALS5-019, quoted from authority page, conf high]

## Oracle — worked examples (C37)
- `al.oracle.example.1.input` = **M-2, weekly 850.00, federal withholding 35.19**  (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ALS5-001: Formula: annualise gross; deduct (A) standard deduction - 0/S: 3,000 if GI<=25,999, minus 25 per 500 above 25,999, 2,500 if GI>=35,500; MS: 4,250 / minus 88 per 250 above 12,999 / 2,500 at 17,750; M: 8,500 / minus 175 per 500 / 5,000 at 35,500; H: 5,200 / minus 135 per 500 / 2,500 at 35,500; (B) ann
- `al.oracle.example.1.withholding` = **29.59** USD (2026-01-01 → open) [A.2, US-ALS5-001, derived arithmetically, conf high] — Booklet example re-derived in Python: 850x52=44,200; deductions 5,000+1,830 (35.19x52=1,829.88 rounded by booklet)+3,000+2,000=11,830; taxable 32,370; tax 20+200+26,370x5%=1,538.50/yr; /52 = 29.59 (30 if rounded to dollar).

## Special populations (US-OWN-005)
- Domestic/household: exempt from AL withholding; UC-covered at 1,000 cash wages in a quarter [US-ALS5-001, US-ALS5-007].
- Agricultural: exempt from withholding (AL does not follow the federal rule); UC at 10+ workers in 20 weeks or 20,000/quarter [US-ALS5-001, US-ALS5-007, US-ALS5-014].
- Minors: under 16 barred except agriculture; 14-15 outside school hours; no youth wage [US-ALS5-014].
- Tipped: federal tip credit; tips are UC wages [US-ALR3-001].
- Clergy: ministers exempt from AL withholding; church employment not UC-covered [US-ALS5-001, US-ALS5-007].
- Students / NRAs / statutory employees: no AL rule beyond federal [US-ALS5-001].
- Other-state workers: 30-day safe harbor; carrier carve-outs (P.L. 91-569, 101-322, 106-489); 3-mile coastal rule [US-ALS5-003, US-ALS5-001].
- Government/nonprofit: 501(c)(3) UC at 4+ workers in 20 weeks; pre-emption does not cover public employees [US-ALS5-007, US-ALS5-010].
- Military spouses: A4-MS (MSRRA) [US-ALS5-001, US-ALS5-002].
- Downsizing severance: up to 50,000 exempt with ADOR approval [US-ALS5-001].

## Language seams (US-OWN-006)
English; a Spanish A4 exists (optional seam) [US-ALS5-005]; posters [US-ALP9L-001]. Payslip/filings en per US-OWN-006.

## QA round 3 research additions (2026-11-02, agent 2)

**RQ-506 closed — standard-deduction phase-out.** ADOR withholding booklet rev. 01/2026, p.6 Formula step 2A, checked against the p.7 Schedule of Standard Deduction Amounts [US-ALS5-001]. Keys per status (`single`, `married_separate`, `married`, `head_of_family`): `al.wh.std_deduction.<status>.phaseout.start_gi`, `.reduction_per_step`, `.step_size`, `.floor_from_gi`, and the summary `al.wh.std_deduction.phaseout_steps` (also in WTC country_specific).
- 0/S: 3,000 up to GI 25,999; less 25 for each 500 or part above 25,999; 2,500 from 35,500.
- MS: 4,250 up to 12,999; less 88 for each 250 or part above 12,999; 2,500 from 17,750.
- M: 8,500 up to 25,999; less 175 for each 500 or part above 25,999; 5,000 from 35,500.
- H: 5,200 up to 25,999; less 135 for each 500 or part above 25,999; 2,500 from 35,500.
Derivation lines: 3,000 - 25 x 19 = 2,525; 4,250 - 88 x 19 = 2,578; 8,500 - 175 x 19 = 5,175; 5,200 - 135 x 19 = 2,635 (last stepped values, each above its floor); schedule spot checks MFJ 26,000-26,499 = 8,325 and MS 13,000-13,249 = 4,162 match.


## QA r3b additions (agent 2, 2026-11-02)
- `al.wh.std_deduction.married_separate.min` = 2,500 and `al.wh.std_deduction.head_of_family.min` = 2,500 [US-ALS5-001], booklet rev. 01/2026 Formula step 2A (PDF p.8). Minimum per status: S 2,500 / MS 2,500 / M 5,000 / H 2,500. Each status has its own `*.phaseout.start_gi` key; married and HoH quotes must bind to `al.wh.std_deduction.married.phaseout.start_gi` / `.head_of_family.phaseout.start_gi`, not the single key.

## Open questions
Mirrors `unresolved[]` in the facts file (same keys).

- `al.sui.rate_schedule.current` (non-blocking) — The 2026 UC rate schedule letter (A-D) and shared-cost percentage are not on any public page; the FAQ points to the per-employer UC-216 notice in eGov. **Would close it:** Workforce Alabama 2026 tax-rate announcement (Experience Rating Section) or an employer 2026 UC-216 notice from the owner/client.
- `al.local.occupational_tax.census` (blocking) — No state list of levying localities; only Leeds is A.2, Birmingham tier C; Auburn site timed out (HTTP 000). **Would close it:** Alabama League of Municipalities occupational-tax list, then each city ordinance/tax page (Birmingham Title 3 Ch. 2, Auburn, Bessemer, Gadsden, Opelika, Fairfield, Macon County). Parallel fan-out per locality.
- `al.pit.wages.transit_group_term_life` (non-blocking) — IRC 132(f) transit and IRC 79 group-term life are not on the booklet exclusion list; AL treatment unconfirmed. **Would close it:** ADOR Admin. Code 810-3-71 or an ADOR fringe-benefit FAQ.
- `al.garn.iwo.employer_fee` (non-blocking) — The AL employer processing fee under a child-support IWO was not located in the sections read. **Would close it:** Ala. Code 30-3-60..71 in full via ALISON GraphQL, or the DHR Child Support employer page.
- `al.nonres.safe_harbor.day_counting_guidance` (non-blocking) — A 2026 ADOR rule/FAQ on day-counting under Act 2025-334 is suggested only by a tier-B lead (Bradley, 2026-09). **Would close it:** ADOR Rules page / Alabama Administrative Monthly 2026 (810-3-71 amendments).
- `al.live.overtime_withholding_exemption.end_date` (non-blocking) — End date 2025-06-30 of the Acts 2023-421/2024-437 withholding-level overtime exemption rests on tier-B leads only. **Would close it:** ADOR page "Overtime Pay Exemption Amended Pursuant to Act 2024-437" linked from US-ALS5-004.

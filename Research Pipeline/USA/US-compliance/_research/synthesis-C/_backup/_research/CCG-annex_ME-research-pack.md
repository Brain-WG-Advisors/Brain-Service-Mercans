# CCG annex_ME research pack — Maine

Synthesis B, 2026-11-02. Source: `_research/stage5/ME.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_ME-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** Minimum wage 15.10 (2026) / 15.70 (2027), CPI-W indexed; Portland 16.75 / 17.75 / 19.00; tip credit max 50%; salaried-exempt threshold 3,000 x MW. Withholding per 2026 booklet: 5,300 per W-4ME allowance; withholding standard deduction 12,450 / 27,750 with phase-out (NOT the return-level 15,300 / 30,600); 5.80 / 6.75 / 7.15%; round to dollar; supplemental 5%; nonresident 12 days AND 3,000 threshold; no reciprocity, no local tax. UI base 12,000, new 2.54% (2.23 + CSSF 0.14 + UPAF 0.17); PFML 1.0% (15+) / 0.5% (<15). Pay statement REQUIRED (26 MRSA 665(1), corrects earlier rows). New hire within 7 days. Oracle: booklet examples 0 / 33 / 257.

## 1 — Employment / labour code
- `me.minwage.hourly` = **15.1** USD (2026-01-01 → 2026-12-31) [A.2, US-MES5-002, quoted from authority page, conf high] — Agricultural and non-agricultural; CPI-W Northeast Aug-Aug rounded to 0.05 each Jan 1 [US-MES5-001]; step 15.10 -> 15.70 not reproduced (CPI not fetched).
- `me.minwage.hourly` = **15.7** USD (2027-01-01 → open) [A.2, US-MES5-003, quoted from authority page, conf high] — 2027 poster (rev. 9/26).
- `me.minwage.tip_credit.max_percent` = **50** percent (2026-01-01 → open) [A.1, US-MES5-001, direct artifact inspection, conf high] — Cash wage >= 7.55 in 2026 (derived); notice items A-F; weekly shortfall test; card tips by next payday without fee.
- `me.minwage.tipped.cash_wage` = **7.55** USD (2026-01-01 → 2026-12-31) [A.1, US-MES5-001, derived arithmetically, conf high] — 15.10 x 0.5.
- `me.local_minwage.portland.hourly` = **16.75** USD (2026-01-01 → 2026-12-31) [A.1, US-MES5-012, direct artifact inspection, conf high] — Hours within city limits; City employees from 2026-07-01; tip credit max half city rate; emergency work 1.5x; CPI-U Northeast from 2029. State does not pre-empt local MW (paid leave is pre-empted).
- `me.local_minwage.portland.hourly` = **17.75** USD (2027-01-01 → 2027-12-31) [A.1, US-MES5-012, direct artifact inspection, conf high]
- `me.local_minwage.portland.hourly` = **19.0** USD (2028-01-01 → open) [A.1, US-MES5-012, direct artifact inspection, conf high]
- `me.overtime.weekly_threshold_hours` = **40** hours (2026-01-01 → open) [A.1, US-MES5-001, direct artifact inspection, conf high] — 1.5x; no daily OT; regular rate includes bonuses/commissions; exemptions auto sales/service, mariners, most public employees, listed ag/fish processing [US-MES5-005].
- `me.exempt.salary.weekly_min` = **871.16** USD (2026-01-01 → 2026-12-31) [A.2, US-MES5-002, quoted from authority page, conf high] — Annualised pay must exceed 3,000 x State MW (or FLSA level): 3,000 x 15.10 / 52 = 871.1538 -> poster 871.16 (first cent above). 2027 poster 905.79 vs formula 905.77 (Q2): safe rule salary must EXCEED 3,000 x MW.
- `me.pay_frequency.rule` = **intervals not exceeding 16 days; each payment covers wages to within 8 days of payday; closed-day payday moves to next business day; lengthening interval needs 30 days written notice; rate decrease needs prior notice**  (2026-01-01 → open) [A.1, US-MES5-004, direct artifact inspection, conf high]
- `me.direct_deposit.fee_prohibited` = **True**  (2026-01-01 → open) [A.1, US-MES5-004, direct artifact inspection, conf high] — 621-A(7); no consent/paycard rule in text read.

## 2 — Income tax (state withholding)
- `me.wh.bracket.single.1.ceiling` = 27400 (2026-01-01 → 2026-12-31) [A.2, US-ME-P5-2-001 — legacy id, NOT a fact] Single 5.80% below 27,400; 1,589 + 6.75% to 64,850; 4,117 + 7.15% above. Same booklet file as US-MES5-011; use 12,450/27,750 withholding standard deduction from US-MES5-011, NOT the 15,300/30,600 in this row.
- `me.wh.bracket.single.2.ceiling` = 64850 (2026-01-01 → 2026-12-31) [A.2, US-ME-P5-2-001 — legacy id, NOT a fact]
- `me.wh.method` = **annualise (52/26/24/12/260); - 5,300 per W-4ME allowance; - withholding standard deduction; apply schedule; divide by periods; round to nearest dollar**  (2026-01-01 → 2026-12-31) [A.2, US-MES5-011, direct artifact inspection, conf high] — 2026 booklet (rev. Dec 2025). Do not reduce for federal W-4 Step 4(b) deductions.
- `me.wh.allowance.annual` = **5300** USD (2026-01-01 → 2026-12-31) [A.2, US-MES5-011, direct artifact inspection, conf high]
- `me.wh.std_deduction.single` = **12450** USD (2026-01-01 → 2026-12-31) [A.2, US-MES5-011, direct artifact inspection, conf high] — If wages <= 102,250; else 12,450 x (177,250 - W) / 75,000; zero from 177,250. NOT the return-level 15,300 (US-ME-P5-2-001 S5A note).
- `me.wh.std_deduction.married` = **27750** USD (2026-01-01 → 2026-12-31) [A.2, US-MES5-011, direct artifact inspection, conf high] — If wages <= 204,550; else 27,750 x (354,550 - W) / 150,000; zero from 354,550.
- `me.wh.std_deduction.single.phaseout_start` = **102250** USD (2026-01-01 → 2026-12-31) [A.2, US-MES5-011, direct artifact inspection, conf high]
- `me.wh.std_deduction.single.phaseout_end` = **177250** USD (2026-01-01 → 2026-12-31) [A.2, US-MES5-011, direct artifact inspection, conf high]
- `me.wh.bracket.married.1.ceiling` = **54850** USD (2026-01-01 → 2026-12-31) [A.2, US-MES5-011, direct artifact inspection, conf high] — 5.80% below 54,850; 3,181 + 6.75% to 129,750; 8,237 + 7.15% above.
- `me.wh.bracket.married.2.ceiling` = **129750** USD (2026-01-01 → 2026-12-31) [A.2, US-MES5-011, direct artifact inspection, conf high]
- `me.wh.bracket.1.rate` = **5.8** percent (2026-01-01 → 2026-12-31) [A.2, US-MES5-011, direct artifact inspection, conf high]
- `me.wh.bracket.2.rate` = **6.75** percent (2026-01-01 → 2026-12-31) [A.2, US-MES5-011, direct artifact inspection, conf high]
- `me.wh.bracket.3.rate` = **7.15** percent (2026-01-01 → 2026-12-31) [A.2, US-MES5-011, direct artifact inspection, conf high]
- `me.wh.supplemental.rate` = **5** percent (2026-01-01 → open) [A.2, US-MES5-011, direct artifact inspection, conf high] — Aggregated or flat 5% when paid separately; backup withholding 5%.
- `me.wh.certificate` = **W-4ME required; none valid = single, zero allowances; more allowances need MRS Allowance Variance Certificate; copy to MRS when IRS demands W-4 or non-Maine-address exempt claimant expects >= 5,000 Maine-source pay**  (2026-01-01 → open) [A.2, US-MES5-011, direct artifact inspection, conf high]

## 2b — Non-resident regime and reciprocity
- `me.nonres.threshold` = **taxable only if present in Maine more than 12 days AND more than 3,000 Maine-source pay in the year (training, inspection, R&D, project-team days excluded)**  (2026-01-01 → open) [A.2, US-MES5-011, direct artifact inspection, conf medium] — Rule on legacy US-ME-P5-2-003; resident credit [US-ME-P5-2-004]; no reciprocity in force [US-ME-P5-2-005].

## 2c — Local wage taxes
- `me.local_wage_tax.exists` = **False**  (2026-01-01 → open) [A.1, US-MER3-001, quoted from authority page, conf high] — [US-MER3-002].

## 3 — Social insurance (SUI / SDI / PFML / levies)
No SDI/TDI, transit or other levy [US-MEP9V-001, US-OWN-007]. PFML rate rests on A.3 FAQ + A.1 ceiling (no A.2 table) - G-NUMBER residual flagged at seal attempt 6.

- `me.sui.new_employer.rate.total` = 2.54 (2026-01-01 → 2026-12-31) [A.2, US-ME-P5-1-001 — legacy id, NOT a fact] 2.23% UI + 0.14% CSSF + 0.17% UPAF (UPAF conflict vs UC-1 0.16%, Q1).
- `me.sui.employer.rate.combined.range` = 0.31% - 6.60% (categories 01-20; adjusted UI 0.00%-6.29%) (2026-01-01 → 2026-12-31) [A.2, US-ME-P5-1-001 — legacy id, NOT a fact]
- `me.sui.wage_base` = **12000** USD (2026-01-01 → open) [A.1, US-MES5-020, direct artifact inspection, conf high] — Fixed, not indexed; other-state wages by same legal entity and predecessor wages count (26 MRSA 1043(19)); non-cash remuneration at cash value.
- `me.pfml.rate.total.15_plus` = **1.0** percent (2025-01-01 → 2027-12-31) [A.3, US-MEP6-001, direct artifact inspection, conf medium] — FAQ (A.3) + statute ceiling 1.0% [US-MES5-024]: 15+ employees employer remits 1.0%, employee max 0.5%; < 15: 0.5% remitted, all deductible. From 2028 department sets by Oct 1. Cap SSA base; employee share deducted AFTER tax; employer-paid employee share is taxable wages; W-2 box 14 "MEPFML"; late 1% of quarterly payroll; coverage follows UI localization.
- `me.pfml.rate.total.under_15` = **0.5** percent (2025-01-01 → 2027-12-31) [A.3, US-MEP6-001, direct artifact inspection, conf medium]
- `me.pfml.employee.max_rate` = **0.5** percent (2025-01-01 → 2027-12-31) [A.3, US-MEP6-001, direct artifact inspection, conf medium]
- `me.pfml.employee_deduction.after_tax` = **True**  (2025-01-01 → open) [A.3, US-MES5-025, direct artifact inspection, conf medium]
- `me.pfml.w2_box14_label` = **MEPFML**  (2025-01-01 → open) [A.3, US-MES5-025, direct artifact inspection, conf medium]

## 4 — Payslip statute
- `me.payslip.required` = **True**  (2026-01-01 → open) [A.1, US-MES5-006, direct artifact inspection, conf high] — 26 MRSA 665(1): with each payment: pay-period date, hours, total earnings, itemized deductions; same record at time of electronic transfer; electronic only with ready access and free printing. CORRECTS US-ME-P5-1-004 / US-ME-P5-2-006 (superseded).
- `me.payslip.items` = **date of the pay period, hours, total earnings, itemized deductions**  (2026-01-01 → open) [A.1, US-MES5-006, direct artifact inspection, conf high]

## 5 — Statutory reporting instruments
- `me.report.wh.semiweekly_threshold` = 18000 (2026-01-01 → open) [A.2, US-ME-P5-2-002 — legacy id, NOT a fact] Look-back 12 months to prior 30 June; semiweekly Wed-Fri -> Wednesday, Sat-Tue -> Friday; electronic payment if combined Maine tax >= 10,000.
- `me.report.wh.941me` = **quarterly, due last day of month after quarter; electronic mandatory (Rule 104) even if nothing to report; deposits semiweekly if look-back >= 18,000 else quarterly; 900ME voucher; no W-3ME after TY2023**  (2026-01-01 → open) [A.2, US-MES5-011, direct artifact inspection, conf high]
- `me.report.w2` = **electronic with MRS by 31 January, paper not accepted; Maine Tax Portal Bulk File Upload Specifications (EFW2 acceptance open); 50 per missing statement**  (2026-01-01 → open) [A.2, US-MES5-011, direct artifact inspection, conf high]
- `me.report.sui.uc1` = **ME UC-1 quarterly, last day of month after quarter, via ReEmployME (file spec published) or paper, filed with MRS; monthly employment (12th), gross/excess/taxable wages, UC rate, CSSF, UPAF; interest 10% from 2026-01-01**  (2026-01-01 → open) [A.2, US-MES5-021, quoted from authority page, conf high]
- `me.newhire.report_days` = **7** days (2026-01-01 → open) [A.1, US-MES5-016, direct artifact inspection, conf high] — To DHHS within 7 days of first services (stricter than federal 20); rehires after 60+ days; DOB; employer UI/UBI number; independent contractors expected >= 2,500 also within 7 days.
- `me.newhire.contractor_threshold` = **2500** USD (2026-01-01 → open) [A.1, US-MES5-016, direct artifact inspection, conf high]

## 6 — Leave
PFML benefits from 2026-05-01 (FAQ lead), paid by the State fund; retro deduction of missed employee premiums during leave; health coverage continues [US-MES5-025]. Earned paid leave payout at separation depends on policy (Q8).

- `me.leave.earned_paid.employer_threshold` = **10** employees (2026-01-01 → open) [A.1, US-MES5-008, direct artifact inspection, conf high] — 26 MRSA 637: MORE than 10 employees for > 120 days; 1 h per 40 h up to 40 h/yr, any purpose; use after 120 days; carryover (PL 2025 c.438 does not reduce next year accrual); base rate; seasonal excluded; local ordinances pre-empted.
- `me.leave.earned_paid.accrual.hours_worked_per_hour` = **40** hours (2026-01-01 → open) [A.1, US-MES5-008, direct artifact inspection, conf high]
- `me.leave.earned_paid.cap_hours` = **40** hours (2026-01-01 → open) [A.1, US-MES5-008, direct artifact inspection, conf high]

## 7 — Termination and final pay
Separating employees receive the Employment Security Law notice (poster copy) [US-MES5-021]. Deductions from final pay: overcompensation and signed loans/advances [US-MES5-007].

- `me.final_pay.rule` = **no later than next established payday (discharge or resignation); on demand earlier of next payday or 2 weeks; accrued vacation from 2023-01-01 payable (not employers with <= 10 employees or public; CBA overrides); liquidated damages 2x**  (2026-01-01 → open) [A.1, US-MES5-007, direct artifact inspection, conf high]
- `me.severance.mass_layoff` = **establishments with 100+ employees: one week pay per year of service, within one pay period after last day; 90 days notice**  (2026-01-01 → open) [A.1, US-MES5-010, direct artifact inspection, conf high]

## 8 — Benefits in kind / taxable wages
- `me.pit.conformity_date` = **2025-12-31 (fixed); no additions for HSA, 125, transit, 401(k) (36 MRSA 5122) - federal exclusions followed**  (2026-01-01 → open) [A.1, US-MES5-018, direct artifact inspection, conf high] — [US-MES5-027].

## 9 — Deductions and garnishments
- `me.garn.creditor.rule` = **least of 25% of disposable, excess over 40 x higher of federal/State MW, or the total**  (2026-01-01 → open) [A.1, US-MES5-013, direct artifact inspection, conf high]
- `me.garn.creditor.weekly_protected` = **604.0** USD (2026-01-01 → 2026-12-31) [A.1, US-MES5-013, derived arithmetically, conf high] — 40 x 15.10.
- `me.garn.employer_fee_per_check` = **1** USD (2026-01-01 → open) [A.1, US-MES5-014, direct artifact inspection, conf high] — Answer within 20 days; no discharge.
- `me.garn.child_support.remit_business_days` = **7** business days (2026-01-01 → open) [A.1, US-MES5-015, direct artifact inspection, conf high] — Order adds 2/week; priority over non-support; processing fee only by DHHS rule.

## 10 — Collective agreements / prevailing wage
- `me.prevailing_wage.threshold` = **50000** USD (2026-01-01 → open) [A.1, US-MES5-017, direct artifact inspection, conf high] — State-funded public works >= 50,000 (< 10,000 never construction); energy projects >= 2 MW; certified payroll filed monthly; records 3 years; fine >= 250/employee/day.

## 11 — Indexation
MW CPI-W Northeast; Portland fixed steps then CPI-U; exempt threshold 3,000 x MW; PIT chained CPI ~Sept 15; UI base fixed; UPAF yearly; PFML cap SSA base; garnishment floor follows MW.


## 12 — Payroll data protection / records
- `me.records.retention_years` = **3** years (2026-01-01 → open) [A.1, US-MES5-006, direct artifact inspection, conf high] — 665(1); 622 date/amount and daily time records except salaried exempt [US-MES5-026]. SSN not requestable on applications [US-MES5-009].

## Oracle — worked examples (C37)
- `me.oracle.booklet.examples_weekly` = **0 / 33 / 257**  (2026-01-01 → 2026-12-31) [A.2, US-MES5-011, derived arithmetically, conf high] — Booklet Examples 1-3 reproduced in Python (weekly, rounded to dollar). No official calculator [US-ME-P5-2-009].

## Special populations (US-OWN-005)
- Domestic: UI at 1,000/quarter; no MW exclusion found [US-MES5-020, US-MES5-005].
- Agricultural: poster applies 15.10 to agriculture while 663(3)(A) excludes ag from the subchapter (Q13).
- Minors: hours limits (774); full MW; newspaper delivery under 18 and child for parent UI-excluded [US-MES5-028, US-MES5-020].
- Tipped: cash >= 50% (7.55); Portland half of 16.75 [US-MES5-001, US-MES5-012].
- Clergy: UI-excluded; no withholding rule beyond federal [US-MES5-020].
- Students: co-op/OJT, student nurses/interns UI-excluded; camp counselors MW-subchapter excluded [US-MES5-020, US-MES5-005].
- NRAs: 12-day / 3,000 nonresident threshold applies.
- Government: most public employees OT-exempt; public employers exempt from vacation payout; PFML exemption under 2023 CBAs until expiry [US-MES5-005, US-MES5-007, US-MES5-024].
- Family members dependent on employer: excluded from MW subchapter and 621-A; own child/spouse UI-excluded [US-MES5-005, US-MES5-020].
- Small employers: <= 10 no earned paid leave or vacation payout; < 15 PFML 0.5% [US-MES5-008, US-MES5-007, US-MES5-024].

## Language seams (US-OWN-006)
No language requirement; bilingual permitted [US-MEL-001, US-MEP9L-001]. Maine DOES require a pay statement (content, not language) - see US-OWN-006 dated note. Payslip English.

## Open questions
Mirrors `unresolved[]` in the facts file (same keys).

- `me.wh.bracket.single.1.ceiling` (non-blocking) — Value 27400 (from 2026-01-01) is carried by register row US-ME-P5-2-001 (active, A.2, Maine Revenue Services), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. Single 5.80% below 27,400; 1,589 + 6.75% to 64,850; 4,117 + 7.15% above. Same booklet file as US-MES5-011; use 12,450/27,750 withholding standard deduction from US-MES5-011, NOT the 15,300/30,600 in this row. **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-ME-P5-2-001) or re-key US-ME-P5-2-001; then emit this key as a fact. No new research needed.
- `me.wh.bracket.single.2.ceiling` (non-blocking) — Value 64850 (from 2026-01-01) is carried by register row US-ME-P5-2-001 (active, A.2, Maine Revenue Services), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-ME-P5-2-001) or re-key US-ME-P5-2-001; then emit this key as a fact. No new research needed.
- `me.report.wh.semiweekly_threshold` (non-blocking) — Value 18000 (from 2026-01-01) is carried by register row US-ME-P5-2-002 (active, A.2, Maine Revenue Services), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. Look-back 12 months to prior 30 June; semiweekly Wed-Fri -> Wednesday, Sat-Tue -> Friday; electronic payment if combined Maine tax >= 10,000. **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-ME-P5-2-002) or re-key US-ME-P5-2-002; then emit this key as a fact. No new research needed.
- `me.sui.new_employer.rate.total` (non-blocking) — Value 2.54 (from 2026-01-01) is carried by register row US-ME-P5-1-001 (active, A.2, Maine Department of Labor, Bureau of Unemployment Compensation), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. 2.23% UI + 0.14% CSSF + 0.17% UPAF (UPAF conflict vs UC-1 0.16%, Q1). **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-ME-P5-1-001) or re-key US-ME-P5-1-001; then emit this key as a fact. No new research needed.
- `me.sui.employer.rate.combined.range` (non-blocking) — Value 0.31% - 6.60% (categories 01-20; adjusted UI 0.00%-6.29%) (from 2026-01-01) is carried by register row US-ME-P5-1-001 (active, A.2, Maine Department of Labor, Bureau of Unemployment Compensation), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-ME-P5-1-001) or re-key US-ME-P5-1-001; then emit this key as a fact. No new research needed.
- `me.sui.upaf.rate.conflict` (blocking) — Rate-year 2026 array says UPAF 0.17%; 2026 UC-1 instructions say 0.16%. **Would close it:** An employer 2026 MDOL rate notice or MDOL BUC confirmation of the 2026 UPAF predetermined yield.
- `me.exempt.salary.next_year` (non-blocking) — 2027 poster 905.79 vs statute formula 905.77. **Would close it:** MDOL overtime guidance page; safe rule: salary must exceed 3,000 x MW.
- `me.minwage.derivation` (non-blocking) — CPI-W Northeast Aug 2025/Aug 2026 not fetched; 15.10 -> 15.70 not reproduced. **Would close it:** BLS series CWUR0100SA0 values.
- `me.local_minwage.other` (non-blocking) — Other municipal minimum wages (e.g. Rockland) not checked. **Would close it:** Municipal ordinance check or MDOL minimum-wage FAQ.
- `me.payment.paycard_consent` (non-blocking) — No paycard/direct-deposit consent rule beyond no-fee. **Would close it:** MDOL rule or Bureau of Consumer Credit Protection guidance.
- `me.pfml.rate.a2_source` (non-blocking) — 1.0%/0.5% split rests on A.3 FAQ plus A.1 ceiling; no A.2 rate table. **Would close it:** 12-702 CMR ch. 1 contributions section or an MDOL 2026 rate notice.
- `me.report.w2.bulk_spec` (non-blocking) — Maine Tax Portal Bulk File Upload Specifications not fetched (EFW2 acceptance open). **Would close it:** MRS bulk file specifications.
- `me.leave.earned_paid.payout` (non-blocking) — Payout of earned paid leave at separation is an interpretation via 626. **Would close it:** MDOL rule 12-170 CMR ch. 18 or FAQ.
- `me.pit.obbba_decoupling` (non-blocking) — Decoupling from federal tips/overtime deductions for 2026 not checked (assessment). **Would close it:** 2026 MRS individual instructions or the conformity act.
- `me.deductions.authorisation` (non-blocking) — 26 MRSA 629/635 not read. **Would close it:** Statute read.
- `me.data_protection.breach_ssn` (non-blocking) — SSN on pay statements and breach law not read. **Would close it:** 10 MRSA 1346-1350-B and 1272-B.
- `me.wh.tables.next_year` (non-blocking) — 2027 withholding tables not published. **Would close it:** MRS 27_wh_tab_instr.pdf (December 2026).
- `me.minwage.agricultural_basis` (non-blocking) — Poster applies 15.10 to agriculture while 663(3)(A) excludes ag workers from the subchapter. **Would close it:** 26 MRSA 664 as amended or the MDOL basis for the agricultural rate.

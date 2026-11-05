# CCG annex_CO research pack — Colorado

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B, 2026-11-02. Source: `_research/stage5/CO.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_CO-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** State minimum wage 15.16 (2026), Denver 19.29; overtime after 40/week or 12/day. Flat 4.40% withholding (DR 1098 method; DR 0004 optional; OBBBA overtime deduction not allowed for CO withholding). Occupational Privilege Taxes in Denver, Greenwood Village, Glendale (Sheridan tier C). UI chargeable wage limit 30,600 (2026) / 32,100 (2027), new employer 3.05% total; FAMLI 0.88% (2026, split 0.44/0.44) and 0.86% (2027). Wage Act pay statement + COMPS Rule 7 items. Several base figures (DR 1098 method, UI wage limit, FAMLI 2026) sit on legacy-id rows and are listed as non-fact lines pending re-key.

## 1 — Employment / labour code
2027 state 15.71 / tipped 12.69 and Denver 19.84, and 2026 Edgewater 18.17 / Boulder 16.82 are tier-B leads only [US-COS5-011 MANUAL]: not facts (CO-OQ-3).

- `co.minwage.hourly` = **15.16** USD (2026-01-01 → 2026-12-31) [A.2, US-COS5-001, quoted from authority page, conf high] — COMPS Rule 3; highest applicable (local) minimum applies. 2027 15.71 is tier-B only (US-COS5-011 MANUAL), not a fact.
- `co.minwage.tip_credit.max` = **3.02** USD (2026-01-01 → 2026-12-31) [A.2, US-COS5-001, quoted from authority page, conf high]
- `co.minwage.tipped.cash_wage` = **12.14** USD (2026-01-01 → 2026-12-31) [A.2, US-COS5-001, derived arithmetically, conf high] — 15.16 - 3.02.
- `co.minwage.minor_reduction.percent` = **15** percent (2026-01-01 → open) [A.2, US-COS5-001, quoted from authority page, conf high] — Unemancipated minors; not for some local minimum wages.
- `co.local_minwage.denver.hourly` = **19.29** USD (2026-01-01 → 2026-12-31) [A.2, US-COS5-010, derived arithmetically, conf high] — G-DERIVE: 18.81 x 1.0256 (CPI-W Denver-Aurora-Lakewood H1/H1) = 19.2915 -> 19.29.
- `co.local_minwage.denver.tipped_food_beverage` = **16.27** USD (2026-01-01 → 2026-12-31) [A.2, US-COS5-010, derived arithmetically, conf high] — 19.29 - 3.02, with at least 3.02 actual tips.
- `co.overtime.rule` = **1.5x after 40 h/week, 12 h/day or 12 consecutive hours; no comp time; agriculture after 48 h (56 highly seasonal)**  (2026-01-01 → open) [A.2, US-COS5-001, quoted from authority page, conf high]
- `co.overtime.daily_threshold_hours` = **12** hours (2026-01-01 → open) [A.2, US-COS5-001, quoted from authority page, conf high]
- `co.exempt.salary.annual_min` = **57784** USD (2026-01-01 → 2026-12-31) [A.2, US-COS5-001, quoted from authority page, conf high]
- `co.rest_break.paid_minutes_per_4h` = **10** minutes (2026-01-01 → open) [A.2, US-COS5-001, quoted from authority page, conf high] — Unprovided rest time paid as extra pay; meal 30 min for shifts over 5 h.
- `co.pay_frequency.rule` = **period no longer than one calendar month or 30 days; payday no later than 10 days after period close unless agreed (8-4-103(1)(a)); paydays posted**  (2025-08-06 → open) [A.1, US-COS5-002, direct artifact inspection, conf high]
- `co.payment.method` = **checks negotiable without discount; direct deposit only with voluntary authorisation; paycard only with free access to full net pay once per period or alternative (8-4-102)**  (2025-08-06 → open) [A.1, US-COS5-002, direct artifact inspection, conf high]

## 2 — Income tax (state withholding)
- `co.wh.method` = annualise; subtract 5,500 (11,000 MFJ/QSS) or DR 0004 line 2; x 4.40%; divide by periods; add DR 0004 line 3; no supplemental rate, no rounding rule (2026-01-01 → open) [A.2, US-COP51-001 — promoted to fact in Synthesis C] DR 1098 (2026).
- `co.pit.rate.flat` = **4.4** percent (2026-01-01 → 2026-12-31) [A.2, US-COS5-012, direct artifact inspection, conf high] — DR 0004 line 3 at 4.40%; method in DR 1098 2026 [US-COP51-001 legacy]. DR 1098 for 2027 not yet published.
- `co.wh.std_allowance.dr1098.single` = **5500** USD (2026-01-01 → 2026-12-31) [A.2, US-COS5-012, direct artifact inspection, conf medium] — DR 1098: subtract 5,500 (11,000 MFJ/QSS) or DR 0004 line 2.
- `co.wh.dr0004.table1.single.1_job` = **14000** USD (2026-01-01 → 2026-12-31) [A.2, US-COS5-012, direct artifact inspection, conf high] — Single/MFS 14,000 / 7,000 / 4,500 / 3,500 by jobs 1/2/3/4+.
- `co.wh.dr0004.table1.hoh.1_job` = **22000** USD (2026-01-01 → 2026-12-31) [A.2, US-COS5-012, direct artifact inspection, conf high] — HoH 22,000 / 11,000 / 7,500 / 5,500.
- `co.wh.dr0004.table1.mfj.1_job` = **30000** USD (2026-01-01 → 2026-12-31) [A.2, US-COS5-012, direct artifact inspection, conf high] — MFJ/QSS 30,000 / 15,000 / 10,000 / 7,500.
- `co.wh.obbba_overtime_deduction.allowed` = **False**  (2026-01-01 → open) [A.2, US-COS5-012, direct artifact inspection, conf high] — Worksheet 1 removes the qualified overtime deduction from W-4 Step 4(b); confirmed in the Guide [US-COS5-007].
- `co.wh.wages.conformity` = **wages subject to CO withholding = wages subject to federal withholding; federal exclusions generally flow through**  (2026-01-01 → open) [A.2, US-COS5-007, direct artifact inspection, conf high]
- `co.wh.exempt_w4_copy_threshold_weekly` = **200** USD (2026-01-01 → open) [A.2, US-COS5-006, direct artifact inspection, conf high] — W-4 claiming exempt with pay over 200/week and no DR 0004: copy to CDOR.

## 2b — Non-resident regime and reciprocity
- `co.nonres.rules` = **residents: all wages except where another state requires withholding; nonresidents: CO-source wages by days present; federal carve-outs rail/air (<=50% CO pay)/motor carrier/military/military spouse; telecommuters not taxed on work outside CO**  (2026-01-01 → open) [A.2, US-COS5-007, direct artifact inspection, conf high] — No reciprocity (Guide word search).

## 2c — Local wage taxes
OPTs are flat monthly amounts on separate city returns (T4). Sheridan 3+3 rests on tier-C MANUAL US-COP7-006: not a fact. Aurora OPT repealed 2025 (corroborated only).

- `co.local.opt.greenwood_village.employee_monthly` = **2** USD (2026-01-01 → open) [A.2, US-COS5-015, quoted from authority page, conf high] — Employer 2/month; trigger 250+ earned in the month in the Village; multiple OPT cities: city where most work done, primary employer only.
- `co.local.opt.greenwood_village.employer_monthly` = **2** USD (2026-01-01 → open) [A.2, US-COS5-015, quoted from authority page, conf high]
- `co.local.opt.greenwood_village.threshold_monthly` = **250** USD (2026-01-01 → open) [A.2, US-COS5-015, quoted from authority page, conf high]
- `co.local.opt.glendale.employee_monthly` = **5** USD (2026-01-01 → open) [A.2, US-COS5-016, quoted from authority page, conf high] — Employer 5/month; trigger more than 750 in the month.
- `co.local.opt.glendale.employer_monthly` = **5** USD (2026-01-01 → open) [A.2, US-COS5-016, quoted from authority page, conf high]
- `co.local.opt.glendale.threshold_monthly` = **750** USD (2026-01-01 → open) [A.2, US-COS5-016, quoted from authority page, conf high]
- `co.local.opt.denver.employee_monthly` = **5.75** USD (2025-01-01 → open) [A.2, US-COP7-004, quoted from authority page, conf medium] — Earnings >= 500/month; 2025 Tax Guide edition, 2026 edition not read (CO-OQ-5).
- `co.local.opt.denver.employer_monthly` = **4.0** USD (2025-01-01 → open) [A.2, US-COP7-005, quoted from authority page, conf medium] — 2026 edition not read.
- `co.local.opt.denver.threshold_monthly` = **500** USD (2025-01-01 → open) [A.2, US-COP7-004, quoted from authority page, conf medium]

## 3 — Social insurance (SUI / SDI / PFML / levies)
Experienced-employer support/solvency surcharges rest on MANUAL rows (US-COL-004, US-COP7-002/003). No employee UI share. FAMLI wage cap follows the SS wage base (FED). Employee may top up FAMLI with PTO.

- `co.sui.wage_base` = 30600 (2026-01-01 → 2026-12-31) [A.2, US-COP51-003 — promoted to fact in Synthesis C] Chargeable wage limit; 32,100 for 2027; employer only.
- `co.sui.wage_base.next_year` = 32100 (2027-01-01 → open) [A.2, US-COP51-003 — promoted to fact in Synthesis C]
- `co.sui.new_employer.rate.total` = 3.05 (2026-01-01 → 2026-12-31) [A.2, US-COP51-004 — promoted to fact in Synthesis C] 1.53% + support surcharge 0.17% + solvency 1.35% (non-construction); heavy construction 6.285%; 2027 1.70% combined, no solvency.
- `co.famli.total.rate` = 0.88 (2026-01-01 → 2026-12-31) [A.2, US-COFAMLI-001 — promoted to fact in Synthesis C] 0.44% employer + 0.44% employee on wages up to the SS wage base (184,500); statutory cap 1.2%.
- `co.famli.total.rate` = **0.86** percent (2027-01-01 → open) [A.2, US-COS5-008, quoted from authority page, conf high] — 2027 total; split and <10-employee exemption not read on a primary page (US-COP7-001 MANUAL).
- `co.sui.coverage` = **follows FUTA thresholds: employer 20 weeks / 1,500 quarter; agricultural 10 workers in 20 weeks or 20,000 quarter; domestic 1,000 quarter; excluded commission insurance/real-estate agents, casual labour, part-time for exempt nonprofits, students at own school**  (2023-01-01 → open) [A.2, US-COS5-014, direct artifact inspection, conf medium] — [partial row]

## 4 — Payslip statute
Electronic delivery consent: no rule read (open). SSN may appear instead of name (8-4-103(4)(e)).

- `co.payslip.items` = gross wages, withholdings/deductions, net wages, pay-period dates, employee name or SSN, employer name and address; at least monthly or each payment; records 3 years; fine up to 250 per employee per month max 7,500 (8-4-103(4)) (2025-08-06 → open) [A.1, US-COP51-005 — promoted to fact in Synthesis C]
- `co.payslip.comps_rule7_items` = **total pay, rate, tips, credits and time worked (in addition to Wage Act items); kept 3 years**  (2026-01-01 → open) [A.2, US-COS5-001, quoted from authority page, conf high]

## 5 — Statutory reporting instruments
UI quarterly wage report format/due date not read (CDLE 403); TPA authorisation in MyUI Employer+ [US-COP52-003 legacy]. New hire: CO page unreachable, federal default 20 days (42 USC 653a, FED unit). POA DR 0145.

- `co.report.wh.frequency` = **< 7,000/yr quarterly (last day of month after quarter); 7,000-50,000 monthly (15th); >= 50,000 weekly Sat-Fri (3rd business day after Friday, EFT mandatory); zero returns required; paper DR 1094**  (2026-01-01 → open) [A.2, US-COS5-006, direct artifact inspection, conf high]
- `co.report.wh.quarterly_threshold` = **7000** USD (2026-01-01 → open) [A.2, US-COS5-006, direct artifact inspection, conf high]
- `co.report.wh.weekly_threshold` = **50000** USD (2026-01-01 → open) [A.2, US-COS5-006, direct artifact inspection, conf high]
- `co.report.w2` = **due 31 January to employees and CDOR; e-file mandatory when federal e-file required (10+); Revenue Online .txt or XLSX template (10-100 employees, TY2026); paper with DR 1093; DR 0995 credit notice to every employee**  (2026-01-01 → open) [A.2, US-COS5-006, direct artifact inspection, conf high]
- `co.report.w2.xlsx_template` = **RE: tax year, employer name, ID type, EIN, address; RS: ID type/EIN, names, SSN (999999999 if none), address, boxes 1, 2, 15, 16, 17; optional local 18-20, second state, dates, weeks, SUI wages**  (2026-01-01 → open) [A.2, US-COS5-013, direct artifact inspection, conf high]
- `co.report.famli.quarterly` = **My FAMLI+ Employer, due one month after quarter end; file and API specs published; ITINs in bulk files from 2026-10-01**  (2026-01-01 → open) [A.2, US-COS5-008, quoted from authority page, conf high]

## 6 — Leave
- `co.leave.sick.accrual.hours_worked_per_hour` = **30** hours (2022-01-01 → open) [A.1, US-COS5-005, direct artifact inspection, conf medium] — [partial row] HFWA 2023 text (partial row): cap 48 h/yr; carry over up to 48; front-load allowed; no payout; reinstated on rehire within 6 months; PHE supplement 80 h; amendments 2024-2026 unchecked.
- `co.leave.sick.cap_hours` = **48** hours (2022-01-01 → open) [A.1, US-COS5-005, direct artifact inspection, conf medium] — [partial row]
- `co.leave.sick.payout_on_separation` = **False**  (2022-01-01 → open) [A.1, US-COS5-005, direct artifact inspection, conf medium] — [partial row]

## 7 — Termination and final pay
- `co.final_pay.rule` = **discharge: immediately (6 h after next workday start if payroll unit closed, 24 h if off-site); resignation: next regular payday; unclaimed check mailed after 60 days**  (2025-08-06 → open) [A.1, US-COS5-003, direct artifact inspection, conf high]
- `co.final_pay.penalty.min` = **1000** USD (2025-08-06 → open) [A.1, US-COS5-003, direct artifact inspection, conf high] — Greater of 2x unpaid wages or 1,000 if unpaid 14 days after written demand (8-4-109(3)(b)).
- `co.final_pay.vacation_payout` = **True**  (2025-08-06 → open) [A.1, US-COS5-003, direct artifact inspection, conf high] — Earned and determinable vacation is wages (8-4-101(14)(a)(III)); owed even if fired for cause [US-COS5-001]. Severance not wages.

## 8 — Benefits in kind / taxable wages
- `co.lodging_credit.weekly_min` = **25** USD (2026-01-01 → open) [A.2, US-COS5-001, quoted from authority page, conf high] — Lodging credit 25-100/week; meals at cost or value; no uniform charges.
- `co.lodging_credit.weekly_max` = **100** USD (2026-01-01 → open) [A.2, US-COS5-001, quoted from authority page, conf high]

## 9 — Deductions and garnishments
- `co.deductions.permitted` = **(a) required by law; (a.5) auto-enrolment retirement; (b) written agreement for loans/advances/goods/equipment; (c) theft after police report; (d) revocable authorisation; (e) unreturned property of terminated employee with notice within 10 days (8-4-105)**  (2025-08-06 → open) [A.1, US-COS5-004, direct artifact inspection, conf high]
- `co.garn.creditor.max_percent` = **20** percent (2022-01-01 → open) [A.3, US-COS5-009, direct artifact inspection, conf medium] — Form 26 SC (R 1/22): exempt greater of 80% of disposable earnings or 40x/80x/86.67x/173.3x higher of state/federal MW; disposable earnings also deduct employer-provided health insurance (CO departure); support first; start first pay date >= 21 days after service.
- `co.garn.creditor.weekly_floor` = **606.4** USD (2026-01-01 → 2026-12-31) [A.3, US-COS5-009, derived arithmetically, conf high] — 40 x 15.16.

## 10 — Collective agreements / prevailing wage
- `co.prevailing_wage.threshold` = 500000 (2026-01-01 → open) [A.2, US-COP52-002 — promoted to fact in Synthesis C] C.R.S. 24-92-201 ff.; weekly pay required.

## 11 — Indexation
State MW CPI-indexed yearly (PAY CALC Order/COMPS poster); Denver CPI-W H1/H1; EAP threshold yearly; UI limit statutory steps 27,200 -> 30,600 -> 32,100; FAMLI set yearly (cap 1.2%); OPTs fixed.


## 12 — Payroll data protection / records
C.R.S. 6-1-713/-713.5/-716 not read (coag.gov 202-empty). No truncation duty on the pay statement.


## 13 — Live legal change
FAMLI 2027 0.86%; UI 2027 base 32,100 and new 1.70%; OBBBA overtime decoupling; XLSX W-2 route; FAMLI ITIN files 2026-10-01; SecureSavings registration duty (programme page not read). CDLE news and Colorado Register not swept (403).


## Special populations (US-OWN-005)
- Domestic: UI FUTA threshold 1,000/quarter [US-COS5-014].
- Agricultural: OT after 48 h (56 seasonal); migratory-laborer disclosures in worker language (8-4-117); 5% language rule [US-COS5-001, US-COS5-014, US-COL-002, US-COP9L-001].
- Minors: 15% below state MW for unemancipated minors [US-COS5-001].
- Tipped: tip credit 3.02; state 12.14; Denver 16.27; tips employee property [US-COS5-001, US-COS5-010, US-COS5-002].
- Clergy / statutory employees: no state rule beyond federal [US-COS5-007, US-COS5-014].
- Students: UI excludes students at own school (not student nurses) [US-COS5-014].
- NRAs: W-2 template SSN 999999999 if none, CO withholding required without valid TIN; FAMLI accepts ITINs [US-COS5-013, US-COS5-008].
- Government: Wage Act excludes state/counties/municipalities/school districts; HFWA includes them, excludes federal [US-COS5-002, US-COS5-005].
- Military/spouses and interstate transport: nonresident exemptions [US-COS5-007].
- Multistate: HFWA covers all employees working in CO (only CO hours accrue - inference); SUI other-state credit and FAMLI multistate coverage open.

## Language seams (US-OWN-006)
CO 8-13.3-408(2) English + first language of 5% of workforce for HFWA notice [US-COL-001]; COMPS Rule 7.4.3 Spanish COMPS/poster [US-COP9L-001]; DR 0995 notice in English plus usual language [US-COS5-006]; payslip English (US-OWN-006).

## Synthesis D additions (2026-11-02)

Source: browser-pass rows S5B-P1 / S5B-P2 merged into `legal-basis-register.csv` and SSA EFW2 TY2026 (US-FEDS5-032) read locally. Every claim below carries its register_id; the facts file is authoritative. Full log: `_research/synthesis-D/SYNTHESIS-D.md`.

Facts added:
- `co.minwage.minor.hourly` = **12.89** USD (2026-01-01 → 2026-12-31) [A.1, US-COB5-001, direct artifact inspection, conf high] — Non-emancipated minors, 15% below the full minimum (15.16 x 0.85 = 12.886 -> 12.89).
- `co.exempt.salary.weekly_min` = **1111.23** USD (2026-01-01 → 2026-12-31) [A.1, US-COB5-001, direct artifact inspection, conf high] — EAP exemption salary; 1,111.23 x 52 = 57,783.96 -> 57,784/yr (co.exempt.salary.annual_min).
- `co.exempt.highly_technical_computer.hourly_min` = **34.85** USD (2026-01-01 → 2026-12-31) [A.1, US-COB5-001, direct artifact inspection, conf high]
- `co.exempt.highly_compensated.annual_min` = **130014** USD (2026-01-01 → 2026-12-31) [A.1, US-COB5-001, direct artifact inspection, conf high]
- `co.wage_claim.max_amount` = **7500** USD (2026-01-01 → 2026-06-30) [A.1, US-COB5-001, direct artifact inspection, conf high] — Administrative wage-claim ceiling per employee.
- `co.wage_claim.max_amount` = **13000** USD (2026-07-01 → 2027-12-31) [A.1, US-COB5-001, direct artifact inspection, conf high]
- `co.famli.employee.rate` = **0.44** percent (2026-01-01 → 2026-12-31) [A.2, US-COB5-003, quoted from authority page, conf high] — Employee share never above 50% of the premium.
- `co.famli.employer.rate` = **0.44** percent (2026-01-01 → 2026-12-31) [A.2, US-COB5-003, quoted from authority page, conf high]
- `co.famli.small_employer.max_employees` = **9** (2026-01-01 → open) [A.2, US-COB5-003, quoted from authority page, conf high] — Employers with 9 or fewer employees remit only the 0.44% employee share (no employer share).

Facts changed:
- `co.minwage.hourly` (2026-01-01): register_id 'US-COS5-001' → 'US-COB5-001'; tier 'A.2' → 'A.1'; verification_method 'quoted from authority page' → 'second independent authority'; note += '2026 PAY CALC Order (7 CCR 1103-14, adopted 2025-12-08, Rule 1.2.1) agrees with the CDLE COMPS poster (US-COS5-001).'
- `co.minwage.tip_credit.max` (2026-01-01): register_id 'US-COS5-001' → 'US-COB5-001'; tier 'A.2' → 'A.1'; verification_method 'quoted from authority page' → 'second independent authority'; note += '2026 PAY CALC Order (7 CCR 1103-14, adopted 2025-12-08, Rule 1.2.1) agrees with the CDLE COMPS poster (US-COS5-001).'
- `co.minwage.tipped.cash_wage` (2026-01-01): register_id 'US-COS5-001' → 'US-COB5-001'; tier 'A.2' → 'A.1'; verification_method 'derived arithmetically' → 'second independent authority'; note += '2026 PAY CALC Order (7 CCR 1103-14, adopted 2025-12-08, Rule 1.2.1) agrees with the CDLE COMPS poster (US-COS5-001).'
- `co.exempt.salary.annual_min` (2026-01-01): register_id 'US-COS5-001' → 'US-COB5-001'; tier 'A.2' → 'A.1'; verification_method 'quoted from authority page' → 'second independent authority'; note += '2026 PAY CALC Order (7 CCR 1103-14, adopted 2025-12-08, Rule 1.2.1) agrees with the CDLE COMPS poster (US-COS5-001).'
- `co.minwage.hourly` (2026-01-01): note 'COMPS Rule 3; highest applicable (local) minimum applies. 2027 15.71 is tier-B only (US-COS5-011 MANUAL), not a fact. 2026 PAY CALC Order (7 CCR 1103-14, adopted 2025-12-08, Rule 1.2.1) agrees with the CDLE COMPS poster (US-COS5-001).' → 'COMPS Rule 3; highest applicable (local) minimum applies. 2026 PAY CALC Order (7 CCR 1103-14, adopted 2025-12-08, Rule 1.2.1) agrees with the CDLE COMPS poster (US-COS5-001). 2027 15.71 is a PROPOSED rule (US-COB5-002, provisional): not a fact until adopted.'
- `co.minwage.tipped.cash_wage` (2026-01-01): note '15.16 - 3.02. 2026 PAY CALC Order (7 CCR 1103-14, adopted 2025-12-08, Rule 1.2.1) agrees with the CDLE COMPS poster (US-COS5-001).' → '15.16 - 3.02; now quoted directly in the 2026 PAY CALC Order (12.14). 2026 PAY CALC Order (7 CCR 1103-14, adopted 2025-12-08, Rule 1.2.1) agrees with the CDLE COMPS poster (US-COS5-001).'

Keys renamed (no alias kept; agent 4 must re-bind):
- `co.famli.rate.total.2026` → `co.famli.total.rate` (fact effective 2026-01-01; year removed from the key, register US-COFAMLI-001)
- `co.famli.rate.total` → `co.famli.total.rate` (fact effective 2027-01-01, register US-COS5-008). Kept key = the WTC/m05 convention `{st}.pfml.total.rate` / `md.famli.total.rate`; WTC already used `co.famli.total.rate` for both years, so CCG annex and WTC now share one key.

Open questions narrowed / added: `co.local_minwage.other_cities`, `co.minwage.hourly.next_year` (lines rewritten in the block below).

Still open, new attempts recorded in `unresolved[].attempted`: `co.famli.split.next_year`.

## QA r1b additions (2026-11-02)

Source: browser pass P3 (`_research/stage5/browser-pass-P3.md`, shard `S5B-P3.csv` merged into the register). Facts file is authoritative; every line below is a fact object with the same key.

**3 - Social insurance: FAMLI 2027 (RQ-490, rate closed).** CDLE FAMLI Business Brief 2026-09-30: 0.86% from 2027-01-01 [A.3 bulletin copy US-COB5-301; the same bulletin is US-COS5-008, A.2]. Split derived from the standing 50% employee cap [US-COB5-003]: 0.86 x 0.5 = 0.43. Residual (non-blocking): A.1 text of the cap.

- `co.famli.employee.rate` = **0.43** percent (2027-01-01 -> open) [A.3, US-COB5-301, derived arithmetically, conf medium] Maximum employee share 2027: 0.86% x 50% = 0.43%. The 0.86% total is on the CDLE bulletin of 2026-09-30; the 50% employee cap is the standing rule on famli.colorado.gov (US-COB5-003, 2026 page) and is not restated in the bulletin.
- `co.famli.employer.rate` = **0.43** percent (2027-01-01 -> open) [A.3, US-COB5-301, derived arithmetically, conf medium] 0.86% - 0.43% employee share = 0.43%, for employers with 10+ employees that deduct the full employee share. Employers with 9 or fewer employees owe no employer share (co.famli.small_employer.max_employees, open-ended).

**1 - Labour code: Boulder localities (narrows RQ-491).** Boulder County [A.2, US-COB5-302] and City of Boulder Ord. 8664 [A.2, US-COB5-303]; both rows supersede the tier-B lead US-COS5-011 for these two localities only (that row stays MANUAL for Edgewater 2026 and Denver 2027). City 2027 (18.17) is conf medium: the page dates from the 2025 launch.

- `co.local_minwage.boulder_county_unincorporated.hourly` = **16.82** USD (2026-01-01 -> 2026-12-31) [A.2, US-COB5-302, quoted from authority page, conf high] Unincorporated Boulder County (ordinance amended November 2025).
- `co.local_minwage.boulder_county_unincorporated.hourly` = **17.43** USD (2027-01-01 -> open) [A.2, US-COB5-302, quoted from authority page, conf high]
- `co.local_minwage.boulder_city.hourly` = **16.82** USD (2026-01-01 -> 2026-12-31) [A.2, US-COB5-303, quoted from authority page, conf high] City of Boulder Ord. 8664 schedule: 15.57 (2025), 16.82 (2026), 18.17 (2027), CPI from 2028.
- `co.local_minwage.boulder_city.hourly` = **18.17** USD (2027-01-01 -> open) [A.2, US-COB5-303, quoted from authority page, conf medium] From the Ord. 8664 FAQ written for the 2025 launch; no later City amendment found (the County lowered its own 2027 step to 17.43 in Nov 2025). Re-check before 2027-01-01.

## Open questions

Mirrors `unresolved[]` in the facts file (same keys, same wording). Regenerated by QA r1b on 2026-11-02.

- `co.sui.wage_base.other_state_credit` (non-blocking) — C.R.S. 8-76-102 text and CDLE premiums page unreachable (403). **Would close it:** C.R.S. 8-76-102 text, CDLE Employer Handbook, or DOL Significant Provisions of State UI Laws 2026 CO line.
- `co.famli.split.next_year` (non-blocking) — 2027 total 0.86% is published (CDLE bulletin, US-COS5-008 / US-COB5-301) and the 2027 split 0.43/0.43 is derived from the standing 50% employee cap read on the 2026 employer page (US-COB5-003). Not read: an A.1 text of the 50% cap and the small-employer exemption (C.R.S. 8-13.3-507, 7 CCR 2702-3). **Would close it:** C.R.S. 8-13.3-507 or 7 CCR 2702-3 text (Colorado Register / famli.colorado.gov), only to upgrade the split from derived to A.1.
- `co.local_minwage.other_cities` (blocking) — City of Boulder and unincorporated Boulder County 2026/2027 are now facts (US-COB5-302/-303). Edgewater 2026 (lead 18.17) and Denver 2027 (lead 19.84) still rest only on tier-B leads (US-COS5-011 MANUAL): edgewaterco.com returns Akamai 403 and denvergov.org a WAF block from the Brazil exit. **Would close it:** City of Edgewater minimum wage ordinance/notice for 2026 and the Denver Labor 2027 minimum wage notice, read from a US exit.
- `co.report.sui.quarterly` (non-blocking) — CDLE MyUI Employer+ wage-report format/due date and CO new-hire specifics not read (CDLE 403; childsupport.colorado.gov timeout). **Would close it:** CDLE MyUI Employer+ wage-report guide and Colorado State Directory of New Hires page.
- `co.local.opt.denver.current_edition` (non-blocking) — Denver OPT figures come from the 2025 Tax Guide; 2026 edition not read; Sheridan only tier C. **Would close it:** Denver Tax Guide Topic 61 2026 revision and the Sheridan city page.
- `co.leave.sick.amendments_and_payslip_econsent` (non-blocking) — HFWA amendments 2024-2026 and electronic pay-statement consent unread (CDLE 403). **Would close it:** CDLE current HFWA text and INFO #6/#13 (browser pass).
- `co.data_protection.statutes` (non-blocking) — 6-1-713/-713.5/-716 and SecureSavings payroll-deduction duties unread (coag.gov 202-empty). **Would close it:** coag.gov data-protection page and the Colorado SecureSavings employer page.
- `co.minwage.hourly.next_year` (non-blocking) — The 2027 state minimum (15.71; tipped 12.69; minors 13.36; EAP 1,151.23/week = 59,864/yr; computer 36.10/h; highly compensated 134,694) exists only as the PROPOSED 2027 PAY CALC Order (US-COB5-002, status provisional; hearing 2026-11-02; rulemaking page shows 'Adopted N/A'). **Would close it:** The adopted 2027 PAY CALC Order (7 CCR 1103-14) posted on the CDLE 'Labor rules proposed and adopted' page.

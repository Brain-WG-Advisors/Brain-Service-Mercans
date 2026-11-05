# CCG annex_CO research pack — Colorado

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
- `co.wh.method` = annualise; subtract 5,500 (11,000 MFJ/QSS) or DR 0004 line 2; x 4.40%; divide by periods; add DR 0004 line 3; no supplemental rate, no rounding rule (2026-01-01 → open) [A.2, US-CO-P5-1-001 — legacy id, NOT a fact] DR 1098 (2026).
- `co.pit.rate.flat` = **4.4** percent (2026-01-01 → 2026-12-31) [A.2, US-COS5-012, direct artifact inspection, conf high] — DR 0004 line 3 at 4.40%; method in DR 1098 2026 [US-CO-P5-1-001 legacy]. DR 1098 for 2027 not yet published.
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

- `co.sui.wage_base` = 30600 (2026-01-01 → 2026-12-31) [A.2, US-CO-P5-1-003 — legacy id, NOT a fact] Chargeable wage limit; 32,100 for 2027; employer only.
- `co.sui.wage_base.next_year` = 32100 (2027-01-01 → open) [A.2, US-CO-P5-1-003 — legacy id, NOT a fact]
- `co.sui.new_employer.rate.total` = 3.05 (2026-01-01 → 2026-12-31) [A.2, US-CO-P5-1-004 — legacy id, NOT a fact] 1.53% + support surcharge 0.17% + solvency 1.35% (non-construction); heavy construction 6.285%; 2027 1.70% combined, no solvency.
- `co.famli.rate.total.2026` = 0.88 (2026-01-01 → 2026-12-31) [A.2, US-CO-FAMLI-001 — legacy id, NOT a fact] 0.44% employer + 0.44% employee on wages up to the SS wage base (184,500); statutory cap 1.2%.
- `co.famli.rate.total` = **0.86** percent (2027-01-01 → open) [A.2, US-COS5-008, quoted from authority page, conf high] — 2027 total; split and <10-employee exemption not read on a primary page (US-COP7-001 MANUAL).
- `co.sui.coverage` = **follows FUTA thresholds: employer 20 weeks / 1,500 quarter; agricultural 10 workers in 20 weeks or 20,000 quarter; domestic 1,000 quarter; excluded commission insurance/real-estate agents, casual labour, part-time for exempt nonprofits, students at own school**  (2023-01-01 → open) [A.2, US-COS5-014, direct artifact inspection, conf medium] — [partial row]

## 4 — Payslip statute
Electronic delivery consent: no rule read (open). SSN may appear instead of name (8-4-103(4)(e)).

- `co.payslip.items` = gross wages, withholdings/deductions, net wages, pay-period dates, employee name or SSN, employer name and address; at least monthly or each payment; records 3 years; fine up to 250 per employee per month max 7,500 (8-4-103(4)) (2025-08-06 → open) [A.1, US-CO-P5-1-005 — legacy id, NOT a fact]
- `co.payslip.comps_rule7_items` = **total pay, rate, tips, credits and time worked (in addition to Wage Act items); kept 3 years**  (2026-01-01 → open) [A.2, US-COS5-001, quoted from authority page, conf high]

## 5 — Statutory reporting instruments
UI quarterly wage report format/due date not read (CDLE 403); TPA authorisation in MyUI Employer+ [US-CO-P5-2-003 legacy]. New hire: CO page unreachable, federal default 20 days (42 USC 653a, FED unit). POA DR 0145.

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
- `co.prevailing_wage.threshold` = 500000 (2026-01-01 → open) [A.2, US-CO-P5-2-002 — legacy id, NOT a fact] C.R.S. 24-92-201 ff.; weekly pay required.

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

## Open questions
Mirrors `unresolved[]` in the facts file (same keys).

- `co.wh.method` (non-blocking) — Value annualise; subtract 5,500 (11,000 MFJ/QSS) or DR 0004 line 2; x 4.40%; divide by periods; add DR 0004 line 3; no supplemental rate, no rounding rule (from 2026-01-01) is carried by register row US-CO-P5-1-001 (active, A.2, Colorado Department of Revenue), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. DR 1098 (2026). **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-CO-P5-1-001) or re-key US-CO-P5-1-001; then emit this key as a fact. No new research needed.
- `co.sui.wage_base` (non-blocking) — Value 30600 (from 2026-01-01) is carried by register row US-CO-P5-1-003 (active, A.2, Colorado Department of Labor and Employment, UI Division), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. Chargeable wage limit; 32,100 for 2027; employer only. **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-CO-P5-1-003) or re-key US-CO-P5-1-003; then emit this key as a fact. No new research needed.
- `co.sui.wage_base.next_year` (non-blocking) — Value 32100 (from 2027-01-01) is carried by register row US-CO-P5-1-003 (active, A.2, Colorado Department of Labor and Employment, UI Division), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-CO-P5-1-003) or re-key US-CO-P5-1-003; then emit this key as a fact. No new research needed.
- `co.sui.new_employer.rate.total` (non-blocking) — Value 3.05 (from 2026-01-01) is carried by register row US-CO-P5-1-004 (active, A.2, Colorado Department of Labor and Employment, UI Division), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. 1.53% + support surcharge 0.17% + solvency 1.35% (non-construction); heavy construction 6.285%; 2027 1.70% combined, no solvency. **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-CO-P5-1-004) or re-key US-CO-P5-1-004; then emit this key as a fact. No new research needed.
- `co.famli.rate.total.2026` (non-blocking) — Value 0.88 (from 2026-01-01) is carried by register row US-CO-FAMLI-001 (active, A.2, Colorado FAMLI Division (CDLE)), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. 0.44% employer + 0.44% employee on wages up to the SS wage base (184,500); statutory cap 1.2%. **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-CO-FAMLI-001) or re-key US-CO-FAMLI-001; then emit this key as a fact. No new research needed.
- `co.payslip.items` (non-blocking) — Value gross wages, withholdings/deductions, net wages, pay-period dates, employee name or SSN, employer name and address; at least monthly or each payment; records 3 years; fine up to 250 per employee per month max 7,500 (8-4-103(4)) (from 2025-08-06) is carried by register row US-CO-P5-1-005 (active, A.1, Colorado Division of Labor Standards and Statistics (CDLE)), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-CO-P5-1-005) or re-key US-CO-P5-1-005; then emit this key as a fact. No new research needed.
- `co.prevailing_wage.threshold` (non-blocking) — Value 500000 (from 2026-01-01) is carried by register row US-CO-P5-2-002 (active, A.2, Colorado Office of the State Architect (DPA)), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. C.R.S. 24-92-201 ff.; weekly pay required. **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-CO-P5-2-002) or re-key US-CO-P5-2-002; then emit this key as a fact. No new research needed.
- `co.sui.wage_base.other_state_credit` (non-blocking) — C.R.S. 8-76-102 text and CDLE premiums page unreachable (403). **Would close it:** C.R.S. 8-76-102 text, CDLE Employer Handbook, or DOL Significant Provisions of State UI Laws 2026 CO line.
- `co.famli.split.next_year` (blocking) — 2027 employee/employer split, under-10-employee employer exemption and multistate coverage not read on a primary page (famli.colorado.gov 403). **Would close it:** 7 CCR 2702-3 and C.R.S. 8-13.3-507 via famli.colorado.gov or Colorado Register (browser pass).
- `co.local_minwage.other_cities` (blocking) — Edgewater, City of Boulder, Boulder County 2026 and state/Denver 2027 values are tier B only; the CDLE PAY CALC Order (7 CCR 1103-14) is a 403 page. **Would close it:** CDLE 2026/2027 PAY CALC Order and Denver Finance 2026 news release (browser pass).
- `co.report.sui.quarterly` (non-blocking) — CDLE MyUI Employer+ wage-report format/due date and CO new-hire specifics not read (CDLE 403; childsupport.colorado.gov timeout). **Would close it:** CDLE MyUI Employer+ wage-report guide and Colorado State Directory of New Hires page.
- `co.local.opt.denver.current_edition` (non-blocking) — Denver OPT figures come from the 2025 Tax Guide; 2026 edition not read; Sheridan only tier C. **Would close it:** Denver Tax Guide Topic 61 2026 revision and the Sheridan city page.
- `co.leave.sick.amendments_and_payslip_econsent` (non-blocking) — HFWA amendments 2024-2026 and electronic pay-statement consent unread (CDLE 403). **Would close it:** CDLE current HFWA text and INFO #6/#13 (browser pass).
- `co.data_protection.statutes` (non-blocking) — 6-1-713/-713.5/-716 and SecureSavings payroll-deduction duties unread (coag.gov 202-empty). **Would close it:** coag.gov data-protection page and the Colorado SecureSavings employer page.

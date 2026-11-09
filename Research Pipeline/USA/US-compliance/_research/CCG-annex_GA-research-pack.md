# CCG annex_GA research pack — Georgia

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B, 2026-11-02. Source: `_research/stage5/GA.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_GA-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** Federal minimum wage applies (state 5.15 nominal); local mandates pre-empted (34-4-3.1). Flat PIT 4.99% for 2026 (HB 463, signed 2026-05-11, retroactive; withholding at 4.99% from 2026-05-11); withholding standard deduction 24,000/12,000 and dependent 4,000 at 5.19% for wages paid 2026-01-01..2026-05-10 (Dec-2025 guide Table E, US-GAV7-001), 30,000/15,000 and 5,000 at 4.99% from 2026-05-11 (US-GAS5-001; transition rule US-GAV7-002); G-4 certificate; no local tax, no reciprocity; HB 463 OT/tip subtractions at assessment only. SUI base 9,500, new employer 2.70% (2.64% + 0.06% admin assessment to 2026-12-31). No pay-statement statute. New-hire within 10 days. Oracle: DOR guide percentage-method example 27.03.

## 1 — Employment / labour code
Overtime: FLSA only (1.5x over 40); no daily OT, no break law [US-GAS5-016, US-GAS5-008]. State-rate exclusions (40,000 sales etc.) tier-B only.

- `ga.minwage.state.hourly` = **5.15** USD (2026-01-01 → open) [A.2, US-GAS5-022, direct artifact inspection, conf medium] — O.C.G.A. 34-4-3; GDOL: the federal 7.25 applies with limited exceptions [US-GAS5-008]. Not indexed; no 2027 increase.
- `ga.minwage.state.exemptions` = 34-4-3(b)-(c): sales of 40,000 USD or less; five employees or less; domestic; farm owner/sharecropper/land renter; gratuity-paid; high-school/college students; newspaper carriers; resident nonprofit child-caring/long-term-care staff paid at least 10,000 USD cash a year; employers subject to a higher federal minimum (2001-07-01 → open) [A.1, US-GAV6C-001, second independent authority, conf high].
- `ga.local_mandates.preempted` = **True**  (2026-01-01 → open) [A.1, US-GAS5-017, direct artifact inspection, conf high] — 34-4-3.1 pre-empts local wage/benefit/scheduling mandates; HB 1157 (2026) repeal introduced, NOT enacted.
- `ga.pay_frequency.rule` = **at least semi-monthly in two equal periods per month; officers/superintendents/department heads monthly (34-7-2)**  (2026-01-01 → open) [A.1, US-GAP9L-001, direct artifact inspection, conf high]
- `ga.payment.method` = **money, check, direct deposit with consent, or payroll card (written fee explanation at hire or 30 days before; opt-out; one free access) - full net amount**  (2026-01-01 → open) [A.1, US-GAP9L-001, direct artifact inspection, conf high]

## 2 — Income tax (state withholding)
- `ga.pit.rate.flat` = **4.99** percent (2026-01-01 -> open) [A.1, US-GAS5-009, second independent authority, conf high] - Statutory rate for taxable year 2026, retroactive to 2026-01-01 (HB 463); the year-end assessment applies 4.99% to all 2026 wages. Withholding level: ga.wh.rate. LEVEL: assessment.
- `ga.wh.rate` = **5.19** percent (2026-01-01 -> 2026-05-10) [A.2, US-GA-001, quoted from authority page, conf high] - Employers kept withholding 5.19% until HB 463 was signed (2026-05-11). LEVEL: withholding.
- `ga.wh.rate` = **4.99** percent (2026-05-11 -> open) [A.1, US-GAS5-009, second independent authority, conf high] - Withholding at 4.99% from 2026-05-11 (DOR Employer Guide US-GA-001 states the start date; HB 463 the rate). LEVEL: withholding.
- `ga.wh.method` = **tax tables (pp. 31-50) or percentage method (Tables E/F): (wages - period standard deduction - dependent allowance x n) x 4.99%; tables use top of band**  (2026-01-01 → open) [A.2, US-GAS5-001, derived arithmetically, conf high] — Per-period values = annual / periods rounded to cent (21 values re-derived in Python); daily = annual/365. Tables and formula "differ slightly".
- `ga.wh.std_deduction.mfj` = **24000** USD (2026-01-01 → 2026-05-10) [A.2, US-GAV7-001, quoted from authority page, conf high] — Dec-2025 guide Table E col (1); weekly 461.54, biweekly 923.08, semimonthly 1,000, monthly 2,000, quarterly 6,000, semiannual 12,000, daily 65.75. Used with 5.19% (`ga.wh.rate`).
- `ga.wh.std_deduction.mfj` = **30000** USD (2026-05-11 → open) [A.2, US-GAS5-001, derived arithmetically, conf high] — Single/HoH 15,000; MFS 15,000; married both working use MFS column.
- `ga.wh.std_deduction.single` = **12000** USD (2026-01-01 → 2026-05-10) [A.2, US-GAV7-001, quoted from authority page, conf high] — Table E col (2) Single/HoH; col (3) MFS identical; weekly 230.77, biweekly 461.54, semimonthly 500, monthly 1,000, daily 32.88.
- `ga.wh.std_deduction.single` = **15000** USD (2026-05-11 → open) [A.2, US-GAS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-GAS5-001: Percentage method: (1) wages less standard deduction per period [annual 30,000 MFJ / 15,000 Single-HoH / 15,000 MFS; weekly 576.92/288.46/288.46; biweekly 1,153.85/576.92; semimonthly 1,250.00/625.00; monthly 2,500.00/1,250.00; quarterly 7,500/3,750; semiannual 15,000/7,500; daily 82.19/41.10]; (2) 
- `ga.wh.dependent_allowance` = **4000** USD (2026-01-01 → 2026-05-10) [A.2, US-GAV7-001, quoted from authority page, conf high] — Table E col (4); weekly 76.92, biweekly 153.85, semimonthly 166.67, monthly 333.33, daily 10.96.
- `ga.wh.dependent_allowance` = **5000** USD (2026-05-11 → open) [A.2, US-GAS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-GAS5-001: Percentage method: (1) wages less standard deduction per period [annual 30,000 MFJ / 15,000 Single-HoH / 15,000 MFS; weekly 576.92/288.46/288.46; biweekly 1,153.85/576.92; semimonthly 1,250.00/625.00; monthly 2,500.00/1,250.00; quarterly 7,500/3,750; semiannual 15,000/7,500; daily 82.19/41.10]; (2) 
- **V11 (2026-11-06, V-04).** The Jun-2026 guide [US-GAV7-002] says HB 463 is retroactive to 1 Jan 2026 for the *taxable year* (assessment) but "Employers must continue to withhold at the rate of 5.19% before the effective date of the change and can begin withholding at the new rate of 4.99%, starting May 11, 2026". The only withholding table in force before 11 May was the Dec-2025 Table E (24,000/12,000/12,000/4,000). `ga.wh.method` (and WTC `ga.sit.method`) are split on the same date. G-DERIVE: every Dec-2025 per-period value = annual / periods (52, 26, 24, 12, 4, 2, 365), half-up to the cent, re-derived in Python, 21/21 match.
- `ga.wh.certificate.form` = **G-4 Rev. 06/03/26: letters A Single, B MFS or MFJ both working, C MFJ one working, D HoH; line 4 dependents; line 5 adjustment allowances (/5,000, remainder >2,500 rounds up); line 6 additional; 8a exempt; 8b MSRRA**  (2026-06-03 → open) [A.2, US-GAS5-010, direct artifact inspection, conf high] — Mail to DOR only if >14 allowances or exempt; no G-4: use W-4 if sufficient else Single 0; exempt valid to 15 Feb next year [US-GAS5-004].
- `ga.wh.supplemental.rate` = **applicable income tax rate in effect when paid (4.99% from 2026-05-11); no separate table**  (2026-01-01 → open) [A.2, US-GAS5-004, direct artifact inspection, conf high]
- `ga.pit.overtime_subtraction.max` = **1750** USD (2026-01-01 → 2028-12-31) [A.1, US-GAS5-009, second independent authority, conf high] — HB 463: full-time hourly OT 2026-2028; operating level ASSESSMENT only, do not reduce withholding; W-2 box 12 TT, box 14b TTOC; RLA "GA OT" 14a; G-7 quarterly totals from 2027 [US-GAS5-003].
- `ga.pit.tip_subtraction.max` = **1750** USD (2026-01-01 → open) [A.1, US-GAS5-009, second independent authority, conf high] — Assessment only; W-2 box 12 TP.

## 2b — Non-resident regime and reciprocity
- `ga.nonres.threshold` = **withhold for nonresidents when more than 5% of wages or more than 5,000 is attributable to Georgia**  (2026-01-01 → open) [A.2, US-GAS5-004, direct artifact inspection, conf high] — Resident: legal resident, living in GA regularly, or 183+ days in 365 ending 31 Dec. Residents working elsewhere: no GA withholding if that state requires it. No reciprocity, no 23-day rule [US-GAP52-003]. NRAs: withhold unless 8233 filed and copy sent to DOR.
- `ga.nonres.threshold_amount` = **5000** USD (2026-01-01 → open) [A.2, US-GAS5-004, direct artifact inspection, conf high]
- `ga.nonres.threshold_percent` = **5** percent (2026-01-01 → open) [A.2, US-GAS5-004, direct artifact inspection, conf high]

## 3 — Social insurance (SUI / SDI / PFML / levies)
Experience rate by reserve ratio; DOL-626 notices on the Employer Portal by 31 Dec. 2026 rate range not on an A-tier source (tier-B 0.04-8.10%): not a fact (Q2). No SDI/PFML (US-GAP51-003 is not active; absence rests on the US-OWN-007 levy census and US-GAP9W-001/-003).

- `ga.sui.wage_base` = 9500 (2013-01-01 → open) [A.2, US-GAW1B-001 — promoted to fact in Synthesis C] HB 347 (2012), not indexed; employer-only (no employee contribution).
- `ga.sui.new_employer.rate.total` = **2.7** percent (2026-01-01 → 2026-12-31) [A.1, US-GAS5-013, derived arithmetically, conf high] — 2.64% contribution (34-8-151(d)) + 0.06% admin assessment (34-8-181) = 2.70%. From 2027 2.7% contribution only (Art. 6 repealed 2027-01-01).
- `ga.sui.admin_assessment.rate` = **0.06** percent (2024-01-01 → 2026-12-31) [A.1, US-GAS5-013, second independent authority, conf high] — May not be deducted from wages; only employer levy [US-GAP9W-001, US-GAP9W-003].
- `ga.sui.new_employer.rate.contribution` = **2.7** percent (2027-01-01 → open) [A.1, US-GAS5-013, second independent authority, conf high] — 34-8-151(a), absent new legislation (none located).
- `ga.sui.coverage` = **1 worker in 20 weeks or 1,500 quarter; agricultural 10 in 20 weeks or 20,000; domestic 1,000 quarter; 501(c)(3) 4 in 20 weeks; officers are employees; UI wages include 401(k) deferrals, tips (FUTA extent), board and lodging; exclude 125 premiums and employer 401(k)**  (2026-01-01 → open) [A.3, US-GAS5-006, direct artifact inspection, conf high]

## 4 — Payslip statute
No Georgia pay-statement content statute: 34-7-2 and the 164-page GDOL handbook read (full-text search); federal layer only; electronic delivery unrestricted; no language clause.


## 5 — Statutory reporting instruments
- `ga.report.wh.payer_status` = **lookback 12 months to prior 30 June: semi-weekly > 50,000 (EFT; G-7 Schedule B); monthly > 200/month (GA-V by 15th; G-7 quarterly); quarterly <= 200/month and > 800/yr; annual <= 800/yr by 31 Jan**  (2026-01-01 → open) [A.2, US-GAS5-002, direct artifact inspection, conf high] — One-day rule > 100,000 per payday; G-7 > 500 makes EFT/e-file mandatory (10% penalty); zero G-7 required; Q3 2026 due 2026-11-02, Q4 2027-02-01.
- `ga.report.wh.semiweekly_threshold` = **50000** USD (2026-01-01 → open) [A.2, US-GAS5-002, direct artifact inspection, conf high]
- `ga.report.annual.g1003` = **W-2s and 1099-NEC with GA withholding due 31 Jan (TY2026: 2027-02-01), other 1099s 28 Feb; e-file if federal e-file or EFT; GTC entry, G-1003 Excel/CSV or EFW2 + GA RS (Rev 01/18); 1099s via IRIS XML only; no CF/SF**  (2026-01-01 → open) [A.2, US-GAS5-003, direct artifact inspection, conf high]
- `ga.report.w2.rs_layout` = **Rev 01/18: 248-267 state employer account; 274-275 state code; 276-286 state wages; 287-297 state tax; 298-307 period end; 331-339 withholding number**  (2018-01-01 → open) [A.2, US-GAS5-011, direct artifact inspection, conf medium] — [partial row] TY2026 layout with GA OT field not yet posted (Q1).
- `ga.report.sui.dol4n` = **DOL-4N due 30 Apr, 31 Jul, 31 Oct, 31 Jan; electronic for 25+ employees (portal <=100, CSV/Excel 100-15,000, SFTP >15,000); domestic-only annual DOL-4 by 31 Jan; corrections DOL-3C; temporary substitute SSN 000-00-000n allowed (correct within 30 days)** (2026-01-01 -> open) [A.3, US-GAS5-005, direct artifact inspection, conf high]
- `ga.report.sui.efile_threshold_employees` = **25** employees (2026-01-01 → open) [A.3, US-GAS5-005, direct artifact inspection, conf medium] — Proposed all-employer mandate (300-2-2-.02(6)) adoption unconfirmed (Q3).
- `ga.newhire.report_days` = **10** days (2026-01-01 → open) [A.2, US-GAS5-012, second independent authority, conf high] — O.C.G.A. 19-11-9.2: FEIN (same as UI), employee name/address/SSN/DOB/start date, medical insurance availability, state of hire.

## 6 — Leave
Family Care Act 34-1-10 (25+ employees offering sick leave; 5 days for family) read only in committee-substitute text [US-GAS5-015 partial]; enacted version and sunset unconfirmed (Q4) - not a fact.

- `ga.leave.paid.mandate.exists` = **False**  (2026-01-01 → open) [A.3, US-GAS5-016, direct artifact inspection, conf high]

## 7 — Termination and final pay
No final-pay statute; vacation contractual. Severance withheld if resident at payment. Final G-7 within 30 days of ceasing employees.

- `ga.separation_notice.dol800` = **DOL-800 (R-02-24) to every separated worker stating reason, on last day or within 3 days; electronic with e-signature allowed (Oct 2026 rules)**  (2026-01-01 → open) [A.3, US-GAS5-007, direct artifact inspection, conf high]
- `ga.separation_notice.delivery_days` = **3** days (2026-01-01 → open) [A.3, US-GAS5-007, direct artifact inspection, conf high]
- `ga.mass_separation.threshold_workers` = **25** workers (2026-01-01 → open) [A.1, US-GAS5-020, direct artifact inspection, conf medium] — [partial row] DOL-402/402A within 48 hours when 25+ separated same day same reason for 7+ days; replaces individual DOL-800s.
- `ga.sales_rep.commission_due_days` = **30** days (2026-01-01 → open) [A.3, US-GAS5-007, direct artifact inspection, conf high]

## 8 — Benefits in kind / taxable wages
- `ga.pit.conformity` = **federal AGI start; IRC conformity as of 2026-01-01 (HB 1199); 401(k)/125/HSA/transit/GTL follow federal; no GA departure located**  (2026-01-01 → open) [A.2, US-GAS5-023, second independent authority, conf medium]

## 9 — Deductions and garnishments
- `ga.garn.creditor.max_percent` = **25** percent (2016-01-01 → open) [A.1, US-GAS5-014, direct artifact inspection, conf medium] — [partial row] [partial] 18-4-5: lesser of 25% of disposable earnings or excess over 217.00 (as printed); CCPA floor 30 x 7.25 = 217.50 binds [US-FED-011]: use 217.50. Support continuing garnishment max 50%. Garnishee expense greater of 50 or 10% capped 100.
- `ga.garn.child_support.setup_fee` = **25** USD (2026-01-01 → open) [A.2, US-GAS5-019, direct artifact inspection, conf high] — 3 per deduction; Family Support Registry.
- `ga.garn.child_support.per_deduction_fee` = **3** USD (2026-01-01 → open) [A.2, US-GAS5-019, direct artifact inspection, conf high]

## 10 — Collective agreements / prevailing wage
- `ga.prevailing_wage.state_law.exists` = False (2026-01-01 → open) [A.2, US-GAP51-002 — promoted to fact in Synthesis C] Davis-Bacon only; right-to-work state [US-GAS5-022].

## 11 — Indexation
Nothing CPI-indexed. HB 463 conditional step schedule: rate -0.125/yr from 2027 to 3.99%; std deduction +750/+375 to 36,000/18,000; dependent +125 to 6,000. If no trigger holds, 2027 = 4.865%, 30,750/15,375, 5,125 (derived projection - NOT facts until OPB 2026-12-01 and the 2027 DOR guide).


## 12 — Payroll data protection / records
Full SSN required on GDOL records. 10-1-393.8 (no public SSN display) only on a tier-B MANUAL row [US-GAS5-018].

- `ga.records.dor.retention_years` = **4** years (2026-01-01 → open) [A.2, US-GAS5-004, direct artifact inspection, conf high]
- `ga.records.gdol.retention_years` = **7** years (2026-01-01 → open) [A.3, US-GAS5-005, direct artifact inspection, conf high] — 34-8-121: full name, full SSN, hire/separation dates, separation reason, quarterly wages incl. non-cash and tips.

## 13 — Live legal change
- `ga.live.hb463.status` = **in force (signed 2026-05-11, retroactive 2026-01-01); levels withholding + assessment (rate), assessment + reporting (subtractions)**  (2026-01-01 → open) [A.1, US-GAS5-009, second independent authority, conf high]
- `ga.live.hb1157.status` = **introduced, NOT enacted (would repeal local-mandate pre-emption)**  (2026-01-01 → open) [A.1, US-GAS5-017, direct artifact inspection, conf high]
- `ga.live.gdol_rules_2026` = **proposed 2026-06-15, announced 2026-10-07: temporary substitute SSN, electronic separation notices, electronic posters, proposed all-employer DOL-4N e-file; adopted text/effective date not read** (2026-10-07 -> open) [A.2, US-GAS5-021, direct artifact inspection, conf medium]

## Oracle — worked examples (C37)
- `ga.oracle.guide.example1.withholding` = **27.03** USD (2026-01-01 → open) [A.2, US-GAS5-001, derived arithmetically, conf high] — MFJ, semimonthly 2,000, 1 dependent: (2,000 - 1,250 - 208.33) x 0.0499 = 27.029 -> 27.03. Table check: Single weekly band 276-294: (294 - 288.46) x 0.0499 = 0.28 as printed.

## Special populations (US-OWN-005)
- Domestic: GA withholding voluntary; UI at 1,000 cash/quarter, annual DOL-4 [US-GAS5-004, US-GAS5-006, US-GAS5-005].
- Agricultural: withholding not required; UI 10 in 20 weeks or 20,000/quarter [US-GAS5-004, US-GAS5-006].
- Minors: DOL-4103 work certificate under 18; DOL-4101 entertainment; newspaper carriers under 18 outside UI [US-GAS5-008, US-GAS5-006].
- Tipped: federal 2.13; tip subtraction at assessment; W-2 TP/TTOC; tips UI wages to FUTA extent [US-GAS5-016, US-GAS5-009, US-GAS5-003, US-GAS5-006].
- Clergy: ministers no GA withholding; church/religious order employees outside UI [US-GAS5-004, US-GAS5-006].
- Students: work-study and student nurses outside UI [US-GAS5-006].
- NRAs: withhold unless 8233 filed + copy to DOR [US-GAS5-004].
- Statutory employees: no state rule; SS-8 determinations accepted for UI [US-GAS5-006].
- Government: mostly reimbursing; elected officials/legislators/judiciary/National Guard outside UI [US-GAS5-006, US-GAS5-004].
- Military spouses: G-4 line 8b [US-GAS5-010]. Sole-proprietor family outside UI [US-GAS5-006]. RLA rail: GA OT field [US-GAS5-003].

## Language seams (US-OWN-006)
No language clause in 34-7-2 [US-GAP9L-001, US-GAP9L-003]; payslip English (US-OWN-006).

## QA round 1 corrections (2026-11-02)

One truth for the 2026 rate, split by level (C32): `ga.wh.rate` (withholding) 5.19% 2026-01-01..2026-05-10 [US-GA-001] and 4.99% from 2026-05-11 [US-GAS5-009]; `ga.pit.rate.flat` (assessment) 4.99% for the whole of taxable year 2026, retroactive (HB 463). The 2025 value 5.19% left the configuration facts (`_history` of the facts file). WTC `ga.sit.rate` is renamed `ga.wh.rate` with the same two periods. C29: "placeholder SSN" reworded "temporary substitute SSN" (meaning unchanged).

## Open questions
Mirrors `unresolved[]` in the facts file (same keys).

- `ga.report.w2.rs_layout.current` (blocking) — TY2026 RS record (GA OT field) and G-1003 2026 template not posted on 2026-11-02 (announced late October 2026). **Would close it:** DOR "2026 Federal Format Specifications" and G-1003 2026 template at https://dor.georgia.gov/federal-format-layout.
- `ga.sui.employer.rate.range` (non-blocking) — 2026 and 2027 experience rate min/max not on an A-tier source (tier-B 0.04-8.10%). **Would close it:** O.C.G.A. 34-8-155(c),(e) on an official host or GDOL publication of the rate schedules.
- `ga.report.sui.efile_all_employers` (non-blocking) — Adoption and effective date of proposed Rule 300-2-2-.02(6) (all-employer electronic DOL-4N) unconfirmed. **Would close it:** Adopted Rule 300-2-2-.02 on rules.sos.ga.gov or the GDOL rules page.
- `ga.leave.family_care.status` (non-blocking) — 34-1-10 read only in committee-substitute text; tier-B lead says repealed in 2023. **Would close it:** Enacted SB 201 (2017) and the 2020-2023 extension act on legis.ga.gov.
- `ga.garn.state_tax_levy` (non-blocking) — DOR wage-levy rules and enacted 18-4-5 (2016 Act, 2020 SB 443) not read. **Would close it:** Enacted acts on legis.ga.gov or the Governor signed-legislation PDFs.
- `ga.pit.rate.next_year` (blocking) — 2027 rate/standard deduction/dependent depend on OPB trigger determination due 2026-12-01; derived projection 4.865% / 30,750 / 15,375 / 5,125 is not a fact. **Would close it:** OPB determination of 2026-12-01 and the DOR 2027 Employer Withholding Tax Guide.
- `ga.data_protection.ssn_paystub` (non-blocking) — 10-1-393.8 read only via mirror (tier B). **Would close it:** Official-host read of 10-1-393.8 as amended and its 2006 enacting act.
- `ga.minwage.state.exemptions` — CLOSED (QA r2, 2026-11-06): 34-4-3(b)-(c) exemptions from the enacted act Ga. L. 2001, p. 201, Act 32 (SB 14), effective 2001-07-01 [A.1, US-GAV6C-001; Legislative Counsel summary US-GAV6C-002]. Currency: the 2025 Legislative Counsel draft SB 273 reprints the same existing text [US-GAV6C-003, non-binding] and GDOL states 5.15 under 34-4-3 in 2026 [US-GAS5-022]. The unenacted SB 24 (2021) source [US-GAV6B-002] is superseded and no longer cited.
- `ga.sui.admin_assessment.next_year` (non-blocking) — No 2026 act extending Article 6 beyond 2026-12-31 located. **Would close it:** GDOL 2027 rate release (December 2026) / DOL-626 notices.

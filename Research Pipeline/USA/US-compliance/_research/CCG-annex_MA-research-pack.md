# CCG annex_MA research pack — Massachusetts

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B, 2026-11-02. Source: `_research/stage5/MA.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_MA-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** Minimum wage 15.00 (not indexed; service rate 6.75; agricultural 8.00); weekly overtime. PIT 5.0% + 4% surtax above 1,107,750 (2026); M-4 exemptions; Circular M tables or percentage method (they differ by up to 0.02); supplemental 5% (9% above threshold); no reciprocity (credit method), no local tax. UI base 15,000, new 2.42%, Schedule E 0.94%-14.37% + COVID Recovery Assessment 0.178%-2.716%; EMAC 0.12/0.24/0.34%; WTF 0.056%; PFML 0.88% (25+) / 0.46% (<25) with the Chapter 101 family/medical swap applied from 2027-01-01 (decision recorded). Pay slip c.149 s.148. Discharge: pay same day.

## 1 — Employment / labour code
Pay weekly or biweekly within 6 days of period end (7 if 7-day week); casual within 7 days [legacy US-MAP51-008]. Payment method/e-stub consent not located (Q1). No local MW located (commissioner power under c.151 s.7 unused).

- `ma.minwage.hourly` = **15.0** USD (2023-01-01 → open) [A.1, US-MAS5-001, direct artifact inspection, conf high] — Never less than federal + 0.50; not indexed; no 2027 rate enacted [US-MAS5-017].
- `ma.minwage.service_rate` = **6.75** USD (2023-01-01 → open) [A.1, US-MAS5-003, direct artifact inspection, conf high] — Tipped cash wage; max tip credit 15.00 - 6.75 = 8.25 (derived); top-up per shift.
- `ma.minwage.tip_credit.max` = **8.25** USD (2023-01-01 → open) [A.1, US-MAS5-003, derived arithmetically, conf high] — 15.00 - 6.75.
- `ma.minwage.agricultural` = **8.0** USD (2026-01-01 → open) [A.1, US-MAS5-004, direct artifact inspection, conf high] — Not children 17 or under or immediate family; agriculture exempt from state OT [US-MAS5-002].
- `ma.overtime.weekly_threshold_hours` = **40** hours (2026-01-01 → open) [A.1, US-MAS5-002, direct artifact inspection, conf high] — 1.5x; no daily OT; commissions/bonuses/incentives excluded from regular rate.

## 2 — Income tax (state withholding)
- `ma.wh.supplemental.rule` = 5% while annualized regular + supplemental to date + this payment <= 1,107,750; above, lesser of 9% of payment or 9% of excess plus 5% of remainder; percentage method excludes supplemental (2026-01-01 → open) [A.2, US-MAP51-003 — promoted to fact in Synthesis C] Circular M 2026.
- `ma.pit.rate` = **5.0** percent (2026-01-01 → open) [A.2, US-MAB5-402, quoted from authority page, conf high] — Plus 4% surtax above 1,107,750 (2026); withholding at combined 9% above threshold. IP 25-18 (4.67% 2027) excluded from ballot per tier-B (SJC-13885) - do not model.
- `ma.pit.surtax.rate` = **4.0** percent (2026-01-01 → open) [A.2, US-MAB5-402, quoted from authority page, conf high]
- `ma.pit.surtax.threshold` = **1107750** USD (2026-01-01 → 2026-12-31) [A.2, US-MAB5-402, quoted from authority page, conf high] — Indexed (CPI mechanism not re-read); published in Circular M.
- `ma.wh.method` = **Circular M wage-bracket tables or percentage method: wages - FICA/Medicare/retirement (max 2,000/yr) - exemption amount for period; x 5%; - HoH / blind reduction**  (2026-01-01 → open) [A.2, US-MAS5-013, quoted from authority page, conf high] — Methods not numerically identical (table vs percentage differ up to 0.02 weekly); engine must use one method consistently [US-MAS5-024].
- `ma.wh.exemption.weekly` = **19n + 66**  (2026-01-01 → open) [A.2, US-MAS5-013, quoted from authority page, conf high] — Daily 3n+9; biweekly 38n+131; semimonthly 42n+141; monthly 83n+284; annual 1,000n+3,400 (n = exemptions).
- `ma.wh.exemption.annual` = **1,000n + 3,400**  (2026-01-01 → open) [A.2, US-MAS5-013, quoted from authority page, conf high]
- `ma.wh.fica_retirement_deduction.annual_max` = **2000** USD (2026-01-01 → open) [A.2, US-MAS5-013, quoted from authority page, conf high]
- `ma.wh.hoh_reduction.weekly` = **2.31** USD (2026-01-01 → open) [A.2, US-MAS5-013, quoted from authority page, conf high] — Biweekly 4.62, semimonthly 5.00, monthly 10.00, daily 0.33.
- `ma.wh.blind_reduction.weekly` = **2.12** USD (2026-01-01 → open) [A.2, US-MAS5-013, quoted from authority page, conf high] — Per person; biweekly 4.23, semimonthly 4.58, monthly 9.17, daily 0.30.
- `ma.wh.certificate` = **M-4: line 1 personal (1, or 2 if 65+), line 2 spouse (4, or 5 if 65+), line 3 dependents, line 5 additional; boxes A HoH, B blind, C spouse blind, D full-time student <= 8,000 (no withholding); none filed = zero exemptions; new M-4 within 10 days on decrease; exemptions only with principal employer**  (2026-01-01 → open) [A.2, US-MAS5-014, direct artifact inspection, conf high] — Edition date not printed in extracted text.
- `ma.wh.student_box_d.income_max` = **8000** USD (2026-01-01 → open) [A.2, US-MAS5-014, direct artifact inspection, conf high]
- `ma.wh.supplemental.rate` = **5** percent (2026-01-01 → open) [A.2, US-MAP51-003 (Circular M 2026 p.13 section G: "If the result of step 4 is $1,107,750 or less, withhold 5%"), quoted from authority page, conf medium] — Circular M [US-MAP51-003 legacy]: 5% while cumulative <= 1,107,750; above, lesser of 9% of payment or 9% of excess + 5% of remainder.
- `ma.wh.rounding` = **wages may be computed to nearest dollar (830 CMR 62B.2.1(8))**  (2026-06-05 → open) [A.1, US-MAS5-023, direct artifact inspection, conf high]

## 2b — Non-resident regime and reciprocity
- `ma.nonres.rules` = **residents on all wages; nonresidents on MA-performed services; nonresident not working in MA not withheld even if paid from MA office; courtesy withholding for residents by out-of-state employers; no reciprocity - credit method: MA amount minus other jurisdiction amount (830 CMR 62B.2.1(9)(b))**  (2026-01-01 → open) [A.2, US-MAS5-013, quoted from authority page, conf high] — No MA withholding where no federal duty (household); MSRRA M-4-MS: do not withhold [US-MAS5-024].

## 2c — Local wage taxes
- `ma.local_wage_tax.exists` = **False**  (2026-01-01 → open) [A.2, US-MAB5-402, quoted from authority page, conf high] — No local wage/payroll/income tax [US-MAR3-001, US-MAR3-003].

## 3 — Social insurance (SUI / SDI / PFML / levies)
No SDI/TDI; PFML the only employee-funded program [US-MAP9W-004]. PFML benefits paid by DFML (optional 5%/10% withholding), not payroll.

- `ma.sui.new_employer.rate` = **2.42** percent (2026-01-01 → 2026-12-31) [A.2, US-MAS5-022, quoted from authority page, conf high] — Under 3 years; construction 6.08%; base 15,000 fixed (c.151A s.14, legacy US-MAP51-005); no employee UI.
- `ma.sui.new_employer.construction.rate` = **6.08** percent (2026-01-01 → 2026-12-31) [A.2, US-MAS5-022, quoted from authority page, conf high]
- `ma.sui.employer.rate.min` = **0.94** percent (2026-01-01 → 2026-12-31) [A.2, US-MAS5-020, direct artifact inspection, conf high] — Schedule E; COVID Recovery Assessment 0.178%-2.716% on same base; effective 1.118%-17.086% (UI + COVID = effective in every band, Python).
- `ma.sui.employer.rate.max` = **14.37** percent (2026-01-01 → 2026-12-31) [A.2, US-MAS5-020, direct artifact inspection, conf high]
- `ma.sui.covid_recovery.rate.min` = **0.178** percent (2026-01-01 → 2026-12-31) [A.2, US-MAS5-020, direct artifact inspection, conf high]
- `ma.sui.covid_recovery.rate.max` = **2.716** percent (2026-01-01 → 2026-12-31) [A.2, US-MAS5-020, direct artifact inspection, conf high]
- `ma.sui.wage_base` = **15000** USD (2026-01-01 → open) [A.2, US-MAS5-020, direct artifact inspection, conf high] — Fixed by statute, not indexed.
- `ma.sui.coverage` = **1 employee 13 weeks or 1,500/quarter; agricultural 40,000/quarter or 10 for 20 weeks; domestic 1,000 cash/quarter; out-of-state employers 200 MA wages/quarter; notices by Jan 31; review requests before Jun 20; 12% late interest**  (2026-01-01 → open) [A.2, US-MAS5-022, quoted from authority page, conf high]
- `ma.emac.rate.year4` = **0.12** percent (2026-01-01 → open) [A.2, US-MAS5-021, quoted from authority page, conf high] — EMAC on 15,000 base: years 1-3 exempt; year 4 0.12%; year 5 0.24%; year 6+ 0.34%; fewer than 6 employees in a quarter exempt.
- `ma.emac.rate.year5` = **0.24** percent (2026-01-01 → open) [A.2, US-MAS5-021, quoted from authority page, conf high]
- `ma.emac.rate.year6_plus` = **0.34** percent (2026-01-01 → open) [A.2, US-MAS5-021, quoted from authority page, conf high]
- `ma.wtf.rate` = **0.056** percent (2026-01-01 → open) [A.2, US-MAB5-401, quoted from authority page, conf medium] — c.151A s.14L; 2026 DUA value not confirmed (commissioner may adjust).
- `ma.pfml.rate.total.25_plus` = **0.88** percent (2026-01-01 → open) [A.2, US-MAS5-012, quoted from authority page, conf high] — Unchanged total in 2027. Cap: SS wage base (c.175M s.6(f)) [US-MAS5-010].
- `ma.pfml.rate.total.under_25` = **0.46** percent (2026-01-01 → open) [A.2, US-MAS5-012, quoted from authority page, conf high] — No employer share.
- `ma.pfml.family.rate` = **0.18** percent (2026-01-01 → 2026-12-31) [A.2, US-MAS5-012, quoted from authority page, conf high] — Up to 100% from employee.
- `ma.pfml.medical.rate` = **0.7** percent (2026-01-01 → 2026-12-31) [A.2, US-MAS5-012, quoted from authority page, conf high] — Employee up to 40% (0.28%), employer 0.42% (25+).
- `ma.pfml.family.rate` = **0.7** percent (2027-01-01 → open) [A.2, US-MAS5-012, quoted from authority page, conf high] — Chapter 101 swap: employee up to 40% (0.28%), employer 0.42%.
- `ma.pfml.medical.rate` = **0.18** percent (2027-01-01 → open) [A.2, US-MAS5-012, quoted from authority page, conf high] — Up to 100% from employee.
- `ma.pfml.employee.max_total.25_plus` = **0.46** percent (2026-01-01 → open) [A.2, US-MAS5-012, derived arithmetically, conf high] — 2026: 0.18 + 0.28; 2027: 0.28 + 0.18 - the employee and employer totals (0.46 / 0.42) are identical either side of the swap; only the family/medical labelling (benefit tax treatment) changes.
- `ma.pfml.split.decision` = **Chapter 101 ss.25-26 family/medical deduction-cap swap applied from 2027-01-01 per DFML; 2026 payroll uses the DFML 2026 table**  (2026-01-01 → open) [A.2, US-MAS5-012, quoted from authority page, conf medium] — DECISION (brief trap): s.45 of Ch. 101 [US-MAS5-026] says ss.25-26 apply "for taxable years beginning on or after January 1, 2026"; DFML, the administering authority, implements from 2027-01-01 [US-MAS5-012]. Decided for DFML: (1) "taxable years" is income-tax language and the swap was made to address the IRS tax treatment of benefits, an assessment-level matter; (2) the contribution totals withheld (0.46% employee / 0.42% employer) are identical under both readings, so no 2026 payroll amount changes; (3) DFML has issued no 2026 re-split or catch-up instruction. Re-open only if DFML/DOR (458 CMR 2.00) issues a transition notice.
- `ma.pfml.benefit.weekly_max` = **1230.39** USD (2026-01-01 → 2026-12-31) [A.2, US-MAS5-025, derived arithmetically, conf high] — 64% x SAWW 1,922.48; benefit side, paid by DFML (not payroll).
- `ma.pfml.benefit.weekly_max` = **1284.61** USD (2027-01-01 → open) [A.2, US-MAS5-025, derived arithmetically, conf high] — 64% x 2,007.20.

## 4 — Payslip statute
- `ma.payslip.items` = **employer name, employee name, date (day/month/year), hours worked, hourly rate, deductions or increases for the period (c.149 s.148)**  (2026-01-01 → open) [A.1, US-MAS5-005, direct artifact inspection, conf medium] — Statute row is legacy US-MAP51-008; e-delivery consent not located.

## 5 — Statutory reporting instruments
Registration MassTaxConnect (DOR, PFML) and DUA portal. PFML quarterly return mechanics unread (Q8).

- `ma.report.wh.frequency` = **<= 100/yr annual (Jan 31); 101-1,200 quarterly; 1,201-25,000 monthly by 15th (quarter-end months on last day of following month); > 25,000 quarterly return + payment within 3 business days when >= 500 accumulated by 7th/15th/22nd/last; e-file mandatory for new registrations, payroll providers, combined liability >= 5,000**  (2026-01-01 → open) [A.2, US-MAS5-013, quoted from authority page, conf high]
- `ma.report.w2` = **due Jan 31; 50+ W-2s electronic via MassTaxConnect/Bulk File Portal; <= 49 paper with M-3; corrections paper W-2c; EFW2 RA/RE/RS/RT, RS MA wages 276-286, MA tax 287-297, RT = sum RS**  (2026-01-30 → open) [A.2, US-MAS5-015, quoted from authority page, conf high] — Format [US-MAS5-019] handbook Rev. 20191219. Guide (Aug 2026) says last day of March / Feb 28 - conflict (Q4); use Jan 31.
- `ma.report.w2.efile_threshold` = **50** forms (2026-01-30 → open) [A.2, US-MAS5-015, quoted from authority page, conf high]
- `ma.report.sui.quarterly` = **DUA wage detail by 3 p.m. Apr 30 / Jul 31 / Oct 31 / Jan 31; CSV, EFW2 or ICESA; EAN, SSN, name, hours, gross, wages subject to withholding, state tax withheld, work location, 12th-of-month, adjustment reason; wages when paid**  (2026-01-01 → open) [A.2, US-MAS5-018, quoted from authority page, conf high]
- `ma.newhire.report_days` = **14** days (2026-01-01 → open) [A.2, US-MAS5-016, quoted from authority page, conf high] — Employees and contractors 600+; rehires after 30+ days; SSN only (no ITIN); 25+ employees online.

## 6 — Leave
PFML benefit: 7-day wait; 80% of AWW to 50% SAWW + 50% above; caps 20/12/26 weeks. Parental, small necessities, DV, jury leave not read.

- `ma.leave.sick.employer_threshold_paid` = **11** employees (2026-01-01 → open) [A.1, US-MAS5-006, direct artifact inspection, conf high] — c.149 s.148C: 1 h per 30 h; use from day 90; 40 h/yr paid (11+) or unpaid; carryover 40; no payout; certification after 24 consecutive scheduled hours.
- `ma.leave.sick.cap_hours` = **40** hours (2026-01-01 → open) [A.1, US-MAS5-006, direct artifact inspection, conf high]
- `ma.leave.sick.payout_on_separation` = **False**  (2026-01-01 → open) [A.1, US-MAS5-006, direct artifact inspection, conf high]

## 7 — Termination and final pay
Sick time no payout. UI separation notice instrument not located (Q10).

- `ma.final_pay.rule` = discharge: in full on the day of discharge; resignation: next regular payday (or following Saturday); agreed vacation/holiday pay are wages payable at termination (c.149 s.148) (2026-01-01 → open) [A.1, US-MAP51-008 — promoted to fact in Synthesis C]

## 8 — Benefits in kind / taxable wages
- `ma.pit.irc_decoupling` = **c.62C s.90 (Ch. 101 s.13, from TY2026): same-year IRC amendments do not affect MA gross income; accountable-plan reimbursements not wages**  (2026-01-01 → open) [A.1, US-MAS5-026, direct artifact inspection, conf high] — Level assessment flowing into withholding definition.

## 9 — Deductions and garnishments
- `ma.garn.creditor.exempt_rule` = **greater of 85% of gross wages or 50 x higher of federal/MA MW per week; support orders: CCPA (c.246 s.28)**  (2026-01-01 → open) [A.1, US-MAS5-009, direct artifact inspection, conf high]
- `ma.garn.creditor.weekly_exempt_floor` = **750** USD (2023-01-01 → open) [A.1, US-MAS5-009, derived arithmetically, conf high] — 50 x 15.00.

## 10 — Collective agreements / prevailing wage
- `ma.prevailing_wage.rule` = wages at least the commissioner rate on public works (c.149 s.26) (2026-01-01 → open) [A.1, US-MAP51-009 — promoted to fact in Synthesis C]
- `ma.prevailing_wage.certified_payroll` = **weekly certified payroll with signed statement to awarding authority; apprentice ID copies; records 3 years after contract; compliance statement within 15 days of completion; no dollar threshold (s.27B)**  (2026-01-01 → open) [A.1, US-MAS5-007, direct artifact inspection, conf high]

## 11 — Indexation
MW and UI base not indexed; UI/COVID and PFML rates yearly; PFML cap = SS base; PFML max benefit 64% SAWW; surtax threshold indexed; M-4 factors static.


## 12 — Payroll data protection / records
No SSN-on-slip rule located; c.93H / 201 CMR 17.00 not read.

- `ma.records.retention_years` = **3** years (2026-01-01 → open) [A.1, US-MAS5-005, direct artifact inspection, conf high] — c.151 s.15; employees may inspect; DOR withholding records 3 years.

## 13 — Live legal change
- `ma.live.chapter_101_2026` = **enacted (emergency, approved 2026-06-12): PFML split swap (applied 2027-01-01, see decision), IRC same-year decoupling, P.L. 119-21 s.70302(f) deduction (subject unchecked)**  (2026-06-12 → open) [A.1, US-MAS5-026, direct artifact inspection, conf high]

## Special populations (US-OWN-005)
- Domestic: MW/OT apply (incl. au pairs); written agreement for 16+ h/week; meal deductions max 1.50/2.25; lodging max 35/30/25 per week; UI 1,000 cash/quarter; paystub records 3 years [US-MAS5-028, US-MAS5-022].
- Agricultural: MW 8.00 (not family/under 18); OT-exempt; UI 40,000/quarter or 10 for 20 weeks [US-MAS5-004, US-MAS5-002, US-MAS5-022].
- Minors: MW applies; UI-exempt working for a parent; permits/hours not read [US-MAS5-001, US-MAS5-022].
- Tipped: service rate 6.75; tips 20+/month reported by 10th are withheld on [US-MAS5-003, US-MAS5-013].
- Clergy: religious order members excluded from MW; some religious work UI-exempt; religious organisations still withhold [US-MAS5-017, US-MAS5-022, US-MAS5-013].
- Students: M-4 box D (<= 8,000) no withholding; nonprofit/public work-training UI-exempt [US-MAS5-014, US-MAS5-024, US-MAS5-022].
- NRAs: follow federal duty [US-MAS5-013]. MSRRA: M-4-MS no withholding [US-MAS5-024]. Statutory employees: no state rule.
- Government: must withhold and report new hires; municipal employees excluded from c.151 MW; earned sick time only on local acceptance [US-MAS5-013].
- Interstate carriers: residents and nonresidents with all duties in MA [US-MAS5-013]. Family employment UI-exempt [US-MAS5-022].

## Language seams (US-OWN-006)
Earned sick time notice languages c.149 s.148C(o) [US-MAL-002]; payslip English (US-OWN-006).

## Synthesis D additions (2026-11-02)

Source: browser-pass rows S5B-P1 / S5B-P2 merged into `legal-basis-register.csv` and SSA EFW2 TY2026 (US-FEDS5-032) read locally. Every claim below carries its register_id; the facts file is authoritative. Full log: `_research/synthesis-D/SYNTHESIS-D.md`.

Facts added:
- `ma.sui.rate_schedule.selection` = **Schedule A-G by Unemployment Compensation Fund reserve %: A >= 1.65; B 1.5-<1.65; C 1.2-<1.5; D 0.9-<1.2; E 0.6-<0.9; F 0.3-<0.6; G < 0.3** (2015-01-01 → open) [A.2, US-MAB5-001, direct artifact inspection, conf high]
- `ma.sui.rate_schedule.table` = **45 account-reserve rows x 7 schedules (positive reserve 17.0+ : A 0.56 / B 0.64 / C 0.73 / D 0.83 / E 0.94 / F 1.07 / G 1.21 ... negative reserve 23+ : 8.62 / 9.79 / 11.13 / 12.65 / 14.37 / 16.33 / 18.55); full transcription in the local file of US-MAB5-001** (2015-01-01 → open) [A.2, US-MAB5-001, direct artifact inspection, conf high]
- `ma.sui.rate_schedule.in_force` = **E** (2026-01-01 → 2026-12-31) [A.2, US-MAB5-001, derived arithmetically, conf high] — G-DERIVE: the 2026 published minimum 0.94% and maximum 14.37% (ma.sui.employer.rate.min/max, US-MAS5-020) coincide only with column E of the schedule table (min row: A 0.56, B 0.64, C 0.73, D 0.83, E 0.94, F 1.07, G 1.21; max row: 8.62, 9.79, 11.13, 12.65, 14.37, 16.33, 18.55).

## QA r1b additions (2026-11-02)

Source: browser pass P3 (`_research/stage5/browser-pass-P3.md`, shard `S5B-P3.csv` merged into the register). Facts file is authoritative; every line below is a fact object with the same key.

**5 - Statutory reporting: W-2 due date (narrows RQ-255; now non-blocking).** 830 CMR 62B.2.1(d) [A.1, US-MAB5-301]: employee statement by January 31 (or 30 days after the last payment), no DOR filing deadline in the regulation. DOR Directive 07-2 (2007) [A.3, US-MAB5-302] is the origin of "Feb 28 paper / Mar 31 electronic", which the Aug 2026 Withholding Tax Guide still echoes; the DOR W-2 page updated 2026-01-30 says January 31 [US-MAS5-015]. Filing by January 31 satisfies every candidate deadline, so `ma.report.w2` (January 31) stands and the conflict no longer blocks the build.

- `ma.report.w2.employee_statement.due` = **Furnish the wage statement to each employee on or before January 31 of the following year, or within 30 days of the last payment if employment ends earlier.** (2026-01-01 -> open) [A.1, US-MAB5-301, quoted from authority page, conf high] LEVEL: employer reporting. 830 CMR 62B.2.1(d) (mass.gov, verbatim Chrome excerpt). The regulation sets no deadline for filing W-2 copies with DOR.

## Open questions

Mirrors `unresolved[]` in the facts file (same keys, same wording). Regenerated by QA r1b on 2026-11-02.

- `ma.payment.method_and_estub_consent` (non-blocking) — Direct deposit, paycard and electronic pay-stub consent rules not located. **Would close it:** AG Fair Labor Division wage-payment advisory or 454 CMR 27.00.
- `ma.wh.certificate.edition` (non-blocking) — M-4 revision date not printed in extracted text. **Would close it:** Form footer or DOR withholding forms list.
- `ma.report.w2.handbook_edition` (non-blocking) — W-2 e-file handbook served is Rev. 20191219 though reissued yearly. **Would close it:** TY2026 edition from DOR bulk-file support.
- `ma.report.w2.due_date_conflict` (non-blocking) — The Feb 28 (paper) / Mar 31 (electronic) dates come from DOR Directive 07-2 (2007, US-MAB5-302), which the Aug 2026 Withholding Tax Guide still echoes. The newer DOR W-2 page (updated 2026-01-30, US-MAS5-015) says January 31, and 830 CMR 62B.2.1(d) fixes January 31 for the employee statement (US-MAB5-301). No TIR or Directive formally replacing 07-2 was found. Filing by January 31 meets every candidate deadline, so the build can configure January 31 without risk. **Would close it:** A DOR TIR/Directive superseding Directive 07-2, or a DOR confirmation that January 31 applies to W-2 filing with DOR.
- `ma.report.quarterly_wage_report.single` (non-blocking) — Whether the DUA wage detail report is the only quarterly wage report (DOR guide mentions DOR reports). **Would close it:** DOR "File quarterly wage reports" page.
- `ma.sui.wtf.current` (non-blocking) — 2026 Workforce Training Fund rate as published by DUA not read. **Would close it:** DUA WTF page or 430 CMR 14.00.
- `ma.report.pfml.quarterly` (non-blocking) — PFML quarterly return mechanics not read. **Would close it:** DFML page "Wage contributions & reporting for PFML".
- `ma.pit.conformity.items` (blocking) — 401(k)/403(b), 125, HSA, transit, GTL treatment not read in a DOR source. **Would close it:** DOR fringe-benefit tax treatment guidance or TIRs.
- `ma.garn.iwo_and_deductions` (non-blocking) — c.149 s.150 deduction authorisation and MA IWO fees/priority not read. **Would close it:** c.149 s.150 text and DOR Child Support Services employer page.
- `ma.pfml.split.transition_notice` (non-blocking) — Ch. 101 s.45 vs DFML effective date (decided for DFML 2027-01-01; totals unaffected). **Would close it:** DFML/DOR notice or 458 CMR 2.00 transition rule.
- `ma.pit.chapter101_s8_deduction` (non-blocking) — Subject of the P.L. 119-21 s.70302(f) deduction and any withholding effect unchecked. **Would close it:** DOR TIR implementing Chapter 101.
- `ma.live.bulletin_sweep` (non-blocking) — 2026 DOR TIRs/Directives and DUA/DFML news not swept. **Would close it:** DOR TIR index 2026 and DFML/DUA news pages.
- `ma.live.ip_25_18` (non-blocking) — IP 25-18 exclusion rests on tier-B (US-MAS5-027 MANUAL); SJC opinion URL 404. **Would close it:** SJC-13885 opinion on mass.gov/sjc or the Secretary of the Commonwealth 2026 ballot list.
- `ma.other_leave_and_minors` (non-blocking) — c.149 ss.52D, 52E, 105D, jury c.234A s.48 and child labour ss.60-66 not read. **Would close it:** Statute texts on malegislature.gov.
- `ma.termination.ui_separation_notice` (non-blocking) — DUA separation notice form/rule not located (430 CMR 5.00 index only). **Would close it:** 430 CMR 4.00/5.00 PDF text or DUA employer guide.

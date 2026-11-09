# CCG annex_ID research pack — Idaho

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B, 2026-11-02. Source: `_research/stage5/ID.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_ID-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** Minimum wage 7.25 tracking federal; tipped cash 3.35; opportunity wage 4.25; local minimum wages barred; FLSA overtime. Flat 5.3% PIT; withholding tables changed MID-YEAR: zero bracket 15,000/30,000 to 2026-07-22, 16,100/32,200 from 2026-07-23 (prospective, no catch-up); allowance value 0; percentage method rounds to whole dollar; supplemental flat 5.3%; nonresident threshold 1,000; no reciprocity, no local tax. SUI base 58,300, new 1.000%. Only a deductions statement is mandated. Final pay earlier of next payday or 10 days. Oracle: STC examples 31 / 20.

## 1 — Employment / labour code
Exclusions (44-1504) [US-IDS5-003]: EAP/outside sales; domestic; nonprofit camp seasonal; under-16 part-time <= 4 h/day; under-18 family; agricultural cases. Government employers outside state MW law (FLSA only). Overtime: no state rule (ch. 44-15 index; IDOL guide) [US-IDS5-025]. Hire notice of rate/payday on request; reduction notice before work (45-610) [US-IDS5-006].

- `id.minwage.hourly` = **7.25** USD (2009-07-24 → open) [A.1, US-IDS5-001, direct artifact inspection, conf high] — 44-1502(1): conforms to and tracks the federal minimum; not indexed; H0813 (2026) filed only [US-IDS5-024].
- `id.minwage.tipped.cash_wage` = **3.35** USD (2026-01-01 → open) [A.1, US-IDS5-001, direct artifact inspection, conf high] — Tip credit up to 3.90; employer makes up shortfall; tipped = > 30/month tips [US-IDS5-002].
- `id.minwage.opportunity_wage` = **4.25** USD (2026-01-01 → open) [A.1, US-IDS5-001, direct artifact inspection, conf high] — Under 20, first 90 consecutive calendar days (44-1502(3)).
- `id.local_minwage.preempted` = **True**  (2026-01-01 → open) [A.1, US-IDS5-001, direct artifact inspection, conf high] — 44-1502(4); H0812 (2026) not enacted.
- `id.pay_frequency.rule` = **at least once per calendar month on designated paydays; period ends <= 15 days before payday; nonworkday payday moves earlier; pattern of late pay up to 500 per period (45-608)**  (2026-01-01 → open) [A.1, US-IDS5-004, direct artifact inspection, conf high]
- `id.payment.method` = **lawful money or checks cashable without charge; direct deposit only with voluntary authorisation to account of choice, revocable (45-608); paycards not addressed**  (2026-01-01 → open) [A.1, US-IDS5-004, direct artifact inspection, conf high]

## 2 — Income tax (state withholding)
- `id.pit.rate.flat` = **5.3** percent (2025-01-01 → open) [A.1, US-IDS5-007, direct artifact inspection, conf high] — 63-3024 (2025 ch. 13, H 40); applies above CPI-indexed 2,500/5,000; no 2026 amendment; H0589/H0782/H0605 not enacted.
- `id.wh.method` = **percentage computation (rounded to nearest whole dollar), annualized wage, or wage bracket (EPB00745); allowance value 0 (Idaho CTC sunset)**  (2026-01-01 → open) [A.2, US-IDS5-008, direct artifact inspection, conf high] — Tables apply prospectively, no retro catch-up.
- `id.wh.rounding` = **nearest whole dollar**  (2026-01-01 → open) [A.2, US-IDS5-008, direct artifact inspection, conf high]
- `id.wh.zero_bracket.single.annual` = **16100** USD (2026-07-23 → open) [A.2, US-IDS5-011, derived arithmetically, conf high] — EPB00744 ed. 07-23-2026; per-period = annual / 12/24/26/52/260 rounded to dollar: monthly 1,342, semimonthly 671, biweekly 619, weekly 310, daily 62 (Python). Equals 2026 federal standard deduction (observation) [US-FEDS5-010].
- `id.wh.zero_bracket.married.annual` = **32200** USD (2026-07-23 → open) [A.2, US-IDS5-011, derived arithmetically, conf high] — Per-period married 2,683 / 1,342 / 1,238 / 619 / 124.
- `id.wh.zero_bracket.single.biweekly` = **619** USD (2026-07-23 → open) [A.2, US-IDS5-011, derived arithmetically, conf high] — Derivation recorded in register row US-IDS5-011: Tax = 5.3% of wages (after ICTCAT allowances, value 0) over threshold. Single/HoH: annual 16,100; monthly 1,342; semimonthly 671; biweekly 619; weekly 310; daily/misc 62. Married: annual 32,200; monthly 2,683; semimonthly 1,342; biweekly 1,238; weekly 619; daily 124. Each period threshold = annual /
- `id.wh.allowance.value` = **0** USD (2026-01-01 → open) [A.2, US-IDS5-008, direct artifact inspection, conf medium] — Child Tax Credit sunset (63-3029L); S1450 (2026) not enacted.
- `id.wh.supplemental.rate` = **5.3** percent (2026-01-01 → open) [A.2, US-IDS5-008, direct artifact inspection, conf high] — Aggregate or flat 5.3% on separately issued payment.
- `id.wh.certificate` = **federal W-4 required; Form ID W-4 (EFO00307) strongly encouraged: A Single/HoH, B Married, C Married at single rate; allowances = children 16 or under (+2 HoH)**  (2025-04-28 → open) [A.2, US-IDS5-013, direct artifact inspection, conf medium] — [partial row] Partial row: 2025 edition; 2026 edition not captured (ID-OQ-1).

## 2b — Non-resident regime and reciprocity
No reciprocity [US-IDB5-401 legacy]; no local wage tax [US-IDP52-003 legacy]. Interstate carrier staff withheld for state of residence; enrolled tribal members on reservation not withheld.

- `id.nonres.withholding_threshold` = **1000** USD (2026-01-01 → open) [A.2, US-IDS5-020, direct artifact inspection, conf high] — Withhold once nonresident earns > 1,000 in Idaho in the calendar year; all Idaho wages on W-2; residents working elsewhere: Idaho withholding optional; out-of-state employers withhold for employees physically in Idaho.

## 3 — Social insurance (SUI / SDI / PFML / levies)
- `id.sui.new_employer.rate` = 1.0 (2026-01-01 → 2026-12-31) [A.2, US-IDP52-004 — promoted to fact in Synthesis C] 0.970% UI + 0.000% admin + 0.030% workforce development; standard rate >= 6 quarters [US-IDS5-021].
- `id.sui.employer.rate.range` = positive classes 0.208%-0.694%; deficit classes 1.250%-5.400% (2026-01-01 → 2026-12-31) [A.2, US-IDP52-004 — promoted to fact in Synthesis C]
- `id.sui.wage_base` = **58300** USD (2026-01-01 → 2026-12-31) [A.2, US-IDB5-402, quoted from authority page, conf medium] — 72-1350: AAW of penultimate year rounded to 100 or FUTA if higher [US-IDS5-014]; not re-derived (2024 AAW not obtained); figure rests on the 2026 rate array (legacy US-IDP52-004).
- `id.sui.workforce_development.rate` = **0.03** percent (2026-01-01 → 2026-12-31) [A.2, US-IDB5-402, quoted from authority page, conf high] — Inside the UI rate; no other levy.
- `id.sui.coverage` = **general 1,500/quarter or 20 weeks; agricultural 20,000 cash/quarter or 10 workers on 20 days (H-2A counted, not taxed); domestic 1,000 cash/quarter; government and nonprofits covered; LLC-as-corporation members = officers; officer opt-out before March 31**  (2026-01-01 → open) [A.1, US-IDS5-022, direct artifact inspection, conf high]
- `id.pfml.exists` = **False**  (2026-01-01 → open) [A.1, US-IDS5-018, direct artifact inspection, conf high] — 2022 H0447 died in committee [US-KYR3-003].

## 4 — Payslip statute
- `id.payslip.required_content` = **written statement of deductions for each pay period in which deductions are made (45-609(2)); no full itemised statute**  (2026-01-01 → open) [A.3, US-IDS5-025, direct artifact inspection, conf medium]

## 5 — Statutory reporting instruments
- `id.report.wh.form910` = **Form 910 in TAP: semimonthly if >= 25,000/month or >= 300,000/12 months (20th / 5th); monthly < 25,000 and > 750/quarter (20th); quarterly <= 750/quarter; annual < 750/yr (last day of Jan); zero return required; cycle fixed for the year (changes by Nov 15)**  (2026-01-01 → open) [A.2, US-IDS5-009, direct artifact inspection, conf high]
- `id.report.annual.form967` = **Form 967 + W-2s due last day of January (1099s with ID withholding last day of February); EFW2 + Idaho state records via TAP (valid EFW2 generates 967); penalty 2/month per missing W-2 min 10 max 2,000; amounts to nearest dollar**  (2026-01-01 → open) [A.2, US-IDS5-010, direct artifact inspection, conf high]
- `id.report.sui.tx20` = **TX20 + TX26 (TX20C amendments) due last day of month after quarter (72-1311), no grace; online Employer Portal mandatory; zero reports required**  (2026-01-01 → open) [A.3, US-IDS5-021, direct artifact inspection, conf high]
- `id.newhire.report_days` = **20** days (2026-01-01 → open) [A.1, US-IDS5-015, direct artifact inspection, conf high] — 72-1604: employee name/address/SSN; employer name/address/FEIN; Idaho UI account; hire date; multistate flag.

## 6 — Leave
- `id.leave.paid_mandate.exists` = **False**  (2026-01-01 → open) [A.3, US-IDS5-025, direct artifact inspection, conf high] — H0641 (2026) sick leave FAILED [US-IDS5-024]; no PFML.

## 7 — Termination and final pay
- `id.final_pay.rule` = **earlier of next regular payday or 10 days excluding weekends/holidays; within 48 hours on written request; piece/commission: MW for last period then balance next payday (45-606)**  (2026-01-01 → open) [A.1, US-IDS5-005, direct artifact inspection, conf high] — No vacation-payout statute (agreement); no discharge notice or separation notice required.
- `id.final_pay.max_days` = **10** days (2026-01-01 → open) [A.1, US-IDS5-005, direct artifact inspection, conf high]

## 8 — Benefits in kind / taxable wages
- `id.pit.conformity_date` = **2026-01-01**  (2026-01-01 → open) [A.1, US-IDS5-019, direct artifact inspection, conf high] — Static conformity (2026 ch. 1, H0559); federal wage exclusions carry over; UI wages include board/lodging; domestic UI on noncash too.

## 9 — Deductions and garnishments
- `id.garn.creditor.max_percent` = **25** percent (2026-01-01 → open) [A.1, US-IDS5-016, direct artifact inspection, conf high] — 11-207 mirrors CCPA: lesser of 25% or excess over 30 x federal MW; support 50/60% (55/65% arrears > 12 weeks).
- `id.garn.child_support.cap_percent` = **50** percent (2025-02-06 → open) [A.1, US-IDS5-017, direct artifact inspection, conf high] — 32-1210: total cap 50% of disposable incl. arrears and fee (stricter than CCPA); remit within 7 business days; answer court order within 10 days; current first then pro rata.
- `id.garn.child_support.employer_fee` = **5** USD (2025-02-06 → open) [A.1, US-IDS5-017, direct artifact inspection, conf high]

## 10 — Collective agreements / prevailing wage
No state prevailing wage (repealed 1985) [US-IDR3-003]; 44-1001 95% Idaho residents on public works, no wage rate.


## 11 — Indexation
MW tracks federal; SUI base AAW penultimate year (2027 unpublished, newest snapshot 2026-08-03); PIT 2,500/5,000 thresholds CPI-U; tables reissued as needed.


## 12 — Payroll data protection / records
No SSN truncation rule located (ch. 28-51 not read). Full SSN on ID W-4 and new-hire report (50%).

- `id.records.retention_years` = **3** years (2026-01-01 → open) [A.1, US-IDS5-006, direct artifact inspection, conf high] — 45-610(1): from last date of service.

## 13 — Live legal change
- `id.live.epb00744_2026_07_23` = **new withholding table in force prospectively from 2026-07-23 (mid_year_rate_change); level withholding**  (2026-07-23 → open) [A.2, US-IDS5-011, derived arithmetically, conf high] — Derivation recorded in register row US-IDS5-011: Tax = 5.3% of wages (after ICTCAT allowances, value 0) over threshold. Single/HoH: annual 16,100; monthly 1,342; semimonthly 671; biweekly 619; weekly 310; daily/misc 62. Married: annual 32,200; monthly 2,683; semimonthly 1,342; biweekly 1,238; weekly 619; daily 124. Each period threshold = annual /
- `id.live.h0544_military_leave` = **enacted (ch. 57), text not read; private-employer impact open**  (2026-01-01 → open) [A.1, US-IDS5-024, direct artifact inspection, conf low]

## Oracle — worked examples (C37)
- `id.oracle.stc.single_biweekly.withholding` = **31** USD (2026-07-23 → open) [A.2, US-IDS5-008, derived arithmetically, conf high] — Single, biweekly 1,212: 5.3% x (1,212 - 619) = 31.43 -> 31; matches 07-23-2026 table.
- `id.oracle.stc.married_weekly.withholding` = **20** USD (2026-01-01 → open) [A.2, US-IDS5-008, derived arithmetically, conf medium] — Married weekly 1,000: (52,000 - 32,000) x 5.3% / 52 = 20.38 -> 20 as published; the example uses 32,000, matching neither table (32,200 / 30,000) - use EPB00744 for numbers (ID-OQ-2).

## Special populations (US-OWN-005)
- Domestic: MW-excluded; withholding not required (account + W-2/967); UI at 1,000 cash/quarter on cash and noncash [US-IDS5-003, US-IDS5-020, US-IDS5-022].
- Agricultural: MW exclusions; withhold where federal applies and >= 1,000/yr; UI 20,000/quarter or 10 on 20 days; H-2A not taxed [US-IDS5-003, US-IDS5-020].
- Minors: opportunity wage 4.25 (under 20, 90 days); under-16 odd jobs and under-18 family MW-excluded; under-21 for parent and under-18 newspaper carriers UI-exempt [US-IDS5-001, US-IDS5-003, US-IDS5-023].
- Tipped: cash 3.35; > 30/month [US-IDS5-001, US-IDS5-002].
- Clergy: churches/seminaries/ministers UI-exempt; PIT follows federal [US-IDS5-023, US-IDS5-019].
- Students: own-school, under-22 work-study, student nurses/interns UI-exempt [US-IDS5-023].
- NRAs: ID W-4 status A, 0 allowances, add-on 15/31/33/66 weekly/biweekly/semimonthly/monthly (India students 0) - 2025 edition [US-IDS5-013].
- US nonresidents: 1,000 threshold [US-IDS5-020]. Statutory employees: no Idaho withholding required [US-IDS5-020].
- Corporate officers: withholding employees; UI opt-out before March 31 [US-IDS5-020, US-IDS5-021].
- Government: outside state MW law; UI covered except elected officials, legislators, guard, emergency temps, election workers < 1,000 [US-IDS5-002, US-IDS5-022, US-IDS5-023].

## Language seams (US-OWN-006)
No language requirement; English and Spanish posters offered [US-IDP9M-001]; payslip English (US-OWN-006).

## Open questions
Mirrors `unresolved[]` in the facts file (same keys).

- `id.wh.certificate.current_edition` (blocking) — Form ID W-4 2026 edition not captured (CDX lists to 04-28-2025); NRA add-ons and multiple-jobs factor (2025: 15,000 and 3,868) may have changed. **Would close it:** EFO00307 current edition from the STC withholding forms page (browser pass).
- `id.wh.example_threshold_discrepancy` (non-blocking) — STC computing page married example uses "over 32,000", matching neither EPB00744 edition. **Would close it:** STC explanation; until then numbers from EPB00744 07-23-2026.
- `id.sui.wage_base.next_year` (non-blocking) — 2027 SUI base/rate array unpublished; 2024 AAW needed to derive 58,300 not obtained. **Would close it:** IDOL 2027 Tax Rate Class array PDF and the annual wage-base notice.
- `id.report.w2.state_record_layout` (non-blocking) — Idaho EFW2 RS/RV state-record spec not fetched. **Would close it:** STC Software Developers page "W-2 e-file specifications" PDF.
- `id.paycard.rule` (non-blocking) — 45-608 does not address paycards. **Would close it:** IDOL Wage and Hour statement or IDAPA rule.
- `id.final_pay.accrued_vacation` (non-blocking) — Whether accrued vacation is "wages" under 45-601(7) when policy is silent. **Would close it:** IDOL Wage and Hour guidance or Idaho Supreme Court decision on 45-606.
- `id.local_leave.preemption` (non-blocking) — Search lead 44-2701 was the non-compete chapter (tier-B error); no pre-emption statute or city leave ordinance located. **Would close it:** Full-text Idaho Code search "political subdivision" + "leave" on the Legislature site.
- `id.garn.state_tax_levy` (non-blocking) — STC wage levy (63-3061ff) and priority vs IWOs not researched. **Would close it:** STC "wage garnishment" employer page or the statute.
- `id.data_protection.breach` (non-blocking) — Idaho Code 28-51 and any SSN display rule not read. **Would close it:** Chapter 28-51 text.
- `id.leave.military_h0544` (non-blocking) — H0544 (2026) text not read; reach to private employers unknown. **Would close it:** Enrolled bill or Session Law ch. 57.

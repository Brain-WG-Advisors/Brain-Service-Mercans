# CCG annex_FL research pack — Florida

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B, 2026-11-02. Source: `_research/stage5/FL.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_FL-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** T1: no state or local wage tax. Payroll obligations: constitutional minimum wage (14.00 to 2026-09-29, 15.00 from 2026-09-30, first CPI-W indexation effective 2028-01-01), tipped cash wage (credit capped at 3.02), employer-only reemployment tax (base 7,000; 0.1%-5.4%; new 2.7%; RT-6 with fixed-length or XML upload), new-hire reporting including non-employees paid 600+, E-Verify certification, and garnishment/child-support rules. No general pay-statement statute (labor pools only); local wage/leave mandates pre-empted.

## 1 — Employment / labour code
- `fl.minwage.hourly` = **14.0** USD (2025-09-30 → 2026-09-29) [A.1, US-FLS5-001, quoted from authority page, conf high] — Fla. Const. Art. X s.24(c). Fla. Stat. 448.110 still prints 6.15 (stale; overridden), but controls coverage (FLSA-covered only).
- `fl.minwage.hourly` = **15.0** USD (2026-09-30 → 2027-12-31) [A.1, US-FLS5-001, quoted from authority page, conf high] — Steps 10.00 (2021) -> 15.00; first CPI-W adjustment calculated 2027-09-30, effective 2028-01-01: no change in 2027.
- `fl.minwage.tip_credit.max` = **3.02** USD (2021-09-30 → open) [A.1, US-FLS5-001, derived arithmetically, conf high] — Capped at the 2003 FLSA tip credit: 5.15 - 2.13 = 3.02 (federal inputs, FED unit).
- `fl.minwage.tipped.cash_wage` = **10.98** USD (2025-09-30 → 2026-09-29) [A.1, US-FLS5-001, derived arithmetically, conf high] — 14.00 - 3.02.
- `fl.minwage.tipped.cash_wage` = **11.98** USD (2026-09-30 → 2027-12-31) [A.1, US-FLS5-001, derived arithmetically, conf high] — 15.00 - 3.02; poster confirmation open (low risk).
- `fl.minwage.pre_suit_notice_days` = **15** days (2026-01-01 → open) [A.1, US-FLS5-002, quoted from authority page, conf high] — 448.110; DOR/FloridaCommerce post new rate by 15 Oct, mailed notice by 15 Nov.
- `fl.local_mandates.preempted` = **True**  (2024-07-01 → open) [A.1, US-FLS5-009, quoted from authority page, conf high] — 218.077(2) (ch. 2024-80): no local minimum wage or employment-benefit mandates (sick leave, vacation, holidays) or contractor-wage control; exceptions own employees and direct subsidy recipients.
- `fl.manual_labor.legal_day_hours` = **10** hours (2026-01-01 → open) [A.1, US-FLS5-027, quoted from authority page, conf high] — 448.01: extra pay beyond 10 h/day absent written contract; no premium rate fixed. Otherwise FLSA only.
- `fl.everify.employer_threshold` = **25** employees (2023-07-01 → open) [A.1, US-FLS5-010, quoted from authority page, conf high] — 448.095: private employers 25+ and all public agencies must use E-Verify within 3 business days; certify on first RT return each year or RT-E Verify [US-FLS5-019].

## 2 — Income tax (state withholding)
No state income tax on natural persons (Fla. Const. Art. VII s.5(a)) [US-FL-001]; DOR tax list has no personal income or withholding tax [US-FL-002, US-FLL-003]. Not applicable: state withholding method, W-4, supplemental, rounding, state W-2, reciprocity, resident/nonresident. Florida residents working elsewhere follow the work state (MULTI).

- `fl.pit.exists` = **False**  (2026-01-01 → open) [A.1, US-FL-001, quoted from authority page, conf high]

## 2c — Local wage taxes
None [US-FLL-003].


## 3 — Social insurance (SUI / SDI / PFML / levies)
- `fl.sdi_pfml.exists` = False (2026-01-01 → open) [A.1, US-FLP52-001 — promoted to fact in Synthesis C] Title XXXI has no SDI/TDI/PFML chapter; no state WARN. Workers comp employer-funded, employee contribution void (440.21) [US-FLP52-002].
- `fl.sui.wage_base` = **7000** USD (2015-01-01 → open) [A.1, US-FLS5-003, second independent authority, conf high] — Fixed in statute; successor may count predecessor wages; out-of-state wages credited via RT-6NF [US-FLS5-020, US-FLS5-018].
- `fl.sui.employer.rate.min` = **0.1** percent (2026-01-01 → 2026-12-31) [A.2, US-FLS5-018, quoted from authority page, conf high] — = 7 per employee.
- `fl.sui.employer.rate.max` = **5.4** percent (2026-01-01 → 2026-12-31) [A.2, US-FLS5-018, quoted from authority page, conf high] — = 378 per employee; +1 point for short-time-compensation employers.
- `fl.sui.new_employer.rate` = **2.7** percent (2026-01-01 → open) [A.1, US-FLS5-004, quoted from authority page, conf high] — While chargeable < 8 quarters (statute); DOR: until reported 10 quarters.
- `fl.sui.rounding` = **contribution fraction under half a cent dropped; half a cent or more rounds up to 1 cent**  (2026-01-01 → open) [A.1, US-FLS5-004, quoted from authority page, conf high]
- `fl.sui.employee.rate` = **0** percent (2026-01-01 → open) [A.1, US-FLS5-004, quoted from authority page, conf high] — 443.131(1): may not be deducted from wages.
- `fl.sui.liability_threshold.quarterly_wages` = **1500** USD (2026-01-01 → open) [A.3, US-FLS5-020, direct artifact inspection, conf medium] — Or 1 employee in 20 weeks or FUTA liability; domestic 1,000 in a quarter.

## 4 — Payslip statute
- `fl.payslip.general_statute.exists` = **False**  (2026-01-01 → open) [A.1, US-FLL-002, quoted from authority page, conf high] — Only labor pools: itemised deductions at each payment (electronic on request) and annual earnings summary by 1 February (448.24(2)(g),(h)).

## 5 — Statutory reporting instruments
Other: BLS-3020 multiple worksite; RT-6EW; RT-6NF; RT-7 annual for domestic-only employers (due 1 Jan, late after 31 Jan). Registration DR-1 online. DR-835 POA / RTS-9 agent [US-FL-005].

- `fl.report.sui.rt6` = **RT-6 (R. 07/23) due 30 Apr, 31 Jul, 31 Oct, 31 Jan (next business day); zero report required; e-payment by 5 pm ET business day before; lines 1 covered employees (12th), 2 gross, 3 excess over 7,000, 4 taxable, 5 tax; wage detail name/SSN/gross/taxable; corrections RT-8A**  (2023-07-01 → open) [A.2, US-FLS5-021, direct artifact inspection, conf high]
- `fl.report.sui.efile_threshold_employees` = **10** employees (2026-01-01 → open) [A.1, US-FLS5-006, quoted from authority page, conf high] — 10+ employees in any quarter of prior state fiscal year must e-file/e-pay; non-electronic report 25 + 1/employee max 300; erroneous report greater of 50 or 10% max 300 [US-FLS5-024]; ITIN not accepted.
- `fl.report.sui.flat_file` = **Flat File Web Import v7 (Dec 2023): fixed-length records 00 Header, 01 Employer, 02 Employee, 03 Totals, 99 Trailer; 2 implied decimals; zip refused**  (2023-12-01 → open) [A.2, US-FLS5-022, direct artifact inspection, conf high]
- `fl.report.sui.xml` = **FL_RT_XML_Schemas_v2026 1.0: 9 XSD in IRS efile envelope; required above 20,000 employee records; RT-6 sample validates (lxml)**  (2026-01-01 → open) [A.2, US-FLS5-023, direct artifact inspection, conf high]
- `fl.report.sui.xml_required_records` = **20000** records (2026-01-01 → open) [A.2, US-FLS5-023, direct artifact inspection, conf high]
- `fl.newhire.report_days` = **20** days (2026-01-01 → open) [A.1, US-FLS5-008, quoted from authority page, conf high] — 409.2576; DOB optional; also NON-EMPLOYEES paid 600+ in a year within 20 days (DD/RSPEC scope item).
- `fl.newhire.nonemployee_threshold` = **600** USD (2026-01-01 → open) [A.1, US-FLS5-008, quoted from authority page, conf high]

## 6 — Leave
- `fl.leave.sick.state_statute.exists` = **False**  (2024-07-01 → open) [A.1, US-FLS5-009, quoted from authority page, conf high] — None at state level; local mandates pre-empted.
- `fl.leave.domestic_violence.days` = **3** working days (2026-01-01 → open) [A.1, US-FLS5-014, quoted from authority page, conf high] — Employers 50+, employees 3+ months; up to 3 working days per 12 months, paid or unpaid at employer choice.

## 7 — Termination and final pay
- `fl.final_pay.state_statute.exists` = **False**  (2026-01-01 → open) [A.1, US-FLS5-016, quoted from authority page, conf medium] — No final-pay timing or vacation payout statute; prevailing party fees in wage action (448.08).

## 8 — Benefits in kind / taxable wages
- `fl.sui.wages.taxable_items` = **personal-use cars, non-convenience meals and lodging, group legal, golden parachutes, excess discounts, below-market loan interest, reported tips**  (2026-01-01 → open) [A.1, US-FLS5-003, second independent authority, conf high] — 443.1217(2)(b)-(g); excluded: sickness/accident/medical/death plan payments, employer-paid employee FICA, convenience meals/lodging, 401(a)/403(a)/SEP/403(b) non-salary-reduction/3121(v)(3). 401(k) deferral treatment open.

## 9 — Deductions and garnishments
- `fl.garn.head_of_family.weekly_exempt` = **750** USD (2026-01-01 → open) [A.1, US-FLS5-012, quoted from authority page, conf high] — 222.11: head of family disposable earnings up to 750/week fully exempt; above only with separate written waiver up to CCPA; others CCPA. Not indexed.
- `fl.garn.child_support.employer_fee.first` = **5** USD (2026-01-01 → open) [A.1, US-FLS5-013, quoted from authority page, conf high] — 61.1301: 5 first deduction, 2 each after; start first pay date > 14 days after service; remit within 2 days after pay date; arrears +20%; termination notice penalty 250/500.
- `fl.garn.child_support.employer_fee.subsequent` = **2** USD (2026-01-01 → open) [A.1, US-FLS5-013, quoted from authority page, conf high]
- `fl.garn.child_support.remit_days` = **2** days (2026-01-01 → open) [A.1, US-FLS5-013, quoted from authority page, conf high]

## 10 — Collective agreements / prevailing wage
- `fl.prevailing_wage.state_law.exists` = False (2026-01-01 → open) [A.1, US-FLP52-003 — promoted to fact in Synthesis C] Ch. 255 scanned in full; local procurement wage control barred (218.077(2)(b)-(c)).

## 11 — Indexation
MW fixed steps to 15.00 (2026-09-30); CPI-W from 2028-01-01; UI base not indexed; UI rates yearly (RT-20); garnishment 750 not indexed.


## 12 — Payroll data protection / records
- `fl.breach.notice_days` = **30** days (2026-01-01 → open) [A.1, US-FLS5-017, quoted from authority page, conf high] — 501.171: notice to Dept. of Legal Affairs for 500+ Floridians within 30 days (+15 for good cause). ch. 2026-52 s. 9 amended only 501.171(11)(d) (public-records exemption, definition of 'proprietary information'), effective 2026-04-23; the 30-day rule is unchanged [US-FLV6C-001].

## 13 — Live legal change
- `fl.live.minwage_2026_09_30` = **minimum wage 15.00 and tipped 11.98 from 2026-09-30, in force**  (2026-09-30 → open) [A.1, US-FLS5-001, quoted from authority page, conf high]

## Oracle — worked examples (C37)
No withholding oracle (no wage tax). UI: Line 4 x rate with half-cent rounding; RT-800002 p.9 worked examples (successor wages; NY to FL transfer) and the 4 RT XML test cases [US-FLS5-020, US-FLS5-023].


## Special populations (US-OWN-005)
- Domestic: UI at 1,000 cash/quarter; RT-7 annual option; minor hours limits not applicable; casual private-residence labor not "employee" for E-Verify [US-FLS5-005, US-FLS5-004].
- Agricultural: UI at 10,000 cash/quarter or 5+ workers in 20 weeks; crew-leader rules [US-FLS5-005].
- Minors: 450.081 hours (15 and under 3 h school days/15 h week; 16-17 8 h/30 h in session); no subminimum; newspaper delivery under 18 UI-exempt [US-FLS5-011, US-FLS5-005].
- Tipped: credit 3.02; 11.98 from 2026-09-30; reported tips are UI wages [US-FLS5-001, US-FLS5-020, US-FLS5-021].
- Clergy: churches/ministers UI-exempt; other 501(c)(3) covered at 4+ in 20 weeks [US-FLS5-005, US-FLS5-020].
- Students: own-school, co-op, student nurses/interns, F/J purpose-related work UI-exempt [US-FLS5-005, US-FLS5-020, US-FLS5-025].
- NRAs: no PIT; UI taxable except F/J; ITIN invalid on RT-6 [US-FLS5-025, US-FLS5-024].
- Statutory employees: agent/commission drivers and traveling salespersons UI-covered; commission insurance/real-estate (and barbers) exempt [US-FLS5-005, US-FLS5-020].
- Government: UI covers public employers with exceptions; E-Verify mandatory; own-employee wage autonomy [US-FLS5-005, US-FLS5-010, US-FLS5-009].
- Corporate officers covered; family employment exempt except in corporations [US-FLS5-005, US-FLS5-020].
- Labor pools: 448.24 itemised statement and annual summary [US-FLL-002].

## Language seams (US-OWN-006)
Minimum-wage poster in English and Spanish (448.109(3)(a)) [US-FLL-001]; RT-83 poster with Spanish version RT-83SP [US-FLS5-026]; payslip English (US-OWN-006). FL postings page unreadable (recorded limit).

## Open questions
Mirrors `unresolved[]` in the facts file (same keys).

- `fl.sui.wages.401k_deferral` (blocking) — 443.1217(2)(f) excludes payments to a 401(a) trust and carves out salary reduction only for 403(b); ambiguous against FUTA 3306(r); DOR guide silent. **Would close it:** A DOR TIP or an answer from DOR e-vendor / Reemployment Tax FAQ.
- `fl.termination.separation_notice` (non-blocking) — 443.151(1) defers to rules; whether a FloridaCommerce rule requires a separation form was not read. **Would close it:** Rule chapters 73B-10/73B-11 F.A.C. on flrules.org.
- `fl.live.ch_2026_52` — CLOSED (QA r2, 2026-11-06): ch. 2026-52 (SB 7026) read on laws.flrules.org [A.1, US-FLV6C-001]: s. 9 amends 501.171(11)(d) only; in force on becoming law 2026-04-23 (s. 19; approved and filed 2026-04-23). US-FLV6-002 effective_from set to 2026-04-23 (was the retrieval date).
- `fl.minwage.tipped.poster_confirmation` (non-blocking) — 11.98 is derived from A.1 but not confirmed on the FloridaCommerce 2026 poster (access gap). **Would close it:** FloridaCommerce 2026 minimum wage poster.
- `fl.report.sui.xml_changes_2026` (non-blocking) — RT_changes.xlsx inside the RT XML package not read. **Would close it:** Read RT_changes.xlsx in FL_DOR_flRtXmlPkg_2026-11-02.zip (Stage 3 / RSPEC).
- `fl.live.bulletin_sweep` (non-blocking) — Florida 2026 session laws other than ch. 2026-52 and the 2026 DOR Tax Information Publications are not among the sources used, so a further 2026 Florida payroll change is not established. **Would close it:** Laws of Florida 2026 index and DOR Tax Information Publications 2026 (browser pass).

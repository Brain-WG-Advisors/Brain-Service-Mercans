# CCG annex_IN research pack — Indiana

Synthesis B, 2026-11-02. Source: `_research/stage5/IN.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_IN-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** Minimum wage tracks the FLSA (7.25; state law covers only non-FLSA employers with 2+ employees); local mandates pre-empted; weekly overtime. State PIT 2.95% (2.90% from 2027 per DOR) plus county LIT in all 92 counties (rate by Jan-1 county, chart R47/10-26 from 2026-10-01: Boone 0.0171); WH-4 exemptions 1,000/1,500/3,000; supplemental flat 2.95% + county; 30-day nonresident safe harbor; reciprocity KY/MI/OH/PA/WI (county still withheld). UI employer-only, base 9,500, new 2.5%. Pay-statement duty literally limited to non-FLSA employers. Oracle: DN#1 example 13.96 + 4.73.

## 1 — Employment / labour code
- `in.minwage.hourly` = **7.25** USD (2009-07-24 → open) [A.1, US-INS5-001, direct artifact inspection, conf high] — IC 22-2-2-4(c): state minimum = FLSA minimum; state law covers employers with 2+ employees NOT subject to FLSA MW (22-2-2-3).
- `in.minwage.tipped.cash_wage` = **2.13** USD (2026-01-01 → open) [A.1, US-INS5-001, direct artifact inspection, conf high]
- `in.local_mandates.preempted` = **True**  (2026-01-01 → open) [A.1, US-INS5-002, direct artifact inspection, conf high] — IC 22-2-2-10.5 (MW) and 22-2-16-3 (benefits/leave); not for a unit's own employees.
- `in.overtime.weekly_threshold_hours` = **40** hours (2026-01-01 → open) [A.1, US-INS5-001, direct artifact inspection, conf high] — 1.5x; no daily OT; hospitals 14-day/80 h with 8 h daily trigger; domestic covered.
- `in.pay_frequency.rule` = **at least semimonthly, or biweekly on request; pay covers wages up to no more than 10 business days before payday (IC 22-2-5-1)**  (2026-01-01 → open) [A.1, US-INS5-003, direct artifact inspection, conf high]
- `in.payment.method` = **US money, negotiable check, draft, money order, or electronic transfer to institution designated by employee; paycards not named; DD cannot be forced (75%)**  (2026-01-01 → open) [A.1, US-INS5-003, direct artifact inspection, conf high]
- `in.late_wages.liquidated_damages_multiple` = **2** ratio (2026-01-01 → open) [A.1, US-INS5-003, direct artifact inspection, conf high] — 22-2-5-2 if not in good faith, plus attorney fees.

## 2 — Income tax (state withholding)
- `in.pit.rate` = **2.95** percent (2026-01-01 → 2026-12-31) [A.2, US-INS5-009, quoted from authority page, conf high] — IC 6-3-2-1 not read (SPA); DOR rates page.
- `in.pit.rate` = **2.9** percent (2027-01-01 → open) [A.2, US-INS5-009, quoted from authority page, conf medium] — DOR: "will adjust in 2027 to 2.90%"; statute not read.
- `in.wh.method` = **taxable wages = gross per period - deduction constants (annual / 52, 26, 24, 12, 365); x 2.95% state and x county rate; 2-decimal constants and results**  (2026-10-01 → open) [A.2, US-INS5-007, derived arithmetically, conf high] — DN#1 R47/10-26 effective 2026-10-01 supersedes R46/01-26 (US-IN-001, effective_to 2026-09-30).
- `in.wh.exemption.personal` = **1000** USD (2026-01-01 → open) [A.2, US-INS5-007, derived arithmetically, conf high] — WH-4 line 5; not indexed.
- `in.wh.exemption.dependent` = **1500** USD (2026-01-01 → open) [A.2, US-INS5-007, derived arithmetically, conf high] — Lines 6 and 7 (first-time dependent one year only).
- `in.wh.exemption.adopted_child` = **3000** USD (2026-01-01 → open) [A.2, US-INS5-007, derived arithmetically, conf high] — Line 8.
- `in.wh.supplemental.rate` = **2.95** percent (2026-01-01 → 2026-12-31) [A.2, US-INS5-007, derived arithmetically, conf high] — Flat state rate plus county rate, no exemptions; Indiana does not follow IRC 3402(n).
- `in.wh.certificate` = **WH-4 (State Form 48845, R10/8-23): counties of residence and principal employment as of Jan 1; additional state/county lines 9-10; new WH-4 within 10 days when exemptions decrease**  (2023-08-01 → open) [A.3, US-INS5-021, direct artifact inspection, conf high]

## 2b — Non-resident regime and reciprocity
- `in.nonres.safe_harbor_days` = **30** days (2024-01-01 → open) [A.2, US-INS5-007, derived arithmetically, conf high] — IC 6-3-2-27.5: no state/county withholding when expected <= 30 days in Indiana; time-and-attendance system or WH-4AFF; catch-up once exceeded.
- `in.reciprocity.states` = **KY, MI, OH, PA, WI**  (2026-01-01 → open) [A.3, US-INS5-012, quoted from authority page, conf high] — WH-47; no state tax, but county tax withheld if principal work county on Jan 1 is in Indiana [US-IN-002, US-INS5-008]. NRAs: one exemption only on WH-4.

## 2c — Local wage taxes
- `in.local.lit.county_basis` = **county of residence on Jan 1 (out-of-state residents: county of principal work on Jan 1), fixed for the year; withheld and reported with state tax on WH-1/WH-3/W-2 RS (T3 piggyback); no separate nonresident rate**  (2026-01-01 → open) [A.2, US-INS5-008, direct artifact inspection, conf high]
- `in.local.lit.rate.boone` = **0.0171** ratio (2026-10-01 → open) [A.2, US-INS5-007, derived arithmetically, conf high] — Was 0.017 to 2026-09-30 (R46).
- `in.local.lit.rate.marion` = **0.0202** ratio (2026-10-01 → open) [A.2, US-INS5-007, derived arithmetically, conf high] — Derivation recorded in register row US-INS5-007: State AGI rate 2026 2.95%. Method: taxable = gross per period - deduction constants (WH-4 line 5 personal exemptions 1,000/yr each incl. 65+/blind; lines 6 and 7 dependent and first-time dependent 1,500/yr each; line 8 adopted child 3,000/yr; constants = annual amount / pay periods: weekly 52, biwee
- `in.local.lit.rate.min` = **0.005** ratio (2026-10-01 → open) [A.2, US-INS5-007, derived arithmetically, conf high] — Porter.
- `in.local.lit.rate.max` = **0.03** ratio (2026-10-01 → open) [A.2, US-INS5-007, derived arithmetically, conf high] — Randolph. Full 92-county chart in DN#1 R47/10-26 (builder reads the chart).
- `in.local.lit.change_calendar` = **ordinance Jan 1-Aug 31 -> effective Oct 1 same year; Sep 1-Oct 31 -> Jan 1 next year; Nov 1-Dec 31 -> Oct 1 next year**  (2026-01-01 → open) [A.2, US-INS5-008, direct artifact inspection, conf high]

## 3 — Social insurance (SUI / SDI / PFML / levies)
No SDI/TDI/PFML/LTC/transit/workforce levy [US-INR3-002, US-KYR3-003, US-OWN-007]. Coverage: domestic 1,000 cash/quarter; agricultural 20,000/quarter or 10 in 20 weeks; clergy excluded.

- `in.sui.wage_base` = **9500** USD (2011-01-01 → open) [A.2, US-INS5-014, derived arithmetically, conf medium] — Not indexed; no 2026-labelled DWD page; IC 22-4-4-2 not read (80%).
- `in.sui.new_employer.rate` = **2.5** percent (2026-01-01 → open) [A.2, US-INS5-014, derived arithmetically, conf medium] — First 4 calendar years; construction lesser of 4.0% or construction average (2.50% for 2025); government 1.6% [US-IN-003].
- `in.sui.employer.rate.min` = **0.5** percent (2026-01-01 → open) [A.2, US-INS5-014, derived arithmetically, conf medium] — 9,500 x 0.50% = 47.50 (table check).
- `in.sui.employer.rate.max` = **7.4** percent (2026-01-01 → open) [A.2, US-INS5-014, derived arithmetically, conf medium] — Good standing; delinquent max 9.40%; penalty rate computed + 2% [US-INS5-015 partial]. 2026 solvency surcharge/schedule not obtained.
- `in.sui.employee.rate` = **0** percent (2026-01-01 → open) [A.2, US-INS5-014, derived arithmetically, conf high] — Derivation recorded in register row US-INS5-014: '2011 to 2025: premiums are based on the first 9,500 of wages per employee per calendar year': minimum 0.50% (47.50), typical new employer 2.50% (237.50), maximum in good standing 7.40% (703.00), maximum delinquent 9.40% (902.50) [9,500 x rate re-derived]. Employer-only premiums (no employee contrib

## 4 — Payslip statute
- `in.payslip.items` = **hours worked, wages paid, deductions made, each pay period (IC 22-2-2-8(a))**  (2026-01-01 → open) [A.1, US-INS5-001, direct artifact inspection, conf medium] — Scope: binds employers subject to the chapter = 2+ employees NOT subject to FLSA MW (literal reading 70%); build emits the three items anyway. No e-delivery/retention clause; federal 3-year fallback.

## 5 — Statutory reporting instruments
- `in.report.wh.wh1` = **WH-1 via INTIME (online or upload < 10 MB) or SFTP; annual if monthly average <= 83.33, monthly if <= 1,000 (30 days after month end), early filer above**  (2026-01-01 → open) [A.2, US-INS5-010, quoted from authority page, conf medium]
- `in.report.annual.wh3` = **WH-3 + state W-2 due Jan 31; electronic mandatory above 25 statements (IC 6-3-4-16.5); XML (schema IDORWTH2016V1.0 not downloaded) / IRIS XML / EFW2 for existing filers; DOR FAQ "Feb 28" conflicts - use Jan 31**  (2026-01-01 → open) [A.2, US-INS5-011, direct artifact inspection, conf high] — 1220 flat file retired 2027-09 [US-INS5-010].
- `in.report.w2.efile_threshold` = **25** statements (2026-01-01 → open) [A.2, US-INS5-011, direct artifact inspection, conf high]
- `in.report.sui.quarterly` = **DWD E S S/UPLINK due Apr 30, Jul 31, Oct 31, Jan 31; electronic filing (646 IAC 5-2-2) and payment (5-2-17) mandatory; penalty 25 per missing report**  (2019-01-01 → open) [A.2, US-INS5-014, derived arithmetically, conf high] — Derivation recorded in register row US-INS5-014: '2011 to 2025: premiums are based on the first 9,500 of wages per employee per calendar year': minimum 0.50% (47.50), typical new employer 2.50% (237.50), maximum in good standing 7.40% (703.00), maximum delinquent 9.40% (902.50) [9,500 x rate re-derived]. Employer-only premiums (no employee contrib
- `in.newhire.report_days` = **20** days (2024-07-01 → open) [A.3, US-INS5-016, second independent authority, conf high] — in-newhire.com, electronic only since 2024-07-01 (SB 148-2024, 4 extra fields); rehire after 60+ days; penalty 25 / 500.

## 6 — Leave
- `in.leave.sick.state_mandate.exists` = **False**  (2026-01-01 → open) [A.1, US-INS5-002, direct artifact inspection, conf high]
- `in.leave.military_family.days` = **10** working days (2026-01-01 → open) [A.1, US-INS5-006, direct artifact inspection, conf high] — IC 22-2-13: unpaid, 12 months and 1,500 hours.

## 7 — Termination and final pay
- `in.final_pay.rule` = **discharge: regular payday for the period of separation (22-2-9-2); resignation: next usual payday; employer pays conceded part of disputed amount (22-2-9-3)**  (2026-01-01 → open) [A.1, US-INS5-005, direct artifact inspection, conf high] — No vacation payout statute (open). No mandatory separation notice; answer DWD SF52984.

## 8 — Benefits in kind / taxable wages
Federal AGI start; withholding duty follows federal duty [US-INS5-012]. IRC conformity date and HSA/125/transit departures not read (low confidence).


## 9 — Deductions and garnishments
- `in.deductions.wage_assignment` = **written, signed, revocable, employer-agreed, copy within 10 days, listed purpose (IC 22-2-6-2(b)); uniforms/tools lesser of 2,500/yr or 5% weekly disposable; no PPE charge; loan interest max prime + 4%**  (2026-01-01 → open) [A.1, US-INS5-004, direct artifact inspection, conf high]
- `in.deductions.overpayment_recovery` = **2 weeks notice; lesser of 25% of weekly disposable or excess over 30 x federal MW (IC 22-2-6-4)**  (2026-01-01 → open) [A.1, US-INS5-004, direct artifact inspection, conf high]
- `in.garn.child_support.employer_fee` = **2.0** USD (2026-01-01 → open) [A.3, US-INS5-017, quoted from authority page, conf high] — IC 31-16-15: start first period within 14 days after service; remit INSCCU each payday; 50+ employees with >1 order electronic; priority except current taxes; lump sums subject to arrears.
- `in.garn.creditor.max_percent` = **25** percent (2026-01-01 → open) [A.3, US-INS5-017, quoted from authority page, conf high] — Statute moved to IC 37-2-6-4 (P.L.115-2026; effective date tier-B 2026-07-01) [US-INS5-020].

## 10 — Collective agreements / prevailing wage
No state prevailing wage since 2015-07-01 (HEA 1019-2015) [US-INR3-005, US-INR3-006].


## 11 — Indexation
MW tracks FLSA; SUI base fixed since 2011; PIT statutory step 2.95 -> 2.90; LIT by county ordinance (Jan 1 / Oct 1); WH-4 amounts not indexed.


## 12 — Payroll data protection / records
- `in.breach.ag_penalty_max` = **150000** USD (2026-01-01 → open) [A.3, US-INS5-018, quoted from authority page, conf medium] — [partial row] [partial] IC 24-4.9.

## 13 — Live legal change
P.L.104-2026 political-subdivision deferred-retirement assignment; P.L.115-2026 UCCC recodified (garnishment cite IC 37-2-6-4); SEA 1-2025 municipal LIT from 2028 (tier-B detail only, US-INS5-019 MANUAL); 1220 flat file retired 2027-09.

- `in.live.dn1_r47` = **DN#1 R47/10-26 in force 2026-10-01 (Boone LIT 0.017 -> 0.0171); level withholding**  (2026-10-01 → open) [A.2, US-INS5-007, derived arithmetically, conf high] — Derivation recorded in register row US-INS5-007: State AGI rate 2026 2.95%. Method: taxable = gross per period - deduction constants (WH-4 line 5 personal exemptions 1,000/yr each incl. 65+/blind; lines 6 and 7 dependent and first-time dependent 1,500/yr each; line 8 adopted child 3,000/yr; constants = annual amount / pay periods: weekly 52, biwee

## Oracle — worked examples (C37)
- `in.oracle.dn1.example.state` = **13.96** USD (2026-10-01 → open) [A.2, US-INS5-007, derived arithmetically, conf high] — Weekly 800; constants A5 96.15 + B3 86.54 + B1 28.85 + C2 115.38 = 326.92; taxable 473.08 x 0.0295 = 13.96.
- `in.oracle.dn1.example.county` = **4.73** USD (2026-10-01 → open) [A.2, US-INS5-007, derived arithmetically, conf high] — 473.08 x 0.01 = 4.73.

## Special populations (US-OWN-005)
- Domestic: state MW law only via FLSA coverage; 40 h OT applies; agency companionship excluded; UI 1,000 cash/quarter; may opt out of withholding [US-INS5-001, US-INS5-014, US-INS5-012].
- Agricultural: excluded from state MW and pay-frequency chapter; UI 20,000/quarter or 10 in 20 weeks [US-INS5-001, US-INS5-003, US-INS5-014].
- Minors: under 16 excluded from state MW; hours limits only [US-INS5-001].
- Tipped: 2.13 + tip credit [US-INS5-001].
- Clergy: excluded from state MW; ministers may choose no withholding; UI-excluded [US-INS5-001, US-INS5-012, US-INS5-014].
- Students: own-school and student nurses excluded from MW [US-INS5-001, US-INS5-021].
- NRAs: one exemption [US-INS5-021]. Nonresidents: 30-day safe harbor; reciprocity with county still withheld [US-INS5-007].
- Commission-only/outside sales: excluded from MW [US-INS5-001].
- Government: wage-assignment chapter applies; UI 1.6% or reimbursable [US-INS5-004, US-INS5-014].
- Casual laborers / pensioners: may choose no withholding [US-INS5-012].

## Language seams (US-OWN-006)
IC 22-2-2-8 has no language clause; bilingual expressly permitted [US-INP6-001, US-INP9L-001]; payslip English (US-OWN-006).

## Open questions
Mirrors `unresolved[]` in the facts file (same keys).

- `in.local.lit.chart.2026_01_to_09` (non-blocking) — County LIT chart R46/01-26 (Boone 0.017; all other counties as in R47) governed 2026-01-01..2026-09-30 but sits on rows now superseded (US-IN-001, US-IN-P5-1-001, effective_to 2026-09-30); superseded rows cannot carry a number under the brief. **Would close it:** Final merge: accept period facts from rows superseded with an explicit effective_to (or register an S5 historical-period row for R46), then emit the Jan-Sep chart with effective_to 2026-09-30.
- `in.payslip.scope` (non-blocking) — IC 22-2-2-8 binds only employers "subject to this chapter" = non-FLSA employers (22-2-2-3); literal reading excludes most employers. **Would close it:** Owner/builder decision; or IDOL guidance on 22-2-2-8 scope. Recommendation: emit hours, wages, deductions anyway.
- `in.sui.rate_year.current` (non-blocking) — 2026 solvency surcharge, applied-rate schedule and a 2026-labelled wage base not obtained (partial row). **Would close it:** DWD state-premium-rate page as currently published, or IC 22-4-4-2 / 22-4-11-3.3 from the 2026 IC PDF (browser pass, US exit).
- `in.pit.rate.next_year.statute` (non-blocking) — 2.90% for 2027 rests on the DOR page alone; IC 6-3-2-1 unread (iga.in.gov SPA). **Would close it:** IC 6-3-2-1 from the 2026 IC Title 6 Article 3 PDF (browser pass).
- `in.report.wh.xml_schema` (non-blocking) — WH-1/WH-3 XML schema IDORWTH2016V1.0 and business rules not downloaded; EFW2 guide labelled 2025 and prior. **Would close it:** Schema files and TY2026 EFW2 guide fetched from a US exit.
- `in.final_pay.accrued_vacation` (non-blocking) — No payout statute; case law (tier-B lead) treats promised vacation as wages. **Would close it:** IDOL knowledge-base article or Indiana Supreme Court decision on courts.in.gov.
- `in.pit.conformity` (non-blocking) — IRC conformity date and HSA/125/transit departures not read. **Would close it:** IC 6-3-1-11 (2026) or DOR IT-40 2025 instructions, Add-backs.
- `in.garn.creditor.statute_text` (non-blocking) — IC 37-2-6-4 text, effective date and any employer fee not read. **Would close it:** IC Title 37 Article 2 (2026) via browser pass.
- `in.leave.other_mandated` (non-blocking) — Jury duty (IC 34-28-4), voting, volunteer firefighter leave not researched. **Would close it:** Those IC sections.

# CCG annex_AR research pack — Arkansas

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B, 2026-11-02. Source: `_research/stage5/AR.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_AR-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** State minimum wage 11.00 (employers with 4+ employees), weekly overtime only. State withholding on the DFA Formula Method 2026 (standard deduction 2,470, personal credit 29 per AR4EC exemption, top rate 3.7% from 2026-01-01 after Act 1 of 2026 1st Ex. Sess.) plus separate low-income tables. No local income tax, no reciprocity (Texarkana exemption). SUI base 7,000, new employer 2.0%, no employee UI, no SDI/PFML. No pay-statement statute; no paid sick leave statute. Several key employer-guide figures sit on legacy-id rows (US-ARP51-002 etc.) and are listed as non-fact lines pending re-key.

## 1 — Employment / labour code
- `ar.pay_frequency.rule` = corporations pay semimonthly; corporations with gross income >= 500,000 may pay FLSA-exempt managers earning > 25,000 at least monthly (11-4-401) (2026-01-01 → open) [A.1, US-ARP51-004 — promoted to fact in Synthesis C] 2008 compilation; later amendment not checked.
- `ar.minwage.hourly` = **11.0** USD (2021-01-01 → open) [A.2, US-ARS5-002, quoted from authority page, conf high] — 2018 Initiated Act (Issue 5); employers with 4+ employees; higher of state/FLSA. No 2027 increase enacted; 2026-11-03 ballot carries no initiative [US-ARS5-004].
- `ar.minwage.employer_size_min` = **4** employees (2021-01-01 → open) [A.2, US-ARS5-002, quoted from authority page, conf high]
- `ar.minwage.tipped.cash_wage` = **2.63** USD (2021-01-01 → open) [A.2, US-ARS5-002, quoted from authority page, conf medium] — Tip credit up to minimum wage; written notice each time the tip-credit amount changes (11 CAR 11).
- `ar.overtime.weekly_threshold_hours` = **40** hours (2026-01-01 → open) [A.2, US-ARS5-002, quoted from authority page, conf high] — 1.5x over 40/week (11-4-211); no daily OT; agricultural and FLSA-exempt excluded.
- `ar.paycard.free_withdrawals_per_load` = **1** count (2019-07-24 → open) [A.1, US-ARS5-003, direct artifact inspection, conf high] — 11-4-403(f) (Act 853 of 2019): direct deposit or preloaded card lawful; no employee-consent clause in the text.

## 2 — Income tax (state withholding)
- `ar.wh.supplemental.rate` = 3.7 (2026-01-01 → open) [A.2, US-ARP51-002 — promoted to fact in Synthesis C] Bonus/commission with regular wages; vacation pay in addition to regular pay treated as supplemental.
- `ar.wh.texarkana.exemption` = Texarkana AR residents exempt on all income; Texarkana TX residents exempt on wages earned in Texarkana AR (26-52-604); AR-TX-4EC; AR-3Q-TEX due 28 Feb (2026-01-01 → open) [A.2, US-ARP51-002 — promoted to fact in Synthesis C]
- `ar.wh.method` = **DFA Formula Method 2026: annualise; less standard deduction; band midpoint (USD 50) below 100,001; bracket formula; round annual tax to dollar; less 29 per exemption; divide by periods**  (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.wh.std_deduction` = **2470** USD (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.wh.personal_credit.per_exemption` = **29.0** USD (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.pit.bracket.1.ceiling` = **5599** USD (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — 0% band.
- `ar.pit.bracket.2.ceiling` = **11199** USD (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — 2% - 111.98
- `ar.pit.bracket.2.rate` = **2** percent (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.pit.bracket.2.subtract` = **111.98** USD (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.pit.bracket.3.ceiling` = **15999** USD (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.pit.bracket.3.rate` = **3** percent (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.pit.bracket.3.subtract` = **223.97** USD (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.pit.bracket.4.ceiling` = **26399** USD (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.pit.bracket.4.rate` = **3.4** percent (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.pit.bracket.4.subtract` = **287.97** USD (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.pit.bracket.5.ceiling` = **94700** USD (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.pit.bracket.5.rate` = **3.7** percent (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — 94,701-97,600: 3.7% with stepped adjustments 369.90 down to 89.90; 97,601+: 3.7% - 79.90.
- `ar.pit.bracket.5.subtract` = **367.16** USD (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.pit.bracket.top.subtract` = **79.9** USD (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.pit.top_rate` = **3.7** percent (2026-01-01 → open) [A.2, US-ARS5-013, direct artifact inspection, conf high] — Act 1 of 2026 1st Ex. Sess. (HB 1001 = SB 1), signed week of 2026-05-04, retroactive to 2026-01-01; operating level assessment for all 2026 and withholding via the reissued formula. Table switch date open (AR-OQ-1). Corporate 4.1% from 2027.
- `ar.wh.low_income_tables.single_weekly_zero_to` = **281.6** USD (2026-01-01 → open) [A.2, US-ARS5-011, direct artifact inspection, conf high] — Separate table-only method for AR4EC line 5; 281.60x52 = 14,643.20 consistent with the AR4ECSP ceiling.
- `ar.wh.certificate.form` = **AR4EC (R 12/04/2025); federal W-4 not used; no certificate = zero exemptions; decrease reported within 10 days**  (2025-12-04 → open) [A.2, US-ARS5-009, direct artifact inspection, conf high]
- `ar.wh.exemption_certificate.ar4ecsp.ceiling.single` = **14643** USD (2026-01-01 → open) [A.2, US-ARS5-010, direct artifact inspection, conf high] — AR4ECSP 2026 ceilings 14,643 / 24,695 / 29,722 / 20,820 / 24,818 (statuses per form).

## 2b — Non-resident regime and reciprocity
No reciprocity (no statutory authority). Rail/motor carriers withhold only for AR residents and nonresidents with all duties in AR; air carriers where 50%+ of scheduled flight time in AR [US-ARP51-002]. Pass-through entity withholding (3.7% / 4.3%) is outside payroll.

- `ar.nonres.sourcing` = **physical presence: work performed in AR when physically located in AR (convenience rule ended for tax years from 2021); apportion by AR working days / total working days**  (2021-01-01 → open) [A.1, US-ARS5-006, direct artifact inspection, conf high] — Act 1019 of 2021, 26-51-202(c), 504(a)(1), 902(5); level assessment and withholding. No day/dollar threshold (HB1116 of 2025 died).

## 2c — Local wage taxes
- `ar.local_wage_tax.exists` = **False**  (2026-01-01 → open) [A.2, US-ARP9V-003, direct artifact inspection, conf high]

## 3 — Social insurance (SUI / SDI / PFML / levies)
No SDI/TDI/PFML/LTC/transit programme: absence settled at mandate level (US-OWN-007 levy census, AR admin assessment 0.1% the only levy [US-ARP9V-001]); the per-state PFML row US-ARP52-007 is tier-B MANUAL and is not relied on. UI coverage: domestic 1,000 cash/quarter; agricultural 20,000/quarter or 10 workers in 20 weeks; exclusions: family employment, commission-only insurance/real-estate agents, students at own school, student nurses [US-ARP9V-001].

- `ar.sui.wage_base` = **7000** USD (2026-01-01 → open) [A.3, US-ARP9V-001, quoted from authority page, conf high] — 11-10-215; credit for wages paid toward the former state base when an employee permanently moves with the same employer.
- `ar.sui.new_employer.rate` = **2.0** percent (2026-01-01 → 2026-12-31) [A.2, US-ARP9V-002, quoted from authority page, conf high]
- `ar.sui.employer.rate.min` = **0.2** percent (2026-01-01 → 2026-12-31) [A.2, US-ARP9V-002, quoted from authority page, conf high] — 0.2-5.1% experienced; deficit 6.1/8.1/10.1%; includes 0.1% Administrative Assessment; conditional 0.2% advance interest and 0.1% extended benefit.
- `ar.sui.employer.rate.max` = **5.1** percent (2026-01-01 → 2026-12-31) [A.2, US-ARP9V-002, quoted from authority page, conf high]
- `ar.sui.admin_assessment.rate` = **0.1** percent (2026-01-01 → 2026-12-31) [A.2, US-ARP9V-002, quoted from authority page, conf high]
- `ar.sui.employee.rate` = **0** percent (2026-01-01 → open) [A.3, US-ARP9V-001, quoted from authority page, conf medium]
- `ar.sui.wages.section125_excluded` = **True**  (2026-01-01 → open) [A.3, US-ARP9V-001, quoted from authority page, conf medium]

## 4 — Payslip statute
- `ar.payslip.state_statute.exists` = False (2026-07-21 → open) [A.1, US-ARP52-006 — promoted to fact in Synthesis C] 11 CAR 11 compilation 2026-07-21; tip-credit change notice in writing.

## 5 — Statutory reporting instruments
- `ar.report.wh.monthly` = AR941M by the 15th of following month (zero voucher if nil); annual AR941A by 31 Jan when deposits under 1,000; EFT mandatory at average 20,000+/month; AR3MAR due 28 Feb (2026-01-01 → open) [A.2, US-ARP51-002 — promoted to fact in Synthesis C]
- `ar.report.w2.efile_threshold_employees` = 125 (2026-01-01 → open) [A.2, US-ARP51-002 — promoted to fact in Synthesis C] EFW2 via ATAP; RA, RE, RW, RS, RT, RF, RCS required; RV not allowed.
- `ar.report.sui.quarterly` = **Tax21 online or paper DWS-ARK-209B/209BR/209BS; due 30 Apr, 31 Jul, 31 Oct, 31 Jan, also when no wages**  (2026-01-01 → open) [A.3, US-ARP9V-001, quoted from authority page, conf high]
- `ar.report.sui.efile_threshold_employees` = **250** employees (2026-01-01 → open) [A.3, US-ARP9V-001, quoted from authority page, conf high]
- `ar.newhire.report_days` = **20** days (2026-01-01 → open) [A.3, US-ARP9V-001, quoted from authority page, conf high] — Via Tax21; all employees living or working in AR.
- `ar.child_support.verification_response_days` = **30** days (2026-01-01 → open) [A.3, US-ARS5-008, quoted from authority page, conf high]

## 6 — Leave
No paid sick leave statute (absence finding, medium) [US-ARS5-002, US-ARP9L-001, US-ARS5-004]; no PFML. Vacation entitlement by written policy [US-ARS5-014]. Jury/voting/military leave not researched (AR-OQ-5).


## 7 — Termination and final pay
- `ar.final_pay.discharge` = **next regular payday; double wages if unpaid within 7 days of that payday**  (2019-07-24 → open) [A.1, US-ARS5-003, direct artifact inspection, conf high] — 11-4-405 (Act 853 of 2019). Resignation deadline not located (AR-OQ-2). Vacation payout only if policy promises it [US-ARS5-014].
- `ar.final_pay.double_wages_after_days` = **7** days (2019-07-24 → open) [A.1, US-ARS5-003, direct artifact inspection, conf high]

## 8 — Benefits in kind / taxable wages
Excluded IRC 112, 125, 219, 401(k), 403(b), 408(k), 408(p), 457; non-cash wages at FMV; tips of 20+/month are wages [US-ARP51-002 legacy]. HSA outside 125, transit, GTL open (AR-OQ-3).


## 9 — Deductions and garnishments
Creditor exemption 16-66-208 (first 25/week) rests only on tier-B MANUAL row US-ARS5-012 — not a fact; CCPA limits apply until replaced (AR-OQ-8).

- `ar.deductions.nonstandard_below_minwage` = **False**  (2026-01-01 → open) [A.2, US-ARS5-002, quoted from authority page, conf high] — Breakage/shortages/fines may not reduce pay below minimum wage; court orders, assignments, board/lodging/apparel may.
- `ar.garn.child_support.arrears_addon.percent` = **10** percent (2026-01-01 → open) [A.3, US-ARS5-007, quoted from authority page, conf medium] — Usually 10% of current support toward arrears, now 20% in some cases (act unnamed, AR-OQ-4); CCPA cap; Arkansas Child Support Clearinghouse; OCSE MyWorkers [US-ARS5-008].

## 10 — Collective agreements / prevailing wage
- `ar.prevailing_wage.state_law.exists` = False (2017-01-01 → open) [A.2, US-ARP51-001 — promoted to fact in Synthesis C] Repealed 2017; Davis-Bacon only.

## 11 — Indexation
Minimum wage not indexed; SUI base fixed; withholding amounts republished yearly by legislation, no index factor.


## 12 — Payroll data protection / records
- `ar.records.withholding.retention_years` = 6 (2026-01-01 → open) [A.2, US-ARP51-002 — promoted to fact in Synthesis C] Including AR4EC copies.
- `ar.records.wage_hour.retention_years` = **3** years (2026-01-01 → open) [A.1, US-ARL-001, quoted from authority page, conf high] — 11-4-217.

## 13 — Live legal change
- `ar.live.act1_2026_ex_sess.status` = **in force retroactive 2026-01-01 (signed week of 2026-05-04); level assessment + withholding**  (2026-01-01 → open) [A.3, US-ARS5-005, quoted from authority page, conf medium]

## Oracle — worked examples (C37)
- `ar.oracle.example.1.input` = **monthly 2,127.00, 2 exemptions (Formula Method 2026)**  (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Derivation recorded in register row US-ARS5-001: Effective 2026-01-01. Annualise (x12/24/26/52; daily x260, 5-day week); standard deduction 2,470; net taxable below 100,001 looked up at the 50 midrange of the 100 band (the worked example says 'less than 97,701' - internal inconsistency), exact figure above; brackets 0-5,599 0%; 5,600-11,199 2% min
- `ar.oracle.example.1.withholding` = **36.5** USD (2026-01-01 → open) [A.2, US-ARS5-001, derived arithmetically, conf high] — Reproduced in Python: 25,524 - 2,470 = 23,054 -> midpoint 23,050 x 3.4% - 287.97 = 495.73 -> 496 - 58 = 438 / 12 = 36.50.

## Special populations (US-OWN-005)
- Domestic: exempt from AR withholding; UI at 1,000 cash/quarter [US-ARP51-002 legacy; US-ARP9V-001].
- Agricultural: withholding required with 4+ agricultural employees in a period; no state OT; UI 20,000/quarter or 10 in 20 weeks [US-ARP51-002, US-ARP51-004 legacy; US-ARP9V-001].
- Tipped: cash wage 2.63; written tip-credit notice; tips 20+/month withheld [US-ARS5-002; US-ARP52-006].
- Clergy: ministers exempt from AR withholding [US-ARP51-002].
- Students: 85% of minimum wage with DOLL certificate (11-4-210(b)); UI excludes students at own school [US-ARP51-004; US-ARP9V-001].
- NRAs: no AR rule beyond federal. Commission agents UI-excluded.
- Government/nonprofit: covered by withholding; UI reimbursable option [US-ARP9V-001].
- Military: active-duty pay 100% exempt (Act 1408 of 2013); spouses ARW-4MS yearly [US-ARP51-002].
- Texarkana residents: see income tax. Employers with fewer than 4 employees: outside AR MW Act [US-ARS5-002].
- Minors: not researched (AR-OQ-5).

## Language seams (US-OWN-006)
No language rule for pay records; posters [US-ARP9L-001]; payslip/filings en per US-OWN-006.

## Synthesis D additions (2026-11-02)

Source: browser-pass rows S5B-P1 / S5B-P2 merged into `legal-basis-register.csv` and SSA EFW2 TY2026 (US-FEDS5-032) read locally. Every claim below carries its register_id; the facts file is authoritative. Full log: `_research/synthesis-D/SYNTHESIS-D.md`.

Facts added:
- `ar.pit.rate.top` = **3.7** percent (2026-01-01 → open) [A.1, US-ARB5-001, direct artifact inspection, conf high] — Act 1 of the 2026 First Extraordinary Session (HB 1001), approved 2026-05-06, A.C.A. 26-51-201(a)(4)/(a)(5); tax years beginning on/after 2026-01-01. LEVEL: assessment rate; withholding formula start date still open (ar.wh.formula.switch_date).
- `ar.pit.high_income.threshold` = **94700** USD (2026-01-01 → open) [A.1, US-ARB5-001, direct artifact inspection, conf high] — Above 94,700 net income the two-band table applies (0-4,700 2%; 4,701+ 3.7%).
- `ar.pit.statute.tables` = **Net income <= 94,700: 0-5,599 0%; 5,600-11,199 2%; 11,200-15,999 3%; 16,000-26,399 3.4%; 26,400-94,700 3.7%. Net income > 94,700: 0-4,700 2%; 4,701+ 3.7%; bracket adjustment 290 at 94,701-94,800, stepping down 10 per 100, 0 from 97,601; tables indexed annually under 26-51-201(d)** (2026-01-01 → open) [A.1, US-ARB5-001, direct artifact inspection, conf high] — Ceilings agree with ar.pit.bracket.1-5 (DFA formula, US-ARS5-001).

Open questions narrowed / added: `ar.wh.formula.switch_date` (lines rewritten in the block below).

## Open questions
Mirrors `unresolved[]` in the facts file (same keys).

- `ar.final_pay.resignation` (non-blocking) — No statutory deadline for final pay on resignation located; current text of 11-4-405 not confirmed for a resignation clause. **Would close it:** Current Ark. Code 11-4-405 text (LexisNexis public portal or arkleg Act history).
- `ar.pit.wages.hsa_transit_gtl` (non-blocking) — Employer HSA outside 125, IRC 132(f) transit and IRC 79 GTL not in the employer guide exclusion list. **Would close it:** DFA Rule 2.26-51 conformity list or the AR IRC-conformity act (26-51-404).
- `ar.garn.iwo.employer_fee` (non-blocking) — Employer child-support fee only on a tier-B lead (2.50 per pay period, 9-14-218); the act raising arrears add-on to 20% is unnamed. **Would close it:** OCSE MyWorkers employer guide (Chrome pass) or Ark. Code 9-14-218 / 9-14-226.
- `ar.leave.mandated_leave` (non-blocking) — Jury, voting, military, crime-victim leave and child-labour hour limits not researched this run. **Would close it:** DOLL child-labour page and Ark. Code 16-31-106 and 7-1-102 (official text).
- `ar.data_protection.ssn_paystub` (non-blocking) — No AR rule on SSN on pay statements located; absence not verified. **Would close it:** Official text of Ark. Code 4-86-107.
- `ar.live.bulletin_sweep` (non-blocking) — 2025 Regular and 2026 Fiscal Session acts not swept (arkleg TLS failure). **Would close it:** arkleg Acts index via the orchestrator browser pass.
- `ar.garn.creditor.exempt_weekly` (non-blocking) — 16-66-208 creditor exemption (first 25/week of net wages of laborers and mechanics) rests only on tier-B MANUAL row US-ARS5-012. **Would close it:** Official Ark. Code 16-66-208 text.
- `ar.wh.formula.switch_date` (blocking) — DFA documents read do not state the date employers had to switch to the 3.7% formula/tables in 2026 or whether a catch-up was required; only a tier-B lead says 2026-05-29. **Would close it:** DFA withholding release/notice of May 2026 announcing the 3.7% formula start date (the Act itself does not state it). *(Synthesis D 2026-11-02)*

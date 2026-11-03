# CCG annex_IL research pack — Illinois

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B, 2026-11-02. Source: `_research/stage5/IL.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_IL-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** State minimum wage 15.00 (not indexed), Chicago 17.05 and suburban Cook 15.40 from 2026-07-01 (both indexed); weekly overtime. Flat 4.95% withholding on wages less IL-W-4 exemptions (2,925 + 1,000); no supplemental rate; reciprocity IA/KY/MI/WI; 30-day nonresident rule; no local tax. UI base 14,250, new 3.350%, no employee share; no SDI/PFML. PLAWA paid leave statewide (not in Chicago/Cook). Pay stub retention 3 years, copy rules. IL-941 quarterly, no annual reconciliation; monthly UI wage report for 25+. Oracle: IL-700-T examples 8.38 / 32.13.

## 1 — Employment / labour code
- `il.minwage.hourly` = **15.0** USD (2025-01-01 → open) [A.1, US-ILS5-001, second independent authority, conf high] — 820 ILCS 105/4, adults 18+; no later step, no indexation [US-ILS5-002].
- `il.minwage.youth.hourly` = **13.0** USD (2025-01-01 → open) [A.1, US-ILS5-001, second independent authority, conf high] — Under 18 working <= 650 h/calendar year.
- `il.minwage.new_hire_reduction` = **0.5** USD (2025-01-01 → open) [A.1, US-ILS5-001, second independent authority, conf high] — First 90 consecutive days, not day/temporary laborers.
- `il.minwage.tipped.cash_wage` = **9.0** USD (2025-01-01 → open) [A.1, US-ILS5-001, second independent authority, conf high] — Tip credit up to 40%.
- `il.minwage.coverage.min_employees` = **4** employees (2026-01-01 → open) [A.1, US-ILS5-026, direct artifact inspection, conf high] — 105/3: fewer than 4 outside the law except domestic workers; also small farms, outside salesmen, religious organisation members, own-college students, etc.
- `il.local_minwage.chicago.hourly` = **17.05** USD (2026-07-01 → 2027-06-30) [A.2, US-ILS5-008, quoted from authority page, conf high] — Employers 4+; tipped 12.96 (17.05 x 0.76 = 12.958); City contracts 18.50; indexed July 1 by CPI capped 2.5%.
- `il.local_minwage.chicago.tipped` = **12.96** USD (2026-07-01 → 2027-06-30) [A.2, US-ILS5-008, quoted from authority page, conf high]
- `il.local_minwage.cook.hourly` = **15.4** USD (2026-07-01 → open) [A.2, US-ILS5-009, derived arithmetically, conf high] — Suburban Cook County, employees over 18 with >= 2 h/week in the County; Chicago and opted-out municipalities excluded; tipped 9.25; OT 23.10 (15.40 x 1.5); tipped OT 16.94.
- `il.local_minwage.cook.tipped` = **9.25** USD (2026-07-01 → open) [A.2, US-ILS5-009, derived arithmetically, conf high] — Derivation recorded in register row US-ILS5-009: Suburban Cook County (not Chicago; municipalities with own MW or opted out excluded) from 2026-07-01: non-tipped $15.40/hour (overtime $23.10), tipped $9.25/hour (overtime $16.94 = 23.10 - 40% x 15.40); applies to employees over 18 working at least 2 hours/week in the County; not to under-18 (state 
- `il.overtime.weekly_threshold_hours` = **40** hours (2026-01-01 → open) [A.1, US-ILS5-001, second independent authority, conf high] — 105/4a; no daily OT; exemptions 4a(2).
- `il.pay_frequency.rule` = **at least semi-monthly, paid within 13 days after period end; EAP and commissions monthly (115/3)**  (2026-01-01 → open) [A.3, US-ILS5-003, quoted from authority page, conf high]
- `il.payment.method` = **direct deposit must be voluntary; cash with signed receipt; payroll card voluntary with written fee disclosure, revocable; card/DD offerors must also offer cash or check (115/4, 115/14.5)**  (2026-01-01 → open) [A.3, US-ILS5-005, quoted from authority page, conf high] — Payroll card rules [US-ILS5-007].

## 2 — Income tax (state withholding)
- `il.pit.rate.flat` = **4.95** percent (2026-01-01 → open) [A.2, US-ILR3-001, quoted from authority page, conf high] — IL-700-T R-12/25 re-verified byte-identical 2026-11-02; 35 ILCS 5/201 not read this pass.
- `il.wh.method` = **.0495 x (wages - exemptions/periods) + IL-W-4 Line 3; exemptions = Line 1 x 2,925 + Line 2 x 1,000 per year**  (2026-01-01 → 2026-12-31) [A.2, US-ILR3-001, quoted from authority page, conf high] — No rounding rule (tables in cents); no separate supplemental rate - bonus/OT/commission are wages [US-ILR3-002].
- `il.wh.exemption.line1` = **2925** USD (2026-01-01 → 2026-12-31) [A.2, US-ILR3-001, quoted from authority page, conf high] — Indexed by IDOR.
- `il.wh.exemption.line2` = **1000** USD (2026-01-01 → 2026-12-31) [A.2, US-ILR3-001, quoted from authority page, conf high]
- `il.wh.certificate` = **IL-W-4 R-07/23 current; no exemptions if AGI > 500k joint / 250k other; none on file = no exemptions; changes effective next quarter date at least 30 days after filing**  (2023-07-01 → open) [A.2, US-ILS5-010, direct artifact inspection, conf high]

## 2b — Non-resident regime and reciprocity
- `il.reciprocity.states` = **IA, KY, MI, WI**  (2026-01-01 → open) [A.2, US-ILS5-014, direct artifact inspection, conf high] — IL-W-5-NR; military spouses excluded.
- `il.nonres.days_threshold` = **30** days (2026-01-01 → open) [A.2, US-ILS5-014, direct artifact inspection, conf high] — No withholding for nonresident with fewer than 31 days of non-localized IL service; IL-W-6 day certificate when > 30 days expected; carrier rules (air > 50% flight miles). IL resident working only in a withholding state: no IL withholding.

## 2c — Local wage taxes
- `il.local_wage_tax.exists` = False (2026-01-01 → open) [A.2, US-ILP52-001 — promoted to fact in Synthesis C] None administered by IDOR.

## 3 — Social insurance (SUI / SDI / PFML / levies)
Levies: Secure Choice Roth IRA payroll deduction [US-ILP52-002 legacy]; no other levy.

- `il.sdi_pfml.exists` = False (2026-01-01 → open) [A.2, US-ILP52-003 — promoted to fact in Synthesis C] PLAWA is an employer-provided benefit, not a premium.
- `il.sui.wage_base` = **14250** USD (2026-01-01 → 2026-12-31) [A.2, US-ILS5-015, quoted from authority page, conf high] — 2025: 13,916; same values as US-IL-002; 820 ILCS 405/235 formula not read; 2027 expected Dec 2026.
- `il.sui.new_employer.rate` = **3.35** percent (2026-01-01 → 2026-12-31) [A.2, US-ILS5-015, quoted from authority page, conf high] — Administrative Support & Waste Management 3.450%.
- `il.sui.employer.rate.min` = **0.75** percent (2026-01-01 → 2026-12-31) [A.2, US-ILS5-015, quoted from authority page, conf high] — Range 0.750%-7.050% incl. fund builder 0.550%; small-employer option 5.4%; state experience factor 102%.
- `il.sui.employer.rate.max` = **7.05** percent (2026-01-01 → 2026-12-31) [A.2, US-ILS5-015, quoted from authority page, conf high]
- `il.sui.fund_builder.rate` = **0.55** percent (2026-01-01 → 2026-12-31) [A.2, US-ILS5-015, quoted from authority page, conf high]
- `il.sui.employee.rate` = **0** percent (2026-01-01 → open) [A.2, US-ILS5-015, quoted from authority page, conf medium]

## 4 — Payslip statute
- `il.payslip.rules` = **pay stub each pay period; itemized deductions; payroll-card payees also hours, rate, deductions; stubs kept >= 3 years; copies within 21 days on request (max twice/12 months; former employees 1 year after separation); offer prior-year stubs if electronic access ends (115/10, P.A. 103-953)**  (2025-01-01 → open) [A.1, US-ILS5-024, direct artifact inspection, conf high]
- `il.payslip.copy_response_days` = **21** days (2025-01-01 → open) [A.1, US-ILS5-024, direct artifact inspection, conf high]

## 5 — Statutory reporting instruments
- `il.report.wh.il941` = **IL-941 quarterly, electronic, due last day of month after quarter (2026: 04-30, 07-31, 11-02, 2027-02-01); no annual reconciliation**  (2026-01-01 → open) [A.2, US-ILS5-011, quoted from authority page, conf high] — Dates [US-ILS5-012].
- `il.report.wh.deposit` = **monthly (15th) when look-back <= 12,000; semi-weekly (federal Wed/Fri, electronic) when > 12,000; IL-501**  (2026-01-01 → open) [A.2, US-ILS5-011, quoted from authority page, conf high]
- `il.report.wh.semiweekly_threshold` = **12000** USD (2026-01-01 → open) [A.2, US-ILS5-011, quoted from authority page, conf high]
- `il.report.w2` = **electronic only: MyTax (manual, CSV, EFW2 under IDR-996) or bulk EFW2 with ETIN (IDR-986); due Jan 31 (2026 W-2s by 2027-02-01); 1099/W-2G bulk via IRIS (IDR-987) from 2026-09-18**  (2026-09-18 → open) [A.2, US-ILS5-013, quoted from authority page, conf high]
- `il.report.sui.quarterly` = **UI-3/40 wage report + contributions due Apr 30 / Jul 31 / Oct 31 / Jan 31**  (2026-01-01 → open) [A.2, US-ILS5-016, quoted from authority page, conf high]
- `il.report.sui.monthly.employer_threshold` = **25** employees (2026-01-01 → open) [A.2, US-ILS5-017, quoted from authority page, conf high] — Monthly wage report for months 1 and 2 of each quarter: name, SSN, wages; MyTax CSV only (P.A. 97-0689).
- `il.newhire.report_days` = **20** days (2026-01-01 → open) [A.2, US-ILS5-018, quoted from authority page, conf high] — From first day on payroll; rehires and independent contractors.

## 6 — Leave
- `il.leave.plawa.accrual` = **1 h per 40 h worked up to 40 h per 12 months (front-load allowed); use after 90 days; exempt deemed 40 h/week; no separation payout unless in a vacation/PTO bank; tipped/commissioned paid at least full MW; not in Chicago/Cook**  (2024-01-01 → open) [A.3, US-ILS5-019, quoted from authority page, conf medium]
- `il.leave.plawa.cap_hours` = **40** hours (2024-01-01 → open) [A.3, US-ILS5-019, quoted from authority page, conf medium]
- `il.leave.chicago.accrual` = **1 h paid leave AND 1 h paid sick leave per 35 h worked from day 1 for anyone with >= 80 h in 120 days; notices with first paycheck and around July 1**  (2024-07-01 → open) [A.2, US-ILS5-020, quoted from authority page, conf medium] — [partial row] [partial row] caps, carryover and payout unread.

## 7 — Termination and final pay
IDES lists "Employee Separation Information" as an employer obligation [US-ILS5-018]; the notice/form to the employee not identified.

- `il.final_pay.rule` = **in full at separation if possible, no later than next regularly scheduled payday (discharge or resignation); mailed on written request (115/5)**  (2026-01-01 → open) [A.1, US-ILS5-023, second independent authority, conf high]
- `il.final_pay.vacation_payout` = **True**  (2026-01-01 → open) [A.3, US-ILS5-004, quoted from authority page, conf high] — Earned vacation paid at final rate, no forfeiture (CBA exception); use-it-or-lose-it allowed with notice (56 IAC 300.520). No statutory severance.

## 8 — Benefits in kind / taxable wages
- `il.wh.wages.conformity` = **IL withholding follows federal (wages subject to federal withholding); federal exclusions follow; no departure found (not proven)**  (2026-01-01 → open) [A.2, US-ILR3-002, quoted from authority page, conf medium]

## 9 — Deductions and garnishments
- `il.deductions.rule` = **only if required by law, for employee benefit, or wage assignment/order or express written consent at time of deduction; cash advance repayment max 15% per paycheck**  (2026-01-01 → open) [A.3, US-ILS5-006, quoted from authority page, conf medium]
- `il.garn.creditor.max_percent_gross` = **15** percent (2026-01-01 → open) [A.1, US-ILS5-022, derived arithmetically, conf high] — 735 ILCS 5/12-803: lesser of 15% of GROSS or disposable - 45 x greater of federal/IL MW.
- `il.garn.creditor.weekly_floor` = **675** USD (2025-01-01 → open) [A.1, US-ILS5-022, derived arithmetically, conf high] — 45 x 15.00.
- `il.garn.child_support.employer_fee_monthly` = **5** USD (2026-01-01 → open) [A.2, US-ILS5-021, quoted from authority page, conf high] — HFS 3683; remit 1-7 business days after payday; up to 50% of disposable; multiple orders pro rata.

## 10 — Collective agreements / prevailing wage
Prevailing Wage Act 820 ILCS 130: IDOL county rates, certified payroll portal [US-ILP52-004 legacy]. CBA can override vacation payout (115/5).


## 11 — Indexation
State MW not indexed; Chicago July 1 CPI capped 2.5%; Cook July 1 CPI (suspended if County unemployment >= 8.5%); UI base yearly; PIT exemption indexed by IDOR; garnishment floor 45 x MW. Chicago CPI derivation impossible (2025 rate not registered).


## 12 — Payroll data protection / records
No SSN truncation rule found (815 ILCS 505/2RR and 530 not read).

- `il.records.paystub.retention_years` = **3** years (2025-01-01 → open) [A.1, US-ILS5-024, direct artifact inspection, conf high]
- `il.bipa.retention_max_years` = **3** years (2026-01-01 → open) [A.1, US-ILS5-025, direct artifact inspection, conf high] — 740 ILCS 14/15: written policy, destroy within 3 years of last interaction; notice + written release before collection (biometric time clocks).

## 13 — Live legal change
- `il.live.14c_end` = **14(c) sub-minimum licences end 2029-12-31 (enacted)**  (2029-12-31 → open) [A.2, US-ILS5-002, quoted from authority page, conf high]

## Oracle — worked examples (C37)
- `il.oracle.il700t.example1.withholding` = **8.38** USD (2026-01-01 → 2026-12-31) [A.2, US-ILR3-001, quoted from authority page, conf high] — IL-700-T: 300 weekly, 2 + 1 allowances.
- `il.oracle.il700t.example2.withholding` = **32.13** USD (2026-01-01 → 2026-12-31) [A.2, US-ILR3-001, derived arithmetically, conf high] — 800 weekly, 2 + 2 allowances: 7,850/52 = 150.96; 649.04 x .0495 = 32.13.

## Special populations (US-OWN-005)
- Domestic: MW Law even under 4 employees; IL withholding only if federal withheld voluntarily [US-ILS5-026, US-ILR3-002].
- Agricultural: no state OT; small farms (<= 500 man-days/quarter), family, some piece-rate harvesters outside MW [US-ILS5-001, US-ILS5-026].
- Minors: 13.00 under 18 <= 650 h/yr; Cook ordinance not under 18 [US-ILS5-001, US-ILS5-009].
- Tipped: state 9.00; Chicago 12.96; Cook 9.25; PLAWA paid at full MW [US-ILS5-001, US-ILS5-008, US-ILS5-009, US-ILS5-019].
- Clergy: religious organisation members outside MW; ministers no IL withholding [US-ILS5-026, US-ILS5-014].
- Students: own-college students outside MW; part-time college students at own school PLAWA-exempt [US-ILS5-026, US-ILS5-019].
- NRAs / statutory employees: follow federal [US-ILR3-002].
- Government: IWPCA excludes State and federal employees; MW covers governmental bodies; UI reimbursement option [US-ILS5-003, US-ILS5-001, US-ILS5-016].
- Other-state residents: reciprocity IA/KY/MI/WI, 30-day rule, IL-W-6 [US-ILS5-014].

## Language seams (US-OWN-006)
No language requirement [US-ILP9L-001]; payslip English (US-OWN-006).

## Open questions
Mirrors `unresolved[]` in the facts file (same keys).

- `il.leave.chicago.paid_leave.payout` (blocking) — Chicago Paid Leave caps, carryover and separation payout by employer size not read (partial row). **Would close it:** BACP FAQ PDF or OLS Paid Leave rules (browser pass) or MCC 6-130.
- `il.leave.cook.paid_leave` (blocking) — Cook County Paid Leave Ordinance not read. **Would close it:** Cook County Commission on Human Rights Paid Leave FAQ (cookcountyil.gov).
- `il.local_minwage.chicago.tipped_schedule` (non-blocking) — One Fair Wage phase-out percentage for 2026 not read (12.96 = 76% of 17.05). **Would close it:** MCC 6-105-020 text or BACP 2026 notice.
- `il.termination.ui_separation_notice` (non-blocking) — Whether Illinois requires a separation notice to the employee not identified. **Would close it:** 56 Ill. Adm. Code 2770 / 820 ILCS 405 via ftp.ilga.gov or the IDES employer handbook.
- `il.pit.rate.statutory` (non-blocking) — 35 ILCS 5/201(b)(5.4) not read; no 2027 change confirmed. **Would close it:** ftp.ilga.gov/ILCS/Ch 0035/Act 0005 section 201 + IDOR news.
- `il.sui.wage_base.next_year` (non-blocking) — 2027 wage base unpublished; 405/235 formula not read. **Would close it:** IDES 2027 rate chart (Dec 2026) and 820 ILCS 405/235 via ftp.ilga.gov.
- `il.payslip.content_list` (non-blocking) — 56 Ill. Adm. Code 300.600 content items not read. **Would close it:** ftp.ilga.gov/JCAR Title 56 Part 300.
- `il.data_protection.ssn_paystub` (non-blocking) — 815 ILCS 505/2RR and 815 ILCS 530 not read. **Would close it:** Those sections via ftp.ilga.gov.
- `il.pit.conformity_statement` (non-blocking) — No IDOR decoupling statement (HSA, 125) read. **Would close it:** IDOR Pub. 101 / IL-1040 subtraction list.
- `il.live.news_sweep` (non-blocking) — IDOL/IDOR/IDES newsrooms 2026 not swept. **Would close it:** One sweep of tax.illinois.gov/research/news.html, labor.illinois.gov/news.html, ides.illinois.gov newsroom.

# CCG annex_IA research pack — Iowa

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B, 2026-11-02. Source: `_research/stage5/IA.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_IA-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** Minimum wage 7.25 (6.35 first 90 days); local mandates void (364.3(12)); FLSA overtime. Flat 3.8% PIT; 2026 withholding formula T1=G-D, x3.80%, less W/P, + A, computed TO THE CENT (correction: not whole dollar as US-IA-001 and the MANDATE currency block say); supplemental 3.8%; reciprocity with IL only; school/EMS surtaxes at assessment. UI employer-only, base 20,400 (2026) / 21,100 (2027) after SF 607, max 5.4%, new 1.0%; other-state wages do NOT count. Pay statement 91A.6. New hire within 15 days. Oracle: IDR formula PDF examples.

## 1 — Employment / labour code
No state overtime rule: ch. 91D adopts FLSA (negative on 91D.1 only, 85%). HF 2212 not enacted.

- `ia.minwage.hourly` = **7.25** USD (2008-01-01 → open) [A.1, US-IAS5-001, direct artifact inspection, conf high] — 91D.1(1)(a),(b): or federal if higher; enterprises under 300,000 gross exempt (not laundries, construction, hospitals, care, schools, public agencies). Not indexed.
- `ia.minwage.first_90_days.hourly` = **6.35** USD (2008-01-01 → open) [A.1, US-IAS5-001, direct artifact inspection, conf high]
- `ia.local_mandates.preempted` = **True**  (2017-03-30 → open) [A.1, US-IAS5-021, direct artifact inspection, conf high] — 364.3(12): no city minimum/living wage, leave, benefits or scheduling ordinances.
- `ia.pay_frequency.rule` = **at least monthly, semimonthly or biweekly on designated paydays; payday at most 12 days after period end excluding Sundays/holidays; written agreement may vary; commissions true-up at least every 12 months (91A.3(1))**  (2026-01-01 → open) [A.1, US-IAS5-002, direct artifact inspection, conf high]
- `ia.payment.method` = **US currency or negotiable instrument; in kind with written consent; direct deposit may be a condition of employment for hires from 2005-07-01 (3 exceptions); employer pays overdraft charges from late pay; expenses reimbursed within 30 days**  (2026-01-01 → open) [A.1, US-IAS5-002, direct artifact inspection, conf high]
- `ia.late_wages.liquidated_damages_percent_per_day` = **5** percent (2026-01-01 → open) [A.1, US-IAS5-027, direct artifact inspection, conf high] — 91A.2(6): excluding Sundays, holidays and first 7 days; capped at unpaid amount.
- `ia.minor.under16.school_week_max_hours` = **28** hours (2026-01-01 → open) [A.1, US-IAS5-014, direct artifact inspection, conf high] — 92.7: 7am-9pm (11pm June-Labor Day); 8 h/day, 40 h/week; 6 h/day and 28 h/week in session; 30-min break for 5+ h.

## 2 — Income tax (state withholding)
- `ia.pit.rate.flat` = **3.8** percent (2025-01-01 → open) [A.1, US-IAS5-006, direct artifact inspection, conf high] — 422.5(1)(a); nonresident fraction at assessment; resident credit at assessment.
- `ia.wh.method` = **T1 = G - D; T2 = T1 x 3.80%; T3 = T2 - W/P; T4 = T3 + A (2026 formula, released Nov 2025); tables alternative (register US-IAS5-015)** (2026-01-01 -> 2026-12-31) [A.2, US-IAS5-005, derived arithmetically, conf high] - Six 2024+ IA W-4 examples re-derived in Python to the cent. P: daily 260, weekly 52, biweekly 26, semimonthly 24, monthly 12.
- `ia.wh.formula.rate` = **3.8** percent (2026-01-01 -> 2026-12-31) [A.2, US-IAS5-005, quoted from authority page, conf high] - Rate applied at step T2 of the 2026 withholding formula. LEVEL: withholding.
- `ia.wh.rounding` = **to the cent, half-up (no whole-dollar rounding in 2026)**  (2026-01-01 → 2026-12-31) [A.2, US-IAS5-005, derived arithmetically, conf high] — Tables Step 5: "rounded to the nearest cent" [US-IAS5-015]. Supersedes the rounding clause of US-IA-001 and the MANDATE currency block listing IA as whole-dollar (S5A-MERGE note on US-IA-001).
- `ia.wh.deduction.other` = **13000** USD (2026-01-01 → 2026-12-31) [A.2, US-IAS5-005, derived arithmetically, conf high] — Other / MFJ spouse with income / missing status; weekly 250, biweekly 500, semimonthly 541.67, monthly 1,083.33, daily 50. Pre-2024 W-4: Single 13,000, Married 26,000, W = allowances x 40.
- `ia.wh.deduction.hoh` = **19500** USD (2026-01-01 → 2026-12-31) [A.2, US-IAS5-005, derived arithmetically, conf high] — Derivation recorded in register row US-IAS5-005: T1 = G - D; T2 = T1 x 3.80%; T3 = T2 - W/P; T4 = T3 + A. D per period (2024+ IA W-4): col A Other / MFJ spouse with earned income / missing: annual 13,000 (weekly 250, biweekly 500, semimonthly 541.67, monthly 1,083.33, daily 50); col B Head of Household: annual 19,500 (biweekly 750, monthly 1,625);
- `ia.wh.deduction.mfj_one_earner_qss` = **26000** USD (2026-01-01 → 2026-12-31) [A.2, US-IAS5-005, derived arithmetically, conf high] — Derivation recorded in register row US-IAS5-005: T1 = G - D; T2 = T1 x 3.80%; T3 = T2 - W/P; T4 = T3 + A. D per period (2024+ IA W-4): col A Other / MFJ spouse with earned income / missing: annual 13,000 (weekly 250, biweekly 500, semimonthly 541.67, monthly 1,083.33, daily 50); col B Head of Household: annual 19,500 (biweekly 750, monthly 1,625);
- `ia.wh.allowance.per_dependent` = **40** USD (2026-01-01 → open) [A.2, US-IAS5-029, direct artifact inspection, conf high] — 2026 IA W-4 44-019a (11/13/2025); due within 15 days of hire; none on file = zero allowances; keep 4 years; new W-4 within 10 days when allowances decrease.
- `ia.wh.supplemental.rate` = **3.8** percent (2026-01-01 → open) [A.2, US-IAS5-016, second independent authority, conf high] — 422.16(2)(e) and 701 IAC 307.2(1)(c) [US-IAS5-006]: when treated separately and federal withheld at flat rate; otherwise aggregate.
- `ia.wh.exempt.threshold.single_under65` = **9000** USD (2026-01-01 → open) [A.2, US-IAS5-016, quoted from authority page, conf high] — 13,500 MFJ/HoH under 65; 32,000 / 24,000 at 65+; nonresidents may not claim EXEMPT.
- `ia.wh.exempt.threshold.mfj_hoh_under65` = **13500** USD (2026-01-01 → open) [A.2, US-IAS5-016, quoted from authority page, conf high]
- `ia.pit.obbba` = **tips, overtime, car-loan interest conformed at ASSESSMENT only (no withholding allowance); senior deduction (up to 6,000) may be claimed as an IA W-4 allowance**  (2026-01-01 → open) [A.2, US-IAS5-019, quoted from authority page, conf high]

## 2b — Non-resident regime and reciprocity
- `ia.reciprocity.states` = **IL**  (2026-01-01 → open) [A.2, US-IAS5-016, quoted from authority page, conf high] — IL resident in IA files 44-016 (employer withholds IL); IA resident in IL files IL-W-5-NR [US-MULTI-018]. Nonresidents otherwise withheld at resident rate from first day (no threshold); exceptions interstate carriers, film/TV (44-017), disaster workers (29C.24).

## 2c — Local wage taxes
- `ia.local.surtax.withheld` = **False**  (2026-01-01 → open) [A.2, US-IAS5-029, direct artifact inspection, conf high] — School-district and EMS surtaxes settled on IA 1040 by residence; employee may adjust allowances/line 8 [US-IAP51-005, US-IAP52-001].

## 3 — Social insurance (SUI / SDI / PFML / levies)
No SDI/TDI/PFML [US-IAP52-004 legacy; mandate US-MQ-32]. 260E/260F training items are credits diverting withholding (NJC 1.5%/3%, SJC 1.5%, ACE up to 10%, TJC 3%), claimed on the quarterly return - not levies [US-IAS5-016]. 2027 rate table unpublished.

- `ia.sui.wage_base` = **20400** USD (2026-01-01 → 2026-12-31) [A.2, US-IAS5-009, derived arithmetically, conf high] — 96.1A(36) as amended by SF 607: 1/3 of AAW rounded up to next 100, not below FUTA: 61,098.90/3 = 20,366.30 -> 20,400 [US-IAS5-008]. 2025: 39,500.
- `ia.sui.wage_base` = **21100** USD (2027-01-01 → open) [A.2, US-IAS5-010, derived arithmetically, conf high] — Announced 2026-06-30: 63,213.58/3 = 21,071.19 -> 21,100.
- `ia.sui.employer.rate.max` = **5.4** percent (2026-01-01 → 2026-12-31) [A.2, US-IAP9V-001, quoted from authority page, conf high] — Table D, ranks 1-9, 0.000%-5.400% (max cut from 9%, tables 8 -> 4).
- `ia.sui.employer.rate.min` = **0** percent (2026-01-01 → 2026-12-31) [A.2, US-IAP9V-001, quoted from authority page, conf high]
- `ia.sui.new_employer.rate` = **1.0** percent (2026-01-01 → 2026-12-31) [A.1, US-IAS5-011, direct artifact inspection, conf high] — Non-construction: rank-4 rate but not less than 1.000% until 12 chargeable quarters; construction rank 9 = 5.400%.
- `ia.sui.new_employer.construction.rate` = **5.4** percent (2026-01-01 → 2026-12-31) [A.1, US-IAS5-011, direct artifact inspection, conf high]
- `ia.sui.employee.rate` = **0** percent (2026-01-01 → open) [A.1, US-IAS5-024, direct artifact inspection, conf high] — 871 IAC 23.6(2).
- `ia.sui.wage_base.other_state_credit` = **False**  (2026-01-01 → open) [A.1, US-IAS5-024, direct artifact inspection, conf high] — 23.6(3): only wages reported to Iowa UI count; successor with experience transfer may count predecessor wages (23.6(4)). Reported tips are UI wages (23.5).

## 4 — Payslip statute
- `ia.payslip.items` = **hours worked, wages earned, deductions made, each regular payday (91A.6(4)); mail, secure electronic, workplace or view access, no separate consent; itemised computation within 10 working days on request**  (2026-01-01 → open) [A.1, US-IAS5-027, direct artifact inspection, conf medium] — Statute row is legacy US-IAP51-002; reach follows Iowa work location (91A.2(3),(4)).

## 5 — Statutory reporting instruments
- `ia.report.wh.filer_class` = **quarterly < 6,000/yr and <= 500/month; monthly 6,000-120,000 (15th); semimonthly > 5,000 per semimonthly period (25th / 10th, electronic); annual election <= 2 employees; quarterly return last day of month after quarter via GovConnectIowa, zero returns required**  (2026-01-01 → open) [A.2, US-IAS5-016, quoted from authority page, conf high] — 422.16(4) [US-IAS5-007].
- `ia.report.annual_reconciliation.exists` = **False**  (2026-01-01 → open) [A.2, US-IAS5-017, quoted from authority page, conf high] — VSPs no longer required.
- `ia.report.w2` = **e-file via GovConnectIowa by February 15 only W-2/1099 with IA withholding; IDR-unique 512-byte EFW2-based format (SSA file rejected); RS state code 19, permit 248-267; IA RV record; Key & Send; employee copy Jan 31, terminated on request within 30 days**  (2023-01-09 → open) [A.2, US-IAS5-018, direct artifact inspection, conf medium] — Spec page dated 2023-01-09 (TY2023-2025); TY2026 edition not seen.
- `ia.report.sui.quarterly` = **Employer Contribution and Payroll Report 65-5300 + wage detail by SSN, electronic, due last day of month after quarter (871 IAC 23.8(1))**  (2026-01-01 → open) [A.1, US-IAS5-024, direct artifact inspection, conf high]
- `ia.newhire.report_days` = **15** days (2026-01-01 → open) [A.1, US-IAS5-012, direct artifact inspection, conf high] — 252G.3: employer name/address/FEIN; employee name/address/SSN/DOB; dependent health coverage availability and date; IWO address; independent contractors too.

## 6 — Leave
- `ia.leave.sick.state_mandate.exists` = **False**  (2026-01-01 → open) [A.1, US-IAS5-021, direct artifact inspection, conf medium]

## 7 — Termination and final pay
- `ia.final_pay.rule` = **next regular payday for the period in which wages were earned (no discharge/resignation distinction); commission true-up within 30 days; vacation only per agreement/pro-rata policy (91A.4)**  (2026-01-01 → open) [A.1, US-IAS5-003, direct artifact inspection, conf high]
- `ia.separation.wage_request_response_days` = **10** days (2026-01-01 → open) [A.3, US-IAS5-026, quoted from authority page, conf medium] — No separation notice statute; IWD Notice of Separation and Wage Request answered within 10 days.

## 8 — Benefits in kind / taxable wages
- `ia.pit.conformity` = **rolling IRC conformity from TY2023; withholding on same wages as federal; 401(k)/125/HSA/transit/GTL follow federal**  (2023-01-01 → open) [A.2, US-IAS5-020, quoted from authority page, conf medium]

## 9 — Deductions and garnishments
- `ia.deductions.rule` = **required by law, court order, or written authorisation for employee benefit; prohibited: shared till shortages, dishonoured checks, non-wilful breakage, lost non-assigned property, gratuities, PPE, relocation over 20 (91A.5)**  (2026-01-01 → open) [A.1, US-IAS5-004, direct artifact inspection, conf high]
- `ia.garn.creditor.annual_cap_schedule` = **per judgment creditor by expected annual earnings: < 12,000: 250; 12,000-16,000: 400; 16,000-24,000: 800; 24,000-35,000: 1,500; 35,000-50,000: 2,000; >= 50,000: 10% (plus CCPA)**  (2026-01-01 → open) [A.1, US-IAS5-013, direct artifact inspection, conf high] — 642.21; not for support; not indexed.
- `ia.garn.child_support.employer_fee` = **2** USD (2026-01-01 → open) [A.1, US-IAS5-022, direct artifact inspection, conf high] — 252D.17: per payment within CCPA; IWO priority; remit to CSC within 7 business days.
- `ia.garn.child_support.remit_business_days` = **7** business days (2026-01-01 → open) [A.1, US-IAS5-022, direct artifact inspection, conf high]

## 10 — Collective agreements / prevailing wage
No state prevailing-wage law (DOL WHD list 2023) [US-IAP51-001 legacy].


## 11 — Indexation
UI base 1/3 AAW yearly (late-June release); rate table by fund formula; PIT flat not indexed (deduction amounts reissued each November); MW and garnishment brackets fixed.


## 12 — Payroll data protection / records
- `ia.breach.notice` = **without unreasonable delay; processor notifies owner immediately (715C.2)**  (2026-01-01 → open) [A.1, US-IAS5-023, direct artifact inspection, conf high]

## 13 — Live legal change
SF 607 in force CY2026 (employer UI level); 2027 base 21,100; 2026 formula/IA W-4 (withholding); OBBBA deductions (assessment); sports wagering 3.8% (non-wage). Full 2026 Acts sweep not done.

- `ia.live.hf2212.status` = **NOT enacted (introduced 2026-01-29, referred House HHS): direct-care minimum 20.00 - do not model**  (2026-01-29 → open) [A.1, US-IAS5-028, direct artifact inspection, conf high]

## Oracle — worked examples (C37)
- `ia.oracle.formula.example6.withholding` = **114.92** USD (2026-01-01 → 2026-12-31) [A.2, US-IAS5-005, derived arithmetically, conf medium] — Formula PDF example 6 (monthly 5,000, HoH, W = 160) printed WITHOUT its final figure; derived 114.92 = (5,000 - 1,625) x 3.8% - 160/12. The other examples (e.g. 59.26, 38.72, 145.50) are printed and reproduced to the cent.

## Special populations (US-OWN-005)
- Domestic: generally excluded from IA withholding; UI at 1,000/quarter [US-IAS5-016, US-IAS5-025].
- Agricultural: withholding follows federal; UI 20,000/quarter or 10+ in 20 weeks [US-IAS5-016, US-IAS5-025, US-IAS5-027].
- Minors: no youth rate beyond 90-day rate; under-16 hours; child under 18 for parent UI-excluded [US-IAS5-001, US-IAS5-014, US-IAS5-025].
- Tipped: tip credit up to 40% of MW (cash wage 4.35 derived on 7.25) for restaurants/hotels/motels/inns/cabins with > 30/month tips; tips UI wages; OBBBA tip deduction at assessment [US-IAS5-001, US-IAS5-024].
- Clergy: excluded from IA withholding; church service excluded from UI [US-IAS5-016, US-IAS5-025].
- Students: own-school and curricular work UI-excluded [US-IAS5-025].
- NRAs: IDR additional withholding guidance (15,000 or 29,200 / P x 3.8%) via line 8; no EXEMPT [US-IAS5-016, US-IAS5-029].
- Statutory employees: follow federal [US-IAS5-016].
- Government: withholding agents; reimbursing UI employers; ch. 91D applies [US-IAS5-025].
- Military spouses: MSRRA/VBTA box [US-IAS5-016, US-IAS5-029]. Interstate transport nonresidents: no IA withholding. New employees first 90 days: 6.35. Corporate officers: UI employees.

## Language seams (US-OWN-006)
No language rule; payslip English [US-IAL-001, US-IAP9L-001, US-IAP9L-002] (US-OWN-006).

## Open questions
Mirrors `unresolved[]` in the facts file (same keys).

- `ia.wh.rounding.history` (non-blocking) — US-IA-001 and the MANDATE currency block say whole-dollar; 2026 formula/tables say nearest cent. The 2025 formula was not read. **Would close it:** Synthesis supersedes the rounding clause of US-IA-001 by US-IAS5-005/-015 (done in S5A note); optionally IDR 2025 formula PDF. Scaffolder to amend the MANDATE currency block (US-MQ-01).
- `ia.sui.rate_table.next_year` (non-blocking) — CY2027 rate table not yet published. **Would close it:** IWD "Information on Rate Computations for Private Employers 2027" or November 2026 rate notices.
- `ia.report.sui.file_format` (non-blocking) — myIowaUI quarterly wage-detail upload layout not acquired. **Would close it:** IWD myIowaUI file specification (UI Tax Bureau, iwduitax@iwd.iowa.gov).
- `ia.report.w2.spec_next_edition` (non-blocking) — IDR W-2 spec covers TY2023-2025 filed in 2026. **Would close it:** IDR TY2026 edition on the same URL (late 2026).
- `ia.live.acts_2026_sweep` (non-blocking) — Full sweep of 2026 enrolled Acts touching chs. 91A, 91D, 92, 96, 252D, 422, 642 not done. **Would close it:** Iowa Legislature Acts and Joint Resolutions 2026 list or Iowa Code 2027 supplement.
- `ia.data_protection.ssn_paystub` (non-blocking) — Iowa Code 715A not read. **Would close it:** Iowa Code 715A.10 and 715A.8 text.
- `ia.garn.state_tax_levy` (non-blocking) — IDR wage-levy procedure not read. **Would close it:** Iowa Code 422.26 / 626 levy provisions or the IDR levy page.
- `ia.overtime.state_rule` (non-blocking) — Negative rests on 91D.1 only. **Would close it:** DIAL Labor Services wage-hour FAQ or the rest of ch. 91D.
- `ia.leave.jury_military` (non-blocking) — Not researched. **Would close it:** Iowa Code 607A.45 and 29A.43.

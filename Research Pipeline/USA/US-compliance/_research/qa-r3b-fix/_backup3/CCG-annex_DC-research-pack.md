# CCG annex_DC research pack — District of Columbia

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B, 2026-11-02. Source: `_research/stage5/DC.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_DC-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** Minimum wage 17.95 -> 18.40 (2026-07-01, CPI Washington MSA); tipped wage 10.30 = 56% of the minimum, rising to 75% by 2034; non-hotel tipped employers must use a third-party payroll business. Income tax withheld by a percentage method/tables with no standard deduction in withholding; the 2026 method after D.C. Act 26-416 (personal exemptions repealed) is UNPUBLISHED and the D-4/D-4A are "under review" (blocking open question). Nonresidents not taxed (Home Rule Act, D-4A). SUI base 9,000, new 2.7%, +0.2% admin assessment; PFL 0.75% employer-only, no cap. Itemised pay statement with tip lines and, from 2026, compensation sources. Overall confidence 85%.

## 1 — Employment / labour code
- `dc.minwage.hourly` = **17.95** USD (2025-07-01 → 2026-06-30) [A.2, US-DCS5-011, derived arithmetically, conf high] — Derivation recorded in register row US-DCS5-011: Minimum wage 17.95 USD/h (2025-07-01 to 2026-06-30) -> 18.40 USD/h from 2026-07-01, all employers regardless of size; CPI (Washington MSA) increase 2025 = 2.4%. Tipped base wage 10.00 -> 10.30 from 2026-07-01, employer pays any shortfall to the full minimum (weekly average). Derivation: 17.95 x 1.02
- `dc.minwage.hourly` = **18.4** USD (2026-07-01 → open) [A.2, US-DCS5-011, derived arithmetically, conf high] — G-DERIVE: 17.95 x 1.024 (CPI-U Washington MSA) = 18.3808 -> 18.40 (nearest 0.05) [US-DCS5-001, 32-1003(a)(6)]. 2027 due by ~June 2027.
- `dc.minwage.tipped.cash_wage` = **10.0** USD (2024-07-01 → 2026-06-30) [A.2, US-DCS5-011, derived arithmetically, conf high] — Derivation recorded in register row US-DCS5-011: Minimum wage 17.95 USD/h (2025-07-01 to 2026-06-30) -> 18.40 USD/h from 2026-07-01, all employers regardless of size; CPI (Washington MSA) increase 2025 = 2.4%. Tipped base wage 10.00 -> 10.30 from 2026-07-01, employer pays any shortfall to the full minimum (weekly average). Derivation: 17.95 x 1.02
- `dc.minwage.tipped.cash_wage` = **10.3** USD (2026-07-01 → open) [A.2, US-DCS5-011, derived arithmetically, conf high] — = 56% x 18.40 = 10.304 -> 10.30; employer tops up weekly shortfall.
- `dc.minwage.tipped.percent_of_minimum` = **56** percent (2026-07-01 → 2028-06-30) [A.1, US-DCS5-001, direct artifact inspection, conf high] — D.C. Law 26-55 s.2222(a): 56% from 2026-07-01, 60% 2028, 65% 2030, 70% 2032, 75% 2034.
- `dc.minwage.tipped.percent_of_minimum` = **60** percent (2028-07-01 → 2030-06-30) [A.1, US-DCS5-001, direct artifact inspection, conf high]
- `dc.minwage.tipped.percent_of_minimum` = **65** percent (2030-07-01 → 2032-06-30) [A.1, US-DCS5-001, direct artifact inspection, conf high]
- `dc.minwage.tipped.percent_of_minimum` = **70** percent (2032-07-01 → 2034-06-30) [A.1, US-DCS5-001, direct artifact inspection, conf high]
- `dc.minwage.tipped.percent_of_minimum` = **75** percent (2034-07-01 → open) [A.1, US-DCS5-001, direct artifact inspection, conf high]
- `dc.tipped.third_party_payroll.required` = **True**  (2025-12-06 → open) [A.1, US-DCS5-010, direct artifact inspection, conf high] — 32-1008(a-1): employers paying the tipped wage, other than hotels.
- `dc.minwage.coverage` = **> 50% of working time in DC, or DC-based with substantial DC time and <= 50% in any one state; any employee with >= 2 h in DC in a workweek gets DC MW for DC hours (32-1003(b),(b-1))**  (2026-01-01 → open) [A.1, US-DCS5-001, direct artifact inspection, conf high]
- `dc.overtime.weekly_threshold_hours` = **40** hours (2026-01-01 → open) [A.1, US-DCS5-001, direct artifact inspection, conf high] — 1.5x over 40; no daily OT; retail/service commission exemption.
- `dc.pay_frequency.rule` = **at least twice per calendar month on paydays designated in advance; EAP or contract/custom monthly; at most 10 working days from period end to payday**  (2026-01-01 → open) [A.1, US-DCS5-002, direct artifact inspection, conf high]
- `dc.payment.method` = **lawful US money or checks payable on demand (32-1302); no DC direct-deposit/paycard statute found**  (2026-01-01 → open) [A.1, US-DCS5-002, direct artifact inspection, conf medium]

## 2 — Income tax (state withholding)
TRAP (brief): DC 2026 withholding method is unpublished. 47-1812.08 is unchanged, but D.C. Act 26-416 repealed personal exemptions (the old D-4 allowance basis) and the D-4/D-4A are under review. Until OTR publishes, the only published instruction is Notice 2022-08 (rate schedule with federal allowance amount) - an inference for 2026; the engine must flag this. No flat supplemental rate: bonuses withheld as regular wages [US-DCR3-001, US-DCR3-002].

- `dc.pit.rate_schedule` = <=10,000 4%; 10,000-40,000 400+6%; 40,000-60,000 2,200+6.5%; 60,000-250,000 3,500+8.5%; 250,000-500,000 19,650+9.25%; 500,000-1,000,000 42,775+9.75%; >1,000,000 91,525+10.75% (2022-01-01 → open) [A.2, US-DCP52-001 — promoted to fact in Synthesis C] Base amounts re-derived in Python (match). Not indexed.
- `dc.wh.notice_2022_08` = apply current rate schedule with the federal allowance amount (no FR-230 after 2018); applying to 2026 is an inference (2022-01-01 → open) [A.2, US-DCP51-002 — promoted to fact in Synthesis C]
- `dc.wh.statutory_method` = **percentage method or tables similar to IRC 3402; no standard-deduction allowance in withholding; wages may be computed to nearest dollar (47-1812.08(b))**  (2026-01-01 → open) [A.1, US-DCS5-025, direct artifact inspection, conf high]
- `dc.wh.lump_sum_retirement.rate` = **10.75** percent (2026-01-01 → open) [A.1, US-DCS5-025, direct artifact inspection, conf high] — Resident lump-sum retirement distributions at highest rate (47-1812.08(m), amended by D.C. Law 26-89 / Act 26-214).
- `dc.wh.certificate.status` = **D-4 and D-4A marked "currently under review" on the OTR forms page, no fill-in link**  (2026-11-02 → open) [A.2, US-DCS5-013, direct artifact inspection, conf high]
- `dc.pit.personal_exemption.repealed` = **True**  (2025-01-01 → open) [A.1, US-DCS5-021, direct artifact inspection, conf high] — D.C. Act 26-416 (emergency, in force 2026-08-13 for <= 90 days, ~to 2026-11-11); tax subtitle as of 2025-01-01; DC standard deduction 15,000 / 22,500 / 30,000 for 2025, COLA from 2026 rounded down to 50. Operating level ASSESSMENT; no change to 47-1812.08.
- `dc.pit.obbba_deductions` = **disallowed TY2025; allowed as DC deductions from TY2026; operating level assessment only (no withholding change)**  (2026-01-01 → open) [A.1, US-DCS5-021, direct artifact inspection, conf high]

## 2b — Non-resident regime and reciprocity
DC exempts all nonresidents (Home Rule Act); MD and VA appear in the MULTI matrix because they exempt DC residents [US-MULTI-016].

- `dc.nonres.taxable` = False (2026-01-01 → open) [A.1, US-DCP51-006 — promoted to fact in Synthesis C] Home Rule Act bars taxing nonresidents; D-4A stops DC withholding; resident credit for other-state tax at assessment.

## 2c — Local wage taxes
None: DC is itself the local layer.


## 3 — Social insurance (SUI / SDI / PFML / levies)
- `dc.sui.wage_base` = **9000** USD (2026-01-01 → open) [A.1, US-DCS5-017, direct artifact inspection, conf high] — 51-103(e)(6); fixed. No explicit other-state credit found (open).
- `dc.sui.new_employer.rate` = **2.7** percent (2026-01-01 → open) [A.2, US-DCS5-016, second independent authority, conf high]
- `dc.sui.employer.rate.min` = **1.9** percent (2026-01-01 → open) [A.1, US-DCS5-017, direct artifact inspection, conf high] — Tax Table VI 1.9%-7.4% (51-103(c)(8)(A)).
- `dc.sui.employer.rate.max` = **7.4** percent (2026-01-01 → open) [A.1, US-DCS5-017, direct artifact inspection, conf high]
- `dc.sui.admin_assessment.rate` = **0.2** percent (2026-01-01 → open) [A.1, US-DCS5-017, direct artifact inspection, conf high] — (m)(1) administrative funding assessment on taxable wages [US-DCB5-401]. 0.1% interest surcharge (l)(1) billing in 2026 unconfirmed [US-DCP7-003].
- `dc.sui.employee.rate` = **0** percent (2026-01-01 → open) [A.1, US-DCS5-017, direct artifact inspection, conf high] — Contributions may not be deducted from wages (d).
- `dc.pfl.employer.rate` = **0.75** percent (2024-07-01 → open) [A.2, US-DCS5-019, second independent authority, conf high] — 100% employer-funded, not deductible from pay, no wage cap (US-DCS5-020). History: 0.62% to 2022-Q2, 0.26% to 2024-Q2.
- `dc.pfl.wage_cap.exists` = **False**  (2026-01-01 → open) [A.1, US-DCS5-020, direct artifact inspection, conf high]
- `dc.pfl.coverage` = **> 50% of work time in DC, or DC-based with substantial DC time and <= 50% elsewhere (32-541.01(3)); not by residence**  (2026-01-01 → open) [A.1, US-DCS5-007, direct artifact inspection, conf high]
- `dc.pfl.benefit.weekly_max` = **1100** USD (2026-10-01 → open) [A.1, US-DCS5-021, direct artifact inspection, conf high] — D.C. Act 26-416 (emergency); CPI-indexed thereafter; durations parental 12 / family 6 / medical 10 / pre-natal 2 weeks for claims 2026-10-01..2030-09-30. Benefit side, not payroll.

## 4 — Payslip statute
Electronic delivery: no DC rule found. Reach follows 32-1003(b)/(b-1) coverage (inference).

- `dc.payslip.items` = **date of payment; gross wages; deductions and additions with separate gratuities line; net wages; hours worked; tip-declaration form split cash/card; from 2026-01-01 list of compensation sources beyond base wages and tips**  (2026-01-01 → open) [A.1, US-DCS5-010, direct artifact inspection, conf high] — 32-1008(b), (b)(6A).
- `dc.hire_notice.language` = **English and also the employee primary language where a Mayor template exists (32-1008(c))**  (2026-01-01 → open) [A.1, US-DCS5-010, direct artifact inspection, conf high]

## 5 — Statutory reporting instruments
- `dc.report.wh.fr900q` = **FR-900Q electronic on MyTax.DC.gov (mandatory since TY2023); deposits weekly/semi-weekly/monthly/quarterly as assigned by 20th of following month; returns due Apr 30, Jul 31, Oct 31, Jan 31; zero return required; payments over 5,000 electronic (ACH code 00300); FR-900A annual if under 200/yr**  (2026-01-01 → open) [A.2, US-DCS5-014, direct artifact inspection, conf high]
- `dc.report.w2` = **EFW2/EFW2C with required RS record via MyTax.DC.gov; mandatory electronic at 25+ forms (else paper with WT or manual entry); due January 31**  (2025-01-01 → open) [A.2, US-DCS5-015, direct artifact inspection, conf medium] — TY2025 edition read; TY2026 not yet published.
- `dc.report.w2.efile_threshold` = **25** forms (2025-01-01 → open) [A.2, US-DCS5-015, direct artifact inspection, conf high]
- `dc.report.sui.quarterly` = **UC-30 via DOES ESSP, due last day of month after quarter; household annual April 15; 250+ employees machine-readable; penalty 10% (min 100), interest 1.5%/month**  (2026-01-01 → open) [A.1, US-DCS5-018, direct artifact inspection, conf high]
- `dc.report.pfl.quarterly` = **same ESSP channel and due dates (Apr 30, Jul 31, Oct 31, Jan 31)**  (2026-01-01 → open) [A.2, US-DCS5-019, second independent authority, conf high]
- `dc.newhire.report_days` = **20** days (2026-01-01 → open) [A.1, US-DCS5-022, direct artifact inspection, conf high] — dc-newhire.com online/mail/fax; employee name/address/SSN, employer name/address/FEIN, hire date; penalty 25/employee.

## 6 — Leave
- `dc.leave.sick.accrual.100_plus` = **1 h per 37 h worked, up to 7 days/yr**  (2026-01-01 → open) [A.1, US-DCS5-004, direct artifact inspection, conf high] — 25-99: 1/43 up to 5 days; <=24: 1/87 up to 3 days; tipped restaurant/bar 1/43 up to 5 days at full MW; use after 90 days; reinstated on rehire within 1 year.
- `dc.leave.sick.accrual.25_99` = **1 h per 43 h worked, up to 5 days/yr**  (2026-01-01 → open) [A.1, US-DCS5-004, direct artifact inspection, conf high]
- `dc.leave.sick.accrual.under_25` = **1 h per 87 h worked, up to 3 days/yr**  (2026-01-01 → open) [A.1, US-DCS5-004, direct artifact inspection, conf high]
- `dc.leave.sick.payout_on_separation` = **False**  (2026-01-01 → open) [A.3, US-DCS5-024, second independent authority, conf medium]

## 7 — Termination and final pay
Accrued vacation payout: no statutory rule (policy). UI separation notice: no DC form found.

- `dc.final_pay.rule` = **discharge: working day after (4 days if employee handled employer money); resignation: next regular payday or 7 days, whichever first; liquidated damages lesser of 10%/working day or treble; CBA may override**  (2026-01-01 → open) [A.1, US-DCS5-003, direct artifact inspection, conf high]

## 8 — Benefits in kind / taxable wages
DC income tax starts from federal gross income: federal exclusions (401(k), 125, HSA, transit, GTL) flow through (70%; 47-1803.02 not read). UI wages include non-cash and customary tips, exclude employer retirement/sickness/medical/death plans [US-DCS5-008].


## 9 — Deductions and garnishments
Child support: OAG CSSD sends IWO within 2 business days of the new-hire entry [US-DCS5-022]; DC fees/priority not read. No DC wage-deduction authorisation rule read.

- `dc.garn.creditor.rule` = **max 25% of weekly disposable wages exceeding 40 x DC minimum wage; one attachment at a time (16-572)**  (2026-01-01 → open) [A.1, US-DCS5-006, direct artifact inspection, conf high]
- `dc.garn.creditor.weekly_threshold` = **736** USD (2026-07-01 → open) [A.1, US-DCS5-006, derived arithmetically, conf high] — 40 x 18.40.

## 10 — Collective agreements / prevailing wage
Sector prevailing wage for underground electrical and gas utility work at Davis-Bacon rates [US-DCP52-005 legacy].

- `dc.living_wage.hourly` = **17.95** USD (2026-01-01 → 2026-06-30) [A.2, US-DCS5-012, second independent authority, conf high] — DC contractors/assistance >= 100,000 (subs 15,000/50,000) [US-DCS5-009]; CPI-U capped 3% each 1 Jan; floor = minimum wage.
- `dc.living_wage.hourly` = **18.4** USD (2026-07-01 → open) [A.2, US-DCS5-012, second independent authority, conf high]
- `dc.living_wage.contract_threshold` = **100000** USD (2026-01-01 → open) [A.1, US-DCS5-009, direct artifact inspection, conf high]

## 11 — Indexation
MW July 1 CPI-U Washington MSA (0.05); tipped % of MW; living wage Jan 1 CPI-U capped 3%; SUI base fixed; PFL rate statutory; PFL max benefit CPI from 2026-10-01; DC standard deduction COLA (assessment); brackets not indexed.


## 12 — Payroll data protection / records
New-hire reports carry the SSN; no truncation rule found; D.C. Code 28-3851 not read (40%).

- `dc.records.retention_years` = **3** years (2026-01-01 → open) [A.1, US-DCS5-010, direct artifact inspection, conf high] — Or federal standard if longer; DOB for employees under 19.

## 13 — Live legal change
D.C. Act 26-416 (emergency, 2026-08-13 to ~2026-11-11; status of the permanent FY2027 BSA unconfirmed); D.C. Law 26-55 (in force 2025-12-06: tipped %, compensation-sources payslip line); MW 18.40 / tipped 10.30 from 2026-07-01; D.C. Law 26-89 and Act 26-214 amend lump-sum retirement withholding only.


## Special populations (US-OWN-005)
- Domestic: covered by MW; household withholding on FR-900Q; UI annual April 15; casual babysitters excluded from ASSLA [US-DCS5-013, US-DCS5-018, US-DCS5-005].
- Agricultural: no DC rule (federal).
- Minors: no youth subminimum; DOB on records under 19 [US-DCS5-001, US-DCS5-010].
- Tipped: 10.30 (56%) with top-up; mandatory third-party payroll (non-hotel); tip lines on payslip; ASSLA 1/43 at full MW [US-DCS5-001, US-DCS5-010, US-DCS5-011, US-DCS5-004].
- Clergy and students: excluded from ASSLA [US-DCS5-005].
- Nonresidents incl. NRAs living outside DC: no DC withholding with D-4A [US-DCP51-006, US-MULTI-016].
- Government: DC government excluded from tipped schedule, covered by ASSLA; District reimburses UI [US-DCS5-001, US-DCS5-005, US-DCS5-017].
- Security officers in office buildings: SCA Guard 1 wage + fringe; workers with disabilities: MW unless 14(c) certificate [US-DCS5-001].

## Language seams (US-OWN-006)
Hire notice in English and the primary language where a Mayor template exists (32-1008(c)) [US-DCS5-010]; payslip English (US-OWN-006). DC postings page unreadable (recorded limit).

## Synthesis D additions (2026-11-02)

Source: browser-pass rows S5B-P1 / S5B-P2 merged into `legal-basis-register.csv` and SSA EFW2 TY2026 (US-FEDS5-032) read locally. Every claim below carries its register_id; the facts file is authoritative. Full log: `_research/synthesis-D/SYNTHESIS-D.md`.

Still open, new attempts recorded in `unresolved[].attempted`: `dc.wh.method`.

## QA r1b additions (2026-11-02)

Source: browser pass P3 (`_research/stage5/browser-pass-P3.md`, shard `S5B-P3.csv` merged into the register). Facts file is authoritative; every line below is a fact object with the same key.

**13 - Live legal change: FY2027 BSA (narrows RQ-146).** G-RULING: identity B26-0661 / D.C. Act 26-418 / D.C. Law 26-189; status IN FORCE from 2026-10-02 after congressional review (73 DCR 13120); level withholding (tax secs. 7111-7113) and employer contribution (PFL secs. 4051-4053) [A.1, US-DCB5-301, Council LIMS legislative history]. Still open (blocking): whether the permanent text equals Act 26-416 for those sections - the 214-page enrolled text was not read.

- `dc.live.fy2027_bsa_permanent` = **B26-0661 Fiscal Year 2027 Budget Support Act of 2026: enacted without the Mayor's signature 2026-08-14 as D.C. Act 26-418 (73 DCR 11735); transmitted to Congress 2026-08-20; D.C. Law 26-189 effective 2026-10-02 (73 DCR 13120). Status: IN FORCE (congressional review complete), before the emergency Act 26-416 lapses.** (2026-10-02 -> open) [A.1, US-DCB5-301, quoted from authority page, conf high] LEVEL: withholding and employer contribution (tax secs. 7111-7113; PFL secs. 4051-4053). Status confirmed on Council LIMS (verbatim excerpt). NOT checked: that Law 26-189 carries the same tax (7112) and PFL (4051-4053) text as Act 26-416 - see unresolved dc.live.fy2027_bsa_permanent.

## Open questions

Mirrors `unresolved[]` in the facts file (same keys, same wording). Regenerated by QA r1b on 2026-11-02.

- `dc.wh.method` (blocking) — 2026 DC withholding method after D.C. Act 26-416 repealed personal exemptions is unpublished; D-4/D-4A "under review"; OTR withholding-instructions page 403. **Would close it:** OTR tax notice or 2026/2027 FR-230 or D-4 revision (OTR Individual Income Tax Division), or the live instructions page via the orchestrator browser pass.
- `dc.wh.supplemental.rate` (non-blocking) — No flat supplemental rate in statute or any FR-230 edition; bonuses modelled as regular wages. **Would close it:** An OTR statement in a future FR-230 or notice.
- `dc.live.fy2027_bsa_permanent` (blocking) — The permanent FY2027 BSA is D.C. Law 26-189, in force from 2026-10-02 (fact dc.live.fy2027_bsa_permanent). Whether its tax (secs. 7111-7113) and PFL (secs. 4051-4053) text is identical to the emergency Act 26-416 the annex models was not compared (214-page text not read). **Would close it:** The enrolled text of B26-0661 / D.C. Law 26-189 (LIMS document or code.dccouncil.gov session law), secs. 4051-4053 and 7111-7113, compared with Act 26-416.
- `dc.sui.wage_base.other_state_credit` (non-blocking) — 51-103(e)(6) as read states no explicit credit for wages subject to another state UI. **Would close it:** 7 DCMR chapter 3 or DOES UI Employer Handbook.
- `dc.pit.std_deduction.cola` (non-blocking) — 2026 COLA amount of the DC standard deduction (assessment level) not read. **Would close it:** OTR 2026 D-40 instructions.
- `dc.payslip.electronic_and_deductions` (non-blocking) — No DC rule found for electronic payslips, direct deposit, deduction authorisation or SSN truncation. **Would close it:** 7 DCMR chapter 9 and D.C. Code 28-3851 et seq.
- `dc.termination.vacation_and_ui_notice` (non-blocking) — No DC statutory rule found for vacation payout or a UI separation notice. **Would close it:** 7 DCMR chapter 3 and the DOES OWH FAQ.
- `dc.leave.sick.coverage_threshold` (non-blocking) — DOES fact sheet says at least 50% of time in DC while 32-1003(b) and 32-541.01 say more than 50%. **Would close it:** 7 DCMR 3299 (ASSLA definitions).
- `dc.report.sui.uc30_fields` (non-blocking) — UC-30 / ESSP bulk-upload field layout is behind the employer login (gated). **Would close it:** DOES ESSP file-upload specification from an employer account (owner/client).

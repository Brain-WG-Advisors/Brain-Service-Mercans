# CCG annex_DE research pack — Delaware

Synthesis B, 2026-11-02. Source: `_research/stage5/DE.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_DE-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** Minimum wage 15.00 (fixed since 2025-01-01, not indexed); FLSA overtime. PIT 0-6.6% (30 Del. C. 1102, not indexed); withholding per Employer Guide (standard deduction 3,250/6,500, 110 credit per exemption); statutory convenience rule; no reciprocity; Wilmington 1.25% EIT. SUI employer-only, base 14,500 (2026) / 16,500 (2027), new 1.0%; Operations & Technology 0.2% billed separately by letter from 2026. Delaware Paid Leave 0.80% (2025-2026), employee share up to 50%. Pay statement for employers with more than 3 employees. Oracle: Employer Guide examples (13.88 weekly; 269.63 supplemental).

## 1 — Employment / labour code
Overtime: no state premium rule (ch. 9 read in full); FLSA 1.5x over 40 (85%). No local minimum wages (absence, 85%). No youth subminimum.

- `de.minwage.hourly` = **15.0** USD (2025-01-01 → open) [A.1, US-DES5-001, quoted from authority page, conf high] — 19 Del. C. 902(a)(5): last statutory step, not indexed, no 2027 step; equals federal if federal exceeds.
- `de.minwage.tipped.cash_wage` = **2.23** USD (2026-01-01 → open) [A.1, US-DES5-001, quoted from authority page, conf high] — Make-up to 15.00; mandatory tip pool capped at 15%; tips withheld as supplemental [US-DES5-021, US-DES5-006].
- `de.minwage.exclusions` = **agriculture; private-home domestic service; EAP and outside sales; US government; fishing; under-18 camp counselors; DOC inmates; CBA minor-league baseball (901(3))**  (2026-01-01 → open) [A.1, US-DES5-001, quoted from authority page, conf high]
- `de.pay_frequency.rule` = **at least once per calendar month on paydays designated in advance; due within 7 days of period close; nonwork-day payday moves earlier (1102)**  (2026-01-01 → open) [A.1, US-DES5-002, quoted from authority page, conf high]
- `de.payment.method` = **cash or check cashable at full value nearby; direct deposit only on employee written request; no paycard rule**  (2026-01-01 → open) [A.1, US-DES5-002, quoted from authority page, conf high]
- `de.wage_theft.penalty.max` = **20000** USD (2026-01-01 → open) [A.1, US-DES5-002, quoted from authority page, conf high] — 1102A: 2,000-20,000 per violation per employee for failing to withhold, failing to forward within 7 days, misclassification.
- `de.minor.work_permit.required` = **True**  (2026-01-01 → open) [A.1, US-DES5-017, quoted from authority page, conf high] — 19 Del. C. 504, under 18.

## 2 — Income tax (state withholding)
- `de.pit.bracket.1.ceiling` = **2000** USD (2014-01-01 → open) [A.1, US-DES5-003, quoted from authority page, conf high] — 0%.
- `de.pit.bracket.2.ceiling` = **5000** USD (2014-01-01 → open) [A.1, US-DES5-003, quoted from authority page, conf high]
- `de.pit.bracket.2.rate` = **2.2** percent (2014-01-01 → open) [A.1, US-DES5-003, quoted from authority page, conf high]
- `de.pit.bracket.3.ceiling` = **10000** USD (2014-01-01 → open) [A.1, US-DES5-003, quoted from authority page, conf high]
- `de.pit.bracket.3.rate` = **3.9** percent (2014-01-01 → open) [A.1, US-DES5-003, quoted from authority page, conf high]
- `de.pit.bracket.4.ceiling` = **20000** USD (2014-01-01 → open) [A.1, US-DES5-003, quoted from authority page, conf high]
- `de.pit.bracket.4.rate` = **4.8** percent (2014-01-01 → open) [A.1, US-DES5-003, quoted from authority page, conf high]
- `de.pit.bracket.5.ceiling` = **25000** USD (2014-01-01 → open) [A.1, US-DES5-003, quoted from authority page, conf high]
- `de.pit.bracket.5.rate` = **5.2** percent (2014-01-01 → open) [A.1, US-DES5-003, quoted from authority page, conf high]
- `de.pit.bracket.6.ceiling` = **60000** USD (2014-01-01 → open) [A.1, US-DES5-003, quoted from authority page, conf high]
- `de.pit.bracket.6.rate` = **5.55** percent (2014-01-01 → open) [A.1, US-DES5-003, quoted from authority page, conf high]
- `de.pit.bracket.7.rate` = **6.6** percent (2014-01-01 → open) [A.1, US-DES5-003, quoted from authority page, conf high] — Over 60,000.
- `de.wh.method` = **annualise (daily x300, weekly x52, biweekly x26, semi-monthly x24, monthly x12); less standard deduction; table 0/66/261/741/1,001/2,943.50 + marginal rate; less 110 x exemptions; divide by periods**  (2025-01-01 → open) [A.2, US-DES5-006, derived arithmetically, conf high] — Guide table "Effective January 1, 2025", live page. Base amounts re-derived from statute rates (Python). Rounding: none stated; examples round half-up to the cent.
- `de.wh.std_deduction.single` = **3250** USD (2025-01-01 → open) [A.2, US-DES5-006, derived arithmetically, conf high] — MFJ 6,500; MFS 3,250.
- `de.wh.std_deduction.mfj` = **6500** USD (2025-01-01 → open) [A.2, US-DES5-006, derived arithmetically, conf high] — Derivation recorded in register row US-DES5-006: Live page text identical to the 2026-10-13 Wayback copy of US-DE-P5-1-003. Annualized method: annualize gross (daily x300, weekly x52, monthly x12, semi-monthly x24, biweekly x26); minus standard deduction 3,250 single / 6,500 MFJ / 3,250 MFS; tax by table 'Effective January 1, 2025': 0-2,000 0; 2,0
- `de.wh.personal_credit.per_exemption` = **110** USD (2025-01-01 → open) [A.2, US-DES5-006, derived arithmetically, conf high] — Derivation recorded in register row US-DES5-006: Live page text identical to the 2026-10-13 Wayback copy of US-DE-P5-1-003. Annualized method: annualize gross (daily x300, weekly x52, monthly x12, semi-monthly x24, biweekly x26); minus standard deduction 3,250 single / 6,500 MFJ / 3,250 MFS; tax by table 'Effective January 1, 2025': 0-2,000 0; 2,0
- `de.wh.duty` = **withhold whenever wages are subject to federal withholding ("If you withhold Federal tax, then you must withhold State tax"); residents and nonresidents**  (2026-01-01 → open) [A.1, US-DES5-005, quoted from authority page, conf high]
- `de.wh.certificate` = **federal W-4 (DE worksheets SD/W-4A, W-4NR); no certificate = single, no allowances; copy to Division within 5 working days for 14+ allowances or exempt with wages over 168.50/week**  (2026-01-01 → open) [A.3, US-DES5-008, quoted from authority page, conf medium] — Mapping of 2020+ W-4 to exemptions open (DE-OQ-1).
- `de.wh.supplemental.method` = **with regular wages: one payment; separately: annualized-with minus annualized-without; tips same; deferred compensation recommended 5%**  (2026-01-01 → open) [A.2, US-DES5-006, derived arithmetically, conf high] — Derivation recorded in register row US-DES5-006: Live page text identical to the 2026-10-13 Wayback copy of US-DE-P5-1-003. Annualized method: annualize gross (daily x300, weekly x52, monthly x12, semi-monthly x24, biweekly x26); minus standard deduction 3,250 single / 6,500 MFJ / 3,250 MFS; tax by table 'Effective January 1, 2025': 0-2,000 0; 2,0
- `de.wh.deferred_comp.recommended_rate` = **5** percent (2026-01-01 → open) [A.2, US-DES5-006, derived arithmetically, conf high] — Derivation recorded in register row US-DES5-006: Live page text identical to the 2026-10-13 Wayback copy of US-DE-P5-1-003. Annualized method: annualize gross (daily x300, weekly x52, monthly x12, semi-monthly x24, biweekly x26); minus standard deduction 3,250 single / 6,500 MFJ / 3,250 MFS; tax by table 'Effective January 1, 2025': 0-2,000 0; 2,0

## 2b — Non-resident regime and reciprocity
- `de.nonres.convenience_rule` = **True**  (2026-01-01 → open) [A.1, US-DES5-004, quoted from authority page, conf high] — 30 Del. C. 1124(b)(1)b statutory. Nonresident tax = resident-basis tax less 110 credits x DE-source / DE AGI (1121). Resident credit for other-state tax at assessment only (1111) [US-DES5-003]. No reciprocity [US-DES5-008].
- `de.reciprocity.exists` = **False**  (2026-01-01 → open) [A.3, US-DES5-008, quoted from authority page, conf high]

## 2c — Local wage taxes
- `de.local.wilmington.eit.rate` = 1.25 (2023-01-01 → open) [A.2, US-DE-P5-2-001 — legacy id, NOT a fact] Wilmington EIT: residents wherever they earn, nonresidents for work in the City; separate return and reconciliation to City Finance. Regulations rev. 2023 not re-verified; 2026 rate assumed at the 22 Del. C. 901-902 cap.

## 3 — Social insurance (SUI / SDI / PFML / levies)
Industry and employer-size assessments (3350E/F) first payable 2027 [US-DEP9V-001]. Blue Collar training tax remains an open MANUAL item from P7 (US-DEL-004). No SDI/TDI.

- `de.sui.wage_base` = **14500** USD (2026-01-01 → 2026-12-31) [A.1, US-DES5-010, second independent authority, conf high] — 3302(28)(A)(viii); confirmed by DOL Merit Rate Table [US-DES5-022]. DOL FAQ still printing 18,500/10,500 is stale [US-DES5-011]. Other-state employment counts (3302(28)(A)(x)).
- `de.sui.wage_base` = **16500** USD (2027-01-01 → open) [A.1, US-DES5-010, quoted from authority page, conf high] — Enacted (or FUTA base if higher).
- `de.sui.new_employer.rate` = **1.0** percent (2026-01-01 → 2026-12-31) [A.2, US-DES5-022, second independent authority, conf high] — Construction new employer 1.0%; delinquent 6.3% (2025: 1.2% / 6.5%).
- `de.sui.employer.rate.min` = **0.3** percent (2026-01-01 → 2026-12-31) [A.2, US-DES5-022, second independent authority, conf high] — Range 0.3%-5.4%; whether it excludes the separately billed Op & Tech 0.2% is open.
- `de.sui.employer.rate.max` = **5.4** percent (2026-01-01 → 2026-12-31) [A.2, US-DES5-022, second independent authority, conf high]
- `de.sui.employee.rate` = **0** percent (2026-01-01 → open) [A.3, US-DES5-011, quoted from authority page, conf medium]
- `de.sui.op_tech_assessment.rate` = **0.2** percent (2026-01-01 → 2026-12-31) [A.1, US-DEL-003, quoted from authority page, conf high] — Billed separately by letter from 2026 (Q1 due 2026-08-31, Q2 2026-09-30; Op & Tech Lockbox) [US-DES5-011]; 0.175% from 2027. Separate DD/RSPEC payable line.
- `de.sui.op_tech_assessment.rate` = **0.175** percent (2027-01-01 → open) [A.1, US-DEL-003, quoted from authority page, conf high]
- `de.pfml.rate.total` = **0.8** percent (2025-01-01 → 2026-12-31) [A.1, US-DES5-012, quoted from authority page, conf high] — 19 Del. C. 3705: medical 0.40 + caregiving 0.08 + parental 0.32; employer may deduct up to 50% of each; FICA wage base; 10-24 employees parental only (0.32%); 25+ all three; <=9 exempt. From 2027 DOL-set, cap 1.00% (unpublished).
- `de.pfml.rate.medical` = **0.4** percent (2025-01-01 → 2026-12-31) [A.1, US-DES5-012, quoted from authority page, conf high]
- `de.pfml.rate.family_caregiving` = **0.08** percent (2025-01-01 → 2026-12-31) [A.1, US-DES5-012, quoted from authority page, conf high]
- `de.pfml.rate.parental` = **0.32** percent (2025-01-01 → 2026-12-31) [A.1, US-DES5-012, quoted from authority page, conf high]
- `de.pfml.employee_share.max_percent` = **50** percent (2025-01-01 → open) [A.1, US-DES5-012, quoted from authority page, conf high]
- `de.pfml.rate.cap` = **1.0** percent (2027-01-01 → open) [A.1, US-DES5-012, quoted from authority page, conf high]
- `de.pfml.benefit.weekly_max` = **900** USD (2026-01-01 → 2027-12-31) [A.1, US-DES5-012, quoted from authority page, conf high] — 80% of AWW, min 100; CPI-U Philadelphia-Camden-Wilmington after 2027.
- `de.pfml.multistate` = **coverage by primary worksite: employees primarily reporting to a DE worksite (3701(6)a), not UI localization**  (2026-01-01 → open) [A.1, US-DES5-012, quoted from authority page, conf high]

## 4 — Payslip statute
- `de.payslip.employer_threshold` = **3** employees (2026-01-01 → open) [A.1, US-DES5-002, quoted from authority page, conf high] — 1108: employers with MORE than 3 employees: at each payment (check, slip, or electronic if retainable; paper on request): wages due, pay period, each deduction, total hours for hourly. Hire notice of rate and payday.
- `de.payslip.items` = **wages due; pay period; total deductions each separately specified; total hours for hourly employees**  (2026-01-01 → open) [A.1, US-DES5-002, quoted from authority page, conf high]

## 5 — Statutory reporting instruments
- `de.report.wh.frequency` = **July-June lookback: quarterly up to 4,500; monthly 4,500-25,000; eighth-monthly over 25,000 (statutory, indexed under 30 Del. C. 515; 2026 values not read)**  (2026-01-01 → open) [A.1, US-DES5-005, quoted from authority page, conf medium]
- `de.report.wh.calendar` = **quarterly: last day of month after quarter; monthly: 15th; eighth-monthly: 3 working days after periods ending 3rd/7th/11th/15th/19th/22nd/25th/last; tax type 01106**  (2026-01-01 → open) [A.2, US-DES5-007, direct artifact inspection, conf high]
- `de.report.annual.wth_rec` = **WTH-REC (rev. 02/03/26) replaces W-3, due last day of January with W-2s; e-file if federal e-file; paper only for 10 or fewer forms; EFW2 with DE RS records; no SSN truncation**  (2026-02-03 → open) [A.2, US-DES5-009, direct artifact inspection, conf high]
- `de.report.w2.paper_max_forms` = **10** forms (2026-02-03 → open) [A.2, US-DES5-009, direct artifact inspection, conf high]
- `de.report.sui.quarterly` = **UC-8 tax report + UC-8A wage report, due end of month after quarter; late 1.5%/month interest and 17.50 per late report; Online Employer Services Portal**  (2026-01-01 → open) [A.3, US-DES5-011, quoted from authority page, conf high]
- `de.report.pfml.quarterly` = **Hours & Wage Report and contributions in Delaware LaborFirst**  (2026-01-01 → open) [A.2, US-DES5-013, quoted from authority page, conf high]
- `de.newhire.report_days` = **20** days (2026-01-01 → open) [A.1, US-DES5-005, quoted from authority page, conf high] — 30 Del. C. 1156A; rehire after 60+ days; fine 25 per failure.
- `de.report.w2.employee_on_termination_days` = **30** days (2026-01-01 → open) [A.1, US-DES5-005, quoted from authority page, conf high] — By Jan 31 or within 30 days of last wage payment on termination (1152).

## 6 — Leave
- `de.leave.sick.state_statute.exists` = **False**  (2026-01-01 → open) [A.3, US-DES5-021, second independent authority, conf high] — DOL KB: no private-sector paid sick leave or required days off; policies must be made available (1108(3)).
- `de.pfml.leave.parental_weeks` = **12** weeks (2026-01-01 → open) [A.1, US-DES5-012, quoted from authority page, conf high] — Medical/caregiving 6 weeks per 24 months; eligibility 12 months and 1,250 hours; employer decides within 5 business days and notifies DOL within 3.

## 7 — Termination and final pay
UI separation notice and WARN not researched.

- `de.final_pay.rule` = **later of next regular payday or 3 business days after last day worked (quit, discharge, suspension, layoff); liquidated damages lower of 10%/day or unpaid wages**  (2026-01-01 → open) [A.1, US-DES5-002, quoted from authority page, conf high] — Vacation payout per written policy (1109, within 30 days); death: up to 300 to family without probate (1106).

## 8 — Benefits in kind / taxable wages
- `de.pit.conformity` = **rolling: DE taxable income = federal AGI as in effect with ch. 11 modifications (1105); federal exclusions flow through; no HSA/125 add-back found**  (2026-01-01 → open) [A.1, US-DES5-019, quoted from authority page, conf medium]

## 9 — Deductions and garnishments
- `de.deductions.rule` = **only if required by law, medical care without employer benefit, or signed authorization for a lawful purpose benefiting the employee (1107)**  (2026-01-01 → open) [A.1, US-DES5-002, quoted from authority page, conf high]
- `de.garn.creditor.exempt_percent` = **85** percent (2026-01-01 → open) [A.1, US-DES5-014, quoted from authority page, conf high] — 10 Del. C. 4913: max 15% of wages; apply lower of DE 15% of wages and CCPA 25% of disposable; one attachment at a time; not for State fines/taxes.
- `de.garn.child_support.arrears_addon_percent` = **20** percent (2026-01-01 → open) [A.1, US-DES5-016, quoted from authority page, conf high] — 13 Del. C. 513: CCPA cap; priority except federal tax liens; arrears up to 20% of current or 20/month; start within 7 days after first payday; EFT/EDI for 50+ employees; fee amount not in statute.

## 10 — Collective agreements / prevailing wage
- `de.prevailing_wage.threshold.new_construction` = **500000** USD (2026-01-01 → open) [A.1, US-DES5-015, quoted from authority page, conf high] — 29 Del. C. 6960; alteration/repair/renovation/demolition 45,000; weekly pay and weekly certified payroll to DOL; penalties 1,000-5,000 + treble.
- `de.prevailing_wage.threshold.alteration` = **45000** USD (2026-01-01 → open) [A.1, US-DES5-015, quoted from authority page, conf high]

## 11 — Indexation
MW, PIT brackets, standard deduction and 110 credit not indexed; SUI base statutory steps; withholding filing thresholds indexed under 30 Del. C. 515 (2026 values not read; Guide prints 6,020/33,460 undated); Paid Leave rate statutory to 2026 then DOL-set; max benefit CPI after 2027.


## 12 — Payroll data protection / records
- `de.records.retention_years` = **3** years (2026-01-01 → open) [A.1, US-DES5-002, quoted from authority page, conf high] — 1108(6); 907 adds hours each day and week [US-DES5-001].
- `de.breach.notice_days` = **60** days (2026-01-01 → open) [A.1, US-DES5-020, quoted from authority page, conf high] — 6 Del. C. ch. 12B: AG notice > 500 residents; 1 year credit monitoring if SSN breached. Full SSN required on W-2 RS and IWO remittances.

## 13 — Live legal change
- `de.live.hb13_hs2.status` = **draft in House Revenue & Finance Committee since 2025-06-17, NOT enacted; would act at assessment and withholding**  (2025-06-17 → open) [A.1, US-DES5-018, quoted from authority page, conf high]

## Oracle — worked examples (C37)
- `de.oracle.guide.example1.withholding_weekly` = **13.88** USD (2025-01-01 → open) [A.2, US-DES5-006, derived arithmetically, conf high] — Guide example 1: single, 1 allowance, 25,000 annual -> tax 832.00; weekly 13.88. Reproduced in Python.
- `de.oracle.guide.example2.supplemental` = **269.63** USD (2025-01-01 → open) [A.2, US-DES5-006, derived arithmetically, conf high] — Guide example 2: 500/week + 5,000 bonus, single, 1 allowance -> 269.625, shown 269.63 (half-up to cent).

## Special populations (US-OWN-005)
- Domestic: excluded from state MW (FLSA applies); UI at 1,000 cash/quarter; PIT follows federal (none required) [US-DES5-001, US-DES5-010, US-DES5-005].
- Agricultural: excluded from MW; UI at 20,000/quarter or 10+ workers in 20 weeks [US-DES5-001, US-DES5-010].
- Minors: work permit; no youth subminimum; under-18 camp counselors excluded; child working for parent UI-excluded [US-DES5-017, US-DES5-001, US-DES5-010].
- Tipped: cash wage 2.23 with make-up; tips employee property; pool cap 15%; supplemental withholding [US-DES5-001, US-DES5-021, US-DES5-006].
- Clergy/religious organisations: UI exclusion per 3302(15)(E); volunteers MW-excluded [US-DES5-010, US-DES5-001].
- Students: own-school and work-study UI-excluded [US-DES5-010].
- NRAs: no DE rule beyond federal [US-DES5-005]. Other-state employees: DE-source wages, convenience rule [US-DES5-004, US-DES5-008].
- Commission agents/direct sellers: UI-excluded [US-DES5-010].
- Government: excluded from ch. 11 and UI (except 3302(14)(B)); US employees MW-excluded; State-plan employees excluded from Paid Leave [US-DES5-002, US-DES5-010, US-DES5-012].
- Family employment: UI-excluded [US-DES5-010, US-DES5-011].
- Small employers: payslip duty only above 3 employees; Paid Leave <10 exempt, 10-24 parental only [US-DES5-002, US-DES5-012].

## Language seams (US-OWN-006)
Paid-leave poster in English, Spanish and any first language of 5%+ of the workforce (19 Del. C. 3710(c)) [US-DEL-001]; bilingual expressly permitted [US-DEP9L-001]; payslip English (US-OWN-006).

## Open questions
Mirrors `unresolved[]` in the facts file (same keys).

- `de.local.wilmington.eit.rate` (non-blocking) — Value 1.25 (from 2023-01-01) is carried by register row US-DE-P5-2-001 (active, A.2, City of Wilmington Department of Finance), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. Wilmington EIT: residents wherever they earn, nonresidents for work in the City; separate return and reconciliation to City Finance. Regulations rev. 2023 not re-verified; 2026 rate assumed at the 22 Del. C. 901-902 cap. **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-DE-P5-2-001) or re-key US-DE-P5-2-001; then emit this key as a fact. No new research needed.
- `de.wh.w4_2020_mapping` (blocking) — The Employer Guide uses pre-2020 allowance wording; how a 2020+ W-4 maps to DE personal exemptions for the 110 credit is not stated. **Would close it:** Division of Revenue memo/FAQ on the 2020+ W-4 (Withholding unit 302-577-8779) or a DE-specific certificate.
- `de.report.wh.thresholds.current` (non-blocking) — 2026 indexed withholding filing thresholds not read (Guide prints 6,020 / 33,460 undated). **Would close it:** 2026 lookback notice or 30 Del. C. 515 adjustment table from the Division of Revenue.
- `de.pfml.rate.next_year` (non-blocking) — 2027 Paid Leave contribution rate is DOL-set (cap 1.00%) and unpublished on 2026-11-02. **Would close it:** DOL Delaware Paid Leave notice or regulation for 2027.
- `de.garn.iwo.employer_fee` (non-blocking) — 13 Del. C. 513(b)(8)a refers to a State-set fee without stating it. **Would close it:** DCSS employer page or regulation stating the fee.
- `de.sui.rate_range.op_tech_inclusion` (non-blocking) — Unclear whether the 2026 0.3%-5.4% range excludes the separately billed 0.2% Op & Tech. **Would close it:** A 2026 DOL employer rate letter or the DOL Employer Handbook.
- `de.report.sui.uc8a_format` (non-blocking) — UI separation-notice duty and UC-8A electronic wage-file format not read (budget). **Would close it:** DOL Employer Handbook linked from the employer-services page.
- `de.live.session_law_amendments` (non-blocking) — Content of 85 Del. Laws c. 301 (amending 1154) and enactment date of the 1103 three-business-day wording not identified. **Would close it:** Session-law pages on legis.delaware.gov.
- `de.local.wilmington.eit.current` (non-blocking) — Wilmington EIT regulations (rev. 2023) not re-verified; 2026 rate assumed at the statutory 1.25% cap. **Would close it:** City of Wilmington Finance EIT page or the 2026 employer reconciliation form.

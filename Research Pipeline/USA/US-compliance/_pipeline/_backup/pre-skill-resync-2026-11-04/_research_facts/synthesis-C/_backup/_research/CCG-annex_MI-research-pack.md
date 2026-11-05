# CCG annex_MI research pack — Michigan

Synthesis B, 2026-11-02. Source: `_research/stage5/MI.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_MI-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** Minimum wage 13.73 (2026) / 15.00 (2027, enacted), CPI-indexed from Oct 2027; tipped 40% (2026) rising to 50% by 2031; local mandates pre-empted. Flat 4.25% PIT less 5,900 per MI-W4 exemption; supplemental 4.25% no exemption; reciprocity IL/IN/KY/MN/OH/WI (state only); 2025 PA 24 tips/overtime deduction at ASSESSMENT only (no withholding change - trap). 24 city income taxes: Detroit 2.4% / 1.2% (Treasury-administered), 23 others self-administered (1% / 0.5% default, rates unread). UI base 9,000 (fund switch; 9,500 delinquent), new 2.7%, range 0.06%-12.2%. Pay statement MCL 408.479; SSN max 4 digits. Oracle: 75.36 state, 47.45 Detroit.

## 1 — Employment / labour code
- `mi.minwage.hourly` = **12.48** USD (2025-02-21 → 2025-12-31) [A.1, US-MIS5-001, direct artifact inspection, conf high]
- `mi.minwage.hourly` = **13.73** USD (2026-01-01 → 2026-12-31) [A.1, US-MIS5-001, direct artifact inspection, conf high] — IWOWA MCL 408.934 (2018 PA 337 as amended by 2025 PA 1); employers with 2+ employees, employees 16+; not FLSA-covered employers unless federal lower (408.940(1)).
- `mi.minwage.hourly` = **15.0** USD (2027-01-01 → open) [A.1, US-MIS5-001, direct artifact inspection, conf high] — Enacted. From Oct 2027 Midwest CPI-U by State Treasurer (published by 1 Nov, effective 1 Jan); no increase if prior-year unemployment >= 8.5%.
- `mi.minwage.tipped.percent` = **40** percent (2026-01-01 → 2026-12-31) [A.1, US-MIS5-003, derived arithmetically, conf high] — Schedule 42% (2027), 44% (2028), 46% (2029), 48% (2030), 50% (2031); conditions: tips cover gap, declared for FICA, kept by employee (pool within chain of service), written notice and consent at hire.
- `mi.minwage.tipped.percent` = **42** percent (2027-01-01 → 2027-12-31) [A.1, US-MIS5-003, derived arithmetically, conf high] — Derivation recorded in register row US-MIS5-003: Training wage 4.25/hour for first 90 days, new employee under 20; under-18 minimum = 85% of general minimum (2026: 13.73 x 0.85 = 11.6705, derived). Tipped minimum = % of general minimum: 38% from 2025-02-21, 40% from 2026-01-01 (13.73 x 0.40 = 5.492, derived), 42% 2027, 44% 2028, 46% 2029, 48% 2030
- `mi.minwage.tipped.cash_wage` = **5.492** USD (2026-01-01 → 2026-12-31) [A.1, US-MIS5-003, derived arithmetically, conf high] — 13.73 x 0.40; statute gives no rounding rule.
- `mi.minwage.tipped.cash_wage` = **6.3** USD (2027-01-01 → 2027-12-31) [A.1, US-MIS5-003, derived arithmetically, conf high] — 15.00 x 0.42.
- `mi.minwage.minor.percent` = **85** percent (2026-01-01 → open) [A.1, US-MIS5-003, derived arithmetically, conf high] — Under 18: 13.73 x 0.85 = 11.6705 (derived, no rounding rule).
- `mi.minwage.training_wage` = **4.25** USD (2026-01-01 → open) [A.1, US-MIS5-003, derived arithmetically, conf high] — First 90 days, new employees under 20.
- `mi.local_mandates.preempted` = **True**  (2015-01-01 → open) [A.1, US-MIS5-014, direct artifact inspection, conf high] — 2015 PA 105 (MCL 123.1385-.1389): local MW, prevailing wage (except state projects), leave and scheduling mandates pre-empted.
- `mi.overtime.weekly_threshold_hours` = **40** hours (2026-01-01 → open) [A.1, US-MIS5-002, direct artifact inspection, conf high] — MCL 408.934a: 1.5x; public hospitals 8/80; exemptions EAP, seasonal amusement, agriculture; comp time 1.5 h per OT hour, cap 240 h, cash out within 30 days of request and at termination; comp time on the earnings statement.
- `mi.comp_time.cap_hours` = **240** hours (2026-01-01 → open) [A.1, US-MIS5-002, direct artifact inspection, conf high]
- `mi.pay_frequency.rule` = **default semi-monthly (1-15 paid by 1st next month; 16-end by 15th); weekly/biweekly payday <= 14 days after period end; monthly within 15 days; December OT may go to next payday (MCL 408.472)**  (2026-01-01 → open) [A.1, US-MIS5-005, direct artifact inspection, conf high]
- `mi.payment.method` = **cash, check, direct deposit, payroll debit card; DD/paycard need full free written consent (mandated DD-or-card election: no return within 30 days = presumed consent); method change within 1 pay period; paycard 1 free withdrawal per period, 21 days notice of fee changes, free balance inquiries; no cost pass-through (MCL 408.476)**  (2026-01-01 → open) [A.1, US-MIS5-006, direct artifact inspection, conf high]

## 2 — Income tax (state withholding)
- `mi.pit.rate.flat` = **4.25** percent (2026-01-01 → open) [A.2, US-MIS5-019, direct artifact inspection, conf high] — Guide 446 Rev. 02-26 [US-MI-PIT-001 legacy]; MCL 206.703.
- `mi.wh.method` = **4.25% x (compensation - 5,900 x MI-W4 exemptions / pay periods)**  (2026-01-01 → 2026-12-31) [A.2, US-MIS5-019, direct artifact inspection, conf high] — Per-period exemption weekly 113.46, biweekly 226.92, semi-monthly 245.83, monthly 491.67 (derived). No rounding rule.
- `mi.wh.exemption.annual` = **5900** USD (2026-01-01 → 2026-12-31) [A.1, US-MIS5-015, direct artifact inspection, conf high] — Indexed: 3,700 x CPI ratio + 600, rounded to 100 (2026 not re-derivable from read sources); 2027 unpublished.
- `mi.wh.exemption.biweekly` = **226.92** USD (2026-01-01 → 2026-12-31) [A.2, US-MIS5-019, derived arithmetically, conf high] — 5,900/26.
- `mi.wh.supplemental.rate` = **4.25** percent (2026-01-01 → open) [A.2, US-MIS5-019, direct artifact inspection, conf medium] — Bonuses/separate payments at 4.25% with no exemption adjustment (Guide 446, legacy US-MI-PIT-001).
- `mi.wh.certificate` = **MI-W4 (Rev. 12-20); federal W-4 may not substitute; line 6 exemptions, line 7 additional, 8a/8b exempt; none = zero exemptions; copies to Treasury for 10+ exemptions or exempt; nonresidency proof by employer certificate/letter**  (2020-12-01 → open) [A.2, US-MIS5-019, direct artifact inspection, conf high]
- `mi.pit.tips_overtime_deduction` = **2025 PA 24 (MCL 206.30(1)(ee)): tax years 2026-2028 deduct federally allowed qualified tips (IRC 224) and overtime (IRC 225); level ASSESSMENT (MI-1040) only - no withholding change**  (2026-01-01 → 2028-12-31) [A.2, US-MIS5-017, direct artifact inspection, conf high] — TRAP: tier-B claim that employers stop withholding on tips is unsupported - do not model. 2026 PA 39 (2026-07-22) amended 206.30 again (content open) [US-MIS5-015].

## 2b — Non-resident regime and reciprocity
- `mi.reciprocity.states` = IL, IN, KY, MN, OH, WI (state tax only, not city tax) (2026-01-01 → open) [A.2, US-MI-P5-1-001 — legacy id, NOT a fact] [US-MULTI-010].
- `mi.nonres.rules` = **withhold nonresidents for MI work unless reciprocity; residents temporarily working elsewhere still withheld; out-of-state employers register and withhold for MI workers**  (2026-01-01 → open) [A.2, US-MIS5-019, direct artifact inspection, conf medium] — Guide 446 [US-MI-PIT-001 legacy].

## 2c — Local wage taxes
- `mi.local.detroit.rate.resident` = **2.4** percent (2026-01-01 → open) [A.2, US-MIR3-002, quoted from authority page, conf high] — Treasury-administered; nonresident 1.2% (predominant place of work Detroit); exemption 600/yr (weekly 11.54, biweekly 23.08, semi-monthly 25.00, monthly 50.00, daily 1.64); DW-4 (Form 5527), none = resident rate no exemption; Form 5323 monthly by 15th; Form 5321 annual due 2027-02-28 for TY2026 [US-MI-P5-1-002].
- `mi.local.detroit.rate.nonresident` = **1.2** percent (2026-01-01 → open) [A.2, US-MIR3-002, quoted from authority page, conf high]
- `mi.local.detroit.exemption.annual` = **600** USD (2026-01-01 → open) [A.2, US-MIR3-002, quoted from authority page, conf high]
- `mi.local.cities.count` = **24** cities (2026-01-01 → open) [A.2, US-MIR3-001, quoted from authority page, conf high] — Detroit + 23 self-administered cities on separate returns (T4); uniform ordinance 1% residents / 0.5% nonresidents unless a city resolves lower (MCL 141.611) [US-MIR3-003]; 23-city rates/forms/dates unread.
- `mi.local.uniform.resident_rate_default` = **1.0** percent (2026-01-01 → open) [A.1, US-MIR3-003, quoted from authority page, conf medium]
- `mi.local.uniform.nonresident_rate_default` = **0.5** percent (2026-01-01 → open) [A.1, US-MIR3-003, quoted from authority page, conf medium]

## 3 — Social insurance (SUI / SDI / PFML / levies)
No employee UI (only AK/NJ/PA). No SDI/TDI/PFML/LTC: absence rests on the US-OWN-007 levy census and US-MIP9V-001/US-MIP9W-001 (the per-state row US-MI-P5-1-008 is MANUAL and not relied on); ESTA is employer-paid leave.

- `mi.sui.wage_base` = **9000** USD (2026-01-01 → 2026-12-31) [A.2, US-MIS5-025, derived arithmetically, conf high] — MCL 421.44(4): 9,500 reduced to 9,000 for non-delinquent employers when fund >= 2.5B on prior 30 June [US-MIS5-010]; 9,500 for delinquent. FAQ saving check: 0.027 x 500 = 13.50 (~14). Not CPI-indexed; 2027 depends on fund at 2026-06-30.
- `mi.sui.wage_base.delinquent` = **9500** USD (2026-01-01 → open) [A.1, US-MIS5-010, direct artifact inspection, conf high]
- `mi.sui.new_employer.rate` = **2.7** percent (2026-01-01 → open) [A.1, US-MIS5-012, direct artifact inspection, conf high] — Years 1-2 (MCL 421.19); construction pays average construction rate (5.0% for 2026).
- `mi.sui.employer.rate.min` = **0.06** percent (2026-01-01 → 2026-12-31) [A.2, US-MIP9W-001, quoted from authority page, conf high] — Range 0.06%-12.2% (15.2% with penalty); no transit/workforce/admin surcharge [US-MIP9V-001, US-MIP9W-002].
- `mi.sui.employer.rate.max` = **12.2** percent (2026-01-01 → 2026-12-31) [A.2, US-MIP9W-001, quoted from authority page, conf high]
- `mi.sui.wages.definition` = **FICA-reported tips included; retirement/health plan payments, employer-paid employee FICA, 401(a) trust payments, SUB pay excluded; wages paid in other states count toward the limit**  (2026-01-01 → open) [A.1, US-MIS5-010, direct artifact inspection, conf high]

## 4 — Payslip statute
- `mi.payslip.items` = **hours worked, gross wages, pay-period identification, separate itemisation of deductions (piece-rate hand harvesters: units); hours may be omitted for EAP-exempt, elected officials, political appointees (MCL 408.479(2)); comp time earned/paid**  (2026-01-01 → open) [A.1, US-MIS5-009, direct artifact inspection, conf high] — IWOWA 408.937 repeats hours/wages/deductions; e-delivery: statute silent.

## 5 — Statutory reporting instruments
State W-2 due Jan 31; 10+ forms via MTO in EFW2/Pub 1220; < 10 MTO, Form 447 media or paper; W-2 not via CF/SF (1099s only); ceasing business: W-2s within 30 days [US-MI-PIT-001 legacy]. New hire: Michigan New Hires Operation Center (mi-newhire.com, Form 3281), federal 20 days [US-MIS5-026 partial]; MI statute/penalty not located. Registration e-Registration (MTO); discontinuance Form 163; Form 151 / UIA 1488 authorisations.

- `mi.report.wh.5080` = **Form 5080 monthly/quarterly due 20th after period (combined SUW return; frequency assigned yearly); late penalty 5%; MTO, software or paper**  (2026-01-01 → open) [A.2, US-MIS5-018, direct artifact inspection, conf high]
- `mi.report.annual.5081` = **Form 5081 annual reconciliation for 2026 due 2027-02-28 (every filer)**  (2026-01-01 → open) [A.2, US-MIS5-021, direct artifact inspection, conf high]
- `mi.report.wh.accelerated_eft_threshold` = **480000** USD (2026-01-01 → open) [A.2, US-MIS5-021, direct artifact inspection, conf high] — Prior-year liability >= 480,000: EFT on the federal deposit day (notified April, from July).
- `mi.report.sui.quarterly` = **MiUI (live 2026-02-23) due 25 Jan / 25 Apr / 25 Jul / 25 Oct; file formats CSV v3 (2026-04-08), ICESA v2, EFW2 v2 (2026-04-03, 512-byte RE/RS UIA profile), XML v1; MiWAM format retired**  (2026-02-23 → open) [A.2, US-MIS5-022, direct artifact inspection, conf high] — Due dates [US-MIS5-020].

## 6 — Leave
- `mi.leave.esta.accrual.hours_worked_per_hour` = **30** hours (2025-02-21 → open) [A.1, US-MIS5-004, direct artifact inspection, conf high] — ESTA (2018 PA 338 as amended by 2025 PA 2): every employer; small (<= 10) cap 40 h or frontload 40 (from 2025-10-01); others cap 72 or frontload 72; FLSA-exempt assumed 40 h; pay greater of base rate or MW (excl. OT/bonus/commission/tips); 1 h increments; new hire wait up to 120 days; no payout; rehire within 2 months restores; documentation for > 3 days; records 3 years.
- `mi.leave.esta.cap_hours.small` = **40** hours (2025-10-01 → open) [A.1, US-MIS5-004, direct artifact inspection, conf high]
- `mi.leave.esta.cap_hours.large` = **72** hours (2025-02-21 → open) [A.1, US-MIS5-004, direct artifact inspection, conf high]
- `mi.leave.esta.small_employer_threshold` = **10** employees (2025-02-21 → open) [A.1, US-MIS5-004, direct artifact inspection, conf high]
- `mi.leave.esta.payout_on_separation` = **False**  (2025-02-21 → open) [A.1, US-MIS5-004, direct artifact inspection, conf high]

## 7 — Termination and final pay
- `mi.final_pay.rule` = **discharge and quit: as soon as the amount can with due diligence be determined (hand harvesters within 3 days); contract workers estimated pay then final at contract end; deceased: designee/next-of-kin (MCL 408.475)**  (2026-01-01 → open) [A.1, US-MIS5-007, direct artifact inspection, conf high] — Vacation payout per written contract/policy (408.471(e)/.473); withholding a benefit due at termination needs written consent (408.474); comp time paid; ESTA no payout.

## 8 — Benefits in kind / taxable wages
- `mi.pit.conformity` = **MI taxable income starts from federal AGI (rolling); fringe benefits follow Pub. 15 (401(k), cafeteria); no departure located**  (2026-01-01 → open) [A.1, US-MIS5-015, direct artifact inspection, conf medium]

## 9 — Deductions and garnishments
Creditor garnishment: CCPA 25% [US-FED-011]; MCL 600.4012 not read; IWO employer fee not located.

- `mi.deductions.rule` = **written consent for each deduction not required by law/CBA; for employer benefit consent each pay and not below MW; overpayment recovery within 6 months, clerical error, notice 1 period ahead, max 15% of gross, not below MW (MCL 408.477)**  (2026-01-01 → open) [A.1, US-MIS5-008, direct artifact inspection, conf high]
- `mi.deductions.overpayment.max_percent_gross` = **15** percent (2026-01-01 → open) [A.1, US-MIS5-008, direct artifact inspection, conf high]
- `mi.garn.child_support.cap_percent` = **50** percent (2026-01-01 → open) [A.1, US-MIS5-016, direct artifact inspection, conf high] — MCL 552.608: total under all support orders max 50% of disposable (stricter than CCPA); remit to MiSDU [US-MIS5-024].

## 10 — Collective agreements / prevailing wage
- `mi.prevailing_wage.certified_payroll` = **state projects (2023 PA 10, from 2024-02-13; energy >= 2 MW and contractor registration from 2025-04-02): no dollar threshold; certified payroll within 10 days after each pay period to contracting agent then LEO database; records 3 years; fine up to 5,000**  (2025-04-02 → open) [A.1, US-MIS5-023, direct artifact inspection, conf high]

## 11 — Indexation
MW fixed to 15.00 then Midwest CPI-U (unless unemployment >= 8.5%); tipped/minor % of MW; PIT exemption 3,700 x CPI ratio + 600 rounded to 100; rate statutory; SUI base fund switch; Detroit exemption fixed.


## 12 — Payroll data protection / records
- `mi.records.retention_years` = **3** years (2026-01-01 → open) [A.1, US-MIS5-009, direct artifact inspection, conf high] — Name, address, birth date, occupation, rate, hours and wages per period, deductions, fringe benefits.
- `mi.payslip.ssn.max_digits` = **4** digits (2005-01-01 → open) [A.1, US-MIS5-013, direct artifact inspection, conf high] — SSN Privacy Act (MCL 445.83/.84): no more than 4 sequential digits displayed; SSN privacy policy required.

## 13 — Live legal change
- `mi.live.miui` = **MiUI replaced MiWAM for the UI tax side on 2026-02-23 with new wage-file specs**  (2026-02-23 → open) [A.2, US-MIS5-022, direct artifact inspection, conf high]

## Oracle — worked examples (C37)
- `mi.oracle.state.biweekly_2000_1ex` = **75.36** USD (2026-01-01 → 2026-12-31) [A.2, US-MIS5-019, derived arithmetically, conf high] — (2,000 - 226.92) x 0.0425 = 75.36. Official oracle: Treasury withholding calculator (michigan.gov/taxes/business-taxes/withholding/tax-calculator).
- `mi.oracle.detroit.resident_biweekly_2000` = **47.45** USD (2026-01-01 → 2026-12-31) [A.2, US-MIR3-002, derived arithmetically, conf high] — (2,000 - 23.08) x 0.024 = 47.45.

## Special populations (US-OWN-005)
- Domestic: MW/OT apply to companionship and non-live-in childcare (except casual under-18 sitters <= 20 h/week, 408.940(2)); UI excludes private-home domestic below threshold (MCL 421.41 thresholds open) [US-MIS5-011].
- Agricultural: state OT exempt; harvest piece-rate outside act until scale set; hand harvesters paid within 2 days after work week; H-2A UI-excluded [US-MIS5-002, US-MIS5-005, US-MIS5-011].
- Minors: 85% under 18; 4.25 training wage under 20 first 90 days; ESTA excludes youth-employment minors; UI excludes child for parent [US-MIS5-003, US-MIS5-004, US-MIS5-011].
- Tipped: 40% (2026) with notice/consent; tips employee property; reported tips UI wages; tips deduction at assessment 2026-2028 [US-MIS5-003, US-MIS5-010, US-MIS5-017].
- Clergy: MI withholding follows federal duty; church employment UI-excluded [US-MIS5-011].
- Students: own-school (<= 30 h/week), co-op under 22, accredited curriculum students UI-excluded [US-MIS5-011].
- NRAs: follow federal duty; H-2A UI-excluded [US-MIS5-011].
- Statutory employees: IRS Pub. 15 definitions; commission-only real estate/investment/insurance agents and direct sellers UI-excluded [US-MIS5-011].
- Government: employers under IWOWA (7k fire/police OT) and Act 390; federal employees excluded from ESTA [US-MIS5-002, US-MIS5-004].

## Language seams (US-OWN-006)
Payslip: no language rule [US-MIL-002]; ESTA notice/poster in English and Spanish plus any first language of 10%+ of workforce if LEO translated it [US-MIL-001, US-MIS5-004]; payslip English (US-OWN-006).

## Open questions
Mirrors `unresolved[]` in the facts file (same keys).

- `mi.reciprocity.states` (non-blocking) — Value IL, IN, KY, MN, OH, WI (state tax only, not city tax) (from 2026-01-01) is carried by register row US-MI-P5-1-001 (active, A.2, Michigan Department of Treasury), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. [US-MULTI-010]. **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-MI-P5-1-001) or re-key US-MI-P5-1-001; then emit this key as a fact. No new research needed.
- `mi.local.cities.rates` (blocking) — Rates, forms and due dates of the 23 self-administered city income taxes (Albion ... Walker) not read. **Would close it:** Each city income-tax withholding instructions for 2026 (city income-tax department pages); parallel fan-out per city.
- `mi.newhire.statute` (non-blocking) — Michigan statute establishing the New Hires Operation Center duty, state penalty and fields not located (mi-newhire.com app JS). **Would close it:** The statute or MDHHS/OCS employer new-hire guide (DHS-Pub-95/96).
- `mi.garn.iwo_fee_and_periodic` (non-blocking) — Employer IWO processing fee and MCL 600.4012 periodic-garnishment procedure not read. **Would close it:** MCL 552.601 et seq. income-withholding sections and MCL 600.4012 / MCR 3.101.
- `mi.live.2026_pa_39` (non-blocking) — 2026 PA 39 (imd. eff. 2026-07-22) amended MCL 206.30; content not isolated. **Would close it:** 2026 PA 39 enrolled bill on legislature.mi.gov (check (ee) and the personal exemption).
- `mi.sui.wage_base.next_year` (non-blocking) — 2027 SUI base (9,000 vs 9,500) depends on fund at 2026-06-30; 2027 personal exemption unpublished. **Would close it:** UIA Employer Advisor / Form 6354 notices for 2027 and Guide 446 TY2027.
- `mi.payslip.electronic_delivery` (non-blocking) — Act 390 silent; no LEO guidance read. **Would close it:** LEO Wage and Hour FAQ on electronic pay statements.
- `mi.sui.coverage.ag_domestic` (non-blocking) — MES Act sec. 41(5)/(6) agricultural and domestic thresholds not read. **Would close it:** MCL 421.41 on legislature.mi.gov.
- `mi.pit.rate.register_alias` (non-blocking) — Guide 446 (rate, supplemental, nonresident, W-2 rules) is carried by legacy row US-MI-PIT-001; facts cite US-MIS5-019 (MI-W4) which also carries 4.25% / 5,900. **Would close it:** Final merge: S5-pattern alias row for Guide 446 Rev. 02-26.

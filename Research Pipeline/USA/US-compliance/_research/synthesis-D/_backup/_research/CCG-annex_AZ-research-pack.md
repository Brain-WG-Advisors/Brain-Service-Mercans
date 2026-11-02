# CCG annex_AZ research pack — Arizona

> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern (map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.

Synthesis B, 2026-11-02. Source: `_research/stage5/AZ.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_AZ-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** Flat-percentage withholding elected on Form A-4 (0.5-3.5%, default 2.0%) on federal wages; no local income tax. State minimum wage CPI-indexed (2026 15.15 / 2027 15.65 are derived from an unconfirmed 2025 base: MANUAL, not facts); Tucson local minimum wage 15.45 / 16.00. Earned paid sick time with mandatory paycheck content (23-375(C)). SUI base 8,000, new employer 2.00%, no employee UI; UI Operating Fund 3.15% of UI liability from 2027. Stricter creditor-garnishment cap (10%).

## 1 — Employment / labour code
State minimum wage 2026/2027: the derived 15.15 (2026) and 15.65 (2027) rest on an unconfirmed 2025 base of 14.70 and on the tier-C MANUAL row US-AZS5-028 (ICA page 403). They are NOT facts (see unresolved az.minwage.hourly). The CPI-U steps are facts. Tipped cash wage likewise derived (12.15/12.65) and not emitted. Overtime: no AZ statute located; FLSA applies (medium). Flagstaff local rate unread.

- `az.minwage.indexation` = **each 1 January by Aug-over-Aug CPI-U (US city average), increase rounded to nearest 0.05 (A.R.S. 23-363(B))**  (2021-01-01 → open) [A.1, US-AZS5-005, direct artifact inspection, conf high]
- `az.minwage.tip_credit.max` = **3.0** USD (2021-01-01 → open) [A.1, US-AZS5-005, direct artifact inspection, conf high] — Employer may pay up to 3.00/h below the minimum if tips + wages reach it each week.
- `az.local_minwage.allowed` = **True**  (2026-01-01 → open) [A.1, US-AZS5-006, direct artifact inspection, conf high] — 23-364(I) (voter-protected) permits county/city ordinances above the state rate; the azleg copy of 23-362 (1997 version, US-AZS5-004) says otherwise. Build rule: local rates apply; flag for counsel.
- `az.local_minwage.tucson.hourly` = **15.45** USD (2026-01-01 → 2026-12-31) [A.2, US-AZS5-027, derived arithmetically, conf high] — Employees with 5+ hours per pay cycle in the city; tip credit max 3.00; State/federal/tribal employers excluded. G-DERIVE: 15.00 x 1.029162 = 15.437 -> 15.45.
- `az.local_minwage.tucson.hourly` = **16.0** USD (2027-01-01 → open) [A.2, US-AZS5-027, derived arithmetically, conf high] — Published 2027 rate; G-DERIVE 15.45 x 1.033965 = 15.975 -> 16.00.
- `az.cpi_u.aug2025_over_aug2024.percent` = **2.9162** percent (2025-08-01 → open) [A.2, US-AZS5-026, derived arithmetically, conf high] — BLS CPI-U Aug 2024 314.796, Aug 2025 323.976: 323.976/314.796 - 1.
- `az.cpi_u.aug2026_over_aug2025.percent` = **3.3965** percent (2026-08-01 → open) [A.2, US-AZS5-026, derived arithmetically, conf high] — BLS CPI-U Aug 2026 334.980 / Aug 2025 323.976 - 1.
- `az.pay_frequency.rule` = **two or more fixed paydays a month, no more than 16 days apart; monthly allowed for FLSA-exempt staff of out-of-state employers with centralized payroll; up to 5 days held back; OT due within 16 days after period**  (2026-01-01 → open) [A.1, US-AZS5-001, direct artifact inspection, conf high]
- `az.payment.method` = **cash or negotiable check; direct deposit with written consent; payroll card if DD offered and employee neither consents nor names an institution; one free withdrawal per deposit**  (2026-01-01 → open) [A.1, US-AZS5-001, direct artifact inspection, conf high]
- `az.minor.under16.school_week_max_hours` = **18** hours (2026-01-01 → open) [A.1, US-AZS5-013, direct artifact inspection, conf high] — 23-233: in session 18 h/week, 3 h/day; outside session 40 h/week, 8 h/day; no night work.

## 2 — Income tax (state withholding)
- `az.wh.method` = **flat percentage of gross taxable wages (federal IRC 3401 wages, W-2 box 1) elected on Form A-4**  (2026-01-01 → open) [A.2, US-AZS5-024, quoted from authority page, conf high] — A.R.S. 43-401(A),(E) [US-AZS5-020]. Same percentage applies to bonus and other emolument: no separate supplemental rate (medium-high).
- `az.wh.rate_options` = **0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5 percent**  (2026-01-01 → open) [A.2, US-AZS5-024, quoted from authority page, conf high]
- `az.wh.default_rate` = **2.0** percent (2026-01-01 → open) [A.2, US-AZS5-024, quoted from authority page, conf high] — Until the employee elects; A-4 due within 5 days of hire. Zero-percent election renewed yearly.
- `az.wh.supplemental.rate` = **same elected percentage (no separate supplemental rate)**  (2026-01-01 → open) [A.1, US-AZS5-020, direct artifact inspection, conf medium]
- `az.wh.december_opt_out` = **True**  (2026-01-01 → open) [A.1, US-AZS5-020, direct artifact inspection, conf high] — 43-401(B),(F): employer may elect not to withhold in December; tell ADOR and employees before 1 July.
- `az.wh.a4c.remit_days_after_quarter` = **15** days (2026-01-01 → open) [A.1, US-AZS5-020, direct artifact inspection, conf high] — A-4C credit-contribution reduction; employee statement within 30 days after year end or 15 days after termination.
- `az.wh.exclusions` = **nonresident common-carrier employees; domestic service in private home; casual labour; seasonal hand farm labour; nonresidents present < 60 days (not athletes/entertainers); disaster-recovery workers**  (2026-01-01 → open) [A.1, US-AZS5-021, direct artifact inspection, conf high] — A.R.S. 43-403.

## 2b — Non-resident regime and reciprocity
- `az.nonres.withholding_days_threshold` = **60** days (2026-01-01 → open) [A.1, US-AZS5-021, direct artifact inspection, conf high] — Nonresident withheld after 60 days (or earlier by agreement). Form WEC exemptions: residents of CA, IN, OR, VA claiming the credit (unilateral; assessment-level credit 43-1096), MSRRA spouses, Native Americans on own reservation [US-AZS5-024]. Resident working outside AZ may opt in with A-4V.
- `az.nonres.wec_states` = **CA, IN, OR, VA**  (2026-01-01 → open) [A.2, US-AZS5-024, quoted from authority page, conf high]

## 2c — Local wage taxes
- `az.local_wage_tax.exists` = **False**  (2026-01-01 → open) [A.2, US-AZR3-006, quoted from authority page, conf high]

## 3 — Social insurance (SUI / SDI / PFML / levies)
UI exclusions (23-615, 23-617) [US-AZS5-014, US-AZS5-015]: farm labour below 10 workers/20 weeks or 20,000 cash a quarter; family employment; students at own school; 501(c)(3) religious/charitable; churches and ministers; commission-only insurance, real estate, securities, tax-preparer salespeople; under-18 newspaper carriers; casual labour. Domestic UI threshold not extracted.

- `az.sui.wage_base` = **8000** USD (2026-01-01 → open) [A.2, US-AZP9V-001, direct artifact inspection, conf high] — Fixed (7,000 before 2023); not indexed.
- `az.sui.new_employer.rate` = **2.0** percent (2026-01-01 → 2026-12-31) [A.2, US-AZP9V-001, direct artifact inspection, conf high]
- `az.sui.employer.rate.min` = **0.03** percent (2026-01-01 → 2026-12-31) [A.2, US-AZR3-003, quoted from authority page, conf high] — 2026 adjusted rates 0.03%-8.36% (UIT-0603A, A.R.S. 23-730).
- `az.sui.employer.rate.max` = **8.36** percent (2026-01-01 → 2026-12-31) [A.2, US-AZP9V-001, direct artifact inspection, conf high]
- `az.sui.employee.rate` = **0** percent (2026-01-01 → open) [A.2, US-AZR3-001, quoted from authority page, conf high] — "You cannot take these taxes out of employee pay."
- `az.ui_operating_fund.rate_of_ui_liability` = **3.15** percent (2027-01-01 → open) [A.2, US-AZR3-004, quoted from authority page, conf high] — Each quarter of 2027 experience-rated employers pay 3.15% of UI liability to the UI Operating Fund (NOT 2026).
- `az.sdi_pfml.exists` = **False**  (2026-01-01 → open) [A.2, US-AZR3-005, quoted from authority page, conf high] — No SDI/PFML or other levy [US-AZP9V-001, US-AZP9V-002].

## 4 — Payslip statute
- `az.payslip.required_when` = **only for direct deposit or payroll card: written or electronic statement of earnings and withholdings, no content list (23-351(E),(F))**  (2026-01-01 → open) [A.1, US-AZS5-001, direct artifact inspection, conf high]
- `az.payslip.sick_time_fields` = **sick time available; sick time used year to date; pay received as sick time (on paycheck or attachment, every regular paycheck)**  (2017-07-01 → open) [A.1, US-AZS5-011, direct artifact inspection, conf high] — A.R.S. 23-375(C); hard PSL/DD field set.

## 5 — Statutory reporting instruments
Registration on JT-1 (ADOR + DES). POA 821-PSC / UIT-1146A. DES quarterly UI report UC-018: format/deadline open (des.az.gov 403).

- `az.report.wh.deposit_schedule` = under 200 average: annual A1-APR due 31 Jan; 200-1,500: quarterly; over 1,500: federal schedule; EFT mandatory at 500+; A1-QRT quarterly even if zero (+10 days for timely payers) (2026-01-01 → open) [A.2, US-AZP52-005 — promoted to fact in Synthesis C]
- `az.report.wh.annual.due` = **A1-R with W-2s due 31 January (43-412(B)); 30-day extension for good cause**  (2026-01-01 → open) [A.1, US-AZS5-022, direct artifact inspection, conf high]
- `az.report.w2.format` = **EFW2 (Pub 701 rev. Jan 2025): mandatory electronic .txt via AZTaxes/AZFSET/transmitter; RS required, RV optional, state code 04; no SSN/EIN truncation; 1099s with AZ withholding direct to ADOR (Pub 1220)**  (2025-01-01 → open) [A.2, US-AZS5-025, direct artifact inspection, conf medium] — Edition: Jan 2025 text speaks of calendar 2024; 2026 edition not located.
- `az.newhire.report_days` = **20** days (2026-01-01 → open) [A.1, US-AZS5-012, direct artifact inspection, conf high] — 23-722.01: DES; electronic two transmissions a month <=16 days apart; includes first day of paid work; no employer penalty.

## 6 — Leave
- `az.leave.sick.accrual.hours_worked_per_hour` = **30** hours (2017-07-01 → open) [A.1, US-AZS5-008, direct artifact inspection, conf high]
- `az.leave.sick.cap_hours.15_plus` = **40** hours (2017-07-01 → open) [A.1, US-AZS5-008, direct artifact inspection, conf high] — Yearly cap 40 h (15+ employees) / 24 h (fewer than 15) unless higher.
- `az.leave.sick.cap_hours.under_15` = **24** hours (2017-07-01 → open) [A.1, US-AZS5-008, direct artifact inspection, conf high]
- `az.leave.sick.waiting_days` = **90** days (2017-07-01 → open) [A.1, US-AZS5-008, direct artifact inspection, conf high]
- `az.leave.sick.rehire_reinstatement_months` = **9** months (2017-07-01 → open) [A.1, US-AZS5-008, direct artifact inspection, conf high]
- `az.leave.sick.payout_on_separation` = **False**  (2017-07-01 → open) [A.1, US-AZS5-008, direct artifact inspection, conf high] — 23-372(F). Paid at normal hourly rate, never below minimum wage; State of AZ and federal employers excluded.

## 7 — Termination and final pay
- `az.final_pay.discharge` = **within 7 working days or end of next regular pay period, whichever sooner; resignation: regular payday of the period**  (2026-01-01 → open) [A.1, US-AZS5-003, direct artifact inspection, conf high] — 23-353. No vacation-payout rule.

## 8 — Benefits in kind / taxable wages
- `az.irc_conformity_date` = **2026-01-01**  (2026-01-01 → open) [A.1, US-AZS5-023, direct artifact inspection, conf high] — 43-105(A); withholding base = federal wages, so federal exclusions flow through.

## 9 — Deductions and garnishments
- `az.deductions.rule` = **only when required by law, with prior revocable written authorization, or during a good-faith wage dispute (23-352)**  (2026-01-01 → open) [A.1, US-AZS5-002, direct artifact inspection, conf high]
- `az.garn.creditor.max_percent` = **10** percent (2026-01-01 → open) [A.1, US-AZS5-016, direct artifact inspection, conf high] — 33-1131(B): lesser of 10% of disposable earnings or excess over 60 x highest applicable minimum wage; support orders 50% exempt. 12-1598.10(F) still cites 25% (AZ OQ-6).
- `az.garn.creditor.minwage_multiple` = **60** ratio (2026-01-01 → open) [A.1, US-AZS5-016, direct artifact inspection, conf high]
- `az.garn.child_support.remit_business_days` = **2** business days (2026-01-01 → open) [A.1, US-AZS5-018, direct artifact inspection, conf high] — 25-504: start within 14 days; employer fee 1 per payment, max 4/month; report termination within 10 days; support priority.
- `az.garn.child_support.employer_fee_per_payment` = **1** USD (2026-01-01 → open) [A.1, US-AZS5-018, direct artifact inspection, conf high]
- `az.garn.child_support.employer_fee_monthly_max` = **4** USD (2026-01-01 → open) [A.1, US-AZS5-018, direct artifact inspection, conf high]

## 10 — Collective agreements / prevailing wage
- `az.prevailing_wage.state_mandate.exists` = False (2026-01-01 → open) [A.1, US-AZP52-003 — promoted to fact in Synthesis C] 34-321(B) bars agencies from requiring prevailing wage.

## 12 — Payroll data protection / records
44-1373 SSN use rules [US-AZS5-019]; sick-time health info confidential (23-377) [US-AZS5-010]; new-hire data purpose limits [US-AZS5-012].

- `az.records.payroll.retention_years` = **4** years (2026-01-01 → open) [A.1, US-AZS5-006, direct artifact inspection, conf high] — 23-364(D): hours each day, wages, sick time paid; employee may inspect and copy.

## 13 — Live legal change
2027: Tucson 16.00; state 2027 poster published 2026-09-25 [US-AZP9M-001] (amount not read); UI Operating Fund 3.15% from 2027-01-01; IRC conformity to 2026-01-01. No ADOR/DES 2026 bulletin sweep (open).


## Special populations (US-OWN-005)
- Domestic: no AZ withholding (43-403(A)(2)); UI threshold not extracted; Tucson MW excludes casual babysitting [US-AZS5-021, US-AZS5-027].
- Agricultural: no withholding for seasonal hand field labour except machine operators (may elect); UI farm thresholds [US-AZS5-021, US-AZS5-014].
- Minors: under-16 hours (23-233); under-18 newspaper carriers UI-excluded [US-AZS5-013, US-AZS5-014].
- Tipped: tip credit up to 3.00 (state and Tucson) [US-AZS5-005, US-AZS5-027].
- Clergy: churches/ministers UI-excluded; no withholding exception (federal wages) [US-AZS5-015, US-AZS5-024].
- Students: own-school students, student nurses/interns, co-op students UI-excluded [US-AZS5-014].
- NRAs / statutory employees: no AZ rule beyond federal; 60-day nonresident rule [US-AZS5-024, US-AZS5-021].
- Government: sick-time law and Tucson MW exclude State and US; school-district pay lag 7 business days [US-AZS5-007, US-AZS5-001].
- Native Americans on own reservation and MSRRA spouses: WEC exemption [US-AZS5-024].
- Nonresident common-carrier/motion-picture/disaster-recovery workers: excluded [US-AZS5-021, US-AZS5-020].

## Language seams (US-OWN-006)
Sick-time notice in English and Spanish (23-375(B)) [US-AZL-001]; minimum-wage and sick-time posters en+es both required [US-AZP9M-001]; pay statement itself English (US-OWN-006).

## Open questions
Mirrors `unresolved[]` in the facts file (same keys).

- `az.minwage.hourly` (blocking) — State minimum wage 2026 (15.15) and 2027 (15.65) are only derived from a 2025 base of 14.70 that no source read confirms; the ICA page returned 403 and the row is tier-C MANUAL (US-AZS5-028). **Would close it:** ICA 2026 and 2027 minimum wage posters (single browser pass); BLS CPI-U from 2019 to check the 2021-2025 chain.
- `az.local_minwage.flagstaff.hourly` (blocking) — Flagstaff local minimum wage not read (guessed URL 404). **Would close it:** flagstaff.az.gov minimum wage ordinance page, 2026 and 2027 values.
- `az.report.sui.quarterly` (non-blocking) — DES UC-018 quarterly wage report format, deadline and e-file mandate, UI separation notice and domestic UI threshold not read (des.az.gov 403). **Would close it:** DES UC-018 instructions and A.R.S. 23-613.01/23-615 remainder via browser pass.
- `az.wh.rounding` (non-blocking) — No rounding rule in 43-401 or the ADOR pages read. **Would close it:** A.A.C. R15-2B-101 on azsos.gov.
- `az.report.w2.pub701_edition` (non-blocking) — Only the Jan 2025 Pub 701 (describing calendar 2024) was found; a 2026 edition not located. **Would close it:** ADOR Pub 701 2026 edition (azdor.gov forms, 403 to curl; browser pass).
- `az.garn.creditor.statute_conflict` (non-blocking) — 33-1131(B) says 10% while 12-1598.10(F) still cites 25%; the 25-510 handling fee amount not read. **Would close it:** Effective date of the Prop. 209 10% amendment and A.R.S. 25-510 text on azleg.
- `az.minwage.statute_23_362_current` (non-blocking) — azleg serves only the 1997 version of 23-362; Prop. 202 definitional text unseen. **Would close it:** Current 23-362 text (Prop. 202) via azleg or Westlaw public.
- `az.pit.departures_from_federal` (non-blocking) — Form 140 additions/subtractions (HSA etc.) not read; assessment level, not withholding. **Would close it:** ADOR Form 140 instructions 2026.
- `az.live.bulletin_sweep` (non-blocking) — ADOR and DES news/bulletins 2026-01-01 to date not swept (DES 403; budget). **Would close it:** ADOR news archive and DES employer bulletins 2026 via browser pass.

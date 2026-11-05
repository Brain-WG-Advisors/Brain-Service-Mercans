# CCG annex_AK research pack — Alaska

Synthesis B, 2026-11-02. Source: `_research/stage5/AK.md` and the active/partial rows of `00-official-sources/legal-basis-register.csv`; no fetching. Facts file: `_research/CCG-annex_AK-facts.json` (validator: PASS). Every value below is a fact object there; key in backticks, register id in brackets.

**Summary.** No individual income tax and no state withholding; no local wage tax. Payroll obligations are UI (employee 0.50% inside which STEP 0.10% and TVEP 0.25% are carved out), minimum wage 14.00 from 2026-07-01 with daily overtime over 8 h, paid sick leave from 2025-07-01, an itemised pay statement (8 AAC 15.160(h), as amended 2025-09-25) and the TQ01C quarterly report. Stage-5 overall confidence about 88%.

## 1 — Employment / labour code
- `ak.minwage.hourly` = **13.0** USD (2025-07-01 → 2026-06-30) [A.1, US-AKS5-001, direct artifact inspection, conf high]
- `ak.minwage.hourly` = **14.0** USD (2026-07-01 → 2027-06-30) [A.2, US-AKS5-002, second independent authority, conf high] — Confirmed on the DOLWD Wage and Hour page updated 2026-05-01.
- `ak.minwage.hourly` = **15.0** USD (2027-07-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high] — Enacted (2024 Ballot Measure 1). From 2028-01-01 indexed to CPI-U Anchorage, rounded up to the next 0.10.
- `ak.minwage.tip_credit.allowed` = **False**  (2025-07-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high] — AS 23.10.065(a): the full minimum wage is due in cash to tipped employees.
- `ak.minwage.school_bus_driver.hourly` = **28.0** USD (2026-07-01 → 2027-06-30) [A.1, US-AKS5-001, direct artifact inspection, conf high] — 2x the state minimum wage (AS 23.10.065(b)).
- `ak.overtime.daily_threshold_hours` = **8** hours (2026-01-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high] — AS 23.10.060: 1.5x over 8 h/day and over 40 h/week; daily OT hours not double-counted toward 40. Employers with fewer than 4 employees exempt.
- `ak.overtime.weekly_threshold_hours` = **40** hours (2026-01-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high]
- `ak.overtime.premium.multiplier` = **1.5** ratio (2026-01-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high]
- `ak.exempt.salary.weekly_min` = **1040.0** USD (2025-07-01 → 2026-06-30) [A.1, US-AKS5-001, derived arithmetically, conf high] — AS 23.10.055(b): 2 x state minimum wage x 40 h = 2 x 13.00 x 40.
- `ak.exempt.salary.weekly_min` = **1120.0** USD (2026-07-01 → 2027-06-30) [A.1, US-AKS5-001, derived arithmetically, conf high] — 2 x 14.00 x 40 (AS 23.10.055(b)).
- `ak.exempt.salary.weekly_min` = **1200.0** USD (2027-07-01 → open) [A.1, US-AKS5-001, derived arithmetically, conf high] — 2 x 15.00 x 40 (AS 23.10.055(b)); enacted rate.
- `ak.pay_frequency.rule` = **monthly or semi-monthly at the employee's election (AS 23.05.140(a))**  (2026-01-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high]
- `ak.direct_deposit.requires_voluntary_authorisation` = **True**  (2026-01-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high] — AS 23.10.043: only if the employee voluntarily authorises it, to the bank of the employee's choice.

## 2 — Income tax (state withholding)
No wage tax: AK has no state W-4, supplemental rate, withholding return, reciprocity or state W-2 filing [US-AK-WT-001, US-AK-WT-002, US-AKP9W-001]. Oracle for income tax: none; the DOLWD UI Tax Calculation Cookbook 2026 is the agency worked example for UI rates [US-AKS5-006].

- `ak.pit.exists` = **False**  (2026-01-01 → open) [A.2, US-AKP9W-001, quoted from authority page, conf high] — No individual income tax and no state income-tax withholding; no state W-4, no withholding return, no state W-2 filing.

## 2b — Non-resident regime and reciprocity
Not applicable: no state income tax, so no resident/non-resident treatment and no reciprocity [US-AK-WT-001]. SUI wage-base credit: wages taxed in another state in the same year for a transferred employee count toward the 54,200 base; TQ01C carries a "wages reported to other states" flag [US-AKS5-005, US-AKS5-013].


## 2c — Local wage taxes
- `ak.local_wage_tax.exists` = **False**  (2026-01-01 → open) [A.2, US-AKR3-001, quoted from authority page, conf high] — No local wage, payroll or income tax; municipal powers are property and sales tax only (US-AKR3-002).

## 3 — Social insurance (SUI / SDI / PFML / levies)
G-DERIVE done in Stage 5 (Python) from the Cookbook: reserve rate 811,365,166 / 17,381,530,724 = 4.668% > 3.3%, solvency credit capped 0.40%; employer 0.73 x ABCR x factor - 0.004 <= 0.16%, so classes 1-20 floor 1.00% and class 21 floor 5.40% [US-AKS5-006]. Workers compensation is an insurer premium outside payroll.

- `ak.sui.wage_base` = **54200.0** USD (2026-01-01 → 2026-12-31) [A.2, US-AKS5-003, derived arithmetically, conf high] — Same figure printed on TQ01C (2/26) [US-AKS5-013]. Mechanism 75% of the AK average annual wage; not re-derived (AK-OQ-1).
- `ak.sui.employee.rate` = **0.5** percent (2026-01-01 → 2026-12-31) [A.2, US-AKS5-003, derived arithmetically, conf high] — Employee UI contribution deducted by the employer. G-DERIVE: 0.27 x ABCR = 0.12%, so the 0.50% floor applies [US-AKS5-006].
- `ak.sui.employer.rate.classes_01_20` = **1.0** percent (2026-01-01 → 2026-12-31) [A.2, US-AKS5-003, derived arithmetically, conf high] — Derivation recorded in register row US-AKS5-003: 2026 taxable wage base 54,200.00 USD; employee rate 0.50%; employer rate classes 01-20 = 1.00% (total 1.50%), class 21 = 5.40% employer + 0.50% employee = 5.90%; total rate = employer + employee; effective 2026-01-01 through 2026-12-31. 2027 page (2027-experience-rates.html) returned HTTP 404 on 202
- `ak.sui.employer.rate.class_21` = **5.4** percent (2026-01-01 → 2026-12-31) [A.2, US-AKS5-003, derived arithmetically, conf high] — Derivation recorded in register row US-AKS5-003: 2026 taxable wage base 54,200.00 USD; employee rate 0.50%; employer rate classes 01-20 = 1.00% (total 1.50%), class 21 = 5.40% employer + 0.50% employee = 5.90%; total rate = employer + employee; effective 2026-01-01 through 2026-12-31. 2027 page (2027-experience-rates.html) returned HTTP 404 on 202
- `ak.sui.new_employer.rate` = **1.0** percent (2026-01-01 → 2026-12-31) [A.2, US-AKS5-004, derived arithmetically, conf high] — Every industry; total with employee share 1.50%.
- `ak.sui.abcr` = **0.004615** ratio (2026-01-01 → 2026-12-31) [A.2, US-AKS5-006, derived arithmetically, conf high] — ABCR = (131,477,612 / 45,628,865,425) / (10,852,857,547 / 17,381,530,724), DOLWD UI Tax Calculation Cookbook 2026 (updated 2025-12-04). Reproduces every published 2026 rate.
- `ak.step.rate_within_employee_ui` = **0.1** percent (2026-01-01 → open) [A.2, US-AKP7-001, quoted from authority page, conf high] — Collected inside the employee 0.50% and credited back; net cost nil. No employer STEP tax (SB 217 not enacted).
- `ak.tvep.rate_within_employee_ui` = **0.25** percent (2026-01-01 → open) [A.2, US-AKP7-002, quoted from authority page, conf high] — Collected inside the employee 0.50%; net cost nil.
- `ak.sdi_pfml.exists` = **False**  (2026-01-01 → open) [A.2, US-AKP9W-001, quoted from authority page, conf high] — No SDI/TDI/PFML/LTC/transit levy. AFLA covers public employers only and is unpaid.

## 4 — Payslip statute
- `ak.payslip.required` = **True**  (2025-09-25 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high] — 8 AAC 15.160(h): written or electronic statement each pay period: rate, gross, net, period dates, FIT and FICA, AK ESA contributions, board/lodging, advances, straight-time and OT hours, other deductions, sick leave used in accrual year and sick leave balance (PTO used/balance satisfies, FAQ Q13 US-AKS5-010).
- `ak.payslip.sick_leave_balance.required` = **True**  (2025-09-25 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high]

## 5 — Statutory reporting instruments
No state withholding return/reconciliation/W-2 filing. Quarterly UI TQ01C with employer-level monthly counts (12th), excess wages and other-states flag; corrections on TADJ [US-AKS5-013]. Registration TREG; Notice to Employees placard 07-1012 [US-AKS5-015]. New hire within 20 days via myAlaska; CSED ACSESS Business Portal since 2025-10-06 [US-AKS5-007, US-AKS5-008].

- `ak.report.sui.quarterly.form` = **TQ01C (2/26) with wage schedule; due last day of month after quarter; zero report required; wages reported in quarter paid**  (2026-01-01 → open) [A.3, US-AKS5-013, direct artifact inspection, conf high]
- `ak.report.sui.quarterly.late_penalty_min` = **10.0** USD (2026-01-01 → open) [A.3, US-AKS5-005, direct artifact inspection, conf medium]
- `ak.report.sui.employee_fields` = **SSN, name, reportable wages, occupational code (6 or 8 digit), 2-digit geographic code**  (2026-01-01 → open) [A.3, US-AKS5-013, direct artifact inspection, conf high] — Alaska-specific DD fields.
- `ak.report.sui.channel` = **file_upload (CSV, no headings; header 11 cols, detail 12 cols, rev. 2016-05-17) or online keying or paper**  (2026-01-01 → open) [A.2, US-AKS5-014, direct artifact inspection, conf high]
- `ak.report.sui.online_mandatory_threshold_employees` = **50** employees (2026-01-01 → open) [A.3, US-AKS5-005, direct artifact inspection, conf medium] — Also mandatory with 1M+ taxable wages in current or prior year, or when a payroll agent files.
- `ak.newhire.report_days` = **20** days (2026-01-01 → open) [A.3, US-AKS5-007, direct artifact inspection, conf medium] — AS 25.27.075 (statute text not read). Online via myAlaska; fax no longer accepted. Penalty 10 USD/employee.

## 6 — Leave
- `ak.leave.sick.accrual.hours_worked_per_hour` = **30** hours (2025-07-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high] — 1 h per 30 h worked, overtime included (AS 23.10.067).
- `ak.leave.sick.cap_hours.under_15_fte` = **40** hours (2025-07-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high] — Cap on accrual and use per year; FTE counted on prior calendar year (8 AAC 15.106).
- `ak.leave.sick.cap_hours.15_plus_fte` = **56** hours (2025-07-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high]
- `ak.leave.sick.payout_on_separation` = **False**  (2025-07-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high] — AS 23.10.068(a)(1). Reinstated on rehire within 6 months.
- `ak.leave.sick.rehire_reinstatement_months` = **6** months (2025-07-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high]

## 7 — Termination and final pay
No statute requires vacation payout (AK-OQ-2 open); no state WARN; return-transport duty AS 23.10.375-.400 not modelled.

- `ak.final_pay.discharge.working_days` = **3** working days (2026-01-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high] — AS 23.05.140(b). Resignation: next regular payday at least 3 days after notice.
- `ak.final_pay.penalty.max_working_days` = **90** working days (2026-01-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high]

## 8 — Benefits in kind / taxable wages
- `ak.sui.wages.excludes_401k_deferrals` = **True**  (2026-01-01 → open) [A.3, US-AKS5-005, direct artifact inspection, conf medium] — AS 23.20.530 per ES Tax Handbook (A.3): 401(k)/403(b)/457/SEP/SIMPLE deferrals excluded from UI wages, unlike FUTA; dependent care, adoption, group legal and cash cafeteria elections ARE UI wages.
- `ak.board_lodging.no_determination_max_per_day` = **20.0** USD (2026-01-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high] — 8 AAC 15.160(d)-(f); prior written notice and signed acceptance required.

## 9 — Deductions and garnishments
Deductions only by written agreement and never below minimum wage/overtime (8 AAC 15.160(a)-(g)). Child support IWO per federal CCPA, remitted via CSED ACSESS [US-AKS5-008]; AK fee/priority unread (AK-OQ-4). Nonresident debtor: federal 30x/75% rule [US-AKS5-017].

- `ak.garn.exempt.weekly` = **473.0** USD (2026-01-01 → open) [A.1, US-AKS5-017, second independent authority, conf medium] — Greater of 473/week or 75% of disposable earnings (AS 09.38.030, CPI-adjusted per 8 AAC 95.030, not read; amounts via CIV-530 8/24). Monthly / 4.3, semi-monthly / 2.17.
- `ak.garn.exempt.weekly_household_support` = **743.0** USD (2026-01-01 → open) [A.1, US-AKS5-017, second independent authority, conf medium]
- `ak.garn.exempt.liquid_assets_monthly` = **1890.0** USD (2026-01-01 → open) [A.1, US-AKS5-017, second independent authority, conf medium]

## 10 — Collective agreements / prevailing wage
Title 36 public construction over 25,000 USD: DOLWD prevailing-wage determination (Pamphlet 600) [US-AK-P5-1-005 — legacy id, narrative only: its id fails the facts.schema pattern, so the threshold is not emitted as a fact]. Certified payroll, Notice of Work and Notice of Completion to DOLWD LSS; online/bulk upload optional, paper allowed [US-AKS5-018]. Multiemployer CBA funds may satisfy sick leave (068(e)).

- `ak.prevailing_wage.threshold` = 25000.0 (2026-01-01 → open) [A.1, US-AK-P5-1-005 — legacy id, NOT a fact] Title 36 public construction over 25,000 USD.

## 11 — Indexation
Minimum wage CPI-U Anchorage from 2028-01-01 (no indexed value yet, so no derivation possible); EAP threshold and school-bus rate follow at 2x; UI base 75% of AAW (2027 not published, HTTP 404 on 2026-11-02); garnishment exemptions CPI (AS 09.38.115).


## 12 — Payroll data protection / records
AS 45.48.400-.480: SSN not on mailed material; recommendation omit/truncate SSN on every pay statement [US-AKS5-016].

- `ak.records.wage_hour.retention_years` = **3** years (2026-01-01 → open) [A.1, US-AKS5-001, direct artifact inspection, conf high] — AS 23.10.100, at the place of employment (central in-state office counts, 8 AAC 15.900).
- `ak.records.ui.retention_years` = **5** years (2026-01-01 → open) [A.3, US-AKS5-005, direct artifact inspection, conf medium] — ES Tax Handbook (A.3).

## 13 — Live legal change
- `ak.live.sb217_employer_step.status` = **not enacted (in S FIN since 2026-04-15); would operate at UI employer contribution level**  (2026-04-15 → open) [A.1, US-AKS5-012, direct artifact inspection, conf high]
- `ak.live.hb161_sick_leave.status` = **not enacted (referred H L&C 2025-03-28, never moved)**  (2025-03-28 → open) [A.1, US-AKS5-011, direct artifact inspection, conf high]

## Special populations (US-OWN-005)
- Domestic/household: exempt from W&H minimum wage, OT and sick leave (23.10.055(a)(4)); UI-excluded under 1,000/quarter [US-AKS5-001, US-AKS5-005].
- Agricultural: exempt from MW, OT, sick leave; UI-excluded under 20,000/quarter or fewer than 10 workers [US-AKS5-001, US-AKS5-005].
- Commercial fishing: crews exempt from W&H and sick leave; UI-excluded if fewer than 10 crew paid on shares; seamen OT-exempt [US-AKS5-001, US-AKS5-005].
- Minors under 18 part-time (30 h/week or less): exempt from W&H and sick leave except in a week over 30 h (8 AAC 15.135) [US-AKS5-001, US-AKS5-010].
- Tipped: no tip credit; full minimum wage in cash (8 AAC 15.907) [US-AKS5-001].
- Clergy/religious orders: UI-excluded; religious nonprofit volunteers W&H-exempt [US-AKS5-005, US-AKS5-001].
- Students at own school and work-study under 22: UI-excluded; student learners MW exemption by certificate (8 AAC 15.125) [US-AKS5-005, US-AKS5-001].
- Nonresident aliens: no state rule beyond federal [US-AK-WT-001].
- Corporate officers: UI-excluded unless the employer elects coverage for all officers; commission insurance/real-estate/stock agents UI-excluded when FUTA-excluded [US-AKS5-005].
- Government: W&H MW/OT and sick-leave exempt; UI contributory or reimbursable; AFLA unpaid leave [US-AKS5-001, US-AKS5-005].
- Nonprofit: UI at 250/quarter or 4+ employees in 20 weeks; reimbursable option; summer camps reduced wage up to 12 weeks [US-AKS5-005, US-AKS5-001].
- Multistate: SUI credit for other-state wages of transferred employees [US-AKS5-005]; sick-leave reach to partly-in-state workers open (AK-OQ-6).

## Language seams (US-OWN-006)
No language clause in the pay-statement rule or posters [US-AKL-001, US-AKP9L-001]: payslip and filings in English (US-OWN-006).

## Open questions
Mirrors `unresolved[]` in the facts file (same keys).

- `ak.prevailing_wage.threshold` (non-blocking) — Value 25000.0 (from 2026-01-01) is carried by register row US-AK-P5-1-005 (active, A.1, Alaska Legislature), but that legacy id fails the facts.schema register_id pattern, so it cannot be emitted as a fact. Title 36 public construction over 25,000 USD. **Would close it:** Final merge: register an S5-pattern alias row (same url/figure, supersedes US-AK-P5-1-005) or re-key US-AK-P5-1-005; then emit this key as a fact. No new research needed.
- `ak.sui.wage_base.derivation` (non-blocking) — The 2026 wage base 54,200 is published but not re-derived: the average annual wage worksheet (75% rule) was not obtained. **Would close it:** DOLWD Research and Analysis "Tax Base Calculation worksheet" 2026, or the signed "AK UI Tax Rates 2026 Full Document" (2026-01-21) attached to SB 217 on BASIS.
- `ak.final_pay.accrued_vacation.payout` (non-blocking) — No statute requires vacation payout; whether accrued vacation is wages due under AS 23.05.140(b) absent a forfeiture policy was not read. **Would close it:** DOLWD Wage and Hour position (Pamphlet 100 index or W&H FAQ) or Alaska Supreme Court case law on an official host.
- `ak.paycard.rule` (non-blocking) — No paycard statute located; AS 23.10.040 requires money or negotiable check and AS 23.10.043 voluntary deposit authorisation. **Would close it:** A DOLWD Wage and Hour opinion on payroll cards.
- `ak.garn.iwo.employer_fee` (non-blocking) — AS 25.27.062 IWO employer fee, priority and remittance deadline not read; akleg.gov unreachable (HTTP 000) and CSED employer pages 404 after the 2025-10 site change. **Would close it:** AS 25.27.062 read through VPN on akleg, or the CSED ACSESS Business Portal employer guide.
- `ak.prevailing_wage.certified_payroll.frequency` (non-blocking) — AS 36.05.040 not read (akleg unreachable) and the Pamphlet 600 edition in force not confirmed. **Would close it:** AS 36.05.040 on akleg and the current Pamphlet 600 at labor.alaska.gov/lss.
- `ak.leave.sick.multistate_coverage` (non-blocking) — The sick leave statute covers employers in Alaska with no hours-in-state threshold; the FAQ (2026-01-28) is silent on partly-in-state and remote workers. **Would close it:** A DOLWD LSS interpretation on coverage of employees working partly in Alaska.
- `ak.live.bulletin_sweep` (non-blocking) — The Alaska Administrative Register 2026 (8 AAC amendments) and 2026 special sessions were not swept (akleg unreachable without VPN). **Would close it:** Lt. Governor Online Public Notices / Administrative Register issues 2026-01..10 and the BASIS Passed Legislation list of the 34th Legislature, read with VPN.
- `ak.sui.wage_base.next_year` (non-blocking) — 2027 wage base and rates not yet published (labor.alaska.gov/estax/2027-experience-rates.html HTTP 404 on 2026-11-02): timing gap. **Would close it:** DOLWD 2027 experience-rates page once published (normally December).

# CCG research pack - annex_NM (New Mexico)

Synthesis-B worker MN-WY, 2026-11-02. Unit `annex_NM` of the CCG (jurisdiction annex, all 13 domains + special populations).
Facts file: `_research/CCG-annex_NM-facts.json` (42 facts, 15 pending on the register_id pattern defect, 11 unresolved). Every claim below carries its register_id inline; numbers may be cited in the CCG only through a fact key.

## 0. How to use this pack

- Body sections 1-13 and Special populations are the stage-5 findings (`_research/stage5/NM.md`), carried verbatim because they are already organised by the 13 CCG domains with register ids inline.
- Federal layer (FIT, FICA, FUTA, W-2/941/940), the multistate rules (reciprocity, sourcing) and the language seams (US-OWN-006: payslip in English; second-language duties attach to notices and posters only) live in annex_FED / annex_MULTI and are not repeated here.
- Special populations (US-OWN-005): the state-level rules are in the Special populations table below; the country-wide coverage matrix is CCG unit `coverage`.
- Values are 2026 unless the fact says otherwise. 2027 values appear only where the row carries an enacted or published 2027 figure; projections are never facts.

## 0.1 Synthesis decisions and traps (bind the builder)

- Workers' compensation admin fee has an EMPLOYEE share (2.25/quarter) deducted from pay and reported on TRD-41431 [US-NMR3-001].
- Garnishment floor follows the highest applicable minimum wage at place of work (40x), e.g. 616/week in Santa Fe from 2026-03-01.
- Oracle: FYI-104 weekly married 1,000 = 41.80 (incl. 20.00 extra).

## 0.2 Register status check of the ids cited in the findings

All ids cited in the findings are `active` in the register.

## 0.3 Facts emitted

| key | value | from | to | register_id | conf |
|---|---|---|---|---|---|
| `nm.minwage.hourly` | 12.0 USD | 2023-01-01 |  | US-NMS5-004 | high |
| `nm.labour.minwage.student.hourly` | 8.5 USD | 2020-01-01 |  | US-NMS5-004 | high |
| `nm.minwage.tipped.cash_wage` | 3.0 USD | 2020-01-01 |  | US-NMS5-004 | high |
| `nm.overtime.weekly_threshold_hours` | 40 hours | 2020-01-01 |  | US-NMS5-004 | high |
| `nm.overtime.premium.multiplier` | 1.5 ratio | 2020-01-01 |  | US-NMS5-004 | high |
| `nm.labour.minwage.local.albuquerque.hourly` | 12.0 USD | 2026-01-01 | 2026-12-31 | US-NMS5-006 | high |
| `nm.labour.minwage.local.albuquerque.hourly` | 13.0 USD | 2027-01-01 |  | US-NMS5-006 | high |
| `nm.labour.minwage.local.albuquerque.tipped.hourly` | 7.2 USD | 2026-01-01 |  | US-NMS5-006 | high |
| `nm.labour.minwage.local.santa_fe_city.hourly` | 15.0 USD | 2025-03-01 | 2026-02-28 | US-NMS5-007 | high |
| `nm.labour.minwage.local.santa_fe_city.hourly` | 15.4 USD | 2026-03-01 | 2026-12-31 | US-NMS5-007 | high |
| `nm.labour.minwage.local.santa_fe_city.hourly` | 17.5 USD | 2027-01-01 |  | US-NMS5-007 | high |
| `nm.labour.minwage.local.santa_fe_city.tipped_base.hourly` | 3.0 USD | 2026-03-01 |  | US-NMS5-007 | high |
| `nm.pay_frequency.rule` | paydays max 16 days apart; days 1-15 by 25th; 16-end by 10th of next month | 2026-01-01 |  | US-NMP8-001 | high |
| `nm.labour.direct_deposit.consent_required` | True | 2026-01-01 |  | US-NMP8-001 | high |
| `nm.pit.tribal.exempt` | income wholly earned on own-tribe lands while living there | 2026-01-01 |  | US-NMS5-013 | high |
| `nm.sui.employer.rate.min` | 0.33 % | 2026-01-01 | 2026-12-31 | US-NMS5-008 | high |
| `nm.sui.employer.rate.max` | 5.4 % | 2026-01-01 | 2026-12-31 | US-NMS5-008 | high |
| `nm.ui.reserve_factor` | 3.6361 ratio | 2026-01-01 | 2026-12-31 | US-NMS5-008 | high |
| `nm.sui.employee.rate` | 0 % | 2026-01-01 |  | US-NMS5-016 | high |
| `nm.wc.admin_fee.employer.quarterly` | 2.55 USD | 2025-07-01 | 2028-06-30 | US-NMR3-001 | high |
| `nm.wc.admin_fee.employee.quarterly` | 2.25 USD | 2025-07-01 | 2028-06-30 | US-NMR3-001 | high |
| `nm.wc.admin_fee.employer.quarterly` | 2.68 USD | 2028-07-01 | 2033-06-30 | US-NMR3-001 | high |
| `nm.wc.admin_fee.employee.quarterly` | 2.38 USD | 2028-07-01 | 2033-06-30 | US-NMR3-001 | high |
| `nm.sdi_pfml.exists` | False | 2026-01-01 |  | US-NMR3-002 | high |
| `nm.payslip.items` | employer identity, gross pay, hours worked, total wages and benefits, itemized deductions | 2026-01-01 |  | US-NMP8-001 | high |
| `nm.payslip.sick_leave_summary` | YTD earned sick leave accrued and used at least quarterly | 2022-07-01 |  | US-NMS5-002 | high |
| `nm.records.sick_leave.retention_months` | 48 months | 2022-07-01 |  | US-NMS5-002 | high |
| `nm.report.trd41414.due` | 25th of month after period (monthly/quarterly/semiannual per certificate) | 2026-01-01 |  | US-NMS5-011 | high |
| `nm.report.trd41431.due` | 25th after quarter end | 2026-01-01 |  | US-NMS5-012 | high |
| `nm.report.ui.quarterly_due` | last day of month after quarter, electronic only | 2026-01-01 |  | US-NMS5-016 | high |
| `nm.newhire.report_days` | 20 days | 1997-10-01 |  | US-NMS5-010 | high |
| `nm.leave.paid_sick.accrual_ratio_hours_worked` | 30 hours | 2022-07-01 |  | US-NMS5-001 | high |
| `nm.leave.paid_sick.annual_cap_hours` | 64 hours | 2022-07-01 |  | US-NMS5-001 | high |
| `nm.leave.sick.payout_on_separation` | False | 2022-07-01 |  | US-NMS5-001 | high |
| `nm.final_pay.discharge` | fixed wages within 5 days; task/piece/commission within 10 days | 2026-01-01 |  | US-NMS5-014 | medium |
| `nm.term.final_pay.quit` | next regular payday | 2026-01-01 |  | US-NMS5-014 | medium |
| `nm.term.vacation.payout` | owed if written policy grants it (vacation pay is wages) | 2017-11-14 |  | US-NMS5-003 | medium |
| `nm.garn.consumer.exempt_multiple_minwage` | 40 | 2023-07-01 |  | US-NMS5-015 | high |
| `nm.garn.consumer.exempt.weekly.state` | 480 USD | 2023-07-01 |  | US-NMS5-015 | high |
| `nm.garn.support.max_rate` | 50 % | 2023-07-01 |  | US-NMS5-015 | high |
| `nm.prevailing_wage.threshold` | 60000 USD | 2026-01-01 |  | US-NMR3-003 | high |
| `nm.prevailing_wage.certified_payroll` | weekly payrolls submitted every two weeks within 5 working days; kept 4 years | 1972-05-31 |  | US-NMS5-009 | high |
| `nm.wh.certificate` | no state form; optional federal W-4 copy marked For New Mexico State Withholding Only | 2026-01-01 |  | US-NM-P5-2-001 (PENDING id pattern) | high |
| `nm.wh.method` | FYI-104 Rev. 11/2025 percentage tables; standard deduction built in; no allowances | 2026-01-01 | 2026-12-31 | US-NM-P5-2-001 (PENDING id pattern) | high |
| `nm.pit.wh.single.zero_bracket` | 8050 USD | 2026-01-01 | 2026-12-31 | US-NM-P5-2-001 (PENDING id pattern) | high |
| `nm.pit.wh.single.band_starts` | 0;5500;16500;33500;66500;210000 | 2026-01-01 | 2026-12-31 | US-NM-P5-2-001 (PENDING id pattern) | high |
| `nm.pit.wh.rates` | 1.5;3.2;4.3;4.7;4.9;5.9 | 2026-01-01 | 2026-12-31 | US-NM-P5-2-001 (PENDING id pattern) | high |
| `nm.pit.wh.rate.top` | 5.9 % | 2026-01-01 | 2026-12-31 | US-NM-P5-2-001 (PENDING id pattern) | high |
| `nm.wh.supplemental.rate` | 5.9 % | 2026-01-01 | 2026-12-31 | US-NM-P5-2-001 (PENDING id pattern) | high |
| `nm.pit.oracle.example_1.withholding` | 41.8 USD | 2026-01-01 | 2026-12-31 | US-NM-P5-2-001 (PENDING id pattern) | high |
| `nm.pit.nonresident.days_threshold` | 15 days | 2026-01-01 |  | US-NM-P5-2-002 (PENDING id pattern) | high |
| `nm.reciprocity.states` | none | 2026-01-01 |  | US-NM-P5-2-002 (PENDING id pattern) | high |
| `nm.local_wage_tax.exists` | False | 2026-10-29 |  | US-NM-P5-2-003 (PENDING id pattern) | high |
| `nm.sui.wage_base` | 34800 USD | 2026-01-01 | 2026-12-31 | US-NM-P5-1-001 (PENDING id pattern) | high |
| `nm.sui.wage_base` | 33200 USD | 2025-01-01 | 2025-12-31 | US-NM-P5-1-001 (PENDING id pattern) | high |
| `nm.ui.rate.new_employer.min` | 1.0 % | 2026-01-01 | 2026-12-31 | US-NM-P5-1-002 (PENDING id pattern) | high |
| `nm.report.w2.due` | 31 January, electronic only | 2026-01-01 |  | US-NM-P5-2-005 (PENDING id pattern) | high |

# Findings by domain (stage 5)

## 1 — labour_code
- **State minimum wage:**
  - 12.00 USD/h on and after 2023-01-01, 50-4-22(A). SB 437 (2019) sets no indexation [US-NMS5-004, A.1, high].
  - DWS restates 12.00 from 2023-01-01 and "the state will enforce the highest available rate" [US-NMS5-005, A.2].
  - **2026 = 12.00. 2027 = 12.00, unless a 2026-session change was enacted.** The search found none (medium-high confidence).
- **Sub-minimum rates** [US-NMS5-004]:
  - Secondary-school students working after school or out of session: 8.50/h (50-4-22(B)).
  - Tipped employees (more than 30 USD/month in tips): cash wage 3.00/h, and tips plus cash must reach the minimum. Tips belong to the employee, but wait staff may pool tips (50-4-22(D)).
  - Agriculture: the employer may deduct the reasonable value of food, utilities, supplies and housing (50-4-22(C)).
- **Exclusions from "employee" (50-4-21(C)):**
  - domestic service in a private home;
  - bona fide executive, administrative and professional staff, and supervisors (test in 11.1.4.7(F) NMAC [US-NMS5-003]);
  - commission or piecework salespersons;
  - registered apprentices and learners;
  - under-18 non-students;
  - G.I. Bill trainees;
  - certified seasonal camp staff;
  - listed agricultural workers;
  - agricultural-commodity processing;
  - residential nonprofit staff.
  - State and political-subdivision employees are covered for the minimum-wage rate only.
- **Overtime:** 1.5x the regular rate for hours over 40 in a 7-day week (50-4-22(E)) [US-NMS5-004, high]. There is no daily overtime.
- **Local minimum wages.** DWS lists five ordinances: Albuquerque, Bernalillo County, Las Cruces, City of Santa Fe and Santa Fe County [US-NMS5-005].
  - **Albuquerque** [US-NMS5-006, A.2, high]:
    - 2026: 12.00.
    - From 2027-01-01: 13.00. The rate stays 12.00 if the employer provides healthcare or childcare benefits worth at least 2,500 USD a year.
    - Tipped cash wage: 7.20 in 2026 and 2027.
  - **City of Santa Fe** [US-NMS5-007, A.2, high]:
    - 15.40 from 2026-03-01; it was 15.00 in 2025.
    - 17.50 from 2027-01-01.
    - From 2028-03-01, the annual change is 50% Western CPI plus 50% HUD fair market rent, capped at 5%.
    - Tipped or commissioned staff earning at least 100 USD/month: base 3.00/h, with tips topping up to 15.40.
  - **Bernalillo County, Santa Fe County and Las Cruces:** NOT READ. The hosts returned 403 or 404 (see ACCESS gaps).
- **Pay frequency** (50-4-2(A) as amended 2005) [US-NMP8-001, A.1]:
  - Paydays at most 16 days apart.
  - Wages for days 1-15 are due by the 25th. Wages for day 16 to month end are due by the 10th of the next month.
  - Where payroll is computed centrally outside NM: by the last day of the month, and by the 15th of the next month.
  - FLSA-exempt professional, administrative, executive and outside-sales staff may be paid monthly, unless covered by a CBA (C).
  - Task, piece or commission pay may be paid monthly by the 10th of the next month, if agreed in writing at hire (B).
- **Method of payment** (50-4-2(B)):
  - Lawful money, or a check or draft convertible to cash at full face value.
  - Direct deposit needs the voluntary authorization of the employer, the employee and the financial institution [US-NMP8-001].
  - No paycard rule was located (open).
- **Minors:** a work permit is ordinarily required under 16 (11.1.4.9 NMAC) [US-NMS5-003]. Hour limits are in the Child Labor Act, 50-6, which was not read.

## 2 — income_tax
- **Withholding form:** there is no state form. The employee may complete a copy of the federal W-4 marked "For New Mexico State Withholding Only" (a convenience, not mandatory).
- **Method:** percentage-method tables, FYI-104 Rev. 11/2025, for wages paid on or after 2026-01-01.
  - Tables 1-8 cover weekly, biweekly, semimonthly, monthly, quarterly, semiannual, annual, and daily/miscellaneous pay.
  - Each table has single, married and head-of-household columns. Rates run from 1.5% to 5.9%.
  - The standard deduction is built in, and there are no allowance amounts.
  - No withholding is due if it would be under 1 USD in a month.
  - Sources: [US-NM-P5-2-001, A.2, high].
- **G-DERIVE** (Python, `scratchpad/NM/derive.py`). Annual single table: zero bracket 8,050; band starts at taxable income 0 / 5,500 / 16,500 / 33,500 / 66,500 / 210,000 at 1.5 / 3.2 / 4.3 / 4.7 / 4.9 / 5.9%.
  - The cumulative base reproduces exactly: 82.50, 434.50, 1,165.50, 2,716.50, then 9,748.00 at 218,050.
  - Married annual reproduces 14,624.00 at 331,100.
  - FYI-104 worked example (weekly, married, 1,000): 12.77 + 210 x 4.3% = 21.80; plus 20.00 extra requested = 41.80. This reproduces.
  - Some printed tables split one rate band into two rows (e.g. 3.2% at 13,550-20,550 and 20,550-24,550). The arithmetic shows these are continuous.
- **Supplemental wages:** use the same method as federal. If federal withholding uses the flat percentage, withhold a flat **5.9%**. Table 8 is recommended for bonuses or overtime paid separately. A married employee who chose the single rate federally uses single for NM [US-NM-P5-2-001].
- **Rounding:** no rule stated in FYI-104. Tables run to cents (open).
- **Residents and nonresidents:**
  - NM residents are withheld on all wages, wherever earned.
  - Nonresidents are withheld only on NM wages. No withholding is required for nonresidents working 15 or fewer days in NM in the calendar year [US-NM-P5-2-002].
  - Resident credit for another state's tax operates at **assessment**. NM withholding may be reduced or eliminated through the NM-only W-4 [US-NM-P5-2-002].
  - No reciprocity agreement exists.
- **Exempt income** [US-NMS5-013; FYI-104]:
  - Income wholly earned by an enrolled member of a NM tribe or pueblo, on the lands of the nation where the member is enrolled and lives.
  - Active-duty military pay, and the pay of military spouses who keep the out-of-state residence.
- **Local income tax:** none. TRD's list of all taxes has no local wage tax [US-NM-P5-2-003].
- **Oracle:** none (no TRD calculator). Use the FYI-104 tables and worked example.

## 3 — social_security
- **SUI rates and base:**
  - 2026 taxable wage base 34,800 USD (33,200 in 2025) [US-NM-P5-1-001].
  - New employer: the greater of the NAICS industry average or 1%. 2026 industry rates run from 1.00 to 1.28 [US-NM-P5-1-002].
  - Experience rate = benefit ratio x reserve factor (2026 = 3.6361) x experience history factor (0.40-1.00).
  - Floor 0.33%, cap 5.4%. When the uncapped rate exceeds 5.4%, an excess-claims premium of (rate - 5.4%) x 10% is added, at most 1% [US-NMS5-008, A.2, high].
  - **No employee UI contribution.** Deducting UI from wages is prohibited [US-NMS5-016, A.3].
- **Wage base indexation:** 60% of the state average annual earnings of the second preceding year, rounded up to the next 100 USD [US-NMS5-016]. No G-DERIVE was possible because the average-wage input was not obtained.
- **Coverage thresholds:**
  - non-agricultural: 450 USD in a quarter, or 1 worker in 20 weeks;
  - agricultural: 20,000 USD in a quarter, or 10 workers in 20 weeks;
  - domestic: 1,000 USD in a quarter.
  - Exempt employers and wages are in 51-1-42(E)/(F), which was not read [US-NMS5-016].
- **SDI, TDI, PFML and LTC:** none. There is no enacted PFML Act, and the DWS page describes only the 2022 task force [US-NMR3-002]. The 2026-session search found no enacted PFML.
- **Workers' compensation administration fee** (52-5-19), per employee per quarter, on TRD-41431 [US-NMR3-001; US-NMS5-012]:
  - employer 2.55 and employee 2.25 from 2025-07-01 to 2028-06-30;
  - then 2.68 / 2.38 until 2033-06-30;
  - then 2.80 / 2.50.
  - The employee share is a payroll deduction.

## 4 — payslip_statute
- **Written receipt each payday** (50-4-2(B)) [US-NMP8-001, A.1; reprinted 2023, US-NMP8-002]. It must show:
  - employer identity;
  - gross pay;
  - hours worked;
  - total wages and benefits earned;
  - an itemized list of deductions.
- **Sick-leave summary:** a year-to-date written summary of earned sick leave accrued and used is required at least quarterly. It may be on the earnings statement or electronic [US-NMS5-002].
- **Electronic delivery:** no consent rule located (open).
- **Retention:**
  - sick-leave and hours records: 48 months [US-NMS5-001/-002];
  - UI wage records (handbook) [US-NMS5-016];
  - certified payrolls: 4 years after the contract [US-NMS5-009].
  - No general 50-4 retention period was read.

## 5 — reporting_instruments
- **Withholding return, TRD-41414:**
  - Monthly, quarterly or semiannual, as shown on the TRD registration certificate. The instructions state no dollar thresholds.
  - Due the 25th of the month after the period. A zero return is required.
  - Sources: [US-NMS5-011, A.2; FYI-104].
- **TRD-41431, new from 2026-01-01** (HB 218 of 2025): Workers' Compensation Fee Return and Employees' Quarterly Wage and Withholding Report.
  - Content: gross wages and NM tax withheld per employee.
  - Due the 25th after quarter end [FYI-104; US-NMS5-012].
- **E-file and e-pay mandate** for TRD-41414, TRD-41431 and TRD-41409 from 2026, under 9-11-6.4 [US-NMS5-012].
  - A TAP bulk-filing schema was announced for mid-January 2026. **Not obtained:** it is inside TAP Help.
- **Annual W-2:**
  - Electronic only from 2026, regardless of employer size.
  - Channels: TAP bulk TXT upload, or the Combined Federal/State Filing Program (code 35; NMBTIN in positions 663-722 of the B record).
  - Due **31 January** to both TRD and employees [FYI-330 Rev. 12/2025, US-NM-P5-2-005].
  - **Conflict:** TRD's live withholding page still says "last day of February" [US-NMS5-013]. Build on FYI-330.
  - The TAP TXT layout (likely EFW2) was not read (open).
  - RPD-41072 annual summary is optional.
- **UI quarterly wage and contribution report:** due the last day of the month after quarter end, electronic only [US-NMS5-016]. Published formats: Delimited, ICESA, XML, EFW2 [US-NMS5-008]. The specs were not read (dws.nm.gov returns 403).
- **New hire:**
  - Report within 20 days, or in two monthly transmissions 16 days apart. Covers rehires after 60 or more days.
  - Fields: FEIN, employer name and address; employee name, address, SSN, hire date (optional: date of birth, state of hire).
  - Channel: nm-newhire.com. Basis: NMSA 50-13-1 to 50-13-4 [US-NMS5-010, A.3].
- **Registration:** TRD (ACD-31015, NMBTIN) and the DWS UI Tax & Claims System.
- **POA:** ACD-31102 [US-NM-P5-1-004]; ES-905 or a third-party administrator login [US-NMP6-001].

## 6 — leave
- **Paid sick leave:** Healthy Workplaces Act, NMSA 50-17-1 to -12, effective 2022-07-01 [US-NMS5-001, A.1; US-NMS5-002, A.1]. Applies to all private employers with 1 or more employees.
  - Accrual: 1 h per 30 h worked, or frontloading of 64 h each 1 January (pro rata for new hires). FLSA-exempt staff are assumed to work 40 h. Hours over 40 accrue at 1:30 only.
  - Use cap: 64 h per 12 months. Unused leave carries over.
  - **No payout at separation.** Leave is reinstated on rehire within 12 months.
  - Pay: the same hourly rate and benefits, never below the minimum wage, for the scheduled hours (fluctuating schedules: average of the prior 2 weeks). Paid on the regular payday.
  - Frontloaded leave may not be recouped by payroll deduction.
- **PFML:** none [US-NMR3-002].
- **Vacation pay** is "wages" where compensation under the employer's written policy (11.1.4.7(O) NMAC) [US-NMS5-003]. It is therefore owed at separation if the policy grants it. No statutory payout mandate was located.

## 7 — termination
- **Discharge:** fixed wages are due on demand and must be paid within 5 days. Task, piece or commission pay within 10 days.
- **Penalty:** wages continue at the same rate until paid (demand required), up to day 60 (50-4-4).
- **Quit:** paid on the next regular payday (50-4-5).
- **Dispute:** the employer pays the conceded amount unconditionally (50-4-7).
- These rules were read from a 2017 bill reprint of the law then in force [US-NMS5-014, A.3, medium-high]. Later amendments are not excluded.
- **Separation notice:** no NM UI separation-notice duty was located (open).
- **WARN:** no state law was checked (DWS menu lists only "Rapid Response & WARN Act", which is federal).

## 8 — benefits_in_kind
- NM withholding follows the federal treatment:
  - Fringe benefits are withheld by the same method as federal.
  - NM taxable wages are federal W-2 wages, less employer medical care savings account exemptions [FYI-104, US-NM-P5-2-001].
- No state departure (401(k), 125, HSA, transit) was found in FYI-104. The PIT conformity statute (7-2-2 "base income") was not read. Confidence: medium.

## 9 — deductions_garnishments
- **Deductions:**
  - Only lawful deductions, or those authorized by employer and employee (50-4-2(B)) [US-NMP8-001].
  - An advance or overpayment needs a signed written authorization, and the employee must still receive minimum wage x hours (11.1.4.7(R)) [US-NMS5-003].
  - Agricultural board and lodging may be deducted [US-NMS5-004].
- **Creditor garnishment** (35-12-7 as amended by SB 216, effective 2023-07-01) [US-NMS5-015, A.1]:
  - Exempt amount = the GREATER of 75% of disposable earnings, or 40 x the highest applicable federal, state or local minimum wage per week at the place of work.
  - Examples: 480/week at the state rate; 616/week in Santa Fe from 2026-03-01; 520/week in Albuquerque in 2027.
  - This is more protective than the CCPA (30x federal).
- **Child support:** 50% of disposable earnings is exempt, and the combined maximum is 50% [US-NMS5-015].
  - Payments go to the NM CSSD State Disbursement Unit (P.O. Box 200796, Dallas TX) [US-NMS5-010].
  - The IWO employer fee was not located (HCA returns 403).
- **State tax levy:** not researched (open).

## 10 — collective_agreements (prevailing wage)
- **Scope and rates:** Public Works Minimum Wage Act, on public works contracts over 60,000 USD [US-NMR3-003; US-NMP6-002]. DWS rate decisions apply.
- **Certified payroll** [US-NMS5-009, A.1]:
  - Weekly payrolls, submitted every two weeks within 5 working days.
  - Fields: classification, rates, fringe, daily/weekly and overtime hours, deductions, net pay, decision number.
  - Payrolls numbered in sequence, with a statement of compliance and an affidavit before final payment.
  - Kept 4 years.

## 11 — indexation
| Item | Indexed? | Publication |
|---|---|---|
| State minimum wage | No (fixed 12.00 since 2023) | DWS Minimum Wage page [US-NMS5-005] |
| Albuquerque minimum wage | Yes, annual (2027 = 13.00) | cabq.gov [US-NMS5-006] |
| Santa Fe living wage | Yes. Western CPI-W until 2027, then 17.50 set by statute, then 50% CPI + 50% FMR (cap 5%) from 2028 | santafenm.gov [US-NMS5-007]. G-DERIVE: 15.00 x 1.0268 = 15.402 -> 15.40 (reproduces) |
| SUI wage base | Yes, 60% of state average annual earnings, rounded up to 100 | DWS UI Tax page [US-NM-P5-1-001; US-NMS5-016] |
| SUI reserve factor | Annual (2026 3.6361) | DWS [US-NMS5-008] |
| PIT withholding tables | Annual reissue of FYI-104 (standard deduction follows federal). Brackets are not indexed | FYI-104 [US-NM-P5-2-001] |
| WC admin fee | Scheduled steps 2025/2028/2033 | TRD [US-NMR3-001] |
| Garnishment floor | Follows the highest applicable minimum wage | 35-12-7 [US-NMS5-015] |

## 12 — data_protection
- Sick-leave records: 48 months, produced to DWS on request [US-NMS5-002].
- TRD taxpayer confidentiality: 7-1-8 to 7-1-8.11 [US-NMS5-011].
- **SSN truncation on pay statements:** no NM rule located. The Privacy Protection Act (57-12B) was not read because nmlegis.gov returns 403 (open).

## 13 — live_legal_change
- **In force from 2026-01-01:**
  - TRD-41431 quarterly wage and withholding report (HB 218, 2025);
  - e-file and e-pay mandate for TRD-41414, 41431 and 41409;
  - electronic W-2 for all employers, due 31 January [FYI-104; FYI-330; US-NMS5-012].
- **WC fee:** steps to 2.55/2.25 on 2025-07-01, and is scheduled to rise to 2.68/2.38 on 2028-07-01 [US-NMR3-001].
- **Local rates:** Albuquerque 13.00 from 2027-01-01 [US-NMS5-006]; Santa Fe 17.50 from 2027-01-01 [US-NMS5-007].
- **2027 FYI-104:** not yet visible. The TRD rates page lists files by JavaScript, so the list could not be read with curl.
- **2026 session:** the web search surfaced HB 98 (2026, state-employee paid parental leave from 2027-07-01). It is a lead only: the text and enactment were not read. It concerns public employers only.
- **PFML:** none enacted [US-NMR3-002].

## Special populations
| Population | NM rule | register_id |
|---|---|---|
| Domestic/household workers | Excluded from the Minimum Wage Act (50-4-21(C)(1)). UI covered at 1,000 USD in a quarter. PIT withholding follows federal (none required where federal withholding is not required) | US-NMS5-004; US-NMS5-016; US-NM-P5-2-001 |
| Agricultural | MWA excludes listed farm workers (500 person-day test, family, hand-harvest piece-rate, range livestock/milk). Board and lodging deductible. UI at 20,000 USD in a quarter or 10 workers. PIT withholding where federal applies ("some agricultural workers") | US-NMS5-004; US-NMS5-016; US-NMS5-013 |
| Minors | Work permit under 16. Secondary-school student minimum 8.50. Under-18 non-students excluded from the MWA | US-NMS5-003; US-NMS5-004 |
| Tipped | State cash wage 3.00 (more than 30 USD/month in tips). Albuquerque 7.20. Santa Fe base 3.00 (100 USD/month or more) | US-NMS5-004; US-NMS5-006; US-NMS5-007 |
| Clergy/religious | Nonprofit/religious volunteers and non-employment relationships are outside the MWA (50-4-21(C)(4)). 501(c)(3) UI reimbursement option. PIT follows federal (no state rule beyond federal in FYI-104) | US-NMS5-004; US-NMS5-016 |
| Students | Secondary-school minimum 8.50. UI student exclusions under 51-1-42(F), not read | US-NMS5-004 |
| Nonresident aliens | No state rule beyond federal (FYI-104 follows the federal W-4 and method) | US-NM-P5-2-001 |
| Native Americans (NM-specific) | Income wholly earned on own-tribe lands while living there is exempt; no withholding | US-NMS5-013; US-NM-P5-2-001 |
| Military / military spouses | Active-duty pay is exempt; spouses keeping out-of-state residence are exempt | US-NM-P5-2-001 |
| Statutory employees | No state rule beyond federal (FYI-104 ties withholding to federal withholding) | US-NM-P5-2-001 |
| Government employees | Covered by the state minimum-wage rate only (50-4-21(B)). Excluded from the Healthy Workplaces Act (the state and political subdivisions are not "employers") | US-NMS5-004; US-NMS5-001 |
| Commission/piecework salespersons | Excluded from the MWA. Final pay within 10 days on discharge | US-NMS5-004; US-NMS5-014 |

## MULTI hand-offs (NM answers)
- **SUI wage-base credit for wages reported to another state:** NOT located. The 2019 handbook is silent, and 51-1-11 was not read. Open.
- **PFML/SDI for multistate workers:** not applicable, because NM has no programme.
- **Paid sick leave for partly in-state workers:** the Act and 11.1.6 NMAC set no hours-in-state threshold. The scope is "employers and employees within the state of New Mexico" (11.1.6.2) [US-NMS5-002]. Read: every hour worked in NM accrues. Confidence medium.
- **Pay-statement reach:** 50-4-2(A) applies to "all employees paid in this state" [US-NMP8-001]. No other reach rule exists. Default: NM work location.

## ACCESS gaps (exact URLs)
- https://lascruces.gov/minimum-wage-notice-for-2026/ (403 direct; Wayback 403): Las Cruces 2026 rate.
- https://www.bernco.gov/planning/required-workplace-postings.aspx (403): Bernalillo County rate.
- https://www.santafecountynm.gov/living-wage (404; the correct URL is unknown): Santa Fe County living wage.
- https://www.dws.nm.gov/Businesses/Rules-and-Regulations/Labor-Relations-FAQs (Wayback 403).
- https://www.dws.nm.gov/Portals/0/DM/LaborRelations/New_Mexico_Minimum_Wage_Act.pdf (Wayback 404).
- https://www.nmlegis.gov/ and https://nmonesource.com/ (403; current compiled NMSA unreadable): 50-4-4/-5 current text, 51-1-11, 51-1-42, 57-12B, 50-6, 7-2-2.
- https://www.hca.nm.gov/ (403): child-support IWO employer fee.
- realfile.tax.newmexico.gov TRD-41431 instructions (`trd-41431ins.pdf` 404); the TAP bulk-filing schema (inside TAP).
- DWS wage file format specifications (Delimited/ICESA/XML/EFW2), linked from the UI pages on www.dws.nm.gov (403).

## Open questions

Mirrors `unresolved[]` of the facts file (same keys, same wording).

- **nm.meta.register_id_pattern** (blocking): 15 facts rest on active register rows whose ids (US-NM-P5-1-001, US-NM-P5-1-002, US-NM-P5-2-001, US-NM-P5-2-002, US-NM-P5-2-003, US-NM-P5-2-005) do not match the facts-schema register_id pattern ^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$ (multi-hyphen legacy ids). They are carried in full in _facts_pending_register_id_pattern and are NOT yet consumable facts. What would close it: Orchestrator decision: a PATCH of facts.schema.json loosening the register_id pattern (e.g. ^[A-Z]{2}-[A-Z0-9-]{2,16}-[0-9]{3,4}$), or register alias ids; then run _research/synthesis-B/_work-MN-WY/promote.py to move the pending facts into facts[].
- **nm.labour.minwage.local.other** (blocking): Las Cruces, Bernalillo County and Santa Fe County 2026/2027 rates not read (403/404). What would close it: Each local government's 2026 notice (browser pass).
- **nm.labour.minwage.state.next_year** (non-blocking): No 2026-session amendment confirmed for 2027. What would close it: 2026 session final-bill list on nmlegis.gov or a DWS notice.
- **nm.report.w2.due_conflict** (non-blocking): FYI-330 (31 Jan) vs TRD page (last day of Feb). What would close it: TRD confirmation or NMSA 7-3-10 text.
- **nm.report.tap_schemas** (non-blocking): TRD-41431/TAP bulk schema and TAP W-2 TXT layout not obtained. What would close it: TAP Help bulk download (login) and TRD-41431 instructions.
- **nm.report.trd41414.thresholds** (non-blocking): Filing-frequency thresholds not stated. What would close it: 3.3.6 NMAC or TRD registration guide.
- **nm.ui.other_state_credit_exclusions** (non-blocking): SUI other-state wage credit and 51-1-42(F) exclusions not read. What would close it: NMSA 51-1-11 and 51-1-42 or 11.3.300 NMAC.
- **nm.data.ssn_electronic_paycard** (non-blocking): SSN truncation (57-12B), electronic pay-statement consent and paycard rule not read (nmlegis 403). What would close it: NMSA compilation (browser).
- **nm.garn.iwo.employer_fee** (non-blocking): Child-support IWO employer fee not located (HCA 403). What would close it: hca.nm.gov Child Support Services employer page.
- **nm.term.final_pay.current_text** (non-blocking): 50-4-4/-5 current text after 2017 not read (A.3 reprint). What would close it: NMSA compilation.
- **nm.pit.tables.next_year** (non-blocking): 2027 FYI-104 not yet visible. What would close it: TRD withholding-rates page in browser (Nov-Dec 2026).

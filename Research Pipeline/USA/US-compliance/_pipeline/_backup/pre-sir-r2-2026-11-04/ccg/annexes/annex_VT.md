# Annex VT: Vermont


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T3 - state withholding; local layer absent or piggybacked on the state return** (build manifest, tier rationale).

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## VT.1 Employment and labour code

- **Minimum wage (21 V.S.A. 384(a)(1)) [US-VTS5-001, US-VTS5-003]:** [[FACT:vt.minwage.hourly=14.42]] USD per hour from 2026-01-01; the federal rate applies if higher. The 2027 rate is not located (blocking open point below).
- **Tipped (service) employees (384(a)(2)):** hotel, motel, tourist-place and restaurant staff above a monthly tip test receive a basic wage of at least half the minimum: [[FACT:vt.minwage.tipped.cash_wage=7.21]] USD per hour from 2026-01-01; the employer makes up any shortfall over the workweek [US-VTS5-003].
- **Local minimum wages:** none located; municipalities have only local option taxes on sales, meals, alcohol and rooms [US-VTP51-005].
- **Overtime (384(b)) [US-VTS5-001]:** [[FACT:vt.overtime.premium.multiplier=1.5]] times the regular rate above [[FACT:vt.overtime.weekly_threshold_hours=40]] hours per workweek; no daily overtime. Broad exemptions beyond the FLSA (retail or service establishments, seasonal amusement, hotel, motel and restaurant, certain transport, political subdivisions, FLSA-covered State employees); hospitals and care homes may elect an 8/80 system. Allowed deductions from the minimum: board, lodging, apparel, rent, utilities (384(c)).
- **Coverage:** the minimum-wage employer definition requires two or more employees (383(3)) [US-VTS5-013]; wage payment uses an ABC test (341) [US-VTS5-019].
- **Pay frequency (342(a)) [US-VTS5-002]:** [[FACT:vt.pay_frequency.rule=weekly by default (wages to max 6 days before payday); biweekly/semimonthly after notice]]; a CBA may set a longer lag.
- **Method of payment (342(c), 343) [US-VTS5-002, US-VTS5-022]:** lawful money or check; direct deposit requires written authorisation ([[FACT:vt.labour.direct_deposit.consent_required=True]]). Payroll cards need written voluntary consent, plain-language disclosures, free withdrawals per period, advance notice of changes and no credit link; card disclosures carry a language rule (342(f)) [US-VTL-001].

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `vt.minwage.hourly` | [[FACT:vt.minwage.hourly=14.42]] | USD | 2026-01-01 to 2026-12-31 | US-VTS5-003 |  |
| `vt.minwage.indexation` | [[FACT:vt.minwage.indexation=smaller of 5% or CPI-U, each 1 January, nearest 0.01; never decreased]] |  | from 2025-07-01 | US-VTS5-001 | 21 V.S.A. 384(a)(1) |
| `vt.minwage.tipped.cash_wage` | [[FACT:vt.minwage.tipped.cash_wage=7.21]] | USD | 2026-01-01 to 2026-12-31 | US-VTS5-003 | 50% of minimum; hotel/motel/tourist/restaurant; >120/month tips |
| `vt.overtime.weekly_threshold_hours` | [[FACT:vt.overtime.weekly_threshold_hours=40]] | hours | from 2025-07-01 | US-VTS5-001 | broad exemptions (retail/service, hotel/restaurant, amusement...) |
| `vt.overtime.premium.multiplier` | [[FACT:vt.overtime.premium.multiplier=1.5]] | ratio | from 2025-07-01 | US-VTS5-001 |  |
| `vt.pay_frequency.rule` | [[FACT:vt.pay_frequency.rule=weekly by default (wages to max 6 days before payday); biweekly/semimonthly after notice]] |  | from 2024-07-01 | US-VTS5-002 | 342(a) |
| `vt.labour.direct_deposit.consent_required` | [[FACT:vt.labour.direct_deposit.consent_required=True]] |  | from 2024-07-01 | US-VTS5-002 | written authorisation; payroll card 3 free withdrawals per period (US-VTS5-022) |

**Open research points**

- Not yet published (expected October 2026; not yet found when last checked on 2026-11-02) [[GAP:RQ-358]]: 2027 VT minimum wage not located.

## VT.2 Income tax withholding

- **Method (GB-1210-2026, effective 2026-01-01 to 2026-12-31) [US-VTS5-016, US-VTP51-001]:** [[FACT:vt.wh.method=GB-1210-2026 percentage tables after W-4VT allowances]]. Wages subject to Vermont withholding = wages subject to federal withholding, paid to a resident or to a nonresident for services in Vermont.
  - Allowance [[FACT:vt.pit.allowance.annual=5400]] USD per year (per-period values in the guide).
  - Annual percentage-table thresholds (USD), single: [[FACT:vt.pit.wh.single.thresholds=3925;54675;126775;260225]]; married: [[FACT:vt.pit.wh.married.thresholds=11775;96475;216525;323825]] (zero below the first threshold; band rates from each threshold).
  - Band rates (%): [[FACT:vt.pit.wh.rates=3.35;6.60;7.60;8.75]]; top rate [[FACT:vt.pit.wh.rate.top=8.75]] %. The cumulative base amounts are printed in the guide and not carried as separate facts. Civil-union partners use the married table.
- **Rounding:** no rule stated; the guide's constants use half-up to the cent.
- **Oracle:** GB-1210-2026 p.6 worked example (weekly, married, two allowances): [[FACT:vt.pit.oracle.example_1.withholding=45.77]] USD, reproduced. Recomputation in Module 12.
- **Certificate:** [[FACT:vt.wh.certificate=W-4VT (Rev. 12/18); federal W-4 fallback]] [US-VTS5-029]. Extra federal withholding on the W-4 adds a proportion to Vermont withholding (guide).
- **Supplemental and non-periodic payments:** Vermont withholding may be estimated at [[FACT:vt.pit.supplemental.ratio_of_federal=30]] % of the federal withholding; no flat supplemental percentage of wages [US-VTS5-016].
- **Statutory rates (5822) [US-VTS5-018]:** brackets indexed yearly by CPI-U. The minimum tax of [[FACT:vt.pit.statutory.min_tax.rate=3]] % on high federal AGI (5822(a)(6)) is **assessment-level only**, never in the withholding tables.
- **Residents and nonresidents [US-VTS5-016, US-VTP51-003, US-VTP52-003]:** a nonresident working in and outside Vermont is taxed on full pay times Vermont hours over total hours; a resident on full pay, less tax withheld for the work state. Out-of-state employers start Vermont withholding after an employee has worked from a Vermont location for [[FACT:vt.pit.nonresident.out_of_state_employer_days=30]] days. Resident credit (5825) at assessment [US-VTP52-001]. Reciprocity: [[FACT:vt.reciprocity.states=none]].
- **Local income taxes:** none (exists: [[FACT:vt.local_wage_tax.exists=False]]) [US-VTP51-005].
- **Resident and nonresident matrix.**

| Income type | Vermont resident | Nonresident |
|---|---|---|
| Regular salary | GB-1210 tables on full pay, less the work state's withholding | GB-1210 tables on the Vermont hours share |
| Bonus / non-periodic | Proportion of federal withholding per the guide | Same, Vermont share |
| Severance, equity, benefits in kind | Follow federal withholding wages | Vermont share |
| High-income minimum tax | Assessment only | Assessment only |

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `vt.wh.method` | [[FACT:vt.wh.method=GB-1210-2026 percentage tables after W-4VT allowances]] |  | 2026-01-01 to 2026-12-31 | US-VTS5-016 | expires 2026-12-31 |
| `vt.pit.allowance.annual` | [[FACT:vt.pit.allowance.annual=5400]] | USD | 2026-01-01 to 2026-12-31 | US-VTS5-016 |  |
| `vt.pit.wh.single.thresholds` | [[FACT:vt.pit.wh.single.thresholds=3925;54675;126775;260225]] |  | 2026-01-01 to 2026-12-31 | US-VTS5-016 | annual; top rate [[FACT:vt.pit.wh.rate.top=8.75]]% Not configured in this release [[GAP:RQ-574]]: The lower bracket rates and base amounts of the 2026 withholding schedule are not yet established as separate values. |
| `vt.pit.wh.married.thresholds` | [[FACT:vt.pit.wh.married.thresholds=11775;96475;216525;323825]] |  | 2026-01-01 to 2026-12-31 | US-VTS5-016 | top rate [[FACT:vt.pit.wh.rate.top=8.75]]%; lower brackets: see the research gap on the single schedule |
| `vt.pit.wh.rates` | [[FACT:vt.pit.wh.rates=3.35;6.60;7.60;8.75]] |  | 2026-01-01 to 2026-12-31 | US-VTS5-016 | percent |
| `vt.pit.wh.rate.top` | [[FACT:vt.pit.wh.rate.top=8.75]] | % | 2026-01-01 to 2026-12-31 | US-VTS5-016 |  |
| `vt.pit.oracle.example_1.withholding` | [[FACT:vt.pit.oracle.example_1.withholding=45.77]] | USD | 2026-01-01 to 2026-12-31 | US-VTS5-016 |  |
| `vt.wh.certificate` | [[FACT:vt.wh.certificate=W-4VT (Rev. 12/18); federal W-4 fallback]] |  | from 2026-01-01 | US-VTS5-029 | extra federal withholding: add 30% to VT |
| `vt.pit.supplemental.ratio_of_federal` | [[FACT:vt.pit.supplemental.ratio_of_federal=30]] | % | 2026-01-01 to 2026-12-31 | US-VTS5-016 | VT may be estimated at 30% of federal withholding on non-periodic payments; NQDC 6% |
| `vt.pit.statutory.min_tax.rate` | [[FACT:vt.pit.statutory.min_tax.rate=3]] | % | from 2026-01-01 | US-VTS5-018 | on federal AGI over 150,000 - ASSESSMENT only, not in tables |
| `vt.reciprocity.states` | [[FACT:vt.reciprocity.states=none]] |  | 2026-01-01 to 2026-12-31 | US-VTS5-016 | absence on 3 authority pages + GB-1210 |
| `vt.pit.nonresident.out_of_state_employer_days` | [[FACT:vt.pit.nonresident.out_of_state_employer_days=30]] | days | from 2026-01-01 | US-VTP51-003 | out-of-state employers start VT withholding after 30 days working from VT |
| `vt.local_wage_tax.exists` | [[FACT:vt.local_wage_tax.exists=False]] |  | from 2026-01-01 | US-VTP51-005 |  |

## VT.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in VT.2.

## VT.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in VT.2.

## VT.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Unemployment insurance (VDOL) [US-VTS5-004, US-VTS5-005, US-VTS5-006, US-VTS5-009].** Taxable wage base [[FACT:vt.sui.wage_base=15,400]] USD for 2026, indexed to the state annual average wage when the fund conditions are met. Rates by class and schedule; schedule I starts at [[FACT:vt.ui.rate.schedule_i.min=0.4]] % and schedule V reaches [[FACT:vt.ui.rate.schedule_v.max=8.4]] %; the rate year starts July 1 (the schedule for the year from 2026-07-01 is open, below). New employer [[FACT:vt.sui.new_employer.rate=1]] % (foreign construction employers take the industry average). Wages already paid for covered employment in another state count toward the base: [[FACT:vt.sui.wage_base.other_state_credit=True]] (1321(b)(2)) [US-VTS5-010]. The no-employee-contribution statement lacks an active register row (open point below).
- **SDI, TDI, PFML:** none mandatory (exists: [[FACT:vt.sdi_pfml.exists=False]]); VT-FMLI is voluntary [US-VTP51-006].
- **Child Care Contribution [US-VTS5-030, US-VTP51-004, US-VTP7-001]:** [[FACT:vt.ccc.total.rate=0.44]] % of all IRC 3401 wages subject to Vermont withholding, no cap; the employer may withhold up to [[FACT:vt.ccc.employee.max_rate=0.11]] % from the employee (less, none, or non-uniform allowed); the employee share goes in W-2 box 14; reported on WHT-436 and paid on the withholding schedule.

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `vt.sui.wage_base` | [[FACT:vt.sui.wage_base=15,400]] | USD | 2026-01-01 to 2026-12-31 | US-VTS5-004 |  |
| `vt.sui.new_employer.rate` | [[FACT:vt.sui.new_employer.rate=1]] | % | from 2004-07-01 | US-VTS5-009 | foreign construction NAICS 236-238 industry average |
| `vt.ui.rate.schedule_i.min` | [[FACT:vt.ui.rate.schedule_i.min=0.4]] | % | from 2024-07-01 | US-VTS5-006 | schedule I 0.4-5.4; schedule V 1.3-8.4; rate year from 1 July |
| `vt.ui.rate.schedule_v.max` | [[FACT:vt.ui.rate.schedule_v.max=8.4]] | % | from 2024-07-01 | US-VTS5-006 |  |
| `vt.sui.wage_base.other_state_credit` | [[FACT:vt.sui.wage_base.other_state_credit=True]] |  | from 2012-01-01 | US-VTS5-010 | 1321(b)(2) |
| `vt.ccc.total.rate` | [[FACT:vt.ccc.total.rate=0.44]] | % | from 2024-07-01 | US-VTS5-030 | Child Care Contribution on all IRC 3401 wages, no cap; on WHT-436 |
| `vt.ccc.employee.max_rate` | [[FACT:vt.ccc.employee.max_rate=0.11]] | % | from 2024-07-01 | US-VTS5-030 | employee share in W-2 Box 14; need not be uniform |
| `vt.sdi_pfml.exists` | [[FACT:vt.sdi_pfml.exists=False]] |  | from 2024-07-01 | US-VTP51-006 | VT-FMLI voluntary only |

**Open research points**

- Not configured in this release [[GAP:RQ-359]]: 2027 UI wage base not located.
- Not configured in this release [[GAP:RQ-360]]: The 2026 base of [[FACT:vt.sui.wage_base=15,400]] USD cannot be re-derived from the prior-year base because the state annual average wage (1338(g)) was not read.
- Not configured in this release [[GAP:RQ-361]]: Schedule I-V for the rate year from 2026-07-01 not confirmed.
- Not configured in this release [[GAP:RQ-369]]: Not established from an official source.

## VT.4 Pay statement

- **Content [US-VTP9-001, US-VTP52-004]:** a detailed written statement with each weekly pay: [[FACT:vt.payslip.items=gross pay, hours worked, hourly rate, all deductions itemised]] (including meals); service employees' weekly tip reports kept for the rule's period. Electronic consent rule: open point below. Language: English (card disclosures excepted) [US-VTL-001, US-OWN-006].
- **Retention:** UI records [[FACT:vt.records.ui.retention_years=4]] years [US-VTS5-009].

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `vt.payslip.items` | [[FACT:vt.payslip.items=gross pay, hours worked, hourly rate, all deductions itemised]] |  | from 2009-01-01 | US-VTP9-001 | tip reports kept 3 years |
| `vt.records.ui.retention_years` | [[FACT:vt.records.ui.retention_years=4]] | years | from 2026-01-01 | US-VTS5-009 |  |

**Open research points**

- Not configured in this release [[GAP:RQ-363]]: Electronic pay statement consent rule not found.

## VT.5 Statutory reporting

- **Withholding (Department of Taxes, myVTax) [US-VTS5-017, US-VTP51-002, US-VTPIT-003]:** registration via myVTax or BR-400; deposit frequency (semiweekly, monthly or quarterly) set by the Department. WHT-436 quarterly reconciliation due [[FACT:vt.report.wht436.due=25th after quarter end]] (it also carries the Child Care Contribution) [US-VTS5-030]. The annual reconciliation form is due [[FACT:vt.report.wht434.due=January 31]] as the transmittal for W-2 and 1099; e-filing above the form threshold and always for payroll services. Vermont left the Combined Fed/State program: W-2s are filed directly with Vermont. W-2 file format: open point below.
- **UI quarterly wage and contribution report [US-VTS5-007, US-VTS5-009]:** every quarter even with no wages, via Employer e-Services, due [[FACT:vt.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]]; per worker name, SSN and gross wages, and for hourly workers also gender and hourly wage (1314a(a)(2)); separation information on request.
- **New hire [US-VTS5-014]:** to VDOL within [[FACT:vt.newhire.report_days=10]] calendar days of the first day worked for pay; rehires after a long separation count as new hires.
- **Powers of attorney:** PA-1 (tax), C-50 (UI) [US-VTP51-012, US-VTP51-013].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `vt.report.wht434.due` | [[FACT:vt.report.wht434.due=January 31]] |  | 2026-01-01 to 2026-12-31 | US-VTS5-017 | e-file at 10+ forms; VT left Combined Fed/State |
| `vt.report.ui.quarterly_due` | [[FACT:vt.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] |  | from 2026-01-01 | US-VTS5-007 | hourly workers also gender and hourly wage (1314a(a)(2)) |
| `vt.newhire.report_days` | [[FACT:vt.newhire.report_days=10]] | days | from 2025-09-01 | US-VTS5-014 | calendar days to VDOL |
| `vt.report.wht436.due` | [[FACT:vt.report.wht436.due=25th after quarter end]] |  | from 2026-01-01 | US-VTP51-002 | deposits semiweekly/monthly (25th)/quarterly by Department assignment |

**Open research points**

- Not configured in this release [[GAP:RQ-362]]: VT W-2 electronic file format not stated.

## VT.6 Leave

- **Earned sick time (21 V.S.A. 481-483) [US-VTS5-008, US-VTS5-011, US-VTS5-012]:** accrual one hour per [[FACT:vt.leave.est.accrual_ratio_hours_worked=52]] hours worked; the employer may cap accrual and use at [[FACT:vt.leave.est.annual_cap_hours=40]] hours per twelve months; waiting period allowed; paid at the greater of the normal rate or minimum wage; carry-over; payout at separation: [[FACT:vt.leave.est.payout_at_separation=False]] unless agreed. Covered employees exclude short-term, minor, per-diem and certain public workers (481(5)).
- **Parental and family leave (471-472) [US-VTS5-026, US-VTS5-027]:** unpaid, job-protected; Act 32 of 2025 added bereavement, safe leave and qualifying exigency; employer-size thresholds possibly outdated (open point below). Short-term family leave (472a) unpaid [US-VTS5-028].

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `vt.leave.est.accrual_ratio_hours_worked` | [[FACT:vt.leave.est.accrual_ratio_hours_worked=52]] | hours | from 2025-05-13 | US-VTS5-008 | cap 40 h per 12 months; employees averaging 18+ h/week |
| `vt.leave.est.annual_cap_hours` | [[FACT:vt.leave.est.annual_cap_hours=40]] | hours | from 2025-05-13 | US-VTS5-008 |  |
| `vt.leave.est.payout_at_separation` | [[FACT:vt.leave.est.payout_at_separation=False]] |  | from 2024-07-01 | US-VTS5-011 | unless employer agrees |

**Open research points**

- Not configured in this release [[GAP:RQ-364]]: Not established from an official source.
- Not configured in this release [[GAP:RQ-365]]: ESTA reach for partly-in-VT workers not stated.

## VT.7 Termination and final pay

- **Final pay (342(b)) [US-VTS5-002]:** voluntary quit: the last regular payday (or the following Friday); discharge: within [[FACT:vt.term.final_pay.discharge.hours=72]] hours. Penalties and officer liability (345) [US-VTS5-024].
- **Accrued vacation:** [[FACT:vt.term.vacation.payout=only if written policy/agreement provides]] (VDOL WH-13) [US-VTS5-025]. Earned sick time: no payout. State WARN (411 ff.): not read (open point below).

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `vt.term.final_pay.discharge.hours` | [[FACT:vt.term.final_pay.discharge.hours=72]] | hours | from 2024-07-01 | US-VTS5-002 | quit: last regular payday or following Friday |
| `vt.term.vacation.payout` | [[FACT:vt.term.vacation.payout=only if written policy/agreement provides]] |  | from 2026-01-01 | US-VTS5-025 | VDOL WH-13 |

**Open research points**

- Not configured in this release [[GAP:RQ-366]]: 21 V.S.A. 411-419 not read.

## VT.8 Benefits in kind and taxable wages

- **Conformity:** Vermont taxable income starts from federal AGI; withholding wages = federal withholding wages; no wage-level departure from the federal exclusions found; civil-union partners treated as spouses for cafeteria-plan purposes [US-VTS5-020, US-VTS5-016].
- **Vermont Saves (state auto-IRA) [US-VTB5-003]:** [[FACT:vt.bik.vt_saves.rule=Vermont Saves state auto-IRA (Roth IRA default, administrator Vestwell): covered employers register and facilitate payroll deductions; eligible employees auto-enrolled and may opt out at any time; employers with a 401(k)/403(b)/SEP/SIMPLE certify exemption]]. Employers with [[FACT:vt.bik.vt_saves.employer_threshold_w2_employees=2]] or more W-2 employees and no qualified plan must register and facilitate payroll deductions. Maximum penalty per covered employee: [[FACT:vt.bik.vt_saves.penalty.max_per_employee=20]] USD through 2026-09-30 and [[FACT:vt.bik.vt_saves.penalty.max_per_employee=75]] USD per year from 2026-10-01 (3 V.S.A. 535). Default contribution rate: open point below.

**Parameters (benefits in kind and the taxable base)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `vt.bik.vt_saves.employer_threshold_w2_employees` | [[FACT:vt.bik.vt_saves.employer_threshold_w2_employees=2]] |  | from 2026-01-01 | US-VTB5-003 | Start date of the threshold not stated on the page. |
| `vt.bik.vt_saves.rule` | [[FACT:vt.bik.vt_saves.rule=Vermont Saves state auto-IRA (Roth IRA default, administrator Vestwell): covered employers register and facilitate payroll deductions; eligible employees auto-enrolled and may opt out at any time; employers with a 401(k)/403(b)/SEP/SIMPLE certify exemption]] |  | from 2026-01-01 | US-VTB5-003 |  |
| `vt.bik.vt_saves.penalty.max_per_employee` | [[FACT:vt.bik.vt_saves.penalty.max_per_employee=20]] | USD | 2026-01-01 to 2026-09-30 | US-VTB5-003 | Maximum penalty per covered employee through 2026-09-30 (3 V.S.A. 535). |
| `vt.bik.vt_saves.penalty.max_per_employee` | [[FACT:vt.bik.vt_saves.penalty.max_per_employee=75]] | USD | from 2026-10-01 | US-VTB5-003 | Per covered employee per calendar year from 2026-10-01 (3 V.S.A. 535). |

**Open research points**

- Not configured in this release [[GAP:RQ-370]]: The Treasurer's Vermont Saves page (US-VTB5-003) does not state the default payroll contribution rate or escalation; Program Rules (Feb 2026) not read.

## VT.9 Deductions and garnishments

- **Wage deductions (VDOL WH-13) [US-VTS5-025]:** goods or services only if pay stays at or above the minimum wage, with written authorisation; taxes and child support as authorised by law; health and retirement contributions with written authorisation; meals and lodging actually furnished.
- **Creditor garnishment (12 V.S.A. 3170) [US-VTS5-021]:** at most [[FACT:vt.garn.creditor.max_percent=25]] % of weekly disposable earnings (CCPA floor); for consumer-credit debts at most [[FACT:vt.garn.consumer_credit.max_rate=15]] % (with a higher protected floor), stricter than the CCPA. No discharge for trustee process.
- **Child-support IWO (15 V.S.A. 787) [US-VTS5-023]:** forward to the registry within the statutory working days; the employer may retain [[FACT:vt.garn.iwo.employer_fee.monthly=5.00]] USD per month as a fee; notify termination. Medical support enrolment and premium withholding (33 V.S.A. 4110(a)) [US-VTS5-014].

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `vt.garn.creditor.max_percent` | [[FACT:vt.garn.creditor.max_percent=25]] | % | from 2010-07-01 | US-VTS5-021 | exempt greater of 75% or 30x FMW; consumer-credit debts: 85% / 40x exempt (max 15%) |
| `vt.garn.consumer_credit.max_rate` | [[FACT:vt.garn.consumer_credit.max_rate=15]] | % | from 2010-07-01 | US-VTS5-021 |  |
| `vt.garn.iwo.employer_fee.monthly` | [[FACT:vt.garn.iwo.employer_fee.monthly=5.00]] | USD | from 2004-09-01 | US-VTS5-023 | forward within 7 working days |

**Open research points**

- Not configured in this release [[GAP:RQ-367]]: Department of Taxes wage levy not read.

## VT.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

- **Prevailing wage (29 V.S.A. 161(b)) [US-VTP51-011]:** State construction projects above [[FACT:vt.prevailing_wage.threshold=100,000]] USD (a higher threshold for projects funded mainly by capital construction acts); at least the mean prevailing wage from the VDOL survey plus a statutory fringe percentage; Transportation and Forests/Parks projects excluded; no certified-payroll filing duty.

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `vt.prevailing_wage.threshold` | [[FACT:vt.prevailing_wage.threshold=100,000]] | USD | from 2026-01-01 | US-VTP51-011 | mean prevailing wage + 42.5% fringe; 200,000 when >=50% capital funded |

## VT.11 Indexation

- **Minimum wage:** [[FACT:vt.minwage.indexation=smaller of 5% or CPI-U, each 1 January, nearest 0.01; never decreased]] [US-VTS5-001]; tipped wage half of it.
- **UI wage base:** state annual average wage, conditional (derivation open, below) [US-VTS5-005]. **UI rate schedule:** fund ratio, rate year from July 1 [US-VTS5-006].
- **PIT brackets and allowance:** CPI-U yearly; new guide each year (GB-1210-2027 expected December 2026) [US-VTS5-018, US-VTS5-016].

## VT.12 Payroll data protection and records

- **SSN Protection Act (9 V.S.A. ch. 62) [US-VTS5-015]:** no SSN on materials mailed to the individual unless required ([[FACT:vt.data.ssn.mailed_prohibited=True]]); never visible through an envelope; secure transmission only; a redacted SSN is outside the prohibition. A mailed payslip may carry a truncated SSN, never the full number.

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `vt.data.ssn.mailed_prohibited` | [[FACT:vt.data.ssn.mailed_prohibited=True]] |  | from 2007-01-01 | US-VTS5-015 | redacted SSN allowed |

## VT.13 Live legal change

- **2026-04-30:** 21 V.S.A. 384 amended (2025 No. 91 Adj. Sess.); **2026-06-18:** 21 V.S.A. 383 amended (2025 No. 177 Adj. Sess.) [US-VTS5-001, US-VTS5-013].
- **2026-10-01:** Vermont Saves penalty cap rises (Section 8) [US-VTB5-003].
- **Not located:** 2027 minimum wage, 2027 UI wage base, GB-1210-2027; the news pages were not swept (open points).

**Open research points**

- Not configured in this release [[GAP:RQ-368]]: GB-1210-2027 expected Dec 2026.

## VT.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## VT.15 Special populations

| Population | Vermont rule | Register id |
|---|---|---|
| Domestic / household | Excluded from minimum wage and overtime (383(2)(B)); UI above a quarterly cash test; withholding follows federal | US-VTS5-013, US-VTS5-009, US-VTS5-016 |
| Agricultural | Excluded from minimum wage and overtime (383(2)(A)); UI coverage tests | US-VTS5-013, US-VTS5-009 |
| Minors | Not covered by earned sick time; child-labour rules not read | US-VTS5-011 |
| Tipped | Basic wage per Section 1; employer top-up; tip reports kept | US-VTS5-001, US-VTS5-003, US-VTP9-001 |
| Clergy / religious | Withholding follows federal; some religious-organisation services exempt from UI | US-VTS5-016, US-VTS5-009 |
| Students | Excluded from minimum wage and overtime during the school year (383(2)(I)); UI exemptions for own-school, work-experience and some camp work | US-VTS5-013, US-VTS5-009 |
| Nonresident aliens | No state rule beyond federal; hours-ratio residency rules apply | US-VTS5-016 |
| Statutory employees | No state rule beyond federal | US-VTS5-016 |
| Government employees | Exclusions from minimum wage, overtime and earned sick time; UI reimbursement options for State and political subdivisions | US-VTS5-013, US-VTS5-001, US-VTS5-011, US-VTS5-005 |
| Owners / officers / LLC members | Earned sick time excludes WC-excluded owners and officers; UI excludes multi-member LLC members without an IRS election | US-VTS5-011, US-VTS5-009 |
| J-1 visa holders | Exempt from UI with documentation | US-VTS5-009 |
| Commission salespeople | Outside salespersons excluded from minimum wage; commission-only agents excluded from UI | US-VTS5-013, US-VTS5-009 |

## VT.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## VT.S Sources

Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file. Authorities:

- Build lead (Claude) under owner delegation (Wallisson Gomes): US-OWN-006
- Owner (Wallisson Gomes): US-OWN-008
- VT official authority: US-VTP7-001
- Vermont Department of Labor: US-VTP51-013, US-VTS5-003, US-VTS5-004, US-VTS5-009
- Vermont Department of Labor / Vermont Secretary of State (Code of Vermont Rules): US-VTP9-001
- Vermont Department of Labor Wage and Hour Program: US-VTP52-004, US-VTS5-025
- Vermont Department of Taxes: US-VTP51-003, US-VTP51-004, US-VTP51-005, US-VTP51-012, US-VTP52-003, US-VTPIT-003, US-VTS5-016, US-VTS5-017, US-VTS5-029, US-VTS5-030
- Vermont General Assembly (Vermont Statutes Online: US-VTS5-001
- (authority named in the register): US-VTS5-019
- (authority named in the register): US-VTS5-022, US-VTS5-027
- (authority named in the register): US-VTS5-023
- (authority named in the register): US-VTS5-007
- (authority named in the register): US-VTS5-006
- (authority named in the register): US-VTS5-014
- (authority named in the register): US-VTS5-012
- (authority named in the register): US-VTS5-005, US-VTS5-010, US-VTS5-021, US-VTS5-026
- (authority named in the register): US-VTS5-011
- (authority named in the register): US-VTS5-008
- (authority named in the register): US-VTS5-028
- (authority named in the register): US-VTS5-015
- (authority named in the register): US-VTS5-020
- (authority named in the register): US-VTS5-002
- (authority named in the register): US-VTS5-018
- (authority named in the register): US-VTS5-013
- Vermont General Assembly: US-VTS5-024
- (authority named in the register): US-VTP51-001
- (authority named in the register): US-VTP52-001
- (authority named in the register): US-VTP51-011
- (authority named in the register): US-VTP51-002
- (authority named in the register): US-VTL-001
- Vermont Office of the Governor: US-VTP51-006
- Vermont Office of the State Treasurer: US-VTB5-003

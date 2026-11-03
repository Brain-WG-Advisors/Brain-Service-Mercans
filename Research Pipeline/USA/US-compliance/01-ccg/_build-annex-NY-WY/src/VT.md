## @labour
- **Minimum wage (21 V.S.A. 384(a)(1)) [US-VTS5-001, US-VTS5-003]:** {{vt.minwage.hourly}} USD per hour from 2026-01-01; the federal rate applies if higher. The 2027 rate is not located (blocking open point below).
- **Tipped (service) employees (384(a)(2)):** hotel, motel, tourist-place and restaurant staff above a monthly tip test receive a basic wage of at least half the minimum: {{vt.minwage.tipped.cash_wage}} USD per hour from 2026-01-01; the employer makes up any shortfall over the workweek [US-VTS5-003].
- **Local minimum wages:** none located; municipalities have only local option taxes on sales, meals, alcohol and rooms [US-VTP51-005].
- **Overtime (384(b)) [US-VTS5-001]:** {{vt.overtime.premium.multiplier}} times the regular rate above {{vt.overtime.weekly_threshold_hours}} hours per workweek; no daily overtime. Broad exemptions beyond the FLSA (retail or service establishments, seasonal amusement, hotel, motel and restaurant, certain transport, political subdivisions, FLSA-covered State employees); hospitals and care homes may elect an 8/80 system. Allowed deductions from the minimum: board, lodging, apparel, rent, utilities (384(c)).
- **Coverage:** the minimum-wage employer definition requires two or more employees (383(3)) [US-VTS5-013]; wage payment uses an ABC test (341) [US-VTS5-019].
- **Pay frequency (342(a)) [US-VTS5-002]:** {{vt.pay_frequency.rule}}; a CBA may set a longer lag.
- **Method of payment (342(c), 343) [US-VTS5-002, US-VTS5-022]:** lawful money or check; direct deposit requires written authorisation ({{vt.labour.direct_deposit.consent_required}}). Payroll cards need written voluntary consent, plain-language disclosures, free withdrawals per period, advance notice of changes and no credit link; card disclosures carry a language rule (342(f)) [US-VTL-001].

## @income_tax
- **Method (GB-1210-2026, effective 2026-01-01 to 2026-12-31) [US-VTS5-016, US-VTP51-001]:** {{vt.wh.method}}. Wages subject to Vermont withholding = wages subject to federal withholding, paid to a resident or to a nonresident for services in Vermont.
  - Allowance {{vt.pit.allowance.annual}} USD per year (per-period values in the guide).
  - Annual percentage-table thresholds (USD), single: {{vt.pit.wh.single.thresholds}}; married: {{vt.pit.wh.married.thresholds}} (zero below the first threshold; band rates from each threshold).
  - Band rates (%): {{vt.pit.wh.rates}}; top rate {{vt.pit.wh.rate.top}} %. The cumulative base amounts are printed in the guide and not carried as separate facts. Civil-union partners use the married table.
- **Rounding:** no rule stated; the guide's constants use half-up to the cent.
- **Oracle:** GB-1210-2026 p.6 worked example (weekly, married, two allowances): {{vt.pit.oracle.example_1.withholding}} USD, reproduced. Recomputation in Module 12.
- **Certificate:** {{vt.wh.certificate}} [US-VTS5-029]. Extra federal withholding on the W-4 adds a proportion to Vermont withholding (guide).
- **Supplemental and non-periodic payments:** Vermont withholding may be estimated at {{vt.pit.supplemental.ratio_of_federal}} % of the federal withholding; no flat supplemental percentage of wages [US-VTS5-016].
- **Statutory rates (5822) [US-VTS5-018]:** brackets indexed yearly by CPI-U. The minimum tax of {{vt.pit.statutory.min_tax.rate}} % on high federal AGI (5822(a)(6)) is **assessment-level only**, never in the withholding tables.
- **Residents and nonresidents [US-VTS5-016, US-VTP51-003, US-VTP52-003]:** a nonresident working in and outside Vermont is taxed on full pay times Vermont hours over total hours; a resident on full pay, less tax withheld for the work state. Out-of-state employers start Vermont withholding after an employee has worked from a Vermont location for {{vt.pit.nonresident.out_of_state_employer_days}} days. Resident credit (5825) at assessment [US-VTP52-001]. Reciprocity: {{vt.reciprocity.states}}.
- **Local income taxes:** none (exists: {{vt.local_wage_tax.exists}}) [US-VTP51-005].
- **Resident and nonresident matrix.**

| Income type | Vermont resident | Nonresident |
|---|---|---|
| Regular salary | GB-1210 tables on full pay, less the work state's withholding | GB-1210 tables on the Vermont hours share |
| Bonus / non-periodic | Proportion of federal withholding per the guide | Same, Vermont share |
| Severance, equity, benefits in kind | Follow federal withholding wages | Vermont share |
| High-income minimum tax | Assessment only | Assessment only |

## @social
- **Unemployment insurance (VDOL) [US-VTS5-004, US-VTS5-005, US-VTS5-006, US-VTS5-009].** Taxable wage base {{vt.sui.wage_base@2026-01-01}} USD for 2026, indexed to the state annual average wage when the fund conditions are met. Rates by class and schedule; schedule I starts at {{vt.ui.rate.schedule_i.min}} % and schedule V reaches {{vt.ui.rate.schedule_v.max}} %; the rate year starts July 1 (the schedule for the year from 2026-07-01 is open, below). New employer {{vt.sui.new_employer.rate}} % (foreign construction employers take the industry average). Wages already paid for covered employment in another state count toward the base: {{vt.sui.wage_base.other_state_credit}} (1321(b)(2)) [US-VTS5-010]. The no-employee-contribution statement lacks an active register row (open point below).
- **SDI, TDI, PFML:** none mandatory (exists: {{vt.sdi_pfml.exists}}); VT-FMLI is voluntary [US-VTP51-006].
- **Child Care Contribution [US-VTS5-030, US-VTP51-004, US-VTP7-001]:** {{vt.ccc.total.rate}} % of all IRC 3401 wages subject to Vermont withholding, no cap; the employer may withhold up to {{vt.ccc.employee.max_rate}} % from the employee (less, none, or non-uniform allowed); the employee share goes in W-2 box 14; reported on WHT-436 and paid on the withholding schedule.

## @payslip
- **Content [US-VTP9-001, US-VTP52-004]:** a detailed written statement with each weekly pay: {{vt.payslip.items}} (including meals); service employees' weekly tip reports kept for the rule's period. Electronic consent rule: open point below. Language: English (card disclosures excepted) [US-VTL-001, US-OWN-006].
- **Retention:** UI records {{vt.records.ui.retention_years}} years [US-VTS5-009].

## @reporting
- **Withholding (Department of Taxes, myVTax) [US-VTS5-017, US-VTP51-002, US-VTPIT-003]:** registration via myVTax or BR-400; deposit frequency (semiweekly, monthly or quarterly) set by the Department. WHT-436 quarterly reconciliation due {{vt.report.wht436.due}} (it also carries the Child Care Contribution) [US-VTS5-030]. The annual reconciliation form is due {{vt.report.wht434.due}} as the transmittal for W-2 and 1099; e-filing above the form threshold and always for payroll services. Vermont left the Combined Fed/State program: W-2s are filed directly with Vermont. W-2 file format: open point below.
- **UI quarterly wage and contribution report [US-VTS5-007, US-VTS5-009]:** every quarter even with no wages, via Employer e-Services, due {{vt.report.ui.quarterly_due}}; per worker name, SSN and gross wages, and for hourly workers also gender and hourly wage (1314a(a)(2)); separation information on request.
- **New hire [US-VTS5-014]:** to VDOL within {{vt.newhire.report_days}} calendar days of the first day worked for pay; rehires after a long separation count as new hires.
- **Powers of attorney:** PA-1 (tax), C-50 (UI) [US-VTP51-012, US-VTP51-013].

## @leave
- **Earned sick time (21 V.S.A. 481-483) [US-VTS5-008, US-VTS5-011, US-VTS5-012]:** accrual one hour per {{vt.leave.est.accrual_ratio_hours_worked}} hours worked; the employer may cap accrual and use at {{vt.leave.est.annual_cap_hours}} hours per twelve months; waiting period allowed; paid at the greater of the normal rate or minimum wage; carry-over; payout at separation: {{vt.leave.est.payout_at_separation}} unless agreed. Covered employees exclude short-term, minor, per-diem and certain public workers (481(5)).
- **Parental and family leave (471-472) [US-VTS5-026, US-VTS5-027]:** unpaid, job-protected; Act 32 of 2025 added bereavement, safe leave and qualifying exigency; employer-size thresholds possibly outdated (open point below). Short-term family leave (472a) unpaid [US-VTS5-028].

## @termination
- **Final pay (342(b)) [US-VTS5-002]:** voluntary quit: the last regular payday (or the following Friday); discharge: within {{vt.term.final_pay.discharge.hours}} hours. Penalties and officer liability (345) [US-VTS5-024].
- **Accrued vacation:** {{vt.term.vacation.payout}} (VDOL WH-13) [US-VTS5-025]. Earned sick time: no payout. State WARN (411 ff.): not read (open point below).

## @bik
- **Conformity:** Vermont taxable income starts from federal AGI; withholding wages = federal withholding wages; no wage-level departure from the federal exclusions found; civil-union partners treated as spouses for cafeteria-plan purposes [US-VTS5-020, US-VTS5-016].
- **Vermont Saves (state auto-IRA) [US-VTB5-003]:** {{vt.bik.vt_saves.rule}}. Employers with {{vt.bik.vt_saves.employer_threshold_w2_employees}} or more W-2 employees and no qualified plan must register and facilitate payroll deductions. Maximum penalty per covered employee: {{vt.bik.vt_saves.penalty.max_per_employee@2026-01-01}} USD through 2026-09-30 and {{vt.bik.vt_saves.penalty.max_per_employee@2026-10-01}} USD per year from 2026-10-01 (3 V.S.A. 535). Default contribution rate: open point below.

## @deductions
- **Wage deductions (VDOL WH-13) [US-VTS5-025]:** goods or services only if pay stays at or above the minimum wage, with written authorisation; taxes and child support as authorised by law; health and retirement contributions with written authorisation; meals and lodging actually furnished.
- **Creditor garnishment (12 V.S.A. 3170) [US-VTS5-021]:** at most {{vt.garn.creditor.max_percent}} % of weekly disposable earnings (CCPA floor); for consumer-credit debts at most {{vt.garn.consumer_credit.max_rate}} % (with a higher protected floor), stricter than the CCPA. No discharge for trustee process.
- **Child-support IWO (15 V.S.A. 787) [US-VTS5-023]:** forward to the registry within the statutory working days; the employer may retain {{vt.garn.iwo.employer_fee.monthly}} USD per month as a fee; notify termination. Medical support enrolment and premium withholding (33 V.S.A. 4110(a)) [US-VTS5-014].

## @cba
- **Prevailing wage (29 V.S.A. 161(b)) [US-VTP51-011]:** State construction projects above {{vt.prevailing_wage.threshold}} USD (a higher threshold for projects funded mainly by capital construction acts); at least the mean prevailing wage from the VDOL survey plus a statutory fringe percentage; Transportation and Forests/Parks projects excluded; no certified-payroll filing duty.

## @indexation
- **Minimum wage:** {{vt.minwage.indexation}} [US-VTS5-001]; tipped wage half of it.
- **UI wage base:** state annual average wage, conditional (derivation open, below) [US-VTS5-005]. **UI rate schedule:** fund ratio, rate year from July 1 [US-VTS5-006].
- **PIT brackets and allowance:** CPI-U yearly; new guide each year (GB-1210-2027 expected December 2026) [US-VTS5-018, US-VTS5-016].

## @data
- **SSN Protection Act (9 V.S.A. ch. 62) [US-VTS5-015]:** no SSN on materials mailed to the individual unless required ({{vt.data.ssn.mailed_prohibited}}); never visible through an envelope; secure transmission only; a redacted SSN is outside the prohibition. A mailed payslip may carry a truncated SSN, never the full number.

## @live
- **2026-04-30:** 21 V.S.A. 384 amended (2025 No. 91 Adj. Sess.); **2026-06-18:** 21 V.S.A. 383 amended (2025 No. 177 Adj. Sess.) [US-VTS5-001, US-VTS5-013].
- **2026-10-01:** Vermont Saves penalty cap rises (Section 8) [US-VTB5-003].
- **Not located:** 2027 minimum wage, 2027 UI wage base, GB-1210-2027; the news pages were not swept (open points).

## @special
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

## @gaps
- vt.ui.wage_base.derivation :: The 2026 base of {{vt.sui.wage_base@2026-01-01}} USD cannot be re-derived from the prior-year base because the state annual average wage (1338(g)) was not fetched. :: VDOL state annual average wage figures.

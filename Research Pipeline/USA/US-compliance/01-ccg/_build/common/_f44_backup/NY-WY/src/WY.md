## @labour
- **Minimum wage (W.S. 27-4-202(a)) [US-WYS5-001, US-WYS5-012]:** {{wy.minwage.hourly}} USD per hour, not indexed, no 2027 change, no local power to set one. **In practice the FLSA rate (Annex FED) binds every FLSA-covered employer;** the state rate matters only for employment outside the FLSA.
- **Tipped employees (27-4-202(b)):** cash wage at least {{wy.minwage.tipped.cash_wage}} USD with make-up to the state minimum; monthly tip record; tips are the employee's property (27-4-507(a)) [US-WYS5-001, US-WYS5-002].
- **Youth training wage (27-4-202(c)):** {{wy.labour.minwage.youth_training.hourly}} USD for young employees during an initial period [US-WYS5-001].
- **Exclusions from the minimum-wage article (27-4-201(a)(iv)):** agriculture, domestic service in a private home, executive, administrative and professional employees, public employees, volunteers, commission-only outside salesmen, on-call ambulance drivers [US-WYS5-001].
- **Overtime:** {{wy.labour.overtime.state_rule}}; 27-5-101 covers only state and county employees [US-WYS5-005].
- **Pay frequency (27-4-101(a)) [US-WYS5-002]:** mandatory only for {{wy.labour.pay_frequency.semimonthly_industries}}; a payday on a non-working day moves to the preceding working day; no general rule for other employers; agricultural operations exempt.
- **Method of payment [US-WYS5-002]:** lawful money or a check cashable at a bank; direct deposit only with the employee's voluntary authorisation ({{wy.labour.direct_deposit.consent_required}}). No paycard statute.
- **Records (27-4-203):** name, address, occupation, rate, pay per period, daily and weekly hours, kept {{wy.records.retention_years}} years [US-WYS5-001].

## @income_tax
- **No state income tax and no withholding** (exists: {{wy.pit.exists}}); income, earnings and wage-based taxes are preempted at every level (W.S. 39-12-101) [US-WYP51-001]. **No local wage tax** (exists: {{wy.local_wage_tax.exists}}).
- **Resident and nonresident matrix.** Nothing is withheld for Wyoming for any income type; a Wyoming resident working in a wage-taxing state is withheld for that state (Annex MULTI). Oracle: federal only (Annex FED).

## @social
- **Unemployment insurance (DWS, WYUI) [US-WYS5-008, US-WYS5-003].** Taxable wage base:

| Year | Wage base |
|---|---|
| 2026 | {{wy.sui.wage_base@2026-01-01}} USD |
| 2027 | {{wy.sui.wage_base@2027-01-01}} USD |

  Indexed annually to a share of the statewide average annual wage, rounded down (27-3-102(a)(xviii)(A), 27-3-303(a)). Wages paid under another state's UI law count toward the base: {{wy.sui.wage_base.other_state_credit}}.
- **Employer only:** contributions may not be deducted from wages; employee rate {{wy.sui.employee.rate}} % (27-3-503(a)) [US-WYP51-002].
- **Rates:** total rate = base rate + adjustment factors; statutory base rate {{wy.ui.rate.statutory_base}} % (also for incomplete registration) [US-WYP52-001]; new employers pay the prior-year industry average plus factors, never less than {{wy.ui.rate.new_employer.floor}} % plus factors (27-3-503(f)) [US-WYP51-002]; delinquent employers +{{wy.ui.delinquent_surcharge.rate}} % [US-WYP9W-001]; statutory maximum {{wy.ui.rate.max}} % [US-WYS5-011]. The 2026 minimum rate, industry new-employer rates and factor values are not published (blocking open point below).
- **UI wages include employee retirement deferrals** ({{wy.sui.wages.401k_included}}), following FUTA [US-WYS5-003].
- **The adjustment factor** inside the UI rate funds the UI fund, the Employment Support Fund and the Workforce Development Training Fund [US-WYP51-003, US-WYP9W-001]. No transit or separate payroll levy.
- **SDI, TDI, PFML, LTC:** none (exists: {{wy.sdi_pfml.exists}}) [US-WYP51-004].
- **Workers' compensation: monopolistic state fund** ({{wy.wc.state_fund.monopolistic}}) [US-WYS5-012, US-WYS5-007]: mandatory for extra-hazardous employment; employer-paid premium with monthly payroll reports (quarterly by permission); joint UI / WC reporting available; no employee share located.

## @payslip
- **Content (27-4-101(b)) [US-WYP51-005]:** {{wy.payslip.items}}. No other content is mandated (no hours, rates, employer name or pay period). Agricultural operations exempt. Electronic delivery: statute silent. No language rule [US-WYL-001]. The duty applies to work performed in Wyoming [US-WYS5-018].

## @reporting
- **No withholding return or state W-2.**
- **Quarterly UI contribution and wage report (WYUI) [US-WYS5-009]:** due {{wy.report.ui.quarterly_due}} (weekend or holiday dates roll forward). File format: open point below.
- **Service suppliers (PEOs) (27-3-502) [US-WYS5-019]:** separate records and a separate quarterly report per client; joint liability of the client on default.
- **Workers' compensation payroll report:** monthly (Section 3) [US-WYS5-007].
- **New hire (27-1-115) [US-WYS5-006, US-WYS5-010]:** to DWS within {{wy.newhire.report_days}} days, or two monthly electronic transmissions; W-4 or approved equivalent; multistate election available.
- **Registration and agents:** Joint Business Registration in WYUI [US-WYP52-001]; POA form MODES-4444 [US-WYR3-001].

## @leave
- **No paid sick leave statute** (exists: {{wy.leave.sick.state_statute.exists}}) [US-WYP51-004, US-WYL-001]. No PFML.
- **Voting leave (22-2-111) [US-WYS5-016]:** {{wy.leave.voting.paid_hours}} hour paid on election day unless the employee has enough consecutive non-working hours while the polls are open; pay kept only if the employee votes.
- **Jury service:** protected from discharge, no duty to pay (1-11-401) [US-WYS5-013].

## @termination
- **Final pay (27-4-104) [US-WYS5-002]:** {{wy.final_pay.rule}} (or as a CBA sets), for quit or discharge; the employer may offset sums owed; layoff or suspension: next regular payday (27-4-101(d)).
- **Accrued vacation (27-4-501(a)(iii)) [US-WYS5-002]:** {{wy.term.vacation.payout}}. The Data Dictionary needs a flag recording whether a written forfeiture policy was acknowledged by the employee.
- **Notices:** no state UI separation notice or WARN law. Child support: notify the clerk after termination (20-6-212(e)) [US-WYS5-014].

## @bik
- **Income tax:** not applicable. **UI wage definition (27-3-102(a)(xviii)) [US-WYS5-003]:** exclusions follow FUTA (cafeteria-plan benefits other than cash, dependent care, educational assistance, group-term life, employer plan contributions, convenience meals and lodging, employer-paid FICA, among others); employee elective deferrals stay UI wages. Non-cash valuation rule not read (open point below).

## @deductions
- **Wage deductions [US-WYS5-002]:** no general written-authorisation statute; offsets against final wages allowed; dishonoured-check deductions restricted (W.S. title 27, ch. 4); assignments of future wages need spousal consent for married employees (27-4-111).
- **Continuing garnishment (1-15-501..511) [US-WYS5-013]:** at most {{wy.garn.creditor.max_percent}} % of weekly disposable earnings or the excess over the federal minimum-wage multiple, as under the CCPA; one writ at a time; no discharge for garnishment.
- **Child support IWO (20-6-201..222) [US-WYS5-014]:** start by the first pay period after service; remit to the SDU within {{wy.garn.iwo.remit_days}} days of payday; employer fee {{wy.garn.iwo.employer_fee.per_payment}} USD per payment within the CCPA cap; the IWO has priority over other state-law process and tolls a continuing garnishment.

## @cba
- **Wyoming Prevailing Wage Act (27-4-401 to -413) [US-WYP51-006]:** construction threshold {{wy.prevailing_wage.construction_threshold}} USD (small work exempt); records of names, occupations and wages paid (27-4-410); no certified-payroll submission form. Right-to-work state.

## @indexation
- **Minimum wage:** not indexed. **SUI wage base:** indexed yearly to the statewide average annual wage, published by DWS [US-WYS5-003, US-WYS5-008]; the derivation is consistent but not exact (open point below). **Adjustment factors:** computed annually by DWS (27-3-505), values unpublished.

## @data
- **Breach notification (40-12-501/502) [US-WYS5-015]:** personal identifying information includes name plus SSN unless redacted to {{wy.data.breach.redaction_digits}} digits or fewer. No SSN-truncation rule for pay statements found.

## @live
- **2026 budget session:** no act amends minimum wage, wage payment, UI contributions or the wage-base formula; HB0006 failed; SF0041 portable benefit accounts enacted (worker classification, not employee payroll) [US-WYS5-017].
- **2027-01-01:** wage base per Section 3 [US-WYS5-008]; 2027 rate notices due by 2026-12-31.

## @special
| Population | Wyoming rule | Register id |
|---|---|---|
| Domestic / household | Excluded from the minimum-wage article (FLSA may apply); UI above a quarterly cash test | US-WYS5-001, US-WYS5-004 |
| Agricultural | Excluded from the minimum-wage article; exempt from payday and pay-statement rules; UI coverage tests; H-2A exempt from UI | US-WYS5-001, US-WYS5-002, US-WYS5-004 |
| Minors | Hours limits and proof of age; youth wage per Section 1; a young child working for a parent excluded from UI | US-WYS5-005, US-WYS5-001, US-WYS5-004 |
| Tipped | Cash wage per Section 1; tips are the employee's property | US-WYS5-001, US-WYS5-002 |
| Clergy / religious | Excluded from UI | US-WYS5-004 |
| Students | Own-school and certified co-op students excluded from UI | US-WYS5-004 |
| Nonresident aliens | No state income tax; UI follows FUTA | US-WYP51-001, US-WYS5-004 |
| Statutory employees / contractors | UI excludes minor newspaper carriers, real-estate licensees, leased owner-operators and booth-rent stylists; portable benefit accounts | US-WYS5-004, US-WYS5-017 |
| Government employees | Excluded from the minimum-wage article; state and county overtime (27-5-101); UI-covered with exclusions | US-WYS5-001, US-WYS5-005, US-WYS5-004, US-WYS5-007 |

## @gaps
- wy.ui.rates.2026_values :: The 2026 minimum and assigned rates, the industry new-employer rates and the adjustment-factor values are not published on the pages read; the WTC rate set-up cannot be completed. :: DWS January 2026 UI rate release or WYUI rate notice (Chrome pass) / DWS helpline.
- wy.ui.wage_base.average_wage :: The exact statewide average annual wage behind the 2026 and 2027 bases is not published; only an interval check is possible. :: DWS Research & Planning average annual wage publication.

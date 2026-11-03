# Annex WY: Wyoming


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T1 - no state wage tax; SUI and levies only** (build manifest, tier rationale).

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## WY.1 Employment and labour code

- **Minimum wage (W.S. 27-4-202(a)) [US-WYS5-001, US-WYS5-012]:** [[FACT:wy.minwage.hourly=5.15]] USD per hour, not indexed, no 2027 change, no local power to set one. **In practice the FLSA rate (Annex FED) binds every FLSA-covered employer;** the state rate matters only for employment outside the FLSA.
- **Tipped employees (27-4-202(b)):** cash wage at least [[FACT:wy.minwage.tipped.cash_wage=2.13]] USD with make-up to the state minimum; monthly tip record; tips are the employee's property (27-4-507(a)) [US-WYS5-001, US-WYS5-002].
- **Youth training wage (27-4-202(c)):** [[FACT:wy.labour.minwage.youth_training.hourly=4.25]] USD for young employees during an initial period [US-WYS5-001].
- **Exclusions from the minimum-wage article (27-4-201(a)(iv)):** agriculture, domestic service in a private home, executive, administrative and professional employees, public employees, volunteers, commission-only outside salesmen, on-call ambulance drivers [US-WYS5-001].
- **Overtime:** [[FACT:wy.labour.overtime.state_rule=none for private sector (FLSA only)]]; 27-5-101 covers only state and county employees [US-WYS5-005].
- **Pay frequency (27-4-101(a)) [US-WYS5-002]:** mandatory only for [[FACT:wy.labour.pay_frequency.semimonthly_industries=railroads, mines, refineries, oil and gas, factories, mills, workshops: semimonthly (1-15 by 1st; rest by 15th)]]; a payday on a non-working day moves to the preceding working day; no general rule for other employers; agricultural operations exempt.
- **Method of payment [US-WYS5-002]:** lawful money or a check cashable at a bank; direct deposit only with the employee's voluntary authorisation ([[FACT:wy.labour.direct_deposit.consent_required=True]]). No paycard statute.
- **Records (27-4-203):** name, address, occupation, rate, pay per period, daily and weekly hours, kept [[FACT:wy.records.retention_years=2]] years [US-WYS5-001].

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wy.minwage.hourly` | [[FACT:wy.minwage.hourly=5.15]] | USD | from 2026-05-08 | US-WYS5-001 |  |
| `wy.minwage.tipped.cash_wage` | [[FACT:wy.minwage.tipped.cash_wage=2.13]] | USD | from 2026-05-08 | US-WYS5-001 |  |
| `wy.labour.minwage.youth_training.hourly` | [[FACT:wy.labour.minwage.youth_training.hourly=4.25]] | USD | from 2026-05-08 | US-WYS5-001 | under 20, first 90 consecutive days |
| `wy.labour.overtime.state_rule` | [[FACT:wy.labour.overtime.state_rule=none for private sector (FLSA only)]] |  | from 2026-05-08 | US-WYS5-005 | 27-5-101 covers state/county employees only |
| `wy.labour.pay_frequency.semimonthly_industries` | [[FACT:wy.labour.pay_frequency.semimonthly_industries=railroads, mines, refineries, oil and gas, factories, mills, workshops: semimonthly (1-15 by 1st; rest by 15th)]] |  | from 2026-05-08 | US-WYS5-002 | 27-4-101(a); no general rule for others; agriculture exempt |
| `wy.labour.direct_deposit.consent_required` | [[FACT:wy.labour.direct_deposit.consent_required=True]] |  | from 2026-05-08 | US-WYS5-002 | voluntary authorisation |

## WY.2 Income tax withholding

- **No state income tax and no withholding** (exists: [[FACT:wy.pit.exists=False]]); income, earnings and wage-based taxes are preempted at every level (W.S. 39-12-101) [US-WYP51-001]. **No local wage tax** (exists: [[FACT:wy.local_wage_tax.exists=False]]).
- **Resident and nonresident matrix.** Nothing is withheld for Wyoming for any income type; a Wyoming resident working in a wage-taxing state is withheld for that state (Annex MULTI). Oracle: federal only (Annex FED).

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wy.pit.exists` | [[FACT:wy.pit.exists=False]] |  | from 2026-01-01 | US-WYP51-001 | 39-12-101 preempts income/wage taxes at all levels |
| `wy.local_wage_tax.exists` | [[FACT:wy.local_wage_tax.exists=False]] |  | from 2026-01-01 | US-WYP51-001 |  |

## WY.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in WY.2.

## WY.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in WY.2.

## WY.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Unemployment insurance (DWS, WYUI) [US-WYS5-008, US-WYS5-003].** Taxable wage base:

| Year | Wage base |
|---|---|
| 2026 | [[FACT:wy.sui.wage_base=33,800]] USD |
| 2027 | [[FACT:wy.sui.wage_base=34,900]] USD |

  Indexed annually to a share of the statewide average annual wage, rounded down (27-3-102(a)(xviii)(A), 27-3-303(a)). Wages paid under another state's UI law count toward the base: [[FACT:wy.sui.wage_base.other_state_credit=True]].
- **Employer only:** contributions may not be deducted from wages; employee rate [[FACT:wy.sui.employee.rate=0]] % (27-3-503(a)) [US-WYP51-002].
- **Rates:** total rate = base rate + adjustment factors; statutory base rate [[FACT:wy.ui.rate.statutory_base=8.5]] % (also for incomplete registration) [US-WYB5-401]; new employers pay the prior-year industry average plus factors, never less than [[FACT:wy.ui.rate.new_employer.floor=1]] % plus factors (27-3-503(f)) [US-WYP51-002]; delinquent employers +[[FACT:wy.ui.delinquent_surcharge.rate=2]] % [US-WYP9W-001]; statutory maximum [[FACT:wy.ui.rate.max=10]] % [US-WYS5-011]. The 2026 minimum rate, industry new-employer rates and factor values are not published (blocking open point below).
- **UI wages include employee retirement deferrals** ([[FACT:wy.sui.wages.401k_included=True]]), following FUTA [US-WYS5-003].
- **The adjustment factor** inside the UI rate funds the UI fund, the Employment Support Fund and the Workforce Development Training Fund [US-WYP51-003, US-WYP9W-001]. No transit or separate payroll levy.
- **SDI, TDI, PFML, LTC:** none (exists: [[FACT:wy.sdi_pfml.exists=False]]) [US-WYP51-004].
- **Workers' compensation: monopolistic state fund** ([[FACT:wy.wc.state_fund.monopolistic=True]]) [US-WYS5-012, US-WYS5-007]: mandatory for extra-hazardous employment; employer-paid premium with monthly payroll reports (quarterly by permission); joint UI / WC reporting available; no employee share located.

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wy.sui.wage_base` | [[FACT:wy.sui.wage_base=33,800]] | USD | 2026-01-01 to 2026-12-31 | US-WYS5-008 | 55% of statewide average annual wage rounded down to 100 (US-WYS5-003); interval-consistent with DWS memo |
| `wy.sui.wage_base` | [[FACT:wy.sui.wage_base=34,900]] | USD | from 2027-01-01 | US-WYS5-008 | published |
| `wy.ui.rate.max` | [[FACT:wy.ui.rate.max=10]] | % | from 2025-01-01 | US-WYS5-011 | statutory: 8.5 base + 1.5 cap on factors (stated in DWS 2025 memo) |
| `wy.ui.delinquent_surcharge.rate` | [[FACT:wy.ui.delinquent_surcharge.rate=2]] | % | from 2026-01-01 | US-WYP9W-001 | Partly confirmed by the published source. |
| `wy.sui.wage_base.other_state_credit` | [[FACT:wy.sui.wage_base.other_state_credit=True]] |  | from 2026-05-08 | US-WYS5-003 |  |
| `wy.sui.wages.401k_included` | [[FACT:wy.sui.wages.401k_included=True]] |  | from 2026-05-08 | US-WYS5-003 |  |
| `wy.wc.state_fund.monopolistic` | [[FACT:wy.wc.state_fund.monopolistic=True]] |  | from 2026-01-01 | US-WYS5-012 | monthly payroll reports by last day of following month (US-WYS5-007); no employee share located |
| `wy.ui.rate.statutory_base` | [[FACT:wy.ui.rate.statutory_base=8.5]] | % | from 2026-01-01 | US-WYB5-401 | also when registration incomplete |
| `wy.ui.rate.new_employer.floor` | [[FACT:wy.ui.rate.new_employer.floor=1]] | % | from 2026-01-01 | US-WYP51-002 | prior-year industry average, never below 1% plus factors |
| `wy.sui.employee.rate` | [[FACT:wy.sui.employee.rate=0]] | % | from 2026-01-01 | US-WYP51-002 | 27-3-503(a) |
| `wy.sdi_pfml.exists` | [[FACT:wy.sdi_pfml.exists=False]] |  | from 2026-01-01 | US-WYP51-004 | no PFML/TDI in Title 27 |

**Open research points**

- Not yet published [[GAP:RQ-398]]: The 2026 minimum and assigned rates, the industry new-employer rates and the adjustment-factor values are not published on the pages read; the WTC rate set-up cannot be completed.
- Not configured in this release [[GAP:RQ-399]]: The exact statewide average annual wage behind the 2026 and 2027 bases is not published; only an interval check is possible.
- Not configured in this release [[GAP:RQ-401]]: Non-cash remuneration valuation rule (commission rule) not read.

## WY.4 Pay statement

- **Content (27-4-101(b)) [US-WYP51-005]:** [[FACT:wy.payslip.items=itemized written statement of all deductions on detachable part of check/voucher or attached slip]]. No other content is mandated (no hours, rates, employer name or pay period). Agricultural operations exempt. Electronic delivery: statute silent. No language rule [US-WYL-001]. The duty applies to work performed in Wyoming [US-WYS5-018].

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wy.records.retention_years` | [[FACT:wy.records.retention_years=2]] | years | from 2026-05-08 | US-WYS5-001 | 27-4-203 |
| `wy.payslip.items` | [[FACT:wy.payslip.items=itemized written statement of all deductions on detachable part of check/voucher or attached slip]] |  | from 2026-01-01 | US-WYP51-005 | 27-4-101(b); agriculture exempt |

## WY.5 Statutory reporting

- **No withholding return or state W-2.**
- **Quarterly UI contribution and wage report (WYUI) [US-WYS5-009]:** due [[FACT:wy.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] (weekend or holiday dates roll forward). File format: open point below.
- **Service suppliers (PEOs) (27-3-502) [US-WYS5-019]:** separate records and a separate quarterly report per client; joint liability of the client on default.
- **Workers' compensation payroll report:** monthly (Section 3) [US-WYS5-007].
- **New hire (27-1-115) [US-WYS5-006, US-WYS5-010]:** to DWS within [[FACT:wy.newhire.report_days=20]] days, or two monthly electronic transmissions; W-4 or approved equivalent; multistate election available.
- **Registration and agents:** Joint Business Registration in WYUI [US-WYB5-401]; POA form MODES-4444 [US-WYR3-001].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wy.report.ui.quarterly_due` | [[FACT:wy.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] |  | from 2026-01-01 | US-WYS5-009 | WYUI; next business day if weekend |
| `wy.newhire.report_days` | [[FACT:wy.newhire.report_days=20]] | days | from 2026-05-08 | US-WYS5-006 | 27-1-115; to DWS |

**Open research points**

- Not configured in this release [[GAP:RQ-400]]: WYUI wage file format and new-hire electronic format not read.

## WY.6 Leave

- **No paid sick leave statute** (exists: [[FACT:wy.leave.sick.state_statute.exists=False]]) [US-WYP51-004, US-WYL-001]. No PFML.
- **Voting leave (22-2-111) [US-WYS5-016]:** [[FACT:wy.leave.voting.paid_hours=1]] hour paid on election day unless the employee has enough consecutive non-working hours while the polls are open; pay kept only if the employee votes.
- **Jury service:** protected from discharge, no duty to pay (1-11-401) [US-WYS5-013].

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wy.leave.voting.paid_hours` | [[FACT:wy.leave.voting.paid_hours=1]] | hours | from 2026-01-01 | US-WYS5-016 | unless 3+ consecutive non-working hours while polls open; only if employee votes |
| `wy.leave.sick.state_statute.exists` | [[FACT:wy.leave.sick.state_statute.exists=False]] |  | from 2026-01-01 | US-WYP51-004 |  |

## WY.7 Termination and final pay

- **Final pay (27-4-104) [US-WYS5-002]:** [[FACT:wy.final_pay.rule=no later than the usual regular payday]] (or as a CBA sets), for quit or discharge; the employer may offset sums owed; layoff or suspension: next regular payday (27-4-101(d)).
- **Accrued vacation (27-4-501(a)(iii)) [US-WYS5-002]:** [[FACT:wy.term.vacation.payout=payable unless written forfeiture policy acknowledged in writing by employee]]. The Data Dictionary needs a flag recording whether a written forfeiture policy was acknowledged by the employee.
- **Notices:** no state UI separation notice or WARN law. Child support: notify the clerk after termination (20-6-212(e)) [US-WYS5-014].

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wy.final_pay.rule` | [[FACT:wy.final_pay.rule=no later than the usual regular payday]] |  | from 2026-05-08 | US-WYS5-002 | 27-4-104; 18% interest in suit |
| `wy.term.vacation.payout` | [[FACT:wy.term.vacation.payout=payable unless written forfeiture policy acknowledged in writing by employee]] |  | from 2026-05-08 | US-WYS5-002 | 27-4-501(a)(iii); DD flag vacation_forfeiture_policy_acknowledged |

## WY.8 Benefits in kind and taxable wages

- **Income tax:** not applicable. **UI wage definition (27-3-102(a)(xviii)) [US-WYS5-003]:** exclusions follow FUTA (cafeteria-plan benefits other than cash, dependent care, educational assistance, group-term life, employer plan contributions, convenience meals and lodging, employer-paid FICA, among others); employee elective deferrals stay UI wages. Non-cash valuation rule not read (open point below).

## WY.9 Deductions and garnishments

- **Wage deductions [US-WYS5-002]:** no general written-authorisation statute; offsets against final wages allowed; dishonoured-check deductions restricted (W.S. title 27, ch. 4); assignments of future wages need spousal consent for married employees (27-4-111).
- **Continuing garnishment (1-15-501..511) [US-WYS5-013]:** at most [[FACT:wy.garn.creditor.max_percent=25]] % of weekly disposable earnings or the excess over the federal minimum-wage multiple, as under the CCPA; one writ at a time; no discharge for garnishment.
- **Child support IWO (20-6-201..222) [US-WYS5-014]:** start by the first pay period after service; remit to the SDU within [[FACT:wy.garn.iwo.remit_days=7]] days of payday; employer fee [[FACT:wy.garn.iwo.employer_fee.per_payment=5]] USD per payment within the CCPA cap; the IWO has priority over other state-law process and tolls a continuing garnishment.

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wy.garn.creditor.max_percent` | [[FACT:wy.garn.creditor.max_percent=25]] | % | from 2026-01-01 | US-WYS5-013 | or excess over 30x FMW (CCPA); writ 90 days; one at a time |
| `wy.garn.iwo.employer_fee.per_payment` | [[FACT:wy.garn.iwo.employer_fee.per_payment=5]] | USD | from 2026-01-01 | US-WYS5-014 | remit within 7 days; priority over garnishment |
| `wy.garn.iwo.remit_days` | [[FACT:wy.garn.iwo.remit_days=7]] | days | from 2026-01-01 | US-WYS5-014 |  |

## WY.10 Collective agreements and prevailing wage

- **Wyoming Prevailing Wage Act (27-4-401 to -413) [US-WYP51-006]:** construction threshold [[FACT:wy.prevailing_wage.construction_threshold=100,000]] USD (small work exempt); records of names, occupations and wages paid (27-4-410); no certified-payroll submission form. Right-to-work state.

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wy.prevailing_wage.construction_threshold` | [[FACT:wy.prevailing_wage.construction_threshold=100,000]] | USD | from 2026-01-01 | US-WYP51-006 | Wyoming Prevailing Wage Act; work <=25,000 exempt |

## WY.11 Indexation

- **Minimum wage:** not indexed. **SUI wage base:** indexed yearly to the statewide average annual wage, published by DWS [US-WYS5-003, US-WYS5-008]; the derivation is consistent but not exact (open point below). **Adjustment factors:** computed annually by DWS (27-3-505), values unpublished.

## WY.12 Payroll data protection and records

- **Breach notification (40-12-501/502) [US-WYS5-015]:** personal identifying information includes name plus SSN unless redacted to [[FACT:wy.data.breach.redaction_digits=5]] digits or fewer. No SSN-truncation rule for pay statements found.

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wy.data.breach.redaction_digits` | [[FACT:wy.data.breach.redaction_digits=5]] |  | from 2026-01-01 | US-WYS5-015 | redacted to 5 digits or fewer = not PII |

## WY.13 Live legal change

- **2026 budget session:** no act amends minimum wage, wage payment, UI contributions or the wage-base formula; HB0006 failed; SF0041 portable benefit accounts enacted (worker classification, not employee payroll) [US-WYS5-017].
- **2027-01-01:** wage base per Section 3 [US-WYS5-008]; 2027 rate notices due by 2026-12-31.

## WY.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## WY.15 Special populations

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

## WY.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## WY.S Sources

Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file. Authorities:

- Build lead (Claude) under owner delegation (Wallisson Gomes): US-OWN-006
- Owner (Wallisson Gomes): US-OWN-008
- Wyoming Department of Workforce Services: US-WYB5-401, US-WYS5-008, US-WYS5-009, US-WYS5-010, US-WYS5-011, US-WYS5-012, US-WYS5-018
- Wyoming Department of Workforce Services, Unemployment Tax Division: US-WYR3-001
- Wyoming Legislative Service Office: US-WYS5-017
- Wyoming Legislature: US-WYP51-001, US-WYP51-002, US-WYP51-003, US-WYP51-004, US-WYP51-005, US-WYP51-006, US-WYP9W-001, US-WYS5-001, US-WYS5-002, US-WYS5-003, US-WYS5-004, US-WYS5-005, US-WYS5-006, US-WYS5-007, US-WYS5-013, US-WYS5-014, US-WYS5-015, US-WYS5-016, US-WYS5-019
- Wyoming Legislature (Title 27 compiled PDF 2026-05-08): US-WYL-001

# Annex SD: South Dakota


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T1 - no state wage tax; SUI and levies only** (build manifest, tier rationale).

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## SD.1 Employment and labour code

- **Minimum wage (SDCL 60-11-3, 60-11-3.2) [US-SDS5-001, US-SDS5-003]:** [[FACT:sd.minwage.hourly=11.85]] USD per hour from 2026-01-01 and [[FACT:sd.minwage.hourly=12.30]] USD from 2027-01-01 (published).
- **Tipped employees (60-11-3.1) [US-SDS5-001, US-SDS5-003]:** cash wage at least half the minimum wage: [[FACT:sd.minwage.tipped.cash_wage=5.925]] USD in 2026 and [[FACT:sd.minwage.tipped.cash_wage=6.15]] USD in 2027; the employer makes up any shortfall each pay period and keeps a record of all tips.
- **Opportunity wage** for young workers per FLSA s.6 (60-11-4.1); apprentices, learners and persons with a developmental disability only with a DLR permit (60-11-5) [US-SDS5-001].
- **Local minimum wage:** none located; no preemption clause in the text read (open point below).
- **Overtime:** [[FACT:sd.labour.overtime.state_rule=none (FLSA only)]] [US-SDS5-012]. No state break or holiday-pay requirement [US-SDS5-011].
- **Pay frequency and method (60-11-9) [US-SDS5-001]:** [[FACT:sd.pay_frequency.rule=at least once each calendar month or regular designated paydays]], in lawful money; check, cash or direct deposit unless otherwise agreed. No express consent rule for direct deposit or paycards located (open point below). The wage-payment sections cover employers "employing any person of this state" (60-11-8).

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sd.minwage.hourly` | [[FACT:sd.minwage.hourly=11.85]] | USD | 2026-01-01 to 2026-12-31 | US-SDS5-003 |  |
| `sd.minwage.hourly` | [[FACT:sd.minwage.hourly=12.30]] | USD | from 2027-01-01 | US-SDS5-003 |  |
| `sd.minwage.indexation` | [[FACT:sd.minwage.indexation=CPI-U Aug/Aug, rounded UP to 5 cents, never decreases; published by 15 Oct]] |  | from 2026-01-01 | US-SDS5-001 | SDCL 60-11-3.2 |
| `sd.minwage.tipped.cash_wage` | [[FACT:sd.minwage.tipped.cash_wage=5.925]] | USD | 2026-01-01 to 2026-12-31 | US-SDS5-003 | 50% of minimum; tips >35/month |
| `sd.minwage.tipped.cash_wage` | [[FACT:sd.minwage.tipped.cash_wage=6.15]] | USD | from 2027-01-01 | US-SDS5-003 |  |
| `sd.labour.overtime.state_rule` | [[FACT:sd.labour.overtime.state_rule=none (FLSA only)]] |  | from 2026-01-01 | US-SDS5-012 |  |
| `sd.pay_frequency.rule` | [[FACT:sd.pay_frequency.rule=at least once each calendar month or regular designated paydays]] |  | from 2026-01-01 | US-SDS5-001 | 60-11-9; check, cash or direct deposit |

**Open research points**

- Not configured in this release [[GAP:RQ-322]]: Not established from an official source.

## SD.2 Income tax withholding

- **No state income tax and no withholding** (income tax exists: [[FACT:sd.pit.exists=False]]) [US-SD-001]: no state W-4, supplemental rate, rounding rule, state W-2 or reciprocity.
- **No local income tax** (exists: [[FACT:sd.local_wage_tax.exists=False]]) [US-SDP52-001].
- **Resident and nonresident matrix.** Nothing is withheld for South Dakota for any income type, resident or nonresident. A South Dakota resident working in a wage-taxing state is withheld for that state under its rules (Annex MULTI).

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sd.pit.exists` | [[FACT:sd.pit.exists=False]] |  | from 2026-01-01 | US-SD-001 | no withholding, W-4, W-2 filing, reciprocity |
| `sd.local_wage_tax.exists` | [[FACT:sd.local_wage_tax.exists=False]] |  | from 2026-07-01 | US-SDP52-001 |  |

## SD.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in SD.2.

## SD.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in SD.2.

## SD.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Reemployment Assistance (UI), DLR [US-SDS5-002, US-SDS5-018].**
  - Taxable wage base [[FACT:sd.sui.wage_base=15,000]] USD, fixed in statute and not indexed (61-1-46); wages already reported to another state in the year count toward it: [[FACT:sd.sui.wage_base.other_state_credit=True]].
  - New employer: [[FACT:sd.ui.rate.new_employer.year1=1.2]] % in year one, then [[FACT:sd.ui.rate.new_employer.later=1]] % while the account balance is positive until experience-rated; construction new employers [[FACT:sd.ui.rate.new_employer.construction.year1=6]] % in year one (61-5-24).
  - Experience-rated employers: the schedule is set by the fund's average high cost multiplier (61-5-25). Schedule in effect for 2026: [[FACT:sd.ui.schedule.in_effect=C]]; its top rate is [[FACT:sd.sui.employer.rate.max=8.52]] % (61-5-25.7, SL 2025 ch 199). A DLR page quoting a higher maximum predates 2026; the statute governs [US-SDS5-013].
  - Administrative fee [[FACT:sd.ui.admin_fee.rate=0.08]] % for every experience-rated employer from 2026 (61-5-28.1); investment fee [[FACT:sd.ui.investment_fee.new_employer.rate=0.55]] % for employers not yet rated, lower by reserve ratio for rated employers (61-5-29). Neither fee may be deducted from wages. Fund-balance surcharge (61-5-28) dormant.
  - Employee contribution [[FACT:sd.sui.employee.rate=0]] % [US-SDP51-002].
- **UI wages [US-SDS5-013]:** employee pre-tax deferrals are included ([[FACT:sd.sui.wages.401k_included=True]]) and cafeteria-plan amounts are included ([[FACT:sd.sui.wages.section125_included=True]]); employer plan contributions and non-required severance are excluded.
- **No SDI, TDI, PFML, LTC or transit levy** (exists: [[FACT:sd.sdi_pfml.exists=False]]) [US-SDP51-002].

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sd.sui.wage_base` | [[FACT:sd.sui.wage_base=15,000]] | USD | from 2015-01-01 | US-SDS5-002 | 61-1-46, not indexed; other-state wages count |
| `sd.sui.wage_base.other_state_credit` | [[FACT:sd.sui.wage_base.other_state_credit=True]] |  | from 2026-01-01 | US-SDS5-002 |  |
| `sd.ui.rate.new_employer.year1` | [[FACT:sd.ui.rate.new_employer.year1=1.2]] | % | from 2026-01-01 | US-SDS5-002 | then [[FACT:sd.ui.rate.new_employer.later=1.0]]% while positive balance; construction 6% then 3% |
| `sd.ui.rate.new_employer.later` | [[FACT:sd.ui.rate.new_employer.later=1]] | % | from 2026-01-01 | US-SDS5-002 |  |
| `sd.ui.rate.new_employer.construction.year1` | [[FACT:sd.ui.rate.new_employer.construction.year1=6]] | % | from 2026-01-01 | US-SDS5-002 |  |
| `sd.ui.schedule.in_effect` | [[FACT:sd.ui.schedule.in_effect=C]] |  | 2026-01-01 to 2026-12-31 | US-SDS5-018 | AHCM >=1.50; rates 0.00-[[FACT:sd.sui.employer.rate.max=8.52]]% |
| `sd.sui.employer.rate.max` | [[FACT:sd.sui.employer.rate.max=8.52]] | % | 2026-01-01 to 2026-12-31 | US-SDS5-002 | Schedule C top (row mapping by hand); DLR page 9.5% is stale |
| `sd.ui.admin_fee.rate` | [[FACT:sd.ui.admin_fee.rate=0.08]] | % | from 2026-01-01 | US-SDS5-002 | all experience-rated employers; not new employers |
| `sd.ui.investment_fee.new_employer.rate` | [[FACT:sd.ui.investment_fee.new_employer.rate=0.55]] | % | from 2026-01-01 | US-SDS5-002 | rated 0.00-0.53% |
| `sd.sui.wages.401k_included` | [[FACT:sd.sui.wages.401k_included=True]] |  | from 2026-01-01 | US-SDS5-013 |  |
| `sd.sui.wages.section125_included` | [[FACT:sd.sui.wages.section125_included=True]] |  | from 2026-01-01 | US-SDS5-013 |  |
| `sd.sui.employee.rate` | [[FACT:sd.sui.employee.rate=0]] | % | from 2026-01-01 | US-SDP51-002 | fees may not be deducted |
| `sd.sdi_pfml.exists` | [[FACT:sd.sdi_pfml.exists=False]] |  | from 2026-01-01 | US-SDP51-002 | no employee SDI/PFML premium in the RA handbook |

## SD.4 Pay statement

- **No pay-statement statute** (exists: [[FACT:sd.payslip.statute.exists=False]]) [US-SDS5-001, US-SD-003, US-SDL-001]; federal recordkeeping applies (Annex FED). The RA handbook lists the per-employee records to keep [US-SDP51-002]; the retention period is open (below).

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sd.payslip.statute.exists` | [[FACT:sd.payslip.statute.exists=False]] |  | from 2026-01-01 | US-SDS5-001 | Title 60 full-text scan |

**Open research points**

- Not configured in this release [[GAP:RQ-324]]: RA record retention period not read.

## SD.5 Statutory reporting

- **No state withholding return, reconciliation or state W-2.**
- **Quarterly RA wage report (Form 21) [US-SDS5-013, US-SDS5-014]:** due (received by) [[FACT:sd.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31 (received)]]; zero reports required; online system or file upload; corrections on Form 21C; domestic employers may elect annual filing [US-SDS5-020].
- **New hire (25-7A-3.3) [US-SDS5-007, US-SDS5-015]:** within [[FACT:sd.newhire.report_days=20]] days, or two monthly electronic transmissions, to the DLR New Hire Reporting Center; covers rehires; a multistate employer may designate one state.
- **Registration and agents:** online registration [US-SDS5-020]; RA power of attorney [US-SDP51-001].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sd.report.ui.quarterly_due` | [[FACT:sd.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31 (received)]] |  | from 2026-01-01 | US-SDS5-013 | Form 21; zero reports; CD layout 85-byte E/S records (US-SDS5-014) |
| `sd.newhire.report_days` | [[FACT:sd.newhire.report_days=20]] | days | from 2026-01-01 | US-SDS5-007 | 25-7A-3.3 |

## SD.6 Leave

- **No paid sick leave, vacation, holiday or PFML statute** (sick leave statute exists: [[FACT:sd.leave.sick.state_statute.exists=False]]) [US-SDS5-011].
- **Voting leave (12-3-5) [US-SDS5-008]:** [[FACT:sd.leave.voting.paid_hours=2]] consecutive hours off while the polls are open, with no deduction from wages, unless the employee already has that much off-duty time.
- **Jury duty:** protection from discharge; pay at the employer's discretion (16-13-41.1). Military: SCRA protections for National Guard; no state duty to pay [US-SDS5-009].

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sd.leave.sick.state_statute.exists` | [[FACT:sd.leave.sick.state_statute.exists=False]] |  | from 2026-01-01 | US-SDS5-011 |  |
| `sd.leave.voting.paid_hours` | [[FACT:sd.leave.voting.paid_hours=2]] | hours | from 2026-01-01 | US-SDS5-008 | no deduction from wages (12-3-5) |

## SD.7 Termination and final pay

- **Final pay (60-11-10, 60-11-11) [US-SDS5-001, US-SDS5-010]:** [[FACT:sd.final_pay.rule=next regular payday (or when property returned)]], on discharge or resignation.
- **Accrued vacation:** no statutory payout rule; follows the agreement or policy (case law open, below) [US-SDS5-011]. No severance, separation-notice or WARN duty.

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sd.final_pay.rule` | [[FACT:sd.final_pay.rule=next regular payday (or when property returned)]] |  | from 2026-01-01 | US-SDS5-001 | 60-11-10/11 |

**Open research points**

- Not configured in this release [[GAP:RQ-325]]: SD Supreme Court holdings on vested vacation not established from an official source.

## SD.8 Benefits in kind and taxable wages

- **Income tax:** not applicable. **UI base:** employee deferrals and cafeteria-plan amounts included; employer plan contributions excluded; board, lodging and goods included at cash value [US-SDS5-013].

## SD.9 Deductions and garnishments

- **Wage-deduction authorisation:** no SD statute located; federal limits apply (open point below).
- **Ordinary garnishment (21-18-51) [US-SDS5-006]:** the lesser of [[FACT:sd.garn.creditor.max_percent=20]] % of weekly disposable earnings, or disposable earnings minus a protected floor of forty times the minimum wage ([[FACT:sd.garn.consumer.floor.weekly=474.00]] USD per week in 2026), reduced by [[FACT:sd.garn.consumer.dependent_reduction.weekly=25]] USD per week for each dependent family member living with the debtor. Stricter than the CCPA. Support orders: CCPA support percentages (21-18-52).
- **Child support IWO [US-SDS5-007]:** statutory cap (25-7A-32); first deduction from the first pay after service; remit within the statutory business days; employer fee up to [[FACT:sd.garn.iwo.employer_fee.monthly=3]] USD per month (25-7A-34); current support has priority (25-7A-35).

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sd.garn.creditor.max_percent` | [[FACT:sd.garn.creditor.max_percent=20]] | % | from 2026-01-01 | US-SDS5-006 | lesser of 20% weekly disposable or disposable - 40x minimum - 25/week per dependent |
| `sd.garn.consumer.floor.weekly` | [[FACT:sd.garn.consumer.floor.weekly=474.00]] | USD | 2026-01-01 to 2026-12-31 | US-SDS5-006 |  |
| `sd.garn.consumer.dependent_reduction.weekly` | [[FACT:sd.garn.consumer.dependent_reduction.weekly=25]] | USD | from 2026-01-01 | US-SDS5-006 |  |
| `sd.garn.iwo.employer_fee.monthly` | [[FACT:sd.garn.iwo.employer_fee.monthly=3]] | USD | from 2026-01-01 | US-SDS5-007 | remit within 7 business days; cap 50% |

**Open research points**

- Not configured in this release [[GAP:RQ-323]]: No SD rule on written authorisation for deductions or paycard/direct-deposit consent.

## SD.10 Collective agreements and prevailing wage

- **No state prevailing-wage law** (exists: [[FACT:sd.prevailing_wage.exists=False]]) [US-SDP51-003]; federal Davis-Bacon only. The evidence rests on an indirect read of the federal state table (open point below).

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sd.prevailing_wage.exists` | [[FACT:sd.prevailing_wage.exists=False]] |  | from 2026-01-01 | US-SDP51-003 |  |

**Open research points**

- Not configured in this release [[GAP:RQ-327]]: Not established from an official source.

## SD.11 Indexation

- **Minimum wage:** [[FACT:sd.minwage.indexation=CPI-U Aug/Aug, rounded UP to 5 cents, never decreases; published by 15 Oct]] [US-SDS5-001, US-SDS5-005]. The tipped wage follows automatically.
- **RA wage base:** not indexed; the rate schedule moves with the fund's high cost multiplier each year (61-5-25).

## SD.12 Payroll data protection and records

- **Breach notice (22-40-19..26) [US-SDS5-017]:** personal information includes the SSN; notify affected residents within the statutory period and the Attorney General when more than [[FACT:sd.data.breach.ag_threshold=250]] residents are affected. No SSN-truncation rule for pay statements located.

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `sd.data.breach.ag_threshold` | [[FACT:sd.data.breach.ag_threshold=250]] |  | from 2018-07-01 | US-SDS5-017 | notify residents within 60 days |

## SD.13 Live legal change

- **2026-01-01 (SL 2025 ch 199):** new rate table and administrative fee for rated employers [US-SDS5-002].
- **SL 2026 ch 205 and ch 204:** investment-fund administration and state apprenticeship agency; payroll-neutral [US-SDS5-002, US-SDS5-001].
- **2027-01-01:** minimum wage and tipped wage per Section 1 [US-SDS5-003]. The 2027 schedule appears only in unapproved advisory-council minutes [US-SDS5-019]; the 2026 session-law list was not read (open point below).

**Open research points**

- Not configured in this release [[GAP:RQ-326]]: LRC 2026 session-law list not read.

## SD.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## SD.15 Special populations

| Population | South Dakota rule | Register id |
|---|---|---|
| Domestic / household | RA coverage above a quarterly cash test (61-1-19); annual reporting option; babysitters excluded from minimum wage | US-SDS5-002, US-SDS5-020, US-SDS5-001 |
| Agricultural | RA coverage tests and crew-leader rules (61-1-17); no state minimum-wage exclusion beyond FLSA | US-SDS5-002 |
| Minors | Hours limits (ch. 60-12); opportunity wage (60-11-4.1); minor newspaper carriers RA-exempt | US-SDS5-016, US-SDS5-001, US-SDS5-002 |
| Tipped | Cash wage per Section 1; make-up each pay period; tips above a monthly test are RA wages | US-SDS5-001, US-SDS5-003, US-SDS5-013 |
| Clergy / religious | RA-exempt (61-1-36) | US-SDS5-002 |
| Students | RA-exempt for own-school, work-study, student nurses and interns (61-1-37, 61-1-38) | US-SDS5-002 |
| Nonresident aliens | No state rule (no income tax); RA follows work localization | US-SD-001, US-SDS5-020 |
| Statutory employees / contractors | RA two-prong test (61-1-11) | US-SDS5-002, US-SDS5-004 |
| Family employment | RA-exempt for service for a child or spouse and a young child working for a parent (61-1-44); corporations have no family exemption | US-SDS5-002, US-SDS5-013 |
| Government employees | State and political subdivisions covered; elected officials, legislators, judges and National Guard excluded | US-SDS5-002 |
| Seasonal amusement / camps | Excluded from minimum wage and tipped wage under the statutory season test | US-SDS5-001 |

## SD.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## SD.S Sources

Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file. Authorities:

- SD Department of Revenue: US-SDP52-001
- South Dakota Department of Labor and Regulation: US-SDP51-002, US-SDS5-003, US-SDS5-011, US-SDS5-012, US-SDS5-013
- South Dakota Department of Labor and Regulation (RA Advisory Council): US-SDS5-018
- South Dakota Department of Revenue: US-SD-001
- South Dakota Legislature (Legislative Research Council): US-SDS5-001, US-SDS5-002, US-SDS5-006, US-SDS5-007, US-SDS5-008, US-SDS5-017
- US Department of Labor Wage and Hour Division: US-SDP51-003

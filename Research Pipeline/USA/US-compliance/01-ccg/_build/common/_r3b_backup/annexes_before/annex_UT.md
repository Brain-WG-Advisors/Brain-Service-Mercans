# Annex UT: Utah


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T3 - state withholding; local layer absent or piggybacked on the state return** (build manifest, tier rationale).

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## UT.1 Employment and labour code

- **Minimum wage [US-UTS5-011, US-UTS5-010]:** [[FACT:ut.minwage.hourly=7.25]] USD per hour, unchanged since 2009-07-24; Utah Code 34-40-103(2)(b) bars the Labor Commission from setting a rate above the federal minimum. No 2027 change. No local rate can exceed it.
- **Minors:** at least [[FACT:ut.labour.minwage.minor_first_90_days.hourly=4.25]] USD per hour for an initial period with an employer, then the full minimum (R610-1-3(B)) [US-UTS5-011].
- **Tipped employees [US-UTS5-011, US-UTS5-008]:** cash wage [[FACT:ut.minwage.tipped.cash_wage=2.13]] USD per hour; written notice at hire; pooling only among tipped staff.
- **Overtime:** [[FACT:ut.labour.overtime.state_rule=none (FLSA only)]] [US-UTS5-007]. Hours worked include on-call time on the premises, meetings, training and rest breaks; fully relieved meal periods are excluded (R610-1-2(B)).
- **Pay frequency (34-28-3(1)) [US-UTP6-001, US-UTS5-009]:** [[FACT:ut.pay_frequency.rule=at least semimonthly within 10 days after period close; yearly salary monthly by 7th]].
- **Pay cards (R610-3-22) [US-UTS5-012]:** allowed only with [[FACT:ut.labour.paycard.conditions=one fee-free full withdrawal; full pay available on payday; deduction statement each payday]]. Direct-deposit consent rule: open point below.

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ut.minwage.hourly` | [[FACT:ut.minwage.hourly=7.25]] | USD | from 2009-07-24 | US-UTS5-011 | capped at federal (34-40-103(2)(b), US-UTS5-010); DOL second authority US-UTS5-007 |
| `ut.labour.minwage.minor_first_90_days.hourly` | [[FACT:ut.labour.minwage.minor_first_90_days.hourly=4.25]] | USD | from 2009-07-24 | US-UTS5-011 | R610-1-3(B) |
| `ut.minwage.tipped.cash_wage` | [[FACT:ut.minwage.tipped.cash_wage=2.13]] | USD | from 2009-07-24 | US-UTS5-011 | tips >=30/month |
| `ut.labour.overtime.state_rule` | [[FACT:ut.labour.overtime.state_rule=none (FLSA only)]] |  | from 2026-01-01 | US-UTS5-007 |  |
| `ut.pay_frequency.rule` | [[FACT:ut.pay_frequency.rule=at least semimonthly within 10 days after period close; yearly salary monthly by 7th]] |  | from 2014-05-13 | US-UTP6-001 | 34-28-3(1) |
| `ut.labour.paycard.conditions` | [[FACT:ut.labour.paycard.conditions=one fee-free full withdrawal; full pay available on payday; deduction statement each payday]] |  | from 2012-04-16 | US-UTS5-012 | R610-3-22 |

**Open research points**

- Not configured in this release [[GAP:RQ-347]]: Direct-deposit consent rule (34-28-2/-3 current) not read.
- Not configured in this release [[GAP:RQ-348]]: 34-40-104 exemptions (agricultural, seasonal, domestic) not read.

## UT.2 Income tax withholding

- **Rate:** flat [[FACT:ut.pit.rate.flat=4.45]] % of state taxable income from 2026-01-01 (Utah Code 59-10-104, Ch. 250 of 2026) [US-UTS5-001].
- **Withholding method [US-UTPIT-003, US-UTS5-013]:** [[FACT:ut.wh.method=Pub 14 Rev. 04/26: wages x 4.45% minus max(0, base allowance - 1.3% x (wages - threshold)); all lines rounded to whole dollars]]. Certificate: [[FACT:ut.wh.certificate=federal W-4 filing status only (no Utah W-4; allowances ignored)]]; Utah taxable wages are the wages subject to federal withholding (IRC 3401(a)).

| Parameter (annual) | Single (also head of household) | Married | Register id |
|---|---|---|---|
| Base allowance | [[FACT:ut.pit.base_allowance.single.annual=485]] USD | [[FACT:ut.pit.base_allowance.married.annual=970]] USD | US-UTPIT-003 |
| Phase-out threshold | [[FACT:ut.pit.phaseout_threshold.single.annual=9348]] USD | [[FACT:ut.pit.phaseout_threshold.married.annual=18,696]] USD | US-UTPIT-003 |
| Phase-out rate | [[FACT:ut.pit.phaseout.rate=1.3]] % | same | US-UTPIT-003 |

  Per-period parameters are the annual values divided by the number of periods (Pub 14 prints them). Rounding: [[FACT:ut.pit.rounding=all lines to whole dollars, half up]].
- **Effective date of these schedules: blocking open point.** Pub 14 Rev. 04/26 does not state it; a mid-year change is possible. Do not apply these parameters to pay periods before the effective date is established (open point below).
- **Oracle (Pub 14 worked examples, all reproduced):** example 1 [[FACT:ut.pit.oracle.example_1.withholding=12]] USD; example 2 [[FACT:ut.pit.oracle.example_2.withholding=116]] USD; example 3 [[FACT:ut.pit.oracle.example_3.withholding=18]] USD; example 4 [[FACT:ut.pit.oracle.example_4.withholding=347]] USD; example 5 [[FACT:ut.pit.oracle.example_5.withholding=367]] USD; example 6 [[FACT:ut.pit.oracle.example_6.withholding=5]] USD. Recomputation in Module 12.
- **Supplemental wages:** no Utah flat rate published; supplemental pay runs through the regular schedules (open point below).
- **Exempt certificate:** an employee who filed a federal exempt W-4 is not withheld (R865-9I-15).
- **Nonresidents and multistate (R865-9I-14(A)-(C)) [US-UTS5-013, US-UTP51-002]:** nonresidents are withheld on services performed in Utah; residents on all wages, reduced by another state's required withholding. Safe harbour: no Utah withholding for a nonresident with no other Utah income who works [[FACT:ut.pit.nonresident.days_safe_harbour=20]] days or less in Utah and lives in a no-tax or similarly excluding state (not for athletes, entertainers, real-property laborers or key employees). Interstate transportation employees and military spouses are exempt (notes in federal W-4 box 4c). Reciprocity: [[FACT:ut.reciprocity.states=none]].
- **Local income tax:** none (exists: [[FACT:ut.local_wage_tax.exists=False]]) [US-UTR3-002].
- **Resident and nonresident matrix.**

| Income type | Utah resident | Nonresident |
|---|---|---|
| Regular salary | Pub 14 formula on all wages, less other states' required withholding | Pub 14 formula on Utah-allocable wages, subject to the safe harbour |
| Bonus / supplemental | Through the regular schedules | Same, Utah share |
| Severance, equity, benefits in kind | Follow federal withholding wages | Utah-allocable share |
| Interstate transportation / military spouse | Resident-state rules | Exempt from Utah withholding |

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ut.pit.rate.flat` | [[FACT:ut.pit.rate.flat=4.45]] | % | from 2026-01-01 | US-UTS5-001 | 59-10-104 as amended by Ch. 250 (2026 GS); retroactive to 2026-01-01 |
| `ut.wh.certificate` | [[FACT:ut.wh.certificate=federal W-4 filing status only (no Utah W-4; allowances ignored)]] |  | from 2026-01-01 | US-UTS5-013 | R865-9I-14(E)-(G) |
| `ut.pit.nonresident.days_safe_harbour` | [[FACT:ut.pit.nonresident.days_safe_harbour=20]] | days | from 2026-01-01 | US-UTS5-013 | no other UT income; home state no-tax or similar exclusion; excludes athletes, entertainers, real-property laborers, key employees |
| `ut.reciprocity.states` | [[FACT:ut.reciprocity.states=none]] |  | from 2026-01-01 | US-UTS5-013 | MULTI matrix |
| `ut.local_wage_tax.exists` | [[FACT:ut.local_wage_tax.exists=False]] |  | from 2026-01-01 | US-UTR3-002 | A.3 |
| `ut.wh.method` | [[FACT:ut.wh.method=Pub 14 Rev. 04/26: wages x 4.45% minus max(0, base allowance - 1.3% x (wages - threshold)); all lines rounded to whole dollars]] |  | from 2026-01-01 | US-UTPIT-003 | earlier 450/900) |
| `ut.pit.base_allowance.single.annual` | [[FACT:ut.pit.base_allowance.single.annual=485]] | USD | from 2026-01-01 | US-UTPIT-003 | also HoH; see effective-date question |
| `ut.pit.base_allowance.married.annual` | [[FACT:ut.pit.base_allowance.married.annual=970]] | USD | from 2026-01-01 | US-UTPIT-003 |  |
| `ut.pit.phaseout_threshold.single.annual` | [[FACT:ut.pit.phaseout_threshold.single.annual=9348]] | USD | from 2026-01-01 | US-UTPIT-003 |  |
| `ut.pit.phaseout_threshold.married.annual` | [[FACT:ut.pit.phaseout_threshold.married.annual=18,696]] | USD | from 2026-01-01 | US-UTPIT-003 |  |
| `ut.pit.phaseout.rate` | [[FACT:ut.pit.phaseout.rate=1.3]] | % | from 2026-01-01 | US-UTPIT-003 |  |
| `ut.pit.rounding` | [[FACT:ut.pit.rounding=all lines to whole dollars, half up]] |  | from 2026-01-01 | US-UTPIT-003 | 9,000 x 0.0445 = 400.5 -> 401 |
| `ut.pit.oracle.example_1.withholding` | [[FACT:ut.pit.oracle.example_1.withholding=12]] | USD | from 2026-01-01 | US-UTPIT-003 | weekly single 400 |
| `ut.pit.oracle.example_2.withholding` | [[FACT:ut.pit.oracle.example_2.withholding=116]] | USD | from 2026-01-01 | US-UTPIT-003 | biweekly single 2,600 |
| `ut.pit.oracle.example_3.withholding` | [[FACT:ut.pit.oracle.example_3.withholding=18]] | USD | from 2026-01-01 | US-UTPIT-003 | semimonthly married 1,200 |
| `ut.pit.oracle.example_4.withholding` | [[FACT:ut.pit.oracle.example_4.withholding=347]] | USD | from 2026-01-01 | US-UTPIT-003 | monthly married 7,800 |
| `ut.pit.oracle.example_5.withholding` | [[FACT:ut.pit.oracle.example_5.withholding=367]] | USD | from 2026-01-01 | US-UTPIT-003 | quarterly single 9,000 |
| `ut.pit.oracle.example_6.withholding` | [[FACT:ut.pit.oracle.example_6.withholding=5]] | USD | from 2026-01-01 | US-UTPIT-003 |  |

**Open research points**

- Not yet published [[GAP:RQ-343]]: Pub 14 Rev. 04/26 does not state from which pay period its base allowances and thresholds apply; a secondary source points to a mid-year 2026 change from lower earlier allowances. Calculations for pay periods before the effective date cannot be fixed.
- Not configured in this release [[GAP:RQ-344]]: No Utah supplemental flat rate published; build assumes regular schedules.

## UT.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in UT.2.

## UT.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in UT.2.

## UT.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Unemployment insurance (DWS) [US-UTSUI-001, US-UTS5-005].** 2026 taxable wage base [[FACT:ut.sui.wage_base=50,700]] USD. Overall rate = benefit ratio times the reserve factor ([[FACT:ut.ui.reserve_factor=1.1]] in 2026) plus the social cost ([[FACT:ut.ui.social_cost.rate=0.1]] %); range [[FACT:ut.sui.employer.rate.min=0.1]] % to [[FACT:ut.sui.employer.rate.max=7.1]] %; delinquency surcharge [[FACT:ut.ui.delinquency_surcharge.rate=1]] % if prior-year contributions are unpaid. New employers take the industry's average benefit ratio (no single rate); new out-of-state contractors take the maximum.
- **UI wages include employee retirement deferrals:** [[FACT:ut.sui.wages.401k_included=True]] [US-UTS5-004]; also meals, lodging, in-kind pay and tips. SUI wages differ from federal taxable wages.
- **Employee contribution:** [[FACT:ut.sui.employee.rate=0]] % [US-UTP52-005]. **SDI, TDI, PFML:** none (exists: [[FACT:ut.sdi_pfml.exists=False]]) [US-UTB5-003]. Other-state wage credit toward the base: open point below.

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ut.sui.wage_base` | [[FACT:ut.sui.wage_base=50,700]] | USD | 2026-01-01 to 2026-12-31 | US-UTS5-005 | not derivable (35A-4-303 not read) |
| `ut.sui.wages.401k_included` | [[FACT:ut.sui.wages.401k_included=True]] |  | from 2026-01-01 | US-UTS5-004 | also tips, meals, lodging, in-kind |
| `ut.ui.reserve_factor` | [[FACT:ut.ui.reserve_factor=1.1]] | ratio | 2026-01-01 to 2026-12-31 | US-UTSUI-001 | rate = benefit ratio x reserve factor + social cost |
| `ut.ui.social_cost.rate` | [[FACT:ut.ui.social_cost.rate=0.1]] | % | 2026-01-01 to 2026-12-31 | US-UTSUI-001 |  |
| `ut.sui.employer.rate.min` | [[FACT:ut.sui.employer.rate.min=0.1]] | % | 2026-01-01 to 2026-12-31 | US-UTSUI-001 |  |
| `ut.sui.employer.rate.max` | [[FACT:ut.sui.employer.rate.max=7.1]] | % | 2026-01-01 to 2026-12-31 | US-UTSUI-001 | new out-of-state contractors 7.1; new employers industry average |
| `ut.ui.delinquency_surcharge.rate` | [[FACT:ut.ui.delinquency_surcharge.rate=1]] | % | 2026-01-01 to 2026-12-31 | US-UTSUI-001 |  |
| `ut.sui.employee.rate` | [[FACT:ut.sui.employee.rate=0]] | % | from 2026-01-01 | US-UTP52-005 |  |
| `ut.sdi_pfml.exists` | [[FACT:ut.sdi_pfml.exists=False]] |  | from 2026-01-01 | US-UTB5-003 | Agency level: the USTC 'List of All Tax Types' carries Employer Withholding Tax as the only wage-based employer tax; no state disability, paid-leave or local wage tax. A DWS/Labor Commission statement would raise confidence. |

**Open research points**

- Not configured in this release [[GAP:RQ-345]]: SUI credit for other-state wages not proven (35A-4-303 not reached).
- Not configured in this release [[GAP:RQ-346]]: 2027 SUI base and range due mid-November 2026.

## UT.4 Pay statement

- **Content (34-28-3(4); R610-3-20) [US-UTP6-001, US-UTS5-012]:** [[FACT:ut.payslip.items=statement of total amount of each deduction each regular payday; construction licensees full statement]]; lawful offsets itemised on a statement or detachable stub. No general content list (hours, rates, gross) for most employers. Electronic statements must be easily accessible and printable at no cost (stated for pay-card employees, R610-3-22(C)).
- **Retention:** UI wage records [[FACT:ut.records.ui.retention_years=4]] years [US-UTS5-004]; withholding records per Pub 14.

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ut.payslip.items` | [[FACT:ut.payslip.items=statement of total amount of each deduction each regular payday; construction licensees full statement]] |  | from 2014-05-13 | US-UTP6-001 | 34-28-3(4)-(5); R610-3-20 itemized |
| `ut.records.ui.retention_years` | [[FACT:ut.records.ui.retention_years=4]] | years | from 2026-01-01 | US-UTS5-004 | withholding records 4 years |

## UT.5 Statutory reporting

- **Withholding (TC-941E, e-file only) [US-UTPIT-003]:** quarterly return and payment by default; monthly payments once withholding reaches [[FACT:ut.report.tc941e.monthly_payment_threshold=1000]] USD a month; annual filing for Schedule H / Form 944 filers. Federal semiweekly rules do not apply (R865-9I-17).
- **Annual reconciliation:** [[FACT:ut.report.annual_reconciliation.due=Jan 31 with all W-2s/1099s (electronic)]]; required even with zero activity.
- **State W-2 [US-UTS5-014, US-UTS5-015]:** [[FACT:ut.report.w2.format=EFW2 with RS record required; lowercase .txt; fixed-length at 250+ forms]]; FEIN and the Utah withholding account number on each form.
- **Quarterly UI report [US-UTS5-004]:** online only, due [[FACT:ut.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]]; zero reports required; domestic employers may elect annual filing.
- **New hire [US-UTS5-003]:** within [[FACT:ut.newhire.report_days=20]] days of the first day of work, new hires and rehires, to the DWS New Hire Registry.
- **Powers of attorney:** TC-737 and DWS UI POA [US-UTP6-002, US-UTP6-003].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ut.report.w2.format` | [[FACT:ut.report.w2.format=EFW2 with RS record required; lowercase .txt; fixed-length at 250+ forms]] |  | from 2026-01-01 | US-UTS5-014 | TI-03 Rev. 12/24 |
| `ut.report.ui.quarterly_due` | [[FACT:ut.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] |  | from 2026-01-01 | US-UTS5-004 | online only; zero reports |
| `ut.newhire.report_days` | [[FACT:ut.newhire.report_days=20]] | days | from 2026-01-01 | US-UTS5-003 |  |
| `ut.report.tc941e.monthly_payment_threshold` | [[FACT:ut.report.tc941e.monthly_payment_threshold=1000]] | USD | from 2026-01-01 | US-UTPIT-003 | monthly payments at >=1,000/month; quarterly returns Apr 30/Jul 31/Oct 31/Jan 31; e-file only |
| `ut.report.annual_reconciliation.due` | [[FACT:ut.report.annual_reconciliation.due=Jan 31 with all W-2s/1099s (electronic)]] |  | from 2026-01-01 | US-UTPIT-003 |  |

## UT.6 Leave

- **No private-sector paid sick leave statute** (exists: [[FACT:ut.leave.sick.state_statute.exists=False]]); vacation, holiday, sick leave, PTO, severance and bonuses are recoverable wages only if due under an agreement or policy (R610-3-4(B)(1)) [US-UTS5-012]. No PFML. Jury and voting leave not checked.

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ut.leave.sick.state_statute.exists` | [[FACT:ut.leave.sick.state_statute.exists=False]] |  | from 2012-04-16 | US-UTS5-012 | negative finding |

## UT.7 Termination and final pay

- **Discharge (34-28-5) [US-UTS5-002]:** wages due immediately and paid within [[FACT:ut.term.final_pay.discharge.hours=24]] hours (mail, direct deposit or hand delivery within the deadline); penalty wages continue for a limited period after a written demand.
- **Resignation:** [[FACT:ut.term.final_pay.resignation=next regular payday]].
- **Accrued vacation:** [[FACT:ut.term.vacation.payout=only if due under agreement or policy]] [US-UTS5-012]. No state separation-notice form or WARN law found.

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ut.term.final_pay.discharge.hours` | [[FACT:ut.term.final_pay.discharge.hours=24]] | hours | from 2018-05-08 | US-UTS5-002 | 34-28-5; penalty up to 60 days after written demand |
| `ut.term.final_pay.resignation` | [[FACT:ut.term.final_pay.resignation=next regular payday]] |  | from 2018-05-08 | US-UTS5-002 |  |
| `ut.term.vacation.payout` | [[FACT:ut.term.vacation.payout=only if due under agreement or policy]] |  | from 2012-04-16 | US-UTS5-012 | R610-3-4(B)(1) |

## UT.8 Benefits in kind and taxable wages

- **Withholding conformity:** Utah taxable wages are wages subject to federal withholding, so federal exclusions flow through to Utah withholding [US-UTPIT-003, US-UTS5-013].
- **UI departs:** employee retirement deferrals and in-kind pay are UI wages (Section 3).

## UT.9 Deductions and garnishments

- **Authorisation (R610-3-18) [US-UTS5-012]:** lawful deductions listed, with written authorisation for benefits, dues and financial-institution deductions; no deduction where wages were paid late.
- **Garnishment:** valid garnishments in proper amounts are honoured; a state variance from the CCPA was not read, so the CCPA limits apply by default (Annex FED). Child support via ORS (e-IWO, EFT) [US-UTS5-016]; fee and timing open (below).

**Open research points**

- Not configured in this release [[GAP:RQ-349]]: State garnishment limits vs CCPA and ORS IWO fee/timing not read.

## UT.10 Collective agreements and prevailing wage

- **No state prevailing-wage law** (exists: [[FACT:ut.prevailing_wage.exists=False]]): repealed in 1981 [US-UTP51-001]. Federal Davis-Bacon only.

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `ut.prevailing_wage.exists` | [[FACT:ut.prevailing_wage.exists=False]] |  | from 2023-01-01 | US-UTP51-001 | repealed 1981 |

## UT.11 Indexation

- **Minimum wage:** not indexed, capped at the federal rate [US-UTS5-010].
- **SUI wage base:** recomputed every year and published by DWS by mid-November [US-UTS5-006]; the statutory formula was not read, so no derivation is possible; 2027 open (below).
- **Income-tax schedules:** revised with the law (Pub 14); the rate is statutory.

## UT.12 Payroll data protection and records

- **W-2** must carry the full SSN (R865-9I-16(A)(5)). No Utah SSN-truncation rule for pay statements found (open point below).

**Open research points**

- Not configured in this release [[GAP:RQ-350]]: SSN truncation on pay statements (13-45) not read.

## UT.13 Live legal change

- **Rate cut retroactive to 2026-01-01** (Ch. 250, 2026) [US-UTS5-001].
- **Pub 14 Rev. 04/26 schedules:** effective date unknown (blocking open point) [US-UTPIT-003].
- **SUI 2027:** rates and base due mid-November 2026 [US-UTS5-006]. Rules R610-1 and R610-3 continued unchanged on 2026-01-08.

## UT.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## UT.15 Special populations

| Population | Utah rule | Register id |
|---|---|---|
| Domestic / household | Utah withholding only by agreement; annual filing with Schedule H; UI annual filing election | US-UTPIT-003, US-UTS5-013, US-UTS5-004 |
| Agricultural | Minimum-wage exemptions (34-40-104) and UI coverage not read | - |
| Minors | Initial-period minor wage per Section 1 | US-UTS5-011 |
| Tipped | Cash wage per Section 1; credit-card fee deduction allowed; pooling among tipped staff; notice at hire | US-UTS5-011, US-UTS5-008 |
| Clergy / religious | No Utah withholding where federal withholding does not apply | US-UTS5-013 |
| Students | No state rule beyond federal for withholding; UI exemption not read | US-UTS5-013 |
| Nonresident aliens | Utah wages = federal withholding wages; no separate rule | US-UTS5-013, US-UTPIT-003 |
| Statutory employees | Utah withholding only where federal withholding applies | US-UTS5-013 |
| Government employees | Minimum wage covers private and public employees (34-40-103(2)(a)) | US-UTS5-010 |
| Interstate transport / military spouses | Exempt from Utah withholding (federal W-4 box 4c notes) | US-UTPIT-003 |
| Nonresident short-term workers | Day-count safe harbour (Section 2) | US-UTP51-002 |

## UT.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## UT.S Sources

Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file. Authorities:

- Salt Lake City Corporation (municipal government): US-UTR3-002
- US Department of Labor, Wage and Hour Division: US-UTP51-001, US-UTS5-007
- Utah Department of Workforce Services: US-UTP52-005, US-UTS5-004, US-UTS5-005, US-UTSUI-001
- Utah Department of Workforce Services (Unemployment Insurance and New Hire Reporting): US-UTS5-003
- Utah Labor Commission (Division of Antidiscrimination and Labor) via Utah Office of Administrative Rules (adminrules.utah.gov): US-UTS5-011
- Utah Labor Commission via adminrules.utah.gov: US-UTS5-012
- Utah State Legislature (le.utah.gov): US-UTP6-001, US-UTS5-001, US-UTS5-002
- Utah State Tax Commission: US-UTB5-003, US-UTPIT-003, US-UTS5-014
- Utah State Tax Commission via adminrules.utah.gov: US-UTS5-013

## @labour
- **Minimum wage [US-UTS5-011, US-UTS5-010]:** {{ut.minwage.hourly}} USD per hour, unchanged since 2009-07-24; Utah Code 34-40-103(2)(b) bars the Labor Commission from setting a rate above the federal minimum. No 2027 change. No local rate can exceed it.
- **Minors:** at least {{ut.labour.minwage.minor_first_90_days.hourly}} USD per hour for an initial period with an employer, then the full minimum (R610-1-3(B)) [US-UTS5-011].
- **Tipped employees [US-UTS5-011, US-UTS5-008]:** cash wage {{ut.minwage.tipped.cash_wage}} USD per hour; written notice at hire; pooling only among tipped staff.
- **Overtime:** {{ut.labour.overtime.state_rule}} [US-UTS5-007]. Hours worked include on-call time on the premises, meetings, training and rest breaks; fully relieved meal periods are excluded (R610-1-2(B)).
- **Pay frequency (34-28-3(1)) [US-UTP6-001, US-UTS5-009]:** {{ut.pay_frequency.rule}}.
- **Pay cards (R610-3-22) [US-UTS5-012]:** allowed only with {{ut.labour.paycard.conditions}}. Direct-deposit consent rule: open point below.

## @income_tax
- **Rate:** flat {{ut.pit.rate.flat}} % of state taxable income from 2026-01-01 (Utah Code 59-10-104, Ch. 250 of 2026) [US-UTS5-001].
- **Withholding method [US-UTPIT-003, US-UTS5-013]:** {{ut.wh.method}}. Certificate: {{ut.wh.certificate}}; Utah taxable wages are the wages subject to federal withholding (IRC 3401(a)).

| Parameter (annual) | Single (also head of household) | Married | Register id |
|---|---|---|---|
| Base allowance | {{ut.pit.base_allowance.single.annual}} USD | {{ut.pit.base_allowance.married.annual}} USD | US-UTPIT-003 |
| Phase-out threshold | {{ut.pit.phaseout_threshold.single.annual}} USD | {{ut.pit.phaseout_threshold.married.annual}} USD | US-UTPIT-003 |
| Phase-out rate | {{ut.pit.phaseout.rate}} % | same | US-UTPIT-003 |

  Per-period parameters are the annual values divided by the number of periods (Pub 14 prints them). Rounding: {{ut.pit.rounding}}.
- **Effective date of these schedules: blocking open point.** Pub 14 Rev. 04/26 does not state it; a mid-year change is possible. Do not apply these parameters to pay periods before the effective date is established (open point below).
- **Oracle (Pub 14 worked examples, all reproduced):** example 1 {{ut.pit.oracle.example_1.withholding}} USD; example 2 {{ut.pit.oracle.example_2.withholding}} USD; example 3 {{ut.pit.oracle.example_3.withholding}} USD; example 4 {{ut.pit.oracle.example_4.withholding}} USD; example 5 {{ut.pit.oracle.example_5.withholding}} USD; example 6 {{ut.pit.oracle.example_6.withholding}} USD. Recomputation in Module 12.
- **Supplemental wages:** no Utah flat rate published; supplemental pay runs through the regular schedules (open point below).
- **Exempt certificate:** an employee who filed a federal exempt W-4 is not withheld (R865-9I-15).
- **Nonresidents and multistate (R865-9I-14(A)-(C)) [US-UTS5-013, US-UTP51-002]:** nonresidents are withheld on services performed in Utah; residents on all wages, reduced by another state's required withholding. Safe harbour: no Utah withholding for a nonresident with no other Utah income who works {{ut.pit.nonresident.days_safe_harbour}} days or less in Utah and lives in a no-tax or similarly excluding state (not for athletes, entertainers, real-property laborers or key employees). Interstate transportation employees and military spouses are exempt (notes in federal W-4 box 4c). Reciprocity: {{ut.reciprocity.states}}.
- **Local income tax:** none (exists: {{ut.local_wage_tax.exists}}) [US-UTR3-002].
- **Resident and nonresident matrix.**

| Income type | Utah resident | Nonresident |
|---|---|---|
| Regular salary | Pub 14 formula on all wages, less other states' required withholding | Pub 14 formula on Utah-allocable wages, subject to the safe harbour |
| Bonus / supplemental | Through the regular schedules | Same, Utah share |
| Severance, equity, benefits in kind | Follow federal withholding wages | Utah-allocable share |
| Interstate transportation / military spouse | Resident-state rules | Exempt from Utah withholding |

## @social
- **Unemployment insurance (DWS) [US-UTSUI-001, US-UTS5-005].** 2026 taxable wage base {{ut.sui.wage_base}} USD. Overall rate = benefit ratio times the reserve factor ({{ut.ui.reserve_factor}} in 2026) plus the social cost ({{ut.ui.social_cost.rate}} %); range {{ut.sui.employer.rate.min}} % to {{ut.sui.employer.rate.max}} %; delinquency surcharge {{ut.ui.delinquency_surcharge.rate}} % if prior-year contributions are unpaid. New employers take the industry's average benefit ratio (no single rate); new out-of-state contractors take the maximum.
- **UI wages include employee retirement deferrals:** {{ut.sui.wages.401k_included}} [US-UTS5-004]; also meals, lodging, in-kind pay and tips. SUI wages differ from federal taxable wages.
- **Employee contribution:** {{ut.sui.employee.rate}} % [US-UTP52-005]. **SDI, TDI, PFML:** none (exists: {{ut.sdi_pfml.exists}}) [US-UTB5-003]. Other-state wage credit toward the base: open point below.

## @payslip
- **Content (34-28-3(4); R610-3-20) [US-UTP6-001, US-UTS5-012]:** {{ut.payslip.items}}; lawful offsets itemised on a statement or detachable stub. No general content list (hours, rates, gross) for most employers. Electronic statements must be easily accessible and printable at no cost (stated for pay-card employees, R610-3-22(C)).
- **Retention:** UI wage records {{ut.records.ui.retention_years}} years [US-UTS5-004]; withholding records per Pub 14.

## @reporting
- **Withholding (TC-941E, e-file only) [US-UTPIT-003]:** quarterly return and payment by default; monthly payments once withholding reaches {{ut.report.tc941e.monthly_payment_threshold}} USD a month; annual filing for Schedule H / Form 944 filers. Federal semiweekly rules do not apply (R865-9I-17).
- **Annual reconciliation:** {{ut.report.annual_reconciliation.due}}; required even with zero activity.
- **State W-2 [US-UTS5-014, US-UTS5-015]:** {{ut.report.w2.format}}; FEIN and the Utah withholding account number on each form.
- **Quarterly UI report [US-UTS5-004]:** online only, due {{ut.report.ui.quarterly_due}}; zero reports required; domestic employers may elect annual filing.
- **New hire [US-UTS5-003]:** within {{ut.newhire.report_days}} days of the first day of work, new hires and rehires, to the DWS New Hire Registry.
- **Powers of attorney:** TC-737 and DWS UI POA [US-UTP6-002, US-UTP6-003].

## @leave
- **No private-sector paid sick leave statute** (exists: {{ut.leave.sick.state_statute.exists}}); vacation, holiday, sick leave, PTO, severance and bonuses are recoverable wages only if due under an agreement or policy (R610-3-4(B)(1)) [US-UTS5-012]. No PFML. Jury and voting leave not checked.

## @termination
- **Discharge (34-28-5) [US-UTS5-002]:** wages due immediately and paid within {{ut.term.final_pay.discharge.hours}} hours (mail, direct deposit or hand delivery within the deadline); penalty wages continue for a limited period after a written demand.
- **Resignation:** {{ut.term.final_pay.resignation}}.
- **Accrued vacation:** {{ut.term.vacation.payout}} [US-UTS5-012]. No state separation-notice form or WARN law found.

## @bik
- **Withholding conformity:** Utah taxable wages are wages subject to federal withholding, so federal exclusions flow through to Utah withholding [US-UTPIT-003, US-UTS5-013].
- **UI departs:** employee retirement deferrals and in-kind pay are UI wages (Section 3).

## @deductions
- **Authorisation (R610-3-18) [US-UTS5-012]:** lawful deductions listed, with written authorisation for benefits, dues and financial-institution deductions; no deduction where wages were paid late.
- **Garnishment:** valid garnishments in proper amounts are honoured; a state variance from the CCPA was not read, so the CCPA limits apply by default (Annex FED). Child support via ORS (e-IWO, EFT) [US-UTS5-016]; fee and timing open (below).

## @cba
- **No state prevailing-wage law** (exists: {{ut.prevailing_wage.exists}}): repealed in 1981 [US-UTP51-001]. Federal Davis-Bacon only.

## @indexation
- **Minimum wage:** not indexed, capped at the federal rate [US-UTS5-010].
- **SUI wage base:** recomputed every year and published by DWS by mid-November [US-UTS5-006]; the statutory formula was not read, so no derivation is possible; 2027 open (below).
- **Income-tax schedules:** revised with the law (Pub 14); the rate is statutory.

## @data
- **W-2** must carry the full SSN (R865-9I-16(A)(5)). No Utah SSN-truncation rule for pay statements found (open point below).

## @live
- **Rate cut retroactive to 2026-01-01** (Ch. 250, 2026) [US-UTS5-001].
- **Pub 14 Rev. 04/26 schedules:** effective date unknown (blocking open point) [US-UTPIT-003].
- **SUI 2027:** rates and base due mid-November 2026 [US-UTS5-006]. Rules R610-1 and R610-3 continued unchanged on 2026-01-08.

## @special
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

## @gaps
- ut.pit.schedule.effective_date :: Pub 14 Rev. 04/26 does not state from which pay period its base allowances and thresholds apply; a tier-B lead points to a mid-year 2026 change from lower earlier allowances. Calculations for pay periods before the effective date cannot be fixed. :: Tax Commission notice or Pub 14 PDF cover (US IP).

# Annex IL: Illinois


**Layer classification (T3).** T3: separate state withholding calculation and state return; no local layer, or a local layer piggybacked on the state return. Source: build manifest tier census, local income tax domain.

**Summary.** State minimum wage 15.00 (not indexed), Chicago [[FACT:il.local_minwage.chicago.hourly=17.05]] and suburban Cook [[FACT:il.local_minwage.cook.hourly=15.40]] from 2026-07-01 (both indexed); weekly overtime. Flat [[FACT:il.pit.rate.flat=4.95]]% withholding on wages less IL-W-4 exemptions ([[FACT:il.wh.exemption.line1=2,925]] + 1,000); no supplemental rate; reciprocity IA/KY/MI/WI; 30-day nonresident rule; no local tax. UI base [[FACT:il.sui.wage_base=14,250]], new [[FACT:il.sui.new_employer.rate=3.350]]%, no employee share; no SDI/PFML. PLAWA paid leave statewide (not in Chicago/Cook). Pay stub retention 3 years, copy rules. IL-941 quarterly, no annual reconciliation; monthly UI wage report for 25+. Oracle: IL-700-T examples [[FACT:il.oracle.il700t.example1.withholding=8.38]] / [[FACT:il.oracle.weekly_800.withholding=32.13]].

Each parameter row gives its key, the period in force and its legal basis: the legal-basis register row, the authority, the source tier and how the value was verified.

## IL.1 Employment and labour code

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `il.local_minwage.chicago.hourly` | [[FACT:il.local_minwage.chicago.hourly=17.05]] USD | 2026-07-01 to 2027-06-30 | US-ILS5-008 (City of Chicago, Department of Business Affairs and Consumer Protection; A.2, quoted from authority page, confidence high) | Employers 4+; tipped [[FACT:il.local_minwage.chicago.tipped=12.96]] ([[FACT:il.local_minwage.chicago.hourly=17.05]] x 0.76 = 12.958); City contracts 18.50; indexed July 1 by CPI, subject to a cap. |
| `il.local_minwage.chicago.tipped` | [[FACT:il.local_minwage.chicago.tipped=12.96]] USD | 2026-07-01 to 2027-06-30 | US-ILS5-008 (City of Chicago, Department of Business Affairs and Consumer Protection; A.2, quoted from authority page, confidence high) |  |
| `il.local_minwage.cook.hourly` | [[FACT:il.local_minwage.cook.hourly=15.40]] USD | 2026-07-01 to open | US-ILS5-009 (Cook County Commission on Human Rights; A.2, derived arithmetically, confidence high) | Suburban Cook County, employees over 18 with >= 2 h/week in the County; Chicago and opted-out municipalities excluded; tipped [[FACT:il.local_minwage.cook.tipped=9.25]]; the overtime and tipped overtime rates follow from these two rates. |
| `il.local_minwage.cook.tipped` | [[FACT:il.local_minwage.cook.tipped=9.25]] USD | 2026-07-01 to open | US-ILS5-009 (Cook County Commission on Human Rights; A.2, derived arithmetically, confidence high) | Derivation recorded in register row US-ILS5-009. |
| `il.minwage.coverage.min_employees` | [[FACT:il.minwage.coverage.min_employees=4]] employees | 2026-01-01 to open | US-ILS5-026 (Illinois General Assembly; A.1, direct artifact inspection, confidence high) | 105/3: fewer than 4 outside the law except domestic workers; also small farms, outside salesmen, religious organisation members, own-college students, etc. |
| `il.minwage.hourly` | [[FACT:il.minwage.hourly=15]] USD | 2025-01-01 to open | US-ILS5-001 (Illinois General Assembly; A.1, second independent authority, confidence high) | 820 ILCS 105/4, adults 18+; no later step, no indexation [US-ILS5-002]. |
| `il.minwage.new_hire_reduction` | [[FACT:il.minwage.new_hire_reduction=0.50]] USD | 2025-01-01 to open | US-ILS5-001 (Illinois General Assembly; A.1, second independent authority, confidence high) | First 90 consecutive days, not day/temporary laborers. |
| `il.minwage.tipped.cash_wage` | [[FACT:il.minwage.tipped.cash_wage=9]] USD | 2025-01-01 to open | US-ILS5-002 (Illinois Department of Labor; A.2, second independent authority, confidence high) | Tip credit up to 40%. |
| `il.minwage.youth.hourly` | [[FACT:il.minwage.youth.hourly=13]] USD | 2025-01-01 to open | US-ILS5-001 (Illinois General Assembly; A.1, second independent authority, confidence high) | Under 18 working <= 650 h/calendar year. |
| `il.overtime.weekly_threshold_hours` | [[FACT:il.overtime.weekly_threshold_hours=40]] hours | 2026-01-01 to open | US-ILS5-001 (Illinois General Assembly; A.1, second independent authority, confidence high) | 105/4a; no daily OT; exemptions 4a(2). |
| `il.pay_frequency.rule` | [[FACT:il.pay_frequency.rule=at least semi-monthly, paid within 13 days after period end; EAP and commissions monthly (115/3)]] | 2026-01-01 to open | US-ILS5-003 (Illinois Department of Labor; A.3, quoted from authority page, confidence high) |  |
| `il.payment.method` | [[FACT:il.payment.method=direct deposit must be voluntary; cash with signed receipt; payroll card voluntary with written fee disclosure, revocable; card/DD offerors must also offer cash or check (115/4, 115/14.5)]] | 2026-01-01 to open | US-ILS5-005 (Illinois Department of Labor; A.3, quoted from authority page, confidence high) | Payroll card rules [US-ILS5-007]. |

## IL.2 Income tax withholding

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `il.pit.rate.flat` | [[FACT:il.pit.rate.flat=4.95]] % | 2026-01-01 to open | US-ILR3-001 (Illinois Department of Revenue; A.2, quoted from authority page, confidence high) | IL-700-T R-12/25 re-verified byte-identical 2026-11-02; 35 ILCS 5/201 not read this pass. |
| `il.wh.certificate` | [[FACT:il.wh.certificate=IL-W-4 R-07/23 current; no exemptions if AGI > 500k joint / 250k other; none on file = no exemptions; changes effective next quarter date at least 30 days after filing]] | 2023-07-01 to open | US-ILS5-010 (Illinois Department of Revenue; A.2, direct artifact inspection, confidence high) |  |
| `il.wh.exemption.line1` | [[FACT:il.wh.exemption.line1=2,925]] USD | 2026-01-01 to 2026-12-31 | US-ILR3-001 (Illinois Department of Revenue; A.2, quoted from authority page, confidence high) | Indexed by IDOR. |
| `il.wh.exemption.line2` | [[FACT:il.wh.exemption.line2=1,000]] USD | 2026-01-01 to 2026-12-31 | US-ILR3-001 (Illinois Department of Revenue; A.2, quoted from authority page, confidence high) |  |
| `il.wh.method` | [[FACT:il.wh.method=.0495 x (wages - exemptions/periods) + IL-W-4 Line 3; exemptions = Line 1 x 2,925 + Line 2 x 1,000 per year]] | 2026-01-01 to 2026-12-31 | US-ILR3-001 (Illinois Department of Revenue; A.2, quoted from authority page, confidence high) | No rounding rule (tables in cents); no separate supplemental rate - bonus/OT/commission are wages [US-ILR3-002]. |

Not configured in this release [[GAP:RQ-198]]: 35 ILCS 5/201(b)(5.4) not read; no 2027 change confirmed.

Not configured in this release [[GAP:RQ-199]]: No IDOR decoupling statement (HSA, s.125) read.

## IL.2b Non-resident regime and reciprocity

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `il.nonres.days_threshold` | [[FACT:il.nonres.days_threshold=30]] days | 2026-01-01 to open | US-ILS5-014 (Illinois Department of Revenue; A.2, direct artifact inspection, confidence high) | No withholding for nonresident with fewer than 31 days of non-localized IL service; IL-W-6 day certificate when > 30 days expected; carrier rules (air > 50% flight miles). IL resident working only in a withholding state: no IL withholding. |
| `il.reciprocity.states` | [[FACT:il.reciprocity.states=IA, KY, MI, WI]] | 2026-01-01 to open | US-ILS5-014 (Illinois Department of Revenue; A.2, direct artifact inspection, confidence high) | IL-W-5-NR; military spouses excluded. |

## IL.2c Local wage taxes

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `il.local_wage_tax.exists` | [[FACT:il.local_wage_tax.exists=False]] | 2026-01-01 to open | US-ILP52-001 (Illinois Department of Revenue; A.2, quoted from authority page, confidence high) | None administered by IDOR. |

## IL.3 Social insurance: unemployment, disability, paid leave and payroll levies

Levies: Secure Choice Roth IRA payroll deduction [US-ILP52-002]; no other levy.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `il.sdi_pfml.exists` | [[FACT:il.sdi_pfml.exists=False]] | 2026-01-01 to open | US-ILP52-003 (Illinois Department of Labor; A.2, quoted from authority page, confidence high) | PLAWA is an employer-provided benefit, not a premium. |
| `il.sui.employee.rate` | [[FACT:il.sui.employee.rate=0]] % | 2026-01-01 to open | US-ILR3C-001 (Illinois General Assembly; A.1, quoted from authority page, confidence high) | 820 ILCS 405/1400: UI contributions shall not be deducted, in whole or in part, from employees' wages. |
| `il.sui.employer.rate.max` | [[FACT:il.sui.employer.rate.max=7.05]] % | 2026-01-01 to 2026-12-31 | US-ILS5-015 (Illinois Department of Employment Security; A.2, quoted from authority page, confidence high) |  |
| `il.sui.employer.rate.min` | [[FACT:il.sui.employer.rate.min=0.75]] % | 2026-01-01 to 2026-12-31 | US-ILS5-015 (Illinois Department of Employment Security; A.2, quoted from authority page, confidence high) | Range [[FACT:il.sui.employer.rate.min=0.750]]%-[[FACT:il.sui.employer.rate.max=7.050]]% incl. fund builder [[FACT:il.sui.fund_builder.rate=0.550]]%; small-employer option and state experience factor apply. |
| `il.sui.fund_builder.rate` | [[FACT:il.sui.fund_builder.rate=0.55]] % | 2026-01-01 to 2026-12-31 | US-ILS5-015 (Illinois Department of Employment Security; A.2, quoted from authority page, confidence high) |  |
| `il.sui.new_employer.rate` | [[FACT:il.sui.new_employer.rate=3.35]] % | 2026-01-01 to 2026-12-31 | US-ILS5-015 (Illinois Department of Employment Security; A.2, quoted from authority page, confidence high) | Administrative Support & Waste Management 3.450%. |
| `il.sui.wage_base` | [[FACT:il.sui.wage_base=14,250]] USD | 2026-01-01 to 2026-12-31 | US-ILS5-015 (Illinois Department of Employment Security; A.2, quoted from authority page, confidence high) | same values as US-IL-002; 820 ILCS 405/235 formula not read; 2027 expected Dec 2026. |

Not configured in this release [[GAP:RQ-200]]: 2027 wage base unpublished; 405/235 formula not read.

## IL.4 Pay statement

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `il.payslip.copy_response_days` | [[FACT:il.payslip.copy_response_days=21]] days | 2025-01-01 to open | US-ILS5-024 (Illinois General Assembly; A.1, direct artifact inspection, confidence high) |  |
| `il.payslip.rules` | [[FACT:il.payslip.rules=pay stub each pay period; itemized deductions; payroll-card payees also hours, rate, deductions; stubs kept >= 3 years; copies within 21 days on request (max twice/12 months; former employees 1 year after separation); offer prior-year stubs if electronic access ends (115/10, P.A. 103-953)]] | 2025-01-01 to open | US-ILS5-024 (Illinois General Assembly; A.1, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-201]]: 56 Ill. Adm. Code 300.600 content items not read.

## IL.5 Statutory reporting

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `il.newhire.report_days` | [[FACT:il.newhire.report_days=20]] days | 2026-01-01 to open | US-ILS5-018 (Illinois Department of Employment Security; A.2, quoted from authority page, confidence high) | From first day on payroll; rehires and independent contractors. |
| `il.report.sui.monthly.employer_threshold` | [[FACT:il.report.sui.monthly.employer_threshold=25]] employees | 2026-01-01 to open | US-ILS5-017 (Illinois Department of Employment Security; A.2, quoted from authority page, confidence high) | Monthly wage report for months 1 and 2 of each quarter: name, SSN, wages; MyTax CSV only (P.A. 97-0689). |
| `il.report.sui.quarterly` | [[FACT:il.report.sui.quarterly=UI-3/40 wage report + contributions due Apr 30 / Jul 31 / Oct 31 / Jan 31]] | 2026-01-01 to open | US-ILS5-016 (Illinois Department of Employment Security; A.2, quoted from authority page, confidence high) |  |
| `il.report.w2` | [[FACT:il.report.w2=electronic only: MyTax (manual, CSV, EFW2 under IDR-996) or bulk EFW2 with ETIN (IDR-986); due Jan 31 (2026 W-2s by 2027-02-01); 1099/W-2G bulk via IRIS (IDR-987) from 2026-09-18]] | 2026-09-18 to open | US-ILS5-013 (Illinois Department of Revenue; A.2, quoted from authority page, confidence high) |  |
| `il.report.wh.deposit` | [[FACT:il.report.wh.deposit=monthly (15th) when look-back <= 12,000; semi-weekly (federal Wed/Fri, electronic) when > 12,000; IL-501]] | 2026-01-01 to open | US-ILS5-011 (Illinois Department of Revenue; A.2, quoted from authority page, confidence high) |  |
| `il.report.wh.il941` | [[FACT:il.report.wh.il941=IL-941 quarterly, electronic, due last day of month after quarter (2026: 04-30, 07-31, 11-02, 2027-02-01); no annual reconciliation]] | 2026-01-01 to open | US-ILS5-011 (Illinois Department of Revenue; A.2, quoted from authority page, confidence high) | Dates [US-ILS5-012]. |
| `il.report.wh.semiweekly_threshold` | [[FACT:il.report.wh.semiweekly_threshold=12,000]] USD | 2026-01-01 to open | US-ILS5-011 (Illinois Department of Revenue; A.2, quoted from authority page, confidence high) |  |

## IL.6 Leave

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `il.leave.chicago.accrual` | [[FACT:il.leave.chicago.accrual=1 h paid leave AND 1 h paid sick leave per 35 h worked from day 1 for anyone with >= 80 h in 120 days; notices with first paycheck and around July 1]] | 2024-07-01 to open | US-ILS5-020 (City of Chicago, Department of Business Affairs and Consumer Protection; A.2, quoted from authority page, confidence medium) | [partial row] [partial row] caps, carryover and payout unread. |
| `il.leave.plawa.accrual` | [[FACT:il.leave.plawa.accrual=1 h per 40 h worked up to 40 h per 12 months (front-load allowed); use after 90 days; exempt deemed 40 h/week; no separation payout unless in a vacation/PTO bank; tipped/commissioned paid at least full MW; not in Chicago/Cook]] | 2024-01-01 to open | US-ILS5-019 (Illinois Department of Labor; A.3, quoted from authority page, confidence medium) |  |
| `il.leave.plawa.cap_hours` | [[FACT:il.leave.plawa.cap_hours=40]] hours | 2024-01-01 to open | US-ILS5-019 (Illinois Department of Labor; A.3, quoted from authority page, confidence medium) |  |

Not yet published [[GAP:RQ-202]]: Chicago Paid Leave caps, carryover and separation payout by employer size not read (partial row).

Not configured in this release [[GAP:RQ-578]]: The Cook County Paid Leave Substantive and Procedural Rules approved 2025-04-10 are listed on the CCHR page but not read; they may refine the FAQ (corrected 04/2024) details written in this annex.

## IL.7 Termination and final pay

IDES lists "Employee Separation Information" as an employer obligation [US-ILS5-018]; the notice/form to the employee not identified.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `il.final_pay.rule` | [[FACT:il.final_pay.rule=in full at separation if possible, no later than next regularly scheduled payday (discharge or resignation); mailed on written request (115/5)]] | 2026-01-01 to open | US-ILS5-023 (Illinois General Assembly; A.1, second independent authority, confidence high) |  |
| `il.final_pay.vacation_payout` | [[FACT:il.final_pay.vacation_payout=True]] | 2026-01-01 to open | US-ILS5-004 (Illinois Department of Labor; A.3, quoted from authority page, confidence high) | Earned vacation paid at final rate, no forfeiture (CBA exception); use-it-or-lose-it allowed with notice (56 IAC 300.520). No statutory severance. |

Not configured in this release [[GAP:RQ-204]]: Whether Illinois requires a separation notice to the employee not identified.

## IL.8 Benefits in kind and taxable wages

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `il.wh.wages.conformity` | [[FACT:il.wh.wages.conformity=IL withholding follows federal (wages subject to federal withholding); federal exclusions follow; no departure found (not proven)]] | 2026-01-01 to open | US-ILR3-002 (Illinois Department of Revenue; A.2, quoted from authority page, confidence medium) |  |

## IL.9 Deductions and garnishments

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `il.deductions.rule` | [[FACT:il.deductions.rule=only if required by law, for employee benefit, or wage assignment/order or express written consent at time of deduction; cash advance repayment max 15% per paycheck]] | 2026-01-01 to open | US-ILS5-006 (Illinois Department of Labor; A.3, quoted from authority page, confidence medium) |  |
| `il.garn.child_support.employer_fee_monthly` | [[FACT:il.garn.child_support.employer_fee_monthly=5]] USD | 2026-01-01 to open | US-ILS5-021 (Illinois Department of Healthcare and Family Services; A.2, quoted from authority page, confidence high) | HFS 3683; remit 1-7 business days after payday; up to 50% of disposable; multiple orders pro rata. |
| `il.garn.creditor.max_percent_gross` | [[FACT:il.garn.creditor.max_percent_gross=15]] % | 2026-01-01 to open | US-ILS5-022 (Illinois General Assembly; A.1, derived arithmetically, confidence high) | 735 ILCS 5/12-803: lesser of [[FACT:il.garn.creditor.max_percent_gross=15]]% of GROSS or disposable - 45 x greater of federal/IL MW. |
| `il.garn.creditor.weekly_floor` | [[FACT:il.garn.creditor.weekly_floor=675]] USD | 2025-01-01 to open | US-ILS5-022 (Illinois General Assembly; A.1, derived arithmetically, confidence high) | 45 x 15.00. |

## IL.10 Collective agreements and prevailing wage

Prevailing Wage Act 820 ILCS 130: IDOL county rates, certified payroll portal [US-ILP52-004]. CBA can override vacation payout (115/5).

## IL.11 Indexation

State MW not indexed; Chicago July 1 CPI (capped); Cook July 1 CPI (suspended above a County unemployment threshold); UI base yearly; PIT exemption indexed by IDOR; garnishment floor 45 x MW. Chicago CPI derivation impossible (2025 rate not registered).

## IL.12 Payroll data protection and records

No SSN truncation rule found (815 ILCS 505/2RR and 530 not read).

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `il.bipa.retention_max_years` | [[FACT:il.bipa.retention_max_years=3]] years | 2026-01-01 to open | US-ILS5-025 (Illinois General Assembly; A.1, direct artifact inspection, confidence high) | 740 ILCS 14/15: written policy, destroy within 3 years of last interaction; notice + written release before collection (biometric time clocks). |
| `il.records.paystub.retention_years` | [[FACT:il.records.paystub.retention_years=3]] years | 2025-01-01 to open | US-ILS5-024 (Illinois General Assembly; A.1, direct artifact inspection, confidence high) |  |

Not configured in this release [[GAP:RQ-205]]: 815 ILCS 505/2RR and 815 ILCS 530 not read.

## IL.13 Live legal change

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `il.leave.cook.paid_leave.accrual` | [[FACT:il.leave.cook.paid_leave.accrual=1 hour of paid leave per 40 hours worked, usable for any reason; FLSA-exempt employees deemed to work 40 hours a week; front-loading allowed.]] | 2023-12-31 to open | US-ILB5-301 (Cook County Commission on Human Rights; A.3, quoted from authority page, confidence high) |  |
| `il.leave.cook.paid_leave.carryover_cap.min_hours` | [[FACT:il.leave.cook.paid_leave.carryover_cap.min_hours=40]] hours | 2023-12-31 to open | US-ILB5-301 (Cook County Commission on Human Rights; A.3, quoted from authority page, confidence high) | An employer carry-over cap may not be set below 40 hours. |
| `il.leave.cook.paid_leave.in_force` | [[FACT:il.leave.cook.paid_leave.in_force=Cook County Paid Leave Ordinance in force from 2023-12-31 (2025-01-01 for park and school districts); does not apply in the City of Chicago (own ordinance); a prior Earned Sick Leave Ordinance opt-out does not carry over.]] | 2023-12-31 to open | US-ILB5-301 (Cook County Commission on Human Rights; A.3, quoted from authority page, confidence high) |  |
| `il.leave.cook.paid_leave.payout_at_separation` | [[FACT:il.leave.cook.paid_leave.payout_at_separation=Not required, unless the leave is credited to a PTO bank or vacation account; then unused leave is paid within 15 days of separation.]] | 2023-12-31 to open | US-ILB5-301 (Cook County Commission on Human Rights; A.3, quoted from authority page, confidence high) |  |
| `il.live.14c_end` | [[FACT:il.live.14c_end=14(c) sub-minimum licences end 2029-12-31 (enacted)]] | 2029-12-31 to open | US-ILS5-002 (Illinois Department of Labor; A.2, quoted from authority page, confidence high) |  |

Not configured in this release [[GAP:RQ-206]]: One Fair Wage phase-out percentage for 2026 not read ([[FACT:il.local_minwage.chicago.tipped=12.96]] = 76% of [[FACT:il.local_minwage.chicago.hourly=17.05]]).

Not configured in this release [[GAP:RQ-207]]: IDOL/IDOR/IDES newsrooms 2026 not reviewed.

## IL.14 Authority worked examples (oracle values)

Each example is computed from the statutory parameters listed in this annex and checked against the result published by the authority. Amounts round half-up to the cent unless the line states another rule.

**Example IL-2: weekly wages 800.00, IL-W-4 Line 1 = 2, Line 2 = 2 (IL-700-T example).**

| Line | Calculation | Result |
|---|---|---|
| Annual exemptions | 2 x [[FACT:il.wh.exemption.line1=2,925]] + 2 x [[FACT:il.wh.exemption.line2=1,000]] | 7,850.00 |
| Weekly exemption | 7,850.00 / 52, rounded to the cent | 150.96 |
| Taxable wages | 800.00 - 150.96 | 649.04 |
| Withholding | 649.04 x [[FACT:il.pit.rate.flat=4.95]] % = 32.1275, half-up to the cent | [[FACT:il.oracle.weekly_800.withholding=32.13]] |

Computed result = published [[FACT:il.oracle.weekly_800.withholding=32.13]] (match).

**Example IL-1: weekly wages 300.00, IL-W-4 Line 1 = 2, Line 2 = 1 (IL-700-T example 1, automated payroll method; the booklet prints the table-method result).**

| Line | Calculation | Result |
|---|---|---|
| Annual exemptions | 2 x [[FACT:il.wh.exemption.line1=2,925]] + 1 x [[FACT:il.wh.exemption.line2=1,000]] | 6,850.00 |
| Weekly exemption | 6,850.00 / 52, rounded to the cent | 131.73 |
| Taxable wages | 300.00 - 131.73 | 168.27 |
| Withholding | 168.27 x [[FACT:il.pit.rate.flat=4.95]] % = 8.3294, half-up to the cent | 8.33 |

Computed result = published automated-method result [[FACT:il.oracle.il700t.example1.automated_method_result=8.33]] (match). The IL-700-T prints [[FACT:il.oracle.il700t.example1.withholding=8.38]] for the same employee because its example uses the wage-bracket table, whose values are computed at the bracket midpoint; both are correct for their method. A payroll engine using the formula reproduces the automated-method result.

| Parameter (key) | Value | In force | Legal basis | Note |
|---|---|---|---|---|
| `il.oracle.il700t.example1.automated_method_result` | [[FACT:il.oracle.il700t.example1.automated_method_result=8.33]] USD | 2026-01-01 to 2026-12-31 | US-ILR3-001 (Illinois Department of Revenue; A.2, derived arithmetically, confidence high) | (300 - (2 x [[FACT:il.wh.exemption.line1=2,925]] + 1 x 1,000)/52) x [[FACT:il.pit.rate.flat=4.95]]% = 168.27 x [[FACT:il.pit.rate.flat=4.95]]% = [[FACT:il.oracle.il700t.example1.automated_method_result=8.33]] (automated payroll method, IL-700-T p.3). |
| `il.oracle.il700t.example1.withholding` | [[FACT:il.oracle.il700t.example1.withholding=8.38]] USD | 2026-01-01 to 2026-12-31 | US-ILR3-001 (Illinois Department of Revenue; A.2, derived arithmetically, confidence high) | IL-700-T p.3 table-method example: 300 weekly, 2 Line-1 + 1 Line-2 allowances: weekly table 300-302 row, 2 allowances = 9.33, minus 0.95 per Line-2 allowance = [[FACT:il.oracle.il700t.example1.withholding=8.38]]. The table values are computed at the bracket midpoint (301): (301 - 2 x [[FACT:il.wh.exemption.line1=2,925]]/52) x [[FACT:il.pit.rate.flat=4.95]]% = 9.33. The automated payroll method on exactly 300 gives [[FACT:il.oracle.il700t.example1.automated_method_result=8.33]] (il.oracle.il700t.example1.automated_method_result). Both are correct for their method; the 0.05 residual is the table midpoint, not a booklet defect. |
| `il.oracle.weekly_800.withholding` | [[FACT:il.oracle.weekly_800.withholding=32.13]] USD | 2026-01-01 to 2026-12-31 | US-ILR3-001 (Illinois Department of Revenue; A.2, derived arithmetically, confidence high) | 800 weekly, 2 + 2 allowances: 7,850/52 = 150.96; 649.04 x .0495 = [[FACT:il.oracle.weekly_800.withholding=32.13]]. |

## IL.15 Special populations

- Domestic: MW Law even under 4 employees; IL withholding only if federal withheld voluntarily [US-ILS5-026, US-ILR3-002].
- Agricultural: no state OT; small farms (<= 500 man-days/quarter), family, some piece-rate harvesters outside MW [US-ILS5-001, US-ILS5-026].
- Minors: 13.00 under 18 <= 650 h/yr; Cook ordinance not under 18 [US-ILS5-001, US-ILS5-009].
- Tipped: state 9.00; Chicago [[FACT:il.local_minwage.chicago.tipped=12.96]]; Cook [[FACT:il.local_minwage.cook.tipped=9.25]]; PLAWA paid at full MW [US-ILS5-001, US-ILS5-008, US-ILS5-009, US-ILS5-019].
- Clergy: religious organisation members outside MW; ministers no IL withholding [US-ILS5-026, US-ILS5-014].
- Students: own-college students outside MW; part-time college students at own school PLAWA-exempt [US-ILS5-026, US-ILS5-019].
- NRAs / statutory employees: follow federal [US-ILR3-002].
- Government: IWPCA excludes State and federal employees; MW covers governmental bodies; UI reimbursement option [US-ILS5-003, US-ILS5-001, US-ILS5-016].
- Other-state residents: reciprocity IA/KY/MI/WI, 30-day rule, IL-W-6 [US-ILS5-014].

## IL.16 Language

No language requirement [US-ILP9L-001]; payslip English (US-OWN-006).

## IL.S Sources

The legal basis of each value (legal-basis register id, authority, source tier and verification method) is given in the row that carries it.

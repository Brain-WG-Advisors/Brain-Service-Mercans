# Annex AK: Alaska


This annex sets out the Alaska payroll rules for the 2026 build year. Read with Annex FED (the federal layer every employee carries) and Annex MULTI (which routes an employee to this State by work location, residence or UI localization). Every value is shown with its effective dates and its source (list at the end of the annex). Federal values are not repeated here.

Classification: T1. Alaska has no wage income tax; the State layer is UI, labour standards and reporting.

## AK.1 Employment and labour code

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Minimum wage hourly | USD [[FACT:ak.minwage.hourly=13]] | 2025-07-01 to 2026-06-30 |  | S1 |  |
| Minimum wage hourly | USD [[FACT:ak.minwage.hourly=14]] | 2026-07-01 to 2027-06-30 |  | S2 | Confirmed on the DOLWD Wage and Hour page updated 2026-05-01. |
| Minimum wage hourly | USD [[FACT:ak.minwage.hourly=15]] | from 2027-07-01 |  | S1 | Enacted (2024 Ballot Measure 1). From 2028-01-01 indexed to CPI-U Anchorage, rounded up to the next 0.10. |
| Minimum wage tip credit allowed | [[FACT:ak.minwage.tip_credit.allowed=False]] | from 2025-07-01 |  | S1 | AS 23.10.065(a): the full minimum wage is due in cash to tipped employees. |
| Minimum wage school bus driver hourly | USD [[FACT:ak.minwage.school_bus_driver.hourly=28]] | 2026-07-01 to 2027-06-30 |  | S1 | 2x the state minimum wage (AS 23.10.065(b)). |
| Overtime daily threshold hours | [[FACT:ak.overtime.daily_threshold_hours=8]] hours | from 2026-01-01 |  | S1 | AS 23.10.060: 1.5x over [[FACT:ak.overtime.daily_threshold_hours=8]] h/day and over 40 h/week; daily OT hours not double-counted toward 40. Employers with fewer than 4 employees exempt. |
| Overtime weekly threshold hours | [[FACT:ak.overtime.weekly_threshold_hours=40]] hours | from 2026-01-01 |  | S1 |  |
| Overtime premium multiplier | [[FACT:ak.overtime.premium.multiplier=1.5]] ratio | from 2026-01-01 |  | S1 |  |
| Exempt salary weekly min | USD [[FACT:ak.exempt.salary.weekly_min=1,040]] | 2025-07-01 to 2026-06-30 |  | S1 | AS 23.10.055(b): 2 x state minimum wage x 40 h = 2 x 13.00 x 40. |
| Exempt salary weekly min | USD [[FACT:ak.exempt.salary.weekly_min=1,120]] | 2026-07-01 to 2027-06-30 |  | S1 | 2 x 14.00 x 40 (AS 23.10.055(b)). |
| Exempt salary weekly min | USD [[FACT:ak.exempt.salary.weekly_min=1,200]] | from 2027-07-01 |  | S1 | 2 x 15.00 x 40 (AS 23.10.055(b)); enacted rate. |
| Pay frequency rule | [[FACT:ak.pay_frequency.rule=monthly or semi-monthly at the employee's election (AS 23.05.140(a))]] | from 2026-01-01 |  | S1 |  |
| Direct deposit requires voluntary authorisation | [[FACT:ak.direct_deposit.requires_voluntary_authorisation=True]] | from 2026-01-01 |  | S1 | AS 23.10.043: only if the employee voluntarily authorises it, to the bank of the employee's choice. |

Not configured in this release [[GAP:RQ-451]]: Paycard rule: not established from an official source.

## AK.2 Income tax withholding

Alaska levies no individual income tax and no State income-tax withholding ([[FACT:ak.pit.exists=False]]): no State withholding certificate, supplemental rate, withholding return, reciprocity or State W-2 filing. Only the federal layer withholds income tax.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| PIT exists | [[FACT:ak.pit.exists=False]] | from 2026-01-01 |  | S3 | No individual income tax and no state income-tax withholding; no state W-4, no withholding return, no state W-2 filing. |

## AK.2b Non-resident regime and reciprocity

Not applicable: without a State income tax there is no resident or non-resident treatment and no reciprocity; the income-tax matrix is the federal one (Annex FED, FED.2b). For UI, wages a transferred employee was paid by the same employer and reported to another State in the same year count toward the Alaska wage base ([[FACT:multi.sui.other_state_wage_credit.ak=True]]); the quarterly report carries a flag for them.

## AK.2c Local wage taxes

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Local wage tax exists | [[FACT:ak.local_wage_tax.exists=False]] | from 2026-01-01 |  | S4 | No local wage, payroll or income tax; municipal powers are property and sales tax only. |

## AK.3 Social insurance: unemployment, disability, paid leave and payroll levies

UI is funded by an employee contribution, deducted by the employer, and an employer contribution, both on wages up to the annual base. The STEP and TVEP shares are carved out of the employee contribution, not added to it. For 2026 every employer class sits at the floor of the schedule. There is no SDI, TDI, PFML, long-term-care or transit levy ([[FACT:ak.sdi_pfml.exists=False]]). Workers' compensation is an insurer premium outside payroll.

```
ak_ui_ee = min(period_UI_wages, max(0, ak_wage_base - ytd_UI_wages)) x ak_ui_employee_rate
ak_ui_er = min(period_UI_wages, max(0, ak_wage_base - ytd_UI_wages)) x employer_class_rate
```

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| SUI wage base | USD [[FACT:ak.sui.wage_base=54,200]] | 2026-01-01 to 2026-12-31 |  | S5 | Same figure printed on TQ01C (2/26). Mechanism 75% of the AK average annual wage; not re-derived. |
| SUI employee rate | [[FACT:ak.sui.employee.rate=0.5]] % | 2026-01-01 to 2026-12-31 |  | S5 | Employee UI contribution deducted by the employer. Derivation: the 0.27 x ABCR product is below the floor, so the [[FACT:ak.sui.employee.rate=0.5]] % floor applies. |
| SUI employer rate classes 01 20 | [[FACT:ak.sui.employer.rate.classes_01_20=1]] % | 2026-01-01 to 2026-12-31 |  | S5 |  |
| SUI employer rate class 21 | [[FACT:ak.sui.employer.rate.class_21=5.4]] % | 2026-01-01 to 2026-12-31 |  | S5 |  |
| SUI new employer rate | [[FACT:ak.sui.new_employer.rate=1]] % | 2026-01-01 to 2026-12-31 |  | S6 | Every industry; the employee share ([[FACT:ak.sui.employee.rate=0.5]] %) is withheld on top. |
| SUI ABCR | [[FACT:ak.sui.abcr=0.004615]] ratio | 2026-01-01 to 2026-12-31 |  | S7 | ABCR = (131,477,612 / 45,628,865,425) / (10,852,857,547 / 17,381,530,724), DOLWD UI Tax Calculation Cookbook 2026 (updated 2025-12-04). Reproduces every published 2026 rate. |
| STEP rate within employee UI | [[FACT:ak.step.rate_within_employee_ui=0.1]] % | from 2026-01-01 |  | S8 | Collected inside the employee [[FACT:ak.sui.employee.rate=0.5]] % and credited back; net cost nil. No employer STEP tax (SB 217 not enacted). |
| TVEP rate within employee UI | [[FACT:ak.tvep.rate_within_employee_ui=0.25]] % | from 2026-01-01 |  | S9 | Collected inside the employee [[FACT:ak.sui.employee.rate=0.5]] %; net cost nil. |
| SDI PFML exists | [[FACT:ak.sdi_pfml.exists=False]] | from 2026-01-01 |  | S3 | No SDI/TDI/PFML/LTC/transit levy. AFLA covers public employers only and is unpaid. |

Not configured in this release [[GAP:RQ-449]]: SUI wage base derivation: not established from an official source.

Not configured in this release [[GAP:RQ-456]]: SUI wage base next year: not established from an official source.

## AK.4 Pay statement

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Payslip required | [[FACT:ak.payslip.required=True]] | from 2025-09-25 |  | S1 | 8 AAC 15.160(h): written or electronic statement each pay period: rate, gross, net, period dates, FIT and FICA, AK ESA contributions, board/lodging, advances, straight-time and OT hours, other deductions, sick leave used in accrual year and sick leave balance. |
| Payslip sick leave balance required | [[FACT:ak.payslip.sick_leave_balance.required=True]] | from 2025-09-25 |  | S1 |  |

## AK.5 Statutory reporting

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Report SUI quarterly form | [[FACT:ak.report.sui.quarterly.form=TQ01C (2/26) with wage schedule; due last day of month after quarter; zero report required; wages reported in quarter paid]] | from 2026-01-01 |  | S10 |  |
| Report SUI quarterly late penalty min | USD [[FACT:ak.report.sui.quarterly.late_penalty_min=10]] | from 2026-01-01 |  | S11 |  |
| Report SUI employee fields | [[FACT:ak.report.sui.employee_fields=SSN, name, reportable wages, occupational code (6 or 8 digit), 2-digit geographic code]] | from 2026-01-01 |  | S10 | Alaska-specific DD fields. |
| Report SUI channel | [[FACT:ak.report.sui.channel=file_upload (CSV, no headings; header 11 cols, detail 12 cols, rev. 2016-05-17) or online keying or paper]] | from 2026-01-01 |  | S12 |  |
| Report SUI online mandatory threshold employees | [[FACT:ak.report.sui.online_mandatory_threshold_employees=50]] employees | from 2026-01-01 |  | S11 | Also mandatory with 1M+ taxable wages in current or prior year, or when a payroll agent files. |
| Newhire report days | [[FACT:ak.newhire.report_days=20]] days | from 2026-01-01 |  | S13 | AS 25.27.075 (statute text not verified). Online via myAlaska; fax no longer accepted. Penalty 10 USD/employee. |

## AK.6 Leave

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Leave sick accrual hours worked per hour | [[FACT:ak.leave.sick.accrual.hours_worked_per_hour=30]] hours | from 2025-07-01 |  | S1 | 1 h per [[FACT:ak.leave.sick.accrual.hours_worked_per_hour=30]] h worked, overtime included (AS 23.10.067). |
| Leave sick cap hours under 15 fte | [[FACT:ak.leave.sick.cap_hours.under_15_fte=40]] hours | from 2025-07-01 |  | S1 | Cap on accrual and use per year; FTE counted on prior calendar year (8 AAC 15.106). |
| Leave sick cap hours 15 plus fte | [[FACT:ak.leave.sick.cap_hours.15_plus_fte=56]] hours | from 2025-07-01 |  | S1 |  |
| Leave sick payout on separation | [[FACT:ak.leave.sick.payout_on_separation=False]] | from 2025-07-01 |  | S1 | AS 23.10.068(a)(1). Reinstated on rehire within 6 months. |
| Leave sick rehire reinstatement months | [[FACT:ak.leave.sick.rehire_reinstatement_months=6]] months | from 2025-07-01 |  | S1 |  |

Not configured in this release [[GAP:RQ-454]]: Leave sick multistate coverage: not established from an official source.

## AK.7 Termination and final pay

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Final pay discharge working days | [[FACT:ak.final_pay.discharge.working_days=3]] working days | from 2026-01-01 |  | S1 | AS 23.05.140(b). Resignation: next regular payday at least [[FACT:ak.final_pay.discharge.working_days=3]] days after notice. |
| Final pay penalty max working days | [[FACT:ak.final_pay.penalty.max_working_days=90]] working days | from 2026-01-01 |  | S1 |  |

Not configured in this release [[GAP:RQ-450]]: Final pay accrued vacation payout: not established from an official source.

## AK.8 Benefits in kind and taxable wages

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| SUI wages excludes 401k deferrals | [[FACT:ak.sui.wages.excludes_401k_deferrals=True]] | from 2026-01-01 |  | S11 | AS 23.20.530 per ES Tax Handbook (A.3): 401(k)/403(b)/457/SEP/SIMPLE deferrals excluded from UI wages, unlike FUTA; dependent care, adoption, group legal and cash cafeteria elections ARE UI wages. |
| Board lodging no determination max per day | USD [[FACT:ak.board_lodging.no_determination_max_per_day=20]] | from 2026-01-01 |  | S1 | 8 AAC 15.160(d)-(f); prior written notice and signed acceptance required. |

## AK.9 Deductions and garnishments

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Garnishment exempt weekly | USD [[FACT:ak.garn.exempt.weekly=473]] | from 2026-01-01 |  | S14 | Greater of [[FACT:ak.garn.exempt.weekly=473]]/week or 75% of disposable earnings (AS 09.38.030, CPI-adjusted per 8 AAC 95.030, not verified; amounts via CIV-530 8/24). Monthly / 4.3, semi-monthly / 2.17. |
| Garnishment exempt weekly household support | USD [[FACT:ak.garn.exempt.weekly_household_support=743]] | from 2026-01-01 |  | S14 |  |
| Garnishment exempt liquid assets monthly | USD [[FACT:ak.garn.exempt.liquid_assets_monthly=1,890]] | from 2026-01-01 |  | S14 |  |

Not configured in this release [[GAP:RQ-452]]: Garnishment IWO employer fee: not established from an official source.

## AK.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Prevailing wage threshold | USD [[FACT:ak.prevailing_wage.threshold=25,000]] | from 2026-01-01 |  | S15 | Title 36 public construction over [[FACT:ak.prevailing_wage.threshold=25,000]] USD. |

Not configured in this release [[GAP:RQ-453]]: Prevailing wage certified payroll frequency: not established from an official source.

## AK.11 Indexation

The minimum wage is indexed to the Anchorage CPI-U from 2028 (no indexed value yet). The exempt-salary threshold and the school-bus driver rate follow the minimum wage by statutory multiple (AK.1). The UI wage base is set yearly from the State average annual wage (next-year base not yet published, AK.3). Garnishment exemptions follow the CPI (AS 09.38.115).

## AK.12 Payroll data protection and records

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Records wage hour retention years | [[FACT:ak.records.wage_hour.retention_years=3]] years | from 2026-01-01 |  | S1 | AS 23.10.100, at the place of employment (central in-state office counts, 8 AAC 15.900). |
| Records UI retention years | [[FACT:ak.records.ui.retention_years=5]] years | from 2026-01-01 |  | S11 | ES Tax Handbook (A.3). |

## AK.13 Live legal change

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Live sb217 employer STEP status | [[FACT:ak.live.sb217_employer_step.status=not enacted (in S FIN since 2026-04-15); would operate at UI employer contribution level]] | from 2026-04-15 |  | S16 |  |
| Live hb161 sick leave status | [[FACT:ak.live.hb161_sick_leave.status=not enacted (referred H L&C 2025-03-28, never moved)]] | from 2025-03-28 |  | S17 |  |

Not configured in this release [[GAP:RQ-455]]: Live bulletin sweep: not established from an official source.

## AK.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## AK.15 Special populations

- Domestic and household workers: excluded from the minimum wage, overtime and sick-leave rules (AS 23.10.055(a)(4)); UI coverage only above the quarterly cash-wage threshold.
- Agricultural workers: excluded from minimum wage, overtime and sick leave; UI coverage only above the agricultural thresholds.
- Commercial fishing: crews excluded from wage-hour and sick-leave rules; small share-paid crews excluded from UI; seamen excluded from overtime.
- Minors under 18 working part time: excluded from wage-hour and sick-leave rules except in a week above the part-time limit (8 AAC 15.135).
- Tipped employees: no tip credit; the full minimum wage is due in cash.
- Clergy and religious orders: excluded from UI; volunteers of religious non-profits excluded from wage-hour rules.
- Students at their own school and young work-study students: excluded from UI; student learners may be paid below the minimum wage under a certificate (8 AAC 15.125).
- Non-resident aliens: no State rule beyond the federal one.
- Corporate officers: excluded from UI unless the employer elects coverage for all officers; commission-only insurance, real-estate and securities agents excluded from UI when excluded from FUTA.
- Government: excluded from the minimum-wage, overtime and sick-leave rules; UI contributory or reimbursable.
- Non-profit employers: UI above the statutory size thresholds, with a reimbursable option.
- Multistate: UI wage-base credit for other-State wages of transferred employees (AK.2b); sick-leave reach to employees working partly in Alaska is open (AK.6).

Not configured in this release [[GAP:RQ-510]]: The coverage thresholds that apply to these populations (quarterly cash-wage and headcount thresholds for UI coverage of domestic, agricultural and non-profit employment) are cited by statute only and are not established as values; the engine must not hard-code them until they are established.

## AK.16 Language

No language clause in the pay-statement rule or the posters: payslip and filings in English.

## AK.S Sources

| Ref | Instrument | Article / section | Authority |
|---|---|---|---|
| S1 | Alaska DOLWD Wage and Hour Pamphlet 100 (October 2025): AS 23.05, AS 23.10 (Alaska Wage and Hour Act incl. 2024 Ballot Measure 1), 8 AAC 15 (incl. sick-leave … | AS 23.05.140, 23.05.160, 23.10.040, 23.10.043, 23.10.055, 23.10.060, 23.10.065, 23.10.066-.069, 23.10.070, 23.10.100; 8 AAC 15.105-15.119, 15.125, 15.135, 15.160, 15.165, 15.900, 15.907, 15.908 | Alaska DOLWD Labor Standards and Safety Division |
| S2 | Alaska DOLWD Wage and Hour home page (minimum wage notice) | Alaska minimum wage notice (page last updated 2026-05-01) | Alaska DOLWD Labor Standards and Safety Division |
| S3 | Alaska DOR Tax Division Tax Types page + Withholding Tax and Employment Security entries | Tax Types (25 items); programs/index.aspx?10003; ?10000 | Alaska Department of Revenue |
| S4 | Alaska Tax Facts (Office of the State Assessor, DCRA) | whole page | Alaska Dept of Commerce, Community and Regional Affairs |
| S5 | Alaska Unemployment Insurance Tax Rates for Experienced Employers, 2026 | 2026 rating period table; AS 23.20.285 | Alaska DOLWD Employment Security Tax |
| S6 | Alaska UI Tax Rates for New (Industry) Employers, 2026 | Industry rate table 2026 | Alaska DOLWD Employment Security Tax |
| S7 | Alaska UI Tax Calculation Cookbook, 2026 rates (last update 2025-12-04) | Steps 1-3; AS 23.20.290(c)-(f); AS 23.20.310(7) | Alaska DOLWD Research and Analysis Section |
| S8 | State Training and Employment Program (STEP) employee contribution | AS 23.15.630; AS 23.20.175 | AK official authority |
| S9 | Technical and Vocational Education Program (TVEP) employee contribution | AS 23.15.835 | AK official authority |
| S10 | Alaska Quarterly Contribution Report TQ01C (2/26), 2026 edition | Form TQ01C (2/26), items 1-16 | Alaska DOLWD Employment Security Tax |
| S11 | Alaska Employment Security Tax Employer Handbook (taxbook.pdf, PDF modified 2025-05-05) | pp. 6-25 (employer, multistate, TQ01, wage base, employee contribution, records, excluded employment, wages, retirement/125/fringe, rates) | Alaska DOLWD Employment Security Tax |
| S12 | Alaska ES Tax Multiple Filer and Single Filer CSV Specifications and General Guidelines (rev. 2016-05-17) for online quarterly wage upload | Header record cols 1-11; wage detail cols 1-12 | Alaska DOLWD Employment Security Tax |
| S13 | Alaska CSSD/CSED New Hire Reporting employer notice (PDF modified 2022-06-02) citing AS 25.27.075 | AS 25.27.075; AS 25.27.075(f) | Alaska Department of Revenue, Child Support Enforcement Division (formerly CSSD) |
| S14 | Alaska Court System form CIV-530 (8/24) Notice of Garnishment and Notice of Right to Exemptions (AS 09.38.030-.065; 8 AAC 95.030; 15 USC 1673) | CIV-530 pp. 1-2 | Alaska Court System |
| S15 | AS 36.05.005 and 36.05.010 prevailing wage on public construction | AS 36.05.005; 36.05.010 | Alaska Legislature |
| S16 | Alaska Legislature, 34th Legislature SB 217 'Employer Contributions' (employer STEP contribution) bill status (wayback snapshot 2026-06-08) | Bill detail: current status | Alaska Legislature (BASIS) |
| S17 | Alaska Legislature, 34th Legislature HB 161 'Paid Sick Leave Exemption' bill status (wayback snapshot 2026-10-15) | Bill detail: current status | Alaska Legislature (BASIS) |

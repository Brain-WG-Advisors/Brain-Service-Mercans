# Annex WA: Washington


Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T1 - no state wage tax; SUI and levies only** (build manifest, tier rationale). The Seattle payroll expense tax, a threshold-conditional employer tax on a city return [US-WAP51-001], is declared as a T4-shaped element.

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]. Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a verified fact and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. A point marked as a research gap has not been closed by the research; it is not filled with an estimate.

## WA.1 Employment and labour code

- **State minimum wage (RCW 49.46.020) [US-WAS5-001, US-WAS5-006, US-WAS5-007]:** [[FACT:wa.minwage.hourly=17.13]] USD per hour in 2026 and [[FACT:wa.minwage.hourly=17.73]] USD from 2027-01-01. Youth aged 14-15: [[FACT:wa.labour.minwage.youth_14_15.hourly=14.56]] USD in 2026 and [[FACT:wa.labour.minwage.youth_14_15.hourly=15.07]] USD in 2027; 16-17 year olds receive the full rate.
- **Tip credit:** not allowed ([[FACT:wa.minwage.tip_credit.allowed=False]]); tips and service charges go to the employee in full; automatic service charges must be disclosed (49.46.160) [US-WAS5-001].
- **Local minimum wages, 2026 [US-WAS5-008].** Each city defines employer size itself. Two localities step up mid-year on 2026-07-01.

| Locality | Rate | Employer tier / period |
|---|---|---|
| Seattle | [[FACT:wa.labour.minwage.local.seattle.hourly=21.30]] USD | single rate |
| Tukwila | [[FACT:wa.labour.minwage.local.tukwila.hourly=21.65]] USD | single rate |
| Bellingham | [[FACT:wa.labour.minwage.local.bellingham.hourly=19.13]] USD | single rate |
| SeaTac | [[FACT:wa.labour.minwage.local.seatac.hourly=20.74]] USD | hospitality and transportation employers |
| Burien | [[FACT:wa.labour.minwage.local.burien.large.hourly=21.78]] / [[FACT:wa.labour.minwage.local.burien.mid.hourly=20.78]] / [[FACT:wa.labour.minwage.local.burien.small.hourly=19.28]] USD | large / mid / small employers |
| King County (unincorporated) | [[FACT:wa.labour.minwage.local.king_county_uninc.large.hourly=20.82]] USD | large employers (other tiers per the L&I page) |
| Everett | [[FACT:wa.labour.minwage.local.everett.large.hourly=20.77]] USD | large employers |
| Everett | [[FACT:wa.labour.minwage.local.everett.mid.hourly=18.77]] USD, then [[FACT:wa.labour.minwage.local.everett.mid.hourly=19.77]] USD from 2026-07-01 | mid-size employers (smallest employers not covered) |
| Renton | [[FACT:wa.labour.minwage.local.renton.large.hourly=21.57]] USD | large employers |
| Renton | [[FACT:wa.labour.minwage.local.renton.mid.hourly=20.57]] USD, then [[FACT:wa.labour.minwage.local.renton.mid.hourly=21.57]] USD from 2026-07-01 | mid-size employers |

  2027 local rates are not obtained [[GAP:RQ-371]] (blocking open point below).
- **Overtime (RCW 49.46.130) [US-WAS5-001]:** [[FACT:wa.overtime.premium.multiplier=1.5]] times the regular rate over [[FACT:wa.overtime.weekly_threshold_hours=40]] hours per week, including agricultural employees since 2024; no daily overtime.
- **Exempt salary threshold (WAC 296-128-545) [US-WAS5-005, US-WAS5-007]:** 2026: [[FACT:wa.exempt.salary.weekly_min=1,541.70]] USD per week for any employer size. 2027: [[FACT:wa.labour.exempt_salary.large.weekly=1,773.00]] USD per week for larger employers and [[FACT:wa.labour.exempt_salary.small.weekly=1,595.70]] USD for smaller employers. Computer professionals paid hourly: [[FACT:wa.labour.computer_professional.hourly=59.96]] USD (2026) and [[FACT:wa.labour.computer_professional.hourly=62.06]] USD (2027).
- **Pay frequency (WAC 296-126-023) [US-WAS5-004]:** [[FACT:wa.pay_frequency.rule=at least monthly; pay day max 10 days after period end for shorter periods]]; overtime paid on the regular payday of the period earned; direct deposit available on payday.
- **Method of payment:** NSF fees reimbursed (RCW 49.48.010(1)) [US-WAS5-002]; direct-deposit and paycard consent rule not read (open point below).

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wa.minwage.hourly` | [[FACT:wa.minwage.hourly=17.13]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-006 | RCW 49.46.020(2)(b) |
| `wa.minwage.hourly` | [[FACT:wa.minwage.hourly=17.73]] | USD | from 2027-01-01 | US-WAS5-007 |  |
| `wa.labour.minwage.youth_14_15.hourly` | [[FACT:wa.labour.minwage.youth_14_15.hourly=14.56]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-007 | 85% of minimum |
| `wa.labour.minwage.youth_14_15.hourly` | [[FACT:wa.labour.minwage.youth_14_15.hourly=15.07]] | USD | from 2027-01-01 | US-WAS5-007 |  |
| `wa.minwage.indexation` | [[FACT:wa.minwage.indexation=CPI-W Aug-Aug, announced Sept 30, effective Jan 1, nearest cent]] |  | from 2021-01-01 | US-WAS5-001 |  |
| `wa.labour.minwage.local.seattle.hourly` | [[FACT:wa.labour.minwage.local.seattle.hourly=21.30]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-008 | single rate |
| `wa.labour.minwage.local.tukwila.hourly` | [[FACT:wa.labour.minwage.local.tukwila.hourly=21.65]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-008 |  |
| `wa.labour.minwage.local.bellingham.hourly` | [[FACT:wa.labour.minwage.local.bellingham.hourly=19.13]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-008 |  |
| `wa.labour.minwage.local.seatac.hourly` | [[FACT:wa.labour.minwage.local.seatac.hourly=20.74]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-008 | hospitality and transportation |
| `wa.labour.minwage.local.burien.large.hourly` | [[FACT:wa.labour.minwage.local.burien.large.hourly=21.78]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-008 | 501+ |
| `wa.labour.minwage.local.burien.mid.hourly` | [[FACT:wa.labour.minwage.local.burien.mid.hourly=20.78]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-008 | 16-500 |
| `wa.labour.minwage.local.burien.small.hourly` | [[FACT:wa.labour.minwage.local.burien.small.hourly=19.28]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-008 | up to 15 |
| `wa.labour.minwage.local.king_county_uninc.large.hourly` | [[FACT:wa.labour.minwage.local.king_county_uninc.large.hourly=20.82]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-008 |  |
| `wa.labour.minwage.local.everett.large.hourly` | [[FACT:wa.labour.minwage.local.everett.large.hourly=20.77]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-008 | >500 WA employees |
| `wa.labour.minwage.local.everett.mid.hourly` | [[FACT:wa.labour.minwage.local.everett.mid.hourly=18.77]] | USD | 2026-01-01 to 2026-06-30 | US-WAS5-008 | 15-499 employees; 14 or fewer not covered |
| `wa.labour.minwage.local.everett.mid.hourly` | [[FACT:wa.labour.minwage.local.everett.mid.hourly=19.77]] | USD | 2026-07-01 to 2026-12-31 | US-WAS5-008 | mid-year step |
| `wa.labour.minwage.local.renton.large.hourly` | [[FACT:wa.labour.minwage.local.renton.large.hourly=21.57]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-008 | >500 employees |
| `wa.labour.minwage.local.renton.mid.hourly` | [[FACT:wa.labour.minwage.local.renton.mid.hourly=20.57]] | USD | 2026-01-01 to 2026-06-30 | US-WAS5-008 | 15-500 |
| `wa.labour.minwage.local.renton.mid.hourly` | [[FACT:wa.labour.minwage.local.renton.mid.hourly=21.57]] | USD | 2026-07-01 to 2026-12-31 | US-WAS5-008 | mid-year step |
| `wa.minwage.tip_credit.allowed` | [[FACT:wa.minwage.tip_credit.allowed=False]] |  | from 2021-01-01 | US-WAS5-001 | tips and service charges to employee |
| `wa.overtime.weekly_threshold_hours` | [[FACT:wa.overtime.weekly_threshold_hours=40]] | hours | from 2021-01-01 | US-WAS5-001 | agricultural from 2024-01-01; no daily OT |
| `wa.overtime.premium.multiplier` | [[FACT:wa.overtime.premium.multiplier=1.5]] | ratio | from 2021-01-01 | US-WAS5-001 |  |
| `wa.exempt.salary.weekly_min` | [[FACT:wa.exempt.salary.weekly_min=1,541.70]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-005 |  |
| `wa.labour.exempt_salary.large.weekly` | [[FACT:wa.labour.exempt_salary.large.weekly=1,773.00]] | USD | 2027-01-01 to 2027-12-31 | US-WAS5-007 | 51+ employees 2.5x |
| `wa.labour.exempt_salary.small.weekly` | [[FACT:wa.labour.exempt_salary.small.weekly=1,595.70]] | USD | 2027-01-01 to 2027-12-31 | US-WAS5-007 | 1-50 employees 2.25x |
| `wa.labour.computer_professional.hourly` | [[FACT:wa.labour.computer_professional.hourly=59.96]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-005 |  |
| `wa.labour.computer_professional.hourly` | [[FACT:wa.labour.computer_professional.hourly=62.06]] | USD | from 2027-01-01 | US-WAS5-007 |  |
| `wa.pay_frequency.rule` | [[FACT:wa.pay_frequency.rule=at least monthly; pay day max 10 days after period end for shorter periods]] |  | from 2026-01-01 | US-WAS5-004 | WAC 296-126-023 |

**Open research points**

- Not yet published (expected autumn 2026, before 2027-01-01) [[GAP:RQ-371]]: 2027 local minimum wages not obtained (seattle.gov blocked).
- Not configured in this release [[GAP:RQ-378]]: Direct deposit/paycard consent rule not read.

## WA.2 Income tax withholding

- **No state income tax on wages in 2026 or 2027** (wage tax exists: [[FACT:wa.pit.exists=False]]) [US-WAS5-017]: no withholding, state W-4, supplemental rate, state W-2 or reciprocity. A tax on very high AGI from 2028 (SB 6346) is **assessment-level**; no employer withholding mechanism is stated (open point below).
- **No local employee wage tax** (exists: [[FACT:wa.pit.local.employee_tax.exists=False]]) [US-WAP51-001]. The Seattle Payroll Expense Tax and the Seattle Social Housing Tax are employer taxes on a city return (T4-shaped element) [US-WAP51-001, US-WAP7-005, US-WAP9V-001].
- **Resident and nonresident matrix.** Nothing is withheld for Washington for any income type; a Washington resident working elsewhere follows the work state's rules (Annex MULTI).

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wa.pit.exists` | [[FACT:wa.pit.exists=False]] |  | 2026-01-01 to 2027-12-31 | US-WAS5-017 | No Washington individual income tax on wages in 2026 or 2027. From 2028-01-01 SB 6346 creates a [[FACT:wa.pit.high_income_tax.rate=9.9]]% tax on AGI over 1,000,000 (see wa.pit.high_income_tax.*), assessment-level. LEVEL: withholding. |
| `wa.pit.local.employee_tax.exists` | [[FACT:wa.pit.local.employee_tax.exists=False]] |  | from 2026-01-01 | US-WAP51-001 | Seattle PET and Social Housing Tax are employer taxes |
| `wa.pit.high_income_tax.rate` | [[FACT:wa.pit.high_income_tax.rate=9.9]] | % | from 2028-01-01 | US-WAS5-017 | SB 6346 (2026): individuals and joint filers with AGI over 1,000,000; first returns due April 2029. No employer withholding guidance published as of 2026-11-02. LEVEL: assessment. |
| `wa.pit.high_income_tax.agi_threshold` | [[FACT:wa.pit.high_income_tax.agi_threshold=1,000,000]] | USD | from 2028-01-01 | US-WAS5-017 | LEVEL: assessment. |

**Open research points**

- Not configured in this release [[GAP:RQ-375]]: SB 6346 text not read to confirm no withholding clause before 2028.

## WA.2b Non-resident regime and reciprocity

The non-resident and reciprocity rules of this jurisdiction are written in WA.2.

## WA.2c Local wage taxes

The local wage taxes of this jurisdiction, where any exist, are written in WA.2.

## WA.3 Social insurance: unemployment, disability, paid leave and payroll levies

- **Unemployment insurance (ESD) [US-WAS5-012, US-WAS5-029].** 2026 taxable wage base [[FACT:wa.sui.wage_base=78,200]] USD. Total 2026 rates (experience rate, social cost and administration fund) from [[FACT:wa.ui.rate.min_total=0.27]] % to [[FACT:wa.ui.rate.max_total=6.02]] %. New employers: [[FACT:wa.ui.rate.new_employer.rule=115% of industry average, floor 1%]]. Employee contribution [[FACT:wa.sui.employee.rate=0]] %. UI wages include commissions, bonuses, non-cash pay and reported tips (RCW 50.04.320) [US-WAS5-022].
- **Paid Family and Medical Leave [US-WAS5-011, US-WAS5-015, US-WAS5-020].** Total premium [[FACT:wa.pfml.total.rate=1.13]] % in 2026, employee share up to [[FACT:wa.pfml.employee.share=71.43]] % of the total; [[FACT:wa.pfml.total.rate=1.2]] % in 2027 (the statutory cap), employee share [[FACT:wa.pfml.employee.share=70.7]] %. Wage cap [[FACT:wa.pfml.wage_cap.annual=184,500]] USD in 2026 (the Social Security wage base). Employers with fewer than [[FACT:wa.pfml.small_employer.threshold=50]] Washington employees owe no employer share but collect the employee share. 2SHB 2345 (effective 2026-06-11, applied from 2027 premiums) reallocates the employee share between the family and medical lines (the 2027 line split is open, below). PFML wages exclude tips (tips included: [[FACT:wa.pfml.wages.tips_included=False]]) [US-WAS5-023]. Penalties and interest on late reports and premiums from [[FACT:wa.pfml.penalties.from=2026-08-01]]; missed premiums cannot be recovered from employees later [US-WAB5-002].
- **WA Cares Fund (long-term care) [US-WAS5-016, US-WAS5-024]:** employee-only premium of [[FACT:wa.ltc.wa_cares.employee.rate=0.58]] % of gross wages, no cap; same gross-wage definition as Paid Leave ([[FACT:wa.cares.base.same_as_pfml=True]]) [US-WAB5-003]. Exemptions include out-of-state residents, active-duty military and spouses, qualifying veterans, approved private-LTC exemptees, and non-immigrant work-visa holders automatically from 2026-01-01 unless they opt in.
- **Workers' compensation (L&I state fund) [US-WAS5-019, US-WALTC-002]:** hourly premiums per risk class; employee deduction rule [[FACT:wa.wc.employee_deduction.rule=50% x (Stay-at-Work + Medical Aid + Supplemental Pension) per hour per risk class]]; 2026 supplemental pension rate [[FACT:wa.wc.supplemental_pension.rate=0.1912]] USD per hour for all classes. 2027 rates proposed only (open point below).
- **Retirement deferrals and cafeteria plans** in UI, PFML and WA Cares wages: open (below).

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wa.sui.wage_base` | [[FACT:wa.sui.wage_base=78,200]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-012 |  |
| `wa.ui.rate.min_total` | [[FACT:wa.ui.rate.min_total=0.27]] | % | 2026-01-01 to 2026-12-31 | US-WAS5-029 | experience 0.00-5.40 + social cost 0.24-0.72 + EAF 0.02-0.03 |
| `wa.ui.rate.max_total` | [[FACT:wa.ui.rate.max_total=6.02]] | % | 2026-01-01 to 2026-12-31 | US-WAS5-029 | delinquent up to 8.15 |
| `wa.ui.rate.new_employer.rule` | [[FACT:wa.ui.rate.new_employer.rule=115% of industry average, floor 1%]] |  | 2026-01-01 to 2026-12-31 | US-WAS5-029 | WAC 192-320-025 |
| `wa.sui.employee.rate` | [[FACT:wa.sui.employee.rate=0]] | % | 2026-01-01 to 2026-12-31 | US-WAS5-012 |  |
| `wa.pfml.total.rate` | [[FACT:wa.pfml.total.rate=1.13]] | % | 2026-01-01 to 2026-12-31 | US-WAS5-015 | employee up to [[FACT:wa.pfml.employee.share=71.43]]% |
| `wa.pfml.employee.share` | [[FACT:wa.pfml.employee.share=71.43]] | % | 2026-01-01 to 2026-12-31 | US-WAB5-002 | of total premium |
| `wa.pfml.total.rate` | [[FACT:wa.pfml.total.rate=1.2]] | % | from 2027-01-01 | US-WAS5-015 |  |
| `wa.pfml.employee.share` | [[FACT:wa.pfml.employee.share=70.7]] | % | from 2027-01-01 | US-WAS5-015 |  |
| `wa.pfml.wage_cap.annual` | [[FACT:wa.pfml.wage_cap.annual=184,500]] | USD | 2026-01-01 to 2026-12-31 | US-WAB5-002 | = SS wage base |
| `wa.pfml.small_employer.threshold` | [[FACT:wa.pfml.small_employer.threshold=50]] |  | from 2026-01-01 | US-WAS5-011 | <50 WA employees owe no employer share |
| `wa.pfml.wages.tips_included` | [[FACT:wa.pfml.wages.tips_included=False]] |  | from 2026-01-01 | US-WAS5-023 | PFML excludes tips; UI includes reported tips (US-WAS5-022) |
| `wa.ltc.wa_cares.employee.rate` | [[FACT:wa.ltc.wa_cares.employee.rate=0.58]] | % | from 2023-07-01 | US-WAS5-016 | employee-only, no cap; non-immigrant visa holders auto-exempt from 2026-01-01 (US-WAS5-024) |
| `wa.wc.employee_deduction.rule` | [[FACT:wa.wc.employee_deduction.rule=50% x (Stay-at-Work + Medical Aid + Supplemental Pension) per hour per risk class]] |  | 2026-01-01 to 2026-12-31 | US-WAS5-019 |  |
| `wa.wc.supplemental_pension.rate` | [[FACT:wa.wc.supplemental_pension.rate=0.1912]] | USD (USD per hour) | 2026-01-01 to 2026-12-31 | US-WAS5-019 | per hour, all classes |
| `wa.pfml.penalties.from` | [[FACT:wa.pfml.penalties.from=2026-08-01]] |  | from 2026-08-01 | US-WAB5-002 | Penalties on past-due reports and interest on overdue premiums from this date; missed premiums cannot be collected from employees in later pay periods. |
| `wa.cares.base.same_as_pfml` | [[FACT:wa.cares.base.same_as_pfml=True]] |  | from 2026-06-26 | US-WAB5-003 | 'Paid Leave and WA Cares use the same definition of gross wages and hours.' |

**Open research points**

- Not configured in this release [[GAP:RQ-372]]: No WAC section or ESD publication names an exclusion for employee elective deferrals (cafeteria plans, retirement deferrals, HSA) from Paid Leave or WA Cares wages, and the UI text is silent.
- Not configured in this release [[GAP:RQ-373]]: 2027 UI wage base not published.
- Not configured in this release [[GAP:RQ-374]]: Final 2027 WC rates and RCW 51.32.073 not read.
- Not configured in this release [[GAP:RQ-380]]: UI exclusions for clergy and students (50.44.040) not read.
- Not configured in this release [[GAP:RQ-381]]: The 2027 family / medical premium line split under 2SHB 2345 is derived only; the ESD split tables were not readable.

## WA.4 Pay statement

- **Content (WAC 296-126-040) [US-WAS5-004]:** [[FACT:wa.payslip.items=pay basis (hours/days), rates, gross, all deductions, pay period dates, payment date; separate from paycheck]]. Electronic delivery allowed if the employee can receive and copy the statement on payday.
- **Paid sick leave balance** at least monthly (accrued, used, available), which may go on the pay statement ([[FACT:wa.payslip.sick_leave_balance.monthly=True]]) (WAC 296-128-755(2)) [US-WAS5-005]. A "WA Cares Fund" paystub label is recommended, not mandatory [US-WAS5-016].
- **Retention:** keep the longest period: ESD records [[FACT:wa.records.esd.retention_years=4]] years from payment (RCW 50.12.070) [US-WAS5-030].

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wa.payslip.items` | [[FACT:wa.payslip.items=pay basis (hours/days), rates, gross, all deductions, pay period dates, payment date; separate from paycheck]] |  | from 2026-01-01 | US-WAS5-004 | WAC 296-126-040; electronic if employee can receive and copy |
| `wa.payslip.sick_leave_balance.monthly` | [[FACT:wa.payslip.sick_leave_balance.monthly=True]] |  | from 2026-01-01 | US-WAS5-005 | WAC 296-128-755(2) |
| `wa.records.esd.retention_years` | [[FACT:wa.records.esd.retention_years=4]] | years | from 2026-01-01 | US-WAS5-030 | L&I 3 years; keep longest |

## WA.5 Statutory reporting

- **No withholding return or state W-2.** Registration: DOR business licence when first hiring [US-WAS5-013].
- **UI quarterly tax and wage report (ESD) [US-WAS5-013, US-FIL-016]:** per employee name, SSN, gross pay, hours worked in the quarter and SOC code; due [[FACT:wa.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]]; nil report required; exempt corporate officers reported separately [US-WAS5-027].
- **Paid Leave + WA Cares combined quarterly report [US-WAB5-003]:** fields [[FACT:wa.report.pfml_ltc.fields=Combined Paid Leave + WA Cares quarterly report; per employee: SSN or ITIN, last and first name (middle initial optional), hours associated with wages paid (rounded up to a whole number; salaried full-time 40 h/week; no hours for leave cash-outs or severance), wages paid in the quarter excluding tips, WA Cares exemption status, date of birth; employer totals of Paid Leave and WA Cares premiums withheld]]; due [[FACT:wa.report.pfml_ltc.due=Last day of the month after each quarter: Apr 30 / Jul 31 / Oct 31 / Jan 31, next business day (WAC 192-540-030)]]; filed even with no payroll ([[FACT:wa.report.pfml_ltc.no_payroll_report=True]]); channels [[FACT:wa.report.pfml_ltc.channels=Manual entry (up to 50 employees), single CSV file (ESD template), ICESA bulk file for employer agents]].
- **New hire (RCW 26.23.040) [US-WAS5-018, US-WAS5-014]:** to the Washington state support registry within [[FACT:wa.newhire.report_days=20]] days of hire, including qualifying rehires.
- **Third-party filing:** UI power of attorney per client [US-FEDP51-016]; Seattle taxpayer authorization form [US-WAP51-001]. **Public works:** certified payroll per Section 10.

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wa.report.ui.quarterly_due` | [[FACT:wa.report.ui.quarterly_due=Apr 30; Jul 31; Oct 31; Jan 31]] |  | from 2026-01-01 | US-WAS5-013 | per employee: hours worked and SOC code; nil report required |
| `wa.newhire.report_days` | [[FACT:wa.newhire.report_days=20]] | days | from 2026-01-01 | US-WAS5-018 | incl. DOB |
| `wa.report.pfml_ltc.fields` | [[FACT:wa.report.pfml_ltc.fields=Combined Paid Leave + WA Cares quarterly report; per employee: SSN or ITIN, last and first name (middle initial optional), hours associated with wages paid (rounded up to a whole number; salaried full-time 40 h/week; no hours for leave cash-outs or severance), wages paid in the quarter excluding tips, WA Cares exemption status, date of birth; employer totals of Paid Leave and WA Cares premiums withheld]] |  | from 2026-06-26 | US-WAB5-003 |  |
| `wa.report.pfml_ltc.due` | [[FACT:wa.report.pfml_ltc.due=Last day of the month after each quarter: Apr 30 / Jul 31 / Oct 31 / Jan 31, next business day (WAC 192-540-030)]] |  | from 2026-06-26 | US-WAB5-003 |  |
| `wa.report.pfml_ltc.no_payroll_report` | [[FACT:wa.report.pfml_ltc.no_payroll_report=True]] |  | from 2026-06-26 | US-WAB5-003 | File every quarter even with no payroll (8 consecutive quarters unless closure notified). |
| `wa.report.pfml_ltc.channels` | [[FACT:wa.report.pfml_ltc.channels=Manual entry (up to 50 employees), single CSV file (ESD template), ICESA bulk file for employer agents]] |  | from 2026-06-26 | US-WAB5-003 |  |

## WA.6 Leave

- **Paid sick leave (RCW 49.46.210) [US-WAS5-001, US-WAS5-005]:** accrual at least one hour per [[FACT:wa.leave.paid_sick.accrual_ratio_hours_worked=40]] hours worked; usable after the statutory waiting period; paid at the greater of minimum wage or normal rate; carry-over may be capped; payout at separation: [[FACT:wa.leave.sick.payout_on_separation=False]] (construction workers excepted); reinstated on rehire within the statutory period.
- **PFML job protection (RCW 50A.35.010) [US-WAS5-028]:** employers with [[FACT:wa.leave.pfml.job_protection.employer_threshold=25]] or more employees in 2026 (lower thresholds in 2027 and 2028), employee tenure test.
- Seattle Paid Sick and Safe Time not obtained [[GAP:RQ-576]] (seattle.gov blocked). No vacation statute.

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wa.leave.paid_sick.accrual_ratio_hours_worked` | [[FACT:wa.leave.paid_sick.accrual_ratio_hours_worked=40]] | hours | from 2021-01-01 | US-WAS5-001 | usable from day 90; carryover cap 40 |
| `wa.leave.sick.payout_on_separation` | [[FACT:wa.leave.sick.payout_on_separation=False]] |  | from 2021-01-01 | US-WAS5-001 | except construction workers |
| `wa.leave.pfml.job_protection.employer_threshold` | [[FACT:wa.leave.pfml.job_protection.employer_threshold=25]] |  | 2026-01-01 to 2026-12-31 | US-WAS5-028 | 15+ in 2027; 8+ from 2028; 180 days tenure |

## WA.7 Termination and final pay

- **Final pay (RCW 49.48.010(2)) [US-WAS5-002]:** [[FACT:wa.final_pay.rule=end of established pay period (discharge and resignation)]]; a CBA may provide otherwise. Final-pay deductions limited (WAC 296-126-025) [US-WAS5-004].
- **Discharge statement:** within [[FACT:wa.term.discharge_statement.days=21]] days of a written request, the discharge date and reason (WAC 296-126-050(4)) [US-WAS5-004].
- **Domestic workers from 2027-07-01:** written termination notice (SHB 2355) [US-WAS5-021]. Vacation payout and state notices: open points below.

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wa.final_pay.rule` | [[FACT:wa.final_pay.rule=end of established pay period (discharge and resignation)]] |  | from 2026-01-01 | US-WAS5-002 | RCW 49.48.010(2) |
| `wa.term.discharge_statement.days` | [[FACT:wa.term.discharge_statement.days=21]] | days | from 2026-01-01 | US-WAS5-004 | on written request |

**Open research points**

- Not configured in this release [[GAP:RQ-376]]: State mini-WARN and ESD separation-notice rules not read.
- Not configured in this release [[GAP:RQ-377]]: Vacation payout at separation: L&I policy not read.

## WA.8 Benefits in kind and taxable wages

- **Income tax:** not applicable. **UI and PFML** count all remuneration including non-cash compensation; tips included for UI, excluded for PFML [US-WAS5-022, US-WAS5-023]. Deferral treatment open (Section 3).

## WA.9 Deductions and garnishments

- **Authorisation (RCW 49.48.010(3), 49.52.060) [US-WAS5-002, US-WAS5-003, US-WAS5-004]:** required by law, agreed (express written advance authorisation for 49.52.060 deductions), or for medical care, with no employer profit. Private-employer overpayment recoupment within the WAC limits; public employers capped per period (49.48.200).
- **Garnishment exemption (RCW 6.27.150) [US-WAS5-009]:** general debts: the greater of [[FACT:wa.garn.general.exempt.weekly=253.75]] USD per week or the CCPA share; consumer debts: the greater of [[FACT:wa.garn.consumer.exempt.weekly=599.55]] USD per week (2026) or [[FACT:wa.garn.consumer.exempt_rate=80]] % of disposable earnings. Private student loans: open point below. Processing fee [[FACT:wa.garn.answer_fee.first=20]] USD for the first answer (6.27.095).
- **Child support (RCW 26.23.060) [US-WAS5-018]:** the DCS order takes priority over any garnishment; cap [[FACT:wa.garn.iwo.max_rate=50]] % of disposable earnings; remit within the statutory working days; employer fee up to [[FACT:wa.garn.iwo.employer_fee.first=10]] USD for the first disbursement and a smaller fee thereafter.

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wa.garn.consumer.exempt_rate` | [[FACT:wa.garn.consumer.exempt_rate=80]] | % | from 2026-01-01 | US-WAS5-009 | consumer debt: greater of 80% or 35x state minimum |
| `wa.garn.consumer.exempt.weekly` | [[FACT:wa.garn.consumer.exempt.weekly=599.55]] | USD | 2026-01-01 to 2026-12-31 | US-WAS5-009 |  |
| `wa.garn.general.exempt.weekly` | [[FACT:wa.garn.general.exempt.weekly=253.75]] | USD | from 2026-01-01 | US-WAS5-009 |  |
| `wa.garn.answer_fee.first` | [[FACT:wa.garn.answer_fee.first=20]] | USD | from 2026-01-01 | US-WAS5-009 | second 10 |
| `wa.garn.iwo.employer_fee.first` | [[FACT:wa.garn.iwo.employer_fee.first=10]] | USD | from 2026-01-01 | US-WAS5-018 | 1 per later disbursement; remit within 7 working days; IWO priority over garnishment |
| `wa.garn.iwo.max_rate` | [[FACT:wa.garn.iwo.max_rate=50]] | % | from 2026-01-01 | US-WAS5-018 |  |

**Open research points**

- Not configured in this release [[GAP:RQ-379]]: Whether "highest minimum wage law in the state" in RCW 6.27.150(3)(a) means the state or a local rate is unresolved.

## WA.10 Collective agreements and prevailing wage

- **Prevailing wage (RCW 39.12) [US-WAP51-002, US-WAS5-010]:** public works and public building service maintenance contracts; certified payroll: [[FACT:wa.prevailing_wage.certified_payroll=monthly in L&I online system; records 3 years]]. No sector CBA sets statutory payroll minima; CBAs may override the pay interval and final-pay timing.

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wa.prevailing_wage.certified_payroll` | [[FACT:wa.prevailing_wage.certified_payroll=monthly in L&I online system; records 3 years]] |  | from 2026-01-01 | US-WAS5-010 | statement of intent on contracts >10,000 |

## WA.11 Indexation

- **State minimum wage:** [[FACT:wa.minwage.indexation=CPI-W Aug-Aug, announced Sept 30, effective Jan 1, nearest cent]] [US-WAS5-001]; youth rate, exempt threshold and computer-professional rate are multiples of it; the consumer-debt garnishment exemption moves with it.
- **Local minimum wages:** each city's ordinance [US-WAS5-008]. **UI wage base:** average wages, published by ESD (2027 open). **PFML cap:** the Social Security wage base; **PFML rate:** formula, capped. **WA Cares:** fixed. **Workers' compensation:** L&I rule each December.

## WA.12 Payroll data protection and records

- **Breach notification (RCW 19.255.010) [US-WAS5-025]:** notify affected residents within [[FACT:wa.data.breach.notice_days=30]] calendar days of discovery; notify the Attorney General above the statutory count; processors (including payroll providers) notify the data owner immediately. No pay-statement SSN rule found.

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `wa.data.breach.notice_days` | [[FACT:wa.data.breach.notice_days=30]] | days | from 2026-01-01 | US-WAS5-025 | AG if >500 residents |

## WA.13 Live legal change

- **2026-01-01:** PFML job-protection thresholds; WA Cares visa-holder exemption [US-WAS5-028, US-WAS5-024].
- **2026-06-11:** 2SHB 2345 (PFML premium allocation, applied from 2027) [US-WAS5-020]. **2026-07-01:** Everett and Renton local steps [US-WAS5-008]. **2026-08-01:** PFML penalties [US-WAB5-002].
- **2027-01-01:** minimum wage, exempt threshold, youth and computer-professional rates; PFML 2027 rate and split [US-WAS5-007, US-WAS5-015]. **2027-07-01:** Domestic Workers Bill of Rights [US-WAS5-021].
- **2028-01-01:** SB 6346 high-income tax (assessment) [US-WAS5-017]. Not yet published: 2027 UI wage base, final 2027 workers' compensation rates, 2027 local minimum wages.

## WA.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## WA.15 Special populations

| Population | Washington rule | Register id |
|---|---|---|
| Domestic / household | Casual labour in a private home excluded from the MWA; from 2027-07-01 minimum wage, overtime, written agreement and termination notice (SHB 2355); UI once the quarterly cash test is met | US-WAS5-001, US-WAS5-021, US-WAS5-013 |
| Agricultural | Overtime over the weekly threshold since 2024; narrow MWA exclusion for piece-rate hand harvesters | US-WAS5-001, US-WAS5-005 |
| Minors | Youth rate for 14-15 year olds (Section 1); full rate for 16-17; prohibited occupations | US-WAS5-006, US-WAS5-005 |
| Tipped | No tip credit; UI includes reported tips, PFML excludes them | US-WAS5-001, US-WAS5-022, US-WAS5-023 |
| Clergy / religious | Volunteers for religious bodies are not employees without a real employment relationship; UI exemption not read | US-WAS5-001 |
| Students | Student-learner sub-minimum by certificate; UI exemption not read | US-WAS5-005 |
| Nonresident aliens | No state income tax; WA Cares visa-holder exemption; no PFML visa exemption located | US-WAS5-024 |
| Corporate officers | Exempt from UI by default for for-profit corporations; coverage optional | US-WAS5-027 |
| Statutory employees | No Washington-specific rule located | - |
| Government employees | Elected and appointed officials and legislative staff excluded from the MWA; public-employer overpayment rules; fire and police work periods | US-WAS5-001, US-WAS5-002 |
| Apprentices / learners / workers with disabilities | Sub-minimum wage by special certificate | US-WAS5-001, US-WAS5-005 |
| Construction workers | Accrued sick leave paid out at separation before eligibility | US-WAS5-001 |

## WA.16 Language

No language rule for employee documents is written for this jurisdiction in this annex.

## WA.S Sources

Register ids cited in this annex resolve to the build record; the URL of each value is in the facts file. Authorities:

- City of Seattle Office of City Finance: US-WAP51-001
- WA Cares Fund (DSHS / ESD): US-WAS5-016
- Washington Department of Revenue: US-WAS5-017
- Washington Employment Security Department: US-WAS5-012, US-WAS5-013, US-WAS5-015, US-WAS5-029, US-WAS5-030
- Washington Employment Security Department (Paid Leave): US-WAB5-002
- Washington Employment Security Department - Paid Family and Medical Leave: US-WAB5-002, US-WAB5-003
- Washington L&I (Code Reviser): US-WAS5-005
- Washington L&I (Code Reviser): US-WAS5-004
- Washington State Department of Labor & Industries: US-WAS5-006, US-WAS5-007, US-WAS5-008, US-WAS5-019
- Washington State Legislature (Code Reviser): US-WAS5-011
- Washington State Legislature (Code Reviser): US-WAS5-018
- Washington State Legislature (Code Reviser): US-WAS5-023
- Washington State Legislature (Code Reviser): US-WAS5-010
- Washington State Legislature (Code Reviser): US-WAS5-028
- Washington State Legislature (Code Reviser): US-WAS5-001
- Washington State Legislature (Code Reviser): US-WAS5-002
- Washington State Legislature (Code Reviser): US-WAS5-009
- Washington State Legislature (Code Reviser): US-WAS5-025

## @labour
- **State minimum wage (RCW 49.46.020) [US-WAS5-001, US-WAS5-006, US-WAS5-007]:** {{wa.minwage.hourly@2026-01-01}} USD per hour in 2026 and {{wa.minwage.hourly@2027-01-01}} USD from 2027-01-01. Youth aged 14-15: {{wa.labour.minwage.youth_14_15.hourly@2026-01-01}} USD in 2026 and {{wa.labour.minwage.youth_14_15.hourly@2027-01-01}} USD in 2027; 16-17 year olds receive the full rate.
- **Tip credit:** not allowed ({{wa.minwage.tip_credit.allowed}}); tips and service charges go to the employee in full; automatic service charges must be disclosed (49.46.160) [US-WAS5-001].
- **Local minimum wages, 2026 [US-WAS5-008].** Each city defines employer size itself. Two localities step up mid-year on 2026-07-01.

| Locality | Rate | Employer tier / period |
|---|---|---|
| Seattle | {{wa.labour.minwage.local.seattle.hourly}} USD | single rate |
| Tukwila | {{wa.labour.minwage.local.tukwila.hourly}} USD | single rate |
| Bellingham | {{wa.labour.minwage.local.bellingham.hourly}} USD | single rate |
| SeaTac | {{wa.labour.minwage.local.seatac.hourly}} USD | hospitality and transportation employers |
| Burien | {{wa.labour.minwage.local.burien.large.hourly}} / {{wa.labour.minwage.local.burien.mid.hourly}} / {{wa.labour.minwage.local.burien.small.hourly}} USD | large / mid / small employers |
| King County (unincorporated) | {{wa.labour.minwage.local.king_county_uninc.large.hourly}} USD | large employers (other tiers per the L&I page) |
| Everett | {{wa.labour.minwage.local.everett.large.hourly}} USD | large employers |
| Everett | {{wa.labour.minwage.local.everett.mid.hourly@2026-01-01}} USD, then {{wa.labour.minwage.local.everett.mid.hourly@2026-07-01}} USD from 2026-07-01 | mid-size employers (smallest employers not covered) |
| Renton | {{wa.labour.minwage.local.renton.large.hourly}} USD | large employers |
| Renton | {{wa.labour.minwage.local.renton.mid.hourly@2026-01-01}} USD, then {{wa.labour.minwage.local.renton.mid.hourly@2026-07-01}} USD from 2026-07-01 | mid-size employers |

  2027 local rates are not obtained (blocking open point below).
- **Overtime (RCW 49.46.130) [US-WAS5-001]:** {{wa.overtime.premium.multiplier}} times the regular rate over {{wa.overtime.weekly_threshold_hours}} hours per week, including agricultural employees since 2024; no daily overtime.
- **Exempt salary threshold (WAC 296-128-545) [US-WAS5-005, US-WAS5-007]:** 2026: {{wa.exempt.salary.weekly_min}} USD per week for any employer size. 2027: {{wa.labour.exempt_salary.large.weekly}} USD per week for larger employers and {{wa.labour.exempt_salary.small.weekly}} USD for smaller employers. Computer professionals paid hourly: {{wa.labour.computer_professional.hourly@2026-01-01}} USD (2026) and {{wa.labour.computer_professional.hourly@2027-01-01}} USD (2027).
- **Pay frequency (WAC 296-126-023) [US-WAS5-004]:** {{wa.pay_frequency.rule}}; overtime paid on the regular payday of the period earned; direct deposit available on payday.
- **Method of payment:** NSF fees reimbursed (RCW 49.48.010(1)) [US-WAS5-002]; direct-deposit and paycard consent rule not read (open point below).

## @income_tax
- **No state income tax on wages in 2026 or 2027** (wage tax exists: {{wa.pit.exists}}) [US-WAS5-017]: no withholding, state W-4, supplemental rate, state W-2 or reciprocity. A tax on very high AGI from 2028 (SB 6346) is **assessment-level**; no employer withholding mechanism is stated (open point below).
- **No local employee wage tax** (exists: {{wa.pit.local.employee_tax.exists}}) [US-WAP51-001]. The Seattle Payroll Expense Tax and the Seattle Social Housing Tax are employer taxes on a city return (T4-shaped element) [US-WAP51-001, US-WAP7-005, US-WAP9V-001].
- **Resident and nonresident matrix.** Nothing is withheld for Washington for any income type; a Washington resident working elsewhere follows the work state's rules (Annex MULTI).

## @social
- **Unemployment insurance (ESD) [US-WAS5-012, US-WAS5-029].** 2026 taxable wage base {{wa.sui.wage_base}} USD. Total 2026 rates (experience rate, social cost and administration fund) from {{wa.ui.rate.min_total}} % to {{wa.ui.rate.max_total}} %. New employers: {{wa.ui.rate.new_employer.rule}}. Employee contribution {{wa.sui.employee.rate}} %. UI wages include commissions, bonuses, non-cash pay and reported tips (RCW 50.04.320) [US-WAS5-022].
- **Paid Family and Medical Leave [US-WAS5-011, US-WAS5-015, US-WAS5-020].** Total premium {{wa.pfml.rate.total@2026-01-01}} % in 2026, employee share up to {{wa.pfml.employee.share@2026-01-01}} % of the total; {{wa.pfml.rate.total@2027-01-01}} % in 2027 (the statutory cap), employee share {{wa.pfml.employee.share@2027-01-01}} %. Wage cap {{wa.pfml.wage_cap.annual}} USD in 2026 (the Social Security wage base). Employers with fewer than {{wa.pfml.small_employer.threshold}} Washington employees owe no employer share but collect the employee share. 2SHB 2345 (effective 2026-06-11, applied from 2027 premiums) reallocates the employee share between the family and medical lines (the 2027 line split is open, below). PFML wages exclude tips (tips included: {{wa.pfml.wages.tips_included}}) [US-WAS5-023]. Penalties and interest on late reports and premiums from {{wa.pfml.penalties.from}}; missed premiums cannot be recovered from employees later [US-WAB5-002].
- **WA Cares Fund (long-term care) [US-WAS5-016, US-WAS5-024]:** employee-only premium of {{wa.ltc.wa_cares.employee.rate}} % of gross wages, no cap; same gross-wage definition as Paid Leave ({{wa.cares.base.same_as_pfml}}) [US-WAB5-003]. Exemptions include out-of-state residents, active-duty military and spouses, qualifying veterans, approved private-LTC exemptees, and non-immigrant work-visa holders automatically from 2026-01-01 unless they opt in.
- **Workers' compensation (L&I state fund) [US-WAS5-019, US-WALTC-002]:** hourly premiums per risk class; employee deduction rule {{wa.wc.employee_deduction.rule}}; 2026 supplemental pension rate {{wa.wc.supplemental_pension.rate}} USD per hour for all classes. 2027 rates proposed only (open point below).
- **Retirement deferrals and cafeteria plans** in UI, PFML and WA Cares wages: open (below).

## @payslip
- **Content (WAC 296-126-040) [US-WAS5-004]:** {{wa.payslip.items}}. Electronic delivery allowed if the employee can receive and copy the statement on payday.
- **Paid sick leave balance** at least monthly (accrued, used, available), which may go on the pay statement ({{wa.payslip.sick_leave_balance.monthly}}) (WAC 296-128-755(2)) [US-WAS5-005]. A "WA Cares Fund" paystub label is recommended, not mandatory [US-WAS5-016].
- **Retention:** keep the longest period: ESD records {{wa.records.esd.retention_years}} years from payment (RCW 50.12.070) [US-WAS5-030].

## @reporting
- **No withholding return or state W-2.** Registration: DOR business licence when first hiring [US-WAS5-013].
- **UI quarterly tax and wage report (ESD) [US-WAS5-013, US-FIL-016]:** per employee name, SSN, gross pay, hours worked in the quarter and SOC code; due {{wa.report.ui.quarterly_due}}; nil report required; exempt corporate officers reported separately [US-WAS5-027].
- **Paid Leave + WA Cares combined quarterly report [US-WAB5-003]:** fields {{wa.report.pfml_ltc.fields}}; due {{wa.report.pfml_ltc.due}}; filed even with no payroll ({{wa.report.pfml_ltc.no_payroll_report}}); channels {{wa.report.pfml_ltc.channels}}.
- **New hire (RCW 26.23.040) [US-WAS5-018, US-WAS5-014]:** to the Washington state support registry within {{wa.newhire.report_days}} days of hire, including qualifying rehires.
- **Third-party filing:** UI power of attorney per client [US-FEDP51-016]; Seattle taxpayer authorization form [US-WAP51-001]. **Public works:** certified payroll per Section 10.

## @leave
- **Paid sick leave (RCW 49.46.210) [US-WAS5-001, US-WAS5-005]:** accrual at least one hour per {{wa.leave.paid_sick.accrual_ratio_hours_worked}} hours worked; usable after the statutory waiting period; paid at the greater of minimum wage or normal rate; carry-over may be capped; payout at separation: {{wa.leave.sick.payout_on_separation}} (construction workers excepted); reinstated on rehire within the statutory period.
- **PFML job protection (RCW 50A.35.010) [US-WAS5-028]:** employers with {{wa.leave.pfml.job_protection.employer_threshold}} or more employees in 2026 (lower thresholds in 2027 and 2028), employee tenure test.
- Seattle Paid Sick and Safe Time not obtained (seattle.gov blocked). No vacation statute.

## @termination
- **Final pay (RCW 49.48.010(2)) [US-WAS5-002]:** {{wa.final_pay.rule}}; a CBA may provide otherwise. Final-pay deductions limited (WAC 296-126-025) [US-WAS5-004].
- **Discharge statement:** within {{wa.term.discharge_statement.days}} days of a written request, the discharge date and reason (WAC 296-126-050(4)) [US-WAS5-004].
- **Domestic workers from 2027-07-01:** written termination notice (SHB 2355) [US-WAS5-021]. Vacation payout and state notices: open points below.

## @bik
- **Income tax:** not applicable. **UI and PFML** count all remuneration including non-cash compensation; tips included for UI, excluded for PFML [US-WAS5-022, US-WAS5-023]. Deferral treatment open (Section 3).

## @deductions
- **Authorisation (RCW 49.48.010(3), 49.52.060) [US-WAS5-002, US-WAS5-003, US-WAS5-004]:** required by law, agreed (express written advance authorisation for 49.52.060 deductions), or for medical care, with no employer profit. Private-employer overpayment recoupment within the WAC limits; public employers capped per period (49.48.200).
- **Garnishment exemption (RCW 6.27.150) [US-WAS5-009]:** general debts: the greater of {{wa.garn.general.exempt.weekly}} USD per week or the CCPA share; consumer debts: the greater of {{wa.garn.consumer.exempt.weekly}} USD per week (2026) or {{wa.garn.consumer.exempt_rate}} % of disposable earnings. Private student loans: open point below. Processing fee {{wa.garn.answer_fee.first}} USD for the first answer (6.27.095).
- **Child support (RCW 26.23.060) [US-WAS5-018]:** the DCS order takes priority over any garnishment; cap {{wa.garn.iwo.max_rate}} % of disposable earnings; remit within the statutory working days; employer fee up to {{wa.garn.iwo.employer_fee.first}} USD for the first disbursement and a smaller fee thereafter.

## @cba
- **Prevailing wage (RCW 39.12) [US-WAP51-002, US-WAS5-010]:** public works and public building service maintenance contracts; certified payroll: {{wa.prevailing_wage.certified_payroll}}. No sector CBA sets statutory payroll minima; CBAs may override the pay interval and final-pay timing.

## @indexation
- **State minimum wage:** {{wa.minwage.indexation}} [US-WAS5-001]; youth rate, exempt threshold and computer-professional rate are multiples of it; the consumer-debt garnishment exemption moves with it.
- **Local minimum wages:** each city's ordinance [US-WAS5-008]. **UI wage base:** average wages, published by ESD (2027 open). **PFML cap:** the Social Security wage base; **PFML rate:** formula, capped. **WA Cares:** fixed. **Workers' compensation:** L&I rule each December.

## @data
- **Breach notification (RCW 19.255.010) [US-WAS5-025]:** notify affected residents within {{wa.data.breach.notice_days}} calendar days of discovery; notify the Attorney General above the statutory count; processors (including payroll providers) notify the data owner immediately. No pay-statement SSN rule found.

## @live
- **2026-01-01:** PFML job-protection thresholds; WA Cares visa-holder exemption [US-WAS5-028, US-WAS5-024].
- **2026-06-11:** 2SHB 2345 (PFML premium allocation, applied from 2027) [US-WAS5-020]. **2026-07-01:** Everett and Renton local steps [US-WAS5-008]. **2026-08-01:** PFML penalties [US-WAB5-002].
- **2027-01-01:** minimum wage, exempt threshold, youth and computer-professional rates; PFML 2027 rate and split [US-WAS5-007, US-WAS5-015]. **2027-07-01:** Domestic Workers Bill of Rights [US-WAS5-021].
- **2028-01-01:** SB 6346 high-income tax (assessment) [US-WAS5-017]. Not yet published: 2027 UI wage base, final 2027 workers' compensation rates, 2027 local minimum wages.

## @special
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

## @gaps
- wa.pfml.family_medical_split :: The 2027 family / medical premium line split under 2SHB 2345 is derived only; the ESD split tables were not readable. :: ESD/paidleave.wa.gov premium split tables.
- wa.ui_pfml_ltc.deferrals :: No WAC section or ESD publication names an exclusion for employee elective deferrals (cafeteria plans, retirement deferrals, HSA) from Paid Leave or WA Cares wages, and the UI text is silent. :: An explicit ESD statement (Paid Leave employer help center or a WAC amendment) and RCW 50.04.320 / ESD UI guidance for UI wages.
- wa.garn.student_loan_wage_meaning :: Whether "highest minimum wage law in the state" in RCW 6.27.150(3)(a) means the state or a local rate is unresolved. :: Court or AG reading.

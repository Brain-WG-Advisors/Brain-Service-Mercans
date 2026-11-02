## @labour
- **Minimum wage (Va. Code 40.1-28.10; 2026 cc.350/351) [US-VAS5-001, US-VAS5-015]:**

| From | Rate |
|---|---|
| 2026-01-01 | {{va.minwage.hourly@2026-01-01}} USD |
| 2027-01-01 | {{va.minwage.hourly@2027-01-01}} USD |
| 2028-01-01 | {{va.minwage.hourly@2028-01-01}} USD |

  CPI-U indexation from 2029-01-01 (published by DOLI by October 1). Each year's rate is the greater of the state and federal rates. On-the-job trainees for a limited initial period: the greater of the federal minimum or {{va.labour.minwage.trainee.ratio}} % of the state rate (the statute fixes no rounding rule).
- **Coverage exclusions (40.1-28.9) [US-VAS5-002]:** under-16s, minors employed by a parent, certain students, babysitters, au pairs, H-2 workers, summer camps, outside salespeople and others; farm laborers are covered from {{va.labour.minwage.farm_laborers_covered_from}} (2026 cc.357/358).
- **Local minimum wages:** none; one statewide rate, no express preemption section found (open point below).
- **Overtime [US-VAS5-004, US-VAS5-023]:** {{va.overtime.premium.multiplier}} times the regular rate over {{va.overtime.weekly_threshold_hours}} hours per week, following the FLSA with state remedies; a separate state rule covers derivative air-carrier employees and home-care direct-support workers.
- **Tipped employees [US-VAS5-015]:** cash wage at least {{va.minwage.tipped.cash_wage}} USD per hour with the FLSA tip credit; cash wage plus tips must reach the state minimum.
- **Pay frequency [US-VAS5-003]:** {{va.pay_frequency.rule}}; monthly pay allowed for work-study students and, by agreement, for high earners.
- **Method of payment [US-VAS5-003]:** {{va.payment.method}}. Remedies: liquidated damages plus interest; treble damages for knowing violations; good-faith cure defence from 2026-07-01.

## @income_tax
- **Method (Va. Code 58.1-461; guide 2614086 Rev. 10/26) [US-VAPIT-002, US-VAS5-013]:** annualised taxable income = gross wages x pay periods - (standard deduction {{va.pit.std_deduction.single@2025-01-01}} USD + {{va.pit.exemption.personal}} USD x personal exemptions + {{va.pit.exemption.aged_blind}} USD x age/blind exemptions); tax by brackets with ceilings at {{va.pit.bracket.1.ceiling}}, {{va.pit.bracket.2.ceiling}} and {{va.pit.bracket.3.ceiling}} USD and a top rate of {{va.pit.bracket.4.rate}} % above the last ceiling; withholding = annual tax / pay periods. The lower bracket rates and base amounts are carried in the formula fact `va.wh.method` (its text contains square brackets, so it is shown in the parameter table rather than as an inline tag). Tables are rounded to the dollar; the formula gives the exact amount.
- **Standard deduction by statute [US-VAS5-018]:** {{va.pit.std_deduction.single@2025-01-01}} USD single and {{va.pit.std_deduction.married@2025-01-01}} USD married for tax years 2025-2026. For tax year 2027 the statute sets {{va.pit.std_deduction.single@2027-01-01}} USD / {{va.pit.std_deduction.married@2027-01-01}} USD, while the Rev. 10/26 guide states a reversion. The statute prevails, but these are assessment-level amounts: **the 2027 withholding deduction is not modelled** until Virginia Tax publishes the 2027 formula (blocking open point below).
- **Certificate [US-VAS5-021]:** {{va.wh.certificate}}; electronic VA-4 allowed.
- **Supplemental wages [US-VAS5-013]:** aggregated when paid with regular wages; when paid separately, the aggregate method or a flat {{va.wh.supplemental.rate}} % if tax was withheld from regular wages.
- **Withholding wages** follow the federal definition, with listed exempt payments [US-VAS5-013].
- **Local income tax:** none (exists: {{va.local_wage_tax.exists}}); barred by 58.1-300 [US-VAR3-001].
- **Reciprocity [US-VAS5-013, US-VAPIT-004]:** {{va.reciprocity.states}}; claimed on the VA-4. Residents of all other states are withheld.
- **Resident and nonresident matrix.**

| Income type | Virginia resident | Nonresident |
|---|---|---|
| Regular salary | Formula or tables on all wages | Wages for services in Virginia, unless a reciprocity exemption is claimed on the VA-4 |
| Bonus / supplemental | Aggregate, or flat {{va.wh.supplemental.rate}} % if paid separately | Same, Virginia share |
| Nonperiodic pension | Separate pension rate per the guide | Same |
| Severance, equity, benefits in kind | Follow federal wages (IRC conformity date in Section 8) | Virginia-source share |

## @social
- **Unemployment insurance (VEC) [US-VASUI-001, US-VAS5-014, US-VAR3-002, US-VAR3-003].** Wage base {{va.sui.wage_base}} USD per employee per year, statutory and not indexed. New employer {{va.sui.new_employer.rate}} % "plus add-ons" (60.2-526(B)). Base rates {{va.sui.employer.rate.min}} % to {{va.sui.employer.rate.max}} %. Add-ons: fund-building charge {{va.ui.fund_building.rate}} % when the trust fund is at or below the statutory level, and a pool cost charge set yearly (2026 percentage not obtained; whether the new-employer rate includes the add-ons is contradictory: blocking open point below). Employee contribution {{va.sui.employee.rate}} %.
- **UI gross wages [US-VAS5-014]:** after cafeteria-plan deductions (included: {{va.sui.wages.section125_included}}) and before retirement deferrals (included: {{va.sui.wages.401k_included}}).
- **Coverage:** FUTA-liable employers and the quarterly or 20-week tests; domestic, agricultural and nonprofit tests; churches and ministers excluded [US-VAS5-014, US-VAS5-020, US-VAS5-012].
- **SDI / TDI:** none.
- **Paid family and medical leave (Title 60.2 ch. 8, 2026 cc.981/1093) [US-VAS5-016, US-VAS5-017]:** no contribution in 2026 or 2027; contributions start {{va.pfml.contributions_start}}, with the rate fixed by 2027-10-01; benefits from 2028-12-01. The wage cap follows the Social Security wage base. Larger employers may deduct up to half from the employee and remit the full contribution; small employers remit only the employee share.
- **Other levies:** per the levy census [US-OWN-007].

## @payslip
- **Content (40.1-29(D)) [US-VAS5-003, US-VAP51-005]:** on each regular pay date, by paystub or online accounting: {{va.payslip.items}}, with enough detail to work out gross and net pay. Statements kept for the statutory period; agricultural employers provide one only on request. Online delivery is expressly allowed; no language clause [US-VAL-001].

## @reporting
- **Withholding (Virginia Tax) [US-VAPIT-003, US-VAR3-004, US-VAS5-013, US-VAS5-009]:** quarterly or monthly VA-5 below the semi-weekly threshold; semi-weekly payment on VA-15 once monthly liability reaches {{va.report.wh.semiweekly_threshold.monthly}} USD, reconciled quarterly on VA-16; annual VA-6 due {{va.report.va6.due}}; returns required even with no tax due; all electronic.
- **State W-2:** due January 31 through Web Upload (EFW2) or eForms; uploading W-2s does not create the VA-6 [US-VAS5-013, US-VAS5-009].
- **UI quarterly report (VEC) [US-VAS5-014]:** due {{va.report.ui.quarterly_due}}, via ESS, eForm or Web Upload; amendments on FC-34; ESS access needs ID.me from 2026-08-01 [US-VAP6-001].
- **New hire [US-VAS5-006]:** to the Virginia New Hire Reporting Center within {{va.newhire.report_days}} days of hire (contractors within the same period of the contract).
- **Registration and agents:** R-1 / R-1H; VEC registration; PAR 101 and ESS TPA invitation [US-VAS5-013, US-VAS5-014, US-VAP51-007, US-VAP6-001].

## @leave
- **Paid sick leave in 2026:** home health workers only (40.1-33.3) ({{va.leave.paid_sick.home_health_only}}) [US-VAS5-005].
- **General paid sick leave (40.1-33.6:1-:7, 2026 cc.1128/1129), enacted [US-VAS5-022]:** phase-in {{va.leave.paid_sick.general.start}}; accrual one hour per {{va.leave.paid_sick.accrual_ratio_hours_worked}} hours worked with statutory caps; front-loading and qualifying PTO policies allowed; no payout at separation; paid at the regular rate without tip credit.
- **PFML benefits** from 2028 (Section 3).

## @termination
- **Final pay [US-VAS5-003]:** {{va.final_pay.rule}}.
- **Accrued vacation:** no statute requires payout; depends on policy (negative finding; open point below). Sick leave from 2027: no payout [US-VAS5-022].
- **W-2 on termination:** on the day of the last payment of remuneration [US-VAS5-009]. VEC sends the separation report only when a claim is filed [US-VAS5-014].

## @bik
- **Conformity:** fixed-date conformity to the IRC as of {{va.bik.conformity.irc_date}} (58.1-301, 2026 c.7); no exception touches employee exclusions, so Virginia follows federal treatment of retirement deferrals, cafeteria plans, HSA, transit and group-term life [US-VAS5-011]. Withholding follows the federal wage definition [US-VAS5-013].
- **UI wages** differ: cafeteria plans excluded, retirement deferrals included (Section 3). Treatment of the federal tips and overtime deductions (P.L. 119-21) is open (below).

## @deductions
- **Deductions:** none without written signed authorisation, except taxes or legally required deductions [US-VAS5-003].
- **Garnishment (34-29) [US-VAS5-007]:** the lesser of {{va.garn.creditor.max_percent}} % of disposable earnings or the amount above forty times the greater of the federal or state minimum wage, a protected floor of {{va.garn.consumer.floor.weekly}} USD per week in 2026; stricter than the CCPA. Support orders: CCPA support percentages. State tax debts come within the limits from 2027-07-01 (2026 c.396).
- **Child-support withholding (20-79.3) [US-VAS5-010]:** the lesser of the ordered amount or the 34-29 maximum; employer fee up to {{va.garn.iwo.employer_fee.per_remittance}} USD per remittance; support has priority, prorated across orders; EFT mandatory for larger employers; notify DCSE on termination.

## @cba
- **Prevailing wage [US-VAS5-019, US-VAP51-006]:** public works for state agencies and covered institutions, and localities that adopt an ordinance; contracts of {{va.prevailing_wage.threshold}} USD or less are excluded; never below Davis-Bacon; certified payroll records and posting duties.

## @indexation
- **Minimum wage:** fixed by statute through 2028, CPI-U from 2029 [US-VAS5-001].
- **UI wage base:** statutory, not indexed [US-VASUI-001]. **PFML:** wage cap tied to the Social Security wage base [US-VAS5-016].
- **Income tax:** brackets and exemptions not indexed; the standard deduction is fixed by statute year by year [US-VAS5-018]. **Garnishment floor:** moves with the minimum wage.

## @data
- **SSN [US-VAS5-008]:** not visible on or through a mailed envelope ({{va.data.ssn.mailed_visible_prohibited}}), not published, not embedded in documents. No pay-statement truncation rule; 40.1-29(D) does not list the SSN. The W-2 carries the SSN [US-VAS5-009].

## @live
- **2026-07-01:** good-faith defence (c.1040); pay transparency (HR, not payroll); prevailing-wage amendments [US-VAS5-003, US-VAS5-024, US-VAS5-019].
- **Tax year 2026:** IRC conformity date [US-VAS5-011].
- **2027-01-01:** minimum wage step; farm laborers covered [US-VAS5-001, US-VAS5-002]. **Tax year 2027:** statutory standard deduction (assessment; withholding formula not yet published) [US-VAS5-018].
- **2027-07-01:** general paid sick leave phase-in; state tax debts within garnishment limits [US-VAS5-022, US-VAS5-007].
- **2028:** minimum wage step; PFML contributions from 2028-04-01 [US-VAS5-001, US-VAS5-016].
- Listed but not read: amendments to 58.1-332 (resident credit) and 40.1-100 (child labour) (open point below) [US-VAS5-025].

## @special
| Population | Virginia rule | Register id |
|---|---|---|
| Domestic / household | Covered by the minimum wage; UI above a quarterly cash test; R-1H registration, annual VA-6H | US-VAS5-002, US-VAS5-014, US-VAS5-013 |
| Agricultural | Covered by the minimum wage from 2027; paystub only on request; UI coverage tests | US-VAS5-002, US-VAS5-003, US-VAS5-020 |
| Minors | Young workers and certain students excluded from the minimum wage; a young child of the employer excluded from UI | US-VAS5-002, US-VAS5-020 |
| Tipped | Cash wage per Section 1; sick pay from 2027 without tip credit | US-VAS5-002, US-VAS5-015, US-VAS5-022 |
| Clergy / religious | Excluded from UI; no Virginia withholding where federal withholding does not apply | US-VAS5-012, US-VAS5-013 |
| Students | Minimum-wage and UI exclusions; work-study monthly pay | US-VAS5-002, US-VAS5-020, US-VAS5-003 |
| Nonresident aliens | No Virginia-specific rule; temporary foreign workers excluded from the minimum wage | US-VAS5-013, US-VAS5-002 |
| Statutory employees | No state withholding rule beyond federal; commission-only agents and direct sellers excluded from UI | US-VAS5-020 |
| Government employees | Covered by the state minimum wage; UI covers state and local service with exclusions; sick leave from 2027 includes the Commonwealth | US-VAS5-015, US-VAS5-012, US-VAS5-022 |
| Home health / home care | Paid sick leave in force; state overtime regular-rate rule | US-VAS5-005, US-VAS5-023 |

## @gaps
- va.pit.formula.next_year :: Virginia Tax has not published the 2027 withholding formula; its Rev. 10/26 guide states a reversion of the standard deduction while the statute sets {{va.pit.std_deduction.single@2027-01-01}} USD for tax year 2027. No 2027 withholding deduction is modelled. :: 2026 c.7 / Sp.Sess.I c.1 enacting clauses and Virginia Tax 2027 guide 2614086.
- va.ui.pool_cost_and_new_employer :: The 2026 pool cost charge was not obtained at tier A, and whether the new-employer rate of {{va.sui.new_employer.rate}} % already includes the add-ons is contradictory between sources. :: VEC 2026 tax-rate notice (ESS) or VEC 2026 rate release (Chrome pass).

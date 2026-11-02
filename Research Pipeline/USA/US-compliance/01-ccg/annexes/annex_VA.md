# Annex VA - Virginia

Jurisdiction annex of the United States Country Configuration Guide (US-CCG-001). Layer classification: **T3 - state withholding; local layer absent or piggybacked on the state return** (build manifest, tier rationale).

The federal layer (federal income tax withholding, FICA, FUTA, Forms W-2, 941 and 940) and the multistate rules (residence and work-location sourcing, reciprocity mechanics) are in Annex FED and Annex MULTI and are not repeated here. Independent contractors and Form 1099-NEC are out of scope (MANDATE, US-OWN-001). Payslip language: English; second-language duties attach to notices and posters only (US-OWN-006).

Every value in this annex is bound to a key of `_research/CCG-annex_VA-facts.json` and carries its legal-basis register id. A value that changes during the year is shown with its effective dates. `RESEARCH-GAP` marks a point the research has not closed; it is not filled with an estimate.

## 1. Labour code and pay rules

- **Minimum wage (Va. Code 40.1-28.10; 2026 cc.350/351) [US-VAS5-001, US-VAS5-015]:**

| From | Rate |
|---|---|
| 2026-01-01 | [[FACT:va.minwage.hourly=12.77]] USD |
| 2027-01-01 | [[FACT:va.minwage.hourly=13.75]] USD |
| 2028-01-01 | [[FACT:va.minwage.hourly=15.00]] USD |

  CPI-U indexation from 2029-01-01 (published by DOLI by October 1). Each year's rate is the greater of the state and federal rates. On-the-job trainees for a limited initial period: the greater of the federal minimum or [[FACT:va.labour.minwage.trainee.ratio=75]] % of the state rate (the statute fixes no rounding rule).
- **Coverage exclusions (40.1-28.9) [US-VAS5-002]:** under-16s, minors employed by a parent, certain students, babysitters, au pairs, H-2 workers, summer camps, outside salespeople and others; farm laborers are covered from [[FACT:va.labour.minwage.farm_laborers_covered_from=2027-01-01]] (2026 cc.357/358).
- **Local minimum wages:** none; one statewide rate, no express preemption section found (open point below).
- **Overtime [US-VAS5-004, US-VAS5-023]:** [[FACT:va.overtime.premium.multiplier=1.5]] times the regular rate over [[FACT:va.overtime.weekly_threshold_hours=40]] hours per week, following the FLSA with state remedies; a separate state rule covers derivative air-carrier employees and home-care direct-support workers.
- **Tipped employees [US-VAS5-015]:** cash wage at least [[FACT:va.minwage.tipped.cash_wage=2.13]] USD per hour with the FLSA tip credit; cash wage plus tips must reach the state minimum.
- **Pay frequency [US-VAS5-003]:** [[FACT:va.pay_frequency.rule=salaried at least monthly; hourly at least biweekly or twice a month]]; monthly pay allowed for work-study students and, by agreement, for high earners.
- **Method of payment [US-VAS5-003]:** [[FACT:va.payment.method=cash, check, direct deposit to designated account, paycard with consent (one free withdrawal)]]. Remedies: liquidated damages plus interest; treble damages for knowing violations; good-faith cure defence from 2026-07-01.

**Parameters (labour code and pay rules)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `va.minwage.hourly` | [[FACT:va.minwage.hourly=12.77]] | USD | 2026-01-01 to 2026-12-31 | US-VAS5-001 | greater of state or federal; DOLI second document US-VAS5-015 |
| `va.minwage.hourly` | [[FACT:va.minwage.hourly=13.75]] | USD | 2027-01-01 to 2027-12-31 | US-VAS5-001 | enacted 2026 cc.350/351 |
| `va.minwage.hourly` | [[FACT:va.minwage.hourly=15.00]] | USD | from 2028-01-01 | US-VAS5-001 | enacted; CPI-U indexation from 2029-01-01 |
| `va.labour.minwage.trainee.ratio` | [[FACT:va.labour.minwage.trainee.ratio=75]] | % | from 2026-01-01 | US-VAS5-001 |  |
| `va.labour.minwage.farm_laborers_covered_from` | [[FACT:va.labour.minwage.farm_laborers_covered_from=2027-01-01]] |  | from 2027-01-01 | US-VAS5-002 | 2026 cc.357/358 |
| `va.overtime.weekly_threshold_hours` | [[FACT:va.overtime.weekly_threshold_hours=40]] | hours | from 2022-07-01 | US-VAS5-004 | FLSA via state remedies; state regular-rate rule for derivative air-carrier and home-care (US-VAS5-023) |
| `va.overtime.premium.multiplier` | [[FACT:va.overtime.premium.multiplier=1.5]] | ratio | from 2022-07-01 | US-VAS5-004 |  |
| `va.pay_frequency.rule` | [[FACT:va.pay_frequency.rule=salaried at least monthly; hourly at least biweekly or twice a month]] |  | from 2026-07-01 | US-VAS5-003 | monthly by agreement above 150% of state average weekly wage |
| `va.payment.method` | [[FACT:va.payment.method=cash, check, direct deposit to designated account, paycard with consent (one free withdrawal)]] |  | from 2026-07-01 | US-VAS5-003 |  |
| `va.minwage.tipped.cash_wage` | [[FACT:va.minwage.tipped.cash_wage=2.13]] | USD | from 2026-01-01 | US-VAS5-015 |  |

**Open research points**

- ⚠️ RESEARCH-GAP: `va.labour.minwage.local_preemption` (non-blocking; research request filed under this key) - Express local preemption not found (only single statewide rate). Closes with: Express Code provision or DOLI statement.

## 2. Income tax withholding (state and local)

- **Method (Va. Code 58.1-461; guide 2614086 Rev. 10/26) [US-VAPIT-002, US-VAS5-013]:** annualised taxable income = gross wages x pay periods - (standard deduction [[FACT:va.pit.std_deduction.single=8750]] USD + [[FACT:va.pit.exemption.personal=930]] USD x personal exemptions + [[FACT:va.pit.exemption.aged_blind=800]] USD x age/blind exemptions); tax by brackets with ceilings at [[FACT:va.pit.bracket.1.ceiling=3000]], [[FACT:va.pit.bracket.2.ceiling=5000]] and [[FACT:va.pit.bracket.3.ceiling=17,000]] USD and a top rate of [[FACT:va.pit.bracket.4.rate=5.75]] % above the last ceiling; withholding = annual tax / pay periods. The lower bracket rates and base amounts are carried in the formula fact `va.wh.method` (its text contains square brackets, so it is shown in the parameter table rather than as an inline tag). Tables are rounded to the dollar; the formula gives the exact amount.
- **Standard deduction by statute [US-VAS5-018]:** [[FACT:va.pit.std_deduction.single=8750]] USD single and [[FACT:va.pit.std_deduction.married=17,500]] USD married for tax years 2025-2026. For tax year 2027 the statute sets [[FACT:va.pit.std_deduction.single=9200]] USD / [[FACT:va.pit.std_deduction.married=18,400]] USD, while the Rev. 10/26 guide states a reversion. The statute prevails, but these are assessment-level amounts: **the 2027 withholding deduction is not modelled** until Virginia Tax publishes the 2027 formula (blocking open point below).
- **Certificate [US-VAS5-021]:** [[FACT:va.wh.certificate=VA-4 mandatory (federal W-4 not accepted); none = zero exemptions]]; electronic VA-4 allowed.
- **Supplemental wages [US-VAS5-013]:** aggregated when paid with regular wages; when paid separately, the aggregate method or a flat [[FACT:va.wh.supplemental.rate=5.75]] % if tax was withheld from regular wages.
- **Withholding wages** follow the federal definition, with listed exempt payments [US-VAS5-013].
- **Local income tax:** none (exists: [[FACT:va.local_wage_tax.exists=False]]); barred by 58.1-300 [US-VAR3-001].
- **Reciprocity [US-VAS5-013, US-VAPIT-004]:** [[FACT:va.reciprocity.states=KY;DC (daily commuters); MD;PA;WV (<183 days, wage-only, taxed at home)]]; claimed on the VA-4. Residents of all other states are withheld.
- **Resident and nonresident matrix.**

| Income type | Virginia resident | Nonresident |
|---|---|---|
| Regular salary | Formula or tables on all wages | Wages for services in Virginia, unless a reciprocity exemption is claimed on the VA-4 |
| Bonus / supplemental | Aggregate, or flat [[FACT:va.wh.supplemental.rate=5.75]] % if paid separately | Same, Virginia share |
| Nonperiodic pension | Separate pension rate per the guide | Same |
| Severance, equity, benefits in kind | Follow federal wages (IRC conformity date in Section 8) | Virginia-source share |

**Parameters (income tax withholding (state and local))**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `va.wh.method` | see the rule text above (formula value carries brackets; components tagged there) |  | from 2025-07-01 | US-VAS5-013 | guide 2614086 Rev. 10/26; tables rounded to nearest dollar |
| `va.pit.std_deduction.single` | [[FACT:va.pit.std_deduction.single=8750]] | USD | 2025-01-01 to 2026-12-31 | US-VAS5-018 |  |
| `va.pit.std_deduction.married` | [[FACT:va.pit.std_deduction.married=17,500]] | USD | 2025-01-01 to 2026-12-31 | US-VAS5-018 |  |
| `va.pit.std_deduction.single` | [[FACT:va.pit.std_deduction.single=9200]] | USD | 2027-01-01 to 2027-12-31 | US-VAS5-018 | ASSESSMENT level enacted (2026 c.7); 2027 withholding formula not published - guide's 3,000 reversion is superseded by statute |
| `va.pit.std_deduction.married` | [[FACT:va.pit.std_deduction.married=18,400]] | USD | 2027-01-01 to 2027-12-31 | US-VAS5-018 |  |
| `va.pit.exemption.personal` | [[FACT:va.pit.exemption.personal=930]] | USD | from 2025-01-01 | US-VAS5-018 |  |
| `va.pit.exemption.aged_blind` | [[FACT:va.pit.exemption.aged_blind=800]] | USD | from 2025-01-01 | US-VAS5-018 |  |
| `va.pit.bracket.1.ceiling` | [[FACT:va.pit.bracket.1.ceiling=3000]] | USD | from 2025-07-01 | US-VAS5-013 | 2% |
| `va.pit.bracket.2.ceiling` | [[FACT:va.pit.bracket.2.ceiling=5000]] | USD | from 2025-07-01 | US-VAS5-013 | 60 + 3% |
| `va.pit.bracket.3.ceiling` | [[FACT:va.pit.bracket.3.ceiling=17,000]] | USD | from 2025-07-01 | US-VAS5-013 | 120 + 5% |
| `va.pit.bracket.4.rate` | [[FACT:va.pit.bracket.4.rate=5.75]] | % | from 2025-07-01 | US-VAS5-013 | 720 + 5.75% |
| `va.wh.certificate` | [[FACT:va.wh.certificate=VA-4 mandatory (federal W-4 not accepted); none = zero exemptions]] |  | from 2026-04-01 | US-VAS5-021 |  |
| `va.wh.supplemental.rate` | [[FACT:va.wh.supplemental.rate=5.75]] | % | from 2025-07-01 | US-VAS5-013 | if paid separately and tax withheld from regular wages; else aggregate |
| `va.reciprocity.states` | [[FACT:va.reciprocity.states=KY;DC (daily commuters); MD;PA;WV (<183 days, wage-only, taxed at home)]] |  | from 2025-07-01 | US-VAS5-013 | claimed on VA-4 |
| `va.local_wage_tax.exists` | [[FACT:va.local_wage_tax.exists=False]] |  | from 2013-01-01 | US-VAR3-001 | 58.1-300 |

**Open research points**

- ⚠️ RESEARCH-GAP: `va.pit.formula.next_year` (blocking; research request filed under this key) - Virginia Tax has not published the 2027 withholding formula; its Rev. 10/26 guide states a reversion of the standard deduction while the statute sets [[FACT:va.pit.std_deduction.single=9200]] USD for tax year 2027. No 2027 withholding deduction is modelled. Closes with: 2026 c.7 / Sp.Sess.I c.1 enacting clauses and Virginia Tax 2027 guide 2614086.

## 3. Social insurance and payroll levies

- **Unemployment insurance (VEC) [US-VASUI-001, US-VAS5-014, US-VAR3-002, US-VAR3-003].** Wage base [[FACT:va.sui.wage_base=8000]] USD per employee per year, statutory and not indexed. New employer [[FACT:va.sui.new_employer.rate=2.5]] % "plus add-ons" (60.2-526(B)). Base rates [[FACT:va.sui.employer.rate.min=0.1]] % to [[FACT:va.sui.employer.rate.max=6.2]] %. Add-ons: fund-building charge [[FACT:va.ui.fund_building.rate=0.2]] % when the trust fund is at or below the statutory level, and a pool cost charge set yearly (2026 percentage not obtained; whether the new-employer rate includes the add-ons is contradictory: blocking open point below). Employee contribution [[FACT:va.sui.employee.rate=0]] %.
- **UI gross wages [US-VAS5-014]:** after cafeteria-plan deductions (included: [[FACT:va.sui.wages.section125_included=False]]) and before retirement deferrals (included: [[FACT:va.sui.wages.401k_included=True]]).
- **Coverage:** FUTA-liable employers and the quarterly or 20-week tests; domestic, agricultural and nonprofit tests; churches and ministers excluded [US-VAS5-014, US-VAS5-020, US-VAS5-012].
- **SDI / TDI:** none.
- **Paid family and medical leave (Title 60.2 ch. 8, 2026 cc.981/1093) [US-VAS5-016, US-VAS5-017]:** no contribution in 2026 or 2027; contributions start [[FACT:va.pfml.contributions_start=2028-04-01]], with the rate fixed by 2027-10-01; benefits from 2028-12-01. The wage cap follows the Social Security wage base. Larger employers may deduct up to half from the employee and remit the full contribution; small employers remit only the employee share.
- **Other levies:** per the levy census [US-OWN-007].

**Parameters (social insurance and payroll levies)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `va.sui.new_employer.rate` | [[FACT:va.sui.new_employer.rate=2.5]] | % | from 2026-01-01 | US-VAR3-002 | "plus add-ons" per VEC FAQ; add-on composition open |
| `va.sui.employer.rate.min` | [[FACT:va.sui.employer.rate.min=0.1]] | % | from 2026-01-01 | US-VAS5-014 | base rates 0.1-6.2 |
| `va.sui.employer.rate.max` | [[FACT:va.sui.employer.rate.max=6.2]] | % | from 2026-01-01 | US-VAS5-014 |  |
| `va.ui.fund_building.rate` | [[FACT:va.ui.fund_building.rate=0.2]] | % | from 2026-01-01 | US-VAR3-003 | when trust fund at 50% or less |
| `va.sui.employee.rate` | [[FACT:va.sui.employee.rate=0]] | % | from 2026-01-01 | US-VAR3-002 |  |
| `va.sui.wages.section125_included` | [[FACT:va.sui.wages.section125_included=False]] |  | from 2026-01-01 | US-VAS5-014 |  |
| `va.sui.wages.401k_included` | [[FACT:va.sui.wages.401k_included=True]] |  | from 2026-01-01 | US-VAS5-014 |  |
| `va.pfml.contributions_start` | [[FACT:va.pfml.contributions_start=2028-04-01]] |  | from 2028-04-01 | US-VAS5-016 | no contribution in 2026/2027; rate fixed by 2027-10-01; benefits from 2028-12-01 (US-VAS5-017) |
| `va.sui.wage_base` | [[FACT:va.sui.wage_base=8000]] | USD | from 2026-01-01 | US-VASUI-001 | statutory, not indexed |

**Open research points**

- ⚠️ RESEARCH-GAP: `va.ui.pool_cost_and_new_employer` (blocking; research request filed under this key) - The 2026 pool cost charge was not obtained at tier A, and whether the new-employer rate of [[FACT:va.sui.new_employer.rate=2.5]] % already includes the add-ons is contradictory between sources. Closes with: VEC 2026 tax-rate notice (ESS) or VEC 2026 rate release (Chrome pass).

## 4. Payslip statute and payroll records

- **Content (40.1-29(D)) [US-VAS5-003, US-VAP51-005]:** on each regular pay date, by paystub or online accounting: [[FACT:va.payslip.items=employer name/address; hours (hourly and below-FLSA-salary); rate; gross; each deduction amount and purpose]], with enough detail to work out gross and net pay. Statements kept for the statutory period; agricultural employers provide one only on request. Online delivery is expressly allowed; no language clause [US-VAL-001].

**Parameters (payslip statute and payroll records)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `va.payslip.items` | [[FACT:va.payslip.items=employer name/address; hours (hourly and below-FLSA-salary); rate; gross; each deduction amount and purpose]] |  | from 2026-07-01 | US-VAS5-003 | paystub or online accounting; keep 3 years |

## 5. Statutory reporting

- **Withholding (Virginia Tax) [US-VAPIT-003, US-VAR3-004, US-VAS5-013, US-VAS5-009]:** quarterly or monthly VA-5 below the semi-weekly threshold; semi-weekly payment on VA-15 once monthly liability reaches [[FACT:va.report.wh.semiweekly_threshold.monthly=1000]] USD, reconciled quarterly on VA-16; annual VA-6 due [[FACT:va.report.va6.due=January 31 (or 30 days after last wages)]]; returns required even with no tax due; all electronic.
- **State W-2:** due January 31 through Web Upload (EFW2) or eForms; uploading W-2s does not create the VA-6 [US-VAS5-013, US-VAS5-009].
- **UI quarterly report (VEC) [US-VAS5-014]:** due [[FACT:va.report.ui.quarterly_due=last day of month after quarter]], via ESS, eForm or Web Upload; amendments on FC-34; ESS access needs ID.me from 2026-08-01 [US-VAP6-001].
- **New hire [US-VAS5-006]:** to the Virginia New Hire Reporting Center within [[FACT:va.newhire.report_days=20]] days of hire (contractors within the same period of the contract).
- **Registration and agents:** R-1 / R-1H; VEC registration; PAR 101 and ESS TPA invitation [US-VAS5-013, US-VAS5-014, US-VAP51-007, US-VAP6-001].

**Parameters (statutory reporting)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `va.report.wh.semiweekly_threshold.monthly` | [[FACT:va.report.wh.semiweekly_threshold.monthly=1000]] | USD | from 2025-07-01 | US-VAS5-013 | <100 quarterly VA-5; 100-999 monthly (25th); >=1,000 semi-weekly VA-15 + VA-16 |
| `va.report.va6.due` | [[FACT:va.report.va6.due=January 31 (or 30 days after last wages)]] |  | from 2025-07-01 | US-VAS5-013 | W-2 upload EFW2 state code 51 does not create VA-6 |
| `va.report.ui.quarterly_due` | [[FACT:va.report.ui.quarterly_due=last day of month after quarter]] |  | from 2026-01-01 | US-VAS5-014 | ESS (ID.me from 2026-08-01) |
| `va.newhire.report_days` | [[FACT:va.newhire.report_days=20]] | days | from 2020-07-01 | US-VAS5-006 | independent contractors also within 20 days of contract |

## 6. Leave

- **Paid sick leave in 2026:** home health workers only (40.1-33.3) ([[FACT:va.leave.paid_sick.home_health_only=True]]) [US-VAS5-005].
- **General paid sick leave (40.1-33.6:1-:7, 2026 cc.1128/1129), enacted [US-VAS5-022]:** phase-in [[FACT:va.leave.paid_sick.general.start=2027-07-01 (50+); 2028-01-01 (25+); 2029-01-01 (all)]]; accrual one hour per [[FACT:va.leave.paid_sick.accrual_ratio_hours_worked=30]] hours worked with statutory caps; front-loading and qualifying PTO policies allowed; no payout at separation; paid at the regular rate without tip credit.
- **PFML benefits** from 2028 (Section 3).

**Parameters (leave)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `va.leave.paid_sick.home_health_only` | [[FACT:va.leave.paid_sick.home_health_only=True]] |  | 2026-01-01 to 2027-06-30 | US-VAS5-005 | 40.1-33.3 |
| `va.leave.paid_sick.general.start` | [[FACT:va.leave.paid_sick.general.start=2027-07-01 (50+); 2028-01-01 (25+); 2029-01-01 (all)]] |  | from 2027-07-01 | US-VAS5-022 | enacted 2026 cc.1128/1129 |
| `va.leave.paid_sick.accrual_ratio_hours_worked` | [[FACT:va.leave.paid_sick.accrual_ratio_hours_worked=30]] | hours | from 2027-07-01 | US-VAS5-022 | 40 h cap accrual and use; no payout |

## 7. Termination

- **Final pay [US-VAS5-003]:** [[FACT:va.final_pay.rule=next regular payday (discharge and resignation)]].
- **Accrued vacation:** no statute requires payout; depends on policy (negative finding; open point below). Sick leave from 2027: no payout [US-VAS5-022].
- **W-2 on termination:** on the day of the last payment of remuneration [US-VAS5-009]. VEC sends the separation report only when a claim is filed [US-VAS5-014].

**Parameters (termination)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `va.final_pay.rule` | [[FACT:va.final_pay.rule=next regular payday (discharge and resignation)]] |  | from 2026-07-01 | US-VAS5-003 |  |

**Open research points**

- ⚠️ RESEARCH-GAP: `va.term.vacation.payout` (non-blocking; research request filed under this key) - No statute on accrued vacation payout (negative finding). Closes with: DOLI Payment of Wage FAQ entry or AG opinion.

## 8. Benefits in kind and the taxable base

- **Conformity:** fixed-date conformity to the IRC as of [[FACT:va.bik.conformity.irc_date=2025-12-31]] (58.1-301, 2026 c.7); no exception touches employee exclusions, so Virginia follows federal treatment of retirement deferrals, cafeteria plans, HSA, transit and group-term life [US-VAS5-011]. Withholding follows the federal wage definition [US-VAS5-013].
- **UI wages** differ: cafeteria plans excluded, retirement deferrals included (Section 3). Treatment of the federal tips and overtime deductions (P.L. 119-21) is open (below).

**Parameters (benefits in kind and the taxable base)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `va.bik.conformity.irc_date` | [[FACT:va.bik.conformity.irc_date=2025-12-31]] |  | from 2026-01-01 | US-VAS5-011 | 2026 c.7 |

**Open research points**

- ⚠️ RESEARCH-GAP: `va.bik.pl119_21_deductions` (non-blocking; research request filed under this key) - Virginia treatment of federal tips/overtime deductions (P.L. 119-21) not established. Closes with: Virginia Tax 2026 conformity guidance or tax bulletin.

## 9. Deductions and garnishments

- **Deductions:** none without written signed authorisation, except taxes or legally required deductions [US-VAS5-003].
- **Garnishment (34-29) [US-VAS5-007]:** the lesser of [[FACT:va.garn.creditor.max_percent=25]] % of disposable earnings or the amount above forty times the greater of the federal or state minimum wage, a protected floor of [[FACT:va.garn.consumer.floor.weekly=510.80]] USD per week in 2026; stricter than the CCPA. Support orders: CCPA support percentages. State tax debts come within the limits from 2027-07-01 (2026 c.396).
- **Child-support withholding (20-79.3) [US-VAS5-010]:** the lesser of the ordered amount or the 34-29 maximum; employer fee up to [[FACT:va.garn.iwo.employer_fee.per_remittance=5]] USD per remittance; support has priority, prorated across orders; EFT mandatory for larger employers; notify DCSE on termination.

**Parameters (deductions and garnishments)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `va.garn.creditor.max_percent` | [[FACT:va.garn.creditor.max_percent=25]] | % | from 2021-07-01 | US-VAS5-007 | or excess over 40x greater of federal/state minimum |
| `va.garn.consumer.floor.weekly` | [[FACT:va.garn.consumer.floor.weekly=510.80]] | USD | 2026-01-01 to 2026-12-31 | US-VAS5-007 |  |
| `va.garn.iwo.employer_fee.per_remittance` | [[FACT:va.garn.iwo.employer_fee.per_remittance=5]] | USD | from 2026-01-01 | US-VAS5-010 | EFT within 4 days; mandatory EFT at 100+ employees |

## 10. Collective agreements and prevailing wage

- **Prevailing wage [US-VAS5-019, US-VAP51-006]:** public works for state agencies and covered institutions, and localities that adopt an ordinance; contracts of [[FACT:va.prevailing_wage.threshold=250,000]] USD or less are excluded; never below Davis-Bacon; certified payroll records and posting duties.

**Parameters (collective agreements and prevailing wage)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `va.prevailing_wage.threshold` | [[FACT:va.prevailing_wage.threshold=250,000]] | USD | from 2026-07-01 | US-VAS5-019 | contracts of 250,000 or less excluded |

## 11. Indexation

- **Minimum wage:** fixed by statute through 2028, CPI-U from 2029 [US-VAS5-001].
- **UI wage base:** statutory, not indexed [US-VASUI-001]. **PFML:** wage cap tied to the Social Security wage base [US-VAS5-016].
- **Income tax:** brackets and exemptions not indexed; the standard deduction is fixed by statute year by year [US-VAS5-018]. **Garnishment floor:** moves with the minimum wage.

## 12. Payroll data protection

- **SSN [US-VAS5-008]:** not visible on or through a mailed envelope ([[FACT:va.data.ssn.mailed_visible_prohibited=True]]), not published, not embedded in documents. No pay-statement truncation rule; 40.1-29(D) does not list the SSN. The W-2 carries the SSN [US-VAS5-009].

**Parameters (payroll data protection)**

| Parameter key | Value | Unit | Effective | Register id | Note |
|---|---|---|---|---|---|
| `va.data.ssn.mailed_visible_prohibited` | [[FACT:va.data.ssn.mailed_visible_prohibited=True]] |  | from 2008-07-01 | US-VAS5-008 |  |

**Open research points**

- ⚠️ RESEARCH-GAP: `va.data.cdpa_employee_exemption` (non-blocking; research request filed under this key) - CDPA employee-data exemption not read. Closes with: Va. Code 59.1-575 et seq.

## 13. Live legal change

- **2026-07-01:** good-faith defence (c.1040); pay transparency (HR, not payroll); prevailing-wage amendments [US-VAS5-003, US-VAS5-024, US-VAS5-019].
- **Tax year 2026:** IRC conformity date [US-VAS5-011].
- **2027-01-01:** minimum wage step; farm laborers covered [US-VAS5-001, US-VAS5-002]. **Tax year 2027:** statutory standard deduction (assessment; withholding formula not yet published) [US-VAS5-018].
- **2027-07-01:** general paid sick leave phase-in; state tax debts within garnishment limits [US-VAS5-022, US-VAS5-007].
- **2028:** minimum wage step; PFML contributions from 2028-04-01 [US-VAS5-001, US-VAS5-016].
- Listed but not read: amendments to 58.1-332 (resident credit) and 40.1-100 (child labour) (open point below) [US-VAS5-025].

**Open research points**

- ⚠️ RESEARCH-GAP: `va.live.unread_amendments` (non-blocking; research request filed under this key) - 2026 amendments to 58.1-332 and 40.1-100 listed but not read. Closes with: Those sections on law.lis.virginia.gov.

## 14. Special populations

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

## 15. Sources

Register ids cited in this annex resolve to `00-official-sources/legal-basis-register.csv`; the URL of each value is in the facts file. Authorities:

- Virginia Department of Labor and Industry (DOLI): US-VAS5-015
- Virginia Department of Taxation: US-VAS5-021
- Virginia Department of Taxation (Virginia Tax): US-VAS5-013
- Virginia Employment Commission (VEC): US-VAS5-014
- Virginia General Assembly (Code of Virginia): US-VAS5-002, US-VAS5-003, US-VAS5-004, US-VAS5-005, US-VAS5-007, US-VAS5-008, US-VAS5-011, US-VAS5-018
- Virginia General Assembly (Code of Virginia); DOLI Commissioner: US-VAS5-019, US-VAS5-022
- Virginia General Assembly (Code of Virginia); DSS Division of Child Support Enforcement: US-VAS5-010
- Virginia General Assembly (Code of Virginia); Virginia Employment Commission: US-VAS5-016
- Virginia General Assembly (Code of Virginia); Virginia New Hire Reporting Center (DSS Division of Child Support Enforcement): US-VAS5-006
- Virginia General Assembly (Code of Virginia, law.lis.virginia.gov): US-VAS5-001
- Virginia General Assembly (LIS): US-VAR3-001, US-VAR3-002, US-VAR3-003, US-VASUI-001

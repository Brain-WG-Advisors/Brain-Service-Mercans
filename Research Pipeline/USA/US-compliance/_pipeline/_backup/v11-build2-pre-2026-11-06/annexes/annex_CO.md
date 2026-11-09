# Annex CO: Colorado


This annex sets out the Colorado payroll rules for the 2026 build year. Read with Annex FED (the federal layer every employee carries) and Annex MULTI (which routes an employee to this State by work location, residence or UI localization). Every value is shown with its effective dates and its source (list at the end of the annex). Federal values are not repeated here.

Classification: T4. Besides State withholding, occupational privilege taxes (OPT) are flat monthly amounts on separate city returns.

## CO.1 Employment and labour code

State minimum wage USD [[FACT:co.minwage.hourly=15.16]] for 2026; Denver USD [[FACT:co.local_minwage.denver.hourly=19.29]]. Overtime: [[FACT:co.overtime.rule=1.5x after 40 h/week, 12 h/day or 12 consecutive hours; no comp time; agriculture after 48 h (56 highly seasonal)]]. Other local minimum wages and the 2027 State rate are open (gaps below); the 2027 figures in the proposed order are not used.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Minimum wage hourly | USD [[FACT:co.minwage.hourly=15.16]] | 2026-01-01 to 2026-12-31 |  | S1 |  |
| Minimum wage tip credit max | USD [[FACT:co.minwage.tip_credit.max=3.02]] | 2026-01-01 to 2026-12-31 |  | S1 | 2026 PAY CALC Order (7 CCR 1103-14, adopted 2025-12-08, Rule 1.2.1) agrees with the CDLE COMPS poster. |
| Minimum wage tipped cash wage | USD [[FACT:co.minwage.tipped.cash_wage=12.14]] | 2026-01-01 to 2026-12-31 |  | S1 | [[FACT:co.minwage.hourly=15.16]] - [[FACT:co.minwage.tip_credit.max=3.02]]; now quoted directly in the 2026 PAY CALC Order ([[FACT:co.minwage.tipped.cash_wage=12.14]]). 2026 PAY CALC Order (7 CCR 1103-14, adopted 2025-12-08, Rule 1.2.1) agrees with the CDLE COMPS poster. |
| Minimum wage minor reduction percent | [[FACT:co.minwage.minor_reduction.percent=15]] % | from 2026-01-01 |  | S2 | Unemancipated minors; not for some local minimum wages. |
| Local minimum wage denver hourly | USD [[FACT:co.local_minwage.denver.hourly=19.29]] | 2026-01-01 to 2026-12-31 |  | S3 | Derivation: 18.81 x 1.0256 (CPI-W Denver-Aurora-Lakewood H1/H1) = 19.2915 -> [[FACT:co.local_minwage.denver.hourly=19.29]]. |
| Local minimum wage denver tipped food beverage | USD [[FACT:co.local_minwage.denver.tipped_food_beverage=16.27]] | 2026-01-01 to 2026-12-31 |  | S3 | [[FACT:co.local_minwage.denver.hourly=19.29]] - [[FACT:co.minwage.tip_credit.max=3.02]], with at least [[FACT:co.minwage.tip_credit.max=3.02]] actual tips. |
| Overtime rule | [[FACT:co.overtime.rule=1.5x after 40 h/week, 12 h/day or 12 consecutive hours; no comp time; agriculture after 48 h (56 highly seasonal)]] | from 2026-01-01 |  | S2 |  |
| Overtime daily threshold hours | [[FACT:co.overtime.daily_threshold_hours=12]] hours | from 2026-01-01 |  | S2 |  |
| Exempt salary annual min | USD [[FACT:co.exempt.salary.annual_min=57,784]] | 2026-01-01 to 2026-12-31 |  | S1 | 2026 PAY CALC Order (7 CCR 1103-14, adopted 2025-12-08, Rule 1.2.1) agrees with the CDLE COMPS poster. |
| Rest break paid minutes per 4h | [[FACT:co.rest_break.paid_minutes_per_4h=10]] minutes | from 2026-01-01 |  | S2 | Unprovided rest time paid as extra pay; meal 30 min for shifts over 5 h. |
| Pay frequency rule | [[FACT:co.pay_frequency.rule=period no longer than one calendar month or 30 days; payday no later than 10 days after period close unless agreed (8-4-103(1)(a)); paydays posted]] | from 2025-08-06 |  | S4 |  |
| Payment method | [[FACT:co.payment.method=checks negotiable without discount; direct deposit only with voluntary authorisation; paycard only with free access to full net pay once per period or alternative (8-4-102)]] | from 2025-08-06 |  | S4 |  |
| Minimum wage minor hourly | USD [[FACT:co.minwage.minor.hourly=12.89]] | 2026-01-01 to 2026-12-31 |  | S1 | Non-emancipated minors, 15% below the full minimum ([[FACT:co.minwage.hourly=15.16]] x 0.85 = 12.886 -> [[FACT:co.minwage.minor.hourly=12.89]]). |
| Exempt salary weekly min | USD [[FACT:co.exempt.salary.weekly_min=1,111.23]] | 2026-01-01 to 2026-12-31 |  | S1 | EAP exemption salary; [[FACT:co.exempt.salary.weekly_min=1,111.23]] x 52 = 57,783.96 -> [[FACT:co.exempt.salary.annual_min=57,784]]/yr (co.exempt.salary.annual_min). |
| Exempt highly technical computer hourly min | USD [[FACT:co.exempt.highly_technical_computer.hourly_min=34.85]] | 2026-01-01 to 2026-12-31 |  | S1 |  |
| Exempt highly compensated annual min | USD [[FACT:co.exempt.highly_compensated.annual_min=130,014]] | 2026-01-01 to 2026-12-31 |  | S1 |  |
| Wage claim max amount | USD [[FACT:co.wage_claim.max_amount=7,500]] | 2026-01-01 to 2026-06-30 |  | S1 | Administrative wage-claim ceiling per employee. |
| Wage claim max amount | USD [[FACT:co.wage_claim.max_amount=13,000]] | 2026-07-01 to 2027-12-31 |  | S1 |  |

Not configured in this release [[GAP:RQ-491]]: Local minimum wage other cities: not established from an official source.

Not configured in this release [[GAP:RQ-496]]: Minimum wage hourly next year: not established from an official source.

## CO.2 Income tax withholding

**Method.** [[FACT:co.wh.method=annualise; subtract 5,500 (11,000 MFJ/QSS) or DR 0004 line 2; x 4.40%; divide by periods; add DR 0004 line 3; no supplemental rate, no rounding rule]]. Flat rate [[FACT:co.pit.rate.flat=4.4]] %. Wage base: [[FACT:co.wh.wages.conformity=wages subject to CO withholding = wages subject to federal withholding; federal exclusions generally flow through]]. The federal overtime deduction is not allowed for Colorado ([[FACT:co.wh.obbba_overtime_deduction.allowed=False]]).

```
annual_wages = period_wages x pay_periods
taxable      = annual_wages - allowance        # DR 1098 allowance, or DR 0004 line 2 when filed
period_tax   = max(0, taxable) x co_flat_rate / pay_periods + DR0004_line3
```

Allowance: single USD [[FACT:co.wh.std_allowance.dr1098.single=5,500]]; DR 0004 Table 1 (one job): single USD [[FACT:co.wh.dr0004.table1.single.1_job=14,000]], head of household USD [[FACT:co.wh.dr0004.table1.hoh.1_job=22,000]], married filing jointly USD [[FACT:co.wh.dr0004.table1.mfj.1_job=30,000]].

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| PIT rate flat | [[FACT:co.pit.rate.flat=4.4]] % | 2026-01-01 to 2026-12-31 |  | S5 | DR 0004 line 3 at [[FACT:co.pit.rate.flat=4.4]] %; method in DR 1098 2026. DR 1098 for 2027 not yet published. |
| Withholding standard allowance dr1098 single | USD [[FACT:co.wh.std_allowance.dr1098.single=5,500]] | 2026-01-01 to 2026-12-31 |  | S5 | DR 1098: subtract [[FACT:co.wh.std_allowance.dr1098.single=5,500]] (11,000 MFJ/QSS) or DR 0004 line 2. |
| Withholding dr0004 table1 single 1 job | USD [[FACT:co.wh.dr0004.table1.single.1_job=14,000]] | 2026-01-01 to 2026-12-31 |  | S5 | Single/MFS [[FACT:co.wh.dr0004.table1.single.1_job=14,000]] / 7,000 / 4,500 / 3,500 by jobs 1/2/3/4+. |
| Withholding dr0004 table1 HoH 1 job | USD [[FACT:co.wh.dr0004.table1.hoh.1_job=22,000]] | 2026-01-01 to 2026-12-31 |  | S5 | HoH [[FACT:co.wh.dr0004.table1.hoh.1_job=22,000]] / 11,000 / 7,500 / 5,500. |
| Withholding dr0004 table1 MFJ 1 job | USD [[FACT:co.wh.dr0004.table1.mfj.1_job=30,000]] | 2026-01-01 to 2026-12-31 |  | S5 | MFJ/QSS [[FACT:co.wh.dr0004.table1.mfj.1_job=30,000]] / 15,000 / 10,000 / 7,500. |
| Withholding obbba overtime deduction allowed | [[FACT:co.wh.obbba_overtime_deduction.allowed=False]] | from 2026-01-01 |  | S5 | Worksheet 1 removes the qualified overtime deduction from W-4 Step 4(b); confirmed in the Guide. |
| Withholding wages conformity | [[FACT:co.wh.wages.conformity=wages subject to CO withholding = wages subject to federal withholding; federal exclusions generally flow through]] | from 2026-01-01 |  | S6 |  |
| Withholding exempt W-4 copy threshold weekly | USD [[FACT:co.wh.exempt_w4_copy_threshold_weekly=200]] | from 2026-01-01 |  | S7 | W-4 claiming exempt with pay over [[FACT:co.wh.exempt_w4_copy_threshold_weekly=200]]/week and no DR 0004: copy to CDOR. |
| Withholding method | [[FACT:co.wh.method=annualise; subtract 5,500 (11,000 MFJ/QSS) or DR 0004 line 2; x 4.40%; divide by periods; add DR 0004 line 3; no supplemental rate, no rounding rule]] | from 2026-01-01 |  | S8 | DR 1098 (2026). |

## CO.2b Non-resident regime and reciprocity

Rules: [[FACT:co.nonres.rules=residents: all wages except where another state requires withholding; nonresidents: CO-source wages by days present; federal carve-outs rail/air (<=50% CO pay)/motor carrier/military/military spouse; telecommuters not taxed on work outside CO]].

**Resident / non-resident matrix (Colorado income tax)**

| Income type | Resident | Non-resident |
|---|---|---|
| Regular salary | Flat-rate method (CO.2) on all wages except where another State requires withholding | Flat-rate method on Colorado-source wages, by days present |
| Annual bonus / supplemental pay | No supplemental rate: aggregate with regular wages | Same, on the Colorado portion |
| Severance | Aggregate with regular wages (wage base = federal withholding wages) | Same, on the Colorado portion |
| Equity | Aggregate; federal classification of equity income in Annex FED (FED.2b) | Same, on the Colorado portion |
| Benefits in kind | Federal exclusions flow through (wage-base conformity) | Same, on the Colorado portion |
| Contractor pay | Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008] | Same |

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Non-resident rules | [[FACT:co.nonres.rules=residents: all wages except where another state requires withholding; nonresidents: CO-source wages by days present; federal carve-outs rail/air (<=50% CO pay)/motor carrier/military/military spouse; telecommuters not taxed on work outside CO]] | from 2026-01-01 |  | S6 | No reciprocity (Guide word search). |

## CO.2c Local wage taxes

Occupational privilege taxes are flat monthly amounts, one employee and one employer amount per employee whose monthly earnings in the city reach the threshold, filed on the city's own return. Denver figures come from the 2025 tax guide (gap below).

```
if monthly_city_earnings >= city_threshold: employee_OPT = city_employee_amount; employer_OPT = city_employer_amount
```

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Local OPT greenwood village employee monthly | USD [[FACT:co.local.opt.greenwood_village.employee_monthly=2]] | from 2026-01-01 |  | S9 | Employer [[FACT:co.local.opt.greenwood_village.employee_monthly=2]]/month; trigger 250+ earned in the month in the Village; multiple OPT cities: city where most work done, primary employer only. |
| Local OPT greenwood village employer monthly | USD [[FACT:co.local.opt.greenwood_village.employer_monthly=2]] | from 2026-01-01 |  | S9 |  |
| Local OPT greenwood village threshold monthly | USD [[FACT:co.local.opt.greenwood_village.threshold_monthly=250]] | from 2026-01-01 |  | S9 |  |
| Local OPT glendale employee monthly | USD [[FACT:co.local.opt.glendale.employee_monthly=5]] | from 2026-01-01 |  | S10 | Employer [[FACT:co.local.opt.glendale.employee_monthly=5]]/month; trigger more than 750 in the month. |
| Local OPT glendale employer monthly | USD [[FACT:co.local.opt.glendale.employer_monthly=5]] | from 2026-01-01 |  | S10 |  |
| Local OPT glendale threshold monthly | USD [[FACT:co.local.opt.glendale.threshold_monthly=750]] | from 2026-01-01 |  | S10 |  |
| Local OPT denver employee monthly | USD [[FACT:co.local.opt.denver.employee_monthly=5.75]] | from 2025-01-01 |  | S11 | Earnings >= 500/month; 2025 Tax Guide edition, 2026 edition not read. |
| Local OPT denver employer monthly | USD [[FACT:co.local.opt.denver.employer_monthly=4]] | from 2025-01-01 |  | S12 | 2026 edition not read. |
| Local OPT denver threshold monthly | USD [[FACT:co.local.opt.denver.threshold_monthly=500]] | from 2025-01-01 |  | S11 |  |
| Local minimum wage boulder county unincorporated hourly | USD [[FACT:co.local_minwage.boulder_county_unincorporated.hourly=16.82]] | 2026-01-01 to 2026-12-31 |  | S13 | Unincorporated Boulder County (ordinance amended November 2025). |
| Local minimum wage boulder county unincorporated hourly | USD [[FACT:co.local_minwage.boulder_county_unincorporated.hourly=17.43]] | from 2027-01-01 |  | S13 |  |
| Local minimum wage boulder city hourly | USD [[FACT:co.local_minwage.boulder_city.hourly=16.82]] | 2026-01-01 to 2026-12-31 |  | S14 | City of Boulder Ord. 8664 schedule: 15.57 (2025), [[FACT:co.local_minwage.boulder_city.hourly=16.82]] (2026), [[FACT:co.local_minwage.boulder_city.hourly=18.17]] (2027), CPI from 2028. |
| Local minimum wage boulder city hourly | USD [[FACT:co.local_minwage.boulder_city.hourly=18.17]] | from 2027-01-01 |  | S14 | From the Ord. 8664 FAQ written for the 2025 launch; no later City amendment found (the County lowered its own 2027 step to [[FACT:co.local_minwage.boulder_county_unincorporated.hourly=17.43]] in Nov 2025). Re-check before 2027-01-01. |

Not configured in this release [[GAP:RQ-493]]: Local OPT denver current edition: not established from an official source.

## CO.3 Social insurance: unemployment, disability, paid leave and payroll levies

Employer-only UI on wages up to the base (USD [[FACT:co.sui.wage_base=30,600]] for 2026; USD [[FACT:co.sui.wage_base=32,100]] for 2027). FAMLI paid family and medical leave: [[FACT:co.famli.total.rate=0.88]] % in 2026, split employee [[FACT:co.famli.employee.rate=0.44]] % and employer [[FACT:co.famli.employer.rate=0.44]] %; employers with up to [[FACT:co.famli.small_employer.max_employees=9]] employees owe only the employee share. 2027 total [[FACT:co.famli.total.rate=0.86]] %; the 2027 split is a blocking gap. The FAMLI wage cap follows the federal OASDI base (Annex FED).

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| FAMLI total rate | [[FACT:co.famli.total.rate=0.86]] % | from 2027-01-01 |  | S15 | 2027 total (CDLE FAMLI Business Brief 2026-09-30): 'The 2027 premium rate will be [[FACT:co.famli.total.rate=0.86]] % of wages, down from [[FACT:co.famli.total.rate=0.88]] % in 2026.' Split: co.famli.employee.rate / co.famli.employer.rate 2027 (derived, 50% cap). |
| SUI coverage | [[FACT:co.sui.coverage=follows FUTA thresholds: employer 20 weeks / 1,500 quarter; agricultural 10 workers in 20 weeks or 20,000 quarter; domestic 1,000 quarter; excluded commission insurance/real-estate agents, casual labour, part-time for exempt nonprofits, students at own school]] | from 2023-01-01 |  | S16 | [partial row] |
| SUI wage base next year | USD [[FACT:co.sui.wage_base.next_year=32,100]] | from 2027-01-01 |  | S17 |  |
| SUI new employer rate total | [[FACT:co.sui.new_employer.rate.total=3.05]] % | 2026-01-01 to 2026-12-31 |  | S18 | Sum of the base rate, the support surcharge and the solvency surcharge (no solvency surcharge in 2027) for non-construction employers; heavy-construction employers are not covered by this rate. |
| SUI new employer rate total | [[FACT:co.sui.new_employer.rate.total=1.7]] % | 2027-01-01 to 2027-12-31 |  | S18 | Sum of the base rate, the support surcharge and the solvency surcharge (no solvency surcharge in 2027) for non-construction employers; heavy-construction employers are not covered by this rate. |
| FAMLI total rate | [[FACT:co.famli.total.rate=0.88]] % | 2026-01-01 to 2026-12-31 |  | S19 | [[FACT:co.famli.employer.rate=0.44]] % employer + [[FACT:co.famli.employee.rate=0.44]] % employee on wages up to the SS wage base ([[FACT:fed.fica.oasdi.wage_base=184,500]]); statutory rate cap applies. |
| SUI wage base | USD [[FACT:co.sui.wage_base=30,600]] | 2026-01-01 to 2026-12-31 |  | S17 | Chargeable wage limit; [[FACT:co.sui.wage_base=32,100]] for 2027; employer only. |
| SUI wage base | USD [[FACT:co.sui.wage_base=32,100]] | from 2027-01-01 |  | S17 |  |
| FAMLI employee rate | [[FACT:co.famli.employee.rate=0.44]] % | 2026-01-01 to 2026-12-31 |  | S20 | Employee share never above 50% of the premium. |
| FAMLI employer rate | [[FACT:co.famli.employer.rate=0.44]] % | 2026-01-01 to 2026-12-31 |  | S20 |  |
| FAMLI small employer max employees | [[FACT:co.famli.small_employer.max_employees=9]] | from 2026-01-01 |  | S20 | Employers with [[FACT:co.famli.small_employer.max_employees=9]] or fewer employees remit only the [[FACT:co.famli.employee.rate=0.44]] % employee share (no employer share). |
| FAMLI employee rate | [[FACT:co.famli.employee.rate=0.43]] % | from 2027-01-01 |  | S15 | Maximum employee share 2027: [[FACT:co.famli.total.rate=0.86]] % x 50% = [[FACT:co.famli.employee.rate=0.43]] %. The [[FACT:co.famli.total.rate=0.86]] % total is on the CDLE bulletin of 2026-09-30; the 50% employee cap is the standing rule on famli.colorado.gov and is not restated in the bulletin. |
| FAMLI employer rate | [[FACT:co.famli.employer.rate=0.43]] % | from 2027-01-01 |  | S15 | [[FACT:co.famli.total.rate=0.86]] % - [[FACT:co.famli.employer.rate=0.43]] % employee share = [[FACT:co.famli.employer.rate=0.43]] %, for employers with 10+ employees that deduct the full employee share. Employers with 9 or fewer employees owe no employer share (co.famli.small_employer.max_employees, open-ended). |

Not configured in this release [[GAP:RQ-489]]: SUI wage base other state credit: not established from an official source.

Not configured in this release [[GAP:RQ-490]]: FAMLI split next year: not established from an official source.

## CO.4 Pay statement

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Payslip comps rule7 items | [[FACT:co.payslip.comps_rule7_items=total pay, rate, tips, credits and time worked (in addition to Wage Act items); kept 3 years]] | from 2026-01-01 |  | S2 |  |
| Payslip items | [[FACT:co.payslip.items=gross wages, withholdings/deductions, net wages, pay-period dates, employee name or SSN, employer name and address; at least monthly or each payment; records 3 years; fine up to 250 per employee per month max 7,500 (8-4-103(4))]] | from 2025-08-06 |  | S21 |  |

## CO.5 Statutory reporting

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Report withholding frequency | [[FACT:co.report.wh.frequency=< 7,000/yr quarterly (last day of month after quarter); 7,000-50,000 monthly (15th); >= 50,000 weekly Sat-Fri (3rd business day after Friday, EFT mandatory); zero returns required; paper DR 1094]] | from 2026-01-01 |  | S7 |  |
| Report withholding quarterly threshold | USD [[FACT:co.report.wh.quarterly_threshold=7,000]] | from 2026-01-01 |  | S7 |  |
| Report withholding weekly threshold | USD [[FACT:co.report.wh.weekly_threshold=50,000]] | from 2026-01-01 |  | S7 |  |
| Report W-2 | [[FACT:co.report.w2=due 31 January to employees and CDOR; e-file mandatory when federal e-file required (10+); Revenue Online .txt or XLSX template (10-100 employees, TY2026); paper with DR 1093; DR 0995 credit notice to every employee]] | from 2026-01-01 |  | S7 |  |
| Report W-2 xlsx template | [[FACT:co.report.w2.xlsx_template=RE: tax year, employer name, ID type, EIN, address; RS: ID type/EIN, names, SSN (999999999 if none), address, boxes 1, 2, 15, 16, 17; optional local 18-20, second state, dates, weeks, SUI wages]] | from 2026-01-01 |  | S22 |  |
| Report FAMLI quarterly | [[FACT:co.report.famli.quarterly=My FAMLI+ Employer, due one month after quarter end; file and API specs published; ITINs in bulk files from 2026-10-01]] | from 2026-01-01 |  | S23 |  |

Not configured in this release [[GAP:RQ-492]]: Report SUI quarterly: not established from an official source.

## CO.6 Leave

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Leave sick accrual hours worked per hour | [[FACT:co.leave.sick.accrual.hours_worked_per_hour=30]] hours | from 2022-01-01 |  | S23 | [partial row] HFWA 2023 text (partial row): cap 48 h/yr; carry over up to 48; front-load allowed; no payout; reinstated on rehire within 6 months; PHE supplement 80 h; amendments 2024-2026 unchecked. |
| Leave sick cap hours | [[FACT:co.leave.sick.cap_hours=48]] hours | from 2022-01-01 |  | S24 | [partial row] |
| Leave sick payout on separation | [[FACT:co.leave.sick.payout_on_separation=False]] | from 2022-01-01 |  | S24 | [partial row] |

Not configured in this release [[GAP:RQ-494]]: Leave sick amendments and payslip electronic consent: not established from an official source.

## CO.7 Termination and final pay

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Final pay rule | [[FACT:co.final_pay.rule=discharge: immediately (6 h after next workday start if payroll unit closed, 24 h if off-site); resignation: next regular payday; unclaimed check mailed after 60 days]] | from 2025-08-06 |  | S25 |  |
| Final pay penalty min | USD [[FACT:co.final_pay.penalty.min=1,000]] | from 2025-08-06 |  | S25 | Greater of 2x unpaid wages or [[FACT:co.final_pay.penalty.min=1,000]] if unpaid 14 days after written demand (8-4-109(3)(b)). |
| Final pay vacation payout | [[FACT:co.final_pay.vacation_payout=True]] | from 2025-08-06 |  | S25 | Earned and determinable vacation is wages (8-4-101(14)(a)(III)); owed even if fired for cause. Severance not wages. |

## CO.8 Benefits in kind and taxable wages

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Lodging credit weekly min | USD [[FACT:co.lodging_credit.weekly_min=25]] | from 2026-01-01 |  | S2 | Lodging credit 25-100/week; meals at cost or value; no uniform charges. |
| Lodging credit weekly max | USD [[FACT:co.lodging_credit.weekly_max=100]] | from 2026-01-01 |  | S2 |  |

## CO.9 Deductions and garnishments

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Deductions permitted | [[FACT:co.deductions.permitted=(a) required by law; (a.5) auto-enrolment retirement; (b) written agreement for loans/advances/goods/equipment; (c) theft after police report; (d) revocable authorisation; (e) unreturned property of terminated employee with notice within 10 days (8-4-105)]] | from 2025-08-06 |  | S26 |  |
| Garnishment creditor max percent | [[FACT:co.garn.creditor.max_percent=20]] % | from 2022-01-01 |  | S27 | Form 26 SC (R 1/22): exempt greater of 80% of disposable earnings or 40x/80x/86.67x/173.3x higher of state/federal MW; disposable earnings also deduct employer-provided health insurance (CO departure); support first; start first pay date >= 21 days after service. |
| Garnishment creditor weekly floor | USD [[FACT:co.garn.creditor.weekly_floor=606.40]] | 2026-01-01 to 2026-12-31 |  | S27 | 40 x [[FACT:co.minwage.hourly=15.16]]. |

## CO.10 Collective agreements and prevailing wage

Prevailing wage (public works) is an optional informational flag [US-OWN-009]: this guide documents prevailing-wage laws, thresholds and certified-payroll duties as an overlay, and the payroll build does not produce certified payroll reports.

| Parameter | Value | Effective | Level | Source | Qualification |
|---|---|---|---|---|---|
| Prevailing wage threshold | USD [[FACT:co.prevailing_wage.threshold=500,000]] | from 2026-01-01 |  | S28 | C.R.S. 24-92-201 ff.; weekly pay required. |

## CO.11 Indexation

The State minimum wage is CPI-indexed yearly (PAY CALC Order); Denver indexes on the local CPI-W; the exempt-salary thresholds are set yearly; the UI wage base follows statutory steps (USD [[FACT:co.sui.wage_base=30,600]] for 2026, USD [[FACT:co.sui.wage_base=32,100]] for 2027); the FAMLI rate is set yearly within a statutory cap; OPT amounts are fixed by ordinance.

## CO.12 Payroll data protection and records

The State data-protection statutes (C.R.S. 6-1-713, 6-1-713.5, 6-1-716) are open (gap below). No duty to truncate the SSN on the pay statement was found; the statement may show the SSN instead of the name (8-4-103(4)(e)).

Not configured in this release [[GAP:RQ-495]]: Data protection statutes: not established from an official source.

## CO.13 Live legal change

FAMLI 2027 [[FACT:co.famli.total.rate=0.86]] %; UI 2027 base [[FACT:co.sui.wage_base.next_year=32,100]] and 2027 new-employer rate [[FACT:co.sui.new_employer.rate.total=1.7]] %; OBBBA overtime decoupling; XLSX W-2 route; FAMLI ITIN files 2026-10-01; SecureSavings registration duty. The CDLE news page and the Colorado Register were not reviewed for this release.

## CO.14 Authority worked examples (oracle values)

No authority worked example is reproduced in this annex; recomputed withholding examples are in Module 12.

## CO.15 Special populations

- Domestic workers: UI follows the federal threshold.
- Agricultural workers: longer overtime thresholds (CO.1 overtime rule); migratory-labourer disclosures in the worker's language (8-4-117).
- Minors: [[FACT:co.minwage.minor_reduction.percent=15]] % below the State minimum for unemancipated minors (USD [[FACT:co.minwage.minor.hourly=12.89]] in 2026).
- Tipped employees: tip credit USD [[FACT:co.minwage.tip_credit.max=3.02]]; State cash wage USD [[FACT:co.minwage.tipped.cash_wage=12.14]]; Denver USD [[FACT:co.local_minwage.denver.tipped_food_beverage=16.27]]; tips are the employee's property.
- Clergy and statutory employees: no State rule beyond the federal one.
- Students: UI excludes students at their own school (not student nurses).
- Non-resident aliens: Colorado withholding applies without a valid TIN; FAMLI accepts ITINs.
- Government: the Wage Act excludes the State, counties, municipalities and school districts; the Healthy Families and Workplaces Act includes them and excludes federal employers.
- Military, military spouses and interstate transport workers: non-resident exemptions (CO.2b).
- Multistate: the Healthy Families and Workplaces Act covers all employees working in Colorado; the UI other-State credit is open (CO.3).

Not configured in this release [[GAP:RQ-515]]: The coverage thresholds that apply to these populations (quarterly cash-wage and headcount thresholds for UI coverage of domestic, agricultural and non-profit employment) are cited by statute only and are not established as values; the engine must not hard-code them until they are established.

## CO.16 Language

The Healthy Families and Workplaces Act notice must be in English and in the first language of a qualifying share of the workforce; the COMPS order and poster also in Spanish; the payslip is in English.

## CO.S Sources

| Ref | Instrument | Article / section | Authority |
|---|---|---|---|
| S1 | 2026 PAY CALC Order, 7 CCR 1103-14 (adopted 2025-12-08) | Rule 1.2.1 table rows (A)-(I); Rule 1.2.2 table row (A); Rule 2.2 | Colorado Department of Labor and Employment, Division of Labor Standards and … |
| S2 | CDLE COMPS Order #40 Poster & Notice (Colorado Overtime & Minimum Pay Standards), effective 1/1/2026 | COMPS Order #40 (7 CCR 1103-1) Rules 1.9, 2.2-2.4, 3, 4, 5.1, 5.2, 6, 7, 8 as summarised on the official poster | Colorado Department of Labor and Employment (CDLE), Division of Labor … |
| S3 | City and County of Denver, Department of Finance news release 'Denver Local Minimum Wage Adjusts to $[[FACT:co.local_minwage.denver.hourly=19.29]] per Hour for 2026' (D.R.M.C. Chapter 58, Art. 16) | D.R.M.C. 58-16 (minimum wage), CPI-W methodology paragraph | City and County of Denver, Department of Finance (enforcement: Denver Labor, … |
| S4 | Colorado Wage Act C.R.S. 8-4-103(1) pay periods/paydays; 8-4-102(2),(2.5) direct deposit and paycard; 8-4-107 payday notice | 8-4-102(2),(2.5); 8-4-103(1)(a); 8-4-107 | Colorado General Assembly (text published by CDLE) |
| S5 | DR 0004, 2026 Colorado Employee Withholding Certificate (rev. 10/29/25), with Worksheet 1, Table 1 Standard Allowance, Table 2 Child Tax Credit Allowance and … | Line 2 Annual Withholding Allowance; Table 1; Worksheet 1 lines 1-5 (3b qualified overtime); Table 2; Line 3 worksheet (x [[FACT:co.pit.rate.flat=4.40]]%) | Colorado Department of Revenue |
| S6 | Colorado Wage Withholding Tax Guide (Revised January 2026), Part 2: wages subject to withholding; federal conformity; OBBBA overtime | Part 2 'Wages', 'Overtime compensation', 'Exempt wages', table 'Exempt Wages for Nonresident Employees' | Colorado Department of Revenue (CDOR), Taxation Division |
| S7 | Colorado Wage Withholding Tax Guide (Revised January 2026), Parts 1, 3, 4: account, returns, deposits, W-2 filing | Part 1 (account, W-4 copy rule); Part 3 table 'Filing Frequency and Due Dates'; Part 4 (W-2, DR 1093, DR 0995) | Colorado Department of Revenue (CDOR), Taxation Division |
| S8 | DR 1098 2026 Colorado Withholding Worksheet for Employers (10/21/25) | Steps 1-2 | Colorado Department of Revenue |
| S9 | City of Greenwood Village, Occupational Privilege Tax (OPT) page | Tax Portions; How to Remit; Employees with Multiple Employers; PEO | City of Greenwood Village, Taxpayer Services |
| S10 | City of Glendale (CO), Occupational Privilege Tax page | OPT page; links to OPT ordinance and monthly/quarterly/annual returns | City of Glendale, Tax & Licensing |
| S11 | Denver Occupational Privilege Tax - employee share | Denver Tax Guide Topic 61 | CO official authority |
| S12 | Denver Occupational Privilege Tax - employer share | Denver Tax Guide Topic 61 | CO official authority |
| S13 | Boulder County - Local Minimum Wage (unincorporated; Ordinance amended November 2025) | Local Minimum Wage | Boulder County Board of County Commissioners |
| S14 | City of Boulder - Local Minimum Wage (Ordinance 8664) FAQ | FAQ 'What will the local minimum wage be in future years?' | City of Boulder |
| S15 | CDLE FAMLI Business Brief bulletin 2026-09-30 ('Heads-up: 2027 Premium Rate') | Heads-up: 2027 Premium Rate Effective Jan 1, 2027 | Colorado Department of Labor and Employment - FAMLI Division |
| S16 | US DOL OUI Comparison of State Unemployment Insurance Laws 2023, Chapter 1 Coverage, Tables 1-1 to 1-9 (Colorado entries) | Tables 1-1, 1-2, 1-3, 1-5, 1-6, 1-7 | US Department of Labor, Employment and Training Administration, Office of … |
| S17 | CDLE UI Premiums page - chargeable wage limits and 2027 rate tables | Premiums | Colorado Department of Labor and Employment, UI Division |
| S18 | CDLE Introductory Rates (new employers) 2026 and 2027 | Introductory Rates | Colorado Department of Labor and Employment, UI Division |
| S19 | Colorado FAMLI 2026 premiums |  | Colorado FAMLI Division (CDLE) |
| S20 | FAMLI Division - Employers page | Premium paragraphs; calculator note | Colorado Department of Labor and Employment, FAMLI Division |
| S21 | Colorado Wage Act C.R.S. 8-4-103(4),(4.5) (Revised Aug 6, 2025) | 8-4-103(4),(4.5) | Colorado Division of Labor Standards and Statistics (CDLE) |
| S22 | CDOR Year-End W-2 XLSX Info Return Template (2026 filing season) and instructions page (Revenue Online upload) | Template tabs Employer Info (RE), Employee Info (RS), Instructions; Withholding Submitter Access steps 1-5 | Colorado Department of Revenue |
| S23 | CDLE FAMLI Division, FAMLI Business Brief of 2026-09-30 (official employer bulletin) | Employer Actions & Deadlines; Heads-up: 2027 Premium Rate; Portal Report; Beyond FAMLI | Colorado Department of Labor and Employment, Family & Medical Leave Insurance … |
| S24 | Healthy Families and Workplaces Act C.R.S. 8-13.3-403, -404 (text revised Aug 7, 2023) | 8-13.3-403(1)(c),(2),(3),(5); 8-13.3-404(1) | Colorado General Assembly (text published by CDLE) |
| S25 | Colorado Wage Act C.R.S. 8-4-109(1) final pay; 8-4-101(14)(a)(III) vacation pay; 8-4-101(14)(b) severance | 8-4-101(14)(a)(III),(b); 8-4-109(1)(a)-(c),(3) | Colorado General Assembly (text published by CDLE) |
| S26 | Colorado Wage Act C.R.S. 8-4-105 permitted payroll deductions | 8-4-105(1)(a)-(e) | Colorado General Assembly (text published by CDLE) |
| S27 | Colorado Judicial Branch Form 26 SC, Writ of Continuing Garnishment (R: 1/22), incl. Calculation of the Amount of Exempt Earnings and Explanation of Wage … | Notice to Garnishee a-f; Calculation; Exemption Chart; Explanation (implements C.R.S. 13-54-104 and 13-54.5) | Colorado Judicial Branch |
| S28 | Colorado OSA Public Projects Defined / Prevailing Wage on Public Projects | C.R.S. 24-92-202; 24-92-201(5) | Colorado Office of the State Architect (DPA) |

# Module 7: Deductions, Exemptions & Benefits
*Purpose: To define rules for all items that adjust income or pay.*

## 7.1 Statutory Tax Reliefs, Deductions, and Exemptions

### Deliverable: For EACH statutory tax relief, deduction, exemption, or other tax advantage, provide: Name and Definition, Eligibility Rules, Statutory Limits & Amounts, Calculation Method, Application Point, Employee Declaration Requirements.

Application point: **W** = reduces federal withholding in payroll; **X** = excluded from wages in payroll; **A** = assessment only (employee's return), never a payroll deduction.

| Relief (name and definition) | Eligibility | Limits and amounts 2026 | Calculation method | Application point | Employee declaration | Fact |
|---|---|---|---|---|---|---|
| Standard deduction (built into the schedules' zero row) | Every employee on a 2020+ W-4 | USD [[FACT:fed.fit.std_deduction.single=16,100]] single / USD [[FACT:fed.fit.std_deduction.mfj=32,200]] MFJ / USD [[FACT:fed.fit.std_deduction.hoh=24,150]] HoH | Zero-rate first row plus line 1g (Module 6) | W | W-4 filing status | [US-FEDS5-010] |
| Pre-2020 withholding allowances | Employees still on a 2019-or-earlier W-4 | USD [[FACT:fed.fit.allowance.pre2020_value=4,300]] per allowance | Allowances x value subtracted from annual wages | W | Old W-4 | [US-FEDS5-001] |
| W-4 Step 3 credits (dependents) | Employee claim | Amount declared | Annual amount / pay periods subtracted from the period tax | W | W-4 Step 3 | [US-FEDS5-006] |
| W-4 Step 4(b) deductions, incl. qualified tips and overtime | Employee claim | Tips deduction cap USD [[FACT:fed.plaw119_21.qualified_tips.deduction_cap=25,000]]; overtime cap USD [[FACT:fed.plaw119_21.qualified_overtime.deduction_cap=12,500]] (USD [[FACT:fed.plaw119_21.qualified_overtime.deduction_cap_mfj=25,000]] MFJ) | Subtracted in Worksheet 1A line 1h; the deductions themselves operate at assessment | W (via Step 4(b)) / A | W-4 Step 4(b) | [US-FEDS5-030]; `practice.fed.pl119_21_withholding` [US-FEDS5-030] |
| Elective deferrals (401(k)-type) | Plan participants; catch-up by age | USD [[FACT:fed.retirement.401k.elective_deferral_limit=24,500]]; +USD [[FACT:fed.retirement.401k.catch_up_50=8,000]] (50+); +USD [[FACT:fed.retirement.401k.catch_up_60_63=11,250]] (60 to 63) | Salary reduction | X (income-tax wages only; FICA and FUTA wages remain, Module 3, Step 2) | Plan election | [US-FED-023] |
| SIMPLE plan deferral | Plan participants | USD [[FACT:fed.retirement.simple.deferral_limit=17,000]] | Salary reduction | X | Plan election | [US-FED-023] |
| Health savings account | [[FACT:fed.bik.hsa.conditions=Qualified individual covered by a high deductible health plan and by no other health coverage except permitted coverage; 2026 HDHP: deductible at least 1,700 self-only / 3,400 family, out-of-pocket max 8,500 / 17,000; no contributions after Medicare enrolment; employer contributions comparable for comparable coverage (35% excise otherwise) unless made through a cafeteria plan, where cafeteria nondiscrimination rules apply; partners and 2% S-corporation shareholders cannot make pre-tax contributions; report in W-2 box 12 code W.]] | USD [[FACT:fed.hsa.limit.self_only=4,400]] self-only / USD [[FACT:fed.hsa.limit.family=8,750]] family | Salary reduction or employer contribution | X | Election | [US-FED-024] |
| Health FSA | [[FACT:fed.bik.health_fsa.conditions=Offered only through a section 125 cafeteria plan; salary reduction for plan years beginning in 2026 capped at 3,400 (a plan without the cap is not a cafeteria plan); optional carryover instead of a grace period.]] | USD [[FACT:fed.bik.health_fsa.salary_reduction_cap=3,400]]; carry-over USD [[FACT:fed.bik.health_fsa.carryover_max=680]] | Salary reduction | X | Election | [US-FEDS5-008] |
| Dependent-care assistance | [[FACT:fed.bik.dependent_care.conditions=Written dependent care assistance program for employees only; services for a qualifying person and needed to let the employee work; exclusion up to 7,500 (3,750 married filing separately) and not above the smaller of the employee's or spouse's earned income; not for highly compensated employees unless the program is nondiscriminatory (section 129(d)).]] | USD [[FACT:fed.bik.dependent_care.exclusion=7,500]] (half for married filing separately) | Excluded up to the limit | X | Election | [US-FEDS5-008] |
| Educational assistance | [[FACT:fed.bik.educational_assistance.conditions=Separate written educational assistance program for employees only; nondiscriminatory in favour of highly compensated employees; not more than 5% of benefits to more-than-5% owners; no choice of cash instead; covers tuition, fees, books, supplies, equipment and qualified student-loan payments; exclusion up to 5,250 a year.]] | USD [[FACT:fed.bik.educational_assistance.exclusion=5,250]] | Excluded up to the limit | X | none established | [US-FEDS5-008] |
| Qualified parking / transit | [[FACT:fed.bik.transportation.conditions=Commuter highway vehicle and transit passes up to 340 a month and qualified parking up to 340 a month are excluded; not available to 2% S-corporation shareholders; cannot be offered through a cafeteria plan.]] | USD [[FACT:fed.bik.parking.monthly_exclusion=340]] / USD [[FACT:fed.bik.transit.monthly_exclusion=340]] a month each | Excess over the monthly limit is wages | X | none established | [US-FEDS5-008] |
| Group-term life insurance | Employer-provided group-term cover | Coverage up to USD [[FACT:fed.bik.group_term_life.excluded_coverage=50,000]] excluded | Imputed cost of excess cover (§7.2) | X (excess: FICA wages) | none | [US-FEDS5-008] |
| Trump-account employer contribution | [[FACT:fed.bik.trump_account.conditions=From 2026-07-04 the employer may contribute up to 2,500 a year toward the 5,000 Trump account limit of an employee or dependent, excluded from gross income if paid under a separate written plan for the exclusive benefit of employees meeting requirements similar to section 129(d)(2), (3), (6), (7) and (8).]] | USD [[FACT:fed.bik.trump_account.employer_contribution_max=2,500]] from 2026-07-04 | Excluded up to the limit; W-2 code TA | X | none established | [US-FEDS5-030] |
| Foreign earned income exclusion | US citizens and residents working abroad | USD [[FACT:fed.feie.amount=132,900]] | Employer may stop withholding on the employee's statement: [[FACT:fed.citizen_abroad.form673=Employer may stop FIT withholding on Form 673 statement (FEIE/housing); citizens only]] | W | Employee statement (Form 673) | [US-FED-025]; [US-FEDR3-007] |
| Treaty exemption (nonresident alien) | Treaty resident with personal-service income | Per treaty | [[FACT:fed.fit.nra.treaty_exempt.reporting=Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S (not W-2 box 1); 2026 Forms 1042-S due 2027-03-15 and must be e-filed via IRIS]] | X | Form 8233 | [US-FEDS5-016] |

Federal bases of each exclusion (Pub. 15-B (2026) Table 2-1):

| Exclusion | Federal income-tax wages | FICA wages | FUTA wages | Source |
|---|---|---|---|---|
| Health savings account | [[FACT:fed.base.hsa_contribution.fit=excluded for a qualified individual up to the HSA contribution limit (employer or section 125 salary-reduction contributions)]] | [[FACT:fed.base.hsa_contribution.fica=excluded for a qualified individual up to the HSA contribution limit (employer or section 125 salary-reduction contributions)]] | [[FACT:fed.base.hsa_contribution.futa=excluded for a qualified individual up to the HSA contribution limit (employer or section 125 salary-reduction contributions)]] | [US-FEDS5-008] |
| Health FSA and other Section 125 health benefits | [[FACT:fed.base.section125_health.fit=excluded]] | [[FACT:fed.base.section125_health.fica=excluded]] | [[FACT:fed.base.section125_health.futa=excluded]] | [US-FEDS5-008] |
| Dependent-care assistance | [[FACT:fed.base.dependent_care.fit=excluded up to 7,500 a year (3,750 married filing separately)]] | [[FACT:fed.base.dependent_care.fica=excluded up to 7,500 a year (3,750 married filing separately)]] | [[FACT:fed.base.dependent_care.futa=excluded up to 7,500 a year (3,750 married filing separately)]] | [US-FEDS5-008] |
| Educational assistance | [[FACT:fed.base.educational_assistance.fit=excluded up to 5,250 a year under a qualifying educational assistance program]] | [[FACT:fed.base.educational_assistance.fica=excluded up to 5,250 a year under a qualifying educational assistance program]] | [[FACT:fed.base.educational_assistance.futa=excluded up to 5,250 a year under a qualifying educational assistance program]] | [US-FEDS5-008] |
| Qualified parking / transit | [[FACT:fed.base.transportation.fit=excluded up to 340 a month for commuter highway vehicle and transit passes and 340 a month for qualified parking]] | [[FACT:fed.base.transportation.fica=excluded up to 340 a month for commuter highway vehicle and transit passes and 340 a month for qualified parking]] | [[FACT:fed.base.transportation.futa=excluded up to 340 a month for commuter highway vehicle and transit passes and 340 a month for qualified parking]] | [US-FEDS5-008] |
| Trump-account employer contribution | Excluded up to the limit in the table above [US-FEDR3-005] | Not configured in this release [[GAP:RQ-591]]: FICA treatment of the employer contribution is not established from an official source. | Not configured in this release [[GAP:RQ-591]]: FUTA treatment of the employer contribution is not established from an official source. | [US-FEDS5-030] |

State conformity differs per State (examples: `ca.hsa.conforms` [US-CAS5-019]; `al.hsa.conforms` [US-ALS5-020]; `nj.bik.nj.hsa.excluded` [US-NJS5-006]; `ms.bik.section125.excluded` [US-MSS5-004]); see annexes.

### Are salary sacrifice arrangements allowed?

Yes, as salary-reduction arrangements: elective deferrals to retirement plans and salary reductions to a health FSA (cap USD [[FACT:fed.bik.health_fsa.salary_reduction_cap=3,400]]) or HSA within the limits above [US-FEDS5-010]. Which federal base each reduction lowers is in Module 3, Step 2 [US-FEDS5-029]; the State bases are in the State annexes.

### List common types of post-tax deductions and any specific ordering rules or limitations.

| Deduction | Rule | Fact |
|---|---|---|
| Child-support income withholding order (IWO) | [[FACT:fed.iwo.priority=IWO for support ranks before other garnishments, except an IRS levy served before the underlying support order]] | [US-FEDS5-014] |
| Creditor garnishments, federal tax levies | Limits of §7.3 | `fed.ccpa.*`; `fed.levy.*` |
| State programme shares classified as after-tax | Example: `me.pfml.employee_deduction.after_tax` [US-MES5-025] | [US-MES5-025] |
| Workers' compensation employee shares | New Mexico fee USD [[FACT:nm.wc.admin_fee.employee.quarterly=2.25]] per quarter; Washington [[FACT:wa.wc.employee_deduction.rule=50% x (Stay-at-Work + Medical Aid + Supplemental Pension) per hour per risk class]] (coverage row `work_accident_occupational_disease` [US-NMR3-001, US-FEDS5-029]) | [US-NMR3-001]; [US-WAS5-019] |
| Voluntary after-tax deductions (union dues, loans, charitable) | Employer policy and State wage-deduction law (annexes) | annexes |

Not configured in this release [[GAP:RQ-571]]: The CCPA definition of disposable earnings (which deductions are 'required by law') and the resulting order of voluntary deductions vs garnishments are not established from an official source.

### List any income types that are statutorily exempt from income tax.

| Income | Treatment | Fact |
|---|---|---|
| Fringe benefits within the exclusions of §7.1 | Excluded up to the limits | [US-FEDS5-008] |
| Minister's parsonage allowance | [[FACT:fed.minister.withholding=No FIT, social security or Medicare withholding (SE tax; voluntary FIT withholding agreement allowed); parsonage allowance excluded from W-2 box 1]] | [US-FED-030] |
| Workers' compensation benefits | Not employer wages (coverage row `work_accident_occupational_disease` [US-NMR3-001, US-FEDS5-029]) | |
| State PFML benefits | Paid by the State, not employer payroll (coverage row `maternity_paternity_parental` [US-FEDS5-026, US-FEDS5-007, US-WAS5-015, US-MAS5-012]) | |
| Foreign earned income (US citizens and residents abroad) | Excluded up to USD [[FACT:fed.feie.amount=132,900]] | [US-FED-025] |
| Treaty-exempt wages of a nonresident alien | Reported on Form 1042-S, not W-2 box 1 | [US-FEDS5-016] |

## 7.2 Benefits in Kind (BIK)

### Are non-cash benefits taxed via the standard payroll system, or a separate employer-paid regime?

Through the standard payroll system. The facts carry no separate employer fringe-benefit tax: a non-excluded benefit is added to the employee's wages and taxed with them, and specific benefits are excluded up to limits [US-FEDS5-008].

### What is the definition of fringe benefits and how is the taxable amount evaluated?

A fringe benefit is any non-cash form of pay. Group-term life insurance is valued by the IRS table below; other taxable benefits by the general valuation rule that follows it; excluded benefits are excluded up to their limits (§7.1):

**Group-term life insurance above USD [[FACT:fed.bik.group_term_life.excluded_coverage=50,000]].** Monthly cost per USD 1,000 of excess coverage (Pub. 15-B Table 2-2):

| Age band | USD per 1,000 per month |
|---|---|
| Under 25 | [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.under_25=0.05]] |
| 25 to 29 | [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.25_29=0.06]] |
| 30 to 34 | [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.30_34=0.08]] |
| 35 to 39 | [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.35_39=0.09]] |
| 40 to 44 | [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.40_44=0.10]] |
| 45 to 49 | [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.45_49=0.15]] |
| 50 to 54 | [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.50_54=0.23]] |
| 55 to 59 | [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.55_59=0.43]] |
| 60 to 64 | [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.60_64=0.66]] |
| 65 to 69 | [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.65_69=1.27]] |
| 70 and over | [[FACT:fed.bik.group_term_life.monthly_cost_per_1000.70_plus=2.06]] |

Source [US-FEDS5-008].

```
imputed_month = (coverage - [[FACT:fed.bik.group_term_life.excluded_coverage=50,000]]) / 1000 x rate_for_age_band
```

Not configured in this release [[GAP:RQ-536]]: The 2026 business standard mileage rate is not printed in Pub. 15-B (FED OQ 7).

**Other taxable fringe benefits.** Valuation and timing (Pub. 15-B (2026) sections 3 and 4):

| Element | Rule | Source |
|---|---|---|
| General valuation rule | [[FACT:fed.bik.valuation.general_rule=Fair market value: the amount an employee would have to pay a third party in an arm's-length transaction to buy or lease the benefit, on all facts and circumstances; neither the employee's view of the value nor the employer's cost determines it.]] | [US-FEDS5-008] |
| Taxable amount | [[FACT:fed.bik.valuation.taxable_amount=Include in pay the amount by which the value of the benefit exceeds the sum of any amount the law excludes and any amount the recipient paid for it.]] | [US-FEDS5-008] |
| Employer-provided vehicle | [[FACT:fed.bik.vehicle.valuation_methods=Employer-provided vehicle personal use: fair market value (lease cost of a comparable vehicle) or one of three special rules: cents-per-mile, commuting (commuting use only) and lease value.]] | [US-FEDS5-008] |
| Vehicle commuting rule | USD [[FACT:fed.bik.vehicle.commuting_rule.value_per_one_way=1.50]] for each one-way commute | [US-FEDS5-008] |
| When the benefit is treated as paid | [[FACT:fed.bik.treated_as_paid=Taxable noncash fringe benefits may be treated as paid per pay period, quarter, half-year, year or other basis, at least annually and all by 31 December; special accounting rule: benefits actually provided in November-December may be treated as paid in the next year. Not for transfers of investment-type personal property or real property (actual transfer date).]] | [US-FEDS5-008] |

### If a separate FBT regime exists, describe it in detail.

Not applicable: no separate fringe-benefit tax appears in the facts (previous answers).

### What is the calculation logic for fringe benefit tax?

Not applicable as a separate tax. Taxable benefits are added to the relevant bases and taxed with cash wages (Module 3, Step 1).

### Are benefits-in-kind also subject to withholding tax?

Group-term life cost above the excluded coverage is FICA wages and income-tax withholding is not required [US-FEDS5-008]. Other taxable benefits: [[FACT:fed.bik.withholding.method=Add the value to regular wages for the payroll period and withhold on the total, or withhold at the 22% supplemental flat rate (37% on supplemental wages over 1 million); income tax, social security and Medicare are withheld on the date(s) the benefit is treated as paid.]] [US-FEDS5-008]. Vehicle benefit: the employer may elect not to withhold income tax on the value of an employee's personal use of a vehicle [US-FEDS5-008]. Nonresident aliens: Module 6.

### Which benefits-in-kind must be processed via payroll, and which require declarations?

| Benefit | Payroll processing | Fact |
|---|---|---|
| Group-term life excess cover | Imputed monthly through payroll (FICA wages) | [US-FEDS5-008] |
| Employer Trump-account contribution | Reported on the W-2 code TA | [US-FEDS5-007] |
| Moving expenses, bicycle commuting reimbursements | Wages (exclusions eliminated) | `fed.bik.moving_and_bicycle.excluded` [US-FEDS5-008] |
| Parking / transit above the monthly limit | Excess added to wages | [US-FEDS5-008] |
| Health FSA, HSA, dependent care | Employee election before the plan year | elections (§7.1) |

## 7.3 Garnishments and Court Orders

### What are the rules for processing statutory deductions like child support, court-ordered fines, or tax levies?

| Order | Rule | Fact |
|---|---|---|
| Child-support IWO, interstate | [[FACT:multi.iwo.governing_law=Interstate IWO: apply the income-withholding law of the State of the obligor's PRINCIPAL PLACE OF EMPLOYMENT for the employer fee, the maximum withheld, timing, priority among obligees and terms not in the order]]; remit within [[FACT:multi.iwo.remittance_business_days=7]] business days | [US-MULTIS5-007] |
| IWO form | OMB approval valid to [[FACT:fed.iwo.omb_expiry=2029-08-31]] | [US-FEDS5-028] |
| Federal tax levy | Exempt amount table below; the employer pays the rest of the take-home pay to the IRS | [US-FEDS5-014] |
| Creditor garnishment | CCPA limits below; stricter State law applies | [US-FEDS5-023] |

Not configured in this release [[GAP:RQ-528]]: States go live with the revised (gig-field) IWO/e-IWO within the one-year extension; dates not known (FED OQ 8).

### Is there a statutory priority order if an employee has multiple garnishments?

Yes: [[FACT:fed.iwo.priority=IWO for support ranks before other garnishments, except an IRS levy served before the underlying support order]] [US-FEDS5-014]. Among support obligees and for fees and timing, the law of the obligor's principal place of employment governs [US-MULTIS5-007]. State examples: Alabama gives the IWO priority and remits within [[FACT:al.garn.child_support.remit_business_days=7]] business days [US-ALS5-013]; Connecticut remits within [[FACT:ct.garn.child_support.remit_business_days=7]] business days [US-CTS5-025]; California [[FACT:ca.garn.child_support.remit_business_days=7]] business days [US-CAS5-022]; Arizona [[FACT:az.garn.child_support.remit_business_days=2]] business days [US-AZS5-018].

### Are there protected earnings limits?

**Federal (CCPA)** on disposable earnings:

| Order | Maximum withheld | Fact |
|---|---|---|
| Ordinary creditor | Lesser of [[FACT:fed.ccpa.max_rate=25]]% of weekly disposable earnings or the excess over USD [[FACT:fed.ccpa.protected_weekly=217.50]] a week | [US-FEDS5-023] |
| Support, employee supporting a spouse or child | [[FACT:fed.ccpa.support.max_rate.with_dependents=50]]% (+[[FACT:fed.ccpa.support.arrears_addon=5]] points with arrears over 12 weeks) | [US-FEDS5-023] |
| Support, no other dependants | [[FACT:fed.ccpa.support.max_rate.without_dependents=60]]% (+[[FACT:fed.ccpa.support.arrears_addon=5]] points with arrears over 12 weeks) | [US-FEDS5-023] |

**Federal tax levy: amounts exempt from levy, 2026 (Pub. 1494)**

| Status | Daily | Weekly | Biweekly | Semimonthly | Monthly |
|---|---|---|---|---|---|
| Single / MFS, no dependent | [[FACT:fed.levy.exempt.single_0dep.daily=61.92]] | [[FACT:fed.levy.exempt.single_0dep.weekly=309.62]] | [[FACT:fed.levy.exempt.single_0dep.biweekly=619.23]] | [[FACT:fed.levy.exempt.single_0dep.semimonthly=670.83]] | [[FACT:fed.levy.exempt.single_0dep.monthly=1,341.67]] |
| Each dependent adds | [[FACT:fed.levy.exempt.per_dependent.daily=20.38]] | [[FACT:fed.levy.exempt.per_dependent.weekly=101.92]] | [[FACT:fed.levy.exempt.per_dependent.biweekly=203.85]] | [[FACT:fed.levy.exempt.per_dependent.semimonthly=220.83]] | [[FACT:fed.levy.exempt.per_dependent.monthly=441.67]] |
| MFJ, no dependent | | [[FACT:fed.levy.exempt.mfj_0dep.weekly=619.23]] | | | [[FACT:fed.levy.exempt.mfj_0dep.monthly=2,683.33]] |
| Head of household, no dependent | | [[FACT:fed.levy.exempt.hoh_0dep.weekly=464.42]] | | | |

Source [US-FEDS5-014].

**State limits stricter than the CCPA (examples; the more protective rule governs)**

| State | Creditor garnishment limit | Fact |
|---|---|---|
| AK | Exempt: greater of USD [[FACT:ak.garn.exempt.weekly=473]] a week or a share of disposable earnings | [US-AKS5-009] |
| AL | [[FACT:al.garn.exempt.percent=75]]% of resident wages exempt | [US-ALS5-013] |
| AZ | Lesser of [[FACT:az.garn.creditor.max_percent=10]]% of disposable earnings or the excess over [[FACT:az.garn.creditor.minwage_multiple=60]] x the highest applicable minimum wage | [US-AZS5-016] |
| CA | Lesser of [[FACT:ca.garn.creditor.max_percent=20]]% of disposable earnings or [[FACT:ca.garn.creditor.excess_percent=40]]% of disposable earnings above [[FACT:ca.garn.creditor.minwage_multiple.weekly=48]] x the minimum wage (weekly) | [US-CAS5-013] |
| CO | Maximum [[FACT:co.garn.creditor.max_percent=20]]% of disposable earnings; weekly floor USD [[FACT:co.garn.creditor.weekly_floor=606.40]] | [US-COS5-009] |
| CT | Lesser of [[FACT:ct.garn.creditor.max_percent=25]]% or the excess over USD [[FACT:ct.garn.creditor.weekly_protected=677.60]] a week | [US-CTS5-024] |
| DC | [[FACT:dc.garn.creditor.rule=max 25% of weekly disposable wages exceeding 40 x DC minimum wage; one attachment at a time (16-572)]] | [US-DCS5-006] |

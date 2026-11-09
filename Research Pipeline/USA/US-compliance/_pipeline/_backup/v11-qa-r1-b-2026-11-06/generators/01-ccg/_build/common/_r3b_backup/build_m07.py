# -*- coding: utf-8 -*-
"""Build 01-ccg/modules/m07_deductions.md from the CCG facts (US build)."""
from ccglib import *

U = "m07_deductions"
set_unit(U)
o = []
A = o.append
ON = "2026-06-30"
G = "⚠️ RESEARCH-GAP (non-blocking): see request `fed.bik.exclusion_conditions`"

A("# Module 7: Deductions, Exemptions & Benefits")
A("*Purpose: To define rules for all items that adjust income or pay.*")

# ---------------------------------------------------------------- 7.1
A(H(2, "7.1 Statutory Tax Reliefs, Deductions, and Exemptions"))
A(H(3, "Deliverable: For EACH statutory tax relief, deduction, exemption, or other tax advantage, provide: Name and Definition, Eligibility Rules, Statutory Limits & Amounts, Calculation Method, Application Point, Employee Declaration Requirements."))
A("Application point: **W** = reduces federal withholding in payroll; **X** = excluded from wages in payroll; "
  "**A** = assessment only (employee's return), never a payroll deduction.")
A("")
A("| Relief (name and definition) | Eligibility | Limits and amounts 2026 | Calculation method | Application point | Employee declaration | Fact |")
A("|---|---|---|---|---|---|---|")
A(f"| Standard deduction (built into the schedules' zero row) | Every employee on a 2020+ W-4 | USD {T('fed.fit.std_deduction.single')} single / USD {T('fed.fit.std_deduction.mfj')} MFJ / USD {T('fed.fit.std_deduction.hoh')} HoH | Zero-rate first row plus line 1g (Module 6) | W | W-4 filing status | {R('fed.fit.std_deduction.single')} |")
A(f"| Pre-2020 withholding allowances | Employees still on a 2019-or-earlier W-4 | USD {T('fed.fit.allowance.pre2020_value')} per allowance | Allowances x value subtracted from annual wages | W | Old W-4 | {R('fed.fit.allowance.pre2020_value')} |")
A(f"| W-4 Step 3 credits (dependents) | Employee claim | Amount declared | Annual amount / pay periods subtracted from the period tax | W | W-4 Step 3 | {R('fed.w4.input_fields')} |")
A(f"| W-4 Step 4(b) deductions, incl. qualified tips and overtime | Employee claim | Tips deduction cap USD {T('fed.plaw119_21.qualified_tips.deduction_cap')}; overtime cap USD {T('fed.plaw119_21.qualified_overtime.deduction_cap')} (USD {T('fed.plaw119_21.qualified_overtime.deduction_cap_mfj')} MFJ) | Subtracted in Worksheet 1A line 1h; the deductions themselves operate at assessment | W (via Step 4(b)) / A | W-4 Step 4(b) | {R('fed.plaw119_21.qualified_tips.deduction_cap')}; {K('practice.fed.pl119_21_withholding')} |")
A(f"| Elective deferrals (401(k)-type) | Plan participants; catch-up by age | USD {T('fed.retirement.401k.elective_deferral_limit')}; +USD {T('fed.retirement.401k.catch_up_50')} (50+); +USD {T('fed.retirement.401k.catch_up_60_63')} (60 to 63) | Salary reduction | X (bases: request `fed.retirement.pretax.tax_treatment`) | Plan election | {R('fed.retirement.401k.elective_deferral_limit')} |")
A(f"| SIMPLE plan deferral | Plan participants | USD {T('fed.retirement.simple.deferral_limit')} | Salary reduction | X | Plan election | {R('fed.retirement.simple.deferral_limit')} |")
A(f"| Health savings account | {G} | USD {T('fed.hsa.limit.self_only')} self-only / USD {T('fed.hsa.limit.family')} family | Salary reduction or employer contribution | X | Election | {R('fed.hsa.limit.self_only')} |")
A(f"| Health FSA | {G} | USD {T('fed.bik.health_fsa.salary_reduction_cap')}; carry-over USD {T('fed.bik.health_fsa.carryover_max')} | Salary reduction | X | Election | {R('fed.bik.health_fsa.salary_reduction_cap')} |")
A(f"| Dependent-care assistance | {G} | USD {T('fed.bik.dependent_care.exclusion')} (half for married filing separately) | Excluded up to the limit | X | Election | {R('fed.bik.dependent_care.exclusion')} |")
A(f"| Educational assistance | {G} | USD {T('fed.bik.educational_assistance.exclusion')} | Excluded up to the limit | X | none in the facts | {R('fed.bik.educational_assistance.exclusion')} |")
A(f"| Qualified parking / transit | {G} | USD {T('fed.bik.parking.monthly_exclusion')} / USD {T('fed.bik.transit.monthly_exclusion')} a month each | Excess over the monthly limit is wages | X | none in the facts | {R('fed.bik.parking.monthly_exclusion')} |")
A(f"| Group-term life insurance | Employer-provided group-term cover | Coverage up to USD {T('fed.bik.group_term_life.excluded_coverage')} excluded | Imputed cost of excess cover (§7.2) | X (excess: FICA wages) | none | {R('fed.bik.group_term_life.excluded_coverage')} |")
A(f"| Trump-account employer contribution | {G} | USD {T('fed.bik.trump_account.employer_contribution_max')} from {D('fed.bik.trump_account.employer_contribution_max')} | Excluded up to the limit; W-2 code TA | X | none in the facts | {R('fed.bik.trump_account.employer_contribution_max')} |")
A(f"| Foreign earned income exclusion | US citizens and residents working abroad | USD {T('fed.feie.amount')} | Employer may stop withholding on the employee's statement: {Q('fed.citizen_abroad.form673')} | W | Employee statement (Form 673) | {R('fed.feie.amount')}; {R('fed.citizen_abroad.form673')} |")
A(f"| Treaty exemption (nonresident alien) | Treaty resident with personal-service income | Per treaty | {Q('fed.fit.nra.treaty_exempt.reporting')} | X | Form 8233 | {R('fed.fit.nra.treaty_exempt.reporting')} |")
A("")
A(GAP("fed.bik.exclusion_conditions",
      "the eligibility conditions of each fringe exclusion (HSA, health FSA, dependent care, educational assistance, parking/transit, Trump account) and their FICA/FUTA scope are not in the facts",
      "Per Pub. 15-B (2026) and Pub. 969, what are the eligibility conditions of each exclusion (HSA with HDHP coverage, health FSA under a cafeteria plan, dependent care sec.129, educational assistance sec.127, qualified transportation sec.132(f), Trump account sec.128) and is each excluded from income-tax withholding, FICA and FUTA?",
      "CCG m07 §7.1 eligibility column empty for six reliefs; WTC Subject-to-X flags for these benefits have no source",
      "benefits_in_kind", tier="A.2", shape="matrix exclusion x (conditions, FIT, FICA, FUTA) with page"))
A("")
A("State conformity differs per State (examples: "
  f"{K('ca.hsa.conforms')}; {K('al.hsa.conforms')}; {K('nj.bik.nj.hsa.excluded')}; {K('ms.bik.section125.excluded')}); see annexes.")
A(H(3, "Are salary sacrifice arrangements allowed?"))
A("Yes, as salary-reduction arrangements: elective deferrals to retirement plans and salary reductions to a health "
  f"FSA (cap USD {T('fed.bik.health_fsa.salary_reduction_cap')}) or HSA within the limits above {R('fed.bik.health_fsa.salary_reduction_cap')}. "
  "Which federal and State bases each reduction lowers is research request `fed.retirement.pretax.tax_treatment` "
  "(Module 3) and the State annexes.")
A(H(3, "List common types of post-tax deductions and any specific ordering rules or limitations."))
A("| Deduction | Rule | Fact |")
A("|---|---|---|")
A(f"| Child-support income withholding order (IWO) | {Q('fed.iwo.priority')} | {R('fed.iwo.priority')} |")
A("| Creditor garnishments, federal tax levies | Limits of §7.3 | `fed.ccpa.*`; `fed.levy.*` |")
A(f"| State programme shares classified as after-tax | Example: {K('me.pfml.employee_deduction.after_tax')} | {R('me.pfml.employee_deduction.after_tax')} |")
A(f"| Workers' compensation employee shares | New Mexico fee USD {T('nm.wc.admin_fee.employee.quarterly', on=ON)} per quarter; Washington {Q('wa.wc.employee_deduction.rule')} ({COV('work_accident_occupational_disease')}) | {R('nm.wc.admin_fee.employee.quarterly', on=ON)}; {R('wa.wc.employee_deduction.rule')} |")
A("| Voluntary after-tax deductions (union dues, loans, charitable) | Employer policy and State wage-deduction law (annexes) | annexes |")
A("")
A(GAP("fed.ccpa.disposable_earnings.definition",
      "the CCPA definition of disposable earnings (which deductions are 'required by law') and the resulting order of voluntary deductions vs garnishments are not in the facts",
      "Under 15 U.S.C. 1672(b) and 29 CFR 870.10, which amounts are subtracted from earnings to obtain disposable earnings (taxes, FICA, State programme shares, voluntary deductions), and do voluntary deductions such as retirement deferrals or health premiums reduce disposable earnings?",
      "CCG m07 §7.1/§7.3 ordering of post-tax deductions and the garnishment base cannot be stated",
      "deductions_garnishments", tier="A.1"))
A(H(3, "List any income types that are statutorily exempt from income tax."))
A("| Income | Treatment | Fact |")
A("|---|---|---|")
A(f"| Fringe benefits within the exclusions of §7.1 | Excluded up to the limits | {R('fed.bik.parking.monthly_exclusion')} |")
A(f"| Minister's parsonage allowance | {Q('fed.minister.withholding')} | {R('fed.minister.withholding')} |")
A(f"| Workers' compensation benefits | Not employer wages ({COV('work_accident_occupational_disease')}) | |")
A(f"| State PFML benefits | Paid by the State, not employer payroll ({COV('maternity_paternity_parental')}) | |")
A(f"| Foreign earned income (US citizens and residents abroad) | Excluded up to USD {T('fed.feie.amount')} | {R('fed.feie.amount')} |")
A(f"| Treaty-exempt wages of a nonresident alien | Reported on Form 1042-S, not W-2 box 1 | {R('fed.fit.nra.treaty_exempt.reporting')} |")

# ---------------------------------------------------------------- 7.2
A(H(2, "7.2 Benefits in Kind (BIK)"))
A(H(3, "Are non-cash benefits taxed via the standard payroll system, or a separate employer-paid regime?"))
A("Through the standard payroll system. The facts carry no separate employer fringe-benefit tax: a non-excluded benefit "
  "is added to the employee's wages and taxed with them, and specific benefits are excluded up to limits "
  f"{R('fed.bik.parking.monthly_exclusion')}.")
A(H(3, "What is the definition of fringe benefits and how is the taxable amount evaluated?"))
A("A fringe benefit is any non-cash form of pay. The facts value one benefit by table and exclude others by limit:")
A("")
A(f"**Group-term life insurance above USD {T('fed.bik.group_term_life.excluded_coverage')}.** Monthly cost per USD 1,000 of excess coverage (Pub. 15-B Table 2-2):")
A("")
A("| Age band | USD per 1,000 per month |")
A("|---|---|")
for k, lab in [("under_25", "Under 25"), ("25_29", "25 to 29"), ("30_34", "30 to 34"), ("35_39", "35 to 39"),
               ("40_44", "40 to 44"), ("45_49", "45 to 49"), ("50_54", "50 to 54"), ("55_59", "55 to 59"),
               ("60_64", "60 to 64"), ("65_69", "65 to 69"), ("70_plus", "70 and over")]:
    A(f"| {lab} | {T('fed.bik.group_term_life.monthly_cost_per_1000.' + k, fmt='money')} |")
A(f"\nSource {R('fed.bik.group_term_life.monthly_cost_per_1000.under_25')}.")
A("")
A("```")
A(f"imputed_month = (coverage - {T('fed.bik.group_term_life.excluded_coverage')}) / 1000 x rate_for_age_band")
A("```")
A("")
A(UNR("fed.bik.business_mileage.rate"))
A("")
A(GAP("fed.bik.valuation_general_rule",
      "the general valuation rule for taxable fringe benefits (fair market value, special valuation rules, timing of inclusion and withholding) is not in the facts",
      "Per Pub. 15-B (2026), how is a taxable non-cash fringe benefit valued (general fair-market-value rule and special rules: vehicle lease value, cents-per-mile, commuting), when must it be treated as paid, and may the employer elect not to withhold income tax on a vehicle benefit?",
      "CCG m07 §7.2 valuation questions answered for group-term life only; WTC in-kind wage types have no valuation rule",
      "benefits_in_kind", tier="A.2"))
A(H(3, "If a separate FBT regime exists, describe it in detail."))
A("Not applicable: no separate fringe-benefit tax appears in the facts (previous answers).")
A(H(3, "What is the calculation logic for fringe benefit tax?"))
A("Not applicable as a separate tax. Taxable benefits are added to the relevant bases and taxed with cash wages "
  "(Module 3, Step 1).")
A(H(3, "Are benefits-in-kind also subject to withholding tax?"))
A(f"Group-term life cost above the excluded coverage is FICA wages and income-tax withholding is not required "
  f"{R('fed.bik.group_term_life.excluded_coverage')}. For other benefits see research request `fed.bik.valuation_general_rule`; "
  "for nonresident aliens, `fed.fit.nra.bik.treatment` (Module 6).")
A(H(3, "Which benefits-in-kind must be processed via payroll, and which require declarations?"))
A("| Benefit | Payroll processing | Fact |")
A("|---|---|---|")
A(f"| Group-term life excess cover | Imputed monthly through payroll (FICA wages) | {R('fed.bik.group_term_life.excluded_coverage')} |")
A(f"| Employer Trump-account contribution | Reported on the W-2 code TA | {R('fed.w2.box12.new_codes')} |")
A(f"| Moving expenses, bicycle commuting reimbursements | Wages (exclusions eliminated) | {K('fed.bik.moving_and_bicycle.excluded')} |")
A(f"| Parking / transit above the monthly limit | Excess added to wages | {R('fed.bik.parking.monthly_exclusion')} |")
A("| Health FSA, HSA, dependent care | Employee election before the plan year | elections (§7.1) |")

# ---------------------------------------------------------------- 7.3
A(H(2, "7.3 Garnishments and Court Orders"))
A(H(3, "What are the rules for processing statutory deductions like child support, court-ordered fines, or tax levies?"))
A("| Order | Rule | Fact |")
A("|---|---|---|")
A(f"| Child-support IWO, interstate | {Q('multi.iwo.governing_law')}; remit within {T('multi.iwo.remittance_business_days')} business days | {R('multi.iwo.governing_law')} |")
A(f"| IWO form | OMB approval valid to {T('fed.iwo.omb_expiry')} | {R('fed.iwo.omb_expiry')} |")
A(f"| Federal tax levy | Exempt amount table below; the employer pays the rest of the take-home pay to the IRS | {R('fed.levy.exempt.single_0dep.weekly')} |")
A(f"| Creditor garnishment | CCPA limits below; stricter State law applies | {R('fed.ccpa.max_rate')} |")
A("")
A(UNR("fed.iwo.revised_form.state_golive"))
A(H(3, "Is there a statutory priority order if an employee has multiple garnishments?"))
A(f"Yes: {Q('fed.iwo.priority')} {R('fed.iwo.priority')}. Among support obligees and for fees and timing, the law of "
  f"the obligor's principal place of employment governs {R('multi.iwo.governing_law')}. State examples: Alabama gives the "
  f"IWO priority and remits within {T('al.garn.child_support.remit_business_days')} business days {R('al.garn.child_support.remit_business_days')}; "
  f"Connecticut remits within {T('ct.garn.child_support.remit_business_days')} business days {R('ct.garn.child_support.remit_business_days')}; "
  f"California {T('ca.garn.child_support.remit_business_days')} business days {R('ca.garn.child_support.remit_business_days')}; "
  f"Arizona {T('az.garn.child_support.remit_business_days')} business days {R('az.garn.child_support.remit_business_days')}.")
A(H(3, "Are there protected earnings limits?"))
A("**Federal (CCPA)** on disposable earnings:")
A("")
A("| Order | Maximum withheld | Fact |")
A("|---|---|---|")
A(f"| Ordinary creditor | Lesser of {T('fed.ccpa.max_rate')}% of weekly disposable earnings or the excess over USD {T('fed.ccpa.protected_weekly')} a week | {R('fed.ccpa.max_rate')} |")
A(f"| Support, employee supporting a spouse or child | {T('fed.ccpa.support.max_rate.with_dependents')}% (+{T('fed.ccpa.support.arrears_addon')} points with arrears over 12 weeks) | {R('fed.ccpa.support.max_rate.with_dependents')} |")
A(f"| Support, no other dependants | {T('fed.ccpa.support.max_rate.without_dependents')}% (+{T('fed.ccpa.support.arrears_addon')} points with arrears over 12 weeks) | {R('fed.ccpa.support.max_rate.without_dependents')} |")
A("")
A("**Federal tax levy: amounts exempt from levy, 2026 (Pub. 1494)**")
A("")
A("| Status | Daily | Weekly | Biweekly | Semimonthly | Monthly |")
A("|---|---|---|---|---|---|")
A(f"| Single / MFS, no dependent | {T('fed.levy.exempt.single_0dep.daily')} | {T('fed.levy.exempt.single_0dep.weekly')} | {T('fed.levy.exempt.single_0dep.biweekly')} | {T('fed.levy.exempt.single_0dep.semimonthly')} | {T('fed.levy.exempt.single_0dep.monthly')} |")
A(f"| Each dependent adds | {T('fed.levy.exempt.per_dependent.daily')} | {T('fed.levy.exempt.per_dependent.weekly')} | {T('fed.levy.exempt.per_dependent.biweekly')} | {T('fed.levy.exempt.per_dependent.semimonthly')} | {T('fed.levy.exempt.per_dependent.monthly')} |")
A(f"| MFJ, no dependent | | {T('fed.levy.exempt.mfj_0dep.weekly')} | | | {T('fed.levy.exempt.mfj_0dep.monthly')} |")
A(f"| Head of household, no dependent | | {T('fed.levy.exempt.hoh_0dep.weekly')} | | | |")
A(f"\nSource {R('fed.levy.exempt.single_0dep.weekly')}.")
A("")
A("**State limits stricter than the CCPA (examples; the more protective rule governs)**")
A("")
A("| State | Creditor garnishment limit | Fact |")
A("|---|---|---|")
A(f"| AK | Exempt: greater of USD {T('ak.garn.exempt.weekly')} a week or a share of disposable earnings | {R('ak.garn.exempt.weekly')} |")
A(f"| AL | {T('al.garn.exempt.percent')}% of resident wages exempt | {R('al.garn.exempt.percent')} |")
A(f"| AZ | Lesser of {T('az.garn.creditor.max_percent')}% of disposable earnings or the excess over {T('az.garn.creditor.minwage_multiple')} x the highest applicable minimum wage | {R('az.garn.creditor.max_percent')} |")
A(f"| CA | Lesser of {T('ca.garn.creditor.max_percent')}% of disposable earnings or {T('ca.garn.creditor.excess_percent')}% of disposable earnings above {T('ca.garn.creditor.minwage_multiple.weekly')} x the minimum wage (weekly) | {R('ca.garn.creditor.max_percent')} |")
A(f"| CO | Maximum {T('co.garn.creditor.max_percent')}% of disposable earnings; weekly floor USD {T('co.garn.creditor.weekly_floor')} | {R('co.garn.creditor.max_percent')} |")
A(f"| CT | Lesser of {T('ct.garn.creditor.max_percent')}% or the excess over USD {T('ct.garn.creditor.weekly_protected')} a week | {R('ct.garn.creditor.max_percent')} |")
A(f"| DC | {Q('dc.garn.creditor.rule')} | {R('dc.garn.creditor.rule')} |")

write_module(U, "\n".join(o))
print("written", U)

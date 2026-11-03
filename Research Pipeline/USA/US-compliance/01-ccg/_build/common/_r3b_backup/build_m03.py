# -*- coding: utf-8 -*-
"""Build 01-ccg/modules/m03_gross_to_net.md from the CCG facts (US build)."""
from ccglib import *

U = "m03_gross_to_net"
set_unit(U)
o = []
A = o.append

A("# Module 3: The Gross-to-Net Calculation Framework")
A("*Purpose: To establish the high-level, sequential logic of the payroll calculation.*")
A(H(2, "3.1 Gross-to-Net Flow"))
A(H(3, "Deliverable: Provide a definitive, step-by-step description or text-based flowchart illustrating the standard Gross-to-Net (G2N) calculation framework."))
A("A US payroll run computes one federal stack and, for each employee, the State and local stacks selected by the "
  "routing keys (`work_location_jurisdiction`, `residence_jurisdiction`, `sui_state`; Module 2). Each stack has its own "
  "taxable base. The order below is binding where a later step consumes an earlier result (flagged **ORDER**).")
A("")
A(f"Coverage: this flow is the treatment of the ordinary employee, {COV('resident_employee')}: federal withholding per "
  f"Form W-4 and Pub. 15-T; FICA employee and employer; FUTA and SUI employer-paid (SUI to the localization State); "
  "State income tax of the work State and, for residents working elsewhere, the residence State per its own rule.")

A(H(4, "Step 1: Summation of Gross Earnings"))
A("Sum every earning paid in the period, by its payment date: regular pay, overtime, commissions, supplemental pay "
  "(bonuses, severance), reported tips and the taxable value of non-cash benefits. Classification of each earning "
  "into regular or supplemental decides the income-tax method in Step 5.")
A("")
A("| Earning | Rule that matters at this step | Fact |")
A("|---|---|---|")
A(f"| Tips | Tips of USD {T('fed.tips.reporting_threshold_monthly')} or more in a month are subject to income tax withholding and FICA | {R('fed.tips.reporting_threshold_monthly')} |")
A(f"| Severance | {K('fed.severance.is_wages')}: wages for FIT, FICA and FUTA | {R('fed.severance.is_wages')} |")
A(f"| Group-term life insurance above USD {T('fed.bik.group_term_life.excluded_coverage')} of coverage | Imputed cost is FICA wages; income tax withholding not required | {R('fed.bik.group_term_life.excluded_coverage')} |")
A(f"| Paid-leave (PFML) employee contribution | {K('fed.pfml.employee_contribution.is_w2_wages')}: remains W-2 wages | {R('fed.pfml.employee_contribution.is_w2_wages')} |")

A(H(4, "Step 2: Application of Pre-Tax Deductions"))
A("Subtract salary-reduction amounts that the law excludes from a base. Each base has its own exclusion list, so one "
  "deduction can reduce the federal income-tax base and leave a State or unemployment base untouched.")
A("")
A("| Deduction | Annual limit 2026 | Fact |")
A("|---|---|---|")
A(f"| Elective deferral, 401(k)-type plan | USD {T('fed.retirement.401k.elective_deferral_limit')}; catch-up USD {T('fed.retirement.401k.catch_up_50')} (age 50+), USD {T('fed.retirement.401k.catch_up_60_63')} (ages 60 to 63) | {R('fed.retirement.401k.elective_deferral_limit')} |")
A(f"| Health FSA salary reduction | USD {T('fed.bik.health_fsa.salary_reduction_cap')} | {R('fed.bik.health_fsa.salary_reduction_cap')} |")
A(f"| HSA contribution | USD {T('fed.hsa.limit.self_only')} self-only / USD {T('fed.hsa.limit.family')} family | {R('fed.hsa.limit.self_only')} |")
A("")
A("State conformity differs, so the State base is built separately (examples):")
A("")
A("| State | Treatment | Fact |")
A("|---|---|---|")
for k in ["ca.wages.401k_deferrals", "pa.bik.pa.401k_403b_457.taxable", "ca.hsa.conforms", "nj.sui.wages.401k_included",
          "nj.sui.wages.section125_included", "ak.sui.wages.excludes_401k_deferrals"]:
    v = FACTS[k][0]["value"]
    label = {"pa.bik.pa.401k_403b_457.taxable": "employee deferrals are taxable for Pennsylvania personal income tax",
             "ca.hsa.conforms": "California does not conform to the federal HSA exclusion (HSA contributions subject to PIT, UI and SDI as stated in the annex)",
             "nj.sui.wages.401k_included": "401(k) deferrals are New Jersey unemployment and disability wages",
             "nj.sui.wages.section125_included": "cafeteria-plan (IRC sec.125) reductions are New Jersey unemployment wages where cash is electable",
             "ak.sui.wages.excludes_401k_deferrals": "deferrals are excluded from Alaska unemployment wages, unlike FUTA"}.get(k)
    A(f"| {k.split('.')[0].upper()} | {Q(k) if label is None else label} | {K(k)} |")
A("")
A(GAP("fed.retirement.pretax.tax_treatment",
      "the federal treatment of elective deferrals, cafeteria-plan (IRC sec.125) salary reductions and HSA salary reductions for each federal base (income-tax wages, FICA wages, FUTA wages) is not stated in the facts",
      "Under 26 U.S.C. 3121(a)(5), 3121(v), 3306(b)(5), 3306(r), 3401(a)(12) and 125, which federal bases (income-tax withholding wages, FICA wages, FUTA wages) are reduced by (a) 401(k)/403(b)/457(b) elective deferrals, (b) Section 125 cafeteria-plan salary reductions for health premiums, health FSA and dependent care, (c) HSA salary reductions?",
      "CCG m03 Step 2 cannot state which federal base each pre-tax deduction reduces; WTC Subject-to-X flags for deductions cannot be sourced",
      "income_tax", tier="A.1", shape="matrix deduction x base: excluded / included, with the section"))

A(H(4, "Step 3: Determination of Taxable Income"))
A("Build one taxable base per tax, from the same gross:")
A("")
A("| Base | Built from | Fact |")
A("|---|---|---|")
A("| Federal income-tax wages | Gross less federally excluded pre-tax deductions; then annualised in Worksheet 1A (Module 6) | `fed.fit.method` |")
A(f"| OASDI wages | FICA wages, capped at USD {T('fed.fica.oasdi.wage_base', on='2026-06-30')} paid by this employer in 2026 | {R('fed.fica.oasdi.wage_base', on='2026-06-30')} |")
A(f"| Medicare wages | FICA wages, no cap; Additional Medicare above USD {T('fed.fica.addl_medicare.withholding_threshold')} per employer | {R('fed.fica.addl_medicare.withholding_threshold')} |")
A(f"| FUTA wages | First USD {T('fed.futa.wage_base')} per employee per employer per year, across all States | {K('multi.futa.wage_base.scope')} |")
A("| State income-tax wages | State definition (conformity table in Step 2; annexes) | annexes |")
A(f"| Local wages | Local definition; example: {Q('oh.local.municipal_base')} (medium confidence) | {R('oh.local.municipal_base')} |")
A("| SUI / SDI / PFML wages | Each programme's definition and cap (Module 5) | annexes |")

A(H(4, "Step 4: Calculation of Employee Social Security Contributions (FICA)"))
A("```")
A(f"oasdi_ee   = round( {T('fed.fica.oasdi.rate.employee')}% x min( oasdi_wages_period , max(0, {T('fed.fica.oasdi.wage_base', on='2026-06-30')} - oasdi_wages_ytd) ) )")
A(f"medicare_ee = round( {T('fed.fica.medicare.rate.employee')}% x medicare_wages_period )")
A(f"addl_medicare = round( {T('fed.fica.addl_medicare.rate')}% x max(0, medicare_wages_ytd_after - max({T('fed.fica.addl_medicare.withholding_threshold')}, medicare_wages_ytd_before)) )")
A("```")
A("")
A(f"Rates and thresholds: {K('fed.fica.oasdi.rate.employee')}; {K('fed.fica.medicare.rate.employee')}; {K('fed.fica.addl_medicare.rate')}; "
  f"{K('fed.fica.addl_medicare.withholding_threshold')}. Additional Medicare is employee-only and is triggered per employer "
  "regardless of filing status. The remaining-base form (lesser of the remaining annual maximum or rate x period base) "
  "is mandatory; never annualise and divide.")

A(H(4, "Step 5: Calculation of Income Tax Withholding"))
A(f"Federal: {Q('fed.fit.method')} {R('fed.fit.method')}. When the W-4 Step 2 box is **not** checked, Worksheet 1A "
  f"line 1g subtracts USD {T('fed.fit.worksheet1a.line1g.mfj')} (married filing jointly) or USD "
  f"{T('fed.fit.worksheet1a.line1g.other')} (all other statuses) {R('fed.fit.worksheet1a.line1g.mfj')}. Supplemental pay "
  f"may instead be withheld at the flat {T('fed.fit.supplemental.flat_rate')}% and must be withheld at "
  f"{T('fed.fit.supplemental.mandatory_rate')}% above USD {T('fed.fit.supplemental.mandatory_threshold')} in the year "
  f"{R('fed.fit.supplemental.flat_rate')}. Full method and examples: Module 6.")
A("")
A("Then State income tax, then local tax. **ORDER** where a State base consumes the federal result:")
A("")
A("| State | Dependency | Fact |")
A("|---|---|---|")
A(f"| AL | {Q('al.wh.fit_before_sit')} | {R('al.wh.fit_before_sit')} |")
A(f"| OR | Federal tax withheld is subtracted from the Oregon base, capped at USD {T('or.pit.federal_tax_subtraction.cap')} (phase-out by income); the Department's 2026 publication also prints a lower figure in places: use the cap above (formula pages) | {R('or.pit.federal_tax_subtraction.cap')}; {K('practice.or.federal_cap')} |")
A("")
A("Resident and nonresident State routing (reciprocity, day thresholds, convenience rules, difference withholding) is "
  "applied before the State computation: Module 6 §6.2.")

A(H(4, "Step 6: Application of Post-Tax Deductions"))
A("Employee shares of State programmes (unemployment in the States that levy one, disability, paid leave, long-term "
  "care), then voluntary after-tax deductions, then garnishments and levies computed on disposable earnings with their "
  f"protected amounts and priority (Module 7). {Q('fed.iwo.priority')} {R('fed.iwo.priority')}.")
A("")
A(f"Note: the facts classify some State programme shares as after-tax (for example {K('me.pfml.employee_deduction.after_tax')}); "
  "the State annex decides per programme.")

A(H(4, "Step 7: Finalization of Net Pay"))
A("```")
A("net_pay = gross")
A("        - pre_tax_deductions")
A("        - (oasdi_ee + medicare_ee + addl_medicare)")
A("        - fit - state_income_tax(es) - local_tax(es)")
A("        - state_programme_employee_shares")
A("        - after_tax_deductions - garnishments")
A("```")
A("")
A(f"Rounding: {Q('fed.fit.rounding')} {R('fed.fit.rounding')}; the quarterly return is always in cents "
  f"({K('fed.form941.amounts_in_cents')}); Iowa computes its 2026 withholding {Q('ia.wh.rounding')} {R('ia.wh.rounding')}. "
  "State rounding table: Module 1 §1.5.")

A(H(3, "Explain where employer on-costs are calculated in parallel."))
A("Employer amounts are computed from the same bases in Step 3, in parallel with Steps 4 to 6, and never reduce net pay:")
A("")
A("| Employer on-cost | Rate / base | Fact |")
A("|---|---|---|")
A(f"| OASDI employer share | {T('fed.fica.oasdi.rate.employer')}% up to the OASDI base | {R('fed.fica.oasdi.rate.employer')} |")
A(f"| Medicare employer share | {T('fed.fica.medicare.rate.employer')}%, no cap; no employer match of Additional Medicare | {R('fed.fica.medicare.rate.employer')} |")
A(f"| FUTA | {T('fed.futa.rate.gross')}% less a credit of up to {T('fed.futa.credit.max')}% = {T('fed.futa.rate.net')}% net on USD {T('fed.futa.wage_base')}, plus any credit reduction of the wages' State | {R('fed.futa.rate.net')} |")
A("| SUI employer contribution | Experience rate of the `sui_state` on that State's base | annexes |")
A(f"| Employer paid-leave shares | Example: District of Columbia paid leave {T('dc.pfml.employer.rate')}%, employer only, no cap | {R('dc.pfml.employer.rate')} |")
A(f"| Employer payroll levies | Examples: Nevada Modified Business Tax {T('nv.mbt.general.rate')}% on quarterly wages above USD {T('nv.mbt.general.quarterly_threshold')}; Oregon TriMet transit {T('or.transit.trimet.employer.rate', on='2026-06-30')}% | {R('nv.mbt.general.rate')}; {R('or.transit.trimet.employer.rate', on='2026-06-30')} |")
A(f"| Per-employee fees | Example: New Mexico workers' compensation fee, employer USD {T('nm.wc.admin_fee.employer.quarterly', on='2026-06-30')} and employee USD {T('nm.wc.admin_fee.employee.quarterly', on='2026-06-30')} per quarter | {R('nm.wc.admin_fee.employer.quarterly', on='2026-06-30')} |")

A(H(3, "G2N flow summary and cross-cutting rules"))
A("```")
A("for each employee, pay period:")
A("  route  -> federal stack + State stack(s) from work/residence/sui_state")
A("  gross  -> sum earnings by payment date (Step 1)")
A("  bases  -> FIT wages, OASDI wages, Medicare wages, FUTA wages, State wages, local wages, SUI/SDI/PFML wages (Steps 2-3)")
A("  ee     -> FICA (remaining-base form) -> FIT -> State tax [AL, OR after FIT] -> local tax -> programme shares (Steps 4-6)")
A("  net    -> gross - all employee deductions (Step 7)")
A("  er     -> OASDI/Medicare ER, FUTA, SUI ER, ER programme shares and levies (parallel)")
A("```")
A("")
A("| Case | Rule | Source |")
A("|---|---|---|")
A(f"| Mid-period joiner or leaver | No proration rule in federal law: withholding is computed on the wages paid in the pay period with the Pub. 15-T period of the payroll frequency; wage bases start at the first payment by this employer in the year | {COV('mid_month_joiner_and_leaver')} |")
A(f"| Employee with more than one employer | Each employer withholds and applies wage bases independently; Additional Medicare per employer at USD {T('fed.fica.addl_medicare.withholding_threshold')}; with W-4 Step 2 checked, line 1g is not subtracted and the Step-2 schedule applies | {COV('multiple_employers')} |")
A(f"| Supplemental and special pay cycles | Pub. 15-T supports daily to annual periods (annualise, then divide); supplemental pay flat {T('fed.fit.supplemental.flat_rate')}% or aggregate, {T('fed.fit.supplemental.mandatory_rate')}% mandatory above USD {T('fed.fit.supplemental.mandatory_threshold')} | {COV('special_pay_cycles')} |")
A(f"| Accrual vs payment | Federal taxes follow the **payment** date: a December-earned, January-paid wage takes the new year's rates and bases. Exception: Massachusetts paid-leave rates apply to wages earned on or after 1 January | {COV('accrual_vs_payment')} |")

write_module(U, "\n".join(o))
print("written", U)

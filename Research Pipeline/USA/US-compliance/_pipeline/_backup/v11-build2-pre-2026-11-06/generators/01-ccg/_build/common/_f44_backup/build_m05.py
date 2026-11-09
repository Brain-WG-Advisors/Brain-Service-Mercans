# -*- coding: utf-8 -*-
"""Build 01-ccg/modules/m05_social_security.md from the CCG facts (US build)."""
from ccglib import *

U = "m05_social_security"
set_unit(U)
o = []
A = o.append
ON = "2026-06-30"


def t26(key, fmt=None):
    """2026 value of a possibly multi-dated key."""
    try:
        return T(key, on=ON if len({(f.get('effective_from'), f.get('effective_to')) for f in FACTS[key]}) > 1 else None, fmt=fmt)
    except ValueError:
        return T(key, on=ON, fmt=fmt)


def r26(key):
    try:
        return R(key, on=ON if len({(f.get('effective_from'), f.get('effective_to')) for f in FACTS[key]}) > 1 else None)
    except ValueError:
        return R(key, on=ON)


A("# Module 5: Social Security & Pension Systems")
A("*Purpose: To detail the rules for all mandatory social security and pension schemes.*")

# ---------------------------------------------------------------- 5.1
A(H(2, "5.1 Contribution Types and Rates"))
A(H(3, "List all mandatory social security and pension contributions for both employer and employee."))
A("**Federal layer (every employee)**")
A("")
A("| Contribution | Employee | Employer | Base / cap 2026 | Fact |")
A("|---|---|---|---|---|")
A(f"| Old-age, survivors and disability insurance (OASDI, social security) | {T('fed.fica.oasdi.rate.employee')}% | {T('fed.fica.oasdi.rate.employer')}% | USD {T('fed.fica.oasdi.wage_base', on=ON)} per employer | {R('fed.fica.oasdi.rate.employee')}; {R('fed.fica.oasdi.wage_base', on=ON)} |")
A(f"| Medicare (hospital insurance) | {T('fed.fica.medicare.rate.employee')}% | {T('fed.fica.medicare.rate.employer')}% | No cap | {R('fed.fica.medicare.rate.employee')} |")
A(f"| Additional Medicare | {T('fed.fica.addl_medicare.rate')}% | none | Wages above USD {T('fed.fica.addl_medicare.withholding_threshold')} paid by this employer in the year | {R('fed.fica.addl_medicare.rate')} |")
A(f"| Federal unemployment (FUTA) | none | {T('fed.futa.rate.gross')}% gross, credit up to {T('fed.futa.credit.max')}% = {T('fed.futa.rate.net')}% net | USD {T('fed.futa.wage_base')} per employer | {R('fed.futa.rate.net')}; {R('fed.futa.wage_base')} |")
A("")
A("There is no federal pension contribution beyond OASDI; occupational pensions are voluntary plans (§5.3).")
A("")
A("**State layer: unemployment insurance (SUI).** Every State levies an employer contribution on its own base, at an "
  "experience rate assigned to the employer (rates in the annexes). Employee contributions exist only in three States: "
  f"{Q('multi.sui.employee_contribution_states')} {R('multi.sui.employee_contribution_states')}.")
A("")
A("| State | Employee UI rate 2026 | Fact |")
A("|---|---|---|")
A(f"| AK | {t26('ak.sui.employee.rate')}% | {r26('ak.sui.employee.rate')} |")
A(f"| NJ | {t26('nj.sui.employee.rate')}% | {r26('nj.sui.employee.rate')} |")
A(f"| PA | {t26('pa.sui.employee.rate')}% on all gross wages, no cap | {r26('pa.sui.employee.rate')} |")
A("")
A("**State layer: disability (SDI/TDI), paid family and medical leave (PFML) and long-term care.**")
A("")
A("| State | Programme | Rate 2026 and split | Fact |")
A("|---|---|---|---|")
A(f"| CA | State Disability Insurance incl. paid family leave | Employee {t26('ca.sdi.employee.rate')}%, no wage cap, no employer share | {r26('ca.sdi.employee.rate')}; {K('ca.sdi.wage_cap.exists')} |")
A(f"| NJ | Temporary disability / family leave insurance | Employee TDI {t26('nj.tdi.employee.rate')}% (annual maximum USD {t26('nj.tdi.employee.max_annual')}); employee FLI {t26('nj.fli.employee.rate')}% (annual maximum USD {t26('nj.fli.employee.max_annual')}) | {r26('nj.tdi.employee.rate')}; {r26('nj.tdi.employee.max_annual')} |")
A(f"| NY | Disability benefits (DBL) and paid family leave (PFL), insurer-funded | DBL employee {t26('ny.dbl.employee.rate')}%, maximum USD {t26('ny.dbl.employee.max_weekly')} a week; PFL employee {t26('ny.pfl.employee.rate')}% (annual maximum USD {t26('ny.pfl.employee.max_annual')}) | {r26('ny.dbl.employee.rate')}; {r26('ny.pfl.employee.rate')} |")
A(f"| HI | Temporary disability insurance, insurer-funded | Employer may withhold up to {t26('hi.tdi.employee.max_rate')}% of weekly wages, maximum USD {t26('hi.tdi.employee.max_weekly_deduction')} a week | {r26('hi.tdi.employee.max_rate')}; {r26('hi.tdi.employee.max_weekly_deduction')} |")
A(f"| RI | Temporary disability / caregiver insurance | Employee {t26('ri.tdi.employee.rate')}% (annual maximum USD {t26('ri.tdi.employee.max_annual')}) | {r26('ri.tdi.employee.rate')} |")
A(f"| WA | Paid Family and Medical Leave | Total {T('wa.pfml.total.rate', on=ON)}% in 2026, employee up to {T('wa.pfml.employee.share', on=ON)}% of the premium; {T('wa.pfml.total.rate', on='2027-06-30')}% in 2027, employee {T('wa.pfml.employee.share', on='2027-06-30')}%; wage cap USD {t26('wa.pfml.wage_cap.annual')}; fewer than {T('wa.pfml.small_employer.threshold')} WA employees: no employer share | {R('wa.pfml.total.rate', on=ON)}; {R('wa.pfml.employee.share', on=ON)} |")
A(f"| WA | WA Cares long-term care | Employee {T('wa.ltc.wa_cares.employee.rate')}%, no cap | {R('wa.ltc.wa_cares.employee.rate')} |")
A(f"| MA | Paid Family and Medical Leave | Total {T('ma.pfml.total.rate')}% (25+ covered individuals); split below | {R('ma.pfml.total.rate')} |")
A(f"| DC | Universal Paid Leave | Employer only {T('dc.pfml.employer.rate')}%, no cap | {R('dc.pfml.employer.rate')} |")
A(f"| OR | Paid Leave Oregon | Total {t26('or.pfml.rate.total')}%; employee {T('or.pfml.employee.share')}% of the contribution | {r26('or.pfml.rate.total')}; {R('or.pfml.employee.share')} |")
A(f"| CO | FAMLI | {T('co.famli.total.rate', on=ON)}% = employee {t26('co.famli.employee.rate')}% + employer {t26('co.famli.employer.rate')}% (2027 total {T('co.famli.total.rate', on='2027-06-30')}%) | {R('co.famli.total.rate', on=ON)} |")
A(f"| CT | Paid Leave | Employee {t26('ct.pfml.employee.rate')}%, no employer share | {r26('ct.pfml.employee.rate')} |")
A(f"| DE | Paid Leave | Total {t26('de.pfml.rate.total')}% (medical {t26('de.pfml.rate.medical')}% + caregiving {t26('de.pfml.rate.family_caregiving')}% + parental {t26('de.pfml.rate.parental')}%); employee up to {T('de.pfml.employee_share.max_percent')}% | {r26('de.pfml.rate.total')} |")
A(f"| ME | Paid Family and Medical Leave | {t26('me.pfml.rate.total.15_plus')}% with 15+ employees, {t26('me.pfml.rate.total.under_15')}% below; employee at most {t26('me.pfml.employee.max_rate')}%; deducted after tax | {r26('me.pfml.rate.total.15_plus')}; {K('me.pfml.employee_deduction.after_tax')} |")
A(f"| MN | Paid Leave | Total {t26('mn.pfml.rate.total')}% (family {t26('mn.pfml.rate.family')}% + medical {t26('mn.pfml.rate.medical')}%); employee at most {t26('mn.pfml.employee.max_share.rate')}%; small employers {t26('mn.pfml.small_employer.rate')}% | {r26('mn.pfml.rate.total')} |")
A(f"| MD | FAMLI (contributions from {D('md.pfml.rate.total')}) | Total {T('md.pfml.rate.total')}%; employee up to {T('md.pfml.employee_share.max_percent')}% | {R('md.pfml.rate.total')} |")
A("")
A(f"Maternity, paternity and parental leave ({COV('maternity_paternity_parental')}): there is no federal paid parental "
  "leave for private employers; paid leave comes from the State PFML/TDI programmes above, whose premiums are withheld or "
  f"paid through payroll while the benefits are paid by the State. {K('fed.pfml.employee_contribution.is_w2_wages')}: the "
  "employee contribution remains W-2 wages.")
A("")
A("**Workers' compensation and levies.** Workers' compensation is State law and generally an insured employer cost "
  f"outside payroll ({COV('work_accident_occupational_disease')}). Payroll touches it where a State levies a per-employee "
  f"fee or allows an employee deduction: New Mexico fee employer USD {T('nm.wc.admin_fee.employer.quarterly', on=ON)} and "
  f"employee USD {T('nm.wc.admin_fee.employee.quarterly', on=ON)} per quarter {R('nm.wc.admin_fee.employer.quarterly', on=ON)}; "
  f"Washington {Q('wa.wc.employee_deduction.rule')} {R('wa.wc.employee_deduction.rule')}.")
A("")
A(UNR("multi.workers_comp.employee_share"))
A("")
A(f"Employer transit levies (Oregon): TriMet {t26('or.transit.trimet.employer.rate')}%, Lane {t26('or.transit.lane.employer.rate')}% "
  f"{r26('or.transit.trimet.employer.rate')}. Other employer payroll levies are in the annexes (scope decision US-OWN-007).")
A(H(3, "Are contributions managed at a national or sub-national level?"))
A("Both. FICA and FUTA are federal (IRS, quarterly and annual federal returns). Unemployment insurance, disability, "
  "paid-leave and long-term-care programmes are State programmes with their own agency, base and return. FUTA links "
  f"the two levels: {Q('fed.futa.legal_basis.state_credit')} {R('fed.futa.legal_basis.state_credit')}.")
A("")
A("| Element | Rule | Fact |")
A("|---|---|---|")
A(f"| Which State's SUI applies | {Q('multi.sui.localization_test')} | {R('multi.sui.localization_test')} |")
A(f"| Telecommuting | {Q('multi.sui.localization.telecommuting')} | {R('multi.sui.localization.telecommuting')} |")
A(f"| Unresolved cases | {Q('multi.sui.reciprocal_coverage_election')} | {R('multi.sui.reciprocal_coverage_election')} |")
A(f"| Which State's PFML/SDI applies | {Q('multi.pfml.coverage_test.default', on=ON)} | {R('multi.pfml.coverage_test.default', on=ON)} |")
A("")
# round 2: the m05 summary item duplicated the per-State requests of Annex MULTI (MULTI.3); pointer instead of a
# second marker without its own research request
A("The PFML/SDI/TDI coverage test of the remaining programmes (California, New Jersey, New York, Massachusetts, "
  "Colorado, Minnesota, Vermont, Hawaii) is open State by State in Annex MULTI (MULTI.3), where each carries its own "
  "research marker.")

# ---------------------------------------------------------------- 5.1.1
A(H(2, "5.1.1 Contribution Basis Definition"))
A(H(3, "For each mandatory contribution, provide the statutory definition of the earnings base."))
A("FICA and FUTA are levied on wages **paid** in the calendar year by the employer "
  f"({COV('accrual_vs_payment')}). FUTA counts one base per employer, not per State: {Q('multi.futa.wage_base.scope')} "
  f"{R('multi.futa.wage_base.scope')}. The inclusion/exclusion lists of FICA and FUTA wages are in Module 4 §4.2 "
  f"{R('fed.fica.wage_definition.exclusions')}. Each State defines its own UI wages; the 2026 taxable wage bases are:")
A("")
A("| State | SUI taxable wage base 2026 (USD) | Fact |")
A("|---|---|---|")
for j in [x.lower() for x in MAN("tier", "_jurisdictions") if len(x) == 2]:
    k = f"{j}.sui.wage_base"
    if not has(k):
        A(f"| {j.upper()} | not in the facts | |")
        continue
    try:
        A(f"| {j.upper()} | {T(k, on=ON) if len(FACTS[k]) > 1 else T(k)} | {R(k, on=ON) if len(FACTS[k]) > 1 else R(k)} |")
    except ValueError:
        A(f"| {j.upper()} | no 2026-dated value in the facts (annex) | |")
A("")
A("Many States count wages already reported by the same employer to another State's UI in the same year toward their "
  f"own base (for example {K('multi.sui.other_state_wage_credit.ca')}, {K('multi.sui.other_state_wage_credit.fl')}); some "
  f"do not ({K('multi.sui.other_state_wage_credit.ia')}; {K('mt.sui.wage_base.other_state_credit')}). Annex MULTI keys each State.")
A("")
A("The States whose other-State wage credit is not yet established are listed in Annex MULTI (MULTI.3), each with "
  "its own research marker.")
A("")
A("State UI wage definitions also differ from FICA wages for deferrals and cafeteria-plan reductions (examples: "
  f"{K('nj.sui.wages.401k_included')}; {K('va.sui.wages.401k_included')}; {K('ak.sui.wages.excludes_401k_deferrals')}; "
  f"{K('ri.ui_tdi.wages.401k_section125_excluded')}).")
A(H(3, "Clarify the legal definitions of any specific terms used."))
A("| Term | Meaning in this guide | Fact |")
A("|---|---|---|")
A("| FICA wages | Remuneration for employment subject to OASDI and Medicare, before the OASDI cap | `fed.fica.*` |")
A(f"| Wage base | Annual cap per employer and calendar year on the wages subject to a contribution | {R('fed.fica.oasdi.wage_base', on=ON)} |")
A(f"| Localization | First step of the UI coverage test: service entirely within the State, or out-of-State service incidental | {R('multi.sui.localization_test')} |")
A(f"| `sui_state` | Result of the localization test, a routing key on the employee master data | {R('multi.ui_wage_report.routing')} |")
A(f"| Credit reduction | Reduction of the FUTA credit for a State with an outstanding Title XII advance | {R('fed.futa.legal_basis.state_credit')} |")
A(H(3, "Deliverable: Provide a comprehensive summary of current contribution rates. Describe rates across various regions and residential statuses, including tiers, ceilings, floors, variations by age or gender."))
A("Federal rates are uniform across States and residence statuses; the tables of §5.1 are the rate summary. Variations:")
A("")
A("| Variation | Rule | Fact |")
A("|---|---|---|")
A(f"| Ceiling | OASDI USD {T('fed.fica.oasdi.wage_base', on=ON)} (2026); USD {T('fed.fica.oasdi.wage_base', on='2027-06-30')} published for 2027 (medium confidence) | {R('fed.fica.oasdi.wage_base', on=ON)}; {R('fed.fica.oasdi.wage_base', on='2027-06-30')} |")
A(f"| Tier above a threshold | Additional Medicare above USD {T('fed.fica.addl_medicare.withholding_threshold')} | {R('fed.fica.addl_medicare.withholding_threshold')} |")
# round 2 (QA r1 C41): the 2025 California / Virgin Islands credit reductions are prior-year values
# (moved to _history by agent 2); the configuration table shows the rule only, the 2026 list is the open item below.
A(f"| Region (FUTA) | Credit reduction for the State of the wages when the State carries an outstanding Title XII advance; the 2026 credit-reduction States are the open item below | {R('fed.futa.legal_basis.state_credit')} |")
A("| Region (State programmes) | SUI, SDI, PFML per State (§5.1) | annexes |")
# round 3 (QA r2 C31): FICA/FUTA exemptions of nonresident aliens and totalization, from the facts agent 2 added
_nra = nra_fica_text()
if _nra:
    A("| Nonresident alien | The NRA withholding add-on has no FICA or FUTA effect; FICA and FUTA apply to actual wages unless "
      "one of these exemptions applies: " + _nra + " | " + COV('non_resident_employee') + " |")
else:
    A("| Nonresident alien | The NRA withholding add-on has no FICA or FUTA effect. FICA and FUTA exemptions of nonresident "
      "aliens (nonimmigrant classes, totalization agreements) are not configured in this release | " + COV('non_resident_employee') + " |")
A(f"| Age | No age-based rates; age-based exemptions only: household workers under 18 (unless principal occupation), family employment, students (§5.2) | {R('fed.household.fica_cash_threshold')}; {K('fed.family_employment.treatment')} |")
A("| Gender | No gender-based rate or exemption in the facts | |")
A("")
A(f"⚠️ RESEARCH-GAP [[GAPKEY:fed.futa.credit_reduction.ca]] (non-blocking): the 2026 FUTA credit reductions for California "
  "and the U.S. Virgin Islands become final only if the Title XII advances remain unpaid on 2026-11-10; the potential "
  "rates and the open items are in Annex FED (FED.3). Closes with: the Department of Labor credit-reduction list "
  "published after 2026-11-10, or the 2026 Schedule A (Form 940) instructions.")
A("")
A("**Massachusetts PFML split (decision recorded).** The employee may bear part of each component; the split changes on "
  f"{D('ma.pfml.split', on='2027-06-30')}:")
A("")
A("| Period | Split | Fact |")
A("|---|---|---|")
A(f"| 2026 | {Q('ma.pfml.split', on=ON)} | {R('ma.pfml.split', on=ON)} |")
A(f"| From 2027 | {Q('ma.pfml.split', on='2027-06-30')} | {R('ma.pfml.split', on='2027-06-30')} |")
A("")
A(f"Decision: {Q('practice.ma.pfml_split')} {R('practice.ma.pfml_split')}. The Act's section 45 makes the swap apply for "
  "taxable years beginning on or after 1 January 2026 [US-MAS5-026], while the Department of Family and Medical Leave "
  "implements it from 2027 [US-MAS5-012]; contributions are set per calendar year by the Department, and the Act gives no "
  "mechanism to re-split amounts already withheld. Massachusetts rates apply to wages **earned** on or after 1 January "
  f"({COV('accrual_vs_payment')}).")
A("")
A(UNR("ma.pfml.split.effective_date"))

# ---------------------------------------------------------------- 5.2
A(H(2, "5.2 Calculation Logic and Edge Cases"))
A(H(3, "What is the step-by-step calculation logic for all types of social security contributions?"))
A("```")
A("for each contribution c with rate r_c and annual cap cap_c (None = no cap):")
A("  base_ytd_before = taxable wages of c already paid by this employer this calendar year")
A("  room            = cap_c - base_ytd_before            (infinite when no cap)")
A("  taxable_period  = min(period_wages_c, max(0, room))")
A("  amount          = round_half_up(taxable_period x r_c, 0.01)")
A("# never annualise and divide; weekly-capped programmes (NY DBL, HI TDI) cap per week")
A("```")
A("")
A(f"Federal application ({COV('resident_employee')}): OASDI {T('fed.fica.oasdi.rate.employee')}% + {T('fed.fica.oasdi.rate.employer')}% "
  f"to USD {T('fed.fica.oasdi.wage_base', on=ON)}; Medicare {T('fed.fica.medicare.rate.employee')}% + {T('fed.fica.medicare.rate.employer')}%; "
  f"Additional Medicare {T('fed.fica.addl_medicare.rate')}% above USD {T('fed.fica.addl_medicare.withholding_threshold')}; FUTA "
  f"{T('fed.futa.rate.net')}% net on USD {T('fed.futa.wage_base')}; SUI per `sui_state`.")
A(H(3, "Are contributions based on actual or standard salary?"))
A(f"Actual wages paid. No notional or standard salary appears in the federal or State bases of the facts; every base is "
  f"wages paid in the period by payment date ({COV('accrual_vs_payment')}).")
A(H(3, "Describe rules for eligibility, joining month, termination month, mid-period hires, mid-period terminations, and mid-period salary changes."))
A(f"No proration and no minimum period: contributions apply to the wages paid in the period from the first payment "
  f"({COV('mid_month_joiner_and_leaver')}). Each base runs per employer per calendar year from the first payment; a "
  "salary change takes effect through the wages of the period in which it is paid. Successor employers may carry FUTA "
  f"wages over ({R('multi.futa.wage_base.scope')}).")
A(H(3, "Do different payment frequencies affect contribution rates or parameters?"))
A("Rates and annual caps do not change with frequency. Weekly-defined parameters do: New York DBL is capped at USD "
  f"{T('ny.dbl.employee.max_weekly')} a week {R('ny.dbl.employee.max_weekly')} and Hawaii TDI at USD "
  f"{t26('hi.tdi.employee.max_weekly_deduction')} a week {r26('hi.tdi.employee.max_weekly_deduction')}; convert these per pay period.")
A(H(3, "Detail variations based on employee age or gender."))
A("| Group | Treatment | Fact |")
A("|---|---|---|")
A(f"| Household employees | FICA when cash wages reach USD {T('fed.household.fica_cash_threshold')} in 2026 (exempt under 18 unless principal occupation); FUTA when USD {T('fed.household.futa_quarter_threshold')} cash wages in any quarter | {R('fed.household.fica_cash_threshold')} |")
A(f"| Family employment | {Q('fed.family_employment.treatment')} | {R('fed.family_employment.treatment')} |")
A(f"| Students | {Q('fed.students.treatment')} | {R('fed.students.treatment')} |")
A("| Gender | No variation in the facts | |")
A(H(3, "Is there a minimum number of working days required for contributions?"))
A("No. The thresholds are monetary, not day counts:")
A("")
A("| Group | Threshold | Fact |")
A("|---|---|---|")
A(f"| Agricultural workers | USD {T('fed.agricultural.per_worker_threshold')} cash wages to a worker in the year, or USD {T('fed.agricultural.total_threshold')} total farm pay; FUTA at USD {T('fed.agricultural.futa_quarter_threshold')} in a quarter | {R('fed.agricultural.per_worker_threshold')} |")
A(f"| Election workers | FICA from USD {T('fed.election_worker.fica_threshold')} | {R('fed.election_worker.fica_threshold')} |")
A(f"| Household employees | See above (USD {T('fed.household.fica_cash_threshold')}) | {R('fed.household.fica_cash_threshold')} |")
A(H(3, "How are contributions calculated for Board of Directors who are also employees?"))
A(f"Corporate officers are employees: officer wages bear FICA and FUTA and State UI covers them; directors' fees "
  f"without employment are not wages and stay outside payroll ({COV('officers_without_employment_contract')}). "
  f"Statutory employees: {Q('fed.statutory_employee.treatment')} {R('fed.statutory_employee.treatment')}. Full treatment: Module 11.")
A(H(3, "Are year-end adjustments required?"))
A(f"No employer regularisation ({COV('annual_regularisation')}): the employer stops OASDI at the cap and starts "
  "Additional Medicare above the threshold per employer; it reconciles four quarterly returns to the annual W-2/W-3 and "
  "corrects through the federal correction forms. Excess OASDI caused by several employers is refunded to the employee "
  f"at assessment ({COV('multiple_employers')}). The FUTA credit reduction of the year is settled on the annual return.")
A("")
A(UNR("fed.common_paymaster.rule"))

# ---------------------------------------------------------------- 5.3
A(H(2, "5.3 Voluntary Contributions & Private Schemes"))
A(H(3, "Can employees and employers make additional voluntary contributions?"))
A("Yes, to employer retirement and health-savings plans, within annual limits:")
A("")
A("| Plan | 2026 limit | Fact |")
A("|---|---|---|")
A(f"| 401(k)-type elective deferral | USD {T('fed.retirement.401k.elective_deferral_limit')}; catch-up USD {T('fed.retirement.401k.catch_up_50')} (50+), USD {T('fed.retirement.401k.catch_up_60_63')} (60 to 63) | {R('fed.retirement.401k.elective_deferral_limit')} |")
A(f"| SIMPLE plan deferral | USD {T('fed.retirement.simple.deferral_limit')} | {R('fed.retirement.simple.deferral_limit')} |")
A(f"| HSA | USD {T('fed.hsa.limit.self_only')} self-only / USD {T('fed.hsa.limit.family')} family | {R('fed.hsa.limit.self_only')} |")
A(f"| Health FSA | USD {T('fed.bik.health_fsa.salary_reduction_cap')}; carry-over up to USD {T('fed.bik.health_fsa.carryover_max')} | {R('fed.bik.health_fsa.salary_reduction_cap')} |")
A("")
A(f"An employer's voluntary payment of the employee's State PFML share is W-2 wages {R('fed.pfml.employee_contribution.is_w2_wages')}.")
A(H(3, "Which employee contributions are allowed as pre-tax deductions?"))
A("Elective deferrals, health FSA and HSA salary reductions are salary-reduction arrangements (limits above). Which "
  f"federal base each one reduces is in Module 3, Step 2 {R('fed.retirement.pretax.tax_treatment')}; State "
  f"treatment differs ({K('ca.wages.401k_deferrals')}; {K('pa.bik.pa.401k_403b_457.taxable')}).")
A(H(3, "Are there private insurance schemes with employer and employee contributions?"))
A("| Scheme | Rule | Fact |")
A("|---|---|---|")
A(f"| New York DBL / PFL | Insured with a private carrier or the State fund; employee share withheld by payroll (§5.1) | {r26('ny.dbl.employee.rate')} |")
A(f"| Hawaii TDI | Insurer-funded, no State return; employee share up to the cap (§5.1) | {r26('hi.tdi.employee.max_rate')} |")
A(f"| California voluntary disability plan | Employer plan in place of State SDI; W-2 box 14 label {T('ca.sdi.voluntary_plan.w2_box14_label')} | {R('ca.sdi.voluntary_plan.w2_box14_label')} |")
A(H(3, "What documents or declarations are required from an employee?"))
A("None for FICA or FUTA. Retirement and HSA salary reductions require the employee's plan election; the Washington "
  f"paid-leave/WA Cares report carries the employee's WA Cares exemption status {R('wa.report.pfml_ltc.fields')}.")

write_module(U, "\n".join(o))
print("written", U)

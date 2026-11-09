# -*- coding: utf-8 -*-
"""Second block of federal-layer country additions: earnings without a global code, fringe and imputed items, annual wage statement
reporting items, garnishments and voluntary deductions."""
import wtc_common as W
import wtc_profiles as P
from wtc_model import YES, NO, YN, NA, X
import wtc_fed as F

val, line, rid = W.val, W.line, W.rid

_SPEC = None


def spec_ref(spec, name):
    """'US-SSA-001 row 134' for the field named `name` of an approved Report Specification (F25: read from the spec)."""
    global _SPEC
    if _SPEC is None:
        _SPEC = {}
        for r in W.D.spec_rows():
            _SPEC.setdefault((r["spec"], r["name"]), r["row"])
    _SPEC[(spec, name)]
    return f"{spec} field {name}"


def add_federal2(reg):
    A = reg.add
    B = P.B()

    # --------------------------------------------------------------------------- earnings ---
    f = P.flags_supp()
    A("commission", "Commission", "Earning",
      ("Commission paid on sales or results: supplemental wages when paid separately, wages for every federal tax. Same treatment and parameters "
       "as the bonus family (anchor 62200): optional flat rate or aggregate method, mandatory rate above the annual threshold, social security, "
       "Medicare and FUTA. Flags marked Yes-No are conditional as stated on the anchor. Inputs: " + f"{F.D_RATE_BASIS}."),
      tax_code="US-TX-02", occ="Additional", flags=f, basis=P.basis_for(f), side="NONE", rep="W-2 boxes 1, 3 and 5", payslip=True,
      inputs=[F.D_RATE_BASIS], legal=["US-FEDS5-003"], fam="fed_earn")

    f = P.flags_tips()
    A("tips_cash", "Cash tips reported by the employee", "Earning",
      (f"Cash tips received by the employee and reported to the employer. FIT: {val('fed.base.tips.fit')} [{rid('fed.base.tips.fit')}]. Social security "
       f"and Medicare: {val('fed.base.tips.fica')} [{rid('fed.base.tips.fica')}]. FUTA: {val('fed.base.tips.futa')} [{rid('fed.base.tips.futa')}]. "
       f"Reporting: W-2 box 12 code {val('fed.w2.box12.code.tp')} [{rid('fed.w2.box12.code.tp')}] and box 14b Treasury Tipped Occupation Code "
       f"({F.D_TTOC1}, {F.D_TTOC2}); {val('fed.obbba.tips_deduction.level')} [{rid('fed.obbba.tips_deduction.level')}]. Qualified tips deduction cap "
       f"{val('fed.plaw119_21.qualified_tips.deduction_cap')} at assessment only [{rid('fed.plaw119_21.qualified_tips.deduction_cap')}]. Washington paid family and medical leave: {val('wa.pfml.base.tips')} [{rid('wa.pfml.base.tips')}]. Accumulator: "
       f"year-to-date tips for the social security wage base (box 7 {X('base_oasdi_tips')}). {W.gap('WTC-RQ-07', 'State unemployment insurance and programme definition of tips')}."),
      tax_code="US-TX-03", occ="Additional", flags=f, basis=P.basis_for(f, {"income_tax": rid("fed.base.tips.fit"), "oasdi": rid("fed.base.tips.fica"),
      "medicare": rid("fed.base.tips.fica"), "futa": rid("fed.base.tips.futa")}), side="NONE",
      rep="W-2 box 7; box 12 code TP; box 14b", payslip=True, inputs=[F.D_TTOC1, F.D_TTOC2],
      legal=["US-FEDS5-029", "US-FEDS5-030", "US-FEDS5-007"], fam="fed_earn")

    A("tips_alloc", "Allocated tips (reporting only)", "Notional",
      (f"Tips allocated to the employee by an establishment that must allocate them: reported in W-2 box 8 and not included in boxes 1, 3, 5 or 7: "
       f"{val('rspec.fed.w2.box_map')} [{', '.join(W.rids('rspec.fed.w2.box_map'))}]. Reporting only; no tax or base effect. Serves {spec_ref('US-SSA-001', 'RO Allocated Tips')}."),
      tax_code="US-NA", rep="W-2 box 8", legal=["US-FEDS5-007"], fam="fed_report")

    f = P.flags_reg()
    A("ot_premium", "Qualified overtime premium (reporting only)", "Notional",
      (f"The premium portion of qualified overtime accumulated for the annual wage statement: W-2 box 12 "
       f"code {val('fed.w2.box12.code.tt')} [{rid('fed.w2.box12.code.tt')}]. It is part of the overtime wages already counted in the overtime rows "
       f"(anchor 62110) and is reported only: {val('fed.obbba.overtime_deduction.level')} [{rid('fed.obbba.overtime_deduction.level')}]. Deduction cap "
       f"{val('fed.plaw119_21.qualified_overtime.deduction_cap')} at assessment. Serves {spec_ref('US-SSA-001', 'RO Code TT')}."),
      tax_code="US-NA", rep="W-2 box 12 code TT", legal=["US-FEDS5-030", "US-FEDS5-007"], fam="fed_report")

    f = dict(income_tax=NO, table_tax=NO, special_tax=NO, oasdi=NO, medicare=NO, futa=NA, sui=NA, state_programmes=NA, pension=NA,
             state_income_tax=NA, local_income_tax=NA)
    A("minister_parsonage", "Minister parsonage allowance", "Earning",
      (f"Parsonage allowance of a minister who is a common-law employee: {val('fed.minister.withholding')} [{rid('fed.minister.withholding')}]. "
       f"Flag: {X('flag_minister')}."),
      tax_code="US-TX-08", flags=f, basis={k: rid("fed.minister.withholding") for k, v in f.items() if v != NA}, rep="W-2 box 1 (excluded)",
      inputs=[F.D_SPECIAL], legal=["US-FED-030"], fam="fed_earn")

    # ------------------------------------------------------------ fringe and imputed income ---
    f = dict(income_tax=NO, table_tax=NO, special_tax=NO, oasdi=YES, medicare=YES, futa=NO, sui=YN, state_programmes=YN, pension=NA,
             state_income_tax=YN, local_income_tax=YN)
    A("gtl_imputed", "Imputed income - group-term life insurance above the excluded coverage", "Notional",
      (f"Cost of employer-paid group-term life coverage above {val('fed.bik.group_term_life.excluded_coverage')} (Table 2-2 cost less the employee's "
       f"payments): FIT {val('fed.base.group_term_life.fit')} [{rid('fed.base.group_term_life.fit')}]; social security and Medicare "
       f"{val('fed.base.group_term_life.fica')} [{rid('fed.base.group_term_life.fica')}]; FUTA {val('fed.base.group_term_life.futa')} "
       f"[{rid('fed.base.group_term_life.futa')}]. Nonresident alien employee: {W.gap('WTC-RQ-15')}. "
       f"Added to wages and deducted again from net pay (an in-kind item): net pay is unchanged. Serves {spec_ref('US-SSA-001', 'RW Employer Cost of Group Term Life Over 50,000')}. "
       f"{W.gap('WTC-RQ-07', 'State unemployment insurance and programme definition')}."),
      tax_code="US-TX-08", flags=f, basis=P.basis_for(f, {"income_tax": rid("fed.base.group_term_life.fit"), "oasdi": rid("fed.base.group_term_life.fica"),
      "medicare": rid("fed.base.group_term_life.fica"), "futa": rid("fed.base.group_term_life.futa")}), side="NONE",
      rep="W-2 boxes 1, 3, 5; box 12 code C", in_kind=True, legal=["US-FEDS5-008", "US-FEDQ1-008"], fam="fed_fringe")

    f = dict(income_tax=YES, table_tax=YN, special_tax=YN, oasdi=YES, medicare=YES, futa=YN, sui=YN, state_programmes=YN, pension=NA,
             state_income_tax=YES, local_income_tax=YES)
    A("vehicle_personal", "Personal use of an employer vehicle (imputed income)", "Notional",
      (f"Value of personal use of an employer vehicle: commuting valuation rule {val('fed.bik.vehicle.commuting_rule.value_per_one_way')} per one-way "
       f"commute [{rid('fed.bik.vehicle.commuting_rule.value_per_one_way')}]. Withholding: {val('fed.bik.withholding.method')} "
       f"[{rid('fed.bik.withholding.method')}]. Election not to withhold FIT on the vehicle benefit: {val('fed.bik.vehicle.election_not_to_withhold_fit')} "
       f"[{rid('fed.bik.vehicle.election_not_to_withhold_fit')}]. Added to wages and deducted again from net pay (in-kind item). "
       f"{W.gap('WTC-RQ-07', 'FUTA, State unemployment insurance and programme definition of the benefit')}."),
      tax_code="US-TX-08", flags=f, basis=P.basis_for(f, {k: rid("fed.bik.withholding.method") for k in ("income_tax", "table_tax", "special_tax", "oasdi", "medicare")}),
      rep="W-2 boxes 1, 3 and 5", in_kind=True, legal=["US-FEDS5-008"], fam="fed_fringe")

    f = dict(income_tax=YN, table_tax=NO, special_tax=NO, oasdi=YN, medicare=YN, futa=YN, sui=YN, state_programmes=YN, pension=NA,
             state_income_tax=YN, local_income_tax=YN)
    A("dep_care", "Dependent care assistance (employer-provided or salary reduction)", "Deduction",
      (f"Dependent care assistance: FIT, FICA and FUTA {val('fed.base.dependent_care.fit')} [{rid('fed.base.dependent_care.fit')}]; exclusion limit "
       f"{val('fed.bik.dependent_care.exclusion')} a year [{rid('fed.bik.dependent_care.exclusion')}]. The amount above the limit is wages. "
       f"Pennsylvania: {val('pa.base.section125.dependent_care.pit')} [{rid('pa.base.section125.dependent_care.pit')}]; New Jersey: {val('nj.base.dependent_care_129.git')} [{rid('nj.base.dependent_care_129.git')}]. Reported in W-2 box 10. Serves {spec_ref('US-SSA-001', 'RW Dependent Care Benefits')}. "
       f"{W.gap('WTC-RQ-07', 'State unemployment insurance and programme definition')}."),
      tax_code="US-TX-08", flags=f, basis=P.basis_for(f, {k: rid("fed.base.dependent_care.fit") for k in ("income_tax", "oasdi", "medicare", "futa")}),
      side="EE", rep="W-2 box 10", legal=["US-FEDS5-008"], fam="fed_fringe")

    A("hsa_er", "Employer contribution to a health savings account", "Employer Contribution",
      (f"Employer or section 125 contribution to an HSA of a qualified individual: FIT, FICA and FUTA {val('fed.base.hsa_contribution.fit')} "
       f"[{rid('fed.base.hsa_contribution.fit')}]; limits {val('fed.hsa.limit.self_only')} self-only and {val('fed.hsa.limit.family')} family "
       f"[{rid('fed.hsa.limit.self_only')}]. California: {val('ca.base.hsa.pit')} [{rid('ca.base.hsa.pit')}]. Reported in W-2 box 12 code W. "
       f"Serves {spec_ref('US-SSA-001', 'RW Employer Contributions to HSA')}."),
      tax_code="US-TX-08", flags=dict(income_tax=YN, table_tax=NO, special_tax=NO, oasdi=YN, medicare=YN, futa=YN, sui=YN, state_programmes=YN,
                                       pension=NA, state_income_tax=YN, local_income_tax=YN),
      basis={k: rid("fed.base.hsa_contribution.fit") for k in ("income_tax", "oasdi", "medicare", "futa")} | {
          "sui": rid("multi.sui.localization_test"), "state_programmes": rid("multi.sui.localization_test"),
          "state_income_tax": rid("multi.no_wage_income_tax.states"), "local_income_tax": rid("multi.no_wage_income_tax.states")},
      side="ER", rep="W-2 box 12 code W", legal=["US-FEDS5-008"], fam="fed_fringe")

    A("trump_er", "Employer Trump-account contribution", "Employer Contribution",
      (f"Employer contribution to a Trump account, excluded from wages up to {val('fed.bik.trump_account.employer_contribution_max')} [{rid('fed.bik.trump_account.employer_contribution_max')}] "
       f"(effective from {W.cur('fed.bik.trump_account.employer_contribution_max')['effective_from']}); reported in W-2 box 12 code {val('fed.w2.box12.code.ta')} [{rid('fed.w2.box12.code.ta')}] (effective from {W.cur('fed.w2.box12.code.ta')['effective_from']}). Serves "
       f"{spec_ref('US-SSA-001', 'RO Code TA')}."),
      tax_code="US-TX-08", flags=dict(income_tax=YN), basis={"income_tax": rid("fed.bik.trump_account.employer_contribution_max")},
      side="ER", rep="W-2 box 12 code TA (from 2026-07-04)", legal=["US-FEDS5-030", "US-FEDS5-007"], fam="fed_fringe")

    # -------------------------------------------------------------- annual wage statement reporting ---
    def rpt(sym, name, expl, rep, spec_name, extra_legal=()):
        A(sym, name, "Notional", expl + f" Serves {spec_ref('US-SSA-001', spec_name)}. Reporting code table: "
          + W.rq08() + ".",
          tax_code="US-NA", rep=rep, legal=["US-FEDS5-007"] + list(extra_legal), fam="fed_report")

    rpt("w2_a", "Uncollected social security or railroad retirement tax on tips (reporting only)",
        "Reporting-only amount of the employee social security tax on tips that could not be collected (W-2 box 12 code A).", "W-2 box 12 code A", "RO Code A")
    rpt("w2_b", "Uncollected Medicare tax on tips (reporting only)",
        "Reporting-only amount of the employee Medicare tax on tips that could not be collected (W-2 box 12 code B).", "W-2 box 12 code B", "RO Code B")
    rpt("w2_j", "Nontaxable sick pay (reporting only)",
        "Reporting-only amount of sick pay that is not taxable (W-2 box 12 code J).", "W-2 box 12 code J", "RO Code J")
    rpt("w2_k", "Excise tax on excess golden parachute payments (reporting only)",
        "Reporting-only excise tax on excess golden parachute payments (W-2 box 12 code K).", "W-2 box 12 code K", "RO Code K")
    rpt("w2_l", "Substantiated employee business expense reimbursements (reporting only)",
        "Reporting-only amount of nontaxable reimbursements under a per diem or mileage arrangement (W-2 box 12 code L).", "W-2 box 12 code L", "RO Code L")
    rpt("w2_p", "Excludable moving expense reimbursements (reporting only)",
        "Reporting-only amount of moving expense reimbursements that remain excludable for members of the armed forces (W-2 box 12 code P); "
        f"moving expense is otherwise taxable: {val('fed.bik.moving_expense.excluded')} [{rid('fed.bik.moving_expense.excluded')}].", "W-2 box 12 code P", "RO Code P",
        ["US-FEDS5-008"])
    rpt("w2_q", "Nontaxable combat pay (reporting only)",
        "Reporting-only amount of combat pay excluded from wages.", "W-2 box 12 code Q", "RW Nontaxable Combat Pay")
    rpt("w2_nq457", "Nonqualified plan section 457 distributions or contributions (reporting only)",
        "Reporting-only amount of distributions or contributions under a nonqualified plan of a tax-exempt or State employer (W-2 box 11).", "W-2 box 11",
        "RW Nonqualified Plan Section 457 Distributions or Contributions")
    rpt("w2_nqnot457", "Nonqualified plan not section 457 (reporting only)",
        "Reporting-only amount of distributions from a nonqualified plan that is not a section 457 plan (W-2 box 11).", "W-2 box 11", "RW Nonqualified Plan Not Section 457")
    rpt("w2_409a", "Deferrals under a section 409A nonqualified deferred compensation plan (reporting only)",
        "Reporting-only amount deferred under a section 409A plan (W-2 box 12 code Y).", "W-2 box 12 code Y",
        "RW Deferrals Under a Section 409A Nonqualified Deferred Compensation Plan")
    rpt("w2_dd", "Cost of employer-sponsored health coverage (reporting only)",
        "Reporting-only total cost of employer-sponsored health coverage, employer and employee shares, not taxable (W-2 box 12 code DD).",
        "W-2 box 12 code DD", "RW Cost of Employer-Sponsored Health Coverage")
    rpt("w2_ff", "Permitted benefits under a qualified small employer health reimbursement arrangement (reporting only)",
        "Reporting-only amount of permitted benefits under a QSEHRA (W-2 box 12 code FF).", "W-2 box 12 code FF", "RW Permitted Benefits under QSEHRA")
    A("flag_retplan", "Retirement plan active participant flag", "Flag",
      "Flag per employee: active participant in an employer retirement plan during the year; reported in W-2 box 13. Serves "
      + spec_ref("US-SSA-001", "RW Retirement Plan Indicator") + ". Reporting code table: " + W.rq08() + ".",
      tax_code="US-NA", rep="W-2 box 13", legal=["US-FEDS5-007"], fam="flag")

    # ----------------------------------------------------- deferrals without a global deduction code ---
    for sym, name, cd, spec_name in (("ded_408k6", "Pre-tax 408(k)(6) salary reduction - employee deduction", "F", "RW Deferred Comp 408(k)(6)"),
                                     ("ded_501c18", "Pre-tax 501(c)(18)(D) contribution - employee deduction", "H", "RW Deferred Comp 501(c)(18)(D)"),
                                     ("ded_roth401", "Designated Roth 401(k) deferral - employee deduction", "AA", "RW Designated Roth 401(k)"),
                                     ("ded_roth403", "Designated Roth 403(b) deferral - employee deduction", "BB", "RW Designated Roth 403(b)")):
        A(sym, name, "Deduction",
          (f"Employee deferral reported in W-2 box 12 code {cd}: {val('fed.w2.box12.code.' + cd.lower())} [{rid('fed.w2.box12.code.' + cd.lower())}]. " + W.gap("WTC-RQ-03", "the tax treatment of this deferral") +
           f". Serves {spec_ref('US-SSA-001', spec_name)}."),
          tax_code="US-NA", side="EE", rep=f"W-2 box 12 code {cd}", payslip=True, legal=["US-FEDS5-007"], fam="fed_report")

    # ----------------------------------------------------------------- garnishments and deductions ---
    A("garn_support", "Child support income withholding order", "Deduction",
      (f"Income withholding for child support: maximum share of disposable earnings {val('fed.ccpa.support.max_rate.with_dependents')} when the employee supports "
       f"another family and {val('fed.ccpa.support.max_rate.without_dependents')} when not, plus {val('fed.ccpa.support.arrears_addon')} for arrears "
       f"[{rid('fed.ccpa.support.max_rate.with_dependents')}]. Priority between orders: {W.gap('WTC-RQ-13')}. "
       f"Law that governs an interstate order: {val('multi.iwo.governing_law')}; remittance within {val('multi.iwo.remittance_business_days')} "
       f"[{rid('multi.iwo.governing_law')}]. Taken after taxes; it does not change any base. Input: {F.D_IWO}."),
      tax_code="US-NA", side="EE", payslip=True, inputs=[F.D_IWO], legal=["US-FEDS5-023", "US-MULTIS5-007", "US-FEDS5-014"], fam="deduction")
    A("garn_levy", "Federal tax levy on wages", "Deduction",
      (f"Federal tax levy: the amount exempt from the levy depends on filing status, dependents and the pay period; single with no dependents "
       f"{val('fed.levy.exempt.single_0dep.weekly')} weekly, {val('fed.levy.exempt.single_0dep.biweekly')} biweekly, "
       f"{val('fed.levy.exempt.single_0dep.semimonthly')} semimonthly, {val('fed.levy.exempt.single_0dep.monthly')} monthly; plus per dependent "
       f"{val('fed.levy.exempt.per_dependent.weekly')} weekly, {val('fed.levy.exempt.per_dependent.biweekly')} biweekly, "
       f"{val('fed.levy.exempt.per_dependent.semimonthly')} semimonthly, {val('fed.levy.exempt.per_dependent.monthly')} monthly "
       f"[{rid('fed.levy.exempt.single_0dep.weekly')}]. Priority: {W.gap('WTC-RQ-13')}. Taken after taxes; it does not change any base."),
      tax_code="US-NA", side="EE", payslip=True, legal=["US-FEDS5-014"], fam="deduction")
    A("garn_creditor", "Creditor garnishment", "Deduction",
      (f"Garnishment for a commercial debt: maximum {val('fed.ccpa.max_rate')} of disposable earnings; weekly earnings protected from garnishment: "
       f"{W.gap('WTC-RQ-12')}. A State limit that is lower applies instead (State annexes of {W.CCG_REF} "
       f"Module 7). Taken after taxes; it does not change any base."),
      tax_code="US-NA", side="EE", payslip=True, legal=["US-FEDS5-023"], fam="deduction")
    A("ded_union", "Union dues deduction (voluntary, after tax)", "Deduction",
      (f"Union dues or fees taken from net pay on the employee's written authorisation; after-tax, it does not change any base. State authorisation "
       f"rules are in the State annexes of {W.CCG_REF} Module 7."), tax_code="US-NA", side="EE", payslip=True, legal=["US-FEDS5-023"], fam="deduction")
    A("ded_loan", "Loan or advance repayment deduction (voluntary, after tax)", "Deduction",
      (f"Repayment of an employer loan or of an advance of net pay on the employee's written authorisation; after-tax, it does not change any base. "
       f"State authorisation rules are in the State annexes of {W.CCG_REF} Module 7. " + W.gap("WTC-RQ-02", "tax treatment of the advance itself")),
      tax_code="US-NA", side="EE", payslip=True, legal=["US-FEDS5-023"], fam="deduction")
    return reg

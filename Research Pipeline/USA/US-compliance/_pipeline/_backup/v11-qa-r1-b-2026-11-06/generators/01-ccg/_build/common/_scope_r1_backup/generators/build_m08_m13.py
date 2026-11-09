# -*- coding: utf-8 -*-
"""Renderer for CCG units m08_leave, m09_termination, m10_reporting, m11_advanced,
m13_practices and coverage (US build, stage 1). Every factual value is pulled from
_research/*-facts.json through factlib (T = tagged value, B = boolean in words,
REG = register id). Run 01-ccg/_examples/build_examples.py first (m09 examples).
Run: python -I build_m08_m13.py
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import factlib as F  # noqa: E402

T, B, REG, TV, V = F.T, F.B, F.REG, F.TV, F.V
MOD = os.path.join(F.BASE, "01-ccg", "modules")
EX = os.path.join(F.BASE, "01-ccg", "_examples", "out")


def H3(mod, sec, q):
    F.set_loc(f"{mod}.md §{sec} {q}")
    return ["", f"### {q}", ""]


def table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return out


def val(key):
    """Tagged value(s) of a key, booleans in words, all dated values shown."""
    es = F.entries(key)
    if isinstance(es[0]["value"], bool):
        return B(key, "yes", "no")
    return TV(key)


PROGRAMME = {"sick": "", "paid_sick": "", "paid": "", "esst": "ESST ", "esta": "ESTA ", "essl": "ESSL ", "esl": "earned sick leave ",
             "earned_paid": "earned paid leave ", "est": "earned sick time ", "plawa": "PLAWA ", "paid_mandate": "",
             "pto": "PTO ", "vacation": "vacation ", "accrued": "accrued leave ", "pittsburgh": "", "chicago": "",
             "nyc_pto": "", "philadelphia": ""}
LABELS = [
    (r"^accrual(\.hours_worked_per_hour|_ratio_hours_worked)$", "hours worked per hour accrued"),
    (r"^accrual_per_hour_worked$", "hours accrued per hour worked"),
    (r"^accrual\.(\w+)$", r"accrual, \1 employees"),
    (r"^accrual_cap_hours$", "accrual cap (hours)"),
    (r"^usage_cap_hours$|^use_cap_hours$", "use cap (hours)"),
    (r"^annual_cap_hours$", "annual cap (hours)"),
    (r"^annual_accrual_cap_hours$", "annual accrual cap (hours)"),
    (r"^annual_earn_cap_hours$", "annual earning cap (hours)"),
    (r"^balance_cap_hours$", "balance cap (hours)"),
    (r"^cap_hours$", "cap (hours)"),
    (r"^cap_hours\.15_plus_fte$", "cap, 15+ FTE employers (hours)"),
    (r"^cap_hours\.under_15_fte$", "cap, under 15 FTE employers (hours)"),
    (r"^cap_hours\.15_plus$", "cap, 15+ employees (hours)"),
    (r"^cap_hours\.under_15$", "cap, under 15 employees (hours)"),
    (r"^cap_hours\.(\w+)$", r"cap, \1 employers (hours)"),
    (r"^annual_cap\.(\w+)_hours$", r"annual cap, \1 employers (hours)"),
    (r"^annual_cap_hours\.(\w+)$", r"annual cap, \1 employees (hours)"),
    (r"^annual_hours\.(\w+)$", r"annual hours, \1 employees"),
    (r"^(coverage_min_employees|coverage_threshold_employees|employer_threshold|employer_threshold_paid|paid_employer_threshold)$",
     "employer-size threshold for paid leave (employees)"),
    (r"^small_employer_threshold$", "small-employer threshold (employees)"),
    (r"^(state_statute\.exists|state_mandate\.exists|mandate\.exists|statewide)$", "statewide paid-sick-leave law"),
    (r"^exists$", "statewide paid-leave mandate"),
    (r"^rehire_reinstatement_months$", "balance reinstated on rehire within (months)"),
    (r"^waiting_days$|^waiting_period_days$", "waiting period (days)"),
    (r"^use_after_days$", "usable after (days)"),
    (r"^(payout_on_separation|payout_at_separation)$", "paid out at separation"),
    (r"^wages_for_final_pay$", "balance is wages in final pay"),
    (r"^vacation\.payout$|^vacation_payout$", "vacation payout"),
    (r"^vested_vacation_payout$", "vested vacation paid out"),
    (r"^vacation\.payout_after_years$", "vacation payout after (years of service)"),
    (r"^rule$", "rule"),
]


def nice(label):
    toks = label.split(".")
    while len(toks) > 1 and toks[0] in ("leave", "term", "final_pay"):
        toks = toks[1:]
    label = ".".join(toks)
    pre = ""
    if toks[0] in PROGRAMME and len(toks) > 1:
        pre = PROGRAMME[toks[0]]
        label = ".".join(toks[1:])
    for rx, rep in LABELS:
        if re.match(rx, label):
            out = (pre + re.sub(rx, rep, label)).replace("_", " ")
            out = re.sub(r"(\d+) (\d+) employ", r"\1-\2 employ", out)
            out = re.sub(r"(\d+) ?plus\b", r"\1+", out)
            return re.sub(r"\bunder(\d+)", r"under \1", out)
    return (pre + label.replace(".", ", ").replace("_", " ")).strip()


def kv_cell(keys, prefix_rx):
    parts = []
    for k in keys:
        label = re.sub(prefix_rx, "", k)
        parts.append(f"{nice(label)}: {val(k)}")
    return "; ".join(parts)


def sname(st):
    return F.STATE_NAMES.get(st, st)


# ======================================================================== m08
def m08():
    M = "m08_leave"
    L = ["# Module 8: Statutory Leave Management", "",
         "*Purpose: To define the rules for all statutory leave types.*", "",
         "## 8.1 Leave Entitlements", "",
         "Leave in the United States sits on two layers. The federal layer sets job-protected leave and no paid leave "
         "for private employers. The State and local layer sets paid sick leave and the paid family and medical leave "
         "(PFML) or temporary disability insurance (TDI) programmes. Payroll accrues the first and withholds premiums for "
         "the second. The State or its insurer pays the benefit. Per-State detail is in the jurisdiction annexes. "
         "This module gives the federal rules and the comparison tables."]
    L += H3(M, "8.1", "For each type of statutory leave, what are the eligibility criteria and accrual methodology?")
    F.bind("fed.paid_leave.private_employers.exists")
    L += ["**Federal layer.**", ""]
    L += table(["Leave", "Entitlement", "Paid by", "Source"], [
        ("Family and Medical Leave Act (FMLA)", f"Up to {T('fed.fmla.weeks')} workweeks of job-protected leave; up to "
         f"{T('fed.fmla.military_caregiver.weeks')} workweeks to care for a covered servicemember. The leave may be unpaid.",
         "Unpaid (the employer may require accrued paid leave to run concurrently)", REG("fed.fmla.weeks")),
        ("Paid leave for private employers", "None at federal level: "
         + B("fed.paid_leave.private_employers.exists", "a federal paid-leave mandate exists", "no federal paid-leave mandate"),
         "—", REG("fed.paid_leave.private_employers.exists")),
    ])
    L += ["", "FMLA eligibility (employer size, employee service and hours) is not carried as a fact. "
          + F.gap("FMLA employer-coverage and employee-eligibility thresholds (29 U.S.C. 2611) are not keyed.", "fed.fmla.eligibility"),
          "", "Paid sick leave for federal contractors under Executive Order 13706: "
          + F.gap(F.GAP_TEXT["fed.eo13706.sick_leave.accrual"], "fed.eo13706.sick_leave.accrual"), ""]
    # state paid sick leave table
    L += ["**State paid sick leave (Table 8.1.1).** Accrual is per hour worked, so it follows the hours actually worked. "
          "A cap limits either the annual accrual or the use, as the key says. Paid sick leave does not have to be paid out at separation "
          "wherever the facts carry a payout key (Table 8.1.3). Coverage of employees who work only partly in a State is "
          "per State and not established at multistate level: "
          + F.gap(F.GAP_TEXT["multi.sick_leave.coverage_threshold"], "multi.sick_leave.coverage_threshold"), ""]
    rows, none = [], []
    sick_rx = r"\.leave\.(sick|paid_sick|paid|esst|esta|essl|esl|earned_paid|est|plawa|paid_mandate)\."
    for st in F.STATES:
        s = st.lower()
        ks = [k for k in F.keys_matching(rf"^{s}\.leave\.") if re.search(sick_rx, k) and "payout" not in k]
        if not ks:
            none.append(st)
            continue
        rows.append((f"{sname(st)} ({st})", kv_cell(ks, rf"^{s}\.leave\."), " ".join(sorted({F.R(k, value=F.entries(k)[0]['value']) for k in ks}))))
    L += table(["State", "Keyed rule (parameter: value)", "Register"], rows)
    L += ["", "States with no paid-sick-leave key in the facts files: " + ", ".join(none) + ". "
          + F.gap("the facts files carry neither a paid-sick-leave rule nor a statement that none exists for these States; "
                  "see each jurisdiction annex.", "multi.paid_sick_leave.state_census"), ""]
    # local
    loc_keys = [k for k in F.FACTS if re.match(r"^(il\.leave\.chicago|ny\.leave\.nyc_pto|pa\.leave\.(philadelphia|pittsburgh))\.", k)
                and "payout" not in k]
    L += ["**Local paid-leave ordinances (Table 8.1.2).** These apply on top of the State rule for work performed in the city.", ""]
    L += table(["Locality", "Keyed rule (parameter: value)"],
               [(lab, kv_cell(sorted(k for k in loc_keys if k.startswith(pre)), rf"^{re.escape(pre)}\."))
                for lab, pre in (("Chicago (IL)", "il.leave.chicago"), ("New York City (NY)", "ny.leave.nyc_pto"),
                                 ("Philadelphia (PA)", "pa.leave.philadelphia"), ("Pittsburgh (PA)", "pa.leave.pittsburgh"))])
    # other statutory leaves
    other_rx = r"\.leave\.(voting|jury|jury_duty|adoption|military_family|dv_sa|domestic_violence|lactation|family|prenatal|wfmla|pfml\.job_protection)\b"
    ok = sorted(k for k in F.FACTS if re.match(r"^[a-z]{2}\.leave\.", k) and re.search(other_rx, k))
    L += ["", "**Other statutory leaves keyed in the facts (Table 8.1.4).** Examples only; the complete set per State is in the annexes.", ""]
    L += table(["State", "Leave (parameter)", "Value", "Register"],
               [(k[:2].upper(), F.humanize(k.split(".leave.")[1]), val(k), F.R(k, value=F.entries(k)[0]["value"])) for k in ok])

    L += H3(M, "8.1", "How are unpaid or partially paid leaves handled?")
    L += ["- **Unpaid leave (FMLA or employer-approved).** No wages are paid, so nothing is withheld or contributed for "
          "the period. Federal income tax, FICA and FUTA attach to wages *paid* in the calendar year "
          f"({T('fed.tax_year.basis')}) {REG('fed.tax_year.basis')}. The OASDI and FUTA wage bases run per employer per calendar year "
          f"from the first payment. They are not prorated for the absence {REG('fed.futa.wage_base')}.",
          "- **Partially paid leave through a State programme.** PFML and TDI benefits are paid by the State fund or by the "
          "employer's approved insurer, not by payroll (Table 8.1.5). The employee's PFML contribution withheld by payroll "
          f"counts as W-2 wages ({B('fed.pfml.employee_contribution.is_w2_wages', 'employee contribution is W-2 wages', 'not W-2 wages')}) "
          f"{REG('fed.pfml.employee_contribution.is_w2_wages')}.",
          "- **Employer top-up of a State benefit.** The facts do not key how an employer supplement paid alongside a State "
          "benefit is taxed. " + F.gap("treatment of an employer top-up paid during State PFML/TDI leave is not keyed.", "fed.pfml.employer_top_up.treatment")]

    L += H3(M, "8.1", "Which wage types are affected by unpaid/partially paid leave?")
    L += ["The hours-based earnings for the absent hours are not paid. Every wage type whose base follows those hours "
          "therefore falls with them: regular pay, shift and hours-based premiums, and the paid-sick-leave accrual (accrual is per hour worked, Table 8.1.1). "
          "Contributions whose base is wages paid fall automatically: OASDI, Medicare, FUTA, SUI, and PFML/TDI premiums. "
          "The Wage Type Catalogue (WTC) carries the codes and their Subject-to flags. "
          "Massachusetts PFML is the exception to the payment-date rule: its rates apply to wages *earned* on or after 1 January "
          f"{REG('ma.pfml.total.rate')}."]

    L += H3(M, "8.1", "Are there any mandatory national military service leaves?")
    L += ["The United States has no national service obligation in peacetime that payroll must model. Re-employment and "
          "leave rights of reservists and guard members (USERRA) are not carried as a fact. "
          + F.gap("USERRA leave and benefit-continuation rules (38 U.S.C. 4301-4335) are not keyed.", "fed.userra.leave_rules"),
          "", "State military-family leave keyed in the facts: Indiana "
          f"{T('in.leave.military_family.days')} days {REG('in.leave.military_family.days')}."]

    L += H3(M, "8.1", "Are any other kinds of leave paid by government authorities?")
    L += ["Yes. The State PFML and TDI programmes pay wage-replacement benefits from a State fund, an approved private plan or "
          "the employer's insurer. Payroll collects the premium (Module 5 carries the rates and wage bases). "
          "It does not pay the benefit (Table 8.1.5).", ""]
    rows = [
        ("California SDI / PFL", "EDD fund (or voluntary plan, W-2 Box 14 label " + T("ca.sdi.voluntary_plan.w2_box14_label") + ")", "not keyed", REG("ca.sdi.employee.rate")),
        ("Colorado FAMLI", "State FAMLI fund", "not keyed", REG("co.famli.employee.rate")),
        ("Connecticut Paid Leave", "CT Paid Leave Authority", T("ct.pfml.benefit.weekly_max"), REG("ct.pfml.benefit.weekly_max")),
        ("Delaware Paid Leave", "State fund", T("de.pfml.benefit.weekly_max"), REG("de.pfml.benefit.weekly_max")),
        ("District of Columbia Paid Family Leave", "DC fund (employer-funded)", "not keyed", REG("dc.pfml.employer.rate")),
        ("Hawaii TDI", "Employer's insured plan", T("hi.tdi.benefit.weekly_max"), REG("hi.tdi.benefit.weekly_max")),
        ("Maryland FAMLI", "State fund; contributions start " + T("md.pfml.contributions.start"), "not keyed", REG("md.pfml.contributions.start")),
        ("Massachusetts PFML", "Department of Family and Medical Leave",
         T("ma.pfml.benefit.weekly_max", ef="2026-01-01") + " (2026); " + T("ma.pfml.benefit.weekly_max", ef="2027-01-01") + " (from 2027-01-01)",
         REG("ma.pfml.benefit.weekly_max", ef="2026-01-01")),
        ("Maine PFML", "State fund", "not keyed", REG("me.pfml.w2_box14_label")),
        ("Minnesota Paid Leave", "State fund", "not keyed", REG("mn.pfml.rate.total")),
        ("New Jersey TDI / FLI", "State fund or private plan", T("nj.tdi.max_weekly_benefit"), REG("nj.tdi.max_weekly_benefit")),
        ("New York PFL / DBL", "Employer's insurer", "PFL: " + T("ny.pfl.benefit.rate_of_aww") + "% of the employee's average weekly wage, capped at "
         + T("ny.pfl.benefit.max_weekly"), REG("ny.pfl.benefit.max_weekly")),
        ("Oregon Paid Leave", "State fund", "not keyed", REG("or.pfml.rate.total")),
        ("Rhode Island TDI", "State fund", "not keyed", REG("ri.tdi.employee.rate")),
        ("Washington PFML and WA Cares", "State fund", "not keyed", REG("wa.pfml.employee.share", ef="2026-01-01")),
        ("Virginia PFML", "State fund; contributions start " + T("va.pfml.contributions_start"), "not keyed", REG("va.pfml.contributions_start")),
    ]
    L += ["**Table 8.1.5: State programmes that pay leave benefits**", ""]
    L += table(["Programme", "Benefit paid by", "Maximum weekly benefit (USD)", "Register"], rows)
    L += ["", "Where the maximum weekly benefit is \"not keyed\", payroll does not need the figure: the benefit is computed "
          "and paid outside payroll."]

    L += H3(M, "8.1", "What are the payout rules for statutory leaves?")
    L += ["- **FMLA:** no payout; the leave is unpaid unless accrued paid leave is substituted.",
          "- **State PFML/TDI:** the State or insurer pays the benefit directly to the employee. Payroll pays nothing.",
          "- **Paid sick leave:** paid at the employee's regular rate when used. It is not paid out at separation in any State where "
          "the facts carry a payout key (Table 8.1.3).",
          "- **Vacation / PTO:** no federal or general statutory entitlement. Where an employer grants it, payout at "
          "separation is State law (Table 8.1.3 and Module 9, Table 9.1.1)."]

    L += H3(M, "8.1", "How are unused paid leaves treated upon termination?")
    pay_rx = (r"^[a-z]{2}\.(term\.vacation\.payout|term\.vacation\.payout_after_years|final_pay\.vacation_payout|final_pay\.vested_vacation_payout|"
              r"leave\.[a-z_]+\.payout_(on|at)_separation|leave\.(vacation|pto)\.payout_at_separation|leave\.accrued\.wages_for_final_pay|"
              r"leave\.pittsburgh\.payout_at_separation)$")
    pk = sorted(k for k in F.FACTS if re.match(pay_rx, k))
    rows = []
    for st in F.STATES:
        s = st.lower()
        ks = [k for k in pk if k.startswith(s + ".")]
        if ks:
            cell = []
            for k in ks:
                kind = "Vacation/PTO" if re.search(r"vacation|\.pto\.|accrued", k) else "Sick leave"
                cell.append(f"{kind}, {nice(re.sub(rf'^{s}\.', '', k))}: {val(k)}")
            rows.append((f"{sname(st)} ({st})", "; ".join(cell), " ".join(sorted({F.R(k, value=F.entries(k)[0]['value']) for k in ks}))))
    L += ["**Table 8.1.3: Unused leave at separation (keyed States).** \"yes\" means the accrued balance is wages due at separation; "
          "\"no\" means it is not paid out.", ""]
    L += table(["State", "Keyed rule (parameter: value)", "Register"], rows)
    L += ["", "States not listed have no payout key in the facts files. Their annex states the rule or carries the gap. "
          "Where a State makes the balance wages due, payroll pays it with the final wages (Module 9.1 for the withholding method)."]

    L += H3(M, "8.1", "Provide the calculation logic for each leave type where applicable.")
    L += ["```", "# paid sick leave accrual (per State, Table 8.1.1)",
          "accrued_hours += hours_worked / RATIO            # RATIO = hours worked per hour accrued",
          "accrued_hours  = min(accrued_hours, ANNUAL_CAP)  # where the State caps the annual accrual",
          "usable_hours   = min(balance, USE_CAP)           # where the State caps the annual use",
          "pay_for_leave  = hours_taken x regular_rate      # wages: FIT, FICA, FUTA, SUI apply",
          "# Nevada accrues a fraction of an hour per hour worked (Table 8.1.1)",
          "# State PFML/TDI: payroll computes only the premium (Module 5); the benefit is paid by the State or insurer",
          "```", "",
          "The State-specific RATIO, caps and employer-size thresholds are the values in Table 8.1.1. New York PFL is an example "
          f"of a benefit computed outside payroll: {T('ny.pfl.benefit.rate_of_aww')}% of the average weekly wage, capped at "
          f"{T('ny.pfl.benefit.max_weekly')} {REG('ny.pfl.benefit.max_weekly')}. Payroll does not compute it."]

    L += H3(M, "8.1", "How does extended unpaid leave impact social security contributions, tax status, and accrual?")
    L += ["- **Contributions:** none for the unpaid period. Federal and State payroll taxes follow wages paid "
          f"{REG('fed.tax_year.basis')}. The annual wage bases are not reduced or prorated, so contributions resume on the first pay after "
          "return. They resume against the same annual base already used in the calendar year.",
          "- **Tax status:** unchanged. The Form W-4 and the State certificates stay in force. A 2026 claim of exemption from "
          f"withholding lapses at year end regardless of leave ({T('fed.w4.exempt.validity')}) {REG('fed.w4.exempt.validity')}.",
          "- **Accrual:** paid-sick-leave accrual stops, because it is earned per hour worked (Table 8.1.1). Vacation accrual "
          "during unpaid leave is a matter of employer policy; no statutory rule is keyed.",
          "- **State PFML/TDI premiums:** none while no wages are paid. The benefit is paid by the State or insurer."]
    return L


# ======================================================================== m09
def m09():
    M = "m09_termination"
    L = ["# Module 9: Termination & Irregular Payments", "",
         "*Objective: To detail calculation and tax rules for non-standard payments.*", "",
         "## 9.1 Termination Payments"]
    L += H3(M, "9.1", "What are the different types of termination payments?")
    L += table(["Payment", "Rule", "Tax treatment", "Source"], [
        ("Final regular wages", f"{T('fed.final_pay.rule')}. State timing: Table 9.1.1.",
         "Regular wages", REG("fed.final_pay.rule")),
        ("Accrued vacation / PTO", "Payable only where State law or the employer's written policy makes it wages due (Module 8, Table 8.1.3)",
         "Wages", "Module 8"),
        ("Severance pay", "Contractual or policy-based. No general federal severance entitlement is keyed.",
         f"Wages for FIT, FICA and FUTA ({B('fed.severance.is_wages', 'severance is wages', 'severance is not wages')})", REG("fed.severance.is_wages")),
        ("Pay in lieu of WARN notice", f"WARN requires {T('fed.warn.notice_days')} days' notice of a plant closing or mass layoff. "
         "Pay in lieu of the notice is wages.", "Wages", REG("fed.warn.notice_days")),
        ("Maine statutory severance", T("me.severance.mass_layoff"), "Wages", REG("me.severance.mass_layoff")),
        ("New Jersey mass-layoff severance", f"{T('nj.term.warn.severance.weeks_per_year')} week of pay per year of service on a covered mass layoff",
         "Wages", REG("nj.term.warn.severance.weeks_per_year")),
    ])
    L += ["", "**Fixed-term contracts.** Employment is at will and a fixed term is a matter of contract; no federal or general State "
          "fixed-term regime exists. The expiry of the term is a separation: final wages follow Table 9.1.1, and any State separation "
          f"notice below applies (Module 11, 11.3; [US-SDS5-010], [US-TNS5-012], {REG('fed.final_pay.rule')})."]
    L += ["", "**Table 9.1.1: State final-pay timing (keyed States).** Timing runs from the separation. Discharge and resignation "
          "differ in many States.", ""]
    rows, none = [], []
    for st in F.STATES:
        s = st.lower()
        ks = F.keys_matching(rf"^{s}\.(final_pay|term\.final_pay)\.")
        ks = [k for k in ks if "vacation" not in k]
        if not ks:
            none.append(st)
            continue
        rows.append((f"{sname(st)} ({st})", kv_cell(ks, rf"^{s}\.(term\.)?final_pay\."),
                     " ".join(sorted({F.R(k, value=F.entries(k)[0]['value']) for k in ks}))))
    L += table(["State", "Keyed rule (parameter: value)", "Register"], rows)
    L += ["", "States with no final-pay key in the facts files: " + ", ".join(none) + ". "
          + F.gap("final-pay timing is not keyed for these States; see each jurisdiction annex.", "multi.final_pay.state_census"),
          "", "**State separation notices keyed in the facts:** California " + T("ca.separation_notice") + " " + REG("ca.separation_notice")
          + "; Connecticut " + T("ct.separation_notice") + " " + REG("ct.separation_notice")
          + "; Georgia " + T("ga.separation_notice.dol800") + " " + REG("ga.separation_notice.dol800")
          + "; New Jersey " + T("nj.term.separation_notice.form") + " " + REG("nj.term.separation_notice.form")
          + "; Tennessee within " + T("tn.term.separation_notice.hours") + " hours " + REG("tn.term.separation_notice.hours") + "."]

    L += H3(M, "9.1", "How do termination rules and calculations differ by residential status and employer type?")
    L += ["- **Federal resident vs nonresident alien.** Severance and final wages are wages for both. For a nonresident alien the "
          "nonresident add-on increases the wage used in the regular withholding computation only. It is not applied to "
          "supplemental wages withheld at the flat rate "
          f"({B('fed.fit.nra_addon.applies_to_supplemental_flat', 'the add-on applies to the flat rate', 'the add-on is not applied to the flat-rate method')}) "
          f"{REG('fed.fit.nra_addon.applies_to_supplemental_flat')}. Treaty-exempt wages claimed on Form 8233 go on Form 1042-S, "
          f"not on Form W-2 ({T('fed.fit.nra.treaty_exempt.reporting')}) {REG('fed.fit.nra.treaty_exempt.reporting')}.",
          "- **State residence.** Final-pay timing follows the work State (Table 9.1.1). State withholding on a termination "
          "payment follows the same residence/work-State routing as regular wages (Module 6 and the MULTI annex).",
          "- **Employer type and size.** WARN applies to covered plant closings and mass layoffs. Maine's statutory severance "
          "applies to establishments of the size stated in the first table of 9.1. Household and agricultural employers follow the "
          "special thresholds of Module 11."]

    L += H3(M, "9.1", "Detail the calculation and tax withholding rules for unused leave paid out on termination.")
    L += ["- **When it is due:** only where Module 8, Table 8.1.3 makes the balance wages due, and on the final-pay date of "
          "Table 9.1.1.",
          "- **Federal withholding:** where due, the payout is paid with the final wages. "
          + f"Classification: {T('fed.vacation_payout.supplemental_status')} "
          f"{REG('fed.vacation_payout.supplemental_status')}. A lump-sum payout of unused leave is withheld on with the "
          "supplemental-wage methods of Module 6 §6.2 (optional flat rate or aggregate).",
          f"- **State example:** Louisiana withholds vacation pay like regular wages, with no flat supplemental rate ({T('la.wh.supplemental.method')}) "
          f"{REG('la.wh.supplemental.method')}."]

    L += H3(M, "9.1", "Describe the rules for statutory severance/redundancy payments.")
    L += [f"Federal law sets a notice duty, not a severance entitlement. WARN requires {T('fed.warn.notice_days')} days' notice "
          f"of a covered plant closing or mass layoff {REG('fed.warn.notice_days')}. Pay in lieu of the notice is wages. Statutory severance "
          f"keyed in the facts: Maine ({T('me.severance.mass_layoff')}) {REG('me.severance.mass_layoff')}; New Jersey "
          f"{T('nj.term.warn.severance.weeks_per_year')} week per year of service on a covered mass layoff {REG('nj.term.warn.severance.weeks_per_year')}. "
          "Severance is withheld as supplemental wages (9.2)."]

    L += H3(M, "9.1", "Provide the statutory formula for any tax-free portion.")
    L += ["**Federal:** none. Severance is wages for FIT, FICA and FUTA in full " + REG("fed.severance.is_wages") + ".",
          "", f"**Alabama:** severance pay up to {T('al.wh.severance.exempt_max')} is exempt from Alabama withholding "
          f"{REG('al.wh.severance.exempt_max')}.", "", "```",
          "AL_exempt_part  = min(severance, AL_SEVERANCE_EXEMPT_MAX)",
          "AL_taxable_part = severance - AL_exempt_part      # withheld under the AL method",
          "FED_taxable     = severance                       # no federal exclusion",
          "```"]

    L += H3(M, "9.1", "For other Employment Termination Payments (ETPs), provide a reference guide.")
    L += table(["Payment", "FIT", "OASDI / Medicare", "FUTA", "Reported on"], [
        ("Final wages, overtime, commissions", "Regular method", "Yes", "Yes", "W-2"),
        ("Severance / pay in lieu of notice", "Supplemental (flat or aggregate)", "Yes", "Yes", "W-2"),
        ("Bonus paid at exit", "Supplemental (flat or aggregate)", "Yes", "Yes", "W-2"),
        ("Accrued vacation payout (where due)", "Paid with final wages (regular or supplemental: gap above)", "Not keyed (gap above)", "Not keyed (gap above)", "W-2"),
        ("Treaty-exempt wages of a nonresident alien", "Per Form 8233", "Per the nonresident rules", "Per the nonresident rules", "1042-S"),
    ])
    F.bind("fed.severance.is_wages")
    F.bind("fed.fit.supplemental.flat_rate")
    F.bind("fed.fit.nra.treaty_exempt.reporting")

    L += H3(M, "9.1", "Detail the rules for any applicable concessional tax cap.")
    L += ["No federal concessional cap applies to termination payments. Supplemental wages paid to one employee above "
          f"{T('fed.fit.supplemental.mandatory_threshold')} in the calendar year must be withheld at "
          f"{T('fed.fit.supplemental.mandatory_rate')}% {REG('fed.fit.supplemental.mandatory_rate')}. This is a mandatory higher rate, not a concession. "
          f"Alabama's severance exemption ({T('al.wh.severance.exempt_max')}) is the only State cap keyed in the facts."]

    L += H3(M, "9.1", "Provide a detailed worked example of a redundancy termination payout.")
    L += open(os.path.join(EX, "m09_redundancy.md"), encoding="utf-8").read().rstrip("\n").split("\n")

    L += ["", "## 9.2 Irregular and Retrospective Payments"]
    L += H3(M, "9.2", "Describe the specific tax calculation method required for irregular payments.")
    L += ["Bonuses, commissions, severance and similar payments are **supplemental wages**. Three federal rules apply "
          f"{REG('fed.fit.supplemental.flat_rate')}:",
          f"1. **Optional flat rate** of {T('fed.fit.supplemental.flat_rate')}%, when the supplemental payment is identified separately from regular wages.",
          "2. **Aggregate method:** the supplemental payment is withheld together with regular wages under the regular tables "
          "(procedure detail: Module 11.1, gap).",
          f"3. **Mandatory rate:** above {T('fed.fit.supplemental.mandatory_threshold')} of supplemental wages in the year, "
          f"{T('fed.fit.supplemental.mandatory_rate')}% applies to the excess, whatever the W-4.",
          "", "FICA and FUTA apply as to any wage. **Table 9.2.1** lists the State supplemental rules keyed in the facts.", ""]
    sk = sorted(k for k in F.FACTS if re.match(r"^[a-z]{2}\.(wh|pit)\.supplemental", k))
    L += table(["State", "Rule (parameter: value)", "Register"],
               [(f"{sname(k[:2].upper())} ({k[:2].upper()})", f"{nice(k.split('supplemental', 1)[1].lstrip('.') or 'rule')}: {val(k)}",
                 F.R(k, value=F.entries(k)[0]["value"])) for k in sk])

    L += H3(M, "9.2", "How are backdated payments and retrospective salary adjustments handled?")
    L += ["Federal payroll taxes follow the **payment date**, not the period the pay relates to "
          f"({T('fed.tax_year.basis')}) {REG('fed.tax_year.basis')}. A retroactive increase paid in 2026 is 2026 wages. It takes the 2026 "
          "tables and the 2026 wage bases, even when it relates to 2025. Massachusetts PFML is the exception: its rate follows the wages "
          f"earned date {REG('ma.pfml.total.rate')}. "
          + F.gap("the federal classification of back pay and retroactive increases (supplemental or regular wages) is not keyed.",
                  "fed.backpay.treatment")]

    L += H3(M, "9.2", "For arrears, how are contributions and deductions computed?")
    L += ["- Arrears paid now are wages of the payment period. OASDI is due on the lesser of the arrears and the remaining "
          f"annual wage base ({T('fed.fica.oasdi.wage_base', ef='2026-01-01')} for 2026) {REG('fed.fica.oasdi.wage_base', ef='2026-01-01')}. "
          "Medicare is due on the full amount. Additional Medicare is due on the part above "
          f"{T('fed.fica.addl_medicare.withholding_threshold')} of wages paid in the year {REG('fed.fica.addl_medicare.withholding_threshold')}.",
          "- FIT uses the supplemental method if the arrears are paid separately (9.2), or the aggregate method if they are paid with regular wages.",
          "- Child-support arrears withheld under an income withholding order follow the CCPA limits "
          f"(add {T('fed.ccpa.support.arrears_addon')} percentage points when arrears exceed 12 weeks) {REG('fed.ccpa.support.arrears_addon')}; see Module 7."]

    L += H3(M, "9.2", "Provide a worked example of a bonus calculation.")
    L += open(os.path.join(EX, "m09_bonus.md"), encoding="utf-8").read().rstrip("\n").split("\n")
    return L


# ======================================================================== m10
def m10():
    M = "m10_reporting"
    L = ["# Module 10: Reporting, Compliance & Finalisation", "",
         "*Purpose: To define all statutory reporting obligations and final processing rules.*", "",
         "## 10.1 Statutory Reporting", "",
         "Field-level content of every return lives in the Report Specifications (04-reports-spec). Channels and "
         "authorisations live in the Statutory Integration Research (03-statutory-integrations). This module states "
         "the obligations."]
    L += H3(M, "10.1", "Describe the country's primary digital payroll reporting system.")
    L += ["There is no single national payroll reporting system. Each layer is reported separately:",
          f"- **Federal (IRS):** Form 941 quarterly ({T('fed.form941.frequency')}) {REG('fed.form941.frequency')}, "
          f"Form 940 annual ({T('fed.form940.due')}) {REG('fed.form940.due')}, and deposits on the schedule set by the lookback liability "
          f"(monthly up to {T('fed.deposit.monthly_max_lookback_liability')}, semiweekly above it, next day from {T('fed.deposit.next_day_threshold')}) "
          f"{REG('fed.deposit.monthly_max_lookback_liability')}.",
          f"- **Federal (SSA):** Forms W-2/W-3 filed electronically in the EFW2 format ({T('sir.fed.w2.format')}) {REG('sir.fed.w2.format')}, "
          f"fixed records of {T('fed.efw2.record_length')} bytes {REG('fed.efw2.record_length')}. Tax-year 2026 changes: {T('fed.efw2.ty2026_changes')} "
          f"{REG('fed.efw2.ty2026_changes')}.",
          f"- **State:** income-tax withholding returns to every State where withholding applies, and the UI quarterly wage report "
          f"to the State of UI coverage only ({T('multi.ui_wage_report.routing')}) {REG('multi.ui_wage_report.routing')}.",
          "- **Local:** separate local returns where a locality collects its own tax (Module 6 and the PA, OH, MI, KY, MO, AL, CO, DE, OR, WV and NJ annexes).",
          "", "**Filing channel for this build.** Federal and State filings are submitted through a third-party filing provider; "
          "there is no ADP integration (owner decision recorded in MANDATE.md). The employer authorises the agent on Form 8655 "
          f"({T('fed.reporting_agent.authorization')}) {REG('fed.reporting_agent.authorization')}. The employer remains liable for the tax. "
          f"Third-party payer arrangements are described in Pub. 15 ({T('sir.fed.third_party_payer.rules')}) {REG('sir.fed.third_party_payer.rules')}."]

    L += H3(M, "10.1", "Provide a Data Disaggregation Mapping Guide describing main reporting categories.")
    L += table(["Reporting category", "Built from payroll", "Federal return / form", "State / local", "Source"], [
        ("Wages subject to federal income tax, and FIT withheld", "Taxable earnings less pre-tax exclusions; FIT per period",
         "941 (quarter), W-2 (year)", "State wages and tax on the State W-2 copy", REG("fed.form941.frequency")),
        ("Social security (OASDI) wages and tax", f"Wages up to the annual base {T('fed.fica.oasdi.wage_base', ef='2026-01-01')}",
         "941, W-2", "—", REG("fed.fica.oasdi.wage_base", ef="2026-01-01")),
        ("Medicare wages and tax, Additional Medicare", f"All wages; Additional Medicare above {T('fed.fica.addl_medicare.withholding_threshold')}",
         "941, W-2", "OH municipal base starts from Medicare wages (Module 6)", REG("fed.fica.addl_medicare.withholding_threshold")),
        ("FUTA wages", f"First {T('fed.futa.wage_base')} per employee per year", "940 (deposit when liability exceeds "
         + T("fed.futa.deposit_threshold") + ")", "SUI taxable wages per State base", REG("fed.futa.deposit_threshold")),
        ("Tips, qualified overtime, Trump-account contributions", T("fed.w2.box12.new_codes"), "W-2 box 12 (new 2026 codes)", "—", REG("fed.w2.box12.new_codes")),
        ("Tipped occupation", T("fed.w2.box14b"), "W-2 box 14b", "—", REG("fed.w2.box14b")),
        ("State and local wages and tax", "Per State and locality of withholding", "—",
         f"W-2 boxes 15-20, up to {T('multi.w2.states_per_form')} States and localities per form", REG("multi.w2.states_per_form")),
        ("State PFML/SDI employee contributions", "Employee premium per programme", "Box 14 (informational)",
         f"Labels e.g. CA {T('psl.w2.box14.ca_sdi')}; ME {T('me.pfml.w2_box14_label')}", REG("psl.w2.box14.ca_sdi")),
        ("UI wages per employee", "Gross wages, taxable wages, (some States) hours and occupation", "—",
         "UI quarterly wage report to the State of coverage", REG("multi.ui_wage_report.routing")),
    ])

    L += H3(M, "10.1", "List all other mandatory reports, stating the frequency, file format, due date, reporting authority.")
    L += ["**Table 10.1.1: Federal reports**", ""]
    L += table(["Report", "Authority", "Frequency / due", "Format / channel", "Source"], [
        ("Form 941", "IRS", T("fed.form941.frequency"), "Electronic via the filing agent", REG("fed.form941.frequency")),
        ("Form 944 (instead of 941)", "IRS", f"Annual, only on written IRS notice (liability up to {T('fed.form944.max_liability')})", "Electronic via the filing agent", REG("fed.form944.max_liability")),
        ("Form 940 (FUTA)", "IRS", T("fed.form940.due"), "Electronic via the filing agent", REG("fed.form940.due")),
        ("Forms W-2 / W-3", "SSA", f"Due {T('fed.w2.due_date')}; a W-2 is required even with no withholding from {T('fed.w2.no_withholding_threshold')} of wages",
         T("sir.fed.w2.format"), REG("fed.w2.due_date")),
        ("Form 1042-S", "IRS", T("fed.form1042s.channel"), "IRIS", REG("fed.form1042s.channel")),
        ("Forms 1094-C / 1095-C (ACA)", "IRS", f"Annual, for applicable large employers ({T('fed.aca.ale.fte_threshold')} or more full-time incl. equivalent employees)",
         f"Electronic filing at {T('fed.aca.efile_threshold')} or more returns", REG("fed.aca.ale.fte_threshold")),
        ("New-hire report", "State Directory of New Hires", f"Within {T('fed.newhire.deadline_days')} days of hire (shorter in many States, Table 10.1.2)",
         T("fed.newhire.form"), REG("fed.newhire.deadline_days")),
        ("Davis-Bacon certified payroll", "Contracting agency", T("fed.davis_bacon.certified_payroll.frequency"), "Paper or electronic to the agency (optional DOL form named in the rule)", REG("fed.davis_bacon.certified_payroll.frequency")),
    ])
    L += ["", "Instructions for the tax-year 2026 Forms 940 and 1094-C/1095-C are not yet issued; the 2025 editions were read. "
          + F.gap(F.GAP_TEXT["fed.form940.instructions_current"], "fed.form940.instructions_current"), ""]
    L += ["**Table 10.1.2: State reporting parameters keyed in the facts.** The withholding-return and reconciliation forms "
          "per State are in the annexes and the Report Specifications.", ""]
    rows = []
    for st in F.STATES:
        s = st.lower()
        cells = []
        for k in (f"{s}.newhire.report_days", f"{s}.report.ui.quarterly_due", f"{s}.report.w2.efile_threshold"):
            cells.append(val(k) if F.has(k) else "—")
        if any(c != "—" for c in cells):
            rows.append([f"{sname(st)} ({st})"] + cells)
    L += table(["State", "New-hire report (days)", "UI quarterly report due", "W-2 e-file threshold (forms)"], rows)
    L += ["", "\"—\" means the parameter is not keyed for that State at this level (see the annex). Multistate employers that report "
          f"electronically may report all new hires to one State ({T('multi.newhire.designated_state')}) {REG('multi.newhire.designated_state')}. "
          + F.gap(F.GAP_TEXT["multi.newhire.registration_channel"], "multi.newhire.registration_channel")]

    L += H3(M, "10.1", "What pay elements are required as intermediates from payroll for reporting?")
    L += ["Per employee and per period, the payroll engine must keep (and accumulate per quarter and per year):",
          "- gross wages; wages subject to FIT; FIT withheld;",
          "- OASDI wages (capped at the annual base) and tax, employee and employer;",
          "- Medicare wages and tax, employee and employer; wages above the Additional Medicare threshold and that tax;",
          "- FUTA taxable wages (first " + T("fed.futa.wage_base") + ");",
          "- per State: State wages, State tax withheld, SUI gross and taxable wages, PFML/SDI premium wages and premiums;",
          "- per locality: local wages and local tax;",
          "- the 2026 W-2 box 12 amounts " + T("fed.w2.box12.new_codes") + " " + REG("fed.w2.box12.new_codes") + ", and the tipped-occupation code;",
          "- hours worked and occupation where a State UI or PFML report requires them (e.g. Washington: "
          + T("wa.report.pfml_ltc.fields") + " " + REG("wa.report.pfml_ltc.fields") + ")."]

    L += ["", "## 10.2 Integrations"]
    L += H3(M, "10.2", "Is there any mandatory inbound integration?")
    L += ["- **Income withholding orders (child support):** the employer must act on IWOs received from State agencies "
          "(paper or e-IWO). For interstate orders the employer applies the law of the employee's principal place of employment "
          f"({T('multi.iwo.governing_law')}) {REG('multi.iwo.governing_law')}. It remits within {T('multi.iwo.remittance_business_days')} "
          f"business days {REG('multi.iwo.remittance_business_days')}. The current federal IWO form is approved until {T('fed.iwo.omb_expiry')} "
          f"{REG('fed.iwo.omb_expiry')}. " + F.gap(F.GAP_TEXT["fed.iwo.revised_form.state_golive"], "fed.iwo.revised_form.state_golive"),
          "- **IRS levies** on wages follow Pub. 1494 exemption amounts (Module 7). Order of priority: "
          f"{T('fed.iwo.priority')} {REG('fed.iwo.priority')}.",
          "- No system-to-system inbound feed from a tax authority (such as a tax-code notice) is mandatory. Withholding "
          "certificates come from the employee (W-4 and State forms)."]
    L += H3(M, "10.2", "Is there any mandatory outbound integration beyond standard reporting?")
    L += [f"- **New-hire reporting** ({T('fed.newhire.fields')}) {REG('fed.newhire.fields')}. Electronic filers transmit "
          f"{T('fed.newhire.electronic_interval')} {REG('fed.newhire.electronic_interval')}.",
          f"- **Certified payroll** on public works: federal Davis-Bacon weekly {REG('fed.davis_bacon.certified_payroll.frequency')}; "
          f"California electronic upload ({T('ca.prevailing_wage.certified_payroll')}) {REG('ca.prevailing_wage.certified_payroll')}.",
          "- All statutory filings go through the third-party filing provider (owner decision). The SIR documents the handoff."]

    L += ["", "## 10.3 Payslip Requirements"]
    L += H3(M, "10.3", "List all mandatory components that must be itemized on an employee payslip.")
    L += [f"**Federal:** no federal law requires a pay statement ({B('psl.fed.statement.required', 'required', 'not required')}) "
          f"{REG('psl.fed.statement.required')}. The FLSA requires records only. They are kept {T('fed.records.flsa.retention_years')} years "
          f"{REG('fed.records.flsa.retention_years')}. Employment-tax records are kept {T('fed.records.irs.retention_years')} years "
          f"{REG('fed.records.irs.retention_years')}.",
          f"**Which State's rule applies:** {T('multi.payslip.reach.default')} {REG('multi.payslip.reach.default')}. "
          "The payslip is in English (owner decision US-OWN-006).", "",
          "**Table 10.3.1: State pay-statement rules keyed in the facts**", ""]
    rows = []
    for st in F.STATES:
        s = st.lower()
        ks = F.keys_matching(rf"^psl\.{s}\.(statement|sick_leave|pay_code_guide)") + F.keys_matching(rf"^{s}\.payslip\.")
        if ks:
            rows.append((f"{sname(st)} ({st})", kv_cell(ks, rf"^(psl\.{s}|{s})\."), " ".join(sorted({F.R(k, value=F.entries(k)[0]['value']) for k in ks}))))
    L += table(["State", "Keyed rule (parameter: value)", "Register"], rows)
    L += ["", "States not listed carry their pay-statement rule (or its absence) in the annex and in the Payslip "
          "Generator research. The Payslip Generator implements the union of these items."]

    L += ["", "## 10.4 Other Compliance"]
    L += H3(M, "10.4", "Is payroll software certification mandatory?")
    L += ["No general federal certification of payroll software is keyed. A filing agent is authorised per employer on Form 8655 "
          f"{REG('sir.fed.agent_authorization.form')}. That is an authorisation, not a software certification. Agent-list changes go "
          f"through the IRS channel described in Pub. 1474 ({T('sir.fed.reporting_agent.tech_spec')}) {REG('sir.fed.reporting_agent.tech_spec')}. "
          f"State example: Wisconsin ({T('sir.wi.provider_registration')}) {REG('sir.wi.provider_registration')}. "
          + F.gap("a census of State software-certification or provider-testing duties (beyond Wisconsin) is not keyed.",
                  "multi.payroll_software.certification")]

    L += ["", "## 10.5 Year-End Processing and Finalisation"]
    L += H3(M, "10.5", "Describe the mandatory year-end finalisation process.")
    L += ["There is no employer-side income-tax regularisation. The employee settles at assessment (Form 1040 and State returns). "
          "The employer's year end is a reconciliation:",
          f"1. Reconcile the four quarterly Forms 941 to the W-2/W-3 totals {REG('fed.form941.frequency')}.",
          f"2. File Form W-2/W-3 with SSA by {T('fed.w2.due_date')} {REG('fed.w2.due_date')}.",
          f"3. File Form 940 ({T('fed.form940.due')}) {REG('fed.form940.due')}.",
          "4. File each State's annual withholding reconciliation and State W-2 copies (Report Specifications; e.g. Michigan "
          f"{T('mi.report.annual.5081')} {REG('mi.report.annual.5081')}).",
          f"5. Collect new W-4 exemption claims for the next year ({T('fed.w4.exempt.validity')}) {REG('fed.w4.exempt.validity')}.",
          "6. Reset the annual accumulators (OASDI, FUTA, SUI and PFML bases, Additional Medicare threshold) at the first payment "
          f"date of the new year. The 2027 OASDI base is {T('fed.fica.oasdi.wage_base', ef='2027-01-01')} {REG('fed.fica.oasdi.wage_base', ef='2027-01-01')}.",
          "", "TY2027 federal indexation is not yet published: " + F.gap(F.GAP_TEXT["fed.indexation.publication_2027"], "fed.indexation.publication_2027")]
    L += H3(M, "10.5", "What documentation or annual statements must be provided to employees?")
    L += [f"- **Form W-2** by {T('fed.w2.due_date')} {REG('fed.w2.due_date')}. For a terminated employee: {T('fed.w2.terminated_employee.furnishing')} "
          f"{REG('fed.w2.terminated_employee.furnishing')}. State examples: Delaware within {T('de.report.w2.employee_on_termination_days')} days of termination on request "
          f"{REG('de.report.w2.employee_on_termination_days')}; Mississippi within {T('ms.term.w2_after_termination.days')} days {REG('ms.term.w2_after_termination.days')}.",
          "- The SSN may be truncated to its last four digits on the employee copies of Form W-2 only, never on Copy A; the EIN is never truncated "
          f"{REG('fed.ssn.truncation.format')}" + ("" if F.bind("fed.ssn.truncation.format") else "") + ".",
          f"- **Form 1042-S** for treaty-exempt wages of nonresident aliens {REG('fed.form1042s.channel')}.",
          f"- **Form 1095-C** for employees of an applicable large employer {REG('fed.aca.ale.fte_threshold')}."]
    L += H3(M, "10.5", "Is there a formal process for correcting errors discovered after the fiscal year has been closed?")
    L += [f"Yes. Wage statements are corrected on Form W-2c, filed electronically in the EFW2C format ({T('sir.fed.w2.format')}) "
          f"{REG('sir.fed.w2.format')}. Quarterly returns are corrected on Form 941-X {REG('fed.form941.frequency')}. Excess OASDI withheld "
          "because of multiple employers is refunded to the employee at assessment, not by the employer. States have their own "
          f"amendment routes; for example Alabama UI ({T('al.report.sui.quarterly')}) {REG('al.report.sui.quarterly')} and Massachusetts W-2 "
          f"({T('ma.report.w2')}) {REG('ma.report.w2')}."]
    return L


# ======================================================================== m11
def m11():
    M = "m11_advanced"
    L = ["# Module 11: Advanced Scenarios & Cross-Cutting Logic", "",
         "*Purpose: To capture complex, overarching rules that affect multiple aspects of payroll.*", "",
         "## 11.1 Calculation Logic"]
    L += H3(M, "11.1", "How is the proration and projection logic applied for income tax, social security, exemptions, and deductions?")
    L += [f"- **Income tax: projection, not proration.** The federal method annualises the period wage by the number of pay periods "
          f"({T('fed.fit.pay_periods_per_year')}) {REG('fed.fit.pay_periods_per_year')}, applies the annual tables and divides by the periods "
          f"({T('fed.fit.method')}) {REG('fed.fit.method')}. There is no cumulative true-up. A part-period pay (joiner or leaver) is "
          "withheld on the wages actually paid with the normal period frequency. Most State formulas follow the same pattern "
          "(Module 12, 12.2.2).",
          "- **Exemptions and allowances:** annual amounts divided by the periods. Example: Michigan's annual exemption "
          f"{T('mi.wh.exemption.annual')} becomes {T('mi.wh.exemption.biweekly')} biweekly {REG('mi.wh.exemption.biweekly')}.",
          "- **Social security:** no proration and no projection. OASDI applies to wages paid up to the annual base "
          f"({T('fed.fica.oasdi.wage_base', ef='2026-01-01')}) per employer. FUTA applies to the first {T('fed.futa.wage_base')}. Each period takes "
          "the rate × the lesser of the remaining base and the period wage (Module 12, Scenario C).",
          "- **Deductions:** garnishment limits are per pay period (Module 7). Plan limits (401(k), HSA) are annual caps "
          "applied cumulatively."]
    L += H3(M, "11.1", "If tax or contribution rates change mid-pay period, which rates apply?")
    L += ["The rates and tables in force on the **payment date** apply to the whole payment "
          f"({T('fed.tax_year.basis')}) {REG('fed.tax_year.basis')}. A December-earned wage paid in January takes the new year's federal "
          f"rates and bases {REG('fed.fica.oasdi.wage_base', ef='2026-01-01')}. Exception: Massachusetts PFML applies to wages earned on or after "
          f"1 January {REG('ma.pfml.total.rate')}.", "", "**Mid-year 2026 changes to date by payment date (Table 11.1.1)**", ""]
    L += table(["Change", "Value", "Source"], [
        # round 2 (QA r1 C32/C41): GA split by level; the 2025 rate is history and is not shown
        ("Georgia income tax", "Withholding rate " + T("ga.wh.rate", ef="2026-01-01") + "% for payments to 2026-05-10, "
         + T("ga.wh.rate", ef="2026-05-11") + "% from 2026-05-11; tax year 2026 assessment rate "
         + T("ga.pit.rate.flat", ef="2026-01-01") + "% (retroactive to 1 January); law " + T("ga.live.hb463.status")
         + ". Withholding examples dated from 2026-05-11 (Module 12)",
         REG("ga.wh.rate", ef="2026-01-01") + " " + REG("ga.wh.rate", ef="2026-05-11")),
        ("Ohio withholding tables", "Effective " + T("oh.wh.tables.effective_from"), REG("oh.wh.tables.effective_from")),
        ("Indiana county rates", T("in.county.change_dates"), REG("in.county.change_dates")),
        ("Idaho single zero bracket (biweekly)", TV("id.wh.zero_bracket.single.biweekly"), REG("id.wh.zero_bracket.single.biweekly", on="2026-08-01")),
        ("Philadelphia wage tax (resident / nonresident)", TV("pa.local.philadelphia.resident.rate") + " / " + TV("pa.local.philadelphia.nonresident.rate"),
         REG("pa.local.philadelphia.resident.rate")),
        ("District of Columbia minimum wage", TV("dc.minwage.hourly"), REG("dc.minwage.hourly", on="2026-08-01")),
        ("Oregon standard minimum wage", TV("or.labour.minwage.standard.hourly"), REG("or.labour.minwage.standard.hourly", on="2026-08-01")),
        ("Trump-account employer contribution exclusion", T("fed.bik.trump_account.employer_contribution_max") + F.dated("fed.bik.trump_account.employer_contribution_max"),
         REG("fed.bik.trump_account.employer_contribution_max")),
    ])
    L += H3(M, "11.1", "How are tax and social security handled when an employee is paid multiple times in a single pay period?")
    L += ["- **FIT:** a second payment in the period is a supplemental wage. Either withhold the optional flat "
          f"{T('fed.fit.supplemental.flat_rate')}% on it (if identified separately), or aggregate it with the regular wages of the period and "
          f"withhold on the total {REG('fed.fit.supplemental.flat_rate')}. "
          f"Aggregate procedure: {T('fed.fit.supplemental.aggregate_method')} {REG('fed.fit.supplemental.aggregate_method')}.",
          "- **FICA and FUTA:** computed payment by payment against the cumulative annual bases. OASDI is the rate × the lesser of "
          "the remaining base and the payment. Additional Medicare applies to the part of the cumulative wages above "
          f"{T('fed.fica.addl_medicare.withholding_threshold')} {REG('fed.fica.addl_medicare.withholding_threshold')}."]
    L += H3(M, "11.1", "How is payroll calculated if an employee's pay cycle changes mid-year?")
    L += ["Each payment uses the pay-period table of its own frequency (" + T("fed.fit.pay_periods_per_year") + ") "
          f"{REG('fed.fit.pay_periods_per_year')}. Annual wage bases are unaffected because they run on wages paid. "
          + F.gap("the IRS rule for a change of payroll period within the year, or for a short transitional period, is not keyed.",
                  "fed.fit.pay_frequency_change")]

    L += ["", "## 11.2 Special Employee Groups & Income"]
    L += H3(M, "11.2", "How does taxation and social security differ for part-time employees and Board of Directors?")
    L += ["- **Part-time employees:** no separate regime. Withholding uses the same method on the wages of the period; FICA "
          "applies from the first dollar. Part-time hours count toward the ACA full-time-equivalent test "
          f"({T('fed.aca.ale.fte_threshold')}) {REG('fed.aca.ale.fte_threshold')} (Module 12, Scenario B).",
          "- **Corporate officers** are employees. Their wages take FIT withholding, FICA and FUTA, and State law includes "
          f"officers for withholding (Oklahoma {REG('multi.resident_out_of_state.ok.withholding_rule')}) and for UI coverage. "
          "**Directors' fees** paid to a non-employee director are not wages and fall outside payroll (self-employment income). "
          f"**Statutory employees:** {T('fed.statutory_employee.treatment')} {REG('fed.statutory_employee.treatment')}."]
    L += H3(M, "11.2", "How is taxation handled for employees with multiple employers?")
    L += ["Each employer withholds and applies the wage bases on its own. The OASDI and FUTA bases are per employer. "
          f"Additional Medicare starts at {T('fed.fica.addl_medicare.withholding_threshold')} of wages paid by that employer. "
          "Excess OASDI from several employers is refunded at assessment. The employee coordinates FIT through W-4 Step 2. When Step 2 "
          f"is checked, the Step-2-checked schedule applies and the line 1g amount ({T('fed.fit.worksheet1a.line1g.other')} / "
          f"{T('fed.fit.worksheet1a.line1g.mfj')}) is not subtracted {REG('fed.fit.worksheet1a.line1g.other')}. "
          + F.gap(F.GAP_TEXT["fed.common_paymaster.rule"], "fed.common_paymaster.rule")]
    L += H3(M, "11.2", "What is the treatment of foreign-sourced employment income for residents?")
    L += [f"- **Federal:** US citizens and residents are taxed on worldwide wages. For a US citizen working abroad the employer may stop FIT "
          f"withholding on a Form 673 statement ({T('fed.citizen_abroad.form673')}) {REG('fed.citizen_abroad.form673')}. The foreign "
          f"earned income exclusion for 2026 is {T('fed.feie.amount')} {REG('fed.feie.amount')}. FICA follows its own coverage rules.",
          f"- **State:** {T('multi.pit.sourcing.general')} {REG('multi.pit.sourcing.general')}."]
    L += H3(M, "11.2", "How do employer stock option plans work and how are they taxed?")
    # round 2: RQ-534 closed by agent 2 (fed.equity.* facts, US-FEDQ1-001/-004/-006)
    L += [f"- **Federal, resident employee:** {T('fed.equity.withholding_treatment.resident')} {REG('fed.equity.withholding_treatment.resident')}.",
          f"- **Nonstatutory option spread:** reported with W-2 box 12 code {T('fed.equity.nso.w2_code')} {REG('fed.equity.nso.w2_code')}.",
          "- **ISO and ESPP:** FICA and FUTA "
          + F.B('fed.equity.iso_espp.fica_futa_applies', 'apply', 'do not apply')
          + " at grant, exercise or disposition, and income-tax withholding "
          + F.B('fed.equity.iso_espp.fit_withholding_required', 'is required', 'is not required')
          + f" on a disqualifying disposition {REG('fed.equity.iso_espp.fica_futa_applies')}.",
          f"- **RSU timing for FICA and FUTA:** {T('fed.equity.rsu.fica_timing')} {REG('fed.equity.rsu.fica_timing')}.",
          f"- **Federal, nonresident alien employee:** {T('fed.equity.withholding_treatment.nonresident')} {REG('fed.equity.withholding_treatment.nonresident')}.",
          f"- **State example:** California withholds bonuses and stock-option income at {T('ca.wh.supplemental.rate.bonus_stock_options')}% "
          f"{REG('ca.wh.supplemental.rate.bonus_stock_options')}."]
    L += H3(M, "11.2", "How is payroll handled for employees who transfer between different legal entities mid-year?")
    L += ["Each legal entity (EIN) is a separate employer. Wage bases restart at the new entity, and each entity files its own "
          "941 and W-2. A successor employer that acquires the business may count the predecessor's wages toward the FUTA base "
          f"{REG('fed.futa.wage_base')}. " + F.gap("common-paymaster relief and the OASDI successor rule for related entities are not keyed.",
                                                   "fed.common_paymaster.rule")]
    L += H3(M, "11.2", "What is the process for an employee who changes citizenship or residency status during the fiscal year?")
    L += ["- **State residency change:** from the move date, the new residence State's rules apply to wages paid. "
          "Withholding follows the new State routing (residence/work State, reciprocity certificates such as "
          f"{T('multi.reciprocity.pa.certificate')} in Pennsylvania {REG('multi.reciprocity.pa.certificate')}). The employee files new State "
          "certificates. The resident credit for tax paid to another State is generally taken at assessment "
          f"(e.g. Arizona: {T('multi.resident_credit.az.level')}) {REG('multi.resident_credit.az.level')}.",
          "- **Nonresident alien becoming a resident alien:** "
          + F.gap("the withholding change when an employee's federal status changes from nonresident alien to resident alien during the year is not keyed.",
                  "fed.nra.residency_change")]
    L += H3(M, "11.2", "Are there specific rules for expatriates or inpatriates?")
    L += ["**Inpatriates (nonresident aliens working in the US):**", ""]
    L += table(["Rule", "Value", "Source"], [
        ("Form W-4", T("fed.fit.nra.w4.rule"), REG("fed.fit.nra.w4.rule")),
        ("Add-on to wages for the FIT computation (2020+ W-4, annual)", T("fed.fit.nra.addon.table2.annual"), REG("fed.fit.nra.addon.table2.annual")),
        ("Add-on (pre-2020 W-4, annual)", T("fed.fit.nra.addon.table1.annual"), REG("fed.fit.nra.addon.table1.annual")),
        ("Treaty-exempt wages", T("fed.fit.nra.treaty_exempt.reporting"), REG("fed.fit.nra.treaty_exempt.reporting")),
        ("Commercial traveler exception", f"Present at most {T('fed.fit.nra.commercial_traveler.max_days')} days and paid at most "
         f"{T('fed.fit.nra.commercial_traveler.max_pay')}", REG("fed.fit.nra.commercial_traveler.max_days")),
    ])
    L += ["", f"**Expatriates (US citizens abroad):** Form 673 and the FEIE, as above {REG('fed.citizen_abroad.form673')}."]

    L += H3(M, "11.2", "Special treatments by worker category")
    L += table(["Category", "Treatment", "Source"], [
        ("Statutory employees", T("fed.statutory_employee.treatment"), REG("fed.statutory_employee.treatment")),
        ("Ministers", T("fed.minister.withholding"), REG("fed.minister.withholding")),
        ("Household employees", f"FICA from {T('fed.household.fica_cash_threshold')} cash wages in the year; FUTA from "
         f"{T('fed.household.futa_quarter_threshold')} in a quarter", REG("fed.household.fica_cash_threshold")),
        ("Agricultural workers", f"FICA where a worker is paid {T('fed.agricultural.per_worker_threshold')} or more, or total pay reaches "
         f"{T('fed.agricultural.total_threshold')}; FUTA from {T('fed.agricultural.futa_quarter_threshold')} in a quarter", REG("fed.agricultural.per_worker_threshold")),
        ("Family employees", T("fed.family_employment.treatment"), REG("fed.family_employment.treatment")),
        ("Students", T("fed.students.treatment"), REG("fed.students.treatment")),
        ("Government employees", T("fed.government_employee.treatment"), REG("fed.government_employee.treatment")),
        ("Election workers", f"FICA from {T('fed.election_worker.fica_threshold')} in the year", REG("fed.election_worker.fica_threshold")),
        ("Military spouses (State tax)", T("multi.military_spouse.rule", ef="2018-12-31"), REG("multi.military_spouse.rule", ef="2018-12-31")),
    ])
    L += H3(M, "11.2", "Fringe benefit exclusions (2026)")
    L += table(["Benefit", "Federal exclusion", "Source"], [
        ("Qualified parking", f"{T('fed.bik.parking.monthly_exclusion')} per month", REG("fed.bik.parking.monthly_exclusion")),
        ("Transit pass / commuter vehicle", f"{T('fed.bik.transit.monthly_exclusion')} per month", REG("fed.bik.transit.monthly_exclusion")),
        ("Dependent care assistance", f"{T('fed.bik.dependent_care.exclusion')} per year", REG("fed.bik.dependent_care.exclusion")),
        ("Educational assistance", f"{T('fed.bik.educational_assistance.exclusion')} per year", REG("fed.bik.educational_assistance.exclusion")),
        ("Group-term life insurance", f"Coverage up to {T('fed.bik.group_term_life.excluded_coverage')}; the cost of coverage above it is FICA wages",
         REG("fed.bik.group_term_life.excluded_coverage")),
        ("Trump-account employer contribution", f"Up to {T('fed.bik.trump_account.employer_contribution_max')}" + F.dated("fed.bik.trump_account.employer_contribution_max"),
         REG("fed.bik.trump_account.employer_contribution_max")),
        ("Moving expenses and bicycle commuting", B("fed.bik.moving_and_bicycle.excluded", "Excluded", "Not excluded (taxable wages)"),
         REG("fed.bik.moving_and_bicycle.excluded")),
        ("Business mileage reimbursement", F.gap(F.GAP_TEXT["fed.bik.business_mileage.rate"], "fed.bik.business_mileage.rate"), "—"),
    ])
    L += ["", f"ACA affordability percentage for 2026: {T('fed.aca.affordability.rate')}% {REG('fed.aca.affordability.rate')}."]
    L += ["", "The population coverage matrix (federal and multistate cut of every special population) follows as §11.3."]
    return L


# ======================================================================== m13
def m13():
    M = "m13_practices"
    L = ["# Module 13: Common Business Practices & Non-Statutory Rules", "",
         "*Purpose: To capture prevalent, non-statutory conventions.*"]
    L += H3(M, "13", "Describe the common practice for off-cycle or ad-hoc payments.")
    L += ["An off-cycle payment (bonus, correction, final pay on a non-payday) is a supplemental wage when paid apart from "
          f"the regular wages. Withhold at the optional flat {T('fed.fit.supplemental.flat_rate')}%, or aggregate with the last regular payment "
          f"{REG('fed.fit.supplemental.flat_rate')}. FICA and FUTA run against the cumulative annual bases (Module 9.2). The State supplemental "
          "rule of Module 9, Table 9.2.1 applies. "
          + F.gap("employer-practice conventions for off-cycle runs (frequency, approval, use of the flat vs aggregate method) were not researched.",
                  "practice.offcycle_payments")]
    L += H3(M, "13", "How are non-recoverable draws against future commissions typically handled?")
    L += ["Draws and commissions are wages when paid. The facts carry one related State rule: Iowa's final-pay rule "
          f"({T('ia.final_pay.rule')}) {REG('ia.final_pay.rule')}. "
          + F.gap("the treatment of recoverable and non-recoverable commission draws (wage status when advanced, recovery limits under "
                  "minimum-wage and wage-deduction law) is not keyed.", "practice.commission_draw")]
    L += H3(M, "13", "Are there common non-statutory leave types? How are they managed and reported?")
    L += ["Vacation and paid time off are not statutory entitlements. They are granted by employer policy. State law governs "
          "their payout at separation where a policy grants them (Module 8, Table 8.1.3). Leave pay is wages, reported in "
          "the ordinary W-2 boxes. Some States require sick-leave balances on the pay statement (Module 10, Table 10.3.1). "
          + F.gap("prevalent non-statutory leave types (bereavement, floating holidays, volunteer days) were not researched.",
                  "practice.non_statutory_leave")]
    L += ["", "## 13.1 Configuration Practices and Known Traps", "",
          "Each row is a build rule held as a fact. It records a point where a published source, a statute and the "
          "withholding method diverge, and which one the engine follows.", ""]
    F.set_loc("m13_practices.md §13.1 Configuration practices table")
    pk = [f["key"] for f in json.load(open(os.path.join(F.RESEARCH, "CCG-m13_practices-facts.json"), encoding="utf-8"))["facts"]]
    rows = []
    for k in pk:
        rows.append((k.split(".")[1].upper(), T(k) + F.dated(k), F.R(k)))
    L += table(["Jurisdiction", "Practice (value)", "Register"], rows)
    F.set_loc("m13_practices.md §13.1 Mid-year changes")
    L += ["", "**Mid-year changes are applied by payment date.** Configure every dated value with its effective date and select it by "
          "the payment date of the run, never by the period worked (Module 11, Table 11.1.1). Massachusetts PFML is the exception "
          f"and follows the earning date {REG('ma.pfml.total.rate')}. Examples in 2026: Ohio withholding tables from {T('oh.wh.tables.effective_from')}; "
          f"District of Columbia minimum wage {TV('dc.minwage.hourly')}; Idaho zero bracket {TV('id.wh.zero_bracket.single.biweekly')}."]
    F.set_loc("m13_practices.md §13.1 Tips and overtime at assessment")
    L += ["", "**Tips and overtime deductions at assessment only (do not reduce withholding).** Federal: "
          f"{T('fed.plaw119_21.tips_overtime.level')} {REG('fed.plaw119_21.tips_overtime.level')}. States keyed in the facts:", ""]
    L += table(["State", "Rule", "Register"], [
        ("MI", T("mi.pit.tips_overtime_deduction") + F.dated("mi.pit.tips_overtime_deduction"), REG("mi.pit.tips_overtime_deduction")),
        ("AL", f"Overtime premium deduction up to {T('al.pit.overtime_premium_deduction.max')} (tax years 2026-2028); assessment only",
         REG("al.pit.overtime_premium_deduction.max")),
        ("GA", f"Overtime subtraction up to {T('ga.pit.overtime_subtraction.max')} and tip subtraction up to {T('ga.pit.tip_subtraction.max')}; assessment only",
         REG("ga.pit.overtime_subtraction.max")),
        ("IA", T("ia.pit.obbba"), REG("ia.pit.obbba")),
        ("HI", "Tips deduction conformed at assessment; overtime deduction "
         + B("hi.pit.ot_deduction.conformed", "conformed", "not conformed"), REG("hi.pit.ot_deduction.conformed")),
        ("DC", T("dc.pit.obbba_deductions"), REG("dc.pit.obbba_deductions")),
    ])
    F.set_loc("m13_practices.md §13.1 Open practice points")
    L += ["", "**Open practice points (not facts):**", "",
          "- Massachusetts PFML split, transition date: " + F.gap(F.GAP_TEXT["ma.pfml.split.effective_date"], "ma.pfml.split.effective_date"),
          "- DOL compilation lists: " + F.gap(F.GAP_TEXT["practice.dol_paid_leave_list"]
                                              + " Never read Michigan's paid-leave or prevailing-wage status from a DOL compilation table.",
                                              "practice.dol_paid_leave_list"),
          "- Utah Pub. 14 effective date: " + F.gap(F.GAP_TEXT["ut.oracle.pub14.examples.withholding"], "ut.oracle.pub14.examples.withholding"),
          "- District of Columbia 2026 method: " + F.gap(F.GAP_TEXT["dc.oracle.method_2026"], "dc.oracle.method_2026"),
          "- North Dakota booklet: the Section 2 example is a booklet defect. Configure from the table "
          f"(Module 12, 12.2.1) {REG('nd.oracle.section2_booklet.withholding')}.",
          f"- Virginia 2027: statutory standard deduction {T('va.pit.std_deduction.single', ef='2027-01-01')} single / "
          f"{T('va.pit.std_deduction.married', ef='2027-01-01')} married (2026: {T('va.pit.std_deduction.single', ef='2025-01-01')} / "
          f"{T('va.pit.std_deduction.married', ef='2025-01-01')}) {REG('va.pit.std_deduction.single')}. It is not modelled in withholding until Virginia Tax publishes the 2027 formula (row above)."]
    return L


# ======================================================================== coverage
COV_ORDER = ["resident_employee", "non_resident_employee", "fixed_term_contract", "part_time",
             "officers_without_employment_contract", "apprentices_and_trainees", "maternity_paternity_parental",
             "work_accident_occupational_disease", "termination_and_final_pay", "mid_month_joiner_and_leaver",
             "annual_regularisation", "overtime", "multiple_employers", "local_regimes", "employer_type_and_size",
             "mid_year_rate_change", "special_pay_cycles", "accrual_vs_payment"]


def coverage():
    """§11.3 population coverage matrix. Treatment text is rewritten from the coverage facts with every number
    bound to a key; numbers without a key are left to the annex named in the row."""
    cv = json.load(open(os.path.join(F.RESEARCH, "CCG-coverage-facts.json"), encoding="utf-8"))["coverage_matrix"]
    L = ["## 11.3 Population Coverage Matrix", "",
         "One row per population (all populations are in scope, owner decision US-OWN-005). Each row gives the federal and "
         "multistate treatment, its effect on income tax, social security and reporting, the module that carries the rule, "
         "and the sources. State-specific treatments are in the annexes named in the row.", ""]
    W = {}
    F.set_loc("coverage.md §11.3 rows")
    W["resident_employee"] = (
        "Ordinary employee. FIT per Form W-4 and the Pub. 15-T method. FICA employee and employer. FUTA and SUI employer-paid, SUI to the "
        "State of UI coverage. State income tax of the work State and, for residents working elsewhere, of the residence State under its own rule "
        "(credit, difference withholding or reciprocity).",
        f"FIT Pub. 15-T 2026 Worksheet 1A (line 1g {T('fed.fit.worksheet1a.line1g.mfj')} MFJ); State withholding per annex",
        f"OASDI {T('fed.fica.oasdi.rate.employee')}% + {T('fed.fica.oasdi.rate.employer')}% up to {T('fed.fica.oasdi.wage_base', ef='2026-01-01')}; "
        f"Medicare {T('fed.fica.medicare.rate.employee')}% + {T('fed.fica.medicare.rate.employer')}%; Additional Medicare {T('fed.fica.addl_medicare.rate')}% "
        f"above {T('fed.fica.addl_medicare.withholding_threshold')}; FUTA {T('fed.futa.rate.net')}% on {T('fed.futa.wage_base')}; SUI per the State of coverage "
        f"({T('multi.sui.localization_test')})",
        f"Form 941 quarterly, 940 annual, W-2 by {T('fed.w2.due_date')}; State withholding and UI returns")
    W["non_resident_employee"] = (
        "Two meanings. (a) **Nonresident alien of the US:** regular withholding with the Pub. 15-T add-on "
        f"({T('fed.fit.nra.addon.table2.annual')} per year, Table 2); W-4 per Notice 1392; treaty-exempt wages via Form 8233 on Form 1042-S; "
        f"commercial-traveler exception (at most {T('fed.fit.nra.commercial_traveler.max_days')} days and {T('fed.fit.nra.commercial_traveler.max_pay')}). "
        "(b) **Nonresident of a State:** work-State withholding subject to reciprocity certificates, day or dollar thresholds "
        f"(e.g. Alabama {T('al.nonres.safe_harbor.days')} days, Louisiana {T('multi.nonresident.la.threshold_days')}, "
        f"West Virginia {T('multi.nonresident.wv.threshold_days')}, Arizona {T('multi.nonresident.az.threshold_days')}, Illinois "
        f"{T('multi.nonresident.il.threshold_days')} working days), convenience rules (New York: {T('multi.convenience.ny.rule')}), "
        "and the federal limits for transport workers and military spouses.",
        "Add-on for withholding only; 1042-S for treaty-exempt wages; State nonresident sourcing per Module 6",
        "The add-on has no FICA or FUTA effect: FICA is computed on actual wages, as for residents. For State nonresidents SUI "
        "follows the localization test, not residence",
        f"W-2 (or 1042-S for treaty-exempt wages: {T('fed.form1042s.channel')}); State nonresident withholding on the work-State return; "
        f"W-2 boxes 15-20 for up to {T('multi.w2.states_per_form')} States")
    W["fixed_term_contract"] = (
        "No federal or general State fixed-term regime: employment is at will, and a fixed term is a matter of contract. Payroll treats "
        "a fixed-term worker as any employee. Expiry of the term is a separation and triggers the work State's final-pay rule "
        f"({T('fed.final_pay.rule')}).",
        "None: same withholding as any employee",
        "None: FICA, FUTA and SUI unchanged; UI benefit eligibility on separation is State law",
        f"Separation: State final pay (Module 9, Table 9.1.1) and any State separation notice (e.g. Tennessee within {T('tn.term.separation_notice.hours')} hours); W-2 as usual")
    W["part_time"] = (
        f"No federal part-time regime: the FLSA minimum wage ({T('fed.minwage.hourly')}) and the 40-hour overtime rule apply per hour and per workweek "
        f"whatever the schedule. Part-time hours count toward the ACA full-time-equivalent test (applicable large employer at {T('fed.aca.ale.fte_threshold')}). "
        "State paid-sick-leave accrual is per hour worked (Module 8).",
        "None: same withholding method, by pay period",
        "None: FICA from the first dollar; SUI and PFML per State (some States have hours-based coverage)",
        "ACA: FTE count for ALE status (1094-C/1095-C); State UI reports with hours where required (e.g. Washington)")
    W["officers_without_employment_contract"] = (
        "Corporate officers are employees for payroll: wages take FIT withholding, FICA and FUTA. State law includes corporate officers "
        "as employees for withholding (Oklahoma) and UI coverage (Florida). Directors' fees and partner or sole-proprietor draws are not wages "
        f"(self-employment, outside payroll). Statutory employees: {T('fed.statutory_employee.treatment')}.",
        "Officer wages: FIT withholding as any employee",
        "FICA and FUTA on officer wages; SUI covers corporate officers (e.g. Florida); some States allow officer exclusions (annexes)",
        "W-2 as any employee; statutory employees W-2 box 13")
    W["apprentices_and_trainees"] = (
        "No federal apprentice payroll regime: the FLSA minimum wage applies (a sub-minimum only under DOL certificates). "
        f"Students: {T('fed.students.treatment')}. States set learner rates (California, Washington: annexes).",
        "FIT withheld as any employee",
        "Student exemptions from FICA and FUTA as listed; State UI student exclusions (annexes)",
        "W-2 as usual")
    W["maternity_paternity_parental"] = (
        f"No federal paid parental leave for private employers. FMLA gives up to {T('fed.fmla.weeks')} workweeks of job-protected leave "
        "(may be unpaid). Paid leave comes from the State PFML/TDI programmes. Premiums are withheld or paid through payroll (e.g. Washington "
        f"{T('wa.pfml.total.rate', ef='2026-01-01')}% in 2026, Massachusetts {T('ma.pfml.total.rate')}%, District of Columbia {T('dc.pfml.employer.rate')}% "
        "employer-only). Benefits are paid by the State or insurer (Module 8, Table 8.1.5).",
        "State PFML benefits are not employer payroll; employee PFML contributions are W-2 wages",
        "Employee and employer PFML contributions per State programme, capped as the State sets (Module 5)",
        "State PFML quarterly returns; W-2 box 14 per State practice")
    W["work_accident_occupational_disease"] = (
        "Workers' compensation is State law and generally an insured employer cost outside payroll. Payroll touches it where a State levies a "
        "per-employee fee or allows an employee deduction (New Mexico fee on TRD-41431; Washington employee share of workers' compensation premiums). "
        "No federal payroll rule. " + F.gap(F.GAP_TEXT["multi.workers_comp.employee_share"], "multi.workers_comp.employee_share"),
        "None at payroll: workers' compensation benefits are not employer wages",
        "New Mexico fee per covered employee per quarter (employer and employee parts); Washington employee deduction; no federal levy",
        "New Mexico TRD-41431 quarterly (fee + wage report); State annexes")
    W["termination_and_final_pay"] = (
        f"{T('fed.final_pay.rule')} (Module 9, Table 9.1.1; vacation payout Module 8, Table 8.1.3). Severance is wages for FIT, FICA and FUTA. "
        f"WARN: {T('fed.warn.notice_days')} days' notice for a plant closing or mass layoff; pay in lieu is wages. W-2 for a terminated employee: "
        f"{T('fed.w2.terminated_employee.furnishing')}.",
        f"Severance and pay in lieu are supplemental wages ({T('fed.fit.supplemental.flat_rate')}% optional flat rate or aggregate)",
        "Severance subject to FICA and FUTA",
        "W-2; State separation notices where required")
    W["mid_month_joiner_and_leaver"] = (
        "No federal proration rule: withholding is computed on the wages paid in the pay period with the period frequency of Pub. 15-T. "
        f"A joiner files a W-4 (and the State certificate) at hire and is reported to the State Directory of New Hires within {T('fed.newhire.deadline_days')} "
        "days (shorter in many States). A leaver receives final pay under State law. Wage bases run per employer per calendar year from the first payment.",
        "Pub. 15-T per-period method on wages actually paid; no catch-up or proration",
        f"Wage bases start at the first payment by this employer in the calendar year (FUTA {T('fed.futa.wage_base')}); successor-employer carry-over for FUTA",
        "New-hire report; W-2 for any part-year employee")
    W["annual_regularisation"] = (
        "No employer year-end income-tax regularisation: the employee settles at assessment. The employer reconciles the quarterly 941s to "
        "the annual W-2/W-3, corrects with 941-X and W-2c, stops OASDI at the wage base and starts Additional Medicare above the threshold per "
        "employer. Excess OASDI from multiple employers is refunded at assessment, not by the employer.",
        f"None at payroll; W-4 exempt status renewed yearly ({T('fed.w4.exempt.validity')})",
        f"Per-employer annual bases (OASDI {T('fed.fica.oasdi.wage_base', ef='2026-01-01')}; FUTA {T('fed.futa.wage_base')}; SUI per State); "
        f"Additional Medicare above {T('fed.fica.addl_medicare.withholding_threshold')}",
        f"W-2/W-3 by {T('fed.w2.due_date')} reconciled to four 941s; 940 annual; State annual reconciliations")
    W["overtime"] = (
        f"FLSA: {T('fed.overtime.premium.multiplier')} × the regular rate above {T('fed.overtime.weekly_threshold_hours')} hours in a workweek; "
        f"no federal daily overtime. States add daily overtime (California: {T('ca.overtime.rule')}; Nevada for employees paid under "
        f"{T('nv.overtime.daily_threshold_wage')} per hour; others in the annexes). The P.L. 119-21 qualified-overtime deduction operates at "
        f"assessment ({T('fed.plaw119_21.qualified_overtime.level')}).",
        "Overtime is regular wages for withholding; the deduction reaches withholding only via W-4 Step 4(b)",
        "Fully subject to FICA, FUTA and SUI",
        f"W-2 box 12 code TT ({T('fed.w2.box12.new_codes')})")
    W["multiple_employers"] = (
        "Each employer withholds and applies the wage bases independently. The OASDI and FUTA bases are per employer (successor carry-over "
        "only on acquisition). Additional Medicare is triggered per employer. The employee coordinates FIT across jobs on W-4 Step 2: the "
        f"line 1g amount ({T('fed.fit.worksheet1a.line1g.mfj')} MFJ) is not subtracted when Step 2 is checked. "
        + F.gap(F.GAP_TEXT["fed.common_paymaster.rule"], "fed.common_paymaster.rule"),
        "W-4 Step 2 checkbox changes the schedule and line 1g",
        f"Per-employer OASDI, FUTA ({T('fed.futa.wage_base')}) and SUI bases; excess OASDI refunded at assessment",
        "Separate W-2 per employer")
    W["local_regimes"] = (
        "Local income and payroll taxes exist in a minority of States and sit outside State reciprocity: Pennsylvania EIT and LST; "
        f"Philadelphia wage tax ({TV('pa.local.philadelphia.resident.rate')} resident); Ohio municipal and school-district taxes "
        f"({T('oh.local.municipal_base')}); Michigan city taxes (Detroit resident {T('mi.local.detroit.rate.resident')}%); Indiana county tax "
        f"({T('in.county.change_dates')}); Maryland county tax; Kentucky occupational taxes; NYC and Yonkers; Oregon transit and local levies. "
        "Per-locality detail is in the annexes.",
        "Local withholding by residence and/or work locality per local rule; W-2 boxes 18-20",
        "Local transit and payroll levies (Oregon, New York MCTMT) per the levy scope",
        f"Local returns per locality; W-2 boxes 18-20 for up to {T('multi.w2.states_per_form')} localities")
    W["employer_type_and_size"] = (
        f"Size and type thresholds change obligations: ACA applicable large employer at {T('fed.aca.ale.fte_threshold')} full-time incl. equivalents "
        f"(1094-C/1095-C, e-file at {T('fed.aca.efile_threshold')}+); deposit schedule by lookback liability ({T('fed.deposit.monthly_max_lookback_liability')} "
        f"monthly/semiweekly; {T('fed.deposit.next_day_threshold')} next day); household employers (FICA at {T('fed.household.fica_cash_threshold')}, "
        f"FUTA at {T('fed.household.futa_quarter_threshold')} per quarter); agricultural ({T('fed.agricultural.per_worker_threshold')} / "
        f"{T('fed.agricultural.total_threshold')} tests); government employers ({T('fed.government_employee.treatment')}); State size tests "
        "(Massachusetts PFML employer share, Nebraska sick leave, Virginia paid sick leave: annexes and Module 8).",
        "Household FIT only by agreement; agricultural FIT and FICA from the thresholds",
        "Household and agricultural thresholds; Massachusetts PFML employer share depends on size",
        "ALE 1094-C/1095-C; Form 943/944/Schedule H routes")
    W["mid_year_rate_change"] = (
        "Several 2026 values change during the year and are applied by payment date (Module 11, Table 11.1.1): District of Columbia minimum wage "
        f"({TV('dc.minwage.hourly')}); Oregon ({TV('or.labour.minwage.standard.hourly')}); Ohio withholding tables from {T('oh.wh.tables.effective_from')}; "
        f"Georgia withholding rate ({T('ga.wh.rate', ef='2026-01-01')}% to 2026-05-10, {T('ga.wh.rate', ef='2026-05-11')}% from 2026-05-11; assessment rate {T('ga.pit.rate.flat', ef='2026-01-01')}% for tax year 2026, {T('ga.live.hb463.status')}); Indiana county rates; Idaho tables; Philadelphia wage tax; "
        f"Trump-account exclusion{F.dated('fed.bik.trump_account.employer_contribution_max')}.",
        "Withholding tables effective by payment date",
        "Rate changes on the effective date (no federal mid-year change in 2026)",
        "Quarterly returns split by period; W-2 annual totals")
    W["special_pay_cycles"] = (
        f"Pub. 15-T supports these periods: {T('fed.fit.pay_periods_per_year')}. Supplemental pay (bonus, commissions, severance): "
        f"{T('fed.fit.supplemental.flat_rate')}% optional flat rate or aggregate; {T('fed.fit.supplemental.mandatory_rate')}% mandatory above "
        f"{T('fed.fit.supplemental.mandatory_threshold')} per year. State pay-frequency rules and State supplemental rates (California "
        f"{T('ca.wh.supplemental.rate.bonus_stock_options')}% bonus / {T('ca.wh.supplemental.rate.other')}% other) are annex detail (Module 9, Table 9.2.1).",
        "Supplemental methods; State supplemental rates",
        "None: FICA on all wages including supplemental",
        "None specific")
    W["accrual_vs_payment"] = (
        f"Federal payroll taxes follow the payment date ({T('fed.tax_year.basis')}): FIT, FICA and FUTA apply to wages paid in the calendar year "
        f"(OASDI base for remuneration paid in 2026; FUTA {T('fed.futa.wage_base')} per employer). Exception: Massachusetts PFML rates apply to wages "
        "earned on or after 1 January. A December-earned, January-paid wage takes the new year's rates and bases federally.",
        "Withholding at payment; table year = payment date",
        "Wage bases by payment date; Massachusetts PFML by earning date",
        "W-2 and 941 by payment date")
    for key in COV_ORDER:
        row = cv[key]
        F.set_loc(f"coverage.md §11.3 {key}")
        treat, it, ss, rep = W[key]
        srcs = "; ".join(f"{s['register_id']} ({s['article']})" for s in row["sources"])
        title = {"non_resident_employee": "Non-resident employee", "maternity_paternity_parental": "Maternity, paternity and parental leave",
                 "work_accident_occupational_disease": "Work accident and occupational disease", "termination_and_final_pay": "Termination and final pay",
                 "mid_month_joiner_and_leaver": "Mid-month joiner and leaver", "apprentices_and_trainees": "Apprentices and trainees",
                 "employer_type_and_size": "Employer type and size", "accrual_vs_payment": "Accrual versus payment"}.get(key, key.replace("_", " ").capitalize())
        where = re.sub(r"(?<![A-Za-z])m(\d\d)_[a-z_]+", lambda mm: f"Module {int(mm.group(1))}", row["ccg_location"])
        L += [f"### {title}", "",
              f"*Status: {row['status']}. Rule carried in: {where}.*", "",
              treat, ""]
        L += table(["Effect on", "Treatment"], [("Income tax", it), ("Social security", ss), ("Reporting", rep)])
        L += ["", f"Sources: {srcs}.", ""]
        for k in row.get("fact_keys", []):
            F.bind(k, value=F.entries(k)[0]["value"])
    return L


def write(name, lines):
    text = F.clean("\n".join(lines).rstrip("\n") + "\n")
    open(os.path.join(MOD, name), "w", encoding="utf-8").write(F.CC.finalize(name, text))


def main():
    write("m08_leave.md", m08())
    write("m09_termination.md", m09())
    write("m10_reporting.md", m10())
    write("m11_advanced.md", m11())
    write("m13_practices.md", m13())
    write("coverage.md", coverage())
    os.makedirs(os.path.join(HERE, "out"), exist_ok=True)
    json.dump([list(b) for b in F.BINDINGS], open(os.path.join(HERE, "out", "bindings_modules.json"), "w", encoding="utf-8"), indent=0)
    json.dump([list(g) for g in F.GAPS], open(os.path.join(HERE, "out", "gaps_modules.json"), "w", encoding="utf-8"), indent=0)
    print("bindings", len(F.BINDINGS), "gaps", len(F.GAPS))


if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""The 300 codes of Global_WTC_V1_0.xlsx configured for the United States.

Every global code is kept character for character. Each family has one ANCHOR row (the first code, or the code named in the
table) that carries the parameters of the treatment with tagged figures; the other codes of the family point to the anchor and
carry no figure, so no tagged value is repeated as boilerplate. The treatment of a family comes from the facts; where the facts
are silent the cell says 'Not configured in this release [[GAP:WTC-RQ-nn]]' and the flags stay empty (NA) or conditional.
"""
import re

from openpyxl import load_workbook

import wtc_common as W
import wtc_profiles as P
from wtc_model import Row, YES, NO, YN, NA, X
import wtc_fed as F
from wtc_why import WHY

val, line, rid = W.val, W.line, W.rid


def load_global():
    ws = load_workbook(W.GLOBAL_WTC, read_only=True).active
    out = []
    for r in ws.iter_rows(min_row=2, values_only=True):
        if r[0] is None:
            continue
        out.append((int(r[0]), str(r[1]).strip(), str(r[2]).strip()))
    return out


# family table: (first code, last code, family id). Codes not listed in a range are not in the family.
RANGES = [
    (62100, 62103, "basic"), (62104, 62104, "rate"), (62108, 62109, "basic"),
    (62110, 62139, "ot"), (62140, 62149, "saladd"), (62150, 62155, "prem"), (62160, 62162, "holiday"), (62170, 62172, "oncall"),
    (62180, 62182, "sev"), (62190, 62190, "ltd"), (62200, 62209, "bonus"), (62210, 62219, "profit"), (62220, 62229, "disc"),
    (62300, 62302, "leave"), (62305, 62305, "leave"), (62310, 62362, "expat"), (62400, 62482, "housing"),
    (62500, 62505, "car"), (62510, 62512, "car"), (62530, 62532, "car"), (62520, 62523, "transp"),
    (62540, 62542, "reloc"), (62560, 62563, "reloc"), (62550, 62552, "travel"), (62570, 62570, "perdiem"),
    (62590, 62591, "birth"), (62599, 62599, "covid"), (62610, 62619, "medical"), (62630, 62632, "personal"),
    (62660, 62662, "personal"), (62640, 62648, "pensionpay"), (62650, 62650, "social"), (62670, 62680, "benefit"),
    (62700, 62700, "edu"), (62710, 62751, "school"), (62760, 62762, "family"), (62770, 62770, "recog"),
    (62870, 62879, "special"), (62880, 62883, "postterm"), (62890, 62890, "stock"), (62990, 62994, "stock"),
    (62900, 62900, "grat"), (62910, 62930, "grat"), (62901, 62901, "supp13"), (62960, 62969, "saladd"), (62980, 62980, "saladd"),
    (21100, 21109, "d_basic"), (21110, 21127, "d_ot"), (21210, 21213, "d_ot"), (21140, 21149, "d_saladd"), (21150, 21152, "d_prem"),
    (21190, 21190, "d_ltd"), (21400, 21400, "d_housing"), (21520, 21520, "d_transp"), (21610, 21611, "d_health"),
    (21640, 21645, "d_pension"), (21670, 21670, "d_benefit"), (21800, 21800, "d_expense"), (21810, 21810, "d_parking"),
    (21820, 21820, "d_donation"), (21890, 21890, "d_stock"), (21900, 21900, "d_oasdi"),
    (23640, 23640, "c_plan"), (23670, 23670, "c_benefit"), (23671, 23673, "c_accrual"),
]

ROLE = re.compile(r"^(Arrears|Adjustment|Advance) - (.+)$")

# family -> (anchor code, tax code, base profile name)
ANCHOR = {"basic": 62100, "ot": 62110, "saladd": 62140, "prem": 62150, "holiday": 62160, "oncall": 62170, "sev": 62180,
          "ltd": 62190, "bonus": 62200, "profit": 62210, "disc": 62220, "leave": 62300, "expat": 62310, "housing": 62400,
          "car": 62500, "transp": 62520, "reloc": 62540, "travel": 62550, "perdiem": 62570, "birth": 62590, "covid": 62599,
          "medical": 62610, "personal": 62660, "pensionpay": 62640, "social": 62650, "benefit": 62670, "edu": 62700,
          "school": 62710, "family": 62760, "recog": 62770, "special": 62870, "postterm": 62880, "stock": 62890, "grat": 62900,
          "supp13": 62901, "rate": 62104}


def fam_of(code):
    for lo, hi, f in RANGES:
        if lo <= code <= hi:
            return f
    raise KeyError(code)


def _same(flags_fn, **over):
    f = flags_fn()
    f.update(over)
    return f


def _prof(fam):
    """(flags, extra basis override) of a family: the federal treatment profile."""
    reg = P.flags_reg
    if fam in ("basic", "ot", "saladd", "prem", "holiday", "oncall", "leave", "recog", "d_basic", "d_ot", "d_saladd", "d_prem"):
        return reg(), {}
    if fam in ("bonus", "profit", "disc", "supp13"):
        return P.flags_supp(), {}
    if fam in ("sev", "postterm", "grat"):
        return P.flags_sev(), {"income_tax": rid("fed.severance.treatment"), "oasdi": rid("fed.severance.treatment"),
                               "medicare": rid("fed.severance.treatment"), "futa": rid("fed.severance.treatment"),
                               "table_tax": rid("fed.severance.treatment")}
    if fam in ("expat", "housing", "car", "travel", "birth", "covid", "personal", "social", "family", "school", "special",
               "d_housing"):
        return _same(P.flags_reg, sui=YN, state_programmes=YN), {}
    if fam == "reloc":
        r = rid("fed.bik.moving_expense.excluded")
        return _same(P.flags_reg, sui=YN, state_programmes=YN), {"income_tax": r, "oasdi": r, "medicare": r, "futa": r, "table_tax": r}
    if fam in ("transp", "d_transp", "d_parking"):
        r = rid("fed.base.transportation.fit")
        return _same(P.flags_reg, income_tax=YN, oasdi=YN, medicare=YN, futa=YN, sui=YN, state_programmes=YN), \
            {"income_tax": r, "oasdi": r, "medicare": r, "futa": r}
    if fam == "edu":
        r = rid("fed.base.educational_assistance.fit")
        return _same(P.flags_reg, income_tax=YN, oasdi=YN, medicare=YN, futa=YN, sui=YN, state_programmes=YN), \
            {"income_tax": r, "oasdi": r, "medicare": r, "futa": r}
    if fam in ("medical", "d_health"):
        r = rid("fed.base.section125.rule")
        return _same(P.flags_reg, income_tax=YN, oasdi=YN, medicare=YN, futa=YN, sui=YN, state_programmes=YN, state_income_tax=YN), \
            {"income_tax": r, "oasdi": r, "medicare": r, "futa": r}
    if fam == "perdiem":
        return _same(P.flags_reg, income_tax=YN, oasdi=YN, medicare=YN, futa=YN, sui=YN, state_programmes=YN), {}
    return {k: NA for k in P.FLAG_NAMES_LIST}, {}


P.FLAG_NAMES_LIST = [k for k in P.flags_reg()]


def _stock_flags(code):
    # 62890 NSO / 62990 RSU / 62991 restricted stock / 62993 ISO-ESPP / 62994 83(i)
    base = P.flags_supp()
    base.update(sui=YN, state_programmes=YN)
    if code == 62993:
        base.update(income_tax=YN, table_tax=NO, special_tax=NO, oasdi=NO, medicare=NO, futa=NO)
    return base


def _stock_basis(code):
    if code == 62993:
        r = rid("fed.equity.iso_espp.fica_futa_applies")
        return {"income_tax": rid("fed.equity.iso_espp.fit_withholding_required"), "oasdi": r, "medicare": r, "futa": r,
                "table_tax": r, "special_tax": r}
    r = rid("fed.equity.withholding_treatment.resident")
    return {"income_tax": r, "table_tax": r, "special_tax": r, "oasdi": r, "medicare": r, "futa": r}


# ----------------------------------------------------------------------------- text ---
def anchor_text(fam, name):
    """Parameter paragraph of a family ANCHOR (tagged figures, register ids, inputs)."""
    W.gap  # noqa: B018
    if fam in ("basic",):
        return ("Salary or hourly wages for the period: cash remuneration for services, wages for every federal tax. " + P.txt_all_taxes() + " "
                + P.txt_state_layer() +
                f" Inputs: {F.D_RATE_BASIS}, {F.D_PAYFREQ}, {F.D_FTPT}. Declared: W-2 boxes 1, 3 and 5 (Report Specification US-SSA-001) and "
                f"the quarterly return line wages, tips and other compensation (US-IRS-001).")
    if fam == "rate":
        return (f"Rate of pay of the employee (hourly rate or period rate) used to value the earning rows; a quantity of the payroll, not an "
                f"amount of wages and not itself a tax base. Input: {F.D_RATE_BASIS}.")
    if fam == "ot":
        return ("Overtime pay: the whole amount, including the premium, is wages for every federal tax. The federal deduction for qualified "
                f"overtime operates at assessment only and does not reduce withholding: {val('fed.obbba.overtime_deduction.level')} "
                f"[{rid('fed.obbba.overtime_deduction.level')}]. The premium portion of qualified overtime is reported in W-2 box 12 code "
                f"{val('fed.w2.box12.code.tt')} [{rid('fed.w2.box12.code.tt')}]; deduction cap for qualified overtime "
                f"{val('fed.plaw119_21.qualified_overtime.deduction_cap')} ({val('fed.plaw119_21.qualified_overtime.deduction_cap_mfj')} "
                f"married filing jointly) [{rid('fed.plaw119_21.qualified_overtime.deduction_cap')}]. State treatment: no State reduces "
                "withholding for it; the State rows list the assessment-level subtractions. " + P.txt_all_taxes() +
                " Each overtime code is one configurable rate tier (multiplier or rule) of the same earning; the tier is a payroll "
                "setting, not a tax difference.")
    if fam == "saladd":
        return ("Pay added to the base salary of the period (allowance paid with salary, differential, supplementary pay): cash remuneration "
                "for services, wages for every federal tax. " + P.txt_all_taxes())
    if fam == "prem":
        return ("Premium pay (shift, night, weekend or hazard premium): cash remuneration for services, wages for every federal tax. The "
                "premium of qualified overtime is reported through the overtime rows. " + P.txt_all_taxes())
    if fam == "holiday":
        return ("Holiday or vacation allowance paid in cash with the wages: wages for every federal tax. " + P.txt_all_taxes())
    if fam == "oncall":
        return ("Standby or on-call pay: cash remuneration for services, wages for every federal tax. " + P.txt_all_taxes())
    if fam == "sev":
        return (f"Severance and seniority pay on termination: {val('fed.severance.treatment')} [{rid('fed.severance.treatment')}]. "
                f"Withholding: a separately identified payment may use the supplemental flat rate of {X('fit_supp22')} or the aggregate method of "
                f"{X('fit_reg')}; the mandatory rate of {X('fit_supp37')} applies above the annual supplemental threshold. W-2 box 1. "
                + W.gap("WTC-RQ-07", "State unemployment insurance and State programme treatment of severance") +
                f". Inputs: {F.D_HIRE}, {F.D_SEP}, {F.D_FINALPAY}.")
    if fam == "ltd":
        return ("Long-term disability benefit paid through the payroll. " + W.gap("WTC-RQ-05", "treatment of long-term disability and third-party sick pay") +
                f". Inputs: {F.D_W2_3PSP}. See the third-party sick pay flag {X('flag_3psp')}.")
    if fam in ("bonus", "profit", "disc"):
        return ("Bonus-type supplemental wages (annual, referral, profit sharing, discretionary or one-time): wages for every federal tax. Federal "
                f"income tax withholding: optional flat rate {val('fed.fit.supplemental.flat_rate')} [{rid('fed.fit.supplemental.flat_rate')}] "
                f"({X('fit_supp22')}) or the aggregate method ({X('fit_reg')}); mandatory rate {val('fed.fit.supplemental.mandatory_rate')} above "
                f"{val('fed.fit.supplemental.mandatory_threshold')} of supplemental wages in the year [{rid('fed.fit.supplemental.mandatory_rate')}] "
                f"({X('fit_supp37')}). " + P.txt_fica() + " " + P.txt_futa() + " " + P.txt_state_layer() +
                " The State flat rates and aggregate-only States for supplemental wages are on the State income tax rows."
                + (" Each code of the family is one type of the same payment." if fam != "profit" else
                   " Profit sharing paid to the employee is a bonus-type payment."))
    if fam == "leave":
        return ("Annual leave (vacation) pay and the payout of accrued leave: wages for every federal tax when paid. "
                + P.txt_all_taxes() + f" Payout at separation depends on the written policy and State law: inputs {F.D_VACFORF}, {F.D_FINALPAY}, "
                f"{F.D_SEP}. Declared as wages in the pay period of payment.")
    if fam == "expat":
        return ("Expatriate or assignment allowance paid in cash: configured as cash remuneration, with the wage treatment of the regular wage "
                "rows. " + W.gap("WTC-RQ-01", "allowance-specific exclusions are not configured") + ". Nonresident alien employees: fringe and "
                f"allowance sourcing rules are on {X('flag_nra')}. {W.gap('WTC-RQ-07', 'State unemployment insurance and programme definition')}. "
                + P.txt_all_taxes())
    if fam == "housing":
        return ("Housing, rent or lodging allowance paid in cash: configured as cash remuneration. " +
                W.gap("WTC-RQ-01", "exclusion of lodging furnished for the convenience of the employer is not configured") +
                f". {W.gap('WTC-RQ-07', 'State unemployment insurance and programme definition')}. " + P.txt_all_taxes())
    if fam == "car":
        # v1.1 (V11 gap merge): WTC-RQ-89 closed by fed.bik.business_mileage.rate (two 2026 periods)
        return ("Car, car maintenance, fuel or car and transportation allowance paid in cash: configured as cash remuneration. "
                + line("fed.bik.business_mileage.rate", "Business standard mileage rate (USD per mile)") + ". "
                + W.gap("WTC-RQ-01", "accountable plan treatment of vehicle reimbursement") + ". " + P.txt_all_taxes())
    if fam == "transp":
        return (f"Transportation allowance. Qualified transportation fringes (transit passes and commuter vehicle) are excluded up to "
                f"{val('fed.bik.transit.monthly_exclusion')} a month and qualified parking up to {val('fed.bik.parking.monthly_exclusion')} a month "
                f"[{rid('fed.bik.transit.monthly_exclusion')}]; FIT, FICA and FUTA: {val('fed.base.transportation.fit')} "
                f"[{rid('fed.base.transportation.fit')}]. The excess over the limit and any cash allowance that is not a qualified fringe is wages. "
                + W.gap("WTC-RQ-07", "State unemployment insurance and programme definition"))
    if fam == "reloc":
        return (f"Relocation or moving allowance: moving expense exclusion applies: {val('fed.bik.moving_expense.excluded')} "
                f"[{rid('fed.bik.moving_expense.excluded')}], so the allowance is wages for every federal tax. Declared in W-2 box 1. "
                + P.txt_all_taxes() + f" {W.gap('WTC-RQ-07', 'State unemployment insurance and programme definition')}.")
    if fam == "travel":
        return ("Travel ticket allowance paid in cash: configured as cash remuneration. " + W.gap("WTC-RQ-01", "accountable plan treatment of travel reimbursement")
                + ". " + P.txt_all_taxes())
    if fam == "perdiem":
        return ("Per diem allowance. " + W.gap("WTC-RQ-01", "the per diem substantiation and accountable plan rules are not configured") +
                ". The flags are conditional on the plan until that rule is configured.")
    if fam in ("birth", "covid", "personal", "social", "family", "school", "special", "recog"):
        return ({"birth": "Birth or marriage allowance paid in cash", "covid": "Special allowance paid in cash during the public health emergency",
                 "personal": "Personal allowance paid in cash", "social": "Social allowance paid in cash",
                 "family": "Family or child allowance paid in cash", "school": "Education or schooling allowance paid to the employee in cash",
                 "special": "Special allowance paid in cash", "recog": "Recognition award paid in cash"}[fam] +
                ": configured as cash remuneration, with the wage treatment of the regular wage rows. " + P.txt_all_taxes() +
                f" {W.gap('WTC-RQ-07', 'State unemployment insurance and programme definition')}.")
    if fam == "medical":
        return (f"Medical insurance or medical care amount paid through the payroll. A benefit chosen under a section 125 plan: "
                f"{val('fed.base.section125.rule')} [{rid('fed.base.section125.rule')}]. Health coverage under a section 125 plan: FIT, FICA and "
                f"FUTA {val('fed.base.section125_health.fit')} [{rid('fed.base.section125_health.fit')}]. Cash paid in place of coverage is wages "
                f"for every federal tax; the flags are conditional on whether the amount is a plan benefit or cash. Health salary reduction cap: "
                f"{val('fed.bik.health_fsa.salary_reduction_cap')}, carry-over {val('fed.bik.health_fsa.carryover_max')} "
                f"[{rid('fed.bik.health_fsa.salary_reduction_cap')}]. {W.gap('WTC-RQ-07', 'State unemployment insurance and programme definition')}.")
    if fam == "pensionpay":
        return ("Pension and pension refund amounts. " + W.gap("WTC-RQ-06", "treatment of pension and pension-refund payments"))
    if fam == "benefit":
        return ("Benefits plan amount paid to the employee through the payroll. " + W.gap("WTC-RQ-02", "treatment of the generic benefit plan amount"))
    if fam == "edu":
        return (f"Education allowance. Educational assistance is excluded from FIT, FICA and FUTA up to {val('fed.bik.educational_assistance.exclusion')} "
                f"a year under a qualifying plan: {val('fed.base.educational_assistance.fit')} [{rid('fed.base.educational_assistance.fit')}]; the "
                f"excess and any amount outside a qualifying plan is wages. {W.gap('WTC-RQ-07', 'State unemployment insurance and programme definition')}.")
    if fam == "stock":
        return (f"Equity compensation (code 62890 nonstatutory option spread and restricted stock; 62990 restricted stock unit; 62991 restricted "
                f"stock vested; 62993 incentive stock option and employee stock purchase plan income; 62994 section 83(i) inclusion). Resident "
                f"employee, 2026: {W.gap('WTC-RQ-14')}. "
                f"Nonresident alien: {val('fed.equity.withholding_treatment.nonresident')} [{rid('fed.equity.withholding_treatment.nonresident')}]. "
                f"Restricted stock unit FICA timing: {val('fed.equity.rsu.fica_timing')} [{rid('fed.equity.rsu.fica_timing')}]. Incentive stock "
                f"option and employee stock purchase plan: FICA and FUTA apply: {val('fed.equity.iso_espp.fica_futa_applies')}; FIT withholding "
                f"required: {val('fed.equity.iso_espp.fit_withholding_required')} [{rid('fed.equity.iso_espp.fica_futa_applies')}]. Nonstatutory "
                f"option income is W-2 box 12 code {val('fed.equity.nso.w2_code')} [{rid('fed.equity.nso.w2_code')}].")
    if fam in ("grat",):
        return (f"Gratuity, end-of-service or post-termination payment on termination: {val('fed.severance.treatment')} "
                f"[{rid('fed.severance.treatment')}]. The United States has no statutory end-of-service gratuity; the code is configured for payments "
                f"made under a contract or policy, with the severance treatment ({X('fit_supp22')} flat rate optional).")
    if fam == "postterm":
        return (f"Payment made after termination (for example pay for the period after the last day): {val('fed.severance.treatment')} "
                f"[{rid('fed.severance.treatment')}]. Inputs: {F.D_SEP}, {F.D_FINALPAY}.")
    if fam == "supp13":
        return ("Supplemental base salary payment (such as a thirteenth or fourteenth month salary): a bonus-type payment, wages for every "
                "federal tax; the supplemental wage rules of the bonus family (anchor 62200) apply: optional flat rate or aggregate method, as on that anchor. " + P.txt_all_taxes())
    raise KeyError(fam)


def deduction_text(fam, code, name):
    """Anchor/solo text of a deduction or contribution family."""
    if fam == "d_oasdi":
        return (f"Social security tax (OASDI) withheld from the employee: {val('fed.fica.oasdi.rate.employee')} of social security wages up to "
                f"the annual wage base {val('fed.fica.oasdi.wage_base')} per employee per employer [{rid('fed.fica.oasdi.wage_base')}]. "
                f"Computation: the lesser of (remaining annual maximum) and (rate x period social security wages), never annualised and divided. "
                f"The employer share is {X('oasdi_er')}. Accumulator: year-to-date social security wages (Subject to Social Insurance Q1 plus the "
                f"year-to-date mechanism). Exempt: {val('fed.fica.nra.fjmq_exempt.scope')} [{rid('fed.fica.nra.fjmq_exempt.scope')}]. Declared: W-2 "
                f"box 4; Form 941 line 5a. Inputs: {F.D_VISA}, {F.D_PURPOSE}, {F.D_TOTAL_CTRY}, {F.D_TOTAL_EX}, {F.D_NO_SSMED}.")
    if fam == "d_health":
        return (f"Employee contribution to health or life insurance (flag class 2, salary reduction through a section 125 plan: No means removed from the base before the tax). Through a section 125 plan: FIT, FICA and FUTA {val('fed.base.section125_health.fit')} "
                f"[{rid('fed.base.section125_health.fit')}]; {val('fed.base.section125.rule')} [{rid('fed.base.section125.rule')}]. Outside a section "
                f"125 plan the contribution is paid from taxed wages and does not reduce any base. HSA through a section 125 plan: "
                f"{val('fed.base.hsa_contribution.fit')} [{rid('fed.base.hsa_contribution.fit')}]; limits {val('fed.hsa.limit.self_only')} and "
                f"{val('fed.hsa.limit.family')} [{rid('fed.hsa.limit.self_only')}]. The monthly employee share of the lowest-cost self-only "
                f"coverage feeds {X('flag_aca')}. {W.gap('WTC-RQ-07', 'State unemployment insurance and programme definition')}.")
    if fam == "d_pension":
        return None
    if fam == "d_parking":
        return (f"Employee parking deduction (qualified parking fringe): excluded up to {val('fed.bik.parking.monthly_exclusion')} a month: "
                f"{val('fed.base.transportation.fit')} [{rid('fed.base.transportation.fit')}]; the excess is wages.")
    if fam == "d_donation":
        return ("Voluntary charitable deduction taken from net pay after all taxes (after-tax deduction): it does not change any tax base. State "
                f"wage-deduction authorisation rules are in the State annexes of {W.CCG_REF} Module 7.")
    if fam == "d_expense":
        return ("Recovery of an expense reimbursement from the employee. " + W.gap("WTC-RQ-02", "treatment of the recovery of a reimbursement"))
    if fam == "d_stock":
        return ("Deduction of the amount paid by the employee for shares or options (purchase or exercise price), taken from net pay after all "
                f"taxes; it does not change the base of the equity income rows ({62890}).")
    if fam == "d_ltd":
        return ("Employee contribution to long-term disability coverage. " + W.gap("WTC-RQ-05", "treatment of long-term disability premiums"))
    if fam == "d_benefit":
        return ("Employee deduction for a benefits plan. " + W.gap("WTC-RQ-02", "treatment of the generic benefit plan deduction"))
    if fam == "c_plan":
        return ("Employer contribution to a retirement plan (not recorded against net pay). " +
                W.gap("WTC-RQ-04", "treatment of employer plan contributions") + f". Elective deferral limit: {val('fed.retirement.401k.elective_deferral_limit')} "
                f"[{rid('fed.retirement.401k.elective_deferral_limit')}].")
    if fam == "c_benefit":
        return ("Employer contribution to a benefits plan. " + W.gap("WTC-RQ-02", "treatment of the generic benefit plan contribution"))
    if fam == "c_accrual":
        return ("Company contribution liability: accrual of an amount that the employer owes to a plan or carrier for the period; it is "
                "not wages of the employee and changes no base. The employer cost of health coverage that the annual wage statement reports "
                f"(box 12 code DD) is kept on {X('w2_dd')}.")
    raise KeyError(fam)


PENSION_MAP = {  # code -> (label, fact key stem)
    21640: ("401(k) elective deferral", "fed.base.401k_deferral"),
    21641: ("403(b) salary reduction", "fed.base.403b_salary_reduction"),
    21642: ("457(b) salary reduction", "fed.base.457b_salary_reduction"),
    21645: ("SIMPLE plan salary reduction", "fed.base.simple_salary_reduction"),
}


def pension_row(code, name):
    label, stem = PENSION_MAP.get(code, (None, None))
    if code in (21640, 21641, 21642, 21645):
        r = rid(f"{stem}.fit")
        fl = dict(income_tax=NO, table_tax=NO, special_tax=NO, oasdi=YES, medicare=YES, futa=YES, sui=YN, state_programmes=YN,
                  pension=NA, state_income_tax=YN, local_income_tax=YN)
        basis = dict(income_tax=r, table_tax=r, special_tax=r, oasdi=rid(f"{stem}.fica"), medicare=rid(f"{stem}.fica"),
                     futa=rid(f"{stem}.futa"), sui=rid("multi.sui.localization_test"), state_programmes=rid("multi.sui.localization_test"),
                     state_income_tax=rid("multi.no_wage_income_tax.states"), local_income_tax=rid("multi.no_wage_income_tax.states"))
        extra = ""
        if code == 21640:
            extra = (f" Limits (2026): elective deferral {val('fed.retirement.401k.elective_deferral_limit')}, catch-up from age 50 "
                     f"{val('fed.retirement.401k.catch_up_50')}, catch-up at ages 60 to 63 {val('fed.retirement.401k.catch_up_60_63')} "
                     f"[{rid('fed.retirement.401k.elective_deferral_limit')}]. Per-State departures: Pennsylvania {val('pa.base.401k_403b_457_deferral.pit')} "
                     f"[{rid('pa.base.401k_403b_457_deferral.pit')}]; New Jersey 401(k) {val('nj.base.401k.git')} [{rid('nj.base.401k.git')}]; "
                     f"unemployment insurance, Alaska {val('ak.sui.base.401k_deferral')} [{rid('ak.sui.base.401k_deferral')}] and Rhode Island "
                     f"{val('ri.base.401k_125.ui_tdi')} [{rid('ri.base.401k_125.ui_tdi')}]; the other States are on their rows. " + W.ug("fed.plan.402g.elective_deferral.limit_2027", WHY["fed.plan.402g.elective_deferral.limit_2027"]))
        if code == 21645:
            extra = f" SIMPLE deferral limit {val('fed.retirement.simple.deferral_limit')} [{rid('fed.retirement.simple.deferral_limit')}]."
        text = (f"Employee pre-tax {label} (flag class 2, salary reduction: No means removed from the base before the tax): {val(stem + '.fit')} for federal income tax [{rid(stem + '.fit')}]; for social security and Medicare "
                f"{val(stem + '.fica')} [{rid(stem + '.fica')}]; for FUTA {val(stem + '.futa')} [{rid(stem + '.futa')}]. The deferral reduces "
                f"the box 1 wages only. Reported in the annual wage statement box 12.{extra}")
        return fl, basis, text
    # 21642 handled above; other pension codes do not exist
    raise KeyError(code)



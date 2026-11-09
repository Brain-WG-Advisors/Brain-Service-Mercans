"""Independent per-pay-period withholding oracle, US pilot, tax year 2026.

Built only from official publications (see params_sources.md). Pure functions:
    calc(case: dict) -> dict  (lines + flags)
No I/O except loading params_2026.json once at import.

Rounding policy (per line):
  * The publication states a rule          -> applied (NC whole dollar; FICA to the cent, Pub 15).
  * Rule shown only by worked examples     -> cents, half-up, at the step the example rounds (CA, NY, NYC,
                                              Yonkers, IL, GA). Flag 'ROUNDING_FROM_EXAMPLES:<line>'.
  * No rule at all                         -> value returned UNROUNDED (6 dp). Flag 'UNROUNDED:<line>'.
  * FIT: Pub 15-T says rounding to whole dollars is optional -> 'fit' unrounded, plus 'fit_whole_dollar'.
"""
from __future__ import annotations

import json
import os
from decimal import Decimal, ROUND_HALF_UP

_HERE = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(_HERE, "params_2026.json"), encoding="utf-8") as _f:
    P = json.load(_f)

D = lambda x: Decimal(str(x))  # noqa: E731
ZERO = Decimal("0")
C = Decimal("0.01")


def r2(x: Decimal) -> Decimal:
    return x.quantize(C, rounding=ROUND_HALF_UP)


def r0(x: Decimal) -> Decimal:
    return x.quantize(Decimal("1"), rounding=ROUND_HALF_UP)


def raw(x: Decimal) -> Decimal:
    return x.quantize(Decimal("0.000001"), rounding=ROUND_HALF_UP)


def periods(freq: str) -> int:
    return P["periods_per_year"][freq]


def bracket(rows, amount: Decimal, strict: bool):
    """Return (lower, rate, base) for the row that applies.
    strict=True -> row applies when amount > lower ('over'); False -> amount >= lower ('at least')."""
    chosen = rows[0]
    for row in rows:
        lo = D(row[0])
        if (amount > lo) if strict else (amount >= lo):
            chosen = row
    return D(chosen[0]), D(chosen[1]), D(chosen[2])


# ----------------------------------------------------------------------------- federal
def fed_fit(case, flags):
    f = case.get("federal", {})
    freq = case["frequency"]
    n = D(periods(freq))
    wages = D(case["gross"])
    fp = P["federal"]["fit"]
    if f.get("exempt"):
        return ZERO
    if f.get("nra"):
        tbl = fp["nra_addition_2020_w4"] if f.get("w4_version", "2020") == "2020" else fp["nra_addition_pre2020_w4"]
        wages = wages + D(tbl[freq])
        flags.append("FIT_NRA_ADDITION_APPLIED")
    line1c = wages * n
    if f.get("w4_version", "2020") == "2020":
        status = f.get("filing_status", "single")
        step2 = bool(f.get("step2", False))
        line1e = line1c + D(f.get("step4a", 0))
        line1g = ZERO if step2 else D(fp["w4_2020_step1g_std_deduction"]["mfj" if status == "mfj" else "other"])
        aawa = max(ZERO, line1e - (D(f.get("step4b", 0)) + line1g))
        table = fp["annual_tables"]["checkbox" if step2 else "standard"][status]
        credits = D(f.get("step3", 0))
        extra = D(f.get("step4c", 0))
    else:  # 2019-or-earlier W-4, Worksheet 1A lines 1j-1l
        marital = f.get("marital", "single")  # 'single' | 'married' | 'married_single_rate'
        aawa = max(ZERO, line1c - D(f.get("allowances", 0)) * D(fp["pre2020_allowance_value"]))
        table = fp["annual_tables"]["standard"]["mfj" if marital == "married" else "single"]
        credits = ZERO
        extra = D(f.get("additional", 0))
    lo, rate, base = bracket(table, aawa, strict=False)
    tentative = (base + (aawa - lo) * rate) / n
    after_credit = max(ZERO, tentative - credits / n)
    return after_credit + extra


def fed_fica(case, out, flags):
    fd = P["federal"]
    w = D(case["gross"])
    ytd = D(case.get("ytd_gross_before", 0))
    base = D(fd["oasdi"]["wage_base"])
    oasdi_wages = max(ZERO, min(w, base - ytd))
    out["oasdi"] = r2(oasdi_wages * D(fd["oasdi"]["rate_ee"]))
    out["oasdi_er"] = r2(oasdi_wages * D(fd["oasdi"]["rate_er"]))
    out["medicare"] = r2(w * D(fd["medicare"]["rate_ee"]))
    out["medicare_er"] = r2(w * D(fd["medicare"]["rate_er"]))
    thr = D(fd["addl_medicare"]["threshold_employer_withholding"])
    over = max(ZERO, ytd + w - max(thr, ytd))
    out["addl_medicare"] = r2(over * D(fd["addl_medicare"]["rate_ee"]))
    if oasdi_wages < w:
        flags.append("OASDI_WAGE_BASE_REACHED")
    if over > 0:
        flags.append("ADDL_MEDICARE_THRESHOLD_CROSSED")
    futa_wages = max(ZERO, min(w, D(fd["futa"]["wage_base"]) - ytd))
    out["futa_er"] = raw(futa_wages * D(fd["futa"]["net_rate"]))
    flags.append("UNROUNDED:futa_er")
    cr = fd["futa"]["credit_reduction_pending_2026_11_10"].get(case["state"])
    if cr is not None:
        out["futa_credit_reduction_er_pending"] = raw(futa_wages * D(cr))
        flags.append("FUTA_CREDIT_REDUCTION_PENDING_2026-11-10")


# ----------------------------------------------------------------------------- states
def sit_ca(case, flags):
    s = case.get("state_inputs", {})
    freq = case["frequency"]
    p = P["CA"]["pit"]
    w = D(case["gross"])
    status = s.get("filing_status", "single")  # single | married | hoh
    regular = int(s.get("allowances", 0))
    est = int(s.get("est_ded_allowances", 0))
    if status == "married":
        col = "married_2plus" if regular >= 2 else "married_0_1"
        flags.append("CA_MARRIED_COLUMN_BY_REGULAR_ALLOWANCES")
    else:
        col = status
    if w <= D(p["low_income_exemption"][col][freq]):
        return D(s.get("additional", 0))
    if est:
        tbl = p["estimated_deduction_per_allowance_table"][freq]
        w = w - (D(tbl[est - 1]) if est <= 10 else D(tbl[0]) * est)
    ti = w - D(p["standard_deduction"][col][freq])
    rt_status = "married" if status == "married" else status
    credit_tbl = p["exemption_allowance_credit_table"]
    if s.get("method", "period") == "annual":
        n = D(periods(freq))
        ann = D(case["gross"]) * n
        if est:
            at = p["estimated_deduction_per_allowance_table"]["annual"]
            ann -= D(at[est - 1]) if est <= 10 else D(at[0]) * est
        ti_a = ann - D(p["standard_deduction"][col]["annual"])
        lo, rate, base = bracket(p["rate_tables"]["annual"][rt_status], max(ZERO, ti_a), strict=True)
        tax_a = r2(base + rate * (max(ZERO, ti_a) - lo))
        cr = D(credit_tbl["annual"][regular]) if regular <= 10 else D(credit_tbl["annual"][1]) * regular
        tax = r2(max(ZERO, tax_a - cr) / n)
    else:
        lo, rate, base = bracket(p["rate_tables"][freq][rt_status], max(ZERO, ti), strict=True)
        computed = r2(base + rate * (max(ZERO, ti) - lo))
        cr = D(credit_tbl[freq][regular]) if regular <= 10 else D(credit_tbl[freq][1]) * regular
        tax = max(ZERO, computed - cr)
    flags.append("ROUNDING_FROM_EXAMPLES:sit_CA")
    return tax + D(s.get("additional", 0))


def _ny_net(gross, freq, status, allowances, tbl):
    b = D(tbl["deduction_table_B"][status][freq])
    c = D(tbl["exemption_table_C"][freq])
    return gross - (b + c * allowances)


def sit_ny_state(case, flags):
    s = case.get("state_inputs", {})
    freq = case["frequency"]
    status = s.get("filing_status", "single")  # single | married
    p = P["NY"]["pit_state"]
    net = _ny_net(D(case["gross"]), freq, status, int(s.get("allowances", 0)), p)
    if net <= 0:
        return ZERO
    t = p["method2"][status][freq]
    if net >= D(t["method3_at"]):
        n = D(periods(freq))
        annual = net * n
        _, rate, _ = bracket([[r[0], r[1], 0] for r in p["method3"][status]], annual, strict=False)
        flags.append("NY_METHOD_III")
        flags.append("ASSUMED_CENTS:sit_NY_method3")
        return r2(annual * rate / n)
    lo, rate, base = bracket(t["rows"], net, strict=False)
    step4 = r2((r2(net) - lo) * rate)
    flags.append("ROUNDING_FROM_EXAMPLES:sit_NY")
    return step4 + base


def sit_nyc(case, flags):
    s = case.get("state_inputs", {})
    freq = case["frequency"]
    status = s.get("filing_status", "single")
    p = P["NY"]["pit_nyc"]
    net = _ny_net(D(case["gross"]), freq, status, int(s.get("allowances", 0)), p)
    if net <= 0:
        return ZERO
    lo, rate, base = bracket(p["method2_same_for_single_and_married"][freq], net, strict=False)
    flags.append("ROUNDING_FROM_EXAMPLES:sit_NYC")
    return r2((r2(net) - lo) * rate) + base


def sit_il(case, flags):
    s = case.get("state_inputs", {})
    p = P["IL"]["pit"]
    n = D(periods(case["frequency"]))
    ex = r2((D(s.get("line1", 1)) * D(p["line1_allowance"]) + D(s.get("line2", 0)) * D(p["line2_allowance"])) / n)
    taxable = max(ZERO, D(case["gross"]) - ex)
    flags.append("ROUNDING_FROM_EXAMPLES:sit_IL")
    return r2(taxable * D(p["rate"])) + D(s.get("additional", 0))


def sit_pa(case, flags):
    flags.append("UNROUNDED:sit_PA")
    return raw(D(case["gross"]) * D(P["PA"]["pit"]["rate"])) + D(case.get("state_inputs", {}).get("additional", 0))


def _regime(regimes, pay_date):
    for r in regimes:
        if r["effective_from"] <= pay_date and (r["effective_to"] is None or pay_date <= r["effective_to"]):
            return r
    raise ValueError(f"no regime for {pay_date}")


def sit_oh(case, flags):
    s = case.get("state_inputs", {})
    reg = _regime(P["OH"]["pit_regimes"], case["pay_date"])
    flags.append(f"OH_REGIME_FROM_{reg['effective_from']}")
    t = reg["periods"][case["frequency"]]
    tw = D(case["gross"]) - D(t["exemption"]) * int(s.get("exemptions", 0))
    if tw <= 0:
        return D(s.get("additional", 0))
    lo, rate, base = bracket(t["rows"], tw, strict=True)
    flags.append("UNROUNDED:sit_OH")
    return raw(base + rate * (tw - lo)) + D(s.get("additional", 0))


def sit_nc(case, flags):
    s = case.get("state_inputs", {})
    p = P["NC"]["pit"]
    col = "hoh" if s.get("filing_status") == "hoh" else "single_married_qss"
    freq = case["frequency"]
    allow = int(s.get("allowances", 0))
    w = D(case["gross"])
    if s.get("method") != "annualized" and freq in p["percentage_method"][col]:
        sd, per = p["percentage_method"][col][freq]
        net = w - (D(sd) + D(per) * allow)
        tax = r0(max(ZERO, net) * D(p["rate"]))
    else:
        n = D(periods(freq))
        net = w * n - (D(p["annualized_method"]["std_deduction"][col]) + D(p["annualized_method"]["allowance"]) * allow)
        tax = r0(max(ZERO, net) * D(p["rate"]) / n)
    return tax + D(s.get("additional", 0))


def sit_mi(case, flags):
    s = case.get("state_inputs", {})
    p = P["MI"]["pit"]
    n = D(periods(case["frequency"]))
    taxable = max(ZERO, D(case["gross"]) - D(s.get("exemptions", 0)) * D(p["exemption_annual"]) / n)
    flags.append("UNROUNDED:sit_MI")
    flags.append("MI_PER_PERIOD_EXEMPTION_PRORATION_NOT_STATED")
    return raw(taxable * D(p["rate"])) + D(s.get("additional", 0))


def sit_ga(case, flags):
    s = case.get("state_inputs", {})
    reg = _regime(P["GA"]["pit_regimes"], case["pay_date"])
    flags.append(f"GA_REGIME_FROM_{reg['effective_from']}")
    row = reg["table"][case["frequency"]]
    col = {"mfj_one_income": 0, "single": 1, "hoh": 1, "mfs": 2, "mfj_both_working": 2}[s.get("filing_status", "single")]
    taxable = max(ZERO, D(case["gross"]) - D(row[col]) - D(row[3]) * int(s.get("dependents", 0)))
    flags.append("ROUNDING_FROM_EXAMPLES:sit_GA")
    return r2(taxable * D(reg["rate"])) + D(s.get("additional", 0))


SIT = {"CA": sit_ca, "IL": sit_il, "PA": sit_pa, "OH": sit_oh, "NC": sit_nc, "MI": sit_mi, "GA": sit_ga}


# ----------------------------------------------------------------------------- employee programs and SUI
def ee_programs(case, out, flags):
    st = case["state"]
    w = D(case["gross"])
    ytd = D(case.get("ytd_gross_before", 0))
    if st == "CA":
        out["sdi_CA"] = raw(w * D(P["CA"]["sdi"]["rate_ee"]))
        flags.append("UNROUNDED:sdi_CA")
    if st == "NY":
        dbl = P["NY"]["dbl"]
        weeks = D(52) / D(periods(case["frequency"]))
        cap = D(dbl["max_per_week"]) * weeks
        out["dbl_NY"] = raw(min(w * D(dbl["rate_ee"]), cap))
        flags.append("UNROUNDED:dbl_NY")
        flags.append("NY_DBL_WEEKLY_CAP_CONVERTED_52_OVER_PERIODS")
        pfl = P["NY"]["pfl"]
        prior = D(case.get("ytd_pfl_contrib_before", min(D(pfl["annual_max_ee"]), ytd * D(pfl["rate_ee"]))))
        room = max(ZERO, D(pfl["annual_max_ee"]) - prior)
        val = min(w * D(pfl["rate_ee"]), room)
        if val < w * D(pfl["rate_ee"]):
            flags.append("NY_PFL_ANNUAL_MAX_REACHED")
        out["pfl_NY"] = raw(val)
        flags.append("UNROUNDED:pfl_NY")
    if st == "PA":
        out["uc_ee_PA"] = raw(w * D(P["PA"]["uc_ee"]["rate_ee"]))
        flags.append("UNROUNDED:uc_ee_PA")


def sui_er(case, out, flags):
    st = case["state"]
    sp = P[st]["sui"]
    w = D(case["gross"])
    ytd = D(case.get("ytd_gross_before", 0))
    rate = D(case.get("employer", {}).get("sui_rate", sp.get("new_employer_rate", sp.get("new_employer_rate_total"))))
    taxable = max(ZERO, min(w, D(sp["wage_base"]) - ytd))
    if taxable < w:
        flags.append("SUI_WAGE_BASE_REACHED")
    out["sui_er"] = raw(taxable * rate)
    flags.append("UNROUNDED:sui_er")
    if st == "CA":
        out["ett_er_CA"] = raw(max(ZERO, min(w, D(P["CA"]["ett"]["wage_base"]) - ytd)) * D(P["CA"]["ett"]["rate"]))
        flags.append("UNROUNDED:ett_er_CA")


# ----------------------------------------------------------------------------- entry point
def calc(case: dict) -> dict:
    flags: list[str] = []
    out: dict = {}
    fit = fed_fit(case, flags)
    out["fit"] = raw(fit)
    out["fit_whole_dollar"] = r0(fit)
    flags.append("FIT_WHOLE_DOLLAR_ROUNDING_OPTIONAL")
    fed_fica(case, out, flags)
    st = case["state"]
    if st in ("TX", "FL"):
        out[f"sit_{st}"] = ZERO
    elif st == "NY":
        out["sit_NY"] = sit_ny_state(case, flags) + D(case.get("state_inputs", {}).get("additional", 0))
        loc = case.get("state_inputs", {}).get("locality")
        if loc == "nyc":
            out["sit_NYC"] = sit_nyc(case, flags)
        elif loc == "yonkers":
            out["sit_YONKERS"] = r2((out["sit_NY"] - D(case.get("state_inputs", {}).get("additional", 0))) * D(P["NY"]["pit_yonkers_resident"]["factor_of_nys_withholding"]))
            flags.append("ROUNDING_FROM_EXAMPLES:sit_YONKERS")
    else:
        out[f"sit_{st}"] = SIT[st](case, flags)
    ee_programs(case, out, flags)
    sui_er(case, out, flags)
    res = {k: float(v) for k, v in out.items()}
    res["flags"] = sorted(set(flags))
    return res


if __name__ == "__main__":
    import sys
    print(json.dumps(calc(json.loads(sys.argv[1])), indent=2))

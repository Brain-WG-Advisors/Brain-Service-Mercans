"""ours.py - the system under test: per-period withholding computed ONLY from OUR research.

Sources allowed (read-only):
  US-compliance/_research/CCG-annex_{FED,CA,NY,IL,PA,OH,NC,MI,GA,TX,FL}-facts.json  (values)
  US-compliance/_research/WTC-country_specific-facts.json                         (fallback values)
  US-compliance/01-ccg/modules/*.md and annexes/*.md                              (rules)
Not read: oracle.py, params_2026.json, params_sources.md.

calc(case) -> {"lines": {line: amount|None}, "trace": {line: [..tags..]}, "silent": [rule notes]}
Every parameter is fetched by facts key (F(...)) and its key is written into the trace.
Where our artifacts are silent, the assumption is tagged "RESEARCH-SILENT:" in the trace.
A line our research cannot compute returns None ("NOT-COMPUTABLE").
"""
import json, os, sys
from decimal import Decimal as D, ROUND_HALF_UP

HERE = os.path.dirname(os.path.abspath(__file__))
RES = os.path.normpath(os.path.join(HERE, "..", "..", "US-compliance", "_research"))
UNITS = ["FED", "CA", "NY", "IL", "PA", "OH", "NC", "MI", "GA", "TX", "FL"]

_FACTS = {}
def _load():
    for u in UNITS:
        p = os.path.join(RES, f"CCG-annex_{u}-facts.json")
        for x in json.load(open(p, encoding="utf-8"))["facts"]:
            if "key" in x:
                _FACTS.setdefault(x["key"], []).append(dict(x, _file=f"CCG-annex_{u}-facts.json"))
    p = os.path.join(RES, "WTC-country_specific-facts.json")
    for x in json.load(open(p, encoding="utf-8"))["facts"]:
        if "key" in x and x["key"] not in _FACTS:
            _FACTS.setdefault("wtc:" + x["key"], []).append(dict(x, _file="WTC-country_specific-facts.json"))
_load()

def F(key, date, tr):
    """Value of a facts key in force on date (YYYY-MM-DD); records the key in trace list tr."""
    rows = _FACTS.get(key) or _FACTS.get("wtc:" + key)
    if not rows:
        raise KeyError(key)
    hit = [r for r in rows if (r.get("effective_from") or "0000") <= date <= (r.get("effective_to") or "9999")]
    if not hit:
        raise KeyError(f"{key}@{date}")
    r = hit[0]
    tr.append(f"{key}={r['value']} [{r['_file']}]")
    v = r["value"]
    return D(str(v)) if isinstance(v, (int, float)) and not isinstance(v, bool) else v

def r2(x):  # half-up to the cent (m05 5.2 'round_half_up(...,0.01)'; m03 Step 4; CA.14; GA.14; IL.14)
    return x.quantize(D("0.01"), rounding=ROUND_HALF_UP)
def r0(x):  # nearest dollar, 50 cents up (fed.fit.rounding; nc.pit.rounding)
    return x.quantize(D("1"), rounding=ROUND_HALF_UP)

def periods(freq, date, tr):
    s = F("fed.fit.pay_periods_per_year", date, tr)  # '2 / 4 / 12 / 24 / 26 / 52 / 260 (semiannual, quarterly, ...)'
    nums, names = s.split("(")
    nums = [int(n) for n in nums.split("/")]
    names = [n.strip() for n in names.rstrip(")").split(",")]
    m = dict(zip(names, nums))
    return D(m[freq])

def pct(x):
    return x / D(100)

# ---------------------------------------------------------------- federal
def bracket_tax(rows, x):
    """rows: list of (floor, rate%, cumulative or None). cumulative recomputed when None (FED.2 note)."""
    cum = D(0); prev = None; out = D(0)
    built = []
    for i, (fl, rt, cu) in enumerate(rows):
        if cu is None:
            cu = D(0) if prev is None else prev[2] + (fl - prev[0]) * pct(prev[1])
        built.append((fl, rt, cu)); prev = (fl, rt, cu)
    for fl, rt, cu in built:
        if x >= fl:
            out = cu + (x - fl) * pct(rt)
    return out

def fit(case, tr, silent):
    d = case["pay_date"]; f = case["federal"]
    P = periods(case["frequency"], d, tr)
    annual = D(str(case["gross"])) * P
    if f["w4_version"] == "2020":
        st = f["filing_status"]
        step2 = bool(f.get("step2"))
        adj = annual + D(str(f.get("step4a", 0))) - D(str(f.get("step4b", 0)))
        if not step2:
            adj -= F("fed.fit.worksheet1a.line1g." + ("mfj" if st == "mfj" else "other"), d, tr)
        adj = max(D(0), adj)
        sched = "step2" if step2 else "standard"
        rows = []
        for b in range(1, 9):
            fl = F(f"fed.fit.{sched}.{st}.bracket.{b}.floor", d, tr)
            rt = F(f"fed.fit.{sched}.{st}.bracket.{b}.rate", d, tr)
            cu = F(f"fed.fit.{sched}.{st}.bracket.{b}.cumulative_tax", d, tr) if sched == "standard" else None
            rows.append((fl, rt, cu))
        tr.append("m06 6.1.1 Worksheet 1A lines 1a-1i, 2e-2h, 3, 4 (annex FED.2 pseudo-code)")
        tent = bracket_tax(rows, adj)
        step3 = D(str(f.get("step3", 0))); extra = D(str(f.get("step4c", 0)))
        per = max(D(0), tent / P - step3 / P) + extra
    else:
        al = D(str(f.get("allowances", 0)))
        adj = max(D(0), annual - al * F("fed.fit.allowance.pre2020_value", d, tr))
        tr.append("m06 6.1.1: pre-2020 W-4: adjusted_annual = annual_wages - allowances x 4,300 (no line 1g)")
        st = "mfj" if f.get("marital") == "married" else "single"
        tr.append("RESEARCH-SILENT: pre-2020 'married' mapped to MFJ STANDARD column, 'single' to Single column")
        silent.append("FED pre-2020 W-4: column mapping (married->MFJ) and the old W-4 line 6 additional amount are not stated in m06/FED.2")
        rows = [(F(f"fed.fit.standard.{st}.bracket.{b}.floor", d, tr), F(f"fed.fit.standard.{st}.bracket.{b}.rate", d, tr),
                 F(f"fed.fit.standard.{st}.bracket.{b}.cumulative_tax", d, tr)) for b in range(1, 9)]
        tent = bracket_tax(rows, adj)
        extra = D(str(f.get("additional", 0)))
        if extra:
            tr.append("RESEARCH-SILENT: pre-2020 W-4 additional amount added per period like Step 4(c)")
        per = max(D(0), tent / P) + extra
    return per

def federal(case, L, T, silent):
    d = case["pay_date"]; g = D(str(case["gross"])); ytd = D(str(case.get("ytd_gross_before", 0)))
    t = []; v = fit(case, t, silent); L["fit"] = v; T["fit"] = t + ["unrounded (fed.fit.rounding = optional)"]
    t2 = list(t); F("fed.fit.rounding", d, t2); L["fit_whole_dollar"] = r0(v); T["fit_whole_dollar"] = t2 + ["tax rounded to nearest dollar; wages not rounded (RESEARCH-SILENT on combining both optional roundings)"]
    for side in ("employee", "employer"):
        t = []; base = F("fed.fica.oasdi.wage_base", d, t); rate = F(f"fed.fica.oasdi.rate.{side}", d, t)
        room = max(D(0), base - ytd); amt = r2(min(g, room) * pct(rate)); t.append("m03 Step 4 oasdi formula, half-up cent")
        L["oasdi" if side == "employee" else "oasdi_er"] = amt; T["oasdi" if side == "employee" else "oasdi_er"] = t
        t = []; rate = F(f"fed.fica.medicare.rate.{side}", d, t); t.append("m03 Step 4, half-up cent")
        L["medicare" if side == "employee" else "medicare_er"] = r2(g * pct(rate)); T["medicare" if side == "employee" else "medicare_er"] = t
    t = []; thr = F("fed.fica.addl_medicare.withholding_threshold", d, t); rate = F("fed.fica.addl_medicare.rate", d, t)
    L["addl_medicare"] = r2(max(D(0), (ytd + g) - max(thr, ytd)) * pct(rate)); T["addl_medicare"] = t + ["m03 Step 4 / FED.3 formula"]
    t = []; base = F("fed.futa.wage_base", d, t); rate = F("fed.futa.rate.net", d, t)
    L["futa_er"] = r2(min(g, max(D(0), base - ytd)) * pct(rate)); T["futa_er"] = t + ["m05 5.2 half-up cent"]

def sui(case, L, T, rate_key, base_key, extra_keys=()):
    d = case["pay_date"]; g = D(str(case["gross"])); ytd = D(str(case.get("ytd_gross_before", 0)))
    t = []; base = F(base_key, d, t); rate = F(rate_key, d, t)
    for k in extra_keys:
        rate += F(k, d, t)
    rate = D(str(case["employer"]["sui_rate"])) if case.get("employer", {}) and case["employer"].get("sui_rate") is not None else rate
    L["sui_er"] = r2(min(g, max(D(0), base - ytd)) * pct(rate)); T["sui_er"] = t + ["m05 5.2: min(period, base-ytd) x rate, half-up cent"]

# ---------------------------------------------------------------- states
def st_CA(case, L, T, silent):
    d = case["pay_date"]; g = D(str(case["gross"])); s = case["state_inputs"]; t = []
    P = periods(case["frequency"], d, t)
    status = s.get("filing_status", "single"); al = int(s.get("allowances", 0)); ed = int(s.get("est_ded_allowances", 0))
    annual = g * P
    F("ca.wh.status_table_map", d, t)
    col = "married_2plus_hoh" if (status == "hoh" or (status == "married" and al >= 2)) else "single"
    lie = F(f"ca.wh.low_income_exemption.{col}", d, t)
    t.append("CA.2 Method B pseudo-code: annualise; LIE test; taxable = annual - est.ded x n - std; brackets - credit x allowances; /periods")
    if s.get("method") == "annual":
        t.append("case method=annual: CA.2 pseudo-code is already annualised; same computation")
    if annual <= lie:
        tax = D(0)
    else:
        taxable = annual - F("ca.wh.estimated_deduction.per_allowance", d, t) * ed - F(f"ca.wh.std_deduction.{col}", d, t)
        taxable = max(D(0), taxable)
        tab = {"single": "single", "married": "married", "hoh": "hoh"}[status]
        rows = []; prev_ceiling = D(0)
        for b in range(1, 11):
            rt = F(f"ca.pit.bracket.{tab}.{b}.rate", d, t)
            base = F(f"ca.pit.bracket.{tab}.{b}.base", d, t) if tab != "single" else None
            rows.append((prev_ceiling, rt, base))
            if b < 10:
                prev_ceiling = F(f"ca.pit.bracket.{tab}.{b}.ceiling", d, t)
        if tab == "single":
            t.append("single bases recomputed from ceilings and rates (CA.14 / ca.oracle.de44.example_e note: 'single cumulative bases also re-derive')")
        gross_tax = bracket_tax(rows, taxable)
        annual_tax = gross_tax - F("ca.wh.allowance_credit.per_allowance", d, t) * al
        tax = max(D(0), annual_tax) / P
    L["sit_CA"] = r2(tax); T["sit_CA"] = t + ["CA.14: half-up to the cent"]
    t = []; L["sdi_CA"] = r2(g * pct(F("ca.sdi.employee.rate", d, t))); F("ca.sdi.wage_cap.exists", d, t); T["sdi_CA"] = t + ["CA.3 formula, no cap; m05 half-up cent"]
    sui(case, L, T, "ca.sui.new_employer.rate", "ca.sui.wage_base")
    t = []; base = F("ca.sui.wage_base", d, t); rate = F("ca.ett.rate", d, t)
    ytd = D(str(case.get("ytd_gross_before", 0)))
    L["ett_er_CA"] = r2(min(g, max(D(0), base - ytd)) * pct(rate)); T["ett_er_CA"] = t + ["ca.ett.rate note: 'On first 7,000'"]
    L["futa_credit_reduction_er_pending"] = None
    T["futa_credit_reduction_er_pending"] = ["NOT-COMPUTABLE: fed.futa.credit_reduction.ca unresolved (GAP RQ-402), final only after 2026-11-10"]

import re
_FREQN = {"daily": "daily", "weekly": "weekly", "biweekly": "biweekly", "semimonthly": "semimonthly", "monthly": "monthly"}
def _per_period(key, date, freq, status_idx, tr):
    """Printed per-period amount inside the facts note ('weekly 142.30/152.90'); None if the note does not print it."""
    rows = _FACTS.get(key) or []
    hit = [r for r in rows if (r.get("effective_from") or "0000") <= date <= (r.get("effective_to") or "9999")]
    if not hit:
        raise KeyError(key)
    note = hit[0].get("note", "")
    m = re.search(r"(?<![a-z])" + freq + r"\s+([0-9.]+)(?:/([0-9.]+))?", note)
    if not m:
        return None
    v = m.group(1 + status_idx) if status_idx == 0 else (m.group(2) or m.group(1))
    tr.append(f"{key} per-period {freq}={v} [printed in note]")
    return D(v)

def _m2_tax(prefix, status, net, P, d, t, nbr):
    """Method II: bracket on the per-period schedule. Facts carry only the ANNUAL schedule, so the
    per-period table is derived (floor/P to whole dollar, add/P to the cent: ny.wh.method2.annualisation note, G-DERIVE)."""
    rows = []
    for i in range(1, nbr + 1):
        s = []
        fl = F(f"{prefix}.{status}.bracket.{i}.floor", d, s); rt = F(f"{prefix}.{status}.bracket.{i}.rate", d, s); bs = F(f"{prefix}.{status}.bracket.{i}.base", d, s)
        rows.append((i, fl, rt, bs))
    line = None
    for i, fl, rt, bs in rows:
        if net >= (fl / P).quantize(D("1"), rounding=ROUND_HALF_UP):
            line = (i, fl, rt, bs)
    i, fl, rt, bs = line
    s = []
    F(f"{prefix}.{status}.bracket.{i}.floor", d, s); F(f"{prefix}.{status}.bracket.{i}.rate", d, s); F(f"{prefix}.{status}.bracket.{i}.base", d, s)
    t.extend(s)
    col3 = (fl / P).quantize(D("1"), rounding=ROUND_HALF_UP); col5 = r2(bs / P)
    t.append(f"{prefix} line {i}: (net - {col3}) x {rt}% + {col5} (per-period table derived from annual: G-DERIVE, ny.wh.method2.annualisation note)")
    return (net - col3) * pct(rt) + col5

def ny_sit(case, L, T, silent):
    d = case["pay_date"]; s = case["state_inputs"]; g = D(str(case["gross"])); freq = case["frequency"]
    status = "married" if s.get("filing_status") == "married" else "single"; idx = 1 if status == "married" else 0
    n = min(int(s.get("allowances", 0)), 10)
    loc = s.get("locality")
    RS = "RESEARCH-SILENT: rounding per RQ-263 open; half-up used"
    def tableA(dk, ek, t):
        ded = _per_period(dk, d, freq, idx, t); ex = _per_period(ek, d, freq, 0, t)
        if ded is None or ex is None:
            return None, [k for k, v in ((dk, ded), (ek, ex)) if v is None]
        return ded + ex * n, []
    t = []; F("ny.wh.method", d, t); F("ny.wh.method2.annualisation", d, t)
    P = periods(freq, d, t)
    F(f"ny.wh.method2.{status}.deduction_allowance", d, t); F("ny.wh.method2.exemption_allowance", d, t)
    A, miss = tableA(f"ny.wh.method2.{status}.deduction_allowance", "ny.wh.method2.exemption_allowance", t)
    if A is None:
        L["sit_NY"] = None; T["sit_NY"] = t + [f"NOT-COMPUTABLE: per-period allowance not printed for {freq}: {miss}"]; nys = None
    else:
        net = max(D(0), g - A); t.append(f"Table A = B + {n} x C = {A}; net wages = {net}")
        ann = net * P
        thr = F(f"ny.wh.method3.{status}.threshold", d, t)
        if ann >= thr:
            rate = None
            for i in (1, 2, 3):
                fl = F(f"ny.wh.method3.{status}.bracket.{i}.floor", d, []) if i > 1 else thr
                if ann >= fl: rate = i
            rt = F(f"ny.wh.method3.{status}.bracket.{rate}.rate", d, t)
            F("ny.wh.method3.annualisation", d, t)
            tax = ann * pct(rt) / P; t.append(f"Method III (annualised net {ann} >= {thr}): flat {rt}% on annualised / P")
        else:
            tax = _m2_tax("ny.wh.method2", status, net, P, d, t, 12 if status == "married" else 10)
        nys = r2(max(D(0), tax)); L["sit_NY"] = nys; T["sit_NY"] = t + [RS]
    if loc == "nyc":
        t = []; F("ny.pit.local.nyc.basis", d, t); F("ny.local.nyc.method2.annualisation", d, t)
        F(f"ny.local.nyc.method2.{status}.deduction_allowance", d, t); F("ny.local.nyc.method2.exemption_allowance", d, t)
        A, miss = tableA(f"ny.local.nyc.method2.{status}.deduction_allowance", "ny.local.nyc.method2.exemption_allowance", t)
        if A is None:
            L["sit_NYC"] = None; T["sit_NYC"] = t + [f"NOT-COMPUTABLE: per-period NYC allowance for {freq} is not printed in facts (only semimonthly/monthly deduction); missing: {miss}"]
        else:
            net = max(D(0), g - A); t.append(f"NYC Table A = {A}; net wages = {net}")
            tax = _m2_tax("ny.local.nyc.method2", status, net, P, d, t, 6)
            L["sit_NYC"] = r2(max(D(0), tax)); T["sit_NYC"] = t + [RS]
    if loc == "yonkers":
        t = []; F("ny.local.yonkers.resident.surcharge.method", d, t)
        rt = F("ny.local.yonkers.resident.surcharge.rate", d, t)
        if nys is None:
            L["sit_YONKERS"] = None; T["sit_YONKERS"] = t + ["NOT-COMPUTABLE: NYS Method II amount not computable"]
        else:
            L["sit_YONKERS"] = r2(nys * pct(rt)); T["sit_YONKERS"] = t + [f"{rt}% of NYS amount {nys}", RS]

def st_NY(case, L, T, silent):
    d = case["pay_date"]; g = D(str(case["gross"])); s = case["state_inputs"]
    ny_sit(case, L, T, silent)
    t = []; P = periods(case["frequency"], d, t)
    rate = F("ny.pfl.employee.rate", d, t); mx = F("ny.pfl.employee.max_annual", d, t)
    ytd = D(str(case.get("ytd_gross_before", 0)))
    if case.get("ytd_pfl_contrib_before") is not None:
        prior = D(str(case["ytd_pfl_contrib_before"]))
    else:
        prior = min(mx, r2(ytd * pct(rate)))
        t.append("RESEARCH-SILENT: prior PFL contributions inferred as min(max, ytd wages x rate)")
    L["pfl_NY"] = r2(min(g * pct(rate), max(D(0), mx - prior))); T["pfl_NY"] = t + ["NY.3: rate on wages, annual max; m05 half-up cent"]
    t = []; rate = F("ny.dbl.employee.rate", d, t); wk = F("ny.dbl.employee.max_weekly", d, t)
    weeks = D(52) / P
    t.append("m05 5.2: 'convert these per pay period' - RESEARCH-SILENT on the conversion; used weekly cap x 52/periods")
    silent.append("NY DBL: weekly cap 0.60 conversion to non-weekly periods not stated (m05 says 'convert', no rule)")
    L["dbl_NY"] = r2(min(g * pct(rate), wk * weeks)); T["dbl_NY"] = t
    sui(case, L, T, "ny.sui.new_employer.total.rate", "ny.sui.wage_base")

def st_IL(case, L, T, silent):
    d = case["pay_date"]; g = D(str(case["gross"])); s = case["state_inputs"]; t = []
    P = periods(case["frequency"], d, t)
    F("il.wh.method", d, t)
    ex = F("il.wh.exemption.line1", d, t) * int(s.get("line1", 0)) + F("il.wh.exemption.line2", d, t) * int(s.get("line2", 0))
    exp = r2(ex / P); t.append("IL.14: per-period exemption rounded to the cent")
    tax = max(D(0), (g - exp)) * pct(F("il.pit.rate.flat", d, t)) + D(str(s.get("additional", 0)))
    L["sit_IL"] = r2(tax); T["sit_IL"] = t + ["IL.14: amounts half-up to the cent (il.wh.method note: no rounding rule)"]
    sui(case, L, T, "il.sui.new_employer.rate", "il.sui.wage_base")

def st_PA(case, L, T, silent):
    d = case["pay_date"]; g = D(str(case["gross"])); s = case["state_inputs"]; t = []
    tax = g * pct(F("pa.pit.rate.flat", d, t)); F("pa.pit.rounding", d, t)
    if s.get("additional"):
        t.append("RESEARCH-SILENT: PA.2 'no PA W-4, no allowances'; voluntary additional withholding not addressed -> not added")
        silent.append("PA: voluntary additional state withholding not addressed (PA.2 says no PA W-4)")
    L["sit_PA"] = tax; T["sit_PA"] = t + ["PA.2 compensation x rate; unrounded (pa.pit.rounding none published)"]
    t = []; L["uc_ee_PA"] = r2(g * pct(F("pa.sui.employee.rate", d, t))); T["uc_ee_PA"] = t + ["PA.3: all wages, no cap, rounded to the cent"]
    sui(case, L, T, "pa.sui.new_employer.rate", "pa.sui.wage_base")

def st_OH(case, L, T, silent):
    d = case["pay_date"]; g = D(str(case["gross"])); s = case["state_inputs"]; t = []
    P = periods(case["frequency"], d, t)
    tw = max(D(0), g * P - F("oh.pit.wh.exemption.annual", d, t) * int(s.get("exemptions", 0)))
    b1 = F("oh.pit.wh.break.1", d, t); b2 = F("oh.pit.wh.break.2", d, t)
    r1_ = F("oh.pit.wh.rate.1", d, t); r2_ = F("oh.pit.wh.rate.2", d, t); r3_ = F("oh.pit.wh.rate.3", d, t)
    bt2 = F("oh.pit.wh.base_tax.2", d, t); bt3 = F("oh.pit.wh.base_tax.3", d, t)
    if tw <= b1: tax = tw * pct(r1_)
    elif tw <= b2: tax = bt2 + (tw - b1) * pct(r2_)
    else: tax = bt3 + (tw - b2) * pct(r3_)
    L["sit_OH"] = tax / P; T["sit_OH"] = t + ["OH.2 'Formula (annualised)', edition by pay date; OH.2 rounding: no rounding instruction -> unrounded"]
    sui(case, L, T, "oh.sui.new_employer.rate", "oh.sui.wage_base")

def st_NC(case, L, T, silent):
    d = case["pay_date"]; g = D(str(case["gross"])); s = case["state_inputs"]; t = []
    P = periods(case["frequency"], d, t)
    stt = s.get("filing_status", "single")
    if stt == "hoh":
        std = F("nc.pit.std_deduction.head_of_household", d, t)
    else:
        std = F("nc.pit.std_deduction.single", d, t)
        if stt == "mfj":
            t.append("nc.pit.std_deduction.single note: 'married withholding tables use single deduction (US-NC-001)'")
    al = F("nc.pit.allowance.amount", d, t) * int(s.get("allowances", 0))
    tax = max(D(0), g * P - std - al) * pct(F("nc.pit.wh.rate", d, t)) / P + D(str(s.get("additional", 0)))
    F("nc.pit.rounding", d, t)
    L["sit_NC"] = r0(tax); T["sit_NC"] = t + ["NC.2 / m12 ex.13 annualised method, nearest whole dollar"]
    sui(case, L, T, "nc.sui.new_employer.rate", "nc.sui.wage_base")

def st_MI(case, L, T, silent):
    d = case["pay_date"]; g = D(str(case["gross"])); s = case["state_inputs"]; t = []
    P = periods(case["frequency"], d, t)
    F("mi.wh.method", d, t)
    exper = r2(F("mi.wh.exemption.annual", d, t) * int(s.get("exemptions", 0)) / P)
    t.append("mi.wh.method note: per-period exemption = annual/periods, derived to the cent (weekly 113.46, biweekly 226.92...)")
    if case["frequency"] == "daily":
        t.append("RESEARCH-SILENT: no daily exemption stated; used 5,900/260 (fed.fit.pay_periods_per_year)")
        silent.append("MI daily pay: per-period exemption for daily payroll not stated")
    tax = max(D(0), g - exper) * pct(F("mi.pit.rate.flat", d, t)) + D(str(s.get("additional", 0)))
    L["sit_MI"] = tax; T["sit_MI"] = t + ["no rounding rule (mi.wh.method note) -> unrounded"]
    sui(case, L, T, "mi.sui.new_employer.rate", "mi.sui.wage_base")

def st_GA(case, L, T, silent):
    d = case["pay_date"]; g = D(str(case["gross"])); s = case["state_inputs"]; t = []
    P = periods(case["frequency"], d, t)
    F("ga.wh.method", d, t)
    stt = s.get("filing_status", "single")
    std_a = F("ga.wh.std_deduction.mfj", d, t) if stt == "mfj_one_income" else F("ga.wh.std_deduction.single", d, t)
    if stt == "mfj_both_working":
        t.append("ga.wh.std_deduction.mfj note: 'married both working use MFS column' (= single 15,000)")
    stdp = r2(std_a / P); depp = r2(F("ga.wh.dependent_allowance", d, t) / P)
    t.append("ga.wh.method note: per-period values = annual / periods rounded to cent")
    rate = F("ga.wh.rate", d, t)
    tax = max(D(0), g - stdp - depp * int(s.get("dependents", 0))) * pct(rate) + D(str(s.get("additional", 0)))
    L["sit_GA"] = r2(tax); T["sit_GA"] = t + ["GA.14: half-up to the cent; rate by pay date"]
    sui(case, L, T, "ga.sui.new_employer.rate.total", "ga.sui.wage_base")

def st_TX(case, L, T, silent):
    t = []; F("tx.pit.exists", case["pay_date"], t); L["sit_TX"] = D(0); T["sit_TX"] = t
    sui(case, L, T, "tx.sui.new_employer.rate", "tx.sui.wage_base")

def st_FL(case, L, T, silent):
    t = []; F("fl.pit.exists", case["pay_date"], t); L["sit_FL"] = D(0); T["sit_FL"] = t
    sui(case, L, T, "fl.sui.new_employer.rate", "fl.sui.wage_base")
    T["sui_er"].append("fl.sui.rounding half-cent up")

STATES = {k[3:]: v for k, v in globals().items() if k.startswith("st_")}

def calc(case):
    L, T, silent = {}, {}, []
    federal(case, L, T, silent)
    STATES[case["state"]](case, L, T, silent)
    out = {k: (None if v is None else float(v)) for k, v in L.items()}
    return {"lines": out, "trace": T, "silent": sorted(set(silent))}

if __name__ == "__main__":
    print(json.dumps(calc(json.loads(sys.argv[1])), indent=1))

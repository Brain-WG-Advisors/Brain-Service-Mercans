# -*- coding: utf-8 -*-
"""CCG worked examples, US build (stage 1, units m09_termination and m12_worked_examples).

Reads every rate, ceiling, bracket and constant from _research/*-facts.json by key
(through 01-ccg/_build/m08_m13/factlib.py), computes every line with Decimal half-up
rounding to the cent, and writes:
  01-ccg/modules/m12_worked_examples.md   Module 12 (complete)
  01-ccg/_examples/out/m09_redundancy.md  Module 9 redundancy payout example
  01-ccg/_examples/out/m09_bonus.md       Module 9 bonus example
  01-ccg/_examples/out/results.json       every computed result (for the validation suite)
No number in these outputs is typed by hand: scenario inputs (wages, hours, periods)
are declared in SCENARIOS below; every statutory figure is a [[FACT:]] tag.
Run: python -I build_examples.py   (exit 1 if any recomputed oracle disagrees with its fact)
"""
import json
import os
import sys
from decimal import Decimal, ROUND_HALF_UP

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "_build", "m08_m13"))
import factlib as F  # noqa: E402

T, V, R = F.T, F.V, F.R
OUT = os.path.join(HERE, "out")
MOD = os.path.join(HERE, "..", "modules")
os.makedirs(OUT, exist_ok=True)
RESULTS = {}
FAILS = []


def D(x):
    return Decimal(str(x))


def c2(x):
    return D(x).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)


def c0(x):
    return D(x).quantize(Decimal("1"), rounding=ROUND_HALF_UP)


def m(x, nd=2):
    x = D(x)
    q = Decimal(1).scaleb(-nd)
    return f"{x.quantize(q, rounding=ROUND_HALF_UP):,.{nd}f}"


def pct(key, **kw):
    return f"{T(key, **kw)}%"


def table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join("---" for _ in header) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) for c in r) + " |")
    return "\n".join(out)


# ------------------------------------------------------------------ federal FIT
def fit_annual(status, adjusted):
    """Annual Percentage Method (STANDARD schedule) bracket for an adjusted annual wage."""
    i = 1
    for n in range(1, 9):
        if adjusted >= D(V(f"fed.fit.standard.{status}.bracket.{n}.floor")):
            i = n
    return i


def fit_lines(loc, status, wage, periods, label_periods):
    """Worksheet 1A (2020+ W-4, Step 2 not checked, Steps 3/4 blank). Returns rows, per-period FIT."""
    F.set_loc(loc)
    rows = []
    annual = c2(D(wage) * periods)
    rows.append(("Annualised wages", f"{m(wage)} × {periods} ({label_periods})", m(annual)))
    l1g_key = "fed.fit.worksheet1a.line1g.mfj" if status == "mfj" else "fed.fit.worksheet1a.line1g.other"
    adj = annual - D(V(l1g_key))
    rows.append(("Adjusted annual wage (W-4 Step 2 not checked: less the line 1g amount)",
                 f"{m(annual)} − {T(l1g_key)}", m(adj)))
    b = fit_annual(status, adj)
    fl, rt, cum = (f"fed.fit.standard.{status}.bracket.{b}.{x}" for x in ("floor", "rate", "cumulative_tax"))
    tax = D(V(cum)) + (adj - D(V(fl))) * D(V(rt)) / 100
    rows.append((f"Annual tentative withholding (STANDARD {status.upper()} schedule, row {b})",
                 f"{T(cum)} + ({m(adj)} − {T(fl)}) × {T(rt)}%", m(tax)))
    per = c2(tax / periods)
    rows.append(("Per-period FIT", f"{m(tax)} ÷ {periods}", m(per)))
    return rows, per


def fica_rows(loc, wage, ytd_before=0):
    """OASDI = rate × lesser of (remaining annual base, period wage); Medicare; Additional Medicare."""
    F.set_loc(loc)
    wage, ytd = D(wage), D(ytd_before)
    base_key = "fed.fica.oasdi.wage_base"
    base = D(V(base_key, ef="2026-01-01"))
    remaining = max(Decimal(0), base - ytd)
    oasdi_base = min(remaining, wage)
    rows = []
    if ytd > 0:
        rows.append(("OASDI base remaining before this pay", f"{T(base_key, ef='2026-01-01')} − {m(ytd)}", m(remaining)))
        rows.append(("OASDI base for this pay (lesser of remaining base and pay)", f"min({m(remaining)}, {m(wage)})", m(oasdi_base)))
    ee = c2(oasdi_base * D(V("fed.fica.oasdi.rate.employee")) / 100)
    med = c2(wage * D(V("fed.fica.medicare.rate.employee")) / 100)
    thr = D(V("fed.fica.addl_medicare.withholding_threshold"))
    over = max(Decimal(0), ytd + wage - max(thr, ytd))
    addl = c2(over * D(V("fed.fica.addl_medicare.rate")) / 100)
    return rows, oasdi_base, ee, med, over, addl


# ------------------------------------------------------------------ examples
SCENARIOS = {
    "A": dict(title="Full-time resident employee on a standard salary (Texas, biweekly)",
              wage=3000, periods=26, plabel="biweekly", status="single", ytd=0, state="TX"),
    "B": dict(title="Part-time hourly employee at the federal minimum wage (weekly)",
              hours=24, periods=52, plabel="weekly", status="single", ytd=0),
    "C": dict(title="High earner crossing the OASDI wage base and the Additional Medicare threshold (semimonthly)",
              wage=20000, periods=24, plabel="semimonthly", status="single", ytd=182000),
}


def gross_to_net(key, sc, wage, loc):
    lines = []
    fit_rows, fit = fit_lines(loc, sc["status"], wage, sc["periods"], sc["plabel"])
    f_rows, ob, ee, med, over, addl = fica_rows(loc, wage, sc.get("ytd", 0))
    F.set_loc(loc)
    lines.append(f"**Federal income tax: Pub. 15-T 2026 Worksheet 1A, Annual Percentage Method** "
                 f"({T('fed.fit.method')}) {F.REG('fed.fit.method')}")
    lines.append("")
    lines.append(table(["Line", "Calculation", "Result (USD)"], fit_rows))
    lines.append("")
    lines.append("**FICA (employee)** " + F.REG("fed.fica.oasdi.rate.employee"))
    lines.append("")
    rows = list(f_rows)
    rows.append(("OASDI employee", f"{m(ob)} × {pct('fed.fica.oasdi.rate.employee')}", m(ee)))
    rows.append(("Medicare employee", f"{m(wage)} × {pct('fed.fica.medicare.rate.employee')}", m(med)))
    if over > 0:
        rows.append(("Wages above the Additional Medicare threshold in this pay",
                     f"{m(D(sc.get('ytd', 0)) + D(wage))} − {T('fed.fica.addl_medicare.withholding_threshold')}", m(over)))
        rows.append(("Additional Medicare (employee only)", f"{m(over)} × {pct('fed.fica.addl_medicare.rate')}", m(addl)))
    lines.append(table(["Line", "Calculation", "Result (USD)"], rows))
    lines.append("")
    net = D(wage) - fit - ee - med - addl
    calc = f"{m(wage)} − {m(fit)} − {m(ee)} − {m(med)}" + (f" − {m(addl)}" if addl else "")
    lines.append("**Net pay**")
    lines.append("")
    lines.append(table(["Line", "Calculation", "Result (USD)"], [
        ("Gross pay", "—", m(wage)),
        ("Total employee deductions", f"{m(fit)} + {m(ee)} + {m(med)}" + (f" + {m(addl)}" if addl else ""),
         m(fit + ee + med + addl)),
        ("Net pay", calc, m(net)),
    ]))
    lines.append("")
    er_oasdi = c2(ob * D(V("fed.fica.oasdi.rate.employer")) / 100)
    er_med = c2(D(wage) * D(V("fed.fica.medicare.rate.employer")) / 100)
    futa_base = max(Decimal(0), min(D(wage), D(V("fed.futa.wage_base")) - D(sc.get("ytd", 0))))
    futa = c2(futa_base * D(V("fed.futa.rate.net")) / 100)
    er_rows = [
        ("OASDI employer", f"{m(ob)} × {pct('fed.fica.oasdi.rate.employer')}", m(er_oasdi)),
        ("Medicare employer (no employer share of Additional Medicare)",
         f"{m(wage)} × {pct('fed.fica.medicare.rate.employer')}", m(er_med)),
        ("FUTA base in this pay (first " + T("fed.futa.wage_base") + " per employee per year)",
         f"min({m(wage)}, {T('fed.futa.wage_base')} − {m(sc.get('ytd', 0))})", m(futa_base)),
        ("FUTA (net rate after the full state credit)", f"{m(futa_base)} × {pct('fed.futa.rate.net')}", m(futa)),
        ("Total employer federal cost", f"{m(er_oasdi)} + {m(er_med)} + {m(futa)}", m(er_oasdi + er_med + futa)),
    ]
    lines.append("**Employer federal contributions** " + F.REG("fed.futa.rate.net"))
    lines.append("")
    lines.append(table(["Line", "Calculation", "Result (USD)"], er_rows))
    RESULTS[key] = dict(gross=str(m(wage)), fit=str(fit), oasdi=str(ee), medicare=str(med), addl_medicare=str(addl),
                        net=str(c2(net)), er_oasdi=str(er_oasdi), er_medicare=str(er_med), futa=str(futa))
    return lines


def supplemental_example(key, loc, amount, ytd, title):
    F.set_loc(loc)
    amount, ytd = D(amount), D(ytd)
    fit = c2(amount * D(V("fed.fit.supplemental.flat_rate")) / 100)
    f_rows, ob, ee, med, over, addl = fica_rows(loc, amount, ytd)
    F.set_loc(loc)
    rows = [("Supplemental payment (paid separately from regular wages)", "—", m(amount)),
            ("FIT, optional flat rate (supplemental wages up to " + T("fed.fit.supplemental.mandatory_threshold") +
             " in the year)", f"{m(amount)} × {pct('fed.fit.supplemental.flat_rate')}", m(fit))]
    rows += f_rows
    rows += [("OASDI employee", f"{m(ob)} × {pct('fed.fica.oasdi.rate.employee')}", m(ee)),
             ("Medicare employee", f"{m(amount)} × {pct('fed.fica.medicare.rate.employee')}", m(med))]
    if addl:
        rows.append(("Additional Medicare", f"{m(over)} × {pct('fed.fica.addl_medicare.rate')}", m(addl)))
    net = amount - fit - ee - med - addl
    rows.append(("Net payment", f"{m(amount)} − {m(fit)} − {m(ee)} − {m(med)}" + (f" − {m(addl)}" if addl else ""), m(net)))
    RESULTS[key] = dict(amount=str(m(amount)), fit=str(fit), oasdi=str(ee), medicare=str(med), net=str(c2(net)))
    return [f"*{title}*", "", table(["Line", "Calculation", "Result (USD)"], rows)]


# ------------------------------------------------------------------ state oracles
ORACLES = []   # (oracle key, jurisdiction, case text, rows, computed, shown_rounding)


def oracle(okey, jur, case, rows, computed, whole_dollar_key=None):
    """Record a recomputed oracle; compare with the oracle fact at the cent (or dollar)."""
    fact = D(V(okey))
    if whole_dollar_key:
        ok = c0(computed) == fact or c2(computed) == fact
    else:
        ok = c2(computed) == c2(fact)
    if not ok:
        FAILS.append((okey, str(computed), str(fact)))
    ORACLES.append((okey, jur, case, rows, computed, whole_dollar_key, ok))


def state_oracles(loc):
    F.set_loc(loc)
    # GA: (wages - std/24 - dependent/24) x 4.99 %   (MFJ one dependent, semimonthly 2,000)
    sd, dep = D(V("ga.wh.std_deduction.mfj")), D(V("ga.wh.dependent_allowance"))
    rate = D(V("ga.wh.rate", on="2026-06-01"))  # round 2: withholding level
    p_sd, p_dep = c2(sd / 24), c2(dep / 24)
    base = D(2000) - p_sd - p_dep
    w = base * rate / 100
    oracle("ga.oracle.mfj_semimonthly.withholding", "GA", "MFJ, one dependent, semimonthly 2,000.00 (from 2026-05-11)", [
        ("Period standard deduction", f"{T('ga.wh.std_deduction.mfj')} ÷ 24", m(p_sd)),
        ("Period dependent allowance (1)", f"{T('ga.wh.dependent_allowance')} ÷ 24", m(p_dep)),
        ("Withholding", f"(2,000.00 − {m(p_sd)} − {m(p_dep)}) × {T('ga.wh.rate', on='2026-06-01')}%", m(w, 4))], w)
    # LA: (S - std/N) x 3.09 %
    r = D(V("la.pit.rate.flat"))
    s1 = D(V("la.wh.std_deduction.single"))
    w1 = (D(700) - s1 / 52) * r / 100
    oracle("la.oracle.weekly_700.withholding", "LA", "L-4 \"1\", weekly 700.00", [
        ("Withholding", f"(700.00 − {T('la.wh.std_deduction.single')} ÷ 52) × {T('la.pit.rate.flat')}%", m(w1, 4))], w1)
    s2 = D(V("la.wh.std_deduction.joint"))
    w2 = (D(4600) - s2 / 26) * r / 100
    oracle("la.oracle.biweekly_4600.withholding", "LA", "L-4 \"2\", biweekly 4,600.00", [
        ("Withholding", f"(4,600.00 − {T('la.wh.std_deduction.joint')} ÷ 26) × {T('la.pit.rate.flat')}%", m(w2, 4))], w2)
    # MI state: (2,000 - biweekly exemption) x 4.25 %
    ex = D(V("mi.wh.exemption.biweekly"))
    w = (D(2000) - ex) * D(V("mi.pit.rate.flat")) / 100
    oracle("mi.oracle.biweekly_2000_1ex.withholding", "MI", "MI-W4 one exemption, biweekly 2,000.00", [
        ("Withholding", f"(2,000.00 − {T('mi.wh.exemption.biweekly')}) × {T('mi.pit.rate.flat')}%", m(w, 4))], w)
    # Detroit resident
    ex = D(V("mi.local.detroit.exemption.annual")) / 26
    w = (D(2000) - ex) * D(V("mi.local.detroit.rate.resident")) / 100
    oracle("mi.oracle.detroit.resident_biweekly_2000", "MI (Detroit)", "Detroit resident, one exemption, biweekly 2,000.00", [
        ("Withholding", f"(2,000.00 − {T('mi.local.detroit.exemption.annual')} ÷ 26) × {T('mi.local.detroit.rate.resident')}%", m(w, 4))], w)
    # MN
    ann = D(2000) * 26 - D(V("mn.pit.allowance.amount"))
    tax = D(V("mn.pit.wh.single.2.base_tax")) + (ann - D(V("mn.pit.wh.single.2.floor"))) * D(V("mn.pit.wh.single.2.rate")) / 100
    oracle("mn.pit.oracle.example_1.withholding", "MN", "Single, one allowance, biweekly 2,000.00", [
        ("Annual taxable wages", f"2,000.00 × 26 − {T('mn.pit.allowance.amount')}", m(ann)),
        ("Annual tax", f"{T('mn.pit.wh.single.2.base_tax')} + ({m(ann)} − {T('mn.pit.wh.single.2.floor')}) × {T('mn.pit.wh.single.2.rate')}%", m(tax)),
        ("Withholding", f"{m(tax)} ÷ 26", m(tax / 26, 4))], tax / 26)
    # OH (tables from 2026-08-01)
    on = "2026-08-01"
    tw = D(2000) * 26 - D(V("oh.pit.wh.exemption.annual"))
    tax = D(V("oh.pit.wh.base_tax.2", on=on)) + (tw - D(V("oh.pit.wh.break.1", on=on))) * D(V("oh.pit.wh.rate.2", on=on)) / 100
    oracle("oh.pit.oracle.example_1.withholding", "OH", "One exemption, biweekly 2,000.00 (tables from 2026-08-01)", [
        ("Annual taxable wages", f"2,000.00 × 26 − {T('oh.pit.wh.exemption.annual')}", m(tw)),
        ("Annual tax", f"{T('oh.pit.wh.base_tax.2', on=on)} + ({m(tw)} − {T('oh.pit.wh.break.1', on=on)}) × {T('oh.pit.wh.rate.2', on=on)}%", m(tax)),
        ("Withholding", f"{m(tax)} ÷ 26", m(tax / 26, 4))], tax / 26)
    # NC single, two allowances, weekly 450
    sdw = D(V("nc.pit.std_deduction.single")) / 52
    alw = 2 * D(V("nc.pit.allowance.amount")) / 52
    w = (D(450) - sdw - alw) * D(V("nc.pit.wh.rate")) / 100
    oracle("nc.oracle.weekly_450_s2.withholding", "NC", "Single, two allowances, weekly 450.00 (before whole-dollar rounding)", [
        ("Weekly standard deduction", f"{T('nc.pit.std_deduction.single')} ÷ 52", m(sdw, 4)),
        ("Weekly allowances (2)", f"2 × {T('nc.pit.allowance.amount')} ÷ 52", m(alw, 4)),
        ("Withholding", f"(450.00 − {m(sdw, 4)} − {m(alw, 4)}) × {T('nc.pit.wh.rate')}%", m(w, 4))], w)
    # SC three allowances, weekly 750
    ann = D(750) * 52
    sdd = min(ann * D(V("sc.pit.wh.std_deduction.rate")) / 100, D(V("sc.pit.wh.std_deduction.cap")))
    ti = ann - 3 * D(V("sc.pit.allowance.annual")) - sdd
    tax = ti * D(V("sc.pit.wh.band.3.rate")) / 100 - D(V("sc.pit.wh.band.3.subtract"))
    oracle("sc.pit.oracle.example_1.withholding", "SC", "Three allowances, weekly 750.00 (2026 tables, not Act 110)", [
        ("Annual wages", "750.00 × 52", m(ann)),
        ("Standard deduction (rate × wages, capped)", f"min({m(ann)} × {T('sc.pit.wh.std_deduction.rate')}%, {T('sc.pit.wh.std_deduction.cap')})", m(sdd)),
        ("Annual taxable wages", f"{m(ann)} − 3 × {T('sc.pit.allowance.annual')} − {m(sdd)}", m(ti)),
        ("Annual tax", f"{m(ti)} × {T('sc.pit.wh.band.3.rate')}% − {T('sc.pit.wh.band.3.subtract')}", m(tax)),
        ("Withholding", f"{m(tax)} ÷ 52", m(tax / 52, 4))], tax / 52)
    # ID single biweekly 1,212 (table from 2026-07-23), whole dollar
    on = "2026-08-01"
    w = (D(1212) - D(V("id.wh.zero_bracket.single.biweekly", on=on))) * D(V("id.pit.rate.flat")) / 100
    oracle("id.oracle.biweekly_1212_single.withholding", "ID", "Single, biweekly 1,212.00 (table from 2026-07-23); whole dollar", [
        ("Withholding before rounding", f"(1,212.00 − {T('id.wh.zero_bracket.single.biweekly', on=on)}) × {T('id.pit.rate.flat')}%", m(w, 4)),
        ("Rounded to the nearest dollar (" + T("id.wh.rounding") + ")", m(w, 4), m(c0(w), 0))], w, whole_dollar_key="id.wh.rounding")
    # KS weekly threshold, single
    w = D(V("ks.pit.std_deduction.single")) / 52
    oracle("ks.oracle.weekly_threshold_single.withholding", "KS", "Single, weekly per-period zero-bracket threshold; whole dollar", [
        ("Weekly threshold", f"{T('ks.pit.std_deduction.single')} ÷ 52", m(w, 4)),
        ("Rounded to the nearest dollar", m(w, 4), m(c0(w), 0))], w, whole_dollar_key="ks.wh.rounding")
    # HI single 3 allowances weekly 500
    ann = D(500) * 52
    ti = ann - 3 * D(V("hi.wh.allowance.annual")) - D(V("hi.wh.lump_sum_allowance.annual"))
    tax = D(V("hi.wh.bracket.single.3.base_tax")) + (ti - D(V("hi.wh.bracket.single.2.ceiling"))) * D(V("hi.wh.bracket.single.3.rate")) / 100
    oracle("hi.oracle.weekly_500_s3.withholding", "HI", "Single, three allowances, weekly 500.00", [
        ("Annual taxable wages", f"500.00 × 52 − 3 × {T('hi.wh.allowance.annual')} − {T('hi.wh.lump_sum_allowance.annual')}", m(ti)),
        ("Annual tax", f"{T('hi.wh.bracket.single.3.base_tax')} + ({m(ti)} − {T('hi.wh.bracket.single.2.ceiling')}) × {T('hi.wh.bracket.single.3.rate')}%", m(tax)),
        ("Withholding", f"{m(tax)} ÷ 52", m(tax / 52, 4))], tax / 52)
    # MS single, zero exemptions, weekly 460
    on = "2026-06-01"
    ti = D(460) * 52 - D(V("ms.pit.std_deduction.single"))
    tax = (ti - D(V("ms.pit.rate.zero_band.ceiling"))) * D(V("ms.pit.rate.flat", on=on)) / 100
    oracle("ms.oracle.weekly_460_0ex.withholding", "MS", "Single, zero exemptions, weekly 460.00 (formula, before the table's whole-dollar rounding)", [
        ("Annual taxable income", f"460.00 × 52 − {T('ms.pit.std_deduction.single')}", m(ti)),
        ("Annual tax", f"({m(ti)} − {T('ms.pit.rate.zero_band.ceiling')}) × {T('ms.pit.rate.flat', on=on)}%", m(tax)),
        ("Withholding", f"{m(tax)} ÷ 52", m(tax / 52, 4))], tax / 52)
    # RI weekly 2,195, one exemption
    taxable_w = D(2195) - D(V("ri.pit.exemption.annual")) / 52
    ann = taxable_w * 52
    tax = D(V("ri.pit.bracket.2.base_tax")) + (ann - D(V("ri.pit.bracket.1.ceiling"))) * D(V("ri.pit.bracket.2.rate")) / 100
    oracle("ri.oracle.weekly_2195.withholding", "RI", "One exemption, weekly 2,195.00", [
        ("Weekly taxable wages", f"2,195.00 − {T('ri.pit.exemption.annual')} ÷ 52", m(taxable_w, 4)),
        ("Annual tax", f"{T('ri.pit.bracket.2.base_tax')} + ({m(taxable_w, 4)} × 52 − {T('ri.pit.bracket.1.ceiling')}) × {T('ri.pit.bracket.2.rate')}%", m(tax, 4)),
        ("Withholding", f"{m(tax, 4)} ÷ 52", m(tax / 52, 4))], tax / 52)
    # CA DE 44 Method B example F: married, 4 allowances, monthly 4,750 (annual 57,000)
    ann = D(57000)
    sd = D(V("ca.wh.std_deduction.married_2plus_hoh"))
    ti = ann - sd
    rate1 = D(V("ca.pit.bracket.single.1.rate"))
    rate2 = D(V("ca.pit.bracket.single.2.rate"))
    c1 = D(V("ca.pit.brackets.married.ceilings").split("/")[0].strip().replace(",", ""))
    tax0 = c2(c1 * rate1 / 100) + (ti - c1) * rate2 / 100
    credit = 4 * D(V("ca.wh.allowance_credit.per_allowance"))
    tax = tax0 - credit
    oracle("ca.oracle.de44_f.monthly.withholding", "CA", "DE 44 Method B example F: married, annual wages 57,000.00, four allowances, monthly", [
        ("Married bracket ceilings (DE 44 Rev. 52)", T("ca.pit.brackets.married.ceilings"), "—"),
        ("Taxable income", f"57,000.00 − {T('ca.wh.std_deduction.married_2plus_hoh')}", m(ti)),
        ("Tax on the first married bracket", f"{m(c1)} × {T('ca.pit.bracket.single.1.rate')}%", m(c2(c1 * rate1 / 100))),
        ("Computed annual tax", f"{m(c2(c1 * rate1 / 100))} + ({m(ti)} − {m(c1)}) × {T('ca.pit.bracket.single.2.rate')}%", m(tax0)),
        ("Exemption allowance credit (4)", f"4 × {T('ca.wh.allowance_credit.per_allowance')}", m(credit)),
        ("Annual withholding", f"{m(tax0)} − {m(credit)}", m(tax)),
        ("Monthly withholding", f"{m(tax)} ÷ 12", m(tax / 12, 4))], tax / 12)
    # AR monthly 2,127, two exemptions
    ann = D(2127) * 12
    ni = ann - D(V("ar.wh.std_deduction"))
    mid = (ni // 100) * 100 + 50
    t1 = mid * D(V("ar.pit.bracket.4.rate")) / 100 - D(V("ar.pit.bracket.4.subtract"))
    t2 = c0(t1) - 2 * D(V("ar.wh.personal_credit.per_exemption"))
    oracle("ar.oracle.example.1.withholding", "AR", "Two exemptions, monthly 2,127.00", [
        ("Annual net taxable income", f"2,127.00 × 12 − {T('ar.wh.std_deduction')}", m(ni)),
        ("Band midpoint (USD 50, per " + T("ar.wh.method") + ")", m(ni), m(mid)),
        ("Annual tax before credits", f"{m(mid)} × {T('ar.pit.bracket.4.rate')}% − {T('ar.pit.bracket.4.subtract')}", m(t1)),
        ("Annual tax rounded to the dollar, less credits (2)", f"{m(c0(t1), 0)} − 2 × {T('ar.wh.personal_credit.per_exemption')}", m(t2)),
        ("Monthly withholding", f"{m(t2)} ÷ 12", m(t2 / 12, 4))], t2 / 12)


ORACLE_TEXT = {
    "quoted from authority page": "quoted",
    "derived arithmetically": "derived by the Stage 5 worker",
}


def m12():
    L = []
    F.set_loc("m12_worked_examples.md §12.1 header")
    L += ["# Module 12: Gross-to-Net Worked Examples", "",
          "*Purpose: To provide a final, comprehensive validation of all researched rules.*", "",
          "## 12.1 Comprehensive Gross-to-Net Examples", "",
          "### Provide complete, end-to-end Gross-to-Net calculation examples for common scenarios:", "",
          "**How these examples are produced.** Every figure below is computed by "
          "`01-ccg/_examples/build_examples.py` from the facts files; no number is typed by hand. "
          "Amounts are rounded half-up to the cent at each line. The optional whole-dollar rounding that "
          f"Pub. 15-T allows ({T('fed.fit.rounding')}) {F.REG('fed.fit.rounding')} is not applied, so the "
          "examples show the exact percentage-method result. Employees are on a 2020-or-later Form W-4 with "
          "Step 2 not checked and Steps 3 and 4 blank unless stated. The federal layer is shown in full. "
          "State and local withholding is shown where the example's work State levies it; "
          "per-State figures live in the jurisdiction annexes.", ""]
    # A
    sc = SCENARIOS["A"]
    loc = "m12_worked_examples.md §12.1 A full-time resident employee on a standard salary"
    F.set_loc(loc)
    hA = "Worked example 1: Scenario A, full-time resident employee (biweekly)"
    RESULTS.setdefault("_headings", {})["A"] = hA   # r3 (QA r2 C69): headings the C69 checker counts
    L += ["### A full-time resident employee on a standard salary", "", "#### " + hA, "",
          f"**Scenario A: {sc['title']}.** Single filer, biweekly salary 3,000.00, first pay of 2026. "
          f"Work and residence State Texas, which levies no wage income tax ({F.B('tx.no_wage_tax', 'no state income tax withholding', 'state withholding applies')}, "
          f"{F.REG('tx.no_wage_tax')}). Employer State unemployment insurance is paid at the employer's assigned Texas rate on the Texas wage base "
          "(Annex TX). It is employer-specific, so it is not computed here.", ""]
    L += gross_to_net("A", sc, sc["wage"], loc)
    L += [""]
    # B
    sc = SCENARIOS["B"]
    loc = "m12_worked_examples.md §12.1 A casual or part-time employee"
    F.set_loc(loc)
    rate = D(V("fed.minwage.hourly"))
    wage = c2(rate * sc["hours"])
    hB = "Worked example 2: Scenario B, part-time employee at the federal minimum wage"
    RESULTS.setdefault("_headings", {})["B"] = hB
    L += ["### A casual or part-time employee", "", "#### " + hB, "",
          f"**Scenario B: {sc['title']}.** Single filer, {sc['hours']} hours in the workweek at the federal minimum wage of "
          f"{T('fed.minwage.hourly')} per hour {F.REG('fed.minwage.hourly')}. No overtime: the hours are below the "
          f"{T('fed.overtime.weekly_threshold_hours')}-hour weekly threshold {F.REG('fed.overtime.weekly_threshold_hours')}. "
          "Work State without a wage income tax. A higher State or local minimum wage displaces the federal one "
          f"({T('multi.wage_hour.overlay_rule')}) {F.REG('multi.wage_hour.overlay_rule')}.", "",
          table(["Line", "Calculation", "Result (USD)"], [("Gross weekly pay", f"{sc['hours']} × {T('fed.minwage.hourly')}", m(wage))]), ""]
    L += gross_to_net("B", sc, wage, loc)
    L += ["", "The adjusted annual wage falls in the 0 % row of the STANDARD Single schedule, so no federal income tax "
          "is withheld. FICA is still due from the first dollar.", ""]
    # pre-tax
    F.set_loc("m12_worked_examples.md §12.1 An employee with a pre-tax deduction")
    L += ["### An employee with a pre-tax deduction", "",
          "The 2026 limits for the main pre-tax plans are facts: 401(k) elective deferral "
          f"{T('fed.retirement.401k.elective_deferral_limit')}, catch-up at age 50 {T('fed.retirement.401k.catch_up_50')}, "
          f"catch-up at ages 60 to 63 {T('fed.retirement.401k.catch_up_60_63')} {F.REG('fed.retirement.401k.elective_deferral_limit')}; "
          f"HSA {T('fed.hsa.limit.self_only')} self-only and {T('fed.hsa.limit.family')} family {F.REG('fed.hsa.limit.self_only')}; "
          f"health FSA salary reduction {T('fed.bik.health_fsa.salary_reduction_cap')} {F.REG('fed.bik.health_fsa.salary_reduction_cap')}. "
          "California taxes 401(k) deferrals for UI and SDI but not for personal income tax "
          f"({T('ca.wages.401k_deferrals')}) {F.REG('ca.wages.401k_deferrals')}.", "",
          F.gap("the facts files carry no key stating how a 401(k) elective deferral or a cafeteria-plan salary reduction "
                "is treated for federal income tax withholding, OASDI/Medicare and FUTA wages. A computed pre-tax "
                "gross-to-net example cannot be written without it.", "fed.retirement.401k.wage_treatment"), ""]
    # student loan / special
    F.set_loc("m12_worked_examples.md §12.1 An employee with a student loan or other special tax obligation")
    L += ["### An employee with a student loan or other special tax obligation", "",
          F.gap("no fact describes a federal or State payroll obligation for student-loan repayment "
                "(for example an administrative wage garnishment order). The case is not computed.",
                "fed.student_loan.payroll_obligation"), "",
          "#### Worked example 3: Supplemental payment above the mandatory threshold", "",
          "**Special tax obligation computed instead: a supplemental payment above the mandatory threshold.** "
          f"Supplemental wages paid to one employee in excess of {T('fed.fit.supplemental.mandatory_threshold')} in the calendar year "
          f"are withheld at the mandatory rate of {T('fed.fit.supplemental.mandatory_rate')}% {F.REG('fed.fit.supplemental.mandatory_rate')}. "
          "Scenario: the employee has already received 1,000,000.00 of supplemental wages in 2026 and OASDI wages above the base. "
          "A further bonus of 50,000.00 is paid.", ""]
    loc = "m12_worked_examples.md §12.1 special tax obligation (mandatory supplemental)"
    F.set_loc(loc)
    bonus = D(50000)
    fit = c2(bonus * D(V("fed.fit.supplemental.mandatory_rate")) / 100)
    med = c2(bonus * D(V("fed.fica.medicare.rate.employee")) / 100)
    addl = c2(bonus * D(V("fed.fica.addl_medicare.rate")) / 100)
    net = bonus - fit - med - addl
    L += [table(["Line", "Calculation", "Result (USD)"], [
        ("Bonus (all above the mandatory threshold)", "—", m(bonus)),
        ("FIT at the mandatory rate", f"{m(bonus)} × {pct('fed.fit.supplemental.mandatory_rate')}", m(fit)),
        ("OASDI (annual wage base already reached)", "—", "0.00"),
        ("Medicare employee", f"{m(bonus)} × {pct('fed.fica.medicare.rate.employee')}", m(med)),
        ("Additional Medicare (wages already above the threshold)", f"{m(bonus)} × {pct('fed.fica.addl_medicare.rate')}", m(addl)),
        ("Net payment", f"{m(bonus)} − {m(fit)} − {m(med)} − {m(addl)}", m(net))]), ""]
    RESULTS["D_mandatory_supplemental"] = dict(fit=str(fit), medicare=str(med), addl=str(addl), net=str(c2(net)))
    RESULTS.setdefault("_headings", {})["D_mandatory_supplemental"] = "Worked example 3: Supplemental payment above the mandatory threshold"
    # C
    sc = SCENARIOS["C"]
    loc = "m12_worked_examples.md §12.1 Other complex scenarios that are common in the country"
    F.set_loc(loc)
    hC = "Worked example 4: Scenario C, OASDI wage base and Additional Medicare threshold (semimonthly)"
    RESULTS.setdefault("_headings", {})["C"] = hC
    L += ["### Other complex scenarios that are common in the country", "", "#### " + hC, "",
          f"**Scenario C: {sc['title']}.** Single filer, semimonthly salary 20,000.00, wages already paid in 2026 by this employer "
          "182,000.00. The OASDI contribution is the rate × the lesser of the remaining annual wage base and the pay "
          f"(base {T('fed.fica.oasdi.wage_base', ef='2026-01-01')} for 2026, {F.REG('fed.fica.oasdi.wage_base', ef='2026-01-01')}). "
          "The Additional Medicare tax applies only to the part of the cumulative wages above the threshold. "
          "The figures are never annualised and then divided.", ""]
    L += gross_to_net("C", sc, sc["wage"], loc)
    L += [""]
    # oracle collection
    loc = "m12_worked_examples.md §12.2 Oracle collection"
    F.set_loc(loc)
    state_oracles(loc)
    F.set_loc(loc)
    L += ["## 12.2 Oracle Collection: Published and Re-derived Withholding Examples", "",
          "The build manifest names the oracle: IRS Pub. 15-T (2026) for the federal layer, and the worked examples "
          f"published by each State {F.REG('fed.oracle.source')}. The IRS Tax Withholding Estimator is not an oracle "
          f"({T('fed.oracle.estimator_not_oracle')}) {F.REG('fed.oracle.estimator_not_oracle')}. "
          "Table 12.2.1 lists every example held as a fact. Each row gives its register id, how the result was obtained "
          "and any residual. Table 12.2.2 recomputes from keyed facts each example whose inputs are all keyed.", "",
          "### 12.2.1 Oracle register", ""]
    m12f = json.load(open(os.path.join(F.RESEARCH, "CCG-m12_worked_examples-facts.json"), encoding="utf-8"))
    rec = {o[0]: o for o in ORACLES}
    rows = []
    for k in ("fed.oracle.pub15t.nra_example.withholding", "fed.oracle.pub15t.tribal_example.withholding"):
        e = F.entry(k)
        note = ("Pub. 15-T wage-bracket result for weekly wages " + T("fed.oracle.pub15t.nra_example.wages") +
                " (300.00 plus the Table 1 add-on " + T("fed.fit.nra.addon.table1.weekly") + "). Not re-derived here: "
                "the example's filing status and allowance count are not keyed."
                if "nra" in k else
                "Tribal gaming monthly payment " + T("fed.oracle.pub15t.tribal_example.payment") +
                ". Tribal gaming tables are not keyed, so it is not re-derived here.")
        rows.append(("FED", k.split(".")[3], T(k), e["register_id"], "quoted", note))
    for f in m12f["facts"]:
        k = f["key"]
        jur = k.split(".")[0].upper()
        o = rec.get(k)
        how = ORACLE_TEXT.get(f["verification_method"], f["verification_method"])
        if o:
            resid = "Recomputed in 12.2.2: " + ("agrees" if o[6] else "DISAGREES")
        else:
            resid = "Not recomputed here: scenario inputs not all keyed (see the annex)."
        if k == "nd.oracle.section2_booklet.withholding":
            resid = ("Booklet defect: the booklet prints this figure while its own table gives a lower amount; "
                     "the oracle uses the table, not the printed example. Never use this row as an expected result.")
        if k.startswith("ct.oracle."):
            resid = ("Table route. The DRS rules route (TPG-211) gives a different figure for the same case; the engine "
                     f"must choose one method (Module 13, 13.1) {F.REG('practice.ct.tables_vs_rules')}.")
        if k == "or.oracle.annual_25000.withholding":
            resid = "Worker re-derivation; the published example is mis-computed (" + T("practice.or.federal_cap") + ")."
        if k == "ia.oracle.formula.example6.withholding":
            resid = "The published example has no final figure; worker derivation. Dependent count not keyed."
        if k == "mi.oracle.biweekly_2000_1ex.withholding":
            resid += " The Treasury withholding calculator (official oracle) was not run."
        if k == "sc.pit.oracle.example_1.withholding":
            resid += " 2026 withholding tables, not the Act 110 return rates (" + T("practice.sc.withholding_rates_2026") + ")."
        rows.append((jur, k.split(".", 2)[2].replace(".withholding", ""), T(k) + F.dated(k), f["register_id"], how, resid))
    L += [table(["Jurisdiction", "Case", "Result (USD)", "Register", "How obtained", "Status / residual"], rows), ""]
    L += ["**Residuals carried as open items (not facts, not expected results):**", ""]
    for uk in ("ny.oracle.nys50t.example2.withholding", "ky.oracle.biweekly_1500.withholding",
               "ut.oracle.pub14.examples.withholding", "dc.oracle.method_2026", "md.oracle.calculator"):
        u = F.UNRESOLVED[uk]
        L.append(f"- **{uk.split('.')[0].upper()}**: " + F.gap(_residual_text(uk), uk))
    L += [""]
    L += ["### 12.2.2 Re-derivation from keyed facts", "",
          "Each table recomputes one oracle from the keyed rates, deductions and brackets. The scenario inputs "
          "(wages, frequency, filing status, allowances) are those of the published example. Results are shown to "
          "four decimals before rounding. The last column of 12.2.1 records agreement with the oracle fact at the cent "
          "(at the dollar where the State rounds withholding to whole dollars).", ""]
    for n_ex, (okey, jur, case, rws, comp, wd, ok) in enumerate(ORACLES, start=5):
        F.set_loc(f"m12_worked_examples.md §12.2.2 {jur}")
        h_ex = f"Worked example {n_ex}: {jur} published example re-derived"
        RESULTS.setdefault("_headings", {})[okey] = h_ex
        L += ["#### " + h_ex, ""]
        if D(m(comp, 4).replace(",", "")) == D(V(okey)):
            lab, calc, _r = rws[-1]
            rws = rws[:-1] + [(lab, calc, T(okey))]
        L += [f"**{jur}: {case}** {F.REG(okey)}. Oracle fact {T(okey)}.", "",
              table(["Line", "Calculation", "Result (USD)"], rws), ""]
        RESULTS[okey] = dict(computed=str(m(comp, 4)), fact=str(V(okey)), agrees=ok)
    return L


def _residual_text(uk):
    return {
        "ny.oracle.nys50t.example2.withholding": "NYS-50-T-NYS Method II example 2: the booklet's printed figures differ by one cent "
            "from half-up arithmetic, and the booklet states no rounding rule. Examples 1, 3 and 4 reproduce. Needs the DTF "
            "rounding convention or a DTF calculator result.",
        "ky.oracle.biweekly_1500.withholding": "Kentucky 2026 formula sheet: the per-period result is printed without a stated "
            "rounding rule, and one intermediate figure is misprinted. Needs DOR KY confirmation of the per-period rounding.",
        "ut.oracle.pub14.examples.withholding": "Utah Pub. 14 (Rev. 04/26): six examples reproduce, but the publication's "
            "effective date is not established, so they are not dated facts. Needs the Tax Commission's statement of the effective date.",
        "dc.oracle.method_2026": "District of Columbia: no 2026 withholding method is published. An emergency act revoked "
            "personal exemptions and the D-4 is under review. Needs the OTR 2026 withholding instructions or the "
            "permanent act.",
        "md.oracle.calculator": "Maryland: the official oracle is the Comptroller's withholding calculator, which was not run. "
            "Needs one calculator run for a fixed case.",
    }[uk]


def m09_examples():
    loc = "m09_termination.md §9.1 redundancy worked example"
    F.set_loc(loc)
    L = ["**Scenario.** An employee whose position is eliminated receives severance pay of 18,000.00 in a separate payment, "
         "after 60,000.00 of 2026 wages from this employer. Severance is wages for FIT, FICA and FUTA "
         f"{F.REG('fed.severance.is_wages')}. Paid separately, it is withheld as supplemental wages at the optional flat rate. "
         "FUTA is already exhausted for the year at this wage level. State withholding and final-pay timing follow the work State (Table 9.1.1). "
         "Alabama, for example, exempts severance up to "
         f"{T('al.wh.severance.exempt_max')} from its withholding {F.REG('al.wh.severance.exempt_max')}.", ""]
    L += supplemental_example("m09_redundancy", loc, 18000, 60000, "Redundancy severance payout (federal layer)")
    open(os.path.join(OUT, "m09_redundancy.md"), "w", encoding="utf-8").write(F.clean("\n".join(L) + "\n"))
    loc = "m09_termination.md §9.2 bonus worked example"
    F.set_loc(loc)
    L = ["**Scenario.** An annual bonus of 5,000.00 is paid on its own check to an employee with 40,000.00 of 2026 wages. "
         "Supplemental wages identified separately from regular wages may be withheld at the optional flat rate "
         f"{F.REG('fed.fit.supplemental.flat_rate')}. FICA applies in full.", ""]
    L += supplemental_example("m09_bonus", loc, 5000, 40000, "Annual bonus, optional flat-rate method (federal layer)")
    open(os.path.join(OUT, "m09_bonus.md"), "w", encoding="utf-8").write(F.clean("\n".join(L) + "\n"))


def main():
    m09_examples()
    L = m12()
    open(os.path.join(MOD, "m12_worked_examples.md"), "w", encoding="utf-8").write(
        F.CC.finalize("m12_worked_examples.md", F.clean("\n".join(L) + "\n")))
    json.dump(RESULTS, open(os.path.join(OUT, "results.json"), "w", encoding="utf-8"), indent=1)
    json.dump([list(b) for b in F.BINDINGS], open(os.path.join(OUT, "bindings_examples.json"), "w", encoding="utf-8"), indent=0)
    json.dump([list(g) for g in F.GAPS], open(os.path.join(OUT, "gaps_examples.json"), "w", encoding="utf-8"), indent=0)
    print(f"oracles recomputed {len(ORACLES)}, disagreements {len(FAILS)}")
    for f in FAILS:
        print("  DISAGREE", f)
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())

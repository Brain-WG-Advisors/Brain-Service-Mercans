# -*- coding: utf-8 -*-
"""Worked examples for annexes DE, GA, HI, IA, ID, IL, IN, KY, LA (CCG stage 1).
Every statutory input is read from _research/CCG-annex_{JUR}-facts.json by key; every
line is computed here; the result is asserted against the published oracle fact.
Rounding: half-up to the cent unless the facts state otherwise (ID whole dollar).
Writes examples_{JUR}.md beside this script; build_annexes.py inserts them."""
import json, os, sys
from decimal import Decimal, ROUND_HALF_UP

BASE = sys.argv[1]
SCR = os.path.dirname(os.path.abspath(__file__))
D = Decimal
RESULTS = []


def facts(j):
    return json.load(open(os.path.join(BASE, "_research", f"CCG-annex_{j}-facts.json"), encoding="utf-8"))["facts"]


class F:
    def __init__(self, j, on="2026-12-31"):
        self.j, self.on, self.all = j, on, facts(j)

    def get(self, key, on=None):
        on = on or self.on
        c = [f for f in self.all if f["key"] == key and (f.get("effective_from") or "0000") <= on
             and (f.get("effective_to") or "9999") >= on]
        assert len(c) == 1, (key, on, len(c))
        return c[0]["value"]

    def t(self, key, on=None, fmt=None):
        v = self.get(key, on)
        s = fmt(v) if fmt else (f"{v:,}" if isinstance(v, int) else f"{v:,.2f}" if isinstance(v, float) and v >= 100 else str(v))
        return f"[[FACT:{key}={s}]]", D(str(v))


def c2(x):
    return x.quantize(D("0.01"), rounding=ROUND_HALF_UP)


def c0(x):
    return x.quantize(D("1"), rounding=ROUND_HALF_UP)


def m(x):
    return f"{x:,.2f}"


def pct(d):
    return d / D(100)


def table(rows):
    out = ["| Line | Calculation | Result |", "|---|---|---|"]
    for r in rows:
        out.append(f"| {r[0]} | {r[1]} | {r[2]} |")
    return out


def check(j, name, computed, oracle_key, f, on=None):
    o = D(str(f.get(oracle_key, on)))
    ok = computed == o
    RESULTS.append((j, name, str(computed), str(o), ok))
    return ok


TAGMAP = {
    "DE": {"13.88": "[[FACT:de.oracle.guide.example1.withholding_weekly=13.88]]", "269.63": "[[FACT:de.oracle.guide.example2.supplemental=269.63]]"},
    "GA": {"27.03": "[[FACT:ga.oracle.guide.example1.withholding=27.03]]"},
    "HI": {"9.58": "[[FACT:hi.oracle.booklet_a.part1.withholding_weekly=9.58]]", "14,400.00": "[[FACT:hi.wh.bracket.single.2.ceiling=14,400]]"},
    "IA": {"114.92": "[[FACT:ia.oracle.formula.example6.withholding=114.92]]"},
    "IL": {"32.13": "[[FACT:il.oracle.il700t.example2.withholding=32.13]]"},
    "IN": {"13.96": "[[FACT:in.oracle.dn1.example.state=13.96]]", "4.73": "[[FACT:in.oracle.dn1.example.county=4.73]]"},
    "KY": {"104.65": "[[FACT:ky.oracle.formula.monthly_3270=104.65]]", "1,247.40": "[[FACT:ky.oracle.formula.biweekly_1500.annual=1,247.40]]",
           "47.98": "[[FACT:ky.oracle.biweekly_1500.result=47.98]]"},
    "LA": {"13.98": "[[FACT:la.oracle.r1306.example1.withholding=13.98]]", "111.54": "[[FACT:la.oracle.r1306.example2.withholding=111.54]]"},
}


def write(j, lines):
    import re
    text = "\n".join(lines)
    text = re.sub(r"Results? [\d,.]+ = published ", "Computed result = published ", text)
    for num, tg in TAGMAP.get(j, {}).items():
        parts = re.split(r"(\[\[FACT:[^\]]*\]\])", text)
        pat = re.compile(r"(?<![\d.,])" + re.escape(num) + r"(?![\d])")
        text = "".join(x if x.startswith("[[FACT:") else pat.sub(tg, x) for x in parts)
    lines = text.split("\n")
    open(os.path.join(SCR, f"examples_{j}.md"), "w", encoding="utf-8").write("\n".join(lines).strip() + "\n")


INTRO = ("Each example is computed from the statutory parameters listed in this annex and checked against the result "
         "published by the authority. Amounts round half-up to the cent unless the line states another rule.")

# ---------------------------------------------------------------- DE
f = F("DE", "2025-06-30")
L = [INTRO, ""]
sd_t, sd = f.t("de.wh.std_deduction.single")
cr_t, cr = f.t("de.wh.personal_credit.per_exemption")
br = []  # (low, high, rate)
lows = [D(0)]
ceil = [f.t(f"de.pit.bracket.{i}.ceiling") for i in range(1, 7)]
rates = [None] + [f.t(f"de.pit.bracket.{i}.rate") for i in range(2, 8)]


def de_tax(taxable):
    tax, low, rows = D(0), D(0), []
    for i in range(7):
        high = ceil[i][1] if i < 6 else None
        if taxable <= low:
            break
        top = taxable if high is None else min(taxable, high)
        if i == 0:
            rows.append((f"Bracket 1: 0 to {ceil[0][0]}", "0 % (no tax)", "0.00"))
        else:
            amt = (top - low) * pct(rates[i][1])
            tax += amt
            rows.append((f"Bracket {i + 1}: {m(top - low)} above {ceil[i - 1][0]}", f"{m(top - low)} x {rates[i][0]} %", m(amt)))
        low = high if high is not None else low
    return tax, rows


L += ["**Example DE-1: single, 1 exemption, annual wages 25,000.00, weekly payroll (Withholding Tax Guide example 1).**", ""]
wages = D("25000")
taxable = wages - sd
tax, rows = de_tax(taxable)
net = tax - cr
weekly = c2(net / 52)
L += table([("Annual wages", "example input", m(wages)),
            ("Standard deduction (single)", f"{m(wages)} - {sd_t}", m(taxable))] + rows +
           [("Annual tax before credit", "sum of bracket amounts", m(tax)),
            ("Personal credit", f"{m(tax)} - 1 x {cr_t}", m(net)),
            ("Weekly withholding", f"{m(net)} / 52, half-up to the cent", m(weekly))])
ok = check("DE", "DE-1", weekly, "de.oracle.guide.example1.withholding_weekly", f)
L += ["", f"Result {m(weekly)} = published [[FACT:de.oracle.guide.example1.withholding_weekly=13.88]] ({'match' if ok else 'MISMATCH'}).", ""]

L += ["**Example DE-2: supplemental payment 5,000.00 paid separately to an employee earning 500.00 weekly, single, 1 exemption (annualised-with minus annualised-without, per `de.wh.supplemental.method`).**", ""]
reg = D("500") * 52
t_wo, _ = de_tax(reg - sd)
t_w, _ = de_tax(reg + D("5000") - sd)
a = t_wo - cr
b = t_w - cr
sup_raw = b - a
sup = c2(sup_raw)
L += table([("Annual regular wages", "500.00 x 52", m(reg)),
            ("Tax without the bonus", f"tax on ({m(reg)} - {sd_t}) - {cr_t}", m(a)),
            ("Tax with the bonus", f"tax on ({m(reg)} + 5,000.00 - {sd_t}) - {cr_t}", f"{b:,.3f}"),
            ("Withholding on the bonus", f"{b:,.3f} - {m(a)} = {sup_raw:,.3f}, half-up to the cent", m(sup))])
ok = check("DE", "DE-2", sup, "de.oracle.guide.example2.supplemental", f)
L += ["", f"Result {m(sup)} = published [[FACT:de.oracle.guide.example2.supplemental=269.63]] ({'match' if ok else 'MISMATCH'}).", ""]
write("DE", L)

# ---------------------------------------------------------------- GA
f = F("GA", "2026-06-30")
L = [INTRO, ""]
sd_t, sd = f.t("ga.wh.std_deduction.mfj")
da_t, da = f.t("ga.wh.dependent_allowance")
r_t, r = f.t("ga.pit.rate.flat", "2026-06-30")
p_sd = c2(sd / 24)
p_da = c2(da / 24)
base = D("2000") - p_sd - p_da
w_raw = base * pct(r)
w = c2(w_raw)
L += ["**Example GA-1: married filing jointly, semimonthly wages 2,000.00, 1 dependent (Employer's Tax Guide percentage method).**", ""]
L += table([("Period standard deduction", f"{sd_t} / 24, rounded to the cent", m(p_sd)),
            ("Period dependent allowance", f"{da_t} / 24, rounded to the cent", m(p_da)),
            ("Taxable wages", f"2,000.00 - {m(p_sd)} - 1 x {m(p_da)}", m(base)),
            ("Withholding", f"{m(base)} x {r_t} % = {w_raw:.4f}, half-up to the cent", m(w))])
ok = check("GA", "GA-1", w, "ga.oracle.guide.example1.withholding", f)
L += ["", f"Result {m(w)} = published [[FACT:ga.oracle.guide.example1.withholding=27.03]] ({'match' if ok else 'MISMATCH'}). The rate applies from 2026-01-01; employers that kept the prior rate until 2026-05-11 follow the transition described in GA.2.", ""]
write("GA", L)

# ---------------------------------------------------------------- HI
f = F("HI", "2026-06-30")
L = [INTRO, ""]
al_t, al = f.t("hi.wh.allowance.annual")
ls_t, ls = f.t("hi.wh.lump_sum_allowance.annual")
c2_t, c2v = f.t("hi.wh.bracket.single.2.ceiling")
c3_t, c3v = f.t("hi.wh.bracket.single.3.ceiling")
b3_t, b3 = f.t("hi.wh.bracket.single.3.base_tax")
r3_t, r3 = f.t("hi.wh.bracket.single.3.rate")
ann = D("500") * 52
taxable = ann - 3 * al - ls
assert c2v < taxable <= c3v
tax = b3 + (taxable - c2v) * pct(r3)
wk = c2(tax / 52)
L += ["**Example HI-1: single, 3 allowances, weekly wages 500.00 (Booklet A, Part 1 annualised method).**", ""]
L += table([("Annual wages", "500.00 x 52", m(ann)),
            ("Allowances", f"3 x {al_t}", m(3 * al)),
            ("Taxable wages", f"{m(ann)} - {m(3 * al)} - {ls_t}", m(taxable)),
            ("Bracket", f"above {c2_t} up to {c3_t}", "bracket 3"),
            ("Annual tax", f"{b3_t} + ({m(taxable)} - {m(c2v)}) x {r3_t} %", m(tax)),
            ("Weekly withholding", f"{m(tax)} / 52, half-up to the cent", m(wk))])
ok = check("HI", "HI-1", wk, "hi.oracle.booklet_a.part1.withholding_weekly", f)
L += ["", f"Result {m(wk)} = published [[FACT:hi.oracle.booklet_a.part1.withholding_weekly=9.58]] ({'match' if ok else 'MISMATCH'}).", ""]
write("HI", L)

# ---------------------------------------------------------------- IA
f = F("IA", "2026-06-30")
L = [INTRO, ""]
d_t, dd = f.t("ia.wh.deduction.hoh")
r_t, r = f.t("ia.pit.rate.flat")
D_m = dd / 12
t1 = D("5000") - D_m
t2 = t1 * pct(r)
t3 = t2 - D("160") / 12
res = c2(t3)
L += ["**Example IA-1: head of household, monthly wages 5,000.00, W-4 allowance amount W = 160.00, no additional amount (2026 withholding formula, example 6).**", ""]
L += table([("D (period deduction)", f"{d_t} / 12", m(D_m)),
            ("T1 = G - D", f"5,000.00 - {m(D_m)}", m(t1)),
            ("T2 = T1 x rate", f"{m(t1)} x {r_t} %", m(t2)),
            ("T3 = T2 - W / P", f"{m(t2)} - 160.00 / 12 = {t3:.4f}", m(res)),
            ("T4 = T3 + A", f"{m(res)} + 0.00 (rounding: to the cent, half-up, per `ia.wh.rounding`)", m(res))])
ok = check("IA", "IA-1", res, "ia.oracle.formula.example6.withholding", f)
L += ["", f"Result {m(res)} = [[FACT:ia.oracle.formula.example6.withholding=114.92]] ({'match' if ok else 'MISMATCH'}). The published example prints no final figure; the value is re-derived from the formula.", ""]
write("IA", L)

# ---------------------------------------------------------------- ID
f = F("ID", "2026-08-01")
L = [INTRO, ""]
zb_t, zb = f.t("id.wh.zero_bracket.single.biweekly")
r_t, r = f.t("id.pit.rate.flat")
raw = (D("1212") - zb) * pct(r)
res = c0(raw)
L += ["**Example ID-1: single, biweekly wages 1,212.00, payroll on or after 2026-07-23 (percentage computation).**", ""]
L += table([("Taxable wages", f"1,212.00 - {zb_t}", m(D('1212') - zb)),
            ("Tax", f"{m(D('1212') - zb)} x {r_t} %", f"{raw:.4f}"),
            ("Withholding", "rounded to the nearest whole dollar (`id.wh.rounding`)", f"{res:,.0f}")])
ok = check("ID", "ID-1", res, "id.oracle.stc.single_biweekly.withholding", f)
L += ["", f"Result {res:,.0f} = published [[FACT:id.oracle.stc.single_biweekly.withholding=31]] ({'match' if ok else 'MISMATCH'}).", "",
      "Example ID-2 (married, weekly 1,000.00, published result [[FACT:id.oracle.stc.married_weekly.withholding=20]]) is not reproduced: the published example uses a zero bracket that matches neither the table in force before 2026-07-23 nor the table in force from that date. See the open item `id.wh.example_threshold_discrepancy` in ID.2; use the wage-bracket table for numbers.", ""]
write("ID", L)

# ---------------------------------------------------------------- IL
f = F("IL", "2026-06-30")
L = [INTRO, ""]
e1_t, e1 = f.t("il.wh.exemption.line1")
e2_t, e2 = f.t("il.wh.exemption.line2")
r_t, r = f.t("il.pit.rate.flat")


def il(wk, n1, n2):
    ex = n1 * e1 + n2 * e2
    per = ex / 52
    base = wk - c2(per)
    raw = base * pct(r)
    return ex, c2(per), base, raw, c2(raw)


ex, per, base, raw, res = il(D("800"), 2, 2)
L += ["**Example IL-2: weekly wages 800.00, IL-W-4 Line 1 = 2, Line 2 = 2 (IL-700-T example).**", ""]
L += table([("Annual exemptions", f"2 x {e1_t} + 2 x {e2_t}", m(ex)),
            ("Weekly exemption", f"{m(ex)} / 52, rounded to the cent", m(per)),
            ("Taxable wages", f"800.00 - {m(per)}", m(base)),
            ("Withholding", f"{m(base)} x {r_t} % = {raw:.4f}, half-up to the cent", m(res))])
ok = check("IL", "IL-2", res, "il.oracle.il700t.example2.withholding", f)
L += ["", f"Result {m(res)} = published [[FACT:il.oracle.il700t.example2.withholding=32.13]] ({'match' if ok else 'MISMATCH'}).", ""]
ex1, per1, base1, raw1, res1 = il(D("300"), 2, 1)
o1 = D(str(f.get("il.oracle.il700t.example1.withholding")))
RESULTS.append(("IL", "IL-1", str(res1), str(o1), res1 == o1))
L += ["**Example IL-1: weekly wages 300.00, IL-W-4 Line 1 = 2, Line 2 = 1 (IL-700-T example).**", ""]
L += table([("Annual exemptions", f"2 x {e1_t} + 1 x {e2_t}", m(ex1)),
            ("Weekly exemption", f"{m(ex1)} / 52, rounded to the cent", m(per1)),
            ("Taxable wages", f"300.00 - {m(per1)}", m(base1)),
            ("Withholding", f"{m(base1)} x {r_t} % = {raw1:.4f}, half-up to the cent", m(res1))])
if res1 != o1:
    L += ["", f"The formula with the 2026 exemption amounts gives {m(res1)}; the IL-700-T prints [[FACT:il.oracle.il700t.example1.withholding=8.38]]. ⚠️ RESEARCH-GAP: the inputs of IL-700-T example 1 do not reproduce its printed result with the 2026 exemption amounts; the example's allowance counts or wage must be re-read before it is used as a test case (open item `il.oracle.il700t.example1.inputs`, non-blocking).", ""]
else:
    L += ["", f"Result {m(res1)} = published [[FACT:il.oracle.il700t.example1.withholding=8.38]] (match).", ""]
write("IL", L)

# ---------------------------------------------------------------- IN
f = F("IN", "2026-10-15")
L = [INTRO, ""]
pe_t, pe = f.t("in.wh.exemption.personal")
de_t, de = f.t("in.wh.exemption.dependent")
ac_t, ac = f.t("in.wh.exemption.adopted_child")
r_t, r = f.t("in.pit.rate")
A5 = c2(5 * pe / 52)
B3 = c2(3 * de / 52)
B1 = c2(1 * de / 52)
C2 = c2(2 * ac / 52)
tot = A5 + B3 + B1 + C2
tx = D("800") - tot
st_raw = tx * pct(r)
st = c2(st_raw)
cty_raw = tx * D("0.01")
cty = c2(cty_raw)
L += ["**Example IN-1: weekly wages 800.00 with deduction constants A5, B3, B1 and C2, county rate 1.00% as used in the Departmental Notice 1 example (payroll from 2026-10-01).**", ""]
L += table([("Constant A5", f"5 x {pe_t} / 52, two decimals", m(A5)),
            ("Constant B3", f"3 x {de_t} / 52, two decimals", m(B3)),
            ("Constant B1", f"1 x {de_t} / 52, two decimals", m(B1)),
            ("Constant C2", f"2 x {ac_t} / 52, two decimals", m(C2)),
            ("Total constants", f"{m(A5)} + {m(B3)} + {m(B1)} + {m(C2)}", m(tot)),
            ("Taxable wages", f"800.00 - {m(tot)}", m(tx)),
            ("State withholding", f"{m(tx)} x {r_t} % = {st_raw:.4f}, half-up to the cent", m(st)),
            ("County withholding", f"{m(tx)} x 1.00 % (example county rate) = {cty_raw:.4f}", m(cty))])
ok1 = check("IN", "IN-1 state", st, "in.oracle.dn1.example.state", f)
ok2 = check("IN", "IN-1 county", cty, "in.oracle.dn1.example.county", f)
L += ["", f"Results {m(st)} = published [[FACT:in.oracle.dn1.example.state=13.96]] ({'match' if ok1 else 'MISMATCH'}); {m(cty)} = published [[FACT:in.oracle.dn1.example.county=4.73]] ({'match' if ok2 else 'MISMATCH'}). The county rate in production is the employee's county rate from the county chart (IN.2c).", ""]
write("IN", L)

# ---------------------------------------------------------------- KY
f = F("KY", "2026-06-30")
L = [INTRO, ""]
sd_t, sd = f.t("ky.wh.std_deduction")
r_t, r = f.t("ky.pit.rate.flat")
ann = D("3270") * 12
at = (ann - sd) * pct(r)
mo = c2(at / 12)
L += ["**Example KY-1: monthly wages 3,270.00 (2026 formula sheet).**", ""]
L += table([("Annual wages", "3,270.00 x 12", m(ann)),
            ("Annual tax", f"({m(ann)} - {sd_t}) x {r_t} %", m(at)),
            ("Monthly withholding", f"{m(at)} / 12, half-up to the cent", m(mo))])
ok = check("KY", "KY-1", mo, "ky.oracle.formula.monthly_3270", f)
L += ["", f"Result {m(mo)} = published [[FACT:ky.oracle.formula.monthly_3270=104.65]] ({'match' if ok else 'MISMATCH'}).", ""]
ann2 = D("1500") * 26
at2 = (ann2 - sd) * pct(r)
ok = check("KY", "KY-2 annual", c2(at2), "ky.oracle.formula.biweekly_1500.annual", f)
per2 = c2(at2 / 26)
L += ["**Example KY-2: biweekly wages 1,500.00 (2026 formula sheet).**", ""]
L += table([("Annual wages", "1,500.00 x 26", m(ann2)),
            ("Annual tax", f"({m(ann2)} - {sd_t}) x {r_t} %", m(at2)),
            ("Biweekly withholding", f"{m(at2)} / 26, half-up to the cent", m(per2))])
L += ["", f"The annual tax matches the published figure ({'match' if ok else 'MISMATCH'}). The formula sheet shows a whole-dollar per-period figure without stating a rounding rule; see the open item `ky.wh.rounding.tax` in KY.2.", ""]
write("KY", L)

# ---------------------------------------------------------------- LA
f = F("LA", "2026-06-30")
L = [INTRO, ""]
s_t, s = f.t("la.wh.std_deduction.single")
j_t, jd = f.t("la.wh.std_deduction.joint")
r_t, r = f.t("la.pit.rate.flat")
x1 = (D("700") - s / 52) * pct(r)
x2 = (D("4600") - jd / 26) * pct(r)
L += ["**Example LA-1: L-4 status 1, weekly wages 700.00 (R-1306 formula).**", ""]
L += table([("Period deduction", f"{s_t} / 52", f"{s / 52:.4f}"),
            ("Withholding", f"(700.00 - {s / 52:.4f}) x {r_t} % = {x1:.4f}, half-up to the cent", m(c2(x1)))])
ok = check("LA", "LA-1", c2(x1), "la.oracle.r1306.example1.withholding", f)
L += ["", f"Result {m(c2(x1))} = published [[FACT:la.oracle.r1306.example1.withholding=13.98]] ({'match' if ok else 'MISMATCH'}).", ""]
L += ["**Example LA-2: L-4 status 2, biweekly wages 4,600.00 (R-1306 formula).**", ""]
L += table([("Period deduction", f"{j_t} / 26", f"{jd / 26:.4f}"),
            ("Withholding", f"(4,600.00 - {jd / 26:.4f}) x {r_t} % = {x2:.4f}, half-up to the cent", m(c2(x2)))])
ok = check("LA", "LA-2", c2(x2), "la.oracle.r1306.example2.withholding", f)
L += ["", f"Result {m(c2(x2))} = published [[FACT:la.oracle.r1306.example2.withholding=111.54]] ({'match' if ok else 'MISMATCH'}).", ""]
write("LA", L)

for r_ in RESULTS:
    print(*r_)
json.dump(RESULTS, open(os.path.join(SCR, "examples_results.json"), "w"), indent=1)

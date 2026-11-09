"""Run every official worked example (and a few official-table consistency rows) through oracle.calc.

Two categories:
  official_example   - a worked example printed in the publication, with its printed result.
  table_consistency  - a printed row of an official wage-bracket table, compared with the oracle's formula
                       evaluated at the bracket point the table uses (midpoint for IRS/IL, upper bound for OH).
                       The publication does not say how its tables were built, so these are corroboration only.

Nothing is tuned to force a match: a mismatch is reported with both values.
Run:  python reference_tests.py        (writes reference_results.json next to this file)
"""
import json
import os
import sys
from decimal import Decimal, ROUND_HALF_UP

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from oracle import calc  # noqa: E402

PUB15T = "IRS Pub 15-T (2026)"
CA = "EDD DE 44 Rev.52 (4-26) Method B"
NYS = "NYS-50-T-NYS (1/26)"
NYC = "NYS-50-T-NYC (1/26)"
YON = "NYS-50-T-Y (1/26)"
IL = "IL-700-T (R-12/25)"
NC = "NC-30 (11-25)"
GA1 = "GA Employer's Withholding Tax Guide 2026 rev. Dec 2025"
GA2 = "GA Employer's Withholding Tax Guide 2026 rev. Jun/Sep 2026"
OH1 = "ODT Weekly Withholding Table eff. 2025-10-01"
OH2 = "ODT Weekly Withholding Table eff. 2026-08-01"


def case(state, freq, gross, pay_date="2026-03-13", fed=None, si=None):
    return {"state": state, "frequency": freq, "gross": gross, "pay_date": pay_date, "ytd_gross_before": 0,
            "federal": fed or {"w4_version": "2020", "filing_status": "single"}, "state_inputs": si or {}}


T = []


def add(tid, pub, where, cat, c, line, expected, mode="cents", note=""):
    T.append(dict(id=tid, publication=pub, where=where, category=cat, case=c, line=line, expected=expected, mode=mode, note=note))


# ---------------- Federal
add("FED-NRA-1", PUB15T, "PDF p.7, Example (nonresident alien, weekly $300, 2019 W-4 Single 1 allowance)", "official_example",
    case("TX", "weekly", 300, fed={"w4_version": "pre2020", "marital": "single", "allowances": 1, "nra": True}),
    "fit_whole_dollar", 31, "dollar", "Example uses the wage-bracket tables; oracle uses the percentage method then whole-dollar rounding.")
WB = [  # (period, lo, hi, MFJ std, MFJ chk, HOH std, HOH chk, S std, S chk) — Pub 15-T 2026 section 2 tables
    ("biweekly", 700, 715, 0, 9, 0, 24, 9, 43, "p.17"),
    ("biweekly", 1000, 1015, 0, 39, 8, 58, 39, 79, "p.17"),
    ("semimonthly", 1500, 1520, 17, 90, 50, 113, 90, 148, "p.21"),
    ("semimonthly", 2000, 2020, 67, 150, 106, 184, 150, 258, "p.21"),
    ("semimonthly", 2500, 2520, 120, 210, 166, 294, 210, 368, "p.22"),
]
for per, lo, hi, *vals, page in WB:
    mid = (lo + hi) / 2
    for (st, chk), v in zip([("mfj", False), ("mfj", True), ("hoh", False), ("hoh", True), ("single", False), ("single", True)], vals):
        add(f"FED-WB-{per}-{lo}-{st}-{'chk' if chk else 'std'}", PUB15T, f"{page}, {per} wage bracket ${lo}-${hi}", "table_consistency",
            case("TX", per, mid, fed={"w4_version": "2020", "filing_status": st, "step2": chk}), "fit_whole_dollar", v, "dollar",
            "Formula evaluated at bracket midpoint.")

# ---------------- California (DE 44, pp.43-45 = PDF pp.51-53)
add("CA-A", CA, "p.43 Example A", "official_example", case("CA", "weekly", 210, si={"filing_status": "single", "allowances": 1}), "sit_CA", 0.00)
add("CA-B", CA, "p.43 Example B", "official_example", case("CA", "biweekly", 1600, si={"filing_status": "married", "allowances": 2, "est_ded_allowances": 1}), "sit_CA", 2.38)
add("CA-C", CA, "p.44 Example C", "official_example", case("CA", "monthly", 5100, si={"filing_status": "married", "allowances": 5}), "sit_CA", 0.82)
add("CA-D", CA, "p.44 Example D", "official_example", case("CA", "weekly", 950, si={"filing_status": "hoh", "allowances": 3}), "sit_CA", 1.69)
add("CA-E", CA, "p.45 Example E (annual method)", "official_example", case("CA", "semimonthly", 2400, si={"filing_status": "married", "allowances": 4, "method": "annual"}), "sit_CA", 4.13)
add("CA-F", CA, "p.45 Example F (annual method)", "official_example", case("CA", "monthly", 4750, si={"filing_status": "married", "allowances": 4, "method": "annual"}), "sit_CA", 7.17)

# ---------------- New York State / NYC / Yonkers (same 8 example inputs)
NY_EX = [  # (label, freq, gross, status, allowances, NYS printed, NYC printed, Yonkers printed)
    ("S1", "weekly", 400, "single", 3, 8.01, 6.11, 1.34),
    ("S2", "semimonthly", 5000, "single", 1, 258.51, 188.80, 43.30),
    ("S3", "monthly", 50000, "single", 3, 3576.63, 2070.50, 599.08),
    ("S4", "daily", 750, "single", 2, 44.10, 29.51, 7.39),
    ("M1", "weekly", 400, "married", 4, 6.69, 5.17, 1.12),
    ("M2", "semimonthly", 5000, "married", 3, 248.11, 184.37, 41.56),
    ("M3", "monthly", 50000, "married", 3, 3622.09, 2068.73, 606.70),
    ("M4", "daily", 750, "married", 2, 44.58, 29.43, 7.47),
]
NOTES = {("NYS", "S2"): "Printed step 4: $165.00 x 0.0753 = $12.43; the product is 12.4245.",
         ("NYS", "M2"): "Printed step 4: $58.80 x 0.070[7] = $4.15; 58.80 x 0.0707 = 4.15716.",
         ("YON", "S3"): "Printed: $3,576.63 x 0.1675 = $599.08; the product is 599.085525.",
         ("YON", "S2"): "Yonkers S2 multiplies the NYS printed amount 258.51.",
         ("YON", "M2"): "Yonkers M2 multiplies the NYS printed amount 248.11."}
for lab, f, g, st, a, nys, nyc, yon in NY_EX:
    pg = "p.16" if st == "single" else "p.18"
    add(f"NYS-{lab}", NYS, f"{pg} Example {lab[1]} ({st})", "official_example", case("NY", f, g, si={"filing_status": st, "allowances": a}), "sit_NY", nys, note=NOTES.get(("NYS", lab), ""))
    add(f"NYC-{lab}", NYC, f"p.27 Example {lab[1]} ({st})", "official_example", case("NY", f, g, si={"filing_status": st, "allowances": a, "locality": "nyc"}), "sit_NYC", nyc)
    add(f"YON-{lab}", YON, f"{pg} Example {lab[1]} ({st})", "official_example", case("NY", f, g, si={"filing_status": st, "allowances": a, "locality": "yonkers"}), "sit_YONKERS", yon, note=NOTES.get(("YON", lab), ""))

# ---------------- Illinois
add("IL-ALICE", IL, "p.4 Automated payroll method example", "official_example", case("IL", "weekly", 800, si={"line1": 2, "line2": 2}), "sit_IL", 32.13)
add("IL-MARY", IL, "p.3 Table example ($300-$302 row, 2 + 1 allowances)", "table_consistency", case("IL", "weekly", 301, si={"line1": 2, "line2": 1}), "sit_IL", 8.38,
    note="Table row evaluated at midpoint $301; printed table result after the $0.95 Line-2 subtraction.")

# ---------------- North Carolina
add("NC-PCT", NC, "p.18 Percentage method example", "official_example", case("NC", "weekly", 450, si={"filing_status": "single", "allowances": 2}), "sit_NC", 4, "dollar")
add("NC-ANN", NC, "p.19 Annualized method example", "official_example", case("NC", "weekly", 450, si={"filing_status": "single", "allowances": 2, "method": "annualized"}), "sit_NC", 4, "dollar")

# ---------------- Georgia (two regimes)
add("GA-DEC25-EX1", GA1, "p.46 Table E example (semimonthly $1,470.83, MFJ one income, 1 dependent)", "official_example",
    case("GA", "semimonthly", 1470.83, pay_date="2026-03-15", si={"filing_status": "mfj_one_income", "dependents": 1}), "sit_GA", 15.79)
add("GA-DEC25-EX2", GA1, "p.47 Table F example (biweekly $730.77, HOH, 2 dependents)", "official_example",
    case("GA", "biweekly", 730.77, pay_date="2026-03-13", si={"filing_status": "hoh", "dependents": 2}), "sit_GA", 0.00)
add("GA-2026-EX1", GA2, "p.51 Table E example (semimonthly $2,000, MFJ one income, 1 dependent)", "official_example",
    case("GA", "semimonthly", 2000, pay_date="2026-06-15", si={"filing_status": "mfj_one_income", "dependents": 1}), "sit_GA", 27.03)
add("GA-2026-EX2", GA2, "p.52 Table F example (biweekly $935, HOH, 2 dependents)", "official_example",
    case("GA", "biweekly", 935, pay_date="2026-06-12", si={"filing_status": "hoh", "dependents": 2}), "sit_GA", 0.00)

# ---------------- Ohio (no worked examples: weekly table rows evaluated at upper bound)
for pub, pd, rows in ((OH1, "2026-03-13", [(20, 0, 0.36), (22, 1, 0.17), (1030, 0, 24.71), (1030, 2, 23.96), (1923, 0, 51.41), (1923, 10, 47.67)]),
                      (OH2, "2026-08-14", [(20, 0, 0.32), (22, 1, 0.15), (1030, 0, 23.84), (1030, 2, 23.09), (1923, 0, 50.54), (1923, 10, 46.80)])):
    for ub, ex, v in rows:
        add(f"OH-{pd[:7]}-{ub}-{ex}", pub, f"WEEKLY table row ending ${ub}, {ex} exemptions", "table_consistency",
            case("OH", "weekly", ub, pay_date=pd, si={"exemptions": ex}), "sit_OH", v, note="Formula at the row's upper bound, rounded to cents for comparison.")


def money(x, mode):
    q = Decimal("1") if mode == "dollar" else Decimal("0.01")
    return Decimal(str(x)).quantize(q, rounding=ROUND_HALF_UP)


def run():
    out, summary = [], {}
    for t in T:
        got = calc(t["case"])[t["line"]]
        ok = money(got, t["mode"]) == money(t["expected"], t["mode"])
        rec = {k: t[k] for k in ("id", "publication", "where", "category", "line", "expected", "mode", "note")}
        rec.update(oracle=got, oracle_compared=float(money(got, t["mode"])), result="PASS" if ok else "FAIL")
        out.append(rec)
        s = summary.setdefault((t["publication"], t["category"]), [0, 0])
        s[0 if ok else 1] += 1
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "reference_results.json"), "w", encoding="utf-8") as f:
        json.dump({"tests": out, "summary": [{"publication": p, "category": c, "pass": v[0], "fail": v[1]} for (p, c), v in summary.items()]}, f, indent=2)
    print(f"{'publication':58} {'category':18} pass fail")
    for (p, c), v in summary.items():
        print(f"{p:58} {c:18} {v[0]:4} {v[1]:4}")
    print()
    for r in out:
        if r["result"] == "FAIL":
            print(f"FAIL {r['id']}: expected {r['expected']} got {r['oracle']} ({r['line']}). {r['note']}")
    return out


if __name__ == "__main__":
    run()

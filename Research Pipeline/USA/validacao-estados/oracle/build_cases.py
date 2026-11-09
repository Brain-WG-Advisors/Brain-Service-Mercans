"""Generate cases.json (15 cases per pilot state) and results.json (oracle output for each case).

Coverage per state: weekly/biweekly/semimonthly/monthly (+ daily where relevant), the state's filing statuses,
low/median/high wages, YTD crossing OASDI, SUI, Additional Medicare and FUTA bases (and NY PFL annual max),
2020+ and pre-2020 Forms W-4, and one case before/after each mid-year change (GA 2026-05-11, OH 2026-08-01).
Run:  python build_cases.py
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from oracle import calc, P  # noqa: E402

W4_S = {"w4_version": "2020", "filing_status": "single"}
W4_M = {"w4_version": "2020", "filing_status": "mfj"}
W4_H = {"w4_version": "2020", "filing_status": "hoh"}
W4_CHK = {"w4_version": "2020", "filing_status": "single", "step2": True, "step3": 2000, "step4a": 1200, "step4b": 3000, "step4c": 25}
W4_OLD = {"w4_version": "pre2020", "marital": "married", "allowances": 3}
W4_OLD_S = {"w4_version": "pre2020", "marital": "single", "allowances": 0, "additional": 10}

# per state: (status_low, status_med, status_alt, extra_dict) for state_inputs
SI = {
    "CA": [{"filing_status": "single", "allowances": 1}, {"filing_status": "married", "allowances": 2}, {"filing_status": "hoh", "allowances": 3},
           {"filing_status": "married", "allowances": 4, "est_ded_allowances": 2}],
    "NY": [{"filing_status": "single", "allowances": 0}, {"filing_status": "married", "allowances": 2}, {"filing_status": "single", "allowances": 1, "locality": "nyc"},
           {"filing_status": "married", "allowances": 3, "locality": "yonkers"}],
    "IL": [{"line1": 1, "line2": 0}, {"line1": 2, "line2": 1}, {"line1": 1, "line2": 2}, {"line1": 0, "line2": 0, "additional": 15}],
    "PA": [{}, {}, {}, {"additional": 5}],
    "OH": [{"exemptions": 0}, {"exemptions": 2}, {"exemptions": 1}, {"exemptions": 4}],
    "NC": [{"filing_status": "single", "allowances": 0}, {"filing_status": "mfj", "allowances": 2}, {"filing_status": "hoh", "allowances": 1},
           {"filing_status": "single", "allowances": 1, "method": "annualized"}],
    "MI": [{"exemptions": 1}, {"exemptions": 3}, {"exemptions": 0}, {"exemptions": 2, "additional": 10}],
    "GA": [{"filing_status": "single", "dependents": 0}, {"filing_status": "mfj_one_income", "dependents": 2}, {"filing_status": "hoh", "dependents": 1},
           {"filing_status": "mfj_both_working", "dependents": 0}],
    "TX": [{}, {}, {}, {}],
    "FL": [{}, {}, {}, {}],
}


def mk(state, n, desc, freq, gross, ytd=0, pay_date="2026-03-13", fed=W4_S, si=None, **extra):
    c = {"id": f"{state}-{n:02d}", "description": desc, "state": state, "pay_date": pay_date, "frequency": freq,
         "gross": gross, "ytd_gross_before": ytd, "federal": fed, "state_inputs": si if si is not None else {}}
    c.update(extra)
    return c


def state_cases(st):
    s0, s1, s2, s3 = SI[st]
    base = P[st]["sui"]["wage_base"]
    cs = [
        mk(st, 1, "weekly low wage", "weekly", 320.00, fed=W4_S, si=s0),
        mk(st, 2, "biweekly median wage", "biweekly", 2400.00, ytd=9600, fed=W4_M, si=s1),
        mk(st, 3, "semimonthly median wage, alt status", "semimonthly", 2900.00, ytd=8700, fed=W4_H, si=s2),
        mk(st, 4, "monthly high wage", "monthly", 18000.00, ytd=36000, fed=W4_S, si=s0),
        mk(st, 5, "weekly high wage", "weekly", 4200.00, ytd=50400, fed=W4_M, si=s1),
        mk(st, 6, f"biweekly, YTD crosses SUI wage base {base}", "biweekly", 3000.00, ytd=base - 1250, fed=W4_S, si=s0),
        mk(st, 7, "semimonthly, YTD crosses OASDI base 184,500", "semimonthly", 9000.00, ytd=180000, pay_date="2026-11-13", fed=W4_M, si=s1),
        mk(st, 8, "monthly, YTD crosses Additional Medicare 200,000", "monthly", 25000.00, ytd=190000, pay_date="2026-09-30", fed=W4_S, si=s0),
        mk(st, 9, "weekly, YTD crosses FUTA base 7,000", "weekly", 1100.00, ytd=6600, fed=W4_S, si=s2),
        mk(st, 10, "biweekly, pre-2020 W-4 married 3 allowances", "biweekly", 3100.00, ytd=15500, fed=W4_OLD, si=s1),
        mk(st, 11, "semimonthly, 2020 W-4 Step 2 checkbox + Step 3/4", "semimonthly", 4100.00, ytd=20500, fed=W4_CHK, si=s3),
        mk(st, 12, "monthly, low wage (deductions exceed wages in some states)", "monthly", 900.00, ytd=1800, fed=W4_H, si=s2),
        mk(st, 13, "monthly, already above SUI base and OASDI base", "monthly", 21000.00, ytd=189000, pay_date="2026-10-30", fed=W4_M, si=s3),
    ]
    if st == "GA":
        cs += [mk(st, 14, "biweekly before GA HB 463 change (pay date 2026-05-08)", "biweekly", 2600.00, ytd=23400, pay_date="2026-05-08", fed=W4_S, si=s1),
               mk(st, 15, "biweekly after GA HB 463 change (pay date 2026-05-22)", "biweekly", 2600.00, ytd=26000, pay_date="2026-05-22", fed=W4_S, si=s1)]
    elif st == "OH":
        cs += [mk(st, 14, "weekly before OH table change (pay date 2026-07-31)", "weekly", 1500.00, ytd=45000, pay_date="2026-07-31", fed=W4_S, si=s1),
               mk(st, 15, "weekly after OH table change (pay date 2026-08-07)", "weekly", 1500.00, ytd=46500, pay_date="2026-08-07", fed=W4_S, si=s1)]
    elif st == "NY":
        cs += [mk(st, 14, "biweekly, YTD crosses NY PFL annual max 411.91", "biweekly", 6000.00, ytd=93000, pay_date="2026-09-25", fed=W4_S, si=s0),
               mk(st, 15, "monthly very high wage, single (NY Method III: net >= 89,796)", "monthly", 200000.00, ytd=0, pay_date="2026-01-30", fed=W4_S, si=s0)]
    elif st == "CA":
        cs += [mk(st, 14, "semimonthly, annual-method option, married 4 allowances", "semimonthly", 2400.00, ytd=0, fed=W4_M,
                  si={"filing_status": "married", "allowances": 4, "method": "annual"}),
               mk(st, 15, "daily/misc pay, single, very high wage (14.63% bracket)", "daily", 5000.00, ytd=0, fed=W4_S,
                  si={"filing_status": "single", "allowances": 0})]
    elif st == "NC":
        cs += [mk(st, 14, "daily, falls back to annualized method", "daily", 400.00, ytd=0, fed=W4_S, si={"filing_status": "single", "allowances": 1}),
               mk(st, 15, "biweekly, pre-2020 W-4 single 0 allowances + additional", "biweekly", 1800.00, ytd=0, fed=W4_OLD_S, si=s2)]
    else:
        cs += [mk(st, 14, "daily pay", "daily", 260.00, ytd=0, fed=W4_S, si=s0),
               mk(st, 15, "biweekly, pre-2020 W-4 single 0 allowances + additional", "biweekly", 1800.00, ytd=0, fed=W4_OLD_S, si=s2)]
    return cs


def main():
    states = ["CA", "NY", "IL", "PA", "OH", "NC", "MI", "GA", "TX", "FL"]
    cases = [c for st in states for c in state_cases(st)]
    # MI/PA/IL/TX/FL tables have no 'daily' issue; OH/GA/NY/CA daily supported by params.
    results = []
    for c in cases:
        r = calc(c)
        results.append({"id": c["id"], "lines": {k: v for k, v in r.items() if k != "flags"}, "flags": r["flags"]})
    with open(os.path.join(HERE, "cases.json"), "w", encoding="utf-8") as f:
        json.dump(cases, f, indent=1)
    with open(os.path.join(HERE, "results.json"), "w", encoding="utf-8") as f:
        json.dump(results, f, indent=1)
    print(len(cases), "cases;", len(results), "results")


if __name__ == "__main__":
    main()

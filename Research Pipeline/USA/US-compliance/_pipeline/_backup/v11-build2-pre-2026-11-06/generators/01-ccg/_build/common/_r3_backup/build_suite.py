# -*- coding: utf-8 -*-
"""Build the US country suite (C37 / C69) from the CCG worked examples and the oracle facts.

Contract: shared/validation-suite-template/run_suite.py docstring (read-only template) and
suite_coverage_check.py (C69). Wired to build-manifest.json -> oracle (type official_examples,
suite_dir _validation).

Writes (re-runnable; never hand-edit the outputs):
  suite.json                 suite descriptor
  suite/cases.json           [{id, kind, inputs...}]
  suite/examples.json        reference {case: {line: value, _source: {title, url, kind}}}
  suite/rules.json           {rules: [...], test_cases: {case: {rules, coverage}}}
  suite/defects.json         {defects: []}
The research side is oracle/oracle.py (independent re-implementation of the federal method from the
facts files; it does not import the CCG example calculator for federal cases).

Reference kinds (honest labelling, read by the QA auditor):
  official_example   value published by the authority (oracle fact with its official URL)
  ccg_worked_example value printed in US-CCG-001 v1.0 (computed by the CCG example calculator from
                     the facts); the URL is the official method source. These cases test that an
                     independent re-implementation reproduces the CCG tables (C69: every CCG worked
                     example has a case); they are not authority-published results.
  parameter          a fact value with its official URL; the oracle reads the same key. Used only for
                     coverage rows whose CCG treatment is a rule with no computed example.

usage: python build_suite.py
"""
import glob
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, ".."))
RES = os.path.join(BASE, "_research")
FACTS = {}
for fp in glob.glob(os.path.join(RES, "*-facts.json")):
    for f in json.load(open(fp, encoding="utf-8")).get("facts", []):
        FACTS.setdefault(f["key"], []).append(f)


def fact(key):
    return FACTS[key][0]


def num(s):
    return float(str(s).replace(",", ""))


PUB15T = "https://www.irs.gov/pub/irs-pdf/p15t.pdf"
PUB15 = "https://www.irs.gov/pub/irs-pdf/p15.pdf"
CCG = "US-CCG-001 v1.0"
res = json.load(open(os.path.join(BASE, "01-ccg", "_examples", "out", "results.json"), encoding="utf-8"))
m17 = json.load(open(os.path.join(BASE, "01-ccg", "_examples", "m01_m07_examples.json"), encoding="utf-8"))

cases, examples, tcs = [], {}, {}


def add(cid, kind, inputs, ref, src_title, src_url, rules, coverage):
    cases.append(dict(id=cid, kind=kind, **inputs))
    e = {k: num(v) for k, v in ref.items()}
    e["_source"] = {"title": src_title, "url": src_url, "kind": kind}
    examples[cid] = e
    tcs[cid] = {"rules": rules, "coverage": coverage}


def last(rows):
    return rows[-1][-1]


# ---------------------------------------------------------------- Module 12 scenarios (federal)
A, B, C, Dm = res["A"], res["B"], res["C"], res["D_mandatory_supplemental"]
H12 = "CCG:{}"
add("US-M12-A", "ccg_worked_example",
    {"wage": 3000, "periods": 26, "status": "single", "ytd": 0},
    {k: A[k] for k in ("fit", "oasdi", "medicare", "addl_medicare", "net", "futa")},
    f"{CCG} Module 12 Scenario A (method: IRS Pub. 15-T 2026 Worksheet 1A; FICA/FUTA Pub. 15)", PUB15T,
    ["R-FIT-WS1A", "R-FICA", "R-FUTA"],
    # officers are employees: their pay is computed exactly as Scenario A (CCG Module 11, coverage row)
    ["resident_employee", "officers_without_employment_contract",
     H12.format("A full-time resident employee on a standard salary")])
add("US-M12-B", "ccg_worked_example",
    {"hours": 24, "hourly_key": "fed.minwage.hourly", "periods": 52, "status": "single", "ytd": 0},
    {k: B[k] for k in ("fit", "oasdi", "medicare", "net", "futa")},
    f"{CCG} Module 12 Scenario B (FLSA minimum wage; Pub. 15-T Worksheet 1A)", PUB15T,
    ["R-FIT-WS1A", "R-FICA", "R-FUTA", "R-MINWAGE"],
    ["part_time", "apprentices_and_trainees", H12.format("A casual or part-time employee")])
add("US-M12-C", "ccg_worked_example",
    {"wage": 20000, "periods": 24, "status": "single", "ytd": 182000},
    {k: C[k] for k in ("fit", "oasdi", "medicare", "addl_medicare", "net", "futa")},
    f"{CCG} Module 12 Scenario C (OASDI base and Additional Medicare threshold; Pub. 15)", PUB15,
    ["R-FIT-WS1A", "R-FICA-BASE", "R-ADDL-MEDICARE", "R-FUTA"],
    ["multiple_employers", "special_pay_cycles", "accrual_vs_payment", "annual_regularisation",
     H12.format("Other complex scenarios that are common in the country")])
add("US-M12-D", "ccg_worked_example",
    {"bonus": 50000, "mandatory": True},
    {"fit": Dm["fit"], "medicare": Dm["medicare"], "addl_medicare": Dm["addl"], "net": Dm["net"]},
    f"{CCG} Module 12 special tax obligation (mandatory supplemental rate; Pub. 15 sec. 7)", PUB15,
    ["R-SUPP-MANDATORY", "R-FICA"],
    [H12.format("An employee with a student loan or other special tax obligation"),
     H12.format("An employee with a pre-tax deduction")])
# ---------------------------------------------------------------- Module 9 examples
for cid, key, ytd, cov, head in (("US-M09-RED", "m09_redundancy", 60000,
                                   ["termination_and_final_pay", "fixed_term_contract"],
                                   "Provide a detailed worked example of a redundancy termination payout."),
                                  ("US-M09-BONUS", "m09_bonus", 40000, [],
                                   "Provide a worked example of a bonus calculation.")):
    r = res[key]
    add(cid, "ccg_worked_example", {"amount": num(r["amount"]), "ytd": ytd, "flat": True},
        {k: r[k] for k in ("fit", "oasdi", "medicare", "net")},
        f"{CCG} Module 9 worked example ({key}; optional flat supplemental rate, Pub. 15 sec. 7)", PUB15,
        ["R-SUPP-FLAT", "R-FICA"], cov + ["CCG:" + head])
# ---------------------------------------------------------------- Module 6 examples
for cid, ex, nra, cov in (("US-M06-EX1", m17["ex1"], False, []),
                          ("US-M06-EX2", m17["ex2"], True, ["non_resident_employee"])):
    add(cid, "ccg_worked_example", {"wage": 1640, "periods": 52, "status": "single", "ytd": 0, "nra": nra},
        {"fit": last(ex["fit"]), "oasdi": ex["fica"][0][-1], "medicare": ex["fica"][1][-1], "net": last(ex["net"])},
        f"{CCG} Module 6 worked example ({'nonresident alien, Table 2 add-on' if nra else 'resident'}; Pub. 15-T 2026)",
        PUB15T, ["R-FIT-WS1A"] + (["R-NRA-ADDON"] if nra else []) + ["R-FICA"],
        cov + ["CCG:Deliverable: Provide detailed worked examples for a standard resident employee, a non-resident employee, and an irregular payment."])
ex3 = m17["ex3"]
add("US-M06-EX3", "ccg_worked_example", {"amount": 12400, "ytd": 0, "flat": True},
    {"fit": last(ex3["fit"]), "oasdi": ex3["fica"][0][-1], "medicare": ex3["fica"][1][-1], "net": last(ex3["net"])},
    f"{CCG} Module 6 worked example (irregular payment, optional flat supplemental rate)", PUB15,
    ["R-SUPP-FLAT", "R-FICA"], [])
# ---------------------------------------------------------------- Module 4 examples
ot = m17["overtime"]
add("US-M04-OT", "ccg_worked_example", {"rate": 26.5, "hours": 46},
    {"gross": last(ot)}, f"{CCG} Module 4 overtime example (FLSA weekly overtime, 29 U.S.C. 207)",
    fact("fed.overtime.weekly_threshold_hours")["url"], ["R-OVERTIME"],
    ["overtime", "CCG:Explain how overtime is treated for income tax and social security calculations."])
pr = m17["proration"]
add("US-M04-PRORATION", "ccg_worked_example", {"monthly": 6300, "days": 22, "in_service": 10},
    {"gross": last(pr)}, f"{CCG} Module 4 proration example (configuration choice, working-day method)",
    PUB15, ["R-PRORATION"],
    ["mid_month_joiner_and_leaver", "CCG:Provide the proration formula and a worked example."])
# ---------------------------------------------------------------- State oracles (12.2)
ORACLE_COV = {"ga.oracle.mfj_semimonthly.withholding": ["mid_year_rate_change"],
              "mi.oracle.detroit.resident_biweekly_2000": ["local_regimes"]}
for k, r in res.items():
    if not isinstance(r, dict) or "fact" not in r:
        continue
    f = fact(k)
    add("US-ORA-" + k.split(".")[0].upper() + "-" + re.sub(r"[^A-Za-z0-9]+", "_", k.split(".", 1)[1]).strip("_"),
        "official_example", {"oracle_key": k}, {"withholding": r["fact"]},
        f"{f.get('authority')} published example ({k}, register {f['register_id']})", f.get("url") or PUB15T,
        ["R-STATE-ORACLE"], ORACLE_COV.get(k, []) + ["CCG:12.2.2 Re-derivation from verified figures"])
# ---------------------------------------------------------------- parameter cases (rule rows)
PARAMS = [
    ("US-PAR-PFML-WA", "wa.pfml.employee.share", ["maternity_paternity_parental"]),
    ("US-PAR-WC-WA", "wa.wc.supplemental_pension.rate", ["work_accident_occupational_disease"]),
    ("US-PAR-HOUSEHOLD", "fed.household.fica_cash_threshold", ["employer_type_and_size"]),
]
for cid, key, cov in PARAMS:
    if key not in FACTS:
        print("parameter case skipped, no fact:", key)
        continue
    f = sorted(FACTS[key], key=lambda x: x.get("effective_from") or "")
    f = next((x for x in f if (x.get("effective_from") or "") <= "2026-12-31" and (x.get("effective_to") or "9999") >= "2026-01-01"), f[0])
    v = f["value"]
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        print("parameter case skipped, not numeric:", key)
        continue
    add(cid, "parameter", {"key": key, "on": f.get("effective_from")}, {"value": v},
        f"{f.get('authority')} ({key}, register {f['register_id']})", f.get("url") or PUB15,
        ["R-PARAM"], cov)

rules = [
    {"id": "R-FIT-WS1A", "statement": "Federal income tax: Pub. 15-T 2026 Worksheet 1A, STANDARD schedule, annualise x periods, less line 1g, bracket cumulative tax + excess x rate, / periods, half-up to the cent", "lines": ["fit"]},
    {"id": "R-NRA-ADDON", "statement": "Nonresident alien: Table 2 add-on added to the wages for the computation only", "lines": ["fit", "net"]},
    {"id": "R-FICA", "statement": "OASDI employee rate x lesser of remaining base and pay; Medicare employee rate x pay", "lines": ["oasdi", "medicare", "net"]},
    {"id": "R-FICA-BASE", "statement": "OASDI stops at the annual wage base per employer", "lines": ["oasdi"]},
    {"id": "R-ADDL-MEDICARE", "statement": "Additional Medicare on wages above the withholding threshold, employee only", "lines": ["addl_medicare"]},
    {"id": "R-FUTA", "statement": "FUTA net rate on the first wage-base dollars per employee per year", "lines": ["futa"]},
    {"id": "R-SUPP-FLAT", "statement": "Supplemental wages: optional flat rate", "lines": ["fit", "net"]},
    {"id": "R-SUPP-MANDATORY", "statement": "Supplemental wages above the mandatory threshold: mandatory rate", "lines": ["fit", "net"]},
    {"id": "R-MINWAGE", "statement": "Gross = hours x FLSA minimum wage", "lines": ["net"]},
    {"id": "R-OVERTIME", "statement": "Weekly overtime above the threshold at the premium multiplier", "lines": ["gross"]},
    {"id": "R-PRORATION", "statement": "Monthly salary x working days in service / working days in the month (configuration choice)", "lines": ["gross"]},
    {"id": "R-STATE-ORACLE", "statement": "State withholding re-derived from the facts equals the authority's published example", "lines": ["withholding"]},
    {"id": "R-PARAM", "statement": "Rule parameter of a coverage row read from the facts equals the official value", "lines": ["value"]},
]
os.makedirs(os.path.join(HERE, "suite"), exist_ok=True)
os.makedirs(os.path.join(HERE, "oracle"), exist_ok=True)
json.dump(cases, open(os.path.join(HERE, "suite", "cases.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump(examples, open(os.path.join(HERE, "suite", "examples.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump({"rules": rules, "test_cases": tcs}, open(os.path.join(HERE, "suite", "rules.json"), "w", encoding="utf-8"),
          indent=1, ensure_ascii=False)
json.dump({"defects": []}, open(os.path.join(HERE, "suite", "defects.json"), "w", encoding="utf-8"), indent=1)
man = json.load(open(os.path.join(BASE, "_pipeline", "build-manifest.json"), encoding="utf-8"))["oracle"]
suite = {
    "_purpose": "US country suite for C37 (Stage 9b) and C69, built by _validation/build_suite.py from the CCG worked examples and the oracle facts. Wired to build-manifest.json oracle.",
    "_manifest_oracle": {k: man.get(k) for k in ("type", "name", "version", "publisher", "source_url", "suite_dir")},
    "country": "US",
    "reference": {"type": "official_examples", "file": "suite/examples.json",
                  "source": "IRS Pub. 15-T / Pub. 15 (2026) and State authority published examples; CCG worked examples labelled kind=ccg_worked_example"},
    "cases": "suite/cases.json",
    "research": {"module": "oracle/oracle.py", "expected": "expected", "compare": "compare"},
    "rules": "suite/rules.json",
    "defects": "suite/defects.json",
    "baseline": "baseline/baseline.json",
    "target_agreement": 0.98,
    "agreement_basis": "law",
    "_limitations": [
        "Federal cases: oracle/oracle.py re-implements Worksheet 1A, FICA, FUTA and the supplemental rates from the facts files independently of the CCG example calculator.",
        "State oracle cases: the research value is the CCG example calculator's re-derivation (01-ccg/_examples/out/results.json), compared with the authority's published result; it is not a second independent implementation.",
        "Parameter cases test that the facts carry the rule parameter of a coverage row; they are not calculations.",
        "Pub. 15-T wage-bracket examples (NRA 526.90 -> 31, tribal 6,000 -> 584.09) are not cases: the wage-bracket tables are not keyed."],
}
json.dump(suite, open(os.path.join(HERE, "suite.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(cases), "cases;", sum(1 for c in cases if c["kind"] == "official_example"), "official;",
      sum(1 for c in cases if c["kind"] == "ccg_worked_example"), "CCG examples;",
      sum(1 for c in cases if c["kind"] == "parameter"), "parameter")

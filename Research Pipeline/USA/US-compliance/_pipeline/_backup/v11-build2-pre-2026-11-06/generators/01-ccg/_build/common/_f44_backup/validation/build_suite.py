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
HEAD = res.get("_headings", {})          # r3: Module 12 "Worked example n" headings (C69 counts them)


def hcov(key):
    return ["CCG:" + HEAD[key]] if key in HEAD else []


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
     H12.format("A full-time resident employee on a standard salary")] + hcov("A"))
add("US-M12-B", "ccg_worked_example",
    {"hours": 24, "hourly_key": "fed.minwage.hourly", "periods": 52, "status": "single", "ytd": 0},
    {k: B[k] for k in ("fit", "oasdi", "medicare", "net", "futa")},
    f"{CCG} Module 12 Scenario B (FLSA minimum wage; Pub. 15-T Worksheet 1A)", PUB15T,
    ["R-FIT-WS1A", "R-FICA", "R-FUTA", "R-MINWAGE"],
    ["part_time", "apprentices_and_trainees", H12.format("A casual or part-time employee")] + hcov("B"))
add("US-M12-C", "ccg_worked_example",
    {"wage": 20000, "periods": 24, "status": "single", "ytd": 182000},
    {k: C[k] for k in ("fit", "oasdi", "medicare", "addl_medicare", "net", "futa")},
    f"{CCG} Module 12 Scenario C (OASDI base and Additional Medicare threshold; Pub. 15)", PUB15,
    ["R-FIT-WS1A", "R-FICA-BASE", "R-ADDL-MEDICARE", "R-FUTA"],
    ["multiple_employers", "special_pay_cycles", "accrual_vs_payment", "annual_regularisation",
     H12.format("Other complex scenarios that are common in the country")] + hcov("C"))
add("US-M12-D", "ccg_worked_example",
    {"bonus": 50000, "mandatory": True},
    {"fit": Dm["fit"], "medicare": Dm["medicare"], "addl_medicare": Dm["addl"], "net": Dm["net"]},
    f"{CCG} Module 12 special tax obligation (mandatory supplemental rate; Pub. 15 sec. 7)", PUB15,
    ["R-SUPP-MANDATORY", "R-FICA"],
    [H12.format("An employee with a student loan or other special tax obligation"),
     H12.format("An employee with a pre-tax deduction")] + hcov("D_mandatory_supplemental"))
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
        ["R-STATE-ORACLE"], ORACLE_COV.get(k, []) + ["CCG:12.2.2 Re-derivation from verified figures"] + hcov(k))
# ---------------------------------------------------------------- annex worked examples (r3, QA r2 C69)
# Annex DC-MA example calculator (01-ccg/_scratch/annex-DC-MA/build_examples_annex_DC-MA.py) re-derives
# published State examples; each agreeing result is a case. Its research value is that calculator's result.
ANNEX_RES = os.path.join(BASE, "01-ccg", "_scratch", "annex-DC-MA", "examples_results.json")
annex_vals = {}
if os.path.exists(ANNEX_RES):
    for row in json.load(open(ANNEX_RES, encoding="utf-8")):
        if len(row) >= 6 and row[4]:
            annex_vals[row[5]] = (row[0], row[1], row[2])
case_keys = {c.get("oracle_key") for c in cases}
for k, (jur, name, comp) in sorted(annex_vals.items()):
    if k in case_keys or k not in FACTS:
        continue
    f = fact(k)
    add("US-ANX-" + jur + "-" + re.sub(r"[^A-Za-z0-9]+", "_", k.split(".", 1)[1]).strip("_"),
        "official_example", {"oracle_key": k, "calc": "annex_DC-MA", "example": name}, {"withholding": f["value"]},
        f"{f.get('authority')} published example ({k}, register {f['register_id']}); CCG Annex {jur} example {name}",
        f.get("url") or PUB15T, ["R-STATE-ORACLE"], ["CCG:Annex " + jur + " " + name])
    case_keys.add(k)
# ---------------------------------------------------------------- CT DRS per-period tables (r3, QA r2 C69)
# Configuration decision of 2026-11-02: the CT engine uses the DRS per-period tables of IP 2026(1).
# The oracle looks the band up independently in the keyed table rows (ct.wh.table.<period>.row.*).
CT_CASES = [("ct.oracle.ex8_f_weekly700.withholding", "weekly", 700, "F", "8"),
            ("ct.oracle.ip2026_1.ex8.withholding", "weekly", 700, "F", "8"),
            ("ct.oracle.ex9_a_weekly1000.withholding", "weekly", 1000, "A", "9"),
            ("ct.oracle.ip2026_1.ex9.withholding", "weekly", 1000, "A", "9"),
            ("ct.oracle.ex10_b_biweekly2300.withholding", "biweekly", 2300, "B", "10"),
            ("ct.oracle.ip2026_1.ex10.withholding", "biweekly", 2300, "B", "10")]
for k, per, wage, code, exn in CT_CASES:
    if k not in FACTS or k in case_keys:
        continue
    f = fact(k)
    add("US-ORA-CT-" + re.sub(r"[^A-Za-z0-9]+", "_", k.split(".", 2)[2]).strip("_"), "official_example",
        {"oracle_key": k, "calc": "ct_table", "period": per, "wage": wage, "code": code},
        {"withholding": f["value"]},
        f"Connecticut DRS IP 2026(1) example {exn} ({k}, register {f['register_id']}); DRS per-period table, code {code}",
        f.get("url") or PUB15T, ["R-CT-TABLE"], ["CCG:Annex CT CT.14 example " + exn])
    case_keys.add(k)
# same published example carried under a second key (value identical): a case on the second key with the
# research value of the first (m12 calculator)
SAME_EXAMPLE = {"mi.oracle.state.biweekly_2000_1ex": "mi.oracle.biweekly_2000_1ex.withholding"}
for k2, k1 in SAME_EXAMPLE.items():
    if k2 in FACTS and k1 in res and k2 not in case_keys and num(fact(k2)["value"]) == num(fact(k1)["value"]):
        f = fact(k2)
        add("US-ORA-" + k2.split(".")[0].upper() + "-" + re.sub(r"[^A-Za-z0-9]+", "_", k2.split(".", 1)[1]).strip("_"),
            "official_example", {"oracle_key": k2, "same_as": k1}, {"withholding": f["value"]},
            f"{f.get('authority')} published example ({k2} = {k1}, register {f['register_id']})", f.get("url") or PUB15T,
            ["R-STATE-ORACLE"], hcov(k1))
        case_keys.add(k2)
# ---------------------------------------------------------------- oracle results without a case (recorded reason)
TAGGED = set()
for fp in glob.glob(os.path.join(BASE, "01-ccg", "modules", "*.md")) + glob.glob(os.path.join(BASE, "01-ccg", "annexes", "*.md")):
    TAGGED |= set(re.findall(r"\[\[FACT:([a-z0-9_.]*\boracle\b[a-z0-9_.]*)=", open(fp, encoding="utf-8").read()))
case_keys = {c.get("oracle_key") for c in cases}
NOT_RESULT = re.compile(r"\.(input|wages|payment|source|suite)$|estimator_not_oracle|examples_weekly")
SPECIAL = {
    "fed.oracle.pub15t.nra_example.withholding": "Pub. 15-T wage-bracket result: the wage-bracket tables are not keyed, so no research value can be computed.",
    "fed.oracle.pub15t.tribal_example.withholding": "Tribal gaming withholding tables are not keyed, so no research value can be computed.",
    "nd.oracle.section2_booklet.withholding": "Booklet defect: the printed figure contradicts the booklet's own table; never an expected result.",
    "il.oracle.il700t.example1.withholding": "IL-700-T table-method result (bracket midpoint); the suite case is the automated-method result of the same example.",
}
without = {}
for k in sorted(TAGGED - case_keys):
    if NOT_RESULT.search(k):
        without[k] = "Not a withholding result (example input, descriptor or source note); nothing to compare."
    elif k in SPECIAL:
        without[k] = SPECIAL[k]
    elif k not in FACTS:
        without[k] = "Key not in the facts files (alias of a keyed result)."
    else:
        v = FACTS[k][0]["value"]
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            without[k] = "Not a numeric result (string fact); nothing to compare."
        else:
            without[k] = ("Published result quoted in the annex: the CCG prints no re-derivation of it (no calculation "
                          "table), so there is no research value independent of the fact itself; a case would compare "
                          "the fact with itself. Closes when a State calculator re-derives it.")
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
    {"id": "R-CT-TABLE", "statement": "Connecticut: withholding = amount of the CT-W4 code column in the DRS per-period table band (wages greater than the lower bound and not above the upper bound)", "lines": ["withholding"]},
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
        "Pub. 15-T wage-bracket examples (NRA 526.90 -> 31, tribal 6,000 -> 584.09) are not cases: the wage-bracket tables are not keyed.",
        "Annex DC-MA cases (US-ANX-*): the research value is the annex example calculator's re-derivation, compared with the authority's published result."],
    "_oracle_results_tagged_in_ccg": len(TAGGED),
    "_oracle_results_with_case": len(TAGGED & {c.get("oracle_key") for c in cases}),
    "_oracle_results_without_case": without,
}
json.dump(suite, open(os.path.join(HERE, "suite.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(TAGGED), "oracle keys tagged in the CCG;", len(TAGGED & {c.get("oracle_key") for c in cases}), "with a case;",
      len(without), "with a recorded reason")
print(len(cases), "cases;", sum(1 for c in cases if c["kind"] == "official_example"), "official;",
      sum(1 for c in cases if c["kind"] == "ccg_worked_example"), "CCG examples;",
      sum(1 for c in cases if c["kind"] == "parameter"), "parameter")

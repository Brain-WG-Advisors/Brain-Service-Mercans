"""Append this builder's research requests to _research/CCG-research-request.json (shared file:
re-read immediately before writing, append only, next free RQ ids) and write the bindings CSV.
Run after build_annexes.py.  python gen_requests.py [--write]"""
import csv, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RES = os.path.join(BASE, "_research")
REQ = os.path.join(RES, "CCG-research-request.json")
rep = json.load(open(os.path.join(HERE, "report.json"), encoding="utf-8"))

DOMAIN = {"labour_code": "labour_code", "income_tax": "income_tax", "income_tax_nonresident": "income_tax",
          "non_resident": "income_tax", "local_tax": "income_tax", "social_security": "social_security",
          "payslip_statute": "payslip_statute", "reporting": "statutory_reporting",
          "reporting_instruments": "statutory_reporting", "leave": "leave", "termination": "termination",
          "benefits_in_kind": "benefits_in_kind", "deductions_garnishments": "deductions_garnishments",
          "collective_agreements": "collective_agreements", "indexation": "indexation",
          "data_protection": "payroll_data_protection", "live_legal_change": "live_legal_change",
          "live_change": "live_legal_change"}
SEC_DOMAIN = {"1": "labour_code", "2": "income_tax", "2b": "income_tax", "2c": "income_tax", "3": "social_security",
              "4": "payslip_statute", "5": "statutory_reporting", "6": "leave", "7": "termination",
              "8": "benefits_in_kind", "9": "deductions_garnishments", "10": "collective_agreements",
              "11": "indexation", "12": "payroll_data_protection", "13": "live_legal_change", "15": "social_security"}


def annex_lines(u):
    return open(os.path.join(BASE, "01-ccg", "annexes", f"annex_{u}.md"), encoding="utf-8").read().splitlines()


def locate_pivot(u, key, lines):
    m = re.match(r"^multi\.(sui\.other_state_wage_credit|pfml\.coverage_test|nonresident|convenience)\.([a-z]{2})", key)
    if not m:
        return None
    title = {"sui.other_state_wage_credit": "Other-State wage-base credit", "pfml.coverage_test": "PFML / SDI / TDI coverage test",
             "nonresident": "Non-resident thresholds", "convenience": "Convenience-of-the-employer"}[m.group(1)]
    start = next(i for i, ln in enumerate(lines) if ln.startswith("**") and title in ln)
    for i in range(start, len(lines)):
        if lines[i].startswith(f"| {m.group(2).upper()} |") and "RESEARCH-GAP" in lines[i]:
            return i + 1
        if i > start + 3 and not lines[i].startswith("|"):
            break
    return None


def section_of(lines, ln):
    for i in range(ln - 1, -1, -1):
        m = re.match(r"^## ([A-Z]+)\.([0-9a-zA-Z]+) ", lines[i])
        if m:
            return f"{m.group(1)}.{m.group(2)}", m.group(2)
    return "?", "?"


reqs = []
unit_facts = {}
for u in rep:
    fj = json.load(open(os.path.join(RES, f"CCG-annex_{u}-facts.json"), encoding="utf-8"))
    unit_facts[u] = fj
    lines = annex_lines(u)
    for g in fj.get("unresolved", []):
        ln = locate_pivot(u, g["key"], lines) if u == "MULTI" else None
        if ln is None:
            ln = rep[u]["gaplines"][g["key"]][0]
        assert "RESEARCH-GAP" in lines[ln - 1], (u, g["key"], ln)
        sec, sid = section_of(lines, ln)
        blk = bool(g.get("blocking"))
        reqs.append({
            "key": g["key"], "location": f"01-ccg/annexes/annex_{u}.md!{sec}!L{ln}",
            "question": f"What does the official source establish for `{g['key']}` for 2026 (and 2027 where published)? Context: {g.get('why', '').strip()}",
            "why_blocking": (f"Annex {u} cannot be built for this item: blocking RESEARCH-GAP at annex_{u}.md!{sec}!L{ln}; the engine cannot compute or route without it."
                             if blk else f"Annex {u} ships this item as a named non-blocking RESEARCH-GAP at annex_{u}.md!{sec}!L{ln}; the CCG cannot be declared final (C29 / G-CLEAN) while the marker stands."),
            "domain": SEC_DOMAIN.get(sid, "live_legal_change"), "acceptable_tier": "A.2",
            "attempted_by_requester": [f"_research/CCG-annex_{u}-facts.json unresolved[] and facts[]",
                                       f"_research/CCG-annex_{u}-research-pack.md (all sections)"],
            "severity": "blocker" if blk else "minor",
            "expected_shape": "a value with unit, effective_from and an active A.1/A.2 register row",
            "_what_would_close_it": g.get("what_would_close_it", ""), "_raised_by_unit": f"annex_{u}",
            "_origin": "facts unresolved[]"})


def find(u, needle):
    lines = annex_lines(u)
    for i, ln in enumerate(lines, 1):
        if needle in ln and "RESEARCH-GAP" in ln:
            sec, _ = section_of(lines, i)
            return f"01-ccg/annexes/annex_{u}.md!{sec}!L{i}"
    raise SystemExit(f"marker not found {u} {needle}")


NEW = [
    ("FED", "fed.equity.withholding_treatment", "federal classification and withholding treatment of equity income", "blocker",
     "How is equity income of an employee treated for federal income tax withholding, FICA and FUTA in 2026 (non-qualified option exercise spread, restricted stock unit vesting, ISO and ESPP dispositions): supplemental wages or not, timing, and the W-2 reporting codes?",
     "C31 resident / non-resident matrix row 'Equity' in Annex FED (and by reference every State matrix) has no keyed treatment; the engine cannot classify equity pay.", "income_tax", "A.1"),
    ("AL", "al.wh.std_deduction.phaseout_steps", "standard-deduction phase-out between the maximum and the minimum", "major",
     "What are the 2026 Alabama withholding standard-deduction phase-out steps by filing status (gross-income start point, reduction per income step, step size and the income at which the minimum applies), per the ADOR withholding booklet rev. 01/2026 p. 7?",
     "The Alabama formula cannot compute the standard deduction for gross income inside the phase-out range (AL.2).", "income_tax", "A.2"),
    ("AR", "ar.wh.severance.treatment", "no Arkansas-specific treatment in the research", "minor",
     "How does Arkansas treat severance pay for withholding in 2026 (regular wages under the formula, supplemental at the flat rate, or exempt), for residents and for non-residents on Arkansas-source pay?",
     "The C31 matrix row 'Severance' in Annex AR carries a RESEARCH-GAP marker.", "income_tax", "A.2"),
    ("CA", "ca.pit.bracket.married.rates", "the married and head-of-household schedules carry their band ceilings as one value", "major",
     "What rate attaches to each band of the 2026 California DE 44 Method B married and head-of-household annual schedules (including the bands around the 1,000,000 point), keyed per band like the single schedule?",
     "Married and head-of-household PIT cannot be computed band by band from keys; only the single schedule is keyed per band (CA.2).", "income_tax", "A.2"),
    ("CT", "ct.wh.tables_c_d_e", "Tables C (phase-out add-back), D (recapture) and E", "major",
     "What are the 2026 Connecticut TPG-211 Tables C (phase-out add-back), D (recapture) and E (personal tax credit) by withholding code, as keyed thresholds, amounts and percentages?",
     "The TPG-211 rules method cannot be computed without Tables C, D and E (CT.2).", "income_tax", "A.2"),
]
for u in ["AK", "AL", "AR", "AZ", "CA", "CO", "CT"]:
    NEW.append((u, f"{u.lower()}.special_populations.ui_coverage_thresholds", "the coverage thresholds that apply to these populations", "minor",
                f"What are the 2026 {u} UI coverage thresholds for domestic, agricultural and non-profit employment (quarterly cash wages, headcount and weeks tests) and the other numeric special-population thresholds cited in the {u} research pack, as keyed facts with their statute?",
                f"Annex {u} special-populations section states these thresholds qualitatively only; DD and WTC cannot encode coverage tests without keys.", "social_security", "A.1"))

for u, key, needle, sev, q, why, dom, tier in NEW:
    reqs.append({"key": key, "location": find(u, needle), "question": q, "why_blocking": why, "domain": dom,
                 "acceptable_tier": tier,
                 "attempted_by_requester": [f"_research/CCG-annex_{u}-facts.json facts[] and unresolved[]",
                                            f"_research/CCG-annex_{u}-research-pack.md"],
                 "severity": sev, "expected_shape": "keyed values with unit, effective_from and an active A.1/A.2 register row",
                 "_raised_by_unit": f"annex_{u}", "_origin": "template demand without a key (builder)"})

print(len(reqs), "requests;", sum(r["severity"] == "blocker" for r in reqs), "blocker")

# bindings CSV
with open(os.path.join(BASE, "_pipeline", "CCG-bindings-annex_FED-CT.csv"), "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["location", "key", "register_id"])
    n = 0
    for u, d in rep.items():
        for loc, key, rid in d["bindings_list"]:
            w.writerow([f"01-ccg/annexes/annex_{u}.md §{loc}", key, rid]); n += 1
print(n, "binding rows")

if "--write" in sys.argv:
    doc = json.load(open(REQ, encoding="utf-8"))  # re-read immediately before writing
    have = {(r["key"], r.get("_raised_by_unit")) for r in doc.get("requests", [])}
    nums = [int(r["id"][3:]) for r in doc.get("requests", [])]
    nxt = (max(nums) if nums else 0) + 1
    added = []
    for r in reqs:
        if (r["key"], r["_raised_by_unit"]) in have:
            continue
        r = dict(id=f"RQ-{nxt:03d}", **r)
        nxt += 1
        doc["requests"].append(r)
        added.append(r["id"])
    tmp = REQ + ".tmp"
    json.dump(doc, open(tmp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    os.replace(tmp, REQ)
    print("appended", len(added), added[:1], added[-1:])
    json.dump(added, open(os.path.join(HERE, "appended_ids.json"), "w"))

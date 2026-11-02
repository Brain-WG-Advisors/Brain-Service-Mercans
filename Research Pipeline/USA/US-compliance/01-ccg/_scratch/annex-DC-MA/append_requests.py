# -*- coding: utf-8 -*-
"""Append one research request per RESEARCH-GAP marker of annexes DC..MA to the shared
_research/CCG-research-request.json (re-read immediately before writing; ids continue
after the current maximum; existing items untouched; idempotent per (unit, key))."""
import json, os, re, sys, glob, datetime

BASE = sys.argv[1]
JURS = sys.argv[2].split(",")
SCR = os.path.dirname(os.path.abspath(__file__))
REQ = os.path.join(BASE, "_research", "CCG-research-request.json")
REQ_DOMAIN = {"1": "labour_code", "2": "income_tax", "2b": "income_tax", "2c": "income_tax",
              "3": "social_security", "4": "payslip_statute", "5": "statutory_reporting", "6": "leave",
              "7": "termination", "8": "benefits_in_kind", "9": "deductions_garnishments",
              "10": "collective_agreements", "11": "indexation", "12": "payroll_data_protection",
              "13": "live_legal_change", "WE": "income_tax", "SP": "labour_code", "LG": "payslip_statute"}
SECNUM = {"WE": "14", "SP": "15", "LG": "16"}
A1 = re.compile(r"(statute|Code|CMR|KAR|IAC|IC |KRS|R\.S\.|HRS|ILCS|K\.S\.A|O\.C\.G\.A|Act|chapter|ch\. |c\.\d|s\.\d|rule|DCMR|LAC|IDAPA|Del\. C|ordinance)", re.I)

items = []
for j in JURS:
    rep = json.load(open(os.path.join(SCR, f"report_{j}.json"), encoding="utf-8"))
    rel = f"01-ccg/modules/annex_{j}.md"
    lines = open(os.path.join(BASE, rel), encoding="utf-8").read().splitlines()
    gaps = list(rep["gaps"])
    if j == "IL":
        gaps.append({"section": "WE", "title": "Worked examples", "key": "il.oracle.il700t.example1.inputs",
                     "why": "IL-700-T example 1 prints 8.38; the formula with the 2026 exemption amounts (il.wh.exemption.line1, il.wh.exemption.line2) and rate il.pit.rate.flat on weekly 300.00 with Line 1 = 2 and Line 2 = 1 gives 8.33.",
                     "what_would_close_it": "IL-700-T (2026) example 1 re-read: wage, pay period and allowance counts it uses, or an IDOR erratum.",
                     "blocking": False, "attempted": []})
    for g in gaps:
        ln = next((i + 1 for i, t in enumerate(lines) if f"`{g['key']}`" in t and "RESEARCH-GAP" in t), None)
        assert ln, (j, g["key"])
        sec = g["section"]
        secnum = SECNUM.get(sec, sec)
        loc = f"{rel}!{j}.{secnum}!L{ln}"
        close = g.get("what_would_close_it", "")
        blocking = bool(g.get("blocking"))
        it = {
            "key": g["key"],
            "location": loc,
            "question": f"For {j} (2026, and 2027 where published): {g['why'].rstrip('.')}. What does the primary source establish? Source to read: {close}",
            "why_blocking": (f"Blocking item: annex {j} section {j}.{secnum} cannot state this rule or value, so the {j} layer cannot be configured or closed (RESEARCH-GAP at {loc})."
                             if blocking else
                             f"Annex {j} ships this as a named non-blocking RESEARCH-GAP at {loc}; the CCG cannot be declared final (C29 / G-CLEAN) while the marker stands."),
            "domain": REQ_DOMAIN[sec],
            "acceptable_tier": "A.1" if A1.search(close) and not re.search(r"\b(page|portal|FAQ|notice|guide|form|table|spec|layout)\b", close, re.I) else "A.2",
            "attempted_by_requester": [f"_research/CCG-annex_{j}-facts.json unresolved[] and facts[]",
                                       f"_research/CCG-annex_{j}-research-pack.md (all sections)"] + [str(a) for a in (g.get("attempted") or [])],
            "severity": "blocker" if blocking else "minor",
            "expected_shape": "a value or rule with effective_from and an active A.1/A.2 legal-basis register row",
            "_what_would_close_it": close,
            "_raised_by_unit": f"annex_{j}",
        }
        items.append(it)

# re-read right before writing
doc = json.load(open(REQ, encoding="utf-8")) if os.path.exists(REQ) else {
    "schema_version": "1.4.0", "artifact": "CCG", "requested_by": "artifact-builder", "round": 1,
    "created_on": datetime.date.today().isoformat(), "requests": []}
have = {(r.get("_raised_by_unit"), r["key"]) for r in doc.get("requests", [])}
mx = max([int(r["id"].split("-")[1]) for r in doc.get("requests", [])] or [0])
added = []
for it in items:
    if (it["_raised_by_unit"], it["key"]) in have:
        continue
    mx += 1
    it = {"id": f"RQ-{mx:03d}", **it}
    doc["requests"].append(it)
    added.append(it["id"])
tmp = REQ + ".tmp-annex-DC-MA"
json.dump(doc, open(tmp, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
os.replace(tmp, REQ)
json.dump(added, open(os.path.join(SCR, "requests_added.json"), "w"), indent=0)
print("appended", len(added), added[:1], added[-1:], "total", len(doc["requests"]))

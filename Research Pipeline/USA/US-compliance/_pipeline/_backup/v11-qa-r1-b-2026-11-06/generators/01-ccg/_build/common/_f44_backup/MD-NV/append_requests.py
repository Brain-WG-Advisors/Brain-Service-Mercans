# -*- coding: utf-8 -*-
"""Append the RESEARCH-GAP items of annexes MD..NV to the shared _research/CCG-research-request.json
(re-read immediately before writing; exclusive lock file; never overwrites other builders' items)."""
import json, os, re, sys, time, datetime
BASE = sys.argv[1]
SCR = os.path.dirname(os.path.abspath(__file__))
res = json.load(open(os.path.join(SCR, "build_result.json"), encoding="utf-8"))
REQ = os.path.join(BASE, "_research", "CCG-research-request.json")
LOCK = REQ + ".lock"
TAG = re.compile(r"\[\[FACT:\s*([A-Za-z0-9_.]+)\s*=\s*([^\]]+?)\s*\]\]")
DOM = {"labour_code": "labour_code", "income_tax": "income_tax", "non_resident": "income_tax",
       "local_tax": "income_tax", "social_security": "social_security", "payslip_statute": "payslip_statute",
       "reporting_instruments": "statutory_reporting", "leave": "leave", "termination": "termination",
       "benefits_in_kind": "benefits_in_kind", "deductions_garnishments": "deductions_garnishments",
       "collective_agreements": "collective_agreements", "indexation": "indexation",
       "data_protection": "payroll_data_protection", "live_change": "live_legal_change"}
VALUE_KEY = re.compile(r"(rate|wage_base|minwage|tables|threshold|fee|base|cap|amount)")

items = []
for r in res:
    jur = r["jur"]
    for g in r["gaps"]:
        key = g["key"]
        why = TAG.sub(lambda m: m.group(2), g["text"]).strip()
        close = TAG.sub(lambda m: m.group(2), g["close"] or "").strip()
        loc = f"{r['file']}!{g['section']}!L{g['line']}"
        if g["blocking"]:
            wb = (f"Blocking: annex {jur} cannot configure this item; it is written as a blocking RESEARCH-GAP at "
                  f"{loc} and the annex cannot close while it is open.")
        else:
            wb = (f"Annex {jur} ships this item as a named non-blocking RESEARCH-GAP at {loc}; the CCG cannot be "
                  f"declared final (C29 / G-CLEAN) while the marker stands.")
        q = f"For {jur} ({key}): {why}" if why.endswith("?") else \
            f"What does the official {jur} source establish for `{key}`, effective for 2026 (and 2027 where published)? Context: {why}"
        it = {"key": key, "location": loc, "question": q, "why_blocking": wb,
              "domain": DOM.get(g["domain"], "labour_code"),
              "acceptable_tier": "A.2" if VALUE_KEY.search(key) else "A.1",
              "attempted_by_requester": [f"_research/CCG-annex_{jur}-facts.json unresolved[] and facts[]",
                                         f"_research/CCG-annex_{jur}-research-pack.md (all sections)"],
              "severity": "blocker" if g["blocking"] else "minor",
              "expected_shape": ("a value with unit, effective_from and an active A.1/A.2 register row"
                                 if VALUE_KEY.search(key) else "a rule statement with its article and an active register row"),
              "_what_would_close_it": close, "_raised_by_unit": f"annex_{jur}"}
        items.append(it)

for _ in range(120):
    try:
        fd = os.open(LOCK, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
        break
    except FileExistsError:
        time.sleep(0.5)
else:
    sys.exit("lock busy")
try:
    if os.path.exists(REQ):
        doc = json.load(open(REQ, encoding="utf-8"))
    else:
        doc = {"schema_version": "1.4.0", "artifact": "CCG", "requested_by": "artifact-builder", "round": 1,
               "created_on": datetime.date.today().isoformat(), "requests": []}
    doc.setdefault("requests", [])
    have = {(x.get("key"), x.get("_raised_by_unit")) for x in doc["requests"]}
    used = [int(x["id"][3:]) for x in doc["requests"] if re.fullmatch(r"RQ-\d{2,3}", x.get("id", ""))]
    nxt = max(used, default=0) + 1
    added = []
    for it in items:
        if (it["key"], it["_raised_by_unit"]) in have:
            continue
        it = {"id": f"RQ-{nxt:03d}", **it}
        nxt += 1
        doc["requests"].append(it)
        added.append(it["id"])
    tmp = REQ + ".tmp-MD-NV"
    json.dump(doc, open(tmp, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    os.replace(tmp, REQ)
finally:
    os.close(fd)
    os.remove(LOCK)
json.dump(added, open(os.path.join(SCR, "request_ids.json"), "w"), indent=0)
print("added", len(added), added[:1], added[-1:], "total", len(doc["requests"]))

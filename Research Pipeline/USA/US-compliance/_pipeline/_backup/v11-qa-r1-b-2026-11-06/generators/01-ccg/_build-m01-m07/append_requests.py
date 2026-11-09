# -*- coding: utf-8 -*-
"""Append the m01..m07 builder's research requests to the shared _research/CCG-research-request.json.
Re-reads the file immediately before writing (parallel builders append too); skips a key already requested
by this builder for the same unit (idempotent re-runs)."""
import glob
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", ".."))
P = os.path.join(BASE, "_research", "CCG-research-request.json")

gaps = []
for f in sorted(glob.glob(os.path.join(HERE, "state", "*.state.json"))):
    gaps += json.load(open(f, encoding="utf-8"))["gaps"]

d = json.load(open(P, encoding="utf-8")) if os.path.exists(P) else {
    "schema_version": "1.4.0", "artifact": "CCG", "requested_by": "artifact-builder", "round": 1,
    "created_on": "2026-11-02", "requests": []}
existing = {(r.get("_unit"), r["key"]) for r in d["requests"]}
nums = [int(r["id"].split("-")[1]) for r in d["requests"]]
n = max(nums) if nums else 0
added = []
for g in gaps:
    if (g["unit"], g["key"]) in existing:
        continue
    n += 1
    locs = [g["loc"]] + g.get("more_locs", [])
    r = {"id": f"RQ-{n:03d}", "key": g["key"],
         "location": f"01-ccg/modules/{g['unit']}.md!{g['loc'].replace('!', '')[:150]}",
         "question": g["question"], "why_blocking": g["why_blocking"], "domain": g["domain"],
         "acceptable_tier": g["tier"],
         "attempted_by_requester": g["attempted"] or [f"_research/CCG-{g['unit']}-facts.json and all CCG-annex_*-facts.json (key search)",
                                                       "_research/CCG-research-pack.md"],
         "severity": g["severity"], "_unit": g["unit"], "_blocking": g["blocking"],
         "_placeholder_written": f"⚠️ RESEARCH-GAP ({'blocking' if g['blocking'] else 'non-blocking'}) at " + "; ".join(locs)}
    if g.get("shape"):
        r["expected_shape"] = g["shape"]
    d["requests"].append(r)
    added.append((r["id"], r["key"], g["unit"], g["blocking"]))
json.dump(d, open(P, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
for a in added:
    print(*a)
print("appended", len(added), "total", len(d["requests"]))

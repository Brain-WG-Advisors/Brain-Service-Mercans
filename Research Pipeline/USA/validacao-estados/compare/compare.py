"""compare.py - ours.py vs oracle results.json, per case and per line, tolerance 0.01.
Writes compare.json and prints the per-state table. Lines the oracle marks as pending
(futa_credit_reduction_er_pending) are listed but not counted in the % (both sides await DOL 2026-11-10)."""
import json, os, sys
from collections import OrderedDict
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import ours

OR = os.path.normpath(os.path.join(HERE, "..", "oracle"))
cases = json.load(open(os.path.join(OR, "cases.json"), encoding="utf-8"))
res = {r["id"]: r for r in json.load(open(os.path.join(OR, "results.json"), encoding="utf-8"))}
TOL = 0.01
EXCLUDED = {"futa_credit_reduction_er_pending"}

rows = []; per_state = OrderedDict()
for c in cases:
    o = res[c["id"]]; me = ours.calc(c)
    for line, ov in o["lines"].items():
        mv = me["lines"].get(line, "MISSING")
        if line in EXCLUDED:
            status = "EXCLUDED_PENDING"
        elif mv is None or mv == "MISSING":
            status = "NOT_COMPUTABLE"
        else:
            status = "MATCH" if abs(mv - ov) <= TOL + 1e-9 else "MISMATCH"
        rows.append({"case": c["id"], "state": c["state"], "line": line, "oracle": ov,
                     "ours": None if mv in (None, "MISSING") else round(mv, 6),
                     "diff": None if mv in (None, "MISSING") else round(mv - ov, 6),
                     "status": status, "oracle_flags": o.get("flags", []),
                     "trace": me["trace"].get(line, []), "research_silent": me["silent"]})
        s = per_state.setdefault(c["state"], {"compared": 0, "match": 0, "mismatch": 0, "not_computable": 0, "excluded": 0})
        if status == "EXCLUDED_PENDING": s["excluded"] += 1; continue
        s["compared"] += 1
        s["match"] += status == "MATCH"
        s["mismatch"] += status == "MISMATCH"
        s["not_computable"] += status == "NOT_COMPUTABLE"
for s in per_state.values():
    s["pct"] = round(100.0 * s["match"] / s["compared"], 2)
tot = {k: sum(v[k] for v in per_state.values()) for k in ("compared", "match", "mismatch", "not_computable", "excluded")}
tot["pct"] = round(100.0 * tot["match"] / tot["compared"], 2)
json.dump({"tolerance": TOL, "per_state": per_state, "total": tot, "rows": rows},
          open(os.path.join(HERE, "compare.json"), "w", encoding="utf-8"), indent=1)
print("| State | Lines compared | Matching | Mismatch | Not computable | % | Excluded (pending) |")
print("|---|---|---|---|---|---|---|")
for k, v in per_state.items():
    print(f"| {k} | {v['compared']} | {v['match']} | {v['mismatch']} | {v['not_computable']} | {v['pct']} | {v['excluded']} |")
print(f"| **Total** | {tot['compared']} | {tot['match']} | {tot['mismatch']} | {tot['not_computable']} | {tot['pct']} | {tot['excluded']} |")
if "-v" in sys.argv:
    for r in rows:
        if r["status"] in ("MISMATCH", "NOT_COMPUTABLE"):
            print(r["case"], r["line"], "oracle", r["oracle"], "ours", r["ours"], "diff", r["diff"], r["status"])

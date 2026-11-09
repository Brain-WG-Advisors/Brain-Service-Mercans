# -*- coding: utf-8 -*-
"""Build gap_text_map.json: round-1 RESEARCH-GAP marker text -> RQ id.

gaps.json locations carry round-1 line numbers (annex_XX.md!XX.n!L44). Most markers name
their key, so ccg_common.tag_gaps() maps them by (unit, key). The rest (e.g. FED-CT markers
written with a humanised key) are mapped through the normalised marker text read at the
round-1 line. Run once against a copy of the round-1 units:

usage: python build_gap_text_map.py <dir holding round-1 modules/ and annexes/>
"""
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ccg_common as C  # noqa: E402

R1 = sys.argv[1]
out, stats = {}, {"mapped": 0, "key_in_text": 0, "no_marker_at_line": 0}
for g in C.GAPS:
    m = re.match(r"01-ccg/(modules|annexes)/([^!]+)!.*!L(\d+)$", g.get("location") or "")
    if not m:
        continue
    d, unit, ln = m.group(1), m.group(2), int(m.group(3))
    p = os.path.join(R1, d, unit)
    if not os.path.exists(p):
        p = os.path.join(R1, "modules" if d == "annexes" else "annexes", unit)
    lines = open(p, encoding="utf-8").read().split("\n")
    if ln > len(lines) or "RESEARCH-GAP" not in lines[ln - 1]:
        stats["no_marker_at_line"] += 1
        continue
    line = lines[ln - 1]
    for s, e in C._segments(line):
        seg = line[s:e]
        if g["key"] in seg:
            stats["key_in_text"] += 1
            continue
        out.setdefault(unit, {})[C.norm_marker(seg)] = g["id"]
        stats["mapped"] += 1
json.dump(out, open(os.path.join(C.HERE, "gap_text_map.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(stats)

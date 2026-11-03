# -*- coding: utf-8 -*-
"""Percent-aware C46 scan of the CCG units (QA r1 finding 42).

The shared C46 treats a rate as a percentage only when the stored value is < 1; US facts store
rates in percent (6.2, not 0.062), so untagged percentages are never detected. This scan reads
every unit .md, strips [[FACT:]]/[[GAP:]] tags, and lists each number written as a percentage
(N%, N %, N percent) whose value equals a fact whose unit_of_measure is percent (or whose key
names a rate), with candidate keys (same jurisdiction first).

usage: python percent_scan.py [--json out.json]
"""
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
TAG = re.compile(r"\[\[(?:FACT|GAP):[^\]]*\]\]")
PCT = re.compile(r"(?<![\w.,/])(\d{1,3}(?:\.\d+)?)\s?(%|percent\b)")

pfacts = {}
for fp in glob.glob(os.path.join(BASE, "_research", "*-facts.json")):
    for f in json.load(open(fp, encoding="utf-8")).get("facts", []):
        v = f.get("value")
        if isinstance(v, bool) or not isinstance(v, (int, float)):
            continue
        is_pct = f.get("unit_of_measure") == "percent" or re.search(r"(^|\.)(rate|percent|pct)(\.|_|$)", f["key"])
        if not is_pct:
            continue
        pfacts.setdefault(round(float(v), 6), set()).add(f["key"])


def scan(path):
    unit = os.path.basename(path)
    jur = None
    m = re.match(r"annex_([A-Z]+)\.md", unit)
    if m:
        jur = m.group(1).lower()
    hits = []
    for i, ln in enumerate(open(path, encoding="utf-8").read().split("\n"), 1):
        if ln.startswith("#"):
            continue
        bare = TAG.sub(lambda mm: " " * len(mm.group(0)), ln)
        for mm in PCT.finditer(bare):
            n = float(mm.group(1))
            if n == 0:
                continue
            keys = pfacts.get(round(n, 6))
            if not keys:
                continue
            same = sorted(k for k in keys if jur and k.split(".")[0] == jur)
            hits.append({"unit": unit, "line": i, "text": mm.group(0), "value": n,
                         "same_jur_keys": same, "keys": sorted(keys)[:6],
                         "context": ln[max(0, mm.start() - 90): mm.end() + 60]})
    return hits


if __name__ == "__main__":
    allh = []
    for d in ("modules", "annexes"):
        for p in sorted(glob.glob(os.path.join(BASE, "01-ccg", d, "*.md"))):
            allh += scan(p)
    if "--json" in sys.argv:
        json.dump(allh, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(len(allh), "untagged percentages equal to a percent fact")
    for h in allh:
        print(f"{h['unit']}:{h['line']} {h['text']!r} same={h['same_jur_keys'][:3]} any={h['keys'][:3]} :: {h['context']}")

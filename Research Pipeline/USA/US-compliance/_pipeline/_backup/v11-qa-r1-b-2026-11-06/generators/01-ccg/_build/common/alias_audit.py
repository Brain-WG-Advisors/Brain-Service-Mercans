# -*- coding: utf-8 -*-
"""Round-2 audit of fix 1: old (alias) keys left in the CCG units, and tags re-pointed vs a round-1 copy.
usage: python alias_audit.py [<round-1 units dir with modules/ and annexes/>]"""
import collections
import csv
import glob
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
rows = list(csv.DictReader(open(os.path.join(BASE, "_research", "qa-r1-fix", "KEY-ALIAS-MAP.csv"), encoding="utf-8")))
olds = {r["old_key"]: r["canonical_key"] for r in rows}
pat = re.compile(r"(?<![A-Za-z0-9_.])(" + "|".join(re.escape(o) for o in sorted(olds, key=len, reverse=True))
                 + r")(?![A-Za-z0-9_]|\.[A-Za-z0-9_])")
units = glob.glob(os.path.join(BASE, "01-ccg", "modules", "*.md")) + glob.glob(os.path.join(BASE, "01-ccg", "annexes", "*.md"))
hits = collections.Counter()
for f in units:
    for m in pat.finditer(open(f, encoding="utf-8").read()):
        hits[(os.path.basename(f), m.group(1))] += 1
print("old keys still written in r2 units:", sum(hits.values()), hits.most_common(10))
TAG = re.compile(r"\[\[FACT:([a-z0-9_.]+)=")
if len(sys.argv) > 1:
    r1 = collections.Counter()
    for f in glob.glob(os.path.join(sys.argv[1], "*", "*.md")):
        for m in TAG.finditer(open(f, encoding="utf-8").read()):
            if m.group(1) in olds:
                r1[m.group(1)] += 1
    print("round-1 tags on old keys:", sum(r1.values()), "distinct keys:", len(r1))
r2 = collections.Counter()
for f in units:
    for m in TAG.finditer(open(f, encoding="utf-8").read()):
        if m.group(1) in olds:
            r2[m.group(1)] += 1
print("round-2 tags on old keys:", sum(r2.values()))

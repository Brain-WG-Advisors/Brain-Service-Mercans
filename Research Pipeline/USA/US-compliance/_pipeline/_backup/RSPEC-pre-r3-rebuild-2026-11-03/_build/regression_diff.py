"""Regression guard: cell-by-cell diff of two folders of *-Spec.xlsx (old vs new).
usage: python rsdiff.py <old_dir> <new_dir> [--detail <file-substring>] [--json out]"""
import glob
import json
import os
import re
import sys
from openpyxl import load_workbook

old_d, new_d = sys.argv[1], sys.argv[2]
detail = sys.argv[sys.argv.index("--detail") + 1] if "--detail" in sys.argv else None
TAG = re.compile(r"\[\[FACT:\s*([A-Za-z0-9_.]+)\s*=")
GAP = re.compile(r"\[\[GAP:([^\]]+)\]\]")


def cells(p):
    wb = load_workbook(p)
    out = {}
    for ws in wb.worksheets:
        for row in ws.iter_rows():
            for c in row:
                if c.value is not None:
                    out[(ws.title, c.coordinate)] = c.value
    return out, {ws.title: (ws.max_row, ws.max_column) for ws in wb.worksheets}


rep = {}
for p in sorted(glob.glob(os.path.join(new_d, "*-Spec.xlsx"))):
    name = os.path.basename(p)
    q = os.path.join(old_d, name)
    a, da = cells(q)
    b, db = cells(p)
    changed = [k for k in set(a) | set(b) if a.get(k) != b.get(k)]
    by_sheet = {}
    for s, c in changed:
        by_sheet[s] = by_sheet.get(s, 0) + 1
    ta = set(TAG.findall(" ".join(str(v) for v in a.values())))
    tb = set(TAG.findall(" ".join(str(v) for v in b.values())))
    ga = set(GAP.findall(" ".join(str(v) for v in a.values())))
    gb = set(GAP.findall(" ".join(str(v) for v in b.values())))
    rep[name] = {"changed_cells": len(changed), "by_sheet": by_sheet, "dims_old": da, "dims_new": db,
                 "keys_added": sorted(tb - ta), "keys_removed": sorted(ta - tb),
                 "gaps_added": sorted(gb - ga), "gaps_removed": sorted(ga - gb)}
    if detail and detail in name:
        for k in sorted(changed)[:400]:
            print(k, "\n   OLD:", str(a.get(k))[:300], "\n   NEW:", str(b.get(k))[:300])
sys.stdout.reconfigure(encoding="utf-8")
for n, r in rep.items():
    print(n, r["changed_cells"], r["by_sheet"], "keys+", len(r["keys_added"]), "keys-", r["keys_removed"],
          "gaps+", r["gaps_added"], "gaps-", r["gaps_removed"])
if "--json" in sys.argv:
    json.dump(rep, open(sys.argv[sys.argv.index("--json") + 1], "w", encoding="utf-8"), indent=1, ensure_ascii=False)

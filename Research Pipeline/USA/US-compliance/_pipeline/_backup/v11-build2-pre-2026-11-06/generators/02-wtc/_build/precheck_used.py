# -*- coding: utf-8 -*-
"""Facts used in the catalogue that carry _figure_located (re-pointed rows) or _precheck_unmatched (our gloss): list for the build log."""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import wtc_common as W  # noqa: E402

used = set()
for r in csv.DictReader(open(os.path.join(W.BASE, "_pipeline", "WTC-bindings.csv"), encoding="utf-8")):
    used.add(r["key"])
out = []
for k in sorted(used):
    for f in W.C.FACTS[k]:
        if f.get("_figure_located"):
            out.append(("LOCATED", k, f["register_id"], f["_figure_located"][:400]))
        if f.get("_precheck_unmatched"):
            out.append(("UNMATCHED", k, f["register_id"], ",".join(f["_precheck_unmatched"])))
sys.stdout.reconfigure(encoding="utf-8")
for o in out:
    print(" | ".join(o))
print(len(out))

# -*- coding: utf-8 -*-
"""CO v1.1 alignment patch - STEP 1: DD field-note cross-references (C16/F13)."""
import json, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_lib import replace_literal

HERE = os.path.dirname(os.path.abspath(__file__))
DD = os.path.abspath(os.path.join(HERE, "..", "..", "05-data-dictionary"))
canon = json.load(open(os.path.join(HERE, "xref_canonical.json"), encoding="utf-8"))

# Details worth preserving that the canonical clause would drop.
KEEP = {
    "ID|5":  " The nomina electronica code list is Anexo Tecnico table 5.2.1.",
    "ID|6":  " Field widths differ by artefact: A(16) space-filled on PILA, N(16) zero-filled on"
             " the cesantias deposit file.",
    "CF|23": " On PILA the field is mandatory where the ING novedad is marked.",
}

pairs = {}
for key, v in canon.items():
    old, new = v["old"], v["new"]
    if old == new:
        continue
    pairs[old] = new + KEEP.get(key, "")

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

lookup = {norm(o): (o, n) for o, n in pairs.items()}
applied = set()

def transform(val):
    nv = norm(val)
    for k, (o, n) in lookup.items():
        if nv.startswith(k):
            applied.add(k)
            return norm(n) + nv[len(k):]
    return val

total = 0
for fn in ("co_dd_data_employee.py", "co_dd_data_employment.py", "co_dd_data_employer.py"):
    p = os.path.join(DD, fn)
    src = open(p, encoding="utf-8").read()
    new, n = replace_literal(src, lambda v: v.lstrip().startswith("Spec ref:"), transform)
    if n:
        open(p, "w", encoding="utf-8").write(new)
    print("%-28s %d note(s) rewritten" % (fn, n))
    total += n

print("TOTAL rewritten:", total, "of", len(pairs), "candidates")
missed = [lookup[k][0][:90] for k in lookup if k not in applied]
if missed:
    print("NOT APPLIED (%d):" % len(missed))
    for m in missed:
        print("   ", m)

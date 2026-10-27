# -*- coding: utf-8 -*-
"""CO v1.1 alignment patch - STEP 1b: the two DD field notes whose 'Spec ref'
clause is not in the standard shape and so was not rewritten automatically.

ID r17 Employer NIT Verification Digit - named the artefacts in prose only
       ("all four DIAN artefacts") and cited A1-004 alone.
ID r18 Employer Document Type - cited CO-PILA-003 A1-001, which is
       'Employer name or corporate name'; the document type is A1-002 (and
       T2R1-005). The same note then cited A1-002 for Company.Document_Number,
       which is A1-003.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_lib import replace_literal

HERE = os.path.dirname(os.path.abspath(__file__))
DD = os.path.abspath(os.path.join(HERE, "..", "..", "05-data-dictionary"))
P = os.path.join(DD, "co_dd_data_employer.py")

EDITS = [
    ("Spec ref: Company.NIT_DV - all four DIAN artefacts plus CO-PILA-003 (A1-004).",
     "Spec ref: Company.NIT_DV - CO-DIAN-001 (NIE034, Mandatory=Y), CO-DIAN-002 (casilla 6, "
     "Mandatory=Y), CO-PILA-003 (A1-004 and T2R1-007, Mandatory=C/Y), CO-DIAN-004 (casilla 6, "
     "Mandatory=Y)."),

    ("Spec ref: Company.Document_Type (CO-PILA-003 A1-001, Mandatory=Y) and the composite",
     "Spec ref: Company.Document_Type - CO-PILA-003 (A1-002 and T2R1-005, Mandatory=Y) and "
     "CO-CESANTIAS-006 (E01, Mandatory=Y), the latter as the composite"),

    ("Company.Document_Number (CO-PILA-003 A1-002, A(16)) is NOT a separate master-data field",
     "Company.Document_Number (CO-PILA-003 A1-003 and T2R1-006, A(16)) is NOT a separate "
     "master-data field"),
]

done = []


def transform(val):
    for i, (old, new) in enumerate(EDITS):
        if old in val:
            val = val.replace(old, new, 1)
            done.append(i)
    return val


src = open(P, encoding="utf-8").read()
new, n = replace_literal(src, lambda v: v.lstrip().startswith("Spec ref:"), transform)
missing = [i for i in range(len(EDITS)) if i not in done]
assert not missing, "not applied: %s" % [EDITS[i][0][:60] for i in missing]
open(P, "w", encoding="utf-8").write(new)
print("co_dd_data_employer.py: %d note(s) rewritten, %d edit(s) applied" % (n, len(done)))

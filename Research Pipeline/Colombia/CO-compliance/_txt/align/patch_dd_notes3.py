# -*- coding: utf-8 -*-
"""CO v1.1 alignment patch - STEP 1c: the last three DD field notes whose
'Spec ref' clause names artefacts in prose rather than by field ID.

CF r6  Employee Second Surname       - "all four per-employee artefacts", no IDs.
CF r20 Place of Work Municipality    - cited CO-DIAN-001 NIE053, which is
                                       LugarTrabajoDireccion (the work ADDRESS);
                                       the municipality is NIE052.
CF r85 Employer Municipality Code    - "(CO-DIAN-001)" with no field ID at all.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_lib import replace_literal

HERE = os.path.dirname(os.path.abspath(__file__))
DD = os.path.abspath(os.path.join(HERE, "..", "..", "05-data-dictionary"))

EDITS = {
    "co_dd_data_employee.py": [
        ("Spec ref: Employee.Second_Surname - all four per-employee artefacts.",
         "Spec ref: Employee.Second_Surname - CO-DIAN-001 (NIE047, Mandatory=Y), CO-PILA-003 "
         "(T2R2-012, Mandatory=Y), CO-DIAN-004 (casilla 27, Mandatory=Y), CO-CESANTIAS-006 "
         "(T06, Mandatory=Y)."),

        ("Spec ref: Employee.Work_Municipality_Code (CO-DIAN-001 NIE053; CO-PILA-003 T2R2-010).",
         "Spec ref: Employee.Work_Municipality_Code - CO-DIAN-001 (NIE052, Mandatory=Y), "
         "CO-PILA-003 (T2R2-010, Mandatory=C)."),
    ],
    "co_dd_data_employer.py": [
        ("Spec ref: Company.Municipality_Code (CO-DIAN-001) and Company.City_Code "
         "(CO-DIAN-004 'Lugar donde se practicó la retención', CO-PILA-003).",
         "Spec ref: Company.Municipality_Code - CO-DIAN-001 (NIE015 generation municipality and "
         "NIE037 employer municipality, Mandatory=Y); and Company.City_Code - CO-PILA-003 "
         "(A1-012, Mandatory=Y) and CO-DIAN-004 (casilla 35 'Lugar donde se practico la "
         "retencion', Mandatory=Y)."),
    ],
}

for fn, edits in EDITS.items():
    p = os.path.join(DD, fn)
    src = open(p, encoding="utf-8").read()
    done = []

    def transform(val, _edits=edits, _done=done):
        for i, (old, new) in enumerate(_edits):
            if old in val:
                val = val.replace(old, new, 1)
                _done.append(i)
        return val

    new, n = replace_literal(src, lambda v: v.lstrip().startswith("Spec ref:"), transform)
    missing = [i for i in range(len(edits)) if i not in done]
    assert not missing, "%s: not applied %s" % (fn, [edits[i][0][:60] for i in missing])
    open(p, "w", encoding="utf-8").write(new)
    print("%-26s %d note(s) rewritten, %d edit(s)" % (fn, n, len(done)))

# -*- coding: utf-8 -*-
"""CO v1.1 alignment patch - STEP 2: DD Country Option Mappers (CHECK 1 / F1).

Fixes, each traced to an authoritative source:

 1. Worker Type - code 40 "Beneficiario UPC adicional" REMOVED. It is absent from
    DIAN Anexo Tecnico (Res. 000013 de 2021) table 5.5.3, which admits exactly
    sixteen codes: 01 02 04 12 18 19 21 22 23 30 31 47 51 54 56 58. It is a
    PILA-only tipo cotizante for a health-coverage beneficiary, not an employee,
    and the mapper drives Employee.Worker_Type_Code -> NIE041, a table-5.5.3
    code. Added to the mapper's excluded-code list with the reason.
 2. Employee Document Type - code 47 Abbreviation "PE" -> "PEP", verbatim from
    Anexo table 5.2.1. The PILA/SOI two-letter equivalent is recorded in the
    Constraint / Notes instead, and now has its own mapper (fix 4).
 3. Worker Sub-Type - the HARD RULE aligned to the PILA anexo statutory list
    (1, 2, 3, 4, 5, 6, 9, 12) with the in-scope subset named separately, and the
    dual-catalogue warning made explicit (table 5.5.4 admits only 00 and 01).
 4. NEW mapper "Employee Document Type (PILA / Cesantias)" - the two-letter
    catalogue verified against PILA Anexo Tecnico 2 (AT2 v09) campo 3 of Registro
    Tipo 2: CC CE TI PA CD SC RC PE, plus PT printed in the cesantias XLS layout
    only. Closes the gap where CD and SC were named as valid in the numeric
    mapper's constraint (b) but had no row, and gives PILA T2R2-003 / T2R2-074
    and CO-CESANTIAS-006 T03 a complete code table.
 5. Cross-reference corrections in mapper Notes (same C16 defect class as the
    field notes): NIE055->NIE041, NIE056->NIE042, NIE059->NIE061, NIE060->NIE029,
    A1-001->A1-002 and T2R1-005, A1-017->A1-020, A1-032->A1-030 and T2R1-021,
    CO-CESANTIAS-006 T02->T09.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from patch_lib import replace_literal

HERE = os.path.dirname(os.path.abspath(__file__))
DD = os.path.abspath(os.path.join(HERE, "..", "..", "05-data-dictionary"))
P = os.path.join(DD, "co_dd_data_mappers.py")
src = open(P, encoding="utf-8").read()

# ---------------------------------------------------------------- fix 1 --
UPC = re.compile(
    r'\n\s*\("40", "UPC", "Beneficiario UPC adicional",\n(?:\s*"[^"]*"\n?)+?\s*\),',
    re.S)
src, n = UPC.subn("", src, count=1)
assert n == 1, "Worker Type code 40 block not found"
print("fix 1  Worker Type code 40 removed")

# ---------------------------------------------------------------- fix 2 --
old47 = '("47", "PE", "PEP - Permiso Especial de Permanencia",'
new47 = '("47", "PEP", "PEP - Permiso Especial de Permanencia",'
assert src.count(old47) == 1
src = src.replace(old47, new47)
print("fix 2  Employee Document Type code 47 abbreviation PE -> PEP")

# ------------------------------------------------- fixes 3 and 5 (notes) --
NOTE_EDITS = [
    # (marker that identifies the note, old fragment, new fragment)
    ("Referenced by Employee Document Type",
     "PILA and the severance-savings deposit file use the two-letter equivalent given in the "
     "Abbreviation column.",
     "PILA and the severance-savings deposit file use a SEPARATE two-letter catalogue, which now "
     "has its own mapper - see 'Employee Document Type (PILA / Cesantias)'. The letter equivalents "
     "are 11=RC, 12=TI, 13=CC, 21=TE, 22=CE, 41=PA and 47=PE; codes 31, 42, 50 and 91 have no "
     "PILA equivalent, and PILA codes CD, SC and PT have no DIAN numeric equivalent."),

    ("Referenced by Employer Document Type",
     "CO-PILA-003 A1-001",
     "CO-PILA-003 A1-002 and T2R1-005"),

    ("Referenced by Legal Representative Document Type",
     "CO-PILA-003 A1-017",
     "CO-PILA-003 A1-020"),

    ("Referenced by Contract Type",
     "CO-DIAN-001 NIE059",
     "CO-DIAN-001 NIE061"),

    ("Referenced by Worker Type",
     "CO-DIAN-001 NIE055 table 5.5.3",
     "CO-DIAN-001 NIE041 table 5.5.3"),

    ("Referenced by Worker Type",
     "and every "
     "independent-worker, pensioner-paid-by-fund, councillor, taxi-driver and UGPP code (03, 16, "
     "32-36, 42-45, 52, 53, 55, 57, 59-63).",
     "40 (beneficiario de UPC adicional) - a health-coverage beneficiary of a "
     "contributor, not an employee, absent from table 5.5.3 altogether and excluded from the PILA "
     "header contributor count; and every independent-worker, pensioner-paid-by-fund, councillor, "
     "taxi-driver and UGPP code (03, 16, 32-36, 42-45, 52, 53, 55, 57, 59-63). The nine codes "
     "retained here are a strict subset of Anexo Tecnico table 5.5.3, so every value is valid in "
     "both the nomina electronica XML and PILA."),

    ("Referenced by Worker Sub-Type",
     "CO-DIAN-001 NIE056 table 5.5.4",
     "CO-DIAN-001 NIE042 table 5.5.4"),

    ("Referenced by Worker Sub-Type",
     "HARD RULE: where the sub-type is 01, 03, 04, 05, 06 or 09 the PILA pension-"
     "contribution rate field MUST be 0.",
     "HARD RULE (PILA Anexo Tecnico 2): where the sub-type is 1, 2, 3, 4, 5, 6, 9 or 12 the PILA "
     "pension-contribution rate field T2R2-046 MUST be 0; of those, 01, 03, 04, 05, 06 and 09 are "
     "in scope here and 02 and 12 are excluded populations. CODE WIDTH TRAP: PILA writes the "
     "sub-type as a single digit (0, 1, 3...) while the nomina electronica table 5.5.4 writes two "
     "(00, 01); the master value is stored zero-filled to two positions and narrowed on output.",),

    ("Referenced by Pay Frequency",
     "CO-DIAN-001 NIE060",
     "CO-DIAN-001 NIE029"),

    ("Referenced by Contributor Type",
     "CO-PILA-003 A1-032",
     "CO-PILA-003 A1-030 and T2R1-021"),

    ("Referenced by Severance-Savings Fund",
     "CO-CESANTIAS-006 T02",
     "CO-CESANTIAS-006 T09"),
]


def make_transform():
    done = []

    def transform(val):
        for i, edit in enumerate(NOTE_EDITS):
            marker, old, new = (edit + ("",))[:3] if len(edit) == 3 else (
                edit[0], edit[1], edit[2])
            if not val.startswith(marker):
                continue
            if old not in val:
                continue
            val = val.replace(old, new, 1)
            done.append(i)
        return val

    return transform, done


tf, done = make_transform()
src, n = replace_literal(src, lambda v: v.startswith("Referenced by "), tf)
missing = [i for i in range(len(NOTE_EDITS)) if i not in done]
assert not missing, "note edits not applied: %s" % [NOTE_EDITS[i][0] for i in missing]
print("fixes 3+5  %d mapper notes rewritten (%d edits)" % (n, len(done)))

# ---------------------------------------------------------------- fix 4 --
NEW_MAPPER = '''
    ("Employee Document Type (PILA / Cesantias)",
     "Referenced by Employee Document Type on the SOCIAL-SECURITY channel - CO-PILA-003 (T2R2-003 "
     "'Tipo documento del cotizante' and T2R2-074, Mandatory=Y/C) and CO-CESANTIAS-006 (T03, "
     "Mandatory=Y). SECOND CODE SYSTEM FOR ONE MASTER VALUE: the same Employee Document Type master "
     "field is emitted as the DIAN numeric code on DIAN artefacts and as the two-letter code below "
     "on PILA and the severance-savings deposit file. Source: PILA Anexo Tecnico 2 (AT2 version 09, "
     "16-09-2019), Registro Tipo 2 campo 3 - the eight values CC, CE, TI, PA, CD, SC, RC and PE, "
     "verbatim. CONSTRAINTS: (a) only PA and CD may be alphanumeric; TI, CC, SC, RC, CE and PE must "
     "be all digits; (b) a PE (PEP) number must be EXACTLY 15 digits (SOI hard rule); (c) where the "
     "Foreign National Not Liable to Pension flag is set only CE, PA, CD, SC and PE are valid; (d) "
     "the Colombian Abroad flag may be used only with CC or TI; (e) NI is an EMPLOYER document type "
     "and is NOT valid for a contributor; (f) for a legal representative only CC, CE, PA and CD are "
     "available - see 'Legal Representative Document Type'. CO-GAP-06 remains open: PT exists in "
     "the cesantias XLS layout but not in the DIAN numeric catalogue, where 47 (PEP) is the only "
     "proxy.",
     [
        ("CC", "13", "Cedula de ciudadania",
         "Colombian national identity card. DIAN numeric equivalent 13. The default for nationals "
         "aged 18 and over. Numeric only."),
        ("CE", "22", "Cedula de extranjeria",
         "Foreign resident's identity card issued by Migracion Colombia. DIAN numeric equivalent "
         "22. Numeric only."),
        ("TI", "12", "Tarjeta de identidad",
         "Identity card for a person aged 7 to 17. DIAN numeric equivalent 12. Numeric only. "
         "Converts to CC on majority, changing the composite key - notify the fund or the deposit "
         "lands on an orphan account."),
        ("PA", "41", "Pasaporte",
         "Passport. DIAN numeric equivalent 41. ALPHANUMERIC permitted on PILA - and this is the "
         "channel difference behind CO-GAP-07, because the nomina electronica types the number as "
         "xsd:integer."),
        ("CD", "-", "Carne diplomatico",
         "Diplomatic card. ALPHANUMERIC permitted. NO DIAN numeric equivalent exists - the "
         "nomina electronica cannot carry this document type at all."),
        ("SC", "-", "Salvoconducto de permanencia",
         "Safe-conduct of stay. Numeric only. NO DIAN numeric equivalent exists."),
        ("RC", "11", "Registro civil de nacimiento",
         "Civil birth registration. DIAN numeric equivalent 11. Valid in the CONTRIBUTOR list but "
         "NOT in the employer list; an under-7 is never an employee, so it is retained for "
         "beneficiary records only."),
        ("PE", "47", "Permiso Especial de Permanencia (PEP)",
         "Special residence permit. DIAN numeric equivalent 47 (abbreviated PEP in Anexo table "
         "5.2.1). Numeric only and EXACTLY 15 digits."),
        ("PT", "-", "Permiso por Proteccion Temporal (PPT)",
         "CESANTIAS XLS LAYOUT ONLY. Printed in the XLS document-type list of the severance-savings "
         "deposit manual; it is absent from the PILA fixed-width list of AT2 version 09 and has no "
         "DIAN numeric equivalent (CO-GAP-06). Do not emit it on PILA or on any DIAN artefact."),
     ]),
'''

anchor = '    ("Employer Document Type",'
assert src.count(anchor) == 1
src = src.replace(anchor, NEW_MAPPER.lstrip("\n") + "\n" + anchor, 1)
print("fix 4  new mapper 'Employee Document Type (PILA / Cesantias)' added")

open(P, "w", encoding="utf-8").write(src)
print("written:", P)

# -*- coding: utf-8 -*-
"""CO v1.1 alignment patch - STEP 4: Version Control bumps on the DD and specs."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SP = os.path.abspath(os.path.join(HERE, "..", "..", "04-reports-spec"))
DD = os.path.abspath(os.path.join(HERE, "..", "..", "05-data-dictionary"))

# ======================================================================
# Specs - one shared v1.1 CHANGE LOG row, emitted on all six workbooks
# ======================================================================
SPEC_DESC = (
    "DD<->SPEC ALIGNMENT PATCH (mandatory pre-audit step). Reconciled this Spec against "
    "05-data-dictionary/CO-DD-001-v1.0.xlsx across the six alignment checks. (1) OPTION MAPPERS: "
    "every Sheet 6 code table compared code by code with the DD Country Option Mappers sheet and "
    "each divergence resolved against the authoritative source - DIAN Anexo Tecnico Res. 000013 de "
    "2021 tables 5.2.1, 5.5.3 and 5.5.4, PILA Anexo Tecnico 2 version 09, and the published "
    "cesantias layouts. (2) COLUMN E 'Payroll Field (Y/N)': Contract.Contractual_Salary is an "
    "AMOUNT and is routed to the Wage Type Catalogue, not the Data Dictionary, so NIE062, "
    "T2R2-040 and T12 now read N and the spec build and the DD build are back in lock-step; "
    "calculated amounts that carried an 'Employee.' System Mapping prefix are retagged 'Payroll.'. "
    "(3) MANDATORY / CONDITIONAL: every Mandatory=C row verified to carry a conditional reason, "
    "and every Data Dictionary cross-reference into this Spec re-derived from the System Mapping "
    "join so the C16 reference is bidirectional and correct. (4) OPTION-VALUE COMPLETENESS: every "
    "column O reference now resolves to a Sheet 6 section; two missing PILA code tables and the "
    "Formato 2276 document-type table were built. (5) COMPOSITE KEYS documented with sub-field "
    "position, length, source and persistence. (6) CODE-PREFIX PATTERNS recorded in column J. "
    "Full record: 07-qa-crosscheck/CO-ALIGNMENT-PATCH.md. | Mercans Compliance")

p = os.path.join(SP, "build_co_specs.py")
src = open(p, encoding="utf-8").read()
OLD = '    ]\n    for ver, desc in log + cfg.get("extra_log", []):'
NEW = ('        ("v1.1 | 2026-09-07 | Issued",\n'
       '         "%s"),\n'
       '    ]\n'
       '    for ver, desc in log + cfg.get("extra_log", []):') % SPEC_DESC
assert src.count(OLD) == 1, "spec change-log anchor not unique"
open(p, "w", encoding="utf-8").write(src.replace(OLD, NEW, 1))
print("build_co_specs.py : v1.1 CHANGE LOG row added (emitted on all six specs)")

# ======================================================================
# Data Dictionary - v1.1 row at line 14 (row 15 stays blank)
# ======================================================================
DD_DESC = (
    "DD<->SPEC ALIGNMENT PATCH (mandatory pre-audit step), reconciling this Data Dictionary with "
    "the six Specs in 04-reports-spec. CROSS-REFERENCES: 49 field rows carried a stale or "
    "incomplete 'Spec ref' citation - a systematic off-by-N drift across the NIE, A1 and T2R "
    "blocks (for example Hire Date cited NIE057, which does not exist; the anexo field is NIE002 "
    "FechaIngreso, and the whole PILA employer block A1-011 to A1-017 was displaced by one). Every "
    "citation is now re-derived from the System Mapping join and states the artefact, the field ID "
    "and the Mandatory flag for each Spec that carries the field. OPTION MAPPERS: Worker Type code "
    "40 (beneficiario de UPC adicional) REMOVED - it is absent from DIAN Anexo Tecnico table 5.5.3 "
    "and is a health-coverage beneficiary rather than an employee, so it could never be a valid "
    "NIE041 value; Employee Document Type code 47 abbreviation corrected to PEP, verbatim from "
    "Anexo table 5.2.1; the Worker Sub-Type hard rule aligned to the PILA statutory list "
    "(1, 2, 3, 4, 5, 6, 9, 12) with the in-scope subset named separately and the code-width trap "
    "recorded. NEW MAPPER 'Employee Document Type (PILA / Cesantias)' carrying the eight "
    "two-letter values of PILA Anexo Tecnico 2 campo 3 (CC, CE, TI, PA, CD, SC, RC, PE) plus the "
    "cesantias-only PT - this closes the contradiction in which CD and SC were named as valid in "
    "the numeric mapper's constraints but had no row, and gives PILA T2R2-003, T2R2-074 and "
    "CO-CESANTIAS-006 T03 a complete code table. Contract.Contractual_Salary remains OUT of the "
    "Data Dictionary as an amount; the deviation is now resolved at source, the spec build having "
    "been corrected to flag it Payroll Field = N, so this is no longer a deviation. "
    "Full record: 07-qa-crosscheck/CO-ALIGNMENT-PATCH.md.")

p = os.path.join(DD, "build_co_dd.py")
src = open(p, encoding="utf-8").read()
OLD = ('    vc["E13"] = "Released"\n'
       '    vc["F13"] = "Mercans Compliance"\n'
       '    for col in ("B", "C", "D", "E", "F"):\n'
       '        vc[col + "14"] = None\n'
       '        vc[col + "15"] = None\n')
NEW = ('    vc["E13"] = "Released"\n'
       '    vc["F13"] = "Mercans Compliance"\n'
       '    vc["B14"] = 1.1\n'
       '    vc["C14"] = datetime(2026, 9, 7)\n'
       '    vc["D14"] = (\n'
       '        "%s"\n'
       '    )\n'
       '    vc["E14"] = "Released"\n'
       '    vc["F14"] = "Mercans Compliance"\n'
       '    for col in ("B", "C", "D", "E", "F"):\n'
       '        vc[col + "15"] = None\n') % DD_DESC
assert src.count(OLD) == 1, "DD version-control anchor not unique"
open(p, "w", encoding="utf-8").write(src.replace(OLD, NEW, 1))
print("build_co_dd.py    : v1.1 Version Control row added")

# The docstring deviation note is now stale - the spec side was corrected.
src = open(p, encoding="utf-8").read()
OLD_DOC = ("ONE DELIBERATE DEVIATION from col-E lock-step, recorded in Version Control and\n"
           "in CO-DD-001-classification.md: Contract.Contractual_Salary (and its December\n"
           "variant) is flagged Payroll Field = Y in the specs but is an AMOUNT, which\n"
           "CLAUDE.md routes to the WTC and not to the Data Dictionary. It is excluded here.\n")
NEW_DOC = ("FULL col-E LOCK-STEP as at v1.1. Contract.Contractual_Salary (and its December\n"
           "variant) is an AMOUNT, which the scope rule routes to the WTC and not to the\n"
           "Data Dictionary, so it is excluded here. Until the v1.1 alignment patch the\n"
           "spec build still flagged it Payroll Field = Y, which made this a deviation;\n"
           "build_co_specs._DD_MASTER_MAPPINGS was corrected, so the two builds now agree\n"
           "and there is no remaining deviation to record.\n")
assert src.count(OLD_DOC) == 1, "DD docstring deviation note not found"
open(p, "w", encoding="utf-8").write(src.replace(OLD_DOC, NEW_DOC, 1))
print("build_co_dd.py    : stale 'deliberate deviation' docstring note updated")

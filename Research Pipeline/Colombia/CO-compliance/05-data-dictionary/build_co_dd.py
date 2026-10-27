#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
build_co_dd.py  -  Colombia Data Dictionary (CO-DD-001-v1.0)

Builds the Colombia Data Dictionary by LOADING the CZ V2.0 template
(shared/CZ_Data_Dictionary_V2_0.xlsx), clearing the Czech data rows and
repopulating with Colombian private-sector master-data fields, while preserving
the template's 8-sheet order, blue/orange header colours, column widths, fonts
and the two ISO reference sheets. Adapted from
CI-compliance/05-data-dictionary/build_ci_dd.py.

Run:  python build_co_dd.py        (use `python`, not `python3`)
Out:  CO-DD-001-v1.0.xlsx  +  CO-DD-001-classification.md

SCOPE - STRICTLY user-input master data (CLAUDE.md). Every field was classified
from the six in-scope report specs (04-reports-spec) by its System Mapping, in
lock-step with the spec build's col-E "Payroll Field (Y/N)" flag
(build_co_specs._DD_MASTER_MAPPINGS):
  Company.* / Employee.* / Contract.*  identifier / name / date / code / flag -> DD
  Calculated amounts and totals, statutory rates, ceilings, UVT and SMMLV
  parameters, authority-generated values, per-payrun transactional data      -> WTC / param / SYS

FULL col-E LOCK-STEP as at v1.1. Contract.Contractual_Salary (and its December
variant) is an AMOUNT, which the scope rule routes to the WTC and not to the
Data Dictionary, so it is excluded here. Until the v1.1 alignment patch the
spec build still flagged it Payroll Field = Y, which made this a deviation;
build_co_specs._DD_MASTER_MAPPINGS was corrected, so the two builds now agree
and there is no remaining deviation to record.

Currency: COP. The DD holds NO amounts.
Private-sector filter: civil servants, military and police, independent workers
and service contractors, domestic workers, community mothers, associated-work
cooperative members and the self-insured are excluded from every option mapper;
excluded codes are named in each mapper's Notes so they are rejected at
validation rather than silently accepted.

Sources: shared/CZ_Data_Dictionary_V2_0.xlsx (format); CO-compliance/
04-reports-spec/*.xlsx (field classification); scope_manifest.json (scope and
option_mapper_scope); 01-ccg/CO-CCG-001-v1.0.docx and 01-ccg/modules/*.md
(master-data groups, identifier formats, calculation drivers).
"""

import os
from copy import copy
from datetime import datetime

import openpyxl
from openpyxl.styles import PatternFill, Font

from co_dd_data_employee import (
    ID_EMPLOYEE, CF_EMPLOYEE_NAME, CF_EMPLOYEE_CONTACT, CF_EMPLOYEE_WORKPLACE,
)
from co_dd_data_employment import (
    CF_EMPLOYEE_EMPLOYMENT, CF_EMPLOYEE_TAX, CF_EMPLOYEE_FAMILY, CF_EMPLOYEE_SOCSEC,
)
from co_dd_data_employer import ID_LEGAL_ENTITY, CF_LEGAL_ENTITY
from co_dd_data_mappers import OPTION_MAPPERS

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
TEMPLATE = os.path.join(ROOT, "shared", "CZ_Data_Dictionary_V2_0.xlsx")
OUTPUT = os.path.join(HERE, "CO-DD-001-v1.0.xlsx")

COUNTRY = "Colombia"

CF_EMPLOYEE = (CF_EMPLOYEE_NAME + CF_EMPLOYEE_CONTACT + CF_EMPLOYEE_WORKPLACE
               + CF_EMPLOYEE_EMPLOYMENT + CF_EMPLOYEE_TAX + CF_EMPLOYEE_FAMILY
               + CF_EMPLOYEE_SOCSEC)

# ---------------------------------------------------------------------------
# STYLE HELPERS
# ---------------------------------------------------------------------------
NO_FILL = PatternFill(fill_type=None)
DEFAULT_FONT = Font()


def snap(cell):
    return (copy(cell.font), copy(cell.fill), copy(cell.alignment), cell.number_format)


def apply_style(cell, s):
    cell.font = copy(s[0])
    cell.fill = copy(s[1])
    cell.alignment = copy(s[2])
    cell.number_format = s[3]


def wipe(ws, r0, r1, c0, c1):
    """Clear values and strip fills/fonts across a rectangular region."""
    for r in range(r0, r1 + 1):
        for c in range(c0, c1 + 1):
            cell = ws.cell(r, c)
            cell.value = None
            cell.fill = NO_FILL
            cell.font = copy(DEFAULT_FONT)


# ---------------------------------------------------------------------------
# BUILD
# ---------------------------------------------------------------------------
def main():
    print("Loading template:", TEMPLATE)
    wb = openpyxl.load_workbook(TEMPLATE)

    # ---- Instructions: change country name only --------------------------
    for sheet in ("Instructions", "Introduction"):
        if sheet in wb.sheetnames:
            ws = wb[sheet]
            for row in ws.iter_rows():
                for cell in row:
                    if isinstance(cell.value, str) and "Czechia" in cell.value:
                        cell.value = cell.value.replace("Czechia", COUNTRY)

    # ---- Version Control -------------------------------------------------
    vc = wb["Version Control"]
    vc["B9"] = COUNTRY
    vc["B13"] = 1.0
    vc["C13"] = datetime(2026, 9, 4)
    vc["D13"] = (
        "Initial version - Colombia Data Dictionary (private-sector master data), fiscal year 2026. "
        "Field set classified from the six in-scope report specifications in 04-reports-spec "
        "(CO-DIAN-001 nomina electronica, CO-DIAN-002 Formulario 350, CO-PILA-003, CO-DIAN-004 "
        "Formulario 220, CO-DIAN-005 Formato 2276, CO-CESANTIAS-006) by System Mapping, in lock-step "
        "with the spec col-E 'Payroll Field (Y/N)' flag (build_co_specs._DD_MASTER_MAPPINGS), and "
        "extended with the calculation-driving master-data groups of CCG Module 2.2 that do not "
        "surface on a filing (working time, withholding procedure, pension regime, concurrent "
        "employer, non-salary pact, work modality). "
        "ONE DELIBERATE DEVIATION from col-E lock-step: Contract.Contractual_Salary is flagged "
        "Payroll Field = Y in the specs but is an AMOUNT and is therefore excluded from the DD and "
        "routed to the Wage Type Catalogue, per the CLAUDE.md scope rule. "
        "Option mappers apply the private-sector filter: civil servants, military and police, "
        "independent workers and service contractors, domestic workers, community mothers, "
        "associated-work cooperative members and the self-insured are excluded, and the excluded "
        "codes are named in each mapper's Notes column so they are rejected at validation. "
        "Codes, lengths and masks are taken from the published Resolucion DIAN 000013 de 2021 "
        "Anexo Tecnico, Resolucion MSPS 2388 de 2016 Anexo Tecnico 2, Resolucion DIAN 000227 de 2025 "
        "and the published severance-deposit layouts; DERIVED items are flagged for RA confirmation "
        "in the Additional Notes."
    )
    vc["E13"] = "Released"
    vc["F13"] = "Mercans Compliance"
    vc["B14"] = 1.1
    vc["C14"] = datetime(2026, 9, 7)
    vc["D14"] = (
        "DD<->SPEC ALIGNMENT PATCH (mandatory pre-audit step), reconciling this Data Dictionary with the six Specs in 04-reports-spec. CROSS-REFERENCES: 49 field rows carried a stale or incomplete 'Spec ref' citation - a systematic off-by-N drift across the NIE, A1 and T2R blocks (for example Hire Date cited NIE057, which does not exist; the anexo field is NIE002 FechaIngreso, and the whole PILA employer block A1-011 to A1-017 was displaced by one). Every citation is now re-derived from the System Mapping join and states the artefact, the field ID and the Mandatory flag for each Spec that carries the field. OPTION MAPPERS: Worker Type code 40 (beneficiario de UPC adicional) REMOVED - it is absent from DIAN Anexo Tecnico table 5.5.3 and is a health-coverage beneficiary rather than an employee, so it could never be a valid NIE041 value; Employee Document Type code 47 abbreviation corrected to PEP, verbatim from Anexo table 5.2.1; the Worker Sub-Type hard rule aligned to the PILA statutory list (1, 2, 3, 4, 5, 6, 9, 12) with the in-scope subset named separately and the code-width trap recorded. NEW MAPPER 'Employee Document Type (PILA / Cesantias)' carrying the eight two-letter values of PILA Anexo Tecnico 2 campo 3 (CC, CE, TI, PA, CD, SC, RC, PE) plus the cesantias-only PT - this closes the contradiction in which CD and SC were named as valid in the numeric mapper's constraints but had no row, and gives PILA T2R2-003, T2R2-074 and CO-CESANTIAS-006 T03 a complete code table. Contract.Contractual_Salary remains OUT of the Data Dictionary as an amount; the deviation is now resolved at source, the spec build having been corrected to flag it Payroll Field = N, so this is no longer a deviation. OPTION-MAPPER ASSIGNMENT (CHECK 1): 'Principal Contributor Document Type' (CO-PILA-003 T2R2-074) was pointed at the mapper 'Employer Document Type', contradicting its own Pre-Defined Format and notes, which both say it takes the PILA two-letter CONTRIBUTOR catalogue. The two lists differ in exactly two places - the employer list carries NI and lacks RC - so the wrong mapper admitted a corporate NIT as a principal contributor's document type and rejected a registro civil, which is precisely the beneficiary case the field exists for. The field now references 'Employee Document Type (PILA / Cesantias)', matching Spec T2R2-074, which points at the same Sheet 6 table as T2R2-003; the employer mapper's own note, which had claimed T2R2-074 as a second referrer, is corrected. This also resolves the orphan-mapper finding for the contributor catalogue added earlier in this patch. CODE-PREFIX PATTERNS (CHECK 6): the seven administradora fields (employer ARL, employee ARL, EPS and EPS transfer, AFP and AFP transfer, CCF) stated only 'A(6) - administradoras catalogue' in Pre-Defined Format while the Specs stated the full six-position prefix pattern; the pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ is now carried on both sides so the two documents describe the same format. The severance-savings fund code is deliberately left at N(2), being a different published catalogue. Full record: 07-qa-crosscheck/CO-ALIGNMENT-PATCH.md."
    )
    vc["E14"] = "Released"
    vc["F14"] = "Mercans Compliance"
    for col in ("B", "C", "D", "E", "F"):
        vc[col + "15"] = None

    # ---- ID Information ---------------------------------------------------
    ws = wb["ID Information"]
    title_st = snap(ws["A2"])
    hdr_txt = [ws.cell(4, c).value for c in range(1, 23)]
    hdr_st = [snap(ws.cell(4, c)) for c in range(1, 23)]
    data_st = [snap(ws.cell(5, c)) for c in range(1, 23)]
    wipe(ws, 2, ws.max_row, 1, 22)

    def write_idinfo_section(start_row, title, rows):
        ws.cell(start_row, 1).value = title
        apply_style(ws.cell(start_row, 1), title_st)
        hrow = start_row + 2
        for c in range(1, 23):
            ws.cell(hrow, c).value = hdr_txt[c - 1]
            apply_style(ws.cell(hrow, c), hdr_st[c - 1])
        r = hrow + 1
        for (name, es, desc, dtype, pre, ftype, fmt, mapper, notes) in rows:
            vals = {1: COUNTRY, 3: name, 5: es, 6: desc, 7: dtype, 8: pre,
                    9: ftype, 10: fmt, 11: mapper, 22: notes}
            for c in range(1, 23):
                apply_style(ws.cell(r, c), data_st[c - 1])
                if c in vals and vals[c] != "":
                    ws.cell(r, c).value = vals[c]
            r += 1
        return r

    next_r = write_idinfo_section(2, "Identification Information", ID_EMPLOYEE)
    write_idinfo_section(next_r + 1, "Country-Specific Legal Entity Fields", ID_LEGAL_ENTITY)

    # ---- Country Fields ---------------------------------------------------
    ws = wb["Country Fields"]
    cf_title_st = snap(ws["B2"])
    cf_hdr_txt = [ws.cell(4, c).value for c in range(2, 24)]   # B..W
    cf_hdr_st = [snap(ws.cell(4, c)) for c in range(2, 24)]
    cf_data_st = [snap(ws.cell(5, c)) for c in range(2, 24)]
    wipe(ws, 2, ws.max_row, 1, 33)

    def write_cf_section(start_row, title, rows):
        ws.cell(start_row, 2).value = title
        apply_style(ws.cell(start_row, 2), cf_title_st)
        hrow = start_row + 2
        for i, c in enumerate(range(2, 24)):
            ws.cell(hrow, c).value = cf_hdr_txt[i]
            apply_style(ws.cell(hrow, c), cf_hdr_st[i])
        r = hrow + 1
        for (name, es, desc, dtype, pre, ftype, fmt, mapper, notes) in rows:
            # B=country C=ord(orange) D=name E=code(orange) F=local G=desc H=dtype
            # I=precond J=ftype K=format L=mapper  M..V orange  W=notes
            vals = {2: COUNTRY, 4: name, 6: es, 7: desc, 8: dtype, 9: pre,
                    10: ftype, 11: fmt, 12: mapper, 23: notes}
            for i, c in enumerate(range(2, 24)):
                apply_style(ws.cell(r, c), cf_data_st[i])
                if c in vals and vals[c] != "":
                    ws.cell(r, c).value = vals[c]
            r += 1
        return r

    next_r = write_cf_section(2, "Country-Specific Fields", CF_EMPLOYEE)
    write_cf_section(next_r + 1, "Country-Specific Legal Entity Fields", CF_LEGAL_ENTITY)

    # ---- Country Option Mappers ------------------------------------------
    ws = wb["Country Option Mappers"]
    om_title_st = snap(ws["B2"])
    om_hdr_st = snap(ws["B4"])
    om_data_st = snap(ws["C5"])
    wipe(ws, 2, ws.max_row, 1, 25)

    ws.cell(2, 2).value = "Country Option Mappers"
    apply_style(ws.cell(2, 2), om_title_st)

    om_headers = ["Option Mapper Description", "Code", "Abbreviation",
                  "Local Name", "English Description", "Constraint / Notes"]
    r = 4
    for (mname, constraint, options) in OPTION_MAPPERS:
        for i, c in enumerate(range(2, 8)):
            ws.cell(r, c).value = om_headers[i]
            apply_style(ws.cell(r, c), om_hdr_st)
        r += 1
        first = True
        for (code, abbr, local, eng) in options:
            for c in range(2, 8):
                apply_style(ws.cell(r, c), om_data_st)
            ws.cell(r, 2).value = mname if first else None
            ws.cell(r, 3).value = code
            ws.cell(r, 4).value = abbr
            ws.cell(r, 5).value = local
            ws.cell(r, 6).value = eng
            ws.cell(r, 7).value = constraint if first else None
            first = False
            r += 1
        r += 1  # blank separator between mapper blocks

    ws.column_dimensions["G"].width = 70

    wb.save(OUTPUT)
    print("Saved:", OUTPUT)
    print("  ID Information       : %d employee + %d legal-entity fields"
          % (len(ID_EMPLOYEE), len(ID_LEGAL_ENTITY)))
    print("  Country Fields       : %d employee + %d legal-entity fields"
          % (len(CF_EMPLOYEE), len(CF_LEGAL_ENTITY)))
    print("  Country Option Mappers: %d mappers, %d codes"
          % (len(OPTION_MAPPERS), sum(len(m[2]) for m in OPTION_MAPPERS)))


if __name__ == "__main__":
    main()

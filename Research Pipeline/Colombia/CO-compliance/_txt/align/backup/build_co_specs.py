#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Colombia (CO) Statutory Report Specifications - SPAIN 9-SHEET STANDARD (v2.4 / v2.7 / v2.8)
===========================================================================================
Builds one field-level Spec workbook per in-scope statutory filing listed in
scope_manifest.json -> authority_filings.in_scope (6 filings):

  CO-DIAN-001      Documento Soporte de Pago de Nomina Electronica   (CO-DIAN-NE-MONTHLY-001)
  CO-DIAN-002      Formulario 350 - Retenciones en la fuente         (CO-DIAN-F350-MONTHLY-002)
  CO-PILA-003      PILA - Aportes seguridad social y parafiscales    (CO-PILA-MONTHLY-003)
  CO-DIAN-004      Formulario 220 - Certificado de ingresos y ret.   (CO-DIAN-F220-ANNUAL-004)
  CO-DIAN-005      Formato 2276 v4 - Informacion exogena             (CO-DIAN-EXO2276-ANNUAL-005)
  CO-CESANTIAS-006 Consignacion anual de cesantias                   (CO-CESANTIAS-DEPOSIT-ANNUAL-006)

Every workbook follows the MANDATORY 9-sheet structure:
  1. Version Control      2. Report Matrix          3. Payroll Scope Summary
  4. <Report> Spec (21 cols A-U)                    5. File Structure
  6. Field Options        7. Population Rules       8. Example Analysis
  9. Sample File

SOURCE STATUS (C19 / failure F14) - Colombia is unusually well sourced.
  PRIMARY, byte/code exact, held in 00-official-sources/pdfs/:
    * AnexoTecnico-NominaElectronica-V1.0.pdf (Res. DIAN 000013 de 2021, 269 pp.)
      -> 195 official NIE / NIAE field codes, XPaths, lengths, cardinality, code
         tables 5.1.1-5.5.8, CUNE algorithm (s.8.1), SoftwareSC (s.8.2),
         TiempoLaborado (s.8.3.1), SOAP contract (s.9), QR contract (s.13.1).
    * Anexo-tecnico-2-2016-pila.pdf (Res. MSPS 2388 de 2016, AT2 v09, 213 pp.)
      -> Archivo Tipo 1 = 34 fields / 567 positions; Archivo Tipo 2 Registro Tipo 1
         = 22 fields / 359 positions; Registro Tipo 2 = 97 fields / 686 positions,
         all with byte-exact Inicial-Final. THIS CLOSES scope_manifest CO-GAP-01.
    * Formulario_350_01082024.pdf (Res. DIAN 000031 de 2024, form design + instructivo)
      -> casillas 1-155 incl. hoja 2 (141-155).
    * Formulario_220_CertificadoIngresosRetenciones.pdf -> casillas 4-82.
    * Resolucion 000227 de 23-09-2025 (Resolucion Unica) art. 1.3.7.1.1
      -> Formato 2276 v4 numerals 1-36 verbatim + Entidad Informante code table
         + art. 1.3.9.1.3 filing calendar.
  DERIVED (no published schema exists):
    * CO-CESANTIAS-006 - each fondo publishes its own layout; the neutral field
      model is derived from Ley 50 de 1990 art. 99 and market practice.

Currency: COP (Colombian peso). Three DIFFERENT rounding conventions coexist and
must never be blended (see each Spec, column P):
  * Nomina electronica XML : 2 decimals, round-half-to-even, tolerance +/-2.00
  * PILA                   : round UP - base to the peso, contribution to the next 100
  * Formulario 350 / 220   : whole pesos; Form 350 to the nearest 1,000 (ET art. 577)

Tax unit (UVT) 2026 = COP 52,374 (Res. DIAN 000238 of 15 Dec 2025).
Minimum wage (SMMLV) 2026 = COP 1,750,905; transport allowance = COP 249,095.
"""

import os
import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))

# -- COLOUR PALETTE (Spain Standard) -----------------------------------------
C_SPEC_HDR  = "FF4472C4"   # Sheet-4 header row: blue, white bold
C_TITLE_BG  = "FF1F4E78"   # dark blue title banners
C_SUBHDR_BG = "FF4BACC6"   # teal (version-control header)
C_SCOPE_HDR = "FF1F4E78"   # dark blue scope header
C_SEC_GREY  = "FFD6DCE4"   # grey section-header rows
C_AMBER     = "FFFFEB9C"   # payroll-populated fields
C_BLUE      = "FFBDD7EE"   # system/technical fields
C_GREEN     = "FFC6EFCE"   # constants / fixed values
C_RED       = "FFFFC7CE"   # not-applicable / excluded
C_ALT       = "FFF2F6FC"   # light zebra
WHITE = "FFFFFFFF"

F_TITLE   = Font(name="Calibri", size=12, bold=True, color=WHITE)
F_HDR     = Font(name="Calibri", size=9,  bold=True, color=WHITE)
F_SECTION = Font(name="Calibri", size=9,  bold=True, color="FF1F4E78")
F_LBL     = Font(name="Calibri", size=9,  bold=True)
F_DATA    = Font(name="Calibri", size=9)
F_MONO    = Font(name="Consolas", size=9)
F_GRN     = Font(name="Calibri", size=9,  bold=True, color="FF006100")
F_RED     = Font(name="Calibri", size=9,  bold=True, color="FF9C0006")

fill = lambda c: PatternFill("solid", fgColor=c)
WRAP   = Alignment(wrap_text=True, vertical="top")
WRAPC  = Alignment(wrap_text=True, vertical="top", horizontal="center")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)
BORDER = Border(*(Side(style="thin", color="FFD9D9D9"),) * 4)

KIND_FILL = {"payroll": C_AMBER, "system": C_BLUE, "const": C_GREEN, "na": C_RED}

# -- SHEET-4 COLUMN DEFINITION (exactly 21 columns A-U) ----------------------
SPEC_HEADERS = [
    "Field Name (EN)", "Field Name (Local ES)", "Record Type", "Field Position",
    "Payroll Field (Y/N)", "Mandatory (Y/N/C)", "Conditional Reason",
    "Position (in file)", "Length", "Format", "Example", "System Mapping",
    "Explanation", "Relevant for Payroll (Y/N)", "Option Values", "Rounding",
    "Negative (Y/N)", "Value Type", "Frequency", "Query to RA", "RA Comments",
]
SPEC_WIDTHS = [30, 32, 18, 14, 9, 9, 34, 26, 8, 20, 24, 30, 78, 11, 26, 26, 8, 14, 14, 34, 24]
assert len(SPEC_HEADERS) == 21 and len(SPEC_WIDTHS) == 21

RA = "Pending RA review"

# Rounding literals - never blend these three conventions
R_XML  = ("2 decimals, round-half-to-even (NTC 3711 / JIS Z 8401); DIAN validation tolerance "
          "+/- 2.00; any residual is carried by the Redondeo element NIE186. Anexo Tecnico s.1.1.1.")
R_PILA = ("Round UP. Contribution base to the whole peso; each contribution value to the next "
          "multiple of 100 (Decreto 1990 de 2016 art. 1).")
R_F350 = ("Whole pesos, then rounded to the nearest 1,000 (ET art. 577) - applies to every money "
          "casilla of the return.")
R_F220 = ("Whole Colombian pesos, approximated to the NEAREST 1,000, exactly as the instructivo "
          "directs. Where a casilla has no value, write ZERO - do not leave it blank.")
R_2276 = "Whole pesos, no decimals, no thousand separators; zero-filled when nil (Res. 227 par. 2)."
R_NONE = "Not an amount - no rounding."

# ---------------------------------------------------------------------------
# col E "Payroll Field (Y/N)" = MASTER-DATA only (failure F3 / DD lock-step).
# E=Y iff the System Mapping (col L) resolves to a Data-Dictionary master-data
# field (a Company.* / Employee.* / Contract.* identifier, name, date, code or
# flag). Calculated amounts and totals, period values, system/sequence values,
# authority/config codes and rates (Mercans.*) and constants are relevant for
# payroll (col N) but are NOT master data, so E=N. Keep in lock-step with the
# 05-Data-Dictionary scope rules when it is built.
# ---------------------------------------------------------------------------
_DD_MASTER_MAPPINGS = {
    # Company / employer master data
    "Company.NIT", "Company.NIT_DV", "Company.Legal_Name", "Company.First_Surname",
    "Company.Second_Surname", "Company.First_Name", "Company.Other_Names",
    "Company.Country_Code", "Company.Department_Code", "Company.Municipality_Code",
    "Company.Address", "Company.Branch_Code", "Company.Branch_Name",
    "Company.Aportante_Class", "Company.Legal_Nature", "Company.Person_Type",
    "Company.Presentation_Form", "Company.City_Code", "Company.Phone",
    "Company.Email", "Company.CIIU_Code", "Company.DIAN_Seccional_Code",
    "Company.ARL_Code", "Company.Risk_Class", "Company.Commercial_Registry_Date",
    "Company.Legal_Rep_ID", "Company.Legal_Rep_ID_DV", "Company.Legal_Rep_ID_Type",
    "Company.Legal_Rep_First_Surname", "Company.Legal_Rep_Second_Surname",
    "Company.Legal_Rep_First_Name", "Company.Legal_Rep_Second_Name",
    "Company.Aportante_Type", "Company.Insolvency_Start_Date", "Company.Action_Type",
    "Company.Trading_Cease_Date", "Company.Department_Code_Registry",
    "Company.Cesantias_Fund_Code", "Company.Document_Type", "Company.Document_Number",
    "Company.Fax", "Company.Exonerated_Flag", "Company.Ley1429_CCF_Flag",
    # Employee master data
    "Employee.Document_Type", "Employee.Document_Number", "Employee.First_Surname",
    "Employee.Second_Surname", "Employee.First_Name", "Employee.Other_Names",
    "Employee.Work_Country_Code", "Employee.Work_Department_Code",
    "Employee.Work_Municipality_Code", "Employee.Work_Address",
    "Employee.Worker_Type_Code", "Employee.Worker_SubType_Code",
    "Employee.High_Risk_Pension_Flag", "Employee.Integral_Salary_Flag",
    "Employee.Internal_Code", "Employee.Tax_Residence_Flag",
    "Employee.Foreign_Not_Pension_Liable_Flag", "Employee.Colombian_Abroad_Flag",
    "Employee.Bank_Name", "Employee.Bank_Account_Type", "Employee.Bank_Account_Number",
    "Employee.AFP_Code", "Employee.AFP_Transfer_Code", "Employee.EPS_Code",
    "Employee.EPS_Transfer_Code", "Employee.CCF_Code", "Employee.ARL_Code",
    "Employee.Cesantias_Fund_Code", "Employee.Cesantias_Fund_Account",
    "Employee.Dependant_Document_Type", "Employee.Dependant_Document_Number",
    "Employee.Dependant_Name", "Employee.Dependant_Relationship",
    "Employee.Address", "Employee.Department_Code", "Employee.Municipality_Code",
    "Employee.Main_Contributor_Doc_Type", "Employee.Main_Contributor_Doc_Number",
    "Employee.Phone", "Employee.Email",
    "Employee.Work_Centre_Code", "Employee.Treaty_Country_Code",
    # Contract master data
    "Contract.Type_Code", "Contract.Start_Date", "Contract.End_Date",
    "Contract.Contractual_Salary", "Contract.Pay_Frequency_Code",
    "Contract.Payment_Form_Code", "Contract.Payment_Method_Code",
    "Contract.Cesantias_Regime",
}


def payroll_master_flag(system_mapping):
    sm = (system_mapping or "").strip()
    base = sm.split(" ", 1)[0].split("+", 1)[0].split("(", 1)[0].strip()
    return "Y" if (sm in _DD_MASTER_MAPPINGS or base in _DD_MASTER_MAPPINGS) else "N"


# ===========================================================================
#  GENERIC SHEET BUILDERS
# ===========================================================================
def _title_banner(ws, text, ncols, fillc=C_TITLE_BG):
    ws.merge_cells(start_row=1, start_column=1, end_row=1, end_column=ncols)
    c = ws.cell(row=1, column=1, value=text)
    c.font = F_TITLE
    c.fill = fill(fillc)
    c.alignment = CENTER
    ws.row_dimensions[1].height = 26


def sheet1_version(ws, cfg):
    ws.title = "Version Control"
    ws.column_dimensions["A"].width = 28
    ws.column_dimensions["B"].width = 118
    _title_banner(ws, "STATUTORY REPORT SPECIFICATION - VERSION CONTROL", 2)
    meta = [
        ("Document ID", cfg["doc_id"]),
        ("Filing ID (scope_manifest)", cfg["filing_id"]),
        ("Report Name (EN)", cfg["name_en"]),
        ("Report Name (Local ES)", cfg["name_es"]),
        ("Country", "Colombia (CO)"),
        ("Currency", "COP (Colombian peso). The peso has a centavo in law but it is not used in "
                     "practice; only the nomina electronica XML carries 2 decimals. See column P "
                     "of the Spec sheet for the applicable rounding convention."),
        ("Authority", cfg["authority_full"]),
        ("Legal Basis", cfg["legal_basis"]),
        ("Standard", "Spain 9-Sheet Statutory Report Spec Standard v2.4 (with v2.7 channel "
                     "verification and v2.8 resident/non-resident controls)"),
        ("Source Status", cfg["source_status"]),
        ("Fiscal Parameters 2026", "UVT = COP 52,374 (Res. DIAN 000238 of 15 Dec 2025); SMMLV = "
                                   "COP 1,750,905; transport allowance = COP 249,095; contribution-base "
                                   "ceiling = 25 SMMLV = COP 43,772,625; contribution-base floor = "
                                   "1 SMMLV = COP 1,750,905."),
    ]
    r = 3
    for lbl, val in meta:
        a = ws.cell(row=r, column=1, value=lbl); a.font = F_LBL; a.alignment = WRAP; a.border = BORDER
        b = ws.cell(row=r, column=2, value=val); b.font = F_DATA; b.alignment = WRAP; b.border = BORDER
        if r % 2 == 0:
            a.fill = fill(C_ALT); b.fill = fill(C_ALT)
        r += 1
    r += 1
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
    c = ws.cell(row=r, column=1, value="CHANGE LOG")
    c.font = F_SECTION; c.fill = fill(C_SEC_GREY)
    r += 1
    for ci, h in enumerate(["Version | Effective Date | Status", "Change Description | Updated By"], 1):
        c = ws.cell(row=r, column=ci, value=h)
        c.font = F_HDR; c.fill = fill(C_SUBHDR_BG); c.alignment = WRAPC; c.border = BORDER
    r += 1
    log = [
        ("v1.0 | 2026-09-04 | Issued",
         "Initial v2.4 build of the Spec from scope_manifest.json authority_filings.in_scope and CCG "
         "Module 10.1. 9-sheet Spain standard; 21-column field sheet. Submission channel verified per "
         "v2.7 STEP 3.5 and recorded in the Report Matrix. Column E 'Payroll Field (Y/N)' reflects the "
         "master-data-only classification (calculated amounts, totals, period values, config rates, "
         "system and constant fields = N; identity / contract / company master data = Y), to be "
         "reconciled with the 05-Data-Dictionary when built. | Mercans Compliance"),
    ]
    for ver, desc in log + cfg.get("extra_log", []):
        a = ws.cell(row=r, column=1, value=ver); a.font = F_DATA; a.alignment = WRAP; a.border = BORDER
        b = ws.cell(row=r, column=2, value=desc); b.font = F_DATA; b.alignment = WRAP; b.border = BORDER
        r += 1


MATRIX_COLS = ["Report ID", "Report Name (EN)", "Report Name (Local ES)", "Authority",
               "Frequency", "Due Date Rule", "Submission Method", "File Format",
               "Legal Basis", "Accuracy Assessment"]
MATRIX_W = [18, 30, 38, 30, 18, 42, 40, 34, 44, 62]


def sheet2_matrix(ws, cfg):
    ws.title = "Report Matrix"
    _title_banner(ws, "REPORT MATRIX - " + cfg["name_en"].upper(), len(MATRIX_COLS))
    for ci, (h, w) in enumerate(zip(MATRIX_COLS, MATRIX_W), 1):
        c = ws.cell(row=2, column=ci, value=h)
        c.font = F_HDR; c.fill = fill(C_SPEC_HDR); c.alignment = WRAPC; c.border = BORDER
        ws.column_dimensions[get_column_letter(ci)].width = w
    rowvals = [cfg["doc_id"], cfg["name_en"], cfg["name_es"], cfg["authority_full"],
               cfg["frequency"], cfg["due_date"], cfg["submission"], cfg["file_format"],
               cfg["legal_basis"], cfg["accuracy"]]
    for ci, v in enumerate(rowvals, 1):
        c = ws.cell(row=3, column=ci, value=v)
        c.font = F_DATA; c.alignment = WRAP; c.border = BORDER
    ws.row_dimensions[3].height = 190
    r = 5
    for block_title, notes in [("SUBMISSION CHANNEL VERIFICATION (v2.7 STEP 3.5)", cfg["channel_notes"]),
                               ("INTEGRATION TYPE AND DIRECTION", cfg["integration_notes"]),
                               ("RESIDENT / NON-RESIDENT TREATMENT (v2.8 control B1)", cfg["b1_notes"]),
                               ("RELATED FILINGS / CROSS-REFERENCES", cfg["related"])]:
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(MATRIX_COLS))
        c = ws.cell(row=r, column=1, value=block_title)
        c.font = F_SECTION; c.fill = fill(C_SEC_GREY)
        r += 1
        for note in notes:
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=len(MATRIX_COLS))
            c = ws.cell(row=r, column=1, value="- " + note)
            c.font = F_DATA; c.alignment = WRAP
            r += 1
        r += 1


def sheet3_scope(ws, cfg):
    ws.title = "Payroll Scope Summary"
    ws.column_dimensions["A"].width = 52
    ws.column_dimensions["B"].width = 14
    ws.column_dimensions["C"].width = 116
    _title_banner(ws, "PAYROLL SCOPE SUMMARY - " + cfg["name_en"].upper(), 3)
    for ci, h in enumerate(["SCENARIO", "REPORT?", "NOTES / REASONING"], 1):
        c = ws.cell(row=2, column=ci, value=h)
        c.font = F_HDR; c.fill = fill(C_SCOPE_HDR); c.alignment = WRAPC; c.border = BORDER
    r = 3
    for item in cfg["scope"]:
        if isinstance(item, str):
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=3)
            c = ws.cell(row=r, column=1, value="=== " + item + " ===")
            c.font = F_SECTION; c.fill = fill(C_SEC_GREY)
            r += 1
            continue
        label, yn, reason = item
        a = ws.cell(row=r, column=1, value=label); a.font = F_DATA; a.alignment = WRAP; a.border = BORDER
        b = ws.cell(row=r, column=2, value=yn); b.alignment = WRAPC; b.border = BORDER
        cc = ws.cell(row=r, column=3, value=reason); cc.font = F_DATA; cc.alignment = WRAP; cc.border = BORDER
        if yn.upper().startswith("Y"):
            b.fill = fill(C_GREEN); b.font = F_GRN
        else:
            b.fill = fill(C_RED); b.font = F_RED
        r += 1


def sheet4_spec(ws, cfg):
    ws.title = cfg["spec_sheet"]
    _title_banner(ws, cfg["name_en"] + " - " + cfg["name_es"], 21)
    for ci, (h, w) in enumerate(zip(SPEC_HEADERS, SPEC_WIDTHS), 1):
        c = ws.cell(row=2, column=ci, value=h)
        c.font = F_HDR; c.fill = fill(C_SPEC_HDR); c.alignment = WRAPC; c.border = BORDER
        ws.column_dimensions[get_column_letter(ci)].width = w
    ws.freeze_panes = "B3"
    ws.auto_filter.ref = "A2:U2"
    r = 3
    for item in cfg["fields"]:
        if isinstance(item, str):
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=21)
            c = ws.cell(row=r, column=1, value="=========== " + item + " ===========")
            c.font = F_SECTION; c.fill = fill(C_SEC_GREY); c.alignment = Alignment(vertical="center")
            r += 1
            continue
        vals, kind = list(item[:21]), item[21]
        if len(vals) != 21:
            raise ValueError("row must have 21 columns, got %d: %r" % (len(vals), vals[:2]))
        vals[4] = payroll_master_flag(vals[11])   # derive col E from System Mapping
        rfill = fill(KIND_FILL[kind])
        for ci in range(1, 22):
            c = ws.cell(row=r, column=ci, value=vals[ci - 1])
            c.font = F_DATA; c.alignment = WRAP; c.border = BORDER; c.fill = rfill
        r += 1


def sheet5_filestruct(ws, cfg):
    ws.title = "File Structure"
    ws.column_dimensions["A"].width = 36
    ws.column_dimensions["B"].width = 130
    _title_banner(ws, "FILE STRUCTURE AND TECHNICAL SPECIFICATIONS", 2)
    r = 2
    for lbl, val in cfg["filestruct"]:
        if lbl == "##":
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2)
            c = ws.cell(row=r, column=1, value="=== " + val + " ===")
            c.font = F_SECTION; c.fill = fill(C_SEC_GREY)
            r += 1
            continue
        a = ws.cell(row=r, column=1, value=lbl); a.font = F_LBL; a.alignment = WRAP; a.border = BORDER
        b = ws.cell(row=r, column=2, value=val)
        b.font = F_MONO if lbl == "" else F_DATA
        b.alignment = WRAP; b.border = BORDER
        if r % 2 == 0:
            a.fill = fill(C_ALT); b.fill = fill(C_ALT)
        r += 1


def sheet6_options(ws, cfg):
    ws.title = "Field Options"
    for ci, (h, w) in enumerate(zip(["Code", "Abbrev", "Local (ES)", "EN Description"],
                                    [16, 18, 56, 78]), 1):
        c = ws.cell(row=2, column=ci, value=h)
        c.font = F_HDR; c.fill = fill(C_SPEC_HDR); c.alignment = WRAPC; c.border = BORDER
        ws.column_dimensions[get_column_letter(ci)].width = w
    _title_banner(ws, "FIELD OPTIONS - CODE TABLES", 4)
    r = 3
    for item in cfg["options"]:
        if isinstance(item, str):
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
            c = ws.cell(row=r, column=1, value="=== " + item + " ===")
            c.font = F_SECTION; c.fill = fill(C_SEC_GREY)
            r += 1
            continue
        for ci, v in enumerate(item, 1):
            c = ws.cell(row=r, column=ci, value=v)
            c.font = F_DATA; c.alignment = WRAP; c.border = BORDER
            if r % 2 == 0:
                c.fill = fill(C_ALT)
        r += 1


def sheet7_population(ws, cfg):
    ws.title = "Population Rules"
    for ci, (h, w) in enumerate(zip(["Field Name", "Source System", "Population Logic", "Edge Cases"],
                                    [34, 26, 96, 74]), 1):
        c = ws.cell(row=2, column=ci, value=h)
        c.font = F_HDR; c.fill = fill(C_SPEC_HDR); c.alignment = WRAPC; c.border = BORDER
        ws.column_dimensions[get_column_letter(ci)].width = w
    _title_banner(ws, "POPULATION RULES - HOW TO FILL EACH FIELD FROM PAYROLL", 4)
    r = 3
    for item in cfg["population"]:
        if isinstance(item, str):
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
            c = ws.cell(row=r, column=1, value="=== " + item + " ===")
            c.font = F_SECTION; c.fill = fill(C_SEC_GREY)
            r += 1
            continue
        for ci, v in enumerate(item, 1):
            c = ws.cell(row=r, column=ci, value=v)
            c.font = F_DATA; c.alignment = WRAP; c.border = BORDER
            if r % 2 == 0:
                c.fill = fill(C_ALT)
        r += 1


def sheet8_example(ws, cfg):
    ws.title = "Example Analysis"
    for ci, (h, w) in enumerate(zip(["Raw Value", "Field Name", "Interpretation", "Notes"],
                                    [30, 36, 74, 66]), 1):
        c = ws.cell(row=2, column=ci, value=h)
        c.font = F_HDR; c.fill = fill(C_SPEC_HDR); c.alignment = WRAPC; c.border = BORDER
        ws.column_dimensions[get_column_letter(ci)].width = w
    _title_banner(ws, "EXAMPLE ANALYSIS - SAMPLE RECORD PARSED FIELD BY FIELD", 4)
    r = 3
    for item in cfg["example"]:
        if isinstance(item, str):
            ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4)
            c = ws.cell(row=r, column=1, value="=== " + item + " ===")
            c.font = F_SECTION; c.fill = fill(C_SEC_GREY)
            r += 1
            continue
        for ci, v in enumerate(item, 1):
            c = ws.cell(row=r, column=ci, value=v)
            c.font = F_DATA; c.alignment = WRAP; c.border = BORDER
            if r % 2 == 0:
                c.fill = fill(C_ALT)
        r += 1


def sheet9_sample(ws, cfg):
    ws.title = "Sample File"
    ws.column_dimensions["A"].width = 165
    _title_banner(ws, "SAMPLE FILE - " + cfg.get("sample_title", "RAW SUBMISSION FORMAT"), 1)
    r = 3
    for line in cfg["sample"].splitlines():
        c = ws.cell(row=r, column=1, value=line)
        c.font = F_MONO
        c.alignment = Alignment(wrap_text=False, vertical="top")
        r += 1


def build_workbook(cfg):
    wb = openpyxl.Workbook()
    sheet1_version(wb.active, cfg)
    sheet2_matrix(wb.create_sheet(), cfg)
    sheet3_scope(wb.create_sheet(), cfg)
    sheet4_spec(wb.create_sheet(), cfg)
    sheet5_filestruct(wb.create_sheet(), cfg)
    sheet6_options(wb.create_sheet(), cfg)
    sheet7_population(wb.create_sheet(), cfg)
    sheet8_example(wb.create_sheet(), cfg)
    sheet9_sample(wb.create_sheet(), cfg)
    return wb

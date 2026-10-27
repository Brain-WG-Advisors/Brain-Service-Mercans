# -*- coding: utf-8 -*-
"""
Colombia (CO) Wage Type Catalogue — workbook writer and v2.5 C3 validator
(part 5). Invoked by build_co_wtc.py.
"""

import copy
import json
import os

import openpyxl
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

from co_wtc_config import COLUMNS, NCOL, COL_WIDTHS, TAX_SS_COLS_1B, BASE_COLS_1B, TAX_CODES
import co_wtc_sheets as sheets


def write_workbook(cz_template, out_path, rows, counts, form_map):
    wb = openpyxl.load_workbook(cz_template)
    ws = wb["Wage Type Catalogue"]

    # capture the template's exact header and data styles
    blue_hdr = copy.copy(ws.cell(1, 2)._style)     # B1 = blue (theme8)
    orange_hdr = copy.copy(ws.cell(1, 1)._style)   # A1 = orange FFFF9900
    data_style = copy.copy(ws.cell(2, 2)._style)

    # wipe all existing content, keeping the sheet (and its formatting) alive
    max_r, max_c = ws.max_row, ws.max_column
    for r in range(1, max_r + 1):
        for c in range(1, max_c + 1):
            ws.cell(r, c).value = None
    ws.data_validations.dataValidation = []

    # header row
    for ci, (title, colour) in enumerate(COLUMNS, start=1):
        cell = ws.cell(1, ci, title)
        cell._style = copy.copy(blue_hdr if colour == "B" else orange_hdr)
        cell.alignment = Alignment(wrap_text=True, vertical="center", horizontal="center")
        ws.column_dimensions[get_column_letter(ci)].width = COL_WIDTHS.get(ci, 16)
    ws.freeze_panes = "C2"
    ws.row_dimensions[1].height = 78

    # data rows
    for ri, row in enumerate(rows, start=2):
        for ci in range(1, NCOL + 1):
            cell = ws.cell(ri, ci, row.get(ci))
            cell._style = copy.copy(data_style)
            cell.alignment = Alignment(wrap_text=True, vertical="top")
            cell.font = Font(name="Calibri", size=9)
    last = len(rows) + 1
    if ws.max_row > last:
        ws.delete_rows(last + 1, ws.max_row - last)
    if ws.max_column > NCOL:
        ws.delete_cols(NCOL + 1, ws.max_column - NCOL)

    # data validations
    def add_dv(options, ranges):
        dv = DataValidation(type="list", formula1='"%s"' % options, allow_blank=True)
        dv.error = "Pick a value from the list"
        dv.showErrorMessage = True
        for rng in ranges:
            dv.add(rng)
        ws.add_data_validation(dv)

    add_dv("Earning,Deduction,Base,Employer Contribution,Flag,Intermediary,Notional,Tax,Percentage",
           ["E2:E%d" % last])
    add_dv("Recurring,Additional,NA", ["J2:J%d" % last])
    add_dv("Pro Rata,Lump Sum,NA", ["H2:H%d" % last])
    add_dv("Yes,No", ["K2:K%d" % last, "AA2:AA%d" % last])
    add_dv("Enforce in default currency,No", ["L2:L%d" % last])
    add_dv("Regular (System default),All payrolls,First Payroll", ["M2:M%d" % last])
    yn = [get_column_letter(c) for c in TAX_SS_COLS_1B]              # N..R
    add_dv("Yes,No,Yes/No,NA", ["%s2:%s%d" % (c, c, last) for c in yn])
    add_dv("Salary,Non-Salary,Paid Rest,Conditional,NA", ["V2:V%d" % last])   # col 22 = V
    add_dv("Yes,No,Yes/No,NA", ["W2:W%d" % last, "X2:X%d" % last])            # cols 23, 24

    # auxiliary sheets
    sheets.write_version_control(wb["Version Control"])
    sheets.write_sick_pay(wb["Sick Leave Paid By Employer"])
    sheets.write_tax_credit(wb["Tax Credit"])
    wb["Sick Leave Paid By Employer"].title = "Employer Sick Pay"

    gc = wb.create_sheet("Global WTC Coverage")
    sheets.write_coverage(gc, blue_hdr, len(rows), counts["specific"], counts["earn"],
                          counts["ded"], counts["er"], counts["struct"])

    fr = wb.create_sheet("Form Reference Guide")
    sheets.write_form_reference(fr, blue_hdr, form_map)

    wb.save(out_path)
    return wb.sheetnames


# ---------------------------------------------------------------------------
# v2.5 C3 POST-GENERATION VALIDATION
# ---------------------------------------------------------------------------
def validate(out_path, global_wtc, manifest_path):
    wb = openpyxl.load_workbook(out_path)
    ws = wb["Wage Type Catalogue"]
    rows = list(ws.iter_rows(min_row=2, values_only=True))
    defined = set(TAX_CODES.keys())
    errs, warns = [], []

    # Check 0 — all 300 global codes present
    gwb = openpyxl.load_workbook(global_wtc)
    gcodes = {int(float(r[0])) for r in gwb["Sheet1"].iter_rows(min_row=2, values_only=True)
              if r[0] is not None}
    present = set()
    for r in rows:
        try:
            present.add(int(float(r[0])))
        except (TypeError, ValueError):
            pass
    missing = gcodes - present
    if missing:
        errs.append("Missing global codes: %s" % sorted(missing)[:10])

    # Check 1 — every scope_manifest in-scope wage-type category is represented
    blob = " ".join(" ".join(str(x) for x in r[:7] if x).lower() for r in rows)
    required = {
        "Basic salary": "salario basico",
        "All-inclusive salary (integral)": "salario integral",
        "Auxilio de transporte": "auxilio de transporte",
        "Auxilio de conectividad": "auxilio de conectividad",
        "Overtime day +25%": "hora extra diurna",
        "Overtime night +75%": "hora extra nocturna",
        "Night premium +35%": "recargo nocturno",
        "Rest-day / holiday premium": "recargo dominical",
        "Paid weekly rest and public holidays": "descanso dominical y festivo remunerado",
        "Commissions": "comision",
        "Habitual bonus": "bonificacion habitual",
        "Non-salary pacted bonus (40% clamp)": "no salarial",
        "Occasional gratuity": "gratificacion ocasional",
        "Salary in kind": "salario en especie",
        "Prima de servicios": "prima de servicios",
        "Cesantias": "cesantias",
        "Intereses a las cesantias": "intereses a las cesantias",
        "Vacaciones": "vacaciones",
        "Vacation compensated in cash": "compensacion en dinero de vacaciones",
        "Dotacion": "dotacion",
        "Incapacidad enfermedad general": "incapacidad por enfermedad general",
        "Incapacidad origen laboral": "incapacidad de origen laboral",
        "Licencia de maternidad": "licencia de maternidad",
        "Licencia de paternidad": "licencia de paternidad",
        "Licencia parental compartida": "licencia parental compartida",
        "Licencia remunerada legal": "licencia remunerada legal",
        "Licencia de luto": "licencia de luto",
        "Apoyo de sostenimiento del aprendiz": "apoyo de sostenimiento del aprendiz",
        "Indemnizacion por despido": "despido sin justa causa",
        "Indemnizacion moratoria": "indemnizacion moratoria",
        "Sancion no consignacion cesantias": "sancion por no consignacion",
        "Pagos de alimentacion a terceros": "pagos de alimentacion a terceros",
        "Medicina prepagada (employer)": "medicina prepagada",
        "Voluntary pension fund (employer)": "pensiones voluntarias",
        "Voluntary RAIS contribution": "cotizacion voluntaria al rais",
        "Equity / share incentives": "acciones",
        "Employee health 4%": "aporte a salud",
        "Employee pension 4%": "aporte a pension obligatoria",
        "Fondo de Solidaridad Pensional": "fondo de solidaridad pensional",
        "Retencion en la fuente": "retencion en la fuente",
        "Union dues": "cuota sindical",
        "Cooperative dues": "cooperativas",
        "Disciplinary sanction": "sancion disciplinaria",
        "Contribucion Sabes": "contribucion sabes",
        "Libranza": "libranza",
        "Employer loan / advance": "prestamo y anticipo del empleador",
        "Garnishment": "embargo",
        "Employer health 8.5%": "aporte a salud - empleador",
        "Employer pension 12%": "aporte a pension obligatoria - empleador",
        "ARL": "riesgos laborales",
        "CCF 4%": "caja de compensacion familiar",
        "SENA 2%": "sena",
        "ICBF 3%": "icbf",
    }
    for label, kw in required.items():
        if kw not in blob:
            errs.append("Scope category not represented in the WTC: %s (kw '%s')" % (label, kw))

    # Check 2 — every tax code referenced is in the Colombian legend (Egypt F20 guard)
    for r in rows:
        tc = r[6]
        if tc and tc not in defined:
            errs.append("Tax code not in the CO legend: %s (row code %s)" % (tc, r[0]))
        if tc and not str(tc).startswith("CO-"):
            errs.append("Non-Colombian tax code leaked: %s (row code %s)" % (tc, r[0]))

    # Check 3 — no ambiguity in the taxability / subjection / base columns without an explanation in D
    amb = {"Yes-No", "Yes/No", "Conditional"}
    for r in rows:
        for idx in [c - 1 for c in TAX_SS_COLS_1B + BASE_COLS_1B]:
            if idx < len(r) and r[idx] in amb and not r[3]:
                errs.append("Conditional value in a taxability column without an explanation: code %s" % r[0])

    # Check 4 — Egypt F20: commission must be present
    if "comision" not in blob:
        errs.append("Commission wage type MISSING (Egypt F20 guard)")

    # Check 5 — every row has a category, a formula and a tax code
    for r in rows:
        if not r[4]:
            errs.append("Row %s has no Category" % r[0])
        if not r[5]:
            errs.append("Row %s has no Formula" % r[0])
        if not r[6]:
            errs.append("Row %s has no Tax Code" % r[0])
        if not r[3]:
            errs.append("Row %s has no Explanation" % r[0])

    # Check 6 — residual-marker lint (C29 pre-flight over this artifact)
    import re
    markers_cs = [r"\bTODO\b", r"\bTBD\b", r"\bFIXME\b", r"\bXXX\b", r"\bVERIFY\s+No\b",
                  r"\[\s*CHECK\s*\]", r"\[\s*\?\s*\]"]
    phrases = ["to be confirmed", "to be verified", "[placeholder]"]
    for sheet in wb.worksheets:
        for row in sheet.iter_rows(values_only=True):
            for v in row:
                if not isinstance(v, str):
                    continue
                for pat in markers_cs:
                    if re.search(pat, v):
                        errs.append("Residual marker %s in sheet %s" % (pat, sheet.title))
                low = v.lower()
                for ph in phrases:
                    if ph in low:
                        errs.append('Residual phrase "%s" in sheet %s' % (ph, sheet.title))

    # Check 7 — the six required sheets exist, in order
    expected = ["Version Control", "Wage Type Catalogue", "Employer Sick Pay", "Tax Credit",
                "Global WTC Coverage", "Form Reference Guide"]
    if wb.sheetnames != expected:
        errs.append("Sheet order/names unexpected: %s" % wb.sheetnames)

    # Check 8 — the Form Reference Guide is populated (C17)
    fr = wb["Form Reference Guide"]
    if fr.max_row < 20:
        errs.append("Form Reference Guide has only %d rows - C17 needs every category mapped" % fr.max_row)

    # Check 9 — manifest sanity
    if os.path.exists(manifest_path):
        man = json.load(open(manifest_path, encoding="utf-8"))
        if man.get("currency") != "COP" or man.get("year") != "2026":
            warns.append("Manifest currency/year mismatch: %s / %s" % (man.get("currency"), man.get("year")))

    errs = sorted(set(errs))
    print("\n--- WTC POST-GENERATION VALIDATION (v2.5 C3) ---")
    co_rows = [r for r in rows if isinstance(r[0], str) and str(r[0]).startswith("CO-")]
    print("rows: %d | global codes present: %d/300 | CO-specific: %d | columns: %d"
          % (len(rows), len(present & gcodes), len(co_rows), ws.max_column))
    print("sheets: %s" % wb.sheetnames)
    if warns:
        print("WARNINGS:")
        for w in warns:
            print("  -", w)
    if errs:
        print("FAILURES:")
        for e in errs[:30]:
            print("  -", e)
        raise SystemExit("WTC validation FAILED (%d issue(s))" % len(errs))
    print("WTC post-generation validation PASSED")

# -*- coding: utf-8 -*-
"""US Compliance Payslip Generator (PSL, stage 7) - the only source of 06-payslip/US_Compliance_Payslip_Generator.xlsx.
usage: python build_psl.py [--out path] [--no-side]
Writes: the workbook; _pipeline/PSL-bindings.csv; _research/PSL-research-request.json; the PSL entries of _research/gaps.json;
_research/PSL-legal-items.json; checks/psl_recon.csv; checks/psl_requests.json.
Sheets (contract, in order): How to set up Payslip | Compliance Payslip | United States (EN) | United States (ES) | Payslip Spec |
Field Option | Population Range | Unit Rate Details.
"""
import csv
import datetime as dt
import hashlib
import io
import json
import os
import re
import shutil
import sys
import zipfile
from decimal import Decimal, ROUND_HALF_UP

from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.properties import PageSetupProperties

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import psl_common as S  # noqa: E402
import psl_content as K  # noqa: E402

# palette measured from REFERENCE_Payslip_Mozambique / Tunisia: DCDCDC labels, A9A9A9 section bars, no other fill on the payslip grid
NAVY, GREY, LABEL, NETG, ALT, ER = "A9A9A9", "A9A9A9", "DCDCDC", "DCDCDC", None, "DCDCDC"
MONEY = '_(* #,##0.00_);_(* \\(#,##0.00\\);_(* "-"??_);_(@_)'
THIN = Side(style="thin", color="999999")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
CENT = Decimal("0.01")
SHEETS = ["How to set up Payslip", "Compliance Payslip", "United States (EN)", "United States (ES)", "Payslip Spec",
          "Field Option", "Population Range", "Unit Rate Details"]
CACHED = {}          # (sheet, addr) -> numeric value of a formula cell
RECON = []           # reconciliation rows
LINES = {}           # sheet -> list of dicts of the example lines
REQ = {}             # key -> request record


def q2(x):
    return Decimal(x).quantize(CENT, rounding=ROUND_HALF_UP)


# ------------------------------------------------------------------ cell helpers ---
def put(ws, rng, value=None, fill=None, bold=False, size=6, color="000000", h="left", fmt=None, wrap=True,
        border=True, italic=False, name="Arial", v="center", merge=True):
    cells = ws[rng] if ":" in rng else ws[rng:rng]
    if merge and ":" in rng and rng.split(":")[0] != rng.split(":")[1] and rng not in [str(m) for m in ws.merged_cells.ranges]:
        ws.merge_cells(rng)
    first = None
    for row in cells:
        for c in row:
            if first is None:
                first = c
            if border:
                c.border = BORDER
            if fill:
                c.fill = PatternFill("solid", fgColor=fill)
            c.font = Font(name=name, size=size, bold=bold, color=color, italic=italic)
            c.alignment = Alignment(horizontal=h, vertical=v, wrap_text=wrap)
            if fmt:
                c.number_format = fmt
    if value is not None:
        first.value = S.clean(value) if isinstance(value, str) and not value.startswith("=") else value
    return first


def fcell(ws, addr, formula, value, **kw):
    """Formula cell with the cached value that the generator computed."""
    put(ws, addr, formula, **kw)
    CACHED[(ws.title, addr.split(":")[0])] = float(value)


# ------------------------------------------------------------------ sample amounts (computed, never typed) ---
def sample():
    d = {}
    d["reg_hours"], d["reg_rate"] = Decimal("80"), Decimal("36.00")
    d["ot_hours"], d["ot_rate"] = Decimal("4"), Decimal("54.00")
    d["reg"] = q2(d["reg_hours"] * d["reg_rate"])
    d["ot"] = q2(d["ot_hours"] * d["ot_rate"])
    d["comm"] = Decimal("17000.00")
    d["gross"] = d["reg"] + d["ot"] + d["comm"]
    d["k401"] = q2(d["gross"] * Decimal("0.05"))
    d["health"] = Decimal("85.00")
    d["fit_wages"] = d["gross"] - d["k401"] - d["health"]
    d["fica_wages"] = d["gross"] - d["health"]
    d["periods"] = Decimal("26")
    d["ytd_ss_wages"] = Decimal("181500.00")
    d["ytd_med_before"] = Decimal("181500.00")      # Medicare wages have no wage base: tracked apart from the social security wages
    d["ytd_gross_before"] = Decimal("185000.00")
    d["base"] = S.num("fed.fica.oasdi.wage_base")
    d["ss_rate"] = S.num("fed.fica.oasdi.rate.employee") / 100
    d["er_ss_rate"] = S.num("fed.fica.oasdi.rate.employer") / 100
    d["med_rate"] = S.num("fed.fica.medicare.rate.employee") / 100
    d["er_med_rate"] = S.num("fed.fica.medicare.rate.employer") / 100
    d["add_rate"] = S.num("fed.fica.addl_medicare.rate") / 100
    d["add_thr"] = S.num("fed.fica.addl_medicare.withholding_threshold")
    d["ytd_ss_tax"] = q2(d["ytd_ss_wages"] * d["ss_rate"])
    d["ss_remaining"] = q2(d["base"] * d["ss_rate"]) - d["ytd_ss_tax"]
    d["ss_period"] = q2(d["fica_wages"] * d["ss_rate"])
    d["ss"] = max(Decimal("0"), min(d["ss_remaining"], d["ss_period"]))
    d["er_ytd_ss_tax"] = q2(d["ytd_ss_wages"] * d["er_ss_rate"])
    d["er_ss_remaining"] = q2(d["base"] * d["er_ss_rate"]) - d["er_ytd_ss_tax"]
    d["er_ss_period"] = q2(d["fica_wages"] * d["er_ss_rate"])
    d["er_ss"] = max(Decimal("0"), min(d["er_ss_remaining"], d["er_ss_period"]))
    d["med"] = q2(d["fica_wages"] * d["med_rate"])
    d["er_med"] = q2(d["fica_wages"] * d["er_med_rate"])
    d["ytd_med_tax_before"] = q2(d["ytd_med_before"] * d["med_rate"])
    d["ytd_med_wages"] = d["ytd_med_before"] + d["fica_wages"]
    d["add_excess"] = max(Decimal("0"), min(d["fica_wages"], d["ytd_med_wages"] - d["add_thr"]))
    d["add"] = q2(d["add_excess"] * d["add_rate"])
    d["ytd_med_tax"] = d["ytd_med_tax_before"] + d["med"] + d["add"]
    d["ytd_gross"] = d["ytd_gross_before"] + d["gross"]
    thr = [Decimal(x) for x in str(S.fact("fed.fit.standard.single.thresholds")["value"]).split("/")]
    rts = [Decimal(x) / 100 for x in str(S.fact("fed.fit.rates")["value"]).split("/")]
    assert len(thr) == len(rts) == 8
    d["thr"], d["rts"] = thr, rts
    d["l1g"] = S.num("fed.fit.worksheet1a.line1g.other")
    d["annual"] = d["fit_wages"] * d["periods"]
    d["adj"] = max(Decimal("0"), d["annual"] - d["l1g"])
    steps, prev = [], Decimal("0")
    for t, r in zip(thr, rts):
        steps.append(max(Decimal("0"), d["adj"] - t) * (r - prev))
        prev = r
    d["steps"] = steps
    d["tent"] = sum(steps)
    d["fit"] = max(Decimal("0"), q2(d["tent"] / d["periods"]))
    d["deductions"] = d["k401"] + d["health"] + d["fit"] + d["ss"] + d["med"] + d["add"]
    d["net"] = d["gross"] - d["deductions"]
    d["ytd_fit"], d["ytd_401"] = Decimal("31000.00"), Decimal("9000.00")
    d["leave_ent"], d["leave_tak"] = Decimal("40.00"), Decimal("8.00")
    return d


# ------------------------------------------------------------------ the payslip tabs ---
def calc_labels(es):
    """Labels of the supporting calculation blocks. Values come from the facts as plain tags: no register id, no stamp."""
    def T(en_, es_):
        return es_ if es else en_

    def F(k):
        return S.fv(k, plain=True)
    t = {}
    t["ss_base"] = T("Social security wage base: ", "Base salarial del Seguro Social: ") + F("fed.fica.oasdi.wage_base")
    t["ss_rate"] = T("Social security rate, employee: ", "Tasa del Seguro Social, empleado: ") + F("fed.fica.oasdi.rate.employee")
    t["ss_wages"] = T("Social security wages of this payslip (gross earnings less the cafeteria-plan contribution)",
                      "Salario sujeto al Seguro Social de este recibo (ingreso bruto menos la contribución del plan cafetería)")
    t["ytd_wages"] = T("Social security wages paid before this payslip (year to date, limited to the wage base)",
                       "Salario sujeto al Seguro Social pagado antes de este recibo (acumulado, limitado a la base salarial)")
    t["ytd_tax"] = T("Social security tax withheld before this payslip (year to date)", "Seguro Social retenido antes de este recibo (acumulado)")
    t["remain"] = T("Remaining annual maximum tax = rate x wage base less tax withheld to date",
                    "Máximo anual restante = tasa x base salarial menos lo retenido")
    t["period"] = T("Rate x social security wages of this payslip", "Tasa x salario sujeto de este recibo")
    t["ss"] = T("Social security tax withheld = lesser of the two amounts above", "Seguro Social retenido = el menor de los dos importes anteriores")
    t["er_rate"] = T("Social security rate, employer: ", "Tasa del Seguro Social, empleador: ") + F("fed.fica.oasdi.rate.employer")
    t["er_ytdt"] = T("Employer social security tax paid before this payslip (year to date)", "Seguro Social del empleador pagado antes de este recibo (acumulado)")
    t["er_rem"] = T("Remaining annual maximum employer tax = rate x wage base less employer tax paid to date",
                    "Máximo anual restante del empleador = tasa x base salarial menos lo pagado")
    t["er_per"] = T("Employer rate x social security wages of this payslip", "Tasa del empleador x salario sujeto de este recibo")
    t["er_ss"] = T("Employer social security tax = lesser of the two amounts above", "Seguro Social del empleador = el menor de los dos importes anteriores")
    t["med_rate"] = T("Medicare rate, employee: ", "Tasa Medicare, empleado: ") + F("fed.fica.medicare.rate.employee")
    t["mw_before"] = T("Medicare wages paid before this payslip (year to date, no wage base)", "Salario sujeto a Medicare pagado antes de este recibo (acumulado, sin base salarial)")
    t["mt_before"] = T("Medicare tax withheld before this payslip (year to date)", "Medicare retenido antes de este recibo (acumulado)")
    t["med"] = T("Medicare tax withheld = rate x Medicare wages of this payslip", "Medicare retenido = tasa x salario sujeto de este recibo")
    t["er_med_rate"] = T("Medicare rate, employer: ", "Tasa Medicare, empleador: ") + F("fed.fica.medicare.rate.employer")
    t["er_med"] = T("Employer Medicare tax = rate x Medicare wages of this payslip", "Medicare del empleador = tasa x salario sujeto de este recibo")
    t["add_thr"] = T("Additional Medicare Tax withholding threshold: ", "Umbral del Medicare adicional: ") + F("fed.fica.addl_medicare.withholding_threshold")
    t["add_rate"] = T("Additional Medicare Tax rate: ", "Tasa del Medicare adicional: ") + F("fed.fica.addl_medicare.rate")
    t["add_ytd"] = T("Medicare wages year to date including this payslip", "Salario Medicare acumulado incluyendo este recibo")
    t["add_exc"] = T("Wages above the threshold, limited to this payslip", "Salario sobre el umbral, limitado a este recibo")
    t["add"] = T("Additional Medicare Tax withheld = rate x wages above the threshold", "Medicare adicional retenido = tasa x salario sobre el umbral")
    t["gross_before"] = T("Earnings paid before this payslip (year to date)", "Ingresos pagados antes de este recibo (acumulado)")
    t["fit_method"] = T("Method: ", "Método: ") + F("fed.fit.method")
    t["l1a"] = T("Line 1a: taxable wages of this payslip (gross less 401(k) deferral and cafeteria-plan contribution)",
                 "Línea 1a: salario sujeto de este recibo (bruto menos 401(k) y plan cafetería)")
    t["l1b"] = T("Line 1b: pay periods per year", "Línea 1b: períodos de pago por año")
    t["l1c"] = T("Line 1c: annualised wages = 1a x 1b", "Línea 1c: salario anualizado = 1a x 1b")
    t["l1g"] = T("Line 1g: Step 2 box not checked, single or married filing separately: ",
                 "Línea 1g: casilla del Paso 2 sin marcar, soltero o casado por separado: ") + F("fed.fit.worksheet1a.line1g.other")
    t["l1i"] = T("Line 1i: adjusted annual wage amount = 1c less 1g", "Línea 1i: salario anual ajustado = 1c menos 1g")
    t["thr"] = T("Standard table thresholds, single or married filing separately: ", "Umbrales de la tabla estándar, soltero o casado por separado: ") + F("fed.fit.standard.single.thresholds")
    t["rts"] = T("Marginal rates of the table: ", "Tasas marginales de la tabla: ") + F("fed.fit.rates")
    t["brk"] = T("Tax in the bracket = (adjusted annual wage - threshold) x increase in the rate", "Impuesto del tramo = (salario ajustado - umbral) x aumento de la tasa")
    t["tent"] = T("Tentative annual withholding amount", "Retención anual provisional")
    t["l2f"] = T("Tentative withholding per pay period = annual amount / pay periods, rounded half-up to the cent",
                 "Retención provisional por período = anual / períodos, redondeada al centavo")
    t["cred"] = T("Step 3 credits per pay period (none in this sample)", "Créditos del Paso 3 por período (ninguno en esta muestra)")
    t["extra"] = T("Step 4(c) extra withholding per pay period (none in this sample)", "Retención adicional del Paso 4(c) por período (ninguna en esta muestra)")
    t["fit"] = T("Federal income tax withheld this payslip", "Impuesto federal retenido en este recibo")
    return t


def payslip_sheet(wb, name, lang, master):
    L = K.LABELS[lang]
    es = lang == "ES"
    ws = wb[name]
    ws.sheet_view.showGridLines = False
    ws.sheet_properties.pageSetUpPr = PageSetupProperties(fitToPage=True)
    for col, w in zip("ABCDEFGHIJ", (15, 11, 14, 10, 15, 10, 11, 12, 11, 11)):
        ws.column_dimensions[col].width = w
    d = sample()
    dd = {}      # named addresses
    S.at(f"{name}")
    # title band
    for r in range(1, 6):
        ws.row_dimensions[r].height = 14
    put(ws, "A1:J5", None, fill=NAVY, border=False, merge=False)
    put(ws, "C2:G4", (L["title"] if not master else L["title"] + " - " + ("master" if not es else "maestro")), fill=NAVY, bold=True, size=15, color="FFFFFF", h="left", border=False)
    put(ws, "H1:J1", L["net"], fill=NETG, bold=True, size=7, h="center")
    put(ws, "H2:J4", None, fill=NETG, bold=True, size=12, h="center", fmt=MONEY)      # formula set below
    put(ws, "H5:J5", L["ccy"], fill=NETG, bold=True, size=7, h="center")
    img = XLImage(os.path.join(S.SHARED, "mercans_logo.png"))
    img.width, img.height = 64, 64
    ws.add_image(img, "A1")
    # header blocks
    ws.row_dimensions[6].height = 12
    r = 7
    L1 = [("emp_name", "Mercans Compliance Sample Inc."), ("emp_addr", "100 Sample Street, Austin, TX 00000"), ("emp_phone", "(000) 000-0000"),
          ("emp_ein", "00-0000000")]
    R1 = [("pay_period", "10/05/2026 - 10/18/2026"), ("pay_date", "10/23/2026"), ("pay_freq", L["v_biweekly"]), ("state", "TX")]
    for (lk, lv), (rk, rv) in zip(L1, R1):
        put(ws, f"A{r}:B{r}", L[lk], fill=LABEL, bold=True)
        put(ws, f"C{r}:E{r}", lv)
        put(ws, f"F{r}:G{r}", L[rk], fill=LABEL, bold=True)
        put(ws, f"H{r}:J{r}", rv)
        r += 1
    r += 1
    L2 = [("ee_name", "Alex Sample"), ("ee_addr", "200 Example Avenue, Austin, TX 00000"), ("ee_title", L["v_title"]), ("ee_basis", L["v_hourly"])]
    R2 = [("ee_id", "E-000045"), ("ee_ssn", "***-**-0000"), ("ee_hire", "03/01/2021"), ("ee_w4", L["v_w4"])]
    for (lk, lv), (rk, rv) in zip(L2, R2):
        put(ws, f"A{r}:B{r}", L[lk], fill=LABEL, bold=True)
        put(ws, f"C{r}:E{r}", lv)
        put(ws, f"F{r}:G{r}", L[rk], fill=LABEL, bold=True)
        put(ws, f"H{r}:J{r}", rv)
        r += 1
    r += 1
    # earnings
    put(ws, f"A{r}:J{r}", L["earn_sec"], fill=GREY, bold=True, size=7, color="FFFFFF", h="center")
    r += 1
    put(ws, f"A{r}:E{r}", L["earn_hdr"], fill=LABEL, bold=True)
    put(ws, f"F{r}", L["rate"], fill=LABEL, bold=True, h="center")
    put(ws, f"G{r}", L["units"], fill=LABEL, bold=True, h="center")
    put(ws, f"H{r}:J{r}", L["amount"], fill=LABEL, bold=True, h="center")
    r += 1
    lines = []
    e0 = r
    earn = [("62100", d["reg"], d["reg_rate"], d["reg_hours"]), ("62110", d["ot"], d["ot_rate"], d["ot_hours"]), ("US-042", d["comm"], None, None)]
    for i, (code, amt, rate, units) in enumerate(earn):
        fill = ALT if i % 2 else None
        put(ws, f"A{r}:E{r}", f"{code} - {K.CW[code]['label']}", fill=fill)
        put(ws, f"F{r}", float(rate) if rate is not None else None, fill=fill, h="right", fmt=MONEY)
        put(ws, f"G{r}", float(units) if units is not None else None, fill=fill, h="right", fmt=MONEY)
        put(ws, f"H{r}:J{r}", float(amt), fill=fill, h="right", fmt=MONEY)
        lines.append(dict(code=code, cell=f"H{r}", sign=1, sheet=name, section="Earnings"))
        dd[code] = f"H{r}"
        r += 1
    e1 = r - 1
    put(ws, f"A{r}:G{r}", L["gross"], fill=LABEL, bold=True)
    fcell(ws, f"H{r}:J{r}", f"=SUM(H{e0}:H{e1})", d["gross"], fill=LABEL, bold=True, h="right", fmt=MONEY)
    dd["gross"] = f"H{r}"
    r += 1
    put(ws, f"A{r}:F{r}", L["hours_total"], fill=LABEL, bold=True)
    fcell(ws, f"G{r}", f"=SUM(G{e0}:G{e1})", d["reg_hours"] + d["ot_hours"], fill=LABEL, bold=True, h="right", fmt=MONEY)
    put(ws, f"H{r}:J{r}", None, fill=LABEL)
    r += 2
    # deductions
    put(ws, f"A{r}:E{r}", L["ded_hdr"], fill=LABEL, bold=True)
    put(ws, f"F{r}", L["rate"], fill=LABEL, bold=True, h="center")
    put(ws, f"G{r}", L["units"], fill=LABEL, bold=True, h="center")
    put(ws, f"H{r}:J{r}", L["amount"], fill=LABEL, bold=True, h="center")
    r += 1
    d0 = r
    ded_order = ["21640", "21610", "US-001", "21900", "US-006", "US-008"]
    ded_row = {}
    for i, code in enumerate(ded_order):
        fill = ALT if i % 2 else None
        put(ws, f"A{r}:E{r}", f"{code} - {K.CW[code]['label']}", fill=fill)
        put(ws, f"F{r}", None, fill=fill)
        put(ws, f"G{r}", None, fill=fill)
        ded_row[code] = r
        dd[code] = f"H{r}"
        lines.append(dict(code=code, cell=f"H{r}", sign=-1, sheet=name, section="Employee deductions"))
        r += 1
    d1 = r - 1
    put(ws, f"A{r}:G{r}", L["ded_total"], fill=LABEL, bold=True)
    fcell(ws, f"H{r}:J{r}", f"=SUM(H{d0}:H{d1})", d["deductions"], fill=LABEL, bold=True, h="right", fmt=MONEY)
    dd["ded"] = f"H{r}"
    r += 2
    put(ws, f"A{r}:G{r}", L["net_row"], fill=NETG, bold=True, size=7, h="right")
    fcell(ws, f"H{r}:J{r}", f"=H{dd['gross'][1:]}-H{dd['ded'][1:]}", d["net"], fill=NETG, bold=True, size=7, h="right", fmt=MONEY)
    dd["net"] = f"H{r}"
    net_row = r
    r += 2
    # employer contributions
    put(ws, f"A{r}:E{r}", L["er_hdr"], fill=ER, bold=True)
    put(ws, f"F{r}", L["rate"], fill=ER, bold=True, h="center")
    put(ws, f"G{r}", L["units"], fill=ER, bold=True, h="center")
    put(ws, f"H{r}:J{r}", L["amount"], fill=ER, bold=True, h="center")
    r += 1
    c0 = r
    er_rows = {}
    for code, amt in (("US-005", d["er_ss"]), ("US-007", d["er_med"])):
        put(ws, f"A{r}:E{r}", f"{code} - {K.CW[code]['label']}", fill=ER)
        put(ws, f"F{r}", None, fill=ER)
        put(ws, f"G{r}", None, fill=ER)
        put(ws, f"H{r}:J{r}", float(amt), fill=ER, h="right", fmt=MONEY)      # formula set after the calculation block
        er_rows[code] = r
        lines.append(dict(code=code, cell=f"H{r}", sign=0, sheet=name, section="Employer contributions"))
        r += 1
    put(ws, f"A{r}:G{r}", L["er_total"], fill=ER, bold=True)
    fcell(ws, f"H{r}:J{r}", f"=SUM(H{c0}:H{r - 1})", d["er_ss"] + d["er_med"], fill=ER, bold=True, h="right", fmt=MONEY)
    r += 2
    # leave balance: the sample work location (TX) has no balance rule, so the block shows that it is not printed
    put(ws, f"A{r}:J{r}", L["leave_sec"], fill=GREY, bold=True, size=7, color="FFFFFF", h="center")
    r += 1
    for i, k in enumerate(("leave_ent", "leave_tak")):
        fill = None if i == 0 else ALT
        put(ws, f"A{r}:G{r}", L[k], fill=fill)
        put(ws, f"H{r}:J{r}", L["not_printed"], fill=fill, h="center", italic=True)
        r += 1
    put(ws, f"A{r}:G{r}", L["leave_bal"], fill=LABEL, bold=True)
    put(ws, f"H{r}:J{r}", L["not_printed"], fill=LABEL, h="center", italic=True, bold=True)
    r += 2
    # payment details
    put(ws, f"A{r}:J{r}", L["bank_sec"], fill=GREY, bold=True, size=7, color="FFFFFF", h="center")
    r += 1
    put(ws, f"A{r}:B{r}", L["bank"], fill=LABEL, bold=True, h="center")
    put(ws, f"C{r}:E{r}", L["acct"], fill=LABEL, bold=True, h="center")
    put(ws, f"F{r}:G{r}", L["method"], fill=LABEL, bold=True, h="center")
    put(ws, f"H{r}:J{r}", L["amount"], fill=LABEL, bold=True, h="center")
    r += 1
    put(ws, f"A{r}:B{r}", L["v_bank"], h="center")
    put(ws, f"C{r}:E{r}", "****0000", h="center")
    put(ws, f"F{r}:G{r}", L["v_dd"], h="center")
    fcell(ws, f"H{r}:J{r}", f"={dd['net']}", d["net"], h="right", fmt=MONEY)
    r += 2
    # state switched fields
    put(ws, f"A{r}:J{r}", L["state_sec"], fill=GREY, bold=True, size=7, color="FFFFFF", h="center")
    r += 1
    for i, k in enumerate(("tips", "comp", "guide", "comptime", "mw_allow", "piece", "az_sick", "nyc_acc", "nyc_paid", "nyc_unpaid_used",
                           "nyc_unpaid_av", "nm_ben", "op_name", "mail_addr")):
        fill = ALT if i % 2 else None
        put(ws, f"A{r}:G{r}", L[k], fill=fill)
        put(ws, f"H{r}:J{r}", L["not_printed"], fill=fill, h="center", italic=True)
        r += 1
    r += 1
    # YTD
    put(ws, f"A{r}:J{r}", L["ytd_sec"], fill=GREY, bold=True, size=7, color="FFFFFF", h="center")
    r += 1
    ytd_ss_row = ytd_med_row = ytd_gross_row = None
    for i, (k, val) in enumerate((("ytd_gross", None), ("ytd_fit", d["ytd_fit"]), ("ytd_ss", None), ("ytd_med", None), ("ytd_401", d["ytd_401"]))):
        fill = ALT if i % 2 else None
        put(ws, f"A{r}:G{r}", L[k], fill=fill)
        if val is not None:
            put(ws, f"H{r}:J{r}", float(val), fill=fill, h="right", fmt=MONEY)
        else:
            put(ws, f"H{r}:J{r}", None, fill=fill, h="right", fmt=MONEY)   # formula set after the calc block
        if k == "ytd_ss":
            ytd_ss_row = r
        if k == "ytd_med":
            ytd_med_row = r
        if k == "ytd_gross":
            ytd_gross_row = r
        r += 1
    r += 1
    # footer, then the print area: the payslip proper ends here
    put(ws, f"A{r}:J{r}", L["sample"], italic=True, h="center", border=False)
    r += 1
    put(ws, f"A{r}:J{r}", L["doc"], h="center", border=False)
    if master:
        r += 1
        put(ws, f"A{r}:J{r}", L["master"], h="center", border=False, italic=True)
    ws.print_area = f"A1:J{r}"
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0
    r += 2
    # supporting calculations (outside the print area)
    CL = calc_labels(es)
    put(ws, f"A{r}:J{r}", L["calc_sec"], fill=GREY, bold=True, size=7, color="FFFFFF", h="center")
    r += 1
    put(ws, f"A{r}:J{r}", L["fica_sec"], fill=GREY, bold=True, size=7, color="FFFFFF", h="center")
    r += 1

    def calc(label, val=None, fmt=MONEY, formula=None, bold=False, rowfill=None):
        nonlocal r
        put(ws, f"A{r}:G{r}", label, fill=rowfill or (ALT if r % 2 else None), bold=bold)
        if formula:
            fcell(ws, f"H{r}:J{r}", formula[0], formula[1], fill=rowfill or (ALT if r % 2 else None), h="right", fmt=fmt, bold=bold)
        else:
            put(ws, f"H{r}:J{r}", float(val), fill=rowfill or (ALT if r % 2 else None), h="right", fmt=fmt, bold=bold)
        a = f"H{r}"
        r += 1
        return a

    c_base = calc(CL["ss_base"], d["base"], "#,##0.00")
    c_rate = calc(CL["ss_rate"], d["ss_rate"], "0.00%")
    c_wages = calc(CL["ss_wages"], formula=(f"={dd['gross']}-{dd['21610']}", d["fica_wages"]))
    c_ytdw = calc(CL["ytd_wages"], d["ytd_ss_wages"])
    c_ytdt = calc(CL["ytd_tax"], formula=(f"=ROUND({c_ytdw}*{c_rate},2)", d["ytd_ss_tax"]))
    c_rem = calc(CL["remain"], formula=(f"=ROUND({c_base}*{c_rate},2)-{c_ytdt}", d["ss_remaining"]))
    c_per = calc(CL["period"], formula=(f"=ROUND({c_wages}*{c_rate},2)", d["ss_period"]))
    c_ss = calc(CL["ss"], formula=(f"=MAX(0,MIN({c_rem},{c_per}))", d["ss"]), bold=True, rowfill=LABEL)
    c_err = calc(CL["er_rate"], d["er_ss_rate"], "0.00%")
    c_er_ytdt = calc(CL["er_ytdt"], formula=(f"=ROUND({c_ytdw}*{c_err},2)", d["er_ytd_ss_tax"]))
    c_er_rem = calc(CL["er_rem"], formula=(f"=ROUND({c_base}*{c_err},2)-{c_er_ytdt}", d["er_ss_remaining"]))
    c_er_per = calc(CL["er_per"], formula=(f"=ROUND({c_wages}*{c_err},2)", d["er_ss_period"]))
    c_er_ss = calc(CL["er_ss"], formula=(f"=MAX(0,MIN({c_er_rem},{c_er_per}))", d["er_ss"]), bold=True, rowfill=LABEL)
    c_mr = calc(CL["med_rate"], d["med_rate"], "0.00%")
    c_mwb = calc(CL["mw_before"], d["ytd_med_before"])
    c_mtb = calc(CL["mt_before"], formula=(f"=ROUND({c_mwb}*{c_mr},2)", d["ytd_med_tax_before"]))
    c_med = calc(CL["med"], formula=(f"=ROUND({c_wages}*{c_mr},2)", d["med"]), bold=True, rowfill=LABEL)
    c_emr = calc(CL["er_med_rate"], d["er_med_rate"], "0.00%")
    c_er_med = calc(CL["er_med"], formula=(f"=ROUND({c_wages}*{c_emr},2)", d["er_med"]), bold=True, rowfill=LABEL)
    c_at = calc(CL["add_thr"], d["add_thr"], "#,##0.00")
    c_ar = calc(CL["add_rate"], d["add_rate"], "0.00%")
    c_ay = calc(CL["add_ytd"], formula=(f"={c_mwb}+{c_wages}", d["ytd_med_wages"]))
    c_ae = calc(CL["add_exc"], formula=(f"=MAX(0,MIN({c_wages},{c_ay}-{c_at}))", d["add_excess"]))
    c_add = calc(CL["add"], formula=(f"=ROUND({c_ae}*{c_ar},2)", d["add"]), bold=True, rowfill=LABEL)
    c_gb = calc(CL["gross_before"], d["ytd_gross_before"])
    r += 1
    put(ws, f"A{r}:J{r}", L["fit_sec"], fill=GREY, bold=True, size=7, color="FFFFFF", h="center")
    r += 1
    put(ws, f"A{r}:J{r}", CL["fit_method"], h="left")
    ws.row_dimensions[r].height = 36
    r += 1
    f1a = calc(CL["l1a"], formula=(f"={dd['gross']}-{dd['21640']}-{dd['21610']}", d["fit_wages"]))
    f1b = calc(CL["l1b"], d["periods"], "0")
    f1c = calc(CL["l1c"], formula=(f"={f1a}*{f1b}", d["annual"]))
    f1g = calc(CL["l1g"], d["l1g"], "#,##0.00")
    f1i = calc(CL["l1i"], formula=(f"=MAX(0,{f1c}-{f1g})", d["adj"]))
    put(ws, f"A{r}:J{r}", CL["thr"], h="left")
    ws.row_dimensions[r].height = 24
    r += 1
    put(ws, f"A{r}:J{r}", CL["rts"], h="left")
    r += 1
    b0 = r
    for i, (t, rt, st) in enumerate(zip(d["thr"], d["rts"], d["steps"])):
        fill = ALT if i % 2 else None
        put(ws, f"A{r}:E{r}", (f"Bracket {i + 1}" if not es else f"Tramo {i + 1}") + ": " + CL["brk"], fill=fill)
        put(ws, f"F{r}", float(t), fill=fill, h="right", fmt="#,##0")
        put(ws, f"G{r}", float(rt), fill=fill, h="right", fmt="0%")
        prev = f"G{r - 1}" if i else "0"
        fcell(ws, f"H{r}:J{r}", f"=MAX(0,{f1i}-F{r})*(G{r}-{prev})", st, fill=fill, h="right", fmt=MONEY)
        r += 1
    tent = calc(CL["tent"], formula=(f"=SUM(H{b0}:H{r - 1})", d["tent"]), bold=True, rowfill=LABEL)
    f2f = calc(CL["l2f"], formula=(f"=ROUND({tent}/{f1b},2)", q2(d["tent"] / d["periods"])))
    f3 = calc(CL["cred"], Decimal("0"))
    f4 = calc(CL["extra"], Decimal("0"))
    c_fit = calc(CL["fit"], formula=(f"=MAX(0,{f2f}-{f3}+{f4})", d["fit"]), bold=True, rowfill=LABEL)
    # formulas that point at the calculation block
    fcell(ws, f"H{ded_row['US-001']}:J{ded_row['US-001']}", f"={c_fit}", d["fit"], h="right", fmt=MONEY,
          fill=ALT if (ded_order.index('US-001') % 2) else None)
    fcell(ws, f"H{ded_row['21900']}:J{ded_row['21900']}", f"={c_ss}", d["ss"], h="right", fmt=MONEY,
          fill=ALT if (ded_order.index('21900') % 2) else None)
    fcell(ws, f"H{ded_row['US-006']}:J{ded_row['US-006']}", f"={c_med}", d["med"], h="right", fmt=MONEY,
          fill=ALT if (ded_order.index('US-006') % 2) else None)
    fcell(ws, f"H{ded_row['US-008']}:J{ded_row['US-008']}", f"={c_add}", d["add"], h="right", fmt=MONEY,
          fill=ALT if (ded_order.index('US-008') % 2) else None)
    put(ws, f"H{ded_row['21640']}:J{ded_row['21640']}", float(d["k401"]), h="right", fmt=MONEY)
    put(ws, f"H{ded_row['21610']}:J{ded_row['21610']}", float(d["health"]), fill=ALT, h="right", fmt=MONEY)
    fcell(ws, f"H{er_rows['US-005']}:J{er_rows['US-005']}", f"={c_er_ss}", d["er_ss"], fill=ER, h="right", fmt=MONEY)
    fcell(ws, f"H{er_rows['US-007']}:J{er_rows['US-007']}", f"={c_er_med}", d["er_med"], fill=ER, h="right", fmt=MONEY)
    fcell(ws, f"H{ytd_gross_row}:J{ytd_gross_row}", f"={c_gb}+{dd['gross']}", d["ytd_gross"], h="right", fmt=MONEY)
    fcell(ws, f"H{ytd_ss_row}:J{ytd_ss_row}", f"={c_ytdt}+{c_ss}", d["ytd_ss_tax"] + d["ss"], h="right", fmt=MONEY)
    fcell(ws, f"H{ytd_med_row}:J{ytd_med_row}", f"={c_mtb}+{c_med}+{c_add}", d["ytd_med_tax"], h="right", fmt=MONEY, fill=ALT)
    # net highlight in the title band
    fcell(ws, "H2:J4", f"={dd['net']}", d["net"], fill=NETG, bold=True, size=12, h="center", fmt=MONEY)
    ws.freeze_panes = None
    ws.page_setup.orientation = "portrait"
    LINES[name] = dict(lines=lines, net=dd["net"], sample=d)
    return ws


# ------------------------------------------------------------------ the other sheets ---
def sheet_howto(ws):
    S.at("How to set up Payslip")
    ws.sheet_view.showGridLines = False
    ws.column_dimensions["A"].width = 3
    ws.column_dimensions["B"].width = 34
    ws.column_dimensions["C"].width = 100
    put(ws, "B1:C1", f"{S.COUNTRY} Compliance Payslip Generator", fill=NAVY, bold=True, size=15, color="FFFFFF", border=False)
    ws.row_dimensions[1].height = 26
    img = XLImage(os.path.join(S.SHARED, "mercans_logo.png"))
    img.width, img.height = 40, 40
    ws.add_image(img, "D1")
    rows = [("Document ID", S.PSL_ID), ("Package version", f"v{S.PKG}"), ("Status", S.STATUS), ("Related documents", f"{S.CCG_REF}; {S.WTC_REF}; {S.DD_REF}")]
    r = 3
    for k, v in rows:
        put(ws, f"B{r}", k, fill=LABEL, bold=True, size=9)
        put(ws, f"C{r}", v, size=9)
        r += 1
    r += 1
    for j, h in enumerate(("Version", "Date", "Author", "Status")):
        pass
    put(ws, f"B{r}", "Version Control", fill=GREY, bold=True, size=9, color="FFFFFF")
    put(ws, f"C{r}", "Version | Issue date | Author | Status", fill=GREY, bold=True, size=9, color="FFFFFF")
    r += 1
    put(ws, f"B{r}", f"v{S.PKG}", size=9)
    put(ws, f"C{r}", f"{S.ISSUE} | {S.AUTHOR} | {S.STATUS}", size=9)
    r += 2
    steps = [
        ("What this workbook is", "One US payslip template with per-State rules. The tab Compliance Payslip is the language-neutral master. The tabs United States (EN) and United States (ES) carry the same fields in English and Spanish. Payslip Spec maps every printed field to the HR and payroll system. Field Option lists the controlled values and the pay-statement rules per work-location State. Population Range says who receives the payslip. Unit Rate Details lists the earning codes with their rate and unit accounts."),
        ("1. Pick the rule set", "Read the work-location State of the employee. Open Field Option, block STATE_STATEMENT_RULE, and read the row of that State. The rule set follows the work location, not the residence."),
        ("2. Copy the master", "Create a new tab, copy the payslip from Compliance Payslip, and translate the labels. Keep the pay element lines in the form code, dash, wage type name; the codes come from " + S.WTC_REF + "."),
        ("3. Switch the optional blocks", "Print the paid leave balance block, the tips and gratuities line, the compensation sources, the pay-code guide reference, compensatory time, minimum-wage allowances, piece-rate units, sick pay received (Arizona), the New York City protected time off detail, benefits earned (New Mexico) and the employer operating name and mailing address (Minnesota) only for the work-location States whose rule names them (Field Option, block STATE_STATEMENT_RULE and block LEAVE_BALANCE_RULE)."),
        ("4. Social Security number", "Print the last four digits at most, and no digits for the States whose rule bars it (Field Option, block SSN_DISPLAY_RULE)."),
        ("5. Check the totals", "Gross earnings is the sum of the earnings lines; total deductions is the sum of the deduction lines; net pay is gross earnings minus total deductions. The net pay box in the title band repeats the net pay row. The tax lines come from the calculation basis blocks under the payslip: the social security line is the lesser of the remaining annual maximum and the rate times the period base."),
        ("6. Export", "Use Normal margins, save the tab as PDF, and deliver it electronically with the consent record and the free print or download access described in Field Option, block ELECTRONIC_DELIVERY_RULE."),
        ("Illustrative sample", "Every name, address, identifier and amount on the payslip tabs is fictitious and shows the layout only. The amounts are computed from the statutory rates, not typed."),
    ]
    for k, v in steps:
        put(ws, f"B{r}", k, fill=LABEL, bold=True, size=9)
        put(ws, f"C{r}", v, size=9)
        ws.row_dimensions[r].height = max(24, 13 * (1 + len(v) // 110))
        r += 1


def sheet_spec(ws, specs):
    S.at("Payslip Spec")
    ws.sheet_view.showGridLines = False
    for col, w in zip("ABCDE", (3, 34, 38, 52, 100)):
        ws.column_dimensions[col].width = w
    r = 2
    cur = None
    n = 0
    for f in specs:
        if f["sec"] != cur:
            if cur is not None:
                r += 1
            cur = f["sec"]
            put(ws, f"B{r}:E{r}", cur, fill="0B5394", bold=True, size=10, color="FFFFFF", name="Calibri")
            r += 1
            for col, h in zip("BCDE", ("Field Name (EN)", "Field Name (Local)", "HRP Mapping (TA & BA)", "Field Explanation")):
                put(ws, f"{col}{r}", h, fill="4BACC6", bold=True, size=10, color="FFFFFF", name="Calibri")
            r += 1
        S.at(f"Payslip Spec!B{r}")
        put(ws, f"B{r}", f["en"], size=10, name="Calibri")
        put(ws, f"C{r}", f["es"], size=10, name="Calibri")
        put(ws, f"D{r}", f["hrp"], size=10, name="Calibri")
        txt = f["text"]
        if f["dd"]:
            txt += " DD fields (" + S.DD_REF + "): " + "; ".join(f["dd"]) + "."
        put(ws, f"E{r}", txt, size=10, name="Calibri")
        ws.row_dimensions[r].height = max(30, 14 * (1 + len(re.sub(r"\[\[[^\]]*\]\]", "x" * 20, txt)) // 95))
        r += 1
        n += 1
    return n


def fo_rows():
    """Field Option rows: (field, value, description, usage)."""
    rows = []
    A = rows.append
    S.at("Field Option")
    A(("CURRENCY", "USD", "United States dollar", "All amounts print in USD with two decimals."))
    A(("PAYSLIP_LANGUAGE", "EN", "English: the issued payslip", "Language of the payslip tab United States (EN)."))
    A(("PAYSLIP_LANGUAGE", "ES", "Spanish label set: documented seam", "Labels only; amounts and pay element codes are identical to the English tab."))
    A(("PAY_FREQUENCY", "Weekly", "Weekly pay", "Pay periods per year come from the payroll calendar."))
    A(("PAY_FREQUENCY", "Biweekly", "Every two weeks", "Pay periods per year come from the payroll calendar."))
    A(("PAY_FREQUENCY", "Semimonthly", "Twice a month", "Pay periods per year come from the payroll calendar."))
    A(("PAY_FREQUENCY", "Monthly", "Once a month", "Pay periods per year come from the payroll calendar."))
    for v, dsc in (("Hourly", "Paid by the hour: hours and rate print"), ("Salary", "Paid a fixed salary per period"),
                   ("Piece rate", "Paid by units produced: units and rate print"), ("Commission", "Paid by commission"),
                   ("Shift", "Paid a rate per shift: shifts and rate print"), ("Day", "Paid a rate per day: days and rate print"),
                   ("Week", "Paid a rate per week: weeks and rate print"), ("Other", "Paid on another basis: the basis prints with the rate")):
        A(("RATE_OF_PAY_BASIS", v, dsc, "Decides which of hours, rate and piece units print."))
    # federal baseline
    S.at("Field Option!FEDERAL_BASELINE")
    for k in ("psl.fed.statement.required", "psl.language.official_federal", "fed.records.flsa.retention_years", "fed.records.irs.retention_years"):
        A(("FEDERAL_BASELINE", k.split(".")[-1] if k.startswith("psl.") else k.rsplit(".", 2)[-2], S.fv(k), "Federal rule that sets the baseline of the payslip; State rules add content."))
    # state rule sets
    cont, scope = K.st_keys("content"), K.st_keys("scope")
    extra_open = {"IL": "psl.il.statement.content_rule_300_600", "IN": "psl.in.statement.scope_confirmation", "TX": "psl.tx.statement.scope_confirmation",
                  "NY": "psl.ny.statement.industry_extras"}
    for stc in K.STATES:
        S.at(f"Field Option!STATE_STATEMENT_RULE {stc}")
        ks = [k for k in (cont.get(stc), scope.get(stc)) if k]
        if ks:
            for k in ks:
                A(("STATE_STATEMENT_RULE", stc, f"{S.state_name(stc)}: " + S.fv(k, jur=stc), "Rule set switched on when the work-location State is " + stc + "."))
        else:
            A(("STATE_STATEMENT_RULE", stc, f"{S.state_name(stc)}: " + S.gap("psl.state.rule.missing", "missing", stc), "Rule set switched on when the work-location State is " + stc + "."))
        if stc in extra_open and not (S.has(extra_open[stc]) and S.usable(extra_open[stc])[0]):
            A(("STATE_STATEMENT_RULE", stc, f"{S.state_name(stc)}: " + S.gap(extra_open[stc], "open", stc), "Open item for this State's rule set."))
    # leave balances
    for k in ("psl.ak.sick_leave.on_statement", "psl.az.sick_leave.on_statement", "psl.ca.sick_leave.on_statement", "psl.md.sick_leave.on_statement",
              "psl.mn.sick_leave.on_statement", "psl.nm.sick_leave.on_statement", "psl.nv.paid_leave.on_statement", "psl.wa.sick_leave.on_statement",
              "psl.nyc.pto.on_statement"):
        stc = k.split(".")[1].upper()
        S.at(f"Field Option!LEAVE_BALANCE_RULE {stc}")
        A(("LEAVE_BALANCE_RULE", stc, S.fv(k, jur=stc), "Print the paid leave balance block of the payslip for this work location."))
    # SSN display
    for k in sorted(k for k in S.C.FACTS if re.match(r"^psl\.[a-z]{2}\.ssn\.rule$", k)) + ["psl.w2.ssn_truncation.rule"]:
        stc = k.split(".")[1].upper()
        S.at(f"Field Option!SSN_DISPLAY_RULE {stc}")
        A(("SSN_DISPLAY_RULE", stc, S.fv(k, jur=stc), "Governs the Social Security number display on pay documents and the annual statement."))
    S.at("Field Option!SSN_DISPLAY_RULE open")
    A(("SSN_DISPLAY_RULE", "UNREAD", S.gap("psl.ssn_rule.unread_states", "open"), "Jurisdictions whose SSN display statute is not yet read: apply the default: last four digits at most."))
    # electronic delivery
    deliv = sorted(k for k in S.C.FACTS if re.match(r"^psl\.[a-z]{2}\.statement\.electronic_delivery$", k))
    for k in deliv:
        stc = k.split(".")[1].upper()
        S.at(f"Field Option!ELECTRONIC_DELIVERY_RULE {stc}")
        A(("ELECTRONIC_DELIVERY_RULE", stc, S.fv(k, jur=stc), "Electronic delivery condition of the work-location State."))
    for stc in ("CA", "CO", "MA", "NY", "NV"):
        k = f"psl.{stc.lower()}.statement.electronic_consent"
        if S.has(k) and S.usable(k)[0]:
            continue
        S.at(f"Field Option!ELECTRONIC_DELIVERY_RULE {stc}")
        A(("ELECTRONIC_DELIVERY_RULE", stc, S.gap(k, "open", stc), "Electronic delivery condition of the work-location State is not yet configured."))
    A(("ELECTRONIC_DELIVERY_RULE", "DEFAULT", "Electronic delivery with an opt-in consent record and free print or download access", "Default that meets the strictest rules listed in this block."))
    # retention (keys of the PSL facts only)
    S.at("Field Option!RETENTION_PERIOD")
    pk = {f["key"] for f in S.PSLFACTS["facts"]}
    for k in sorted(k for k in pk if re.search(r"retention.*years$", k)):
        parts = k.split(".")
        if parts[0] == "psl":
            j, what = parts[1].upper(), ".".join(parts[2:])
        else:
            j, what = ("FED" if parts[0] == "fed" else parts[0].upper()), ".".join(parts[1:])
        what = re.sub(r"\.?years$", "", what).replace(".", " ").replace("_", " ").strip()
        S.at(f"Field Option!RETENTION_PERIOD {j}")
        A(("RETENTION_PERIOD", j, f"{what}: " + S.fv(k, jur=j), "Minimum keeping period of the record named."))
    for k in ("psl.ri.retention_and_hire_notice_2026", "psl.nc.retention.withholding_records.years"):
        j = "RI" if ".ri." in k else "NC"
        if S.has(k) and S.usable(k)[0]:          # a closed item prints its fact above, never a gap
            continue
        S.at(f"Field Option!RETENTION_PERIOD {j}")
        A(("RETENTION_PERIOD", j, S.gap(k, "open", j), "Keeping period is not yet configured."))
    A(("RETENTION_PERIOD", "DEFAULT", "Archive every payslip for the longest keeping period among the rules listed in this block", "Default: one archive period that satisfies every listed rule."))
    # W-2 feed, multistate, companion documents, notice language
    S.at("Field Option!W2_FEED_ITEM")
    for k in ("psl.w2.box12.new_codes_2026", "psl.w2.box14b.tipped_occupation_code", "psl.w2.box14.vt_child_care_contribution", "me.pfml.w2_box14_label",
              "psl.w2.box14.ca_sdi", "psl.w2.multistate.boxes_15_20", "fed.plaw119_21.tips_overtime.level"):
        A(("W2_FEED_ITEM", k.split(".")[-1], S.fv(k), "Item the payslip and year-to-date figures must feed on the annual wage statement."))
    S.at("Field Option!MULTISTATE_REACH")
    for k in ("psl.multi.reach.ca", "psl.multi.reach.default", "psl.ia.statement.reach"):
        A(("MULTISTATE_REACH", k.split(".")[-1], S.fv(k), "Which State's pay-statement rule applies to the employee."))
    S.at("Field Option!COMPANION_DOCUMENT")
    for k in ("psl.or.new_hire_explanation", "psl.ct.pay_code_guide.url_on_pay_record"):
        A(("COMPANION_DOCUMENT", k.split(".")[1].upper(), S.fv(k), "Document that accompanies the payslip in this State."))
    for k in sorted(k for k in S.C.FACTS if k.startswith("psl.notice_language.")):
        S.at(f"Field Option!NOTICE_LANGUAGE {k.split('.')[-1]}")
        A(("NOTICE_LANGUAGE", k.split(".")[-1].upper(), S.fv(k), "Language rule of a notice or poster that is not the payslip itself."))
    # every other fact of the payslip research, so that none is left out of the workbook
    S.at("Field Option!STATE_RULE_DETAIL")
    used = {k for (k, _e) in S.USED}
    for f in S.PSLFACTS["facts"]:
        k = f["key"]
        if k in used or k in {x for x in S.GAPS}:
            continue
        parts = k.split(".")
        j = parts[1].upper() if parts[0] == "psl" else parts[0].upper()
        S.at(f"Field Option!STATE_RULE_DETAIL {j}")
        A(("STATE_RULE_DETAIL", j, S.fv(k, jur=j), "Further rule of the jurisdiction that bears on the payslip."))
    # the statutory payslip lines
    S.at("Field Option!PAYSLIP_LINE")
    for code, label, sec, side in K.catalogue():
        A(("PAYSLIP_LINE", code, label, f"{sec}: prints as '{code} - {label}' when the amount is not zero. Wage type of {S.WTC_REF}."))
    return rows


def sheet_field_option(ws, rows):
    for col, w in zip("ABCD", (30, 22, 120, 70)):
        ws.column_dimensions[col].width = w
    for c, h in zip("ABCD", ("Field Name", "Option Value", "Option Description", "Usage Context")):
        put(ws, f"{c}1", h, fill=LABEL, bold=True, size=10, name="Times New Roman")
    ws.freeze_panes = "A2"
    r = 2
    for f, v, dsc, u in rows:
        put(ws, f"A{r}", f, size=10, name="Times New Roman")
        put(ws, f"B{r}", v, size=10, name="Times New Roman")
        put(ws, f"C{r}", dsc, size=10, name="Times New Roman")
        put(ws, f"D{r}", u, size=10, name="Times New Roman")
        ws.row_dimensions[r].height = max(15, 13 * (1 + len(re.sub(r"\[\[[^\]]*\]\]", "x" * 30, dsc)) // 130))
        r += 1
    return r - 2


def sheet_population(ws, pop):
    S.at("Population Range")
    for col, w in zip("ABC", (42, 18, 140)):
        ws.column_dimensions[col].width = w
    for c, h in zip("ABC", ("Worker Situation", "Include? (YES/NO)", "Notes")):
        put(ws, f"{c}1", h, fill=LABEL, bold=True, size=10, name="Times New Roman")
    for i, (a, b, c) in enumerate(pop, start=2):
        put(ws, f"A{i}", a, size=10, name="Times New Roman")
        put(ws, f"B{i}", b, size=10, name="Times New Roman")
        put(ws, f"C{i}", c, size=10, name="Times New Roman")
        ws.row_dimensions[i].height = max(15, 13 * (1 + len(re.sub(r"\[\[[^\]]*\]\]", "x" * 30, c)) // 150))


TIME_BASED = {
    "62100": "Regular hours from the hours worked accumulator US-030, with the rate of wage type 62104; amount = hours x rate.",
    "62110": "Overtime hours from the hours worked accumulator US-030; amount = overtime hours x overtime rate of the line, printed apart from straight time.",
    "62150": "Premium hours from the hours worked accumulator US-030; amount = premium hours x premium rate of the line.",
    "62160": "Holiday hours from the hours worked accumulator US-030; amount = holiday hours x rate of the line.",
    "62170": "On-call hours from the hours worked accumulator US-030; amount = on-call hours x on-call rate of the line.",
    "62300": "Annual leave hours from the hours worked accumulator US-030; amount = leave hours x rate of the line.",
}


def unit_rows():
    earn = [(c, l) for c, l, sec, side in K.catalogue() if sec == "Earnings"]
    rate_codes = {c for c, w in K.WTC.items() if str(c).startswith("62") and "(rate" in str(w["label"]).lower()}
    top = [e for e in earn if e[0].startswith("62") and e[0] not in rate_codes][:24] + [e for e in earn if e[0].startswith("US-")]
    out = []
    for c, l in top:
        if c in TIME_BASED:
            rate = "62104" if c == "62100" and "62104" in rate_codes else "No rate wage type in the catalogue"
            out.append((l, c, rate, "US-030", TIME_BASED[c]))
        else:
            out.append((l, c, "Amount only, no rate account", "Amount only, no unit account",
                        f"Amount only: the line prints the amount of {l[0].lower() + l[1:]} of the pay run; no hours, units or rate print."))
    return out


def sheet_unit(ws, rows):
    S.at("Unit Rate Details")
    for col, w in zip("ABCDEF", (3, 52, 14, 34, 28, 100)):
        ws.column_dimensions[col].width = w
    for c, h in zip("BCDEF", ("Earning Description", "Earning Code", "Rate Account", "Unit Account", "Basis")):
        put(ws, f"{c}2", h, bold=True, size=10, name="Times New Roman", fill=LABEL)
    for i, (l, c, ra, ua, basis) in enumerate(rows, start=3):
        put(ws, f"B{i}", l, size=10, name="Times New Roman")
        put(ws, f"C{i}", c, size=10, name="Times New Roman")
        put(ws, f"D{i}", ra, size=10, name="Times New Roman")
        put(ws, f"E{i}", ua, size=10, name="Times New Roman")
        put(ws, f"F{i}", basis, size=10, name="Times New Roman")
    return len(rows)


# ------------------------------------------------------------------ workbook, cached values, deterministic zip ---
def fixed_zip(src, dst):
    zin = zipfile.ZipFile(src)
    names = zin.namelist()
    wbxml = zin.read("xl/workbook.xml").decode("utf-8")
    sheet_names = re.findall(r'<sheet [^>]*name="([^"]+)"', wbxml)
    rels = zin.read("xl/_rels/workbook.xml.rels").decode("utf-8")
    rid_target = dict(re.findall(r'<Relationship [^>]*Id="([^"]+)"[^>]*Target="([^"]+)"', rels))
    rid_target.update({a: b for b, a in re.findall(r'<Relationship [^>]*Target="([^"]+)"[^>]*Id="([^"]+)"', rels)})
    order = re.findall(r'<sheet [^>]*name="([^"]+)"[^>]*r:id="([^"]+)"', wbxml)
    part_of = {}
    for nm, rid in order:
        t = rid_target[rid].lstrip("/")
        part_of["xl/" + t if not t.startswith("xl/") else t] = nm.replace("&amp;", "&")
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as zout:
        for n in sorted(names):
            data = zin.read(n)
            if n in part_of:
                sh = part_of[n]
                x = data.decode("utf-8")

                def rep(m):
                    addr = m.group(1)
                    v = CACHED.get((sh, addr))
                    if v is None:
                        return m.group(0)
                    return m.group(0).replace("<v></v>", f"<v>{repr(round(v, 6))}</v>").replace("<v />", f"<v>{repr(round(v, 6))}</v>")
                x = re.sub(r'<c r="([A-Z]+\d+)"[^>]*><f>[^<]*</f><v\s*/?>(?:</v>)?</c>', rep, x)
                data = x.encode("utf-8")
            if n == "docProps/core.xml":
                data = re.sub(rb"(<dcterms:(?:created|modified)[^>]*>)[^<]*(</dcterms:)", rb"\g<1>2026-11-04T00:00:00Z\g<2>", data)
            zi = zipfile.ZipInfo(n, date_time=(2026, 11, 4, 0, 0, 0))
            zi.compress_type = zipfile.ZIP_DEFLATED
            zi.external_attr = 0o600 << 16
            zout.writestr(zi, data)
    open(dst, "wb").write(out.getvalue())


def assemble():
    S.USED.clear()
    S.GAPS.clear()
    CACHED.clear()
    RECON.clear()
    LINES.clear()
    wb = Workbook()
    wb.remove(wb.active)
    for n in SHEETS:
        wb.create_sheet(n)
    wb.properties.creator = "Mercans Compliance Regulations Team"
    wb.properties.title = f"{S.COUNTRY} Compliance Payslip Generator {S.PSL_ID} v{S.PKG}"
    wb.properties.created = dt.datetime(2026, 11, 4, 0, 0, 0)
    wb.properties.modified = dt.datetime(2026, 11, 4, 0, 0, 0)
    wb.calculation.fullCalcOnLoad = True
    sheet_howto(wb["How to set up Payslip"])
    payslip_sheet(wb, "Compliance Payslip", "EN", True)
    payslip_sheet(wb, "United States (EN)", "EN", False)
    payslip_sheet(wb, "United States (ES)", "ES", False)
    specs = K.spec_fields()
    nspec = sheet_spec(wb["Payslip Spec"], specs)
    rows = fo_rows()
    nfo = sheet_field_option(wb["Field Option"], rows)
    sheet_population(wb["Population Range"], K.population())
    nur = sheet_unit(wb["Unit Rate Details"], unit_rows())
    return wb, dict(specs=specs, spec_rows=nspec, fo_rows=nfo, unit_rows=nur)


def short(s, n=300):
    s = re.sub(r"\s+", " ", str(s))
    return s if len(s) <= n else s[:n - 1].rstrip() + "."


OPEN_LABEL = {}


def make_requests():
    unres = S.UNRESOLVED
    out = {}
    idmap = json.load(open(os.path.join(HERE, "gap_ids.json"), encoding="utf-8"))
    nxt = max(int(v.split("-")[-1]) for v in idmap.values()) + 1
    for key in sorted(S.GAPS):
        if key not in idmap:                      # ids are never reused: a new gap takes the next unused number
            idmap[key] = f"PSL-RQ-{nxt:02d}"
            nxt += 1
    json.dump(idmap, open(os.path.join(HERE, "gap_ids.json"), "w", encoding="utf-8"), indent=1)
    for key in sorted(S.GAPS):
        g = S.GAPS[key]
        gid = idmap[key]
        i = int(gid.split("-")[-1])
        why = g.get("why")
        if key in unres:
            u = unres[key]
            q = f"What does the official source state for {key}? Recorded reason: {u['why']}"
            doc_what = f"Not read: {key.replace('.', ' ')}"
            closes = u.get("what_would_close_it", "The official source, saved and read")
            searched = list(u.get("attempted") or []) + ["_research/PSL-facts.json unresolved[]"]
        elif why == "f44":
            miss = S.BLOCKED.get(key) or []
            els = ", ".join(f"{k} {e if not isinstance(e, (list, tuple)) else '-'.join(map(str, e))}" for k, e in miss[:6])
            f = S.fact(key)
            q = (f"Which official source row carries the wording of the statement recorded for {key} "
                 f"(text elements not found in the saved copy of {', '.join(S.rids(f))}: {els})?")
            closes = "A saved copy of the cited authority page that contains these elements, or a corrected statement with the row that carries it"
            doc_what = f"Statement {key.replace('.', ' ')} whose wording is not proven in the saved copy of its source"
            doc_closes = "The authority page that carries the wording, saved and read"
            searched = [f"saved copies of {', '.join(S.rids(f))}", "same-jurisdiction rows of the register"]
        elif key == "psl.ny.statement.industry_extras":
            q = ("Which official source states the industry-specific payslip items of Labor Law 195(3) for home care aides "
                 "(benefits, prevailing wage supplements)? The register row names them; no payslip fact carries them.")
            closes = "The text of Labor Law 195(3) saved from the official host and read, with the register row that carries it"
            doc_what = "Industry-specific payslip items of New York Labor Law 195(3) are not configured"
            doc_closes = closes
            searched = ["00-official-sources/legal-basis-register.csv", "_research/PSL-facts.json"]
        else:
            q = f"Which authority page states the pay-statement rule for {', '.join(sorted(g['jurs'])) or key}?"
            closes = "The authority's own page for each jurisdiction named, read on the official host"
            doc_what = f"No source recorded for {key.replace('.', ' ')}"
            doc_closes = closes
            searched = ["_research/PSL-facts.json", "00-official-sources/legal-basis-register.csv"]
        if key in unres:
            doc_closes = closes
        out[key] = dict(gid=gid, rq=f"RQ-{i:02d}", key=key, question=q, question_short=short(q, 230), closes=short(closes, 230),
                        doc_what=short(doc_what, 200), doc_closes=short(doc_closes, 200), why=why, searched=searched,
                        locations=g["locations"], jurs=sorted(g["jurs"]))
    return out


def new_key_ok(key):
    return re.match(r"^[a-z][a-z0-9_]*(\.[a-z0-9_]+)+$", key) is not None


def write_workbook(out, final_info):
    wb, info = final_info
    tmp = out + ".tmp"
    wb.save(tmp)
    fixed_zip(tmp, out)
    os.remove(tmp)
    return info


def main():
    out = os.path.join(S.PSLDIR, S.FILENAME)
    if "--out" in sys.argv:
        out = sys.argv[sys.argv.index("--out") + 1]
    S.GAP_IDS.clear()
    REQ.clear()
    assemble()                                           # pass 1: collect the gaps
    REQ.update(make_requests())
    for k, r in REQ.items():
        S.GAP_IDS[k] = r["gid"]
    built = assemble()                                   # pass 2: final text with gap ids
    REQ2 = make_requests()
    assert {k: v["gid"] for k, v in REQ2.items()} == {k: v["gid"] for k, v in REQ.items()}, "gap ids changed between passes"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    if os.path.exists(out) and "--no-side" not in sys.argv:       # keep a copy of the previous build before it is replaced
        h = hashlib.md5(open(out, "rb").read()).hexdigest()[:8]
        bk = os.path.join(S.HERE, "_backup", f"{os.path.splitext(os.path.basename(out))[0]}.{h}.xlsx")
        if not os.path.exists(bk):
            shutil.copy2(out, bk)
    info = write_workbook(out, built)
    if "--no-side" not in sys.argv:
        import psl_side
        psl_side.write_all(info, REQ, LINES, built[0], out)
    print("written", out)


if __name__ == "__main__":
    main()

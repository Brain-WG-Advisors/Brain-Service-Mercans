# -*- coding: utf-8 -*-
"""Builds one visual payslip sheet (EN / ES / language-neutral master).

Geometry is identical on all three sheets - only the label set and the
pay-element names change, so the master really is a copy-and-translate base.

Formula hygiene (v2.7 / C26):
  * totals are SUM over ONE amount column (H) and appear only on total rows
  * Net  = Gross cell - Total deductions cell
  * Leave balance = Entitlement cell - Taken cell
  * no CONCATENATE / TEXT totals anywhere, no total on a data row
"""

from openpyxl.styles import Font
from openpyxl.drawing.image import Image as XLImage

from co_payslip_style import (
    NAVY, GRAY_HDR, GRAY_LBL, ALT, GREEN, ORANGE, ACC2, NUM4, DAYS2, HOURS,
    title_font, hdr_font, lbl_font, val_font, LEFT, LEFT_WRAP, CENTER, RIGHT,
    paint,
)
import co_payslip_data as D

WIDTHS = {"A": 34, "B": 12, "C": 16, "D": 12, "E": 20, "F": 17,
          "G": 11, "H": 19, "I": 15, "J": 12}
LAST = "J"


def _put(ws, ref, value=None, fill_rgb=None, font=None, align=None,
         fmt=None, border=True):
    """Merge (if a range), write the value into the anchor cell, then paint."""
    if ":" in ref:
        ws.merge_cells(ref)
        anchor = ref.split(":")[0]
    else:
        anchor = ref
    if value is not None:
        ws[anchor] = value
    paint(ws, ref, fill_rgb, font, align, fmt, border)
    return ws[anchor]


def _section(ws, row, text):
    _put(ws, "A%d:%s%d" % (row, LAST, row), text, GRAY_HDR, hdr_font(9), CENTER)
    ws.row_dimensions[row].height = 16.5


def _pair(ws, row, l1, v1, l2=None, v2=None):
    """label | value | label | value  - or a full-width value when l2 is None."""
    _put(ws, "A%d:B%d" % (row, row), l1, GRAY_LBL, lbl_font(), LEFT)
    if l2 is None:
        _put(ws, "C%d:%s%d" % (row, LAST, row), v1, None, val_font(), LEFT)
    else:
        _put(ws, "C%d:E%d" % (row, row), v1, None, val_font(), LEFT)
        _put(ws, "F%d:G%d" % (row, row), l2, GRAY_LBL, lbl_font(), LEFT)
        _put(ws, "H%d:%s%d" % (row, LAST, row), v2, None, val_font(), LEFT)
    ws.row_dimensions[row].height = 13.5


def _tablehead(ws, row, item, rate, unit, amount):
    _put(ws, "A%d:E%d" % (row, row), item, GRAY_LBL, lbl_font(), LEFT)
    _put(ws, "F%d" % row, rate, GRAY_LBL, lbl_font(), CENTER)
    _put(ws, "G%d" % row, unit, GRAY_LBL, lbl_font(), CENTER)
    _put(ws, "H%d:%s%d" % (row, LAST, row), amount, GRAY_LBL, lbl_font(), CENTER)
    ws.row_dimensions[row].height = 14.0


def _dataline(ws, row, label, rate, unit, unit_fmt, amount, shade):
    bg = ALT if shade else None
    _put(ws, "A%d:E%d" % (row, row), label, bg, val_font(), LEFT)
    _put(ws, "F%d" % row, rate, bg, val_font(),
         RIGHT if isinstance(rate, (int, float)) else CENTER,
         ACC2 if isinstance(rate, (int, float)) else None)
    _put(ws, "G%d" % row, unit, bg, val_font(), CENTER, unit_fmt)
    _put(ws, "H%d:%s%d" % (row, LAST, row), amount, bg, val_font(), RIGHT, ACC2)
    ws.row_dimensions[row].height = 13.0


def _totalline(ws, row, label, formula, fill_rgb=GRAY_LBL, bold=True):
    _put(ws, "A%d:G%d" % (row, row), label, fill_rgb, lbl_font(9) if bold else val_font(), LEFT)
    _put(ws, "H%d:%s%d" % (row, LAST, row), formula, fill_rgb,
         lbl_font(9) if bold else val_font(), RIGHT, ACC2)
    ws.row_dimensions[row].height = 15.0


def _calcline(ws, row, label, formula, fmt=ACC2, shade=False):
    bg = ALT if shade else None
    _put(ws, "A%d:G%d" % (row, row), label, bg, val_font(), LEFT)
    _put(ws, "H%d:%s%d" % (row, LAST, row), formula, bg, val_font(), RIGHT, fmt)
    ws.row_dimensions[row].height = 13.0


def build(ws, L, lang, logo_path=None):
    """lang in {'EN','ES','MASTER'}.  Returns a dict of key row numbers."""
    master = lang == "MASTER"
    es = lang == "ES"
    for col, w in WIDTHS.items():
        ws.column_dimensions[col].width = w
    ws.sheet_view.showGridLines = False
    ws.page_setup.orientation = "portrait"
    ws.sheet_properties.pageSetUpPr.fitToPage = True
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = 0

    R = {}

    # ---------------- title band -------------------------------------------
    _put(ws, "A1:B4", None, None, None, CENTER)
    _put(ws, "C1:%s2" % LAST, L["title"], NAVY, title_font(15), CENTER)
    ws.row_dimensions[1].height = 26
    ws.row_dimensions[2].height = 26
    _put(ws, "C3:D3", L["period"], GRAY_LBL, lbl_font(), LEFT)
    _put(ws, "E3:H3", "%s  -  %s" % (D.PERIOD_START, D.PERIOD_END), None,
         val_font(9, bold=True), LEFT)
    _put(ws, "C4:D4", L["paydate"], GRAY_LBL, lbl_font(), LEFT)
    _put(ws, "E4:H4", D.PAY_DATE, None, val_font(9, bold=True), LEFT)
    _put(ws, "I3:J3", L["netbox"], GREEN, lbl_font(9), CENTER)
    net_box = _put(ws, "I4:J4", None, GREEN, lbl_font(10), CENTER, ACC2)
    ws.row_dimensions[3].height = 15
    ws.row_dimensions[4].height = 18
    ws.row_dimensions[5].height = 6

    if logo_path:
        img = XLImage(logo_path)
        img.width, img.height = 62, 62
        ws.add_image(img, "A1")

    row = 6
    # ---------------- employer ---------------------------------------------
    _section(ws, row, L["sec_employer"]); row += 1
    E = D.EMPLOYER
    _pair(ws, row, L["employer_name"], E["name"], L["employer_nit"], E["nit"]); row += 1
    _pair(ws, row, L["employer_addr"], E["address"]); row += 1
    _pair(ws, row, L["employer_city"], E["city"], L["employer_arl"], E["arl"]); row += 1
    _pair(ws, row, L["employer_type"], E["person_type"], L["employer_op"], E["operator"]); row += 1
    _pair(ws, row, L["employer_prefix"], E["prefix"], L["employer_gen"], E["gendate"]); row += 1
    _pair(ws, row, L["employer_cune"], E["cune"]); row += 1

    # ---------------- employee ---------------------------------------------
    _section(ws, row, L["sec_employee"]); row += 1
    P = D.EMPLOYEE
    _pair(ws, row, L["emp_name"], P["name"], L["emp_doc"], P["doc"]); row += 1
    _pair(ws, row, L["emp_code"], P["code"], L["emp_pos"], P["position"]); row += 1
    _pair(ws, row, L["emp_dep"], P["department"], L["emp_contract"], P["contract"]); row += 1
    _pair(ws, row, L["emp_hire"], P["hire"], L["emp_service"], P["service"]); row += 1
    _pair(ws, row, L["emp_wtype"], P["worker_type"], L["emp_freq"], P["frequency"]); row += 1
    _pair(ws, row, L["emp_eps"], P["eps"], L["emp_afp"], P["afp"]); row += 1
    _pair(ws, row, L["emp_ces"], P["cesantias"], L["emp_ccf"], P["ccf"]); row += 1
    _pair(ws, row, L["emp_days"], P["days_worked"], L["emp_abs"], P["days_absent"]); row += 1
    _pair(ws, row, L["emp_mod"], P["modality"], L["emp_pay"], P["payment"]); row += 1
    _pair(ws, row, L["emp_tax"], P["tax_status"]); row += 1

    # ---------------- earnings ---------------------------------------------
    _section(ws, row, L["sec_earn"]); row += 1
    _tablehead(ws, row, L["col_item"], L["col_rate"], L["col_unit"], L["col_amount"]); row += 1
    R["earn_first"] = row
    ekeys = ["basic", "hed", "rn", "com", "bonNS", "aux"]
    for i, (code, en, sp, rate, unit, ufmt, amount) in enumerate(D.EARNINGS):
        name = ("XXXXX - Earning pay element %d" % (i + 1)) if master else \
               "%s - %s" % (code, sp if es else en)
        ufmt_x = None
        if ufmt == "HOURS":
            ufmt_x = HOURS
        elif ufmt == "DAYS":
            unit = "30 dias" if es else "30 days"
        amt = amount
        if amount is None:
            amt = "=ROUND(F%d*G%d,2)" % (row, row)
        _dataline(ws, row, name, rate, unit, ufmt_x, amt, i % 2 == 1)
        R[ekeys[i]] = row
        row += 1
    R["earn_last"] = row - 1
    R["gross"] = row
    _totalline(ws, row, L["tot_earn"],
               "=SUM(H%d:H%d)" % (R["earn_first"], R["earn_last"])); row += 1

    # ---------------- statutory bases --------------------------------------
    _section(ws, row, L["sec_base"]); row += 1
    R["ibc"] = row
    _calcline(ws, row, L["base_ibc"], "=ROUNDUP(H%d+H%d+H%d+H%d,0)"
              % (R["basic"], R["hed"], R["rn"], R["com"])); row += 1
    R["para"] = row
    _calcline(ws, row, L["base_para"], "=H%d" % R["ibc"], shade=True); row += 1
    R["prest"] = row
    _calcline(ws, row, L["base_prest"], "=ROUND(H%d+H%d+H%d+H%d+H%d,2)"
              % (R["basic"], R["hed"], R["rn"], R["com"], R["aux"])); row += 1
    R["vac"] = row
    _calcline(ws, row, L["base_vac"], "=ROUND(H%d+H%d+H%d,2)"
              % (R["basic"], R["rn"], R["com"]), shade=True); row += 1

    # ---------------- withholding depuration -------------------------------
    _section(ws, row, L["sec_tax"]); row += 1
    R["tax_a"] = row
    _calcline(ws, row, L["tax_a"], "=H%d" % R["gross"]); row += 1
    R["tax_b"] = row
    tax_b_row = row
    row += 1
    R["tax_c"] = row
    _calcline(ws, row, L["tax_c"], "=ROUND(H%d+H%d,2)" % (R["tax_a"], R["tax_b"]),
              shade=True); row += 1
    R["tax_d"] = row
    tax_d_row = row
    row += 1
    R["tax_e"] = row
    _calcline(ws, row, L["tax_e"],
              "=-MIN(ROUND((H%d+H%d)*0.25,2),ROUND(790/12*%d,2))"
              % (R["tax_c"], R["tax_d"], D.UVT), shade=True); row += 1
    R["tax_f"] = row
    _calcline(ws, row, L["tax_f"],
              "=-MIN(-(H%d+H%d),ROUND(H%d*0.4,2),ROUND(1340/12*%d,2))"
              % (R["tax_d"], R["tax_e"], R["tax_c"], D.UVT)); row += 1
    R["tax_g"] = row
    _calcline(ws, row, L["tax_g"], "=ROUND(H%d+H%d,2)" % (R["tax_c"], R["tax_f"]),
              shade=True); row += 1
    R["tax_h"] = row
    _calcline(ws, row, L["tax_h"], "=ROUND(H%d/%d,4)" % (R["tax_g"], D.UVT), fmt=NUM4)
    row += 1
    R["tax_i"] = row
    _calcline(ws, row, L["tax_i"],
              "=ROUND((H%d-95*%d)*0.19,2)" % (R["tax_g"], D.UVT), shade=True); row += 1

    # ---------------- deductions -------------------------------------------
    _section(ws, row, L["sec_ded"]); row += 1
    _tablehead(ws, row, L["col_ded"], L["col_rate"], L["col_unit"], L["col_amount"]); row += 1
    R["ded_first"] = row
    dkeys = ["salud", "pension", "fsp", "tax", "prepaid", "libranza"]
    for i, (code, en, sp, rate, key) in enumerate(D.DEDUCTIONS):
        name = ("XXXXX - Deduction pay element %d" % (i + 1)) if master else \
               "%s - %s" % (code, sp if es else en)
        if key == "IBC*0.04":
            amt = "=ROUND($H$%d*0.04,2)" % R["ibc"]
        elif key == "IBC*0.01":
            amt = "=ROUND($H$%d*0.01,2)" % R["ibc"]
        elif key == "TAX":
            amt = "=H%d" % R["tax_i"]
        else:
            amt = key
        _dataline(ws, row, name, None, None, None, amt, i % 2 == 1)
        ws.cell(row, 6).value = rate
        ws.cell(row, 6).alignment = CENTER
        R[dkeys[i]] = row
        row += 1
    R["ded_last"] = row - 1
    R["ded_total"] = row
    _totalline(ws, row, L["tot_ded"],
               "=SUM(H%d:H%d)" % (R["ded_first"], R["ded_last"])); row += 1
    R["net"] = row
    _totalline(ws, row, L["net"], "=H%d-H%d" % (R["gross"], R["ded_total"]),
               fill_rgb=GREEN); row += 1
    ws.row_dimensions[R["net"]].height = 18

    # deferred tax rows B and D (they reference deduction rows written above)
    _calcline(ws, tax_b_row, L["tax_b"],
              "=-ROUND(H%d+H%d+H%d,2)" % (R["salud"], R["pension"], R["fsp"]),
              shade=True)
    _calcline(ws, tax_d_row, L["tax_d"],
              "=-MIN(H%d,ROUND(16*%d,2))" % (R["prepaid"], D.UVT))

    # ---------------- employer contributions -------------------------------
    _section(ws, row, L["sec_er"]); row += 1
    _tablehead(ws, row, L["col_contrib"], L["col_rate"], L["col_unit"], L["col_amount"]); row += 1
    R["er_first"] = row
    for i, (code, en, sp, rate, key) in enumerate(D.EMPLOYER_CONTRIB):
        name = ("XXXXX - Employer contribution pay element %d" % (i + 1)) if master else \
               "%s - %s" % (code, sp if es else en)
        if key == "ZERO":
            amt = 0.00
        elif key == "PARA*0.04":
            amt = "=ROUND($H$%d*0.04,2)" % R["para"]
        else:
            factor = key.split("*")[1]
            amt = "=ROUND($H$%d*%s,2)" % (R["ibc"], factor)
        _put(ws, "A%d:E%d" % (row, row), name, ORANGE, val_font(), LEFT)
        _put(ws, "F%d" % row, rate, ORANGE, val_font(), CENTER)
        _put(ws, "G%d" % row, None, ORANGE, val_font(), CENTER)
        _put(ws, "H%d:%s%d" % (row, LAST, row), amt, ORANGE, val_font(), RIGHT, ACC2)
        ws.row_dimensions[row].height = 13.0
        row += 1
    R["er_last"] = row - 1
    R["er_total"] = row
    _totalline(ws, row, L["tot_er"],
               "=SUM(H%d:H%d)" % (R["er_first"], R["er_last"]), fill_rgb=ORANGE); row += 1

    # ---------------- provisions -------------------------------------------
    _section(ws, row, L["sec_prov"]); row += 1
    _tablehead(ws, row, L["col_contrib"], L["col_rate"], L["col_unit"], L["col_amount"]); row += 1
    R["prov_first"] = row
    for i, (code, en, sp, rate, key) in enumerate(D.PROVISIONS):
        name = ("XXXXX - Employer accrual pay element %d" % (i + 1)) if master else \
               "%s - %s" % (code, sp if es else en)
        if key == "PREST/12":
            amt = "=ROUND($H$%d/12,2)" % R["prest"]
        elif key == "PREST*0.01":
            amt = "=ROUND($H$%d*0.01,2)" % R["prest"]
        else:
            amt = "=ROUND($H$%d/24,2)" % R["vac"]
        _dataline(ws, row, name, None, None, None, amt, i % 2 == 1)
        ws.cell(row, 6).value = rate
        ws.cell(row, 6).alignment = CENTER
        row += 1
    R["prov_last"] = row - 1
    R["prov_total"] = row
    _totalline(ws, row, L["tot_prov"],
               "=SUM(H%d:H%d)" % (R["prov_first"], R["prov_last"])); row += 1
    R["cost"] = row
    _totalline(ws, row, L["tot_cost"], "=H%d+H%d+H%d"
               % (R["gross"], R["er_total"], R["prov_total"])); row += 1

    # ---------------- leave balances ---------------------------------------
    _section(ws, row, L["sec_leave"]); row += 1
    _put(ws, "A%d:D%d" % (row, row), L["leave_type"], GRAY_LBL, lbl_font(), LEFT)
    _put(ws, "E%d" % row, L["leave_ent"], GRAY_LBL, lbl_font(), CENTER)
    _put(ws, "F%d" % row, L["leave_taken"], GRAY_LBL, lbl_font(), CENTER)
    _put(ws, "G%d:H%d" % (row, row), L["leave_bal"], GRAY_LBL, lbl_font(), CENTER)
    _put(ws, "I%d:%s%d" % (row, LAST, row), L["leave_note"], GRAY_LBL, lbl_font(), CENTER)
    ws.row_dimensions[row].height = 14.0
    row += 1
    R["leave_first"] = row
    for i, (en, sp, ent, taken, note) in enumerate(D.LEAVE):
        bg = ALT if i % 2 else None
        _put(ws, "A%d:D%d" % (row, row), sp if es else en, bg, val_font(), LEFT)
        _put(ws, "E%d" % row, ent, bg, val_font(), RIGHT, DAYS2)
        _put(ws, "F%d" % row, taken, bg, val_font(), RIGHT, DAYS2)
        _put(ws, "G%d:H%d" % (row, row), "=E%d-F%d" % (row, row), bg,
             lbl_font(8), RIGHT, DAYS2)
        _put(ws, "I%d:%s%d" % (row, LAST, row), note, bg, val_font(7), LEFT)
        ws.row_dimensions[row].height = 13.0
        row += 1
    R["leave_last"] = row - 1

    # ---------------- year to date -----------------------------------------
    _section(ws, row, L["sec_ytd"]); row += 1
    R["ytd_first"] = row
    for i, (en, sp, amount) in enumerate(D.YTD):
        _calcline(ws, row, sp if es else en, amount, shade=i % 2 == 1)
        row += 1
    R["ytd_last"] = row - 1

    # ---------------- banking ----------------------------------------------
    _section(ws, row, L["sec_bank"]); row += 1
    _put(ws, "A%d:C%d" % (row, row), L["bank_ben"], GRAY_LBL, lbl_font(), LEFT)
    _put(ws, "D%d:E%d" % (row, row), L["bank_bank"], GRAY_LBL, lbl_font(), LEFT)
    _put(ws, "F%d:G%d" % (row, row), L["bank_type"], GRAY_LBL, lbl_font(), LEFT)
    _put(ws, "H%d:%s%d" % (row, LAST, row), L["bank_no"], GRAY_LBL, lbl_font(), LEFT)
    ws.row_dimensions[row].height = 14.0
    row += 1
    B = D.BANK
    _put(ws, "A%d:C%d" % (row, row), B["beneficiary"], None, val_font(), LEFT)
    _put(ws, "D%d:E%d" % (row, row), B["bank"], None, val_font(), LEFT)
    _put(ws, "F%d:G%d" % (row, row), B["acct_type"], None, val_font(), LEFT)
    _put(ws, "H%d:%s%d" % (row, LAST, row), B["acct_no"], None, val_font(), LEFT)
    ws.row_dimensions[row].height = 13.5
    row += 1

    # ---------------- statutory notes --------------------------------------
    _section(ws, row, L["sec_notes"]); row += 1
    from co_payslip_text import NOTES_EN, NOTES_ES, NOTES_MASTER
    notes = NOTES_MASTER if master else (NOTES_ES if es else NOTES_EN)
    R["notes_first"] = row
    for i, note in enumerate(notes):
        _put(ws, "A%d:%s%d" % (row, LAST, row), "* " + note,
             ALT if i % 2 == 0 else None, val_font(7, italic=True), LEFT_WRAP)
        ws.row_dimensions[row].height = max(24, 9.0 * (len(note) // 155 + 1))
        row += 1
    R["notes_last"] = row - 1

    # ---------------- footer -----------------------------------------------
    row += 1
    _put(ws, "A%d:%s%d" % (row, LAST, row), L["footer"], NAVY,
         Font(name="Arial", size=8, bold=True, color="FFFFFF"), CENTER)
    ws.row_dimensions[row].height = 15.0
    row += 1
    _put(ws, "A%d:%s%d" % (row, LAST, row), L["ref"], None,
         val_font(7, italic=True), CENTER)
    R["footer"] = row

    # net-pay highlight beside the title
    net_box.value = "=H%d" % R["net"]
    ws.freeze_panes = "A6"
    return R

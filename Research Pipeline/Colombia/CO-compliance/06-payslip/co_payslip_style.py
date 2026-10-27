# -*- coding: utf-8 -*-
"""Shared v2.7 formatting tokens for the Colombia Compliance Payslip Generator."""

from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

NAVY = "1F3864"
GRAY_HDR = "A9A9A9"     # section headers
GRAY_LBL = "DCDCDC"     # field labels / table column headers
ALT = "F2F2F2"          # alternating data rows
GREEN = "C6EFCE"        # net pay
ORANGE = "FCE4D6"       # employer contributions (informative)
WHITE = "FFFFFF"

FONT = "Arial"

# accounting formats - 2 decimals for currencies WITH a minor unit (COP),
# integer variant kept here for zero-minor-unit currencies re-using this module
ACC2 = '_(* #,##0.00_);_(* \\(#,##0.00\\);_(* "-"??_);_(@_)'
ACC0 = '_(* #,##0_);_(* \\(#,##0\\);_(* "-"??_);_(@_)'
NUM4 = '#,##0.0000'
DAYS2 = '#,##0.00'
HOURS = '0.00" h"'

THIN = Side(style="thin", color="7F7F7F")
BORDER = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)


def fill(rgb):
    return PatternFill("solid", fgColor=rgb)


def title_font(size=15):
    return Font(name=FONT, size=size, bold=True, color=WHITE)


def hdr_font(size=9):
    return Font(name=FONT, size=size, bold=True, color=WHITE)


def lbl_font(size=8):
    return Font(name=FONT, size=size, bold=True)


def val_font(size=8, bold=False, italic=False):
    return Font(name=FONT, size=size, bold=bold, italic=italic)


LEFT = Alignment(horizontal="left", vertical="center", wrap_text=False)
LEFT_WRAP = Alignment(horizontal="left", vertical="top", wrap_text=True)
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=False)
RIGHT = Alignment(horizontal="right", vertical="center", wrap_text=False)


def paint(ws, ref, fill_rgb=None, font=None, align=None, fmt=None, border=True):
    """Apply style tokens to every cell of a range (works on merged ranges too)."""
    from openpyxl.utils import range_boundaries
    mn_col, mn_row, mx_col, mx_row = range_boundaries(ref)
    for r in range(mn_row, mx_row + 1):
        for c in range(mn_col, mx_col + 1):
            cell = ws.cell(r, c)
            if fill_rgb:
                cell.fill = fill(fill_rgb)
            if font:
                cell.font = font
            if align:
                cell.alignment = align
            if fmt:
                cell.number_format = fmt
            if border:
                cell.border = BORDER

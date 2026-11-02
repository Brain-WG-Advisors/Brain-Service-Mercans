# Shared helpers for the Colombia simulation workbooks (style copied from the France model).
import json, os, datetime
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.workbook.defined_name import DefinedName
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.utils import get_column_letter

VAL = r"C:\Users\instituto\Documents\brain-service\Research Pipeline\Colombia\2026-10-29-validacao-research"
ORA = os.path.join(VAL, "oracle")

NAVY = "1F3864"; HEAD = "3B5F90"; INPUT = "FFF2CC"; RES = "D7E2F8"; SECT2 = "D9D9D9"
F_TITLE = Font(name="Arial", size=13, bold=True, color=NAVY)
F_SUB = Font(name="Arial", size=10, bold=True, color=NAVY)
F_TXT = Font(name="Arial", size=10)
F_TXTI = Font(name="Arial", size=9, italic=True, color="595959")
F_LINK = Font(name="Arial", size=9, bold=True, color="0563C1", underline="single")
F_SECT = Font(name="Arial", size=11, bold=True, color="FFFFFF")
F_HEAD = Font(name="Arial", size=10, bold=True, color="FFFFFF")
F_IN = Font(name="Arial", size=10, color="0000FF")
F_BOLD = Font(name="Arial", size=10, bold=True)
FILL = lambda c: PatternFill("solid", fgColor=c)
NUM = '#,##0.00_);[Red](#,##0.00)'
NUM0 = '#,##0_);[Red](#,##0)'
PCT = '0.000%'
THIN = Side(style="thin", color="BFBFBF")
BOX = Border(left=THIN, right=THIN, top=THIN, bottom=THIN)
WRAP = Alignment(wrap_text=True, vertical="top")

def load(p):
    return json.load(open(p, encoding="utf-8"))

def oracle_results():
    r = load(os.path.join(ORA, "results-v2r4-20261030-133546.json"))
    n = load(os.path.join(ORA, "results-v2r4-novos-20261030-133546.json"))
    rr = load(os.path.join(ORA, "results-research-v2r4-20261030-133546.json"))
    d = {x["id"]: x for x in r["results"]}
    dn = {x["id"]: x for x in n["results"]}
    drr = {x["id"]: x for x in rr["results"]}
    return d, dn, drr

def cases():
    c = load(os.path.join(ORA, "cases.json"))["cases"]
    v = load(os.path.join(ORA, "cases_v2r4.json"))["cases"]
    rc = load(os.path.join(ORA, "cases_research.json"))["cases"]
    return {x["id"]: x for x in c}, {x["id"]: x for x in v}, {x["id"]: x for x in rc}

# ---------------- Parameters (value, unit, English description, primary source) ----------------
PARAMS = [
 # name, description, value, unit, source
 ("SMMLV", "Legal monthly minimum wage 2026", 1750905, "COP", "Decree 1469 of 29 Dec 2025 art. 1 (Consejo de Estado lifted the provisional suspension on 9 Jul 2026; Decree 0159 of 2026 set the same value meanwhile)"),
 ("UVT", "Tax value unit 2026", 52374, "COP", "Resolution DIAN 000238 of 15 Dec 2025 art. 1"),
 ("AUX", "Transport allowance 2026 (monthly)", 249095, "COP", "Decree 1470 of 2025 art. 1"),
 ("AUX_CAP", "Transport allowance due up to this many minimum wages (inclusive)", 2, "x SMMLV", "Law 15 of 1959 art. 2; Decree 1470 of 2025 art. 1; prorated to days worked (Decree 1258 of 1959 art. 5)"),
 ("DIV1", "Monthly hours divisor, 44-hour week (from 15 Jul 2025)", 220, "hours", "Law 2101 of 2021 art. 3; CST art. 161 (Law 2466 of 2025 art. 11): weekly hours / 6 x 30"),
 ("DIV2", "Monthly hours divisor, 42-hour week", 210, "hours", "Law 2101 of 2021 art. 3: 42 hours from 15 Jul 2026"),
 ("DIV2_FROM", "Date from which the 42-hour divisor applies", datetime.date(2026, 7, 15), "date", "Law 2101 of 2021 art. 3"),
 ("DOM1", "Rest-day / holiday surcharge from 1 Jul 2025", 0.80, "rate", "CST art. 179 transitional paragraph (Law 2466 of 2025 art. 14)"),
 ("DOM2", "Rest-day / holiday surcharge from 1 Jul 2026", 0.90, "rate", "CST art. 179 transitional paragraph (Law 2466 of 2025 art. 14)"),
 ("DOM2_FROM", "Date of the 90% step", datetime.date(2026, 7, 1), "date", "CST art. 179 transitional paragraph"),
 ("DOM3", "Rest-day / holiday surcharge from 1 Jul 2027", 1.00, "rate", "CST art. 179 transitional paragraph"),
 ("DOM3_FROM", "Date of the 100% step", datetime.date(2027, 7, 1), "date", "CST art. 179 transitional paragraph"),
 ("REC_RN", "Night premium (ordinary night hours)", 0.35, "rate", "CST art. 168 num. 1"),
 ("REC_HED", "Daytime overtime premium", 0.25, "rate", "CST art. 168 num. 2"),
 ("REC_HEN", "Night overtime premium", 0.75, "rate", "CST art. 168 num. 3"),
 ("IBC_MIN", "Contribution base floor, in minimum wages (prorated to contributory days)", 1, "x SMMLV", "Law 100 of 1993 art. 18 (Law 797 of 2003 art. 5)"),
 ("IBC_MAX", "Contribution base ceiling, in minimum wages (prorated to contributory days)", 25, "x SMMLV", "Law 100 of 1993 art. 18 (Law 797 of 2003 art. 5)"),
 ("INTEGRAL_PCT", "All-inclusive salary: share of the salary that is the contribution and levy base", 0.70, "rate", "Law 100 of 1993 art. 18; CST art. 132 num. 3"),
 ("NS_MAX", "Pacted non-salary payments: maximum share of total remuneration", 0.40, "rate", "Law 1393 of 2010 art. 30; Consejo de Estado SU exp. 25185 of 9 Dec 2021, rule 3"),
 ("SAL_EE", "Health, employee", 0.04, "rate", "Law 100 of 1993 art. 204 (Law 1122 of 2007 art. 10)"),
 ("SAL_ER", "Health, employer", 0.085, "rate", "Law 100 of 1993 art. 204 (Law 1122 of 2007 art. 10)"),
 ("PEN_TOT", "Pension, total rate", 0.16, "rate", "Law 100 of 1993 art. 20 (Law 797 of 2003 art. 7)"),
 ("PEN_ER_SHARE", "Pension, employer share of the total", 0.75, "rate", "Law 100 of 1993 art. 20 (Law 797 of 2003 art. 7)"),
 ("FSP_MIN", "Solidarity pension fund: applies from this many minimum wages (inclusive)", 4, "x SMMLV", "Law 100 of 1993 arts. 20 and 27 (Law 797 of 2003 arts. 7 and 8)"),
 ("FSP_SOL", "Solidarity pension fund, solidarity sub-account", 0.005, "rate", "Law 100 of 1993 arts. 20 and 27 (Law 797 of 2003 arts. 7 and 8); PILA Technical Annex 2 field 51"),
 ("FSP_SUB", "Solidarity pension fund, subsistence sub-account (base)", 0.005, "rate", "Law 100 of 1993 arts. 20 and 27 (Law 797 of 2003 arts. 7 and 8); PILA Technical Annex 2 field 52"),
 ("FSP_B1", "Subsistence surcharge, IBC from 16 to 17 minimum wages (16 inclusive)", 0.002, "rate", "Law 797 of 2003 arts. 7 and 8; PILA Technical Annex 2 v30 field 52"),
 ("FSP_B2", "Subsistence surcharge, IBC above 17 up to 18", 0.004, "rate", "idem"),
 ("FSP_B3", "Subsistence surcharge, IBC above 18 up to 19", 0.006, "rate", "idem"),
 ("FSP_B4", "Subsistence surcharge, IBC above 19 up to 20", 0.008, "rate", "idem"),
 ("FSP_B5", "Subsistence surcharge, IBC above 20", 0.010, "rate", "idem"),
 ("EXON_LIM", "Art. 114-1 exoneration: salary payments and IBC strictly below this many minimum wages", 10, "x SMMLV", "Tax Code art. 114-1 (Law 1819 of 2016 art. 65); DIAN Conceptos 8380 of 2024 and 7196 of 2025; PILA Technical Annex 2 v30 field 76"),
 ("CCF", "Family compensation fund (employer)", 0.04, "rate", "Law 21 of 1982 arts. 12 and 17"),
 ("SENA", "Apprenticeship training levy (employer)", 0.02, "rate", "Law 21 of 1982 art. 12"),
 ("ICBF", "Family welfare levy (employer)", 0.03, "rate", "Law 89 of 1988 art. 1"),
 ("ARL_I", "Occupational risk class I, initial rate", 0.00522, "rate", "Decree 1772 of 1994 art. 13; Decree 1072 of 2015 art. 2.2.4.3.5"),
 ("ARL_II", "Occupational risk class II, initial rate", 0.01044, "rate", "idem"),
 ("ARL_III", "Occupational risk class III, initial rate", 0.02436, "rate", "idem"),
 ("ARL_IV", "Occupational risk class IV, initial rate", 0.04350, "rate", "idem"),
 ("ARL_V", "Occupational risk class V, initial rate", 0.06960, "rate", "idem"),
 ("RET_DEP_PCT", "Dependants deduction, share of gross labour income", 0.10, "rate", "Tax Code art. 387; Decree 1625 of 2016 art. 1.2.4.1.6 num. 4.3"),
 ("RET_DEP_UVT", "Dependants deduction, monthly maximum", 32, "UVT", "idem"),
 ("RET_PREP_UVT", "Prepaid health payments, monthly maximum", 16, "UVT", "Tax Code art. 387; Decree 1625 of 2016 art. 1.2.4.1.6 num. 4.2"),
 ("RET_VIV_UVT", "Mortgage interest, monthly maximum", 100, "UVT", "Tax Code art. 119; Decree 1625 of 2016 art. 1.2.4.1.23"),
 ("RET_AFC_PCT", "Voluntary pension / AFC savings exempt, share of labour income", 0.30, "rate", "Tax Code arts. 126-1 and 126-4"),
 ("RET_AFC_UVT", "Voluntary pension / AFC savings exempt, annual maximum (monthly = /12)", 3800, "UVT", "Tax Code arts. 126-1 and 126-4"),
 ("RET_E25_PCT", "Exempt labour income", 0.25, "rate", "Tax Code art. 206 num. 10 (Law 2277 of 2022 art. 2)"),
 ("RET_E25_UVT", "Exempt labour income, annual maximum (monthly = /12, operating convention)", 790, "UVT", "Tax Code art. 206 num. 10 (Law 2277 of 2022 art. 2)"),
 ("RET_CAP_PCT", "Deductions + exempt income cap, share of net income", 0.40, "rate", "Tax Code art. 336 num. 3 (Law 2277 of 2022 art. 7); Decree 1625 of 2016 art. 1.2.4.1.6 par. 3 (Decree 2231 of 2023)"),
 ("RET_CAP_UVT", "Deductions + exempt income cap, annual (monthly = /12, operating convention)", 1340, "UVT", "idem"),
 ("T_B1", "Art. 383 table: upper bound band 0 (0%)", 95, "UVT", "Tax Code art. 383; Decree 1625 of 2016 art. 1.2.4.1.17"),
 ("T_B2", "Art. 383 table: upper bound band 19%", 150, "UVT", "idem"),
 ("T_B3", "Art. 383 table: upper bound band 28%", 360, "UVT", "idem"),
 ("T_B4", "Art. 383 table: upper bound band 33%", 640, "UVT", "idem"),
 ("T_B5", "Art. 383 table: upper bound band 35%", 945, "UVT", "idem"),
 ("T_B6", "Art. 383 table: upper bound band 37%", 2300, "UVT", "idem"),
 ("T_R1", "Marginal rate > 95 to 150 UVT", 0.19, "rate", "idem"),
 ("T_R2", "Marginal rate > 150 to 360 UVT", 0.28, "rate", "idem"),
 ("T_R3", "Marginal rate > 360 to 640 UVT", 0.33, "rate", "idem"),
 ("T_R4", "Marginal rate > 640 to 945 UVT", 0.35, "rate", "idem"),
 ("T_R5", "Marginal rate > 945 to 2,300 UVT", 0.37, "rate", "idem"),
 ("T_R6", "Marginal rate > 2,300 UVT", 0.39, "rate", "idem"),
 ("T_F2", "Fixed UVT added from 150 UVT", 10, "UVT", "idem"),
 ("T_F3", "Fixed UVT added from 360 UVT", 69, "UVT", "idem"),
 ("T_F4", "Fixed UVT added from 640 UVT", 162, "UVT", "idem"),
 ("T_F5", "Fixed UVT added from 945 UVT", 268, "UVT", "idem"),
 ("T_F6", "Fixed UVT added from 2,300 UVT", 770, "UVT", "idem"),
 ("IND_UVT", "Dismissal indemnity: 20% withholding where monthly income exceeds", 204, "UVT", "Tax Code art. 401-3; Decree 1625 of 2016 art. 1.2.4.1.13"),
 ("IND_RATE", "Dismissal indemnity withholding rate above 204 UVT", 0.20, "rate", "Tax Code art. 401-3"),
 ("INT_CES", "Interest on severance savings, annual", 0.12, "rate", "Law 50 of 1990 art. 99 num. 2; Law 52 of 1975 art. 1"),
 ("VAC_DAYS", "Paid vacation per year of service", 15, "business days", "CST art. 186 num. 1"),
 ("VAC_COMP_MAX", "Share of vacation that may be paid in cash during employment", 0.5, "rate", "CST art. 189 num. 1"),
 ("INC_23", "General illness benefit, days 1-90", 2/3, "rate", "CST art. 227; Decree 780 of 2016 art. 3.2.1.10 par. 1 (days 1-2 paid by the employer)"),
 ("INC_12", "General illness benefit, days 91-180", 0.5, "rate", "CST art. 227"),
 ("MAT_WEEKS", "Maternity leave", 18, "weeks", "CST art. 236 num. 1 (Law 2114 of 2021)"),
 ("IND_LT10_FIRST", "Art. 64 indemnity, salary < 10 SMMLV: days for the first year", 30, "days", "CST art. 64 (Law 789 of 2002 art. 28)"),
 ("IND_LT10_ADD", "Art. 64 indemnity, salary < 10 SMMLV: days per further year (pro rata)", 20, "days", "idem"),
 ("IND_GE10_FIRST", "Art. 64 indemnity, salary >= 10 SMMLV: days for the first year", 20, "days", "idem"),
 ("IND_GE10_ADD", "Art. 64 indemnity, salary >= 10 SMMLV: days per further year (pro rata)", 15, "days", "idem"),
 ("APR_LECT", "Apprentice maintenance support, classroom phase (share of SMMLV)", 0.75, "rate", "CST art. 81 (Law 2466 of 2025 art. 21)"),
 ("APR_PRACT", "Apprentice maintenance support, practical phase (share of SMMLV)", 1.00, "rate", "CST art. 81 (Law 2466 of 2025 art. 21)"),
]
PARAM_VAL = {p[0]: p[2] for p in PARAMS}

def add_params_sheet(wb, title, note):
    ws = wb.create_sheet("Parameters")
    ws.sheet_properties.tabColor = NAVY
    ws["A1"] = title; ws["A1"].font = F_TITLE
    ws["A2"] = note; ws["A2"].font = F_TXTI
    hdr(ws, 4, ["Name", "Description", "Value", "Unit", "Source"], 1)
    r = 5
    for name, desc, val, unit, src in PARAMS:
        ws.cell(r, 1, name).font = F_BOLD
        ws.cell(r, 2, desc).font = F_TXT
        c = ws.cell(r, 3, val); c.font = F_IN; c.fill = FILL(INPUT)
        if unit == "rate":
            c.number_format = "0.000%"
        elif unit == "date":
            c.number_format = "yyyy-mm-dd"
        else:
            c.number_format = "#,##0.####"
        ws.cell(r, 4, unit).font = F_TXT
        ws.cell(r, 5, src).font = F_TXT
        for col in range(1, 6):
            ws.cell(r, col).border = BOX
        wb.defined_names["p_" + name] = DefinedName("p_" + name, attr_text="Parameters!$C$%d" % r)
        r += 1
    widths(ws, {"A": 18, "B": 70, "C": 16, "D": 12, "E": 110})
    ws.freeze_panes = "A5"
    return ws

def hdr(ws, row, labels, col0=1, fill=HEAD):
    for i, l in enumerate(labels):
        c = ws.cell(row, col0 + i, l)
        c.font = F_HEAD; c.fill = FILL(fill); c.alignment = Alignment(wrap_text=True, vertical="center"); c.border = BOX

def section(ws, row, text, ncols=15):
    for col in range(1, ncols + 1):
        ws.cell(row, col).fill = FILL(NAVY)
    c = ws.cell(row, 1, text); c.font = F_SECT

def widths(ws, d):
    for k, v in d.items():
        ws.column_dimensions[k].width = v

def okdiff_cf(ws, rng):
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"OK"'], fill=FILL("C6EFCE"), font=Font(name="Arial", size=10, bold=True, color="006100")))
    ws.conditional_formatting.add(rng, CellIsRule(operator="equal", formula=['"DIFF"'], fill=FILL("FFC7CE"), font=Font(name="Arial", size=10, bold=True, color="9C0006")))

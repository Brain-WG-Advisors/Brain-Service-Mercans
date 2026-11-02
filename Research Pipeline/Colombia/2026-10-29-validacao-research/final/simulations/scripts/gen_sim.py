# Generates CO_Simulation_2026_10_30_V1.0.xlsx (structure of FR_Simulation_2026_10_06_V1.0.xlsx).
import sys, os, re, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from colib import *
from casedesc import DESC, PENDING_EN
from openpyxl.worksheet.hyperlink import Hyperlink

OUT = sys.argv[1]
ORES, ONEW, ORC = oracle_results()
CASES, CNEW, CRC = cases()

COLS = ["Ordinal", "Regulation / line", "Base", "Rate / factor", "Research formula (the Excel formula of the result cell, shown as text)",
        "Research result", "Oracle rule (oracle_v2)", "Oracle formula (as implemented, from the law)", "Oracle result (value)",
        "Difference (research - oracle)", "Check", "Norm / notes", "Intermediate (design)", "EE / ER", "Taxability matrix (WTC v1.7 column)", "Case"]
WID = {"A": 9, "B": 46, "C": 16, "D": 11, "E": 46, "F": 16, "G": 26, "H": 46, "I": 16, "J": 12, "K": 8, "L": 60, "M": 13, "N": 7, "O": 22, "P": 7}
CHECKS = []   # (sheet, line, case, eeer, row, note)
FORMULA_ROWS = {}  # line label -> (words, generic, example cell, oracle rule, oracle formula)

class Block:
    """Collects entries for one sheet; resolves {placeholders} to cell refs after row assignment."""
    def __init__(self):
        self.e = []
    def add(self, kind, **kw):
        self.e.append((kind, kw))

def resolve(s, refs):
    if s is None:
        return None
    def rep(m):
        k = m.group(1)
        if k not in refs:
            raise KeyError(k)
        return refs[k]
    return re.sub(r"\{([A-Za-z0-9_\.]+)\}", rep, str(s))

def write_block(ws, blk, start_row, case_id, sheetname):
    # pass 1: rows
    r = start_row
    refs = {}
    rows = []
    for kind, kw in blk.e:
        rows.append(r)
        if kind == "inp":
            refs[kw["key"]] = "$D$%d" % r
        elif kind == "line":
            refs[kw["key"]] = "$F$%d" % r
            refs[kw["key"] + ".C"] = "$C$%d" % r
            refs[kw["key"] + ".D"] = "$D$%d" % r
        r += 1
    # pass 2: write
    for (kind, kw), row in zip(blk.e, rows):
        if kind == "section":
            section(ws, row, kw["text"], 16)
        elif kind == "sub":
            for col in range(1, 17):
                ws.cell(row, col).fill = FILL(SECT2)
            c = ws.cell(row, 1, kw["text"]); c.font = F_BOLD
        elif kind == "hdr":
            hdr(ws, row, kw["labels"], kw.get("col0", 1))
        elif kind == "ihdr":
            hdr(ws, row, ["Field", "HR code (design)", "Value", "Source / note"], 2)
        elif kind == "note":
            c = ws.cell(row, 2, kw["text"]); c.font = F_TXTI
        elif kind == "inp":
            ws.cell(row, 2, kw["label"]).font = F_TXT
            ws.cell(row, 3, kw.get("code", "")).font = F_TXT
            c = ws.cell(row, 4, kw["value"]); c.font = F_IN; c.fill = FILL(INPUT)
            fmt = kw.get("fmt")
            if isinstance(kw["value"], (datetime.date, datetime.datetime)):
                c.number_format = "yyyy-mm-dd"
            elif fmt:
                c.number_format = fmt
            elif isinstance(kw["value"], (int, float)):
                c.number_format = "#,##0.##"
            ws.cell(row, 5, kw.get("note", "")).font = F_TXT
            for col in range(2, 6):
                ws.cell(row, col).border = BOX
        elif kind == "line":
            f = resolve(kw["f"], refs)
            ws.cell(row, 1, kw.get("ord", "")).font = F_TXT
            ws.cell(row, 2, kw["label"]).font = F_BOLD if kw.get("bold") else F_TXT
            if kw.get("base"):
                c = ws.cell(row, 3, resolve(kw["base"], refs)); c.number_format = NUM
            if kw.get("rate"):
                c = ws.cell(row, 4, resolve(kw["rate"], refs)); c.number_format = kw.get("ratefmt", "0.000%")
            t = ws.cell(row, 5, f); t.data_type = "s"; t.font = Font(name="Consolas", size=8)
            c = ws.cell(row, 6, f); c.fill = FILL(RES); c.font = F_BOLD if kw.get("bold") else F_TXT
            c.number_format = kw.get("fmt", NUM)
            okey = kw.get("okey"); ores = kw.get("ores")
            ws.cell(row, 7, kw.get("orule", "")).font = F_TXT
            ws.cell(row, 8, kw.get("oform", "")).font = F_TXT
            tol = kw.get("tol", 0.01)
            if okey is not None and ores is not None and okey in ores:
                v = ores[okey]
                if isinstance(v, bool):
                    v = "Yes" if v else "No"
                ci = ws.cell(row, 9, v); ci.number_format = kw.get("fmt", NUM)
                if isinstance(v, str):
                    ws.cell(row, 10, None)
                    ws.cell(row, 11, '=IF(F%d=I%d,"OK","DIFF")' % (row, row))
                else:
                    ws.cell(row, 10, "=ROUND(F%d-I%d,6)" % (row, row)).number_format = "#,##0.00####"
                    ws.cell(row, 11, '=IF(ABS(J%d)<=%s,"OK","DIFF")' % (row, tol))
                ws.cell(row, 11).font = F_BOLD; ws.cell(row, 11).fill = FILL(RES)
                CHECKS.append((sheetname, kw["label_key"] if kw.get("label_key") else kw["label"], case_id, kw.get("eeer", ""), row, kw.get("norm", "")))
                lk = kw.get("label_key") or kw["label"]
                if lk not in FORMULA_ROWS:
                    FORMULA_ROWS[lk] = (kw.get("words", ""), f, "='%s'!$F$%d" % (sheetname, row), kw.get("orule", ""), kw.get("oform", ""))
            elif kw.get("na"):
                ws.cell(row, 9, "not available in the oracle").font = F_TXTI
                ws.cell(row, 11, "n/a").font = F_TXTI
            ws.cell(row, 12, kw.get("norm", "")).font = F_TXT
            ws.cell(row, 13, kw.get("acct", "")).font = F_TXT
            ws.cell(row, 14, kw.get("eeer", "")).font = F_TXT
            ws.cell(row, 15, kw.get("wtc", "")).font = F_TXT
            ws.cell(row, 16, case_id).font = F_TXTI
            for col in range(1, 17):
                ws.cell(row, col).border = BOX
    return r, refs

def sheet_head(ws, title, settings, howto):
    ws.sheet_properties.tabColor = "2F75B5"
    c = ws.cell(1, 1, "◄ Summary"); c.font = F_LINK; c.hyperlink = "#'Summary'!A1"
    ws.cell(1, 2, title).font = F_TITLE
    ws.cell(2, 2, settings).font = F_TXTI
    ws.cell(3, 2, howto).font = F_TXTI
    ws.cell(4, 2, '="Checks vs oracle:  OK "&COUNTIF(K:K,"OK")&"   |   DIFF "&COUNTIF(K:K,"DIFF")&"   |   not available in the oracle "&COUNTIF(K:K,"n/a")').font = F_SUB
    widths(ws, WID)
    ws.freeze_panes = "A5"

HOWTO = ("How to read: each line shows the research formula (column E, the formula of the yellow-blue result cell F) next to the independent oracle "
         "result (column I, a value). Difference = research - oracle; Check = OK when |difference| <= the line tolerance (0.01 COP unless stated).")
SET_STD = "Standard settings: full month (30-day convention), legal-person employer eligible for the Tax Code art. 114-1 exoneration, occupational risk class I, resident employee, withholding Procedure 1, 2026 parameters (sheet Parameters)."

ORULE = {
 "basic": ("monthly(): base_pay", "salary x days / 30"),
 "aux": ("monthly(): aux", "if not all-inclusive and salary <= 2 SMMLV: AUX x days / 30"),
 "exceso": ("monthly(): exceso", "max(pacted NS - 40% x (salary payments + pacted NS), 0)"),
 "ibc": ("monthly(): IBC", "ceil_peso(min(max(salary base x [70% if all-inclusive] + excess, SMMLV x days/30), 25 SMMLV x days/30))"),
 "ibcsm": ("monthly(): IBC_en_SMMLV", "IBC / (SMMLV x days / 30)"),
 "exon": ("monthly(): exonerado_114_1", "eligible AND salary payments < 10 SMMLV AND IBC < 10 SMMLV"),
 "contrib": ("monthly(): ceil100(IBC x rate)", "IBC x rate, rounded up to the next COP 100 per contributor and fund"),
 "levy": ("monthly(): ceil100(para_base x rate)", "max(salary base [x70% all-inclusive], floor) x rate, rounded up to COP 100; no Law 1393 excess"),
 "ret": ("retencion()", "Procedure 1 (Decree 1625 of 2016 art. 1.2.4.1.3)"),
}

def ret_tax_formula(b):
    return ("IF({b}<=p_T_B1,0,IF({b}<=p_T_B2,({b}-p_T_B1)*p_T_R1,IF({b}<=p_T_B3,({b}-p_T_B2)*p_T_R2+p_T_F2,IF({b}<=p_T_B4,({b}-p_T_B3)*p_T_R3+p_T_F3,"
            "IF({b}<=p_T_B5,({b}-p_T_B4)*p_T_R4+p_T_F4,IF({b}<=p_T_B6,({b}-p_T_B5)*p_T_R5+p_T_F5,({b}-p_T_B6)*p_T_R6+p_T_F6))))))").replace("{b}", b)

TYPE_EN = {"HED": "Daytime overtime", "HEN": "Night overtime", "RN": "Night premium (ordinary hours)", "DOM": "Rest-day / Sunday ordinary hours",
           "RN_DOM": "Night premium on a rest day", "HED_DOM": "Daytime overtime on a rest day", "HEN_DOM": "Night overtime on a rest day"}
def factor_expr(t, d):
    dom = "IF({d}>=p_DOM3_FROM,p_DOM3,IF({d}>=p_DOM2_FROM,p_DOM2,p_DOM1))".replace("{d}", d)
    return {"RN": "p_REC_RN", "HED": "(1+p_REC_HED)", "HEN": "(1+p_REC_HEN)", "DOM": "(1+%s)" % dom,
            "RN_DOM": "(1+p_REC_RN+%s)" % dom, "HED_DOM": "(1+p_REC_HED+%s)" % dom, "HEN_DOM": "(1+p_REC_HEN+%s)" % dom}[t]

MONTHS = {"2026-03": ("March 2026", datetime.date(2026, 3, 1)), "2026-06": ("June 2026", datetime.date(2026, 6, 1)),
          "2026-07": ("July 2026", datetime.date(2026, 7, 1)), "2026-08": ("August 2026", datetime.date(2026, 8, 1)),
          "2026-09": ("September 2026", datetime.date(2026, 9, 1))}

def monthly_block(c, ores):
    b = Block()
    per = MONTHS.get(c.get("period", "2026-03"))
    retention = c.get("retention", True)
    r = c.get("ret", {})
    b.add("section", text="1.  INPUTS - employee and period (yellow = input; fictitious test data)")
    b.add("ihdr")
    b.add("inp", key="period", label="Pay period", code="$period", value=per[0])
    b.add("inp", key="d1", label="First day of the period", code="$period.begin_date", value=per[1])
    b.add("inp", key="days", label="Contributory days in the month (30-day convention)", code="58295", value=c.get("days", 30), note="CST art. 134; Decree 780 of 2016 art. 3.2.1.5 (base prorated to contributory days)")
    b.add("inp", key="sal", label="Contractual monthly salary", code="Basic salary (WTC)", value=c["salary"], fmt=NUM0)
    b.add("inp", key="integral", label="All-inclusive salary? (Yes/No)", code="58201", value="Yes" if c.get("integral") else "No", note="CST art. 132 (>= 13 minimum wages, written agreement)")
    b.add("inp", key="comm", label="Commissions of the month (salary)", code="WTC Commissions", value=c.get("commission", 0), fmt=NUM0, note="CST art. 127")
    b.add("inp", key="ns", label="Non-salary payment of the month", code="WTC Non-Salary", value=c.get("nonsalary", 0), fmt=NUM0)
    b.add("inp", key="nskind", label="Non-salary kind (Pacted / Natural)", code="58202", value="Natural" if c.get("nonsalary_kind") == "natural" else "Pacted",
          note="Pacted = desalarised by written pact (Law 1393 art. 30 test); Natural = not remunerating the service (outside the test). CE SU 25185/2021")
    b.add("inp", key="nsnat", label="Additional non-salary by nature (taxable only)", code="WTC Non-Salary - non-remunerative", value=c.get("nonsalary_natural", 0), fmt=NUM0)
    b.add("inp", key="elig", label="Employer eligible for the art. 114-1 exoneration? (Yes/No)", code="58203", value="No" if c.get("exonerated") is False else "Yes", note="Tax Code art. 114-1: legal-person income-tax filer, or natural person with 2+ employees")
    b.add("inp", key="risk", label="Occupational risk class (I-V)", code="58204", value=c.get("risk", "I"))
    b.add("inp", key="wh", label="Withholding (Procedure 1 / None)", code="58206", value="Procedure 1" if retention else "None")
    b.add("inp", key="dep", label="Dependants deduction claimed? (Yes/No)", code="58207", value="Yes" if r.get("dependientes") else "No")
    b.add("inp", key="prep", label="Prepaid health paid in the month", code="WTC prepaid health", value=r.get("prepagada", 0), fmt=NUM0)
    b.add("inp", key="viv", label="Mortgage interest paid in the month", code="WTC mortgage interest", value=r.get("vivienda", 0), fmt=NUM0)
    b.add("inp", key="afc", label="Voluntary pension / AFC savings in the month", code="WTC AFC / AVP", value=r.get("afc", 0), fmt=NUM0)
    b.add("inp", key="dep72", label="Number of dependants (annual return only)", code="58207 (count)", value=r.get("dep72", 0), note="72 UVT each, max 4: annual return only (DIAN Concepto 011383 of 2024 IV.2)")
    ext = c.get("extras", [])
    if ext:
        b.add("note", text="Hours worked in the month (type, date, hours). Type codes: HED daytime overtime, HEN night overtime, RN night premium, DOM rest-day ordinary hours, *_DOM on a rest day.")
        for i, h in enumerate(ext):
            b.add("inp", key="h%dt" % i, label="Hours line %d - type" % (i + 1), code="WTC hours", value=h["type"], note=TYPE_EN[h["type"]])
            b.add("inp", key="h%dd" % i, label="Hours line %d - date worked" % (i + 1), code="", value=datetime.date.fromisoformat(h["date"]))
            b.add("inp", key="h%dn" % i, label="Hours line %d - hours" % (i + 1), code="", value=h["hours"])
    b.add("section", text="2.  EARNINGS - pay elements of the month")
    b.add("hdr", labels=COLS)
    b.add("line", key="basic", ord="10", label="Basic salary for the period", f="={sal}*{days}/30", okey="basic", ores=ores, orule=ORULE["basic"][0], oform=ORULE["basic"][1],
          norm="CST arts. 134 and 140 (30-day month)", acct="WTC basic", wtc="V Salary", words="Monthly salary x contributory days / 30")
    ext_keys = []
    for i, h in enumerate(ext):
        d = "{h%dd}" % i
        div = "IF(%s>=p_DIV2_FROM,p_DIV2,p_DIV1)" % d
        key = "x%d" % i
        ext_keys.append(key)
        b.add("line", key=key, ord="12", label="%s, %s, %s h" % (TYPE_EN[h["type"]], h["date"], h["hours"]),
              label_key="Hours: " + TYPE_EN[h["type"]],
              base="={sal}/%s" % div, rate="=" + factor_expr(h["type"], d), ratefmt="0.00",
              f="={h%dn}*{sal}/%s*%s" % (i, div, factor_expr(h["type"], d)),
              okey="extra_%s_%s" % (h["type"], h["date"]), ores=ores, orule="hours_line()", oform="hours x salary / divisor(date) x factor(type, date)",
              norm="CST arts. 168, 179 (Law 2466 of 2025 art. 14: 80% from 1 Jul 2025, 90% from 1 Jul 2026); divisor 220 / 210 from 15 Jul 2026 (Law 2101 of 2021 art. 3)",
              acct="58180", wtc="V Salary; X Vacation base: No", words="Hours x (salary / monthly divisor of the date) x (1 + premium); rest-day work = 100% + surcharge")
    if ext:
        b.add("line", key="extras", ord="12", label="Total overtime and premium hours", f="=" + "+".join("{%s}" % k for k in ext_keys), okey="extras_total", ores=ores,
              orule="monthly(): extras", oform="sum of hours lines", norm="CST art. 127 (salary)", acct="58180", label_key="Total overtime and premium hours", words="Sum of the hours lines")
    else:
        b.add("line", key="extras", ord="12", label="Total overtime and premium hours", f="=0", acct="58180")
    b.add("line", key="commx", ord="", label="Commissions", f="={comm}", norm="CST art. 127", wtc="V Salary")
    b.add("line", key="aux", ord="13", label="Transport allowance (non-salary by law)", f='=IF(AND({integral}="No",{sal}<=p_AUX_CAP*p_SMMLV),p_AUX*{days}/30,0)', okey="auxilio_transporte", ores=ores,
          orule=ORULE["aux"][0], oform=ORULE["aux"][1], norm="Law 15 of 1959 art. 2; Decree 1470 of 2025; prorated to days (Decree 1258 of 1959 art. 5)", acct="58109", wtc="V Non-Salary - non-remunerative",
          words="Allowance x days / 30 when salary <= 2 minimum wages and not all-inclusive")
    b.add("line", key="salpay", ord="16", label="Salary payments of the month", f="={basic}+{extras}+{commx}", acct="58101", wtc="V = Salary", bold=True)
    b.add("line", key="nspact", ord="17", label="Pacted non-salary payments", f='=IF({nskind}="Pacted",{ns},0)', acct="58102", wtc="V = Non-Salary - pacted")
    b.add("line", key="nsnatl", ord="", label="Non-salary payments by nature", f='=IF({nskind}="Natural",{ns},0)+{nsnat}', acct="", wtc="V = Non-Salary - non-remunerative")
    b.add("line", key="gross", ord="15", label="GROSS EARNINGS (total devengado)", f="={salpay}+{nspact}+{nsnatl}+{aux}", acct="58100", bold=True)
    b.add("section", text="3.  BASES - contribution base (IBC), Law 1393 test, payroll-levy base, art. 114-1 test")
    b.add("hdr", labels=COLS)
    b.add("line", key="totrem", ord="18", label="Total remuneration for the 40% test", f="={salpay}+{nspact}", acct="58103",
          norm="Law 1393 of 2010 art. 30; UGPP ABC Empleadores 2025 (salary + pacted non-salary); non-salary by nature outside (CE SU 25185/2021)")
    b.add("line", key="exc", ord="19", label="Law 1393 excess (pacted non-salary above 40%)", f="=MAX({nspact}-p_NS_MAX*{totrem},0)",
          okey="ley1393_exceso" if (c.get("nonsalary") or c.get("nonsalary_natural")) else None, ores=ores, orule=ORULE["exceso"][0], oform=ORULE["exceso"][1],
          norm="Law 1393 of 2010 art. 30; CE SU 25185 of 9 Dec 2021 rule 3", acct="58104", wtc="Q/U/R/S Yes/No (pacted)", words="Pacted non-salary above 40% of total remuneration")
    b.add("line", key="salbase", ord="20", label="Salary base after the all-inclusive factor", f='=IF({integral}="Yes",{salpay}*p_INTEGRAL_PCT,{salpay})', acct="58105",
          norm="Law 100 of 1993 art. 18 (70% of the all-inclusive salary); the excess is added without the 70% reduction (CE SU 25185/2021; CE 25907/2022)")
    b.add("line", key="floor", ord="", label="IBC floor (1 minimum wage x days / 30)", f="=p_IBC_MIN*p_SMMLV*{days}/30", norm="Law 100 of 1993 art. 18")
    b.add("line", key="cap", ord="", label="IBC ceiling (25 minimum wages x days / 30)", f="=p_IBC_MAX*p_SMMLV*{days}/30", norm="Law 100 of 1993 art. 18")
    b.add("line", key="ibc", ord="21", label="CONTRIBUTION BASE (IBC)", f="=ROUNDUP(ROUND(MIN(MAX({salbase}+{exc},{floor}),{cap}),6),0)", okey="IBC", ores=ores,
          orule=ORULE["ibc"][0], oform=ORULE["ibc"][1], norm="Law 100 of 1993 art. 18; Decree 780 of 2016 art. 3.2.1.5 num. 1 (rounded up to the whole peso)", acct="58106",
          wtc="Q Health / U Pension / R FSP / S ARL", bold=True, words="Salary base (+70% rule) + Law 1393 excess, floor 1 SMMLV, ceiling 25 SMMLV, rounded up to the peso")
    b.add("line", key="ibcsm", ord="22", label="IBC in minimum wages", f="={ibc}/(p_SMMLV*{days}/30)", okey="IBC_en_SMMLV", ores=ores, tol=0.000001, fmt="0.000000",
          orule=ORULE["ibcsm"][0], oform=ORULE["ibcsm"][1], norm="Law 797 of 2003 art. 8 (FSP bands measured in minimum wages)", acct="58107", words="IBC / (SMMLV x days / 30)")
    b.add("line", key="levy", ord="23", label="Payroll-levy base (CCF / SENA / ICBF)", f="={salbase}", acct="58108",
          norm="Law 21 of 1982 art. 17 (salary + paid rest; no floor, no ceiling); 70% for all-inclusive (CST art. 132 num. 3); Law 1393 excess never added (Law 1393 art. 30 covers Law 100 arts. 18 and 204 only)",
          wtc="T Payroll levies")
    b.add("line", key="exon", ord="25", label="Art. 114-1 exoneration applies? (Yes/No)",
          f='=IF(AND({elig}="Yes",{salpay}<p_EXON_LIM*p_SMMLV,{ibc}<p_EXON_LIM*p_SMMLV),"Yes","No")', okey="exonerado_114_1", ores=ores, fmt="General",
          orule=ORULE["exon"][0], oform=ORULE["exon"][1], acct="58210",
          norm="Tax Code art. 114-1; only the salary payments of the month count (DIAN Conceptos 8380 of 2024 and 7196 of 2025); IBC >= 10 SMMLV blocks it (PILA Annex 2 v30 field 76)",
          words="Employer eligible AND salary payments < 10 SMMLV AND IBC < 10 SMMLV")
    b.add("section", text="4.  SOCIAL SECURITY CONTRIBUTIONS AND PAYROLL LEVIES - research formula and result vs oracle")
    b.add("hdr", labels=COLS)
    C100 = "=ROUNDUP(ROUND({%s}*{%s.D},6)/100,0)*100"
    fsp_sol = "=IF({ibcsm}>=p_FSP_MIN,p_FSP_SOL,0)"
    fsp_sub = "=IF({ibcsm}>=p_FSP_MIN,p_FSP_SUB+IF({ibcsm}>20,p_FSP_B5,IF({ibcsm}>19,p_FSP_B4,IF({ibcsm}>18,p_FSP_B3,IF({ibcsm}>17,p_FSP_B2,IF({ibcsm}>=16,p_FSP_B1,0))))),0)"
    arl = '=CHOOSE(MATCH({risk},{"I","II","III","IV","V"},0),p_ARL_I,p_ARL_II,p_ARL_III,p_ARL_IV,p_ARL_V)'
    contrib = [
      ("hee", "31", "Health, employee 4%", "ibc", "=p_SAL_EE", "salud_trab", "EE", "58121", "Q Health", "Law 100 of 1993 art. 204 (Law 1122 of 2007 art. 10)"),
      ("pee", "32", "Pension, employee 4%", "ibc", "=p_PEN_TOT*(1-p_PEN_ER_SHARE)", "pension_trab", "EE", "58122", "U Pension", "Law 100 of 1993 art. 20 (Law 797 of 2003 art. 7): 16%, 25% employee"),
      ("fs1", "33", "Solidarity pension fund, solidarity 0.5% (IBC >= 4 SMMLV)", "ibc", fsp_sol, "fsp_solidaridad", "EE", "58123", "R FSP", "Law 100 of 1993 arts. 20 and 27 (Law 797 of 2003 arts. 7 and 8); PILA Annex 2 v30 field 51"),
      ("fs2", "34", "Solidarity pension fund, subsistence 0.5% + band 0.2%-1.0%", "ibc", fsp_sub, "fsp_subsistencia", "EE", "58124", "R FSP", "Law 797 of 2003 arts. 7 and 8 (16 inclusive; (17,18], (18,19], (19,20], >20); PILA Annex 2 v30 field 52"),
    ]
    for key, o, lab, bas, rate, ok, ee, acct, wtc, norm in contrib:
        b.add("line", key=key, ord=o, label=lab, base="={%s}" % bas, rate=rate, f=C100 % (bas, key), okey=ok, ores=ores, eeer=ee, acct=acct, wtc=wtc,
              orule=ORULE["contrib"][0], oform=ORULE["contrib"][1], norm=norm + "; Decree 780 of 2016 art. 3.2.1.5 num. 2 (up to the next COP 100)", words="IBC x rate, up to the next COP 100")
    b.add("line", key="totee", ord="39", label="Total employee contributions", f="={hee}+{pee}+{fs1}+{fs2}", eeer="EE", acct="58129", bold=True)
    contrib2 = [
      ("her", "41", "Health, employer 8.5% (0 when exonerated)", "ibc", '=IF({exon}="Yes",0,p_SAL_ER)', "salud_emp", "58141", "Q Health", "Law 100 of 1993 art. 204; Tax Code art. 114-1"),
      ("per", "42", "Pension, employer 12%", "ibc", "=p_PEN_TOT*p_PEN_ER_SHARE", "pension_emp", "58142", "U Pension", "Law 100 of 1993 art. 20 (Law 797 of 2003 art. 7)"),
      ("arl", "43", "Occupational risk (ARL), class rate", "ibc", arl, "arl", "58143", "S ARL", "Decree 1772 of 1994 art. 13; Decree 1072 of 2015 art. 2.2.4.3.5; IBC incl. Law 1393 excess (Decree-Law 1295 of 1994 art. 17)"),
      ("ccf", "44", "Family compensation fund 4% (never exonerated)", "levy", "=p_CCF", "ccf", "58144", "T Payroll levies", "Law 21 of 1982 arts. 12 and 17"),
      ("sena", "45", "SENA 2% (0 when exonerated)", "levy", '=IF({exon}="Yes",0,p_SENA)', "sena", "58145", "T Payroll levies", "Law 21 of 1982 art. 12; Tax Code art. 114-1"),
      ("icbf", "46", "ICBF 3% (0 when exonerated)", "levy", '=IF({exon}="Yes",0,p_ICBF)', "icbf", "58146", "T Payroll levies", "Law 89 of 1988 art. 1; Tax Code art. 114-1"),
    ]
    for key, o, lab, bas, rate, ok, acct, wtc, norm in contrib2:
        rule = ORULE["levy"] if bas == "levy" else ORULE["contrib"]
        b.add("line", key=key, ord=o, label=lab, base="={%s}" % bas, rate=rate, f=C100 % (bas, key), okey=ok, ores=ores, eeer="ER", acct=acct, wtc=wtc,
              orule=rule[0], oform=rule[1], norm=norm + "; up to the next COP 100 (Decree 780 of 2016 art. 3.2.1.5 num. 2)", words=("Payroll-levy base" if bas == "levy" else "IBC") + " x rate, up to the next COP 100")
    b.add("line", key="toter", ord="49", label="Total employer contributions and levies", f="={her}+{per}+{arl}+{ccf}+{sena}+{icbf}", eeer="ER", acct="58149", bold=True)
    b.add("section", text="5.  WITHHOLDING TAX - Procedure 1 depuration (Decree 1625 of 2016 art. 1.2.4.1.3) - research formula and result vs oracle")
    b.add("hdr", labels=COLS)
    R = lambda k: k if retention else None
    b.add("line", key="inc", ord="51", label="Taxable labour payments of the month", f="={salpay}+{ns}+{nsnat}+{aux}", okey=R("ret_ingreso_laboral"), ores=ores,
          orule="retencion(): income", oform="salary payments + non-salary + transport allowance", norm="Tax Code arts. 103 and 388", acct="58150", wtc="N Subject to tax", words="All labour payments of the month")
    b.add("line", key="incr", ord="52", label="Non-taxable income: mandatory employee contributions (before PILA rounding)",
          f="={ibc}*p_SAL_EE+{ibc}*p_PEN_TOT*(1-p_PEN_ER_SHARE)+{ibc}*{fs1.D}+{ibc}*{fs2.D}", okey=R("ret_incrngo_ss"), ores=ores,
          orule="retencion(): incrngo", oform="raw EE health + pension + FSP", norm="Tax Code arts. 55 and 56", acct="58151", words="IBC x (4% + 4% + FSP rates), unrounded")
    b.add("line", key="neti", ord="53", label="Net income", f="={inc}-{incr}", okey=R("ret_subtotal_tras_incrngo"), ores=ores, orule="retencion(): base1", oform="income - INCRNGO", acct="58152", norm="Tax Code art. 388", words="Income less non-taxable income")
    b.add("line", key="dedd", ord="54", label="Dependants deduction (10%, max 32 UVT)", f='=IF({dep}="Yes",MIN(p_RET_DEP_PCT*{inc},p_RET_DEP_UVT*p_UVT),0)', okey=R("ret_deduc_dependientes"), ores=ores,
          orule="retencion(): dep", oform="min(10% x income, 32 UVT)", norm="Tax Code art. 387; Decree 1625 of 2016 art. 1.2.4.1.6 num. 4.3", acct="58153", words="min(10% x gross labour income, 32 UVT)")
    b.add("line", key="dedp", ord="55", label="Prepaid health deduction (max 16 UVT)", f="=MIN({prep},p_RET_PREP_UVT*p_UVT)", okey=R("ret_deduc_prepagada"), ores=ores,
          orule="retencion(): prep", oform="min(paid, 16 UVT)", norm="Tax Code art. 387; Decree 1625 of 2016 art. 1.2.4.1.6 num. 4.2", acct="58154", words="min(paid, 16 UVT)")
    b.add("line", key="dedv", ord="56", label="Mortgage interest deduction (max 100 UVT)", f="=MIN({viv},p_RET_VIV_UVT*p_UVT)", okey=R("ret_deduc_vivienda"), ores=ores,
          orule="retencion(): viv", oform="min(paid, 100 UVT)", norm="Tax Code art. 119; Decree 1625 of 2016 art. 1.2.4.1.23", acct="58155", words="min(paid, 100 UVT)")
    b.add("line", key="afcx", ord="57", label="Voluntary pension / AFC exempt (30%, 3,800 UVT a year)", f="=MIN({afc},MIN(p_RET_AFC_PCT*{inc},p_RET_AFC_UVT*p_UVT/12))", okey=R("ret_exenta_afc"), ores=ores,
          orule="retencion(): afc_ex", oform="min(paid, 30% x income, 3,800 UVT / 12)", norm="Tax Code arts. 126-1 and 126-4", acct="58156", words="min(paid, 30% x income, 3,800 UVT / 12)")
    b.add("line", key="e25", ord="58", label="Exempt labour income 25% (computed last; 790 UVT a year)", f="=MIN(p_RET_E25_PCT*MAX({neti}-{dedd}-{dedp}-{dedv}-{afcx},0),p_RET_E25_UVT*p_UVT/12)",
          okey=R("ret_exenta_25"), ores=ores, orule="retencion(): e25", oform="min(25% x (net income - deductions - other exempt), 790 UVT / 12)",
          norm="Tax Code art. 206 num. 10 (Law 2277 of 2022 art. 2); monthly 790/12 is an operating convention", acct="58157", words="25% of the residue after all other reliefs, max 790 UVT / 12")
    b.add("line", key="capl", ord="59", label="Cap on deductions + exempt income (40% of net income, 1,340 UVT a year)", f="=MIN(p_RET_CAP_PCT*{neti},p_RET_CAP_UVT*p_UVT/12)",
          okey=R("ret_cap_40_1340"), ores=ores, orule="retencion(): cap", oform="min(40% x net income, 1,340 UVT / 12)",
          norm="Tax Code art. 336 num. 3; Decree 1625 of 2016 art. 1.2.4.1.6 par. 3 (Decree 2231 of 2023)", acct="58158", words="min(40% x net income, 1,340 UVT / 12)")
    b.add("line", key="appl", ord="59", label="Reliefs applied (within the cap)", f="=MIN({dedd}+{dedp}+{dedv}+{afcx}+{e25},MAX({capl},0))", okey=R("ret_beneficios_aplicados"), ores=ores,
          orule="retencion(): aplicado", oform="min(sum of reliefs, cap)", acct="58159", words="min(sum of reliefs, cap)", norm="Decree 1625 of 2016 art. 1.2.4.1.6 par. 3")
    b.add("line", key="d72", ord="", label="Information: 72 UVT per dependant (annual return only, NOT deducted here)", f="=MIN({dep72},4)*72*p_UVT/12",
          okey=R("ret_dep72_so_declaracao_anual"), ores=ores, orule="retencion(): dep72 (information)", oform="min(count, 4) x 72 UVT / 12, not deducted",
          norm="Tax Code art. 336 num. 3 (annual return); DIAN Concepto 011383 of 2024 IV.2 (art. 388 refers to art. 387, not 336)", words="Information only")
    b.add("line", key="base", ord="60", label="TAXABLE BASE", f="=MAX({neti}-{appl},0)", okey=R("ret_base_gravable"), ores=ores, orule="retencion(): base", oform="max(net income - reliefs applied, 0)", acct="58160", bold=True,
          norm="Tax Code art. 388", words="Net income less reliefs applied")
    b.add("line", key="buvt", ord="60", label="Taxable base in UVT", f="={base}/p_UVT", okey=R("ret_base_uvt"), ores=ores, fmt="0.0000", orule="retencion(): base_uvt", oform="base / UVT (oracle shows 2 decimals)", words="Base / UVT", norm="Tax Code art. 383")
    b.add("line", key="tuvt", ord="61", label="Tax in UVT (art. 383 table)", f="=" + ret_tax_formula("{buvt}"), okey=R("ret_impuesto_uvt"), ores=ores, fmt="0.0000",
          orule="retencion(): imp", oform="(base UVT - lower bound) x marginal rate + fixed UVT; intervals open on the left", norm="Tax Code art. 383; Decree 1625 of 2016 art. 1.2.4.1.17", words="Marginal table in UVT")
    b.add("line", key="wht", ord="61", label="WITHHOLDING TAX (Procedure 1)", f='=IF({wh}="Procedure 1",ROUND(ROUND({tuvt}*p_UVT,6),0),0)', okey=R("ret_valor_retener"), ores=ores,
          orule="retencion(): valor_retener", oform="tax UVT x UVT, rounded to the peso", acct="58161", bold=True, eeer="EE", norm="Tax Code art. 383; Decree 1625 of 2016 art. 1.2.4.1.3 (Procedure 1)", words="Tax UVT x UVT, rounded to the peso")
    b.add("section", text="6.  NET PAY")
    b.add("hdr", labels=COLS)
    b.add("line", key="net", ord="71", label="Net pay before PILA rounding (oracle convention: unrounded employee contributions)",
          f='={inc}-{incr}-IF({wh}="Procedure 1",{tuvt}*p_UVT,0)', okey="neto_aprox_raw", ores=ores, orule="monthly(): neto_aprox_raw",
          oform="income - raw EE contributions - raw withholding", acct="58170", bold=True, words="Payments less unrounded employee contributions and withholding", norm="CST art. 149 (only lawful deductions)")
    b.add("line", key="net2", ord="71", label="Net pay with the employee contributions as rounded for PILA (up to COP 100)", f="={inc}-{totee}-{wht}", na=True, acct="58170",
          norm="Open item: how the PILA-rounded total per fund is split between employee and employer is not stated in any source read (Decree 780 of 2016 art. 3.2.1.5 num. 2 rounds per contributor and fund)")
    b.add("line", key="cost", ord="49+", label="Total employer cost (gross + employer contributions and levies)", f="={gross}+{toter}", na=True, acct="", norm="Statutory benefit accruals (21.8333%) not included; see sheet Benefits")
    return b

def add_table383(ws, row, buvt_ref):
    section(ws, row, "7.  WITHHOLDING TABLE (Tax Code art. 383, in UVT) - reference", 16)
    hdr(ws, row + 1, ["", "From (UVT, exclusive)", "To (UVT, inclusive)", "Marginal rate", "Fixed UVT", "Band applied"], 1)
    bands = [("0", "p_T_B1", "0", "0"), ("p_T_B1", "p_T_B2", "p_T_R1", "0"), ("p_T_B2", "p_T_B3", "p_T_R2", "p_T_F2"), ("p_T_B3", "p_T_B4", "p_T_R3", "p_T_F3"),
             ("p_T_B4", "p_T_B5", "p_T_R4", "p_T_F4"), ("p_T_B5", "p_T_B6", "p_T_R5", "p_T_F5"), ("p_T_B6", "99999999", "p_T_R6", "p_T_F6")]
    for i, (lo, hi, rt, fx) in enumerate(bands):
        r = row + 2 + i
        ws.cell(r, 2, "=" + lo); ws.cell(r, 3, "=" + hi); c = ws.cell(r, 4, "=" + rt); c.number_format = "0%"; ws.cell(r, 5, "=" + fx)
        ws.cell(r, 6, '=IF(AND(%s>B%d,%s<=C%d),"<< applied","")' % (buvt_ref, r, buvt_ref, r)) if i else ws.cell(r, 6, '=IF(%s<=C%d,"<< applied","")' % (buvt_ref, r))
        for col in range(2, 7):
            ws.cell(r, col).border = BOX; ws.cell(r, col).font = F_TXT

# ---------------------------------------------------------------- workbook
wb = Workbook()
wsS = wb.active; wsS.title = "Scenario"
wsR = wb.create_sheet("Read me")
wsSum = wb.create_sheet("Summary")
add_params_sheet(wb, "Parameters 2026, Colombia - every research formula reads these cells through the defined names p_<Name>",
                 "Values: approved research (CCG v1.5, WTC v1.7) and the oracle parameter file (one primary source per value). Edit a yellow cell and every scenario sheet recalculates.")
SCEN = []  # (n, id, explanation, sheets, oracle ref, tab group)

monthly_ids = [k for k in CASES if CASES[k]["module"] == "monthly" and not CASES[k].get("pending")]
for cid in monthly_ids:
    c = CASES[cid]
    per = MONTHS[c.get("period", "2026-03")][0]
    sn = "%s %s" % (cid, per.split()[0][:3])
    ws = wb.create_sheet(sn)
    sheet_head(ws, "%s  %s, %s" % (cid, DESC[cid], per), SET_STD, HOWTO)
    blk = monthly_block(c, ORES[cid]["lines"])
    end, refs = write_block(ws, blk, 6, cid, sn)
    add_table383(ws, end + 1, refs["buvt"])
    SCEN.append((cid, DESC[cid], sn, "oracle case " + cid, "monthly"))

for i, cid in enumerate(["V01", "V02", "V03", "V04", "V05"]):
    did = "D0%d" % (i + 1)
    c = CNEW[cid]
    sn = "%s Mar" % did
    ws = wb.create_sheet(sn)
    sheet_head(ws, "%s  %s, March 2026" % (did, DESC[did]),
               "Decision case: no withholding computed by the oracle for this case (contributions only). " + SET_STD, HOWTO)
    blk = monthly_block(c, ONEW[cid]["lines"])
    end, refs = write_block(ws, blk, 6, did, sn)
    add_table383(ws, end + 1, refs["buvt"])
    SCEN.append((did, DESC[did], sn, "oracle decision case %s (30 Oct 2026)" % cid, "monthly"))

# ---------------- module sheets ----------------
def module_sheet(name, title, settings, tab="ED7D31"):
    ws = wb.create_sheet(name)
    sheet_head(ws, title, settings, HOWTO)
    ws.sheet_properties.tabColor = tab
    return ws

def run_blocks(ws, blocks):
    row = 6
    for cid, blk in blocks:
        row, _ = write_block(ws, blk, row, cid, ws.title)
        row += 1

# Withholding table T01-T18
ws = module_sheet("Withholding table", "T01-T18  Art. 383 withholding table - boundary cases (base exactly on, 1 peso below and 1 peso above each bound)",
                  "Base given in COP; the table is read in UVT (UVT 2026 = 52,374). Intervals are open on the left: a base exactly on a bound stays in the lower band.")
blocks = []
for cid in [k for k in CASES if CASES[k]["module"] == "ret_table"]:
    c = CASES[cid]; o = ORES[cid]["lines"]; b = Block()
    b.add("sub", text="%s  %s" % (cid, DESC[cid]))
    b.add("inp", key="bc", label="Taxable base (COP)", code="58160", value=c["base_cop"], fmt=NUM0)
    b.add("hdr", labels=COLS)
    b.add("line", key="bu", ord="60", label="Taxable base in UVT", f="={bc}/p_UVT", okey="base_uvt", ores=o, tol=0.000001, fmt="0.000000", orule="ret_table(): base_uvt", oform="base / UVT",
          label_key="Table 383: base in UVT", words="Base / UVT", norm="Tax Code art. 383")
    b.add("line", key="tu", ord="61", label="Tax in UVT", f="=" + ret_tax_formula("{bu}"), okey="impuesto_uvt", ores=o, tol=0.000001, fmt="0.000000", orule="ret_table(): imp",
          oform="(base UVT - lower bound) x marginal + fixed", label_key="Table 383: tax in UVT", words="Marginal table in UVT", norm="Tax Code art. 383; Decree 1625 of 2016 art. 1.2.4.1.17")
    b.add("line", key="vr", ord="61", label="Withholding (COP)", f="=ROUND(ROUND({tu}*p_UVT,6),0)", okey="valor_retener", ores=o, orule="ret_table(): valor_retener", oform="tax UVT x UVT, rounded to the peso",
          label_key="Table 383: withholding", words="Tax UVT x UVT, rounded", acct="58161", eeer="EE", norm="Tax Code art. 383")
    blocks.append((cid, b)); SCEN.append((cid, DESC[cid], ws.title, "oracle case " + cid, "module"))
run_blocks(ws, blocks)

# Benefits P01-P06
ws = module_sheet("Benefits", "P01-P06  Service bonus (prima), severance savings (cesantias) and interest",
                  "Base = monthly salary + transport allowance when salary <= 2 minimum wages (not all-inclusive). Commercial year of 360 days.")
blocks = []
for cid in [k for k in CASES if CASES[k]["module"] == "prestaciones"]:
    c = CASES[cid]; o = ORES[cid]["lines"]; b = Block()
    b.add("sub", text="%s  %s" % (cid, DESC[cid]))
    b.add("inp", key="s", label="Monthly salary", code="Basic salary (WTC)", value=c["salary"], fmt=NUM0)
    b.add("inp", key="d", label="Days of service in the period (360-day year)", code="58295 (period)", value=c["days"])
    b.add("hdr", labels=COLS)
    b.add("line", key="bb", ord="81", label="Benefits base (salary + transport allowance)", f="={s}+IF({s}<=p_AUX_CAP*p_SMMLV,p_AUX,0)", okey="base_prima_cesantias", ores=o, tol=0.5,
          orule="prestaciones(): base", oform="salary + AUX if salary <= 2 SMMLV", label_key="Benefits base", words="Salary + transport allowance (<= 2 SMMLV)",
          norm="CST arts. 249 and 306; Law 1 of 1963 art. 7 (transport allowance in the base); WTC column W", acct="58171", wtc="W Statutory-benefit base")
    if c["kind"] in ("prima", "all"):
        b.add("line", key="pr", ord="82", label="Service bonus (prima de servicios)", f="=ROUND(ROUND({bb}*{d}/360,6),0)", okey="prima", ores=o, orule="prestaciones(): prima",
              oform="base x days / 360, rounded", label_key="Service bonus", words="Base x days / 360", norm="CST art. 306 (30 days a year, paid half by 30 June and half by 20 December)", acct="58172", eeer="ER")
    if c["kind"] in ("cesantias", "all"):
        b.add("line", key="ce", ord="83", label="Severance savings (cesantias)", f="=ROUND(ROUND({bb}*{d}/360,6),0)", okey="cesantias", ores=o, orule="prestaciones(): cesantias",
              oform="base x days / 360, rounded", label_key="Severance savings", words="Base x days / 360", norm="CST art. 249; Law 50 of 1990 art. 99 num. 1-3 (deposit by 14 February)", acct="58173", eeer="ER")
        b.add("line", key="ic", ord="84", label="Interest on severance savings (12% a year, pro rata)", f="=ROUND(ROUND({bb}*{d}/360*{d}*p_INT_CES/360,6),0)", okey="intereses_cesantias", ores=o,
              orule="prestaciones(): intereses", oform="cesantias x days x 12% / 360, rounded", label_key="Interest on severance savings", words="Severance x days x 12% / 360",
              norm="Law 50 of 1990 art. 99 num. 2; Law 52 of 1975 art. 1 (paid to the employee in January)", acct="58174", eeer="ER")
    blocks.append((cid, b)); SCEN.append((cid, DESC[cid], ws.title, "oracle case " + cid, "module"))
run_blocks(ws, blocks)

# Vacation V01-V05
ws = module_sheet("Vacation", "V01-V05  Vacation taken, compensated in cash, mixed, and accrued on termination",
                  "Base = ordinary salary, excluding overtime and rest-day work (CST art. 192). 15 business days per year (CST art. 186).")
blocks = []
for cid in [k for k in CASES if CASES[k]["module"] == "vacaciones"]:
    c = CASES[cid]; o = ORES[cid]["lines"]; b = Block()
    b.add("sub", text="%s  %s" % (cid, DESC[cid]))
    b.add("inp", key="s", label="Ordinary monthly salary (vacation base)", code="WTC column X", value=c["salary"], fmt=NUM0)
    m = c["mode"]
    if m in ("gozadas", "compensadas"):
        b.add("inp", key="dh", label="Business days of vacation", code="", value=c["dias_habiles"])
    if m == "mixta":
        b.add("inp", key="g", label="Business days taken", code="", value=c["gozadas"]); b.add("inp", key="k", label="Business days compensated", code="", value=c["compensadas"])
    if m == "causacion":
        b.add("inp", key="dw", label="Days worked without vacation (360-day year)", code="", value=c["days_worked"])
    b.add("hdr", labels=COLS)
    if m == "gozadas":
        b.add("line", key="vd", ord="85", label="Vacation pay per day", f="=ROUND({s}/30,0)", okey="vac_valor_dia", ores=o, orule="vacaciones(): valor_dia", oform="salary / 30, rounded",
              label_key="Vacation: daily value", words="Salary / 30", norm="CST art. 192 num. 1", acct="58176")
        b.add("line", key="vp", ord="85", label="Vacation pay (taken)", f="=ROUND(ROUND({s}/30*{dh},6),0)", okey="vac_pago", ores=o, orule="vacaciones(): pago", oform="salary / 30 x days",
              label_key="Vacation pay", words="Salary / 30 x business days", norm="CST arts. 186, 192", acct="58176")
    elif m == "compensadas":
        b.add("line", key="mx", ord="85", label="Maximum business days that may be compensated in cash", f="=p_VAC_DAYS*p_VAC_COMP_MAX", okey="max_compensable_dias", ores=o, fmt="0.0",
              orule="vacaciones(): max", oform="15 x 50%", label_key="Vacation: compensable maximum", words="15 x 50%", norm="CST art. 189 num. 1")
        b.add("line", key="ex", ord="85", label="Request exceeds half? (Yes = not allowed)", f='=IF({dh}>{mx},"Yes","No")', okey="compensacion_excede_mitad", ores=o, fmt="General",
              orule="vacaciones(): excede", oform="days > maximum", label_key="Vacation: exceeds half", words="Days > maximum", norm="CST art. 189 num. 1")
        b.add("line", key="vp", ord="85", label="Vacation compensated in cash", f="=ROUND(ROUND({s}/30*{dh},6),0)", okey="vac_pago", ores=o, orule="vacaciones(): pago", oform="salary / 30 x days",
              label_key="Vacation pay", words="Salary / 30 x business days (not / 720 during employment)", norm="CST arts. 186, 189", acct="58176")
    elif m == "mixta":
        b.add("line", key="vg", ord="85", label="Vacation taken", f="=ROUND(ROUND({s}/30*{g},6),0)", okey="vac_pago_gozadas", ores=o, orule="vacaciones(): gozadas", oform="salary / 30 x days",
              label_key="Vacation pay", words="Salary / 30 x days", norm="CST art. 192", acct="58176")
        b.add("line", key="vk", ord="85", label="Vacation compensated", f="=ROUND(ROUND({s}/30*{k},6),0)", okey="vac_pago_compensadas", ores=o, orule="vacaciones(): compensadas", oform="salary / 30 x days",
              label_key="Vacation pay", words="Salary / 30 x days", norm="CST art. 189", acct="58176")
        b.add("line", key="vt", ord="85", label="Total vacation pay", f="={vg}+{vk}", okey="vac_total", ores=o, orule="vacaciones(): total", oform="sum", label_key="Vacation pay", words="Sum", acct="58176")
    else:
        b.add("line", key="vc", ord="86", label="Vacation accrued, paid on termination", f="=ROUND(ROUND({s}*{dw}/720,6),0)", okey="vac_causada", ores=o, orule="vacaciones(): causacion",
              oform="salary x days / 720", label_key="Vacation on termination", words="Salary x days / 720 (15 days per 360)", norm="CST arts. 186 and 189 num. 3 (proportional on termination)", acct="58177")
    blocks.append((cid, b)); SCEN.append((cid, DESC[cid], ws.title, "oracle case " + cid, "module"))
run_blocks(ws, blocks)

# Leave I01-I04, M01
ws = module_sheet("Leave", "I01-I04, M01  General illness and maternity leave",
                  "General illness: 2/3 of the salary for days 1-90 (days 1-2 paid by the employer, from day 3 by the health insurer), 1/2 for days 91-180. Maternity: 18 weeks at full salary.")
blocks = []
for cid in [k for k in CASES if CASES[k]["module"] in ("incapacidad", "maternidad")]:
    c = CASES[cid]; o = ORES[cid]["lines"]; b = Block()
    b.add("sub", text="%s  %s" % (cid, DESC[cid]))
    b.add("inp", key="s", label="Monthly salary", code="Basic salary (WTC)", value=c["salary"], fmt=NUM0)
    if c["module"] == "incapacidad":
        b.add("inp", key="d", label="Days of incapacity", code="", value=c["days"])
        b.add("hdr", labels=COLS)
        b.add("line", key="a", ord="93", label="Days 1-2, paid by the employer (2/3)", f="=ROUND(ROUND({s}/30*p_INC_23*MIN({d},2),6),0)", okey="inc_dias_1_2_empleador", ores=o,
              orule="incapacidad(): days 1-2", oform="salary / 30 x 2/3 x days", label_key="Illness: employer days 1-2", words="Daily salary x 2/3 x days (max 2)",
              norm="CST art. 227; Decree 780 of 2016 art. 3.2.1.10 par. 1", acct="58192", eeer="ER")
        b.add("line", key="bb", ord="93", label="Days 3-90, paid by the health insurer (2/3)", f="=ROUND(ROUND({s}/30*p_INC_23*MAX(0,MIN({d},90)-2),6),0)", okey="inc_dias_3_90_EPS", ores=o,
              orule="incapacidad(): days 3-90", oform="salary / 30 x 2/3 x days", label_key="Illness: insurer days 3-90", words="Daily salary x 2/3 x days", norm="CST art. 227; Decree 780 of 2016 art. 3.2.1.10", acct="58193")
        b.add("line", key="cc", ord="93", label="Days 91-180, paid by the health insurer (1/2)", f="=ROUND(ROUND({s}/30*p_INC_12*MAX(0,MIN({d},180)-90),6),0)", okey="inc_dias_91_180_EPS", ores=o,
              orule="incapacidad(): days 91-180", oform="salary / 30 x 1/2 x days", label_key="Illness: insurer days 91-180", words="Daily salary x 1/2 x days", norm="CST art. 227", acct="58193")
        b.add("line", key="t", ord="93", label="Total illness benefit", f="=ROUND(ROUND({s}/30*(p_INC_23*MIN({d},90)+p_INC_12*MAX(0,MIN({d},180)-90)),6),0)", okey="inc_total", ores=o,
              orule="incapacidad(): total", oform="sum, unrounded parts", label_key="Illness: total", words="Sum of the segments", norm="CST art. 227")
        b.add("line", key="v", ord="93", label="Daily benefit without the floor (2/3)", f="=ROUND({s}/30*p_INC_23,0)", okey="inc_valor_dia_sin_piso", ores=o, orule="incapacidad(): valor_dia", oform="salary / 30 x 2/3",
              label_key="Illness: daily value", words="Daily salary x 2/3", norm="CST art. 227")
        b.add("line", key="p", ord="93", label="Daily minimum wage (floor reference)", f="=ROUND(p_SMMLV/30,0)", okey="piso_smldv_dia", ores=o, orule="incapacidad(): piso", oform="SMMLV / 30",
              label_key="Illness: daily minimum wage", words="SMMLV / 30", norm="Floor: benefit never below the minimum-wage equivalent (Constitutional Court C-543 of 2007; Concepto MinSalud 202311602174531 of 2023); default on, configurable")
        b.add("line", key="pa", ord="93", label="Floor would apply? (Yes/No)", f='=IF({s}/30*p_INC_23<p_SMMLV/30,"Yes","No")', okey="piso_aplica", ores=o, fmt="General", orule="incapacidad(): piso_aplica",
              oform="daily benefit < daily minimum wage", label_key="Illness: floor applies", words="Daily benefit < daily minimum wage", norm="Not triggered in these cases (66,667 > 58,364 a day)")
        b.add("line", key="ib", ord="21", label="IBC for the incapacity days", f="=ROUND(ROUND(MAX({s}/30*(p_INC_23*MIN({d},90)+p_INC_12*MAX(0,MIN({d},180)-90)),p_SMMLV*{d}/30),6),0)",
              okey="IBC_incapacidad", ores=o, orule="incapacidad(): IBC", oform="max(benefit, SMMLV x days / 30)", label_key="Illness: IBC", words="Benefit value, floored at the prorated minimum wage",
              norm="Decree 780 of 2016 art. 3.2.1.10 (IBC = value of the incapacity, never below the minimum)", acct="58106")
    else:
        b.add("hdr", labels=COLS)
        b.add("line", key="ld", ord="94", label="Maternity leave days", f="=p_MAT_WEEKS*7", okey="lic_dias", ores=o, fmt="0", orule="maternidad(): dias", oform="18 x 7", label_key="Maternity: days", words="18 weeks x 7",
              norm="CST art. 236 num. 1 (Law 2114 of 2021)")
        b.add("line", key="lv", ord="94", label="Maternity leave pay", f="=ROUND(ROUND({s}/30*{ld},6),0)", okey="lic_valor", ores=o, orule="maternidad(): valor", oform="salary / 30 x days",
              label_key="Maternity: pay", words="Daily salary x days", norm="CST art. 236 num. 1 (salary earned at the start of the leave)", acct="58194")
        b.add("line", key="li", ord="21", label="IBC for the leave", f="=ROUND(ROUND(MAX({s}/30*{ld},p_SMMLV/30*{ld}),6),0)", okey="lic_IBC", ores=o, orule="maternidad(): IBC", oform="max(value, SMMLV / 30 x days)",
              label_key="Maternity: IBC", words="Leave value, floored at the minimum wage", norm="Decree 780 of 2016 art. 3.2.1.10", acct="58106")
    blocks.append((cid, b)); SCEN.append((cid, DESC[cid], ws.title, "oracle case " + cid, "module"))
run_blocks(ws, blocks)

# Termination T-A..T-E
ws = module_sheet("Termination", "T-A to T-E  Indemnity for dismissal without just cause (CST art. 64), indefinite-term contracts",
                  "Days of service on the commercial 30/360 basis, inclusive. Tier by salary: below 10 minimum wages 30 + 20 days a year; from 10 minimum wages 20 + 15 days a year, pro rata for fractions.")
blocks = []
for cid in [k for k in CASES if CASES[k]["module"] == "terminacion"]:
    c = CASES[cid]; o = ORES[cid]["lines"]; b = Block()
    b.add("sub", text="%s  %s" % (cid, DESC[cid]))
    b.add("inp", key="s", label="Monthly salary", code="Basic salary (WTC)", value=c["salary"], fmt=NUM0)
    b.add("inp", key="a", label="Hire date", code="$employee.hire_date", value=datetime.date.fromisoformat(c["start"]))
    b.add("inp", key="e", label="Termination date", code="$employee.last_working_date", value=datetime.date.fromisoformat(c["end"]))
    b.add("hdr", labels=COLS)
    b.add("line", key="n", ord="91", label="Days of service (30/360, inclusive)", f="=(YEAR({e})-YEAR({a}))*360+(MONTH({e})-MONTH({a}))*30+(MIN(DAY({e}),30)-MIN(DAY({a}),30))+1",
          okey="dias_servicio_360", ores=o, fmt="#,##0", orule="days360()", oform="(Y2-Y1) x 360 + (M2-M1) x 30 + (min(D2,30) - min(D1,30)) + 1", label_key="Art. 64: days of service",
          words="Commercial 30/360 day count, inclusive", norm="CST art. 64 (proportional by fraction); commercial year")
    b.add("line", key="t", ord="91", label="Salary tier (< 10 or >= 10 minimum wages)", f='=IF({s}>=10*p_SMMLV,">=10","<10")', fmt="General", norm="CST art. 64 (Law 789 of 2002 art. 28)")
    b.add("line", key="dd", ord="91", label="Indemnity days", f='=IF({n}<=360,IF({t}=">=10",p_IND_GE10_FIRST,p_IND_LT10_FIRST),IF({t}=">=10",p_IND_GE10_FIRST+p_IND_GE10_ADD*({n}-360)/360,p_IND_LT10_FIRST+p_IND_LT10_ADD*({n}-360)/360))',
          okey="indemnizacion_dias", ores=o, tol=0.000001, fmt="0.000000", orule="terminacion(): dias", oform="first-year days + days per year x (days - 360) / 360",
          label_key="Art. 64: indemnity days", words="First-year days + further days pro rata", norm="CST art. 64 lit. a) and b) (Law 789 of 2002 art. 28)")
    b.add("line", key="v", ord="91", label="Indemnity value", f="=ROUND(ROUND({s}/30*{dd},6),0)", okey="indemnizacion_valor", ores=o, orule="terminacion(): valor", oform="salary / 30 x days, rounded",
          label_key="Art. 64: indemnity value", words="Daily salary x indemnity days", norm="CST art. 64; base = salary (variable pay: open point, see Law vs Provider)", acct="58191", eeer="ER")
    blocks.append((cid, b)); SCEN.append((cid, DESC[cid], ws.title, "oracle case " + cid, "module"))
run_blocks(ws, blocks)

# PILA type 51
ws = module_sheet("PILA type 51", "L01-L30  Contributor type 51 (part-time workers paid by days): bases in quarters of the minimum wage",
                  "Pension and family compensation fund on weekly quarters of the minimum wage (1-7 days 1/4; 8-14 2/4; 15-21 3/4; 22-30 1 SMMLV); occupational risk always on 1 minimum wage.")
blocks = []
for cid in [k for k in CASES if CASES[k]["module"] == "pila51"]:
    c = CASES[cid]; o = ORES[cid]["lines"]; b = Block()
    b.add("sub", text="%s  %s" % (cid, DESC[cid]))
    b.add("inp", key="d", label="Days worked in the month", code="58295", value=c["days"])
    b.add("hdr", labels=COLS)
    q = "IF({d}<=7,1,IF({d}<=14,2,IF({d}<=21,3,4)))"
    nm = "PILA Technical Annex 2 v30, contributor type 51 (Decree 2616 of 2013)"
    b.add("line", key="ip", ord="97", label="Pension base (quarters of SMMLV)", f="=ROUND(p_SMMLV*%s/4,0)" % q, okey="IBC_pension", ores=o, orule="pila51(): IBC_pension", oform="SMMLV x quarters / 4",
          label_key="Type 51: pension base", words="SMMLV x quarters / 4", norm=nm, acct="58197")
    b.add("line", key="pt", ord="97", label="Pension total 16%", f="=ROUND(p_SMMLV*%s/4*p_PEN_TOT,0)" % q, okey="pension_total", ores=o, orule="pila51(): pension_total", oform="base x 16%, rounded to the peso",
          label_key="Type 51: pension total", words="Base x 16%", norm=nm)
    b.add("line", key="pe", ord="97", label="Pension employer 12%", f="=ROUND(p_SMMLV*%s/4*p_PEN_TOT*p_PEN_ER_SHARE,0)" % q, okey="pension_emp", ores=o, orule="pila51(): pension_emp", oform="base x 12%",
          label_key="Type 51: pension employer", words="Base x 12%", eeer="ER", norm=nm)
    b.add("line", key="pw", ord="97", label="Pension employee 4%", f="=ROUND(p_SMMLV*%s/4*p_PEN_TOT*(1-p_PEN_ER_SHARE),0)" % q, okey="pension_trab", ores=o, orule="pila51(): pension_trab", oform="base x 4%",
          label_key="Type 51: pension employee", words="Base x 4%", eeer="EE", norm=nm)
    b.add("line", key="ia", ord="97", label="Occupational risk base (always 1 SMMLV)", f="=ROUND(p_SMMLV,0)", okey="IBC_arl", ores=o, orule="pila51(): IBC_arl", oform="SMMLV", label_key="Type 51: ARL base", words="1 SMMLV", norm=nm)
    b.add("line", key="ar", ord="97", label="Occupational risk class I", f="=ROUND(p_SMMLV*p_ARL_I,0)", okey="arl", ores=o, orule="pila51(): arl", oform="SMMLV x class rate", label_key="Type 51: ARL", words="SMMLV x class I", eeer="ER", norm=nm)
    b.add("line", key="ic", ord="97", label="Family compensation fund base", f="=ROUND(p_SMMLV*%s/4,0)" % q, okey="IBC_ccf", ores=o, orule="pila51(): IBC_ccf", oform="same quarters", label_key="Type 51: CCF base", words="Same quarters", norm=nm)
    b.add("line", key="cf", ord="97", label="Family compensation fund 4%", f="=ROUND(p_SMMLV*%s/4*p_CCF,0)" % q, okey="ccf", ores=o, orule="pila51(): ccf", oform="base x 4%", label_key="Type 51: CCF", words="Base x 4%", eeer="ER", norm=nm)
    blocks.append((cid, b)); SCEN.append((cid, DESC[cid], ws.title, "oracle case " + cid, "module"))
run_blocks(ws, blocks)

# Apprentice (research only)
ws = module_sheet("Apprentice", "AP1-AP2  SENA apprentice: maintenance support and contributions (research rule; not in the oracle)",
                  "Hand-checked against the research (CCG v1.5 Module 4.1 and 5.2): support 75% (classroom) or 100% (practical) of the minimum wage; contribution base never below 1 minimum wage (Decree 0223 of 2026 art. 2.2.6.3.3.4 par. 2).",
                  tab="7F7F7F")
blocks = []
for aid, phase, pct in [("AP1", "Classroom phase", "p_APR_LECT"), ("AP2", "Practical phase", "p_APR_PRACT")]:
    b = Block()
    b.add("sub", text="%s  Apprentice, %s, March 2026, employer eligible for art. 114-1, risk class I" % (aid, phase.lower()))
    b.add("inp", key="ph", label="Phase", code="58208", value=phase)
    b.add("hdr", labels=COLS)
    b.add("line", key="sup", ord="96", label="Maintenance support (CST art. 81)", f="=%s*p_SMMLV" % pct, na=True, norm="CST art. 81 (Law 2466 of 2025 art. 21): 75% classroom, 100% practical", acct="WTC apprentice support")
    b.add("line", key="ib", ord="96", label="Contribution base (floored at 1 SMMLV)", f="=ROUNDUP(ROUND(MAX({sup},p_SMMLV),6),0)", na=True, norm="Decree 0223 of 2026 art. 2.2.6.3.3.4 par. 2", acct="58106")
    b.add("line", key="h", ord="31", label="Health, employee 4% (on the floored base)", f="=ROUNDUP(ROUND({ib}*p_SAL_EE,6)/100,0)*100", na=True, eeer="EE", norm="Decree 0223 of 2026 art. 2.2.6.3.3.4 par. 2 (employee deductions on that base)", acct="58121")
    b.add("line", key="he", ord="41", label="Health, employer 8.5% (exonerated: salary < 10 SMMLV)", f="=0", na=True, eeer="ER", norm="Tax Code art. 114-1", acct="58141")
    if aid == "AP1":
        b.add("line", key="p", ord="32", label="Pension (not due in the classroom phase)", f="=0", na=True, eeer="EE", norm="Research: classroom phase = health and occupational risk only (CCG v1.5 Module 4.6 table)", acct="58122")
        b.add("line", key="ar", ord="43", label="Occupational risk class I", f="=ROUNDUP(ROUND({ib}*p_ARL_I,6)/100,0)*100", na=True, eeer="ER", norm="Research: classroom phase = health and occupational risk only", acct="58143")
        b.add("line", key="cc", ord="44", label="CCF / SENA / ICBF (not in the levy base in the classroom phase)", f="=0", na=True, eeer="ER", norm="Research: payroll-levy base only in the practical / dual phase", acct="58144")
    else:
        b.add("line", key="p", ord="32", label="Pension, employee 4%", f="=ROUNDUP(ROUND({ib}*p_PEN_TOT*(1-p_PEN_ER_SHARE),6)/100,0)*100", na=True, eeer="EE", norm="CST art. 81: practical phase = all rights of an employment contract", acct="58122")
        b.add("line", key="pe", ord="42", label="Pension, employer 12%", f="=ROUNDUP(ROUND({ib}*p_PEN_TOT*p_PEN_ER_SHARE,6)/100,0)*100", na=True, eeer="ER", norm="CST art. 81", acct="58142")
        b.add("line", key="ar", ord="43", label="Occupational risk class I", f="=ROUNDUP(ROUND({ib}*p_ARL_I,6)/100,0)*100", na=True, eeer="ER", norm="CST art. 81", acct="58143")
        b.add("line", key="cc", ord="44", label="Family compensation fund 4%", f="=ROUNDUP(ROUND({sup}*p_CCF,6)/100,0)*100", na=True, eeer="ER", norm="Research: payroll-levy base in the practical phase (Law 21 of 1982 art. 17)", acct="58144")
        b.add("line", key="se", ord="45", label="SENA / ICBF (exonerated)", f="=0", na=True, eeer="ER", norm="Tax Code art. 114-1", acct="58145")
        b.add("line", key="tx", ord="13", label="Transport allowance (practical phase: all allowances of an employment contract)", f="=IF({sup}<=p_AUX_CAP*p_SMMLV,p_AUX,0)", na=True, norm="CST art. 81 (Law 2466 of 2025 art. 21); Decree 1470 of 2025; outside the contribution base", acct="58109")
    b.add("note", text="Expected by hand: base 1,750,905; health 70,100; " + ("ARL 9,200; pension and levies 0. Transport allowance in the classroom phase: not stated in the research, not paid." if aid == "AP1"
                        else "pension 70,100 / 210,200; ARL 9,200; CCF 70,100; transport allowance 249,095 (CST art. 81: all allowances of an employment contract)."))
    blocks.append((aid, b)); SCEN.append((aid, "Apprentice, " + phase.lower() + " (research rule; not in the oracle)", ws.title, "pending oracle case X01", "module"))
run_blocks(ws, blocks)

# ---------------- Scenario, Summary, Checks index, Formula comparison, Read me ----------------
ws = wsS
ws.sheet_properties.tabColor = NAVY
hdr(ws, 1, ["Scenario", "Scenario explanation", "Case ID", "Sheet", "Oracle reference"])
for i, (cid, d, sn, ref, grp) in enumerate(SCEN, start=2):
    ws.cell(i, 1, i - 1); ws.cell(i, 2, d); ws.cell(i, 3, cid); c = ws.cell(i, 4, sn); c.hyperlink = "#'%s'!A1" % sn; c.font = Font(name="Arial", size=10, color="0563C1", underline="single")
    ws.cell(i, 5, ref)
r0 = len(SCEN) + 2
for j, pid in enumerate(["X01", "X02", "X03", "X04", "X05", "X06", "X07"]):
    r = r0 + j
    ws.cell(r, 1, "-"); ws.cell(r, 2, DESC[pid] + " - NOT IN THE ORACLE: " + PENDING_EN[pid]); ws.cell(r, 3, pid); ws.cell(r, 4, "-"); ws.cell(r, 5, "pending oracle case " + pid)
widths(ws, {"A": 9, "B": 110, "C": 9, "D": 20, "E": 34})
ws.freeze_panes = "A2"

ws = wsSum
ws.sheet_properties.tabColor = NAVY
ws["A1"] = "Summary - research formulas vs the independent oracle (oracle_v2, built from the law), per case"; ws["A1"].font = F_TITLE
ws["A2"] = "Counts are live COUNTIFS formulas over the Check (K) and Case (P) columns of each sheet. OK = |difference| within the line tolerance."; ws["A2"].font = F_TXTI
hdr(ws, 4, ["Case", "Scenario", "Sheet", "OK", "DIFF", "Lines compared", "% OK", "Not available in the oracle", "Reason for every DIFF"])
for i, (cid, d, sn, ref, grp) in enumerate(SCEN, start=5):
    q = "'%s'" % sn
    ws.cell(i, 1, cid); ws.cell(i, 2, d); c = ws.cell(i, 3, sn); c.hyperlink = "#%s!A1" % q
    ws.cell(i, 4, '=COUNTIFS(%s!P:P,"%s",%s!K:K,"OK")' % (q, cid, q))
    ws.cell(i, 5, '=COUNTIFS(%s!P:P,"%s",%s!K:K,"DIFF")' % (q, cid, q))
    ws.cell(i, 6, "=D%d+E%d" % (i, i)); c = ws.cell(i, 7, '=IF(F%d=0,"",D%d/F%d)' % (i, i, i)); c.number_format = "0.0%"
    ws.cell(i, 8, '=COUNTIFS(%s!P:P,"%s",%s!K:K,"n/a")' % (q, cid, q))
    ws.cell(i, 9, '=IF(E%d=0,"no DIFF","see sheet")' % i)
tot = len(SCEN) + 5
ws.cell(tot, 2, "TOTAL").font = F_BOLD
for col in "DEFH":
    ws["%s%d" % (col, tot)] = "=SUM(%s5:%s%d)" % (col, col, tot - 1); ws["%s%d" % (col, tot)].font = F_BOLD
ws["G%d" % tot] = "=IF(F%d=0,\"\",D%d/F%d)" % (tot, tot, tot); ws["G%d" % tot].number_format = "0.0%"
ws["B%d" % (tot + 1)] = "Pending oracle cases X01-X07: listed on sheet Scenario with the reason (not counted)."
widths(ws, {"A": 8, "B": 80, "C": 18, "D": 8, "E": 8, "F": 10, "G": 8, "H": 12, "I": 20})
ws.freeze_panes = "A5"

wsC = wb.create_sheet("Checks index"); wsC.sheet_properties.tabColor = NAVY
hdr(wsC, 1, ["Sheet", "Line", "Case", "EE/ER", "Check", "Norm"])
for i, (sn, lab, cid, ee, row, norm) in enumerate(CHECKS, start=2):
    wsC.cell(i, 1, sn); wsC.cell(i, 2, lab); wsC.cell(i, 3, cid); wsC.cell(i, 4, ee); wsC.cell(i, 5, "='%s'!K%d" % (sn, row)); wsC.cell(i, 6, norm)
widths(wsC, {"A": 18, "B": 60, "C": 8, "D": 7, "E": 8, "F": 100}); wsC.freeze_panes = "A2"
okdiff_cf(wsC, "E2:E%d" % (len(CHECKS) + 1))

wsF = wb.create_sheet("Formula comparison"); wsF.sheet_properties.tabColor = NAVY
wsF["A1"] = "Formula comparison - research formula vs the oracle rule (oracle_v2.py; parameters with one primary source each)"; wsF["A1"].font = F_TITLE
wsF["A2"] = "The oracle was written from the law only (Labour Code, Law 100, Law 1393, Tax Code, Decree 1625, Decree 780, PILA Annex 2), independently of the research artifacts. Counts are live COUNTIFS over 'Checks index'."; wsF["A2"].font = F_TXTI
hdr(wsF, 4, ["Line", "Research formula in words", "Research Excel formula (first occurrence)", "Example cell", "Oracle rule (function)", "Oracle formula", "Same logic?", "OK checks", "DIFF checks", "Result match"])
for i, (lab, (words, f, ex, orule, oform)) in enumerate(FORMULA_ROWS.items(), start=5):
    wsF.cell(i, 1, lab); wsF.cell(i, 2, words); t = wsF.cell(i, 3, f); t.data_type = "s"; wsF.cell(i, 4, ex); wsF.cell(i, 5, orule); wsF.cell(i, 6, oform)
    wsF.cell(i, 7, "Yes")
    wsF.cell(i, 8, '=COUNTIFS(\'Checks index\'!B:B,A%d,\'Checks index\'!E:E,"OK")' % i)
    wsF.cell(i, 9, '=COUNTIFS(\'Checks index\'!B:B,A%d,\'Checks index\'!E:E,"DIFF")' % i)
    wsF.cell(i, 10, '=IF(H%d+I%d=0,"not compared",IF(I%d=0,"all OK","DIFF on "&I%d&" of "&(H%d+I%d)))' % (i, i, i, i, i, i))
widths(wsF, {"A": 40, "B": 50, "C": 60, "D": 22, "E": 30, "F": 50, "G": 10, "H": 9, "I": 9, "J": 16}); wsF.freeze_panes = "B5"

ws = wsR; ws.sheet_properties.tabColor = NAVY
ws["A1"] = "CO_Simulation_2026_10_30_V1.0 - Read me"; ws["A1"].font = F_TITLE
rm = [
 ("Purpose", "Colombia payroll simulation 2026 in the same format as the France reference (FR_Simulation_2026_10_06_V1.0.xlsx): every statutory line of the approved research is written as a live Excel formula and compared, line by line, with an independent oracle built from the law."),
 ("Scenarios", "One sheet per monthly case (C01-C27 base cases, R01-R10 withholding depuration, H01-H07 overtime and rest-day premiums, D01-D05 decision cases), and one sheet per module (Withholding table T01-T18, Benefits P01-P06, Vacation V01-V05, Leave I01-I04 and M01, Termination T-A to T-E, PILA type 51 L01-L30, Apprentice AP1-AP2). Sheet Scenario lists them all, plus the seven oracle cases not simulated (X01-X07) with the reason."),
 ("Research values", "Approved research: CO-CCG-001 v1.5, CO-WTC-001 v1.7, CO-DD-001 v1.4, specs v1.1, Payslip v1.2, SIR v1.2. Includes: art. 114-1 test on the salary payments of the month and the IBC (field 76 lock); all-inclusive IBC = 70% + Law 1393 excess; Law 1393 excess only in health, pension and occupational risk; 40% test only on pacted non-salary; 72 UVT per dependant only in the annual return; 40% / 1,340 UVT cap kept in the monthly withholding; transport allowance prorated to days; vacation compensated during employment = salary / 30 x days."),
 ("Parameters", "Sheet Parameters: every rate, threshold and amount is a yellow input cell with its primary source; formulas read them through the defined names p_<Name>. Edit a value and every sheet recalculates."),
 ("Sheet layout", "Monthly sheets: rows 1-4 title, settings, how to read and live check counter; then 1 INPUTS, 2 EARNINGS, 3 BASES (IBC, Law 1393, levy base, art. 114-1), 4 CONTRIBUTIONS, 5 WITHHOLDING (Procedure 1 depuration), 6 NET PAY, 7 art. 383 table. Module sheets hold one titled block per case."),
 ("Design codes", "Ordinals, intermediate accounts (58xxx) and flags (582xx) follow CO_Regulation_Design_v1_0.md (final/design). Column O names the WTC v1.7 perimeter column that feeds the base."),
 ("Oracle", "Column 'Oracle result' holds the value produced by oracle_v2.py (30 Oct 2026) from params.json, as a value (no formula). The oracle is an independent re-implementation from the statutes; it was not derived from the research artifacts."),
 ("Legend", "Difference = research - oracle. Check = OK if |difference| <= 0.01 COP (base in UVT and tax in UVT: 0.01, as the oracle reports 2 decimals; IBC in minimum wages and indemnity days: 0.000001). 'n/a' = line with no oracle counterpart (hand-checked; reason in the note)."),
 ("Rounding", "IBC rounded up to the whole peso and each contribution up to the next COP 100 per contributor and fund (Decree 780 of 2016 art. 3.2.1.5). Withholding rounded to the peso. Prima, cesantias, vacation, leave and indemnity rounded to the peso."),
 ("Coverage", "% OK is over the lines the oracle computes. Lines it does not compute are counted in Summary column H (n/a). Oracle cases X01-X07 are not simulated: open in the law, outside 2026 or resolved elsewhere (sheet Scenario)."),
 ("Navigation and colours", "Tab colours: navy = read me, summary and reference sheets; blue = monthly cases; orange = module sheets; grey = research-only (no oracle). Yellow cell / blue font = input. Light blue = research result."),
 ("Recalculation", "Recalculated with Microsoft Excel (CalculateFull) before delivery; 0 formula errors. Values cross-checked with an independent reader after recalculation (README.md in this folder)."),
 ("Data protection", "All cases are fictitious test data. No employee identifier, name or individual salary of any client appears in this workbook."),
]
for i, (a, bt) in enumerate(rm, start=3):
    ws.cell(i, 1, a).font = F_BOLD; c = ws.cell(i, 2, bt); c.font = F_TXT; c.alignment = WRAP
widths(ws, {"A": 26, "B": 150})

for w in wb.worksheets:
    if w.title not in ("Scenario", "Read me", "Summary", "Parameters", "Checks index", "Formula comparison"):
        okdiff_cf(w, "K1:K400")
wb.save(OUT)
print("sheets", len(wb.worksheets), "checks", len(CHECKS), "scenarios", len(SCEN), "formula rows", len(FORMULA_ROWS))

# Generates "Tax Simulations - Colombia.xlsx" (payslip layout of "Tax Simulations - France.xlsx").
import sys, os, re, datetime, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUTX = sys.argv[1]
src = open(os.path.join(HERE, "gen_sim.py"), encoding="utf-8").read().split("# ---------------------------------------------------------------- workbook")[0]
sys.argv = [sys.argv[0], "unused"]
ns = {"__file__": os.path.join(HERE, "gen_sim.py"), "__name__": "gensim_lib"}
exec(compile(src, "gen_sim_lib", "exec"), ns)
globals().update({k: v for k, v in ns.items() if not k.startswith("__")})
sys.path.insert(0, os.path.join(VAL, "oracle"))
import oracle_v2 as ORC_MOD

SAL_FILL = "FBD4B4"; ER_FILL = "FDE9D9"; TAX_FILL = "DDEBF7"; BASE_FILL = "F2DCDB"
SUMROWS = []

def render_payslip(ws, blk, case_id, sheetname):
    """Payslip layout: A code, B concept, C base, D rate, E our result, F oracle, G diff, H check, I formula text, J note.
    Non-input entries first, then the INPUTS section."""
    order = [e for e in blk.e if e[0] not in ("inp", "ihdr", "hdr")]
    inps = [e for e in blk.e if e[0] == "inp"]
    seq = order + [("section", {"text": "INPUTS (yellow = fictitious test data)"})] + inps
    r = 10; rows = []; refs = {}
    for kind, kw in seq:
        rows.append(r)
        if kind == "inp":
            refs[kw["key"]] = "$E$%d" % r
        elif kind == "line":
            refs[kw["key"]] = "$E$%d" % r; refs[kw["key"] + ".C"] = "$C$%d" % r; refs[kw["key"] + ".D"] = "$D$%d" % r
        r += 1
    checks = 0
    for (kind, kw), row in zip(seq, rows):
        if kind == "section":
            c = ws.cell(row, 2, kw["text"].split(" - ")[0]); c.font = F_BOLD
            for col in range(1, 11):
                ws.cell(row, col).fill = FILL("D9D9D9")
        elif kind in ("sub", "note"):
            ws.cell(row, 2, kw["text"]).font = F_TXTI
        elif kind == "inp":
            ws.cell(row, 1, kw.get("code", "")).font = F_TXT
            ws.cell(row, 2, kw["label"]).font = F_TXT
            c = ws.cell(row, 5, kw["value"]); c.font = F_IN; c.fill = FILL(INPUT)
            if isinstance(kw["value"], (datetime.date, datetime.datetime)):
                c.number_format = "yyyy-mm-dd"
            elif isinstance(kw["value"], (int, float)):
                c.number_format = NUM
            ws.cell(row, 10, kw.get("note", "")).font = F_TXT
        elif kind == "line":
            f = resolve(kw["f"], refs)
            ws.cell(row, 1, kw.get("acct") or kw.get("ord", "")).font = F_TXT
            ws.cell(row, 2, kw["label"]).font = F_BOLD if kw.get("bold") else F_TXT
            if kw.get("base"):
                c = ws.cell(row, 3, resolve(kw["base"], refs)); c.number_format = NUM
            if kw.get("rate"):
                c = ws.cell(row, 4, resolve(kw["rate"], refs)); c.number_format = kw.get("ratefmt", "0.000%")
            c = ws.cell(row, 5, f); c.number_format = kw.get("fmt", NUM); c.font = F_BOLD if kw.get("bold") else F_TXT
            t = ws.cell(row, 9, f); t.data_type = "s"; t.font = Font(name="Consolas", size=8)
            ee = kw.get("eeer", "")
            fillc = SAL_FILL if ee == "EE" and kw.get("ord", "").startswith("3") else ER_FILL if ee == "ER" else TAX_FILL if kw.get("ord", "").startswith(("5", "6")) else None
            if fillc:
                ws.cell(row, 2).fill = FILL(fillc)
            okey, ores = kw.get("okey"), kw.get("ores")
            if okey is not None and ores is not None and okey in ores:
                v = ores[okey]
                if isinstance(v, bool):
                    v = "Yes" if v else "No"
                ci = ws.cell(row, 6, v); ci.number_format = kw.get("fmt", NUM)
                if isinstance(v, str):
                    ws.cell(row, 8, '=IF(E%d=F%d,"OK","DIFF")' % (row, row))
                else:
                    ws.cell(row, 7, "=ROUND(E%d-F%d,6)" % (row, row)).number_format = "#,##0.00####"
                    ws.cell(row, 8, '=IF(ABS(G%d)<=%s,"OK","DIFF")' % (row, kw.get("tol", 0.01)))
                ws.cell(row, 8).font = F_BOLD
                checks += 1
            elif kw.get("na"):
                ws.cell(row, 6, "not available in the oracle").font = F_TXTI
                ws.cell(row, 8, "n/a").font = F_TXTI
            ws.cell(row, 10, kw.get("norm", "")).font = F_TXT
        for col in range(1, 11):
            ws.cell(row, col).border = BOX
    return refs, rows[-1]

def param_block(ws, names):
    ws.cell(2, 13, "RATES, CEILINGS AND BRACKETS USED ON THIS SHEET (2026)").font = F_SUB
    ws.cell(3, 13, "Approved research values (Parameters of CO_Simulation_2026_10_30_V1.0.xlsx; one primary source each)").font = F_TXTI
    leg = [("Social security (employee)", SAL_FILL), ("Employer contribution / levy", ER_FILL), ("Withholding tax line", TAX_FILL), ("Input", INPUT)]
    for i, (t, col) in enumerate(leg):
        c = ws.cell(5 + i, 13, t); c.fill = FILL(col); c.font = F_TXT
    hdr(ws, 9, ["Name", "Rate / parameter", "Value", "Unit", "Source"], 13)
    pv = {p[0]: p for p in PARAMS}
    for i, n in enumerate(names):
        r = 10 + i
        name, desc, val, unit, srcx = pv[n]
        ws.cell(r, 13, name).font = F_BOLD; ws.cell(r, 14, desc).font = F_TXT
        c = ws.cell(r, 15, val); c.font = F_IN; c.fill = FILL(INPUT)
        c.number_format = "0.000%" if unit == "rate" else ("yyyy-mm-dd" if unit == "date" else "#,##0.####")
        ws.cell(r, 16, unit).font = F_TXT; ws.cell(r, 17, srcx).font = F_TXT
        ws.defined_names["p_" + name] = DefinedName("p_" + name, attr_text="'%s'!$O$%d" % (ws.title, r))

ALLP = [p[0] for p in PARAMS]

def tax_sheet(wb, title, case_label, eeid, period, blk, case_id, settings, part="1"):
    ws = wb.create_sheet(title[:31])
    ws.sheet_properties.tabColor = "2F75B5" if part == "1" else "ED7D31"
    c = ws.cell(1, 1, "◄ SUMMARY"); c.font = F_LINK; c.hyperlink = "#'SUMMARY'!A1"
    ws.cell(1, 2, '="Checks vs oracle:  OK "&COUNTIF(H10:H400,"OK")&"   |   DIFF "&COUNTIF(H10:H400,"DIFF")&"   |   not available in the oracle "&COUNTIF(H10:H400,"n/a")').font = F_SUB
    c = ws.cell(2, 2, title); c.font = Font(name="Arial", size=12, bold=True); c.fill = FILL(SAL_FILL)
    ws.cell(3, 2, case_label).font = F_BOLD
    ws.cell(4, 2, "All payments").font = F_TXT; ws.cell(4, 3, eeid)
    ws.cell(5, 2, period).font = F_TXT; ws.cell(5, 3, "TEST")
    ws.cell(6, 2, "Company: CO-TEST-01 - fictitious legal-person employer, income-tax filer (eligible for Tax Code art. 114-1); occupational risk class I").font = F_TXT; ws.cell(6, 3, "TEST")
    ws.cell(7, 2, settings).font = F_TXTI
    ws.cell(8, 2, "PAYSLIP").font = F_BOLD
    hdr(ws, 9, ["CODE (design account / WTC)", "CONCEPT", "BASE", "RATE", "OUR RESULT (live formula)", "ORACLE RESULT (oracle_v2, value)", "Difference (ours - oracle)",
                "Check (OK = same result)", "OUR FORMULA (the Excel formula in the OUR RESULT cell)", "Norm / note"])
    param_block(ws, ALLP)
    refs, last = render_payslip(ws, blk, case_id, ws.title)
    widths(ws, {"A": 13, "B": 58, "C": 15, "D": 10, "E": 17, "F": 19, "G": 12, "H": 10, "I": 58, "J": 70, "K": 3, "L": 3, "M": 18, "N": 60, "O": 14, "P": 10, "Q": 90})
    ws.freeze_panes = "C10"
    okdiff_cf(ws, "H10:H400")
    return ws, refs

wb = Workbook()
wsSum = wb.active; wsSum.title = "SUMMARY"
wsRM = wb.create_sheet("READ ME")

def std_block(c, ores, extra_lines=None):
    blk = monthly_block(c, ores)
    blk.add("section", text="TOTALS")
    blk.add("line", key="tded", ord="69", label="TOTAL DEDUCTIONS (employee contributions as rounded + withholding)", f="={totee}+{wht}", na=True, bold=True,
            norm="Employee contributions rounded up to COP 100 per fund (open item on the split, see Read me)")
    blk.add("line", key="npay", ord="71", label="NET PAY (total paid - total deductions)", f="={gross}-{tded}", na=True, bold=True)
    blk.add("line", key="ecost", ord="49+", label="EMPLOYER COST (gross + employer contributions and levies)", f="={gross}+{toter}", na=True)
    return blk

TAXCASES = [
 ("EE NO DEDUCTIONS", "R01", CASES["R01"], ORES["R01"]["lines"], "Request: depuration with the 25% exempt income only"),
 ("EE WITH DEPENDANTS", "R02", CASES["R02"], ORES["R02"]["lines"], "Request: dependants deduction, Tax Code art. 387 (10%, max 32 UVT)"),
 ("EE DEPENDANTS 72 UVT ANNUAL", "RC03", CRC["RC03"], ORC["RC03"]["lines"], "Request: two dependants - art. 387 deduction in the month; the 72 UVT per dependant only in the annual return"),
 ("EE WITH AFC SAVINGS", "R03", CASES["R03"], ORES["R03"]["lines"], "Request: voluntary pension / AFC exempt income (30%, 3,800 UVT a year)"),
 ("EE WITH PREPAID HEALTH", "R04", CASES["R04"], ORES["R04"]["lines"], "Request: prepaid health deduction (16 UVT a month)"),
 ("EE WITH MORTGAGE INTEREST", "R05", CASES["R05"], ORES["R05"]["lines"], "Request: mortgage interest deduction (100 UVT a month)"),
 ("40 PCT CAP BINDING", "R06", CASES["R06"], ORES["R06"]["lines"], "Request: 40% cap on deductions + exempt income binding"),
 ("1340 UVT CAP BINDING", "R07", CASES["R07"], ORES["R07"]["lines"], "Request: 1,340 UVT annual cap (monthly 1/12) binding"),
 ("25 PCT EXEMPT 790 UVT CAP", "R08", CASES["R08"], ORES["R08"]["lines"], "Request: 25% exempt income limited to 790 UVT a year (monthly 1/12)"),
 ("BELOW 95 UVT", "R09", CASES["R09"], ORES["R09"]["lines"], "Base below 95 UVT: no withholding"),
 ("FIRST BAND 19 PCT", "R10", CASES["R10"], ORES["R10"]["lines"], "Base in the first taxable band (> 95 to 150 UVT, 19%)"),
 ("ALL-INCLUSIVE SALARY", "C22", CASES["C22"], ORES["C22"]["lines"], "All-inclusive salary of 13 minimum wages: IBC 70%; withholding on the full payment"),
 ("NON-SALARY ABOVE 40 PCT", "C26", CASES["C26"], ORES["C26"]["lines"], "Pacted non-salary 50%: Law 1393 excess in the IBC; full amount taxable"),
 ("NON-SALARY BONUS", "RC05", CRC["RC05"], ORC["RC05"]["lines"], "Salary 8,000,000 + pacted non-salary bonus 20,000,000 (research worked example)"),
]
summary_rows = []
for title, cid, c, o, why in TAXCASES:
    per = MONTHS.get(c.get("period", "2026-03"))
    blk = std_block(c, o)
    eeid = "EE-CO-" + cid
    ws, refs = tax_sheet(wb, title, "%s - %s, %s" % (cid, DESC.get(cid, why), per[0]), eeid,
                         "From %s to %s   (paid on the last day)" % (per[1].strftime("%d/%m/%Y"), (per[1].replace(day=28) + datetime.timedelta(days=4)).replace(day=1) - datetime.timedelta(days=1)), blk, cid,
                         "Standard settings: full month, resident employee, withholding Procedure 1, 2026 parameters. " + why)
    summary_rows.append(("1", ws.title, "%s - %s" % (cid, DESC.get(cid, why)), eeid, refs))

# Indemnity sheets (withholding on the indemnity: research rule; indemnity value from the oracle)
def indemnity_block(sal, start, end, ores, monthly_income, avg12, label):
    b = Block()
    b.add("section", text="EARNINGS")
    b.add("line", key="n", ord="91", label="Days of service (30/360, inclusive)", f="=(YEAR({e})-YEAR({a}))*360+(MONTH({e})-MONTH({a}))*30+(MIN(DAY({e}),30)-MIN(DAY({a}),30))+1",
          okey="dias_servicio_360", ores=ores, fmt="#,##0", norm="CST art. 64 (proportional by fraction)")
    b.add("line", key="dd", ord="91", label="Indemnity days (CST art. 64)", f='=IF({n}<=360,IF({s}>=10*p_SMMLV,p_IND_GE10_FIRST,p_IND_LT10_FIRST),IF({s}>=10*p_SMMLV,p_IND_GE10_FIRST+p_IND_GE10_ADD*({n}-360)/360,p_IND_LT10_FIRST+p_IND_LT10_ADD*({n}-360)/360))',
          okey="indemnizacion_dias", ores=ores, tol=0.000001, fmt="0.000000", norm="CST art. 64 (Law 789 of 2002 art. 28)")
    b.add("line", key="v", ord="91", label="INDEMNITY FOR DISMISSAL WITHOUT JUST CAUSE", f="=ROUND(ROUND({s}/30*{dd},6),0)", okey="indemnizacion_valor", ores=ores, bold=True, acct="58191", norm="CST art. 64")
    b.add("section", text="WITHHOLDING ON THE INDEMNITY (outside the ordinary monthly base)")
    b.add("line", key="mu", ord="64", label="Monthly income in UVT (test against 204 UVT)", f="={mi}/p_UVT", na=True, fmt="0.0000",
          norm="Tax Code art. 401-3. Premise (research): the 204-UVT test is applied to the monthly income")
    b.add("line", key="gt", ord="64", label="Income above 204 UVT? (Yes/No)", f='=IF({mu}>p_IND_UVT,"Yes","No")', na=True, fmt="General", norm="Tax Code art. 401-3")
    b.add("line", key="au", ord="64", label="Average monthly taxable income of the last 12 months, in UVT", f="={a12}/12/p_UVT", na=True, fmt="0.0000",
          norm="Decree 1625 of 2016 art. 1.2.4.1.8 (12 months before termination / 12)")
    b.add("line", key="tp", ord="64", label="Table percentage on the 12-month average (tax in UVT / average in UVT)", f="=IF({au}<=p_T_B1,0,(" + ret_tax_formula("{au}") + ")/{au})", na=True, fmt="0.0000%",
          norm="Decree 1625 of 2016 art. 1.2.4.1.8; Tax Code art. 383")
    b.add("line", key="rt", ord="64", label="Rate applied to the indemnity", rate=None, f='=IF({gt}="Yes",p_IND_RATE,{tp})', na=True, fmt="0.00%", norm="20% above 204 UVT (Tax Code art. 401-3), else the table percentage")
    b.add("line", key="wi", ord="64", label="WITHHOLDING ON THE INDEMNITY", base="={v}", rate="={rt}", f="=ROUND(ROUND({v}*{rt},6),0)", na=True, bold=True, eeer="EE", acct="58164",
          norm="Tax Code art. 401-3; Decree 1625 of 2016 arts. 1.2.4.1.8 and 1.2.4.1.13 (oracle has no indemnity withholding: hand-checked)")
    b.add("inp", key="s", label="Monthly salary", code="Basic salary (WTC)", value=sal)
    b.add("inp", key="a", label="Hire date", code="$employee.hire_date", value=start)
    b.add("inp", key="e", label="Termination date", code="$employee.last_working_date", value=end)
    b.add("inp", key="mi", label="Monthly income for the 204-UVT test", code="58150", value=monthly_income)
    b.add("inp", key="a12", label="Taxable payments of the 12 months before termination", code="58150 (_12m)", value=avg12, note="Salary x 12 + service bonuses paid in the 12 months")
    return b

oT = ORES["T-B"]["lines"]
blk = indemnity_block(20000000, datetime.date(2024, 1, 10), datetime.date(2026, 6, 30), oT, 20000000, 20000000 * 12 + 2 * 10000000, "T-B")
ws, refs = tax_sheet(wb, "INDEMNITY 20 PCT ABOVE 204 UVT", "T-B - Dismissal without just cause, salary COP 20,000,000 (>= 10 minimum wages), 2024-01-10 to 2026-06-30",
                     "EE-CO-T-B", "Termination 30/06/2026", blk, "T-B",
                     "Request: indemnity withholding 20% where income exceeds 204 UVT (Tax Code art. 401-3). Expected by hand: 381.87 UVT > 204 -> 20% x 28,083,333 = 5,616,667.", part="2")
summary_rows.append(("2", ws.title, "T-B - Indemnity, income above 204 UVT (20%)", "EE-CO-T-B", refs))
oI = ORC_MOD.terminacion({"salary": 4500000, "start": "2022-03-01", "end": "2026-08-31"})
blk = indemnity_block(4500000, datetime.date(2022, 3, 1), datetime.date(2026, 8, 31), oI, 4500000, 58500000, "TI")
ws, refs = tax_sheet(wb, "INDEMNITY 12-MONTH AVERAGE", "TI - Dismissal without just cause, salary COP 4,500,000, 4 years 6 months (research worked example, termination 31/08/2026)",
                     "EE-CO-TI", "Termination 31/08/2026", blk, "TI",
                     "Indemnity withholding below 204 UVT: table percentage of the 12-month average (Decree 1625 of 2016 art. 1.2.4.1.8). Expected by hand: 93.08 UVT <= 95 -> 0%. Oracle values: terminacion() run on these inputs.", part="2")
summary_rows.append(("2", ws.title, "TI - Indemnity, income below 204 UVT (12-month average)", "EE-CO-TI", refs))

# Service bonus separate read (Procedure 1)
oP = ORC_MOD.retencion(ORC_MOD.D(750000), ORC_MOD.D(0), False, 0, 0, 0, None)
b = Block()
b.add("section", text="SERVICE BONUS - separate table read under Procedure 1")
b.add("line", key="inc", ord="65", label="Statutory service bonus paid", f="={pb}", okey="ret_ingreso_laboral", ores=oP, norm="CST art. 306; Decree 1625 of 2016 art. 1.2.4.1.3 (Procedure 1: separate read of the bonus)")
b.add("line", key="e25", ord="58", label="Exempt labour income 25%", f="=MIN(p_RET_E25_PCT*{inc},p_RET_E25_UVT*p_UVT/12)", okey="ret_exenta_25", ores=oP, norm="Tax Code art. 206 num. 10")
b.add("line", key="cap", ord="59", label="Cap 40%", f="=MIN(p_RET_CAP_PCT*{inc},p_RET_CAP_UVT*p_UVT/12)", okey="ret_cap_40_1340", ores=oP, norm="Decree 1625 of 2016 art. 1.2.4.1.6 par. 3")
b.add("line", key="base", ord="60", label="Taxable base", f="=MAX({inc}-MIN({e25},{cap}),0)", okey="ret_base_gravable", ores=oP, bold=True, norm="Tax Code art. 388")
b.add("line", key="bu", ord="60", label="Taxable base in UVT", f="={base}/p_UVT", okey="ret_base_uvt", ores=oP, fmt="0.0000")
b.add("line", key="tu", ord="61", label="Tax in UVT", f="=" + ret_tax_formula("{bu}"), okey="ret_impuesto_uvt", ores=oP, fmt="0.0000", norm="Tax Code art. 383")
b.add("line", key="w", ord="65", label="WITHHOLDING ON THE SERVICE BONUS", f="=ROUND(ROUND({tu}*p_UVT,6),0)", okey="ret_valor_retener", ores=oP, bold=True, eeer="EE", acct="58165")
b.add("note", text="Open point (not simulated): how the monthly 790-UVT apportionment of the 25% is shared between the salary read and the bonus read in the same month is not stated in the sources read.")
b.add("inp", key="pb", label="Service bonus (research worked example: 4,500,000 x 60 / 360)", code="58172", value=750000)
ws, refs = tax_sheet(wb, "SERVICE BONUS SEPARATE READ", "PB - Service bonus COP 750,000 read separately (research worked example)", "EE-CO-PB", "August 2026", b, "PB",
                     "Oracle values: retencion() applied to the bonus alone (no non-taxable income, no deductions).", part="2")
summary_rows.append(("2", ws.title, "PB - Service bonus withheld on its own table read", "EE-CO-PB", refs))

# Table 383 boundaries (compact)
ws = wb.create_sheet("TABLE 383 BOUNDARIES"); ws.sheet_properties.tabColor = "2F75B5"
c = ws.cell(1, 1, "◄ SUMMARY"); c.font = F_LINK; c.hyperlink = "#'SUMMARY'!A1"
ws.cell(1, 2, '="Checks vs oracle:  OK "&COUNTIF(H10:H400,"OK")&"   |   DIFF "&COUNTIF(H10:H400,"DIFF")').font = F_SUB
c = ws.cell(2, 2, "TABLE 383 BOUNDARIES"); c.font = Font(name="Arial", size=12, bold=True); c.fill = FILL(SAL_FILL)
ws.cell(3, 2, "T01-T18 - base exactly on, 1 peso below and 1 peso above every bound of the Tax Code art. 383 table (UVT 52,374)").font = F_BOLD
param_block(ws, ALLP)
hdr(ws, 9, ["CASE", "CONCEPT", "BASE (COP)", "BASE (UVT)", "OUR RESULT: WITHHOLDING (live)", "ORACLE RESULT", "Difference", "Check", "OUR FORMULA", "Note"])
r = 10
for cid in [k for k in CASES if CASES[k]["module"] == "ret_table"]:
    cc = CASES[cid]; o = ORES[cid]["lines"]
    ws.cell(r, 1, cid); ws.cell(r, 2, DESC[cid])
    x = ws.cell(r, 3, cc["base_cop"]); x.font = F_IN; x.fill = FILL(INPUT); x.number_format = NUM0
    ws.cell(r, 4, "=C%d/p_UVT" % r).number_format = "0.000000"
    f = "=ROUND(ROUND((" + ret_tax_formula("D%d" % r) + ")*p_UVT,6),0)"
    ws.cell(r, 5, f).number_format = NUM; t = ws.cell(r, 9, f); t.data_type = "s"; t.font = Font(name="Consolas", size=8)
    ws.cell(r, 6, o["valor_retener"]).number_format = NUM
    ws.cell(r, 7, "=ROUND(E%d-F%d,6)" % (r, r)); ws.cell(r, 8, '=IF(ABS(G%d)<=0.01,"OK","DIFF")' % r)
    ws.cell(r, 10, "Tax Code art. 383; intervals open on the left (a base exactly on a bound stays in the lower band)")
    for col in range(1, 11):
        ws.cell(r, col).border = BOX
    r += 1
widths(ws, {"A": 8, "B": 50, "C": 15, "D": 14, "E": 18, "F": 15, "G": 11, "H": 9, "I": 70, "J": 60, "M": 18, "N": 60, "O": 14, "P": 10, "Q": 90})
ws.freeze_panes = "C10"; okdiff_cf(ws, "H10:H40")
summary_rows.append(("1", ws.title, "T01-T18 - art. 383 table boundaries", "-", None))

# SUMMARY
ws = wsSum; ws.sheet_properties.tabColor = NAVY
ws["A1"] = "SUMMARY - Colombia tax simulations 2026: research payslip vs independent oracle (oracle_v2, built from the law)"; ws["A1"].font = F_TITLE
ws["A2"] = "One row per payslip. Part 1 = monthly withholding depuration (Procedure 1); Part 2 = indemnity and service-bonus withholding (separate reads). Amounts are live links to the payslip sheets."; ws["A2"].font = F_TXTI
hdr(ws, 4, ["Part", "Scenario sheet", "Payslip", "EE ID", "Total gross", "Taxable base", "Withholding", "Total deductions", "Net pay", "Employer cost", "OK", "DIFF", "Lines compared", "Not available in the oracle"])
for i, (part, sn, lab, eeid, refs) in enumerate(summary_rows, start=5):
    q = "'%s'" % sn
    ws.cell(i, 1, part); c = ws.cell(i, 2, sn); c.hyperlink = "#%s!A1" % q; ws.cell(i, 3, lab); ws.cell(i, 4, eeid)
    if refs:
        for col, k in zip(range(5, 11), ["gross", "base", "wht", "tded", "npay", "ecost"]):
            if k in refs:
                ws.cell(i, col, "=%s!%s" % (q, refs[k])).number_format = NUM
        if "wi" in refs:
            ws.cell(i, 7, "=%s!%s" % (q, refs["wi"])).number_format = NUM
        if "w" in refs:
            ws.cell(i, 7, "=%s!%s" % (q, refs["w"])).number_format = NUM
    ws.cell(i, 11, '=COUNTIF(%s!H10:H400,"OK")' % q); ws.cell(i, 12, '=COUNTIF(%s!H10:H400,"DIFF")' % q); ws.cell(i, 13, "=K%d+L%d" % (i, i))
    ws.cell(i, 14, '=COUNTIF(%s!H10:H400,"n/a")' % q)
t = len(summary_rows) + 5
ws.cell(t, 3, "TOTAL").font = F_BOLD
for col in "KLMN":
    ws["%s%d" % (col, t)] = "=SUM(%s5:%s%d)" % (col, col, t - 1); ws["%s%d" % (col, t)].font = F_BOLD
widths(ws, {"A": 6, "B": 34, "C": 70, "D": 13, "E": 15, "F": 15, "G": 14, "H": 15, "I": 15, "J": 15, "K": 6, "L": 6, "M": 9, "N": 12})
ws.freeze_panes = "C5"

ws = wsRM; ws.sheet_properties.tabColor = NAVY
ws["A1"] = "Tax Simulations - Colombia (2026)"; ws["A1"].font = F_TITLE
rm = [
 ("Purpose", "Payslip-style simulations of the Colombian withholding scenarios requested (Part 1 = monthly depuration under Procedure 1; Part 2 = indemnity and service-bonus withholding read outside the monthly base), in the same layout as 'Tax Simulations - France.xlsx'."),
 ("Standard settings", "March 2026 unless the payslip header says otherwise; full month (30-day convention); resident employee; legal-person employer eligible for Tax Code art. 114-1; occupational risk class I; withholding Procedure 1 (Decree 1625 of 2016 art. 1.2.4.1.3)."),
 ("Research values", "Approved research CO-CCG-001 v1.5 / CO-WTC-001 v1.7: 25% exempt income computed last and limited to 790 UVT a year; deductions and exempt income capped at 40% of net income and 1,340 UVT a year (Decree 1625 of 2016 art. 1.2.4.1.6 par. 3); annual caps applied monthly as 1/12 (operating convention, configurable); dependants deduction art. 387 (10%, 32 UVT); 72 UVT per dependant only in the annual return (DIAN Concepto 011383 of 2024 IV.2); indemnity withheld outside the monthly base (Tax Code art. 401-3; Decree 1625 of 2016 arts. 1.2.4.1.8 and 1.2.4.1.13)."),
 ("Formulas", "Every amount is a live Excel formula reading the right-hand parameter block of the same sheet (cells named p_<Name> at sheet scope). Column I shows the formula of column E as text."),
 ("Oracle", "Column F holds the oracle_v2 result as a value. Indemnity withholding has no oracle function: those lines show 'not available in the oracle' and were hand-checked (expected value in the sheet settings line)."),
 ("Legend", "Salmon = employee contribution; light pink = employer contribution or levy; light blue = withholding line; yellow / blue font = input. Difference = ours - oracle; Check = OK when |difference| <= 0.01 COP (UVT lines: 0.01, the oracle reports 2 decimals)."),
 ("Coverage", "SUMMARY counts OK / DIFF / not available per payslip. Lines not computed by the oracle: rounded totals and net pay (the oracle nets unrounded contributions), and the indemnity withholding."),
 ("Open points", "(1) Split of the PILA-rounded total per fund between employee and employer; (2) how the monthly 790-UVT figure is shared between the salary read and the service-bonus read; (3) the 204-UVT test is applied to the monthly income (research premise). None changes a compared line."),
 ("Technical workbook", "CO_Simulation_2026_10_30_V1.0.xlsx (same folder): the same rules for 103 cases with the regulation chain, ordinals and design accounts of CO_Regulation_Design_v1_0.md."),
 ("Data protection", "Fictitious test data only. No employee identifier, name or individual salary of any client."),
]
for i, (a, bt) in enumerate(rm, start=3):
    ws.cell(i, 1, a).font = F_BOLD; c = ws.cell(i, 2, bt); c.font = F_TXT; c.alignment = WRAP
r = len(rm) + 4
ws.cell(r, 1, "Sheets").font = F_BOLD
hdr(ws, r + 1, ["Sheet", "Scenario"])
for j, (part, sn, lab, eeid, refs) in enumerate(summary_rows, start=r + 2):
    ws.cell(j, 1, sn); ws.cell(j, 2, "Part %s: %s" % (part, lab))
widths(ws, {"A": 34, "B": 150})
wb.move_sheet("READ ME", offset=-(len(wb.sheetnames) - 1))
wb.move_sheet("SUMMARY", offset=-(len(wb.sheetnames) - 2))
wb.save(OUTX)
print("tax sheets", len(wb.sheetnames))

# Generates "Colombia Simulations - Law vs Provider.xlsx" (structure of "France Simulations - Official vs Internal.xlsx"),
# aggregated only: no employee index, name, ID or individual salary.
import sys, os, json, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from colib import *
OUT = sys.argv[1]
R = load(os.path.join(VAL, "test4-folha-setembro", "resultados-v2.json"))
det = R["detalhe"]
cnt = collections.defaultdict(collections.Counter)
emps = collections.defaultdict(set)
for d in det:
    k = (d["bloco"], d["linha"]); cnt[k][d["classe"]] += 1
    emps[k].add(d["emp"])
BLOCK = {"A-IBC": "A - Contribution base", "B-APORTES": "B - Contributions and levies", "C-RETEFUENTE": "C - Withholding tax", "D-INDEMNIZACAO": "D - Art. 64 indemnity", "E-LICENCAS": "E - Leave"}
# line -> (English line, law formula, logic, why different / reason)
L = {
 ("A-IBC", "IBC"): ("Contribution base (IBC)", "ceil_peso(min(max(salary payments [x70% all-inclusive] + Law 1393 excess, 1 SMMLV x days/30), 25 SMMLV x days/30))", "Law 100 art. 18; Law 1393 art. 30; Decree 780 art. 3.2.1.5", "No data: month with vacation / incapacity / leave (IBC of the absence days not modelled: 51); apprentices and interns (20); missing report line (2)"),
 ("A-IBC", "excesso_ley1393"): ("Law 1393 excess", "max(pacted non-salary - 40% x (salary + pacted non-salary), 0)", "Law 1393 of 2010 art. 30; CE SU 25185/2021", "No data: excess not derivable from the reports (14)"),
 ("B-APORTES", "25110 CCF 4% (base do oraculo)"): ("Family compensation fund 4%", "levy base x 4%, up to COP 100", "Law 21 of 1982 arts. 12 and 17 (no Law 1393 excess)", "Mechanism 4: employer base (provider wage type 64990) smaller than the employee IBC"),
 ("B-APORTES", "25111 ICBF 3% (exon. 114-1)"): ("ICBF 3% (art. 114-1)", "0 if exonerated, else levy base x 3%", "Tax Code art. 114-1; Law 89 of 1988", "Mechanism 1: provider tests salary + non-salary + vacation against 10 SMMLV"),
 ("B-APORTES", "25112 SENA 2% (exon. 114-1)"): ("SENA 2% (art. 114-1)", "0 if exonerated, else levy base x 2%", "Tax Code art. 114-1; Law 21 of 1982", "Mechanism 1: provider tests salary + non-salary + vacation against 10 SMMLV"),
 ("B-APORTES", "2553 FSP"): ("Solidarity pension fund", "IBC x (0.5% + 0.5% + band 0.2%-1.0%) from 4 SMMLV", "Law 100 arts. 20 and 27 (Law 797 arts. 7 and 8)", ""),
 ("B-APORTES", "2554 salud trab 4%"): ("Health, employee 4%", "IBC x 4%, up to COP 100", "Law 100 art. 204", ""),
 ("B-APORTES", "2556 pension trab 4%"): ("Pension, employee 4%", "IBC x 4%, up to COP 100", "Law 100 art. 20", ""),
 ("B-APORTES", "2560 ARL"): ("Occupational risk (months with absence)", "IBC of the days worked x class rate", "Decree 1072 of 2015 art. 2.2.4.2.1.6", "No data: no ARL on vacation / incapacity days, base differs from the total IBC (51)"),
 ("B-APORTES", "2560 ARL classe I"): ("Occupational risk, class I", "IBC x 0.522%", "Decree 1772 of 1994 art. 13", "Mechanism 3: applied rate differs from the Master Data class"),
 ("B-APORTES", "2560 ARL classe II"): ("Occupational risk, class II", "IBC x 1.044%", "Decree 1772 of 1994 art. 13", "Mechanism 3: applied rate differs from the Master Data class"),
 ("B-APORTES", "2564 salud emp 8,5% (exon. 114-1)"): ("Health, employer 8.5% (art. 114-1)", "0 if eligible AND salary payments < 10 SMMLV AND IBC < 10 SMMLV, else IBC x 8.5%", "Tax Code art. 114-1; DIAN Conceptos 8380/2024 and 7196/2025; PILA Annex 2 field 76", "Mechanism 1 (8 employees) and the field-76 lock (1 employee)"),
 ("B-APORTES", "2567 pension emp 12%"): ("Pension, employer 12%", "IBC x 12%, up to COP 100", "Law 100 art. 20", "Mechanism 4: employer base smaller than the employee IBC"),
 ("C-RETEFUENTE", "AFC+APV <=30%/3800 UVT"): ("Voluntary pension / AFC exempt", "min(paid, 30% x income, 3,800 UVT / 12)", "Tax Code arts. 126-1, 126-4", "No effect: above the cap, but the 1,340 UVT cap already binds (2)"),
 ("C-RETEFUENTE", "G2N 2552 = Base of Withholding (consistencia interna)"): ("Provider consistency: payslip withholding = withholding report", "equality check", "internal consistency", ""),
 ("C-RETEFUENTE", "INCRNGO"): ("Non-taxable income (no IBC available)", "EE health + pension + FSP", "Tax Code arts. 55-56", "No data: no provider IBC to recompute (2)"),
 ("C-RETEFUENTE", "INCRNGO (salud+pension+FSP)"): ("Non-taxable income (mandatory contributions)", "EE health + pension + FSP", "Tax Code arts. 55-56", "Tolerance: IBC with cents and contributions rounded to the peso by the provider (max 3.24 COP)"),
 ("C-RETEFUENTE", "base"): ("Withholding base (no report line)", "-", "-", "No data: employee without a line in the withholding report (20)"),
 ("C-RETEFUENTE", "base gravable"): ("Taxable base", "net income - reliefs within 40% / 1,340 UVT", "Tax Code art. 388; Decree 1625 art. 1.2.4.1.6 par. 3", "Mechanism 2: base without any relief (5); tolerance from the 25% figure (3,447,953 vs 3,447,955.50)"),
 ("C-RETEFUENTE", "beneficios aplicados (40% / 1.340 UVT)"): ("Reliefs applied", "min(sum of reliefs, 40% x net income, 1,340 UVT / 12)", "Tax Code art. 336 num. 3; Decree 1625 art. 1.2.4.1.6 par. 3", "Mechanism 2: no relief applied (5)"),
 ("C-RETEFUENTE", "dependientes 10%/32 UVT"): ("Dependants deduction", "min(10% x income, 32 UVT)", "Tax Code art. 387", ""),
 ("C-RETEFUENTE", "porcentaje fijo proc.2"): ("Procedure 2 fixed percentage", "-", "Decree 1625 art. 1.2.4.1.4", "No data: the half-yearly percentage needs the previous 12 months (96)"),
 ("C-RETEFUENTE", "prepagada <=16 UVT"): ("Prepaid health deduction", "min(paid, 16 UVT)", "Tax Code art. 387", ""),
 ("C-RETEFUENTE", "renta exenta 25% (790 UVT/ano)"): ("Exempt labour income 25%", "min(25% x residue, 790 UVT / 12)", "Tax Code art. 206 num. 10", "Tolerance: provider uses 3,447,953; exact 790 x 52,374 / 12 = 3,447,955.50"),
 ("C-RETEFUENTE", "retencion proc.'3'"): ("Provider 'procedure 3' (20% + constant)", "-", "not Procedure 1 or 2 of Decree 1625", "No data: not recomputed; possibly a voluntary higher rate (9)"),
 ("C-RETEFUENTE", "retencion proc.1 (tabla art. 383)"): ("Withholding, Procedure 1", "art. 383 table on the taxable base", "Tax Code art. 383", "Mechanism 2: base without reliefs (3)"),
 ("C-RETEFUENTE", "retencion proc.2 = base x % (aritmetica)"): ("Withholding, Procedure 2 (arithmetic)", "base x provider percentage", "Decree 1625 art. 1.2.4.1.4", ""),
 ("C-RETEFUENTE", "retencion proc.2 com a base do oraculo x % do provedor"): ("Withholding, Procedure 2 on the law base", "law base x provider percentage", "Decree 1625 art. 1.2.4.1.4", "Mechanism 2: base without reliefs (1)"),
 ("C-RETEFUENTE", "vivienda <=100 UVT"): ("Mortgage interest deduction", "min(paid, 100 UVT)", "Tax Code art. 119", ""),
 ("D-INDEMNIZACAO", "dias"): ("Indemnity days", "first-year days + further days pro rata (30/20 or 20/15)", "CST art. 64 (Law 789 of 2002 art. 28)", "Mechanisms 6 and 7: more favourable day table (allowed, CST art. 13); fraction of year truncated to whole days"),
 ("D-INDEMNIZACAO", "indemnizacao"): ("Indemnity (not computable)", "-", "-", "No data: probation period (12), fixed-term contract (2), Law 789 transitional table (3), missing data (1)"),
 ("D-INDEMNIZACAO", "valor"): ("Indemnity value", "daily salary x indemnity days", "CST arts. 64 and 127", "Mechanisms 6, 7 and 8: value on basic salary only while the report's own base includes variable pay"),
 ("E-LICENCAS", "incapacidad 79008"): ("General illness benefit", "2/3 of daily salary (days 1-2 employer)", "CST art. 227", "Mechanism 5: paid at 100% (more favourable, CST art. 13)"),
 ("E-LICENCAS", "incapacidad 79011"): ("General illness benefit (insurer days)", "2/3 of daily salary", "CST art. 227", "Mechanism 5: paid at 100% (more favourable, CST art. 13)"),
 ("E-LICENCAS", "vacaciones 79001"): ("Vacation pay", "-", "CST art. 192", "No data: base = ordinary salary or 12-month average when variable; business vs calendar days (54)"),
 ("E-LICENCAS", "vacaciones 79003"): ("Vacation pay (other)", "-", "CST art. 192", "No data: as above (5)"),
}
MECH_EN = [
 # (block, provider mechanism key substring, English, norm, research position, impact)
 ("B-APORTES", "exoneracao 114-1: provedor cobra", "Art. 114-1 test: provider adds non-salary and vacation pay to the salary of the month; employees below 10 SMMLV lose the exoneration (employer health 8.5%)",
  "Tax Code art. 114-1; DIAN Conceptos 8380/2024 and 7196/2025; CE S4 exp. 25302/2022", "Research corrected: test on salary payments of the month and IBC < 10 SMMLV (PILA spec and CCG aligned)", "Provider over-pays; warn the payroll team"),
 ("B-APORTES", "exoneracao 114-1 (ICBF)", "Art. 114-1 test (ICBF 3%): same mechanism", "Tax Code art. 114-1", "As above", "Provider over-pays"),
 ("B-APORTES", "exoneracao 114-1 (SENA)", "Art. 114-1 test (SENA 2%): same mechanism", "Tax Code art. 114-1", "As above", "Provider over-pays"),
 ("B-APORTES", "exoneracao 114-1: provedor exonera", "Field-76 lock: salary < 10 SMMLV but IBC >= 10 SMMLV; provider exonerates, the law (PILA field 76) does not allow it",
  "PILA Technical Annex 2 v30 field 76; Tax Code art. 114-1", "Research: no exoneration when the IBC reaches 10 SMMLV; manual review", "Provider under-pays (1 employee)"),
 ("C-RETEFUENTE", "base sem nenhum beneficio", "Withholding base without any relief (no 25% exempt income, no dependants, no AFC/APV) although the provider's own sheet computes the relief",
  "Tax Code art. 206 num. 10, art. 336 num. 3; Decree 1625 art. 1.2.4.1.6", "Research applies the 25% and the cap every month", "Provider over-withholds; warn the payroll team"),
 ("B-APORTES", "ARL: taxa implicita", "Occupational-risk rate applied differs from the risk class in the Master Data", "Decree 1772 of 1994 art. 13; Decree 1072 art. 2.2.4.3.5",
  "Research: rate by the work centre's class (DD field 'Work Centre Occupational Risk Class')", "Mixed direction"),
 ("B-APORTES", "inconsistencia interna", "Employer pension / ARL / CCF computed on a base smaller than the employee IBC", "Law 100 of 1993 arts. 18 and 20 (one contribution base)", "Research uses one base", "Provider under-pays (2 employees)"),
 ("E-LICENCAS", "pago a 100%", "General illness paid at 100% of the daily salary", "CST art. 227 (2/3)", "Research default 66.67%, configurable; 100% is more favourable (CST art. 13)", "No research change"),
 ("D-INDEMNIZACAO", "dias: tabela mais favoravel que o art. 64 (convencional/contratual; CST art. 13 permite)", "Indemnity days above art. 64 (collective or contractual table)",
  "CST arts. 13 and 64", "Research follows art. 64; a more favourable agreement is lawful", "No research change (agreement not available)"),
 ("D-INDEMNIZACAO", "dias: fracao de ano truncada", "Fraction of the year truncated to whole days", "CST art. 64 ('proportionally by fraction')", "Research prorates the fraction", "Provider under-pays up to 1 day"),
 ("D-INDEMNIZACAO", "valor: so o salario basico", "Indemnity value on basic salary only (the report's own base includes variable pay)", "CST arts. 127 and 64", "Research silent on the indemnity base: possible gap (70% confidence)", "Open point"),
]
wb = Workbook()
wsR = wb.active; wsR.title = "READ ME"
wsL = wb.create_sheet("LAW SIMULATION"); wsP = wb.create_sheet("PROVIDER RESULT"); wsM = wb.create_sheet("BY MECHANISM"); wsO = wb.create_sheet("OFFICIAL EXAMPLES")
for w in (wsR, wsM, wsO):
    w.sheet_properties.tabColor = NAVY
wsL.sheet_properties.tabColor = "2F75B5"; wsP.sheet_properties.tabColor = "ED7D31"
keys = sorted(cnt.keys())
wsL["A1"] = "LAW SIMULATION - independent oracle (oracle_v2.py, built from the statutes) recomputing the September 2026 payroll"; wsL["A1"].font = F_TITLE
wsL["A2"] = "Rule and logic the oracle applied on each payroll line, and how many employee-lines it recomputed. Same rows as sheet PROVIDER RESULT. Aggregated: no employee index, name or salary."; wsL["A2"].font = F_TXTI
hdr(wsL, 4, ["Block", "Line", "Formula used (law, oracle)", "Logic used (norm)", "Employee-lines recomputed", "Employees"])
wsP["A1"] = "PROVIDER RESULT - payroll provider, September 2026 (masked copies of the provider reports), compared with the law line by line"; wsP["A1"].font = F_TITLE
wsP["F1"] = '=SUM(C5:C%d)&" of "&SUM(H5:H%d)&" comparable lines give the law result within 1 COP ("&ROUND(100*SUM(C5:C%d)/SUM(H5:H%d),1)&" %%); within 100 COP: "&ROUND(100*(SUM(C5:C%d)+SUM(D5:D%d))/SUM(H5:H%d),1)&" %%"' % ((len(keys) + 4,) * 7)
wsP["F1"].font = F_SUB
wsP["A2"] = "Match = |provider - law| <= 1 COP; Tolerance = <= 100 COP (rounding); Divergence = more; No data = not recomputable; No effect = above a cap that another cap already binds. Comparable = Match + Tolerance + Divergence."; wsP["A2"].font = F_TXTI
hdr(wsP, 4, ["Block", "Line", "Match (<= 1 COP)", "Tolerance (<= 100 COP)", "Divergence", "No data", "No effect", "Comparable lines", "% same as law", "Why different / why no data"])
for i, k in enumerate(keys, start=5):
    en = L.get(k, (k[1], "", "", ""))
    cc = cnt[k]; tot = sum(cc.values())
    wsL.cell(i, 1, BLOCK[k[0]]); wsL.cell(i, 2, en[0]); wsL.cell(i, 3, en[1]); wsL.cell(i, 4, en[2]); wsL.cell(i, 5, tot); wsL.cell(i, 6, len(emps[k]))
    wsP.cell(i, 1, BLOCK[k[0]]); wsP.cell(i, 2, en[0])
    for col, cl in zip(range(3, 8), ["BATE", "TOLERANCIA", "DIVERGENCIA", "SEM_DADO", "SEM_EFEITO"]):
        wsP.cell(i, col, cc.get(cl, 0))
    wsP.cell(i, 8, "=C%d+D%d+E%d" % (i, i, i)); c = wsP.cell(i, 9, '=IF(H%d=0,"",(C%d+D%d)/H%d)' % (i, i, i, i)); c.number_format = "0.0%"
    wsP.cell(i, 10, en[3])
    for w in (wsL, wsP):
        for col in range(1, 11):
            w.cell(i, col).border = BOX; w.cell(i, col).font = F_TXT
t = len(keys) + 5
wsP.cell(t, 2, "TOTAL").font = F_BOLD; wsL.cell(t, 2, "TOTAL").font = F_BOLD
for col in "CDEFGH":
    wsP["%s%d" % (col, t)] = "=SUM(%s5:%s%d)" % (col, col, t - 1); wsP["%s%d" % (col, t)].font = F_BOLD
wsP["I%d" % t] = "=(C%d+D%d)/H%d" % (t, t, t); wsP["I%d" % t].number_format = "0.0%"
wsL["E%d" % t] = "=SUM(E5:E%d)" % (t - 1)
widths(wsL, {"A": 30, "B": 52, "C": 70, "D": 60, "E": 14, "F": 11}); widths(wsP, {"A": 30, "B": 52, "C": 11, "D": 12, "E": 11, "F": 9, "G": 9, "H": 12, "I": 11, "J": 110})
wsL.freeze_panes = "C5"; wsP.freeze_panes = "C5"

wsM["A1"] = "DIVERGENCE BY MECHANISM - every real divergence, grouped by the rule the provider applies, with the norm and what the research says"; wsM["A1"].font = F_TITLE
wsM["A2"] = "Sum of absolute differences is shown only when 3 or more employees are affected (otherwise suppressed to avoid exposing an individual amount). Employee-lines can count twice when one line has two mechanisms. A sum adds every line of the mechanism (bases, reliefs and amounts alike) and shows size, not cash impact; the cash impact per mechanism is in the Impact column."; wsM["A2"].font = F_TXTI
hdr(wsM, 4, ["#", "Block", "Mechanism", "Employee-lines", "Employees", "Sum of absolute differences", "Norm", "Research position", "Impact", "Unit of the sum"])
r = 5
used = set()
for blk, sub, en, norm, pos, imp in MECH_EN:
    rows = [m for m in R["divergencias_por_mecanismo"] if m["bloco"] == blk and sub in m["mecanismo"] and id(m) not in used]
    if blk == "D-INDEMNIZACAO":
        rows = [m for m in rows if m["mecanismo"].startswith(sub) and "+ valor" not in m["mecanismo"]]
    for m in rows:
        used.add(id(m))
    lines = sum(m["linhas"] for m in rows); em = sum(m["empregados"] for m in rows); sd = sum(m["soma_abs_dif"] for m in rows)
    wsM.cell(r, 1, r - 4); wsM.cell(r, 2, BLOCK[blk]); wsM.cell(r, 3, en); wsM.cell(r, 4, lines); wsM.cell(r, 5, em)
    c = wsM.cell(r, 6, sd if em >= 3 else "suppressed (< 3 employees)"); c.number_format = NUM0
    wsM.cell(r, 7, norm); wsM.cell(r, 8, pos); wsM.cell(r, 9, imp)
    its = set(i for m in rows for i in m["itens"])
    wsM.cell(r, 10, "days" if its == {"dias"} else ("mixed: days + COP (COP from the value lines)" if "dias" in its else "COP"))
    for col in range(1, 11):
        wsM.cell(r, col).border = BOX; wsM.cell(r, col).font = F_TXT; wsM.cell(r, col).alignment = WRAP
    r += 1
rest = [m for m in R["divergencias_por_mecanismo"] if id(m) not in used]
for m in rest:   # combined indemnity mechanisms (days + value)
    wsM.cell(r, 1, r - 4); wsM.cell(r, 2, BLOCK[m["bloco"]])
    wsM.cell(r, 3, "Indemnity value with two mechanisms combined: " + ("more favourable day table" if "tabela" in m["mecanismo"] else "fraction truncated") + " + value on basic salary only")
    wsM.cell(r, 4, m["linhas"]); wsM.cell(r, 5, m["empregados"]); c = wsM.cell(r, 6, m["soma_abs_dif"] if m["empregados"] >= 3 else "suppressed (< 3 employees)"); c.number_format = NUM0
    wsM.cell(r, 7, "CST arts. 13, 64 and 127"); wsM.cell(r, 8, "See the rows above"); wsM.cell(r, 9, "Mixed"); wsM.cell(r, 10, "COP")
    for col in range(1, 11):
        wsM.cell(r, col).border = BOX; wsM.cell(r, col).font = F_TXT; wsM.cell(r, col).alignment = WRAP
    r += 1
wsM.cell(r, 3, "TOTAL employee-lines").font = F_BOLD; wsM.cell(r, 4, "=SUM(D5:D%d)" % (r - 1)).font = F_BOLD
widths(wsM, {"A": 4, "B": 26, "C": 70, "D": 13, "E": 11, "F": 22, "G": 44, "H": 52, "I": 34, "J": 22}); wsM.freeze_panes = "C5"

wsO["A1"] = "OFFICIAL EXAMPLES AND CALCULATORS"; wsO["A1"].font = F_TITLE
hdr(wsO, 3, ["Source", "What it shows", "Used how", "Result"])
ex = [
 ("UGPP, ABC Empleadores 2025 (worked example)", "Salary 5,000,000 + pacted non-salary 4,000,000: IBC for social security 5,400,000; family compensation fund on 5,000,000",
  "Same inputs run in the oracle (decision case D01 of the simulation workbook)", "Reproduced exactly: IBC 5,400,000; CCF base 5,000,000"),
 ("PILA Technical Annex 2 v30 (Resolution MSPS 2388 of 2016)", "Rounding (fields 47 ff.), FSP bands (fields 51-52), exoneration lock (field 76), contributor type 51 quarters",
  "Rules transcribed into the oracle parameters", "All suite cases on these rules OK (CO_Simulation_2026_10_30_V1.0.xlsx)"),
 ("Official online simulators (DIAN, UGPP, information operators)", "-", "None used in this validation", "Not applicable"),
]
for i, row in enumerate(ex, start=4):
    for j, v in enumerate(row, start=1):
        c = wsO.cell(i, j, v); c.font = F_TXT; c.alignment = WRAP; c.border = BOX
widths(wsO, {"A": 44, "B": 70, "C": 50, "D": 50})

wsR["A1"] = "Colombia Simulations - Law vs Provider (September 2026 payroll)"; wsR["A1"].font = F_TITLE
rm = [
 ("Purpose", "Equivalent of 'France Simulations - Official vs Internal.xlsx' for Colombia, where no official full gross-to-net simulator exists: the independent oracle (built from the statutes) recomputes the real September 2026 payroll of a client, and every line is compared with what the payroll provider calculated."),
 ("Question answered", "The specifications were already adjusted to this payroll in October 2026, so this test does not prove the research. It answers: (1) does a law-only engine agree with the provider? (2) where it does not, what does the research say?"),
 ("Sources", "Masked copies of the provider reports (IBC detail, withholding base, vertical gross-to-net, leave, master data, accumulated report, severance calculation). 261 employees, 372 indemnity simulation lines, 5,958 compared lines."),
 ("Data protection", "Aggregated only: counts per line and per mechanism. No employee index, ID, name or individual salary. Sums of differences shown only when 3+ employees are affected. The client is not named."),
 ("Sheets", "LAW SIMULATION and PROVIDER RESULT share the same rows (one per payroll line). BY MECHANISM lists every real divergence with the norm and the research position. OFFICIAL EXAMPLES lists the official worked examples reproduced."),
 ("Headline", "4,530 lines match within 1 COP and 342 within 100 COP (rounding). 742 diverge, all explained by 8 provider mechanisms (sheet BY MECHANISM). On 7 of them the research matches the law (the art. 114-1 test and the field-76 lock were aligned in the research on 30 Oct 2026); on the 8th (variable pay in the indemnity base) the research is silent: open point. 342 lines are not recomputable (no data), 2 have no effect."),
 ("Limits", "The salary / non-salary classification of each wage type is the provider's; the test checks the rules applied on that classification. Vacation pay, IBC of months with absence and Procedure 2 percentages need 12 months of history and were not recomputed."),
 ("Oracle", "oracle_v2.py with params.json (one primary source per parameter); comparison script and per-line result file kept with the validation working papers (not distributed: they hold the masked per-employee index)."),
]
for i, (a, bt) in enumerate(rm, start=3):
    wsR.cell(i, 1, a).font = F_BOLD; c = wsR.cell(i, 2, bt); c.font = F_TXT; c.alignment = WRAP
widths(wsR, {"A": 22, "B": 150})
wb.save(OUT)
print("mech rows", r - 5, "lines", len(keys), "used", len(used), "rest", len(rest))

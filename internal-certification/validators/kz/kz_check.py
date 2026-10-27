"""Kazakhstan - Mastercard (Representative office of MasterCard Europe SA in RK), October 2026, 1C payroll.
Scope (decision 14-10-2026): recalculation x 1C payroll x payment orders x bank; quarterly report 200.00, GL and master
= Not tested. Usage: python -I kz_check.py"""
import glob
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "common"))
sys.stdout.reconfigure(encoding="utf-8")

import pandas as pd  # noqa: E402

from framework import Evidence, eq, num  # noqa: E402

PKG = os.path.join(HERE, "..", "..", "Kazakhstan", "Mastercard - 2026-10")
VAL = os.path.join(PKG, "02 Validation")
X = os.path.join(VAL, "_extracted")

MRP, MZP = 4325, 85000                        # Budget law 239-VIII art. 7 (S02)
R_OPV, R_OPVR, R_SO, R_SN, R_VOSMS, R_OOSMS = 0.10, 0.035, 0.05, 0.06, 0.02, 0.03
DEADLINE = "2026-11-25"                       # 25th of the month after payment
KNP = {"ОПВ": "010", "ОПВР": "089", "СО": "012", "ВОСМС": "122", "ООСМС": "121", "ИПН": "911", "СН": "911"}
KBK = {"ИПН": "101201", "СН": "103101"}

ev = Evidence("Mastercard - Representative office of MasterCard Europe SA in RK - October 2026")

# ---- 1C payroll summary ----
df = pd.read_excel(os.path.join(X, "Payroll 1C October.xlsx"), header=None, dtype=object)
P = {}
for r in df.values.tolist():
    v = [x for x in r if not (isinstance(x, float) and pd.isna(x)) and x is not None]
    if v and isinstance(v[0], str) and v[0].strip():
        rest = v[1:] + [None, None, None]
        P[v[0].strip()] = (num(rest[0]) if not isinstance(rest[0], str) else rest[0], rest[1], rest[2])
gross = P["Начислено"][0]
days, hours = P["Начислено"][1], P["Начислено"][2]

# ---- payment orders (MT102 text) ----
orders = {}
for fp in glob.glob(os.path.join(X, "z*_*Swift.txt")):
    raw = open(fp, "rb").read().decode("utf-8-sig", "replace")
    part = raw[raw.rfind("{1:"):]                      # the file repeats the header block; use the complete last copy
    name = os.path.basename(fp)
    kind = "ЗП" if "Зарплат" in name else re.search(r"Перечисление_([^_]+)_", name).group(1)
    amt = re.search(r":32A:(\d{6})KZT([\d,]+)", part)
    orders[kind] = {"file": name, "date": "20" + amt.group(1), "amount": num(amt.group(2).replace(",", ".")),
                    "knp": (re.search(r"/KNP/(\d+)", part) or [None, None])[1],
                    "kbk": (re.search(r"/BCLASS/(\d+)", part) or [None, None])[1],
                    "iin": (re.search(r"/IDN/(\d{12})\s*\n/LA|/DT/\d+\s*\n/IDN/(\d{12})", part)),
                    "period": (re.search(r"/PERIOD/(\d+)", part) or [None, None])[1],
                    "ee_idn": re.findall(r"/IDN/(\d{12})", part), "payer": re.findall(r"/IDN/(\d{12})", part)[0],
                    "text": part}

# ---- payslip ----
import pdfplumber  # noqa: E402
with pdfplumber.open(glob.glob(os.path.join(X, "z02_*.pdf"))[0]) as _pdf:
    ps = "\n".join(pg.extract_text() or "" for pg in _pdf.pages)
ps_amt = lambda code: num(re.search(rf"^{code}\s.*?(-?[\d,]+\.\d{{2}})\s*$", ps, re.M).group(1))  # noqa: E731
slip = {"gross": num(re.search(r"Base Salary.*?([\d,]+\.\d{2})", ps).group(1)), "opv": ps_amt("540"),
        "vosms": ps_amt("540voms"), "ipn": ps_amt("565"), "net": ps_amt("722"),
        "days": int(re.search(r"Base Salary \(G\)\s+(\d+)", ps).group(1)),
        "emp": re.search(r"Employee:\s+(\d+)", ps).group(1), "period": re.search(r"(\w+ 2026)\s*$", ps.split("\n")[3] if
                                                                                    len(ps.split("\n")) > 3 else "", re.M)}

# ---- PRE template (client reporting) ----
pre = pd.read_excel(os.path.join(X, "z03_PRE Template 2025 PRE 100 HC_03.10.2026.xlsm"), sheet_name=None, header=None, dtype=object)
pl = pre["Payroll-Local"].values.tolist()
cycle = pl[1][1]
emprow = [x for x in next(r for r in pl if str(r[0]).strip().isdigit())
          if not (isinstance(x, float) and pd.isna(x)) and x is not None]
pr560 = pre["PR560"].values.tolist()

iin = "850520300013"
born = "1985-05-20"

# ================= A. scope =================
ev.check("A-01", "Scope", "1C payroll organisation and month; payslip month", "1 employee",
         P["Организация"][0] == "Мастеркард" and "Октябрь 2026" in str(df.values.tolist()) and "October 2026" in ps,
         f"1C 'Мастеркард' Октябрь 2026; payslip 'October 2026' (file name says 'Payslips August')")
ev.check("A-02", "Scope", "Same employee in 1C payment orders, bank transfer and payslip (IIN / name)", "1 employee",
         all(iin in o["text"] for o in orders.values() if o["file"].find("ИПН") < 0 and o["file"].find("СН") < 0)
         and "Zhamalov" in ps, f"IIN {iin} (born {born}); payslip employee no. {slip['emp']}; PRE EE# {emprow[0]}")

# ================= B. recalculation =================
opv = round(min(gross, 50 * MZP) * R_OPV, 2)
vosms = min(gross, 20 * MZP) * R_VOSMS
opvr = round(min(max(gross, MZP), 50 * MZP) * R_OPVR, 2)
so = min(max(gross - opv, MZP), 7 * MZP) * R_SO
oosms = min(gross, 40 * MZP) * R_OOSMS
sn = (gross - P["ОПВ"][0] - P["Взносы ОСМС"][0]) * R_SN
ipn_basic = (gross - P["ОПВ"][0] - P["Взносы ОСМС"][0] - 30 * MRP) * 0.10
ipn_nobasic = (gross - P["ОПВ"][0] - P["Взносы ОСМС"][0]) * 0.10
rows = [
    ("ОПВ 10% (Social Code art. 249)", opv, P["ОПВ"][0]),
    ("ВОСМС 2% (OSMS Law art. 28)", vosms, P["Взносы ОСМС"][0]),
    ("ОПВР 3.5% 2026, born after 1975 (Social Code art. 251)", opvr, P["Обязательные пенсионные взносы работодателя"][0]),
    ("СО 5% of (income - ОПВ), 1-7 МЗП (Social Code arts. 244-245)", so, P["Социальные отчисления"][0]),
    ("ООСМС 3% (OSMS Law art. 27)", oosms, P["Отчисления на ОСМС"][0]),
    ("СН 6% of (income - ОПВ - ВОСМС), no СО offset (Tax Code arts. 556-557)", sn, P["Социальный налог"][0]),
]
ev.d["recalc"] = [{"Item": n, "Statutory (unrounded)": round(e, 4), "1C / paid": a, "Difference": round(a - e, 2)} for n, e, a in rows]
ev.d["recalc"] += [{"Item": "ИПН - month alone, with 30 МРП basic deduction", "Statutory (unrounded)": round(ipn_basic, 2),
                    "1C / paid": P["ИПН"][0], "Difference": round(P["ИПН"][0] - ipn_basic, 2)},
                   {"Item": "ИПН - month alone, no basic deduction", "Statutory (unrounded)": round(ipn_nobasic, 2),
                    "1C / paid": P["ИПН"][0], "Difference": round(P["ИПН"][0] - ipn_nobasic, 2)}]
for i, (n, e, a) in enumerate(rows, 1):
    ev.check(f"B-0{i}", "Recalculation", n, "1 employee", eq(e, a, 0.5) and abs(a - e) < 0.5 or eq(e, a, 0.005),
             f"statutory {e:,.4f} / 1C {a:,.2f}")
ev.check("B-07", "Recalculation", "ИПН 10% after ОПВ, ВОСМС and basic deduction - cumulative YTD (Tax Code arts. 363, 401-403, 441)",
         "1 employee", False, f"1C {P['ИПН'][0]:,.2f}; October alone: {ipn_basic:,.2f} with the 30 МРП deduction, "
         f"{ipn_nobasic:,.2f} without; YTD figures not in the pack", result="Not tested")
ev.check("B-08", "Recalculation", "1C totals: Удержано = ИПН + ОПВ + ВОСМС; Выплачено = Начислено - Удержано; "
         "Справочно = СО + СН + ООСМС + ОПВР", "1 employee",
         eq(P["Удержано"][0], P["ИПН"][0] + P["ОПВ"][0] + P["Взносы ОСМС"][0], 0.01)
         and eq(P["Выплачено"][0], gross - P["Удержано"][0], 0.01)
         and eq(P["Справочно"][0], P["Социальные отчисления"][0] + P["Социальный налог"][0] + P["Отчисления на ОСМС"][0]
                + P["Обязательные пенсионные взносы работодателя"][0], 0.01))

# ================= C. payment orders =================
pairs = [("ИПН", P["ИПН"][0]), ("СН", P["Социальный налог"][0]), ("ОПВ", P["ОПВ"][0]), ("ОПВР", P["Обязательные пенсионные взносы работодателя"][0]),
         ("СО", P["Социальные отчисления"][0]), ("ВОСМС", P["Взносы ОСМС"][0]), ("ООСМС", P["Отчисления на ОСМС"][0]),
         ("ЗП", P["Выплата зарплаты"][0])]
for k, v in pairs:
    ev.recon(f"Payment order {k}", "1C payroll", v, f"MT102 {orders[k]['file']}", orders[k]["amount"])
bad = [f"{k}: КНП {orders[k]['knp']} (expected {KNP[k]})" for k in KNP if orders[k]["knp"] != KNP[k]]
bad += [f"{k}: КБК {orders[k]['kbk']} (expected {KBK[k]})" for k in KBK if orders[k]["kbk"] != KBK[k]]
ev.check("C-01", "Payment orders", "КНП per contribution and КБК for ИПН/СН (NB Resolution 203; MinFin Order 151)", "7 orders",
         not bad, "; ".join(bad))
ev.check("C-02", "Payment orders", "Contribution orders carry the employee IIN and period 102026", "5 orders",
         all(iin in orders[k]["text"] and orders[k]["period"] == "102026" for k in ("ОПВ", "ОПВР", "СО", "ВОСМС", "ООСМС")))
ev.check("C-03", "Payment orders", f"Payment dates not later than the deadline {DEADLINE} (25th of the following month)", "8 orders",
         all(o["date"] <= DEADLINE.replace("-", "") for o in orders.values()),
         "; ".join(f"{k} {o['date']}" for k, o in orders.items()))
ev.check("C-04", "Payment orders", "Salary transfer to the employee (IIN, net amount)", "1 transfer",
         iin in orders["ЗП"]["text"] and eq(orders["ЗП"]["amount"], P["Выплата зарплаты"][0], 0.01))

# ================= D. payslip =================
ev.check("D-01", "Payslip", "Payslip gross, ОПВ, ВОСМС, ИПН and net = 1C", "1 payslip",
         eq(slip["gross"], gross) and eq(slip["opv"], P["ОПВ"][0]) and eq(slip["vosms"], P["Взносы ОСМС"][0])
         and eq(slip["ipn"], P["ИПН"][0]) and eq(slip["net"], P["Выплачено"][0]),
         f"{slip['gross']} / {slip['opv']} / {slip['vosms']} / {slip['ipn']} / {slip['net']}")
tot_ded = re.search(r"Total deducted:\s+([\d,]+\.\d{2})", ps.replace("\n", " "))
ev.check("D-02", "Payslip", "Payslip totals: 'Total deducted' = ОПВ + ВОСМС + ИПН and 'Employee net pay' = net", "1 payslip",
         False, f"payslip prints Total deducted {tot_ded.group(1) if tot_ded else '?'} (= gross) and Employee net pay 0.00; "
         f"expected {P['Удержано'][0]:,.2f} and {P['Выплачено'][0]:,.2f}; net shown on line '722 TOTAL TO PAY'")
ev.check("D-03", "Payslip", "Days on payslip = days in 1C; payslip file name matches the period", "1 payslip",
         slip["days"] == days and "August" not in glob.glob(os.path.join(X, "z02_*.pdf"))[0],
         f"payslip {slip['days']} days / 1C {days} days, {hours} h; file 'Payslips August.xlsm - Zhamalov .pdf'")
ev.check("D-04", "Payslip", "Employee number on payslip = PRE template EE#", "1 employee", str(emprow[0]) == slip["emp"],
         f"payslip {slip['emp']} / PRE {emprow[0]}")

# ================= E. PRE template (client reporting) =================
ev.check("E-01", "PRE template", "PRE totals = 1C (gross, EE deductions, ER contributions, net)", "1 employee",
         eq(emprow[4], gross) and all(eq(v, w, 0.01) for v, w in zip(
             [next(r[2] for r in pre["Payroll Funding Request"].values.tolist() if r[1] == lab) for lab in ("Net Pay", "EE Deductions", "ER Deductions")],
             [P["Выплачено"][0], P["Удержано"][0], P["Справочно"][0]])), "Net 359,758.75; EE 95,182.95; ER 74,064.87")
ev.check("E-02", "PRE template", "PRE dates and controls: transaction dates = pay cycle; PR560 = Payroll-Local; no formula errors",
         "1 template", False, f"pay cycle {cycle}; employee rows dated {emprow[3]}; PR560 wage total "
         f"{pr560[2][1]} vs Payroll-Local {pr560[1][1]} (2x); '#NAME?' in Adjustments/Funding Requirement and ProcessLevel")
fund = {str(r[0]).strip(): (r[1], r[2]) for r in pre["Payroll Funding Request"].values.tolist() if isinstance(r[0], str)}
ev.check("E-03", "PRE template", "PRE GL code labels match the Kazakh items (СН = social tax, СО = social contributions)",
         "3 lines", False, f"13GL '{fund.get('13GL', ('?',))[0]}' = 24,020.91 (СН); 11GL '{fund.get('11GL', ('?',))[0]}' = "
         f"20,473 (СО); 21GL '{fund.get('21GL', ('?',))[0]}' = 13,648 (ООСМС)")

ev.nt("NT-01", "Quarterly declaration 200.00 and authority receipt", "Filed quarterly; Q4 2026 (Oct-Dec) is due 15.02.2027 "
      "(Tax Code arts. 445, 562). Not supplied. A 200.00 form approved under the new Code was not located (MinFin Order 39 "
      "app. 121/122 still applies - INFERENCE).", "Latest filed 200.00 (Q3 2026) with KGD receipt, or Q4 after filing.")
ev.nt("NT-02", "ИПН cumulative calculation", "Art. 441 computes ИПН year-to-date; January-September income, deductions and ИПН "
      "and the employee's basic-deduction application are not in the pack.", "1C tax card (налоговая карточка) / YTD "
      "ведомость for 2026 and the basic-deduction application.")
ev.nt("NT-03", "GL", "No GL in the pack.", "GL / accounting export for October 2026.")
ev.nt("NT-04", "Master data (exemptions, residency, disability)", "No master data; exemption status inferred from birth date "
      "in the IIN (1985) only.", "Employee master record.")
ev.nt("NT-05", "Rounding rule for СО/ВОСМС/ООСМС to whole tenge", "Not located in the Social Code / OSMS Law extracts.",
      "Official rule or GFSS/FSMS guidance.")
ev.save(VAL)

# Test 4 - leitor da folha REAL de setembro/2026 (PMI, ja mascarada). SO LEITURA das copias mascaradas.
# Monta, por empregado (indice E001...), as entradas para o oraculo e o que o provedor reporta.
# Uso: python -I leitor.py <dir 03-client-reports-masked> <saida entradas.json>
# Nao grava IDs mascarados na saida: a ordem E001.. e deterministica (ordenacao pelo ID mascarado do G2N).
import sys, json, datetime, collections
import openpyxl

SRC = sys.argv[1].rstrip("/\\") + "/"
OUT = sys.argv[2]

F_IBC = "1764_PMI_Detail_IBC_per_Employees_S.S._Report_202609.xlsx"
F_BOW = "1764_PMI_Base of Withholding 2026-09-01 - 2026-09-30.xlsx"
F_G2N = "Vertical G2N Dynamic 2026-09-01 - 2026-09-30.xlsx"
F_LV = "1764_PMI_Leave_Absence_Report_.xlsx"
F_ACC = "Accumulated Report.xlsx"
F_SEV = "Severance Massive Calculation Structure September 2026.xlsx"
F_MD = "1764_Master_Data_Report_202609.xlsx"


def sheet(f, header_row):
    wb = openpyxl.load_workbook(SRC + f, read_only=True, data_only=True)
    rows = list(wb.worksheets[0].iter_rows(min_row=header_row, values_only=True))
    h = [str(x).strip() if x is not None else "" for x in rows[0]]
    return h, [r for r in rows[1:] if r and r[0] not in (None, "", "GRAND TOTAL")]


def num(x):
    if x in (None, ""):
        return 0.0
    return float(x)


def dmy(s):
    if not s:
        return None
    s = str(s)[:10]
    if "-" in s and len(s.split("-")[0]) == 4:
        return s
    d, m, y = s.split("-")
    return "%s-%s-%s" % (y, m, d)


# 1) descricao e indicador salarial dos WT (Accumulated Report: WT Description nao foi mascarado; col. 'Salary Payment Indicator')
h, acc = sheet(F_ACC, 7)
WT = {}
for r in acc:
    if r[5] is not None:
        WT.setdefault(str(r[5]), {"desc": r[6], "salary_flag": r[7] == "X"})
# 2) master data
h, md = sheet(F_MD, 12)
ix = {k: h.index(k) for k in ["Employee ID", "Employee Professional Risk Class (ARL)", "Employee Group Code", "Employee Subgroup Code",
                              "Regime", "Tax Procedure 1", "Employment Status", "Basic Salary"]}
MD = {r[ix["Employee ID"]]: r for r in md}
# 3) G2N vertical
h, g2n = sheet(F_G2N, 9)
G = collections.OrderedDict()
for r in g2n:
    eid = r[0]
    e = G.setdefault(eid, {"hire": dmy(r[4]), "leave": dmy(r[5]), "salary_assigned": num(r[6]), "wt": collections.defaultdict(float)})
    if r[7] is not None:
        e["wt"][str(r[7])] += num(r[9])
# 4) IBC report
h, ibc = sheet(F_IBC, 11)
IBC = {r[0]: {"salary_value": num(r[2]), "nonwage_value": num(r[3]), "not_applicable_ss": num(r[4]), "ibc_total": num(r[5])} for r in ibc}
# 5) Base of Withholding
h, bow = sheet(F_BOW, 12)
BCOL = ["pct_retention", "basic_salary", "other_income", "income_total", "incrngo", "afc", "apv", "base1", "dep", "prepaid", "housing",
        "base2", "exempt25", "base3", "limit40", "total_relief", "limit_applied", "wht_basis", "wht_with", "wht_basis_without", "wht_without", "contingent"]
BOW = {r[0]: dict(zip(BCOL, [num(x) for x in r[3:25]])) for r in bow}
# 6) leaves
h, lv = sheet(F_LV, 10)
LV = collections.defaultdict(list)
for r in lv:
    LV[r[0]].append({"wt": str(r[3]), "desc": r[4], "from": dmy(r[5]), "to": dmy(r[6]), "days": num(r[7]), "amount": num(r[9])})

emps = []
for n, eid in enumerate(sorted(G.keys()), 1):
    g = G[eid]
    m = MD.get(eid)
    wt = {k: round(v, 2) for k, v in g["wt"].items() if v != 0}
    sal_earn = sum(v for k, v in wt.items() if WT.get(k, {}).get("salary_flag") and not k.startswith("79"))
    leave_pay = sum(v for k, v in wt.items() if k.startswith("794"))
    e = {
        "idx": "E%03d" % n,
        "integral": "62140" in wt or "62141" in wt,
        "salary_assigned": g["salary_assigned"],
        "hire": g["hire"], "leave": g["leave"],
        "arl_class": (m[ix["Employee Professional Risk Class (ARL)"]] if m else None),
        "group": (m[ix["Employee Group Code"]] if m else None),
        "subgroup": (m[ix["Employee Subgroup Code"]] if m else None),
        "regime": (m[ix["Regime"]] if m else None),
        "tax_procedure": (m[ix["Tax Procedure 1"]] if m else None),
        "wt": wt,
        "g2n_salary_flag_earnings_excl_leave": round(sal_earn, 2),
        "g2n_leave_payouts": round(leave_pay, 2),
        "ibc_report": IBC.get(eid),
        "bow": BOW.get(eid),
        "leaves": LV.get(eid, []),
    }
    emps.append(e)

json.dump({"generated": datetime.datetime.now().isoformat(timespec="seconds"), "source_dir": "03-client-reports-masked (copias mascaradas)",
           "wt_catalog": WT, "employees": emps}, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# severance massive calculation (indemnizacao art. 64) -> lista separada, sem nomes/IDs
h, sev = sheet(F_SEV, 11)
S = []
for k, r in enumerate(sev, 1):
    S.append({"idx": "S%03d" % k, "tipo_salario": r[7], "contrato": r[8], "ingreso": dmy(r[9]), "ajustada": dmy(r[10]),
              "salario_basico": num(r[11]), "variable": num(r[12]), "base": num(r[13]), "dias": num(r[14]), "valor": num(r[15])})
json.dump(S, open(OUT.replace(".json", "-indemnizacao.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("empregados", len(emps), "com IBC", sum(1 for e in emps if e["ibc_report"]), "com BoW", sum(1 for e in emps if e["bow"]),
      "integral", sum(e["integral"] for e in emps), "indemnizacao", len(S))

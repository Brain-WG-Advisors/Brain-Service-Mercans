# Gera cases.json (suite ~60+ casos). Valores derivados so de SMMLV/UVT ancoras.
import json
S = 1750905
UVT = 52374
cases = []


def add(id, name, cls, module, **kw):
    d = {"id": id, "name": name, "class": cls, "module": module}
    d.update(kw)
    cases.append(d)


def m(id, name, cls, sal, **kw):
    kw.setdefault("period", "2026-03")
    add(id, name, cls, "monthly", salary=sal, **kw)


# --- A. base minima, auxilio de transporte, parcial
m("C01", "1 SMMLV com auxilio, mes completo", "minimo", S)
m("C02", "2 SMMLV exato (auxilio SIM)", "borda auxilio", 2 * S)
m("C03", "2 SMMLV +1 (auxilio NAO)", "borda auxilio", 2 * S + 1)
m("C04", "2 SMMLV -1 (auxilio SIM)", "borda auxilio", 2 * S - 1)
m("C05", "ingresso no mes: 17 dias a 1 SMMLV", "mes parcial", S, days=17)
m("C06", "ingresso no mes: 12 dias a 2.500.000", "mes parcial", 2500000, days=12)
# --- B. FSP
m("C07", "FSP 4 SMMLV -1 (sem FSP)", "FSP", 4 * S - 1)
m("C08", "FSP 4 SMMLV exato", "FSP", 4 * S)
m("C09", "FSP 16 SMMLV -1", "FSP", 16 * S - 1)
m("C10", "FSP 16 SMMLV exato (+0,2)", "FSP", 16 * S)
m("C11", "FSP 17 SMMLV exato (+0,2 ainda)", "FSP", 17 * S)
m("C12", "FSP 17 SMMLV +1 (+0,4)", "FSP", 17 * S + 1)
m("C13", "FSP 19 SMMLV +1 (+0,8)", "FSP", 19 * S + 1)
m("C14", "FSP 20 SMMLV exato (+0,8)", "FSP", 20 * S)
m("C15", "FSP 20 SMMLV +1 (+1,0)", "FSP", 20 * S + 1)
# --- C. ET 114-1
m("C16", "exoneracao 114-1: 10 SMMLV -1 (exonerado)", "exoneracao", 10 * S - 1)
m("C17", "exoneracao 114-1: 10 SMMLV exato (NAO exonerado)", "exoneracao", 10 * S)
m("C18", "empleador NAO exonerado (pessoa fisica/regime nao 114-1) 3.000.000", "exoneracao", 3000000, exonerated=False)
# --- D. IBC cap, integral
m("C19", "IBC teto: 25 SMMLV exato", "IBC teto", 25 * S)
m("C20", "IBC teto: 25 SMMLV +1.000.000 (corta)", "IBC teto", 25 * S + 1000000)
m("C21", "IBC teto: 30 SMMLV (corta em 25)", "IBC teto", 30 * S)
m("C22", "salario integral 13 SMMLV (IBC 70%)", "integral", 13 * S, integral=True)
m("C23", "salario integral 40 SMMLV (70% > 25 SMMLV => teto)", "integral", 40 * S, integral=True)
# --- E. Ley 1393
m("C24", "Ley 1393: nao salarial 40% exato (2.000.000 de 5.000.000)", "ley1393", 3000000, nonsalary=2000000)
m("C25", "Ley 1393: nao salarial 40% +1 (2.000.001)", "ley1393", 3000000, nonsalary=2000001)
m("C26", "Ley 1393: nao salarial 3.000.000 (50%)", "ley1393", 3000000, nonsalary=3000000)
m("C27", "Ley 1393: nao salarial 400.000 (abaixo)", "ley1393", 3000000, nonsalary=400000)
# --- F. retencion: tabla en bordes (base ya depurada)
for lbl, uvt in (("95", 95), ("150", 150), ("360", 360), ("640", 640), ("945", 945), ("2300", 2300)):
    add("C28" + chr(96 + len(cases) % 26), "tabla 383: base %s UVT -1 COP" % lbl, "ret tabla", "ret_table", base_cop=uvt * UVT - 1)
    add("C29" + chr(96 + len(cases) % 26), "tabla 383: base %s UVT exata" % lbl, "ret tabla", "ret_table", base_cop=uvt * UVT)
    add("C30" + chr(96 + len(cases) % 26), "tabla 383: base %s UVT +1 COP" % lbl, "ret tabla", "ret_table", base_cop=uvt * UVT + 1)
# renumera tabla
n = 0
for c in cases:
    if c["module"] == "ret_table":
        n += 1
        c["id"] = "T%02d" % n
# --- G. retencion con depuracion completa
m("R01", "retencion: 8.000.000 sem deducciones (25% exento)", "ret depuracion", 8000000)
m("R02", "retencion: 8.000.000 + dependiente", "ret depuracion", 8000000, ret={"dependientes": True})
m("R03", "retencion: 8.000.000 + AFC 1.500.000", "ret depuracion", 8000000, ret={"afc": 1500000})
m("R04", "retencion: 8.000.000 + medicina prepagada 1.200.000 (tope 16 UVT)", "ret depuracion", 8000000, ret={"prepagada": 1200000})
m("R05", "retencion: 8.000.000 + intereses vivienda 6.000.000 (tope 100 UVT)", "ret depuracion", 8000000, ret={"vivienda": 6000000})
m("R06", "retencion: tope 40% ligado (10.000.000 con todas as deducoes)", "ret tope 40%", 10000000, ret={"dependientes": True, "prepagada": 837984, "vivienda": 5237400})
m("R07", "retencion: tope 1340 UVT ligado (40.000.000 + AFC 10.000.000)", "ret tope 1340", 40000000, ret={"afc": 10000000, "dependientes": True})
m("R08", "retencion: 25% exento com tope 790 UVT/ano ligado (20.000.000)", "ret 25%", 20000000)
m("R09", "retencion: abaixo de 95 UVT (3.500.000)", "ret procedimiento 1", 3500000)
m("R10", "retencion: ingreso 5.500.000 (1o tramo 19%)", "ret procedimiento 1", 5500000)
# --- H. horas extras y recargos
m("H01", "marzo: HED 10h + HEN 5h + RN 20h (divisor 220)", "horas", 3000000,
  extras=[{"type": "HED", "hours": 10, "date": "2026-03-10"}, {"type": "HEN", "hours": 5, "date": "2026-03-10"}, {"type": "RN", "hours": 20, "date": "2026-03-10"}])
m("H02", "marzo: domingo 8h ordinarias (80%) + HED dominical 4h + RN dominical 6h", "horas", 3000000,
  extras=[{"type": "DOM", "hours": 8, "date": "2026-03-08"}, {"type": "HED_DOM", "hours": 4, "date": "2026-03-08"}, {"type": "RN_DOM", "hours": 6, "date": "2026-03-08"}])
m("H03", "junho 28 (dom, 80%) e HED 30/jun (220)", "horas", 3000000, period="2026-06",
  extras=[{"type": "DOM", "hours": 8, "date": "2026-06-28"}, {"type": "HED", "hours": 4, "date": "2026-06-30"}])
m("H04", "julho split: 14/jul HED (220) e 15/jul HED (210)", "horas borda divisor", 3000000, period="2026-07",
  extras=[{"type": "HED", "hours": 10, "date": "2026-07-14"}, {"type": "HED", "hours": 10, "date": "2026-07-15"}])
m("H05", "julho: dominical 90% desde 1/jul (dom 5/jul) e 19/jul (210)", "horas borda dominical", 3000000, period="2026-07",
  extras=[{"type": "DOM", "hours": 8, "date": "2026-07-05"}, {"type": "DOM", "hours": 8, "date": "2026-07-19"}, {"type": "HED_DOM", "hours": 2, "date": "2026-07-19"}])
m("H06", "agosto: 90% e divisor 210", "horas", 3000000, period="2026-08",
  extras=[{"type": "HED", "hours": 10, "date": "2026-08-12"}, {"type": "HEN", "hours": 5, "date": "2026-08-12"}, {"type": "RN", "hours": 20, "date": "2026-08-12"},
          {"type": "DOM", "hours": 8, "date": "2026-08-09"}, {"type": "HEN_DOM", "hours": 2, "date": "2026-08-09"}])
m("H07", "agosto 1 SMMLV com HED 10h (aux + extras)", "horas", S, period="2026-08", extras=[{"type": "HED", "hours": 10, "date": "2026-08-12"}])
# --- I. prima / cesantias
add("P01", "prima 1o semestre salario 3.000.000 (180 dias)", "prima", "prestaciones", salary=3000000, days=180, kind="prima")
add("P02", "prima 1 SMMLV com auxilio (180 dias)", "prima", "prestaciones", salary=S, days=180, kind="prima")
add("P03", "prima 2o semestre ingresso 1/set (120 dias) 4.000.000", "prima", "prestaciones", salary=4000000, days=120, kind="prima")
add("P04", "cesantias+intereses ano completo 3.000.000", "cesantias", "prestaciones", salary=3000000, days=360, kind="cesantias")
add("P05", "cesantias+intereses 1 SMMLV (com auxilio) ano completo", "cesantias", "prestaciones", salary=S, days=360, kind="cesantias")
add("P06", "cesantias+intereses fracao 200 dias 5.000.000", "cesantias", "prestaciones", salary=5000000, days=200, kind="cesantias")
# --- J. vacaciones
add("V01", "vacaciones gozadas 15 dias habiles 3.000.000", "vacaciones", "vacaciones", salary=3000000, mode="gozadas", dias_habiles=15)
add("V02", "vacaciones compensadas 7 dias habiles (<= metade)", "vacaciones", "vacaciones", salary=3000000, mode="compensadas", dias_habiles=7)
add("V03", "vacaciones compensadas 8 dias habiles (> metade => nao permitido)", "vacaciones", "vacaciones", salary=3000000, mode="compensadas", dias_habiles=8)
add("V04", "vacaciones mixta 7,5 gozadas + 7,5 compensadas", "vacaciones", "vacaciones", salary=3000000, mode="mixta", gozadas=7.5, compensadas=7.5)
add("V05", "vacaciones causacion 360 dias 3.000.000", "vacaciones", "vacaciones", salary=3000000, mode="causacion", days_worked=360)
# --- K. incapacidad, maternidad
add("I01", "incapacidad comum 2 dias (empleador) 3.000.000", "incapacidad", "incapacidad", salary=3000000, days=2)
add("I02", "incapacidad comum 10 dias (1-2 e 3-10)", "incapacidad", "incapacidad", salary=3000000, days=10)
add("I03", "incapacidad comum 100 dias (1-2,3-90,91-100)", "incapacidad", "incapacidad", salary=3000000, days=100)
add("I04", "incapacidad comum 180 dias", "incapacidad", "incapacidad", salary=3000000, days=180)
add("M01", "licenca maternidade 18 semanas 3.000.000", "maternidade", "maternidad", salary=3000000)
# --- L. terminacao
add("T-A", "indefinido sem justa causa <10 SMMLV, 4a6m (2022-03-15 a 2026-09-30) 5.000.000", "terminacao", "terminacion", salary=5000000, start="2022-03-15", end="2026-09-30")
add("T-B", "indefinido sem justa causa >=10 SMMLV, 2a6m 20.000.000", "terminacao", "terminacion", salary=20000000, start="2024-01-10", end="2026-06-30")
add("T-C", "indefinido <1 ano 4.000.000 (2026-02-01 a 2026-10-01)", "terminacao", "terminacion", salary=4000000, start="2026-02-01", end="2026-10-01")
add("T-D", "borda 10 SMMLV -1, 3 anos", "terminacao", "terminacion", salary=10 * S - 1, start="2023-01-01", end="2025-12-31")
add("T-E", "borda 10 SMMLV exato, 3 anos", "terminacao", "terminacion", salary=10 * S, start="2023-01-01", end="2025-12-31")
# --- M. PILA tipo 51
for d in (1, 7, 8, 14, 15, 21, 22, 30):
    add("L%02d" % d, "PILA tipo 51: %d dias" % d, "pila51", "pila51", days=d)
# --- N. PENDENTE
pend = [
    ("X01", "aprendiz SENA (cuota de aprendizaje/aportes)", "lei em aberto: Ley 789/2002 art.30 e reforma Ley 2466/2025 nao resolvidas localmente"),
    ("X02", "incapacidad comum com piso SMLDV (salario 1 SMMLV, 5 dias)", "piso de 1 SMLDV por dia: base legal nao pacificada no texto local (CST 227 sem piso)"),
    ("X03", "licenca nao remunerada: aportes a salud/pension/ARL/CCF", "lei em aberto: Decreto 780/2016 e AT2 (SLN) vs jurisprudencia"),
    ("X04", "mesada de junho (14a mesada/pensionados) em PILA tipo pensionado", "AT3 v15; regime pos Ley 2381 nao resolvido"),
    ("X05", "FSP regime 'N' (Ley 2381/2024 art.20): 4-7 SMMLV 1,0% .. >=20 2,5%", "AT2 v30 traz dois regimes; eficacia da Ley 2381 nao resolvida"),
    ("X06", "retencao sobre prima de servicos (proc.1: tabela so sobre a prima)", "DUR 1.2.4.1.3 b: depuracao da prima nao detalhada localmente"),
    ("X07", "deducao 72 UVT por dependente (ET 336 num.3) na retencao mensal", "texto local so no contexto da declaracao anual"),
]
for i, n, r in pend:
    add(i, n, "pendente", "monthly", salary=0, pending=r)
json.dump({"anchors": {"SMMLV": S, "UVT": UVT, "AUX": 249095}, "cases": cases}, open("cases.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(cases), "cases")

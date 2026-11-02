# Casos derivados dos exemplos da research (inputs copiados dos enunciados; valores esperados so no compare.py)
import json
S = 1750905
c = []
def add(i, n, mod, **kw):
    d = {"id": i, "name": n, "module": mod, "class": "research-example"}
    d.update(kw); c.append(d)
add("RC01", "CCG 4.3 ingreso 12/ago/2026, 2.400.000, 20 dias", "monthly", salary=2400000, days=20, period="2026-08", ret={"sub30": True})
add("RC02", "CCG 6.1.1 / 6.3 Ex.1 agosto 8.000.000", "monthly", salary=8000000, period="2026-08")
add("RC03", "CCG 6.3 Ex.2 deducoes (vivienda 1,2M, prepagada 0,7M, 2 dependentes)", "monthly", salary=8000000, period="2026-08",
    ret={"dependientes": True, "dep72": 2, "vivienda": 1200000, "prepagada": 700000})
add("RC04", "CCG 6.3 Ex.3 alternativa residente 15.000.000", "monthly", salary=15000000, period="2026-08")
add("RC05", "CCG 6.3 Ex.4 8.000.000 + bono nao salarial 20.000.000", "monthly", salary=8000000, nonsalary=20000000, period="2026-09")
add("RC06", "Spec NominaElectronica/350/PILA/220 marco 2026, 12.000.000", "monthly", salary=12000000, period="2026-03")
add("RC07", "Payslip EN: 18M + HE 250k + RN 250k + comissoes 700k (valores dados)", "monthly", salary=18000000, commission=1200000, period="2026-08")
add("RC08", "CCG 4.5 prima 1o sem 2026, 2.400.000", "prestaciones", salary=2400000, days=180, kind="prima")
add("RC09", "CCG 9.1/8.x pago vacaciones na rescisao, 510 dias, 2.400.000", "vacaciones", salary=2400000, mode="causacion", days_worked=510)
add("RC10", "Payslip: provisao prima mensal sobre 19.200.000 (30 dias)", "prestaciones", salary=19200000, days=30, kind="prima")
add("RC11", "Payslip: provisao vacacoes mensal sobre 18.950.000 (30 dias)", "vacaciones", salary=18950000, mode="causacion", days_worked=30)
add("RC12", "Spec Cesantias 006: base 2.000.000 (1.750.905+aux) 360 dias", "prestaciones", salary=S, days=360, kind="cesantias")
add("RC13", "Spec 220/2276: cesantias saldo 2025 sobre 12.000.000 (360 dias)", "prestaciones", salary=12000000, days=360, kind="cesantias")
add("RC14", "CCG 1.3 semanal 500.000x4 = 2.000.000 (base)", "monthly", salary=2000000, period="2026-03", retention=False)
add("RC15", "CCG 1.3 semanal 500.000x5 = 2.500.000 (base)", "monthly", salary=2500000, period="2026-03", retention=False)
add("RC16", "CCG 1.5 arredondamento 8.000.000 (ARL 0,522%)", "monthly", salary=8000000, period="2026-03", retention=False)
add("RC17", "Spec PILA-007 pensionista: FSP 1% (mesada 22.000.000 = 12,56 SMMLV)", "monthly", salary=0, pending="fora do escopo do oraculo: pensionados (Ley 1250/2008 nao local; AT3)")
json.dump({"cases": c}, open("cases_research.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(c))

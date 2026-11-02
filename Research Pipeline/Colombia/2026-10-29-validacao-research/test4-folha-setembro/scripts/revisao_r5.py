# -*- coding: utf-8 -*-
"""Test 4 - revisao da rodada 5 (2026-11-02): achados de RETENCAO contra o provedor a luz de
  A-1: tetos de 790 UVT (ET 206 num. 10), 1.340 UVT (ET 336 num. 3 / DUR 1.2.4.1.6 par. 3) e 3.800 UVT AFC
       (DUR 1.2.1.22.43) sao ANUAIS, controlados pelo acumulado do ano, sem 1/12 (CE S4 rad. 24047, 28/10/2021);
  A-2: cesantias e intereses nao sofrem retencao (Ley 100 art. 135 par. 3; DUR 1.2.4.1.11).
O oraculo (oracle/oracle_v2.py) NAO e alterado: como em revisao/rodada5/scripts/oracle_r5_ytd.py, o limite mensal que ele
le (PAR[...]['value'] * UVT / 12) e trocado, so durante a chamada, pelo SALDO anual suposto em setembro.

Sem historico jan-ago por empregado, o saldo de setembro e desconhecido. Tres cenarios de saldo (aplicados aos 3 tetos):
  S0  = 0                   (sem premissa nenhuma: o ano ja teria consumido tudo)        -> retencao maxima possivel
  S1  = 1/12 do teto anual  (premissa fraca: saldo >= 1/12; = calculo do oraculo v2)
  S4  = 4/12 do teto anual  (premissa P: jan-ago o agente nunca deu mais que 1/12 por mes -> consumo <= 8/12)
  S12 = teto anual inteiro  (nada consumido: ingresso no mes)                             -> retencao minima possivel
Sob P, a retencao correta de setembro fica em [R(S12), R(S4)]. Sem premissa, em [R(S12), R(S0)].
Entradas: so as do provedor no Base of Withholding (renda, INCRNGO, dependentes, prepagada, vivienda, AFC+APV), para
isolar o efeito dos tetos. Proc. 1 = tabela art. 383; proc. 2 = base x % do provedor (o % semestral nao e recalculado);
proc. '3' fica fora (como no comparar_v2).
Uso: python -I revisao_r5.py <entradas.json do leitor.py> <resultados-v2.json> [saida-resultados-r5.json]
A saida grava so classe e diferencas por indice mascarado (E###), nunca valores absolutos.
"""
import sys, json, os, importlib.util, collections
from decimal import Decimal as Dc

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
ORA = os.path.normpath(os.path.join(HERE, "..", "..", "oracle", "oracle_v2.py"))
spec = importlib.util.spec_from_file_location("oracle_v2", ORA)
O = importlib.util.module_from_spec(spec)
spec.loader.exec_module(O)
UVT = O.UVT
K = {"25": "RET_EXENTA25_UVT_ANO", "cap": "RET_CAP_UVT_ANO", "afc": "RET_AFC_MAX_UVT_ANO"}
ANO = {k: Dc(str(O.V(v))) for k, v in K.items()}
assert ANO == {"25": 790, "cap": 1340, "afc": 3800}, ANO
M = {k: ANO[k] * UVT / 12 for k in ANO}  # 1/12 em COP
TOL = 100  # mesma tolerancia do comparar_v2

ENT = json.load(open(sys.argv[1], encoding="utf-8"))
RV2 = json.load(open(sys.argv[2], encoding="utf-8"))
OUT = sys.argv[3] if len(sys.argv) > 3 else None


def ret(b, frac, proc2):
    """retencao de setembro com saldo = frac x teto anual (os 3 tetos)."""
    old = {k: O.PAR[v]["value"] for k, v in K.items()}
    try:
        for k, v in K.items():
            O.PAR[v]["value"] = str(ANO[k] * frac * 12)  # o oraculo divide por 12 -> saldo = frac x anual
        r = O.retencion(Dc(str(b["income_total"])), Dc(str(b["incrngo"])), b["dep"] > 0, b["prepaid"], b["housing"],
                        b["afc"] + b["apv"], None)
    finally:
        for k, v in K.items():
            O.PAR[v]["value"] = old[k]
    val = round(r["ret_base_gravable"] * b["pct_retention"]) if proc2 else r["ret_valor_retener"]
    return val, r


def raw_benef(b):
    """beneficios sem nenhum teto UVT (so 25%, 30% AFC e 40%): o maximo que o mes pode pedir."""
    base1 = b["income_total"] - b["incrngo"]
    dep = min(0.1 * b["income_total"], 32 * float(UVT)) if b["dep"] > 0 else 0.0
    deds = dep + min(b["prepaid"], 16 * float(UVT)) + min(b["housing"], 100 * float(UVT))
    afc = min(b["afc"] + b["apv"], 0.3 * b["income_total"])
    e25 = 0.25 * max(base1 - deds - afc, 0.0)
    return {"base1": base1, "e25": e25, "afc": afc, "total": deds + afc + e25, "cap40": 0.4 * base1}


cases = []
for e in ENT["employees"]:
    b = e["bow"]
    if not b or b["income_total"] == 0:
        continue
    proc = "3" if e.get("tax_procedure") == "3" else ("1" if b["pct_retention"] == 0 else "2")
    rb = raw_benef(b)
    applied_prov = rb["base1"] - b["wht_basis"]
    tot_prov = b["dep"] + b["prepaid"] + b["housing"] + b["afc"] + b["apv"] + b["exempt25"]
    # comportamento do provedor
    if abs(applied_prov) <= 1 and tot_prov > 0:
        comp = "ZERO"  # nenhum beneficio aplicado (mecanismo #2 do RELATORIO-TEST4)
    elif (abs(b["exempt25"] - float(M["25"])) <= 5 and rb["e25"] > float(M["25"]) + 1) or \
         (abs(applied_prov - float(M["cap"])) <= 5 and min(rb["total"], rb["cap40"]) > float(M["cap"]) + 1):
        comp = "1/12"  # o provedor cortou no 1/12 de 790 e/ou de 1.340 com o mes pedindo mais
    else:
        comp = "SEM_TETO"  # nenhum teto UVT mensal ligado no provedor
    exc_1_12 = b["exempt25"] > float(M["25"]) + 5 or applied_prov > float(M["cap"]) + 5  # provedor acima do 1/12?
    rec = {"emp": e["idx"], "proc": proc, "comportamento_provedor": comp, "provedor_acima_de_1_12": exc_1_12,
           "e25_bruto_acima_1_12": rb["e25"] > float(M["25"]) + 1, "e25_bruto_acima_4_12": rb["e25"] > 4 * float(M["25"]),
           "cap_1340_acima_4_12": min(rb["total"], rb["cap40"]) > 4 * float(M["cap"])}
    if proc == "3":
        rec["categoria"] = "FORA (proc. 3, nao recalculado)"
        cases.append(rec)
        continue
    prov = b["wht_with"]
    R = {k: ret(b, f, proc == "2")[0] for k, f in (("S0", Dc(0)), ("S1", Dc(1) / 12), ("S4", Dc(4) / 12), ("S12", Dc(1)))}
    d = {k: round(prov - v, 2) for k, v in R.items()}  # provedor - cenario (positivo = provedor reteve mais)
    rec.update({"dif_vs_" + k: v for k, v in d.items()})
    over_P = d["S4"] > TOL       # sob P, reteve a mais com certeza
    under_P = d["S12"] < -TOL     # sob P, reteve a menos com certeza
    over_weak = d["S1"] > TOL     # sob a premissa fraca (saldo >= 1/12)
    over_any = d["S0"] > TOL      # sem premissa nenhuma
    if over_any:
        cat = "(a0) a mais sem premissa nenhuma"
    elif comp == "ZERO" and over_weak:
        cat = "(a) conclusivo: nenhum beneficio aplicado"
    elif comp == "1/12" and over_P:
        cat = "(c) provedor aplicou 1/12: retem a mais sob P"
    elif over_P:
        cat = "(a) conclusivo sob P (outro)"
    elif under_P:
        cat = "(u) retem a menos sob P"
    elif abs(d["S4"]) <= TOL and abs(d["S12"]) <= TOL:
        cat = "OK: tetos nao interferem (saldo >= 4/12 cobre o mes)"
    else:
        cat = "(b) depende do acumulado"
    rec["categoria"] = cat
    cases.append(rec)

# ---------- A-2: cesantias / intereses pagos no mes (WT de pagamento ao empregado) ----------
CES = {"62110": "Cash-out of Severance Pay", "62117": "Cash-out of Interest Severance Pay",
       "62126": "Advance Severance Last Year", "62127": "Advance Interest Severance Pay"}
a2 = []
for e in ENT["employees"]:
    amt = sum(v for k, v in e["wt"].items() if k in CES)
    if not amt:
        continue
    b = e["bow"] or {}
    # se as cesantias entrassem na renda de retencao, a parcela "other income" do BoW teria de ser >= o valor pago
    a2.append({"emp": e["idx"], "wts": sorted(k for k in e["wt"] if k in CES),
               "cesantias_na_renda_de_retencao": bool(b) and b.get("other_income", 0) >= amt - 1})

# ---------- achados nao-retencao (114-1, art. 64): de resultados-v2.json (so diferencas) ----------
det = RV2["detalhe"]
exon = [l for l in det if l["classe"] == "DIVERGENCIA" and str(l.get("mecanismo", "")).startswith("exoneracao 114-1")]
exon8 = {l["emp"] for l in exon if "provedor cobra" in l.get("mecanismo", "")}
x114 = {"empregados_provedor_cobra": len(exon8),
        "soma_dif_COP_nesses": round(sum(l["dif"] for l in exon if l["emp"] in exon8)),
        "por_linha": dict(collections.Counter(l["linha"] for l in exon if l["emp"] in exon8)),
        "outros_empregados_114_1": sorted({l["emp"] for l in exon} - exon8).__len__()}
ind = [l for l in det if l["bloco"] == "D-INDEMNIZACAO" and l["classe"] == "DIVERGENCIA" and l["linha"] == "valor"]
trunc_sem_var = [l for l in ind if "truncada" in l.get("mecanismo", "") and "variavel" not in l.get("mecanismo", "")]
so_basico = [l for l in ind if "so o salario basico" in l.get("mecanismo", "")]
x64 = {"truncada_sem_variavel_linhas": len(trunc_sem_var), "truncada_sem_variavel_soma_dif": round(sum(l["dif"] for l in trunc_sem_var)),
       "valor_so_basico_linhas": len(so_basico)}
v2_ret = [l for l in det if l["bloco"] == "C-RETEFUENTE" and l["classe"] == "DIVERGENCIA" and l["linha"].startswith("retencion")]

# ---------- resumo ----------
summ = collections.defaultdict(lambda: {"n": 0, "proc": collections.Counter(), "soma_dif_S1": 0.0, "soma_dif_S4": 0.0, "soma_dif_S12": 0.0,
                                        "soma_dif_S0": 0.0})
for c in cases:
    s = summ[(c["categoria"], c["comportamento_provedor"])]
    s["n"] += 1
    s["proc"][c["proc"]] += 1
    for k in ("S0", "S1", "S4", "S12"):
        s["soma_dif_" + k] += c.get("dif_vs_" + k, 0.0)
res = {"regra": "saldo anual em setembro: S0=0, S1=1/12, S4=4/12, S12=anual; sob P (jan-ago <= 1/12 por mes) correto em [R(S12), R(S4)]",
       "empregados_com_renda_no_BoW": len(cases),
       "provedor_acima_de_1_12_em_algum_caso": sum(c["provedor_acima_de_1_12"] for c in cases),
       "e25_bruto_acima_de_4_12": sum(c["e25_bruto_acima_4_12"] for c in cases),
       "cap1340_acima_de_4_12": sum(c["cap_1340_acima_4_12"] for c in cases),
       "categorias": [{"categoria": k[0], "comportamento_provedor": k[1], "empregados": v["n"], "proc": dict(v["proc"]),
                       **{kk: round(vv) for kk, vv in v.items() if kk.startswith("soma")}}
                      for k, v in sorted(summ.items())],
       "v2_divergencias_retencao": {"linhas": len(v2_ret), "empregados": len({l["emp"] for l in v2_ret}),
                                    "soma_dif": round(sum(l["dif"] for l in v2_ret))},
       "A2_cesantias": {"empregados_com_pagamento_no_mes": len(a2),
                        "com_cesantias_na_renda_de_retencao": sum(x["cesantias_na_renda_de_retencao"] for x in a2),
                        "wts": sorted({w for x in a2 for w in x["wts"]})},
       "x114_1": x114, "art64": x64}
print(json.dumps(res, ensure_ascii=False, indent=1))
if OUT:
    json.dump({"resumo": res, "detalhe": cases, "a2": a2,
               "nota_privacidade": "so classe e diferencas (provedor - cenario) por indice mascarado; sem valores absolutos"},
              open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

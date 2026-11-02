# -*- coding: utf-8 -*-
"""Rodada 5 (2026-11-02), A-1: roda o oraculo v2 (oracle/oracle_v2.py, NAO alterado) nos casos de retencao da suite
com os tetos de 790 e 1.340 UVT ANUAIS controlados pelo acumulado do ano (CE S4 rad. 24047/2021; Decreto 2231/2023 art. 9;
DIAN Concepto 011383/2024 IV.1), em vez do 1/12 mensal do oraculo.

Como: para cada caso 'monthly' com retencao, primeiro roda o oraculo como esta (1/12) e marca se o 25% (790/12) ou o teto
conjunto (1.340/12) limitou o resultado. Para os casos limitados, simula jan..dez de 2026 com a premissa 'mesmo pagamento
desde 1/1, sem outra renda isenta': em cada mes o limite do oraculo (PAR[...]['value'] * UVT / 12) e trocado, so durante a
chamada, por (limite anual - consumo do ano ate o mes anterior). O codigo do oraculo nao muda; so o valor do parametro lido.
A-2 (cesantias de nao residente): o oraculo nao modela retencao de nao residente (nao ha ET 408 no codigo) -> nao aplicavel.
Uso: python -I oracle_r5_ytd.py   (grava ../oracle-r5-ytd.json e imprime o resumo)
"""
import os, sys, json, importlib.util
from decimal import Decimal as Dc
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
VAL = os.path.normpath(os.path.join(HERE, '..', '..', '..'))
ORA = os.path.join(VAL, 'oracle')
spec = importlib.util.spec_from_file_location('oracle_v2', os.path.join(ORA, 'oracle_v2.py'))
O = importlib.util.module_from_spec(spec); spec.loader.exec_module(O)
UVT = O.UVT
A790, A1340 = Dc(790) * UVT, Dc(1340) * UVT
K25, KCAP = 'RET_EXENTA25_UVT_ANO', 'RET_CAP_UVT_ANO'
assert O.V(K25) == 790 and O.V(KCAP) == 1340, (O.V(K25), O.V(KCAP))


def load(fn):
    c = json.load(open(os.path.join(ORA, fn), encoding='utf-8'))
    return c['cases'] if isinstance(c, dict) else c


def run_with_room(c, room25, roomcap):
    """roda monthly(c) com o limite mensal do oraculo = 'room' (COP)."""
    old25, oldcap = O.PAR[K25]['value'], O.PAR[KCAP]['value']
    try:
        O.PAR[K25]['value'] = str(max(room25, Dc(0)) * 12 / UVT)
        O.PAR[KCAP]['value'] = str(max(roomcap, Dc(0)) * 12 / UVT)
        return O.monthly(c)
    finally:
        O.PAR[K25]['value'], O.PAR[KCAP]['value'] = old25, oldcap



# casos em que o pagamento do mes da simulacao NAO se repete nos meses anteriores (bonus pontual): consumo do ano
# calculado sobre o caso sem o bonus (premissa do CCG: mesmo salario desde 1/1).
PRIOR = {'RC05': {'nonsalary': 0}}  # RC07 = exemplo do Payslip (ago/2026, mesmo pagamento todo mes)


def ytd_months(c, prior_over=None):
    """jan..dez: se prior_over, os meses anteriores ao mes da simulacao usam o caso sem o bonus."""
    per = int(str(c.get('period', '2026-03'))[5:7])
    cp = dict(c, **prior_over) if prior_over else c
    used25 = usedcap = Dc(0); months = []
    for m in range(1, 13):
        cc = c if (not prior_over or m == per) else cp
        r = run_with_room(cc, A790 - used25, A1340 - usedcap)
        used25 += Dc(str(r['ret_exenta_25'])); usedcap += Dc(str(r['ret_beneficios_aplicados']))
        months.append({'mes': m, 'exenta_25': r['ret_exenta_25'], 'beneficios': r['ret_beneficios_aplicados'],
                       'retencao': r['ret_valor_retener_raw'], 'consumo_25_ate_o_mes_anterior': O.f2(used25 - Dc(str(r['ret_exenta_25'])))})
    return months

cases = [c for c in load('cases.json') + load('cases_v2r4.json') + load('cases_research.json') if c.get('module') == 'monthly' and not c.get('pending')
         and c.get('retention', True)]
out = {'premissa': 'mesmo pagamento mensal desde 1/1/2026, sem outra renda isenta nem deducao; prima de servicos nao incluida no consumo',
       'casos_rodados': len(cases), 'afetados': [], 'nao_afetados': []}
for c in cases:
    o = O.monthly(c)
    if 'ret_exenta_25' not in o:
        continue
    base1 = Dc(str(o['ret_subtotal_tras_incrngo']))
    e25, cap = Dc(str(o['ret_exenta_25'])), Dc(str(o['ret_cap_40_1340']))
    m25 = A790 / 12; mcap = A1340 / 12
    hit25 = abs(e25 - Dc(str(O.f2(m25)))) < Dc('0.01')
    hitcap = abs(cap - Dc(str(O.f2(mcap)))) < Dc('0.01') and Dc(str(o['ret_beneficios_aplicados'])) >= cap - Dc('0.01')
    if not (hit25 or hitcap):
        out['nao_afetados'].append(c['id']); continue
    months = ytd_months(c, PRIOR.get(c['id']))
    t12 = Dc(str(o['ret_valor_retener_raw']))
    tytd = sum(Dc(str(x['retencao'])) for x in months)
    first = next((x['mes'] for x in months if Dc(str(x['exenta_25'])) < Dc(str(months[0]['exenta_25'])) - Dc('0.01')), None)
    per = int(str(c.get('period', '2026-03'))[5:7])
    out['afetados'].append({'id': c['id'], 'nome': c.get('name'), 'mes_da_simulacao': per,
                            'retencao_no_mes_da_simulacao_ytd': months[per - 1]['retencao'],
                            'exenta25_no_mes_da_simulacao_ytd': months[per - 1]['exenta_25'], 'limite_1_12': ('790/12 ' if hit25 else '') + ('1340/12' if hitcap else ''),
                            'retencao_mensal_1_12': O.f2(t12), 'retencao_mes1_ytd': months[0]['retencao'],
                            'diferenca_mes1': O.f2(Dc(str(months[0]['retencao'])) - t12),
                            'mes_em_que_o_teto_anual_comeca_a_limitar': first,
                            'anual_1_12': O.f2(t12 * 12), 'anual_ytd': O.f2(tytd), 'meses': months})
# exemplos do CCG (premissa escrita no CCG: mesmo salario desde 1/1/2026; bonus so no mes do exemplo)
CCG = [
 ('T105 (Ex. 4, set/2026: 8.000.000 + bonus 20.000.000 com pacto)', {'id': 'T105', 'module': 'monthly', 'salary': 8000000, 'nonsalary': 20000000, 'period': '2026-09'}, {'nonsalary': 0}),
 ('T180 (out/2026: 6.000.000 + bonus habitual 12.000.000)', {'id': 'T180', 'module': 'monthly', 'salary': 6000000, 'commission': 12000000, 'period': '2026-10'}, {'commission': 0}),
 ('T183 C3 (mesmo caso com pacto nao salarial)', {'id': 'T183', 'module': 'monthly', 'salary': 6000000, 'nonsalary': 12000000, 'period': '2026-10'}, {'nonsalary': 0}),
 ('T239 (integral 25.000.000, mes de jan a jul)', {'id': 'T239', 'module': 'monthly', 'salary': 25000000, 'integral': True, 'period': '2026-07'}, None),
]
out['exemplos_ccg'] = []
for nm, c, pr in CCG:
    o = O.monthly(c); ms = ytd_months(c, pr); per = int(c['period'][5:7])
    out['exemplos_ccg'].append({'exemplo': nm, 'retencao_1_12': o['ret_valor_retener_raw'], 'exenta25_ytd': ms[per - 1]['exenta_25'],
                                'consumo_25_ate_o_mes_anterior': ms[per - 1]['consumo_25_ate_o_mes_anterior'],
                                'retencao_ytd': ms[per - 1]['retencao'], 'meses': ms})
    print(f"CCG {nm}: 1/12={o['ret_valor_retener_raw']:,.2f}  YTD={ms[per-1]['retencao']:,.2f}  (25% isento {ms[per-1]['exenta_25']:,.2f}; consumo antes {ms[per-1]['consumo_25_ate_o_mes_anterior']:,.2f})")
json.dump(out, open(os.path.join(HERE, '..', 'oracle-r5-ytd.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('casos monthly com retencao:', len(cases), '| afetados pelo 1/12:', len(out['afetados']))
for a in out['afetados']:
    print(f"{a['id']:6} {a['limite_1_12']:16} 1/12={a['retencao_mensal_1_12']:>14,.2f}  YTD mes1={a['retencao_mes1_ytd']:>14,.2f}  "
          f"mes sim={a['mes_da_simulacao']} YTD nele={a['retencao_no_mes_da_simulacao_ytd']:>14,.2f}  teto anual limita a partir do mes {a['mes_em_que_o_teto_anual_comeca_a_limitar']}  anual 1/12={a['anual_1_12']:>15,.2f} YTD={a['anual_ytd']:>15,.2f}")

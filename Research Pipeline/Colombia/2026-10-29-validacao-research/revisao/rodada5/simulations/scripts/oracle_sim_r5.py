# -*- coding: utf-8 -*-
"""Rodada 5 (2026-11-02), A-1 nas simulacoes: valores do oraculo (oracle/oracle_v2.py, NAO alterado) para as linhas de
retencao de cada caso mensal, com os tetos de 790 e 1.340 UVT ANUAIS controlados pelo acumulado do ano (mesmo metodo de
revisao/rodada5/scripts/oracle_r5_ytd.py: o limite mensal lido do parametro e trocado, so durante a chamada, pelo saldo
anual nao usado). Premissa: mesmo pagamento mensal desde 1/1/2026 (RC05/T105: meses anteriores so com o salario).
Grava ../oracle-sim-r5.json com, por caso, as linhas do oraculo no 1/12 (antes) e no acumulado (depois), no mes da simulacao.
Uso: python -I oracle_sim_r5.py
"""
import os, sys, json, importlib.util
from decimal import Decimal as Dc
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
VAL = os.path.normpath(os.path.join(HERE, '..', '..', '..', '..'))
ORA = os.path.join(VAL, 'oracle')
spec = importlib.util.spec_from_file_location('oracle_v2', os.path.join(ORA, 'oracle_v2.py'))
O = importlib.util.module_from_spec(spec); spec.loader.exec_module(O)
UVT = O.UVT
A790, A1340 = Dc(790) * UVT, Dc(1340) * UVT
K25, KCAP = 'RET_EXENTA25_UVT_ANO', 'RET_CAP_UVT_ANO'
KEYS = ['ret_exenta_afc', 'ret_exenta_25', 'ret_cap_40_1340', 'ret_beneficios_aplicados', 'ret_base_gravable',
        'ret_base_uvt', 'ret_impuesto_uvt', 'ret_valor_retener', 'ret_valor_retener_raw', 'neto_aprox_raw']
PRIOR = {'RC05': {'nonsalary': 0}}


def load(fn):
    c = json.load(open(os.path.join(ORA, fn), encoding='utf-8'))
    return c['cases'] if isinstance(c, dict) else c


def run_with_room(c, room25, roomcap):
    old25, oldcap = O.PAR[K25]['value'], O.PAR[KCAP]['value']
    try:
        O.PAR[K25]['value'] = str(max(room25, Dc(0)) * 12 / UVT)
        O.PAR[KCAP]['value'] = str(max(roomcap, Dc(0)) * 12 / UVT)
        return O.monthly(c)
    finally:
        O.PAR[K25]['value'], O.PAR[KCAP]['value'] = old25, oldcap


def ytd_at(c, prior_over=None):
    per = int(str(c.get('period', '2026-03'))[5:7])
    cp = dict(c, **prior_over) if prior_over else c
    used25 = usedcap = Dc(0)
    for m in range(1, per + 1):
        cc = c if m == per else cp
        r = run_with_room(cc, A790 - used25, A1340 - usedcap)
        if m < per:
            used25 += Dc(str(r['ret_exenta_25'])); usedcap += Dc(str(r['ret_beneficios_aplicados']))
    return r, O.f2(used25), O.f2(usedcap)


cases = [c for c in load('cases.json') + load('cases_v2r4.json') + load('cases_research.json')
         if c.get('module') == 'monthly' and not c.get('pending')]
out = {'premissa': 'mesmo pagamento mensal desde 1/1/2026, sem outra renda isenta nem deducao (RC05: meses anteriores so com o salario)',
       'casos': {}}
for c in cases:
    o12 = O.monthly(c)
    if 'ret_exenta_25' not in o12:
        continue
    oy, u25, ucap = ytd_at(c, PRIOR.get(c['id']))
    out['casos'][c['id']] = {'periodo': c.get('period', '2026-03'), 'antes_1_12': {k: o12.get(k) for k in KEYS},
                             'depois_acumulado': {k: oy.get(k) for k in KEYS},
                             'consumo_25_ate_mes_anterior': u25, 'consumo_1340_ate_mes_anterior': ucap,
                             'mudou': any(o12.get(k) != oy.get(k) for k in KEYS)}
json.dump(out, open(os.path.join(HERE, '..', 'oracle-sim-r5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
ch = [k for k, v in out['casos'].items() if v['mudou']]
print('casos mensais com retencao:', len(out['casos']), '| mudaram:', len(ch), ch)
for k in ch:
    v = out['casos'][k]
    print(f"{k:6} ret 1/12={v['antes_1_12']['ret_valor_retener_raw']:>14,.2f}  acumulado={v['depois_acumulado']['ret_valor_retener_raw']:>14,.2f}  consumo25={v['consumo_25_ate_mes_anterior']:>14,.2f}")

# -*- coding: utf-8 -*-
"""Conferencia das simulacoes R5 depois do recalculo no Excel: erros de formula, contagem OK/DIFF/n-a, tabela
caso | antes | depois | oraculo | diferenca para as linhas de retencao, RC05/T105, texto da formula = formula, sem 1/12.
Uso: python -I check_sim_r5.py  -> imprime e grava ../check-sim-r5.json"""
import os, re, sys, json, collections
import openpyxl
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.normpath(os.path.join(HERE, '..'))
OLD = os.path.normpath(os.path.join(SIM, '..', '..', '..', 'final', 'simulations'))
ORS = json.load(open(os.path.join(SIM, 'oracle-sim-r5.json'), encoding='utf-8'))['casos']
ERR = ('#REF', '#VAL', '#NAM', '#DIV', '#N/A', '#NUM', '#NUL')
res = {}


def scan(path, chk_col):
    wv = openpyxl.load_workbook(path, data_only=True); wf = openpyxl.load_workbook(path)
    errs, cnt, diffs, txt_mismatch, still12 = [], collections.Counter(), [], [], []
    for ws in wv.worksheets:
        fs = wf[ws.title]
        for row in ws.iter_rows():
            for c in row:
                if isinstance(c.value, str) and c.value.startswith(ERR):
                    errs.append((ws.title, c.coordinate, c.value))
        for r in range(1, ws.max_row + 1):
            k = ws.cell(r, chk_col).value
            if k in ('OK', 'DIFF', 'n/a'):
                cnt[k] += 1
                if k == 'DIFF':
                    diffs.append((ws.title, r, ws.cell(r, 2).value))
        for row in fs.iter_rows():
            for c in row:
                if isinstance(c.value, str) and re.search(r'p_RET_(E25|CAP|AFC)_UVT\*p_UVT/12', c.value):
                    still12.append((ws.title, c.coordinate))
    return wv, wf, errs, cnt, diffs, still12


ROWS = [('Exempt labour income 25%', 'ret_exenta_25'), ('Reliefs applied', 'ret_beneficios_aplicados'),
        ('TAXABLE BASE', 'ret_base_gravable'), ('WITHHOLDING TAX (Procedure 1)', 'ret_valor_retener')]


def find(ws, prefix, lo=1):
    for r in range(lo, ws.max_row + 1):
        v = ws.cell(r, 2).value
        if isinstance(v, str) and v.startswith(prefix):
            return r


def table(wv_new, wv_old, sheets, col_res, col_or):
    out = []
    for title, cid in sheets:
        n, o = wv_new[title], wv_old[title]
        r = find(n, 'Voluntary pension / AFC exempt')
        line = {'aba': title, 'caso': cid}
        for lab, key in ROWS:
            rr = find(n, lab, r)
            line[key] = {'antes': o.cell(rr, col_res).value, 'depois': n.cell(rr, col_res).value,
                         'oraculo': ORS[cid]['depois_acumulado'][key], 'oraculo_celula': n.cell(rr, col_or).value}
            line[key]['dif'] = round(line[key]['depois'] - line[key]['oraculo'], 6)
        rw = find(n, 'Tax in UVT', r)
        line['retencao_bruta'] = round(n.cell(rw, col_res).value * 52374, 2)
        out.append(line)
    return out


# CO_Simulation
p_new = os.path.join(SIM, 'CO_Simulation_2026_11_02_V1.1.xlsx')
wv, wf, errs, cnt, diffs, still = scan(p_new, 11)
wold = openpyxl.load_workbook(os.path.join(OLD, 'CO_Simulation_2026_10_30_V1.0.xlsx'), data_only=True)
_, _, _, cnt_old, _, _ = scan(os.path.join(OLD, 'CO_Simulation_2026_10_30_V1.0.xlsx'), 11)
txt = []
for ws in wf.worksheets:
    if re.match(r'^[CRHD]\d\d ', ws.title):
        r = find(ws, 'Voluntary pension / AFC exempt')
        for rr in (r, r + 1, r + 2):
            if ws.cell(rr, 5).value != ws.cell(rr, 6).value:
                txt.append((ws.title, rr))
mon = [(ws.title, ws.title.split()[0]) for ws in wv.worksheets if re.match(r'^[CRHD]\d\d ', ws.title)]
changed = []
for title, cid in mon:
    o, n = wold[title], wv[title]
    rw = find(n, 'WITHHOLDING TAX (Procedure 1)')
    if o.cell(rw, 6).value != n.cell(rw, 6).value:
        changed.append((title, cid))
tab_co = table(wv, wold, changed, 6, 9)
res['co'] = {'erros': errs, 'contagem_antes': dict(cnt_old), 'contagem_depois': dict(cnt), 'diffs': diffs, 'ainda_1_12': still,
             'texto_formula_diferente': txt, 'abas_que_mudaram': [c for _, c in changed], 'tabela': tab_co}

# Tax Simulations
p_new = os.path.join(SIM, 'Tax Simulations - Colombia.xlsx')
wv, wf, errs, cnt, diffs, still = scan(p_new, 8)
wold = openpyxl.load_workbook(os.path.join(OLD, 'Tax Simulations - Colombia.xlsx'), data_only=True)
_, _, _, cnt_old, _, _ = scan(os.path.join(OLD, 'Tax Simulations - Colombia.xlsx'), 8)
txt = []
for ws in wf.worksheets:
    for rr in (12, 13, 50, 51, 52):
        e, i = ws.cell(rr, 5).value, ws.cell(rr, 9).value
        if isinstance(e, str) and e.startswith('=') and 'p_RET' in e and e != i:
            txt.append((ws.title, rr))
dep = [(ws.title, ws['C4'].value.replace('EE-CO-', '')) for ws in wv.worksheets if wf[ws.title]['E51'].value and 'E$97' in str(wf[ws.title]['E51'].value)]
changed = [(t, c) for t, c in dep if wold[t]['E58'].value != wv[t]['E58'].value]
tab_tax = table(wv, wold, changed, 5, 6)
pb = wv['SERVICE BONUS SEPARATE READ']
res['tax'] = {'erros': errs, 'contagem_antes': dict(cnt_old), 'contagem_depois': dict(cnt), 'diffs': diffs, 'ainda_1_12': still,
              'texto_formula_diferente': txt, 'abas_que_mudaram': [c for _, c in changed], 'tabela': tab_tax,
              'PB': {'e25': pb['E12'].value, 'cap': pb['E13'].value, 'retencao': pb['E17'].value}}
rc = wv['NON-SALARY BONUS']
res['tax']['RC05'] = {'consumo_25_jan_ago': rc['E96'].value, 'saldo_790': rc['E97'].value, 'isento_25': rc['E51'].value,
                      'base': rc['E55'].value, 'imposto_uvt': rc['E57'].value, 'retencao_bruta': round(rc['E57'].value * 52374, 2),
                      'retencao_arredondada': rc['E58'].value}

# Law vs Provider
p_new = os.path.join(SIM, 'Colombia Simulations - Law vs Provider.xlsx')
wv, wf, errs, cnt, diffs, still = scan(p_new, 11)
res['lvp'] = {'erros': errs, 'F1': wv['PROVIDER RESULT']['F1'].value}

# AFC: o /12 do oraculo nunca limitou (senao o anual mudaria o valor)
afc_bind = [k for k, v in ORS.items() if v['antes_1_12']['ret_exenta_afc'] and abs(v['antes_1_12']['ret_exenta_afc'] - 3800 * 52374 / 12) < 0.01]
res['afc_limitado_pelo_1_12'] = afc_bind
json.dump(res, open(os.path.join(SIM, 'check-sim-r5.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
for k in ('co', 'tax'):
    d = res[k]
    print(k, 'erros', len(d['erros']), 'antes', d['contagem_antes'], 'depois', d['contagem_depois'], 'DIFF', d['diffs'][:5], '1/12 restante', d['ainda_1_12'][:5], 'texto!=formula', d['texto_formula_diferente'][:5])
    print('  abas que mudaram:', d['abas_que_mudaram'])
    for t in d['tabela']:
        w = t['ret_valor_retener']; e = t['ret_exenta_25']
        print(f"  {t['caso']:5} ret antes={w['antes']:>12,.0f} depois={w['depois']:>12,.0f} oraculo={w['oraculo']:>12,.0f} dif={w['dif']}  | 25% depois={e['depois']:>14,.2f} or={e['oraculo']:>14,.2f} dif={e['dif']} | base dif={t['ret_base_gravable']['dif']} relief dif={t['ret_beneficios_aplicados']['dif']} | bruta={t['retencao_bruta']:,.2f}")
print('PB', res['tax']['PB']); print('RC05', res['tax']['RC05']); print('LvP', res['lvp']); print('AFC limitado 1/12:', afc_bind)

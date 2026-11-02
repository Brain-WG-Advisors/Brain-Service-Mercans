# -*- coding: utf-8 -*-
"""Rodada 5 (2026-11-02), decisao A-1 nas copias das simulacoes (revisao/rodada5/simulations/):
tetos anuais de 790 UVT (ET 206 num. 10), 1.340 UVT (ET 336 num. 3; DUR 1.2.4.1.6 par. 3) e 3.800 UVT (AFC/AVP,
ET 126-1/126-4; DUR 1.2.1.22.43) controlados pelo ACUMULADO do ano, sem 1/12.
Fonte: CE Seccion Cuarta rad. 24047 (28/10/2021) anulou o limite mensal; Decreto 2231/2023 art. 9 ("UVT anuales").
- Formulas continuam formulas: limite = min(% do mes, saldo anual = teto anual - consumo jan..mes anterior).
- Consumo: bloco explicito na aba, premissa 'mesmo pagamento desde 1/1/2026' (CCG); Tax/NON-SALARY BONUS: meses
  anteriores so com o salario (entrada 'Monthly salary in each earlier month').
- Valores do oraculo (coluna I / F) trocados pelos de ../oracle-sim-r5.json (oracle_v2 mes a mes com o saldo anual).
Uso: python -I apply_sim_r5.py   (edita as copias no lugar; rodar sobre copias limpas de final/simulations)
"""
import os, re, sys, json
from copy import copy
import openpyxl
from openpyxl.styles import Alignment
sys.stdout.reconfigure(encoding='utf-8')
HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.normpath(os.path.join(HERE, '..'))
F_CO = os.path.join(SIM, 'CO_Simulation_2026_11_02_V1.1.xlsx')
F_TAX = os.path.join(SIM, 'Tax Simulations - Colombia.xlsx')
F_LVP = os.path.join(SIM, 'Colombia Simulations - Law vs Provider.xlsx')
ORS = json.load(open(os.path.join(SIM, 'oracle-sim-r5.json'), encoding='utf-8'))['casos']
LOG = {'co': [], 'tax': [], 'lvp': []}

SRC = ('CE Seccion Cuarta exp. 24047 of 28 Oct 2021 (monthly limit annulled); Decree 2231 of 2023 art. 9 ("UVT anuales"); '
       'Decree 1625 of 2016 arts. 1.2.4.1.6 par. 3 and 1.2.1.22.43')
NOTE25 = 'Tax Code art. 206 num. 10 (Law 2277 of 2022 art. 2); 790 UVT a year controlled year-to-date (annual room left), not 1/12: ' + SRC
NOTECAP = 'Tax Code art. 336 num. 3; Decree 1625 of 2016 art. 1.2.4.1.6 par. 3 (Decree 2231 of 2023 art. 9); 1,340 UVT a year controlled year-to-date (annual room left), not 1/12: CE S4 exp. 24047/2021'
NOTEAFC = 'Tax Code arts. 126-1 and 126-4; Decree 1625 of 2016 art. 1.2.1.22.43; 3,800 UVT a year controlled year-to-date (annual room left), not 1/12'
H_AFC = 'min(paid, 30% x income, 3,800 UVT a year - used Jan to previous month)'
H_E25 = 'min(25% x (net income - deductions - other exempt), 790 UVT a year - 25% used Jan to previous month); oracle_v2 run month by month with the annual room (rodada5 oracle_sim_r5.py)'
H_CAP = 'min(40% x net income, 1,340 UVT a year - reliefs applied Jan to previous month); oracle_v2 run month by month with the annual room (rodada5 oracle_sim_r5.py)'
KEYMAP = [('Voluntary pension / AFC exempt', 'ret_exenta_afc'), ('Exempt labour income 25%', 'ret_exenta_25'),
          ('Cap on deductions', 'ret_cap_40_1340'), ('Reliefs applied', 'ret_beneficios_aplicados'),
          ('TAXABLE BASE', 'ret_base_gravable'), ('Taxable base in UVT', 'ret_base_uvt'), ('Tax in UVT', 'ret_impuesto_uvt'),
          ('WITHHOLDING TAX (Procedure 1)', 'ret_valor_retener'), ('Net pay before PILA rounding', 'neto_aprox_raw')]


def style_from(dst, src):
    dst.font = copy(src.font); dst.fill = copy(src.fill); dst.border = copy(src.border)
    dst.alignment = copy(src.alignment); dst.number_format = src.number_format; dst.protection = copy(src.protection)


def find_row(ws, col, prefix, lo=1, hi=None):
    for r in range(lo, (hi or ws.max_row) + 1):
        v = ws.cell(r, col).value
        if isinstance(v, str) and v.startswith(prefix):
            return r
    return None


def prior_reliefs(n, x, D, c40, A):
    """soma das reliefs aplicadas jan..mes anterior (40% por mes), com o 25% de cada mes limitado ao saldo de 790 UVT."""
    q = f'INT({A}/{x})'
    return (f'IF({x}<=0,{n}*MIN({D},{c40}),IF({n}<={q},{n}*MIN({D}+{x},{c40}),'
            f'{q}*MIN({D}+{x},{c40})+MIN({D}+{A}-{q}*{x},{c40})+({n}-{q}-1)*MIN({D},{c40})))')


def set_oracle(ws, col_label, col_or, cid, lo, hi, tag):
    """troca o valor do oraculo nas linhas de retencao do caso (so se mudou) e confere o 'antes'."""
    o = ORS.get(cid)
    if not o:
        return 0
    n = 0
    for lab, key in KEYMAP:
        r = find_row(ws, col_label, lab, lo, hi)
        if r is None:
            continue
        cell = ws.cell(r, col_or)
        old = cell.value
        a, d = o['antes_1_12'][key], o['depois_acumulado'][key]
        if isinstance(old, (int, float)):
            assert abs(old - a) <= 0.011, (tag, cid, lab, old, a)
        if a != d:
            cell.value = d
            n += 1
            LOG[tag].append({'aba': ws.title, 'caso': cid, 'linha': lab, 'celula': cell.coordinate, 'antes': old, 'depois': d})
    return n


# ----------------------------------------------------------------------------------------------- CO_Simulation
wb = openpyxl.load_workbook(F_CO)
monthly = [ws for ws in wb.worksheets if re.match(r'^[CRHD]\d\d ', ws.title)]
first = None
for ws in monthly:
    cid = ws.title.split()[0]
    rA = find_row(ws, 2, 'Voluntary pension / AFC exempt'); rE = rA + 1; rC = rA + 2
    assert ws.cell(rE, 2).value.startswith('Exempt labour income 25%') and ws.cell(rC, 2).value.startswith('Cap on deductions'), ws.title
    fa, fe, fc = ws.cell(rA, 6).value, ws.cell(rE, 6).value, ws.cell(rC, 6).value
    m = re.fullmatch(r'=MIN\(\$D\$23,MIN\(p_RET_AFC_PCT\*\$F\$(\d+),p_RET_AFC_UVT\*p_UVT/12\)\)', fa); inc = m.group(1)
    m = re.fullmatch(r'=MIN\(p_RET_E25_PCT\*MAX\(\$F\$(\d+)-\$F\$(\d+)-\$F\$(\d+)-\$F\$(\d+)-\$F\$(\d+),0\),p_RET_E25_UVT\*p_UVT/12\)', fe)
    net, d1, d2, d3, afc = m.groups(); assert int(afc) == rA
    m = re.fullmatch(r'=MIN\(p_RET_CAP_PCT\*\$F\$(\d+),p_RET_CAP_UVT\*p_UVT/12\)', fc); assert m.group(1) == net
    r0 = int(inc)  # bloco em R:T a partir da linha 'Taxable labour payments of the month'
    S = lambda k: f'$S${r0 + k}'
    lab_src, val_src, hdr_src = ws.cell(r0, 2), ws.cell(rE, 6), ws.cell(r0 - 2, 1)
    A790, A1340, A3800 = 'p_RET_E25_UVT*p_UVT', 'p_RET_CAP_UVT*p_UVT', 'p_RET_AFC_UVT*p_UVT'
    Dm = f'($F${d1}+$F${d2}+$F${d3}+$F${afc})'
    rows = [
        ('YEAR-TO-DATE ANNUAL CAPS (decision A-1, 2 Nov 2026)', None, SRC),
        ('Months of 2026 before this pay period', '=MONTH($D$9)-1', 'Pay period date in D9'),
        ('Premise: same pay as this month in every earlier month since 1 Jan 2026 (CCG premise); no other employer, exempt income or deduction earlier in the year', None, 'Consumption Jan to previous month is derived from this premise (no payroll history in this workbook)'),
        ('Voluntary pension / AFC used Jan to previous month (3,800 UVT a year)', f'=MIN({S(1)}*MIN($D$23,p_RET_AFC_PCT*$F${inc}),{A3800})', 'Tax Code arts. 126-1 and 126-4; Decree 1625 of 2016 art. 1.2.1.22.43'),
        ('Voluntary pension / AFC annual room left', f'={A3800}-{S(3)}', 'Feeds the AFC line (column F)'),
        ('25% exempt of the month before the annual cap', f'=p_RET_E25_PCT*MAX($F${net}-$F${d1}-$F${d2}-$F${d3}-$F${afc},0)', 'Same residue as the 25% line'),
        ('25% exempt used Jan to previous month (790 UVT a year)', f'=MIN({S(1)}*{S(5)},{A790})', 'Tax Code art. 206 num. 10'),
        ('790 UVT annual room left', f'={A790}-{S(6)}', 'Feeds the 25% line (column F)'),
        ('Reliefs applied Jan to previous month (40% each month; 1,340 UVT a year)',
         '=MIN(' + prior_reliefs(S(1), S(5), Dm, f'p_RET_CAP_PCT*$F${net}', A790) + f',{A1340})',
         'Each earlier month: min(deductions + AFC + 25% of that month, 40% of net income); 25% of each month within the 790 UVT room'),
        ('1,340 UVT annual room left', f'={A1340}-{S(8)}', 'Feeds the cap line (column F)'),
    ]
    for k, (lab, f, note) in enumerate(rows):
        r = r0 + k
        c = ws.cell(r, 18, lab); style_from(c, hdr_src if k == 0 else lab_src)
        if k == 2:
            al = lab_src.alignment
            c.alignment = Alignment(horizontal=al.horizontal, vertical=al.vertical, wrap_text=True)
        if f:
            v = ws.cell(r, 19, f); style_from(v, val_src)
        t = ws.cell(r, 20, note); style_from(t, lab_src)
        if k == 0:
            style_from(ws.cell(r, 19), hdr_src); style_from(t, hdr_src)
    ws.column_dimensions['R'].width = 62; ws.column_dimensions['S'].width = 18; ws.column_dimensions['T'].width = 70
    newA = f'=MIN($D$23,MIN(p_RET_AFC_PCT*$F${inc},{S(4)}))'
    newE = f'=MIN(p_RET_E25_PCT*MAX($F${net}-$F${d1}-$F${d2}-$F${d3}-$F${afc},0),{S(7)})'
    newC = f'=MIN(p_RET_CAP_PCT*$F${net},{S(9)})'
    for r, f, h, note in ((rA, newA, H_AFC, NOTEAFC), (rE, newE, H_E25, NOTE25), (rC, newC, H_CAP, NOTECAP)):
        ws.cell(r, 5).value = f   # coluna E = texto da formula (string)
        ws.cell(r, 5).data_type = 's'
        ws.cell(r, 6).value = f
        ws.cell(r, 8).value = h
        ws.cell(r, 12).value = note
    n = set_oracle(ws, 2, 9, cid, rA, ws.max_row, 'co')
    if cid == 'R07':
        ws['B1'].value = ws['B1'].value + ' - with the annual caps controlled year-to-date the 40% limit binds in March; the 1,340 UVT annual cap binds from May (same pay since 1 Jan)'
    if cid == 'R08':
        ws['B1'].value = ws['B1'].value + ' - with the 790 UVT controlled year-to-date the cap does not bind in March; it binds from October (same pay since 1 Jan)'
    if first is None:
        first = (ws.title, rA, newA, newE, newC)

# Parameters
ws = wb['Parameters']
for r, txt in ((50, 'Voluntary pension / AFC savings exempt, annual maximum (controlled year-to-date: annual room left = 3,800 UVT - used Jan to previous month; no 1/12)'),
               (52, 'Exempt labour income, annual maximum (controlled year-to-date: annual room left = 790 UVT - used Jan to previous month; no 1/12)'),
               (54, 'Deductions + exempt income cap, annual (controlled year-to-date: annual room left = 1,340 UVT - applied Jan to previous month; no 1/12)')):
    assert ws.cell(r, 2).value.startswith(('Voluntary', 'Exempt', 'Deductions')), r
    ws.cell(r, 2).value = txt
ws['E50'].value = 'Tax Code arts. 126-1 and 126-4; Decree 1625 of 2016 art. 1.2.1.22.43 (annual)'
ws['E52'].value = 'Tax Code art. 206 num. 10 (Law 2277 of 2022 art. 2); CE Seccion Cuarta exp. 24047 of 28 Oct 2021 (monthly limit annulled); Decree 2231 of 2023 art. 9'
ws['E54'].value = 'Tax Code art. 336 num. 3 (Law 2277 of 2022 art. 7); Decree 1625 of 2016 art. 1.2.4.1.6 par. 3 (Decree 2231 of 2023 art. 9, "UVT anuales"); CE S4 exp. 24047/2021'

# Checks index (nota da linha) e Formula comparison
ws = wb['Checks index']
for r in range(2, ws.max_row + 1):
    b = ws.cell(r, 2).value
    if isinstance(b, str):
        if b.startswith('Exempt labour income 25%'): ws.cell(r, 6).value = NOTE25
        elif b.startswith('Cap on deductions'): ws.cell(r, 6).value = NOTECAP
        elif b.startswith('Voluntary pension / AFC exempt'): ws.cell(r, 6).value = NOTEAFC
ws = wb['Formula comparison']
_, rA, newA, newE, newC = first
for r, words, f, h in ((26, 'Paid, max 30% of income and the 3,800 UVT annual room left (year-to-date)', newA, H_AFC),
                       (27, '25% of the residue after all other reliefs, max the 790 UVT annual room left (year-to-date)', newE, H_E25),
                       (28, '40% of net income, max the 1,340 UVT annual room left (year-to-date)', newC, H_CAP)):
    ws.cell(r, 2).value = words; ws.cell(r, 3).value = f; ws.cell(r, 3).data_type = 's'; ws.cell(r, 6).value = h

# Read me
ws = wb['Read me']
ws['A1'].value = 'CO_Simulation_2026_11_02_V1.1 - Read me'
ws['B5'].value = ws['B5'].value.replace('40% / 1,340 UVT cap kept in the monthly withholding',
    '40% / 1,340 UVT cap kept in the monthly withholding; the annual caps of 790 UVT (25% exempt), 1,340 UVT (40% cap) and 3,800 UVT (voluntary pension / AFC) are controlled by the year-to-date amount (annual room left = annual cap - amount used Jan to previous month), not by 1/12 (decision A-1 of 2 Nov 2026; ' + SRC + '). Premise for the amount used: same pay as the simulated month since 1 Jan 2026 (block YEAR-TO-DATE ANNUAL CAPS, columns R-T of each monthly sheet)')
assert 'year-to-date' in ws['B5'].value
ws['B9'].value = ("Column 'Oracle result' holds the value produced by oracle_v2.py (30 Oct 2026) from params.json, as a value (no formula). "
                  "Withholding lines from 2 Nov 2026 (V1.1): oracle_v2 run month by month from January with the annual room left (code unchanged; revisao/rodada5/simulations/scripts/oracle_sim_r5.py). "
                  "The oracle is an independent re-implementation from the statutes; it was not derived from the research artifacts.")
ws['B14'].value = 'Recalculated with Microsoft Excel (CalculateFull) before delivery; 0 formula errors. V1.1 (2 Nov 2026): annual caps year-to-date (decision A-1); recalculated and checked against the oracle (revisao/rodada5/simulations/CONFERENCIA-SIMULACOES-R5.md).'
wb.save(F_CO)
print('CO_Simulation: abas mensais', len(monthly), '| celulas do oraculo trocadas', len(LOG['co']))

# ----------------------------------------------------------------------------------------------- Tax Simulations
wb = openpyxl.load_workbook(F_TAX)
dep = [ws for ws in wb.worksheets if isinstance(ws['E51'].value, str) and 'p_RET_E25_UVT' in ws['E51'].value]
assert len(dep) == 14, len(dep)
FSP = ('IF($E$90/p_SMMLV>=p_FSP_MIN,p_FSP_SOL+p_FSP_SUB+IF($E$90/p_SMMLV>20,p_FSP_B5,IF($E$90/p_SMMLV>19,p_FSP_B4,'
       'IF($E$90/p_SMMLV>18,p_FSP_B3,IF($E$90/p_SMMLV>17,p_FSP_B2,IF($E$90/p_SMMLV>=16,p_FSP_B1,0))))),0)')
for ws in dep:
    cid = ws['C4'].value.replace('EE-CO-', '')
    assert ws['E50'].value == '=MIN($E$83,MIN(p_RET_AFC_PCT*$E$44,p_RET_AFC_UVT*p_UVT/12))', ws.title
    assert ws['E51'].value == '=MIN(p_RET_E25_PCT*MAX($E$46-$E$47-$E$48-$E$49-$E$50,0),p_RET_E25_UVT*p_UVT/12)', ws.title
    assert ws['E52'].value == '=MIN(p_RET_CAP_PCT*$E$46,p_RET_CAP_UVT*p_UVT/12)', ws.title
    assert all(ws.cell(r, c).value is None for r in range(86, 101) for c in range(1, 11)), ws.title
    hdr, lab, inp, res, note = ws['B67'], ws['B71'], ws['E71'], ws['E51'], ws['J72']
    A790, A1340, A3800 = 'p_RET_E25_UVT*p_UVT', 'p_RET_CAP_UVT*p_UVT', 'p_RET_AFC_UVT*p_UVT'
    prior_sal = 8000000 if cid == 'RC05' else None
    rows = [
        (86, '7.  YEAR-TO-DATE ANNUAL CAPS (decision A-1, 2 Nov 2026)', None, SRC, 'hdr'),
        (87, 'Months of 2026 before this pay period', '=MONTH($E$69)-1', 'Pay period date in E69', 'res'),
        (88, 'Monthly salary in each earlier month of 2026 (input; blank = same pay as this month since 1 Jan 2026)', prior_sal,
         ('Research worked example (CCG T105): salary 8,000,000 since 1 Jan, bonus only in September' if cid == 'RC05'
          else 'Premise: same pay as this month in every earlier month (CCG premise); no other employer, exempt income or deduction earlier in the year'), 'inp'),
        (89, 'Taxable labour payments in each earlier month', '=IF($E$88="",$E$44,$E$88+IF($E$88<=p_AUX_CAP*p_SMMLV,p_AUX,0))', 'Salary-only months: salary + transport allowance when due (not all-inclusive)', 'res'),
        (90, 'IBC in each earlier month', '=IF($E$88="",$E$26,ROUNDUP(ROUND(MIN(MAX($E$88,p_IBC_MIN*p_SMMLV),p_IBC_MAX*p_SMMLV),6),0))', 'Law 100 of 1993 art. 18', 'res'),
        (91, 'Net income in each earlier month', '=IF($E$88="",$E$46,$E$89-$E$90*(p_SAL_EE+p_PEN_TOT*(1-p_PEN_ER_SHARE)+' + FSP + '))', 'Tax Code arts. 55, 56 and 388 (mandatory employee contributions before PILA rounding)', 'res'),
        (92, 'Deductions + voluntary pension / AFC in each earlier month', '=IF($E$88="",$E$47+$E$48+$E$49+$E$50,IF($E$80="Yes",MIN(p_RET_DEP_PCT*$E$89,p_RET_DEP_UVT*p_UVT),0)+$E$48+$E$49+MIN($E$83,p_RET_AFC_PCT*$E$89))', 'Same deductions as this month', 'res'),
        (93, '25% exempt in each earlier month (before the annual cap)', '=p_RET_E25_PCT*MAX($E$91-$E$92,0)', 'Tax Code art. 206 num. 10', 'res'),
        (94, 'Voluntary pension / AFC used Jan to previous month (3,800 UVT a year)', f'=MIN($E$87*MIN($E$83,p_RET_AFC_PCT*$E$89),{A3800})', 'Tax Code arts. 126-1 and 126-4; Decree 1625 of 2016 art. 1.2.1.22.43', 'res'),
        (95, 'Voluntary pension / AFC annual room left', f'={A3800}-$E$94', 'Feeds line 58156', 'res'),
        (96, '25% exempt used Jan to previous month (790 UVT a year)', f'=MIN($E$87*$E$93,{A790})', 'Tax Code art. 206 num. 10', 'res'),
        (97, '790 UVT annual room left', f'={A790}-$E$96', 'Feeds line 58157', 'res'),
        (98, 'Reliefs applied Jan to previous month (40% each month; 1,340 UVT a year)',
         '=MIN(' + prior_reliefs('$E$87', '$E$93', '$E$92', 'p_RET_CAP_PCT*$E$91', A790) + f',{A1340})',
         'Each earlier month: min(deductions + AFC + 25% of that month, 40% of net income); Decree 1625 of 2016 art. 1.2.4.1.6 par. 3', 'res'),
        (99, '1,340 UVT annual room left', f'={A1340}-$E$98', 'Feeds line 58158', 'res'),
    ]
    for r, l, f, nt, kind in rows:
        c = ws.cell(r, 2, l); style_from(c, hdr if kind == 'hdr' else lab)
        if kind == 'hdr':
            for col in range(1, 11): style_from(ws.cell(r, col), hdr)
            ws.cell(r, 2).value = l
        else:
            v = ws.cell(r, 5, f); style_from(v, inp if kind == 'inp' else res)
            t = ws.cell(r, 10, nt); style_from(t, note)
    for r, f, nt, h in ((50, '=MIN($E$83,MIN(p_RET_AFC_PCT*$E$44,$E$95))', NOTEAFC, None),
                        (51, '=MIN(p_RET_E25_PCT*MAX($E$46-$E$47-$E$48-$E$49-$E$50,0),$E$97)', NOTE25, None),
                        (52, '=MIN(p_RET_CAP_PCT*$E$46,$E$99)', NOTECAP, None)):
        ws.cell(r, 5).value = f; ws.cell(r, 9).value = f; ws.cell(r, 9).data_type = 's'; ws.cell(r, 10).value = nt
    ws['N55'].value = 'Voluntary pension / AFC savings exempt, annual maximum (controlled year-to-date, no 1/12)'
    ws['N57'].value = 'Exempt labour income, annual maximum (controlled year-to-date, no 1/12)'
    ws['N59'].value = 'Deductions + exempt income cap, annual (controlled year-to-date, no 1/12)'
    ws['Q57'].value = 'Tax Code art. 206 num. 10 (Law 2277 of 2022 art. 2); CE Seccion Cuarta exp. 24047 of 28 Oct 2021; Decree 2231 of 2023 art. 9'
    if cid == 'R07':
        ws['B7'].value = ('Standard settings: full month, resident employee, withholding Procedure 1, 2026 parameters. Request: 1,340 UVT annual cap binding. '
                          'With the annual caps controlled year-to-date (decision A-1) the 40% limit binds in March; the 1,340 UVT annual cap binds from May (same pay since 1 Jan).')
    if cid == 'R08':
        ws['B7'].value = ('Standard settings: full month, resident employee, withholding Procedure 1, 2026 parameters. Request: 25% exempt income limited to 790 UVT a year. '
                          'Controlled year-to-date (decision A-1): the cap does not bind in March; it binds from October (same pay since 1 Jan).')
    set_oracle(ws, 2, 6, cid, 44, 66, 'tax')

# PB: leitura separada do premio de servicos
ws = wb['SERVICE BONUS SEPARATE READ']
assert ws['E12'].value == '=MIN(p_RET_E25_PCT*$E$11,p_RET_E25_UVT*p_UVT/12)' and ws['E13'].value == '=MIN(p_RET_CAP_PCT*$E$11,p_RET_CAP_UVT*p_UVT/12)'
assert ws['B21'].value is None and ws['B22'].value is None and ws['E21'].value is None
for r, l, nt in ((21, '25% exempt income already used in 2026 before this read', 'Premise: 0 - bonus read alone, as in the research worked example; in a real payroll = 25% exempt of the salary reads Jan to this month'),
                 (22, 'Reliefs already applied in 2026 before this read (1,340 UVT cap)', 'Premise: 0 - as above')):
    c = ws.cell(r, 2, l); style_from(c, ws['B20'])
    v = ws.cell(r, 5, 0); style_from(v, ws['E20'])
    t = ws.cell(r, 10, nt); style_from(t, ws['J11'])
for r, f in ((12, '=MIN(p_RET_E25_PCT*$E$11,p_RET_E25_UVT*p_UVT-$E$21)'), (13, '=MIN(p_RET_CAP_PCT*$E$11,p_RET_CAP_UVT*p_UVT-$E$22)')):
    ws.cell(r, 5).value = f; ws.cell(r, 9).value = f; ws.cell(r, 9).data_type = 's'
ws['J12'].value = 'Tax Code art. 206 num. 10; 790 UVT a year shared by the salary reads and the bonus read (annual room left; CE S4 exp. 24047/2021)'
ws['J13'].value = 'Decree 1625 of 2016 art. 1.2.4.1.6 par. 3 (1,340 UVT a year, annual room left)'
ws['B18'].value = ('Decision A-1 (2 Nov 2026): the 790 UVT and 1,340 UVT caps are annual and controlled year-to-date, so there is one cap for the year '
                   'shared by the salary reads and the bonus read; the bonus read takes the annual room left (inputs E21 and E22). The former open point on splitting a monthly 790/12 no longer exists.')

ws = wb['READ ME']
ws['B5'].value = ws['B5'].value.replace('annual caps applied monthly as 1/12 (operating convention, configurable)',
    'annual caps of 790 UVT, 1,340 UVT and 3,800 UVT (voluntary pension / AFC) controlled by the year-to-date amount (annual room left = annual cap - amount used Jan to previous month), not 1/12 (decision A-1 of 2 Nov 2026; ' + SRC + '); amount used from the block YEAR-TO-DATE ANNUAL CAPS (rows 86-99 of each depuration sheet: same pay since 1 Jan 2026, or the salary of the earlier months when entered)')
assert 'year-to-date' in ws['B5'].value
ws['B7'].value = ws['B7'].value + ' Withholding lines from 2 Nov 2026: oracle_v2 run month by month from January with the annual room left (code unchanged; revisao/rodada5/simulations/scripts/oracle_sim_r5.py).'
ws['B10'].value = ('(1) Split of the PILA-rounded total per fund between employee and employer; (2) closed on 2 Nov 2026: the 790 UVT cap is annual and controlled year-to-date, '
                   'so the salary reads and the service-bonus read share one annual room (decision A-1); (3) the 204-UVT test is applied to the monthly income (research premise). None changes a compared line.')
ws['B11'].value = ws['B11'].value.replace('CO_Simulation_2026_10_30_V1.0.xlsx', 'CO_Simulation_2026_11_02_V1.1.xlsx')
for w in wb.worksheets:
    if w['M3'].value and 'CO_Simulation_2026_10_30_V1.0' in str(w['M3'].value):
        w['M3'].value = w['M3'].value.replace('CO_Simulation_2026_10_30_V1.0.xlsx', 'CO_Simulation_2026_11_02_V1.1.xlsx')
wb.save(F_TAX)
print('Tax Simulations: abas de depuracao', len(dep), '| celulas do oraculo trocadas', len(LOG['tax']))

# ----------------------------------------------------------------------------------------------- Law vs Provider
wb = openpyxl.load_workbook(F_LVP)
ws = wb['LAW SIMULATION']
assert ws['B28'].value == 'Exempt labour income 25%' and ws['C28'].value == 'min(25% x residue, 790 UVT / 12)'
ws['C28'].value = 'min(25% x residue, 790 UVT / 12) - as run on 29-30 Oct 2026; NOT re-run with the annual cap (see note in PROVIDER RESULT J28)'
ws = wb['PROVIDER RESULT']
assert ws['B28'].value == 'Exempt labour income 25%'
ws['J28'].value = ('Tolerance: provider uses 3,447,953; oracle 790 x 52,374 / 12 = 3,447,955.00 (the earlier text said 3,447,955.50). '
                   'LIMITATION (decision A-1, 2 Nov 2026): the law caps the 25% at 790 UVT a year controlled year-to-date, not 790/12 a month. '
                   'Re-running this line needs each employee\'s 25% exempt used January-August 2026, which is not in these aggregates; '
                   'the counts of this line and of the dependent withholding lines are kept as computed with 1/12 and are not a verdict on the provider. '
                   'To close: re-run from the Test 4 inputs (outside this workbook, without client data here).')
ws = wb['READ ME']
ws['B8'].value = ws['B8'].value + (' Limitation (2 Nov 2026): the withholding lines were computed with the 790 UVT cap as 1/12 a month; under decision A-1 '
                                   '(annual cap controlled year-to-date) they need the January-August consumption per employee, not in these aggregates (PROVIDER RESULT J28).')
wb.save(F_LVP)
LOG['lvp'] = ['LAW SIMULATION C28', 'PROVIDER RESULT J28', 'READ ME B8']
json.dump(LOG, open(os.path.join(SIM, 'apply_sim_r5_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1, default=str)
print('Law vs Provider: C28, J28 e READ ME B8 com nota de limitacao')

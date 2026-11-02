"""Consolida achados/VERIFICADO-1.md e VERIFICADO-2.md no comparativo final (como está → o que pode mudar).
Uso: python -I scripts/build_comparativo.py <pasta da validação>
Exclui REFUTADO. Ordena por gravidade (S1→S4), veredito (CONFIRMADO, PROVÁVEL, SEM FONTE) e artefato."""
import sys, os, re, collections, openpyxl
from openpyxl.styles import Font, PatternFill, Alignment

V = sys.argv[1]
rows = []
for f in ('VERIFICADO-1.md', 'VERIFICADO-2.md'):
    head = None
    for l in open(os.path.join(V, 'achados', f), encoding='utf-8'):
        if not l.startswith('|'):
            head = None if not l.strip() else head
            continue
        cells = [c.strip() for c in l.strip().strip('|').split('|')]
        if cells[0] == 'ID':
            head = cells
            continue
        if head is None or set(l.replace('|', '').strip()) <= set('-: '):
            continue
        if len(cells) < 10:
            continue
        cells = cells[:9] + [' | '.join(cells[9:])] if len(cells) > 10 else cells
        rows.append(cells + [f])

def norm_v(v):
    u = v.upper()
    for k in ('REFUTADO', 'CONFIRMADO', 'PROVÁVEL', 'PROVAVEL', 'SEM FONTE'):
        if k in u:
            return 'PROVÁVEL' if k == 'PROVAVEL' else k
    return v

def sev(g):
    m = re.search(r'S([1-4])', g)
    return int(m.group(1)) if m else 9

keep = [r for r in rows if norm_v(r[8]) != 'REFUTADO' and not r[1].lower().startswith('ver ')]
ref = [r for r in rows if norm_v(r[8]) == 'REFUTADO']
order = {'CONFIRMADO': 0, 'PROVÁVEL': 1, 'SEM FONTE': 2}
keep.sort(key=lambda r: (sev(r[7]), order.get(norm_v(r[8]), 3), r[1], r[0]))

wb = openpyxl.Workbook()
ws = wb.active
ws.title = 'Comparativo'
H = ['#', 'ID', 'Artefato', 'Onde (aba/célula/seção)', 'Como está hoje', 'O que pode mudar (proposta)', 'Fonte primária',
     'Classe', 'Gravidade', 'Veredito', 'Confiança %', 'Origem']
ws.append(H)
fill = {1: 'F8CBAD', 2: 'FFE699', 3: 'DDEBF7', 4: 'EDEDED'}
for i, r in enumerate(keep, 1):
    ws.append([i, r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7], norm_v(r[8]), r[9], r[10]])
    s = sev(r[7])
    if s in fill:
        ws.cell(row=i + 1, column=9).fill = PatternFill('solid', fgColor=fill[s])
for c in ws[1]:
    c.font = Font(bold=True, color='FFFFFF')
    c.fill = PatternFill('solid', fgColor='1F4E78')
for col, wd in zip('ABCDEFGHIJKL', (5, 12, 16, 26, 50, 55, 50, 12, 9, 13, 9, 16)):
    ws.column_dimensions[col].width = wd
for row in ws.iter_rows(min_row=2):
    for c in row:
        c.alignment = Alignment(wrap_text=True, vertical='top')
ws.freeze_panes = 'A2'
ws.auto_filter.ref = ws.dimensions

s = wb.create_sheet('Resumo')
s.append(['Artefato', 'S1', 'S2', 'S3', 'S4', 'Total', 'Confirmado', 'Provável', 'Sem fonte'])
arts = collections.OrderedDict()
for r in keep:
    a = r[1]
    d = arts.setdefault(a, collections.Counter())
    d['S%d' % sev(r[7])] += 1
    d[norm_v(r[8])] += 1
    d['tot'] += 1
for a, d in arts.items():
    s.append([a, d['S1'], d['S2'], d['S3'], d['S4'], d['tot'], d['CONFIRMADO'], d['PROVÁVEL'], d['SEM FONTE']])
s.append(['TOTAL'] + [sum(1 for r in keep if sev(r[7]) == k) for k in (1, 2, 3, 4)] + [len(keep)]
         + [sum(1 for r in keep if norm_v(r[8]) == k) for k in ('CONFIRMADO', 'PROVÁVEL', 'SEM FONTE')])
s.append([])
s.append(['Refutados (não entram)', len(ref)])
for r in ref:
    s.append([r[0], r[1], r[3][:200], r[10]])
out = os.path.join(V, 'COMPARATIVO-FINAL-CO-v1.0.xlsx')
wb.save(out)
print('linhas', len(keep), 'refutados', len(ref))
for r in s.iter_rows(values_only=True):
    if r and r[0] and r[0] != 'Refutados (não entram)' and len(r) > 5 and r[5] is not None:
        print(r)

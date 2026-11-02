"""Monta a RTM (matriz de rastreabilidade) da validação CO a partir da linha de base.
Uso: python -I scripts/build_rtm.py <pasta Research Pipeline/Colombia> <saida.xlsx>
Risco = nível de integridade (IEEE 1012-2024): alto / medio / baixo, pelas regras abaixo.
- CCG: alto se tem alíquota, valor, UVT/SMMLV, IBC, teto, limite, prazo; medio se cita lei sem valor; baixo o resto.
- WTC: marcações estatutárias (tax, saúde, FSP, ARL, parafiscales, pensão, salarial, bases) = alto; elemento NE, fórmula, tax code = medio; nome = baixo.
- DD: campo do país que muda cálculo = alto; demais campos e mapeadores = medio; ID = baixo.
- Specs: campo calculado pela folha (coluna 'Payroll Field (Y/N)' = Y) = alto; demais campos, regras, opções, estrutura = medio; matriz, resumo, exemplos, amostra = baixo (agregado).
- SIR: prazo, penalidade, artigo = alto; resto = medio.
- Payslip: linhas de valor da Payslip Spec = alto; resto = medio.
Classificação automática preliminar; revisar por amostra antes do GA."""
import sys, re, glob, os, openpyxl, docx
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

base, out = sys.argv[1], sys.argv[2]
V = os.path.join(base, '2026-10-29-validacao-research')
LAW = re.compile(r'((?:art(?:[ií]culo)?s?\.?\s*[\d\.\-]+[\w\-]*)|(?:Ley|Decreto|Resoluci[oó]n|Res\.|Concepto|Oficio|Sentencia|Circular|DUR|ET|CST)\s*(?:DIAN|MSPS)?\s*[\d\.]+(?:\s*(?:de|/)\s*\d{4})?)', re.I)
HI = re.compile(r'(\d+(?:[,\.]\d+)?\s?%|\$\s?[\d\.]+|COP\s?[\d\.]+|\bUVT\b|SMMLV|SMLMV|\bIBC\b|divisor|tarifa|al[ií]cuota|\btope\b|l[ií]mite|plazo|deadline|\brate\b|ceiling|\bcap\b|business day|d[ií]as? h[aá]bil)', re.I)
TASK = {'alto': 'Simulação + verificação total contra a fonte',
        'medio': 'Verificação automática total + fonte do que falhar',
        'baixo': 'Verificação automática + amostra'}
rows, count = [], {}


def add(art, loc, sec, item, risk, src=None):
    count[art] = count.get(art, 0) + 1
    cites = '; '.join(sorted(set(m.group(0).strip() for m in LAW.finditer(item or ''))))[:250]
    rows.append([f'{art}-{count[art]:05d}', art, loc, (sec or '')[:120], (item or '')[:1500], src or cites, risk, TASK[risk], '', '', ''])


def ok(v):
    return v not in (None, '') and str(v).strip().upper() not in ('NA', 'N/A', 'NONE')


# CCG
d = docx.Document(os.path.join(base, '2026-10-22-auditoria-lote1/CO-CCG-001-v1.4.docx'))
sec, n = '', 0
for p in d.paragraphs:
    t = p.text.strip()
    if not t:
        continue
    n += 1
    if p.style.name.startswith('Heading'):
        sec = t
        continue
    add('CCG', f'parágrafo {n}', sec, t, 'alto' if HI.search(t) else ('medio' if LAW.search(t) else 'baixo'))
for ti, t in enumerate(d.tables, 1):
    for ri, r in enumerate(t.rows, 1):
        cells = []
        for c in r.cells:
            ct = c.text.strip()
            if ct and (not cells or cells[-1] != ct):
                cells.append(ct)
        txt = ' | '.join(cells)
        if txt:
            add('CCG', f'tabela {ti} linha {ri}', 'tabela', txt, 'alto' if HI.search(txt) else ('medio' if LAW.search(txt) else 'baixo'))

# WTC
w = openpyxl.load_workbook(os.path.join(base, '2026-10-22-auditoria-lote1/CO-WTC-001-v1.6.xlsx'), read_only=True, data_only=True)
data = list(w['Wage Type Catalogue'].iter_rows(values_only=True))
h = [str(x or '') for x in data[0]]
stat = [i for i, x in enumerate(h) if x.startswith(('Subject to', 'Table Tax', 'Special Tax', 'Salary or', 'Statutory-Benefit', 'Vacation Base'))]
med = [i for i, x in enumerate(h) if x.startswith(('Nomina Electronica', 'Formula', 'Tax Code'))]
for ri, r in enumerate(data[1:], 2):
    if not any(v not in (None, '') for v in r):
        continue
    wt = f'{r[0]} — {r[1]}'
    for i in stat:
        if ok(r[i]):
            add('WTC', f'Wage Type Catalogue!{get_column_letter(i + 1)}{ri}', h[i], f'{wt}: {h[i]} = {r[i]}', 'alto')
    for i in med:
        if ok(r[i]):
            add('WTC', f'Wage Type Catalogue!{get_column_letter(i + 1)}{ri}', h[i], f'{wt}: {h[i]} = {r[i]}', 'medio')
    add('WTC', f'Wage Type Catalogue!A{ri}', 'nome/explicação', wt, 'baixo')
for sh in ('Employer Sick Pay', 'Tax Credit', 'Form Reference Guide'):
    for ri, r in enumerate(w[sh].iter_rows(values_only=True), 1):
        txt = ' | '.join(str(v) for v in r if v not in (None, ''))
        if txt and ri > 1:
            add('WTC', f'{sh}!linha {ri}', sh, txt, 'alto' if (sh != 'Form Reference Guide' and HI.search(txt)) else 'medio')

# DD
CALC = re.compile(r'(salar|integral|contrat|riesgo|\bARL\b|dependient|\bAFC\b|fecha|date|cotizante|subtipo|pensi|salud|health|cesant|vivienda|prepagad|interes|aprendiz|residen|exoner|hora|jornada|part-time|tiempo parcial|régimen|regime|tax|retenci|withhold|fund|fondo|EPS|AFP|CCF|caja)', re.I)
w = openpyxl.load_workbook(os.path.join(base, '2026-10-22-auditoria-lote1/CO-DD-001-v1.3.xlsx'), read_only=True, data_only=True)
for sh in ('ID Information', 'Country Fields', 'Country Option Mappers'):
    for ri, r in enumerate(w[sh].iter_rows(values_only=True), 1):
        if ri < 5:
            continue
        txt = ' | '.join(str(v) for v in r if v not in (None, ''))
        if txt:
            risk = 'alto' if (sh == 'Country Fields' and CALC.search(txt[:200])) else ('medio' if sh != 'ID Information' else 'baixo')
            add('DD', f'{sh}!linha {ri}', sh, txt, risk)

# Specs
VAL = re.compile(r'(valor|value|amount|monto|\bIBC\b|aporte|cotiz|contribution|retenci|withhold|total|salar|base|tarifa|rate|d[ií]as|days|ingreso|income|deducci|devengad|cesant|interes|prima|bonus|vacaci)', re.I)
for f in sorted(glob.glob(os.path.join(base, 'co-report-crosscheck/05-final/*.xlsx'))):
    code = os.path.basename(f).split('-Spec')[0]
    w = openpyxl.load_workbook(f, read_only=True, data_only=True)
    ws = w.worksheets[3]
    rs = list(ws.iter_rows(values_only=True))
    hh = [str(x or '') for x in rs[1]]
    ip = next((i for i, x in enumerate(hh) if x.startswith('Payroll Field')), None)
    for ri, r in enumerate(rs[2:], 3):
        if not any(v not in (None, '') for v in r):
            continue
        name = f'{r[0]} / {r[1]}'
        payroll = ip is not None and str(r[ip]).strip().upper().startswith('Y')
        rest = ' | '.join(str(v) for v in r[2:] if v not in (None, ''))[:1200]
        add('SPEC', f'{code} {ws.title}!linha {ri}', code, name + ' — ' + rest, 'alto' if payroll else 'medio')
    for sh in ('Population Rules', 'Field Options', 'File Structure'):
        if sh in w.sheetnames:
            for ri, r in enumerate(w[sh].iter_rows(values_only=True), 1):
                txt = ' | '.join(str(v) for v in r if v not in (None, ''))
                if txt and ri > 2:
                    add('SPEC', f'{code} {sh}!linha {ri}', f'{code} {sh}', txt, 'medio')
    for sh in ('Report Matrix', 'Payroll Scope Summary', 'Example Analysis', 'Sample File'):
        if sh in w.sheetnames:
            k = sum(1 for r in w[sh].iter_rows(values_only=True) if any(v not in (None, '') for v in r))
            add('SPEC', f'{code} {sh}', f'{code} {sh}', f'{k} linhas (verificação automática de coerência com a aba de campos)', 'baixo')

# SIR (captura de 29/10)
sec = ''
with open(os.path.join(V, 'linha-de-base/CO-SIR-001-v1.1-captura-2026-10-29.md'), encoding='utf-8') as fh:
    for i, l in enumerate(fh, 1):
        l = l.strip()
        if l.startswith('#'):
            sec = l.strip('# ')
            continue
        if l.startswith(('-', 'Document ID', 'Related', 'Histórico')):
            risky = HI.search(l) or re.search(r'(prazo|dia|antes de|até|penal|Ley|art\.)', l, re.I)
            add('SIR', f'captura linha {i}', sec, l.lstrip('- '), 'alto' if risky else 'medio')

# Payslip
w = openpyxl.load_workbook(os.path.join(base, 'CO-compliance/06-payslip/CO_Compliance_Payslip_Generator-v1.1-DRAFT.xlsx'), read_only=True, data_only=True)
for sh in ('Payslip Spec', 'Field Option', 'Population Range', 'Unit Rate Details'):
    if sh in w.sheetnames:
        for ri, r in enumerate(w[sh].iter_rows(values_only=True), 1):
            txt = ' | '.join(str(v) for v in r if v not in (None, ''))
            if txt and ri > 1:
                add('PAYSLIP', f'{sh}!linha {ri}', sh, txt, 'alto' if (sh == 'Payslip Spec' and VAL.search(txt[:150])) else 'medio')

# grava
wb = openpyxl.Workbook()
ws = wb.active
ws.title = 'RTM'
ws.append(['ID', 'Artefato', 'Local', 'Seção / coluna', 'Item (texto)', 'Fonte citada no artefato', 'Risco (integridade)',
           'Tarefa mínima', 'Caso(s) / verificação', 'Veredito', 'Observação'])
for r in rows:
    ws.append(r)
for c in ws[1]:
    c.font = Font(bold=True, color='FFFFFF')
    c.fill = PatternFill('solid', fgColor='1F4E78')
    c.alignment = Alignment(wrap_text=True)
for col, wd in zip('ABCDEFGHIJK', (13, 9, 30, 28, 80, 35, 10, 30, 22, 12, 30)):
    ws.column_dimensions[col].width = wd
ws.freeze_panes = 'A2'
ws.auto_filter.ref = ws.dimensions
s = wb.create_sheet('Resumo')
s.append(['Artefato', 'alto', 'medio', 'baixo', 'total'])
for a in ('CCG', 'WTC', 'DD', 'SPEC', 'SIR', 'PAYSLIP'):
    c = [sum(1 for r in rows if r[1] == a and r[6] == k) for k in ('alto', 'medio', 'baixo')]
    s.append([a] + c + [sum(c)])
s.append(['TOTAL'] + [sum(1 for r in rows if r[6] == k) for k in ('alto', 'medio', 'baixo')] + [len(rows)])
s.append([])
s.append(['Regras de risco: docstring de scripts/build_rtm.py e PLANO-DE-ACAO §4. Classificação automática preliminar; revisar por amostra antes do GA.'])
wb.save(out)
for r in s.iter_rows(values_only=True):
    if r and r[0]:
        print(r)

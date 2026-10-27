"""BE-WTC-001 v1.3: acrescenta os códigos 62 / 65 / 79 da aba "All Codes" do Global WTC 1.1 que faltam.

Pedido da Suman (22/10): "this is 79 series" + "Please use this complete Global WTC for creating the one for
Belgium" (Global Wage Type Catalogue 1.1, aba All Codes, gid 1123343809). Lida pelo Chrome em 22/10 (export csv em
memória, sem download): 1044 códigos 62/65/79, dos quais 355 faltam na v1.2. Lista abaixo (ALLCODES), transcrita
da leitura. Base: v1.2 (= Drive). Edição por XML (sem openpyxl.save). Linhas novas a partir da 829, azul FFDDEBF7.
Uso: python -I build_wtc_v1_3.py BE-WTC-001-v1.2.xlsx BE-WTC-001-v1.3.xlsx
"""
import sys, re, zipfile, csv, os, html
import openpyxl

SRC, OUT = sys.argv[1:3]
HERE = os.path.dirname(os.path.abspath(__file__))

def rng(a, b):
    return list(range(a, b + 1))

# ------------------------------------------------ All Codes (Global 1.1): código -> (nome, unidade, ocorrência, tipo)
G = {}
def add(codes, name, unit, occ, typ):
    for c in codes:
        G[str(c)] = (name, unit, occ, typ)
add([62105], 'Basic salary (rate)', 'Month', 'Recurring', 'Rate')
for i, c in enumerate(rng(65110, 65119), 1):
    add([c], f'Social Security {i} (employer) expense', 'Month', 'Recurring', 'Tax')
add([65508, 65509], 'Car benefit (notional)', 'Month', 'Recurring', 'Earning')
add([65609], 'Phone benefit (notional)', 'Month', 'Recurring', 'Earning')
add([65659], 'Meal benefit (notional)', 'Month', 'Recurring', 'Earning')
LT = {1: 'Vacation leave', 2: 'Emergency leave', 3: 'Examination leave', 4: 'Hajj leave', 5: 'Marriage leave',
      6: 'Maternity leave', 7: 'Paternity leave', 8: 'Sick leave', 9: 'Training leave', 10: 'Unpaid leave',
      50: 'Vacation cashout leave'}
def lt(nn):
    return LT.get(nn, 'Other leave')
# 790xx unidades
for nn in list(range(1, 51)) + list(range(80, 100)):
    add([79000 + nn], lt(nn), 'Unit', 'Recurring', 'Leave')
add([79068], 'Sick leave 2', 'Unit', 'Recurring', 'Leave')
add([79078], 'Sick leave 3', 'Unit', 'Recurring', 'Leave')
# 791xx tirados
for nn in range(1, 51):
    name = f'Other leave {nn - 11} year 1 transitional taken' if 41 <= nn <= 49 else lt(nn) + ' taken'
    add([79100 + nn], name, 'Unit', 'Recurring', 'Cumulative')
add([79168], 'Sick leave taken 2', 'Unit', 'Recurring', 'Cumulative')
add([79178], 'Sick leave taken 3', 'Unit', 'Recurring', 'Cumulative')
# 792xx saldos
for nn in range(1, 51):
    name = 'Other leave 39 year 1 transitional taken' if nn == 40 else lt(nn) + ' balance'
    add([79200 + nn], name, 'Unit', 'Recurring', 'Cumulative')
add([79268], 'Sick leave balance 2', 'Unit', 'Recurring', 'Cumulative')
add([79278], 'Sick leave balance 3', 'Unit', 'Recurring', 'Cumulative')
add([79301], 'Vacation leave increment', 'Unit', 'Recurring', 'Cumulative')
# unidades de doença 793/796/797/798/799
for h in (3, 6, 7, 8, 9):
    add([79008 + h * 100], 'Sick leave unit', 'Unit', 'Recurring', 'Leave')
    add([79068 + h * 100], 'Sick leave unit 2', 'Unit', 'Recurring', 'Leave')
    add([79078 + h * 100], 'Sick leave unit 3', 'Unit', 'Recurring', 'Leave')
# 795xx pagamento calculado
for nn in range(1, 51):
    add([79500 + nn], lt(nn) + ' calculated payout days', 'Amount', 'Additional', 'Earning')
add([79568], 'Sick leave calculated payout days 2', 'Amount', 'Additional', 'Earning')
add([79578], 'Sick leave calculated payout days 3', 'Amount', 'Additional', 'Earning')
# 799xx unidade geral (menos 79908/79968/79978, já acima)
for c in rng(79901, 79999):
    if str(c) not in G:
        add([c], 'General Leave Unit', 'Unit', 'Recurring', 'Leave')

# conferência com a contagem lida no All Codes
from collections import Counter
cnt = Counter((v[1], v[2], v[3]) for v in G.values())
assert len(G) == 355, len(G)
assert cnt == Counter({('Unit', 'Recurring', 'Leave'): 183, ('Unit', 'Recurring', 'Cumulative'): 105,
                       ('Amount', 'Additional', 'Earning'): 52, ('Month', 'Recurring', 'Tax'): 10,
                       ('Month', 'Recurring', 'Earning'): 4, ('Month', 'Recurring', 'Rate'): 1}), cnt

# ------------------------------------------------ holandês
NLT = {'Vacation leave': 'Vakantieverlof', 'Emergency leave': 'Noodverlof', 'Examination leave': 'Examenverlof',
       'Hajj leave': 'Hadj-verlof', 'Marriage leave': 'Huwelijksverlof', 'Maternity leave': 'Moederschapsverlof',
       'Paternity leave': 'Vaderschapsverlof', 'Sick leave': 'Ziekteverlof', 'Training leave': 'Opleidingsverlof',
       'Unpaid leave': 'Onbetaald verlof', 'Other leave': 'Ander verlof', 'Vacation cashout leave': 'Vakantiesaldo'}
SUF = {'taken': 'opgenomen', 'balance': 'saldo', 'increment': 'opbouw', 'unit': 'eenheid',
       'calculated payout days': 'berekende uitbetaling (dagen)'}
def dutch(n):
    fixed = {'Basic salary (rate)': 'Basisloon (tarief)', 'Car benefit (notional)': 'Voordeel bedrijfswagen (fictief)',
             'Phone benefit (notional)': 'Voordeel telefoon (fictief)', 'Meal benefit (notional)': 'Voordeel maaltijden (fictief)',
             'General Leave Unit': 'Algemene verlofeenheid'}
    if n in fixed:
        return fixed[n]
    m = re.match(r'^Social Security (\d+) \(employer\) expense$', n)
    if m:
        return f'Socialezekerheidsbijdrage {m.group(1)} (werkgever) - kost'
    m = re.match(r'^Other leave (\d+) year 1 transitional taken$', n)
    if m:
        return f'Ander verlof {m.group(1)} jaar 1 overgangsregeling - opgenomen'
    m = re.match(r'^(.*? leave)(?: (taken|balance|increment|unit|calculated payout days))?(?: (\d))?$', n)
    assert m, n
    out = NLT[m.group(1)]
    if m.group(3):
        out += ' ' + m.group(3)
    if m.group(2):
        out += ' - ' + SUF[m.group(2)]
    return out

# ------------------------------------------------ base
wb = openpyxl.load_workbook(SRC, data_only=True)
ws = wb['Wage Type Catalogue']
BE, ROW = {}, {}
for i, r in enumerate(ws.iter_rows(min_row=2, max_col=20, values_only=True), 2):
    if r[0] is not None:
        k = str(int(r[0])) if isinstance(r[0], float) else str(r[0])
        BE[k] = ['' if v is None else str(v) for v in r]
        ROW[k] = i
assert not set(G) & set(BE)
assert max(ROW.values()) == 828

def ref(code):
    return f"{code} '{BE[code][1]}' (this sheet, row {ROW[code]})"

NA5 = ['NA'] * 5
UNPAID = ('Unpaid leave carries no pay in Belgium; the unpaid days are handled through '
          f"{ref('62109')} and the reduction {ref('21109')}.")

def treat(c, name, unit, occ, typ):
    """-> (E, F, G, J, flags, linha equivalente)"""
    head = f"Global WTC 1.1 code {c} ('{name}', All Codes)."
    n = int(c)
    if c == '62105':
        return ('Intermediary', f"{head} Rate carrier, not a payment: holds the monthly salary rate used to compute "
                f"the basic salary and its proration. The amount paid goes to {ref('62100')}, whose explanation "
                "carries the legal basis.", 'NA', 'Recurring', NA5, '62100')
    if 65110 <= n <= 65119:
        return ('Employer Contribution', f"{head} Expense posting of an employer social security contribution, not "
                f"an employee earning. Belgian treatment follows {ref('23671')}, whose explanation carries the rates "
                "and the legal basis; the other employer levies are the 23xxx rows of this sheet.",
                'NA', 'Recurring', NA5, '23671')
    if c in ('65508', '65509', '65609', '65659'):
        a = {'65508': '62500', '65509': '62500', '65609': 'BE-057', '65659': 'BE-056'}[c]
        b = BE[a]
        return (b[4], f"{head} Notional value of the benefit, used as the taxable base. Belgian treatment follows "
                f"{ref(a)}, whose explanation carries the legal basis.", b[6], b[9], b[13:18], a)
    nn, blk = n % 100, (n // 100) % 10
    payout = str(79400 + nn)
    if typ in ('Leave', 'Cumulative'):
        kind = {'Leave': 'Leave-day counter (unit)', 'Cumulative': 'Leave accumulator (days)'}[typ]
        if name == 'General Leave Unit':
            tail = ('The pay for the leave, where due, goes to the payout row of the leave type concerned '
                    '(79401 to 79499 in this sheet).')
            a = 'NA'
        elif nn == 10:
            tail = UNPAID
            a = '62109'
        else:
            tail = (f"The pay for these days, where due, goes to {ref(payout)}, whose explanation names the Belgian "
                    "treatment and its legal basis.")
            a = payout
        return ('Intermediary', f"{head} {kind}, not a payment; it carries no tax or social security treatment of "
                f"its own. {tail}", 'NA', 'Recurring', NA5, a)
    if typ == 'Earning' and blk == 5:
        if nn == 10:
            return ('Earning', f"{head} Not applicable in Belgium: {UNPAID}", 'NA', 'Additional', NA5, 'NA')
        b = BE[payout]
        return (b[4], f"{head} Calculated payout value for the leave days. Belgian treatment follows {ref(payout)}, "
                "whose explanation names the Belgian treatment and its legal basis.", b[6], b[9], b[13:18], payout)
    raise ValueError(c)

order = sorted(G, key=int)
rows, audit = [], []
for c in order:
    name, unit, occ, typ = G[c]
    E, F, Gc, J, flags, a = treat(c, name, unit, occ, typ)
    rows.append([c, name, dutch(name), '', E, F, Gc, '', '', J, '', '', '', *flags, '', ''])
    audit.append([c, name, unit, occ, typ, a, E, Gc, J, *flags])

with open(os.path.join(HERE, 'mapeamento-v1.3.csv'), 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.writer(f)
    w.writerow(['Codigo', 'Nome All Codes', 'Pay Unit', 'Occurrence Global', 'Type Global', 'Linha BE equivalente',
                'Category', 'Tax Code', 'Occurrence', 'Subject to Tax', 'Table Tax', 'Special Tax', 'Subject to SI',
                'Subject to Pension'])
    w.writerows(audit)

# ------------------------------------------------ XML
zin = zipfile.ZipFile(SRC)
parts = {n: zin.read(n) for n in zin.namelist()}
COLS = [chr(65 + i) for i in range(20)]
STY = {'A': 95, 'B': 96, 'C': 96, 'D': 97, 'F': 96, 'T': 99}   # clones azuis criados na v1.1
EXTRA = ['U', 'V', 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI']

def cell(r, val, s):
    if val == '':
        return f'<c r="{r}" s="{s}"/>'
    if r[0] == 'A' and val.isdigit():
        return f'<c r="{r}" s="{s}"><v>{val}</v></c>'
    return f'<c r="{r}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{html.escape(val, quote=False)}</t></is></c>'

sh = parts['xl/worksheets/sheet2.xml'].decode('utf-8')
for i, r in enumerate(rows):
    rn = 829 + i
    cells = ''.join(cell(f'{col}{rn}', r[j], STY.get(col, 98)) for j, col in enumerate(COLS))
    cells += ''.join(f'<c r="{c}{rn}" s="16"/>' for c in EXTRA)
    newrow = f'<row r="{rn}" ht="15.75" customHeight="1">{cells}</row>'
    if rn <= 1000:
        sh, n = re.subn(rf'<row r="{rn}"[^>]*>.*?</row>', lambda m: newrow, sh, count=1, flags=re.S)
        assert n == 1, rn
    else:
        k = sh.index('</sheetData>')
        sh = sh[:k] + newrow + sh[k:]
parts['xl/worksheets/sheet2.xml'] = sh.encode('utf-8')

vc = parts['xl/worksheets/sheet1.xml'].decode('utf-8')
desc = ("Added the codes of the 62, 65 and 79 series in the Global WTC 1.1 'All Codes' tab that were still missing "
        f"({len(rows)} rows, catalogue rows 829 to {828 + len(rows)}, highlighted in light blue): 62105 basic salary rate, "
        "65110 to 65119 employer social security expense, 4 notional benefits, and in the 79 series the leave units, "
        "the taken, balance and increment accumulators and the calculated payout values. Counters and accumulators "
        "carry no tax or social security treatment of their own; payout values follow the matching 794xx row. "
        "Rows 2 to 828 unchanged.")
vals = {'B16': ('1.3', 'n'), 'C16': ('46317', 'n'), 'D16': (desc, 's'), 'E16': ('Under Review', 's'), 'F16': ('Wallisson Gomes', 's')}
def vcell(m):
    r, s = m.group(1), m.group(2)
    v, t = vals[r]
    if t == 'n':
        return f'<c r="{r}" s="{s}"><v>{v}</v></c>'
    return f'<c r="{r}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{html.escape(v, quote=False)}</t></is></c>'
vc, n = re.subn(r'<c r="([B-F]16)" s="(\d+)"/>', vcell, vc)
assert n == 5, n
parts['xl/worksheets/sheet1.xml'] = vc.encode('utf-8')

with zipfile.ZipFile(OUT, 'w') as zout:
    for info in zin.infolist():
        zout.writestr(info, parts[info.filename], compress_type=info.compress_type)
print('ok', OUT, len(rows), 'linhas', 829, '-', 828 + len(rows))

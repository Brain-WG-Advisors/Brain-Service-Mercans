"""QA r1b item 4: assemble and verify the CT 2026 withholding tables from raw-lines.tsv
(output of ct_tables_parse.py). Writes ct-tables/CT-2026-withholding-tables.csv and verify.json.
Usage: python -I ct_tables_build.py <outdir>"""
import sys, os, re, json, csv
from decimal import Decimal as D, ROUND_HALF_UP

OUT = sys.argv[1]
PERIOD = {31: 'weekly', 32: 'weekly', 33: 'biweekly', 34: 'biweekly', 35: 'semimonthly', 36: 'semimonthly',
          37: 'monthly', 38: 'monthly'}
NUM = re.compile(r'^\$[\d,]+(\.\d\d)?$')
num = lambda s: D(s.replace('$', '').replace(',', ''))
tab = {p: [] for p in ('weekly', 'biweekly', 'semimonthly', 'monthly')}
over = {}
for ln in open(os.path.join(OUT, 'raw-lines.tsv'), encoding='utf-8'):
    f = ln.rstrip('\n').split('\t')
    pg = int(f[0]); toks = [t.rsplit('@', 1) for t in f[2:]]
    vals = [t[0] for t in toks]
    if len(vals) == 7 and all(NUM.match(v) for v in vals):
        xs = [float(t[1]) for t in toks]
        assert xs == sorted(xs)
        tab[PERIOD[pg]].append([pg] + [num(v) for v in vals])
    elif vals and NUM.match(vals[0]) and len(vals) > 1 and all('?' in v or v.isdigit() for v in vals[1:]):
        over[PERIOD[pg]] = num(vals[0])          # '$1,932  Over  Refer to TPG-211' line (text glyphs not decoded)

checks = {}
for p, rows in tab.items():
    c = {'rows': len(rows), 'first': [str(x) for x in rows[0][1:3]], 'last': [str(x) for x in rows[-1][1:3]],
         'over_threshold': str(over.get(p))}
    gaps = [(i, str(rows[i - 1][2]), str(rows[i][1])) for i in range(1, len(rows)) if rows[i][1] != rows[i - 1][2]]
    c['contiguity_breaks'] = gaps
    c['band_inverted'] = [i for i, r in enumerate(rows) if not r[1] < r[2]]
    c['first_band_starts_at_0'] = rows[0][1] == 0
    c['last_upper_equals_over_threshold'] = rows[-1][2] == over.get(p)
    dec = {}
    for j, code in enumerate('ABCDF'):
        col = [r[3 + j] for r in rows]
        dec[code] = [i for i in range(1, len(col)) if col[i] < col[i - 1]]
    c['amount_decreases'] = dec
    checks[p] = c

def look(period, wage, code):
    for r in tab[period]:
        if r[1] < wage <= r[2]:
            return r[3 + 'ABCDF'.index(code)], (str(r[1]), str(r[2]))
    return None, None

ex = {}
v, band = look('weekly', D('700'), 'F')
ex['Ex8'] = {'period': 'weekly', 'wages': '700', 'code': 'F', 'table_amount': str(v), 'band': band,
             'expected_full': '17.65', 'ct_share': '0.60', 'withheld': str((v * D('0.60')).quantize(D('0.01'), ROUND_HALF_UP)),
             'expected_withheld': '10.59'}
v, band = look('weekly', D('1000'), 'A')
ex['Ex9'] = {'period': 'weekly', 'wages': '1000', 'code': 'A', 'table_amount': str(v), 'band': band, 'expected_full': '39.97',
             'week1_40pct': str((v * D('0.40')).quantize(D('0.01'), ROUND_HALF_UP)), 'expected_week1': '15.99'}
v, band = look('biweekly', D('2300'), 'B')
ex['Ex10'] = {'period': 'biweekly', 'wages': '2300', 'code': 'B', 'table_amount': str(v), 'band': band, 'expected_full': '78.82'}
ok = (ex['Ex8']['table_amount'] == '17.65' and ex['Ex8']['withheld'] == '10.59' and ex['Ex9']['table_amount'] == '39.97'
      and ex['Ex9']['week1_40pct'] == '15.99' and ex['Ex10']['table_amount'] == '78.82')
allok = ok and all(not c['contiguity_breaks'] and not c['band_inverted'] and c['first_band_starts_at_0']
                   and c['last_upper_equals_over_threshold'] and not any(c['amount_decreases'].values()) for c in checks.values())
json.dump({'checks': checks, 'examples': ex, 'examples_reproduce': ok, 'all_checks_pass': allok},
          open(os.path.join(OUT, 'verify.json'), 'w'), indent=1)
with open(os.path.join(OUT, 'CT-2026-withholding-tables.csv'), 'w', encoding='utf-8', newline='') as fh:
    w = csv.writer(fh, lineterminator='\n')
    w.writerow(['period', 'row', 'pdf_page', 'wages_greater_than', 'wages_less_than_or_equal_to', 'A', 'B', 'C', 'D', 'F'])
    for p, rows in tab.items():
        for i, r in enumerate(rows, 1):
            w.writerow([p, i, r[0]] + ['%s' % x for x in r[1:]])
print(json.dumps({p: {k: v for k, v in c.items() if k in ('rows', 'over_threshold', 'contiguity_breaks', 'amount_decreases', 'last_upper_equals_over_threshold')} for p, c in checks.items()}))
print(json.dumps(ex)); print('examples_reproduce', ok, 'all_checks_pass', allok)

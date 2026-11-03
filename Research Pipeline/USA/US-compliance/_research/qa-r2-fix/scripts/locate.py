import sys, json; sys.path.insert(0, '.')
from lib import *
SYN = {'wage_base': ['wage base', 'taxable wage', 'wage limit', 'taxable payroll'], 'minwage': ['minimum wage'], 'tipped': ['tip'], 'cash_wage': ['cash wage', 'tip'],
 'garn': ['garnish', 'exempt', 'disposable'], 'supplemental': ['supplemental', 'bonus'], 'overtime': ['overtime', 'one and one-half', 'one and one half', 'time and a half'],
 'multiplier': ['one and one-half', 'one and one half', 'times'], 'famli': ['famli', 'premium'], 'pfml': ['premium', 'contribution'], 'pfl': ['premium', 'contribution'],
 'sui': ['unemployment', 'contribution', 'tax rate'], 'ui': ['unemployment', 'contribution'], 'new_employer': ['new employer'], 'flat': ['rate', 'percent'],
 'rate': ['rate', 'percent', '%'], 'youth': ['youth', 'under 20', 'minor', 'student'], 'student_learner': ['student', 'learner'], 'breach': ['breach', 'attorney general'],
 'data': ['breach', 'resident'], 'mbt': ['modified business', 'payroll'], 'eit': ['earned income', 'wage tax'], 'oracle': ['withh'], 'withholding': ['withh'],
 'band': ['over', 'not over', 'withh'], 'sciad': ['adjustment', 'deduction'], 'wh': ['withh'], 'pit': ['tax'], 'threshold': ['threshold', 'more than', 'exceed'],
 'max': ['maximum', 'max'], 'min': ['minimum'], 'weekly': ['week'], 'monthly': ['month'], 'hourly': ['hour'], 'efile': ['electronic', 'e-file'],
 'prevailing_wage': ['prevailing', 'construction'], 'municipal': ['municipal'], 'count_in_force': ['municipal'], 'foreign_construction': ['foreign', 'construction'],
 'agi_threshold': ['adjusted gross', 'income'], 'high_income_tax': ['income'], 'base_week': ['base week'], 'tip_credit': ['tip'], 'exempt': ['exempt'], 'salary': ['salary'],
 'liquid_assets': ['liquid', 'exemption'], 'household_support': ['household', 'support'], 'top_rate': ['%'], 'lump_sum': ['lump', 'highest'], 'gross_volume': ['gross', 'sales', 'business'],
 'metro_shs': ['supportive housing', 'metro'], 'multnomah_pfa': ['preschool', 'multnomah'], 'withholding_trigger': ['withh'], 'consumer': ['exempt', 'week'], 'floor': ['exempt', 'week', 'times']}
def kw(key):
    segs = key.split('.'); words = set()
    for s in segs:
        words |= set(SYN.get(s, []))
        for part in s.split('_'):
            if len(part) >= 5: words.add(part[:6])
    for i in range(len(segs) - 1):
        j = segs[i] + '_' + segs[i + 1]
    return [w.lower() for w in words]
def forms(v):
    if isinstance(v, bool) or not isinstance(v, (int, float)): return []
    out = []
    def numstr(x):
        x = round(x, 6); r = []
        if x == int(x):
            i = int(x); r += [f'{i:,}', str(i), f'{i:,}.00', f'{i}.00']
        for d in (1, 2, 3, 4):
            s = f'{x:.{d}f}'
            if abs(float(s) - x) < 1e-9: r += [s, f'{x:,.{d}f}'] + ([s[1:]] if s.startswith('0.') else [])
        return list(dict.fromkeys(r))
    out += numstr(v)
    if abs(v) < 1: out += [s + '%' for s in numstr(v * 100)] + [s + ' percent' for s in numstr(v * 100)]
    return list(dict.fromkeys(out))
def locate(key, v, paths, small_ok=False):
    words = kw(key); best = None
    for p in paths:
        t = text_of(p); tl = t.lower()
        for s in forms(v):
            for m in re.finditer(r'(?<![\d.,])' + re.escape(s) + r'(?![\d]|[.,]\d)', t):
                ctx = tl[max(0, m.start() - 220): m.end() + 220]
                sc = sum(1 for w in words if w in ctx)
                if best is None or sc > best[0]:
                    best = (sc, p, m.start(), s)
    if not best: return None
    sc, p, pos, s = best; t = text_of(p)
    return {'score': sc, 'file': p, 'page': page_at(t, pos), 'form': s, 'snip': snippet(t, pos, 110)}

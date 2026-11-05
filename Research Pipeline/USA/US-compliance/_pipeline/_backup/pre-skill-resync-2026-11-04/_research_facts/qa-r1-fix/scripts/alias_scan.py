"""Find alias key groups (same register_id + value + effective_from, same meaning) across _research/*-facts.json."""
import json, glob, collections, re, sys, os
BASE = sys.argv[1] if len(sys.argv) > 1 else "."
R = os.path.join(BASE, '_research')
PREFIX = {'rspec', 'sir', 'psl', 'dd', 'wtc', 'ccg'}
SYN = {'sit': 'pit', 'wh': 'pit', 'std': 'standard', 'newhire': 'new hire', 'exists': 'applies',
       'pct': 'rate', 'percent': 'rate', 'yrs': 'years', 'retention_years': 'retention years',
       'sui': 'ui', 'suta': 'ui', 'oasdi': 'ss', 'socsec': 'ss', 'deadline': 'due', 'report': 'due',
       'num': 'count', 'max_working_days': 'max working days', 'lit': 'local', 'mw': 'minwage',
       'minimum_wage': 'minwage', 'min_wage': 'minwage', 'paystub': 'payslip', 'pay_statement': 'payslip',
       'wage_base': 'base', 'taxable_wage_base': 'base', 'wagebase': 'base', 'ceiling': 'base'}
FILL = {'value', 'per', 'amount', 'rule', 'the', 'of', 'state', 'general', 'flat', 'statutory', 'figure'}
JUR = None

def words(key):
    t = key.split('.')
    if t[0] in PREFIX:
        t = t[1:]
    s = ' '.join(t)
    for k, v in SYN.items():
        s = re.sub(r'(?<![a-z0-9])' + re.escape(k) + r'(?![a-z0-9])', v, s)
    w = set(re.split(r'[ ._]+', s)) - {''}
    w = {SYN.get(x, x) for x in w}
    return w - FILL

SOFT = {'annual', 'rate', 'county', 'pit', 'ui', 'levy', 'result', 'withholding', 'total', 'max', 'wages',
        'share', 'percent', 'amount', 'applies', 'nonresident', 'nonres', 'local', 'statutory', 'top', 'tax',
        'number', 'fields', 'list', 'full', 'days', 'threshold', 'current', 'single_rate'}

def same(a, b):
    wa, wb = words(a), words(b)
    if wa == wb:
        return True
    if 'oracle' in wa and 'oracle' in wb:
        return True
    lo, hi = (wa, wb) if len(wa) <= len(wb) else (wb, wa)
    if lo <= hi and (hi - lo) <= SOFT:
        return True
    # differ only by soft words on both sides
    if (wa - wb) <= SOFT and (wb - wa) <= SOFT and len(wa & wb) >= 3:
        return True
    return False

def load():
    out = []
    for f in sorted(glob.glob(os.path.join(R, '*-facts.json'))):
        d = json.load(open(f, encoding='utf-8'))
        for i, x in enumerate(d['facts']):
            out.append((os.path.basename(f), i, x))
    return out

if __name__ == '__main__':
    allf = load()
    g = collections.defaultdict(lambda: collections.defaultdict(list))
    for f, i, x in allf:
        g[(x['register_id'], json.dumps(x['value'], ensure_ascii=False), x['effective_from'])][x['key']].append(f)
    alias, distinct = [], []
    for k, kv in g.items():
        if len(kv) < 2:
            continue
        keys = sorted(kv)
        # cluster keys by equal normalized word set
        par = {x: x for x in keys}
        def find(x):
            while par[x] != x:
                x = par[x]
            return x
        for a in keys:
            for b in keys:
                if a < b and same(a, b):
                    par[find(a)] = find(b)
        cl = collections.defaultdict(list)
        for key in keys:
            cl[find(key)].append(key)
        for ks in cl.values():
            if len(ks) > 1:
                alias.append((k, sorted(ks), {kk: kv[kk] for kk in ks}))
        for ks in cl.values():
            if len(ks) == 1 and len(cl) > 1:
                pass
        if all(len(ks) == 1 for ks in cl.values()):
            distinct.append((k, keys))
    json.dump({'alias': [[list(k), ks, fs] for k, ks, fs in alias], 'distinct': [[list(k), ks] for k, ks in distinct]},
              open(sys.argv[2], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('candidate groups', sum(1 for v in g.values() if len(v) > 1), 'alias clusters', len(alias), 'distinct groups', len(distinct))

# Synthesis C step 5: one key = one value/date set across all facts files.
# Usage: python -I step5_fix.py <BASE> [--write]
import json, glob, collections, os, sys, shutil, copy, datetime, csv, re
BASE = sys.argv[1]; WRITE = '--write' in sys.argv
RES = os.path.join(BASE, '_research'); BK = os.path.join(RES, 'synthesis-C', '_backup'); WORK = os.path.join(RES, 'synthesis-C', '_work')
REG = {r['id']: r for r in csv.DictReader(open(os.path.join(BASE, '00-official-sources', 'legal-basis-register.csv'), encoding='utf-8'))}
ISO = re.compile(r'^\d{4}-\d{2}-\d{2}$')
def backup(p):
    dst = os.path.join(BK, os.path.relpath(p, BASE))
    if not os.path.exists(dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy2(p, dst)
def prio(fn):
    if fn.startswith('CCG-annex_'): return 0
    if fn.startswith('CCG-'): return 1
    if fn.startswith('WTC-global'): return 2
    if fn.startswith('WTC-'): return 3
    return {'RSPEC-facts.json': 4, 'DD-8_sheets-facts.json': 5, 'SIR-facts.json': 6, 'PSL-facts.json': 7}.get(fn, 9)
def daybefore(d): return (datetime.date.fromisoformat(d) - datetime.timedelta(days=1)).isoformat()

docs = {os.path.basename(p): json.load(open(p, encoding='utf-8')) for p in sorted(glob.glob(os.path.join(RES, '*-facts.json')))}
LOG = []

# --- specific fix: WTC IN county chart dated by edition (R46 Jan-Sep, R47 from Oct)
w = docs['WTC-country_specific-facts.json']
newf = []
for f in w['facts']:
    if f['key'] in ('in.local.county_lit.rate.marion', 'in.local.county_lit.rate.min', 'in.local.county_lit.rate.max') and f['effective_from'] == '2026-01-01' and f['register_id'] == 'US-INS5-007':
        a = copy.deepcopy(f); r = REG['US-IN-001']
        a.update({'effective_to': '2026-09-30', 'register_id': 'US-IN-001', 'tier': r['tier'], 'authority': r['authority'], 'url': r['url'], 'verification_method': 'direct artifact inspection'})
        a['note'] = 'DN#1 R46/01-26 county chart (local copy inspected); same rate as R47.'
        b = copy.deepcopy(f); b['effective_from'] = '2026-10-01'
        newf += [a, b]; LOG.append(('WTC-country_specific-facts.json', f['key'], 'split by edition: R46 (US-IN-001) 2026-01-01..09-30 + R47 (US-INS5-007) from 2026-10-01'))
    else:
        newf.append(f)
w['facts'] = newf

by = collections.defaultdict(lambda: collections.defaultdict(list))
for fn, d in docs.items():
    for i, f in enumerate(d['facts']): by[f['key']][fn].append(f)
changed = set(); report = []
for key, files in by.items():
    if len(files) < 2: continue
    groups = collections.defaultdict(list)
    for fn, xs in files.items():
        for x in xs: groups[x['effective_from']].append((prio(fn), fn, x))
    # merge adjacent periods with the same value when no single file carries both (dating basis differs, not the value)
    alias = {}
    order = sorted(groups)
    i = 0
    while i < len(order) - 1:
        a, b = order[i], order[i + 1]
        va = {json.dumps(x['value']) for _, _, x in groups[a]}; vb = {json.dumps(x['value']) for _, _, x in groups[b]}
        fa = {fn for _, fn, _ in groups[a]}; fb = {fn for _, fn, _ in groups[b]}
        num = lambda vs: {round(float(json.loads(v)), 9) if json.loads(v).__class__ in (int, float) else v for v in vs}
        if len(num(va)) == 1 and num(va) == num(vb) and not (fa & fb):
            groups[a] += groups.pop(b); alias[b] = a; order.pop(i + 1)
            for k2, v2 in list(alias.items()):
                if v2 == b: alias[k2] = a
        else:
            i += 1
    canon = {}
    for ef, lst in groups.items():
        lst.sort(key=lambda t: (t[0], t[1]))
        c = copy.deepcopy(lst[0][2]); c['effective_from'] = ef
        r = REG.get(c['register_id'], {})
        if c.get('effective_to') is None:
            if ISO.match(r.get('effective_to') or '') and r['effective_to'] >= ef: c['effective_to'] = r['effective_to']
            else:
                b = sorted({x.get('effective_to') for _, _, x in lst if x.get('effective_to')})
                if b: c['effective_to'] = b[0]
        canon[ef] = c
    efs = sorted(canon)
    for a, b in zip(efs, efs[1:]):
        lim = daybefore(b)
        if canon[a].get('effective_to') is None or canon[a]['effective_to'] > lim: canon[a]['effective_to'] = lim
    sig = [(ef, canon[ef].get('effective_to'), json.dumps(canon[ef]['value'])) for ef in efs]
    for fn, xs in files.items():
        mine = {alias.get(x['effective_from'], x['effective_from']): x for x in xs}
        before = sorted((x['effective_from'], x.get('effective_to'), json.dumps(x['value'])) for x in xs)
        if before == sig: continue
        out = []
        for ef in efs:
            if ef in mine:
                x = mine[ef]; x['value'] = canon[ef]['value']; x['effective_from'] = ef; x['effective_to'] = canon[ef].get('effective_to')
            else:
                x = copy.deepcopy(canon[ef]); x.pop('consumed_by', None)
                x['note'] = ((x.get('note') or '') + ' | Synthesis C: period copied from the owning file for cross-file consistency.').strip(' |')
            out.append(x)
        d = docs[fn]
        d['facts'] = [f for f in d['facts'] if f['key'] != key] + out
        changed.add(fn)
        report.append((key, fn, before, sig))
for fn in sorted(changed | {'WTC-country_specific-facts.json'}):
    if WRITE:
        p = os.path.join(RES, fn); backup(p)
        json.dump(docs[fn], open(p, 'w', encoding='utf-8', newline='\n'), ensure_ascii=False, indent=1)
with open(os.path.join(WORK, 'step5-divergences.csv'), 'w', encoding='utf-8', newline='') as fh:
    wr = csv.writer(fh, lineterminator='\n'); wr.writerow(['key', 'file_changed', 'before(effective_from,effective_to,value)', 'after'])
    for k, fn, b, s in report: wr.writerow([k, fn, json.dumps(b, ensure_ascii=False), json.dumps(s, ensure_ascii=False)])
    for fn, k, what in LOG: wr.writerow([k, fn, 'specific fix', what])
print('keys fixed', len({r[0] for r in report}), 'file-key rewrites', len(report), 'files', sorted(changed))

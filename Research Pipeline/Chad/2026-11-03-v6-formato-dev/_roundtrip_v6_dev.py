"""Round trip of the v6 export in the Dev format + structural diff against the Dev export.

1. Reads back x-v6/*.md with _leitor_dev_md.py (as a loader would) — no access to the writer.
2. Structure: every regulation, flag, matrix file and the Tax Table read back = the v6 build (_build_v6.py).
3. Numbers: the 12 scenarios + 26 extra checks of _build_v6.py run on the regulations READ FROM THE .md,
   with the v6 engine; every account of every case must be identical (==) to the v6 run, and the six
   results must equal the expected hand-computed values.
4. Information only: the same files through the Dev engine model (simulacao/sim_dev.py, assumptions S1-S12).
5. Writes ROUNDTRIP-run.txt and DIFF-vs-Dev.md.
Run:  python -I _roundtrip_v6_dev.py      (exit 0 only if 1-3 pass)
"""
import importlib.util, os, sys

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
CHAD = os.path.dirname(HERE)
V6_BUILD = os.path.join(CHAD, '2026-11-02-design-v6', '_build_v6.py')
EXP = os.path.join(CHAD, '2026-10-29-teste-design-hrblizz', '2026-10-30-export-ram')
DEV_X = os.path.join(EXP, 'x')
SIM_DEV = os.path.join(EXP, 'simulacao', 'sim_dev.py')
X6 = os.path.join(HERE, 'x-v6')


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b6 = load('build_v6', V6_BUILD)
L = load('leitor_dev_md', os.path.join(HERE, '_leitor_dev_md.py'))
NUMK = ('f', 't', 'ee', 'er', 'floor', 'ceil')
ENGK = ('f', 't', 'ee', 'er', 'floor', 'ceil', 'credit', 'formula', 'assertion', 'ceilacc', 'deb', 'cred')


def bt(b):
    return tuple('' if b[k] == '' else (float(b[k]) if k in NUMK else str(b[k])) for k in ENGK)


def sm(m):
    return sorted([tuple(x[:3]) for x in m], key=lambda x: (int(x[0]), x[1]))


out, fail = [], 0


def check(label, ok, detail=''):
    global fail
    fail += not ok
    out.append(f"{'OK  ' if ok else 'FAIL'} {label}" + (f' — {detail}' if detail else ''))


# ------------------------------------------------------------------ 1-2 structure
P = L.read_design(os.path.join(X6, '2  CT-A-588-v6.md'))
S = L.read_spec(os.path.join(X6, '1  CT-A-580-v6.md'))
out.append('# Round trip — Chad v6 in the Dev export format (x-v6/*.md read back)')
out.append('')
out.append('## Structure')
check('regulations read back', [r['id'] for r in P] == [r['id'] for r in b6.R], f'{len(P)} / {len(b6.R)}, same order')
bad = []
for r, p in zip(b6.R, P):
    for k in ('id', 'ord', 'name', 'group', 'trg', 'ttype', 'pre'):
        if str(r[k]) != str(p[k]):
            bad.append((r['id'], k))
    if [bt(b) for b in r['bands']] != [bt(b) for b in p['bands']]:
        bad.append((r['id'], 'bands'))
    if sm(r['matrix']) != sm(p['matrix']):
        bad.append((r['id'], 'matrix'))
    if (p['currency'], p['tax_years'], p['status']) != ('XAF', 'td_2026', 'active'):
        bad.append((r['id'], 'classification'))
nb = sum(len(r['bands']) for r in b6.R)
nm = sum(len(r['matrix']) for r in b6.R)
check('every regulation field read back = v6 (id, ordinal, name, groups, type, pre-condition, bands, matrix)', not bad,
      f'36 regulations, {nb} bands, {nm} matrix rows' + (f'; differences {bad}' if bad else ''))
fl = {a: f for a, n, f, v in b6.FLAGS}
check('flag formulas read back = v6', S['flags'] == fl, f"{len(S['flags'])} / {len(fl)} flags")
dbad = []
for row, p in zip(S['design'], P):
    pairs = [(b['deb'], b['cred']) for b in p['bands']]
    if len(set(pairs)) == 1:
        pairs = pairs[:1]
    if (row['ord'], row['id'], row['name'], row['group'], row['trg'], row['ttype'], row['deb'], row['cred']) != \
            (p['ord'], p['id'], p['name'], p['group'], p['trg'], p['ttype'], [x[0] for x in pairs], [x[1] for x in pairs]):
        dbad.append(row['id'])
check('Design table of the spec = New Design', len(S['design']) == len(P) and not dbad, f"{len(S['design'])} rows" + (f'; differ {dbad}' if dbad else ''))
PR = {p['id']: p for p in P}
mfiles = sorted(f for f in os.listdir(X6) if f[0] in '345678')
for f in mfiles:
    title, rows = L.read_matrix(os.path.join(X6, f))
    with open(os.path.join(X6, f), encoding='utf-8') as fh:
        used = [int(x) for x in fh.read().split('**Used by:** ')[1].split(',')]
    ok = all(sm(rows) == sm(PR[u]['matrix']) for u in used)
    check(f'matrix file {f} = inline matrix of {used}', ok, f'{len(rows)} rows')
tt = L.read_tax_table(os.path.join(X6, '9  CT-A-582-v6.md'))
check('Tax Table file = bands of 9148211', tt == [(float(b['f']), float(b['t']), float(b['ee'])) for b in PR[9148211]['bands']], f'{len(tt)} bands')
# no forbidden words in the generated files
import re
words = re.compile(r'Claude|\bDev\b|\bv5\b|ASSUMPTIONS|correcoes|front decision|the front')
hits = []
for f in os.listdir(X6):
    with open(os.path.join(X6, f), encoding='utf-8') as fh:
        hits += [(f, m.group(0)) for m in words.finditer(fh.read())]
check('no internal words (Claude, Dev, v5, ASSUMPTIONS, correcoes, front) in x-v6', not hits, repr(hits[:5]) if hits else '9 files')

# ------------------------------------------------------------------ 3 numbers
ENG_R = [dict(id=p['id'], ord=p['ord'], name=p['name'], trg=p['trg'], ttype=p['ttype'], pre=p['pre'], group=p['group'], matrix=[tuple(m) for m in p['matrix']],
              bands=[{k: b[k] for k in ENGK} for b in p['bands']]) for p in P]
ORIG_R, ORIG_F = b6.R, b6.FLAG_F


def run_case(regs, flagf, inp, fo):
    b6.R, b6.FLAG_F = regs, flagf
    try:
        return b6.outcome(inp, fo)
    finally:
        b6.R, b6.FLAG_F = ORIG_R, ORIG_F


out += ['', '## Numbers (v6 engine on the regulations read from the .md vs v6 build)', '',
        '| Case | EE CNPS | IRPP | TFE | TAFP | PSA | Net | = expected | accounts identical |', '| --- | --- | --- | --- | --- | --- | --- | --- | --- |']
tot_vals, res = 0, {}
for title, sc in (('12 scenarios', b6.SCEN), ('26 extra checks', b6.EXTRA)):
    ok_n = 0
    for name, inp, fo, exp in sc:
        g6, A6 = run_case(ORIG_R, ORIG_F, inp, fo)
        gm, Am = run_case(ENG_R, S['flags'], inp, fo)
        keys = set(A6) | set(Am)
        same = all(A6.get(k, 0.0) == Am.get(k, 0.0) for k in keys) and set(A6) == set(Am)
        tot_vals += len(keys)
        expok = all(abs(a - e) < 0.005 for a, e in zip(gm, exp))
        ok_n += same and expok and tuple(g6) == tuple(gm)
        out.append(f"| {name} | " + ' | '.join(f'{x:,.0f}' if x == int(x) else f'{x:,.2f}' for x in gm) +
                   f" | {'yes' if expok else 'NO'} | {'yes' if same else 'NO'} ({len(keys)}) |")
    res[title] = (ok_n, len(sc))
for t, (a, b) in res.items():
    check(f'{t}: identical to v6, account by account, and = expected', a == b, f'{a}/{b}')
out.append(f'values compared (every account of every case): {tot_vals}')

# ------------------------------------------------------------------ 4 Dev engine model (information)
sd = load('sim_dev', SIM_DEV)
TD = [dict(ordinal=p['ord'], name=p['name'], assertion=p['pre'], taxRuleGroup=p['trg'], taxationType=p['ttype'],
           taxabilityRules=[dict(account=a, pattern=pt or None, isTaxable=(y == 'Yes')) for a, pt, y in p['matrix']],
           bands=[dict(incomeFrom=b['f'] if b['f'] != '' else 0.0, incomeTo=b['t'] if b['t'] != '' else None,
                       employeeRate=None if b['ee'] == '' else b['ee'], employerRate=None if b['er'] == '' else b['er'],
                       floorAmount=None if b['floor'] == '' else b['floor'], ceilingAmount=None if b['ceil'] == '' else b['ceil'],
                       formula=b['formula'] or None, assertion=b['assertion'] or None, debitAccount=b['deb'], creditAccount=b['cred'])
                  for b in p['bands']]) for p in sorted(P, key=lambda p: p['ord'])]
simdiff = []
for name, inp, fo, exp in b6.SCEN + b6.EXTRA:
    f = dict(b6.RES)
    f.update(fo)
    for d in b6.DERIVED:
        f[d] = float(b6.ev(S['flags'][d], {k: float(v) for k, v in f.items()}))
    A = sd.run_dev(inp, f, TD)
    _, A6 = b6.outcome(inp, fo)
    dk = [k for k in sorted(set(A) | set(A6)) if k not in f and k not in inp and abs(A.get(k, 0) - A6.get(k, 0)) > 0.005]
    if dk:
        simdiff.append(f"{name.split()[0]}: " + ', '.join(f'{k} v6 {A6.get(k, 0):,.2f} / Dev model {A.get(k, 0):,.2f}' for k in dk))
out += ['', '## Information only: the same .md through the Dev engine model (simulacao/sim_dev.py, S1-S12)', '',
        f'cases with any account different: {len(simdiff)} of {len(b6.SCEN) + len(b6.EXTRA)}'] + ['  ' + x for x in simdiff]
out += ['', 'RESULT: ' + ('ROUND TRIP 100% IDENTICAL' if not fail else f'{fail} CHECK(S) FAILED')]
with open(os.path.join(HERE, 'ROUNDTRIP-run.txt'), 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('\n'.join(out) + '\n')

# ------------------------------------------------------------------ 5 diff against the Dev export
D = {r['id']: r for r in L.read_design(os.path.join(DEV_X, '2  CT-A-588.md'))}
DS = L.read_spec(os.path.join(DEV_X, '1  CT-A-580.md'))


def mdelta(ours, dev):
    o = {(a, p): y for a, p, y, *_ in ours}
    d = {(a, p): y for a, p, y, *_ in dev}
    same = [k for k in o if k in d and o[k] == d[k]]
    chg = [k for k in o if k in d and o[k] != d[k]]
    add = [k for k in o if k not in d]
    rem = [k for k in d if k not in o]
    return same, chg, add, rem


def kstr(ks, o=None):
    return ', '.join((p or a) + (f' {o[(a, p)]}' if o else '') for a, p in sorted(ks, key=lambda k: (int(k[0]), k[1])))


def g(v):
    if v == '' or v is None:
        return '—'
    if isinstance(v, float):
        return str(int(v)) if v.is_integer() else repr(v)
    return str(v)


def band_detail(r, d):
    if len(r['bands']) != len(d['bands']):
        return f"bands {len(d['bands'])} → {len(r['bands'])}"
    lab = dict(f='incomeFrom', t='incomeTo', ee='EE rate', er='ER rate', floor='floor', ceil='ceiling', formula='formula', assertion='band assertion', deb='debit', cred='credit')
    det = []
    for i, (x, y) in enumerate(zip(r['bands'], d['bands'])):
        for k in lab:
            xv, yv = bt(x)[ENGK.index(k)], bt(y)[ENGK.index(k)]
            if xv != yv:
                det.append(f"b{i + 1} {lab[k]}: `{g(y[k])}` → `{g(x[k])}`")
    return '; '.join(det)


rows, cnt = [], dict(SAME=0, CHANGED=0, NEW=0, REMOVED=0)
for p in P:
    if p['id'] not in D:
        cnt['NEW'] += 1
        rows.append(f"| {p['id']} | {p['name']} | NEW | no pair in the Dev design |")
        continue
    d = D[p['id']]
    what = []
    for k, lab in (('name', 'name'), ('ord', 'ordinal'), ('group', 'tax group'), ('trg', 'rule group'), ('ttype', 'taxation type')):
        if str(p[k]) != str(d[k]):
            what.append(f"{lab}: `{d[k]}` → `{p[k]}`")
    if p['pre'] != d['pre']:
        what.append(f"pre-condition: `{d['pre'] or '—'}` → `{p['pre'] or '—'}`")
    bd = band_detail(p, d)
    if bd:
        what.append(bd)
    s_, c_, a_, r_ = mdelta(p['matrix'], d['matrix'])
    if c_ or a_ or r_:
        what.append(f'matrix: {len(s_)} same, {len(c_)} flag changed, {len(a_)} added, {len(r_)} removed')
    st = 'CHANGED' if what else 'SAME'
    cnt[st] += 1
    rows.append(f"| {p['id']} | {p['name']} | {st} | {'<br>'.join(what) or '—'} |")
for i in D:
    if i not in PR:
        cnt['REMOVED'] += 1
        rows.append(f"| {i} | {D[i]['name']} | REMOVED | replaced by 9148192 (base 58552 after 9148191; non-resident on the progressive scale) |")
mrows = []
for f in mfiles:
    dev_f = f.replace('-v6', '')
    _, ours = L.read_matrix(os.path.join(X6, f))
    _, dev = L.read_matrix(os.path.join(DEV_X, dev_f))
    s_, c_, a_, r_ = mdelta(ours, dev)
    o = {(a, p): y for a, p, y, _ in ours}
    mrows.append(f"| {f[3:-3]} vs {dev_f[3:-3]} | {len(s_)} | {len(c_)}{(': ' + kstr(c_, o)) if c_ else ''} | {len(a_)}{(': ' + kstr(a_, o)) if a_ else ''} | {len(r_)}{(': ' + kstr(r_)) if r_ else ''} |")
dtt = L.read_tax_table(os.path.join(DEV_X, '9  CT-A-582.md'))
ttrow = 'same rates (0 / 10.5 / 15 / 20 / 25 / 30); limits changed: ' + ', '.join(f'{g(a[0])}–{g(a[1])} → {g(b[0])}–{g(b[1])}' for a, b in zip(dtt, tt) if a[:2] != b[:2]) \
    if [x[2] for x in dtt] == [x[2] for x in tt] else 'rates differ'
frows = []
dflags = DS['flags']
for a, n_, f_, v in b6.FLAGS:
    if a not in dflags:
        frows.append(f'| {a} | {n_} | NEW | `{f_}` |')
    elif dflags[a].startswith(f_):
        frows.append(f'| {a} | {n_} | SAME | `{f_}` |')
    else:
        frows.append(f'| {a} | {n_} | CHANGED | Dev `{dflags[a]}` → `{f_}` |')
for a in dflags:
    if a not in fl:
        frows.append(f'| {a} | — | REMOVED | Dev `{dflags[a]}` |')
D_L = ['# DIFF — Chad v6 (test set) × Dev export CT-A-580..588', '',
       f'Generated by `_roundtrip_v6_dev.py` from the files themselves (x-v6/ × ../2026-10-29-teste-design-hrblizz/2026-10-30-export-ram/x/). Status by regulation ID: '
       f"SAME {cnt['SAME']} · CHANGED {cnt['CHANGED']} · NEW {cnt['NEW']} · REMOVED {cnt['REMOVED']} (v6: {len(P)} regulations; Dev: {len(D)}).", '',
       '## Regulations', '', '| ID | Name (v6) | Status | What differs (Dev → v6) |', '| --- | --- | --- | --- |'] + rows + \
      ['', '## Matrix files (rows keyed by account + pattern)', '', '| File | Same | Taxable flag changed | Added in v6 | Removed in v6 |', '| --- | --- | --- | --- | --- |'] + mrows + \
      ['', '## Tax Table', '', f'9  CT-A-582-v6 vs 9  CT-A-582: {ttrow}.', '',
       '## Flags', '', '| Account | Flag (v6) | Status | Formula |', '| --- | --- | --- | --- |'] + frows + ['']
with open(os.path.join(HERE, 'DIFF-vs-Dev.md'), 'w', encoding='utf-8', newline='\n') as fh:
    fh.write('\n'.join(D_L))

print('\n'.join(x for x in out if not x.startswith('| ')))
sys.exit(1 if fail else 0)

"""QA r1 fix (agent 2): collapse alias keys to one canonical key per fact across every _research/*-facts.json.

Alias = same register_id + same value + same effective_from AND same meaning (normalised key words equal,
differ only by filler words, both are oracle results of the same worked example, or listed by hand in
manual_alias_sets.json after a human read of the group). Groups that only share a number are left alone.

Canonical choice, in order: key carried in a CCG facts file; jurisdiction-first key (not multi./rspec./sir./psl./dd.);
'pit' over 'sit'/'wh'; most fact objects; shortest; alphabetical.
Writes _research/qa-r1-fix/KEY-ALIAS-MAP.csv and rewrites the facts files in place (backups already taken).
Usage: python -I alias_apply.py <BASE> <alias.json from alias_scan.py> [--dry]
"""
import csv, collections, glob, json, os, sys

BASE, ALIAS = sys.argv[1], sys.argv[2]
DRY = '--dry' in sys.argv
R = os.path.join(BASE, '_research')
HERE = os.path.dirname(os.path.abspath(__file__))
PREF = ('multi.', 'rspec.', 'sir.', 'psl.', 'dd.', 'wtc.')

files = sorted(glob.glob(os.path.join(R, '*-facts.json')))
data = {f: json.load(open(f, encoding='utf-8')) for f in files}
occ = collections.Counter()
in_ccg = set()
where = collections.defaultdict(set)
for f, d in data.items():
    for x in d['facts']:
        occ[x['key']] += 1
        where[x['key']].add(os.path.basename(f))
        if os.path.basename(f).startswith('CCG-'):
            in_ccg.add(x['key'])

par = {}
def find(x):
    par.setdefault(x, x)
    while par[x] != x:
        par[x] = par[par[x]]
        x = par[x]
    return x
def union(a, b):
    par[find(a)] = find(b)

al = json.load(open(ALIAS, encoding='utf-8'))
basis = {}
for grp, ks, _fs in al['alias']:
    for k in ks[1:]:
        union(ks[0], k)
    for k in ks:
        basis.setdefault(k, 'normalised key words equal / oracle result of the same example')
for ks in json.load(open(os.path.join(HERE, 'manual_alias_sets.json'), encoding='utf-8')):
    missing = [k for k in ks if k not in occ]
    if missing:
        print('MANUAL SET KEY NOT FOUND', missing)
        continue
    for k in ks[1:]:
        union(ks[0], k)
    for k in ks:
        basis[k] = 'manual read of the group: same register row, value and date, same meaning'

comp = collections.defaultdict(set)
for k in list(par):
    comp[find(k)].add(k)

def score(k):
    toks = k.split('.')
    return (0 if k in in_ccg else 1, 1 if k.startswith(PREF) else 0,
            1 if ('sit' in toks or 'wh' in toks) else 0, -occ[k], len(k), k)

ren = {}
for ks in comp.values():
    if len(ks) < 2:
        continue
    can = sorted(ks, key=score)[0]
    for k in ks:
        if k != can:
            ren[k] = can

rows = []
changed = collections.Counter()
conflicts = []
for f, d in data.items():
    bn = os.path.basename(f)
    seen = {}
    out = []
    for x in d['facts']:
        k = x['key']
        if k in ren:
            x['key'] = ren[k]
            x['_renamed_from'] = k
            changed[bn] += 1
        sig = (x['key'], x.get('effective_from'), x.get('effective_to'))
        if sig in seen:
            prev = seen[sig]
            if json.dumps(prev['value']) == json.dumps(x['value']) and prev['register_id'] == x['register_id']:
                continue  # exact duplicate after rename: drop
            conflicts.append((bn, x['key'], prev['value'], x['value']))
        seen[sig] = x
        out.append(x)
    d['facts'] = out
    for u in d.get('unresolved', []):
        if u.get('key') in ren:
            u['_renamed_from'] = u['key']
            u['key'] = ren[u['key']]
            changed[bn] += 1

for old, new in sorted(ren.items()):
    rows.append({'old_key': old, 'canonical_key': new, 'old_key_files': ';'.join(sorted(where[old])),
                 'canonical_key_files_before': ';'.join(sorted(where[new])), 'basis': basis.get(old, ''),
                 'action': 'renamed in facts files on 2026-11-02; builders re-point [[FACT:old_key=...]] tags to canonical_key'})

print('components', sum(1 for v in comp.values() if len(v) > 1), 'renamed keys', len(ren),
      'files changed', len(changed), 'conflicts', len(conflicts))
for c in conflicts[:30]:
    print('CONFLICT', c)
if not DRY:
    with open(os.path.join(R, 'qa-r1-fix', 'KEY-ALIAS-MAP.csv'), 'w', encoding='utf-8', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)
    for f, d in data.items():
        if changed[os.path.basename(f)]:
            json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(json.dumps(changed, indent=0))

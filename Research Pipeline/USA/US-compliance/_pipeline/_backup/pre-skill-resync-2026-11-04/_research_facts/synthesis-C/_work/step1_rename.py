# Synthesis C step 1: register id normalization. Usage: python -I step1_rename.py <BASE>
import csv, re, os, sys, shutil, json, glob, collections
BASE = sys.argv[1]
REG = os.path.join(BASE, '00-official-sources', 'legal-basis-register.csv')
RES = os.path.join(BASE, '_research')
BK = os.path.join(RES, 'synthesis-C', '_backup')
PAT = re.compile(r'^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$')
def backup(p):
    rel = os.path.relpath(p, BASE)
    dst = os.path.join(BK, rel)
    if os.path.exists(dst): return
    os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy2(p, dst)
rows = list(csv.DictReader(open(REG, encoding='utf-8', newline='')))
FIELDS = list(rows[0].keys())
ids = {r['id'] for r in rows}
m = {}; short = []
for r in rows:
    i = r['id']
    if PAT.match(i): continue
    p = i.split('-')
    mid = ''.join(p[1:-1]); new = f'{p[0]}-{mid}-{p[-1]}'
    if len(mid) > 12 or new in ids or new in m.values() or not PAT.match(new):
        raise SystemExit(f'needs shortening: {i} -> {new}')
    m[i] = new
os.makedirs(os.path.join(RES, 'stage5'), exist_ok=True)
with open(os.path.join(RES, 'stage5', 'ID-RENAME-MAP.csv'), 'w', encoding='utf-8', newline='') as f:
    w = csv.writer(f, lineterminator='\n'); w.writerow(['old_id', 'new_id', 'status_at_rename'])
    st = {r['id']: r['status'] for r in rows}
    for k, v in m.items(): w.writerow([k, v, st[k]])
alts = sorted(m, key=len, reverse=True)
RX = re.compile(r'(?<![A-Za-z0-9-])(' + '|'.join(re.escape(a) for a in alts) + r')(?![A-Za-z0-9])')
def sub(s): return RX.subn(lambda mo: m[mo.group(1)], s)
# register
backup(REG)
cnt = collections.Counter()
for r in rows:
    for c in FIELDS:
        new, n = sub(r[c])
        if n: cnt[c] += n; r[c] = new
with open(REG, 'w', encoding='utf-8', newline='') as f:
    w = csv.DictWriter(f, fieldnames=FIELDS, lineterminator='\n'); w.writeheader(); w.writerows(rows)
print('register replacements per column', dict(cnt))
# research files
files = []
for ext in ('json', 'md', 'py', 'csv', 'txt'):
    files += glob.glob(os.path.join(RES, '**', f'*.{ext}'), recursive=True)
tot = 0; per = {}
for p in files:
    rel = os.path.relpath(p, RES).replace(os.sep, "/")
    if '_backup' in rel or rel.startswith('synthesis-C/') or rel == 'stage5/ID-RENAME-MAP.csv' or '__pycache__' in rel: continue
    s = open(p, encoding='utf-8').read()
    new, n = sub(s)
    if n:
        backup(p); open(p, 'w', encoding='utf-8', newline='').write(new); per[rel] = n; tot += n
json.dump(per, open(os.path.join(RES, 'synthesis-C', '_work', 'step1-file-counts.json'), 'w'), indent=0)
print('renamed ids', len(m), 'files changed', len(per), 'occurrences', tot)
# scaffolder-owned files: count only
sc = {}
for rel in ('00-official-sources/MANDATE.md', '_pipeline/build-manifest.json', 'SKELETON-MANIFEST.md'):
    p = os.path.join(BASE, rel)
    if os.path.exists(p):
        s = open(p, encoding='utf-8').read(); hits = collections.Counter(mo.group(1) for mo in RX.finditer(s))
        sc[rel] = {'occurrences': sum(hits.values()), 'distinct_ids': len(hits)}
json.dump(sc, open(os.path.join(RES, 'synthesis-C', '_work', 'step1-scaffolder-counts.json'), 'w'), indent=1)
print('scaffolder files', sc)

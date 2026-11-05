# Synthesis C step 2b: align research packs with promoted facts. Usage: python -I step2b_packs.py <BASE>
import os, re, sys, json, glob, shutil
BASE = sys.argv[1]; RES = os.path.join(BASE, '_research'); BK = os.path.join(RES, 'synthesis-C', '_backup')
def backup(p):
    dst = os.path.join(BK, os.path.relpath(p, BASE))
    if not os.path.exists(dst):
        os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy2(p, dst)
BANNER = ('> **Synthesis C (2026-11-02).** Register ids were normalized to the facts-schema pattern '
          '(map: `_research/stage5/ID-RENAME-MAP.csv`, ids in this pack already rewritten). Every fact that was held for the '
          'register_id pattern defect (marked here as "legacy id, NOT a fact", "PENDING", "(P)", "parked" or "carried in unresolved") '
          'is now a validated fact in `facts[]`; promotion log `_research/synthesis-C/_work/step2-promotion-log.csv`. '
          'Counts of held facts quoted below are historical. The Open questions block below mirrors the current `unresolved[]`.')
stats = {}
for fp in sorted(glob.glob(os.path.join(RES, '*-facts.json'))):
    fn = os.path.basename(fp)
    if re.match(r'CCG-(m\d\d_|coverage)', fn): continue
    bkf = os.path.join(BK, os.path.relpath(fp, BASE))
    if not os.path.exists(bkf): continue
    old = {u['key'] for u in json.load(open(bkf, encoding='utf-8'))['unresolved']}
    cur = {u['key'] for u in json.load(open(fp, encoding='utf-8'))['unresolved']}
    removed = old - cur
    stem = fn.replace('-facts.json', '')
    cands = [os.path.join(RES, stem + '-research-pack.md')]
    if stem.startswith('WTC-'): cands = [os.path.join(RES, 'WTC-research-pack.md')]
    if stem.startswith('DD-'): cands = [os.path.join(RES, 'DD-research-pack.md')]
    for pp in cands:
        if not os.path.exists(pp): continue
        s = open(pp, encoding='utf-8').read(); s0 = s
        s = s.replace('— legacy id, NOT a fact]', '— promoted to fact in Synthesis C]')
        s = re.sub(r'\s*\(PENDING id pattern\)', ' (promoted, Synthesis C)', s)
        s = s.replace('— PENDING register_id pattern', '— promoted to fact in Synthesis C')
        # drop open-question bullets for keys no longer unresolved
        lines = s.split('\n'); out = []; inoq = False; dropped = 0
        for ln in lines:
            if ln.startswith('## Open questions'): inoq = True
            elif ln.startswith('## ') : inoq = False
            if inoq and ln.startswith('- '):
                m = re.match(r'- (?:\*\*)?`?([a-z][a-z0-9_.]+)`?(?:\*\*)?', ln)
                if m and m.group(1) in removed:
                    dropped += 1; continue
            out.append(ln)
        s = '\n'.join(out)
        if 'Synthesis C (2026-11-02)' not in s:
            i = s.find('\n')
            s = s[:i + 1] + '\n' + BANNER + '\n' + s[i + 1:]
        if s != s0:
            backup(pp); open(pp, 'w', encoding='utf-8', newline='').write(s)
            st = stats.setdefault(os.path.basename(pp), {'oq_dropped': 0}); st['oq_dropped'] += dropped
json.dump(stats, open(os.path.join(RES, 'synthesis-C', '_work', 'step2b-packs.json'), 'w'), indent=1)
print(len(stats), 'packs updated;', sum(v['oq_dropped'] for v in stats.values()), 'open-question lines dropped')

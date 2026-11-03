# -*- coding: utf-8 -*-
"""Release of the Colombia finals, issue 2026-11-02 round 6 (text only): CCG v1.7, WTC v1.9, DD v1.6, CO-DIAN-004 v1.3,
from the DRAFT-R6 of revisao/rodada6/ (apply_r6.py). Same method as release_r5.py, reusing release.py unchanged:
xlsx = highlight FFDDEBF7 removed (no other edit: the DRAFT-R6 already carries the final text and Version Control row);
docx = all tracked changes accepted; issue metadata = 2026-11-02.
The finals they replace are MOVED first to final/_historico/2026-11-02-r5/ (with a copy of MD5-FINAIS.txt).
Then a cross-check proves, cell by cell and paragraph by paragraph, that each new final differs from the final it
replaces ONLY at the edits logged by apply_r6.py, with the logged text, and that no highlight / tracked change is left.
Usage: python -I final/scripts/release_r6.py
"""
import os, re, sys, json, shutil, hashlib, zipfile, calendar, time
HERE = os.path.dirname(os.path.abspath(__file__)); VAL = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import release as R, colib
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(VAL)
ISSUE = '2026-11-02'
R.DAY = ISSUE; R.STAMP = ISSUE + 'T09:00:00Z'; R.AUTHOR = 'Wallisson Gomes'
R.EPOCH = calendar.timegm(time.strptime(ISSUE + ' 09:00:00', '%Y-%m-%d %H:%M:%S'))
R.LOG = []
FIN = 'final/'; HIST = 'final/_historico/2026-11-02-r5/'; R6 = 'revisao/rodada6/'
md5 = lambda p: hashlib.md5(open(p, 'rb').read()).hexdigest()

PAIRS = [  # (art, draft, old final (moved), new final)
 ('CCG', R6 + 'CO-CCG-001-v1.7-DRAFT-R6.docx', 'CO-CCG-001-v1.6.docx', 'CO-CCG-001-v1.7.docx'),
 ('WTC', R6 + 'CO-WTC-001-v1.9-DRAFT-R6.xlsx', 'CO-WTC-001-v1.8.xlsx', 'CO-WTC-001-v1.9.xlsx'),
 ('DD', R6 + 'CO-DD-001-v1.6-DRAFT-R6.xlsx', 'CO-DD-001-v1.5.xlsx', 'CO-DD-001-v1.6.xlsx'),
 ('F220', R6 + 'CO-DIAN-004-Formulario220-Spec-v1.3-DRAFT-R6.xlsx', 'specs/CO-DIAN-004-Formulario220-Spec.xlsx', 'specs/CO-DIAN-004-Formulario220-Spec.xlsx'),
]


def read_md5(p):
    out = {}
    for ln in open(p, encoding='utf-8'):
        if ln.startswith('#') or not ln.strip(): continue
        h, f = ln.split(None, 1); out[f.strip()] = h
    return out


# 1. move the replaced finals
if not os.path.exists(HIST + 'MD5-FINAIS.txt'):
    cur = read_md5(FIN + 'MD5-FINAIS.txt')
    for _, _, old, _ in PAIRS:
        assert md5(FIN + old) == cur[old], 'final alterado: ' + old
    os.makedirs(HIST + 'specs', exist_ok=True)
    for _, _, old, _ in PAIRS:
        shutil.move(FIN + old, HIST + old)
    shutil.copy2(FIN + 'MD5-FINAIS.txt', HIST + 'MD5-FINAIS.txt')
    print('moved', len(PAIRS), 'finals to', HIST)
prev = read_md5(HIST + 'MD5-FINAIS.txt')
for _, _, old, _ in PAIRS:
    assert md5(HIST + old) == prev[old], 'historico alterado: ' + old

# 2. release
for art, d, old, new in PAIRS:
    if new.endswith('.docx'):
        n0 = R.docx_release(art, d, FIN + new, [])
        print(f'{art:5} {new}: {n0} tracked changes accepted')
    else:
        st, pok, nadd = R.xlsx_release(art, d, HIST + old, FIN + new, {})
        print(f'{art:5} {new}: highlight removed {st} (base styles usable: {pok}; new xf {nadd})')

# 3. cross-check: old final -> new final differs only at the logged edits
log = json.load(open(R6 + 'apply_r6_log.json', encoding='utf-8'))
fails = []
for art, d, old, new in PAIRS:
    mine = [e for e in log if e['art'] == art]
    if new.endswith('.xlsx'):
        a = {(s, r): v for s, r, v, f, st in colib.xlsx_cells(HIST + old)}
        b = {(s, r): v for s, r, v, f, st in colib.xlsx_cells(FIN + new)}
        diff = {k for k in set(a) | set(b) if (a.get(k) or '') != (b.get(k) or '')}
        decl = {}
        for e in mine:
            sh, ref = e['where'].split('!'); decl[(sh, ref)] = e['after']
        if diff != set(decl): fails.append((art, 'cells differ', sorted(diff ^ set(decl))))
        for k, v in decl.items():
            if str(b.get(k)) != str(v): fails.append((art, k, 'text', b.get(k), v))
        z = zipfile.ZipFile(FIN + new); blue = colib.blue_xfs(z); z.close()
        nb = sum(1 for s, r, v, f, st in colib.xlsx_cells(FIN + new) if st in blue)
        if nb: fails.append((art, 'highlight left', nb))
        print(f'{art:5} cells changed {len(diff)} = declared {len(decl)}; highlight left {nb}')
    else:
        pa = colib.docx_paras(HIST + old, accept=False); pb = colib.docx_paras(FIN + new, accept=False)
        import difflib
        sm = difflib.SequenceMatcher(None, pa, pb, autojunk=False)
        ch = [(t, pa[i1:i2], pb[j1:j2]) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != 'equal']
        afters = [e['after'] for e in mine if e['where'] not in ('word/footer1.xml',) and not e['where'].startswith('T1 new row')]
        row = [e for e in mine if e['where'].startswith('T1 new row')][0]['after'].split(' | ')
        newp = [p for t, x, y in ch for p in y]
        # every changed/new paragraph must be a logged 'after' text (last edit per paragraph) or a cell of the new row
        lastafter = {}
        for e in mine:
            if e['where'] not in ('word/footer1.xml',) and not e['where'].startswith('T1 new row'): lastafter[e['where']] = e['after']
        allowed = set(lastafter.values()) | set(row)
        bad = [p for p in newp if p not in allowed]
        if bad: fails.append((art, 'unexpected paragraph', bad))
        if len(newp) != len(lastafter) + len(row): fails.append((art, 'paragraph count', len(newp), len(lastafter) + len(row)))
        x = zipfile.ZipFile(FIN + new).read('word/document.xml').decode('utf-8')
        if re.search(r'<w:(ins|del) |<w:delText', x): fails.append((art, 'tracked change left'))
        ft = ''.join(re.findall(r'<w:t[^>]*>([^<]*)', zipfile.ZipFile(FIN + new).read('word/footer1.xml').decode('utf-8')))
        if 'CO-CCG-001 v1.7 |' not in ft: fails.append((art, 'footer'))
        print(f'{art:5} paragraphs changed/added {len(newp)} = declared {len(lastafter)} edited + {len(row)} new-row cells; tracked left: {bool(re.search(r"<w:(ins|del) ", x))}')

# 4. MD5-FINAIS
cur = read_md5(FIN + 'MD5-FINAIS.txt') if os.path.exists(FIN + 'MD5-FINAIS.txt') else {}
lines = []
for f, h in prev.items():
    rep = [p for p in PAIRS if p[2] == f]
    if rep: f = rep[0][3]
    lines.append(f'{md5(FIN + f)}  {f}')
with open(FIN + 'MD5-FINAIS.txt', 'w', encoding='utf-8') as o:
    o.write('# MD5 dos finais (emissão 2026-11-02, rodada 6: CCG v1.7, WTC v1.9, DD v1.6, CO-DIAN-004 v1.3, só texto; os demais sem mudança desde a rodada 5); gerado por final/scripts/release_r6.py\n')
    o.write('\n'.join(lines) + '\n')
print('FAILS' if fails else 'PASS', json.dumps(fails, ensure_ascii=False, indent=1) if fails else '')

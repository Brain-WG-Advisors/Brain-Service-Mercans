# -*- coding: utf-8 -*-
"""Residuals corrected on the released CO finals before the Drive upload (issue 2026-11-02), after release_r5.py and
release_xref.py. Each final in release_r5_edits.RESID_BEFORE (md5 checked) is first copied to
final/_historico/2026-11-02-antes-residuos/; the declared edits (RESID for xlsx, RESID_DOCX for the docx) are applied
on that copy with release.py's surgery (xlsx: the edited cell becomes an inline string with the same style; docx:
paragraph edit on word/document.xml; no highlight, no tracked change; every other zip part byte for byte) and the
final is rewritten with the same issue metadata. Idempotent: an existing copy is reused (md5 checked).
Usage: python -I final/scripts/release_residuos.py
"""
import os, sys, json, shutil, hashlib, calendar, time
HERE = os.path.dirname(os.path.abspath(__file__)); VAL = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
import release as R, release_r5_edits as E
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(VAL)
R.DAY = E.ISSUE; R.STAMP = E.ISSUE + 'T09:00:00Z'; R.AUTHOR = E.AUTHOR
R.EPOCH = calendar.timegm(time.strptime(E.ISSUE + ' 09:00:00', '%Y-%m-%d %H:%M:%S'))
R.LOG = []
md5 = lambda p: hashlib.md5(open(p, 'rb').read()).hexdigest()
PRE = 'final/_historico/2026-11-02-antes-residuos'
for art, (f, m) in E.RESID_BEFORE.items():
    pre = os.path.join(PRE, f); fin = os.path.join('final', f)
    os.makedirs(os.path.dirname(pre), exist_ok=True)
    if not os.path.exists(pre):
        assert md5(fin) == m, f'{f}: final differs from the one listed in MD5-FINAIS (10:12)'
        shutil.copy2(fin, pre)
    assert md5(pre) == m
    if f.endswith('.docx'):
        R.docx_release(art, pre, fin, E.RESID_DOCX[art])
        n = len(E.RESID_DOCX[art])
    else:
        R.xlsx_release(art, pre, pre, fin, E.RESID[art])
        n = len(E.RESID[art])
    print(f'{art}: {n} residual edits -> {fin} md5 {md5(fin)}')
R.LOG = [l for l in R.LOG if l[1] != 'comments']  # the released docx has no comment left (0 removed)
json.dump([dict(artifact=a, where=w, before=b, after=c) for a, w, b, c in R.LOG],
          open(os.path.join('final', 'scripts', 'release_residuos_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# -*- coding: utf-8 -*-
"""Cross-references updated to current versions (CO finals, issue 2026-11-02), applied on the released finals.
The released final (md5 in release_r5_edits.XREF_BEFORE) is first copied to final/_historico/2026-11-02-antes-xref/;
the declared XREF edits are applied on that copy with release.xlsx_release's cell surgery (the edited cell becomes an
inline string with the same style; no highlight; sharedStrings and every other zip part byte for byte), and the final
is rewritten with the same issue metadata. Idempotent: if the copy already exists (md5 checked) it is reused.
Usage: python -I final/scripts/release_xref.py
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
PRE = 'final/_historico/2026-11-02-antes-xref'
os.makedirs(PRE, exist_ok=True)
for art, (f, m) in E.XREF_BEFORE.items():
    pre = os.path.join(PRE, f); fin = os.path.join('final', f)
    if not os.path.exists(pre):
        assert md5(fin) == m, f'{f}: final differs from the released one'
        shutil.copy2(fin, pre)
    assert md5(pre) == m
    # xlsx_release on an already-released file: no highlight left, so only the declared edits change anything
    R.xlsx_release(art, pre, pre, fin, E.XREF[art])
    print(f'{art}: {len(E.XREF[art])} cross-references updated -> {fin} md5 {md5(fin)}')
json.dump([dict(artifact=a, where=w, before=b, after=c) for a, w, b, c in R.LOG],
          open(os.path.join('final', 'scripts', 'release_xref_log.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

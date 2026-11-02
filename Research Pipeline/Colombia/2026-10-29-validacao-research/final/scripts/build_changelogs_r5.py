# -*- coding: utf-8 -*-
"""Changelogs of the 2026-11-02 issue (CCG v1.6, WTC v1.8, DD v1.5, five specs v1.2, Payslip v1.3, SIR v1.3).
Each changelog in final/changelogs/ gets a new section 2026-11-02 at the top: release header, files and md5, every
change of the round-5 DRAFT against the version in force (revisao/rodada5/apply_r5_log.json: where, before, after,
source; includes the step-0 change on the 3,800-UVT cap) and what the release changed against the DRAFT-R5
(final/scripts/release_r5_log.json). The previous changelog follows verbatim. Versioned names are renamed to the new
version (one changelog per artifact). Idempotent: on a rerun the 2026-11-02 section is rebuilt, not duplicated.
Usage: python -I final/scripts/build_changelogs_r5.py
"""
import os, sys, json, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); VAL = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE); os.chdir(VAL)
import release_r5_edits as E
sys.stdout.reconfigure(encoding='utf-8')
md5 = lambda p: hashlib.md5(open(p, 'rb').read()).hexdigest()
A = json.load(open('revisao/rodada5/apply_r5_log.json', encoding='utf-8'))
RL = json.load(open('final/scripts/release_r5_log.json', encoding='utf-8'))
MARK = '<!-- fim da seção 2026-11-02 -->'
CL = 'final/changelogs/'
OLDNAME = {'CCG': 'CO-CCG-001-v1.5-CHANGELOG.md', 'WTC': 'CO-WTC-001-v1.7-CHANGELOG.md', 'DD': 'CO-DD-001-v1.4-CHANGELOG.md',
           'SIR': 'CO-SIR-001-v1.2-CHANGELOG.md'}
NEWNAME = {'CCG': 'CO-CCG-001-v1.6-CHANGELOG.md', 'WTC': 'CO-WTC-001-v1.8-CHANGELOG.md', 'DD': 'CO-DD-001-v1.5-CHANGELOG.md',
           'SIR': 'CO-SIR-001-v1.3-CHANGELOG.md'}
PREV = {'CCG': '1.5', 'WTC': '1.7', 'DD': '1.4', 'PAYSLIP': '1.2', 'SIR': '1.2'}
STEP0 = 'passo 0 de 2026-11-02'


def cut(s, n=500):
    s = (s or '').replace('|', '\\|').replace('\n', ' ⏎ ')
    return s if len(s) <= n else s[:n] + ' …'


def target(art, f):
    if art in NEWNAME: return CL + NEWNAME[art], CL + OLDNAME[art]
    n = CL + os.path.basename(f).rsplit('.', 1)[0] + '-CHANGELOG.md'
    return n, n


def previous(new, old):
    p = new if os.path.exists(new) else old
    t = open(p, encoding='utf-8').read()
    if MARK in t: t = t.split(MARK, 1)[1].lstrip('\n')
    return t, p


def section(art, name, v, final_rel, draft, base, kind):
    prev = PREV.get(art, '1.1')
    mine = [x for x in A if x['art'] == art]
    rel = [x for x in RL if x['artifact'] == art]
    n0 = sum(1 for x in mine if STEP0 in x['src'])
    L = ['> **Released 2026-11-02 — approved by Wallisson Gomes (Compliance Regulations Team Lead).** The section below is the '
         'review trail of this version; words such as "DRAFT" or "round 5" describe the state during review, before approval. '
         'The released file carries none of those marks (`final/RELEASE-CROSSCHECK-R5.md`).', '',
         f'# {name} (version {v}, issued 2026-11-02): changelog', '',
         f'- **Released file:** `{final_rel}` (md5 `{md5(final_rel)}`).',
         f'- **DRAFT-R5 (approved):** `{draft}` (md5 `{md5(draft)}`).',
         f'- **Version in force before this one:** `{base}` (version {prev}, issued 2026-10-30; md5 `{md5(base)}`).',
         '- **Method:** ' + kind, '',
         f'## 2026-11-02 (version {v}): changes against version {prev}', '',
         'Decisions of `pesquisa-2026-11-02/TABELA-RODADA5.md` applied by `revisao/rodada5/scripts/apply_r5.py` '
         '(full list with the before text in `revisao/rodada5/mudancas-RODADA5.md`; conference `revisao/rodada5/CONFERENCIA-R5.md`, PASS)'
         + (f'; {n0} change(s) of step 0 (the shared 3,800-UVT cap of voluntary pension funds and AFC / AVC accounts is annual, tracked year-to-date, with no monthly one-twelfth limit).' if n0 else '.'), '',
         '| # | Where | Before | After | Source |', '|---|---|---|---|---|']
    for i, x in enumerate(mine, 1):
        L.append(f"| {i} | {cut(x['where'], 80)} | {cut(x['before'])} | {cut(x['after'])} | {cut(x['src'], 400)} |")
    L += ['', '## Release 2026-11-02: what the release changed against the DRAFT-R5', '']
    if kind.startswith('XML surgery on the sheet'):
        L.append('- **Review highlight removed:** every cell with the fill `FFDDEBF7` gets back the style of the version in force (or the equivalent non-highlighted style of its column); no other formatting changes.')
    elif art == 'CCG':
        L.append('- **Tracked changes accepted** (author Wallisson Gomes); track changes switched off.')
    L += ['- **Issue metadata:** created = modified = 2026-11-02, revision 1, author Wallisson Gomes.' if art != 'SIR' else '- Text to paste in the Google Doc; review markers [R5] and the DRAFT header removed.', '',
          '| # | Where | Before (DRAFT-R5) | After (released) |', '|---|---|---|---|']
    for i, x in enumerate(rel, 1):
        L.append(f"| {i} | {cut(x['where'], 80)} | {cut(x['before'])} | {cut(x['after'])} |")
    return L, len(mine), n0


def write(art, new, old, L):
    body, src = previous(new, old)
    out = '\n'.join(L) + '\n\n' + MARK + '\n\n---\n\n' + body
    open(new, 'w', encoding='utf-8').write(out)
    if src != new and os.path.exists(src): os.remove(src)   # renamed: one changelog per artifact
    return src


tot = {}
for art, d, b, f, v in E.PAIRS:
    kind = ('all tracked changes accepted by XML surgery on word/document.xml (version also updated in the footer); every other part copied byte for byte.'
            if f.endswith('.docx') else 'XML surgery on the sheet parts and styles.xml; every other zip part copied byte for byte (no openpyxl save).')
    new, old = target(art, f)
    L, n, n0 = section(art, os.path.basename(f), v, 'final/' + f, d, b, kind)
    src = write(art, new, old, L); tot[art] = (n, n0)
    print(f'{art:8} {new} <- {src}: {n} changes ({n0} step 0)')
sd, sb, sf, sv = E.SIR
L, n, n0 = section('SIR', sf, sv, 'final/' + sf, sd, sb, 'text to paste in the Google Doc (the SIR has no local docx).')
src = write('SIR', CL + NEWNAME['SIR'], CL + OLDNAME['SIR'], L)
print('SIR     ', CL + NEWNAME['SIR'], '<-', src, n)

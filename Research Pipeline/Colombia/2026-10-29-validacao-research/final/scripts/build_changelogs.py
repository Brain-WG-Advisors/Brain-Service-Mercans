# -*- coding: utf-8 -*-
"""One changelog per final in final/changelogs/, as in the France release (docs/history/2026-10-06-final-release):
release header + the review trail of the approved DRAFT (revisao/<group>/CHANGELOG.md, verbatim) + the release section
(cleanup edits from release_log.json, highlight removal, Test 0 corrections from test0_corrections.py).
Usage: python -I final/scripts/build_changelogs.py
"""
import os, sys, json, hashlib, collections
HERE = os.path.dirname(os.path.abspath(__file__)); VAL = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE); os.chdir(VAL)
import pairs, release_edits as E
try:
    import test0_corrections as T0
except ImportError:
    T0 = None
sys.stdout.reconfigure(encoding='utf-8')

HEAD = ('> **Released 2026-10-30 — approved by Wallisson Gomes (Compliance Regulations Team Lead).** This changelog is the review '
        'trail of the corrections; statements below such as "DRAFT", "COVAL", "round" or "not promoted" describe the state during '
        'review, before approval and release. The released file carries none of those marks (see the release section at the end '
        'and `final/RELEASE-CROSSCHECK.md`).\n')
GROUP = {'CCG': 'CCG', 'WTC': 'WTC', 'DD': 'DD', 'NE': 'NE', 'F350': 'FORMS', 'F220': 'FORMS', 'F2276': 'FORMS', 'CES006': 'FORMS',
         'PILA003': 'PILA', 'PILA007': 'PILA', 'PAYSLIP': 'PAYSLIP'}
log = json.load(open('final/scripts/release_log.json', encoding='utf-8'))
md5 = lambda p: hashlib.md5(open(p, 'rb').read()).hexdigest()
t0 = getattr(T0, 'ITEMS', []) if T0 else []
import residuos_corrections as RS, consistencia_corrections as CS
rs_cells = {(a_, f'{sh}!{c}') for M in (RS, CS) for a_, cells in M.XLSX.items() for (sh, c) in cells}
rs_olds = [e[0] for M in (RS, CS) for e in M.DOCX]
os.makedirs('final/changelogs', exist_ok=True)


def cut(s, n=400):
    s = (s or '').replace('|', '\\|').replace('\n', ' ⏎ ')
    return s if len(s) <= n else s[:n] + ' …'


for art, d, b, f, v in pairs.PAIRS:
    name = os.path.basename(f)
    trail = open(f'revisao/{GROUP[art]}/CHANGELOG.md', encoding='utf-8').read()
    L = [HEAD, f'# {name} (version {v}, issued 2026-10-30): changelog', '',
         f'- **Released file:** `final/{f}` (md5 `{md5("final/" + f)}`).',
         f'- **Approved DRAFT:** `{d}` (md5 `{md5(d)}`).',
         f'- **Version in force before this one:** `{b}` (md5 `{md5(b)}`).',
         '- **Method:** ' + ('all tracked changes accepted by XML surgery on word/document.xml; every other part copied byte for byte (rsids and the inherited review comment removed).'
                             if f.endswith('.docx') else 'XML surgery on the sheet parts and styles.xml; every other zip part copied byte for byte (no openpyxl save).'),
         '', '## Release 2026-10-30: what the release changed against the approved DRAFT', '']
    if f.endswith('.xlsx'):
        L.append('- **Review highlight removed:** every cell with the fill `FFDDEBF7` gets back the style of the version in force (or the equivalent non-highlighted style of its column); no other formatting changes. Count in `final/RELEASE-CROSSCHECK.md`.')
    L += ['- **Issue metadata:** created = modified = 2026-10-30, revision 1, author Wallisson Gomes, no custom properties.', '',
          '| # | Where | Before (DRAFT) | After (released) | Why |', '|---|---|---|---|---|']
    t0w = {(x['artifact'], x['where']) for x in t0}
    n = 0
    for x in log:
        if x['artifact'] != art: continue
        rs = (art, x['where']) in rs_cells or (art == 'CCG' and x['where'] == 'paragraph' and any(o in (x['before'] or '') for o in rs_olds))
        why = 'Post-release review 2026-10-30 (see below)' if rs else 'Test 0 correction (see below)' if (art, x['where']) in t0w else ('Version Control / issue data' if 'Version Control' in x['where'] or x['where'].startswith('Payslip Spec!B85') or x['where'].startswith('Payslip Spec!C85') or x['where'].startswith('Payslip Spec!D85') or x['where'].startswith('Payslip Spec!E85') or 'Report Matrix!B19' in x['where'] else 'internal mark removed / neutral product wording')
        n += 1
        L.append(f'| {n} | {x["where"]} | {cut(x["before"])} | {cut(x["after"])} | {why} |')
    mine = [x for x in t0 if x['artifact'] == art]
    L += ['', '## Test 0 (independent reviewer, 2026-10-30)', '']
    if mine:
        L += ['| ID | Where | Finding | Correction | Source |', '|---|---|---|---|---|']
        for x in mine:
            L.append(f'| {x["id"]} | {x["where"]} | {cut(x["finding"], 300)} | {cut(x["correction"], 300)} | {cut(x["source"], 200)} |')
    else:
        L.append('No confirmed finding on this artifact.')
    mrs = [x for x in RS.ITEMS + CS.ITEMS if x['artifact'] == art]
    L += ['', '## Post-release review 2026-10-30', '',
          'Residual Test 0 items (`final/test0/RESIDUOS-DECISOES.md`, edits in `final/scripts/residuos_corrections.py`) and the '
          'second pass on consistency between the CCG and the specs / WTC / Payslip (IDs PR-nn; decisions, sources and literal '
          'extracts in `final/test0/CONSISTENCIA-DECISOES.md`, edits in `final/scripts/consistencia_corrections.py`), all decided on '
          'primary sources after the release and proven by `final/RELEASE-CROSSCHECK.md`. Same version and issue date.', '']
    if mrs:
        L += ['| ID | Where | Finding | Correction | Source |', '|---|---|---|---|---|']
        for x in mrs:
            L.append(f'| {x["id"]} | {x["where"]} | {cut(x["finding"], 300)} | {cut(x["correction"], 300)} | {cut(x["source"], 250)} |')
    else:
        L.append('No change to this artifact.')
    L += ['', '---', '', f'## Review trail of the approved DRAFT (`revisao/{GROUP[art]}/CHANGELOG.md`, verbatim)', '', trail]
    out = f'final/changelogs/{name.rsplit(".", 1)[0]}-CHANGELOG.md'
    open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
    print(out, n, 'release edits', len(mine), 'test0')

# SIR
sir = ['> **Released 2026-10-30 — approved by Wallisson Gomes (Compliance Regulations Team Lead).** This changelog is the review trail of the corrections; statements below such as "DRAFT", "COVAL" or "round" describe the state during review, before approval and release.\n',
       '# CO-SIR-001 v1.2 (issued 2026-10-30): changelog', '',
       '- **Released text:** `final/CO-SIR-001-v1.2-texto-final.md` (to paste in the Google Doc; the SIR has no local docx).',
       '- **Approved redline:** `revisao/SIR/CO-SIR-001-v1.2-DRAFT-COVAL-2026-10-29-REDLINE.md`; base `linha-de-base/CO-SIR-001-v1.1-captura-2026-10-29.md`.', '',
       '## Release 2026-10-30: what the release changed against the approved redline', '',
       '- Version `v1.2 DRAFT` → `v1.2`; Version history row rewritten without IDs, rounds or "provisional" (date 2026-10-30).',
       '- Related deliverables: `scope_manifest.json` and the folder name `04-reports-spec` (internal working files) left out of the new line.',
       '- S-07 (rule count): the redline note "Position — confidence 80%" stays only in this trail; the text to paste states the rule without the exact split.',
       '- Every other block is the redline\'s "Novo" text, verbatim.', '']
mine = [x for x in t0 if x['artifact'] == 'SIR']
sir += ['## Test 0 (independent reviewer, 2026-10-30)', '']
sir += [f'- {x["id"]} {x["where"]}: {x["finding"]} → {x["correction"]} ({x["source"]})' for x in mine] or ['No confirmed finding on the SIR text.']
sir += ['', '---', '', '## Review trail (`revisao/SIR/CHANGELOG.md`, verbatim)', '', open('revisao/SIR/CHANGELOG.md', encoding='utf-8').read()]
open('final/changelogs/CO-SIR-001-v1.2-CHANGELOG.md', 'w', encoding='utf-8').write('\n'.join(sir) + '\n')
print('SIR changelog ok')

"""Regenera 01-ccg, 02-wtc, 04-reports-spec e 05-data-dictionary da skill BE a partir das fontes do Drive.

Usa os conversores do refresh de 16/09 (~/mercans-pipeline/BE-compliance/_work_stage11) sem alterá-los.
Uso: python -I regen_refs.py   (rodar nesta pasta)
"""
import os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__))
CONV = os.path.expanduser('~/mercans-pipeline/BE-compliance/_work_stage11')
sys.path.insert(0, CONV)
import xlsx2md, docx2md, openpyxl  # noqa: E402

F = os.path.join(HERE, 'fontes')
R = os.path.join(HERE, 'payroll-compliance-belgium', 'references')
OLD_WTC = os.path.expanduser('~/mercans-pipeline/BE-compliance/08-skill/payroll-compliance-belgium/references/02-wtc.md')

def write(name, text):
    with open(os.path.join(R, name), 'w', encoding='utf-8') as fh:
        fh.write(text)
    print('wrote', name, len(text))

# 01 — CCG (Drive, export de 21/10)
write('01-ccg.md', docx2md.build(os.path.join(F, 'BE-CCG-001-v1.0_export-2026-10-21.docx'),
                                 'Belgium — Country Compliance Guide (CCG) — BE-CCG-001 v1.0 (Drive, as at 2026-10-21)'))

# 02 — WTC (Drive v1.3) + notas de build do workbook do pipeline (não estão no arquivo do Drive)
wtc = xlsx2md.build(os.path.join(F, 'BE-WTC-001-v1.3.xlsx'),
                    'Belgium — Wage Type Catalogue (WTC) — BE-WTC-001 v1.3 (Drive, 2026-10-22)',
                    'Belgium › 03 - WTC › BE-WTC-001-v1.3.xlsx')
old = open(OLD_WTC, encoding='utf-8').read()
m = re.search(r'## Sheet: `Version Control`\n(.*?)\n## Sheet: `Wage Type Catalogue`', old, re.S)
notes = m.group(1).strip()
wtc = wtc.rstrip() + '\n\n---\n\n## Appendix: build notes of the pipeline workbook (16 September 2026)\n\n' \
      '*The Drive workbook carries a short Version Control (1.0 Initial Version, 1.1 Global WTC 62/65/79 completion, 1.2 employer rate in row 23671, 1.3 All Codes 62/65/79 completion at rows 829-1183). ' \
      'The pipeline build workbook of 16 September 2026, whose Wage Type Catalogue rows 2-360 are identical to the Drive file, ' \
      'carried the full build history and remarks below. They are kept here verbatim as reference; row numbers they cite ' \
      'are unchanged in v1.3.*\n\n' + notes + '\n'
write('02-wtc.md', wtc)

# 04 — Report Specs (Drive v1.1, Field Explanation em inglês)
SPECS = [
    ('BE-NSSO-001-Dimona-Spec_v1.1.xlsx', 'BE-NSSO-001 — Dimona (immediate employment declaration)'),
    ('BE-NSSO-002-DmfA-Spec_v1.1.xlsx', 'BE-NSSO-002 — DmfA (quarterly multifunctional declaration)'),
    ('BE-NSSO-003-DmfAModification-Spec_v1.1.xlsx', 'BE-NSSO-003 — DmfA modification'),
    ('BE-NSSO-004-DRS-Spec_v1.1.xlsx', 'BE-NSSO-004 — DRS / ASR (social risk declaration)'),
    ('BE-NSSO-005-Limosa-Spec_v1.1.xlsx', 'BE-NSSO-005 — Limosa (OUT OF SCOPE — retained for reference only)'),
    ('BE-FIN-001-Finprof274-Spec_v1.1.xlsx', 'BE-FIN-001 — FinProf form 274 (withholding tax return)'),
    ('BE-FIN-002-Belcotax28110-Spec_v1.1.xlsx', 'BE-FIN-002 — Belcotax-on-web form 281.10'),
    ('BE-FEDRIS-001-WorkAccident-Spec_v1.1.xlsx', 'BE-FEDRIS-001 — Fedris work accident declaration'),
    ('BE-FEBELFIN-001-SEPACreditTransfer-Spec_v1.1.xlsx', 'BE-FEBELFIN-001 — Febelfin SEPA credit transfer (pain.001)'),
]
blocks = []
for fn, title in SPECS:
    wb = openpyxl.load_workbook(os.path.join(F, 'specs', fn), data_only=True)
    names = wb.sheetnames
    out = ['## %s' % title, '', '*Source workbook: `Belgium › 12- Country Report Codes › %s` — %d sheets: %s*'
           % (fn, len(names), ', '.join('`%s`' % n for n in names)), '']
    subnav = []
    for ws in wb.worksheets:
        subnav.append((ws.title, len(out)))
        out += ['### Sheet: `%s`' % ws.title, '']
        rows = xlsx2md.sheet_rows(ws)
        if rows:
            out.append('| ' + ' | '.join(rows[0]) + ' |')
            out.append('| ' + ' | '.join(['---'] * len(rows[0])) + ' |')
            out += ['| ' + ' | '.join(r) + ' |' for r in rows[1:]]
        else:
            out.append('*(empty sheet)*')
        out.append('')
    wb.close()
    blocks.append((title, out, subnav))
head = ['# Belgium — Statutory Report Specifications (9 workbooks, v1.1, Field Explanation in English)', '', '---', '',
        '<!-- nav-index -->', '## Navigation — line numbers in this file', '',
        '*Read this file with `offset`/`limit` rather than whole; it is large.*', '']
tail = ['', '---', '']
cur = len(head) + sum(1 + len(sn) for _, _, sn in blocks) + len(tail) + 1
nav = []
for title, out, subnav in blocks:
    nav.append('- L%d: %s' % (cur, title))
    nav += ['  - L%d: Sheet: `%s`' % (cur + off, s) for s, off in subnav]
    cur += len(out)
lines = head + nav + tail
for _, out, _ in blocks:
    lines += out
write('04-reports-spec.md', '\n'.join(lines).rstrip() + '\n')

# 05 — DD (Drive v1.0 = conteúdo do v1.4 do pipeline; só o Version Control difere)
write('05-data-dictionary.md', xlsx2md.build(os.path.join(F, 'BE-DD-001-v1.0_export-2026-10-16.xlsx'),
                                             'Belgium — Data Dictionary (DD) — BE-DD-001 v1.0 (Drive)',
                                             'Belgium › 02- DD › BE-DD-001-v1.0 (export 2026-10-16)'))

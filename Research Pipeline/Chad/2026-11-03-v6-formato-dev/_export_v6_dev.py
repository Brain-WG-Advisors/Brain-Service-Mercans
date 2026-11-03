"""Chad design v6 written in the development team's export format (CT-A-580..588 .md layout).

Data source: ../2026-11-02-design-v6/_build_v6.py (imported, read only; nothing copied by hand):
FLAGS, DERIVED, R (36 regulations: bands, matrices, notes), CASH_GROSS, CNPS_GROSS, TFE_BASE, TAFP_BASE.
Format source: ../2026-10-29-teste-design-hrblizz/2026-10-30-export-ram/x/ (9 .md of the Dev export).
Output: x-v6/ — one TD Specifications, one New Design, six taxability matrices, one Tax Table.

Run:  python -I _export_v6_dev.py      then  python -I _roundtrip_v6_dev.py
"""
import importlib.util, os, re, sys

sys.dont_write_bytecode = True          # never write __pycache__ into the read-only v6 folder
HERE = os.path.dirname(os.path.abspath(__file__))
CHAD = os.path.dirname(HERE)
V6_BUILD = os.path.join(CHAD, '2026-11-02-design-v6', '_build_v6.py')
DEV_X = os.path.join(CHAD, '2026-10-29-teste-design-hrblizz', '2026-10-30-export-ram', 'x')
WTC_XLSX = os.path.join(CHAD, '2026-10-29-teste-design-hrblizz', '2026-10-30-export-ram', 'CHAD-WTC_V3.0-export-2026-11-01.xlsx')
OUT = os.path.join(HERE, 'x-v6')
TAG = 'Compliance v6 (test set)'


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


b6 = load('build_v6', V6_BUILD)
L = load('leitor_dev_md', os.path.join(HERE, '_leitor_dev_md.py'))
REG = {r['id']: r for r in b6.R}

# ------------------------------------------------------------------ file names (Dev pattern + v6 suffix)
F_SPEC, F_DESIGN, F_TAX = '1  CT-A-580-v6.md', '2  CT-A-588-v6.md', '9  CT-A-582-v6.md'
# (file, Dev counterpart, title as the Dev writes it, matrix from the v6 build, regulations that use it)
MATRICES = [
    ('3  CT-A-587-v6.md', '3  CT-A-587.md', 'TD: Cash Gross Salary', b6.CASH_GROSS, [9148009, 9148010]),
    ('4  CT-A-581-v6.md', '4  CT-A-581.md', 'TD: Taxable Gross', REG[9148131]['matrix'], [9148131]),
    ('5  CT-A-586-v6.md', '5  CT-A-586.md', 'TD: CNPS Salary', b6.CNPS_GROSS, [9148155]),
    ('6  CT-A-585-v6.md', '6  CT-A-585.md', 'TD Employer Lump-Sum Tax Base', b6.TFE_BASE, [9148151]),
    ('7  CT-A-584-v6.md', '7  CT-A-584.md', 'TD: Apprenticeship Base', b6.TAFP_BASE, [9148141]),
    ('8  CT-A-583-v6.md', '8  CT-A-583.md', 'TD: Non-Resident Tax Base', REG[9148192]['matrix'], [9148192]),
]
for _f, _d, _t, _m, _u in MATRICES:
    for _i in _u:
        assert sorted(REG[_i]['matrix'], key=lambda x: (int(x[0]), x[1])) == sorted(_m, key=lambda x: (int(x[0]), x[1])), (_f, _i)
TAX_REG = 9148211


def label(fname, title):
    return fname.split('  ')[1][:-3] + ' ' + title          # e.g. "CT-A-587-v6 TD: Cash Gross Salary"


def skey(row):
    return (int(row[0]), row[1])


def sorted_matrix(m):
    return sorted(m, key=skey)                                # the Dev lists accounts in ascending order


def named_matrix(rid):
    for f, _, t, mm, users in MATRICES:
        if rid in users:
            return label(f, t)
    return None


# ------------------------------------------------------------------ neutral wording for the notes
SUBS = [
    (r'technical decision of the front, 60% \(A34\)', 'open point, pending sign-off'),
    (r'technical decision of the front, guide p\. 8, pending the user’s ok; ASSUMPTIONS D1', 'guide p. 8; open point, pending sign-off'),
    (r'technical decision of the front, pending the user’s ok; ASSUMPTIONS D2', 'open point, pending sign-off'),
    (r'technical decision of the front, pending the user’s ok; reverses `correcoes\.md` 2026-07-07 \("severance outside the TFE"; ASSUMPTIONS A20\)',
     'open point, pending sign-off; reverses the earlier position "severance outside the TFE"'),
    (r'front decision pending the user’s ok', 'open point, pending sign-off'),
    (r'Round 4: ', ''), (r' — v6 r3 — ', ' '), (r' — v6 r3: ', ' — '), (r'v6 r3: ', ''), (r'v6 r2: ', ''),
    (r' \(A2[3-7]\)', ''), (r'\(A26: ', '('), (r', A24\)', ')'), (r' \(to create, R1[5-7]\)', ' (to create in the WTC)'),
    (r' \(R1[5-7]\)', ' (to create in the WTC)'), (r'; ASSUMPTIONS [A-Z]\d+', ''), (r' \(ASSUMPTIONS [A-Z]\d+\)', ''),
    (r' left out as in v5', ' left out'), (r', as in v5 —', ' —'), (r'v6 keeps', 'this set keeps'),
    (r'Additional regulation \(no Dev pair\), Dev pattern', 'New regulation (no pair in the current design), current-design pattern'),
    (r'Additional regulation \(no Dev pair\), in the Dev convention', 'New regulation (no pair in the current design), current-design convention'),
    (r'Additional regulation \(no Dev pair\), Dev convention', 'New regulation (no pair in the current design), current-design convention'),
    (r'\(replaces Dev 9148011\)', '(replaces 9148011)'),
    (r'As the Dev formula', 'Formula kept from the current design'), (r'As the Dev', 'Kept from the current design'), (r'as the Dev', 'as in the current design'),
    (r'the Dev\'s', 'the current design\'s'), (r'the Dev ', 'the current design '), (r'Dev NOT', 'current-design NOT'),
    (r'The Dev ', 'The current design '), (r'\(the Dev: ', '(current design: '), (r'the Dev field', 'the current-design field'),
    (r'Dev formula', 'current-design formula'), (r'the Dev\)', 'the current design)'),
]
FORBIDDEN = re.compile(r'Claude|\bDev\b|\bv5\b|\bv6 r\d|front|user|ASSUMPTIONS|correcoes|\bA\d\d\b|\bR1\d\b')


def neutral(t):
    for a, b in SUBS:
        t = re.sub(a, b, t)
    bad = FORBIDDEN.findall(t)
    assert not bad, (bad, t)
    return t


def n(v):
    if v == '' or v is None:
        return ''
    v = float(v)
    return str(int(v)) if v.is_integer() else repr(v)


# ------------------------------------------------------------------ classification against the Dev export
DEV = {r['id']: r for r in L.read_design(os.path.join(DEV_X, '2  CT-A-588.md'))}
ENGINE_BAND = ['f', 't', 'ee', 'er', 'floor', 'ceil', 'formula', 'assertion', 'ceilacc', 'deb', 'cred']


def band_t(b):
    return tuple('' if b[k] == '' else (float(b[k]) if k in ('f', 't', 'ee', 'er', 'floor', 'ceil') else str(b[k])) for k in ENGINE_BAND)


def compare(r, d):
    """fields of the regulation that differ from the Dev regulation with the same ID"""
    out = []
    for k, lab in (('name', 'name'), ('ord', 'ordinal'), ('group', 'tax group'), ('trg', 'rule group'), ('ttype', 'taxation type'), ('pre', 'pre-condition')):
        if str(r[k]) != str(d[k]):
            out.append(lab)
    if [band_t(b) for b in r['bands']] != [band_t(b) for b in d['bands']]:
        out.append('bands')
    if sorted_matrix(r['matrix']) != sorted_matrix(d['matrix']):
        out.append('matrix')
    return out


def status(r):
    if r['id'] not in DEV:
        return 'NEW', []
    c = compare(r, DEV[r['id']])
    return ('CHANGED' if c else 'SAME'), c


# ------------------------------------------------------------------ WTC names for the comment column of the matrix files
def wtc_names():
    import openpyxl
    wb = openpyxl.load_workbook(WTC_XLSX, read_only=True, data_only=True)
    d = {}
    for r in wb['Wage Type Catalogue'].iter_rows(min_row=2, values_only=True):
        if r[0] is None:
            continue
        c = str(int(r[0])) if isinstance(r[0], (int, float)) else str(r[0])
        d[c] = (r[1] or '').strip()
    return d


def comment(acc, pat, W):
    if not pat:
        return W.get(acc, '')
    if pat.count('%') == 1:                                   # one series: name of its first code (e.g. 6218% -> 62180)
        return W.get(pat.replace('%', '0'), '')
    return ''


# ------------------------------------------------------------------ writers
BAND_HDR = '| ' + ' | '.join(L.BAND_COLS) + ' |'
BAND_SEP = '| ' + ' | '.join(['---'] * 15) + ' |'


def write(fname, lines):
    with open(os.path.join(OUT, fname), 'w', encoding='utf-8', newline='\n') as fh:
        fh.write('\n'.join(lines))


def write_design():
    Lx = [f'# TD: New Design — {TAG}']
    for r in b6.R:
        st, ch = status(r)
        Lx += [f"# {r['id']} - {r['name']}", '', f"## **Regulation Name: {r['name']}**", '', '**System Tax Years:** td_2026', '',
               '**System Reporting Periods:**', '', f"**Regulation ID:** {r['id']}", '', '**Status:** active', '',
               f"**Processing Order (Ordinal):** {r['ord']:02d}", '', '**1. Classification**', '',
               f"* **Tax Group:** {r['group']}", f"* **Tax Rule Group:** {r['trg']}", f"* **Taxation Type:** {r['ttype']}", '* **Currency:** XAF', '',
               '**2. Execution Conditions (Assertions)**', '', ('* **Pre-condition:** ' + r['pre']).rstrip(), '',
               '**3. Calculation Logic (Bands)**', '', BAND_HDR, BAND_SEP]
        for b in r['bands']:
            assert b['credit'] == '', 'creditAmount has no column in the Dev layout'
            Lx.append('| ' + ' | '.join([n(b['f']), n(b['t']), n(b['ee']), n(b['er']), n(b['floor']), n(b['ceil']), b['formula'], b['assertion'],
                                          '', '', '', '', b['ceilacc'], b['deb'], b['cred']]) + ' |')
        Lx += ['', '**4. Taxability Rules (Applicable Accounts)**', '', '| Account | Pattern | Is Taxable? |', '| --- | --- | --- |']
        Lx += [f'| {a} | {p} | {y} |' for a, p, y in sorted_matrix(r['matrix'])]
        mark = {'NEW': 'NEW (no pair in the current design)', 'SAME': 'SAME as the current design',
                'CHANGED': 'CHANGED vs the current design (' + ', '.join(ch) + ')'}[st]
        Lx += ['', f"> **Test set:** {mark}. {neutral(r['note'])}", '', '---', '']
    write(F_DESIGN, Lx)


def bands_cell(r):
    if r['ttype'] == 'differential':
        items = ([f"Regulation Assertion: {r['pre']}"] if r['pre'] else []) + [label(F_TAX, 'Tax Table')]
        return '<br />'.join(items)
    out = [f"Regulation Assertion: {r['pre']}"] if r['pre'] else []
    for b in r['bands']:
        it = []
        if b['assertion']:
            it.append(f"Band Assertion: {b['assertion']}")
        if b['ee'] != '':
            it.append(f"Employee Rate: {n(b['ee'])}")
        if b['er'] != '':
            it.append(f"Employer Rate: {n(b['er'])}")
        if b['floor'] != '':
            it.append(f"Floor Amount: {n(b['floor'])}")
        if b['ceil'] != '':
            it.append(f"Ceiling Amount: {n(b['ceil'])}")
        if b['formula']:
            it.append(f"Formula: {b['formula']}")
        out.append('<br />'.join(it))
    return '<br /><br />'.join(out)


def matrix_cell(rid, m):
    lab = named_matrix(rid)
    if lab:
        return lab
    m = sorted_matrix(m)
    if all(not p and y == 'Yes' for a, p, y in m):
        return '<br />'.join(a for a, p, y in m)
    sfx = lambda y: '' if y == 'Yes' else ' (No)'
    acc = [a + sfx(y) for a, p, y in m if not p]
    pat = [p + sfx(y) for a, p, y in m if p]
    parts = []
    if acc:
        parts.append('Account:<br />' + '<br />'.join(acc))
    if pat:
        parts.append('Pattern:<br />' + '<br />'.join(pat))
    return '<br /><br />'.join(parts)


def dc_cells(r):
    pairs = [(b['deb'], b['cred']) for b in r['bands']]
    if len(set(pairs)) == 1:
        pairs = pairs[:1]
    return '<br />'.join(p[0] for p in pairs), '<br />'.join(p[1] for p in pairs)


HR_IN_DEV = {'$hr.employee_type', '$hr.young_graduate_employee_exemption_start_date', '$entry.period_end_date'}


def write_spec():
    Lx = [f'# TD Specifications — {TAG}', '**Flags**:', '']
    for a, name, f, v in b6.FLAGS:
        der = ' Derived from other flags in the same run (evaluated before the regulations).' if a in b6.DERIVED else ''
        Lx += [f'**{a}**: {f}', '', f'{name} — {neutral(v)}.{der}', '']
    Lx += ['', '', '**Notionals:**', '',
           'None defined in this set (the regulations of this set read no notional account).', '', '', '',
           '**HR Fields:**', '']
    fields = []
    for a, name, f, v in b6.FLAGS:
        for m in re.finditer(r'\$(?:hr|legal_entity_hr|entry|period)\.[a-z_]+', f):
            if m.group(0) not in [x[0] for x in fields]:
                fields.append((m.group(0), a, '::key' in f[m.end():m.end() + 5]))
    for fld, a, key in fields:
        new = '' if fld in HR_IN_DEV else ' — new field'
        kind = ' (list field, read with ::key)' if key else ''
        Lx += [f'{fld}\tflag {a}{kind}{new}', '']
    Lx += ['', '', '**Design**:', '',
           '| Ordinal | Regulation ID | Regulation Name | **Tax Group** | **Tax Rule Group** | **Taxation Type** | Debit | Credit | Taxability Matrix | Regulation Bands |',
           '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
    for r in b6.R:
        d, c = dc_cells(r)
        Lx.append(f"| {r['ord']:02d} | {r['id']} | {r['name']} | {r['group']} | {r['trg']} | {r['ttype']} | {d} | {c} | {matrix_cell(r['id'], r['matrix'])} | {bands_cell(r)} |")
    new = [r['id'] for r in b6.R if status(r)[0] == 'NEW']
    gone = [i for i in DEV if i not in REG]
    Lx += ['', f"**New regulations in this set (no pair in the current design):** {', '.join(map(str, new))}", '',
           f"**Regulations of the current design not in this set:** {', '.join(map(str, gone))} (replaced by 9148192, which reads 58552 after 9148191)", '',
           'IDs, names and ordinals follow the current design (9148xxx); every regulation of the set is described in full, with its note, in CT-A-588-v6.', '']
    Lx += ['', '**Prerequisites not yet in the system (needed before this set can run):**', '',
           '- HR / entity fields marked "new field" in the HR Fields list above.',
           '- New intermediate accounts: 58113, 58114, 58115, 58172.',
           '- New flags: 58202, 58203, 58204, 58207, 58210, 58213, 58215, 58216, 58217, 58219, 58223, 58225, 58226 (58219 and 58226 are derived from other flags and must be evaluated after them).',
           '- New liability account: 2570 (TD PSA EE, food security levy).',
           '- New wage types: 6287x (function expense allowance), 6288x, 62890, and a 216xx code for a compulsory supplementary pension scheme.',
           '- GL accounts on the debit side to check against the chart of accounts: 2610, 6020, 6034, 6037, 6040, 6063.', '']
    write(F_SPEC, Lx)
    return new, gone


def write_matrices():
    W = wtc_names()
    for f, _, title, m, users in MATRICES:
        Lx = [f'# {title} — {TAG}', '| Account | Pattern | Is Taxable |  |', '| --- | --- | --- | --- |']
        Lx += [f'| {a} | {p} | {y} | {comment(a, p, W)} |' for a, p, y in sorted_matrix(m)]
        Lx += ['', f"**Used by:** {', '.join(map(str, users))}"]
        write(f, Lx)


def write_tax_table():
    r = REG[TAX_REG]
    Lx = [f'# TD: Tax Table — {TAG}', '| Income From | Income To | Employee Rate |', '| --- | --- | --- |']
    Lx += [f"| {n(b['f'])} | {n(b['t'])} | {n(b['ee'])} |" for b in r['bands']]
    Lx += ['', 'Limits at the round figure: incomeTo of a band = incomeFrom of the next one (the tax starts at the 800,001st franc). CGI Art. 1-IV.', '']
    write(F_TAX, Lx)


if __name__ == '__main__':
    os.makedirs(OUT, exist_ok=True)
    write_design()
    new, gone = write_spec()
    write_matrices()
    write_tax_table()
    st = [status(r)[0] for r in b6.R]
    print(f'regulations {len(b6.R)}: SAME {st.count("SAME")} · CHANGED {st.count("CHANGED")} · NEW {st.count("NEW")} ({new}); not in this set: {gone}')
    print('written:', sorted(os.listdir(OUT)))

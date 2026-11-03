"""Reader of the development team's design export (.md, CT-A-580..588 layout).

Pure parser, no dependency on the v6 generator: it reads a New Design file, a TD Specifications file,
a taxability-matrix file and a Tax Table file the way a loader would, and returns plain structures
in the shape of the regulation dicts of _build_v6.py (id, ord, name, group, trg, ttype, pre, bands, matrix).
Used by _roundtrip_v6_dev.py (round trip of the generated files) and by _export_v6_dev.py (reading the
Dev export to mark each regulation NEW / CHANGED / SAME).
"""
import re

BAND_COLS = ['incomeFrom', 'incomeTo', 'employeeRate', 'employerRate', 'floorAmount', 'ceilingAmount', 'Formula', 'assertion',
             'unit account', 'employeeRateAccount', 'employerRateAccount', 'floorAccount', 'ceilingAccount', 'debitAccount', 'creditAccount']


def num(s):
    s = s.strip()
    if s == '':
        return ''
    return float(s)


def cells(line):
    line = line.strip()
    assert line.startswith('|') and line.endswith('|'), line
    return [c.strip() for c in line[1:-1].split('|')]


def _field(block, label):
    m = re.search(r'^\*?\s*\*\*' + re.escape(label) + r':\*\*[ \t]*(.*)$', block, flags=re.M)
    return m.group(1).strip() if m else None


def read_design(path):
    """New Design (.md) -> list of regulation dicts, in file order."""
    with open(path, encoding='utf-8') as fh:
        txt = fh.read()
    parts = re.split(r'^# (\d{7}) - (.+)$', txt, flags=re.M)
    regs = []
    for i in range(1, len(parts), 3):
        rid, name, body = parts[i], parts[i + 1].strip(), parts[i + 2]
        r = dict(id=int(rid), name=name)
        m = re.search(r'^## \*\*Regulation Name: (.*)\*\*$', body, flags=re.M)
        assert m and m.group(1).strip() == name, (rid, 'name')
        assert int(_field(body, 'Regulation ID')) == r['id'], (rid, 'id')
        r['ord'] = int(_field(body, 'Processing Order (Ordinal)'))
        r['group'] = _field(body, 'Tax Group')
        r['trg'] = _field(body, 'Tax Rule Group')
        r['ttype'] = _field(body, 'Taxation Type')
        r['currency'] = _field(body, 'Currency')
        r['tax_years'] = _field(body, 'System Tax Years')
        r['status'] = _field(body, 'Status')
        r['pre'] = _field(body, 'Pre-condition') or ''
        lines = body.split('\n')
        # bands
        hi = next(k for k, l in enumerate(lines) if l.startswith('| incomeFrom'))
        assert cells(lines[hi]) == BAND_COLS, (rid, 'band header')
        bands, k = [], hi + 2
        while k < len(lines) and lines[k].startswith('|'):
            c = cells(lines[k])
            assert len(c) == 15, (rid, 'band width', len(c))
            bands.append(dict(f=num(c[0]), t=num(c[1]), ee=num(c[2]), er=num(c[3]), floor=num(c[4]), ceil=num(c[5]), credit='',
                              formula=c[6], assertion=c[7], unit=c[8], eeacc=c[9], eracc=c[10], flooracc=c[11],
                              ceilacc=c[12], deb=c[13], cred=c[14]))
            k += 1
        r['bands'] = bands
        # matrix
        mi = next(k for k, l in enumerate(lines) if l.startswith('| Account | Pattern'))
        mat, k = [], mi + 2
        while k < len(lines) and lines[k].startswith('|'):
            c = cells(lines[k])
            mat.append((c[0], c[1], c[2]))
            k += 1
        r['matrix'] = mat
        # optional note (blockquote) — not loaded by the engine, kept for the reader
        nm = re.search(r'^> (.*)$', body, flags=re.M)
        r['note'] = nm.group(1) if nm else ''
        regs.append(r)
    return regs


def read_matrix(path):
    """Taxability matrix file -> (title, [(account, pattern, taxable, comment)])."""
    with open(path, encoding='utf-8') as fh:
        lines = fh.read().split('\n')
    title = lines[0][2:].strip()
    hi = next(k for k, l in enumerate(lines) if l.startswith('| Account | Pattern'))
    rows, k = [], hi + 2
    while k < len(lines) and lines[k].startswith('|'):
        c = cells(lines[k])
        rows.append((c[0], c[1], c[2], c[3] if len(c) > 3 else ''))
        k += 1
    return title, rows


def read_tax_table(path):
    with open(path, encoding='utf-8') as fh:
        lines = fh.read().split('\n')
    hi = next(k for k, l in enumerate(lines) if l.startswith('| Income From'))
    rows, k = [], hi + 2
    while k < len(lines) and lines[k].startswith('|'):
        c = cells(lines[k])
        rows.append((num(c[0]), num(c[1]), num(c[2])))
        k += 1
    return rows


def read_spec(path):
    """TD Specifications -> dict(flags={acc: formula}, design=[row dicts], fields=[...])."""
    with open(path, encoding='utf-8') as fh:
        txt = fh.read()
    flags_part = txt.split('**Notionals:**')[0]
    flags = {m.group(1): m.group(2).strip() for m in re.finditer(r'^\*\*(\d{5})\*\*: (.+)$', flags_part, flags=re.M)}
    lines = txt.split('\n')
    hi = next(k for k, l in enumerate(lines) if l.startswith('| Ordinal | Regulation ID'))
    design, k = [], hi + 2
    while k < len(lines) and lines[k].startswith('|'):
        c = cells(lines[k])
        design.append(dict(ord=int(c[0]), id=int(c[1]), name=c[2], group=c[3], trg=c[4], ttype=c[5],
                           deb=[x for x in re.split(r'<br ?/>', c[6]) if x], cred=[x for x in re.split(r'<br ?/>', c[7]) if x],
                           matrix=c[8], bands=c[9]))
        k += 1
    return dict(flags=flags, design=design)

import sys, re, docx, openpyxl, datetime
from docx.oxml.ns import qn

def clean(s):
    if s is None: return ''
    if isinstance(s, datetime.datetime):
        return s.strftime('%Y-%m-%d') if (s.hour, s.minute, s.second) == (0, 0, 0) else s.isoformat(sep=' ')
    if isinstance(s, float):
        if s.is_integer(): return str(int(s))
        return repr(s)
    s = str(s).replace('\r', '')
    s = s.replace('|', '\\|')
    s = re.sub(r'\n+', ' <br> ', s.strip())
    s = re.sub(r'[ \t]+', ' ', s)
    return s

def ptext(el):
    out = []
    for n in el.iter():
        if n.tag == qn('w:t'): out.append(n.text or '')
        elif n.tag == qn('w:tab'): out.append(' ')
        elif n.tag in (qn('w:br'), qn('w:cr')): out.append('\n')
    return ''.join(out)

def docx_md(path, shift=0):
    d = docx.Document(path)
    out = []
    body = d.element.body
    for child in body.iterchildren():
        if child.tag == qn('w:p'):
            sty = child.find(qn('w:pPr'))
            sname = ''
            if sty is not None and sty.find(qn('w:pStyle')) is not None:
                sid = sty.find(qn('w:pStyle')).get(qn('w:val'))
                try: sname = d.styles.get_by_id(sid, 1).name
                except Exception: sname = sid or ''
            t = ptext(child).strip()
            if not t: continue
            m = re.match(r'Heading (\d)', sname)
            if m:
                out.append('\n' + '#' * min(6, int(m.group(1)) + shift) + ' ' + t.replace('\n', ' ') + '\n')
            elif sname == 'Title':
                out.append('\n' + '#' * (1 + shift) + ' ' + t + '\n')
            elif 'List' in sname or (sty is not None and sty.find(qn('w:numPr')) is not None):
                out.append('- ' + t.replace('\n', ' '))
            elif '\n' in t:
                out.append('\n```\n' + t + '\n```\n')
            else:
                out.append('\n' + t + '\n')
        elif child.tag == qn('w:tbl'):
            rows = []
            for tr in child.iter(qn('w:tr')):
                cells = [clean(chr(10).join(ptext(pp) for pp in tc.iter(qn('w:p')))) for tc in tr.findall(qn('w:tc'))]
                rows.append(cells)
            if not rows: continue
            w = max(len(r) for r in rows)
            rows = [r + [''] * (w - len(r)) for r in rows]
            if w == 1:
                for r in rows: out.append('\n> ' + r[0] + '\n')
                continue
            out.append('')
            out.append('| ' + ' | '.join(rows[0]) + ' |')
            out.append('|' + '---|' * w)
            for r in rows[1:]:
                out.append('| ' + ' | '.join(r) + ' |')
            out.append('')
    txt = '\n'.join(out)
    return re.sub(r'\n{3,}', '\n\n', txt)

def sheet_md(ws, hdr_level='###', table_from=None):
    """Render a sheet. Rows with 1 non-empty cell become text lines; rows with >=2 become table rows.
    Consecutive multi-cell rows form a table; the first of a run is used as header. Empty columns dropped per table."""
    rows = []
    for i, row in enumerate(ws.iter_rows(values_only=True), 1):
        vals = [clean(v) for v in row]
        while vals and vals[-1] == '': vals.pop()
        if not any(vals): rows.append(None); continue
        rows.append((i, vals))
    out = []
    run = []
    def flush():
        if not run: return
        w = max(len(v) for _, v in run)
        mat = [[('Row' if k == 0 else str(i))] + v + [''] * (w - len(v)) for k, (i, v) in enumerate(run)]
        w += 1
        keep = [0] + [j for j in range(1, w) if any(r[j] for r in mat)]
        mat = [[r[j] for j in keep] for r in mat]
        if len(keep) <= 2:
            for r in mat: out.append(' '.join(x for x in r[1:] if x) + '  ')
        else:
            out.append('')
            out.append('| ' + ' | '.join(mat[0]) + ' |')
            out.append('|' + '---|' * len(keep))
            for r in mat[1:]: out.append('| ' + ' | '.join(r) + ' |')
            out.append('')
        run.clear()
    for item in rows:
        if item is None:
            continue
        i, vals = item
        ne = [v for v in vals if v]
        if len(ne) == 1 and not run:
            out.append(ne[0] + '  ')
        elif len(ne) == 1 and run:
            # separator / note row inside a table: keep as a table row (bold when it is a section banner)
            v2 = [('**' + v + '**') if (v and v.startswith('═')) else v for v in vals]
            run.append((i, v2))
        else:
            run.append((i, vals))
    flush()
    txt = '\n'.join(out)
    return re.sub(r'\n{3,}', '\n\n', txt)

def xlsx_md(path, level='##', skip=()):
    wb = openpyxl.load_workbook(path, read_only=True, data_only=True)
    parts = []
    for ws in wb.worksheets:
        if ws.title in skip: continue
        parts.append(f'\n{level} Sheet: {ws.title}\n')
        parts.append(sheet_md(ws))
    return '\n'.join(parts)

if __name__ == '__main__':
    kind, path, outp = sys.argv[1], sys.argv[2], sys.argv[3]
    if kind == 'docx':
        md = docx_md(path, shift=int(sys.argv[4]) if len(sys.argv) > 4 else 0)
    else:
        md = xlsx_md(path, level=sys.argv[4] if len(sys.argv) > 4 else '##')
    open(outp, 'w', encoding='utf-8').write(md)
    print(outp, len(md))

"""XML-level patch of an xlsx (no openpyxl save): replaces one exact substring per cell (shared or inline strings)
and appends one Version Control row copied from the row of the previous version.
Usage: python xlsx_patch.py <src.xlsx> <dst.xlsx> <spec.json>
spec.json = {"edits": [[sheet, cell, old_substring, new_substring], ...],
             "vc": {"sheet": "Version Control", "after": "1.2", "version": "1.3", "date": "2026-10-22",
                    "desc": "...", "status": "Draft", "author": "Wallisson Gomes"}}"""
import zipfile, re, sys, html, json, datetime
sys.stdout.reconfigure(encoding='utf-8')
src, dst, specf = sys.argv[1], sys.argv[2], sys.argv[3]
spec = json.load(open(specf, encoding='utf-8'))
z = zipfile.ZipFile(src); names = z.namelist(); data = {n: z.read(n) for n in names}
wb = data['xl/workbook.xml'].decode('utf8'); rels = data['xl/_rels/workbook.xml.rels'].decode('utf8')
sheets = dict(re.findall(r'<sheet [^>]*?name="([^"]+)"[^>]*?r:id="([^"]+)"', wb))
rmap = dict(re.findall(r'<Relationship [^>]*?Id="([^"]+)"[^>]*?Target="([^"]+)"', rels))
rmap.update({a: b for b, a in re.findall(r'<Relationship [^>]*?Target="([^"]+)"[^>]*?Id="([^"]+)"', rels)})
def spath(name):
    t = rmap[sheets[html.escape(name, quote=False)] if html.escape(name, quote=False) in sheets else sheets[name]].lstrip('/')
    return t if t.startswith('xl/') else 'xl/' + t
ss = data['xl/sharedStrings.xml'].decode('utf8'); sis = re.findall(r'<si>.*?</si>', ss, re.S)
def si_text(s): return html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>', s, re.S)))
refcount = {}
for n in names:
    if n.startswith('xl/worksheets/sheet'):
        for v in re.findall(r'<c [^>]*t="s"[^>]*>\s*<v>(\d+)</v>', data[n].decode('utf8')): refcount[int(v)] = refcount.get(int(v), 0) + 1
def esc(s): return html.escape(s, quote=False)
log = []
for sh, cell, o, n in spec['edits']:
    p = spath(sh); x = data[p].decode('utf8')
    m = re.search(r'<c r="%s"([^>]*)>(.*?)</c>' % cell, x, re.S); assert m, (sh, cell)
    attrs, body = m.group(1), m.group(2)
    if 't="s"' in attrs:
        idx = int(re.search(r'<v>(\d+)</v>', body).group(1)); cur = si_text(sis[idx])
        assert cur.count(o) == 1, (sh, cell, 'old text count', cur.count(o))
        new = cur.replace(o, n)
        if refcount.get(idx, 0) == 1 and not re.search(r'<r>', sis[idx]):
            sis[idx] = '<si><t xml:space="preserve">%s</t></si>' % esc(new)
        else:
            sis.append('<si><t xml:space="preserve">%s</t></si>' % esc(new)); nidx = len(sis) - 1
            x = x[:m.start()] + m.group(0).replace('<v>%d</v>' % idx, '<v>%d</v>' % nidx) + x[m.end():]; data[p] = x.encode('utf8')
    elif 'inlineStr' in attrs:
        cur = html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>', body, re.S)))
        assert cur.count(o) == 1, (sh, cell, 'old text count', cur.count(o))
        new = cur.replace(o, n)
        x = x[:m.start()] + '<c r="%s"%s><is><t xml:space="preserve">%s</t></is></c>' % (cell, attrs, esc(new)) + x[m.end():]; data[p] = x.encode('utf8')
    else:
        raise SystemExit('unsupported cell type %s %s' % (sh, cell))
    log.append((sh, cell, cur, new))
vc = spec['vc']; p = spath(vc['sheet']); x = data[p].decode('utf8'); target = None
for r in re.finditer(r'<row [^>]*r="(\d+)"[^>]*>(.*?)</row>', x, re.S):
    cb = re.search(r'<c r="B%s"([^>]*)>(.*?)</c>' % r.group(1), r.group(2), re.S)
    if cb:
        v = re.search(r'<v>(.*?)</v>', cb.group(2)); t = re.search(r'<t[^>]*>(.*?)</t>', cb.group(2))
        val = si_text(sis[int(v.group(1))]) if (v and 't="s"' in cb.group(1)) else (v.group(1) if v else (t.group(1) if t else None))
        if val is not None and str(val).strip() in (vc['after'],): target = r
assert target, 'previous version row not found'
rn = int(target.group(1)); nr = rn + 1
nxt = re.search(r'<row [^>]*r="%d"[^>]*>(.*?)</row>|<row [^>]*r="%d"[^>]*/>' % (nr, nr), x, re.S)
if nxt: assert not re.search(r'<v>|<t>|<t ', nxt.group(0)), 'next row not empty'
bstr = 't="s"' in (re.search(r'<c r="B%d"([^>]*)>' % rn, target.group(0)).group(1)) or 'inlineStr' in target.group(0).split('<c r="C')[0]
newrow = re.sub(r'r="([A-Z]+)%d"' % rn, lambda mm: 'r="%s%d"' % (mm.group(1), nr), target.group(0).replace('r="%d"' % rn, 'r="%d"' % nr, 1))
def setc(rowxml, col, val, kind):
    m = re.search(r'<c r="%s%d"([^>]*?)(/>|>(.*?)</c>)' % (col, nr), rowxml, re.S)
    style = re.search(r' s="(\d+)"', m.group(1)) if m else None; s = ' s="%s"' % style.group(1) if style else ''
    c = ('<c r="%s%d"%s t="inlineStr"><is><t xml:space="preserve">%s</t></is></c>' % (col, nr, s, esc(str(val))) if kind == 'str'
         else '<c r="%s%d"%s><v>%s</v></c>' % (col, nr, s, val))
    return rowxml.replace(m.group(0), c) if m else rowxml
newrow = setc(newrow, 'B', vc['version'], 'str' if bstr else 'num')
newrow = setc(newrow, 'C', (datetime.date.fromisoformat(vc['date']) - datetime.date(1899, 12, 30)).days, 'num')
for col, key in (('D', 'desc'), ('E', 'status'), ('F', 'author')): newrow = setc(newrow, col, vc[key], 'str')
x = x.replace(nxt.group(0), newrow) if nxt else x.replace(target.group(0), target.group(0) + newrow)
data[p] = x.encode('utf8')
ssx = ss[:ss.find('<si>')] + ''.join(sis) + ss[ss.rfind('</si>') + 5:]
ssx = re.sub(r'uniqueCount="\d+"', 'uniqueCount="%d"' % len(sis), ssx, 1); data['xl/sharedStrings.xml'] = ssx.encode('utf8')
with zipfile.ZipFile(dst, 'w') as out:
    for info in z.infolist(): out.writestr(info, data[info.filename])
for l in log: print('==', l[0], l[1]); print('  OLD:', l[2][:300]); print('  NEW:', l[3][:400])
print('VC row', nr, 'added after row', rn, '| B as', 'str' if bstr else 'num')

"""Remove a block of rows and edit text cells in a final spec by XML surgery (no openpyxl save).
Usage: python -I scripts/remove_block.py <map.json>
map = {"src": "05-final/<file>.xlsx",
       "delete_rows": {"<sheet>": [row, ...]},                 # rows removed, rows below shift up
       "edits": [[sheet, cell, old_substring, new_substring]]}  # cell refs BEFORE the deletion; new '' on the whole text clears the cell
The previous copy goes to 05-final/_previous/<name>.<timestamp>.xlsx (or "prev_dir", relative to src, when given; "src" may be absolute); the result replaces the file."""
import zipfile, re, sys, html, json, os, shutil, datetime
sys.stdout.reconfigure(encoding='utf-8')
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
M = json.load(open(sys.argv[1], encoding='utf-8'))
src = os.path.join(ROOT, M['src'])
z = zipfile.ZipFile(src); data = {n: z.read(n) for n in z.namelist()}
wb = data['xl/workbook.xml'].decode('utf8'); rels = data['xl/_rels/workbook.xml.rels'].decode('utf8')
rid2t = {re.search(r'Id="([^"]+)"', m).group(1): re.search(r'Target="([^"]+)"', m).group(1) for m in re.findall(r'<Relationship\b[^>]*/>', rels)}
part = {}
for name, rid in re.findall(r'<sheet\b[^>]*name="([^"]+)"[^>]*r:id="([^"]+)"', wb):
    t = rid2t[rid].lstrip('/'); part[html.unescape(name)] = t if t.startswith('xl/') else 'xl/' + t
ss = data['xl/sharedStrings.xml'].decode('utf8') if 'xl/sharedStrings.xml' in data else None
sis = re.findall(r'<si>.*?</si>', ss, re.S) if ss else []
def si_text(s): return html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>', s, re.S)))
def esc(s): return html.escape(s, quote=False)
log = []
# 1. text edits (before any row shift)
for sh, cell, o, n in M['edits']:
    p = part[sh]; x = data[p].decode('utf8')
    m = re.search(r'<c r="%s"([^>]*?)(?:/>|>(.*?)</c>)' % cell, x, re.S); assert m, (sh, cell)
    attrs, body = m.group(1), m.group(2) or ''
    if 't="s"' in attrs: cur = si_text(sis[int(re.search(r'<v>(\d+)</v>', body).group(1))])
    elif 'inlineStr' in attrs: cur = html.unescape(''.join(re.findall(r'<t[^>]*>(.*?)</t>', body, re.S)))
    else: raise SystemExit('unsupported cell %s %s' % (sh, cell))
    assert cur.count(o) == 1, (sh, cell, 'old text count', cur.count(o))
    new = cur.replace(o, n)
    a2 = re.sub(r'\s*t="[^"]*"', '', attrs)
    c = '<c r="%s"%s/>' % (cell, a2) if new == '' else '<c r="%s"%s t="inlineStr"><is><t xml:space="preserve">%s</t></is></c>' % (cell, a2, esc(new))
    x = x[:m.start()] + c + x[m.end():]; data[p] = x.encode('utf8'); log.append((sh, cell, cur, new))
# 2. row deletions
def shift_ref(ref, dels):
    col, row = re.match(r'([A-Z]+)(\d+)', ref).groups(); row = int(row)
    return '%s%d' % (col, row - sum(1 for d in dels if d < row))
for sh, dels in M.get('delete_rows', {}).items():
    dels = sorted(set(dels)); p = part[sh]; x = data[p].decode('utf8')
    i0, i1 = x.index('<sheetData>') + len('<sheetData>'), x.index('</sheetData>')
    out = []
    for r in re.finditer(r'<row r="(\d+)"[^>]*?(?:/>|>.*?</row>)', x[i0:i1], re.S):
        rn = int(r.group(1)); rx = r.group(0)
        if rn in dels: continue
        k = sum(1 for d in dels if d < rn)
        if k:
            rx = re.sub(r'^<row r="\d+"', '<row r="%d"' % (rn - k), rx)
            rx = re.sub(r'<c r="([A-Z]+)%d"' % rn, lambda mm: '<c r="%s%d"' % (mm.group(1), rn - k), rx)
        out.append(rx)
    x = x[:i0] + ''.join(out) + x[i1:]
    def fix_merge(mm):
        a, b = mm.group(1).split(':'); ra, rb = int(re.sub(r'\D', '', a)), int(re.sub(r'\D', '', b))
        if all(r in dels for r in range(ra, rb + 1)): return ''
        assert not any(d in range(ra, rb + 1) for d in dels), ('partial merge', mm.group(1))
        return '<mergeCell ref="%s:%s"/>' % (shift_ref(a, dels), shift_ref(b, dels))
    x = re.sub(r'<mergeCell ref="([^"]+)"/>', fix_merge, x)
    cnt = len(re.findall(r'<mergeCell ref=', x))
    x = re.sub(r'<mergeCells count="\d+">', '<mergeCells count="%d">' % cnt, x)
    x = x.replace('<mergeCells count="0"></mergeCells>', '')
    for tag in ('<conditionalFormatting', '<dataValidation ', '<hyperlink ', '<f>', '<f '):
        assert tag not in x, ('unsupported feature in', sh, tag)
    data[p] = x.encode('utf8'); log.append((sh, 'rows', 'deleted %s' % dels, ''))
tmp = src + '.tmp'
with zipfile.ZipFile(tmp, 'w', zipfile.ZIP_DEFLATED) as o:
    for info in z.infolist(): o.writestr(info, data[info.filename])
z.close()
prev = os.path.join(os.path.dirname(src), M['prev_dir']) if 'prev_dir' in M else os.path.join(ROOT, '05-final', '_previous'); os.makedirs(prev, exist_ok=True)
base = os.path.basename(src)[:-5]
shutil.copy2(src, os.path.join(prev, '%s.%s.xlsx' % (base, datetime.datetime.now().strftime('%Y%m%d-%H%M%S'))))
os.replace(tmp, src)
for l in log: print('==', l[0], l[1]); print('  OLD:', l[2][:200]); print('  NEW:', l[3][:200])

# HRBS-16029: WTC SG V4.2 -> V4.3 (62866 CPF-able, Additional Wages). Edicao XML + copia byte a byte das demais partes.
import zipfile, re, sys, datetime
from xml.sax.saxutils import escape
BASE, OUT = sys.argv[1], sys.argv[2]
z = zipfile.ZipFile(BASE)
P = {n: z.read(n) for n in z.namelist()}
sst = P['xl/sharedStrings.xml'].decode('utf-8')
sis = re.findall(r'<si>.*?</si>', sst, re.S)
def add_str(t):
    global sst, sis
    sst = sst.replace('</sst>', '<si><t xml:space="preserve">%s</t></si></sst>' % escape(t))
    sis.append(t); return len(sis) - 1
def sidx(t):
    for i, x in enumerate(sis):
        if re.sub(r'<[^>]+>', '', x) == t: return i
    raise SystemExit('string nao encontrada: ' + t)
YES, AW, UR = sidx('Yes'), sidx('Additional Wages'), sidx('Under Review')
REMARK = add_str('Cash payment through payroll is wages for CPF and SDL (CPF Act s.2; SDL Act s.2). One-off payment: Additional Wages (CPF Act, First Schedule para 5(d)). HRBS-16029.')
VCTXT = add_str('62866 Childbirth Allowance: Subject to CPF No -> Yes; Ordinary/Additional Wage NA -> Additional Wages (HRBS-16029)')
AUTH = add_str('Wallisson Gomes')
n = len(sis)
sst = re.sub(r'uniqueCount="\d+"', 'uniqueCount="%d"' % n, sst)
# estilos: fill azul-claro + clones dos xf usados
st = P['xl/styles.xml'].decode('utf-8')
nf = int(re.search(r'<fills count="(\d+)">', st).group(1))
st = st.replace('</fills>', '<fill><patternFill patternType="solid"><fgColor rgb="FFDDEBF7"/><bgColor rgb="FFDDEBF7"/></patternFill></fill></fills>')
st = re.sub(r'<fills count="\d+">', '<fills count="%d">' % (nf + 1), st)
xfblk = re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>', st, re.S)
xs = re.findall(r'<xf [^>]*/>|<xf [^>]*[^/]>.*?</xf>', xfblk.group(2), re.S)
newx = {}
def blue(sid):
    if sid in newx: return newx[sid]
    x = re.sub(r'fillId="\d+"', 'fillId="%d"' % nf, xs[sid])
    if 'applyFill' not in x: x = x.replace('<xf ', '<xf applyFill="1" ', 1)
    xs.append(x); newx[sid] = len(xs) - 1; return newx[sid]
def cell(ref, sid, val=None, kind='s'):
    if val is None: return '<c r="%s" s="%d"/>' % (ref, sid)
    if kind == 's': return '<c r="%s" s="%d" t="s"><v>%d</v></c>' % (ref, sid, val)
    return '<c r="%s" s="%d"><v>%s</v></c>' % (ref, sid, val)
def setc(xml, ref, new):
    pat = r'<c r="%s"[^>]*?(?:/>|>.*?</c>)' % ref
    if len(re.findall(pat, xml, re.S)) != 1: raise SystemExit('celula ' + ref)
    return re.sub(pat, new, xml, count=1, flags=re.S)
s2 = P['xl/worksheets/sheet2.xml'].decode('utf-8')
assert '<c r="A685" s="15"><v>62866.0</v></c>' in s2
assert '<c r="N685" s="15" t="s"><v>30</v></c>' in s2 and '<c r="Q685" s="15" t="s"><v>46</v></c>' in s2 and '<c r="T685" s="5"/>' in s2
s2 = setc(s2, 'N685', cell('N685', blue(15), YES))
s2 = setc(s2, 'Q685', cell('Q685', blue(15), AW))
s2 = setc(s2, 'T685', cell('T685', blue(5), REMARK))
s1 = P['xl/worksheets/sheet1.xml'].decode('utf-8')
assert '<c r="B32" s="4"/>' in s1 and '<c r="D32" s="7"/>' in s1
serial = (datetime.date(2026, 10, 27) - datetime.date(1899, 12, 30)).days
s1 = setc(s1, 'B32', cell('B32', blue(35), '4.3', 'n'))
s1 = setc(s1, 'C32', cell('C32', blue(47), '%d.0' % serial, 'n'))
s1 = setc(s1, 'D32', cell('D32', blue(40), VCTXT))
s1 = setc(s1, 'E32', cell('E32', blue(42), UR))
s1 = setc(s1, 'F32', cell('F32', blue(35), AUTH))
st = st[:xfblk.start()] + '<cellXfs count="%d">%s</cellXfs>' % (len(xs), ''.join(xs)) + st[xfblk.end():]
P['xl/sharedStrings.xml'] = sst.encode('utf-8'); P['xl/styles.xml'] = st.encode('utf-8')
P['xl/worksheets/sheet1.xml'] = s1.encode('utf-8'); P['xl/worksheets/sheet2.xml'] = s2.encode('utf-8')
with zipfile.ZipFile(OUT, 'w') as o:
    for i in z.infolist():
        if i.filename in ('xl/sharedStrings.xml', 'xl/styles.xml', 'xl/worksheets/sheet1.xml', 'xl/worksheets/sheet2.xml'):
            o.writestr(i, P[i.filename], compress_type=zipfile.ZIP_DEFLATED)
        else:
            o.writestr(i, z.read(i.filename), compress_type=i.compress_type)
print('ok', OUT)

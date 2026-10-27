# -*- coding: utf-8 -*-
"""Gera a v1.2 da spec SNHI por cirurgia XML (skill mercans-pipeline-methodology §4).
Uso: python -I build_v12.py <base.xlsx> <saida.xlsx>
- Só sheet1/2/3.xml e styles.xml são reescritos; demais partes copiadas com os mesmos bytes.
- Célula alterada/nova: estilo original clonado com preenchimento FFDDEBF7.
- Strings novas como inlineStr (sharedStrings.xml intocado)."""
import datetime, re, sys, zipfile, os
from xml.sax.saxutils import escape
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edits_v12 import EDITS

BLUE = "FFDDEBF7"
base, out = sys.argv[1], sys.argv[2]
zin = zipfile.ZipInfo
src = zipfile.ZipFile(base)
parts = {i.filename: src.read(i.filename) for i in src.infolist()}

# ---------- styles: novo fill + clones dos xf ----------
st = parts["xl/styles.xml"].decode("utf-8")
m = re.search(r'<fills count="(\d+)">(.*?)</fills>', st, re.S)
nfill = int(m.group(1))
assert len(re.findall(r"<fill>", m.group(2))) == nfill
newfill = ('<fill><patternFill patternType="solid"><fgColor rgb="%s"/><bgColor rgb="%s"/>'
           '</patternFill></fill>' % (BLUE, BLUE))
st = st.replace(m.group(0), '<fills count="%d">%s%s</fills>' % (nfill + 1, m.group(2), newfill), 1)
blue_fill_id = nfill

m = re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>', st, re.S)
xfs = re.findall(r'<xf [^>]*?(?:/>|>.*?</xf>)', m.group(2), re.S)
assert len(xfs) == int(m.group(1)), (len(xfs), m.group(1))
clone_of = {}
added = []

def blue_style(s):
    s = int(s)
    if s not in clone_of:
        x = xfs[s]
        x = re.sub(r'fillId="\d+"', 'fillId="%d"' % blue_fill_id, x, count=1)
        if 'applyFill="' in x:
            x = re.sub(r'applyFill="\d"', 'applyFill="1"', x, count=1)
        else:
            x = x.replace("<xf ", '<xf applyFill="1" ', 1)
        clone_of[s] = len(xfs) + len(added)
        added.append(x)
    return clone_of[s]

# ---------- folhas ----------
def excel_serial(d):
    return (d - datetime.date(1899, 12, 30)).days

sheets = {}
for part, cell, kind, val, _src in EDITS:
    sheets.setdefault(part, []).append((cell, kind, val))

for part, cells in sheets.items():
    x = parts[part].decode("utf-8")
    for cell, kind, val in cells:
        pat = re.compile(r'<c r="%s"(?P<a>[^>]*?)(?:/>|>(?P<b>.*?)</c>)' % cell, re.S)
        hits = list(pat.finditer(x))
        assert len(hits) == 1, (part, cell, len(hits))
        h = hits[0]
        sm = re.search(r's="(\d+)"', h.group("a"))
        assert sm, (part, cell, "sem estilo")
        ns = blue_style(sm.group(1))
        if part.endswith("sheet2.xml") and cell == "B23":
            pass  # conferido em compare_v12 (texto antigo preservado como prefixo)
        if kind == "str":
            new = '<c r="%s" s="%d" t="inlineStr"><is><t xml:space="preserve">%s</t></is></c>' % (
                cell, ns, escape(val))
        elif kind == "num":
            new = '<c r="%s" s="%d"><v>%s</v></c>' % (cell, ns, repr(float(val)))
        elif kind == "date":
            new = '<c r="%s" s="%d"><v>%d</v></c>' % (cell, ns, excel_serial(val))
        else:
            raise ValueError(kind)
        x = x[:h.start()] + new + x[h.end():]
    parts[part] = x.encode("utf-8")

st = st.replace(m.group(0), '<cellXfs count="%d">%s%s</cellXfs>' % (
    len(xfs) + len(added), m.group(2), "".join(added)), 1)
parts["xl/styles.xml"] = st.encode("utf-8")

# ---------- reempacotar na mesma ordem ----------
with zipfile.ZipFile(out, "w") as z:
    for i in src.infolist():
        ni = zipfile.ZipInfo(i.filename, date_time=i.date_time)
        ni.compress_type = i.compress_type
        ni.external_attr = i.external_attr
        ni.create_system = i.create_system
        z.writestr(ni, parts[i.filename])
print("ok:", out, "| fill id", blue_fill_id, "| estilos clonados", clone_of)

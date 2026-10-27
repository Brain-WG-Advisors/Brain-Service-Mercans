# -*- coding: utf-8 -*-
"""Build Taiwan Tax Report Spec v1.3 by XML surgery (no openpyxl save).
Usage: python -I -X utf8 build_v1_3.py <base.xlsx> <out.xlsx>
Only xl/styles.xml and the edited sheet XMLs change; every other zip entry is copied byte for byte.
"""
import sys, os, re, zipfile
from xml.sax.saxutils import escape
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from edits_v1_3 import EDITS

BASE, OUT = sys.argv[1], sys.argv[2]
FILL = '<fill><patternFill patternType="solid"><fgColor rgb="FFDDEBF7"/><bgColor rgb="FFDDEBF7"/></patternFill></fill>'

zin = zipfile.ZipFile(BASE)
data = {i.filename: zin.read(i.filename) for i in zin.infolist()}

# sheet name -> part
wb = data["xl/workbook.xml"].decode("utf-8")
rels = data["xl/_rels/workbook.xml.rels"].decode("utf-8")
rid2target = dict(re.findall(r'Id="(rId\d+)"[^>]*Target="([^"]+)"', rels)) or {}
for m in re.finditer(r'<Relationship [^>]*>', rels):
    t = m.group(0)
    rid2target[re.search(r'Id="([^"]+)"', t).group(1)] = re.search(r'Target="([^"]+)"', t).group(1)
sheet_part = {}
for m in re.finditer(r'<sheet [^>]*name="([^"]+)"[^>]*r:id="([^"]+)"', wb):
    sheet_part[m.group(1)] = "xl/" + rid2target[m.group(2)]

# styles: add fill, clone xfs
st = data["xl/styles.xml"].decode("utf-8")
m = re.search(r'<fills count="(\d+)">', st)
nfills = int(m.group(1)); FILL_ID = nfills
st = st.replace(m.group(0), f'<fills count="{nfills+1}">', 1).replace("</fills>", FILL + "</fills>", 1)
cx = re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>', st, re.S)
xfs = re.findall(r'<xf [^>]*?(?:/>|>.*?</xf>)', cx.group(2), re.S)
assert len(xfs) == int(cx.group(1)), (len(xfs), cx.group(1))
new_xfs, clone_map = [], {}

def clone(s, wrap):
    key = (s, wrap)
    if key in clone_map:
        return clone_map[key]
    x = xfs[s]
    x = re.sub(r'fillId="\d+"', f'fillId="{FILL_ID}"', x)
    if 'applyFill=' not in x:
        x = x.replace('<xf ', '<xf applyFill="1" ', 1)
    if wrap:
        if '<alignment' in x:
            al = re.search(r'<alignment[^>]*/>', x).group(0)
            al2 = re.sub(r'\s*wrapText="\d"', '', al).replace('<alignment', '<alignment wrapText="1"', 1)
            if 'vertical=' not in al2:
                al2 = al2.replace('<alignment', '<alignment vertical="top"', 1)
            x = x.replace(al, al2)
        else:
            if x.endswith('/>'):
                x = x[:-2] + '><alignment vertical="top" wrapText="1"/></xf>'
            x = x.replace('<xf ', '<xf applyAlignment="1" ', 1) if 'applyAlignment' not in x else x
    idx = len(xfs) + len(new_xfs)
    new_xfs.append(x); clone_map[key] = idx
    return idx

changed = {}
for sheet, cells in EDITS.items():
    part = sheet_part[sheet]
    xml = data[part].decode("utf-8")
    for ref, (val, wrap) in cells.items():
        pat = re.compile(r'<c r="%s"(?P<attrs>[^>]*?)(?:/>|>(?P<body>.*?)</c>)' % ref, re.S)
        mm = pat.search(xml)
        assert mm, (sheet, ref)
        sm = re.search(r' s="(\d+)"', mm.group("attrs"))
        s = int(sm.group(1)) if sm else 0
        ns = clone(s, wrap)
        if isinstance(val, (int, float)):
            cell = f'<c r="{ref}" s="{ns}"><v>{val}</v></c>'
        else:
            cell = f'<c r="{ref}" s="{ns}" t="inlineStr"><is><t xml:space="preserve">{escape(val)}</t></is></c>'
        xml = xml[:mm.start()] + cell + xml[mm.end():]
    changed[part] = xml.encode("utf-8")

st = st.replace(cx.group(0), f'<cellXfs count="{len(xfs)+len(new_xfs)}">' + cx.group(2) + "".join(new_xfs) + "</cellXfs>")
changed["xl/styles.xml"] = st.encode("utf-8")

with zipfile.ZipFile(OUT, "w") as zout:
    for info in zin.infolist():
        if info.filename in changed:
            zi = zipfile.ZipInfo(info.filename, date_time=info.date_time)
            zi.compress_type = info.compress_type; zi.external_attr = info.external_attr
            zout.writestr(zi, changed[info.filename])
        else:
            zout.writestr(info, data[info.filename])  # same bytes, same ZipInfo
print("parts changed:", sorted(changed)); print("new xfs:", len(new_xfs), "fillId:", FILL_ID)

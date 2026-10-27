"""DD Spain V5.1 -> V5.2: ESS = Write for the Modelo 145 fields of Employee Tax Relief Declaration (Nihita, chat STG 20/10).
Fields outside Form 145 keep ESS = Read. Birth Year rows get Form 145 = Yes. Changed cells in FFFFE699."""
import re, sys, zipfile, datetime
from xml.sax.saxutils import escape
import openpyxl

SRC, OUT = sys.argv[1], sys.argv[2]
zin = zipfile.ZipFile(SRC)
parts = {n: zin.read(n) for n in zin.namelist()}
wbv = openpyxl.load_workbook(SRC)

styles = parts["xl/styles.xml"].decode("utf-8")
fm = re.search(r'(<fills count=")(\d+)(">)(.*?)(</fills>)', styles, re.S)
FILL = int(fm.group(2))
styles = (styles[:fm.start()] + fm.group(1) + str(FILL + 1) + fm.group(3) + fm.group(4)
          + '<fill><patternFill patternType="solid"><fgColor rgb="FFFFE699"/><bgColor rgb="FFFFE699"/></patternFill></fill>'
          + fm.group(5) + styles[fm.end():])
m = re.search(r'(<cellXfs count=")(\d+)(">)(.*?)(</cellXfs>)', styles, re.S)
xfs = re.findall(r'<xf [^>]*?(?:/>|>.*?</xf>)', m.group(4), re.S)
assert int(m.group(2)) == len(xfs)
new_xfs, clone = [], {}
def hi(s):
    s = int(s)
    if s not in clone:
        x = re.sub(r'fillId="\d+"', f'fillId="{FILL}"', xfs[s])
        if 'applyFill=' not in x:
            x = x.replace('<xf ', '<xf applyFill="1" ', 1)
        clone[s] = len(xfs) + len(new_xfs); new_xfs.append(x)
    return clone[s]
def set_cell(xml, ref, val):
    pat = re.compile(rf'<c r="{ref}"(?P<a>(?: [^>]*?)?)(?:/>|>(?:(?!</c>).)*?</c>)', re.S)
    mm = pat.search(xml); assert mm, ref
    st = re.search(r's="(\d+)"', mm.group("a")); st = st.group(1) if st else "0"
    new = f'<c r="{ref}" s="{hi(st)}" t="inlineStr"><is><t xml:space="preserve">{escape(val)}</t></is></c>'
    return xml[:mm.start()] + new + xml[mm.end():]

CF = wbv["Country Fields"]
# Not declared by the employee on Form 145 (matriz 2026-10-19, Observações): keep ESS = Read
KEEP_READ = {"$hr.perceptor_situation", "$hr.disability_degree", "$hr.child_count_total"}
edits = {}
for r in range(1, CF.max_row + 1):
    if CF.cell(r, 16).value != "employee_tax_relief_declaration": continue
    code = CF.cell(r, 5).value
    if code in KEEP_READ: continue
    if CF.cell(r, 22).value != "Write": edits[f"V{r}"] = "Write"
    if code.endswith("_birth_year") and CF.cell(r, 24).value != "Yes": edits[f"X{r}"] = "Yes"
f = "xl/worksheets/sheet5.xml"; x = parts[f].decode("utf-8")
for ref, val in edits.items(): x = set_cell(x, ref, val)
parts[f] = x.encode("utf-8")

f = "xl/worksheets/sheet1.xml"; s1 = parts[f].decode("utf-8")
row35 = re.search(r'<row r="35"[^>]*>.*?</row>', s1, re.S).group(0)
sty = dict(re.findall(r'<c r="([A-G])35" s="(\d+)"', row35))
serial = (datetime.date(2026, 10, 20) - datetime.date(1899, 12, 30)).days
VC = ("ESS permission confirmed by implementation (STG Spain, 20/10): Employee Tax Relief Declaration fields declared on Form 145 "
      "set to ESS = Write. Perceptor Situation (SITUPER), Disability Degree (%) and Child Count (Total) are not on Form 145 and stay ESS = Read. "
      "Child 1-16 Birth Year marked Form 145 = Yes. Changes in yellow FFFFE699.")
def inl(ref, s, t): return f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{escape(t)}</t></is></c>'
def h(col): return hi(sty[col])
vc_row = (f'<row r="36" ht="15.75" customHeight="1"><c r="A36" s="{sty["A"]}"/><c r="B36" s="{h("B")}"><v>5.2</v></c>'
          f'<c r="C36" s="{h("C")}"><v>{serial}.0</v></c>' + inl("D36", h("D"), VC) + inl("E36", h("E"), "Draft")
          + inl("F36", h("F"), "Wallisson Gomes") + f'<c r="G36" s="{sty["G"]}"/></row>')
def rows1(mm):
    r = int(mm.group(2)); nr = r + 1 if r >= 36 else r
    body = re.sub(r'(<c r=")([A-Z]+)(\d+)(")', lambda q: f'{q.group(1)}{q.group(2)}{nr}{q.group(4)}', mm.group(4))
    return (vc_row if r == 36 else "") + f'<row r="{nr}"{mm.group(3)}>{body}</row>'
s1 = re.sub(r'(<row r="(\d+)"([^>]*)>(.*?)</row>)', rows1, s1, flags=re.S)
def shref(ref):
    c, r = re.match(r"([A-Z]+)(\d+)$", ref).groups(); r = int(r)
    return f"{c}{r + 1 if r >= 36 else r}"
s1 = re.sub(r'<mergeCell ref="([A-Z]+\d+):([A-Z]+\d+)"/>', lambda q: f'<mergeCell ref="{shref(q.group(1))}:{shref(q.group(2))}"/>', s1)
s1 = re.sub(r'<dimension ref="([A-Z]+\d+):([A-Z]+)(\d+)"/>', lambda q: f'<dimension ref="{q.group(1)}:{q.group(2)}{int(q.group(3)) + 1}"/>', s1)
parts[f] = s1.encode("utf-8")

m = re.search(r'(<cellXfs count=")(\d+)(">)(.*?)(</cellXfs>)', styles, re.S)
styles = styles[:m.start()] + m.group(1) + str(len(xfs) + len(new_xfs)) + m.group(3) + m.group(4) + "".join(new_xfs) + m.group(5) + styles[m.end():]
parts["xl/styles.xml"] = styles.encode("utf-8")
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
    for info in zin.infolist():
        zo.writestr(info, parts[info.filename])
print("ESS edits", sum(k.startswith("V") for k in edits), "| Form145 edits", sum(k.startswith("X") for k in edits))

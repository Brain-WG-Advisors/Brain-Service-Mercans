"""DD Spain V5.1 consolidated (user decision 20/10: one version for the day).
Input: V5.1 partial (Form 145 wording/order). Adds: ESS = Write for Form 145 fields (Nihita, 20/10), Birth Year Form 145 = Yes,
Form 145 flag cleared for Disability Degree (%) and Child Count (Total), Child Count (Total) fill rule. Same light orange FFFCE4D6."""
import re, sys, zipfile
from xml.sax.saxutils import escape
import openpyxl

SRC, OUT = sys.argv[1], sys.argv[2]
zin = zipfile.ZipFile(SRC)
parts = {n: zin.read(n) for n in zin.namelist()}
wbv = openpyxl.load_workbook(SRC)

styles = parts["xl/styles.xml"].decode("utf-8")
fills = re.findall(r'<fill>.*?</fill>', re.search(r'<fills count="\d+">(.*?)</fills>', styles, re.S).group(1), re.S)
ORANGE = [i for i, f in enumerate(fills) if 'FFFCE4D6' in f]; assert len(ORANGE) == 1; ORANGE = ORANGE[0]
m = re.search(r'(<cellXfs count=")(\d+)(">)(.*?)(</cellXfs>)', styles, re.S)
xfs = re.findall(r'<xf [^>]*?(?:/>|>.*?</xf>)', m.group(4), re.S)
assert int(m.group(2)) == len(xfs)
new_xfs, clone = [], {}
def hi(s):
    s = int(s)
    if f'fillId="{ORANGE}"' in xfs[s] if s < len(xfs) else False:
        return s
    if s not in clone:
        x = re.sub(r'fillId="\d+"', f'fillId="{ORANGE}"', xfs[s])
        if 'applyFill=' not in x:
            x = x.replace('<xf ', '<xf applyFill="1" ', 1)
        clone[s] = len(xfs) + len(new_xfs); new_xfs.append(x)
    return clone[s]
def set_cell(xml, ref, val):
    pat = re.compile(rf'<c r="{ref}"(?P<a>(?: [^>]*?)?)(?:/>|>(?:(?!</c>).)*?</c>)', re.S)
    mm = pat.search(xml); assert mm, ref
    st = re.search(r's="(\d+)"', mm.group("a")); st = st.group(1) if st else "0"
    if val is None:
        new = f'<c r="{ref}" s="{hi(st)}"/>'
    else:
        new = f'<c r="{ref}" s="{hi(st)}" t="inlineStr"><is><t xml:space="preserve">{escape(val)}</t></is></c>'
    return xml[:mm.start()] + new + xml[mm.end():]

CF = wbv["Country Fields"]
NOT_ON_FORM = {"$hr.perceptor_situation", "$hr.disability_degree", "$hr.child_count_total"}
COUNT_RULE = ("Must equal the number of children entered (Child 1-16). Derive automatically if possible; "
              "otherwise HR fills it in MSS. Not a box of Form 145, so ESS = Read.")
edits = {}
for r in range(1, CF.max_row + 1):
    if CF.cell(r, 16).value != "employee_tax_relief_declaration": continue
    code = CF.cell(r, 5).value
    if code in NOT_ON_FORM:
        if code != "$hr.perceptor_situation" and CF.cell(r, 24).value is not None: edits[f"X{r}"] = None
        if code == "$hr.child_count_total":
            edits[f"G{r}"] = CF.cell(r, 7).value.rstrip() + " " + COUNT_RULE
        continue
    if CF.cell(r, 22).value != "Write": edits[f"V{r}"] = "Write"
    if code.endswith("_birth_year") and CF.cell(r, 24).value != "Yes": edits[f"X{r}"] = "Yes"
f = "xl/worksheets/sheet5.xml"; x = parts[f].decode("utf-8")
for ref, val in edits.items(): x = set_cell(x, ref, val)
parts[f] = x.encode("utf-8")

VC = ("STG Spain feedback on the ESS (Modelo 145), Employee Tax Relief Declaration: official Form 145 wording added as ESS help text; "
      "Family Situation and Disability option texts aligned to the form; Related Person NIF renamed Spouse NIF, required only when "
      "Family Situation = 2; Disability shown in ESS as 3 options plus the assistance flag (key 2 derived for Modelo 190), flag only "
      "with 33%-65%; Descendants and Ascendants ordinals follow the form order; ESS = Write for the fields declared on Form 145 "
      "(confirmed by implementation, 20/10); Perceptor Situation, Disability Degree (%) and Child Count (Total) are not on the form "
      "and stay ESS = Read; Child Count (Total) must equal the children entered. Internal codes unchanged. Changes in light orange.")
f = "xl/worksheets/sheet1.xml"; s1 = parts[f].decode("utf-8")
mm = re.search(r'<c r="D35" s="(\d+)" t="inlineStr"><is><t xml:space="preserve">[^<]*</t></is></c>', s1); assert mm
s1 = s1[:mm.start()] + f'<c r="D35" s="{mm.group(1)}" t="inlineStr"><is><t xml:space="preserve">{escape(VC)}</t></is></c>' + s1[mm.end():]
parts[f] = s1.encode("utf-8")

m = re.search(r'(<cellXfs count=")(\d+)(">)(.*?)(</cellXfs>)', styles, re.S)
styles = styles[:m.start()] + m.group(1) + str(len(xfs) + len(new_xfs)) + m.group(3) + m.group(4) + "".join(new_xfs) + m.group(5) + styles[m.end():]
parts["xl/styles.xml"] = styles.encode("utf-8")
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
    for info in zin.infolist():
        zo.writestr(info, parts[info.filename])
print("edits", len(edits), {k[0]: sum(1 for e in edits if e[0] == k[0]) for k in edits}, "new xfs", len(new_xfs))

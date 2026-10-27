# -*- coding: utf-8 -*-
"""Rodada 2 (achados #2-#10 da REVISAO-independente.md) sobre a saida da rodada 1.

Uso: python -I build_v2_2_r2.py <v2.2_r1.xlsx> <v2.2_final.xlsx> <anexo_D24E.txt>
Pipeline completo:  v2.1 --build_v2_2.py--> r1 --build_v2_2_r2.py--> v2.2
Mesma tecnica: cirurgia XML + zip, strings acrescentadas, destaque FFDDEBF7.
Atualiza changes_manifest.json (valor final por celula; tag de mudanca acumulada)
e grava changes_r2.json (antes da rodada 2 -> depois).
"""
import json, math, re, sys, zipfile
from pathlib import Path
from xml.sax.saxutils import escape

SRC, OUT, ANEXO_E = sys.argv[1], sys.argv[2], sys.argv[3]
HERE = Path(__file__).resolve().parent
HL = "FFDDEBF7"
zin = zipfile.ZipFile(SRC)
parts = {n: zin.read(n) for n in zin.namelist()}
txt = lambda n: parts[n].decode("utf-8")

def unesc(s):
    return s.replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&apos;", "'").replace("&amp;", "&")
sst = txt("xl/sharedStrings.xml")
si_texts = ["".join(re.findall(r"<t[^>]*>(.*?)</t>", si, flags=re.S)) for si in re.findall(r"<si>(.*?)</si>", sst, flags=re.S)]
si_texts = [unesc(t) for t in si_texts]
sst_unique = int(re.search(r'uniqueCount="(\d+)"', sst).group(1)); sst_count = int(re.search(r' count="(\d+)"', sst).group(1))
new_si = []
def add_string(s):
    global sst_unique, sst_count
    new_si.append('<si><t xml:space="preserve">%s</t></si>' % escape(s)); si_texts.append(s)
    sst_unique += 1; sst_count += 1
    return sst_unique - 1

sty = txt("xl/styles.xml")
fills = re.findall(r"<fill>.*?</fill>", re.search(r"<fills[^>]*>(.*?)</fills>", sty, flags=re.S).group(1), flags=re.S)
HL_FILL = next(i for i, f in enumerate(fills) if HL in f)          # fill criado na rodada 1
xfs_block = re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>', sty, flags=re.S)
xf_list = re.findall(r"<xf [^>]*?/>|<xf [^>]*?>.*?</xf>", xfs_block.group(2), flags=re.S)
new_xfs, hl_cache = [], {}
def hl_style(s):
    s = int(s)
    if re.search(r'fillId="%d"' % HL_FILL, xf_list[s]): return s     # ja destacado
    if s in hl_cache: return hl_cache[s]
    x = re.sub(r'fillId="\d+"', 'fillId="%d"' % HL_FILL, xf_list[s], count=1)
    if "applyFill" not in x: x = x.replace("<xf ", '<xf applyFill="1" ', 1)
    new_xfs.append(x); hl_cache[s] = len(xf_list) + len(new_xfs) - 1
    return hl_cache[s]

wb = txt("xl/workbook.xml"); rels = txt("xl/_rels/workbook.xml.rels")
sheet_file = {}
for name, rid in re.findall(r'<sheet state="visible" name="([^"]+)" sheetId="\d+" r:id="(rId\d+)"/>', wb):
    sheet_file[name] = "xl/" + re.search(r'Id="%s" Type="[^"]+" Target="([^"]+)"' % rid, rels).group(1)
sheets = {}
def sx(n):
    if n not in sheets: sheets[n] = txt(sheet_file[n])
    return sheets[n]
def col_idx(c):
    n = 0
    for ch in c: n = n * 26 + ord(ch) - 64
    return n
CELL = r'<c r="%s"(?: [^>/]*)?(?:/>|>(.*?)</c>)'
def read_cell(x, ref):
    m = re.search(CELL % ref, x, flags=re.S)
    tag = m.group(0); s = re.search(r' s="(\d+)"', tag).group(1)
    v = re.search(r"<v>(.*?)</v>", tag)
    return s, (si_texts[int(v.group(1))] if (' t="s"' in tag and v) else (v.group(1) if v else None))

r2 = []; touched = {}
def set_cell(sheet, ref, text, change):
    x = sx(sheet); old_s, old_v = read_cell(x, ref)
    if old_v == text: raise SystemExit("sem mudanca: %s!%s" % (sheet, ref))
    newc = '<c r="%s" s="%d" t="s"><v>%d</v></c>' % (ref, hl_style(old_s), add_string(text))
    m = re.search(CELL % ref, x, flags=re.S)
    sheets[sheet] = x[:m.start()] + newc + x[m.end():]
    r2.append({"sheet": sheet, "cell": ref, "change": change, "before_r2": old_v, "new": text})
    touched.setdefault(sheet, {}).setdefault(int(re.sub(r"[A-Z]", "", ref)), []).append((col_idx(re.sub(r"\d", "", ref)), text))
def fit_rows():
    for sheet, rows in touched.items():
        x = sx(sheet)
        w = {}
        for a, b, wd in re.findall(r'<col [^>]*?min="(\d+)" max="(\d+)" width="([\d.]+)"', x):
            for i in range(int(a), int(b) + 1): w[i] = float(wd)
        for row, cells in rows.items():
            lines = max(sum(max(1, math.ceil(len(p) / max(8, int(w.get(ci, 14.43) * 1.15)))) for p in t.split("\n")) for ci, t in cells)
            need = round(lines * 15.0 + 6, 2)
            rm = re.search(r'<row r="%d"((?: [^>/]*)?)(/?)>' % row, x); attrs = rm.group(1)
            cur = re.search(r' ht="([\d.]+)"', attrs)
            if cur and float(cur.group(1)) >= need: continue
            attrs = re.sub(r' customHeight="\d"', "", re.sub(r' ht="[\d.]+"', "", attrs)) + ' ht="%s" customHeight="1"' % need
            x = x[:rm.start()] + '<row r="%d"%s%s>' % (row, attrs, rm.group(2)) + x[rm.end():]
        sheets[sheet] = x

DS, FO, ER, RM, PR, SF, HK = "DAS Spec", "Field Options", "Evidence Register", "Report Matrix", "Population Rules", "Sample File", "Henkel Configuration"

# #2 Payroll.ReferenceYear nao existe no DD v1.1
for r in ("L6", "L20"):
    set_cell(DS, r, "Run parameter (reference year, CCYY) - not a DD field", "R2-#2")

# #3 Field Name real do DZ-DD-001-v1.1 em toda citacao "DD: X.Y"
EST = "NEW DD FIELD (proposed): Employee Establishment (CNAS employer-number assignment)"
FN = lambda alias, name, tab: "DD: %s - Field Name '%s' (DZ-DD-001-v1.1, %s)" % (alias, name, tab)
set_cell(DS, "L4", FN("Employer.CNASNumber", "Employer CNAS Contributor Number", "ID Information") + " of the employee's establishment, resolved via " + EST, "R2-#3")
set_cell(DS, "L19", FN("Employer.CNASNumber", "Employer CNAS Contributor Number", "ID Information") + " of the employee's establishment, resolved via " + EST, "R2-#3")
set_cell(DS, "L7", FN("Employer.CNASCentre", "Employer CNAS Paying Centre", "ID Information") + " of the establishment's CNAS employer number", "R2-#3")
set_cell(DS, "L9", FN("Employer.LegalName", "Employer Legal Name", "Country Fields"), "R2-#3")
set_cell(DS, "L10", "NEW DD FIELD (proposed): Establishment Address (Adresse de l'établissement, AN50). " + FN("Employer.Address", "Employer Head-Office Address", "Country Fields") + " holds the head-office address only.", "R2-#3")
set_cell(DS, "L22", FN("Employee.SSNumber", "Employee CNAS Social Security Number", "ID Information"), "R2-#3")
set_cell(DS, "L23", FN("Employee.LastName", "Surname", "Country Fields"), "R2-#3")
set_cell(DS, "L24", FN("Employee.FirstName", "First Name", "Country Fields"), "R2-#3")
set_cell(DS, "L25", FN("Employee.BirthDate", "Date of Birth", "Country Fields"), "R2-#3")
set_cell(DS, "L39", FN("Employee.HireDate", "Date of Hire", "Country Fields"), "R2-#3")
set_cell(DS, "L40", FN("Employee.TerminationDate", "Date of Termination", "Country Fields"), "R2-#3")
set_cell(DS, "L41", "Blank (20 spaces) by default. " + FN("Employee.JobTitle", "Job Title / Occupation", "Country Fields") + " only where the client opts in.", "R2-#3")

# #4 conteudo de cliente fora do corpo do padrao pais
for q, r in ((1, 26), (2, 29), (3, 32), (4, 35)):
    set_cell(DS, "L%d" % r, "Derived: duration worked in Q%d, in the unit of the Q%d unit field - months (M, 0-3), DAYS (J, 0-92: the client's full-quarter day convention minus unpaid-absence days) or hours (H). Never hours with unit J; never 'Working Hours'. The client's day convention and absence wage types are recorded in its configuration annex." % (q, q), "R2-#4")
for r in ("M27", "M30", "M33", "M36"):
    set_cell(DS, r, "M = mensuel, J = journalier, H = horaire. Guide p.36 prescribes M for monthly-paid workers. The unit is a CLIENT-LEVEL PARAMETER: the client decides and records it in its configuration annex; it is not a compliance decision. The duration feeds the insured-period record used for pension validation.", "R2-#4")

# #5 unidade como parametro (coerencia com C6)
set_cell(ER, "D9", "Normative code list (M / J / H). Which unit applies is a client-level parameter (v2.2); the guide prescribes M for monthly-paid workers.", "R2-#5")
set_cell(FO, "F7", "Monthly-paid worker (guide p.36: travailleurs mensuels). Durée expressed in MONTHS; full quarter = 3. Selected through the client-level DAS unit parameter. NOTE: the value basis is inferred — M has not been observed in an accepted file.", "R2-#5")
set_cell(FO, "F8", "Day-paid worker (guide p.36: journaliers). Durée expressed in DAYS on a 30-day-month convention; full quarter = 90. Selected through the client-level DAS unit parameter. The only unit observed in an accepted file.", "R2-#5")
set_cell(FO, "F9", "Hourly-paid worker (guide p.36: payés à l'heure). Durée expressed in HOURS; full quarter ≈ 520 (3 x 173.33). Selected through the client-level DAS unit parameter. NOTE: the value basis is inferred — H has not been observed in an accepted file.", "R2-#5")

# #6 B28: prazo nao vem do guia
_, b28 = read_cell(sx(RM), "B28")
old = "All 36 fields, both filenames, the centimes and no-separator rules, the M/J/H unit rule, the deadline and the complete p.41-42 validation catalogue are taken verbatim from the guide and confirmed against the live portal copy."
assert old in b28
set_cell(RM, "B28", b28.replace(old, "All 36 fields, both filenames, the centimes and no-separator rules, the M/J/H unit codes and the complete p.41-42 validation catalogue are taken verbatim from the guide and confirmed against the live portal copy. The filing deadline is NOT in the guide: its source is Loi n° 83-14 art. 14 (30 days after the end of the calendar year; ⚠️ 31 January not confirmed by a regulatory text)."), "R2-#6")

# #7 Sample File: Observation em branco (ultimas 20 posicoes) nos 4 registros
for r in ("A10", "A11", "A12", "A13"):
    _, v = read_cell(sx(SF), r)
    assert len(v) == 194
    set_cell(SF, r, v[:174] + " " * 20, "R2-#7")

# #8 Henkel C5:F5 a partir do entete 2024 aceito (dados da empresa)
e = open(ANEXO_E, "rb").read().decode("latin-1")
assert len(e) == 216 and e[0:10] == "1638091858"
NOTE = " (from accepted DAS 2024 header; client to confirm)"
set_cell(HK, "C5", e[15:20].rstrip() + NOTE, "R2-#8")
set_cell(HK, "D5", e[20:50].rstrip() + NOTE, "R2-#8")
set_cell(HK, "E5", e[50:80].rstrip() + " (from accepted DAS 2024 header - this field carried the activity, not a legal name; client to confirm)", "R2-#8")
set_cell(HK, "F5", e[80:130].rstrip() + NOTE, "R2-#8")

# #9 tier B para numeracao por arquivo
set_cell(PR, "D28", "B", "R2-#9")
# #10 tamanho do nome do arquivo
set_cell(DS, "I3", "18", "R2-#10")
set_cell(DS, "I18", "18", "R2-#10")

fit_rows()

out = dict(parts)
for n, x in sheets.items(): out[sheet_file[n]] = x.encode("utf-8")
sst = re.sub(r'count="\d+" uniqueCount="\d+"', 'count="%d" uniqueCount="%d"' % (sst_count, sst_unique), sst, count=1)
out["xl/sharedStrings.xml"] = sst.replace("</sst>", "".join(new_si) + "</sst>").encode("utf-8")
if new_xfs:
    sty = sty[:xfs_block.start()] + '<cellXfs count="%d">%s</cellXfs>' % (len(xf_list) + len(new_xfs), xfs_block.group(2) + "".join(new_xfs)) + sty[xfs_block.end():]
out["xl/styles.xml"] = sty.encode("utf-8")
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
    for info in zin.infolist():
        zo.writestr(info.filename, out[info.filename], compress_type=zipfile.ZIP_DEFLATED)

# manifesto consolidado (v2.1 -> final)
man = json.load(open(HERE / "changes_manifest.json", encoding="utf-8"))
idx = {(c["sheet"], c["cell"]): c for c in man["changes"]}
for c in r2:
    k = (c["sheet"], c["cell"])
    if k in idx:
        idx[k]["change"] += "+" + c["change"]; idx[k]["new"] = c["new"]
    else:
        e2 = {"sheet": c["sheet"], "cell": c["cell"], "change": c["change"], "old": c["before_r2"], "new": c["new"]}
        man["changes"].append(e2); idx[k] = e2
json.dump(man, open(HERE / "changes_manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
json.dump(r2, open(HERE / "changes_r2.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("rodada 2: %d celulas; novos estilos %d" % (len(r2), len(new_xfs)))

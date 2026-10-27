# -*- coding: utf-8 -*-
"""Gera DZ-CNAS-DAS-CountryStandard-Spec_v2.2.xlsx a partir da v2.1 por cirurgia XML.

Uso: python -I build_v2_2.py <v2.1.xlsx> <saida_v2.2.xlsx>
- Partes nao alteradas sao copiadas byte a byte (mesmo conteudo descomprimido).
- Toda celula alterada/nova recebe preenchimento FFDDEBF7 (clone do estilo original).
- Cada alteracao leva um ID de mudanca (C1..C11) gravado em changes_manifest.json
  para a conferencia celula a celula (compare_v21_v22.py).
"""
import json, math, re, sys, zipfile
from pathlib import Path
from xml.sax.saxutils import escape

SRC, OUT = sys.argv[1], sys.argv[2]
HERE = Path(__file__).resolve().parent
HL = "FFDDEBF7"

zin = zipfile.ZipFile(SRC)
parts = {n: zin.read(n) for n in zin.namelist()}
txt = lambda n: parts[n].decode("utf-8")

# ---------------------------------------------------------------- shared strings
sst = txt("xl/sharedStrings.xml")
sst_unique = int(re.search(r'uniqueCount="(\d+)"', sst).group(1))
sst_count = int(re.search(r' count="(\d+)"', sst).group(1))
new_si = []
def add_string(s):
    global sst_unique, sst_count
    new_si.append('<si><t xml:space="preserve">%s</t></si>' % escape(s))
    sst_unique += 1; sst_count += 1
    return sst_unique - 1
# map existing strings (for reading originals)
si_list = re.findall(r"<si>(.*?)</si>", sst, flags=re.S)
def si_text(i):
    return "".join(re.findall(r"<t[^>]*>(.*?)</t>", si_list[i], flags=re.S)).replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&apos;", "'")

# ---------------------------------------------------------------- styles
sty = txt("xl/styles.xml")
fills_count = int(re.search(r'<fills count="(\d+)"', sty).group(1))
sty = sty.replace('<fills count="%d">' % fills_count, '<fills count="%d">' % (fills_count + 1))
sty = sty.replace("</fills>", '<fill><patternFill patternType="solid"><fgColor rgb="%s"/><bgColor rgb="%s"/></patternFill></fill></fills>' % (HL, HL))
HL_FILL = fills_count
xfs_block = re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>', sty, flags=re.S)
xf_list = re.findall(r"<xf [^>]*?/>|<xf [^>]*?>.*?</xf>", xfs_block.group(2), flags=re.S)
new_xfs, hl_cache = [], {}
def hl_style(s):
    s = int(s)
    if s in hl_cache: return hl_cache[s]
    base = xf_list[s]
    x = re.sub(r'fillId="\d+"', 'fillId="%d"' % HL_FILL, base, count=1)
    if "applyFill" not in x:
        x = x.replace("<xf ", '<xf applyFill="1" ', 1)
    new_xfs.append(x)
    hl_cache[s] = len(xf_list) + len(new_xfs) - 1
    return hl_cache[s]

# ---------------------------------------------------------------- sheet helpers
sheet_file = {}
wb = txt("xl/workbook.xml"); rels = txt("xl/_rels/workbook.xml.rels")
for name, rid in re.findall(r'<sheet state="visible" name="([^"]+)" sheetId="\d+" r:id="(rId\d+)"/>', wb):
    tgt = re.search(r'Id="%s" Type="[^"]+" Target="([^"]+)"' % rid, rels).group(1)
    sheet_file[name] = "xl/" + tgt
sheets = {}
def sx(name):
    if name not in sheets: sheets[name] = txt(sheet_file[name])
    return sheets[name]
def col_idx(c):
    n = 0
    for ch in c: n = n * 26 + ord(ch) - 64
    return n
def split_ref(ref):
    m = re.match(r"([A-Z]+)(\d+)$", ref); return m.group(1), int(m.group(2))
def col_widths(x):
    w = {}
    for a, b, wd in re.findall(r'<col [^>]*?min="(\d+)" max="(\d+)" width="([\d.]+)"', x):
        for i in range(int(a), int(b) + 1): w[i] = float(wd)
    return w

manifest = []   # {sheet, cell, change, old, new}
touched_rows = {}  # sheet -> {row: [ (col, text) ]}

def read_cell(x, ref):
    m = re.search(r'<c r="%s"(?: [^>/]*)?(?:/>|>(.*?)</c>)' % ref, x, flags=re.S)
    if not m: return None, None
    tag = m.group(0)
    s = re.search(r' s="(\d+)"', tag); s = s.group(1) if s else "0"
    v = re.search(r"<v>(.*?)</v>", tag)
    if ' t="s"' in tag and v: return s, si_text(int(v.group(1)))
    f = re.search(r"<f>(.*?)</f>", tag)
    if f: return s, "=" + f.group(1)
    return s, (v.group(1) if v else None)

def set_cell(sheet, ref, text, change, style=None):
    x = sx(sheet)
    col, row = split_ref(ref)
    old_s, old_v = read_cell(x, ref)
    s = style if style is not None else (old_s if old_s is not None else "0")
    if text == "":
        newc = '<c r="%s" s="%d"/>' % (ref, hl_style(s))
    else:
        newc = '<c r="%s" s="%d" t="s"><v>%d</v></c>' % (ref, hl_style(s), add_string(text))
    rm = re.search(r'<row r="%d"(?: [^>/]*)?(?:/>|>.*?</row>)' % row, x, flags=re.S)
    if rm is None:
        # insert new row in order
        nxt = None
        for m in re.finditer(r'<row r="(\d+)"', x):
            if int(m.group(1)) > row: nxt = m; break
        newrow = '<row r="%d">%s</row>' % (row, newc)
        x = x[:nxt.start()] + newrow + x[nxt.start():] if nxt else x.replace("</sheetData>", newrow + "</sheetData>")
    else:
        rowxml = rm.group(0)
        if rowxml.endswith("/>"):
            rowxml2 = rowxml[:-2] + ">" + newc + "</row>"
        else:
            cm = re.search(r'<c r="%s"(?: [^>/]*)?(?:/>|>.*?</c>)' % ref, rowxml, flags=re.S)
            if cm:
                rowxml2 = rowxml[:cm.start()] + newc + rowxml[cm.end():]
            else:
                pos = None
                for c in re.finditer(r'<c r="([A-Z]+)\d+"', rowxml):
                    if col_idx(c.group(1)) > col_idx(col): pos = c.start(); break
                if pos is None: pos = rowxml.rindex("</row>")
                rowxml2 = rowxml[:pos] + newc + rowxml[pos:]
        x = x[:rm.start()] + rowxml2 + x[rm.end():]
    sheets[sheet] = x
    manifest.append({"sheet": sheet, "cell": ref, "change": change, "old": old_v, "new": text})
    touched_rows.setdefault(sheet, {}).setdefault(row, []).append((col_idx(col), text))

def append_text(sheet, ref, extra, change):
    _, old = read_cell(sx(sheet), ref)
    set_cell(sheet, ref, old + extra, change)

def fit_rows():
    """Ajusta so a altura das linhas que receberam texto alterado (texto nao fica cortado)."""
    for sheet, rows in touched_rows.items():
        x = sx(sheet); w = col_widths(x)
        for row, cells in rows.items():
            lines = 1
            for ci, t in cells:
                cpl = max(8, int(w.get(ci, 14.43) * 1.15))
                lines = max(lines, sum(max(1, math.ceil(len(p) / cpl)) for p in t.split("\n")))
            need = round(lines * 15.0 + 6, 2)
            rm = re.search(r'<row r="%d"((?: [^>]*?)?)(/?)>' % row, x)
            attrs = rm.group(1)
            cur = re.search(r' ht="([\d.]+)"', attrs)
            if cur and float(cur.group(1)) >= need: continue
            attrs2 = re.sub(r' ht="[\d.]+"', "", attrs); attrs2 = re.sub(r' customHeight="\d"', "", attrs2)
            attrs2 += ' ht="%s" customHeight="1"' % need
            x = x[:rm.start()] + '<row r="%d"%s%s>' % (row, attrs2, rm.group(2)) + x[rm.end():]
        sheets[sheet] = x

# ================================================================= MUDANCAS
VC, RM, ER, DS, FS, PR, VR, EA = ("Version Control", "Report Matrix", "Evidence Register", "DAS Spec",
                                  "File Structure", "Population Rules", "Validation Rules", "Example Analysis")
EST = "NEW DD FIELD (proposed): Employee Establishment (CNAS employer-number assignment)"

# --- C1 regra por estabelecimento
set_cell(RM, "B21", "ONE file pair per CNAS employer number (cotisant). An employer holding several employer numbers (e.g. one per establishment / work location) files a separate pair for each; files are never merged across employer numbers. Generation key: employee -> establishment -> CNAS employer number (10), centre payeur (5), Dénomination, Nom ou Raison Sociale and Adresse of that establishment - see Population Rules 'Per-establishment generation'.", "C1")
set_cell(DS, "L4", "DD: Employer.CNASNumber of the employee's establishment, resolved via " + EST, "C1")
set_cell(DS, "L19", "DD: Employer.CNASNumber of the employee's establishment, resolved via " + EST, "C1")
append_text(DS, "M21", " Numbering restarts at 1 in each détail file (i.e. per CNAS employer number).", "C1")
append_text(DS, "M39", " Transfer between establishments within the year: Date Entrée of the attachment to THIS employer number - see Population Rules 'Transfer between establishments' (⚠️ proposal, no primary source).", "C1")
append_text(DS, "M40", " Transfer between establishments within the year: Date Sortie of the attachment to THIS employer number - see Population Rules 'Transfer between establishments' (⚠️ proposal, no primary source).", "C1")
append_text(FS, "C7", " Grouping key: employee -> establishment -> CNAS employer number; one pair per distinct number in the reference-year population.", "C1")
set_cell(FS, "C27", "Sequential from 1, restarting at 1 in each détail file (per CNAS employer number).", "C1")
append_text(VR, "E10", " Grouping key: employee -> establishment -> CNAS employer number (see Population Rules 'Per-establishment generation').", "C1")
# novas linhas em Population Rules (acrescentadas ao fim; nada deslocado)
set_cell(PR, "A26", "═══ PER-ESTABLISHMENT GENERATION (v2.2) ═══", "C1", style="11")
set_cell(PR, "B26", "", "C1", style="12"); set_cell(PR, "C26", "", "C1", style="12"); set_cell(PR, "D26", "", "C1", style="13")
set_cell(PR, "A27", "Per-establishment generation", "C1", style="15")
set_cell(PR, "B27", "Both files; employer fields 1, 4-7", "C1", style="15")
set_cell(PR, "C27", "Generate one entête + détail pair per DISTINCT CNAS employer number found in the reference-year population. Key: employee -> establishment (" + EST + ") -> CNAS employer number (10), centre payeur (5), Dénomination, Nom ou Raison Sociale and Adresse of that establishment. Each pair carries only the employees attached to that number; entête totals and headcount aggregate only its own détail file. Basis: one employer number per file name and per record (guide p.35-36) and rejection 'Numéro cotisant (employeur) erroné' (p.41). The guide does not literally say 'one DAS per establishment'.", "C1", style="15")
set_cell(PR, "D27", "A", "C1", style="15")
set_cell(PR, "A28", "Line numbering per file", "C1", style="15")
set_cell(PR, "B28", "N° Ligne", "C1", style="15")
set_cell(PR, "C28", "N° Ligne restarts at 1 in each détail file and runs without gaps or duplicates within that file.", "C1", style="15")
set_cell(PR, "D28", "A", "C1", style="15")
set_cell(PR, "A29", "Transfer between establishments", "C1", style="14")
set_cell(PR, "B29", "Durée / Salaire Tn, Date Entrée, Date Sortie", "C1", style="14")
set_cell(PR, "C29", "⚠️ PROPOSAL - NO PRIMARY SOURCE. The guide only states (p.14, EMS) that any change of the employer number to which an employee is attached is a movement. Proposed treatment: the employee appears in the pair of each employer number held during the year; each record carries only the quarters and salaries earned under that number (other quarters 0/0), with Date Entrée / Date Sortie of the attachment to that number. Confirm with CNAS / the client before go-live.", "C1", style="14")
set_cell(PR, "D29", "Proposal", "C1", style="14")

# --- C2 nome do arquivo por nº CNAS do estabelecimento
for ref in ("M3", "M18"):
    append_text(DS, ref, " The cotisant is the 10-digit CNAS employer number of the establishment being filed; the same number appears in field 1 of the entête and of every détail record.", "C2")
append_text(FS, "C5", " Cotisant = CNAS number of the establishment being filed; same number on every record.", "C2")
append_text(FS, "C6", " Cotisant = CNAS number of the establishment being filed; same number on every record.", "C2")

# --- C3 mapeamentos -> nomes reais do DZ-DD-001-v1.1 ou NEW DD FIELD
set_cell(DS, "L7", "DD: Employer.CNASCentre (of the establishment's CNAS employer number)", "C3")
set_cell(DS, "L8", "NEW DD FIELD (proposed): Establishment Denomination (Dénomination, A30)", "C3")
set_cell(DS, "L10", "NEW DD FIELD (proposed): Establishment Address (Adresse de l'établissement, AN50). DD: Employer.Address holds the head-office address only.", "C3")
set_cell(DS, "L22", "DD: Employee.SSNumber", "C3")
for q, r in ((1, 27), (2, 30), (3, 33), (4, 36)):
    set_cell(DS, "L%d" % r, "Client parameter: NEW DD FIELD (proposed): DAS Duration Unit (M/J/H), per client / establishment; default derived from NEW DD FIELD (proposed): Pay Frequency (Monthly=M, Daily=J, Hourly=H)", "C3+C6")
for q, r in ((1, 28), (2, 31), (3, 34), (4, 37)):
    set_cell(DS, "L%d" % r, "Payroll result: CNAS contributory base for Q%d (sum of the 3 months), in centimes - product WT 64551 (to be confirmed by Development; not validatable in DZ-WTC-001-v1.0, which carries no Mercans WT codes)" % q, "C3+C4")

# --- C4 duracao em dias / sem separador / sem "Working Hours"
for q, r in ((1, 26), (2, 29), (3, 32), (4, 35)):
    set_cell(DS, "L%d" % r, "Derived: duration worked in Q%d, in the unit of the Q%d unit field. Unit J = DAYS, 0-92 (client convention, e.g. Henkel: 90 per full quarter minus unpaid-absence days; absence WTs 63121 / 63122 / 63129 / 63801 - to be confirmed by Development, not validatable in DZ-WTC-001-v1.0). Never hours; never 'Working Hours'." % (q, q), "C4")
append_text(DS, "M26", " NO SEPARATOR: the birth date (pos 83-90) is immediately followed by the Q1 duration (pos 91-93), e.g. '15011985' + '90 ' + 'J' - this is correct per the guide (p.36), not a defect. With unit J the value is DAYS 0-92; a value such as 143 with unit J is invalid ('Nombre de jours incorrect', p.42).", "C4")
for r in ("M29", "M32", "M35"):
    append_text(DS, r, " With unit J the value is DAYS 0-92 - never hours. No separator before or after this field (guide p.36).", "C4")
set_cell(PR, "C9", "The unit code determines the measure of the duration. The unit is a CLIENT-LEVEL PARAMETER (guide p.36: M for monthly-paid, J for day-paid, H for hourly-paid workers; the client decides and records it). M = months worked (full quarter 3); J = DAYS worked, 0-92 per quarter (client convention, e.g. 90 per full quarter minus unpaid-absence days); H = hours worked (full quarter ≈ 520). Partial quarters are prorated on the same basis as the unit emitted. Never emit hours with unit J. The layout has no separator, so the birth date is immediately followed by the Q1 duration - this is correct. The duration feeds the insured-period record used for pension validation, so an incorrect unit may pass the file check yet still misstate entitlement.", "C4+C6")

# --- C5 Observation em branco por default
set_cell(DS, "K41", "(20 spaces)", "C5")
set_cell(DS, "L41", "Blank (20 spaces) by default. DD: Employee.JobTitle only where the client opts in.", "C5")
set_cell(DS, "M41", "Optional free text (guide p.36: 'dans la mesure du possible'). DEFAULT = blank (20 spaces). Populate with the employee function only on explicit client request.", "C5")
set_cell(FS, "C39", "Optional; blank (20 spaces) by default; employee function only on client request.", "C5")

# --- C6 unidade = parametro por cliente
for r in ("M27", "M30", "M33", "M36"):
    set_cell(DS, r, "M = mensuel, J = journalier, H = horaire. Guide p.36 prescribes M for monthly-paid workers. The unit is a CLIENT-LEVEL PARAMETER: the client decides and records it (e.g. Henkel's accepted 2024 filing used J for all records - see the Henkel Configuration tab); it is not a compliance decision. The duration feeds the insured-period record used for pension validation.", "C6")
set_cell(ER, "D16", "Documented as tolerated. The unit is a client-level parameter (v2.2): the guide prescribes M for monthly-paid workers; a client may keep J on its own decision, recorded in its configuration annex.", "C6")
set_cell(VR, "E49", "The unit equals the client-configured DAS unit parameter; where it differs from the guide (M for monthly-paid), the client decision is recorded in its configuration annex.", "C6")

# --- C7 pareamento duracao<->salario rebaixado a WARN
for r in ("G26", "G29", "G32", "G35"):
    append_text(DS, r, " Severity WARN only (SEM-02): the guide does not state this rule.", "C7")
append_text(PR, "C10", " SEVERITY WARN (v2.2): this pairing is NOT stated in the guide, and an accepted submission contained 9 quarters breaching it (7 with duration > 0 and salary 0; 2 with duration 0 and salary > 0). Investigate; do not block.", "C7")
set_cell(PR, "D10", "B", "C7", style="14")
set_cell(VR, "C48", "B", "C7")
set_cell(VR, "D48", "WARN", "C7")
append_text(VR, "E48", " WARN only (v2.2): the guide does not state this rule and an accepted submission contained 9 breaching quarters.", "C7")

# --- C8 prazo e penalidade
set_cell(RM, "B13", "Within thirty (30) days following the end of each calendar year: Loi n° 83-14 du 2 juillet 1983, art. 14 - \"dans les trente (30) jours qui suivent la fin de chaque année civile\". A literal count gives 30 January. ⚠️ 31 January appears in secondary sources, but no regulatory text fixing that date has been located; treat 30 January as the safe date unless a CNAS communiqué for the filing year says otherwise.", "C8")
set_cell(RM, "B14", "Loi n° 83-14 du 2 juillet 1983 (art. 8, art. 14; art. 16 as reworded and art. 16 bis as inserted by Loi n° 04-17 du 10 novembre 2004, JORADP n° 72 of 13/11/2004, arts. 11-12). Recovery/penalties: Loi n° 08-08 du 23 février 2008. Contribution rates: Décret exécutif n° 94-187 as amended by n° 15-236 (DAC-relevant, not DAS layout).", "C8")
set_cell(RM, "B15", "Failure to file the salary declaration in the conditions and deadline of art. 14: penalty of 15% of the contributions due, increased by 5% per month of delay (Loi 83-14 art. 16, as worded by Loi 04-17 art. 11; the original 1983 wording was 10% + 2% per month). Omitting an employee from the declaration, or deliberate inaccuracy in the declared salaries: 1,000 DA per worker and/or inaccuracy (art. 16 bis, inserted by Loi 04-17 art. 12). ⚠️ Later amendments to arts. 14/16 (finance laws, Loi 08-08) not verified - confirm with the local agency.", "C8")
set_cell(VR, "E57", "The DAS is filed within the thirty (30) days following the end of the reference year (Loi 83-14 art. 14) - i.e. by 30 January on a literal count. ⚠️ 31 January is not confirmed by a regulatory text.", "C8")
set_cell(VR, "F57", "Late-filing penalty 15% of contributions due + 5% per month of delay (art. 16, Loi 04-17); 1,000 DA per omitted worker / inaccuracy (art. 16 bis)", "C8")

# --- C9 celulas que viravam formula
set_cell(EA, "D10", "Equals 4 x 2,700,000,000 exactly (ARI-01).", "C9")
set_cell(EA, "D17", "Equals 0 + 1,800,000,000 + 2,700,000,000 + 2,700,000,000.", "C9")

# --- C10 version control
set_cell(VC, "A15", "", "C10", style="10")
set_cell(VC, "B15", "2.2", "C10", style="10")
set_cell(VC, "C15", "2026-10-27", "C10", style="10")
set_cell(VC, "D15", "Draft for HRBS-3466: per-establishment generation (one E/S pair per CNAS employer number, grouping key, line numbering per file, transfer rule as an unsourced proposal); file name per establishment number; System Mapping aligned to DZ-DD-001-v1.1 field names or marked NEW DD FIELD (proposed); duration in DAYS 0-92 for unit J and no-separator note; Observation blank by default; unit as a client parameter; SEM-02 downgraded to WARN; deadline and penalties per Loi 83-14 art. 14 and arts. 16 / 16 bis (Loi 04-17); formula-error cells fixed; Henkel Configuration annex added.", "C10", style="10")
set_cell(VC, "E15", "Draft", "C10", style="10")
set_cell(VC, "F15", "Wallisson Gomes", "C10", style="10")
set_cell(RM, "B22", "2.2 - country standard (Draft, 2026-10-27); 2.1 remains the current released version", "C10")

# --- C11 aba Henkel Configuration (+ aviso na capa)
append_text(VC, "B5", " The 'Henkel Configuration' tab (added in v2.2) is a CLIENT ANNEX for HRBS-3466 and is not part of the national standard.", "C11")

fit_rows()

TBC = "TO BE CONFIRMED BY CLIENT"
henkel_rows = [
    ["HENKEL - CLIENT CONFIGURATION ANNEX (ticket HRBS-3466) - not part of the DZ country standard"],
    ["Only values proven by a source are filled; everything else is TO BE CONFIRMED BY CLIENT. No employee personal data (names, social-security numbers, salaries) is held in this tab."],
    [],
    ["Location", "CNAS employer number (10)", "Centre payeur (5)", "Dénomination (A30)", "Nom ou Raison Sociale (A30)", "Adresse (AN50)", "Population (employees attached)", "DAS duration unit", "Observation", "Source / status"],
    ["Dely Ibrahim", "1638091858", TBC, TBC, TBC, TBC, TBC, TBC + " (J used for 100% of records in the accepted DAS 2024 file; guide p.36 prescribes M for monthly-paid)", "Blank (20 spaces)", "CNAS number: file name and field 1 of the accepted DAS 2024 files D24E1638091858 / D24S1638091858 (HRBS-3466 attachments); the address field of that entête is in Dely Ibrahim. Observation blank: client request V3 (HRBS-3466, 31/12/2025). ⚠️ Not proven whether this number also covered the other locations in 2024."],
    ["Reghaia", TBC, TBC, TBC, TBC, TBC, TBC, TBC + " (J or M)", "Blank (20 spaces)", "Location named in the client request (HRBS-3466, 25/12/2025). ⚠️ Not proven that it holds its own CNAS employer number."],
    ["Chelghoum Laid", TBC, TBC, TBC, TBC, TBC, TBC, TBC + " (J or M)", "Blank (20 spaces)", "Location named in the client request (HRBS-3466, 25/12/2025). ⚠️ Not proven that it holds its own CNAS employer number."],
    [],
    ["Client rules applied to all locations"],
    ["Files", "One E + S pair per CNAS employer number above; names D + YY + E/S + CNAS number (10) + .TXT."],
    ["Duration", "Unit J (if confirmed): DAYS 0-92 per quarter, convention 90 per full quarter minus unpaid-absence days (absence WTs 63121 / 63122 / 63129 / 63801 - to be confirmed by Development). Never hours."],
    ["Quarterly salary", "CNAS contributory base per quarter, product WT 64551 - to be confirmed by Development."],
    ["Observation", "Blank (20 spaces) for every record (client request V3)."],
]
# ------------------------------------------------------------- monta sheet13
def cref(ci, r):
    s = ""
    while ci: ci, rem = divmod(ci - 1, 26); s = chr(65 + rem) + s
    return "%s%d" % (s, r)
st_title, st_note, st_head, st_body = hl_style(2), hl_style(5), hl_style(17), hl_style(10)
widths = [20, 16, 14, 22, 22, 26, 20, 34, 18, 60]
rows_xml = []
for i, row in enumerate(henkel_rows, start=1):
    if not row: continue
    cells = []
    for j, v in enumerate(row, start=1):
        st = st_title if i == 1 else st_note if i == 2 else st_head if i in (4, 9) else (st_head if j == 1 else st_body)
        cells.append('<c r="%s" s="%d" t="s"><v>%d</v></c>' % (cref(j, i), st, add_string(v)))
        manifest.append({"sheet": "Henkel Configuration", "cell": cref(j, i), "change": "C11", "old": None, "new": v})
    if 5 <= i <= 7: ht = ' ht="96.0" customHeight="1"'
    elif i in (2, 11): ht = ' ht="33.0" customHeight="1"'
    else: ht = ""
    rows_xml.append('<row r="%d"%s>%s</row>' % (i, ht, "".join(cells)))
merges = ['<mergeCell ref="A1:J1"/>', '<mergeCell ref="A2:J2"/>'] + ['<mergeCell ref="B%d:J%d"/>' % (r, r) for r in (10, 11, 12, 13)]
sheet13 = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n'
           '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
           '<sheetViews><sheetView workbookViewId="0"/></sheetViews><sheetFormatPr defaultColWidth="14.43" defaultRowHeight="15.0"/>'
           '<cols>' + "".join('<col customWidth="1" min="%d" max="%d" width="%s"/>' % (k, k, w) for k, w in enumerate(widths, 1)) + '</cols>'
           '<sheetData>' + "".join(rows_xml) + '</sheetData>'
           '<mergeCells count="%d">%s</mergeCells>' % (len(merges), "".join(merges)) +
           '<pageMargins bottom="1.0" footer="0.0" header="0.0" left="0.75" right="0.75" top="1.0"/></worksheet>')

# ------------------------------------------------------------- grava partes
out_parts = dict(parts)
for name, x in sheets.items():
    out_parts[sheet_file[name]] = x.encode("utf-8")
sst = re.sub(r'count="\d+" uniqueCount="\d+"', 'count="%d" uniqueCount="%d"' % (sst_count, sst_unique), sst, count=1)
out_parts["xl/sharedStrings.xml"] = sst.replace("</sst>", "".join(new_si) + "</sst>").encode("utf-8")
cx = xfs_block.group(2) + "".join(new_xfs)
sty = sty[:xfs_block.start()] + '<cellXfs count="%d">%s</cellXfs>' % (len(xf_list) + len(new_xfs), cx) + sty[xfs_block.end():]
out_parts["xl/styles.xml"] = sty.encode("utf-8")
wb = wb.replace("</sheets>", '<sheet state="visible" name="Henkel Configuration" sheetId="13" r:id="rId17"/></sheets>')
out_parts["xl/workbook.xml"] = wb.encode("utf-8")
rels = rels.replace("</Relationships>", '<Relationship Id="rId17" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet13.xml"/></Relationships>')
out_parts["xl/_rels/workbook.xml.rels"] = rels.encode("utf-8")
ct = txt("[Content_Types].xml").replace("</Types>", '<Override ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml" PartName="/xl/worksheets/sheet13.xml"/></Types>')
out_parts["[Content_Types].xml"] = ct.encode("utf-8")
out_parts["xl/worksheets/sheet13.xml"] = sheet13.encode("utf-8")

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
    for info in zin.infolist():
        zo.writestr(info.filename, out_parts[info.filename], compress_type=zipfile.ZIP_DEFLATED)
    zo.writestr("xl/worksheets/sheet13.xml", out_parts["xl/worksheets/sheet13.xml"], compress_type=zipfile.ZIP_DEFLATED)

changed = sorted(n for n in parts if out_parts[n] != parts[n]) + ["xl/worksheets/sheet13.xml (new)"]
json.dump({"changes": manifest, "changed_parts": changed}, open(HERE / "changes_manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("cells:", len(manifest), "parts changed:", changed)

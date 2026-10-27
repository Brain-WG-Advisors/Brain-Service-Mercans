# -*- coding: utf-8 -*-
"""SR-109 Taiwan Payslip spec v1.1(export) -> v1.2 por cirurgia XML + zip.
Partes nao alteradas sao copiadas byte a byte. Uso:
  python -I build_v12.py <base.xlsx> <saida.xlsx>
"""
import sys, re, zipfile
from xml.sax.saxutils import escape

BASE, OUT = sys.argv[1], sys.argv[2]
HL = "FFDDEBF7"
TBC = "TO BE CONFIRMED BY MOHIT/BA"

zin = zipfile.ZipFile(BASE)
parts = {i.filename: zin.read(i.filename) for i in zin.infolist()}
infos = zin.infolist()

# ---------- styles: nova fill + clones de xf ----------
st = parts["xl/styles.xml"].decode("utf-8")
m = re.search(r'<fills count="(\d+)">(.*?)</fills>', st, re.S)
nfill = int(m.group(1))
newfill = f'<fill><patternFill patternType="solid"><fgColor rgb="{HL}"/><bgColor rgb="{HL}"/></patternFill></fill>'
st = st.replace(m.group(0), f'<fills count="{nfill+1}">{m.group(2)}{newfill}</fills>')
FILL_ID = nfill
mx = re.search(r'<cellXfs count="(\d+)">(.*?)</cellXfs>', st, re.S)
xfs = re.findall(r'<xf [^>]*?/>|<xf [^>]*?>.*?</xf>', mx.group(2), re.S)
assert len(xfs) == int(mx.group(1))
added, cache = [], {}

def hl(base):
    base = int(base)
    if base in cache:
        return cache[base]
    x = xfs[base]
    x = re.sub(r'fillId="\d+"', f'fillId="{FILL_ID}"', x, count=1)
    if 'applyFill=' not in x:
        x = x.replace('<xf ', '<xf applyFill="1" ', 1)
    idx = len(xfs) + len(added)
    added.append(x)
    cache[base] = idx
    return idx

def wrapclone(base):
    """clone com fill azul e wrapText (para textos longos novos)."""
    base = int(base)
    key = ("w", base)
    if key in cache:
        return cache[key]
    x = xfs[base]
    x = re.sub(r'fillId="\d+"', f'fillId="{FILL_ID}"', x, count=1)
    if 'applyFill=' not in x:
        x = x.replace('<xf ', '<xf applyFill="1" ', 1)
    if '<alignment' in x:
        if 'wrapText' not in x:
            x = x.replace('<alignment ', '<alignment wrapText="1" ', 1)
        x = x.replace('<alignment ', '<alignment vertical="top" ', 1) if 'vertical=' not in x else x
    else:
        x = x.replace('/>', ' applyAlignment="1"><alignment vertical="top" wrapText="1"/></xf>', 1) if x.endswith('/>') else x
    idx = len(xfs) + len(added)
    added.append(x)
    cache[key] = idx
    return idx

# ---------- helpers de celula ----------
def col2n(c):
    n = 0
    for ch in c:
        n = n * 26 + ord(ch) - 64
    return n

def cellxml(ref, s, text):
    if text is None or text == "":
        return f'<c r="{ref}" s="{s}"/>'
    return f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{escape(text)}</t></is></c>'

CHANGES = []  # (sheet, ref, text)

def set_cell(xml, sheetname, ref, text, style_fn=hl, default_base=8):
    col = re.match(r'[A-Z]+', ref).group(0)
    r = int(ref[len(col):])
    rm = re.search(r'<row r="%d"[^>]*?(?:/>|>.*?</row>)' % r, xml, re.S)
    assert rm, f"row {r} nao existe"
    row = rm.group(0)
    cm = re.search(r'<c r="%s"[^>]*?(?:/>|>.*?</c>)' % ref, row, re.S)
    if cm:
        sm = re.search(r' s="(\d+)"', cm.group(0))
        base = sm.group(1) if sm else default_base
        new = cellxml(ref, style_fn(base), text)
        row2 = row.replace(cm.group(0), new, 1)
    else:
        new = cellxml(ref, style_fn(default_base), text)
        if row.endswith('/>'):
            row2 = row[:-2] + '>' + new + '</row>'
        else:
            cells = list(re.finditer(r'<c r="([A-Z]+)\d+"', row))
            pos = None
            for c in cells:
                if col2n(c.group(1)) > col2n(col):
                    pos = c.start(); break
            if pos is None:
                pos = row.rindex('</row>')
            row2 = row[:pos] + new + row[pos:]
    CHANGES.append((sheetname, ref, text))
    return xml.replace(row, row2, 1)

# ---------- Spec (sheet2.xml) ----------
sp = parts["xl/worksheets/sheet2.xml"].decode("utf-8")
S = "Spec"
spec_edits = [
    # header das colunas novas (T/U)
    ("T4", "Field description - RA (v1.2)", 19),
    ("U4", "Label zh-TW (proposed)", 19),
    # Company
    ("T5", "Legal name of the employing entity.", None),
    ("Q6", f"{TBC} - legal entity address variable (TW DD V3.3 has only $legal_entity_hr.post_code)", None),
    ("T6", "Registered address of the employing entity. Not a mandatory item of LSA Enforcement Rules art. 14-1; kept because the example payslip shows it.", None),
    ("T7", "Country of the legal entity (Taiwan).", None),
    ("T8", "Pay period begin and end dates of the payroll run.", None),
    ("U8", "薪資月份", None),
    # Employee
    ("T9", "Employee full name.", None),
    ("U9", "姓名", None),
    ("T10", "Employee reference code in the system.", None),
    ("T11", "Employee position / job title.", None),
    ("U11", "職稱", None),
    ("Q12", "$hr.id_card_number", None),
    ("T12", "Optional. Taiwan ID card number (TW DD V3.3, ID Information, ordinal 8; same field as the Tax Report and SNHI specs). Not a mandatory item of LSA Enforcement Rules art. 14-1. Fallback for employees without ID card (the SI Termination spec uses $hr.passport_number): " + TBC + ".", None),
    ("U12", "證件號碼", None),
    ("T13", "Employee primary email.", None),
    ("T14", "Employee hire date.", None),
    ("U14", "到職日期", None),
    ("Q15", f"{TBC} - payment date of the payroll run (no variable found in TW DD V3.3)", None),
    ("T15", "Date the net pay is paid / credited to the employee. Shown in the MOL reference payslips (發薪日期 / 入帳日期); not a mandatory item of LSA Enforcement Rules art. 14-1.", None),
    ("U15", "發薪日期", None),
    ("T16", "Payment method (e.g. bank transfer).", None),
    # Earnings
    ("T17", "Each earning pay element on its own line (code + name), only when the value is not 0 (ticket, 03/12/2025). Covers LSA Enforcement Rules art. 14-1 item 2 (amount of each wage item).", None),
    ("U17", "應發項目", None),
    ("T18", "Amount per earning pay element. Overtime by day type comes from WTC V2.3+ PEs 62110/62111 (work day), 62120-62122 (rest day) and 62130-62132 (public holiday), all inside 62106:62999.", None),
    ("U18", "金額", None),
    ("M20", "Earnings", None),
    ("N20", "Overtime rate (overtime lines only)", None),
    ("Q20", "Static rate from the WTC V2.8 PE name: 62110=1.33, 62111=1.67, 62120=1.33, 62121=1.67, 62122=2.67, 62130=1, 62131=1.33, 62132=1.67. Display on payslip: " + TBC, None),
    ("T20", "Recommended, not mandatory (MOL reference payslip model 3 shows rate and hours; note 7: items may be added or removed). Rates checked against LSA art. 24 (work day: +1/3 first 2 h, +2/3 next 2 h; rest day: 1 1/3 first 2 h, 1 2/3 after) and MOL notes 3-4 (rest day over 8 h: 2 2/3; holiday: 1 extra day within 8 h, +1/3 and +2/3 over 8 h; LSA art. 39).", None),
    ("U20", "倍率", None),
    ("M21", "Earnings", None),
    ("N21", "Overtime hours (overtime lines only)", None),
    ("Q21", TBC + " - WTC V2.8 overtime PEs are Lump Sum without formula; no hours input found in WTC/DD. If not available, show the amount only.", None),
    ("T21", "Optional (MOL reference payslip model 3). Shown only if the engine stores hours per overtime PE.", None),
    ("U21", "時數", None),
    ("M22", "Earnings", None),
    ("N22", "Total Gross", None),
    ("Q22", "SUM of Accounts: 62100:62103+62106:62999+65500:65859+79401:79450", None),
    ("T22", "Sum of all earning lines shown (same accounts as Earnings). MOL reference payslips show this subtotal.", None),
    ("U22", "應發金額", None),
    ("M23", "Agreed wage", None),
    ("N23", "Agreed Total Wage", None),
    ("Q23", TBC + " - NEW DD FIELD (proposed) or contractual salary amount; no such field in TW DD V3.3", None),
    ("T23", "Mandatory: LSA Enforcement Rules art. 14-1 item 1 (total wage agreed by employer and employee). Proposed: monthly contractual wage (basic + fixed allowances, before proration/absence), as in MOL reference payslip model 2 (約定薪資結構). Exact definition: " + TBC + ".", None),
    ("U23", "勞雇雙方議定之工資總額", None),
    # Deductions
    ("T27", "Each deduction pay element on its own line, only when the value is not 0. Covers LSA Enforcement Rules art. 14-1 item 3 (amounts deducted under law or agreement).", None),
    ("U27", "應扣項目", None),
    ("T28", "Amount per deduction (LI, EI, NHI, SNHI, voluntary pension, EWF, income tax per WTC V2.8).", None),
    ("U28", "金額", None),
    ("N30", "Total Deductions", None),
    ("Q30", "SUM of Accounts: 21100:21999+25500:25899+2551+2555+2554+2558+2517+2557+2552+2572+2582+2592+2593+2594", None),
    ("T30", "Sum of all deduction lines shown (same accounts as Deductions).", None),
    ("U30", "應扣金額", None),
    # Net
    ("T37", "Amount actually paid. Covers LSA Enforcement Rules art. 14-1 item 4. Expected to equal Total Gross - Total Deductions; BA to confirm for the system accounts used.", None),
    ("U37", "實發金額", None),
    # ER
    ("T38", "Employer contributions, one line per pay element when the value is not 0. Information only; not an item of LSA Enforcement Rules art. 14-1.", None),
    ("T39", "Amount per employer contribution (LI, EI, OAI, wage arrears fund, NHI, SNHI, labor pension new/old per WTC V2.8).", None),
    ("N41", "Total Employer Contributions", None),
    ("Q41", "SUM of Accounts: 2550+2565+2560+2566+2564+2568+2537+2538+23550:23900", None),
    ("T41", "Sum of the employer contribution lines shown. Information only.", None),
    # Bank
    ("T47", "Employee bank name.", None),
    ("U47", "銀行", None),
    ("T48", "SWIFT/BIC of the employee bank.", None),
    ("T49", "Account holder name.", None),
    ("U49", "帳戶名稱", None),
    ("T50", "Employee account number.", None),
    ("U50", "轉帳帳號", None),
    ("M51", "Banking details", 34),
    ("N51", "Account currency", 92),
    ("Q51", TBC + " (shown in the example, cell I63; no mapping)", 39),
    ("T51", "Currency of the employee account.", None),
    ("M52", "Banking details", 125),
    ("N52", "Account type", 151),
    ("Q52", TBC + " (shown in the example, cell K63; no mapping)", 154),
    ("T52", "Primary / secondary account.", None),
    # Exemplo (bloco B-K)
    ("F16", "Agreed Total Wage", 102),
    ("H16", TBC, 84),
]
for ref, text, base in spec_edits:
    col = re.match(r'[A-Z]+', ref).group(0)
    if col in ("T", "U") and ref not in ("T4", "U4"):
        fn = lambda b: wrapclone(38)  # borda fina, fonte da tabela, wrap
        sp = set_cell(sp, S, ref, text, style_fn=fn)
    elif base is not None:
        fn = (lambda bb: (lambda b: hl(bb)))(base)
        sp = set_cell(sp, S, ref, text, style_fn=fn)
    else:
        sp = set_cell(sp, S, ref, text)
# merges do exemplo (linha 16, mesmo padrao da linha 13/14)
sp = re.sub(r'<mergeCells count="(\d+)">',
            lambda m: f'<mergeCells count="{int(m.group(1))+2}"><mergeCell ref="F16:G16"/><mergeCell ref="H16:K16"/>', sp, 1)
# largura das colunas T/U (eram 17.0)
sp = sp.replace('<col customWidth="1" min="20" max="21" width="17.0"/>',
                '<col customWidth="1" min="20" max="20" width="60.0"/><col customWidth="1" min="21" max="21" width="22.0"/>', 1)
parts["xl/worksheets/sheet2.xml"] = sp.encode("utf-8")

# ---------- Version Control (sheet1.xml) ----------
vc = parts["xl/worksheets/sheet1.xml"].decode("utf-8")
V = "Version Control"
for ref, text in [
    ("B13", "1.2"),
    ("C13", "2026-10-27"),
    ("D13", "Spec review (LSA art. 23-24, Enforcement Rules art. 14-1): added Agreed Total Wage, Payment Date, Employer Address, total rows, overtime rate/hours, ID field, Report Matrix, RA descriptions and zh-TW labels. Items marked TO BE CONFIRMED pending BA."),
    ("E13", "Draft"),
    ("F13", "Wallisson Gomes"),
]:
    vc = set_cell(vc, V, ref, text)
parts["xl/worksheets/sheet1.xml"] = vc.encode("utf-8")

# ---------- Report Matrix (novo sheet4.xml) ----------
RM = [
    ("Report Name", "Taiwan Payslip (工資各項目計算方式明細)"),
    ("Report Code", "taiwan-payslip"),
    ("Allowed Submission Frequency", "Payroll Run"),
    ("Periodicity", "Each wage payment (LSA art. 23 para. 1: wages paid at least twice a month unless otherwise agreed or paid monthly in advance; the itemised statement is provided with the payment)."),
    ("File Format", "PDF"),
    ("Report Encoding", TBC + " (must support Traditional Chinese if bilingual labels are approved)"),
    ("Other Supported File Formats", ""),
    ("File Naming Convention", TBC),
    ("Grouping/Filter Formula (Summary, Detail, Employee Level)", "Employee level: one payslip per employee per payroll run."),
    ("Filing Method", "Not filed with an authority. Issued to the employee on paper, electronically or by other means the employee can access and print at any time (LSA Enforcement Rules art. 14-1 para. 2)."),
    ("Language for Printing", "Proposed: one bilingual layout, Traditional Chinese (zh-TW) + English labels (Spec, column U). Product decision, " + TBC + ": LSA art. 23 and Enforcement Rules art. 14-1 do not set a language; a Chinese version was requested on the ticket (08/08/2025)."),
    ("Other Supported Languages", "English"),
    ("Population Range (Nature of Employee/Employee Status)", "All employees included in the payroll run."),
    ("Inclusion Filter (Event)", "Pay elements shown only when the value is not 0 (ticket, 03/12/2025)."),
    ("Reporting Currency", "TWD (NT$) - " + TBC),
    ("Rounding (Report-wise)", TBC),
    ("Number Format", TBC),
    ("Delimiter (Used in TXT/CSV)", "N/A (PDF)"),
    ("Introduction and Purpose of Report", "LSA art. 23 para. 1 requires the employer to give each worker an itemised statement of how each wage item is calculated (工資各項目計算方式明細). LSA Enforcement Rules art. 14-1 sets the minimum content: (1) total wage agreed by employer and employee; (2) amount of each wage item; (3) amounts deducted under law or agreement; (4) amount actually paid. Breach of art. 23: fine of NT$20,000 to NT$1,000,000 (LSA art. 79)."),
    ("Legal basis", "Labor Standards Act arts. 23, 24, 39, 79; LSA Enforcement Rules art. 14-1; MOL reference payslip examples (參考例, attached to ticket SR-109). Texts read on laws.mol.gov.tw (copies dated 2026-10-23)."),
]
s_title = hl(13)
s_lab = wrapclone(118)
s_val = wrapclone(38)
rows = [f'<row r="1"><c r="A1" s="{s_title}" t="inlineStr"><is><t>Report Matrix</t></is></c></row>']
CHANGES.append(("Report Matrix", "A1", "Report Matrix"))
for i, (lab, val) in enumerate(RM):
    r = 3 + i
    rows.append(f'<row r="{r}">{cellxml("A%d" % r, s_lab, lab)}{cellxml("B%d" % r, s_val, val)}</row>')
    CHANGES.append(("Report Matrix", f"A{r}", lab))
    CHANGES.append(("Report Matrix", f"B{r}", val))
sheet4 = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
          '<worksheet xmlns="http://schemas.openxmlformats.org/spreadsheetml/2006/main" '
          'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships">'
          '<sheetViews><sheetView workbookViewId="0"/></sheetViews>'
          '<sheetFormatPr defaultRowHeight="15.0"/>'
          '<cols><col customWidth="1" min="1" max="1" width="48.0"/><col customWidth="1" min="2" max="2" width="100.0"/></cols>'
          '<sheetData>' + "".join(rows) + '</sheetData>'
          '<pageMargins bottom="0.75" footer="0.0" header="0.0" left="0.7" right="0.7" top="0.75"/></worksheet>')
parts["xl/worksheets/sheet4.xml"] = sheet4.encode("utf-8")

wb = parts["xl/workbook.xml"].decode("utf-8")
wb = wb.replace('<sheet state="visible" name="Version Control" sheetId="1" r:id="rId5"/>',
                '<sheet state="visible" name="Version Control" sheetId="1" r:id="rId5"/><sheet state="visible" name="Report Matrix" sheetId="4" r:id="rId8"/>', 1)
assert 'Report Matrix' in wb
parts["xl/workbook.xml"] = wb.encode("utf-8")
rel = parts["xl/_rels/workbook.xml.rels"].decode("utf-8")
rel = rel.replace('</Relationships>', '<Relationship Id="rId8" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/worksheet" Target="worksheets/sheet4.xml"/></Relationships>')
parts["xl/_rels/workbook.xml.rels"] = rel.encode("utf-8")
ct = parts["[Content_Types].xml"].decode("utf-8")
ct = ct.replace('PartName="/xl/worksheets/sheet3.xml"/>', 'PartName="/xl/worksheets/sheet3.xml"/><Override ContentType="application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml" PartName="/xl/worksheets/sheet4.xml"/>', 1)
parts["[Content_Types].xml"] = ct.encode("utf-8")

# ---------- fecha styles ----------
allx = xfs + added
st = st.replace(mx.group(0), f'<cellXfs count="{len(allx)}">' + "".join(allx) + '</cellXfs>')
parts["xl/styles.xml"] = st.encode("utf-8")

# ---------- repack: ordem original, entradas nao alteradas byte a byte ----------
orig = {i.filename: zin.read(i.filename) for i in infos}
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
    for i in infos:
        zi = zipfile.ZipInfo(i.filename, date_time=i.date_time)
        zi.compress_type = i.compress_type
        zi.external_attr = i.external_attr
        zo.writestr(zi, parts[i.filename])
    zi = zipfile.ZipInfo("xl/worksheets/sheet4.xml", date_time=infos[0].date_time)
    zi.compress_type = zipfile.ZIP_DEFLATED
    zo.writestr(zi, parts["xl/worksheets/sheet4.xml"])

changed = [n for n in orig if orig[n] != parts[n]]
print("partes alteradas:", changed, "+ nova: xl/worksheets/sheet4.xml")
print("estilos novos:", len(added))
import json
json.dump(CHANGES, open(sys.argv[3], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("celulas escritas:", len(CHANGES))

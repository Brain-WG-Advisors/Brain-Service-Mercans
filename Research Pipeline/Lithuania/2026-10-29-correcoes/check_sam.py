# -*- coding: utf-8 -*-
"""check_sam.py - conferencia mecanica da SAM spec LT-SODRA-003 v1.1.

Uso:
  python check_sam.py <spec_v1.1.xlsx> <SAM-V07 SAMPLE (1).ffdata oficial>

1. Extrai o XML da aba 'Sample File' (B3..) e confere a estrutura contra o FFData oficial
   da Sodra (nomes de elementos e de atributos; NUNCA imprime valores do arquivo oficial:
   ele contem o login de quem o criou e dados de empresa).
2. Confere a lista de campos de cada pagina (SAM / SAM3SD contra o FFData oficial;
   SAM3SDP contra a DSA secao 7 e contra a coluna H da aba 'SAM Spec').
3. Formatos: virgula decimal, marcas 0/1, mes 1-12 sem zero, datas, DocDate/DocNumber vazios,
   digito de controle dos codigos pessoais (mod 11 lituano).
4. Refaz as contas do Sample File, dos exemplos da 'SAM Spec' (col. K), da 'Example Analysis'
   e da tabela de taxas P3 2026 da 'Field Options'.
5. Nenhuma celula de texto comeca com '='.
Sai com codigo 1 se houver qualquer FAIL.
"""
import sys, re, math
import xml.etree.ElementTree as ET
from decimal import Decimal, ROUND_HALF_UP
import openpyxl

sys.stdout.reconfigure(encoding="utf-8")
SPEC, OFFICIAL = sys.argv[1], sys.argv[2]
fails, oks = [], []
def ok(msg): oks.append(msg); print("OK   ", msg)
def fail(msg): fails.append(msg); print("FAIL ", msg)
def chk(cond, msg): ok(msg) if cond else fail(msg)

def dec(s): return Decimal(s.replace(",", "."))
def q(x): return x.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
def lt_cd(code):
    d = [int(c) for c in code[:10]]
    r = sum(a * b for a, b in zip(d, [1, 2, 3, 4, 5, 6, 7, 8, 9, 1])) % 11
    if r == 10:
        r = sum(a * b for a, b in zip(d, [3, 4, 5, 6, 7, 8, 9, 1, 2, 3])) % 11
        r = 0 if r == 10 else r
    return r == int(code[10])

wb = openpyxl.load_workbook(SPEC)
# ---------------- 0. '=' lint
eq = [f"{ws.title}!{c.coordinate}" for ws in wb for row in ws.iter_rows() for c in row
      if isinstance(c.value, str) and c.value.startswith("=")]
chk(not eq, "nenhuma celula de texto comeca com '=' (%s)" % (eq or "0 ocorrencias"))
chk(len(wb.sheetnames) == 9, "9 abas: %s" % wb.sheetnames)

# ---------------- 1. extract sample XML
sf = wb["Sample File"]
lines = []
for r in range(3, sf.max_row + 1):
    v = sf.cell(r, 2).value
    if v is None: continue
    lines.append(v)
xml = "\n".join(lines)
raw = xml.encode("utf-8")
chk(not raw.startswith(b"\xef\xbb\xbf"), "Sample File: sem BOM; %d linhas XML" % len(lines))
chk(lines[0] == '<?xml version="1.0" encoding="UTF-8"?>', "declaracao XML UTF-8")
s_root = ET.fromstring(raw)
o_root = ET.fromstring(open(OFFICIAL, "rb").read())

# ---------------- 2. structure vs official (names only)
def shape(e, depth=0, stop=("Fields",)):
    """element/attribute-name skeleton, Group names and ListPage codes included (structural, not personal)"""
    out = [("  " * depth) + e.tag + "[" + ",".join(sorted(e.attrib)) + "]" +
           (" Name=" + e.attrib["Name"] if e.tag == "Group" else "") +
           (" =" + e.text.strip() if e.tag == "ListPage" else "")]
    if e.tag in stop: return out
    for c in e: out += shape(c, depth + 1)
    return out
chk(s_root.tag == o_root.tag == "FFData", "raiz FFData")
chk(sorted(s_root.attrib) == sorted(o_root.attrib),
    "atributos de FFData iguais ao oficial (nomes): %s" % sorted(s_root.attrib))
chk(s_root.attrib.get("Version") == o_root.attrib.get("Version") == "1", "FFData Version=\"1\"")
sf_, of_ = s_root.find("Form"), o_root.find("Form")
chk(len(s_root.findall("Form")) == 1, "um unico <Form>")
chk(sorted(sf_.attrib) == sorted(of_.attrib), "atributos de Form iguais ao oficial (nomes): %s" % sorted(sf_.attrib))
chk(sf_.attrib["FormDefId"] == of_.attrib["FormDefId"] == "{963BF380-47C3-4B69-A7F7-1B4593572CFE}", "FormDefId igual ao oficial")
chk([c.tag for c in sf_] == ["DocumentPages", "Pages"], "Form > DocumentPages + Pages (DSA 2.2)")
extra = [c.tag for c in of_ if c.tag not in ("DocumentPages", "Pages")]
chk([c.tag for c in of_ if c.tag in ("DocumentPages", "Pages")] == ["DocumentPages", "Pages"], "oficial: Form > DocumentPages + Pages")
print("INFO  FFData oficial traz tambem %s (log de validacao do eFormFiller; nao consta da DSA 2.2, nao reproduzido)" % extra)
s_dp, o_dp = shape(sf_.find("DocumentPages")), shape(of_.find("DocumentPages"))
# official sample has no SAM3SDP page: compare the common prefix (Forma + Priedas SAM3SD)
chk(s_dp[:7] == o_dp[:7] and len(o_dp) == 7, "DocumentPages: Forma/ListPages/ListPage SAM + Group 'Priedas SAM3SD' iguais ao oficial")
chk(any("Priedas SAM3SDP" in x for x in s_dp), "DocumentPages: Group 'Priedas SAM3SDP' presente (DSA 2.3/3)")
for P in (sf_.find("Pages"), of_.find("Pages")):
    pass
sp, op = sf_.find("Pages"), of_.find("Pages")
chk(sorted(sp.attrib) == sorted(op.attrib) == ["Count"], "Pages[Count]")
chk(int(sp.get("Count")) == len(sp), "Pages Count=%s = %d paginas" % (sp.get("Count"), len(sp)))
chk([int(p.get("PageNumber")) for p in sp] == list(range(1, len(sp) + 1)), "Page PageNumber sequencial a partir de 1 (DSA 2.8)")
o_attr_page = {tuple(sorted(p.attrib)) for p in op}
chk({tuple(sorted(p.attrib)) for p in sp} == o_attr_page, "atributos de Page iguais ao oficial: %s" % o_attr_page)
o_field_attrs = {tuple(sorted(f.attrib)) for p in op for f in p.find("Fields")}
s_field_attrs = {tuple(sorted(f.attrib)) for p in sp for f in p.find("Fields")}
chk(s_field_attrs == {("Name",)}, "Field usa so o atributo Name (DSA 2.10)")
print("INFO  FFData oficial (eFormFiller) usa em Field os atributos %s; 'Text' espelha o valor e nao consta da DSA 2.10" % sorted(o_field_attrs))

def fields(p): return {f.get("Name"): (f.text or "") for f in p.find("Fields")}
off = {p.get("PageDefName"): fields(p) for p in op}
smp = {}
for p in sp:
    fl = p.find("Fields")
    chk(int(fl.get("Count")) == len(fl), "%s p.%s: Fields Count=%s = %d Field" % (p.get("PageDefName"), p.get("PageNumber"), fl.get("Count"), len(fl)))
    names = [f.get("Name") for f in fl]
    chk(len(names) == len(set(names)), "%s: nomes de Field unicos na pagina (DSA 2.10)" % p.get("PageDefName"))
    smp[p.get("PageDefName")] = fields(p)
for pg in ("SAM", "SAM3SD"):
    chk(set(smp[pg]) == set(off[pg]), "%s: os %d nomes de campo = FFData oficial" % (pg, len(off[pg])))
row13 = ["RowNumber", "PersonCode", "InsuranceSeries", "InsuranceNumber", "PersonFirstName", "PersonLastName", "PeriodStartDate",
         "PeriodEndDate", "InsIncomeSum", "TaxRate", "PaymentSum", "ReasonCode", "ReasonText"]
page9 = ["InsIncomePage", "PaymentPage", "InsurerCode", "PageNumber", "PageTotal", "DocDate", "DocNumber", "FormCode", "FormVersion"]
dsa7 = {"%s_%d" % (n, i) for i in (1, 2, 3) for n in row13} | set(page9)
chk(set(smp["SAM3SDP"]) == dsa7 and len(dsa7) == 48, "SAM3SDP: 48 nomes = DSA secao 7 (13 x 3 + 9)")
# against column H of SAM Spec
spec = wb["SAM Spec"]
exp = {"SAM": set(), "SAM3SD": set(), "SAM3SDP": set()}
for r in range(2, spec.max_row + 1):
    h = spec.cell(r, 8).value
    if not h or "/" not in h: continue
    pg, nm = h.split("/")
    m = re.match(r"(\w+)_1\.\.(\d)", nm)
    if m: exp[pg] |= {"%s_%d" % (m.group(1), i) for i in range(1, int(m.group(2)) + 1)}
    else: exp[pg].add(nm)
for pg in exp:
    chk(exp[pg] == set(smp[pg]), "%s: coluna H da 'SAM Spec' (%d) = campos do Sample File" % (pg, len(exp[pg])))

# ---------------- 3. formats
DEC2 = re.compile(r"^\d+,\d{2}$")
amount_fields = re.compile(r"^(Apdx[23](InsIncomeSum|PaymentSum)|InsIncomeSum_\d|PaymentSum_\d|TaxRate_\d|InsIncomePage|PaymentPage)$")
bad = [(pg, n, v) for pg in smp for n, v in smp[pg].items() if amount_fields.match(n) and v and not DEC2.match(v)]
chk(not bad, "valores decimais com virgula e 2 casas (DSA 2.10) %s" % (bad or ""))
chk(not any("." in v for pg in smp for n, v in smp[pg].items() if amount_fields.match(n)), "nenhum ponto decimal")
marks = {n: smp["SAM"][n] for n in ("RevisedDocument", "Appendixes2", "Appendixes3")}
chk(all(v in ("0", "1") for v in marks.values()), "marcas 0/1 (DSA 2.10): %s" % marks)
chk(re.fullmatch(r"(1[0-2]|[1-9])", smp["SAM"]["CycleMonth"]) is not None, "CycleMonth=%s: numero 1-12 sem zero" % smp["SAM"]["CycleMonth"])
for pg in smp:
    chk(smp[pg]["DocDate"] == "" and smp[pg]["DocNumber"] == "", "%s: DocDate e DocNumber vazios (DSA 5-7 'nepildomas')" % pg)
    chk(smp[pg]["FormVersion"] == "07" and smp[pg]["FormCode"] == pg, "%s: FormCode/FormVersion 07 como Field" % pg)
dates = [v for pg in smp for n, v in smp[pg].items() if n.startswith("Period") and v]
chk(all(re.fullmatch(r"\d{4}-\d{2}-\d{2}", d) for d in dates), "datas AAAA-MM-DD: %s" % dates)
codes = [v for pg in smp for n, v in smp[pg].items() if n.startswith("PersonCode_") and v]
chk(all(len(c) == 11 and lt_cd(c) for c in codes), "%d codigos pessoais (ficticios) com digito de controle valido" % len(codes))
gender_ok = all(smp[pg]["PersonCode_%s" % k[-1]][0] in "35" if smp[pg][k].endswith(("as", "is")) else smp[pg]["PersonCode_%s" % k[-1]][0] in "46"
                for pg in ("SAM3SD", "SAM3SDP") for k in smp[pg] if k.startswith("PersonLastName_") and smp[pg][k])
chk(gender_ok, "1o digito do codigo coerente com o genero do sobrenome (-is/-as masc.; -ė fem.)")
chk(smp["SAM3SDP"]["ReasonCode_1"] in ["%02d" % i for i in range(1, 11)], "ReasonCode no dominio 01-10")
chk("civilinę sutartį" in smp["SAM3SDP"]["ReasonText_1"] and len(smp["SAM3SDP"]["ReasonText_1"]) <= 65, "ReasonText com diacriticos, <= 65")

# ---------------- 4. arithmetic in the sample
def annex(pg, rows):
    d = smp[pg]; inc = pay = Decimal(0); persons = 0
    for i in range(1, rows + 1):
        if not d["RowNumber_%d" % i]: continue
        a11, p3, a12 = dec(d["InsIncomeSum_%d" % i]), dec(d["TaxRate_%d" % i]), dec(d["PaymentSum_%d" % i])
        chk(q(a11 * p3 / 100) == a12, "%s linha %d: A12 %s = A11 %s x P3 %s %%" % (pg, i, a12, a11, p3))
        inc += a11; pay += a12; persons += 1
    chk(dec(d["InsIncomePage"]) == inc, "%s: P7 %s = soma A11 %s" % (pg, d["InsIncomePage"], inc))
    chk(dec(d["PaymentPage"]) == pay, "%s: P8 %s = soma A12 %s" % (pg, d["PaymentPage"], pay))
    return inc, pay, persons
t = smp["SAM"]
for pg, rows, k in (("SAM3SD", 6, "2"), ("SAM3SDP", 3, "3")):
    inc, pay, n = annex(pg, rows)
    chk(dec(t["Apdx%sInsIncomeSum" % k]) == inc, "P2%s.4 = soma do anexo %s" % ("0" if k == "2" else "1", pg))
    chk(dec(t["Apdx%sPaymentSum" % k]) == pay, "P2%s.5 = soma do anexo %s" % ("0" if k == "2" else "1", pg))
    chk(int(t["Apdx%sPersonCount" % k]) == n, "P2%s.3 = %d segurados" % ("0" if k == "2" else "1", n))
    npages = sum(1 for p in sp if p.get("PageDefName") == pg)
    chk(int(t["Apdx%sPageCount" % k]) == npages == int(smp[pg]["PageTotal"]), "%s: paginas = P2x.2 = PageTotal = %d" % (pg, npages))
    chk(t["Appendixes%s" % k] == ("1" if npages else "0"), "Appendixes%s coerente com a existencia do anexo" % k)
    chk(smp[pg]["InsurerCode"] == t["InsurerCode"], "%s: InsurerCode = pagina SAM (C2334)" % pg)
chk(int(t["ApdxPageCountTotal"]) == int(t["Apdx2PageCount"]) + int(t["Apdx3PageCount"]), "P23 = P20.2 + P21.2")

# ---------------- 5. examples in SAM Spec col K
K = lambda r: spec.cell(r, 11).value
a11, p3, a12 = dec(K(45)), dec(K(46)), dec(K(47))
chk(q(a11 * p3 / 100) == a12, "SAM Spec K47 %s = K45 x K46" % K(47))
chk(dec(K(48)) == 6 * a11 and dec(K(49)) == 6 * a12, "K48/K49 = pagina cheia (6 linhas)")
n = int(K(19))
chk(int(K(18)) == math.ceil(n / 6) == int(K(35)), "K18 = K35 = ceil(%d/6) = %d folhas" % (n, math.ceil(n / 6)))
chk(dec(K(20)) == n * a11, "K20 %s = %d x A11" % (K(20), n))
chk(dec(K(21)) == n * a12, "K21 %s = %d x A12" % (K(21), n))
chk(int(K(27)) == int(K(18)) + int(K(23)), "K27 P23 = K18 + K23")
chk(dec(K(25)) == dec(K(68)) == dec(K(71)) and dec(K(26)) == dec(K(70)) == dec(K(72)), "SAM3SDP: K25/K26 = K68,K71/K70,K72")
chk(q(dec(K(68)) * dec(K(69)) / 100) == dec(K(70)), "K70 = K68 x K69")
chk(K(12) == "7" and K(17) == "1" and K(22) == "1" and K(13) == "0", "K12 mes 7; K13/K17/K22 marcas 0/1")
chk(all(lt_cd(str(K(r))) for r in (40, 59)), "K40 %s e K59 %s com digito valido" % (K(40), K(59)))
chk(all(spec.cell(r, 9).value == "2" for r in (32, 51, 74)), "I32/I51/I74 FormVersion = 2")
chk(all(spec.cell(r, 6).value == "N" for r in (8, 9, 37, 38, 56, 57)), "F8,F9,F37,F38,F56,F57 = N (DocDate/DocNumber)")
dot = [f"K{r}" for r in range(2, 75) if isinstance(K(r), str) and re.fullmatch(r"\d+\.\d{2}", K(r))]
chk(not dot, "nenhum exemplo da coluna K com ponto decimal %s" % (dot or ""))

# ---------------- 6. Example Analysis
ea = wb["Example Analysis"]; A = lambda r: ea.cell(r, 1).value
chk(q(dec(A(11)) * dec(A(12)) / 100) == dec(A(13)), "Example Analysis A13 = A11 x A12")
chk(dec(A(14)) == 6 * dec(A(11)), "Example Analysis A14 = 6 x A11")
chk(int(A(9)) == int(K(27)) and int(A(10)) == n, "Example Analysis A9/A10 = SAM Spec K27/K19")
chk(A(7) == "7" and A(8) == "1", "Example Analysis A7 mes 7, A8 marca 1")
chk(q(Decimal("1500") * dec(A(17)) / 100) == dec(A(18)), "Example Analysis A18 = 1500 x A17")

# ---------------- 7. Field Options P3 2026 table
fo = wb["Field Options"]
UN = {"Indefinite": Decimal("1.31"), "Fixed-term": Decimal("2.03")}
AC = {"I": Decimal("0.14"), "II": Decimal("0.49"), "III": Decimal("0.70"), "IV": Decimal("1.40")}
rates = []
for r in range(2, fo.max_row + 1):
    if fo.cell(r, 1).value == "General contribution rate (P3) - 2026":
        m = re.match(r"(Indefinite|Fixed-term) / gr\. (IV|III|II|I)( \+3%)?$", fo.cell(r, 3).value)
        exp_ = Decimal("12.52") + Decimal("6.98") + UN[m.group(1)] + AC[m.group(2)] + Decimal("0.32") + (Decimal(3) if m.group(3) else 0)
        rates.append(dec(fo.cell(r, 2).value))
        chk(dec(fo.cell(r, 2).value) == exp_, "Field Options B%d %s = %s" % (r, fo.cell(r, 2).value, fo.cell(r, 3).value))
chk(len(rates) == 16 and min(rates) == Decimal("21.27") and max(rates) == Decimal("26.25"), "16 taxas, min 21,27 / max 26,25")
chk([fo.cell(r, 2).value for r in range(12, 24)] == [str(i) for i in range(1, 13)], "Field Options B12:B23 = 1..12")
print("INFO  teto 2026: 60 x 2312,15 = %s; MMA 2026 = 1153" % (60 * Decimal("2312.15")))

print("\nRESUMO: %d OK, %d FAIL" % (len(oks), len(fails)))
sys.exit(1 if fails else 0)

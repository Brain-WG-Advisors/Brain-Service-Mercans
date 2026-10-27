"""DD Spain V5.0 -> V5.1: STG feedback on the ESS (Modelo 145). In-place cell edits by XML, byte-copy of untouched parts.
Changed cells get a new light-orange fill FFFCE4D6 (V5.0 additions stay light yellow FFFFF2CC)."""
import re, sys, zipfile, datetime
from xml.sax.saxutils import escape
import openpyxl

SRC, OUT = sys.argv[1], sys.argv[2]
zin = zipfile.ZipFile(SRC)
parts = {n: zin.read(n) for n in zin.namelist()}
wbv = openpyxl.load_workbook(SRC)  # values only used to locate rows / read current text

# ---------- styles: new fill + cloned xfs ----------
styles = parts["xl/styles.xml"].decode("utf-8")
fm = re.search(r'(<fills count=")(\d+)(">)(.*?)(</fills>)', styles, re.S)
ORANGE = int(fm.group(2))
styles = (styles[:fm.start()] + fm.group(1) + str(ORANGE + 1) + fm.group(3) + fm.group(4)
          + '<fill><patternFill patternType="solid"><fgColor rgb="FFFCE4D6"/><bgColor rgb="FFFCE4D6"/></patternFill></fill>'
          + fm.group(5) + styles[fm.end():])
m = re.search(r'(<cellXfs count=")(\d+)(">)(.*?)(</cellXfs>)', styles, re.S)
xfs = re.findall(r'<xf [^>]*?(?:/>|>.*?</xf>)', m.group(4), re.S)
assert int(m.group(2)) == len(xfs)
new_xfs, clone = [], {}
def hi(s):
    s = int(s)
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
    if isinstance(val, float):
        new = f'<c r="{ref}" s="{hi(st)}"><v>{val}</v></c>'
    else:
        new = f'<c r="{ref}" s="{hi(st)}" t="inlineStr"><is><t xml:space="preserve">{escape(val)}</t></is></c>'
    return xml[:mm.start()] + new + xml[mm.end():]

def sheet_file(name):
    idx = wbv.sheetnames.index(name) + 1
    return f"xl/worksheets/sheet{idx}.xml"

# ---------- Country Fields ----------
CF = wbv["Country Fields"]
row_of = {}
for r in range(1, CF.max_row + 1):
    v = CF.cell(r, 5).value
    if isinstance(v, str) and v.startswith("$hr."):
        row_of[v[4:]] = r
def cur(code, col): return CF.cell(row_of[code], col).value or ""
COL = dict(ord="C", name="D", label="F", desc="G", pre="I", valid="M", notes="W")
NUM = dict(ord=3, name=4, label=6, desc=7, pre=9, valid=13, notes=23)
edits = {}
def put(code, key, val): edits[f"{COL[key]}{row_of[code]}"] = val
def app(code, key, txt):
    base = str(cur(code, NUM[key])).rstrip()
    put(code, key, (base + " " + txt).strip() if base else txt)

HELP = "ESS help text (Form 145{sec}, official wording): «{t}»"
T_MOVIL = ("Si anteriormente estaba Vd. en situación de desempleo e inscrito en la oficina de empleo y la aceptación del puesto "
           "de trabajo actual ha exigido el traslado de su residencia habitual a un nuevo municipio, indique la fecha de dicho traslado")
T_IRREG = ("Marque esta casilla si, en el plazo comprendido en los 5 períodos impositivos anteriores al ejercicio al que corresponde "
           "la presente comunicación, ha percibido rendimientos del trabajo con período de generación superior a 2 años, a los que, "
           "a efectos del cálculo del tipo de retención le haya sido aplicada la reducción por irregularidad contemplada en el "
           "artículo 18.2 de la Ley del Impuesto y, sin embargo, posteriormente usted no haya aplicado la citada reducción en su "
           "correspondiente autoliquidación del Impuesto sobre la Renta")
T_VIV = ("Si está Vd. efectuando pagos por préstamos destinados a la adquisición o rehabilitación de su vivienda habitual por los que "
         "vaya a tener derecho a deducción por inversión en vivienda habitual en el IRPF y la cuantía total de sus retribuciones "
         "íntegras en concepto de rendimientos del trabajo procedentes de todos sus pagadores es inferior a 33.007,20 euros anuales, "
         "marque con una \"X\" esta casilla. Importante: sólo podrán cumplimentar este apartado los contribuyentes que hayan "
         "adquirido su vivienda habitual, o hayan satisfecho cantidades por obras de rehabilitación de la misma, antes del 1 de enero de 2013.")
T_PENS = "Pensión compensatoria en favor del cónyuge. Importe anual que está Vd. obligado a satisfacer por resolución judicial"
T_ANUA = "Anualidades por alimentos en favor de los hijos. Importe anual que está Vd. obligado a satisfacer por resolución judicial"
T_DESC = ("Datos de los hijos o descendientes menores de 25 años (o mayores de dicha edad si son discapacitados) que conviven con Vd. "
          "y que no tienen rentas anuales superiores a 8.000 euros.")
T_ASC = ("Datos de los ascendientes mayores de 65 años (o menores de dicha edad si son discapacitados) que conviven con Vd. durante, "
         "al menos, la mitad del año y que no tienen rentas anuales superiores a 8.000 euros.")
T_ENTERO = ("En caso de hijos que convivan únicamente con Vd., sin convivir también con el otro progenitor (padre o madre), o de nietos "
            "que convivan únicamente con Vd., sin convivir también con ningún otro de sus abuelos, indíquelo marcando con una \"X\" esta casilla.")
T_ADOP = ("Solamente en el caso de hijos adoptados o de menores acogidos. Tratándose de hijos adoptados que previamente hubieran "
          "estado acogidos, indique únicamente el año del acogimiento.")
T_CONV = ("Si alguno de los ascendientes convive también, al menos durante la mitad del año, con otros descendientes del mismo grado "
          "que Vd., indique en esta casilla el número total de descendientes con los que convive, incluido Vd. (Si los ascendientes "
          "sólo conviven con Vd., no rellene esta casilla).")
V_DISC = ("ESS: show only 3 options with the Form 145 wording (Disability Codes keys 0, 1 and 3) plus the separate assistance/reduced "
          "mobility flag. Key 2 is not shown to the employee: it is derived when key 1 is chosen and the flag = Yes (Modelo 190 pos. 167).")
V_FLAG = ("Only allowed when the disability is 33% or more and below 65% (AEAT withholding algorithm 2026, validations 8, 15 and 17). "
          "At 65% or more the +3,000 EUR assistance amount already applies (LIRPF art. 60).")

# Employee Information
app("family_situation", "valid", "ESS: dropdown with the 3 options of Form 145 Section 1, showing the full official text (Family Situation Codes).")
put("related_person_nif", "name", "Spouse NIF")
put("related_person_nif", "label", "NIF del cónyuge")
put("related_person_nif", "desc", "NIF of the spouse. Required only when Family Situation = 2 and must be empty otherwise "
    "(Form 145 Section 1: «si ha marcado la casilla 2, deberá consignar en esta casilla el NIF de su cónyuge»; AEAT withholding "
    "algorithm 2026, validations 4 and 5). Modelo 190 pos. 158-166.")
put("related_person_nif", "pre", "If Family Situation = 2")
app("disability_code", "valid", V_DISC)
app("disability_assistance_reduced_mobility_flag", "valid", V_FLAG)
app("geographic_mobility", "desc", HELP.format(sec=" Section 1", t=T_MOVIL))
app("geographic_mobility_relocation_date", "desc", HELP.format(sec=" Section 1", t=T_MOVIL))
app("irregular_income_reduction_not_applied_flag", "desc", HELP.format(sec=" Section 1", t=T_IRREG))
app("home_loan_deduction_flag", "desc", HELP.format(sec=" Section 5", t=T_VIV))
app("spousal_compensatory_pension_annual", "desc", HELP.format(sec=" Section 4", t=T_PENS))
app("child_maintenance_annuities_annual", "desc", HELP.format(sec=" Section 4", t=T_ANUA))

# Descendants: form order per child (birth year, adoption year, full computation, disability, assistance)
for n in range(1, 17):
    b = 5 * (n - 1)
    put(f"child_{n}_birth_year", "ord", float(b + 1))
    put(f"child_{n}_adoption_year", "ord", float(b + 2))
    put(f"child_{n}_full_computation_flag", "ord", float(b + 3))
    put(f"child_{n}_disability_code", "ord", float(b + 4))
    put(f"child_{n}_disability_assistance_flag", "ord", float(b + 5))
    app(f"child_{n}_full_computation_flag", "desc", HELP.format(sec=" Section 2", t=T_ENTERO))
    app(f"child_{n}_adoption_year", "desc", HELP.format(sec=" Section 2, note (1)", t=T_ADOP))
    app(f"child_{n}_disability_code", "valid", V_DISC)
    app(f"child_{n}_disability_assistance_flag", "valid", V_FLAG)
app("child_1_birth_year", "notes", "Descendants sub-group " + HELP.format(sec=" Section 2", t=T_DESC))

# Ascendants: form order (birth year, cohabitation, disability, assistance)
for n in (1, 2):
    b = 4 * (n - 1)
    put(f"ascendant_{n}_birth_year", "ord", float(b + 1))
    put(f"ascendant_{n}_cohabitation_count", "ord", float(b + 2))
    put(f"ascendant_{n}_disability_code", "ord", float(b + 3))
    put(f"ascendant_{n}_disability_assistance_flag", "ord", float(b + 4))
    app(f"ascendant_{n}_cohabitation_count", "desc", HELP.format(sec=" Section 3", t=T_CONV))
    app(f"ascendant_{n}_disability_code", "valid", V_DISC)
    app(f"ascendant_{n}_disability_assistance_flag", "valid", V_FLAG)
app("ascendant_1_birth_year", "notes", "Ascendants sub-group " + HELP.format(sec=" Section 3", t=T_ASC))

# drop no-op edits
edits = {k: v for k, v in edits.items()
         if CF[k].value != v and not (isinstance(v, float) and CF[k].value == v)}
f = sheet_file("Country Fields"); x = parts[f].decode("utf-8")
for ref, val in edits.items(): x = set_cell(x, ref, val)
parts[f] = x.encode("utf-8")
CF_EDITS = edits

# ---------- Country Option Mappers ----------
OM = wbv["Country Option Mappers"]
def om_row(mapper, key):
    for r in range(1, OM.max_row + 1):
        if OM.cell(r, 2).value == mapper and str(OM.cell(r, 3).value) == key: return r
    raise KeyError((mapper, key))
OMV = {
 ("Family Situation Codes", "1"): ("Single, widowed, divorced or legally separated, with unmarried children under 18 (or legally incapacitated and under extended or restored parental authority) who live only with you and not also with the other parent, provided at least one child or descendant is entered in Section 2.",
   "Soltero/a, viudo/a, divorciado/a o separado/a legalmente con hijos solteros menores de 18 años o incapacitados judicialmente y sometidos a patria potestad prorrogada o rehabilitada que conviven exclusivamente con Vd., sin convivir también con el otro progenitor, siempre que proceda consignar al menos un hijo o descendiente en el apartado 2 de este documento."),
 ("Family Situation Codes", "2"): ("Married and not legally separated, and your spouse does not earn more than EUR 1,500 a year, excluding exempt income.",
   "Casado/a y no separado/a legalmente cuyo cónyuge no obtiene rentas superiores a 1.500 euros anuales, excluidas las exentas."),
 ("Family Situation Codes", "3"): ("Family situation other than the two above (e.g. single without children, married with a spouse earning more than EUR 1,500 a year). Also choose this option if you do not wish to state your family situation.",
   "Situación familiar distinta de las dos anteriores (solteros sin hijos, casados cuyo cónyuge obtiene rentas superiores a 1.500 euros anuales, ..., etc.). Marque también esta casilla si no desea manifestar su situación familiar."),
 ("Disability Codes", "0"): ("No disability, or degree below 33%", "Sin discapacidad o grado inferior al 33%"),
 ("Disability Codes", "1"): ("Degree of 33% or more and below 65%", "Igual o superior al 33% e inferior al 65%"),
 ("Disability Codes", "2"): ("Degree of 33% or more and below 65%, with need for third-party assistance or reduced mobility",
   "Igual o superior al 33% e inferior al 65%, con necesidad de ayuda de terceras personas o movilidad reducida"),
 ("Disability Codes", "3"): ("Degree of 65% or more", "Igual o superior al 65%"),
}
OM_NOTE2 = ("Modelo 190 pos. 167, code 2. Not shown in ESS: derived when key 1 is chosen and the assistance/reduced mobility flag = Yes "
            "(Form 145 shows the assistance box separately).")
om_edits = {}
for (mp, k), (en, es) in OMV.items():
    r = om_row(mp, k)
    for col, v in (("D", en), ("E", es)):
        if OM[f"{col}{r}"].value != v: om_edits[f"{col}{r}"] = v
r2 = om_row("Disability Codes", "2"); om_edits[f"F{r2}"] = OM_NOTE2
f = sheet_file("Country Option Mappers"); x = parts[f].decode("utf-8")
for ref, val in om_edits.items(): x = set_cell(x, ref, val)
parts[f] = x.encode("utf-8")

# ---------- Filteration for SaaS (hidden): same ordinals for the rows that exist there ----------
FS = wbv["Filteration for SaaS"]
new_ord = {k: v for k, v in ((c, CF[f"C{row_of[c]}"].value) for c in row_of)}
for ref, val in CF_EDITS.items():
    if ref.startswith("C"):
        code = CF[f"E{ref[1:]}"].value[4:]; new_ord[code] = val
fs_edits = {}
for r in range(1, FS.max_row + 1):
    for c in range(1, 9):
        v = FS.cell(r, c).value
        if isinstance(v, str) and v in new_ord and (v.startswith("child_") or v.startswith("ascendant_")):
            oc = FS.cell(r, c - 1)
            if isinstance(oc.value, (int, float)) and oc.value != new_ord[v]:
                fs_edits[oc.coordinate] = float(new_ord[v])
f = sheet_file("Filteration for SaaS"); x = parts[f].decode("utf-8")
for ref, val in fs_edits.items(): x = set_cell(x, ref, val)
parts[f] = x.encode("utf-8")

# ---------- Version Control: insert row 35 (5.1) ----------
f = sheet_file("Version Control"); s1 = parts[f].decode("utf-8")
row34 = re.search(r'<row r="34"[^>]*>.*?</row>', s1, re.S).group(0)
sty = dict(re.findall(r'<c r="([A-G])34" s="(\d+)"', row34))
serial = (datetime.date(2026, 10, 20) - datetime.date(1899, 12, 30)).days
VC = ("STG Spain feedback on the ESS (Modelo 145), Employee Tax Relief Declaration: official Form 145 wording added as ESS help text; "
      "Family Situation and Disability option texts aligned to the form; Related Person NIF renamed Spouse NIF, required only when "
      "Family Situation = 2; Disability shown in ESS as 3 options plus the assistance flag (key 2 derived for Modelo 190), flag only "
      "with 33%-65%; Descendants and Ascendants ordinals follow the form order. Internal codes unchanged. Changes in light orange.")
def inl(ref, s, t): return f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{escape(t)}</t></is></c>'
def h(col): return hi(sty[col])
vc_row = (f'<row r="35" ht="15.75" customHeight="1"><c r="A35" s="{sty["A"]}"/><c r="B35" s="{h("B")}"><v>5.1</v></c>'
          f'<c r="C35" s="{h("C")}"><v>{serial}.0</v></c>' + inl("D35", h("D"), VC) + inl("E35", h("E"), "Draft")
          + inl("F35", h("F"), "Wallisson Gomes") + f'<c r="G35" s="{sty["G"]}"/></row>')
def rows1(mm):
    r = int(mm.group(2)); nr = r + 1 if r >= 35 else r
    body = re.sub(r'(<c r=")([A-Z]+)(\d+)(")', lambda q: f'{q.group(1)}{q.group(2)}{nr}{q.group(4)}', mm.group(4))
    return (vc_row if r == 35 else "") + f'<row r="{nr}"{mm.group(3)}>{body}</row>'
s1 = re.sub(r'(<row r="(\d+)"([^>]*)>(.*?)</row>)', rows1, s1, flags=re.S)
def shref(ref):
    c, r = re.match(r"([A-Z]+)(\d+)$", ref).groups(); r = int(r)
    return f"{c}{r + 1 if r >= 35 else r}"
s1 = re.sub(r'<mergeCell ref="([A-Z]+\d+):([A-Z]+\d+)"/>', lambda q: f'<mergeCell ref="{shref(q.group(1))}:{shref(q.group(2))}"/>', s1)
s1 = re.sub(r'<dimension ref="([A-Z]+\d+):([A-Z]+)(\d+)"/>', lambda q: f'<dimension ref="{q.group(1)}:{q.group(2)}{int(q.group(3)) + 1}"/>', s1)
parts[f] = s1.encode("utf-8")

# ---------- write styles + zip ----------
m = re.search(r'(<cellXfs count=")(\d+)(">)(.*?)(</cellXfs>)', styles, re.S)
styles = styles[:m.start()] + m.group(1) + str(len(xfs) + len(new_xfs)) + m.group(3) + m.group(4) + "".join(new_xfs) + m.group(5) + styles[m.end():]
parts["xl/styles.xml"] = styles.encode("utf-8")
with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as zo:
    for info in zin.infolist():
        zo.writestr(info, parts[info.filename])
print("Country Fields edits", len(CF_EDITS), "| Option Mappers", len(om_edits), "| SaaS ordinals", len(fs_edits), "| new xfs", len(new_xfs))

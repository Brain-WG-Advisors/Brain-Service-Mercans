"""DD Spain V4.9 -> V5.0: Modelo 145 fields. XML surgery, byte-copy of untouched parts."""
import re, sys, zipfile, datetime
from xml.sax.saxutils import escape

SRC, OUT = sys.argv[1], sys.argv[2]
zin = zipfile.ZipFile(SRC)
parts = {n: zin.read(n) for n in zin.namelist()}

# ---------- styles: clone xfs with a new light-yellow fill (FFFFF2CC) ----------
styles = parts["xl/styles.xml"].decode("utf-8")
m = re.search(r'(<cellXfs count=")(\d+)(">)(.*?)(</cellXfs>)', styles, re.S)
xfs = re.findall(r'<xf [^>]*?(?:/>|>.*?</xf>)', m.group(4), re.S)
assert int(m.group(2)) == len(xfs)
fm = re.search(r'(<fills count=")(\d+)(">)(.*?)(</fills>)', styles, re.S)
YELLOW = int(fm.group(2))
styles = (styles[:fm.start()] + fm.group(1) + str(YELLOW + 1) + fm.group(3) + fm.group(4)
          + '<fill><patternFill patternType="solid"><fgColor rgb="FFFFF2CC"/><bgColor rgb="FFFFF2CC"/></patternFill></fill>'
          + fm.group(5) + styles[fm.end():])
m = re.search(r'(<cellXfs count=")(\d+)(">)(.*?)(</cellXfs>)', styles, re.S)
new_xfs, clone_map = [], {}
def blue(s):
    s = int(s)
    if s not in clone_map:
        x = xfs[s]
        x = re.sub(r'fillId="\d+"', f'fillId="{YELLOW}"', x)
        if 'applyFill=' not in x:
            x = x.replace('<xf ', '<xf applyFill="1" ', 1)
        clone_map[s] = len(xfs) + len(new_xfs)
        new_xfs.append(x)
    return clone_map[s]

# ---------- Country Fields (sheet5) ----------
s5 = parts["xl/worksheets/sheet5.xml"].decode("utf-8")
GROUP = "Employee Tax Relief Declaration"
SUB = {"EI": ("Employee Information", 1.0, "employee_information"),
       "DE": ("Descendants", 2.0, "descendants"),
       "AS": ("Ascendants", 3.0, "ascendants")}
D = {
 1: "Annual amount the employee must pay to the spouse by court order. Reduces the base for calculating the withholding rate.",
 2: "Annual amount the employee must pay to the children by court order. Triggers the separate withholding calculation of RIRPF art. 85.2.",
 3: "Employee pays a loan for a main home bought or renovated before 01-01-2013. If total pay is below 33,007.20 EUR, the withholding rate is reduced by 2 points.",
 4: "Employee states that the 30% reduction for income generated over more than 2 years, applied by the payer in the last 5 years, was not used in their tax return. Without this flag, the payer cannot apply the reduction again.",
 5: "Year of adoption or foster placement. The +2,800 EUR minimum applies in that year and the next 2, regardless of the child's age.",
 6: "Number of descendants (employee included) the ascendant lives with. The ascendant minimum is divided by this number.",
}
def row(ordn, name, code, label, desc, ftype, fmt, valid, sub, default, note):
    g = SUB[sub]
    # columns B..X
    return [("s", "Spain"), ("n", ordn), ("s", name), ("s", code), ("s", label), ("s", desc), ("s", "O"), None,
            ("s", ftype), ("s", fmt) if fmt else None, None, ("s", valid) if valid else None,
            ("s", GROUP), ("n", 9.0), ("s", "employee_tax_relief_declaration"),
            ("s", g[0]), ("n", g[1]), ("s", g[2]),
            (("n", default) if isinstance(default, float) else ("s", default)) if default is not None else None,
            ("s", "Write"), ("s", "Read"), ("s", note), ("s", "Yes")]

EI_ROWS = [
 row(10.0, "Spousal Compensatory Pension (Annual Amount)", "$hr.spousal_compensatory_pension_annual",
     "Pensión compensatoria a favor del cónyuge (importe anual)", D[1], "Decimal", "Amount, 2 decimals (EUR)",
     "Numeric >= 0.", "EI", None,
     "Form 145 Section 4. RIRPF art. 83.3.f; AEAT withholding algorithm 2026 (CONYUGE); Modelo 190 pos. 197-209."),
 row(11.0, "Child Maintenance Annuities (Annual Amount)", "$hr.child_maintenance_annuities_annual",
     "Anualidades por alimentos a favor de los hijos (importe anual)", D[2], "Decimal", "Amount, 2 decimals (EUR)",
     "Numeric >= 0.", "EI", None,
     "Form 145 Section 4. RIRPF art. 85.2; LIRPF art. 64; AEAT withholding algorithm 2026 (ANUALIDADES); Modelo 190 pos. 210-222."),
 row(12.0, "Home Loan Deduction (Flag)", "$hr.home_loan_deduction_flag",
     "Préstamo para vivienda habitual (deducción)", D[3], "Boolean", "Yes/No",
     "Only when total annual employment income from all payers is below 33,007.20 EUR and the home was bought or renovated before 01-01-2013.", "EI", "No",
     "Form 145 Section 5. RIRPF arts. 86.1 (last para.) and 88.1; LIRPF transitional provision 18; AEAT withholding algorithm 2026 (PRESVIV); Modelo 190 pos. 254."),
 row(13.0, "Irregular Income Reduction Not Applied (Flag)", "$hr.irregular_income_reduction_not_applied_flag",
     "Rendimientos irregulares: reducción no aplicada en la autoliquidación", D[4], "Boolean", "Yes/No",
     None, "EI", "No",
     "Form 145 Section 1. LIRPF art. 18.2 (3rd para.); RIRPF art. 83.3.a (2nd para.)."),
]
DE_ROWS = [row(16.0 + n, f"Child {n} - Adoption/Foster Year", f"$hr.child_{n}_adoption_year",
               f"Hijo/a {n}: año de adopción o acogimiento", D[5], "Integer", None,
               "4-digit year. Only for adopted or fostered children; for an adopted child previously fostered, the year of foster placement.",
               "DE", None, "Form 145 Section 2. LIRPF art. 58.2 (2nd para.); AEAT withholding algorithm 2026 (AÑOADOP); Modelo 190 pos. 223.")
           for n in range(1, 5)]

EI_ROWS.append(
 row(14.0, "Geographic Mobility - Relocation Date", "$hr.geographic_mobility_relocation_date",
     "Movilidad geográfica: fecha del traslado",
     "Date the employee moved residence to take the job (previously unemployed and registered). The +2,000 EUR expense increase applies only in the year of the move and the next one (LIRPF art. 19.2.f); Modelo 190 reports it per year. Form 145 Section 1.",
     "Date", "YYYY-MM-DD", None, "EI", None,
     "Form 145 Section 1. LIRPF art. 19.2.f (2nd para.); AEAT withholding algorithm 2026 (MOVIL); Modelo 190 pos. 170."))
EI_ROWS[-1][6] = ("s", "CM"); EI_ROWS[-1][7] = ("s", "If Geographic Mobility = Yes")

SUFFIX = (" Descendants from the 4th onward add 4,500 EUR each (LIRPF art. 58.1); the AEAT withholding service "
          "accepts up to 16 descendants (AEATRetenciones2026.xsd, Descendiente maxOccurs=16).")
def child_rows(n):
    base = 21.0 + 5 * (n - 5)
    def r(k, name, code, label, desc, ftype, mapper, valid, note, x):
        cells = [("s", "Spain"), ("n", base + k), ("s", name), ("s", code), ("s", label), ("s", desc + SUFFIX), ("s", "O"), None,
                 ("s", ftype), None, ("s", mapper) if mapper else None, ("s", valid) if valid else None,
                 ("s", GROUP), ("n", 9.0), ("s", "employee_tax_relief_declaration"),
                 ("s", "Descendants"), ("n", 2.0), ("s", "descendants"), None,
                 ("s", "Write"), ("s", "Read"), ("s", note) if note else None, ("s", x) if x else None]
        return cells
    out = [
     r(0, f"Child {n} - Disability Code", f"$hr.child_{n}_disability_code", f"Hijo {n}: discapacidad (grado reconocido)",
       "Disability category for the child/descendant as per Form 145.", "Text", "Disability Codes", None, "Form 145 Section 2.", "Yes"),
     r(1, f"Child {n} - Disability Assistance/Reduced Mobility (Flag)", f"$hr.child_{n}_disability_assistance_flag",
       f"Hijo {n}: necesidad de ayuda / movilidad reducida",
       "Indicates whether the child/descendant has accredited the need for assistance from third parties or reduced mobility (Form 145).",
       "Text", "Boolean", None, "Form 145 Section 2.", "Yes"),
     r(2, f"Child {n} - Full Computation (Cómputo por entero) (Flag)", f"$hr.child_{n}_full_computation_flag",
       f"Hijo {n}: cómputo por entero",
       "Indicates the child is computed fully for personal minimums because the child lives exclusively with the employee (Form 145).",
       "Text", "Boolean", None, "Form 145 Section 2.", "Yes"),
     r(3, f"Child {n} - Birth Year", f"$hr.child_{n}_birth_year", f"Hijo/a {n}: año de nacimiento",
       f"Year of birth of descendant {n}, used to determine AEAT age-band classification (under 3 vs. 3-and-over) for Modelo 190 pos. 223-228.",
       "Integer", None, "4-digit year.", None, None),
     r(4, f"Child {n} - Adoption/Foster Year", f"$hr.child_{n}_adoption_year", f"Hijo/a {n}: año de adopción o acogimiento",
       D[5], "Integer", None,
       "4-digit year. Only for adopted or fostered children; for an adopted child previously fostered, the year of foster placement.",
       "Form 145 Section 2. LIRPF art. 58.2 (2nd para.); AEAT withholding algorithm 2026 (AÑOADOP); Modelo 190 pos. 223.", "Yes"),
    ]
    return out
CH_ROWS = [c for n in range(5, 17) for c in child_rows(n)]

AS_ROWS = [row(6.0 + n, f"Ascendant {n} - Cohabitation Count", f"$hr.ascendant_{n}_cohabitation_count",
               f"Ascendiente {n}: convivencia con otros descendientes (n.º)", D[6], "Integer", None,
               "Integer 1-9. Keep 1 when the ascendant lives only with the employee.",
               "AS", 1.0, "Form 145 Section 3. LIRPF art. 61.1; AEAT withholding algorithm 2026 (CONVIVENCIA, values 1-9).")
           for n in range(1, 3)]

# ordinal renumbering of existing rows (original row -> new ordinal)
RENUM = {}   # option A (user, 2026-10-19): existing ordinals unchanged
INSERTS = [(56, EI_ROWS, 76), (72, DE_ROWS + CH_ROWS, 76), (78, AS_ROWS, 76)]   # after row, rows, template style
def shift(r):
    return r + sum(len(rows_) for after, rows_, _ in INSERTS if after < r)

def col_letter(i): return chr(ord("A") + i)
def ref_shift(ref):
    c, r = re.match(r"([A-Z]+)(\d+)$", ref).groups()
    return f"{c}{shift(int(r))}"

rows = re.findall(r'(<row r="(\d+)"([^>]*)>(.*?)</row>)', s5, re.S)
out_rows, changed = [], {}
def build_new(rn, cells, s):
    xs = [f'<c r="A{rn}" s="{s}"/>']
    for i, v in enumerate(cells):
        L = col_letter(i + 1)
        st = (97 if L == "K" else s) if L in ("W", "X") else blue(97 if L == "K" else s)
        if v is None:
            xs.append(f'<c r="{L}{rn}" s="{st}"/>')
        elif v[0] == "n":
            xs.append(f'<c r="{L}{rn}" s="{st}"><v>{v[1]}</v></c>')
        else:
            xs.append(f'<c r="{L}{rn}" s="{st}" t="inlineStr"><is><t xml:space="preserve">{escape(v[1])}</t></is></c>')
    return f'<row r="{rn}" ht="15.75" customHeight="1">' + "".join(xs) + "</row>"

for full, r, attrs, body in rows:
    r = int(r); nr = shift(r)
    body2 = re.sub(r'(<c r=")([A-Z]+)(\d+)(")', lambda m: f'{m.group(1)}{m.group(2)}{nr}{m.group(4)}', body)
    if r in RENUM:
        def fix(mm):
            st = mm.group(1)
            return f'<c r="C{nr}" s="{blue(st)}"><v>{RENUM[r]}</v></c>'
        body2, k = re.subn(rf'<c r="C{nr}" s="(\d+)"><v>[^<]*</v></c>', fix, body2)
        assert k == 1, r
    out_rows.append(f'<row r="{nr}"{attrs}>{body2}</row>')
    for after, new, tmpl in INSERTS:
        if r == after:
            for j, cells in enumerate(new):
                out_rows.append(build_new(nr + 1 + j, cells, tmpl))

head = s5[:s5.find('<row r="')]
tail = s5[s5.rfind("</row>") + 6:]
assert '<sheetData>' in head and tail.lstrip().startswith('</sheetData>')
tail = re.sub(r'<mergeCell ref="([A-Z]+\d+):([A-Z]+\d+)"/>',
              lambda m: f'<mergeCell ref="{ref_shift(m.group(1))}:{ref_shift(m.group(2))}"/>', tail)
head = re.sub(r'(sqref|activeCell)="([A-Z]+\d+)"', lambda m: f'{m.group(1)}="{ref_shift(m.group(2))}"', head)
parts["xl/worksheets/sheet5.xml"] = (head + "".join(out_rows) + tail).encode("utf-8")

t4 = parts["xl/tables/table4.xml"].decode("utf-8")
t4 = re.sub(r'ref="([A-Z]+\d+):([A-Z]+\d+)"', lambda m: f'ref="{ref_shift(m.group(1))}:{ref_shift(m.group(2))}"', t4, count=1)
parts["xl/tables/table4.xml"] = t4.encode("utf-8")

# ---------- Version Control (sheet1): insert row 34 ----------
s1 = parts["xl/worksheets/sheet1.xml"].decode("utf-8")
serial = (datetime.date(2026, 10, 19) - datetime.date(1899, 12, 30)).days
vc_desc = ("Modelo 145 x DD review (STG Spain): added 10 fields to Employee Tax Relief Declaration. "
           "Employee Information: spousal_compensatory_pension_annual, child_maintenance_annuities_annual, "
           "home_loan_deduction_flag, irregular_income_reduction_not_applied_flag. "
           "Descendants: child_1..4_adoption_year. Ascendants: ascendant_1..2_cohabitation_count. "
           "Also: geographic_mobility_relocation_date; child_5..16 (5 fields each).")
def inl(ref, s, text):
    return f'<c r="{ref}" s="{s}" t="inlineStr"><is><t xml:space="preserve">{escape(text)}</t></is></c>'
vc_row = (f'<row r="34" ht="15.75" customHeight="1"><c r="A34" s="74"/><c r="B34" s="{blue(64)}"><v>5.0</v></c>'
          f'<c r="C34" s="{blue(71)}"><v>{serial}.0</v></c>' + inl("D34", blue(83), vc_desc) + inl("E34", blue(68), "Draft")
          + inl("F34", blue(68), "Wallisson Gomes") + '<c r="G34" s="74"/></row>')
def sh1(r): return r + 1 if r >= 34 else r
def rows1(mm):
    r = int(mm.group(2)); nr = sh1(r)
    body = re.sub(r'(<c r=")([A-Z]+)(\d+)(")', lambda m: f'{m.group(1)}{m.group(2)}{nr}{m.group(4)}', mm.group(4))
    pre = vc_row if r == 34 else ""
    return pre + f'<row r="{nr}"{mm.group(3)}>{body}</row>'
s1 = re.sub(r'(<row r="(\d+)"([^>]*)>(.*?)</row>)', rows1, s1, flags=re.S)
parts["xl/worksheets/sheet1.xml"] = s1.encode("utf-8")

# ---------- styles write-back ----------
allx = m.group(4).rstrip() + "".join(new_xfs)
styles = styles[:m.start()] + m.group(1) + str(len(xfs) + len(new_xfs)) + m.group(3) + allx + m.group(5) + styles[m.end():]
parts["xl/styles.xml"] = styles.encode("utf-8")

touched = {"xl/styles.xml", "xl/worksheets/sheet5.xml", "xl/worksheets/sheet1.xml", "xl/tables/table4.xml"}
with zipfile.ZipFile(OUT, "w") as zo:
    for info in zin.infolist():
        if info.filename in touched:
            zo.writestr(info, parts[info.filename], compress_type=zipfile.ZIP_DEFLATED)
        else:
            zo.writestr(info, zin.read(info.filename))
print("ok; new xfs", clone_map)

# -*- coding: utf-8 -*-
import io, datetime
import openpyxl

WB = "06-payslip/CO_Compliance_Payslip_Generator.xlsx"
OUT = "08-skill/co-compliance/references/06-payslip.md"
wbv = openpyxl.load_workbook(WB, data_only=True)
wbf = openpyxl.load_workbook(WB, data_only=False)


def raw(v):
    if v is None:
        return ""
    if isinstance(v, (datetime.datetime, datetime.date)):
        return v.isoformat()[:10]
    if isinstance(v, float) and v == int(v):
        return str(int(v))
    return str(v).replace("\r", "").rstrip()


def cl(s):
    return s.replace("|", "\\|").replace("\n", "<br>").strip()


HEAD = """# Colombia - Payslip - COMPLETE REFERENCE

**Source artifact:** `06-payslip/CO_Compliance_Payslip_Generator.xlsx` (8 sheets, Mercans reference format,
palette matched cell-for-cell to `shared/REFERENCE_Payslip_Spain.xlsx`)
**Jurisdiction:** Colombia (CO) - **Currency:** COP - **Fiscal year:** 2026
**Sheets:** `How to set up Payslip` - `Compliance Payslip` - `Colombia (EN)` - `Colombia (ES)` -
`Payslip Spec` - `Field Option` - `Population Range` - `Unit Rate Details`

---

## 1. Mandatory payslip content - the legal position

**Colombia has NO statutory payslip-content article in its labour code.** The Substantive Labour Code
(*Codigo Sustantivo del Trabajo*, Decreto 2663 de 1950) was grep-tested across its full consolidated text for
the seven Spanish terms used for a payslip - *desprendible*, *comprobante de pago*, *colilla*,
*volante de pago*, *recibo de pago*, *constancia de pago* and *detalle de la liquidacion* - with **zero hits**.
Ley 2466 de 2025 added none.

**The operative itemisation rule is tax law, not labour law: Resolucion DIAN 000013 de 2021 art. 5**, which
lists the mandatory content of the electronic payroll support document, read with **art. 24**, which makes the
graphical representation *permissive* but requires it to carry that content if it is issued.

A separate, genuinely labour-law duty exists and is narrower: **Ley 1393 de 2010** obliges the employer to
inform the worker of the social-security contributions paid on the worker's behalf.

### Resolucion DIAN 000013 de 2021 art. 5 - the 13 mandatory items, and their status in this generator

| # | Item | Present in the generator |
|---|---|---|
| 1 | Employer's or issuer's surnames and names, or corporate name, and tax identification number | YES - rows 7, 9 |
| 2 | Employee's or beneficiary's surnames and names, and identity document number | YES - rows 12, 16 |
| 3 | Identification of the document - a unique consecutive number preceded by the authorised prefix | **NO** - only a static `REF-CO-2026` footer |
| 4 | Generation date (*fecha de generacion*) | **NO** |
| 5 | Payment or credit date (*fecha de pago o abono*) | **NO** |
| 6 | Accrued payroll values (*valores devengados de nomina*), itemised by concept | YES - rows 21-25 |
| 7 | Deducted payroll values (*valores deducidos de nomina*), itemised by concept | YES - rows 28-32 |
| 8 | Total difference between accrued and deducted | YES - row 34 |
| 9 | Payment or credit period | PARTIAL - `Tax Month` / `Days in Month`, no explicit period start/end |
| 10 | Payment method and medium (*forma y medio de pago*) | PARTIAL - banking block, no payment-method code |
| 11 | Country, department and municipality of origin | PARTIAL - free-text employer address |
| 12 | Content of the authorised technical annex | - |
| 13 | **CUNE** - *Codigo Unico de Nomina Electronica* | **NO** |
| - | Technical Annex 13.1: **QR code at least 2 cm x 2 cm on EVERY page**, encoding the DIAN document-search URL with the CUNE as key | **NO** |

> **[QA MAJOR-02]** Grepping the entire workbook for `CUNE`, `QR`, `prefij`, `consecutiv`,
> `Fecha de generacion` and `Generation date` returns **zero hits in all 8 sheets**. If a client issues the
> graphical representation, the document as templated does not carry the art. 5 content that art. 24 requires -
> and the CUNE + QR are precisely what make the paper document traceable to the validated XML.
> **Fix:** add a header block for `Prefijo + Consecutivo`, `Fecha de generacion`, `Fecha de pago`,
> `Periodo de pago (desde/hasta)`, `Forma y medio de pago`, `Pais / Departamento / Municipio de origen`, a
> `CUNE` field, and a placeholder image anchor sized >= 2 cm x 2 cm for the QR. The DD fields already exist:
> `Electronic Payroll Document Prefix`, `Place of Work Country/Department/Municipality Code`, `Payment Form`,
> `Payment Method`.

### Additional mandatory formal requirements where a graphical representation is issued

| Requirement | Rule |
|---|---|
| **Language** | **Spanish**, mandatory. Another language may be **added**, never substituted (Res. DIAN 000013 de 2021 art. 26) |
| **Currency** | **Colombian pesos**, mandatory. Another currency may be added (art. 26) |
| **QR code** | At least **2 cm x 2 cm on every page**, encoding the DIAN document-search URL with the CUNE as the key (Anexo Tecnico 13.1) |
| **Legal status** | The paper or PDF document is a **representation** of the electronic document, not the document itself. Its legal validity derives from the validated XML |

The bilingual design of this generator - `Colombia (ES)` fully in Spanish plus `Colombia (EN)` in English -
satisfies art. 26: Spanish is mandatory and any other language is additive.

### Mercans practice - good practice, not legally required

- itemisation of **employer contributions** for transparency (never a deduction from the employee);
- the **statutory benefit accruals** (*prestaciones sociales*) and balances;
- the **vacation balance**;
- the **hourly divisor and rest-day premium percentage applied**, given the two mid-2026 cut-overs
  (divisor 220 -> 210 on 15 Jul 2026; rest-day premium 80% -> 90% on 1 Jul 2026);
- contract type, hire date and pay frequency;
- year-to-date totals.

### A rounding rule that must not be blended

The payslip carries the **XML** figures - two decimals, round-half-to-even. It must **not** display the
PILA contribution figures (rounded **up** to the nearest 100) as if they were the deduction, nor the
Formulario 350 figure (rounded to the nearest 1,000). Where the client requires the contribution-return figure
to be shown, it must appear as a **separate, labelled line**.

*Legal basis: Resolucion DIAN 000013 de 11 febrero 2021 arts. 5, 24, 26 and Anexo Tecnico 13.1; Ley 1393 de
2010; Codigo Sustantivo del Trabajo (Decreto 2663 de 1950), full consolidated text - no payslip-content
article.*

---

## 2. Line-by-line payslip layout, EN and ES labels side by side

Row numbers are the actual worksheet rows of `Colombia (EN)` and `Colombia (ES)` (identical geometry).
Amounts are the delivered worked example: monthly gross **19,200,000 COP**, net **15,221,235 COP**.

| Row | Section | Label - Colombia (EN) | Label - Colombia (ES) | Rate | Amount (COP) |
|---|---|---|---|---|---|
"""

L = []
W = L.append
W(HEAD)

en = wbv["Colombia (EN)"]
es = wbv["Colombia (ES)"]
enf = wbf["Colombia (EN)"]

SECTION = {
    3: "Title", 6: "Net pay banner", 7: "Employer details", 12: "Employee details",
    19: "Earnings (Devengados)", 27: "Deductions (Deducciones)", 34: "Net pay",
    36: "Employer contributions (Aportes del Empleador)",
    46: "Benefit provisions (Prestaciones Sociales)",
    54: "Banking details", 58: "Contribution & provision summary",
    65: "Year-to-date (Acumulados)", 71: "Statutory notes", 81: "Footer",
}
cursec = ""
for r in range(1, 84):
    if r in SECTION:
        cursec = SECTION[r]

    def firsttext(ws, row):
        for c in range(1, 9):
            v = raw(ws.cell(row=row, column=c).value)
            if v:
                return v
        return ""

    len_ = firsttext(en, r)
    les = firsttext(es, r)
    if not len_ and not les:
        continue
    rate = raw(en.cell(row=r, column=6).value)
    amt = raw(en.cell(row=r, column=8).value)
    famt = raw(enf.cell(row=r, column=8).value)
    if famt.startswith("="):
        amt = "`%s`" % famt
    if amt == len_ or amt == les:
        amt = ""
    if rate == len_ or rate == les:
        rate = ""
    # skip the long statutory notes here - reproduced verbatim in section 5
    if r >= 72 and r <= 79:
        continue
    W("| %d | %s | %s | %s | %s | %s |" % (r, cursec, cl(len_)[:200], cl(les)[:200], cl(rate), cl(amt)))

W("""
> **[QA MAJOR-01]** Every wage-type code on both language sheets is an `XXXXX` placeholder
> (rows 21-24, 28-31, 38-43, 48-51 = 18 lines x 2 sheets = **36 cells**). The WTC contains exact matches for
> all 18 lines. Substitute the real codes:
> `CO-SALARIO-BASICO`, `CO-AUX-TRANSPORTE`, `CO-COMISIONES`, `CO-DED-SALUD`, `CO-DED-PENSION`,
> `CO-DED-FSP-SOLIDARIDAD`, `CO-RETENCION-FUENTE`, `CO-ER-SALUD`, `CO-ER-PENSION`, `CO-ER-ARL`, `CO-ER-CCF`,
> `CO-ER-SENA`, `CO-ER-ICBF`, `CO-PROV-CESANTIAS`, `CO-PROV-INTERESES-CESANTIAS`, `CO-PROV-PRIMA`,
> `CO-PROV-VACACIONES`. Rows 22 (*Overtime & Surcharges*) and 23 (*Commissions & Bonuses*) each bundle
> multiple wage types - split them or label them with an explicit multi-code list.

---

## 3. The calculation - every formula in the generator, and the arithmetic re-derived

| Cell | Line | Formula (verbatim) |
|---|---|---|""")

for r in enf.iter_rows(min_row=1, max_row=90):
    for c in r:
        if isinstance(c.value, str) and c.value.startswith("="):
            lbl = ""
            for cc in range(1, 9):
                v = raw(enf.cell(row=c.row, column=cc).value)
                if v and not v.startswith("="):
                    lbl = v
                    break
            W("| `%s` | %s | `%s` |" % (c.coordinate, cl(lbl)[:90], cl(c.value)))

W("""
### Re-derivation (independently verified by the stage-07 QA cross-check - exact)

| Line | Basis | Value (COP) |
|---|---|---|
| Basic salary (`H21`) | contractual | 18,000,000 |
| Overtime & surcharges (`H22`) | worked example | 500,000 |
| Commissions & bonuses (`H23`) | worked example | 700,000 |
| Transport allowance (`H24`) | nil - salary is far above 2 SMMLV | 0 |
| **Total earnings** | 18,000,000 + 500,000 + 700,000 + 0 | **19,200,000** |
| IBC (contribution base, `H59`) | `SUM(H21:H23)` - excludes the auxilio de transporte | 19,200,000 |
| Health - employee 4% (`H28`) | IBC 19,200,000, below the 25-SMMLV cap of 43,772,625 | 768,000 |
| Pension - employee 4% (`H29`) | idem | 768,000 |
| FSP 1% (`H30`) | IBC is above the 4-SMMLV trigger of 7,003,620 | 192,000 |
| **Retencion en la fuente** (`H31`) | see the depuration below | **2,250,765** |
| Total deductions | 768,000 + 768,000 + 192,000 + 2,250,765 | 3,978,765 |
| **Net pay** (`I8` -> `H34`) | `SUM(H21:J24) - SUM(H28:J31)` | **15,221,235** |

**Withholding depuration, ET arts. 383 / 388 (re-derived to the peso):**

```
gross                                    19,200,000
- employee contributions (4+4+1%)         1,728,000   ET arts. 55, 56 (non-taxable income)
= subtotal                               17,472,000
- 25% exempt income, capped 790 UVT/yr    3,447,955   ET art. 206 num. 10; 790 UVT / 12 = 65.8333 UVT
= taxable base                           14,024,045   = 267.76732 UVT  (UVT 2026 = 52,374)
ET art. 383 band 150-360 UVT:  0.28 x (267.76732 - 150) + 10 = 42.97485 UVT
42.97485 UVT x 52,374                   = 2,250,765   <- the exact figure on the payslip
```

The **40% / 1,340-UVT** caps of ET art. 388 were tested and are **not binding** on this example.

**Employer block (`H38:H43`)** - Salud 8.5% - Pension 12% - ARL 0.522% (risk class I) - CCF 4% - SENA 2% -
ICBF 3%, all on `SUM(H21:H23)`.

**Provisions (`H48:H51`)** - Cesantias 8.33% - Intereses a las cesantias 1% - Prima de servicios 8.33% -
Provision de vacaciones 4.17% = **21.83%** total (agreeing with the WTC's 21.8333%).

**The base split is deliberate and correct:** the **cesantias, intereses and prima** provisions run on
`SUM($H$21:$H$24)` and therefore **include the auxilio de transporte** (CST art. 253 / Ley 15 de 1959 art. 7),
while the **vacation** provision runs on `SUM($H$21:$H$23)` and **excludes** it (CST art. 192). This is the
counter-intuitive Colombian distinction and the generator implements it rather than glossing it.

> **[QA MINOR-05]** `H51` (vacation provision) includes row 22, which bundles *Overtime & Surcharges*. Per
> CST art. 192 - and per WTC column X, which sets `CO-HED` / `CO-HEN` / `CO-RECARGO-DOMINICAL` to vacation base
> **No** while `CO-RECARGO-NOCTURNO` is **Yes** - overtime and rest-day work must be **excluded** from the
> vacation base while the night premium is **included**. The bundled demo line makes the two inseparable.
> **Fix:** split row 22 into an overtime line (excluded from `H51`) and a premium line (included).

**Year-to-date block (7 months):** gross 134,400,000 - employee contributions 12,096,000 - income tax
15,755,355 - net **106,548,645**. YTD net / 7 = 15,221,235, exactly the monthly net, so the YTD and monthly
blocks are mutually consistent.

> **[QA MINOR-06]** The `Colombia (EN)` / `(ES)` sheets use only the grey family (`FFDCDCDC`, `FFA9A9A9`,
> `FFF5F5F5`). This **matches `shared/REFERENCE_Payslip_Spain.xlsx` exactly**, which itself has no navy and no
> green - so the build faithfully mirrors the reference. The v2.4 check nonetheless calls for a navy/grey
> palette with a green net-pay highlight (`FF1F4E78` navy on the section header rows 19, 27, 36, 46, 54, 58,
> 65, 71; `FFC6EFCE` green on `A34:H34`). Cosmetic; should be raised against the shared Spain reference rather
> than fixed only in Colombia.

---
""")


def dump_sheet(shname, title, note=""):
    W("\n## %s\n" % title)
    if note:
        W(note + "\n")
    ws = wbv[shname]
    blocks = []
    cur = None
    for r in ws.iter_rows(min_row=1, max_row=ws.max_row):
        v = [raw(c.value) for c in r]
        while v and v[-1].strip() == "":
            v.pop()
        if not any(x.strip() for x in v):
            if cur is not None and cur[0] == "text" and cur[1] and cur[1][-1] != [""]:
                cur[1].append([""])
            continue
        kind = "table" if len([x for x in v if x.strip()]) >= 2 else "text"
        if cur is None or cur[0] != kind:
            cur = (kind, [])
            blocks.append(cur)
        cur[1].append(v)
    for kind, rows in blocks:
        if kind == "text":
            while rows and rows[-1] == [""]:
                rows.pop()
            W("")
            for v in rows:
                line = next((x for x in v if x.strip()), "")
                W(line)
            W("")
        else:
            ncol = max(len(v) for v in rows)
            rows = [v + [""] * (ncol - len(v)) for v in rows]
            keep = [i for i in range(ncol) if any(r[i].strip() for r in rows)]
            rows = [[cl(r[i]) for i in keep] for r in rows]
            n = len(keep)
            W("")
            if n == 2 and len(rows) >= 3:
                W("| Item | Value |")
                W("|---|---|")
                body = rows
            else:
                W("| " + " | ".join(rows[0]) + " |")
                W("|" + "---|" * n)
                body = rows[1:]
            for v in body:
                W("| " + " | ".join(v) + " |")
            W("")


W("---\n")
W("# 4. Sheet `Payslip Spec` - field list, local labels and HRB mapping (verbatim)\n")
dump_sheet("Payslip Spec", "4.1 Full spec table", "")

W("\n---\n\n# 5. Statutory notes printed on the payslip (verbatim, both languages)\n")
W("## 5.1 `Colombia (EN)` - Statutory Notes - Fiscal Year 2026\n")
W("```")
for r in range(71, 84):
    v = raw(en.cell(row=r, column=1).value)
    if v:
        W(v)
        W("")
W("```")
W("\n## 5.2 `Colombia (ES)` - Notas Legales - Ejercicio Fiscal 2026\n")
W("```")
for r in range(71, 84):
    v = raw(es.cell(row=r, column=1).value)
    if v:
        W(v)
        W("")
W("```")

W("\n---\n")
W("# 6. Remaining sheets\n")
dump_sheet("Field Option", "6.1 Sheet `Field Option`")
dump_sheet("Population Range", "6.2 Sheet `Population Range`")
dump_sheet("Unit Rate Details", "6.3 Sheet `Unit Rate Details` - earning / rate / unit account codes",
           "> **[VERIFY WITH RA]** The sheet itself is headed *\"illustrative placeholder account codes; align "
           "to actual CO-WTC once available\"*. These 5-digit numbers are **not** the WTC codes and must be "
           "reconciled to the WTC (or to the Mercans numeric range once assigned for Colombia) at "
           "configuration time.")
dump_sheet("Compliance Payslip", "6.4 Sheet `Compliance Payslip` (the Mercans reference template, unmodified)")
dump_sheet("How to set up Payslip", "6.5 Sheet `How to set up Payslip` (template instructions, unmodified)")

W("""
---

# 7. Payslip readiness summary

| Item | Status |
|---|---|
| 8-sheet Mercans standard, reference order | PASS |
| Grey palette matched to `REFERENCE_Payslip_Spain.xlsx` | PASS (navy/green absent - MINOR-06) |
| Spanish sheet fully translated (Res. DIAN 000013 art. 26) | PASS - the only residual English tokens are Spanish-English cognates (*Pension*, *Base*, *Total*) |
| Arithmetic (gross, IBC, three employee contributions, withholding, net, YTD, employer block, provisions) | **PASS - re-derived exactly** |
| CST art. 192 vs art. 253 base distinction | PASS (implemented) |
| Wage-type codes wired to the WTC | **FAIL - `XXXXX` placeholders (MAJOR-01)** |
| Res. DIAN 000013 art. 5 header block, CUNE, QR | **FAIL - absent (MAJOR-02)** |
| Vacation base excludes bundled overtime | **PARTIAL (MINOR-05)** |
| `Unit Rate Details` account codes | **Placeholder - [VERIFY WITH RA]** |
""")

txt = "\n".join(L)
io.open(OUT, "w", encoding="utf-8").write(txt)
print(OUT, len(txt))

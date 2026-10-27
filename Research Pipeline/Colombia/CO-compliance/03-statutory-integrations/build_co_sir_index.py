# -*- coding: utf-8 -*-
"""Build CO-SIR-INDEX-001-v1.0.docx from integration-landscape.json."""
import json, os
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "integration-landscape.json")
OUT = os.path.join(BASE, "CO-SIR-INDEX-001-v1.0.docx")

LS = json.load(open(SRC, encoding="utf-8"))
AUTH = {a["code"]: a for a in LS["authorities"]}
S = LS["summary"]

NAVY = RGBColor(0x1F, 0x3A, 0x5F)

doc = Document()
n = doc.styles["Normal"]
n.font.name = "Arial"
n.font.size = Pt(11)
n.element.rPr.rFonts.set(qn("w:eastAsia"), "Arial")

sec = doc.sections[0]
sec.orientation = WD_ORIENT.LANDSCAPE
sec.page_width, sec.page_height = Cm(29.7), Cm(21.0)
sec.left_margin = sec.right_margin = Cm(1.5)
sec.top_margin = sec.bottom_margin = Cm(1.5)


def para(text="", size=11, bold=False, color=None, align=None, space_after=6, italic=False):
    p = doc.add_paragraph()
    if align is not None:
        p.alignment = align
    p.paragraph_format.space_after = Pt(space_after)
    if text:
        r = p.add_run(text)
        r.font.name = "Arial"
        r.font.size = Pt(size)
        r.bold = bold
        r.italic = italic
        if color is not None:
            r.font.color.rgb = color
    return p


def h1(text):
    return para(text, size=14, bold=True, color=NAVY, space_after=8)


def set_cell(cell, text, size=9, bold=False, color=None, italic=False):
    cell.text = ""
    p = cell.paragraphs[0]
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.space_before = Pt(2)
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(size)
    r.bold = bold
    r.italic = italic
    if color is not None:
        r.font.color.rgb = color
    return p


def add_cell_line(cell, text, size=8, italic=True, bold=False):
    p = cell.add_paragraph()
    p.paragraph_format.space_after = Pt(2)
    r = p.add_run(text)
    r.font.name = "Arial"
    r.font.size = Pt(size)
    r.italic = italic
    r.bold = bold
    return p


def set_widths(table, widths_cm):
    table.autofit = False
    for row in table.rows:
        for i, w in enumerate(widths_cm):
            row.cells[i].width = Cm(w)


def repeat_header(row):
    trPr = row._tr.get_or_add_trPr()
    el = OxmlElement("w:tblHeader")
    el.set(qn("w:val"), "true")
    trPr.append(el)


# ------------------------------------------------------------------ cover block
para(space_after=0)
para("Colombia\nStatutory Integration Register -- Authority Index",
     size=22, bold=True, color=NAVY, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=4)
para("CO-SIR-INDEX-001  v1.0", size=14, bold=True,
     align=WD_ALIGN_PARAGRAPH.CENTER, space_after=10)
para("Mercans Compliance Regulations Team", size=11,
     align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
para("Jurisdiction: Colombia (CO)  |  Currency: COP  |  Tax Year 2026", size=11,
     align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
para("Scope: private-sector salaried population per scope_manifest v1.0 "
     "(6 in-scope filings, 7 descoped)", size=11,
     align=WD_ALIGN_PARAGRAPH.CENTER, space_after=2)
para("Source: 03-statutory-integrations/integration-landscape.json  |  "
     "Discovery verdict: %s  |  Generated %s" % (LS["verdict"], LS["generated"]),
     size=11, align=WD_ALIGN_PARAGRAPH.CENTER, space_after=14)

# ---------------------------------------------------------------- version table
h1("Version Control")
vt = doc.add_table(rows=2, cols=4)
vt.style = "Light Grid Accent 1"
vt.alignment = WD_TABLE_ALIGNMENT.LEFT
for i, htxt in enumerate(["Version", "Date", "Author", "Notes"]):
    set_cell(vt.rows[0].cells[i], htxt, size=9, bold=True)
for i, v in enumerate(["v1.0", LS["generated"], "Mercans Compliance Regulations Team",
                       "Initial issue. Authority index generated from "
                       "integration-landscape.json (produced by %s)." % LS["produced_by"]]):
    set_cell(vt.rows[1].cells[i], v, size=9)
set_widths(vt, [2.2, 2.6, 6.0, 15.9])
para(space_after=8)

# -------------------------------------------------------------- authority index
h1("1. Authority Index")
para("One row per authority identified in the Colombian payroll statutory landscape. "
     "%d authorities in total: %d with a genuine system-to-system channel, %d manual. "
     "Of the %d in-scope filings, %d is carried system-to-system and %d are manual."
     % (S["authorities_total"], S["authorities_with_system_to_system"],
        S["authorities_manual_only"], S["in_scope_filings_total"],
        S["in_scope_filings_via_system_to_system"], S["in_scope_filings_manual"]),
     size=10, space_after=8)

COLS = ["Authority", "Integration", "Channel", "Direction(s)",
        "Developer portal", "Runbook location"]
WIDTHS = [5.0, 1.9, 8.4, 4.4, 5.0, 2.0]

ROWS = [
    {
        "code": "DIAN-NE",
        "title": "DIAN -- Servicio de Validacion de Nomina Electronica",
        "legal": "Unidad Administrativa Especial Direccion de Impuestos y Aduanas "
                 "Nacionales (DIAN)",
        "filings": "Carries: CO-DIAN-NE-MONTHLY-001 (monthly, one document per employee, "
                   "within the first 10 days of the following month)",
        "integration": "YES",
        "channel": "Machine-to-machine SOAP 1.2 web service over HTTPS (WS-Addressing, "
                   "WS-Security timestamp). Operation SendNominaSync on "
                   "WcfDianCustomerServices, plus GetStatus. Payload is base64 of a ZIP "
                   "holding one XAdES-EPES-signed UBL 2.1 XML, max 500 KB, UTF-8 only. "
                   "Authenticated by an X.509 certificate from an ONAC-accredited CA. No "
                   "portal step in the transmission path; habilitacion (SoftwareID + PIN) "
                   "is a one-time portal-gated onboarding prerequisite, not a channel.",
        "direction": "OUTBOUND + INBOUND -- both legs in one synchronous call. Outbound: "
                     "signed NominaIndividual / NominaIndividualDeAjuste. Inbound: base64 "
                     "ApplicationResponse (IsValid, StatusCode, XmlDocumentKey). The "
                     "inbound leg is a hard dependency, not a receipt -- the CUNE and "
                     "validation status must be persisted, since deductibility of the "
                     "payroll cost depends on validation.",
        "portal": "https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/"
                  "documentacion-tecnica-soporte-de-pago-nomina-electronica/",
        "portal_note": "Artefacts BUILD-READY: WSDL, XSD v1.0.6, UBL/XAdES schema set, "
                       "samples and the 269-page annex, all public with no login.",
        "runbook": "03-statutory-integrations/DIAN-NE/",
    },
    {
        "code": "DIAN-MUISCA",
        "title": "DIAN -- Servicios Informaticos Electronicos / Muisca",
        "legal": "Unidad Administrativa Especial Direccion de Impuestos y Aduanas "
                 "Nacionales (DIAN)",
        "filings": "Carries: CO-DIAN-F350-MONTHLY-002, CO-DIAN-EXO2276-ANNUAL-005, "
                   "CO-DIAN-F220-ANNUAL-004",
        "integration": "NO",
        "channel": "Portal round-trip (browser). Form 350 is keyed or loaded in the Muisca "
                   "web form; Formato 2276 v4 is prepared offline in the prevalidador and "
                   "uploaded as XML through the informacion exogena service. Authenticated "
                   "by the DIAN Instrumento de Firma Electronica (IFE), which is issued to "
                   "a natural person and exercised interactively -- the structural reason "
                   "no M2M path exists. Same legal entity as DIAN-NE, entirely different "
                   "posture: the electronic payroll web service does not carry these "
                   "filings.",
        "direction": "OUTBOUND only.",
        "portal": "None published by the authority.",
        "portal_note": "No SOAP, REST or SFTP filing surface exists. Vendor-marketed "
                       "\"DIAN APIs\" are commercial wrappers around the e-invoicing "
                       "service and do not cover Form 350 or exogena -- do not model them "
                       "as a statutory channel.",
        "runbook": "Not applicable -- manual authority.",
    },
    {
        "code": "PILA-OI",
        "title": "PILA -- Planilla Integrada de Liquidacion de Aportes, via a licensed "
                 "operador de informacion",
        "legal": "Ministerio de Salud y Proteccion Social (system owner); collection "
                 "intermediated by private operadores de informacion supervised by the "
                 "Superintendencia Financiera",
        "filings": "Carries: CO-PILA-MONTHLY-003 (monthly; 2nd to 16th business day of the "
                   "following month, by the last two digits of the employer NIT). SENA, "
                   "ICBF and Cajas de Compensacion ride on this same planilla.",
        "integration": "NO",
        "channel": "Portal round-trip through a licensed private operador de informacion "
                   "(SOI/ACH Colombia, Simple S.A., SuAporte/ARUS, Aportes en Linea, Mi "
                   "Planilla, Asopagos, Compensar). Under Res. MSPS 2388 de 2016 the "
                   "modalidad electronica is keying the planilla online or uploading a "
                   "fixed-width flat file (.txt/.csv) to the electronic means made "
                   "available by the operator; the operator settles, collects and forwards "
                   "to each administradora. Operator account credentials only -- no "
                   "certificate, no signature. The employer never transacts directly with "
                   "the government and there is no government-facing endpoint to integrate "
                   "with.",
        "direction": "OUTBOUND + INBOUND. Outbound: Archivo Tipo 1 (34 fields / 567 "
                     "positions) and Archivo Tipo 2 (header 22 fields / 359 positions, one "
                     "Registro Tipo 2 per contributor), fixed-width. Inbound: the "
                     "operator's settlement/payment output, which must be reconciled "
                     "(planilla number, payment date, per-contributor rejections) -- "
                     "operator-specific, with no published layout.",
        "portal": "None published by the authority.",
        "portal_note": "See note (a) below on the ARUS/SuAporte \"Portal Desarrolladores "
                       "APIS PILA\" (https://www.suaporte.com.co/portal-apis/) -- a "
                       "private commercial offering, deliberately not scored as an "
                       "integration.",
        "runbook": "Not applicable -- manual authority.",
    },
    {
        "code": "FONDOS-CESANTIAS",
        "title": "Fondos de Cesantias -- annual severance-savings deposit allocation",
        "legal": "Private severance-savings funds (Porvenir, Proteccion, Colfondos, "
                 "Skandia, FNA), reached through a licensed operador de informacion",
        "filings": "Carries: CO-CESANTIAS-DEPOSIT-ANNUAL-006 (annual; by 14 February "
                   "following the 31 December liquidation -- for accrual year 2026, "
                   "deposit by Friday 12 February 2027)",
        "integration": "NO",
        "channel": "Portal round-trip through an operador de informacion, in two selectable "
                   "modes: online form (Planilla En Linea) or file upload (Envio de Archivo "
                   "Unificado de Cesantias), .txt/.csv (zipped above 1 MB) or XLS 97-2003 "
                   "(16 columns A-P, no header row). Operator account credentials only. "
                   "Explicitly not machine-to-machine: no XSD, no SOAP, no digital "
                   "signature, no certificate.",
        "direction": "OUTBOUND + INBOUND. Outbound: the deposit allocation file. Inbound: "
                     "planilla number, comprobante PDF and the fund's deposit certificate "
                     "evidencing compliance with the February deadline.",
        "portal": "None published by the authority.",
        "portal_note": "Record layouts are nevertheless public, from two independent "
                       "operator manuals (ACH/SOI and Simple S.A.), and are the basis of "
                       "CO-CESANTIAS-006.",
        "runbook": "Not applicable -- manual authority.",
    },
]

t = doc.add_table(rows=1, cols=len(COLS))
t.style = "Light Grid Accent 1"
t.alignment = WD_TABLE_ALIGNMENT.LEFT
for i, htxt in enumerate(COLS):
    set_cell(t.rows[0].cells[i], htxt, size=9, bold=True)
repeat_header(t.rows[0])

assert len(ROWS) == len(LS["authorities"]) == S["authorities_total"]

for r in ROWS:
    # cross-check every row against the JSON so the docx cannot drift from source
    src = AUTH[r["code"]]
    assert (src["integration"] is True) == (r["integration"] == "YES"), r["code"]
    expected_rb = src.get("runbook_location") or "Not applicable -- manual authority."
    assert expected_rb == r["runbook"], r["code"]
    assert sorted(src["directions"]) == sorted(
        ["outbound"] if r["direction"].startswith("OUTBOUND only")
        else ["inbound", "outbound"]), r["code"]

    cells = t.add_row().cells
    set_cell(cells[0], r["code"], size=9, bold=True, color=NAVY)
    add_cell_line(cells[0], r["title"], size=8, italic=False)
    add_cell_line(cells[0], r["legal"], size=8, italic=True)
    add_cell_line(cells[0], r["filings"], size=8, italic=True)
    set_cell(cells[1], r["integration"], size=9, bold=True,
             color=NAVY if r["integration"] == "YES" else None)
    set_cell(cells[2], r["channel"], size=8)
    set_cell(cells[3], r["direction"], size=8)
    set_cell(cells[4], r["portal"], size=8)
    add_cell_line(cells[4], r["portal_note"], size=8, italic=True)
    set_cell(cells[5], r["runbook"], size=8, bold=(r["integration"] == "YES"))

set_widths(t, WIDTHS)
para(space_after=6)

para("(a)  One operator, ARUS / Enlace Operativo, markets \"APIS PILA\" and runs a "
     "developer portal at https://www.suaporte.com.co/portal-apis/. Fetched on 2026-09-04 "
     "it returned only a welcome shell -- no API catalogue, no endpoints, no OpenAPI or "
     "WSDL, no authentication description. It is a private commercial offering from one "
     "intermediary, available under contract, with no public specification and no statutory "
     "standing; it does not generalise across operators and cannot be built from public "
     "artefacts. PILA is therefore scored integration=false.",
     size=8, italic=True, space_after=12)

# -------------------------------------------------------------- runbook policy
h1("2. Configuration Runbooks")
para("Per-authority Configuration Runbooks are produced only for authorities carrying "
     "integration=true. In Colombia that is a single authority, DIAN-NE, whose runbook is "
     "filed at 03-statutory-integrations/DIAN-NE/. The authorities scored integration=false "
     "-- DIAN-MUISCA, PILA-OI and FONDOS-CESANTIAS -- are manual channels: the obligation is "
     "discharged by a human in a browser (a DIAN Muisca web form under a personal IFE, or a "
     "file upload to a private operador de informacion), so there is no connection to "
     "configure and no runbook is produced for them. Their record layouts, deadlines and "
     "validation rules are still fully specified, but they belong to the report "
     "specifications in 04-reports-spec rather than to this register. The absence of a "
     "runbook for a manual authority is a deliberate scoping decision recorded here, not an "
     "omission.", size=10, space_after=10)

para("Delivery note: the cesantias deposit has no integration, and late deposit costs one "
     "day's salary per day of delay per employee, uncapped (Ley 50 de 1990 art. 99 num. 3). "
     "The manual posture therefore concentrates operational risk on the single most "
     "expensive Colombian year-end failure, and warrants an explicit controlled manual "
     "procedure in delivery planning even though no runbook is written.",
     size=10, italic=True, space_after=10)

para("Channel types absent from the Colombian landscape entirely: %s."
     % ", ".join(S["no_channel_type_found_anywhere"]), size=9, italic=True)

doc.save(OUT)
print("WROTE", OUT, os.path.getsize(OUT), "bytes")

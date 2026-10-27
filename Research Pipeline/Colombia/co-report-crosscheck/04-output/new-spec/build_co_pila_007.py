# -*- coding: utf-8 -*-
"""Builds CO-PILA-007-AportesPensionados-Spec.xlsx (PILA of the pension payer, Res. MSPS 2388/2016 Anexo Tecnico 3 v15).

Styles are copied cell by cell from the structural precedent 05-final/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx
(fonts, fills, borders, alignment, widths, freeze panes). No content is copied from it.
Run:  python build_co_pila_007.py   (writes CO-PILA-007-AportesPensionados-Spec.xlsx next to this script)
"""
import copy, math, pathlib
import openpyxl
from openpyxl.styles import PatternFill

HERE = pathlib.Path(__file__).resolve().parent
KIT = HERE.parent.parent
PREC = KIT / "05-final" / "CO-PILA-003-AportesSeguridadSocial-Spec.xlsx"
OUT = HERE / "CO-PILA-007-AportesPensionados-Spec.xlsx"

AT3 = "AT3 v15"  # Res. MSPS 2388/2016 Anexo Tecnico 3 'Aportes a Seguridad Social de Pensionados', v15, 24-07-2026
SPEC_SHEET = "PILA Pensioners Spec"
SMLMV = 1750905  # 2026 SMMLV, Decreto 0159 de 2026 (used only for the worked example)

pw = openpyxl.load_workbook(PREC)


def st(ws_name, coord):
    c = pw[ws_name][coord]
    return dict(font=copy.copy(c.font), fill=copy.copy(c.fill), border=copy.copy(c.border),
                alignment=copy.copy(c.alignment), number_format=c.number_format)


def put(ws, r, c, v, style, fill=None):
    cell = ws.cell(r, c, v)
    cell.font = copy.copy(style["font"]); cell.fill = copy.copy(style["fill"])
    cell.border = copy.copy(style["border"]); cell.alignment = copy.copy(style["alignment"])
    cell.number_format = style["number_format"]
    if fill:
        cell.fill = PatternFill(fill_type="solid", fgColor=fill, bgColor=fill)
    return cell


def height(ws, r, texts_widths, base=15.0):
    lines = 1
    for t, w in texts_widths:
        if t is None:
            continue
        n = 0
        for part in str(t).split("\n"):
            n += max(1, math.ceil(len(part) / max(1.0, w * 1.15)))
        lines = max(lines, n)
    ws.row_dimensions[r].height = base if lines <= 1 else round(10.5 * lines + 11.25, 2)


def widths_from(ws, prec_name):
    for k, d in pw[prec_name].column_dimensions.items():
        if d.width:
            ws.column_dimensions[k].width = d.width


wb = openpyxl.Workbook()
wb.remove(wb.active)

# ---------------------------------------------------------------- formatting helpers
N_FMT = "N({n}) - numeric, right-justified, ZERO-filled to the left"
A_FMT = "A({n}) - alphanumeric, left-justified, SPACE-filled to the right"
NO_RND = "Not an amount - no rounding."
RND_IBC = "Rounded UP to the whole peso (Decreto 780 de 2016 art. 3.2.1.5 num. 1, text of Decreto 1990 de 2016 art. 1)."
RND_100 = ("Rounded UP to the next multiple of 100 (Decreto 780 de 2016 art. 3.2.1.5 num. 2, text of Decreto 1990 de 2016 art. 1; "
           f"{AT3} requires the rounding rules in force for contributions).")
RND_MES = f"Whole pesos (numeric field without decimals, {AT3} ch. 1 s.0, p. 7); the mesada is reported as paid."
RND_RATE = "Rate - no rounding; the decimal layout is held in the file-format configuration of the chosen information operator."
CAT = {"P": "FFFFEB9C", "S": "FFBDD7EE", "K": "FFC6EFCE", "X": "FFFFC7CE"}

FIELDS = []  # (section or None, dict)


def sec(title):
    FIELDS.append((title, None))


def F(rec, campo, en, local, L, start, end, typ, mand, cond, ex, mapping, expl, pay="Y", rel="Y",
      opts="-", rnd=NO_RND, neg="N", vt="Text", cat="P", fmt=None, pos=None):
    rid = {"A1": "A1", "R1": "T2R1", "R2": "T2R2"}[rec]
    recname = {"A1": "File Type 1 - Pension payer", "R1": "File Type 2 - Record 1 Header",
               "R2": "File Type 2 - Record 2 Pensioner detail"}[rec]
    if fmt is None:
        fmt = (N_FMT if typ == "N" else A_FMT).format(n=L)
    FIELDS.append((None, dict(rec=rec, campo=campo, en=en, local=local, L=L, start=start, end=end, typ=typ,
                              recname=recname, fid=f"{rid}-{campo:03d}", mand=mand, cond=cond, ex=ex,
                              mapping=mapping, expl=expl, pay=pay, rel=rel, opts=opts, rnd=rnd, neg=neg,
                              vt=vt, cat=cat, fmt=fmt, pos=pos or f"Pos {start}-{end}")))


# ================================================================ ARCHIVO TIPO 1
sec("═══ FILE TYPE 1 - GENERAL DATA OF THE PENSION PAYER (27 campos, 482 posiciones) ═══")
F("A1", 1, "Pension payer name or corporate name", "Nombre o razón social del pagador de pensiones", 150, 1, 150, "A", "Y", None,
  "MERCANS COLOMBIA S.A.S.", "Payer.Legal_Name",
  f"Registered name of the pension payer, supplied by the payer. Echoed byte for byte into the header record (T2R1-003: 'El registrado en el campo 1 del archivo tipo 1'). Source: {AT3} §1.1 campo 1, p. 7; §2.1.1 campo 3, p. 14.")
F("A1", 2, "Pension payer document type", "Tipo documento del pagador de pensiones", 2, 151, 152, "A", "Y", None, "NI", "Payer.Document_Type",
  f"Closed list: NI (Número de Identificación Tributaria), CC, CE, PA, CD. A legal-person payer reports NI. Echoed into T2R1-004. Source: {AT3} §1.1 campo 2, p. 7.",
  opts="-> Field Options: Document type of the pension payer", vt="Code")
F("A1", 3, "Pension payer identification number", "Número de identificación del pagador de pensiones", 16, 153, 168, "A", "Y", None, "900123456", "Payer.Document_Number",
  f"The payer's identification number. The information operator validates that it contains only letters A-Z and digits 0-9. Alphanumeric only for PA (up to 16) and CD (up to 11); digits only for CC (up to 10), NI (up to 9) and CE (up to 7). The NIT check digit is reported separately in A1-004. Echoed into T2R1-005. This validation applies to payments made from 1 October 2026 (pension contribution period September 2026). Source: {AT3} §1.1 campo 3, pp. 7-8; ch. 5 §5.32, pp. 132-133.",
  vt="Identifier")
F("A1", 4, "Verification digit", "Dígito de verificación", 1, 169, 169, "N", "C",
  "MANDATORY where 'Person type' (A1-009) = J (Jurídica); ZERO in every other case.", "8", "Payer.NIT_DV",
  f"Check digit of the payer's NIT, validated by the information operator under the rules defined by DIAN. Echoed into T2R1-006. Source: {AT3} §1.1 campo 4, p. 8.", vt="Identifier")
F("A1", 5, "Branch or dependency code", "Código de la sucursal o dependencia", 10, 170, 179, "A", "C",
  "MANDATORY where 'Form of presentation' (A1-010) = S (Sucursal).", "", "Payer.Branch_Code",
  f"Code of the branch or dependency that files. Echoed into T2R1-008. Source: {AT3} §1.1 campo 5, p. 8.", vt="Code")
F("A1", 6, "Branch or dependency name", "Nombre de la sucursal o dependencia", 40, 180, 219, "A", "C",
  "MANDATORY where A1-010 = S. Where the branch has no name, its code is written here.", "", "Payer.Branch_Name",
  f"Name of the branch or dependency. Where the branch has no name, the payer writes its code. Echoed into T2R1-009. Source: {AT3} §1.1 campo 6, p. 8.")
F("A1", 7, "Pension payer class", "Clase de pagador de pensiones", 1, 220, 220, "A", "Y", None, "B", "Payer.Pension_Payer_Class",
  f"A = pension payer with 200 or more pensioners; B = pension payer with fewer than 200 pensioners; I = Independiente (the payer is a natural person). The count takes in all pensioners of all branches or dependencies. Source: {AT3} §1.1 campo 7, pp. 8-9; §1.2.1, p. 12.",
  opts="-> Field Options: Pension payer class", vt="Code")
F("A1", 8, "Legal nature", "Naturaleza jurídica", 1, 221, 221, "N", "Y", None, "2", "Payer.Legal_Nature",
  f"1 Pública (legal person of public law); 2 Privada (natural or legal person of private law); 3 Mixta (sociedades de economía mixta, Ley 489 de 1998 art. 97). Source: {AT3} §1.1 campo 8, p. 9; §1.2.2, p. 12.",
  opts="-> Field Options: Legal nature", vt="Code")
F("A1", 9, "Person type", "Tipo persona", 1, 222, 222, "A", "Y", None, "J", "Payer.Person_Type",
  f"N Natural or J Jurídica. Where J, the verification digit (A1-004), the legal representative's identification number (A1-018) and document type (A1-020) are mandatory. Source: {AT3} §1.1 campo 9, p. 9; §1.2.3, p. 12.",
  opts="-> Field Options: Person type", vt="Code")
F("A1", 10, "Form of presentation", "Forma de presentación", 1, 223, 223, "A", "Y", None, "U", "Payer.Presentation_Form",
  f"Validated against the list U Único / S Sucursal. S makes the branch code and name (A1-005, A1-006) mandatory. Echoed into T2R1-007. Source: {AT3} §1.1 campo 10, p. 9.",
  opts="-> Field Options: Form of presentation", vt="Code")
F("A1", 11, "Correspondence address", "Dirección correspondencia", 40, 224, 263, "A", "Y", None, "CALLE 100 7 33", "Payer.Address",
  f"Correspondence address of the payer, supplied by the payer. Source: {AT3} §1.1 campo 11, p. 9.")
F("A1", 12, "City or municipality code", "Código ciudad o municipio", 3, 264, 266, "A", "Y", None, "001", "Payer.Municipality_Code",
  f"Municipality code, validated by the information operator against the DANE DIVIPOLA list. Source: {AT3} §1.1 campo 12, p. 9.", vt="Code")
F("A1", 13, "Department code", "Código departamento", 2, 267, 268, "A", "Y", None, "11", "Payer.Department_Code",
  f"Department code, validated by the information operator against the DANE DIVIPOLA list. Source: {AT3} §1.1 campo 13, p. 9.", vt="Code")
F("A1", 14, "DANE economic activity code", "Código DANE de la actividad económica", 4, 269, 272, "N", "Y", None, "6920", "Payer.Economic_Activity_Code",
  f"Economic activity of the payer, validated by the information operator against the CIIU Rev. 4 A.C. table issued by DANE (Resolución 66 de 2012 or the rule that replaces it). Source: {AT3} §1.1 campo 14, pp. 9-10.", vt="Code")
F("A1", 15, "Telephone", "Teléfono", 10, 273, 282, "N", "Y", None, "6017000000", "Payer.Phone",
  f"Telephone number of the payer, supplied by the payer. Source: {AT3} §1.1 campo 15, p. 10.", vt="Identifier")
F("A1", 16, "Fax", "Fax", 10, 283, 292, "N", "N", None, "0000000000", "Payer.Fax",
  f"Fax number, optional. As a numeric field it is zero-filled when there is no fax. Source: {AT3} §1.1 campo 16, p. 10; ch. 1 s.0, p. 7.",
  pay="N", rel="N", vt="Identifier", cat="X")
F("A1", 17, "E-mail address", "Dirección de correo electrónico (E-mail)", 60, 293, 352, "A", "N", None, "nomina@mercans.com", "Payer.Email",
  f"Optional. User name: letters a-z, digits 0-9, hyphen, underscore, apostrophe and dot; then the character @; domain name of letters a-z and digits 0-9, hyphen allowed but never as first or last character of the domain. Source: {AT3} §1.1 campo 17, p. 10.",
  pay="N", rel="N")
F("A1", 18, "Legal representative identification number", "Número de identificación del representante legal", 16, 353, 368, "A", "C",
  "MANDATORY where A1-009 = J; blank in every other case.", "79123456", "Payer.Legal_Rep_Document_Number",
  f"Only letters A-Z and digits 0-9. Alphanumeric only for PA (up to 16) and CD (up to 11); digits only for CC (up to 10) and CE (up to 7). This validation applies to payments made from 1 October 2026. Source: {AT3} §1.1 campo 18, pp. 10-11; ch. 5 §5.32, pp. 132-133.",
  vt="Identifier")
F("A1", 19, "Legal representative verification digit", "Dígito de verificación representante legal", 1, 369, 369, "N", "Y", None, "0", "Constant 0",
  f"Always reported as zero: 'Este campo se deberá reportar en cero'. Source: {AT3} §1.1 campo 19, p. 11.",
  pay="N", rel="N", vt="Constant", cat="K")
F("A1", 20, "Legal representative document type", "Tipo identificación representante legal", 2, 370, 371, "A", "C",
  "MANDATORY where A1-009 = J; blank in every other case.", "CC", "Payer.Legal_Rep_Document_Type",
  f"Valid values CC, CE, PA, CD. Source: {AT3} §1.1 campo 20, p. 11.", opts="-> Field Options: Document type of the legal representative", vt="Code")
F("A1", 21, "Legal representative first surname", "Primer apellido del representante legal", 20, 372, 391, "A", "Y", None, "MUESTRA", "Payer.Legal_Rep_First_Surname",
  f"Mandatory, supplied by the payer. Source: {AT3} §1.1 campo 21, p. 11.")
F("A1", 22, "Legal representative second surname", "Segundo apellido del representante legal", 30, 392, 421, "A", "N", None, "EJEMPLO", "Payer.Legal_Rep_Second_Surname",
  f"Supplied by the payer where it exists. Source: {AT3} §1.1 campo 22, p. 11.")
F("A1", 23, "Legal representative first name", "Primer nombre del representante legal", 20, 422, 441, "A", "Y", None, "ANA", "Payer.Legal_Rep_First_Name",
  f"Mandatory, supplied by the payer. Length 20 from position 422; AT3 prints the final position as 440, and the 20-position length, the start of campo 24 at 442 and the record total of 482 fix the field at 422-441. Source: {AT3} §1.1 campo 23, p. 11.")
F("A1", 24, "Legal representative second name", "Segundo nombre del representante legal", 30, 442, 471, "A", "N", None, "MARIA", "Payer.Legal_Rep_Second_Name",
  f"Supplied by the payer where it exists. Source: {AT3} §1.1 campo 24, p. 11.")
F("A1", 25, "Information operator code", "Código del operador", 2, 472, 473, "N", "Y", "Assigned by the information operator's system.", "00", "System.PILA_Operator_Code",
  f"Assigned by the system of the information operator. Echoed into T2R1-017. Source: {AT3} §1.1 campo 25, p. 11; §2.1.1 campo 17, p. 15.",
  pay="N", rel="N", vt="Code", cat="S")
F("A1", 26, "Payment period", "Período de pago", 7, 474, 480, "N", "Y", "Assigned by the information operator's system.", "2026-03", "System.PILA_Payment_Period",
  f"Mandatory, assigned by the system, format AAAA-MM. Source: {AT3} §1.1 campo 26, p. 11.",
  pay="N", rel="N", vt="Period", cat="S", fmt="N(7) - period written as the literal AAAA-MM")
F("A1", 27, "Pension payer type", "Tipo de pagador de pensiones", 2, 481, 482, "N", "Y", None, "01", "Payer.Pension_Payer_Type (constant 01 for this report)",
  f"01 Empleador: public or private companies or natural persons that pay the pensions of their workers. This report covers payer type 01 only. With 01, the pensioner type (T2R2-017) may be 5, 6 or 9 (R01) and the pension type (T2R2-009) may be 2, 3, 4, 8, 10, 11, 12, 13, 14, 20 or 21 (R02). Echoed into T2R1-016. Source: {AT3} §1.1 campo 27, p. 11; §1.2.4, pp. 12-13; ch. 4 §1 table 3, pp. 100-101; ch. 4 §2 table 5, pp. 102-103.",
  opts="-> Field Options: Pension payer type", vt="Code", cat="K")

# ================================================================ REGISTRO TIPO 1
sec("═══ FILE TYPE 2, RECORD TYPE 1 - HEADER (18 campos, 285 posiciones) ═══")
F("R1", 1, "Record type", "Tipo de registro", 2, 1, 2, "N", "Y", None, "01", "Constant 01",
  f"Must be 01. Generated by the operator's system when data are keyed on the web; reported by the payer when the data are uploaded as flat files. Only one header per file, and it is the first record. Source: {AT3} §2.1, p. 14; §2.1.1 campo 1, p. 14.",
  pay="N", rel="N", vt="Constant", cat="K")
F("R1", 2, "Sequence", "Secuencia", 5, 3, 7, "N", "Y", None, "00001", "System.PILA_Header_Sequence",
  f"Ascending sequence, starting at 00001 for each pension payer. Reported by the payer when the data are uploaded as flat files. Source: {AT3} §2.1.1 campo 2, p. 14.",
  pay="N", rel="N", vt="Counter", cat="S")
F("R1", 3, "Pension payer name or corporate name", "Nombre o razón social del pagador de pensiones", 150, 8, 157, "A", "Y", None, "MERCANS COLOMBIA S.A.S.", "Echo of A1-001",
  f"The value of File Type 1 campo 1, byte for byte. Source: {AT3} §2.1.1 campo 3, p. 14.")
F("R1", 4, "Pension payer document type", "Tipo documento del pagador de pensiones", 2, 158, 159, "A", "Y", None, "NI", "Echo of A1-002",
  f"The value of File Type 1 campo 2. Source: {AT3} §2.1.1 campo 4, p. 14.", vt="Code")
F("R1", 5, "Pension payer identification number", "Número de identificación del pagador de pensiones", 16, 160, 175, "A", "Y", None, "900123456", "Echo of A1-003",
  f"The value of File Type 1 campo 3. Source: {AT3} §2.1.1 campo 5, p. 14.", vt="Identifier")
F("R1", 6, "Verification digit", "Dígito de verificación", 1, 176, 176, "N", "C", "Follows A1-004: the check digit where A1-009 = J, zero otherwise.", "8", "Echo of A1-004",
  f"The value of File Type 1 campo 4. Source: {AT3} §2.1.1 campo 6, p. 14.", vt="Identifier")
F("R1", 7, "Form of presentation", "Forma de presentación", 1, 177, 177, "A", "Y", None, "U", "Echo of A1-010",
  f"The value of File Type 1 campo 10. Source: {AT3} §2.1.1 campo 7, p. 14.", vt="Code")
F("R1", 8, "Branch or dependency code", "Código de la sucursal o de la dependencia", 10, 178, 187, "A", "C", "Follows A1-005: populated where A1-010 = S.", "", "Echo of A1-005",
  f"The value of File Type 1 campo 5. Source: {AT3} §2.1.1 campo 8, p. 14.", vt="Code")
F("R1", 9, "Branch or dependency name", "Nombre de la sucursal o dependencia", 40, 188, 227, "A", "C", "Follows A1-006: populated where A1-010 = S.", "", "Echo of A1-006",
  f"The value of File Type 1 campo 6. Source: {AT3} §2.1.1 campo 9, p. 15.")
F("R1", 10, "Payment period for subsystems other than health", "Período de pago para los sistemas diferentes al de salud", 7, 228, 234, "A", "Y", None, "2026-03", "PayPeriod.Period_Code",
  f"Mandatory, format aaaa-mm, supplied by the pension payer. It is the period to which the pension and family compensation fund contributions relate, according to the obligation to contribute. Source: {AT3} §2.1.1 campo 10, p. 15; §2.1.2.1, p. 16.", vt="Period")
F("R1", 11, "Payment period for the health subsystem", "Período de pago para el sistema de salud", 7, 235, 241, "A", "Y", None, "2026-03", "PayPeriod.Health_Period_Code",
  f"Mandatory, format aaaa-mm, supplied by the pension payer. Source: {AT3} §2.1.1 campo 11, p. 15.", vt="Period")
F("R1", 12, "Filing number of the integrated settlement form", "Número de radicación o de la planilla integrada de liquidación de aportes", 10, 242, 251, "N", "Y",
  "Assigned by the information operator's system.", "0000000000", "System.PILA_Planilla_Number",
  f"Assigned by the system; unique per information operator. Source: {AT3} §2.1.1 campo 12, p. 15.", pay="N", rel="N", vt="Identifier", cat="S")
F("R1", 13, "Payment date", "Fecha de pago (aaaa-mm-dd)", 10, 252, 261, "A", "Y", "Assigned by the information operator's system.", "", "System.PILA_Payment_Date",
  f"Assigned by the system from the date of effective payment, format aaaa-mm-dd. Source: {AT3} §2.1.1 campo 13, p. 15.", pay="N", rel="N", vt="Date", cat="S")
F("R1", 14, "Total number of pensioners", "Número total de pensionados", 7, 262, 268, "N", "Y", None, "0000002",
  "COUNT(Record Type 2 where T2R2-017 <> 9)",
  f"Mandatory. Must equal the number of pensioners in the Record Type 2 detail, EXCLUDING the records with 9 (additional UPC beneficiary) in campo 17. Source: {AT3} §2.1.1 campo 14, p. 15.",
  vt="Counter", cat="S")
F("R1", 15, "Total payroll value", "Valor total de la nómina", 12, 269, 280, "N", "Y", None, "000025500000",
  "SUM(T2R2-058 where T2R2-017 <> 9); T2R2-058 is fed by WT 62154 'Monthly Retired Pension-6798'",
  f"Mandatory, supplied by the pension payer: the sum of campo 58 'Valor de mesada pensional' of Record Type 2, EXCLUDING the records with 9 in campo 17. Source: {AT3} §2.1.1 campo 15, p. 15.",
  rnd="Sum of whole-peso mesadas - no further rounding.", vt="Amount")
F("R1", 16, "Pension payer type", "Tipo de pagador de pensiones", 2, 281, 282, "N", "Y", None, "01", "Echo of A1-027",
  f"The value of File Type 1 campo 27 (01 Empleador for this report). Source: {AT3} §2.1.1 campo 16, p. 15.", vt="Code", cat="K")
F("R1", 17, "Information operator code", "Código del operador de información", 2, 283, 284, "N", "Y", "Assigned by the information operator's system.", "00", "Echo of A1-025",
  f"The value of File Type 1 campo 25. Source: {AT3} §2.1.1 campo 17, p. 15.", pay="N", rel="N", vt="Code", cat="S")
F("R1", 18, "Pensioner planilla type", "Tipo de planilla pensionado", 1, 285, 285, "A", "Y", None, "P", "Mercans.PILA_Pensioner_Planilla_Type",
  f"P Planilla pago normal pagadores de pensiones: the main planilla, used by every type of pension payer for the monthly contributions of the pensioners; periods paid late carry interest on arrears. R Planilla pago retroactivo: contributions not paid while the recognition of a pension was outstanding; where the retroactive pension is recognised for the first time, the health contribution goes to ADRES under code MIN001 (except pensioners of the special health regime). L Planilla pago reliquidación: higher contributions from the reliquidation of the mesada for periods before January 2020; only the adjustment is reported. V Planilla pago reliquidación enero de 2020 en adelante: reliquidation from January 2020, one planilla per reliquidated period, each pensioner reported first in A records (as initially reported) and then in C records (final values), health to MIN001. C: reserved for the entity authorised by the National Government for pensioners of territorial entities; an employer payer does not use it. To use P, R, L or V the payer must appear in the file 'INFORMACIÓN PAGADORES DE PENSIONES' that the Ministry of Health places monthly on the secure FTP of each information operator; a payer that does not appear requests inclusion from the Ministry's Subdirección de Pensiones y Otras Prestaciones. More than one planilla per period is allowed, with interest on arrears where due (Decreto 780 de 2016 arts. 3.2.2.1 to 3.2.2.3). Source: {AT3} §2.1.1 campo 18, pp. 15-16; §2.1.2.2, pp. 16-20; ch. 4 §4 table 7, pp. 104-105.",
  opts="-> Field Options: Pensioner planilla type", vt="Code")

# ================================================================ REGISTRO TIPO 2
sec("═══ FILE TYPE 2, RECORD TYPE 2 - DETAILED SETTLEMENT PER PENSIONER (63 campos, 519 posiciones) ═══")
sec("═══ -- record identity and pensioner identification (campos 1 to 8) -- ═══")
F("R2", 1, "Record type", "Tipo de registro", 2, 1, 2, "N", "Y", None, "02", "Constant 02",
  f"Must be 02. At least one record per pensioner, and one record per pension type where a beneficiary holds two types of pension. Source: {AT3} §2.2, p. 21; §2.2.1 campo 1, p. 21.",
  pay="N", rel="N", vt="Constant", cat="K")
F("R2", 2, "Sequence", "Secuencia", 7, 3, 9, "N", "Y", None, "0000001", "System.PILA_Detail_Sequence",
  f"Starts at 0000001 and runs sequentially through the remaining detail records. Reported by the payer when the data are uploaded as flat files. Source: {AT3} §2.2.1 campo 2, pp. 21-22.",
  pay="N", rel="N", vt="Counter", cat="S")
F("R2", 3, "Pensioner first surname", "Primer apellido del pensionado", 20, 10, 29, "A", "Y", None, "PRUEBA", "Pensioner.First_Surname",
  f"Mandatory. Where the document type and number match the Base de Datos Única de Afiliados (BDUA), the information operator replaces campos 3 to 6 with the BDUA values; where they do not match, the payer's values stand. In a pensioner type 9 record: the surname of the additional UPC beneficiary. Source: {AT3} §2.2.1 campo 3, p. 22; §2.2.2.1, pp. 39-40; §2.2.2.4, p. 49.")
F("R2", 4, "Pensioner second surname", "Segundo apellido del pensionado", 30, 30, 59, "A", "N", None, "EJEMPLO", "Pensioner.Second_Surname",
  f"Supplied by the payer where it exists; BDUA replacement as for campo 3. Source: {AT3} §2.2.1 campo 4, p. 22; §2.2.2.1, pp. 39-40.")
F("R2", 5, "Pensioner first name", "Primer nombre del pensionado", 20, 60, 79, "A", "Y", None, "PEDRO", "Pensioner.First_Name",
  f"Mandatory; BDUA replacement as for campo 3. Source: {AT3} §2.2.1 campo 5, p. 22; §2.2.2.1, pp. 39-40.")
F("R2", 6, "Pensioner second name", "Segundo nombre del pensionado", 30, 80, 109, "A", "N", None, "", "Pensioner.Second_Name",
  f"Supplied by the payer where it exists; BDUA replacement as for campo 3. Source: {AT3} §2.2.1 campo 6, p. 22; §2.2.2.1, pp. 39-40.")
F("R2", 7, "Pensioner document type", "Tipo documento del pensionado", 2, 110, 111, "A", "Y", None, "CC", "Pensioner.Document_Type",
  f"Valid values CC, CE, TI, RC, PA, CD, PE, PT. PE (Permiso Especial de Permanencia) may not be used for health contribution periods from September 2023 onwards. Source: {AT3} §2.2.1 campo 7, p. 22; ch. 5 §5.24, p. 130.",
  opts="-> Field Options: Document type of the pensioner", vt="Code")
F("R2", 8, "Pensioner identification number", "Número de identificación del pensionado", 16, 112, 127, "A", "Y", None, "1000000001", "Pensioner.Document_Number",
  f"Mandatory. Only letters A-Z and digits 0-9. Alphanumeric only for PA (up to 16) and CD (up to 11); digits only for TI (up to 11), CC (up to 10), RC (up to 11), CE (up to 7), PE (15), PT (up to 8) and PC (PEP-TUTOR, up to 16). The operator validates that the payer's document type and number differ from the pensioner's (pension type 16 foreign pensioners excepted). This validation applies to payments made from 1 October 2026. Source: {AT3} §2.2.1 campo 8, pp. 22-23; p. 39; §2.2.2.2 type 16, p. 46; ch. 5 §5.32, pp. 132-133.",
  vt="Identifier")
sec("═══ -- pension, pensioner type, causante and residence (campos 9 to 21) -- ═══")
F("R2", 9, "Pension type", "Tipo de pensión", 2, 128, 129, "N", "Y", None, "10", "Pension.Type",
  f"Mandatory. For pension payer type 01 the valid pension types are 2, 3, 4, 8, 10, 11, 12, 13, 14, 20 and 21 (R02). 10 Jubilación: recognised by the employer when the holder reaches the age and the minimum time required. 11 Jubilación para compartir and 14 Convencional para compartir: the employer pays the pension and contributes to the Régimen de Prima Media until the administradora takes over the old-age pension. 13 Convencional: granted by collective agreement, for pensions recognised up to 31 July 2010 (Acto Legislativo 01 de 2005 par. trans. 3). Pension types 20 and 21 carry no maximum or minimum pension validations. For a pensioner type 9 record (additional UPC beneficiary) this field is zero. Valid combinations with the pensioner type are in R03 (10 with 5, 6, 7, 8; 13 with 5, 6). Source: {AT3} §2.2.1 campo 9, pp. 23-24; §2.2.2.2, pp. 40-47; ch. 4 §2 table 5, pp. 102-103; ch. 4 §3 table 6, p. 104.",
  opts="-> Field Options: Pension type", vt="Code")
F("R2", 10, "Shared pension", "Pensión compartida", 1, 130, 130, "A", "Y", None, "N", "Pension.Shared_Flag",
  f"S where the pensioner paid by the employer has already obtained recognition of the shared pension from the corresponding administradora or pension payer; N in every other case. Where S and campo 63 exceeds 10 SMLMV, the information operator multiplies campo 58 by the factor for the total mesada and settles the Fondo de Solidaridad Pensional subsistence contribution. Source: {AT3} §2.2.1 campo 10, pp. 24-25; §2.2.2.21, p. 62.",
  opts="S / N", vt="Flag")
F("R2", 11, "Causante first surname", "Primer apellido del causante", 20, 131, 150, "A", "C", "MANDATORY for pension types 2, 3, 4, 5, 6 and 7.", "", "Pension.Causante_First_Surname",
  f"Surname of the person from whom the survivor pension derives. BDUA replacement applies to campos 11 to 14 as for the pensioner's names. Source: {AT3} §2.2.1 campo 11, p. 25; §2.2.2.3, p. 47.")
F("R2", 12, "Causante second surname", "Segundo apellido del causante", 30, 151, 180, "A", "N", None, "", "Pension.Causante_Second_Surname",
  f"Supplied by the payer where it exists. Source: {AT3} §2.2.1 campo 12, p. 25; §2.2.2.3, p. 47.")
F("R2", 13, "Causante first name", "Primer nombre del causante", 20, 181, 200, "A", "C", "MANDATORY for pension types 2, 3, 4, 5, 6 and 7.", "", "Pension.Causante_First_Name",
  f"First name of the causante. Source: {AT3} §2.2.1 campo 13, p. 25; §2.2.2.3, p. 47.")
F("R2", 14, "Causante second name", "Segundo nombre del causante", 30, 201, 230, "A", "N", None, "", "Pension.Causante_Second_Name",
  f"Supplied by the payer where it exists. Source: {AT3} §2.2.1 campo 14, p. 25; §2.2.2.3, p. 47.")
F("R2", 15, "Causante document type", "Tipo de identificación del causante de la pensión", 2, 231, 232, "A", "C",
  "Populated where there is a causante (pension types 2 to 7, §2.2.2.3); AT3 marks the field 'Obligatorio'.", "", "Pension.Causante_Document_Type",
  f"Valid values CC, CE, TI, RC, PA, CD, PE, PT. Source: {AT3} §2.2.1 campo 15, p. 25; §2.2.2.3, p. 47; ch. 5 §5.26, p. 130.",
  opts="-> Field Options: Document type of the pensioner", vt="Code")
F("R2", 16, "Causante identification number", "Número de identificación del causante", 16, 233, 248, "A", "C",
  "MANDATORY where there is a causante, for pension types 2, 3, 4, 5, 6 and 7.", "", "Pension.Causante_Document_Number",
  f"Same character and length rules as campo 8 (PA up to 16, CD up to 11, TI up to 11, CC up to 10, RC up to 11, CE up to 7, PE up to 15, PT up to 8, PC up to 16). This validation applies to payments made from 1 October 2026. Source: {AT3} §2.2.1 campo 16, pp. 26-27; ch. 5 §5.32, pp. 132-133.",
  vt="Identifier")
F("R2", 17, "Pensioner type", "Tipo de pensionado", 1, 249, 249, "N", "Y", None, "5", "Pensioner.Pensioner_Type",
  f"For pension payer type 01 the valid values are 5, 6 and 9 (R01). 5 Pensionado por el empleador con tope de pensión máxima de 25 SMMLV: the mesada is capped at 25 SMMLV. 6 Pensionado por el empleador sin tope de pensión máxima de 25 SMMLV: the mesada may exceed 25 SMMLV, but the health contribution is made on at most 25 SMLMV. 9 Beneficiario UPC adicional: one additional Record Type 2 per additional UPC beneficiary of a pensioner, carrying campos 3 to 9, 17, 32, 37, 50, 53 and 54 only (campo 9 = 0, campo 37 = 30), every other field blank or zero. For all pensioners the health and pension contribution may never exceed 25 SMMLV. Source: {AT3} §2.2.1 campo 17, p. 27; §2.2.2.4, pp. 48-49; ch. 4 §1 table 3, pp. 100-101.",
  opts="-> Field Options: Pensioner type", vt="Code")
F("R2", 18, "Pensioner resident abroad", "Pensionado en el exterior", 1, 250, 250, "A", "C",
  "X only where the pensioner resides abroad; blank otherwise. Usable with document types CC, TI, RC, CE and PA.", "", "Pensioner.Resident_Abroad_Flag",
  f"Blank or X. With X the pensioner resides abroad and the health contribution is zero for periods after December 2015 (Decreto 780 de 2016 art. 2.1.3.17); the health rate (campo 48) is then 0%, the EPS code (campo 32) may be blank, the health days (campo 37) may be zero and the date of filing abroad (campo 59) is mandatory. A pensioner with a family group in Colombia does not use X and pays the full health percentage. Source: {AT3} §2.2.1 campo 18, pp. 27-28; §2.2.2.2, pp. 40-46; §2.2.2.5, p. 49; ch. 4 §9, p. 113.",
  opts="X / blank", vt="Flag")
F("R2", 19, "Department of residence code", "Código del departamento de residencia", 2, 251, 252, "A", "C",
  "MANDATORY; blank where campo 18 = X. A pensioner abroad who contributes voluntarily to a CCF carries the department of the CCF coverage.", "11", "Pensioner.Residence_Department_Code",
  f"DIVIPOLA (DANE) department code, validated by the information operator. Source: {AT3} §2.2.1 campo 19, p. 28.", vt="Code")
F("R2", 20, "Municipality of residence code", "Código del municipio de residencia", 3, 253, 255, "A", "C",
  "MANDATORY; blank where campo 18 = X. A pensioner abroad who contributes voluntarily to a CCF carries the municipality of the CCF coverage.", "001", "Pensioner.Residence_Municipality_Code",
  f"DIVIPOLA (DANE) municipality code, validated by the information operator. Source: {AT3} §2.2.1 campo 20, pp. 28-29.", vt="Code")
F("R2", 21, "Pension paid abroad", "Pensionado cuyo pago se sitúa en el exterior", 1, 256, 256, "A", "Y", None, "N", "Pensioner.Payment_Abroad_Flag",
  f"S where the payment of the pension is made abroad; N where it is not. Source: {AT3} §2.2.1 campo 21, p. 29.", opts="S / N", vt="Flag")
sec("═══ -- change events (campos 22 to 29) -- ═══")
F("R2", 22, "ING: entry", "ING: Ingreso", 1, 257, 257, "A", "C", "Marked only in the period of entry; blank otherwise.", "", "Pensioner.Entry_Event",
  f"Blank, X or C. X: the payer enters the pensioner in all subsystems it reports, and the days may be fewer than 30 according to the day of entry. C: entry to the family compensation fund only. The entry date (campo 55) may accompany it. Source: {AT3} §2.2.1 campo 22, p. 29; §2.2.2.6, pp. 49-50; ch. 4 §5 table 8, p. 106.",
  opts="X / C / blank", vt="Flag")
F("R2", 23, "RET: withdrawal", "RET: Retiro", 1, 258, 258, "A", "C", "Marked only in the period of withdrawal; blank otherwise.", "", "Pensioner.Withdrawal_Event",
  f"Blank, X, P or C. X: the payer withdraws the pensioner from all subsystems it reports, and the days may be fewer than 30. P: withdrawal from the pension subsystem only, for pension types 4, 7, 11 and 14. C: withdrawal from the family compensation fund only. The withdrawal date (campo 56) may accompany it. Source: {AT3} §2.2.1 campo 23, p. 29; §2.2.2.7, p. 50.",
  opts="X / P / C / blank", vt="Flag")
F("R2", 24, "TDE: transfer from another EPS or EOC", "TDE: Traslado desde otra EPS o EOC", 1, 259, 259, "A", "N", "Must be blank.", "", "Constant blank",
  f"Must be reported blank. Source: {AT3} §2.2.1 campo 24, p. 29.", pay="N", rel="N", vt="Flag", cat="X")
F("R2", 25, "TAE: transfer to another EPS", "TAE: Traslado a otra EPS", 1, 260, 260, "A", "N", "Must be blank.", "", "Constant blank",
  f"Must be reported blank. Source: {AT3} §2.2.1 campo 25, p. 29.", pay="N", rel="N", vt="Flag", cat="X")
F("R2", 26, "TDP: transfer from another pension administradora", "TDP: Traslado desde otra Administradora de Pensiones", 1, 261, 261, "A", "N", "Must be blank.", "", "Constant blank",
  f"Must be reported blank. Source: {AT3} §2.2.1 campo 26, p. 29.", pay="N", rel="N", vt="Flag", cat="X")
F("R2", 27, "TAP: transfer to another pension administradora", "TAP: Traslado a otra Administradora de Pensiones", 1, 262, 262, "A", "N", "Must be blank.", "", "Constant blank",
  f"Must be reported blank. Source: {AT3} §2.2.1 campo 27, p. 29.", pay="N", rel="N", vt="Flag", cat="X")
F("R2", 28, "VSP: permanent variation of the mesada", "VSP: Variación permanente de la mesada pensional", 1, 263, 263, "A", "C",
  "X in the period in which the mesada increases; never together with SUS.", "", "Pension.Permanent_Variation_Event",
  f"Blank or X. Reported when the mesada increases, except where the suspension event (campo 29) is reported. The start date (campo 57) may accompany it. Source: {AT3} §2.2.1 campo 28, p. 29; §2.2.2.8, p. 50.",
  opts="X / blank", vt="Flag")
F("R2", 29, "SUS: suspension", "SUS: Suspensión", 1, 264, 264, "A", "C", "S only where the mesada is suspended; blank otherwise.", "", "Pension.Suspension_Event",
  f"S where a recognised pension is suspended because the beneficiary did not prove in time the condition to keep receiving it, or for any other legal ground (for example a court decision on the right between several spouses or partners, or student children who did not prove their condition). With S the days reported are the days of suspension in the month, and the mesada (campo 58) and the IBC (campo 39) are zero. Dates in campos 60 and 61 may accompany it. Source: {AT3} §2.2.1 campo 29, pp. 29-30; §2.2.2.9, pp. 50-51.",
  opts="S / blank", vt="Flag")
sec("═══ -- administradoras (campos 30 to 34) -- ═══")
F("R2", 30, "Pension administradora or ACCAI code", "Código de la Administradora de Pensiones o de la ACCAI a la cual se encuentra vinculado el pensionado cotizante", 6, 265, 270, "A", "C",
  "MANDATORY for pension types 4, 7, 11, 14 and 22; OPTIONAL for 12, 20 and 21 where the pensioner contributes voluntarily to pensions; may be blank with SUS.", "", "Pensioner.Pension_Fund_Code",
  f"A valid administradora code. Where the pensioner appears with S in campo 5 of the file 'INFORMACIÓN DE AFILIACIÓN A PENSIONES', the information operator reports the administradora of campo 3 of that file; with N and an IBC above 2.3 SMLMV, the ACCAI of campo 6 of that file (or the payer supplies it where the file has none); with N and an IBC up to 2.3 SMLMV, Colpensiones as administradora of the Componente de Prima Media. Source: {AT3} §2.2.1 campo 30, pp. 30-31.",
  vt="Code")
F("R2", 31, "Destination pension administradora code", "Código de la Administradora de Pensiones a la cual se traslada el pensionado cotizante", 6, 271, 276, "A", "N", "Must be blank.", "", "Constant blank",
  f"Must be reported blank. Source: {AT3} §2.2.1 campo 31, p. 31.", pay="N", rel="N", vt="Code", cat="X")
F("R2", 32, "EPS or EOC code", "Código EPS o EOC a la cual pertenece el afiliado", 6, 277, 282, "A", "C",
  "MANDATORY; blank only where campo 18 = X.", "EPS001", "Pensioner.EPS_Code",
  f"A valid EPS code supplied by the payer. In R and L planillas for a retroactive amount paid for the first time, and in A and C records of a V planilla, the code is MIN001 (ADRES), except for pensioners of the special health regime. For a pensioner type 9 record it is the EPS of the additional UPC beneficiary. Source: {AT3} §2.2.1 campo 32, p. 31; §2.1.2.2, pp. 17-19; §2.2.2.4, p. 49; ch. 4 §8, p. 109.",
  vt="Code")
F("R2", 33, "Destination EPS or EOC code", "Código EPS o EOC a la cual se traslada el afiliado", 6, 283, 288, "A", "N", "Must be blank.", "", "Constant blank",
  f"Must be reported blank. Source: {AT3} §2.2.1 campo 33, p. 32.", pay="N", rel="N", vt="Code", cat="X")
F("R2", 34, "CCF code", "Código CCF a la que pertenece el pensionado afiliado", 6, 289, 294, "A", "C",
  "Populated only where the pensioner contributes to a family compensation fund (optional subsystem, R6).", "", "Pensioner.CCF_Code",
  f"A valid family compensation fund code. Contribution to a CCF is optional ('O') for every pension type in R6. Source: {AT3} §2.2.1 campo 34, p. 32; ch. 4 §6 table 9, pp. 107-108.",
  vt="Code")
sec("═══ -- days contributed (campos 35 to 38) -- ═══")
F("R2", 35, "Days contributed to pension", "Número de días cotizados a pensión", 2, 295, 296, "N", "C",
  "MANDATORY for pension types 4, 7, 11 and 14; OPTIONAL for 12, 20 and 21 where the pensioner contributes voluntarily to pensions.", "00", "Pension.Pension_Days",
  f"Values 0 to 30. The days of a pensioner obliged to contribute total 30 whether the month has 28, 30 or 31 days; fewer than 30 only with an entry or withdrawal event. Zero only where the pensioner is not obliged to contribute to pensions. Source: {AT3} §2.2.1 campo 35, p. 32; §2.2.2.10, p. 51.",
  vt="Days")
F("R2", 36, "Days contributed to the Fondo de Solidaridad Pensional", "Número días cotizados al Fondo de Solidaridad Pensional", 2, 297, 298, "N", "C",
  "MANDATORY where the mesada exceeds 10 SMLMV.", "00", "Pension.FSP_Days",
  f"Values 0 to 30; 30 for a full month whatever its calendar length, fewer only with an entry or withdrawal event. Zero only where the pensioner is not obliged to contribute to the Fondo de Solidaridad Pensional under Ley 797 de 2003. Source: {AT3} §2.2.1 campo 36, p. 32; §2.2.2.11, p. 51.",
  vt="Days")
F("R2", 37, "Days contributed to health", "Número de días cotizados a salud", 2, 299, 300, "N", "Y", None, "30", "Pension.Health_Days",
  f"Mandatory, values 0 to 30; 30 for a full month whatever its calendar length. Fewer than 30 requires an entry or withdrawal event. Where campo 50 (additional UPC) is above zero the value is 30. Zero only where campo 18 = X. Source: {AT3} §2.2.1 campo 37, p. 32; §2.2.2.12, pp. 51-52.",
  vt="Days")
F("R2", 38, "Days contributed to the family compensation fund", "Número de días cotizados a Cajas de Compensación", 2, 301, 302, "N", "C",
  "MANDATORY where campo 34 (CCF code) is populated.", "00", "Pension.CCF_Days",
  f"Values 0 to 30, supplied by the payer. Source: {AT3} §2.2.1 campo 38, p. 33.", vt="Days")
sec("═══ -- contribution base (campo 39) -- ═══")
F("R2", 39, "Contribution base (IBC)", "Ingreso Base de Cotización", 9, 303, 311, "N", "Y", None, "003500000",
  "MIN(Pension.Monthly_Amount, 25 x SMLMV); Pension.Monthly_Amount fed by WT 62154 'Monthly Retired Pension-6798'",
  f"Mandatory. The value of the mesada (Decreto 780 de 2016 art. 2.2.1.1.2.1: 'Para los pensionados las cotizaciones se calcularán con base en la mesada pensional'). Where the mesada exceeds 25 SMLMV the field carries 25 SMLMV. It is the base of the health contribution, and of the pension contribution for pension types 4, 7, 11 and 14. Minimum by pension type: at least 1 SMLMV for types 1, 8, 9, 10, 12, 13, 15 and 22; may be below 1 SMLMV for types 2 to 7, 11, 14, 16, 20 and 21. Zero for a pensioner type 9 record and for a suspended mesada (campo 29 = S). Source: {AT3} §2.2.1 campo 39, p. 33; §2.2.2.13, p. 52; §2.2.2.9, p. 51; ch. 4 §7, pp. 108-109.",
  rnd=RND_IBC, vt="Amount")
sec("═══ -- pension settlement (campos 40 to 44) -- ═══")
F("R2", 40, "Pension contribution rate", "Tarifa de aportes a pensión", 7, 312, 318, "N", "C",
  "MANDATORY for pension types 4, 7, 11, 14 and 22; OPTIONAL for 12, 20 and 21 where the pensioner contributes voluntarily.", "0.00000", "Mercans.Pensioner_Pension_Rate",
  f"The rate legally in force for the period paid. Zero only where the pensioner is not obliged to contribute to pensions (R6: pension contribution X for types 4, 7, 11, 14 and 22, O for 12, 20 and 21, not permitted for the other types). Source: {AT3} §2.2.1 campo 40, p. 33; §2.2.2.15, p. 52; ch. 4 §6 table 9, pp. 107-108.",
  rnd=RND_RATE, vt="Rate", cat="S", fmt="N(7) - rate; decimal layout per the operator's file-format configuration")
F("R2", 41, "Compulsory pension contribution", "Cotización obligatoria a pensiones", 9, 319, 327, "N", "C",
  "MANDATORY for pension types 4, 7, 11, 14 and 22; OPTIONAL for 12, 20 and 21 where the pensioner contributes voluntarily.", "000000000", "Pension.Pension_Contribution",
  f"Campo 40 x campo 39. From the pension contribution period of July 2025 the information operator distributes this amount between the Componente de Prima Media and the Componente Complementario de Ahorro Individual (Ley 2381 de 2024) before payment; the payer reports the whole contribution here. Source: {AT3} §2.2.1 campo 41, p. 33; §2.2.2.16, pp. 53-59.",
  rnd=RND_100, vt="Amount")
F("R2", 42, "Voluntary contribution to the compulsory pension fund", "Cotización voluntaria del afiliado al Fondo de Pensiones Obligatoria", 9, 328, 336, "N", "N",
  "Optional; individual-savings regime only, pension types 4, 7, 11, 14 and 22 (optional for 12, 20, 21); only where the pensioner is S in campo 5 of 'INFORMACIÓN DE AFILIACIÓN A PENSIONES'.", "000000000", "Pension.Voluntary_Pension_Contribution",
  f"Zero in the Régimen de Prima Media con Prestación Definida. Source: {AT3} §2.2.1 campo 42, pp. 33-34; §2.2.2.17, p. 59.",
  pay="N", rnd=RND_100, vt="Amount", cat="X")
F("R2", 43, "Total contribution", "Total cotización", 9, 337, 345, "N", "Y", "Calculated by the system.", "000000000", "Sum of T2R2-041 and T2R2-042",
  f"Calculated by the system: the sum of campos 41 and 42. Source: {AT3} §2.2.1 campo 43, p. 34.", rnd=RND_100, vt="Amount", cat="S")
F("R2", 44, "Value not withheld for voluntary contributions", "Valor no retenido por aportes voluntarios", 9, 346, 354, "N", "N",
  "Optional for pension types 4, 7, 11 and 14; zero in the Régimen de Prima Media.", "000000000", "Pension.Voluntary_Not_Withheld",
  f"The difference between the withholding that would have applied without the voluntary contributions to the individual-savings regime and the withholding actually made. Source: {AT3} §2.2.1 campo 44, p. 34; §2.2.2.18, p. 59.",
  pay="N", rnd=RND_100, vt="Amount", cat="X")
sec("═══ -- Fondo de Solidaridad Pensional (campos 45 to 47) -- ═══")
F("R2", 45, "FSP contribution - solidarity subaccount", "Aportes a Fondo de solidaridad pensional - Subcuenta de solidaridad", 10, 355, 364, "N", "C",
  "Applies only to pension types 4, 7, 11, 14 and 22 where campo 63 >= 4 SMLMV (12, 20, 21 where the pensioner contributes voluntarily and campo 63 > 4 SMLMV); zero for every other pension type.", "0000000000", "Calculated by the information operator",
  f"Liquidated by the information operator: campo 58 x 0.5% to the solidarity subaccount (Ley 100 de 1993 art. 27). Several lines of the same pensioner and pension type in one planilla are added to test the 4 SMLMV threshold. Source: {AT3} §2.2.1 campo 45, p. 34; §2.2.2.19, pp. 59-60.",
  pay="N", rnd=RND_100, vt="Amount", cat="S")
F("R2", 46, "FSP contribution - subsistence subaccount (pension contributors)", "Aportes a Fondo de Solidaridad Pensional - Subcuenta de Subsistencia", 10, 365, 374, "N", "C",
  "Same scope as campo 45; zero for every other pension type.", "0000000000", "Calculated by the information operator",
  f"Liquidated by the information operator: campo 58 x 0.5% to the subsistence subaccount, plus, for pensioner contributors with S in campo 5 of 'INFORMACIÓN DE AFILIACIÓN A PENSIONES', 0.2% to 1.0% for an IBC from 16 SMLMV (Ley 797 de 2003 art. 8) or, with N, 1.0% to 2.5% from 4 SMLMV (Ley 2381 de 2024 art. 20). Source: {AT3} §2.2.1 campo 46, pp. 34-35; §2.2.2.20, pp. 60-61.",
  pay="N", rnd=RND_100, vt="Amount", cat="S")
F("R2", 47, "FSP contribution - subsistence subaccount (pensioners above 10 SMLMV)", "Aportes a Fondo de Solidaridad Pensional - Subcuenta de Subsistencia", 7, 375, 381, "N", "C",
  "MANDATORY where campo 63 (total mesada) exceeds 10 SMLMV; zero otherwise.", "0000000",
  "Pension.FSP_Pensioner_Contribution; fed by WT 21643 / 21648 / 21644 (attribute per WT from the WTC)",
  f"Pensioners whose mesada exceeds 10 SMLMV and up to 20 SMLMV contribute 1%, and above 20 SMLMV 2%, to the subsistence subaccount (Ley 797 de 2003 art. 8, Ley 100 de 1993 art. 27). Value = campo 58 x the factor that corresponds to campo 63. Where one beneficiary has several pensions in the same planilla, the factor follows the sum of campo 63 and is applied to each campo 58. Supplied by the payer and recalculated by the information operator; paid under code FSP001 - Fondo de Solidaridad Pensional. Source: {AT3} §2.2.1 campo 47, p. 35; §2.2.2.2, pp. 40-47; §2.2.2.21, pp. 61-62.",
  rnd=RND_100, vt="Amount")
sec("═══ -- health settlement (campos 48 to 50) -- ═══")
F("R2", 48, "Health contribution rate", "Tarifa de aportes a Salud", 7, 382, 388, "N", "Y", None, "0.10000", "Mercans.Pensioner_Health_Rate (band on T2R2-063)",
  f"The rate legally in force for the contribution period paid, selected on the total mesada (campo 63) under Ley 100 de 1993 art. 204 par. 5: periods 2020-2021: 1 SMLMV 8%, more than 1 and up to 2 SMLMV 10%, more than 2 SMLMV 12%; periods 2022-2023: 1 SMLMV 4%, more than 1 and up to 2 SMLMV 10%, more than 2 SMLMV 12%; periods from 2024: 1 SMLMV 4%, more than 1 and up to 3 SMLMV 10%, more than 3 SMLMV 12% (Ley 100 de 1993 art. 204 par. 5 with the inciso added by Ley 2294 de 2023 art. 78; Res. MSPS 1271 de 2023 art. 1 nums. 3 to 5, Anexo Técnico 1). The information operator checks the rate against campo 63 for pension types 1 to 16, 20 and 21; in R, L and V planillas it validates the rate in force for the period reported. Zero where the pensioner resides abroad (campo 18 = X). Source: {AT3} §2.2.1 campo 48, p. 35; §2.1.2.2, p. 20; §2.2.2.22, pp. 62-63; ch. 4 §9, pp. 109-113.",
  opts="-> Field Options: Health rate of pensioners", rnd=RND_RATE, vt="Rate", cat="S",
  fmt="N(7) - rate; decimal layout per the operator's file-format configuration")
F("R2", 49, "Compulsory health contribution", "Cotización obligatoria a salud", 9, 389, 397, "N", "Y", None, "000350000",
  "Pension.Health_Contribution; fed by WT 21645 / 21646 / 21647 (attribute per WT from the WTC)",
  f"Campo 48 x campo 39, rounded UP to the next multiple of 100 (Decreto 780 de 2016 art. 3.2.1.5 num. 2), also where the IBC is below 1 SMLMV. The contribution is borne in full by the pensioner (Ley 100 de 1993 art. 143) and withheld from the mesada by the payer. Source: {AT3} §2.2.1 campo 49, p. 35; §2.2.2.23, p. 63.",
  rnd=RND_100, vt="Amount")
F("R2", 50, "Additional UPC value", "Valor de la UPC adicional", 9, 398, 406, "N", "C",
  "MANDATORY for pensioner type 9; zero in every other case.", "000000000", "Pensioner.UPC_Additional_Value (BDUA file campo 11)",
  f"The value in campo 11 of the file 'información de la Base de Datos Única de Afiliados - BDUA con destino a los operadores de información'. Source: {AT3} §2.2.1 campo 50, p. 35; §2.2.2.24, p. 63.",
  vt="Amount", cat="S")
sec("═══ -- family compensation fund (campos 51 and 52) -- ═══")
F("R2", 51, "CCF contribution rate", "Tarifa de aportes CCF", 7, 407, 413, "N", "C", "MANDATORY where a CCF is reported (campo 34).", "0.00000", "Mercans.Pensioner_CCF_Rate",
  f"The rate legally in force for the period paid, written as a decimal, left-justified and completed with zeros to the right: 2.0% is written 0.02000. Source: {AT3} §2.2.1 campo 51, p. 35; §2.2.2.25, p. 63.",
  rnd=RND_RATE, vt="Rate", cat="S", fmt="N(7) - decimal, left-justified, zeros to the right (2.0% = 0.02000)")
F("R2", 52, "CCF contribution value", "Valor aporte CCF", 9, 414, 422, "N", "C", "MANDATORY where a CCF is reported (campo 34).", "000000000", "Pension.CCF_Contribution (no wage type established)",
  f"Campo 51 x campo 58 (the mesada, uncapped). Source: {AT3} §2.2.1 campo 52, p. 35; §2.2.2.26, p. 63; §2.2.2.27, p. 64.",
  rnd=RND_100, vt="Amount")
sec("═══ -- principal contributor of an additional UPC beneficiary (campos 53 and 54) -- ═══")
F("R2", 53, "Principal contributor document type", "Tipo de documento del cotizante principal", 2, 423, 424, "A", "C", "Reported only in a pensioner type 9 record.", "", "Pensioner.Main_Contributor_Doc_Type",
  f"Values CC, CE, TI, RC, PA, CD, PE (not usable for health periods from September 2023), PT. Source: {AT3} §2.2.1 campo 53, p. 36; §2.2.2.4, p. 49.",
  opts="-> Field Options: Document type of the pensioner", vt="Code")
F("R2", 54, "Principal contributor identification number", "Número de identificación del cotizante principal", 16, 425, 440, "A", "C", "Reported only in a pensioner type 9 record.", "", "Pensioner.Main_Contributor_Doc_Number",
  f"Same character and length rules as campo 8. This validation applies to payments made from 1 October 2026. Source: {AT3} §2.2.1 campo 54, pp. 36-37; ch. 5 §5.32, pp. 132-133.",
  vt="Identifier")
sec("═══ -- change event dates, mesada and corrections (campos 55 to 63) -- ═══")
F("R2", 55, "Entry date", "Fecha de ingreso", 10, 441, 450, "A", "C", "Optional with the ING event (campo 22); blank where the event is not reported.", "", "Pensioner.Entry_Date",
  f"Format AAAA-MM-DD; a valid date within the period being settled. Source: {AT3} §2.2.1 campo 55, p. 37.", vt="Date", fmt="A(10) - date AAAA-MM-DD")
F("R2", 56, "Withdrawal date", "Fecha de retiro", 10, 451, 460, "A", "C", "Optional with the RET event (campo 23); blank where the event is not reported.", "", "Pensioner.Withdrawal_Date",
  f"Format AAAA-MM-DD; a valid date within the period being settled. Source: {AT3} §2.2.1 campo 56, p. 38.", vt="Date", fmt="A(10) - date AAAA-MM-DD")
F("R2", 57, "VSP start date", "Fecha inicio VSP", 10, 461, 470, "A", "C", "Optional with the VSP event (campo 28); blank where the event is not reported.", "", "Pension.Variation_Start_Date",
  f"Format AAAA-MM-DD; a valid date within the period being settled. Source: {AT3} §2.2.1 campo 57, p. 38.", vt="Date", fmt="A(10) - date AAAA-MM-DD")
F("R2", 58, "Mesada value", "Valor de mesada pensional", 9, 471, 479, "N", "Y", None, "003500000",
  "Pension.Monthly_Amount; fed by WT 62154 'Monthly Retired Pension-6798'",
  f"Mandatory. The value of the recognised mesada; it may exceed 25 SMLMV. It is the base of the Fondo de Solidaridad Pensional contributions (campos 45, 46 and, where the pension is not shared, 47) and of the family compensation fund contribution (campo 52). Zero for a pensioner type 9 record and for a suspended mesada. Source: {AT3} §2.2.1 campo 58, p. 38; §2.2.2.27, p. 64; §2.2.2.9, p. 51.",
  rnd=RND_MES, vt="Amount")
F("R2", 59, "Date of filing abroad", "Fecha radicación en el exterior", 10, 480, 489, "A", "C", "MANDATORY where campo 18 = X; otherwise optional.", "", "Pensioner.Foreign_Filing_Date",
  f"Format AAAA-MM-DD. Reported once, when the pensioner has notified the EPS of the end of enrolment because of residence abroad with the family group. Source: {AT3} §2.2.1 campo 59, p. 38.", vt="Date", fmt="A(10) - date AAAA-MM-DD")
F("R2", 60, "Suspension start date", "Fecha inicio de la suspensión", 10, 490, 499, "A", "C", "Optional where campo 29 = S; blank where the event is not reported.", "", "Pension.Suspension_Start_Date",
  f"Format AAAA-MM-DD; a valid date within the period being settled. Source: {AT3} §2.2.1 campo 60, pp. 38-39.", vt="Date", fmt="A(10) - date AAAA-MM-DD")
F("R2", 61, "Suspension end date", "Fecha fin de la suspensión", 10, 500, 509, "A", "C", "Optional where campo 29 = S; blank where the event is not reported.", "", "Pension.Suspension_End_Date",
  f"Format AAAA-MM-DD; a valid date within the period being settled. Source: {AT3} §2.2.1 campo 61, p. 39.", vt="Date", fmt="A(10) - date AAAA-MM-DD")
F("R2", 62, "Corrections", "Correcciones", 1, 510, 510, "A", "C", "Blank in planillas other than reliquidation; A or C in a reliquidation planilla.", "", "Mercans.PILA_Correction_Line_Type",
  f"Blank for planillas other than 'L - Reliquidaciones'. A: the initial record. C: the adjusted record with the final value of the mesada, IBC or rate. In a V planilla each pensioner is reported in A records followed by C records, and the contribution settled is the difference C minus A. Source: {AT3} §2.2.1 campo 62, p. 39; §2.1.2.2, pp. 19-20.",
  opts="A / C / blank", vt="Code")
F("R2", 63, "Total mesada value", "Valor total de la mesada pensional", 9, 511, 519, "N", "Y", None, "003500000",
  "Pension.Total_Monthly_Amount (= Pension.Monthly_Amount, WT 62154, where the pension is not shared)",
  f"Mandatory for all pension types. The sum of the shared mesadas, or of the mesadas received in Colombia and in the other paying country, or of the amounts of all beneficiaries of a survivor or substitution pension. The information operator uses it to select the health rate (Ley 100 de 1993 art. 204 par. 5) and the Fondo de Solidaridad Pensional subsistence rate (Ley 100 de 1993 art. 27) for pension types 1, 2, 3, 4, 5, 6, 7, 8, 10, 11, 13, 14, 16 and 20. For types 1, 8, 10, 13, 16 and 20 not shared, and for types 9, 12, 15 and 21, it equals campo 58. Where fewer than 30 days are reported because of an entry or withdrawal, the operator checks that it is at least the proportion of the SMLMV for the days reported. Source: {AT3} §2.2.1 campo 63, p. 39; §2.2.2.28, p. 64.",
  rnd=RND_MES, vt="Amount")

# ---------------------------------------------------------------- position integrity check
TOTALS = {"A1": 482, "R1": 285, "R2": 519}
COUNTS = {"A1": 27, "R1": 18, "R2": 63}
for rec in TOTALS:
    fl = [d for s, d in FIELDS if d and d["rec"] == rec]
    assert len(fl) == COUNTS[rec], (rec, len(fl))
    p = 1
    for d in fl:
        assert d["start"] == p, (rec, d["campo"], d["start"], p)
        assert d["end"] - d["start"] + 1 == d["L"], (rec, d["campo"])
        p = d["end"] + 1
    assert p - 1 == TOTALS[rec], (rec, p - 1)

# ================================================================ SHEET 1 Version Control
ws = wb.create_sheet("Version Control"); widths_from(ws, "Version Control")
ttl, hdr, dat = st("Version Control", "B8"), st("Version Control", "B12"), st("Version Control", "B13")
for r, v in ((8, "Statutory Report Specification"), (9, "COLOMBIA"),
             (10, "Integrated Contribution Settlement Return of the Pension Payer (PILA Pensionados) - pensioners' contributions")):
    for c in range(2, 7):
        put(ws, r, c, v if c == 2 else None, ttl)
    ws.merge_cells(start_row=r, start_column=2, end_row=r, end_column=6)
for c, v in enumerate(["Version", "Effective Date", "Change Description", "Status", "Updated By"], start=2):
    put(ws, 12, c, v, hdr)
for c, v in enumerate(["1.0", "2026-10-21", "Initial version.", "Approved", "Wallisson Gomes"], start=2):
    put(ws, 13, c, v, dat)

# ================================================================ SHEET 2 Report Matrix
ws = wb.create_sheet("Report Matrix"); widths_from(ws, "Report Matrix")
t1, lab, val = st("Report Matrix", "A1"), st("Report Matrix", "A3"), st("Report Matrix", "B3")
sect, sub, bul = st("Report Matrix", "A22"), st("Report Matrix", "A23"), st("Report Matrix", "A25")
put(ws, 1, 1, "INTEGRATED CONTRIBUTION SETTLEMENT RETURN OF THE PENSION PAYER (PILA PENSIONADOS) — REPORT MATRIX", t1)
ws.row_dimensions[1].height = 25.5
RM = [
    ("Report ID", "CO-PILA-007"),
    ("Report Name (EN)", "Integrated Contribution Settlement Return of the Pension Payer (PILA Pensionados) - pensioners' contributions"),
    ("Report Name (Local)", "Planilla Integrada de Liquidación de Aportes - Aportes a Seguridad Social de Pensionados (Anexo Técnico 3)"),
    ("Document ID", "CO-PILA-007"),
    ("Document Title", "Integrated Contribution Settlement Return of the Pension Payer - Field Specification"),
    ("Country", "Colombia"),
    ("Authority", "Ministry of Health and Social Protection (Res. MSPS 2388 de 2016, Anexo Técnico 3), filed THROUGH A LICENSED PRIVATE INFORMATION OPERATOR"),
    ("Report Type", "Statutory monthly settlement of the social-security contributions of the pensioners whose pension the employer pays directly"),
    ("Tax Type", "Social security contributions withheld from the mesada: health, Fondo de Solidaridad Pensional and, where they apply, pension and family compensation fund (not an income-tax filing)"),
    ("Relationship", "Employer as pension payer type 01 (Empleador) to information operator (never directly to government)"),
    ("Frequency", "Monthly - planilla type P for the monthly contributions; R, L and V for retroactive amounts and reliquidations"),
    ("Submission Deadline", "By the business day that Decreto 780 de 2016 art. 3.2.2.1 assigns to the last two digits of the payer's NIT (15 bands, 00-07 to 94-99); the article applies to all contributors (aportantes)"),
    ("File Format", "Two fixed-width flat files: File Type 1 (general data of the pension payer) and File Type 2 (header record type 1 + one detail record type 2 per pensioner and pension type)"),
    ("File Extension", "Not prescribed by the annex. The file extension is held in the information-operator configuration, as published by the chosen operador."),
    ("Character Encoding", "Not prescribed by the annex. The character encoding is held in the information-operator configuration, as published by the chosen operador."),
    ("Record Types / Sections", "File Type 1 (27 campos, 482 positions); File Type 2 Record Type 1 Encabezado (18 campos, 285 positions); File Type 2 Record Type 2 Liquidación detallada de aportes (63 campos, 519 positions)"),
    ("Version", "v1.0"),
]
r = 3
for a, b in RM:
    put(ws, r, 1, a, lab); put(ws, r, 2, b, val)
    height(ws, r, [(a, 34), (b, 88)]); r += 1
r += 2
put(ws, r, 1, "DETAILED COMPLIANCE NOTES (Colombia-specific)", sect); r += 1
NOTES_RM = [
    ("SUBMISSION CHANNEL", [
        "- Channel: upload of the two fixed-width files (or keying) on the web site of a licensed information operator chosen by the payer. Source: AT3 v15 ch. 1 s.0, p. 7.",
        "- The planilla is self-settled and paid electronically: pension payers with 20 or more pensioners have been bound to the electronic modality since 6 March 2017 (Decreto 780 de 2016 art. 3.2.3.9).",
        "- Prerequisite: the payer must appear in the Ministry of Health file 'INFORMACIÓN PAGADORES DE PENSIONES', placed monthly on each operator's secure FTP; a payer that does not appear requests inclusion from the Subdirección de Pensiones y Otras Prestaciones (AT3 v15 §2.1.2.2, p. 16).",
        "- The payer updates its File Type 1 registration with the operator in July and January, as a precondition for settling the planilla of that month (AT3 v15 §1.1, pp. 11-12).",
    ]),
    ("SCOPE OF THIS REPORT", [
        "- Covers the pensions the employer pays directly as pension payer type 01, pensioner types 5 and 6, and the pensioner type 9 records of their additional UPC beneficiaries (AT3 v15 ch. 4 §1 table 3, pp. 100-101).",
        "- Active employees, including employed pensioners in active service, are reported in the employees' PILA under Anexo Técnico 2 (CO-PILA-003), a different file with a different layout.",
        "- Payments that are not a pension (for example an instalment of a retirement bonus) have no record here: every detail record carries a pension type (campo 9) and a mesada (campo 58).",
    ]),
    ("CONTRIBUTIONS SETTLED", [
        "- Health: borne in full by the pensioner (Ley 100 de 1993 art. 143) on the mesada capped at 25 SMLMV; rate by total mesada and contribution period, from January 2024 4% (1 SMLMV) / 10% (more than 1 and up to 3 SMLMV) / 12% (more than 3 SMLMV), earlier periods as in T2R2-048 (Ley 100 de 1993 art. 204 par. 5; Res. MSPS 1271 de 2023 art. 1).",
        "- Fondo de Solidaridad Pensional, subsistence subaccount: 1% for a total mesada above 10 and up to 20 SMLMV, 2% above 20 SMLMV, on the mesada (AT3 v15 §2.2.2.2 and §2.2.2.21; Ley 797 de 2003 art. 8).",
        "- Pension: only for pension types that contribute (11 and 14 'para compartir', 4, 7, 22; optional 12, 20, 21) per R6 (AT3 v15 ch. 4 §6 table 9, pp. 107-108).",
        "- Family compensation fund: optional for every pension type (R6, 'O').",
        "- No occupational risk, SENA or ICBF in this file.",
    ]),
    ("RELATED FILINGS / CROSS-REFERENCES", [
        "- The pensions paid by the employer and the deductions withheld from them are also reported in the electronic payroll (CO-DIAN-001): Res. DIAN 000227 de 2025 art. 1.5.3.2.3 includes 'pagos a los pensionados a cargo del empleador'.",
        "- Totals records types 3 to 7 (pension, FSP subsistence, health, CCF and total payable) and the output files to the administradoras are generated by the information operator, not by the payer (AT3 v15 ch. 2-3, pp. 65-98).",
    ]),
]
for title, lines in NOTES_RM:
    put(ws, r, 1, title, sub); r += 1
    for ln in lines:
        put(ws, r, 1, ln, bul); ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2); height(ws, r, [(ln, 122)]); r += 1

# ================================================================ SHEET 3 Payroll Scope Summary
ws = wb.create_sheet("Payroll Scope Summary"); widths_from(ws, "Payroll Scope Summary")
t1, pur = st("Payroll Scope Summary", "A1"), st("Payroll Scope Summary", "A2")
hd, grp = st("Payroll Scope Summary", "A4"), st("Payroll Scope Summary", "A5")
ca, cb, cc = st("Payroll Scope Summary", "A6"), st("Payroll Scope Summary", "B6"), st("Payroll Scope Summary", "C6")
put(ws, 1, 1, "PAYROLL SCOPE SUMMARY - INTEGRATED CONTRIBUTION SETTLEMENT RETURN OF THE PENSION PAYER (PILA PENSIONADOS)", t1)
ws.row_dimensions[1].height = 25.5
put(ws, 2, 1, "PURPOSE: Tell the developer WHO is reported on the monthly pensioners' planilla of the employer as pension payer, and what happens to a borderline case.", pur)
ws.merge_cells("A3:C3")
for c, v in enumerate(["SCENARIO", "REPORT?", "NOTES / REASONING"], start=1):
    put(ws, 4, c, v, hd)
PSS = [
    ("═══ WHO GETS REPORTED ═══", None, None),
    ("Pensioner whose pension the employer pays directly (pension WT 62154)", "YES",
     "The employer is pension payer type 01 Empleador: 'empresas públicas o privadas o personas naturales que tienen a su cargo el pago de pensiones de sus trabajadores' (AT3 v15 §1.2.4, p. 13). Pensioners are members of the contributory health regime (Ley 100 de 1993 art. 157) and the pension payer self-settles and pays their contributions through PILA (Decreto 780 de 2016 art. 3.2.3.9; Res. MSPS 2388 de 2016 art. 1, Anexo Técnico 3). Pensioner type 5 or 6 (R01)."),
    ("Survivor (sustitución) beneficiary of a pension the employer pays", "YES",
     "Pension types 2, 3 and 4 are valid for payer type 01 (R02, AT3 v15 pp. 102-103). The causante block (campos 11 to 16) becomes mandatory, and campo 63 carries the total of all beneficiaries (AT3 v15 §2.2.2.3, p. 47; §2.2.2.28, p. 64)."),
    ("Additional UPC beneficiary of a pensioner", "YES",
     "Reported as an extra detail record with pensioner type 9, carrying only the fields listed in AT3 v15 §2.2.2.4 (p. 49). EXCLUDED from the header count (T2R1-014) and the header payroll total (T2R1-015)."),
    ("Pensioner resident abroad without a family group in Colombia", "YES",
     "Reported with campo 18 = X: health rate 0% and health contribution zero for periods after December 2015, EPS may be blank, date of filing abroad mandatory (AT3 v15 §2.2.2.5, p. 49; ch. 4 §9, p. 113). The exemption covers the health contribution only; the FSP contribution above 10 SMLMV still applies (AT3 v15 §2.2.2.21, pp. 61-62)."),
    ("Pensioner whose mesada is suspended in the month", "YES",
     "Reported with SUS = S; days = days of suspension, mesada and IBC zero (AT3 v15 §2.2.2.9, p. 51)."),
    ("Active employee, including an employed pensioner in active service", "NO",
     "Reported in the employees' PILA under Anexo Técnico 2 (CO-PILA-003), which is 'Aportes a Seguridad Social de Activos' (Res. MSPS 2388 de 2016 art. 1)."),
    ("Former employee paid a retirement bonus in instalments", "NO",
     "Not a pension: no pension type (campo 9) and no mesada (campo 58) exist for it, and the person is not an active contributor of Anexo Técnico 2. A payment that is in fact a periodic jubilación or convencional pension paid by the employer is reported here, with pension type 10 or 13."),
    ("Pensioner whose pension is paid by a pension fund or administradora", "NO",
     "Reported by that administradora as pension payer type 02 (AT3 v15 §1.2.4, p. 13), not by the employer."),
    ("═══ AMOUNTS AND CONCEPTS REPORTED ═══", None, None),
    ("Mesada (pension WT 62154)", "YES",
     "Campo 58, uncapped, and campo 63 (total mesada). The header payroll total T2R1-015 is the sum of campo 58 (AT3 v15 pp. 15, 38-39)."),
    ("Health contribution of the pensioner (WT 21645 / 21646 / 21647)", "YES",
     "Campo 49 = campo 48 x campo 39. Rate on the total mesada, for contribution periods from January 2024: 1 SMLMV 4%; more than 1 and up to 3 SMLMV 10%; more than 3 SMLMV 12% (Ley 100 de 1993 art. 204 par. 5 with Ley 2294 de 2023 art. 78; Res. MSPS 1271 de 2023 art. 1); earlier periods as in T2R2-048. Base = mesada capped at 25 SMLMV (AT3 v15 §2.2.2.13, p. 52)."),
    ("Fondo de Solidaridad Pensional on mesadas above 10 SMLMV (WT 21643 / 21648 / 21644)", "YES",
     "Campo 47: 1% above 10 and up to 20 SMLMV, 2% above 20 SMLMV, on campo 58 (AT3 v15 §2.2.2.21, pp. 61-62; Ley 797 de 2003 art. 8). Days in campo 36."),
    ("Pension contribution", "VARIES",
     "Only for the pension types R6 marks X (4, 7, 11, 14, 22) or O (12, 20, 21). Jubilación (10) and Convencional (13) carry no pension contribution: campos 30, 35, 40 and 41 stay blank or zero (AT3 v15 ch. 4 §6 table 9, pp. 107-108)."),
    ("Family compensation fund (CCF)", "VARIES",
     "Optional for every pension type (R6 'O'). Where the pensioner contributes, campos 34, 38, 51 and 52 are populated: campo 52 = campo 51 x campo 58 (AT3 v15 §2.2.2.26, p. 63)."),
    ("Income tax withholding on the pension", "NO",
     "This is a contribution settlement, not a tax return. Withholding goes on Form 350."),
    ("═══ TIMING AND RELATIONSHIP ═══", None, None),
    ("Monthly planilla", "YES",
     "Planilla type P is the main planilla for the monthly contributions of the pensioners (AT3 v15 §2.1.2.2, p. 16)."),
    ("Retroactive pension or reliquidation of the mesada", "YES",
     "Separate planillas: R (retroactive), L (reliquidation of periods before January 2020), V (reliquidation from January 2020, A and C records) (AT3 v15 §2.1.2.2, pp. 17-20)."),
    ("Payer not listed in the Ministry file 'INFORMACIÓN PAGADORES DE PENSIONES'", "NO",
     "Planilla types P, R, L and V require the listing. The payer first requests inclusion from the Ministry's Subdirección de Pensiones y Otras Prestaciones (AT3 v15 §2.1.2.2, pp. 16-20)."),
]
r = 5
for a, b, c in PSS:
    if b is None:
        put(ws, r, 1, a, grp); ws.row_dimensions[r].height = 15.0
    else:
        put(ws, r, 1, a, ca); put(ws, r, 2, b, cb); put(ws, r, 3, c, cc)
        height(ws, r, [(a, 52), (c, 116)])
    r += 1

# ================================================================ SHEET 4 Spec
ws = wb.create_sheet(SPEC_SHEET); widths_from(ws, "PILA Spec")
ws.freeze_panes = "B3"
ttl, hdr, secs, dat = st("PILA Spec", "A1"), st("PILA Spec", "A2"), st("PILA Spec", "A3"), st("PILA Spec", "A4")
put(ws, 1, 1, "Integrated Contribution Settlement Return of the Pension Payer (PILA Pensionados) - pensioners' contributions", ttl)
for c in range(2, 22):
    put(ws, 1, c, None, ttl)
ws.merge_cells("A1:U1"); ws.row_dimensions[1].height = 25.5
HEAD = ["Field Name (EN)", "Field Name (Local ES)", "Record Type / Section", "Field Position", "Payroll Field (Y/N)",
        "Mandatory (Y/N/C)", "Conditional Reason", "Position (Start-End)", "Field Length", "Format", "Example",
        "System Mapping", "Field Explanation", "Relevant for Payroll (Y/N)", "Option Values", "Rounding",
        "Negative (Y/N)", "Value Type", "Reporting Frequency", "Query to RA", "RA Comments"]
for c, v in enumerate(HEAD, start=1):
    put(ws, 2, c, v, hdr)
ws.row_dimensions[2].height = 32.25
W = {i + 1: (pw["PILA Spec"].column_dimensions[chr(65 + i)].width or 13) for i in range(21)}
r = 3
for title, d in FIELDS:
    if title:
        put(ws, r, 1, title, secs)
        for c in range(2, 22):
            put(ws, r, c, None, secs)
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=21); ws.row_dimensions[r].height = 15.0
        r += 1; continue
    row = [d["en"], d["local"], d["recname"], d["fid"], d["pay"], d["mand"], d["cond"], d["pos"], str(d["L"]), d["fmt"],
           d["ex"] if d["ex"] != "" else None, d["mapping"], d["expl"], d["rel"], d["opts"], d["rnd"], d["neg"], d["vt"], "Monthly",
           None, None]
    for c, v in enumerate(row, start=1):
        put(ws, r, c, v, dat, fill=CAT[d["cat"]])
    height(ws, r, [(row[i - 1], W[i]) for i in range(1, 20)])
    r += 1

# ================================================================ SHEET 5 File Structure
ws = wb.create_sheet("File Structure"); widths_from(ws, "File Structure")
t1, grp, lab, val = st("File Structure", "A1"), st("File Structure", "A2"), st("File Structure", "A3"), st("File Structure", "B3")
put(ws, 1, 1, "FILE STRUCTURE AND TECHNICAL SPECIFICATIONS", t1); put(ws, 1, 2, None, t1); ws.merge_cells("A1:B1")
ws.row_dimensions[1].height = 25.5


def layout(rec):
    return " | ".join(f"{d['campo']} {d['local']} ({d['start']}-{d['end']})" if d['start'] != d['end'] else f"{d['campo']} {d['local']} ({d['start']})"
                      for s, d in FIELDS if d and d["rec"] == rec)


FS = [
    ("═══ SUBMISSION FORMAT ═══", None),
    ("Governing layout", "Res. MSPS 2388 de 2016, Anexo Técnico 3 'Aportes a Seguridad Social de Pensionados', version 15 dated 24-07-2026 (cited as AT3 v15), incorporating up to Res. MSPS 1529 de 2026."),
    ("Channel", "Upload of the two fixed-width flat files into the web portal of a licensed information operator, or keying on the same portal. The pension payer never transacts directly with the government for these contributions."),
    ("Electronic modality", "Pension payers with 20 or more pensioners self-settle and pay through the electronic planilla (Decreto 780 de 2016 art. 3.2.3.9)."),
    ("Payer listing", "Planilla types P, R, L and V require the payer to appear in the Ministry file 'INFORMACIÓN PAGADORES DE PENSIONES' (AT3 v15 §2.1.2.2, pp. 16-20)."),
    ("Operator upload wrapper", "The two files below follow the official annex position by position. Each operador's upload wrapper and any additional validations it applies are published by the operador and held in the information-operator configuration for the operador the payer has chosen."),
    ("═══ FILE FORMAT ═══", None),
    ("File type", "Two fixed-width flat text files, one record per line: File Type 1 'Datos generales del pagador de pensiones' and File Type 2 'Información planilla integrada' (AT3 v15 ch. 1 s.0, p. 7)."),
    ("Numeric fields (tipo N)", "Right-justified, ZERO-filled to the left (AT3 v15 ch. 1 s.0, p. 7; §2, p. 13)."),
    ("Alphanumeric fields (tipo A)", "Left-justified, SPACE-filled to the right (AT3 v15 ch. 1 s.0, p. 7; §2, p. 13)."),
    ("Record lengths", "File Type 1 = 482 positions. File Type 2 Record Type 1 = 285 positions. File Type 2 Record Type 2 = 519 positions. All three equal the printed totals of AT3 v15 (pp. 11, 16, 39)."),
    ("Rounding", "The contribution base (IBC, campo 39) is rounded UP to the whole peso and each contribution value is rounded UP to the next multiple of 100 (Decreto 780 de 2016 art. 3.2.1.5, text of Decreto 1990 de 2016 art. 1). AT3 v15 requires the rounding rules in force in campos 41, 42, 45, 46, 47, 49 and 52 (pp. 53, 59-63)."),
    ("Rate fields", "Campos 40, 48 and 51 are numeric, seven positions. AT3 v15 prints the decimal layout for campo 51: decimal, left-justified, zeros to the right, 2.0% = 0.02000 (p. 63). The layout of every rate field is held in the file-format configuration as published by the chosen information operator."),
    ("Registration update", "The pension payer updates its File Type 1 data with the information operator in July and January, before settling the planilla of that month; the operator notifies a payer that has not updated at least two months in advance (AT3 v15 pp. 11-12)."),
    ("═══ RECORD STRUCTURE ═══", None),
    ("File Type 1", "Datos generales del pagador de pensiones. 27 campos, positions 1 to 482. ONE record per payer (or per branch where the form of presentation is S). Sent with every payment and reported to the Fondo de Solidaridad Pensional and the administradoras (AT3 v15 §1, p. 7)."),
    ("File Type 2, Record Type 1", "Encabezado. 18 campos, positions 1 to 285. ONE record per planilla, and it is the first record. Identified by record type 01 in positions 1-2 (AT3 v15 §2.1, p. 14)."),
    ("File Type 2, Record Type 2", "Liquidación detallada de aportes. 63 campos, positions 1 to 519. At least ONE record PER PENSIONER, and one record per pension type where a beneficiary holds two types of pension; one extra record per additional UPC beneficiary (pensioner type 9). Identified by record type 02, sequence from 0000001 in positions 3-9 (AT3 v15 §2.2, p. 21; §2.2.2.4, p. 49)."),
    ("Records Type 3 to 7", "TOTALS RECORDS GENERATED BY THE OPERADOR, never sent by the payer: type 3 total pension contributions; type 4 Fondo de Solidaridad Pensional subsistence subaccount; type 5 health; type 6 family compensation funds; type 7 total payable for the period (AT3 v15 ch. 2, pp. 65-72)."),
    ("═══ SECTION LAYOUT - FILE TYPE 1 (27 CAMPOS, 482 POSICIONES) ═══", None),
    ("Positions", layout("A1")),
    ("═══ SECTION LAYOUT - FILE TYPE 2, RECORD TYPE 1 (18 CAMPOS, 285 POSICIONES) ═══", None),
    ("Positions", layout("R1")),
    ("═══ SECTION LAYOUT - FILE TYPE 2, RECORD TYPE 2 (63 CAMPOS, 519 POSICIONES) ═══", None),
    ("Positions", layout("R2")),
    ("═══ INBOUND - OPERATOR SETTLEMENT ═══", None),
    ("What comes back", "The operador assigns the planilla number (T2R1-012) and the payment date (T2R1-013), generates the totals records types 3 to 7, and rejects a planilla that fails the ch. 4 coherence rules (R01 to R6), informing the payer of the error (AT3 v15 ch. 2, pp. 65-72; ch. 4, pp. 99-108)."),
]
r = 2
for a, b in FS:
    if b is None:
        put(ws, r, 1, a, grp); put(ws, r, 2, None, grp)
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=2); ws.row_dimensions[r].height = 15.0
    else:
        put(ws, r, 1, a, lab); put(ws, r, 2, b, val); height(ws, r, [(a, 36), (b, 130)])
    r += 1

# ================================================================ SHEET 6 Field Options
ws = wb.create_sheet("Field Options"); widths_from(ws, "Field Options")
t1, hd, grp = st("Field Options", "A1"), st("Field Options", "A2"), st("Field Options", "A3")
alt, nor = st("Field Options", "A4"), st("Field Options", "A5")
put(ws, 1, 1, "FIELD OPTIONS - CODE TABLES", t1)
for c in range(2, 5):
    put(ws, 1, c, None, t1)
ws.merge_cells("A1:D1"); ws.row_dimensions[1].height = 25.5
for c, v in enumerate(["Code", "Abbrev", "Local (ES)", "EN Description"], start=1):
    put(ws, 2, c, v, hd)
FO = [
    ("DOCUMENT TYPE OF THE PENSION PAYER (A1-002)", [
        ("NI", "NIT", "Número de identificación Tributaria", "Tax identification number; the value for a legal-person payer."),
        ("CC", "CC", "Cédula de ciudadanía", "Citizenship card."), ("CE", "CE", "Cédula de extranjería", "Foreigner's identity card."),
        ("PA", "PA", "Pasaporte", "Passport."), ("CD", "CD", "Carné diplomático", "Diplomatic card.")]),
    ("PENSION PAYER CLASS (A1-007)", [
        ("A", "200+", "Pagador de pensiones con 200 o más pensionados", "200 or more pensioners, counted across all branches or dependencies (AT3 v15 §1.2.1, p. 12)."),
        ("B", "<200", "Pagador de pensiones con menos de 200 pensionados", "Fewer than 200 pensioners, counted across all branches or dependencies."),
        ("I", "IND", "Independiente", "The pension payer is a natural person.")]),
    ("LEGAL NATURE (A1-008)", [
        ("1", "PUB", "Pública", "Legal person of public law."), ("2", "PRIV", "Privada", "Natural or legal person of private law."),
        ("3", "MIX", "Mixta", "Sociedad de economía mixta (Ley 489 de 1998 art. 97).")]),
    ("PERSON TYPE (A1-009)", [
        ("N", "NAT", "Natural", "Natural person responsible for the contributions of its pensioners."),
        ("J", "JUR", "Jurídica", "Legal person responsible for the contributions of its pensioners. Makes A1-004, A1-018 and A1-020 mandatory.")]),
    ("FORM OF PRESENTATION (A1-010)", [
        ("U", "UNI", "Único", "One planilla for the whole payer; branch code and name blank."),
        ("S", "SUC", "Sucursal", "Planilla per branch or dependency; branch code and name mandatory.")]),
    ("DOCUMENT TYPE OF THE LEGAL REPRESENTATIVE (A1-020)", [
        ("CC", "CC", "Cédula de ciudadanía", "Citizenship card."), ("CE", "CE", "Cédula de extranjería", "Foreigner's identity card."),
        ("PA", "PA", "Pasaporte", "Passport."), ("CD", "CD", "Carné diplomático", "Diplomatic card.")]),
    ("PENSION PAYER TYPE (A1-027, T2R1-016)", [
        ("01", "EMP", "Empleador", "Public or private companies or natural persons that pay the pensions of their workers. The type this report covers."),
        ("02", "ADM", "Administrador de pensiones", "Administradoras of the Régimen de Prima Media and of the Régimen de Ahorro Individual. Outside this report."),
        ("03", "PAG", "Pagador de pensiones", "Entities paying pensions recognised by public-sector entities, or foreign pensioners resident in Colombia under international agreements. Outside this report."),
        ("04", "REE", "Pensiones de entidades de los regímenes especial y de excepción", "Entities of the special and exception regimes (Ley 100 de 1993 art. 279; Ley 1643 de 2013). Outside this report.")]),
    ("PENSIONER PLANILLA TYPE (T2R1-018)", [
        ("P", "NORMAL", "Planilla pago normal pagadores de pensiones", "Main planilla for the monthly contributions. Valid with pensioner types 1 to 9 (R04)."),
        ("R", "RETRO", "Planilla pago retroactivo", "Retroactive contributions while the recognition of a pension was outstanding. Valid with pensioner types 1 to 8."),
        ("L", "RELIQ", "Planilla pago reliquidación periodos anteriores a enero de 2020", "Reliquidation of the mesada for periods before January 2020. Valid with pensioner types 1 to 8."),
        ("V", "RELIQ20", "Planilla pago reliquidación enero de 2020 en adelante", "Reliquidation from January 2020, A and C records, one planilla per reliquidated period."),
        ("C", "TERR", "Planilla pago aportes a pensión a cargo de entidades territoriales por un tercero", "Only the entity authorised by the National Government; an employer payer does not use it.")]),
    ("DOCUMENT TYPE OF THE PENSIONER (T2R2-007, T2R2-015, T2R2-053)", [
        ("CC", "CC", "Cédula de ciudadanía", "Citizenship card."), ("CE", "CE", "Cédula de extranjería", "Foreigner's identity card."),
        ("TI", "TI", "Tarjeta de identidad", "Identity card of a minor."), ("RC", "RC", "Registro civil", "Civil registry."),
        ("PA", "PA", "Pasaporte", "Passport."), ("CD", "CD", "Carné diplomático", "Diplomatic card."),
        ("PE", "PEP", "Permiso Especial de Permanencia", "May not be used for health contribution periods from September 2023 onwards."),
        ("PT", "PPT", "Permiso por Protección Temporal", "Temporary protection permit.")]),
    ("PENSION TYPE (T2R2-009) - VALID FOR PAYER TYPE 01 (R02) AND SUBSYSTEMS (R6)", [
        ("2", "SVRC", "Sobrevivencia vitalicia riesgo común", "Life survivor pension, common risk. Health X, pension -, CCF O."),
        ("3", "STRC", "Sobrevivencia temporal riesgo común", "Temporary survivor pension, common risk. Health X, pension -, CCF O."),
        ("4", "STRC30", "Sobrevivencia temporal riesgo común. Cónyuge o compañera (o) menor de 30 años sin hijos", "Temporary survivor pension of a spouse or partner under 30 without children. Health X, pension X, CCF O."),
        ("8", "INVRC", "Invalidez riesgo común", "Disability pension, common risk. Health X, pension -, CCF O."),
        ("10", "JUB", "Jubilación", "Retirement pension recognised by the employer. Health X, pension -, CCF O. Pensioner type 5, 6, 7 or 8 (R03)."),
        ("11", "JUBC", "Jubilación para compartir", "Retirement pension to be shared with the Régimen de Prima Media. Health X, pension X, CCF O."),
        ("12", "SAN", "Sanción", "Pension for the employer's omission to affiliate (Ley 100 de 1993 art. 133). Health X, pension O, CCF O."),
        ("13", "CONV", "Convencional", "Collective-agreement pension recognised up to 31 July 2010. Health X, pension -, CCF O. Pensioner type 5 or 6 (R03)."),
        ("14", "CONVC", "Convencional para compartir", "Collective-agreement pension to be shared. Health X, pension X, CCF O."),
        ("20", "SENT", "Sentencia judicial", "Granted by a court decision; contributions as the decision states. Health X, pension O, CCF O."),
        ("21", "CONC", "Conciliaciones", "Granted by a conciliation. Health X, pension O, CCF O.")]),
    ("PENSIONER TYPE (T2R2-017) - VALID FOR PAYER TYPE 01 (R01)", [
        ("5", "EMP25", "Pensionado por el empleador, con tope máximo de pensión de 25 SMLMV", "Employer pensioner; mesada capped at 25 SMMLV."),
        ("6", "EMPSIN", "Pensionado por el empleador, sin tope máximo de pensión", "Employer pensioner; mesada may exceed 25 SMMLV, health contribution on at most 25 SMLMV."),
        ("9", "UPC", "Beneficiario UPC adicional", "Additional UPC beneficiary record; excluded from the header count and payroll total.")]),
    ("HEALTH RATE OF PENSIONERS (T2R2-048), SELECTED ON T2R2-063", [
        ("1 SMLMV", "4%", "Mesada pensional de 1 SMLMV", "4% for periods from January 2022 (8% in 2020-2021) (Ley 100 de 1993 art. 204 par. 5; Res. MSPS 1271 de 2023 art. 1 nums. 3 to 5)."),
        ("> 1 to 3 SMLMV", "10%", "> 1 SMLMV y hasta 3 SMLMV", "10% for periods from January 2024 (Ley 100 de 1993 art. 204 par. 5 with Ley 2294 de 2023 art. 78; Res. MSPS 1271 de 2023 art. 1 num. 5). For periods 2020-2023 the 10% band is more than 1 and up to 2 SMLMV."),
        ("> 3 SMLMV", "12%", "> 3 SMLMV", "12% for periods from January 2024 (same sources). For periods 2020-2023 the 12% band starts above 2 SMLMV."),
        ("Abroad (campo 18 = X)", "0%", "Pensionado residente en el exterior", "0% for periods after December 2015 (AT3 v15 ch. 4 §9, p. 113).")]),
    ("FONDO DE SOLIDARIDAD PENSIONAL - PENSIONERS (T2R2-047), SELECTED ON T2R2-063", [
        ("<= 10 SMLMV", "0%", "Mesada hasta 10 SMLMV", "No contribution; campo 47 zero."),
        ("> 10 to 20 SMLMV", "1%", "Mesada superior a 10 y hasta 20 SMLMV", "1% of campo 58 (Ley 797 de 2003 art. 8; AT3 v15 §2.2.2.21)."),
        ("> 20 SMLMV", "2%", "Mesada superior a 20 SMLMV", "2% of campo 58.")]),
    ("CHANGE EVENTS (T2R2-022, 023, 028, 029, 062)", [
        ("ING X / C", "ING", "Ingreso", "X entry to all subsystems; C entry to the family compensation fund only."),
        ("RET X / P / C", "RET", "Retiro", "X withdrawal from all subsystems; P from pensions only (types 4, 7, 11, 14); C from the CCF only."),
        ("VSP X", "VSP", "Variación permanente de la mesada pensional", "Permanent increase of the mesada; not with SUS."),
        ("SUS S", "SUS", "Suspensión", "Mesada suspended; mesada and IBC zero, days = days of suspension."),
        ("Correcciones A / C", "CORR", "Correcciones", "A initial record, C adjusted record, in reliquidation planillas.")]),
]
r = 3
for title, rows in FO:
    put(ws, r, 1, f"═══ {title} ═══", grp)
    for c in range(2, 5):
        put(ws, r, c, None, grp)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4); r += 1
    for i, row in enumerate(rows):
        s = alt if i % 2 == 0 else nor
        for c, v in enumerate(row, start=1):
            put(ws, r, c, v, s)
        height(ws, r, [(row[2], 56), (row[3], 78)]); r += 1

# ================================================================ SHEET 7 Population Rules
ws = wb.create_sheet("Population Rules"); widths_from(ws, "Population Rules")
t1, hd, grp, cel = st("Population Rules", "A1"), st("Population Rules", "A2"), st("Population Rules", "A3"), st("Population Rules", "A4")
put(ws, 1, 1, "POPULATION RULES - HOW TO FILL EACH FIELD FROM PAYROLL", t1); ws.row_dimensions[1].height = 25.5
for c, v in enumerate(["Field Name", "Source System", "Population Logic", "Edge Cases"], start=1):
    put(ws, 2, c, v, hd)
PR = [
    ("═══ WHO IS REPORTED ═══", None),
    (("Population of Record Type 2", "Payroll engine",
      "One detail record per pensioner whose pension the employer pays directly (pension WT 62154) and per pension type held, for every month the pension is in force, plus one pensioner type 9 record per additional UPC beneficiary. The employer files as pension payer type 01; the pensioner type is 5 (mesada capped at 25 SMMLV) or 6 (no cap) (AT3 v15 §2.2, p. 21; ch. 4 §1, pp. 99-101).",
      "Employees, including employed pensioners in active service, go in CO-PILA-003. Instalments of a retirement bonus are not a pension and have no record. A suspended mesada is still reported, with SUS = S.")),
    (("Payer listing prerequisite", "Configuration",
      "Before the first planilla P, R, L or V, the payer must appear in the Ministry file 'INFORMACIÓN PAGADORES DE PENSIONES' (monthly, operator FTP). Where it does not, it requests inclusion from the Subdirección de Pensiones y Otras Prestaciones of the Ministry of Health (AT3 v15 §2.1.2.2, pp. 16-20).",
      "The listing is held by the Ministry and the operator; the engine records the payer's listing status as configuration and does not produce the planilla without it.")),
    ("═══ MANDATORY FIELD RULES ═══", None),
    (("Mesada and total mesada (T2R2-058, T2R2-063)", "Payroll engine",
      "Campo 58 = the mesada of the month (WT 62154), uncapped. Campo 63 = the total mesada: equal to campo 58 for a pension that is not shared (types 10 and 13 included); the sum of the shared amounts, of the Colombian and foreign mesadas, or of all survivor beneficiaries otherwise (AT3 v15 §2.2.2.27-28, p. 64).",
      "Campo 63 drives the health band and the FSP factor; campo 58 is the base of the FSP and CCF amounts. Keep the two separate even where they are equal.")),
    (("Contribution base (T2R2-039)", "Payroll engine",
      "IBC = mesada, capped at 25 SMLMV, rounded UP to the whole peso (AT3 v15 §2.2.2.13, p. 52; Decreto 780 de 2016 arts. 2.2.1.1.2.1 and 3.2.1.5).",
      "Minimum 1 SMLMV for pension types 10 and 13 (AT3 v15 ch. 4 §7, pp. 108-109). Zero with SUS = S and for pensioner type 9.")),
    (("Health rate and contribution (T2R2-048, T2R2-049)", "Payroll engine",
      "Select the rate on campo 63 for the contribution period: from January 2024 a mesada of 1 SMLMV 4%; more than 1 and up to 3 SMLMV 10%; more than 3 SMLMV 12% (Ley 100 de 1993 art. 204 par. 5 with Ley 2294 de 2023 art. 78; Res. MSPS 1271 de 2023 art. 1); periods 2020-2023 as in T2R2-048. Campo 49 = campo 48 x campo 39, rounded UP to the next multiple of 100. The amount is the sum of the health WTs 21645 / 21646 / 21647 withheld from the mesada.",
      "Pensioner abroad (campo 18 = X): rate 0% and contribution zero. With fewer than 30 days (ING / RET), the operator checks campo 63 against the proportion of the SMLMV for the days reported (AT3 v15 p. 64).")),
    (("Fondo de Solidaridad Pensional (T2R2-036, T2R2-047)", "Payroll engine",
      "Where campo 63 exceeds 10 SMLMV: campo 47 = campo 58 x 1% (more than 10 and up to 20 SMLMV) or x 2% (more than 20 SMLMV), rounded UP to the next multiple of 100; campo 36 = days (30 for a full month). The amount is the sum of the FSP WTs 21643 / 21648 / 21644 (AT3 v15 §2.2.2.21, pp. 61-62; Ley 797 de 2003 art. 8).",
      "Several pensions of one beneficiary in the same planilla: the factor follows the sum of campo 63 and applies to each campo 58. Campos 45 and 46 stay zero for pension types 10 and 13; the operator liquidates them only for the contributing types.")),
    (("Days (T2R2-035 to T2R2-038)", "Payroll engine",
      "30 for a full month whatever its calendar length; fewer only with ING or RET. Health days mandatory; pension days only for the contributing pension types; FSP days where the mesada exceeds 10 SMLMV; CCF days where a CCF is reported (AT3 v15 §2.2.2.10-12, pp. 51-52).",
      "Health days zero only with campo 18 = X; 30 for a pensioner type 9 record.")),
    ("═══ CRITICAL VALIDATION RULES ═══", None),
    (("Header-to-detail consistency", "Engine (validation)",
      "T2R1-003 to T2R1-009 equal File Type 1 campos 1, 2, 3, 4, 10, 5 and 6; T2R1-016 equals A1-027; T2R1-017 equals A1-025. T2R1-014 = number of pensioners in Record Type 2 excluding pensioner type 9; T2R1-015 = sum of campo 58 excluding pensioner type 9 (AT3 v15 §2.1.1, pp. 14-15).",
      "The type 9 exclusion applies to both the count and the payroll total.")),
    (("Coherence tables R01 to R6", "Engine (validation)",
      "Before submission check: pensioner type against payer type 01 (5, 6, 9); pension type against payer type 01 (2, 3, 4, 8, 10, 11, 12, 13, 14, 20, 21); pension type against pensioner type (R03); planilla type against pensioner type (R04); change events against pension type (table 8); subsystems against pension type (R6) (AT3 v15 ch. 4 §1-6, pp. 99-108).",
      "A combination outside these tables makes the operator reject the whole planilla.")),
    (("Payer and pensioner identities differ", "Engine (validation)",
      "The pensioner's document type and number must differ from the payer's (AT3 v15 p. 39).",
      "The exception for pension type 16 (foreign pensioners under international agreements) does not arise for payer type 01.")),
    (("Change event to date interlock", "Engine (validation)",
      "ING with campo 55, RET with campo 56, VSP with campo 57, SUS with campos 60-61; each date must fall within the period settled. TDE, TAE, TDP, TAP and campos 31 and 33 are always blank (AT3 v15 §2.2.1, pp. 29-39).",
      "VSP and SUS are not reported together.")),
    ("═══ AMOUNT FORMAT RULES ═══", None),
    (("Rounding is UP", "Engine (formatting)",
      "IBC rounded UP to the whole peso; each contribution (campos 41, 42, 45, 46, 47, 49, 52) rounded UP to the next multiple of 100 (Decreto 780 de 2016 art. 3.2.1.5, text of Decreto 1990 de 2016 art. 1).",
      "Reconcile with payroll on unrounded values with a tolerance of 100 pesos per contribution.")),
    (("Numeric and alphanumeric justification", "Engine (formatting)",
      "Numeric fields right-justified and zero-filled; alphanumeric fields left-justified and space-filled (AT3 v15 ch. 1 s.0, p. 7).",
      "An empty numeric field is a run of zeros, an empty alphanumeric field a run of spaces.")),
]
r = 3
for item in PR:
    if item[1] is None:
        put(ws, r, 1, item[0], grp)
        for c in range(2, 5):
            put(ws, r, c, None, grp)
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4); ws.row_dimensions[r].height = 15.0
    else:
        for c, v in enumerate(item, start=1):
            put(ws, r, c, v, cel)
        height(ws, r, [(item[0], 34), (item[2], 96), (item[3], 74)])
    r += 1

# ================================================================ SAMPLE RECORDS (built from the field table)
SAMPLE = {
    "A1": {1: "MERCANS COLOMBIA S.A.S.", 2: "NI", 3: "900123456", 4: "8", 7: "B", 8: "2", 9: "J", 10: "U",
           11: "CALLE 100 7 33", 12: "001", 13: "11", 14: "6920", 15: "6017000000", 16: "0", 17: "nomina@mercans.com",
           18: "79123456", 19: "0", 20: "CC", 21: "MUESTRA", 22: "EJEMPLO", 23: "ANA", 24: "MARIA", 25: "0",
           26: "2026-03", 27: "01"},
    "R1": {1: "01", 2: "1", 3: "MERCANS COLOMBIA S.A.S.", 4: "NI", 5: "900123456", 6: "8", 7: "U", 10: "2026-03",
           11: "2026-03", 12: "0", 14: "2", 15: "25500000", 16: "01", 17: "0", 18: "P"},
}
P1 = {1: "02", 2: "1", 3: "PRUEBA", 4: "EJEMPLO", 5: "PEDRO", 7: "CC", 8: "1000000001", 9: "10", 10: "N", 17: "5",
      19: "11", 20: "001", 21: "N", 32: "EPS001", 35: "0", 36: "0", 37: "30", 38: "0", 39: "3500000",
      40: "0.00000", 41: "0", 42: "0", 43: "0", 44: "0", 45: "0", 46: "0", 47: "0", 48: "0.10000", 49: "350000",
      50: "0", 51: "0.00000", 52: "0", 58: "3500000", 63: "3500000"}
P2 = dict(P1); P2.update({2: "2", 3: "MUESTRA", 4: "PRUEBA", 5: "LUISA", 8: "1000000002", 9: "13", 36: "30", 39: "22000000",
                          47: "220000", 48: "0.12000", 49: "2640000", 58: "22000000", 63: "22000000"})


def rec_line(rec, vals):
    out = ""
    for s, d in FIELDS:
        if not d or d["rec"] != rec:
            continue
        v = vals.get(d["campo"], "")
        if d["typ"] == "N":
            v = v.rjust(d["L"], "0") if v else "0" * d["L"]
        else:
            v = v.ljust(d["L"], " ")
        assert len(v) == d["L"], (rec, d["campo"], v)
        out += v
    return out


L1, L2, L3, L4 = rec_line("A1", SAMPLE["A1"]), rec_line("R1", SAMPLE["R1"]), rec_line("R2", P1), rec_line("R2", P2)
assert (len(L1), len(L2), len(L3), len(L4)) == (482, 285, 519, 519)
# arithmetic of the example
assert int(P1[49]) == int(P1[39]) * 10 // 100 and int(P2[49]) == int(P2[39]) * 12 // 100
assert int(P2[47]) == int(P2[58]) // 100 and int(SAMPLE["R1"][15]) == int(P1[58]) + int(P2[58])
assert SMLMV < int(P1[63]) <= 3 * SMLMV and 10 * SMLMV < int(P2[63]) <= 20 * SMLMV and int(P2[39]) <= 25 * SMLMV

# ================================================================ SHEET 8 Example Analysis
ws = wb.create_sheet("Example Analysis"); widths_from(ws, "Example Analysis")
t1, hd, grp, cel = st("Example Analysis", "A1"), st("Example Analysis", "A2"), st("Example Analysis", "A3"), st("Example Analysis", "A4")
put(ws, 1, 1, "EXAMPLE ANALYSIS - SAMPLE RECORDS PARSED FIELD BY FIELD", t1); ws.row_dimensions[1].height = 25.5
for c, v in enumerate(["Raw Value", "Field Name", "Interpretation", "Notes"], start=1):
    put(ws, 2, c, v, hd)
EA = [
    ("═══ WORKED EXAMPLE - MARCH 2026 PLANILLA P, TWO PENSIONERS ═══", None),
    (("(scenario)", "Pension payer", "MERCANS COLOMBIA S.A.S., NIT 900123456-8, private legal person, pension payer type 01 Empleador, class B (fewer than 200 pensioners), single planilla (U), Bogotá D.C.",
      "Synthetic payer and data. SMLMV 2026 = COP 1,750,905 (Decreto 0159 de 2026); 3 SMLMV = 5,252,715; 10 SMLMV = 17,509,050; 20 SMLMV = 35,018,100; 25 SMLMV = 43,772,625.")),
    (("(scenario)", "Pensioner 1", "Synthetic pensioner, CC 1000000001, pension type 10 Jubilación, pensioner type 5, mesada COP 3,500,000, full month.",
      "Mesada of 2.0 SMLMV: health band more than 1 and up to 3 SMLMV = 10%; no FSP (not above 10 SMLMV).")),
    (("(scenario)", "Pensioner 2", "Synthetic pensioner, CC 1000000002, pension type 13 Convencional, pensioner type 5, mesada COP 22,000,000, full month.",
      "Mesada of 12.6 SMLMV: health 12% (more than 3 SMLMV); FSP 1% (more than 10 and up to 20 SMLMV); IBC below 25 SMLMV, so no cap.")),
    ("═══ FILE TYPE 1 AND HEADER - KEY FIELDS ═══", None),
    (("NI / 900123456 / 8", "A1-002 / A1-003 / A1-004", "Payer document type, number and verification digit.", "The DV is mandatory because A1-009 = J; all three are echoed into T2R1-004 to T2R1-006.")),
    (("B", "A1-007 - Clase de pagador de pensiones", "Fewer than 200 pensioners, counted across all branches.", "A payer with 200 or more pensioners reports A.")),
    (("01", "A1-027 / T2R1-016 - Tipo de pagador de pensiones", "Empleador.", "Restricts the pensioner type to 5, 6, 9 and the pension type to the R02 list.")),
    (("2026-03 / 2026-03", "T2R1-010 / T2R1-011", "Period for pension and CCF; period for health.", "Both supplied by the payer in aaaa-mm format.")),
    (("0000002", "T2R1-014 - Número total de pensionados", "Two pensioners.", "Pensioner type 9 records would be excluded from the count.")),
    (("000025500000", "T2R1-015 - Valor total de la nómina", "3,500,000 + 22,000,000 = 25,500,000.", "Sum of campo 58, excluding pensioner type 9.")),
    (("P", "T2R1-018 - Tipo de planilla pensionado", "Monthly planilla.", "Requires the payer's listing in 'INFORMACIÓN PAGADORES DE PENSIONES'.")),
    ("═══ RECORD TYPE 2 - PENSIONER 2 ═══", None),
    (("13 / N / 5", "T2R2-009 / T2R2-010 / T2R2-017", "Convencional, not shared, employer pensioner with the 25 SMMLV cap.", "R03 allows pension type 13 with pensioner types 5 and 6.")),
    (("00 / 30 / 30 / 00", "T2R2-035 to T2R2-038", "Days: pension 0, FSP 30, health 30, CCF 0.", "No pension contribution for type 13 (R6); FSP days because the mesada exceeds 10 SMLMV; no CCF.")),
    (("022000000", "T2R2-039 - IBC", "Mesada below 25 SMLMV, so IBC = mesada.", "Rounded up to the whole peso (already whole).")),
    (("0220000", "T2R2-047 - FSP subsistencia", "22,000,000 x 1% = 220,000.", "Factor chosen on campo 63 (12.6 SMLMV); fed by the FSP WTs 21643 / 21648 / 21644.")),
    (("0.12000 / 002640000", "T2R2-048 / T2R2-049", "Health 12% x 22,000,000 = 2,640,000.", "Already a multiple of 100; fed by the health WTs 21645 / 21646 / 21647.")),
    (("022000000 / 022000000", "T2R2-058 / T2R2-063", "Mesada and total mesada.", "Equal because the pension is not shared.")),
]
r = 3
for item in EA:
    if item[1] is None:
        put(ws, r, 1, item[0], grp)
        for c in range(2, 5):
            put(ws, r, c, None, grp)
        ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=4); ws.row_dimensions[r].height = 15.0
    else:
        for c, v in enumerate(item, start=1):
            put(ws, r, c, v, cel)
        height(ws, r, [(item[0], 30), (item[1], 36), (item[2], 74), (item[3], 66)])
    r += 1

# ================================================================ SHEET 9 Sample File
ws = wb.create_sheet("Sample File"); widths_from(ws, "Sample File")
t1, mono = st("Sample File", "A1"), st("Sample File", "A3")
put(ws, 1, 1, "SAMPLE FILE - FIXED-WIDTH RECORDS GENERATED FROM THE OFFICIAL POSITION TABLE", t1); ws.row_dimensions[1].height = 25.5


def chunks(line):
    out = []
    for i in range(0, len(line), 110):
        a, b = i + 1, min(i + 110, len(line))
        out.append(f"  pos {a:>4}-{b:<4} |{line[i:i + 110]}|")
    return out


SF = ["PROVENANCE NOTE - READ FIRST", "═══════════",
      "The records below were GENERATED PROGRAMMATICALLY by placing each value at the",
      "position published in Res. MSPS 2388 de 2016 Anexo Técnico 3 (AT3 version 15,",
      "24-07-2026) and applying the annex's justification rules - numeric fields",
      "right-justified and zero-filled, alphanumeric fields left-justified and space-filled.",
      "", "The record lengths are EXACT:",
      "    Archivo Tipo 1                   482 characters (annex total: 482)",
      "    Archivo Tipo 2, Registro Tipo 1  285 characters (annex total: 285)",
      "    Archivo Tipo 2, Registro Tipo 2  519 characters (annex total: 519)",
      "", "All names, identification numbers and amounts are synthetic. EPS001 is an",
      "illustrative administradora code; the real six-position codes are the Ministry",
      "catalogue codes distributed by the chosen operador. Rate fields use the decimal",
      "layout AT3 prints for campo 51 (2.0% = 0.02000); the operator's file-format",
      "configuration governs the layout of each rate field.",
      "", "-" * 79, "1. ARCHIVO TIPO 1 - DATOS GENERALES DEL PAGADOR DE PENSIONES", "-" * 79,
      f"Record (length {len(L1)})"] + chunks(L1) + [
      "", "-" * 79, "2. ARCHIVO TIPO 2, REGISTRO TIPO 1 - ENCABEZADO", "-" * 79, f"Record (length {len(L2)})"] + chunks(L2) + [
      "", "-" * 79, "3. ARCHIVO TIPO 2, REGISTRO TIPO 2 - LIQUIDACION DETALLADA (one per pensioner)", "-" * 79,
      f"Pensioner 1 (length {len(L3)})"] + chunks(L3) + ["", f"Pensioner 2 (length {len(L4)})"] + chunks(L4) + [
      "", "  Reading of the key positions (pensioner 2):",
      "    pos 1-2      02    - tipo de registro (detalle)",
      "    pos 3-9      0000002 - secuencia",
      "    pos 110-111  CC    - tipo documento del pensionado",
      "    pos 128-129  13    - tipo de pensión, convencional",
      "    pos 130      N     - pensión no compartida",
      "    pos 249      5     - pensionado por el empleador con tope de 25 SMMLV",
      "    pos 277-282  EPS001 - EPS del pensionado (illustrative code)",
      "    pos 297-300  30 30 - días FSP y días salud",
      "    pos 303-311  022000000 - IBC = mesada (below 25 SMLMV)",
      "    pos 375-381  0220000 - FSP subcuenta de subsistencia, 1% of the mesada",
      "    pos 382-388  0.12000 - tarifa salud 12% (total mesada above 3 SMLMV)",
      "    pos 389-397  002640000 - cotización salud = IBC x tarifa",
      "    pos 471-479  022000000 - valor de la mesada pensional",
      "    pos 511-519  022000000 - valor total de la mesada pensional",
      "", "-" * 79, "4. TOTALS RECORDS - GENERATED BY THE OPERADOR, NOT BY THE PAYER", "-" * 79,
      "Registro Tipo 3   Total aportes del periodo para pensiones",
      "Registro Tipo 4   Total aportes al Fondo de Solidaridad Pensional - subcuenta de subsistencia",
      "Registro Tipo 5   Total aportes del periodo a salud",
      "Registro Tipo 6   Total aportes del periodo a cajas de compensación familiar",
      "Registro Tipo 7   Registro total a pagar durante el periodo"]
for i, line in enumerate(SF, start=3):
    put(ws, i, 1, line, mono)

wb.save(OUT)
(HERE / "sample-records.txt").write_text("\n".join([L1, L2, L3, L4]) + "\n", encoding="utf-8")
print("saved", OUT)

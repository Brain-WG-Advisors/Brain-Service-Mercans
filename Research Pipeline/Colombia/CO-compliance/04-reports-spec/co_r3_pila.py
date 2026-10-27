# -*- coding: utf-8 -*-
"""
CO-PILA-003 - Planilla Integrada de Liquidacion de Aportes (PILA).
Filing ID: CO-PILA-MONTHLY-003.

EVERY field number, length and byte position in this module comes from the
OFFICIAL source held at
  00-official-sources/pdfs/Anexo-tecnico-2-2016-pila.pdf
(Resolucion MSPS 2388 de 2016, Anexo Tecnico 2, codigo AT2, version 09, fecha
16-09-2019, 213 pages), extracted to _txt/pila_anexo2.txt and
_txt/pila_fields.json and embedded verbatim in co_r3_pila_layout.py.

Record totals reconcile exactly to the annex:
  Archivo Tipo 1                    34 campos, 567 posiciones
  Archivo Tipo 2, Registro Tipo 1   22 campos, 359 posiciones
  Archivo Tipo 2, Registro Tipo 2   97 campos, 686 posiciones

THIS CLOSES scope_manifest known gap CO-GAP-01, which recorded the Registro
Tipo 2 byte positions as not extracted.

C19 code pattern: field identifiers are the annex's own CAMPO numbers, rendered
here as A1-nnn, T2R1-nnn and T2R2-nnn. Pattern ^(A1|T2R1|T2R2)-[0-9]{3}$. The
numeric part is the annex campo number; nothing is derived.
"""

from build_co_specs import (R_PILA, R_NONE, RA)
from co_scope_common import SCOPE_WHO, SCOPE_TIMING
from co_r3_pila_layout import A1, A2R1, A2R2, TOTALS

_LAYOUT = {"A1": {t[0]: t for t in A1},
           "T2R1": {t[0]: t for t in A2R1},
           "T2R2": {t[0]: t for t in A2R2}}

_REC_NAME = {"A1": "Archivo Tipo 1 - Aportante",
             "T2R1": "Archivo Tipo 2, Registro Tipo 1 - Encabezado",
             "T2R2": "Archivo Tipo 2, Registro Tipo 2 - Liquidacion"}


def R(rec, campo, en, mand, cond, ex, mapping, expl, opts="-", rnd=R_NONE,
      vt="Text", freq="Monthly", kind="payroll", q="", neg="N", fmt_extra=""):
    """Build a 21-column Spec row from the official layout plus enrichment.

    fmt_extra (v1.1 alignment patch, CHECK 6) appends a code-prefix pattern to
    column J for coded identifier fields, so the pattern is stated where the
    dev team reads the format and not only in the Sheet 6 note.
    """
    n, lng, ini, fin, tipo, desc = _LAYOUT[rec][campo]
    fmt = ("N(%d) - numeric, right-justified, ZERO-filled to the left" % lng
           if tipo == "N" else
           "A(%d) - alphanumeric, left-justified, SPACE-filled to the right" % lng)
    if fmt_extra:
        fmt = fmt + ". " + fmt_extra
    return [en, desc, _REC_NAME[rec], "%s-%03d" % (rec, campo), "", mand, cond,
            "Pos %d-%d" % (ini, fin), str(lng), fmt, ex, mapping, expl,
            "Y" if kind == "payroll" else "N", opts, rnd, neg, vt, freq, q, RA, kind]


DIVIPOLA = "-> Sheet 6: DIVIPOLA (DANE)"

FIELDS = [
    "ARCHIVO TIPO 1 - DATOS GENERALES DEL APORTANTE (34 campos, 567 posiciones)",
    R("A1", 1, "Employer name or corporate name", "Y", "", "MERCANS COLOMBIA S.A.S.",
      "Company.Legal_Name",
      "Registered name of the contributing employer. Supplied by the aportante and echoed into "
      "Archivo Tipo 2 Registro Tipo 1 campo 4, where the annex says expressly 'El registrado en el "
      "campo 1 del archivo tipo 1' - the two must be byte-identical.",
      vt="Text"),
    R("A1", 2, "Employer document type", "Y", "", "NI", "Company.Document_Type",
      "Identity-document type of the employer, from the closed list NI, CC, CE, TI, PA, CD, SC, PE. "
      "For a corporate employer it is always NI (numero de identificacion tributaria). Echoed into "
      "T2R1 campo 5.",
      opts="-> Sheet 6: Tipo documento aportante", vt="Code"),
    R("A1", 3, "Employer identification number", "Y", "", "900123456", "Company.Document_Number",
      "The employer's identification number. The operador de informacion validates that it contains "
      "only A-Z and 0-9. An ALPHANUMERIC number is permitted ONLY for document types PA (pasaporte) "
      "and CD (carne diplomatico); for NI, CC, CE, TI, SC and PE it must be all digits. Echoed into "
      "T2R1 campo 6. Same number as Formulario 350 casilla 5 and nomina electronica NIE033.",
      vt="Identifier"),
    R("A1", 4, "Verification digit", "C",
      "MANDATORY where 'Employer person type' (A1-009) = J (Juridica); for every other case the "
      "field must be ZERO. Bidirectional pair with A1-009.",
      "7", "Company.NIT_DV",
      "DIAN check digit of the employer NIT. The annex requires the operador de informacion to "
      "validate it against the DIAN algorithm. Echoed into T2R1 campo 7.",
      vt="Identifier"),
    R("A1", 5, "Branch or dependency code", "C",
      "MUST BE BLANK where 'Form of presentation' (A1-010) = U (Unico). Populated only where "
      "A1-010 = S (Sucursal). Bidirectional pair with A1-010 and with 'Branch name' (A1-006).",
      "", "Company.Branch_Code",
      "Code of the branch or dependency filing this planilla. Echoed into T2R1 campo 12. A "
      "multi-branch employer files one planilla per branch under S; a single consolidated planilla "
      "uses U and leaves this blank.",
      vt="Code"),
    R("A1", 6, "Branch or dependency name", "C",
      "Populated together with 'Branch or dependency code' (A1-005). The annex directs that where "
      "the branch has no name, the branch CODE is written here instead.",
      "", "Company.Branch_Name",
      "Name of the branch. Echoed into T2R1 campo 13. Where the branch is unnamed, repeat the code "
      "from A1-005 rather than leaving it blank.",
      vt="Text"),
    R("A1", 7, "Class of contributor", "Y", "", "B", "Company.Aportante_Class",
      "A = 200 or more contributors; B = fewer than 200; C = Mipyme electing the Ley 590 de 2000 "
      "parafiscal discounts; D = beneficiary of the Ley 1429 de 2010 formalisation regime. The "
      "headcount test for A and B counts contributors across ALL branches. For class C the operador "
      "de informacion must verify MONTHLY that the employer appears in the file DIAN sends the "
      "Ministry under Decreto 525 de 2009 art. 6 - so the class cannot simply be asserted.",
      opts="-> Sheet 6: Clase de aportante", vt="Code"),
    R("A1", 8, "Legal nature", "Y", "", "2", "Company.Legal_Nature",
      "1 Publica, 2 Privada, 3 Mixta, 4 Organismos multilaterales, 5 Entidades de derecho publico no "
      "sometidas a la legislacion colombiana. Private-sector corporate payroll is 2.",
      opts="-> Sheet 6: Naturaleza juridica", vt="Code"),
    R("A1", 9, "Employer person type", "Y", "", "J", "Company.Person_Type",
      "N Natural or J Juridica. Where N, the valid document types in A1-002 narrow to CC, CE, TI, "
      "PA, CD, PE and SC - NI is not available to a natural person. Where J, the verification digit "
      "(A1-004) and the whole legal-representative block (A1-018 to A1-024) become mandatory.",
      opts="-> Sheet 6: Tipo persona", vt="Code"),
    R("A1", 10, "Form of presentation", "Y", "", "U", "Company.Presentation_Form",
      "U Unico or S Sucursal. Determines whether the branch code and name (A1-005, A1-006) are "
      "filled or blank. Echoed into T2R1 campo 11.",
      opts="-> Sheet 6: Forma de presentacion", vt="Code"),
    R("A1", 11, "Correspondence address", "Y", "", "CALLE 100 No 7-33 PISO 12", "Company.Address",
      "Postal address of the employer for correspondence from the subsystem administrators.",
      vt="Text"),
    R("A1", 12, "City or municipality code", "Y", "", "001", "Company.City_Code",
      "THREE-digit DANE DIVIPOLA municipality code - note that this is the municipality suffix "
      "ALONE, not the five-digit code used by the nomina electronica. Bogota D.C. is 001 here and "
      "11001 there. Left BLANK where the 'Colombiano en el exterior' flag is marked.",
      opts=DIVIPOLA, vt="Code"),
    R("A1", 13, "Department code", "Y", "", "11", "Company.Department_Code",
      "Two-digit DANE DIVIPOLA department code. Concatenated with A1-012 it reconstructs the "
      "five-digit code used elsewhere: 11 + 001 = 11001, Bogota D.C.",
      opts=DIVIPOLA, vt="Code"),
    R("A1", 14, "DANE economic activity code", "Y", "", "6920", "Company.CIIU_Code",
      "Four-digit economic activity from the CIIU revision 4 adapted for Colombia, issued by DANE "
      "through Resolucion 66 de 2012 or its successor. The SAME classification drives the DIAN "
      "self-withholding rate in Formulario 350 casilla 27; keep one code, consumed twice.",
      opts="-> Sheet 6: CIIU rev. 4 A.C.", vt="Code"),
    R("A1", 15, "Telephone", "Y", "", "6017439999", "Company.Phone",
      "Contact telephone of the employer. Mandatory in the annex even though it plays no part in "
      "the settlement.",
      vt="Text"),
    R("A1", 16, "Fax", "N", "", "", "Company.Fax",
      "Fax number. Optional and, in practice, obsolete - but the ten positions remain reserved in "
      "the record and must be zero-filled if unused, because the field is typed N.",
      vt="Text", kind="na"),
    R("A1", 17, "E-mail address", "Y", "", "nomina@mercans.com", "Company.Email",
      "Employer e-mail. The annex prescribes the validation in detail: the local part may contain "
      "a-z, 0-9, hyphen, underscore, apostrophe and full stop; the separator must be the @ "
      "character; the domain may contain a-z, 0-9 and hyphen, and the hyphen may be neither the "
      "first nor the last character of the domain.",
      vt="Text"),
    R("A1", 18, "Legal representative identification number", "C",
      "MANDATORY where 'Employer person type' (A1-009) = J (Juridica); OPTIONAL where A1-009 = N "
      "(Natural). Bidirectional pair with A1-009 and with the legal-representative block A1-019 to "
      "A1-024.",
      "79123456", "Company.Legal_Rep_ID",
      "Identity number of the legal representative. The operador validates that it contains only "
      "A-Z and 0-9. An alphanumeric value is permitted only for document types PA and CD; for CC "
      "and CE it must be all digits.",
      vt="Identifier"),
    R("A1", 19, "Legal representative verification digit", "Y", "", "0", "Company.Legal_Rep_ID_DV",
      "The annex is explicit and counter-intuitive here: 'Este campo se debera reportar en cero'. "
      "It is ALWAYS zero, whatever the representative's document. Do not compute a check digit.",
      vt="Identifier", kind="const"),
    R("A1", 20, "Legal representative document type", "C",
      "MANDATORY where 'Employer person type' (A1-009) = J; optional where A1-009 = N. "
      "Bidirectional pair with A1-009 and A1-018.",
      "CC", "Company.Legal_Rep_ID_Type",
      "Closed list of only four values: CC Cedula de ciudadania, CE Cedula de extranjeria, "
      "PA Pasaporte, CD Carne diplomatico. Narrower than the employer's own document-type list in "
      "A1-002 - NI, TI, SC and PE are not available for a legal representative.",
      opts="-> Sheet 6: Tipo documento representante legal", vt="Code"),
    R("A1", 21, "Legal representative first surname", "C",
      "MANDATORY where 'Employer person type' (A1-009) = J. Bidirectional pair with A1-009.",
      "GOMEZ", "Company.Legal_Rep_First_Surname",
      "First surname of the legal representative.", vt="Text"),
    R("A1", 22, "Legal representative second surname", "N", "", "RUIZ",
      "Company.Legal_Rep_Second_Surname",
      "Second surname. Supplied by the aportante; not mandatory even for a legal person, which "
      "accommodates a representative with a single surname - unlike the nomina electronica, where "
      "the employee's second surname is use=required (CO-GAP-07).",
      vt="Text"),
    R("A1", 23, "Legal representative first name", "C",
      "MANDATORY where 'Employer person type' (A1-009) = J. Bidirectional pair with A1-009.",
      "ANA", "Company.Legal_Rep_First_Name",
      "First given name of the legal representative.", vt="Text"),
    R("A1", 24, "Legal representative second name", "N", "", "MARIA",
      "Company.Legal_Rep_Second_Name",
      "Second given name. Optional.", vt="Text"),
    R("A1", 25, "Insolvency, restructuring, liquidation or cessation start date", "C",
      "Optional in general, but MANDATORY where 'Type of action' (A1-026) is populated. "
      "Bidirectional pair with A1-026: the annex says 'Es obligatorio cuando se diligencia "
      "informacion en el campo 26 de este archivo'.",
      "", "Company.Insolvency_Start_Date",
      "Date from which the concordato, restructuring, liquidation or cessation of activities takes "
      "effect. Format AAAA-MM-DD. Used where there is no payroll and no payment.",
      vt="Date", kind="system"),
    R("A1", 26, "Type of action", "C",
      "Optional. Where populated, it makes 'Insolvency start date' (A1-025) mandatory and "
      "'Commercial-activity cessation date' (A1-027) required. Bidirectional set with A1-025 and "
      "A1-027.",
      "", "Company.Action_Type",
      "1 Concordato, 2 Reestructuracion, 3 Liquidacion, 4 Cese de actividades.",
      opts="-> Sheet 6: Tipo de accion", vt="Code", kind="system"),
    R("A1", 27, "Date commercial activities ceased", "C",
      "Optional in general; the annex directs that it 'se debe diligenciar cuando se ha reportado "
      "informacion en el campo 26 de este registro'. Bidirectional pair with A1-026.",
      "", "Company.Trading_Cease_Date",
      "Date from which the employer is no longer obliged to make contributions. Format AAAA-MM-DD. "
      "This is the field that stops the obligation - not the mere absence of employees.",
      vt="Date", kind="system"),
    R("A1", 28, "Information operator code", "Y", "", "01", "System.PILA_Operator_Code",
      "Assigned by the system of the licensed operador de informacion, not by the employer. "
      "Colombia's social-security filing is intermediated: THE EMPLOYER NEVER TRANSACTS DIRECTLY "
      "WITH THE GOVERNMENT for contributions.",
      opts="-> Sheet 6: Operadores de informacion", vt="Code", kind="system"),
    R("A1", 29, "Payment period", "Y", "", "2026-03", "PayPeriod.Period_Code",
      "Assigned by the system. Format AAAA-MM, seven positions. The contribution period, not the "
      "payment date.",
      vt="Date", kind="system",
      q="TYPE / FORMAT CONFLICT IN THE OFFICIAL ANNEX, recorded. The layout table types this field "
        "as N (numeric, zero-filled) yet prescribes the format AAAA-MM, which occupies all seven "
        "positions only if it contains a hyphen - a non-numeric character. The equivalent header "
        "fields T2R1-015 and T2R1-016 are typed A for the same format. Confirm with the RA and with "
        "the chosen operador whether A1-029 is written as '2026-03' (hyphenated, as the format "
        "implies) or as '0202603' / '2026003' (some other seven-digit numeric form)."),
    R("A1", 30, "Contributor type", "Y", "", "01", "Company.Aportante_Type",
      "Twelve-value list: 1 Empleador, 2 Independiente, 3 Entidades o universidades publicas de "
      "regimenes especial y de excepcion, 4 Agremiaciones/asociaciones/congregaciones religiosas, "
      "5 Cooperativas y precooperativas de trabajo asociado, 6 Misiones diplomaticas/consulares/"
      "organismos multilaterales, 7 Organizaciones del Programa de Hogares de Bienestar, 8 Pagador "
      "de concejales y ediles, 9 Pagador contrato sindical, 10 Pagador programa de reincorporacion, "
      "11 Pagador parafiscales del Magisterio, 12 Pagador prestacion humanitaria. Private corporate "
      "payroll is 1. Echoed into T2R1 campo 21, where the annex requires equality.",
      opts="-> Sheet 6: Tipo de aportante", vt="Code"),
    R("A1", 31, "Commercial registry date", "C",
      "MANDATORY for an employer benefiting from the Ley 1429 de 2010 formalisation regime - i.e. "
      "where 'Class of contributor' (A1-007) = D or 'Ley 1429 CCF benefit' (A1-034) = S. "
      "Bidirectional set with A1-007, A1-032 and A1-034.",
      "", "Company.Commercial_Registry_Date",
      "Date of the commercial registry of the employer's principal seat. The annex restricts the "
      "admissible range to 29 December 2010 through 31 December 2014 - the Ley 1429 window. A date "
      "outside that range is rejected.",
      vt="Date", kind="system"),
    R("A1", 32, "Department code (registered seat)", "C",
      "MANDATORY for a Ley 1429 de 2010 beneficiary. Bidirectional set with A1-007, A1-031 and "
      "A1-034.",
      "", "Company.Department_Code_Registry",
      "DIVIPOLA department of the employer's principal domicile, as distinct from A1-013 which is "
      "the correspondence department. For most employers the two coincide.",
      opts=DIVIPOLA, vt="Code", kind="system"),
    R("A1", 33, "Employer exonerated from health, SENA and ICBF contributions", "Y", "", "S",
      "Company.Exonerated_Flag",
      "S or N. THE SINGLE MOST CONSEQUENTIAL FLAG IN THE EMPLOYER RECORD. It declares that the "
      "employer is exonerated under ET art. 114-1 from the EMPLOYER health contribution of 8.5%, "
      "from the SENA levy of 2% and from the ICBF levy of 3%, for employees earning less than 10 "
      "SMMLV (COP 17,509,050 in 2026). It does NOT touch pension, occupational risk or the family "
      "compensation fund 4%, none of which is ever exonerated. The per-employee side of the same "
      "test is Registro Tipo 2 campo 76, and the DIAN side is Formulario 350 casilla 27 - configure "
      "the test once and consume it in all three places.",
      opts="-> Sheet 6: Exoneracion art. 114-1", vt="Flag"),
    R("A1", 34, "Employer electing Ley 1429 art. 5 benefits for the family compensation fund",
      "Y", "", "N", "Company.Ley1429_CCF_Flag",
      "S or N. Declares that the employer claims the Ley 1429 de 2010 art. 5 progressive relief on "
      "the 4% family-compensation-fund contribution. Distinct from the art. 114-1 exoneration in "
      "A1-033: the CCF 4% is NEVER exonerated under art. 114-1, so this is the only route to relief "
      "on it. Bidirectional set with A1-007 (class D), A1-031 and A1-032.",
      opts="-> Sheet 6: Ley 1429 de 2010", vt="Flag"),

    "ARCHIVO TIPO 2, REGISTRO TIPO 1 - ENCABEZADO (22 campos, 359 posiciones)",
    R("T2R1", 1, "Record type", "Y", "", "01", "Mercans.PILA_Record_Type",
      "A CONSTANT. Must be 01 for the header record of Archivo Tipo 2. The detail records that "
      "follow carry 02 in the same two positions, which is how a parser distinguishes them.",
      vt="Code", kind="const"),
    R("T2R1", 2, "Planilla modality", "Y", "", "1", "Mercans.PILA_Modality",
      "1 Electronica - the employer keys or uploads the settlement on the operador's web site; "
      "2 Asistida - the employer telephones the operador's call centre and the operador keys it. "
      "The annex adds that where Decreto 780 de 2016 art. 3.2.3.9 par. 2 exceptionally allows "
      "assisted payment, the field must still say ELECTRONICA, and the operador reports those "
      "employers separately to the Ministry through SISPRO structure PUB019EXPE by the fifth "
      "business day of the following month.",
      opts="-> Sheet 6: Modalidad de la planilla", vt="Code", kind="system"),
    R("T2R1", 3, "Sequence", "Y", "", "0001", "System.PILA_Header_Sequence",
      "Header sequence number within the file.", vt="Identifier", kind="system"),
    R("T2R1", 4, "Employer name or corporate name", "Y", "", "MERCANS COLOMBIA S.A.S.",
      "Company.Legal_Name",
      "Must be identical to Archivo Tipo 1 campo 1 - the annex says 'El registrado en el campo 1 "
      "del archivo tipo 1'. Any divergence between the two files is a validation failure at the "
      "operador, not at the Ministry.",
      vt="Text"),
    R("T2R1", 5, "Employer document type", "Y", "", "NI", "Company.Document_Type",
      "Must equal Archivo Tipo 1 campo 2.",
      opts="-> Sheet 6: Tipo documento aportante", vt="Code"),
    R("T2R1", 6, "Employer identification number", "Y", "", "900123456", "Company.Document_Number",
      "Must equal Archivo Tipo 1 campo 3. The LAST TWO DIGITS of this number determine the PILA "
      "filing deadline - the 2nd to 16th business day of the following month - which is a different "
      "rule from Formulario 350, where only the LAST digit matters.",
      vt="Identifier"),
    R("T2R1", 7, "Employer verification digit", "Y", "", "7", "Company.NIT_DV",
      "Must equal Archivo Tipo 1 campo 4.", vt="Identifier"),
    R("T2R1", 8, "Planilla type", "Y", "", "E", "Mercans.PILA_Planilla_Type",
      "Single letter selecting the settlement type. E Planilla empleados is the ordinary monthly "
      "employer planilla. The full list also carries Y (independientes empresas), A (cotizantes con "
      "novedad de ingreso), I (independientes), S (servicio domestico), M (mora), N (correcciones), "
      "H (madres sustitutas), T and F (Sistema General de Participaciones - DESCOPED, public sector "
      "only), J (sentencia judicial), X (empresa liquidada), U (uso UGPP pago por terceros), "
      "K (estudiantes) and O (obligaciones determinadas por la UGPP). Types I and Y are descoped in "
      "scope_manifest - the contribution base for an independent worker is 40% of fees, not salary.",
      opts="-> Sheet 6: Tipo de planilla", vt="Code"),
    R("T2R1", 9, "Associated planilla number", "C",
      "MUST BE BLANK where 'Planilla type' (T2R1-008) is E, A, I, M, S, Y, T, X or K. Populated "
      "where the type is N or F (the period planilla being corrected or completed), U (the judicial "
      "deposit title), J (the planilla of the original payment) or O (the planilla of the payment "
      "that produced the UGPP inexactitud). In all other cases the field is ZERO. Bidirectional "
      "pair with T2R1-008 and with 'Associated planilla payment date' (T2R1-010).",
      "0000000000", "Mercans.PILA_Associated_Planilla",
      "The planilla number this settlement relates back to. It is what turns a correction (N) or a "
      "late payment (M) into an amendment of a specific earlier filing rather than a new one.",
      vt="Identifier", kind="system"),
    R("T2R1", 10, "Associated planilla payment date", "C",
      "MUST BE BLANK where 'Planilla type' (T2R1-008) is E, A, I, M, S, Y, T, X or K. Populated in "
      "the same cases as 'Associated planilla number' (T2R1-009), with which it is a bidirectional "
      "pair.",
      "", "Mercans.PILA_Associated_Planilla_Date",
      "Payment date of the associated planilla, format AAAA-MM-DD. For planilla type U the UGPP "
      "enters the date the judicial deposit was constituted.",
      vt="Date", kind="system"),
    R("T2R1", 11, "Form of presentation", "Y", "", "U", "Company.Presentation_Form",
      "Must equal Archivo Tipo 1 campo 10.",
      opts="-> Sheet 6: Forma de presentacion", vt="Code"),
    R("T2R1", 12, "Branch code", "C",
      "Must equal Archivo Tipo 1 campo 5, and is therefore blank where 'Form of presentation' "
      "(T2R1-011) = U. Bidirectional pair with T2R1-011.",
      "", "Company.Branch_Code",
      "Branch code, echoed from Archivo Tipo 1.", vt="Code"),
    R("T2R1", 13, "Branch name", "C",
      "Must equal Archivo Tipo 1 campo 6; populated together with 'Branch code' (T2R1-012).",
      "", "Company.Branch_Name",
      "Branch name, echoed from Archivo Tipo 1.", vt="Text"),
    R("T2R1", 14, "ARL code", "Y", "", "ARL001", "Company.ARL_Code",
      "Code of the occupational-risk insurer (Administradora de Riesgos Laborales) to which the "
      "EMPLOYER is affiliated. The employer has one ARL; the per-employee ARL in Registro Tipo 2 "
      "campo 77 normally matches it, but the RISK CLASS varies by work centre, not by employer.",
      opts="-> Sheet 6: Administradoras (ARL / EPS / AFP / CCF)", vt="Code", fmt_extra="Prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - THREE alphabetic positions identifying the subsystem followed by THREE numeric positions identifying the administradora. Verified against the PILA anexo, which names FSP001, MIN001 and MIN002 in running prose. The code LIST itself is master data published by the Ministerio de Salud y Proteccion Social; validate the prefix here and the code against the catalogue"),
    R("T2R1", 15, "Payment period for subsystems other than health", "Y", "", "2026-03",
      "PayPeriod.Period_Code",
      "Format AAAA-MM, CALCULATED BY THE OPERADOR, not supplied by the employer. Covers pension, "
      "occupational risk and the parafiscal levies.",
      vt="Date", kind="system"),
    R("T2R1", 16, "Payment period for the health subsystem", "Y", "", "2026-04",
      "PayPeriod.Health_Period_Code",
      "Format AAAA-MM, SUPPLIED BY THE EMPLOYER. COLOMBIA'S MOST-MISSED PILA RULE: health is paid "
      "ONE MONTH IN ADVANCE, so the health period is normally the month AFTER the period in "
      "T2R1-015. A settlement for March salaries carries pension period 2026-03 and health period "
      "2026-04. Getting these equal is the classic first-run defect.",
      vt="Date", kind="system"),
    R("T2R1", 17, "Planilla filing number", "Y", "", "0000123456", "System.PILA_Planilla_Number",
      "Assigned by the operador's system and unique per operador. This is the number the employer "
      "quotes in any later correction, and the number the inbound settlement response returns.",
      vt="Identifier", kind="system"),
    R("T2R1", 18, "Payment date", "Y", "", "2026-04-10", "System.PILA_Payment_Date",
      "Assigned by the system from the effective payment date, format AAAA-MM-DD. Where it falls "
      "after the statutory deadline the operador computes interest on arrears and the planilla "
      "becomes a mora settlement.",
      vt="Date", kind="system"),
    R("T2R1", 19, "Total number of contributors", "Y", "", "00001",
      "COUNT(Registro Tipo 2 records)",
      "Must equal the number of UNIQUE contributors in the Registro Tipo 2 detail, EXCLUDING those "
      "whose 'Tipo cotizante' (T2R2-005) is 40 - Beneficiario UPC Adicional. That exclusion is easy "
      "to miss and produces a header-to-detail mismatch that the operador rejects.",
      vt="Count", kind="system"),
    R("T2R1", 20, "Total payroll value", "Y", "", "000012000000", "SUM(Payroll.Parafiscal_Base)",
      "The annex defines it precisely: 'la sumatoria de los IBC para el pago de los aportes de "
      "PARAFISCALES de la totalidad de los empleados'. It is the PARAFISCAL base - Registro Tipo 2 "
      "campo 95 - NOT the pension or health base. The two differ because the parafiscal base is "
      "uncapped and includes paid rest days (Ley 21 de 1982 art. 17), whereas the contribution "
      "bases are capped at 25 SMMLV. May be zero for a planilla of independent workers.",
      rnd=R_PILA, vt="Amount"),
    R("T2R1", 21, "Contributor type", "Y", "", "01", "Company.Aportante_Type",
      "Mandatory and must be EQUAL to Archivo Tipo 1 campo 30. The annex states the equality "
      "expressly.",
      opts="-> Sheet 6: Tipo de aportante", vt="Code"),
    R("T2R1", 22, "Information operator code", "Y", "", "01", "System.PILA_Operator_Code",
      "Assigned by the operador's system. Same value as Archivo Tipo 1 campo 28.",
      opts="-> Sheet 6: Operadores de informacion", vt="Code", kind="system"),
]


# ---------------------------------------------------------------------------
#  ARCHIVO TIPO 2, REGISTRO TIPO 2 - 97 campos, 686 posiciones
# ---------------------------------------------------------------------------
_NOVEDAD_COND = (
    "Change-event (novedad) flag. Populated only in the month the event occurs, and only for the "
    "employee it affects. The whole novedad block T2R2-015 to T2R2-030 is mutually constraining: "
    "the flag drives which of the date fields T2R2-080 to T2R2-097 become mandatory, and it drives "
    "the day counts in T2R2-036 to T2R2-039.")

FIELDS += [
    "ARCHIVO TIPO 2, REGISTRO TIPO 2 - LIQUIDACION DETALLADA (97 campos, 686 posiciones)",
    "-- IDENTIFICATION OF THE CONTRIBUTOR --",
    R("T2R2", 1, "Record type", "Y", "", "02", "Mercans.PILA_Record_Type",
      "A CONSTANT. Must be 02 for a detail record. Distinguishes it from the 01 header in the same "
      "file.", vt="Code", kind="const"),
    R("T2R2", 2, "Sequence", "Y", "", "00001", "System.PILA_Detail_Sequence",
      "Must start at 00001 and be strictly sequential for the remaining detail records in the file.",
      vt="Identifier", kind="system"),
    R("T2R2", 3, "Contributor document type", "Y", "", "CC", "Employee.Document_Type",
      "Closed list CC, CE, TI, PA, CD, SC, PE, RC. An ALPHANUMERIC identification number is "
      "permitted only for PA and CD; for TI, CC, SC, RC, CE and PE the number must be all digits. "
      "NOTE the divergence from the nomina electronica, which uses NUMERIC codes (13 = CC) rather "
      "than these two-letter codes - the engine must MAP, not copy.",
      opts="-> Sheet 6: Tipo documento cotizante", vt="Code"),
    R("T2R2", 4, "Contributor identification number", "Y", "", "1020304050",
      "Employee.Document_Number",
      "Identity number of the contributor. Join key to the nomina electronica NIE045, to Formulario "
      "220 casilla 25 and to Formato 2276 numeral 2.",
      vt="Identifier"),
    R("T2R2", 5, "Contributor type", "Y", "", "01", "Employee.Worker_Type_Code",
      "The full PILA tipo cotizante list - far longer than the sixteen values the nomina "
      "electronica recognises. Values include 1 Dependiente, 2 Servicio domestico, 3 Independiente, "
      "4 Madre sustituta, 12 and 19 Aprendices, 16, 18, 20 to 23, 30 to 36, 40 Beneficiario UPC "
      "Adicional, 42 to 45, 47, 51 to 63. Codes 3, 16, 20, 32 to 45, 52, 53, 55, 57 and 59 to 63 "
      "have NO nomina electronica equivalent, so a direct copy will fail DIAN validation. Type 40 "
      "is additionally excluded from the header count in T2R1-019.",
      opts="-> Sheet 6: Tipo cotizante (PILA)", vt="Code"),
    R("T2R2", 6, "Contributor sub-type", "Y", "", "00", "Employee.Worker_SubType_Code",
      "Twelve-value list: 0 No aplica, 1 Dependiente pensionado por vejez/jubilacion/invalidez "
      "activo, 2 Independiente pensionado, 3 No obligado a cotizar a pensiones por edad, "
      "4 Requisitos cumplidos para pension, 5 Indemnizacion sustitutiva o devolucion de saldos "
      "reconocida, 6 Regimen exceptuado de pensiones, 9 Pensionado con mesada >= 25 SMLMV, "
      "10 Residente en el exterior afiliado voluntario, 11 and 12 Conductores de taxi. HARD RULE "
      "printed in the annex: where the sub-type is 1, 2, 3, 4, 5, 6, 9 or 12, campo 46 (pension "
      "contribution rate) MUST be 0. Only sub-types 0 and 1 have a nomina electronica equivalent.",
      opts="-> Sheet 6: Subtipo cotizante (PILA)", vt="Code"),
    R("T2R2", 7, "Foreign national not liable to contribute to pensions", "C",
      "Blank or X. Where marked, the ONLY valid document types in 'Contributor document type' "
      "(T2R2-003) are CE, PA, CD, SC and PE. Bidirectional pair with T2R2-003.",
      "", "Employee.Foreign_Not_Pension_Liable_Flag",
      "Marks a foreign employee who proves affiliation to a pension system abroad and elects out of "
      "Colombian pension affiliation under Decreto 1072 de 2015 art. 2.2.1.2.1.4. Health, "
      "occupational risk and the parafiscal levies remain fully payable - only pension is waived.",
      vt="Flag"),
    R("T2R2", 8, "Colombian abroad", "C",
      "Blank or X. Used only where 'Contributor document type' (T2R2-003) is CC or TI. Where "
      "marked, the work-location department and municipality (T2R2-009 and T2R2-010) must be left "
      "BLANK. Bidirectional set with T2R2-003, T2R2-009 and T2R2-010.",
      "", "Employee.Colombian_Abroad_Flag",
      "Marks a Colombian national contributing from abroad. Its practical effect on this record is "
      "to suppress the DIVIPOLA work-location fields, which have no meaning outside Colombia.",
      vt="Flag"),
    R("T2R2", 9, "Work location department code", "C",
      "Left BLANK where 'Colombian abroad' (T2R2-008) is marked, and where 'Contributor type' "
      "(T2R2-005) = 40 (Beneficiario UPC Adicional). Bidirectional set with T2R2-008 and T2R2-005.",
      "11", "Employee.Work_Department_Code",
      "DIVIPOLA department where the work is performed. The operador validates it against the DANE "
      "DIVIPOLA catalogue. Should reconcile to nomina electronica NIE051.",
      opts=DIVIPOLA, vt="Code"),
    R("T2R2", 10, "Work location municipality code", "C",
      "Left BLANK in the same two cases as 'Work location department code' (T2R2-009) - "
      "'Colombian abroad' marked, or contributor type 40. Bidirectional set with T2R2-008 and "
      "T2R2-005.",
      "001", "Employee.Work_Municipality_Code",
      "THREE-digit DIVIPOLA municipality suffix - not the five-digit code used by the nomina "
      "electronica. Concatenate with T2R2-009 to obtain the five-digit form: 11 + 001 = 11001. "
      "Should reconcile to NIE052.",
      opts=DIVIPOLA, vt="Code"),
    R("T2R2", 11, "First surname", "Y", "", "PEREZ", "Employee.First_Surname",
      "First surname of the contributor. Mandatory.", vt="Text"),
    R("T2R2", 12, "Second surname", "N", "", "GOMEZ", "Employee.Second_Surname",
      "Second surname. NOT mandatory here - a material contrast with the nomina electronica, where "
      "SegundoApellido is use=required and a single-surname employee forces a placeholder "
      "(CO-GAP-07). The same employee can therefore be reported correctly in PILA and imperfectly "
      "in the XML.",
      vt="Text"),
    R("T2R2", 13, "First name", "Y", "", "JUAN", "Employee.First_Name",
      "First given name. Mandatory.", vt="Text"),
    R("T2R2", 14, "Second name", "N", "", "CARLOS", "Employee.Other_Names",
      "Second given name. Optional.", vt="Text"),

    "-- CHANGE EVENTS (NOVEDADES), campos 15 to 30 --",
    R("T2R2", 15, "ING - hire", "C",
      _NOVEDAD_COND + " Permitted values are blank, R, X or C. Where marked, 'Hire date' "
      "(T2R2-080) becomes mandatory.",
      "", "Payroll.Novedad_ING",
      "Marks the employee's entry into the contribution system in this period. Drives the "
      "proportional day counts in campos 36 to 39 and pairs with the hire date in campo 80.",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 16, "RET - termination", "C",
      _NOVEDAD_COND + " Permitted values are blank, P, R, X or C. Where marked, 'Termination date' "
      "(T2R2-081) becomes mandatory.",
      "", "Payroll.Novedad_RET",
      "Marks the employee's exit. Pairs with the termination date in campo 81 and reduces the "
      "contributory days in campos 36 to 39.",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 17, "TDE - transfer from another EPS", "C",
      _NOVEDAD_COND + " Blank or X. Pairs with 'EPS to which the member belongs' (T2R2-033).",
      "", "Payroll.Novedad_TDE",
      "Transfer INTO the reported health insurer from another EPS or EOC.",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 18, "TAE - transfer to another EPS", "C",
      _NOVEDAD_COND + " Blank or X. Where marked, 'EPS to which the member transfers' (T2R2-034) "
      "becomes mandatory. Bidirectional pair with T2R2-034.",
      "", "Payroll.Novedad_TAE",
      "Transfer OUT to another health insurer. The destination EPS code goes in campo 34.",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 19, "TDP - transfer from another pension administrator", "C",
      _NOVEDAD_COND + " Blank or X. Pairs with 'Pension fund to which the member belongs' "
      "(T2R2-031).",
      "", "Payroll.Novedad_TDP",
      "Transfer INTO the reported pension administrator.",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 20, "TAP - transfer to another pension administrator", "C",
      _NOVEDAD_COND + " Blank or X. Where marked, 'Pension fund to which the member transfers' "
      "(T2R2-032) becomes mandatory. Bidirectional pair with T2R2-032.",
      "", "Payroll.Novedad_TAP",
      "Transfer OUT to another pension administrator. Colombia permits a regime change every five "
      "years, so this is a recurring event, not an exception.",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 21, "VSP - permanent salary variation", "C",
      _NOVEDAD_COND + " Blank or X. Where marked, 'VSP start date' (T2R2-082) becomes mandatory. "
      "Bidirectional pair with T2R2-082.",
      "", "Payroll.Novedad_VSP",
      "A permanent change in salary taking effect during the period. Distinct from VST (campo 23), "
      "which is transitory. The distinction matters: a permanent variation resets the contribution "
      "base going forward, a transitory one does not.",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 22, "Corrections", "C",
      _NOVEDAD_COND + " Permitted values are blank, A or C. Used with planilla type N in "
      "'Planilla type' (T2R1-008). Bidirectional pair with T2R1-008.",
      "", "Payroll.Novedad_Correccion",
      "A adds a contributor omitted from the original planilla; C corrects a contributor already "
      "reported. Only meaningful on a correction planilla.",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 23, "VST - transitory salary variation", "C",
      _NOVEDAD_COND + " Blank or X.",
      "", "Payroll.Novedad_VST",
      "A one-off variation in the contribution base for this period only - typically a bonus or a "
      "retroactive payment - that does not change the standing salary.",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 24, "SLN - contract suspension or unpaid leave", "C",
      _NOVEDAD_COND + " Permitted values are blank, X or C. Where marked, 'SLN start date' "
      "(T2R2-083) and 'SLN end date' (T2R2-084) become mandatory. Bidirectional set with T2R2-083 "
      "and T2R2-084.",
      "", "Payroll.Novedad_SLN",
      "Temporary suspension of the contract, unpaid leave, or a commission of service. Reduces the "
      "contributory days in campos 36 to 39 and must reconcile to the nomina electronica LicenciaNR "
      "block (NIE136 to NIE138).",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 25, "IGE - temporary incapacity, general illness", "C",
      _NOVEDAD_COND + " Blank or X. Where marked, 'IGE start date' (T2R2-085) and 'IGE end date' "
      "(T2R2-086) become mandatory, and campos 57 and 58 (authorisation number and value) become "
      "relevant. Bidirectional set with T2R2-085, T2R2-086, T2R2-057 and T2R2-058.",
      "", "Payroll.Novedad_IGE",
      "Sick leave for general illness. The employer bears days 1-2 and the EPS funds from day 3. "
      "Maps to nomina electronica Incapacidad with Tipo = 1 (Comun).",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 26, "LMA - maternity or paternity leave", "C",
      _NOVEDAD_COND + " Blank or X. Where marked, 'LMA start date' (T2R2-087) and 'LMA end date' "
      "(T2R2-088) become mandatory, and campos 59 and 60 become relevant. Bidirectional set with "
      "T2R2-087, T2R2-088, T2R2-059 and T2R2-060.",
      "", "Payroll.Novedad_LMA",
      "Maternity or paternity leave, funded by the EPS and advanced by the employer. Maps to the "
      "nomina electronica LicenciaMP block (NIE128 to NIE131).",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 27, "VAC-LR - vacation or paid leave", "C",
      _NOVEDAD_COND + " Permitted values are X (vacaciones), L (licencia remunerada) or blank. "
      "Where marked, 'VAC-LR start date' (T2R2-089) and 'VAC-LR end date' (T2R2-090) become "
      "mandatory. Bidirectional set with T2R2-089 and T2R2-090.",
      "", "Payroll.Novedad_VAC_LR",
      "A THREE-VALUE flag, not a simple X: X means vacation, L means remunerated leave. They map to "
      "two DIFFERENT nomina electronica blocks - VacacionesComunes (NIE109 to NIE112) and LicenciaR "
      "(NIE132 to NIE135) respectively - so the value carries real information and must not be "
      "normalised to X.",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 28, "AVP - voluntary contribution", "C",
      _NOVEDAD_COND + " Blank or X. Where marked, campos 48 and 49 (member and employer voluntary "
      "pension contributions) become relevant. Bidirectional set with T2R2-048 and T2R2-049.",
      "", "Payroll.Novedad_AVP",
      "Signals that a voluntary pension contribution is included in this settlement.",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 29, "VCT - change of work centre", "C",
      _NOVEDAD_COND + " Blank or X. Where marked, 'VCT start date' (T2R2-091) and 'VCT end date' "
      "(T2R2-092) become mandatory, and 'Work centre' (T2R2-062) changes. Bidirectional set with "
      "T2R2-091, T2R2-092 and T2R2-062.",
      "", "Payroll.Novedad_VCT",
      "Change of work centre during the period. It matters because THE OCCUPATIONAL-RISK CLASS "
      "ATTACHES TO THE WORK CENTRE, NOT TO THE EMPLOYER (Decreto 1072 de 2015 art. 2.2.4.2.5.6), so "
      "a move can change the ARL rate mid-period.",
      opts="-> Sheet 6: Novedades", vt="Flag"),
    R("T2R2", 30, "IRL - days of occupational accident or disease incapacity", "C",
      _NOVEDAD_COND + " Zero, or a day count between 01 and 30. Where non-zero, 'IRL start date' "
      "(T2R2-093) and 'IRL end date' (T2R2-094) become mandatory. Bidirectional set with T2R2-093 "
      "and T2R2-094.",
      "00", "Payroll.Novedad_IRL_Days",
      "UNLIKE THE OTHER NOVEDAD FLAGS THIS ONE CARRIES A NUMBER, not an X: it is the count of days "
      "of incapacity arising from an occupational accident or disease, funded by the ARL from day "
      "one at 100%. Maps to nomina electronica Incapacidad with Tipo = 2 or 3.",
      vt="Count"),

    "-- ADMINISTRADORAS (campos 31 to 35) --",
    R("T2R2", 31, "Pension fund of the member", "C",
      "Mandatory in general. Blank is permitted ONLY where 'Contributor type' (T2R2-005) or "
      "'Contributor sub-type' (T2R2-006) is one that is not obliged to contribute to the Sistema "
      "General de Pensiones. Bidirectional set with T2R2-005 and T2R2-006.",
      "AFP001", "Employee.AFP_Code",
      "Code of the pension administrator - either Colpensiones in the average-premium regime or a "
      "private individual-account fund. The employee elects the regime and may change it every five "
      "years.",
      opts="-> Sheet 6: Administradoras (ARL / EPS / AFP / CCF)", vt="Code", fmt_extra="Prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - THREE alphabetic positions identifying the subsystem followed by THREE numeric positions identifying the administradora. Verified against the PILA anexo, which names FSP001, MIN001 and MIN002 in running prose. The code LIST itself is master data published by the Ministerio de Salud y Proteccion Social; validate the prefix here and the code against the catalogue"),
    R("T2R2", 32, "Pension fund to which the member transfers", "C",
      "Mandatory where 'TAP - transfer to another pension administrator' (T2R2-020) is marked; "
      "blank otherwise. Bidirectional pair with T2R2-020.",
      "", "Employee.AFP_Transfer_Code",
      "Destination pension administrator on a regime or fund change.",
      opts="-> Sheet 6: Administradoras (ARL / EPS / AFP / CCF)", vt="Code", fmt_extra="Prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - THREE alphabetic positions identifying the subsystem followed by THREE numeric positions identifying the administradora. Verified against the PILA anexo, which names FSP001, MIN001 and MIN002 in running prose. The code LIST itself is master data published by the Ministerio de Salud y Proteccion Social; validate the prefix here and the code against the catalogue"),
    R("T2R2", 33, "EPS or EOC of the member", "Y", "", "EPS001", "Employee.EPS_Code",
      "Code of the health insurer. Health is the subsystem paid one month in advance, per T2R1-016.",
      opts="-> Sheet 6: Administradoras (ARL / EPS / AFP / CCF)", vt="Code", fmt_extra="Prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - THREE alphabetic positions identifying the subsystem followed by THREE numeric positions identifying the administradora. Verified against the PILA anexo, which names FSP001, MIN001 and MIN002 in running prose. The code LIST itself is master data published by the Ministerio de Salud y Proteccion Social; validate the prefix here and the code against the catalogue"),
    R("T2R2", 34, "EPS or EOC to which the member transfers", "C",
      "Mandatory where 'TAE - transfer to another EPS' (T2R2-018) is marked; blank otherwise. "
      "Bidirectional pair with T2R2-018.",
      "", "Employee.EPS_Transfer_Code",
      "Destination health insurer on a transfer.",
      opts="-> Sheet 6: Administradoras (ARL / EPS / AFP / CCF)", vt="Code", fmt_extra="Prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - THREE alphabetic positions identifying the subsystem followed by THREE numeric positions identifying the administradora. Verified against the PILA anexo, which names FSP001, MIN001 and MIN002 in running prose. The code LIST itself is master data published by the Ministerio de Salud y Proteccion Social; validate the prefix here and the code against the catalogue"),
    R("T2R2", 35, "CCF of the member", "Y", "", "CCF001", "Employee.CCF_Code",
      "Code of the family compensation fund. Organised by department, so a multi-site employer "
      "legitimately reports several CCF codes across its population - the 4% rate does not vary, "
      "only the receiving institution.",
      opts="-> Sheet 6: Administradoras (ARL / EPS / AFP / CCF)", vt="Code", fmt_extra="Prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - THREE alphabetic positions identifying the subsystem followed by THREE numeric positions identifying the administradora. Verified against the PILA anexo, which names FSP001, MIN001 and MIN002 in running prose. The code LIST itself is master data published by the Ministerio de Salud y Proteccion Social; validate the prefix here and the code against the catalogue"),

    "-- CONTRIBUTORY DAYS PER SUBSYSTEM (campos 36 to 39) --",
    R("T2R2", 36, "Days contributed to pension", "Y", "", "30", "Payroll.Pension_Days",
      "Contributory days for the pension subsystem on the 30-day commercial month. EACH SUBSYSTEM "
      "CARRIES ITS OWN DAY COUNT and they legitimately differ - which is precisely why the engine "
      "must compute and store four separate counters rather than one 'days worked'.",
      vt="Count"),
    R("T2R2", 37, "Days contributed to health", "Y", "", "30", "Payroll.Health_Days",
      "Contributory days for health. Diverges from the pension count during unpaid leave, where "
      "health may still be payable under some configurations while pension is not.",
      vt="Count"),
    R("T2R2", 38, "Days contributed to occupational risk", "Y", "", "30", "Payroll.ARL_Days",
      "Contributory days for the occupational-risk subsystem.", vt="Count"),
    R("T2R2", 39, "Days contributed to the family compensation fund", "Y", "", "30",
      "Payroll.CCF_Days",
      "Contributory days for the family compensation fund.", vt="Count"),

    "-- CONTRIBUTION BASES (campos 40 to 45, 95) --",
    R("T2R2", 40, "Basic salary", "Y", "", "000012000000", "Payroll.Contractual_Salary",
      "SCOPE ROUTING (v1.1 alignment patch): the amount is owned by the Wage Type Catalogue, "
      "not the Data Dictionary - the pipeline scope rule routes 'Base Salary / Basic Salary "
      "amounts -> WTC, NOT DD'. The 'Payroll.' prefix marks it as outside DD master data; it "
      "is a standing contract attribute, not a per-run computation. Column E is therefore N "
      "and the Data Dictionary correctly holds no Contractual Salary field. "
      "The employee's basic salary. Distinct from the four IBC fields that follow: the IBC is the "
      "contribution base after non-salary payments, the 40% clamp and the ceiling and floor, "
      "whereas this is the contractual salary itself.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 41, "All-inclusive salary flag", "C",
      "X where the employee is on an all-inclusive salary under CST art. 132 num. 2 (minimum 13 "
      "SMMLV). Where marked, the four IBC fields (T2R2-042 to T2R2-045) must be 70% of the integral "
      "salary. Bidirectional set with T2R2-042 to T2R2-045.",
      "", "Employee.Integral_Salary_Flag",
      "Marks salario integral. The 70% rule is the single most consequential consequence: the "
      "contribution base is 70% of the integral salary, not 100%, because 30% is the statutory "
      "prestacional factor. Maps to nomina electronica SalarioIntegral (NIE056).",
      vt="Flag"),
    R("T2R2", 42, "Pension contribution base (IBC)", "Y", "", "000012000000",
      "Payroll.IBC_Pension",
      "Contribution base for pension. FLOOR 1 SMMLV = COP 1,750,905; CEILING 25 SMMLV = "
      "COP 43,772,625 in 2026. Must reconcile to nomina electronica NIE166 divided by the rate in "
      "T2R2-046, allowing for the different rounding conventions.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 43, "Health contribution base (IBC)", "Y", "", "000012000000", "Payroll.IBC_Health",
      "Contribution base for health. Same floor and ceiling as pension. The four IBC values "
      "legitimately DIFFER from one another once a non-salary payment, a change event or a "
      "subsystem-specific rule enters - do not populate them from one variable.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 44, "Occupational risk contribution base (IBC)", "Y", "", "000012000000",
      "Payroll.IBC_ARL",
      "Contribution base for occupational risk. Same floor and ceiling.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 45, "Family compensation fund contribution base (IBC)", "Y", "", "000012000000",
      "Payroll.IBC_CCF",
      "Contribution base for the family compensation fund. Same floor and ceiling as the other "
      "three, but NOT the same as the parafiscal base in campo 95, which is uncapped.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 95, "Contribution base for parafiscals other than the CCF", "Y", "", "000012000000",
      "Payroll.IBC_Parafiscal",
      "THE FIFTH AND MOST-MISSED BASE. The base for SENA, ICBF, ESAP and MEN. Ley 21 de 1982 "
      "art. 17 defines it differently from the contribution bases: it includes paid rest days and "
      "it is UNCAPPED - the 25-SMMLV ceiling does not apply. Header campo T2R1-020 is the sum of "
      "THIS field across the population, not of campo 45.",
      rnd=R_PILA, vt="Amount"),

    "-- PENSION SETTLEMENT (campos 46 to 53) --",
    R("T2R2", 46, "Pension contribution rate", "Y", "", "0160000", "Mercans.Pension_Total_Rate",
      "TOTAL pension rate - employer 12% plus employee 4% = 16% (Ley 100 de 1993 art. 20 as "
      "substituted by Ley 797 de 2003 art. 7). HARD RULE from the annex: where 'Contributor "
      "sub-type' (T2R2-006) is 1, 2, 3, 4, 5, 6, 9 or 12, THIS FIELD MUST BE 0. A high-risk "
      "employee under Decreto Ley 2090 de 2003 carries an additional employer charge - see "
      "scope_manifest CO-GAP-02, which must be resolved before configuring one.",
      opts="-> Sheet 6: Tarifas 2026", rnd="Rate expressed with implied decimals in 7 positions.",
      vt="Rate", kind="system",
      q="CO-GAP-02: confirm the 2026 high-risk additional pension rate and its base before "
        "configuring any Decreto Ley 2090 de 2003 employee."),
    R("T2R2", 47, "Mandatory pension contribution", "Y", "", "000001920000",
      "Payroll.Pension_Contribution_Total",
      "16% of the pension IBC - the WHOLE contribution, employer and employee together. The nomina "
      "electronica reports only the employee's 4% (NIE166); this field reports 16%. They are not "
      "interchangeable.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 48, "Member's voluntary contribution to the mandatory pension fund", "C",
      "Populated where 'AVP - voluntary contribution' (T2R2-028) is marked. Bidirectional pair with "
      "T2R2-028 and with T2R2-049.",
      "000000000000", "Payroll.Voluntary_Pension_Employee",
      "Voluntary contribution made BY THE EMPLOYEE into the mandatory pension fund.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 49, "Employer's voluntary contribution to the mandatory pension fund", "C",
      "Populated where 'AVP - voluntary contribution' (T2R2-028) is marked. Bidirectional pair with "
      "T2R2-028 and with T2R2-048.",
      "000000000000", "Payroll.Voluntary_Pension_Employer",
      "Voluntary contribution made BY THE EMPLOYER into the employee's mandatory pension fund.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 50, "Total contribution to the general pension system", "Y", "", "000001920000",
      "T2R2-047 + T2R2-048 + T2R2-049",
      "Sum of the mandatory contribution and both voluntary contributions. This is the figure the "
      "pension administrator receives.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 51, "Solidarity pension fund - solidarity sub-account", "C",
      "Payable only where the contribution base is at or above 4 SMMLV (COP 7,003,620 in 2026). "
      "Bidirectional pair with 'Solidarity pension fund - subsistence sub-account' (T2R2-052), "
      "which has a HIGHER 16-SMMLV trigger, and with the pension IBC in T2R2-042.",
      "000000120000", "Payroll.FSP_Solidarity",
      "1% of the contribution base, borne ENTIRELY BY THE EMPLOYEE and additional to the 4% pension. "
      "Reconciles to nomina electronica NIE168.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 52, "Solidarity pension fund - subsistence sub-account", "C",
      "Payable only where the contribution base is at or above 16 SMMLV (COP 28,014,480 in 2026) - "
      "a HIGHER trigger than the solidarity sub-account. Cannot be present unless T2R2-051 is also "
      "present. Bidirectional pair with T2R2-051.",
      "000000000000", "Payroll.FSP_Subsistence",
      "Banded 0.2% to 1.0% by contribution base, employee-borne. Reconciles to nomina electronica "
      "NIE170. Reported SEPARATELY from the solidarity sub-account in both artefacts - never merged.",
      opts="-> Sheet 6: Bandas del fondo de solidaridad pensional", rnd=R_PILA, vt="Amount"),
    R("T2R2", 53, "Value not withheld for voluntary contributions", "C",
      "Populated where a voluntary contribution reduces the amount withheld. Related to T2R2-048 "
      "and T2R2-049.",
      "000000000000", "Payroll.Voluntary_Not_Withheld",
      "Amount of voluntary contribution not withheld from the employee in the period.",
      rnd=R_PILA, vt="Amount"),

    "-- HEALTH SETTLEMENT (campos 54 to 60) --",
    R("T2R2", 54, "Health contribution rate", "Y", "", "0040000", "Mercans.Health_Total_Rate",
      "TOTAL health rate - employer 8.5% plus employee 4% = 12.5%. WHERE THE ART. 114-1 EXONERATION "
      "APPLIES (see T2R2-076) the employer's 8.5% falls away and only the employee's 4% is due, so "
      "the effective rate reported becomes 4%. This is the field where the exoneration becomes "
      "visible in money terms.",
      opts="-> Sheet 6: Tarifas 2026", rnd="Rate expressed with implied decimals in 7 positions.",
      vt="Rate", kind="system"),
    R("T2R2", 55, "Mandatory health contribution", "Y", "", "000000480000",
      "Payroll.Health_Contribution_Total",
      "Health contribution actually due. For an exonerated employee earning under 10 SMMLV this is "
      "the employee's 4% alone; for a non-exonerated employee it is the full 12.5%. Reconciles to "
      "nomina electronica NIE163 for the employee portion.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 56, "Additional UPC value", "C",
      "Populated only for contributor type 40 (Beneficiario UPC Adicional) in 'Contributor type' "
      "(T2R2-005). Bidirectional pair with T2R2-005; note that type 40 is also EXCLUDED from the "
      "header contributor count in T2R1-019.",
      "000000000000", "Payroll.UPC_Additional",
      "Additional capitation-unit premium for a beneficiary in a higher-cost health plan. Not part "
      "of ordinary corporate payroll.",
      rnd=R_PILA, vt="Amount", kind="na"),
    R("T2R2", 57, "General-illness incapacity authorisation number", "C",
      "Populated where 'IGE' (T2R2-025) is marked. Bidirectional set with T2R2-025 and with "
      "'General-illness incapacity value' (T2R2-058).",
      "", "Payroll.IGE_Authorisation",
      "Authorisation number issued by the EPS for the sick-leave benefit. Fifteen alphanumeric "
      "positions. Without it the EPS will not reimburse the employer's advance.",
      vt="Identifier"),
    R("T2R2", 58, "General-illness incapacity value", "C",
      "Populated where 'IGE' (T2R2-025) is marked. Bidirectional pair with T2R2-057.",
      "000000000", "Payroll.IGE_Value",
      "Money value of the general-illness incapacity in the period. The employer ADVANCES it and "
      "recovers from the EPS - see the inbound EPS/ARL determination in the Report Matrix.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 59, "Maternity or paternity leave authorisation number", "C",
      "Populated where 'LMA' (T2R2-026) is marked. Bidirectional set with T2R2-026 and with "
      "'Maternity leave value' (T2R2-060).",
      "", "Payroll.LMA_Authorisation",
      "Authorisation number issued by the EPS for the maternity or paternity benefit.",
      vt="Identifier"),
    R("T2R2", 60, "Maternity leave value", "C",
      "Populated where 'LMA' (T2R2-026) is marked. Bidirectional pair with T2R2-059.",
      "000000000", "Payroll.LMA_Value",
      "Money value of the maternity or paternity leave. Advanced by the employer, funded by the EPS.",
      rnd=R_PILA, vt="Amount"),

    "-- OCCUPATIONAL RISK SETTLEMENT (campos 61 to 63, 77, 78) --",
    R("T2R2", 61, "Occupational risk contribution rate", "Y", "", "000005220",
      "Mercans.ARL_Rate",
      "Rate for the employee's risk class, EMPLOYER-BORNE IN FULL - there is no employee "
      "occupational-risk deduction in Colombia, which is why no nomina electronica element "
      "corresponds to it. Initial rates by class: I 0.522%, II 1.044%, III 2.436%, IV 4.350%, "
      "V 6.960%, within statutory minimum-maximum ranges of 0.348% to 8.7%. THE CLASS ATTACHES TO "
      "THE WORK CENTRE, not to the employer.",
      opts="-> Sheet 6: Clases de riesgo laboral", rnd="Rate with implied decimals.", vt="Rate",
      kind="system"),
    R("T2R2", 62, "Work centre", "C",
      "Populated where the employer has more than one work centre, and mandatory where 'VCT - "
      "change of work centre' (T2R2-029) is marked. Bidirectional set with T2R2-029 and with 'Risk "
      "class' (T2R2-078).",
      "000000001", "Employee.Work_Centre_Code",
      "Identifier of the work centre to which the employee is attached. It determines the "
      "occupational-risk class and therefore the rate: a company with two work centres legitimately "
      "carries two risk classes (Decreto 1072 de 2015 art. 2.2.4.2.5.6). Where a person performs "
      "several occupations they contribute at the HIGHEST class.",
      vt="Code"),
    R("T2R2", 63, "Mandatory occupational risk contribution", "Y", "", "000000062700",
      "Payroll.ARL_Contribution",
      "The occupational-risk premium. Employer cost in full. NOTE the rounding: 0.522% of "
      "12,000,000 is 62,640, which rounds UP to the next multiple of 100 to give 62,700 - a "
      "worked illustration of the PILA convention.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 77, "ARL of the member", "Y", "", "ARL001", "Employee.ARL_Code",
      "Occupational-risk insurer to which the employee is affiliated. Normally equal to the "
      "employer's ARL in T2R1-014.",
      opts="-> Sheet 6: Administradoras (ARL / EPS / AFP / CCF)", vt="Code", fmt_extra="Prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - THREE alphabetic positions identifying the subsystem followed by THREE numeric positions identifying the administradora. Verified against the PILA anexo, which names FSP001, MIN001 and MIN002 in running prose. The code LIST itself is master data published by the Ministerio de Salud y Proteccion Social; validate the prefix here and the code against the catalogue"),
    R("T2R2", 78, "Risk class", "Y", "", "1", "Company.Risk_Class",
      "Class I to V. Bidirectional with 'Work centre' (T2R2-062): the class follows the work centre, "
      "so a VCT event can change it mid-period. Recorded defect in an official document: Decreto "
      "1072 de 2015 art. 2.2.4.3.5 prints the class IV initial rate inconsistently with the "
      "Decreto 1772 de 1994 art. 13 table; use the Decreto 1772 values (0.522, 1.044, 2.436, 4.350, "
      "6.960).",
      opts="-> Sheet 6: Clases de riesgo laboral", vt="Code"),

    "-- PARAFISCAL LEVIES (campos 64 to 73) --",
    R("T2R2", 64, "CCF contribution rate", "Y", "", "0040000", "Mercans.CCF_Rate",
      "4% of the contribution base. NEVER exonerated under ET art. 114-1 - a point that catches "
      "many implementations, which assume the exoneration covers all three parafiscals. The only "
      "relief available on the CCF is the Ley 1429 de 2010 art. 5 regime flagged in A1-034.",
      opts="-> Sheet 6: Tarifas 2026", rnd="Rate with implied decimals.", vt="Rate", kind="system"),
    R("T2R2", 65, "CCF contribution value", "Y", "", "000000480000", "Payroll.CCF_Contribution",
      "4% of the CCF base. Employer cost in full.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 66, "SENA contribution rate", "C",
      "ZERO where the employee is exonerated under ET art. 114-1 - that is, where 'Contributor "
      "exonerated from payment' (T2R2-076) is marked and the employee earns less than 10 SMMLV. "
      "Bidirectional set with T2R2-076 and with A1-033.",
      "0000000", "Mercans.SENA_Rate",
      "2% of the parafiscal base, or 0% where the art. 114-1 exoneration applies.",
      opts="-> Sheet 6: Tarifas 2026", rnd="Rate with implied decimals.", vt="Rate", kind="system"),
    R("T2R2", 67, "SENA contribution value", "C",
      "Zero where the art. 114-1 exoneration applies. Bidirectional pair with T2R2-066 and with "
      "T2R2-076.",
      "000000000000", "Payroll.SENA_Contribution",
      "2% of the parafiscal base in T2R2-095, or nil under the exoneration. Employer cost.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 68, "ICBF contribution rate", "C",
      "ZERO where the art. 114-1 exoneration applies. Bidirectional set with T2R2-076 and A1-033.",
      "0000000", "Mercans.ICBF_Rate",
      "3% of the parafiscal base, or 0% under the exoneration.",
      opts="-> Sheet 6: Tarifas 2026", rnd="Rate with implied decimals.", vt="Rate", kind="system"),
    R("T2R2", 69, "ICBF contribution value", "C",
      "Zero where the art. 114-1 exoneration applies. Bidirectional pair with T2R2-068 and with "
      "T2R2-076.",
      "000000000000", "Payroll.ICBF_Contribution",
      "3% of the parafiscal base in T2R2-095, or nil under the exoneration. Employer cost.",
      rnd=R_PILA, vt="Amount"),
    R("T2R2", 70, "ESAP contribution rate", "C",
      "Applies to PUBLIC-SECTOR employers only. Zero for private-sector corporate payroll.",
      "0000000", "Mercans.ESAP_Rate",
      "0.5% levy for the Escuela Superior de Administracion Publica. Out of scope for private-sector "
      "payroll; the field is still present in the record and must be zero-filled.",
      rnd=R_NONE, vt="Rate", kind="na"),
    R("T2R2", 71, "ESAP contribution value", "C",
      "Public-sector employers only. Zero for private-sector corporate payroll.",
      "000000000000", "Payroll.ESAP_Contribution",
      "ESAP levy value. Zero-filled for the in-scope population.",
      rnd=R_PILA, vt="Amount", kind="na"),
    R("T2R2", 72, "MEN contribution rate", "C",
      "Applies to PUBLIC-SECTOR employers only. Zero for private-sector corporate payroll.",
      "0000000", "Mercans.MEN_Rate",
      "1% levy for the Ministerio de Educacion Nacional (escuelas industriales e institutos "
      "tecnicos). Out of scope for private-sector payroll.",
      rnd=R_NONE, vt="Rate", kind="na"),
    R("T2R2", 73, "MEN contribution value", "C",
      "Public-sector employers only. Zero for private-sector corporate payroll.",
      "000000000000", "Payroll.MEN_Contribution",
      "MEN levy value. Zero-filled for the in-scope population.",
      rnd=R_PILA, vt="Amount", kind="na"),

    "-- PRINCIPAL CONTRIBUTOR AND EXONERATION (campos 74 to 76) --",
    R("T2R2", 74, "Principal contributor document type", "C",
      "Populated only for a dependent beneficiary record - typically contributor type 40. "
      "Bidirectional pair with 'Principal contributor identification number' (T2R2-075) and with "
      "'Contributor type' (T2R2-005).",
      "", "Employee.Main_Contributor_Doc_Type",
      "Document type of the principal contributor to whom this beneficiary attaches.",
      opts="-> Sheet 6: Tipo documento cotizante", vt="Code", kind="na"),
    R("T2R2", 75, "Principal contributor identification number", "C",
      "Populated only for a dependent beneficiary record. Bidirectional pair with T2R2-074.",
      "", "Employee.Main_Contributor_Doc_Number",
      "Identification number of the principal contributor.",
      vt="Identifier", kind="na"),
    R("T2R2", 76, "Contributor exonerated from payment", "C",
      "Marked where THIS EMPLOYEE, in THIS MONTH, earns less than 10 SMMLV (COP 17,509,050 in 2026) "
      "and the employer has declared itself exonerated in Archivo Tipo 1 campo 33. Bidirectional "
      "set with A1-033 and with the SENA and ICBF rate and value fields T2R2-066 to T2R2-069 and "
      "the health rate T2R2-054, all of which must be consistent with it. HARD RULE printed at "
      "annex s.2.1.2.3.39: where 'Health contribution base' (T2R2-043) is at or above 10 SMMLV this "
      "field MUST be N - and likewise where a NATURAL-person employer employs two or more workers "
      "and the health base reaches 10 SMMLV.",
      "S", "Payroll.Exoneration_Flag_Monthly",
      "THE PER-EMPLOYEE, PER-MONTH SIDE of the ET art. 114-1 exoneration (introduced by Ley 1607 de "
      "2012 and confirmed by Ley 1819 de 2016 art. 65). Values are S and N, not X. The "
      "employer-level flag in A1-033 declares eligibility; THIS field applies it to a specific "
      "employee in a specific month. The test is monthly, so an employee who crosses 10 SMMLV "
      "because of a bonus loses the exoneration for that month alone - the engine must evaluate it "
      "every period, never once a year. Where marked S, the employer's health 8.5%, SENA 2% and "
      "ICBF 3% fall away and the health rate in T2R2-054 becomes the EMPLOYEE rate alone (4%); "
      "pension, occupational risk and the CCF 4% remain payable in full.",
      opts="-> Sheet 6: Exoneracion art. 114-1", vt="Flag",
      q="DEFECT IN THE OFFICIAL ANNEX, recorded. Section 2.1.2.3.21 (campo 54) refers to the "
        "exoneration flag as 'el campo 72 Cotizante exonerado de pago de aporte Salud, SENA e ICBF' "
        "of Registro Tipo 2, but campo 72 is 'Tarifa aportes MEN'; the exoneration flag is campo 76, "
        "as section 2.1.2.3.39 itself correctly states. The layout table is authoritative; the "
        "cross-reference in s.2.1.2.3.21 is wrong. Confirm with the RA that no operador has "
        "implemented the erroneous reference."),

    "-- SPECIAL PENSION FLAGS (campos 79, 96) --",
    R("T2R2", 79, "Special pension rate indicator", "C",
      "Populated where a non-standard pension rate applies - notably a high-risk activity under "
      "Decreto Ley 2090 de 2003. Bidirectional pair with 'Pension contribution rate' (T2R2-046).",
      "", "Employee.High_Risk_Pension_Flag",
      "Signals that the pension rate in T2R2-046 departs from the standard 16%. Corresponds to the "
      "nomina electronica AltoRiesgoPension flag (NIE043). See CO-GAP-02 before use.",
      vt="Flag",
      q="CO-GAP-02: the additional high-risk employer pension rate and its base were not confirmed "
        "from a primary 2026 source. Verify before configuring any high-risk employee."),
    R("T2R2", 96, "Hours worked", "C",
      "Populated for part-time contributors - notably contributor type 51 (Trabajador de tiempo "
      "parcial). Bidirectional pair with 'Contributor type' (T2R2-005).",
      "000", "Payroll.Hours_Worked",
      "Hours worked in the period, used for the partial-time contribution regime where the base is "
      "not simply floored at 1 SMMLV. Three positions, so a maximum of 999 hours.",
      vt="Count"),

    "-- NOVEDAD DATES (campos 80 to 94, 97) --",
    R("T2R2", 80, "Hire date", "C",
      "Mandatory where 'ING - hire' (T2R2-015) is marked. Bidirectional pair with T2R2-015.",
      "2021-01-11", "Contract.Start_Date",
      "Date of entry, format AAAA-MM-DD. Should equal nomina electronica FechaIngreso (NIE002).",
      vt="Date"),
    R("T2R2", 81, "Termination date", "C",
      "Mandatory where 'RET - termination' (T2R2-016) is marked. Bidirectional pair with T2R2-016.",
      "", "Contract.End_Date",
      "Date of exit, format AAAA-MM-DD. Should equal nomina electronica FechaRetiro (NIE003).",
      vt="Date"),
    R("T2R2", 82, "VSP start date", "C",
      "Mandatory where 'VSP - permanent salary variation' (T2R2-021) is marked. Bidirectional pair "
      "with T2R2-021.",
      "", "Payroll.VSP_Start_Date",
      "Effective date of the permanent salary variation, format AAAA-MM-DD. Only a start date - a "
      "permanent variation has no end.",
      vt="Date"),
    R("T2R2", 83, "SLN start date", "C",
      "Mandatory where 'SLN - suspension or unpaid leave' (T2R2-024) is marked. Bidirectional set "
      "with T2R2-024 and T2R2-084.",
      "", "Payroll.SLN_Start_Date",
      "First day of the suspension or unpaid leave, format AAAA-MM-DD.",
      vt="Date"),
    R("T2R2", 84, "SLN end date", "C",
      "Mandatory where 'SLN' (T2R2-024) is marked. Bidirectional set with T2R2-024 and T2R2-083.",
      "", "Payroll.SLN_End_Date",
      "Last day of the suspension or unpaid leave.", vt="Date"),
    R("T2R2", 85, "IGE start date", "C",
      "Mandatory where 'IGE' (T2R2-025) is marked. Bidirectional set with T2R2-025 and T2R2-086.",
      "", "Payroll.IGE_Start_Date",
      "First day of the general-illness incapacity.", vt="Date"),
    R("T2R2", 86, "IGE end date", "C",
      "Mandatory where 'IGE' (T2R2-025) is marked. Bidirectional set with T2R2-025 and T2R2-085.",
      "", "Payroll.IGE_End_Date",
      "Last day of the general-illness incapacity.", vt="Date"),
    R("T2R2", 87, "LMA start date", "C",
      "Mandatory where 'LMA' (T2R2-026) is marked. Bidirectional set with T2R2-026 and T2R2-088.",
      "", "Payroll.LMA_Start_Date",
      "First day of maternity or paternity leave.", vt="Date"),
    R("T2R2", 88, "LMA end date", "C",
      "Mandatory where 'LMA' (T2R2-026) is marked. Bidirectional set with T2R2-026 and T2R2-087.",
      "", "Payroll.LMA_End_Date",
      "Last day of maternity or paternity leave.", vt="Date"),
    R("T2R2", 89, "VAC-LR start date", "C",
      "Mandatory where 'VAC-LR' (T2R2-027) carries X or L. Bidirectional set with T2R2-027 and "
      "T2R2-090.",
      "", "Payroll.VAC_LR_Start_Date",
      "First day of vacation or remunerated leave.", vt="Date"),
    R("T2R2", 90, "VAC-LR end date", "C",
      "Mandatory where 'VAC-LR' (T2R2-027) carries X or L. Bidirectional set with T2R2-027 and "
      "T2R2-089.",
      "", "Payroll.VAC_LR_End_Date",
      "Last day of vacation or remunerated leave.", vt="Date"),
    R("T2R2", 91, "VCT start date", "C",
      "Mandatory where 'VCT - change of work centre' (T2R2-029) is marked. Bidirectional set with "
      "T2R2-029 and T2R2-092.",
      "", "Payroll.VCT_Start_Date",
      "Date from which the new work centre applies - and therefore from which a different "
      "occupational-risk rate may apply.",
      vt="Date"),
    R("T2R2", 92, "VCT end date", "C",
      "Mandatory where 'VCT' (T2R2-029) is marked. Bidirectional set with T2R2-029 and T2R2-091.",
      "", "Payroll.VCT_End_Date",
      "Date to which the work-centre change applies.", vt="Date"),
    R("T2R2", 93, "IRL start date", "C",
      "Mandatory where 'IRL days' (T2R2-030) is non-zero. Bidirectional set with T2R2-030 and "
      "T2R2-094.",
      "", "Payroll.IRL_Start_Date",
      "First day of incapacity from an occupational accident or disease.", vt="Date"),
    R("T2R2", 94, "IRL end date", "C",
      "Mandatory where 'IRL days' (T2R2-030) is non-zero. Bidirectional set with T2R2-030 and "
      "T2R2-093.",
      "", "Payroll.IRL_End_Date",
      "Last day of occupational incapacity.", vt="Date"),
    R("T2R2", 97, "Date of filing abroad", "C",
      "Populated where 'Colombian abroad' (T2R2-008) is marked. Bidirectional pair with T2R2-008.",
      "", "Payroll.Foreign_Filing_Date",
      "Filing date for a contributor abroad, format AAAA-MM-DD. The last field of the record, "
      "closing at position 686.",
      vt="Date", kind="na"),
]



# ---------------------------------------------------------------------------
#  v1.1 ALIGNMENT PATCH - CHECK 3 / v2.4 C16 BIDIRECTIONAL REFERENCES
#  Where a Mandatory=C field's Conditional Reason names another field on this
#  artefact, that other field must reference it back. The reverse references
#  below were the ones still missing after the first pass of this stage, which
#  had tested only the DD-note -> spec-field-ID direction. Applied as a keyed
#  post-assembly pass so each sentence travels with the row it belongs to and
#  survives a rebuild.
#  A conditional row takes the sentence in its Conditional Reason (column G);
#  an unconditional row takes it in its Explanation (column M), because a
#  Mandatory=Y row must never acquire a conditional reason.
# ---------------------------------------------------------------------------
_C16_REVERSE = {
    'A1-007':
        "Bidirectional set with 'Commercial registry date' (A1-031) and 'Department code (registered "
        "seat)' (A1-032), both of which become mandatory where this field = D, the Ley 1429 de 2010 "
        "formalisation beneficiary.",
    'A1-019':
        "Bidirectional pair with 'Legal representative identification number' (A1-018): the operador "
        "validates this digit against the number carried in A1-018.",
    'A1-024':
        "Part of the bidirectional legal-representative name set governed by 'Legal representative "
        "identification number' (A1-018) and 'Employer person type' (A1-009).",
    'A1-033':
        "Bidirectional set with the Registro Tipo 2 exoneration fields: 'Contributor exonerated from "
        "payment' (T2R2-076), and the SENA and ICBF rate fields (T2R2-066 and T2R2-068) which must be "
        "ZERO wherever the ET art. 114-1 exoneration reaches the individual employee.",
    'T2R1-008':
        "Bidirectional set with 'Associated planilla number' (T2R1-009) and 'Associated planilla "
        "payment date' (T2R1-010), which are populated only where this type is N or F, and with the "
        "'Corrections' novedad (T2R2-022).",
    'T2R1-011':
        "Bidirectional pair with 'Branch code' (T2R1-012), which is blank where this field = U "
        "(Unico) and populated where it = S (Sucursal).",
    'T2R1-012':
        "Also bidirectional with 'Branch name' (T2R1-013), which is populated together with this "
        "code.",
    'T2R1-019':
        "Bidirectional pair with 'Additional UPC value' (T2R2-056): contributor type 40 records are "
        "precisely the records that carry that value and that are excluded from this count.",
    'T2R2-003':
        "Bidirectional set with 'Foreign national not liable to contribute to pension' (T2R2-007), "
        "which where marked restricts this field to CE, PA, CD, SC or PE, and with 'Colombian abroad' "
        "(T2R2-008), which is used only where this field is CC or TI.",
    'T2R2-005':
        "Bidirectional set with the fields this code gates: 'Work location department code' "
        "(T2R2-009) and 'Work location municipality code' (T2R2-010) are blank for type 40; "
        "'Additional UPC value' (T2R2-056) and 'Principal contributor document type' (T2R2-074) are "
        "populated only for type 40; 'Hours worked' (T2R2-096) only for part-time type 51; and "
        "'Pension fund of the member' (T2R2-031) may be blank only for a type not obliged to "
        "contribute to pension.",
    'T2R2-006':
        "Bidirectional pair with 'Pension fund of the member' (T2R2-031), which may be blank only "
        "where this sub-type is one not obliged to contribute to the Sistema General de Pensiones.",
    'T2R2-008':
        "Also bidirectional with 'Date of filing abroad' (T2R2-097), which is populated only where "
        "this flag is marked.",
    'T2R2-009':
        "Also bidirectional with 'Work location municipality code' (T2R2-010), which is left blank in "
        "the same two cases.",
    'T2R2-031':
        "Also bidirectional with the 'TDP - transfer from another pension administrator' novedad "
        "(T2R2-019), which reports the move between administrators that changes the value carried "
        "here.",
    'T2R2-033':
        "Bidirectional pair with the 'TDE - transfer from another EPS' novedad (T2R2-017), which "
        "reports the move between health insurers that changes the value carried here.",
    'T2R2-036':
        "Bidirectional set with the whole novedad block (T2R2-015 to T2R2-030): those change-event "
        "flags are what drive this day count, so a novedad reported without a matching movement in "
        "the day counters is a reconciliation error the operador will surface.",
    'T2R2-039':
        "Bidirectional set with the whole novedad block (T2R2-015 to T2R2-030): those change-event "
        "flags are what drive this day count, so a novedad reported without a matching movement in "
        "the day counters is a reconciliation error the operador will surface.",
    'T2R2-042':
        "Bidirectional set with 'All-inclusive salary flag' (T2R2-041), which where marked sets this "
        "base to 70% of the all-inclusive salary, and with 'Solidarity pension fund - solidarity "
        "sub-account' (T2R2-051), which is payable only where this base reaches 4 SMMLV.",
    'T2R2-043':
        "Bidirectional pair with 'Contributor exonerated from payment' (T2R2-076), which is marked "
        "only where this base is below 10 SMMLV.",
    'T2R2-045':
        "Bidirectional pair with 'All-inclusive salary flag' (T2R2-041), which where marked sets this "
        "base to 70% of the all-inclusive salary.",
    'T2R2-046':
        "Bidirectional pair with 'Special pension rate indicator' (T2R2-079), which is populated "
        "wherever a non-standard rate - notably a Decreto Ley 2090 de 2003 high-risk rate - replaces "
        "the standard 16%.",
    'T2R2-048':
        "Also bidirectional with 'Value not withheld for voluntary contributions' (T2R2-053), which "
        "reports the amount this contribution removes from the withholding.",
    'T2R2-049':
        "Also bidirectional with 'Value not withheld for voluntary contributions' (T2R2-053), which "
        "reports the amount this contribution removes from the withholding.",
    'T2R2-066':
        "Also bidirectional with 'SENA contribution value' (T2R2-067), which is the amount this rate "
        "produces and is zero in the same cases.",
    'T2R2-068':
        "Also bidirectional with 'ICBF contribution value' (T2R2-069), which is the amount this rate "
        "produces and is zero in the same cases.",
    'T2R2-080':
        "More broadly, this field sits in the date block T2R2-080 to T2R2-097 that the whole novedad "
        "block (T2R2-015 to T2R2-030) gates.",
    'T2R2-097':
        "More broadly, this field sits in the date block T2R2-080 to T2R2-097 that the whole novedad "
        "block (T2R2-015 to T2R2-030) gates.",
}


def _apply_c16(fields):
    seen = set()
    for row in fields:
        if not isinstance(row, list) or len(row) < 13:
            continue
        s = _C16_REVERSE.get(row[3])
        if not s or row[3] in seen:
            continue
        seen.add(row[3])
        i = 6 if row[5] == "C" else 12
        cur = (row[i] or "").strip()
        if s in cur:
            continue
        row[i] = (cur + " " + s).strip() if cur and cur != "-" else s
    missing = set(_C16_REVERSE) - seen
    assert not missing, "C16 reverse target not found: %s" % sorted(missing)
    return fields


FIELDS = _apply_c16(FIELDS)


CFG = {
    "doc_id": "CO-PILA-003",
    "filing_id": "CO-PILA-MONTHLY-003",
    "name_en": "Integrated Contribution Settlement Return (PILA) - social security and payroll levies",
    "name_es": "Planilla Integrada de Liquidacion de Aportes (PILA)",
    "spec_sheet": "PILA Spec",
    "authority_full": "Ministerio de Salud y Proteccion Social, filed THROUGH A LICENSED PRIVATE "
                      "OPERADOR DE INFORMACION. The employer never transacts directly with the "
                      "government for social security.",
    "frequency": "Monthly. A planilla is required while the employment relationship subsists, even "
                 "in a month with no payment - unlike Formulario 350, which has a nil-period "
                 "exemption.",
    "due_date": "Between the 2nd and the 16th BUSINESS DAY of the month following the period, by the "
                "LAST TWO DIGITS of the employer identification number (Decreto 780 de 2016 "
                "art. 3.2.2.1 as substituted by Decreto 1990 de 2016 art. 2). Note the contrast "
                "with Formulario 350, which is keyed to the LAST digit and runs from the 7th to the "
                "16th business day.",
    "submission": "PORTAL ROUND-TRIP THROUGH A LICENSED PRIVATE OPERADOR DE INFORMACION. The "
                  "employer either keys the settlement on the operador's web site (modalidad "
                  "Electronica) or telephones its call centre (modalidad Asistida), or uploads the "
                  "two fixed-width files described here. The operador validates, settles, collects "
                  "and distributes to each administradora. THE EMPLOYER NEVER REACHES THE GOVERNMENT "
                  "DIRECTLY. Operadores are licensed by the Ministerio de Salud y Proteccion Social.",
    "file_format": "TWO FIXED-WIDTH FLAT FILES, byte-exact. Archivo Tipo 1 - datos generales del "
                   "aportante, 34 fields, 567 positions, one record. Archivo Tipo 2 - informacion "
                   "planilla integrada, Registro Tipo 1 (encabezado) 22 fields, 359 positions, one "
                   "record, followed by Registro Tipo 2 (liquidacion detallada) 97 fields, 686 "
                   "positions, one record per contributor. Numeric fields are right-justified and "
                   "ZERO-filled; alphanumeric fields are left-justified and SPACE-filled.",
    "legal_basis": "Resolucion MSPS 2388 de 2016 y su Anexo Tecnico 2 (codigo AT2, version 09, "
                   "16-09-2019); Decreto 780 de 2016 arts. 3.2.1.5, 3.2.2.1 y 3.2.3.9, como fueron "
                   "sustituidos por el Decreto 1990 de 2016 arts. 1 y 2; Ley 100 de 1993 arts. 20, "
                   "204; Ley 797 de 2003 art. 7; Ley 21 de 1982 art. 17; Ley 89 de 1988; Ley 1122 de "
                   "2007; Ley 1393 de 2010 art. 30; ET art. 114-1; Decreto 1072 de 2015 arts. "
                   "2.2.4.2.5.6, 2.2.4.3.3, 2.2.4.3.5; Decreto 1772 de 1994 art. 13; Decreto Ley "
                   "2090 de 2003; Decreto 525 de 2009; Ley 590 de 2000; Ley 1429 de 2010 art. 5; "
                   "Decreto 1469 de 2025 (SMMLV 2026).",
    "accuracy": "96% (PRIMARY SOURCE, byte-exact). Every field number, length, start and end "
                "position and data type is transcribed from the official 213-page Anexo Tecnico 2 "
                "at 00-official-sources/pdfs/Anexo-tecnico-2-2016-pila.pdf, and the three record "
                "totals reconcile exactly to the annex's own printed totals of 567, 359 and 686 "
                "positions. THIS BUILD CLOSES scope_manifest known gap CO-GAP-01, which recorded "
                "the Registro Tipo 2 positions as not extracted. The 4% reservation is: (a) the "
                "annex in the source registry is version 09 of 16 September 2019 and later "
                "resolutions may have amended individual code tables without changing the layout, "
                "so the code lists should be re-verified against the chosen operador's current "
                "technical guide; (b) each operador de informacion publishes its own upload "
                "wrapper and may impose additional validations on top of the annex; (c) CO-GAP-02 "
                "leaves the high-risk pension rate unconfirmed. It would rise to 99% with the "
                "chosen operador's current technical guide and a resolved CO-GAP-02.",
    "source_status": "PRIMARY, BYTE-EXACT. Anexo-tecnico-2-2016-pila.pdf (Res. MSPS 2388 de 2016, "
                     "Anexo Tecnico 2, AT2 v09, 16-09-2019, 213 pages), extracted to "
                     "_txt/pila_anexo2.txt and _txt/pila_fields.json and embedded in "
                     "co_r3_pila_layout.py. Field counts and position totals verified: A1 = 34 "
                     "campos / 567 posiciones; A2R1 = 22 campos / 359 posiciones; A2R2 = 97 campos "
                     "/ 686 posiciones. C19 pattern ^(A1|T2R1|T2R2)-[0-9]{3}$ - the numeric part is "
                     "the annex's own campo number, nothing derived.",
    "channel_notes": [
        "Channel: file_upload (fixed-width) into a PORTAL operated by a licensed private operador "
        "de informacion | Portal: the chosen operador's web site (the operador is licensed by the "
        "Ministerio de Salud y Proteccion Social; the employer selects one commercially) | Source: "
        "Res. MSPS 2388 de 2016 Anexo Tecnico 2 s.0 and s.2.1.1.2.1, and Decreto 780 de 2016 "
        "art. 3.2.3.9 as substituted by Decreto 1990 de 2016 | CONFIRMED.",
        "THE SOCIAL-SECURITY CHANNEL IS NOT THE TAX CHANNEL. PILA never touches DIAN Muisca, and "
        "Formulario 350 never touches an operador de informacion. Labelling either with the other's "
        "portal is a category error.",
        "Two modalities exist: 1 Electronica (the employer keys or uploads on the operador's site) "
        "and 2 Asistida (the operador's call centre keys it). Where Decreto 780 de 2016 art. 3.2.3.9 "
        "par. 2 exceptionally permits assisted payment, the modality field must still say "
        "ELECTRONICA and the operador reports those employers to the Ministry through SISPRO "
        "structure PUB019EXPE by the fifth business day of the following month.",
        "The layout is byte-exact and published, so this Spec CAN and DOES carry a real fixed-width "
        "sample on Sheet 9 - generated programmatically from the position table so that the record "
        "lengths are exactly 567, 359 and 686 characters.",
        "FORMAT TO CONFIRM vs a real filing: each operador wraps the two files in its own upload "
        "envelope and may add validations. Confirm the wrapper and any operador-specific rules with "
        "the client's chosen operador before go-live.",
    ],
    "integration_notes": [
        "integration_type = BOTH (scope_manifest CO-BOTH-PILA). Outbound: the two fixed-width files. "
        "Inbound: the operador's settlement response.",
        "The inbound leg (CO-IN-PILA-SETTLEMENT) is specified here rather than in a separate "
        "workbook because it is the response half of one exchange and is keyed on this filing's own "
        "planilla number (T2R1-017). The engine must reconcile the settled contributions against its "
        "own computation, capture the planilla number and payment date, and detect rejected "
        "contributor records. Each operador's response layout is proprietary and must be obtained "
        "from the client's chosen operador - it has no published national standard, so no field-"
        "level spec can honestly be written for it here.",
        "product_mapping_required = true. PILA needs FIVE contribution bases per employee (pension, "
        "health, occupational risk, CCF, and the separate uncapped parafiscal base), FOUR day "
        "counts, and sixteen change-event flags with their date pairs. None of these can be derived "
        "at reporting time from a single gross figure.",
        "Owned upstream (CCG control B7): the operador de informacion's own file wrapper and portal. "
        "Mercans produces the two annex-conformant files; the operador owns everything after that.",
    ],
    "b1_notes": [
        "PILA IS NOT A TAX FILING and carries NO residence concept. A non-resident employee working "
        "in Colombia under a Colombian contract contributes to social security on exactly the same "
        "terms as a resident - same bases, same rates, same ceiling and floor. The flat 20% of ET "
        "art. 408 has no application here.",
        "The one immigration-related field is 'Foreign national not liable to contribute to "
        "pensions' (T2R2-007), and it is about PENSION AFFILIATION, not tax residence: a foreign "
        "employee who proves affiliation to a pension system abroad may elect out of Colombian "
        "pension affiliation under Decreto 1072 de 2015 art. 2.2.1.2.1.4. Health, occupational risk "
        "and the parafiscal levies remain fully payable.",
        "It follows that the same employee can be simultaneously (a) withheld at 20% on hoja 2 of "
        "Formulario 350 as a non-resident, and (b) reported in PILA on ordinary terms. Do not let "
        "the tax residence flag leak into the PILA population rules.",
        "The mirror case - 'Colombian abroad' (T2R2-008) - is also not a tax field. It suppresses "
        "the DIVIPOLA work-location fields and enables the foreign filing date in T2R2-097.",
    ],
    "related": [
        "The employee health, pension and solidarity-fund figures must reconcile to nomina "
        "electronica NIE163, NIE166 and NIE168 / NIE170 (CO-DIAN-001), allowing for the different "
        "rounding conventions - PILA rounds UP to the next 100, the XML uses two decimals "
        "round-half-to-even.",
        "The ET art. 114-1 exoneration in A1-033 and T2R2-076 rests on the SAME test as Formulario "
        "350 casilla 27 (CO-DIAN-002). Configure it once.",
        "The employee's mandatory health and pension contributions - the amounts settled here - are "
        "the ingresos no constitutivos de renta that reduce the Formulario 350 casilla 77 base and "
        "are reported annually at Formulario 220 casillas 53-54 (CO-DIAN-004) and Formato 2276 "
        "numerals 23-24 (CO-DIAN-005).",
        "PILA planilla types T and F (Sistema General de Participaciones) and types I and Y "
        "(independent workers) are DESCOPED in scope_manifest - public sector and non-employees "
        "respectively.",
        "The occupational-risk premium (T2R2-063) and the employer's share of pension, health and "
        "the levies never appear on the nomina electronica, because that document reports only what "
        "the employee accrued and what was deducted from the employee.",
    ],
    "scope": (SCOPE_WHO + [
        "AMOUNTS AND CALCULATIONS",
        ("Salary and salary-constituting payments", "YES",
         "The core of all five contribution bases (CST art. 127)."),
        ("Non-salary payments within the 40% clamp", "NO",
         "Excluded from the contribution base - but only up to 40% of total remuneration. Ley 1393 "
         "de 2010 art. 30 adds the EXCESS over 40% back into the base, and that added-back amount "
         "must be separately identifiable because it is in the contribution base but out of the "
         "statutory-benefit base."),
        ("Statutory transport allowance", "NO",
         "Not salary for contribution purposes. It IS in the base of cesantias, prima and the "
         "severance indemnity - a different base, and one of the sharpest traps in Colombian "
         "payroll."),
        ("Paid rest days", "YES",
         "In the PARAFISCAL base (Ley 21 de 1982 art. 17) - campo T2R2-095 - which is why that base "
         "differs from the four contribution bases."),
        ("Contribution base ceiling of 25 SMMLV", "YES",
         "COP 43,772,625 in 2026. Applies to pension, health, occupational risk and the CCF. Does "
         "NOT apply to the parafiscal base in campo 95, which is uncapped."),
        ("Contribution base floor of 1 SMMLV", "YES",
         "COP 1,750,905 in 2026, except for the partial-time regime (contributor type 51), which "
         "uses hours worked in campo 96."),
        ("All-inclusive salary at 70% of the integral salary", "YES",
         "CST art. 132 num. 2. Flagged in campo 41 and applied to all four IBC fields."),
        ("Employer contributions", "YES",
         "PILA is the ONLY artefact that reports the employer's cost - pension 12%, health 8.5%, "
         "occupational risk 0.348% to 8.7%, CCF 4%, SENA 2%, ICBF 3%."),
        ("Employee deductions", "YES",
         "Pension 4%, health 4%, solidarity fund 1% to 2%. Reported as part of the total "
         "contribution, not as a separate deduction line."),
        ("Income tax withholding", "NO",
         "PILA is a contribution settlement, not a tax return. Withholding goes on Formulario 350."),
        ("SENA and ICBF for employees under 10 SMMLV where the employer is exonerated", "NO",
         "ET art. 114-1 exonerates employer health 8.5%, SENA 2% and ICBF 3%. Flagged at employer "
         "level in A1-033 and applied per employee per month in T2R2-076."),
        ("CCF 4% for the same employees", "YES",
         "The family compensation fund is NEVER exonerated under art. 114-1. The only relief is the "
         "Ley 1429 de 2010 art. 5 regime, flagged separately in A1-034."),
    ] + SCOPE_TIMING + [
        "SPECIAL CASES",
        ("Health period one month ahead of the other subsystems", "YES",
         "T2R1-016 normally carries the month AFTER T2R1-015: health is paid one month in advance. "
         "Setting them equal is the classic first-run defect."),
        ("Employee on unpaid leave for the whole month", "YES",
         "Reported with the SLN flag, its date pair, and reduced day counts. The employment "
         "relationship subsists, so the planilla is still filed."),
        ("Employed old-age pensioner", "YES",
         "Contributor sub-type 01. The annex forces the pension rate in campo 46 to zero for "
         "sub-types 1, 2, 3, 4, 5, 6, 9 and 12."),
        ("Foreign employee with proven pension cover abroad", "YES",
         "Flagged in campo 7. Pension is waived; health, occupational risk and the levies remain."),
        ("Employee at more than one work centre with different risk classes", "YES",
         "The class attaches to the WORK CENTRE (Decreto 1072 de 2015 art. 2.2.4.2.5.6). Where a "
         "person performs several occupations they contribute at the HIGHEST class; a mid-period "
         "move is reported through the VCT flag and its date pair."),
        ("Contributor type 40 (Beneficiario UPC Adicional)", "PARTIAL",
         "Reported as a detail record but EXCLUDED from the header contributor count in T2R1-019, "
         "and with its DIVIPOLA work-location fields blank."),
        ("Late payment", "YES",
         "Filed as planilla type M (mora), or N for a correction, with the associated planilla "
         "number and date in T2R1-009 and T2R1-010. The operador computes the interest on arrears."),
    ]),
    "fields": FIELDS,
    "_totals": TOTALS,
}

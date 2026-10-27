# -*- coding: utf-8 -*-
"""
CO-PILA-003 - Sheets 5 to 9 for the Planilla Integrada de Liquidacion de Aportes.

The Sample File sheet is GENERATED from the official position table in
co_r3_pila_layout.py, so the three records are guaranteed to be exactly 567,
359 and 686 characters long with every value in its published position.
"""

from co_r3_pila import CFG
from co_r3_pila_layout import A1, A2R1, A2R2, TOTALS

_IDX = {"A1": {t[0]: t for t in A1},
        "T2R1": {t[0]: t for t in A2R1},
        "T2R2": {t[0]: t for t in A2R2}}


def _render(rec, values):
    """Place each value at its official position; return the fixed-width record."""
    total = max(t[3] for t in _IDX[rec].values())
    buf = [" "] * total
    for campo, (n, lng, ini, fin, tipo, desc) in sorted(_IDX[rec].items()):
        v = values.get(campo, "")
        if tipo == "N":
            v = (v or "0").rjust(lng, "0")[:lng]
        else:
            v = (v or "").ljust(lng)[:lng]
        buf[ini - 1:fin] = list(v)
    out = "".join(buf)
    assert len(out) == total, (rec, len(out), total)
    return out


# --- worked example values, consistent with the other five Colombia Specs ----
_A1 = {
    1: "MERCANS COLOMBIA S.A.S.", 2: "NI", 3: "900123456", 4: "7",
    5: "", 6: "", 7: "B", 8: "2", 9: "J", 10: "U",
    11: "CALLE 100 No 7-33 PISO 12", 12: "001", 13: "11", 14: "6920",
    15: "6017439999", 16: "", 17: "nomina@mercans.com",
    18: "79123456", 19: "0", 20: "CC", 21: "GOMEZ", 22: "RUIZ", 23: "ANA", 24: "MARIA",
    25: "", 26: "", 27: "", 28: "01", 29: "2026-03", 30: "01",
    31: "", 32: "", 33: "S", 34: "N",
}
_T2R1 = {
    1: "01", 2: "1", 3: "0001", 4: "MERCANS COLOMBIA S.A.S.", 5: "NI",
    6: "900123456", 7: "7", 8: "E", 9: "", 10: "", 11: "U", 12: "", 13: "",
    14: "ARL001", 15: "2026-03", 16: "2026-04", 17: "0000123456",
    18: "2026-04-10", 19: "00001", 20: "12000000", 21: "01", 22: "01",
}
_T2R2 = {
    1: "02", 2: "00001", 3: "CC", 4: "1020304050", 5: "01", 6: "00",
    7: "", 8: "", 9: "11", 10: "001",
    11: "PEREZ", 12: "GOMEZ", 13: "JUAN", 14: "CARLOS",
    30: "0",
    31: "AFP001", 32: "", 33: "EPS001", 34: "", 35: "CCF001",
    36: "30", 37: "30", 38: "30", 39: "30",
    40: "12000000", 41: "",
    42: "12000000", 43: "12000000", 44: "12000000", 45: "12000000",
    46: "160000", 47: "1920000", 48: "0", 49: "0", 50: "1920000",
    51: "120000", 52: "0", 53: "0",
    54: "40000", 55: "480000", 56: "0",
    57: "", 58: "0", 59: "", 60: "0",
    61: "5220", 62: "1", 63: "62700",
    64: "40000", 65: "480000",
    66: "0", 67: "0", 68: "0", 69: "0", 70: "0", 71: "0", 72: "0", 73: "0",
    74: "", 75: "", 76: "S", 77: "ARL001", 78: "1", 79: "",
    80: "2021-01-11", 81: "", 82: "", 83: "", 84: "", 85: "", 86: "",
    87: "", 88: "", 89: "", 90: "", 91: "", 92: "", 93: "", 94: "",
    95: "12000000", 96: "0", 97: "",
}

_REC_A1 = _render("A1", _A1)
_REC_T2R1 = _render("T2R1", _T2R1)
_REC_T2R2 = _render("T2R2", _T2R2)


def _ruler(width):
    """Column ruler so a reader can count positions on the printed sample."""
    tens = "".join(str((i // 10) % 10) for i in range(1, width + 1))
    ones = "".join(str(i % 10) for i in range(1, width + 1))
    return tens, ones


def _wrapped(label, record, width=110):
    """Break a long fixed-width record into position-labelled chunks."""
    lines = []
    for start in range(0, len(record), width):
        end = min(start + width, len(record))
        lines.append("  pos %4d-%-4d |%s|" % (start + 1, end, record[start:end]))
    return ["%s (length %d)" % (label, len(record))] + lines


# ===========================================================================
#  SHEET 5 - FILE STRUCTURE
# ===========================================================================
CFG["filestruct"] = [
    ("##", "SUBMISSION FORMAT - VERIFIED (v2.7 STEP 3.5)"),
    ("Channel", "file_upload of two fixed-width flat files into the web portal of a LICENSED "
                "PRIVATE OPERADOR DE INFORMACION, or direct keying / call-centre entry on the same "
                "portal. The employer NEVER transacts directly with the government for social "
                "security."),
    ("Portal", "The operador de informacion chosen commercially by the employer. Operadores are "
               "licensed by the Ministerio de Salud y Proteccion Social. THIS IS NOT THE DIAN "
               "PORTAL: PILA never touches Muisca and Formulario 350 never touches an operador."),
    ("Source for the channel", "Res. MSPS 2388 de 2016 Anexo Tecnico 2, s.0 (Descripcion de "
                               "archivos) and s.2.1.1.2.1 (Modalidad de la planilla); Decreto 780 de "
                               "2016 art. 3.2.3.9 as substituted by Decreto 1990 de 2016. CONFIRMED."),
    ("Modalities", "1 Electronica - the employer keys or uploads on the operador's web site. "
                   "2 Asistida - the operador's call centre keys it. Where Decreto 780 art. 3.2.3.9 "
                   "par. 2 exceptionally permits assisted payment, the field must still read "
                   "ELECTRONICA and the operador reports those employers to the Ministry through "
                   "SISPRO structure PUB019EXPE by the fifth business day of the following month."),
    ("FORMAT TO CONFIRM", "The two files below are byte-exact against the official annex. What is "
                          "NOT publicly specified is each operador's upload wrapper and any "
                          "additional validations it layers on top. Confirm with the client's chosen "
                          "operador before go-live."),

    ("##", "FILE FORMAT"),
    ("File type", "Two fixed-width flat text files, one record per line."),
    ("Numeric fields (tipo N)", "Right-justified, ZERO-filled to the left. The annex states this "
                                "expressly at s.0."),
    ("Alphanumeric fields (tipo A)", "Left-justified, SPACE-filled to the right."),
    ("Record lengths", "Archivo Tipo 1 = 567 positions. Archivo Tipo 2 Registro Tipo 1 = 359 "
                       "positions. Archivo Tipo 2 Registro Tipo 2 = 686 positions. All three "
                       "verified against the annex's own printed totals."),
    ("Rounding", "ROUND UP throughout. The contribution base is rounded up to the whole peso and "
                 "each contribution value is rounded up to the NEXT MULTIPLE OF 100 (Decreto 1990 "
                 "de 2016 art. 1). This is a different convention from the nomina electronica "
                 "(2 decimals, round-half-to-even) and from Formulario 350 (nearest 1,000). The "
                 "same contribution therefore appears as different numbers in different artefacts."),
    ("Annual refresh obligation", "The annex requires the employer to update ALL Archivo Tipo 1 "
                                  "information with the operador from January 2018 onward, and to "
                                  "refresh it ANNUALLY. The operador must prompt for it."),

    ("##", "RECORD STRUCTURE"),
    ("Archivo Tipo 1", "Datos generales del aportante. 34 campos, positions 1 to 567. ONE record "
                       "per employer (or per branch where the form of presentation is S)."),
    ("Archivo Tipo 2, Registro Tipo 1", "Encabezado. 22 campos, positions 1 to 359. ONE record. "
                                        "Identified by record type 01 in positions 1-2."),
    ("Archivo Tipo 2, Registro Tipo 2", "Liquidacion detallada de aportes. 97 campos, positions 1 "
                                        "to 686. ONE record PER CONTRIBUTOR. Identified by record "
                                        "type 02 in positions 1-2, with a strictly sequential "
                                        "counter in positions 3-7 starting at 00001."),
    ("Registros Tipo 3 to 12", "TOTALS RECORDS GENERATED BY THE OPERADOR, not by the employer. "
                               "Type 3 total pension contributions; type 4 solidarity pension fund; "
                               "type 5 health; type 6 occupational risk; type 7 family compensation "
                               "funds; type 8 SENA; type 9 ICBF; type 10 ESAP; type 11 MEN; type 12 "
                               "total payable for the period. They also carry the days-in-arrears "
                               "count and the interest on arrears, which the operador computes from "
                               "the payment date. The employer neither produces nor validates them, "
                               "which is why they are OUT OF SCOPE for this Spec - but the engine "
                               "must PARSE them from the settlement response to reconcile."),

    ("##", "SECTION LAYOUT - ARCHIVO TIPO 1 (34 campos, 567 posiciones)"),
    ("Identification", "1 Nombre/razon social (1-200) | 2 Tipo documento (201-202) | 3 Numero de "
                       "identificacion (203-218) | 4 Digito de verificacion (219)"),
    ("Branch", "5 Codigo sucursal (220-229) | 6 Nombre sucursal (230-269)"),
    ("Classification", "7 Clase de aportante (270) | 8 Naturaleza juridica (271) | 9 Tipo persona "
                       "(272) | 10 Forma de presentacion (273)"),
    ("Location and contact", "11 Direccion (274-313) | 12 Codigo ciudad (314-316) | 13 Codigo "
                             "departamento (317-318) | 14 Codigo DANE actividad economica (319-322) "
                             "| 15 Telefono (323-332) | 16 Fax (333-342) | 17 E-mail (343-402)"),
    ("Legal representative", "18 Numero identificacion (403-418) | 19 Digito verificacion (419) | "
                             "20 Tipo identificacion (420-421) | 21 Primer apellido (422-441) | "
                             "22 Segundo apellido (442-471) | 23 Primer nombre (472-491) | "
                             "24 Segundo nombre (492-521)"),
    ("Insolvency", "25 Fecha inicio concordato/reestructuracion/liquidacion/cese (522-531) | "
                   "26 Tipo de accion (532) | 27 Fecha fin actividades comerciales (533-542)"),
    ("System and period", "28 Codigo del operador (543-544) | 29 Periodo de pago (545-551) | "
                          "30 Tipo de aportante (552-553)"),
    ("Ley 1429 and exoneration", "31 Fecha matricula mercantil (554-563) | 32 Codigo departamento "
                                 "(564-565) | 33 APORTANTE EXONERADO SALUD/SENA/ICBF (566) | "
                                 "34 Beneficios art. 5 Ley 1429 para CCF (567)"),

    ("##", "SECTION LAYOUT - ARCHIVO TIPO 2, REGISTRO TIPO 1 (22 campos, 359 posiciones)"),
    ("Header", "1 Tipo de registro = 01 (1-2) | 2 Modalidad de la planilla (3) | 3 Secuencia (4-7)"),
    ("Employer echo", "4 Nombre/razon social (8-207) | 5 Tipo documento (208-209) | 6 Numero "
                      "identificacion (210-225) | 7 Digito verificacion (226) - all four must equal "
                      "Archivo Tipo 1 campos 1, 2, 3 and 4"),
    ("Planilla identity", "8 Tipo de planilla (227) | 9 Numero planilla asociada (228-237) | "
                          "10 Fecha pago planilla asociada (238-247)"),
    ("Branch and ARL", "11 Forma de presentacion (248) | 12 Codigo sucursal (249-258) | 13 Nombre "
                       "sucursal (259-298) | 14 Codigo ARL (299-304)"),
    ("Periods", "15 Periodo de pago sistemas distintos de salud (305-311) | 16 PERIODO DE PAGO "
                "SALUD (312-318) - normally the month AFTER campo 15, because health is paid one "
                "month in advance"),
    ("Settlement", "17 Numero de radicacion / planilla (319-328) | 18 Fecha de pago (329-338) | "
                   "19 Numero total de cotizantes (339-343) | 20 Valor total de la nomina - the "
                   "PARAFISCAL base sum (344-355) | 21 Tipo de aportante (356-357) | 22 Codigo del "
                   "operador (358-359)"),

    ("##", "SECTION LAYOUT - ARCHIVO TIPO 2, REGISTRO TIPO 2 (97 campos, 686 posiciones)"),
    ("Identity (1-14)", "1 Tipo de registro = 02 (1-2) | 2 Secuencia (3-7) | 3 Tipo documento (8-9) "
                        "| 4 Numero identificacion (10-25) | 5 Tipo cotizante (26-27) | 6 Subtipo "
                        "(28-29) | 7 Extranjero no obligado a pension (30) | 8 Colombiano en el "
                        "exterior (31) | 9 Departamento laboral (32-33) | 10 Municipio laboral "
                        "(34-36) | 11-14 Apellidos y nombres (37-136)"),
    ("Novedades (15-30)", "15 ING (137) | 16 RET (138) | 17 TDE (139) | 18 TAE (140) | 19 TDP (141) "
                          "| 20 TAP (142) | 21 VSP (143) | 22 Correcciones (144) | 23 VST (145) | "
                          "24 SLN (146) | 25 IGE (147) | 26 LMA (148) | 27 VAC-LR (149) | 28 AVP "
                          "(150) | 29 VCT (151) | 30 IRL dias (152-153)"),
    ("Administradoras (31-35)", "31 AFP del afiliado (154-159) | 32 AFP destino (160-165) | 33 EPS "
                                "del afiliado (166-171) | 34 EPS destino (172-177) | 35 CCF "
                                "(178-183)"),
    ("Dias cotizados (36-39)", "36 Pension (184-185) | 37 Salud (186-187) | 38 Riesgos laborales "
                               "(188-189) | 39 CCF (190-191)"),
    ("Bases (40-45)", "40 Salario basico (192-200) | 41 Salario integral (201) | 42 IBC pension "
                      "(202-210) | 43 IBC salud (211-219) | 44 IBC riesgos laborales (220-228) | "
                      "45 IBC CCF (229-237)"),
    ("Pension (46-53)", "46 Tarifa pension (238-244) | 47 Cotizacion obligatoria (245-253) | "
                        "48 Aporte voluntario afiliado (254-262) | 49 Aporte voluntario aportante "
                        "(263-271) | 50 Total SGP (272-280) | 51 FSP solidaridad (281-289) | "
                        "52 FSP subsistencia (290-298) | 53 Valor no retenido (299-307)"),
    ("Salud (54-60)", "54 Tarifa salud (308-314) | 55 Cotizacion obligatoria salud (315-323) | "
                      "56 UPC adicional (324-332) | 57 Autorizacion IGE (333-347) | 58 Valor IGE "
                      "(348-356) | 59 Autorizacion LMA (357-371) | 60 Valor LMA (372-380)"),
    ("Riesgos laborales (61-63)", "61 Tarifa ARL (381-389) | 62 Centro de trabajo (390-398) | "
                                  "63 Cotizacion obligatoria ARL (399-407)"),
    ("Parafiscales (64-73)", "64 Tarifa CCF (408-414) | 65 Valor CCF (415-423) | 66 Tarifa SENA "
                             "(424-430) | 67 Valor SENA (431-439) | 68 Tarifa ICBF (440-446) | "
                             "69 Valor ICBF (447-455) | 70 Tarifa ESAP (456-462) | 71 Valor ESAP "
                             "(463-471) | 72 Tarifa MEN (472-478) | 73 Valor MEN (479-487)"),
    ("Principal y exoneracion (74-79)", "74 Tipo documento cotizante principal (488-489) | "
                                        "75 Numero identificacion principal (490-505) | "
                                        "76 COTIZANTE EXONERADO (506) | 77 ARL del afiliado "
                                        "(507-512) | 78 Clase de riesgo (513) | 79 Indicador tarifa "
                                        "especial pensiones (514)"),
    ("Fechas de novedad (80-94)", "80 Ingreso (515-524) | 81 Retiro (525-534) | 82 Inicio VSP "
                                  "(535-544) | 83 Inicio SLN (545-554) | 84 Fin SLN (555-564) | "
                                  "85 Inicio IGE (565-574) | 86 Fin IGE (575-584) | 87 Inicio LMA "
                                  "(585-594) | 88 Fin LMA (595-604) | 89 Inicio VAC-LR (605-614) | "
                                  "90 Fin VAC-LR (615-624) | 91 Inicio VCT (625-634) | 92 Fin VCT "
                                  "(635-644) | 93 Inicio IRL (645-654) | 94 Fin IRL (655-664)"),
    ("Cierre (95-97)", "95 IBC OTROS PARAFISCALES DIFERENTES A CCF (665-673) | 96 Numero de horas "
                       "laboradas (674-676) | 97 Fecha radicacion en el exterior (677-686)"),

    ("##", "INBOUND - SETTLEMENT RESPONSE (integration CO-IN-PILA-SETTLEMENT)"),
    ("What comes back", "The operador returns a settlement: the planilla number (matching "
                        "T2R1-017), the payment date, the totals records (types 3 to 12) and any "
                        "rejected contributor records."),
    ("What the engine must do", "Reconcile the settled contributions against its own computation "
                                "per subsystem; capture the planilla number and payment date as "
                                "evidence of compliance; and detect rejected contributor records "
                                "so they can be re-filed on a correction planilla (type N)."),
    ("Why no field-level spec here", "Each operador's response layout is PROPRIETARY. There is no "
                                     "published national standard for it, so writing a field-level "
                                     "specification would be invention. Obtain the layout from the "
                                     "client's chosen operador at implementation. This is an "
                                     "upstream-owned interface under CCG control B7."),
]

# ===========================================================================
#  SHEET 6 - FIELD OPTIONS
# ===========================================================================
CFG["options"] = [
    "CLASE DE APORTANTE (A1-007)",
    ("A", "200+", "Aportante con 200 o mas cotizantes",
     "Counted across ALL branches and dependencies, not per branch."),
    ("B", "<200", "Aportante con menos de 200 cotizantes",
     "Counted across all branches. The default for most corporate employers."),
    ("C", "MIPYME", "Aportante Mipyme que se acoge a Ley 590 de 2000",
     "Fewer than 200 contributors AND eligible for the SENA, ICBF and CCF parafiscal discounts of "
     "Ley 590 de 2000 and Decreto 525 de 2009. The operador must verify MONTHLY that the employer "
     "appears in the file DIAN sends the Ministry under Decreto 525 art. 6, checking the fechinst "
     "date - so the class cannot simply be asserted by the employer."),
    ("D", "LEY1429", "Aportante beneficiario de la Ley de Formalizacion y Generacion de Empleo",
     "Beneficiary of Ley 1429 de 2010 under Decreto 1074 de 2015 art. 2.2.2.42.1. Requires the "
     "commercial-registry date in A1-031, which must fall between 29 December 2010 and 31 December "
     "2014."),

    "NATURALEZA JURIDICA (A1-008)",
    ("1", "PUB", "Publica", "Public entity."),
    ("2", "PRIV", "Privada", "Private entity - the in-scope population."),
    ("3", "MIX", "Mixta", "Mixed-capital entity."),
    ("4", "MULTI", "Organismos multilaterales", "Multilateral organisation."),
    ("5", "EXT", "Entidades de derecho publico no sometidas a la legislacion colombiana",
     "Public-law entity not subject to Colombian law - typically a foreign mission."),

    "TIPO PERSONA (A1-009) and TIPO DOCUMENTO APORTANTE (A1-002, T2R1-005)",
    ("J", "JUR", "Juridica", "Legal person. Makes A1-004 (DV) and the whole legal-representative "
     "block A1-018 to A1-024 mandatory."),
    ("N", "NAT", "Natural", "Natural person. Narrows the valid document types to CC, CE, TI, PA, "
     "CD, PE and SC - NI is not available."),
    ("NI", "NI", "Numero de identificacion tributaria", "The document type of a corporate employer."),
    ("CC", "CC", "Cedula de ciudadania", "Numeric only."),
    ("CE", "CE", "Cedula de extranjeria", "Numeric only."),
    ("TI", "TI", "Tarjeta de identidad", "Numeric only."),
    ("PA", "PA", "Pasaporte", "ALPHANUMERIC permitted."),
    ("CD", "CD", "Carne diplomatico", "ALPHANUMERIC permitted."),
    ("SC", "SC", "Salvoconducto de permanencia", "Numeric only."),
    ("PE", "PE", "Permiso Especial de Permanencia", "Numeric only."),
    ("RC", "RC", "Registro civil", "Available in the CONTRIBUTOR list (T2R2-003) but not in the "
     "employer list."),

    "TIPO DOCUMENTO REPRESENTANTE LEGAL (A1-020) - only four values",
    ("CC", "CC", "Cedula de ciudadania", "Numeric."),
    ("CE", "CE", "Cedula de extranjeria", "Numeric."),
    ("PA", "PA", "Pasaporte", "Alphanumeric permitted."),
    ("CD", "CD", "Carne diplomatico", "Alphanumeric permitted."),
    ("(narrower)", "-", "-", "NI, TI, SC, PE and RC are NOT available for a legal representative, "
     "although several of them are available for the employer itself."),

    "FORMA DE PRESENTACION (A1-010, T2R1-011)",
    ("U", "UNICO", "Unico", "A single consolidated planilla. Branch code and name must be BLANK."),
    ("S", "SUC", "Sucursal", "One planilla per branch. Branch code and name become required."),

    "TIPO DE ACCION (A1-026)",
    ("1", "CONC", "Concordato", "Insolvency arrangement."),
    ("2", "REEST", "Reestructuracion", "Restructuring."),
    ("3", "LIQ", "Liquidacion", "Liquidation."),
    ("4", "CESE", "Cese de actividades", "Cessation of activities. Where populated, A1-027 fixes the "
     "date from which the employer is no longer obliged to contribute."),

    "TIPO DE APORTANTE (A1-030, T2R1-021) - must be equal in both records",
    ("1", "EMPL", "Empleador", "The in-scope value for private corporate payroll."),
    ("2", "IND", "Independiente", "Independent worker - DESCOPED (planilla types I and Y)."),
    ("3", "PUB-ESP", "Entidades o universidades publicas de regimenes especial y de exception",
     "Public sector."),
    ("4", "AGREM", "Agremiaciones, asociaciones o congregaciones religiosas", "-"),
    ("5", "COOP", "Cooperativas y precooperativas de trabajo asociado", "-"),
    ("6", "DIPL", "Misiones diplomaticas, consulares o de organismos multilaterales", "-"),
    ("7", "HOG", "Organizaciones del Programa de Hogares de Bienestar", "-"),
    ("8", "CONC", "Pagador de concejales y ediles", "-"),
    ("9", "SIND", "Pagador de aportes contrato sindical", "-"),
    ("10", "REINC", "Pagador programa de reincorporacion", "-"),
    ("11", "MAG", "Pagador aportes parafiscales del Magisterio", "-"),
    ("12", "HUM", "Pagador prestacion humanitaria", "-"),

    "TIPO DOCUMENTO COTIZANTE (T2R2-003 and T2R2-074) - VERBATIM from Anexo Tecnico 2 campo 3; "
    "eight values, and NOT the DIAN numeric catalogue. Mirrors the Data Dictionary mapper "
    "'Employee Document Type (PILA / Cesantias)'",
    ("CC", "13", "Cedula de ciudadania", "Colombian national identity card. Numeric only. DIAN "
     "numeric equivalent 13."),
    ("CE", "22", "Cedula de extranjeria", "Foreign resident's identity card. Numeric only. DIAN "
     "numeric equivalent 22."),
    ("TI", "12", "Tarjeta de identidad", "Identity card for a person aged 7 to 17. Numeric only. "
     "DIAN numeric equivalent 12."),
    ("PA", "41", "Pasaporte", "Passport. ALPHANUMERIC permitted here - the annex names PA and CD "
     "as the only two alphanumeric types. DIAN numeric equivalent 41."),
    ("CD", "-", "Carne diplomatico", "Diplomatic card. ALPHANUMERIC permitted. NO DIAN numeric "
     "equivalent exists, so this document type cannot be carried on the nomina electronica."),
    ("SC", "-", "Salvoconducto de permanencia", "Safe-conduct of stay. Numeric only. NO DIAN "
     "numeric equivalent exists."),
    ("RC", "11", "Registro civil", "Civil birth registration. Available in the CONTRIBUTOR list "
     "but NOT in the employer list (A1-002). DIAN numeric equivalent 11."),
    ("PE", "47", "Permiso Especial de Permanencia", "Numeric only and EXACTLY 15 digits (SOI hard "
     "rule). DIAN numeric equivalent 47, abbreviated PEP in Anexo table 5.2.1."),
    ("(not PT)", "-", "Permiso por Proteccion Temporal", "PT is NOT in this fixed-width list. It "
     "is printed in the cesantias XLS document-type list only - see CO-CESANTIAS-006. CO-GAP-06."),

    "LEY 1429 DE 2010 (A1-034) - eleccion del beneficio del art. 5 para la caja de compensacion "
    "familiar",
    ("S", "SI", "Si - el aportante se acoge al beneficio", "The employer elects the Ley 1429 art. 5 "
     "progressive CCF contribution. Decreto 1074 de 2015 art. 2.2.2.42.1. Normally accompanies "
     "Clase de aportante = D, and it makes the commercial registry date (A1-031) and the "
     "registered-seat department code (A1-032) MANDATORY."),
    ("N", "NO", "No - el aportante no se acoge", "THE DEFAULT for an established employer. The "
     "full 4% CCF contribution applies."),
    ("(hard rule)", "-", "-", "The election is only available to an employer that qualifies under "
     "Ley 1429 de 2010 as a small business formalised in the benefit window. Where A1-034 = S but "
     "A1-007 (clase de aportante) is not D, the operador rejects the archivo tipo 1."),

    "MODALIDAD DE LA PLANILLA (T2R1-002)",
    ("1", "ELEC", "Electronica", "Prepared and paid over the internet on the operador's site. Also "
     "the value to use where Decreto 780 de 2016 art. 3.2.3.9 par. 2 exceptionally permits assisted "
     "PAYMENT - the modality still reads electronica, and the operador reports those employers "
     "separately through SISPRO structure PUB019EXPE."),
    ("2", "ASIST", "Asistida", "The employer telephones the operador's call centre, which keys or "
     "digitises the information."),

    "TIPO DE PLANILLA (T2R1-008)",
    ("E", "EMPL", "Planilla empleados", "THE IN-SCOPE VALUE. Used for contributor types 1, 12, 18, "
     "19, 20, 21, 22, 30, 31, 32, 40, 51, 54 and others."),
    ("A", "ING", "Planilla cotizantes con novedad de ingreso", "New joiners settled separately."),
    ("M", "MORA", "Planilla mora", "Late payment. The operador computes interest on arrears."),
    ("N", "CORR", "Planilla correcciones", "Correction of an earlier planilla. Requires the "
     "associated planilla number and date in T2R1-009 and T2R1-010, and the operador must settle "
     "interest on arrears except for salary retroactives and timely termination novedades."),
    ("S", "DOM", "Planilla empleados de servicio domestico", "Domestic service."),
    ("I", "IND", "Planilla independientes", "DESCOPED - independent workers contribute on 40% of "
     "fees, not salary, and the payer is not an employer."),
    ("Y", "IND-EMP", "Planilla independientes empresas", "DESCOPED - the contratante paying for "
     "service contractors."),
    ("H", "MAD", "Planilla madres sustitutas", "Substitute mothers."),
    ("T", "SGP", "Planilla entidad beneficiaria del Sistema General de Participaciones",
     "DESCOPED - public sector only (contributor type 47)."),
    ("F", "SGP-PAT", "Planilla pago aporte patronal faltante SGP", "DESCOPED - public sector only."),
    ("J", "JUD", "Planilla pago seguridad social en cumplimiento de sentencia judicial",
     "Court-ordered settlement of salary factors omitted from the original liquidation."),
    ("X", "LIQ", "Planilla para el pago empresa liquidada", "Liquidated company."),
    ("U", "UGPP", "Planilla de uso UGPP para pago por terceros", "UGPP third-party payment; "
     "T2R1-009 carries the judicial deposit title number."),
    ("K", "EST", "Planilla estudiantes", "Students."),
    ("O", "UGPP-OBL", "Planilla obligaciones determinadas por la UGPP",
     "UGPP-determined liabilities; T2R1-009 carries the planilla of the original payment."),

    "TIPO COTIZANTE (T2R2-005) - the PILA list, WIDER than the nomina electronica list",
    ("1", "DEP", "Dependiente", "Standard employee. Maps to nomina electronica TipoTrabajador 01."),
    ("2", "DOM", "Servicio domestico", "Maps to 02."),
    ("3", "IND", "Independiente", "NO nomina electronica equivalent - descoped population."),
    ("4", "MAD", "Madre sustituta", "Maps to 04 (Madre comunitaria) with care."),
    ("12", "APR-L", "Aprendices en etapa lectiva", "Maps to 12."),
    ("16", "AGREM", "Independiente agremiado o asociado", "NO nomina electronica equivalent."),
    ("18", "FUN", "Funcionarios publicos sin tope maximo en el IBC", "Maps to 18."),
    ("19", "APR-P", "Aprendices en etapa productiva", "Maps to 19."),
    ("20", "EST-789", "Estudiantes (Regimen especial - Ley 789/2002)",
     "NO nomina electronica equivalent."),
    ("21", "EST-PG", "Estudiantes de postgrado en salud", "Maps to 21."),
    ("22", "PROF", "Profesor de establecimiento particular", "Maps to 22."),
    ("23", "EST-RL", "Estudiantes aporte solo riesgos laborales", "Maps to 23."),
    ("30", "DEP-ESP", "Dependiente entidades o universidades publicas de regimenes especial y de "
     "excepcion", "Maps to 30."),
    ("31", "COOP", "Cooperados o precooperativas de trabajo asociado", "Maps to 31. The only type "
     "for which the nomina electronica Compensacion elements apply."),
    ("32", "DIPL", "Cotizante de carrera diplomatica o consular extranjera o de organismo "
     "multilateral", "NO nomina electronica equivalent."),
    ("33", "FSP", "Beneficiario del Fondo de Solidaridad Pensional", "NO equivalent."),
    ("34 / 35 / 36", "CONC", "Concejales y ediles", "NO equivalent."),
    ("40", "UPC", "Beneficiario UPC Adicional", "NO equivalent. EXCLUDED from the header contributor "
     "count in T2R1-019, and its DIVIPOLA work-location fields must be blank."),
    ("42", "IND-SAL", "Cotizante independiente pago solo salud", "NO equivalent."),
    ("43", "PEN-3RO", "Cotizante a pensiones con pago por tercero", "NO equivalent."),
    ("44 / 45", "EMERG", "Cotizante dependiente de empleo de emergencia", "NO equivalent."),
    ("47", "SGP", "Trabajador dependiente de entidad beneficiaria del SGP", "Maps to 47. Public "
     "sector - planilla types T and F are descoped."),
    ("51", "PARC", "Trabajador de tiempo parcial", "Maps to 51. Uses the hours-worked field "
     "T2R2-096 instead of the 1-SMMLV floor."),
    ("52", "CES", "Beneficiario del mecanismo de proteccion al cesante", "NO equivalent."),
    ("53 / 55", "PART", "Afiliado participe / participe-dependiente", "NO equivalent."),
    ("54", "PREP", "Prepensionado de entidad en liquidacion", "Maps to 54."),
    ("56", "PREP-V", "Prepensionado con aporte voluntario a salud", "Maps to 56."),
    ("57", "IND-RL", "Independiente voluntario al Sistema de Riesgos Laborales", "NO equivalent."),
    ("58", "EST-PUB", "Estudiantes de practicas laborales en el sector publico", "Maps to 58."),
    ("59", "IND-PS", "Independiente con contrato de prestacion de servicios superior a 1 mes",
     "NO equivalent - descoped population."),
    ("60 / 61 / 62 / 63", "OTROS", "Edil no beneficiario FSP / reincorporacion / Magisterio / "
     "prestacion humanitaria", "NO nomina electronica equivalent."),
    ("(mapping warning)", "-", "-", "The nomina electronica TipoTrabajador table 5.5.3 carries only "
     "SIXTEEN values. Copying a PILA code straight into the XML will fail DIAN validation for every "
     "code marked 'NO equivalent' above. Build an explicit mapping table."),

    "SUBTIPO COTIZANTE (T2R2-006)",
    ("0", "NA", "Cuando no aplique ningun subtipo", "The default."),
    ("1", "PEN-DEP", "Dependiente pensionado por vejez, jubilacion o invalidez activo",
     "The only value with a nomina electronica equivalent (SubTipoTrabajador 01)."),
    ("2", "PEN-IND", "Independiente pensionado activo", "-"),
    ("3", "EDAD", "Cotizante no obligado a cotizacion a pensiones por edad", "-"),
    ("4", "REQ", "Cotizante con requisitos cumplidos para pension", "-"),
    ("5", "IND-SUST", "Cotizante con indemnizacion sustitutiva o devolucion de saldos reconocida",
     "-"),
    ("6", "EXCEP", "Cotizante de regimen exceptuado de pensiones", "-"),
    ("9", "MESADA", "Pensionado con mesada igual o superior a 25 SMLMV", "-"),
    ("10", "EXT-VOL", "Residente en el exterior afiliado voluntario", "-"),
    ("11 / 12", "TAXI", "Conductores de servicio publico individual de pasajeros en vehiculos taxi",
     "12 is additionally not obliged to contribute to pension."),
    ("(hard rule)", "-", "-", "Where the subtipo is 1, 2, 3, 4, 5, 6, 9 or 12, campo T2R2-046 "
     "(pension contribution rate) MUST be 0. The annex states this expressly."),

    "NOVEDADES (T2R2-015 to T2R2-030) - permitted values",
    ("ING", "blank / R / X / C", "Ingreso", "Hire. Makes T2R2-080 mandatory."),
    ("RET", "blank / P / R / X / C", "Retiro", "Termination. Makes T2R2-081 mandatory."),
    ("TDE / TAE", "blank / X", "Traslado desde / a otra EPS o EOC",
     "Health-insurer transfer. TAE makes T2R2-034 mandatory."),
    ("TDP / TAP", "blank / X", "Traslado desde / a otra administradora de pensiones",
     "Pension-fund transfer. TAP makes T2R2-032 mandatory."),
    ("VSP", "blank / X", "Variacion permanente de salario", "Makes T2R2-082 mandatory."),
    ("Correcciones", "blank / A / C", "Correcciones",
     "A adds a contributor omitted from the original planilla; C corrects one already reported. "
     "Only meaningful on planilla type N."),
    ("VST", "blank / X", "Variacion transitoria del salario", "A one-off base variation."),
    ("SLN", "blank / X / C", "Suspension temporal del contrato o licencia no remunerada",
     "Makes T2R2-083 and T2R2-084 mandatory. Value C plus a PUBLIC-law employer is one of only two "
     "cases in which the health rate T2R2-054 may be reported as zero."),
    ("IGE", "blank / X", "Incapacidad temporal por enfermedad general",
     "Makes T2R2-085, T2R2-086 and the authorisation fields relevant."),
    ("LMA", "blank / X", "Licencia de maternidad o paternidad",
     "Makes T2R2-087, T2R2-088 and the authorisation fields relevant."),
    ("VAC-LR", "X / L / blank", "Vacaciones / Licencia remunerada",
     "A THREE-VALUE flag: X = vacaciones, L = licencia remunerada. They map to two DIFFERENT nomina "
     "electronica blocks, so the value carries information and must not be normalised."),
    ("AVP", "blank / X", "Aporte voluntario", "Makes T2R2-048 and T2R2-049 relevant."),
    ("VCT", "blank / X", "Variacion centros de trabajo",
     "Makes T2R2-091 and T2R2-092 mandatory and may change the occupational-risk rate."),
    ("IRL", "00 to 30", "Dias de incapacidad por accidente de trabajo o enfermedad laboral",
     "NOT a flag - a DAY COUNT. Makes T2R2-093 and T2R2-094 mandatory when non-zero."),

    "EXONERACION ART. 114-1 E.T. (A1-033 and T2R2-076)",
    ("S", "SI", "Exonerado", "The employer (A1-033) or the individual contributor (T2R2-076) is "
     "exonerated from EMPLOYER health 8.5%, SENA 2% and ICBF 3%. Introduced by Ley 1607 de 2012 and "
     "confirmed by Ley 1819 de 2016 art. 65."),
    ("N", "NO", "No exonerado", "Full employer contributions due. MANDATORY value where the health "
     "base (T2R2-043) reaches 10 SMMLV = COP 17,509,050 in 2026, and where a natural-person employer "
     "employs two or more workers and the base reaches 10 SMMLV."),
    ("(never exonerated)", "-", "Pension, riesgos laborales y CCF",
     "The art. 114-1 exoneration does NOT touch pension 12%, occupational risk, or the family "
     "compensation fund 4%. Only the Ley 1429 de 2010 art. 5 regime (A1-034) gives relief on the CCF."),

    "TARIFAS 2026",
    ("16.0000%", "Pension", "Cotizacion total a pensiones",
     "Employer 12% + employee 4%. Ley 100 art. 20 as substituted by Ley 797 de 2003 art. 7. Base "
     "floor 1 SMMLV = COP 1,750,905; ceiling 25 SMMLV = COP 43,772,625."),
    ("12.5000%", "Salud", "Cotizacion total a salud",
     "Employer 8.5% + employee 4%. Where the exoneration applies, the rate REPORTED in T2R2-054 is "
     "the employee rate alone, 4.0000% (annex s.2.1.2.3.21)."),
    ("1.0000%", "FSP solidaridad", "Fondo de solidaridad pensional - subcuenta de solidaridad",
     "Employee-borne, from a base of 4 SMMLV = COP 7,003,620."),
    ("0.2000% - 1.0000%", "FSP subsistencia", "Subcuenta de subsistencia",
     "Employee-borne, banded, from a base of 16 SMMLV = COP 28,014,480."),
    ("0.3480% - 8.7000%", "Riesgos laborales", "Cotizacion a riesgos laborales",
     "Employer-borne in full. By risk class of the WORK CENTRE."),
    ("4.0000%", "CCF", "Caja de compensacion familiar",
     "Employer-borne. NEVER exonerated under art. 114-1."),
    ("2.0000%", "SENA", "Servicio Nacional de Aprendizaje",
     "Employer-borne on the PARAFISCAL base (campo 95). Exonerated under art. 114-1."),
    ("3.0000%", "ICBF", "Instituto Colombiano de Bienestar Familiar",
     "Employer-borne on the parafiscal base. Exonerated under art. 114-1."),

    "CLASES DE RIESGO LABORAL (T2R2-078) - Decreto 1772 de 1994 art. 13",
    ("I", "0.522%", "Riesgo minimo", "Initial rate 0.522%; range 0.348% to 0.696%. Offices, "
     "financial services, commerce."),
    ("II", "1.044%", "Riesgo bajo", "Initial rate 1.044%; range 0.435% to 1.653%. Light "
     "manufacturing, textiles."),
    ("III", "2.436%", "Riesgo medio", "Initial rate 2.436%; range 0.783% to 4.089%. Heavier "
     "manufacturing, food processing."),
    ("IV", "4.350%", "Riesgo alto", "Initial rate 4.350%. RECORDED DEFECT: Decreto 1072 de 2015 "
     "art. 2.2.4.3.5 prints the class IV initial rate inconsistently with the Decreto 1772 de 1994 "
     "art. 13 table. Use the Decreto 1772 values."),
    ("V", "6.960%", "Riesgo maximo", "Initial rate 6.960%; maximum 8.7%."),
    ("(work centre)", "-", "-", "The class attaches to the WORK CENTRE, not to the employer "
     "(Decreto 1072 de 2015 art. 2.2.4.2.5.6). A company with two work centres legitimately carries "
     "two classes; a person performing several occupations contributes at the HIGHEST class."),

    "BANDAS DEL FONDO DE SOLIDARIDAD PENSIONAL (T2R2-051, T2R2-052)",
    ("4 to 16 SMMLV", "1.0% / 0%", "Solo solidaridad", "COP 7,003,620 to 28,014,480."),
    ("16 to 17 SMMLV", "1.0% / 0.2%", "Solidaridad + subsistencia", "Total 1.2%."),
    ("17 to 18 SMMLV", "1.0% / 0.4%", "Solidaridad + subsistencia", "Total 1.4%."),
    ("18 to 19 SMMLV", "1.0% / 0.6%", "Solidaridad + subsistencia", "Total 1.6%."),
    ("19 to 20 SMMLV", "1.0% / 0.8%", "Solidaridad + subsistencia", "Total 1.8%."),
    ("above 20 SMMLV", "1.0% / 1.0%", "Solidaridad + subsistencia", "Total 2.0%, to the 25-SMMLV "
     "ceiling."),

    "DIVIPOLA (DANE) - A1-012 / A1-013 / T2R2-009 / T2R2-010",
    ("11", "BOG-DPTO", "Bogota D.C. - departamento", "TWO-digit department code."),
    ("001", "BOG-MPIO", "Bogota D.C. - municipio", "THREE-digit municipality suffix. PILA carries "
     "the department and the municipality in SEPARATE fields, whereas the nomina electronica carries "
     "the five-digit combined code (11001). Concatenate to convert."),
    ("(catalogue)", "-", "Division Politica y Administrativa - DIVIPOLA",
     "Issued by DANE. The operador validates every code against it. Blank where the 'Colombiano en "
     "el exterior' flag is marked or the contributor type is 40."),

    "CIIU REV. 4 A.C. (A1-014)",
    ("(4 digits)", "-", "Codigo DANE de la actividad economica",
     "CIIU revision 4 adapted for Colombia, DANE Resolucion 66 de 2012 or its successor. The SAME "
     "classification drives the DIAN self-withholding rate at Formulario 350 casilla 27."),

    "OPERADORES DE INFORMACION (A1-028, T2R1-022)",
    ("(2 digits)", "-", "Codigo del operador de informacion",
     "Assigned by the operador's own system. Operadores are private entities licensed by the "
     "Ministerio de Salud y Proteccion Social. The employer chooses one commercially; the code is "
     "therefore client-specific and must be obtained at implementation, not configured from a "
     "national catalogue."),

    "ADMINISTRADORAS (ARL / EPS / AFP / CCF) - 6-position codes",
    ("(6 positions)", "-", "Codigos de administradoras",
     "T2R1-014 (employer ARL), T2R2-031 / 032 (AFP), T2R2-033 / 034 (EPS), T2R2-035 (CCF) and "
     "T2R2-077 (employee ARL) are all SIX positions. The catalogue is maintained by the Ministry and "
     "distributed through the operadores de informacion; the placeholders used in the worked example "
     "(AFP001, EPS001, CCF001, ARL001) are illustrative only and MUST be replaced with the real "
     "codes obtained from the client's operador."),
]

# ===========================================================================
#  SHEET 7 - POPULATION RULES
# ===========================================================================
CFG["population"] = [
    "MANDATORY FIELD RULES",
    ("The five contribution bases (T2R2-042 to T2R2-045 and T2R2-095)", "Payroll engine",
     "Compute and STORE five separate bases per employee per month. Four are the IBC for pension, "
     "health, occupational risk and the CCF: total salary-constituting payments, plus the excess "
     "over the 40% non-salary clamp of Ley 1393 de 2010 art. 30, floored at 1 SMMLV "
     "(COP 1,750,905) and capped at 25 SMMLV (COP 43,772,625). The fifth is the PARAFISCAL base of "
     "campo 95, defined by Ley 21 de 1982 art. 17: it INCLUDES paid rest days and it is UNCAPPED. "
     "Never populate all five from one variable.",
     "The four IBC values legitimately differ from one another once a change event enters - for "
     "example health may remain payable during an unpaid leave where pension does not. The header "
     "total in T2R1-020 is the sum of campo 95, NOT of campo 45; using the CCF base there is a "
     "silent, systematic understatement for any employer whose employees earn above the ceiling or "
     "who has significant paid rest days."),
    ("The four day counts (T2R2-036 to T2R2-039)", "Payroll engine",
     "Maintain a contributory-day counter PER SUBSYSTEM on the 30-day commercial month. Start at 30 "
     "(or the proportion from a mid-month hire or to a mid-month leave), then apply the change "
     "events: SLN and lawful strike reduce all four; IGE and IRL follow the subsystem-specific "
     "rules; vacation and remunerated leave do not reduce them at all because they are paid.",
     "February is 30 days and a 31-day month is 30 days. The counts must reconcile to the novedad "
     "date pairs: a five-day SLN in a full month gives 25 contributory days and dates in T2R2-083 "
     "and T2R2-084 that span exactly five days."),
    ("Health period one month ahead (T2R1-016)", "Engine (control)",
     "Set the health payment period to the month AFTER the period in T2R1-015. Health is paid one "
     "month in advance; the other subsystems are paid in arrears. A March salary settlement carries "
     "period 2026-03 in T2R1-015 and 2026-04 in T2R1-016.",
     "Setting the two equal is the single most common first-run defect. Note also the split of "
     "responsibility the annex records: T2R1-015 is CALCULATED BY THE OPERADOR, while T2R1-016 is "
     "SUPPLIED BY THE EMPLOYER."),
    ("Exoneration flags (A1-033 and T2R2-076)", "Engine (control)",
     "A1-033 is an EMPLOYER-LEVEL, standing declaration that the employer qualifies under ET "
     "art. 114-1. T2R2-076 is a PER-EMPLOYEE, PER-MONTH application of it, and may be S only where "
     "A1-033 is S. The employee test is that the health base (T2R2-043) is BELOW 10 SMMLV = "
     "COP 17,509,050 in 2026; at or above that it MUST be N. Where a NATURAL-person employer employs "
     "two or more workers and the base reaches 10 SMMLV it must also be N. Where T2R2-076 is S, set "
     "T2R2-054 to the EMPLOYEE rate alone (4.0000%), and set the SENA and ICBF rates and values "
     "(T2R2-066 to T2R2-069) to zero.",
     "Because the test is MONTHLY, an employee who crosses 10 SMMLV in a bonus month loses the "
     "exoneration for that month alone and regains it the next. Evaluating it annually, or at hire, "
     "systematically under-contributes. The same test drives Formulario 350 casilla 27."),

    "CRITICAL VALIDATION RULES",
    ("Header-to-detail consistency", "Engine (validation)",
     "Before submission assert: T2R1-004, 005, 006 and 007 equal Archivo Tipo 1 campos 1, 2, 3 and "
     "4 byte for byte; T2R1-011, 012 and 013 equal Archivo Tipo 1 campos 10, 5 and 6; T2R1-021 "
     "equals Archivo Tipo 1 campo 30; T2R1-019 equals the count of UNIQUE contributors in the "
     "detail EXCLUDING those with contributor type 40; and T2R1-020 equals the sum of T2R2-095 "
     "across the detail.",
     "The type-40 exclusion from the contributor count is easy to miss and produces a "
     "header-to-detail mismatch the operador rejects outright."),
    ("Pension rate forced to zero", "Engine (validation)",
     "Where the contributor sub-type (T2R2-006) is 1, 2, 3, 4, 5, 6, 9 or 12, the pension rate "
     "(T2R2-046) MUST be 0 and no pension contribution may be settled.",
     "The nomina electronica equivalent is narrower - only SubTipoTrabajador 01 forces the rate to "
     "zero there. Map between the two lists; do not assume they agree."),
    ("Health rate may be zero only in two cases", "Engine (validation)",
     "The annex is explicit: T2R2-054 may be reported as zero ONLY where (a) SLN (T2R2-024) is X and "
     "the exoneration flag (T2R2-076) is S, or (b) SLN is C and the employer's legal nature is "
     "public. And where the health contribution (T2R2-055) is zero, the health days (T2R2-037), the "
     "health base (T2R2-043) and the health rate (T2R2-054) must ALL be zero - except for those same "
     "SLN-plus-exoneration contributors.",
     "This is a four-field interlock. Implement it as one validation, not four independent ones."),
    ("Novedad flag to date-pair interlock", "Engine (validation)",
     "Every marked novedad flag must have its corresponding date field or pair populated, and every "
     "populated date field must have its flag marked: ING to 080, RET to 081, VSP to 082, SLN to "
     "083 and 084, IGE to 085 and 086, LMA to 087 and 088, VAC-LR to 089 and 090, VCT to 091 and "
     "092, IRL days to 093 and 094, TAE to 034, TAP to 032, AVP to 048 and 049.",
     "Build the interlock as a table, not as a chain of conditionals - there are twelve pairs and a "
     "missed one produces a rejection at the operador rather than at Mercans."),
    ("Contribution calculation checks published in the annex", "Engine (validation)",
     "The annex prints the arithmetic the operador will apply: campo 55 = campo 43 x campo 54; "
     "campo 65 = campo 45 x campo 64; campo 67 = campo 95 x campo 66; campo 69 = campo 95 x campo "
     "68; campo 71 = campo 95 x campo 70; campo 73 = campo 95 x campo 72. Note that the CCF uses "
     "the CCF base while SENA, ICBF, ESAP and MEN all use the PARAFISCAL base.",
     "Reproduce these checks internally before submission. Each must then be rounded UP to the next "
     "multiple of 100."),

    "AMOUNT FORMAT RULES",
    ("Rounding is UP, not to nearest", "Engine (formatting)",
     "Round the contribution base UP to the whole peso, and round EACH contribution value UP to the "
     "next multiple of 100 (Decreto 1990 de 2016 art. 1). Worked illustration: occupational risk at "
     "class I on a base of 12,000,000 is 0.522% = 62,640, which becomes 62,700.",
     "This is neither the nomina electronica convention (2 decimals, round-half-to-even) nor the "
     "Formulario 350 convention (nearest 1,000). Blending them produces reconciliation differences "
     "that look like errors but are not - the reconciliation must be run on the UNROUNDED values "
     "with a tolerance."),
    ("Numeric and alphanumeric justification", "Engine (formatting)",
     "Numeric fields are right-justified and ZERO-filled to the left; alphanumeric fields are "
     "left-justified and SPACE-filled to the right. The annex states this at s.0 and it applies "
     "without exception across all three records.",
     "An empty numeric field is a run of zeros, not a run of spaces. This catches optional numeric "
     "fields such as A1-016 (Fax) and the unused parafiscal rate and value fields."),
    ("Rate fields carry implied decimals", "Engine (formatting)",
     "The rate fields are numeric with implied decimals in their published width - seven positions "
     "for T2R2-046, 054, 064, 066, 068, 070 and 072, and nine for T2R2-061. Confirm the implied "
     "decimal placement with the chosen operador before go-live; the annex does not print it "
     "unambiguously for every rate field.",
     "FORMAT TO CONFIRM. This is the one presentation detail of the layout that the annex leaves "
     "under-specified, and it differs between the seven-position and nine-position rate fields."),

    "PAYROLL-SPECIFIC POPULATION RULES",
    ("The 40% non-salary clamp", "Payroll engine",
     "Total the salary and the non-salary payments for the period. Where non-salary payments exceed "
     "40% of total remuneration, add the EXCESS back into the four contribution bases (Ley 1393 de "
     "2010 art. 30). Store the added-back amount as its own quantity: it is IN the contribution base "
     "but OUT of the statutory-benefit base for cesantias, prima and the severance indemnity.",
     "The clamp is computed on the period's totals, so a single large non-salary bonus can push an "
     "otherwise compliant employee over the line for one month. It also interacts with the "
     "exoneration test, because the added-back amount raises the health base toward the 10-SMMLV "
     "threshold."),
    ("All-inclusive salary at 70%", "Payroll engine",
     "Where the employee is on salario integral (CST art. 132 num. 2, minimum 13 SMMLV = "
     "COP 22,761,765 in 2026), mark T2R2-041 and set the four IBC fields to 70% of the integral "
     "salary. The remaining 30% is the statutory prestacional factor and is not a contribution base.",
     "Note the interaction with the ceiling: 70% of a large integral salary can still exceed 25 "
     "SMMLV, in which case the ceiling applies to the 70% figure, not to the full salary."),
    ("Work centre and risk class", "Employee master data",
     "Carry the work centre on the employee record and derive the risk class from it, not from the "
     "employer. Where an employee performs several occupations, contribute at the HIGHEST class "
     "(Decreto 1072 de 2015 art. 2.2.4.2.5.6). Where the employee moves work centre mid-period, mark "
     "VCT (T2R2-029) and populate T2R2-091 and T2R2-092.",
     "A mid-period move can change the ARL rate. Confirm with the operador whether the period is "
     "settled at one rate or split - the annex does not prescribe a split, so market practice "
     "governs."),
    ("Foreign employee electing out of pension", "Employee master data",
     "Mark T2R2-007 where the employee is a foreign national who has proved affiliation to a pension "
     "system abroad and elected out under Decreto 1072 de 2015 art. 2.2.1.2.1.4. Health, "
     "occupational risk and the parafiscal levies remain fully payable. The election narrows the "
     "valid document types to CE, PA, CD, SC and PE.",
     "THIS IS NOT A TAX FIELD. It says nothing about tax residence: the same employee may be "
     "withheld at the flat 20% of ET art. 408 on hoja 2 of Formulario 350 while contributing to "
     "Colombian health and occupational risk on ordinary terms."),
    ("Incapacity and leave advanced by the employer", "Payroll engine",
     "Colombian employers universally ADVANCE the EPS and ARL benefits through payroll and recover "
     "from the institution. Report the IGE and LMA authorisation numbers (T2R2-057, T2R2-059) and "
     "values (T2R2-058, T2R2-060), and model the benefit as PAID to the employee and RECEIVABLE from "
     "the institution.",
     "Without the authorisation number the institution will not reimburse. CO-GAP-03 and CO-GAP-04: "
     "the employer's first-two-days rate for general illness (Mercans default 66.67%) and the "
     "one-minimum-wage floor on incapacity pay are configurable and need the client's documented "
     "election."),

    "CROSS-FIELD VALIDATIONS",
    ("A1-009 drives A1-004, A1-018, A1-020, A1-021 and A1-023", "Engine (validation)",
     "Where the employer person type is J, the verification digit and the legal representative's "
     "identification number, document type, first surname and first name are all mandatory. Where "
     "it is N, the verification digit must be ZERO and the legal-representative block is optional.",
     "Note the asymmetry: A1-019 (the representative's own verification digit) is ALWAYS zero "
     "whatever the person type, because the annex says so expressly."),
    ("A1-010 drives A1-005 and A1-006", "Engine (validation)",
     "Where the form of presentation is U, the branch code and name must be BLANK. Where it is S, "
     "both must be populated - and where the branch has no name, the annex directs that the CODE be "
     "repeated in the name field.",
     "The same interlock repeats at T2R1-011, T2R1-012 and T2R1-013."),
    ("T2R1-008 drives T2R1-009 and T2R1-010", "Engine (validation)",
     "Where the planilla type is E, A, I, M, S, Y, T, X or K, both associated-planilla fields must "
     "be blank (or zero for the numeric one). Where it is N or F they carry the period planilla; "
     "where it is U, the judicial deposit title; where it is J or O, the planilla of the original "
     "payment.",
     "The annex adds that where the operador cannot find the initial planilla for that contributor "
     "and period, it must NOT permit the correction planilla at all."),
    ("A1-007 = D drives A1-031, A1-032 and A1-034", "Engine (validation)",
     "A Ley 1429 de 2010 beneficiary must carry the commercial-registry date and the registered "
     "department, and the registry date must fall between 29 December 2010 and 31 December 2014.",
     "The window is closed and historical: an employer registered after 2014 cannot be class D, "
     "whatever its size."),
    ("T2R2-008 drives T2R2-009, T2R2-010 and T2R2-097", "Engine (validation)",
     "Where 'Colombiano en el exterior' is marked, the DIVIPOLA work-location department and "
     "municipality must be BLANK and the foreign filing date becomes relevant. The flag is available "
     "only for document types CC and TI.",
     "Contributor type 40 also blanks the two DIVIPOLA fields, for a different reason."),
    ("Cross-report reconciliation", "Engine (reconciliation)",
     "After settlement assert: T2R2-055 (employee portion) reconciles to nomina electronica NIE163; "
     "the employee 4% within T2R2-047 reconciles to NIE166; T2R2-051 and T2R2-052 reconcile to "
     "NIE168 and NIE170. Reconcile on the UNROUNDED values with a tolerance of 100 pesos per "
     "contribution, because PILA rounds up to the next 100 and the XML does not.",
     "The employer-borne amounts - pension 12%, health 8.5%, occupational risk, CCF, SENA, ICBF - "
     "have NO nomina electronica counterpart at all and cannot be reconciled to it. They reconcile "
     "only to the employer-cost ledger."),
]

# ===========================================================================
#  SHEET 8 - EXAMPLE ANALYSIS
# ===========================================================================
CFG["example"] = [
    "WORKED EXAMPLE - MARCH 2026 PLANILLA, ONE CONTRIBUTOR",
    ("(scenario)", "Employer", "MERCANS COLOMBIA S.A.S., NIT 900123456-7, private legal person, "
     "fewer than 200 contributors, exonerated under ET art. 114-1, Bogota D.C.",
     "Same employer as the other five Colombia Spec workbooks."),
    ("(scenario)", "Contributor", "Juan Carlos Perez Gomez, CC 1020304050, dependiente, full month, "
     "salary COP 12,000,000, risk class I.",
     "Below 10 SMMLV (COP 17,509,050), so the art. 114-1 exoneration applies; at or above 4 SMMLV "
     "(COP 7,003,620), so the solidarity surcharge applies; below 16 SMMLV, so the subsistence "
     "surcharge does not."),

    "ARCHIVO TIPO 1 - KEY FIELDS",
    ("NI / 900123456 / 7", "A1-002 / A1-003 / A1-004",
     "Employer document type, number and verification digit.",
     "The DV is mandatory because A1-009 = J. All three are echoed byte for byte into T2R1-005, "
     "T2R1-006 and T2R1-007."),
    ("B", "A1-007 - Clase de aportante", "Fewer than 200 contributors, counted across all branches.",
     "Class C would require the operador to verify MONTHLY against the DIAN file under Decreto 525 "
     "de 2009 art. 6; class D would require a commercial-registry date between 29 Dec 2010 and "
     "31 Dec 2014."),
    ("J / U", "A1-009 / A1-010", "Legal person; single consolidated planilla.",
     "U forces the branch code and name (A1-005, A1-006) to be blank, here and in T2R1-012 and "
     "T2R1-013."),
    ("11 / 001", "A1-013 / A1-012", "Department 11, municipality 001 - Bogota D.C.",
     "PILA splits DIVIPOLA across two fields; the nomina electronica carries the combined five-digit "
     "code 11001. Concatenate department + municipality to convert."),
    ("0", "A1-019 - DV del representante legal", "ALWAYS zero.",
     "The annex says expressly 'Este campo se debera reportar en cero'. Do not compute a check digit "
     "for the representative - a genuinely counter-intuitive rule."),
    ("S", "A1-033 - Aportante exonerado", "The employer declares the ET art. 114-1 exoneration.",
     "This is the standing employer-level declaration. It is applied per employee per month at "
     "T2R2-076, and it rests on the same test as Formulario 350 casilla 27."),
    ("N", "A1-034 - Beneficios art. 5 Ley 1429", "Not a Ley 1429 beneficiary.",
     "Distinct from A1-033: the CCF 4% is NEVER exonerated under art. 114-1, so this is the only "
     "route to relief on it."),

    "ARCHIVO TIPO 2, REGISTRO TIPO 1 - KEY FIELDS",
    ("01 / 1 / E", "T2R1-001 / T2R1-002 / T2R1-008",
     "Header record, electronic modality, planilla de empleados.",
     "Record type 01 distinguishes the header from the 02 detail records in the same file."),
    ("2026-03 / 2026-04", "T2R1-015 / T2R1-016",
     "Pension, occupational risk and levies for March; HEALTH FOR APRIL.",
     "COLOMBIA'S MOST-MISSED PILA RULE. Health is paid one month in advance. Setting these equal is "
     "the classic first-run defect. Note also that T2R1-015 is calculated by the OPERADOR while "
     "T2R1-016 is supplied by the EMPLOYER."),
    ("00001", "T2R1-019 - Numero total de cotizantes", "One contributor.",
     "Must exclude any contributor whose type (T2R2-005) is 40 - Beneficiario UPC Adicional."),
    ("000012000000", "T2R1-020 - Valor total de la nomina",
     "The sum of the PARAFISCAL base (T2R2-095) across the detail - not the CCF base.",
     "The annex defines it as 'la sumatoria de los IBC para el pago de los aportes de PARAFISCALES'. "
     "Using campo 45 instead of campo 95 is a silent, systematic understatement for any employer "
     "with employees above the ceiling or with material paid rest days."),

    "ARCHIVO TIPO 2, REGISTRO TIPO 2 - BASES AND DAYS",
    ("30 / 30 / 30 / 30", "T2R2-036 to T2R2-039",
     "Full contributory month for pension, health, occupational risk and the CCF.",
     "Four SEPARATE counters. They diverge as soon as a change event enters - a five-day SLN gives "
     "25 and a date pair spanning exactly five days."),
    ("012000000 x4", "T2R2-042 to T2R2-045",
     "The four IBC values, all COP 12,000,000 in this simple month.",
     "Between the floor of 1 SMMLV (COP 1,750,905) and the ceiling of 25 SMMLV (COP 43,772,625). "
     "They coincide here only because there is no non-salary payment and no change event."),
    ("012000000", "T2R2-095 - IBC otros parafiscales",
     "The FIFTH base, for SENA, ICBF, ESAP and MEN.",
     "Defined by Ley 21 de 1982 art. 17: includes paid rest days and is UNCAPPED. Equal to the "
     "others here, but it diverges as soon as the employee earns above the ceiling."),

    "REGISTRO TIPO 2 - PENSION",
    ("0160000", "T2R2-046 - Tarifa de aportes pensiones",
     "16% total - employer 12% plus employee 4%.",
     "Would be forced to 0 if the contributor sub-type were 1, 2, 3, 4, 5, 6, 9 or 12."),
    ("001920000", "T2R2-047 - Cotizacion obligatoria a pensiones",
     "16% of COP 12,000,000 = COP 1,920,000. Already a multiple of 100.",
     "THE WHOLE contribution, employer and employee together. The nomina electronica reports only "
     "the employee's 4% (COP 480,000) at NIE166 - the two figures are not interchangeable."),
    ("000120000", "T2R2-051 - FSP subcuenta de solidaridad",
     "1% of COP 12,000,000 = COP 120,000, because the base is at or above 4 SMMLV.",
     "Employee-borne and ADDITIONAL to the 4% pension. Reconciles to nomina electronica NIE168. "
     "Reported SEPARATELY from pension in both artefacts - merging them is the most common Colombian "
     "mapping error."),
    ("000000000", "T2R2-052 - FSP subcuenta de subsistencia",
     "Nil: the base is below 16 SMMLV (COP 28,014,480).",
     "The two sub-accounts have DIFFERENT triggers - 4 SMMLV and 16 SMMLV."),

    "REGISTRO TIPO 2 - HEALTH AND THE EXONERATION",
    ("S", "T2R2-076 - Cotizante exonerado de pago",
     "The employee earns below 10 SMMLV and the employer has declared itself exonerated in A1-033.",
     "TESTED MONTHLY. A bonus that pushes this employee above COP 17,509,050 in one month forces "
     "this field to N for that month alone."),
    ("0040000", "T2R2-054 - Tarifa de aportes salud",
     "4% - THE EMPLOYEE RATE ALONE, because the exoneration applies.",
     "The annex directs at s.2.1.2.3.21 that where A1-033 and T2R2-076 are both S, the rate to enter "
     "here is 'la tarifa correspondiente al trabajador'. Without the exoneration this field would "
     "read 0125000 (12.5%) and the contribution would be COP 1,500,000."),
    ("000480000", "T2R2-055 - Cotizacion obligatoria a salud",
     "4% of COP 12,000,000 = COP 480,000. The annex's own check is campo 43 x campo 54.",
     "Reconciles to nomina electronica NIE163, which reports the same COP 480,000 - here they "
     "coincide because the figure is already a multiple of 100."),

    "REGISTRO TIPO 2 - OCCUPATIONAL RISK AND LEVIES",
    ("1 / 000005220", "T2R2-078 / T2R2-061", "Risk class I, rate 0.522%.",
     "The class attaches to the WORK CENTRE (T2R2-062), not to the employer."),
    ("000062700", "T2R2-063 - Cotizacion obligatoria riesgos laborales",
     "0.522% of COP 12,000,000 = COP 62,640, ROUNDED UP to the next multiple of 100 = COP 62,700.",
     "THE CLEAREST ILLUSTRATION OF THE PILA ROUNDING CONVENTION. Decreto 1990 de 2016 art. 1 rounds "
     "UP, never to nearest. Employer-borne in full - there is no employee occupational-risk "
     "deduction in Colombia, which is why no nomina electronica element corresponds to it."),
    ("0040000 / 000480000", "T2R2-064 / T2R2-065", "CCF at 4% of COP 12,000,000 = COP 480,000.",
     "NEVER exonerated under art. 114-1. Only the Ley 1429 art. 5 regime gives relief on the CCF, "
     "and this employer has declared N at A1-034."),
    ("0000000 / 000000000", "T2R2-066 / T2R2-067", "SENA at 0% and nil.",
     "Exonerated under ET art. 114-1 because T2R2-076 is S. Without the exoneration this would be "
     "2% of the PARAFISCAL base = COP 240,000."),
    ("0000000 / 000000000", "T2R2-068 / T2R2-069", "ICBF at 0% and nil.",
     "Exonerated. Without it, 3% of the parafiscal base = COP 360,000. The exoneration is therefore "
     "worth COP 1,620,000 a month for this one employee - health 1,020,000 plus SENA 240,000 plus "
     "ICBF 360,000."),
    ("0 / 0", "T2R2-070 to T2R2-073", "ESAP and MEN at nil.",
     "Public-sector levies. Out of scope for private corporate payroll, but the positions remain in "
     "the record and must be zero-filled."),

    "CROSS-REPORT RECONCILIATION FROM THIS PLANILLA",
    ("480000", "= nomina electronica NIE163", "Employee health.",
     "Coincides exactly here. It will differ by up to 99 pesos where the raw figure is not a "
     "multiple of 100 - PILA rounds up, the XML does not."),
    ("480000 (4% within 1,920,000)", "= nomina electronica NIE166", "Employee pension.",
     "The XML reports the employee 4% alone; PILA campo 47 reports the whole 16%. Derive, do not "
     "copy."),
    ("120000", "= nomina electronica NIE168", "Solidarity fund.",
     "Reported separately in both artefacts. Never merged into pension."),
    ("(no counterpart)", "Employer 12% pension, 8.5% health, ARL, CCF, SENA, ICBF",
     "COP 1,440,000 + 0 + 62,700 + 480,000 + 0 + 0 = COP 1,982,700 of employer cost.",
     "None of this appears on the nomina electronica, which reports only what the employee accrued "
     "and what was deducted from the employee. It reconciles to the employer-cost ledger alone."),
]

# ===========================================================================
#  SHEET 9 - SAMPLE FILE (generated from the official position table)
# ===========================================================================
CFG["sample_title"] = "FIXED-WIDTH RECORDS GENERATED FROM THE OFFICIAL POSITION TABLE"

_sample_lines = [
    "PROVENANCE NOTE - READ FIRST",
    "============================",
    "The three records below were GENERATED PROGRAMMATICALLY by placing each",
    "value at the position published in the official Anexo Tecnico 2 (Resolucion",
    "MSPS 2388 de 2016, AT2 version 09, 16-09-2019) and applying the annex's own",
    "justification rules - numeric fields right-justified and zero-filled,",
    "alphanumeric fields left-justified and space-filled.",
    "",
    "The record lengths are therefore EXACT, not approximate:",
    "    Archivo Tipo 1                   %d characters (annex total: 567)" % len(_REC_A1),
    "    Archivo Tipo 2, Registro Tipo 1  %d characters (annex total: 359)" % len(_REC_T2R1),
    "    Archivo Tipo 2, Registro Tipo 2  %d characters (annex total: 686)" % len(_REC_T2R2),
    "",
    "This is NOT an official MSPS sample file - none is published - but the",
    "LAYOUT is the official layout, byte for byte. What each operador de",
    "informacion wraps around these two files, and what additional validations it",
    "applies, is operador-specific and must be confirmed before go-live.",
    "",
    "Administradora codes (AFP001, EPS001, CCF001, ARL001) are PLACEHOLDERS. The",
    "real six-position codes come from the client's chosen operador.",
    "",
    "Values are the worked example on the Example Analysis sheet: MERCANS",
    "COLOMBIA S.A.S., NIT 900123456-7, one contributor on COP 12,000,000 for",
    "March 2026, exonerated under ET art. 114-1, risk class I.",
    "",
    "-" * 79,
    "1. ARCHIVO TIPO 1 - DATOS GENERALES DEL APORTANTE",
    "-" * 79,
]
_sample_lines += _wrapped("Record", _REC_A1)
_sample_lines += [
    "",
    "  Reading of the key positions:",
    "    pos 1-200    MERCANS COLOMBIA S.A.S. (space-filled)",
    "    pos 201-202  NI    - tipo documento del aportante",
    "    pos 203-218  900123456 (space-filled) - numero de identificacion",
    "    pos 219      7     - digito de verificacion (mandatory because campo 9 = J)",
    "    pos 220-269  blank - no branch, because campo 10 = U",
    "    pos 270      B     - clase de aportante, fewer than 200 contributors",
    "    pos 271      2     - naturaleza juridica, privada",
    "    pos 272      J     - tipo persona, juridica",
    "    pos 273      U     - forma de presentacion, unico",
    "    pos 314-316  001   - codigo municipio (three digits, PILA style)",
    "    pos 317-318  11    - codigo departamento",
    "    pos 319-322  6920  - codigo DANE actividad economica, zero-filled numeric",
    "    pos 419      0     - DV del representante legal: ALWAYS zero per the annex",
    "    pos 545-551  2026-03 - periodo de pago (see the RA query on the N/format conflict)",
    "    pos 566      S     - APORTANTE EXONERADO de salud, SENA e ICBF (art. 114-1)",
    "    pos 567      N     - no acoge los beneficios del art. 5 de la Ley 1429",
    "",
    "-" * 79,
    "2. ARCHIVO TIPO 2, REGISTRO TIPO 1 - ENCABEZADO",
    "-" * 79,
]
_sample_lines += _wrapped("Record", _REC_T2R1)
_sample_lines += [
    "",
    "  Reading of the key positions:",
    "    pos 1-2      01    - tipo de registro (header)",
    "    pos 3        1     - modalidad electronica",
    "    pos 8-207    MERCANS COLOMBIA S.A.S. - must equal Archivo Tipo 1 campo 1",
    "    pos 227      E     - planilla de empleados",
    "    pos 299-304  ARL001 - codigo ARL del aportante (six positions)",
    "    pos 305-311  2026-03 - periodo pension / riesgos laborales / parafiscales",
    "    pos 312-318  2026-04 - PERIODO SALUD, one month AHEAD. The classic defect",
    "                           is setting these two equal.",
    "    pos 339-343  00001 - numero total de cotizantes (excludes tipo cotizante 40)",
    "    pos 344-355  000012000000 - valor total de la nomina = SUM of campo 95,",
    "                           the PARAFISCAL base, not the CCF base",
    "",
    "-" * 79,
    "3. ARCHIVO TIPO 2, REGISTRO TIPO 2 - LIQUIDACION DETALLADA (one per contributor)",
    "-" * 79,
]
_sample_lines += _wrapped("Record", _REC_T2R2)
_sample_lines += [
    "",
    "  Reading of the key positions:",
    "    pos 1-2      02    - tipo de registro (detail)",
    "    pos 3-7      00001 - secuencia, starts at 00001 and is strictly sequential",
    "    pos 8-9      CC    - tipo documento del cotizante (two LETTERS; the nomina",
    "                         electronica uses the NUMERIC code 13 for the same thing)",
    "    pos 10-25    1020304050 - numero de identificacion",
    "    pos 26-27    01    - tipo cotizante, dependiente",
    "    pos 28-29    00    - subtipo, no aplica",
    "    pos 137-153  blank / 00 - no novedades this month; IRL is a DAY COUNT, not a flag",
    "    pos 154-159  AFP001 - administradora de pensiones (six positions)",
    "    pos 166-171  EPS001 - EPS",
    "    pos 178-183  CCF001 - caja de compensacion familiar",
    "    pos 184-191  30 30 30 30 - the FOUR separate contributory-day counters",
    "    pos 192-200  012000000 - salario basico",
    "    pos 202-237  012000000 x4 - the four IBC values (pension, salud, ARL, CCF)",
    "    pos 238-244  0160000 - tarifa pension 16% (employer 12 + employee 4)",
    "    pos 245-253  001920000 - cotizacion obligatoria a pensiones, the WHOLE 16%",
    "    pos 281-289  000120000 - FSP subcuenta de solidaridad, 1%, employee-borne",
    "    pos 290-298  000000000 - FSP subsistencia nil: base is below 16 SMMLV",
    "    pos 308-314  0040000 - tarifa salud 4%: the EMPLOYEE rate alone, because the",
    "                           art. 114-1 exoneration applies (annex s.2.1.2.3.21)",
    "    pos 315-323  000480000 - cotizacion salud = IBC salud x tarifa",
    "    pos 381-389  000005220 - tarifa riesgos laborales, class I, 0.522%",
    "    pos 399-407  000062700 - cotizacion ARL: 0.522% of 12,000,000 = 62,640,",
    "                           ROUNDED UP to the next multiple of 100 = 62,700",
    "    pos 408-423  0040000 / 000480000 - CCF 4%, NEVER exonerated",
    "    pos 424-455  zeros - SENA and ICBF nil under the art. 114-1 exoneration",
    "    pos 456-487  zeros - ESAP and MEN, public sector only",
    "    pos 506      S     - COTIZANTE EXONERADO de salud, SENA e ICBF",
    "    pos 507-512  ARL001 - ARL del afiliado",
    "    pos 513      1     - clase de riesgo I",
    "    pos 515-524  2021-01-11 - fecha de ingreso",
    "    pos 665-673  012000000 - IBC OTROS PARAFISCALES (the fifth base, uncapped)",
    "    pos 674-676  000   - horas laboradas (only for tipo cotizante 51)",
    "    pos 677-686  blank - fecha radicacion en el exterior; closes the record at 686",
    "",
    "-" * 79,
    "4. TOTALS RECORDS - GENERATED BY THE OPERADOR, NOT BY THE EMPLOYER",
    "-" * 79,
    "Registro Tipo 3   Total aportes del periodo para pensiones",
    "Registro Tipo 4   Total aportes al fondo de solidaridad pensional",
    "Registro Tipo 5   Total aportes para salud",
    "Registro Tipo 6   Total aportes para riesgos laborales",
    "Registro Tipo 7   Total aportes para cajas de compensacion familiar",
    "Registro Tipo 8   Total aportes al SENA",
    "Registro Tipo 9   Total aportes al ICBF",
    "Registro Tipo 10  Total aportes a la ESAP",
    "Registro Tipo 11  Total aportes al Ministerio de Educacion Nacional",
    "Registro Tipo 12  Total a pagar durante el periodo",
    "",
    "These records also carry the days-in-arrears count and the interest on",
    "arrears, which the operador computes from the payment date. The employer",
    "neither produces nor validates them - but the ENGINE MUST PARSE THEM from",
    "the settlement response in order to reconcile, capture the planilla number",
    "and payment date, and detect rejected contributor records.",
]

CFG["sample"] = "\n".join(_sample_lines)

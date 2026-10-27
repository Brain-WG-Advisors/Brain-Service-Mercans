# -*- coding: utf-8 -*-
"""CO-CESANTIAS-006 - Sheets 5 to 9 for the annual severance-savings deposit.

The Sheet-9 sample is BUILT PROGRAMMATICALLY from the published 258-position
layout and asserted to be exactly 258 characters, field by field, so that no
position can drift. It is not a fabricated format: every position, length and
padding rule comes from the Simple S.A. 'Manual Cesantias' s. 3.2 held in
00-official-sources/pdfs/pagosimple_cesantias.pdf.
"""

from co_r6_cesantias import CFG

# ===========================================================================
#  SHEET 5 - FILE STRUCTURE (a PUBLISHED layout, not a neutral model)
# ===========================================================================
CFG["filestruct"] = [
    ("##", "SUBMISSION CHANNEL - VERIFIED (v2.7 STEP 3.5)"),
    ("Channel", "TWO channels, both through a licensed operador de informacion, NOT through a "
                "government portal. (A) online_form - 'Planilla En Linea' (SOI) / 'Elaborar "
                "planilla' (Simple S.A.), each employee keyed into the operator's form. (B) "
                "file_upload - 'Liquidacion Por Archivo' (SOI) / 'Envio de Archivo Unificado de "
                "Cesantias' (Simple S.A.). CONFIRMED in both operators' published instructivos."),
    ("Portals verified", "ACH Colombia S.A. (SOI) - www.nuevosoi.com.co, instructivo "
                         "DDS-DES-INS-008 v2. Simple S.A. - www.pagosimple.com, 'Manual "
                         "Cesantias'. The same service is offered by Aportes en Linea, Asopagos, "
                         "Enlace Operativo and MiPlanilla; those were NOT verified and may impose "
                         "an operator-specific layout."),
    ("Authentication", "Portal session with (company document type + number), (user document type "
                       "+ number) and a password. Simple S.A. states the credentials are the SAME "
                       "ones used for PILA. There is NO certificate, NO electronic signature and "
                       "NO machine-to-machine service - contrast CO-DIAN-001, which has a SOAP "
                       "contract, a XAdES signature and a synchronous ApplicationResponse."),
    ("What comes back", "A planilla number (one per fondo where the medio de pago is Pago "
                        "Credito), a pre-payment comprobante in PDF, and after payment the informe "
                        "por fondo / por afiliado / completo in PDF or Excel."),
    ("NOT XML", "No XSD, no cahier des charges and no XML of any kind exists for this filing. The "
                "word XML must not appear against CO-CESANTIAS-006. scope_manifest records the "
                "format as CSV; CSV is accepted by SOI, but the two layouts published at field "
                "level are the fixed-width TXT and the XLS 97-2003, and this Spec is written to "
                "those."),

    ("##", "LAYOUT A - FIXED-WIDTH TXT, 20 FIELDS IN 258 POSITIONS (PUBLISHED)"),
    ("Source", "Simple S.A. 'Manual Cesantias' s. 3.2 - 'Podras cargar un archivo plano o TXT sin "
               "encabezado; los campos deben estar organizados por posiciones'. Extracted to "
               "_txt/pagosimple_cesantias.txt."),
    ("Record model", "FLAT. One record per employee. Record type is the constant '02' in positions "
                     "1-2. There is NO type-01 header record, NO trailer, NO declared record count "
                     "and NO declared control total - the aportante identity and the accrual year "
                     "live in the portal envelope (Spec fields E01-E06), not in the file."),
    ("Encoding and line ending", "Plain text. The instructivo does not state the code page or the "
                                 "line terminator. Write ASCII with no accents and no special "
                                 "characters (both operators reject them in names) and use CRLF, "
                                 "which is what the Windows-oriented tooling in this space "
                                 "expects. FORMAT TO CONFIRM against a real accepted file."),
    ("Size limit", "SOI: a file above 1 MB must be COMPRESSED before upload. At 258 bytes plus a "
                   "terminator per record that is roughly 4,000 employees per uncompressed file."),
    ("Sequence", "Positions 3-7, starts at 00001, consecutive. Maximum 99,999 records."),
    ("", "Campo  Len  Ini  Fin  Type   Field"),
    ("", "  1      2    1    2   N      Tipo de registro                  (constant '02')"),
    ("", "  2      5    3    7   N      Secuencia                         (00001, consecutive)"),
    ("", "  3      2    8    9   A      Tipo de documento del cotizante   (CC/CE/TI/PA/CD/SC/PE)"),
    ("", "  4     16   10   25   N      Numero de identificacion          (right-aligned, 0-filled)"),
    ("", "  5     20   26   45   A      Primer apellido                   (obligatorio)"),
    ("", "  6     20   46   65   A      Segundo apellido"),
    ("", "  7     20   66   85   A      Primer nombre                     (obligatorio)"),
    ("", "  8     20   86  105   A      Segundo nombre"),
    ("", "  9      2  106  107   N      Codigo del Fondo de Cesantias     (02/03/10/15/19)"),
    ("", " 10      3  108  110   N      Numero de dias trabajados         (1 to 360)"),
    ("", " 11      4  111  114   N      Espacio con ceros                 (must contain zeros)"),
    ("", " 12      9  115  123   N      Salario basico del ultimo mes     (December of the year)"),
    ("", " 13      4  124  127   N      Espacio con ceros                 (must contain zeros)"),
    ("", " 14      9  128  136   N      Valor de las cesantias            (>= 1 day of 1 SMLMV)"),
    ("", " 15     50  137  186   CHAR   Direccion de residencia"),
    ("", " 16      2  187  188   N      Codigo departamento (DANE)"),
    ("", " 17      3  189  191   N      Codigo municipio (DANE)"),
    ("", " 18      7  192  198   N      Telefono fijo                     (exactly 7 digits)"),
    ("", " 19     50  199  248   CHAR   Correo electronico"),
    ("", " 20     10  249  258   N      Fecha de ingreso                  (AAAA-MM-DD)"),
    ("Arithmetic check", "2+5+2+16+20+20+20+20+2+3+4+9+4+9+50+2+3+7+50+10 = 258. Every "
                         "Inicial-Final pair in the published table is consistent with its stated "
                         "length and with its neighbours; there are no gaps and no overlaps. This "
                         "was verified field by field, and the Sheet-9 sample is generated from "
                         "the same table with a 258-character assertion."),
    ("The two zero fillers", "Campos 11 and 13 exist only in this layout. Read them with the campo-"
                             "14 note - 'antes de cada valor deben ir 4 espacios (pueden ser "
                             "rellenos con ceros o en blanco)' - and the intent becomes clear: the "
                             "two amounts are really 13-position frames whose leading 4 positions "
                             "must be zeros or blanks. The campo-11 and campo-13 rules say 'Debe "
                             "contener ceros' without the alternative, so WRITE ZEROS: zeros "
                             "satisfy both readings, blanks satisfy only one."),

    ("##", "LAYOUT B - EXCEL 97-2003 .XLS, 16 COLUMNS A TO P (PUBLISHED)"),
    ("Source", "Simple S.A. 'Manual Cesantias' s. 3.1, with the filled-in example table reproduced "
               "in the manual."),
    ("Rules", "Save as .XLS (MS Excel 97-2003). NO aportante data in the file. NO header row - the "
              "contributor data start on the FIRST row. All records on ONE sheet of the workbook."),
    ("", "A  Tipo de identificacion del empleado   (CC/CE/TI/PA/CD/SC/PE/PT - 2 chars)"),
    ("", "B  Numero de identificacion              (numeric, max 15, no dots or commas)"),
    ("", "C  Primer apellido                       (obligatorio, up to 20)"),
    ("", "D  Segundo apellido                      (optional, up to 20)"),
    ("", "E  Primer nombre                         (obligatorio, up to 20)"),
    ("", "F  Segundo nombre                        (optional, up to 20)"),
    ("", "G  Codigo del Fondo de Cesantias         (02/03/10/15/19)"),
    ("", "H  Numero de dias laborados              (1 to 360)"),
    ("", "I  Salario base                          (obligatorio, max 13, no decimals)"),
    ("", "J  Valor cesantias                       (obligatorio, max 13, no decimals)"),
    ("", "K  Direccion de residencia del empleado"),
    ("", "L  Codigo del departamento (DANE)"),
    ("", "M  Codigo del municipio (DANE)"),
    ("", "N  Telefono fijo del empleado            (7 digits only)"),
    ("", "O  Correo electronico del empleado"),
    ("", "P  Fecha de ingreso del empleado         (AAAA-MM-DD)"),
    ("THREE DIFFERENCES between the two layouts",
     "(1) The XLS has no record type, no sequence and no zero fillers - so campos 1, 2, 11 and 13 "
     "of the TXT layout have no XLS column. (2) The XLS admits PT (Permiso temporal) in column A; "
     "the TXT document-type list printed in the same manual stops at PE. Where the workforce "
     "includes PPT holders, prefer the XLS route or confirm PT with the operator. (3) The identity "
     "number is right-aligned and zero-filled to 16 in the TXT but plain numeric to a 15-character "
     "maximum in the XLS. A generator that shares one formatter across both routes will be wrong "
     "in one of them."),

    ("##", "VALIDATIONS THE CHANNEL PERFORMS (both operators)"),
    ("Structure and content", "Run on upload. Errors are returned as a downloadable Excel report; "
                              "the file must be corrected and re-uploaded. Nothing is partially "
                              "accepted."),
    ("Asofondos affiliate-base check", "Surnames and names are validated against the affiliate "
                                       "base that ASOFONDOS delivers to the operadores de "
                                       "informacion ANNUALLY. Differences produce an Excel report "
                                       "and a SI / NO question: SI overwrites the employer's values "
                                       "with the Asofondos values, NO keeps the employer's. Answer "
                                       "NO and fix the master data - see Spec field E09."),
    ("Minimum recaudo", "Campo 14 must be at least one day of one SMMLV of the accrual year. For "
                        "accrual year 2026: 1,750,905 / 30 = COP 58,363.50."),
    ("Character rules", "No accents and no special characters (both operators list rejected "
                        "characters); identity numbers without spaces, dots or punctuation; "
                        "amounts without points, commas, decimals or signs."),
    ("What is NOT validated", "The channel does NOT check the STATUTORY correctness of campo 14. It "
                              "accepts any figure at or above the floor. In particular it will "
                              "accept a liquidation computed WITHOUT the auxilio de transporte, "
                              "which is a short deposit penalised at one day's salary per day of "
                              "delay. The only defence is to compute campo 14 in the engine."),

    ("##", "THE MONTHLY ADVANCE - A DIFFERENT CHANNEL ENTIRELY, AND NOT YET OPEN"),
    ("Where it goes", "NOT to this file. Ley 2466 de 2025 art. 64 par. 1 routes the 8.33% monthly "
                      "advance through PILA, and the MinTrabajo draft decree repeats it twice: "
                      "'exclusivamente a traves de la Planilla Integrada de Liquidacion de Aportes "
                      "-PILA-' and 'debera reportarse en la PILA como aportes al sistema de "
                      "cesantias mediante el tipo de cotizacion que defina el Ministerio de Salud "
                      "y Proteccion Social'."),
    ("Why it is not yet open", "The decree is a DRAFT as at 4 September 2026. Even on publication, "
                               "its art. 1 par. 2 gives MinSalud SIX MONTHS to adjust PILA and then "
                               "gives the fondos and the operadores de informacion a FURTHER SIX "
                               "MONTHS to build. Until both are done there is no tipo de cotizacion "
                               "to write and the annual planilla is the only lawful route."),
    ("What survives regardless", "The annual consolidation and the February deadline. Draft art. 1 "
                                 "par. 1: the definitive consolidation at year end on the "
                                 "average-of-the-year base, with adjustments. Draft art. 4 par. 4: "
                                 "'La omision de uno o varios pagos mensuales no configurara mora, "
                                 "siempre que se complete el valor total anual a mas tardar el 14 "
                                 "de febrero del ano siguiente, configurandose la mora a partir del "
                                 "15 de febrero.'"),
]

# ===========================================================================
#  SHEET 6 - FIELD OPTIONS
# ===========================================================================
CFG["options"] = [
    "CODIGO DEL FONDO DE CESANTIAS (Spec field T09 / XLS column G) - VERBATIM from the published "
    "layout; exactly five values are admitted",
    ("02", "PROTECCION", "Fondo de Cesantias Proteccion (Proteccion S.A.)",
     "Private severance-savings fund administered by Proteccion S.A."),
    ("03", "PORVENIR", "Porvenir Cesantias (Porvenir S.A.)",
     "Private severance-savings fund administered by Porvenir S.A., the largest by affiliates."),
    ("10", "COLFONDOS", "Colfondos Cesantias (Colfondos S.A. Pensiones y Cesantias)",
     "Private severance-savings fund administered by Colfondos S.A."),
    ("15", "FNA", "Fondo Nacional del Ahorro (FNA)",
     "The STATE-OWNED fund - an Empresa Industrial y Comercial del Estado. The only public-sector "
     "option, and the one whose own employer instructivo would be the single genuinely official "
     "schema for this filing; its published URL now 404s after the FNA site redesign."),
    ("19", "SKANDIA", "Old Mutual (antes Skandia) - printed label; the entity trades as Skandia",
     "STALE LABEL, LIVE CODE. The published layout prints 'Old Mutual (Antes Skandia)', but the "
     "administrator trades as Skandia again - Skandia Administradora de Fondos de Pensiones y "
     "Cesantias S.A., authorised by the Superintendencia Financiera in January 2025 as SKANDIA "
     "AFP-ACCAI S.A. under Ley 2381 de 2024. Send the CODE 19, never the name. Colombian press "
     "coverage of the 2026 deadline lists the five funds as FNA, Colfondos, Porvenir, Proteccion "
     "and Skandia, which corroborates the code table one-for-one."),
    ("-", "-", "Any other value", "REJECTED. The layout states the codes are 'validado contra el "
                                  "listado de Fondos de Cesantias registrados en el sistema. Solo "
                                  "son validos' the five above."),

    "TIPO DE DOCUMENTO (Spec field T03 / XLS column A) - VERBATIM; note the TXT and XLS lists differ",
    ("CC", "CC", "Cedula de ciudadania", "Colombian national identity card. In both layouts."),
    ("CE", "CE", "Cedula de extranjeria", "Foreign resident identity card. In both layouts."),
    ("TI", "TI", "Tarjeta de identidad", "Minor's identity card. In both layouts. Converts to CC on "
                                         "majority - a change of the T03+T04 join key that must "
                                         "reach the fund."),
    ("PA", "PA", "Pasaporte", "Passport. In both layouts."),
    ("CD", "CD", "Carnet diplomatico", "Diplomatic card. In both layouts."),
    ("SC", "SC", "Salvoconducto de permanencia", "Safe-conduct of stay. In both layouts."),
    ("PE", "PE", "Permiso especial de permanencia (PEP)",
     "In both layouts. SOI records a hard length rule: where the document is a PEP the NUMBER must "
     "be EXACTLY 15 digits."),
    ("PT", "PT", "Permiso temporal (PPT - Permiso por Proteccion Temporal)",
     "PRINTED IN THE XLS LIST ONLY. The fixed-width document-type list in the same manual stops at "
     "PE. Where the workforce includes PPT holders (a large Venezuelan-migrant population), prefer "
     "the XLS route or confirm PT with the operator before generating fixed-width files."),
    ("-", "-", "Cross-reference warning",
     "THESE ARE NOT THE CODES USED ELSEWHERE. Formulario 220, Formato 2276 and the nomina "
     "electronica use DIAN NUMERIC document-type codes (13 = cedula de ciudadania, and so on) and "
     "PILA Registro Tipo 2 campo 3 uses a different admitted list. One document type in master "
     "data, three mappers out."),

    "SERVICIO PCSS (Spec field E02) - the service selected in the operator portal",
    ("CESANTIAS", "CES", "Cesantias", "This filing. A Pago Complementario a la Seguridad Social."),
    ("PENSIONES VOLUNTARIAS", "PVOL", "Pensiones voluntarias",
     "The other PCSS service the same portals offer. NOT this filing and not a statutory employer "
     "obligation."),
    ("PILA", "PILA", "Planilla Integrada de Liquidacion de Aportes",
     "A DIFFERENT service in the same portal, with the same login. Monthly, not annual. See "
     "CO-PILA-003. Building a PILA planilla and expecting the cesantias to be inside it is the most "
     "common channel error."),

    "TIPO DE AFILIACION DE LA PLANILLA (Spec field E04) - VERBATIM from the SOI instructivo",
    ("DEPENDIENTE", "DEP", "Dependiente",
     "'Pago de aportes derivados de contrato por nomina'. THE VALUE FOR THIS FILING - always."),
    ("AGREMIADO", "AGR", "Agremiado",
     "'Pago de aportes de independientes asociados o agremiados'. Not an employer filing."),
    ("INDEPENDIENTE", "IND", "Independiente",
     "'Aportes realizados por parte de una persona natural para si misma'. Not an employer filing; "
     "and note that independent workers have no cesantias entitlement at all - cesantias is a "
     "prestacion social of an employment contract."),

    "MEDIO DE PAGO (Spec field E05) - changes the CARDINALITY of the return",
    ("PSE", "PSE", "Pago por PSE (Proveedor de Servicios Electronicos)",
     "Electronic bank payment. ONE planilla number for the whole settlement."),
    ("PAGO CREDITO", "CRE", "Pago credito",
     "ONE PLANILLA NUMBER PER ADMINISTRADORA contained in the settlement (SOI instructivo, footnote "
     "6). The reconciliation store must therefore be one-to-many. See E05 and E10."),

    "RESPUESTA A LA VALIDACION ASOFONDOS (Spec field E09)",
    ("SI", "SI", "Si - ajustar automaticamente",
     "The system replaces the employer's names with the values from the Asofondos affiliate base. "
     "Convenient and wrong: it hides a master-data defect that will recur every year and that is "
     "also wrong on Formulario 220 and Formato 2276."),
    ("NO", "NO", "No - mantener la informacion reportada",
     "Keeps the employer's values. THE CORRECT ANSWER, followed by an investigation of each "
     "difference at source."),

    "ESTADO DE CUMPLIMIENTO DE LA CONSIGNACION (Spec field E91) - Mercans-derived, not a channel code",
    ("ON TIME", "OK", "Consignado en plazo",
     "Payment date (E90) at or before the deadline. No exposure."),
    ("LATE", "MORA", "Consignado en mora",
     "One day's salary per day of delay, per employee, UNCAPPED - Ley 50 de 1990 art. 99 num. 3. "
     "Store the day count. The draft decree fixes the first day of mora as 15 February."),
    ("SHORT", "CORTO", "Consignado por menor valor",
     "The deposit was made in time but for less than the statutory liquidation - typically because "
     "the auxilio de transporte was omitted from the base (see T14). Treated as non-deposit of the "
     "shortfall."),
    ("DISCHARGED", "PAGO DIRECTO", "Liberado por pago directo al trabajador",
     "CST art. 57 par. 4, added by Ley 2466 de 2025 art. 15. No planilla record and no penalty, but "
     "the evidence must be fehaciente, the discharge is rebuttable on the freedom-and-purpose test, "
     "and fund affiliation remains compulsory."),
    ("N/A", "NA", "No aplica",
     "Salario integral, leaver settled in the final settlement, pre-1991 retrospective regime, or a "
     "residue below one day of the SMMLV. See the Payroll Scope Summary."),

    "CODIGOS DANE (Spec fields T16 and T17) - reference only; the full divipola list is master data",
    ("11 / 001", "BOG", "Bogota, D.C.", "Department 11, municipality 001 - divipola 11001. The "
                                        "example used on Sheets 8 and 9."),
    ("05 / 001", "MED", "Medellin (Antioquia)", "Department 05, municipality 001 - divipola 05001."),
    ("76 / 001", "CAL", "Cali (Valle del Cauca)", "Department 76, municipality 001 - divipola 76001."),
    ("08 / 001", "BAQ", "Barranquilla (Atlantico)", "Department 08, municipality 001 - divipola 08001."),
    ("-", "-", "Composite rule",
     "T16 is the two-digit DEPARTMENT prefix and T17 the three-digit MUNICIPALITY suffix of ONE "
     "five-digit divipola code. Writing the full 11001 into the three-position T17 truncates to 110 "
     "and relocates the affiliate."),

    "FISCAL PARAMETERS THAT DRIVE THIS FILING - accrual year 2026",
    ("1750905", "SMMLV", "Salario minimo mensual legal vigente 2026",
     "Decreto 1469 de 2025. Sets the minimum-recaudo validation (one day = COP 58,363.50) and, for "
     "a minimum-wage employee, the salary half of the base."),
    ("249095", "AUX TTE", "Auxilio de transporte 2026",
     "Decreto 1469 de 2025. PART OF THE CESANTIAS BASE under CST art. 253, payable where the salary "
     "does not exceed 2 SMMLV (COP 3,501,810). The operator's calculator omits it - see T14."),
    ("2000000", "BASE MIN", "Base de liquidacion de un trabajador de salario minimo 2026",
     "1,750,905 + 249,095 = exactly COP 2,000,000. A full year at 360 days therefore liquidates to "
     "COP 2,000,000, against COP 1,750,905 if the transport allowance is wrongly excluded - a "
     "shortfall of COP 249,095 per employee."),
    ("52374", "UVT", "Unidad de Valor Tributario 2026",
     "Res. DIAN 000238 of 15 Dec 2025. Not used in this file, but it fixes the ET art. 206 num. 4 "
     "exemption bands (350 UVT = COP 18,330,900) that apply when the money is PAID and reported on "
     "Formulario 220 and Formato 2276."),
    ("360", "ANO COMERCIAL", "Ano comercial de 360 dias",
     "The divisor in both the statutory formula and the layout's own calculator. Not 365."),
]

# ===========================================================================
#  SHEET 7 - POPULATION RULES
# ===========================================================================
CFG["population"] = [
    "STEP 0 - BUILD THE POPULATION (this is where the filing is usually got wrong)",
    ("Population of the planilla", "Payroll master data + service history",
     "Select every employee IN SERVICE AT 31 DECEMBER of the accrual year who is on the annual "
     "cesantias regime (Ley 50 de 1990 art. 99 - all employees hired from 1 January 1991, plus "
     "pre-1991 hires who migrated). EXCLUDE, in this order: (1) salario integral employees, whose "
     "cesantias is absorbed by CST art. 132 num. 2; (2) employees who LEFT during the year, whose "
     "cesantias was settled and paid in the final settlement; (3) pre-1991 non-migrated employees "
     "on the retrospective regime, for whom there is no fund deposit at all; (4) employees "
     "discharged by proven direct payment under CST art. 57 par. 4; (5) records whose liquidation "
     "falls below one day of one SMMLV, which the channel rejects. Do NOT build the population from "
     "the December PILA planilla, however convenient the portal makes it (E08): PILA is the "
     "population PAID in a month, not the population ENTITLED for the year - it contains every "
     "salario integral employee and omits every mid-year leaver.",
     "A leaver included = double payment, and the money is then in a fund account the ex-employee "
     "must claim. A salario integral employee included = an unrecoverable deposit. A missed "
     "employee = one day's salary per day of delay, uncapped, running until it is found."),
    ("Fund per employee", "Employee master data",
     "Read Employee.Cesantias_Fund_Code. It is the EMPLOYEE'S statutory choice under Ley 50 de 1990 "
     "art. 99 num. 3 ('en el fondo de cesantia que el mismo elija'), so it is employee master data "
     "and never a company default. Where a mid-year change of fund has been notified, use the fund "
     "in force at the date of the deposit. Where the field is empty the record cannot be built - "
     "escalate, because affiliation is compulsory even where the cesantias is paid directly (CST "
     "art. 57 par. 4 in fine). Set E07 to N so that this per-employee value governs.",
     "An empty fund code is not a payroll defect to be defaulted - it is an unfulfilled affiliation "
     "obligation. Answering YES to the portal's single-fund question to get past it deposits other "
     "people's money into the wrong fund and does not discharge the obligation."),

    "STEP 1 - COMPUTE THE BASE AND THE AMOUNT (CST arts. 249 and 253)",
    ("T14 Valor de las cesantias", "Payroll engine - annual liquidation",
     "Compute, do NOT let the portal compute. (a) Determine the BASE under CST art. 253: the LAST "
     "monthly salary if it has not varied in the last three months; otherwise, and for every "
     "variable salary, the AVERAGE of the last year of service, or of the whole period served if "
     "shorter. (b) ADD THE AUXILIO DE TRANSPORTE where it is payable - CST art. 253 requires it and "
     "it is payable where the salary does not exceed 2 SMMLV (COP 3,501,810 in 2026). (c) Multiply "
     "by days of service over 360. (d) Round to the whole peso - not up to the next 100 as PILA "
     "requires, and not to the nearest 1,000 as Formulario 350 requires. (e) Validate against the "
     "floor of one day of one SMMLV (COP 58,363.50 for 2026). (f) Where a lawful partial settlement "
     "was made during the year under CST art. 254, deduct it. (g) Where the monthly advance regime "
     "is ever switched on, deposit only the difference (MA05). Write the result into positions "
     "128-136, right-aligned and zero-filled, with '0000' in positions 124-127.",
     "THE TRAP: the layout's own formula is 'Salario basico * (dias trabajados / 360)' and campo 12 "
     "is named 'salario basico'. Follow the portal and a minimum-wage employee is deposited COP "
     "1,750,905 instead of COP 2,000,000 - a COP 249,095 short deposit per employee, penalised as "
     "non-deposit at one day's salary per day of delay. The floor also bites in reverse: a residue "
     "below COP 58,363.50 cannot be deposited and must be settled with the employee instead."),
    ("T12 Salario basico del ultimo mes", "Payroll - December of the accrual year",
     "Report the DECEMBER basic salary of the accrual year, exactly as the layout specifies ('el "
     "ultimo salario basico reportado en el mes de diciembre del ano causado de cesantias'), in 9 "
     "integer positions, zero-filled, with '0000' in positions 111-114. This is a REPORTING field "
     "for the fund's records - it is NOT the statutory base, and the two will legitimately differ "
     "for a variable-salary employee whose base is a twelve-month average. Do not reverse-engineer "
     "T12 from T14 to make the portal's calculator agree.",
     "For an employee who was on unpaid leave in December, or who was hired on 20 December, the "
     "December basic is still the contractual monthly salary, not the amount actually earned that "
     "month. For an employee whose salary changed in November, T12 carries the December figure "
     "while the CST art. 253 base is the twelve-month average - so T14 will not equal T12 * "
     "T10/360, and that is correct."),
    ("T10 Numero de dias trabajados", "Payroll - service calendar",
     "Count the days of service in the accrual year on the 360-day COMMERCIAL convention: each "
     "complete month is 30 days, a full year is 360. Include paid leave, paid holidays and "
     "recognised incapacity, all of which count as service. Exclude unpaid leave (licencia no "
     "remunerada) and suspension. For an employee in service the whole year write 360, not 365 and "
     "not 366. The field admits 1 to 360 only, so any computation that can produce 361 or more is "
     "wrong before it reaches the file.",
     "A leap year does not change the divisor. An employee hired on 31 January accrues 330 days, "
     "not 335. Where unpaid leave straddles a month end, count the calendar days of the leave on "
     "the 30-day convention and subtract - do not subtract whole months."),

    "STEP 2 - IDENTIFICATION AND CONTACT FIELDS",
    ("T03 + T04 Tipo y numero de documento", "Employee master data",
     "Map the document type to the two-letter cesantias code (CC/CE/TI/PA/CD/SC/PE, plus PT in the "
     "XLS route only) - this is a DIFFERENT mapper from the DIAN numeric codes used on Formulario "
     "220 and Formato 2276 and from the PILA list. Strip dots, commas, spaces and hyphens from the "
     "number, then RIGHT-ALIGN and ZERO-FILL to 16 positions for the fixed-width route, or leave it "
     "plain to a 15-character maximum for the XLS route. Where the type is PE the number must be "
     "exactly 15 digits.",
     "A regularisation that converts a PEP or PPT into a Cedula de Extranjeria changes the join key "
     "the fund holds; unless the change reaches the fund, the February deposit lands on an orphan "
     "account and the employee cannot see it. A TI holder reaching majority is the same problem. "
     "Where the workforce includes PPT holders and the fixed-width route is used, the document-type "
     "list printed for that layout has no PT value - confirm with the operator rather than "
     "substituting CE."),
    ("T05-T08 Apellidos y nombres", "Employee master data",
     "Write the four name components into their own 20-position fields, left-aligned and "
     "space-filled: primer apellido (obligatorio), segundo apellido, primer nombre (obligatorio), "
     "segundo nombre. Strip accents and every special character the operators reject. Where a "
     "component is absent, SPACE-FILL THE WHOLE FIELD - never shift the following fields up, "
     "because the record is positional and the fund code at 106-107 would then be read out of the "
     "middle of a name. Space-fill rather than truncate; a truncated surname mismatches the "
     "Asofondos base every year. Answer NO to the auto-adjust question (E09) and fix differences at "
     "source.",
     "Compound surnames longer than 20 characters have to be truncated somewhere - do it "
     "deliberately and record the rule, because the same truncation must be applied consistently "
     "year on year or the mismatch report churns. A person with one name and one surname produces "
     "two space-filled fields, which is valid. Foreign employees whose passport shows a single name "
     "field need a documented split rule; the fund's record follows whatever was first sent."),
    ("T15-T19 Direccion, DANE, telefono, correo", "Employee master data",
     "Write the RESIDENTIAL address (not the work address - the fund communicates with its member "
     "at home), 50 positions space-filled. Split the DANE divipola code into its two-digit "
     "department half at 187-188 and its three-digit municipality half at 189-191. The landline "
     "field admits EXACTLY seven digits, so a 10-digit mobile cannot go in it; zero- or space-fill "
     "instead. The e-mail field is 50 positions and the operator validates the local part, the @ and "
     "the domain separately, with the hyphen barred from the first and last position of the domain.",
     "The single most common defect here is sending the WORK municipality, because that is what "
     "PILA and the nomina electronica want; the affiliate then never receives a fund statement. "
     "Truncating a mobile number to seven digits produces a wrong-number record on the fund's file, "
     "which is worse than an empty one. Addresses longer than 50 characters must be abbreviated by "
     "a documented rule, not cut mid-token."),
    ("T20 Fecha de ingreso", "Contract master data",
     "Write the CONTRACT HIRE DATE in AAAA-MM-DD, ten positions including the hyphens, at 249-258. "
     "For an employee hired in 2019 and reported for accrual year 2026 the value is 2019-03-01 - "
     "not 2026-01-01, and not the start of the accrual period.",
     "Sending the accrual-year start corrupts the fund's seniority record, which the fund uses for "
     "its own member-benefit rules. For a rehired employee, use the hire date of the CURRENT "
     "contract, which is the contract the cesantias accrued under. Note the layout types this field "
     "N while the content contains hyphens; a strict numeric writer will emit 8 characters and fail "
     "validation even though nothing shifts, because the field is last in the record."),

    "STEP 3 - ENVELOPE, PAYMENT AND RECONCILIATION",
    ("E01-E06 Planilla envelope", "Company master data + run parameters",
     "Authenticate with the company document pair, select the service CESANTIAS (not PILA), enter "
     "the ACCRUAL YEAR (not a month), select afiliacion type DEPENDIENTE, select the medio de pago "
     "and label the planilla with the run identifier so the returned planilla number can be tied "
     "back. Answer NO to the seed-from-PILA question and NO to the single-fund question.",
     "The period concept is the trap: every other Colombian payroll filing is monthly and keyed to "
     "a payment date, and this one is keyed to the accrual year that closed on 31 December. A "
     "planilla built in February 2027 carries ano causado 2026."),
    ("E10-E11, E90 Return values", "Operator portal - inbound",
     "Store the planilla number, the total payable and the PAYMENT date. Where the medio de pago is "
     "Pago Credito, expect and store MANY planilla numbers - one per fondo. Reconcile the returned "
     "total against the engine's own sum of T14 before paying, because the file carries no header, "
     "no trailer, no record count and no declared total, so a truncated upload is not "
     "self-detecting. Download and archive the comprobante PDF and the per-fondo report.",
     "Liquidating the planilla is not paying it. A planilla liquidated on 13 February and paid on "
     "17 February is LATE - the deadline attaches to the deposit, so the compliance evidence is the "
     "payment date, not the liquidation date."),
    ("E91-E93 Compliance status and evidence", "Engine-derived + fund certificate",
     "Derive the per-employee status (ON TIME / LATE with a day count / SHORT with a shortfall / "
     "DISCHARGED BY DIRECT PAYMENT) from E90 against the deadline, and hold it with the fund's "
     "deposit certificate reference for at least the employee's three-year limitation period under "
     "CST art. 488 as substituted by Ley 2466 de 2025 art. 62. Quantify the exposure: the penalty "
     "is one day's salary per day of delay, per employee, uncapped - for 100 minimum-wage employees "
     "a fortnight is of the order of COP 81.7 million.",
     "The certificate is issued by the FUND, but CCG Module 10 records that the EMPLOYER must be "
     "able to evidence it - so the reference must be stored employer-side, not left on a portal. A "
     "SHORT deposit made on time is not a lesser problem than a late one: the shortfall is treated "
     "as non-deposit and accrues the same daily penalty."),

    "STEP 4 - THE TWO THINGS THAT ARE NOT IN THIS FILE",
    ("IN01-IN03 Intereses de cesantias", "Payroll engine - paid to the EMPLOYEE",
     "Compute 12% per annum on the 31 December balance, pro-rated on days over 360, and PAY IT TO "
     "THE EMPLOYEE DIRECTLY DURING JANUARY of the following year - never to the fund and never in "
     "February. Liquidate no interest on interest. Where a WRITTEN agreement exists under Ley 2466 "
     "de 2025 art. 64 par. 2, pay instead 1% monthly of the monthly base (salary + transport "
     "allowance), within the calendar month following accrual per the draft decree. Evidence the "
     "payment - failure costs an indemnity equal to the interest owed, once only, under Ley 52 de "
     "1975 art. 1.",
     "Two obligations, two payees, two deadlines, two penalties, and they are routinely conflated. "
     "Depositing the interest to the fund discharges nothing and leaves the January obligation open. "
     "Note also that the monthly 1% option and the annual 12% do NOT arrive at the same figure, "
     "because the monthly base is the monthly salary while the annual base is the accumulated "
     "balance."),
    ("Tax treatment of the cesantias", "CO-DIAN-004 and CO-DIAN-005, not here",
     "No withholding is practised on the DEPOSIT. When the money is eventually paid to the employee, "
     "a RESIDENT gets the ET art. 206 num. 4 exemption - full below a six-month average of 350 UVT "
     "(COP 18,330,900 in 2026), then tapering 90/80/60/40/20 per cent across the 350-410, 410-470, "
     "470-530, 530-590 and 590-650 UVT bands - while a NON-RESIDENT gets no exemption and the flat "
     "20% of ET art. 408 on the gross. The figures are reported on Formulario 220 casillas 48-49 "
     "and Formato 2276 numerals 19-20.",
     "Formato 2276 numerals 19 and 20 are TRANSPOSED against Formulario 220 casillas 48 and 49 - "
     "map by MEANING, per the CO-DIAN-005 Spec. Nothing about the tax treatment changes a character "
     "of the record sent to the fund, which is why a non-resident's record is identical to a "
     "resident's."),
]

# ===========================================================================
#  SHEET 8 - EXAMPLE ANALYSIS
# ===========================================================================
CFG["example"] = [
    "THE SCENARIO",
    ("-", "Employee", "Juan Carlos Perez Gomez, CC 1.020.304.050, hired 1 March 2019, in service "
                      "the whole of accrual year 2026, resident in Bogota D.C., affiliated to "
                      "Porvenir.",
     "Chosen deliberately: an employee on the 2026 minimum wage, because that is the case in which "
     "the auxilio de transporte is payable and the operator's calculator therefore gives the wrong "
     "answer."),
    ("-", "Pay", "Basic salary COP 1,750,905 (the 2026 SMMLV), unchanged through the year. Auxilio "
                 "de transporte COP 249,095, payable because the salary does not exceed 2 SMMLV "
                 "(COP 3,501,810). CST art. 253 base = 1,750,905 + 249,095 = COP 2,000,000 exactly.",
     "Decreto 1469 de 2025 sets both figures. The base is exactly two million, which makes the "
     "arithmetic below checkable by eye."),
    ("-", "Liquidation", "2,000,000 x 360 / 360 = COP 2,000,000, deposited to Porvenir before 15 "
                         "February 2027.",
     "What the operator's own calculator would have produced: 1,750,905 x 360 / 360 = COP "
     "1,750,905. A shortfall of COP 249,095 - see the trap note at the end of this sheet."),

    "THE 258-POSITION RECORD, FIELD BY FIELD",
    ("02", "T01 Tipo de registro (1-2)", "Constant. Every detail line is a type-02 record.",
     "There is no header and no trailer, so the file carries no record count and no control total."),
    ("00001", "T02 Secuencia (3-7)", "First record of the planilla.",
     "Must start at 00001 and be consecutive. Positions 1-7 together are the record key the "
     "operator's structure validation reads first."),
    ("CC", "T03 Tipo de documento (8-9)", "Cedula de ciudadania.",
     "Two ALPHABETIC characters. Not the DIAN numeric code 13 that the same employee carries on "
     "Formulario 220 casilla 24 and Formato 2276 numeral 2."),
    ("0000001020304050", "T04 Numero de identificacion (10-25)",
     "1020304050, right-aligned and zero-filled to 16 positions.",
     "Six leading zeros. In the XLS route the SAME number is written plain as 1020304050 to a "
     "15-character maximum - one formatter cannot serve both routes."),
    ("PEREZ...............", "T05 Primer apellido (26-45)", "PEREZ plus 15 spaces.",
     "Left-aligned, space-filled. Dots shown here only to make the padding visible; the real file "
     "carries spaces."),
    ("GOMEZ...............", "T06 Segundo apellido (46-65)", "GOMEZ plus 15 spaces.",
     "Not marked obligatorio. Had the employee no second surname, all 20 positions would be "
     "spaces - never omitted, or everything after position 45 shifts."),
    ("JUAN................", "T07 Primer nombre (66-85)", "JUAN plus 16 spaces.", "Obligatorio."),
    ("CARLOS..............", "T08 Segundo nombre (86-105)", "CARLOS plus 14 spaces.",
     "Optional. Maps to the Data-Dictionary Other_Names field, shared with the nomina electronica "
     "and Formulario 220."),
    ("03", "T09 Codigo del Fondo (106-107)", "Porvenir - the employee's own choice.",
     "Only 02, 03, 10, 15 and 19 are admitted. Had E07 been answered YES, this value would have "
     "been overwritten for every employee in the planilla."),
    ("360", "T10 Dias trabajados (108-110)", "A full accrual year on the 360-day commercial "
                                             "convention.",
     "Not 365, and not 366 in a leap year. The field cannot carry more than 360."),
    ("0000", "T11 Espacio con ceros (111-114)", "Zero filler in front of the salary field.",
     "'Debe contener ceros'. Absent from the XLS layout."),
    ("001750905", "T12 Salario basico del ultimo mes (115-123)",
     "The December 2026 basic salary, COP 1,750,905, zero-filled to 9 positions.",
     "A REPORTING field for the fund. It is the basic salary ALONE - the transport allowance does "
     "not belong here, only in the base of T14."),
    ("0000", "T13 Espacio con ceros (124-127)", "Zero filler in front of the cesantias value.",
     "Same rule as T11. Together the two fillers make each amount a 13-position frame."),
    ("002000000", "T14 Valor de las cesantias (128-136)",
     "COP 2,000,000 - the CST art. 253 base of 2,000,000 for 360 of 360 days.",
     "Above the floor of one day of one SMMLV (COP 58,363.50). Computed by the engine and written "
     "in, so no automatic calculation is performed."),
    ("CALLE 26 NO 68-35 APTO 502", "T15 Direccion de residencia (137-186)",
     "The employee's HOME address, space-filled to 50 positions.",
     "Not the work address. The fund posts member statements here - contrast PILA and the nomina "
     "electronica, which carry the WORK municipality."),
    ("11", "T16 Codigo departamento (187-188)", "Bogota D.C.",
     "The two-digit half of divipola 11001."),
    ("001", "T17 Codigo municipio (189-191)", "Bogota D.C.",
     "The three-digit half of divipola 11001. Writing 11001 here truncates to 110."),
    ("6013456", "T18 Telefono fijo (192-198)", "A seven-digit landline.",
     "'Solo admite 7 numeros'. A 10-digit mobile does not fit and must not be truncated."),
    ("juan.perez@empresa.com.co", "T19 Correo electronico (199-248)",
     "Local part, @, domain - space-filled to 50 positions.",
     "The operator validates the three parts separately; the hyphen may be neither the first nor "
     "the last character of the domain."),
    ("2019-03-01", "T20 Fecha de ingreso (249-258)", "The CONTRACT hire date, 1 March 2019.",
     "NOT 2026-01-01. Ten positions including the hyphens, even though the layout types the field "
     "N."),

    "RECONCILIATION OF THIS RECORD ACROSS THE OTHER COLOMBIAN FILINGS",
    ("2000000", "Formulario 220 casilla 48 / 49", "The same cesantias figure reported to DIAN on "
                                                  "the employee's annual certificate.",
     "Casilla 48 is the amount deposited to the fund and casilla 49 the traditional-regime amount. "
     "For this employee, 48 = 2,000,000 and 49 = 0. See the CO-DIAN-004 Spec."),
    ("2000000", "Formato 2276 numerals 19 and 20", "The same figure again in the information return.",
     "AND THEY ARE TRANSPOSED against Formulario 220 - numeral 19 and numeral 20 do not sit in the "
     "same order as casillas 48 and 49. Map by MEANING; a positional mapping swaps them and the "
     "error is invisible because both feed the same total. See the CO-DIAN-005 Spec."),
    ("240000", "Interest at 12% - IN02", "2,000,000 x 12% x 360/360 = COP 240,000, paid to the "
                                         "EMPLOYEE in January 2027.",
     "Not in this file and not to the fund. Failure to pay costs an indemnity equal to the interest "
     "owed, once only (Ley 52 de 1975 art. 1)."),
    ("0", "PILA", "Nothing. Cesantias is a prestacion social and is not part of the contribution "
                  "base.",
     "That will change only as to CHANNEL, not nature, if the monthly advance under Ley 2466 de "
     "2025 art. 64 par. 1 is ever brought into force - see MA04."),

    "THE FOUR TRAPS IN THIS RECORD",
    ("249095", "Trap 1 - the auxilio de transporte", "The operator's formula is 'Salario basico * "
                                                     "(dias trabajados / 360)' and would have "
                                                     "produced COP 1,750,905.",
     "CST art. 253 requires the transport allowance in the base. Following the portal short-deposits "
     "COP 249,095 for this employee, and a short deposit is penalised as non-deposit at one day's "
     "salary per day of delay, uncapped. ALWAYS write the engine's figure into T14."),
    ("360", "Trap 2 - the divisor", "360, not 365 or 366.",
     "Both the statute and the layout use the commercial year. Using 365 understates every full-year "
     "liquidation by about 1.4%, which is again a short deposit."),
    ("2019-03-01", "Trap 3 - which date", "The hire date of the contract, not the start of the "
                                          "accrual year.",
     "T20 is the field most often filled with 1 January of the accrual year. It corrupts the fund's "
     "seniority record for the member."),
    ("11 / 001", "Trap 4 - which address", "The RESIDENCE, split into the two halves of one DANE "
                                           "divipola code.",
     "PILA and the nomina electronica want the WORK municipality; this file wants the home one. "
     "Reusing the PILA mapping sends the member's statements to the office."),
]

# ===========================================================================
#  SHEET 9 - SAMPLE FILE
#  Generated from the published layout with a hard 258-character assertion.
# ===========================================================================


def _rec(seq, doctype, docnum, ap1, ap2, no1, no2, fondo, dias, salario, valor,
         direccion, dep, mun, tel, mail, ingreso):
    """Build one detail record strictly to the published 258-position layout."""
    parts = [
        ("02", 2),
        ("%05d" % seq, 5),
        (doctype.ljust(2), 2),
        (docnum.rjust(16, "0"), 16),
        (ap1.ljust(20)[:20], 20),
        (ap2.ljust(20)[:20], 20),
        (no1.ljust(20)[:20], 20),
        (no2.ljust(20)[:20], 20),
        (fondo.rjust(2, "0"), 2),
        ("%03d" % dias, 3),
        ("0000", 4),
        ("%09d" % salario, 9),
        ("0000", 4),
        ("%09d" % valor, 9),
        (direccion.ljust(50)[:50], 50),
        (dep.rjust(2, "0"), 2),
        (mun.rjust(3, "0"), 3),
        (tel.rjust(7), 7),
        (mail.ljust(50)[:50], 50),
        (ingreso.ljust(10), 10),
    ]
    out = ""
    pos = 1
    for value, length in parts:
        if len(value) != length:
            raise ValueError("field at position %d is %d chars, expected %d: %r"
                             % (pos, len(value), length, value))
        out += value
        pos += length
    if len(out) != 258:
        raise ValueError("record is %d characters, expected 258" % len(out))
    return out


_R1 = _rec(1, "CC", "1020304050", "PEREZ", "GOMEZ", "JUAN", "CARLOS", "03", 360,
           1750905, 2000000, "CALLE 26 NO 68-35 APTO 502", "11", "001", "6013456",
           "juan.perez@empresa.com.co", "2019-03-01")
_R2 = _rec(2, "CC", "52987654", "RAMIREZ", "", "ANA", "", "02", 210,
           4200000, 2450000, "CARRERA 43A NO 1-50 TORRE 2", "05", "001", "6045678",
           "ana.ramirez@empresa.com.co", "2026-06-01")
_R3 = _rec(3, "PE", "123456789012345", "MARQUEZ", "SILVA", "LUIS", "", "15", 360,
           2500000, 2749095, "DIAGONAL 15 NO 100-22", "76", "001", "6023456",
           "luis.marquez@empresa.com.co", "2023-11-02")

_RULER = ("         1         2         3         4         5         6         7         8"
          "         9        10")
_TICKS = "123456789" + ("0123456789" * 10)

CFG["sample_title"] = ("PUBLISHED 258-POSITION FIXED-WIDTH LAYOUT - SAMPLE GENERATED FROM THE "
                       "SIMPLE S.A. SPECIFICATION")
CFG["sample"] = r"""
===============================================================================
PROVENANCE - READ THIS BEFORE USING THE SAMPLE
===============================================================================
This sample is NOT fabricated and it is NOT a neutral model. It is generated
programmatically from the layout published in

  Simple S.A. (licensed operador de informacion), "Manual Cesantias -
  Cesantias Simple - Manual de usuario", section 3.2 "Elaboracion de planillas
  carga de archivo TXT",
  held at 00-official-sources/pdfs/pagosimple_cesantias.pdf,
  extracted to _txt/pagosimple_cesantias.txt.

Every position, length, type, padding rule and code value below is transcribed
from that table. The generator in co_r6_sheets.py asserts each field's width
and asserts the total record length is exactly 258 characters, so no position
can drift silently.

WHAT IS STILL TO CONFIRM:
  * Whether the other licensed operadores de informacion (Aportes en Linea,
    Asopagos, Enlace Operativo, MiPlanilla) accept this same 258-position
    record, or impose an operator-specific variant. The channel itself is
    confirmed independently by the ACH Colombia (SOI) instructivo, but SOI
    publishes its column layout only inside the upload screen.
  * The code page and the line terminator, which the instructivo does not
    state. Written here as ASCII with CRLF.
  * The Fondo Nacional del Ahorro's own employer instructivo, whose published
    URL now returns 404 after the FNA site redesign. FNA is a state entity and
    its layout would be the one genuinely official schema for this filing.

===============================================================================
POSITION RULER
===============================================================================
""" + _RULER + "\n" + _TICKS + r"""

===============================================================================
SAMPLE PLANILLA - ACCRUAL YEAR 2026, THREE RECORDS
Envelope keyed in the portal (NOT in the file):
  Aportante            NI 9001234567
  Servicio             Cesantias
  Ano causado          2026
  Tipo de afiliacion   Dependiente
  Medio de pago        PSE
  Fondo unico          NO  (each employee keeps their own chosen fund)
  Seed from PILA       NO
  Asofondos autoajuste NO
===============================================================================
""" + _R1 + "\n" + _R2 + "\n" + _R3 + r"""

===============================================================================
WHAT EACH RECORD DEMONSTRATES
===============================================================================
RECORD 1 - the ordinary full-year case, and the transport-allowance trap.
  Juan Carlos Perez Gomez, CC 1020304050, Porvenir (03), 360 days.
  December basic 1,750,905 (the 2026 SMMLV) in campo 12.
  Cesantias 2,000,000 in campo 14 = (1,750,905 + 249,095 auxilio de
  transporte) x 360/360, per CST art. 253.
  The portal's own calculator would have written 1,750,905. The COP 249,095
  difference is a SHORT DEPOSIT, penalised at one day's salary per day of
  delay under Ley 50 de 1990 art. 99 num. 3, uncapped, per employee.

RECORD 2 - a mid-year hire, no second surname, no second name, salary above
  2 SMMLV so NO transport allowance in the base.
  Ana Ramirez, CC 52987654, Proteccion (02), hired 1 June 2026.
  210 days of service on the 360-day commercial convention (7 x 30).
  December basic 4,200,000; base excludes the transport allowance because the
  salary exceeds 2 SMMLV (COP 3,501,810).
  4,200,000 x 210/360 = 2,450,000.
  Note positions 46-65 and 86-105: TWENTY SPACES each, not omitted. Omitting
  them would shift the fondo code out of positions 106-107 and every field
  after it.

RECORD 3 - a foreign employee on a Permiso Especial de Permanencia, the
  state-owned fund, and the transport allowance applied correctly.
  Luis Marquez Silva, PE 123456789012345, Fondo Nacional del Ahorro (15).
  December basic 2,500,000, which is below 2 SMMLV, so the auxilio de
  transporte IS payable: base = 2,500,000 + 249,095 = 2,749,095, and
  360/360 gives campo 14 = 2,749,095. Contrast record 1, where the same
  rule was applied, and note that the portal calculator would have written
  2,500,000 here too.
  The PEP number is EXACTLY 15 digits, per the length rule in the SOI
  instructivo, so positions 10-25 carry one leading zero and then the 15.
  A later regularisation to a Cedula de Extranjeria CHANGES the join key that
  the fund holds (campos 3 and 4) and must be notified, or the following
  February's deposit lands on an orphan account.

===============================================================================
FIELD-BY-FIELD DECOMPOSITION OF RECORD 1
===============================================================================
positions  value                              campo
   1-2     02                                 1  Tipo de registro (constant)
   3-7     00001                              2  Secuencia
   8-9     CC                                 3  Tipo de documento
  10-25    0000001020304050                   4  Numero de identificacion
  26-45    PEREZ + 15 spaces                  5  Primer apellido
  46-65    GOMEZ + 15 spaces                  6  Segundo apellido
  66-85    JUAN + 16 spaces                   7  Primer nombre
  86-105   CARLOS + 14 spaces                 8  Segundo nombre
 106-107   03                                 9  Codigo del Fondo (Porvenir)
 108-110   360                               10  Dias trabajados
 111-114   0000                              11  Espacio con ceros
 115-123   001750905                         12  Salario basico de diciembre
 124-127   0000                              13  Espacio con ceros
 128-136   002000000                         14  Valor de las cesantias
 137-186   CALLE 26 NO 68-35 APTO 502 + 24sp 15  Direccion de residencia
 187-188   11                                16  Codigo departamento (DANE)
 189-191   001                               17  Codigo municipio (DANE)
 192-198   6013456                           18  Telefono fijo
 199-248   juan.perez@empresa.com.co + 25sp  19  Correo electronico
 249-258   2019-03-01                        20  Fecha de ingreso

Length check: 2+5+2+16+20+20+20+20+2+3+4+9+4+9+50+2+3+7+50+10 = 258.

===============================================================================
THE SAME PLANILLA IN THE XLS 97-2003 ROUTE (16 columns, no header row)
===============================================================================
A    B                C        D       E     F       G   H    I        J        K                           L   M    N        O                          P
CC   1020304050       PEREZ    GOMEZ   JUAN  CARLOS  03  360  1750905  2000000  CALLE 26 NO 68-35 APTO 502  11  001  6013456  juan.perez@empresa.com.co  2019-03-01
CC   52987654         RAMIREZ          ANA           02  210  4200000  2450000  CARRERA 43A NO 1-50 TORRE 2 05  001  6045678  ana.ramirez@empresa.com.co 2026-06-01
PE   123456789012345  MARQUEZ  SILVA   LUIS          15  360  2500000  2749095  DIAGONAL 15 NO 100-22       76  001  6023456  luis.marquez@empresa.com.co 2023-11-02

Note the three differences from the fixed-width route: there is no record type,
no sequence and no zero filler; the identity number is plain and capped at 15
characters rather than zero-filled to 16; and column A additionally admits PT
(Permiso temporal), which the fixed-width document-type list does not print.

===============================================================================
WHAT THE CHANNEL RETURNS
===============================================================================
  Numero de planilla        1234567890
                            (ONE number with PSE; one number PER FONDO where
                            the medio de pago is Pago Credito)
  Valor total a pagar       7,199,095   = 2,000,000 + 2,450,000 + 2,749,095
                            Reconcile this against the engine's own sum. The
                            file has NO header, NO trailer, NO record count and
                            NO declared total, so a truncated upload is not
                            self-detecting.
  Comprobante previo al pago  PDF
  Asofondos name validation   Excel difference report, if any - answer NO to
                              the auto-adjust question and fix master data.
  After payment               Informe por fondo / por afiliado / completo, in
                              PDF or Excel; plus the fund's own deposit
                              certificate, which the EMPLOYER must be able to
                              evidence.

===============================================================================
DEADLINE FOR THIS SAMPLE
===============================================================================
Accrual year 2026 liquidates at 31 December 2026 and must be deposited BEFORE
15 FEBRUARY 2027 (Ley 50 de 1990 art. 99 num. 3), so the last compliant day is
Sunday 14 February 2027. Colombian practice moves a deadline falling on a
non-business day to the next business day - and for accrual year 2025 the shift
from Saturday 14 February 2026 to Monday 16 February 2026 was reported
uniformly in the Colombian press - but no MinTrabajo concepto stating the rule
was located, and the draft decree fixes mora as running "a partir del 15 de
febrero". DO NOT RELY ON THE SHIFT: pay by Friday 12 February 2027.

The penalty for getting it wrong is ONE DAY'S SALARY FOR EACH DAY OF DELAY,
PER EMPLOYEE, UNCAPPED. For 100 minimum-wage employees a two-week delay is of
the order of COP 81.7 million.
"""


# ===========================================================================
#  BUILD ENTRY POINT
#     python co_r6_sheets.py
#  -> CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx
# ===========================================================================
if __name__ == "__main__":
    import os
    from build_co_specs import build_workbook, OUTPUT_DIR

    _out = os.path.join(OUTPUT_DIR, "CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx")
    build_workbook(CFG).save(_out)
    print("saved %s" % _out)

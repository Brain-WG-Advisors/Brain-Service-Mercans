# -*- coding: utf-8 -*-
"""
CO-DIAN-001 - Sheets 5 to 9 (File Structure, Field Options, Population Rules,
Example Analysis, Sample File) for the Documento Soporte de Pago de Nomina
Electronica.

All structural facts are transcribed from the official Anexo Tecnico version 1.0
(Resolucion DIAN 000013 of 11 February 2021) held at
00-official-sources/pdfs/AnexoTecnico-NominaElectronica-V1.0.pdf.
"""

from co_r1_nomina_electronica import CFG

# ===========================================================================
#  SHEET 5 - FILE STRUCTURE
# ===========================================================================
CFG["filestruct"] = [
    ("##", "FILE FORMAT"),
    ("File type", "XML 1.0. The signature area uses OASIS UBL 2.1; every other section uses DIAN's "
                  "own structure as published in the Anexo Tecnico. This is a REAL XML submission "
                  "with a published schema - not a portal form - so the wire format below is the "
                  "actual submission format, not a logical model."),
    ("Schema", "XSD version 1.0.6, referenced by Anexo Tecnico version 1.0. Root elements: "
               "NominaIndividual (TipoXML 102) and NominaIndividualDeAjuste (TipoXML 103)."),
    ("Character encoding", "UTF-8 ONLY. Anexo s.9.7.1. Any other encoding is rejected at unzip time."),
    ("Transport packaging", "The XML is placed in a ZIP; the ZIP is base64-encoded; the base64 string "
                            "is the single wcf:contentFile parameter of SendNominaSync."),
    ("Maximum size", "500 KB for the transmitted payload."),
    ("Signature", "XAdES-EPES enveloped signature inside "
                  "/NominaIndividual/UBLExtensions/UBLExtension/ExtensionContent/ds:Signature, using "
                  "an X.509 certificate from a certification authority accredited by ONAC. The "
                  "ClaimedRole must be thirdparty or supplier (Anexo s.7)."),
    ("Decimal convention", "Two decimals, decimal POINT, no thousand separators, no currency symbol. "
                           "Rounding is round-half-to-even; validation tolerance is +/- 2.00."),
    ("Date / time convention", "Dates AAAA-MM-DD. Times HH:MM:SS with the GMT offset, always -05:00 "
                               "for Colombia (no daylight saving). Overtime start / end times use "
                               "the 19-character form AAAA-MM-DDTHH:MM:SS."),

    ("##", "TRANSPORT - SOAP 1.2 WEB SERVICE (Anexo s.9)"),
    ("Protocol", "SOAP 1.2, Style/Encoding Document/Literal, over HTTPS with TLS 1.2 and MUTUAL "
                 "authentication by digital certificate."),
    ("Security model", "WS-Security 1.0 (OASIS) with X.509 Certificate Token Profile 1.1."),
    ("Namespaces", "soap = http://www.w3.org/2003/05/soap-envelope ; "
                   "wcf = http://wcf.dian.colombia"),
    ("Submission operation", "SendNominaSync - one parameter, wcf:contentFile, carrying the base64 "
                             "of the ZIP. Synchronous."),
    ("Response action", "http://wcf.dian.colombia/IWcfDianCustomerServices/SendNominaSyncResponse"),
    ("Query operation", "GetStatus - retrieves the status of a previously transmitted document "
                        "(Anexo s.9.8)."),
    ("Server-side checks, in order", "1. ZIP is not empty. 2. ZIP is not corrupt. 3. The UBL 2.1 "
                                     "signed section exists. 4. The document matches the "
                                     "NominaIndividual or NominaIndividualDeAjuste XSD. 5. No error "
                                     "against the Anexo's own structural rules. Only then is the "
                                     "ApplicationResponse produced."),

    ("##", "XML STRUCTURE - NominaIndividual (root, TipoXML 102)"),
    ("", "NominaIndividual"),
    ("", "  |-- UBLExtensions                                   NIE001   1-1"),
    ("", "  |     +-- UBLExtension/ExtensionContent/ds:Signature          1-1  (XAdES-EPES)"),
    ("", "  |-- Novedad  @CUNENov                               NIE199 / NIE204   0-1"),
    ("", "  |-- Periodo  @FechaIngreso @FechaRetiro"),
    ("", "  |            @FechaLiquidacionInicio @FechaLiquidacionFin"),
    ("", "  |            @TiempoLaborado @FechaGen              NIE002-NIE008     1-1"),
    ("", "  |-- NumeroSecuenciaXML  @CodigoTrabajador @Prefijo"),
    ("", "  |            @Consecutivo @Numero                   NIE009-NIE012     1-1"),
    ("", "  |-- LugarGeneracionXML  @Pais @DepartamentoEstado"),
    ("", "  |            @MunicipioCiudad @Idioma               NIE013-NIE016     1-1"),
    ("", "  |-- ProveedorXML  @RazonSocial @PrimerApellido @SegundoApellido"),
    ("", "  |            @PrimerNombre @OtrosNombres @NIT @DV"),
    ("", "  |            @SoftwareID @SoftwareSC                NIE205-NIE020     1-1"),
    ("", "  |-- CodigoQR                                        NIE021   1-1"),
    ("", "  |-- InformacionGeneral  @Version @Ambiente @TipoXML @CUNE"),
    ("", "  |            @EncripCUNE @FechaGen @HoraGen"),
    ("", "  |            @PeriodoNomina @TipoMoneda @TRM        NIE022-NIE200     1-1"),
    ("", "  |-- Notas                                           NIE031   0-N"),
    ("", "  |-- Empleador  @RazonSocial @PrimerApellido @SegundoApellido"),
    ("", "  |            @PrimerNombre @OtrosNombres @NIT @DV @Pais"),
    ("", "  |            @DepartamentoEstado @MunicipioCiudad"),
    ("", "  |            @Direccion                             NIE032-NIE038     1-1"),
    ("", "  |-- Trabajador  @TipoTrabajador @SubTipoTrabajador"),
    ("", "  |            @AltoRiesgoPension @TipoDocumento @NumeroDocumento"),
    ("", "  |            @PrimerApellido @SegundoApellido @PrimerNombre"),
    ("", "  |            @OtrosNombres @LugarTrabajoPais"),
    ("", "  |            @LugarTrabajoDepartamentoEstado"),
    ("", "  |            @LugarTrabajoMunicipioCiudad @LugarTrabajoDireccion"),
    ("", "  |            @SalarioIntegral @TipoContrato @Sueldo"),
    ("", "  |            @CodigoTrabajador                      NIE041-NIE063     1-1"),
    ("", "  |-- Pago  @Forma @Metodo @Banco @TipoCuenta"),
    ("", "  |            @NumeroCuenta                          NIE064-NIE068     1-1"),
    ("", "  |-- FechasPagos"),
    ("", "  |     +-- FechaPago                                 NIE203   1-N"),
    ("", "  |-- Devengados"),
    ("", "  |     |-- Basico  @DiasTrabajados @SueldoTrabajado  NIE069-NIE070     1-1"),
    ("", "  |     |-- Transporte  @AuxilioTransporte"),
    ("", "  |     |        @ViaticoManuAlojS @ViaticoManuAlojNS NIE071-NIE073     0-N"),
    ("", "  |     |-- HEDs/HED       @HoraInicio @HoraFin @Cantidad @Porcentaje @Pago   0-N"),
    ("", "  |     |-- HENs/HEN       (same five attributes)                             0-N"),
    ("", "  |     |-- HRNs/HRN       (same five attributes)                             0-N"),
    ("", "  |     |-- HEDDFs/HEDDF   (same five attributes)                             0-N"),
    ("", "  |     |-- HRDDFs/HRDDF   (same five attributes)                             0-N"),
    ("", "  |     |-- HENDFs/HENDF   (same five attributes)                             0-N"),
    ("", "  |     |-- HRNDFs/HRNDF   (same five attributes)                             0-N"),
    ("", "  |     |-- Vacaciones/Comunes    @FechaInicio @FechaFin @Cantidad @Pago      0-N"),
    ("", "  |     |-- Vacaciones/Compensadas @Cantidad @Pago                            0-N"),
    ("", "  |     |-- Primas    @Cantidad @Pago @PagoNS         NIE117-NIE119     0-1"),
    ("", "  |     |-- Cesantias @Pago @Porcentaje @PagoIntereses NIE120-NIE122    0-1"),
    ("", "  |     |-- Incapacidades/Incapacidad @FechaInicio @FechaFin"),
    ("", "  |     |        @Cantidad @Tipo @Pago                NIE123-NIE127     0-N"),
    ("", "  |     |-- Licencias/LicenciaMP  @FechaInicio @FechaFin @Cantidad @Pago      0-N"),
    ("", "  |     |-- Licencias/LicenciaR   @FechaInicio @FechaFin @Cantidad @Pago      0-N"),
    ("", "  |     |-- Licencias/LicenciaNR  @FechaInicio @FechaFin @Cantidad           0-N"),
    ("", "  |     |-- Bonificaciones/Bonificacion @BonificacionS @BonificacionNS        0-N"),
    ("", "  |     |-- Auxilios/Auxilio      @AuxilioS @AuxilioNS                        0-N"),
    ("", "  |     |-- HuelgasLegales/HuelgaLegal @FechaInicio @FechaFIn @Cantidad       0-N"),
    ("", "  |     |-- OtrosConceptos/OtroConcepto @DescripcionConcepto"),
    ("", "  |     |        @ConceptoS @ConceptoNS               NIE146-NIE148     0-N"),
    ("", "  |     |-- Compensaciones/Compensacion @CompensacionO @CompensacionE         0-N"),
    ("", "  |     |-- BonoEPCTVs/BonoEPCTV @PagoS @PagoNS"),
    ("", "  |     |        @PagoAlimentacionS @PagoAlimentacionNS NIE151-NIE154    0-N"),
    ("", "  |     |-- Comisiones/Comision                       NIE155   0-N"),
    ("", "  |     |-- PagosTerceros/PagoTercero                 NIE193   0-N"),
    ("", "  |     |-- Anticipos/Anticipo                        NIE194   0-N"),
    ("", "  |     |-- Dotacion                                  NIE156   0-1"),
    ("", "  |     |-- ApoyoSost                                 NIE157   0-1"),
    ("", "  |     |-- Teletrabajo                               NIE158   0-1"),
    ("", "  |     |-- BonifRetiro                               NIE159   0-1"),
    ("", "  |     |-- Indemnizacion                             NIE160   0-1"),
    ("", "  |     +-- Reintegro                                 NIE201   0-1"),
    ("", "  |-- Deducciones"),
    ("", "  |     |-- Salud        @Porcentaje @Deduccion       NIE161 / NIE163   1-1"),
    ("", "  |     |-- FondoPension @Porcentaje @Deduccion       NIE164 / NIE166   1-1"),
    ("", "  |     |-- FondoSP      @Porcentaje @DeduccionSP"),
    ("", "  |     |        @PorcentajeSub @DeduccionSub         NIE167-NIE170     0-1"),
    ("", "  |     |-- Sindicato    @Porcentaje @Deduccion       NIE171 / NIE172   0-N"),
    ("", "  |     |-- Sanciones/Sancion @SancionPublic @SancionPriv NIE173/NIE174 0-N"),
    ("", "  |     |-- Libranzas/Libranza @Descripcion @Deduccion NIE175 / NIE176  0-N"),
    ("", "  |     |-- PagosTerceros/PagoTercero                 NIE195   0-N"),
    ("", "  |     |-- Anticipos/Anticipo                        NIE196   0-N"),
    ("", "  |     |-- OtrasDeducciones/OtraDeduccion            NIE197   0-N"),
    ("", "  |     |-- PensionVoluntaria                         NIE198   0-1"),
    ("", "  |     |-- RetencionFuente                           NIE177   0-1"),
    ("", "  |     |-- AFC                                       NIE179   0-1"),
    ("", "  |     |-- Cooperativa                               NIE180   0-1"),
    ("", "  |     |-- EmbargoFiscal                             NIE181   0-1"),
    ("", "  |     |-- PlanComplementarios                       NIE182   0-1"),
    ("", "  |     |-- Educacion                                 NIE183   0-1"),
    ("", "  |     |-- Reintegro                                 NIE184   0-1"),
    ("", "  |     +-- Deuda                                     NIE185   0-1"),
    ("", "  |-- Redondeo                                        NIE186   0-1"),
    ("", "  |-- DevengadosTotal                                 NIE187   1-1"),
    ("", "  |-- DeduccionesTotal                                NIE188   1-1"),
    ("", "  +-- ComprobanteTotal                                NIE189   1-1"),

    ("##", "XML STRUCTURE - NominaIndividualDeAjuste (root, TipoXML 103)"),
    ("", "NominaIndividualDeAjuste"),
    ("", "  |-- TipoNota                       NIAE214   1-1   1 Reemplazar | 2 Eliminar"),
    ("", "  |-- Reemplazar        (present only when TipoNota = 1)"),
    ("", "  |     +-- <the ENTIRE NominaIndividual structure, NIAE-prefixed>"),
    ("", "  +-- Eliminar          (present only when TipoNota = 2)"),
    ("", "        +-- <reduced structure; CUNE computed with ValDev = ValDed = ValTol = 0.00"),
    ("", "            and DocEmp = 0, per Anexo s.8.1.1.4>"),

    ("##", "MANDATORY CONTENT - Resolucion DIAN 000013 de 2021 art. 5 (13 items)"),
    ("Item 1", "Employer surnames and names or corporate name, and tax identification number "
               "(NIE032 / NIE210-213, NIE033, NIE034)."),
    ("Item 2", "Employee surnames and names, and identity document number (NIE046-NIE049, NIE045)."),
    ("Item 3", "Unique consecutive document number preceded by the authorised prefix (NIE010-NIE012)."),
    ("Item 4", "Generation date (NIE026)."),
    ("Item 5", "Payment or credit date (NIE203)."),
    ("Item 6", "Accrued payroll values, itemised by concept (the whole Devengados block)."),
    ("Item 7", "Deducted payroll values, itemised by concept (the whole Deducciones block)."),
    ("Item 8", "Total difference between accrued and deducted (NIE187, NIE188, NIE189)."),
    ("Item 9", "Payment or credit period (NIE004, NIE005)."),
    ("Item 10", "Payment method and medium (NIE064, NIE065)."),
    ("Item 11", "Country, department and municipality of origin (NIE035, NIE036, NIE037)."),
    ("Item 12", "Content of the authorised technical annex (the whole document)."),
    ("Item 13", "CUNE - the unique electronic payroll code (NIE024)."),

    ("##", "CONTROL MECHANISMS"),
    ("CUNE (Anexo s.8.1)", "SHA-384 of NumNE + FecNE + HorNE + ValDev + ValDed + ValTolNE + NitNE + "
                           "DocEmp + TipoXML + Software-Pin + TipAmb, concatenated with no "
                           "separators. Money inputs are TRUNCATED to two decimals, not rounded. "
                           "Result is 96 lower-case hexadecimal characters."),
    ("SoftwareSC (Anexo s.8.2)", "SHA-384 of SoftwareID + PIN + document number. Changes with every "
                                 "document, unlike SoftwareID."),
    ("TiempoLaborado (Anexo s.8.3.1)", "Days on the 360/30 commercial convention: "
                                       "(years x 360) + (months x 30) + odd days. Annex example: "
                                       "5 years + 3 months + 18 days = 1908.00."),
    ("QR (Anexo s.13.1)", "URL of the DIAN document-search service keyed on the CUNE. If a graphical "
                          "representation is issued, the QR must be at least 2 cm x 2 cm on EVERY "
                          "page."),
    ("Key validation rules", "NIE022 - the Version literal must be exactly 'V1.0: Documento Soporte "
                             "de Pago de Nomina Electronica'. Global rule 90 - a document number may "
                             "be transmitted only ONCE per employee. Global rule 92 - a document "
                             "from a non-enabled issuer is rejected. Full rule set at Anexo s.6.1."),
]

# ===========================================================================
#  SHEET 6 - FIELD OPTIONS
# ===========================================================================
CFG["options"] = [
    "AMBIENTE - destination environment (Anexo table 5.1.1, NIE023)",
    ("1", "Produccion", "Produccion", "Production. Documents have legal effect."),
    ("2", "Pruebas", "Pruebas / Habilitacion", "Test. Used for the DIAN enablement process. Because "
     "Ambiente is an input to the CUNE, a test document can never be replayed into production."),

    "ALGORITMO CUNE (Anexo table 5.1.2, NIE025)",
    ("CUNE-SHA384", "SHA-384", "CUNE-SHA384", "The only permitted value. Declares that the CUNE in "
     "NIE024 is a SHA-384 digest."),

    "VERSION LITERAL (NIE022) - a constant, not a code table",
    ("(literal)", "V1.0", "V1.0: Documento Soporte de Pago de Nomina Electronica",
     "Must be emitted character for character, accents included. Validation rule NIE022 rejects any "
     "variation, including a trimmed or unaccented form."),

    "TIPO DE DOCUMENTO DE IDENTIFICACION (Anexo table 5.2.1, NIE044)",
    ("11", "RC", "Registro civil", "Civil birth registration. Used for minors."),
    ("12", "TI", "Tarjeta de identidad", "Identity card for a person aged 7 to 17."),
    ("13", "CC", "Cedula de ciudadania", "National identity card. The overwhelming majority of "
     "Colombian employees."),
    ("21", "TE", "Tarjeta de extranjeria", "Foreigner's identity card."),
    ("22", "CE", "Cedula de extranjeria", "Foreign resident's identity card."),
    ("31", "NIT", "NIT", "Tax identification number. Used where the beneficiary is an entity."),
    ("41", "PA", "Pasaporte", "Passport. See CO-GAP-07: an alphanumeric passport number cannot "
     "satisfy the xsd:integer typing of NIE045."),
    ("42", "DIE", "Documento de identificacion extranjero", "Foreign identity document."),
    ("47", "PEP", "PEP - Permiso Especial de Permanencia", "Special residence permit. CO-GAP-06: "
     "there is NO code for the PPT (Permiso por Proteccion Temporal, Decreto 216 de 2021, created "
     "one month after this annex), which the large majority of regularised Venezuelan migrants now "
     "hold. Code 47 is the only available proxy."),
    ("50", "NIT-EXT", "NIT de otro pais", "Foreign tax identification number."),
    ("91", "NUIP", "NUIP", "Unique personal identification number. The annex restricts this code to "
     "the EMPLOYEE, because it is not a RUT document type."),

    "PERIODO DE NOMINA (Anexo table 5.5.1, NIE029)",
    ("1", "SEM", "Semanal", "Weekly."),
    ("2", "DEC", "Decenal", "Every ten days."),
    ("3", "CAT", "Catorcenal", "Every fourteen days."),
    ("4", "QUI", "Quincenal", "Semi-monthly - the most common Colombian cycle. Still ONE monthly "
     "document, carrying two FechaPago occurrences."),
    ("5", "MEN", "Mensual", "Monthly."),
    ("6", "OTR", "Otro", "Any other cycle."),

    "TIPO DE CONTRATO (Anexo table 5.5.2, NIE061)",
    ("1", "FIJO", "Termino Fijo", "Fixed-term contract. CST art. 46; maximum four years after "
     "Ley 2466 de 2025 art. 6."),
    ("2", "INDEF", "Termino Indefinido", "Indefinite-term contract. CST art. 47."),
    ("3", "OBRA", "Obra o Labor", "Contract for a specific work or task. CST art. 46."),
    ("4", "APREN", "Aprendizaje", "Apprenticeship. Ley 2466 de 2025 art. 21 recast this as a special "
     "fixed-term LABOUR contract, regulated by Decreto 0223 of 5 March 2026."),
    ("5", "PRACT", "Practicas o Pasantias", "Internship or practical placement."),

    "TIPO DE TRABAJADOR (Anexo table 5.5.3, NIE041) - 16 values only",
    ("01", "DEP", "Dependiente", "Standard employee. The default for corporate payroll."),
    ("02", "DOM", "Servicio domestico", "Domestic service worker."),
    ("04", "MAD", "Madre comunitaria", "Community mother."),
    ("12", "APR-L", "Aprendices del Sena en etapa lectiva", "SENA apprentice, classroom phase."),
    ("18", "FUN", "Funcionarios publicos sin tope maximo de ibc", "Public official with no "
     "contribution-base ceiling."),
    ("19", "APR-P", "Aprendices del SENA en etapa productiva", "SENA apprentice, productive phase."),
    ("21", "EST-PG", "Estudiantes de postgrado en salud", "Health postgraduate student. "
     "Same mnemonic as the PILA tipo cotizante 21 and the DD Worker Type mapper."),
    ("22", "PROF", "Profesor de establecimiento particular", "Teacher at a private establishment."),
    ("23", "EST-RL", "Estudiantes aportes solo riesgos laborales", "Student contributing to "
     "occupational risk only."),
    ("30", "DEP-ESP", "Dependiente entidades o universidades publicas con regimen especial en salud",
     "Employee of a public entity or university under a special health regime."),
    ("31", "COOP", "Cooperados o pre cooperativas de trabajo asociado", "Associated-work cooperative "
     "member. The only worker type for which the Compensacion elements (NIE149 / NIE150) apply."),
    ("47", "SGP", "Trabajador dependiente de entidad beneficiaria del sistema general de "
     "participaciones - aportes patronales", "Employee of an SGP-beneficiary entity. Public sector; "
     "PILA planilla types T and F are descoped in scope_manifest."),
    ("51", "PARC", "Trabajador de tiempo parcial", "Part-time worker under the special partial-time "
     "contribution regime."),
    ("54", "PREP", "Pre pensionado de entidad en liquidacion", "Pre-pensioner of an entity in "
     "liquidation."),
    ("56", "PREP-V", "Pre pensionado con aporte voluntario a salud", "Pre-pensioner with a voluntary "
     "health contribution."),
    ("58", "EST-PUB", "Estudiantes de practicas laborales en el sector publico", "Student on a public-"
     "sector work placement."),
    ("(mapping warning)", "-", "-", "This 16-value list is a SUBSET of the PILA tipo cotizante list, "
     "which carries far more values (03, 16, 20, 32 to 45, 52, 53, 55, 57, 59 to 63). The engine "
     "must MAP between the two, never copy: a PILA code with no DIAN equivalent is not valid here."),

    "SUBTIPO DE TRABAJADOR (Anexo table 5.5.4, NIE042) - only 2 values",
    ("00", "NA", "No Aplica", "Does not apply. The value for almost every employee."),
    ("01", "PEN", "Dependiente pensionado por vejez activo", "Employed old-age pensioner in active "
     "service. Pension contribution is nil, so NIE164 (pension rate) must be 0.00."),
    ("(mapping warning)", "-", "-", "The PILA subtipo cotizante list carries twelve values "
     "(00 to 06, 09 to 12). Only 00 and 01 exist here."),

    "TIPO DE HORA EXTRA O RECARGO / OVERTIME - SURCHARGE TYPE (Anexo table 5.5.5, "
    "@Porcentaje on the 7 hour blocks)",
    ("1", "HED", "Hora Extra Diurna", "Day overtime. Annex percentage 25.00. CST art. 168."),
    ("2", "HEN", "Hora Extra Nocturna", "Night overtime. Annex percentage 75.00."),
    ("3", "HRN", "Hora Recargo Nocturno", "Night-work surcharge. Annex percentage 35.00. The "
     "night window is 21:00 to 06:00 following Ley 2101 de 2021."),
    ("4", "HEDDF", "Hora Extra Diurna Dominical y Festivos", "Sunday / holiday day overtime. Annex "
     "percentage 100.00."),
    ("5", "HRDDF", "Hora Recargo Diurno Dominical y Festivos", "Sunday / holiday day surcharge. Annex "
     "percentage 75.00."),
    ("6", "HENDF", "Hora Extra Nocturna Dominical y Festivos", "Sunday / holiday night overtime. "
     "Annex percentage 150.00."),
    ("7", "HRNDF", "Hora Recargo Nocturno Dominical y Festivos", "Sunday / holiday night surcharge. "
     "Annex percentage 110.00."),
    ("(source conflict)", "-", "-", "ESCALATE. The annex percentages for codes 4, 5, 6 and 7 embed a "
     "75% Sunday / public-holiday surcharge. Ley 2101 de 2021 and Ley 2466 de 2025 raise that "
     "surcharge to 80% from 1 July 2025 and to 90% from 1 JULY 2026, so from that date the statutory "
     "rate diverges from the printed annex value. The annex is still at version 1.0 and DIAN has not "
     "reissued table 5.5.5. A written DIAN position is required on whether @Porcentaje must carry "
     "the annex value or the statutory value."),

    "TIPO DE INCAPACIDAD (Anexo table 5.5.6, NIE126)",
    ("1", "COM", "Comun", "General illness. The employer bears days 1-2 (Decreto 780 de 2016 "
     "art. 3.2.1.10); the EPS funds from day 3. CO-GAP-03: the first-two-days rate is a Mercans "
     "configurable default of 66.67%."),
    ("2", "PROF", "Profesional", "Occupational disease. Funded by the ARL from day one at 100%."),
    ("3", "LAB", "Laboral", "Occupational accident. Funded by the ARL from day one at 100%."),

    "TIPO DE XML (Anexo table 5.5.7, NIE202 / NIAE202)",
    ("102", "NI", "NominaIndividual", "Documento Soporte de Pago de Nomina Electronica - the payroll "
     "support document itself."),
    ("103", "NIA", "NominaIndividualDeAjuste", "Nota de Ajuste - the adjustment note."),

    "TIPO DE NOTA DE AJUSTE (Anexo table 5.5.8, NIAE214)",
    ("1", "REEMP", "Reemplazar", "Replace. Used for arithmetic, accounting or content errors. The "
     "Reemplazar block repeats the entire document with corrected values and carries its own CUNE."),
    ("2", "ELIM", "Eliminar", "Cancel. Used where a document was transmitted in error. The annex "
     "warns expressly that this only INVALIDATES the erroneous document; a corrected document must "
     "follow. Its CUNE is computed with ValDev, ValDed and ValTol forced to 0.00 and DocEmp to 0."),

    "FORMA DE PAGO (Anexo table 5.3.3.1, NIE064)",
    ("1", "CONT", "Contado", "Cash / immediate settlement. The annex publishes this single value."),

    "MEDIO DE PAGO (Anexo table 5.3.3.2, NIE065) - realistic payroll subset of the 1-97 list",
    ("10", "EFEC", "Efectivo", "Cash. Where used, the Banco, TipoCuenta and NumeroCuenta attributes "
     "(NIE066-NIE068) must be absent."),
    ("20", "CHEQ", "Cheque", "Cheque."),
    ("42", "CONS", "Consignacion bancaria", "Bank deposit. The most common Colombian payroll method."),
    ("45", "TCB", "Transferencia Credito Bancario", "Bank credit transfer."),
    ("47", "TDB", "Transferencia Debito Bancaria", "Bank debit transfer."),
    ("48", "TCRE", "Tarjeta Credito", "Credit card."),
    ("49", "TDEB", "Tarjeta Debito", "Debit card."),
    ("71", "BON", "Bonos", "Vouchers. Where salary is paid in vouchers the amount also belongs in "
     "the BonoEPCTV devengado elements (NIE151-NIE154)."),
    ("72", "VAL", "Vales", "Vales / meal tickets."),
    ("(full list)", "-", "-", "The complete UN/EDIFACT 4461 medium-of-payment catalogue, codes 1 to "
     "97, is printed at Anexo table 5.3.3.2. Only the subset above is realistic for Colombian "
     "payroll."),

    "IDIOMA (Anexo table 5.3.1, NIE016) and MONEDA (table 5.3.2, NIE030)",
    ("es", "ES", "Espanol", "ISO 639-1. Spanish is MANDATORY on the graphical representation "
     "(Res. 000013 de 2021 art. 26); another language may be added, never substituted."),
    ("COP", "COP", "Peso colombiano", "ISO 4217. The Colombian peso is MANDATORY (art. 26). The TRM "
     "element (NIE200) exists for foreign-currency documents but is out of scope for Colombian "
     "payroll."),

    "GEOGRAPHIC CODES - PAISES (Anexo table 5.4.1), DEPARTAMENTOS (table 5.4.2) and "
    "MUNICIPIOS (table 5.4.3)",
    ("CO", "CO", "Colombia", "ISO 3166-1 alpha-2, table 5.4.1."),
    ("11", "BOG", "Bogota D.C.", "DANE DIVIPOLA department code, table 5.4.2 (ISO 3166-2:CO)."),
    ("11001", "BOG", "Bogota D.C.", "DANE DIVIPOLA municipality code, table 5.4.3. Positions 1-2 are "
     "the department, positions 3-5 the municipality. The annex prints the full national catalogue "
     "at pages 144-178."),

    "CONTRIBUTION RATES 2026 (context for the Deducciones rate attributes)",
    ("4.00", "Salud EE", "Salud - aporte del trabajador",
     "Employee health rate for NIE161. The employer's 8.5% is not an employee deduction."),
    ("4.00", "Pension EE", "Pension - aporte del trabajador",
     "Employee pension rate for NIE164. Employer 12%; total 16%. Set to 0.00 for an employed "
     "old-age pensioner (SubTipoTrabajador 01)."),
    ("1.00", "FSP solidaridad", "Fondo de solidaridad pensional - subcuenta de solidaridad",
     "NIE167. Trigger: contribution base at or above 4 SMMLV = COP 7,003,620 in 2026."),
    ("0.20 - 1.00", "FSP subsistencia", "Fondo de solidaridad pensional - subcuenta de subsistencia",
     "NIE169. Banded, from 16 SMMLV = COP 28,014,480. See the band table below."),

    "SOLIDARITY PENSION FUND BANDS (Ley 100 art. 20 as substituted by Ley 797 de 2003 art. 7)",
    ("4 to 16 SMMLV", "1.0% / 0%", "Solo subcuenta de solidaridad",
     "COP 7,003,620 to 28,014,480. Solidarity 1.0%; subsistence nil. Total 1.0%."),
    ("16 to 17 SMMLV", "1.0% / 0.2%", "Solidaridad + subsistencia",
     "COP 28,014,480 to 29,765,385. Total 1.2%."),
    ("17 to 18 SMMLV", "1.0% / 0.4%", "Solidaridad + subsistencia", "Total 1.4%."),
    ("18 to 19 SMMLV", "1.0% / 0.6%", "Solidaridad + subsistencia", "Total 1.6%."),
    ("19 to 20 SMMLV", "1.0% / 0.8%", "Solidaridad + subsistencia", "Total 1.8%."),
    ("above 20 SMMLV", "1.0% / 1.0%", "Solidaridad + subsistencia", "Total 2.0%, up to the 25-SMMLV "
     "contribution ceiling of COP 43,772,625."),
    ("(pension reform)", "-", "Ley 2381 de 2024",
     "Ley 2381 de 2024 would REPLACE this two-account structure with a single five-band scale "
     "(1.5 / 1.8 / 2.5 / 2.8 / 3.0%). Its entry into force was SUSPENDED by Constitutional Court "
     "Auto 841 of 18 June 2025 pending a re-run of the fourth plenary debate. Until that is cured "
     "the table above remains in force. Monitor."),

    "CESANTIAS INTEREST RATE (NIE121)",
    ("12.00", "12%", "Intereses sobre cesantias",
     "12% per annum on the 31 December balance, or pro rata for a partial year (Ley 52 de 1975 "
     "art. 1). Paid TO THE EMPLOYEE during January. Ley 2466 de 2025 art. 64 permits monthly payment "
     "of the 1% by written agreement."),

    "VALIDATION OUTCOME (inbound ApplicationResponse, INB-03)",
    ("Aceptado", "OK", "Documento validado", "Accepted. Store the CUNE and the validation timestamp; "
     "the payroll cost is now supported for income-tax purposes."),
    ("Rechazado", "KO", "Documento rechazado", "Rejected. Store the rule codes from INB-04, correct "
     "and re-transmit with a NEW consecutive number - rule 90 forbids reuse."),
    ("(rule NIE022)", "-", "Version literal incorrecta", "The Version element does not carry the "
     "exact required literal."),
    ("(rule 90)", "-", "Numero de documento repetido", "That document number has already been "
     "transmitted for that employee."),
    ("(rule 92)", "-", "Emisor no habilitado", "The issuer is not enabled in the DIAN payroll "
     "platform. This is an enablement failure, not a data failure."),
]

# ===========================================================================
#  SHEET 7 - POPULATION RULES
# ===========================================================================
CFG["population"] = [
    "MANDATORY FIELD RULES",
    ("Version (NIE022)", "Configuration",
     "Emit the constant string 'V1.0: Documento Soporte de Pago de Nomina Electronica' exactly, "
     "including accents and the colon-space. Never build it from a version variable, never trim, "
     "never transliterate. Validation rule NIE022 compares the whole literal.",
     "A configuration file saved as ASCII will silently strip the accent on 'Nomina' and every "
     "document will be rejected."),
    ("Numero (NIE012)", "Engine sequence + configuration",
     "Concatenate the DIAN-authorised Prefijo (NIE010) with the next unused Consecutivo (NIE011), "
     "with no separator. Persist the last-used consecutive per prefix range in a transactional "
     "store, and increment it BEFORE transmission, never after, so that a failed transmission does "
     "not leave a reusable number. Global rule 90 permits a given number only once per employee.",
     "A rejected document consumes its number. On re-transmission the corrected document must carry "
     "a NEW consecutive. Never re-send a rejected number."),
    ("CUNE (NIE024)", "Engine (computed)",
     "Compute SHA-384 over the eleven inputs concatenated with no separators, in the published "
     "order: Numero, FechaGen, HoraGen (with the -05:00 offset), DevengadosTotal, DeduccionesTotal, "
     "ComprobanteTotal, employer NIT (no DV), employee document number, TipoXML, the secret software "
     "PIN, and Ambiente. The three money inputs must be TRUNCATED to two decimals - not rounded - "
     "and written with a decimal point, no thousand separators and no currency symbol. Emit the "
     "result as 96 lower-case hexadecimal characters.",
     "The four classic failures: (1) rounding instead of truncating the money inputs; (2) omitting "
     "the -05:00 offset from HoraGen; (3) including the employer DV in NitNE; (4) using the "
     "SoftwareID instead of the PIN. All four produce a well-formed but wrong CUNE."),
    ("SoftwareSC (NIE020)", "Engine (computed)",
     "Compute SHA-384 over SoftwareID + PIN + document number. Recompute for EVERY document, because "
     "the document number is an input. Do not cache it at software level.",
     "Caching SoftwareSC as if it were a constant is a common error - it is constant only for a "
     "single document."),
    ("TiempoLaborado (NIE006)", "Engine (computed)",
     "Compute cumulative service from FechaIngreso to FechaLiquidacionFin on the Colombian "
     "commercial convention: 1 year = 360 days, 1 month = 30 days. Decompose the elapsed period into "
     "whole years, whole months and residual days, then evaluate (years x 360) + (months x 30) + "
     "days. Emit with two decimals. The annex's own example is 5 years + 3 months + 18 days = 1908.00.",
     "Do NOT use a calendar day-count. A naive (date2 - date1).days gives 1913 for the annex's own "
     "example instead of 1908, and DIAN will not flag it - the error surfaces only in a seniority "
     "dispute."),
    ("DiasTrabajados (NIE069)", "Payroll engine",
     "Days actually worked and paid in the period on the 30-day commercial month. Start at 30 (or "
     "the number of days from a mid-month hire), then subtract unpaid-leave days (LicenciaNR), "
     "suspension days and lawful-strike days. Do NOT subtract incapacity, maternity or vacation days "
     "- those are paid and appear in their own devengado blocks.",
     "February always counts 30 days in Colombian payroll, not 28. A 31-day month also counts 30."),

    "CRITICAL VALIDATION RULES",
    ("DevengadosTotal / DeduccionesTotal / ComprobanteTotal (NIE187-NIE189)", "Engine (computed)",
     "DevengadosTotal is the sum of every populated element in the Devengados block; DeduccionesTotal "
     "is the sum of every populated element in Deducciones; ComprobanteTotal is DevengadosTotal minus "
     "DeduccionesTotal, adjusted for the Redondeo residual. Each element is first rounded "
     "half-to-even to two decimals, then summed - not summed and then rounded. Where a residual "
     "remains, disclose it in Redondeo (NIE186) rather than absorbing it into a concept. Validation "
     "tolerance is +/- 2.00.",
     "Summing unrounded values and rounding the total produces a figure that ties to the cent but "
     "does not match the sum of the printed lines on the payslip. Round first, then sum."),
    ("Salary / non-salary paired elements", "Wage-type configuration",
     "Every paired element (ViaticoManuAlojS / NS, BonificacionS / NS, AuxilioS / NS, ConceptoS / NS, "
     "PagoS / NS, PagoAlimentacionS / NS, Primas Pago / PagoNS) must be driven by a HARD salary / "
     "non-salary flag carried on the wage type and set at configuration time. Never infer the split "
     "at reporting time from the amount, the description or the wage-type name.",
     "The 40% non-salary clamp of Ley 1393 de 2010 art. 30 depends on this split, as does the "
     "contribution base. An inference error propagates into PILA and into the employer cost."),
    ("Employer contributions must never appear in Deducciones", "Wage-type configuration",
     "The Deducciones block reports only what was withheld FROM THE EMPLOYEE. The employer's 12% "
     "pension, 8.5% health, occupational-risk premium and the 9% payroll levies (SENA 2%, ICBF 3%, "
     "CCF 4%) are employer costs reported on PILA. Configure them on a cost, not a deduction, "
     "wage-type class so they cannot leak into this block.",
     "A single mis-classified employer wage type inflates DeduccionesTotal and understates "
     "ComprobanteTotal, which then disagrees with the actual bank payment."),
    ("Solidarity fund must not be merged into pension", "Wage-type configuration",
     "FondoSP carries FOUR attributes - the solidarity rate and amount, and the subsistence rate and "
     "amount. They are validated independently of FondoPension. Configure the solidarity surcharge "
     "as its own wage type from the outset.",
     "This is the single most common Colombian mapping error. Merging produces a 5% 'pension' line "
     "that fails reconciliation against PILA fields 47, 51 and 52."),
    ("Overtime cannot be aggregated", "Payroll engine",
     "Emit one element per contiguous block of hours of a single type. Split a block that crosses "
     "21:00 or midnight, because the applicable code changes. Populate quantity, percentage and "
     "amount for every block, plus start and end times where the client reports them.",
     "A block that crosses the 21:00 boundary but is emitted as a single HED element misstates both "
     "the code and the premium."),

    "AMOUNT FORMAT RULES",
    ("All monetary elements", "Engine (formatting)",
     "Two decimals, decimal POINT, no thousand separator, no currency symbol, no leading plus sign. "
     "Rounding is round-half-to-even (NTC 3711 / JIS Z 8401), not half-up. Negative values are not "
     "used in the accrued or deducted blocks; only Redondeo (NIE186) may legitimately be negative.",
     "A locale-aware formatter will emit a comma decimal separator in an es-CO locale and the "
     "document will fail schema validation."),
    ("Three rounding conventions coexist", "Engine (formatting)",
     "The XML uses two decimals round-half-to-even. PILA rounds the base UP to the peso and each "
     "contribution UP to the next multiple of 100. Formulario 350 rounds to the nearest 1,000. The "
     "same health contribution therefore legitimately appears as three different numbers in three "
     "artefacts. Store the unrounded value once and apply each convention at output time.",
     "Never display the PILA figure on the payslip as if it were the deduction. If the client wants "
     "it shown, it must be a separate, labelled line (CCG Module 10.3)."),
    ("Percentage attributes", "Configuration",
     "Rate attributes (NIE077 and the other six @Porcentaje, NIE161, NIE164, NIE167, NIE169, NIE121, "
     "NIE171) carry the rate itself, expressed to two decimals - 4.00 not 0.04, 25.00 not 0.25.",
     "Emitting 0.04 for the 4% health rate passes schema validation and produces a document that is "
     "internally inconsistent with @Deduccion."),

    "PAYROLL-SPECIFIC POPULATION RULES",
    ("RetencionFuente (NIE177) - RESIDENT", "Payroll engine (tax)",
     "Build the ET art. 388 depurated base: gross taxable payments, less the mandatory health, "
     "pension and solidarity-fund contributions (ingresos no constitutivos de renta), less the "
     "art. 387 deductions elected by the employee (dependants at 10% of gross capped at 32 UVT per "
     "month, prepaid health up to 16 UVT per month, housing-loan interest up to 100 UVT per month), "
     "less the 25% exempt income of art. 206 num. 10. Apply the two caps: deductions plus exempt "
     "income may not exceed 40% of gross less non-constitutive income, nor 1,340 UVT per year "
     "(Mercans apportions at 111.6667 UVT per month - see CO-GAP-05). Convert the resulting base to "
     "UVT at 52,374, read the art. 383 table, convert back to pesos, and approximate to the nearest "
     "1,000 under ET art. 868. Under Procedure 2 apply instead the fixed percentage recomputed each "
     "June and December on the preceding twelve months divided by 13.",
     "Exclude severance savings and the interest on them from the monthly base under BOTH procedures "
     "(art. 206 num. 4). Under Procedure 1 the statutory minimum service bonus gets its OWN separate "
     "read of the table (art. 385) and does not merge into the ordinary base. For a sub-30-day "
     "period apply the art. 385 rule: gross the payments to 30 days, read the table for a "
     "PERCENTAGE, then apply that percentage to the actual smaller payment - never read the table "
     "for an amount on the grossed-up figure."),
    ("RetencionFuente (NIE177) - NON-RESIDENT", "Payroll engine (tax)",
     "Apply a FLAT 20% to the GROSS payment under ET art. 408. Do not depurate: no deduction of the "
     "mandatory contributions, no art. 387 deductions, no 25% exempt income, no tax-free band, no "
     "Procedure 1 or 2 election. This applies to salary, to the service bonus, to severance savings, "
     "to dismissal indemnity, to equity income and to benefits in kind alike. Carry a residence flag "
     "with an effective date on the employee record, re-evaluate it EVERY period against the "
     "art. 10 test (more than 183 days in any 365-day period), and switch to the art. 383 table "
     "PROSPECTIVELY from the payment following the date the test is met.",
     "Never apply the switch retroactively and never true up the earlier months through payroll - "
     "DIAN Concepto 011108 of 29 June 2026 expressly rejects anticipating future residence. The "
     "employee reconciles on their own return. Where the work is performed ENTIRELY outside Colombia "
     "the income is foreign-source and there is no withholding at all; LugarTrabajoPais (NIE050) is "
     "the evidencing field. Treaty relief is applied ONLY on written client instruction with a "
     "residence certificate."),
    ("AuxilioTransporte (NIE071)", "Payroll engine",
     "Emit only where the employee's salary does not exceed 2 SMMLV (COP 3,501,810 in 2026). The "
     "2026 amount is COP 249,095 per month, prorated by days worked. Where the employee is above the "
     "threshold, OMIT the element rather than emitting zero.",
     "The allowance is NOT salary for contribution purposes but IS included in the base of cesantias, "
     "prima and the severance indemnity (Ley 1 de 1963 art. 7). Carrying a single 'transport' wage "
     "type with one base flag will get one of the two treatments wrong."),
    ("Cesantias (NIE120) and PagoIntereses (NIE122)", "Payroll engine",
     "Cesantias accrue at one month's salary per year of service, on salary plus the transport "
     "allowance. Interest accrues at 12% per annum on the 31 December balance and is paid TO THE "
     "EMPLOYEE during January. Where the client has adopted the Ley 2466 de 2025 art. 64 option, the "
     "8.33% is deposited monthly and the 1% interest paid monthly, by written agreement - a "
     "configurable engine option.",
     "Cesantias are EXCLUDED from the monthly withholding base but must still be reported here. They "
     "split THREE ways downstream - paid to the employee, deposited to the fund, and under the "
     "pre-1991 traditional regime - for Formulario 220 casillas 47-49 and Formato 2276 numerals "
     "18-20. Maintain the three buckets from the outset."),
    ("Meal payments (NIE153 / NIE154)", "Payroll engine",
     "Maintain the ET art. 387-1 split independently of the S / NS split: the amount UP TO 41 UVT per "
     "month (COP 2,147,334 in 2026) where salary does not exceed 310 UVT (COP 16,235,940) goes to "
     "Formato 2276 numeral 32, and the EXCESS goes to numeral 8. Both are still reported in the XML "
     "as PagoAlimentacionS or NS.",
     "Two orthogonal splits apply to the same amount - salary / non-salary for the XML and "
     "contributions, and under-41-UVT / excess for the information return. Model them as two "
     "independent attributes, not one."),
    ("Incapacity (NIE123-NIE127)", "Payroll engine",
     "Emit one Incapacidad element per episode with its dates, day count, type code and amount. For "
     "type 1 (comun) the employer bears days 1-2 and the EPS funds from day 3; for types 2 and 3 the "
     "ARL funds from day one at 100%. The employer ADVANCES the benefit and recovers it from the "
     "institution, so the amount here is what the employee received.",
     "CO-GAP-03: the first-two-days rate is a Mercans configurable default of 66.67% (CST art. 227 "
     "two-thirds for the first 90 days); the primary source does not state it. CO-GAP-04: the "
     "one-minimum-wage floor on incapacity pay follows settled practice, not a retrieved regulation. "
     "Both require the client's documented election."),
    ("AltoRiesgoPension (NIE043)", "Employee master data",
     "Set true where the employee performs an activity listed in Decreto Ley 2090 de 2003. The flag "
     "is always emitted (1-1); write the literal true or false, not 1 or 0.",
     "CO-GAP-02: the ADDITIONAL employer pension contribution for high-risk work (the Resolucion "
     "2388 rate table implies 26% total against the standard 16%, so ten additional points borne by "
     "the employer) and its precise base were not confirmed from a primary 2026 source. Verify "
     "before configuring any high-risk employee."),

    "CROSS-FIELD VALIDATIONS",
    ("NIE014 / NIE015 and NIE051 / NIE052", "Engine (validation)",
     "The five-digit municipality code must begin with the two-digit department code. Validate this "
     "for both the generation location and the place of work before transmission.",
     "DIVIPOLA codes are re-used across departments in their last three digits; only the full "
     "five-digit code is unique."),
    ("NIE065 and NIE066 / NIE067 / NIE068", "Engine (validation)",
     "Where the payment method is a bank-mediated medium (42, 45, 46, 47, 48, 49), the bank, account "
     "type and account number must all be present. Where it is 10 (Efectivo), all three must be absent.",
     "Colombia does NOT use IBAN. Account numbers are numeric, of bank-specific length, with no "
     "national check digit, so no structural validation is possible - only a bank-specific rule or "
     "pre-notification."),
    ("NIE199 and NIE204", "Engine (validation)",
     "Where the Novedad element is present, CUNENov is mandatory inside it; where Novedad is absent, "
     "CUNENov must not appear. Bidirectional.",
     "A Novedad without a referenced CUNE breaks the cross-reference chain for the employment "
     "relationship."),
    ("NIAE214 and the Reemplazar / Eliminar blocks", "Engine (validation)",
     "TipoNota = 1 requires the Reemplazar block and forbids Eliminar; TipoNota = 2 requires "
     "Eliminar and forbids Reemplazar. Mutually exclusive.",
     "The Eliminar CUNE uses ValDev = ValDed = ValTol = 0.00 and DocEmp = 0 (Anexo s.8.1.1.4). A "
     "shared CUNE routine that reads the real totals will produce a wrong hash for cancellations."),
    ("NIE041 and NIE042 and NIE164", "Engine (validation)",
     "Where SubTipoTrabajador (NIE042) = 01 (employed old-age pensioner), the pension rate NIE164 "
     "must be 0.00 and no pension deduction may be emitted.",
     "The PILA equivalent (subtipo 1, 2, 3, 4, 5, 6, 9 or 12 forces field 46 to zero) is broader; "
     "map, do not copy."),
    ("NIE157 and NIE061 and NIE041", "Engine (validation)",
     "Where the apprentice maintenance support (NIE157) is populated, the contract type must be 4 "
     "(Aprendizaje) and the worker type must be 12 or 19.",
     "Ley 2466 de 2025 art. 21 made the apprenticeship a labour contract from 2026, so an apprentice "
     "now also generates a full PILA settlement - not only the support payment."),
    ("Cross-report reconciliation", "Engine (reconciliation)",
     "Monthly: SUM(NIE177) over all employees must equal Formulario 350 casilla 93 after the "
     "nearest-1,000 rounding. SUM(NIE163), SUM(NIE166) and SUM(NIE168 + NIE170) must equal the PILA "
     "totals for health, pension and the solidarity fund, allowing for PILA's round-up-to-100. "
     "Annually: the accumulation of each Devengados element must equal the corresponding Formulario "
     "220 casilla and Formato 2276 numeral.",
     "Run the reconciliation BEFORE transmission. A mismatch discovered after validation can only be "
     "corrected by an adjustment note, which consumes a new document number."),
]

# ===========================================================================
#  SHEET 8 - EXAMPLE ANALYSIS
# ===========================================================================
CFG["example"] = [
    "WORKED EXAMPLE - MARCH 2026, RESIDENT EMPLOYEE ON COP 12,000,000",
    ("(scenario)", "Employer", "MERCANS COLOMBIA S.A.S., NIT 900123456-7, Bogota D.C. "
     "(department 11, municipality 11001).",
     "The same employer, employee and period are used across all six Colombia Spec workbooks so the "
     "cross-report reconciliations can be followed end to end."),
    ("(scenario)", "Employee", "Juan Carlos Perez Gomez, cedula de ciudadania 1020304050, hired "
     "11 January 2021, indefinite-term contract, contractual salary COP 12,000,000, not integral, "
     "not high-risk, tax RESIDENT.",
     "Salary is above 2 SMMLV so there is no transport allowance, and below 16 SMMLV so there is no "
     "subsistence surcharge - which keeps the example legible while still exercising the solidarity "
     "surcharge."),

    "HEADER AND IDENTIFICATION",
    ("V1.0: Documento Soporte de Pago de Nomina Electronica", "Version (NIE022)",
     "The mandatory constant literal.", "Any deviation is rejected by rule NIE022."),
    ("1", "Ambiente (NIE023)", "Production environment.",
     "Also CUNE input [11]. A test document (2) can never be replayed into production."),
    ("102", "TipoXML (NIE202)", "NominaIndividual - the payroll support document itself.",
     "103 would be an adjustment note. CUNE input [9]."),
    ("NE1042", "Numero (NIE012)", "Prefix NE + consecutive 1042.",
     "Composite: positions 1-2 = authorised prefix, remainder = consecutive. CUNE input [1]. Rule 90 "
     "permits this number only once for this employee."),
    ("2026-04-05", "FechaGen (NIE026)", "Document generated on 5 April 2026.",
     "Within the first ten days of the month following the 31 March payment, so the art. 8 deadline "
     "is met. CUNE input [2]."),
    ("10:53:10-05:00", "HoraGen (NIE027)", "Generated at 10:53:10 Colombian time.",
     "The -05:00 offset is part of the string and part of CUNE input [3]. Colombia has no daylight "
     "saving, so the offset never varies."),
    ("5", "PeriodoNomina (NIE029)", "Monthly pay cycle.",
     "Had the employee been paid quincenal this would read 4 - and there would still be exactly ONE "
     "document, with two FechaPago occurrences."),
    ("COP", "TipoMoneda (NIE030)", "Colombian peso.",
     "Mandatory under art. 26. TRM (NIE200) stays absent."),

    "EMPLOYER AND EMPLOYEE",
    ("900123456", "Empleador/@NIT (NIE033)", "Employer tax number without the verification digit.",
     "CUNE input [7] uses the NIT ALONE. Including the DV here is a classic hash failure."),
    ("7", "Empleador/@DV (NIE034)", "Verification digit of the employer NIT.",
     "Carried separately; deliberately excluded from the CUNE."),
    ("11 / 11001", "Empleador department / municipality (NIE036 / NIE037)", "Bogota D.C.",
     "The five-digit municipality begins with the two-digit department. Art. 5 item 11."),
    ("01", "TipoTrabajador (NIE041)", "Dependiente - standard employee.",
     "One of only sixteen values in annex table 5.5.3. The PILA equivalent for this employee is "
     "tipo cotizante 1 - the codes are similar but the lists are not the same."),
    ("00", "SubTipoTrabajador (NIE042)", "No aplica.",
     "Only 00 and 01 exist in table 5.5.4. Had this been an employed old-age pensioner (01), the "
     "pension rate NIE164 would have to be 0.00."),
    ("false", "AltoRiesgoPension (NIE043)", "Not a Decreto Ley 2090 de 2003 high-risk activity.",
     "Always emitted, as the literal true or false. See CO-GAP-02 before setting true."),
    ("13 / 1020304050", "TipoDocumento / NumeroDocumento (NIE044 / NIE045)",
     "Cedula de ciudadania number 1020304050.",
     "CUNE input [8]. Had this been a passport (41), CO-GAP-07 would bite: the XSD types the number "
     "as xsd:integer, so an alphanumeric passport number cannot be schema-valid."),
    ("2 / 12000000.00", "TipoContrato / Sueldo (NIE061 / NIE062)",
     "Indefinite-term contract, contractual salary COP 12,000,000.",
     "Sueldo is the CONTRACTUAL figure and does not move with days worked; SueldoTrabajado (NIE070) "
     "does."),

    "PERIOD",
    ("2021-01-11", "FechaIngreso (NIE002)", "Hired 11 January 2021.",
     "Drives TiempoLaborado and the cesantias accrual."),
    ("2026-03-01 / 2026-03-31", "FechaLiquidacionInicio / Fin (NIE004 / NIE005)",
     "The document settles the whole of March 2026.",
     "One document per employee per month, whatever the pay cycle (art. 3)."),
    ("1850.00", "TiempoLaborado (NIE006)",
     "Cumulative service on the 360/30 convention: 5 years + 1 month + 20 days from 11 January 2021 "
     "to 31 March 2026 = (5 x 360) + (1 x 30) + 20 = 1850.00.",
     "A calendar day-count would give 1905 and be wrong. The annex's own example is "
     "5y 3m 18d = 1908.00."),
    ("30", "DiasTrabajados (NIE069)", "A full commercial month.",
     "February would also be 30, and so would a 31-day month. Reduced only by unpaid leave, "
     "suspension or strike."),
    ("2026-03-31", "FechaPago (NIE203)", "Single payment on 31 March 2026.",
     "Cardinality 1-N. A quincenal payroll would carry two occurrences here."),

    "ACCRUED - DEVENGADOS",
    ("12000000.00", "SueldoTrabajado (NIE070)", "Full month's basic salary.",
     "The only devengado in this simple month. It is the entire ET art. 388 gross and the entire "
     "PILA contribution base."),
    ("(absent)", "AuxilioTransporte (NIE071)",
     "Not payable: COP 12,000,000 exceeds 2 SMMLV (COP 3,501,810).",
     "OMITTED, not zero-filled. Had it been payable it would be COP 249,095 - not salary for "
     "contributions, but in the base of cesantias, prima and the severance indemnity."),
    ("12000000.00", "DevengadosTotal (NIE187)", "Sum of the Devengados block.",
     "Art. 5 item 6. CUNE input [4], truncated to two decimals."),

    "DEDUCTED - DEDUCCIONES",
    ("4.00 / 480000.00", "Salud @Porcentaje / @Deduccion (NIE161 / NIE163)",
     "Employee health at 4% of COP 12,000,000.",
     "The employer's 8.5% does NOT appear here - and in this case is nil anyway, because the "
     "employee earns under 10 SMMLV and the employer is exonerated under ET art. 114-1. The PILA "
     "figure for the same contribution is COP 480,000 rounded UP to the next 100, which happens to "
     "coincide here."),
    ("4.00 / 480000.00", "FondoPension @Porcentaje / @Deduccion (NIE164 / NIE166)",
     "Employee pension at 4% of COP 12,000,000.",
     "The employer's 12% is a PILA cost, not a deduction. Total pension into the system is 16% = "
     "COP 1,920,000."),
    ("1.00 / 120000.00", "FondoSP @Porcentaje / @DeduccionSP (NIE167 / NIE168)",
     "Solidarity sub-account surcharge at 1% of COP 12,000,000, because the base is at or above "
     "4 SMMLV (COP 7,003,620).",
     "SEPARATE from pension. Merging this into FondoPension to show a 5% pension line is the single "
     "most common Colombian mapping error."),
    ("(absent)", "FondoSP @PorcentajeSub / @DeduccionSub (NIE169 / NIE170)",
     "Subsistence surcharge not payable: the base is below 16 SMMLV (COP 28,014,480).",
     "The two sub-accounts have DIFFERENT triggers - 4 SMMLV and 16 SMMLV."),
    ("617000.00", "RetencionFuente (NIE177)",
     "Withholding computed under Procedure 1: gross 12,000,000 less non-constitutive contributions "
     "1,080,000 = 10,920,000; less 25% exempt income 2,730,000 (within both the 40% and the "
     "apportioned 1,340-UVT caps) = base 8,190,000; = 156.375 UVT; band 150-360 UVT at 28%: "
     "(156.375 - 150) x 0.28 + 10 = 11.785 UVT; x 52,374 = COP 617,232, approximated to the nearest "
     "1,000 under ET art. 868 = COP 617,000.",
     "NON-RESIDENT CONTRAST: the same employee, before acquiring residence, would be withheld at the "
     "flat 20% of ET art. 408 on the GROSS - 20% x 12,000,000 = COP 2,400,000, with no depuration "
     "and no exempt income. Nearly four times the resident figure."),
    ("1697000.00", "DeduccionesTotal (NIE188)",
     "480,000 + 480,000 + 120,000 + 617,000.",
     "Art. 5 item 7. CUNE input [5]."),

    "TOTALS AND CONTROL",
    ("(absent)", "Redondeo (NIE186)",
     "No residual: every concept is a whole peso, so the round-half-to-even sums tie exactly.",
     "Where a residual arises it must be disclosed here, within the +/- 2.00 tolerance, not absorbed "
     "into a concept."),
    ("10303000.00", "ComprobanteTotal (NIE189)", "12,000,000 - 1,697,000.",
     "Art. 5 item 8. CUNE input [6]. This is the amount that must match the bank payment file."),
    ("16560dc8...f3bac2", "CUNE (NIE024)",
     "SHA-384 over NE1042 + 2026-04-05 + 10:53:10-05:00 + 12000000.00 + 1697000.00 + 10303000.00 + "
     "900123456 + 1020304050 + 102 + <PIN> + 1.",
     "96 hexadecimal characters. The PIN never appears in the XML. Any change to any of the eleven "
     "inputs yields a different document."),

    "CROSS-REPORT RECONCILIATION FROM THIS RECORD",
    ("617000", "-> Formulario 350 casilla 93", "Retenciones - rentas de trabajo, personas naturales.",
     "The March total across all employees, rounded to the nearest 1,000."),
    ("8190000", "-> Formulario 350 casilla 77", "Base sujeta a retencion - rentas de trabajo.",
     "The depurated base, not the gross."),
    ("12000000", "-> PILA Registro Tipo 2 fields 42, 43, 44, 45", "IBC for pension, health, "
     "occupational risk and the family compensation fund.",
     "All four bases coincide here; they diverge as soon as a non-salary payment or the 40% clamp "
     "enters."),
    ("144000000", "-> Formulario 220 casilla 36 and Formato 2276 numeral 5",
     "Twelve months of salary at COP 12,000,000.",
     "Annual accumulation. The certificate is issued to the employee by the last business day of "
     "March 2027 for the 2026 tax year."),
]

# ===========================================================================
#  SHEET 9 - SAMPLE FILE
# ===========================================================================
CFG["sample_title"] = ("XML AND SOAP ENVELOPE - CONSTRUCTED FROM THE OFFICIAL ANEXO TECNICO XPATH "
                       "INVENTORY")
CFG["sample"] = r"""
PROVENANCE NOTE - READ FIRST
============================
The SOAP envelopes below are QUOTED VERBATIM from the official Anexo Tecnico
version 1.0, sections 9.5 and 9.7.2.

The XML instance below is CONSTRUCTED from the annex's own XPath inventory
(sections 3 and 4, 195 NIE codes) and populated with the worked example on the
Example Analysis sheet. DIAN publishes no sample instance in the annex and none
was supplied in 00-official-sources/sample-files/, so this is a faithful
reconstruction of the documented structure - NOT an official DIAN sample.
Validate it against XSD v1.0.6 in the DIAN habilitacion environment before use.
The ds:Signature block is shown as a placeholder; it is produced by the signing
component, not by payroll.

-------------------------------------------------------------------------------
1. TRANSMISSION - SOAP 1.2 request (Anexo Tecnico s.9.5 / s.9.7.2, verbatim)
-------------------------------------------------------------------------------
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
               xmlns:wcf="http://wcf.dian.colombia">
   <soap:Header/>
   <soap:Body>
      <wcf:SendNominaSync>
         <!--Optional:-->
         <wcf:contentFile>cid:1057568194758</wcf:contentFile>
      </wcf:SendNominaSync>
   </soap:Body>
</soap:Envelope>

   wcf:contentFile carries the base64 encoding of a ZIP containing the XML below.
   Maximum 500 KB. UTF-8 only. TLS 1.2 with mutual certificate authentication.

-------------------------------------------------------------------------------
2. RESPONSE - SOAP 1.2 response header (Anexo Tecnico s.9.7.2, verbatim)
-------------------------------------------------------------------------------
<s:Envelope xmlns:s="http://www.w3.org/2003/05/soap-envelope"
            xmlns:a="http://www.w3.org/2005/08/addressing"
            xmlns:u="http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd">
   <s:Header>
      <a:Action s:mustUnderstand="1">
         http://wcf.dian.colombia/IWcfDianCustomerServices/SendNominaSyncResponse
      </a:Action>
   </s:Header>
   ...
   <!-- the body carries an ApplicationResponse encoded in Base64 with DIAN's
        validation verdict. THIS MUST BE PARSED AND PERSISTED - a payroll cost
        is deductible only where the document has been validated. -->
</s:Envelope>

-------------------------------------------------------------------------------
3. PAYLOAD - NominaIndividual (constructed from the annex XPath inventory)
-------------------------------------------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<NominaIndividual>

  <UBLExtensions>
    <UBLExtension>
      <ExtensionContent>
        <!-- XAdES-EPES enveloped signature, X.509 from an ONAC-accredited CA,
             ClaimedRole = thirdparty | supplier (Anexo s.7) -->
        <ds:Signature xmlns:ds="http://www.w3.org/2000/09/xmldsig#">...</ds:Signature>
      </ExtensionContent>
    </UBLExtension>
  </UBLExtensions>

  <Periodo FechaIngreso="2021-01-11"
           FechaLiquidacionInicio="2026-03-01"
           FechaLiquidacionFin="2026-03-31"
           TiempoLaborado="1850.00"
           FechaGen="2026-04-05"/>

  <NumeroSecuenciaXML CodigoTrabajador="EMP-00417"
                      Prefijo="NE"
                      Consecutivo="1042"
                      Numero="NE1042"/>

  <LugarGeneracionXML Pais="CO"
                      DepartamentoEstado="11"
                      MunicipioCiudad="11001"
                      Idioma="es"/>

  <ProveedorXML RazonSocial="MERCANS COLOMBIA S.A.S."
                NIT="901234567"
                DV="3"
                SoftwareID="56f2ae23-4a7c-4e51-9b7d-1f2c3d4e5f60"
                SoftwareSC="9b1c2d3e4f5061728394a5b6c7d8e9f0a1b2c3d4e5f6071829
                            3a4b5c6d7e8f9001122334455667788990aabbccddeeff"/>

  <CodigoQR>https://catalogo-vpfe.dian.gov.co/document/searchqr?documentkey=16560dc8...f3bac2</CodigoQR>

  <InformacionGeneral Version="V1.0: Documento Soporte de Pago de Nomina Electronica"
                      Ambiente="1"
                      TipoXML="102"
                      CUNE="16560dc8956122e84ffb743c817fe7d494e058a44d9ca3fa4c234c268b4f766003253fbee7ea4af9682dd57210f3bac2"
                      EncripCUNE="CUNE-SHA384"
                      FechaGen="2026-04-05"
                      HoraGen="10:53:10-05:00"
                      PeriodoNomina="5"
                      TipoMoneda="COP"/>

  <Notas>Nomina correspondiente al mes de marzo de 2026</Notas>

  <Empleador RazonSocial="MERCANS COLOMBIA S.A.S."
             NIT="900123456"
             DV="7"
             Pais="CO"
             DepartamentoEstado="11"
             MunicipioCiudad="11001"
             Direccion="CALLE 100 No 7-33 PISO 12"/>

  <Trabajador TipoTrabajador="01"
              SubTipoTrabajador="00"
              AltoRiesgoPension="false"
              TipoDocumento="13"
              NumeroDocumento="1020304050"
              PrimerApellido="PEREZ"
              SegundoApellido="GOMEZ"
              PrimerNombre="JUAN"
              OtrosNombres="CARLOS"
              LugarTrabajoPais="CO"
              LugarTrabajoDepartamentoEstado="11"
              LugarTrabajoMunicipioCiudad="11001"
              LugarTrabajoDireccion="CALLE 100 No 7-33 PISO 12"
              SalarioIntegral="false"
              TipoContrato="2"
              Sueldo="12000000.00"
              CodigoTrabajador="EMP-00417"/>

  <Pago Forma="1"
        Metodo="42"
        Banco="BANCOLOMBIA"
        TipoCuenta="AHORROS"
        NumeroCuenta="12345678901"/>

  <FechasPagos>
    <FechaPago>2026-03-31</FechaPago>
  </FechasPagos>

  <Devengados>
    <Basico DiasTrabajados="30" SueldoTrabajado="12000000.00"/>
    <!-- AuxilioTransporte OMITTED: salary exceeds 2 SMMLV (COP 3,501,810).
         Omitted, never zero-filled. -->
    <!-- No overtime, vacation, prima, cesantias, incapacity or leave in this month. -->
  </Devengados>

  <Deducciones>
    <Salud Porcentaje="4.00" Deduccion="480000.00"/>
    <FondoPension Porcentaje="4.00" Deduccion="480000.00"/>
    <FondoSP Porcentaje="1.00" DeduccionSP="120000.00"/>
    <!-- PorcentajeSub / DeduccionSub OMITTED: base is below 16 SMMLV
         (COP 28,014,480). The two sub-accounts have different triggers. -->
    <RetencionFuente>617000.00</RetencionFuente>
  </Deducciones>

  <DevengadosTotal>12000000.00</DevengadosTotal>
  <DeduccionesTotal>1697000.00</DeduccionesTotal>
  <ComprobanteTotal>10303000.00</ComprobanteTotal>

</NominaIndividual>

-------------------------------------------------------------------------------
4. NON-RESIDENT VARIANT (v2.8 control B1)
-------------------------------------------------------------------------------
The same document for a NON-RESIDENT employee differs in exactly one element -
there is no residence attribute in the schema:

  <Deducciones>
    <Salud Porcentaje="4.00" Deduccion="480000.00"/>
    <FondoPension Porcentaje="4.00" Deduccion="480000.00"/>
    <FondoSP Porcentaje="1.00" DeduccionSP="120000.00"/>
    <RetencionFuente>2400000.00</RetencionFuente>   <!-- ET art. 408: 20% x GROSS -->
  </Deducciones>

  <DevengadosTotal>12000000.00</DevengadosTotal>
  <DeduccionesTotal>3480000.00</DeduccionesTotal>
  <ComprobanteTotal>8520000.00</ComprobanteTotal>

Flat 20% of ET art. 408 applied to the GROSS COP 12,000,000, with no art. 388
depuration, no 25% exempt income, no art. 387 deductions and no tax-free band
(DIAN Concepto 011108 of 29 June 2026). Where the work were performed ENTIRELY
outside Colombia, LugarTrabajoPais would not be CO and there would be NO
withholding at all (DIAN Oficio 28380 of 2019).

-------------------------------------------------------------------------------
5. ADJUSTMENT NOTE SKELETON (NominaIndividualDeAjuste, TipoXML 103)
-------------------------------------------------------------------------------
<?xml version="1.0" encoding="UTF-8"?>
<NominaIndividualDeAjuste>
  <TipoNota>1</TipoNota>                    <!-- 1 Reemplazar | 2 Eliminar -->
  <Reemplazar>
    <!-- the ENTIRE NominaIndividual structure repeated with corrected values,
         under NIAE-prefixed codes, carrying its OWN CUNE computed on the same
         eleven inputs taken from this Reemplazar block -->
  </Reemplazar>
</NominaIndividualDeAjuste>

For TipoNota = 2 the Eliminar block is used instead, and its CUNE is computed
with ValDev = ValDed = ValTol = 0.00 and DocEmp = 0 (Anexo s.8.1.1.4). A shared
CUNE routine that reads the real totals will produce a wrong hash for a
cancellation - this is a deliberate divergence in the specification, not an
error in it.
"""

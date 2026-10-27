# -*- coding: utf-8 -*-
"""CO-DIAN-005 - Sheets 5 to 9 for Formato 2276 version 4."""

from co_r5_formato2276 import CFG

# ===========================================================================
#  SHEET 5 - FILE STRUCTURE (neutral field model - layout not published locally)
# ===========================================================================
CFG["filestruct"] = [
    ("##", "SUBMISSION FORMAT - VERIFIED CHANNEL, UNVERIFIED SCHEMA (v2.7 STEP 3.5)"),
    ("Channel", "file_upload into the DIAN informacion exogena service at www.dian.gov.co, in an "
                "authenticated portal session signed with the Instrumento de Firma Electronica "
                "(IFE). CONFIRMED."),
    ("File format", "XML prepared to the DIAN especificaciones tecnicas for Formato 2276 version 4. "
                    "Res. DIAN 000227 de 2025 art. 1.3.10.1 lists the format in its "
                    "formatos-y-especificaciones-tecnicas table as entry T3.45, version 4."),
    ("FORMAT TO CONFIRM", "The especificaciones tecnicas annex that fixes the XML ELEMENT NAMES, "
                          "the field ordering and the column lengths is a SEPARATE document and is "
                          "NOT in the local source registry. Res. 227 prescribes WHAT to report, "
                          "not how the file is shaped. Every element path in this Spec is therefore "
                          "marked DERIVED in column T. Obtain the published especificaciones "
                          "tecnicas before configuring a productive layout."),
    ("Why this is NOT machine-to-machine", "There is no SOAP service, no XAdES document signature "
                                           "and no synchronous ApplicationResponse. Contrast the "
                                           "nomina electronica (CO-DIAN-001), which has all three. "
                                           "Here the employer uploads through an authenticated "
                                           "portal session and reads the outcome on screen."),
    ("What the model below is", "A NEUTRAL FIELD MODEL - the resolution's own thirty-six numerals "
                                "in their published order, plus the envelope attributes the "
                                "deadline depends on. It is a LOGICAL MODEL, not the wire format."),

    ("##", "LOGICAL MODEL - ONE RECORD PER BENEFICIARY"),
    ("Envelope", "Informant NIT | Taxpayer category (Gran Contribuyente / persona juridica / "
                 "persona natural) | Tax year | Format 2276 version 4"),
    ("Block 1 - Entidad informante", "N01 Entidad informante (code 1 to 8) | N35 Identificacion del "
                                     "fideicomiso (only where N01 = 2) | N36 Tipo documento e "
                                     "identificacion del participante en contrato (only where N01 "
                                     "is 3 to 8)"),
    ("Block 2 - Beneficiario", "N02 Tipo de documento y numero de identificacion | N03 Apellidos y "
                               "nombres | N04 Ubicacion (departamento y municipio)"),
    ("Block 3 - Ingresos", "N05 Salarios | N06 Emolumentos eclesiasticos | N07 Bonos, cheques, "
                           "tarjetas, vales | N08 Exceso alimentacion > 41 UVT | N09 Honorarios | "
                           "N10 Servicios | N11 Comisiones | N12 Prestaciones sociales | "
                           "N13 Viaticos | N14 Gastos de representacion | N15 Compensaciones "
                           "trabajo asociado cooperativo | N16 Apoyos economicos educativos | "
                           "N17 Otros pagos"),
    ("Block 4 - Cesantias", "N18 Pagadas al empleado | N19 Consignadas al fondo | N20 Regimen "
                            "tradicional del CST"),
    ("Block 5 - Pensiones y total", "N21 Pensiones de jubilacion, vejez o invalidez | N22 TOTAL "
                                    "INGRESOS BRUTOS"),
    ("Block 6 - Aportes", "N23 Aportes obligatorios salud | N24 Aportes obligatorios pensiones y "
                          "solidaridad | N25 Aportes voluntarios RAIS | N26 Aportes voluntarios "
                          "fondos de pensiones | N27 Aportes AFC | N28 Aportes AVC"),
    ("Block 7 - Retenciones e IVA", "N29 Retenciones practicadas | N30 IVA mayor valor del costo o "
                                    "gasto | N31 Retencion de IVA"),
    ("Block 8 - Informativos y especiales", "N32 Alimentacion hasta 41 UVT (INFORMATIVE, outside "
                                            "N22) | N33 Ingreso laboral promedio ultimos 6 meses | "
                                            "N34 Dependiente economico"),

    ("##", "INTERPRETIVE RULES PRINTED IN RES. 227 ART. 1.3.7.1.1"),
    ("Paragrafo 1", "Numeral 32 (meal payments up to 41 UVT) 'se considera de caracter informativo'. "
                    "It therefore does NOT enter the gross total in numeral 22."),
    ("Paragrafo 2", "'Las casillas de valores son de obligatorio diligenciamiento. En caso de no "
                    "tener ningun valor, se deben diligenciar con cero (0).' Every value field is "
                    "populated; write ZERO, never blank."),
    ("Paragrafo 3", "The eight-value Entidad Informante code table - reproduced on Sheet 6."),
    ("Paragrafo 4", "For an ordinary employer the Entidad Informante is concepto 1 (Informante "
                    "general), and numerals 35 and 36 are NOT filled. Where the income is paid out "
                    "of trust assets, concepto 2 plus numeral 35 and no numeral 36. Where it is "
                    "paid under a collaboration contract, the contract concepto plus numeral 36 and "
                    "no numeral 35."),
    ("Paragrafo 5", "Payments to natural persons receiving work income NOT from an employment, "
                    "legal or statutory relationship, but withheld under ET art. 383, ARE reported "
                    "in Formato 2276. Where art. 383 withholding did NOT apply, they are reported "
                    "in the ordinary payments-and-withholdings formats instead."),
    ("Paragrafo 6", "'El valor reportado en el numeral 7 no debe contener la informacion reportada "
                    "en los demas numerales del Formato 2276.' Numeral 7 is residual - it must not "
                    "double-report anything already in another numeral."),
    ("Paragrafo 7", "Educational support paid DIRECTLY by the employer goes to numeral 16; support "
                    "administered by a THIRD PARTY goes to Formato 5247 concepto 5102. Added by "
                    "Res. 188 de 2024 art. 8; first applies to tax year 2025, filed in calendar "
                    "2026 (art. 1.3.9.1.3 par. 5)."),

    ("##", "AMOUNT AND ROUNDING CONVENTION"),
    ("Rounding", "Whole pesos, no decimals, no thousand separators, zero-filled where nil. This is "
                 "the fourth Colombian convention encountered across the six filings, alongside the "
                 "nomina electronica (2 decimals round-half-to-even), PILA (round UP to the next "
                 "100) and Formulario 350 and 220 (nearest 1,000). Store the unrounded value once "
                 "and apply each convention at output."),
    ("Nil values", "Write ZERO. Res. 227 par. 2 is explicit. This matches Formulario 220 and "
                   "INVERTS the nomina electronica, where an inapplicable element is omitted."),

    ("##", "FILING CALENDAR - RES. 227 ART. 1.3.9.1.3"),
    ("Grandes Contribuyentes", "By the LAST digit of the NIT: 1 = 17th business day of April; "
                               "2 = 18th business day of April; 3 = 1st business day of May; "
                               "4 = 2nd; 5 = 3rd; 6 = 4th; 7 = 5th; 8 = 6th; 9 = 7th; 0 = 8th "
                               "business day of May."),
    ("Personas juridicas y naturales", "By the LAST TWO digits of the NIT, in five-number bands: "
                                       "01-05 = 9th business day of May, rising one business day "
                                       "per band through 51-55 = 19th business day of May, then "
                                       "56-60 = 1st business day of June, through 96-00 = 9th "
                                       "business day of June."),
    ("Category tested at filing", "Art. 1.3.9.1.3 par. 1: the Gran Contribuyente, legal-person or "
                                  "natural-person status is the one held AT THE MOMENT OF FILING, "
                                  "not at the year end being reported."),
    ("Three different deadline rules", "Formulario 350 uses the LAST digit and the 7th-16th business "
                                       "day of the following MONTH. PILA uses the LAST TWO digits "
                                       "and the 2nd-16th business day of the following MONTH. This "
                                       "return uses the LAST digit for Grandes Contribuyentes and "
                                       "the LAST TWO for everyone else, in MAY or JUNE of the "
                                       "following YEAR. Do not generalise one rule to another "
                                       "filing."),
]

# ===========================================================================
#  SHEET 6 - FIELD OPTIONS
# ===========================================================================
CFG["options"] = [
    "ENTIDAD INFORMANTE (numeral 1) - Res. 227 art. 1.3.7.1.1 par. 3, verbatim",
    ("1", "GEN", "Informante general",
     "THE VALUE FOR AN ORDINARY EMPLOYER. Par. 4: 'cuando el empleador reporte pagos o abonos en "
     "cuenta por concepto de rentas de trabajo y de pensiones, la casilla Entidad Informante se "
     "debe diligenciar con el concepto 1 - Informante general', and numerals 35 and 36 are left "
     "blank."),
    ("2", "FID", "Fiduciarias",
     "Where the work income is paid out of trust assets. Requires numeral 35 (identificacion del "
     "fideicomiso); numeral 36 stays blank."),
    ("3", "MAND", "Mandatario y/o Administrador delegado",
     "Requires numeral 36 (contract participants); numeral 35 stays blank."),
    ("4", "CONS", "Consorcio y/o Union Temporal", "Requires numeral 36."),
    ("5", "HIDRO", "Exploracion y Explotacion de hidrocarburos, gases y minerales",
     "Requires numeral 36."),
    ("6", "JV", "Joint Venture", "Requires numeral 36."),
    ("7", "CP", "Gestor en Cuentas en Participacion", "Requires numeral 36."),
    ("8", "COOP-PUB", "Convenios de cooperacion con entidades publicas", "Requires numeral 36."),

    "LAS TRES LINEAS DE CESANTIAS (numerals 18, 19, 20) - ORDER DIFFERS FROM FORM 220",
    ("N18", "PAGADA", "Cesantias e intereses efectivamente pagadas al empleado",
     "Amounts ACTUALLY PAID to the employee. Formulario 220 casilla 47. Same position in both."),
    ("N19", "FONDO", "Cesantias consignadas al fondo de cesantias",
     "Deposited to the fund by 14 February under Ley 50 de 1990 art. 99. FORMULARIO 220 CASILLA "
     "49 - NOT 48."),
    ("N20", "TRADICIONAL", "Auxilio de cesantias del regimen tradicional del CST",
     "Pre-1991 retroactive regime. FORMULARIO 220 CASILLA 48 - NOT 49."),
    ("(mapping warning)", "-", "-", "THE SECOND AND THIRD LINES ARE TRANSPOSED between the two "
     "artefacts. A positional mapping - 47 to 18, 48 to 19, 49 to 20 - swaps the fund deposit and "
     "the traditional-regime amount. Map by MEANING."),

    "UMBRALES UVT 2026 (UVT = COP 52,374, Res. DIAN 000238 de 15 dic 2025)",
    ("41 UVT", "2,147,334", "Tope mensual de alimentacion, art. 387-1",
     "Meal payments to a third party up to this monthly amount are NOT income of the employee. They "
     "go to numeral 32 as INFORMATIVE and stay outside the gross total in numeral 22. The excess "
     "goes to numeral 8 as taxable income."),
    ("310 UVT", "16,235,940", "Salario mensual maximo para el beneficio de alimentacion",
     "Where the employee's monthly salary EXCEEDS this, the art. 387-1 exclusion does not apply at "
     "all: the whole meal payment falls to numeral 7 and BOTH numeral 8 and numeral 32 stay nil."),
    ("350 UVT", "18,330,900", "Ingreso laboral promedio para la exencion de cesantias, art. 206 "
     "num. 4", "Severance and interest are exempt in full where the six-month average in numeral 33 "
     "does not exceed this; tapered above."),
    ("1,000 UVT", "52,374,000", "Tope mensual exento de pensiones, art. 206 num. 5",
     "Employer-paid pension income is taxable only above this monthly amount. Numeral 21."),
    ("32 UVT", "1,675,968", "Tope mensual de la deduccion por dependientes, art. 387 par. 2",
     "The dependants deduction is 10% of gross employment income capped at this monthly amount. The "
     "dependant is identified in numeral 34."),

    "TIPO DE DOCUMENTO (numerals 2 and 34) - the DIAN NUMERIC catalogue (Anexo Tecnico de la "
    "nomina electronica, table 5.2.1). Res. 227 does not print the list; the especificaciones "
    "tecnicas of the exogena reuse the DIAN catalogue, so the codes below are DERIVED from "
    "table 5.2.1 and are the SAME table the Data Dictionary mapper 'Employee Document Type' "
    "holds. CONFIRM against the especificaciones tecnicas of formato 2276 version 4 before "
    "configuring",
    ("11", "RC", "Registro civil", "Civil birth registration. Realistic only at numeral 34 "
     "(economic dependant), never at numeral 2."),
    ("12", "TI", "Tarjeta de identidad", "Identity card for a person aged 7 to 17."),
    ("13", "CC", "Cedula de ciudadania", "National identity card. The great majority of "
     "beneficiaries and dependants."),
    ("21", "TE", "Tarjeta de extranjeria", "Foreigner's identity card."),
    ("22", "CE", "Cedula de extranjeria", "Foreign resident's identity card."),
    ("31", "NIT", "NIT", "Tax identification number, where the beneficiary is an entity."),
    ("41", "PA", "Pasaporte", "Passport."),
    ("42", "DIE", "Documento de identificacion extranjero", "Foreign identity document."),
    ("47", "PEP", "PEP - Permiso Especial de Permanencia", "Special residence permit. "
     "CO-GAP-06: there is still no code for the PPT."),
    ("50", "NIT-EXT", "NIT de otro pais", "Foreign tax identification number."),
    ("91", "NUIP", "NUIP", "Unique personal identification number; employee only."),
    ("(mapping warning)", "-", "-", "THREE artefacts, THREE catalogues. Formulario 220 prints "
     "a SIX-value list (12, 13, 21, 22, 31, 41) and PILA uses two-letter codes (CC, CE, TI, "
     "PA, CD, SC, RC, PE). Map by MEANING through the Data Dictionary master value; never "
     "copy a code between channels."),

    "DIVIPOLA (DANE) - numeral 4",
    ("11 / 001", "BOG", "Bogota D.C. - departamento y municipio",
     "The beneficiary's location. NOT the same question as the nomina electronica place of work "
     "(NIE051 / NIE052) or the Formulario 220 place where the withholding was practised (casillas "
     "34 / 35) - three artefacts, three different geographic questions about the same person."),

    "CALENDARIO DE LA EXOGENA - Res. 227 art. 1.3.9.1.3",
    ("GC last digit 1", "-", "Decimo septimo dia habil del mes de abril", "Grandes Contribuyentes."),
    ("GC last digit 2", "-", "Decimo octavo dia habil del mes de abril", "Grandes Contribuyentes."),
    ("GC last digits 3-0", "-", "Primer a octavo dia habil del mes de mayo",
     "Grandes Contribuyentes: 3 = 1st business day of May, then one business day per digit through "
     "0 = 8th business day of May."),
    ("PJ/PN 01-05", "-", "Noveno dia habil del mes de mayo",
     "Personas juridicas y naturales, by the LAST TWO digits of the NIT."),
    ("PJ/PN 06-55", "-", "Decimo a decimo noveno dia habil del mes de mayo",
     "One business day per five-number band."),
    ("PJ/PN 56-00", "-", "Primer a noveno dia habil del mes de junio",
     "The bands continue into June: 56-60 = 1st business day of June through 96-00 = 9th business "
     "day of June."),
    ("(par. 1)", "-", "Calidad al momento de informar",
     "The Gran Contribuyente, legal-person or natural-person status used is the one held AT THE "
     "MOMENT OF FILING, not at the reported year end."),

    "FORMATO Y VERSION",
    ("2276 / 4", "T3.45", "Informacion de rentas de trabajo y pensiones, version 4",
     "Listed in the formatos-y-especificaciones-tecnicas table at Res. 227 art. 1.3.10.1 as entry "
     "T3.45. A version mismatch is rejected at upload."),
    ("5247 / -", "-", "Formato para apoyos economicos administrados por terceros",
     "NOT a payroll filing. Educational support ADMINISTERED BY A THIRD PARTY is reported there "
     "under concepto 5102 instead of at numeral 16 here (Res. 227 par. 7)."),

    "NUMERALS THAT ARE NOT PAYROLL FIELDS",
    ("N30 / N31", "-", "IVA mayor valor del costo o gasto / Retencion de IVA",
     "Colombian employment income carries no VAT. Relevant only where the beneficiary is a "
     "VAT-responsible contractor paid under the ET art. 383 table. Owned by the client's tax "
     "function."),
    ("N35 / N36", "-", "Fideicomiso / participante en contrato",
     "Res. 227 par. 4: for an ordinary employer reporting under concepto 1 they 'no se deben "
     "diligenciar'. Mutually exclusive with each other."),
]

# ===========================================================================
#  SHEET 7 - POPULATION RULES
# ===========================================================================
CFG["population"] = [
    "MANDATORY FIELD RULES",
    ("Numeral 1 - Entidad informante", "Configuration",
     "For an ordinary employer reporting employment and pension income, set the code to 1 - "
     "Informante general - and leave numerals 35 and 36 BLANK. Res. 227 par. 4 states this in "
     "terms. Depart from concepto 1 only where the income was genuinely paid out of trust assets "
     "(concepto 2, plus numeral 35) or under a collaboration contract (conceptos 3 to 8, plus "
     "numeral 36).",
     "The three cases are mutually exclusive and each drives a different pair of numerals. Getting "
     "the concepto wrong changes which identifier fields DIAN expects and produces a validation "
     "failure rather than a silent misstatement."),
    ("Numerals 5 to 21 - the income concepts", "Payroll engine",
     "Accumulate each concept separately for the whole tax year on the PAYMENT date. Then apply the "
     "two exclusion rules the resolution imposes: par. 6 forbids numeral 7 from repeating anything "
     "reported in another numeral, and par. 7 sends third-party-administered educational support to "
     "Formato 5247 rather than to numeral 16.",
     "Note two concepts that Formulario 220 does NOT separate: numeral 6 (ecclesiastical "
     "emoluments), which Form 220 folds into casilla 39, and numeral 32 (meal payments up to 41 "
     "UVT), for which Form 220 has no casilla at all."),
    ("Numeral 22 - Total ingresos brutos", "Engine (computed)",
     "Sum numerals 5 to 21. DO NOT include numeral 32: par. 1 makes it informative, because meal "
     "payments below the threshold are income of the food supplier and not of the employee. Assert "
     "that numeral 22 equals Formulario 220 casilla 52 for the same employee and year.",
     "Including numeral 32 in the total overstates the employee's gross income and breaks the "
     "reconciliation to Formulario 220 - and it is an easy mistake because every other value "
     "numeral does enter the total."),
    ("Numeral 33 - Ingreso laboral promedio", "Payroll engine",
     "Populate ONLY for employees to whom ET art. 206 num. 4 applies - that is, where severance or "
     "its interest was paid or deposited in the year, so that numerals 18, 19 or 20 are non-zero. "
     "The resolution says 'UNICAMENTE'. Maintain the rolling six-month average year-round; on a "
     "termination use the last six months OF EMPLOYMENT.",
     "The average cannot be reconstructed from annual totals at year end. Populating it for every "
     "employee regardless is also wrong: the resolution restricts it, and an unnecessary value "
     "invites an enquiry."),
    ("Numeral 34 - Dependiente economico", "Employee master data",
     "Populate the document type and number of each dependant claimed under ET art. 387 par. 2 "
     "during the year. Keep it byte-identical to Formulario 220 casillas 79 and 80.",
     "THIS IS THE FIELD DIAN USES TO CROSS-CHECK a dependant claimed by more than one taxpayer - "
     "typically both parents claiming the same child. A divergence between this return and the "
     "certificate the employee holds produces an enquiry to the employee, not to the employer."),

    "CRITICAL VALIDATION RULES",
    ("Write zero, never blank", "Engine (formatting)",
     "Res. 227 par. 2: 'Las casillas de valores son de obligatorio diligenciamiento. En caso de no "
     "tener ningun valor, se deben diligenciar con cero (0).' Every value numeral is populated.",
     "Matches Formulario 220 and INVERTS the nomina electronica, where an inapplicable element is "
     "omitted rather than zero-filled. Two DIAN artefacts, two opposite conventions."),
    ("Numeral 7 must not double-report", "Engine (validation)",
     "Par. 6 forbids numeral 7 from containing anything reported in another numeral. Before filing, "
     "assert that no amount is counted both in numeral 7 and in numerals 5, 8, 12, 17 or elsewhere.",
     "The risk is real because voucher and card payments can plausibly be classified as salary "
     "(numeral 5), as a meal benefit (numerals 8 or 32) or as other payments (numeral 17). Fix the "
     "classification on the wage type, once."),
    ("The meal-payment fork", "Payroll engine",
     "Apply the two ET art. 387-1 tests MONTHLY and in sequence. First: does the employee's monthly "
     "salary exceed 310 UVT (COP 16,235,940 in 2026)? If YES, the whole meal payment goes to "
     "numeral 7 and both numeral 8 and numeral 32 stay nil for that month. If NO, split the payment "
     "at 41 UVT (COP 2,147,334): the part up to the threshold goes to numeral 32 (informative), and "
     "the EXCESS goes to numeral 8 (taxable).",
     "Three possible destinations for one payment, decided monthly. An employee can fork one way in "
     "some months and the other way in others within the same annual record, so the accumulation "
     "must be per month and then summed - not decided once on the annual figures."),
    ("Numerals 35 and 36 are mutually exclusive", "Engine (validation)",
     "Numeral 35 is populated only where numeral 1 = 2; numeral 36 only where numeral 1 is 3 to 8; "
     "both blank where numeral 1 = 1. Never both.",
     "Res. 227 par. 4 spells out each of the three cases explicitly."),
    ("Numerals 19 and 20 are mutually exclusive per employee", "Engine (validation)",
     "An employee is in the Ley 50 de 1990 fund-deposit regime or in the pre-1991 traditional "
     "regime, not both. Assert that at most one of numerals 19 and 20 is non-zero for any "
     "beneficiary.",
     "The only exception is a formal regime election in the transition year - rare enough to "
     "warrant an explicit override rather than a silent allowance."),

    "AMOUNT FORMAT RULES",
    ("Whole pesos, no separators", "Engine (formatting)",
     "Amounts are whole Colombian pesos with no decimals and no thousand separators. Round once, at "
     "the annual accumulation, not per month.",
     "This is the fourth rounding convention across the six filings. Store the unrounded value once "
     "and apply each convention at output; never derive one artefact's figures from another's "
     "rounded output."),
    ("Numeral 24 combines two concepts", "Engine (accumulation)",
     "Numeral 24 carries mandatory PENSION contributions AND the solidarity-fund surcharge in one "
     "figure, exactly as Formulario 220 casilla 54 does. The nomina electronica reports three "
     "separate elements and PILA three separate campos.",
     "Sum them only at this point. Combining them earlier makes the monthly artefacts impossible to "
     "produce correctly."),
    ("Numerals 25 and 26 split one nomina electronica element", "Engine (accumulation)",
     "Numeral 25 is voluntary RAIS contributions under ET art. 55; numeral 26 is voluntary "
     "contributions to VOLUNTARY pension funds under ET art. 126-1. The nomina electronica has ONE "
     "element for both (PensionVoluntaria, NIE198).",
     "Carry the distinction on the wage type from configuration. It cannot be recovered from the "
     "XML at year end."),
    ("Numeral 28 has no nomina electronica element", "Engine (accumulation)",
     "AVC contributions to the Fondo Nacional del Ahorro have no dedicated nomina electronica "
     "element and fall to OtraDeduccion (NIE197). Tag the wage type so the amount can be recovered "
     "here and at Formulario 220 casilla 58.",
     "Without the tag the amount is indistinguishable from any other 'other deduction' in the "
     "annual accumulation."),

    "PAYROLL-SPECIFIC POPULATION RULES",
    ("Numeral 29 - RESIDENT", "Payroll engine (tax)",
     "Accumulate the withholding actually practised under the ET art. 383 progressive table, "
     "Procedure 1 or Procedure 2, on the art. 388 depurated base. Assert that it equals Formulario "
     "220 casilla 60 for the same employee and twelve months of nomina electronica NIE177.",
     "An employee whose depurated base fell in the 0% band all year still gets a record, with "
     "numeral 29 at zero and numerals 5 to 22 populated."),
    ("Numeral 29 - NON-RESIDENT", "Payroll engine (tax)",
     "Accumulate the flat 20% of ET art. 408 applied to the GROSS. Numerals 23 and 24 still report "
     "the contributions actually deducted, but they did NOT reduce the base - art. 408 admits no "
     "depuration. Numeral 33 is reported where severance was paid but has no effect, because the "
     "art. 206 num. 4 exemption belongs to the resident cedula-general regime.",
     "USEFUL INTERNAL CONTROL: for a pure non-resident record, numeral 29 should be almost exactly "
     "20% of numeral 22. A material divergence means either a residence change during the year or a "
     "misclassification. The format has no residence field, so this arithmetic is the only signal."),
    ("Mid-year residence change", "Payroll engine (tax)",
     "Produce ONE record. Numeral 29 sums the months withheld at 20% under art. 408 and the months "
     "withheld under the art. 383 table. The format has no field to disclose the split.",
     "Retain the split internally. It also breaks the 20%-of-numeral-22 control above, so document "
     "the reason before the control fires."),
    ("Non-employment work income under par. 5", "Payroll engine / accounts payable",
     "Where the employer pays a natural person work income that does NOT arise from an employment, "
     "legal or statutory relationship, report it HERE if it was withheld under ET art. 383 "
     "(art. 383 par. 2, added by Ley 2277 de 2022 art. 8, using the pagos mensualizados method). "
     "Where art. 383 withholding did NOT apply, report it in the ordinary payments-and-withholdings "
     "formats instead - not here.",
     "The test is about the WITHHOLDING REGIME, not about residence and not about employment "
     "status. It is the most commonly misread paragraph of the article, and it determines which "
     "FORMAT the payment appears in, not merely which numeral."),
    ("Work performed entirely abroad by a non-resident", "Payroll engine (tax)",
     "Foreign-source income, not withheld, and NOT reported in this return at all.",
     "The evidencing field is the nomina electronica place of work (NIE050). Keep the two "
     "consistent: a document showing a non-CO place of work for a non-resident should produce no "
     "2276 record."),

    "CROSS-FIELD VALIDATIONS",
    ("Numeral 22 arithmetic", "Engine (validation)",
     "Numeral 22 must equal the sum of numerals 5 to 21, EXCLUDING numeral 32. Assert it, and "
     "assert equality with Formulario 220 casilla 52 for the same employee.",
     "The exclusion of numeral 32 is the trap. Every other value numeral enters the total."),
    ("Numerals 8 and 32 are a pair", "Engine (validation)",
     "Where either is non-zero the other is normally non-zero too, because the same underlying "
     "payment is split at 41 UVT. The exception is an employee earning over 310 UVT, where both are "
     "nil and the payment sits in numeral 7 instead.",
     "Three-way interlock between numerals 7, 8 and 32, driven by two monthly UVT tests."),
    ("Numerals 18, 19, 20 and 33 travel together", "Engine (validation)",
     "Where any of numerals 18, 19 or 20 is non-zero, numeral 33 should be populated, because ET "
     "art. 206 num. 4 applies. Where all three are zero, numeral 33 should be blank.",
     "The resolution restricts numeral 33 with the word 'unicamente', so populating it "
     "unnecessarily is as wrong as omitting it when required."),
    ("Numeral 1 drives numerals 35 and 36", "Engine (validation)",
     "Concepto 1 - both blank. Concepto 2 - numeral 35 populated, numeral 36 blank. Conceptos 3 to "
     "8 - numeral 36 populated, numeral 35 blank.",
     "Implement as a three-branch rule, not as two independent nullable fields."),
    ("Cross-report reconciliation", "Engine (reconciliation)",
     "Before filing, assert per beneficiary: numeral 22 equals Formulario 220 casilla 52; numeral 29 "
     "equals casilla 60 and twelve months of nomina electronica NIE177; numerals 23 and 24 equal "
     "casillas 53 and 54 and the employee portions of PILA campos 55, 47, 51 and 52; numeral 19 "
     "equals the deposit made under CO-CESANTIAS-006; numeral 34 equals Formulario 220 casillas 79 "
     "and 80. Across the population, assert that the sum of numeral 29 equals twelve months of "
     "Formulario 350 casilla 93.",
     "MAP THE SEVERANCE LINES BY MEANING: numeral 18 to casilla 47, numeral 19 to casilla 49, "
     "numeral 20 to casilla 48. A positional mapping swaps the fund deposit and the "
     "traditional-regime amount, and the error is invisible in the totals because both feed "
     "numeral 22."),
]

# ===========================================================================
#  SHEET 8 - EXAMPLE ANALYSIS
# ===========================================================================
CFG["example"] = [
    "WORKED EXAMPLE - TAX YEAR 2026 RECORD, FILED IN 2027",
    ("(scenario)", "Informant", "MERCANS COLOMBIA S.A.S., NIT 900123456-7, persona juridica.",
     "NIT ends in 56, so under Res. 227 art. 1.3.9.1.3 the record is due on the 1st business day of "
     "June 2027."),
    ("(scenario)", "Beneficiary", "Juan Carlos Perez Gomez, CC 1020304050, employed the whole of "
     "2026, salary COP 12,000,000 a month, tax RESIDENT.",
     "The same employee and the same annual build-up as the Formulario 220 workbook, so the two "
     "can be reconciled line by line."),

    "REPORTING ENTITY AND BENEFICIARY",
    ("1", "N01 - Entidad informante", "Informante general.",
     "Res. 227 par. 4 requires concepto 1 for an ordinary employer, and numerals 35 and 36 are then "
     "left blank."),
    ("13 / 1020304050", "N02 - Tipo de documento y numero de identificacion",
     "Composite: document-type code plus the number.",
     "The join key across every Colombian artefact. Note that the three artefacts use THREE "
     "different document-type catalogues - the nomina electronica's numeric table 5.2.1, "
     "Formulario 220's six-value list, and PILA's two-letter codes. Map, never copy."),
    ("PEREZ / GOMEZ / JUAN / CARLOS", "N03 - Apellidos y nombres",
     "Composite: four sub-fields in the standard DIAN order.",
     "DIAN matches on the surname columns, so the order matters."),
    ("11 / 001", "N04 - Ubicacion del beneficiario", "Bogota D.C.",
     "The BENEFICIARY's location - a different question from the nomina electronica place of work "
     "and from the Formulario 220 place where the withholding was practised."),

    "INCOME CONCEPTS",
    ("144000000", "N05 - Pagos por salarios", "Twelve months at COP 12,000,000.",
     "Equals Formulario 220 casilla 36."),
    ("0", "N06 - Emolumentos eclesiasticos", "Not applicable.",
     "A SEPARATE numeral here; Formulario 220 folds ecclesiastical emoluments into casilla 39 "
     "(honorarios). Written as ZERO, per par. 2."),
    ("0", "N07 - Bonos, cheques, tarjetas, vales", "No such payments.",
     "Par. 6: this numeral must not repeat anything reported elsewhere in the format. It is "
     "residual."),
    ("0 / 0", "N08 / N32 - Alimentacion",
     "No third-party meal payments, so both the excess (N08) and the informative amount up to "
     "41 UVT (N32) are nil.",
     "Had there been meal payments, the monthly fork would apply: salary above 310 UVT sends the "
     "whole amount to N07; salary at or below 310 UVT splits it at 41 UVT between N32 "
     "(informative) and N08 (taxable)."),
    ("12000000", "N12 - Prestaciones sociales",
     "The statutory service bonus, paid in two instalments by 30 June and 20 December.",
     "Excludes severance and its interest, which have their own three numerals. Equals Formulario "
     "220 casilla 42."),

    "THE THREE SEVERANCE NUMERALS - AND THE TRANSPOSITION",
    ("1440000", "N18 - Cesantias e intereses PAGADAS al empleado",
     "The 12% interest on the 31 December 2025 balance, paid in January 2026.",
     "= Formulario 220 casilla 47. Same position in both artefacts."),
    ("12000000", "N19 - Cesantias CONSIGNADAS al fondo",
     "One month's salary for 2026, deposited by 14 February 2027.",
     "= FORMULARIO 220 CASILLA 49, NOT casilla 48. Must also reconcile to the deposit under "
     "CO-CESANTIAS-006, where late payment costs one day's salary per day of delay, uncapped."),
    ("0", "N20 - Regimen tradicional del CST",
     "The employee is under the Ley 50 de 1990 regime, so this is nil.",
     "= FORMULARIO 220 CASILLA 48, NOT casilla 49. THE SECOND AND THIRD SEVERANCE LINES ARE "
     "TRANSPOSED between the two artefacts. A positional mapping swaps them, and the error is "
     "invisible in the totals because both feed numeral 22."),

    "TOTAL AND CONTRIBUTIONS",
    ("157440000", "N22 - Total ingresos brutos",
     "144,000,000 + 12,000,000 + 1,440,000 + 12,000,000 = 157,440,000.",
     "Numerals 5 to 21 summed, EXCLUDING numeral 32 - par. 1 makes that informative. Equals "
     "Formulario 220 casilla 52."),
    ("5760000", "N23 - Aportes obligatorios por salud", "Twelve months at COP 480,000.",
     "= Formulario 220 casilla 53; reconciles to twelve months of nomina electronica NIE163 and to "
     "the employee portion of PILA campo 55."),
    ("7200000", "N24 - Aportes obligatorios a pensiones y solidaridad pensional",
     "Twelve months at COP 600,000 - pension 480,000 plus solidarity 120,000.",
     "ONE numeral for TWO concepts, as in Formulario 220 casilla 54. The nomina electronica keeps "
     "them as NIE166 and NIE168; PILA as campos 47 and 51. Sum only here."),
    ("0 / 0 / 0 / 0", "N25 / N26 / N27 / N28", "No voluntary savings.",
     "N25 and N26 split what the nomina electronica carries in ONE element (NIE198); N28 (AVC) has "
     "no nomina electronica element at all and must be tagged on the wage type."),

    "WITHHOLDING AND SPECIAL NUMERALS",
    ("7404000", "N29 - Retenciones practicadas",
     "The year's withholding under the ET art. 383 table.",
     "= Formulario 220 casilla 60; reconciles to twelve months of nomina electronica NIE177, and "
     "across the population to twelve months of Formulario 350 casilla 93."),
    ("13120000", "N33 - Ingreso laboral promedio de los ultimos seis meses",
     "Populated because severance was paid and deposited, so ET art. 206 num. 4 applies.",
     "Below 350 UVT (COP 18,330,900), so the severance in N18 and N19 is exempt in full. The "
     "resolution restricts this numeral with the word 'UNICAMENTE' - do not populate it where "
     "numerals 18, 19 and 20 are all nil."),
    ("(blank)", "N34 - Dependiente economico", "No dependant claimed.",
     "Where one is claimed, this must be byte-identical to Formulario 220 casillas 79 and 80. It is "
     "where DIAN cross-checks a dependant claimed by more than one taxpayer."),
    ("(blank) / (blank)", "N35 / N36", "Not applicable under concepto 1.",
     "Res. 227 par. 4: for an ordinary employer they 'no se deben diligenciar'. They are mutually "
     "exclusive with each other."),
    ("0 / 0", "N30 / N31 - IVA", "Not payroll fields.",
     "Colombian employment income carries no VAT. Relevant only for a VAT-responsible contractor "
     "paid under the art. 383 table; owned by the client's tax function."),

    "NON-RESIDENT CONTRAST (v2.8 control B1)",
    ("157440000 / 31488000", "N22 / N29 for a NON-RESIDENT",
     "The same gross, withheld at the flat 20% of ET art. 408.",
     "USEFUL CONTROL: for a pure non-resident record, N29 is almost exactly 20% of N22. Here "
     "31,488,000 / 157,440,000 = 20.00%. A resident's ratio is 4.7%. The format has no residence "
     "field, so this arithmetic is the only signal - and a mid-year residence change breaks it, "
     "which is itself worth flagging before the control fires."),
    ("5760000 / 7200000", "N23 / N24 for a NON-RESIDENT", "Unchanged - the contributions were still "
     "deducted.", "But they did NOT reduce the withholding base: art. 408 taxes the gross."),
    ("13120000", "N33 for a NON-RESIDENT", "Reported where severance was paid, but of no effect.",
     "The art. 206 num. 4 exemption belongs to the resident cedula-general regime."),

    "FILING",
    ("Persona juridica, NIT ...56", "Deadline",
     "1st business day of June 2027, per Res. 227 art. 1.3.9.1.3.",
     "THREE DIFFERENT DEADLINE RULES across the pipeline: Formulario 350 by the LAST digit, 7th-16th "
     "business day of the following MONTH; PILA by the LAST TWO digits, 2nd-16th business day of "
     "the following MONTH; this return by the last digit for Grandes Contribuyentes and the last "
     "two for everyone else, in MAY or JUNE of the following YEAR."),
    ("(at filing)", "Calidad del informante",
     "Art. 1.3.9.1.3 par. 1: the status held AT THE MOMENT OF FILING governs.",
     "An employer that becomes a Gran Contribuyente between the year end and the filing date files "
     "on the EARLIER Gran Contribuyente calendar, not the later one."),
]

# ===========================================================================
#  SHEET 9 - SAMPLE FILE
# ===========================================================================
CFG["sample_title"] = "VERIFIED CHANNEL STATEMENT AND NEUTRAL RECORD MODEL"
CFG["sample"] = r"""
WHY THERE IS NO XML SAMPLE
==========================
Formato 2276 version 4 is uploaded as a file to the DIAN informacion exogena
service, and the exogena service accepts XML. That much is CONFIRMED from
Resolucion DIAN 000227 de 2025 arts. 1.3.7.1.1 and 1.3.10.1, both held locally.

What is NOT held locally, and is not published inside the resolution, is the
ESPECIFICACIONES TECNICAS annex for Formato 2276 version 4 - the document that
fixes the XML element names, the field ordering and the column lengths. The
resolution only points to it ("de acuerdo con los parametros establecidos en las
especificaciones tecnicas del Formato 2276 Version 4") and lists it in the
formats table at art. 1.3.10.1 as entry T3.45.

Writing an XML instance here would therefore mean INVENTING element names. That
is exactly the fabrication the v2.7 standard forbids and the C25 audit fails.

What follows instead is a NEUTRAL RECORD MODEL: the resolution's own thirty-six
numerals in their published order, populated with the worked example. This is
the content the engine must produce; the wrapper comes from the especificaciones
tecnicas.

FORMAT TO CONFIRM vs a real filing: obtain the published especificaciones
tecnicas for Formato 2276 v4 and map each numeral below to its element name,
ordinal position and column length before configuring a productive layout.

-------------------------------------------------------------------------------
ENVELOPE (attributes the deadline and validation depend on)
-------------------------------------------------------------------------------
  Informant NIT ......................... 900123456
  Taxpayer category ..................... Persona juridica
  Tax year reported ..................... 2026
  Format / version ...................... 2276 / 4   (Res. 227 art. 1.3.10.1, T3.45)
  Deadline .............................. 1st business day of June 2027
                                          (NIT ends 56; art. 1.3.9.1.3)

-------------------------------------------------------------------------------
RECORD - ONE PER BENEFICIARY
Res. DIAN 000227 de 2025, art. 1.3.7.1.1, numerals 1 to 36 in published order
-------------------------------------------------------------------------------
  N01  Entidad informante ...................... 1  (Informante general)
  N02  Tipo doc. y numero de identificacion .... 13 / 1020304050
  N03  Apellidos y nombres ..................... PEREZ / GOMEZ / JUAN / CARLOS
  N04  Ubicacion del beneficiario .............. 11 / 001  (Bogota D.C.)

  N05  Pagos por salarios ...................... 144000000
  N06  Pagos por emolumentos eclesiasticos .....         0
  N07  Bonos, cheques, tarjetas, vales, etc. ...         0
  N08  Exceso alimentacion > 41 UVT (art.387-1)          0
  N09  Pagos por honorarios ....................         0
  N10  Pagos por servicios .....................         0
  N11  Pagos por comisiones ....................         0
  N12  Pagos por prestaciones sociales .........  12000000
  N13  Pagos por viaticos ......................         0
  N14  Pagos por gastos de representacion ......         0
  N15  Compensaciones trabajo asociado coop. ...         0
  N16  Apoyos economicos educativos (Estado) ...         0
  N17  Otros pagos .............................         0

  N18  Cesantias e intereses PAGADAS al empleado   1440000    -> F220 casilla 47
  N19  Cesantias CONSIGNADAS al fondo ..........  12000000    -> F220 casilla 49  (NOT 48)
  N20  Cesantias REGIMEN TRADICIONAL del CST ...         0    -> F220 casilla 48  (NOT 49)

  N21  Pensiones de jubilacion, vejez, invalidez         0
  N22  TOTAL INGRESOS BRUTOS ................... 157440000
       (numerals 5 to 21; numeral 32 is EXCLUDED - par. 1 makes it informative)

  N23  Aportes obligatorios por salud ..........   5760000
  N24  Aportes obligatorios pensiones y FSP ....   7200000
  N25  Aportes voluntarios RAIS ................         0
  N26  Aportes voluntarios fondos de pensiones .         0
  N27  Aportes a cuentas AFC ...................         0
  N28  Aportes a cuentas AVC ...................         0

  N29  RETENCIONES PRACTICADAS .................   7404000
  N30  IVA mayor valor del costo o gasto .......         0   (not a payroll field)
  N31  Retencion de IVA ........................         0   (not a payroll field)

  N32  Alimentacion mensual hasta 41 UVT .......         0   INFORMATIVE - outside N22
  N33  Ingreso laboral promedio ultimos 6 meses  13120000   (only where art.206 num.4 applies)
  N34  Dependiente economico ...................   (blank)   (none claimed)
  N35  Identificacion del fideicomiso ..........   (blank)   (par. 4: blank under concepto 1)
  N36  Participante en contrato ................   (blank)   (par. 4: blank under concepto 1)

-------------------------------------------------------------------------------
NON-RESIDENT VARIANT (v2.8 control B1)
-------------------------------------------------------------------------------
The same record for a NON-RESIDENT differs in exactly one numeral - the format
has no residence field:

  N22  TOTAL INGRESOS BRUTOS ................... 157440000   (unchanged)
  N23  Aportes obligatorios por salud ..........   5760000   (unchanged - still deducted)
  N24  Aportes obligatorios pensiones y FSP ....   7200000   (unchanged - still deducted)
  N29  RETENCIONES PRACTICADAS .................  31488000   <== 20% of GROSS, ET art. 408
  N33  Ingreso laboral promedio ................  13120000   (reported, no effect)

INTERNAL CONTROL: for a pure non-resident record N29 / N22 = 20.00% exactly.
For this resident it is 4.70%. Because the format carries no residence flag,
that ratio is the only signal available - and a mid-year residence change
legitimately breaks it, so document the reason before the control fires.

The contributions in N23 and N24 are still reported because they were still
deducted, but they did NOT reduce the withholding base: ET art. 408 taxes the
gross with no depuration (DIAN Concepto 011108 of 29 June 2026). N33 is reported
where severance was paid but has no effect, because the art. 206 num. 4
exemption belongs to the resident cedula-general regime.

-------------------------------------------------------------------------------
THE FOUR TRAPS IN THIS RECORD
-------------------------------------------------------------------------------
1. N32 is INFORMATIVE and does NOT enter N22 (par. 1). Every other value numeral
   does. Including it overstates gross income and breaks the reconciliation to
   Formulario 220 casilla 52.

2. N19 and N20 are TRANSPOSED against Formulario 220 casillas 48 and 49. Map by
   MEANING. A positional mapping swaps the fund deposit and the traditional-
   regime amount, and the error is invisible in N22 because both feed it.

3. N07 must not double-report anything in another numeral (par. 6). Voucher and
   card payments can plausibly be classified as salary, as a meal benefit or as
   other payments - fix the classification on the wage type, once.

4. N33 is restricted by the word UNICAMENTE to employees to whom ET art. 206
   num. 4 applies. Populating it for everyone is as wrong as omitting it when
   required.
"""

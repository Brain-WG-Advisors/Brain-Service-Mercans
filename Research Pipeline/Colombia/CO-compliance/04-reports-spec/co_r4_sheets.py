# -*- coding: utf-8 -*-
"""CO-DIAN-004 - Sheets 5 to 9 for Formulario 220."""

from co_r4_formulario220 import CFG

# ===========================================================================
#  SHEET 5 - FILE STRUCTURE (neutral field model - this is a CERTIFICATE)
# ===========================================================================
CFG["filestruct"] = [
    ("##", "SUBMISSION FORMAT - VERIFIED (v2.7 STEP 3.5)"),
    ("Channel", "Issued TO THE EMPLOYEE, on paper or electronically as agreed, and RETAINED BY THE "
                "EMPLOYER. There is NO government channel: Formulario 220 is a certificate, not a "
                "return, and is not submitted to DIAN."),
    ("Source", "ET arts. 378, 379 and 380; DUR 1625 de 2016 art. 1.6.1.13.2.40 (deadline) and "
               "art. 1.6.1.13.2.7 (substitution for the income-tax return); the form's own "
               "instructivo, which addresses only issuing. CONFIRMED."),
    ("Why there is no file format", "DIAN prescribes the FORM but not a transmission format, "
                                    "because nothing is transmitted. The structure below is "
                                    "therefore a LOGICAL MODEL - the casilla list and its "
                                    "hierarchy - not a wire format."),
    ("Where DIAN does see this data", "Annually, through Formato 2276 (CO-DIAN-005), which IS "
                                      "filed. The two obligations overlap in content but differ in "
                                      "field set, ordering and deadline, and neither is derived "
                                      "from the other."),
    ("Retention", "The employer retains the issued certificate as evidence of the withholding. "
                  "Where the employee signs the six ET art. 380 declarations, the certificate "
                  "substitutes for their income-tax return, so its evidential value runs beyond "
                  "the employer."),

    ("##", "LOGICAL MODEL - SECTIONS AND CASILLAS"),
    ("Header", "Formulario 220 | Ano gravable | 4 Numero de formulario (assigned BY THE EMPLOYER, "
               "not by DIAN)"),
    ("Section 1 - Agente retenedor", "5 NIT | 6 DV | 7 Primer apellido | 8 Segundo apellido | "
                                     "9 Primer nombre | 10 Otros nombres | 11 Razon social"),
    ("Section 2 - Trabajador o pensionado", "24 Tipo de documento | 25 Numero de identificacion | "
                                            "26 Primer apellido | 27 Segundo apellido | 28 Primer "
                                            "nombre | 29 Otros nombres"),
    ("Section 3 - Periodo y lugar", "30 Periodo DE | 31 Periodo A | 32 Fecha de expedicion | "
                                    "33 Lugar donde se practico la retencion | 34 Cod. Dpto. | "
                                    "35 Cod. Ciudad/Municipio"),
    ("Section 4 - Concepto de los ingresos",
     "36 Pagos por salarios | 37 Pagos con bonos, cheques, tarjetas, vales | 38 Exceso alimentacion "
     "> 41 UVT | 39 Honorarios | 40 Servicios | 41 Comisiones | 42 Prestaciones sociales | "
     "43 Viaticos | 44 Gastos de representacion | 45 Compensaciones trabajo asociado cooperativo | "
     "46 Otros pagos | 47 Cesantia e intereses PAGADOS AL EMPLEADO | 48 Cesantia REGIMEN "
     "TRADICIONAL | 49 Cesantia CONSIGNADA AL FONDO | 50 Pensiones | 51 Apoyos educativos con "
     "recursos publicos | 52 TOTAL INGRESOS BRUTOS (Sume 36 a 51)"),
    ("Section 5 - Concepto de los aportes",
     "53 Aportes obligatorios salud | 54 Aportes obligatorios pensiones Y SOLIDARIDAD (combined) | "
     "55 Cotizaciones voluntarias RAIS | 56 Aportes voluntarios a fondos de pensiones | 57 Aportes "
     "AFC | 58 Aportes AVC | 59 Ingreso laboral promedio de los ultimos seis meses | 60 VALOR DE LA "
     "RETENCION EN LA FUENTE"),
    ("Section 6 - Datos a cargo del trabajador",
     "61-66 Otros ingresos, valor recibido | 68-73 Otros ingresos, valor retenido | 67 Total "
     "recibido (Sume 61 a 66) | 74 Total retenido (Sume 68 a 73) | 75 TOTAL RETENCIONES ANO "
     "GRAVABLE (Sume 60 + 74)"),
    ("Section 7 - Patrimonio", "76 Identificacion de los bienes poseidos (3 rows) | 77 Valor "
                               "patrimonial | 78 Deudas vigentes a 31 de diciembre"),
    ("Section 8 - Dependiente economico", "79 Tipo documento | 80 No. Documento | 81 Apellidos y "
                                          "nombres | 82 Parentesco"),
    ("Section 9 - Certificacion ET art. 380", "Six unnumbered declarations plus the employee's "
                                              "signature. DISPLAY-ONLY - not data fields."),
    ("Section 10 - Firma", "Nombre del pagador o agente retenedor plus the issuing signature."),

    ("##", "ARITHMETIC PRINTED ON THE FORM"),
    ("Casilla 52", "Sume 36 a 51 - sixteen income casillas."),
    ("Casilla 67", "Sume 61 a 66 - employee-declared other income received."),
    ("Casilla 74", "Sume 68 a 73 - employee-declared other income withheld."),
    ("Casilla 75", "Sume 60 + 74 - the employer's withholding plus the employee-declared "
                   "withholding."),

    ("##", "AMOUNT AND ROUNDING CONVENTION"),
    ("Rounding", "The instructivo is explicit: values 'deben ser expresados en pesos colombianos y "
                 "aproximados al multiplo de mil (1.000) mas cercano'. The SAME convention as "
                 "Formulario 350, and NOT the nomina electronica convention of two decimals "
                 "round-half-to-even."),
    ("Nil values", "'En el evento en que no haya valor a registrar en alguna casilla escriba cero "
                   "(0)'. Write ZERO, do not leave blank. This differs from the nomina electronica, "
                   "where an inapplicable element is OMITTED rather than zero-filled."),
    ("RUT consistency", "The instructivo repeats for casillas 7 to 11 that where the value does not "
                        "match the RUT, THE RUT MUST BE UPDATED BEFORE THE CERTIFICATE IS ISSUED. "
                        "The certificate does not override the register."),

    ("##", "THE THREE SEVERANCE LINES - AND THE ORDERING TRAP"),
    ("Form 220", "47 = paid to the employee | 48 = traditional pre-1991 CST regime | 49 = deposited "
                 "to the fund"),
    ("Formato 2276", "18 = paid to the employee | 19 = deposited to the fund | 20 = traditional "
                     "pre-1991 CST regime"),
    ("The trap", "THE SECOND AND THIRD LINES ARE TRANSPOSED BETWEEN THE TWO ARTEFACTS. An "
                 "implementation that maps positionally - 47 to 18, 48 to 19, 49 to 20 - will swap "
                 "the fund deposit and the traditional-regime amount in the information return. Map "
                 "by MEANING, never by position."),
    ("Recorded defect", "The instructivo for casilla 42 cross-refers severance deposited to the "
                        "fund to 'la casilla 48'. The form's own printed label puts the fund "
                        "deposit at casilla 49 and the traditional regime at casilla 48. The form "
                        "layout is authoritative; the cross-reference is wrong. Escalated in "
                        "column T of casilla 42."),
]

# ===========================================================================
#  SHEET 6 - FIELD OPTIONS
# ===========================================================================
CFG["options"] = [
    "TIPO DE DOCUMENTO (casillas 24 and 79) - the SIX values printed on the form",
    ("12", "TI", "Tarjeta de identidad", "Identity card for a person aged 7 to 17."),
    ("13", "CC", "Cedula de ciudadania", "National identity card. The great majority of employees."),
    ("21", "TE", "Tarjeta de extranjeria", "Foreigner's identity card."),
    ("22", "CE", "Cedula de extranjeria", "Foreign resident's identity card."),
    ("31", "NIT", "NIT", "Tax identification number, where the beneficiary is an entity."),
    ("41", "PA", "Pasaporte", "Passport."),
    ("(gap)", "-", "-", "THIS LIST IS NARROWER THAN THE NOMINA ELECTRONICA LIST at Anexo table "
     "5.2.1, which also carries 11 Registro civil, 42 Documento de identificacion extranjero, "
     "47 PEP, 50 NIT de otro pais and 91 NUIP. There is NO code here for a PEP holder and none for "
     "a PPT holder (Decreto 216 de 2021) - which is the document the large majority of regularised "
     "Venezuelan migrants now hold. Escalated in column T of casilla 24."),

    "LAS TRES LINEAS DE CESANTIAS (casillas 47, 48, 49)",
    ("47", "PAGADA", "Auxilio de cesantia e intereses efectivamente pagados al empleado",
     "Severance savings and interest ACTUALLY PAID to the employee - the January interest payment, "
     "an authorised partial withdrawal, or a termination settlement. Formato 2276 numeral 18."),
    ("48", "TRADICIONAL", "Auxilio de cesantia reconocido a trabajadores del regimen tradicional "
     "del CST (Cap. VII, Tit. VIII, Parte Primera)",
     "Severance RECOGNISED under the pre-1991 retroactive regime, for employees hired before "
     "1 January 1991 who did not elect the Ley 50 de 1990 regime. Formato 2276 numeral 20 - NOT 19."),
    ("49", "FONDO", "Auxilio de cesantia consignado al fondo de cesantias",
     "The amount DEPOSITED to the employee's chosen fund by 14 February under Ley 50 de 1990 "
     "art. 99. Formato 2276 numeral 19 - NOT 20. Must reconcile to CO-CESANTIAS-006."),
    ("(mapping warning)", "-", "-", "The second and third lines are TRANSPOSED between Form 220 and "
     "Formato 2276. Map by meaning, never by position."),

    "UMBRALES UVT 2026 (UVT = COP 52,374, Res. DIAN 000238 de 15 dic 2025)",
    ("41 UVT", "2,147,334", "Tope mensual de pagos por alimentacion, art. 387-1",
     "Monthly meal payments to a third party up to this amount are not income of the employee. The "
     "EXCESS goes to casilla 38."),
    ("310 UVT", "16,235,940", "Salario mensual maximo para el beneficio de alimentacion",
     "Where the employee's monthly salary EXCEEDS this, the art. 387-1 exclusion does not apply at "
     "all and the WHOLE meal payment goes to casilla 37, not casilla 38."),
    ("350 UVT", "18,330,900", "Ingreso laboral promedio para la exencion de cesantias, art. 206 "
     "num. 4", "Severance savings and interest are exempt in full where the six-month average "
     "labour income in casilla 59 does not exceed this; tapered above it."),
    ("1,000 UVT", "52,374,000", "Tope mensual exento de pensiones, art. 206 num. 5",
     "Employer-paid pension income is taxable only above this monthly amount. Casilla 50."),
    ("32 UVT", "1,675,968", "Tope mensual de la deduccion por dependientes, art. 387 par. 2",
     "The dependants deduction is 10% of gross employment income capped at this monthly amount. "
     "Evidenced by casillas 79 to 82."),
    ("790 UVT", "41,375,460", "Tope anual de la renta exenta del 25%, art. 206 num. 10",
     "Annual cap on the 25% exempt income. Mercans apportions at 65.8333 UVT per month - see "
     "scope_manifest CO-GAP-05."),
    ("1,340 UVT", "70,181,160", "Tope anual conjunto de deducciones y rentas exentas, art. 336",
     "Annual cap on deductions plus exempt income, alongside the 40% limit. Mercans apportions at "
     "111.6667 UVT per month - see CO-GAP-05."),
    ("4,500 UVT", "235,683,000", "Patrimonio bruto - condicion 1 del art. 380",
     "One of the six conditions under which this certificate substitutes for the income-tax return."),
    ("1,400 UVT", "73,323,600", "Ingresos brutos, consumos y consignaciones - condiciones 2, 4, 5 y "
     "6 del art. 380", "The remaining monetary conditions for substitution."),

    "PARENTESCO - DEPENDIENTE ECONOMICO (casilla 82, ET art. 387 par. 2). Casilla 82 accepts "
    "FREE TEXT, so the engine emits the Local (ES) wording; the Code column is the "
    "Mercans-internal normalisation and is the SAME code table as the Data Dictionary mapper "
    "'Dependant Relationship'. The five limbs are EXHAUSTIVE.",
    ("HIJO-M18", "H18", "Hijos menores de 18 anos", "Children under 18."),
    ("HIJO-EST", "HED", "Hijos entre 18 y 23 anos financiados por el contribuyente en su educacion",
     "Children aged 18 to 23 whose education the taxpayer finances at a recognised institution."),
    ("HIJO-DEP", "HDP", "Hijos mayores de 23 anos en situacion de dependencia certificada",
     "Children over 23 with certified physical or psychological dependency."),
    ("CONYUGE", "CON", "Conyuge o companero permanente en situacion de dependencia",
     "Spouse or permanent partner in a certified state of dependency by absence of income or "
     "physical or psychological factors."),
    ("ASCEND-HERM", "APH", "Padres y hermanos en situacion de dependencia",
     "Parents and siblings in a certified state of dependency."),

    "DIVIPOLA (DANE) - casillas 34 and 35",
    ("11", "BOG-DPTO", "Bogota D.C. - departamento", "TWO-digit DANE department code. The "
     "instructivo directs the use of the DANE 'Codigo de departamentos' tables."),
    ("001", "BOG-MPIO", "Bogota D.C. - ciudad/municipio", "THREE-digit DANE municipality code. Like "
     "PILA and unlike the nomina electronica, Form 220 splits the code across two casillas."),

    "CONCEPTS THAT ARE CERTIFIED BUT NOT WITHHELD AS EMPLOYMENT INCOME",
    ("Casilla 38", "-", "Exceso de alimentacion sobre 41 UVT",
     "Taxable income of the employee, withheld as EMPLOYMENT income."),
    ("Casilla 47", "-", "Cesantias e intereses pagados",
     "Certified here, but EXCLUDED from the monthly withholding base under both Procedure 1 and "
     "Procedure 2 because of the ET art. 206 num. 4 exemption and its taper."),
    ("Casilla 50", "-", "Pensiones",
     "Taxable only above 1,000 UVT per month; below that, certified at zero."),
]

# ===========================================================================
#  SHEET 7 - POPULATION RULES
# ===========================================================================
CFG["population"] = [
    "MANDATORY FIELD RULES",
    ("Casilla 4 - Numero de formulario", "Engine sequence",
     "Assign the certificate number from the ENGINE's own series - the instructivo says it is "
     "'asignado por la persona natural o juridica que expide la certificacion'. Keep the series "
     "stable and unique per employee per tax year, because the employee may quote it when filing "
     "or when asking for a duplicate.",
     "SHARP CONTRAST WITH FORMULARIO 350, where casilla 4 is DIAN-assigned. Do not reuse the Form "
     "350 numbering logic here."),
    ("Casillas 30 and 31 - Periodo de la certificacion", "Payroll engine",
     "Set casilla 30 to 1 January or the hire date, whichever is later, and casilla 31 to "
     "31 December or the termination date, whichever is earlier. Write year, month, day in that "
     "order, as the instructivo directs.",
     "A leaver certificate covers only the employment window. It is still due by the last business "
     "day of March following the tax year, not on termination."),
    ("Casilla 36 - Pagos por salarios", "Payroll engine",
     "Accumulate salary payments ACTUALLY MADE in the period, on the CST art. 127 definition the "
     "instructivo quotes in full - ordinary fixed or variable remuneration plus everything received "
     "in money or in kind as direct consideration for the service: primas, sobresueldos, habitual "
     "bonuses, overtime, work on mandatory rest days, sales percentages and commissions. Then apply "
     "the exclusion rule: remove anything belonging in casillas 38 to 46.",
     "The exclusion rule is the trap. Commissions under an employment contract are salary and stay "
     "in casilla 36; commissions outside an employment relationship go to casilla 41. Per diems go "
     "to casilla 43 even where the permanent portion is salary for contribution purposes. The "
     "certificate's classification and the contribution base's classification are NOT the same."),
    ("Casillas 47, 48 and 49 - the three severance lines", "Payroll engine",
     "Maintain THREE separate severance buckets from the outset, not one: (47) amounts and interest "
     "ACTUALLY PAID to the employee, (48) amounts RECOGNISED under the pre-1991 traditional CST "
     "regime, and (49) amounts DEPOSITED to the fund by 14 February. Casillas 48 and 49 are "
     "mutually exclusive for the same employee, because an employee is in one regime or the other.",
     "They CANNOT be split retrospectively out of a single annual cesantias figure. And when "
     "mapping to Formato 2276, map by MEANING: 47 to numeral 18, 48 to numeral 20, 49 to numeral "
     "19. The second and third lines are transposed between the two artefacts."),
    ("Casilla 59 - Ingreso laboral promedio de los ultimos seis meses", "Payroll engine",
     "Maintain a rolling six-month average of labour income YEAR-ROUND and store it monthly. On a "
     "termination, use the average of the last six months OF EMPLOYMENT. The average drives the ET "
     "art. 206 num. 4 severance exemption: full exemption where it does not exceed 350 UVT "
     "(COP 18,330,900 per month in 2026), tapered above.",
     "This is the single field on the certificate that cannot be reconstructed at year end. A "
     "moving six-month window is not derivable from twelve annual totals, and getting it wrong "
     "changes the exemption on the severance, not merely the disclosure."),
    ("Casilla 60 - Valor de la retencion", "Payroll engine (tax)",
     "Accumulate the retencion en la fuente actually practised on this employee's work and pension "
     "income during the certified period. For a RESIDENT this is the ET art. 383 table result under "
     "Procedure 1 or 2; for a NON-RESIDENT it is the flat 20% of ET art. 408 on the gross. Where "
     "the employee changed residence status mid-year, sum both.",
     "Reconcile to twelve months of nomina electronica NIE177 for this employee BEFORE issuing. A "
     "certificate that disagrees with the transmitted documents is evidence against the employer, "
     "because the XML is the tax support for the cost."),

    "CRITICAL VALIDATION RULES",
    ("Write zero, never blank", "Engine (formatting)",
     "The instructivo directs: 'En el evento en que no haya valor a registrar en alguna casilla "
     "escriba cero (0)'. Every money casilla is populated, with zero where there is nothing.",
     "This INVERTS the nomina electronica rule, where an inapplicable element is OMITTED rather "
     "than zero-filled. Two artefacts, two opposite conventions, from the same authority."),
    ("Round to the nearest 1,000", "Engine (formatting)",
     "All money casillas are expressed in Colombian pesos and approximated to the nearest 1,000, "
     "exactly as on Formulario 350. Apply the rounding to each casilla value, then check that the "
     "printed sums still tie - casilla 52 = sum of 36 to 51, casilla 75 = 60 + 74.",
     "Rounding sixteen casillas independently can make casilla 52 differ from the rounded sum of "
     "the unrounded parts by up to 8,000 pesos. Compute casilla 52 from the ROUNDED casillas so "
     "the arithmetic printed on the form holds."),
    ("RUT consistency before issue", "Engine (control)",
     "Casillas 5 to 11 must match casillas 5, 6, 31, 32, 33, 34 and 35 of the RUT. The instructivo "
     "repeats for each that where they do not match, THE RUT MUST BE UPDATED BEFORE THE CERTIFICATE "
     "IS ISSUED.",
     "Do not let the certificate diverge from the register in order to meet the March deadline - "
     "the register governs."),
    ("Casilla 37 versus casilla 38 - the meal-payment fork", "Payroll engine",
     "Where the employee's monthly salary EXCEEDS 310 UVT (COP 16,235,940 in 2026), the WHOLE meal "
     "payment goes to casilla 37 and casilla 38 stays nil. Where it does not exceed 310 UVT, the "
     "payment is not income up to 41 UVT (COP 2,147,334) and only the EXCESS goes to casilla 38, "
     "with nothing in casilla 37 for that concept.",
     "Two thresholds, applied in sequence, and the outcome routes the amount to a DIFFERENT "
     "casilla. Both tests are MONTHLY, so an employee can fork one way in some months and the other "
     "way in others within the same certificate."),
    ("Casilla 48 and casilla 49 are mutually exclusive", "Engine (validation)",
     "An employee is either in the pre-1991 traditional severance regime or in the Ley 50 de 1990 "
     "annual-deposit regime, not both. Assert that at most one of the two is non-zero for any "
     "employee.",
     "The only exception is a transition year in which an employee formally elected the new regime "
     "- rare, and worth an explicit override rather than a silent allowance."),

    "AMOUNT FORMAT RULES",
    ("Casilla 54 combines two concepts", "Engine (accumulation)",
     "Casilla 54 carries mandatory PENSION contributions AND the solidarity-fund surcharge in ONE "
     "figure. The nomina electronica reports them as three separate elements (NIE166, NIE168, "
     "NIE170) and PILA as three separate campos (47, 51, 52). Keep them separate internally and sum "
     "them only at this casilla.",
     "Summing them earlier makes the nomina electronica and PILA outputs impossible to produce "
     "correctly."),
    ("Casillas 55 and 56 split one nomina electronica element", "Engine (accumulation)",
     "Casilla 55 is voluntary contributions to the RAIS under ET art. 55; casilla 56 is voluntary "
     "contributions to VOLUNTARY pension funds under ET art. 126-1. The nomina electronica has ONE "
     "element for both (PensionVoluntaria, NIE198), so the engine must carry the distinction on the "
     "wage type.",
     "Different legal bases, different caps in some scenarios. Combining them here is a "
     "misstatement even though the XML cannot tell them apart."),
    ("Casilla 58 has no nomina electronica element", "Engine (accumulation)",
     "AVC contributions to the Fondo Nacional del Ahorro have no dedicated nomina electronica "
     "element and fall to OtraDeduccion (NIE197). Tag the wage type so the amount can be recovered "
     "for this casilla and for Formato 2276 numeral 28.",
     "Without the tag the amount is indistinguishable from any other 'other deduction' at year end."),

    "PAYROLL-SPECIFIC POPULATION RULES",
    ("Non-resident certificate", "Payroll engine (tax)",
     "Issue the same certificate. Casilla 52 carries the gross and casilla 60 carries 20% of it "
     "under ET art. 408 - so the two stand in a simple 20% relationship with no depuration visible. "
     "Casillas 53 and 54 still report the contributions actually deducted, even though they did NOT "
     "reduce the withholding base for a non-resident.",
     "Casilla 59 is reported for completeness but has no effect: the ET art. 206 num. 4 severance "
     "exemption is an exemption of the RESIDENT cedula-general regime and does not attach to a "
     "non-resident's flat withholding."),
    ("Mid-year residence change", "Payroll engine (tax)",
     "Issue ONE certificate for the whole period. Casilla 60 sums the months withheld at 20% under "
     "art. 408 and the months withheld under the art. 383 table. The form has no field to disclose "
     "the split.",
     "Retain the split internally for audit and for any DIAN enquiry. The employee reconciles on "
     "their own return; the employer performs no true-up."),
    ("Dependants (casillas 79 to 82)", "Employee master data",
     "Populate all four casillas together where the employee claimed the ET art. 387 par. 2 "
     "dependants deduction during the period. The deduction is 10% of gross employment income "
     "capped at 32 UVT per month (COP 1,675,968 in 2026).",
     "The same dependant is reported in Formato 2276 numeral 34, which is where DIAN cross-checks "
     "a dependant claimed by more than one taxpayer. Keep the two consistent or the employee "
     "receives an enquiry."),
    ("Employee-declared sections (casillas 61 to 78)", "The employee",
     "Payroll does NOT populate casillas 61 to 78. They are supplied by the employee so that the "
     "certificate can substitute for the income-tax return under ET art. 380. Provide the employee "
     "with a means to supply them and leave them at zero where the employee does not.",
     "Issuing the certificate with these sections at zero does not invalidate it - it simply means "
     "the employee cannot rely on it as a substitute return and must file."),

    "CROSS-FIELD VALIDATIONS",
    ("Casilla 52 arithmetic", "Engine (validation)",
     "Casilla 52 must equal the sum of the ROUNDED casillas 36 to 51. Assert it before issuing.",
     "Sixteen casillas. A single mis-classified concept both understates one casilla and overstates "
     "another while leaving casilla 52 correct - so also reconcile casilla 52 to the annual gross "
     "from the nomina electronica."),
    ("Casilla 75 arithmetic", "Engine (validation)",
     "Casilla 75 must equal casilla 60 plus casilla 74. Where the employee supplies nothing, "
     "casilla 74 is zero and casilla 75 equals casilla 60.", "-"),
    ("Casillas 79 to 82 populate together", "Engine (validation)",
     "All four dependant casillas are populated together or none is. A document number without a "
     "relationship, or a relationship without a number, is incomplete.", "-"),
    ("Cross-report reconciliation", "Engine (reconciliation)",
     "Before issuing, assert per employee: casilla 60 equals twelve months of nomina electronica "
     "NIE177; casilla 53 equals twelve months of NIE163 and the employee portion of PILA campo 55; "
     "casilla 54 equals twelve months of NIE166 + NIE168 + NIE170 and the employee portions of PILA "
     "campos 47, 51 and 52; casilla 49 equals the amount actually deposited under CO-CESANTIAS-006. "
     "Across the population, assert that the sum of casilla 60 equals twelve months of Formulario "
     "350 casilla 93.",
     "Reconcile on the UNROUNDED values with a tolerance, because the four artefacts round three "
     "different ways. A material difference means a payment was made without a nomina electronica "
     "document, or a document was rejected and never re-transmitted."),
]

# ===========================================================================
#  SHEET 8 - EXAMPLE ANALYSIS
# ===========================================================================
CFG["example"] = [
    "WORKED EXAMPLE - CERTIFICATE FOR TAX YEAR 2026",
    ("(scenario)", "Employer", "MERCANS COLOMBIA S.A.S., NIT 900123456-7, Bogota D.C.",
     "Same employer as the other five Colombia Spec workbooks."),
    ("(scenario)", "Employee", "Juan Carlos Perez Gomez, CC 1020304050, employed the whole of 2026, "
     "salary COP 12,000,000 a month, tax RESIDENT.",
     "Twelve months of the March figures used in the nomina electronica and PILA workbooks, plus "
     "the annual statutory benefits."),
    ("(scenario)", "Annual build-up",
     "Salary 12 x 12,000,000 = 144,000,000. Prima de servicios 12,000,000 (two instalments). "
     "Cesantias for 2026 = 12,000,000, deposited to the fund by 14 February 2027. Interest on the "
     "2025 cesantias balance = 1,440,000, paid in January 2026.",
     "The January interest payment falls in the 2026 certificate because Colombia certifies on the "
     "PAYMENT date, not the accrual date."),

    "HEADER AND IDENTIFICATION",
    ("2026-000417", "Casilla 4 - Numero de formulario", "Assigned by the EMPLOYER.",
     "Contrast Formulario 350, where casilla 4 is DIAN-assigned. Keep the series stable - the "
     "employee may quote it."),
    ("900123456 / 7", "Casillas 5 / 6", "Employer NIT and verification digit.",
     "Without dots, hyphens or letters, as the instructivo insists."),
    ("MERCANS COLOMBIA S.A.S.", "Casilla 11 - Razon social", "Legal person.",
     "Casillas 7 to 10 stay blank; the instructivo says a natural-person issuer must not fill "
     "casilla 11."),
    ("13 / 1020304050", "Casillas 24 / 25", "Cedula de ciudadania.",
     "Had the employee held a PEP or a PPT, neither has a code in the six-value list printed on "
     "this form - escalated in column T."),
    ("2026 01 01 / 2026 12 31", "Casillas 30 / 31", "Full calendar year certified.",
     "A leaver would carry the termination date in casilla 31."),
    ("2027 03 31", "Casilla 32 - Fecha de expedicion", "Issued on the last business day of March "
     "2027.", "The statutory deadline under DUR 1625 de 2016 art. 1.6.1.13.2.40."),

    "INCOME CONCEPTS",
    ("144.000.000", "Casilla 36 - Pagos por salarios",
     "Twelve months at COP 12,000,000, on the CST art. 127 definition.",
     "Excludes anything belonging in casillas 38 to 46 - here, the prima and the cesantias."),
    ("0", "Casilla 37 / Casilla 38", "No voucher or meal payments.",
     "Written as ZERO, not left blank: 'escriba cero (0)'. This inverts the nomina electronica "
     "convention, where an inapplicable element is omitted."),
    ("12.000.000", "Casilla 42 - Pagos por prestaciones sociales",
     "The statutory service bonus (prima de servicios), paid in two instalments by 30 June and "
     "20 December.",
     "Excludes severance and its interest, which go to casillas 47 to 49. Vacation pay and "
     "dotaciones would also sit here."),
    ("1.440.000", "Casilla 47 - Cesantia e intereses pagados al empleado",
     "The 12% interest on the 31 December 2025 severance balance, paid to the employee during "
     "January 2026.",
     "Excluded from the monthly withholding base under ET art. 206 num. 4, but still certified. "
     "Maps to Formato 2276 numeral 18."),
    ("0", "Casilla 48 - Regimen tradicional", "The employee is under the Ley 50 de 1990 regime.",
     "Mutually exclusive with casilla 49. Maps to Formato 2276 numeral 20 - NOT numeral 19."),
    ("12.000.000", "Casilla 49 - Cesantia consignada al fondo",
     "One month's salary for the year, deposited by 14 February 2027.",
     "Maps to Formato 2276 numeral 19 - NOT numeral 20. The second and third severance lines are "
     "TRANSPOSED between the two artefacts; map by meaning, never by position. Must reconcile to "
     "CO-CESANTIAS-006."),
    ("157.440.000", "Casilla 52 - Total ingresos brutos",
     "144,000,000 + 12,000,000 + 1,440,000 + 12,000,000, per the form's own 'Sume 36 a 51'.",
     "Compute from the ROUNDED casillas so the printed arithmetic holds."),

    "CONTRIBUTIONS AND WITHHOLDING",
    ("5.760.000", "Casilla 53 - Aportes obligatorios por salud",
     "Twelve months at COP 480,000 - the employee's 4%.",
     "Reconciles to twelve months of nomina electronica NIE163 and to the employee portion of PILA "
     "campo 55."),
    ("7.200.000", "Casilla 54 - Aportes obligatorios a pensiones y solidaridad pensional",
     "Twelve months at COP 480,000 pension plus COP 120,000 solidarity = COP 600,000 a month.",
     "ONE casilla for TWO concepts. The nomina electronica keeps them as NIE166 and NIE168, and "
     "PILA as campos 47, 51 and 52. Keep them separate internally and sum only here."),
    ("0", "Casillas 55 to 58", "No voluntary savings.",
     "Casillas 55 and 56 split what the nomina electronica carries in ONE element (NIE198); "
     "casilla 58 (AVC) has no nomina electronica element at all and must be tagged on the wage type."),
    ("13.120.000", "Casilla 59 - Ingreso laboral promedio de los ultimos seis meses",
     "The rolling six-month average of labour income, driven by the actual monthly payments "
     "including the December prima instalment.",
     "Below 350 UVT (COP 18,330,900), so the severance in casillas 47 and 49 is EXEMPT IN FULL "
     "under ET art. 206 num. 4. This is the field that cannot be reconstructed at year end - "
     "maintain it monthly."),
    ("7.404.000", "Casilla 60 - Valor de la retencion en la fuente",
     "The year's withholding: twelve ordinary months at COP 617,000 = 7,404,000, the prima having "
     "been withheld separately under ET art. 385 with its own table read and, on these figures, "
     "producing no additional withholding.",
     "Must reconcile to twelve months of nomina electronica NIE177 for this employee. The sum "
     "across all employees must reconcile to twelve months of Formulario 350 casilla 93."),

    "EMPLOYEE-DECLARED SECTIONS",
    ("0", "Casillas 61 to 78", "Not supplied by the employee.",
     "Payroll does NOT populate these. They exist so the certificate can substitute for the "
     "income-tax return under ET art. 380; left at zero, the employee simply cannot rely on the "
     "substitution."),
    ("7.404.000", "Casilla 75 - Total retenciones ano gravable", "Casilla 60 + casilla 74 (nil).",
     "-"),
    ("(unsigned)", "Certificacion ET art. 380",
     "Six declarations on gross wealth below 4,500 UVT, gross income and consumption below 1,400 "
     "UVT, and non-VAT-responsible status.",
     "DISPLAY-ONLY on the form. Where all six hold and the employee signs, the certificate "
     "substitutes for the income-tax return 'para todos los efectos legales'."),

    "NON-RESIDENT CONTRAST (v2.8 control B1)",
    ("157.440.000 / 31.488.000", "Casilla 52 / Casilla 60 for a NON-RESIDENT",
     "The same gross income, but withheld at the flat 20% of ET art. 408 = COP 31,488,000.",
     "Four and a quarter times the resident's COP 7,404,000. Casillas 53 and 54 still report the "
     "contributions actually deducted, but they did NOT reduce the base - art. 408 taxes the gross."),
    ("13.120.000", "Casilla 59 for a NON-RESIDENT", "Reported, but of no effect.",
     "The ET art. 206 num. 4 severance exemption belongs to the RESIDENT cedula-general regime and "
     "does not attach to a non-resident's flat withholding."),

    "CROSS-REPORT RECONCILIATION FROM THIS CERTIFICATE",
    ("7.404.000", "= 12 x nomina electronica NIE177", "Annual withholding for this employee.",
     "Reconcile on unrounded values with a tolerance - the two artefacts round differently."),
    ("12.000.000", "= CO-CESANTIAS-006 deposit", "Casilla 49 equals the fund deposit.",
     "Late deposit costs ONE DAY'S SALARY PER DAY OF DELAY, per employee, uncapped - so this "
     "reconciliation has a direct financial consequence."),
    ("(map by meaning)", "-> Formato 2276 numerals 18, 19, 20",
     "Casilla 47 to numeral 18, casilla 49 to numeral 19, casilla 48 to numeral 20.",
     "NOT positional. The second and third severance lines are transposed between the two artefacts."),
]

# ===========================================================================
#  SHEET 9 - SAMPLE FILE
# ===========================================================================
CFG["sample_title"] = "VERIFIED CHANNEL STATEMENT AND COMPLETED-CERTIFICATE RENDERING"
CFG["sample"] = r"""
WHY THERE IS NO SAMPLE FILE
===========================
Formulario 220 is NOT SUBMITTED TO ANY AUTHORITY. It is a certificate issued to
the employee and retained by the employer (ET arts. 378-380; DUR 1625 de 2016
art. 1.6.1.13.2.40). DIAN prescribes the FORM but no transmission format,
because nothing is transmitted.

There is therefore no wire format, no XSD and no import layout to sample.
Fabricating one would be inventing a format that does not exist. What follows
is a COMPLETED-CERTIFICATE RENDERING: the casilla-value set the engine must
produce, which is the actual deliverable.

Amounts are in Colombian pesos, approximated to the nearest 1,000, with ZERO
written where a casilla has no value - both rules stated expressly in the
instructivo.

-------------------------------------------------------------------------------
FORMULARIO 220 - CERTIFICADO DE INGRESOS Y RETENCIONES
POR RENTAS DE TRABAJO Y DE PENSIONES          Ano gravable: 2026
-------------------------------------------------------------------------------
  4  Numero de formulario ................................ 2026-000417
                                                           (assigned BY THE EMPLOYER)

  Informacion del agente retenedor
  5  Numero de Identificacion Tributaria (NIT) ........... 900123456
  6  DV .................................................. 7
  7  Primer apellido ..................................... (blank - legal person)
  8  Segundo apellido .................................... (blank - legal person)
  9  Primer nombre ....................................... (blank - legal person)
 10  Otros nombres ....................................... (blank - legal person)
 11  Razon social ........................................ MERCANS COLOMBIA S.A.S.

  Datos del trabajador o pensionado
 24  Tipo de documento ................................... 13  (Cedula de ciudadania)
 25  Numero de identificacion ............................ 1020304050
 26  Primer apellido ..................................... PEREZ
 27  Segundo apellido .................................... GOMEZ
 28  Primer nombre ....................................... JUAN
 29  Otros nombres ....................................... CARLOS

  Periodo de la certificacion
 30  DE .................................................. 2026 01 01
 31  A ................................................... 2026 12 31
 32  Fecha de expedicion ................................. 2027 03 31
 33  Lugar donde se practico la retencion ................ BOGOTA D.C.
 34  Cod. Dpto. .......................................... 11
 35  Cod. Ciudad/Municipio ............................... 001

  Concepto de los ingresos                                          Valor
 36  Pagos por salarios .................................. 144.000.000
 37  Pagos con bonos, cheques, tarjetas, vales, etc. .....           0
 38  Exceso de pagos por alimentacion > 41 UVT (art.387-1)           0
 39  Pagos por honorarios ................................           0
 40  Pagos por servicios .................................           0
 41  Pagos por comisiones ................................           0
 42  Pagos por prestaciones sociales .....................  12.000.000
 43  Pagos por viaticos ..................................           0
 44  Pagos por gastos de representacion ..................           0
 45  Compensaciones por trabajo asociado cooperativo .....           0
 46  Otros pagos .........................................           0
 47  Cesantia e intereses PAGADOS AL EMPLEADO ............   1.440.000
 48  Cesantia REGIMEN TRADICIONAL del CST ................           0
 49  Cesantia CONSIGNADA AL FONDO ........................  12.000.000
 50  Pensiones de jubilacion, vejez o invalidez ..........           0
 51  Apoyos economicos educativos con recursos publicos ..           0
 52  TOTAL INGRESOS BRUTOS (Sume 36 a 51) ............... 157.440.000

  Concepto de los aportes                                           Valor
 53  Aportes obligatorios por salud ......................   5.760.000
 54  Aportes obligatorios a pensiones Y SOLIDARIDAD ......   7.200.000
 55  Cotizaciones voluntarias RAIS .......................           0
 56  Aportes voluntarios a fondos de pensiones ...........           0
 57  Aportes a cuentas AFC ...............................           0
 58  Aportes a cuentas AVC ...............................           0
 59  Ingreso laboral promedio ultimos seis meses .........  13.120.000
 60  VALOR DE LA RETENCION EN LA FUENTE ..................   7.404.000

  Datos a cargo del trabajador o pensionado
      Concepto                          Valor recibido   Valor retenido
 61/68  Arrendamientos ......................... 0                 0
 62/69  Honorarios, comisiones y servicios ..... 0                 0
 63/70  Intereses y rendimientos financieros ... 0                 0
 64/71  Enajenacion de activos fijos ........... 0                 0
 65/72  Loterias, rifas, apuestas y similares .. 0                 0
 66/73  Otros .................................. 0                 0
 67/74  TOTALES ................................ 0                 0
 75  TOTAL RETENCIONES ANO GRAVABLE (Sume 60 + 74) ......   7.404.000

  Bienes poseidos a 31 de diciembre
 76  Identificacion de los bienes poseidos ............... (not supplied)
 77  Valor patrimonial ...................................           0
 78  Deudas vigentes a 31 de diciembre ...................           0

  Identificacion del dependiente economico (art. 387 par. 2 E.T.)
 79  Tipo documento ...................................... (none claimed)
 80  No. Documento ....................................... (none claimed)
 81  Apellidos y nombres ................................. (none claimed)
 82  Parentesco .......................................... (none claimed)

  Certifico que durante el ano gravable:                  [DISPLAY-ONLY]
   1. Mi patrimonio bruto no excedio de 4.500 UVT.
   2. Mis ingresos brutos fueron inferiores a 1.400 UVT.
   3. No fui responsable del impuesto sobre las ventas a 31 de diciembre.
   4. Mis consumos mediante tarjeta de credito no excedieron 1.400 UVT.
   5. El total de mis compras y consumos no supero 1.400 UVT.
   6. El total de mis consignaciones, depositos o inversiones no excedio 1.400 UVT.
                                        Firma del Trabajador o Pensionado: ______

  Nombre del pagador o agente retenedor: MERCANS COLOMBIA S.A.S.
                                        Firma: ______

-------------------------------------------------------------------------------
NON-RESIDENT VARIANT (v2.8 control B1)
-------------------------------------------------------------------------------
The same certificate for a NON-RESIDENT employee changes exactly one figure:

 52  TOTAL INGRESOS BRUTOS ............................... 157.440.000  (unchanged)
 53  Aportes obligatorios por salud ......................   5.760.000  (unchanged)
 54  Aportes obligatorios a pensiones y solidaridad ......   7.200.000  (unchanged)
 59  Ingreso laboral promedio ultimos seis meses .........  13.120.000  (no effect)
 60  VALOR DE LA RETENCION EN LA FUENTE ..................  31.488.000  <== 20% of GROSS

ET art. 408 taxes the GROSS at a flat 20%: 20% x 157,440,000 = 31,488,000. The
contributions in casillas 53 and 54 are still certified because they were still
deducted - but they did NOT reduce the withholding base. Casilla 59 is reported
for completeness and has no effect, because the art. 206 num. 4 severance
exemption belongs to the resident cedula-general regime.

An employee who ACQUIRES RESIDENCE mid-year receives ONE certificate; casilla 60
sums the 20% months and the art. 383 months, and the form has no field to
disclose the split. Retain the split internally for audit.

-------------------------------------------------------------------------------
MAPPING TO FORMATO 2276 - MAP BY MEANING, NOT BY POSITION
-------------------------------------------------------------------------------
  Form 220 casilla 36  ->  2276 numeral  5   Pagos por salarios
  Form 220 casilla 37  ->  2276 numeral  7   Bonos, cheques, tarjetas, vales
  Form 220 casilla 38  ->  2276 numeral  8   Exceso alimentacion > 41 UVT
  Form 220 casilla 39  ->  2276 numeral  9   Honorarios
  Form 220 casilla 40  ->  2276 numeral 10   Servicios
  Form 220 casilla 41  ->  2276 numeral 11   Comisiones
  Form 220 casilla 42  ->  2276 numeral 12   Prestaciones sociales
  Form 220 casilla 43  ->  2276 numeral 13   Viaticos
  Form 220 casilla 44  ->  2276 numeral 14   Gastos de representacion
  Form 220 casilla 45  ->  2276 numeral 15   Compensaciones trabajo asociado
  Form 220 casilla 46  ->  2276 numeral 17   Otros pagos
  Form 220 casilla 47  ->  2276 numeral 18   Cesantias PAGADAS al empleado
  Form 220 casilla 49  ->  2276 numeral 19   Cesantias CONSIGNADAS al fondo   <== NOT 20
  Form 220 casilla 48  ->  2276 numeral 20   Cesantias REGIMEN TRADICIONAL    <== NOT 19
  Form 220 casilla 50  ->  2276 numeral 21   Pensiones
  Form 220 casilla 51  ->  2276 numeral 16   Apoyos economicos educativos
  Form 220 casilla 52  ->  2276 numeral 22   Total ingresos brutos
  Form 220 casilla 53  ->  2276 numeral 23   Aportes obligatorios salud
  Form 220 casilla 54  ->  2276 numeral 24   Aportes obligatorios pension y FSP
  Form 220 casilla 55  ->  2276 numeral 25   Aportes voluntarios RAIS
  Form 220 casilla 56  ->  2276 numeral 26   Aportes voluntarios fondos pensiones
  Form 220 casilla 57  ->  2276 numeral 27   Aportes AFC
  Form 220 casilla 58  ->  2276 numeral 28   Aportes AVC
  Form 220 casilla 59  ->  2276 numeral 33   Ingreso laboral promedio 6 meses
  Form 220 casilla 60  ->  2276 numeral 29   Retenciones practicadas
  Form 220 casillas 79-82 -> 2276 numeral 34 Dependiente economico

THE TWO HIGHLIGHTED LINES ARE TRANSPOSED. A positional mapping - 47 to 18,
48 to 19, 49 to 20 - swaps the fund deposit and the traditional-regime amount
in the information return. There is also a Form 220 concept with NO 2276
counterpart in this list (the meal payments UP TO 41 UVT, which 2276 reports
separately at numeral 32 as informative and Form 220 does not report at all)
and a 2276 concept with no Form 220 counterpart (numeral 6, emolumentos
eclesiasticos, which Form 220 folds into casilla 39).
"""

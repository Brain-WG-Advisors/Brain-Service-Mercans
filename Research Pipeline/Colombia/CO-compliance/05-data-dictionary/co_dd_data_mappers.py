# -*- coding: utf-8 -*-
"""
Colombia Data Dictionary - Country Option Mappers (part 4).

Each mapper: (MapperName, Constraint/Notes, [(Code, Abbreviation, Local Name ES,
English Description), ...])

v2.4 rule C14 - OPTION MAPPER COMPLETENESS. Every code carries a code value, an
abbreviation, a local name and an English description; where a Spec field
references the mapper with Mandatory=C, the constraint is documented in the
Constraint / Notes column of the mapper block.

PRIVATE SECTOR FILTER. Civil servants, military and police, the self-insured,
cooperative members without a labour contract, domestic workers and persons on
unemployment benefit are EXCLUDED from every mapper. Where a published Colombian
catalogue carries such codes, the excluded codes are named in the Notes so the
dev team can reject them at validation rather than silently accept them.
"""

OPTION_MAPPERS = [

    # ---------------------------------------------------------------- IDs --
    ("Employee Document Type",
     "Referenced by Employee Document Type (Mandatory=Y on CO-DIAN-001 NIE044, CO-PILA-003 "
     "T2R2-003, CO-DIAN-004 casilla 24 and CO-CESANTIAS-006 T03). Scope "
     "option_mapper_scope.personal_id_type. TWO CODE SYSTEMS, ONE MASTER VALUE: DIAN artefacts use "
     "the numeric code in the Code column; PILA and the severance-savings deposit file use a "
     "SEPARATE two-letter catalogue, which now has its own mapper - see 'Employee Document Type "
     "(PILA / Cesantias)'. The letter equivalents are 11=RC, 12=TI, 13=CC, 21=TE, 22=CE, 41=PA and "
     "47=PE; codes 31, 42, 50 and 91 have no PILA equivalent, and PILA codes CD, SC and PT have no "
     "DIAN numeric equivalent. CONSTRAINTS: (a) a PEP number must be EXACTLY 15 digits (SOI hard "
     "rule); (b) where the Foreign National Not Liable to Pension flag is set, only CE, PA, CD, SC "
     "and PE are valid; (c) the Colombian Abroad flag may be used only with CC or TI; (d) CO-GAP-06 "
     "- no code exists for the PPT (Decreto 216 de 2021), 47 is the only proxy; (e) CO-GAP-07 - the "
     "nómina electrónica types the number as xsd:integer, so an alphanumeric passport cannot be "
     "schema-valid. Formulario 220 carries a NARROWER list (12, 13, 21, 22, 31, 41).",
     [
        ("11", "RC", "Registro civil de nacimiento",
         "Civil birth registration. Under-7s; never an employee, retained for beneficiary records."),
        ("12", "TI", "Tarjeta de identidad",
         "Identity card for a person aged 7 to 17. Authorised minors 15-17 may be employed; converts "
         "to a cédula de ciudadanía on majority, changing the composite key."),
        ("13", "CC", "Cédula de ciudadanía",
         "Colombian national identity card. The default for nationals aged 18 and over and the "
         "overwhelming majority of Colombian employees. Numeric, no check digit."),
        ("21", "TE", "Tarjeta de extranjería",
         "Foreigner's identity card for minors. Alphanumeric in practice - see the integer-typing trap."),
        ("22", "CE", "Cédula de extranjería",
         "Foreign resident's identity card, issued by Migración Colombia. Numeric, typically 6-7 digits."),
        ("31", "NIT", "NIT",
         "Tax identification number. Rare for an employee; used where the beneficiary is a legal person. "
         "Carries a separate verification digit."),
        ("41", "PA", "Pasaporte",
         "Passport. Alphanumeric - cannot satisfy the xsd:integer typing of the nómina electrónica "
         "worker document-number attribute (CO-GAP-07)."),
        ("42", "DIE", "Documento de identificación extranjero",
         "Foreign identity document. Alphanumeric."),
        ("47", "PEP", "PEP - Permiso Especial de Permanencia",
         "Special residence permit. 15 numeric digits, exactly. Used as the proxy for the PPT, which "
         "has no code of its own."),
        ("50", "NIT-EXT", "NIT de otro país",
         "Foreign tax identification number. Alphanumeric."),
        ("91", "NUIP", "NUIP",
         "Unique personal identification number. EMPLOYEE USE ONLY - this document type is not held "
         "in the DIAN tax-registry database."),
     ]),

    ("Employee Document Type (PILA / Cesantias)",
     "Referenced by Employee Document Type on the SOCIAL-SECURITY channel - CO-PILA-003 (T2R2-003 "
     "'Tipo documento del cotizante' and T2R2-074, Mandatory=Y/C) and CO-CESANTIAS-006 (T03, "
     "Mandatory=Y). SECOND CODE SYSTEM FOR ONE MASTER VALUE: the same Employee Document Type master "
     "field is emitted as the DIAN numeric code on DIAN artefacts and as the two-letter code below "
     "on PILA and the severance-savings deposit file. Source: PILA Anexo Tecnico 2 (AT2 version 09, "
     "16-09-2019), Registro Tipo 2 campo 3 - the eight values CC, CE, TI, PA, CD, SC, RC and PE, "
     "verbatim. CONSTRAINTS: (a) only PA and CD may be alphanumeric; TI, CC, SC, RC, CE and PE must "
     "be all digits; (b) a PE (PEP) number must be EXACTLY 15 digits (SOI hard rule); (c) where the "
     "Foreign National Not Liable to Pension flag is set only CE, PA, CD, SC and PE are valid; (d) "
     "the Colombian Abroad flag may be used only with CC or TI; (e) NI is an EMPLOYER document type "
     "and is NOT valid for a contributor; (f) for a legal representative only CC, CE, PA and CD are "
     "available - see 'Legal Representative Document Type'. CO-GAP-06 remains open: PT exists in "
     "the cesantias XLS layout but not in the DIAN numeric catalogue, where 47 (PEP) is the only "
     "proxy.",
     [
        ("CC", "13", "Cedula de ciudadania",
         "Colombian national identity card. DIAN numeric equivalent 13. The default for nationals "
         "aged 18 and over. Numeric only."),
        ("CE", "22", "Cedula de extranjeria",
         "Foreign resident's identity card issued by Migracion Colombia. DIAN numeric equivalent "
         "22. Numeric only."),
        ("TI", "12", "Tarjeta de identidad",
         "Identity card for a person aged 7 to 17. DIAN numeric equivalent 12. Numeric only. "
         "Converts to CC on majority, changing the composite key - notify the fund or the deposit "
         "lands on an orphan account."),
        ("PA", "41", "Pasaporte",
         "Passport. DIAN numeric equivalent 41. ALPHANUMERIC permitted on PILA - and this is the "
         "channel difference behind CO-GAP-07, because the nomina electronica types the number as "
         "xsd:integer."),
        ("CD", "-", "Carne diplomatico",
         "Diplomatic card. ALPHANUMERIC permitted. NO DIAN numeric equivalent exists - the "
         "nomina electronica cannot carry this document type at all."),
        ("SC", "-", "Salvoconducto de permanencia",
         "Safe-conduct of stay. Numeric only. NO DIAN numeric equivalent exists."),
        ("RC", "11", "Registro civil de nacimiento",
         "Civil birth registration. DIAN numeric equivalent 11. Valid in the CONTRIBUTOR list but "
         "NOT in the employer list; an under-7 is never an employee, so it is retained for "
         "beneficiary records only."),
        ("PE", "47", "Permiso Especial de Permanencia (PEP)",
         "Special residence permit. DIAN numeric equivalent 47 (abbreviated PEP in Anexo table "
         "5.2.1). Numeric only and EXACTLY 15 digits."),
        ("PT", "-", "Permiso por Proteccion Temporal (PPT)",
         "CESANTIAS XLS LAYOUT ONLY. Printed in the XLS document-type list of the severance-savings "
         "deposit manual; it is absent from the PILA fixed-width list of AT2 version 09 and has no "
         "DIAN numeric equivalent (CO-GAP-06). Do not emit it on PILA or on any DIAN artefact."),
     ]),

    ("Employer Document Type",
     "Referenced by Employer Document Type (Mandatory=Y, CO-PILA-003 A1-002 and T2R1-005). NOT "
     "used by Principal Contributor Document Type (T2R2-074), which takes the CONTRIBUTOR "
     "catalogue 'Employee Document Type (PILA / Cesantias)' - the two lists differ in exactly "
     "two places, this one carrying NI and lacking RC. CONSTRAINT: where "
     "Employer Person Type = N (natural) the type NI is NOT available; where Person Type = J only "
     "NI is used in practice. RC is available in the CONTRIBUTOR list but not in the employer list.",
     [
        ("NI", "NI", "Número de identificación tributaria",
         "The document type of a corporate employer. Requires Employer Person Type = J."),
        ("CC", "CC", "Cédula de ciudadanía", "Natural-person employer. Numeric only."),
        ("CE", "CE", "Cédula de extranjería", "Natural-person employer. Numeric only."),
        ("TI", "TI", "Tarjeta de identidad", "Natural-person employer. Numeric only."),
        ("PA", "PA", "Pasaporte", "Natural-person employer. Alphanumeric permitted."),
        ("CD", "CD", "Carné diplomático", "Natural-person employer. Alphanumeric permitted."),
        ("SC", "SC", "Salvoconducto de permanencia", "Natural-person employer. Numeric only."),
        ("PE", "PE", "Permiso Especial de Permanencia", "Natural-person employer. Numeric only."),
     ]),

    ("Legal Representative Document Type",
     "Referenced by Legal Representative Document Type (Mandatory=C, CO-PILA-003 A1-020). "
     "CONSTRAINT: mandatory where Employer Person Type = J; optional where Person Type = N. This "
     "list is NARROWER than the employer and contributor lists - NI, TI, SC, PE and RC are NOT "
     "available for a legal representative.",
     [
        ("CC", "CC", "Cédula de ciudadanía", "Numeric."),
        ("CE", "CE", "Cédula de extranjería", "Numeric."),
        ("PA", "PA", "Pasaporte", "Alphanumeric permitted."),
        ("CD", "CD", "Carné diplomático", "Alphanumeric permitted."),
     ]),

    ("Dependant Document Type",
     "Referenced by Dependant Document Type (Mandatory=C, CO-DIAN-004 casilla 79 and CO-DIAN-005 "
     "Formato 2276). CONSTRAINT: populated only where the employee claimed the ET art. 387 par. 2 "
     "dependants deduction during the period, and always as a bidirectional set with the "
     "dependant's document number, full name and relationship. This Formulario 220 list is "
     "NARROWER than the nómina electrónica list at Anexo table 5.2.1, which also carries 11, 42, "
     "47, 50 and 91.",
     [
        ("12", "TI", "Tarjeta de identidad", "Identity card for a dependant aged 7 to 17."),
        ("13", "CC", "Cédula de ciudadanía", "National identity card. The great majority of dependants."),
        ("21", "TE", "Tarjeta de extranjería", "Foreigner's identity card for a minor dependant."),
        ("22", "CE", "Cédula de extranjería", "Foreign resident's identity card."),
        ("31", "NIT", "NIT", "Where the dependant beneficiary is an entity - not an ordinary case."),
        ("41", "PA", "Pasaporte", "Passport."),
     ]),

    ("Gender",
     "Referenced by Gender (Optional). Not reported on any of the six in-scope statutory filings "
     "and not a calculation driver - Colombia varies no payroll rate, threshold or contribution by "
     "gender. Held for HR master data and affiliation paperwork only.",
     [
        ("M", "M", "Masculino", "Male"),
        ("F", "F", "Femenino", "Female"),
     ]),

    # ------------------------------------------------------ employment ----
    ("Contract Type",
     "Referenced by Contract Type (Mandatory=Y, CO-DIAN-001 NIE061, Anexo Técnico table 5.5.2). "
     "Scope option_mapper_scope.contract_type. All five values are private-sector employment "
     "contracts. Independent service contracts (contrato de prestación de servicios) are NOT a "
     "contract type - they are not employment and are out of scope.",
     [
        ("1", "FIJO", "Término fijo",
         "Fixed-term contract. Labour Code art. 46; maximum four years after Ley 2466 de 2025 art. 6."),
        ("2", "INDEF", "Término indefinido",
         "Indefinite-term contract - the legal default. Labour Code art. 47; Ley 2466 de 2025 art. 5."),
        ("3", "OBRA", "Obra o labor determinada",
         "Contract for a specific work or task. Labour Code art. 46."),
        ("4", "APREN", "Aprendizaje",
         "Apprenticeship. Ley 2466 de 2025 art. 21 recast this as a special fixed-term LABOUR "
         "contract, regulated by Decreto 0223 of 5 March 2026. PILA worker type 12 (lectiva) or "
         "19 (productiva)."),
        ("5", "PRACT", "Prácticas o pasantías",
         "Internship or practical placement. Reported where remunerated."),
     ]),

    ("Worker Type",
     "Referenced by Worker Type (Mandatory=Y, CO-DIAN-001 NIE041 table 5.5.3 and CO-PILA-003 "
     "T2R2-005). MAPPING TRAP: the nómina electrónica table carries only SIXTEEN values while the "
     "PILA tipo cotizante list carries more than forty - copying a PILA code straight into the XML "
     "is a documented failure. PRIVATE-SECTOR FILTER, excluded codes: 02 (servicio doméstico) and "
     "04 (madre comunitaria) - private but outside standard corporate payroll and descoped in "
     "scope_manifest; 18, 30, 47 and 58 - public sector; 31 - associated-work cooperative members "
     "without a labour contract; 20 - Ley 789 de 2002 students (planilla K); 40 (beneficiario de "
     "UPC adicional) - a health-coverage beneficiary of a contributor, not an employee, absent from "
     "table 5.5.3 altogether and excluded from the PILA header contributor count; and every "
     "independent-worker, pensioner-paid-by-fund, councillor, taxi-driver and UGPP code (03, 16, "
     "32-36, 42-45, 52, 53, 55, 57, 59-63). The nine codes retained here are a strict subset of "
     "Anexo Tecnico table 5.5.3, so every value is valid in both the nomina electronica XML and "
     "PILA.",
     [
        ("01", "DEP", "Dependiente",
         "Standard employee. THE DEFAULT for private corporate payroll."),
        ("12", "APR-L", "Aprendiz del SENA en etapa lectiva",
         "Apprentice, classroom phase. Reduced contribution scenario - health only in the lectiva phase."),
        ("19", "APR-P", "Aprendiz del SENA en etapa productiva",
         "Apprentice, productive phase. Full contribution scenario."),
        ("21", "EST-PG", "Estudiante de postgrado en salud",
         "Health postgraduate student contributing through the host institution."),
        ("22", "PROF", "Profesor de establecimiento particular",
         "Teacher at a private establishment - expressly a private-sector category."),
        ("23", "EST-RL", "Estudiante con aporte solo a riesgos laborales",
         "Student on placement contributing to occupational risk only. Pairs with contract type 5."),
        ("51", "PARC", "Trabajador de tiempo parcial",
         "Part-time worker under the special partial-time contribution regime of Ley 2466 de 2025 "
         "art. 34. Uses the hours-worked field instead of the one-minimum-wage base floor."),
        ("54", "PREP", "Prepensionado de entidad en liquidación",
         "Pre-pensioner of an entity in liquidation. Pairs with planilla type X."),
        ("56", "PREP-V", "Prepensionado con aporte voluntario a salud",
         "Pre-pensioner making a voluntary health contribution."),
     ]),

    ("Worker Sub-Type",
     "Referenced by Worker Sub-Type (Mandatory=Y, CO-DIAN-001 NIE042 table 5.5.4 and CO-PILA-003 "
     "T2R2-006). HARD RULE (PILA Anexo Tecnico 2): where the sub-type is 1, 2, 3, 4, 5, 6, 9 or 12 "
     "the PILA pension-contribution rate field T2R2-046 MUST be 0; of those, 01, 03, 04, 05, 06 and "
     "09 are in scope here and 02 and 12 are excluded populations. CODE WIDTH TRAP: PILA writes the "
     "sub-type as a single digit (0, 1, 3...) while the nomina electronica table 5.5.4 writes two "
     "(00, 01); the master value is stored zero-filled to two positions and narrowed on output. "
     "MAPPING TRAP: the nómina electrónica table carries ONLY 00 and 01; PILA carries the wider "
     "list. This field, not a separate flag, carries the 'employed active pensioner' attribute. "
     "PRIVATE-SECTOR FILTER, excluded codes: 02 (independiente pensionado activo), 10 (residente en "
     "el exterior afiliado voluntario) and 11/12 (conductores de taxi) - all self-insured or "
     "non-employee categories.",
     [
        ("00", "NA", "No aplica",
         "No sub-type applies. The value for almost every employee."),
        ("01", "PEN-DEP", "Dependiente pensionado por vejez, jubilación o invalidez activo",
         "Employed old-age, retirement or disability pensioner in active service. NO pension "
         "contribution; health and the payroll levies still apply. The only sub-type with a nómina "
         "electrónica equivalent."),
        ("03", "EDAD", "Cotizante no obligado a cotizar a pensiones por edad",
         "Employee not obliged to contribute to pension by reason of age. Pension rate must be 0."),
        ("04", "REQ", "Cotizante con requisitos cumplidos para pensión",
         "Employee who has met the pension requirements. Pension rate must be 0."),
        ("05", "IND-SUST", "Cotizante con indemnización sustitutiva o devolución de saldos reconocida",
         "Employee granted a substitute indemnity or return of balances. Pension rate must be 0."),
        ("06", "EXCEP", "Cotizante de régimen exceptuado de pensiones",
         "Employee under a pension regime excepted from the general system. Pension rate must be 0."),
        ("09", "MESADA", "Pensionado con mesada igual o superior a 25 SMLMV",
         "Pensioner whose pension equals or exceeds 25 minimum wages. Pension rate must be 0."),
     ]),

    ("Pay Frequency",
     "Referenced by Pay Frequency (Mandatory=Y, CO-DIAN-001 NIE029, Anexo Técnico table 5.5.1). "
     "Labour Code art. 134 caps the interval at one month for monthly salaries and one week for day "
     "wages; any shorter frequency is permitted. CRITICAL: whatever the value, the electronic "
     "payroll support document is ONE MONTHLY document per employee (Res. DIAN 000013 de 2021 art. "
     "3) - a semi-monthly payroll does NOT produce two filings a month.",
     [
        ("1", "SEM", "Semanal", "Weekly."),
        ("2", "DEC", "Decenal", "Every ten days."),
        ("3", "CAT", "Catorcenal", "Every fourteen days."),
        ("4", "QUI", "Quincenal",
         "Semi-monthly - the most common Colombian cycle. Still one monthly document, carrying two "
         "payment-date occurrences."),
        ("5", "MEN", "Mensual", "Monthly."),
        ("6", "OTR", "Otro", "Any other cycle."),
     ]),

    ("Payment Form",
     "Referenced by Payment Form (Mandatory=Y, CO-DIAN-001 NIE064, Anexo Técnico table 5.3.3.1). "
     "The annex publishes a single value. Distinct from Payment Method: 'forma' is the settlement "
     "form, 'método' is the medium.",
     [
        ("1", "CONT", "Contado", "Cash / immediate settlement. The only published value."),
     ]),

    ("Payment Method",
     "Referenced by Payment Method (Mandatory=Y, CO-DIAN-001 NIE065, Anexo Técnico table 5.3.3.2). "
     "CONSTRAINT: bidirectional set with the three bank fields - where the value is 10 (efectivo) "
     "the bank name, account type and account number attributes MUST BE ABSENT; for every "
     "bank-mediated medium all three are required. The complete UN/EDIFACT 4461 catalogue (codes 1 "
     "to 97) is printed at Anexo table 5.3.3.2; the values below are those used in payroll.",
     [
        ("10", "EFEC", "Efectivo",
         "Cash. The bank attributes must be absent."),
        ("20", "CHEQ", "Cheque", "Cheque."),
        ("42", "CONS", "Consignación bancaria",
         "Bank deposit. The most common Colombian payroll method."),
        ("45", "TCB", "Transferencia crédito bancario", "Bank credit transfer."),
        ("47", "TDB", "Transferencia débito bancaria", "Bank debit transfer."),
        ("48", "TCRE", "Tarjeta crédito", "Credit card."),
        ("49", "TDEB", "Tarjeta débito", "Debit card."),
        ("71", "BON", "Bonos",
         "Vouchers. Where salary is paid in vouchers the amount also belongs in the BonoEPCTV "
         "devengado elements of the XML."),
        ("72", "VAL", "Vales", "Vales / meal tickets."),
     ]),

    ("Bank Account Type",
     "Referenced by Employee Bank Account Type (Mandatory=C, CO-DIAN-001 NIE067). CONSTRAINT: "
     "populated together with Employee Bank Name and Employee Bank Account Number whenever Payment "
     "Method is a bank-mediated medium; absent for a cash payment. Colombia has only these two "
     "account types and does NOT use IBAN.",
     [
        ("AHORROS", "AHO", "Cuenta de ahorros", "Savings account."),
        ("CORRIENTE", "CTE", "Cuenta corriente", "Current account."),
     ]),

    ("Work Modality",
     "Referenced by Work Modality (Mandatory=C). Legal basis: Ley 1221 de 2008 as amended by Ley "
     "2466 de 2025 arts. 52-54; CCG Module 4. CONSTRAINT: mandatory where the employee is a "
     "teleworker; defaults to PRES otherwise. Calculation-driving - a teleworker earning less than "
     "two minimum wages receives the MANDATORY connectivity allowance IN PLACE OF the transport "
     "allowance, and the two are NEVER paid together.",
     [
        ("PRES", "PRES", "Trabajo presencial", "On-site work. The default."),
        ("TT-AUT", "AUT", "Teletrabajo autónomo",
         "Autonomous telework - the employee works wholly outside the employer's premises."),
        ("TT-MOV", "MOV", "Teletrabajo móvil",
         "Mobile telework - the employee has no fixed workplace and relies on mobile devices."),
        ("TT-SUP", "SUP", "Teletrabajo suplementario",
         "Supplementary telework - the employee alternates between the employer's premises and a "
         "remote location."),
     ]),

    # ------------------------------------------------------------- tax ----
    ("Tax Residence Status",
     "Referenced by Tax Residence Status (Mandatory). THE SINGLE MOST CONSEQUENTIAL WITHHOLDING "
     "SWITCH IN COLOMBIAN PAYROLL. Tax Code art. 10 residence tests; DIAN Concepto 011108 of 29 "
     "June 2026. The switch is PROSPECTIVE, never retroactive - acquiring residence does not "
     "reopen earlier months. Independent of Nationality: a Colombian national can be a "
     "non-resident and a foreign national can be a resident.",
     [
        ("RES", "RES", "Residente fiscal",
         "Colombian tax resident. Withheld on the progressive art. 383 table (0/19/28/33/35/37/39%) "
         "applied to the art. 388 depurated base, by Procedure 1 or Procedure 2."),
        ("NRES", "NRES", "No residente fiscal",
         "Non-resident. Withheld at a FLAT 20% under art. 408 on the GROSS payment: no art. 388 "
         "depuration, no 25% exempt income, no art. 387 deductions, no tax-free band and no "
         "procedure election."),
     ]),

    ("Withholding Procedure",
     "Referenced by Withholding Procedure (Mandatory). Employer election made PER EMPLOYEE; once "
     "elected, Procedure 2 binds for the whole six-month semester. CONSTRAINT: not applicable to a "
     "non-resident, who is withheld at the flat art. 408 rate with no procedure. The fixed "
     "percentage produced by the June/December recalculation is a CALCULATED value (WTC), not "
     "master data.",
     [
        ("1", "P1", "Procedimiento 1",
         "Tax Code art. 385. Each month stands alone; the statutory minimum service bonus is "
         "withheld separately on its own read of the art. 383 table. A sub-30-day period is grossed "
         "to 30 days."),
        ("2", "P2", "Procedimiento 2",
         "Tax Code art. 386. A fixed percentage recomputed each June and December from the "
         "preceding 12 months; the service bonus sits inside the ordinary base and is NOT given a "
         "separate table read."),
     ]),

    ("Treaty Status",
     "Referenced by Treaty Status (Mandatory=C, CO-DIAN-002 casilla 141). CONSTRAINT: required on "
     "every Formulario 350 annex row, i.e. wherever a payment is made to a non-resident; not "
     "applicable to a resident employee. Where the value is CON CONVENIO the treaty country must be "
     "one with a treaty in force.",
     [
        ("SIN CONVENIO", "SC", "Países sin convenio",
         "No double-tax treaty in force. Payment-concept list 1 to 18; the employee concept is 5 "
         "(prestación de servicios y compensación por servicios personales) at the 20% general rate "
         "of ET art. 408."),
        ("CON CONVENIO", "CC", "Países con convenio vigente",
         "A double-tax treaty is in force. Payment-concept list 19 to 33; the employee concept is 24 "
         "(rentas de trabajo) and the rate comes from the applicable treaty, which may be lower "
         "than 20% or nil."),
     ]),

    ("Dependant Relationship",
     "Referenced by Dependant Relationship (Mandatory=C, CO-DIAN-004 casilla 82 and CO-DIAN-005). "
     "CONSTRAINT: populated as a bidirectional set with the dependant's document type, document "
     "number and full name - all four together or none. The five limbs of ET art. 387 par. 2 are "
     "EXHAUSTIVE: a person outside them is not a dependant however genuine the support. Formulario "
     "220 casilla 82 accepts free text, so the engine emits the Local Name; the Code column is the "
     "Mercans-internal normalisation. Qualifying evidence must be retained.",
     [
        ("HIJO-M18", "H18", "Hijo o hija menor de 18 años",
         "Child under 18. No further condition."),
        ("HIJO-EST", "HED", "Hijo o hija entre 18 y 23 años en formación",
         "Child aged 18 to 23 whose education the taxpayer finances at a recognised institution."),
        ("HIJO-DEP", "HDP", "Hijo o hija mayor de 23 años en situación de dependencia certificada",
         "Child over 23 with certified physical or psychological dependency."),
        ("CONYUGE", "CON", "Cónyuge o compañero permanente en situación de dependencia",
         "Spouse or permanent partner in a certified state of dependency by absence of income or by "
         "physical or psychological condition."),
        ("ASCEND-HERM", "APH", "Padres y hermanos en situación de dependencia",
         "Parents and siblings in a certified state of dependency."),
     ]),

    # -------------------------------------------------- social security ----
    ("Pension Regime",
     "Referenced by Pension Regime (Mandatory). CCG Module 5. Employee election that survives a "
     "change of employer and must be declared by a new joiner. Determines which administrator "
     "catalogue the AFP code is drawn from and which voluntary-contribution route is available. The "
     "CONTRIBUTION RATES are identical across the two regimes and are parameters (WTC).",
     [
        ("RPM", "RPM", "Régimen de Prima Media con Prestación Definida",
         "Public defined-benefit, pay-as-you-go regime administered by Colpensiones. Additional "
         "voluntary contributions are contributions, not a tax relief."),
        ("RAIS", "RAIS", "Régimen de Ahorro Individual con Solidaridad",
         "Private funded individual-account regime administered by the pension administrators. "
         "Voluntary contributions to the individual account are non-taxable income under ET art. 55 "
         "within the statutory caps."),
     ]),

    ("Severance-Savings Fund",
     "Referenced by Severance-Savings Fund Code (Mandatory=Y, CO-CESANTIAS-006 T09) and by "
     "Single-Fund Planilla Severance Fund Code (Mandatory=C). CONSTRAINT: the per-employee value is "
     "IGNORED where the employer files a single-fund planilla (E07 = Y), in which case the "
     "planilla-level fund overwrites every record. Codes are validated against the registered list "
     "of severance-savings funds - ANY OTHER VALUE IS REJECTED. Misdirecting a deposit costs one "
     "day's salary per day of delay, per employee, uncapped (Ley 50 de 1990 art. 99 num. 3).",
     [
        ("02", "PROTECCION", "Fondo de Cesantías Protección (Protección S.A.)",
         "Private severance-savings fund administered by Protección S.A."),
        ("03", "PORVENIR", "Porvenir Cesantías (Porvenir S.A.)",
         "Private severance-savings fund administered by Porvenir S.A., the largest by affiliates."),
        ("10", "COLFONDOS", "Colfondos Cesantías (Colfondos S.A. Pensiones y Cesantías)",
         "Private severance-savings fund administered by Colfondos S.A."),
        ("15", "FNA", "Fondo Nacional del Ahorro (FNA)",
         "The state-owned fund, an Empresa Industrial y Comercial del Estado. IN SCOPE despite being "
         "state-owned: it is an EMPLOYEE election open to private-sector employees, not a "
         "public-sector employment category."),
        ("19", "SKANDIA", "Skandia (etiqueta publicada: 'Old Mutual (antes Skandia)')",
         "STALE LABEL, LIVE CODE. The published layout prints 'Old Mutual (Antes Skandia)' but the "
         "administrator trades as Skandia. Use the code, not the printed label."),
     ]),

    ("Severance-Savings Regime",
     "Referenced by Severance-Savings Regime (Mandatory). REPORTING TRAP: Formulario 220 reports "
     "the pre-1991 traditional regime at casilla 48 and the amount deposited to the fund at casilla "
     "49, while Formato 2276 reports them in the OPPOSITE order at numerals N19 (fund) and N20 "
     "(traditional). MAP BY MEANING, NEVER BY POSITION.",
     [
        ("LEY50", "L50", "Régimen de Ley 50 de 1990 - consignación anual",
         "The annual-deposit regime. The default for everyone hired from 1 January 1991. Deposited "
         "to the employee's chosen fund by 14 February. Reported at Formulario 220 casilla 49 and "
         "Formato 2276 numeral N19."),
        ("TRADICIONAL", "TRAD", "Régimen tradicional retroactivo del CST (anterior a 1991)",
         "The pre-1991 retroactive regime, for employees hired before 1 January 1991 who did not "
         "switch. Reported at Formulario 220 casilla 48 and Formato 2276 numeral N20."),
        ("INTEGRAL", "INT", "Salario integral - sin cesantías",
         "All-inclusive salary under Labour Code art. 132 num. 2: severance savings, severance "
         "interest and the service bonus are already inside the salary, so no separate accrual and "
         "no deposit arise."),
     ]),

    ("Severance-Savings Deposit Arrangement",
     "Referenced by Severance-Savings Deposit Arrangement (Mandatory=C). CONSTRAINT: the value "
     "MENSUAL is the one that maps to Y in the spec field Contract.Cesantias_Regime "
     "(CO-CESANTIAS-006 MA01) and it GATES the monthly-advance fields MA02 to MA05 - where the "
     "value is anything else, those fields are not produced and the ordinary annual detail record "
     "is the only route. MENSUAL and DIRECTO each require a WRITTEN agreement on file.",
     [
        ("ANUAL", "ANU", "Consignación anual al fondo de cesantías",
         "The ordinary route: liquidation at 31 December, deposit to the employee's chosen fund by "
         "14 February. Ley 50 de 1990 art. 99 nums. 1-3."),
        ("MENSUAL", "MEN", "Consignación mensual anticipada del 8,33%",
         "Monthly advance deposit of 8.33% plus monthly payment of the 1% interest, by written "
         "agreement. Ley 2466 de 2025 art. 64, adding two paragraphs to Ley 50 de 1990 art. 99."),
        ("DIRECTO", "DIR", "Pago directo al trabajador (liberatorio)",
         "Direct payment to the employee discharging the deposit obligation. Labour Code art. 57 "
         "par. 4, added by Ley 2466 de 2025 art. 15. No planilla record and no penalty, but the "
         "evidence must be retained; fund affiliation remains compulsory."),
        ("NA", "NA", "No aplica",
         "All-inclusive salary, a leaver settled in the final settlement, or the pre-1991 "
         "retroactive regime."),
     ]),

    ("Occupational Risk Class",
     "Referenced by Work Centre Occupational Risk Class (Mandatory=Y, CO-PILA-003 T2R2-078). THE "
     "CLASS ATTACHES TO THE WORK CENTRE, NOT TO THE COMPANY (Decreto 1072 de 2015 art. "
     "2.2.4.2.5.6): a company with a corporate office and a plant legitimately carries two classes "
     "and two rates, and each employee follows the class of the centre where they work. "
     "Bidirectional set with Work Centre Code and the VCT change-of-work-centre event. THE RATES "
     "BELOW ARE SHOWN FOR ORIENTATION ONLY - they are parameters held in the WTC, not master data.",
     [
        ("I", "I", "Riesgo mínimo",
         "Initial rate 0.522%; permitted range 0.348% to 0.696%. Offices, financial services, commerce."),
        ("II", "II", "Riesgo bajo",
         "Initial rate 1.044%; permitted range 0.435% to 1.653%. Light manufacturing, textiles."),
        ("III", "III", "Riesgo medio",
         "Initial rate 2.436%; permitted range 0.783% to 4.089%. Heavier manufacturing, food processing."),
        ("IV", "IV", "Riesgo alto",
         "Initial rate 4.350%. RECORDED DEFECT: Decreto 1072 de 2015 art. 2.2.4.3.5 prints the class "
         "IV initial rate inconsistently - see the CO-PILA-003 Field Options note."),
        ("V", "V", "Riesgo máximo",
         "Initial rate 6.960%; global maximum 8.700%."),
     ]),

    ("Social Security Subsystem",
     "Reference mapper for the eight contribution subsystems that the employer settles through the "
     "integrated contribution return. Referenced indirectly by the fund-code fields (EPS, AFP, CCF, "
     "ARL) and by the art. 114-1 exoneration flag. Scope option_mapper_scope.insurance_type. THE "
     "RATES, BASES AND CEILINGS ARE PARAMETERS HELD IN THE WTC, NOT MASTER DATA - they appear here "
     "only to identify the subsystem unambiguously.",
     [
        ("SALUD", "SAL", "Salud",
         "Health. Employee 4% / employer 8.5%; base capped at 25 minimum wages. The EMPLOYER limb is "
         "exonerable under ET art. 114-1 below a 10-minimum-wage base."),
        ("PENSION", "PEN", "Pensión",
         "Pension. Employee 4% / employer 12%; base capped at 25 minimum wages and floored at 1. "
         "NEVER exonerable."),
        ("FSP-SOL", "FSPS", "Fondo de Solidaridad Pensional - subcuenta de solidaridad",
         "Employee-borne 1%, from a contribution base of 4 minimum wages."),
        ("FSP-SUB", "FSPU", "Fondo de Solidaridad Pensional - subcuenta de subsistencia",
         "Employee-borne, banded 0.2% to 1.0%, from a contribution base of 16 minimum wages."),
        ("ARL", "ARL", "Riesgos laborales",
         "Occupational risk. EMPLOYER ONLY, by risk class of the WORK CENTRE; global bounds 0.348% "
         "to 8.700%. Never exonerable."),
        ("CCF", "CCF", "Caja de compensación familiar",
         "Family compensation fund. Employer 4% on the payroll-levy base, no ceiling. NEVER "
         "exonerable under art. 114-1."),
        ("SENA", "SENA", "Servicio Nacional de Aprendizaje",
         "Training levy. Employer 2% on the payroll-levy base, no ceiling. Exonerable under art. 114-1."),
        ("ICBF", "ICBF", "Instituto Colombiano de Bienestar Familiar",
         "Family-welfare levy. Employer 3% on the payroll-levy base, no ceiling. Exonerable under "
         "art. 114-1."),
     ]),

    ("PILA Novedad (Change Event) Type",
     "Reference mapper for the change events reported per contributor on the integrated "
     "contribution return. Scope option_mapper_scope.benefit_type. THESE ARE TRANSACTIONAL "
     "PER-PAYRUN VALUES, NOT MASTER DATA - the mapper is documented here because each event GATES "
     "the conditionality of a master-data field, as recorded in the Pre-Condition column: ING -> "
     "Hire Date; RET -> Termination Date; TAE -> EPS Transfer Code; TAP -> AFP Transfer Code; VCT "
     "-> Work Centre Code. The DAY COUNTS and AMOUNTS the events carry are payroll inputs and "
     "calculated values (WTC).",
     [
        ("ING", "ING", "Ingreso",
         "Hire. Makes the hire-date field mandatory."),
        ("RET", "RET", "Retiro",
         "Termination. Makes the termination-date field mandatory."),
        ("TDE", "TDE", "Traslado desde otra EPS o EOC",
         "Transfer FROM another health insurer."),
        ("TAE", "TAE", "Traslado a otra EPS o EOC",
         "Transfer TO another health insurer. Makes the EPS transfer code mandatory."),
        ("TDP", "TDP", "Traslado desde otra administradora de pensiones",
         "Transfer FROM another pension administrator."),
        ("TAP", "TAP", "Traslado a otra administradora de pensiones",
         "Transfer TO another pension administrator. Makes the AFP transfer code mandatory."),
        ("VSP", "VSP", "Variación permanente de salario",
         "Permanent salary variation. Makes the new-salary field mandatory."),
        ("VST", "VST", "Variación transitoria del salario",
         "One-off transitory variation of the contribution base."),
        ("SLN", "SLN", "Suspensión temporal del contrato o licencia no remunerada",
         "Contract suspension or unpaid leave. Health moves to 8.5% or 0%, pension to 12% or 16%, "
         "and the payroll levies to 0%. Makes the from/to date fields mandatory."),
        ("IGE", "IGE", "Incapacidad temporal por enfermedad general",
         "General sickness absence. The employer bears days 1-2 (Decreto 780 de 2016 art. 3.2.1.10); "
         "the health insurer funds from day 3."),
        ("LMA", "LMA", "Licencia de maternidad o paternidad",
         "Maternity or paternity leave. Benefit funded by the health insurer; record-only for the "
         "employer."),
        ("VAC", "VAC", "Vacaciones",
         "Annual leave. Carried in a THREE-VALUE flag shared with paid leave - value X."),
        ("LR", "LR", "Licencia remunerada",
         "Other paid leave. The same flag as vacaciones - value L. The two map to DIFFERENT nómina "
         "electrónica blocks and must not be merged."),
        ("IRL", "IRL", "Incapacidad por accidente de trabajo o enfermedad laboral",
         "Occupational accident or disease absence. NOT a flag - a DAY COUNT from 00 to 30. Funded "
         "by the occupational-risk insurer from day one at 100%."),
        ("AVP", "AVP", "Aporte voluntario a pensión",
         "Voluntary pension contribution reported in the period."),
        ("VCT", "VCT", "Variación de centro de trabajo",
         "Change of work centre. Makes the work-centre fields mandatory and may change the "
         "occupational-risk class and therefore the rate."),
        ("A", "CORR-A", "Corrección - adición de cotizante omitido",
         "Correction limb A: adds a contributor omitted from the original planilla. Meaningful only "
         "on planilla type N."),
        ("C", "CORR-C", "Corrección - corrección de cotizante reportado",
         "Correction limb C: corrects a contributor already reported. Paired with an A record; the "
         "sum of C bases and days must be greater than or equal to the sum of A."),
     ]),

    # ------------------------------------------------- employer profile ----
    ("Employer Person Type",
     "Referenced by Employer Person Type (Mandatory=Y, CO-PILA-003 A1-009). GATES a large "
     "conditional block: where J, the NIT verification digit and the whole legal-representative "
     "block (document type, number, DV and the four name fields) become mandatory; where N, the "
     "verification digit must be ZERO and the employer document type narrows to the "
     "natural-person list.",
     [
        ("J", "JUR", "Jurídica", "Legal person. The ordinary corporate employer."),
        ("N", "NAT", "Natural", "Natural person acting as employer."),
     ]),

    ("Employer Legal Nature",
     "Referenced by Employer Legal Nature (Mandatory=Y, CO-PILA-003 A1-008). PRIVATE-SECTOR "
     "FILTER: only value 2 is in scope. EXCLUDED codes and why: 1 Pública - public entity, separate "
     "legislation; 3 Mixta - mixed-capital entity, partly public; 4 Organismos multilaterales - "
     "multilateral organisation, aportante type 6 and out of scope; 5 Entidades de derecho público "
     "no sometidas a la legislación colombiana - typically a foreign mission, out of scope. An "
     "employer presenting any of these values must be rejected at validation, not silently "
     "processed.",
     [
        ("2", "PRIV", "Privada",
         "Private entity. THE IN-SCOPE POPULATION for the Mercans platform."),
     ]),

    ("Class of Contributor",
     "Referenced by Class of Contributor (Mandatory=Y, CO-PILA-003 A1-007). The headcount is "
     "counted across ALL branches and dependencies of the legal person, NOT per branch. CONSTRAINT: "
     "class D makes the commercial-registry date and the registered-seat department code mandatory "
     "and is normally accompanied by Ley 1429 CCF benefit = S. All four values are private-sector.",
     [
        ("A", "200+", "Aportante con 200 o más cotizantes",
         "Employer with 200 or more contributors, counted across all branches."),
        ("B", "<200", "Aportante con menos de 200 cotizantes",
         "Employer with fewer than 200 contributors. The default for most corporate employers."),
        ("C", "MIPYME", "Aportante Mipyme acogido a la Ley 590 de 2000",
         "Fewer than 200 contributors AND eligible for the SENA, ICBF and family-compensation-fund "
         "discounts of Ley 590 de 2000."),
        ("D", "LEY1429", "Aportante beneficiario de la Ley 1429 de 2010",
         "Beneficiary of the formalisation and employment-generation regime, Decreto 1074 de 2015 "
         "art. 2.2.2.42.1. Requires the commercial-registry date."),
     ]),

    ("Contributor Type",
     "Referenced by Contributor Type (Mandatory=Y, CO-PILA-003 A1-030 and T2R1-021). PRIVATE-SECTOR "
     "FILTER: only value 1 is in scope. EXCLUDED codes and why: 2 Independiente - self-insured, "
     "contributes on 40% of fees and is not an employer filing; 3 Entidades o universidades "
     "públicas de regímenes especial y de excepción - public sector; 4 Agremiaciones, asociaciones "
     "o congregaciones religiosas; 5 Cooperativas y precooperativas de trabajo asociado - members "
     "without a labour contract; 6 Misiones diplomáticas, consulares o de organismos "
     "multilaterales; 7 Hogares de Bienestar; 8 Pagador de concejales y ediles; 9 Contrato "
     "sindical; 10 Programa de reincorporación; 11 Parafiscales del Magisterio; 12 Prestación "
     "humanitaria. None of these is a private-sector employment relationship settled through "
     "corporate payroll.",
     [
        ("1", "EMPL", "Empleador",
         "Employer. THE IN-SCOPE VALUE for private corporate payroll."),
     ]),

    ("Form of Presentation",
     "Referenced by Form of Presentation (Mandatory=Y, CO-PILA-003 A1-010). CONSTRAINT: "
     "bidirectional pair with Branch or Dependency Code and Branch or Dependency Name - where the "
     "value is U both MUST BE BLANK; where it is S both become required, and the Archivo Tipo 2 "
     "header values must equal the Archivo Tipo 1 values.",
     [
        ("U", "UNICO", "Único",
         "A single consolidated planilla for the whole legal person. Branch code and name blank."),
        ("S", "SUC", "Sucursal",
         "One planilla per branch. Branch code and name required."),
     ]),

    ("PILA Filing Modality",
     "Referenced by PILA Filing Modality (Mandatory). Employer-level election gated by headcount "
     "under Decreto 780 de 2016 art. 3.2.3.9 as substituted by Decreto 1990 de 2016; the headcount "
     "is aggregated across all branches under the same legal person. The THRESHOLD is a parameter "
     "(WTC); the elected modality is master data.",
     [
        ("1", "ELEC", "Electrónica",
         "Prepared and paid over the internet on the operador's site."),
        ("2", "ASIST", "Asistida",
         "The employer instructs the operador's call centre, which keys or digitises the information."),
     ]),

    ("PILA Planilla Type",
     "Referenced by PILA Planilla Type (Mandatory). Scope option_mapper_scope.correction_codes. The "
     "employer's DEFAULT is master data; the value used in a given run may be overridden by the "
     "event, and that override is TRANSACTIONAL. CONSTRAINT: planilla type N requires the "
     "associated planilla number and date, and its A/C record pairs must satisfy sum(C bases and "
     "days) >= sum(A). PRIVATE-SECTOR / SCOPE FILTER, excluded types: S (servicio doméstico), I and "
     "Y (independientes - contribute on 40% of fees, the payer is not an employer), T and F "
     "(Sistema General de Participaciones - public sector only), H (madres sustitutas), K "
     "(estudiantes Ley 789 de 2002), U and O (UGPP third-party and UGPP-determined liabilities).",
     [
        ("E", "EMPL", "Planilla empleados",
         "THE IN-SCOPE DEFAULT. Regular monthly payment for dependent contributors."),
        ("A", "ING", "Planilla cotizantes con novedad de ingreso",
         "New joiners omitted from the month's main planilla, settled separately with no late interest."),
        ("N", "CORR", "Planilla correcciones",
         "Correction of an earlier planilla - contribution base, rate, contributor type or sub-type, "
         "or an omitted change event - in paired A/C record groups."),
        ("M", "MORA", "Planilla mora",
         "Periods with a total absence of payment. The operador computes interest on arrears."),
        ("J", "JUD", "Planilla pago en cumplimiento de sentencia judicial",
         "Court-ordered settlement: reinstatement, contrato realidad, or reliquidation of salary "
         "factors omitted from the original liquidation."),
        ("X", "LIQ", "Planilla para el pago de empresa liquidada",
         "Liquidated company. Pairs with worker types 54 and 56."),
     ]),

    ("Employer Status Action Type",
     "Referenced by Employer Status Action Type (Mandatory=C, CO-PILA-003 A1-026). CONSTRAINT: "
     "optional in general, but where populated it makes the insolvency start date MANDATORY and the "
     "commercial-activity cessation date required - a bidirectional set of three fields.",
     [
        ("1", "CONC", "Concordato", "Insolvency arrangement."),
        ("2", "REEST", "Reestructuración", "Restructuring."),
        ("3", "LIQ", "Liquidación", "Liquidation."),
        ("4", "CESE", "Cese de actividades",
         "Cessation of activities. Fixes the date from which the employer is no longer obliged to "
         "contribute."),
     ]),

    ("Formato 2276 Informant Type",
     "Referenced by Formato 2276 Informant Type (Mandatory). Res. DIAN 000227 de 2025 par. 4. "
     "CONSTRAINT: where the value is 1, the trust identification (numeral 35) and the "
     "contract-participant numeral (36) 'no se deben diligenciar' - they are mutually exclusive "
     "with the ordinary-employer case. EXCLUDED values 2 to 8 (fiduciarias, mandatario o "
     "administrador delegado, consorcio o unión temporal, hidrocarburos, joint venture, cuentas en "
     "participación, convenios de cooperación con entidades públicas) attach to structures that are "
     "not ordinary employer payroll and each requires numeral 35 or 36.",
     [
        ("1", "GEN", "Informante general",
         "THE VALUE FOR AN ORDINARY EMPLOYER reporting payments for rentas de trabajo."),
     ]),

    ("Yes/No Indicator",
     "Generic two-value indicator referenced by every S/N master-data flag in this dictionary: "
     "Colombian Abroad Flag, All-Inclusive Salary Flag, Non-Salary Pact Flag, High-Risk Pension "
     "Activity Flag, Foreign National Not Liable to Pension Flag, Concurrent Employer Flag, "
     "36-Hour Shift System Flag, Disability Status, Art. 380 Non-Filer Declaration, Exonerated from "
     "Health/SENA/ICBF and Ley 1429 art. 5 CCF Benefit. EMISSION RULE: on the PILA fixed-width file "
     "several of these are emitted as BLANK or X rather than S or N - the fixed-width emission is a "
     "formatting concern, the stored master value is always S or N. CONSTRAINT on the exoneration "
     "flag: N is MANDATORY where the health contribution base reaches 10 minimum wages.",
     [
        ("S", "SI", "Sí", "Yes / the condition applies."),
        ("N", "NO", "No", "No / the condition does not apply."),
     ]),
]

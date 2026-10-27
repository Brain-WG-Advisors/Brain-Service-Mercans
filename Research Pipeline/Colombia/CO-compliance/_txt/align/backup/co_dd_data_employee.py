# -*- coding: utf-8 -*-
"""
Colombia Data Dictionary - EMPLOYEE-side field tables (part 1 of the data set).

Each tuple:
  (FieldName EN, Label local ES, Description, DataType M/CM/O, Pre-Condition,
   FieldType, Pre-Defined Format, Option Mapper, Additional Notes)

Scope discipline (CLAUDE.md): user-input MASTER DATA only. Calculated amounts,
statutory rates, ceilings, UVT/SMMLV parameters, authority-generated values and
per-payrun transactional data are excluded and land in the WTC / parameters /
system buckets. See CO-DD-001-classification.md.
"""

# ---------------------------------------------------------------------------
# SHEET 4 - ID Information : employee identity / payment identifiers
# ---------------------------------------------------------------------------
ID_EMPLOYEE = [
    ("Employee Document Type",
     "Tipo de documento de identificación del trabajador",
     "Coded identity-document type of the employee. Colombia issues NO separate social-security "
     "number: the document type plus the document number IS the composite key across the electronic "
     "payroll XML, the integrated contribution return (PILA), Formulario 220 and Formato 2276. The "
     "code system differs by artefact - DIAN filings use the numeric catalogue (13 = cédula de "
     "ciudadanía) while PILA and the severance-savings deposit file use the two-letter catalogue "
     "(CC). One master value; the engine emits the artefact's own code.",
     "M", "",
     "Text", "N(2) DIAN numeric catalogue; emitted as A(2) alpha on PILA and cesantías",
     "Employee Document Type",
     "Spec ref: Employee.Document_Type - CO-DIAN-001 (NIE044, table 5.2.1), CO-PILA-003 (T2R2-003), "
     "CO-DIAN-004 (casilla 24), CO-CESANTIAS-006 (T03); Mandatory=Y on all four. Scope "
     "option_mapper_scope.personal_id_type. Validates the length of the document NUMBER - a PEP must "
     "be exactly 15 digits (SOI hard rule). CO-GAP-06: no code exists for the PPT (Permiso por "
     "Protección Temporal, Decreto 216 de 2021); code 47 (PEP) is the only available proxy."),

    ("Employee Document Number",
     "Número de identificación del trabajador",
     "Identity-document number of the employee, without dots, hyphens, spaces or a verification "
     "digit. Primary per-employee key on every Colombian statutory filing and the social-security "
     "identifier.",
     "M", "",
     "Text", "Numeric, no separators (cédula 8-10 digits; PEP exactly 15). Alphanumeric only for "
             "passport (41), foreign identity document (42) and foreign tax number (50)",
     "",
     "Spec ref: Employee.Document_Number - CO-DIAN-001 (NIE045), CO-PILA-003 (T2R2-004, A(16) "
     "space-filled), CO-DIAN-004 (casilla 25), CO-CESANTIAS-006 (T04, N(16) zero-filled); "
     "Mandatory=Y on all four. CO-GAP-07 (SCHEMA TRAP): NIE045 is typed xsd:integer in the "
     "nómina electrónica XSD, so an alphanumeric passport number cannot be schema-valid. No "
     "official workaround published - carry as an open item."),

    ("Employee Bank Name",
     "Banco",
     "Name of the bank holding the employee's salary account. Reported on the electronic payroll "
     "support document whenever the payment medium is bank-mediated.",
     "CM",
     "Mandatory where Payment Method is a bank-mediated medium (42, 45, 47, 48, 49). Must be absent "
     "or empty where Payment Method = 10 (efectivo).",
     "Text", "Free text", "",
     "Spec ref: Employee.Bank_Name (CO-DIAN-001 NIE066, Mandatory=C). Bidirectional set with "
     "Payment Method, Bank Account Type and Bank Account Number."),

    ("Employee Bank Account Type",
     "Tipo de cuenta",
     "Type of the employee's salary bank account - savings or current. Colombia has only these two.",
     "CM",
     "Mandatory together with Employee Bank Name and Employee Bank Account Number where Payment "
     "Method is a bank-mediated medium.",
     "Text", "AHORROS / CORRIENTE", "Bank Account Type",
     "Spec ref: Employee.Bank_Account_Type (CO-DIAN-001 NIE067, Mandatory=C)."),

    ("Employee Bank Account Number",
     "Número de cuenta",
     "Employee salary account number. COLOMBIA DOES NOT USE IBAN. Domestic account numbers are "
     "numeric, of bank-specific length (commonly 10-17 digits), with no national check-digit "
     "standard.",
     "CM",
     "Mandatory together with Employee Bank Name and Employee Bank Account Type where Payment "
     "Method is a bank-mediated medium.",
     "Text", "Numeric, bank-specific length (commonly 10-17 digits). NOT an IBAN.", "",
     "Spec ref: Employee.Bank_Account_Number (CO-DIAN-001 NIE068, Mandatory=C). CCG Module 2.2 "
     "confirms no IBAN and no national check digit - do not apply an IBAN validator."),

    ("Employee Internal Code",
     "Código del trabajador",
     "Employer's own internal employee number. Optional on the electronic payroll support document; "
     "used by the employer to reconcile the document to its own personnel records.",
     "O", "",
     "Text", "Free text (employer-defined)", "",
     "Spec ref: Employee.Internal_Code (CO-DIAN-001 NIE047, Mandatory=N). Not the document number "
     "and not a substitute for it."),

    ("Severance-Savings Fund Account Number",
     "Número de cuenta del fondo de cesantías",
     "Account number held by the employee at the chosen severance-savings fund, used on the annual "
     "severance deposit file.",
     "CM",
     "Mandatory where the fund requires an account number on the deposit file; otherwise the "
     "employee is identified by document type plus document number validated against the Asofondos "
     "affiliate base.",
     "Text", "Fund-specific numeric/alphanumeric", "",
     "Declared in build_co_specs._DD_MASTER_MAPPINGS as Employee.Cesantias_Fund_Account but not "
     "carried as a positional field in the published Simple S.A. / SOI layout, which keys the "
     "record on document type + number. DERIVED - confirm per-fund requirement with RA."),
]

# ---------------------------------------------------------------------------
# SHEET 5 - Country Fields : employee master data
# ---------------------------------------------------------------------------

CF_EMPLOYEE_NAME = [
    ("Employee First Surname",
     "Primer apellido",
     "First (paternal) surname of the employee as registered with the civil authorities.",
     "M", "", "Text", "A(20) on PILA and cesantías; variable length on the DIAN artefacts", "",
     "Spec ref: Employee.First_Surname - CO-DIAN-001 (NIE048), CO-PILA-003 (T2R2-011), CO-DIAN-004 "
     "(casillas 26-29), CO-CESANTIAS-006 (T05); Mandatory=Y on all four. Validated as a SET with the "
     "other three name parts against the Asofondos affiliate base on the cesantías deposit."),

    ("Employee Second Surname",
     "Segundo apellido",
     "Second (maternal) surname of the employee.",
     "CM",
     "The nómina electrónica schema declares this a REQUIRED attribute even though many Colombians "
     "and virtually all foreign nationals have only one surname. Where the person has no second "
     "surname a placeholder must be emitted or schema validation fails. Space-filled on the PILA "
     "and cesantías fixed-width layouts.",
     "Text", "A(20) on PILA and cesantías; variable length on the DIAN artefacts", "",
     "Spec ref: Employee.Second_Surname - all four per-employee artefacts. SCHEMA TRAP recorded in "
     "CCG Module 2.2: no official guidance exists on the placeholder value. Carry as an open item "
     "and agree the placeholder with RA before go-live."),

    ("Employee First Name",
     "Primer nombre",
     "First given name of the employee.",
     "M", "", "Text", "A(20) on PILA and cesantías; variable length on the DIAN artefacts", "",
     "Spec ref: Employee.First_Name - CO-DIAN-001 (NIE050), CO-PILA-003 (T2R2-013), CO-DIAN-004, "
     "CO-CESANTIAS-006 (T07); Mandatory=Y on all four."),

    ("Employee Other Names",
     "Otros nombres",
     "Second and any further given names of the employee.",
     "CM",
     "Conditional on the person having a second or further given name; space-filled on the "
     "fixed-width layouts when absent.",
     "Text", "A(20) on PILA and cesantías; A(30) on the PILA employer block; variable on DIAN", "",
     "Spec ref: Employee.Other_Names - all four per-employee artefacts (Mandatory=C/N). PILA calls "
     "the field 'Segundo nombre'; the nómina electrónica calls it 'OtrosNombres' and accepts more "
     "than one given name in the single attribute."),

    ("Date of Birth",
     "Fecha de nacimiento",
     "Employee date of birth. Not reported on any of the six in-scope statutory filings, but held as "
     "onboarding master data because it drives the identity-document path: a worker aged 15-17 holds "
     "a tarjeta de identidad (code 12) which converts to a cédula de ciudadanía (code 13) on "
     "majority - a change of the document-type + number composite key that must be actioned.",
     "O", "", "Date", "AAAA-MM-DD", "",
     "Not filing-mandated on the in-scope returns. CCG Module 2.2 records the minor-to-adult "
     "document-type change. Retirement age (57 women / 62 men, public defined-benefit regime) "
     "affects entitlement, not the payroll rate - see CCG Module 5."),

    ("Gender",
     "Sexo",
     "Employee gender. Standard onboarding demographic; Colombia does not vary any payroll rate, "
     "threshold or contribution by gender.",
     "O", "", "Text", "M / F", "Gender",
     "Not reported on any of the six in-scope statutory filings and not a calculation driver. Held "
     "for HR master data and affiliation paperwork only."),

    ("Nationality",
     "Nacionalidad",
     "Employee nationality. Drives the identity-document path (Colombian national -> cédula de "
     "ciudadanía 13; resident foreign national -> cédula de extranjería 22; non-resident -> "
     "passport 41) and, together with proof of affiliation to a foreign pension system, the "
     "foreign-national pension-waiver flag.",
     "M", "", "Text", "ISO 3166-1 alpha-2 (e.g. CO)",
     "ISO 3166-1 (see the 'Country Codes - ISO 3166-1' sheet)",
     "Calculation-driving classifier. NOT the same question as Tax Residence Status: a Colombian "
     "national can be a non-resident and a foreign national can be a resident. Keep the two fields "
     "independent - see CCG Module 2.2 and the resident/non-resident matrix at Module 6.2."),
]

CF_EMPLOYEE_CONTACT = [
    ("Employee Residential Address",
     "Dirección de residencia del trabajador",
     "Residential address of the employee, as reported on the annual severance-savings deposit file.",
     "CM",
     "Mandatory on the annual severance-savings deposit record. Must be consistent with the "
     "residence department and municipality codes, which are the DANE halves of the same address.",
     "Text", "CHAR(50)", "",
     "Spec ref: Employee.Address (CO-CESANTIAS-006 T15, Mandatory=C). DISTINCT from Place of Work "
     "Address - the nómina electrónica reports where the employee WORKS, this reports where the "
     "employee LIVES. Do not map one to the other."),

    ("Residence Department Code",
     "Código del departamento de residencia",
     "Two-digit DANE DIVIPOLA department code of the employee's residential address.",
     "CM",
     "Mandatory wherever the residential address is reported. Must be the department half of the "
     "same five-digit DIVIPOLA code whose municipality half is the residence municipality code.",
     "Text", "N(2) DANE DIVIPOLA", "",
     "Spec ref: Employee.Department_Code (CO-CESANTIAS-006 T16, Mandatory=C). Use the DANE DIVIPOLA "
     "catalogue, NOT the ISO 3166-2:CO list on the reference sheets."),

    ("Residence Municipality Code",
     "Código del municipio de residencia",
     "Three-digit DANE DIVIPOLA municipality suffix of the employee's residential address.",
     "CM",
     "Mandatory wherever the residential address is reported. Must be the municipality half of the "
     "same five-digit DIVIPOLA code whose department half is the residence department code.",
     "Text", "N(3) DANE DIVIPOLA suffix (e.g. 001 for Bogotá D.C. within department 11)", "",
     "Spec ref: Employee.Municipality_Code (CO-CESANTIAS-006 T17, Mandatory=C). SPLIT-CODE TRAP: "
     "PILA, Formulario 220 and the cesantías file carry the department and municipality in SEPARATE "
     "2 + 3 fields, whereas the nómina electrónica carries ONE five-digit code (11001). Store the "
     "five digits once and split on output."),

    ("Employee E-mail Address",
     "Correo electrónico del trabajador",
     "Employee e-mail address, reported on the annual severance-savings deposit file and used for "
     "payslip and certificate delivery.",
     "CM", "Conditional on an e-mail address being held for the employee.",
     "Text", "CHAR(50)", "",
     "Spec ref: Employee.Email (CO-CESANTIAS-006 T18, Mandatory=C)."),

    ("Employee Landline Telephone",
     "Teléfono fijo del trabajador",
     "Seven-digit landline telephone number of the employee, as required by the severance-savings "
     "deposit layout.",
     "CM",
     "Conditional on a 7-digit landline being held; the layout is filled with spaces or zeros where "
     "only a mobile number exists.",
     "Text", "N(7)", "",
     "Spec ref: Employee.Phone (CO-CESANTIAS-006 T19, Mandatory=C). The layout has no mobile-number "
     "field - a mobile number cannot be substituted."),

    ("Colombian Abroad Flag",
     "Colombiano en el exterior",
     "Indicates that the employee is a Colombian national performing the work outside Colombia. "
     "Where set, the work-location department and municipality must be left BLANK on the "
     "contribution return.",
     "CM",
     "Usable ONLY where Employee Document Type is cédula de ciudadanía (13 / CC) or tarjeta de "
     "identidad (12 / TI). Where set, Place of Work Department Code and Place of Work Municipality "
     "Code must be blank.",
     "Text", "S / N (emitted as blank or X on the PILA fixed-width file)", "Yes/No Indicator",
     "Spec ref: Employee.Colombian_Abroad_Flag (CO-PILA-003 T2R2-008, Mandatory=C). Bidirectional "
     "set with Employee Document Type and the two work-location codes."),
]

CF_EMPLOYEE_WORKPLACE = [
    ("Place of Work Country Code",
     "País del lugar de trabajo",
     "Country in which the employee performs the work. A required attribute of the worker element on "
     "the electronic payroll support document.",
     "M", "", "Text", "ISO 3166-1 alpha-2 (Anexo Técnico table 5.4.1)",
     "ISO 3166-1 (see the 'Country Codes - ISO 3166-1' sheet)",
     "Spec ref: Employee.Work_Country_Code (CO-DIAN-001 NIE051, Mandatory=Y). For a transnational "
     "teleworker a Colombian contract remains governed by Colombian law and the ARL must guarantee "
     "cover in the country of performance - Ley 2466 de 2025 art. 54, CCG Module 11."),

    ("Place of Work Department Code",
     "Departamento del lugar de trabajo",
     "Two-digit DANE DIVIPOLA department code of the place where the employee performs the work.",
     "CM",
     "Mandatory on the nómina electrónica. Left BLANK on the contribution return where the "
     "Colombian Abroad Flag is set, and where Worker Type = 40 (beneficiario UPC adicional).",
     "Text", "N(2) DANE DIVIPOLA (Anexo Técnico table 5.4.2)", "",
     "Spec ref: Employee.Work_Department_Code (CO-DIAN-001 NIE052 Mandatory=Y; CO-PILA-003 T2R2-009 "
     "Mandatory=C). Bidirectional set with the Colombian Abroad Flag and Worker Type."),

    ("Place of Work Municipality Code",
     "Municipio del lugar de trabajo",
     "DANE DIVIPOLA municipality of the place where the employee performs the work.",
     "CM",
     "Mandatory on the nómina electrónica. Left BLANK on the contribution return in the same two "
     "cases as the work-location department code - Colombian Abroad Flag set, or Worker Type = 40.",
     "Text", "N(5) full DIVIPOLA on the nómina electrónica (11001); N(3) municipality suffix on PILA",
     "",
     "Spec ref: Employee.Work_Municipality_Code (CO-DIAN-001 NIE053; CO-PILA-003 T2R2-010). "
     "SPLIT-CODE TRAP - see Residence Municipality Code. Store five digits once and split on output."),

    ("Place of Work Address",
     "Dirección del lugar de trabajo",
     "Street address of the place where the employee performs the work. A required attribute of the "
     "worker element on the electronic payroll support document.",
     "M", "", "Text", "Free text", "",
     "Spec ref: Employee.Work_Address (CO-DIAN-001 NIE054, Mandatory=Y). DISTINCT from the "
     "employee's residential address."),

    ("Work Centre Code",
     "Centro de trabajo",
     "Employer-assigned code of the work centre to which the employee is attached. The occupational-"
     "risk CLASS attaches to the WORK CENTRE, not to the company, so this field selects the risk "
     "class - and therefore the occupational-risk rate - that applies to the employee.",
     "CM",
     "Mandatory where the employer operates more than one work centre, and mandatory where the VCT "
     "change-of-work-centre event is reported for the period.",
     "Text", "N(9) zero-filled to the left", "",
     "Spec ref: Employee.Work_Centre_Code (CO-PILA-003 T2R2-091, Mandatory=C). Bidirectional set "
     "with the VCT novedad and with the work centre's Occupational Risk Class. Legal basis: Decreto "
     "1072 de 2015 art. 2.2.4.2.5.6 - a company with a corporate office and a plant legitimately "
     "carries two different risk classes. The RATE itself is a parameter (WTC), not DD."),
]

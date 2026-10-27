# -*- coding: utf-8 -*-
"""
Colombia Data Dictionary - EMPLOYER / legal-entity master-data blocks (part 3).
"""

# ---------------------------------------------------------------------------
# SHEET 4 - ID Information : employer registration identifiers
# ---------------------------------------------------------------------------
ID_LEGAL_ENTITY = [
    ("Employer NIT",
     "NIT del empleador",
     "Tax identification number assigned by DIAN on registration in the Single Tax Registry (RUT). "
     "Primary employer key on every Colombian statutory artefact. Stored and transmitted WITHOUT "
     "dots, hyphens or the verification digit.",
     "M", "",
     "Text", "N(9) to N(10) - no dots, no hyphens, no verification digit", "",
     "Spec ref: Company.NIT - CO-DIAN-001 (NIE033, Mandatory=Y), CO-DIAN-002 (casilla 5, "
     "Mandatory=Y), CO-DIAN-004 (casilla 5, Mandatory=Y), CO-DIAN-005 (numeral ENV-01, "
     "Mandatory=Y). Validation rules NIE038 and NIE041 require the number 'sin guiones ni DV' in "
     "one attribute and the verification digit in another - an engine that concatenates them FAILS "
     "schema validation. The last digit(s) of the NIT also fix the filing deadline for Formulario "
     "350, PILA and the información exógena."),

    ("Employer NIT Verification Digit (DV)",
     "Dígito de verificación (DV) del NIT",
     "Single-digit verification digit of the employer NIT, computed by DIAN using a weighted "
     "modulus-11 algorithm. ALWAYS A SEPARATE FIELD from the NIT itself.",
     "M",
     "On the contribution return the value is mandatory where Employer Person Type = J (jurídica); "
     "for every other case the field must be ZERO.",
     "Text", "N(1), 0 to 9", "",
     "Spec ref: Company.NIT_DV - CO-DIAN-001 (NIE034, Mandatory=Y), CO-DIAN-002 (casilla 6, "
     "Mandatory=Y), CO-PILA-003 (A1-004 and T2R1-007, Mandatory=C/Y), CO-DIAN-004 (casilla 6, "
     "Mandatory=Y). Verified algorithm (CCG Module 2.1): weights "
     "[3,7,13,17,19,23,29,37,41,43,47,53,59,67,71] applied right to left, S = sum(digit_i x W_i), R "
     "= S mod 11, DV = R if R < 2 else 11 - R. Verified against NIT 902025831 -> DV 4 and NIT "
     "800197268 -> DV 4. Stored, not recomputed at runtime, but validated on entry."),

    ("Employer Document Type",
     "Tipo de documento del aportante",
     "Identity-document type of the employer on the integrated contribution return. A corporate "
     "employer is NI (número de identificación tributaria); a natural-person employer uses a "
     "personal document type.",
     "M", "",
     "Text", "A(2) - PILA employer document-type catalogue", "Employer Document Type",
     "Spec ref: Company.Document_Type - CO-PILA-003 (A1-002 and T2R1-005, Mandatory=Y) and "
     "CO-CESANTIAS-006 (E01, Mandatory=Y), the latter as the composite Company.Document_Type + "
     "Company.Document_Number ('Tipo y número de documento del aportante') on CO-CESANTIAS-006. "
     "Where Employer Person Type = N (natural) the type NI is NOT available. "
     "Company.Document_Number (CO-PILA-003 A1-003 and T2R1-006, A(16)) is NOT a separate "
     "master-data field: for a legal person it is the Employer NIT and for a natural person it is "
     "the personal document number - hold the value once and emit it into whichever field the "
     "artefact requires."),

    ("Employer Commercial Registration Number",
     "Número de matrícula mercantil",
     "Commercial registration number issued by the Chamber of Commerce of the municipality of "
     "domicile.",
     "CM",
     "Mandatory for commercial entities and for any employer claiming the Ley 1429 de 2010 "
     "formalisation benefits or the Ley 2466 de 2025 art. 34 part-time contribution regime.",
     "Text", "Alphanumeric - format set by each Chamber of Commerce", "",
     "CCG Module 2.1. One of only three sub-national registration elements in Colombian payroll "
     "(the others being the family compensation fund and the work-centre risk class). DERIVED "
     "format - the Chambers do not publish a common mask; confirm with RA."),

    ("DIAN Electronic Payroll Software Identifier",
     "Identificador del software (SoftwareID)",
     "Identifier assigned by DIAN when the employer's payroll software is activated for the "
     "electronic payroll support document. Together with a secret PIN it produces the CUNE security "
     "code carried in every document.",
     "M", "",
     "Text", "String assigned by DIAN at software activation", "",
     "CCG Module 2.1; Res. DIAN 000013 de 2021 arts. 1, 5, 22. THE PAIRED PIN IS A CREDENTIAL: it "
     "never appears in the XML and is held in the integration credential store described in "
     "CO-SIR-001, NOT in this Data Dictionary. The security code itself (SHA-384 of SoftwareID + "
     "PIN + document number) is a COMPUTED value (SYS), not master data."),

    ("Electronic Payroll Document Prefix",
     "Prefijo de numeración de la nómina electrónica",
     "Employer-defined prefix of the electronic payroll document number. The document number is the "
     "prefix plus a consecutive sequence and must be unique per employee.",
     "M", "",
     "Text", "Employer-defined alphanumeric prefix", "",
     "CCG Module 2.1. The CONSECUTIVE NUMBER is generated by the engine (SYS), not master data. "
     "DIAN global validation rule 90 rejects a repeated document number for the same employee; a "
     "rejected document must be re-transmitted with a NEW consecutive number."),

    ("Information Operator Code",
     "Código del operador de información",
     "Code of the licensed private information operator through which the integrated contribution "
     "return is filed and paid. The employer NEVER transacts directly with the government for "
     "social security.",
     "M", "",
     "Text", "N(2) - assigned by the operador's own system", "",
     "Spec ref: CO-PILA-003 Field Options ('Código del operador de información', 2 digits). CCG "
     "Module 2.1 item 9 - an employer-level election stored once and inherited by every employee. "
     "Operadores are private entities licensed by the Ministerio de Salud y Protección Social."),

    ("Legal Representative Document Type",
     "Tipo de identificación del representante legal",
     "Identity-document type of the employer's legal representative, who signs the contribution "
     "return and the withholding-tax return.",
     "CM",
     "Mandatory where Employer Person Type = J (jurídica); optional where Employer Person Type = N "
     "(natural). Bidirectional pair with Employer Person Type.",
     "Text", "A(2) - narrower catalogue than the contributor list",
     "Legal Representative Document Type",
     "Spec ref: Company.Legal_Rep_ID_Type - CO-PILA-003 (A1-020, Mandatory=C). NI, TI, SC, PE and "
     "RC are NOT available for a legal representative even though several of them are available for "
     "a contributor."),

    ("Legal Representative Identification Number",
     "Número de identificación del representante legal / signatario",
     "Identity-document number of the legal representative or signatory of the return.",
     "CM",
     "Mandatory where Employer Person Type = J (jurídica); optional where Employer Person Type = N. "
     "Bidirectional pair with Employer Person Type and with the legal-representative name block.",
     "Text", "A(16) on PILA, left-justified and space-filled; numeric on Formulario 350", "",
     "Spec ref: Company.Legal_Rep_ID - CO-DIAN-002 (casilla 139, Mandatory=Y), CO-PILA-003 (A1-018, "
     "Mandatory=C)."),

    ("Legal Representative Verification Digit",
     "DV del signatario",
     "Verification digit of the legal representative's or signatory's identification number.",
     "CM",
     "Populated wherever the signatory identification number is populated.",
     "Text", "N(1), 0 to 9", "",
     "Spec ref: Company.Legal_Rep_ID_DV - CO-DIAN-002 (casilla 140, Mandatory=Y), CO-PILA-003 "
     "(A1-019, Mandatory=Y). Same weighted modulus-11 algorithm as the employer NIT DV."),
]

# ---------------------------------------------------------------------------
# SHEET 5 - Country Fields : employer / legal-entity master data
# ---------------------------------------------------------------------------
CF_LEGAL_ENTITY = [
    # -- Identity of the declarant -----------------------------------------
    ("Employer Corporate Name",
     "Razón social del empleador",
     "Registered corporate name of the employer. Declarant name on every statutory artefact.",
     "CM",
     "Populated where the employer is a LEGAL person or a sociedad de hecho. MUTUALLY EXCLUSIVE "
     "with the four employer natural-person name fields: a natural-person employer must NOT "
     "populate this field.",
     "Text", "A(200) on PILA; variable length on the DIAN artefacts", "",
     "Spec ref: Company.Legal_Name - CO-DIAN-001 (NIE032, Mandatory=C), CO-DIAN-002 (casilla 11, "
     "Mandatory=C), CO-PILA-003 (A1-001 and T2R1-004, Mandatory=Y), CO-DIAN-004 (casilla 11, "
     "Mandatory=C/Y). Bidirectional exclusivity with the natural-person name block, enforced by the "
     "instructivo of every artefact."),

    ("Employer First Surname",
     "Primer apellido del empleador (persona natural)",
     "First surname of the employer where the employer is a natural person.",
     "CM",
     "Populated ONLY where the employer is a natural person. Mutually exclusive with Employer "
     "Corporate Name.",
     "Text", "Variable length", "",
     "Spec ref: Company.First_Surname - CO-DIAN-001 (NIE210, Mandatory=C), CO-DIAN-002 (casilla 7, "
     "Mandatory=C), CO-DIAN-004 (casilla 7, Mandatory=C)."),

    ("Employer Second Surname",
     "Segundo apellido del empleador (persona natural)",
     "Second surname of the employer where the employer is a natural person.",
     "CM",
     "Populated ONLY where the employer is a natural person. Mutually exclusive with Employer "
     "Corporate Name.",
     "Text", "Variable length", "",
     "Spec ref: Company.Second_Surname - CO-DIAN-001 (NIE211, Mandatory=C), CO-DIAN-002 (casilla 8, "
     "Mandatory=C), CO-DIAN-004 (casilla 8, Mandatory=C)."),

    ("Employer First Name",
     "Primer nombre del empleador (persona natural)",
     "First given name of the employer where the employer is a natural person.",
     "CM",
     "Populated ONLY where the employer is a natural person. Mutually exclusive with Employer "
     "Corporate Name.",
     "Text", "Variable length", "",
     "Spec ref: Company.First_Name - CO-DIAN-001 (NIE212, Mandatory=C), CO-DIAN-002 (casilla 9, "
     "Mandatory=C), CO-DIAN-004 (casilla 9, Mandatory=C)."),

    ("Employer Other Names",
     "Otros nombres del empleador (persona natural)",
     "Further given names of the employer where the employer is a natural person.",
     "CM",
     "Populated ONLY where the employer is a natural person. Mutually exclusive with Employer "
     "Corporate Name.",
     "Text", "Variable length", "",
     "Spec ref: Company.Other_Names - CO-DIAN-001 (NIE213, Mandatory=C), CO-DIAN-002 (casilla 10, "
     "Mandatory=C), CO-DIAN-004 (casilla 10, Mandatory=C)."),

    # -- Classification -----------------------------------------------------
    ("Employer Person Type",
     "Tipo de persona del aportante",
     "Whether the employer is a legal person or a natural person. Gates a large conditional block "
     "on the contribution return.",
     "M", "",
     "Text", "J / N", "Employer Person Type",
     "Spec ref: Company.Person_Type - CO-PILA-003 (A1-009, Mandatory=Y). Where J: the NIT "
     "verification digit and the whole legal-representative block become mandatory. Where N: the "
     "valid employer document types narrow to CC, CE, TI, PA, CD, PE and SC - NI is not available - "
     "and the verification digit must be ZERO."),

    ("Employer Legal Nature",
     "Naturaleza jurídica del aportante",
     "Legal nature of the employer entity.",
     "M", "",
     "Text", "N(1)", "Employer Legal Nature",
     "Spec ref: Company.Legal_Nature - CO-PILA-003 (A1-008, Mandatory=Y). PRIVATE-SECTOR FILTER: "
     "the Mercans platform serves private employers, so only value 2 (Privada) is in scope. Public "
     "(1), mixed-capital (3), multilateral organisations (4) and foreign public-law entities not "
     "subject to Colombian law (5) are excluded - see the mapper Notes."),

    ("Class of Contributor",
     "Clase de aportante",
     "Size and benefit classification of the employer, driven by the number of contributors across "
     "ALL branches and by eligibility for the small-business and formalisation regimes.",
     "M", "",
     "Text", "A(1) - A / B / C / D", "Class of Contributor",
     "Spec ref: Company.Aportante_Class - CO-PILA-003 (A1-007, Mandatory=Y). The headcount is "
     "counted across all branches and dependencies, NOT per branch. Class D (Ley 1429 de 2010 "
     "beneficiary) makes the commercial-registry date and the registered-seat department code "
     "mandatory."),

    ("Contributor Type",
     "Tipo de aportante",
     "Category of the party making the contribution. For corporate payroll the value is always "
     "1 - Empleador.",
     "M", "",
     "Text", "N(2) zero-filled", "Contributor Type",
     "Spec ref: Company.Aportante_Type - CO-PILA-003 (A1-030 and T2R1-021, Mandatory=Y). "
     "PRIVATE-SECTOR FILTER: only value 1 (Empleador) is in scope. Independents (2), public "
     "entities and universities (3), guilds and religious congregations (4), associated-work "
     "cooperatives (5), diplomatic missions (6) and the remaining special payers (7-12) are "
     "excluded - see the mapper Notes."),

    ("Form of Presentation",
     "Forma de presentación",
     "Whether the employer files one consolidated contribution return for the whole legal person or "
     "one return per branch.",
     "M", "",
     "Text", "U (único) / S (sucursal)", "Form of Presentation",
     "Spec ref: Company.Presentation_Form - CO-PILA-003 (A1-010 and T2R1-011, Mandatory=Y). "
     "Bidirectional pair with the branch code and branch name: where U, both MUST BE BLANK; where "
     "S, both become required."),

    ("PILA Filing Modality",
     "Modalidad de la planilla (electrónica o asistida)",
     "Whether the contribution return is prepared and paid electronically on the operador's site or "
     "keyed by the operador's call centre on the employer's instruction.",
     "M", "",
     "Text", "1 (electrónica) / 2 (asistida)", "PILA Filing Modality",
     "Spec ref: CO-PILA-003 Field Options. Employer-level election gated by headcount under Decreto "
     "780 de 2016 art. 3.2.3.9 as substituted by Decreto 1990 de 2016 - the headcount is aggregated "
     "across all branches under the same legal person. The THRESHOLD is a parameter (WTC); the "
     "elected modality is master data."),

    ("PILA Planilla Type",
     "Tipo de planilla",
     "Default planilla type the employer files. The standard value for private corporate payroll is "
     "E (planilla empleados).",
     "M", "",
     "Text", "A(1)", "PILA Planilla Type",
     "Scope option_mapper_scope.correction_codes. The DEFAULT is master data; the value actually "
     "used in a given run may be overridden by the event (A for omitted hires, N for corrections, M "
     "for arrears, J for a court-ordered settlement, X for a liquidated company) and that override "
     "is TRANSACTIONAL, not master data. Planilla types S, I, Y, T, F, H, K, U and O are out of "
     "scope - see the mapper Notes."),

    ("Formato 2276 Informant Type",
     "Tipo de informante - Formato 2276",
     "Capacity in which the employer files the annual rentas de trabajo information return. An "
     "ordinary employer files as informante general.",
     "M", "",
     "Text", "N(1)", "Formato 2276 Informant Type",
     "Spec ref: CO-DIAN-005 (Res. DIAN 000227 de 2025 par. 4). Where the value is 1 the trust and "
     "contract-participant numerals (N35, N36) 'no se deben diligenciar'. Values 2-8 attach to "
     "trust, mandate, consortium, hydrocarbons, joint-venture, participation-account and public-"
     "cooperation structures and are out of scope for ordinary employer payroll."),

    # -- Location and contact ----------------------------------------------
    ("Employer Address",
     "Dirección del empleador",
     "Registered address of the employer, reported in the declarant section of the statutory "
     "artefacts.",
     "M", "",
     "Text", "A(40) on PILA; variable length on the nómina electrónica", "",
     "Spec ref: Company.Address - CO-DIAN-001 (NIE038, Mandatory=Y), CO-PILA-003 (A1-011, "
     "Mandatory=Y)."),

    ("Employer Country Code",
     "País del empleador",
     "Country of the employer's registered address. A required attribute of the employer element on "
     "the electronic payroll support document.",
     "M", "",
     "Text", "ISO 3166-1 alpha-2 (Anexo Técnico table 5.4.1)",
     "ISO 3166-1 (see the 'Country Codes - ISO 3166-1' sheet)",
     "Spec ref: Company.Country_Code - CO-DIAN-001 (NIE013 and NIE035, Mandatory=Y)."),

    ("Employer Department Code",
     "Departamento del empleador",
     "Two-digit DANE DIVIPOLA department code of the employer's registered address.",
     "M", "",
     "Text", "N(2) DANE DIVIPOLA (Anexo Técnico table 5.4.2)", "",
     "Spec ref: Company.Department_Code - CO-DIAN-001 (NIE014 and NIE036, Mandatory=Y), CO-PILA-003 "
     "(A1-013, Mandatory=Y), CO-DIAN-004 (casilla 34, Mandatory=Y). Use the DANE DIVIPOLA "
     "catalogue, NOT the ISO 3166-2:CO list."),

    ("Employer Municipality Code",
     "Municipio del empleador",
     "DANE DIVIPOLA municipality of the employer's registered address. Also serves as the 'lugar "
     "donde se practicó la retención' on the annual certificate of income and withholdings.",
     "M", "",
     "Text", "N(5) full DIVIPOLA on the nómina electrónica (11001); N(3) suffix on PILA and "
             "Formulario 220",
     "",
     "Spec ref: Company.Municipality_Code - CO-DIAN-001 (NIE015 generation municipality and NIE037 "
     "employer municipality, Mandatory=Y); and Company.City_Code - CO-PILA-003 (A1-012, "
     "Mandatory=Y) and CO-DIAN-004 (casilla 35 'Lugar donde se practico la retencion', "
     "Mandatory=Y). SPLIT-CODE TRAP - store five digits once and split into 2 + 3 on the artefacts "
     "that require it."),

    ("Registered-Seat Department Code",
     "Código del departamento del domicilio (Ley 1429)",
     "Two-digit DANE department code of the employer's registered seat, required of a Ley 1429 de "
     "2010 formalisation beneficiary.",
     "CM",
     "Mandatory for a Ley 1429 de 2010 beneficiary, i.e. where Class of Contributor = D or the "
     "Ley 1429 CCF benefit flag = S. Bidirectional set with those two fields and with the "
     "commercial-registry date.",
     "Text", "A(2) DANE DIVIPOLA", "",
     "Spec ref: Company.Department_Code_Registry - CO-PILA-003 (A1-032, Mandatory=C). Distinct from "
     "the ordinary employer department code, which follows the operating address."),

    ("Employer Telephone",
     "Teléfono del empleador",
     "Contact telephone number of the employer, reported on the contribution return.",
     "M", "",
     "Text", "N(10) right-justified, zero-filled", "",
     "Spec ref: Company.Phone - CO-PILA-003 (A1-015, Mandatory=Y)."),

    ("Employer Fax",
     "Fax del empleador",
     "Fax number of the employer. Retained in the contribution-return layout; supplied by the "
     "employer where held.",
     "O", "",
     "Text", "N(10) right-justified, zero-filled", "",
     "Spec ref: Company.Fax - CO-PILA-003 (A1-016, Mandatory=N). Legacy field in the Resolución "
     "2388 de 2016 layout - zero-fill where not held."),

    ("Employer E-mail Address",
     "Dirección de correo electrónico del empleador",
     "Contact e-mail address of the employer, reported on the contribution return and used by the "
     "operador for notifications.",
     "M", "",
     "Text", "A(60)", "",
     "Spec ref: Company.Email - CO-PILA-003 (A1-017, Mandatory=Y)."),

    # -- Branch -------------------------------------------------------------
    ("Branch or Dependency Code",
     "Código de la sucursal o de la dependencia",
     "Employer-assigned code of the branch or dependency for which the contribution return is filed.",
     "CM",
     "MUST BE BLANK where Form of Presentation = U (único). Populated only where Form of "
     "Presentation = S (sucursal). Bidirectional pair with Form of Presentation and with the "
     "branch name.",
     "Text", "A(10) left-justified, space-filled", "",
     "Spec ref: Company.Branch_Code - CO-PILA-003 (A1-005 and T2R1-012, Mandatory=C). The Archivo "
     "Tipo 2 header value must equal the Archivo Tipo 1 value."),

    ("Branch or Dependency Name",
     "Nombre de la sucursal o de la dependencia",
     "Name of the branch or dependency for which the contribution return is filed.",
     "CM",
     "Populated together with the branch code, i.e. only where Form of Presentation = S. Where the "
     "branch has no name, the annex directs that the branch CODE is written here instead.",
     "Text", "A(40) left-justified, space-filled", "",
     "Spec ref: Company.Branch_Name - CO-PILA-003 (A1-006 and T2R1-013, Mandatory=C). Branches "
     "trading under the same corporate name are NOT separate registrations - CCG Module 2.1."),

    # -- Sector / risk / levies --------------------------------------------
    ("Economic Activity Code (CIIU)",
     "Código de actividad económica principal (CIIU rev. 4 A.C.)",
     "Principal economic activity of the employer under the CIIU revision 4 classification adapted "
     "for Colombia. Taken from casilla 46 of the RUT.",
     "M", "",
     "Text", "N(4)", "",
     "Spec ref: Company.CIIU_Code - CO-DIAN-002 (casilla 27, Mandatory=C), CO-PILA-003 (A1-014, "
     "Mandatory=Y). The SAME classification drives the occupational-risk class assignment and, for "
     "a legal person exonerated under ET art. 114-1, the self-withholding rate on Formulario 350. "
     "External catalogue - DIAN Resoluciones 000114 de 2020, 001232 de 2022 and successors; DANE "
     "Resolución 66 de 2012 for the PILA variant."),

    ("DIAN Sectional Office Code",
     "Código de la dirección seccional",
     "Code of the DIAN sectional office of the employer's principal domicile, taken from casilla 12 "
     "of the RUT.",
     "M", "",
     "Text", "N(2)", "",
     "Spec ref: Company.DIAN_Seccional_Code - CO-DIAN-002 (casilla 12, Mandatory=Y). A "
     "configuration constant per legal entity, not a per-return input. External DIAN catalogue."),

    ("Employer ARL Code",
     "Código de la ARL del aportante",
     "Institution code of the occupational-risk insurer with which the employer is affiliated.",
     "M", "",
     "Text", "A(6) - administradoras catalogue; prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - three alphabetic positions naming the subsystem then three numeric positions naming the entity", "",
     "Spec ref: Company.ARL_Code - CO-PILA-003 (T2R1-014, Mandatory=Y). EMPLOYER election (CCG "
     "Module 2.1 item 3), inherited by every employee."),

    ("Work Centre Occupational Risk Class",
     "Clase de riesgo laboral del centro de trabajo",
     "Occupational-risk class I to V of the work centre. The class attaches to the WORK CENTRE, not "
     "to the company, so an employer with a corporate office and a plant legitimately carries more "
     "than one class - and each employee's contribution follows the class of the centre where they "
     "work.",
     "M", "",
     "Text", "I / II / III / IV / V", "Occupational Risk Class",
     "Spec ref: Company.Risk_Class - CO-PILA-003 (T2R2-078, Mandatory=Y). Legal basis: Decreto 1072 "
     "de 2015 arts. 2.2.4.2.5.6 and 2.2.4.3.5. The class is master data held per work centre; the "
     "RATE (initial rate and the class minimum/maximum) is a parameter (WTC), NOT DD. Bidirectional "
     "set with Work Centre Code and the VCT change-of-work-centre event."),

    ("Commercial Registry Date",
     "Fecha de matrícula mercantil",
     "Date of the employer's commercial registration with the Chamber of Commerce.",
     "CM",
     "MANDATORY for an employer benefiting from the Ley 1429 de 2010 formalisation regime, i.e. "
     "where Class of Contributor = D or the Ley 1429 CCF benefit flag = S. Bidirectional set with "
     "those fields and with the registered-seat department code.",
     "Date", "AAAA-MM-DD", "",
     "Spec ref: Company.Commercial_Registry_Date - CO-PILA-003 (A1-031, Mandatory=C)."),

    ("Exonerated from Health, SENA and ICBF (art. 114-1)",
     "Aportante exonerado de aportes a salud, SENA e ICBF",
     "Indicates that the employer is exonerated from the employer health contribution and from the "
     "SENA and ICBF payroll levies under Tax Code art. 114-1.",
     "M", "",
     "Text", "S / N", "Yes/No Indicator",
     "Spec ref: Company.Exonerated_Flag - CO-PILA-003 (A1-033, Mandatory=Y). THE EXONERATION NEVER "
     "TOUCHES pension (12%), occupational risk, or the family compensation fund (4%). It is also "
     "disapplied per employee where the health contribution base reaches 10 minimum wages - that "
     "per-contributor test produces a DERIVED value on the return (CALC), not a second master-data "
     "field. Bidirectional with the CIIU self-withholding activity code on Formulario 350."),

    ("Ley 1429 art. 5 CCF Benefit",
     "Aportante acogido a los beneficios del artículo 5 de la Ley 1429 de 2010 (CCF)",
     "Indicates that the employer has elected the Ley 1429 de 2010 art. 5 benefits in respect of the "
     "family compensation fund levy.",
     "M", "",
     "Text", "S / N", "Yes/No Indicator",
     "Spec ref: Company.Ley1429_CCF_Flag - CO-PILA-003 (A1-034, Mandatory=Y). Where S, the "
     "commercial-registry date and the registered-seat department code become mandatory and Class "
     "of Contributor is normally D."),

    ("Single-Fund Planilla Severance Fund Code",
     "Código del fondo de cesantías de la planilla (fondo único)",
     "Code of the severance-savings fund used at PLANILLA level where the employer deposits the "
     "whole file to a single fund. Where the single-fund indicator is set, this value OVERWRITES "
     "the per-employee fund code for every record in the file.",
     "CM",
     "Mandatory where the employer files a single-fund severance deposit planilla; blank where each "
     "employee's own fund code governs.",
     "Text", "N(2) - published fund catalogue", "Severance-Savings Fund",
     "Spec ref: Company.Cesantias_Fund_Code (declared in build_co_specs._DD_MASTER_MAPPINGS; the "
     "single-fund indicator is CO-CESANTIAS-006 E07, which back-references the per-employee field "
     "T02). Using a single fund where employees are affiliated to different funds MISDIRECTS the "
     "deposit - the penalty is one day's salary per day of delay, per employee, uncapped."),

    # -- Employer status events --------------------------------------------
    ("Employer Status Action Type",
     "Tipo de acción (concordato, reestructuración, liquidación, cese)",
     "Insolvency, restructuring, liquidation or cessation event affecting the employer.",
     "CM",
     "Optional in general. Where populated it makes the insolvency start date MANDATORY and the "
     "commercial-activity cessation date required. Bidirectional set with both dates.",
     "Text", "N(1)", "Employer Status Action Type",
     "Spec ref: Company.Action_Type - CO-PILA-003 (A1-026, Mandatory=C). A value of 4 (cese de "
     "actividades) fixes the date from which the employer is no longer obliged to contribute."),

    ("Insolvency / Restructuring / Liquidation Start Date",
     "Fecha de inicio del concordato, reestructuración, liquidación o cese de actividades",
     "Date on which the employer status event began.",
     "CM",
     "MANDATORY where the employer status action type is populated. Bidirectional pair with that "
     "field.",
     "Date", "AAAA-MM-DD", "",
     "Spec ref: Company.Insolvency_Start_Date - CO-PILA-003 (A1-025, Mandatory=C)."),

    ("Commercial Activity Cessation Date",
     "Fecha en que terminó actividades comerciales",
     "Date on which the employer ceased commercial activity.",
     "CM",
     "Required where the employer status action type is populated - the annex directs that it "
     "'se debe diligenciar cuando se ha reportado información en el campo 26 de este registro'.",
     "Date", "AAAA-MM-DD", "",
     "Spec ref: Company.Trading_Cease_Date - CO-PILA-003 (A1-027, Mandatory=C)."),

    # -- Legal representative names ----------------------------------------
    ("Legal Representative First Surname",
     "Primer apellido del representante legal",
     "First surname of the employer's legal representative.",
     "CM",
     "MANDATORY where Employer Person Type = J. Bidirectional pair with Employer Person Type.",
     "Text", "A(20) left-justified, space-filled", "",
     "Spec ref: Company.Legal_Rep_First_Surname - CO-PILA-003 (A1-021, Mandatory=C)."),

    ("Legal Representative Second Surname",
     "Segundo apellido del representante legal",
     "Second surname of the employer's legal representative.",
     "O", "",
     "Text", "A(30) left-justified, space-filled", "",
     "Spec ref: Company.Legal_Rep_Second_Surname - CO-PILA-003 (A1-022, Mandatory=N)."),

    ("Legal Representative First Name",
     "Primer nombre del representante legal",
     "First given name of the employer's legal representative.",
     "CM",
     "MANDATORY where Employer Person Type = J. Bidirectional pair with Employer Person Type.",
     "Text", "A(20) left-justified, space-filled", "",
     "Spec ref: Company.Legal_Rep_First_Name - CO-PILA-003 (A1-023, Mandatory=C)."),

    ("Legal Representative Second Name",
     "Segundo nombre del representante legal",
     "Second given name of the employer's legal representative.",
     "O", "",
     "Text", "A(30) left-justified, space-filled", "",
     "Spec ref: Company.Legal_Rep_Second_Name - CO-PILA-003 (A1-024, Mandatory=N)."),
]

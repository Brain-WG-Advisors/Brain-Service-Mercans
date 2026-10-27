# -*- coding: utf-8 -*-
"""
Colombia Data Dictionary - employment / working-time / tax / family / social-security
employee master-data blocks (part 2 of the data set).
"""

CF_EMPLOYEE_EMPLOYMENT = [
    ("Hire Date",
     "Fecha de ingreso del trabajador",
     "Date on which the employment relationship with the declaring employer commenced.",
     "M", "",
     "Date", "AAAA-MM-DD", "",
     "Spec ref: Contract.Start_Date - CO-DIAN-001 (NIE002, Mandatory=Y), CO-PILA-003 (T2R2-080, "
     "Mandatory=C), CO-CESANTIAS-006 (T20, Mandatory=Y). On PILA the field is mandatory where the "
     "ING novedad is marked. Seniority driver for the severance-savings liquidation, the indemnity "
     "tier and work-clothing eligibility. Colombia has NO cumulative-withholding carry-over between "
     "employers and no P45 equivalent - a new employer starts the withholding calculation fresh "
     "(CCG Module 2.2)."),

    ("Termination Date",
     "Fecha de retiro del trabajador",
     "Date on which the employment relationship ended.",
     "CM",
     "Mandatory upon a leaver event: populated on the nómina electrónica only for the month in "
     "which the relationship ends, and mandatory on the contribution return where the RET "
     "(retiro) novedad is marked.",
     "Date", "AAAA-MM-DD", "",
     "Spec ref: Contract.End_Date - CO-DIAN-001 (NIE003, Mandatory=C), CO-PILA-003 (T2R2-081, "
     "Mandatory=C). Bidirectional pair with the RET novedad. Must fall inside or before the "
     "settlement window of the document."),

    ("Contract Type",
     "Tipo de contrato",
     "Type of employment contract. Five values in the private-sector population: fixed-term "
     "(maximum four years after Ley 2466 de 2025 art. 6), indefinite-term, specific work or task, "
     "apprenticeship and internship.",
     "M", "",
     "Text", "N(1) - code 1 to 5 (Anexo Técnico table 5.5.2)", "Contract Type",
     "Spec ref: Contract.Type_Code - CO-DIAN-001 (NIE061, Mandatory=Y). Scope "
     "option_mapper_scope.contract_type. Ley 2466 de 2025 art. 21 recast the apprenticeship as a "
     "special fixed-term LABOUR contract, regulated by Decreto 0223 of 5 March 2026 - it is now a "
     "contract type, not a training arrangement."),

    ("Worker Type",
     "Tipo de trabajador / tipo de cotizante",
     "Contributor category of the employee. Selects the contribution rules that apply on the "
     "integrated contribution return and on the electronic payroll support document.",
     "M", "",
     "Text", "N(2) zero-filled - e.g. 01 (Anexo Técnico table 5.5.3 / PILA tipo cotizante)",
     "Worker Type",
     "Spec ref: Employee.Worker_Type_Code - CO-DIAN-001 (NIE041, Mandatory=Y), CO-PILA-003 "
     "(T2R2-005, Mandatory=Y). MAPPING TRAP: the nómina electrónica table 5.5.3 carries only "
     "SIXTEEN values while the PILA tipo cotizante list carries far more - copying a PILA code "
     "straight into the XML is a documented failure. Public-sector codes 18, 30, 47 and 58, "
     "domestic service 02, community mothers 04, associated-work cooperative members 31 and every "
     "independent-worker code are OUT OF SCOPE - see the mapper Notes."),

    ("Worker Sub-Type",
     "Subtipo de trabajador / subtipo de cotizante",
     "Contributor sub-category. The value that matters for corporate payroll is 01 - an employed "
     "old-age pensioner in active service, who makes NO pension contribution.",
     "M", "",
     "Text", "N(2) zero-filled - 00 where no sub-type applies", "Worker Sub-Type",
     "Spec ref: Employee.Worker_SubType_Code - CO-DIAN-001 (NIE042, Mandatory=Y), CO-PILA-003 "
     "(T2R2-006, Mandatory=Y). HARD RULE: where the sub-type is 01, 02, 03, 04, 05, 06, 09 or 12 "
     "the PILA pension-contribution rate field MUST be 0. This field carries the 'active pensioner' "
     "attribute - do NOT create a separate active-pensioner flag. MAPPING TRAP: the nómina "
     "electrónica table 5.5.4 carries only 00 and 01; PILA carries more."),

    ("Pay Frequency",
     "Periodo de nómina",
     "Frequency at which salary is paid. Labour Code art. 134 caps the interval at one month for "
     "monthly salaries and one week for day wages; any shorter frequency is permitted.",
     "M", "",
     "Text", "N(1) - code 1 to 6 (Anexo Técnico table 5.5.1)", "Pay Frequency",
     "Spec ref: Contract.Pay_Frequency_Code - CO-DIAN-001 (NIE029, Mandatory=Y). CRITICAL "
     "CONFIGURATION POINT: whatever the frequency, the electronic payroll support document is ONE "
     "MONTHLY document per employee - Res. DIAN 000013 de 2021 art. 3, 'con independencia de que el "
     "obligado realice pagos en periodos diferentes o inferiores'. A semi-monthly payroll does NOT "
     "produce two filings a month."),

    ("Payment Form",
     "Forma de pago",
     "Settlement form of the payroll payment. The Anexo Técnico publishes a single value - contado "
     "(immediate settlement).",
     "M", "",
     "Text", "N(1) - code 1 (Anexo Técnico table 5.3.3.1)", "Payment Form",
     "Spec ref: Contract.Payment_Form_Code - CO-DIAN-001 (NIE064, Mandatory=Y). Distinct from "
     "Payment Method - 'forma' is cash-vs-credit settlement, 'método' is the medium."),

    ("Payment Method",
     "Medio de pago",
     "Medium through which the net salary is paid. Drives whether the bank block (bank name, "
     "account type, account number) must be populated.",
     "M", "",
     "Text", "N(2) - UN/EDIFACT 4461 code (Anexo Técnico table 5.3.3.2)", "Payment Method",
     "Spec ref: Contract.Payment_Method_Code - CO-DIAN-001 (NIE065, Mandatory=Y). Bidirectional set "
     "with the three bank fields: where the value is 10 (efectivo) the bank attributes must be "
     "ABSENT; where it is a bank-mediated medium they are all required."),

    ("Weekly Contracted Hours",
     "Jornada semanal contratada",
     "Contracted ordinary weekly working hours. The statutory maximum steps DOWN during fiscal "
     "year 2026: 44 hours to 14 July 2026 and 42 hours from 15 July 2026.",
     "M", "",
     "Decimal", "Hours per week, up to 2 decimals (e.g. 42.00)", "",
     "CCG Module 2.2 working-time group. Calculation-driving: the ordinary hourly rate, and "
     "therefore every overtime and night-surcharge value, is derived from it. NOT on any in-scope "
     "statutory filing - held as a calculation input. The 42-hour step is a PARAMETER (WTC); this "
     "field is the employee's contracted value."),

    ("Days Worked Per Week",
     "Días laborados por semana",
     "Number of ordinary working days in the employee's week - five or six.",
     "M", "",
     "Integer", "5 or 6", "",
     "CCG Module 2.2 working-time group. Together with the obligatory rest day it determines which "
     "days attract the Sunday / public-holiday surcharge. Not on any in-scope statutory filing."),

    ("Obligatory Rest Day",
     "Día de descanso obligatorio",
     "Weekday designated as the employee's obligatory paid rest day. SUNDAY IS PRESUMED unless a "
     "written agreement designates another day.",
     "M", "",
     "Text", "Weekday name (default: Domingo)", "",
     "CCG Module 2.2. Calculation-driving: the Sunday / public-holiday surcharge attaches to the "
     "designated rest day, not automatically to the calendar Sunday. Default value: Domingo."),

    ("36-Hour Shift System Flag",
     "Jornada por turnos sucesivos de 36 horas",
     "Indicates that the employee works the successive-shift regime, which has its own weekly-hours "
     "and surcharge treatment.",
     "O", "",
     "Text", "S / N", "Yes/No Indicator",
     "CCG Module 2.2 working-time group. Calculation-driving where set. Not on any in-scope "
     "statutory filing."),

    ("Work Modality (Telework / On-Site)",
     "Modalidad de trabajo (teletrabajo / presencial)",
     "Working modality of the employee. A teleworker earning less than two minimum wages receives "
     "the MANDATORY connectivity allowance IN PLACE OF the transport allowance - the two are never "
     "paid together.",
     "CM",
     "Mandatory where the employee is a teleworker under Ley 1221 de 2008 as amended by Ley 2466 de "
     "2025 arts. 52-54; defaults to on-site otherwise.",
     "Text", "PRES / TT-AUT / TT-MOV / TT-SUP", "Work Modality",
     "CCG Module 4 (connectivity allowance, Ley 2466 de 2025 art. 53) and Module 2.2. "
     "Calculation-driving: selects connectivity allowance vs transport allowance. The nómina "
     "electrónica carries a dedicated Teletrabajo devengado element (NIE158); the ALLOWANCE AMOUNT "
     "is a parameter/wage type (WTC), not DD."),

    ("All-Inclusive Salary Flag",
     "Salario integral",
     "Indicates that the employee is remunerated under the all-inclusive salary regime of Labour "
     "Code art. 132 num. 2, which requires a salary of at least 13 minimum wages AND a written "
     "agreement.",
     "M", "",
     "Text", "Boolean true/false on the nómina electrónica XML; S / N (blank or X) on PILA",
     "Yes/No Indicator",
     "Spec ref: Employee.Integral_Salary_Flag - CO-DIAN-001 (NIE056, Mandatory=Y), CO-PILA-003 "
     "(T2R2-041, Mandatory=C). HARD RULE: where set, the four PILA contribution-base fields must be "
     "70% of the integral salary. An all-inclusive-salary employee accrues NO separate severance "
     "savings, service bonus or severance interest - see the Severance-Savings Regime field."),

    ("Non-Salary Pact Flag",
     "Pacto de exclusión salarial",
     "Indicates that an express, written, signed non-salary pact under Labour Code art. 128 attaches "
     "to specified payments made to this employee.",
     "CM",
     "Mandatory where any wage type paid to the employee is treated as non-salary by written pact. "
     "The pact must be (a) express, (b) written and (c) attached to identified payments.",
     "Text", "S / N", "Yes/No Indicator",
     "CCG Module 4 (Labour Code art. 128; Ley 1393 de 2010 art. 30). Calculation-driving: a valid "
     "pact removes the payment from the labour-law salary base permanently, but excludes it from "
     "the CONTRIBUTION base only up to 40% of total remuneration - everything above that line is "
     "added back. The 40% clamp itself is a parameter and the add-back is a calculated amount "
     "(WTC); this flag is the master-data switch that turns the clamp on."),

    ("High-Risk Pension Activity Flag",
     "Actividad de alto riesgo para pensión",
     "Indicates that the employee performs a high-risk activity under Decreto Ley 2090 de 2003, "
     "which carries a non-standard (higher) pension contribution.",
     "M", "",
     "Text", "Boolean true/false on the nómina electrónica XML; S / N (blank or X) on PILA",
     "Yes/No Indicator",
     "Spec ref: Employee.High_Risk_Pension_Flag - CO-DIAN-001 (NIE043, Mandatory=Y), CO-PILA-003 "
     "(T2R2-079, Mandatory=C). Bidirectional pair with the PILA pension-contribution-rate field. "
     "The RATE is a parameter (WTC), not DD."),

    ("Disability / Reinforced Job-Stability Status",
     "Situación de discapacidad / estabilidad laboral reforzada",
     "Indicates that the employee holds certified disability status. Held because it changes the "
     "TERMINATION path - dismissal requires prior Ministry of Labour authorisation under Ley 361 de "
     "1997 - and because Ley 2466 de 2025 art. 15 obliges the employer to report a disability-hiring "
     "contract to the Ministry of Labour within 15 days of signature.",
     "O", "",
     "Text", "S / N", "Yes/No Indicator",
     "CCG Modules 2.1 and 9. NOT a contribution or withholding driver in Colombia - Colombia has no "
     "disability-percentage tax relief on the payroll side. Held as a compliance-path selector."),
]

CF_EMPLOYEE_TAX = [
    ("Tax Residence Status",
     "Condición de residencia fiscal",
     "Whether the employee is a Colombian tax resident under Tax Code art. 10 (more than 183 days "
     "of physical presence in any 365-day period, or one of the diplomatic / nationality-plus-"
     "connection tests). THE SINGLE MOST CONSEQUENTIAL WITHHOLDING SWITCH IN COLOMBIAN PAYROLL.",
     "M", "",
     "Text", "RES / NRES", "Tax Residence Status",
     "Calculation-driving. Resident: the progressive art. 383 table (0/19/28/33/35/37/39%) on the "
     "art. 388 depurated base, by Procedure 1 or 2. Non-resident: a FLAT 20% under art. 408 on the "
     "GROSS payment, with no depuration, no 25% exempt income, no art. 387 deductions and no "
     "tax-free band (DIAN Concepto 011108 of 29 June 2026, upholding Concepto 1789 int. 14595 of "
     "2025). THE SWITCH IS PROSPECTIVE, NEVER RETROACTIVE. INTERNAL CONFLICT TO ESCALATE: CCG "
     "Module 2.2 states a non-resident employee is withheld on the same art. 383 table, which "
     "contradicts the Module 6.2 matrix and the scope_manifest; Module 6.2 is the authoritative "
     "text and is the basis of this field."),

    ("Withholding Procedure",
     "Procedimiento de retención en la fuente",
     "Employer election, made per employee, between Procedure 1 (Tax Code art. 385 - each month "
     "stands alone) and Procedure 2 (art. 386 - a fixed percentage recomputed each June and "
     "December from the preceding 12 months).",
     "M", "",
     "Text", "1 / 2", "Withholding Procedure",
     "Calculation-driving. CCG Module 6.2: the procedure is elected by the EMPLOYER, per employee, "
     "and once elected Procedure 2 binds for the whole six-month semester. The FIXED PERCENTAGE "
     "produced by the June/December recalculation is a CALCULATED value (CALC/WTC), not master "
     "data. Not available at all for a non-resident, who is withheld at the flat art. 408 rate."),

    ("Employee-Requested Withholding Rate",
     "Tarifa de retención solicitada por el trabajador",
     "Higher withholding percentage requested in writing by the employee under Tax Code art. 383 "
     "par. 3. Employee-declared master data - the employer may not unilaterally increase the "
     "Procedure 2 fixed percentage mid-semester, so this is the only lawful route to a higher rate "
     "inside a semester.",
     "O", "",
     "Decimal", "Percentage, up to 2 decimals (e.g. 15.00)", "",
     "CCG Module 6.2. This is a USER-INPUT rate, not a statutory parameter: the statutory tables "
     "and thresholds remain in the WTC / parameter set. Requires a written employee request on file."),

    ("Treaty Status",
     "País con o sin convenio",
     "Whether the non-resident beneficiary is resident in a jurisdiction with a double-tax treaty in "
     "force with Colombia. Selects which payment-concept list and which rate basis apply on the "
     "monthly withholding return annex.",
     "CM",
     "Mandatory on every Formulario 350 annex row, i.e. wherever a payment is made to a "
     "non-resident. Not applicable to a resident employee.",
     "Text", "CON CONVENIO / SIN CONVENIO", "Treaty Status",
     "Spec ref: Employee.Treaty_Country_Code - CO-DIAN-002 (casilla 141 and casilla 144, "
     "Mandatory=C). SIN CONVENIO -> concepto 5 (prestación de servicios y compensación por "
     "servicios personales), rate 20% under ET art. 408. CON CONVENIO -> concepto 24 (rentas de "
     "trabajo), rate taken from the applicable treaty and possibly lower or nil."),

    ("Treaty Country Code",
     "País del convenio",
     "Country of residence of the non-resident beneficiary, used on the monthly withholding return "
     "annex.",
     "CM",
     "Mandatory on every Formulario 350 annex row. Where Treaty Status = CON CONVENIO the country "
     "must be one with a treaty in force with Colombia.",
     "Text", "ISO 3166-1 alpha-2", "ISO 3166-1 (see the 'Country Codes - ISO 3166-1' sheet)",
     "Spec ref: Employee.Treaty_Country_Code - CO-DIAN-002 (casilla 141 and casilla 144, "
     "Mandatory=C). Treaties in force include ES, CL, CH, CA, MX, KR, PT, IN, CZ, GB, FR, IT and "
     "JP; Bolivia, Ecuador and Peru are covered by Andean Community Decision 578 rather than a "
     "bilateral treaty. The TREATY RATE is a parameter (WTC), not DD - confirm the current list "
     "with RA each year."),

    ("Art. 380 Non-Filer Declaration",
     "Declaración del trabajador - artículo 380 E.T.",
     "The employee's own written declaration that the six conditions of Tax Code art. 380 are met, "
     "so that the annual certificate of income and withholdings substitutes for the employee's "
     "income-tax return.",
     "CM",
     "Mandatory where the employee is not obliged to file an income-tax return and asks that "
     "Formulario 220 serve as the substitute. Section 2 of Formulario 220 is completed from the "
     "employee's declaration, not from payroll data.",
     "Text", "S / N", "Yes/No Indicator",
     "Spec ref: CO-DIAN-004 Formulario 220 section 2 (ET arts. 378-380). The MONETARY conditions "
     "(4,500 UVT gross assets; 1,400 UVT gross income, consumption and deposits) are parameters "
     "(WTC); this field records only that the declaration was obtained. Evidence must be retained."),
]

CF_EMPLOYEE_FAMILY = [
    ("Number of Dependants",
     "Número de dependientes económicos",
     "Count of economic dependants declared by the employee under Tax Code art. 387 par. 2 and "
     "art. 336 num. 3.",
     "CM",
     "Mandatory where the employee claims the dependants deduction; enter 0 if none. Each dependant "
     "must also be identified individually - a count alone is not sufficient for the annual "
     "information return.",
     "Integer", "0 to N", "",
     "Calculation-driving family attribute. CCG Module 2.2 and Module 6/7. The DEDUCTION AMOUNTS "
     "and caps (10% of gross employment income capped at 32 UVT per month; the additional 72 UVT "
     "per dependant per year under art. 336 num. 3, up to four dependants) are parameters and "
     "calculated amounts (WTC), NOT DD. Not available to a non-resident."),

    ("Dependant Document Type",
     "Tipo de documento del dependiente económico",
     "Identity-document type of each declared economic dependant. Repeating block - one occurrence "
     "per dependant.",
     "CM",
     "Mandatory where the employee claimed the art. 387 par. 2 dependants deduction during the "
     "period. Populated as a bidirectional set with the dependant's document number, name and "
     "relationship - all four together or none.",
     "Text", "N(2) - Formulario 220 document-type catalogue", "Dependant Document Type",
     "Spec ref: Employee.Dependant_Document_Type - CO-DIAN-004 (casilla 79, Mandatory=C), "
     "CO-DIAN-005 (numeral N34, Mandatory=C). The information return requires the dependant's "
     "DOCUMENT, not merely a count - a missing document rejects the return. The Form 220 list is "
     "NARROWER than the nómina electrónica list."),

    ("Dependant Document Number",
     "Número de documento del dependiente económico",
     "Identity-document number of each declared economic dependant.",
     "CM",
     "Mandatory together with the dependant's document type, name and relationship wherever the "
     "dependants deduction is claimed.",
     "Text", "Numeric / alphanumeric per the dependant's document type", "",
     "Spec ref: Employee.Dependant_Document_Number - CO-DIAN-004 (casilla 80, Mandatory=C)."),

    ("Dependant Full Name",
     "Apellidos y nombres del dependiente económico",
     "Surnames and given names of each declared economic dependant.",
     "CM",
     "Mandatory together with the dependant's document type, document number and relationship.",
     "Text", "Free text", "",
     "Spec ref: Employee.Dependant_Name - CO-DIAN-004 (casilla 81, Mandatory=C)."),

    ("Dependant Relationship",
     "Parentesco del dependiente económico",
     "Relationship of the dependant to the employee and the basis on which dependency is claimed - "
     "the two are one question in Colombian law, because each of the five art. 387 par. 2 limbs "
     "combines a relationship with a qualifying condition.",
     "CM",
     "Mandatory together with the dependant's document type, document number and name. The "
     "qualifying evidence (education enrolment, medical certification of dependency, absence of "
     "income) must be retained.",
     "Text", "Coded value; emitted as free text on Formulario 220 casilla 82",
     "Dependant Relationship",
     "Spec ref: Employee.Dependant_Relationship - CO-DIAN-004 (casilla 82, Mandatory=C). "
     "Calculation-driving: the five limbs of ET art. 387 par. 2 are exhaustive; a person outside "
     "them is not a dependant however genuine the support."),
]

CF_EMPLOYEE_SOCSEC = [
    ("EPS Code",
     "Código de la EPS o EOC del afiliado",
     "Institution code of the health insurer (EPS or EOC) the employee has chosen. THE EMPLOYEE "
     "CHOOSES; the employer must affiliate to the existing entity, and the choice survives a change "
     "of employer.",
     "M", "",
     "Text", "A(6) - contribution-return institution catalogue (administradoras); prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - three alphabetic positions naming the subsystem then three numeric positions naming the entity", "",
     "Spec ref: Employee.EPS_Code - CO-PILA-003 (T2R2-033, Mandatory=Y). Codes come from the "
     "operador's administradoras catalogue, which is an EXTERNAL reference table maintained by the "
     "Ministerio de Salud - not enumerated here. CCG Module 2.2: a wrong institution code produces "
     "rejected or misdirected contributions."),

    ("EPS Transfer Code",
     "Código de la EPS o EOC a la cual se traslada el afiliado",
     "Institution code of the health insurer to which the employee is transferring in the period.",
     "CM",
     "Mandatory where the TAE (traslado a otra EPS) novedad is reported for the period; blank "
     "otherwise. Bidirectional pair with the TAE change event.",
     "Text", "A(6) - administradoras catalogue; prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - three alphabetic positions naming the subsystem then three numeric positions naming the entity", "",
     "Spec ref: Employee.EPS_Transfer_Code - CO-PILA-003 (T2R2-034, Mandatory=C). Scope "
     "option_mapper_scope.benefit_type (TDE / TAE)."),

    ("AFP Code",
     "Código de la administradora de fondos de pensiones del afiliado",
     "Institution code of the pension administrator the employee has chosen - a private "
     "individual-account administrator or Colpensiones. THE EMPLOYEE CHOOSES; the choice survives a "
     "change of employer.",
     "CM",
     "Mandatory in general. Blank is permitted ONLY where the Worker Type or Worker Sub-Type is one "
     "that is not obliged to contribute to the general pension system - notably Worker Sub-Type 01, "
     "an employed old-age pensioner in active service.",
     "Text", "A(6) - administradoras catalogue; prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - three alphabetic positions naming the subsystem then three numeric positions naming the entity", "",
     "Spec ref: Employee.AFP_Code - CO-PILA-003 (T2R2-031, Mandatory=C). Bidirectional set with "
     "Worker Type and Worker Sub-Type."),

    ("AFP Transfer Code",
     "Código de la administradora de pensiones a la cual se traslada el afiliado",
     "Institution code of the pension administrator to which the employee is transferring in the "
     "period.",
     "CM",
     "Mandatory where the TAP (traslado a otra administradora de pensiones) novedad is reported for "
     "the period; blank otherwise. Bidirectional pair with the TAP change event.",
     "Text", "A(6) - administradoras catalogue; prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - three alphabetic positions naming the subsystem then three numeric positions naming the entity", "",
     "Spec ref: Employee.AFP_Transfer_Code - CO-PILA-003 (T2R2-032, Mandatory=C). Scope "
     "option_mapper_scope.benefit_type (TDP / TAP)."),

    ("Pension Regime",
     "Régimen pensional",
     "Which of the two Colombian pension regimes the employee belongs to - the public "
     "defined-benefit regime (Régimen de Prima Media, administered by Colpensiones) or the private "
     "individual-account regime (Régimen de Ahorro Individual con Solidaridad).",
     "M", "",
     "Text", "RPM / RAIS", "Pension Regime",
     "CCG Module 5. Employee election that survives a change of employer and must be declared by a "
     "new joiner. Determines which administrator catalogue the AFP code is drawn from and which "
     "voluntary-contribution route (art. 55 RAIS voluntary contributions vs additional RPM "
     "contributions) is available. The CONTRIBUTION RATES are identical across the two regimes and "
     "are parameters (WTC)."),

    ("CCF Code",
     "Código de la caja de compensación familiar",
     "Institution code of the family compensation fund to which the employer is affiliated for this "
     "employee. Generally organised by department, so a multi-department employer legitimately "
     "carries more than one.",
     "M", "",
     "Text", "A(6) - administradoras catalogue; prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - three alphabetic positions naming the subsystem then three numeric positions naming the entity", "",
     "Spec ref: Employee.CCF_Code - CO-PILA-003 (T2R2-035, Mandatory=Y). EMPLOYER election (CCG "
     "Module 2.1), inherited by the employee, unlike the EPS and AFP which the employee chooses. "
     "The 4% levy is NEVER exonerated under ET art. 114-1."),

    ("Employee ARL Code",
     "Código de la administradora de riesgos laborales del afiliado",
     "Institution code of the occupational-risk insurer covering the employee.",
     "M", "",
     "Text", "A(6) - administradoras catalogue; prefix pattern ^(ARL|EPS|EOC|AFP|CCF|FSP)[0-9]{3}$ - three alphabetic positions naming the subsystem then three numeric positions naming the entity", "",
     "Spec ref: Employee.ARL_Code - CO-PILA-003 (T2R2-077, Mandatory=Y). EMPLOYER election, "
     "inherited by the employee. Normally equal to the employer ARL code; held per employee because "
     "the contribution-return layout carries both."),

    ("Severance-Savings Fund Code",
     "Código del fondo de cesantías del afiliado",
     "Code of the severance-savings fund the employee has chosen to receive the annual deposit. THE "
     "EMPLOYEE CHOOSES; affiliation is compulsory even where the employer pays severance savings "
     "directly under Labour Code art. 57 par. 4.",
     "M", "",
     "Text", "N(2) - published fund catalogue", "Severance-Savings Fund",
     "Spec ref: Employee.Cesantias_Fund_Code - CO-CESANTIAS-006 (T09, Mandatory=Y). IGNORED where "
     "the employer files a single-fund planilla, in which case the planilla-level fund overwrites "
     "this value for every record - see the employer field 'Single-Fund Planilla Severance Fund "
     "Code'. Any value outside the registered list is REJECTED."),

    ("Severance-Savings Regime",
     "Régimen de cesantías",
     "Which severance-savings regime the employee is under: the Ley 50 de 1990 annual-deposit "
     "regime (the default for everyone hired from 1 January 1991), the pre-1991 retroactive regime "
     "of the Labour Code, or none because the employee is on an all-inclusive salary.",
     "M", "",
     "Text", "LEY50 / TRADICIONAL / INTEGRAL", "Severance-Savings Regime",
     "Calculation-driving, and a documented reporting trap. Formulario 220 reports the pre-1991 "
     "regime at casilla 48 and the amount deposited to the fund at casilla 49, while Formato 2276 "
     "reports them in the OPPOSITE order at numerals N19 (fund) and N20 (traditional). MAP BY "
     "MEANING, NEVER BY POSITION - see CO-DIAN-004 and CO-DIAN-005 Field Options."),

    ("Severance-Savings Deposit Arrangement",
     "Modalidad de consignación de cesantías",
     "How the employee's severance savings are settled: the ordinary annual deposit to the fund by "
     "14 February, the monthly 8.33% advance deposit permitted by Ley 2466 de 2025 art. 64 under a "
     "written agreement, or direct payment to the employee discharging the deposit obligation under "
     "Labour Code art. 57 par. 4.",
     "CM",
     "Mandatory for every employee under the Ley 50 de 1990 regime. Where the value is MENSUAL a "
     "written agreement must be on file, and the monthly-advance fields of the deposit file are "
     "produced; where it is ANUAL only the ordinary annual detail record is produced.",
     "Text", "ANUAL / MENSUAL / DIRECTO / NA", "Severance-Savings Deposit Arrangement",
     "Spec ref: Contract.Cesantias_Regime (CO-CESANTIAS-006 MA01 'Acuerdo escrito para la "
     "consignación mensual anticipada', Mandatory=C) - the spec models the monthly-advance gate as "
     "a Y/N flag; this DD models the full four-way arrangement and MENSUAL is the value that maps "
     "to Y. LATE DEPOSIT COSTS ONE DAY'S SALARY PER DAY OF DELAY, PER EMPLOYEE, UNCAPPED (Ley 50 de "
     "1990 art. 99 num. 3)."),

    ("Foreign National Not Liable to Pension Flag",
     "Extranjero no obligado a cotizar a pensiones",
     "Indicates that the employee is a foreign national exempt from pension affiliation because "
     "affiliation to a pension system abroad has been proved (Decreto 1072 de 2015 art. "
     "2.2.1.2.1.4).",
     "CM",
     "Where set, the ONLY valid values of Employee Document Type are cédula de extranjería (CE), "
     "pasaporte (PA), carné diplomático (CD), salvoconducto (SC) and permiso especial de "
     "permanencia (PE). Bidirectional pair with Employee Document Type.",
     "Text", "S / N (emitted as blank or X on the PILA fixed-width file)", "Yes/No Indicator",
     "Spec ref: Employee.Foreign_Not_Pension_Liable_Flag - CO-PILA-003 (T2R2-007, Mandatory=C). "
     "Calculation-driving: suppresses the pension contribution only. Health, occupational risk and "
     "the payroll levies continue to apply. Requires documentary proof on file."),

    ("Concurrent Employer (Multi-Employer) Flag",
     "Cotizante con más de un empleador",
     "Indicates that the employee holds another concurrent employment. Where there are two or more "
     "employers, contributions are made PROPORTIONALLY to each remuneration and accumulate up to "
     "the shared 25-minimum-wage ceiling, and the health contribution must be made on the same base.",
     "CM",
     "Mandatory where the new joiner declares another concurrent employer. The other employer's "
     "contribution base must also be captured to apportion the shared ceiling.",
     "Text", "S / N", "Yes/No Indicator",
     "CCG Module 2.2 new-joiner declarations; Ley 100 de 1993 art. 18 par. 1 as substituted by Ley "
     "797 de 2003 art. 5. Calculation-driving switch. The other employer's BASE is a monetary input "
     "to the calculation and sits in the WTC / payroll-input set, not in this master-data field. "
     "Mis-configuration produces over- or under-contribution against the shared ceiling and is a "
     "standing UGPP audit exposure."),

    ("Principal Contributor Document Type",
     "Tipo de documento del cotizante principal",
     "Identity-document type of the principal contributor to whom a dependent-beneficiary record "
     "attaches on the contribution return.",
     "CM",
     "Populated ONLY for a dependent-beneficiary record - typically Worker Type 40, beneficiario "
     "UPC adicional. Bidirectional pair with the principal contributor's document number and with "
     "Worker Type.",
     "Text", "A(2) - PILA contributor document-type catalogue",
     "Employee Document Type (PILA / Cesantias)",
     "Spec ref: Employee.Main_Contributor_Doc_Type - CO-PILA-003 (T2R2-074, Mandatory=C). Uses the "
     "PILA two-letter CONTRIBUTOR catalogue, not the DIAN numeric one and not the EMPLOYER "
     "catalogue: the principal contributor is a natural person, so NI is not available here, "
     "while RC is (a beneficiary record may attach to a registro civil). Spec T2R2-074 points at "
     "the same Sheet 6 table as T2R2-003, 'Tipo documento cotizante'."),

    ("Principal Contributor Document Number",
     "Número de identificación del cotizante principal",
     "Identity-document number of the principal contributor to whom a dependent-beneficiary record "
     "attaches.",
     "CM",
     "Populated ONLY for a dependent-beneficiary record. Bidirectional pair with the principal "
     "contributor's document type.",
     "Text", "A(16) left-justified, space-filled", "",
     "Spec ref: Employee.Main_Contributor_Doc_Number - CO-PILA-003 (T2R2-075, Mandatory=C)."),
]

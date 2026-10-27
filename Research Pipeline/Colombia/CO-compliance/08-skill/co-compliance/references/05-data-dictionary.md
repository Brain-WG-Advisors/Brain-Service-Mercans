# Colombia - Data Dictionary (DD) - COMPLETE REFERENCE

**Source artifact:** `05-data-dictionary/CO-DD-001-v1.0.xlsx` (v1.0 of 2026-09-04, patched to **v1.1** on
2026-09-07 by the DD-to-Spec alignment patch)
**Format:** Mercans CZ V2.0 Data Dictionary template - all 8 sheets in template order.
**Jurisdiction:** Colombia (CO) - **Currency:** COP - **Fiscal year:** 2026

## Contents and totals

| Sheet | Content | Rows |
|---|---|---|
| 1. Version Control | change log (v1 initial + v1.1 alignment patch) | 2 entries |
| 2. Introduction | template introduction and table of contents | - |
| 3. Instructions | column-by-column instructions (template, verbatim) | 15 items |
| 4. ID Information | Colombia identification fields - employee + legal entity | **17 fields** |
| 5. Country Fields | Colombia country-specific data fields | **98 fields** |
| 6. Country Option Mappers | code tables consumed by the fields above | **35 mappers** (counted in the v1.0/v1.1 file) |
| 7. Currency Codes - ISO 4217 | template reference list (`DO NOT TOUCH`) | ISO 4217 |
| 8. Country Codes - ISO 3166-1 | template reference list (`DO NOT TOUCH`) | ISO 3166-1 alpha-2 |

**Field total: 115** (17 ID Information + 98 Country Fields), of which **53 M** (Mandatory) ·
**53 CM** (Conditional Mandatory) · **9 O** (Optional).

> **Count note [VERIFY WITH RA]:** the stage-07 QA report states *"30 option mappers"* and
> *"all 30 carrying a `Referenced by ...` reverse-reference"*. Counted directly in the delivered workbook there
> are **35** mappers: **32** carry an explicit `Referenced by <field> (Mandatory=...)` reverse-reference, and
> **3** are documented reference/generic mappers instead — `Social Security Subsystem` and
> `PILA Novedad (Change Event) Type` (*"Reference mapper for ..."*) and `Yes/No Indicator` (*"Generic two-value
> indicator referenced by every S/N master-data flag in this dictionary"*). The C16 intent is met in all 35
> cases; only the QA report's count is stale.

## Scope rules observed (verified by the QA cross-check, all PASS)

- **No amounts in the Data Dictionary.** Contractual monthly salary, salary-in-kind valuation, housing-loan
  interest, prepaid-health premiums, voluntary pension / AFC contributions and third-party meal payments are
  **deliberately absent**. Zero occurrences of SMMLV, UVT or any ceiling value anywhere in the DD.
- **No Base Salary field.**
- **Blue columns only.** The 12 orange system columns (`Ordinal`, `Internal Code`, `Parent Field Group` and its
  ordinal / internal code, `Sub Group` and its ordinal / internal code, `Default Value`, `MSS Field Permissions`,
  `ESS Field Permissions`) are intentionally **left blank** - they are populated at system-configuration time,
  not by compliance. Their headers are shown below with empty cells.
- **`Country Fields` starts at column B**, exactly as the CZ V2.0 template does.
- No Czech residue in Introduction or Instructions.

## Mandatoriness and traceability

- **53 fields are `CM` (Conditional Mandatory)** and **all 53** carry a populated
  `Pre-Condition for Conditional Mandatory` - control **C16**, 100%.
- **All 35 option mappers** are bidirectionally documented - 32 with an explicit
  `Referenced by <field> (Mandatory=...)` reverse-reference back to the consuming DD field, 3 as declared
  reference/generic mappers - the C16 bidirectional requirement, satisfied in full.
- **94 of 94** `DD`-bucket field tokens from the six report specs (`Employee.*`, `Company.*`, `Contract.*`,
  160 spec rows) are present here - **100%** 4-bucket reconciliation.
- 22 of the 115 DD fields carry **no** `Spec ref:` (Date of Birth, Gender, Nationality, weekly hours, days per
  week, obligatory rest day, 36-hour shift flag, work modality, withholding procedure, pension regime,
  severance regime, multi-employer flag and 10 others). Each is a CCG-Module-2-sourced calculation or
  configuration input that no *filing* carries - legitimately DD-only, not orphaned.

## Open QA items on this artifact

> **[QA MINOR-03]** `Country Option Mappers` rows 5 (code `11`, *Registro civil de nacimiento*) and 22 / 23 / 26
> (`CD` *Carne diplomatico*, `SC` *Salvoconducto*, `PT` *Permiso por Proteccion Temporal*) carry codes that
> `scope_manifest.json` -> `option_mapper_scope.personal_id_type` declares **out of scope** (its `_comment`
> states out-of-scope codes must be excluded from **all** artifacts). In mitigation the DD annotates each one
> (*"Under-7s; never an employee"*, *"CESANTIAS XLS LAYOUT ONLY"*) rather than presenting it as usable, and
> `CD` / `SC` / `PT` are genuinely in the published PILA and cesantias catalogues. **Read these four as
> REFERENCE ONLY - NOT IN SCOPE** until the manifest and the DD are reconciled.

> **[QA MINOR-11]** The **active-pensioner flag** has no discrete DD field. CCG Module 2 lists it as a
> social-security profile field and the WTC defines `CO-FLAG-PENSIONADO-ACTIVO`, but the DD carries it only
> through **`Worker Sub-Type` = `01`**, which is therefore its sole carrier. The manifest's
> `inbound_data_contract` also names it explicitly among the per-employee inputs the engine must receive.
> Functionally covered; formally under-specified.

**Colombia has NO separate social-security number.** The identity-document type + document number pair is the
key on every statutory artefact - see `Employee Document Type` / `Employee Document Number` and the PILA
`T2R2-003 + T2R2-004` composite key. **Colombia does not use IBAN** for domestic accounts.

---



---

## Sheet 1 - Version Control


**Data Dictionary**
**Colombia**


| Version | Effective Date | Change Description | Status | Updated By |
|---|---|---|---|---|
| 1 | 2026-09-04 | Initial version - Colombia Data Dictionary (private-sector master data), fiscal year 2026. Field set classified from the six in-scope report specifications in 04-reports-spec (CO-DIAN-001 nomina electronica, CO-DIAN-002 Formulario 350, CO-PILA-003, CO-DIAN-004 Formulario 220, CO-DIAN-005 Formato 2276, CO-CESANTIAS-006) by System Mapping, in lock-step with the spec col-E 'Payroll Field (Y/N)' flag (build_co_specs._DD_MASTER_MAPPINGS), and extended with the calculation-driving master-data groups of CCG Module 2.2 that do not surface on a filing (working time, withholding procedure, pension regime, concurrent employer, non-salary pact, work modality). ONE DELIBERATE DEVIATION from col-E lock-step: Contract.Contractual_Salary is flagged Payroll Field = Y in the specs but is an AMOUNT and is therefore excluded from the DD and routed to the Wage Type Catalogue, per the CLAUDE.md scope rule. Option mappers apply the private-sector filter: civil servants, military and police, independent workers and service contractors, domestic workers, community mothers, associated-work cooperative members and the self-insured are excluded, and the excluded codes are named in each mapper's Notes column so they are rejected at validation. Codes, lengths and masks are taken from the published Resolucion DIAN 000013 de 2021 Anexo Tecnico, Resolucion MSPS 2388 de 2016 Anexo Tecnico 2, Resolucion DIAN 000227 de 2025 and the published severance-deposit layouts; DERIVED items are flagged for RA confirmation in the Additional Notes. | Released | Mercans Compliance |
| 1.1 | 2026-09-07 | DD<->SPEC ALIGNMENT PATCH (mandatory pre-audit step), reconciling this Data Dictionary with the six Specs in 04-reports-spec. CROSS-REFERENCES: 49 field rows carried a stale or incomplete 'Spec ref' citation - a systematic off-by-N drift across the NIE, A1 and T2R blocks (for example Hire Date cited NIE057, which does not exist; the anexo field is NIE002 FechaIngreso, and the whole PILA employer block A1-011 to A1-017 was displaced by one). Every citation is now re-derived from the System Mapping join and states the artefact, the field ID and the Mandatory flag for each Spec that carries the field. OPTION MAPPERS: Worker Type code 40 (beneficiario de UPC adicional) REMOVED - it is absent from DIAN Anexo Tecnico table 5.5.3 and is a health-coverage beneficiary rather than an employee, so it could never be a valid NIE041 value; Employee Document Type code 47 abbreviation corrected to PEP, verbatim from Anexo table 5.2.1; the Worker Sub-Type hard rule aligned to the PILA statutory list (1, 2, 3, 4, 5, 6, 9, 12) with the in-scope subset named separately and the code-width trap recorded. NEW MAPPER 'Employee Document Type (PILA / Cesantias)' carrying the eight two-letter values of PILA Anexo Tecnico 2 campo 3 (CC, CE, TI, PA, CD, SC, RC, PE) plus the cesantias-only PT - this closes the contradiction in which CD and SC were named as valid in the numeric mapper's constraints but had no row, and gives PILA T2R2-003, T2R2-074 and CO-CESANTIAS-006 T03 a complete code table. Contract.Contractual_Salary remains OUT of the Data Dictionary as an amount; the deviation is now resolved at source, the spec build having been corrected to flag it Payroll Field = N, so this is no longer a deviation. OPTION-MAPPER ASSIGNMENT (CHECK 1): 'Principal Contributor Document Type' (CO-PILA-003 T2R2-074) was pointed at the mapper 'Employer Document Type', contradicting its own Pre-Defined Format and notes, which both say it takes the PILA two-letter CONTRIBUTOR catalogue. The two lists differ in exactly two places - the employer list carries NI and lacks RC - so the wrong mapper admitted a corporate NIT as a principal contributor's document type and rejected a registro civil, which is precisely the beneficiary case the field exists for. The field now references 'Employee Document Type (PILA / Cesantias)', matching Spec T2R2-074, which points at the same Sheet 6 table as T2R2-003; the employer mapper's own note, which had claimed T2R2-074 as a second referrer, is corrected. This also resolves the orphan-mapper finding for the contributor catalogue added earlier in this patch. CODE-PREFIX PATTERNS (CHECK 6): the seven administradora fields (employer ARL, employee ARL, EPS and EPS transfer, AFP and AFP transfer, CCF) stated only 'A(6) - administradoras catalogue' in Pre-Defined Format while the Specs stated the full six-position prefix pattern; the pattern ^(ARL\|EPS\|EOC\|AFP\|CCF\|FSP)[0-9]{3}$ is now carried on both sides so the two documents describe the same format. The severance-savings fund code is deliberately left at N(2), being a different published catalogue. Full record: 07-qa-crosscheck/CO-ALIGNMENT-PATCH.md. | Released | Mercans Compliance |


**Business Analyst**
**Regulation Analyst**



---

## Sheet 2 - Introduction


**Table of Contents:**


| # | Section | Description |
|---|---|---|
| 1 | Instructions | Please read this section first. |
|  | ID Information | List of country-specific ID fields. |
|  | Country Fields | List of country-specific data fields, including employee fields and legal entity fields. |
|  | Country Option Mappers | List of country option mappers. |
|  | Currency Codes | ISO currency codes. No action required. |
|  | Country Codes | ISO country codes. No action required. |



---

## Sheet 3 - Instructions (template, verbatim)


**Instructions**


| Item | Value |
|---|---|
| Field Name | Instructions/Descriptions |
| Field Group | Mercans' field group name. The values in this field should not be updated. |
| Field Name | Data field name in Mercans' system. This field should be updated only for the field in the Implementation-Specific Fields tab. The values in this field are not always the same as the actual database field names. |
| Internal Code | Mercans' data field code. This field is used to map Client's data against Mercans fields. |
| Label in Local Language | Field name in the local language and should reflect the same terminology as used on statutory forms or local language reports. |
| Field Description (Long Description of the Field) | Include a full description of the respective data field. |
| Data Type - Mandatory (M), Conditional Mandatory (CM), Optional (O) | The values of this field should not be updated for Universal or Country-Specific Fields. Each Implementation-Specific Fields must be categorized as a either Mandatory, Conditional Mandatory or Optional fields. Mandatory fields must be filled for each employee record and Conditional Mandatory fields only if a certain condition is met. |
| Pre-Condition for Conditional Mandatory | This field should be filled for all data fields identified as Conditional-Minatory. It should include the condition that makes the respective field mandatory. |
| Field Type (Text, Number, Date, Integer, Decimal, Counter) | Available field type options are Text, Number, Date, Integer, Decimal, and Counter. Each field must include a field type. |
| Pre-Defined Format | Field format should be provided for the fields that must be in specific formats; i.e. (999) 123-4567, etc. |
| Validations, Restrictions, Pick Lists etc. | Field-specific validations are defined in this field. Validations can include specific pick lists, length validations, etc. |
| Default Value | A default value should be filled for each record if no other value is applicable. |
| MSS Field Permissions | For each field identify whether the field is not visible/available (hidden), visible but not editable (view) or editable (edit) through Payroll Administrator Console (PAC). Further field specific access restrictions can be defined based on PAC user roles and access rights. |
| ESS Field Permissions | For each field identify whether the field is not visible/available (hidden), visible but not editable (view) or editable (edit) through Employee Self Service (ESS) by employees for their own records. |
| Additional Notes | Include any additional clarifications or notes here. |



---

## Sheet 4 - ID Information (17 fields: employee + legal entity)


**Identification Information**


| Country | Ordinal | Field Name | Internal Code | Label in Local Language | Field Description (Long Description of the Field) | Data Type  -Mandatory (M), Conditional Mandatory (CM), Optional (O) | Pre-Condition for Conditional Mandatory | Field Type (Text, Number, Date, Integer, Decimal, Counter) | Pre-Defined Format | Option Mapper | Validations, Restrictions, Pick Lists etc. | Parent Field Group | Ordinal of Parent Field Group | Internal Code of Parent Field Group | Sub Group under Parent Field Group | Ordinal of Sub Group under Parent Field Group | Internal Code of Sub Group under Parent Field Group | Default Value | MSS Field Permissions (Read, Write) | ESS Field Permissions (Read, Write) | Additional Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colombia |  | Employee Document Type |  | Tipo de documento de identificación del trabajador | Coded identity-document type of the employee. Colombia issues NO separate social-security number: the document type plus the document number IS the composite key across the electronic payroll XML, the integrated contribution return (PILA), Formulario 220 and Formato 2276. The code system differs by artefact - DIAN filings use the numeric catalogue (13 = cédula de ciudadanía) while PILA and the severance-savings deposit file use the two-letter catalogue (CC). One master value; the engine emits the artefact's own code. | M |  | Text | N(2) DIAN numeric catalogue; emitted as A(2) alpha on PILA and cesantías | Employee Document Type |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Document_Type - CO-DIAN-001 (NIE044, Mandatory=Y), CO-PILA-003 (T2R2-003, Mandatory=Y), CO-DIAN-004 (casilla 24, Mandatory=Y), CO-DIAN-005 (numeral N02, Mandatory=Y), CO-CESANTIAS-006 (T03, Mandatory=Y). The nomina electronica code list is Anexo Tecnico table 5.2.1. Scope option_mapper_scope.personal_id_type. Validates the length of the document NUMBER - a PEP must be exactly 15 digits (SOI hard rule). CO-GAP-06: no code exists for the PPT (Permiso por Protección Temporal, Decreto 216 de 2021); code 47 (PEP) is the only available proxy. |
| Colombia |  | Employee Document Number |  | Número de identificación del trabajador | Identity-document number of the employee, without dots, hyphens, spaces or a verification digit. Primary per-employee key on every Colombian statutory filing and the social-security identifier. | M |  | Text | Numeric, no separators (cédula 8-10 digits; PEP exactly 15). Alphanumeric only for passport (41), foreign identity document (42) and foreign tax number (50) |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Document_Number - CO-DIAN-001 (NIE045, Mandatory=Y), CO-PILA-003 (T2R2-004, Mandatory=Y), CO-DIAN-004 (casilla 25, Mandatory=Y), CO-CESANTIAS-006 (T04, Mandatory=Y). Field widths differ by artefact: A(16) space-filled on PILA, N(16) zero-filled on the cesantias deposit file. CO-GAP-07 (SCHEMA TRAP): NIE045 is typed xsd:integer in the nómina electrónica XSD, so an alphanumeric passport number cannot be schema-valid. No official workaround published - carry as an open item. |
| Colombia |  | Employee Bank Name |  | Banco | Name of the bank holding the employee's salary account. Reported on the electronic payroll support document whenever the payment medium is bank-mediated. | CM | Mandatory where Payment Method is a bank-mediated medium (42, 45, 47, 48, 49). Must be absent or empty where Payment Method = 10 (efectivo). | Text | Free text |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Bank_Name - CO-DIAN-001 (NIE066, Mandatory=C). Bidirectional set with Payment Method, Bank Account Type and Bank Account Number. |
| Colombia |  | Employee Bank Account Type |  | Tipo de cuenta | Type of the employee's salary bank account - savings or current. Colombia has only these two. | CM | Mandatory together with Employee Bank Name and Employee Bank Account Number where Payment Method is a bank-mediated medium. | Text | AHORROS / CORRIENTE | Bank Account Type |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Bank_Account_Type - CO-DIAN-001 (NIE067, Mandatory=C). |
| Colombia |  | Employee Bank Account Number |  | Número de cuenta | Employee salary account number. COLOMBIA DOES NOT USE IBAN. Domestic account numbers are numeric, of bank-specific length (commonly 10-17 digits), with no national check-digit standard. | CM | Mandatory together with Employee Bank Name and Employee Bank Account Type where Payment Method is a bank-mediated medium. | Text | Numeric, bank-specific length (commonly 10-17 digits). NOT an IBAN. |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Bank_Account_Number - CO-DIAN-001 (NIE068, Mandatory=C). CCG Module 2.2 confirms no IBAN and no national check digit - do not apply an IBAN validator. |
| Colombia |  | Employee Internal Code |  | Código del trabajador | Employer's own internal employee number. Optional on the electronic payroll support document; used by the employer to reconcile the document to its own personnel records. | O |  | Text | Free text (employer-defined) |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Internal_Code - CO-DIAN-001 (NIE009 and NIE063, Mandatory=N). Not the document number and not a substitute for it. |
| Colombia |  | Severance-Savings Fund Account Number |  | Número de cuenta del fondo de cesantías | Account number held by the employee at the chosen severance-savings fund, used on the annual severance deposit file. | CM | Mandatory where the fund requires an account number on the deposit file; otherwise the employee is identified by document type plus document number validated against the Asofondos affiliate base. | Text | Fund-specific numeric/alphanumeric |  |  |  |  |  |  |  |  |  |  |  | Declared in build_co_specs._DD_MASTER_MAPPINGS as Employee.Cesantias_Fund_Account but not carried as a positional field in the published Simple S.A. / SOI layout, which keys the record on document type + number. DERIVED - confirm per-fund requirement with RA. |


**Country-Specific Legal Entity Fields**


| Country | Ordinal | Field Name | Internal Code | Label in Local Language | Field Description (Long Description of the Field) | Data Type  -Mandatory (M), Conditional Mandatory (CM), Optional (O) | Pre-Condition for Conditional Mandatory | Field Type (Text, Number, Date, Integer, Decimal, Counter) | Pre-Defined Format | Option Mapper | Validations, Restrictions, Pick Lists etc. | Parent Field Group | Ordinal of Parent Field Group | Internal Code of Parent Field Group | Sub Group under Parent Field Group | Ordinal of Sub Group under Parent Field Group | Internal Code of Sub Group under Parent Field Group | Default Value | MSS Field Permissions (Read, Write) | ESS Field Permissions (Read, Write) | Additional Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colombia |  | Employer NIT |  | NIT del empleador | Tax identification number assigned by DIAN on registration in the Single Tax Registry (RUT). Primary employer key on every Colombian statutory artefact. Stored and transmitted WITHOUT dots, hyphens or the verification digit. | M |  | Text | N(9) to N(10) - no dots, no hyphens, no verification digit |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.NIT - CO-DIAN-001 (NIE033, Mandatory=Y), CO-DIAN-002 (casilla 5, Mandatory=Y), CO-DIAN-004 (casilla 5, Mandatory=Y), CO-DIAN-005 (numeral ENV-01, Mandatory=Y). Validation rules NIE038 and NIE041 require the number 'sin guiones ni DV' in one attribute and the verification digit in another - an engine that concatenates them FAILS schema validation. The last digit(s) of the NIT also fix the filing deadline for Formulario 350, PILA and the información exógena. |
| Colombia |  | Employer NIT Verification Digit (DV) |  | Dígito de verificación (DV) del NIT | Single-digit verification digit of the employer NIT, computed by DIAN using a weighted modulus-11 algorithm. ALWAYS A SEPARATE FIELD from the NIT itself. | M | On the contribution return the value is mandatory where Employer Person Type = J (jurídica); for every other case the field must be ZERO. | Text | N(1), 0 to 9 |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.NIT_DV - CO-DIAN-001 (NIE034, Mandatory=Y), CO-DIAN-002 (casilla 6, Mandatory=Y), CO-PILA-003 (A1-004 and T2R1-007, Mandatory=C/Y), CO-DIAN-004 (casilla 6, Mandatory=Y). Verified algorithm (CCG Module 2.1): weights [3,7,13,17,19,23,29,37,41,43,47,53,59,67,71] applied right to left, S = sum(digit_i x W_i), R = S mod 11, DV = R if R < 2 else 11 - R. Verified against NIT 902025831 -> DV 4 and NIT 800197268 -> DV 4. Stored, not recomputed at runtime, but validated on entry. |
| Colombia |  | Employer Document Type |  | Tipo de documento del aportante | Identity-document type of the employer on the integrated contribution return. A corporate employer is NI (número de identificación tributaria); a natural-person employer uses a personal document type. | M |  | Text | A(2) - PILA employer document-type catalogue | Employer Document Type |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Document_Type - CO-PILA-003 (A1-002 and T2R1-005, Mandatory=Y) and CO-CESANTIAS-006 (E01, Mandatory=Y), the latter as the composite Company.Document_Type + Company.Document_Number ('Tipo y número de documento del aportante') on CO-CESANTIAS-006. Where Employer Person Type = N (natural) the type NI is NOT available. Company.Document_Number (CO-PILA-003 A1-003 and T2R1-006, A(16)) is NOT a separate master-data field: for a legal person it is the Employer NIT and for a natural person it is the personal document number - hold the value once and emit it into whichever field the artefact requires. |
| Colombia |  | Employer Commercial Registration Number |  | Número de matrícula mercantil | Commercial registration number issued by the Chamber of Commerce of the municipality of domicile. | CM | Mandatory for commercial entities and for any employer claiming the Ley 1429 de 2010 formalisation benefits or the Ley 2466 de 2025 art. 34 part-time contribution regime. | Text | Alphanumeric - format set by each Chamber of Commerce |  |  |  |  |  |  |  |  |  |  |  | CCG Module 2.1. One of only three sub-national registration elements in Colombian payroll (the others being the family compensation fund and the work-centre risk class). DERIVED format - the Chambers do not publish a common mask; confirm with RA. |
| Colombia |  | DIAN Electronic Payroll Software Identifier |  | Identificador del software (SoftwareID) | Identifier assigned by DIAN when the employer's payroll software is activated for the electronic payroll support document. Together with a secret PIN it produces the CUNE security code carried in every document. | M |  | Text | String assigned by DIAN at software activation |  |  |  |  |  |  |  |  |  |  |  | CCG Module 2.1; Res. DIAN 000013 de 2021 arts. 1, 5, 22. THE PAIRED PIN IS A CREDENTIAL: it never appears in the XML and is held in the integration credential store described in CO-SIR-001, NOT in this Data Dictionary. The security code itself (SHA-384 of SoftwareID + PIN + document number) is a COMPUTED value (SYS), not master data. |
| Colombia |  | Electronic Payroll Document Prefix |  | Prefijo de numeración de la nómina electrónica | Employer-defined prefix of the electronic payroll document number. The document number is the prefix plus a consecutive sequence and must be unique per employee. | M |  | Text | Employer-defined alphanumeric prefix |  |  |  |  |  |  |  |  |  |  |  | CCG Module 2.1. The CONSECUTIVE NUMBER is generated by the engine (SYS), not master data. DIAN global validation rule 90 rejects a repeated document number for the same employee; a rejected document must be re-transmitted with a NEW consecutive number. |
| Colombia |  | Information Operator Code |  | Código del operador de información | Code of the licensed private information operator through which the integrated contribution return is filed and paid. The employer NEVER transacts directly with the government for social security. | M |  | Text | N(2) - assigned by the operador's own system |  |  |  |  |  |  |  |  |  |  |  | Spec ref: CO-PILA-003 Field Options ('Código del operador de información', 2 digits). CCG Module 2.1 item 9 - an employer-level election stored once and inherited by every employee. Operadores are private entities licensed by the Ministerio de Salud y Protección Social. |
| Colombia |  | Legal Representative Document Type |  | Tipo de identificación del representante legal | Identity-document type of the employer's legal representative, who signs the contribution return and the withholding-tax return. | CM | Mandatory where Employer Person Type = J (jurídica); optional where Employer Person Type = N (natural). Bidirectional pair with Employer Person Type. | Text | A(2) - narrower catalogue than the contributor list | Legal Representative Document Type |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Legal_Rep_ID_Type - CO-PILA-003 (A1-020, Mandatory=C). NI, TI, SC, PE and RC are NOT available for a legal representative even though several of them are available for a contributor. |
| Colombia |  | Legal Representative Identification Number |  | Número de identificación del representante legal / signatario | Identity-document number of the legal representative or signatory of the return. | CM | Mandatory where Employer Person Type = J (jurídica); optional where Employer Person Type = N. Bidirectional pair with Employer Person Type and with the legal-representative name block. | Text | A(16) on PILA, left-justified and space-filled; numeric on Formulario 350 |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Legal_Rep_ID - CO-DIAN-002 (casilla 139, Mandatory=Y), CO-PILA-003 (A1-018, Mandatory=C). |
| Colombia |  | Legal Representative Verification Digit |  | DV del signatario | Verification digit of the legal representative's or signatory's identification number. | CM | Populated wherever the signatory identification number is populated. | Text | N(1), 0 to 9 |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Legal_Rep_ID_DV - CO-DIAN-002 (casilla 140, Mandatory=Y), CO-PILA-003 (A1-019, Mandatory=Y). Same weighted modulus-11 algorithm as the employer NIT DV. |



---

## Sheet 5 - Country Fields (98 Colombia-specific fields)


**Country-Specific Fields**


| Country | Ordinal | Field Name | Internal Code | Label in Local Language | Field Description (Long Description of the Field) | Data Type  -Mandatory (M), Conditional Mandatory (CM), Optional (O) | Pre-Condition for Conditional Mandatory | Field Type (Text, Number, Date, Integer, Decimal, Counter) | Pre-Defined Format | Option Mapper | Validations, Restrictions, Pick Lists etc. | Parent Field Group | Ordinal of Parent Field Group | Internal Code of Parent Field Group | Sub Group under Parent Field Group | Ordinal of Sub Group under Parent Field Group | Internal Code of Sub Group under Parent Field Group | Default Value | MSS Field Permissions (Read, Write) | ESS Field Permissions (Read, Write) | Additional Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colombia |  | Employee First Surname |  | Primer apellido | First (paternal) surname of the employee as registered with the civil authorities. | M |  | Text | A(20) on PILA and cesantías; variable length on the DIAN artefacts |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.First_Surname - CO-DIAN-001 (NIE046, Mandatory=Y), CO-PILA-003 (T2R2-011, Mandatory=Y), CO-DIAN-004 (casilla 26, Mandatory=Y), CO-DIAN-005 (numeral N03, Mandatory=Y), CO-CESANTIAS-006 (T05, Mandatory=Y). Validated as a SET with the other three name parts against the Asofondos affiliate base on the cesantías deposit. |
| Colombia |  | Employee Second Surname |  | Segundo apellido | Second (maternal) surname of the employee. | CM | The nómina electrónica schema declares this a REQUIRED attribute even though many Colombians and virtually all foreign nationals have only one surname. Where the person has no second surname a placeholder must be emitted or schema validation fails. Space-filled on the PILA and cesantías fixed-width layouts. | Text | A(20) on PILA and cesantías; variable length on the DIAN artefacts |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Second_Surname - CO-DIAN-001 (NIE047, Mandatory=Y), CO-PILA-003 (T2R2-012, Mandatory=Y), CO-DIAN-004 (casilla 27, Mandatory=Y), CO-CESANTIAS-006 (T06, Mandatory=Y). SCHEMA TRAP recorded in CCG Module 2.2: no official guidance exists on the placeholder value. Carry as an open item and agree the placeholder with RA before go-live. |
| Colombia |  | Employee First Name |  | Primer nombre | First given name of the employee. | M |  | Text | A(20) on PILA and cesantías; variable length on the DIAN artefacts |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.First_Name - CO-DIAN-001 (NIE048, Mandatory=Y), CO-PILA-003 (T2R2-013, Mandatory=Y), CO-DIAN-004 (casilla 28, Mandatory=Y), CO-CESANTIAS-006 (T07, Mandatory=Y). |
| Colombia |  | Employee Other Names |  | Otros nombres | Second and any further given names of the employee. | CM | Conditional on the person having a second or further given name; space-filled on the fixed-width layouts when absent. | Text | A(20) on PILA and cesantías; A(30) on the PILA employer block; variable on DIAN |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Other_Names - CO-DIAN-001 (NIE049, Mandatory=N), CO-PILA-003 (T2R2-014, Mandatory=N), CO-DIAN-004 (casilla 29, Mandatory=N), CO-CESANTIAS-006 (T08, Mandatory=C). PILA calls the field 'Segundo nombre'; the nómina electrónica calls it 'OtrosNombres' and accepts more than one given name in the single attribute. |
| Colombia |  | Date of Birth |  | Fecha de nacimiento | Employee date of birth. Not reported on any of the six in-scope statutory filings, but held as onboarding master data because it drives the identity-document path: a worker aged 15-17 holds a tarjeta de identidad (code 12) which converts to a cédula de ciudadanía (code 13) on majority - a change of the document-type + number composite key that must be actioned. | O |  | Date | AAAA-MM-DD |  |  |  |  |  |  |  |  |  |  |  | Not filing-mandated on the in-scope returns. CCG Module 2.2 records the minor-to-adult document-type change. Retirement age (57 women / 62 men, public defined-benefit regime) affects entitlement, not the payroll rate - see CCG Module 5. |
| Colombia |  | Gender |  | Sexo | Employee gender. Standard onboarding demographic; Colombia does not vary any payroll rate, threshold or contribution by gender. | O |  | Text | M / F | Gender |  |  |  |  |  |  |  |  |  |  | Not reported on any of the six in-scope statutory filings and not a calculation driver. Held for HR master data and affiliation paperwork only. |
| Colombia |  | Nationality |  | Nacionalidad | Employee nationality. Drives the identity-document path (Colombian national -> cédula de ciudadanía 13; resident foreign national -> cédula de extranjería 22; non-resident -> passport 41) and, together with proof of affiliation to a foreign pension system, the foreign-national pension-waiver flag. | M |  | Text | ISO 3166-1 alpha-2 (e.g. CO) | ISO 3166-1 (see the 'Country Codes - ISO 3166-1' sheet) |  |  |  |  |  |  |  |  |  |  | Calculation-driving classifier. NOT the same question as Tax Residence Status: a Colombian national can be a non-resident and a foreign national can be a resident. Keep the two fields independent - see CCG Module 2.2 and the resident/non-resident matrix at Module 6.2. |
| Colombia |  | Employee Residential Address |  | Dirección de residencia del trabajador | Residential address of the employee, as reported on the annual severance-savings deposit file. | CM | Mandatory on the annual severance-savings deposit record. Must be consistent with the residence department and municipality codes, which are the DANE halves of the same address. | Text | CHAR(50) |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Address - CO-CESANTIAS-006 (T15, Mandatory=C). DISTINCT from Place of Work Address - the nómina electrónica reports where the employee WORKS, this reports where the employee LIVES. Do not map one to the other. |
| Colombia |  | Residence Department Code |  | Código del departamento de residencia | Two-digit DANE DIVIPOLA department code of the employee's residential address. | CM | Mandatory wherever the residential address is reported. Must be the department half of the same five-digit DIVIPOLA code whose municipality half is the residence municipality code. | Text | N(2) DANE DIVIPOLA |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Department_Code - CO-DIAN-005 (numeral N04, Mandatory=Y), CO-CESANTIAS-006 (T16, Mandatory=C). Use the DANE DIVIPOLA catalogue, NOT the ISO 3166-2:CO list on the reference sheets. |
| Colombia |  | Residence Municipality Code |  | Código del municipio de residencia | Three-digit DANE DIVIPOLA municipality suffix of the employee's residential address. | CM | Mandatory wherever the residential address is reported. Must be the municipality half of the same five-digit DIVIPOLA code whose department half is the residence department code. | Text | N(3) DANE DIVIPOLA suffix (e.g. 001 for Bogotá D.C. within department 11) |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Municipality_Code - CO-CESANTIAS-006 (T17, Mandatory=C). SPLIT-CODE TRAP: PILA, Formulario 220 and the cesantías file carry the department and municipality in SEPARATE 2 + 3 fields, whereas the nómina electrónica carries ONE five-digit code (11001). Store the five digits once and split on output. |
| Colombia |  | Employee E-mail Address |  | Correo electrónico del trabajador | Employee e-mail address, reported on the annual severance-savings deposit file and used for payslip and certificate delivery. | CM | Conditional on an e-mail address being held for the employee. | Text | CHAR(50) |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Email - CO-CESANTIAS-006 (T19, Mandatory=C). |
| Colombia |  | Employee Landline Telephone |  | Teléfono fijo del trabajador | Seven-digit landline telephone number of the employee, as required by the severance-savings deposit layout. | CM | Conditional on a 7-digit landline being held; the layout is filled with spaces or zeros where only a mobile number exists. | Text | N(7) |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Phone - CO-CESANTIAS-006 (T18, Mandatory=C). The layout has no mobile-number field - a mobile number cannot be substituted. |
| Colombia |  | Colombian Abroad Flag |  | Colombiano en el exterior | Indicates that the employee is a Colombian national performing the work outside Colombia. Where set, the work-location department and municipality must be left BLANK on the contribution return. | CM | Usable ONLY where Employee Document Type is cédula de ciudadanía (13 / CC) or tarjeta de identidad (12 / TI). Where set, Place of Work Department Code and Place of Work Municipality Code must be blank. | Text | S / N (emitted as blank or X on the PILA fixed-width file) | Yes/No Indicator |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Colombian_Abroad_Flag - CO-PILA-003 (T2R2-008, Mandatory=C). Bidirectional set with Employee Document Type and the two work-location codes. |
| Colombia |  | Place of Work Country Code |  | País del lugar de trabajo | Country in which the employee performs the work. A required attribute of the worker element on the electronic payroll support document. | M |  | Text | ISO 3166-1 alpha-2 (Anexo Técnico table 5.4.1) | ISO 3166-1 (see the 'Country Codes - ISO 3166-1' sheet) |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Work_Country_Code - CO-DIAN-001 (NIE050, Mandatory=Y). For a transnational teleworker a Colombian contract remains governed by Colombian law and the ARL must guarantee cover in the country of performance - Ley 2466 de 2025 art. 54, CCG Module 11. |
| Colombia |  | Place of Work Department Code |  | Departamento del lugar de trabajo | Two-digit DANE DIVIPOLA department code of the place where the employee performs the work. | CM | Mandatory on the nómina electrónica. Left BLANK on the contribution return where the Colombian Abroad Flag is set, and where Worker Type = 40 (beneficiario UPC adicional). | Text | N(2) DANE DIVIPOLA (Anexo Técnico table 5.4.2) |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Work_Department_Code - CO-DIAN-001 (NIE051, Mandatory=Y), CO-PILA-003 (T2R2-009, Mandatory=C). Bidirectional set with the Colombian Abroad Flag and Worker Type. |
| Colombia |  | Place of Work Municipality Code |  | Municipio del lugar de trabajo | DANE DIVIPOLA municipality of the place where the employee performs the work. | CM | Mandatory on the nómina electrónica. Left BLANK on the contribution return in the same two cases as the work-location department code - Colombian Abroad Flag set, or Worker Type = 40. | Text | N(5) full DIVIPOLA on the nómina electrónica (11001); N(3) municipality suffix on PILA |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Work_Municipality_Code - CO-DIAN-001 (NIE052, Mandatory=Y), CO-PILA-003 (T2R2-010, Mandatory=C). SPLIT-CODE TRAP - see Residence Municipality Code. Store five digits once and split on output. |
| Colombia |  | Place of Work Address |  | Dirección del lugar de trabajo | Street address of the place where the employee performs the work. A required attribute of the worker element on the electronic payroll support document. | M |  | Text | Free text |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Work_Address - CO-DIAN-001 (NIE053, Mandatory=Y). DISTINCT from the employee's residential address. |
| Colombia |  | Work Centre Code |  | Centro de trabajo | Employer-assigned code of the work centre to which the employee is attached. The occupational-risk CLASS attaches to the WORK CENTRE, not to the company, so this field selects the risk class - and therefore the occupational-risk rate - that applies to the employee. | CM | Mandatory where the employer operates more than one work centre, and mandatory where the VCT change-of-work-centre event is reported for the period. | Text | N(9) zero-filled to the left |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Work_Centre_Code - CO-PILA-003 (T2R2-062, Mandatory=C). Bidirectional set with the VCT novedad and with the work centre's Occupational Risk Class. Legal basis: Decreto 1072 de 2015 art. 2.2.4.2.5.6 - a company with a corporate office and a plant legitimately carries two different risk classes. The RATE itself is a parameter (WTC), not DD. |
| Colombia |  | Hire Date |  | Fecha de ingreso del trabajador | Date on which the employment relationship with the declaring employer commenced. | M |  | Date | AAAA-MM-DD |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Contract.Start_Date - CO-DIAN-001 (NIE002, Mandatory=Y), CO-PILA-003 (T2R2-080, Mandatory=C), CO-CESANTIAS-006 (T20, Mandatory=Y). On PILA the field is mandatory where the ING novedad is marked. Seniority driver for the severance-savings liquidation, the indemnity tier and work-clothing eligibility. Colombia has NO cumulative-withholding carry-over between employers and no P45 equivalent - a new employer starts the withholding calculation fresh (CCG Module 2.2). |
| Colombia |  | Termination Date |  | Fecha de retiro del trabajador | Date on which the employment relationship ended. | CM | Mandatory upon a leaver event: populated on the nómina electrónica only for the month in which the relationship ends, and mandatory on the contribution return where the RET (retiro) novedad is marked. | Date | AAAA-MM-DD |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Contract.End_Date - CO-DIAN-001 (NIE003, Mandatory=C), CO-PILA-003 (T2R2-081, Mandatory=C). Bidirectional pair with the RET novedad. Must fall inside or before the settlement window of the document. |
| Colombia |  | Contract Type |  | Tipo de contrato | Type of employment contract. Five values in the private-sector population: fixed-term (maximum four years after Ley 2466 de 2025 art. 6), indefinite-term, specific work or task, apprenticeship and internship. | M |  | Text | N(1) - code 1 to 5 (Anexo Técnico table 5.5.2) | Contract Type |  |  |  |  |  |  |  |  |  |  | Spec ref: Contract.Type_Code - CO-DIAN-001 (NIE061, Mandatory=Y). Scope option_mapper_scope.contract_type. Ley 2466 de 2025 art. 21 recast the apprenticeship as a special fixed-term LABOUR contract, regulated by Decreto 0223 of 5 March 2026 - it is now a contract type, not a training arrangement. |
| Colombia |  | Worker Type |  | Tipo de trabajador / tipo de cotizante | Contributor category of the employee. Selects the contribution rules that apply on the integrated contribution return and on the electronic payroll support document. | M |  | Text | N(2) zero-filled - e.g. 01 (Anexo Técnico table 5.5.3 / PILA tipo cotizante) | Worker Type |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Worker_Type_Code - CO-DIAN-001 (NIE041, Mandatory=Y), CO-PILA-003 (T2R2-005, Mandatory=Y). MAPPING TRAP: the nómina electrónica table 5.5.3 carries only SIXTEEN values while the PILA tipo cotizante list carries far more - copying a PILA code straight into the XML is a documented failure. Public-sector codes 18, 30, 47 and 58, domestic service 02, community mothers 04, associated-work cooperative members 31 and every independent-worker code are OUT OF SCOPE - see the mapper Notes. |
| Colombia |  | Worker Sub-Type |  | Subtipo de trabajador / subtipo de cotizante | Contributor sub-category. The value that matters for corporate payroll is 01 - an employed old-age pensioner in active service, who makes NO pension contribution. | M |  | Text | N(2) zero-filled - 00 where no sub-type applies | Worker Sub-Type |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Worker_SubType_Code - CO-DIAN-001 (NIE042, Mandatory=Y), CO-PILA-003 (T2R2-006, Mandatory=Y). HARD RULE: where the sub-type is 01, 02, 03, 04, 05, 06, 09 or 12 the PILA pension-contribution rate field MUST be 0. This field carries the 'active pensioner' attribute - do NOT create a separate active-pensioner flag. MAPPING TRAP: the nómina electrónica table 5.5.4 carries only 00 and 01; PILA carries more. |
| Colombia |  | Pay Frequency |  | Periodo de nómina | Frequency at which salary is paid. Labour Code art. 134 caps the interval at one month for monthly salaries and one week for day wages; any shorter frequency is permitted. | M |  | Text | N(1) - code 1 to 6 (Anexo Técnico table 5.5.1) | Pay Frequency |  |  |  |  |  |  |  |  |  |  | Spec ref: Contract.Pay_Frequency_Code - CO-DIAN-001 (NIE029, Mandatory=Y). CRITICAL CONFIGURATION POINT: whatever the frequency, the electronic payroll support document is ONE MONTHLY document per employee - Res. DIAN 000013 de 2021 art. 3, 'con independencia de que el obligado realice pagos en periodos diferentes o inferiores'. A semi-monthly payroll does NOT produce two filings a month. |
| Colombia |  | Payment Form |  | Forma de pago | Settlement form of the payroll payment. The Anexo Técnico publishes a single value - contado (immediate settlement). | M |  | Text | N(1) - code 1 (Anexo Técnico table 5.3.3.1) | Payment Form |  |  |  |  |  |  |  |  |  |  | Spec ref: Contract.Payment_Form_Code - CO-DIAN-001 (NIE064, Mandatory=Y). Distinct from Payment Method - 'forma' is cash-vs-credit settlement, 'método' is the medium. |
| Colombia |  | Payment Method |  | Medio de pago | Medium through which the net salary is paid. Drives whether the bank block (bank name, account type, account number) must be populated. | M |  | Text | N(2) - UN/EDIFACT 4461 code (Anexo Técnico table 5.3.3.2) | Payment Method |  |  |  |  |  |  |  |  |  |  | Spec ref: Contract.Payment_Method_Code - CO-DIAN-001 (NIE065, Mandatory=Y). Bidirectional set with the three bank fields: where the value is 10 (efectivo) the bank attributes must be ABSENT; where it is a bank-mediated medium they are all required. |
| Colombia |  | Weekly Contracted Hours |  | Jornada semanal contratada | Contracted ordinary weekly working hours. The statutory maximum steps DOWN during fiscal year 2026: 44 hours to 14 July 2026 and 42 hours from 15 July 2026. | M |  | Decimal | Hours per week, up to 2 decimals (e.g. 42.00) |  |  |  |  |  |  |  |  |  |  |  | CCG Module 2.2 working-time group. Calculation-driving: the ordinary hourly rate, and therefore every overtime and night-surcharge value, is derived from it. NOT on any in-scope statutory filing - held as a calculation input. The 42-hour step is a PARAMETER (WTC); this field is the employee's contracted value. |
| Colombia |  | Days Worked Per Week |  | Días laborados por semana | Number of ordinary working days in the employee's week - five or six. | M |  | Integer | 5 or 6 |  |  |  |  |  |  |  |  |  |  |  | CCG Module 2.2 working-time group. Together with the obligatory rest day it determines which days attract the Sunday / public-holiday surcharge. Not on any in-scope statutory filing. |
| Colombia |  | Obligatory Rest Day |  | Día de descanso obligatorio | Weekday designated as the employee's obligatory paid rest day. SUNDAY IS PRESUMED unless a written agreement designates another day. | M |  | Text | Weekday name (default: Domingo) |  |  |  |  |  |  |  |  |  |  |  | CCG Module 2.2. Calculation-driving: the Sunday / public-holiday surcharge attaches to the designated rest day, not automatically to the calendar Sunday. Default value: Domingo. |
| Colombia |  | 36-Hour Shift System Flag |  | Jornada por turnos sucesivos de 36 horas | Indicates that the employee works the successive-shift regime, which has its own weekly-hours and surcharge treatment. | O |  | Text | S / N | Yes/No Indicator |  |  |  |  |  |  |  |  |  |  | CCG Module 2.2 working-time group. Calculation-driving where set. Not on any in-scope statutory filing. |
| Colombia |  | Work Modality (Telework / On-Site) |  | Modalidad de trabajo (teletrabajo / presencial) | Working modality of the employee. A teleworker earning less than two minimum wages receives the MANDATORY connectivity allowance IN PLACE OF the transport allowance - the two are never paid together. | CM | Mandatory where the employee is a teleworker under Ley 1221 de 2008 as amended by Ley 2466 de 2025 arts. 52-54; defaults to on-site otherwise. | Text | PRES / TT-AUT / TT-MOV / TT-SUP | Work Modality |  |  |  |  |  |  |  |  |  |  | CCG Module 4 (connectivity allowance, Ley 2466 de 2025 art. 53) and Module 2.2. Calculation-driving: selects connectivity allowance vs transport allowance. The nómina electrónica carries a dedicated Teletrabajo devengado element (NIE158); the ALLOWANCE AMOUNT is a parameter/wage type (WTC), not DD. |
| Colombia |  | All-Inclusive Salary Flag |  | Salario integral | Indicates that the employee is remunerated under the all-inclusive salary regime of Labour Code art. 132 num. 2, which requires a salary of at least 13 minimum wages AND a written agreement. | M |  | Text | Boolean true/false on the nómina electrónica XML; S / N (blank or X) on PILA | Yes/No Indicator |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Integral_Salary_Flag - CO-DIAN-001 (NIE056, Mandatory=Y), CO-PILA-003 (T2R2-041, Mandatory=C). HARD RULE: where set, the four PILA contribution-base fields must be 70% of the integral salary. An all-inclusive-salary employee accrues NO separate severance savings, service bonus or severance interest - see the Severance-Savings Regime field. |
| Colombia |  | Non-Salary Pact Flag |  | Pacto de exclusión salarial | Indicates that an express, written, signed non-salary pact under Labour Code art. 128 attaches to specified payments made to this employee. | CM | Mandatory where any wage type paid to the employee is treated as non-salary by written pact. The pact must be (a) express, (b) written and (c) attached to identified payments. | Text | S / N | Yes/No Indicator |  |  |  |  |  |  |  |  |  |  | CCG Module 4 (Labour Code art. 128; Ley 1393 de 2010 art. 30). Calculation-driving: a valid pact removes the payment from the labour-law salary base permanently, but excludes it from the CONTRIBUTION base only up to 40% of total remuneration - everything above that line is added back. The 40% clamp itself is a parameter and the add-back is a calculated amount (WTC); this flag is the master-data switch that turns the clamp on. |
| Colombia |  | High-Risk Pension Activity Flag |  | Actividad de alto riesgo para pensión | Indicates that the employee performs a high-risk activity under Decreto Ley 2090 de 2003, which carries a non-standard (higher) pension contribution. | M |  | Text | Boolean true/false on the nómina electrónica XML; S / N (blank or X) on PILA | Yes/No Indicator |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.High_Risk_Pension_Flag - CO-DIAN-001 (NIE043, Mandatory=Y), CO-PILA-003 (T2R2-079, Mandatory=C). Bidirectional pair with the PILA pension-contribution-rate field. The RATE is a parameter (WTC), not DD. |
| Colombia |  | Disability / Reinforced Job-Stability Status |  | Situación de discapacidad / estabilidad laboral reforzada | Indicates that the employee holds certified disability status. Held because it changes the TERMINATION path - dismissal requires prior Ministry of Labour authorisation under Ley 361 de 1997 - and because Ley 2466 de 2025 art. 15 obliges the employer to report a disability-hiring contract to the Ministry of Labour within 15 days of signature. | O |  | Text | S / N | Yes/No Indicator |  |  |  |  |  |  |  |  |  |  | CCG Modules 2.1 and 9. NOT a contribution or withholding driver in Colombia - Colombia has no disability-percentage tax relief on the payroll side. Held as a compliance-path selector. |
| Colombia |  | Tax Residence Status |  | Condición de residencia fiscal | Whether the employee is a Colombian tax resident under Tax Code art. 10 (more than 183 days of physical presence in any 365-day period, or one of the diplomatic / nationality-plus-connection tests). THE SINGLE MOST CONSEQUENTIAL WITHHOLDING SWITCH IN COLOMBIAN PAYROLL. | M |  | Text | RES / NRES | Tax Residence Status |  |  |  |  |  |  |  |  |  |  | Calculation-driving. Resident: the progressive art. 383 table (0/19/28/33/35/37/39%) on the art. 388 depurated base, by Procedure 1 or 2. Non-resident: a FLAT 20% under art. 408 on the GROSS payment, with no depuration, no 25% exempt income, no art. 387 deductions and no tax-free band (DIAN Concepto 011108 of 29 June 2026, upholding Concepto 1789 int. 14595 of 2025). THE SWITCH IS PROSPECTIVE, NEVER RETROACTIVE. INTERNAL CONFLICT TO ESCALATE: CCG Module 2.2 states a non-resident employee is withheld on the same art. 383 table, which contradicts the Module 6.2 matrix and the scope_manifest; Module 6.2 is the authoritative text and is the basis of this field. |
| Colombia |  | Withholding Procedure |  | Procedimiento de retención en la fuente | Employer election, made per employee, between Procedure 1 (Tax Code art. 385 - each month stands alone) and Procedure 2 (art. 386 - a fixed percentage recomputed each June and December from the preceding 12 months). | M |  | Text | 1 / 2 | Withholding Procedure |  |  |  |  |  |  |  |  |  |  | Calculation-driving. CCG Module 6.2: the procedure is elected by the EMPLOYER, per employee, and once elected Procedure 2 binds for the whole six-month semester. The FIXED PERCENTAGE produced by the June/December recalculation is a CALCULATED value (CALC/WTC), not master data. Not available at all for a non-resident, who is withheld at the flat art. 408 rate. |
| Colombia |  | Employee-Requested Withholding Rate |  | Tarifa de retención solicitada por el trabajador | Higher withholding percentage requested in writing by the employee under Tax Code art. 383 par. 3. Employee-declared master data - the employer may not unilaterally increase the Procedure 2 fixed percentage mid-semester, so this is the only lawful route to a higher rate inside a semester. | O |  | Decimal | Percentage, up to 2 decimals (e.g. 15.00) |  |  |  |  |  |  |  |  |  |  |  | CCG Module 6.2. This is a USER-INPUT rate, not a statutory parameter: the statutory tables and thresholds remain in the WTC / parameter set. Requires a written employee request on file. |
| Colombia |  | Treaty Status |  | País con o sin convenio | Whether the non-resident beneficiary is resident in a jurisdiction with a double-tax treaty in force with Colombia. Selects which payment-concept list and which rate basis apply on the monthly withholding return annex. | CM | Mandatory on every Formulario 350 annex row, i.e. wherever a payment is made to a non-resident. Not applicable to a resident employee. | Text | CON CONVENIO / SIN CONVENIO | Treaty Status |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Treaty_Country_Code - CO-DIAN-002 (casilla 141 and casilla 144, Mandatory=C). SIN CONVENIO -> concepto 5 (prestación de servicios y compensación por servicios personales), rate 20% under ET art. 408. CON CONVENIO -> concepto 24 (rentas de trabajo), rate taken from the applicable treaty and possibly lower or nil. |
| Colombia |  | Treaty Country Code |  | País del convenio | Country of residence of the non-resident beneficiary, used on the monthly withholding return annex. | CM | Mandatory on every Formulario 350 annex row. Where Treaty Status = CON CONVENIO the country must be one with a treaty in force with Colombia. | Text | ISO 3166-1 alpha-2 | ISO 3166-1 (see the 'Country Codes - ISO 3166-1' sheet) |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Treaty_Country_Code - CO-DIAN-002 (casilla 141 and casilla 144, Mandatory=C). Treaties in force include ES, CL, CH, CA, MX, KR, PT, IN, CZ, GB, FR, IT and JP; Bolivia, Ecuador and Peru are covered by Andean Community Decision 578 rather than a bilateral treaty. The TREATY RATE is a parameter (WTC), not DD - confirm the current list with RA each year. |
| Colombia |  | Art. 380 Non-Filer Declaration |  | Declaración del trabajador - artículo 380 E.T. | The employee's own written declaration that the six conditions of Tax Code art. 380 are met, so that the annual certificate of income and withholdings substitutes for the employee's income-tax return. | CM | Mandatory where the employee is not obliged to file an income-tax return and asks that Formulario 220 serve as the substitute. Section 2 of Formulario 220 is completed from the employee's declaration, not from payroll data. | Text | S / N | Yes/No Indicator |  |  |  |  |  |  |  |  |  |  | Spec ref: CO-DIAN-004 Formulario 220 section 2 (ET arts. 378-380). The MONETARY conditions (4,500 UVT gross assets; 1,400 UVT gross income, consumption and deposits) are parameters (WTC); this field records only that the declaration was obtained. Evidence must be retained. |
| Colombia |  | Number of Dependants |  | Número de dependientes económicos | Count of economic dependants declared by the employee under Tax Code art. 387 par. 2 and art. 336 num. 3. | CM | Mandatory where the employee claims the dependants deduction; enter 0 if none. Each dependant must also be identified individually - a count alone is not sufficient for the annual information return. | Integer | 0 to N |  |  |  |  |  |  |  |  |  |  |  | Calculation-driving family attribute. CCG Module 2.2 and Module 6/7. The DEDUCTION AMOUNTS and caps (10% of gross employment income capped at 32 UVT per month; the additional 72 UVT per dependant per year under art. 336 num. 3, up to four dependants) are parameters and calculated amounts (WTC), NOT DD. Not available to a non-resident. |
| Colombia |  | Dependant Document Type |  | Tipo de documento del dependiente económico | Identity-document type of each declared economic dependant. Repeating block - one occurrence per dependant. | CM | Mandatory where the employee claimed the art. 387 par. 2 dependants deduction during the period. Populated as a bidirectional set with the dependant's document number, name and relationship - all four together or none. | Text | N(2) - Formulario 220 document-type catalogue | Dependant Document Type |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Dependant_Document_Type - CO-DIAN-004 (casilla 79, Mandatory=C), CO-DIAN-005 (numeral N34, Mandatory=C). The information return requires the dependant's DOCUMENT, not merely a count - a missing document rejects the return. The Form 220 list is NARROWER than the nómina electrónica list. |
| Colombia |  | Dependant Document Number |  | Número de documento del dependiente económico | Identity-document number of each declared economic dependant. | CM | Mandatory together with the dependant's document type, name and relationship wherever the dependants deduction is claimed. | Text | Numeric / alphanumeric per the dependant's document type |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Dependant_Document_Number - CO-DIAN-004 (casilla 80, Mandatory=C). |
| Colombia |  | Dependant Full Name |  | Apellidos y nombres del dependiente económico | Surnames and given names of each declared economic dependant. | CM | Mandatory together with the dependant's document type, document number and relationship. | Text | Free text |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Dependant_Name - CO-DIAN-004 (casilla 81, Mandatory=C). |
| Colombia |  | Dependant Relationship |  | Parentesco del dependiente económico | Relationship of the dependant to the employee and the basis on which dependency is claimed - the two are one question in Colombian law, because each of the five art. 387 par. 2 limbs combines a relationship with a qualifying condition. | CM | Mandatory together with the dependant's document type, document number and name. The qualifying evidence (education enrolment, medical certification of dependency, absence of income) must be retained. | Text | Coded value; emitted as free text on Formulario 220 casilla 82 | Dependant Relationship |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Dependant_Relationship - CO-DIAN-004 (casilla 82, Mandatory=C). Calculation-driving: the five limbs of ET art. 387 par. 2 are exhaustive; a person outside them is not a dependant however genuine the support. |
| Colombia |  | EPS Code |  | Código de la EPS o EOC del afiliado | Institution code of the health insurer (EPS or EOC) the employee has chosen. THE EMPLOYEE CHOOSES; the employer must affiliate to the existing entity, and the choice survives a change of employer. | M |  | Text | A(6) - contribution-return institution catalogue (administradoras); prefix pattern ^(ARL\|EPS\|EOC\|AFP\|CCF\|FSP)[0-9]{3}$ - three alphabetic positions naming the subsystem then three numeric positions naming the entity |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.EPS_Code - CO-PILA-003 (T2R2-033, Mandatory=Y). Codes come from the operador's administradoras catalogue, which is an EXTERNAL reference table maintained by the Ministerio de Salud - not enumerated here. CCG Module 2.2: a wrong institution code produces rejected or misdirected contributions. |
| Colombia |  | EPS Transfer Code |  | Código de la EPS o EOC a la cual se traslada el afiliado | Institution code of the health insurer to which the employee is transferring in the period. | CM | Mandatory where the TAE (traslado a otra EPS) novedad is reported for the period; blank otherwise. Bidirectional pair with the TAE change event. | Text | A(6) - administradoras catalogue; prefix pattern ^(ARL\|EPS\|EOC\|AFP\|CCF\|FSP)[0-9]{3}$ - three alphabetic positions naming the subsystem then three numeric positions naming the entity |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.EPS_Transfer_Code - CO-PILA-003 (T2R2-034, Mandatory=C). Scope option_mapper_scope.benefit_type (TDE / TAE). |
| Colombia |  | AFP Code |  | Código de la administradora de fondos de pensiones del afiliado | Institution code of the pension administrator the employee has chosen - a private individual-account administrator or Colpensiones. THE EMPLOYEE CHOOSES; the choice survives a change of employer. | CM | Mandatory in general. Blank is permitted ONLY where the Worker Type or Worker Sub-Type is one that is not obliged to contribute to the general pension system - notably Worker Sub-Type 01, an employed old-age pensioner in active service. | Text | A(6) - administradoras catalogue; prefix pattern ^(ARL\|EPS\|EOC\|AFP\|CCF\|FSP)[0-9]{3}$ - three alphabetic positions naming the subsystem then three numeric positions naming the entity |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.AFP_Code - CO-PILA-003 (T2R2-031, Mandatory=C). Bidirectional set with Worker Type and Worker Sub-Type. |
| Colombia |  | AFP Transfer Code |  | Código de la administradora de pensiones a la cual se traslada el afiliado | Institution code of the pension administrator to which the employee is transferring in the period. | CM | Mandatory where the TAP (traslado a otra administradora de pensiones) novedad is reported for the period; blank otherwise. Bidirectional pair with the TAP change event. | Text | A(6) - administradoras catalogue; prefix pattern ^(ARL\|EPS\|EOC\|AFP\|CCF\|FSP)[0-9]{3}$ - three alphabetic positions naming the subsystem then three numeric positions naming the entity |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.AFP_Transfer_Code - CO-PILA-003 (T2R2-032, Mandatory=C). Scope option_mapper_scope.benefit_type (TDP / TAP). |
| Colombia |  | Pension Regime |  | Régimen pensional | Which of the two Colombian pension regimes the employee belongs to - the public defined-benefit regime (Régimen de Prima Media, administered by Colpensiones) or the private individual-account regime (Régimen de Ahorro Individual con Solidaridad). | M |  | Text | RPM / RAIS | Pension Regime |  |  |  |  |  |  |  |  |  |  | CCG Module 5. Employee election that survives a change of employer and must be declared by a new joiner. Determines which administrator catalogue the AFP code is drawn from and which voluntary-contribution route (art. 55 RAIS voluntary contributions vs additional RPM contributions) is available. The CONTRIBUTION RATES are identical across the two regimes and are parameters (WTC). |
| Colombia |  | CCF Code |  | Código de la caja de compensación familiar | Institution code of the family compensation fund to which the employer is affiliated for this employee. Generally organised by department, so a multi-department employer legitimately carries more than one. | M |  | Text | A(6) - administradoras catalogue; prefix pattern ^(ARL\|EPS\|EOC\|AFP\|CCF\|FSP)[0-9]{3}$ - three alphabetic positions naming the subsystem then three numeric positions naming the entity |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.CCF_Code - CO-PILA-003 (T2R2-035, Mandatory=Y). EMPLOYER election (CCG Module 2.1), inherited by the employee, unlike the EPS and AFP which the employee chooses. The 4% levy is NEVER exonerated under ET art. 114-1. |
| Colombia |  | Employee ARL Code |  | Código de la administradora de riesgos laborales del afiliado | Institution code of the occupational-risk insurer covering the employee. | M |  | Text | A(6) - administradoras catalogue; prefix pattern ^(ARL\|EPS\|EOC\|AFP\|CCF\|FSP)[0-9]{3}$ - three alphabetic positions naming the subsystem then three numeric positions naming the entity |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.ARL_Code - CO-PILA-003 (T2R2-077, Mandatory=Y). EMPLOYER election, inherited by the employee. Normally equal to the employer ARL code; held per employee because the contribution-return layout carries both. |
| Colombia |  | Severance-Savings Fund Code |  | Código del fondo de cesantías del afiliado | Code of the severance-savings fund the employee has chosen to receive the annual deposit. THE EMPLOYEE CHOOSES; affiliation is compulsory even where the employer pays severance savings directly under Labour Code art. 57 par. 4. | M |  | Text | N(2) - published fund catalogue | Severance-Savings Fund |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Cesantias_Fund_Code - CO-CESANTIAS-006 (T09, Mandatory=Y). IGNORED where the employer files a single-fund planilla, in which case the planilla-level fund overwrites this value for every record - see the employer field 'Single-Fund Planilla Severance Fund Code'. Any value outside the registered list is REJECTED. |
| Colombia |  | Severance-Savings Regime |  | Régimen de cesantías | Which severance-savings regime the employee is under: the Ley 50 de 1990 annual-deposit regime (the default for everyone hired from 1 January 1991), the pre-1991 retroactive regime of the Labour Code, or none because the employee is on an all-inclusive salary. | M |  | Text | LEY50 / TRADICIONAL / INTEGRAL | Severance-Savings Regime |  |  |  |  |  |  |  |  |  |  | Calculation-driving, and a documented reporting trap. Formulario 220 reports the pre-1991 regime at casilla 48 and the amount deposited to the fund at casilla 49, while Formato 2276 reports them in the OPPOSITE order at numerals N19 (fund) and N20 (traditional). MAP BY MEANING, NEVER BY POSITION - see CO-DIAN-004 and CO-DIAN-005 Field Options. |
| Colombia |  | Severance-Savings Deposit Arrangement |  | Modalidad de consignación de cesantías | How the employee's severance savings are settled: the ordinary annual deposit to the fund by 14 February, the monthly 8.33% advance deposit permitted by Ley 2466 de 2025 art. 64 under a written agreement, or direct payment to the employee discharging the deposit obligation under Labour Code art. 57 par. 4. | CM | Mandatory for every employee under the Ley 50 de 1990 regime. Where the value is MENSUAL a written agreement must be on file, and the monthly-advance fields of the deposit file are produced; where it is ANUAL only the ordinary annual detail record is produced. | Text | ANUAL / MENSUAL / DIRECTO / NA | Severance-Savings Deposit Arrangement |  |  |  |  |  |  |  |  |  |  | Spec ref: Contract.Cesantias_Regime (CO-CESANTIAS-006 MA01 'Acuerdo escrito para la consignación mensual anticipada', Mandatory=C) - the spec models the monthly-advance gate as a Y/N flag; this DD models the full four-way arrangement and MENSUAL is the value that maps to Y. LATE DEPOSIT COSTS ONE DAY'S SALARY PER DAY OF DELAY, PER EMPLOYEE, UNCAPPED (Ley 50 de 1990 art. 99 num. 3). |
| Colombia |  | Foreign National Not Liable to Pension Flag |  | Extranjero no obligado a cotizar a pensiones | Indicates that the employee is a foreign national exempt from pension affiliation because affiliation to a pension system abroad has been proved (Decreto 1072 de 2015 art. 2.2.1.2.1.4). | CM | Where set, the ONLY valid values of Employee Document Type are cédula de extranjería (CE), pasaporte (PA), carné diplomático (CD), salvoconducto (SC) and permiso especial de permanencia (PE). Bidirectional pair with Employee Document Type. | Text | S / N (emitted as blank or X on the PILA fixed-width file) | Yes/No Indicator |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Foreign_Not_Pension_Liable_Flag - CO-PILA-003 (T2R2-007, Mandatory=C). Calculation-driving: suppresses the pension contribution only. Health, occupational risk and the payroll levies continue to apply. Requires documentary proof on file. |
| Colombia |  | Concurrent Employer (Multi-Employer) Flag |  | Cotizante con más de un empleador | Indicates that the employee holds another concurrent employment. Where there are two or more employers, contributions are made PROPORTIONALLY to each remuneration and accumulate up to the shared 25-minimum-wage ceiling, and the health contribution must be made on the same base. | CM | Mandatory where the new joiner declares another concurrent employer. The other employer's contribution base must also be captured to apportion the shared ceiling. | Text | S / N | Yes/No Indicator |  |  |  |  |  |  |  |  |  |  | CCG Module 2.2 new-joiner declarations; Ley 100 de 1993 art. 18 par. 1 as substituted by Ley 797 de 2003 art. 5. Calculation-driving switch. The other employer's BASE is a monetary input to the calculation and sits in the WTC / payroll-input set, not in this master-data field. Mis-configuration produces over- or under-contribution against the shared ceiling and is a standing UGPP audit exposure. |
| Colombia |  | Principal Contributor Document Type |  | Tipo de documento del cotizante principal | Identity-document type of the principal contributor to whom a dependent-beneficiary record attaches on the contribution return. | CM | Populated ONLY for a dependent-beneficiary record - typically Worker Type 40, beneficiario UPC adicional. Bidirectional pair with the principal contributor's document number and with Worker Type. | Text | A(2) - PILA contributor document-type catalogue | Employee Document Type (PILA / Cesantias) |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Main_Contributor_Doc_Type - CO-PILA-003 (T2R2-074, Mandatory=C). Uses the PILA two-letter CONTRIBUTOR catalogue, not the DIAN numeric one and not the EMPLOYER catalogue: the principal contributor is a natural person, so NI is not available here, while RC is (a beneficiary record may attach to a registro civil). Spec T2R2-074 points at the same Sheet 6 table as T2R2-003, 'Tipo documento cotizante'. |
| Colombia |  | Principal Contributor Document Number |  | Número de identificación del cotizante principal | Identity-document number of the principal contributor to whom a dependent-beneficiary record attaches. | CM | Populated ONLY for a dependent-beneficiary record. Bidirectional pair with the principal contributor's document type. | Text | A(16) left-justified, space-filled |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Employee.Main_Contributor_Doc_Number - CO-PILA-003 (T2R2-075, Mandatory=C). |


**Country-Specific Legal Entity Fields**


| Country | Ordinal | Field Name | Internal Code | Label in Local Language | Field Description (Long Description of the Field) | Data Type  -Mandatory (M), Conditional Mandatory (CM), Optional (O) | Pre-Condition for Conditional Mandatory | Field Type (Text, Number, Date, Integer, Decimal, Counter) | Pre-Defined Format | Option Mapper | Validations, Restrictions, Pick Lists etc. | Parent Field Group | Ordinal of Parent Field Group | Internal Code of Parent Field Group | Sub Group under Parent Field Group | Ordinal of Sub Group under Parent Field Group | Internal Code of Sub Group under Parent Field Group | Default Value | MSS Field Permissions (Read, Write) | ESS Field Permissions (Read, Write) | Additional Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Colombia |  | Employer Corporate Name |  | Razón social del empleador | Registered corporate name of the employer. Declarant name on every statutory artefact. | CM | Populated where the employer is a LEGAL person or a sociedad de hecho. MUTUALLY EXCLUSIVE with the four employer natural-person name fields: a natural-person employer must NOT populate this field. | Text | A(200) on PILA; variable length on the DIAN artefacts |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Legal_Name - CO-DIAN-001 (NIE032, Mandatory=C), CO-DIAN-002 (casilla 11, Mandatory=C), CO-PILA-003 (A1-001 and T2R1-004, Mandatory=Y), CO-DIAN-004 (casilla 11, Mandatory=C/Y). Bidirectional exclusivity with the natural-person name block, enforced by the instructivo of every artefact. |
| Colombia |  | Employer First Surname |  | Primer apellido del empleador (persona natural) | First surname of the employer where the employer is a natural person. | CM | Populated ONLY where the employer is a natural person. Mutually exclusive with Employer Corporate Name. | Text | Variable length |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.First_Surname - CO-DIAN-001 (NIE210, Mandatory=C), CO-DIAN-002 (casilla 7, Mandatory=C), CO-DIAN-004 (casilla 7, Mandatory=C). |
| Colombia |  | Employer Second Surname |  | Segundo apellido del empleador (persona natural) | Second surname of the employer where the employer is a natural person. | CM | Populated ONLY where the employer is a natural person. Mutually exclusive with Employer Corporate Name. | Text | Variable length |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Second_Surname - CO-DIAN-001 (NIE211, Mandatory=C), CO-DIAN-002 (casilla 8, Mandatory=C), CO-DIAN-004 (casilla 8, Mandatory=C). |
| Colombia |  | Employer First Name |  | Primer nombre del empleador (persona natural) | First given name of the employer where the employer is a natural person. | CM | Populated ONLY where the employer is a natural person. Mutually exclusive with Employer Corporate Name. | Text | Variable length |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.First_Name - CO-DIAN-001 (NIE212, Mandatory=C), CO-DIAN-002 (casilla 9, Mandatory=C), CO-DIAN-004 (casilla 9, Mandatory=C). |
| Colombia |  | Employer Other Names |  | Otros nombres del empleador (persona natural) | Further given names of the employer where the employer is a natural person. | CM | Populated ONLY where the employer is a natural person. Mutually exclusive with Employer Corporate Name. | Text | Variable length |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Other_Names - CO-DIAN-001 (NIE213, Mandatory=C), CO-DIAN-002 (casilla 10, Mandatory=C), CO-DIAN-004 (casilla 10, Mandatory=C). |
| Colombia |  | Employer Person Type |  | Tipo de persona del aportante | Whether the employer is a legal person or a natural person. Gates a large conditional block on the contribution return. | M |  | Text | J / N | Employer Person Type |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Person_Type - CO-PILA-003 (A1-009, Mandatory=Y). Where J: the NIT verification digit and the whole legal-representative block become mandatory. Where N: the valid employer document types narrow to CC, CE, TI, PA, CD, PE and SC - NI is not available - and the verification digit must be ZERO. |
| Colombia |  | Employer Legal Nature |  | Naturaleza jurídica del aportante | Legal nature of the employer entity. | M |  | Text | N(1) | Employer Legal Nature |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Legal_Nature - CO-PILA-003 (A1-008, Mandatory=Y). PRIVATE-SECTOR FILTER: the Mercans platform serves private employers, so only value 2 (Privada) is in scope. Public (1), mixed-capital (3), multilateral organisations (4) and foreign public-law entities not subject to Colombian law (5) are excluded - see the mapper Notes. |
| Colombia |  | Class of Contributor |  | Clase de aportante | Size and benefit classification of the employer, driven by the number of contributors across ALL branches and by eligibility for the small-business and formalisation regimes. | M |  | Text | A(1) - A / B / C / D | Class of Contributor |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Aportante_Class - CO-PILA-003 (A1-007, Mandatory=Y). The headcount is counted across all branches and dependencies, NOT per branch. Class D (Ley 1429 de 2010 beneficiary) makes the commercial-registry date and the registered-seat department code mandatory. |
| Colombia |  | Contributor Type |  | Tipo de aportante | Category of the party making the contribution. For corporate payroll the value is always 1 - Empleador. | M |  | Text | N(2) zero-filled | Contributor Type |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Aportante_Type - CO-PILA-003 (A1-030 and T2R1-021, Mandatory=Y). PRIVATE-SECTOR FILTER: only value 1 (Empleador) is in scope. Independents (2), public entities and universities (3), guilds and religious congregations (4), associated-work cooperatives (5), diplomatic missions (6) and the remaining special payers (7-12) are excluded - see the mapper Notes. |
| Colombia |  | Form of Presentation |  | Forma de presentación | Whether the employer files one consolidated contribution return for the whole legal person or one return per branch. | M |  | Text | U (único) / S (sucursal) | Form of Presentation |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Presentation_Form - CO-PILA-003 (A1-010 and T2R1-011, Mandatory=Y). Bidirectional pair with the branch code and branch name: where U, both MUST BE BLANK; where S, both become required. |
| Colombia |  | PILA Filing Modality |  | Modalidad de la planilla (electrónica o asistida) | Whether the contribution return is prepared and paid electronically on the operador's site or keyed by the operador's call centre on the employer's instruction. | M |  | Text | 1 (electrónica) / 2 (asistida) | PILA Filing Modality |  |  |  |  |  |  |  |  |  |  | Spec ref: CO-PILA-003 Field Options. Employer-level election gated by headcount under Decreto 780 de 2016 art. 3.2.3.9 as substituted by Decreto 1990 de 2016 - the headcount is aggregated across all branches under the same legal person. The THRESHOLD is a parameter (WTC); the elected modality is master data. |
| Colombia |  | PILA Planilla Type |  | Tipo de planilla | Default planilla type the employer files. The standard value for private corporate payroll is E (planilla empleados). | M |  | Text | A(1) | PILA Planilla Type |  |  |  |  |  |  |  |  |  |  | Scope option_mapper_scope.correction_codes. The DEFAULT is master data; the value actually used in a given run may be overridden by the event (A for omitted hires, N for corrections, M for arrears, J for a court-ordered settlement, X for a liquidated company) and that override is TRANSACTIONAL, not master data. Planilla types S, I, Y, T, F, H, K, U and O are out of scope - see the mapper Notes. |
| Colombia |  | Formato 2276 Informant Type |  | Tipo de informante - Formato 2276 | Capacity in which the employer files the annual rentas de trabajo information return. An ordinary employer files as informante general. | M |  | Text | N(1) | Formato 2276 Informant Type |  |  |  |  |  |  |  |  |  |  | Spec ref: CO-DIAN-005 (Res. DIAN 000227 de 2025 par. 4). Where the value is 1 the trust and contract-participant numerals (N35, N36) 'no se deben diligenciar'. Values 2-8 attach to trust, mandate, consortium, hydrocarbons, joint-venture, participation-account and public-cooperation structures and are out of scope for ordinary employer payroll. |
| Colombia |  | Employer Address |  | Dirección del empleador | Registered address of the employer, reported in the declarant section of the statutory artefacts. | M |  | Text | A(40) on PILA; variable length on the nómina electrónica |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Address - CO-DIAN-001 (NIE038, Mandatory=Y), CO-PILA-003 (A1-011, Mandatory=Y). |
| Colombia |  | Employer Country Code |  | País del empleador | Country of the employer's registered address. A required attribute of the employer element on the electronic payroll support document. | M |  | Text | ISO 3166-1 alpha-2 (Anexo Técnico table 5.4.1) | ISO 3166-1 (see the 'Country Codes - ISO 3166-1' sheet) |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Country_Code - CO-DIAN-001 (NIE013 and NIE035, Mandatory=Y). |
| Colombia |  | Employer Department Code |  | Departamento del empleador | Two-digit DANE DIVIPOLA department code of the employer's registered address. | M |  | Text | N(2) DANE DIVIPOLA (Anexo Técnico table 5.4.2) |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Department_Code - CO-DIAN-001 (NIE014 and NIE036, Mandatory=Y), CO-PILA-003 (A1-013, Mandatory=Y), CO-DIAN-004 (casilla 34, Mandatory=Y). Use the DANE DIVIPOLA catalogue, NOT the ISO 3166-2:CO list. |
| Colombia |  | Employer Municipality Code |  | Municipio del empleador | DANE DIVIPOLA municipality of the employer's registered address. Also serves as the 'lugar donde se practicó la retención' on the annual certificate of income and withholdings. | M |  | Text | N(5) full DIVIPOLA on the nómina electrónica (11001); N(3) suffix on PILA and Formulario 220 |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Municipality_Code - CO-DIAN-001 (NIE015 generation municipality and NIE037 employer municipality, Mandatory=Y); and Company.City_Code - CO-PILA-003 (A1-012, Mandatory=Y) and CO-DIAN-004 (casilla 35 'Lugar donde se practico la retencion', Mandatory=Y). SPLIT-CODE TRAP - store five digits once and split into 2 + 3 on the artefacts that require it. |
| Colombia |  | Registered-Seat Department Code |  | Código del departamento del domicilio (Ley 1429) | Two-digit DANE department code of the employer's registered seat, required of a Ley 1429 de 2010 formalisation beneficiary. | CM | Mandatory for a Ley 1429 de 2010 beneficiary, i.e. where Class of Contributor = D or the Ley 1429 CCF benefit flag = S. Bidirectional set with those two fields and with the commercial-registry date. | Text | A(2) DANE DIVIPOLA |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Department_Code_Registry - CO-PILA-003 (A1-032, Mandatory=C). Distinct from the ordinary employer department code, which follows the operating address. |
| Colombia |  | Employer Telephone |  | Teléfono del empleador | Contact telephone number of the employer, reported on the contribution return. | M |  | Text | N(10) right-justified, zero-filled |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Phone - CO-PILA-003 (A1-015, Mandatory=Y). |
| Colombia |  | Employer Fax |  | Fax del empleador | Fax number of the employer. Retained in the contribution-return layout; supplied by the employer where held. | O |  | Text | N(10) right-justified, zero-filled |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Fax - CO-PILA-003 (A1-016, Mandatory=N). Legacy field in the Resolución 2388 de 2016 layout - zero-fill where not held. |
| Colombia |  | Employer E-mail Address |  | Dirección de correo electrónico del empleador | Contact e-mail address of the employer, reported on the contribution return and used by the operador for notifications. | M |  | Text | A(60) |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Email - CO-PILA-003 (A1-017, Mandatory=Y). |
| Colombia |  | Branch or Dependency Code |  | Código de la sucursal o de la dependencia | Employer-assigned code of the branch or dependency for which the contribution return is filed. | CM | MUST BE BLANK where Form of Presentation = U (único). Populated only where Form of Presentation = S (sucursal). Bidirectional pair with Form of Presentation and with the branch name. | Text | A(10) left-justified, space-filled |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Branch_Code - CO-PILA-003 (A1-005 and T2R1-012, Mandatory=C). The Archivo Tipo 2 header value must equal the Archivo Tipo 1 value. |
| Colombia |  | Branch or Dependency Name |  | Nombre de la sucursal o de la dependencia | Name of the branch or dependency for which the contribution return is filed. | CM | Populated together with the branch code, i.e. only where Form of Presentation = S. Where the branch has no name, the annex directs that the branch CODE is written here instead. | Text | A(40) left-justified, space-filled |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Branch_Name - CO-PILA-003 (A1-006 and T2R1-013, Mandatory=C). Branches trading under the same corporate name are NOT separate registrations - CCG Module 2.1. |
| Colombia |  | Economic Activity Code (CIIU) |  | Código de actividad económica principal (CIIU rev. 4 A.C.) | Principal economic activity of the employer under the CIIU revision 4 classification adapted for Colombia. Taken from casilla 46 of the RUT. | M |  | Text | N(4) |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.CIIU_Code - CO-DIAN-002 (casilla 27, Mandatory=C), CO-PILA-003 (A1-014, Mandatory=Y). The SAME classification drives the occupational-risk class assignment and, for a legal person exonerated under ET art. 114-1, the self-withholding rate on Formulario 350. External catalogue - DIAN Resoluciones 000114 de 2020, 001232 de 2022 and successors; DANE Resolución 66 de 2012 for the PILA variant. |
| Colombia |  | DIAN Sectional Office Code |  | Código de la dirección seccional | Code of the DIAN sectional office of the employer's principal domicile, taken from casilla 12 of the RUT. | M |  | Text | N(2) |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.DIAN_Seccional_Code - CO-DIAN-002 (casilla 12, Mandatory=Y). A configuration constant per legal entity, not a per-return input. External DIAN catalogue. |
| Colombia |  | Employer ARL Code |  | Código de la ARL del aportante | Institution code of the occupational-risk insurer with which the employer is affiliated. | M |  | Text | A(6) - administradoras catalogue; prefix pattern ^(ARL\|EPS\|EOC\|AFP\|CCF\|FSP)[0-9]{3}$ - three alphabetic positions naming the subsystem then three numeric positions naming the entity |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.ARL_Code - CO-PILA-003 (T2R1-014, Mandatory=Y). EMPLOYER election (CCG Module 2.1 item 3), inherited by every employee. |
| Colombia |  | Work Centre Occupational Risk Class |  | Clase de riesgo laboral del centro de trabajo | Occupational-risk class I to V of the work centre. The class attaches to the WORK CENTRE, not to the company, so an employer with a corporate office and a plant legitimately carries more than one class - and each employee's contribution follows the class of the centre where they work. | M |  | Text | I / II / III / IV / V | Occupational Risk Class |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Risk_Class - CO-PILA-003 (T2R2-078, Mandatory=Y). Legal basis: Decreto 1072 de 2015 arts. 2.2.4.2.5.6 and 2.2.4.3.5. The class is master data held per work centre; the RATE (initial rate and the class minimum/maximum) is a parameter (WTC), NOT DD. Bidirectional set with Work Centre Code and the VCT change-of-work-centre event. |
| Colombia |  | Commercial Registry Date |  | Fecha de matrícula mercantil | Date of the employer's commercial registration with the Chamber of Commerce. | CM | MANDATORY for an employer benefiting from the Ley 1429 de 2010 formalisation regime, i.e. where Class of Contributor = D or the Ley 1429 CCF benefit flag = S. Bidirectional set with those fields and with the registered-seat department code. | Date | AAAA-MM-DD |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Commercial_Registry_Date - CO-PILA-003 (A1-031, Mandatory=C). |
| Colombia |  | Exonerated from Health, SENA and ICBF (art. 114-1) |  | Aportante exonerado de aportes a salud, SENA e ICBF | Indicates that the employer is exonerated from the employer health contribution and from the SENA and ICBF payroll levies under Tax Code art. 114-1. | M |  | Text | S / N | Yes/No Indicator |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Exonerated_Flag - CO-PILA-003 (A1-033, Mandatory=Y). THE EXONERATION NEVER TOUCHES pension (12%), occupational risk, or the family compensation fund (4%). It is also disapplied per employee where the health contribution base reaches 10 minimum wages - that per-contributor test produces a DERIVED value on the return (CALC), not a second master-data field. Bidirectional with the CIIU self-withholding activity code on Formulario 350. |
| Colombia |  | Ley 1429 art. 5 CCF Benefit |  | Aportante acogido a los beneficios del artículo 5 de la Ley 1429 de 2010 (CCF) | Indicates that the employer has elected the Ley 1429 de 2010 art. 5 benefits in respect of the family compensation fund levy. | M |  | Text | S / N | Yes/No Indicator |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Ley1429_CCF_Flag - CO-PILA-003 (A1-034, Mandatory=Y). Where S, the commercial-registry date and the registered-seat department code become mandatory and Class of Contributor is normally D. |
| Colombia |  | Single-Fund Planilla Severance Fund Code |  | Código del fondo de cesantías de la planilla (fondo único) | Code of the severance-savings fund used at PLANILLA level where the employer deposits the whole file to a single fund. Where the single-fund indicator is set, this value OVERWRITES the per-employee fund code for every record in the file. | CM | Mandatory where the employer files a single-fund severance deposit planilla; blank where each employee's own fund code governs. | Text | N(2) - published fund catalogue | Severance-Savings Fund |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Cesantias_Fund_Code (declared in build_co_specs._DD_MASTER_MAPPINGS; the single-fund indicator is CO-CESANTIAS-006 E07, which back-references the per-employee field T02). Using a single fund where employees are affiliated to different funds MISDIRECTS the deposit - the penalty is one day's salary per day of delay, per employee, uncapped. |
| Colombia |  | Employer Status Action Type |  | Tipo de acción (concordato, reestructuración, liquidación, cese) | Insolvency, restructuring, liquidation or cessation event affecting the employer. | CM | Optional in general. Where populated it makes the insolvency start date MANDATORY and the commercial-activity cessation date required. Bidirectional set with both dates. | Text | N(1) | Employer Status Action Type |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Action_Type - CO-PILA-003 (A1-026, Mandatory=C). A value of 4 (cese de actividades) fixes the date from which the employer is no longer obliged to contribute. |
| Colombia |  | Insolvency / Restructuring / Liquidation Start Date |  | Fecha de inicio del concordato, reestructuración, liquidación o cese de actividades | Date on which the employer status event began. | CM | MANDATORY where the employer status action type is populated. Bidirectional pair with that field. | Date | AAAA-MM-DD |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Insolvency_Start_Date - CO-PILA-003 (A1-025, Mandatory=C). |
| Colombia |  | Commercial Activity Cessation Date |  | Fecha en que terminó actividades comerciales | Date on which the employer ceased commercial activity. | CM | Required where the employer status action type is populated - the annex directs that it 'se debe diligenciar cuando se ha reportado información en el campo 26 de este registro'. | Date | AAAA-MM-DD |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Trading_Cease_Date - CO-PILA-003 (A1-027, Mandatory=C). |
| Colombia |  | Legal Representative First Surname |  | Primer apellido del representante legal | First surname of the employer's legal representative. | CM | MANDATORY where Employer Person Type = J. Bidirectional pair with Employer Person Type. | Text | A(20) left-justified, space-filled |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Legal_Rep_First_Surname - CO-PILA-003 (A1-021, Mandatory=C). |
| Colombia |  | Legal Representative Second Surname |  | Segundo apellido del representante legal | Second surname of the employer's legal representative. | O |  | Text | A(30) left-justified, space-filled |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Legal_Rep_Second_Surname - CO-PILA-003 (A1-022, Mandatory=N). |
| Colombia |  | Legal Representative First Name |  | Primer nombre del representante legal | First given name of the employer's legal representative. | CM | MANDATORY where Employer Person Type = J. Bidirectional pair with Employer Person Type. | Text | A(20) left-justified, space-filled |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Legal_Rep_First_Name - CO-PILA-003 (A1-023, Mandatory=C). |
| Colombia |  | Legal Representative Second Name |  | Segundo nombre del representante legal | Second given name of the employer's legal representative. | O |  | Text | A(30) left-justified, space-filled |  |  |  |  |  |  |  |  |  |  |  | Spec ref: Company.Legal_Rep_Second_Name - CO-PILA-003 (A1-024, Mandatory=N). |



---

## Sheet 6 - Country Option Mappers (30 mappers)


**Country Option Mappers**


| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
|---|---|---|---|---|---|
| Employee Document Type | 11 | RC | Registro civil de nacimiento | Civil birth registration. Under-7s; never an employee, retained for beneficiary records. | Referenced by Employee Document Type (Mandatory=Y on CO-DIAN-001 NIE044, CO-PILA-003 T2R2-003, CO-DIAN-004 casilla 24 and CO-CESANTIAS-006 T03). Scope option_mapper_scope.personal_id_type. TWO CODE SYSTEMS, ONE MASTER VALUE: DIAN artefacts use the numeric code in the Code column; PILA and the severance-savings deposit file use a SEPARATE two-letter catalogue, which now has its own mapper - see 'Employee Document Type (PILA / Cesantias)'. The letter equivalents are 11=RC, 12=TI, 13=CC, 21=TE, 22=CE, 41=PA and 47=PE; codes 31, 42, 50 and 91 have no PILA equivalent, and PILA codes CD, SC and PT have no DIAN numeric equivalent. CONSTRAINTS: (a) a PEP number must be EXACTLY 15 digits (SOI hard rule); (b) where the Foreign National Not Liable to Pension flag is set, only CE, PA, CD, SC and PE are valid; (c) the Colombian Abroad flag may be used only with CC or TI; (d) CO-GAP-06 - no code exists for the PPT (Decreto 216 de 2021), 47 is the only proxy; (e) CO-GAP-07 - the nómina electrónica types the number as xsd:integer, so an alphanumeric passport cannot be schema-valid. Formulario 220 carries a NARROWER list (12, 13, 21, 22, 31, 41). |
|  | 12 | TI | Tarjeta de identidad | Identity card for a person aged 7 to 17. Authorised minors 15-17 may be employed; converts to a cédula de ciudadanía on majority, changing the composite key. |  |
|  | 13 | CC | Cédula de ciudadanía | Colombian national identity card. The default for nationals aged 18 and over and the overwhelming majority of Colombian employees. Numeric, no check digit. |  |
|  | 21 | TE | Tarjeta de extranjería | Foreigner's identity card for minors. Alphanumeric in practice - see the integer-typing trap. |  |
|  | 22 | CE | Cédula de extranjería | Foreign resident's identity card, issued by Migración Colombia. Numeric, typically 6-7 digits. |  |
|  | 31 | NIT | NIT | Tax identification number. Rare for an employee; used where the beneficiary is a legal person. Carries a separate verification digit. |  |
|  | 41 | PA | Pasaporte | Passport. Alphanumeric - cannot satisfy the xsd:integer typing of the nómina electrónica worker document-number attribute (CO-GAP-07). |  |
|  | 42 | DIE | Documento de identificación extranjero | Foreign identity document. Alphanumeric. |  |
|  | 47 | PEP | PEP - Permiso Especial de Permanencia | Special residence permit. 15 numeric digits, exactly. Used as the proxy for the PPT, which has no code of its own. |  |
|  | 50 | NIT-EXT | NIT de otro país | Foreign tax identification number. Alphanumeric. |  |
|  | 91 | NUIP | NUIP | Unique personal identification number. EMPLOYEE USE ONLY - this document type is not held in the DIAN tax-registry database. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Employee Document Type (PILA / Cesantias) | CC | 13 | Cedula de ciudadania | Colombian national identity card. DIAN numeric equivalent 13. The default for nationals aged 18 and over. Numeric only. | Referenced by Employee Document Type on the SOCIAL-SECURITY channel - CO-PILA-003 (T2R2-003 'Tipo documento del cotizante' and T2R2-074, Mandatory=Y/C) and CO-CESANTIAS-006 (T03, Mandatory=Y). SECOND CODE SYSTEM FOR ONE MASTER VALUE: the same Employee Document Type master field is emitted as the DIAN numeric code on DIAN artefacts and as the two-letter code below on PILA and the severance-savings deposit file. Source: PILA Anexo Tecnico 2 (AT2 version 09, 16-09-2019), Registro Tipo 2 campo 3 - the eight values CC, CE, TI, PA, CD, SC, RC and PE, verbatim. CONSTRAINTS: (a) only PA and CD may be alphanumeric; TI, CC, SC, RC, CE and PE must be all digits; (b) a PE (PEP) number must be EXACTLY 15 digits (SOI hard rule); (c) where the Foreign National Not Liable to Pension flag is set only CE, PA, CD, SC and PE are valid; (d) the Colombian Abroad flag may be used only with CC or TI; (e) NI is an EMPLOYER document type and is NOT valid for a contributor; (f) for a legal representative only CC, CE, PA and CD are available - see 'Legal Representative Document Type'. CO-GAP-06 remains open: PT exists in the cesantias XLS layout but not in the DIAN numeric catalogue, where 47 (PEP) is the only proxy. |
|  | CE | 22 | Cedula de extranjeria | Foreign resident's identity card issued by Migracion Colombia. DIAN numeric equivalent 22. Numeric only. |  |
|  | TI | 12 | Tarjeta de identidad | Identity card for a person aged 7 to 17. DIAN numeric equivalent 12. Numeric only. Converts to CC on majority, changing the composite key - notify the fund or the deposit lands on an orphan account. |  |
|  | PA | 41 | Pasaporte | Passport. DIAN numeric equivalent 41. ALPHANUMERIC permitted on PILA - and this is the channel difference behind CO-GAP-07, because the nomina electronica types the number as xsd:integer. |  |
|  | CD | - | Carne diplomatico | Diplomatic card. ALPHANUMERIC permitted. NO DIAN numeric equivalent exists - the nomina electronica cannot carry this document type at all. |  |
|  | SC | - | Salvoconducto de permanencia | Safe-conduct of stay. Numeric only. NO DIAN numeric equivalent exists. |  |
|  | RC | 11 | Registro civil de nacimiento | Civil birth registration. DIAN numeric equivalent 11. Valid in the CONTRIBUTOR list but NOT in the employer list; an under-7 is never an employee, so it is retained for beneficiary records only. |  |
|  | PE | 47 | Permiso Especial de Permanencia (PEP) | Special residence permit. DIAN numeric equivalent 47 (abbreviated PEP in Anexo table 5.2.1). Numeric only and EXACTLY 15 digits. |  |
|  | PT | - | Permiso por Proteccion Temporal (PPT) | CESANTIAS XLS LAYOUT ONLY. Printed in the XLS document-type list of the severance-savings deposit manual; it is absent from the PILA fixed-width list of AT2 version 09 and has no DIAN numeric equivalent (CO-GAP-06). Do not emit it on PILA or on any DIAN artefact. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Employer Document Type | NI | NI | Número de identificación tributaria | The document type of a corporate employer. Requires Employer Person Type = J. | Referenced by Employer Document Type (Mandatory=Y, CO-PILA-003 A1-002 and T2R1-005). NOT used by Principal Contributor Document Type (T2R2-074), which takes the CONTRIBUTOR catalogue 'Employee Document Type (PILA / Cesantias)' - the two lists differ in exactly two places, this one carrying NI and lacking RC. CONSTRAINT: where Employer Person Type = N (natural) the type NI is NOT available; where Person Type = J only NI is used in practice. RC is available in the CONTRIBUTOR list but not in the employer list. |
|  | CC | CC | Cédula de ciudadanía | Natural-person employer. Numeric only. |  |
|  | CE | CE | Cédula de extranjería | Natural-person employer. Numeric only. |  |
|  | TI | TI | Tarjeta de identidad | Natural-person employer. Numeric only. |  |
|  | PA | PA | Pasaporte | Natural-person employer. Alphanumeric permitted. |  |
|  | CD | CD | Carné diplomático | Natural-person employer. Alphanumeric permitted. |  |
|  | SC | SC | Salvoconducto de permanencia | Natural-person employer. Numeric only. |  |
|  | PE | PE | Permiso Especial de Permanencia | Natural-person employer. Numeric only. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Legal Representative Document Type | CC | CC | Cédula de ciudadanía | Numeric. | Referenced by Legal Representative Document Type (Mandatory=C, CO-PILA-003 A1-020). CONSTRAINT: mandatory where Employer Person Type = J; optional where Person Type = N. This list is NARROWER than the employer and contributor lists - NI, TI, SC, PE and RC are NOT available for a legal representative. |
|  | CE | CE | Cédula de extranjería | Numeric. |  |
|  | PA | PA | Pasaporte | Alphanumeric permitted. |  |
|  | CD | CD | Carné diplomático | Alphanumeric permitted. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Dependant Document Type | 12 | TI | Tarjeta de identidad | Identity card for a dependant aged 7 to 17. | Referenced by Dependant Document Type (Mandatory=C, CO-DIAN-004 casilla 79 and CO-DIAN-005 Formato 2276). CONSTRAINT: populated only where the employee claimed the ET art. 387 par. 2 dependants deduction during the period, and always as a bidirectional set with the dependant's document number, full name and relationship. This Formulario 220 list is NARROWER than the nómina electrónica list at Anexo table 5.2.1, which also carries 11, 42, 47, 50 and 91. |
|  | 13 | CC | Cédula de ciudadanía | National identity card. The great majority of dependants. |  |
|  | 21 | TE | Tarjeta de extranjería | Foreigner's identity card for a minor dependant. |  |
|  | 22 | CE | Cédula de extranjería | Foreign resident's identity card. |  |
|  | 31 | NIT | NIT | Where the dependant beneficiary is an entity - not an ordinary case. |  |
|  | 41 | PA | Pasaporte | Passport. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Gender | M | M | Masculino | Male | Referenced by Gender (Optional). Not reported on any of the six in-scope statutory filings and not a calculation driver - Colombia varies no payroll rate, threshold or contribution by gender. Held for HR master data and affiliation paperwork only. |
|  | F | F | Femenino | Female |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Contract Type | 1 | FIJO | Término fijo | Fixed-term contract. Labour Code art. 46; maximum four years after Ley 2466 de 2025 art. 6. | Referenced by Contract Type (Mandatory=Y, CO-DIAN-001 NIE061, Anexo Técnico table 5.5.2). Scope option_mapper_scope.contract_type. All five values are private-sector employment contracts. Independent service contracts (contrato de prestación de servicios) are NOT a contract type - they are not employment and are out of scope. |
|  | 2 | INDEF | Término indefinido | Indefinite-term contract - the legal default. Labour Code art. 47; Ley 2466 de 2025 art. 5. |  |
|  | 3 | OBRA | Obra o labor determinada | Contract for a specific work or task. Labour Code art. 46. |  |
|  | 4 | APREN | Aprendizaje | Apprenticeship. Ley 2466 de 2025 art. 21 recast this as a special fixed-term LABOUR contract, regulated by Decreto 0223 of 5 March 2026. PILA worker type 12 (lectiva) or 19 (productiva). |  |
|  | 5 | PRACT | Prácticas o pasantías | Internship or practical placement. Reported where remunerated. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Worker Type | 01 | DEP | Dependiente | Standard employee. THE DEFAULT for private corporate payroll. | Referenced by Worker Type (Mandatory=Y, CO-DIAN-001 NIE041 table 5.5.3 and CO-PILA-003 T2R2-005). MAPPING TRAP: the nómina electrónica table carries only SIXTEEN values while the PILA tipo cotizante list carries more than forty - copying a PILA code straight into the XML is a documented failure. PRIVATE-SECTOR FILTER, excluded codes: 02 (servicio doméstico) and 04 (madre comunitaria) - private but outside standard corporate payroll and descoped in scope_manifest; 18, 30, 47 and 58 - public sector; 31 - associated-work cooperative members without a labour contract; 20 - Ley 789 de 2002 students (planilla K); 40 (beneficiario de UPC adicional) - a health-coverage beneficiary of a contributor, not an employee, absent from table 5.5.3 altogether and excluded from the PILA header contributor count; and every independent-worker, pensioner-paid-by-fund, councillor, taxi-driver and UGPP code (03, 16, 32-36, 42-45, 52, 53, 55, 57, 59-63). The nine codes retained here are a strict subset of Anexo Tecnico table 5.5.3, so every value is valid in both the nomina electronica XML and PILA. |
|  | 12 | APR-L | Aprendiz del SENA en etapa lectiva | Apprentice, classroom phase. Reduced contribution scenario - health only in the lectiva phase. |  |
|  | 19 | APR-P | Aprendiz del SENA en etapa productiva | Apprentice, productive phase. Full contribution scenario. |  |
|  | 21 | EST-PG | Estudiante de postgrado en salud | Health postgraduate student contributing through the host institution. |  |
|  | 22 | PROF | Profesor de establecimiento particular | Teacher at a private establishment - expressly a private-sector category. |  |
|  | 23 | EST-RL | Estudiante con aporte solo a riesgos laborales | Student on placement contributing to occupational risk only. Pairs with contract type 5. |  |
|  | 51 | PARC | Trabajador de tiempo parcial | Part-time worker under the special partial-time contribution regime of Ley 2466 de 2025 art. 34. Uses the hours-worked field instead of the one-minimum-wage base floor. |  |
|  | 54 | PREP | Prepensionado de entidad en liquidación | Pre-pensioner of an entity in liquidation. Pairs with planilla type X. |  |
|  | 56 | PREP-V | Prepensionado con aporte voluntario a salud | Pre-pensioner making a voluntary health contribution. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Worker Sub-Type | 00 | NA | No aplica | No sub-type applies. The value for almost every employee. | Referenced by Worker Sub-Type (Mandatory=Y, CO-DIAN-001 NIE042 table 5.5.4 and CO-PILA-003 T2R2-006). HARD RULE (PILA Anexo Tecnico 2): where the sub-type is 1, 2, 3, 4, 5, 6, 9 or 12 the PILA pension-contribution rate field T2R2-046 MUST be 0; of those, 01, 03, 04, 05, 06 and 09 are in scope here and 02 and 12 are excluded populations. CODE WIDTH TRAP: PILA writes the sub-type as a single digit (0, 1, 3...) while the nomina electronica table 5.5.4 writes two (00, 01); the master value is stored zero-filled to two positions and narrowed on output. MAPPING TRAP: the nómina electrónica table carries ONLY 00 and 01; PILA carries the wider list. This field, not a separate flag, carries the 'employed active pensioner' attribute. PRIVATE-SECTOR FILTER, excluded codes: 02 (independiente pensionado activo), 10 (residente en el exterior afiliado voluntario) and 11/12 (conductores de taxi) - all self-insured or non-employee categories. |
|  | 01 | PEN-DEP | Dependiente pensionado por vejez, jubilación o invalidez activo | Employed old-age, retirement or disability pensioner in active service. NO pension contribution; health and the payroll levies still apply. The only sub-type with a nómina electrónica equivalent. |  |
|  | 03 | EDAD | Cotizante no obligado a cotizar a pensiones por edad | Employee not obliged to contribute to pension by reason of age. Pension rate must be 0. |  |
|  | 04 | REQ | Cotizante con requisitos cumplidos para pensión | Employee who has met the pension requirements. Pension rate must be 0. |  |
|  | 05 | IND-SUST | Cotizante con indemnización sustitutiva o devolución de saldos reconocida | Employee granted a substitute indemnity or return of balances. Pension rate must be 0. |  |
|  | 06 | EXCEP | Cotizante de régimen exceptuado de pensiones | Employee under a pension regime excepted from the general system. Pension rate must be 0. |  |
|  | 09 | MESADA | Pensionado con mesada igual o superior a 25 SMLMV | Pensioner whose pension equals or exceeds 25 minimum wages. Pension rate must be 0. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Pay Frequency | 1 | SEM | Semanal | Weekly. | Referenced by Pay Frequency (Mandatory=Y, CO-DIAN-001 NIE029, Anexo Técnico table 5.5.1). Labour Code art. 134 caps the interval at one month for monthly salaries and one week for day wages; any shorter frequency is permitted. CRITICAL: whatever the value, the electronic payroll support document is ONE MONTHLY document per employee (Res. DIAN 000013 de 2021 art. 3) - a semi-monthly payroll does NOT produce two filings a month. |
|  | 2 | DEC | Decenal | Every ten days. |  |
|  | 3 | CAT | Catorcenal | Every fourteen days. |  |
|  | 4 | QUI | Quincenal | Semi-monthly - the most common Colombian cycle. Still one monthly document, carrying two payment-date occurrences. |  |
|  | 5 | MEN | Mensual | Monthly. |  |
|  | 6 | OTR | Otro | Any other cycle. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Payment Form | 1 | CONT | Contado | Cash / immediate settlement. The only published value. | Referenced by Payment Form (Mandatory=Y, CO-DIAN-001 NIE064, Anexo Técnico table 5.3.3.1). The annex publishes a single value. Distinct from Payment Method: 'forma' is the settlement form, 'método' is the medium. |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Payment Method | 10 | EFEC | Efectivo | Cash. The bank attributes must be absent. | Referenced by Payment Method (Mandatory=Y, CO-DIAN-001 NIE065, Anexo Técnico table 5.3.3.2). CONSTRAINT: bidirectional set with the three bank fields - where the value is 10 (efectivo) the bank name, account type and account number attributes MUST BE ABSENT; for every bank-mediated medium all three are required. The complete UN/EDIFACT 4461 catalogue (codes 1 to 97) is printed at Anexo table 5.3.3.2; the values below are those used in payroll. |
|  | 20 | CHEQ | Cheque | Cheque. |  |
|  | 42 | CONS | Consignación bancaria | Bank deposit. The most common Colombian payroll method. |  |
|  | 45 | TCB | Transferencia crédito bancario | Bank credit transfer. |  |
|  | 47 | TDB | Transferencia débito bancaria | Bank debit transfer. |  |
|  | 48 | TCRE | Tarjeta crédito | Credit card. |  |
|  | 49 | TDEB | Tarjeta débito | Debit card. |  |
|  | 71 | BON | Bonos | Vouchers. Where salary is paid in vouchers the amount also belongs in the BonoEPCTV devengado elements of the XML. |  |
|  | 72 | VAL | Vales | Vales / meal tickets. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Bank Account Type | AHORROS | AHO | Cuenta de ahorros | Savings account. | Referenced by Employee Bank Account Type (Mandatory=C, CO-DIAN-001 NIE067). CONSTRAINT: populated together with Employee Bank Name and Employee Bank Account Number whenever Payment Method is a bank-mediated medium; absent for a cash payment. Colombia has only these two account types and does NOT use IBAN. |
|  | CORRIENTE | CTE | Cuenta corriente | Current account. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Work Modality | PRES | PRES | Trabajo presencial | On-site work. The default. | Referenced by Work Modality (Mandatory=C). Legal basis: Ley 1221 de 2008 as amended by Ley 2466 de 2025 arts. 52-54; CCG Module 4. CONSTRAINT: mandatory where the employee is a teleworker; defaults to PRES otherwise. Calculation-driving - a teleworker earning less than two minimum wages receives the MANDATORY connectivity allowance IN PLACE OF the transport allowance, and the two are NEVER paid together. |
|  | TT-AUT | AUT | Teletrabajo autónomo | Autonomous telework - the employee works wholly outside the employer's premises. |  |
|  | TT-MOV | MOV | Teletrabajo móvil | Mobile telework - the employee has no fixed workplace and relies on mobile devices. |  |
|  | TT-SUP | SUP | Teletrabajo suplementario | Supplementary telework - the employee alternates between the employer's premises and a remote location. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Tax Residence Status | RES | RES | Residente fiscal | Colombian tax resident. Withheld on the progressive art. 383 table (0/19/28/33/35/37/39%) applied to the art. 388 depurated base, by Procedure 1 or Procedure 2. | Referenced by Tax Residence Status (Mandatory). THE SINGLE MOST CONSEQUENTIAL WITHHOLDING SWITCH IN COLOMBIAN PAYROLL. Tax Code art. 10 residence tests; DIAN Concepto 011108 of 29 June 2026. The switch is PROSPECTIVE, never retroactive - acquiring residence does not reopen earlier months. Independent of Nationality: a Colombian national can be a non-resident and a foreign national can be a resident. |
|  | NRES | NRES | No residente fiscal | Non-resident. Withheld at a FLAT 20% under art. 408 on the GROSS payment: no art. 388 depuration, no 25% exempt income, no art. 387 deductions, no tax-free band and no procedure election. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Withholding Procedure | 1 | P1 | Procedimiento 1 | Tax Code art. 385. Each month stands alone; the statutory minimum service bonus is withheld separately on its own read of the art. 383 table. A sub-30-day period is grossed to 30 days. | Referenced by Withholding Procedure (Mandatory). Employer election made PER EMPLOYEE; once elected, Procedure 2 binds for the whole six-month semester. CONSTRAINT: not applicable to a non-resident, who is withheld at the flat art. 408 rate with no procedure. The fixed percentage produced by the June/December recalculation is a CALCULATED value (WTC), not master data. |
|  | 2 | P2 | Procedimiento 2 | Tax Code art. 386. A fixed percentage recomputed each June and December from the preceding 12 months; the service bonus sits inside the ordinary base and is NOT given a separate table read. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Treaty Status | SIN CONVENIO | SC | Países sin convenio | No double-tax treaty in force. Payment-concept list 1 to 18; the employee concept is 5 (prestación de servicios y compensación por servicios personales) at the 20% general rate of ET art. 408. | Referenced by Treaty Status (Mandatory=C, CO-DIAN-002 casilla 141). CONSTRAINT: required on every Formulario 350 annex row, i.e. wherever a payment is made to a non-resident; not applicable to a resident employee. Where the value is CON CONVENIO the treaty country must be one with a treaty in force. |
|  | CON CONVENIO | CC | Países con convenio vigente | A double-tax treaty is in force. Payment-concept list 19 to 33; the employee concept is 24 (rentas de trabajo) and the rate comes from the applicable treaty, which may be lower than 20% or nil. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Dependant Relationship | HIJO-M18 | H18 | Hijo o hija menor de 18 años | Child under 18. No further condition. | Referenced by Dependant Relationship (Mandatory=C, CO-DIAN-004 casilla 82 and CO-DIAN-005). CONSTRAINT: populated as a bidirectional set with the dependant's document type, document number and full name - all four together or none. The five limbs of ET art. 387 par. 2 are EXHAUSTIVE: a person outside them is not a dependant however genuine the support. Formulario 220 casilla 82 accepts free text, so the engine emits the Local Name; the Code column is the Mercans-internal normalisation. Qualifying evidence must be retained. |
|  | HIJO-EST | HED | Hijo o hija entre 18 y 23 años en formación | Child aged 18 to 23 whose education the taxpayer finances at a recognised institution. |  |
|  | HIJO-DEP | HDP | Hijo o hija mayor de 23 años en situación de dependencia certificada | Child over 23 with certified physical or psychological dependency. |  |
|  | CONYUGE | CON | Cónyuge o compañero permanente en situación de dependencia | Spouse or permanent partner in a certified state of dependency by absence of income or by physical or psychological condition. |  |
|  | ASCEND-HERM | APH | Padres y hermanos en situación de dependencia | Parents and siblings in a certified state of dependency. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Pension Regime | RPM | RPM | Régimen de Prima Media con Prestación Definida | Public defined-benefit, pay-as-you-go regime administered by Colpensiones. Additional voluntary contributions are contributions, not a tax relief. | Referenced by Pension Regime (Mandatory). CCG Module 5. Employee election that survives a change of employer and must be declared by a new joiner. Determines which administrator catalogue the AFP code is drawn from and which voluntary-contribution route is available. The CONTRIBUTION RATES are identical across the two regimes and are parameters (WTC). |
|  | RAIS | RAIS | Régimen de Ahorro Individual con Solidaridad | Private funded individual-account regime administered by the pension administrators. Voluntary contributions to the individual account are non-taxable income under ET art. 55 within the statutory caps. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Severance-Savings Fund | 02 | PROTECCION | Fondo de Cesantías Protección (Protección S.A.) | Private severance-savings fund administered by Protección S.A. | Referenced by Severance-Savings Fund Code (Mandatory=Y, CO-CESANTIAS-006 T09) and by Single-Fund Planilla Severance Fund Code (Mandatory=C). CONSTRAINT: the per-employee value is IGNORED where the employer files a single-fund planilla (E07 = Y), in which case the planilla-level fund overwrites every record. Codes are validated against the registered list of severance-savings funds - ANY OTHER VALUE IS REJECTED. Misdirecting a deposit costs one day's salary per day of delay, per employee, uncapped (Ley 50 de 1990 art. 99 num. 3). |
|  | 03 | PORVENIR | Porvenir Cesantías (Porvenir S.A.) | Private severance-savings fund administered by Porvenir S.A., the largest by affiliates. |  |
|  | 10 | COLFONDOS | Colfondos Cesantías (Colfondos S.A. Pensiones y Cesantías) | Private severance-savings fund administered by Colfondos S.A. |  |
|  | 15 | FNA | Fondo Nacional del Ahorro (FNA) | The state-owned fund, an Empresa Industrial y Comercial del Estado. IN SCOPE despite being state-owned: it is an EMPLOYEE election open to private-sector employees, not a public-sector employment category. |  |
|  | 19 | SKANDIA | Skandia (etiqueta publicada: 'Old Mutual (antes Skandia)') | STALE LABEL, LIVE CODE. The published layout prints 'Old Mutual (Antes Skandia)' but the administrator trades as Skandia. Use the code, not the printed label. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Severance-Savings Regime | LEY50 | L50 | Régimen de Ley 50 de 1990 - consignación anual | The annual-deposit regime. The default for everyone hired from 1 January 1991. Deposited to the employee's chosen fund by 14 February. Reported at Formulario 220 casilla 49 and Formato 2276 numeral N19. | Referenced by Severance-Savings Regime (Mandatory). REPORTING TRAP: Formulario 220 reports the pre-1991 traditional regime at casilla 48 and the amount deposited to the fund at casilla 49, while Formato 2276 reports them in the OPPOSITE order at numerals N19 (fund) and N20 (traditional). MAP BY MEANING, NEVER BY POSITION. |
|  | TRADICIONAL | TRAD | Régimen tradicional retroactivo del CST (anterior a 1991) | The pre-1991 retroactive regime, for employees hired before 1 January 1991 who did not switch. Reported at Formulario 220 casilla 48 and Formato 2276 numeral N20. |  |
|  | INTEGRAL | INT | Salario integral - sin cesantías | All-inclusive salary under Labour Code art. 132 num. 2: severance savings, severance interest and the service bonus are already inside the salary, so no separate accrual and no deposit arise. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Severance-Savings Deposit Arrangement | ANUAL | ANU | Consignación anual al fondo de cesantías | The ordinary route: liquidation at 31 December, deposit to the employee's chosen fund by 14 February. Ley 50 de 1990 art. 99 nums. 1-3. | Referenced by Severance-Savings Deposit Arrangement (Mandatory=C). CONSTRAINT: the value MENSUAL is the one that maps to Y in the spec field Contract.Cesantias_Regime (CO-CESANTIAS-006 MA01) and it GATES the monthly-advance fields MA02 to MA05 - where the value is anything else, those fields are not produced and the ordinary annual detail record is the only route. MENSUAL and DIRECTO each require a WRITTEN agreement on file. |
|  | MENSUAL | MEN | Consignación mensual anticipada del 8,33% | Monthly advance deposit of 8.33% plus monthly payment of the 1% interest, by written agreement. Ley 2466 de 2025 art. 64, adding two paragraphs to Ley 50 de 1990 art. 99. |  |
|  | DIRECTO | DIR | Pago directo al trabajador (liberatorio) | Direct payment to the employee discharging the deposit obligation. Labour Code art. 57 par. 4, added by Ley 2466 de 2025 art. 15. No planilla record and no penalty, but the evidence must be retained; fund affiliation remains compulsory. |  |
|  | NA | NA | No aplica | All-inclusive salary, a leaver settled in the final settlement, or the pre-1991 retroactive regime. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Occupational Risk Class | I | I | Riesgo mínimo | Initial rate 0.522%; permitted range 0.348% to 0.696%. Offices, financial services, commerce. | Referenced by Work Centre Occupational Risk Class (Mandatory=Y, CO-PILA-003 T2R2-078). THE CLASS ATTACHES TO THE WORK CENTRE, NOT TO THE COMPANY (Decreto 1072 de 2015 art. 2.2.4.2.5.6): a company with a corporate office and a plant legitimately carries two classes and two rates, and each employee follows the class of the centre where they work. Bidirectional set with Work Centre Code and the VCT change-of-work-centre event. THE RATES BELOW ARE SHOWN FOR ORIENTATION ONLY - they are parameters held in the WTC, not master data. |
|  | II | II | Riesgo bajo | Initial rate 1.044%; permitted range 0.435% to 1.653%. Light manufacturing, textiles. |  |
|  | III | III | Riesgo medio | Initial rate 2.436%; permitted range 0.783% to 4.089%. Heavier manufacturing, food processing. |  |
|  | IV | IV | Riesgo alto | Initial rate 4.350%. RECORDED DEFECT: Decreto 1072 de 2015 art. 2.2.4.3.5 prints the class IV initial rate inconsistently - see the CO-PILA-003 Field Options note. |  |
|  | V | V | Riesgo máximo | Initial rate 6.960%; global maximum 8.700%. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Social Security Subsystem | SALUD | SAL | Salud | Health. Employee 4% / employer 8.5%; base capped at 25 minimum wages. The EMPLOYER limb is exonerable under ET art. 114-1 below a 10-minimum-wage base. | Reference mapper for the eight contribution subsystems that the employer settles through the integrated contribution return. Referenced indirectly by the fund-code fields (EPS, AFP, CCF, ARL) and by the art. 114-1 exoneration flag. Scope option_mapper_scope.insurance_type. THE RATES, BASES AND CEILINGS ARE PARAMETERS HELD IN THE WTC, NOT MASTER DATA - they appear here only to identify the subsystem unambiguously. |
|  | PENSION | PEN | Pensión | Pension. Employee 4% / employer 12%; base capped at 25 minimum wages and floored at 1. NEVER exonerable. |  |
|  | FSP-SOL | FSPS | Fondo de Solidaridad Pensional - subcuenta de solidaridad | Employee-borne 1%, from a contribution base of 4 minimum wages. |  |
|  | FSP-SUB | FSPU | Fondo de Solidaridad Pensional - subcuenta de subsistencia | Employee-borne, banded 0.2% to 1.0%, from a contribution base of 16 minimum wages. |  |
|  | ARL | ARL | Riesgos laborales | Occupational risk. EMPLOYER ONLY, by risk class of the WORK CENTRE; global bounds 0.348% to 8.700%. Never exonerable. |  |
|  | CCF | CCF | Caja de compensación familiar | Family compensation fund. Employer 4% on the payroll-levy base, no ceiling. NEVER exonerable under art. 114-1. |  |
|  | SENA | SENA | Servicio Nacional de Aprendizaje | Training levy. Employer 2% on the payroll-levy base, no ceiling. Exonerable under art. 114-1. |  |
|  | ICBF | ICBF | Instituto Colombiano de Bienestar Familiar | Family-welfare levy. Employer 3% on the payroll-levy base, no ceiling. Exonerable under art. 114-1. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| PILA Novedad (Change Event) Type | ING | ING | Ingreso | Hire. Makes the hire-date field mandatory. | Reference mapper for the change events reported per contributor on the integrated contribution return. Scope option_mapper_scope.benefit_type. THESE ARE TRANSACTIONAL PER-PAYRUN VALUES, NOT MASTER DATA - the mapper is documented here because each event GATES the conditionality of a master-data field, as recorded in the Pre-Condition column: ING -> Hire Date; RET -> Termination Date; TAE -> EPS Transfer Code; TAP -> AFP Transfer Code; VCT -> Work Centre Code. The DAY COUNTS and AMOUNTS the events carry are payroll inputs and calculated values (WTC). |
|  | RET | RET | Retiro | Termination. Makes the termination-date field mandatory. |  |
|  | TDE | TDE | Traslado desde otra EPS o EOC | Transfer FROM another health insurer. |  |
|  | TAE | TAE | Traslado a otra EPS o EOC | Transfer TO another health insurer. Makes the EPS transfer code mandatory. |  |
|  | TDP | TDP | Traslado desde otra administradora de pensiones | Transfer FROM another pension administrator. |  |
|  | TAP | TAP | Traslado a otra administradora de pensiones | Transfer TO another pension administrator. Makes the AFP transfer code mandatory. |  |
|  | VSP | VSP | Variación permanente de salario | Permanent salary variation. Makes the new-salary field mandatory. |  |
|  | VST | VST | Variación transitoria del salario | One-off transitory variation of the contribution base. |  |
|  | SLN | SLN | Suspensión temporal del contrato o licencia no remunerada | Contract suspension or unpaid leave. Health moves to 8.5% or 0%, pension to 12% or 16%, and the payroll levies to 0%. Makes the from/to date fields mandatory. |  |
|  | IGE | IGE | Incapacidad temporal por enfermedad general | General sickness absence. The employer bears days 1-2 (Decreto 780 de 2016 art. 3.2.1.10); the health insurer funds from day 3. |  |
|  | LMA | LMA | Licencia de maternidad o paternidad | Maternity or paternity leave. Benefit funded by the health insurer; record-only for the employer. |  |
|  | VAC | VAC | Vacaciones | Annual leave. Carried in a THREE-VALUE flag shared with paid leave - value X. |  |
|  | LR | LR | Licencia remunerada | Other paid leave. The same flag as vacaciones - value L. The two map to DIFFERENT nómina electrónica blocks and must not be merged. |  |
|  | IRL | IRL | Incapacidad por accidente de trabajo o enfermedad laboral | Occupational accident or disease absence. NOT a flag - a DAY COUNT from 00 to 30. Funded by the occupational-risk insurer from day one at 100%. |  |
|  | AVP | AVP | Aporte voluntario a pensión | Voluntary pension contribution reported in the period. |  |
|  | VCT | VCT | Variación de centro de trabajo | Change of work centre. Makes the work-centre fields mandatory and may change the occupational-risk class and therefore the rate. |  |
|  | A | CORR-A | Corrección - adición de cotizante omitido | Correction limb A: adds a contributor omitted from the original planilla. Meaningful only on planilla type N. |  |
|  | C | CORR-C | Corrección - corrección de cotizante reportado | Correction limb C: corrects a contributor already reported. Paired with an A record; the sum of C bases and days must be greater than or equal to the sum of A. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Employer Person Type | J | JUR | Jurídica | Legal person. The ordinary corporate employer. | Referenced by Employer Person Type (Mandatory=Y, CO-PILA-003 A1-009). GATES a large conditional block: where J, the NIT verification digit and the whole legal-representative block (document type, number, DV and the four name fields) become mandatory; where N, the verification digit must be ZERO and the employer document type narrows to the natural-person list. |
|  | N | NAT | Natural | Natural person acting as employer. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Employer Legal Nature | 2 | PRIV | Privada | Private entity. THE IN-SCOPE POPULATION for the Mercans platform. | Referenced by Employer Legal Nature (Mandatory=Y, CO-PILA-003 A1-008). PRIVATE-SECTOR FILTER: only value 2 is in scope. EXCLUDED codes and why: 1 Pública - public entity, separate legislation; 3 Mixta - mixed-capital entity, partly public; 4 Organismos multilaterales - multilateral organisation, aportante type 6 and out of scope; 5 Entidades de derecho público no sometidas a la legislación colombiana - typically a foreign mission, out of scope. An employer presenting any of these values must be rejected at validation, not silently processed. |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Class of Contributor | A | 200+ | Aportante con 200 o más cotizantes | Employer with 200 or more contributors, counted across all branches. | Referenced by Class of Contributor (Mandatory=Y, CO-PILA-003 A1-007). The headcount is counted across ALL branches and dependencies of the legal person, NOT per branch. CONSTRAINT: class D makes the commercial-registry date and the registered-seat department code mandatory and is normally accompanied by Ley 1429 CCF benefit = S. All four values are private-sector. |
|  | B | <200 | Aportante con menos de 200 cotizantes | Employer with fewer than 200 contributors. The default for most corporate employers. |  |
|  | C | MIPYME | Aportante Mipyme acogido a la Ley 590 de 2000 | Fewer than 200 contributors AND eligible for the SENA, ICBF and family-compensation-fund discounts of Ley 590 de 2000. |  |
|  | D | LEY1429 | Aportante beneficiario de la Ley 1429 de 2010 | Beneficiary of the formalisation and employment-generation regime, Decreto 1074 de 2015 art. 2.2.2.42.1. Requires the commercial-registry date. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Contributor Type | 1 | EMPL | Empleador | Employer. THE IN-SCOPE VALUE for private corporate payroll. | Referenced by Contributor Type (Mandatory=Y, CO-PILA-003 A1-030 and T2R1-021). PRIVATE-SECTOR FILTER: only value 1 is in scope. EXCLUDED codes and why: 2 Independiente - self-insured, contributes on 40% of fees and is not an employer filing; 3 Entidades o universidades públicas de regímenes especial y de excepción - public sector; 4 Agremiaciones, asociaciones o congregaciones religiosas; 5 Cooperativas y precooperativas de trabajo asociado - members without a labour contract; 6 Misiones diplomáticas, consulares o de organismos multilaterales; 7 Hogares de Bienestar; 8 Pagador de concejales y ediles; 9 Contrato sindical; 10 Programa de reincorporación; 11 Parafiscales del Magisterio; 12 Prestación humanitaria. None of these is a private-sector employment relationship settled through corporate payroll. |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Form of Presentation | U | UNICO | Único | A single consolidated planilla for the whole legal person. Branch code and name blank. | Referenced by Form of Presentation (Mandatory=Y, CO-PILA-003 A1-010). CONSTRAINT: bidirectional pair with Branch or Dependency Code and Branch or Dependency Name - where the value is U both MUST BE BLANK; where it is S both become required, and the Archivo Tipo 2 header values must equal the Archivo Tipo 1 values. |
|  | S | SUC | Sucursal | One planilla per branch. Branch code and name required. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| PILA Filing Modality | 1 | ELEC | Electrónica | Prepared and paid over the internet on the operador's site. | Referenced by PILA Filing Modality (Mandatory). Employer-level election gated by headcount under Decreto 780 de 2016 art. 3.2.3.9 as substituted by Decreto 1990 de 2016; the headcount is aggregated across all branches under the same legal person. The THRESHOLD is a parameter (WTC); the elected modality is master data. |
|  | 2 | ASIST | Asistida | The employer instructs the operador's call centre, which keys or digitises the information. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| PILA Planilla Type | E | EMPL | Planilla empleados | THE IN-SCOPE DEFAULT. Regular monthly payment for dependent contributors. | Referenced by PILA Planilla Type (Mandatory). Scope option_mapper_scope.correction_codes. The employer's DEFAULT is master data; the value used in a given run may be overridden by the event, and that override is TRANSACTIONAL. CONSTRAINT: planilla type N requires the associated planilla number and date, and its A/C record pairs must satisfy sum(C bases and days) >= sum(A). PRIVATE-SECTOR / SCOPE FILTER, excluded types: S (servicio doméstico), I and Y (independientes - contribute on 40% of fees, the payer is not an employer), T and F (Sistema General de Participaciones - public sector only), H (madres sustitutas), K (estudiantes Ley 789 de 2002), U and O (UGPP third-party and UGPP-determined liabilities). |
|  | A | ING | Planilla cotizantes con novedad de ingreso | New joiners omitted from the month's main planilla, settled separately with no late interest. |  |
|  | N | CORR | Planilla correcciones | Correction of an earlier planilla - contribution base, rate, contributor type or sub-type, or an omitted change event - in paired A/C record groups. |  |
|  | M | MORA | Planilla mora | Periods with a total absence of payment. The operador computes interest on arrears. |  |
|  | J | JUD | Planilla pago en cumplimiento de sentencia judicial | Court-ordered settlement: reinstatement, contrato realidad, or reliquidation of salary factors omitted from the original liquidation. |  |
|  | X | LIQ | Planilla para el pago de empresa liquidada | Liquidated company. Pairs with worker types 54 and 56. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Employer Status Action Type | 1 | CONC | Concordato | Insolvency arrangement. | Referenced by Employer Status Action Type (Mandatory=C, CO-PILA-003 A1-026). CONSTRAINT: optional in general, but where populated it makes the insolvency start date MANDATORY and the commercial-activity cessation date required - a bidirectional set of three fields. |
|  | 2 | REEST | Reestructuración | Restructuring. |  |
|  | 3 | LIQ | Liquidación | Liquidation. |  |
|  | 4 | CESE | Cese de actividades | Cessation of activities. Fixes the date from which the employer is no longer obliged to contribute. |  |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Formato 2276 Informant Type | 1 | GEN | Informante general | THE VALUE FOR AN ORDINARY EMPLOYER reporting payments for rentas de trabajo. | Referenced by Formato 2276 Informant Type (Mandatory). Res. DIAN 000227 de 2025 par. 4. CONSTRAINT: where the value is 1, the trust identification (numeral 35) and the contract-participant numeral (36) 'no se deben diligenciar' - they are mutually exclusive with the ordinary-employer case. EXCLUDED values 2 to 8 (fiduciarias, mandatario o administrador delegado, consorcio o unión temporal, hidrocarburos, joint venture, cuentas en participación, convenios de cooperación con entidades públicas) attach to structures that are not ordinary employer payroll and each requires numeral 35 or 36. |
| Option Mapper Description | Code | Abbreviation | Local Name | English Description | Constraint / Notes |
| Yes/No Indicator | S | SI | Sí | Yes / the condition applies. | Generic two-value indicator referenced by every S/N master-data flag in this dictionary: Colombian Abroad Flag, All-Inclusive Salary Flag, Non-Salary Pact Flag, High-Risk Pension Activity Flag, Foreign National Not Liable to Pension Flag, Concurrent Employer Flag, 36-Hour Shift System Flag, Disability Status, Art. 380 Non-Filer Declaration, Exonerated from Health/SENA/ICBF and Ley 1429 art. 5 CCF Benefit. EMISSION RULE: on the PILA fixed-width file several of these are emitted as BLANK or X rather than S or N - the fixed-width emission is a formatting concern, the stored master value is always S or N. CONSTRAINT on the exoneration flag: N is MANDATORY where the health contribution base reaches 10 minimum wages. |
|  | N | NO | No | No / the condition does not apply. |  |



---

## Sheet 7 - Currency Codes, ISO 4217 (template reference, DO NOT TOUCH)


**DO NOT TOUCH**
**Currency Codes (ISO 4217)**


| Country | Currency | Alphabetic Code | Numeric Code | Minor unit |
|---|---|---|---|---|
| AFGHANISTAN | Afghani | AFN | 971 | 2 |
| ÅLAND ISLANDS | Euro | EUR | 978 | 2 |
| ALBANIA | Lek | ALL | 008 | 2 |
| ALGERIA | Algerian Dinar | DZD | 012 | 2 |
| AMERICAN SAMOA | US Dollar | USD | 840 | 2 |
| ANDORRA | Euro | EUR | 978 | 2 |
| ANGOLA | Kwanza | AOA | 973 | 2 |
| ANGUILLA | East Caribbean Dollar | XCD | 951 | 2 |
| ANTIGUA AND BARBUDA | East Caribbean Dollar | XCD | 951 | 2 |
| ARGENTINA | Argentine Peso | ARS | 032 | 2 |
| ARMENIA | Armenian Dram | AMD | 051 | 2 |
| ARUBA | Aruban Florin | AWG | 533 | 2 |
| AUSTRALIA | Australian Dollar | AUD | 036 | 2 |
| AUSTRIA | Euro | EUR | 978 | 2 |
| AZERBAIJAN | Azerbaijan Manat | AZN | 944 | 2 |
| BAHAMAS (THE) | Bahamian Dollar | BSD | 044 | 2 |
| BAHRAIN | Bahraini Dinar | BHD | 048 | 3 |
| BANGLADESH | Taka | BDT | 050 | 2 |
| BARBADOS | Barbados Dollar | BBD | 052 | 2 |
| BELARUS | Belarusian Ruble | BYN | 933 | 2 |
| BELGIUM | Euro | EUR | 978 | 2 |
| BELIZE | Belize Dollar | BZD | 084 | 2 |
| BENIN | CFA Franc BCEAO | XOF | 952 | 0 |
| BERMUDA | Bermudian Dollar | BMD | 060 | 2 |
| BHUTAN | Indian Rupee | INR | 356 | 2 |
| BHUTAN | Ngultrum | BTN | 064 | 2 |
| BOLIVIA (PLURINATIONAL STATE OF) | Boliviano | BOB | 068 | 2 |
| BOLIVIA (PLURINATIONAL STATE OF) | Mvdol | BOV | 984 | 2 |
| BONAIRE, SINT EUSTATIUS AND SABA | US Dollar | USD | 840 | 2 |
| BOSNIA AND HERZEGOVINA | Convertible Mark | BAM | 977 | 2 |
| BOTSWANA | Pula | BWP | 072 | 2 |
| BOUVET ISLAND | Norwegian Krone | NOK | 578 | 2 |
| BRAZIL | Brazilian Real | BRL | 986 | 2 |
| BRITISH INDIAN OCEAN TERRITORY (THE) | US Dollar | USD | 840 | 2 |
| BRUNEI DARUSSALAM | Brunei Dollar | BND | 096 | 2 |
| BULGARIA | Bulgarian Lev | BGN | 975 | 2 |
| BURKINA FASO | CFA Franc BCEAO | XOF | 952 | 0 |
| BURUNDI | Burundi Franc | BIF | 108 | 0 |
| CABO VERDE | Cabo Verde Escudo | CVE | 132 | 2 |
| CAMBODIA | Riel | KHR | 116 | 2 |
| CAMEROON | CFA Franc BEAC | XAF | 950 | 0 |
| CANADA | Canadian Dollar | CAD | 124 | 2 |
| CAYMAN ISLANDS (THE) | Cayman Islands Dollar | KYD | 136 | 2 |
| CENTRAL AFRICAN REPUBLIC (THE) | CFA Franc BEAC | XAF | 950 | 0 |
| CHAD | CFA Franc BEAC | XAF | 950 | 0 |
| CHILE | Chilean Peso | CLP | 152 | 0 |
| CHILE | Unidad de Fomento | CLF | 990 | 4 |
| CHINA | Yuan Renminbi | CNY | 156 | 2 |
| CHRISTMAS ISLAND | Australian Dollar | AUD | 036 | 2 |
| COCOS (KEELING) ISLANDS (THE) | Australian Dollar | AUD | 036 | 2 |
| COLOMBIA | Colombian Peso | COP | 170 | 2 |
| COLOMBIA | Unidad de Valor Real | COU | 970 | 2 |
| COMOROS (THE) | Comorian Franc | KMF | 174 | 0 |
| CONGO (THE DEMOCRATIC REPUBLIC OF THE) | Congolese Franc | CDF | 976 | 2 |
| CONGO (THE) | CFA Franc BEAC | XAF | 950 | 0 |
| COOK ISLANDS (THE) | New Zealand Dollar | NZD | 554 | 2 |
| COSTA RICA | Costa Rican Colon | CRC | 188 | 2 |
| CÔTE D'IVOIRE | CFA Franc BCEAO | XOF | 952 | 0 |
| CROATIA | Kuna | HRK | 191 | 2 |
| CUBA | Cuban Peso | CUP | 192 | 2 |
| CUBA | Peso Convertible | CUC | 931 | 2 |
| CURAÇAO | Netherlands Antillean Guilder | ANG | 532 | 2 |
| CYPRUS | Euro | EUR | 978 | 2 |
| CZECHIA | Czech Koruna | CZK | 203 | 2 |
| DENMARK | Danish Krone | DKK | 208 | 2 |
| DJIBOUTI | Djibouti Franc | DJF | 262 | 0 |
| DOMINICA | East Caribbean Dollar | XCD | 951 | 2 |
| DOMINICAN REPUBLIC (THE) | Dominican Peso | DOP | 214 | 2 |
| ECUADOR | US Dollar | USD | 840 | 2 |
| EGYPT | Egyptian Pound | EGP | 818 | 2 |
| EL SALVADOR | El Salvador Colon | SVC | 222 | 2 |
| EL SALVADOR | US Dollar | USD | 840 | 2 |
| EQUATORIAL GUINEA | CFA Franc BEAC | XAF | 950 | 0 |
| ERITREA | Nakfa | ERN | 232 | 2 |
| ESTONIA | Euro | EUR | 978 | 2 |
| ESWATINI | Lilangeni | SZL | 748 | 2 |
| ETHIOPIA | Ethiopian Birr | ETB | 230 | 2 |
| EUROPEAN UNION | Euro | EUR | 978 | 2 |
| FALKLAND ISLANDS (THE) [MALVINAS] | Falkland Islands Pound | FKP | 238 | 2 |
| FAROE ISLANDS (THE) | Danish Krone | DKK | 208 | 2 |
| FIJI | Fiji Dollar | FJD | 242 | 2 |
| FINLAND | Euro | EUR | 978 | 2 |
| FRANCE | Euro | EUR | 978 | 2 |
| FRENCH GUIANA | Euro | EUR | 978 | 2 |
| FRENCH POLYNESIA | CFP Franc | XPF | 953 | 0 |
| FRENCH SOUTHERN TERRITORIES (THE) | Euro | EUR | 978 | 2 |
| GABON | CFA Franc BEAC | XAF | 950 | 0 |
| GAMBIA (THE) | Dalasi | GMD | 270 | 2 |
| GEORGIA | Lari | GEL | 981 | 2 |
| GERMANY | Euro | EUR | 978 | 2 |
| GHANA | Ghana Cedi | GHS | 936 | 2 |
| GIBRALTAR | Gibraltar Pound | GIP | 292 | 2 |
| GREECE | Euro | EUR | 978 | 2 |
| GREENLAND | Danish Krone | DKK | 208 | 2 |
| GRENADA | East Caribbean Dollar | XCD | 951 | 2 |
| GUADELOUPE | Euro | EUR | 978 | 2 |
| GUAM | US Dollar | USD | 840 | 2 |
| GUATEMALA | Quetzal | GTQ | 320 | 2 |
| GUERNSEY | Pound Sterling | GBP | 826 | 2 |
| GUINEA | Guinean Franc | GNF | 324 | 0 |
| GUINEA-BISSAU | CFA Franc BCEAO | XOF | 952 | 0 |
| GUYANA | Guyana Dollar | GYD | 328 | 2 |
| HAITI | Gourde | HTG | 332 | 2 |
| HAITI | US Dollar | USD | 840 | 2 |
| HEARD ISLAND AND McDONALD ISLANDS | Australian Dollar | AUD | 036 | 2 |
| HOLY SEE (THE) | Euro | EUR | 978 | 2 |
| HONDURAS | Lempira | HNL | 340 | 2 |
| HONG KONG | Hong Kong Dollar | HKD | 344 | 2 |
| HUNGARY | Forint | HUF | 348 | 2 |
| ICELAND | Iceland Krona | ISK | 352 | 0 |
| INDIA | Indian Rupee | INR | 356 | 2 |
| INDONESIA | Rupiah | IDR | 360 | 2 |
| INTERNATIONAL MONETARY FUND (IMF) | SDR (Special Drawing Right) | XDR | 960 | N.A. |
| IRAN (ISLAMIC REPUBLIC OF) | Iranian Rial | IRR | 364 | 2 |
| IRAQ | Iraqi Dinar | IQD | 368 | 3 |
| IRELAND | Euro | EUR | 978 | 2 |
| ISLE OF MAN | Pound Sterling | GBP | 826 | 2 |
| ISRAEL | New Israeli Sheqel | ILS | 376 | 2 |
| ITALY | Euro | EUR | 978 | 2 |
| JAMAICA | Jamaican Dollar | JMD | 388 | 2 |
| JAPAN | Yen | JPY | 392 | 0 |
| JERSEY | Pound Sterling | GBP | 826 | 2 |
| JORDAN | Jordanian Dinar | JOD | 400 | 3 |
| KAZAKHSTAN | Tenge | KZT | 398 | 2 |
| KENYA | Kenyan Shilling | KES | 404 | 2 |
| KIRIBATI | Australian Dollar | AUD | 036 | 2 |
| KOREA (THE DEMOCRATIC PEOPLE’S REPUBLIC OF) | North Korean Won | KPW | 408 | 2 |
| KOREA (THE REPUBLIC OF) | Won | KRW | 410 | 0 |
| KUWAIT | Kuwaiti Dinar | KWD | 414 | 3 |
| KYRGYZSTAN | Som | KGS | 417 | 2 |
| LAO PEOPLE’S DEMOCRATIC REPUBLIC (THE) | Lao Kip | LAK | 418 | 2 |
| LATVIA | Euro | EUR | 978 | 2 |
| LEBANON | Lebanese Pound | LBP | 422 | 2 |
| LESOTHO | Loti | LSL | 426 | 2 |
| LESOTHO | Rand | ZAR | 710 | 2 |
| LIBERIA | Liberian Dollar | LRD | 430 | 2 |
| LIBYA | Libyan Dinar | LYD | 434 | 3 |
| LIECHTENSTEIN | Swiss Franc | CHF | 756 | 2 |
| LITHUANIA | Euro | EUR | 978 | 2 |
| LUXEMBOURG | Euro | EUR | 978 | 2 |
| MACAO | Pataca | MOP | 446 | 2 |
| NORTH MACEDONIA | Denar | MKD | 807 | 2 |
| MADAGASCAR | Malagasy Ariary | MGA | 969 | 2 |
| MALAWI | Malawi Kwacha | MWK | 454 | 2 |
| MALAYSIA | Malaysian Ringgit | MYR | 458 | 2 |
| MALDIVES | Rufiyaa | MVR | 462 | 2 |
| MALI | CFA Franc BCEAO | XOF | 952 | 0 |
| MALTA | Euro | EUR | 978 | 2 |
| MARSHALL ISLANDS (THE) | US Dollar | USD | 840 | 2 |
| MARTINIQUE | Euro | EUR | 978 | 2 |
| MAURITANIA | Ouguiya | MRU | 929 | 2 |
| MAURITIUS | Mauritius Rupee | MUR | 480 | 2 |
| MAYOTTE | Euro | EUR | 978 | 2 |
| MEMBER COUNTRIES OF THE AFRICAN DEVELOPMENT BANK GROUP | ADB Unit of Account | XUA | 965 | N.A. |
| MEXICO | Mexican Peso | MXN | 484 | 2 |
| MEXICO | Mexican Unidad de Inversion (UDI) | MXV | 979 | 2 |
| MICRONESIA (FEDERATED STATES OF) | US Dollar | USD | 840 | 2 |
| MOLDOVA (THE REPUBLIC OF) | Moldovan Leu | MDL | 498 | 2 |
| MONACO | Euro | EUR | 978 | 2 |
| MONGOLIA | Tugrik | MNT | 496 | 2 |
| MONTENEGRO | Euro | EUR | 978 | 2 |
| MONTSERRAT | East Caribbean Dollar | XCD | 951 | 2 |
| MOROCCO | Moroccan Dirham | MAD | 504 | 2 |
| MOZAMBIQUE | Mozambique Metical | MZN | 943 | 2 |
| MYANMAR | Kyat | MMK | 104 | 2 |
| NAMIBIA | Namibia Dollar | NAD | 516 | 2 |
| NAMIBIA | Rand | ZAR | 710 | 2 |
| NAURU | Australian Dollar | AUD | 036 | 2 |
| NEPAL | Nepalese Rupee | NPR | 524 | 2 |
| NETHERLANDS (THE) | Euro | EUR | 978 | 2 |
| NEW CALEDONIA | CFP Franc | XPF | 953 | 0 |
| NEW ZEALAND | New Zealand Dollar | NZD | 554 | 2 |
| NICARAGUA | Cordoba Oro | NIO | 558 | 2 |
| NIGER (THE) | CFA Franc BCEAO | XOF | 952 | 0 |
| NIGERIA | Naira | NGN | 566 | 2 |
| NIUE | New Zealand Dollar | NZD | 554 | 2 |
| NORFOLK ISLAND | Australian Dollar | AUD | 036 | 2 |
| NORTHERN MARIANA ISLANDS (THE) | US Dollar | USD | 840 | 2 |
| NORWAY | Norwegian Krone | NOK | 578 | 2 |
| OMAN | Rial Omani | OMR | 512 | 3 |
| PAKISTAN | Pakistan Rupee | PKR | 586 | 2 |
| PALAU | US Dollar | USD | 840 | 2 |
| PALESTINE, STATE OF | No universal currency |  |  |  |
| PANAMA | Balboa | PAB | 590 | 2 |
| PANAMA | US Dollar | USD | 840 | 2 |
| PAPUA NEW GUINEA | Kina | PGK | 598 | 2 |
| PARAGUAY | Guarani | PYG | 600 | 0 |
| PERU | Sol | PEN | 604 | 2 |
| PHILIPPINES (THE) | Philippine Peso | PHP | 608 | 2 |
| PITCAIRN | New Zealand Dollar | NZD | 554 | 2 |
| POLAND | Zloty | PLN | 985 | 2 |
| PORTUGAL | Euro | EUR | 978 | 2 |
| PUERTO RICO | US Dollar | USD | 840 | 2 |
| QATAR | Qatari Rial | QAR | 634 | 2 |
| RÉUNION | Euro | EUR | 978 | 2 |
| ROMANIA | Romanian Leu | RON | 946 | 2 |
| RUSSIAN FEDERATION (THE) | Russian Ruble | RUB | 643 | 2 |
| RWANDA | Rwanda Franc | RWF | 646 | 0 |
| SAINT BARTHÉLEMY | Euro | EUR | 978 | 2 |
| SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA | Saint Helena Pound | SHP | 654 | 2 |
| SAINT KITTS AND NEVIS | East Caribbean Dollar | XCD | 951 | 2 |
| SAINT LUCIA | East Caribbean Dollar | XCD | 951 | 2 |
| SAINT MARTIN (FRENCH PART) | Euro | EUR | 978 | 2 |
| SAINT PIERRE AND MIQUELON | Euro | EUR | 978 | 2 |
| SAINT VINCENT AND THE GRENADINES | East Caribbean Dollar | XCD | 951 | 2 |
| SAMOA | Tala | WST | 882 | 2 |
| SAN MARINO | Euro | EUR | 978 | 2 |
| SAO TOME AND PRINCIPE | Dobra | STN | 930 | 2 |
| SAUDI ARABIA | Saudi Riyal | SAR | 682 | 2 |
| SENEGAL | CFA Franc BCEAO | XOF | 952 | 0 |
| SERBIA | Serbian Dinar | RSD | 941 | 2 |
| SEYCHELLES | Seychelles Rupee | SCR | 690 | 2 |
| SIERRA LEONE | Leone | SLL | 694 | 2 |
| SINGAPORE | Singapore Dollar | SGD | 702 | 2 |
| SINT MAARTEN (DUTCH PART) | Netherlands Antillean Guilder | ANG | 532 | 2 |
| SISTEMA UNITARIO DE COMPENSACION REGIONAL DE PAGOS "SUCRE" | Sucre | XSU | 994 | N.A. |
| SLOVAKIA | Euro | EUR | 978 | 2 |
| SLOVENIA | Euro | EUR | 978 | 2 |
| SOLOMON ISLANDS | Solomon Islands Dollar | SBD | 090 | 2 |
| SOMALIA | Somali Shilling | SOS | 706 | 2 |
| SOUTH AFRICA | Rand | ZAR | 710 | 2 |
| SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS | No universal currency |  |  |  |
| SOUTH SUDAN | South Sudanese Pound | SSP | 728 | 2 |
| SPAIN | Euro | EUR | 978 | 2 |
| SRI LANKA | Sri Lanka Rupee | LKR | 144 | 2 |
| SUDAN (THE) | Sudanese Pound | SDG | 938 | 2 |
| SURINAME | Surinam Dollar | SRD | 968 | 2 |
| SVALBARD AND JAN MAYEN | Norwegian Krone | NOK | 578 | 2 |
| SWEDEN | Swedish Krona | SEK | 752 | 2 |
| SWITZERLAND | Swiss Franc | CHF | 756 | 2 |
| SWITZERLAND | WIR Euro | CHE | 947 | 2 |
| SWITZERLAND | WIR Franc | CHW | 948 | 2 |
| SYRIAN ARAB REPUBLIC | Syrian Pound | SYP | 760 | 2 |
| TAIWAN (PROVINCE OF CHINA) | New Taiwan Dollar | TWD | 901 | 2 |
| TAJIKISTAN | Somoni | TJS | 972 | 2 |
| TANZANIA, UNITED REPUBLIC OF | Tanzanian Shilling | TZS | 834 | 2 |
| THAILAND | Baht | THB | 764 | 2 |
| TIMOR-LESTE | US Dollar | USD | 840 | 2 |
| TOGO | CFA Franc BCEAO | XOF | 952 | 0 |
| TOKELAU | New Zealand Dollar | NZD | 554 | 2 |
| TONGA | Pa’anga | TOP | 776 | 2 |
| TRINIDAD AND TOBAGO | Trinidad and Tobago Dollar | TTD | 780 | 2 |
| TUNISIA | Tunisian Dinar | TND | 788 | 3 |
| TURKEY | Turkish Lira | TRY | 949 | 2 |
| TURKMENISTAN | Turkmenistan New Manat | TMT | 934 | 2 |
| TURKS AND CAICOS ISLANDS (THE) | US Dollar | USD | 840 | 2 |
| TUVALU | Australian Dollar | AUD | 036 | 2 |
| UGANDA | Uganda Shilling | UGX | 800 | 0 |
| UKRAINE | Hryvnia | UAH | 980 | 2 |
| UNITED ARAB EMIRATES (THE) | UAE Dirham | AED | 784 | 2 |
| UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND (THE) | Pound Sterling | GBP | 826 | 2 |
| UNITED STATES MINOR OUTLYING ISLANDS (THE) | US Dollar | USD | 840 | 2 |
| UNITED STATES OF AMERICA (THE) | US Dollar | USD | 840 | 2 |
| UNITED STATES OF AMERICA (THE) | US Dollar (Next day) | USN | 997 | 2 |
| URUGUAY | Peso Uruguayo | UYU | 858 | 2 |
| URUGUAY | Uruguay Peso en Unidades Indexadas (UI) | UYI | 940 | 0 |
| URUGUAY | Unidad Previsional | UYW | 927 | 4 |
| UZBEKISTAN | Uzbekistan Sum | UZS | 860 | 2 |
| VANUATU | Vatu | VUV | 548 | 0 |
| VENEZUELA (BOLIVARIAN REPUBLIC OF) | Bolívar Soberano | VES | 928 | 2 |
| VIET NAM | Dong | VND | 704 | 0 |
| VIRGIN ISLANDS (BRITISH) | US Dollar | USD | 840 | 2 |
| VIRGIN ISLANDS (U.S.) | US Dollar | USD | 840 | 2 |
| WALLIS AND FUTUNA | CFP Franc | XPF | 953 | 0 |
| WESTERN SAHARA | Moroccan Dirham | MAD | 504 | 2 |
| YEMEN | Yemeni Rial | YER | 886 | 2 |
| ZAMBIA | Zambian Kwacha | ZMW | 967 | 2 |
| ZIMBABWE | Zimbabwe Dollar | ZWL | 932 | 2 |



---

## Sheet 8 - Country Codes, ISO 3166-1 alpha-2 (template reference, DO NOT TOUCH)


**DO NOT TOUCH**
**Country Codes - ISO 3166-1 alpha-2 code**


| Item | Value |
|---|---|
| Name | Code |
| Afghanistan | AF |
| √Öland Islands | AX |
| Albania | AL |
| Algeria | DZ |
| American Samoa | AS |
| Andorra | AD |
| Angola | AO |
| Anguilla | AI |
| Antarctica | AQ |
| Antigua and Barbuda | AG |
| Argentina | AR |
| Armenia | AM |
| Aruba | AW |
| Australia | AU |
| Austria | AT |
| Azerbaijan | AZ |
| Bahamas | BS |
| Bahrain | BH |
| Bangladesh | BD |
| Barbados | BB |
| Belarus | BY |
| Belgium | BE |
| Belize | BZ |
| Benin | BJ |
| Bermuda | BM |
| Bhutan | BT |
| Bolivia, Plurinational State of | BO |
| Bonaire, Sint Eustatius and Saba | BQ |
| Bosnia and Herzegovina | BA |
| Botswana | BW |
| Bouvet Island | BV |
| Brazil | BR |
| British Indian Ocean Territory | IO |
| Brunei Darussalam | BN |
| Bulgaria | BG |
| Burkina Faso | BF |
| Burundi | BI |
| Cambodia | KH |
| Cameroon | CM |
| Canada | CA |
| Cape Verde | CV |
| Cayman Islands | KY |
| Central African Republic | CF |
| Chad | TD |
| Chile | CL |
| China | CN |
| Christmas Island | CX |
| Cocos (Keeling) Islands | CC |
| Colombia | CO |
| Comoros | KM |
| Congo | CG |
| Congo, the Democratic Republic of the | CD |
| Cook Islands | CK |
| Costa Rica | CR |
| C√¥te d'Ivoire | CI |
| Croatia | HR |
| Cuba | CU |
| Cura√ßao | CW |
| Cyprus | CY |
| Czech Republic | CZ |
| Denmark | DK |
| Djibouti | DJ |
| Dominica | DM |
| Dominican Republic | DO |
| Ecuador | EC |
| Egypt | EG |
| El Salvador | SV |
| Equatorial Guinea | GQ |
| Eritrea | ER |
| Estonia | EE |
| Ethiopia | ET |
| Falkland Islands (Malvinas) | FK |
| Faroe Islands | FO |
| Fiji | FJ |
| Finland | FI |
| France | FR |
| French Guiana | GF |
| French Polynesia | PF |
| French Southern Territories | TF |
| Gabon | GA |
| Gambia | GM |
| Georgia | GE |
| Germany | DE |
| Ghana | GH |
| Gibraltar | GI |
| Greece | GR |
| Greenland | GL |
| Grenada | GD |
| Guadeloupe | GP |
| Guam | GU |
| Guatemala | GT |
| Guernsey | GG |
| Guinea | GN |
| Guinea-Bissau | GW |
| Guyana | GY |
| Haiti | HT |
| Heard Island and McDonald Islands | HM |
| Holy See (Vatican City State) | VA |
| Honduras | HN |
| Hong Kong | HK |
| Hungary | HU |
| Iceland | IS |
| India | IN |
| Indonesia | ID |
| Iran, Islamic Republic of | IR |
| Iraq | IQ |
| Ireland | IE |
| Isle of Man | IM |
| Israel | IL |
| Italy | IT |
| Jamaica | JM |
| Japan | JP |
| Jersey | JE |
| Jordan | JO |
| Kazakhstan | KZ |
| Kenya | KE |
| Kiribati | KI |
| Korea, Democratic People's Republic of | KP |
| Korea, Republic of | KR |
| Kuwait | KW |
| Kyrgyzstan | KG |
| Lao People's Democratic Republic | LA |
| Latvia | LV |
| Lebanon | LB |
| Lesotho | LS |
| Liberia | LR |
| Libya | LY |
| Liechtenstein | LI |
| Lithuania | LT |
| Luxembourg | LU |
| Macao | MO |
| Macedonia, the Former Yugoslav Republic of | MK |
| Madagascar | MG |
| Malawi | MW |
| Malaysia | MY |
| Maldives | MV |
| Mali | ML |
| Malta | MT |
| Marshall Islands | MH |
| Martinique | MQ |
| Mauritania | MR |
| Mauritius | MU |
| Mayotte | YT |
| Mexico | MX |
| Micronesia, Federated States of | FM |
| Moldova, Republic of | MD |
| Monaco | MC |
| Mongolia | MN |
| Montenegro | ME |
| Montserrat | MS |
| Morocco | MA |
| Mozambique | MZ |
| Myanmar | MM |
| Namibia | NA |
| Nauru | NR |
| Nepal | NP |
| Netherlands | NL |
| New Caledonia | NC |
| New Zealand | NZ |
| Nicaragua | NI |
| Niger | NE |
| Nigeria | NG |
| Niue | NU |
| Norfolk Island | NF |
| Northern Mariana Islands | MP |
| Norway | NO |
| Oman | OM |
| Pakistan | PK |
| Palau | PW |
| Palestine, State of | PS |
| Panama | PA |
| Papua New Guinea | PG |
| Paraguay | PY |
| Peru | PE |
| Philippines | PH |
| Pitcairn | PN |
| Poland | PL |
| Portugal | PT |
| Puerto Rico | PR |
| Qatar | QA |
| R√©union | RE |
| Romania | RO |
| Russian Federation | RU |
| Rwanda | RW |
| Saint Barthelemy | BL |
| Saint Helena, Ascension and Tristan da Cunha | SH |
| Saint Kitts and Nevis | KN |
| Saint Lucia | LC |
| Saint Martin (French part) | MF |
| Saint Pierre and Miquelon | PM |
| Saint Vincent and the Grenadines | VC |
| Samoa | WS |
| San Marino | SM |
| Sao Tome and Principe | ST |
| Saudi Arabia | SA |
| Senegal | SN |
| Serbia | RS |
| Seychelles | SC |
| Sierra Leone | SL |
| Singapore | SG |
| Sint Maarten (Dutch part) | SX |
| Slovakia | SK |
| Slovenia | SI |
| Solomon Islands | SB |
| Somalia | SO |
| South Africa | ZA |
| South Georgia and the South Sandwich Islands | GS |
| South Sudan | SS |
| Spain | ES |
| Sri Lanka | LK |
| Sudan | SD |
| Suriname | SR |
| Svalbard and Jan Mayen | SJ |
| Swaziland | SZ |
| Sweden | SE |
| Switzerland | CH |
| Syrian Arab Republic | SY |
| Taiwan, Province of China | TW |
| Tajikistan | TJ |
| Tanzania, United Republic of | TZ |
| Thailand | TH |
| Timor-Leste | TL |
| Togo | TG |
| Tokelau | TK |
| Tonga | TO |
| Trinidad and Tobago | TT |
| Tunisia | TN |
| Turkey | TR |
| Turkmenistan | TM |
| Turks and Caicos Islands | TC |
| Tuvalu | TV |
| Uganda | UG |
| Ukraine | UA |
| United Arab Emirates | AE |
| United Kingdom | GB |
| United States | US |
| United States Minor Outlying Islands | UM |
| Uruguay | UY |
| Uzbekistan | UZ |
| Vanuatu | VU |
| Venezuela, Bolivarian Republic of | VE |
| Viet Nam | VN |
| Virgin Islands, British | VG |
| Virgin Islands, U.S. | VI |
| Wallis and Futuna | WF |
| Western Sahara | EH |
| Yemen | YE |
| Zambia | ZM |
| Zimbabwe | ZW |

# Colombia DATA DICTIONARY — CZ V2.0 FORMAT

You are building the Colombia Data Dictionary using the CZ V2.0 template format.

## FORMAT REFERENCE
Load: ~/mercans-pipeline/shared/CZ_Data_Dictionary_V2_0.xlsx
Do NOT create a new Workbook(). Load CZ file, clear data rows, populate
preserving all formatting, colors, column widths, sheet order, row heights.

## 8 SHEETS (preserve from CZ template)
1. Version Control
2. Introduction
3. Instructions (change country name only)
4. ID Information
5. Country Fields
6. Country Option Mappers
7. Currency Codes - ISO 4217 (preserve as-is)
8. Country Codes - ISO 3166-1 (preserve as-is)

## COLUMN RULES
POPULATE ONLY BLUE columns (4472C4). Leave ORANGE (FF9900) columns empty — dev team fills those.

ID Information sheet (22 cols A-V):
A: Country="Colombia" BLUE | B: Ordinal ORANGE | C: Field Name BLUE | D: Internal Code ORANGE
E: Label Local (Spanish) BLUE | F: Description BLUE | G: Data Type M/CM/O BLUE
H: Pre-Condition BLUE | I: Field Type BLUE | J: Format BLUE | K: Option Mapper BLUE
L-U: ORANGE | V: Additional Notes BLUE

Country Fields sheet: same pattern, col A empty, content from col B.

## SCOPE — STRICTLY user-input master data only

INCLUDE:
- Identification (tax ID, national ID, SS number, bank IBAN, employer reg numbers)
- Demographics (name, DOB, gender, nationality, marital status, place of birth)
- Contact (address, postcode, email, phone)
- Employment (hire date, contract type, job title, hours, FTE%, termination date)
- Tax profile (residency status, tax number, exemption flags)
- SS profile (fund eligibility, contribution category, special status flags)
- Family attributes (number of children, disability %, spouse info) IF calculation-driving
- Employer master data (name, registration numbers, addresses, sector)
- Code/selector fields that drive calculation paths

EXCLUDE (dev team will reject):
- Calculated amounts → WTC scope
- Base Salary / Basic Salary amounts → WTC, NOT DD
- Gross pay, net pay, taxable income → calculated
- Tax rates, SS rates → parameters
- Ceilings, thresholds, minimum wage → parameters
- Authority-generated values (submission IDs, receipts)
- Transactional per-payrun data (period dates, days worked, sick leave dates)

## PRIVATE SECTOR FILTER — CRITICAL
The Mercans platform serves PRIVATE SECTOR employers only.
When building Country Option Mappers, EXCLUDE non-private-sector categories:
- Civil servants / state employees — separate legislation
- Military, police, security forces — separate state SS scheme
- Self-insured persons (freelancers, craftsmen, farmers) — pay SS directly, not via employer
- Cooperative members without labour contract — not employment income
- Persons receiving unemployment benefits — registered with Employment Agency, not employer

INCLUDE for private sector option mappers:
- Standard employees under employment contract — full SS scenario
- Managers/directors under management contracts (with note: which SS funds apply)
- Employees on maternity/parental/sick leave (record-only, benefit paid by SS authority)
- Working pensioners under employment contract
- Part-time, fixed-term, posted, foreign nationals under standard employment

## ALIGNMENT WITH REPORT SPECS
Cross-reference report specs at ~/mercans-pipeline/CO-compliance/04-reports-spec/
For each spec field, classify: DD / TX / CALC / SYS
Ensure all DD-bucket fields are in the DD. TX/CALC/SYS are correctly excluded.

## v2.4 — OPTION MAPPER COMPLETENESS (C14)
For every Option Mapper in Country Option Mappers sheet:
- Every code must have: (a) code value, (b) description, (c) constraint flag if conditional
- If a Spec field references this mapper with Mandatory=C, the constraint MUST be
  documented in the mapper's Notes column

## SOURCES
1. CZ template: ~/mercans-pipeline/shared/CZ_Data_Dictionary_V2_0.xlsx
2. Report Specs: ~/mercans-pipeline/CO-compliance/04-reports-spec/
3. scope_manifest.json
4. CCG: ~/mercans-pipeline/CO-compliance/01-ccg/CO-CCG-001-v1.0.docx
5. Official PDFs: ~/mercans-pipeline/CO-compliance/00-official-sources/pdfs/

## OUTPUT
Save to: ~/mercans-pipeline/CO-compliance/05-data-dictionary/CO-DD-001-v1.0.xlsx
Use openpyxl. Load CZ template, clear data rows, populate all sheets.

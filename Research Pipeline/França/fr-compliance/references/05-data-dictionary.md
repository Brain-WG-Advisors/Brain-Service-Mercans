# France Data Dictionary (DD) - FR-DD-001 (file v1.0, contents v1.1)

The complete France Data Dictionary: 25 ID Information fields, 164 Country Fields and 54 Country Option Mappers (303 codes), each with format, mandatory/conditional status, valid values, French label and NEODeS rubrique where one applies, plus the ISO 4217 and ISO 3166-1 reference sheets.


## Provenance

| Source artifact | Bytes | SHA-256 |
|---|---|---|
| `FR-compliance/05-data-dictionary/FR-DD-001-v1.0.xlsx` | 590,693 | `8d528992510b3a21…` |
| `FR-compliance/05-data-dictionary/FR-DD-001-build-log.md` | 5,558 | `a6f836e8dd56cee9…` |

This file is a complete, verbatim conversion of the artifacts above. Figures, dates, code values, French terminology and legal citations are reproduced exactly as delivered; nothing is summarised or rounded.


## Navigation index

Read with `offset` / `limit` rather than opening the whole file.

| Line | Section |
|---|---|
| 44 | France Data Dictionary - all sheets |
| 46 | &nbsp;&nbsp;&nbsp;&nbsp;Sheet: `Version Control` |
| 61 | &nbsp;&nbsp;&nbsp;&nbsp;Sheet: `Introduction` |
| 76 | &nbsp;&nbsp;&nbsp;&nbsp;Sheet: `Instructions` |
| 99 | &nbsp;&nbsp;&nbsp;&nbsp;Sheet: `ID Information` |
| 133 | &nbsp;&nbsp;&nbsp;&nbsp;Sheet: `Country Fields` |
| 306 | &nbsp;&nbsp;&nbsp;&nbsp;Sheet: `Country Option Mappers` |
| 671 | &nbsp;&nbsp;&nbsp;&nbsp;Sheet: `Currency Codes - ISO 4217` |
| 950 | &nbsp;&nbsp;&nbsp;&nbsp;Sheet: `Country Codes - ISO 3166-1` |
| 1211 | Annex - Data Dictionary build log |
| 1213 | &nbsp;&nbsp;&nbsp;&nbsp;FR-DD-001-v1.0 — build log |
| 1220 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Contents |
| 1235 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Column discipline |
| 1247 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sources |
| 1264 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Private-sector and régime-général filter |
| 1277 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;C14 — option mapper completeness |
| 1288 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Checks run |
| 1298 | &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Open item for the scope owner |

---


# France Data Dictionary - all sheets

## Sheet: `Version Control`

_27 rows x 6 columns._

**Data Dictionary**

**<France>**

| col1 | Version | Effective Date | Change Description | Status | Updated By |
|---|---|---|---|---|---|
|  | 1.0 | 2026-08-27 | Initial version - France Data Dictionary | Released | Wallisson Gomes |
|  | 1.1 | 2026-08-27 | Alignment patch against the 15 delivered report specs in FR-compliance/04-reports-spec (FR-ALIGNMENT-PATCH.md). Country Option Mappers: three codes that the private-sector filter removed without naming them are now named in their mapper notes - Contract Nature 32 and 60 (S21.G00.40.007) and Public-Policy or Collectively Agreed Scheme 80 (S21.G00.40.008). No code value, local name or English description was changed: all 285 code-pairs shared with the specs were compared and matched exactly before this patch. | Released | Wallisson Gomes |
|  | Business Analyst |  |  |  |  |
|  | Regulation Analyst |  |  |  |  |

## Sheet: `Introduction`

_16 rows x 4 columns._

**Table of Contents:**

| col1 | # | Section | Description |
|---|---|---|---|
|  | 1 | Instructions | Please read this section first. |
|  |  | ID Information | List of country-specific ID fields. |
|  |  | Country Fields | List of country-specific data fields, including employee fields and legal entity fields. |
|  |  | Country Option Mappers | List of country option mappers. |
|  |  | Currency Codes | ISO currency codes. No action required. |
|  |  | Country Codes | ISO country codes. No action required. |

## Sheet: `Instructions`

_18 rows x 3 columns._

**Instructions**

| col1 | Field Name | Instructions/Descriptions |
|---|---|---|
|  | Field Group | Mercans' field group name. The values in this field should not be updated. |
|  | Field Name | Data field name in Mercans' system. This field should be updated only for the field in the Implementation-Specific Fields tab. The values in this field are not always the same as the actual database field names. |
|  | Internal Code | Mercans' data field code. This field is used to map Client's data against Mercans fields. |
|  | Label in Local Language | Field name in the local language and should reflect the same terminology as used on statutory forms or local language reports. |
|  | Field Description (Long Description of the Field) | Include a full description of the respective data field. |
|  | Data Type - Mandatory (M), Conditional Mandatory (CM), Optional (O) | The values of this field should not be updated for Universal or Country-Specific Fields. Each Implementation-Specific Fields must be categorized as a either Mandatory, Conditional Mandatory or Optional fields. Mandatory fields must be filled for each employee record and Conditional Mandatory fields only if a certain condition is met. |
|  | Pre-Condition for Conditional Mandatory | This field should be filled for all data fields identified as Conditional-Minatory. It should include the condition that makes the respective field mandatory. |
|  | Field Type (Text, Number, Date, Integer, Decimal, Counter) | Available field type options are Text, Number, Date, Integer, Decimal, and Counter. Each field must include a field type. |
|  | Pre-Defined Format | Field format should be provided for the fields that must be in specific formats; i.e. (999) 123-4567, etc. |
|  | Validations, Restrictions, Pick Lists etc. | Field-specific validations are defined in this field. Validations can include specific pick lists, length validations, etc. |
|  | Default Value | A default value should be filled for each record if no other value is applicable. |
|  | MSS Field Permissions | For each field identify whether the field is not visible/available (hidden), visible but not editable (view) or editable (edit) through Payroll Administrator Console (PAC). Further field specific access restrictions can be defined based on PAC user roles and access rights. |
|  | ESS Field Permissions | For each field identify whether the field is not visible/available (hidden), visible but not editable (view) or editable (edit) through Employee Self Service (ESS) by employees for their own records. |
|  | Additional Notes | Include any additional clarifications or notes here. |

## Sheet: `ID Information`

_29 rows x 22 columns._

**Identification Information**

| Country | Ordinal | Field Name | Internal Code | Label in Local Language | Field Description (Long Description of the Field) | Data Type  -Mandatory (M), Conditional Mandatory (CM), Optional (O) | Pre-Condition for Conditional Mandatory | Field Type (Text, Number, Date, Integer, Decimal, Counter) | Pre-Defined Format | Option Mapper | Validations, Restrictions, Pick Lists etc. | Parent Field Group | Ordinal of Parent Field Group | Internal Code of Parent Field Group | Sub Group under Parent Field Group | Ordinal of Sub Group under Parent Field Group | Internal Code of Sub Group under Parent Field Group | Default Value | MSS Field Permissions (Read, Write) | ESS Field Permissions (Read, Write) | Additional Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| France |  | Employee Social Security Number (NIR) |  | Numéro d'inscription au répertoire (NIR) | The employee's French social security number, allocated by INSEE and used by every social protection body. Thirteen significant digits encoding sex, year and month of birth, department and commune of birth and the order number in the birth register, followed by a two-digit verification key held in the next field. It is the key on which the DSN individual block is built and on which the tax administration returns the withholding rate. | CM | Mandatory as soon as the NIR is known. Where it is not yet known - typically a newly arrived foreign national - the Temporary Technical Number (NTT) must be supplied instead, and must be replaced by the NIR as soon as the NIR is issued. | Text | 13 digits: S(1) YY(2) MM(2) DD(2) CCC(3) OOO(3). Corsican birth departments are coded 2A and 2B | Personal Identifier Type |  |  |  |  |  |  |  |  |  |  | Employee ID. Design point carried from FR-CCG-001 Module 2.2: the employer does NOT capture the employee's tax reference number (numéro fiscal / SPI). DGFiP matches the employee to their tax file from the NIR and the civil-status data transmitted in the DSN, and returns the withholding rate in the return flow. A field asking the employee for a tax number is unnecessary and questionable under data minimisation. Norm reference: NEODeS CT2026.1.2 S21.G00.30.001. |
| France |  | NIR Verification Key |  | Clé de contrôle du NIR | The two-digit check key of the social security number. It equals 97 minus the thirteen-digit number modulo 97. For a birth in Corsica the department code 2A or 2B is first converted by substituting A or B with 0 and subtracting 1,000,000 or 2,000,000 respectively, before the key is computed. | CM | Mandatory whenever the NIR is supplied. | Text | 2 digits, 01 to 97 |  |  |  |  |  |  |  |  |  |  |  | Employee ID. The DSN transmits only the thirteen significant digits; the key is held so that a mistyped NIR is rejected at capture. That is the cheapest control in the French build, because a wrong NIR is otherwise only discovered weeks later through a DSN return-flow anomaly. Source: FR-CCG-001 Module 2.2. |
| France |  | Temporary Technical Number (NTT) |  | Numéro technique temporaire (NTT) | The provisional identifier used in the DSN for an employee whose NIR is not yet known. It is conventionally the employer's SIRET followed by an internal sequence and it identifies the individual to the collecting bodies until the NIR is issued. | CM | Mandatory where the employee has no NIR yet. Must be cleared once the NIR is captured. | Text | 11 to 40 characters; conventionally SIRET (14) + internal sequence | Personal Identifier Type |  |  |  |  |  |  |  |  |  |  | Employee ID. A contract left on an NTT beyond a few months generates a recurring DSN anomaly, so this field must be monitored and not merely stored. Norm reference: NEODeS CT2026.1.2 S21.G00.30.020. |
| France |  | Employee Number |  | Matricule de l'individu dans l'entreprise | The employer's own personnel number for the individual, unique within the legal entity. It is the stable key the collecting bodies use to follow an individual across successive monthly declarations when the NIR is corrected or replaced. | M |  | Text | 1 to 30 characters |  |  |  |  |  |  |  |  |  |  |  | Employee ID. Must remain stable for the life of the employment relationship; changing it mid-year breaks the continuity checks the collecting bodies run on the DSN. Norm reference: NEODeS CT2026.1.2 S21.G00.30.019. |
| France |  | Employment Contract Number |  | Numéro du contrat | The employer's identifier for the individual employment contract. An individual may hold more than one contract with the same employer at the same time, and each contract carries its own contribution set, working-time arrangement and end-of-contract declaration, so the contract number and not the employee number is the key of the contract block. | M |  | Text | 5 to 20 characters |  |  |  |  |  |  |  |  |  |  |  | Employee ID. Must be unique per contract and must not be reused after a termination, because the end-of-contract signal and every later correction are keyed on it. Norm reference: NEODeS CT2026.1.2 S21.G00.40.009. |
| France |  | SIREN |  | SIREN | The nine-digit identifier of the legal entity, allocated by INSEE through the single formalities window operated by INPI. It is constant for the life of the entity and is unaffected by relocation or by a change of activity. It carries a Luhn check digit. | M |  | Text | 9 digits, Luhn check |  |  |  |  |  |  |  |  |  |  |  | Employer ID. The SIREN is the identifier DGFiP uses for the income tax withheld at source and for the payroll tax. A change of payroll provider does not change the SIREN and therefore does not interrupt any cumulative mechanism: year-to-date figures must be migrated. Source: FR-CCG-001 Modules 2.1 and 2.3; NEODeS CT2026.1.2 S21.G00.06.001. |
| France |  | Establishment SIRET |  | SIRET de l'établissement | The fourteen-digit identifier of a specific establishment: the SIREN followed by the five-digit establishment sequence (NIC). It changes when the establishment moves to another commune. It carries a Luhn check digit. | M |  | Text | 14 digits = SIREN (9) + NIC (5), Luhn check |  |  |  |  |  |  |  |  |  |  |  | Employer ID. France is a unitary state and the identifiers are national, but the industrial-accident rate, the mobility levy rate, the sector paid-leave fund, the occupational health service and the DSN establishment block are all fixed per establishment. The SIRET is therefore the practical configuration key. Source: FR-CCG-001 Module 2.1. |
| France |  | Establishment Sequence (NIC) |  | NIC de l'établissement | The five-digit establishment sequence inside the SIRET, the last digit of which is a check digit. The NIC of the head office is declared separately from the NIC of the employing establishment. | M |  | Text | 5 digits, last digit is a check digit |  |  |  |  |  |  |  |  |  |  |  | Employer ID. Captured both for the head office, declared in the legal entity block, and for each employing establishment. Norm reference: NEODeS CT2026.1.2 S21.G00.06.002 and S21.G00.11.001. |
| France |  | Entity Activity Code (APEN) |  | Code APEN de l'entreprise | The activity code allocated by INSEE to the legal entity under the NAF nomenclature. It drives the presumed sector collective agreement and several sector levies. | M |  | Text | 4 digits + 1 letter, for example 6201Z |  |  |  |  |  |  |  |  |  |  |  | Employer ID. The APE code is a presumption, not a determination: the collective agreement that actually applies is the one matching the entity's real principal activity, and where the two diverge the IDCC captured below governs, not the activity code. Source: FR-CCG-001 Module 2.1; NEODeS CT2026.1.2 S21.G00.06.003. |
| France |  | Establishment Activity Code (APET) |  | Code APET de l'établissement | The activity code allocated by INSEE to the establishment under the NAF nomenclature. It underpins the industrial-accident risk classification applied to that establishment. | M |  | Text | 4 digits + 1 letter, for example 6201Z |  |  |  |  |  |  |  |  |  |  |  | Employer ID. May differ from the entity code where an establishment carries on a different activity. Norm reference: NEODeS CT2026.1.2 S21.G00.11.002. |
| France |  | URSSAF Contributor Account Number |  | Numéro de compte cotisant URSSAF | The account the collecting body opens for the employer, keyed on the SIRET. It is quoted on every DSN and on every contribution payment and it is the reference under which URSSAF holds the employer's contribution ledger. | M |  | Text | As allocated by URSSAF; keyed on the SIRET |  |  |  |  |  |  |  |  |  |  |  | Employer ID. URSSAF collects the social security contributions, the unemployment contribution, the wage guarantee contribution, the training and apprenticeship contributions and the mobility levy, and receives the DSN. Source: FR-CCG-001 Module 2.1. |
| France |  | Intra-Community VAT Number |  | Numéro de TVA intracommunautaire | The value added tax identifier of the legal entity: the country prefix FR, a two-character computed key and the nine digits of the SIREN. | O |  | Text | FR + 2-character key + SIREN (9 digits) |  |  |  |  |  |  |  |  |  |  |  | Employer ID. Not a payroll identifier. It is captured because it is requested on the same onboarding form and because it appears on the payroll tax return, but no payroll calculation depends on it. Source: FR-CCG-001 Module 2.1. |
| France |  | Collective Agreement Code (IDCC) |  | Code convention collective applicable (IDCC) | The four-digit identifier of the sector collective agreement that applies. It is mandatory on the payslip and in the DSN and it governs the notice period, severance above the statutory floor, seniority leave, sick-pay top-up and grading. | M |  | Text | 4 digits, for example 1486, 1090, 3239 |  |  |  |  |  |  |  |  |  |  |  | Employer ID. Not a registration number in the strict sense, but it behaves like one in payroll configuration and must be captured per establishment as well as per entity, because a multi-establishment employer may apply different agreements. Where an individual contract departs from the establishment default it is captured again at contract level. Source: FR-CCG-001 Module 2.1; NEODeS CT2026.1.2 S21.G00.06.015 and S21.G00.11.022. |
| France |  | Occupational-Accident Risk Code (AT/MP) |  | Numéro de risque accident du travail / maladie professionnelle | The risk code allocated per establishment and per activity by the regional sickness-insurance fund (CARSAT, or CRAMIF in the Paris region). It identifies the risk category under which the establishment is rated for occupational accidents and diseases. | M |  | Text | 5 to 6 characters: 3 digits + 2 letters, with an optional section character |  |  |  |  |  |  |  |  |  |  |  | Employer ID. Notified to the employer by CARSAT together with the net rate, through the AT/MP account service on net-entreprises.fr. It is a per-establishment master-data value supplied by the authority, not a national parameter. Source: FR-CCG-001 Module 2.1; FR-CARSAT-001; NEODeS CT2026.1.2 S21.G00.40.040. |
| France |  | Occupational-Accident Net Rate (AT/MP) |  | Taux net accident du travail / maladie professionnelle | The net contribution rate notified to the establishment by CARSAT for the occupational-accident and occupational-disease risk. It is specific to the establishment and to its risk code, it is re-notified at least annually and it must be applied from the effective date stated in the notification. | M |  | Decimal | Percentage to 2 decimals, for example 2.15 |  |  |  |  |  |  |  |  |  |  |  | Employer ID. Deliberately in the Data Dictionary and not in the parameter tables: unlike the national contribution rates this is an employer-specific value notified per establishment, it must be stored against the establishment and it must be supplied by the client. The 0.49 fixed points of it that are imputable against the general degressive reduction are a statutory constant and remain in FR-CCG-001 Module 5. Source: FR-CARSAT-001; Arrêté du 30 décembre 2025 (tarification AT/MP 2026). |
| France |  | Occupational-Accident Rate Effective Date |  | Date d'effet du taux AT/MP | The date from which the notified net occupational-accident rate applies. A rate may be re-notified during the year, in which case the payroll must apply each rate over its own period of validity and regularise any month already run at the superseded rate. | M |  | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Employer ID. Stored with the rate as the start of its validity. Holding a rate without its effective date is the defect that produces silent under- or over-contribution when CARSAT re-notifies mid-year. Source: FR-CARSAT-001. |
| France |  | Skills Operator Code (OPCO) |  | Opérateur de compétences (OPCO) | The code of the skills operator to which the establishment is attached for vocational training and apprenticeship purposes. The attachment follows the collective agreement, not the activity code. | CM | Mandatory where the establishment employs at least one employee subject to the vocational training contribution or the apprenticeship tax. | Text | 2 characters, from the DSN external referential OPCO |  |  |  |  |  |  |  |  |  |  |  | Employer ID. Norm reference: NEODeS CT2026.1.2 S21.G00.11.023. |
| France |  | Occupational Health Service Identifier (SPST) |  | Identifiant du Service de Prévention et de Santé au Travail (SPST) | The membership identifier of the occupational prevention and health service to which the establishment is affiliated. Affiliation is compulsory for every private-sector employer, and the service carries out the statutory medical examinations. | CM | Mandatory where the establishment is affiliated to an inter-company occupational health service. Not applicable where the employer operates its own autonomous service. | Text | 1 to 14 characters |  |  |  |  |  |  |  |  |  |  |  | Employer ID. Also captured at contract level for an employee attached to a service other than the establishment default. Source: FR-CCG-001 Module 2.1; NEODeS CT2026.1.2 S21.G00.11.025 and S21.G00.30.030. |
| France |  | Sector Paid-Leave Fund Code |  | Code caisse professionnelle de congés payés | The membership code of the sector paid-leave fund, where the establishment belongs to a sector in which holiday pay is paid by a fund rather than by the employer: construction and public works, entertainment, dockers and certain transport activities. | CM | Mandatory where the establishment belongs to a sector operating a paid-leave fund, for example a CIBTP fund. Not applicable otherwise. | Text | 2 to 20 characters |  |  |  |  |  |  |  |  |  |  |  | Employer ID. This field carries a decisive payroll design difference and is not cosmetic. In these sectors the employer pays a contribution to the fund and the FUND pays the employee's holiday pay. A payroll engine configured on the general-regime assumption that the employer pays holiday pay will be wrong for these clients in both the payslip and the DSN. Source: FR-CCG-001 Module 2.1; NEODeS CT2026.1.2 S21.G00.40.022. |
| France |  | Agirc-Arrco Institution Membership Number |  | Numéro d'adhésion à l'institution Agirc-Arrco | The membership number held with the Agirc-Arrco member institution to which the employer is affiliated. Affiliation to the unified supplementary pension scheme is mandatory for every private-sector employer and covers all employees, managerial grade or not. | M |  | Text | As allocated by the member institution |  |  |  |  |  |  |  |  |  |  |  | Employer ID. Since the 2019 merger there is a single unified scheme and no separate managerial-grade pension scheme; managerial grade nevertheless still governs the compulsory 1.50% employer death-and-disability contribution on the first band. Source: FR-CCG-001 Modules 2.1 and 2.2. |
| France |  | Death-and-Disability Insurer Code |  | Code organisme de prévoyance | The code of the insurer, provident institution or mutual carrying the death-and-disability or supplementary health cover, taken from the DSN reference table of insurance bodies. | M |  | Text | 5 to 9 characters, from the DSN external referential DSN_Ref_Ops_4_5 |  |  |  |  |  |  |  |  |  |  |  | Employer ID. Compulsory supplementary health cover applies to every private-sector employer for all employees, with an employer share of at least 50% of the premium; managerial-grade death-and-disability cover at 1.50% of the capped band is wholly employer-paid. Source: FR-CCG-001 Module 5; NEODeS CT2026.1.2 S21.G00.15.002. |
| France |  | Death-and-Disability Contract Reference |  | Référence du contrat de prévoyance | The policy reference of the collective death-and-disability or health cover contract taken out by the employer with the insurer named above. | M |  | Text | 1 to 30 characters |  |  |  |  |  |  |  |  |  |  |  | Employer ID. Norm reference: NEODeS CT2026.1.2 S21.G00.15.001. |
| France |  | Delegated Administrator Code |  | Code délégataire de gestion | The code of the body to which day-to-day administration of the cover has been delegated by the insurer, where administration and underwriting are separated. | CM | Mandatory where the insurer has delegated administration of the contract to a third party. | Text | 6 characters, from the DSN external referential DSN_Code_Deleg_Gestion |  |  |  |  |  |  |  |  |  |  |  | Employer ID. Norm reference: NEODeS CT2026.1.2 S21.G00.15.003. |
| France |  | Membership Technical Identifier |  | Identifiant technique adhésion | The technical sequence number distinguishing one membership from another where the employer holds several contracts with the same insurer. It is the key on which each employee affiliation is attached to the correct contract. | M |  | Text | 1 to 3 digits, from 1 |  |  |  |  |  |  |  |  |  |  |  | Employer ID. Norm reference: NEODeS CT2026.1.2 S21.G00.15.005. |
| France |  | Approved OETH Collective Agreement Reference |  | Référence de l'accord agréé OETH | The reference of the approved collective agreement under which the employer discharges its disabled-worker employment obligation through an agreed action programme instead of by paying the annual contribution. | CM | Mandatory where the employer is covered by an approved disabled-worker employment agreement. | Text | 12 characters, from the DSN external referential OethAccord |  |  |  |  |  |  |  |  |  |  |  | Employer ID. Source: FR-URSSAF-003 DOETH; NEODeS CT2026.1.2 S21.G00.13.001. |

## Sheet: `Country Fields`

_168 rows x 23 columns._

**Country-Specific Fields**

| col1 | Country | Ordinal | Field Name | Internal Code | Label in Local Language | Field Description (Long Description of the Field) | Data Type  -Mandatory (M), Conditional Mandatory (CM), Optional (O) | Pre-Condition for Conditional Mandatory | Field Type (Text, Number, Date, Integer, Decimal, Counter) | Pre-Defined Format | Option Mapper | Validations, Restrictions, Pick Lists etc. | Parent Field Group | Ordinal of Parent Field Group | Internal Code of Parent Field Group | Sub Group under Parent Field Group | Ordinal of Sub Group under Parent Field Group | Internal Code of Sub Group under Parent Field Group | Default Value | MSS Field Permissions (Read, Write) | ESS Field Permissions (Read, Write) | Additional Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|  | France |  | Surname at Birth |  | Nom de famille | The employee's family name as it appears on the birth record. It is the name under which the individual is registered with the social protection bodies and it is the name that must be transmitted, whether or not the employee uses another name day to day. | M |  | Text | 1 to 80 characters |  |  |  |  |  |  |  |  |  |  |  | Personal information. Transmitting a married name in this field instead of the birth name is one of the commonest causes of a failed identification check in the DSN return flow, because the bodies match on the birth record. Norm reference: NEODeS CT2026.1.2 S21.G00.30.002. |
|  | France |  | Name in Use |  | Nom d'usage | The name the employee actually uses, where it differs from the surname at birth - typically a spouse's name or a double-barrelled name. It is the name that appears on the payslip and on correspondence. | CM | Mandatory where the employee uses a name other than the surname at birth. | Text | 1 to 80 characters |  |  |  |  |  |  |  |  |  |  |  | Personal information. Held in addition to, never instead of, the surname at birth. Norm reference: NEODeS CT2026.1.2 S21.G00.30.003. |
|  | France |  | Forenames |  | Prénoms | All the employee's given names, in the order shown on the birth record, separated by spaces. The first forename is the one used on the payslip. | M |  | Text | 1 to 80 characters, forenames separated by a space |  |  |  |  |  |  |  |  |  |  |  | Personal information. Norm reference: NEODeS CT2026.1.2 S21.G00.30.004. |
|  | France |  | Sex |  | Sexe | The employee's sex as recorded on the birth record. It must agree with the first digit of the social security number, which is 1 for male and 2 for female; a disagreement between the two is rejected by the identification check. | M |  | Text | 2-character code | Sex |  |  |  |  |  |  |  |  |  |  | Personal information. Norm reference: NEODeS CT2026.1.2 S21.G00.30.005. |
|  | France |  | Date of Birth |  | Date de naissance | The employee's date of birth. It must agree with positions 2 to 5 of the social security number, which encode the year and month of birth. | M |  | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Personal information. The norm accepts the conventional values 00 and 99 for an unknown day or month where the birth record itself is incomplete, which occurs for some employees born outside France. Norm reference: NEODeS CT2026.1.2 S21.G00.30.006. |
|  | France |  | Place of Birth |  | Lieu de naissance | The commune of birth for a birth in France, or the town of birth for a birth abroad. It is transmitted as free text, not as an INSEE commune code. | CM | Mandatory where the individual is identified by a NIR. Not required where the individual is declared under a Temporary Technical Number. | Text | 1 to 30 characters |  |  |  |  |  |  |  |  |  |  |  | Personal information. Norm reference: NEODeS CT2026.1.2 S21.G00.30.007. |
|  | France |  | Department of Birth Code |  | Code département de naissance | The two-character code of the French department of birth. It must agree with positions 6 and 7 of the social security number. Corsica is coded 2A and 2B, and the conventional value 99 is used for a birth outside France. | M |  | Text | 2 characters: 01 to 95, 2A, 2B, 97x for the overseas departments, or 99 for a birth abroad |  |  |  |  |  |  |  |  |  |  |  | Personal information. Norm reference: NEODeS CT2026.1.2 S21.G00.30.014. |
|  | France |  | Country of Birth Code |  | Code pays de naissance | The ISO 3166-1 alpha-2 code of the country of birth. For a birth in France the code is FR and the department of birth code carries the detail. | M |  | Text | 2 letters, ISO 3166-1 alpha-2 (see the Country Codes sheet) |  |  |  |  |  |  |  |  |  |  |  | Personal information. Norm reference: NEODeS CT2026.1.2 S21.G00.30.015. |
|  | France |  | Country of Birth Name |  | Libellé du pays de naissance | The name of the country of birth in plain text, transmitted where the country of birth is not France. | CM | Mandatory where the country of birth code is not FR. | Text | 1 to 30 characters |  |  |  |  |  |  |  |  |  |  |  | Personal information. Norm reference: NEODeS CT2026.1.2 S21.G00.30.029. |
|  | France |  | Nationality Band |  | Nationalité | The employee's nationality expressed in the three bands the industrial-accident declaration form uses: French, national of another state of the European Economic Area or of Switzerland, or other. The band and not the individual nationality is what the form requires. | CM | Mandatory where an industrial-accident or occupational-disease declaration is raised for the employee. | Text | Single selection from the mapper | Nationality Band |  |  |  |  |  |  |  |  |  |  | Personal information. Only the band is collected; a finer-grained nationality field would exceed what any French payroll filing requires and would be difficult to justify under data minimisation. Source: FR-CPAM-002 Déclaration d'accident du travail (form S6200). |
|  | France |  | Cross-Border Status (EU Coding) |  | Codification UE | The employee's status relative to the European Union and the European Economic Area, used by the collecting bodies for statistical and coordination purposes: resident of France, of another EU member state, of another EEA state, or of the rest of the world. | M |  | Text | 2-character code | Cross-Border Status (EU Coding) |  |  |  |  |  |  |  |  |  |  | Personal information. This is a residence-based classification and is independent of both tax residence and social security affiliation; the three must not be conflated. Norm reference: NEODeS CT2026.1.2 S21.G00.30.013. |
|  | France |  | Highest Level of Education Attained |  | Niveau de formation le plus élevé obtenu par l'individu | The highest level of education the employee has completed, on the eight-level national scale from compulsory schooling to doctorate. | CM | Mandatory for an employee on an apprenticeship or professionalisation contract, where it is a condition of the training funding. | Text | 2-character code | Highest Level of Education Attained |  |  |  |  |  |  |  |  |  |  | Personal information. Collected only for work-study contracts; it is not a general payroll field and must not be requested from every employee. Norm reference: NEODeS CT2026.1.2 S21.G00.30.024. |
|  | France |  | Level of Qualification Being Prepared |  | Niveau de diplôme préparé par l'individu | The level of the qualification the employee is working towards under a work-study contract, on the same national scale as the field above. | CM | Mandatory for an employee on an apprenticeship or professionalisation contract. | Text | 2-character code | Level of Qualification Being Prepared |  |  |  |  |  |  |  |  |  |  | Personal information. Norm reference: NEODeS CT2026.1.2 S21.G00.30.025. |
|  | France |  | Combined Employment and Retirement |  | Cumul emploi retraite | Indicates that the employee is drawing a retirement pension while working under a contract of employment. The status changes the old-age contribution treatment: contributions remain due but, for a full-rate pension already liquidated, they generate no further pension entitlement. | CM | Mandatory where the employee has liquidated a retirement pension and continues or resumes work under a contract of employment. | Text | 2-character code | Combined Employment and Retirement |  |  |  |  |  |  |  |  |  |  | Personal information. Working pensioners under a contract of employment are in scope for this build. Norm reference: NEODeS CT2026.1.2 S21.G00.30.023. |
|  | France |  | Address - Street |  | Numéro, extension, nature et libellé de la voie | The street element of the employee's postal address: the number, any extension such as bis or ter, the type of way and its name, on a single line. | CM | Mandatory where the employee has a postal address in France or abroad, that is, in substantially every case. | Text | 1 to 50 characters |  |  |  |  |  |  |  |  |  |  |  | Contact and address. Norm reference: NEODeS CT2026.1.2 S21.G00.30.008. |
|  | France |  | Address - Delivery Service Complement |  | Service de distribution, complément de localisation de la voie | The second address line: a delivery service reference, a post box, a hamlet or any other complement locating the way. | CM | Mandatory where the address requires a delivery complement. | Text | 1 to 50 characters |  |  |  |  |  |  |  |  |  |  |  | Contact and address. Norm reference: NEODeS CT2026.1.2 S21.G00.30.017. |
|  | France |  | Address - Building Complement |  | Complément de la localisation de la construction | The address line locating the dwelling within the building: entrance, staircase, floor, flat number, residence name. | CM | Mandatory where the address requires a building complement. | Text | 1 to 50 characters |  |  |  |  |  |  |  |  |  |  |  | Contact and address. Norm reference: NEODeS CT2026.1.2 S21.G00.30.016. |
|  | France |  | Address - Postal Code |  | Code postal | The five-digit postal code of the employee's address, validated against the La Poste Hexaposte referential for a French address. | CM | Mandatory for an address in France. For an address abroad the foreign distribution code is used instead. | Text | 5 digits, validated against the La Poste Hexaposte referential |  |  |  |  |  |  |  |  |  |  |  | Contact and address. Norm reference: NEODeS CT2026.1.2 S21.G00.30.009. |
|  | France |  | Address - Town |  | Localité | The town or city of the employee's address. | CM | Mandatory where the employee has a postal address. | Text | 1 to 50 characters, letters, digits and spaces only |  |  |  |  |  |  |  |  |  |  |  | Contact and address. Norm reference: NEODeS CT2026.1.2 S21.G00.30.010. |
|  | France |  | Address - Country Code |  | Code pays | The ISO 3166-1 alpha-2 code of the country of the employee's address. It is transmitted only where the address is outside France. | CM | Mandatory where the employee's address is outside France. | Text | 2 letters, ISO 3166-1 alpha-2 (see the Country Codes sheet) |  |  |  |  |  |  |  |  |  |  |  | Contact and address. Norm reference: NEODeS CT2026.1.2 S21.G00.30.011. |
|  | France |  | Address - Foreign Distribution Code |  | Code de distribution à l'étranger | The foreign postal routing element - the equivalent of a postal code and town in the destination country's own format - used where the employee's address is outside France. | CM | Mandatory where the employee's address is outside France. | Text | 1 to 50 characters |  |  |  |  |  |  |  |  |  |  |  | Contact and address. Norm reference: NEODeS CT2026.1.2 S21.G00.30.012. |
|  | France |  | E-mail Address |  | Adresse mél | The employee's electronic mail address, used for the electronic payslip and for scheme correspondence. | CM | Mandatory where the employer issues payslips in electronic form or where the collective cover requires it. | Text | 6 to 100 characters, valid e-mail format |  |  |  |  |  |  |  |  |  |  |  | Contact and address. If the client elects electronic payslips the employee must be informed and may object, and the archiving obligation runs for 50 years or until the employee reaches 75, whichever is later. A five-year retention setting on an electronic payslip archive is a breach of Labour Code Article D3243-8. Source: FR-CCG-001 Module 2.3. |
|  | France |  | Bank Account IBAN |  | IBAN du salarié | The international bank account number of an account the employee holds or jointly holds, into which the net pay is transferred. Payment of wages above the statutory cash threshold must be made by transfer or by crossed cheque, and the employee may not be required to accept an account they do not hold. | M |  | Text | 15 to 34 characters; a French IBAN is 27 characters, FR + 2 check digits + 23 characters |  |  |  |  |  |  |  |  |  |  |  | Payment details. Legal basis: Labour Code Article L3241-1. The account must belong to, or be jointly held by, the employee; an employer may not require payment into a third party's account. Source: FR-CCG-001 Module 2.2. |
|  | France |  | Bank Identifier Code (BIC) |  | BIC du salarié | The bank identifier code of the institution holding the employee's account. | CM | Mandatory where the account is held outside the SEPA area or where the payment channel requires it. Not required for a French IBAN in a domestic SEPA transfer. | Text | 8 or 11 characters |  |  |  |  |  |  |  |  |  |  |  | Payment details. |
|  | France |  | Contract Start Date |  | Date de début du contrat | The date on which the employment contract takes effect. It is the date from which the social security ceiling entitlement, the seniority calculation and the unified degressive reduction all run for this contract. | M |  | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. France has no carry-forward of cumulative payroll figures between employers: each employer restarts the ceiling, the reduction calculation and the contribution-base caps at zero on the hire date. Source: FR-CCG-001 Module 2.2; NEODeS CT2026.1.2 S21.G00.40.001. |
|  | France |  | Date and Time of Hire |  | Date et heure d'embauche | The date and the clock time at which the employee is taken on. Both elements are required by the pre-employment declaration, which must be filed with URSSAF in the eight days before the employee starts work and no later than the moment work begins. | M |  | Text | DD/MM/YYYY HH:MM |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. The time element is easy to overlook and is not optional: Labour Code Article R1221-1, 3° (a) requires the date AND the time of hire on the pre-employment declaration. Filing late or omitting the declaration exposes the employer to the fixed penalty and, in aggravated cases, to the concealed-employment offence. Source: FR-URSSAF-001 DPAE; Labour Code Articles R1221-1 to R1221-5. |
|  | France |  | Expected Contract End Date |  | Date de fin prévisionnelle du contrat | The date on which a fixed-term contract, an assignment or a work-study contract is expected to end, as stated in the contract. It is not the actual end date, which is captured separately in the termination block. | CM | Mandatory for a fixed-term contract, a temporary-agency assignment, an apprenticeship or a professionalisation contract. Not applicable to a permanent contract. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.40.010. |
|  | France |  | Contract Nature |  | Nature du contrat | The legal form of the employment relationship: permanent contract, fixed-term contract, temporary-agency assignment, internship agreement, company officer's mandate and so on. It is the primary selector for the contribution set, the end-of-contract entitlements and the termination rules. | M |  | Text | 2-character code | Contract Nature |  |  |  |  |  |  |  |  |  |  | Contract and employment. Apprenticeship and professionalisation contracts are NOT values of this field: an apprentice is declared with the contract nature of the underlying contract, permanent or fixed-term, together with the public-policy scheme code that identifies the apprenticeship. Source: FR-CCG-001 Module 2.2; NEODeS CT2026.1.2 S21.G00.40.007. |
|  | France |  | Public-Policy or Collectively Agreed Scheme |  | Dispositif de politique publique et conventionnel | The assisted-employment or work-study scheme under which the contract is concluded, where there is one: apprenticeship, professionalisation, subsidised employment contract, industrial research training agreement, and so on. It carries the exemptions and the specific contribution treatment attaching to the scheme. | M |  | Text | 2-character code; the value 99 is used where no scheme applies | Public-Policy or Collectively Agreed Scheme |  |  |  |  |  |  |  |  |  |  | Contract and employment. This field, not the contract nature, is what identifies an apprentice or a professionalisation contract and therefore what drives the corresponding contribution and tax treatment. Norm reference: NEODeS CT2026.1.2 S21.G00.40.008. |
|  | France |  | Reason for Using a Fixed-Term or Agency Contract |  | Motif de recours | The statutory ground on which a fixed-term contract or a temporary-agency assignment is used. French law permits a fixed-term contract only for a listed reason, and the reason governs whether the end-of-contract indemnity is due. | CM | Mandatory for a fixed-term contract or a temporary-agency assignment. Not applicable to a permanent contract. | Text | 2-character code | Reason for Using a Fixed-Term or Agency Contract |  |  |  |  |  |  |  |  |  |  | Contract and employment. The reason is not administrative colour: a seasonal contract and a contract of customary use carry no 10% end-of-contract indemnity, while a replacement or activity-increase contract does. Source: FR-CCG-001 Module 9; NEODeS CT2026.1.2 S21.G00.40.021. |
|  | France |  | Trial Period Duration |  | Durée de la période d'essai | The length of any trial period stipulated in the contract, expressed in the unit the contract uses. It is required on the pre-employment declaration and it governs the shortened notice arrangements applying during the trial. | CM | Mandatory where the contract stipulates a trial period. | Text | Free text stating the number and the unit, for example "2 mois" or "15 jours" |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. Legal basis: Labour Code Article R1221-1, 3° (d). Source: FR-URSSAF-001 DPAE. |
|  | France |  | Job Title |  | Libellé de l'emploi | The employee's job title in plain language, as it appears in the contract and on the payslip. | M |  | Text | 1 to 120 characters |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.40.006. |
|  | France |  | Occupation Code (PCS-ESE) |  | Code profession et catégorie socioprofessionnelle (PCS-ESE) | The four-character INSEE occupation and socio-professional category code for the post. It is a statistical classification used by INSEE and DARES and it is independent of the collective-agreement grading. | M |  | Text | 4 characters, from the INSEE PCS-ESE referential |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.40.004. |
|  | France |  | PCS-ESE Complement Code |  | Code complément PCS-ESE | The complement to the occupation code, used for certain sectors and grade referentials. | CM | Mandatory where the sector referential attaching to the PCS-ESE code requires a complement. | Text | 2 to 6 characters, from the DSN PCS-ESE complement referential |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. The public-service grade referentials NEH, NET and NNE that also use this rubrique are outside the scope of this build. Norm reference: NEODeS CT2026.1.2 S21.G00.40.005. |
|  | France |  | Employee Status under the Collective Agreement |  | Statut du salarié (conventionnel) | The employee's occupational category under the collective agreement: senior executive, other managerial grade, intermediate profession, clerical employee or manual worker. It is one of the two status fields, and it is the one used for statistical and collective-agreement purposes. | M |  | Text | 2-character code | Employee Status under the Collective Agreement |  |  |  |  |  |  |  |  |  |  | Contract and employment. Distinct from, and to be captured independently of, the supplementary-pension category status below: the two answer different questions and can legitimately disagree. Source: FR-CCG-001 Module 2.2; NEODeS CT2026.1.2 S21.G00.40.002. |
|  | France |  | Supplementary Pension Category Status |  | Code statut catégoriel Retraite Complémentaire obligatoire | Whether the employee is treated as managerial grade for the compulsory supplementary pension scheme. Since the 2019 Agirc-Arrco merger there is no separate managerial-grade pension scheme, but this status still governs the compulsory 1.50% employer death-and-disability contribution on the first band of pay and membership of the executive employment association. | M |  | Text | 2-character code | Supplementary Pension Category Status |  |  |  |  |  |  |  |  |  |  | Contract and employment. This is the field that triggers the 1.50% employer death-and-disability contribution. Failure to insure a managerial-grade employee makes the employer liable to the beneficiaries for a capital sum equal to three years' pay, so the flag is not merely declarative. Source: FR-CCG-001 Modules 2.2 and 5; NEODeS CT2026.1.2 S21.G00.40.003. |
|  | France |  | Employment Status |  | Statut d'emploi du salarié | Whether the employee holds a statutory or a non-statutory position. In a private-sector build under the general scheme the applicable value is normally "not concerned"; the statutory values exist for the special schemes. | M |  | Text | 2-character code | Employment Status |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.40.026. |
|  | France |  | Grading Coefficient |  | Coefficient hiérarchique | The grading coefficient assigned to the post under the applicable collective agreement. It is one of the inputs to the agreed minimum pay for the grade. | CM | Mandatory where the applicable collective agreement uses a coefficient-based grading system. | Text | 1 to 8 characters: up to 3 digits, or up to 5 alphanumeric characters, a dot and 2 alphanumeric characters |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.40.071. |
|  | France |  | Step |  | Échelon | The step within the grade under the applicable collective agreement. | CM | Mandatory where the applicable collective agreement uses steps. | Text | 2 digits, 01 to 12 |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.40.070. |
|  | France |  | Pay Level |  | Niveau de rémunération | The pay level or band assigned to the post under the applicable collective agreement. | CM | Mandatory where the applicable collective agreement uses pay levels. | Text | 2 to 3 characters |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.40.069. |
|  | France |  | Position in the Collective Agreement |  | Positionnement dans la convention collective | The employee's position in the classification grid of the applicable collective agreement, in plain text, where the grid is not adequately expressed by the coefficient, step and level fields. | CM | Mandatory where the applicable collective agreement requires a textual classification. | Text | 1 to 100 characters |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.40.041. |
|  | France |  | Final Classification Category |  | Catégorie de classement finale | The final classification category resulting from the grading, where the collective agreement produces a single consolidated category. | CM | Mandatory where the applicable collective agreement produces a consolidated final classification category. | Text | 2 digits, 01 to 20 |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.40.075. |
|  | France |  | Contract-Level Collective Agreement Code (IDCC) |  | Code convention collective applicable au contrat | The collective agreement applying to this individual contract, where it differs from the agreement recorded for the establishment. It is a mandatory payslip mention. | M |  | Text | 4 digits, from the DSN CCN referential |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. Captured at three levels in France - entity, establishment and contract - because a multi-establishment employer may apply different agreements and an individual contract may depart from its establishment default. Source: FR-CCG-001 Module 2.1; NEODeS CT2026.1.2 S21.G00.40.017. |
|  | France |  | Place-of-Work Identifier |  | Identifiant du lieu de travail | The identifier of the site at which the employee actually works, where that site is not the employing establishment. It is normally the SIRET of the site. | CM | Mandatory where the employee works at a site other than the employing establishment, and for a temporary-agency assignment. | Text | 2 to 14 characters; normally a 14-digit SIRET |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. The place of work, not the employee's residence and not the employing establishment, is what triggers the Alsace-Moselle local health scheme and what determines the mobility levy rate. Getting this field wrong produces a wrong contribution set, not merely a wrong statistic. Source: FR-CCG-001 Module 2.1; NEODeS CT2026.1.2 S21.G00.40.019 and S21.G00.85.001. |
|  | France |  | Multiple-Jobs Code |  | Code emplois multiples | Whether the employee holds one post or several posts with this employer. It is used by the collecting bodies to reconcile several contract blocks for the same individual. | M |  | Text | 2-character code | Multiple-Jobs Code |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.40.036. |
|  | France |  | Multiple-Employers Code |  | Code employeurs multiples | Whether the employee works for this employer only or for several employers. It matters because each employer restarts the social security ceiling independently, so an employee with several employers may exceed the annual ceiling across the group of them. | M |  | Text | 2-character code | Multiple-Employers Code |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.40.037. |
|  | France |  | Worker Abroad Status |  | Travailleur à l'étranger au sens du code de la Sécurité Sociale | Whether the employee works outside France and on what footing: posted by this employer and remaining in the French scheme, expatriate outside the French scheme, or frontier worker. | M |  | Text | 2-character code | Worker Abroad Status |  |  |  |  |  |  |  |  |  |  | Contract and employment. This field records an employee sent OUT of France by a French employer. A worker posted INTO France who remains affiliated to a foreign scheme under a portable document A1 is outside the scope of this build entirely: no French contributions are due and there is no French payslip to produce. Source: FR-CCG-001 Module 2.2; scope_manifest.json employment_types.out_of_scope; NEODeS CT2026.1.2 S21.G00.40.024. |
|  | France |  | DSN Exclusion Reason |  | Motif d'exclusion DSN | The ground on which a contract is excluded from the ordinary DSN population, for the small number of categories that are declared through another channel. | CM | Mandatory only where the contract falls into one of the excluded categories. | Text | 2-character code | DSN Exclusion Reason |  |  |  |  |  |  |  |  |  |  | Contract and employment. Every value of this code list falls outside the scope of this build. The field is carried so that an excluded contract can be recognised and routed away from the DSN rather than silently mis-declared. Norm reference: NEODeS CT2026.1.2 S21.G00.40.025. |
|  | France |  | Seniority Type |  | Type d'ancienneté | Which seniority is being recorded: seniority in the entity, in the group, in the post, in the occupational category or in the sector. Several collective-agreement entitlements turn on one of these rather than on length of service in the entity. | CM | Mandatory where a seniority value is recorded for the contract. | Text | 2-character code | Seniority Type |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.86.001. |
|  | France |  | Seniority Unit of Measure |  | Unité de mesure de l'ancienneté | The unit in which the seniority value is expressed: days, months or years. | CM | Mandatory where a seniority value is recorded for the contract. | Text | 2-character code | Seniority Unit of Measure |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.86.002. |
|  | France |  | Seniority Value |  | Valeur de l'ancienneté | The seniority accrued, expressed in the unit stated above and for the seniority type stated above. | CM | Mandatory where a seniority type and unit are recorded for the contract. | Integer | Up to 5 digits |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. Length of service must be migrated when the payroll provider changes: restarting it at zero under-calculates severance, notice and every collective-agreement entitlement that turns on it. Source: FR-CCG-001 Module 2.3; NEODeS CT2026.1.2 S21.G00.86.003. |
|  | France |  | Unemployment-Insurance Allocation Code |  | Code affectation Assurance chômage | The allocation code identifying the unemployment-insurance arrangement applying to the contract, where the employer is not on the ordinary arrangement. | CM | Mandatory where the employer or the contract is on a specific unemployment-insurance arrangement. | Text | 6 characters |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.40.027. |
|  | France |  | Specific Flat-Rate Professional-Expenses Deduction Rate |  | Taux de déduction forfaitaire spécifique pour frais professionnels | The rate of the specific flat-rate deduction for professional expenses applied to the contribution base, where the employee's occupation is one of those for which the deduction is available and the conditions for applying it are met. | CM | Mandatory where the specific flat-rate deduction is applied to the contract. Not applicable otherwise. | Decimal | Percentage to 2 decimals |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. This is master data and not a parameter: the rate depends on the occupation and, since the 2021 reform, on an election that must be evidenced and that is being phased down occupation by occupation. It is per contract, it must be supplied by the client and it is one of the highest-value findings in a URSSAF inspection when applied without evidence. Norm reference: NEODeS CT2026.1.2 S21.G00.40.023. |
|  | France |  | Remuneration by Tips |  | Rémunération au pourboire | Indicates that the employee is remunerated wholly or partly by tips, which changes how the contribution base is constituted. | CM | Mandatory where the employee is remunerated wholly or partly by tips. | Text | 2-character code | Remuneration by Tips |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.40.045. |
|  | France |  | Contract-Level Occupational Health Service Identifier |  | Identifiant du Service de Prévention et de Santé au Travail (contrat) | The occupational health service to which this individual contract is attached, where it differs from the establishment default. | CM | Mandatory where the employee is attached to an occupational health service other than the establishment default. | Text | 1 to 14 characters |  |  |  |  |  |  |  |  |  |  |  | Contract and employment. Norm reference: NEODeS CT2026.1.2 S21.G00.30.030. |
|  | France |  | Previously Declared Contract Number |  | Numéro du contrat déclaré précédemment | The contract number under which this contract was previously declared, where the contract has been transferred between establishments or between employers without a break, or where the employer has renumbered its contracts. | CM | Mandatory where the contract was previously declared under another number or by another SIRET. | Text | 5 to 20 characters |  |  |  |  |  |  |  |  |  |  |  | Previous employment. Together with the field below this preserves the continuity the collecting bodies check across declarations. Norm reference: NEODeS CT2026.1.2 S21.G00.45.002. |
|  | France |  | SIRET That Previously Declared the Contract |  | SIRET déclarant le contrat précédemment | The SIRET of the establishment that previously declared this contract, where it has been transferred. | CM | Mandatory where the contract was previously declared by another SIRET. | Text | 14 digits |  |  |  |  |  |  |  |  |  |  |  | Previous employment. Norm reference: NEODeS CT2026.1.2 S21.G00.45.001. |
|  | France |  | Prior End-of-Contract Certificate Received |  | Attestation employeur du précédent employeur reçue | Confirms that the new joiner has produced the end-of-contract certificate from the previous employer, now transmitted through the DSN. It establishes the end date and the reason of the previous contract, which matters where a notice period overlaps the new hire date. | CM | Mandatory for a new joiner who was previously employed elsewhere. | Text | Yes / No |  |  |  |  |  |  |  |  |  |  |  | Previous employment. France has no carry-forward of cumulative payroll figures between employers, so what the new joiner must supply is documentary rather than numerical. Without this certificate there is a risk of overlapping declarations for the same period. Source: FR-CCG-001 Module 2.2. |
|  | France |  | Prior Final Settlement Statement Received |  | Solde de tout compte du précédent employeur reçu | Confirms that the new joiner has produced the final settlement statement from the previous employer, which shows whether accrued paid leave was already paid out. | CM | Mandatory for a new joiner who was previously employed elsewhere. | Text | Yes / No |  |  |  |  |  |  |  |  |  |  |  | Previous employment. Without it there is a risk of paying the same leave entitlement twice. Two things the employee does NOT need to supply: the previous employer's payslips, because there is no cumulative carry-forward, and the withholding rate, because the tax administration transmits it directly. Source: FR-CCG-001 Module 2.2. |
|  | France |  | Contractual Working Time |  | Quotité de travail du contrat | The working time stipulated in the contract, expressed in the unit of measure recorded below. For a full-time 35-hour week it is 151.67 hours a month. | M |  | Decimal | Numeric with 2 decimals, for example 151.67 |  |  |  |  |  |  |  |  |  |  |  | Working time. It drives the proration of the social security ceiling for a part-time employee, the minimum-wage test, the overtime threshold and the unified degressive reduction. Source: FR-CCG-001 Module 2.2; NEODeS CT2026.1.2 S21.G00.40.013. |
|  | France |  | Reference Working Time for the Category |  | Quotité de travail de référence de l'entreprise pour la catégorie de salarié | The full-time reference working time the entity applies to the employee's category. The ratio of the contractual working time to this reference is what defines part-time working and what prorates the ceiling. | M |  | Decimal | Numeric with 2 decimals, for example 151.67 |  |  |  |  |  |  |  |  |  |  |  | Working time. Norm reference: NEODeS CT2026.1.2 S21.G00.40.012. |
|  | France |  | Working-Time Unit of Measure |  | Unité de mesure de la quotité de travail | The unit in which the contractual working time is expressed: hours, days, an annual day-count arrangement, an hour-count arrangement, or one of the piece and assignment bases used in specific sectors. | M |  | Text | 2-character code | Working-Time Unit of Measure |  |  |  |  |  |  |  |  |  |  | Working time. An employee on an annual day-count arrangement, typically 218 days, works no overtime, so the unit of measure is a genuine calculation-path selector and not a label. Source: FR-CCG-001 Module 2.2; NEODeS CT2026.1.2 S21.G00.40.011. |
|  | France |  | Working-Time Arrangement |  | Modalité d'exercice du temps de travail | Whether the employee works full time, part time, part time as of right, or part time as of right for a child. | M |  | Text | 2-character code | Working-Time Arrangement |  |  |  |  |  |  |  |  |  |  | Working time. Norm reference: NEODeS CT2026.1.2 S21.G00.40.014. |
|  | France |  | Part-Time Working Rate |  | Taux de travail à temps partiel | The employee's working time as a percentage of the full-time reference, for a part-time employee. | CM | Mandatory where the working-time arrangement is part time. Not applicable to a full-time employee. | Decimal | Percentage to 2 decimals, for example 80.00 |  |  |  |  |  |  |  |  |  |  |  | Working time. Norm reference: NEODeS CT2026.1.2 S21.G00.40.055. |
|  | France |  | Part-Time Employee Contributing on a Full-Time Basis |  | Salarié à temps partiel cotisant à temps plein | Indicates that the employer and the employee have agreed, in writing, that old-age contributions are computed on the full-time equivalent pay even though the employee works part time, so that the part-time work does not reduce the pension entitlement. The code states whether the agreement covers the basic old-age scheme alone or the basic scheme and the supplementary pension. | CM | Mandatory where such an agreement is in force for the contract. | Text | 2-character code | Part-Time Contribution on a Full-Time Basis |  |  |  |  |  |  |  |  |  |  | Working time. The agreement must be in writing and the employer normally bears the difference. Norm reference: NEODeS CT2026.1.2 S21.G00.40.044. |
|  | France |  | Sickness-Risk Basic Scheme Code |  | Code régime de base risque maladie | The basic scheme covering the employee for the sickness risk. For a private-sector employee under the general scheme it is the general scheme code. | M |  | Text | 3-character code | Sickness-Risk Basic Scheme Code |  |  |  |  |  |  |  |  |  |  | Social security profile. Norm reference: NEODeS CT2026.1.2 S21.G00.40.018. |
|  | France |  | Old-Age-Risk Basic Scheme Code |  | Code régime de base risque vieillesse | The basic scheme covering the employee for the old-age risk. For a private-sector employee under the general scheme it is the general scheme code. | M |  | Text | 3-character code | Old-Age-Risk Basic Scheme Code |  |  |  |  |  |  |  |  |  |  | Social security profile. Norm reference: NEODeS CT2026.1.2 S21.G00.40.020. |
|  | France |  | Occupational-Accident-Risk Basic Scheme Code |  | Code régime de base risque accident du travail | The basic scheme covering the employee for the occupational-accident and occupational-disease risk. | M |  | Text | 3-character code | Occupational-Accident-Risk Basic Scheme Code |  |  |  |  |  |  |  |  |  |  | Social security profile. Norm reference: NEODeS CT2026.1.2 S21.G00.40.039. |
|  | France |  | Contract-Level Occupational-Accident Risk Code |  | Code risque accident du travail (contrat) | The occupational-accident risk code applying to this contract, where the employee is rated under a risk code other than the establishment default - for example an employee working at a site with a different risk classification. | M |  | Text | 5 to 6 characters, from the DSN AT/MP risk-code referential |  |  |  |  |  |  |  |  |  |  |  | Social security profile. Defaults to the establishment risk code recorded on the ID Information sheet, but must be capable of being overridden per contract. Norm reference: NEODeS CT2026.1.2 S21.G00.40.040. |
|  | France |  | Compulsory Scheme Base Complement |  | Complément de base au régime obligatoire | Identifies a local scheme layered on top of the general scheme. For this build the value that matters is the Alsace-Moselle local health scheme. | M |  | Text | 2-character code | Compulsory Scheme Base Complement |  |  |  |  |  |  |  |  |  |  | Social security profile. Employees whose PLACE OF WORK is in Bas-Rhin, Haut-Rhin or Moselle pay an additional employee health contribution of 1.30% of total remuneration for 2026, held unchanged from 2025 by decision of the local scheme's board of 19 December 2025, and receive two extra public holidays. The trigger is the place of work, not the employee's residence. Source: FR-CCG-001 Module 2.1; NEODeS CT2026.1.2 S21.G00.40.016. |
|  | France |  | Supplementary Pension Scheme Code |  | Code régime Retraite Complémentaire | The compulsory supplementary pension scheme to which the employee is affiliated. Since 1 January 2019 the private-sector scheme is the unified Agirc-Arrco scheme. | M |  | Text | 4 to 8 characters | Supplementary Pension Scheme Code |  |  |  |  |  |  |  |  |  |  | Social security profile. Norm reference: NEODeS CT2026.1.2 S21.G00.71.002. |
|  | France |  | Sickness-Risk Delegated Administrator Code |  | Code délégataire du risque maladie | The body administering the sickness risk for the employee, where administration has been delegated by the primary fund - for example a student mutual or a delegated administration body. | CM | Mandatory where the employee's sickness risk is administered by a delegated body rather than by the primary sickness insurance fund. | Text | 3-character code |  |  |  |  |  |  |  |  |  |  |  | Social security profile. Norm reference: NEODeS CT2026.1.2 S21.G00.40.035. |
|  | France |  | Collective Cover - Affiliation Technical Identifier |  | Identifiant technique affiliation | The technical sequence number of the employee's affiliation to a collective health or death-and-disability contract. It is the key linking the employee to one specific membership held by the employer. | CM | Mandatory where the employee is affiliated to a collective health or death-and-disability contract. | Text | 1 to 3 digits, from 1 |  |  |  |  |  |  |  |  |  |  |  | Collective cover. Norm reference: NEODeS CT2026.1.2 S21.G00.70.012. |
|  | France |  | Collective Cover - Membership Technical Identifier |  | Identifiant technique adhésion (affiliation) | The technical identifier of the employer membership to which this employee affiliation attaches, where the employer holds several contracts with the same insurer. | CM | Mandatory where the employee is affiliated to a collective health or death-and-disability contract. | Text | 1 to 3 digits, from 1 |  |  |  |  |  |  |  |  |  |  |  | Collective cover. Norm reference: NEODeS CT2026.1.2 S21.G00.70.013. |
|  | France |  | Collective Cover - Option Chosen |  | Code option retenue par le salarié | The cover option the employee has selected within the collective contract, where the contract offers options - for example a base option or a reinforced option. | CM | Mandatory where the collective contract offers more than one option. | Text | 1 to 30 characters, as defined by the insurer |  |  |  |  |  |  |  |  |  |  |  | Collective cover. Norm reference: NEODeS CT2026.1.2 S21.G00.70.004. |
|  | France |  | Collective Cover - Attachment Population |  | Code population de rattachement | The population within the collective contract to which the employee belongs, where the contract distinguishes populations - for example managerial and non-managerial grades with different premiums. | CM | Mandatory where the collective contract distinguishes populations. | Text | 1 to 30 characters, as defined by the insurer |  |  |  |  |  |  |  |  |  |  |  | Collective cover. Norm reference: NEODeS CT2026.1.2 S21.G00.70.005. |
|  | France |  | Collective Cover - Affiliation Start Date |  | Date de début de l'affiliation | The date from which the employee is affiliated to the collective health or death-and-disability contract. | CM | Mandatory where the employee is affiliated to a collective health or death-and-disability contract. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Collective cover. Norm reference: NEODeS CT2026.1.2 S21.G00.70.014. |
|  | France |  | Collective Cover - Affiliation End Date |  | Date de fin de l'affiliation | The date on which the employee's affiliation to the collective contract ends. | CM | Mandatory where the affiliation has ended. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Collective cover. Norm reference: NEODeS CT2026.1.2 S21.G00.70.015. |
|  | France |  | Health Cover Exemption Claimed |  | Dispense d'affiliation à la complémentaire santé demandée | Indicates that the employee has asked, in writing, to be exempted from membership of the compulsory supplementary health cover. The exemption is lawful only if the employee requests it in writing, provides evidence, and the founding document of the scheme provides for it. | CM | Mandatory where the employee has claimed an exemption from the compulsory health cover. | Text | Yes / No |  |  |  |  |  |  |  |  |  |  |  | Collective cover. An exemption granted without evidence is the most common finding in a contribution inspection of this area, because the employer's contribution is then treated as ordinary pay for the whole period concerned. Source: FR-CCG-001 Module 5. |
|  | France |  | Health Cover Exemption Reason |  | Motif de dispense d'affiliation | The ground on which the employee is exempted from membership of the compulsory supplementary health cover. | CM | Mandatory where an exemption from the compulsory health cover is claimed. | Text | Single selection from the mapper | Health Cover Exemption Reason |  |  |  |  |  |  |  |  |  |  | Collective cover. The written request and its supporting evidence must be renewed annually. Source: FR-CCG-001 Module 5. |
|  | France |  | Health Cover Exemption Evidence Date |  | Date de l'attestation justifiant la dispense | The date of the supporting evidence produced for the health cover exemption - typically a certificate of cover from a spouse's employer. | CM | Mandatory where an exemption from the compulsory health cover is claimed. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Collective cover. Held so that the annual renewal can be monitored; evidence more than a year old no longer supports the exemption. Source: FR-CCG-001 Module 5. |
|  | France |  | Number of Dependent Children |  | Nombre d'enfants à charge | The number of children the employee has as dependants. It is used by the collective cover for the premium and it is one of the inputs to the wage-attachment scale. | CM | Mandatory where the employee has dependent children and either a collective cover premium or a wage attachment turns on the number. | Integer | 1 to 2 digits |  |  |  |  |  |  |  |  |  |  |  | Dependants. Legal basis for the attachment use: Décret n° 2025-1299 of 24 December 2025 (wage attachment bands). Norm reference: NEODeS CT2026.1.2 S21.G00.70.007. |
|  | France |  | Number of Adult Dependants Covered |  | Nombre d'ayants-droit conjoint / concubin | The number of spouse, civil partner or cohabiting partner dependants covered under the employee's collective health or death-and-disability contract. | CM | Mandatory where the collective contract prices on the number of covered dependants. | Integer | 1 to 2 digits |  |  |  |  |  |  |  |  |  |  |  | Dependants. Norm reference: NEODeS CT2026.1.2 S21.G00.70.008. |
|  | France |  | Number of Child Dependants Covered |  | Nombre d'enfants ayants-droit | The number of children covered as dependants under the employee's collective health or death-and-disability contract. | CM | Mandatory where the collective contract prices on the number of covered dependants. | Integer | 1 to 2 digits |  |  |  |  |  |  |  |  |  |  |  | Dependants. Norm reference: NEODeS CT2026.1.2 S21.G00.70.011. |
|  | France |  | Number of Other Dependants Covered |  | Nombre d'ayants-droit autres (ascendants, collatéraux) | The number of other dependants - ascendants, collaterals - covered under the employee's collective health or death-and-disability contract. | CM | Mandatory where the collective contract prices on the number of covered dependants. | Integer | 1 to 2 digits |  |  |  |  |  |  |  |  |  |  |  | Dependants. Norm reference: NEODeS CT2026.1.2 S21.G00.70.010. |
|  | France |  | Total Number of Dependants Covered |  | Nombre d'ayants-droit attachés au salarié | The total number of dependants attached to the employee for the collective cover named. | CM | Mandatory where the collective contract prices on the number of covered dependants. | Integer | 1 to 2 digits |  |  |  |  |  |  |  |  |  |  |  | Dependants. Norm reference: NEODeS CT2026.1.2 S21.G00.70.009. |
|  | France |  | Dependant - Type |  | Type d'ayant-droit | Whether the named dependant is an adult - spouse, civil partner or cohabiting partner - a child, or another dependant such as an ascendant or a collateral. | CM | Mandatory for each dependant named individually under the collective cover. | Text | 2-character code | Dependant Type |  |  |  |  |  |  |  |  |  |  | Dependants. Norm reference: NEODeS CT2026.1.2 S21.G00.73.003. |
|  | France |  | Dependant - Surname at Birth |  | Nom de famille de l'ayant-droit | The family name of the named dependant as it appears on the birth record. | CM | Mandatory for each dependant named individually under the collective cover. | Text | 1 to 80 characters |  |  |  |  |  |  |  |  |  |  |  | Dependants. Norm reference: NEODeS CT2026.1.2 S21.G00.73.006. |
|  | France |  | Dependant - Forenames |  | Prénoms de l'ayant-droit | The given names of the named dependant. | CM | Mandatory for each dependant named individually under the collective cover. | Text | 1 to 80 characters |  |  |  |  |  |  |  |  |  |  |  | Dependants. Norm reference: NEODeS CT2026.1.2 S21.G00.73.009. |
|  | France |  | Dependant - Date of Birth |  | Date de naissance de l'ayant-droit | The date of birth of the named dependant. | CM | Mandatory for each dependant named individually under the collective cover. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Dependants. Norm reference: NEODeS CT2026.1.2 S21.G00.73.005. |
|  | France |  | Dependant - Social Security Number (NIR) |  | NIR de l'ayant-droit | The social security number of the named dependant, where the dependant holds one in their own right. | CM | Mandatory for a named dependant who holds a NIR in their own right - typically an adult dependant. | Text | 13 digits, same structure as the employee NIR |  |  |  |  |  |  |  |  |  |  |  | Dependants. Special-category considerations apply: dependant data is collected only because the collective cover requires it and must not be retained beyond the affiliation. Source: FR-CCG-001 Module 2.3; NEODeS CT2026.1.2 S21.G00.73.007. |
|  | France |  | Dependant - Primary Insured's NIR |  | NIR ouvrant-droit régime de base maladie | The social security number of the person through whom the dependant derives their basic sickness cover, where that person is not the employee. | CM | Mandatory where the dependant derives basic sickness cover through a person other than the employee. | Text | 13 digits, same structure as the employee NIR |  |  |  |  |  |  |  |  |  |  |  | Dependants. Norm reference: NEODeS CT2026.1.2 S21.G00.73.008. |
|  | France |  | Dependant - Attachment Start Date |  | Date de début de rattachement à l'ouvrant-droit | The date from which the dependant is attached to the primary insured under the collective cover. | CM | Mandatory for each dependant named individually under the collective cover. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Dependants. Norm reference: NEODeS CT2026.1.2 S21.G00.73.004. |
|  | France |  | Dependant - Attachment End Date |  | Date de fin de rattachement à l'ouvrant-droit | The date on which the dependant's attachment to the primary insured ends. | CM | Mandatory where the attachment has ended. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Dependants. Norm reference: NEODeS CT2026.1.2 S21.G00.73.011. |
|  | France |  | Dependant - Alsace-Moselle Local Scheme |  | Régime local Alsace-Moselle (ayant-droit) | Indicates that the named dependant is covered by the Alsace-Moselle local health scheme. | CM | Mandatory where the dependant is covered by the Alsace-Moselle local scheme. | Text | 2-character code | Alsace-Moselle Local Scheme |  |  |  |  |  |  |  |  |  |  | Dependants. Norm reference: NEODeS CT2026.1.2 S21.G00.73.001. |
|  | France |  | Dependant - Sickness Insurance Body Code |  | Code organisme d'affiliation à l'assurance maladie de l'ayant-droit | The code of the sickness insurance body with which the named dependant is affiliated. | CM | Mandatory where the collective contract requires the dependant's sickness insurance body to be identified. | Text | 1 to 30 characters |  |  |  |  |  |  |  |  |  |  |  | Dependants. Norm reference: NEODeS CT2026.1.2 S21.G00.73.010. |
|  | France |  | Disabled-Worker Beneficiary Status (BOETH) |  | Statut BOETH | The ground on which the employee counts towards the employer's disabled-worker employment obligation: recognition by the disability rights commission, an industrial-accident annuity for at least 10% permanent incapacity, an invalidity pension reducing working capacity by at least two thirds, and so on. | CM | Mandatory where the employee has declared a disabled-worker status and wishes it to be counted. The declaration is voluntary and cannot be required. | Text | 2-character code | Disabled-Worker Beneficiary Status (BOETH) |  |  |  |  |  |  |  |  |  |  | Statutory add-ons. Disabled-worker status is special-category data under the GDPR: it requires a distinct justification, restricted access and separate retention. It reduces the annual employment-obligation contribution, so omitting it overstates the contribution. Source: FR-CCG-001 Modules 2.2 and 2.3; NEODeS CT2026.1.2 S21.G00.40.072. |
|  | France |  | Occupational Hardship Exposure Factor |  | Facteur d'exposition à la pénibilité | The occupational hardship factor to which the employee is exposed beyond the statutory thresholds: hyperbaric environment, extreme temperatures, noise, night work, successive alternating shifts, or repetitive work. | CM | Mandatory where the employee is exposed to one or more hardship factors beyond the statutory thresholds during the attachment year. | Text | 2-character code; declared once per factor | Occupational Hardship Exposure Factor |  |  |  |  |  |  |  |  |  |  | Statutory add-ons. Declared annually and credited to the employee's professional prevention account. Norm reference: NEODeS CT2026.1.2 S21.G00.34.001. |
|  | France |  | Public Transport Season Ticket Held |  | Abonnement de transport public souscrit | Indicates that the employee holds a season ticket for public transport between home and work, which the employer must reimburse at 50%. | CM | Mandatory where the employee holds a public transport season ticket and claims the reimbursement. | Text | Yes / No |  |  |  |  |  |  |  |  |  |  |  | Statutory add-ons. The 50% employer reimbursement is compulsory nationwide under Labour Code Article L3261-2 and applies whether or not a mobility levy is payable in the commune. Failing to reimburse is a breach, not a discretionary saving. The reimbursed AMOUNT is a payroll component and belongs to FR-WTC-001; only the eligibility flag and the ticket reference are master data. Source: FR-CCG-001 Modules 2.2 and 4. |
|  | France |  | Public Transport Season Ticket Reference |  | Référence de l'abonnement de transport | The reference of the employee's public transport season ticket, held as the evidence supporting the compulsory 50% reimbursement. | CM | Mandatory where the employee claims the public transport season ticket reimbursement. | Text | Free text |  |  |  |  |  |  |  |  |  |  |  | Statutory add-ons. Source: FR-CCG-001 Module 4. |
|  | France |  | Wage Attachment in Force |  | Saisie sur rémunération en cours | Indicates that a wage attachment, an assignment of wages or a maintenance order is in force against the employee. Attachments follow the employee, not the employer, so a new joiner must declare any order already in force. | CM | Mandatory where an attachment, assignment or maintenance order is in force against the employee. | Text | Yes / No |  |  |  |  |  |  |  |  |  |  |  | Deductions. If the employer does not act on an order served on it, it becomes personally liable to the creditor for the sums that should have been withheld. The procedure ceased to be judicial on 1 July 2025 and is now conducted by court enforcement officers under Act n° 2023-1059 of 20 November 2023 and the implementing Décret of 12 February 2025. Source: FR-CCG-001 Modules 2.2 and 7. |
|  | France |  | Wage Attachment Type |  | Type de saisie ou de cession | The category of the order in force, which fixes its rank in the statutory priority order and whether it is limited by the seizable fraction: direct payment of maintenance, an assignment of wages, an administrative levy by the tax authorities, or an ordinary garnishment. | CM | Mandatory where a wage attachment is in force against the employee. | Text | Single selection from the mapper | Wage Attachment Type |  |  |  |  |  |  |  |  |  |  | Deductions. The priority order is statutory and is not a matter of arrival sequence: direct payment of maintenance ranks first and is NOT limited by the seizable fraction. Source: FR-CCG-001 Module 7. |
|  | France |  | Wage Attachment Reference |  | Référence de l'acte de saisie | The reference of the record of attachment issued by the court enforcement officer, or of the administrative levy notice issued by the public finances directorate. | CM | Mandatory where a wage attachment is in force against the employee. | Text | 1 to 40 characters |  |  |  |  |  |  |  |  |  |  |  | Deductions. Where the order is an administrative third-party attachment issued by DGFiP, this field holds the SATD identifier, which is echoed back in the DSN. Norm reference: NEODeS CT2026.1.2 S21.G00.98.001. |
|  | France |  | Tax Residence Status |  | Statut de résidence fiscale | Whether the employee is domiciled in France for tax purposes. An individual is a French tax resident if any one of the tests in General Tax Code Article 4 B is met - household or principal place of stay in France, main professional activity carried on in France, or centre of economic interests in France - subject to any applicable double tax treaty. | M |  | Text | Single selection from the mapper | Tax Residence Status |  |  |  |  |  |  |  |  |  |  | Tax profile. France operates TWO INDEPENDENT status tests and confusing them is a classic source of error: an individual can be a French tax resident affiliated to a foreign social security scheme, or the reverse. Tax residence decides the income tax mechanism; social security affiliation decides whether French contributions are due at all. Legal basis: General Tax Code Article 4 B. Source: FR-CCG-001 Module 2.2. |
|  | France |  | Withholding-at-Source Rate |  | Taux de prélèvement à la source | The income tax withholding rate to apply to the employee, as transmitted by the tax administration in the DSN return flow. The employer never computes this rate and never asks the employee for it. | CM | Mandatory once the tax administration has transmitted a rate for the employee. Until a rate is received the statutory default grid applies. | Decimal | Percentage to 2 decimals, for example 7.50 |  |  |  |  |  |  |  |  |  |  |  | Tax profile. This is master data supplied by the authority and stored against the employee, not a parameter and not a calculated value. The employer applies the default grid until the rate arrives, typically in the return flow following the first DSN. Source: FR-CCG-001 Modules 2.2 and 6; FR-DGFIP-002 Compte rendu métier PAS; NEODeS CT2026.1.2 S21.G00.50.006. |
|  | France |  | Withholding Rate Type |  | Type du taux de prélèvement à la source | Which rate is being applied: the rate transmitted by the tax administration, or one of the statutory default grids by territory and by pay period. | M |  | Text | 2-character code | Withholding Rate Type |  |  |  |  |  |  |  |  |  |  | Tax profile. The default grids in force from 1 May 2026 are published at BOI-BAREME-000037-20260407; the 2025 grids are superseded and must not be used. Source: FR-CCG-001 Module 6; NEODeS CT2026.1.2 S21.G00.50.007. |
|  | France |  | Withholding Rate Identifier |  | Identifiant du taux de prélèvement à la source | The identifier the tax administration attaches to the rate it transmits. It is echoed back in the DSN so that the administration can match the rate applied to the rate it issued. | CM | Mandatory where a rate transmitted by the tax administration is applied. | Text | As transmitted by DGFiP |  |  |  |  |  |  |  |  |  |  |  | Tax profile. Source: FR-DGFIP-002; NEODeS CT2026.1.2 S21.G00.50.008. |
|  | France |  | Withholding Rate Validity Date |  | Date de validité du taux de prélèvement à la source | The date until which the transmitted withholding rate remains valid. A rate that has expired must not be reapplied: the default grid takes over until a new rate is received. | CM | Mandatory where a rate transmitted by the tax administration is applied. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Tax profile. Stored with the rate; it drives the date check on every payroll run. Applying a lapsed rate is the defect this field exists to prevent. Source: FR-DGFIP-002. |
|  | France |  | Foreign Status for Tax Purposes |  | Statut à l'étranger au sens fiscal | Whether the employee is a frontier worker or works abroad, for income tax purposes. It is a tax classification and is independent of the social security worker-abroad status recorded above. | CM | Mandatory where the employee is a frontier worker or works abroad. | Text | 2-character code | Foreign Status for Tax Purposes |  |  |  |  |  |  |  |  |  |  | Tax profile. A non-resident employee working in France and affiliated to the French scheme is withheld under General Tax Code Article 182 A on the 0/12/20 bands, or 0/8/14.4 for overseas-source income, not under the ordinary withholding at source. Source: FR-CCG-001 Module 6; NEODeS CT2026.1.2 S21.G00.30.022. |
|  | France |  | Contract End Date |  | Date de fin du contrat | The actual date on which the employment contract ends. For a contract with a notice period it is the end of the notice, whether or not the notice was worked. | CM | Mandatory once the contract has ended. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Termination. Norm reference: NEODeS CT2026.1.2 S21.G00.62.001. |
|  | France |  | Contract Termination Reason |  | Motif de la rupture du contrat | The ground on which the contract ended. It governs the severance entitlement, the end-of-contract indemnity, the employer's unemployment-insurance position and, for a mutually agreed termination, the 40% employer contribution. | CM | Mandatory once the contract has ended. | Text | 3-character code | Contract Termination Reason |  |  |  |  |  |  |  |  |  |  | Termination. The employer contribution on a mutually agreed termination is 40% for 2026, up from 30%, under the Social Security Financing Act for 2026. Source: FR-CCG-001 Module 9; NEODeS CT2026.1.2 S21.G00.62.002. |
|  | France |  | Termination Notification Date |  | Date de notification de la rupture de contrat | The date on which the termination was notified to the employee. It is the date from which the notice period runs. | CM | Mandatory for a termination requiring notification - dismissal, resignation, retirement. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Termination. Norm reference: NEODeS CT2026.1.2 S21.G00.62.003. |
|  | France |  | Mutually-Agreed Termination Signature Date |  | Date de signature de la convention de rupture | The date on which the parties signed the mutually agreed termination agreement. It starts the statutory reflection period and the administrative approval timetable. | CM | Mandatory where the termination reason is a mutually agreed termination. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Termination. Norm reference: NEODeS CT2026.1.2 S21.G00.62.004. |
|  | France |  | Dismissal Procedure Start Date |  | Date d'engagement de la procédure de licenciement | The date on which the dismissal procedure was started, that is, the date of the letter calling the employee to the preliminary interview. | CM | Mandatory where the termination reason is a dismissal. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Termination. Norm reference: NEODeS CT2026.1.2 S21.G00.62.005. |
|  | France |  | Last Day Worked and Paid at the Usual Salary |  | Dernier jour travaillé et payé au salaire habituel | The last day for which the employee was paid at the usual rate. It is the reference date France Travail uses to compute the unemployment entitlement and it is not necessarily the contract end date. | CM | Mandatory once the contract has ended. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Termination. Norm reference: NEODeS CT2026.1.2 S21.G00.62.006. |
|  | France |  | Notice Performance and Payment Type |  | Type de réalisation et de paiement du préavis | Whether the notice was worked and paid, not worked but paid, or neither worked nor paid, and under which arrangement. | CM | Mandatory where the contract carried a notice period. | Text | 2-character code | Notice Performance and Payment Type |  |  |  |  |  |  |  |  |  |  | Termination. Norm reference: NEODeS CT2026.1.2 S21.G00.63.001. |
|  | France |  | Notice Start Date |  | Date de début de préavis | The date on which the notice period begins. | CM | Mandatory where the contract carried a notice period. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Termination. Norm reference: NEODeS CT2026.1.2 S21.G00.63.002. |
|  | France |  | Notice End Date |  | Date de fin de préavis | The date on which the notice period ends. | CM | Mandatory where the contract carried a notice period. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Termination. Norm reference: NEODeS CT2026.1.2 S21.G00.63.003. |
|  | France |  | Settlement Negotiation in Progress |  | Transaction en cours | Indicates that a settlement is being negotiated with the departing employee. It signals to France Travail that the final position may be amended. | CM | Mandatory in the end-of-contract signal. | Text | 2-character code | Settlement Negotiation in Progress |  |  |  |  |  |  |  |  |  |  | Termination. Norm reference: NEODeS CT2026.1.2 S21.G00.62.008. |
|  | France |  | Special Employee Status at Termination |  | Statut particulier du salarié | The corporate office or special capacity the departing employee held, where they held one: manager, director, chair, member of the management or supervisory board, association officer, shareholder, or umbrella-company employee. It affects the unemployment-insurance entitlement. | CM | Mandatory where the departing employee held a corporate office or one of the listed special capacities. | Text | 2-character code | Special Employee Status at Termination |  |  |  |  |  |  |  |  |  |  | Termination. Company officers treated as employees pay full contributions except unemployment insurance and the wage guarantee scheme, which is precisely why this field changes the France Travail outcome. Source: FR-CCG-001 Module 9; scope_manifest.json employment_types.in_scope; NEODeS CT2026.1.2 S21.G00.62.014. |
|  | France |  | Continuation of Collective Cover Membership |  | Maintien de l'affiliation du salarié au contrat collectif | Indicates that the departing employee's membership of the collective health and death-and-disability cover continues after the contract ends, under the portability rules. | CM | Mandatory where the employee's collective cover continues after the contract ends. | Text | 2-character code | Continuation of Collective Cover Membership |  |  |  |  |  |  |  |  |  |  | Termination. Norm reference: NEODeS CT2026.1.2 S21.G00.62.016. |
|  | France |  | Refusal of a Permanent Contract after a Fixed-Term or Agency Contract |  | Refus de la proposition d'un CDI suite à CDD ou contrat de mission | Indicates that the employee refused an offer of a permanent contract made at the end of a fixed-term contract or agency assignment. The refusal must be declared and it affects the unemployment entitlement. | CM | Mandatory where a permanent contract was offered at the end of a fixed-term contract or agency assignment and refused. | Text | 2-character code | Refusal of a Permanent Contract after a Fixed-Term or Agency Contract |  |  |  |  |  |  |  |  |  |  | Termination. Norm reference: NEODeS CT2026.1.2 S21.G00.62.021. |
|  | France |  | Employer Legal Name |  | Raison sociale de l'employeur | The registered name of the legal entity, or the surname and first names where the employer is a natural person. It is a mandatory mention on the pre-employment declaration and on the industrial-accident declaration. | M |  | Text | Free text |  |  |  |  |  |  |  |  |  |  |  | Employer information. Legal basis: Labour Code Article R1221-1, 1° (a). Source: FR-URSSAF-001 DPAE; FR-CPAM-002 form S6200. |
|  | France |  | Employer Legal Nature |  | Nature juridique de l'employeur | Whether the employer is a private body, a public body, or a private establishment with a majority public shareholding. It determines which declaration channel and which contribution set apply. | M |  | Text | 2-character code | Employer Legal Nature |  |  |  |  |  |  |  |  |  |  | Employer information. Norm reference: NEODeS CT2026.1.2 S21.G00.11.017. |
|  | France |  | Legal Entity Location |  | Implantation de l'entreprise | Whether the employer is a foreign entity with or without an establishment in France, and if without, whether it is established inside or outside the European Union. A foreign employer without an establishment in France registers with the dedicated URSSAF service for foreign firms and is subject to specific arrangements. | CM | Mandatory where the legal entity is registered outside France. | Text | 2-character code | Legal Entity Location |  |  |  |  |  |  |  |  |  |  | Employer information. Norm reference: NEODeS CT2026.1.2 S21.G00.06.012. |
|  | France |  | Employer Telephone Number |  | Numéro de téléphone de l'employeur | The employer's telephone number, required on the industrial-accident declaration. | CM | Mandatory where an industrial-accident or occupational-disease declaration is raised. | Text | Free text, international format accepted |  |  |  |  |  |  |  |  |  |  |  | Employer information. Source: FR-CPAM-002 form S6200. |
|  | France |  | Entity Address - Street |  | Numéro, extension, nature et libellé de la voie (entreprise) | The street element of the legal entity's registered address. | M |  | Text | 1 to 50 characters |  |  |  |  |  |  |  |  |  |  |  | Employer information. Norm reference: NEODeS CT2026.1.2 S21.G00.06.004. |
|  | France |  | Entity Address - Delivery Service Complement |  | Service de distribution, complément de localisation de la voie (entreprise) | The second address line of the legal entity's registered address. | CM | Mandatory where the address requires a delivery complement. | Text | 1 to 50 characters |  |  |  |  |  |  |  |  |  |  |  | Employer information. Norm reference: NEODeS CT2026.1.2 S21.G00.06.008. |
|  | France |  | Entity Address - Building Complement |  | Complément de la localisation de la construction (entreprise) | The address line locating the premises within the building, for the legal entity's registered address. | CM | Mandatory where the address requires a building complement. | Text | 1 to 50 characters |  |  |  |  |  |  |  |  |  |  |  | Employer information. Norm reference: NEODeS CT2026.1.2 S21.G00.06.007. |
|  | France |  | Entity Address - Postal Code |  | Code postal (entreprise) | The postal code of the legal entity's registered address. | CM | Mandatory for an address in France. | Text | 5 digits, validated against the La Poste Hexaposte referential |  |  |  |  |  |  |  |  |  |  |  | Employer information. Norm reference: NEODeS CT2026.1.2 S21.G00.06.005. |
|  | France |  | Entity Address - Town |  | Localité (entreprise) | The town of the legal entity's registered address. | M |  | Text | 1 to 50 characters, letters, digits and spaces only |  |  |  |  |  |  |  |  |  |  |  | Employer information. Norm reference: NEODeS CT2026.1.2 S21.G00.06.006. |
|  | France |  | Entity Address - Country Code |  | Code pays (entreprise) | The ISO 3166-1 alpha-2 code of the country of the legal entity's registered address, where that address is outside France. | CM | Mandatory where the registered address is outside France. | Text | 2 letters, ISO 3166-1 alpha-2 (see the Country Codes sheet) |  |  |  |  |  |  |  |  |  |  |  | Employer information. Norm reference: NEODeS CT2026.1.2 S21.G00.06.010. |
|  | France |  | Entity Address - Foreign Distribution Code |  | Code de distribution à l'étranger (entreprise) | The foreign postal routing element for the legal entity's registered address, where that address is outside France. | CM | Mandatory where the registered address is outside France. | Text | 1 to 50 characters |  |  |  |  |  |  |  |  |  |  |  | Employer information. Norm reference: NEODeS CT2026.1.2 S21.G00.06.011. |
|  | France |  | Establishment Address - Street |  | Numéro, extension, nature et libellé de la voie (établissement) | The street element of the employing establishment's address. | M |  | Text | 1 to 50 characters |  |  |  |  |  |  |  |  |  |  |  | Establishment information. Legal basis for the pre-employment declaration use: Labour Code Article R1221-1, 1° (c). Norm reference: NEODeS CT2026.1.2 S21.G00.11.003. |
|  | France |  | Establishment Address - Delivery Service Complement |  | Service de distribution, complément de localisation de la voie (établissement) | The second address line of the employing establishment's address. | CM | Mandatory where the address requires a delivery complement. | Text | 1 to 50 characters |  |  |  |  |  |  |  |  |  |  |  | Establishment information. Norm reference: NEODeS CT2026.1.2 S21.G00.11.007. |
|  | France |  | Establishment Address - Building Complement |  | Complément de la localisation de la construction (établissement) | The address line locating the premises within the building, for the employing establishment. | CM | Mandatory where the address requires a building complement. | Text | 1 to 50 characters |  |  |  |  |  |  |  |  |  |  |  | Establishment information. Norm reference: NEODeS CT2026.1.2 S21.G00.11.006. |
|  | France |  | Establishment Address - Postal Code |  | Code postal (établissement) | The postal code of the employing establishment's address. | M |  | Text | 5 digits, validated against the La Poste Hexaposte referential |  |  |  |  |  |  |  |  |  |  |  | Establishment information. Norm reference: NEODeS CT2026.1.2 S21.G00.11.004. |
|  | France |  | Establishment Address - Town |  | Localité (établissement) | The town of the employing establishment's address. | M |  | Text | 1 to 50 characters, letters, digits and spaces only |  |  |  |  |  |  |  |  |  |  |  | Establishment information. Norm reference: NEODeS CT2026.1.2 S21.G00.11.005. |
|  | France |  | Establishment Address - Country Code |  | Code pays (établissement) | The ISO 3166-1 alpha-2 code of the country of the establishment's address, where it is outside France. | CM | Mandatory where the establishment's address is outside France. | Text | 2 letters, ISO 3166-1 alpha-2 (see the Country Codes sheet) |  |  |  |  |  |  |  |  |  |  |  | Establishment information. Norm reference: NEODeS CT2026.1.2 S21.G00.11.015. |
|  | France |  | Establishment Address - Foreign Distribution Code |  | Code de distribution à l'étranger (établissement) | The foreign postal routing element for the establishment's address, where it is outside France. | CM | Mandatory where the establishment's address is outside France. | Text | 1 to 50 characters |  |  |  |  |  |  |  |  |  |  |  | Establishment information. Norm reference: NEODeS CT2026.1.2 S21.G00.11.016. |
|  | France |  | TESE / CEA Scheme Joining Date |  | Date d'effet de l'adhésion au dispositif TESE/CEA | The date from which the establishment joined the simplified employment scheme for very small firms - the titre emploi service entreprise or the chèque emploi associatif. | CM | Mandatory where the establishment has joined the TESE or CEA scheme. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Establishment information. Norm reference: NEODeS CT2026.1.2 S21.G00.11.019. |
|  | France |  | TESE / CEA Scheme Exit Date |  | Date d'effet de la sortie du dispositif TESE/CEA | The date from which the establishment left the simplified employment scheme. | CM | Mandatory where the establishment has left the TESE or CEA scheme. | Date | DD/MM/YYYY |  |  |  |  |  |  |  |  |  |  |  | Establishment information. Norm reference: NEODeS CT2026.1.2 S21.G00.11.020. |
|  | France |  | Basis of Unemployment-Insurance Pay for Expatriates |  | Type de rémunération soumise à contributions d'Assurance chômage pour expatriés | Whether unemployment-insurance contributions for expatriate employees are assessed on their actual pay or on a comparison salary. | CM | Mandatory where the establishment employs expatriates covered by the French unemployment insurance scheme. | Text | 2-character code | Basis of Unemployment-Insurance Pay for Expatriates |  |  |  |  |  |  |  |  |  |  | Establishment information. Norm reference: NEODeS CT2026.1.2 S21.G00.11.009. |
|  | France |  | Place of Work - Identifier |  | Identifiant du lieu de travail | The identifier of a site of work declared separately from the employing establishment, normally its SIRET. | CM | Mandatory where employees work at a site other than the employing establishment. | Text | 2 to 14 characters; normally a 14-digit SIRET |  |  |  |  |  |  |  |  |  |  |  | Place of work. Norm reference: NEODeS CT2026.1.2 S21.G00.85.001. |
|  | France |  | Place of Work - Legal Nature |  | Nature juridique du lieu de travail | Whether the site is an establishment, another kind of site, or home working. | CM | Mandatory where a place of work is declared separately from the employing establishment. | Text | 2-character code | Place of Work Legal Nature |  |  |  |  |  |  |  |  |  |  | Place of work. Norm reference: NEODeS CT2026.1.2 S21.G00.85.010. |
|  | France |  | Place of Work - Activity Code (APET) |  | Code APET du lieu de travail | The NAF activity code of the site of work, where it differs from that of the employing establishment. | CM | Mandatory where a place of work is declared separately and its activity differs from that of the employing establishment. | Text | 4 digits + 1 letter, for example 6201Z |  |  |  |  |  |  |  |  |  |  |  | Place of work. Norm reference: NEODeS CT2026.1.2 S21.G00.85.002. |
|  | France |  | Place of Work - INSEE Municipality Code |  | Code INSEE commune du lieu de travail | The five-character INSEE code of the commune in which the site of work is situated. | CM | Mandatory where a place of work is declared separately from the employing establishment. | Text | 5 characters, from the DSN INSEE commune referential |  |  |  |  |  |  |  |  |  |  |  | Place of work. This is the field on which the mobility levy rate turns: the levy is set by the transport authority of the commune, so an employee working in a different commune from the employing establishment may attract a different rate. Source: FR-CCG-001 Module 2.1; NEODeS CT2026.1.2 S21.G00.85.011. |
|  | France |  | Place of Work - Address Street |  | Numéro, extension, nature et libellé de la voie (lieu de travail) | The street element of the site of work's address. | CM | Mandatory where a place of work is declared separately from the employing establishment. | Text | 1 to 50 characters |  |  |  |  |  |  |  |  |  |  |  | Place of work. Norm reference: NEODeS CT2026.1.2 S21.G00.85.003. |
|  | France |  | Place of Work - Address Postal Code |  | Code postal (lieu de travail) | The postal code of the site of work's address. | CM | Mandatory where a place of work is declared separately from the employing establishment. | Text | 5 digits, validated against the La Poste Hexaposte referential |  |  |  |  |  |  |  |  |  |  |  | Place of work. Norm reference: NEODeS CT2026.1.2 S21.G00.85.004. |
|  | France |  | Place of Work - Address Town |  | Localité (lieu de travail) | The town of the site of work's address. | CM | Mandatory where a place of work is declared separately from the employing establishment. | Text | 1 to 50 characters, letters, digits and spaces only |  |  |  |  |  |  |  |  |  |  |  | Place of work. Norm reference: NEODeS CT2026.1.2 S21.G00.85.005. |
|  | France |  | Occupational Health Service Name and Address |  | Nom et adresse du service de santé au travail | The name and postal address of the occupational prevention and health service to which the establishment is affiliated. Both are required in full on the industrial-accident declaration. | CM | Mandatory where an industrial-accident or occupational-disease declaration is raised. | Text | Free text: name, address and postcode |  |  |  |  |  |  |  |  |  |  |  | Establishment information. Held in addition to the SPST identifier on the ID Information sheet, because the accident declaration form requires the name and address in full and not the identifier. Source: FR-CPAM-002 form S6200. |
|  | France |  | Subrogation Policy |  | Politique de subrogation | Whether the employer elects to receive the social security daily allowances directly during a sick leave, paying the employee their full salary and being reimbursed by the fund, or lets the fund pay the employee directly. | M |  | Text | 2-character code | Subrogation |  |  |  |  |  |  |  |  |  |  | Filing configuration. This is a standing employer election that drives the payslip and the DSN work-stoppage signal for every absence, so it belongs to master data even though it is declared per stoppage. The daily allowances themselves and the individual stoppage dates are per-payrun transactional data and are out of Data Dictionary scope. Norm reference: NEODeS CT2026.1.2 S21.G00.60.004. |
|  | France |  | Employer Bank Account IBAN |  | IBAN de l'employeur | The employer's bank account into which social security daily allowances are paid under subrogation, and into which the state agency pays employment aids. | CM | Mandatory where the employer operates subrogation, or where it receives employment aids paid by the state agency. | Text | 15 to 34 characters; a French IBAN is 27 characters |  |  |  |  |  |  |  |  |  |  |  | Filing configuration. Norm reference: NEODeS CT2026.1.2 S21.G00.60.007 and S21.G00.12.003. |
|  | France |  | Employer Bank Identifier Code (BIC) |  | BIC de l'employeur | The bank identifier code of the institution holding the employer's account named above. | CM | Mandatory where the employer's IBAN is supplied and the payment channel requires the BIC. | Text | 8 or 11 characters |  |  |  |  |  |  |  |  |  |  |  | Filing configuration. Norm reference: NEODeS CT2026.1.2 S21.G00.60.008 and S21.G00.12.002. |
|  | France |  | Employer Bank Account Usage Type |  | Type d'usage du compte bancaire employeur | The purpose for which the employer's bank account is declared in the DSN. | CM | Mandatory where an employer bank account is declared for the payment of state agency employment aids. | Text | 2-character code | Employer Bank Account Usage Type |  |  |  |  |  |  |  |  |  |  | Filing configuration. Norm reference: NEODeS CT2026.1.2 S21.G00.12.001. |
|  | France |  | Contribution Payment Method |  | Mode de paiement des cotisations | The channel by which the employer settles the contributions declared in the DSN: bank transfer, SEPA direct debit, cheque, interbank payment order, or payment made by another establishment. | M |  | Text | 2-character code | Contribution Payment Method |  |  |  |  |  |  |  |  |  |  | Filing configuration. France consolidates: social security contributions and the income tax withheld at source travel in the same DSN file but are settled through separate payment orders to URSSAF and to DGFiP. Source: FR-CCG-001 Module 10; NEODeS CT2026.1.2 S21.G00.20.010. |
|  | France |  | Declared Contact - Type |  | Type de contact déclaré | The purpose for which a contact is declared to the collecting bodies: daily allowances, end-of-contract matters, statistical bodies, contribution recovery, employee or establishment identification, disabled-worker follow-up, paid-leave funds, vocational training. | M |  | Text | 2-character code | Declared Contact Type |  |  |  |  |  |  |  |  |  |  | Filing configuration. At least one contact must be declared; several are usual, because the bodies route different queries to different types. Norm reference: NEODeS CT2026.1.2 S20.G00.07.004. |
|  | France |  | Declared Contact - Name |  | Nom et prénom du contact déclaré | The surname and first name of the person declared as contact for the purpose stated above. | M |  | Text | Free text |  |  |  |  |  |  |  |  |  |  |  | Filing configuration. Norm reference: NEODeS CT2026.1.2 S20.G00.07.001. |
|  | France |  | Declared Contact - E-mail Address |  | Adresse mél du contact déclaré | The electronic mail address of the declared contact, to which the collecting bodies address queries and anomaly notifications. | M |  | Text | 6 to 100 characters, valid e-mail format |  |  |  |  |  |  |  |  |  |  |  | Filing configuration. This address is where the DSN return-flow anomalies land, so an out-of-date value here means anomalies go unread for months. Norm reference: NEODeS CT2026.1.2 S20.G00.07.003. |
|  | France |  | Declared Contact - Telephone Number |  | Numéro de téléphone du contact déclaré | The telephone number of the declared contact. | CM | Mandatory where the collecting body requires a telephone contact for the declared contact type. | Text | Free text, international format accepted |  |  |  |  |  |  |  |  |  |  |  | Filing configuration. Norm reference: NEODeS CT2026.1.2 S20.G00.07.002. |
|  | France |  | Tax Liability Code |  | Code taxe (assujettissement fiscal) | The employer's liability or non-liability to each of the payroll-borne taxes declared through the DSN: the apprenticeship tax and its supplementary contribution, the construction-effort contribution, the vocational training contribution, the fixed-term contract personal training account contribution, and the payroll tax. | M |  | Text | 3-character code; one occurrence per tax | Tax Liability Code |  |  |  |  |  |  |  |  |  |  | Filing configuration. Both liability and non-liability are declared explicitly: silence is not a valid answer, and the codes come in matched pairs so that the collecting body can distinguish a genuine exemption from an omission. Norm reference: NEODeS CT2026.1.2 S21.G00.44.001. |
|  | France |  | Apprenticeship Tax Exemption Reason |  | Motif de non-assujettissement à la taxe d'apprentissage | The ground on which the employer is not liable to the apprenticeship tax. | CM | Mandatory where the employer declares non-liability to the apprenticeship tax. | Text | 3 characters, from the DSN external referential MNATA |  |  |  |  |  |  |  |  |  |  |  | Filing configuration. Source: FR-URSSAF-004 Solde de la taxe d'apprentissage; NEODeS CT2026.1.2 S21.G00.44.004. |
|  | France |  | External Disabled-Worker Beneficiary Type |  | Type BOETH externe | The category of disabled-worker beneficiary made available to the establishment by a third party and counted towards the employment obligation: agency worker, employee of an employer grouping, unnamed trainee, employee of an intermediate association, model agency employee, or employee of a shared part-time employment company. | CM | Mandatory where the establishment counts externally supplied disabled-worker beneficiaries towards its employment obligation. | Text | 2-character code | External Disabled-Worker Beneficiary Type |  |  |  |  |  |  |  |  |  |  | Filing configuration. Source: FR-URSSAF-003 DOETH; NEODeS CT2026.1.2 S21.G00.13.002. |
|  | France |  | Collective Cover - Covered Population |  | Personnel couvert | Whether the collective death-and-disability or health contract covers at least one employee of the establishment to which it is attached. | M |  | Text | 2-character code | Collective Cover - Covered Population |  |  |  |  |  |  |  |  |  |  | Filing configuration. Norm reference: NEODeS CT2026.1.2 S21.G00.15.004. |

## Sheet: `Country Option Mappers`

_413 rows x 7 columns._

**Country Option Mappers**

| col1 | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|---|---|---|---|---|---|---|
|  | Personal Identifier Type | NIR | Social security number | Numéro d'inscription au répertoire (NIR) | The definitive social security number: 13 significant digits plus a 2-digit key, key = 97 minus (the 13-digit number modulo 97). Corsican birth departments 2A and 2B are converted before the key is computed. | Exactly one of the two identifiers must be present on every contract. The NIR is the target state; the NTT is provisional and must be replaced as soon as the NIR is issued. A contract left on an NTT beyond a few months produces a recurring DSN anomaly. No third identifier is permitted: the employer does not capture the employee's tax reference number. Constraint - Employee Social Security Number (NIR) is Conditional Mandatory: Mandatory as soon as the NIR is known. Where it is not yet known - typically a newly arrived foreign national - the Temporary Technical Number (NTT) must be supplied instead, and must be replaced by the NIR as soon as the NIR is issued. Constraint - Temporary Technical Number (NTT) is Conditional Mandatory: Mandatory where the employee has no NIR yet. Must be cleared once the NIR is captured. Source: FR-CCG-001 Module 2.2; scope_manifest.json option_mapper_scope.personal_id_type |
|  |  | NTT | Temporary technical number | Numéro technique temporaire (NTT) | The provisional identifier used until the NIR is issued: up to 40 characters, conventionally the SIRET plus an internal sequence. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Sex | 01 | Male | masculin | Male. | Must agree with the first digit of the NIR, which is 1 for male and 2 for female. A disagreement between this field and the NIR is rejected by the identification check run on the DSN. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.30.005 |
|  |  | 02 | Female | féminin | Female. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Nationality Band | FR | French | Française | French national. | Conditional: required only where an industrial-accident or occupational-disease declaration is raised for the employee. The form asks for the band, not the individual nationality; collecting a finer value would exceed what any French payroll filing requires. Constraint - Nationality Band is Conditional Mandatory: Mandatory where an industrial-accident or occupational-disease declaration is raised for the employee. Source: FR-CPAM-002 Déclaration d'accident du travail, form S6200 (Cerfa 14463) |
|  |  | EEE | EEA or Swiss | EEE ou Suisse | National of another state of the European Economic Area, or of Switzerland. |  |
|  |  | AUT | Other | Autre | National of any other state. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Cross-Border Status (EU Coding) | 01 | France | France | Resident in France. | A residence-based classification used by the collecting bodies for coordination and statistics. It is independent of both tax residence and social security affiliation and must not be used as a proxy for either. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.30.013 |
|  |  | 02 | European Union | UE | Resident in another member state of the European Union. |  |
|  |  | 03 | European Economic Area | EEE | Resident in another state of the European Economic Area outside the European Union. |  |
|  |  | 04 | Rest of the world | Reste du Monde | Resident outside the European Economic Area. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Foreign Status for Tax Purposes | 01 | Frontier work | travail frontalier | The employee is a frontier worker, living in one state and working in another and returning at least weekly. | Conditional: transmitted only where one of the two situations applies. It is a tax classification and is independent of the social security Worker Abroad Status mapper; an employee may be in one without being in the other. Constraint - Foreign Status for Tax Purposes is Conditional Mandatory: Mandatory where the employee is a frontier worker or works abroad. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.30.022 |
|  |  | 02 | Work abroad | travail à l’étranger | The employee performs their work outside France. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Combined Employment and Retirement | 01 | No | Non | The employee is not combining employment with a liquidated retirement pension. | Conditional: declared where the employee has liquidated a retirement pension and works under a contract of employment. Working pensioners under a contract of employment are in scope for this build. Old-age contributions remain due; where the pension was liquidated at the full rate they generate no further entitlement. Constraint - Combined Employment and Retirement is Conditional Mandatory: Mandatory where the employee has liquidated a retirement pension and continues or resumes work under a contract of employment. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.30.023 |
|  |  | 03 | Yes | Oui | The employee is combining employment with a liquidated retirement pension. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Highest Level of Education Attained | 01 | Compulsory schooling only | Formation n'allant pas au-delà de la scolarité obligatoire (16 ans) | Education not going beyond compulsory schooling, to age 16. | Conditional: collected only for an employee on an apprenticeship or professionalisation contract, where it is a condition of the training funding. It must not be requested from every employee. Constraint - Highest Level of Education Attained is Conditional Mandatory: Mandatory for an employee on an apprenticeship or professionalisation contract, where it is a condition of the training funding. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.30.024 |
|  |  | 02 | Up to one year after lower secondary | Formation d'une durée maximale d'un an après le collège | Education of at most one year after lower secondary school. |  |
|  |  | 03 | Vocational certificate level | Niveau de formation équivalent au CAP (certificat d'aptitude professionnelle) ou au BEP (brevet d'études professionnelles) | Education at the level of the vocational aptitude certificate (CAP) or the vocational studies certificate (BEP). |  |
|  |  | 04 | Upper secondary level | Formation de niveau du bac (général, technologique ou professionnel), du brevet de technicien (BT) ou du brevet professionnel | Education at upper secondary level: the general, technological or vocational baccalaureate, the technician's certificate or the vocational certificate. |  |
|  |  | 05 | Two years of higher education | Formation de niveau bac+2 : licence 2, BTS (brevet de technicien supérieur), DUT (diplôme universitaire de technologie), etc. | Two years of higher education: second-year degree, higher technician's certificate (BTS), university technology diploma (DUT). |  |
|  |  | 06 | Three or four years of higher education | Formation de niveau bac+3 et bac+4 : licence 3, licence professionnelle, master 1, etc. | Three or four years of higher education: third-year degree, vocational degree, first-year master's. |  |
|  |  | 07 | Five years of higher education | Formation de niveau bac+5 : master 2, diplôme d'études approfondies, diplôme d'études supérieures spécialisées, diplôme d'ingénieur, etc. | Five years of higher education: second-year master's, advanced studies diploma, engineering diploma. |  |
|  |  | 08 | Doctorate | Formation de niveau bac+8 : doctorat, habilitation à diriger des recherches, etc. | Eight years of higher education: doctorate, accreditation to supervise research. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Level of Qualification Being Prepared | 03 | Vocational certificate level | Niveau de formation équivalent au CAP (certificat d'aptitude professionnelle) ou au BEP (brevet d'études professionnelles) | Qualification at the level of the vocational aptitude certificate (CAP) or the vocational studies certificate (BEP). | Conditional: mandatory for an employee on an apprenticeship or professionalisation contract. The scale is the same as for the highest level attained, but it starts at the vocational certificate level because no work-study qualification sits below it. Constraint - Level of Qualification Being Prepared is Conditional Mandatory: Mandatory for an employee on an apprenticeship or professionalisation contract. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.30.025 |
|  |  | 04 | Upper secondary level | Formation de niveau du bac (général, technologique ou professionnel), du brevet de technicien (BT) ou du brevet professionnel | Qualification at upper secondary level: the general, technological or vocational baccalaureate, the technician's certificate or the vocational certificate. |  |
|  |  | 05 | Two years of higher education | Formation de niveau bac+2 : licence 2, BTS (brevet de technicien supérieur), DUT (diplôme universitaire de technologie), etc. | Two years of higher education: second-year degree, higher technician's certificate (BTS), university technology diploma (DUT). |  |
|  |  | 06 | Three or four years of higher education | Formation de niveau bac+3 et bac+4 : licence 3, licence professionnelle, master 1, etc. | Three or four years of higher education: third-year degree, vocational degree, first-year master's. |  |
|  |  | 07 | Five years of higher education | Formation de niveau bac+5 : master 2, diplôme d'études approfondies, diplôme d'études supérieures spécialisées, diplôme d'ingénieur, etc. | Five years of higher education: second-year master's, advanced studies diploma, engineering diploma. |  |
|  |  | 08 | Doctorate | Formation de niveau bac+8 : doctorat, habilitation à diriger des recherches, etc. | Eight years of higher education: doctorate, accreditation to supervise research. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Contract Nature | 01 | Permanent contract (CDI) | Contrat de travail à durée indéterminée de droit privé | Private-law contract of indefinite duration - the ordinary permanent employment contract. | PRIVATE-SECTOR FILTER APPLIED. Excluded from the norm's full list: public-law permanent and fixed-term contracts (09, 10), public-service secondments and appointments (20, 21, 50, 52), occasional public-service collaborator assignments (51), penitentiary employment (53, 54), work-support contracts in sheltered establishments (70), elected-office mandates (81), civic-service volunteering (89), and maritime engagement contracts and lines of service (91, 92, 93), the last group being descoped with the ENIM scheme. Also excluded, and named here so that no code of the norm's list is dropped silently: the business-project support contract (32, contrat d'appui au projet d'entreprise), because its beneficiary is not an employee under a contract of employment - Commercial Code art. L127-1 - and therefore falls outside the perimeter of this build; and the educational engagement contract (60, contrat d'engagement educatif, Social Action and Families Code arts. L432-1 to L432-6), which IS a private-law contract under the regime general but is not one of the six contract types carried in scope_manifest.json option_mapper_scope.contract_type. Code 60 is therefore a SCOPE OWNER DECISION, not a technical exclusion: if the owner rules it in, it is added here with its verbatim norm label. Apprenticeship and professionalisation contracts are NOT values of this list: they are carried by the Public-Policy or Collectively Agreed Scheme mapper on top of a permanent or fixed-term contract nature. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.007 |
|  |  | 02 | Fixed-term contract (CDD) | Contrat de travail à durée déterminée de droit privé | Private-law contract of definite duration. Requires a statutory reason, carried by the Reason for Using a Fixed-Term or Agency Contract mapper. |  |
|  |  | 03 | Temporary-agency assignment | Contrat  de mission (contrat de travail temporaire) | Assignment contract under a temporary work arrangement. In scope where the client is the agency and is therefore the employer. |  |
|  |  | 07 | Intermittent permanent contract | Contrat à durée indéterminée intermittent | Permanent contract with alternating worked and unworked periods, available only where a collective agreement provides for it. |  |
|  |  | 08 | Permanent agency contract | Contrat à durée indéterminée intérimaire | Permanent contract concluded by a temporary work agency with an agency worker, who is then assigned to successive user firms. |  |
|  |  | 29 | Internship agreement | Convention de stage (hors formation professionnelle) | Internship agreement outside vocational training. The gratuity is not a wage and is exempt from contributions up to 15% of the hourly ceiling per hour of attendance. |  |
|  |  | 80 | Corporate officer's mandate | Mandat social | Corporate office held by a company officer treated as an employee: chair or managing director of a SAS or SA, minority or equal-shareholding manager of a SARL. Full contributions apply except unemployment insurance and the wage guarantee scheme. |  |
|  |  | 82 | Project or operation permanent contract | Contrat de travail à durée indéterminée de Chantier ou d'opération | Permanent contract for the duration of a defined site or operation, ending when the operation ends. |  |
|  |  | 90 | Other contract, agreement or mandate | Autre nature de contrat, convention, mandat (hors mandat social) | Any other nature of contract, agreement or mandate outside a corporate officer's mandate. Use only where no more specific value fits, and record the reason. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Public-Policy or Collectively Agreed Scheme | 21 | Employment initiative contract (CUI-CIE) | CUI - Contrat Initiative Emploi | Subsidised employment initiative contract under the single integration contract. | PRIVATE-SECTOR FILTER APPLIED. Public-sector apprenticeship under the 1992 Act (81) is excluded, as is the generation contract (80, contrat de generation), a closed historic scheme abolished by Ordonnance n. 2017-1387 of 22 September 2017 and incapable of applying to a 2026 period - excluded on the same ground as the 2004 phased-retirement value in the Working-Time Arrangement mapper. This field, not the contract nature, is what identifies an apprentice or a professionalisation contract and therefore what drives the corresponding exemptions and contribution treatment. The value 99 must be supplied where no scheme applies; leaving the field empty is not equivalent. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.008 |
|  |  | 41 | Skills pathway (PEC / CUI-CAE) | Parcours Emploi Compétences / CUI - CAE | Skills and employment pathway, formerly the employment support contract under the single integration contract. |  |
|  |  | 42 | Overseas access-to-employment contract | CUI - Contrat d'accès à l'emploi - DOM | Access-to-employment contract under the single integration contract, in the overseas departments. |  |
|  |  | 61 | Professionalisation contract | Contrat de Professionnalisation | Work-study contract combining employment with a vocational qualification. In scope for this build. |  |
|  |  | 64 | Apprenticeship - craft or small firm | Contrat d'apprentissage entreprises artisanales ou de moins de 11 salariés (loi du 3 janvier 1979) | Apprenticeship contract in a craft firm or a firm with fewer than 11 employees, under the Act of 3 January 1979. |  |
|  |  | 65 | Apprenticeship - firm of 11 or more | Contrat d’apprentissage entreprises non inscrites au répertoire des métiers d’au moins 11 salariés (loi de 1987) | Apprenticeship contract in a firm of at least 11 employees not entered in the trades register, under the 1987 Act. |  |
|  |  | 66 | Industrial research training agreement (CIFRE) | Convention industrielle de formation par la recherche en entreprise (CIFRE) | Industrial agreement for training through research in a firm. |  |
|  |  | 70 | Fixed-term contract for older workers | Contrat à durée déterminée pour les séniors | Fixed-term contract for senior employees. |  |
|  |  | 71 | Integration fixed-term contract | Contrat à durée déterminée d’insertion | Fixed-term contract for occupational integration. |  |
|  |  | 83 | Experience valorisation contract | Contrat de valorisation de l’expérience | Contract for the valorisation of occupational experience. |  |
|  |  | 92 | Vocational training placement | Stage de la formation professionnelle | Placement forming part of vocational training. |  |
|  |  | 93 | Workplace immersion period | Période de mise en situation en milieu professionnel | Period of immersion in a working environment. |  |
|  |  | 94 | Adult mediator contract | Contrat adulte relais | Adult mediator contract. |  |
|  |  | 99 | Not concerned | Non concerné | No public-policy or collectively agreed scheme applies to this contract. This is the ordinary value for a standard employment contract. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Reason for Using a Fixed-Term or Agency Contract | 01 | Replacement of an employee | Remplacement d'un salarié | Replacement of an absent employee, or of an employee whose contract is suspended. | Conditional: mandatory for a fixed-term contract or a temporary-agency assignment, not applicable to a permanent contract. PRIVATE-SECTOR FILTER APPLIED: the replacement of the head of an agricultural holding (08) is excluded with the MSA scheme. The reason is not administrative colour - a seasonal contract (03) and a contract of customary use (05) carry no 10% end-of-contract indemnity, whereas a replacement (01) or an activity-increase contract (02) does. Constraint - Reason for Using a Fixed-Term or Agency Contract is Conditional Mandatory: Mandatory for a fixed-term contract or a temporary-agency assignment. Not applicable to a permanent contract. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.021 |
|  |  | 02 | Temporary increase in activity | Accroissement temporaire de l'activité de l'entreprise | Temporary increase in the firm's activity. |  |
|  |  | 03 | Seasonal employment | Emplois à caractère saisonnier | Seasonal work. No end-of-contract indemnity is due. |  |
|  |  | 04 | Grape-harvest contract | Contrat vendanges | Grape-harvest contract. |  |
|  |  | 05 | Contract of customary use | Contrat d’usage | Contract of customary use in a sector where fixed-term contracts are customary and permanent contracts are not used. No end-of-contract indemnity is due. |  |
|  |  | 06 | Fixed-purpose fixed-term contract | Contrat à durée déterminée à objet défini | Fixed-term contract for a defined purpose, concluded with an engineer or manager for a project of 18 to 36 months. |  |
|  |  | 07 | Replacement of a business head | Remplacement d'un chef d'entreprise (« artisanale, industrielle ou commerciale, d'une personne exerçant une profession libérale, de son conjoint participant effectivement à l'activité de l'entreprise à titre professionnel et habituel ou d'un associé non salarié d'une société civile professionnelle, d'une société civile de moyens ou d'une société d'exercice libéral ») | Replacement of the head of a craft, industrial or commercial business, of a self-employed professional, of their spouse working in the business, or of a non-salaried partner in a professional partnership. |  |
|  |  | 09 | Recruitment of a person facing barriers to employment | Recrutement de personnes sans emploi rencontrant des difficultés sociales et professionnelles particulières | Recruitment of an unemployed person facing particular social and occupational difficulties. |  |
|  |  | 10 | Supplementary vocational training | Complément de formation professionnelle au salarié | Supplementary vocational training for the employee. |  |
|  |  | 11 | Training through apprenticeship | Formation professionnelle au salarié par la voie de l'apprentissage, en vue de l'obtention d'une qualification professionnelle sanctionnée par un diplôme ou un titre à finalité professionnelle enregistré au répertoire national des certifications professionnelles | Vocational training through apprenticeship, leading to a qualification entered in the national register of vocational certifications. |  |
|  |  | 12 | Replacement of an employee temporarily part time | Remplacement d’un salarié passé provisoirement à temps partiel | Replacement of an employee who has provisionally moved to part-time work. |  |
|  |  | 13 | Pending abolition of a post | Attente de la suppression définitive du poste du salarié ayant quitté définitivement l’entreprise | Pending the definitive abolition of the post of an employee who has permanently left the firm. |  |
|  |  | 14 | Travel contract | Contrat de voyage | Travel contract. |  |
|  |  | 15 | Recruitment of a disabled agency worker | Recrutement d'un intérimaire en sa qualité de BOETH | Recruitment of an agency worker in their capacity as a disabled-worker beneficiary. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Employee Status under the Collective Agreement | 02 | Salaried craftsman or trader | artisan ou commerçant salarié de son entreprise | Craftsman or trader who is an employee of their own company. | PRIVATE-SECTOR FILTER APPLIED. Excluded: State, hospital and territorial public-service agents (08, 09, 10). The salaried farmer (01) is excluded with the MSA scheme. This mapper answers a different question from the Supplementary Pension Category Status mapper and the two may legitimately disagree; both must be captured. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.002 |
|  |  | 03 | Senior executive | cadre dirigeant (votant au collège employeur des élections prud'homales) | Senior executive, voting in the employer college at the industrial tribunal elections. |  |
|  |  | 04 | Other managerial grade | autres cadres au sens de la convention collective (ou du statut pour les régimes spéciaux) | Other managerial-grade employee within the meaning of the collective agreement. |  |
|  |  | 05 | Intermediate profession | profession intermédiaire (technicien, contremaître, agent de maîtrise, clergé) | Intermediate profession: technician, foreman, supervisor. |  |
|  |  | 06 | Clerical or service employee | employé administratif d'entreprise, de commerce, agent de service | Administrative or commercial clerical employee, or service agent. |  |
|  |  | 07 | Manual worker | ouvriers qualifiés et non qualifiés y compris ouvriers agricoles | Skilled and unskilled manual workers. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Supplementary Pension Category Status | 01 | Managerial grade (arts. 4 and 4bis) | cadre (article 4 et 4bis) | Managerial grade within the meaning of Articles 4 and 4bis of the former 1947 national agreement, carried forward by the national interprofessional agreement of 17 November 2017. | This is the field that triggers the compulsory 1.50% employer death-and-disability contribution on the first band of pay for managerial-grade employees. Failure to insure makes the employer liable to the beneficiaries for a capital sum equal to three years' pay, so codes 01 and 02 are not merely declarative. Since the 2019 merger there is a single unified Agirc-Arrco scheme and no separate managerial-grade pension scheme. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.003 |
|  |  | 02 | Extended managerial grade | extension cadre pour retraite complémentaire | Extension of managerial grade for supplementary pension purposes, under Article 36 of the former Annex I. |  |
|  |  | 04 | Non-managerial | non cadre | Not managerial grade for supplementary pension purposes. |  |
|  |  | 98 | Scheme defines no managerial status | retraite complémentaire ne définissant pas de statut cadre ou non-cadre | The supplementary pension scheme does not define a managerial or non-managerial status. |  |
|  |  | 99 | No supplementary pension | pas de retraite complémentaire | No supplementary pension scheme applies. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Employment Status | 03 | Statutory | Statutaire | Employee holding a statutory position. Retained for completeness; it applies to schemes outside the general scheme. | PRIVATE-SECTOR FILTER APPLIED. Excluded: every value prefixed [FP] in the norm - established civil servants, public-service contract staff, trainee civil servants, State manual workers, career and reserve military personnel, and the public-service career-access pathway (01, 02, 08, 09, 10, 11, 12) - together with hospital medical staff and doctors without hospital status (06, 07). In a private-sector build under the general scheme the ordinary value is 99. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.026 |
|  |  | 04 | Non-statutory | Non statutaire | Employee not holding a statutory position. |  |
|  |  | 99 | Not concerned | Non concerné | Not applicable. This is the ordinary value for a private-sector employee under the general scheme. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Multiple-Jobs Code | 01 | Single job | emploi unique | The employee holds a single post with this employer. | Mandatory on every contract. Used by the collecting bodies to reconcile several contract blocks declared for the same individual by the same employer. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.036 |
|  |  | 02 | Multiple jobs | emplois multiples | The employee holds several posts with this employer. |  |
|  |  | 03 | Situation not known | situation non connue | The employer does not know whether the employee holds more than one post. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Multiple-Employers Code | 01 | Single employer | employeur unique | The employee works for this employer only. | Mandatory on every contract. It matters because each employer restarts the social security ceiling independently, so an employee with several employers may exceed the annual ceiling across all of them; the reconciliation is made by the collecting bodies, not by any one employer. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.037 |
|  |  | 02 | Multiple employers | employeurs multiples | The employee works for several employers. |  |
|  |  | 03 | Situation not known | situation non connue | The employer does not know whether the employee has other employers. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Worker Abroad Status | 01 | Posted | Détaché | Employee posted abroad by this employer and remaining affiliated to the French social security scheme, evidenced by a portable document A1 or the equivalent certificate. | Mandatory on every contract. This mapper records an employee sent OUT of France by a French employer. A worker posted INTO France who remains affiliated to a foreign scheme under a portable document A1 is outside the scope of this build entirely: no French contributions are due, the foreign employer pays the worker and there is no French payslip to produce. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.024; EU Regulation (EC) No 883/2004; Social Security Code Article L111-2-2 |
|  |  | 02 | Expatriate | Expatrié | Employee expatriated outside the French social security scheme. |  |
|  |  | 03 | Frontier worker | Frontalier | Frontier worker. |  |
|  |  | 99 | Not concerned | Non concerné | The employee works in France. This is the ordinary value. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | DSN Exclusion Reason | 01 | Public service | Fonctionnaires de l’une des trois fonctions publiques (Etat, Territoriale, Hospitalière) sauf admission spécifique | Established civil servants of the State, territorial or hospital public service, save on specific admission. | Conditional and, for this build, diagnostic rather than operational: EVERY value of this list falls outside the scope of the France build. The mapper is carried so that a contract in one of these categories is recognised and routed away from the DSN rather than silently mis-declared. Codes 01 (public service), 02 and 03 (merchant-navy crew and sea fishermen, descoped with ENIM) and 13 (registered dockers) are outside scope by scheme; codes 05 and 06 cover entertainment contracts declared through the monthly employer certificate channel instead. Constraint - DSN Exclusion Reason is Conditional Mandatory: Mandatory only where the contract falls into one of the excluded categories. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.025 |
|  |  | 02 | Merchant-navy crew | Personnels navigants de la marine marchande | Seagoing personnel of the merchant navy. |  |
|  |  | 03 | Sea fishermen | Marins-pêcheurs | Sea fishermen. |  |
|  |  | 05 | Entertainment technician (AEM) | Contrat de travail faisant l'objet d’une attestation employeur mensuelle (AEM) pour un ouvrier ou technicien de l'édition d'enregistrement sonore, de la production cinématographique et audiovisuelle, de la radio, de la diffusion et du spectacle | Contract covered by a monthly employer certificate for a worker or technician in sound recording, film and audiovisual production, radio, broadcasting or live performance. |  |
|  |  | 06 | Performing artist (AEM) | Contrat de travail faisant l'objet d'une attestation employeur mensuelle (AEM) pour un artiste du spectacle | Contract covered by a monthly employer certificate for a performing artist. |  |
|  |  | 13 | Registered docker (card G) | Dockers carte G | Docker holding a G card. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Remuneration by Tips | 01 | Yes | oui | The employee is remunerated wholly or partly by tips. | Conditional: declared only where it applies. The norm publishes a single affirmative value; the absence of the rubrique means the employee is not remunerated by tips. Where it applies, the contribution base is constituted differently and the minimum-wage test must be run against the reconstituted base. Constraint - Remuneration by Tips is Conditional Mandatory: Mandatory where the employee is remunerated wholly or partly by tips. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.045 |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Part-Time Contribution on a Full-Time Basis | 01 | Basic old-age scheme only | pour la vieillesse régime de base | Contributions are computed on the full-time equivalent for the basic old-age scheme only. | Conditional: declared only where a written agreement is in force. The agreement must be in writing and the employer normally bears the difference in contributions. The absence of the rubrique means no such agreement exists. Constraint - Part-Time Employee Contributing on a Full-Time Basis is Conditional Mandatory: Mandatory where such an agreement is in force for the contract. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.044 |
|  |  | 02 | Basic scheme and supplementary pension | pour la vieillesse régime de base et la retraite complémentaire | Contributions are computed on the full-time equivalent for both the basic old-age scheme and the supplementary pension. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Working-Time Unit of Measure | 10 | Hours | heure | Working time measured in hours. The ordinary value: a full-time 35-hour week is 151.67 hours a month. | Mandatory on every contract. A genuine calculation-path selector, not a label: an employee on an annual day-count arrangement (20) works no overtime, and the piece and share bases (31 to 35) change how the minimum-wage test and the ceiling proration are run. PRIVATE-SECTOR FILTER: the share basis (35) is retained because it is used in sectors other than sea fishing, but a client using it in a maritime context is outside scope. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.011 |
|  |  | 12 | Days | journée | Working time measured in days. |  |
|  |  | 20 | Annual day-count arrangement | forfait jour | Annual day-count arrangement (forfait annuel en jours), typically 218 days. No overtime arises. |  |
|  |  | 21 | Hour-count arrangement | forfait heure | Hour-count arrangement (forfait en heures). |  |
|  |  | 31 | Per piece | à la pige | Remuneration per piece of work, used in journalism and related sectors. |  |
|  |  | 32 | Per session | à la vacation | Remuneration per session or engagement. |  |
|  |  | 33 | Per task | à la tâche | Remuneration per task. |  |
|  |  | 34 | At the minimum wage | au SMIC | Working time expressed by reference to the statutory minimum wage. |  |
|  |  | 35 | Per share | à la part | Remuneration by share of the proceeds. |  |
|  |  | 99 | Not concerned | salarié non concerné | The employee has no measured working time. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Working-Time Arrangement | 10 | Full time | Temps plein | Full-time work. | Mandatory on every contract. PRIVATE-SECTOR FILTER APPLIED: alternating time for civil-aviation flight crew (30) and the 2004 phased-retirement arrangement (40) are excluded, the first as a sector arrangement outside this build and the second as a closed historic scheme. Where the value is part time (20, 41, 42) the Part-Time Working Rate field becomes mandatory and the social security ceiling is prorated on the hours ratio. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.014 |
|  |  | 20 | Part time | Temps partiel | Part-time work by agreement. |  |
|  |  | 41 | Part time as of right | Temps partiel de droit | Part-time work taken as of right. |  |
|  |  | 42 | Part time as of right for a child | Temps partiel de droit pour enfant | Part-time work taken as of right to care for a child. |  |
|  |  | 99 | Not concerned | Salarié non concerné | Not applicable. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Sickness-Risk Basic Scheme Code | 200 | General scheme (CNAM) | régime général (CNAM) | The general social security scheme, administered for the sickness risk by the national sickness insurance fund. This is the value for a private-sector employee in scope for this build. | PRIVATE-SECTOR FILTER APPLIED, and this is the sharpest filter on the sheet. Excluded: SNCF (134), RATP (135), ENIM (136), the miners' scheme CANSSM (137), career military CNMSS (138), notarial staff CRPCEN (140), the Paris chamber of commerce (141), the National Assembly (144), the Senate (145), the port of Bordeaux (146), the electricity and gas scheme CAMIEG (147), the clergy scheme CAVIMAC (149), the agricultural scheme MSA (300), the Banque de France scheme (400) and the overseas territorial reserve (900). For a private-sector employee under the general scheme the value is 200. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.018 |
|  |  | 909 | Foreign worker not liable in France | travailleur étranger non assujetti à un régime de base risque maladie en France | Foreign worker not subject to a basic sickness scheme in France - typically an employee covered by a foreign scheme under a coordination agreement. |  |
|  |  | 999 | No compulsory scheme | sans régime obligatoire | No compulsory basic sickness scheme applies. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Old-Age-Risk Basic Scheme Code | 200 | General scheme (CNAV) | régime général (CNAV) | The general social security scheme, administered for the old-age risk by the national old-age insurance fund. This is the value for a private-sector employee in scope for this build. | PRIVATE-SECTOR FILTER APPLIED. Excluded: the public-service pension schemes CNRACL, FSPOEIE and SRE (120, 121, 122), the railway, RATP, ENIM, miners', Banque de France, notarial, Paris chamber of commerce, parliamentary, CNIEG, CAVIMAC, CNBF, SEITA, Comédie-Française and Opéra de Paris schemes (134 to 160), the agricultural scheme MSA (300), the overseas territorial reserve and Monaco (900, 904), Mayotte's CSSM (905), and the non-affiliation values reserved for hospital academic staff, civil servants in accessory activity and elected officials (994, 995, 998). Value 997, non-affiliation for an intern outside vocational training, IS retained because interns receiving a statutory gratuity are in scope. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.020 |
|  |  | 909 | Worker not liable in France | travailleur non assujetti à un régime de base risque vieillesse en France | Worker not subject to a basic old-age scheme in France. |  |
|  |  | 996 | Non-affiliation - expatriate | absence d’affiliation pour un expatrié | No affiliation, because the employee is an expatriate outside the French scheme. |  |
|  |  | 997 | Non-affiliation - intern | absence d’affiliation pour un stagiaire hors formation professionnelle | No affiliation, because the individual is an intern outside vocational training receiving a gratuity rather than a wage. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Occupational-Accident-Risk Basic Scheme Code | 200 | General scheme (CNAM) | régime général (CNAM) | The general social security scheme for the occupational-accident and occupational-disease risk, rated per establishment by CARSAT. This is the value for a private-sector employee in scope for this build. | PRIVATE-SECTOR FILTER APPLIED. Excluded: SNCF (134), RATP (135), ENIM (136), the miners' scheme (137), the electricity and gas scheme (147), the agricultural scheme (300), the residual other-scheme value (900) and the value reserved for public servants whose occupational-accident risk is borne by the State (999). Codes 401 and 402, where the employer bears the risk itself in whole or in part, are also excluded: they sit outside the general-scheme rating mechanism on which the AT/MP net rate captured in this Data Dictionary depends. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.039 |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Compulsory Scheme Base Complement | 01 | Alsace-Moselle local scheme | régime local Alsace Moselle | The employee's place of work is in Bas-Rhin, Haut-Rhin or Moselle and the local health scheme applies on top of the general scheme. | Mandatory on every contract; the value 99 must be supplied where no complement applies. PRIVATE-SECTOR FILTER APPLIED: the CAMIEG values (02, 03) are excluded with the electricity and gas scheme. Where code 01 applies the employee pays an additional health contribution of 1.30% of total remuneration for 2026, held unchanged from 2025 by decision of the local scheme's board of 19 December 2025, and is entitled to two extra public holidays. THE TRIGGER IS THE PLACE OF WORK, NOT THE EMPLOYEE'S RESIDENCE. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.016; Social Security Code Articles L325-1 and D242-10; Loi du 1er juin 1924 |
|  |  | 99 | Not applicable | non applicable | No local scheme complement applies. This is the ordinary value. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Supplementary Pension Scheme Code | RUAA | Unified Agirc-Arrco scheme | Régime unifié AGIRC-ARRCO | The unified Agirc-Arrco supplementary pension scheme. This is the value for every private-sector employee for periods from 1 January 2019 onwards. | PRIVATE-SECTOR FILTER APPLIED. Excluded: the chartered accountants' scheme CAVEC, the bar scheme CNBF, the notarial staff scheme CRPCEN, the civil-aviation flight crew scheme CRPNPAC and the public-sector non-established staff scheme IRCANTEC. The historic ARRCO and ARRCO-plus-AGIRC codes (RETA, RETC) are retained only for the declaration of periods before the 1 January 2019 merger; for any 2026 period the value is RUAA. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.71.002; Chiffr'Agirc-Arrco 2026 |
|  |  | RETA | ARRCO (pre-2019) | Retraite complémentaire ARRCO | Former ARRCO supplementary pension. Historic value, valid only for periods before 1 January 2019. |  |
|  |  | RETC | ARRCO and AGIRC (pre-2019) | Retraite complémentaire ARRCO et AGIRC | Former ARRCO and AGIRC supplementary pension. Historic value, valid only for periods before 1 January 2019. |  |
|  |  | 90000 | No supplementary scheme | pas de régime complémentaire | No supplementary pension scheme applies. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Disabled-Worker Beneficiary Status (BOETH) | 01 | Recognised disabled worker | Travailleur reconnu handicapé par la commission des droits et de l'autonomie des personnes handicapées | Worker recognised as disabled by the commission on the rights and autonomy of disabled persons. | Conditional and voluntary: the declaration is made by the employee and cannot be required by the employer. PRIVATE-SECTOR FILTER APPLIED: the two public-agent values, redeployed public agent (10) and public agent receiving a temporary invalidity allowance (11), are excluded. This is special-category data under the GDPR: it requires a distinct justification, restricted access and separate retention. Omitting a declared status overstates the annual employment-obligation contribution. Constraint - Disabled-Worker Beneficiary Status (BOETH) is Conditional Mandatory: Mandatory where the employee has declared a disabled-worker status and wishes it to be counted. The declaration is voluntary and cannot be required. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.40.072; Labour Code Articles L5212-13 and L5212-7 |
|  |  | 02 | Industrial-accident annuitant, 10% or more | Victime d'accident du travail ou de maladie professionnelle ayant entraîné une incapacité permanente au moins égale à 10 % et titulaire d'une rente | Victim of an industrial accident or occupational disease resulting in permanent incapacity of at least 10% and holding an annuity. |  |
|  |  | 03 | Invalidity pensioner, two-thirds capacity loss | Titulaire d'une pension d'invalidité à condition que l'invalidité réduise au moins des deux tiers sa capacité de travail | Holder of an invalidity pension, where the invalidity reduces working capacity by at least two thirds. |  |
|  |  | 04 | Military invalidity pensioner (art. L241-2) | Bénéficiaire mentionné à l'article L.241-2 du Code des pensions militaires d'invalidité et des victimes de la guerre | Beneficiary under Article L241-2 of the Code of military invalidity pensions and war victims. |  |
|  |  | 05 | Military invalidity pensioner (arts. L241-3, L241-4) | Bénéficiaire mentionné aux articles L.241-3 et L.241-4 du Code des pensions militaires d'invalidité et des victimes de la guerre | Beneficiary under Articles L241-3 and L241-4 of the Code of military invalidity pensions and war victims. |  |
|  |  | 06 | Invalidity allowance or annuity (1991 Act) | Titulaire d'une allocation ou d'une rente d'invalidité dans les conditions définies par la Loi n°91-1389 du 31 décembre 1991 | Holder of an invalidity allowance or annuity under the conditions set by Act n° 91-1389 of 31 December 1991. |  |
|  |  | 07 | Inclusion mobility card - invalidity | Titulaire de la carte "mobilité inclusion" portant la mention "invalidité" (L. 241-3 du Code de l'action sociale et des familles) | Holder of the inclusion mobility card bearing the invalidity mention, under Article L241-3 of the Social Action and Families Code. |  |
|  |  | 08 | Disabled adults' allowance | Titulaire de l'allocation aux adultes handicapés | Holder of the disabled adults' allowance. |  |
|  |  | 09 | Military invalidity pensioner (arts. L241-5, L241-6) | Bénéficiaire mentionné aux articles L.241-5 et L.241-6 du Code des pensions militaires d'invalidité et des victimes de guerre | Beneficiary under Articles L241-5 and L241-6 of the Code of military invalidity pensions and war victims. |  |
|  |  | 12 | Trainee entitled to disability compensation | Ayant droit à la prestation de compensation du handicap, à l'allocation compensatrice pour tierce personne ou à l'allocation d'éducation de l'enfant handicapé bénéficiant d'un stage (L.5212-7 du Code du travail) | Person entitled to the disability compensation benefit, the third-party carer's allowance or the disabled child education allowance, undertaking a placement under Labour Code Article L5212-7. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | External Disabled-Worker Beneficiary Type | 01 | Agency workers | BOETH intérimaires | Disabled-worker beneficiaries supplied as temporary agency workers. | Conditional: declared only where the establishment counts externally supplied disabled-worker beneficiaries towards its employment obligation. These are people made available to the establishment by a third party, and they are counted differently from the establishment's own employees, who are declared through the individual BOETH status instead. Constraint - External Disabled-Worker Beneficiary Type is Conditional Mandatory: Mandatory where the establishment counts externally supplied disabled-worker beneficiaries towards its employment obligation. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.13.002; FR-URSSAF-003 DOETH |
|  |  | 02 | Employer-grouping employees | BOETH salariés d'un groupement d'employeurs mis à disposition | Disabled-worker beneficiaries who are employees of an employer grouping made available to the establishment. |  |
|  |  | 03 | Trainees not individually declared | BOETH stagiaires n’ayant pas fait l’objet d’une déclaration nominative au préalable | Disabled-worker beneficiaries on placement who have not been the subject of a prior named declaration. |  |
|  |  | 04 | Intermediate-association employees | BOETH salariés d’une association intermédiaire mis à disposition | Disabled-worker beneficiaries who are employees of an intermediate association made available to the establishment. |  |
|  |  | 05 | Model-agency employees | BOETH salariés d’une agence de mannequin mis à disposition | Disabled-worker beneficiaries who are employees of a model agency made available to the establishment. |  |
|  |  | 06 | Shared part-time company employees | BOETH salariés d’une entreprise de travail à temps partagé (ETTP) mis à disposition | Disabled-worker beneficiaries who are employees of a shared part-time employment company made available to the establishment. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Occupational Hardship Exposure Factor | 05 | Hyperbaric environment | les activités exercées en milieu hyperbare | Activities performed in a hyperbaric environment. | Conditional: declared once per factor, and only where exposure exceeds the statutory threshold over the attachment year. Six factors remain declarable after the 2017 reform, which removed the four ergonomic factors from the account mechanism. The cancellation value 99 is used to withdraw a factor previously declared in error and must not be used as a null. Constraint - Occupational Hardship Exposure Factor is Conditional Mandatory: Mandatory where the employee is exposed to one or more hardship factors beyond the statutory thresholds during the attachment year. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.34.001; Labour Code Articles L4163-1 and following |
|  |  | 06 | Extreme temperatures | les températures extrêmes | Exposure to extreme temperatures. |  |
|  |  | 07 | Noise | le bruit | Exposure to noise above the statutory threshold. |  |
|  |  | 08 | Night work | le travail de nuit | Night work. |  |
|  |  | 09 | Successive alternating shifts | le travail en équipes successives alternantes | Work in successive alternating shifts. |  |
|  |  | 10 | Repetitive work | le travail répétitif (répétition d'un même geste, à une cadence contrainte avec un temps de cycle défini) | Repetitive work: repetition of the same movement at a constrained pace with a defined cycle time. |  |
|  |  | 99 | Cancellation | annulation | Cancellation of a factor previously declared for the attachment year. Not a null value. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Seniority Type | 02 | Seniority in the sector | Ancienneté dans la branche professionnelle ou le secteur d'activité | Seniority in the industry sector or branch of activity. | Conditional: mandatory where a seniority value is recorded. Several collective-agreement entitlements turn on a seniority other than length of service in the entity, which is why the type must be captured alongside the value and not assumed. All values are in scope for a private-sector build. Constraint - Seniority Type is Conditional Mandatory: Mandatory where a seniority value is recorded for the contract. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.86.001 |
|  |  | 03 | Seniority in the category | Ancienneté dans le collège ou la catégorie professionnelle | Seniority in the college or occupational category. |  |
|  |  | 04 | Seniority in the post | Ancienneté dans le poste | Seniority in the post held. |  |
|  |  | 06 | Seniority in the group | Ancienneté dans le groupe | Seniority in the group of companies. |  |
|  |  | 07 | Seniority in the entity | Ancienneté dans l'entreprise | Seniority in the legal entity. This is the seniority on which statutory severance and notice are computed. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Seniority Unit of Measure | 01 | Days | Jours | Seniority expressed in days. | Conditional: mandatory where a seniority value is recorded. The unit must be stated explicitly; a bare number is ambiguous and the collecting bodies do not infer it. Constraint - Seniority Unit of Measure is Conditional Mandatory: Mandatory where a seniority value is recorded for the contract. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.86.002 |
|  |  | 02 | Months | Mois | Seniority expressed in months. |  |
|  |  | 03 | Years | Années | Seniority expressed in years. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Wage Attachment Type | PDA | Direct payment of maintenance | Paiement direct de pension alimentaire | Direct payment of a maintenance obligation, served by the creditor's enforcement officer or by the family allowance fund. Ranks first and is NOT limited by the seizable fraction. | Conditional: mandatory where an attachment is in force. THE PRIORITY ORDER IS STATUTORY AND IS NOT THE ORDER OF ARRIVAL. Direct payment of maintenance ranks first and is NOT limited by the seizable fraction; the other three are. If the employer does not act on an order served on it, it becomes personally liable to the creditor for the sums that should have been withheld. The procedure ceased to be judicial on 1 July 2025 and is now conducted by court enforcement officers. Constraint - Wage Attachment Type is Conditional Mandatory: Mandatory where a wage attachment is in force against the employee. Source: FR-CCG-001 Module 7; Act n° 2023-1059 of 20 November 2023; Décret of 12 February 2025; Décret n° 2025-1299 of 24 December 2025 |
|  |  | CES | Assignment of wages | Cession sur rémunération | Voluntary assignment of wages made by the employee before a court registrar. Limited by the seizable fraction. |  |
|  |  | SATD | Administrative third-party attachment | Saisie administrative à tiers détenteur | Administrative levy served by the public finances directorate for unpaid tax or other public debt. Limited by the seizable fraction. The identifier is echoed back in the DSN. |  |
|  |  | SR | Ordinary wage attachment | Saisie sur rémunération | Ordinary attachment for a private debt, served by a court enforcement officer with a certificate confirming that no challenge is outstanding. Limited by the seizable fraction and shared between competing creditors by the distributing officer. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Health Cover Exemption Reason | D1 | Covered as a spouse's dependant | Couvert en tant qu'ayant droit du régime obligatoire du conjoint | The employee is already covered as a dependant under a spouse's compulsory scheme. Evidenced by a certificate of cover from the spouse's employer, renewed annually. | Conditional: mandatory where an exemption from the compulsory supplementary health cover is claimed. An exemption is lawful ONLY where the employee requests it in writing, provides evidence, and the founding document of the scheme provides for that ground. The evidence must be renewed annually. An exemption granted without evidence is the most common finding in a contribution inspection of this area, because the employer's contribution is then reclassified as ordinary pay for the whole period concerned. Constraint - Health Cover Exemption Reason is Conditional Mandatory: Mandatory where an exemption from the compulsory health cover is claimed. Source: FR-CCG-001 Module 5; Social Security Code Article D911-2; national interprofessional agreement of 11 January 2013 |
|  |  | D2 | Present when the scheme was imposed | Salarié présent lors de la mise en place unilatérale du régime | The employee was in post when the employer set the scheme up unilaterally and would be required to contribute. |  |
|  |  | D3 | Short contract with individual cover | CDD ou mission de moins de trois mois avec couverture individuelle responsable | The employee is on a fixed-term contract or an assignment shorter than three months and holds responsible individual cover. |  |
|  |  | D4 | Contribution exceeds 10% of pay | Salarié à temps partiel dont la cotisation excède 10% de la rémunération | The employee works part time and the employee contribution would exceed 10% of their pay. |  |
|  |  | D5 | Covered by another compulsory scheme | Bénéficiaire d'un autre régime obligatoire, dont la complémentaire santé solidaire | The employee is covered by one of the other listed compulsory schemes, including the solidarity health scheme. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Dependant Type | 01 | Adult partner | adulte (conjoint, concubin, pacs) | Adult dependant: spouse, cohabiting partner or civil partner. | Conditional: mandatory for each dependant named individually under the collective cover. Dependant data is collected only because the collective contract requires it, must be restricted in access and must not be retained beyond the affiliation. Constraint - Dependant - Type is Conditional Mandatory: Mandatory for each dependant named individually under the collective cover. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.73.003 |
|  |  | 02 | Child | enfant | Dependent child. |  |
|  |  | 03 | Other | autre (ascendant, collatéraux, …) | Other dependant: ascendant, collateral relative. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Alsace-Moselle Local Scheme | 01 | Yes | Oui | The named dependant is covered by the Alsace-Moselle local health scheme. | Conditional: declared only where it applies. The norm publishes a single affirmative value; the absence of the rubrique means the dependant is not covered by the local scheme. Constraint - Dependant - Alsace-Moselle Local Scheme is Conditional Mandatory: Mandatory where the dependant is covered by the Alsace-Moselle local scheme. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.73.001; Social Security Code Articles L325-1 and D242-10 |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Collective Cover - Covered Population | 01 | Yes - covers at least one employee | Oui, concerne au moins un salarié de l'établissement d'affectation | The contract covers at least one employee of the establishment of assignment. | Mandatory for each membership declared. It tells the insurer whether the membership is live for the establishment to which it is attached in this declaration; a membership covering no employee of the establishment must be declared as such rather than omitted. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.15.004 |
|  |  | 02 | No - covers no employee | Non, ne concerne aucun salarié de l'établissement d'affectation | The contract covers no employee of the establishment of assignment. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Tax Residence Status | R | Tax resident | Résident fiscal (domicilié fiscalement en France) | Domiciled in France for tax purposes because at least one of the Article 4 B tests is met: household or principal place of stay in France, main professional activity carried on in France, or centre of economic interests in France - subject to the applicable double tax treaty. | Mandatory on every employee. TAX RESIDENCE AND SOCIAL SECURITY AFFILIATION ARE INDEPENDENT TESTS decided by independent criteria: an individual may be a French tax resident affiliated to a foreign social security scheme, or the reverse. This mapper answers the tax question only; the social security question is answered by the Worker Abroad Status and basic scheme mappers. Tax residence decides the withholding mechanism: ordinary withholding at source for a resident, and the specific non-resident withholding of General Tax Code Article 182 A for a non-resident. Source: General Tax Code Article 4 B, as modified by any applicable double tax treaty; FR-CCG-001 Modules 2.2 and 6 |
|  |  | NR | Non-resident | Non-résident | Not domiciled in France for tax purposes. Withheld under General Tax Code Article 182 A on the 0/12/20 bands, or 0/8/14.4 for overseas-source income, and not under the ordinary withholding at source. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Withholding Rate Type | 01 | Rate transmitted by DGFiP | Taux transmis par la DGFIP | Rate transmitted by the tax administration, whether a personal rate, an individualised rate within a couple, or a rate the taxpayer has elected not to individualise. | Mandatory on every remuneration declared. The rate transmitted by the tax administration (01) is the target state; the employer applies a default grid only until that rate arrives, typically in the return flow following the first DSN. The default grids in force from 1 May 2026 are those published at BOI-BAREME-000037-20260407; the 2025 grids are superseded and must not be used. SCOPE NOTE: code 33 covers Guyane and Mayotte jointly; Mayotte has its own social security scheme and is outside the scope of this build, so code 33 is usable for Guyane only. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.50.007; BOI-BAREME-000037-20260407 (default grids from 1 May 2026) |
|  |  | 13 | Monthly grid - metropolitan France | Barème mensuel métropole | Statutory default grid, monthly basis, metropolitan France. |  |
|  |  | 17 | Mathematical monthly grid - metropolitan France | Barème mathématique sur base mensuelle métropole | Statutory default grid computed on the mathematical formula, monthly basis, metropolitan France. |  |
|  |  | 23 | Monthly grid - Guadeloupe, Réunion, Martinique | Barème mensuel Guadeloupe, Réunion et Martinique | Statutory default grid, monthly basis, Guadeloupe, La Réunion and Martinique. |  |
|  |  | 27 | Mathematical monthly grid - Guadeloupe, Réunion, Martinique | Barème mathématique sur base mensuelle Guadeloupe, Réunion et Martinique | Statutory default grid computed on the mathematical formula, monthly basis, Guadeloupe, La Réunion and Martinique. |  |
|  |  | 33 | Monthly grid - Guyane | Barème mensuel Guyane et Mayotte | Statutory default grid, monthly basis, Guyane. The norm's own wording covers Guyane and Mayotte together; Mayotte is outside the scope of this build. |  |
|  |  | 37 | Mathematical monthly grid - Guyane | Barème mathématique sur base mensuelle Guyane et Mayotte | Statutory default grid computed on the mathematical formula, monthly basis, Guyane. The norm's own wording covers Guyane and Mayotte together; Mayotte is outside the scope of this build. |  |
|  |  | 99 | Prior-year overpayment - no rate | Indu relatif à un exercice antérieur – pas de taux de PAS | Recovery relating to an earlier year, for which no withholding rate applies. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Tax Liability Code | 001 | Liable - apprenticeship tax | Assujettissement à la taxe à l'apprentissage | Liable to the apprenticeship tax. | Mandatory, once per tax. Both liability and non-liability are declared explicitly and the codes come in matched pairs, so that the collecting body can distinguish a genuine exemption from an omission. Silence is not a valid answer. Where non-liability to the apprenticeship tax is declared (002), the Apprenticeship Tax Exemption Reason field becomes mandatory. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.44.001; FR-DGFIP-003 Taxe sur les salaires; FR-URSSAF-004 Solde de la taxe d'apprentissage |
|  |  | 002 | Not liable - apprenticeship tax | Non assujettissement à la taxe à l'apprentissage | Not liable to the apprenticeship tax. Requires an exemption reason. |  |
|  |  | 003 | Liable - supplementary apprenticeship contribution | Assujettissement à la contribution supplémentaire à l’apprentissage | Liable to the supplementary apprenticeship contribution. |  |
|  |  | 004 | Not liable - supplementary apprenticeship contribution | Non assujettissement à la contribution supplémentaire à l’apprentissage | Not liable to the supplementary apprenticeship contribution. |  |
|  |  | 005 | Liable - construction-effort contribution | Assujettissement à la participation des employeurs à l'effort de construction (PEEC) | Liable to the employers' construction-effort contribution (PEEC). |  |
|  |  | 006 | Not liable - construction-effort contribution | Non assujettissement à la participation des employeurs à l'effort de construction (PEEC) | Not liable to the employers' construction-effort contribution. |  |
|  |  | 007 | Liable - vocational training contribution | Assujettissement à la contribution à la formation professionnelle (CFP) | Liable to the vocational training contribution (CFP). |  |
|  |  | 008 | Not liable - vocational training contribution | Non assujettissement à la contribution à la formation professionnelle (CFP) | Not liable to the vocational training contribution. |  |
|  |  | 009 | Liable - payroll tax | Assujettissement à la taxe sur les salaires | Liable to the payroll tax (taxe sur les salaires). |  |
|  |  | 010 | Not liable - payroll tax | Non assujettissement à la taxe sur les salaires | Not liable to the payroll tax. |  |
|  |  | 013 | Liable - CPF-CDD contribution | Assujettissement à la contribution dédiée au financement du Compte Personnel de Formation pour les titulaires de CDD (CPF-CDD) | Liable to the contribution funding the personal training account for holders of fixed-term contracts. |  |
|  |  | 014 | Not liable - CPF-CDD contribution | Non assujettissement à la contribution dédiée au financement du Compte Personnel de Formation pour les titulaires de CDD (CPF-CDD) | Not liable to the contribution funding the personal training account for holders of fixed-term contracts. |  |
|  |  | 015 | Payroll tax base - first increased rate | Assiette de la taxe sur les salaires au premier taux | Payroll tax base at the first increased rate. |  |
|  |  | 016 | Payroll tax base - second increased rate | Assiette de la taxe sur les salaires au deuxième taux | Payroll tax base at the second increased rate. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Contract Termination Reason | 011 | Dismissal - insolvency proceedings | licenciement suite à liquidation judiciaire ou à redressement judiciaire | Dismissal following judicial liquidation or judicial reorganisation. | Conditional: mandatory once the contract has ended. PRIVATE-SECTOR FILTER APPLIED: the two public-service revocation values, revocation for abandonment of post (070) and revocation following a criminal sanction (071), are excluded, as are end of a line of service (116) and end of assignment (119), which belong to the maritime and public-sector constructs descoped from this build. The 2026 employer contribution on a mutually agreed termination (043) is 40%, up from 30%, under the Social Security Financing Act for 2026 - a stale 30% is a defect, not a rounding difference. Constraint - Contract Termination Reason is Conditional Mandatory: Mandatory once the contract has ended. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.62.002; Labour Code Articles L1234-1 and following, L1237-11 and following, L1243-8 |
|  |  | 012 | Dismissal - permanent closure | licenciement suite à fermeture définitive de l'établissement | Dismissal following the permanent closure of the establishment. |  |
|  |  | 014 | Dismissal - economic grounds | licenciement pour motif économique | Dismissal on economic grounds. |  |
|  |  | 015 | Dismissal - end of site or operation | licenciement pour fin de chantier ou d'opération | Dismissal on the end of a site or operation. |  |
|  |  | 020 | Dismissal - other grounds | licenciement pour autre motif | Dismissal on other grounds. |  |
|  |  | 025 | Other economic termination | autre fin de contrat pour motif économique | Other end of contract on economic grounds. |  |
|  |  | 026 | Termination - acceptance of a CSP | rupture pour motif économique suite à l'acceptation d’un contrat de sécurisation professionnelle | Termination on economic grounds following acceptance of an occupational securing contract. |  |
|  |  | 031 | End of fixed-term contract | fin de contrat à durée déterminée ou fin d'accueil occasionnel | End of a fixed-term contract, or end of occasional engagement. |  |
|  |  | 032 | End of agency assignment | fin de mission d'intérim | End of a temporary-agency assignment. |  |
|  |  | 033 | Early termination - medical unfitness | rupture anticipée d’un CDD ou d’un contrat de mission en cas d’inaptitude physique constatée par le médecin du travail | Early termination of a fixed-term or assignment contract on medical unfitness established by the occupational physician. |  |
|  |  | 034 | End of trial period - employer | fin de période d'essai à l'initiative de l'employeur | End of the trial period at the employer's initiative. |  |
|  |  | 035 | End of trial period - employee | fin de période d'essai à l'initiative du salarié | End of the trial period at the employee's initiative. |  |
|  |  | 036 | Early termination - employer | rupture anticipée d'un CDD, d’un contrat de professionnalisation, d'un contrat d'apprentissage ou d’un contrat de mission à l'initiative de l'employeur | Early termination of a fixed-term, professionalisation, apprenticeship or assignment contract at the employer's initiative. |  |
|  |  | 037 | Early termination - employee | rupture anticipée d'un CDD, d’un contrat de professionnalisation, d'un contrat d'apprentissage ou d’un contrat de mission à l'initiative du salarié | Early termination of a fixed-term, professionalisation, apprenticeship or assignment contract at the employee's initiative. |  |
|  |  | 038 | Retirement at the employer's initiative | mise à la retraite par l'employeur | Retirement imposed by the employer. |  |
|  |  | 039 | Retirement at the employee's initiative | départ à la retraite à l'initiative du salarié | Retirement at the employee's own initiative. |  |
|  |  | 043 | Mutually agreed termination | rupture conventionnelle | Mutually agreed termination (rupture conventionnelle). Carries a 40% employer contribution for 2026 on the indemnity. |  |
|  |  | 058 | Constructive termination by the employee | prise d'acte de la rupture de contrat de travail | Constructive termination of the contract by the employee (prise d'acte). |  |
|  |  | 059 | Resignation | démission | Resignation. |  |
|  |  | 065 | Death or internment of the employer | décès de l'employeur ou internement / conduit à un licenciement autre motif | Death or internment of the employer, leading to a dismissal on other grounds. |  |
|  |  | 066 | Death of the employee | décès de l’individu | Death of the employee. |  |
|  |  | 081 | End of apprenticeship contract | fin de contrat d'apprentissage | End of an apprenticeship contract at its term. |  |
|  |  | 082 | Judicial rescission | résiliation judiciaire du contrat de travail | Judicial rescission of the employment contract. |  |
|  |  | 083 | Force majeure | rupture de contrat de travail ou d’un contrat de mission pour force majeure ou fait du prince | Termination of an employment or assignment contract for force majeure or act of a public authority. |  |
|  |  | 084 | Termination by mutual consent | rupture d'un commun accord du CDD, d’un contrat de professionnalisation, du contrat d'apprentissage ou d’un contrat de mission | Termination by mutual consent of a fixed-term, professionalisation, apprenticeship or assignment contract. |  |
|  |  | 085 | End of mandate | fin de mandat | End of a corporate officer's mandate. |  |
|  |  | 086 | Dismissal - CATS agreement | licenciement convention CATS | Dismissal under an early cessation of activity agreement. |  |
|  |  | 087 | Dismissal - serious misconduct | licenciement pour faute grave | Dismissal for serious misconduct. |  |
|  |  | 088 | Dismissal - gross misconduct | licenciement pour faute lourde | Dismissal for gross misconduct. |  |
|  |  | 089 | Dismissal - force majeure | licenciement pour force majeure | Dismissal for force majeure. |  |
|  |  | 091 | Dismissal - non-occupational unfitness | licenciement pour inaptitude physique d'origine non professionnelle | Dismissal for medical unfitness of non-occupational origin. |  |
|  |  | 092 | Dismissal - occupational unfitness | licenciement pour inaptitude physique d'origine  professionnelle | Dismissal for medical unfitness of occupational origin. |  |
|  |  | 093 | Dismissal - administrative decision | licenciement suite à décision d'une autorité administrative | Dismissal following a decision of an administrative authority. |  |
|  |  | 094 | Early termination - filming stopped | rupture anticipée du contrat de travail pour arrêt de tournage | Early termination of the employment contract because filming stopped. |  |
|  |  | 095 | Early termination - serious misconduct | rupture anticipée du contrat de travail ou d’un contrat de mission pour faute grave | Early termination of an employment or assignment contract for serious misconduct. |  |
|  |  | 096 | Early termination - gross misconduct | rupture anticipée du contrat de travail ou d’un contrat de mission pour faute lourde | Early termination of an employment or assignment contract for gross misconduct. |  |
|  |  | 097 | Early termination - establishment closure | rupture anticipée d’un contrat de travail ou d’un contrat de mission suite à fermeture de l'établissement | Early termination of an employment or assignment contract following the closure of the establishment. |  |
|  |  | 098 | Withdrawal of the child | retrait d'enfant | Withdrawal of the child, in childminding employment. |  |
|  |  | 099 | Cancellation | Annulation | Cancellation of an end-of-contract previously declared. Not a termination reason: it withdraws an earlier declaration. |  |
|  |  | 100 | Transfer without termination | Mutation au sein du même groupe ou extérieure au groupe pour les secteurs d’activité autorisés (gardiennage, ménage, restauration, etc.) sans rupture du contrat | Transfer within or outside the group, in the sectors where it is permitted - security, cleaning, catering and similar - without termination of the contract. |  |
|  |  | 110 | Collective mutually agreed termination | Rupture conventionnelle collective | Collective mutually agreed termination. |  |
|  |  | 111 | Amicable termination - mobility leave | Rupture amiable dans le cadre d’un congé de mobilité | Amicable termination in the context of mobility leave. |  |
|  |  | 112 | Termination - collective performance agreement | Rupture dans le cadre d'un accord de performance collective | Termination under a collective performance agreement. |  |
|  |  | 113 | Dismissal - specific ground (art. L2254-2) | Licenciement pour motif spécifique (Article L. 2254-2 du Code du Travail) | Dismissal on the specific ground provided by Labour Code Article L2254-2. |  |
|  |  | 114 | Termination by mutual consent - entry into PAP | Rupture d’un commun accord pour entrée en PAP | Termination by mutual consent on entry into a personalised support pathway. |  |
|  |  | 115 | Dismissal - 2017 Act arts. 18 and 19 | Licenciement au titre des articles 18 et 19 de la loi n° 2017-1339 du 15 septembre 2017 | Dismissal under Articles 18 and 19 of Act n° 2017-1339 of 15 September 2017. |  |
|  |  | 117 | Dismissal - economic, CSP refused | licenciement pour motif économique suite au refus d’un contrat de sécurisation professionnelle | Dismissal on economic grounds following refusal of an occupational securing contract. |  |
|  |  | 118 | End of business support contract | Fin de contrat d’appui au projet d’entreprise | End of a business project support contract. |  |
|  |  | 998 | Transfer outside the DSN | transfert du contrat de travail sans rupture du contrat vers un autre établissement pas rentré dans la DSN | Transfer of the employment contract without termination to another establishment not carried in this DSN. |  |
|  |  | 999 | End of another relationship | fin de relation avec l’employeur (autres que contrat de travail, convention ou mandat) | End of a relationship with the employer other than an employment contract, agreement or mandate. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Notice Performance and Payment Type | 01 | Worked and paid | préavis effectué et payé | Notice worked and paid. | Conditional: mandatory where the contract carried a notice period. The value 90, no notice clause applicable, must be supplied where there is no notice; leaving the block absent is not equivalent. Notice that is not worked but is paid remains subject to contributions and to the withholding at source; notice that is neither worked nor paid is not. Constraint - Notice Performance and Payment Type is Conditional Mandatory: Mandatory where the contract carried a notice period. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.63.001; Labour Code Articles L1234-1 and following |
|  |  | 02 | Not worked, paid | préavis non effectué et payé | Notice not worked but paid. Remains subject to contributions and to the withholding at source. |  |
|  |  | 03 | Not worked, not paid | préavis non effectué et non payé | Notice neither worked nor paid. |  |
|  |  | 10 | Not worked, not paid - CSP | préavis non effectué non payé dans le cadre d’un contrat de sécurisation professionnelle (CSP) | Notice neither worked nor paid, in the context of an occupational securing contract. |  |
|  |  | 50 | Not worked, paid - redeployment leave | préavis non effectué et payé dans le cadre d’un congé de reclassement | Notice not worked but paid, in the context of redeployment leave. |  |
|  |  | 51 | Not worked, paid - mobility leave | préavis non effectué et payé dans le cadre d’un congé de mobilité | Notice not worked but paid, in the context of mobility leave. |  |
|  |  | 60 | Advance-warning period | Délai de prévenance | Advance-warning period (délai de prévenance), applicable at the end of a trial period. |  |
|  |  | 61 | Not worked, not paid - PAP | préavis non effectué et non payé dans le cadre du parcours d’accompagnement personnalisé (PAP) | Notice neither worked nor paid, in the context of a personalised support pathway. |  |
|  |  | 90 | No notice clause applicable | pas de clause de préavis applicable | No notice clause applies to this contract. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Settlement Negotiation in Progress | 01 | Yes | oui | A settlement is being negotiated with the departing employee. | Mandatory in the end-of-contract signal. It tells France Travail that the final position may be amended, so that the unemployment entitlement is not fixed prematurely. An affirmative value must be followed by an amended declaration when the settlement concludes. Constraint - Settlement Negotiation in Progress is Conditional Mandatory: Mandatory in the end-of-contract signal. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.62.008 |
|  |  | 02 | No | non | No settlement is being negotiated. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Special Employee Status at Termination | 01 | Manager or management board | Gérant ou collège de gérance | Manager (gérant) or member of a college of managers. | Conditional: declared where the departing employee held a corporate office or one of the listed special capacities. It changes the France Travail outcome, because company officers treated as employees pay full contributions EXCEPT unemployment insurance and the wage guarantee scheme, and therefore have no unemployment entitlement arising from that office. All values are private-sector constructs and are retained. Constraint - Special Employee Status at Termination is Conditional Mandatory: Mandatory where the departing employee held a corporate office or one of the listed special capacities. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.62.014 |
|  |  | 02 | Director | Administrateur | Member of the board of directors. |  |
|  |  | 03 | Managing director | Directeur Général | Managing director (directeur général). |  |
|  |  | 04 | Chair and managing director | Président Directeur Général | Chair and managing director (président directeur général). |  |
|  |  | 05 | Member of the management board | Membre du Directoire | Member of the management board (directoire). |  |
|  |  | 06 | Chair of the management board | Président du Directoire | Chair of the management board. |  |
|  |  | 07 | Member of the supervisory board | Membre du Conseil de surveillance | Member of the supervisory board. |  |
|  |  | 08 | Association officer | Président, administrateur, secrétaire ou trésorier d'une association | Chair, director, secretary or treasurer of an association. |  |
|  |  | 09 | EIG officer or member | Contrôleur de gestion, membre ou administrateur membre d'un GIE | Management controller, member or administrator-member of an economic interest grouping. |  |
|  |  | 10 | Partner or shareholder | Associé, actionnaire | Partner or shareholder. |  |
|  |  | 11 | Umbrella-company employee | Salarié en portage salarial | Employee working under an umbrella-company arrangement (portage salarial). |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Continuation of Collective Cover Membership | 01 | Yes | oui | The departing employee's membership of the collective cover continues after the contract ends. | Conditional: declared only where the cover continues. The norm publishes a single affirmative value; the absence of the rubrique means the membership ends with the contract. Portability of health and death-and-disability cover is free of charge to the former employee and runs for up to twelve months where the termination opens an unemployment entitlement. Constraint - Continuation of Collective Cover Membership is Conditional Mandatory: Mandatory where the employee's collective cover continues after the contract ends. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.62.016; national interprofessional agreement of 11 January 2013 (portability) |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Refusal of a Permanent Contract after a Fixed-Term or Agency Contract | 01 | Offer refused | Proposition refusée | The employee refused an offer of a permanent contract made at the end of the fixed-term contract or assignment. | Conditional: declared only where a permanent contract was offered at the end of a fixed-term contract or agency assignment and refused. The norm publishes a single value; the absence of the rubrique means no offer was refused. Two refusals within twelve months can remove the unemployment entitlement, so the declaration is consequential for the employee and must not be made loosely. Constraint - Refusal of a Permanent Contract after a Fixed-Term or Agency Contract is Conditional Mandatory: Mandatory where a permanent contract was offered at the end of a fixed-term contract or agency assignment and refused. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.62.021; Labour Code Article L1243-11-1 |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Employer Legal Nature | 01 | Private | Privée | Private body. | PRIVATE-SECTOR FILTER APPLIED: the public body value (02) is excluded, since a public employer is outside the perimeter of this build. Code 03 is retained because a private establishment with a majority public shareholding remains a private-law employer under the general scheme. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.11.017 |
|  |  | 03 | Private with majority public capital | Etablissement privé à capitaux majoritaires publics | Private establishment with a majority public shareholding. Remains a private-law employer under the general scheme. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Legal Entity Location | 01 | Foreign entity with a French establishment | Entreprise étrangère avec établissement en France | Foreign firm with an establishment in France. | Conditional: declared only where the legal entity is registered outside France. A foreign employer with no establishment in France registers with the dedicated URSSAF service for foreign firms and may, in the EU cases, agree with the employee that the employee accounts for the contributions - an arrangement that changes who files, and must be settled before go-live. Constraint - Legal Entity Location is Conditional Mandatory: Mandatory where the legal entity is registered outside France. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.06.012 |
|  |  | 02 | Foreign entity outside the EU, no French establishment | Entreprise étrangère hors UE sans établissement en France | Foreign firm outside the European Union with no establishment in France. |  |
|  |  | 03 | Foreign entity in the EU, no French establishment | Entreprise étrangère dans l’UE sans établissement en France | Foreign firm in the European Union with no establishment in France. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Place of Work Legal Nature | 01 | Establishment | Etablissement | The site of work is an establishment. | Conditional: mandatory where a place of work is declared separately from the employing establishment. Home working (03) is declared here and not through the establishment address; it matters because the mobility levy follows the commune of the place of work. Constraint - Place of Work - Legal Nature is Conditional Mandatory: Mandatory where a place of work is declared separately from the employing establishment. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.85.010 |
|  |  | 02 | Other | Autre | The site of work is of another kind. |  |
|  |  | 03 | Home working | A domicile | The employee works from home. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Basis of Unemployment-Insurance Pay for Expatriates | 01 | Actual pay | Salaire réel | Unemployment-insurance contributions are assessed on the expatriate's actual pay. | Conditional: declared only where the establishment employs expatriates covered by the French unemployment insurance scheme. The choice is made once for the establishment and applies to all its expatriates; it cannot be varied employee by employee. Constraint - Basis of Unemployment-Insurance Pay for Expatriates is Conditional Mandatory: Mandatory where the establishment employs expatriates covered by the French unemployment insurance scheme. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.11.009 |
|  |  | 02 | Comparison salary | Salaire de comparaison | Unemployment-insurance contributions are assessed on a comparison salary. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Declared Contact Type | 01 | Daily allowances | Contact chez le déclaré pour les IJ | Contact at the declared entity for sickness and maternity daily allowances. | At least one contact must be declared, and several are usual, because the bodies route different queries to different types. PRIVATE-SECTOR FILTER: all values are retained, but code 15 is relevant only to employers in the sectors operating a paid-leave fund. The e-mail address attached to type 06 is where the employee identification anomalies land, so an out-of-date value there means NIR anomalies go unread for months. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S20.G00.07.004 |
|  |  | 02 | End of contract | Contact chez le déclaré pour les fins de contrats de travail (France Travail) | Contact at the declared entity for end-of-contract matters, used by France Travail. |  |
|  |  | 03 | Statistical bodies | Contact chez le déclaré pour les acteurs statistiques (DARES, INSEE, etc …) | Contact at the declared entity for the statistical bodies - DARES, INSEE and others. |  |
|  |  | 04 | Contribution recovery | Contact chez le déclaré recouvrant, entre autres, des cotisations de Sécurité Sociale (Urssaf CN, MSA) et contributions assurance chômage et cotisations AGS (France Travail) | Contact at the declared entity for the recovery of social security contributions, unemployment contributions and wage guarantee contributions. |  |
|  |  | 05 | Supplementary scheme recovery | Contact chez le déclaré pour le recouvrement des cotisations (retraite complémentaire et autres) | Contact at the declared entity for the recovery of supplementary pension and other scheme contributions. |  |
|  |  | 06 | Employee identification (NIR) | Contact sur l’identification des salariés (NIR) | Contact for employee identification questions. This is where NIR anomalies from the return flow are addressed. |  |
|  |  | 07 | Establishment identification (SIRET) | Contact sur l’identification de l’établissement (SIRET) | Contact for establishment identification questions. |  |
|  |  | 08 | General | Contextualisable à l’ensemble des organismes, hors typologies 1 à 7, et 9 | General contact, contextualisable to all bodies outside types 01 to 07 and 09. |  |
|  |  | 09 | Daily allowances - centralising establishment | Contact chez l'établissement centralisateur pour les IJ | Contact at the centralising establishment for daily allowances. |  |
|  |  | 13 | State agency employment aids | Contact chez le déclaré pour les aides versées par l'ASP | Contact at the declared entity for employment aids paid by the state agency. |  |
|  |  | 14 | Disabled-worker follow-up | Contact chez le déclaré pour le suivi des travailleurs handicapés | Contact at the declared entity for the follow-up of disabled workers. |  |
|  |  | 15 | Paid-leave funds | Contact pour les congés payés (CIBTP, Transport, Manutention portuaire) | Contact for the paid-leave funds - construction, transport, port handling. |  |
|  |  | 16 | Vocational training | Contact chez le déclaré pour la formation professionnelle | Contact at the declared entity for vocational training. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Contribution Payment Method | 01 | Cheque | chèque | Payment by cheque. | Mandatory on every payment order. France CONSOLIDATES: the social security contributions and the income tax withheld at source travel in the same DSN file, but they are settled through SEPARATE payment orders to URSSAF and to DGFiP. Declaring one payment method does not mean one payment. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.20.010; FR-CCG-001 Module 10 |
|  |  | 02 | Bank transfer | virement | Payment by bank transfer. |  |
|  |  | 04 | Interbank payment order | titre inter-bancaire de paiement | Payment by interbank payment order. |  |
|  |  | 05 | SEPA direct debit | prélèvement SEPA | Payment by SEPA direct debit. |  |
|  |  | 06 | Paid by another establishment | versement réalisé par un autre établissement | Payment made by another establishment of the entity. |  |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Employer Bank Account Usage Type | 01 | State agency aid payment | Paiement aide ASP | Account for the payment of employment aids by the services and payment agency (ASP). | Conditional: declared only where an employer bank account is supplied for the payment of state agency employment aids. The norm publishes a single value. The employer account used for subrogation is declared in the work-stoppage block instead and is not a value of this list. Constraint - Employer Bank Account Usage Type is Conditional Mandatory: Mandatory where an employer bank account is declared for the payment of state agency employment aids. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.12.001 |
|  | Option Mapper Description | Code | Abbreviation | Local Name | English Description | Notes |
|  | Subrogation | 01 | Yes | oui | The employer operates subrogation: it maintains the employee's pay and receives the daily allowances directly from the fund. | Recorded as a standing employer election in this Data Dictionary, because it drives the payslip and the work-stoppage signal for every absence. The individual stoppage dates and the daily allowance amounts are per-payrun transactional data and are deliberately OUT of Data Dictionary scope. Where subrogation applies, the employer's IBAN must be present. Source: NEODeS CT2026.1.2 (P26V01, revision 20251224), GIP-MDS / net-entreprises.fr - S21.G00.60.004; Social Security Code Article L323-1 |
|  |  | 02 | No | non | The employer does not operate subrogation: the fund pays the daily allowances to the employee. |  |

## Sheet: `Currency Codes - ISO 4217`

_272 rows x 6 columns._

**DO NOT TOUCH**

**Currency Codes (ISO 4217)**

| col1 | Country | Currency | Alphabetic Code | Numeric Code | Minor unit |
|---|---|---|---|---|---|
|  | AFGHANISTAN | Afghani | AFN | 971 | 2 |
|  | ÅLAND ISLANDS | Euro | EUR | 978 | 2 |
|  | ALBANIA | Lek | ALL | 008 | 2 |
|  | ALGERIA | Algerian Dinar | DZD | 012 | 2 |
|  | AMERICAN SAMOA | US Dollar | USD | 840 | 2 |
|  | ANDORRA | Euro | EUR | 978 | 2 |
|  | ANGOLA | Kwanza | AOA | 973 | 2 |
|  | ANGUILLA | East Caribbean Dollar | XCD | 951 | 2 |
|  | ANTIGUA AND BARBUDA | East Caribbean Dollar | XCD | 951 | 2 |
|  | ARGENTINA | Argentine Peso | ARS | 032 | 2 |
|  | ARMENIA | Armenian Dram | AMD | 051 | 2 |
|  | ARUBA | Aruban Florin | AWG | 533 | 2 |
|  | AUSTRALIA | Australian Dollar | AUD | 036 | 2 |
|  | AUSTRIA | Euro | EUR | 978 | 2 |
|  | AZERBAIJAN | Azerbaijan Manat | AZN | 944 | 2 |
|  | BAHAMAS (THE) | Bahamian Dollar | BSD | 044 | 2 |
|  | BAHRAIN | Bahraini Dinar | BHD | 048 | 3 |
|  | BANGLADESH | Taka | BDT | 050 | 2 |
|  | BARBADOS | Barbados Dollar | BBD | 052 | 2 |
|  | BELARUS | Belarusian Ruble | BYN | 933 | 2 |
|  | BELGIUM | Euro | EUR | 978 | 2 |
|  | BELIZE | Belize Dollar | BZD | 084 | 2 |
|  | BENIN | CFA Franc BCEAO | XOF | 952 | 0 |
|  | BERMUDA | Bermudian Dollar | BMD | 060 | 2 |
|  | BHUTAN | Indian Rupee | INR | 356 | 2 |
|  | BHUTAN | Ngultrum | BTN | 064 | 2 |
|  | BOLIVIA (PLURINATIONAL STATE OF) | Boliviano | BOB | 068 | 2 |
|  | BOLIVIA (PLURINATIONAL STATE OF) | Mvdol | BOV | 984 | 2 |
|  | BONAIRE, SINT EUSTATIUS AND SABA | US Dollar | USD | 840 | 2 |
|  | BOSNIA AND HERZEGOVINA | Convertible Mark | BAM | 977 | 2 |
|  | BOTSWANA | Pula | BWP | 072 | 2 |
|  | BOUVET ISLAND | Norwegian Krone | NOK | 578 | 2 |
|  | BRAZIL | Brazilian Real | BRL | 986 | 2 |
|  | BRITISH INDIAN OCEAN TERRITORY (THE) | US Dollar | USD | 840 | 2 |
|  | BRUNEI DARUSSALAM | Brunei Dollar | BND | 096 | 2 |
|  | BULGARIA | Bulgarian Lev | BGN | 975 | 2 |
|  | BURKINA FASO | CFA Franc BCEAO | XOF | 952 | 0 |
|  | BURUNDI | Burundi Franc | BIF | 108 | 0 |
|  | CABO VERDE | Cabo Verde Escudo | CVE | 132 | 2 |
|  | CAMBODIA | Riel | KHR | 116 | 2 |
|  | CAMEROON | CFA Franc BEAC | XAF | 950 | 0 |
|  | CANADA | Canadian Dollar | CAD | 124 | 2 |
|  | CAYMAN ISLANDS (THE) | Cayman Islands Dollar | KYD | 136 | 2 |
|  | CENTRAL AFRICAN REPUBLIC (THE) | CFA Franc BEAC | XAF | 950 | 0 |
|  | CHAD | CFA Franc BEAC | XAF | 950 | 0 |
|  | CHILE | Chilean Peso | CLP | 152 | 0 |
|  | CHILE | Unidad de Fomento | CLF | 990 | 4 |
|  | CHINA | Yuan Renminbi | CNY | 156 | 2 |
|  | CHRISTMAS ISLAND | Australian Dollar | AUD | 036 | 2 |
|  | COCOS (KEELING) ISLANDS (THE) | Australian Dollar | AUD | 036 | 2 |
|  | COLOMBIA | Colombian Peso | COP | 170 | 2 |
|  | COLOMBIA | Unidad de Valor Real | COU | 970 | 2 |
|  | COMOROS (THE) | Comorian Franc | KMF | 174 | 0 |
|  | CONGO (THE DEMOCRATIC REPUBLIC OF THE) | Congolese Franc | CDF | 976 | 2 |
|  | CONGO (THE) | CFA Franc BEAC | XAF | 950 | 0 |
|  | COOK ISLANDS (THE) | New Zealand Dollar | NZD | 554 | 2 |
|  | COSTA RICA | Costa Rican Colon | CRC | 188 | 2 |
|  | CÔTE D'IVOIRE | CFA Franc BCEAO | XOF | 952 | 0 |
|  | CROATIA | Kuna | HRK | 191 | 2 |
|  | CUBA | Cuban Peso | CUP | 192 | 2 |
|  | CUBA | Peso Convertible | CUC | 931 | 2 |
|  | CURAÇAO | Netherlands Antillean Guilder | ANG | 532 | 2 |
|  | CYPRUS | Euro | EUR | 978 | 2 |
|  | CZECHIA | Czech Koruna | CZK | 203 | 2 |
|  | DENMARK | Danish Krone | DKK | 208 | 2 |
|  | DJIBOUTI | Djibouti Franc | DJF | 262 | 0 |
|  | DOMINICA | East Caribbean Dollar | XCD | 951 | 2 |
|  | DOMINICAN REPUBLIC (THE) | Dominican Peso | DOP | 214 | 2 |
|  | ECUADOR | US Dollar | USD | 840 | 2 |
|  | EGYPT | Egyptian Pound | EGP | 818 | 2 |
|  | EL SALVADOR | El Salvador Colon | SVC | 222 | 2 |
|  | EL SALVADOR | US Dollar | USD | 840 | 2 |
|  | EQUATORIAL GUINEA | CFA Franc BEAC | XAF | 950 | 0 |
|  | ERITREA | Nakfa | ERN | 232 | 2 |
|  | ESTONIA | Euro | EUR | 978 | 2 |
|  | ESWATINI | Lilangeni | SZL | 748 | 2 |
|  | ETHIOPIA | Ethiopian Birr | ETB | 230 | 2 |
|  | EUROPEAN UNION | Euro | EUR | 978 | 2 |
|  | FALKLAND ISLANDS (THE) [MALVINAS] | Falkland Islands Pound | FKP | 238 | 2 |
|  | FAROE ISLANDS (THE) | Danish Krone | DKK | 208 | 2 |
|  | FIJI | Fiji Dollar | FJD | 242 | 2 |
|  | FINLAND | Euro | EUR | 978 | 2 |
|  | FRANCE | Euro | EUR | 978 | 2 |
|  | FRENCH GUIANA | Euro | EUR | 978 | 2 |
|  | FRENCH POLYNESIA | CFP Franc | XPF | 953 | 0 |
|  | FRENCH SOUTHERN TERRITORIES (THE) | Euro | EUR | 978 | 2 |
|  | GABON | CFA Franc BEAC | XAF | 950 | 0 |
|  | GAMBIA (THE) | Dalasi | GMD | 270 | 2 |
|  | GEORGIA | Lari | GEL | 981 | 2 |
|  | GERMANY | Euro | EUR | 978 | 2 |
|  | GHANA | Ghana Cedi | GHS | 936 | 2 |
|  | GIBRALTAR | Gibraltar Pound | GIP | 292 | 2 |
|  | GREECE | Euro | EUR | 978 | 2 |
|  | GREENLAND | Danish Krone | DKK | 208 | 2 |
|  | GRENADA | East Caribbean Dollar | XCD | 951 | 2 |
|  | GUADELOUPE | Euro | EUR | 978 | 2 |
|  | GUAM | US Dollar | USD | 840 | 2 |
|  | GUATEMALA | Quetzal | GTQ | 320 | 2 |
|  | GUERNSEY | Pound Sterling | GBP | 826 | 2 |
|  | GUINEA | Guinean Franc | GNF | 324 | 0 |
|  | GUINEA-BISSAU | CFA Franc BCEAO | XOF | 952 | 0 |
|  | GUYANA | Guyana Dollar | GYD | 328 | 2 |
|  | HAITI | Gourde | HTG | 332 | 2 |
|  | HAITI | US Dollar | USD | 840 | 2 |
|  | HEARD ISLAND AND McDONALD ISLANDS | Australian Dollar | AUD | 036 | 2 |
|  | HOLY SEE (THE) | Euro | EUR | 978 | 2 |
|  | HONDURAS | Lempira | HNL | 340 | 2 |
|  | HONG KONG | Hong Kong Dollar | HKD | 344 | 2 |
|  | HUNGARY | Forint | HUF | 348 | 2 |
|  | ICELAND | Iceland Krona | ISK | 352 | 0 |
|  | INDIA | Indian Rupee | INR | 356 | 2 |
|  | INDONESIA | Rupiah | IDR | 360 | 2 |
|  | INTERNATIONAL MONETARY FUND (IMF) | SDR (Special Drawing Right) | XDR | 960 | N.A. |
|  | IRAN (ISLAMIC REPUBLIC OF) | Iranian Rial | IRR | 364 | 2 |
|  | IRAQ | Iraqi Dinar | IQD | 368 | 3 |
|  | IRELAND | Euro | EUR | 978 | 2 |
|  | ISLE OF MAN | Pound Sterling | GBP | 826 | 2 |
|  | ISRAEL | New Israeli Sheqel | ILS | 376 | 2 |
|  | ITALY | Euro | EUR | 978 | 2 |
|  | JAMAICA | Jamaican Dollar | JMD | 388 | 2 |
|  | JAPAN | Yen | JPY | 392 | 0 |
|  | JERSEY | Pound Sterling | GBP | 826 | 2 |
|  | JORDAN | Jordanian Dinar | JOD | 400 | 3 |
|  | KAZAKHSTAN | Tenge | KZT | 398 | 2 |
|  | KENYA | Kenyan Shilling | KES | 404 | 2 |
|  | KIRIBATI | Australian Dollar | AUD | 036 | 2 |
|  | KOREA (THE DEMOCRATIC PEOPLE’S REPUBLIC OF) | North Korean Won | KPW | 408 | 2 |
|  | KOREA (THE REPUBLIC OF) | Won | KRW | 410 | 0 |
|  | KUWAIT | Kuwaiti Dinar | KWD | 414 | 3 |
|  | KYRGYZSTAN | Som | KGS | 417 | 2 |
|  | LAO PEOPLE’S DEMOCRATIC REPUBLIC (THE) | Lao Kip | LAK | 418 | 2 |
|  | LATVIA | Euro | EUR | 978 | 2 |
|  | LEBANON | Lebanese Pound | LBP | 422 | 2 |
|  | LESOTHO | Loti | LSL | 426 | 2 |
|  | LESOTHO | Rand | ZAR | 710 | 2 |
|  | LIBERIA | Liberian Dollar | LRD | 430 | 2 |
|  | LIBYA | Libyan Dinar | LYD | 434 | 3 |
|  | LIECHTENSTEIN | Swiss Franc | CHF | 756 | 2 |
|  | LITHUANIA | Euro | EUR | 978 | 2 |
|  | LUXEMBOURG | Euro | EUR | 978 | 2 |
|  | MACAO | Pataca | MOP | 446 | 2 |
|  | NORTH MACEDONIA | Denar | MKD | 807 | 2 |
|  | MADAGASCAR | Malagasy Ariary | MGA | 969 | 2 |
|  | MALAWI | Malawi Kwacha | MWK | 454 | 2 |
|  | MALAYSIA | Malaysian Ringgit | MYR | 458 | 2 |
|  | MALDIVES | Rufiyaa | MVR | 462 | 2 |
|  | MALI | CFA Franc BCEAO | XOF | 952 | 0 |
|  | MALTA | Euro | EUR | 978 | 2 |
|  | MARSHALL ISLANDS (THE) | US Dollar | USD | 840 | 2 |
|  | MARTINIQUE | Euro | EUR | 978 | 2 |
|  | MAURITANIA | Ouguiya | MRU | 929 | 2 |
|  | MAURITIUS | Mauritius Rupee | MUR | 480 | 2 |
|  | MAYOTTE | Euro | EUR | 978 | 2 |
|  | MEMBER COUNTRIES OF THE AFRICAN DEVELOPMENT BANK GROUP | ADB Unit of Account | XUA | 965 | N.A. |
|  | MEXICO | Mexican Peso | MXN | 484 | 2 |
|  | MEXICO | Mexican Unidad de Inversion (UDI) | MXV | 979 | 2 |
|  | MICRONESIA (FEDERATED STATES OF) | US Dollar | USD | 840 | 2 |
|  | MOLDOVA (THE REPUBLIC OF) | Moldovan Leu | MDL | 498 | 2 |
|  | MONACO | Euro | EUR | 978 | 2 |
|  | MONGOLIA | Tugrik | MNT | 496 | 2 |
|  | MONTENEGRO | Euro | EUR | 978 | 2 |
|  | MONTSERRAT | East Caribbean Dollar | XCD | 951 | 2 |
|  | MOROCCO | Moroccan Dirham | MAD | 504 | 2 |
|  | MOZAMBIQUE | Mozambique Metical | MZN | 943 | 2 |
|  | MYANMAR | Kyat | MMK | 104 | 2 |
|  | NAMIBIA | Namibia Dollar | NAD | 516 | 2 |
|  | NAMIBIA | Rand | ZAR | 710 | 2 |
|  | NAURU | Australian Dollar | AUD | 036 | 2 |
|  | NEPAL | Nepalese Rupee | NPR | 524 | 2 |
|  | NETHERLANDS (THE) | Euro | EUR | 978 | 2 |
|  | NEW CALEDONIA | CFP Franc | XPF | 953 | 0 |
|  | NEW ZEALAND | New Zealand Dollar | NZD | 554 | 2 |
|  | NICARAGUA | Cordoba Oro | NIO | 558 | 2 |
|  | NIGER (THE) | CFA Franc BCEAO | XOF | 952 | 0 |
|  | NIGERIA | Naira | NGN | 566 | 2 |
|  | NIUE | New Zealand Dollar | NZD | 554 | 2 |
|  | NORFOLK ISLAND | Australian Dollar | AUD | 036 | 2 |
|  | NORTHERN MARIANA ISLANDS (THE) | US Dollar | USD | 840 | 2 |
|  | NORWAY | Norwegian Krone | NOK | 578 | 2 |
|  | OMAN | Rial Omani | OMR | 512 | 3 |
|  | PAKISTAN | Pakistan Rupee | PKR | 586 | 2 |
|  | PALAU | US Dollar | USD | 840 | 2 |
|  | PALESTINE, STATE OF | No universal currency |  |  |  |
|  | PANAMA | Balboa | PAB | 590 | 2 |
|  | PANAMA | US Dollar | USD | 840 | 2 |
|  | PAPUA NEW GUINEA | Kina | PGK | 598 | 2 |
|  | PARAGUAY | Guarani | PYG | 600 | 0 |
|  | PERU | Sol | PEN | 604 | 2 |
|  | PHILIPPINES (THE) | Philippine Peso | PHP | 608 | 2 |
|  | PITCAIRN | New Zealand Dollar | NZD | 554 | 2 |
|  | POLAND | Zloty | PLN | 985 | 2 |
|  | PORTUGAL | Euro | EUR | 978 | 2 |
|  | PUERTO RICO | US Dollar | USD | 840 | 2 |
|  | QATAR | Qatari Rial | QAR | 634 | 2 |
|  | RÉUNION | Euro | EUR | 978 | 2 |
|  | ROMANIA | Romanian Leu | RON | 946 | 2 |
|  | RUSSIAN FEDERATION (THE) | Russian Ruble | RUB | 643 | 2 |
|  | RWANDA | Rwanda Franc | RWF | 646 | 0 |
|  | SAINT BARTHÉLEMY | Euro | EUR | 978 | 2 |
|  | SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA | Saint Helena Pound | SHP | 654 | 2 |
|  | SAINT KITTS AND NEVIS | East Caribbean Dollar | XCD | 951 | 2 |
|  | SAINT LUCIA | East Caribbean Dollar | XCD | 951 | 2 |
|  | SAINT MARTIN (FRENCH PART) | Euro | EUR | 978 | 2 |
|  | SAINT PIERRE AND MIQUELON | Euro | EUR | 978 | 2 |
|  | SAINT VINCENT AND THE GRENADINES | East Caribbean Dollar | XCD | 951 | 2 |
|  | SAMOA | Tala | WST | 882 | 2 |
|  | SAN MARINO | Euro | EUR | 978 | 2 |
|  | SAO TOME AND PRINCIPE | Dobra | STN | 930 | 2 |
|  | SAUDI ARABIA | Saudi Riyal | SAR | 682 | 2 |
|  | SENEGAL | CFA Franc BCEAO | XOF | 952 | 0 |
|  | SERBIA | Serbian Dinar | RSD | 941 | 2 |
|  | SEYCHELLES | Seychelles Rupee | SCR | 690 | 2 |
|  | SIERRA LEONE | Leone | SLL | 694 | 2 |
|  | SINGAPORE | Singapore Dollar | SGD | 702 | 2 |
|  | SINT MAARTEN (DUTCH PART) | Netherlands Antillean Guilder | ANG | 532 | 2 |
|  | SISTEMA UNITARIO DE COMPENSACION REGIONAL DE PAGOS "SUCRE" | Sucre | XSU | 994 | N.A. |
|  | SLOVAKIA | Euro | EUR | 978 | 2 |
|  | SLOVENIA | Euro | EUR | 978 | 2 |
|  | SOLOMON ISLANDS | Solomon Islands Dollar | SBD | 090 | 2 |
|  | SOMALIA | Somali Shilling | SOS | 706 | 2 |
|  | SOUTH AFRICA | Rand | ZAR | 710 | 2 |
|  | SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS | No universal currency |  |  |  |
|  | SOUTH SUDAN | South Sudanese Pound | SSP | 728 | 2 |
|  | SPAIN | Euro | EUR | 978 | 2 |
|  | SRI LANKA | Sri Lanka Rupee | LKR | 144 | 2 |
|  | SUDAN (THE) | Sudanese Pound | SDG | 938 | 2 |
|  | SURINAME | Surinam Dollar | SRD | 968 | 2 |
|  | SVALBARD AND JAN MAYEN | Norwegian Krone | NOK | 578 | 2 |
|  | SWEDEN | Swedish Krona | SEK | 752 | 2 |
|  | SWITZERLAND | Swiss Franc | CHF | 756 | 2 |
|  | SWITZERLAND | WIR Euro | CHE | 947 | 2 |
|  | SWITZERLAND | WIR Franc | CHW | 948 | 2 |
|  | SYRIAN ARAB REPUBLIC | Syrian Pound | SYP | 760 | 2 |
|  | TAIWAN (PROVINCE OF CHINA) | New Taiwan Dollar | TWD | 901 | 2 |
|  | TAJIKISTAN | Somoni | TJS | 972 | 2 |
|  | TANZANIA, UNITED REPUBLIC OF | Tanzanian Shilling | TZS | 834 | 2 |
|  | THAILAND | Baht | THB | 764 | 2 |
|  | TIMOR-LESTE | US Dollar | USD | 840 | 2 |
|  | TOGO | CFA Franc BCEAO | XOF | 952 | 0 |
|  | TOKELAU | New Zealand Dollar | NZD | 554 | 2 |
|  | TONGA | Pa’anga | TOP | 776 | 2 |
|  | TRINIDAD AND TOBAGO | Trinidad and Tobago Dollar | TTD | 780 | 2 |
|  | TUNISIA | Tunisian Dinar | TND | 788 | 3 |
|  | TURKEY | Turkish Lira | TRY | 949 | 2 |
|  | TURKMENISTAN | Turkmenistan New Manat | TMT | 934 | 2 |
|  | TURKS AND CAICOS ISLANDS (THE) | US Dollar | USD | 840 | 2 |
|  | TUVALU | Australian Dollar | AUD | 036 | 2 |
|  | UGANDA | Uganda Shilling | UGX | 800 | 0 |
|  | UKRAINE | Hryvnia | UAH | 980 | 2 |
|  | UNITED ARAB EMIRATES (THE) | UAE Dirham | AED | 784 | 2 |
|  | UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND (THE) | Pound Sterling | GBP | 826 | 2 |
|  | UNITED STATES MINOR OUTLYING ISLANDS (THE) | US Dollar | USD | 840 | 2 |
|  | UNITED STATES OF AMERICA (THE) | US Dollar | USD | 840 | 2 |
|  | UNITED STATES OF AMERICA (THE) | US Dollar (Next day) | USN | 997 | 2 |
|  | URUGUAY | Peso Uruguayo | UYU | 858 | 2 |
|  | URUGUAY | Uruguay Peso en Unidades Indexadas (UI) | UYI | 940 | 0 |
|  | URUGUAY | Unidad Previsional | UYW | 927 | 4 |
|  | UZBEKISTAN | Uzbekistan Sum | UZS | 860 | 2 |
|  | VANUATU | Vatu | VUV | 548 | 0 |
|  | VENEZUELA (BOLIVARIAN REPUBLIC OF) | Bolívar Soberano | VES | 928 | 2 |
|  | VIET NAM | Dong | VND | 704 | 0 |
|  | VIRGIN ISLANDS (BRITISH) | US Dollar | USD | 840 | 2 |
|  | VIRGIN ISLANDS (U.S.) | US Dollar | USD | 840 | 2 |
|  | WALLIS AND FUTUNA | CFP Franc | XPF | 953 | 0 |
|  | WESTERN SAHARA | Moroccan Dirham | MAD | 504 | 2 |
|  | YEMEN | Yemeni Rial | YER | 886 | 2 |
|  | ZAMBIA | Zambian Kwacha | ZMW | 967 | 2 |
|  | ZIMBABWE | Zimbabwe Dollar | ZWL | 932 | 2 |

## Sheet: `Country Codes - ISO 3166-1`

_253 rows x 3 columns._

**DO NOT TOUCH**

**Country Codes - ISO 3166-1 alpha-2 code**

| col1 | Name | Code |
|---|---|---|
|  | Afghanistan | AF |
|  | √Öland Islands | AX |
|  | Albania | AL |
|  | Algeria | DZ |
|  | American Samoa | AS |
|  | Andorra | AD |
|  | Angola | AO |
|  | Anguilla | AI |
|  | Antarctica | AQ |
|  | Antigua and Barbuda | AG |
|  | Argentina | AR |
|  | Armenia | AM |
|  | Aruba | AW |
|  | Australia | AU |
|  | Austria | AT |
|  | Azerbaijan | AZ |
|  | Bahamas | BS |
|  | Bahrain | BH |
|  | Bangladesh | BD |
|  | Barbados | BB |
|  | Belarus | BY |
|  | Belgium | BE |
|  | Belize | BZ |
|  | Benin | BJ |
|  | Bermuda | BM |
|  | Bhutan | BT |
|  | Bolivia, Plurinational State of | BO |
|  | Bonaire, Sint Eustatius and Saba | BQ |
|  | Bosnia and Herzegovina | BA |
|  | Botswana | BW |
|  | Bouvet Island | BV |
|  | Brazil | BR |
|  | British Indian Ocean Territory | IO |
|  | Brunei Darussalam | BN |
|  | Bulgaria | BG |
|  | Burkina Faso | BF |
|  | Burundi | BI |
|  | Cambodia | KH |
|  | Cameroon | CM |
|  | Canada | CA |
|  | Cape Verde | CV |
|  | Cayman Islands | KY |
|  | Central African Republic | CF |
|  | Chad | TD |
|  | Chile | CL |
|  | China | CN |
|  | Christmas Island | CX |
|  | Cocos (Keeling) Islands | CC |
|  | Colombia | CO |
|  | Comoros | KM |
|  | Congo | CG |
|  | Congo, the Democratic Republic of the | CD |
|  | Cook Islands | CK |
|  | Costa Rica | CR |
|  | C√¥te d'Ivoire | CI |
|  | Croatia | HR |
|  | Cuba | CU |
|  | Cura√ßao | CW |
|  | Cyprus | CY |
|  | Czech Republic | CZ |
|  | Denmark | DK |
|  | Djibouti | DJ |
|  | Dominica | DM |
|  | Dominican Republic | DO |
|  | Ecuador | EC |
|  | Egypt | EG |
|  | El Salvador | SV |
|  | Equatorial Guinea | GQ |
|  | Eritrea | ER |
|  | Estonia | EE |
|  | Ethiopia | ET |
|  | Falkland Islands (Malvinas) | FK |
|  | Faroe Islands | FO |
|  | Fiji | FJ |
|  | Finland | FI |
|  | France | FR |
|  | French Guiana | GF |
|  | French Polynesia | PF |
|  | French Southern Territories | TF |
|  | Gabon | GA |
|  | Gambia | GM |
|  | Georgia | GE |
|  | Germany | DE |
|  | Ghana | GH |
|  | Gibraltar | GI |
|  | Greece | GR |
|  | Greenland | GL |
|  | Grenada | GD |
|  | Guadeloupe | GP |
|  | Guam | GU |
|  | Guatemala | GT |
|  | Guernsey | GG |
|  | Guinea | GN |
|  | Guinea-Bissau | GW |
|  | Guyana | GY |
|  | Haiti | HT |
|  | Heard Island and McDonald Islands | HM |
|  | Holy See (Vatican City State) | VA |
|  | Honduras | HN |
|  | Hong Kong | HK |
|  | Hungary | HU |
|  | Iceland | IS |
|  | India | IN |
|  | Indonesia | ID |
|  | Iran, Islamic Republic of | IR |
|  | Iraq | IQ |
|  | Ireland | IE |
|  | Isle of Man | IM |
|  | Israel | IL |
|  | Italy | IT |
|  | Jamaica | JM |
|  | Japan | JP |
|  | Jersey | JE |
|  | Jordan | JO |
|  | Kazakhstan | KZ |
|  | Kenya | KE |
|  | Kiribati | KI |
|  | Korea, Democratic People's Republic of | KP |
|  | Korea, Republic of | KR |
|  | Kuwait | KW |
|  | Kyrgyzstan | KG |
|  | Lao People's Democratic Republic | LA |
|  | Latvia | LV |
|  | Lebanon | LB |
|  | Lesotho | LS |
|  | Liberia | LR |
|  | Libya | LY |
|  | Liechtenstein | LI |
|  | Lithuania | LT |
|  | Luxembourg | LU |
|  | Macao | MO |
|  | Macedonia, the Former Yugoslav Republic of | MK |
|  | Madagascar | MG |
|  | Malawi | MW |
|  | Malaysia | MY |
|  | Maldives | MV |
|  | Mali | ML |
|  | Malta | MT |
|  | Marshall Islands | MH |
|  | Martinique | MQ |
|  | Mauritania | MR |
|  | Mauritius | MU |
|  | Mayotte | YT |
|  | Mexico | MX |
|  | Micronesia, Federated States of | FM |
|  | Moldova, Republic of | MD |
|  | Monaco | MC |
|  | Mongolia | MN |
|  | Montenegro | ME |
|  | Montserrat | MS |
|  | Morocco | MA |
|  | Mozambique | MZ |
|  | Myanmar | MM |
|  | Namibia | NA |
|  | Nauru | NR |
|  | Nepal | NP |
|  | Netherlands | NL |
|  | New Caledonia | NC |
|  | New Zealand | NZ |
|  | Nicaragua | NI |
|  | Niger | NE |
|  | Nigeria | NG |
|  | Niue | NU |
|  | Norfolk Island | NF |
|  | Northern Mariana Islands | MP |
|  | Norway | NO |
|  | Oman | OM |
|  | Pakistan | PK |
|  | Palau | PW |
|  | Palestine, State of | PS |
|  | Panama | PA |
|  | Papua New Guinea | PG |
|  | Paraguay | PY |
|  | Peru | PE |
|  | Philippines | PH |
|  | Pitcairn | PN |
|  | Poland | PL |
|  | Portugal | PT |
|  | Puerto Rico | PR |
|  | Qatar | QA |
|  | R√©union | RE |
|  | Romania | RO |
|  | Russian Federation | RU |
|  | Rwanda | RW |
|  | Saint Barthelemy | BL |
|  | Saint Helena, Ascension and Tristan da Cunha | SH |
|  | Saint Kitts and Nevis | KN |
|  | Saint Lucia | LC |
|  | Saint Martin (French part) | MF |
|  | Saint Pierre and Miquelon | PM |
|  | Saint Vincent and the Grenadines | VC |
|  | Samoa | WS |
|  | San Marino | SM |
|  | Sao Tome and Principe | ST |
|  | Saudi Arabia | SA |
|  | Senegal | SN |
|  | Serbia | RS |
|  | Seychelles | SC |
|  | Sierra Leone | SL |
|  | Singapore | SG |
|  | Sint Maarten (Dutch part) | SX |
|  | Slovakia | SK |
|  | Slovenia | SI |
|  | Solomon Islands | SB |
|  | Somalia | SO |
|  | South Africa | ZA |
|  | South Georgia and the South Sandwich Islands | GS |
|  | South Sudan | SS |
|  | Spain | ES |
|  | Sri Lanka | LK |
|  | Sudan | SD |
|  | Suriname | SR |
|  | Svalbard and Jan Mayen | SJ |
|  | Swaziland | SZ |
|  | Sweden | SE |
|  | Switzerland | CH |
|  | Syrian Arab Republic | SY |
|  | Taiwan, Province of China | TW |
|  | Tajikistan | TJ |
|  | Tanzania, United Republic of | TZ |
|  | Thailand | TH |
|  | Timor-Leste | TL |
|  | Togo | TG |
|  | Tokelau | TK |
|  | Tonga | TO |
|  | Trinidad and Tobago | TT |
|  | Tunisia | TN |
|  | Turkey | TR |
|  | Turkmenistan | TM |
|  | Turks and Caicos Islands | TC |
|  | Tuvalu | TV |
|  | Uganda | UG |
|  | Ukraine | UA |
|  | United Arab Emirates | AE |
|  | United Kingdom | GB |
|  | United States | US |
|  | United States Minor Outlying Islands | UM |
|  | Uruguay | UY |
|  | Uzbekistan | UZ |
|  | Vanuatu | VU |
|  | Venezuela, Bolivarian Republic of | VE |
|  | Viet Nam | VN |
|  | Virgin Islands, British | VG |
|  | Virgin Islands, U.S. | VI |
|  | Wallis and Futuna | WF |
|  | Western Sahara | EH |
|  | Yemen | YE |
|  | Zambia | ZM |
|  | Zimbabwe | ZW |


# Annex - Data Dictionary build log

## FR-DD-001-v1.0 — build log

**Artifact:** `FR-compliance/05-data-dictionary/FR-DD-001-v1.0.xlsx`
**Template:** `shared/CZ_Data_Dictionary_V2_0.xlsx` (loaded and repopulated — not recreated)
**Built:** 2026-08-27
**Scope version:** scope_manifest.json 1.0, locked 2026-08-26

### Contents

| Sheet | Rows written | Note |
|---|---|---|
| Version Control | header updated | country set to France, Czech 2.0 revision row cleared |
| Introduction | unchanged | generic, no country reference |
| Instructions | unchanged | generic, contains no country name |
| ID Information | 25 | 5 employee + 20 employer identifiers |
| Country Fields | 164 | 122 employee + 42 legal entity |
| Country Option Mappers | 54 mappers / 303 codes | each group preceded by its own header row, per CZ convention |
| Currency Codes — ISO 4217 | untouched | |
| Country Codes — ISO 3166-1 | untouched | |

**189 fields** in total.

### Column discipline

Verified programmatically against the template: all ten ORANGE (FF9900) columns on
ID Information and all ten on Country Fields are empty, and every BLUE (4472C4)
column is populated. Sheet order, fills, column widths and the `E1` freeze pane on
ID Information are identical to the template.

One column was **added**: `Country Option Mappers!G` "Notes", styled from its blue
neighbour. The CZ template has no Notes column on that sheet, but C14 requires the
constraint on a conditional mapper to be recorded somewhere; inventing the record
elsewhere would have been worse than adding the column.

### Sources

| Source | Use |
|---|---|
| NEODeS cahier technique CT2026.1.2 (P26V01, rev. 20251224), GIP-MDS | 49 of the 54 option mappers; all code values and French local names reproduced verbatim |
| FR-CCG-001-v1.0 modules m02, m05, m07 | Tax Residence Status, Health Cover Exemption Reason, Wage Attachment Type, Personal Identifier Type |
| FR-CPAM-002 form S6200 (Cerfa 14463) | Nationality Band — the three bands printed on the form |
| FR-compliance/04-reports-spec/ (15 specs) | field alignment cross-check |

**Zero invented codes.** All 303 option codes were checked against the norm: every
code belonging to a mapper with a DSN rubrique exists in that rubrique's value list.
The five mappers with no DSN enumeration behind them are named explicitly in
`fr_dd_data_mappers.py` with their non-DSN source.

All 303 codes carry a French local name; the 287 the content module did not supply
were looked up verbatim from NEODeS by (rubrique, code) at build time.

### Private-sector and régime-général filter

Applied per the DD mandate and per `shared/FR_regime_scope_note.txt`, which locks
this build to the **régime général** only (scope owner, 26 Aug 2026). Every removed
code is retained in the module's `excluded` list rather than deleted silently.

Representative effects:

- **Contract Nature** — 9 of 26 kept; public-law contracts, all `[FP]` codes, public-service appointment and maritime engagement removed.
- **Employment Status** — 3 of 12 kept; all `[FP]` codes, state industrial workers, military and hospital medical staff removed.
- **Old-age / sickness / accident scheme codes** — reduced to the régime général; RATP, ENIM, CNBF, CRPCEN, CAVIMAC, CNIEG/CAMIEG and MSA removed as descoped régimes spéciaux.
- **Employer Legal Nature** — public bodies removed.

### C14 — option mapper completeness

Every mapper has, for every code, a code value, an English abbreviation, a French
local name and an English description. **29 mappers** are referenced by at least one
Conditional Mandatory field; for each, the referencing field's pre-condition is
appended verbatim to the mapper's Notes cell at build time, so the constraint cannot
drift from the field that imposes it.

Referential integrity is exact: 54 mappers referenced by fields, 54 defined, no
orphans in either direction.

### Checks run

- sheet order identical to template — pass
- orange columns empty / blue columns populated — pass
- option codes stored as text, 197 leading-zero codes preserved — pass
- no Czech residue in any populated sheet — pass
- no residual markers (TODO/TBD/RESEARCH-GAP/NOT FOUND) — pass
- scope sweep for banned content (base salary, gross/net, rates, ceilings, authority-generated, per-payrun) — 0 hits
- zip integrity — pass

### Open item for the scope owner

**Employee share schemes (actionnariat salarié — S89.G00.87/88/89).** The report
specs classify **30 rubriques** in this block as payroll master data of type *Input*
— award date, vesting date, number of shares, unit value, acquisition price. None of
them are in this Data Dictionary, and `scope_manifest.json` does not explicitly
descope them.

They were left out because they are per-award event data reported annually through
the DGFiP S89 flow rather than employee master data, and because the amount-bearing
members of the set (unit value, acquisition price) are excluded by the DD mandate
outright. That is a defensible reading but it is a scope call, not a technical one,
so it is flagged here rather than decided unilaterally. If the owner rules them in,
the non-amount members are the ones that would be added.

The other 118 uncited DD-bucket rubriques were reviewed and are correctly out of
scope: the DSN "Changement" blocks (S21.G00.41, .31, .16, .72 — 58 rubriques) mirror
master-data fields already present and are produced by comparing successive states;
the rest are work-stoppage, suspension, SATD and attachment-year rubriques that are
transactional, calculated or authority-generated.


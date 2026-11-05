# US-IRS-006-Form1042S-Spec


## Version Control

|  | Statutory Report Specification |  |  |  |  |
|---|---|---|---|---|---|
|  | United States of America |  |  |  |  |
|  | US-IRS-006 Form 1042-S Treaty-Exempt Wages of Nonresident Aliens |  |  |  |  |
|  | Document ID | US-IRS-006 |  |  |  |
|  | Version | Effective Date | Change Description | Status | Updated By |
|  | 1.0 | 2027-03-31 00:00:00 | For QA. | For QA | Wallisson Gomes |
|  | REMARKS |  |  |  |  |
|  | Topic | Remark |  |  |  |
|  | Scope | One Report Specification per authority return in scope for the United States package v1.0. Field-level definitions of master data are owned by the Data Dictionary US-DD-001 v1.0; rules and rates by the Country Configuration Guide US-CCG-001 v1.0. |  |  |  |
|  | Channel | Every return is transmitted by the third-party filing provider acting as reporting agent (Form 8655 for federal returns). The payroll produces the data set of the field model; the provider maps it to the authority wire format. |  |  |  |
|  | Limitations | Open points are written in place with an open-point reference and listed in the Report Matrix accuracy note. No value is assumed where the official source has not been read. |  |  |  |

## Report Matrix

| US-IRS-006 FORM 1042-S TREATY-EXEMPT WAGES OF NONRESIDENT ALIENS |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| Document ID | US-IRS-006 |  |  |  |  |  |  |  |  |
| Document Title | US-IRS-006 Form 1042-S Treaty-Exempt Wages of Nonresident Aliens |  |  |  |  |  |  |  |  |
| Country | United States of America |  |  |  |  |  |  |  |  |
| Authority | Internal Revenue Service (IRS), U.S. Department of the Treasury |  |  |  |  |  |  |  |  |
| Report Type | Outbound statutory return (employer to authority, through the filing provider hand-off) |  |  |  |  |  |  |  |  |
| Tax Type | Federal income tax treaty exemption reporting |  |  |  |  |  |  |  |  |
| Relationship | Excluded wages do not enter the W-2 wage box (US-SSA-001) |  |  |  |  |  |  |  |  |
| Frequency | Annual |  |  |  |  |  |  |  |  |
| Submission Deadline | IRIS (FIRE retired for TY2026); due 2027-03-15 |  |  |  |  |  |  |  |  |
| File Format | Electronic filing through IRIS. FIELD MODEL: logical model - not the wire/submission format. |  |  |  |  |  |  |  |  |
| File Extension | Provider-defined (logical field model) |  |  |  |  |  |  |  |  |
| Character Encoding | Provider-defined |  |  |  |  |  |  |  |  |
| Record Length | Not applicable (logical field model) |  |  |  |  |  |  |  |  |
| Record Types / Sections | Withholding agent; Recipient; Amounts; Box codes |  |  |  |  |  |  |  |  |
| Version | 1.0 |  |  |  |  |  |  |  |  |
| Created Date | 2027-03-31 |  |  |  |  |  |  |  |  |
| Created By | Mercans Compliance Regulations Team |  |  |  |  |  |  |  |  |
| Official Source | https://www.irs.gov/pub/irs-pdf/p515.pdf [US-FEDS5-016] |  |  |  |  |  |  |  |  |
| Last Update Reference | Publication 515 as read for this release |  |  |  |  |  |  |  |  |
| Similar To | US-SSA-001 Forms W-2/W-3 |  |  |  |  |  |  |  |  |
| ═══ REPORT MATRIX ═══ |  |  |  |  |  |  |  |  |  |
| Report ID | Report Name (EN) | Report Name (Local) | Authority | Frequency | Due Date Rule | Submission Method | File Format | Legal Basis | Accuracy Assessment |
| US-IRS-006 | Form 1042-S, Foreign Person's U.S. Source Income Subject to Withholding (treaty-exempt wages) | Form 1042-S | Internal Revenue Service (IRS) | Annual | IRIS (FIRE retired for TY2026); due 2027-03-15 | file_upload: electronic filing through IRIS by the reporting agent | Electronic filing through IRIS (IRIS (FIRE retired for TY2026); due 2027-03-15). FIELD MODEL: logical model - not the wire/submission format. | [US-FEDS5-016]; https://www.irs.gov/pub/irs-pdf/p515.pdf | Channel: file_upload \| Portal: IRS IRIS \| Source: https://www.irs.gov/pub/irs-pdf/p515.pdf \| CONFIRMED (channel and box codes), TO CONFIRM (code pairing for wages). Accuracy 80% (rule, channel and box codes read; pairing for wages applied from the instruction text). Closes with: one accepted real filing for a treaty-exempt employee. |

## Payroll Scope Summary

| US-IRS-006 FORM 1042-S TREATY-EXEMPT WAGES OF NONRESIDENT ALIENS — PAYROLL SCOPE SUMMARY |  |  |
|---|---|---|
| Nonresident alien employees whose wages are exempt under a tax treaty claimed on Form 8233. |  |  |
| SCENARIO | REPORT? | NOTES / REASONING |
| ═══ WHO GETS REPORTED ═══ |  |  |
| Nonresident aliens with an accepted Form 8233 treaty claim | YES | Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S (not W-2 box 1); 2026 Forms 1042-S due 2027-03-15 and must be e-filed via IRIS |
| Nonresident aliens without a treaty claim | NO | Their wages go on Form W-2 (US-SSA-001). |
| ═══ TIMING & RELATIONSHIP ═══ |  |  |
| Annual filing through IRIS | YES | IRIS (FIRE retired for TY2026); due 2027-03-15 |
| ═══ AMOUNTS & CALCULATIONS ═══ |  |  |
| Treaty-exempt wages | YES | Row F1042S-005. |
| ═══ SPECIAL CASES ═══ |  |  |
| Recipient becomes a resident alien during the year | PARTIAL | Only pay while a nonresident alien with the treaty claim is reported here. |

## Form 1042-S Spec

| Field Name (EN) | Field Name (Authority label, EN) | Record Type | Field Position | Payroll Field (Y/N) | Mandatory (Y/N/C) | Conditional Reason | Position (Start-End) | Field Length | Format | Example | System Mapping | Field Explanation | Relevant for Payroll | Option Values | Rounding | Negative (Y/N) | Value Type | Reporting Frequency | Query to RA | RA Comments |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ═══ WITHHOLDING AGENT AND RECIPIENT ═══ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Employer Identification Number (EIN) | Employer identification number | Header (employer) | F1042S-001 | Y | Y | Not conditional: every return identifies the employer. | Logical field (field model) | 9 digits | NN-NNNNNNN | 12-3456789 (fictitious) | US-DD-001 v1.0: Employer Identification Number (EIN) | The employer's federal identification number, nine-digit number issued by the IRS, arranged 00-0000000 [US-FEDS5-029]. It identifies the employer on the Form 1042-S and must equal the EIN on every other federal return of the same employer. Never truncated. [US-FEDS5-029] Source type: Web research (official authority page). https://www.irs.gov/pub/irs-pdf/p15.pdf | Yes: employer master data | Not applicable | Not applicable | N | Input (Identifier) | Per return | No open query. |  |
| Employer legal name and address | Name and address | Header (employer) | F1042S-002 | Y | Y | Not conditional: every return identifies the employer. | Logical field (field model) | Text | Text | Example Holdings Inc., 100 Main St, Springfield | US-DD-001 v1.0: Employer legal name \| Employer address location line \| Employer address delivery line \| Employer address city \| Employer address State \| Employer address ZIP code \| Employer address ZIP code extension \| Employer address foreign State or province \| Employer address foreign postal code \| Employer address country | Legal name and mailing address of the employer as registered with the IRS for the Form 1042-S. Taken from employer master data; a change of address is reported by the employer through the IRS channel, not by a payroll field. Source: US-CCG-001 v1.0 Module 2 (employer registration). | Yes: employer master data | Not applicable | Not applicable | N | Input (Text) | Per return | No open query. |  |
| Recipient nonresident alien flag and treaty claim | Recipient status | Recipient | F1042S-003 | Y | Y | Not conditional: only flagged recipients enter the return. | Logical field (field model) | 1 | Flag | Y | US-DD-001 v1.0: Nonresident alien flag \| Form 8233 treaty exemption claimed | nonresident alien flag + Notice 1392 W-4 and Form 8233 treaty exemption (exempt wages to 1042-S, not W-2 box 1) [US-FEDS5-016]. Only treaty-exempt wages claimed on Form 8233 are reported here: Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S (not W-2 box 1); 2026 Forms 1042-S due 2027-03-15 and must be e-filed via IRIS. The flag and the treaty claim are employee master data in the Data Dictionary, one character Y / N; only recipients flagged Y enter the return. Wages without a Form 8233 claim on file do not enter this return. [US-FEDS5-016] Source type: Web research (official authority page). https://www.irs.gov/pub/irs-pdf/p515.pdf | Yes: selects the population | Y / N | Not applicable | N | Input (Flag) | Annual | No open query. |  |
| Recipient visa class | Immigration status | Recipient | F1042S-004 | Y | Y | Not conditional. | Logical field (field model) | Text | Code | J-1 | US-DD-001 v1.0: Nonresident alien visa class | Immigration status of the nonresident alien recipient, held in the Data Dictionary: Immigration status for nonresident aliens: visa class (F-1, J-1, M-1, Q-1, other), whether the work carries out the purpose of admission (incl. authorised CPT/OPT), and resident/nonresident alien status; drives the FICA (IRC 3121(b)(19)) and FUTA (IRC 3306(c)(19)) exemption flags. [US-FEDR2-001] [US-FEDS5-016] [US-FEDR2-002]. It is written as the visa class code of Field Options and decides which exemptions the payroll applied to the wages reported on Form 1042-S (FICA and FUTA exemption flags of the Data Dictionary). One code per recipient, as held in master data. | Yes: recipient classification | See Field Options | Not applicable | N | Input (Code) | Annual | No open query. |  |
| Treaty-exempt wages paid in the year | Gross income | Amounts | F1042S-005 | Y | Y | Not conditional. | Logical field (field model) | Amount | Decimal 13.2 | 24,000.00 | Payroll result: treaty-exempt wage accumulator | Wages exempt under a treaty claim; excluded from the W-2 wage box (US-SSA-001) [US-FEDS5-016]. FICA treatment follows the visa class (US-IRS-001 row F941-015). | Yes: annual amount | Not applicable | Cents (2 decimals) | N | Input (Amount) | Annual | No open query. |  |
| ═══ FORM 1042-S BOX CODES FOR TREATY-EXEMPT WAGES ═══ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Box codes for treaty-exempt wages (source) | Box codes | Box codes | F1042S-006 | N | Y | Not conditional. | Not applicable | Not applicable | Text | See rows F1042S-007 to F1042S-011 | Return generator code table (system constant) | Box codes for treaty-exempt wages, as read: Treaty-exempt wages of a nonresident alien employee: Box 1 income code 18 (compensation for dependent personal services) (also 19 teaching, 20 studying/training, 42/43 artist/athlete); Box 3 chapter indicator '3'; Box 3a ch.3 exemption code 04 (exempt or reduced withholding under tax treaty), 3b rate 00.00 (or treaty rate); Box 4a ch.4 exemption code 16 (excluded nonfinancial payment, Reg. 1.1473-1(a)(4)(iii)), 4b 00.00; Box 5 withholding allowance only where the treaty exempts up to a specific amount (then Box 6 net income); Box 13b recipient country code must be a treaty country when 3a=04; Box 13j ch.3 status 16 (individual), 13k ch.4 status 23 (individual). No treaty-article box on Form 1042-S (article is documented on Form 8233); Box 13n LOB code applies to entity recipients only. [US-FEDS6-005]. Rows F1042S-007 to F1042S-011 give each box. [US-FEDS6-005] Source type: Official spec. https://www.irs.gov/pub/irs-pdf/i1042s.pdf | Yes: completeness of the return | See Field Options | Not applicable | N | Display-only (Text) | Annual | Confirm against a real filing: the pairing of the chapter 4 code and the status codes for wages is applied from the instruction text [US-FEDS6-005]. |  |
| Box 1: Income code | Income code | Box codes | F1042S-007 | N | Y | Not conditional. | Box 1 | Code | Code | 18 | Return generator code table (system constant) | Box 1: Income code for compensation for dependent personal services of a nonresident alien employee. Teaching, studying or training and artist or athlete income use the other codes listed in row F1042S-006. Code: 18. [US-FEDS6-005] Source type: Official spec. https://www.irs.gov/pub/irs-pdf/i1042s.pdf | Yes: box of the return | See Field Options | Not applicable | N | Input (Code) | Annual | No open query. |  |
| Boxes 3, 3a, 3b: Chapter 3 exemption code and rate | Chapter 3 exemption code and rate | Box codes | F1042S-008 | N | Y | Not conditional. | Boxes 3, 3a, 3b | Code | Code | 04 | Return generator code table (system constant) | Boxes 3, 3a, 3b: Chapter 3 exemption code for income exempt or reduced under a tax treaty, with the chapter indicator and the withholding rate as stated in row F1042S-006. Code: 04. The code is a constant of the return generator code table and is written on every line of treaty-exempt wages; the rate box follows row F1042S-006. [US-FEDS6-005] Source type: Official spec. https://www.irs.gov/pub/irs-pdf/i1042s.pdf | Yes: box of the return | See Field Options | Not applicable | N | Input (Code) | Annual | No open query. |  |
| Boxes 4a, 4b: Chapter 4 exemption code and rate | Chapter 4 exemption code and rate | Box codes | F1042S-009 | N | Y | Not conditional. | Boxes 4a, 4b | Code | Code | 16 | Return generator code table (system constant) | Boxes 4a, 4b: Chapter 4 exemption code for an excluded nonfinancial payment, with the rate as stated in row F1042S-006. Code: 16. The code is a constant of the return generator code table and is written on every line of treaty-exempt wages of the return. [US-FEDS6-005] Source type: Official spec. https://www.irs.gov/pub/irs-pdf/i1042s.pdf | Yes: box of the return | See Field Options | Not applicable | N | Input (Code) | Annual | No open query. |  |
| Boxes 13b, 13j, 13k: Recipient country and status codes | Recipient country and status codes | Box codes | F1042S-010 | Y | Y | Not conditional. | Boxes 13b, 13j, 13k | Code | Code | As held | US-DD-001 v1.0: Nonresident alien country of residence \| Form 8233 treaty exemption claimed | Boxes 13b, 13j, 13k: Recipient country code (a treaty country when the chapter 3 exemption code is the treaty code) and the chapter 3 / chapter 4 status codes of an individual, as stated in row F1042S-006. The treaty article is documented on Form 8233, not on Form 1042-S. Code: See row F1042S-006. [US-FEDS6-005] Source type: Official spec. https://www.irs.gov/pub/irs-pdf/i1042s.pdf | Yes: box of the return | Not applicable | Not applicable | N | Input (Code) | Annual | Confirm against a real filing: the pairing of the chapter 4 code and the status codes for wages is applied from the instruction text [US-FEDS6-005]. |  |
| Boxes 5, 6: Withholding allowance and net income | Withholding allowance and net income | Box codes | F1042S-011 | Y | C | Only when the treaty exempts up to a specific amount; back-reference to F1042S-005. | Boxes 5, 6 | Code | Code | As held | US-DD-001 v1.0: Nonresident alien country of residence \| Form 8233 treaty exemption claimed | Boxes 5, 6: Used only where the treaty exempts income up to a specific amount: the allowance goes in box 5 and the net income in box 6, as stated in row F1042S-006. Code: See row F1042S-006. [US-FEDS6-005] Source type: Official spec. https://www.irs.gov/pub/irs-pdf/i1042s.pdf | Yes: box of the return | Not applicable | Not applicable | N | Input (Code) | Annual | Confirm against a real filing: the pairing of the chapter 4 code and the status codes for wages is applied from the instruction text [US-FEDS6-005]. |  |

## File Structure

| US-IRS-006 Form 1042-S Treaty-Exempt Wages of Nonresident Aliens — FILE STRUCTURE AND TECHNICAL SPECIFICATIONS |
|---|
| ═══ FILE FORMAT ═══ |
| Electronic filing through IRIS (IRIS (FIRE retired for TY2026); due 2027-03-15). |
| FIELD MODEL: logical model - not the wire/submission format. |
| Box codes: rows F1042S-006 to F1042S-011. |
| FORMAT TO CONFIRM vs a real filing. |
| ═══ BOX CODES (wages) ═══ |
| As read: Treaty-exempt wages of a nonresident alien employee: Box 1 income code 18 (compensation for dependent personal services) (also 19 teaching, 20 studying/training, 42/43 artist/athlete); Box 3 chapter indicator '3'; Box 3a ch.3 exemption code 04 (exempt or reduced withholding under tax treaty), 3b rate 00.00 (or treaty rate); Box 4a ch.4 exemption code 16 (excluded nonfinancial payment, Reg. 1.1473-1(a)(4)(iii)), 4b 00.00; Box 5 withholding allowance only where the treaty exempts up to a specific amount (then Box 6 net income); Box 13b recipient country code must be a treaty country when 3a=04; Box 13j ch.3 status 16 (individual), 13k ch.4 status 23 (individual). No treaty-article box on Form 1042-S (article is documented on Form 8233); Box 13n LOB code applies to entity recipients only. [US-FEDS6-005] |

## Field Options

| Field Name | Option Code | Description (EN) | Description (Authority wording, EN) | Authority Reference |
|---|---|---|---|---|
| ═══ VISA CLASS (F1042S-004) ═══ |  |  |  |  |
| Visa class | Per Data Dictionary | Immigration status for nonresident aliens: visa class (F-1, J-1, M-1, Q-1, other), whether the work carries out the purpose of admission (incl. authorised CPT/OPT), and resident/nonresident alien status; drives the FICA (IRC 3121(b)(19)) and FUTA (IRC 3306(c)(19)) exemption flags. | Visa class as issued | [US-FEDR2-001] |
| ═══ BOX CODES FOR TREATY-EXEMPT WAGES (F1042S-007 to F1042S-009) ═══ |  |  |  |  |
| Box 1 income code | 18 | Compensation for dependent personal services | Income code | [US-FEDS6-005] |
| Box 3a chapter 3 exemption code | 04 | Exempt or reduced withholding under a tax treaty | Exemption code | [US-FEDS6-005] |
| Box 4a chapter 4 exemption code | 16 | Excluded nonfinancial payment | Exemption code | [US-FEDS6-005] |

## Population Rules

| Rule Category | Field Name | Source System | Population Logic | Edge Cases |
|---|---|---|---|---|
| ═══ PAYROLL-SPECIFIC POPULATION RULES ═══ |  |  |  |  |
| Conditional | F1042S-005 treaty-exempt wages | NRA flag; Form 8233 claim | Accumulate only the wages covered by an accepted treaty claim while the employee is a nonresident alien; the same pay is excluded from the W-2 wage box and never reported twice. | A claim that exceeds the treaty limit during the year stops at the limit; pay above it goes to Form W-2. |
| Conditional | F1042S-011 withholding allowance | Treaty claim (Form 8233) | Fill the allowance and net income boxes only when the treaty exempts income up to a specific amount; for a full exemption the gross income box carries the treaty-exempt wages and the allowance box stays empty. | A treaty limit reached during the year moves the excess to Form W-2 and leaves the allowance at the limit. |

## Example Analysis

| US-IRS-006 Form 1042-S Treaty-Exempt Wages of Nonresident Aliens — EXAMPLE FILE ANALYSIS |  |  |  |
|---|---|---|---|
| Raw Value | Field Name | Interpretation | Notes |
| ═══ WORKED EXAMPLE: ROUTING OF A TREATY CLAIM (constructed) ═══ |  |  |  |
| 24,000.00 | Wages of a J-1 researcher with a Form 8233 treaty claim | Constructed input | Input |
| 24,000.00 | Form 1042-S amount (F1042S-005) | Treaty-exempt wages | Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S (not W-2 box 1); 2026 Forms 1042-S due 2027-03-15 and must be e-filed via IRIS |
| 0.00 | W-2 federal wages for the same pay | Excluded from the W-2 wage box | No double reporting |

## Sample File

| US-IRS-006 Form 1042-S Treaty-Exempt Wages of Nonresident Aliens — SAMPLE FILE |
|---|
| No official sample is held and none is constructed. Verified channel: electronic filing through IRIS by the reporting agent. The provider produces the transmission from the field model. |


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `dd.fed.nra.flag` | nonresident alien flag + Notice 1392 W-4 and Form 8233 treaty exemption (exempt wages to 1042-S, not W-2 box 1) | from 2026-01-01 | US-FEDS5-016 |
| `dd.fed.nra.visa_class` | Immigration status for nonresident aliens: visa class (F-1, J-1, M-1, Q-1, other), whether the work carries out the purpose of admission (incl. authorised CPT/OPT), and resident/nonresident alien status; drives the FICA (IRC 3121(b)(19)) and FUTA (IRC 3306(c)(19)) exemption flags. | from 2026-01-01 | US-FEDR2-001 |
| `fed.ein.format` | nine-digit number issued by the IRS, arranged 00-0000000 | from 2026-01-01 | US-FEDS5-029 |
| `fed.fit.nra.treaty_exempt.reporting` | Treaty-exempt wages claimed on Form 8233 are reported on Form 1042-S (not W-2 box 1); 2026 Forms 1042-S due 2027-03-15 and must be e-filed via IRIS | from 2026-01-01 | US-FEDS5-016 |
| `fed.form1042s.channel` | IRIS (FIRE retired for TY2026); due 2027-03-15 | from 2026-01-01 | US-FEDS5-016 |
| `rspec.fed.form1042s.ch3_exemption_code.treaty` | 04 | from 2026-01-01 | US-FEDS6-005 |
| `rspec.fed.form1042s.ch4_exemption_code.excluded_nonfinancial` | 16 | from 2026-01-01 | US-FEDS6-005 |
| `rspec.fed.form1042s.income_code.dependent_personal_services` | 18 | from 2026-01-01 | US-FEDS6-005 |
| `rspec.fed.form1042s.wage_codes` | Treaty-exempt wages of a nonresident alien employee: Box 1 income code 18 (compensation for dependent personal services) (also 19 teaching, 20 studying/training, 42/43 artist/athlete); Box 3 chapter indicator '3'; Box 3a ch.3 exemption code 04 (exempt or reduced withholding under tax treaty), 3b rate 00.00 (or treaty rate); Box 4a ch.4 exemption code 16 (excluded nonfinancial payment, Reg. 1.1473-1(a)(4)(iii)), 4b 00.00; Box 5 withholding allowance only where the treaty exempts up to a specific amount (then Box 6 net income); Box 13b recipient country code must be a treaty country when 3a=04; Box 13j ch.3 status 16 (individual), 13k ch.4 status 23 (individual). No treaty-article box on Form 1042-S (article is documented on Form 8233); Box 13n LOB code applies to entity recipients only. | from 2026-01-01 | US-FEDS6-005 |

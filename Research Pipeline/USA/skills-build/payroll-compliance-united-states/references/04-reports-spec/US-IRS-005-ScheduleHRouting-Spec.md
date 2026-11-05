# US-IRS-005-ScheduleHRouting-Spec


## Version Control

|  | Statutory Report Specification |  |  |  |  |
|---|---|---|---|---|---|
|  | United States of America |  |  |  |  |
|  | US-IRS-005 Schedule H Routing (Household Employees) |  |  |  |  |
|  | Document ID | US-IRS-005 |  |  |  |
|  | Version | Effective Date | Change Description | Status | Updated By |
|  | 1.0 | 2027-03-31 00:00:00 | For QA. | For QA | Wallisson Gomes |
|  | REMARKS |  |  |  |  |
|  | Topic | Remark |  |  |  |
|  | Scope | One Report Specification per authority return in scope for the United States package v1.0. Field-level definitions of master data are owned by the Data Dictionary US-DD-001 v1.0; rules and rates by the Country Configuration Guide US-CCG-001 v1.0. |  |  |  |
|  | Channel | Every return is transmitted by the third-party filing provider acting as reporting agent (Form 8655 for federal returns). The payroll produces the data set of the field model; the provider maps it to the authority wire format. |  |  |  |
|  | Limitations | Open points are written in place with an open-point reference and listed in the Report Matrix accuracy note. No value is assumed where the official source has not been read. |  |  |  |

## Report Matrix

| US-IRS-005 SCHEDULE H ROUTING (HOUSEHOLD EMPLOYEES) |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| Document ID | US-IRS-005 |  |  |  |  |  |  |  |  |
| Document Title | US-IRS-005 Schedule H Routing (Household Employees) |  |  |  |  |  |  |  |  |
| Country | United States of America |  |  |  |  |  |  |  |  |
| Authority | Internal Revenue Service (IRS), U.S. Department of the Treasury |  |  |  |  |  |  |  |  |
| Report Type | Outbound statutory return (employer to authority, through the filing provider hand-off) |  |  |  |  |  |  |  |  |
| Tax Type | Household employment taxes (reported by the household employer) |  |  |  |  |  |  |  |  |
| Relationship | Excluded from Form 941 (US-IRS-001) and Form 940 (US-IRS-004) |  |  |  |  |  |  |  |  |
| Frequency | Annual |  |  |  |  |  |  |  |  |
| Submission Deadline | With the household employer's personal return: 2027-04-15 (with the 2026 Form 1040/1040-SR/1040-SS/1040-NR/1041; extension of the return extends Schedule H; stand-alone if no return) |  |  |  |  |  |  |  |  |
| File Format | Routing flag only: household-employee wages are reported by the household employer on Schedule H. Not a file produced by the payroll. |  |  |  |  |  |  |  |  |
| File Extension | Provider-defined (logical field model) |  |  |  |  |  |  |  |  |
| Character Encoding | Provider-defined |  |  |  |  |  |  |  |  |
| Record Length | Not applicable (logical field model) |  |  |  |  |  |  |  |  |
| Record Types / Sections | Routing flag; coverage tests; annual statement to the household employer |  |  |  |  |  |  |  |  |
| Version | 1.0 |  |  |  |  |  |  |  |  |
| Created Date | 2027-03-31 |  |  |  |  |  |  |  |  |
| Created By | Mercans Compliance Regulations Team |  |  |  |  |  |  |  |  |
| Official Source | [US-FEDS5-029] [US-FEDS6-010] |  |  |  |  |  |  |  |  |
| Last Update Reference | Schedule H (2026) line references and IRS household employer guidance as read for this release |  |  |  |  |  |  |  |  |
| Similar To | US-IRS-001 Form 941 |  |  |  |  |  |  |  |  |
| ═══ REPORT MATRIX ═══ |  |  |  |  |  |  |  |  |  |
| Report ID | Report Name (EN) | Report Name (Local) | Authority | Frequency | Due Date Rule | Submission Method | File Format | Legal Basis | Accuracy Assessment |
| US-IRS-005 | Schedule H routing (household employees) | Schedule H (household employer's individual return) | Internal Revenue Service (IRS) | Annual | With the household employer's personal return: 2027-04-15 (with the 2026 Form 1040/1040-SR/1040-SS/1040-NR/1041; extension of the return extends Schedule H; stand-alone if no return) | Not transmitted by the payroll: routing flag only | Routing flag only: household-employee wages are reported by the household employer on Schedule H. Not a file produced by the payroll. | [US-FEDS5-029] | Channel: none (routing flag) \| Portal: Not applicable \| Source: https://www.irs.gov/pub/irs-pdf/p926.pdf \| CONFIRMED. Accuracy 90% (routing rule, thresholds, statement content and due date read). Closes with: one household employer's filed Schedule H checked against the statement. |

## Payroll Scope Summary

| US-IRS-005 SCHEDULE H ROUTING (HOUSEHOLD EMPLOYEES) — PAYROLL SCOPE SUMMARY |  |  |
|---|---|---|
| Flag household employees so that their wages are routed to the household employer's Schedule H. |  |  |
| SCENARIO | REPORT? | NOTES / REASONING |
| ═══ WHO GETS REPORTED ═══ |  |  |
| Household (domestic) employees | YES | Flag only [US-OWN-005, US-FEDS5-029]. |
| Filing of the household employer's own return | NO | Out of scope: filed with the personal return. |
| ═══ TIMING & RELATIONSHIP ═══ |  |  |
| Annual coverage tests | YES | Rows SCHH-002, SCHH-003. |
| ═══ AMOUNTS & CALCULATIONS ═══ |  |  |
| FICA cash-wage test | YES | 3,000 |
| FUTA quarter test | YES | 1,000 |
| ═══ SPECIAL CASES ═══ |  |  |
| State household returns (e.g. CT-W3 HHE, NJ-927-H, OR Form OA) | NO | State-level special-population rules are deferred to a later round [US-OWN-005]. |

## Schedule H Spec

| Field Name (EN) | Field Name (Authority label, EN) | Record Type | Field Position | Payroll Field (Y/N) | Mandatory (Y/N/C) | Conditional Reason | Position (Start-End) | Field Length | Format | Example | System Mapping | Field Explanation | Relevant for Payroll | Option Values | Rounding | Negative (Y/N) | Value Type | Reporting Frequency | Query to RA | RA Comments |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ═══ ROUTING FLAG (no return produced by the payroll) ═══ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Household employee flag | Household employee | Routing | SCHH-001 | Y | Y | Not conditional: every employee carries the flag (Y or N). | Logical field (field model) | 1 | Flag | Y | US-DD-001 v1.0: Employee special population category | Marks wages paid by a household employer. Those wages are reported by the household employer on Schedule H with the personal return [US-FEDS5-029]; the payroll does not file that return and excludes the wages from Forms 941 and 940 (US-IRS-001, US-IRS-004). | Yes: routing of the wages | Y / N | Not applicable | N | Input (Flag) | Annual | No open query. |  |
| Household cash wages for the FICA test | Cash wages | Routing | SCHH-002 | Y | C | Only when SCHH-001 = Y. | Logical field (field model) | Amount | Decimal 13.2 | 3,200.00 | Payroll result: household cash wages per employee per year | Cash wages paid to the household employee in the year, compared with 3,000 USD [US-FEDS5-029]; at or above it the wages are FICA wages. Taken from the household cash wage accumulator per employee for the year, in cents; only cash wages enter this test. Below the threshold the social security and Medicare items of the statement stay at zero for that employee (rows SCHH-005 onwards). [US-FEDS5-029] Source type: Web research (official authority page). https://www.irs.gov/pub/irs-pdf/p15.pdf | Yes: FICA coverage test | Not applicable | Cents (2 decimals) | N | Input (Amount) | Annual | No open query. |  |
| Household cash wages per quarter for the FUTA test | Quarterly cash wages | Routing | SCHH-003 | Y | C | Only when SCHH-001 = Y. | Logical field (field model) | Amount per quarter | Decimal 13.2 | 1,100.00 | Payroll result: household cash wages per quarter (all household employees) | Total household cash wages in a calendar quarter compared with 1,000 USD [US-FEDS5-029] for FUTA. Taken from the household cash wage accumulator per quarter, summed over all household employees, in cents. When a quarter of the current or the preceding year reaches the threshold the FUTA items of the statement are produced; otherwise they stay at zero. [US-FEDS5-029] Source type: Web research (official authority page). https://www.irs.gov/pub/irs-pdf/p15.pdf | Yes: FUTA coverage test | Q1 to Q4 | Cents (2 decimals) | N | Input (Amount) | Quarterly | No open query. |  |
| Federal income tax withholding by agreement | Voluntary withholding | Routing | SCHH-004 | Y | C | Only when SCHH-001 = Y and the employee asked for withholding. | Logical field (field model) | 1 | Flag | N | US-DD-001 v1.0: Household employee: federal income tax withholding agreement | Switch for federal income tax withholding on household wages: it is withheld only by agreement [US-FEDS5-029] between the household employer and the employee. Held as a Y / N flag in the Data Dictionary; when Y the payroll withholds FIT per US-CCG-001 v1.0 Module 6 and the amount enters the annual statement below, when N no FIT is withheld. Social security, Medicare and FUTA coverage follow their own cash-wage tests (rows above), not this flag. | Yes: withholding switch | Y / N | Not applicable | N | Input (Flag) | Per payment | No open query. |  |
| ═══ ANNUAL STATEMENT HANDED TO THE HOUSEHOLD EMPLOYER (Schedule H amounts) ═══ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Schedule H statement (source) | Annual amounts for Schedule H | Statement | SCHH-005 | N | Y | Not conditional: produced for every household employer with household employees (SCHH-001 = Y). | Not applicable | Not applicable | Text | See the item rows below | Statement generator (system constant) | Annual amounts per household employee/employer for Schedule H (2026): cash wages subject to social security tax (line 1; only if >= 3,000 cash wages to the employee in 2026; capped at 184,500); cash wages subject to Medicare tax (line 3); wages subject to Additional Medicare Tax withholding (line 5, over 200,000); federal income tax withheld (line 7); state unemployment contributions paid and state(s) (lines 13-14 / 17); cash wages subject to FUTA (line 15 or 20: first 7,000 per employee when cash wages >= 1,000 in any calendar quarter of 2025 or 2026); plus the employee/employer social security and Medicare tax amounts (lines 2, 4, 6) [US-FEDS6-010]. Each item below is one line of this statement. The statement is produced by the payroll once a year per household employer from the annual accumulators of each household employee; it is handed over, not filed by the payroll. Items whose coverage test (rows SCHH-002 and SCHH-003) is not met are shown at zero. [US-FEDS6-010] Source type: Official spec. https://www.irs.gov/pub/irs-pdf/p926.pdf | Yes: completeness of the hand-off | Not applicable | Not applicable | N | Display-only (Text) | Annual | No open query. |  |
| Statement: Cash wages subject to social security tax | Cash wages subject to social security tax | Statement | SCHH-006 | Y | C | Only when SCHH-001 = Y and the amount arises for the employee in the year; back-reference to SCHH-002 and SCHH-003 for the coverage tests. | Not applicable | Amount | Decimal 13.2 | See Example Analysis | Payroll result: household annual accumulator per employee | Statement item for the household employer's Schedule H: cash wages subject to social security tax (line 1; only if >= 3,000 USD cash wages to the employee in 2026; capped at 184,500 USD). The payroll hands the amount over once a year; the household employer files it with the personal return. [US-FEDS6-010] Source type: Official spec. https://www.irs.gov/pub/irs-pdf/p926.pdf | Yes: hand-off to the household employer | Not applicable | Cents (2 decimals) | N | Input (Amount) | Annual | No open query. |  |
| Statement: Cash wages subject to Medicare tax | Cash wages subject to Medicare tax | Statement | SCHH-007 | Y | C | Only when SCHH-001 = Y and the amount arises for the employee in the year; back-reference to SCHH-002 and SCHH-003 for the coverage tests. | Not applicable | Amount | Decimal 13.2 | See Example Analysis | Payroll result: household annual accumulator per employee | Statement item for the household employer's Schedule H: cash wages subject to Medicare tax (line 3). The payroll hands the amount over once a year; the household employer files it with the personal return. [US-FEDS6-010] Source type: Official spec. https://www.irs.gov/pub/irs-pdf/p926.pdf | Yes: hand-off to the household employer | Not applicable | Cents (2 decimals) | N | Input (Amount) | Annual | No open query. |  |
| Statement: Wages subject to Additional Medicare Tax withholding | Wages subject to Additional Medicare Tax withholding | Statement | SCHH-008 | Y | C | Only when SCHH-001 = Y and the amount arises for the employee in the year; back-reference to SCHH-002 and SCHH-003 for the coverage tests. | Not applicable | Amount | Decimal 13.2 | See Example Analysis | Payroll result: household annual accumulator per employee | Statement item for the household employer's Schedule H: wages subject to Additional Medicare Tax withholding (line 5, over 200,000 USD). The payroll hands the amount over once a year; the household employer files it with the personal return. [US-FEDS6-010] Source type: Official spec. https://www.irs.gov/pub/irs-pdf/p926.pdf | Yes: hand-off to the household employer | Not applicable | Cents (2 decimals) | N | Input (Amount) | Annual | No open query. |  |
| Statement: Federal income tax withheld | Federal income tax withheld | Statement | SCHH-009 | Y | C | Only when SCHH-001 = Y and the amount arises for the employee in the year; back-reference to SCHH-002 and SCHH-003 for the coverage tests. | Not applicable | Amount | Decimal 13.2 | See Example Analysis | Payroll result: household annual accumulator per employee | Statement item for the household employer's Schedule H: federal income tax withheld (line 7). The payroll hands the amount over once a year; the household employer files it with the personal return. [US-FEDS6-010] Source type: Official spec. https://www.irs.gov/pub/irs-pdf/p926.pdf | Yes: hand-off to the household employer | Not applicable | Cents (2 decimals) | N | Input (Amount) | Annual | No open query. |  |
| Statement: State unemployment contributions paid and state(s) | State unemployment contributions paid and state(s) | Statement | SCHH-010 | Y | C | Only when SCHH-001 = Y and the amount arises for the employee in the year; back-reference to SCHH-002 and SCHH-003 for the coverage tests. | Not applicable | Amount | Decimal 13.2 | See Example Analysis | Payroll result: household annual accumulator per employee | Statement item for the household employer's Schedule H: state unemployment contributions paid and state(s) (lines 13-14 / 17). The payroll hands the amount over once a year; the household employer files it with the personal return. [US-FEDS6-010] Source type: Official spec. https://www.irs.gov/pub/irs-pdf/p926.pdf | Yes: hand-off to the household employer | Not applicable | Cents (2 decimals) | N | Input (Amount) | Annual | No open query. |  |
| Statement: Cash wages subject to FUTA | Cash wages subject to FUTA | Statement | SCHH-011 | Y | C | Only when SCHH-001 = Y and the amount arises for the employee in the year; back-reference to SCHH-002 and SCHH-003 for the coverage tests. | Not applicable | Amount | Decimal 13.2 | See Example Analysis | Payroll result: household annual accumulator per employee | Statement item for the household employer's Schedule H: cash wages subject to FUTA (line 15 or 20: first 7,000 USD per employee when cash wages >= 1,000 USD in any calendar quarter of 2025 or 2026). The payroll hands the amount over once a year; the household employer files it with the personal return. [US-FEDS6-010] Source type: Official spec. https://www.irs.gov/pub/irs-pdf/p926.pdf | Yes: hand-off to the household employer | Not applicable | Cents (2 decimals) | N | Input (Amount) | Annual | No open query. |  |
| Statement: Employee/employer social security and Medicare tax amounts | Employee/employer social security and Medicare tax amounts | Statement | SCHH-012 | Y | C | Only when SCHH-001 = Y and the amount arises for the employee in the year; back-reference to SCHH-002 and SCHH-003 for the coverage tests. | Not applicable | Amount | Decimal 13.2 | See Example Analysis | Calculated from the household payroll results | Statement item for the household employer's Schedule H: plus the employee/employer social security and Medicare tax amounts (lines 2, 4, 6). The payroll hands the amount over once a year; the household employer files it with the personal return. [US-FEDS6-010] Source type: Official spec. https://www.irs.gov/pub/irs-pdf/p926.pdf | Yes: hand-off to the household employer | Not applicable | Cents (2 decimals) | N | Calculated | Annual | No open query. |  |
| Schedule H due date | Due date | Statement | SCHH-013 | N | Y | Not conditional. | Not applicable | Date | YYYY-MM-DD | 2027-04-15 | Filing calendar of the payroll (system constant) | 2027-04-15 (with the 2026 Form 1040/1040-SR/1040-SS/1040-NR/1041; extension of the return extends Schedule H; stand-alone if no return) [US-FEDS6-010]. The statement is handed over early enough for the household employer to file by that date; Forms W-2 for household employees follow US-SSA-001. Held in the filing calendar of the payroll as a date (YYYY-MM-DD); the household employer files Schedule H with the personal return, so an extension of that return moves the date as the rule states. [US-FEDS6-010] Source type: Web research (official authority page). https://www.irs.gov/pub/irs-pdf/p926.pdf | Yes: hand-off calendar | Not applicable | Not applicable | N | Input (Date) | Annual | No open query. |  |
| Household coverage thresholds (Schedule H) | Thresholds | Statement | SCHH-014 | N | Y | Not conditional. | Not applicable | Amount | Decimal | See column M | System constant per year | FICA cash-wage test 3,000 USD [US-FEDS6-010] per employee in the year; FUTA test 1,000 USD [US-FEDS6-010] of cash wages in any calendar quarter. Same figures as SCHH-002 and SCHH-003. [US-FEDS6-010] Source type: Web research (official authority page). https://www.irs.gov/pub/irs-pdf/p926.pdf | Yes: coverage tests | Not applicable | Whole dollars as published | N | Input (Amount) | Annual | No open query. |  |

## File Structure

| US-IRS-005 Schedule H Routing (Household Employees) — FILE STRUCTURE AND TECHNICAL SPECIFICATIONS |
|---|
| ═══ FILE FORMAT ═══ |
| No file is produced by the payroll for this filing. |
| Hand-off: one annual statement per household employer with the Schedule H amounts of each household employee (rows SCHH-005 onwards). |
| ═══ STATEMENT CONTENT ═══ |
| Annual amounts per household employee/employer for Schedule H (2026): cash wages subject to social security tax (line 1; only if >= 3,000 cash wages to the employee in 2026; capped at 184,500); cash wages subject to Medicare tax (line 3); wages subject to Additional Medicare Tax withholding (line 5, over 200,000); federal income tax withheld (line 7); state unemployment contributions paid and state(s) (lines 13-14 / 17); cash wages subject to FUTA (line 15 or 20: first 7,000 per employee when cash wages >= 1,000 in any calendar quarter of 2025 or 2026); plus the employee/employer social security and Medicare tax amounts (lines 2, 4, 6) [US-FEDS6-010] |

## Field Options

| Field Name | Option Code | Description (EN) | Description (Authority wording, EN) | Authority Reference |
|---|---|---|---|---|
| ═══ HOUSEHOLD FLAG (SCHH-001) ═══ |  |  |  |  |
| Household employee | Y | Household employee | Domestic service in a private home | [US-FEDS5-029] |
| Household employee | N | Other employee | Not household | [US-FEDS5-029] |

## Population Rules

| Rule Category | Field Name | Source System | Population Logic | Edge Cases |
|---|---|---|---|---|
| ═══ PAYROLL-SPECIFIC POPULATION RULES ═══ |  |  |  |  |
| Conditional | SCHH-002, SCHH-003, SCHH-004 | Household flag; payroll results | When SCHH-001 = Y, accumulate cash wages per employee per year and per quarter for all household employees, apply the FICA and FUTA tests, and withhold federal income tax only if the employee and employer agreed to it. | Non-cash household pay is outside the cash tests. |
| Conditional | SCHH-006 onwards (statement items) | Household payroll results | For each household employer, total each statement item per household employee for the calendar year and hand the statement over before the Schedule H due date; items whose coverage test is not met stay at zero. | A household employee crossing the FICA cash-wage test late in the year brings all cash wages of the year into the FICA items. |

## Example Analysis

| US-IRS-005 Schedule H Routing (Household Employees) — EXAMPLE FILE ANALYSIS |  |  |  |
|---|---|---|---|
| Raw Value | Field Name | Interpretation | Notes |
| ═══ WORKED EXAMPLE: COVERAGE TESTS (constructed) ═══ |  |  |  |
| 3,200.00 | Cash wages in the year (SCHH-002) | 3,200.00 against 3,000 | At or above: FICA wages |
| 1,100.00 | Cash wages in Q2 (SCHH-003) | 1,100.00 against 1,000 | At or above: FUTA coverage |

## Sample File

| US-IRS-005 Schedule H Routing (Household Employees) — SAMPLE FILE |
|---|
| No file is produced for this filing; the payroll sets a routing flag. No sample exists. |


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `fed.fica.addl_medicare.withholding_threshold` | 200,000 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.fica.oasdi.wage_base` | 184,500 | from 2026-01-01 to 2026-12-31 | US-FEDS5-005 |
| `fed.futa.wage_base` | 7,000 | from 2025-01-01 | US-FED-007 |
| `fed.household.fica_cash_threshold` | 3,000 | from 2026-01-01 to 2026-12-31 | US-FEDS5-029 |
| `fed.household.fit.withholding` | only by agreement | from 2026-01-01 | US-FEDS5-029 |
| `fed.household.futa_quarter_threshold` | 1,000 | from 2026-01-01 | US-FEDS5-029 |
| `rspec.fed.household.fica_cash_wage_threshold` | 3,000 | from 2026-01-01 | US-FEDS6-010 |
| `rspec.fed.household.futa_quarter_threshold` | 1,000 | from 2026-01-01 | US-FEDS6-010 |
| `rspec.fed.schedule_h.due` | 2027-04-15 (with the 2026 Form 1040/1040-SR/1040-SS/1040-NR/1041; extension of the return extends Schedule H; stand-alone if no return) | from 2026-01-01 | US-FEDS6-010 |
| `rspec.fed.schedule_h.employer_statement` | Annual amounts per household employee/employer for Schedule H (2026): cash wages subject to social security tax (line 1; only if >= 3,000 cash wages to the employee in 2026; capped at 184,500); cash wages subject to Medicare tax (line 3); wages subject to Additional Medicare Tax withholding (line 5, over 200,000); federal income tax withheld (line 7); state unemployment contributions paid and state(s) (lines 13-14 / 17); cash wages subject to FUTA (line 15 or 20: first 7,000 per employee when cash wages >= 1,000 in any calendar quarter of 2025 or 2026); plus the employee/employer social security and Medicare tax amounts (lines 2, 4, 6) | from 2026-01-01 | US-FEDS6-010 |

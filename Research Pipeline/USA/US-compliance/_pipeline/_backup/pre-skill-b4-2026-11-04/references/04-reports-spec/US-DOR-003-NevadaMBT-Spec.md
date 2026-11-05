# US-DOR-003-NevadaMBT-Spec


## Version Control

|  | Statutory Report Specification |  |  |  |  |
|---|---|---|---|---|---|
|  | United States of America |  |  |  |  |
|  | US-DOR-003 Nevada Modified Business Tax Return (Form TAX-F003, general business) |  |  |  |  |
|  | Document ID | US-DOR-003 |  |  |  |
|  | Version | Effective Date | Change Description | Status | Updated By |
|  | 1.0 | 2027-03-31 00:00:00 | For QA. | For QA | Wallisson Gomes |
|  | REMARKS |  |  |  |  |
|  | Topic | Remark |  |  |  |
|  | Scope | One Report Specification per authority return in scope for the United States package v1.0. Field-level definitions of master data are owned by the Data Dictionary US-DD-001 v1.0; rules and rates by the Country Configuration Guide US-CCG-001 v1.0. |  |  |  |
|  | Channel | Every return is transmitted by the third-party filing provider acting as reporting agent (Form 8655 for federal returns). The payroll produces the data set of the field model; the provider maps it to the authority wire format. |  |  |  |
|  | Limitations | Open points are written in place with an open-point reference and listed in the Report Matrix accuracy note. No value is assumed where the official source has not been read. |  |  |  |

## Report Matrix

| US-DOR-003 NEVADA MODIFIED BUSINESS TAX RETURN (FORM TAX-F003, GENERAL BUSINESS) |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| Document ID | US-DOR-003 |  |  |  |  |  |  |  |  |
| Document Title | US-DOR-003 Nevada Modified Business Tax Return (Form TAX-F003, general business) |  |  |  |  |  |  |  |  |
| Country | United States of America |  |  |  |  |  |  |  |  |
| Authority | Nevada Department of Taxation |  |  |  |  |  |  |  |  |
| Report Type | Outbound statutory return (employer to authority, through the filing provider hand-off) |  |  |  |  |  |  |  |  |
| Tax Type | Modified Business Tax (employer payroll tax) |  |  |  |  |  |  |  |  |
| Relationship | Wages must match the Nevada UI report (US-UI-001) |  |  |  |  |  |  |  |  |
| Frequency | Quarterly |  |  |  |  |  |  |  |  |
| Submission Deadline | last day of month after quarter (file even if no tax) |  |  |  |  |  |  |  |  |
| File Format | My Nevada Tax e-file or paper. FIELD MODEL: logical model - not the wire/submission format. |  |  |  |  |  |  |  |  |
| File Extension | Per jurisdiction (see Report Matrix) |  |  |  |  |  |  |  |  |
| Character Encoding | Per jurisdiction (ASCII for fixed-length layouts) |  |  |  |  |  |  |  |  |
| Record Length | Per jurisdiction |  |  |  |  |  |  |  |  |
| Record Types / Sections | Amounts; NV section |  |  |  |  |  |  |  |  |
| Version | 1.0 |  |  |  |  |  |  |  |  |
| Created Date | 2027-03-31 |  |  |  |  |  |  |  |  |
| Created By | Mercans Compliance Regulations Team |  |  |  |  |  |  |  |  |
| Official Source | https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F003-MBT-Return-General-Business.pdf |  |  |  |  |  |  |  |  |
| Last Update Reference | Department of Taxation pages as read |  |  |  |  |  |  |  |  |
| Similar To | US-UI-001 |  |  |  |  |  |  |  |  |
| ═══ REPORT MATRIX ═══ |  |  |  |  |  |  |  |  |  |
| Report ID | Report Name (EN) | Report Name (Local) | Authority | Frequency | Due Date Rule | Submission Method | File Format | Legal Basis | Accuracy Assessment |
| US-DOR-003-NV | Nevada: Modified Business Tax return | MBT quarterly TAX-F003 (V2026.1), last day of month after quarter, even no tax due | Nevada Department of Taxation | Quarterly | last day of month after quarter (file even if no tax) | online_form (My Nevada Tax) | Portal or form as stated in column C. FIELD MODEL: logical model - not the wire/submission format. | [US-NVP51-002] [US-NVS5-009] [US-NVS5-010] [US-NVS5-011]; https://tax.nv.gov/tax-types/modified-business-tax/ https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F003-MBT-Return-General-Business.pdf | Channel: online_form \| Portal: My Nevada Tax (named in [US-NVS5-009]) \| Source: https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F003-MBT-Return-General-Business.pdf \| TO CONFIRM. Accuracy 75% (form and timing read; channel detail from the form rule). Closes with: a real filing or the provider's acceptance report for this jurisdiction. |

## Payroll Scope Summary

| US-DOR-003 NEVADA MODIFIED BUSINESS TAX RETURN (FORM TAX-F003, GENERAL BUSINESS) — PAYROLL SCOPE SUMMARY |  |  |
|---|---|---|
| Nevada employers with UI wages above the quarterly exclusion. |  |  |
| SCENARIO | REPORT? | NOTES / REASONING |
| ═══ WHO GETS REPORTED ═══ |  |  |
| Nevada employers liable for UI | YES | UI gross wages + tips as reported to the Employment Security Division (ESD) less employer-paid health benefits |
| ═══ TIMING & RELATIONSHIP ═══ |  |  |
| Quarterly return, even with no tax | YES | MBT quarterly TAX-F003 (V2026.1), last day of month after quarter, even no tax due |
| ═══ AMOUNTS & CALCULATIONS ═══ |  |  |
| Quarterly exclusion and rate | YES | 50,000; 1.17% |
| ═══ SPECIAL CASES ═══ |  |  |
| Nonresident alien employees | PARTIAL | Reported like other employees unless the jurisdiction rule in its section says otherwise; federal treaty exemptions do not change State reporting by themselves. |
| Household and agricultural employees (State level) | NO | State-level rules for special populations are deferred to a later round [US-OWN-005]. |
| Independent contractors | NO | Out of scope [US-OWN-008]. |

## Nevada MBT Spec

| Field Name (EN) | Field Name (Authority label, EN) | Record Type | Field Position | Payroll Field (Y/N) | Mandatory (Y/N/C) | Conditional Reason | Position (Start-End) | Field Length | Format | Example | System Mapping | Field Explanation | Relevant for Payroll | Option Values | Rounding | Negative (Y/N) | Value Type | Reporting Frequency | Query to RA | RA Comments |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ═══ COMMON FIELD MODEL (all jurisdictions) ═══ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Gross wages as reported for UI | UI gross wages | Amounts | MBT-C-001 | Y | Y | Not conditional. | Logical field (field model) | Money | Decimal 13.2 | 180,000.00 | Payroll result: Nevada UI gross wages of the quarter | Base definition: UI gross wages + tips as reported to the Employment Security Division (ESD) less employer-paid health benefits [US-NVS5-011] [US-NVS5-009]. from 2026-01-01 MBT wages compared with ESD wages every quarter; mismatch = deficiency. Taken from the Nevada UI gross wage accumulator of the quarter, the same amount the employer reports on the Nevada UI wage report (US-UI-001), in cents. Employer-paid health benefits are deducted in row MBT-C-002, never inside this field; a difference between this amount and the UI wages of the quarter is resolved before filing (rule above). | Yes | Not applicable | Cents | N | Input (Amount) | Quarterly | No open query. |  |
| Employer-paid health benefits deducted | Health benefits | Amounts | MBT-C-002 | Y | C | Only when the employer pays health benefits. | Logical field (field model) | Money | Decimal 13.2 | 10,000.00 | Payroll result: employer health benefit cost | Employer-paid health benefits for the quarter, deducted from the Modified Business Tax base: UI gross wages + tips as reported to the Employment Security Division (ESD) less employer-paid health benefits [US-NVS5-011] [US-NVS5-009]. The amount is the employer's cost for the quarter, taken from the payroll result for employer health benefit cost, and is reported in cents next to the wages of row MBT-C-001. It is reported only for a quarter in which the employer paid such benefits; otherwise the field is zero and the base is the UI gross wages alone. | Yes | Not applicable | Cents | N | Input (Amount) | Quarterly | No open query. |  |
| Taxable wages and tax due | Tax due | Amounts | MBT-C-003 | N | Y | Not conditional. | Logical field (field model) | Money | Decimal 13.2 | See Example Analysis | Calculated by the return generator | Taxable wages and the tax due for the quarter, computed by the return generator and never keyed: (row MBT-C-001 minus row MBT-C-002, minus 50,000 USD a quarter) x 1.17% for general business [US-NVP51-002]; the quarterly exclusion is [US-NVS5-011]. Financial institutions and mining use 1.554%. When the base does not exceed the exclusion the tax is zero, but the return is still filed: MBT quarterly TAX-F003 (V2026.1), last day of month after quarter, even no tax due. Rounded to the cent, half-up (see Example Analysis). | Yes | Not applicable | Cents | N | Calculated | Quarterly | No open query. |  |
| ═══ NV: NEVADA ═══ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| NV Return form and filing rule | Nevada authority wording (English filing language) | Jurisdiction parameter: NV | DOR-NV-001 | N | Y | Not conditional: applies to every employer filing this return in the jurisdiction. | Return level (not a file position) | Not applicable (configuration value) | Code / rule | Form generated for the 2026 period | Jurisdiction configuration (system constant) | Nevada: return form and filing rule: MBT quarterly TAX-F003 (V2026.1), last day of month after quarter, even no tax due. Names the authority form generated for the period and the condition under which it applies. [US-NVS5-010] Source type: Official spec. https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F003-MBT-Return-General-Business.pdf | Yes: governs how the quarterly return is produced for Nevada | Value as stated in column M | Not applicable | N | Input (Rule) | Quarterly | Confirm against a real filing: the source carries confidence medium [US-NVS5-010]. |  |
| NV Reporting rule | Nevada authority wording (English filing language) | Jurisdiction parameter: NV | DOR-NV-002 | N | C | Applies only in the situation stated in column M. | Return level (not a file position) | Not applicable (configuration value) | Rule | Rule applied when its condition occurs | Jurisdiction configuration (system constant) | Nevada: reporting rule: from 2026-01-01 MBT wages compared with ESD wages every quarter; mismatch = deficiency. Applied by the payroll when the situation named in the rule occurs. [US-NVS5-009] Source type: Web research (official authority page). https://tax.nv.gov/tax-types/modified-business-tax/ | Yes: governs how the quarterly return is produced for Nevada | Value as stated in column M | Not applicable | N | Input (Rule) | Quarterly | No open query. |  |
| NV Contribution or tax rate | Nevada authority wording (English filing language) | Jurisdiction parameter: NV | DOR-NV-003 | N | C | Applies to the base and payer stated in column M for employers liable in the jurisdiction. | Return level (not a file position) | Not applicable (configuration value) | Rate | Rate applied to the period base | Jurisdiction rate table (dated system constant) | Nevada: contribution or tax rate: 1.17% of the quarterly taxable wages above 50,000 USD; borne by the employer. The payroll applies the rate to the base and payer stated in this row for each period; the amount is computed by the payroll from the period results, never keyed. [US-NVP51-002] Source type: Web research (official authority page). https://tax.nv.gov/tax-types/modified-business-tax/ | Yes: governs how the quarterly return is produced for Nevada | Value as stated in column M | As published (decimal places of the source kept) | N | Input (Rate) | Quarterly | No open query. |  |
| NV Taxable wage threshold | Nevada authority wording (English filing language) | Jurisdiction parameter: NV | DOR-NV-004 | N | C | Applies to the quarterly taxable wages stated in column M for employers liable in the jurisdiction. | Return level (not a file position) | Not applicable (configuration value) | Amount or count | Quarterly wages compared with the threshold | Jurisdiction configuration (dated system constant) | Nevada: taxable wage threshold: 50,000 USD of taxable wages per quarter; the general MBT rate applies only to the quarterly wages above this amount. The payroll compares the employer's quarterly taxable wages with this amount and applies the rate only to the wages above it. [US-NVS5-011] Source type: Web research (official authority page). https://www.leg.state.nv.us/NRS/NRS-363B.html | Yes: governs how the quarterly return is produced for Nevada | Value as stated in column M | Whole units as published | N | Input (Amount) | Quarterly | No open query. |  |
| NV Reporting rule | Nevada authority wording (English filing language) | Jurisdiction parameter: NV | DOR-NV-005 | N | C | Applies only in the situation stated in column M. | Return level (not a file position) | Not applicable (configuration value) | Rule | Rule applied when its condition occurs | Jurisdiction configuration (system constant) | Nevada: reporting rule: UI gross wages + tips as reported to the Employment Security Division (ESD) less employer-paid health benefits. Applied by the payroll when the situation named in the rule occurs. [US-NVS5-011] [US-NVS5-009] Source type: Web research (official authority page). https://www.leg.state.nv.us/NRS/NRS-363B.html | Yes: governs how the quarterly return is produced for Nevada | Value as stated in column M | Not applicable | N | Input (Rule) | Quarterly | No open query. |  |
| NV Due date rule | Nevada authority wording (English filing language) | Jurisdiction parameter: NV | DOR-NV-006 | N | Y | Not conditional: applies to every employer filing this return in the jurisdiction. | Return level (not a file position) | Not applicable (configuration value) | Date rule | 2026 Q1 return: due per the rule in column M | Filing calendar of the payroll (system constant per jurisdiction) | Nevada: due date rule: last day of month after quarter (file even if no tax). Drives the filing calendar for the provider hand-off; a due date on a Saturday, Sunday or legal holiday follows the roll-forward stated in the rule or the authority's calendar. [US-NVS5-010] Source type: Web research (official authority page). https://tax.nv.gov/wp-content/uploads/2025/12/TAX-F003-MBT-Return-General-Business.pdf | Yes: governs how the quarterly return is produced for Nevada | Value as stated in column M | Not applicable | N | Input (Rule) | Quarterly | No open query. |  |

## File Structure

| US-DOR-003 Nevada Modified Business Tax Return (Form TAX-F003, general business) — FILE STRUCTURE AND TECHNICAL SPECIFICATIONS |
|---|
| ═══ FILE FORMAT ═══ |
| FIELD MODEL: logical model - not the wire/submission format for the common field model; each jurisdiction's own channel and layout are in its section of the core sheet and in the Report Matrix. |
| Where a jurisdiction layout is published and read, its positions are given in the jurisdiction section; otherwise the provider maps the field model to the authority format. |
| FORMAT TO CONFIRM vs a real filing in every jurisdiction. |

## Field Options

| Field Name | Option Code | Description (EN) | Description (Authority wording, EN) | Authority Reference |
|---|---|---|---|---|
| ═══ SUBMISSION CHANNEL CLASS (Report Matrix column G) ═══ |  |  |  |  |
| Channel class | online_form | Portal entry (keyed or web form) on the authority portal | Portal entry (keyed or web form) on the authority portal | Mercans Report Specification standard (channel classes) |
| Channel class | file_upload | File upload (fixed-length, CSV, EFW2, ICESA or another authority layout) | File upload (fixed-length, CSV, EFW2, ICESA or another authority layout) | Mercans Report Specification standard (channel classes) |
| Channel class | xml | XML file under a published schema or file specification | XML file under a published schema or file specification | Mercans Report Specification standard (channel classes) |
| Channel class | api | System-to-system transmission (web service, FSET) | System-to-system transmission (web service, FSET) | Mercans Report Specification standard (channel classes) |
| Channel class | paper | Paper form, coupon, CD/DVD, mail or fax | Paper form, coupon, CD/DVD, mail or fax | Mercans Report Specification standard (channel classes) |

## Population Rules

| Rule Category | Field Name | Source System | Population Logic | Edge Cases |
|---|---|---|---|---|
| ═══ CROSS-FIELD VALIDATIONS ═══ |  |  |  |  |
| Match | MBT-C-001 | Nevada UI report | The MBT wages equal the gross wages of the Nevada UI report of the same quarter; a mismatch creates a deficiency. | Amended UI reports require an amended MBT return. |
| ═══ CONDITIONAL JURISDICTION PARAMETERS ═══ |  |  |  |  |
| Conditional (jurisdiction) | MBT-C-002 Employer-paid health benefits deducted | Jurisdiction configuration | Employer-paid health benefits deducted: Only when the employer pays health benefits. The rule text and figure are in column M of row MBT-C-002; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-DOR-003 Nevada Modified Business Tax Return (Form TAX-F003, general business). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |
| Conditional (jurisdiction) | DOR-NV-002 NV Reporting rule | Jurisdiction configuration | NV Reporting rule: Applies only in the situation stated in column M. The rule text and figure are in column M of row DOR-NV-002; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-DOR-003 Nevada Modified Business Tax Return (Form TAX-F003, general business). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |
| Conditional (jurisdiction) | DOR-NV-003 NV Contribution or tax rate | Jurisdiction configuration | NV Contribution or tax rate: Applies to the base and payer stated in column M for employers liable in the jurisdiction. The rule text and figure are in column M of row DOR-NV-003; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-DOR-003 Nevada Modified Business Tax Return (Form TAX-F003, general business). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |
| Conditional (jurisdiction) | DOR-NV-004 NV Taxable wage threshold | Jurisdiction configuration | NV Taxable wage threshold: Applies to the quarterly taxable wages stated in column M for employers liable in the jurisdiction. The rule text and figure are in column M of row DOR-NV-004; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-DOR-003 Nevada Modified Business Tax Return (Form TAX-F003, general business). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |
| Conditional (jurisdiction) | DOR-NV-005 NV Reporting rule | Jurisdiction configuration | NV Reporting rule: Applies only in the situation stated in column M. The rule text and figure are in column M of row DOR-NV-005; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-DOR-003 Nevada Modified Business Tax Return (Form TAX-F003, general business). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |

## Example Analysis

| US-DOR-003 Nevada Modified Business Tax Return (Form TAX-F003, general business) — EXAMPLE FILE ANALYSIS |  |  |  |
|---|---|---|---|
| Raw Value | Field Name | Interpretation | Notes |
| ═══ WORKED EXAMPLE: GENERAL BUSINESS MBT FOR ONE QUARTER (constructed) ═══ |  |  |  |
| 180,000.00 | UI gross wages (MBT-C-001) | Constructed input | Input |
| 10,000.00 | Employer-paid health benefits (MBT-C-002) | Constructed input | Input |
| 170,000.00 | Base | 180,000.00 - 10,000.00 | Calculation |
| 120,000.00 | Taxable wages | 170,000.00 - 50,000 | Calculation |
| 1,404.00 | MBT due | 120,000.00 x 1.17% | Half-up to the cent |

## Sample File

| US-DOR-003 Nevada Modified Business Tax Return (Form TAX-F003, general business) — SAMPLE FILE |
|---|
| No official sample filing is held for these returns and none is constructed. Verified channels: the per-jurisdiction channel classes and portals in the Report Matrix (column G and the accuracy note). |


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `nv.mbt.base` | UI gross wages + tips as reported to the Employment Security Division (ESD) less employer-paid health benefits | from 2026-01-01 | US-NVS5-011 |
| `nv.mbt.financial_mining.rate` | 1.554 | from 2026-01-01 | US-NVP51-002 |
| `nv.mbt.general.quarterly_threshold` | 50,000 | from 2026-01-01 | US-NVS5-011 |
| `nv.mbt.general.rate` | 1.17 | from 2026-01-01 | US-NVP51-002 |
| `nv.report.mbt.due` | last day of month after quarter (file even if no tax) | from 2025-12-02 | US-NVS5-010 |
| `rspec.nv.mbt.form` | MBT quarterly TAX-F003 (V2026.1), last day of month after quarter, even no tax due | from 2025-12-02 | US-NVS5-010 |
| `rspec.nv.mbt.ui_match` | from 2026-01-01 MBT wages compared with ESD wages every quarter; mismatch = deficiency | from 2023-07-01 | US-NVS5-009 |

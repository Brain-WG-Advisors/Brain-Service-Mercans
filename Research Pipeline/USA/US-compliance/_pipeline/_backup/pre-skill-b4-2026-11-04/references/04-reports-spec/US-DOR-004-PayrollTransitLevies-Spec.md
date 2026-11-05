# US-DOR-004-PayrollTransitLevies-Spec


## Version Control

|  | Statutory Report Specification |  |  |  |  |
|---|---|---|---|---|---|
|  | United States of America |  |  |  |  |
|  | US-DOR-004 Employer Payroll Transit Levies (Oregon, New York) |  |  |  |  |
|  | Document ID | US-DOR-004 |  |  |  |
|  | Version | Effective Date | Change Description | Status | Updated By |
|  | 1.0 | 2027-03-31 00:00:00 | For QA. | For QA | Wallisson Gomes |
|  | REMARKS |  |  |  |  |
|  | Topic | Remark |  |  |  |
|  | Scope | One Report Specification per authority return in scope for the United States package v1.0. Field-level definitions of master data are owned by the Data Dictionary US-DD-001 v1.0; rules and rates by the Country Configuration Guide US-CCG-001 v1.0. |  |  |  |
|  | Channel | Every return is transmitted by the third-party filing provider acting as reporting agent (Form 8655 for federal returns). The payroll produces the data set of the field model; the provider maps it to the authority wire format. |  |  |  |
|  | Limitations | Open points are written in place with an open-point reference and listed in the Report Matrix accuracy note. No value is assumed where the official source has not been read. |  |  |  |

## Report Matrix

| US-DOR-004 EMPLOYER PAYROLL TRANSIT LEVIES (OREGON, NEW YORK) |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| Document ID | US-DOR-004 |  |  |  |  |  |  |  |  |
| Document Title | US-DOR-004 Employer Payroll Transit Levies (Oregon, New York) |  |  |  |  |  |  |  |  |
| Country | United States of America |  |  |  |  |  |  |  |  |
| Authority | Oregon Department of Revenue; New York State Department of Taxation and Finance |  |  |  |  |  |  |  |  |
| Report Type | Outbound statutory return (employer to authority, through the filing provider hand-off) |  |  |  |  |  |  |  |  |
| Tax Type | Employer payroll transit taxes |  |  |  |  |  |  |  |  |
| Relationship | Oregon levies are carried on Form OQ (US-DOR-001 OR section) |  |  |  |  |  |  |  |  |
| Frequency | Quarterly |  |  |  |  |  |  |  |  |
| Submission Deadline | Per levy (Report Matrix) |  |  |  |  |  |  |  |  |
| File Format | Per levy channel: Oregon on Form OQ; New York MCTMT on Form MTA-305. FIELD MODEL: logical model - not the wire/submission format. |  |  |  |  |  |  |  |  |
| File Extension | Per jurisdiction (see Report Matrix) |  |  |  |  |  |  |  |  |
| Character Encoding | Per jurisdiction (ASCII for fixed-length layouts) |  |  |  |  |  |  |  |  |
| Record Length | Per jurisdiction |  |  |  |  |  |  |  |  |
| Record Types / Sections | Amounts; OR and NY sections |  |  |  |  |  |  |  |  |
| Version | 1.0 |  |  |  |  |  |  |  |  |
| Created Date | 2027-03-31 |  |  |  |  |  |  |  |  |
| Created By | Mercans Compliance Regulations Team |  |  |  |  |  |  |  |  |
| Official Source | https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf; https://www.tax.ny.gov/forms/current-forms/mta/mta305i.htm |  |  |  |  |  |  |  |  |
| Last Update Reference | Pages as read for this release |  |  |  |  |  |  |  |  |
| Similar To | US-DOR-001 |  |  |  |  |  |  |  |  |
| ═══ REPORT MATRIX ═══ |  |  |  |  |  |  |  |  |  |
| Report ID | Report Name (EN) | Report Name (Local) | Authority | Frequency | Due Date Rule | Submission Method | File Format | Legal Basis | Accuracy Assessment |
| US-DOR-004-NY | New York: employer payroll transit levy | MTA-305 quarterly | NY Department of Taxation and Finance | Quarterly | Quarterly; due dates in row DOR-NY-002 (MTA-305 quarterly) | online_form (NY DTF Web File) | Form MTA-305 through NY DTF Web File. FIELD MODEL: logical model - not the wire/submission format. | [US-NY-003] [US-NYS6-001]; https://www.tax.ny.gov/forms/current-forms/mta/mta305i.htm | Channel: online_form \| Portal: NY DTF Web File https://www.tax.ny.gov/forms/current-forms/mta/mta305i.htm \| Source: https://www.tax.ny.gov/forms/current-forms/mta/mta305i.htm \| TO CONFIRM. Accuracy 85% (MTA-305 instructions read: lines, rates by zone and band, threshold, due dates; form PDF not held). Closes with: the MTA-305 form itself and a real filing or the provider's acceptance report. |
| US-DOR-004-OR | Oregon: employer payroll transit levy | Form OQ combined quarterly (withholding, UI, Paid Leave, WBF, TriMet, Lane Transit, STT) + Schedule B + Form 132 (wage and hour detail) via Frances Online | Oregon Department of Revenue with OED and DCBS | Quarterly | 2026: 2026-04-30, 2026-07-31, 2026-11-02, 2027-02-01; filed even with no payroll | online_form (Frances Online) | Portal or form as stated in column C. FIELD MODEL: logical model - not the wire/submission format. | [US-ORS5-010]; https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf | Channel: online_form \| Portal: Frances Online \| Source: https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf \| CONFIRMED. Accuracy 75% (form and timing read; channel detail from the form rule). Closes with: a real filing or the provider's acceptance report for this jurisdiction. |

## Payroll Scope Summary

| US-DOR-004 EMPLOYER PAYROLL TRANSIT LEVIES (OREGON, NEW YORK) — PAYROLL SCOPE SUMMARY |  |  |
|---|---|---|
| Employer-borne payroll transit levies. |  |  |
| SCENARIO | REPORT? | NOTES / REASONING |
| ═══ WHO GETS REPORTED ═══ |  |  |
| Employers with payroll in a transit district or MCTMT zone | YES | Sections. |
| ═══ TIMING & RELATIONSHIP ═══ |  |  |
| Oregon on the combined Form OQ | YES | Form OQ combined quarterly (withholding, UI, Paid Leave, WBF, TriMet, Lane Transit, STT) + Schedule B + Form 132 (wage and hour detail) via Frances Online |
| New York MTA-305 | YES | MTA-305 quarterly |
| ═══ AMOUNTS & CALCULATIONS ═══ |  |  |
| Employer-borne rates | YES | TRN-C-002. |
| Oregon statewide transit tax (employee) | NO | Withheld from employees, on Form OQ (US-DOR-001): 0.1%. |
| ═══ SPECIAL CASES ═══ |  |  |
| Nonresident alien employees | PARTIAL | Reported like other employees unless the jurisdiction rule in its section says otherwise; federal treaty exemptions do not change State reporting by themselves. |
| Household and agricultural employees (State level) | NO | State-level rules for special populations are deferred to a later round [US-OWN-005]. |
| Independent contractors | NO | Out of scope [US-OWN-008]. |

## Transit Levy Spec

| Field Name (EN) | Field Name (Authority label, EN) | Record Type | Field Position | Payroll Field (Y/N) | Mandatory (Y/N/C) | Conditional Reason | Position (Start-End) | Field Length | Format | Example | System Mapping | Field Explanation | Relevant for Payroll | Option Values | Rounding | Negative (Y/N) | Value Type | Reporting Frequency | Query to RA | RA Comments |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ═══ COMMON FIELD MODEL (all jurisdictions) ═══ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Payroll subject to the transit levy | Payroll | Amounts | TRN-C-001 | Y | Y | Not conditional. | Logical field (field model) | Money | Decimal 13.2 | 100,000.00 | Payroll result: wages per transit district / zone | Oregon: wages for work in the district (TriMet / Lane transit district of work). New York: MCTMT zone payroll. Taken from the payroll results per transit district or zone of work, one amount per district or zone and quarter, in cents. The district or zone comes from the work location in the Data Dictionary; wages for work outside every district are not included, and the tax of row TRN-C-002 is computed from this amount. | Yes | Not applicable | Cents | N | Input (Amount) | Quarterly | No open query. |  |
| Employer transit tax due | Tax due | Amounts | TRN-C-002 | N | Y | Not conditional. | Logical field (field model) | Money | Decimal 13.2 | See Example Analysis | Calculated by the return generator | Employer transit tax due for the quarter, computed by the return generator from the wages of row TRN-C-001 and never keyed. Oregon: wages for work in the district x TriMet 0.8237% or Lane Transit 0.8% [US-ORS5-010], carried on the combined Oregon return (US-DOR-001). New York MCTMT: zone payroll x the rate of its payroll band (rate table in the NY section). The tax is employer-borne and never withheld from employees; it is rounded to the cent, half-up (see Example Analysis). | Yes | Not applicable | Cents | N | Calculated | Quarterly | No open query. |  |
| ═══ NY: NEW YORK ═══ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| NY Return form and filing rule | New York authority wording (English filing language) | Jurisdiction parameter: NY | DOR-NY-001 | N | Y | Not conditional: applies to every employer filing this return in the jurisdiction. | Return level (not a file position) | Not applicable (configuration value) | Code / rule | Form generated for the 2026 period | Jurisdiction configuration (system constant) | New York: return form and filing rule: MTA-305 quarterly. Names the authority form generated for the period and the condition under which it applies. [US-NY-003] Source type: Web research (official authority page). https://www.tax.ny.gov/forms/current-forms/mta/mta305i.htm | Yes: governs how the quarterly return is produced for New York | Value as stated in column M | Not applicable | N | Input (Rule) | Quarterly | No open query. |  |
| NY Reporting rule | New York authority wording (English filing language) | Jurisdiction parameter: NY | DOR-NY-002 | N | C | Applies only in the situation stated in column M. | Return level (not a file position) | Not applicable (configuration value) | Rule | Rule applied when its condition occurs | Jurisdiction configuration (system constant) | New York: reporting rule: MTA-305 (MTA-305-I 1/26), quarters from 2025-07-01. Zone 1 (New York, Bronx, Kings, Queens, Richmond) line 2a: payroll 0-375,000 x 0.055%; 375,000-437,500 x 0.115%; 437,500-2,500,000 x 0.60%; > 2,500,000 x 0.895% (local government employer max 0.60%). Zone 2 (Rockland, Nassau, Suffolk, Orange, Putnam, Dutchess, Westchester) line 2b: 0.055% / 0.115% / 0.34% / 0.635% (local government employers exempt). Rate applies to the whole zone payroll. Lines: A1/A2/A3 covered employees Zone 1/Zone 2/total; B special condition code G1 (local government); C final payroll date; 1a Zone 1 payroll expense; 1b Zone 2; 1c total MCTD payroll (not > 312,500 -> not subject); 2a, 2b tax by zone; 2c total MCTMT; 3 PrompTax payments and prior overpayment; 4 balance due (2c - 3); 5 overpayment; 6a refund / 6b credit. Due Apr 30, Jul 31, Oct 31, Jan 31; no extensions; Web File.. Applied by the payroll when the situation named in the rule occurs. [US-NYS6-001] Source type: Web research (official authority page). https://www.tax.ny.gov/forms/current-forms/mta/mta305i.htm | Yes: governs how the quarterly return is produced for New York | Value as stated in column M | Not applicable | N | Input (Rule) | Quarterly | No open query. |  |
| NY Reporting rule | New York authority wording (English filing language) | Jurisdiction parameter: NY | DOR-NY-003 | N | C | Applies only in the situation stated in column M. | Return level (not a file position) | Not applicable (configuration value) | Rule | Rule applied when its condition occurs | Jurisdiction configuration (system constant) | New York: reporting rule: MCTMT zone payroll. Applied by the payroll when the situation named in the rule occurs. [US-NY-003] Source type: Web research (official authority page). https://www.tax.ny.gov/forms/current-forms/mta/mta305i.htm | Yes: governs how the quarterly return is produced for New York | Value as stated in column M | Not applicable | N | Input (Rule) | Quarterly | No open query. |  |
| MCTMT quarterly payroll threshold | Line 1c test | Jurisdiction parameter: NY | DOR-NY-004 | N | Y | Not conditional: tested every quarter. | Form line 1c | Amount | Whole dollars | See Example Analysis | Jurisdiction configuration (system constant) | New York: an employer whose total MCTD payroll expense of the quarter (MTA-305 line 1c) is not above 312,500 USD [US-NYS6-001] is not subject for that quarter. The return generator compares the employer's payroll expense of the quarter (the total of the zone payroll of row TRN-C-001 for New York) with this value every quarter; when it is not above the value no MCTMT is computed for the quarter. The value is held in the jurisdiction configuration in whole dollars and is re-read each year from the form instructions. [US-NYS6-001] Source type: Web research (official authority page). https://www.tax.ny.gov/forms/current-forms/mta/mta305i.htm | Yes: decides whether MTA-305 tax is due | Value as stated in column M | Whole units as published | N | Input (Amount) | Quarterly | No open query. |  |
| MCTMT Zone 1 rate table (line 2a) | Zone 1 rates | Jurisdiction parameter: NY | DOR-NY-005 | N | C | Only for payroll expense in Zone 1; back-reference to TRN-C-001 and TRN-C-002. | Form line 2a | Rate | Percent | See Example Analysis | US-DD-001 v1.0: New York MCTMT zone; rate table per zone (system constant) | New York MCTMT, Zone 1, quarters from 2025-07-01: payroll up to 375,000 USD: 0.055%; above 375,000 USD up to 437,500 USD: 0.115%; above 437,500 USD up to 2,500,000 USD: 0.6%; above 2,500,000 USD: 0.895% [US-NYS6-001]. The rate of the band applies to the whole Zone 1 payroll of the quarter (no marginal split). Counties and the local government rule: row of the MTA-305 lines and rates. [US-NYS6-001] Source type: Web research (official authority page). https://www.tax.ny.gov/forms/current-forms/mta/mta305i.htm | Yes: computes MTA-305 line 2a | Bands as stated in column M | Rates as published | N | Input (Rate) | Quarterly | Confirm against a real filing: the band is read from the Zone 1 payroll of the quarter [US-NYS6-001]. |  |
| MCTMT Zone 2 rate table (line 2b) | Zone 2 rates | Jurisdiction parameter: NY | DOR-NY-006 | N | C | Only for payroll expense in Zone 2; back-reference to TRN-C-001 and TRN-C-002. | Form line 2b | Rate | Percent | See Example Analysis | US-DD-001 v1.0: New York MCTMT zone; rate table per zone (system constant) | New York MCTMT, Zone 2, quarters from 2025-07-01: payroll up to 375,000 USD: 0.055%; above 375,000 USD up to 437,500 USD: 0.115%; above 437,500 USD up to 2,500,000 USD: 0.34%; above 2,500,000 USD: 0.635% [US-NYS6-001]. The rate of the band applies to the whole Zone 2 payroll of the quarter (no marginal split). Counties and the local government rule: row of the MTA-305 lines and rates. [US-NYS6-001] Source type: Web research (official authority page). https://www.tax.ny.gov/forms/current-forms/mta/mta305i.htm | Yes: computes MTA-305 line 2b | Bands as stated in column M | Rates as published | N | Input (Rate) | Quarterly | Confirm against a real filing: the band is read from the Zone 2 payroll of the quarter [US-NYS6-001]. |  |
| ═══ OR: OREGON ═══ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| OR Return form and filing rule | Oregon authority wording (English filing language) | Jurisdiction parameter: OR | DOR-OR-001 | N | Y | Not conditional: applies to every employer filing this return in the jurisdiction. | Return level (not a file position) | Not applicable (configuration value) | Code / rule | Form generated for the 2026 period | Jurisdiction configuration (system constant) | Oregon: return form and filing rule: Form OQ combined quarterly (withholding, UI, Paid Leave, WBF, TriMet, Lane Transit, STT) + Schedule B + Form 132 (wage and hour detail) via Frances Online. Names the authority form generated for the period and the condition under which it applies. [US-ORS5-010] Source type: Official spec. https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf | Yes: governs how the quarterly return is produced for Oregon | Value as stated in column M | Not applicable | N | Input (Rule) | Quarterly | No open query. |  |
| OR Due date rule | Oregon authority wording (English filing language) | Jurisdiction parameter: OR | DOR-OR-002 | N | Y | Not conditional: applies to every employer filing this return in the jurisdiction. | Return level (not a file position) | Not applicable (configuration value) | Date rule | 2026 Q1 return: due per the rule in column M | Filing calendar of the payroll (system constant per jurisdiction) | Oregon: due date rule: 2026: 2026-04-30, 2026-07-31, 2026-11-02, 2027-02-01; filed even with no payroll. Drives the filing calendar for the provider hand-off; a due date on a Saturday, Sunday or legal holiday follows the roll-forward stated in the rule or the authority's calendar. [US-ORS5-010] Source type: Official spec. https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf | Yes: governs how the quarterly return is produced for Oregon | Value as stated in column M | Not applicable | N | Input (Rule) | Quarterly | No open query. |  |
| OR Contribution or tax rate | Oregon authority wording (English filing language) | Jurisdiction parameter: OR | DOR-OR-003 | N | C | Applies to the base and payer stated in column M for employers liable in the jurisdiction. | Return level (not a file position) | Not applicable (configuration value) | Rate | Rate applied to the period base | Jurisdiction rate table (dated system constant) | Oregon: contribution or tax rate: 0.8237% (TriMet transit district employer rate), borne by the employer. The payroll applies the rate to the base and payer stated in this row for each period; the amount is computed by the payroll from the period results, never keyed. [US-ORS5-010] Source type: Web research (official authority page). https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf | Yes: governs how the quarterly return is produced for Oregon | Value as stated in column M | As published (decimal places of the source kept) | N | Input (Rate) | Quarterly | No open query. |  |
| OR Contribution or tax rate | Oregon authority wording (English filing language) | Jurisdiction parameter: OR | DOR-OR-004 | N | C | Applies to the base and payer stated in column M for employers liable in the jurisdiction. | Return level (not a file position) | Not applicable (configuration value) | Rate | Rate applied to the period base | Jurisdiction rate table (dated system constant) | Oregon: contribution or tax rate: 0.8% (Lane transit district employer rate), borne by the employer. The payroll applies the rate to the base and payer stated in this row for each period; the amount is computed by the payroll from the period results, never keyed. [US-ORS5-010] Source type: Web research (official authority page). https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf | Yes: governs how the quarterly return is produced for Oregon | Value as stated in column M | As published (decimal places of the source kept) | N | Input (Rate) | Quarterly | No open query. |  |

## File Structure

| US-DOR-004 Employer Payroll Transit Levies (Oregon, New York) — FILE STRUCTURE AND TECHNICAL SPECIFICATIONS |
|---|
| ═══ FILE FORMAT ═══ |
| FIELD MODEL: logical model - not the wire/submission format for the common field model; each jurisdiction's own channel and layout are in its section of the core sheet and in the Report Matrix. |
| Where a jurisdiction layout is published and read, its positions are given in the jurisdiction section; otherwise the provider maps the field model to the authority format. |
| FORMAT TO CONFIRM vs a real filing in every jurisdiction. |
| ═══ NEW YORK FORM MTA-305 ═══ |
| MTA-305 (MTA-305-I 1/26), quarters from 2025-07-01. Zone 1 (New York, Bronx, Kings, Queens, Richmond) line 2a: payroll 0-375,000 x 0.055%; 375,000-437,500 x 0.115%; 437,500-2,500,000 x 0.60%; > 2,500,000 x 0.895% (local government employer max 0.60%). Zone 2 (Rockland, Nassau, Suffolk, Orange, Putnam, Dutchess, Westchester) line 2b: 0.055% / 0.115% / 0.34% / 0.635% (local government employers exempt). Rate applies to the whole zone payroll. Lines: A1/A2/A3 covered employees Zone 1/Zone 2/total; B special condition code G1 (local government); C final payroll date; 1a Zone 1 payroll expense; 1b Zone 2; 1c total MCTD payroll (not > 312,500 -> not subject); 2a, 2b tax by zone; 2c total MCTMT; 3 PrompTax payments and prior overpayment; 4 balance due (2c - 3); 5 overpayment; 6a refund / 6b credit. Due Apr 30, Jul 31, Oct 31, Jan 31; no extensions; Web File. [US-NYS6-001] |

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
| ═══ PAYROLL-SPECIFIC POPULATION RULES ═══ |  |  |  |  |
| Conditional | TRN-NY MCTMT zone rate tables | Work location zone; payroll expense per zone | Each quarter, total the payroll expense per MCTMT zone from the work location of each employee; if the total of both zones is not above the quarterly threshold no MCTMT is due for the quarter, otherwise each zone's payroll is taxed at the rate of its band. | Local government employers follow the special rule of the MTA-305 instructions (row of the MTA-305 lines and rates). |
| ═══ CONDITIONAL JURISDICTION PARAMETERS ═══ |  |  |  |  |
| Conditional (jurisdiction) | DOR-NY-002 NY Reporting rule | Jurisdiction configuration | NY Reporting rule: Applies only in the situation stated in column M. The rule text and figure are in column M of row DOR-NY-002; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-DOR-004 Employer Payroll Transit Levies (Oregon, New York). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |
| Conditional (jurisdiction) | DOR-NY-003 NY Reporting rule | Jurisdiction configuration | NY Reporting rule: Applies only in the situation stated in column M. The rule text and figure are in column M of row DOR-NY-003; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-DOR-004 Employer Payroll Transit Levies (Oregon, New York). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |
| Conditional (jurisdiction) | DOR-NY-005 MCTMT Zone 1 rate table (line 2a) | Jurisdiction configuration | MCTMT Zone 1 rate table (line 2a): Only for payroll expense in Zone 1; back-reference to TRN-C-001 and TRN-C-002. The rule text and figure are in column M of row DOR-NY-005; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-DOR-004 Employer Payroll Transit Levies (Oregon, New York). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |
| Conditional (jurisdiction) | DOR-NY-006 MCTMT Zone 2 rate table (line 2b) | Jurisdiction configuration | MCTMT Zone 2 rate table (line 2b): Only for payroll expense in Zone 2; back-reference to TRN-C-001 and TRN-C-002. The rule text and figure are in column M of row DOR-NY-006; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-DOR-004 Employer Payroll Transit Levies (Oregon, New York). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |
| Conditional (jurisdiction) | DOR-OR-003 OR Contribution or tax rate | Jurisdiction configuration | OR Contribution or tax rate: Applies to the base and payer stated in column M for employers liable in the jurisdiction. The rule text and figure are in column M of row DOR-OR-003; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-DOR-004 Employer Payroll Transit Levies (Oregon, New York). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |
| Conditional (jurisdiction) | DOR-OR-004 OR Contribution or tax rate | Jurisdiction configuration | OR Contribution or tax rate: Applies to the base and payer stated in column M for employers liable in the jurisdiction. The rule text and figure are in column M of row DOR-OR-004; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-DOR-004 Employer Payroll Transit Levies (Oregon, New York). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |

## Example Analysis

| US-DOR-004 Employer Payroll Transit Levies (Oregon, New York) — EXAMPLE FILE ANALYSIS |  |  |  |
|---|---|---|---|
| Raw Value | Field Name | Interpretation | Notes |
| ═══ WORKED EXAMPLE: OREGON EMPLOYER TRANSIT TAXES ON 100,000.00 (constructed) ═══ |  |  |  |
| 823.70 | TriMet | 100,000.00 x 0.8237% | Half-up |
| 800.00 | Lane Transit | 100,000.00 x 0.8% | Half-up |
| ═══ WORKED EXAMPLE 2: NEW YORK MCTMT FOR ONE QUARTER (constructed) ═══ |  |  |  |
| 1,000,000.00 | Zone 1 payroll expense (line 1a) | Constructed input | Input |
| 200,000.00 | Zone 2 payroll expense (line 1b) | Constructed input | Input |
| 1,200,000.00 | Total MCTD payroll expense (line 1c) | 1,000,000.00 + 200,000.00; above 312,500: subject | Threshold test |
| 6,000.00 | Zone 1 tax (line 2a) | 1,000,000.00 is in band 3: 1,000,000.00 x 0.6% | Whole zone payroll at the band rate; half-up to the cent |
| 110.00 | Zone 2 tax (line 2b) | 200,000.00 is in band 1: 200,000.00 x 0.055% | Whole zone payroll at the band rate; half-up to the cent |
| 6,110.00 | Total MCTMT (line 2c) | 6,000.00 + 110.00 | Calculation |

## Sample File

| US-DOR-004 Employer Payroll Transit Levies (Oregon, New York) — SAMPLE FILE |
|---|
| No official sample filing is held for these returns and none is constructed. Verified channels: the per-jurisdiction channel classes and portals in the Report Matrix (column G and the accuracy note). |


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `dd.employer.ny_mctmt_zone` | MCTMT zone payroll | from 2025-07-01 | US-NY-003 |
| `dd.or.transit_district` | TriMet / Lane transit district of work | from 2026-01-01 to 2026-12-31 | US-ORS5-010 |
| `or.stt.employee.rate` | 0.1 | from 2018-07-01 | US-ORS5-011 |
| `or.transit.lane.employer.rate` | 0.8 | from 2026-01-01 to 2026-12-31 | US-ORS5-010 |
| `or.transit.trimet.employer.rate` | 0.8237 | from 2026-01-01 to 2026-12-31 | US-ORS5-010 |
| `rspec.ny.mctmt.band.1.ceiling` | 375,000 | from 2025-07-01 | US-NYS6-001 |
| `rspec.ny.mctmt.band.2.ceiling` | 437,500 | from 2025-07-01 | US-NYS6-001 |
| `rspec.ny.mctmt.band.3.ceiling` | 2,500,000 | from 2025-07-01 | US-NYS6-001 |
| `rspec.ny.mctmt.form` | MTA-305 quarterly | from 2025-07-01 | US-NY-003 |
| `rspec.ny.mctmt.quarterly_threshold` | 312,500 | from 2025-07-01 | US-NYS6-001 |
| `rspec.ny.mctmt.rates_lines` | MTA-305 (MTA-305-I 1/26), quarters from 2025-07-01. Zone 1 (New York, Bronx, Kings, Queens, Richmond) line 2a: payroll 0-375,000 x 0.055%; 375,000-437,500 x 0.115%; 437,500-2,500,000 x 0.60%; > 2,500,000 x 0.895% (local government employer max 0.60%). Zone 2 (Rockland, Nassau, Suffolk, Orange, Putnam, Dutchess, Westchester) line 2b: 0.055% / 0.115% / 0.34% / 0.635% (local government employers exempt). Rate applies to the whole zone payroll. Lines: A1/A2/A3 covered employees Zone 1/Zone 2/total; B special condition code G1 (local government); C final payroll date; 1a Zone 1 payroll expense; 1b Zone 2; 1c total MCTD payroll (not > 312,500 -> not subject); 2a, 2b tax by zone; 2c total MCTMT; 3 PrompTax payments and prior overpayment; 4 balance due (2c - 3); 5 overpayment; 6a refund / 6b credit. Due Apr 30, Jul 31, Oct 31, Jan 31; no extensions; Web File. | from 2025-07-01 | US-NYS6-001 |
| `rspec.ny.mctmt.zone1.band.1.rate` | 0.055 | from 2025-07-01 | US-NYS6-001 |
| `rspec.ny.mctmt.zone1.band.2.rate` | 0.115 | from 2025-07-01 | US-NYS6-001 |
| `rspec.ny.mctmt.zone1.band.3.rate` | 0.6 | from 2025-07-01 | US-NYS6-001 |
| `rspec.ny.mctmt.zone1.band.4.rate` | 0.895 | from 2025-07-01 | US-NYS6-001 |
| `rspec.ny.mctmt.zone2.band.1.rate` | 0.055 | from 2025-07-01 | US-NYS6-001 |
| `rspec.ny.mctmt.zone2.band.2.rate` | 0.115 | from 2025-07-01 | US-NYS6-001 |
| `rspec.ny.mctmt.zone2.band.3.rate` | 0.34 | from 2025-07-01 | US-NYS6-001 |
| `rspec.ny.mctmt.zone2.band.4.rate` | 0.635 | from 2025-07-01 | US-NYS6-001 |
| `rspec.or.oq.due` | 2026: 2026-04-30, 2026-07-31, 2026-11-02, 2027-02-01; filed even with no payroll | from 2026-01-01 to 2026-12-31 | US-ORS5-010 |
| `rspec.or.oq.form` | Form OQ combined quarterly (withholding, UI, Paid Leave, WBF, TriMet, Lane Transit, STT) + Schedule B + Form 132 (wage and hour detail) via Frances Online | from 2026-01-01 to 2026-12-31 | US-ORS5-010 |

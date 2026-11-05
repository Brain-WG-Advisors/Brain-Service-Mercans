# US-WC-001-StateFundWorkersComp-Spec


## Version Control

|  | Statutory Report Specification |  |  |  |  |
|---|---|---|---|---|---|
|  | United States of America |  |  |  |  |
|  | US-WC-001 State-Fund Workers' Compensation Premiums and Fees Collected through Payroll (WA, NM, OR, WY) |  |  |  |  |
|  | Document ID | US-WC-001 |  |  |  |
|  | Version | Effective Date | Change Description | Status | Updated By |
|  | 1.0 | 2027-03-31 00:00:00 | For QA. | For QA | Wallisson Gomes |
|  | REMARKS |  |  |  |  |
|  | Topic | Remark |  |  |  |
|  | Scope | One Report Specification per authority return in scope for the United States package v1.0. Field-level definitions of master data are owned by the Data Dictionary US-DD-001 v1.0; rules and rates by the Country Configuration Guide US-CCG-001 v1.0. |  |  |  |
|  | Channel | Every return is transmitted by the third-party filing provider acting as reporting agent (Form 8655 for federal returns). The payroll produces the data set of the field model; the provider maps it to the authority wire format. |  |  |  |
|  | Limitations | Open points are written in place with an open-point reference and listed in the Report Matrix accuracy note. No value is assumed where the official source has not been read. |  |  |  |

## Report Matrix

| US-WC-001 STATE-FUND WORKERS' COMPENSATION PREMIUMS AND FEES COLLECTED THROUGH PAYROLL (WA, NM, OR, WY) |  |  |  |  |  |  |  |  |  |
|---|---|---|---|---|---|---|---|---|---|
| Document ID | US-WC-001 |  |  |  |  |  |  |  |  |
| Document Title | US-WC-001 State-Fund Workers' Compensation Premiums and Fees Collected through Payroll (WA, NM, OR, WY) |  |  |  |  |  |  |  |  |
| Country | United States of America |  |  |  |  |  |  |  |  |
| Authority | WA Department of Labor & Industries; NM Taxation and Revenue Department; OR Department of Revenue; WY Department of Workforce Services |  |  |  |  |  |  |  |  |
| Report Type | Outbound statutory return (employer to authority, through the filing provider hand-off) |  |  |  |  |  |  |  |  |
| Tax Type | Workers' compensation premiums and fees |  |  |  |  |  |  |  |  |
| Relationship | NM fee on TRD-41431 and OR WBF on Form OQ (US-DOR-001); WY joint UI / WC report (US-UI-001) |  |  |  |  |  |  |  |  |
| Frequency | Quarterly (WY monthly, quarterly by permission) |  |  |  |  |  |  |  |  |
| Submission Deadline | Per State (Report Matrix) |  |  |  |  |  |  |  |  |
| File Format | Per State channel (Report Matrix). FIELD MODEL: logical model - not the wire/submission format. |  |  |  |  |  |  |  |  |
| File Extension | Per jurisdiction (see Report Matrix) |  |  |  |  |  |  |  |  |
| Character Encoding | Per jurisdiction (ASCII for fixed-length layouts) |  |  |  |  |  |  |  |  |
| Record Length | Per jurisdiction |  |  |  |  |  |  |  |  |
| Record Types / Sections | Amounts; State sections |  |  |  |  |  |  |  |  |
| Version | 1.0 |  |  |  |  |  |  |  |  |
| Created Date | 2027-03-31 |  |  |  |  |  |  |  |  |
| Created By | Mercans Compliance Regulations Team |  |  |  |  |  |  |  |  |
| Official Source | State pages cited per row |  |  |  |  |  |  |  |  |
| Last Update Reference | Pages as read for this release |  |  |  |  |  |  |  |  |
| Similar To | US-DOR-001; US-UI-001 |  |  |  |  |  |  |  |  |
| ═══ REPORT MATRIX ═══ |  |  |  |  |  |  |  |  |  |
| Report ID | Report Name (EN) | Report Name (Local) | Authority | Frequency | Due Date Rule | Submission Method | File Format | Legal Basis | Accuracy Assessment |
| US-WC-001-NM | New Mexico: State-fund workers' compensation report | TRD-41431 (new 2026-01-01): WC fee return + employee quarterly wage and withholding report, 25th after quarter | New Mexico Taxation and Revenue Department | Quarterly | As stated in column C (TRD-41431 (new 2026-01-01): WC fee return + employee quarterly wage and withholding report, 25th after quarter) | online_form | Portal or form as stated in column C. FIELD MODEL: logical model - not the wire/submission format. | [US-NMR3-001] [US-NMS5-012]; https://www.tax.newmexico.gov/businesses/workers-compensation/ https://www.tax.newmexico.gov/individuals/wp-content/uploads/sites/5/2026/05/E-file-E-pay-Mandate.pdf | Channel: online_form \| Portal: not named in the cited channel sources \| Source: https://www.tax.newmexico.gov/individuals/wp-content/uploads/sites/5/2026/05/E-file-E-pay-Mandate.pdf \| CONFIRMED. Accuracy 75% (form and timing read; channel detail from the form rule). Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-WC-001-OR | Oregon: State-fund workers' compensation report | Form OQ combined quarterly (withholding, UI, Paid Leave, WBF, TriMet, Lane Transit, STT) + Schedule B + Form 132 (wage and hour detail) via Frances Online | Oregon Department of Revenue with OED and DCBS | Quarterly | As stated in column C (Form OQ combined quarterly (withholding, UI, Paid Leave, WBF, TriMet, Lane Transit, STT) + Schedule B + Form 132 (wage and hour detail) via Frances Online) | online_form (Frances Online) | Portal or form as stated in column C. FIELD MODEL: logical model - not the wire/submission format. | [US-ORS5-010]; https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf | Channel: online_form \| Portal: Frances Online \| Source: https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf \| CONFIRMED. Accuracy 75% (form and timing read; channel detail from the form rule). Closes with: a real filing or the provider's acceptance report for this jurisdiction. |
| US-WC-001-WA | Washington: State-fund workers' compensation report | employer (not self-insured) deducts from each worker one-half of the medical aid premium per hour per risk class | Washington State Department of Labor & Industries | Quarterly | As stated in column C (employer (not self-insured) deducts from each worker one-half of the medical aid premium per hour per risk class) | online_form | Not configured in this release (open gap RSPEC-GAP-042) | [US-WAS5-019] [US-WAS7-001]; https://app.leg.wa.gov/RCW/default.aspx?cite=51.16.140 https://lni.wa.gov/insurance/_docs/2026RatesByClassCodeFund.xlsx | Channel: online_form \| Portal: not named in the cited channel sources \| Source: https://app.leg.wa.gov/RCW/default.aspx?cite=51.16.140 \| CONFIRMED. Accuracy 75% (form and timing read; channel detail from the form rule). Closes with: the L&I Employer Quarterly Report instructions or the WAC 296-17 reporting sections (open gap RSPEC-GAP-042). |
| US-WC-001-WY | Wyoming: State-fund workers' compensation report | workers compensation payroll report monthly (quarterly by permission), joint UI/WC reporting | Wyoming Department of Workforce Services | workers compensation payroll report monthly (quarterly by permission), joint UI/WC reporting | As stated in column C | online_form | Portal or form as stated in column C. FIELD MODEL: logical model - not the wire/submission format. | [US-WYS5-007]; https://wyoleg.gov/statutes/compress/title27.pdf | Channel: online_form \| Portal: not named in the cited channel sources \| Source: https://wyoleg.gov/statutes/compress/title27.pdf \| TO CONFIRM. Accuracy 75% (form and timing read; channel detail from the form rule). Closes with: a real filing or the provider's acceptance report for this jurisdiction. |

## Payroll Scope Summary

| US-WC-001 STATE-FUND WORKERS' COMPENSATION PREMIUMS AND FEES COLLECTED THROUGH PAYROLL (WA, NM, OR, WY) — PAYROLL SCOPE SUMMARY |  |  |
|---|---|---|
| Workers' compensation amounts collected through payroll for State funds; private insurer premiums are outside payroll. |  |  |
| SCENARIO | REPORT? | NOTES / REASONING |
| ═══ WHO GETS REPORTED ═══ |  |  |
| Employees covered by a State fund collected through payroll | YES | State sections. |
| Private insurer premiums in other States | NO | Outside payroll (MANDATE workers' compensation row). |
| ═══ TIMING & RELATIONSHIP ═══ |  |  |
| Quarterly or monthly reports | YES | workers compensation payroll report monthly (quarterly by permission), joint UI/WC reporting |
| ═══ AMOUNTS & CALCULATIONS ═══ |  |  |
| Employee shares deducted | YES | WC-C-002. |
| ═══ SPECIAL CASES ═══ |  |  |
| Nonresident alien employees | PARTIAL | Reported like other employees unless the jurisdiction rule in its section says otherwise; federal treaty exemptions do not change State reporting by themselves. |
| Household and agricultural employees (State level) | NO | State-level rules for special populations are deferred to a later round [US-OWN-005]. |
| Independent contractors | NO | Out of scope [US-OWN-008]. |

## State Fund WC Spec

| Field Name (EN) | Field Name (Authority label, EN) | Record Type | Field Position | Payroll Field (Y/N) | Mandatory (Y/N/C) | Conditional Reason | Position (Start-End) | Field Length | Format | Example | System Mapping | Field Explanation | Relevant for Payroll | Option Values | Rounding | Negative (Y/N) | Value Type | Reporting Frequency | Query to RA | RA Comments |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| ═══ COMMON FIELD MODEL (all jurisdictions) ═══ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Hours worked or employees covered in the period | Hours / employees | Amounts | WC-C-001 | Y | Y | Not conditional. | Logical field (field model) | Count | N | 520 | Payroll result: hours per risk class / covered employees | Hours worked, or employees covered, in the period: the quantity the State-fund premium or fee is charged on. Washington premiums are per hour by risk class (employer (not self-insured) deducts from each worker one-half of the medical aid premium per hour per risk class); the Oregon Workers' Benefit Fund is 0.018 USD per hour [US-ORS5-010]; the New Mexico fee is per employee per quarter. Taken from the hours per risk class or the covered-employee count of the payroll results, in whole hours; an employee with no hours in the period is not counted. | Yes | Not applicable | Whole hours | N | Input (Count) | Quarterly | No open query. |  |
| Employee share deducted | Employee share | Amounts | WC-C-002 | Y | Y | Not conditional. | Logical field (field model) | Money | Decimal 13.2 | See Example Analysis | Payroll result: WC employee deduction | Employee share of the State-fund premium or fee deducted from pay in the period, taken from the WC employee deduction of the payroll results. New Mexico employee part 2.25 USD a quarter [US-NMR3-001]; Washington: the worker share defined in row WC-C-001; Oregon half of the WBF (State annexes of US-CCG-001 v1.0). Reported in cents; a fund without an employee share leaves the field at zero. | Yes | Not applicable | Cents | N | Input (Amount) | Quarterly | No open query. |  |
| Employer share | Employer share | Amounts | WC-C-003 | N | Y | Not conditional. | Logical field (field model) | Money | Decimal 13.2 | See Example Analysis | Calculated by the return generator | Employer share of the State-fund premium or fee for the period, computed by the return generator and never keyed. New Mexico employer part 2.55 USD a quarter [US-NMR3-001]; Washington and Oregon: the employer part of the hourly premiums of row WC-C-001; Wyoming monopolistic State fund premiums (workers compensation payroll report monthly (quarterly by permission), joint UI/WC reporting). Rounded to the cent, half-up. | Yes | Not applicable | Cents | N | Calculated | Quarterly | No open query. |  |
| ═══ NM: NEW MEXICO ═══ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| NM Return form and filing rule | New Mexico authority wording (English filing language) | Jurisdiction parameter: NM | WC-NM-001 | N | Y | Not conditional: applies to every employer filing this return in the jurisdiction. | Return level (not a file position) | Not applicable (configuration value) | Code / rule | Form generated for the 2026 period | Jurisdiction configuration (system constant) | New Mexico: return form and filing rule: TRD-41431 (new 2026-01-01): WC fee return + employee quarterly wage and withholding report, 25th after quarter. Names the authority form generated for the period and the condition under which it applies. [US-NMS5-012] Source type: Official spec. https://www.tax.newmexico.gov/individuals/wp-content/uploads/sites/5/2026/05/E-file-E-pay-Mandate.pdf | Yes: governs how the quarterly return is produced for New Mexico | Value as stated in column M | Not applicable | N | Input (Rule) | Quarterly | No open query. |  |
| NM Fee amount | New Mexico authority wording (English filing language) | Jurisdiction parameter: NM | WC-NM-002 | N | C | Applies on the basis stated in column M for employers liable for the fee. | Return level (not a file position) | Not applicable (configuration value) | Amount | Fee charged on the stated basis | Jurisdiction rate table (dated system constant) | New Mexico: fee amount: 2.55 USD per employee per quarter, paid by the employer on Form TRD-41431. The payroll charges the fee on the basis stated in this row for each period and reports it on the return named in the Report Matrix. [US-NMR3-001] Source type: Web research (official authority page). https://www.tax.newmexico.gov/businesses/workers-compensation/ | Yes: governs how the quarterly return is produced for New Mexico | Value as stated in column M | As published (decimal places of the source kept) | N | Input (Amount) | Quarterly | No open query. |  |
| NM Fee amount | New Mexico authority wording (English filing language) | Jurisdiction parameter: NM | WC-NM-003 | N | C | Applies on the basis stated in column M for employers liable for the fee. | Return level (not a file position) | Not applicable (configuration value) | Amount | Fee charged on the stated basis | Jurisdiction rate table (dated system constant) | New Mexico: fee amount: 2.25 USD per covered employee per quarter, deducted from the employee's pay. The payroll charges the fee on the basis stated in this row for each period and reports it on the return named in the Report Matrix. [US-NMR3-001] Source type: Web research (official authority page). https://www.tax.newmexico.gov/businesses/workers-compensation/ | Yes: governs how the quarterly return is produced for New Mexico | Value as stated in column M | As published (decimal places of the source kept) | N | Input (Amount) | Quarterly | No open query. |  |
| ═══ OR: OREGON ═══ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| OR Return form and filing rule | Oregon authority wording (English filing language) | Jurisdiction parameter: OR | WC-OR-001 | N | Y | Not conditional: applies to every employer filing this return in the jurisdiction. | Return level (not a file position) | Not applicable (configuration value) | Code / rule | Form generated for the 2026 period | Jurisdiction configuration (system constant) | Oregon: return form and filing rule: Form OQ combined quarterly (withholding, UI, Paid Leave, WBF, TriMet, Lane Transit, STT) + Schedule B + Form 132 (wage and hour detail) via Frances Online. Names the authority form generated for the period and the condition under which it applies. [US-ORS5-010] Source type: Official spec. https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf | Yes: governs how the quarterly return is produced for Oregon | Value as stated in column M | Not applicable | N | Input (Rule) | Quarterly | No open query. |  |
| OR Rate per hour worked | Oregon authority wording (English filing language) | Jurisdiction parameter: OR | WC-OR-002 | N | C | Applies to the hours worked by the covered employees stated in column M. | Return level (not a file position) | Not applicable (configuration value) | Rate | Hours worked x amount per hour | Jurisdiction rate table (dated system constant) | Oregon: rate per hour worked: 0.018 USD per hour worked (Workers' Benefit Fund assessment), split half employee and half employer. The payroll multiplies the hours worked in the period by this amount per hour; the hours come from the period time and attendance results. [US-ORS5-010] Source type: Web research (official authority page). https://www.oregon.gov/dor/forms/FormsPubs/combined-payroll_211-155-2_2026.pdf | Yes: governs how the quarterly return is produced for Oregon | Value as stated in column M | As published (decimal places of the source kept) | N | Input (Rate) | Quarterly | No open query. |  |
| ═══ WA: WASHINGTON ═══ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| WA Return form and filing rule | Washington authority wording (English filing language) | Jurisdiction parameter: WA | WC-WA-001 | N | Y | Not conditional: applies to every employer filing this return in the jurisdiction. | Return level (not a file position) | Not applicable (configuration value) | Code / rule | Form generated for the 2026 period | Jurisdiction configuration (system constant) | Washington: return form and filing rule: employer (not self-insured) deducts from each worker one-half of the medical aid premium per hour per risk class. Names the authority form generated for the period and the condition under which it applies. [US-WAS7-001] Source type: Web research (official authority page). https://app.leg.wa.gov/RCW/default.aspx?cite=51.16.140 | Yes: governs how the quarterly return is produced for Washington | Value as stated in column M | Not applicable | N | Input (Rule) | Quarterly | No open query. |  |
| WA Rate per hour worked | Washington authority wording (English filing language) | Jurisdiction parameter: WA | WC-WA-002 | N | C | Applies to the hours worked by the covered employees stated in column M. | Return level (not a file position) | Not applicable (configuration value) | Rate | Hours worked x amount per hour | Jurisdiction rate table (dated system constant) | Washington: rate per hour worked: 0.1912 USD per hour worked (Supplemental Pension Fund), the same amount for all risk classes. The payroll multiplies the hours worked in the period by this amount per hour; the hours come from the period time and attendance results. [US-WAS5-019] Source type: Web research (official authority page). https://lni.wa.gov/insurance/_docs/2026RatesByClassCodeFund.xlsx | Yes: governs how the quarterly return is produced for Washington | Value as stated in column M | As published (decimal places of the source kept) | N | Input (Rate) | Quarterly | No open query. |  |
| WA Return parameters and file layout | Washington authority wording (English filing language) | Jurisdiction parameter: WA | WC-WA-003 | N | C | Applies once the open point is closed; until then the return is prepared from the common field model only and checked against the authority portal before submission. | Return level (not a file position) | Not applicable (configuration value) | Text | No value configured | Provider hand-off configuration per jurisdiction (system constant) | Washington: return parameters and file layout: not configured in this release (open gap RSPEC-GAP-042). Open point: the Washington L&I workers' compensation quarterly report (fields, hours basis, due dates) is not part of this release. Closes with: the L&I Employer Quarterly Report instructions or the WAC 296-17 reporting sections. | Yes: Washington quarterly return | Not applicable | Not applicable | N | Input (Rule) | Quarterly | Open point (open gap RSPEC-GAP-042): the L&I Employer Quarterly Report instructions or the WAC 296-17 reporting sections. |  |
| ═══ WY: WYOMING ═══ |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| WY Filing and deposit frequency rule | Wyoming authority wording (English filing language) | Jurisdiction parameter: WY | WC-WY-001 | N | Y | Not conditional: applies to every employer filing this return in the jurisdiction. | Return level (not a file position) | Not applicable (configuration value) | Code / rule | Frequency held as employer master data | US-DD-001 v1.0: State employer account number \| State filing frequency | Wyoming: filing and deposit frequency rule: workers compensation payroll report monthly (quarterly by permission), joint UI/WC reporting. The frequency is employer master data (assigned by the authority or derived from the lookback amount) and selects the period and form of each return. [US-WYS5-007] Source type: Official spec. https://wyoleg.gov/statutes/compress/title27.pdf | Yes: governs how the quarterly return is produced for Wyoming | See Field Options (jurisdiction channel / frequency codes) | Not applicable | N | Input (Rule) | Quarterly | No open query. |  |

## File Structure

| US-WC-001 State-Fund Workers' Compensation Premiums and Fees Collected through Payroll (WA, NM, OR, WY) — FILE STRUCTURE AND TECHNICAL SPECIFICATIONS |
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
| ═══ CONDITIONAL JURISDICTION PARAMETERS ═══ |  |  |  |  |
| Conditional (jurisdiction) | WC-NM-002 NM Fee amount | Jurisdiction configuration | NM Fee amount: Applies on the basis stated in column M for employers liable for the fee. The rule text and figure are in column M of row WC-NM-002; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-WC-001 State-Fund Workers' Compensation Premiums and Fees Collected through Payroll (WA, NM, OR, WY). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |
| Conditional (jurisdiction) | WC-NM-003 NM Fee amount | Jurisdiction configuration | NM Fee amount: Applies on the basis stated in column M for employers liable for the fee. The rule text and figure are in column M of row WC-NM-003; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-WC-001 State-Fund Workers' Compensation Premiums and Fees Collected through Payroll (WA, NM, OR, WY). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |
| Conditional (jurisdiction) | WC-OR-002 OR Rate per hour worked | Jurisdiction configuration | OR Rate per hour worked: Applies to the hours worked by the covered employees stated in column M. The rule text and figure are in column M of row WC-OR-002; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-WC-001 State-Fund Workers' Compensation Premiums and Fees Collected through Payroll (WA, NM, OR, WY). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |
| Conditional (jurisdiction) | WC-WA-002 WA Rate per hour worked | Jurisdiction configuration | WA Rate per hour worked: Applies to the hours worked by the covered employees stated in column M. The rule text and figure are in column M of row WC-WA-002; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-WC-001 State-Fund Workers' Compensation Premiums and Fees Collected through Payroll (WA, NM, OR, WY). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |
| Conditional (jurisdiction) | WC-WA-003 WA Return parameters and file layout | Jurisdiction configuration | WA Return parameters and file layout: Applies once the open point is closed; until then the return is prepared from the common field model only and checked against the authority portal before submission. The rule text and figure are in column M of row WC-WA-003; the payroll evaluates the condition each quarterly period for every employer registered in the jurisdiction before generating the US-WC-001 State-Fund Workers' Compensation Premiums and Fees Collected through Payroll (WA, NM, OR, WY). | Scenarios: an employer crossing the threshold mid-year switches route from the next period the authority names; a multistate employer applies the rule only to the wages of this jurisdiction; nonresident aliens, household and agricultural employees follow the federal population rules unless the jurisdiction rule says otherwise. |

## Example Analysis

| US-WC-001 State-Fund Workers' Compensation Premiums and Fees Collected through Payroll (WA, NM, OR, WY) — EXAMPLE FILE ANALYSIS |  |  |  |
|---|---|---|---|
| Raw Value | Field Name | Interpretation | Notes |
| ═══ WORKED EXAMPLE: STATE-FUND AMOUNTS FOR ONE EMPLOYEE AND QUARTER (constructed) ═══ |  |  |  |
| 4.80 | New Mexico fee | 2.25 + 2.55 | Per employee per quarter |
| 520 | Oregon hours worked | Constructed input | Input |
| 9.36 | Oregon WBF | 520 x 0.018 | Split half employee / half employer |

## Sample File

| US-WC-001 State-Fund Workers' Compensation Premiums and Fees Collected through Payroll (WA, NM, OR, WY) — SAMPLE FILE |
|---|
| No official sample filing is held for these returns and none is constructed. Verified channels: the per-jurisdiction channel classes and portals in the Report Matrix (column G and the accuracy note). |


## Fact index

Every value above with its key, effective period and register id.

| Key | Value | Effective | Register id |
|---|---|---|---|
| `nm.wc.admin_fee.employee.quarterly` | 2.25 | from 2025-07-01 to 2028-06-30 | US-NMR3-001 |
| `nm.wc.admin_fee.employer.quarterly` | 2.55 | from 2025-07-01 to 2028-06-30 | US-NMR3-001 |
| `or.wbf.rate.per_hour` | 0.018 | from 2026-01-01 to 2026-12-31 | US-ORS5-010 |
| `rspec.nm.wh_qtr_report.form` | TRD-41431 (new 2026-01-01): WC fee return + employee quarterly wage and withholding report, 25th after quarter | from 2026-01-01 | US-NMS5-012 |
| `rspec.or.oq.form` | Form OQ combined quarterly (withholding, UI, Paid Leave, WBF, TriMet, Lane Transit, STT) + Schedule B + Form 132 (wage and hour detail) via Frances Online | from 2026-01-01 to 2026-12-31 | US-ORS5-010 |
| `rspec.wy.wc_report.frequency` | workers compensation payroll report monthly (quarterly by permission), joint UI/WC reporting | from 2026-05-08 | US-WYS5-007 |
| `wa.wc.employee_deduction.rule` | employer (not self-insured) deducts from each worker one-half of the medical aid premium per hour per risk class | from 2026-01-01 to 2026-12-31 | US-WAS7-001 |
| `wa.wc.supplemental_pension.rate` | 0.1912 | from 2026-01-01 to 2026-12-31 | US-WAS5-019 |

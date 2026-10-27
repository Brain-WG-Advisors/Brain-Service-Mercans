# Colombia QA CROSS-CHECK — v2.4 STANDARDS

Audit all artifacts for consistency, completeness, and v2.4 compliance.

## READ ALL ARTIFACTS
CCG:          ~/mercans-pipeline/CO-compliance/01-ccg/CO-CCG-001-v1.0.docx
Report Specs: ~/mercans-pipeline/CO-compliance/04-reports-spec/
DD:           ~/mercans-pipeline/CO-compliance/05-data-dictionary/CO-DD-001-v1.0.xlsx
WTC:          ~/mercans-pipeline/CO-compliance/02-wtc/CO-WTC-001-v1.0.xlsx
SIR index:    ~/mercans-pipeline/CO-compliance/03-statutory-integrations/CO-SIR-INDEX-001-v1.0.docx (runbooks: <AUTH>/ via si-runbook)
Payslip:      ~/mercans-pipeline/CO-compliance/06-payslip/CO_Compliance_Payslip_Generator.xlsx
scope_manifest: ~/mercans-pipeline/CO-compliance/scope_manifest.json
Global WTC:   ~/mercans-pipeline/shared/Global_WTC_V1_0.xlsx

## CHECKS

### 1. CCG ↔ WTC alignment
Every wage type in CCG Modules 3-9 must exist in WTC with matching tax/SS treatment.
Score: X of Y matched.

### 2. CCG ↔ DD alignment
Every field in CCG Module 2 must exist in DD.

### 3. CCG ↔ Report Specs alignment
Every report in CCG Module 10 must have a matching Report Spec xlsx.

### 4. DD ↔ Report Specs alignment (4-BUCKET METHOD)
Classify each spec field as: DD / TX / CALC / SYS
Only DD-bucket fields must be in DD. TX/CALC/SYS correctly excluded.
Score: X of Y DD-bucket fields found in DD = Z% alignment.
NOTE: Do NOT penalize for TX/CALC/SYS fields not being in DD.

### 5. Global WTC coverage audit
Check "Global WTC Coverage" sheet in WTC file against Global_WTC_V1_0.xlsx.
Report: X included, Y excluded with reasons, Z% coverage.

### 6. Scope discipline
- No calculated amounts or Base Salary in DD
- No identification data in WTC
- No full field specs in CCG Module 2 or 10

### 7. Report Spec format compliance (per report)
- Exactly 9 sheets with correct names
- Sheet 4 has 21 columns A-U with correct headers
- Header row is blue FF4472C4, white, bold
- Row colors applied (amber/blue/green/red/grey)
- Payroll Scope Summary has green/red coloring
- Population Rules sheet completed

### 8. v2.4 standards
- CCG uses 13 official modules with exact titles AND template Q&A format (H3 headings)
- DD uses CZ V2.0 format, blue columns only
- WTC uses CZ V2.0 + Global WTC baseline + Form Reference Guide sheet
- Report Specs use Spain 9-sheet format with 21-column Sheet 4
- Payslip uses the 8-sheet Mercans standard, navy/grey palette, green net-pay

### 9. v2.4 NEW — Composite key / Inter-field constraints
- Composite-key fields documented in Sheet 4 column M (C13)
- Conditional fields have bidirectional documentation (C16)
- Form Reference Guide present in WTC (C17)
- Scope decision audit trail complete (C20)

## OUTPUT
Save to: ~/mercans-pipeline/CO-compliance/07-qa-crosscheck/CO-QA-REPORT.md

Include:
- Executive summary (overall score /100)
- Per-check alignment scores
- Issues list with severity: CRITICAL / MAJOR / MINOR + fix recommendation
- Global WTC coverage summary
- v2.4 compliance summary
- Readiness verdict: READY FOR DEV TEAM / NEEDS PATCHES / MAJOR REWORK

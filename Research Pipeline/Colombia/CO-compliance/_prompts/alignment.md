# Colombia ALIGNMENT PATCH — DD vs REPORT SPECS

Fix all mismatches between the Data Dictionary and Report Specs before the audit.
This is a mandatory step. Do NOT skip any check.

## STEP 0 — VERIFY CURRENT STATE FIRST (a prior run of this exact stage may
## have been interrupted partway through)

Before applying any fix, check the CURRENT content of the DD and each spec —
do not assume a pristine, unfixed starting point. For each of the 6 checks
below: if the DD/spec pair already reflects the correct, aligned state,
leave it alone and move to the next check. Only apply a fix where the
current file content genuinely still shows the mismatch. This avoids both
redundant rework and accidentally re-breaking something an interrupted prior
pass already corrected. Verifying a check takes far fewer turns than
re-applying it — spend the budget on what's actually still wrong.

## READ ALL FILES
1. DD: ~/mercans-pipeline/CO-compliance/05-data-dictionary/CO-DD-001-v1.0.xlsx
2. ALL report specs: ~/mercans-pipeline/CO-compliance/04-reports-spec/
3. CCG: ~/mercans-pipeline/CO-compliance/01-ccg/CO-CCG-001-v1.0.docx
4. scope_manifest.json

## CHECK 1: OPTION MAPPER CODE ALIGNMENT (F1 prevention)
For every Option Mapper referenced in any spec Sheet 6 (Field Options):
- Find the same mapper in DD Country Option Mappers sheet
- Compare every code, value, and local name
- If they differ: update BOTH files to match the authoritative source
  (authoritative = official government form/XSD > CCG > web research)
- Document every fix: field name | old value | new value | source

## CHECK 2: FIELD CLASSIFICATION ACCURACY (F3 prevention)
For every field in every spec Sheet 4 (Field Specification), column E (Payroll Field Y/N):
- If field exists in DD Country Fields sheet → it is an EMPLOYEE field
- If field exists in DD ID Information (employer rows) → it is an EMPLOYER field
- If field is calculated (amount, total, tax) → it is NOT a payroll master data field
- Fix any misclassification found

## CHECK 3: MANDATORY/CONDITIONAL FLAGS (F13 prevention)
For every field marked Mandatory=C (conditional) in specs:
- Verify the Conditional Reason column (col G) is filled with a clear condition
- If empty → research the condition from official docs and fill it
- Common pattern: "Required when [field X] = [value Y]"
- v2.4 C16: ensure bidirectional reference — if A's condition mentions B, then
  B's notes must mention A

## CHECK 4: OPTION VALUES COMPLETENESS (F14 prevention)
For every field with Option Values (col O not empty) in spec Sheet 4:
- Verify Sheet 6 (Field Options) has a complete code table for it
- Verify DD Country Option Mappers has the same table with local language values
- If incomplete: research official codes and complete both

## CHECK 5: COMPOSITE KEY DOCUMENTATION (F12 prevention)
For every field where Length > 8 chars and Example shows concatenated patterns
(date + code + sequence), verify column M (Explanation) documents the
"Composite Key Structure" — each sub-field's position, length, source, persistence.

## CHECK 6: CODE PREFIX VERIFICATION (F14 prevention)
For every coded identifier field (eazon, CRA, DT, DJ, AEAT key, etc.):
- Extract prefix pattern from the source PDF
- Verify every code in the spec matches the pattern
- Document the prefix pattern in column J (Format)

## FIXES
- Overwrite DD: ~/mercans-pipeline/CO-compliance/05-data-dictionary/CO-DD-001-v1.0.xlsx
- Overwrite affected specs: ~/mercans-pipeline/CO-compliance/04-reports-spec/
- Bump version in Version Control sheet of each patched file
- Save patch log: ~/mercans-pipeline/CO-compliance/07-qa-crosscheck/CO-ALIGNMENT-PATCH.md
  Format: Check | Field/Mapper | Issue Found | Fix Applied | File Patched

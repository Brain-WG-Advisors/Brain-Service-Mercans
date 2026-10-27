# Pre-Submission QA Report — France (FR) — v3

**Date:** 2026-09-03
**Prepared by:** Wallisson Gomes
**Supersedes:** FR-QA-REPORT-v2-20260902.md (generated before WTC/CCG/SIR/Report Specs/Alignment Patch/DD reached their current closed state — that report is now stale, not wrong)

---

## Executive Summary

**Overall verdict: READY FOR DEV TEAM.**

Every artifact family in this build has now been through a field-level or code-level audit against primary sources (DSN Cahier Technique CT2026.1.2, Legifrance, URSSAF, BOFiP), not a structural/mechanical check alone. Mechanical audit (Stage 9, this date): **12/12 PASS**.

| Artifact | Depth of audit | Errors found | Errors fixed |
|---|---|---|---|
| CCG | 13/13 modules, worked-example arithmetic re-derived | 6 (arithmetic in worked examples) | 6/6 |
| WTC | 378/378 wage types, code-by-code | 0 confirmed content errors | — |
| SIR (3 systems) | 28/28 files, phase-by-phase | 4 (format/direction/SIRET-control-code) | 4/4 |
| Report Specs | 15/15 files, 1,437 field rows | 19 (1 critical tax-rate error, 18 text-contamination) | 19/19 |
| Data Dictionary | 54/54 option mappers code-by-code; 198/198 fields structurally | 1 (Contract Nature, 17 of 26 codes missing) | 1/1 |
| Payslip | Unit Rate Details, Payslip Spec formula, EN/FR visual example with full tax cascade | 2 (merge-corruption risk caught before write; BIK formula range bug) | 2/2 |
| Alignment Patch | 6/6 responsibilities | 1 (AGIRC-001 Field Options data contamination) | 1/1 |

**Zero open defects.** Every finding above was corrected and independently re-verified by re-reading the saved file from disk, not by trusting the script that wrote it.

---

## Artifact-by-artifact detail

### CCG — `01-ccg/FR-CCG-001-v1.0.docx`
13/13 modules read in full. Markdown-heading-leak bug in Module 3 found and fixed (structural, not factual). Six arithmetic errors in worked examples (Modules 3, 9, 12) found and corrected. Module 12.1 Example 1 kept synchronised with the Payslip's illustrative example after the Payslip gained a new wage type (FR-075) — six independent recalculated figures matched to the cent. Loi n° 2026-534 (social/fiscal anti-fraud law, in force 27 June 2026) incorporated into Module 10 with its one payroll-relevant mechanism (CPAM fraud notification interacting with subrogation).

### WTC — `02-wtc/FR-WTC-001-v1.0.xlsx`
378/378 wage types read individually or via one of 13 identified boilerplate blocks, each confirmed by full-text comparison before being treated as a repeat. Multiple figures cross-validated against three independent sources within the same day's work (payslip cascade, CCG worked examples, external search) with no contradiction found.

### SIR — `03-statutory-integrations/`
Three systems, 28 files: DGFIP-EDI (10/10, 3 corrections to integration-landscape.json), NETENT-DSN (9/9, 0 errors), URSSAF-DPAE (9/9, 1 correction — `N_SIRET` control code 02→01, confirmed against the P5 error catalogue and test case T-09).

### Report Specs — `04-reports-spec/` (15 files)
1,437 field rows read individually. One critical finding: FR-DGFIP-003 carried the payroll-tax rates as 4.25%/9.35% instead of the correct 8.50%/13.60% (Art. 231 CGI, confirmed against Legifrance and 6 independent sources) — corrected across 12 cells in 6 tabs. A recurring text-contamination pattern (a neighbouring field's description overwriting the wrong cell) was found and corrected in 18 places across 8 files, including in the shared envelope block (Title code / Telephone number) common to most DSN-derived specs, and in the DGFIP-EDI/NETENT-DSN Field Options tables.

### Data Dictionary — `05-data-dictionary/FR-DD-001-v1.1.xlsx` (now v1.3 in Version Control)
Full audit of the Country Option Mappers sheet (413 rows, 54 distinct mappers): one real defect found (Contract Nature carried only 9 of the norm's 26 codes; 12 were correctly excludable under the established private-sector filter, 3 — penitentiary employment 53/54 and the ESAT work-support contract 70 — were genuine gaps confirmed via primary/authoritative sources and added; one, CAPE code 32, was confirmed correctly excluded on Commercial Code art. L127-1; one, the educational engagement contract 60, remains a documented scope-owner decision). All other 53 mappers reconciled exactly (kept codes + named exclusions = official total), including four mappers where an unexplained numbering gap was independently confirmed to be non-consecutive numbering in the norm itself, not a missing code. ID Information (25 fields) and Country Fields (173 fields) audited structurally: all 54 mappers correctly cross-referenced, no field found that should sit in the WTC instead.

### Payslip — `06-payslip/FR_Compliance_Payslip_Generator.xlsx`
Unit Rate Details extended with the four new BIK wage types; a row-insertion merge bug that risked losing the Base Salary rate/quantity values was caught, reverted from backup, and fixed with a safe insert-then-shift-merges method. The Payslip Spec's "Benefits in Kind" HRP formula was a numeric range (`62400:62499`) incompatible with the string-coded new wage types; corrected to an explicit code list, which also fixed a pre-existing inclusion error (cash housing allowances wrongly counted as benefits in kind). The EN/FR visual example was extended with a real meal benefit, its full tax cascade recalculated and cross-checked against the CCG's own worked example to the cent.

**Open item, not a defect:** two legacy template sheets (`How to set up Payslip`, `Compliance Payslip`) remain in the workbook; the pipeline's own build instructions call for their removal and they were not removed. Does not affect the 5 required sheets' content or the visual/spec deliverable.

### Alignment Patch — 6/6 responsibilities
Option Mapper Cross-Validation, Field Classification (96/96), Option Values Completeness, Bidirectional Documentation (15/15 samples), Code Prefix Verification (193 combinations), SIR Inbound/Outbound — all closed. One data-contamination finding in FR-AGIRC-001's Field Options sheet, corrected.

---

## Mechanical audit (Stage 9, this date)

12/12 PASS. Full machine-readable result: `07-qa-crosscheck/audit_v3_mechanical.json`.

---

## Remaining open items (none blocking)

| Item | Nature |
|---|---|
| Payslip legacy sheets (`How to set up Payslip`, `Compliance Payslip`) | Cosmetic/cleanup, not a content defect |
| Part-Time Contribution on a Full-Time Basis (DD, `S21.G00.40.044`) | Reviewed by pattern only, not independently confirmed against Field Options |
| Contrat d'engagement educatif (DD Contract Nature, code 60) | Documented scope-owner decision, intentionally left open |

## Readiness verdict

**READY FOR DEV TEAM.** No known content defect remains open in any artifact. Share with Mohit's team when convenient.

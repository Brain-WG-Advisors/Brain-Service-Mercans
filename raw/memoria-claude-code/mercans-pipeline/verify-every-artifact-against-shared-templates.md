---
name: verify-every-artifact-against-shared-templates
description: Wallisson requires every pipeline-generated artifact to be reviewed against the shared/ templates before moving to the next stage
metadata: 
  node_type: memory
  type: feedback
  originSessionId: f5c714b2-3318-4b0c-a412-d5d0707161ba
  modified: 2026-08-11T22:18:37.070Z
---

Every file the compliance pipeline generates must be analysed and reviewed against the
canonical templates in `shared/` **before** the next stage starts — never batched into a
post-hoc audit at the end of a country build.

The reference machinery lives entirely in `shared/` and is country-independent:
- `PRESUBMISSION_AUDIT.md` — checks C1–C22 (mechanical PASS/FAIL/MANUAL + Claude content fixer)
- `country_failure_log.md` — failure patterns F1–F28
- `QA_METHODOLOGY_BAKE_IN.md` — per-stage Definition of Done with cross-checks baked in
- Templates: `CZ_Data_Dictionary_V2_0.xlsx`, `_CZ_Wage_Type_Catalogue_V2_0.xlsx`,
  `Global_WTC_V1_0.xlsx`, `CCG_TEMPLATE_QUESTIONS.md`, `report-spec-template/`,
  `REFERENCE_Payslip_Mozambique.xlsx`, `REFERENCE_Payslip_Tunisia.xlsx`

**Why:** the defects that survived longest on the Canada build were not statutory errors —
they were propagation (artifact A changed, artifact B that quoted A was never re-synced) and
buildability (field names that don't resolve, calculated values sitting in master-data files).
Those are only caught by comparing each artifact against its template at the moment it is
built.

**How to apply:** after generating any artifact, run its C-checks and the stage's Definition
of Done before declaring the stage complete. Never assume the state of an artifact — open and
read the real current file before editing or referencing it (this exact assumption caused the
F24–F28 misnumbering incident). See [[mercans-pipeline-windows-deployment]].

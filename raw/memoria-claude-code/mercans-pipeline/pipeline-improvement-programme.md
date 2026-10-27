---
name: pipeline-improvement-programme
description: "Status and standing decisions of the post-France pipeline improvement programme (PIPELINE_IMPROVEMENT_PROMPT.md, phases 0-6, checks C34-C47)"
metadata:
  node_type: memory
  type: project
  originSessionId: db8d7f08-ed82-4703-bd63-ad9a5c4a6a45
  modified: 2026-10-08T02:03:27.145Z
---

The programme in `mercans-pipeline/PIPELINE_IMPROVEMENT_PROMPT.md` is tracked in `mercans-pipeline/IMPROVEMENT_LOG.md`. Read the log first.

**Status on 2026-10-07**
- Phases 0-5 are done and verified.
- Phase 6 is prepared: a 13-stage dry run passes and the metrics harness is ready.
- The pilot build itself waits for Wallisson to choose a pilot country. `shared/pilot/PILOT_PLAN.md` holds the command and the criteria.
- After Phase 3, Wallisson said "faça tudo… está tudo aprovado": no more gates are needed for this programme.

**Standing decisions**
- **D1:** Stage 9b sits inside Stage 9, Design is Stage 12, Release is Stage 13.
- **D2:** C34 onwards block.
- **D3:** the contract is now at 1.3.0 (`oracle`, `coverage_matrix`, `numeric_verification`, `package`, `DESIGN`).
- **D5:** the FR suite lives in `FR-compliance/_validation`.
- **D6:** the FR finals are the pipeline files.
- **D7:** C37 uses the `law` basis; raw agreement is reported as the KPI.

**Why:** France needed 211 post-delivery changes to its CCG alone. The programme makes builds right the first time.

**How to apply**
- The FR builder imports `shared/spec-builder`, so any change to `mercans_spec` must still reproduce the FR finals with 0 differences (`compare_specs.py`).
- In this environment, never write a regex into a file through a bash heredoc. The backslashes get mangled: `\b` became a backspace character three times. Use the Write or Edit tool, or `chr(92)`.

**Known defects in delivered artifacts, reported but not fixed (rule 2):**
- BE-FEBELFIN-001: `RF98…` fails ISO 11649.
- FR-CCG v1.1: three typed numbers in Example 1 (C38), and an `FR-NSSO` leftover.
- FR-DSN-001/002/003: `BE-NSSO` in the Report Matrix.
- FR payslip: a note citing the Tunisia reference.
- FR: version mismatches.
- FR `scope_manifest`: format mismatches.

Related: [[verify-every-artifact-against-shared-templates]], [[mercans-pipeline-windows-deployment]].

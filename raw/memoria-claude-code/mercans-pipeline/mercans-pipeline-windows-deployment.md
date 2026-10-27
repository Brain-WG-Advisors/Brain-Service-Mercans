---
name: mercans-pipeline-windows-deployment
description: "State of the mercans-pipeline deployment on the Windows machine as of 11 Aug 2026, and what is still missing"
metadata: 
  node_type: memory
  type: project
  originSessionId: f5c714b2-3318-4b0c-a412-d5d0707161ba
  modified: 2026-08-11T22:18:44.730Z
---

The pipeline is being migrated from the Mac (`wallissongomes@BRA-A3240-407`, paths
`~/mercans-pipeline/...`) to this Windows box at `C:\Users\instituto\mercans-pipeline`.
Next country build is **Belgium**; the Canada build stays on the Mac.

As of 11 Aug 2026 the repo here contains only `.git/` and `shared/` (21 files, complete).

Still missing on this machine:
- `mercans_pipeline_v2_6.sh` — the pipeline driver. Attached to the MERCANS project on
  claude.ai and reportedly on Google Drive; the Drive connector token is expired and needs
  the user to reconnect at claude.ai → Personalizar → Conectores.
- `presubmission_audit_local.py` — the mechanical implementation of checks C1–C22 referenced
  by `shared/PRESUBMISSION_AUDIT.md`. Not present anywhere in the repo.
- `jq` is not installed (Git Bash 5.3, Claude Code 2.1.228 and python3 are present).

Trap to know: the local commit `aad1387` "Snapshot: full Canada build + shared QA
methodology (pre-Belgium)" contains **only `.gitignore`** — it is not a backup of anything,
and there is no git remote. Do not treat it as a restore point.

See [[verify-every-artifact-against-shared-templates]] for the review discipline that applies
to every artifact this pipeline generates.

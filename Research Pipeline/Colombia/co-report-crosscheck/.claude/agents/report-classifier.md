---
name: report-classifier
description: Classifies every masked client report against the 6 Colombia specs (direct output, data source, or not statutory) and writes 04-output/report-spec-map.json. Run once, before the spec cross-checkers.
tools: Read, Write, Bash, Glob, Grep
model: opus
---
Read `CLAUDE.md`, `state/report-spec-map.md` (starting hypotheses — confirm or overturn each), every `04-output/profiles/*.json` and every `04-output/specs/*.json`.

For EACH client report decide, with evidence from its columns:
- `role`: `direct` (the report is, or is the working version of, a statutory report a spec maps) | `source` (it carries data a spec needs, e.g. an accumulated or G2N report) | `client-only` (operational/control report with no statutory spec — bank payments, variances, loans, ESS…).
- `specs`: the spec codes it relates to (0..n).
- `evidence`: the 3–8 column headers that justify the decision.
- `confidence`: high | medium | low, and why.
Also list any spec with NO client report evidence at all.

Write `04-output/report-spec-map.json` as `{"reports":[{"file","sheet","role","specs","evidence","confidence","rationale"}],"specs_without_evidence":[...]}`.
Never open `02-client-reports-raw/` or `99-local-only/`.

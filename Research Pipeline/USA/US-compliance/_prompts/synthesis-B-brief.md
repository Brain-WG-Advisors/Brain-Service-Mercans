# Synthesis B brief — research packs and facts files (US build)

Written by the orchestrator, 2026-11-02. Every Synthesis-B worker reads this first.

BASE = C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance (never write under ~/mercans-pipeline).

## Rules
- **No fetching.** Draw only on rows already in `00-official-sources/legal-basis-register.csv` (status active; partial only with the partial flag carried). Never cite superseded/MANUAL/gated/historical rows for a number.
- Load the skill `mercans-pipeline-contracts` first and write facts files in exactly the contract shape it gives (schema `facts`). Validate every file you write with `python ~/mercans-pipeline/shared/schemas/validate_contract.py facts <file>` (read-only use of that script). A file that does not PASS is not done.
- Every fact carries `register_id`. A fact with no active row is not written as a value: it goes into the facts file's unresolved/gap list (contract field) with what would close it (copy from `_research/stage5/{JUR}.md` open questions or `_research/stage5/ACCESS-GAPS.md`).
- Values with vigência: effective_from/to as the row says. 2027 values only where the row is an enacted/published 2027 value; projections are never facts.
- Inputs to read: `_pipeline/build-manifest.json` (artifacts, units, tier, languages, oracle), `00-official-sources/MANDATE.md` (sealed answers, US-OWN-001..007), `_research/stage5/{JUR}.md` (53 findings files), `_research/stage5/SYNTHESIS-A.md`, `_pipeline/RUN-JOURNAL.md` (known traps: SC Act 110 not in 2026 withholding; WI/NE/KS tables ≠ statutory brackets; MI tips/overtime deduction at assessment only; VA 2027 deduction not modelled; DC 2026 method unpublished; CT tables × rules; MA PFML split date conflict — decide on the Ch. 101 s.45 text vs DFML and record the decision with both row ids; etc.).
- Oracle: collect every worked example the workers reproduced (CA DE 44 E/F, GA 27.03, MN 91.27, MI 75.36/47.45, OH 45.13, NY NYS-50-T examples, IL 32.13, WI 7.59/14.34/22.08, VT 45.77, CT 17.65/39.97/78.82, MO, ME, NC, LA 13.98/111.54, AL 29.59, IN 13.96+4.73, OK 37.00, RI 87.57, HI 9.58, AR 36.50, ND (use table, not the booklet example), UT 6 examples, IA 6 examples, MS formula rows, DE examples, KY …) into the facts of the artifact that owns calculation examples, each with its register_id and the noted residuals.
- Write incrementally; a crash must not lose work. Use your own scratch subfolder.
- Do NOT edit MANDATE.md, build-manifest.json, SKELETON-MANIFEST.md, or anything under 01-…09-. Append to `consumed_by` in the register is done by the final merge worker only (list the ids you consumed in your report file instead).

## Outputs per worker
- `_research/{ARTIFACT}-research-pack.md` (or the unit-level file the contract allows) — sections per the artifact's needs, citing register ids; carry special populations (US-OWN-005) and the language seams (US-OWN-006).
- `_research/{ARTIFACT}-facts.json` (or unit-level facts files the contract allows; if the contract only allows one file per artifact and the artifact is split across workers, write fragments to `_research/facts-fragments/{ARTIFACT}-{unit}.json` and say so).
- `_research/synthesis-B/{ARTIFACT}-{unit}-report.md`: facts written, unresolved count, ids consumed, validator output.

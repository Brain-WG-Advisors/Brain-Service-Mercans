# Agent 2 (source hunter): QA r3d fix 2

Date: 2026-11-02. No fetching. Backups: `_research/qa-r3d-fix/_backup2/` (register + 5 facts files, taken before the write). `01-ccg/` not touched.

1. Register: `US-OHR3C-001` (ORC 4141.23, version eff. 2025-09-30) status `superseded` -> `active`, `effective_to` 2026-06-15 kept (closed-period rule: correct basis for 2026-01-01..2026-06-15). `US-OHR3D-001`: `supersedes` cleared; successor link kept as information in `figure_or_rule_carried` of both rows. No other register line changed.
2. `CCG-annex_MD-facts.json` `md.local.county_rates` note: 2025 rates (Allegany 3.03, Kent 3.20) removed; note now says the rates changed for 2026 and cites the 2026 values in the same table and in `md.live.county_rates_2026` [US-MDS5-004].
3. Internal `MULTI.md 2.x` references removed from fact notes/values: 15 notes in `CCG-annex_MULTI` (incl. `mt.reciprocity.states`), the `multi.resident_out_of_state.ms.withholding_rule` value, 1 note in `WTC-global_baseline`, `tx.no_wage_tax` (m01), `multi.sit.work_location.rule` (m02). Remaining `.md` hits in facts files are state-code keys (`*.md.*`), `_produced_by`/`_synthesis_d` metadata and `unresolved[].attempted` provenance, not fact notes/values; left as is.

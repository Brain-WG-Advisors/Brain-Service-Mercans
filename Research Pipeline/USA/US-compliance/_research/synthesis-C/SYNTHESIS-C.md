# Synthesis C: final merge (US build, 2026-11-02)

Worker: compliance-source-hunter. No fetching. Every rewritten file was first copied to `_research/synthesis-C/_backup/` (mirror of the BASE-relative path; the copy is the pre-Synthesis-C state). Scripts and logs: `_research/synthesis-C/_work/` (step1_rename.py, step2_promote.py, step2b_packs.py, step5_fix.py, step5_consistency.py, step7_consumed.py, plus their logs).

## 1. Id normalization
- **590 register ids renamed**, which is every id that failed `^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$`. By status at rename: 403 active, 108 superseded, 61 MANUAL, 10 gated, 4 partial, 3 historical, 1 provisional. Rule: `US-` + middle segments joined without hyphens + `-NNN`, e.g. US-AZ-P5-1-003 -> US-AZP51-003 and US-UT-PIT-003 -> US-UTPIT-003. No middle segment was longer than 12 characters and no new id collided, so no shortened form was needed. After the rename, 0 of 2,533 register ids fail the pattern.
- The map is in `_research/stage5/ID-RENAME-MAP.csv` (`old_id,new_id,status_at_rename`).
- **Register:** the map was applied to `id` (590) and `supersedes` (159). **Deviation (reversible):** the same token-safe substitution was also applied to the free-text columns that cite ids: figure_or_rule_carried 235, verification_method 16, instrument_name 3, article_or_section 2. Without it, those cross-references would have pointed at ids that no longer exist.
- **_research:** 356 files rewritten, 5,890 occurrences in total (120 top-level facts/packs, 136 under synthesis-B including the scratch generators, 55 stage5, 45 mandate-answers). `_register-shards/` and every `_backup/` were left unchanged. The substitution regex was `(?<![A-Za-z0-9-])OLD(?![A-Za-z0-9])`.
- **Scaffolder-owned files. These were NOT edited; the scaffolder must apply the same map with the same regex:**

| File | Occurrences to replace | Distinct old ids |
|---|---|---|
| `00-official-sources/MANDATE.md` | 1,113 | 464 |
| `_pipeline/build-manifest.json` | 1,147 | 473 |
| `SKELETON-MANIFEST.md` | 12 | 11 |

  The exact list per file and id is in `_research/synthesis-C/SCAFFOLDER-ID-REPLACEMENTS.csv` (`file,old_id,new_id,occurrences`). The one remaining old-style string in `_research` is the illustrative `US-XX-P5-1-003`, which is not a register id.

## 2. Held facts promoted (513 in non-core files, + 3 in CCG core)
Each promoted fact got tier, authority and url from its row. The row was checked to be active or partial with tier A.x (0 problems).

Promoted by kind:
- 271 from `_facts_pending_register_id_pattern` (MN–WY annexes, MULTI, DD, RSPEC);
- 99 from `_facts_blocked_by_register_id_pattern` (PSL 29, SIR 70);
- 48 from "legacy id, NOT a fact" items, rebuilt from the AK–MI `spec_*.py` LEGACY tuples (units set explicitly);
- 77 WTC `Value is sourced…` carries;
- 18 closed-period facts (§3).

Number re-check (log: `_work/step2-promotion-log.csv`):
- 165 numbers were found in the row text and 36 in the row's local file (pdftotext or html);
- 7 zero employee rates rest on an explicit "not deducted / cannot withhold" statement in the row;
- 1 number was derived;
- 301 facts are non-numeric;
- 3 were NOT FOUND literally (`sc.labour.pay_change_notice.days`=7, `sc.records.wage.retention_years`=3, `psl.sc.retention.wage_records.years`=3, all on US-SCP52-006, whose excerpt says "three years" but has no 7-day clause). These were downgraded to confidence medium with a note.

Fixes made during promotion:
- `mo.pit.local.kansas_city.earnings_tax.rate` was rebound from US-MOP52-006 (the St. Louis row, which does not carry KC) to US-MOP9W-001 (KC 1%).
- WTC `co.sui.new_employer.total.rate` 3.05 was rebound from US-COP51-003 to US-COP51-004 (1.53+0.17+1.35).
- WTC `mi.oracle.biweekly_2000_1ex.result` 75.36 now has `derived arithmetically`, with the derivation line.

Meta unresolved entries removed:
- 28 `*.meta.register_id_pattern` entries;
- all 48 legacy entries and 77 WTC carry entries, plus WTC `mt.sui.rate_schedule`;
- the 4 closed-period unresolved entries.

In the packs, the matching Open-questions lines were dropped (81 lines in 57 packs). Each pack got a Synthesis C banner, and the "legacy id, NOT a fact", "(PENDING id pattern)" and "PENDING register_id pattern" marks were rewritten.

Promoted / unresolved-removed per file:
AK 1/1 · AR 8/8 · AZ 2/2 · CO 7/7 · DC 3/3 · DE 1/1 · FL 2/2 · GA 2/2 · HI 2/2 · ID 5/3 · IL 2/2 · IN 4/1 · KS 1/1 · KY 1/1 · LA 3/3 · MA 3/3 · MD 2/2 · ME 5/5 · MI 1/1 · MN 14/1 · MO 11/1 · MS 2/1 · MT 18/1 · MULTI 37/0 · NC 3/1 · ND 4/1 · NE 12/1 · NH 1/1 · NJ 13/1 · NM 15/1 · NV 6/1 · NY 1/1 · OH 10/2 · OK 1/1 · OR 1/1 · PA 3/1 · RI 4/1 · SC 8/1 · SD 4/1 · TN 3/1 · TX 4/1 · UT 22/1 · VA 1/1 · VT 5/1 · WA 1/1 · WI 13/1 · WV 6/1 · WY 9/1 · DD 15/0 · PSL 29/0 · RSPEC 32/0 · SIR 70/0 · WTC country_specific 67/66 · WTC global_baseline 13/13.

CCG core: the source `scratch-ccg-core/facts_core.py` was edited.
- Promoted: `ak.no_wage_tax` (US-AKWT-002), `nm.oracle.weekly_1000_married.withholding` 41.80 (US-NMP52-001) and `mi.oracle.biweekly_2000_1ex.withholding` 75.36 (US-MIPIT-001).
- CA SDI 1.3% (US-CAEDD-004) is keyed to the annex-owned `ca.sdi.employee.rate`, so it de-duplicates (keymap.py: `sdi.ca.rate` -> `ca.sdi.employee.rate`). The old `ca.sdi.rate` was never emitted as a fact.
- Removed: `practice.contract.register_id_pattern`.
- The NY, KY and UT oracle residuals keep only their real obstacle: a rounding conflict for NY and KY, and an open Pub 14 effective date for UT.

## 3. Closed-period rows (status back to `active`, period kept)

| Row | Period | Facts emitted |
|---|---|---|
| US-IDS5-012 (EPB00744 ed. 04-28-2025) | 2025-04-28 .. 2026-07-22 (unchanged) | annex ID: zero bracket single 15,000 / married 30,000 / biweekly 577. WTC: `id.sit.zero_bracket.single/married` |
| US-IN-001 (DN#1 R46/01-26) | 2026-01-01 .. 2026-09-30 | annex IN `in.local.lit.rate.boone` 0.017, marion 0.0202, min 0.005, max 0.03. WTC: boone 0.017; WTC marion/min/max split R46 (Jan–Sep) / R47 (from Oct). Values inspected directly in the local R46 PDF |
| US-INP51-001 (R46 re-read) | 2026-01-01 .. 2026-09-30 | none (prose row) |
| US-OHP52-001 (Optional Computer Formula eff. 2025-10-01) | effective_to corrected 2026-08-01 -> **2026-07-31** | annex OH `oh.pit.wh.method.period_a`, rate.1 1.775, rate.2 2.99, rate.3 3.64, break.1 26,050, break.2 100,000, base_tax.2 462.39, base_tax.3 2,673.50 |

GA 5.19%: there is no superseded GA row. The 5.19% rests on active US-GA-001, so no row change was needed (see §4). Other superseded rows ending in 2026 were checked. They are re-reads replaced by a better copy of the same value (e.g. US-WVPIT-004, US-WVP52-001, US-CTP51-002), not closed periods, so they stay superseded.

## 4. WTC `ga.sit.rate` and CCG core rebuild
- `ga.sit.rate` was already correct in WTC country_specific: 5.19 from 2026-01-01 to **2026-05-10** (US-GA-001) and 4.99 from **2026-05-11** (US-GAS5-009, withholding level; retroactive at assessment). Re-checked after every step; no change was needed.
- `scratch-ccg-core/build.py` was re-run, then `finish.py`. Problems: 0. 144 annex-owned keys were de-duplicated, against 135 in Synthesis B. All 14 module/coverage files PASS. `CCG-research-pack.md` and the 14 `synthesis-B/CCG-*-report.md` files were regenerated, with the "pattern-blocked" prose corrected in `pack-prose.md`.

## 5. Cross-file consistency
- 193 keys appear in more than one facts file. 141 of them diverged and were fixed, with 148 file-key rewrites. Log: `_work/step5-divergences.csv`.
- **There were no conflicting values for the same period.** All divergences were about dating:
  - `effective_to` null in WTC against 2026-12-31 in the annex;
  - a different `effective_from` basis, e.g. FL wage base since 2015 against 2026;
  - periods present in one file only (2025 or 2027 values);
  - wording of string values.
- The rule applied:
  - the owning file wins (CCG annex > CCG core > WTC global > WTC country > RSPEC > DD > SIR > PSL);
  - `effective_to` comes from the canonical fact, else from the register row, else from a bounded sibling;
  - adjacent same-value periods from different files are merged into the earlier date;
  - every file then carries the same period set.
- 6 overlapping 2026/2027 periods inside WTC were closed at 2026-12-31: co.famli.total.rate, ga.sui.new_employer.rate, mt.sit.rate.top, nj.tdi_fli.employee.wage_base, wa.pfml.employee_share.max, co.sui.new_employer.total.rate.
- Final re-check: 0 divergent keys.
- **Observation, not fixed (keys are never renamed silently):** CO FAMLI 0.88% is carried as `co.famli.rate.total.2026` in annex CO (a legacy key with the year in it) and as `co.famli.total.rate` in WTC. These are two keys with one meaning, and agent 3 / agent 4 should re-bind deliberately.

## 6. Validator
`python ~/mercans-pipeline/shared/schemas/validate_contract.py facts <file>` was run on all **73 facts files: 73 PASS, 0 FAIL**. Output is in `_work/step6-validator.txt`.

## 7. consumed_by
1,460 register rows are cited by facts, by coverage sources or by `_annex_keys_cited`. 1,450 rows were updated with 2,480 `{ARTIFACT}/{unit}` tokens. Tokens were appended; nothing was removed. None of the cited ids is missing from the register, and none of the cited rows is non-active or tier B.

## 8. Final counts and remaining unresolved

| Artifact | Files | Facts | Unresolved blocking | Unresolved non-blocking |
|---|---|---|---|---|
| CCG annexes (51 + FED + MULTI) | 53 | 3,158 | 48 | 453 |
| CCG core m01–m13 + coverage | 14 | 106 | 0 | 22 |
| WTC (global_baseline + country_specific) | 2 | 909 | 4 | 72 |
| RSPEC | 1 | 383 | 25 | 24 |
| DD | 1 | 103 | 0 | 3 |
| SIR | 1 | 293 | 1 | 14 |
| PSL | 1 | 165 | 0 | 12 |
| **Total** | **73** | **5,117** | **78** | **600** |

Blocking items:
- **WTC:** dc.sit.method.2026, oh.local.municipal.rate_table, ut.sit.schedule.effective_date, wa.base.125_401k.ui_pfml_cares.
- **SIR:** sir.fed.efw2.layout_ty2026. The EFW2 TY2026 row US-FEDS5-032 is now active, so SIR and RSPEC should re-read it locally.
- **RSPEC:** 25 file-layout reads (EFW2 TY2026, state W-2 / UI wage-file specs; list in RSPEC-facts.json).
- **CCG annexes:** 48 across 36 jurisdictions. These are mostly browser reads, next-year publications, local rate tables and the DC 2026 method.

Register after Synthesis C: 2,533 rows. 2,128 active, 201 superseded, 117 MANUAL, 54 partial, 25 gated, 6 historical, 1 provisional, 1 not_applicable.

## 9. What the scaffolder must do next
1. Apply `_research/stage5/ID-RENAME-MAP.csv` to `MANDATE.md` (1,113 occurrences / 464 ids), `build-manifest.json` (1,147 / 473) and `SKELETON-MANIFEST.md` (12 / 11). Use the regex in §1, and check the result against `SCAFFOLDER-ID-REPLACEMENTS.csv`. Afterwards, no string matching `US-[A-Z0-9]+-[A-Z0-9]+-[A-Z0-9]+-[0-9]{3}` should remain except the illustrative `US-XX-…`.
2. Reseal `build-manifest.json`. Note that 4 rows changed status (US-IDS5-012, US-IN-001, US-INP51-001, US-OHP52-001 are now active with closed `effective_to`).

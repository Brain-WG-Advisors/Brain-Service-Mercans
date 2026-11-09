
## Units annex_NY, annex_OH, annex_OK, annex_OR, annex_PA, annex_RI, annex_SC, annex_SD, annex_TN, annex_TX, annex_UT, annex_VA, annex_VT, annex_WA, annex_WI, annex_WV, annex_WY (builder NY–WY, round 1, 2026-11-02)

Artifact: CCG | Country: US | Round: 1 | Brief: `_prompts/ccg-build-brief.md`
Manifest: `_pipeline/build-manifest.json` (USD, minor units 2; tier overall T4; payslip English; mandate sealed 2026-11-02).
Inputs per unit: `_research/CCG-annex_{JUR}-research-pack.md` + `_research/CCG-annex_{JUR}-facts.json` (869 facts, 139 unresolved, 14 blocking).
Outputs: `01-ccg/annexes/annex_{JUR}.md` (17 files; same folder as the MD–NV builder; the AK–MA builders wrote to `01-ccg/modules/`, so the assembler must read both).
Generator: `01-ccg/_build-annex-NY-WY/` — `build.py` (renders every annex from `src/{JUR}.md` narrative + the facts file), `src/{JUR}.md` (hand-written rules; numbers only as `{{key}}` / `{{key@effective_from}}` placeholders resolved from the facts file; `@gaps` overrides), `lint.py` (C46 logic of `shared/consistency-checks` against all facts files + C29 marker scan), `rq-map.json` (unresolved key → RQ id), `dropped-notes.json`. Rebuild: `python build.py` then `python lint.py NY,OH,...,WY`.

### Precedent inspection (L1)
`shared/REFERENCE_CCG_Bulgaria.docx` opened with python-docx: 1,317 paragraphs, 3 tables, Heading 1 = 14, Heading 2 = 84, Heading 3 = 210, Heading 4 = 2. The 265-line question list governs m01–m13; annexes carry no template questions. Each annex: H1 = annex, H2 = 15 numbered sections (13 domains in the order of the research-request domain enum, 14 special populations, 15 sources); every domain = number-free or tagged rule bullets + a parameter table (key | value tag | unit | effective | register id | note) + RESEARCH-GAP markers.

### Fact bindings
- 869 of 869 facts carried as `[[FACT:key=value]]` in the parameter tables (one row per fact and period); every narrative number is a placeholder resolved from the facts file at build time (a missing key or an ambiguous multi-period key stops the build). 1,757 tags in total. Full section → key → value → register_id → period table: `_pipeline/CCG-bindings-annex_NY-WY.csv`.
- Exception: `va.wh.method` — its string value contains `[ ]`, which the tag syntax cannot carry (C46 regex stops at `]`). Its components are tagged in VA §2 (`va.pit.std_deduction.single`, `va.pit.exemption.personal`, `va.pit.exemption.aged_blind`, `va.pit.bracket.1..3.ceiling`, `va.pit.bracket.4.rate`); the table row points to the rule text. The lower VA bracket rates/base amounts exist only inside that string. Route to agent 2: split `va.wh.method` into keyed components or drop the brackets from the value.
- Fact notes are printed in the Note column; 75 notes were blanked because they held numbers that C46 would read as unbound values of other facts (`dropped-notes.json`); notes and gap texts are cleaned of pipeline wording (archive, summariser, MANUAL, tier-B, register-row status, HTTP codes) for C47.
- Self-check (`lint.py`, C46 logic, all facts files in `_research/`): 1,757 tags, 0 tags without a matching fact value, 0 unbound distinctive values, 0 C29 markers; C47 rework-word scan (release_crosscheck patterns, tags stripped): 0 hits.

### Decisions (traps from the brief and pack §0.1)
- SC: Act 110 rates (`sc.pit.statutory.rate.1/2`) written as assessment-level only; 2026 withholding stays on WH-1603F; revised tables = blocking gap.
- WI: W-166 withholding schedule vs statutory assessment rates (`wi.pit.statutory.rates`) separated; WTC uses W-166 only.
- OH: two 2026 withholding editions (pay dates to 2026-07-31 / from 2026-08-01) in one dated table; schedule ≠ flat statutory 2.75 %; municipal base (elective deferrals taxable) kept apart.
- NY: NYS-50 Method II schedules described as withholding schedules (no statutory brackets); local supplemental rates not written (blocking gap); example 2 residual stated as an open point.
- VA: 2027 standard deduction written as statute/assessment, **not modelled** for withholding (blocking gap `va.pit.formula.next_year`); PFML contributions only from 2028-04-01.
- UT: Pub 14 parameters written with an explicit "do not apply before the effective date" instruction (blocking gap).
- TX: Labor Code 62.003 earnings statement stated for non-FLSA employees (never "no pay-statement law").
- WA: SB 6346 (2028) assessment-level; PFML key used as it exists in the facts file (`wa.pfml.rate.total`).
- WV: only Charleston's service fee written; other cities and the SB 1053 fee base are blocking gaps.
- No worked example is computed in the annexes (oracle results quoted as facts; recomputation belongs to m12 / the validation suite).

### Deviations and findings to route
- C46 checker limitation: 37 multi-period keys (82 tags) carry a value valid in a period other than the last one listed in the facts files (e.g. `ny.pfl.employee.rate` 2026/2027, `oh.pit.wh.rate.*` two editions, `or.sui.wage_base` 2025 row listed after 2026, `wy.sui.wage_base` 2025/2026/2027). `consistency_checks.c46` keeps one value per key (last wins) and will report them as mismatches although each equals a fact. Same limitation the MD–NV builder logged; fix belongs to the checker (key + effective_from).
- Facts-file defect: `wa.pit.exists` = False carries effective_from 2028-01-01 while its note says it covers 2026 and 2027. Written as "no state income tax on wages in 2026 or 2027" bound to the key; agent 2 should correct the dates.
- Facts-file note: `wa.wc.supplemental_pension.rate` (0.1912, USD per hour, no unit_of_measure) matches the C46 percentage heuristic; written without a % sign, so no false binding.
- Form and section numbers that collide with other jurisdictions' fact values were reworded (e.g. VT annual reconciliation form, VT SSN Act cited by chapter, WY dishonoured-check section, PA LTEA section, OH/OR/TN "section 125" phrasing).

### Open items
139 RESEARCH-GAP markers, one per `unresolved[]` item, each in place in its domain section → `_research/CCG-research-request.json` RQ-263 … RQ-401 (appended after re-reading the shared file; schema research-request 1.4.0 PASS). The RQ id is not printed in the annex (digits would collide with C46); key ↔ RQ map in `rq-map.json`.

| Unit | Facts | Non-blocking gaps | Blocking gaps | Blocking keys |
|---|---|---|---|---|
| NY | 69 | 9 | 1 | `ny.pit.supplemental.local_rates` |
| OH | 72 | 10 | 0 | - |
| OK | 58 | 8 | 0 | - |
| OR | 68 | 7 | 1 | `or.pit.local.multnomah_pfa.step_year` |
| PA | 53 | 9 | 0 | - |
| RI | 56 | 6 | 1 | `ri.records.2026_version` |
| SC | 50 | 6 | 1 | `sc.pit.tables.post_act110` |
| SD | 34 | 6 | 0 | - |
| TN | 33 | 8 | 0 | - |
| TX | 33 | 6 | 1 | `tx.report.ui.enhanced_fields_layout` |
| UT | 45 | 7 | 1 | `ut.pit.schedule.effective_date` |
| VA | 49 | 5 | 2 | `va.pit.formula.next_year`, `va.ui.pool_cost_and_new_employer` |
| VT | 49 | 12 | 1 | `vt.minwage.hourly.next_year` |
| WA | 69 | 10 | 1 | `wa.labour.minwage.local.next_year` |
| WI | 56 | 6 | 0 | - |
| WV | 42 | 7 | 3 | `wv.pit.tables.start_date`, `wv.pit.local.service_fees`, `wv.ui.sb1053_fee` |
| WY | 33 | 3 | 1 | `wy.ui.rates.2026_values` |
| **Total** | **869** | **125** | **14** | |

Pack details stated with numbers but without a facts key (e.g. NY Method II band constants, OK married band widths, VT/RI/OR cumulative base amounts, special-population thresholds) were described without the number, not raised as new requests; the build relies on the keyed values.

### Accuracy
Research-only evidence (statutes and authority pages via the register; no portal or real filing): NY ~88 %, OH ~88 %, OK ~90 %, OR ~85 %, PA ~88 %, RI ~85 %, SC ~85 %, SD ~90 %, TN ~85 %, TX ~85 %, UT ~82 %, VA ~82 %, VT ~82 %, WA ~85 %, WI ~90 %, WV ~78 %, WY ~85 %. The 14 blocking gaps are not closable by more building; they need the A.1/A.2 sources named in each request.

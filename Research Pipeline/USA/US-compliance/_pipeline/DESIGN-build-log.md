# DESIGN — build log
Artifact: DESIGN (regulation design, stage 12) | Country: US | Round: 1 | Built: 2026-11-04
Manifest: _pipeline/build-manifest.json (USD, minor units 2, year 2026, package 1.0; DESIGN parked in `_design_artifact`, status `researched`, because the shared schema caps artifacts[].stage at 11; not edited)
Output: 09-design/US_Regulation_Design_v1.0.md (status For QA; package version 1.0; one Version Control row)
Generator: 09-design/_build/build_design.py (+ design_common.py, write_gaps.py); checks in 09-design/_build/checks/
Facts: all _research/*-facts.json (5,304 keys; no fact added or edited). No research pack for this stage: the design is generated from the approved facts, WTC, DD and the CCG coverage matrix.

## Precedent inspection (L1)
REFERENCE_FR_Regulation_Design_v1_0.md read as text (Markdown, not a binary): 8 parts (0 sweep, 1 flags, 2 accounts, 3 sequence, 4 detail, 5 taxability matrices, 6 open items, 7 self-review); flag rows `| account | name | definition | values |`; sequence rows `| order | regulation | ...`; account rows `| account | type | regulation | ...`. README (shared/design-template) rules 1-4 applied. Structure only: no precedent identifier, series, authority or country name is carried.
Approved WTC (533 rows, 20 columns A-T, code in column A) and DD (ID Information + Country Fields, field name in column C; the internal-code column is empty, so the design names DD fields by field name, written DD:`name`) opened with openpyxl. Every code and field named is read from those files by the generator, which fails the build if one is absent.

## Fact bindings
Full list: `_pipeline/DESIGN-bindings.csv` (location -> key -> register_id; 407 rows, 398 distinct keys, 165 register ids). Highlights:
| Location | Claim | key | register_id |
|---|---|---|---|
| 9840031 | OASDI base 2026 and 2027, rates | `fed.fica.oasdi.wage_base` (two dated entries), `fed.fica.oasdi.rate.employee` | US-FEDS5-005 |
| 9840021 | Worksheet 1A line 1g; standard and Step-2 schedules (8 rows x 3 statuses) | `fed.fit.worksheet1a.line1g.*`, `fed.fit.standard.*`, `fed.fit.step2.*` | US-FEDS5-001 |
| 9840022/23 | flat rate, mandatory rate and threshold | `fed.fit.supplemental.*` | US-FEDS5-003 |
| 9840041 | FUTA net rate, base, deposit threshold, potential credit reduction | `fed.futa.*` | US-FED-007, US-FEDS5-031 |
| Part 4.4 (51 rows) | flat rates; SUI wage base, new-employer and employee rates per period | `<st>.pit.rate(.flat)`, `<st>.sui.*` | per row in the CSV |
| 9840053 | programme parameters, every dated entry reaching 2026-2027 (CA SDI 1.3 then 1.4 from 2027-01-01; MA PFML split swap from 2027-01-01) | `<st>.(sdi, pfml, tdi, fli, pfl, famli, cares, phc, dbl, wbf, ccc, mbt, mctmt, transit, wc).*` | per row in the CSV |
| Part 0 | 18 answered coverage rows; populations of the owner decision | coverage matrix, `special_population.*`, population keys under `fed.*` | US-OWN-005 and row sources |
| Part 6 | statute against published method | `practice.*` | per row |
Boolean facts (no wage tax, no Medicare cap, flat-rate NRA add-on) are classification inputs written as words, not as tags.
UT period start 2026-04-01 -> flag 58421 and DESIGN-RQ-01 (the earlier table is not carried). OASDI 184,500 (2026) and 192,300 (2027) -> flag 58420 with two labelled lines. MA PFML 2027 -> dated programme rows and Part 6.

## Scope decisions
| Item | Decision | Why |
|---|---|---|
| Federal, State (50 + DC), State programmes | In design | scope manifest; WTC rows US-001 to US-233 |
| Local taxes | By reference to the CCG annexes; routed by 9840061, rates not repeated | the annexes own the locality tables |
| Special populations | All in (US-OWN-005); State-level rules deferred (scope statement) | owner decision |
| Contractors / 1099-NEC | Out (US-OWN-008) | owner decision |
| Per-State graduated tables | Method class + annex reference, not 51 second copies | the approved CCG annexes hold the tables; research wins |
| Employer-assigned SUI rate, supplemental election, W-4 revision, Form 673 | Limitations DESIGN-RQ-02 to 05 | no DD field exists; the DD is approved and not edited here |

## Deviations from this agent's stated constants
- Design accounts are numeric (flags 58401-58423, calculation 58501-58521, regulations 9840011-9840061) because the shared gate check reads numeric flag ids; US WTC codes are `US-nnn`, so flags and accounts map to WTC codes in Parts 1 and 2 and are not WTC codes themselves (reconciled: no flag id exists in the WTC).
- `_pipeline/tag_sync_check.py` and `01-ccg/_build/common/note_vocab_lint.py` extended to 09-design/*.md; nothing else outside 09-design, _pipeline and _research was touched.
- open_check.ps1 opens .docx/.xlsx only: 0 files in 09-design (Markdown design), 0 not clean.
- The unbound-value scan strips WTC code tokens (`US-nnn`, backticked 5-digit codes): identifiers whose digits coincide with unrelated fact values (same practice as the WTC lint). The shared C46 on the design alone still reports 27 period mismatches (one value per key, last file wins) and 9 code-digit collisions: the known package-wide shared-checker limitation. The period-aware C46 is 0.

## Checks (final file)
| Check | Result |
|---|---|
| C29 hard markers / X-run | 0 |
| WORD / PATH / NOTES | 0 / 0 / 0 (note_vocab_lint extended to .md: 0 hits) |
| FRAC / PCT / UNIT | 0 / 0 / 0 |
| C30 | 0 |
| C45 | 23 flags, 21 gates, 0 dead, 0 undeclared, 0 forward reads; shared C45 PASS; a synthetic dead gate is detected |
| C46 period-aware | 438 tags, 0 missing key, 0 mismatch, 31 tags of another period all period-labelled, 0 unbound, binding 1.0 |
| C70 | PASS (all [[GAP:id]] in gaps.json with sources and date; request file matches) |
| C71 | three consecutive rebuilds, identical md5 |
| Recon (09-design/_build/checks/design_recon.csv) | WTC 336, DD 14, register 40, gaps 12, flags 23, regulations 12 references; 0 unmapped |
| tag_sync_check (extended) | DESIGN 438 tags, 0 stale; other artifacts 0 stale |
| C42 / C43 | PASS / PASS (package 1.0) |
| validate_contract --all | PASS (107 files; DESIGN request file validates) |

## Open items
| Location | Marker | Request | Blocking |
|---|---|---|---|
| Part 1 flag 58421; Part 6 item 1 | [[GAP:DESIGN-RQ-01]] Utah table before 2026-04-01 | RQ-01 | no |
| Part 4 (9840024, 9840021); item 2 | [[GAP:DESIGN-RQ-02]] Form W-4 before 2020: allowance method, NRA Table 1 (no DD field) | RQ-02 | no |
| Part 4 (9840022); item 3 | [[GAP:DESIGN-RQ-03]] supplemental method election (no DD field) | RQ-03 | no |
| Part 4 (9840052); item 4 | [[GAP:DESIGN-RQ-04]] SUI assigned rate (no DD field) | RQ-04 | no |
| Part 4 (9840021); item 5 | [[GAP:DESIGN-RQ-05]] Form 673 statement (no DD field) | RQ-05 | no |
| Part 4.4; item 6 | [[GAP:DESIGN-RQ-06]] single new-employer rate for CO, GA, LA, MD, ME, MN, MS, MT, NM, SD, UT, WA, WI, WY | RQ-06 | no |
| Parts 4 and 6 | referenced, not duplicated: RQ-402 and RQ-403 (FUTA credit reduction), RQ-530 (2027 federal), RQ-170 (HI 2027), RQ-351 (VA 2027), RQ-138 (DC method) | existing | no |
Entries DESIGN-RQ-01 to 06 were added to _research/gaps.json (documented_limitation; counts recomputed; backup 09-design/_build/_backup/gaps.json.pre-DESIGN) and _research/DESIGN-research-request.json (ids RQ-01 to 06, schema 1.4.0). DESIGN-RQ-02 to 05 are Data Dictionary additions for the owner to decide, not research gaps.

## Accuracy
88% as a design for a development team. Every value is a bound fact and every code and field reconciles. The remaining 12%: State graduated-withholding and local-tax tables are referenced from the CCG annexes and not restated; six named limitations; no engine run of these regulations (no oracle for the US design). Closing it needs the owner decision on the four Data Dictionary fields and the Utah and new-employer sources named above.

## Round 2 (QA r1 fix batch B1-B15, 2026-11-04)
Copy before the rebuild: 09-design/_build/_backup/pre-r1fix/. Markers read: FACTS-READY and DD-READY, both STATUS: COMPLETE (new DD fields "Supplemental wage withholding method election" and "State-assigned unemployment insurance rate"; fact ma.pfml.rate.selection_basis).
- B1/B2: supplemental wages moved to account 58522/58523 and kept out of 58501; 9840022 flat rate only on the part under the threshold, aggregate method in 58524, 9840023 incremental on the excess; gates 58406/58409/58403.
- B3: RQ-03 and RQ-04 closed (gaps.json status closed); flag 58414 from the new DD field with default rule; flag 58429 and the SUI assigned rate read in 9840052; DD-RQ-11 (notice mechanism) referenced.
- B4: fallbacks in Part 0 and Part 6 for RQ-02 (manual handling) and RQ-05 (withheld normally); DD 1.1 change requests in the gaps.json entries.
- B5: 9840051 split into work-State (58517) and residence-State (58527) results, reciprocity withholds for the residence State, State wages 58525, federal withholding read, Utah gate 58421.
- B6: flat-rate class wording, MA surtax, annex section id on every row. B7: 9840071 minimum wage by hours-worked date.
- B8: flag 58428 (date earned) selects programme parameters; RQ-08 lists parameters without a 2027 value.
- B9: gates for student (FICA and FUTA, Medicare included), clergy on Additional Medicare, F/J/M/Q (58424), totalization (58425), WA Cares (58426), statutory FUTA (58427), household, agricultural and election-worker thresholds (58430); flags 58410, 58412 and 58423 dropped.
- B10/B11: method column; or.stt and NJ workforce fund carried; US-204 moved out of programmes; RQ-07 for US-205, US-207 and the Iowa school district.
- B12: locality flags 58431-58440 from the DD locality fields. B13 done by the source hunter (register consumed_by). B14: jurisdiction register at Part 4 level; W-4 Step fields named; state_wage_base(58417; 58420).
Checks round 2: C45 strict (every flag with values used by a gate, every gate flag named in the Reads): 37 flags, 52 gates, 0 dead, 0 unused, shared C45 PASS; C46 period-aware 520 tags 0 mismatch 0 unbound; tag_sync DESIGN 520 tags 0 stale (CCG shows 11 stale tags from the reworded practice facts: CCG rebuild is pending, not part of this file); recon 0 unmapped (WTC 335, DD 37, register 45, gaps 13, flags 37, regulations 13); note vocabulary 0; C29/WORD/PATH/NOTES/FRAC/PCT/UNIT/C30 0; C70 PASS; three rebuilds identical (C71); validate_contract --all PASS (108 files). Diff vs copy: 704 changed lines; new sections Jurisdiction register and 9840071.

## Round 3 (QA r2 fix batch R2-B1..B8, 2026-11-04)
Copy before the rebuild: 09-design/_build/_backup/pre-r2fix/. Diff: 107 changed lines, 47 lines added.
- R2-B1: 9840071 carries NY, OR, GA and the MN, NM, WA local rows with their periods and the DD fields that pick the region; the federal fallback sentence lists only AL, LA, MS, NC, NH, OK, SC, TN (GA state rate is below federal). Sector and age rates: DESIGN-RQ-10.
- R2-B2: parameters with a per-hour unit (WA supplemental pension) use method per hour. R2-B3: 58524 gated by 58403, 58406, 58409.
- R2-B4: catch-up of earlier wages when a household, agricultural or election-worker threshold is crossed; FUTA liability by any quarter of the current or preceding year.
- R2-B5: 58428 only for MA paid family and medical leave; other programmes on 58420; DESIGN-RQ-09 (paid or earned basis of CA, CO, NJ, NY, WA). R2-B6 by the source hunter. R2-B7: 8 lines appended to PROPAGATION-LEDGER.md.
Checks: strict C45 37 flags, 54 gates, 0 dead, 0 unused; C46 period-aware 561 tags, 0 mismatch, 0 unbound; tag_sync DESIGN 561 tags 0 stale (all artifacts 0 stale); recon 0 unmapped; note vocabulary 0; C70 PASS; three rebuilds identical; validate_contract PASS (109 files). Shared C46 on the design alone still fails on the known one-value-per-key limitation.

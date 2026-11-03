# CCG — build log
Artifact: CCG | Country: US | Round: 1 | Built: 2026-11-02 (sections appended per unit by the parallel builders)

## Units annex_MD, annex_ME, annex_MI, annex_MN, annex_MO, annex_MS, annex_MT, annex_NC, annex_ND, annex_NE, annex_NH, annex_NJ, annex_NM, annex_NV (builder MD–NV, round 1, 2026-11-02)

Artifact: CCG | Country: US | Round: 1 | Brief: `_prompts/ccg-build-brief.md`
Manifest: `_pipeline/build-manifest.json` (USD, minor units 2; tier overall T4; languages en, payslip English; mandate sealed 2026-11-02).
Inputs per unit: `_research/CCG-annex_{JUR}-research-pack.md` + `_research/CCG-annex_{JUR}-facts.json` (801 facts, 123 unresolved, 6 blocking); `00-official-sources/MANDATE.md` (per-jurisdiction tier row, read-only).
Outputs: `01-ccg/annexes/annex_{JUR}.md` (14 files, same folder the other annex builders use). Generator and self-checks: `_research/synthesis-B/_scratch-ccg-build-MD-NV/` (`build_annexes.py`, `decisions.json`, `gap_overrides.json`, `note_overrides.json`, `check_annexes.py`, `append_requests.py`). Rebuild: `python -I build_annexes.py <BASE>` then `python -I check_annexes.py <BASE>`.

### Precedent inspection (L1)
`shared/REFERENCE_CCG_Bulgaria.docx` opened with python-docx: 1,317 paragraphs, 3 tables; styles Heading 1 (14, one per module + Version Control), Heading 2 (84), Heading 3 (210 = template questions), Heading 4 (2); version table 5 columns (Version, Effective Date, Change Description, Status, Updated By). The annexes carry no template questions (the 265-line question list governs m01–m13), so each annex uses H1 = annex, H2 = numbered section ({JUR}.0–{JUR}.20); assembly maps them one level below the module H1 if the assembler nests annexes.

### Annex structure (identical in all 14)
{JUR}.0 scope (federal layer → Annex FED, multistate → Annex MULTI, contractors out of scope, payslip English) · {JUR}.1 jurisdiction layer (tier + basis quoted from the MANDATE per-jurisdiction tier table; MI and NJ basis re-worded to bind their numbers to keys) · {JUR}.2 configuration decisions (hand-written from the pack §0.1 traps and the brief's journal traps; every number tagged) · {JUR}.3–{JUR}.17 the 13 domains (labour; withholding; non-residents/reciprocity; local taxes; SUI/SDI/PFML/levies; pay statement; reporting; leave; termination; taxable wages/BIK; deductions/garnishments; prevailing wage; indexation; data protection/records; legal change) each = facts table (Item key | Value | Valid from | Valid to | Source register_id (tier, authority) | Note) + number-free rules from the pack + RESEARCH-GAP markers · {JUR}.18 special populations · {JUR}.19 language · {JUR}.20 sources (register_id → authority; the URL stays in the register row).

### Fact bindings
- 801 of 801 facts written as `[[FACT:key=value]]` in a table row (one row per fact and period); 979 tags in total (decisions and notes cite the same keys). Full section → key → value → register_id table: `_pipeline/CCG-bindings-annex_MD-NV.csv` (801 table bindings + 93 note bindings).
- Notes column = the fact's own `note` (attribute of the bound fact, same register_id). Distinctive numbers inside notes that equal a fact value are tagged with that key: own annex first, then a same-jurisdiction key from another facts file (e.g. `md.local.county.carroll.rate`, `nj.bik.lodging.weekly`, `ms.oracle.weekly_460_0ex.withholding`), then `fed.minwage.hourly` only (7.25 references). 93 such note tags, listed in the CSV.
- Rule lines carried from the pack are kept only when the whole line contains no number and no pipeline wording (top-level bullets; sub-bullet fragments dropped); special-population lines keep their number-free clauses.
- Self-check (`check_annexes.py`, C46 logic of `shared/consistency-checks`, run against all 73 facts files): 979 tags, 0 key/value mismatches, 0 unbound distinctive values, 0 C29 markers, 0 C47 rework words (one NM rule line holds "check or draft", bank-draft sense — LEGIT for C47 config if flagged).

### Decisions and deviations
- Trap handling (brief + pack §0.1): MI tips/overtime deduction stated as assessment-only, not modelled in withholding; MI prevailing wage never read off the 2023 US DOL table; NE Circular EN withholding rates kept apart from statutory rates (assessment); ND booklet example declared stale, table/formula result `nd.pit.oracle.example_1.withholding` used; NC withholding rate `nc.pit.wh.rate` used, not the statutory rate; MS 2027 rate liability-only; MT/NE 2027 minimum wage and NC 2027 rate not written (blocking gaps); ME combined new-employer UI rate flagged unconfirmed because of the UPAF conflict; NJ GIT vs UI/TDI/FLI base differences and employer-only city payroll taxes; NV MBT base = UI gross wages.
- 21 fact notes rewritten (`note_overrides.json`): bare numbers that collided with other jurisdictions' fact values (C46 false bindings: e.g. "Section 125" vs an AR threshold 125, "2018 PA 338" vs an OR garnishment floor) or pipeline wording; the dropped numbers are restatements or derivation scaffolding, the bound value is unchanged. Unverified candidate values that appear in some `unresolved[].why` texts (ME UPAF component, ME 2027 exempt threshold, MT/NE 2027 minimum wage, NC 2027 rate, MD domestic threshold) are NOT written; those gap texts were re-worded (`gap_overrides.json`).
- Generic sanitizer removes pipeline wording from notes and gap texts (legacy, stage 5, Python, G-DERIVE, tier-B, annex_X → Annex X, OQ ids); "(the source address is held in the register row)" replaces the URL column (URL digits triggered C46 false positives).
- Worked examples: the annexes contain no computed example tables (state oracle examples are in m12). Arithmetic quoted inside notes was re-computed by hand: ME 871.1538, MI 11.6705 / 75.36 / 47.45, MN 91.27, MT 10.86→10.85 and 47,285.31, NC 10.03, ND 701.51 / 13.49, NM 15.402, NV 68,128.92 / 45,419.28 — all reproduce.

### Checker limitation to route (not fixable by the builder)
- 62 tags carry a value valid in a period other than the last one listed for the same key (multi-period keys: e.g. `nj.minwage.hourly` 2026/2027, `mi.minwage.hourly` 2025/2026/2027, `mt.pit.bracket.1.ceiling.*` 2026/2027, `nm.labour.minwage.local.santa_fe_city.hourly`, `mo.sui.wage_base` 2025/2026). `consistency_checks.c46` keeps one value per key (last wins), so it will report these as mismatches although each equals a fact. Fix belongs to the checker (key + effective_from) or the facts schema; detail: `_research/synthesis-B/_scratch-ccg-build-MD-NV/check_output.txt`.
- `nd.sdi_pfml.exists` note cites N.D.C.C. 34-01-15.1; "15.1" can collide with `me.minwage.hourly` (15.1, 2026 period) if the checker's last-wins order changes.

### Open items (RESEARCH-GAP markers, all in place in the annex)
137 markers → `_research/CCG-research-request.json` RQ-001…RQ-137 (file created by this builder; schema research-request 1.4.0 PASS).
- Blocking (6): `me.sui.upaf.rate.conflict` (ME.7), `mi.local.cities.rates` (MI.6), `mt.minwage.hourly.next_year` (MT.3), `nc.pit.rate.next_year` (NC.4), `ne.minwage.hourly.next_year` (NE.3), `nm.labour.minwage.local.other` (NM.3).
- Non-blocking (131): the 117 non-blocking `unresolved[]` items of the 14 facts files + 14 `{jur}.special_populations.thresholds` items (special-population thresholds stated in the packs without a facts key).

### Accuracy
Research-only evidence per annex (official statutes and authority pages via the register; no portal or real filing): ~85% overall. Every value is bound to a register row; what keeps the annexes below 90% is the 6 blocking gaps (Michigan city rates, Santa Fe County minimum wage, three 2027 values, Maine UPAF) and the special-population thresholds without facts. Closing them needs the source-hunter (A.1/A.2 rows), not more building.

## Units annex_DC, annex_DE, annex_FL, annex_GA, annex_HI, annex_IA, annex_ID, annex_IL, annex_IN, annex_KS, annex_KY, annex_LA, annex_MA (builder 4 of 6), round 1

Artifact: CCG | Country: US | Round: 1 | Built: 2026-11-02
Manifest: _pipeline/build-manifest.json (USD, minor units 2, rounding 0.01/0.01, year 2026, overall tier T4; state_income_tax T4, local_income_tax T4; languages en, payslip English). Mandate: 00-official-sources/MANDATE.md sealed 2026-11-02 (contractors / 1099-NEC out of scope, US-OWN-008).
Brief: _prompts/ccg-build-brief.md. Inputs per unit: _research/CCG-annex_{JUR}-research-pack.md and _research/CCG-annex_{JUR}-facts.json (validated by Synthesis C/D). No fetching; no edit of facts, register, MANDATE or manifest.

### Precedent inspection (L1)
- `shared/REFERENCE_CCG_Bulgaria.docx` opened with python-docx (toolkit `inspect_docx.py`): 1 section, portrait 8.5 x 11 in, 310 headings (H1 14 = Version Control + 13 modules, H2 84, H3 210, H4 2), 3 tables, 18,276 words, C29 scan clean. The precedent has no jurisdiction annexes; annex structure below is this build's own (H1 per annex, H2 per domain, parameter tables), to be placed after the 13 modules at assembly.
- `shared/CCG_TEMPLATE_QUESTIONS.md` governs m01..m13 (H3 = template question). Annexes are not template modules, so no H3-per-question rule applies; the domain order follows the research-pack sections (1..13 + worked examples, special populations, language).

### Outputs
- `01-ccg/modules/annex_{DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA}.md` (13 files, same folder as annex_AK..CT / FED / MULTI).
- PATH NOTE for assembly: the MD..WY builders wrote to `01-ccg/annexes/`; annexes are therefore split across `01-ccg/modules/` (AK..MA, FED, MULTI) and `01-ccg/annexes/` (MD..WY). The DOCX assembly must read both or the orchestrator must pick one folder.
- Build scripts (reproducible, scratch): `01-ccg/_scratch/annex-DC-MA/build_annexes.py` (annex generator), `overrides.py` (text overrides and internal-wording cleaning, all logged), `build_examples_annex_DC-MA.py` (worked examples, computed from facts and asserted against the oracle facts), `check_c46.py` (local C46 emulation), `append_requests.py`, `write_log.py`. Rebuild: `python build_examples_annex_DC-MA.py <BASE>` then `python build_annexes.py <BASE> DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA`.

### Construction rules applied
- Every fact object of each annex facts file is written once as a parameter row (key, `[[FACT:key=value]]`, period in force, register_id + authority + tier + verification method + confidence, note). Multi-period keys get one row per period.
- Notes are the fact record's own note (bound to that row's key and register_id). Notes that were truncated copies of register text ("Derivation recorded in register row ...", 61 notes) are replaced by a pointer to the register row instead of the truncated text.
- Pack narrative (non-fact lines) is carried with its register citations; distinctive numbers equal to a USD / percent / ratio fact of the same annex are tagged automatically (same-section key preferred). Pipeline-internal wording (Python, Synthesis, MANDATE, Q-ids, OQ-ids, legacy, tier-B / MANUAL / gated, browser pass, builder, engine) is rewritten by the CLEAN rules in `overrides.py` (C47).
- Each `unresolved[]` item of a facts file is a `⚠️ RESEARCH-GAP` line in place (section chosen by key), with blocking / non-blocking and what would close it, plus one research request (below). Blocking items are not filled.
- Brief traps written as explicit configuration rules: KS withholding uses KW-100 table parameters, not the statutory brackets (KS.2); GA.2, IA.2, HI.2, DC.2 tips/overtime deductions at assessment only, withholding unchanged; DC 2026 withholding method unpublished = blocking gap `dc.wh.method` (DC.2); MA PFML 2026 per DFML table, swap from 2027-01-01 (MA.3).
- Layer classification line per annex taken from the manifest tier census: FL T1; DE, KY T4; DC, GA, HI, IA, ID, IL, IN, KS, LA, MA T3.

### Fact bindings (summary; full section -> key -> register_id table below)
| Unit | facts | distinct keys | own keys tagged | tags in file | cross-unit keys cited | RESEARCH-GAP blocking / non-blocking |
|---|---|---|---|---|---|---|
| annex_DC | 51 | 44 | 44 | 75 | - | 2 / 7 |
| annex_DE | 70 | 68 | 68 | 127 | - | 1 / 7 |
| annex_FL | 37 | 35 | 35 | 59 | `fed.tipped.cash_wage.hourly` | 1 / 5 |
| annex_GA | 45 | 44 | 44 | 74 | `fed.ccpa.protected_weekly`, `fed.minwage.hourly`, `fed.tipped.cash_wage.hourly` | 2 / 7 |
| annex_HI | 87 | 85 | 85 | 124 | - | 1 / 8 |
| annex_IA | 45 | 44 | 43 | 72 | - | 0 / 9 |
| annex_ID | 42 | 39 | 39 | 77 | - | 1 / 9 |
| annex_IL | 51 | 51 | 51 | 86 | - | 2 / 9 |
| annex_IN | 49 | 44 | 44 | 101 | - | 0 / 8 |
| annex_KS | 54 | 54 | 54 | 83 | - | 0 / 7 |
| annex_KY | 44 | 44 | 44 | 87 | `ky.oracle.biweekly_1500.result` | 1 / 10 |
| annex_LA | 34 | 34 | 34 | 60 | `fed.minwage.hourly` | 2 / 11 |
| annex_MA | 63 | 60 | 60 | 100 | - | 2 / 13 |
| **total** | 672 | 646 | 645 | 1125 | | 15 / 110 |

Untaggable value (carried verbatim in the row with its key, no tag): `ia.wh.method` (its value contains square brackets, `[US-IAS5-015]`, which would break the `[[FACT:]]` tag syntax). Cross-unit keys are cited with the exact value of the FED annex / WTC facts files.

### Worked examples (C38): computed from facts, asserted against the published oracle facts
| Example | Computed | Oracle | Result |
|---|---|---|---|
| DE-1 | 13.88 | 13.88 | match |
| DE-2 | 269.63 | 269.63 | match |
| GA-1 | 27.03 | 27.03 | match |
| HI-1 | 9.58 | 9.58 | match |
| IA-1 | 114.92 | 114.92 | match |
| ID-1 | 31 | 31 | match |
| IL-2 | 32.13 | 32.13 | match |
| IL-1 | 8.33 | 8.38 | NO MATCH -> RESEARCH-GAP il.oracle.il700t.example1.inputs |
| IN-1 state | 13.96 | 13.96 | match |
| IN-1 county | 4.73 | 4.73 | match |
| KY-1 | 104.65 | 104.65 | match |
| KY-2 annual | 1247.40 | 1247.4 | match |
| LA-1 | 13.98 | 13.98 | match |
| LA-2 | 111.54 | 111.54 | match |
No state oracle example in the facts for DC, FL, KS, MA (section 14 says so). ID-2 (published 20) not reproduced: its zero bracket matches neither ID table (open item `id.wh.example_threshold_discrepancy`). KY-2 per-period rounding (sheet prints 47) open (`ky.wh.rounding.tax`).

### Text overrides applied (each binds a number to an existing key or removes an unkeyed number)
- DC: `401(k), 125, HSA` -> `401(k), s.125, HSA` (x1)
- DE: ` (Withholding unit 302-577-8779)` -> ` (Withholding unit)` (x1)
- DE: ` Separate DD/RSPEC payable line.` -> ` Separate payable line.` (x1)
- FL: `still prints 6.15 (stale; overridden)` -> `still prints a stale pre-amendment amount (overridden)` (x1)
- FL: `Capped at the 2003 FLSA tip credit: 5.15 - 2.13 = ` -> `Capped at the 2003 FLSA tip credit (2003 federal minimum wage less the federal tipped cash wage [[FACT:fed.tip` (x1)
- FL: ` (DD/RSPEC scope item)` -> `` (x1)
- FL: ` (Stage 3 / RSPEC)` -> `` (x1)
- GA: `the federal 7.25 applies` -> `the federal [[FACT:fed.minwage.hourly=7.25]] applies` (x1)
- GA: `CCPA floor 30 x 7.25 = 217.50 binds [US-FED-011]: use 217.50` -> `CCPA floor 30 x [[FACT:fed.minwage.hourly=7.25]] = [[FACT:fed.ccpa.protected_weekly=217.50]] binds [US-FED-011` (x1)
- GA: `federal 2.13` -> `federal [[FACT:fed.tipped.cash_wage.hourly=2.13]]` (x1)
- GA: `; derived projection 4.865% / 30,750 / 15,375 / 5,125 is not a fact.` -> `; no 2027 value is modelled until it is published.` (x1)
- GA: ` 2026 rate range not on a primary source (secondary source: 0.04-8.10%): not a fact.` -> ` The 2026 rate range is not on a primary source and is not modelled.` (x1)
- GA: `; enacted version and sunset unconfirmed - not a fact.` -> `; enacted version and sunset unconfirmed, not modelled.` (x1)
- GA: `HB 463 conditional step schedule: rate -0.125/yr from 2027 to 3.99%; std deduction +750/+375 to 36,000/18,000;` -> `HB 463 sets a conditional step schedule for the rate, standard deduction and dependent allowance from 2027; no` (x1)
- HI: `IRC 225 overtime` -> `IRC s.225 overtime` (x1)
- HI: `continues to 8.25/9/10/11% above` -> `continues to higher rates above` (x1)
- HI: `would close it: Final merge: alias row for HRS 387-6(c) with S5-pattern id.)` -> `would close it: a legal-basis register row that cites HRS 387-6(c) directly at high confidence.)` (x1)
- IA: `(cash wage 4.35 derived on [[FACT:ia.minwage.hourly=7.25]])` -> `(cash wage derived as the minimum wage [[FACT:ia.minwage.hourly=7.25]] less the 40% credit)` (x1)
- IA: `(correction: not whole dollar as US-IA-001 and the MANDATE currency block say)` -> `(not whole dollar)` (x1)
- IA: ` Supersedes the rounding clause of US-IA-001 and the MANDATE currency block listing IA as whole-dollar` -> ` Supersedes the whole-dollar rounding clause of US-IA-001` (x1)
- IA: ` (S5A-MERGE note on US-IA-001)` -> `` (x1)
- IA: `RESEARCH-GAP: US-IA-001 and the MANDATE currency block say whole-dollar; 2026 formula/tables say nearest cent.` -> `RESEARCH-GAP: an older register row (US-IA-001) states whole-dollar rounding; the 2026 formula and tables say ` (x1)
- IA: `would close it: Synthesis supersedes the rounding clause of US-IA-001 by US-IAS5-005/-015 (done in S5A note); ` -> `would close it: the Iowa Department of Revenue 2025 withholding formula, needed only for periods before 2026.)` (x1)
- IL: `(HSA, 125)` -> `(HSA, s.125)` (x1)
- IN: `HSA/125/transit` -> `HSA/s.125/transit` (x2)
- IN: `PIT statutory step 2.95 -> 2.90` -> `PIT statutory step [[FACT:in.pit.rate=2.95]]% -> [[FACT:in.pit.rate=2.9]]%` (x1)
- KS: ` 2027 projection ~15,700 NOT a fact.` -> ` No 2027 value is modelled.` (x1)
- KY: `(125/deferred comp)` -> `(s.125/deferred comp)` (x2)
- KY: `sheet shows 47 for 47.98` -> `sheet shows 47 for [[FACT:ky.oracle.biweekly_1500.result=47.98]]` (x2)
- KY: `/26 = 47.98, sheet shows 47` -> `/26 = [[FACT:ky.oracle.biweekly_1500.result=47.98]], sheet shows 47` (x1)
- LA: `of 125, 401(k)` -> `of s.125, 401(k)` (x1)
- LA: `(FLSA 7.25)` -> `(FLSA [[FACT:fed.minwage.hourly=7.25]])` (x1)
- LA: `FLSA 7.25 for covered` -> `FLSA [[FACT:fed.minwage.hourly=7.25]] for covered` (x1)
- LA: ` [[FACT:la.wh.std_deduction.single=12,875]]/12,500 = 1.03 (2025 base secondary source only).` -> `` (x1)
- MA: `401(k)/403(b), 125, HSA` -> `401(k)/403(b), s.125, HSA` (x1)
- MA: `12.65, 14.37, 16.33` -> `12.65, [[FACT:ma.sui.employer.rate.max=14.37]], 16.33` (x1)

### Local C46 emulation on the annex markdown (the real check runs on the assembled DOCX)
- Tags whose key is not in any facts file: 0. Tags disagreeing with every period of their key: 0.
- 53 tags carry the value of a NON-LAST period of a multi-period key (e.g. `dc.minwage.hourly` 17.95 to 2026-06-30 and 18.40 from 2026-07-01). `consistency_checks.c46` keeps only the last value per key (`facts[f['key']] = f.get('value')`), so it will report these as mismatches although each tag equals the fact of its own period. Checker limitation, not a content defect: needs either a period-aware C46 or period-qualified keys in the facts (owner of shared/ decides).
- 17 residual untagged numbers that coincide with a fact value of ANOTHER unit (legal citations or example arithmetic, no key of their own):
  - annex_DC (39, '214', ['oh.local.school_district.count', 'oh.pit.school_district.count'])
  - annex_DC (160, '214', ['oh.local.school_district.count', 'oh.pit.school_district.count'])
  - annex_DE (187, '1,750.00', ['ga.pit.overtime_subtraction.max', 'ga.pit.tip_subtraction.max'])
  - annex_DE (187, '1,750.00', ['ga.pit.overtime_subtraction.max', 'ga.pit.tip_subtraction.max'])
  - annex_GA (63, '347', ['ut.oracle.pub14.monthly_married_7800.result', 'ut.pit.oracle.example_4.withholding'])
  - annex_GA (172, '276', ['ct.report.sui.record_length'])
  - annex_HI (110, '1.21', ['ri.sui.new_employer.rate'])
  - annex_HI (179, '1.21', ['ri.sui.new_employer.rate'])
  - annex_IA (63, '871', ['hi.tdi.benefit.weekly_max'])
  - annex_ID (165, '20.38', ['fed.levy.exempt.per_dependent.daily'])
  - annex_KS (5, '269', ['hi.wh.bracket.married.2.base_tax'])
  - annex_KS (41, '512', ['fed.efw2.record_length', 'rspec.fed.efw2.record_length'])
  - annex_KY (148, '367', ['ut.oracle.pub14.quarterly_single_9000.result', 'ut.pit.oracle.example_5.withholding'])
  - annex_MA (30, '4.58', ['wv.pit.statutory.rate.top'])
  - annex_MA (87, '1.21', ['ri.sui.new_employer.rate'])
  - annex_MA (87, '12.65', ['az.minwage.tipped.cash_wage'])
  - annex_MA (195, '2.25', ['ky.local.lexington.rate', 'md.local.county.worcester.rate', 'md.nonres.special_rate'])
  - annex_MA: 0, 'multi': 53, 'unbound': 17, 'notkey': 0, 'tags': 1125}
  Reasons: DC 214 = D.C. Act 26-214 citation; DE 1,750.00 = bracket-5 slice of example DE-1; GA 347 = HB 347 citation, 276 = withholding-table band in the guide example; HI 1.21 = TDI statutory multiplier (no key); IA 871 = 871 IAC citation; ID 20.38 = unrounded published example; KS 269 = SB 269 citation, 512 = KS period threshold in a note; KY 367 = KRS 367 citation; MA 4.58 = M-4 semimonthly per-person amount, 1.21 / 12.65 = schedule-table cells, 2.25 = meal deduction cap. None is a claim about the other unit's fact.

### Research requests appended to `_research/CCG-research-request.json`
- 125 items, RQ-138..RQ-262 (one per RESEARCH-GAP marker: 124 facts-file `unresolved[]` items + 1 new: `il.oracle.il700t.example1.inputs`). File re-read immediately before writing; existing items untouched; validated with `shared/schemas/validate_contract.py research-request` -> PASS.
- Blocking (15): `dc.live.fy2027_bsa_permanent`, `dc.wh.method`, `de.wh.w4_2020_mapping`, `fl.sui.wages.401k_deferral`, `ga.pit.rate.next_year`, `ga.report.w2.rs_layout.current`, `hi.wh.bracket.next_year`, `id.wh.certificate.current_edition`, `il.leave.chicago.paid_leave.payout`, `il.leave.cook.paid_leave`, `ky.local.occupational_tax.census`, `la.nonres.mobile_workforce.catch_up`, `la.pit.conformity`, `ma.pit.conformity.items`, `ma.report.w2.due_date_conflict`.

### Deviations from the agent's stated constants
- Annex layout (H1 annex, H2 domain, parameter tables) is not in the Bulgaria precedent, which has no annexes; it is a build decision, reversible at assembly.
- Output folder `01-ccg/modules/` (brief: 'one output file per unit under 01-ccg/'); see PATH NOTE.
- `[[FACT:]]` tags on bool and string facts are written with the exact facts value (string comparison in C46).

### Open items
- 15 blocking RESEARCH-GAP markers: the annexes DC, DE, FL, GA, HI, ID, IL, KY, LA, MA cannot close until they are answered (IA, IN, KS have no blocking gap).
- 110 non-blocking markers ship as named limitations (each with what would close it, in place and in the research request).
- C29: no residual marker other than the RESEARCH-GAP lines (lint run on the 13 files: 0 hits for placeholder/TODO/TBD/FIXME/XXX/[CHECK]/[?]/VERIFY No./to be confirmed/to be verified).

### Accuracy
About 85%. Every value is an A.1/A.2 register-backed fact (some at medium confidence) and the 13 computable oracle examples reproduce the published results except IL-700-T example 1. The gap is the 15 blocking items (DC 2026 withholding method and the permanent FY2027 act; DE W-4 2020+ mapping; FL 401(k) deferrals in the UI base; GA TY2026 W-2 RS layout and 2027 rate trigger; HI 2027 withholding tables; ID W-4 2026 edition; IL Chicago and Cook County paid leave; KY local occupational-tax census; LA mobile-workforce catch-up and IRC conformity; MA W-2 due date and IRC conformity) and 110 non-blocking items, mostly file layouts behind employer logins and statute texts not read. They are closed by the authorities' own publications listed per request, not by more secondary research.

### Full binding table (section -> key -> register_id)
| Location | key | register_id |
|---|---|---|
| 01-ccg/modules/annex_DC.md Employment and labour code | `dc.minwage.coverage` | US-DCS5-001 |
| 01-ccg/modules/annex_DC.md Employment and labour code | `dc.minwage.hourly` | US-DCS5-011 |
| 01-ccg/modules/annex_DC.md Employment and labour code | `dc.minwage.tipped.cash_wage` | US-DCS5-011 |
| 01-ccg/modules/annex_DC.md Employment and labour code | `dc.minwage.tipped.percent_of_minimum` | US-DCS5-001 |
| 01-ccg/modules/annex_DC.md Employment and labour code | `dc.overtime.weekly_threshold_hours` | US-DCS5-001 |
| 01-ccg/modules/annex_DC.md Employment and labour code | `dc.pay_frequency.rule` | US-DCS5-002 |
| 01-ccg/modules/annex_DC.md Employment and labour code | `dc.payment.method` | US-DCS5-002 |
| 01-ccg/modules/annex_DC.md Employment and labour code | `dc.tipped.third_party_payroll.required` | US-DCS5-010 |
| 01-ccg/modules/annex_DC.md State income tax withholding | `dc.pit.obbba_deductions` | US-DCS5-021 |
| 01-ccg/modules/annex_DC.md State income tax withholding | `dc.pit.personal_exemption.repealed` | US-DCS5-021 |
| 01-ccg/modules/annex_DC.md State income tax withholding | `dc.pit.rate_schedule` | US-DCP52-001 |
| 01-ccg/modules/annex_DC.md State income tax withholding | `dc.wh.certificate.status` | US-DCS5-013 |
| 01-ccg/modules/annex_DC.md State income tax withholding | `dc.wh.lump_sum_retirement.rate` | US-DCS5-025 |
| 01-ccg/modules/annex_DC.md State income tax withholding | `dc.wh.notice_2022_08` | US-DCP51-002 |
| 01-ccg/modules/annex_DC.md State income tax withholding | `dc.wh.statutory_method` | US-DCS5-025 |
| 01-ccg/modules/annex_DC.md Non-resident regime and reciprocity | `dc.nonres.taxable` | US-DCP51-006 |
| 01-ccg/modules/annex_DC.md Social insurance (unemployment, disability, paid leave, levies) | `dc.pfl.benefit.weekly_max` | US-DCS5-021 |
| 01-ccg/modules/annex_DC.md Social insurance (unemployment, disability, paid leave, levies) | `dc.pfl.coverage` | US-DCS5-007 |
| 01-ccg/modules/annex_DC.md Social insurance (unemployment, disability, paid leave, levies) | `dc.pfl.employer.rate` | US-DCS5-019 |
| 01-ccg/modules/annex_DC.md Social insurance (unemployment, disability, paid leave, levies) | `dc.pfl.wage_cap.exists` | US-DCS5-020 |
| 01-ccg/modules/annex_DC.md Social insurance (unemployment, disability, paid leave, levies) | `dc.sui.admin_assessment.rate` | US-DCS5-017 |
| 01-ccg/modules/annex_DC.md Social insurance (unemployment, disability, paid leave, levies) | `dc.sui.employee.rate` | US-DCS5-017 |
| 01-ccg/modules/annex_DC.md Social insurance (unemployment, disability, paid leave, levies) | `dc.sui.employer.rate.max` | US-DCS5-017 |
| 01-ccg/modules/annex_DC.md Social insurance (unemployment, disability, paid leave, levies) | `dc.sui.employer.rate.min` | US-DCS5-017 |
| 01-ccg/modules/annex_DC.md Social insurance (unemployment, disability, paid leave, levies) | `dc.sui.new_employer.rate` | US-DCS5-016 |
| 01-ccg/modules/annex_DC.md Social insurance (unemployment, disability, paid leave, levies) | `dc.sui.wage_base` | US-DCS5-017 |
| 01-ccg/modules/annex_DC.md Pay statement | `dc.hire_notice.language` | US-DCS5-010 |
| 01-ccg/modules/annex_DC.md Pay statement | `dc.payslip.items` | US-DCS5-010 |
| 01-ccg/modules/annex_DC.md Statutory reporting | `dc.newhire.report_days` | US-DCS5-022 |
| 01-ccg/modules/annex_DC.md Statutory reporting | `dc.report.pfl.quarterly` | US-DCS5-019 |
| 01-ccg/modules/annex_DC.md Statutory reporting | `dc.report.sui.quarterly` | US-DCS5-018 |
| 01-ccg/modules/annex_DC.md Statutory reporting | `dc.report.w2` | US-DCS5-015 |
| 01-ccg/modules/annex_DC.md Statutory reporting | `dc.report.w2.efile_threshold` | US-DCS5-015 |
| 01-ccg/modules/annex_DC.md Statutory reporting | `dc.report.wh.fr900q` | US-DCS5-014 |
| 01-ccg/modules/annex_DC.md Leave | `dc.leave.sick.accrual.100_plus` | US-DCS5-004 |
| 01-ccg/modules/annex_DC.md Leave | `dc.leave.sick.accrual.25_99` | US-DCS5-004 |
| 01-ccg/modules/annex_DC.md Leave | `dc.leave.sick.accrual.under_25` | US-DCS5-004 |
| 01-ccg/modules/annex_DC.md Leave | `dc.leave.sick.payout_on_separation` | US-DCS5-024 |
| 01-ccg/modules/annex_DC.md Termination and final pay | `dc.final_pay.rule` | US-DCS5-003 |
| 01-ccg/modules/annex_DC.md Deductions and garnishments | `dc.garn.creditor.rule` | US-DCS5-006 |
| 01-ccg/modules/annex_DC.md Deductions and garnishments | `dc.garn.creditor.weekly_threshold` | US-DCS5-006 |
| 01-ccg/modules/annex_DC.md Collective agreements and prevailing wage | `dc.living_wage.contract_threshold` | US-DCS5-009 |
| 01-ccg/modules/annex_DC.md Collective agreements and prevailing wage | `dc.living_wage.hourly` | US-DCS5-012 |
| 01-ccg/modules/annex_DC.md Payroll data protection and records | `dc.records.retention_years` | US-DCS5-010 |
| 01-ccg/modules/annex_DE.md Employment and labour code | `de.minor.work_permit.required` | US-DES5-017 |
| 01-ccg/modules/annex_DE.md Employment and labour code | `de.minwage.exclusions` | US-DES5-001 |
| 01-ccg/modules/annex_DE.md Employment and labour code | `de.minwage.hourly` | US-DES5-001 |
| 01-ccg/modules/annex_DE.md Employment and labour code | `de.minwage.tipped.cash_wage` | US-DES5-001 |
| 01-ccg/modules/annex_DE.md Employment and labour code | `de.pay_frequency.rule` | US-DES5-002 |
| 01-ccg/modules/annex_DE.md Employment and labour code | `de.payment.method` | US-DES5-002 |
| 01-ccg/modules/annex_DE.md Employment and labour code | `de.wage_theft.penalty.max` | US-DES5-002 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.pit.bracket.1.ceiling` | US-DES5-003 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.pit.bracket.2.ceiling` | US-DES5-003 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.pit.bracket.2.rate` | US-DES5-003 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.pit.bracket.3.ceiling` | US-DES5-003 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.pit.bracket.3.rate` | US-DES5-003 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.pit.bracket.4.ceiling` | US-DES5-003 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.pit.bracket.4.rate` | US-DES5-003 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.pit.bracket.5.ceiling` | US-DES5-003 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.pit.bracket.5.rate` | US-DES5-003 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.pit.bracket.6.ceiling` | US-DES5-003 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.pit.bracket.6.rate` | US-DES5-003 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.pit.bracket.7.rate` | US-DES5-003 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.wh.certificate` | US-DES5-008 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.wh.deferred_comp.recommended_rate` | US-DES5-006 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.wh.duty` | US-DES5-005 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.wh.method` | US-DES5-006 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.wh.personal_credit.per_exemption` | US-DES5-006 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.wh.std_deduction.mfj` | US-DES5-006 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.wh.std_deduction.single` | US-DES5-006 |
| 01-ccg/modules/annex_DE.md State income tax withholding | `de.wh.supplemental.method` | US-DES5-006 |
| 01-ccg/modules/annex_DE.md Non-resident regime and reciprocity | `de.nonres.convenience_rule` | US-DES5-004 |
| 01-ccg/modules/annex_DE.md Non-resident regime and reciprocity | `de.reciprocity.exists` | US-DES5-008 |
| 01-ccg/modules/annex_DE.md Local wage taxes | `de.local.wilmington.eit.rate` | US-DEP52-001 |
| 01-ccg/modules/annex_DE.md Social insurance (unemployment, disability, paid leave, levies) | `de.pfml.benefit.weekly_max` | US-DES5-012 |
| 01-ccg/modules/annex_DE.md Social insurance (unemployment, disability, paid leave, levies) | `de.pfml.employee_share.max_percent` | US-DES5-012 |
| 01-ccg/modules/annex_DE.md Social insurance (unemployment, disability, paid leave, levies) | `de.pfml.multistate` | US-DES5-012 |
| 01-ccg/modules/annex_DE.md Social insurance (unemployment, disability, paid leave, levies) | `de.pfml.rate.cap` | US-DES5-012 |
| 01-ccg/modules/annex_DE.md Social insurance (unemployment, disability, paid leave, levies) | `de.pfml.rate.family_caregiving` | US-DES5-012 |
| 01-ccg/modules/annex_DE.md Social insurance (unemployment, disability, paid leave, levies) | `de.pfml.rate.medical` | US-DES5-012 |
| 01-ccg/modules/annex_DE.md Social insurance (unemployment, disability, paid leave, levies) | `de.pfml.rate.parental` | US-DES5-012 |
| 01-ccg/modules/annex_DE.md Social insurance (unemployment, disability, paid leave, levies) | `de.pfml.rate.total` | US-DES5-012 |
| 01-ccg/modules/annex_DE.md Social insurance (unemployment, disability, paid leave, levies) | `de.sui.employee.rate` | US-DES5-011 |
| 01-ccg/modules/annex_DE.md Social insurance (unemployment, disability, paid leave, levies) | `de.sui.employer.rate.max` | US-DES5-022 |
| 01-ccg/modules/annex_DE.md Social insurance (unemployment, disability, paid leave, levies) | `de.sui.employer.rate.min` | US-DES5-022 |
| 01-ccg/modules/annex_DE.md Social insurance (unemployment, disability, paid leave, levies) | `de.sui.new_employer.rate` | US-DES5-022 |
| 01-ccg/modules/annex_DE.md Social insurance (unemployment, disability, paid leave, levies) | `de.sui.op_tech_assessment.rate` | US-DEL-003 |
| 01-ccg/modules/annex_DE.md Social insurance (unemployment, disability, paid leave, levies) | `de.sui.wage_base` | US-DES5-010 |
| 01-ccg/modules/annex_DE.md Pay statement | `de.payslip.employer_threshold` | US-DES5-002 |
| 01-ccg/modules/annex_DE.md Pay statement | `de.payslip.items` | US-DES5-002 |
| 01-ccg/modules/annex_DE.md Statutory reporting | `de.newhire.report_days` | US-DES5-005 |
| 01-ccg/modules/annex_DE.md Statutory reporting | `de.report.annual.wth_rec` | US-DES5-009 |
| 01-ccg/modules/annex_DE.md Statutory reporting | `de.report.pfml.quarterly` | US-DES5-013 |
| 01-ccg/modules/annex_DE.md Statutory reporting | `de.report.sui.quarterly` | US-DES5-011 |
| 01-ccg/modules/annex_DE.md Statutory reporting | `de.report.w2.employee_on_termination_days` | US-DES5-005 |
| 01-ccg/modules/annex_DE.md Statutory reporting | `de.report.w2.paper_max_forms` | US-DES5-009 |
| 01-ccg/modules/annex_DE.md Statutory reporting | `de.report.wh.calendar` | US-DES5-007 |
| 01-ccg/modules/annex_DE.md Statutory reporting | `de.report.wh.frequency` | US-DES5-005 |
| 01-ccg/modules/annex_DE.md Leave | `de.leave.sick.state_statute.exists` | US-DES5-021 |
| 01-ccg/modules/annex_DE.md Leave | `de.pfml.leave.parental_weeks` | US-DES5-012 |
| 01-ccg/modules/annex_DE.md Termination and final pay | `de.final_pay.rule` | US-DES5-002 |
| 01-ccg/modules/annex_DE.md Benefits in kind and taxable wages | `de.pit.conformity` | US-DES5-019 |
| 01-ccg/modules/annex_DE.md Deductions and garnishments | `de.deductions.rule` | US-DES5-002 |
| 01-ccg/modules/annex_DE.md Deductions and garnishments | `de.garn.child_support.arrears_addon_percent` | US-DES5-016 |
| 01-ccg/modules/annex_DE.md Deductions and garnishments | `de.garn.creditor.exempt_percent` | US-DES5-014 |
| 01-ccg/modules/annex_DE.md Collective agreements and prevailing wage | `de.prevailing_wage.threshold.alteration` | US-DES5-015 |
| 01-ccg/modules/annex_DE.md Collective agreements and prevailing wage | `de.prevailing_wage.threshold.new_construction` | US-DES5-015 |
| 01-ccg/modules/annex_DE.md Payroll data protection and records | `de.breach.notice_days` | US-DES5-020 |
| 01-ccg/modules/annex_DE.md Payroll data protection and records | `de.records.retention_years` | US-DES5-002 |
| 01-ccg/modules/annex_DE.md Live legal change | `de.live.hb13_hs2.status` | US-DES5-018 |
| 01-ccg/modules/annex_DE.md Worked examples | `de.oracle.guide.example1.withholding_weekly` | US-DES5-006 |
| 01-ccg/modules/annex_DE.md Worked examples | `de.oracle.guide.example2.supplemental` | US-DES5-006 |
| 01-ccg/modules/annex_FL.md Employment and labour code | `fl.everify.employer_threshold` | US-FLS5-010 |
| 01-ccg/modules/annex_FL.md Employment and labour code | `fl.local_mandates.preempted` | US-FLS5-009 |
| 01-ccg/modules/annex_FL.md Employment and labour code | `fl.manual_labor.legal_day_hours` | US-FLS5-027 |
| 01-ccg/modules/annex_FL.md Employment and labour code | `fl.minwage.hourly` | US-FLS5-001 |
| 01-ccg/modules/annex_FL.md Employment and labour code | `fl.minwage.pre_suit_notice_days` | US-FLS5-002 |
| 01-ccg/modules/annex_FL.md Employment and labour code | `fl.minwage.tip_credit.max` | US-FLS5-001 |
| 01-ccg/modules/annex_FL.md Employment and labour code | `fl.minwage.tipped.cash_wage` | US-FLS5-001 |
| 01-ccg/modules/annex_FL.md State income tax withholding | `fl.pit.exists` | US-FL-001 |
| 01-ccg/modules/annex_FL.md Social insurance (unemployment, disability, paid leave, levies) | `fl.sdi_pfml.exists` | US-FLP52-001 |
| 01-ccg/modules/annex_FL.md Social insurance (unemployment, disability, paid leave, levies) | `fl.sui.employee.rate` | US-FLS5-004 |
| 01-ccg/modules/annex_FL.md Social insurance (unemployment, disability, paid leave, levies) | `fl.sui.employer.rate.max` | US-FLS5-018 |
| 01-ccg/modules/annex_FL.md Social insurance (unemployment, disability, paid leave, levies) | `fl.sui.employer.rate.min` | US-FLS5-018 |
| 01-ccg/modules/annex_FL.md Social insurance (unemployment, disability, paid leave, levies) | `fl.sui.liability_threshold.quarterly_wages` | US-FLS5-020 |
| 01-ccg/modules/annex_FL.md Social insurance (unemployment, disability, paid leave, levies) | `fl.sui.new_employer.rate` | US-FLS5-004 |
| 01-ccg/modules/annex_FL.md Social insurance (unemployment, disability, paid leave, levies) | `fl.sui.rounding` | US-FLS5-004 |
| 01-ccg/modules/annex_FL.md Social insurance (unemployment, disability, paid leave, levies) | `fl.sui.wage_base` | US-FLS5-003 |
| 01-ccg/modules/annex_FL.md Pay statement | `fl.payslip.general_statute.exists` | US-FLL-002 |
| 01-ccg/modules/annex_FL.md Statutory reporting | `fl.newhire.nonemployee_threshold` | US-FLS5-008 |
| 01-ccg/modules/annex_FL.md Statutory reporting | `fl.newhire.report_days` | US-FLS5-008 |
| 01-ccg/modules/annex_FL.md Statutory reporting | `fl.report.sui.efile_threshold_employees` | US-FLS5-006 |
| 01-ccg/modules/annex_FL.md Statutory reporting | `fl.report.sui.flat_file` | US-FLS5-022 |
| 01-ccg/modules/annex_FL.md Statutory reporting | `fl.report.sui.rt6` | US-FLS5-021 |
| 01-ccg/modules/annex_FL.md Statutory reporting | `fl.report.sui.xml` | US-FLS5-023 |
| 01-ccg/modules/annex_FL.md Statutory reporting | `fl.report.sui.xml_required_records` | US-FLS5-023 |
| 01-ccg/modules/annex_FL.md Leave | `fl.leave.domestic_violence.days` | US-FLS5-014 |
| 01-ccg/modules/annex_FL.md Leave | `fl.leave.sick.state_statute.exists` | US-FLS5-009 |
| 01-ccg/modules/annex_FL.md Termination and final pay | `fl.final_pay.state_statute.exists` | US-FLS5-016 |
| 01-ccg/modules/annex_FL.md Benefits in kind and taxable wages | `fl.sui.wages.taxable_items` | US-FLS5-003 |
| 01-ccg/modules/annex_FL.md Deductions and garnishments | `fl.garn.child_support.employer_fee.first` | US-FLS5-013 |
| 01-ccg/modules/annex_FL.md Deductions and garnishments | `fl.garn.child_support.employer_fee.subsequent` | US-FLS5-013 |
| 01-ccg/modules/annex_FL.md Deductions and garnishments | `fl.garn.child_support.remit_days` | US-FLS5-013 |
| 01-ccg/modules/annex_FL.md Deductions and garnishments | `fl.garn.head_of_family.weekly_exempt` | US-FLS5-012 |
| 01-ccg/modules/annex_FL.md Collective agreements and prevailing wage | `fl.prevailing_wage.state_law.exists` | US-FLP52-003 |
| 01-ccg/modules/annex_FL.md Payroll data protection and records | `fl.breach.notice_days` | US-FLS5-017 |
| 01-ccg/modules/annex_FL.md Live legal change | `fl.live.minwage_2026_09_30` | US-FLS5-001 |
| 01-ccg/modules/annex_GA.md Employment and labour code | `ga.local_mandates.preempted` | US-GAS5-017 |
| 01-ccg/modules/annex_GA.md Employment and labour code | `ga.minwage.state.hourly` | US-GAS5-022 |
| 01-ccg/modules/annex_GA.md Employment and labour code | `ga.pay_frequency.rule` | US-GAP9L-001 |
| 01-ccg/modules/annex_GA.md Employment and labour code | `ga.payment.method` | US-GAP9L-001 |
| 01-ccg/modules/annex_GA.md State income tax withholding | `ga.pit.overtime_subtraction.max` | US-GAS5-009 |
| 01-ccg/modules/annex_GA.md State income tax withholding | `ga.pit.rate.flat` | US-GA-001 |
| 01-ccg/modules/annex_GA.md State income tax withholding | `ga.pit.rate.flat` | US-GAS5-009 |
| 01-ccg/modules/annex_GA.md State income tax withholding | `ga.pit.tip_subtraction.max` | US-GAS5-009 |
| 01-ccg/modules/annex_GA.md State income tax withholding | `ga.wh.certificate.form` | US-GAS5-010 |
| 01-ccg/modules/annex_GA.md State income tax withholding | `ga.wh.dependent_allowance` | US-GAS5-001 |
| 01-ccg/modules/annex_GA.md State income tax withholding | `ga.wh.method` | US-GAS5-001 |
| 01-ccg/modules/annex_GA.md State income tax withholding | `ga.wh.std_deduction.mfj` | US-GAS5-001 |
| 01-ccg/modules/annex_GA.md State income tax withholding | `ga.wh.std_deduction.single` | US-GAS5-001 |
| 01-ccg/modules/annex_GA.md State income tax withholding | `ga.wh.supplemental.rate` | US-GAS5-004 |
| 01-ccg/modules/annex_GA.md Non-resident regime and reciprocity | `ga.nonres.threshold` | US-GAS5-004 |
| 01-ccg/modules/annex_GA.md Non-resident regime and reciprocity | `ga.nonres.threshold_amount` | US-GAS5-004 |
| 01-ccg/modules/annex_GA.md Non-resident regime and reciprocity | `ga.nonres.threshold_percent` | US-GAS5-004 |
| 01-ccg/modules/annex_GA.md Social insurance (unemployment, disability, paid leave, levies) | `ga.sui.admin_assessment.rate` | US-GAS5-013 |
| 01-ccg/modules/annex_GA.md Social insurance (unemployment, disability, paid leave, levies) | `ga.sui.coverage` | US-GAS5-006 |
| 01-ccg/modules/annex_GA.md Social insurance (unemployment, disability, paid leave, levies) | `ga.sui.new_employer.rate.contribution` | US-GAS5-013 |
| 01-ccg/modules/annex_GA.md Social insurance (unemployment, disability, paid leave, levies) | `ga.sui.new_employer.rate.total` | US-GAS5-013 |
| 01-ccg/modules/annex_GA.md Social insurance (unemployment, disability, paid leave, levies) | `ga.sui.wage_base` | US-GAW1B-001 |
| 01-ccg/modules/annex_GA.md Statutory reporting | `ga.newhire.report_days` | US-GAS5-012 |
| 01-ccg/modules/annex_GA.md Statutory reporting | `ga.report.annual.g1003` | US-GAS5-003 |
| 01-ccg/modules/annex_GA.md Statutory reporting | `ga.report.sui.dol4n` | US-GAS5-005 |
| 01-ccg/modules/annex_GA.md Statutory reporting | `ga.report.sui.efile_threshold_employees` | US-GAS5-005 |
| 01-ccg/modules/annex_GA.md Statutory reporting | `ga.report.w2.rs_layout` | US-GAS5-011 |
| 01-ccg/modules/annex_GA.md Statutory reporting | `ga.report.wh.payer_status` | US-GAS5-002 |
| 01-ccg/modules/annex_GA.md Statutory reporting | `ga.report.wh.semiweekly_threshold` | US-GAS5-002 |
| 01-ccg/modules/annex_GA.md Leave | `ga.leave.paid.mandate.exists` | US-GAS5-016 |
| 01-ccg/modules/annex_GA.md Termination and final pay | `ga.mass_separation.threshold_workers` | US-GAS5-020 |
| 01-ccg/modules/annex_GA.md Termination and final pay | `ga.sales_rep.commission_due_days` | US-GAS5-007 |
| 01-ccg/modules/annex_GA.md Termination and final pay | `ga.separation_notice.delivery_days` | US-GAS5-007 |
| 01-ccg/modules/annex_GA.md Termination and final pay | `ga.separation_notice.dol800` | US-GAS5-007 |
| 01-ccg/modules/annex_GA.md Benefits in kind and taxable wages | `ga.pit.conformity` | US-GAS5-023 |
| 01-ccg/modules/annex_GA.md Deductions and garnishments | `ga.garn.child_support.per_deduction_fee` | US-GAS5-019 |
| 01-ccg/modules/annex_GA.md Deductions and garnishments | `ga.garn.child_support.setup_fee` | US-GAS5-019 |
| 01-ccg/modules/annex_GA.md Deductions and garnishments | `ga.garn.creditor.max_percent` | US-GAS5-014 |
| 01-ccg/modules/annex_GA.md Collective agreements and prevailing wage | `ga.prevailing_wage.state_law.exists` | US-GAP51-002 |
| 01-ccg/modules/annex_GA.md Payroll data protection and records | `ga.records.dor.retention_years` | US-GAS5-004 |
| 01-ccg/modules/annex_GA.md Payroll data protection and records | `ga.records.gdol.retention_years` | US-GAS5-005 |
| 01-ccg/modules/annex_GA.md Live legal change | `ga.live.gdol_rules_2026` | US-GAS5-021 |
| 01-ccg/modules/annex_GA.md Live legal change | `ga.live.hb1157.status` | US-GAS5-017 |
| 01-ccg/modules/annex_GA.md Live legal change | `ga.live.hb463.status` | US-GAS5-009 |
| 01-ccg/modules/annex_GA.md Worked examples | `ga.oracle.guide.example1.withholding` | US-GAS5-001 |
| 01-ccg/modules/annex_HI.md Employment and labour code | `hi.minwage.exempt.guaranteed_monthly` | US-HIS5-003 |
| 01-ccg/modules/annex_HI.md Employment and labour code | `hi.minwage.hourly` | US-HIS5-001 |
| 01-ccg/modules/annex_HI.md Employment and labour code | `hi.minwage.tip_credit` | US-HIS5-001 |
| 01-ccg/modules/annex_HI.md Employment and labour code | `hi.minwage.tip_credit.min_total_over_minwage` | US-HIS5-001 |
| 01-ccg/modules/annex_HI.md Employment and labour code | `hi.overtime.weekly_threshold_hours` | US-HIS5-003 |
| 01-ccg/modules/annex_HI.md Employment and labour code | `hi.pay_frequency.rule` | US-HIS5-007 |
| 01-ccg/modules/annex_HI.md Employment and labour code | `hi.paycard.rules` | US-HIS5-017 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.pit.ot_deduction.conformed` | US-HIS5-029 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.allowance.annual` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.1.ceiling` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.1.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.2.base_tax` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.2.ceiling` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.2.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.3.base_tax` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.3.ceiling` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.3.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.4.base_tax` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.4.ceiling` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.4.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.5.base_tax` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.5.ceiling` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.5.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.6.base_tax` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.6.ceiling` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.6.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.7.base_tax` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.7.ceiling` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.7.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.8.base_tax` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.married.8.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.1.ceiling` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.1.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.2.base_tax` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.2.ceiling` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.2.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.3.base_tax` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.3.ceiling` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.3.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.4.base_tax` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.4.ceiling` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.4.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.5.base_tax` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.5.ceiling` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.5.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.6.base_tax` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.6.ceiling` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.6.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.7.base_tax` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.7.ceiling` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.7.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.8.base_tax` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.bracket.single.8.rate` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.certificate.form` | US-HIS5-026 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.lump_sum_allowance.annual` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md State income tax withholding | `hi.wh.method` | US-HIS5-004 |
| 01-ccg/modules/annex_HI.md Non-resident regime and reciprocity | `hi.nonres.exempt_days` | US-HIP51-002 |
| 01-ccg/modules/annex_HI.md Social insurance (unemployment, disability, paid leave, levies) | `hi.phc.employee_share.max_percent_of_wages` | US-HIS5-015 |
| 01-ccg/modules/annex_HI.md Social insurance (unemployment, disability, paid leave, levies) | `hi.phc.min_monthly_wage` | US-HIS5-015 |
| 01-ccg/modules/annex_HI.md Social insurance (unemployment, disability, paid leave, levies) | `hi.sui.employee.rate` | US-HIS5-010 |
| 01-ccg/modules/annex_HI.md Social insurance (unemployment, disability, paid leave, levies) | `hi.sui.employer.rate.max` | US-HIP9V-001 |
| 01-ccg/modules/annex_HI.md Social insurance (unemployment, disability, paid leave, levies) | `hi.sui.et_assessment.rate` | US-HIP9V-001 |
| 01-ccg/modules/annex_HI.md Social insurance (unemployment, disability, paid leave, levies) | `hi.sui.new_employer.rate` | US-HIS5-011 |
| 01-ccg/modules/annex_HI.md Social insurance (unemployment, disability, paid leave, levies) | `hi.sui.wage_base` | US-HIS5-011 |
| 01-ccg/modules/annex_HI.md Social insurance (unemployment, disability, paid leave, levies) | `hi.tdi.benefit.weekly_max` | US-HIS5-015 |
| 01-ccg/modules/annex_HI.md Social insurance (unemployment, disability, paid leave, levies) | `hi.tdi.employee.max_rate` | US-HIS5-014 |
| 01-ccg/modules/annex_HI.md Social insurance (unemployment, disability, paid leave, levies) | `hi.tdi.employee.max_weekly_deduction` | US-HIS5-015 |
| 01-ccg/modules/annex_HI.md Social insurance (unemployment, disability, paid leave, levies) | `hi.tdi.max_weekly_wage_base` | US-HIS5-015 |
| 01-ccg/modules/annex_HI.md Pay statement | `hi.payslip.items` | US-HIS5-007 |
| 01-ccg/modules/annex_HI.md Statutory reporting | `hi.newhire.report_days` | US-HIS5-021 |
| 01-ccg/modules/annex_HI.md Statutory reporting | `hi.report.sui.ucb6` | US-HIS5-012 |
| 01-ccg/modules/annex_HI.md Statutory reporting | `hi.report.w2.efile_threshold_forms` | US-HIS5-006 |
| 01-ccg/modules/annex_HI.md Statutory reporting | `hi.report.wh.hw14` | US-HIS5-005 |
| 01-ccg/modules/annex_HI.md Statutory reporting | `hi.report.wh.semiweekly_threshold` | US-HIS5-005 |
| 01-ccg/modules/annex_HI.md Leave | `hi.leave.family.employer_threshold` | US-HIS5-023 |
| 01-ccg/modules/annex_HI.md Leave | `hi.leave.sick.state_mandate.exists` | US-HIS5-024 |
| 01-ccg/modules/annex_HI.md Termination and final pay | `hi.final_pay.rule` | US-HIS5-008 |
| 01-ccg/modules/annex_HI.md Deductions and garnishments | `hi.deductions.rule` | US-HIS5-009 |
| 01-ccg/modules/annex_HI.md Deductions and garnishments | `hi.garn.child_support.employer_fee` | US-HIS5-022 |
| 01-ccg/modules/annex_HI.md Deductions and garnishments | `hi.garn.child_support.remit_working_days` | US-HIS5-022 |
| 01-ccg/modules/annex_HI.md Deductions and garnishments | `hi.garn.creditor.schedule` | US-HIS5-019 |
| 01-ccg/modules/annex_HI.md Collective agreements and prevailing wage | `hi.prevailing_wage.certified_payroll` | US-HIS5-020 |
| 01-ccg/modules/annex_HI.md Collective agreements and prevailing wage | `hi.prevailing_wage.threshold` | US-HIP52-002 |
| 01-ccg/modules/annex_HI.md Live legal change | `hi.live.act24_2026` | US-HIS5-029 |
| 01-ccg/modules/annex_HI.md Worked examples | `hi.oracle.booklet_a.part1.withholding_weekly` | US-HIS5-004 |
| 01-ccg/modules/annex_IA.md Employment and labour code | `ia.late_wages.liquidated_damages_percent_per_day` | US-IAS5-027 |
| 01-ccg/modules/annex_IA.md Employment and labour code | `ia.local_mandates.preempted` | US-IAS5-021 |
| 01-ccg/modules/annex_IA.md Employment and labour code | `ia.minor.under16.school_week_max_hours` | US-IAS5-014 |
| 01-ccg/modules/annex_IA.md Employment and labour code | `ia.minwage.first_90_days.hourly` | US-IAS5-001 |
| 01-ccg/modules/annex_IA.md Employment and labour code | `ia.minwage.hourly` | US-IAS5-001 |
| 01-ccg/modules/annex_IA.md Employment and labour code | `ia.pay_frequency.rule` | US-IAS5-002 |
| 01-ccg/modules/annex_IA.md Employment and labour code | `ia.payment.method` | US-IAS5-002 |
| 01-ccg/modules/annex_IA.md State income tax withholding | `ia.pit.obbba` | US-IAS5-019 |
| 01-ccg/modules/annex_IA.md State income tax withholding | `ia.pit.rate.flat` | US-IAS5-006 |
| 01-ccg/modules/annex_IA.md State income tax withholding | `ia.wh.allowance.per_dependent` | US-IAS5-029 |
| 01-ccg/modules/annex_IA.md State income tax withholding | `ia.wh.deduction.hoh` | US-IAS5-005 |
| 01-ccg/modules/annex_IA.md State income tax withholding | `ia.wh.deduction.mfj_one_earner_qss` | US-IAS5-005 |
| 01-ccg/modules/annex_IA.md State income tax withholding | `ia.wh.deduction.other` | US-IAS5-005 |
| 01-ccg/modules/annex_IA.md State income tax withholding | `ia.wh.exempt.threshold.mfj_hoh_under65` | US-IAS5-016 |
| 01-ccg/modules/annex_IA.md State income tax withholding | `ia.wh.exempt.threshold.single_under65` | US-IAS5-016 |
| 01-ccg/modules/annex_IA.md State income tax withholding | `ia.wh.method` | US-IAS5-005 |
| 01-ccg/modules/annex_IA.md State income tax withholding | `ia.wh.rounding` | US-IAS5-005 |
| 01-ccg/modules/annex_IA.md State income tax withholding | `ia.wh.supplemental.rate` | US-IAS5-016 |
| 01-ccg/modules/annex_IA.md Non-resident regime and reciprocity | `ia.reciprocity.states` | US-IAS5-016 |
| 01-ccg/modules/annex_IA.md Local wage taxes | `ia.local.surtax.withheld` | US-IAS5-029 |
| 01-ccg/modules/annex_IA.md Social insurance (unemployment, disability, paid leave, levies) | `ia.sui.employee.rate` | US-IAS5-024 |
| 01-ccg/modules/annex_IA.md Social insurance (unemployment, disability, paid leave, levies) | `ia.sui.employer.rate.max` | US-IAP9V-001 |
| 01-ccg/modules/annex_IA.md Social insurance (unemployment, disability, paid leave, levies) | `ia.sui.employer.rate.min` | US-IAP9V-001 |
| 01-ccg/modules/annex_IA.md Social insurance (unemployment, disability, paid leave, levies) | `ia.sui.new_employer.construction.rate` | US-IAS5-011 |
| 01-ccg/modules/annex_IA.md Social insurance (unemployment, disability, paid leave, levies) | `ia.sui.new_employer.rate` | US-IAS5-011 |
| 01-ccg/modules/annex_IA.md Social insurance (unemployment, disability, paid leave, levies) | `ia.sui.wage_base` | US-IAS5-009 |
| 01-ccg/modules/annex_IA.md Social insurance (unemployment, disability, paid leave, levies) | `ia.sui.wage_base` | US-IAS5-010 |
| 01-ccg/modules/annex_IA.md Social insurance (unemployment, disability, paid leave, levies) | `ia.sui.wage_base.other_state_credit` | US-IAS5-024 |
| 01-ccg/modules/annex_IA.md Pay statement | `ia.payslip.items` | US-IAS5-027 |
| 01-ccg/modules/annex_IA.md Statutory reporting | `ia.newhire.report_days` | US-IAS5-012 |
| 01-ccg/modules/annex_IA.md Statutory reporting | `ia.report.annual_reconciliation.exists` | US-IAS5-017 |
| 01-ccg/modules/annex_IA.md Statutory reporting | `ia.report.sui.quarterly` | US-IAS5-024 |
| 01-ccg/modules/annex_IA.md Statutory reporting | `ia.report.w2` | US-IAS5-018 |
| 01-ccg/modules/annex_IA.md Statutory reporting | `ia.report.wh.filer_class` | US-IAS5-016 |
| 01-ccg/modules/annex_IA.md Leave | `ia.leave.sick.state_mandate.exists` | US-IAS5-021 |
| 01-ccg/modules/annex_IA.md Termination and final pay | `ia.final_pay.rule` | US-IAS5-003 |
| 01-ccg/modules/annex_IA.md Termination and final pay | `ia.separation.wage_request_response_days` | US-IAS5-026 |
| 01-ccg/modules/annex_IA.md Benefits in kind and taxable wages | `ia.pit.conformity` | US-IAS5-020 |
| 01-ccg/modules/annex_IA.md Deductions and garnishments | `ia.deductions.rule` | US-IAS5-004 |
| 01-ccg/modules/annex_IA.md Deductions and garnishments | `ia.garn.child_support.employer_fee` | US-IAS5-022 |
| 01-ccg/modules/annex_IA.md Deductions and garnishments | `ia.garn.child_support.remit_business_days` | US-IAS5-022 |
| 01-ccg/modules/annex_IA.md Deductions and garnishments | `ia.garn.creditor.annual_cap_schedule` | US-IAS5-013 |
| 01-ccg/modules/annex_IA.md Payroll data protection and records | `ia.breach.notice` | US-IAS5-023 |
| 01-ccg/modules/annex_IA.md Live legal change | `ia.live.hf2212.status` | US-IAS5-028 |
| 01-ccg/modules/annex_IA.md Worked examples | `ia.oracle.formula.example6.withholding` | US-IAS5-005 |
| 01-ccg/modules/annex_ID.md Employment and labour code | `id.local_minwage.preempted` | US-IDS5-001 |
| 01-ccg/modules/annex_ID.md Employment and labour code | `id.minwage.hourly` | US-IDS5-001 |
| 01-ccg/modules/annex_ID.md Employment and labour code | `id.minwage.opportunity_wage` | US-IDS5-001 |
| 01-ccg/modules/annex_ID.md Employment and labour code | `id.minwage.tipped.cash_wage` | US-IDS5-001 |
| 01-ccg/modules/annex_ID.md Employment and labour code | `id.pay_frequency.rule` | US-IDS5-004 |
| 01-ccg/modules/annex_ID.md Employment and labour code | `id.payment.method` | US-IDS5-004 |
| 01-ccg/modules/annex_ID.md State income tax withholding | `id.pit.rate.flat` | US-IDS5-007 |
| 01-ccg/modules/annex_ID.md State income tax withholding | `id.wh.allowance.value` | US-IDS5-008 |
| 01-ccg/modules/annex_ID.md State income tax withholding | `id.wh.certificate` | US-IDS5-013 |
| 01-ccg/modules/annex_ID.md State income tax withholding | `id.wh.method` | US-IDS5-008 |
| 01-ccg/modules/annex_ID.md State income tax withholding | `id.wh.rounding` | US-IDS5-008 |
| 01-ccg/modules/annex_ID.md State income tax withholding | `id.wh.supplemental.rate` | US-IDS5-008 |
| 01-ccg/modules/annex_ID.md State income tax withholding | `id.wh.zero_bracket.married.annual` | US-IDS5-012 |
| 01-ccg/modules/annex_ID.md State income tax withholding | `id.wh.zero_bracket.married.annual` | US-IDS5-011 |
| 01-ccg/modules/annex_ID.md State income tax withholding | `id.wh.zero_bracket.single.annual` | US-IDS5-012 |
| 01-ccg/modules/annex_ID.md State income tax withholding | `id.wh.zero_bracket.single.annual` | US-IDS5-011 |
| 01-ccg/modules/annex_ID.md State income tax withholding | `id.wh.zero_bracket.single.biweekly` | US-IDS5-012 |
| 01-ccg/modules/annex_ID.md State income tax withholding | `id.wh.zero_bracket.single.biweekly` | US-IDS5-011 |
| 01-ccg/modules/annex_ID.md Non-resident regime and reciprocity | `id.nonres.withholding_threshold` | US-IDS5-020 |
| 01-ccg/modules/annex_ID.md Social insurance (unemployment, disability, paid leave, levies) | `id.pfml.exists` | US-IDS5-018 |
| 01-ccg/modules/annex_ID.md Social insurance (unemployment, disability, paid leave, levies) | `id.sui.coverage` | US-IDS5-022 |
| 01-ccg/modules/annex_ID.md Social insurance (unemployment, disability, paid leave, levies) | `id.sui.employer.rate.range` | US-IDP52-004 |
| 01-ccg/modules/annex_ID.md Social insurance (unemployment, disability, paid leave, levies) | `id.sui.new_employer.rate` | US-IDP52-004 |
| 01-ccg/modules/annex_ID.md Social insurance (unemployment, disability, paid leave, levies) | `id.sui.wage_base` | US-IDP7-001 |
| 01-ccg/modules/annex_ID.md Social insurance (unemployment, disability, paid leave, levies) | `id.sui.workforce_development.rate` | US-IDP7-001 |
| 01-ccg/modules/annex_ID.md Pay statement | `id.payslip.required_content` | US-IDS5-025 |
| 01-ccg/modules/annex_ID.md Statutory reporting | `id.newhire.report_days` | US-IDS5-015 |
| 01-ccg/modules/annex_ID.md Statutory reporting | `id.report.annual.form967` | US-IDS5-010 |
| 01-ccg/modules/annex_ID.md Statutory reporting | `id.report.sui.tx20` | US-IDS5-021 |
| 01-ccg/modules/annex_ID.md Statutory reporting | `id.report.wh.form910` | US-IDS5-009 |
| 01-ccg/modules/annex_ID.md Leave | `id.leave.paid_mandate.exists` | US-IDS5-025 |
| 01-ccg/modules/annex_ID.md Termination and final pay | `id.final_pay.max_days` | US-IDS5-005 |
| 01-ccg/modules/annex_ID.md Termination and final pay | `id.final_pay.rule` | US-IDS5-005 |
| 01-ccg/modules/annex_ID.md Benefits in kind and taxable wages | `id.pit.conformity_date` | US-IDS5-019 |
| 01-ccg/modules/annex_ID.md Deductions and garnishments | `id.garn.child_support.cap_percent` | US-IDS5-017 |
| 01-ccg/modules/annex_ID.md Deductions and garnishments | `id.garn.child_support.employer_fee` | US-IDS5-017 |
| 01-ccg/modules/annex_ID.md Deductions and garnishments | `id.garn.creditor.max_percent` | US-IDS5-016 |
| 01-ccg/modules/annex_ID.md Payroll data protection and records | `id.records.retention_years` | US-IDS5-006 |
| 01-ccg/modules/annex_ID.md Live legal change | `id.live.epb00744_2026_07_23` | US-IDS5-011 |
| 01-ccg/modules/annex_ID.md Live legal change | `id.live.h0544_military_leave` | US-IDS5-024 |
| 01-ccg/modules/annex_ID.md Worked examples | `id.oracle.stc.married_weekly.withholding` | US-IDS5-008 |
| 01-ccg/modules/annex_ID.md Worked examples | `id.oracle.stc.single_biweekly.withholding` | US-IDS5-008 |
| 01-ccg/modules/annex_IL.md Employment and labour code | `il.local_minwage.chicago.hourly` | US-ILS5-008 |
| 01-ccg/modules/annex_IL.md Employment and labour code | `il.local_minwage.chicago.tipped` | US-ILS5-008 |
| 01-ccg/modules/annex_IL.md Employment and labour code | `il.local_minwage.cook.hourly` | US-ILS5-009 |
| 01-ccg/modules/annex_IL.md Employment and labour code | `il.local_minwage.cook.tipped` | US-ILS5-009 |
| 01-ccg/modules/annex_IL.md Employment and labour code | `il.minwage.coverage.min_employees` | US-ILS5-026 |
| 01-ccg/modules/annex_IL.md Employment and labour code | `il.minwage.hourly` | US-ILS5-001 |
| 01-ccg/modules/annex_IL.md Employment and labour code | `il.minwage.new_hire_reduction` | US-ILS5-001 |
| 01-ccg/modules/annex_IL.md Employment and labour code | `il.minwage.tipped.cash_wage` | US-ILS5-001 |
| 01-ccg/modules/annex_IL.md Employment and labour code | `il.minwage.youth.hourly` | US-ILS5-001 |
| 01-ccg/modules/annex_IL.md Employment and labour code | `il.overtime.weekly_threshold_hours` | US-ILS5-001 |
| 01-ccg/modules/annex_IL.md Employment and labour code | `il.pay_frequency.rule` | US-ILS5-003 |
| 01-ccg/modules/annex_IL.md Employment and labour code | `il.payment.method` | US-ILS5-005 |
| 01-ccg/modules/annex_IL.md State income tax withholding | `il.pit.rate.flat` | US-ILR3-001 |
| 01-ccg/modules/annex_IL.md State income tax withholding | `il.wh.certificate` | US-ILS5-010 |
| 01-ccg/modules/annex_IL.md State income tax withholding | `il.wh.exemption.line1` | US-ILR3-001 |
| 01-ccg/modules/annex_IL.md State income tax withholding | `il.wh.exemption.line2` | US-ILR3-001 |
| 01-ccg/modules/annex_IL.md State income tax withholding | `il.wh.method` | US-ILR3-001 |
| 01-ccg/modules/annex_IL.md Non-resident regime and reciprocity | `il.nonres.days_threshold` | US-ILS5-014 |
| 01-ccg/modules/annex_IL.md Non-resident regime and reciprocity | `il.reciprocity.states` | US-ILS5-014 |
| 01-ccg/modules/annex_IL.md Local wage taxes | `il.local_wage_tax.exists` | US-ILP52-001 |
| 01-ccg/modules/annex_IL.md Social insurance (unemployment, disability, paid leave, levies) | `il.sdi_pfml.exists` | US-ILP52-003 |
| 01-ccg/modules/annex_IL.md Social insurance (unemployment, disability, paid leave, levies) | `il.sui.employee.rate` | US-ILS5-015 |
| 01-ccg/modules/annex_IL.md Social insurance (unemployment, disability, paid leave, levies) | `il.sui.employer.rate.max` | US-ILS5-015 |
| 01-ccg/modules/annex_IL.md Social insurance (unemployment, disability, paid leave, levies) | `il.sui.employer.rate.min` | US-ILS5-015 |
| 01-ccg/modules/annex_IL.md Social insurance (unemployment, disability, paid leave, levies) | `il.sui.fund_builder.rate` | US-ILS5-015 |
| 01-ccg/modules/annex_IL.md Social insurance (unemployment, disability, paid leave, levies) | `il.sui.new_employer.rate` | US-ILS5-015 |
| 01-ccg/modules/annex_IL.md Social insurance (unemployment, disability, paid leave, levies) | `il.sui.wage_base` | US-ILS5-015 |
| 01-ccg/modules/annex_IL.md Pay statement | `il.payslip.copy_response_days` | US-ILS5-024 |
| 01-ccg/modules/annex_IL.md Pay statement | `il.payslip.rules` | US-ILS5-024 |
| 01-ccg/modules/annex_IL.md Statutory reporting | `il.newhire.report_days` | US-ILS5-018 |
| 01-ccg/modules/annex_IL.md Statutory reporting | `il.report.sui.monthly.employer_threshold` | US-ILS5-017 |
| 01-ccg/modules/annex_IL.md Statutory reporting | `il.report.sui.quarterly` | US-ILS5-016 |
| 01-ccg/modules/annex_IL.md Statutory reporting | `il.report.w2` | US-ILS5-013 |
| 01-ccg/modules/annex_IL.md Statutory reporting | `il.report.wh.deposit` | US-ILS5-011 |
| 01-ccg/modules/annex_IL.md Statutory reporting | `il.report.wh.il941` | US-ILS5-011 |
| 01-ccg/modules/annex_IL.md Statutory reporting | `il.report.wh.semiweekly_threshold` | US-ILS5-011 |
| 01-ccg/modules/annex_IL.md Leave | `il.leave.chicago.accrual` | US-ILS5-020 |
| 01-ccg/modules/annex_IL.md Leave | `il.leave.plawa.accrual` | US-ILS5-019 |
| 01-ccg/modules/annex_IL.md Leave | `il.leave.plawa.cap_hours` | US-ILS5-019 |
| 01-ccg/modules/annex_IL.md Termination and final pay | `il.final_pay.rule` | US-ILS5-023 |
| 01-ccg/modules/annex_IL.md Termination and final pay | `il.final_pay.vacation_payout` | US-ILS5-004 |
| 01-ccg/modules/annex_IL.md Benefits in kind and taxable wages | `il.wh.wages.conformity` | US-ILR3-002 |
| 01-ccg/modules/annex_IL.md Deductions and garnishments | `il.deductions.rule` | US-ILS5-006 |
| 01-ccg/modules/annex_IL.md Deductions and garnishments | `il.garn.child_support.employer_fee_monthly` | US-ILS5-021 |
| 01-ccg/modules/annex_IL.md Deductions and garnishments | `il.garn.creditor.max_percent_gross` | US-ILS5-022 |
| 01-ccg/modules/annex_IL.md Deductions and garnishments | `il.garn.creditor.weekly_floor` | US-ILS5-022 |
| 01-ccg/modules/annex_IL.md Payroll data protection and records | `il.bipa.retention_max_years` | US-ILS5-025 |
| 01-ccg/modules/annex_IL.md Payroll data protection and records | `il.records.paystub.retention_years` | US-ILS5-024 |
| 01-ccg/modules/annex_IL.md Live legal change | `il.live.14c_end` | US-ILS5-002 |
| 01-ccg/modules/annex_IL.md Worked examples | `il.oracle.il700t.example1.withholding` | US-ILR3-001 |
| 01-ccg/modules/annex_IL.md Worked examples | `il.oracle.il700t.example2.withholding` | US-ILR3-001 |
| 01-ccg/modules/annex_IN.md Employment and labour code | `in.late_wages.liquidated_damages_multiple` | US-INS5-003 |
| 01-ccg/modules/annex_IN.md Employment and labour code | `in.local_mandates.preempted` | US-INS5-002 |
| 01-ccg/modules/annex_IN.md Employment and labour code | `in.minwage.hourly` | US-INS5-001 |
| 01-ccg/modules/annex_IN.md Employment and labour code | `in.minwage.tipped.cash_wage` | US-INS5-001 |
| 01-ccg/modules/annex_IN.md Employment and labour code | `in.overtime.weekly_threshold_hours` | US-INS5-001 |
| 01-ccg/modules/annex_IN.md Employment and labour code | `in.pay_frequency.rule` | US-INS5-003 |
| 01-ccg/modules/annex_IN.md Employment and labour code | `in.payment.method` | US-INS5-003 |
| 01-ccg/modules/annex_IN.md State income tax withholding | `in.pit.rate` | US-INS5-009 |
| 01-ccg/modules/annex_IN.md State income tax withholding | `in.wh.certificate` | US-INS5-021 |
| 01-ccg/modules/annex_IN.md State income tax withholding | `in.wh.exemption.adopted_child` | US-INS5-007 |
| 01-ccg/modules/annex_IN.md State income tax withholding | `in.wh.exemption.dependent` | US-INS5-007 |
| 01-ccg/modules/annex_IN.md State income tax withholding | `in.wh.exemption.personal` | US-INS5-007 |
| 01-ccg/modules/annex_IN.md State income tax withholding | `in.wh.method` | US-INS5-007 |
| 01-ccg/modules/annex_IN.md State income tax withholding | `in.wh.supplemental.rate` | US-INS5-007 |
| 01-ccg/modules/annex_IN.md Non-resident regime and reciprocity | `in.nonres.safe_harbor_days` | US-INS5-007 |
| 01-ccg/modules/annex_IN.md Non-resident regime and reciprocity | `in.reciprocity.states` | US-INS5-012 |
| 01-ccg/modules/annex_IN.md Local wage taxes | `in.local.lit.change_calendar` | US-INS5-008 |
| 01-ccg/modules/annex_IN.md Local wage taxes | `in.local.lit.county_basis` | US-INS5-008 |
| 01-ccg/modules/annex_IN.md Local wage taxes | `in.local.lit.rate.boone` | US-IN-001 |
| 01-ccg/modules/annex_IN.md Local wage taxes | `in.local.lit.rate.boone` | US-INS5-007 |
| 01-ccg/modules/annex_IN.md Local wage taxes | `in.local.lit.rate.marion` | US-IN-001 |
| 01-ccg/modules/annex_IN.md Local wage taxes | `in.local.lit.rate.marion` | US-INS5-007 |
| 01-ccg/modules/annex_IN.md Local wage taxes | `in.local.lit.rate.max` | US-IN-001 |
| 01-ccg/modules/annex_IN.md Local wage taxes | `in.local.lit.rate.max` | US-INS5-007 |
| 01-ccg/modules/annex_IN.md Local wage taxes | `in.local.lit.rate.min` | US-IN-001 |
| 01-ccg/modules/annex_IN.md Local wage taxes | `in.local.lit.rate.min` | US-INS5-007 |
| 01-ccg/modules/annex_IN.md Social insurance (unemployment, disability, paid leave, levies) | `in.sui.employee.rate` | US-INS5-014 |
| 01-ccg/modules/annex_IN.md Social insurance (unemployment, disability, paid leave, levies) | `in.sui.employer.rate.max` | US-INS5-014 |
| 01-ccg/modules/annex_IN.md Social insurance (unemployment, disability, paid leave, levies) | `in.sui.employer.rate.min` | US-INS5-014 |
| 01-ccg/modules/annex_IN.md Social insurance (unemployment, disability, paid leave, levies) | `in.sui.new_employer.rate` | US-INS5-014 |
| 01-ccg/modules/annex_IN.md Social insurance (unemployment, disability, paid leave, levies) | `in.sui.wage_base` | US-INS5-014 |
| 01-ccg/modules/annex_IN.md Pay statement | `in.payslip.items` | US-INS5-001 |
| 01-ccg/modules/annex_IN.md Statutory reporting | `in.newhire.report_days` | US-INS5-016 |
| 01-ccg/modules/annex_IN.md Statutory reporting | `in.report.annual.wh3` | US-INS5-011 |
| 01-ccg/modules/annex_IN.md Statutory reporting | `in.report.sui.quarterly` | US-INS5-014 |
| 01-ccg/modules/annex_IN.md Statutory reporting | `in.report.w2.efile_threshold` | US-INS5-011 |
| 01-ccg/modules/annex_IN.md Statutory reporting | `in.report.wh.wh1` | US-INS5-010 |
| 01-ccg/modules/annex_IN.md Leave | `in.leave.military_family.days` | US-INS5-006 |
| 01-ccg/modules/annex_IN.md Leave | `in.leave.sick.state_mandate.exists` | US-INS5-002 |
| 01-ccg/modules/annex_IN.md Termination and final pay | `in.final_pay.rule` | US-INS5-005 |
| 01-ccg/modules/annex_IN.md Deductions and garnishments | `in.deductions.overpayment_recovery` | US-INS5-004 |
| 01-ccg/modules/annex_IN.md Deductions and garnishments | `in.deductions.wage_assignment` | US-INS5-004 |
| 01-ccg/modules/annex_IN.md Deductions and garnishments | `in.garn.child_support.employer_fee` | US-INS5-017 |
| 01-ccg/modules/annex_IN.md Deductions and garnishments | `in.garn.creditor.max_percent` | US-INS5-017 |
| 01-ccg/modules/annex_IN.md Payroll data protection and records | `in.breach.ag_penalty_max` | US-INS5-018 |
| 01-ccg/modules/annex_IN.md Live legal change | `in.live.dn1_r47` | US-INS5-007 |
| 01-ccg/modules/annex_IN.md Worked examples | `in.oracle.dn1.example.county` | US-INS5-007 |
| 01-ccg/modules/annex_IN.md Worked examples | `in.oracle.dn1.example.state` | US-INS5-007 |
| 01-ccg/modules/annex_KS.md Employment and labour code | `ks.local_mandates.preempted` | US-KSS5-012 |
| 01-ccg/modules/annex_KS.md Employment and labour code | `ks.minwage.hourly` | US-KSS5-008 |
| 01-ccg/modules/annex_KS.md Employment and labour code | `ks.minwage.tipped.cash_wage` | US-KSS5-008 |
| 01-ccg/modules/annex_KS.md Employment and labour code | `ks.overtime.non_flsa.weekly_threshold_hours` | US-KSS5-010 |
| 01-ccg/modules/annex_KS.md Employment and labour code | `ks.pay_frequency.rule` | US-KSS5-013 |
| 01-ccg/modules/annex_KS.md Employment and labour code | `ks.payment.method` | US-KSS5-013 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.pit.bracket.1.rate` | US-KSS5-004 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.pit.bracket.2.rate` | US-KSS5-004 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.pit.bracket.mfj.1.ceiling` | US-KSS5-004 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.pit.bracket.single.1.ceiling` | US-KSS5-004 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.pit.exemption.dependent` | US-KSS5-006 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.pit.exemption.mfj` | US-KSS5-006 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.pit.exemption.single` | US-KSS5-006 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.pit.rate_cut_trigger.2026` | US-KSS5-002 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.pit.rate_cut_trigger.2027` | US-KSS5-003 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.pit.std_deduction.married` | US-KSS5-005 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.pit.std_deduction.single` | US-KSS5-005 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.wh.allowance.weekly.single` | US-KSS5-001 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.wh.certificate` | US-KSS5-025 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.wh.method` | US-KSS5-001 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.wh.rounding` | US-KSS5-001 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.wh.supplemental.rate` | US-KSS5-001 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.wh.table.married.band1_ceiling.annual` | US-KSS5-001 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.wh.table.married.zero_bracket.annual` | US-KSS5-001 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.wh.table.single.band1_ceiling.annual` | US-KSS5-001 |
| 01-ccg/modules/annex_KS.md State income tax withholding | `ks.wh.table.single.zero_bracket.annual` | US-KSS5-001 |
| 01-ccg/modules/annex_KS.md Non-resident regime and reciprocity | `ks.nonres.rules` | US-KSS5-001 |
| 01-ccg/modules/annex_KS.md Local wage taxes | `ks.local_wage_tax.exists` | US-KSP9V-002 |
| 01-ccg/modules/annex_KS.md Social insurance (unemployment, disability, paid leave, levies) | `ks.sui.employee.rate` | US-KSS5-023 |
| 01-ccg/modules/annex_KS.md Social insurance (unemployment, disability, paid leave, levies) | `ks.sui.employer.rate.max` | US-KSS5-023 |
| 01-ccg/modules/annex_KS.md Social insurance (unemployment, disability, paid leave, levies) | `ks.sui.employer.rate.min` | US-KSS5-023 |
| 01-ccg/modules/annex_KS.md Social insurance (unemployment, disability, paid leave, levies) | `ks.sui.government_rated.rate` | US-KSS5-023 |
| 01-ccg/modules/annex_KS.md Social insurance (unemployment, disability, paid leave, levies) | `ks.sui.new_employer.construction.rate` | US-KSS5-029 |
| 01-ccg/modules/annex_KS.md Social insurance (unemployment, disability, paid leave, levies) | `ks.sui.new_employer.rate` | US-KSS5-029 |
| 01-ccg/modules/annex_KS.md Social insurance (unemployment, disability, paid leave, levies) | `ks.sui.wage_base` | US-KSS5-023 |
| 01-ccg/modules/annex_KS.md Social insurance (unemployment, disability, paid leave, levies) | `ks.sui.wage_base.other_state_credit` | US-KSS5-020 |
| 01-ccg/modules/annex_KS.md Pay statement | `ks.payslip.required` | US-KSS5-013 |
| 01-ccg/modules/annex_KS.md Statutory reporting | `ks.newhire.report_business_days` | US-KSS5-019 |
| 01-ccg/modules/annex_KS.md Statutory reporting | `ks.report.annual.kw3` | US-KSS5-001 |
| 01-ccg/modules/annex_KS.md Statutory reporting | `ks.report.sui.quarterly` | US-KSS5-022 |
| 01-ccg/modules/annex_KS.md Statutory reporting | `ks.report.w2.efile_threshold_forms` | US-KSS5-026 |
| 01-ccg/modules/annex_KS.md Statutory reporting | `ks.report.wh.deposit_frequency` | US-KSS5-007 |
| 01-ccg/modules/annex_KS.md Leave | `ks.leave.sick.state_mandate.exists` | US-KSS5-012 |
| 01-ccg/modules/annex_KS.md Termination and final pay | `ks.final_pay.rule` | US-KSS5-014 |
| 01-ccg/modules/annex_KS.md Termination and final pay | `ks.final_wage.deductions` | US-KSS5-016 |
| 01-ccg/modules/annex_KS.md Benefits in kind and taxable wages | `ks.pit.conformity` | US-KSS5-028 |
| 01-ccg/modules/annex_KS.md Deductions and garnishments | `ks.deductions.authorised` | US-KSS5-016 |
| 01-ccg/modules/annex_KS.md Deductions and garnishments | `ks.garn.child_support.cap_percent` | US-KSS5-018 |
| 01-ccg/modules/annex_KS.md Deductions and garnishments | `ks.garn.child_support.fee_monthly_max` | US-KSS5-018 |
| 01-ccg/modules/annex_KS.md Deductions and garnishments | `ks.garn.child_support.fee_per_period` | US-KSS5-018 |
| 01-ccg/modules/annex_KS.md Deductions and garnishments | `ks.garn.creditor.rule` | US-KSS5-017 |
| 01-ccg/modules/annex_KS.md Collective agreements and prevailing wage | `ks.prevailing_wage.state_law.exists` | US-KSP52-002 |
| 01-ccg/modules/annex_KS.md Payroll data protection and records | `ks.records.retention_years` | US-KSS5-011 |
| 01-ccg/modules/annex_KS.md Live legal change | `ks.live.sb471.status` | US-KSS5-027 |
| 01-ccg/modules/annex_KY.md Employment and labour code | `ky.minwage.hourly` | US-KYS5-001 |
| 01-ccg/modules/annex_KY.md Employment and labour code | `ky.overtime.seventh_day_rule` | US-KYS5-003 |
| 01-ccg/modules/annex_KY.md Employment and labour code | `ky.overtime.weekly_threshold_hours` | US-KYS5-002 |
| 01-ccg/modules/annex_KY.md Employment and labour code | `ky.pay_frequency.rule` | US-KYS5-004 |
| 01-ccg/modules/annex_KY.md Employment and labour code | `ky.payment.method` | US-KYS5-006 |
| 01-ccg/modules/annex_KY.md Employment and labour code | `ky.rest_break.paid_minutes_per_4h` | US-KYS5-015 |
| 01-ccg/modules/annex_KY.md Employment and labour code | `ky.tip_pool.rule` | US-KYS5-008 |
| 01-ccg/modules/annex_KY.md Employment and labour code | `ky.tipped.definition` | US-KYS5-021 |
| 01-ccg/modules/annex_KY.md State income tax withholding | `ky.pit.rate.flat` | US-KYS5-009 |
| 01-ccg/modules/annex_KY.md State income tax withholding | `ky.wh.certificate` | US-KYS5-013 |
| 01-ccg/modules/annex_KY.md State income tax withholding | `ky.wh.method` | US-KY-002 |
| 01-ccg/modules/annex_KY.md State income tax withholding | `ky.wh.rounding` | US-KYS5-010 |
| 01-ccg/modules/annex_KY.md State income tax withholding | `ky.wh.std_deduction` | US-KY-002 |
| 01-ccg/modules/annex_KY.md State income tax withholding | `ky.wh.supplemental.method` | US-KY-001 |
| 01-ccg/modules/annex_KY.md Non-resident regime and reciprocity | `ky.reciprocity.states` | US-KY-001 |
| 01-ccg/modules/annex_KY.md Local wage taxes | `ky.local.basis` | US-KYS5-024 |
| 01-ccg/modules/annex_KY.md Local wage taxes | `ky.local.lexington.rate` | US-KYS5-024 |
| 01-ccg/modules/annex_KY.md Local wage taxes | `ky.local.louisville.rate.all_wages` | US-KYP9W-001 |
| 01-ccg/modules/annex_KY.md Local wage taxes | `ky.local.louisville.rate.resident_total` | US-KYP9W-001 |
| 01-ccg/modules/annex_KY.md Social insurance (unemployment, disability, paid leave, levies) | `ky.sui.coverage` | US-KYS5-019 |
| 01-ccg/modules/annex_KY.md Social insurance (unemployment, disability, paid leave, levies) | `ky.sui.employer.rate.max` | US-KY-003 |
| 01-ccg/modules/annex_KY.md Social insurance (unemployment, disability, paid leave, levies) | `ky.sui.employer.rate.min` | US-KY-003 |
| 01-ccg/modules/annex_KY.md Social insurance (unemployment, disability, paid leave, levies) | `ky.sui.new_employer.rate` | US-KY-003 |
| 01-ccg/modules/annex_KY.md Social insurance (unemployment, disability, paid leave, levies) | `ky.sui.scuf.rate` | US-KYP7-001 |
| 01-ccg/modules/annex_KY.md Social insurance (unemployment, disability, paid leave, levies) | `ky.sui.wage_base` | US-KY-003 |
| 01-ccg/modules/annex_KY.md Social insurance (unemployment, disability, paid leave, levies) | `ky.sui.wage_base.other_state_credit` | US-KYS5-018 |
| 01-ccg/modules/annex_KY.md Pay statement | `ky.payslip.deduction_statement.employer_threshold` | US-KYP8-001 |
| 01-ccg/modules/annex_KY.md Statutory reporting | `ky.newhire.report_days` | US-KYS5-020 |
| 01-ccg/modules/annex_KY.md Statutory reporting | `ky.report.sui.quarterly` | US-KYS5-019 |
| 01-ccg/modules/annex_KY.md Statutory reporting | `ky.report.w2` | US-KYS5-013 |
| 01-ccg/modules/annex_KY.md Statutory reporting | `ky.report.w2.efile_threshold` | US-KYS5-013 |
| 01-ccg/modules/annex_KY.md Statutory reporting | `ky.report.wh.frequency` | US-KYS5-013 |
| 01-ccg/modules/annex_KY.md Leave | `ky.leave.adoption.weeks` | US-KYS5-016 |
| 01-ccg/modules/annex_KY.md Leave | `ky.leave.voting.hours` | US-KYS5-025 |
| 01-ccg/modules/annex_KY.md Termination and final pay | `ky.final_pay.max_days` | US-KYS5-005 |
| 01-ccg/modules/annex_KY.md Termination and final pay | `ky.final_pay.rule` | US-KYS5-005 |
| 01-ccg/modules/annex_KY.md Benefits in kind and taxable wages | `ky.pit.conformity_date` | US-KYS5-022 |
| 01-ccg/modules/annex_KY.md Benefits in kind and taxable wages | `ky.wh.chart_42a003` | US-KYS5-023 |
| 01-ccg/modules/annex_KY.md Deductions and garnishments | `ky.deductions.rule` | US-KYS5-007 |
| 01-ccg/modules/annex_KY.md Deductions and garnishments | `ky.garn.creditor.rule` | US-KYS5-014 |
| 01-ccg/modules/annex_KY.md Collective agreements and prevailing wage | `ky.prevailing_wage.state_law.exists` | US-KYP52-004 |
| 01-ccg/modules/annex_KY.md Payroll data protection and records | `ky.records.retention_years` | US-KYP8-002 |
| 01-ccg/modules/annex_KY.md Worked examples | `ky.oracle.formula.biweekly_1500.annual` | US-KY-002 |
| 01-ccg/modules/annex_KY.md Worked examples | `ky.oracle.formula.monthly_3270` | US-KY-002 |
| 01-ccg/modules/annex_LA.md Employment and labour code | `la.local_mandates.preempted` | US-LAS5-005 |
| 01-ccg/modules/annex_LA.md Employment and labour code | `la.minwage.state_law.exists` | US-LAS5-006 |
| 01-ccg/modules/annex_LA.md Employment and labour code | `la.pay_frequency.rule` | US-LAS5-004 |
| 01-ccg/modules/annex_LA.md State income tax withholding | `la.pit.rate.flat` | US-LAS5-001 |
| 01-ccg/modules/annex_LA.md State income tax withholding | `la.wh.method` | US-LAS5-001 |
| 01-ccg/modules/annex_LA.md State income tax withholding | `la.wh.std_deduction.joint` | US-LAS5-001 |
| 01-ccg/modules/annex_LA.md State income tax withholding | `la.wh.std_deduction.single` | US-LAS5-001 |
| 01-ccg/modules/annex_LA.md State income tax withholding | `la.wh.supplemental.method` | US-LAP51-002 |
| 01-ccg/modules/annex_LA.md State income tax withholding | `la.wh.who` | US-LAS5-003 |
| 01-ccg/modules/annex_LA.md Non-resident regime and reciprocity | `la.nonres.mobile_workforce.days` | US-LAS5-002 |
| 01-ccg/modules/annex_LA.md Local wage taxes | `la.local_income_tax.exists` | US-LAP52-001 |
| 01-ccg/modules/annex_LA.md Social insurance (unemployment, disability, paid leave, levies) | `la.agency.name` | US-LAS5-004 |
| 01-ccg/modules/annex_LA.md Social insurance (unemployment, disability, paid leave, levies) | `la.sui.employer.rate.max` | US-LAP9V-002 |
| 01-ccg/modules/annex_LA.md Social insurance (unemployment, disability, paid leave, levies) | `la.sui.employer.rate.min` | US-LASUI-001 |
| 01-ccg/modules/annex_LA.md Social insurance (unemployment, disability, paid leave, levies) | `la.sui.new_employer.rate` | US-LAP9V-001 |
| 01-ccg/modules/annex_LA.md Social insurance (unemployment, disability, paid leave, levies) | `la.sui.wage_base` | US-LAP9V-001 |
| 01-ccg/modules/annex_LA.md Statutory reporting | `la.newhire.report_days` | US-LAS5-010 |
| 01-ccg/modules/annex_LA.md Statutory reporting | `la.report.annual.l3` | US-LAS5-009 |
| 01-ccg/modules/annex_LA.md Statutory reporting | `la.report.sui.quarterly` | US-LAS5-007 |
| 01-ccg/modules/annex_LA.md Statutory reporting | `la.report.w2.efile_threshold` | US-LAS5-009 |
| 01-ccg/modules/annex_LA.md Statutory reporting | `la.report.wh.l1` | US-LAS5-003 |
| 01-ccg/modules/annex_LA.md Leave | `la.leave.jury.paid_days` | US-LAS5-013 |
| 01-ccg/modules/annex_LA.md Termination and final pay | `la.final_pay.max_days` | US-LAR3-002 |
| 01-ccg/modules/annex_LA.md Termination and final pay | `la.final_pay.penalty_wages.max_days` | US-LAR3-001 |
| 01-ccg/modules/annex_LA.md Termination and final pay | `la.final_pay.rule` | US-LAR3-002 |
| 01-ccg/modules/annex_LA.md Termination and final pay | `la.test_cost_recovery.working_days` | US-LAS5-004 |
| 01-ccg/modules/annex_LA.md Deductions and garnishments | `la.deductions.fines` | US-LAS5-004 |
| 01-ccg/modules/annex_LA.md Deductions and garnishments | `la.garn.child_support.max_percent` | US-LAS5-012 |
| 01-ccg/modules/annex_LA.md Deductions and garnishments | `la.garn.creditor.exempt_percent` | US-LAS5-012 |
| 01-ccg/modules/annex_LA.md Collective agreements and prevailing wage | `la.cba.fringe_as_wages` | US-LAS5-015 |
| 01-ccg/modules/annex_LA.md Live legal change | `la.live.lac_61_i_1923` | US-LAS5-002 |
| 01-ccg/modules/annex_LA.md Live legal change | `la.live.sb133_2025` | US-LAS5-014 |
| 01-ccg/modules/annex_LA.md Worked examples | `la.oracle.r1306.example1.withholding` | US-LAS5-001 |
| 01-ccg/modules/annex_LA.md Worked examples | `la.oracle.r1306.example2.withholding` | US-LAS5-001 |
| 01-ccg/modules/annex_MA.md Employment and labour code | `ma.minwage.agricultural` | US-MAS5-004 |
| 01-ccg/modules/annex_MA.md Employment and labour code | `ma.minwage.hourly` | US-MAS5-001 |
| 01-ccg/modules/annex_MA.md Employment and labour code | `ma.minwage.service_rate` | US-MAS5-003 |
| 01-ccg/modules/annex_MA.md Employment and labour code | `ma.minwage.tip_credit.max` | US-MAS5-003 |
| 01-ccg/modules/annex_MA.md Employment and labour code | `ma.overtime.weekly_threshold_hours` | US-MAS5-002 |
| 01-ccg/modules/annex_MA.md State income tax withholding | `ma.pit.rate` | US-MAR3-002 |
| 01-ccg/modules/annex_MA.md State income tax withholding | `ma.pit.surtax.rate` | US-MAR3-002 |
| 01-ccg/modules/annex_MA.md State income tax withholding | `ma.pit.surtax.threshold` | US-MAR3-002 |
| 01-ccg/modules/annex_MA.md State income tax withholding | `ma.wh.blind_reduction.weekly` | US-MAS5-013 |
| 01-ccg/modules/annex_MA.md State income tax withholding | `ma.wh.certificate` | US-MAS5-014 |
| 01-ccg/modules/annex_MA.md State income tax withholding | `ma.wh.exemption.annual` | US-MAS5-013 |
| 01-ccg/modules/annex_MA.md State income tax withholding | `ma.wh.exemption.weekly` | US-MAS5-013 |
| 01-ccg/modules/annex_MA.md State income tax withholding | `ma.wh.fica_retirement_deduction.annual_max` | US-MAS5-013 |
| 01-ccg/modules/annex_MA.md State income tax withholding | `ma.wh.hoh_reduction.weekly` | US-MAS5-013 |
| 01-ccg/modules/annex_MA.md State income tax withholding | `ma.wh.method` | US-MAS5-013 |
| 01-ccg/modules/annex_MA.md State income tax withholding | `ma.wh.rounding` | US-MAS5-023 |
| 01-ccg/modules/annex_MA.md State income tax withholding | `ma.wh.student_box_d.income_max` | US-MAS5-014 |
| 01-ccg/modules/annex_MA.md State income tax withholding | `ma.wh.supplemental.rate` | US-MAR3-002 |
| 01-ccg/modules/annex_MA.md State income tax withholding | `ma.wh.supplemental.rule` | US-MAP51-003 |
| 01-ccg/modules/annex_MA.md Non-resident regime and reciprocity | `ma.nonres.rules` | US-MAS5-013 |
| 01-ccg/modules/annex_MA.md Local wage taxes | `ma.local_wage_tax.exists` | US-MAR3-002 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.emac.rate.year4` | US-MAS5-021 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.emac.rate.year5` | US-MAS5-021 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.emac.rate.year6_plus` | US-MAS5-021 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.pfml.benefit.weekly_max` | US-MAS5-025 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.pfml.employee.max_total.25_plus` | US-MAS5-012 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.pfml.family.rate` | US-MAS5-012 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.pfml.medical.rate` | US-MAS5-012 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.pfml.rate.total.25_plus` | US-MAS5-012 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.pfml.rate.total.under_25` | US-MAS5-012 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.pfml.split.decision` | US-MAS5-012 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.sui.coverage` | US-MAS5-022 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.sui.covid_recovery.rate.max` | US-MAS5-020 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.sui.covid_recovery.rate.min` | US-MAS5-020 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.sui.employer.rate.max` | US-MAS5-020 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.sui.employer.rate.min` | US-MAS5-020 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.sui.new_employer.construction.rate` | US-MAS5-022 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.sui.new_employer.rate` | US-MAS5-022 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.sui.rate_schedule.in_force` | US-MAB5-001 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.sui.rate_schedule.selection` | US-MAB5-001 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.sui.rate_schedule.table` | US-MAB5-001 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.sui.wage_base` | US-MAS5-020 |
| 01-ccg/modules/annex_MA.md Social insurance (unemployment, disability, paid leave, levies) | `ma.wtf.rate` | US-MAP7-001 |
| 01-ccg/modules/annex_MA.md Pay statement | `ma.payslip.items` | US-MAS5-005 |
| 01-ccg/modules/annex_MA.md Statutory reporting | `ma.newhire.report_days` | US-MAS5-016 |
| 01-ccg/modules/annex_MA.md Statutory reporting | `ma.report.sui.quarterly` | US-MAS5-018 |
| 01-ccg/modules/annex_MA.md Statutory reporting | `ma.report.w2` | US-MAS5-015 |
| 01-ccg/modules/annex_MA.md Statutory reporting | `ma.report.w2.efile_threshold` | US-MAS5-015 |
| 01-ccg/modules/annex_MA.md Statutory reporting | `ma.report.wh.frequency` | US-MAS5-013 |
| 01-ccg/modules/annex_MA.md Leave | `ma.leave.sick.cap_hours` | US-MAS5-006 |
| 01-ccg/modules/annex_MA.md Leave | `ma.leave.sick.employer_threshold_paid` | US-MAS5-006 |
| 01-ccg/modules/annex_MA.md Leave | `ma.leave.sick.payout_on_separation` | US-MAS5-006 |
| 01-ccg/modules/annex_MA.md Termination and final pay | `ma.final_pay.rule` | US-MAP51-008 |
| 01-ccg/modules/annex_MA.md Benefits in kind and taxable wages | `ma.pit.irc_decoupling` | US-MAS5-026 |
| 01-ccg/modules/annex_MA.md Deductions and garnishments | `ma.garn.creditor.exempt_rule` | US-MAS5-009 |
| 01-ccg/modules/annex_MA.md Deductions and garnishments | `ma.garn.creditor.weekly_exempt_floor` | US-MAS5-009 |
| 01-ccg/modules/annex_MA.md Collective agreements and prevailing wage | `ma.prevailing_wage.certified_payroll` | US-MAS5-007 |
| 01-ccg/modules/annex_MA.md Collective agreements and prevailing wage | `ma.prevailing_wage.rule` | US-MAP51-009 |
| 01-ccg/modules/annex_MA.md Payroll data protection and records | `ma.records.retention_years` | US-MAS5-005 |
| 01-ccg/modules/annex_MA.md Live legal change | `ma.live.chapter_101_2026` | US-MAS5-026 |


## Units annex_FED, annex_MULTI, annex_AK, annex_AL, annex_AR, annex_AZ, annex_CA, annex_CO, annex_CT (builder FED–CT, round 1, 2026-11-02)

Artifact: CCG | Country: US | Round: 1 | Brief: `_prompts/ccg-build-brief.md`
Manifest: `_pipeline/build-manifest.json` (USD, minor units 2; tier overall T4, per-domain tiers read; languages en, payslip English; package 1.0; mandate sealed 2026-11-02).
Inputs: `_research/CCG-annex_{JUR}-research-pack.md` + `_research/CCG-annex_{JUR}-facts.json` for the 9 units (907 facts, 103 unresolved of which 7 blocking); all 9 facts files validate against `facts.schema.json` (validate_contract.py: PASS each). `legal-basis-register.csv` read-only (Sources tables only).
Outputs: `01-ccg/annexes/annex_{FED,MULTI,AK,AL,AR,AZ,CA,CO,CT}.md` (2,584 lines). Generator, hand text and self-checks: `01-ccg/_scratch/annex-FED-CT/` (`build_annexes.py`, `content.py` = hand-written text with `{{key}}` placeholders, `overrides.py`, `c46scan.py`, `gen_requests.py`). Rebuild: `python build_annexes.py` then `python c46scan.py` then `python gen_requests.py`.

### Precedent inspection (L1)
`shared/REFERENCE_CCG_Bulgaria.docx` opened with python-docx: Heading 1 = 14 (Version Control + modules), Heading 2 = 84, Heading 3 = 210 (template questions), Heading 4 = 2; 3 tables; 1 section; footer "CONFIDENTIAL – Mercans |". The annexes carry no template questions (they belong to m01–m13), so each annex is H1 = annex, H2 = `{JUR}.n` sections; the assembler nests them under an annex H1.

### Annex structure (all 9)
Intro (scope, how to read, tier classification from the manifest) · `{JUR}.1` labour · `.2` income-tax withholding (method pseudo-code + bracket tables) · `.2b` non-resident regime and reciprocity with the **C31 resident / non-resident matrix** (FED, AL, AR, AZ, CA, CO, CT; AK: no income tax, points to FED.2b) · `.2c` local wage taxes · `.3` UI/SDI/PFML/levies · `.4` pay statement · `.5` reporting · `.6` leave · `.7` termination · `.8` taxable wages / benefits in kind · `.9` deductions / garnishments · `.10` prevailing wage · `.11` indexation · `.12` data protection / records · `.13` live change · `.14` authority worked examples · `.15` special populations · `.16` language · `.S` sources (register instrument / article / authority; register ids stay in this log). MULTI is laid out as State-pivot tables (resident-out-of-state rule + credit level, reciprocity, non-resident thresholds, convenience rules, UI other-State credit, PFML coverage test) with gaps written in the cell of the State they concern.

### Fact bindings
- 907 of 907 facts written as `[[FACT:key=value]]` (one table row per fact and period; 1,316 tags in total incl. hand text and qualification notes). Generator check: every facts key present in its annex (no MISSING keys). Full section → key → register_id table: `_pipeline/CCG-bindings-annex_FED-CT.csv` (907 rows).
- Hand-written text uses placeholders resolved from the facts files only; prose from the packs was **not** copied (stale after Synthesis C/D in places, e.g. AZ minimum wage, and full of unkeyed figures). Qualification notes are the fact record's own note, cleaned of pipeline wording; numbers in them are tagged to the row's key or to a unique distinctive match in the unit; unkeyed phase-out / threshold figures were removed from notes and replaced by gaps (AL standard deduction; CT tip credits; CO surcharges).
- Cross-annex tags: MULTI keys are cited from FED/AK; FED keys from CO; `ca.sui.max_per_employee` from the WTC facts file.

### Self-checks run
- C38 (tables recompute): FED STANDARD schedules MFJ / Single / HoH cumulative-tax column recomputed from floors and rates — all 8 rows OK each; AR subtraction column recomputed from ceilings and rates — OK. Worked examples computed by script (`content.py` example_al / example_ar / example_ca, half-up to the cent, assert = published value): AL booklet example 29.59 weekly, AR DFA example 36.50 monthly, CA DE 44 example F 7.17 monthly — all reproduce. CT oracle (IP 2026(1) Ex. 8–10) not reproducible: tables not keyed (blocking gap). FED Pub. 15-T examples recorded as oracle values (wage-bracket table and tribal table not keyed); percentage-method reproduction belongs to m12.
- C46 (shared `consistency_checks.py` functions applied to the markdown): 1,316 tags, 0 key/value mismatches. 23 "unbound" hits remain, all statute/section numbers that coincide with a fact value elsewhere in the build (e.g. "8 AAC 15.160" vs `co.minwage.hourly` 15.16; "31-254(b)"; "IAC 871"; "C.R.S. 8-13.3-…"; "Act 2026-604" in fact-record text and the key-derived label "Live act 2026 604 status") — checker false positives, not values. **Checker limitation:** C46 keeps one value per key (last file wins), so the 44 tags of multi-period keys (e.g. `ak.minwage.hourly` 13 / 14 / 15, `co.sui.wage_base` 2026 / 2027) will read as mismatches although each equals its own period's fact; needs a per-period comparison in the checker (route to the pipeline owner).
- C29 lint over every line (TODO, TBD, FIXME, XXX, [CHECK], [?], placeholder, to be confirmed / verified) and pipeline-wording lint (Stage, Synthesis, G-*, tier-B/C, MANUAL, PENDING, Python, register row, browser pass, VPN, fan-out): 0 hits outside fact values. Note: `fed.ssn.truncation.format` = "XXX-XX-1234" is a fact value; after Release strips the tag a naive C29 lint will hit it (false positive).
- C70 wording: no "not obtained / could not be obtained / not retrievable / was not available" phrasing in the annexes (gaps use RESEARCH-GAP markers + requests, not `[[GAP:]]`).

### Scope decisions
| Item | Verdict | Basis |
|---|---|---|
| Independent contractors / 1099-NEC | out of scope (matrix row "Contractor pay") | manifest `_scope`, MANDATE owner instruction 2026-10-29 |
| P.L. 119-21 tips / overtime deductions (FED), AL Act 2026-604 overtime deduction | assessment level only; reporting duty; never a payroll deduction | `fed.plaw119_21.*` `_level`, `al.pit.overtime_premium_deduction.max` note, journal trap |
| CO federal overtime deduction | not allowed in CO withholding | `co.wh.obbba_overtime_deduction.allowed` |
| CT engine method (TPG-211 rules vs DRS tables) | owner decision, recorded as decision record in CT.2; both blocked by the tables gap | journal trap "CT tables vs rules open"; `ct.wh.method` |
| AR 3.7 % formula start date | not modelled; blocking gap | `ar.wh.formula.switch_date` unresolved |
| Equity income (all matrices) | federal classification unkeyed → blocking gap in FED.2b; State matrices point to it | no equity fact in any facts file (searched CCG, WTC, m04, m06) |
| Pay-statement reach | work-location State; CA per *Ward* | `multi.payslip.reach.default`, `multi.ca.ward.rule` |

### Deviations
- Output folder `01-ccg/annexes/` (same as builders MD–NV and NY–WY). Builder DC–MA wrote to `01-ccg/modules/`; the two folders must be reconciled before assembly (orchestrator).
- Pack "Open questions" not reproduced: every `unresolved[]` item is a RESEARCH-GAP marker at its section (MULTI: inside the State's pivot cell).
- Sections without facts and without a rule in the research carry "No {State}-specific rule for this domain is recorded in the research." instead of an empty heading.

### Open items (RESEARCH-GAP markers → `_research/CCG-research-request.json`, appended RQ-402 … RQ-516, 115 items, file re-validated PASS)
| Unit | Blocking | Non-blocking | Blocking items (RQ) |
|---|---|---|---|
| FED | 1 (shown in 2 matrix cells) | 9 | equity withholding treatment (RQ-505) |
| MULTI | 0 | 38 | — |
| AK | 0 | 9 | — |
| AL | 1 | 7 | local occupational-tax census (RQ-458); major: standard-deduction phase-out steps (RQ-506) |
| AR | 1 | 10 | 3.7 % formula switch date (RQ-463) |
| AZ | 0 | 8 | — |
| CA | 2 | 11 | local minimum wages (RQ-478); fast-food / health-care minimums (RQ-479); major: married/HoH per-band rates (RQ-508) |
| CO | 2 | 7 | FAMLI 2027 split (RQ-490); other local minimum wages (RQ-491) |
| CT | 1 | 9 | per-period withholding tables (RQ-497); major: TPG-211 Tables C/D/E (RQ-509) |
Totals: 8 blocking requests (9 blocking marker cells), 107 non-blocking requests (incl. 7 special-population threshold requests, one per State).

### Accuracy
- FED ~90 %: authority publications for every value (Pub. 15-T, Pub. 15/15-B/1494, Rev. Proc. 2025-32, EFW2 TY2026); open: equity treatment, 2026 FUTA credit reductions (final after 2026-11-10), 2027 OASDI base re-verification, TY2026 i940 / ACA instructions.
- MULTI ~80 %: routing rules sourced, but 24 States without a UI other-State-credit answer and 8 PFML coverage tests open.
- AK ~88 %, AZ ~85 %, AL ~80 % (locality census blocking), AR ~80 % (formula switch date blocking), CA ~82 % (local and industry minimum wages blocking), CO ~80 % (local minimum wages, FAMLI 2027 blocking), CT ~78 % (withholding tables blocking).
Research-based figures; the remainder closes only with the official documents named in each request, not with more prose.

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

## Units m01_foundational, m02_master_data, m03_gross_to_net, m04_compensation, m05_social_security, m06_tax, m07_deductions (core-module builder m01–m07, round 1, 2026-11-02)

Artifact: CCG | Country: US | Round: 1 | Brief: `_prompts/ccg-build-brief.md`
Manifest: `_pipeline/build-manifest.json` (USD, minor units 2; rounding 0.01; tier overall T4, repeated verbatim in m01 with the by_domain table and the rationale; languages en, payslip English; package 1.0).
Inputs: `_research/CCG-research-pack.md` (one combined core pack; its m01–m07 sections are the per-unit slices, no separate `CCG-{unit}-research-pack.md` exists), `_research/CCG-m01..m07-facts.json`, the annex facts files for keys listed in `_annex_keys_cited` (FED, MULTI, CA, WA, FL, DC, AK) and further annex / m13 keys cited as State examples; `CCG-coverage-facts.json` (18 rows); `00-official-sources/MANDATE.md` (scope, US-OWN decisions; read-only).
Outputs: `01-ccg/modules/m01_foundational.md`, `m02_master_data.md`, `m03_gross_to_net.md`, `m04_compensation.md`, `m05_social_security.md`, `m06_tax.md`, `m07_deductions.md`.
Generator (build source; never hand-edit the .md): `01-ccg/_build-m01-m07/` (`ccglib.py`, `build_m01.py` … `build_m07.py`, `lint.py`, `append_requests.py`, `state/*.state.json`). Worked examples: `01-ccg/_examples/build_examples_m01_m07.py` → `m01_m07_examples.json` (unit-specific name so the m12 builder's `build_examples.py` is not overwritten). Rebuild: run the examples script, then `build_m01.py` … `build_m07.py`, then `lint.py`.

### Precedent inspection (L1)
`shared/REFERENCE_CCG_Bulgaria.docx` opened with `inspect_docx.py` (python-docx): 1,317 paragraphs, 18,276 words, 310 headings (H1 14 = Version Control + 13 modules, H2 84, H3 210, H4 2), 3 tables, portrait 8.5×11 in, C29 clean. Modules built as H1 module / H2 template section / H3 template question **verbatim** from `CCG_TEMPLATE_QUESTIONS.md` (Bulgaria shortens some H3s; the agent contract requires verbatim, followed). Deliverables are H3 headed with the deliverable sentence; m03 steps are H4 (Bulgaria uses H3 for steps; H4 keeps the H3 count 1:1 with template items).
Unit names follow the manifest (`m03_gross_to_net`), not the agent file (`m03_g2n`).

### Structure and H3 coverage
| Unit | H3 | Template items | Extra H3 | Words | Tags |
|---|---|---|---|---|---|
| m01 | 16 | 15 | Tier verdict | 3,144 | 87 |
| m02 | 11 | 11 | – | 2,084 | 67 |
| m03 | 3 | 1 deliverable | on-costs, flow summary | 1,528 | 45 |
| m04 | 22 | 22 | – | 3,376 | 140 |
| m05 | 17 | 17 | – | 2,913 | 159 |
| m06 | 18 | 18 | – (C31 matrix as H2 §6.0) | 3,868 | 290 |
| m07 | 13 | 13 | – | 1,922 | 82 |
All template questions of Modules 1–7 present (C11: 100% for these units).

### Fact bindings
- 1,556 bindings, 717 distinct keys, 384 register ids. Full section → key → register_id → value table: `_pipeline/CCG-bindings-m01-m07.csv`. Every number is a `[[FACT:key=value]]` tag rendered by the generator from the facts file (never typed); rule facts are quoted verbatim inside a tag or cited as `` `key` [register_id] ``; booleans are cited, not tagged (the checker would compare `True` as a string).
- Self-check (`lint.py`, C46 logic of `shared/consistency-checks` over all `_research/*-facts.json`): 0 tag/value mismatches, 0 unbound distinctive fact values, 0 C29 markers, 0 C70 gap phrases.
- Coverage matrix (C40): every row whose `ccg_location` names m01–m07 is written in that module with its treatment and source ids (resident_employee m03/m05/m06; non_resident_employee m06; part_time, apprentices_and_trainees, overtime m04; maternity_paternity_parental m05; work_accident_occupational_disease m05/m07; mid_month_joiner_and_leaver m02/m03; annual_regularisation m05; multiple_employers m03/m05; local_regimes m06; mid_year_rate_change m04/m06; special_pay_cycles m03/m06; accrual_vs_payment m03/m05). Checked mechanically from `state/*.state.json`.
- C31: the resident vs non-resident matrix is the first section of m06 (six income types × two columns).
- Worked examples (C38): m04 proration (labelled configuration choice, non-statutory) and overtime; m06 resident, NRA and bonus examples (Worksheet 1A, FICA, net). All computed by the script from facts by key; half-up to the cent; expressions re-checked by hand (9,931.60 ÷ 52 = 190.99; 34,879.20 × 22% = 7,673.42; 13,473.42 ÷ 52 = 259.10). Scenario amounts chosen so no scenario number equals an unrelated fact value (first choices 1,500 / 10,000 / 6,000 / 25.00 collided and were changed). Calculation cells carry FACT tags; after the release strip they are pure arithmetic.

### Decisions and deviations
- Journal traps applied: SC Act 110 not in 2026 withholding; WI W-166, NE Circular EN, KS KW-100, OH graduated tables used instead of statute (trap table m06 §6.2); MI/AL/GA/IA/DC tips and overtime deductions assessment-only (m04 §4.4, m06); HI has no fact → RESEARCH-GAP; VA 2027 not modelled; DC 2026 method unpublished and UT Pub 14 effective date carried as the facts' unresolved markers; CT tables vs rules stated as a method choice; MA PFML follows DFML for 2026, swap 2027 (decision quoted with both register ids, residual-risk marker); ND booklet example flagged as recorded defect (use the method); MI never read off the 2023 DOL list (m04 §4.6).
- Facts conflicts noted: the m05 facts note says WA PFML 2026 split 29.3/70.7, while annex WA carries 71.43% employee for 2026 and 70.7% for 2027; built from the dated annex key `wa.pfml.employee.share`. `ca.sdi.employee.rate`: the pack's m05 key index names US-CAEDD-004, the annex CA fact carries US-CAP7-002; the fact's id is used. PFML key split per brief: m05 uses `wa.pfml.total.rate` (m05 file); other States use the annex `{st}.pfml.rate.total` keys.
- Numbers taken from a fact's `note` (e.g. AK "fewer than 4 employees", NV "1.5 x over 8 hours", CA learners "first 160 hours", CCPA "30 x") are cited with that fact's register id; they have no key of their own.
- "Section 125" written "IRC sec.125" to avoid a false C46 binding with an AR value 125. The SSN truncation pattern is paraphrased (its literal form contains the C29 token "XXX").
- The ID certificate blocking item (`id.wh.certificate.current_edition`) and CA local minimum wages (`ca.local_minwage.hourly`) belong to annexes ID/CA; the modules cite them as annex open items without repeating the blocking marker.

### Checker limitations to route (not fixable by the builder)
- C46 keeps one value per key (last loaded). 56 tags in m01–m07 carry the correct value of another period of a multi-dated key (e.g. `fed.fica.oasdi.wage_base` 184,500 vs 192,300 for 2027; State minimum wages; `pa.local.philadelphia.*`) and will be reported as mismatches although each equals a dated fact.
- C70's repealed-citation test matches superseded register rows whose `article_or_section` is a generic string ("2026", "Withholding", "Tables", "Contributions"); any paragraph containing those words fails. Register hygiene for agent 2 / QA.

### Open items
New research requests appended to `_research/CCG-research-request.json` (schema PASS, 572 requests in total): RQ-550 … RQ-572 (23).
- Blocking (2 requests, 3 markers, C31 cells in m06 §6.0): RQ-565 `fed.equity.withholding_treatment` (resident and NRA cells), RQ-566 `fed.fit.nra.bik.treatment`.
- Non-blocking (21): RQ-550 pay frequency (AL, FL, MA, MT, NH, PA, SC); RQ-551 payday on a non-working day; RQ-552 common pay dates; RQ-553 53-pay year; RQ-554/555 federal and State holidays; RQ-556 employer number formats; RQ-557 SSN/ITIN format; RQ-558 payroll data protection; RQ-559 federal pre-tax treatment of deferrals / cafeteria / HSA; RQ-560 minimum wage of 9 States; RQ-561 deductions below minimum wage; RQ-562 FICA/FUTA/FIT wage definitions; RQ-563 HI tips/overtime level; RQ-564 statutory bonus; RQ-567 3401(a) definition; RQ-568 missing W-4 / SSN default; RQ-569 employer refund/adjustment procedure; RQ-570 fringe exclusion conditions; RQ-571 CCPA disposable earnings; RQ-572 fringe valuation.
- Already tracked in facts `unresolved[]`, marked in place, no duplicate request: `fl.no_wage_tax`, `wy.no_wage_tax`, `ky.wh.rounding.tax` (m01); `multi.newhire.registration_channel`, `fed.common_paymaster.rule` (m02, m05); `practice.dol_paid_leave_list` (m04); `multi.workers_comp.employee_share`, `multi.pfml.coverage_test.remaining_states`, `multi.sui.other_state_wage_credit.remaining_states`, `fed.futa.credit_reduction.potential_2026`, `ma.pfml.split.effective_date` (m05); `multi.nonresident.la.catch_up_rule`, `dc.oracle.method_2026`, `ut.oracle.pub14.examples.withholding`, `fed.indexation.publication_2027` (m06); `fed.bik.business_mileage.rate`, `fed.iwo.revised_form.state_golive` (m07). All non-blocking.
- Markers in the text: 3 blocking + 53 non-blocking (m01 10, m02 5, m03 1, m04 12, m05 6, m06 8 + 3 blocking, m07 11).

### Accuracy
Research-only evidence through registered official sources (statutes, IRS/SSA/State agency pages and publications); no portal check or real filing: about 85% for the federal content of m01–m07, lower for the State pattern tables, which depend on annex coverage. The units cannot close while RQ-565 / RQ-566 (C31) are open; closing them and the 21 non-blocking requests needs the source-hunter (A.1/A.2 rows), not more building.


## Units m08_leave, m09_termination, m10_reporting, m11_advanced, m12_worked_examples, m13_practices, coverage (core-module builder m08–m13 + coverage, round 1, 2026-11-02)

Artifact: CCG | Country: US | Round: 1 | Brief: `_prompts/ccg-build-brief.md`
Manifest: `_pipeline/build-manifest.json` (USD, minor units 2, rounding 0.01; tier overall T4; payslip and filings in English; mandate sealed 2026-11-02; package 1.0).
Inputs: `_research/CCG-research-pack.md` (combined core pack; sections m08–m13 and Coverage are the unit slices), `_research/CCG-m08_leave … m13_practices-facts.json`, `_research/CCG-coverage-facts.json` (18 rows, all answered), and the annex / WTC / PSL / SIR facts files for the keys listed in `_annex_keys_cited` and for the comparison tables. Nothing researched, no facts file, register, MANDATE or manifest edited.
Outputs (one file per unit): `01-ccg/modules/m08_leave.md`, `m09_termination.md`, `m10_reporting.md`, `m11_advanced.md`, `m12_worked_examples.md`, `m13_practices.md`, `coverage.md` (to be assembled as Module 11 §11.3, after `m11_advanced.md`).
Generators (build source; never hand-edit the .md): `01-ccg/_build/m08_m13/factlib.py` (fact loader, `[[FACT:]]` tag writer, binding and gap recorder, text clean-up), `01-ccg/_build/m08_m13/build_m08_m13.py` (m08–m11, m13, coverage), `01-ccg/_examples/build_examples.py` (m12 complete + the two m09 worked examples in `01-ccg/_examples/out/`), `01-ccg/_build/m08_m13/append_requests.py`. Rebuild order: `python -I 01-ccg/_examples/build_examples.py` then `python -I 01-ccg/_build/m08_m13/build_m08_m13.py`.

### Precedent inspection (L1)
`shared/REFERENCE_CCG_Bulgaria.docx` opened with python-docx: 1,317 paragraphs, 3 tables, styles Heading 1 (14), Heading 2 (84), Heading 3 (210), Heading 4 (2). Module headings `Module N: Title` (H1), `N.x` sections (H2), questions as H3; Bulgaria adds its own H2/H3 beyond the template questions (e.g. 9.4 Severance Compensation Table, 13.1–13.3). The units follow that shape: `# Module N`, `## N.x`, every template question verbatim as `###`. `shared/CCG_TEMPLATE_QUESTIONS.md` read at run time (Modules 8–13: 52 questions and deliverables).

### Structure and H3 coverage
- 52 of 52 template items of Modules 8–13 present as verbatim H3 (mechanical check); 56 H3 in m08–m13 in total (extra: "Special treatments by worker category", "Fringe benefit exclusions (2026)", oracle sections 12.2.1/12.2.2), plus 18 H3 in `coverage.md` (one per population).
- Added sections beyond the template (Bulgaria precedent): 12.2 Oracle Collection, 13.1 Configuration Practices and Known Traps, 11.3 Population Coverage Matrix (`coverage.md`).
- Coverage matrix (C40): all 18 rows written in `coverage.md` with treatment, effects (income tax / social security / reporting), the module that carries the rule and the source register ids. Rows whose `ccg_location` names m08–m13 are also answered inside those modules: maternity_paternity_parental (m08 8.1, Table 8.1.5), termination_and_final_pay and fixed_term_contract (m09 9.1), annual_regularisation, part_time, overtime, employer_type_and_size (m10 10.1/10.5), officers_without_employment_contract, apprentices_and_trainees, non_resident_employee, employer_type_and_size (m11 11.2), mid_year_rate_change (m11 Table 11.1.1, m13 13.1). Rows located only in m02–m07 are carried by the m01–m07 builder (its stanza above).

### Fact bindings
- Full table section → key → value as written → register_id: `_pipeline/CCG-bindings-m08-m13-coverage.csv` (985 rows; 776 distinct keys; 428 distinct register ids; 881 `[[FACT:]]` tags in the seven files).
- Every own fact of the unit facts files is bound (m08 1/1, m09 1/1, m10 3/3, m11 1/1, m12 37/37, m13 16/16), every `_annex_keys_cited` key is bound (34/34), and every coverage `fact_keys` entry is bound (37/37).
- Every tag equals one dated entry of its key in `_research/*-facts.json` (mechanical check: 881/881). Dated keys are written with their dates (C41), e.g. MA PFML maximum weekly benefit 2026 and 2027, Idaho zero bracket before/after 2026-07-23, Philadelphia rates before/after 2026-07-01, DC minimum wage, VA standard deduction 2026/2027.
- Booleans are written in words (C46 compares booleans as strings) and their binding is in the CSV with value True/False.
- Sample rows:

| Location | Claim | key | register_id |
|---|---|---|---|
| m12 §12.1 Scenario A | 2026 single STANDARD row 4: 5,800 + 22% over 57,900 | `fed.fit.standard.single.bracket.4.*` | US-FEDS5-001 |
| m12 §12.1 Scenario C | OASDI base 184,500 (2026), lesser-of rule | `fed.fica.oasdi.wage_base` (ef 2026-01-01) | US-FEDS5-005 |
| m08 Table 8.1.5 | MA PFML maximum weekly benefit 1,230.39 (2026) / 1,284.61 (2027) | `ma.pfml.max_weekly_benefit` | US-MAS5-025 |
| m09 §9.1 | Alabama severance exemption up to 50,000 | `al.wh.severance.exempt_max` | US-ALS5-001 |
| m10 Table 10.1.1 | W-2 due 2027-02-01 | `fed.w2.due_date` | US-FEDS5-007 |
| m13 §13.1 | SC 2026 withholding tables 0/3/6%, Act 110 at return only | `practice.sc.withholding_rates_2026` | US-SCS5-004 |

### Worked examples (C38)
- `build_examples.py` computes every figure from keyed facts with Decimal half-up rounding to the cent (rounding rule stated in m12; Pub. 15-T optional whole-dollar rounding not applied). Federal scenarios: A (resident single biweekly 3,000.00, Texas), B (part-time 24 h at the federal minimum wage), C (high earner crossing the OASDI base and the Additional Medicare threshold: lesser of remaining base or rate × pay, never annualised-then-divided), mandatory 37% supplemental above 1,000,000; m09: redundancy severance 18,000.00 and annual bonus 5,000.00 (optional flat rate).
- Oracle collection: all 37 m12 oracle facts + the 2 federal Pub. 15-T examples listed with register id, how obtained (quoted / re-derived from the published method) and residual. 16 oracles recomputed from keyed inputs (GA, LA ×2, MI, Detroit, MN, OH, NC, SC, ID, KS, HI, MS, RI, CA, AR): 16/16 agree (at the cent, or at the dollar where the State rounds to whole dollars). The others are quoted only, with the reason (scenario inputs not all verified). ND Section 2 booklet figure carried and flagged as a booklet defect, never an expected result; CT shown as the table route with the rules-route divergence pointed to 13.1.
- Release simulation (tags stripped, C38 `check_rows` on every markdown table of the seven files with the facts-file rates loaded): 95 results recomputed, 0 mismatches.

### Traps from the journal respected
SC Act 110 not in 2026 withholding (m12 SC, m13); WI/NE/KS/OH tables ≠ statutory brackets (m13 13.1); MI/AL/GA/IA/HI/DC tips and overtime deductions at assessment only (m13 table); VA 2027 deduction not modelled (m13); DC 2026 method unpublished (gap, m12/m13); UT Pub 14 effective date unknown (gap); CT tables vs rules (m12, m13); MA PFML 2026 per DFML, swap 2027 (m13 + open point); ND booklet example stale (m12: table used); MI never read off the 2023 DOL tables (m13 open point).

### Deviations and decisions
- File names follow the unit names, as the m01–m07 builder did (`m12_worked_examples.md`, not the agent definition's `m12_examples.md`); the coverage unit is `01-ccg/modules/coverage.md` (the modules folder already holds annex files from other builders).
- Owner decisions (third-party filing provider, no ADP integration; payslip in English US-OWN-006; all populations in scope US-OWN-005) are cited in prose only (owner tier cannot be a fact register_id).
- Pipeline-internal wording removed from the text by `factlib.clean()` (no "facts file", "worker", stage or OQ ids outside fact values). One fact value tagged in m13 (`practice.ct.tables_vs_rules`) carries "(CT-OQ-1)" inside the value; it is the fact as recorded.
- "(partial source)" is written after every tag whose register row is partial (`fed.form941.frequency`, `fed.form944.max_liability`, `fed.form940.due`, `fed.futa.deposit_threshold`, `fed.aca.*`).

### Check results and known check limitations (for agent 4 and the orchestrator)
- C29 residual markers: 0 hits in the seven files (an SSN-mask fact value containing "XXX" is paraphrased, not tagged).
- C46 emulation on the seven files: 881 tags, 0 tags without a matching facts entry. The shared `consistency_checks.c46` collapses each key to its LAST value across all facts files, so 24 correct tags of dated keys read as mismatches (`fed.fica.oasdi.wage_base` 184,500 vs the 2027 entry 192,300; `ma.pfml.max_weekly_benefit`; `ct.leave.sick.coverage_threshold_employees`; `ga.pit.rate.flat`; `id.wh.zero_bracket.single.biweekly`; `oh.pit.wh.base_tax.2`; `ms.pit.rate.flat`; `pa.local.philadelphia.*`; `dc.minwage.hourly`; `va.pit.std_deduction.*`; `wa.pfml.total.rate`). The check needs to compare a tag with every dated entry of its key; the text must not drop the dated values. Unbound numbers: 27, all section numbers that equal a fact value (headings and cross-references "12.2", "10.3", "12.2.1"; e.g. `mi.sui.employer.rate.max` = 12.2, `dc.minwage.tipped.cash_wage` = 10.3); the template numbering cannot avoid them.
- Unit convention: US facts store rates in percent units (6.2, not 0.062). `worked_examples_check.load_rates` and `distinctive_forms` assume fractions; on the DOCX, any "Base × Rate" row with a plain "6.2 %" would be flagged kind F. The tables here use Line | Calculation | Result, so no R-row is formed; the issue applies to the other units and to the RSPEC Example Analysis sheets.

### Open items (all non-blocking; RESEARCH-GAP markers in place; requests appended to `_research/CCG-research-request.json`, schema PASS)

| Location (file) | Marker | Request | Blocking |
|---|---|---|---|
| m08 8.1 | FMLA eligibility thresholds | RQ-517 `fed.fmla.eligibility` | no |
| m08 8.1 | EO 13706 contractor sick leave | RQ-518 `fed.eo13706.sick_leave.accrual` | no |
| m08 8.1 | multistate sick-leave coverage | RQ-519 `multi.sick_leave.coverage_threshold` | no |
| m08 Table 8.1.1 | AR, KY, LA, WV without a verified sick-leave rule | RQ-520 `multi.paid_sick_leave.state_census` | no |
| m08 8.1 | employer top-up of State benefits | RQ-521 `fed.pfml.employer_top_up.treatment` | no |
| m08 8.1 | USERRA | RQ-522 `fed.userra.leave_rules` | no |
| m09 Table 9.1.1 | AL, GA, MS final pay | RQ-523 `multi.final_pay.state_census` | no |
| m09 9.1 | vacation payout supplemental status | RQ-524 `fed.vacation_payout.supplemental_status` | no |
| m09 9.2 | back pay / retro classification | RQ-525 `fed.backpay.treatment` | no |
| m10 10.1 | TY2026 940 / 1094-C instructions | RQ-526 `fed.form940.instructions_current` | no |
| m10 10.1 | multistate new-hire registration channel | RQ-527 `multi.newhire.registration_channel` | no |
| m10 10.2 | revised IWO go-live per State | RQ-528 `fed.iwo.revised_form.state_golive` | no |
| m10 10.4 | State software/provider certification | RQ-529 `multi.payroll_software.certification` | no |
| m10 10.5 | TY2027 indexation | RQ-530 `fed.indexation.publication_2027` | no |
| m11 11.1 | aggregate supplemental procedure | RQ-531 `fed.fit.supplemental.aggregate_method` | no |
| m11 11.1 | pay-frequency change | RQ-532 `fed.fit.pay_frequency_change` | no |
| m11 11.2, coverage | common paymaster / successor | RQ-533 `fed.common_paymaster.rule` | no |
| m11 11.2 | equity compensation | RQ-534 `fed.equity.compensation_treatment` | no |
| m11 11.2 | NRA → resident change | RQ-535 `fed.nra.residency_change` | no |
| m11 fringe table | 2026 mileage rate | RQ-536 `fed.bik.business_mileage.rate` | no |
| m13 | off-cycle conventions | RQ-537 `practice.offcycle_payments` | no |
| m13 | commission draws | RQ-538 `practice.commission_draw` | no |
| m13 | non-statutory leave | RQ-539 `practice.non_statutory_leave` | no |
| m13 13.1 | MA PFML split date | RQ-540 `ma.pfml.split.effective_date` | no |
| m13 13.1 | DOL paid-leave compilation | RQ-541 `practice.dol_paid_leave_list` | no |
| m12 12.2.1, m13 13.1 | UT Pub 14 effective date | RQ-542 `ut.oracle.pub14.examples.withholding` | no |
| m12 12.2.1, m13 13.1 | DC 2026 method | RQ-543 `dc.oracle.method_2026` | no |
| coverage work_accident row | employee workers' comp share | RQ-544 `multi.workers_comp.employee_share` | no |
| m12 12.1 | 401(k)/section 125 wage treatment (pre-tax example not computed) | RQ-545 `fed.retirement.401k.wage_treatment` | no |
| m12 12.1 | student-loan payroll obligation | RQ-546 `fed.student_loan.payroll_obligation` | no |
| m12 12.2.1 | NY example 2 rounding | RQ-547 `ny.oracle.nys50t.example2.withholding` | no |
| m12 12.2.1 | KY per-period rounding | RQ-548 `ky.oracle.biweekly_1500.withholding` | no |
| m12 12.2.1 | MD calculator not run | RQ-549 `md.oracle.calculator` | no |

33 request items (RQ-517..RQ-549), 37 marker occurrences (three keys are marked in two or three places), 0 blocking. Exact line locations are in each request's `location`.

### Accuracy
About 85% for the federal content of m08–m13 (registered IRS, SSA, DOL and statute sources; the computed examples reproduce the published method and 16 State oracles agree), about 75–80% for the State comparison tables, which carry only what the annex facts verify (four States without a sick-leave rule, three without a final-pay rule). Not closed by more reading: a portal check or a real filing for the reporting channels, the State calculators (MD, MI) and the pending 2027 publications. The units can close at round 1 only as named limitations: the 33 non-blocking requests above, plus the two C46 check limitations reported for the orchestrator.

## Assembly: US-CCG-001-v1.0.docx (assembler, round 1, 2026-11-02)

Artifact: CCG | Country: US | Round: 1 | Step: final assembly of the 67 units into the DOCX. No unit text, facts file, register, MANDATE or manifest was edited.
Manifest: `_pipeline/build-manifest.json` (code US, package 1.0, issue_date 2027-03-31 which the manifest notes as a planning placeholder, year 2026, USD).
Output: `01-ccg/US-CCG-001-v1.0.docx`, 696,321 bytes, md5 `c0e1d1eb21960f93d1ba83ed3641350f`.
Assembler (build source, re-runnable): `01-ccg/_build/assemble/build_ccg_docx.py`; run `python -I 01-ccg/_build/assemble/build_ccg_docx.py <BASE>`. Pattern taken from `FR-compliance/01-ccg/build_ccg_docx.py` (read-only), extended to protect `[[FACT:]]` tags from inline markdown parsing (one KY tag value contains asterisks), H4 headings, nested bullets, header-row shading and repeat, and the annex part.

### Precedent inspection (L1)
`shared/REFERENCE_CCG_Bulgaria.docx` opened with the toolkit's `inspect_docx.py`: 1 section, portrait 8.5 x 11 in, 310 headings (H1 14 = Version Control + 13 modules, H2 84, H3 210, H4 2), 3 tables, 18,276 words. Its Version Control table has 5 columns (Version, Effective Date, Change Description, Status, Updated By); the assembly uses the same columns.

### Annex folder (task: move the 13 DC-MA annexes only if their generator can be pointed there)
- Done. The 13 files `annex_{DC,DE,FL,GA,HI,IA,ID,IL,IN,KS,KY,LA,MA}.md` were moved from `01-ccg/modules/` to `01-ccg/annexes/`. All 53 annexes now live in `01-ccg/annexes/`; `01-ccg/modules/` holds m01-m13 + coverage only.
- Proof before the move: the generator, run on a scratch copy with its output folder redirected, regenerated all 13 files byte-identical to the files in `modules/`. After repointing, the real generator was run once into `annexes/`: 13/13 byte-identical, and its scratch reports (`report_*.json`, `overrides_applied.json`) unchanged.
- Repointed (path only): `01-ccg/_scratch/annex-DC-MA/build_annexes.py` (`OUT` = `01-ccg/annexes`), `check_c46.py`, `append_requests.py`. `write_log.py` was left as written (it only regenerates the DC-MA stanza above, whose paths `01-ccg/modules/annex_XX.md` now read `01-ccg/annexes/annex_XX.md`).
- `_research/CCG-research-request.json`: the 250 `01-ccg/modules/annex_XX.md` path strings of the DC-MA items rewritten to `01-ccg/annexes/annex_XX.md` (location text only; no item added, removed or reworded); schema research-request PASS after the edit. The docstring of `_scratch/annex-FED-CT/build_annexes.py` ("writes 01-ccg/modules") is stale but harmless: its `OUT` already is `01-ccg/annexes`.

### Document structure (re-verified by reopening the saved file)
- Front matter: title page `United States of America Country Configuration Guide — US-CCG-001 v1.0` (tax year, currency, scope line with contractors out of scope); TOC field on page 2 (`TOC \o "1-2" \h \z \u`; Word reports 1 TOC, filled on the first field update); Version Control (H1, one row: 1.0 | 2027-03-31 | Initial issue | Draft | issued_by from the manifest; release.py rewrites the row to "Issued").
- Unit order (67): m01, m02, m03, m04, m05, m06, m07, m08, m09, m10, m11, coverage (Module 11 section 11.3, no page break), m12, m13; H1 "Jurisdiction Annexes" (one structural sentence, no figure); Annex FED, Annex MULTI; AK AL AR AZ CA CO CT DC DE FL GA HI IA ID IL IN KS KY LA MA MD ME MI MN MO MS MT NC ND NE NH NJ NM NV NY OH OK OR PA RI SC SD TN TX UT VA VT WA WI WV WY.
- Counts: 807 pages (Word `ComputeStatistics`, before the TOC is filled), 193,627 words, 5,412 paragraphs, 909 tables, 1 section, Letter portrait. Headings: H1 69 (TOC, Version Control, 13 modules, annex part, 53 annexes), H2 980, H3 174, H4 7. Formatting: Arial 11 body, H1 14 / H2 12 / H3 11 bold / H4 11 bold italic; tables Arial 9 (8 when 6 or more columns) with a shaded repeating header row; code blocks Consolas 8.5; page break before every H1; footer `US-CCG-001 v1.0 | Mercans Compliance Regulations Team | 2026`.
- Template coverage (C11): all 149 items of `CCG_TEMPLATE_QUESTIONS.md` present as H3 (deliverables written without the "Deliverable:" prefix in m09/m10/m12; m03 cut before "Process:"); 174 H3 in total (extra = coverage rows and added sections).
- Fidelity (mechanical, markdown vs DOCX text): 6,928 `[[FACT:]]` tags in the units = 6,928 in the DOCX, same multiset (3,566 distinct tag strings); 628 "RESEARCH-GAP" occurrences in the units = 628 in the DOCX (611 `⚠️ RESEARCH-GAP` markers + 17 explanatory sentences in the NY-WY annex intros). No markdown syntax left in the text except `#` comments inside pseudo-code blocks.
- `[[FACT:key=value]]` tags kept in the build file: `shared/release/README.md` and `release.py` (GENERIC_RULES) strip them at release (`[[FACT:k=v]]` becomes `v`).

### Facts bound
- 67 CCG facts files, 3,357 facts, 3,221 distinct keys: 3,210 carried by a tag; 92 more tagged keys come from other facts files (FED/WTC/RSPEC/SIR keys cited across units); 0 tags whose key is absent from every facts file.
- The 11 CCG keys without a tag are cited by key: 7 `{st}.no_wage_tax` booleans (m01 table: "none levied" + key + register id); `ia.wh.method` and `va.wh.method` (values contain square brackets, which the tag syntax cannot hold; components tagged); `multi.sit.work_location.rule` (m02 cites the key); `nj.minwage.general.hourly` (m04 binds the same 15.92 through the annex key `nj.minwage.hourly`).

### RESEARCH-GAP totals (markers in place, copied unchanged)
| Unit | Blocking | Non-blocking |
|---|---|---|
| m01 / m02 / m03 / m04 / m05 / m07 | 0 | 10 / 5 / 1 / 12 / 6 / 11 |
| m06 | 3 (C31 cells, 2 requests) | 8 |
| m08 / m09 / m10 / m11 / coverage / m12 / m13 | 0 | 6 / 3 / 5 / 7 / 2 / 7 / 7 (stated non-blocking by their builder) |
| FED | 2 (1 request shown in 2 matrix cells) | 9 |
| MULTI | 0 | 38 |
| AL, AR, CT, DE, FL, HI, ID, KY, ME, MI, MT, NC, NE, NM, NY, OR, RI, SC, TX, UT, VT, WA, WY | 1 each (23) | per annex stanza |
| CA, CO, DC, GA, IL, LA, MA, VA | 2 each (16) | per annex stanza |
| WV | 3 | 7 |
| AK, AZ, IA, IN, KS, MD, MN, MO, MS, ND, NH, NJ, NV, OH, OK, PA, SD, TN, WI | 0 | per annex stanza |
| **Total markers** | **47** | **564** |

Distinct items: 45 blocking, equal to the 45 `severity: blocker` requests in `_research/CCG-research-request.json` (572 requests: 45 blocker, 24 major, 503 minor). Per-annex counts reproduce the FED-CT, DC-MA, MD-NV and NY-WY stanzas exactly. The CCG cannot close while the 45 blocking items are open.

### Checks run on the assembled file
| Check | Result | Note |
|---|---|---|
| Structure (toolkit `inspect_docx.py`, reopened file) | PASS | 1 section, portrait Letter, H1 order as above, TOC field present |
| Office open (shared `release/open_check.ps1`, Word COM read-only, on a copy) | PASS | 1 file, 0 not clean; Word page count 807 |
| C11 template coverage | PASS | 149/149 |
| C29 residual markers (`inspect_docx.py`) | 3 hits, all inside fact values | `fed.ssn.truncation.format` (`XXX-XX-1234`, the IRS truncated-SSN mask, FED annex table 176); `ga.report.sui.dol4n` and `ga.live.gdol_rules_2026` (GDOL "placeholder SSN" rule, GA annex tables 351/358). Not residual markers; kept as the facts record them. Needs a C29 allowance for tag values. The 611 RESEARCH-GAP markers are not C29 hits but mean the artifact is not final. |
| C42 template leakage (`consistency_checks.py`) | PASS | 0 hits |
| C43 version (`consistency_checks.py`) | PASS | package 1.0, 0 problems |
| C46 facts binding (`consistency_checks.py`) | FAIL (checker limitations below) | 6,928 tags, 323 "mismatches", 67 "unbound", binding 99.0% |
| C38 worked examples (`worked_examples_check.py --module all --facts _research`, on a tag-stripped copy that simulates release) | FAIL (checker limitations below) | 152 results recomputed; 12 flagged, 0 real arithmetic errors |
| C70 citations (`content_checks.py --checks C70`) | FAIL (checker limitation + one open convention) | 5,575 "repealed cited" hits; 16 gap statements without `[[GAP:id]]` |
| C47 release crosscheck (informational, tag-stripped copy) | 664 findings | release-stage check; see below |

### Known checker limitations (recorded; correct text not changed to satisfy them)
- **C46, last value per key.** `consistency_checks.c46` keeps one value per key (the last loaded). 322 of the 323 mismatches equal a dated entry of the same key (multi-period keys: `fed.fica.oasdi.wage_base` 184,500 for 2026 vs 192,300 for 2027, State minimum wages, `pa.local.philadelphia.*`, `dc.minwage.hourly`, `wa.pfml.total.rate`, `nm.wc.admin_fee.*`, and others). Needs a period-aware comparison (key + effective_from).
- **C46, bracket substitution.** 1 mismatch: `fed.efw2.records` (FED annex table 170) is written with `(RO)`/`(RS)`/`(RU)`/`(RV)` where the fact has square brackets; the tag syntax cannot hold `]`. Same cause as the untagged `ia.wh.method` / `va.wh.method`. Needs a tag escape or a facts value without brackets.
- **C46, numbers that are not fact claims.** The 67 "unbound" values: 27 are section/table cross-references (`10.3`, `12.2`, `12.2.1`, "Recomputed in 12.2.2") equal to `dc.minwage.tipped.cash_wage` / `mi.sui.employer.rate.max`; 40 are legal-citation numbers (Act 26-214, SB 269, HB 347, KRS 367, 871 IAC, 36 MRSA 5250, C.R.S. 8-13.3, 8 AAC 15.160, Conn. Gen. Stat. 31-254, IRC s.125, Act 2026-604) or schedule/example cells equal to another unit's fact (HI 1.21 TDI multiplier, MA schedule cells, ID unrounded 20.38, GA band 276, KS 512 threshold, MA 4.58 and 2.25, DE bracket slice 1,750.00). None states the other unit's fact (detail in the DC-MA and m08-m13 stanzas).
- **C46, section numbers.** Covered by the previous item: C46 counts section numbers as untagged values.
- **C38, percent units.** US facts store rates in percent (6.2, not 0.062); `worked_examples_check.load_rates` expects fractions, so 9 "kind F" flags (m12 tables 71/74/76: OASDI 6.2%, Medicare 1.45%, supplemental 22%; AL.14 bands 2% and 4%) say "rate not in the facts files" although each rate is a tagged fact.
- **C38, parsing.** 3 flags in Annex AL section AL.14 (tables 226/227) are parsing artefacts, re-done by hand: Band 2 base cell "6,000.00 - 1,000.00 = 5,000.00" read as 6,000 (5,000.00 x 4% = 200.00 is right); Band 3 "32,370.12 - 6,000.00 = 26,370.12" read as 32,370.12 (26,370.12 x 5% = 1,318.506, half-up 1,318.51 is right); the note "5,000+1,830 (...)+3,000+2,000=11,830" cut at the parenthesis (the full sum 11,830 is right). Annual tax 1,538.51 / 52 = 29.59 matches the oracle.
- **C70, generic register strings.** All 5,575 "repealed cited" hits come from superseded register rows whose `article_or_section` is a generic word (US-OR-003 "Withholding", US-NE-003 "2026", US-MDP51-003 "Contributions", US-SC-006 "Tables", US-NJR3-001/-002 "Payroll Tax", US-NJ-002 and US-TXSUI-004 "2026 rates"). Register hygiene for agent 2 / QA (already reported by the m01-m07 builder).
- **C70, `[[GAP:id]]` convention (open, routed).** 16 statements ("not obtained", "was not available") in the ID, IN, MD, MT, NC, NE, NH, NJ, NM, VA and WA annexes are RESEARCH-GAP markers with a research request but without a `[[GAP:id]]` tag, and `_research/gaps.json` does not exist. Changing unit text is not an assembly task; the unit builders, or the orchestrator if it accepts RESEARCH-GAP + research request as equivalent, decide.
- **C47 (release stage, informational).** On the tag-stripped copy: metadata, rsid and customXml findings are removed by `release.py`; 628 "build tags" are the RESEARCH-GAP mentions (release cannot pass while they exist); 22 rework words include the "Draft" status of the Version Control row (release.py rewrites it to "Issued") and bill statuses such as "DRAFT, NOT ENACTED" (content); 6 "stamp dates" are source publication dates ("updated 2026-05-01"); 2 "versions" are the CT Paid Leave File Specification Toolkit v2.1.9 (an external document version, to list under `external_versions` in a future `_release/release_rules.json`).

### Deviations from the agent's stated constants
- 807 pages against the agent's 80-150 for a CCG: the 13 modules follow the template; the excess is the 53 jurisdiction annexes the US mandate requires (federal + multistate + 51).
- Annex heading styles differ by builder: FED-NV annexes use `Annex XX: Name` and `XX.n` sections; NY-WY use `Annex XX - Name` and `1.` to `n.` sections, and their intro sentence names `_research/CCG-annex_XX-facts.json` (pipeline-internal path in deliverable text). Copied as written; harmonising is a unit-text change for the NY-WY builder.
- TOC limited to levels 1-2 to keep it usable (about 1,050 entries); H3 questions stay in the navigation pane.

### Open items
- 45 blocking items (47 markers) and 564 non-blocking markers, all in place and all in `_research/CCG-research-request.json`.
- Shared-check limitations above go to the owner of `shared/` (period-aware C46, tag escape for `]`, percent-unit rates and composite base cells in C38, generic register strings in C70, C29 allowance for the three fact values).

### Accuracy
About 85% for the federal core and the modules, 75-85% per jurisdiction annex (research through registered official sources; no portal check or real filing), as the unit stanzas state. The assembly adds no content and loses none (6,928 tags and 628 gap mentions carried 1:1). The artifact is **not closable** in round 1: 45 blocking research items are open, and C46/C38/C70 report FAIL for the checker limitations recorded here.


## Round 2 rebuild (artifact-builder, 2026-11-02): QA r1 findings routed to the builder + agent 2 R1/R1b facts

Artifact: CCG | Country: US | Round: 2 | Input review: `_qa/CCG-review-r1.json` (findings 39, 42, 43, 49, 51, 52, 57, 58, 63 routed to the builder; 37/38 fixed in place by QA) | Facts: rewritten by agent 2 (`_research/qa-r1-fix/AGENT2-R1.md`, `AGENT2-R1b.md`) | Orchestrator decision: CT engine method = DRS tables.
Output: `01-ccg/US-CCG-001-v1.0.docx` (same path and version), md5 `8966ad5ce76b3a185e6853bd040f93b4` (r1 after the QA in-place fix: `6a3ff6b8a94e1b3f240435a5a23bf75a`), 744,486 bytes, 5,647 paragraphs, 913 tables, 209,730 words, H1 69 / H2 1,049 / H3 174 / H4 7, 1 section, Letter portrait.
No generated unit was hand-edited. Every change is in a generator, its inputs, or the new shared layer below; all 67 units and the DOCX were regenerated.

### Rebuild entry point (re-runnable after any facts / gaps / request change, e.g. the parallel browser worker)
`python 01-ccg/_build/common/rebuild_all.py` runs, in order: `_examples/build_examples_m01_m07.py`, `_build-m01-m07/build_m01..07.py`, `_examples/build_examples.py`, `_build/m08_m13/build_m08_m13.py`, `_scratch/annex-FED-CT/build_annexes.py`, `_scratch/annex-DC-MA/build_examples_annex_DC-MA.py` + `build_annexes.py`, `_research/synthesis-B/_scratch-ccg-build-MD-NV/build_annexes.py`, `_build-annex-NY-WY/build.py`, then `_build/assemble/build_ccg_docx.py`. Per-unit audit records: `01-ccg/_build/common/out/finalize_<unit>.json`.
New shared layer `01-ccg/_build/common/` (imported by every generator): `ccg_common.py` (`finalize()`: prior-year strip, percent tags, `[[GAP:]]` tags, decided gaps, C70 phrase tags, internal-path strip; `normalize_annex()`: one annex skeleton; `alias()`), `percent_tags.json`, `gap_phrase_tags.json`, `gap_text_map.json` (+ `build_gap_text_map.py`), `repoint_aliases.py`, `r2_append_requests.py`, `r2_hook_generators.py`, `r2_ga_level_split.py`, `percent_scan.py`, `c46_period_aware.py`, `alias_audit.py`, `patchlib.py`. One-off idempotent input patches: `_scratch/annex-FED-CT/r2_patch_content.py`, `r2_patch_ct.py`, `_scratch/annex-DC-MA/r2_patch_il.py`, `_build-annex-NY-WY/r2_prior_year.py`.
Robustness added because facts changed during the run (agent 2 R1b): a dated key used without an explicit period defaults to the value in force on 2026-06-30 (`ccglib._pick` identity = value + effective_from; `factlib.REG`; FED-CT `fill`); NY-WY `@gaps` overrides whose gap was closed are reported as obsolete instead of stopping the build (NY `ny.pit.supplemental.local_rates`, TX `tx.report.ui.enhanced_fields_layout`); `xx.local.*` keys sit in the income-tax section of NY-WY; the assembler no longer splits a table cell on a `|` inside a `[[FACT:]]` tag (CT per-period table rows).

### Per fix
| # | Fix | Result |
|---|---|---|
| 1 | Re-point tags through `KEY-ALIAS-MAP.csv` | `repoint_aliases.py`: 176 key strings in 29 generator files; aliases also resolved at load (`CC.alias`). Round-1 units carried 124 tags on 65 old keys; round 2: 0 tags and 0 mentions of any old key (`alias_audit.py`). GA split by level: withholding text bound to `ga.wh.rate` (5.19 to 2026-05-10, 4.99 from 2026-05-11: annex GA summary/notes/example, m06 flat-rate table, m11 Table 11.1.1, coverage row, m12 GA oracle), assessment to `ga.pit.rate.flat`. WA 2028 tax tagged in m01. IN LIT values now percent. New facts fill the gaps they close: m01 1.3 (RQ-553), m01 1.4 (11 federal holidays 2026 + 2027 and DC Emancipation Day, non-business-day rule; RQ-554), m06 6.0 C31 matrix equity resident / NRA and NRA benefits in kind (RQ-505/565/566), m11 stock options (RQ-534), annex FED.2b matrix. m01 FL / WY rows bound to the annex facts `fl.pit.exists` / `wy.pit.exists`. IL-700-T example 1 labelled as the table method; formula result tagged `il.oracle.il700t.example1.automated_method_result` (finding 55). NY local supplemental rates written in NY.2. CT per-period tables (556 band rows) rendered from `ct.wh.table.*`, layout from `ct.wh.tables.columns`. |
| 2 | Untagged percentages | QA's 81 plus the rest found by `percent_scan.py`: 0 distinctive (decimal or 3+ significant digits) untagged percentages equal to a fact remain. Unique same-jurisdiction matches auto-tagged at generation; ambiguous or non-fact ones handled in `percent_tags.json` (tagged to the right key, or reworded without the number when it is a sum, a prior-year figure, a CPI/statutory mechanism or another tax). VT lower withholding brackets were unkeyed numbers in a note: replaced by a gap (RQ-574). 179 integer percentages equal some fact by coincidence (e.g. 75 %, 5 %); not distinctive under the C46 rule. Kept: IN DN1 example county rate 1.00 % (example input; RQ-575 asks to key it). |
| 3 | `[[GAP:id]]` on every RESEARCH-GAP | 600 GAP tags, 564 distinct ids; 0 markers without a tag. Mapping order: marker key (`[[GAPKEY:]]` emitted by ccglib / factlib / FED-CT), key in the text, key in the table row, round-1 text map, open request. C70 phrases outside markers tagged via `gap_phrase_tags.json`. |
| 4 | One annex skeleton | Chosen = the scheme of the majority (FED-CT + DC-MA, 22 of 53 annexes; also QA's target): `# Annex XX: Name`, unnumbered intro, `XX.1` labour, `.2` withholding, `.2b` non-resident/reciprocity, `.2c` local wage taxes, `.3` social insurance, `.4` pay statement, `.5` reporting, `.6` leave, `.7` termination, `.8` BIK/taxable wages, `.9` deductions, `.10` CBA/prevailing wage, `.11` indexation, `.12` data protection/records, `.13` live change, `.14` authority worked examples, `.15` special populations, `.16` language, `.S` sources. Same title per number in all 53; an empty section carries one structural sentence. MD-NV `.0-.2` (scope, layer, configuration decisions) became bold lead-ins of the intro; in-text references re-numbered (e.g. "section ME.7" -> ME.3, "MD.20" -> MD.S). Verified in the DOCX: 53 `Annex XX:` H1, 1,007 annex H2 = 53 x 19. gaps.json / request locations still carry round-1 section numbers. |
| 5 | Internal paths | 0 left (`_research/`, `*-facts.json`, `01-ccg/`, `_pipeline/`, `00-official-sources/`, `.py`): NY-WY intro, ccglib open-item text, MD-NV register path, m01 manifest/MANDATE references. |
| 6 | Prior-year values | Facts in `_history` are not rendered; hand text that referenced them removed (m05 FUTA 2025 credit reductions, m04 P.L. 119-21 TY2025 relief -> 2026 W-2 codes fact, m11 GA 2025 rate, RI/WY tables, OR/VT text, DE note). 8 untagged "2025: n" comparisons stripped from configuration-table notes. |
| 7 | C69 suite | `_validation/suite.json` + `build_suite.py` + `suite/{cases,examples,rules,defects}.json` + `oracle/oracle.py`, wired to build-manifest `oracle` (official_examples, suite_dir `_validation`). 30 cases: 16 State official examples, 11 CCG worked examples (m12 A-D, m09 x2, m06 x3, m04 overtime and proration), 3 parameter cases; 18/18 answered coverage rows mapped. Federal cases re-implemented independently from the facts; State oracle research values come from the CCG calculator (stated in `suite.json._limitations`). |
| 8 | Closed / next-year markers | Markers of closed requests removed, facts written instead (RQ-505/534/553/554/565/566; R1b RQ-118/147/203/272/337/479/497). 9 documented limitations written as "Not yet published (expected ...) [[GAP:id]]" notes (GA, HI, MT, NC, NE, OR, VA, VT, WA). CT engine method: configuration decision (DRS tables up to each table maximum, TPG-211 above it / as reference), CT.2 decision record and CT.14 note updated; RQ-577 raised then closed. |
| 52/57/63 | Paths, contractor sentence, C38 | One contractor sentence everywhere, title page included: "Independent contractors and Form 1099-NEC reporting are out of scope (owner instruction of 2026-10-29) [US-OWN-008]." AL.14 oracle note rewritten as plain expressions. |
| 58 | Non-citable ids (TN/NC/MS) | Not changed this round (they sit inside fact notes); carried to round 3. |

### Research requests written (`_research/CCG-research-request.json`, schema PASS; gaps.json not edited)
RQ-573 `fed.equity.nra.sourcing_period`, RQ-574 `vt.pit.wh.lower_brackets`, RQ-575 `in.oracle.dn1.example.county_rate`, RQ-576 `wa.leave.seattle_psst`, RQ-578 `il.leave.cook.paid_leave.rules_2025`, RQ-579 `nm.labour.minwage.local.santa_fe_county.next_rate`, RQ-580 `tx.report.ui.enhanced_fields.adoption` (all non-blocking). RQ-577 `ct.wh.engine_method` closed by the orchestrator decision. Routed to agent 2: add RQ-573..576 and RQ-578..580 to gaps.json (C70 fails on RQ-576 until then); close RQ-208 (explained by the automated-method fact); close the m01 unresolved `fl/wy.no_wage_tax`; check `oh.records.wage_hour.retention_years` (dated 2027 only, used for 2026).

### Checks on the assembled DOCX
| Check | Result |
|---|---|
| Structure (inspect_docx, reopened) | PASS: 1 section, Letter portrait, TOC field, 13 modules + 53 annexes |
| Word open check (open_check.ps1, on a copy) | PASS, 0 not clean |
| C11 | PASS 96/96 template questions, 174 H3 |
| C29 residual markers | PASS 0 |
| C42 / C43 | PASS / PASS (package 1.0) |
| C46 shared (raw) | FAIL: 7,702 tags, 378 "mismatches", 109 "unbound", binding 98.6 %. The 378 are dated values of multi-period keys (the checker keeps the last value per key). The unbound include digits of `[[GAP:RQ-nnn]]` ids (the checker strips FACT tags only), section / citation / row-label numbers (Act 2026-604, KRS 367, "row 125"), example inputs and computed example results equal to an oracle fact |
| C46 period-aware (`c46_period_aware.py`: key + effective_from, percent-aware, GAP-stripped) | 7,702 tags, 0 keys missing, **0 mismatches**; 280 tags carry a non-2026 dated value, 277 labelled with their period in the row or paragraph, 3 not (OH retention fact dated 2027 only, routed; DC 2034 step); 95 unbound, all non-claims of the kinds above |
| Percent scan (distinctive) | 0 |
| C38 worked examples | PASS: 48 results recomputed, 0 mismatches |
| C70 | FAIL on 1 statement only (RQ-576 not yet in gaps.json); 0 not in register, 0 repealed cited |
| C69 | PASS: 18/18 answered rows with a case (the checker's heading regex finds no "Example n" headings in Module 12; every m12/m09/m06/m04 example is mapped by name) |
| C37 (run_suite.py) | PASS: 30 cases, 62/62 lines |
| validate_contract --all | PASS 76 files |

### Open items
- 24 blocking research items, all in gaps.json and tagged: RQ-021 ME, 029 MI, 138 DC, 146 DC, 156 FL, 165 GA, 189 ID, 202 IL, 227 KY, 236/237 LA, 250 MA, 308 RI, 315 SC, 343 UT, 352 VA, 388/390/391 WV, 398 WY, 458 AL, 463 AR, 478 CA, 491 CO. The CCG cannot close while they are open.
- Non-blocking: 524 open gaps.json items + 1 check_existing_fact (RQ-286) + 6 request-only items, all tagged; 9 "not yet published" notes.
- Finding 58 carried to round 3.

### Accuracy
About 85 % for the federal core and the modules (official sources through the register; the suite reproduces every federal CCG example independently and every State oracle), 75-85 % per jurisdiction annex. Not closable: 24 blocking 2026 items open.


## Round 3 rebuild (artifact-builder, 2026-11-02): QA r2 findings routed to the builder + agent 2 R2 facts

Artifact: CCG | Country: US | Round: 3 (last) | Input review: `_qa/CCG-review-r2.json` (builder findings: C29 markers, 2 X-runs, Version Control date, 2 wrong bindings, untagged numbers, period labels, TN/OH/IA citations, C69, build-log md5; NRA FICA rendering of the agent 2 facts) | Facts: agent 2 R2 (`_research/qa-r2-fix/AGENT2-R2.md`, present before the final rebuild).
Output: `01-ccg/US-CCG-001-v1.0.docx`, **md5 `eedaa839a526763c255ee011a4d8c1a0`**, 722,123 bytes, 5,676 paragraphs, 913 tables, H1 69 (13 modules + 53 annexes) / H2 1,049 / H3 174 / H4 27, 1 section, TOC field present. Built with `CCG_BUILD_DATE=2026-11-02 python 01-ccg/_build/common/rebuild_all.py`. No unit or DOCX was hand-edited. Backups of every changed generator: `01-ccg/_build/common/_r3_backup/`.

### Per finding
| QA r2 finding | Change (generator / input) | Result |
|---|---|---|
| C29: 587 RESEARCH-GAP markers | `ccg_common.neutralize_markers()` (new, in `finalize()` after GAP tagging): each marker becomes "Not configured in this release [[GAP:id]]: <rule as far as established>". `clean_gap_body()` strips request bookkeeping (request keys, "open item", "Closes with / To close / Source that would close it", builder flags, QA notes) and pipeline wording. Limitation notes ("Not yet published (expected ...) [[GAP:id]]") use the same cleaning. No value is added. | 0 RESEARCH-GAP. 572 neutral statements (563 with a GAP tag, 9 without; see open items). 35 "Not yet published" notes |
| C29: X-runs | `text_fixes.json` (new; applied in `finalize()`). FL: "Florida Statutes Title 31 has no SDI/TDI/PFML chapter". KS box 15: "Kansas withholding account number in its published layout (prefix 036, account body, suffix F-01)" | 0 unsanctioned X-runs |
| Version Control 2027-03-31 | `build_ccg_docx.py`: while the manifest `issue_date` `_note` says it is a placeholder, the row carries the build date (`CCG_BUILD_DATE`, else today) with status Draft | `1.0 / 2026-11-02 / Draft` |
| C46 wrong bindings (CT "1 Jan", DE penalty) | FED-CT `autotag()` and DC-MA `autotag()`: a number next to a month name is never tagged. DC-MA no longer binds a round number (fewer than 3 significant digits) to a fact of another section. The safety-net text fixes found 0 hits because the taggers are fixed at source. Audit of all units: 0 tags next to a month. 11 cross-section round-number tags remain, all semantically correct (e.g. the KY flat rate in KY formulas) | CT: "week containing 1 January". DE: "penalties 1,000-5,000 + treble", untagged, on row US-DES5-015 |
| Untagged numbers (MA, "WV" = MA blind / HoH, KS, IL) | `text_fixes.json`: per-period values replaced by the rule (DOR table, or annual ÷ periods). MA domestic meal/lodging and UI amounts and the agricultural UI test replaced by references to 454 CMR 27 and the MA.3 coverage row. IL overtime values removed | 0 of the listed numbers left |
| IN DN1 county rate (RQ-575) | `build_examples_annex_DC-MA.py` uses `in.oracle.dn1.example.county_rate` when that key exists; otherwise it shows the DN1 example input with its GAP tag | rendered with [[GAP:RQ-575]] (no fact key yet) |
| ME / IN 2027 values without year | `text_fixes.json` | "15.70 from 2027-01-01"; "2.9 % from 2027-01-01". Period-aware C46: 0 unlabelled off-year tags |
| TN / OH / IA citations | `src/TN.md`: US-TNR3-001 dropped (US-TNP51-003 and US-TNS5-001 kept); PC 617 no longer cites the MANUAL row US-TNS5-015. `src/OH.md`: the 2026 records/retention and special-population rules cite US-OHS5-005 (2026 poster). IA: "No SDI/TDI/PFML [US-IAP52-004]" becomes "none configured in this release", plus the agent 2 unresolved item | done |
| OH internal path in a fact value | Agent 2 stripped it from `oh.pit.school_district.full_list`. `oh.pit.municipal.rate_table` still carries it, so a regex entry in `text_fixes.json` renders that fact as a paraphrase without the path or counts (the row keeps US-OHB5-002) | 0 internal paths in the DOCX |
| Secondary-only numbers (agent 2 finding 3) | `BODY_OVERRIDES` + `text_fixes.json`: removed from the text the GA 40,000 sales threshold, the HI FEN125 5/7 days, the IN 2026-07-01 date, the KY 1 USD / 150 USD amounts, the MA 4.67 % rate and the NC 6.50 rate | 0 left |
| C31 NRA FICA (m05 table 50) | `ccglib.nra_fica_keys()/nra_fica_text()` render the 5 agent 2 facts (`fed.fica.nra.fjmq_exempt`, `.scope`, `fed.futa.nra.fjmq_exempt`, `fed.fica.nra.other_visas.liable`, `fed.fica.totalization.exemption_rule`) in three places: the m05 5.1 NRA row; a new m06 6.0 matrix row, "Social security (FICA) and FUTA on wages" (resident vs NRA); and a cross-reference in Annex FED.2b | rendered with register ids (US-FEDR2-001, US-FEDS5-016, ...). `agreements_in_force` stays a neutral open item |
| C69: 48 oracle results without a case | `build_examples.py`: Module 12 carries H4 "Worked example n" headings (4 scenarios + 16 re-derivations) that C69 counts. `build_suite.py` adds cases for the DC-MA annex example calculator (re-derivations that agree with the published value), 6 CT DRS-table cases with an independent band lookup in `oracle.py` (`ct_table`), and 1 MI same-example case. Every remaining oracle key carries a recorded reason in `suite.json._oracle_results_without_case` | 48 cases. 80 oracle keys tagged: 34 with a case, 46 with a reason (35 "published result quoted, the CCG prints no re-derivation", 8 non-results, NRA/tribal wage-bracket, ND booklet defect, IL table method). C69 counts 20 CCG examples |
| Build-log md5 | this section | the md5 above is the file on disk after the final rebuild |

### Checks on the final DOCX (`01-ccg/_build/common/run_checks_r3.py`, output `out/checks_r3.json`)
| Check | Result |
|---|---|
| Structure (reopened) | PASS: 13 modules + 53 annexes, TOC field, 1 section. Version Control `1.0 / 2026-11-02 / Draft` |
| Word open (`open_check.ps1` on a copy) | PASS, 0 not clean |
| C11 | PASS 96/96, 174 H3 |
| C29 (v2.12 logic, paragraphs + table cells) | PASS: 0 hard (RESEARCH-GAP counted), 0 bare, 0 X-runs |
| C38 | PASS: 48 recomputed, 0 mismatches |
| C40 | PASS 18/18 |
| C42 / C43 | PASS / PASS (package 1.0) |
| C46 shared | FAIL, a known checker limitation (it keeps the last value per key, misreads the percent form, and counts digits inside GAP tags): 7,628 tags, 375 "mismatches", 101 "unbound" |
| C46 period-aware | 7,628 tags, 0 keys missing, **0 mismatches**, 274 off-year values, **0 unlabelled**. 104 unbound (citation / section / row numbers, example inputs) |
| C69 | PASS: 18 answered rows and 20 CCG examples, all with a case |
| C70 | PASS: 0 not in register, 0 repealed, 0 gap problems |
| C37 | PASS: 48 cases, 80/80 lines, 0 residuals |
| validate_contract --all | PASS |

### Open items (for the QA report / agent 2)
- 9 neutral statements have no GAP tag. They are unresolved items that agent 2 R2 added after gaps.json was written: `fed.fica.totalization.agreements_in_force`, `ga.ui.rate_exclusion.thresholds`, `hi.garn.child_support.remit_working_days`, `ia.pfml.state_program.none`, `in.garn.statute_move.effective_date`, `ky.garn.child_support.iwo_fee_per_payment`, `ky.garn.child_support.lump_sum.reporting_threshold`, `ma.pit.ballot_ip25_18.rate`, `nc.labour.minwage.student_learner.hourly`. C70 passes because none uses a source-gap phrase. Agent 2 should add gaps.json entries; a rebuild then tags them.
- RQ-575 (`in.oracle.dn1.example.county_rate`) still has no fact key. The example shows the DN1 input with its GAP tag.
- The `oh.pit.municipal.rate_table` fact value still carries a local path (agent 2). It is rendered as a paraphrase until then.
- 35 oracle results are quoted only, with no CCG re-derivation; the reasons are recorded in `_validation/suite.json`.
- All 24 former blocking items are documented limitations (agent 2). The CCG writes them as "Not configured in this release" or "Not yet published", with their GAP tags; their detail belongs in the QA report.

### Accuracy
About 85 % for the federal core and modules, and 75-85 % per annex. This round does not close the remaining limitations: authority pages blocked from our access, unpublished 2027 values, and the 389 gaps that agent 2 reports were never searched by URL.


## Round 3b targeted rebuild (artifact-builder, 2026-11-02): QA r3 escalation, option A

Artifact: CCG | Country: US | Round: 3b (targeted rebuild after the round-3 FAIL, by orchestrator decision) | Input review: `_qa/CCG-review-r3.json` (blockers 1-4, minors 9-12 and 14) | Facts: agent 2 R3 (`_research/qa-r3-fix/AGENT2-R3.md`).
Output: `01-ccg/US-CCG-001-v1.0.docx`, **md5 `ade94a2389de07d75b6c6c897f49933a`**, 729,914 bytes, 5,688 paragraphs, 923 tables, H1 69 (13 modules + 53 annexes) / H2 1,049 / H3 174 / H4 27, 1 section, TOC field present. Built with `CCG_BUILD_DATE=2026-11-02 python 01-ccg/_build/common/rebuild_all.py`. No unit and no DOCX was edited by hand. Backups of the changed generators are in `01-ccg/_build/common/_r3b_backup/`. build_m02.py and build_m05.py were edited without a copy there; their prior state is the round-3 working tree.

### Per finding
| QA r3 finding | Change (generator / input) | Result |
|---|---|---|
| Blocker 1, RQ-559 (m03 Step 2) | `build_m03.py`: the GAP is replaced by a table of deduction x base (401(k), 403(b), 457(b), SIMPLE, Section 125 health, dependent care, HSA). The FIT / FICA / FUTA cells are `fed.base.<item>.{fit,fica,futa}`, followed by the rule `fed.retirement.pretax.tax_treatment` and `fed.base.section125.rule` | rendered, [US-FEDS5-029] / [US-FEDS5-008] |
| Blocker 1, RQ-562 (m04 §4.2) | `build_m04.py`: the tips, group-term life, transportation, educational assistance and dependent care rows are rendered from `fed.base.*`. The PFML FUTA cell says "no FUTA exclusion is configured" and cites `fed.wages.general_definition`. A new table gives the statutory definitions (`fed.wages.general_definition`, `fed.fica.wage_definition.exclusions`, `fed.futa.wage_definition.exclusions`). The Trump-account FUTA cell now carries RQ-591 | 0 RQ-562 tags; [US-FEDQ1-002], [US-FEDQ3-002], [US-FEDQ3-003] |
| Blocker 1, RQ-567 (m06 §6.1.1) | `build_m06.py`: definition and exclusions table (`fed.fit.wage_definition`, `.exclusions`) | [US-FEDQ3-001] |
| Blocker 1, RQ-568 (m06 §6.3) | `build_m06.py`: table of the four defaults (`fed.w4.default_no_certificate`, `.pre2020_employee`, `fed.w4.exempt_not_renewed.default`, `fed.ssn.not_issued.w2_rule`) | [US-FEDQ3-004] |
| Blocker 1, RQ-570 (m07 §7.1) | `build_m07.py`: the eligibility column is `fed.bik.<benefit>.conditions` (HSA, health FSA, dependent care, educational assistance, transportation, Trump account). A new FIT / FICA / FUTA table per exclusion comes from `fed.base.*`. The Trump-account FICA/FUTA cells are tagged RQ-591 (agent 2 unresolved item) | [US-FEDS5-008], [US-FEDR3-005] |
| Blocker 1, RQ-572 (m07 §7.2) | `build_m07.py`: valuation table (`fed.bik.valuation.general_rule`, `.taxable_amount`, `fed.bik.vehicle.valuation_methods`, `fed.bik.vehicle.commuting_rule.value_per_one_way` = 1.50, `fed.bik.treated_as_paid`). The BIK withholding answer comes from `fed.bik.withholding.method` and `fed.bik.vehicle.election_not_to_withhold_fit` | [US-FEDS5-008] |
| Blocker 1, RQ-524 / RQ-531 (m09 / m11) | `build_m08_m13.py`: `fed.vacation_payout.supplemental_status` and `fed.fit.supplemental.aggregate_method` are rendered where the gaps were | [US-FEDQ1-002] |
| Blocker 2, RQ-508 (CA.2) | `annex-FED-CT/content.py`: the GAP and the "ceilings carried as one value" paragraph are replaced by a pointer to the tables per status. `overrides.default_section()`: a fact without `_domain` is now placed by key prefix (`gap_section`) instead of section 13. The married and HoH band tables (rate, ceiling, base, N = 1..10) therefore sit in CA.2 | married and HoH tables in CA.2, [US-CAS5-001] |
| Blocker 3, RQ-506 (AL.2) | `annex-FED-CT/content.py`: phase-out rule (`al.wh.std_deduction.phaseout_steps`), a formula block, and a table per status (maximum, start GI, reduction per step, step size, floor GI) | [US-ALS5-001] |
| Blocker 4 (C30) | `text_fixes.json` removes: GA.3 "(secondary source: 0.04-8.10%)" (RQ-163 stays); LA.3 "(secondary source: 7,700 in 2025)"; the KY.9 paragraph on the 1 USD fee and the 150+ threshold (RQ-233/586/587 state the limitation). IN.9: the date is replaced by "effective date: see the open point in this section" (RQ-585). The C30 scan also found IN.13 "municipal LIT from 2028", which rests on the MANUAL row US-INS5-019 ("LEAD ONLY, no number to be used"). It is rewritten without the year | 0 secondary-only figures (scan below) |
| Minor 9 (13 untagged statements) | RQ-581..591 are now in gaps.json (agent 2), so the rebuild tags them. `text_fixes.json` tags GA.1 (RQ-582), the HI.9 table note (RQ-583), TN.13 PC 617 (RQ-329) and the MT/NE/NH summary lines (RQ-065/089/102, post stage). MA.15 meal/lodging is reworded as a reference to 454 CMR 27, because agent 2 reports that no key exists | 0 "not configured" statements without a GAP tag in the DOCX |
| Minor 10 ("not researched") | DE.7: neutral limitation with the new request **RQ-592** `de.termination.separation_notice_warn`. It is appended to `CCG-research-request.json`, and its gaps.json entry is routed to agent 2. LA.12: "Not researched." removed (RQ-244 states it). WV.12: the sentence is removed (RQ-396 states it) | 0 "researched" phrases |
| Minor 11 (pipeline wording) | Fixed in the generators or text_fixes: m02 "open item of annex ID"; the m05 and m07 "research request ..." sentences; m04 "open item of annex CA"; the m02 SSN-paystub key list and DD folder path; KY "open item `ky.wh.rounding.tax`". Fixed in text_fixes: ME "CORRECTS ..."; RI "US-RI-006 value is wrong"; WV "supersedes US-WVLAB-001"; GA "US-GAP51-003 is not active" | 0 hits for the listed phrases |
| Minor 12 (IN.2) | `text_fixes.json` with the new stage "post" (in `ccg_common.apply_text_fixes`, applied after `neutralize_markers`): "Source of the 2027 rate [[GAP:RQ-209]]: the 2027 value of 2.90% (table above) is configured from the DOR page [US-INS5-009]; the statute IC 6-3-2-1 was not read." | no contradiction with table 422 |
| Minor 14 (C1 colours) | `build_ccg_docx.py`: Heading 1-4 colour 1F4E79; table header fill E8EDF2 | see the precedent note |
| AR RQ-590 (agent 2) | readable limitation wording (post stage); the 250 figure is absent | tagged RQ-590 |
| Safety net | `ccg_common.tag_gaps()`: a marker whose gaps.json status is `closed` is now dropped and logged (`closed_marker_left`) instead of tagged | 0 closed markers left |
| validate_contract | The 11 agent-2 request entries (RQ-581..591) had a location without the '!' section part, and RQ-590 had the domain `reporting_instruments`. The locations are now set to `<unit>!<section>!L<n>` from the rendered units, and the domain to `statutory_reporting` | PASS (78 files) |

### Precedent inspection (L1), minor 14
`~/mercans-pipeline/shared/REFERENCE_CCG_Bulgaria.docx` was opened read-only with python-docx. Heading 1/2/3: Arial bold, colour 1F4E79. Content tables are nested tables; their header cells are filled E8EDF2 (392 cells) with bold 1A1A1A text. The document-ID table has a 1F4E79 header and the version table a 5B9BD5 header. Built: Heading 1-4 in 1F4E79 (sizes stay at the CCG contract's 14/12/11 pt), and every table header in E8EDF2. Recorded deviation: the Version Control header also uses E8EDF2 (not 5B9BD5), and the header text stays black, not 1A1A1A. The toolkit's statement "1F4E79 appears in no file" is wrong for the CCG docx precedent (QA r3 minor 15, for the toolkit owner).

### Checks on the final DOCX (`run_checks_r3.py`, `c30_scan.py`, `open_check.ps1`)
| Check | Result |
|---|---|
| Structure (reopened) | PASS: 13 modules + 53 annexes, TOC field, 1 section, Version Control `1.0 / 2026-11-02 / Draft` |
| Word open (`open_check.ps1` on a copy with the same md5) | PASS, 0 not clean |
| C11 | PASS 96/96, 174 H3 |
| C29 (v2.12 logic) | PASS: 0 hard, 0 bare, 0 X-runs |
| C30 scan (new `01-ccg/_build/common/c30_scan.py`; weak = register tier B/C or status MANUAL) | 0 tagged numbers whose rows are all weak. 1 text unit cites only a weak row and contains digits (MA RQ-262); "IP 25-18" and "404" there are identifiers, not figures. 11 units have "secondary" wording plus digits; all the digits are statute, bill or form identifiers (e.g. "34-1-10", "S.B. 4219", "BLS 3020") |
| C38 | PASS: 48 recomputed, 0 mismatches |
| C40 | PASS 18/18 |
| C42 / C43 | PASS / PASS |
| C46 shared | FAIL, a known checker limitation (it keeps the last value per key, misreads the percent form and counts digits in GAP tags): 7,812 tags, 376 "mismatches", 116 "unbound". The 150 listed details contain none on a key added this round |
| C46 period-aware | 7,812 tags, 0 keys missing, **0 mismatches**, 277 off-year values, **0 unlabelled**, 118 unbound |
| C69 | PASS: 18 answered rows, 20 CCG examples |
| C70 | PASS: 0 not in register, 0 repealed, 0 gap problems |
| C37 | PASS |
| validate_contract --all | PASS (78 files) |
| Residual phrases | 0 tags of RQ-506/508/524/531/559/562/567/568/570/572; RQ-581..592 each tagged; "Not configured in this release" 554 (572 in r3) |

### Open items
- RQ-592 (`de.termination.separation_notice_warn`) is tagged from the request file only. Agent 2 must add its gaps.json entry.
- RQ-591 (Trump-account FICA/FUTA) and RQ-590 (AR e-file threshold) stay open limitations.
- The propagation ledger needs lines for this round (QA): the m03/m04/m06/m07 federal base tables and the RQ-592 request.
- The m04 "Ministers' pay" FUTA cell still reads "not in the facts". QA did not flag it in r3, and it was left as it is.

### Accuracy
About 88 % for the federal core and modules: the federal gross-to-net bases, wage definitions, W-4 defaults and fringe valuation are now configured from the Pub. 15 / 15-B / IRC copies on disk. Annexes: 75-85 % each. The remaining limitations are the open gaps listed in the QA report.

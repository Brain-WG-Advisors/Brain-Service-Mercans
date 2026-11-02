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



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

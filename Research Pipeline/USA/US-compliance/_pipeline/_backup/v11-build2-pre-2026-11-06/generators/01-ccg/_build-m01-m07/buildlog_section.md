
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

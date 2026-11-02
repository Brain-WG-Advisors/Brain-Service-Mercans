# US Compliance — Skeleton Manifest

**Created:** 2026-10-29 by compliance-scaffolder. **BASE:** `C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance`. Nothing pre-existed; everything below was created.

## Tier verdict (verbatim)

> Overall T4 (discriminator confirmed 2026-10-29 on source-read evidence; per-jurisdiction census completed at seal attempt 3 and re-checked at seal attempts 4, 5 and 6, 2026-10-30 to 2026-11-02; mandate sealed 2026-11-02 with all 65 questions answered; the limbs reopened and closed at seal attempt 6 (US-MQ-26 CT, US-MQ-45 MS, US-MQ-57 OR) bear on no tier; Stage-5 re-check 2026-11-02: superseded citations re-pointed to their S5 successors, census unchanged (new local layers found only inside T4 states: Lexington KY, Greenwood Village and Glendale CO OPT), and the five prevailing-wage limbs reopened that day (US-MQ-30 GA, 32 IA, 45 MS, 47 NC, 64 UT) and closed at the reseal the same day bear on no tier). Employer-operation test: T4 requires a second independent calculation AND a separate remittance/return to a second authority. Federal: 26 U.S.C. 3402(a)(1) obliges every employer to withhold federal income tax under IRS tables and covers federal tax only [US-FED-012]; FICA and FUTA go on federal returns 941/944/940 [US-FED-005, US-FED-007, US-FED-015]. State: a wage-taxing state imposes its own withholding computed on its own basis (e.g. Va. Code 58.1-461 [US-VAPIT-002]) remitted to the state revenue authority on its own returns (Virginia Tax VA-5/VA-6 [US-VAPIT-003]); state UI is a separate state tax base and agency (Fla. Stat. 443.1216 [US-MULTI-001]; SC Code ch. 41-31 [US-SCS5-015]). Nothing is absorbed into the federal deduction (contrast Switzerland, StHG Art. 36a Abs. 1, where one deduction discharges all levels). FUTA is federal but its credit depends on state UI paid and on the state's Title XII loan status (26 U.S.C. 3302(c)(2) [US-FED-014]): a cross-layer dependency, so futa is T3. Inside a state, a local layer is T4 where a locality receives a separate return (City of Portland Metro SHS / Multnomah PFA [US-ORS5-004]; Ohio municipal income tax, ORC 718.03 [US-OHP52-003]; Pennsylvania Act 32 EIT/LST to the local collector [US-PA-004]; Jersey City and Newark employer payroll taxes on quarterly city returns [US-NJP6-001, US-NJP6-002]) and T3 where it is piggybacked on the state return (Maryland county tax on MW506 [US-MDP51-001]; NYC and Yonkers on NYS-45/NYS-1 [US-NY-008]). Consequence: the federal core and each jurisdiction are declared and scoped as parallel layers, and the multistate domain routes each employee to one or more of them. Jurisdiction annexes (re-checked 2026-10-30, seal attempt 5): 9 T1 (no state wage tax; SUI and levies only: AK, FL, NH, NV, SD, TN, TX, WA, WY; WA declares the Seattle payroll expense tax, a threshold-conditional employer tax on a city return [US-WAP51-001], as a T4-shaped element), 31 T3 (state withholding, local layer absent or piggybacked on the state return), 11 T4 (local layer remitted to the locality on its own return: AL occupational taxes [US-ALP51-001], CO Denver OPT [US-COP52-001], DE Wilmington [US-DEP52-001], KY occupational taxes [US-KYP52-002], MI 23 self-administering cities [US-MIP52-002], MO St. Louis/Kansas City [US-MOP52-006], NJ Jersey City/Newark employer payroll taxes filed with the city [US-NJP6-001, US-NJP6-002], OH [US-OHP52-003], OR [US-ORS5-004], PA [US-PA-004], WV municipal service fees withheld and remitted to the city, W. Va. Code 8-13-13 [US-WVR3-001], Charleston [US-WVR3-002]); 0 unclassified; no classification rests on MANUAL/gated evidence.

**Obligation on agents 3 and 4:** repeat this verdict and its reasoning in the same words in **CCG m01 (Foundational)**, in **scope_manifest.json** and in **the QA report**. A verdict that lives only in MANDATE.md drifts (F24).

## Tree

```
US-compliance/
├── 00-official-sources/        MANDATE.md (scaffolder); legal-basis-register.csv (agent 2)
│   ├── pdfs/  spec-sources/  wtc-sources/  dd-sources/  sample-files/
│   └── ccg-sources/{FED,MULTI,AK..WY}/   53 jurisdiction slices, one source-hunter each
├── 01-ccg/modules/   stage 1  CCG (agent 3)
├── 02-wtc/          stage 5  WTC (agent 3)
├── 03-statutory-integrations/  stage 6  SIR, third-party provider handoff (agent 3)
├── 04-reports-spec/ stage 3  Report Specs (agent 3)
├── 05-data-dictionary/  stage 4  DD (agent 3)
├── 06-payslip/      stage 7  Payslip (agent 3)
├── 07-qa-crosscheck/  stages 8-10  (agent 4)
├── 08-skill/        stage 11 staging (agent 3)
├── 09-design/       stage 12 DESIGN (agent 3)
├── integration-sources/  stage 6 sources (agent 2)
├── logs/  _prompts/  manual re-run path
├── _pipeline/       build-manifest.json (scaffolder), {ARTIFACT}-build-log.md
├── _research/       research packs, facts.json, research-requests, partitioning-update.json (agent 2)
├── _qa/             {ARTIFACT}-review-r{N}.json (agent 4)
├── scope_manifest.json   seeded from shared template; agent 3 fills at stage 2
├── PROPAGATION-LEDGER.md  empty; agent 4 owns it
└── SKELETON-MANIFEST.md
../skills-build/payroll-compliance-united-states/   SIBLING, not created (writes restricted to BASE)
```

**Empty-stage-folder rule:** `01-ccg` ... `09-design`, `integration-sources`, `logs`, `_prompts` are empty at scaffold time. No files, placeholders or README stubs; nothing has been written yet. Checked 2026-11-02: every stage folder is empty except `_prompts/chrome-rehunt.md` (2026-10-29, the orchestrator's manual re-run prompt, not a stage artifact; preserved, not the scaffolder's file).

## Mandate status

**`sealed` 2026-11-02 (resealed after the post-Stage-5 re-check; sealed earlier the same day at seal attempt 6, reopened at the re-check).** 65 of 65 blocks answered: the five part-6 prevailing-wage limbs (US-MQ-30 GA, US-MQ-32 IA, US-MQ-45 MS, US-MQ-47 NC, US-MQ-64 UT) closed on their restored A.2 rows, read on the saved DOL WHD copy `00-official-sources/ccg-sources/MULTI/DOL-WHD-state-prevailing-wages_2026-11-02.html` (edition 2023-01-01; not used for MI). Every register_id cited resolves to an `active` row of `legal-basis-register.csv` (mechanical check, 2,533 rows). Every artifact in `_pipeline/build-manifest.json` is still `scaffolded`; only the orchestrator advances status.

## Per-stage source partitioning (F22/F23)

Limit 33,554,432 bytes (32 MB) per stage input. The pre-flight sums recursively: measure the folder the stage reads, keep each file in exactly one subfolder.

| Stage | Reads | Measured bytes | Budget |
|---|---|---|---|
| 1 | `00-official-sources/ccg-sources/{JUR} (one jurisdiction per fan-out unit)` | 3,933,039 whole tree, 9 files (largest slice OR 1,996,204), measured 2026-11-02 | 33,554,432 |
| 3 | `00-official-sources/spec-sources` | 0 (empty) | 33,554,432 |
| 4 | `00-official-sources/dd-sources` | 0 (empty) | 33,554,432 |
| 5 | `00-official-sources/wtc-sources` | 0 (empty) | 33,554,432 |
| 6 | `integration-sources` | 0 (empty) | 33,554,432 |
| 7 | `00-official-sources/sample-files` | 0 (empty) | 33,554,432 |

Stages 3-7: 0 bytes, re-measured 2026-11-02. `00-official-sources/pdfs/` (mandate research corpus, 688 files, 214,620,192 bytes on 2026-11-02) is read by no stage and must never be a stage input.

Stage 1 cannot read the whole `ccg-sources/` tree: 53 jurisdiction corpora will exceed 32 MB. Each fan-out unit reads only `ccg-sources/{JUR}/`. Agent 2 reports measured bytes in `_research/partitioning-update.json`; the scaffolder merges them into `source_partitioning` and updates this table. Stages 3-5 may need the same per-jurisdiction split once measured.

## Fan-out units (Step 5)

| Unit | Mandate questions |
|---|---|
| FED | US-MQ-01..09, US-MQ-11, US-MQ-12 |
| MULTI | US-MQ-10 |
| AK (Alaska) | US-MQ-20 |
| AL (Alabama) | US-MQ-21 |
| AR (Arkansas) | US-MQ-22 |
| AZ (Arizona) | US-MQ-23 |
| CA (California) | US-MQ-24 |
| CO (Colorado) | US-MQ-25 |
| CT (Connecticut) | US-MQ-26 |
| DC (District of Columbia) | US-MQ-27 |
| DE (Delaware) | US-MQ-28 |
| FL (Florida) | US-MQ-29 |
| GA (Georgia) | US-MQ-30 |
| HI (Hawaii) | US-MQ-31 |
| IA (Iowa) | US-MQ-32 |
| ID (Idaho) | US-MQ-33 |
| IL (Illinois) | US-MQ-34 |
| IN (Indiana) | US-MQ-35 |
| KS (Kansas) | US-MQ-36 |
| KY (Kentucky) | US-MQ-37 |
| LA (Louisiana) | US-MQ-38 |
| MA (Massachusetts) | US-MQ-39 |
| MD (Maryland) | US-MQ-40 |
| ME (Maine) | US-MQ-41 |
| MI (Michigan) | US-MQ-42 |
| MN (Minnesota) | US-MQ-43 |
| MO (Missouri) | US-MQ-44 |
| MS (Mississippi) | US-MQ-45 |
| MT (Montana) | US-MQ-46 |
| NC (North Carolina) | US-MQ-47 |
| ND (North Dakota) | US-MQ-48 |
| NE (Nebraska) | US-MQ-49 |
| NH (New Hampshire) | US-MQ-50 |
| NJ (New Jersey) | US-MQ-51 |
| NM (New Mexico) | US-MQ-52 |
| NV (Nevada) | US-MQ-53 |
| NY (New York) | US-MQ-54 |
| OH (Ohio) | US-MQ-55 |
| OK (Oklahoma) | US-MQ-56 |
| OR (Oregon) | US-MQ-57 |
| PA (Pennsylvania) | US-MQ-58 |
| RI (Rhode Island) | US-MQ-59 |
| SC (South Carolina) | US-MQ-60 |
| SD (South Dakota) | US-MQ-61 |
| TN (Tennessee) | US-MQ-62 |
| TX (Texas) | US-MQ-63 |
| UT (Utah) | US-MQ-64 |
| VA (Virginia) | US-MQ-65 |
| VT (Vermont) | US-MQ-66 |
| WA (Washington) | US-MQ-67 |
| WI (Wisconsin) | US-MQ-68 |
| WV (West Virginia) | US-MQ-69 |
| WY (Wyoming) | US-MQ-70 |

Owner questions: US-MQ-11 (validation exemptions), US-MQ-13 (state priority), US-MQ-14 (package shape).

## Changelog

- 2026-10-29 — compliance-scaffolder: skeleton created.

## Changelog

- 2026-10-29 — compliance-scaffolder: tier verdict replaced verbatim with the seal-attempt text (T4 confirmed with citations; per-jurisdiction census in MANDATE.md). Mandate NOT sealed.
- 2026-10-29 — compliance-scaffolder: tier verdict updated verbatim (seal attempt 2: local-layer citations OH/PA/NY added; census 9 T1 / 34 T3 / 5 T4 / 3 unclassified). Mandate NOT sealed (58 open).
- 2026-10-30 — compliance-scaffolder: tier verdict updated verbatim (seal attempt 3: census 9 T1 / 33 T3 / 9 T4 / 0 unclassified; CO, KY, MI, MO now T4; AL, DE T4 verified). Mandate NOT sealed (31 open; 34 answered). Stage folders untouched.
- 2026-10-30 — compliance-scaffolder: tier verdict updated verbatim (seal attempt 4: WV T3 provisional -> T4; census 9 T1 / 32 T3 / 10 T4; 10 jurisdiction questions open). Mandate NOT sealed (13 open). Stage folders unchanged.
- 2026-10-30 — compliance-scaffolder: tier verdict updated verbatim (seal attempt 5: NJ T3 provisional -> T4; census 9 T1 / 31 T3 / 11 T4; employer_payroll_levies T4-shaped; WA Seattle element declared T4-shaped; citations re-pointed to active rows). Mandate NOT sealed (2 open: US-MQ-03, US-MQ-05; 63 of 65 answered). Stage folders unchanged.
- 2026-11-02 — compliance-scaffolder: seal attempt 6 completed, mandate SEALED (65/65; attempt 6 answered US-MQ-03/05 on US-OWN-006/007 and reopened then closed US-MQ-26 CT, 45 MS, 57 OR on US-CTP10-001, US-MSP10-001, US-ORP10-001). Tier verdict updated verbatim (census unchanged: 9 T1 / 31 T3 / 11 T4). Partitioning table re-measured. Stage folders unchanged (only the pre-existing _prompts/chrome-rehunt.md noted). Non-blocking hygiene: about 60 supersedes links and 24 free-text supersedes values (P9-MERGE section 7).
- 2026-11-02 — compliance-scaffolder: post-Stage-5 mandate re-check. Tier verdict re-emitted verbatim (parenthetical extended; citations re-pointed to S5 successors: US-OR-003 -> US-ORS5-004, US-SC-002 -> US-SCS5-015); census unchanged 9 T1 / 31 T3 / 11 T4. Mandate status sealed -> pending_research (five prevailing-wage limbs reopened: GA, IA, MS, NC, UT). Stage folders untouched; partitioning unchanged.
- 2026-11-02 — compliance-scaffolder: reseal. Mandate status pending-research -> sealed (65/65; prevailing-wage limbs GA, IA, MS, NC, UT answered on the saved DOL WHD copy). Tier verdict parenthetical updated verbatim ('and closed at the reseal the same day'); census unchanged. Stage folders untouched; partitioning unchanged.

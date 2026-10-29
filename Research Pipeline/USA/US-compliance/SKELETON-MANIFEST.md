# US Compliance — Skeleton Manifest

**Created:** 2026-10-29 by compliance-scaffolder. **BASE:** `C:/Users/instituto/Documents/brain-service/Research Pipeline/USA/US-compliance`. Nothing pre-existed; everything below was created.

## Tier verdict (verbatim)

> Overall T4 (provisional: citations pending US-MQ-04, US-MQ-10 and US-MQ-20..70). Employer-operation test: T4 requires a second independent calculation AND a separate remittance/return to a second authority. The employer computes federal income-tax withholding, FICA and FUTA for the IRS (Forms 941/940, W-2), and in every state that taxes wages computes a SEPARATE state withholding under that state's own tables/certificate and remits it to the state revenue department on a state return; state unemployment insurance is likewise a separate calculation on a separate quarterly report to a state agency. Nothing is absorbed into the federal deduction (contrast Switzerland, StHG Art. 36a Abs. 1, where one deduction discharges all levels). This is the Quebec pattern repeated for up to 51 jurisdictions, plus a local layer (city/county/school district) that is T4 where remitted separately and T3 where piggybacked on the state return. Consequence: the federal core and each jurisdiction are declared and scoped as parallel layers, and the multistate domain routes each employee to one or more of them. No US instrument is on disk yet; the candidate instruments to confirm are IRC chapter 24 (federal withholding), chapters 21/23 (FICA/FUTA) and each state's withholding and UI statutes.

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

**Empty-stage-folder rule:** `01-ccg` ... `09-design`, `integration-sources`, `logs`, `_prompts` are empty at scaffold time. No files, placeholders or README stubs; nothing has been written yet.

## Per-stage source partitioning (F22/F23)

Limit 33,554,432 bytes (32 MB) per stage input. The pre-flight sums recursively: measure the folder the stage reads, keep each file in exactly one subfolder.

| Stage | Reads | Measured bytes | Budget |
|---|---|---|---|
| 1 | `00-official-sources/ccg-sources/{JUR} (one jurisdiction per fan-out unit)` | 0 (empty) | 33,554,432 |
| 3 | `00-official-sources/spec-sources` | 0 (empty) | 33,554,432 |
| 4 | `00-official-sources/dd-sources` | 0 (empty) | 33,554,432 |
| 5 | `00-official-sources/wtc-sources` | 0 (empty) | 33,554,432 |
| 6 | `integration-sources` | 0 (empty) | 33,554,432 |
| 7 | `00-official-sources/sample-files` | 0 (empty) | 33,554,432 |

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

# US — QA cross-check report (Stages 8–10, run close)

- **Country:** United States of America (US). **Build year:** 2026. **Package:** 1.0. **Status:** "For QA" (not issued).
- **Reviewer:** compliance-qa-auditor (independent; it built none of these artifacts). **Date:** 2026-11-04.
- **Verdict (release round 2, 2026-11-05): RELEASED-LOCAL (not uploaded).** REL-1 is fixed: the CCG passes C71 and its md5_final is sealed at 20307cd3. C47 passes with 0 findings on the 26 released files. Section 13.1 has the details. Earlier sections record the previous passes.
- **Evidence:** every command output is in `07-qa-crosscheck/_runclose/out/`, and the scripts are in `07-qa-crosscheck/_runclose/`.

## 1. Tier verdict (same words as the build manifest, the scope manifest and CCG Module 1)

The check found that `build-manifest.json` `tier.rationale` is equal to `scope_manifest.json` `tier.verdict_verbatim` and that the same text appears verbatim in the CCG docx (3,373 characters).

> Overall T4 (discriminator confirmed 2026-10-29 on source-read evidence; per-jurisdiction census completed at seal attempt 3 and re-checked at seal attempts 4, 5 and 6, 2026-10-30 to 2026-11-02; mandate sealed 2026-11-02 with all 65 questions answered; the limbs reopened and closed at seal attempt 6 (US-MQ-26 CT, US-MQ-45 MS, US-MQ-57 OR) bear on no tier; Stage-5 re-check 2026-11-02: superseded citations re-pointed to their S5 successors, census unchanged (new local layers found only inside T4 states: Lexington KY, Greenwood Village and Glendale CO OPT), and the five prevailing-wage limbs reopened that day (US-MQ-30 GA, 32 IA, 45 MS, 47 NC, 64 UT) and closed at the reseal the same day bear on no tier). Employer-operation test: T4 requires a second independent calculation AND a separate remittance/return to a second authority. Federal: 26 U.S.C. 3402(a)(1) obliges every employer to withhold federal income tax under IRS tables and covers federal tax only [US-FED-012]; FICA and FUTA go on federal returns 941/944/940 [US-FED-005, US-FED-007, US-FED-015]. State: a wage-taxing state imposes its own withholding computed on its own basis (e.g. Va. Code 58.1-461 [US-VAPIT-002]) remitted to the state revenue authority on its own returns (Virginia Tax VA-5/VA-6 [US-VAPIT-003]); state UI is a separate state tax base and agency (Fla. Stat. 443.1216 [US-MULTI-001]; SC Code ch. 41-31 [US-SCS5-015]). Nothing is absorbed into the federal deduction (contrast Switzerland, StHG Art. 36a Abs. 1, where one deduction discharges all levels). FUTA is federal but its credit depends on state UI paid and on the state's Title XII loan status (26 U.S.C. 3302(c)(2) [US-FED-014]): a cross-layer dependency, so futa is T3. Inside a state, a local layer is T4 where a locality receives a separate return (City of Portland Metro SHS / Multnomah PFA [US-ORS5-004]; Ohio municipal income tax, ORC 718.03 [US-OHP52-003]; Pennsylvania Act 32 EIT/LST to the local collector [US-PA-004]; Jersey City and Newark employer payroll taxes on quarterly city returns [US-NJP6-001, US-NJP6-002]) and T3 where it is piggybacked on the state return (Maryland county tax on MW506 [US-MDP51-001]; NYC and Yonkers on NYS-45/NYS-1 [US-NY-008]). Consequence: the federal core and each jurisdiction are declared and scoped as parallel layers, and the multistate domain routes each employee to one or more of them. Jurisdiction annexes (re-checked 2026-10-30, seal attempt 5): 9 T1 (no state wage tax; SUI and levies only: AK, FL, NH, NV, SD, TN, TX, WA, WY; WA declares the Seattle payroll expense tax, a threshold-conditional employer tax on a city return [US-WAP51-001], as a T4-shaped element), 31 T3 (state withholding, local layer absent or piggybacked on the state return), 11 T4 (local layer remitted to the locality on its own return: AL occupational taxes [US-ALP51-001], CO Denver OPT [US-COP52-001], DE Wilmington [US-DEP52-001], KY occupational taxes [US-KYP52-002], MI 23 self-administering cities [US-MIP52-002], MO St. Louis/Kansas City [US-MOP52-006], NJ Jersey City/Newark employer payroll taxes filed with the city [US-NJP6-001, US-NJP6-002], OH [US-OHP52-003], OR [US-ORS5-004], PA [US-PA-004], WV municipal service fees withheld and remitted to the city, W. Va. Code 8-13-13 [US-WVR3-001], Charleston [US-WVR3-002]); 0 unclassified; no classification rests on MANUAL/gated evidence.

## 2. Per-artifact rounds, final review and md5

| Artifact | Review files (rounds) | Final review | Delivered file md5 (2026-11-04) | md5 vs seal | Note |
|---|---|---|---|---|---|
| CCG | r1, r2, r3, r3b, r3c, r3d, r3e (PASS), r4 (targeted PASS), r5 (run-close targeted PASS) | `_qa/CCG-review-r5.json` PASS, 1 minor | `01-ccg/US-CCG-001-v1.0.docx` b9de40ce69edefd94c76439261c3318b | No md5_final file. r5 reviewed this md5 | This build had no review until r5 (rebuilt 13:29 after the DESIGN fact re-sync). The r5 diff shows only 6 fact-bound keys changed |
| SCOPE | r1, r2, r3 (PASS) | `_qa/SCOPE-review-r3.json` | `scope_manifest.json` 8c1b7e8a191021db67d3edd8de5fb1ef | Post-PASS minors (c3bdccd4 → 8c1b7e8a), accepted in RSPEC r2/r3 | |
| RSPEC | r1, r2, r3, r3b, r3c (PASS) | `_qa/RSPEC-review-r3c.json` | 20 workbooks = `04-reports-spec/_build/checks/md5_final.txt` (list md5 c58b8d92baccd54bcaf6bfa38ca9c140) | 22/22 OK | C71 re-run at close: 20 files, 0 differences |
| DD | r1, r2, r3 (PASS) | `_qa/DD-review-r3.json` (reviewed e38e8bbc) | `05-data-dictionary/US-DD-001-v1.0.xlsx` f65dc9bc1d512e4a37c6381ee79a816b | 17/17 OK | Changed after r3 when 2 legal-entity fields were added for DESIGN. The diff was verified in `_qa/DESIGN-review-r2.json` B3; no DD review file covers it (finding RC-2) |
| WTC | r1, r2, r3 (PASS) | `_qa/WTC-review-r3.json` (reviewed dccad368) | `02-wtc/US-WTC-001-v1.0.xlsx` 372ac8cb64cb875646865c1033ed6adc | 1/1 OK | Rebuilt for D370 and the "For QA" status; the diff was verified in `_qa/SIR-review-r3.json` (RC-2) |
| SIR | r1, r2, r3 (PASS) | `_qa/SIR-review-r3.json` | `03-statutory-integrations/US-SIR-INDEX-001-v1.0.docx` 36d88850fc8baccaef81fb9c34d2d1af | 22/22 OK | |
| PSL | r1, r2, r3 (PASS) | `_qa/PSL-review-r3.json` | `06-payslip/US_Compliance_Payslip_Generator.xlsx` a34f96d5e0177caed6df89b8280d5b2f | 22/22 OK | |
| SKILL | r1, r2, r3, r3b (PASS), **r4 (FAIL, F28, escalated)** | `_qa/SKILL-review-r4.json` | 99 files = `_pipeline/SKILL-md5.txt` (list md5 cb37ec799a4742698a5e286288cc96ff) | 99/99 OK, but stale | `references/` predate CCG b9de40ce and DD f65dc9bc |
| DESIGN | r1, r2, r3 (content PASS; 1 major escalated, closed by option A and verified by the orchestrator) | `_qa/DESIGN-review-r3.json` | `09-design/US_Regulation_Design_v1.0.md` 729c7cdbf4e51e37d3098b5fa565cb0d | 1/1 OK | Held in `_design_artifact`, because schema 1.4.0 caps the stage at 11 |

## 3. Stage 8 — alignment (re-run at close)

| Recon | Result |
|---|---|
| RSPEC × DD (`dd_recon.py`, both directions) | 949 spec rows: 190 MAPPED, 759 NOT-DD (by rule), **0 UNMAPPED**. DD usage 145/145 elements used. 0 "(forward reference)" left in column L (ledger line 91) |
| WTC × DD × RSPEC (`wtc_recon.py`) | 635 rows: 634 MAPPED, 1 EXCEPTION (the recorded notice-template input) |
| SIR × RSPEC × DD (`sir_recon.py`) | 229 REPORT_ROW + 7 MAPPED_LIMITATION, 20 SPEC, **0 UNMAPPED**. It also lists 2 DD elements with no consumer: the DESIGN-only fields "Supplemental wage withholding method election" and "State-assigned unemployment insurance rate". sir_recon does not count DESIGN as a consumer, while dd_recon does. Finding RC-3 (minor) |
| PSL (`psl_recon_check.py`) | 250 rows, 0 UNMAPPED, 0 missing crosswalk lines, 0 PSL facts not placed |
| DESIGN (`design_recon.py`) | WTC 335, DD 40, REG 45, GAP 15, FLAG 37, REGULATION 13: **0 unmapped** |

Sealed outputs were compared before and after the re-runs. `sir_recon.csv` was overwritten by the re-run and then restored byte-exact (md5 05c7a301… = md5_final); the run-close copy is `_runclose/out/sir_recon_runclose.csv`. The other four outputs were unchanged.

## 4. Stage 9 — pre-delivery audit

The deterministic ids in `mercans_pipeline_v2_12.sh` were confirmed with grep (C37, C38, C39, C41 blocks present). The table records which version of each check was applied.

| Check | Result | Evidence |
|---|---|---|
| C37 (Stage 9b suite) | **PASS**: 49 cases, 85/85 lines, 100 % law-basis agreement (target 98 %), 0 residuals, 0 regressions | `_validation/results/run-20261104-135134/c37_report.json` |
| C38 worked examples (`--module all --facts --specs`) | **PASS**: 927 tables, 55 results recomputed, 0 mismatches | `out/c38.json` |
| C39 Test 0 | **FAIL**: 41/56 = 73.2 % (target 95 %). 41 PASS, 0 FAIL, 15 UNVERIFIED (access blocked). 33 of the 56 items are high risk | `07-qa-crosscheck/US-TEST0.json`, `out/c39.json` |
| C40 coverage matrix | PASS 18/18 | `out/c40_c41.json` |
| C41 currency | **FAIL** (see section 7, B2) | `out/c40_c41.json`, `_runclose/c41_breakdown.py` |
| C42 / C43 | PASS (0 foreign leftovers; one package version 1.0, 0 problems) | `out/c42_c44.json` |
| C44 | Shared checker SKIPs (US filing ids are not document ids). Crosswalk run `c44_mapped.py`: **PASS**, 20 filings = 20 specs. Weak: most manifest formats name no format family | `out/c44_mapped.json` |
| C45 (design) | PASS: 54 conditions, 0 dead, 0 unit errors, 0 forward refs | `out/c45.json` |
| C46 period-aware (mandatory) | **PASS**: 27 deliverables, 12,216 tags, 0 keys missing, **0 mismatches**. 407 tags hold out-of-year values; 1 is unlabelled to the checker (UI-001 Example Analysis!C7, NJ 319; row B7 says "in 2027", so this is a false positive). 247 unbound numbers are citation, layout and code-table numbers of the class already recorded in each review; binding 98.0 % | `out/c46_period_pkg.json` |
| C46 shared, package-wide | FAIL, **exempt** (US-OWN-011, checker keeps one value per key) | `out/c46_shared.json` |
| C47 clean release | Not applicable yet. It runs at Stage 13 on `10-release/` (release_crosscheck), and no release folder exists | — |
| C48 / C49 / C50 | FAIL with 1 problem each, exactly the **exempted** items (US-051 TA from 2026-07-04; KW-100 form id; US-126 GA wording) | `out/content.json` |
| C53 SIR, C56 spec field sources, C57 payslip, C70 citations | PASS (0 problems; C56 934 fields; C70 7 citations, 0 gap problems) | `out/content.json` |
| C69 suite coverage | PASS (18 answered rows, 21 CCG examples) | `out/c69.json` |
| C71 spec regeneration | PASS (20 files, 0 differences); workbook md5 unchanged after the run | `out/c71.json` |
| C29 residual markers, package incl. design and skill | PASS: 126 files, 0 hits. "FORMAT TO CONFIRM vs a real filing" (203 Report Matrix / File Structure cells) is the sanctioned portal-registry label and does not count as a marker | `out/c29_pkg.json` |
| `tag_sync_check.py` | **0 stale** (CCG 7,924, SIR 479, RSPEC 1,565, DD 202, WTC 1,266, PSL 219, DESIGN 561 tags) | `out/tag_sync.json` |
| Vocabulary / PATH lint (`note_vocab_lint.py`, incl. .md) | 0 hits | `out/vocab_lint.log` |
| md5 of every deliverable vs md5_final | WTC 1/1, SIR 22/22, RSPEC 22/22, DD 17/17, PSL 22/22, DESIGN 1/1, SKILL 99/99: all OK | `out/md5.json` |
| `validate_contract --all` | PASS (110 files before the two new review files; each new file validated individually: PASS) | `out/validate_contract.log` |
| C5 / C6 / C7 / C9 / C21 (manual, no automation in v2.12) | Run by hand in the per-artifact reviews (C5/C6/C7: CCG, SCOPE, RSPEC, DD, SIR, PSL; C9: CCG, WTC, PSL; C21 8-sheet payslip: PSL, RSPEC, CCG). Not re-run at close | `_qa/*-review-r3*.json` manual_review_items |

### C41 decision (recorded)
**C41 blocks release.** In the v2.11 definition, C41 is one of the external gates that keep the run open, and no `validation_exemptions.C41` exists. The auditor may not write an exemption (definition 7.1, F68). C41 can become a named limitation only if the owner records `validation_exemptions.C41` in `build-manifest.json` (reason, official source URL, decided_on) with a dated sweep requirement. The auditor does not recommend that route, because the sweep is mechanical and the FUTA credit-reduction list for 2026 is due from DOL around 2026-11-10. The recommended route is to close C41 as described in section 7, B2.

## 5. Exemptions in force (`build-manifest.json` `validation_exemptions`)

| Check | Owner row | Reason (short) | Source | Decided |
|---|---|---|---|---|
| C34, C35, C36 | US-OWN-010 | No machine-callable national norm, validator or identifier plugin. SSA AccuWage validates EFW2 only inside an authenticated BSO session; State formats are State-specific | https://www.ssa.gov/employer/efw/26efw2.pdf | 2026-11-03, owner default (asked, no objection, reversible) |
| C46 (package-wide shared checker only) | US-OWN-011 | The shared c46() keeps one value per key, so multi-period keys (e.g. OASDI 184,500 / 192,300) mismatch. Period-aware C46 stays mandatory and passes | https://www.ssa.gov/oact/cola/cbb.html | 2026-11-04, owner default |
| C48 | US-OWN-011 | WTC US-051 (W-2 box 12 TA) valid only from 2026-07-04 | https://www.irs.gov/instructions/iw2w3 | 2026-11-04, owner default |
| C49 | US-OWN-011 | False positive: KW-100 is the Kansas guide id (US-KSS5-001), not a WTC code | https://www.ksrevenue.gov/kw100.html | 2026-11-04, owner default |
| C50 | US-OWN-011 | US-126 GA SUI is employer-only; the phrase names the excluded premiums (US-GAS5-006) | https://dol.georgia.gov/document/unemployment-tax/employer-handbook/download | 2026-11-04, owner default |

All five are "owner default", applied by the orchestrator after the owner raised no objection. An explicit owner confirmation is still open (section 6).

## 6. Named limitations (open, with what closes them)

| # | Limitation | Count / detail | What closes it |
|---|---|---|---|
| L-1 | Open research gaps by artifact (`_research/gaps.json`, 753 entries) | CCG 534 open + 32 limitations + 1 check; SIR 39 open; PSL 13 open; WTC 84 limitations; DD 9 limitations; DESIGN 8 limitations; RSPEC (own block) 25 open non-blocking + 23 limitations. Total 586 open, 134 limitations, 32 closed. 2 entries flagged blocking (WTC-RQ-25 DC 2026 method after Act 26-416; WTC-RQ-43 UT Pub 14 effective date) are documented limitations, shown as gaps in the WTC | Source hunter, per gap (`what_would_close_it` in each entry) |
| L-2 | TY2025-labelled items (2026 editions not yet published) | Form 940 2026 instructions and due date (RQ-406, RQ-526, RSPEC-GAP-001, SIR-RQ-03; fact `rspec.fed.form940.due` expired 2026-02-10); 1094-C/1095-C TY2026 (RQ-407, RSPEC-GAP-002, SIR-RQ-02); FUTA credit-reduction States 2026 (`rspec.fed.futa.credit_reduction.states` expired 2025-12-31; DOL list due ~2026-11-10); SC RS-1 TY2026 (RSPEC-GAP-035); State W-2 specs TY2026 for 8 jurisdictions (SIR-RQ-36); 24 `multi.sui.other_state_wage_credit.*` reads (RQ-412..434) | Re-read when IRS/DOL/States publish (Dec 2026–Jan 2027). Refresh facts, CCG/RSPEC/SIR, re-run C41 |
| L-3 | Access-blocked sources | Register: 25 rows `gated`, 114 `MANUAL`. RSPEC: 11 access-outside-US + 5 portal-login + 2 not-published limitations. Test 0: 15 items blocked on 2026-11-04 (all present in the registered local copies). See `BLOQUEIOS-CHROME.md` | Browser session (domain permission) or US network / US colleague; refresh `verified_on` |
| L-4 | DESIGN-RQ-02: Form W-4 before the 2020 revision (allowance method, NRA Table 1) | Not configured in 1.0. **Fallback:** the employee is handled manually; the operator enters the withholding and the engine never runs the employee on the 2020 method silently (Design Part 0, lines 81/241/295/890) | Owner decision on DD 1.1 change request: add Form W-4 revision and allowance count on the employee |
| L-5 | DESIGN-RQ-05: citizen abroad with a Form 673 statement | Not configured in 1.0. **Fallback:** withheld normally (Design line 893) | Owner decision on DD 1.1 change request: add the Form 673 statement indicator and its dates |
| L-6 | DD 1.1 change requests | Two (`dd_change_request_1_1` on DESIGN-RQ-02 and DESIGN-RQ-05). DD-RQ-11 (how each State notifies the assigned SUI rate) remains a limitation; the field exists in 1.0 | Owner, then DD 1.1 build + targeted QA |
| L-7 | US-OWN-009 prevailing wage: optional informational indicator, certified payroll not produced | Build-lead decision (2026-11-02) pending owner confirmation; worded identically in MANDATE, register, scope manifest and CCG (56 sentences) | Owner confirms or reverses. Reversal is a one-constant change in `ccg_common.py` plus a rebuild |
| L-8 | Exemptions applied as "owner default" | US-OWN-010 (C34–C36), US-OWN-011 (C46 shared, C48, C49, C50) | Owner confirms explicitly |
| L-9 | No real filed sample, provider layout or engine run | Every Report Matrix row is "FORMAT TO CONFIRM vs a real filing"; the provider runbook is deferred until a provider is chosen (SIR-RQ-27) | Choice of provider; one accepted filing per channel |
| L-10 | Package-wide shared C46 FAIL | Checker limitation (last value per key wins); exempted; period-aware C46 = 0 mismatches | Shared checker made period-aware (owner of shared tools) |

## 7. What blocks release (exact list)

| # | Gate | Problem | What closes it | Owner |
|---|---|---|---|---|
| B1 | **C39 Test 0** | 41/56 = 73.2 % < 95 %. The 15 UNVERIFIED items (T42–T56) could not be fetched from this machine (403 / refused / script page). All 41 fetched items PASS | Re-verify T42–T56 on the authority site from a browser and add the quotes to `US-TEST0.json`. Re-run `test0_check.py --artifacts CCG,WTC,DD,RSPEC`. The registered local copies already contain all 15 values, so 56/56 is expected | Auditor (browser session) |
| B2 | **C41 currency** | (a) `00-official-sources/bulletin-sweep.json` missing, so no sweep per authority and no `next_year` entry. (b) 987 non-superseded register rows not current: 948 with no effective_from, 19 past effective_to but still active, 13 with no effective_from and no verified_on, 6 with no verified_on, 1 with no effective_from and past effective_to. (c) 2 facts expired: `rspec.fed.form940.due` (to 2026-02-10, no successor) and `rspec.fed.futa.credit_reduction.states` (to 2025-12-31). (d) 4 in-year changes whose change date is not written in the CCG or design: `rspec.me.wh_return.form` (2026-04-14), `sir.nj.withholding.agent_authorization` (2026-06-09), `sir.dc.withholding.agent_authorization` (2026-09-16), `sir.tx.ui.agent_authorization` (2026-03-13) | (a) Source hunter writes the sweep, one per register authority, ≤ 14 days old, plus `next_year`. (b) Fill effective_from (in-force or publication date) and verified_on; set past rows to `superseded`/`historical`. (c) Add the successor period (TY2026 rule or an explicit "TY2025 rule until the 2026 edition" entry) and the 2026 credit-reduction list when DOL publishes. (d) Builder writes the change dates where these keys are printed. Then re-run `research_checks.py` | Source hunter, then builder |
| B3 | **F28 SKILL** | `references/` predate CCG b9de40ce and DD f65dc9bc. The 5 practice notes (GA/SC/NE/OH/CT) are stale in `01-ccg/m06_tax.md`, `01-ccg/m13_practices.md` and `13-gotchas.md`; the 2 new DD elements are missing from `05-data-dictionary.md`; `ma.pfml.rate.selection_basis` is missing from `12-states/MA.md` (`_qa/SKILL-review-r4.json`) | Human go-ahead (the round ceiling has been reached). Then one bounded regeneration of the skill + selfcheck + `SKILL-md5.txt`, and a targeted F28 re-check | Owner → builder → auditor |

## 8. Other findings (non-blocking)

| Id | Severity | Location | Problem | Expected |
|---|---|---|---|---|
| RC-1 | minor | `01-ccg/US-CCG-001-v1.0.docx` Module 6 and Module 13, SC practice row, Sources cell | Prints the IL 26-20 schedule (1.99 / 5.21 minus 966) but cites only [US-SCS5-004] | Cite [US-SCS5-004; US-SCS5-005] at the next CCG build (`_qa/CCG-review-r5.json`) |
| RC-2 | minor | `_qa/` | The post-PASS changes to DD (f65dc9bc) and WTC (372ac8cb) have no own targeted review file; their evidence is in DESIGN-review-r2 B3 and SIR-review-r3 | From the next country on, one targeted review file per post-PASS change (proposed L14) |
| RC-3 | minor | `03-statutory-integrations/_build/sir_recon.py` DD_ELEMENT direction | The 2 DESIGN-only DD elements show as NO_CONSUMER on a re-run | Credit DESIGN as a consumer, as `dd_recon.py` does, at the next SIR build |

## 9. Accuracy (honest, by evidence on disk)

The bands follow the definition: research only gives 75–85 %; an official template or specification plus research gives 90–95 %. No real filing and no portal verification exist for any artifact, so no artifact reaches 95–100 %.

| Artifact | Accuracy | Justification |
|---|---|---|
| CCG | **about 88 %** for the federal core and the modules; **75–85 %** per State annex | Every value is bound to a registered fact (tag_sync 0 stale; period-aware C46 0 mismatches). C37 is 100 % on 49 cases against the IRS / State published examples. C38 recomputes 55 results with 0 mismatches. Test 0 passed every CCG item it could fetch (13/13; 8 more blocked). 534 open CCG gaps, mostly per-State detail, keep the annexes at research level |
| SCOPE | about 92 % | Census cross-check 1,319 items, 0 without a pair. The WV fee is open. US-OWN-009 is unconfirmed |
| RSPEC | about 78 % overall (row range 50–90 % in the Report Matrix) | Federal forms and EFW2 are read from official specifications (Pub. 42-007, Forms 941/940/944/943 drafts), which supports up to 90 % for those rows. State rows are research only, with 25 open and 23 limitation gaps. No validator or sample (C34–C36 exempt) |
| DD | about 80 % | 145 elements, recon both directions 0 unmapped; 9 limitations (State certificate lines, external code lists); 2 DD 1.1 change requests |
| WTC | about 85 % | 533 rows bound to facts; 84 limitation cells; C48–C50 residues are exempted items |
| SIR | 75–85 % | Official channel pages read for most rows; no provider layout and no real filing; 39 open cells |
| PSL | about 85 % | Built on the official reference structure, with every rule in a register row; 13 open items; no real US payslip sample |
| SKILL | about 85 % **once re-synced**. As delivered it is stale for 5 practice notes and 2 DD elements | Verbatim copy of the approved artifacts |
| DESIGN | about 88 % | 0 dead flags, recon 0 unmapped. State tables are referenced, not restated. No engine run |

Test 0 is 73.2 % by the C39 rule; on the items that could be fetched it is 41/41. These figures are not rounded up. The package becomes releasable only when B1–B3 are closed.

## 10. Run-close re-check after the B1–B3 fixes (2026-11-04)

This section supersedes sections 2, 4 and 7 wherever they differ.

### Status of the three blockers
| # | Gate | Result now | Evidence |
|---|---|---|---|
| B1 | C39 Test 0 | **FAIL: 50/56 = 89.3 %**. 50 PASS, 0 FAIL, 6 UNVERIFIED. By artifact: CCG 17/21, WTC 13/14, SIR 3/4, DD 6/6, PSL 5/5, RSPEC 6/6. The 9 new PASS quotes (T42–T45, T47, T48, T52–T54) were checked against the saved Chrome texts under `00-official-sources/ccg-sources/` (`_runclose/c39_quotes.py`). The T48 quote was a paraphrase; the auditor re-aligned it to the saved text (field `_quote_fixed_by`). The value (7,000) was in the saved text throughout. The saved texts are short transcribed excerpts (147 to 532 bytes), not full page captures. They are accepted as reading records because each value is also in the registered local copy | `US-TEST0.json` (backup `.bak-c39`), `_runclose/out/c39_r2.json` |
| B2 | C41 | **PASS**: 2,441 active rows, 0 not current, 0 expired facts; 58 sweeps (last on 2026-11-04), 0 authorities unswept, 5 hits. Also: C40 PASS 18/18; C70 PASS (0 repealed cited); tag_sync 0 stale; period-aware C46 0 mismatches over 12,221 tags | `_runclose/out/c40_c41.json`, `c70_r2.json`, `tag_sync.json`, `c46_period_pkg.json` |
| B3 | SKILL F28 | **PASS** (`_qa/SKILL-review-r5.json`). Every item from SKILL-review-r4 is cleared. The skill was built at 14:57, after the last CCG, DD and SIR builds. The auditor re-ran selfcheck and selfcheck_strict: 0 misses | `_qa/SKILL-review-r5.json` |

### Post-PASS rebuilds reviewed (targeted)
| Artifact | md5 now | Review | Diff vs `_pipeline/_backup/pre-c41-2026-11-04/` (and `pre-c70-2026-11-04/`) |
|---|---|---|---|
| CCG | 2bdf6f88ebcaa31c6ee743f0ba458096 | `_qa/CCG-review-r6.json` PASS (1 major register item, 1 minor) | 11 lines added, all in the m10 "Changes during 2026" table (6 keys, each found in its registered copy). Against pre-c70: 0 text changes |
| RSPEC | 22/22 = md5_final | `_qa/RSPEC-review-r3d.json` PASS (1 major, F27) | DOR-001: 3 cells (ME "(from 2026-04-14)"); IRS-004: 7 cells; the other 18 workbooks: 0. C71: 0 differences |
| SIR | 22/22 = md5_final | `_qa/SIR-review-r4.json` PASS (1 minor) | SIR-RQ ids renumbered by +2; gaps.json and the skill use the new numbers consistently. 22 real changes: NJ/DC/TX change dates, Form 940 rule replaced by a gap, Ohio school district code replaced by a gap, new DD element row |
| DD, WTC, DESIGN | no text change | none needed | 0 text changes; the md5 differences come from workbook packaging only |

### Spot-check of retrieval-dated register rows (20 of the 825 newly dated, seed 41)
All 20 rows carry `effective_from_basis: retrieval` and the note "effective_from not stated in the instrument; in force as at retrieved_on". In each, effective_from equals retrieved_on and there is no publication date. Examples: US-DCR3-001 (D.C. Code 47-1812.08), US-MAS5-005 (MGL c.151 s.15), US-TNS5-003 (TN premium chart), US-FIL-016 (GA wage-file page).

**The flag is honest:** it does not claim a start date. The date is a lower bound: the rule is known to be in force on that day. Register dates must therefore never be used for period selection. The facts carry their own effective dates, and period-aware C46 shows 0 mismatches. Basis counts: retrieval 866, publication_date 95.

### Decision on the 6 rows set back to active
- **Accepted:**
  - US-FEDS5-013: Notice 2025-62 still governs the TY2025 penalty relief.
  - US-CAS5-020: FTB 2025 instructions; no 2026 edition exists and it is not repealed.
  - US-INP51-001: the earlier end date had no successor notice.
- **Accepted only as a temporary workaround, not as correct data** (major, routed to the source hunter):
  - US-OHR3C-001 (true end 2026-06-15) and US-OHP52-001 (true end 2026-07-31): their end dates were moved into free text.
  - US-RIS5-008: the row now reads "version effective until 2026-01-01" with effective_from 2026-11-02, which is plainly false.
- **Correct fix:** keep the true periods, set status `historical`, and have the shared C41 skip `historical` rows as it already skips `superseded` ones (C70 already ignores `historical`).
- **Impact:** the workaround changes no value, because the facts carry the right periods.
- **Inconsistency to note:** US-FEDS6-009 (the 2025 credit-reduction list) is `superseded`, yet CCG m10 and RSPEC IRS-004 cite it as the source of the closed period. That is the treatment the six rows were moved away from.

### Other findings from the re-check (none blocks release)
| Id | Severity | Location | Problem | Expected |
|---|---|---|---|---|
| RC-4 | major | `04-reports-spec/US-IRS-004-Form940-Spec.xlsx` Report Matrix B11/F27 vs the SIR row for US-IRS-004 | The RSPEC prints the labelled TY2026 Form 940 carry-forward (Feb 1, 2027; re-derived and correct); the SIR prints a gap for the same return | One treatment in both, mirrored the same day (F27) |
| RC-5 | major | register rows US-RIS5-008, US-OHR3C-001, US-OHP52-001 | Closed-period sources shown as active with no end date; RIS5-008 also has a false start date | As above |
| RC-1 | minor | CCG SC practice row | Still cites only US-SCS5-004 | Add US-SCS5-005 |
| RC-6 | minor | SIR section 8, Ohio school district code | Bare gap, while the DD and RSPEC use the limitation wording | Print the DD limitation wording |

### All gates at the re-check
- **md5 vs md5_final:** every deliverable matches (WTC 1/1, SIR 22/22, RSPEC 22/22, DD 17/17, PSL 22/22, DESIGN 1/1, SKILL 99/99). The CCG is 2bdf6f88, reviewed in r6.
- **PASS:**
  - C37: 49 cases, 100 %.
  - C38: 928 tables, 55 recomputed, 0 mismatches.
  - C40, C41, C42, C43, C45, C46 period-aware, C53, C56, C57, C69, C70, C71.
  - C44 through the crosswalk.
  - C29 package: 0. Vocabulary lint: 0.
  - validate_contract: PASS for 112 files; the 4 new reviews were validated individually.
- **Exempted:** C48, C49 and C50 fail only on the exempted items.
- **FAIL:** C39 only.

### What a C39 owner exemption or limitation must say (if the owner chooses that route)
The auditor will not write it (definition 7.1, F68). The owner must record it in `build-manifest.json` `validation_exemptions.C39` (contract 1.4.0), with these elements:
1. **reason:** "6 of the 56 Test 0 assertions could not be opened on the authority site from the build location on 2026-11-04, by WebFetch or browser (connection refused, Cloudflare, geo-block): T46 IN income tax 2026 2.95 % [US-INS5-009]; T49 NC 3.99 % [US-NCS5-011]; T50 KY 3.5 % [US-KYS5-009]; T51 UT 4.45 % [US-UTS5-001]; T55 TX Form C-42 [US-TXP52-008]; T56 OR ORS 657 other-state wage credit [US-ORS5-015]. The other 50 are PASS with quotes and 0 FAIL. The registered local copies (retrieved 2026-10-29 to 2026-11-03) contain all 6 values (07-qa-crosscheck/_runclose/blocked_local.py). Measured Test 0 is 89.3 %, and 100 % of the readable sample."
2. **source:** the official URL of each of the six items (the `url` field of T46, T49, T50, T51, T55 and T56 in `US-TEST0.json`).
3. **decided_on / decided_by:** the owner's own date and name, not "owner default".
4. **Dated condition:** the six pages are re-read on the authority sites from a US network or by a US colleague, before production or by a stated date. The results go into `US-TEST0.json` and `test0_check.py` is re-run. Any FAIL reopens the run, and the fact is corrected at its source.
5. **Register row:** a `US-OWN-0xx` governance row citing the exemption, as US-OWN-010/011 do, with the same words in the QA report and the handover.

**Route with no exemption:** a US colleague, or a US VPN exit (an owner decision, see `BLOQUEIOS-CHROME.md`), reads the six pages. 56/56 = 100 % passes C39.

### Accuracy (updated)
Unchanged from section 9 except for two points: Test 0 is 89.3 % under the C39 rule and 50/50 on the readable items, and SKILL is about 85 % and now in sync.


## 11. Re-check 3: F27 fix, minor fixes and skill round 6 (2026-11-04)

This section supersedes section 10 wherever the two differ.

**Verdict: BLOCKED, by C39 only.** C39 Test 0 is unchanged at 50/56 = 89.3 %. Nothing new blocks release.

| Item | Result | Review |
|---|---|---|
| RC-4 (F27): Form 940 rule, RSPEC vs SIR | **Closed.** The SIR Form 940 cells now print `[[FACT:rspec.fed.form940.due]]` with the same text as RSPEC IRS-004 | `_qa/SIR-review-r5.json` |
| RC-6: SIR wording for the Ohio school district code | **Closed.** The SIR prints the fact followed by the DD limitation sentence (based on the 2025 list US-OHS5-019, effective to 2025-12-31) | `_qa/SIR-review-r5.json` |
| RC-1: SC citation in the CCG | **Closed.** The SC, WI, NE, OH, CT and MA practice rows in m06 and m13, and the m05 MA PFML decision line, now cite their `_also` rows. The WI row was also under-cited before this fix: its W-166 rates 3.54/4.65 are only in US-WIS5-011. The fix corrects that too | `_qa/CCG-review-r7.json` (md5 333e8ee60a3d97a9b229b859c4f5da7c) |
| `f44_lib.py` `LIMITATION_KEYS` | **Accepted for 1.0, minor finding.** It skips F44 for the two keys whatever their value. The auditor checked by hand that the skip is safe today: US-FEDS5-031 contains "February 2, 2026" and "February 10", US-OHS5-019 contains "9999", and the TY2026 dates re-derive. A later change of value would not be checked, so pin the skip to the current value (or to the derived elements only) at the next SIR build | `_qa/SIR-review-r5.json` |
| Skill round 6 (6 files) | **PASS.** The diff from `pre-skill-b4` maps to the same CCG citation changes, the SIR changes, the review ids and the gap counts. Selfcheck and selfcheck_strict show 0 misses | `_qa/SKILL-review-r6.json` |

**Diff mapping:**
- **CCG (24 lines).** Only the citation cells changed; the tag text is unchanged.
- **SIR (208 raw lines).** The SIR-RQ ids were renumbered by -2 because the two F44 gaps were removed. With the ids masked, 12 lines changed, and each maps to a stated cause. `gaps.json` (39 SIR-RQ entries) and the skill's `14-known-gaps.md` agree id by id.

**Gates re-run:**
- tag_sync: 0 stale.
- C41: PASS. C40: PASS. C70: PASS. C53: PASS.
- C71: 0 differences.
- C38: PASS, 0 mismatches.
- Period-aware C46: 12,224 tags, 0 mismatches.
- C29: 0. Vocabulary lint: 0.
- SIR f44_self: 409 tags, 0 misses.
- md5 vs md5_final:
  - WTC 1/1, SIR 22/22, RSPEC 22/22, DD 17/17, PSL 22/22, DESIGN 1/1, SKILL 99/99.
  - CCG is 333e8ee6, reviewed in r7.

**Still open and not blocking:**
- RC-5 (major): register rows US-RIS5-008, US-OHR3C-001 and US-OHP52-001 (section 10).
- The `LIMITATION_KEYS` pin (minor).
- Everything named in section 6.

The C39 options are unchanged: either a US reader confirms the 6 pages, or the owner records an exemption with the content set out in section 10.


## 12. Re-check 4 (C39), 2026-11-05

**Verdict: RELEASE-READY.** C39 now PASSes, and it was the only gate still failing. This section supersedes sections 10 and 11 where they differ.

- **What changed.** The user opened five of the blocked pages live on their official hosts through a browser VPN (Americas region) and saved them to `00-official-sources/ccg-sources/_test0-opera-2026-11-05/`.
- **Independent check by the auditor.** Each quote was looked up in the saved file (`_runclose/c39_vpn.py`):

| Test | Saved file | Text found in the file | Supports the assertion |
|---|---|---|---|
| T46 IN 2.95 % | IN-DOR-rates.html | "The Indiana Individual adjusted gross income tax rate for 2026 is 2.95% and will adjust in 2027 to 2.9…" | Yes |
| T49 NC 3.99 % | NC-GS105-153.7.html | "Taxable Years Beginning … In 2025 4.25% After 2025 3.99%" | Yes |
| T50 KY 3.5 % | KY-KRS141.020.pdf | "(f) For taxable years beginning on or after January 1, 2026, the tax shall be three and one-half percent (3.5%) of net income" | Yes |
| T55 TX Form C-42 | TX-C42.html | "Form C-42 is used to authorize an individual or service company to represent you…"; title "Written Authorization to Represent Employing Unit (Form C-42)" | Yes |
| T56 OR other-state wages | OR-ORS657.html | ORS 657.095(2): "The remuneration paid by an employer located in this state for work performed in other states … shall be included in payroll when the work in the other states is covered by unemployment insurance laws. The Director … shall prescribe the manner of providing proof of the payment of payroll taxes on the wages of an employee earned while working in other states." | Yes. The statute counts wages taxed in another State toward the Oregon payroll (the taxable-wage computation), with proof of the other State's tax. The section does not use the word "credit"; that word is the CCG's paraphrase of this rule |

- **Shared check.** `test0_check.py`: **C39 PASS, 55/56 = 98.2 %** (target 95 %).
  - By artifact: CCG 20/21, WTC 14/14, SIR 4/4, DD 6/6, PSL 5/5, RSPEC 6/6.
  - 33 of the 56 items are high risk. There are 0 FAIL.
- **md5.** No artifact changed. Every deliverable matches its md5_final: WTC 1/1, SIR 22/22, RSPEC 22/22, DD 17/17, PSL 22/22, DESIGN 1/1, SKILL 99/99. The CCG is still 333e8ee60a3d97a9b229b859c4f5da7c (reviewed in r7) and SCOPE is 8c1b7e8a. The other checks were not re-run, because only `US-TEST0.json` changed.
- **Non-blocking, before production.** Re-read T51 (UT income tax 2026 = 4.45 %, [US-UTS5-001], https://le.utah.gov/xcode/Title59/Chapter10/C59-10-S104_2026050620260506.html) from a US IP. Record the quote in `US-TEST0.json` and re-run `test0_check.py`. The registered local copy already holds 4.45.
- **Still open, non-blocking.** RC-5 (major, register closed-period rows), the `LIMITATION_KEYS` pin (minor), and everything named in section 6, including the owner confirmations US-OWN-009, US-OWN-010 and US-OWN-011.
- **Accuracy.** As in section 9. Test 0 is 98.2 % (55/56 assertions confirmed on the authority hosts).


## 13. Release check (stage 13, re-check 5), 2026-11-05

**Verdict: RELEASE CHECK FAILED. Not RELEASED-LOCAL.** The package itself remains release-ready on content (section 12). The release step fails on one point: the delivered CCG cannot be reproduced from its generator (C71). As instructed, this is recorded and the review stops here. No md5_final was written for the CCG.

### What holds
- **C47** (`release_crosscheck.py 10-release --version 1.0 --issue-date 2026-11-05 --config _release/release_rules.json`): **PASS, 0 findings.** Output: `_runclose/out/c47.json`.
- **`release_rules.json`.** The file has 25 legit rules, 6 external_versions rules and 3 text_rules. All of them are narrow phrases from the domain:
  - IRS early-release drafts;
  - statutory amendment wording;
  - corrections made on Form W-2c / 941-X;
  - agency spec and toolkit versions;
  - "page/spec updated <date>" rewritten as "dated <date>".

  No rule matches review-process wording. The 4 legit hits in the release (reissued formula, later amendment not checked, pre-amendment amount) sit in statute and formula context.
- **Own grep of the 26 released files** (`_runclose/release_scan.py`). It found 0 review ids, 0 "Corrected <date>" stamps, 0 "now reads", 0 "was:", 0 changelog wording and 0 `[[FACT:` tags. Pipeline-vocabulary hits:
  - 83 × "Wayback copy" in source titles. This is citation provenance (Internet Archive), not revision residue. Minor note: it could be worded "archived copy".
  - 1 × "fund builder". This is Oregon's UI fund-builder rate.
- **The 25 docx/xlsx open** with python-docx/openpyxl: 0 failures.
- **Three released files spot-checked against their sources** (`_runclose/release_spot.py`, after normalising tags):
  - SIR: 0 differences.
  - US-UI-001: only the text_rule ("spec dated") and the Version Control row (2026-11-05, Issued) differ.
  - WTC: only whitespace and the removed "(v2.4 C9)" header suffix differ.
- **The source change to the CCG maps to its stated cause.** Old build 333e8ee6 → new build 20307cd3. No copy of 333e8ee6 exists, so it was reconstructed from the pre-f27 copy plus the known r7 diff. Exactly 3 changes:
  - the DC note `dc.minwage.tipped.cash_wage`, "= 56% x" → "Derived as 56% x";
  - the LA note `la.wh.std_deduction.joint`, "= 2 x" → "Derived as 2 x";
  - the Version Control date 2026-11-04 → 2026-11-05.
- **Checks on the two changed notes:**
  - tag_sync: 0 stale in all 7 artifacts.
  - F44: 56% is in US-DCS5-001 (D.C. Code 32-1003, "as of July 1, 2026 … 56%"); 18.40 and 10.30 are in US-DCS5-011; 12,875 and 25,750 are in US-LAS5-001.
  - Arithmetic: 0.56 × 18.40 = 10.304, which rounds to 10.30; 2 × 12,875 = 25,750.

### What fails (blocks RELEASED-LOCAL)
| Id | Severity | Location | Problem | Expected |
|---|---|---|---|---|
| REL-1 | blocker | `01-ccg/_scratch/annex-DC-MA/build_annexes.py` → `01-ccg/annexes/annex_FL.md`, rows `fl.sui.employer.rate.max` and `fl.sui.employer.rate.min` (notes column) | **C71 for the CCG fails.** A full regeneration (`rebuild_all.py`, run against a scratch copy) gives a CCG different from the delivered 20307cd3 (4 docx lines). The new "= " → "Derived as " rule also rewrites the two Florida notes: "= 378 per employee" becomes "Derived as 378 per employee", and "= 7 per employee" becomes "Derived as 7 per employee". The delivered build was assembled before this rule touched FL, so it cannot be reproduced. The rewrite is also wrong in meaning: 378 and 7 are the per-employee amounts at the 7,000 wage base (5.4 % and 0.1 % × 7,000). The rates are not derived from them | Limit the rule to true derivations (the DC and LA keys), or word the FL notes "equal to 378 per employee at the 7,000 wage base" / "equal to 7 per employee at the 7,000 wage base". Then: rebuild the CCG, confirm C71 shows 0 differences between two runs, run tag_sync and C47, write the CCG md5_final, and re-release. |

**Note on the auditor's own action.** `rebuild_all.py` writes in place. After the comparison, the auditor restored `01-ccg/annexes/annex_FL.md` and `01-ccg/US-CCG-001-v1.0.docx` byte for byte from the scratch copy. The md5 is back to 20307cd395c7994bdc1f30e3d9d831c2, and every other module and annex is byte-identical. The build-side reports (`01-ccg/_build/common/out/finalize_*.json` and similar) were regenerated; they are not deliverables. The regenerated FL file and docx are kept as evidence in `_runclose/out/ccg71_rebuild/`.

**After REL-1 is fixed:** re-run CCG C71, tag_sync and C47 with `--config`, then seal the CCG md5. If those pass, the verdict becomes RELEASED-LOCAL (not uploaded).


### 13.1 REL-1 re-check (release round 2), 2026-11-05: **RELEASED-LOCAL (not uploaded)**
- **Generator fix.** `build_annexes.py` (md5 303094c7) now applies the "Derived as" rule only to `dc.minwage.tipped.cash_wage` and `la.wh.std_deduction.joint`.
- **Independent rebuild.** The auditor ran `rebuild_all.py` twice in a scratch copy of the build tree (`01-ccg`, `_research`, `_pipeline` without `_backup`, `00-official-sources`, `_validation`), not in place:
  - Every module and annex `.md` file is byte-identical to the delivered units. `annex_FL.md` is 5ddbb2a2 on both sides.
  - The rebuilt docx and the delivered 20307cd3 have identical text. Of the zip parts, only `docProps/core.xml` differs, and that part holds the build time. **CCG C71: PASS.**
  - The real tree was not touched.
- **Florida notes.** Both the CCG and `10-release/01-ccg` read "= 378 per employee; +1 point for short-time-compensation employers" and "= 7 per employee". That is the original wording.
- **Sealed.** `01-ccg/_build/checks/md5_final.txt` = `20307cd395c7994bdc1f30e3d9d831c2 *01-ccg/US-CCG-001-v1.0.docx`. The md5 of every deliverable matches its md5_final.
- **C47** (`--config _release/release_rules.json`) on the fresh `10-release` (26 files): **PASS, 0 findings**. All 25 docx/xlsx open.
- **Stale evidence.** The copy in `_runclose/out/ccg71_rebuild/` predates the fix. It is evidence of the REL-1 failure only and is no longer current.
- **Verdict: RELEASED-LOCAL.** The package is in `10-release/` and has not been uploaded to the Drive. Non-blocking items carried over: re-read T51 UT from a US IP before production; RC-5 (register rows for closed periods); pin `LIMITATION_KEYS`; the owner confirmations US-OWN-009, US-OWN-010 and US-OWN-011; the limitations listed in section 6.

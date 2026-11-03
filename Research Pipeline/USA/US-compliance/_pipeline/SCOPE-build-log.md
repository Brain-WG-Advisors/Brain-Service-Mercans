# SCOPE — build log
Artifact: SCOPE (stage 2) | Country: US | Round: 1 | Built: 2026-11-02
Manifest: _pipeline/build-manifest.json (USD, minor units 2, tier T4, package 1.0 / 2027-03-31)
Inputs: 00-official-sources/MANDATE.md (sealed 2026-11-02); legal-basis-register.csv (2,670 lines incl. header; US-OWN-009 added by agent 2 at 18:42, `_research/scope-r1-fix/READY-FOR-BUILD`); US-CCG-001 v1.0 (rebuilt this round, md5 2de2b30cb18a0645d22838fdcb37a152); review `_qa/SCOPE-review-r1.json` (FAIL, finding 1 = expected content).
Template: ~/mercans-pipeline/shared/scope_manifest_template.json, read only (md5 17ad1d6831925b17d2872ed27163a761 before and after; nothing written under ~/mercans-pipeline).
Build command: `python _pipeline/scope/build_scope_manifest.py` (the only source of the file; a correction goes into the script).
Output: `scope_manifest.json` md5 **fa57cd3b930f8d1a97f215f93f52d871** (36,705 bytes).

## Template inspection
Template keys, in order: _comment, country, country_code, year, currency, package{_note, version, issue_date}, oracle{_note, type, name, version, publisher, source_url, suite_dir, notes}, scope_version, scope_decided_by, scope_decided_on, employment_types{in_scope, out_of_scope, rationale}, authority_filings{in_scope[filing_id, authority, frequency, format, integration_type, product_mapping_required], out_of_scope[filing_id, descoping_reason]}, wage_type_categories{in_scope, out_of_scope, special_rules}, option_mapper_scope{_comment, personal_id_type, insurance_type, contract_type, correction_codes, benefit_type}, integrations{outbound, inbound, both, _note}, known_failure_patterns_to_check (F1-F8). All kept in this order; US additions: oracle._register_ids, _scope_decision_dates, tier, jurisdictions, register_ids / ccg_location / channel on entries, option_mapper_scope.filing_status_w4 and `_..._basis` notes, _failure_pattern_decisions.

## Copied, not retyped
| Field | Source | Check |
|---|---|---|
| country / country_code / year / currency | build-manifest country, code, year, currency | equal |
| package | build-manifest.package {1.0, 2027-03-31} | equal. 2027-03-31 is the planning placeholder recorded in build-manifest (`_note`: the owner has not set a date); used because C43 / check 8 need an ISO date identical to build-manifest.package. |
| oracle | build-manifest.oracle (type official_examples, Pub. 15-T 2026, IRS, https://www.irs.gov/publications/p15t, suite_dir _validation, notes, _register_ids US-FED-027, US-FED-001, US-FED-021) | all 8 fields equal |
| tier.verdict_verbatim | build-manifest tier.rationale | byte-identical; present as the '> ' quote in MANDATE.md; 3,373 chars |
| employment_types.rationale | ccg_common CONTRACTOR_SENTENCE + POPULATIONS_SENTENCE | same constants print CCG m01 1.0 and m11.3 |
| prevailing-wage descoping / special rule | ccg_common PREVAILING_WAGE_SENTENCE (worded from US-OWN-009) | same constant prints m04, m10 and every annex section 10 |

## Scope decisions (each with its basis)
| Decision | Verdict | Basis |
|---|---|---|
| Common-law employees of private-sector employers | in scope | US-OWN-008 |
| NRA, statutory, household, agricultural, clergy, employees abroad | in scope at the federal layer | US-OWN-005 (+ US-FEDS5-002/015, US-FEDR3-005, US-FEDS5-029, US-FEDR3-006, US-FED-025) |
| State-level rules for special populations | out (deferred round) | US-OWN-005 |
| Independent contractors / Form 1099-NEC and 1099 series | out | US-OWN-008 |
| Public-sector employers | out | US-OWN-008 (employers = private sector) |
| Jurisdictions FED + MULTI + 50 States + DC (53 CCG annexes) | in scope | MANDATE 'Scope facts' Structure line (owner, 2026-10-29); single package US-OWN-003; equals build-manifest artifacts[CCG].units |
| Territories PR, GU, VI, AS, MP | out | outside the owner's 51-jurisdiction set; MANDATE sdi_tdi_pfml row 'PR, out of scope' [US-FEDP52-007] |
| NH Business Enterprise Tax | out | US-OWN-007 |
| Prevailing wage | optional informational flag; certified payroll reports (WH-347, CA eCPR) out | US-OWN-009 (build lead, pending owner confirmation), US-FEDS5-027, US-CAS5-017 (partial row) |
| Federal filings 941, 944, 943, 940, W-2/W-3 (+W-2c), 1042-S, 1094-C/1095-C, 941-X, Schedule H routing | in, outbound via provider, product_mapping_required true | US-FEDS5-031 (partial), US-FEDR3-006, US-FED-007, US-FEDS5-007, US-FIL-002, US-FEDS5-032, US-FEDS5-016, US-FEDS5-012 (partial), US-FEDS5-029, US-FED-008/028 |
| State withholding, reconciliation/W-2, SUI quarterly, SDI/TDI/PFML/LTC, local returns, OR/NY transit levies, new-hire reports | in, outbound via provider, product_mapping_required true | US-MULTIS5-017, US-MULTIS5-011, US-FEDP52-007, US-WAB5-003, US-COS5-008, US-OWN-007, US-FEDS5-024, US-FEDB5-001, US-MULTIS5-006 |
| Inbound: IWO / e-IWO; IRS levy (668-W); State UI rate notices | in, product_mapping_required true (F8) | US-MULTIS5-007, US-FEDS5-028, US-FEDS5-014; US-AZR3-002, US-CAS5-016, US-AKP51-006 |
| integrations.both | none identified (one explanatory entry, product_mapping_required false) | US-FED-008 |

Every US-* register id cited in the file resolves to the register: 70 active, 3 partial (US-FEDS5-031, US-FEDS5-012, US-CAS5-017, each flagged in the entry or here), 0 missing (the other ids found by the scan are document / question ids inside the verbatim tier text).

## Deviations from the review's expected content
- **IRS lock-in letters not written as an inbound integration.** No register row, fact or MANDATE text supports them (register searched for 'lock-in' / 'lock in': 0 rows). Fact-binding rule: no key, it does not go in. Research request `_research/SCOPE-research-request.json` RQ-01 (non-blocking, validated PASS against research-request.schema.json). The three sourced inbound documents carry the F8 decision; the IRS levy (Form 668-W, US-FEDS5-014) was added in its place as a sourced inbound document.
- **option_mapper_scope codes are scope labels, not DD codes.** They name the in-scope values from CCG m02/m05/m07 with their register basis; the DD (Stage 4) assigns the codes, and C27/F1 reconciles them. Re-check wage_type_categories and mappers against the WTC at WTC close (QA_METHODOLOGY Stage 2 DoD).
- **Jurisdiction-set decision has no owner register row.** The 51-jurisdiction decision of 2026-10-29 is recorded in MANDATE 'Scope facts' (owner) but has no US-OWN-* row; cited through MANDATE + US-OWN-003. Routed to the orchestrator / agent 2 (add an owner row, consumed_by SCOPE); not a builder change.

## Validation (Stage 2 checks 1-8, re-implemented from mercans_pipeline_v2_12.sh L992-1036; scratchpad s2_checks.py)
| Check | Result |
|---|---|
| 1 valid JSON | PASS |
| 2 sections present and non-empty (employment_types x3, authority_filings in/out with reasons, wage_type_categories, the five template option mappers, integrations outbound/inbound/both) | PASS |
| 3 in-scope filing fields (filing_id, authority, frequency, format, integration_type in {inbound, outbound, both}, boolean product_mapping_required) | PASS, 16 filings |
| 4 inbound product_mapping_required set | PASS, 3 inbound, 0 false (no F8 warning) |
| 5 no code in both in_scope and out_of_scope of the same mapper | PASS (also: jurisdictions in/out disjoint) |
| 6 known_failure_patterns_to_check F1-F15 | PASS (F1-F8 template text kept, F9-F15 added with titles from country_failure_log.md; one decision per pattern in _failure_pattern_decisions) |
| 7 oracle (type, name, publisher, irs.gov URL) | PASS; identical to build-manifest.oracle |
| 8 package (N.N, ISO date) | PASS 1.0 / 2027-03-31; identical to build-manifest.package |
| C29 residual markers (placeholder, TODO, TBD, FIXME, XXX, [CHECK], [?], to be confirmed/verified, RESEARCH-GAP, template placeholders 'YYYY-MM-DD', 'https://...', 'engine \| official_examples', 'outbound \| inbound') | PASS, 0 hits; 0 empty string values |
| Wording identity (P4.3) | population sentence in scope rationale, CCG m01 and m11.3: True/True/True; prevailing-wage sentence 2x in the manifest, 56x in the CCG DOCX; tier verdict byte-identical to build-manifest and MANDATE |
| Template diff | non-empty (the file is no longer the seed) |

Not run here (auditor's): the B7 decision table in 07-qa-crosscheck/scope_validation.md; C6 format re-check (formats here are channel-level; field-level formats come with the Report Specs); C44 at RSPEC close.

## Open items
| Location | Item | Route | Blocking |
|---|---|---|---|
| scope_manifest.json!integrations.inbound | IRS lock-in letters unsourced | SCOPE-research-request.json RQ-01 (agent 2) | no |
| scope_manifest.json!jurisdictions | no US-OWN row for the 51-jurisdiction decision | orchestrator / agent 2 | no |
| scope_manifest.json!authority_filings.out_of_scope[3] and special_rules[0] | US-OWN-009 pending owner confirmation | orchestrator to the owner | no |
| scope_manifest.json!package.issue_date | planning placeholder 2027-03-31 (build-manifest) | owner sets the date; rebuild with the script | no |
| scope_manifest.json!wage_type_categories, option_mapper_scope | re-check against the WTC (not built) | WTC close | no |

## Accuracy
About 90 % for the scope statements: every decision rests on an owner row or an active register row, copied from the sealed MANDATE and the CCG. What keeps it below 100 %: one owner decision is delegated and unconfirmed (US-OWN-009), the jurisdiction set has no owner register row, the lock-in letter inbound is unsourced, three cited rows are 'partial', and the mapper / wage-type lists are not yet reconciled with the WTC and DD.

---

# SCOPE — build log, round 3 (after _qa/SCOPE-review-r2.json)
Artifact: SCOPE | Country: US | Round: 3 | Built: 2026-11-03 | Builder: artifact-builder (retry; the previous builder stalled before saving, script was unchanged = backup md5 011f89b1)
Inputs: MANDATE.md (sealed), build-manifest.json, legal-basis-register.csv (US-OWN-002 widened; marker _research/scope-r2-fix/READY-FOR-BUILD), CCG facts (_research/CCG-*-facts.json, 66 files), RSPEC facts (_research/RSPEC-facts.json, 412 facts), CCG m07 / m10 modules.
Changed: only _pipeline/scope/build_scope_manifest.py; scope_manifest.json regenerated by it (never edited by hand).
Script md5 011f89b10d4ba50471084ce833a61c71 -> db2ef5df8ed21df4cd2f89956dd3e7a4. scope_manifest.json md5 fa57cd3b930f8d1a97f215f93f52d871 -> ec4afc3dcc545a67bd5641c14f0a5765 (54,386 bytes).

## Per finding
| # | Finding | Action | What changed |
|---|---|---|---|
| 1 | F15 NV MBT, Seattle PET/SHT missing (blocker) | fixed | New in_scope entries: NV MBT TAX-F003 [US-NVS5-010, -009, -011, US-NVP51-002], CCG Annex NV.3/NV.5; Seattle PET + SHT [US-WAP51-001, US-WAP7-005, US-WAP9V-001], CCG Annex WA.2/WA.5. Cross-check of CCG m10 + RSPEC facts added: "City employer payroll taxes on separate city returns" (Jersey City, Newark [US-NJP6-001/-002], St. Louis PET [US-MOP52-006], Pittsburgh PET [US-PAB5-401]); "State-fund workers' compensation premiums and fees" (WA L&I, NM TRD-41431 fee, OR WBF, WY joint UI/WC). Local entry now names every locality return in the facts (PA EIT/LST, Philadelphia, OH municipal + SD 101/141, MI Detroit, KY Louisville/Lexington, MO St. Louis/KC, AL occupational, CO Denver/Greenwood Village/Glendale OPT, DE Wilmington, OR Portland Metro/Multnomah, WV, NJ). CA DE 542 contractor report added to out_of_scope (US-OWN-008). |
| 2 | F21 separate-return lists | fixed | Local ccg_location = annexes AL, CO, DE, KY, MI, MO, NJ, OH, OR, PA, WV (+ WA Seattle entry); IN/MD/NY piggy-back note on the State withholding entry [US-INS5-007, US-MDP51-001, US-NY-008]. PFML entry = MANDATE separate set WA (+WA Cares), CT, CO, DE, ME, MD (2027-01-01), plus MN [US-MNS5-018], MA [US-MAS5-012], DC [US-DCS5-019] from annex section 5. CA (DE 9) and OR (Form OQ) on the State wage return; NJ on NJ-927/WR-30; RI on TX-17; NY/HI insurer-funded [US-NYB5-401/-402 successors of superseded US-NY-005/-010, US-HI-003]; VT no programme [US-VTP51-006], CCC on WHT-436 [US-VTS5-030]; VA PFML starts 2028-04-01 [US-VAS5-016]. |
| 3 | F2 insurance_type / wage-type categories | fixed | insurance_type 10 -> 19 labels; _insurance_type_basis is now label -> register basis (dict). Added STATEWIDE_TRANSIT_TAX_OR, WORKERS_COMP_EMPLOYEE_SHARE, WORKERS_COMP_STATE_FUND_EMPLOYER, WORKERS_COMP_FEE_NM, CHILD_CARE_CONTRIBUTION_VT, HI_PREPAID_HEALTH_CARE_EMPLOYEE_SHARE, STATE_UI_ADMIN_SOLVENCY_LEVY (US-OWN-007 limb 2 list incl. MA COVID/EMAC/WTF, GA, AR, CA ETT ...), STATE_EMPLOYER_PAYROLL_TAX (NV MBT), CITY_EMPLOYER_PAYROLL_TAX. US-OWN-007 scope statement quoted in full, read from the register at build time (_insurance_type_note). Employee and employer contribution categories carry the same items. |
| 4 | F8 wording | fixed | "All three inbound documents above (IWO / e-IWO, IRS levy Form 668-W, State UI rate notices) ...; IRS lock-in letters pending RQ-01." |
| 5 | clergy / abroad bases | fixed | clergy [US-OWN-005, US-FED-030]; parsonage rule [US-FED-030]; abroad [US-OWN-005, US-FEDR3-007, US-FED-025]. |
| 6 | US-OWN-002 register text | agent 2 done (READY marker); builder re-cited | jurisdictions.in_scope_note, _scope_decision_dates and scope_decided_by now cite US-OWN-002. |
| 7 | Voluntary after-tax deductions empty basis | fixed | register_ids = US-FEDS5-023 + State wage-deduction rows AZ, CO, CT, DE, HI, IA, IL, IN, KS, KY, MD, MI (annex section 7 facts); _basis_note quotes CCG m07 7.1 and RQ-571. |
| 8 | consumed_by ';SCOPE' on 46 rows | routed (agent 2) | Not a builder change. Register read now: US-OWN-002 consumed_by = "MANDATE;SCOPE" (narrower than the review's expected value). The rows added this round also need ';SCOPE'. |

## Scope decisions added this round
| Item | Verdict | Basis |
|---|---|---|
| NV MBT return; Seattle PET/SHT; city employer payroll taxes; State-fund WC premiums/fees | in scope (filings) | CCG annexes + register rows above; tier verdict / build-manifest employer_payroll_levies |
| CA DE 542 contractor report | out of scope | US-OWN-008 (contractor sentence) |
| One-time registrations (CA DE 1, AZ JT-1, ID IBR); employee notices (GA DOL-800, NJ BC-10, CT UC-21, CO DR 0995, DC hire notice); WARN; UI wage-information request responses (IA) | reversible builder classification: in scope for the CCG, no authority return, so no Report Spec (new key authority_filings.related_obligations_no_return) | fact rows cited per item |
| UI rate components (NH admin contribution, NM/UT reserve factor, UT social cost / delinquency surcharge, WY delinquent surcharge, MN special assessment) | inside SUI, not a separate item | SUI basis text |
| TN workers' compensation benefit maxima | not a payroll item (insurer-paid benefit levels) | cross-check exclusion |

## Validation (scratchpad scope_r3_checks.py)
check1 JSON PASS · check2 sections PASS · check3 filing fields PASS (20 filings, each with register_ids) · check4 inbound PMR PASS (3 inbound, 0 false) · check5 mapper overlap PASS (+ insurance_type labels = basis keys) · check6 F1-F15 PASS · check7 oracle PASS (= build-manifest) · check8 package PASS 1.0 / 2027-03-31 · C29 PASS (0 markers) · tier verbatim PASS · register: 186 ids, 0 unresolved, 181 active, 5 partial (US-CAS5-017, US-FEDS5-012, US-FEDS5-031, US-GAS5-020, US-WYP9W-001).
Cross-check: 1,319 filing / insurance / levy facts from the CCG facts (66 files) and the RSPEC facts were classified. Specific items (local, MBT, WC report, school district, municipal, MCTMT, contractor report, registration, notices, PFML returns, UI-linked levies) must have their register id cited in the manifest, or the programme label / filing entry must name the State. Generic per-State returns map to the per-State entries. Result: PASS, 0 unmatched (the first run had 125 unmatched; 8 real gaps were fixed in the script, and the rest were parameter rows of covered programmes after the test was refined).

## Open items
| Location | Item | Owner | Blocking |
|---|---|---|---|
| PFML entry, MA | MA PFML return mechanics unread (ma.report.pfml.quarterly, MA annex) | agent 2 | no |
| register consumed_by | ';SCOPE' on the review-r2 finding 8 rows + rows added this round | agent 2 | no |
| integrations.inbound | IRS lock-in letters (RQ-01) | agent 2 | no |
| partial rows | 5 partial register rows cited | agent 2 | no |
| mappers / wage-type categories | reconcile with WTC / DD real codes | WTC / DD close | no |

## Accuracy
About 92 % for the scope statements: every filing and mapper item now rests on a register row and was cross-checked mechanically against the CCG and RSPEC facts. What remains: US-OWN-009 is still a delegated decision; MA PFML return mechanics are unread; 5 cited rows are partial; and the labels are not yet reconciled with the WTC and DD.

---

# SCOPE — build log, post-PASS minors (after _qa/SCOPE-review-r3.json, verdict PASS; no new SCOPE round)
Artifact: SCOPE | Country: US | Built: 2026-11-03 | Builder: artifact-builder
Scope of this pass: review-r3 findings 4, 5 and 6 (minor, routed_to_builder). Findings 1-3 and 7 not touched.
Changed: only _pipeline/scope/build_scope_manifest.py (backup `build_scope_manifest.py.bak-before-postpass-minors`, md5 3212d0074c05655851dbe52619d87713 = the auditor's post-fix script); scope_manifest.json regenerated by it, never edited by hand.
Script md5 3212d0074c05655851dbe52619d87713 -> 761d096dee46818508717d4228b0c677. scope_manifest.json md5 c3bdccd421424692a7eee43721e929ab -> **8c1b7e8a191021db67d3edd8de5fb1ef** (55,892 bytes). Two consecutive runs give the same md5.

## Per finding
| # | Finding | Action | What changed |
|---|---|---|---|
| 4 | partial rows not flagged where cited | fixed | SUI entry note: "US-GAS5-020 is a partial register row (GDOL proposed rule; adopted text not read)."; option_mapper_scope._insurance_type_basis.SUI: "(US-WYP9W-001 partial: 2026 factor values not in statute)"; out_of_scope[3] (certified payroll): new `note` "US-CAS5-017 partial: eCPR thresholds not stated." (descoping_reason left as the shared ccg_common PREVAILING_WAGE_SENTENCE, so the CCG wording identity holds). |
| 5 | WV unemployment automation and administration fee | fixed | STATE_UI_ADMIN_SOLVENCY_LEVY basis: "WV unemployment automation and administration fee from 2026-07-01, an annual employer bill issued by WorkForce WV by March 31, not part of the quarterly UI return (figure open: CCG wv.ui.sb1053_fee) US-WVS5-002". SUI entry note: "... levies (US-OWN-007, second limb), except where a levy is billed separately (WV annual fee, billed by WorkForce WV, not on the quarterly UI return [US-WVS5-002])." No figure written (register row: '7%' reading unresolved). |
| 6 | duplicate returns | fixed | Local entry: US-NJP6-001/-002 and US-MOP52-006 removed from register_ids; text cross-references the city employer entry for Jersey City / Newark and for the St. Louis W-10 / P-10 (Kansas City US-MOP52-007 stays). City employer entry: "St. Louis Forms W-10 / P-10, one quarterly return carrying both the employer payroll expense tax and the earnings tax withheld from employees [US-MOP52-006]". _in_scope_note: "... with one Report Specification per authority return: Jersey City and Newark payroll-tax returns are specified under the city employer entry; the St. Louis W-10 / P-10 is one return carrying the earnings tax and the payroll expense tax [US-MOP52-006]; the local entry cross-references these." Local ccg_location unchanged (11 MANDATE jurisdictions incl. NJ and MO). |

## Validation (scratchpad scope_r3_checks.py, same script as round 3)
check1 JSON PASS · check2 sections PASS · check3 filing fields PASS (20 filings) · check4 inbound PMR PASS (3 inbound, 0 false) · check5 mapper overlap PASS · check6 F1-F15 PASS · check7 oracle PASS · check8 package PASS 1.0 / 2027-03-31 · C29 PASS (0 markers) · tier verbatim PASS · register: 187 ids (+US-WVS5-002), 0 unresolved, 182 active, 5 partial.
Cross-check (CCG facts 66 files + RSPEC facts): 1,319 items classified, PASS, 0 unmatched.
Jersey City / Newark / St. Louis register ids now appear in exactly one in_scope entry (city employer payroll taxes).

## Routed (not builder changes)
| Item | Owner | Blocking |
|---|---|---|
| append ';SCOPE' to US-WVS5-002 consumed_by (now "CCG;DD;WTC;CCG/annex_WV;WTC/country_specific") | agent 2 | no |
| US-FEDS5-031 is also cited unflagged in the Form 944, Form 940 and Form 941-X entries (in_scope[1], [3], [8]); the review accepted the single flag on the 941 entry, not changed here | auditor's call | no |

## Accuracy
Unchanged at about 92 %; the WV fee figure stays open (CCG wv.ui.sb1053_fee).

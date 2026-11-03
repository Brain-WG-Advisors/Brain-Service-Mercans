# US Scope Lock-In Validation (Stage 2) - round 3 (final)

Reviewer: compliance-qa-auditor (fresh instance; built no part of scope_manifest.json, build_scope_manifest.py, the build-manifest, the register or the CCG)
Date: 2026-11-03
File under review:
- Builder delivery: `scope_manifest.json` md5 `ec4afc3dcc545a67bd5641c14f0a5765` (54,386 bytes), produced by `_pipeline/scope/build_scope_manifest.py` (md5 `db2ef5df`). It regenerates byte-identically from that script.
- After the auditor's two in-place fixes (made through the script, never by hand): `scope_manifest.json` md5 `c3bdccd421424692a7eee43721e929ab` (54,953 bytes); script md5 `3212d0074c05655851dbe52619d87713`.

Ground truth:
- `00-official-sources/MANDATE.md` md5 `1f4ffae0` (sealed 2026-11-02).
- `_pipeline/build-manifest.json` md5 `04633ca4` (unchanged since r2).
- `00-official-sources/legal-basis-register.csv` md5 `245eb2e1` (2,669 rows).
- `01-ccg/US-CCG-001-v1.0.docx` md5 `2de2b30c`.

Review file: `_qa/SCOPE-review-r3.json` (validate_contract: PASS).
Earlier rounds: `_qa/SCOPE-review-r1.json`, `_qa/SCOPE-review-r2.json`.

## Result

**PASS** (round 3 of 3). Findings: 0 blockers, 1 major, 6 minor.
- Fixed in place (2): the major (finding 1) and one minor (finding 2).
- Routed, non-blocking (5): findings 3-7.

All eight r2 findings are closed. Stage 3 (RSPEC) may start on md5 `c3bdccd4`.

## r2 findings: status

| r2 # | Finding | Status in r3 | Evidence |
|---|---|---|---|
| 1 | NV MBT and Seattle PET/SHT returns missing (blocker) | closed | in_scope[16] NV MBT [US-NVS5-010]; in_scope[15] Seattle [US-WAP51-001, US-WAP7-005, US-WAP9V-001]. Live TAX-F003 V2026.1 re-read (.0117, 50,000, due the last day of the month after the quarter; line 1 must match the ESD wages). Seattle PET and SHT pages re-read |
| 2 | Separate vs piggy-backed return lists | closed | Local entry lists exactly the 11 MANDATE jurisdictions. IN / MD / NY piggy-back note sits on the State withholding entry. PFML set = MANDATE set + MN / MA / DC; CA / OR / NJ / RI go on the State or UI return; NY / HI are insurer-funded; VT has none |
| 3 | insurance_type / wage-type categories drop items | closed | 19 labels = basis keys. US-OWN-007 quote is byte-identical to the register text |
| 4 | F8 wording | closed | three inbound documents named |
| 5 | clergy / abroad bases | closed | US-FED-030; US-FEDR3-007 |
| 6 | US-OWN-002 text and consumed_by | closed | register carries US-MQ-13 set; consumed_by MANDATE;SCOPE;CCG/m01_foundational;CCG/annex_MULTI |
| 7 | voluntary deductions empty basis | closed | US-FEDS5-023 + 12 State wage-deduction rows |
| 8 | ';SCOPE' in consumed_by | closed | 186/186 cited rows carry SCOPE |

## Stage 2 checks

The v2.12 script carries these checks only as prompt text at L992-1036, not as a deterministic block. They were re-implemented and run by hand in the auditor scratchpad.

| Check | Result | Evidence |
|---|---|---|
| 1 valid JSON | PASS | json.loads |
| 2 sections present and non-empty | PASS | employment_types, authority_filings, wage_type_categories, option_mapper_scope, integrations |
| 3 in-scope filing fields | PASS | 20 of 20 complete, each with register_ids; 7 out_of_scope, each with descoping_reason |
| 4 inbound product_mapping_required | PASS | 3 inbound, 0 false |
| 5 no code both in and out | PASS | filings, wage-type categories and jurisdictions are disjoint; insurance_type labels = basis keys |
| 6 F1-F15 listed | PASS | 15 of 15 |
| 7 oracle | PASS | equal to build-manifest.oracle |
| 8 package | PASS | 1.0 / 2027-03-31 (planning placeholder; known, non-blocking) |
| C29 residual markers | PASS | 0 hits on both files |
| C30 tier B | PASS | 0 tier-B rows cited |
| Tier verbatim | PASS | identical in build-manifest, MANDATE, CCG m01 and here; by_domain equal |
| Register resolution | PASS | 186 rows: 181 active, 5 partial, 0 superseded or gated; plus US-CCG-001 (document id) |
| C42 / C43 | PASS / PASS | consistency_checks.py |
| C44 | SKIP | no Report Specification yet |
| C56 / C70 | PASS / PASS | content_checks.py. C48/C49/C50/C53 FAIL only because WTC and SIR are not built yet: not applicable at SCOPE close |
| Filings / levies vs CCG + RSPEC facts | PASS | independent re-run on 4,616 facts (1,115 filing / levy / insurance keys). No in-scope filing missing. One contradiction (finding 1) was fixed |
| Wording identity (P4.3) | PASS | prevailing-wage, contractor, tier and population sentences match the CCG. FED.15 / MULTI.15 drift routed (finding 7) |
| Numeric / base-rule verification | 72 / 72 | live WebFetch, or the registered local copy where the host blocks it. Two identifier caveats (AZ UC-603, EFW2C 42-014) are listed in the review |

## Findings (round 3)

| # | Severity | Location | What | Action |
|---|---|---|---|---|
| 1 | major | authority_filings.in_scope[10] note | OR household / agricultural annual returns (OA, WA / OR-STT-A) were put in scope, against the US-OWN-005 deferral in the same file | **fixed in place**: note now names OR-WR; new out_of_scope record [US-OWN-005, US-ORS5-010] |
| 2 | minor | in_scope[12] note, MA clause | 'return to DOR' is not carried by US-MAS5-012 (the page says 'send to DFML') | **fixed in place**: 'contribution to DFML; return channel ... open' |
| 3 | minor | in_scope[5] format; _correction_codes_basis | 'EFW2C Pub. 42-014' is not carried by US-FIL-002 or any other active cited row | agent 2 widens US-FIL-002 |
| 4 | minor | SUI note; SUI basis; out_of_scope[3] | partial rows US-GAS5-020, US-WYP9W-001 and US-CAS5-017 not flagged where cited | builder |
| 5 | minor | STATE_UI_ADMIN_SOLVENCY_LEVY basis; SUI note | WV automation / administration fee [US-WVS5-002] (MANDATE line 52) is missing; it is an annual bill, not on the UI return | builder + agent 2 (consumed_by) |
| 6 | minor | in_scope[13] / [14] | Jersey City / Newark returns are in two entries; St. Louis W-10/P-10 is one return split across two | builder (one spec per return note) |
| 7 | minor | CCG FED.15 P1047, MULTI.15 P1117 | 'State rules are in the State annexes' contradicts the US-OWN-005 deferral sentence | builder at the next CCG touch |

## Ruling: `authority_filings.related_obligations_no_return`

**Accepted** as a reversible builder classification. Reasons:
- Nothing leaves scope. The CCG keeps documenting these obligations, so there is no F15 descoping.
- None of them is a recurring authority return built from payroll data, so Stage 3 has nothing to specify.
- WARN is an HR-scope notice (F19).
- Event-driven per-employee UI reports to an agency (SC UCB-113, GA DOL-402, OH mass-layoff) correctly stay in the SUI entry.

Bases re-read for this ruling:
- 29 USC 2102 (60 days)
- IWD (10 days)
- CDOR DR 0995 notice
- CT UC-21
- GA DOL-800
- NJ BC-10

**Condition:** the RSPEC builder treats the four classes as rules, not as a closed list. That brings in TN LB-0489, PA UC-1609, NY IA 12.3, the State POA forms (CA DE 48, CO DR 0145) and the MN, NH and SC notices.

## B7 decision table (one row per scope decision)

DECISION | IN-SCOPE | OWNED-UPSTREAM | INBOUND-DATA-CONTRACT | REVERSIBLE(Y/N) | BASIS
---|---|---|---|---|---
Private-sector employers; common-law employees | Y | Owner | N | Y | US-OWN-008
Special populations (NRA, statutory, household, agricultural, clergy, abroad), federal layer | Y | Owner | N | Y | US-OWN-005; US-FEDS5-002/-015, US-FEDR3-005, US-FEDS5-029, US-FEDR3-006, US-FED-030, US-FEDR3-007
State-level rules for special populations | N (deferred round) | Owner | N | Y | US-OWN-005
State annual returns of household / agricultural employers (OR OA, WA / OR-STT-A; equivalents in CT, DC, FL, GA, LA) | N (deferred; new out_of_scope record, r3 finding 1) | Owner | N | Y | US-OWN-005, US-ORS5-010
Independent contractors / 1099-NEC / 1099 series; CA DE 542 and State contractor reports | N | Owner | N | Y | US-OWN-008 (+US-CAS5-002)
Public-sector employers | N | Owner | N | Y | US-OWN-008
Jurisdictions FED + MULTI + 50 States + DC | Y | Owner | N | Y | US-OWN-002 (US-MQ-13); single package US-OWN-003
Territories PR, GU, VI, AS, MP | N | Owner | N | Y | US-OWN-002; US-FEDP52-007
NH Business Enterprise Tax | N | Build lead under delegation | N | Y | US-OWN-007
Prevailing wage: optional informational flag; certified payroll (WH-347, CA eCPR) not produced | Flag Y / reports N | Build lead under delegation, **pending owner confirmation** | N | Y | US-OWN-009, US-FEDS5-027, US-CAS5-017 (partial)
Federal returns 941 / 944 / 943 / 940 / 941-X | Y | Provider (outbound hand-off) | N | N (statutory) | US-FEDS5-031 (partial), US-FED-008, US-FEDR3-006, US-FED-028, US-FED-007
Schedule H routing flag; household employer's own Schedule H return out | Flag Y / return N | Household employer | N | Y | US-FEDS5-029
W-2 / W-3 (+W-2c) via EFW2 / EFW2C | Y | Provider | N | N | US-FEDS5-007, US-FIL-002, US-FEDS5-032 (42-014 identifier: r3 finding 3)
1042-S (treaty-exempt NRA wages) via IRIS | Y | Provider | N | N | US-FEDS5-016
1094-C / 1095-C (ALE) | Y | Provider | N | N | US-FEDS5-012 (partial)
State withholding returns (IN / MD / NY local piggy-backed; combined OR OQ, NY NYS-45, NJ NJ-927 / WR-30, NM TRD-41431, VT WHT-436) | Y | Provider | N | N | US-MULTIS5-017, US-INS5-007, US-MDP51-001, US-NY-008, US-ORS5-010, US-NYS5-010, US-NMS5-012, US-VTS5-030, US-NJP51-001
State annual reconciliation and State W-2 (OR: OR-WR) | Y | Provider | N | N | US-MULTIS5-011, US-ORS5-010
SUI quarterly report (incl. event-driven mass-separation reports; UI-linked levies) | Y | Provider | N | N | US-MULTIS5-017, US-ILS5-017, US-RIS5-017, US-WYS5-007, US-SCS5-007, US-GAS5-020 (partial). WV annual fee billed separately: r3 finding 5
PFML / SDI / LTC programme reports where separate (WA + WA Cares, CT, CO, DE, ME, MD from 2027, MN, MA, DC) | Y | Provider | N | N | US-FEDP52-007, US-WAPFML-001, US-WALTC-001, US-WAB5-003, US-CTS5-022, US-COS5-008, US-DES5-013, US-MES5-024, US-MDS5-014, US-MNS5-018, US-MAS5-012, US-DCS5-019, US-VAS5-016, US-CTB5-001, US-MULTIS5-024
Local income / wage tax returns (11 jurisdictions) | Y | Provider | N | N | MANDATE local_income_tax census; 25 register rows in the entry
City employer payroll taxes (Jersey City, Newark, St. Louis, Pittsburgh) | Y | Provider | N | N | US-NJP6-001/-002, US-MOP52-006, US-PAB5-401 (one spec per return: r3 finding 6)
Seattle PET / Social Housing Tax | Y | Provider | N | N | US-WAP51-001, US-WAP7-005, US-WAP9V-001
NV Modified Business Tax (TAX-F003) | Y | Provider | N | N | US-NVS5-010, US-NVS5-009, US-NVS5-011, US-NVP51-002
Transit levies OR (TriMet, Lane) and NY (MCTMT, MTA-305) | Y | Provider | N | N | US-OWN-007, US-ORS5-010, US-NY-003
State-fund workers' compensation premiums / fees (WA L&I, NM fee, OR WBF, WY) | Y | Provider | N | N | US-WALTC-002, US-WAS5-019, US-NMR3-001, US-NMS5-012, US-ORS5-010, US-WYS5-007, US-WYS5-012
Private-insurer workers' compensation premiums | N (outside payroll) | Insurer | N | Y | MANDATE workers_compensation row (data-problem)
New-hire reports | Y | Provider | N | N | US-FEDS5-024, US-FEDB5-001, US-MULTIS5-006
Related obligations with no authority return (one-time registrations, employee notices, WARN, UI wage-request responses) | Y in CCG / no Report Spec | Employer (HR / account set-up) | N | Y (builder classification, accepted r3) | US-CAS5-002, US-AZP52-005, US-IDS5-021, US-GAS5-007, US-NJS5-015, US-CTS5-031, US-COS5-006, US-DCS5-010, US-FEDS5-025, US-CAS5-018, US-IAS5-026
Inbound: child-support IWO / e-IWO | Y | Employer acts | Y (pmr true) | N | US-MULTIS5-007, US-FEDS5-028, US-FEDS5-014
Inbound: IRS levy Form 668-W | Y | Employer acts | Y (pmr true) | N | US-FEDS5-014
Inbound: State UI rate notices (AZ, CA DE 2088, AK TR02) | Y | Employer loads | Y (pmr true) | N | US-AZR3-002, US-CAS5-016, US-AKP51-006
Inbound: IRS lock-in letters | not written | - | - | - | RQ-01 (agent 2), non-blocking (F8 met by the three sourced inbound documents)
Mappers: insurance_type (19 labels), contract_type, benefit_type, correction_codes, filing_status_w4, personal_id_type | Y (scope labels; codes at DD) | DD / WTC | N | Y | `_*_basis` per mapper; reconcile at DD close (C27) and WTC close

## Open items carried (non-blocking)

- US-OWN-009 needs owner confirmation; MANDATE US-MQ-07 still reads '(owner to confirm the flag)'.
- package.issue_date 2027-03-31 is a planning placeholder. Rebuild with the script when the owner sets the date in build-manifest.package.
- RQ-01: IRS lock-in letters (agent 2).
- MA PFML return mechanics: ma.report.pfml.quarterly (agent 2).
- r3 findings 3-7, before RSPEC builds the affected specs. Finding 7 is taken at the next CCG touch.
- wage_type_categories and option_mapper_scope are re-checked against the WTC / DD real codes at their close.

The CCG post-pass change dc445c19 -> 2de2b30c was verified at r2; see `_qa/SCOPE-review-r2.json` `_ccg_post_pass_change`.

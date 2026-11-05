# P9-MERGE: register consolidation, 2026-11-01

Pass by agent 2, register work only (no web). Input: `legal-basis-register.csv` (1,161 rows), shards `mandate-P9-levy-r1/r2.csv` and `mandate-P9-lang-r1/r2.csv`, MANDATE.md "Seal assessment (attempt 5)" items 1-8. MANDATE.md and build-manifest.json not edited.

**Method.** Same as earlier merges: shard rows appended in shard order (levy-r1, levy-r2, lang-r1, lang-r2) under the unchanged 20-column header; existing rows edited field by field in place, never reordered. The file was parsed and re-written with Python csv (LF, no BOM); the round-trip of the untouched file was byte-identical before any edit. Every note added to an existing row goes at the end of `figure_or_rule_carried`, prefixed `[P9-MERGE 2026-11-01]`. Backup of the pre-merge file: session scratchpad `register-before.csv`.

**Before/after diff (mechanical).** 1,161 rows before, 1,300 after (137 shard rows plus US-OWN-006 and US-OWN-007). 84 pre-existing rows changed, every one in the edit log, with no unlogged change. Fields touched on old rows: status 55, figure_or_rule_carried 55, effective_to 28, tier 24, local_file 2, supersedes 2, id 1. All rows have 20 columns and the ids are unique. Status after: active 1,003, superseded 142, MANUAL 110, gated 27, partial 10, historical 6, provisional 1, not_applicable 1. Tier after: A.2 781, A.1 330, A.3 98, B 56, C 28, owner 7. No tier-B row is left `active` or `partial`.

## 1. Rows merged (137)
| Shard | Rows | Status |
|---|---|---|
| mandate-P9-levy-r1.csv | 44 (US-xxP9V-nnn) | 36 active, 8 partial |
| mandate-P9-levy-r2.csv | 26 (US-xxP9W-nnn) | 23 active, 3 partial |
| mandate-P9-lang-r1.csv | 55 (US-xxP9L-nnn) | 52 active, 3 partial |
| mandate-P9-lang-r2.csv | 12 (US-xxP9M-nnn) | 11 active, 1 partial |

There were no id collisions and every `supersedes` target resolves. Separators `"; "` were normalised to `;`.

## 2. Rows superseded by the merge (34 distinct; status=superseded, effective_to=2026-11-01)
- **Tier-B absence rows (P9-LEVY table):** US-MEL-003 (by US-MEP9V-001), US-MIL-003 (by US-MIP9V-001), US-MOL-002 (by US-MOP9V-002), US-NCL-002 (by US-NCP9V-001/-002), US-NDL-002 (by US-NDP9V-001), US-NEL-002 (by US-NEP9V-001).
- **P7 rows:** US-ARP7-001, US-HIP7-001, US-LAP7-001, US-MOP7-003, US-MOP7-004, US-RIP7-002, US-UTP7-002, US-VAP7-001, US-NYP7-005, US-WAP7-006, US-DEP7-004, US-DEP7-005, US-GAP7-001, US-KYP7-002, US-WYP7-002.
- **P9 r1 rows replaced by r2:** US-CTP9V-002, US-GAP9V-001, US-GAP9V-002, US-NHP9V-001, US-VAP9V-001, US-UTP9V-002, US-IAP9V-002, US-AKP9V-002, US-MOP9V-001, US-GAP9L-002, US-OHP9L-001, US-NJP9L-001.
- **Language:** US-GAL-001 (by US-GAP9L-001).

## 3. Defect fixes (seal attempt 5)
| # | Row(s) | Fix |
|---|---|---|
| 1 | US-NYP7-002 | Removed the "GAP: DFS page 403; confirmed on search excerpts" note. A note now points to US-NYP8-001 (DFS 2026 decision page quoted: 0.432%, max 411.91). Status stays active. |
| 2 | US-WVP7-001 | active -> **partial**. The row cites no local file, and no copy of SB 1053 (2026) is held: pdfs/WV has 21A-5-5 only as a 2025 pre-amendment Wayback copy. So the "7 points vs 7% relative" ambiguity cannot be settled from local evidence. |
| 3 | US-VTP9-001 | tier A -> **A.1** (Code of Vermont Rules: regulation text in the official compilation). |
| 3 | US-NHP9-001 | tier A -> **A.3** (NHES Employer Handbook: official employer guide, procedure). |
| 3 | US-INP52-002 | tier D -> **B** (law-firm and press summaries). It was already named in `supersedes` of US-INR3-005 (A.2, active), so status MANUAL -> superseded. |
| 3 | US-OWN-001..007 | tier `owner` kept. It is outside the enum {A.1, A.2, A.3, B, C}, but it is the established marker for decision rows, so changing it is a scaffolder/contract decision. **Flagged, not changed.** |
| 4 | Tier-B `active`/`partial` rows (47 at start) | 6 superseded by the merge (section 2). 3 -> **historical** as duplicates of A.2 rows on the same document: US-MEL-002 (= US-MEP51-001 and US-MEP7-001/-002, same Maine DOL 2026 rate PDF), US-MTL-002 (= US-MTP7-001), US-NHL-002 (= US-NH-006). 21 had their **tier label corrected** to the grade the register gives the same source, where another row read that source directly; status unchanged (see 4a). 17 -> **MANUAL** (see 4b). |
| 6 | US-UTP51-001 | tier B -> **A.2**. The source is the US DOL WHD state prevailing-wage page, graded A.2 and read in full in US-INR3-005 (also US-IDR3-003, US-NMR3-003). Status stays active. |
| 5 | US-NJP52-001 | Added to `supersedes` of US-NJP8-001; status -> superseded, effective_to 2026-11-01. Its own outdated link to US-NJ-003 is now moot. |
| 5 | US-NHR3-001 | Added to `supersedes` of US-NHP8-001; status -> superseded, effective_to 2026-11-01. |
| 7 | WebFetch-saved PDFs | See 3c. |

**4a. Tier B -> A (21), status unchanged.**
- DOL WHD prevailing-wage page (peer US-INR3-005), -> A.2: US-PAP51-006, US-OHP51-003, US-GAP51-002, US-NCP51-004, US-LAP52-004, US-IAP51-001, US-UTP51-001, US-OKP51-001, US-ARP51-001, US-MSP51-001.
- DOL WB featured-paid-leave page (peer US-FEDP51-011), -> A.2: US-OHP51-004, US-GAP51-003, US-NCP51-005, US-MIP51-008, US-IAP52-004, US-UTP52-006, US-OKP52-005, US-ARP52-007, US-MSP52-006.
- DOL WB History of Paid Leave PDF (peers US-KYR3-003, US-MOR3-001, US-WIR3-004), -> A.2: US-LAP52-002.
- AR DOL statutes compilation (peer US-ARL-001), -> A.1: US-ARP51-004.

**4b. Tier B -> MANUAL (17).** These are Justia mirrors, legislative research reports, a search-built locator, and summariser reads with no directly read A-graded peer:
US-MULTI-002, US-GAP52-001, US-GAP52-002, US-CTP52-001, US-KSP52-004, US-MSP51-006, US-IAP52-003, US-IAP52-005, US-UTP52-007, US-OKP52-003, US-OKP52-006, US-ARP52-004, US-ARP52-005, US-ARP52-008, US-MSP52-001, US-MSP52-004, US-MSP52-007.

Several are covered in substance by active P9 rows:
- GA 34-7-2: US-GAP9L-001.
- IA, AR, OK and MS revenue lists: the P9V/P9W rows of each state.

The scaffolder can re-point the citations.

**3c. WebFetch ruling (defect 7).** The binary was checked before applying the rule. In this build, a WebFetch-saved PDF is the authority's file itself: every one held locally starts with `%PDF-`, and US-VTP51-003's recorded md5 98672d93c1d27752c64867a0c1d3e7b5 re-computes exactly. So "original held locally" holds for all of them, and they are not downgraded. Applied:
- **US-VTP51-003: MANUAL -> active.** The official GB-1210-2026 PDF is held; the figures 0.44, 207.69 and 225.00 were found again in its text.
- **US-VTPIT-002, US-VAPIT-005, US-WVPIT-004 -> superseded** (effective_to 2026-11-01). None had a local file, and each is already named in `supersedes` of a row holding the official file: US-VTP51-003, US-VAP51-001 (Wayback copy, Rev. 10/26, figures 8,750/930/800/720/5.75 found again), and US-WVP51-005 (Wayback IT-100.2A March 2026, figures 38.46/76.92/83.33/2.11/28.14/4.58 found again).
- **local_file filled, status unchanged:** US-IAL-001 -> pdfs/IA/IowaCode-91A.6_2026-10-29.pdf; US-ORP51-002 -> ccg-sources/OR/OR-DOR_150-206-436_withholding-formulas_2026.pdf.
- **-> MANUAL (WebFetch-saved file not held anywhere in the build):** US-NDL-001, US-CTP51-002, US-CTP51-003, US-LAP51-003, US-ORP51-001.
- **Not changed, flagged:** US-HIP52-003 and other rows read only through the WebFetch summariser (e.g. US-MTP51-007), which have no saved file. The ruling as given covers saved files, so these were left for a separate decision.

## 4. Renames
- `US-UTP51-001-dup1` -> **`US-UTP51-006`** (Utah Pub 14 Rev. 04/26; content unchanged; 006 was free across the register and all shards). There are still references to the old id in MANDATE.md line 1244 (seal-assessment text) and build-manifest.json line 5081 (defect list). They were not edited (scaffolder files).

## 5. Owner-decision rows added
- **US-OWN-006** (US-MQ-03), **US-OWN-007** (US-MQ-05 limb c). Same columns as US-OWN-001..005: domain governance, instrument_type owner_decision, tier `owner`, status active, consumed_by MANDATE. local_file is `Research Pipeline/USA/PLANO-ATE-O-FIM.md` (rule 1, line 8, read). The decision text is verbatim from the instruction, followed by "Rests on:" and every P9L/P9M row (US-OWN-006) or P9V/P9W row (US-OWN-007) that is active or partial after the merge.

## 6. Checks
- **Validator:** `validate_contract.py build-manifest _pipeline/build-manifest.json` -> `ok ... PASS (1 file)` (jsonschema 4.26.0). Called with no schema name, the script prints a usage error.
- **P9 citations** (regex on every `US-...-nnn` id in P9-*.md, `..` ranges expanded; ", -002" shorthand not expanded). 0 unresolved.
  - P9-LANG: 116 active. 4 superseded (US-GAL-001, US-GAP9L-002, US-NJP9L-001, US-OHP9L-001), each cited as the row being replaced. 2 partial (US-GAP9M-001, US-MSL-001), both stated as partial in the text. 2 MANUAL:
    - US-MSP52-004 (Justia TOC, demoted in 4b; P9-LANG line 12 relies on it for "MS has no pay-statement statute").
    - **US-NDL-001** (WebFetch ruling; P9-LANG line 54 marks ND "closed" on it). The ND statute limb needs the NDCC ch. 34-14 PDF saved locally.
  - P9-LEVY: 45 active. 29 superseded, all in "supersedes X" or "old row" context. 1 MANUAL, US-MIP7-001, cited as MANUAL in the text. 2 partial, US-VAP9W-001 and US-WYP9W-001, both stated as partial.
- **MANDATE.md impact (for the scaffolder):** 26 rows that were active and are now not active are cited in MANDATE.md:
  - MULTI-002 x6, MEL-002, MEL-003, MIL-003, MOL-002, MTL-002, NCL-002, NDL-002, NEL-002.
  - GA-P5-2-001/002, CT-P5-1-002/003, LA-P5-1-003, OR-P5-1-001, CT-P5-2-001 x3, KS-P5-2-004.
  - IA-P5-2-003/005, UT-P5-2-007, OK-P5-2-003, AR-P5-2-005, MS-P5-2-001/004/007, WVP7-001.

  Re-point them to the active successors named above or reopen the limb.

## 7. Found, not fixed (outside this pass)
- About 60 `supersedes` links whose target is not `superseded`. Many are "refines" links pointing at a replacer that is gated or MANUAL (e.g. US-VAP51-001 -> US-VAPIT-005 was one, now fixed). There are also 24 free-text `supersedes` values that are not ids (e.g. "Rev. Proc. 2007-38", "US-OH-001 (adds file)"). A dedicated supersedes-hygiene pass should take them one by one; a bulk flip would wrongly supersede active A.1 rows (e.g. US-NJ-003, US-NHP52-002).
- 91 of the 92 rows that were already `superseded` have an empty `effective_to` (register convention up to now). Only rows superseded in this pass carry 2026-11-01.

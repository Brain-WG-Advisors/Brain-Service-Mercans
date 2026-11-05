# RELEASE - build log

## Round 2026-11-05 - C47 clean release (package 1.0, issue 2026-11-05)

Rules file: `_release/release_rules.json` (new). C47 must be run with `--config US-compliance/_release/release_rules.json`; without it the crosscheck does not load `legit` / `external_versions`.

Counts: before 433 findings in 14 files (373 "draft", 11 "amendment", 6 "corrected on", 5 "reissued", 1 "prior version", 23 "version != 1.0", 10 "stamp dates", 4 `[[FACT:` leftovers). After: **C47 PASS, 0 findings in 0 files** (26 files released, 25 docx/xlsx load with python-docx/openpyxl).

### Category (a) - domain usage, exempted in `crosscheck.legit` (rework words)
| Regex | Example match |
|---|---|
| `IRS early-release draft` | US-IRS-002 Form 944 Spec!T16 "...from the IRS early-release draft [US-FEDS...]" |
| `per 20\d\d draft` | Form 944 Spec!M23 "Per 2026 draft: read from the IRS early-release..." |
| `\(20\d\d draft\)` | US-IRS-007 File Structure!A9 "FORM 1094-C LINE MAP (2026 draft)" |
| `Form [0-9]+(?:-[A-Z]+)? for 20\d\d \(draft\)` | Form 943 Spec!M16 "Line 1 (Form 943 for 2026 (draft))" |
| `DRAFT, NOT ENACTED` | CCG "S. 1443 (introduced 2025-04-10, Senate Finance): DRAFT, NOT ENACTED - do not model" |
| `edition is an IRS draft, not citable` | CCG "the 2026 edition is an IRS draft, not citable." |
| `negotiable check, draft, money order` | CCG "US money, negotiable check, draft, money order, or electronic transfer" |
| `draft in House Revenue &(?:amp;)? Finance Committee` | CCG "draft in House Revenue & Finance Committee since 2025-06-17" |
| `official form draft` | SIR index "official form draft" |
| `form instructions draft` | SIR index "form instructions draft" |
| `corrected on Form (?:W-2c\|941-X)` | CCG "Wage statements are corrected on Form W-2c" |
| `corrected on a later Form 941` | US-IRS-008 Payroll Scope Summary "Never corrected on a later Form 941." |
| `corrected on the fourth-quarter return` | US-LOC-003 Population Rules!D3 |
| `their own amendment routes` | CCG "States have their own amendment routes" |
| `later amendment not checked` | CCG "2008 compilation; later amendment not checked." |
| `no later City amendment` | CCG "no later City amendment found" |
| `pre-amendment amount` | CCG "Fla. Stat. 448.110 still prints a stale pre-amendment amount" |
| `no 20\d\d amendment;` | CCG "no 2026 amendment; H0589/H0782/H0605 not enacted" |
| `proposed amendment to 40 TAC 815\.107` | CCG "TWC proposed amendment to 40 TAC 815.107" |
| `815\.107 amendment` | US-UI-001 Report Matrix!J70 "the adopted 40 TAC 815.107 amendment" |
| `the reissued formula` | CCG "apply the reissued formula" |
| `deduction amounts reissued each November` | CCG |
| `tables reissued as needed` | CCG |
| `handbook served is Rev\. \d+ though reissued yearly` | CCG "W-2 e-file handbook served is Rev. 20191219 though reissued yearly" |
| `Division \(A\) is unchanged from the prior version` | CCG (statute text, prior version of the code section) |

### Category (a) - external versions, exempted in `crosscheck.external_versions`
| Regex | Example match |
|---|---|
| `File Specification Toolkit (?:v\|version )\d+\.\d+\.\d+` | CCG / US-PFML-001 "CT Paid Leave File Specification Toolkit v2.1.9" |
| `Premiums-Toolkit-v\d+\.\d+-20\d\d` | US-PFML-001 Report Matrix!I37 "...Premiums-Toolkit-v25.1-2026.06.26.pdf" |
| `FSET v\d+\.\d+` | SIR index "SD 141, FSET v4.4" |
| `XML or CSV \(spec v\d+\.\d+` | US-UI-001 Report Matrix!H67 "XML or CSV (spec v1.6, 2023-10-25)" |
| `TAX-F\d{3} \(V20\d\d\.\d\)` | US-DOR-003 Report Matrix!C27 "MBT quarterly TAX-F003 (V2026.1)" |
| `carried to version \d+\.\d+ of the Data Dictionary as a change request` | 09-design L81 |

### Category (a) - external page/spec dates, reworded by `text_rules` (C47 has no exemption hook for "stamp dates"; meaning kept)
| Rule | Example |
|---|---|
| `\b(page\|spec) (?:last )?updated (20\d\d-\d\d-\d\d)` -> `\1 dated \2` | "DOLWD Wage and Hour page updated 2026-05-01" -> "page dated 2026-05-01"; US-UI-001 "(spec updated 2026-04-20)" -> "(spec dated 2026-04-20)" |
| `\((?:last )?updated (20\d\d-\d\d-\d\d)` -> `(dated \1` | CCG "Cookbook 2026 (updated 2025-12-04)" -> "(dated 2025-12-04)" |
| `tipped-employee definition changed (date) \(HB 185\)` -> `...changed by HB 185 (date)` | CCG Kentucky "changed 2026-04-10 (HB 185)" -> "changed by HB 185 (2026-04-10)" |

### Category (b) - real residue
- 4 `[[FACT:` tags in the CCG (annex DC `dc.minwage.tipped.cash_wage` note, annex LA `la.wh.std_deduction.joint` note). Cause: the note text began with "= ", and release.py skips any string starting with "=" (formula guard), so the FACT strip never ran; a text_rule cannot help for the same reason. Fixed at the source generator: `01-ccg/_scratch/annex-DC-MA/build_annexes.py` now writes a note opening with "= " as "Derived as ...". Rebuilt `build_annexes.py <BASE> DC,LA` (diff: exactly those 2 lines) and `_build/assemble/build_ccg_docx.py` (text diff vs previous docx: those 2 cells + build date 2026-11-04 -> 2026-11-05; 40,745 paragraphs/cells both sides).
- No review ids, "Corrected <date>" stamps, "now reads", "was:" or changelog wording were found in the release.

### New md5
| File | md5 |
|---|---|
| 01-ccg/US-CCG-001-v1.0.docx (source, was 333e8ee60a3d97a9b229b859c4f5da7c) | 20307cd395c7994bdc1f30e3d9d831c2 |
| 01-ccg/annexes/annex_DC.md | 90701a481a74e038c2b36f08ee63e12b |
| 01-ccg/annexes/annex_LA.md | 2a4fc8da9ec8b5de72812bf2cb4564da |
| 01-ccg/_scratch/annex-DC-MA/build_annexes.py | b6f1945382ada8f2900a4a5218acf96d |
| 10-release/01-ccg/US-CCG-001-v1.0.docx | f4620c721973594f97b18a5bdee5ae48 |

### GAP markers
release.py has no rule for `[[GAP:id]]`: the markers pass through verbatim (1,058 in 17 released files, e.g. "Not configured in this release [[GAP:RQ-550]]"). C47 does not flag them (it flags `RESEARCH-GAP` and `[[FACT:` only). No rule was added to hide them: they are the named open items of this release.

### Procedure note
The old 10-release subfolders were removed by absolute path and the release regenerated from scratch (26 files = release-manifest.json).

## Round 2026-11-05 r2 - REL-1 fix (QA re-check 5)
- Defect: the "= " -> "Derived as " rule in `build_annexes.py` (DC-MA) applied to every note, so a full rebuild also turned the FL SUI notes "= 378 per employee" / "= 7 per employee" (per-employee amounts at the 7,000 wage base, not derivations) into "Derived as ...". The delivered CCG had been built from DC,LA only, so a full rebuild (C71) differed by 4 lines.
- Fix: the rule is restricted to keys `dc.minwage.tipped.cash_wage` and `la.wh.std_deduction.joint`. `build_annexes.py` md5 303094c7bc230503baba0bbf2ca8b388.
- Full rebuild (`_build/common/rebuild_all.py`, all steps OK): every `modules/*.md` and `annexes/*.md` is byte-identical to the files before the rebuild. `annex_FL.md` unchanged, md5 5ddbb2a2d23ef6e2de9ad0e811d7c902 (QA's copy in `07-qa-crosscheck/_runclose/out/ccg71_rebuild/annex_FL.md` still has the 2 wrong "Derived as" notes; not touched).
- C71 (CCG): the freshly rebuilt docx and the kept docx have 0 text differences (python-docx paragraphs + table rows), and every zip part is identical except `docProps/core.xml` (build timestamp). Kept CCG: `01-ccg/US-CCG-001-v1.0.docx` md5 **20307cd395c7994bdc1f30e3d9d831c2**, unchanged from round 1.
- `_pipeline/tag_sync_check.py`: stale_or_unknown 0 in every section.
- Release regenerated into a cleared 10-release (26 files); C47 with `--config _release/release_rules.json`: PASS, 0 findings. Load test: 25 docx/xlsx open. Released CCG md5 f4620c721973594f97b18a5bdee5ae48 (same as round 1).

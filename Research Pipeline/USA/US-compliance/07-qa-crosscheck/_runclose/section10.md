
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

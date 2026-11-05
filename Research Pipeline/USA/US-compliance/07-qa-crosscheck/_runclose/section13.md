

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

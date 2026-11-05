

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

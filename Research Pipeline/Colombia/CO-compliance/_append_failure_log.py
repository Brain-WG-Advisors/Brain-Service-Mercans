from pathlib import Path

p = Path.home() / 'mercans-pipeline' / 'shared' / 'country_failure_log.md'
s = p.read_text(encoding='utf-8')

entry = """

---

## Colombia v2.4 (2026-09-07) — confirms F24, F25; adds F27 (C29 "todo" regression), F28 (C33 symbol misread)

Sixth country (after BH/OM/TN/CI/CG) to hit the **F24 + F25** shared-harness false positives. The CO
copy of `_audit_v24_mechanical.py` still carried the pre-v2.6 `check_c12` / `check_c20`, so both
reproduced exactly as logged. Both are now FIXED in the CO harness (see v2.9 notes below), together
with the C27 widening that the CG entry recommended.

- **F25 (C12 banner-row):** all 6 CO spec sheets carry a merged single-cell title banner on row 1 and
  the real 21-column header on row 2. Reading `max_row=1` scored 0-1/16 keywords and produced
  `6/6 specs have thin schema` = **FAIL** (thin_count > 2 escalates MANUAL to FAIL, so on CO this
  actually BLOCKED the gate rather than merely warning as on OM). Row 2 scores 13/16 on every spec.
  The 3 misses are labelling differences, not missing columns: `Query to RA` / `RA Comments` instead
  of `Error Code` / `Error Message`, and `Option Values` instead of `Code Table`.
- **F24 (C20 traceability):** semantic `filing_id` (`CO-DIAN-NE-MONTHLY-001`, `CO-PILA-MONTHLY-003`)
  vs sequence-number filenames (`CO-DIAN-001-NominaElectronica-Spec.xlsx`). All 6 in-scope filings
  already carried an explicit `spec_file` link in `scope_manifest.json` and all 6 resolve on disk.
- **Interpreter/env mismatch, worse form:** the audit also needs the country env injected
  (`CL_AUDIT_CODE`, `CL_AUDIT_COUNTRY`, `CL_AUDIT_LOCAL_LANG_SHORT`, `CL_AUDIT_CURRENCY`). Run bare,
  `CODE` defaults to `XX`, `BASE` resolves to `XX-compliance`, and **every** artifact check reports
  "missing" — a fully false BLOCKED that looks like catastrophic artifact loss. Run with `python`
  (has docx + openpyxl), not `python3`.

---

## F27 — C29 re-introduces the Spanish "todo" false positive that C8 had already fixed (v2.8 BUG)

**Source:** Colombia v2.4 pre-submission audit (Wallison Gomes, 7 Sep 2026)
**Observed:** C29 reported `CO-WTC-001-v1.0.xlsx[Wage Type Catalogue]: \\bTODO\\b` and **FAILed the
gate** (C29 is a deterministic FAIL). Inspection found 29 cells, every one the ordinary Spanish word
`todo`/`Todo` inside quoted statutory text — `todo` x27, `Todo` x2, and **zero** uppercase `TODO`.
Contexts: Labour Code art. 129 *"debe valorarse expresamente en todo contrato de trabajo"* (x25),
Law 1221 of 2008 *"En todo caso, los teletrabajadores..."*, Law 11 of 1984 art. 7 and the
occupational-risk affiliation rule *"Todo empleador que..."*, Decree 1072 of 2015 art. 2.2.6.3.3.4
par. 2 *"en todo caso la base de cotizacion..."*.
**Root cause:** `check_c29` (added in v2.8) scans with `_re.search(pat, text, _re.IGNORECASE)` over
`r'\\bTODO\\b'`. This is the *same* defect the harness docstring claims was already fixed one check
earlier — "C8 uses word-boundary regex (no false positive on Spanish 'todo' etc.)". C8 got the word
boundary but C29 added `IGNORECASE` on top of it, which re-opens the hole: the word boundary stops
`todos`, it does not stop `todo`. Guaranteed to fire in every ES/PT/IT country that quotes statute.
Chile v2.4 hit the same family ("a todo evento", Art. 164 CdT).
**Mitigation (this build):** C29 now matches markers that collide with a natural-language word
**case-sensitively**. `markers_re` became a list of `(pattern, flags)` pairs: `\\bTODO\\b` and
`\\bTodo\\s*:` at flags `0`; `TBD`, `FIXME`, `VERIFY No`, `[placeholder]`, `[CHECK]`, `[?]` keep
`IGNORECASE`. A real marker written `Todo:` is still caught, so detection strength is preserved.
**v2.9 fix:** port to the shared harness. General rule for this whole defect family: **an open-item
marker is an ALL-CAPS convention — never match one case-insensitively when the lowercase form is an
ordinary word in the country's language.**

---

## F28 — C33 "non-Latin script" test flags mathematical and typographic symbols (v2.9 BUG)

**Source:** Colombia v2.4 pre-submission audit (Wallison Gomes, 7 Sep 2026)
**Observed:** C33 reported `158 possible local-language passage(s) in CCG prose` and instructed the
content fixer to "translate to English". Every flagged sample was already a fully English sentence,
e.g. `"CO-CCG-001 . Version 1.0 . Fiscal Year 2026"`, `"NIT 902025831 -> DV 4"`,
`"The Technical Annex S1.1.1.1"`, `"round half to even, with a +-2.00 tolerance"`.
**Root cause:** `nonlatin_re` is a negated character class that excludes basic Latin, the Latin
accent blocks, whitespace, digits and a **hand-written list of punctuation**. Anything not on that
hand-list is treated as foreign script. Character-level analysis over all 7,292 CO CCG prose strings
showed the 170 flagged strings are triggered by exactly nine characters, none of them a letter in any
language: RIGHTWARDS ARROW U+2192 (x87), MINUS SIGN U+2212 (x33), SECTION SIGN U+00A7 (x31),
LESS-THAN OR EQUAL U+2264 (x29), MIDDLE DOT U+00B7 (x27), GREATER-THAN OR EQUAL U+2265 (x19),
PLUS-MINUS U+00B1 (x3), GREEK CAPITAL SIGMA U+03A3 (x1, in the NIT check-digit formula), ALMOST EQUAL
U+2248 (x1). The check self-describes as "a zero-false-positive signal", which is what makes it
dangerous: it invites the fixer to "translate" English prose. Note also that the code `continue`s
after a non-Latin hit, so the curated function-word branch never ran on any of the 158 strings —
the real language test was silently skipped on exactly the strings that were reported.
**Verification that no leakage existed:** the Spanish function-word branch, run separately over all
7,292 strings, returned **0 hits**; a broader ~90-word scan returned 16 candidates, all English
sentences caught on cognates ("social", "pension", "literal") or on correctly-introduced terms of art.
**Mitigation (this build):** replaced the punctuation blocklist with a Unicode **general-category**
test — a character is script leakage only if `unicodedata.category(ch).startswith('L')` and it falls
outside the Latin blocks (`ord < 0x0250`, or Latin Extended Additional `0x1E00-0x1EFF`). Symbols,
punctuation, marks and digits can never trigger it. A short whitelist covers Greek letters used as
mathematical notation (Sigma, Pi, Delta, mu, sigma, ...). **Regression-tested both ways:** all nine CO
symbol cases now read clean, while Bulgarian Cyrillic, Arabic, Japanese and Greek *prose* are still
flagged, and Latin-accented terms (`Liquidacion de Aportes`, `Sao Paulo`, `Koln`, `Angstrom`) read
clean.
**v2.9 fix:** port to the shared harness. General rule: **detect script by Unicode letter category,
never by a punctuation blocklist** — a blocklist can only ever be as complete as the last document
that was tested against it.

---

## C27 widening implemented (closes the CG v2.4 recommendation)

The CG entry recommended "widening C27's DERIVED classifier (recognize `min(`/`max(`/`count(`/
arithmetic and dotted master-data paths) and giving C27 the same banner-row offset handling as C12".
Implemented on CO. C27 flagged 476 mappings; column L genuinely *is* `System Mapping`, but the check
requires a whole DD cell string (>4 chars) to appear as a substring of the mapping text, and the two
sides use different naming conventions — the DD names fields in prose (`Employee Document Type`)
while specs use dotted identifiers (`Employee.Document_Type`). Under an alphanumeric-only
normalisation, **459 of 465 non-header values (98%) resolve**. `min_row=2` also read the banner-offset
header row as data (6 of the 476 were the literal header cell `"System Mapping"`). Post-fix the count
is 230, all genuinely derived/structural: `Payroll.*` engine results (158), `Mercans.*` pipeline
configuration (69), cross-field arithmetic (3). Left as MANUAL by choice — auto-accepting the
`Payroll.*` namespace would let a genuinely unmapped payroll field pass silently.

---

## Log change history (continued)

| Version | Date | Author | Change |
|---|---|---|---|
| 2.9-draft | 7 Sep 2026 | Wallison Gomes | F24 + F25 + interpreter/env mismatch reproduced on CO v2.4 (6th country); F27 (C29 Spanish "todo" regression) and F28 (C33 symbol misread) added; C12/C20/C27/C29/C33 fixes implemented in the CO audit harness |
"""

if 'F27 — C29 re-introduces' in s:
    print('already appended; nothing to do')
else:
    p.write_text(s.rstrip() + entry, encoding='utf-8')
    print('appended %d chars to %s' % (len(entry), p))

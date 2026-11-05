# PRECHECK (next artifacts) - 2026-11-03, agent 2

Tool: copy of rspec-r2-fix/selfcheck (work/selfcheck.py, textcache.py; r2 defects fixed: number-word regex now ``..``; numeric values also matched as v*100 and v/100; bindings filter dropped so every fact is checked). Every text element (form ids, channels, dates, quarters, numbers, units, acronyms) of each value must appear in the local copy of `register_id` or `_also_register_ids`.

| file | elements checked | misses before | misses after | keys with miss before -> after | still no local copy |
|---|---|---|---|---|---|
| DD-8_sheets-facts.json | 207 -> 207 | 21 | 6 | 15 -> 6 | 0 elements |
| WTC-global_baseline-facts.json | 293 -> 293 | 43 | 14 | 14 -> 5 | 0 elements |
| WTC-country_specific-facts.json | 1406 -> 1406 | 160 | 82 | 99 -> 64 | 2 elements |
| SIR-facts.json | 947 -> 946 | 154 | 56 | 74 -> 39 | 10 elements |
| PSL-facts.json | 370 -> 370 | 42 | 17 | 28 -> 16 | 2 elements |

Total misses 420 -> 175. Remaining by kind: {'word': 60, 'num': 57, 'form': 21, 'chan': 14, 'iso': 1, 'numv': 22}.

## Changes

1. **41 copy-less register rows got a local copy** (`00-official-sources/precheck-copies/<id>.html|pdf`, 16 MB total, re-downloaded from the row URL; register `local_file` filled under facts.lock; 6 stub pages (403/Cloudflare/404) discarded and left empty: US-MAP51-007, US-NYP51-003, US-TNR3-002, US-OH-002, US-OHR3-001, US-NCW1B-003). Still blocked (403/429/no response): US-COP52-003, US-KYP52-002, US-MIL-001, US-MOP52-008, US-MOP7-001, US-MOP7-002, US-ORL-001. Note: copies are the page as of 2026-11-03, not the date the row was first read; Wayback rows were not re-fetched.
2. **Re-point to the row that carries the element** (same jurisdiction only; forms, dates, quarters, distinctive numbers, acronyms of 4+ letters): the row id was appended to `_also_register_ids` and a `_figure_located` string (copy file, page, quote) was written. Counts: DD 6, WTC-global 12, WTC-country 46, SIR 44, PSL 7 elements. register consumed_by got 55 new tokens.
3. **Re-sync with CCG (approved reference) and latest RSPEC facts**, same key + same effective_from: `effective_to` aligned (WTC-global 23, WTC-country 94, mostly CCG 2026-12-31 on annual figures); `register_id` aligned to CCG (WTC-global 1, WTC-country 25; the previous row is kept in `_also_register_ids` and in `_precheck_prev_register_id`); SIR 1 value aligned to RSPEC (`rspec.mn.pfml_qtr.form`, DEED now spelled out; old text in `_precheck_prev_value`). Values of all other shared keys already equal. Not in the reference with that date (left as is, WTC carries an extra year): ga.sui.new_employer.rate.contribution 2026-01-01, ma.pfml.total.rate 2027-01-01, ma.pfml.rate.total.under_25 2027-01-01.
4. **No value was rewritten to copy wording** except the RSPEC sync above. Every element still missing is listed on its fact in `_precheck_unmatched` and one non-blocking `unresolved[]` entry `precheck.next.text_elements_unmatched` per file names them (what would close it: builder treats as our gloss, or agent 2 rewrites to copy wording / adds the carrying row; blocked rows need a browser-read copy).

## Residual (175 elements, 129 facts) - what they are

- Acronym expansions and our own glosses (FIT, FICA, FUTA, IRC, MFJ, DOR, POA, TPA, DOB, NOT, PFML, AGI...): not source wording.
- WTC rates stored as percent where the copy carries a different split or a derived figure (e.g. MA PFML medical 0.7 while the DFML page carries total 0.88; NJ/NY/PA/OR/UT small rates; oracle results 47.98, 91.27, 45.13, 75.36, 47.45 whose worked-example copies are scans or tables not in the cached text).
- Worked-example/arithmetic elements in method strings (OH, SC, MT, WV tables) whose row is a form PDF with image tables; need OCR of the cited pages.
- Elements whose cited row has no copy (blocked pages above).

Full per-element list: `work/after.json` (misses[]); before: `work/before.json`. Backups of the five facts files and the register: `_backup/`. Validation: validate_contract.py facts = PASS on all five files.

Accuracy statement: the check proves presence of tokens in the cached copy, not meaning; re-pointed rows were accepted on token match within the same jurisdiction and have not been read in context.
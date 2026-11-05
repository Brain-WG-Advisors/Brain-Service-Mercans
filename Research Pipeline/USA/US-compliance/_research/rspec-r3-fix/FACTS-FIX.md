# RSPEC r3 blockers 1-3: citation fix (2026-11-03, agent 2). No value changed.
Lock: `_research/facts.lock` (no pre-existing lock; taken, released). Backups: `_pipeline/_backup/register-pre-rspec-r3fix-2026-11-03/` (register + 4 facts files); md5 before: `MD5-BEFORE.txt`.

## Quotes (local copy opened)
- US-AZB5-006 (`ccg-sources/AZ/AZ_DES_UI-operating-fund_2026-11-02.txt`, line 19): "Bulk Filers: Azure / File Transfer Submission will identify the new UIOF line item." Same line in US-AZB5-402 (`AZ_DES_UIOF_browser_2026-11-02.txt`, line 24); only 006 added (006 already lists RSPEC, 402 does not; the bulk clause is the same).
  Caveat: the line names the bulk-filer route "Azure / File Transfer Submission"; it does not use the words "bulk file transfer" as a filing-method sentence.
- US-ILS5-011 (`ccg-sources/IL/IDOR_IL-941-instr_2026-11-02.pdf`, text extracted with pypdf): "MyTax Illinois ... an IDOR-approved tax-prep software program (software you develop or purchase off-the-shelf) to file electronically".
- US-FEDR2-004 (`ccg-sources/FED/FED_USC-26-3111_govinfo-2024_2026-11-02.htm`, line 22): "(c) Relief from taxes in cases covered by certain international agreements".

## Keys changed (added `_also_register_ids`, value untouched)
| file | key | added |
|---|---|---|
| RSPEC-facts.json | rspec.az.ui_qtr.form | US-AZB5-006 |
| RSPEC-facts.json | rspec.il.wh_return.form | US-ILS5-011 |
| CCG-annex_FED-facts.json | fed.fica.totalization.exemption_rule | US-FEDR2-004 |
| CCG-m05_social_security-facts.json | same | US-FEDR2-004 |
| WTC-global_baseline-facts.json | same | US-FEDR2-004 |
Register: US-FEDR2-004 consumed_by + `;RSPEC` (US-AZB5-006 and US-ILS5-011 already had RSPEC). Only that one cell differs from the backup.

## Validator
`validate_contract.py facts <file>`: PASS on all 4 files.

## C71
FAIL, 20 files, 3 differences: US-DOR-001 M59, US-IRS-001 M20, US-UI-001 M33 (exactly the three cells that will now cite the added ids). Expected: the issued workbooks pre-date the facts change; the builder must regenerate and re-issue the 3 workbooks (and re-sync CCG annex_FED / WTC / m05 tags if they print the cited ids). After re-issue C71 should return 0.

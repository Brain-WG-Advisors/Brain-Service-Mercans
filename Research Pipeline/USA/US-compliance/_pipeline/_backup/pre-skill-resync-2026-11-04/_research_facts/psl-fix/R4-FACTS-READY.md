# PSL fix R4 (2026-11-04)
QA2-02, route (b) for both: neither copy proves absence (LA copy is R.S. 23:631 only; MS is an A.3 posters page), so no neutral absence statement is possible.
- psl.la.statement.scope, psl.ms.statement.scope: value limited to what the copy shows, no pipeline wording; `_limitation: true`; each added to unresolved[] with what would close it.
- Builder: print the gap for LA and MS, not a rule. Backup _backup2/PSL-facts.json.pre-R4; lock released; ledger line added; validate_contract --all PASS (102 files).

STATUS: COMPLETE

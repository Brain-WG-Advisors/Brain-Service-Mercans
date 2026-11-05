# Facts fix 2 (2026-11-04)
Changed key: sc.sit.act110_rates.level (WTC-country_specific-facts.json) -> "assessment only for 2026 (1.99/5.21%); not in the 2026 withholding tables".
Sweep of all _research/*-facts.json "value" fields for journal/orchestrator/agent 2/triage/precheck: no other value hit. Non-value fields (note, why, what_would_close_it) still carry such wording (e.g. WTC notes "journal trap", dc.sit.method.2026 why); not changed, underscore fields untouched.
Backup: _research/la-fix/_backup2/. Lock taken and released. Ledger line added. validate_contract --all PASS.

STATUS: COMPLETE

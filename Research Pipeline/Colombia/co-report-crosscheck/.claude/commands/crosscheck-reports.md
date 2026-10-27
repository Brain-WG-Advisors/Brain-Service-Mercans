Run the full cross-check of the 6 Colombia specs against the client's real reports. Talk to Wallisson in Portuguese; write every file in English.

1. Check `03-client-reports-masked/` has files. If empty, tell Wallisson to run `bash scripts/00_setup.sh` and `python3 scripts/mask_reports.py` first, and stop.
2. Read `04-output/pii-check.txt` (written by the masking script). If it lists suspected personal names, show them to Wallisson and STOP until he confirms they are not personal data.
3. Run `python3 scripts/profile_reports.py` and `python3 scripts/spec_inventory.py` (both write to `04-output/`).
4. Run the `report-classifier` subagent. Show Wallisson the resulting map (report → spec → role) in a short table.
5. Run the `spec-crosschecker` subagent IN PARALLEL, one instance per spec: CO-PILA-003, CO-DIAN-001, CO-DIAN-002, CO-DIAN-004, CO-DIAN-005, CO-CESANTIAS-006.
6. When each finishes, run the `crosscheck-verifier` subagent for that spec (in parallel).
7. Run `python3 scripts/build_crosscheck_workbook.py` → `04-output/CO-SPECS-vs-CLIENT-REPORTS-CROSSCHECK.xlsx`.
8. Answer Wallisson in Portuguese: per spec the verdict counts and the verifier agreement rate; the corrections that change what development builds (missing fields, wrong formats, conflicts); the client reports with no statutory spec (decision needed: build as client-specific report or out of scope); anything still needing his decision. Then draft, in English, the status e-mail to Manju and Cinthya in the same format as the 14 Oct minutes (status per artifact, what is pending and with whom). Do not mark any spec approved and do not edit any spec.

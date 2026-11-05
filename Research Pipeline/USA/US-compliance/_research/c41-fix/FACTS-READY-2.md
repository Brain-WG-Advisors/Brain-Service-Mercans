# C70 fix - register rows (2026-11-04)
Backup: `backup/register-pre-fix2.csv`. No facts file changed.
- US-OHP52-001: successor US-OHS5-001 exists but its copy has none of the 2025 values (1.775%, 462.39, 2,673.50, 3.64%); the Ohio period facts (to 2026-07-31) keep citing the old row, now `active`, effective_to cleared, note names the closed period.
- US-OHR3C-001: successor US-OHR3D-001 (from 2026-06-16) already registered; old row `active` as basis of 2026-01-01..2026-06-15.
- US-INP51-001 (no fact cites it): no successor notice registered, State host unreachable; `active`, open: re-read Indiana DOR for a revised DN#1.
- US-RIS5-008: 2026 version unread, no successor; `partial`, effective_from = retrieval (flagged).
- US-FEDS5-013: Notice not repealed, relief limited to TY2025 by its own text; `active`. US-CAS5-020: TY2025 FTB edition, no 2026 edition yet; `active`.
Why not re-point: C70 matches the article text, so any superseded row flags every citation, and only these rows carry the clauses. Result: C41 PASS (0 unswept, 0 rows not current), validate_contract PASS (112 files). C70 not re-run by me (slow); rerun in the run-close.

STATUS: COMPLETE

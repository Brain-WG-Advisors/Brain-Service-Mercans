# C41 fix - facts ready (2026-11-04)

Changed keys (RSPEC-facts.json, backup in `backup/`):
- `rspec.fed.form940.due`: new successor period from 2026-02-11 ("TY2025 rule applies until the 2026 Form 940 instructions are published"), confidence low, register US-FEDS5-031. Existing period and gap ids unchanged.
- `rspec.fed.futa.credit_reduction.states`: 2025 period effective_to moved 2025-12-31 -> 2026-02-10 (TY2025 return due 2026-02-02/10; the C41 expiry rule needs a successor inside the build year); new 2026 period from 2026-02-11: list not yet published, no numbers, re-read DOL OUI on/after 2026-11-10. Register US-FEDS5-009.
- Already carrying their change date as effective_from (no edit needed; builder must print the date): `rspec.me.wh_return.form` 2026-04-14, `sir.nj.withholding.agent_authorization` 2026-06-09, `sir.dc.withholding.agent_authorization` 2026-09-16, `sir.tx.ui.agent_authorization` 2026-03-13. New date to print: 2026-02-11 (form940 / credit reduction successors).

Register: 943 rows given effective_from/verified_on (basis flagged in verification_method), 20 closed superseded, US-GAS5-018 rejected, US-RIS5-008 superseded. Sweep: `00-official-sources/bulletin-sweep.json`.
Checks: validate_contract --all PASS (112 files); C40 PASS; C41 authorities unswept 0, register rows not current 0, facts expired 0; remaining C41 problem = 5 change dates not yet written in CCG/design (builder).
Limits: 20 State news pages were blocked to WebFetch and ~20 States were not attempted; entries say so (browser re-read pending).

STATUS: COMPLETE

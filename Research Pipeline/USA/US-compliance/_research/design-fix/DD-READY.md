# DD-READY (DD builder, 2026-11-04)
DD `05-data-dictionary/US-DD-001-v1.0.xlsx` rebuilt (145 elements: ID Information 11, Country Fields 134; 36 mappers). Backup: `_pipeline/_backup/dd-design-2026-11-04/`. RSPEC overlay unchanged, specs not rebuilt.

| DD Field Name (ID Information, legal entity block) | id | Mapper / type | Facts |
|---|---|---|---|
| Supplemental wage withholding method election | er.supplemental_wage_method | option mapper "Supplemental wage withholding method": 1 Flat rate (optional flat rate), 2 Aggregate (aggregate method); the mandatory rate over the annual threshold is not an option | fed.fit.supplemental.aggregate_method, fed.fit.supplemental.flat_rate, fed.fit.supplemental.mandatory_rate, fed.fit.supplemental.mandatory_threshold |
| State-assigned unemployment insurance rate | er.state_sui_rate | Decimal percentage, per State account (State and number from "State employer account State / programme / number"), effective-dated | none; limitation DD-RQ-11 (notice mechanism per State) in DD-research-request.json and gaps.json |

Checks: dd_lint 0 (tags 202), C46 period-aware 0, C70 PASS, C71 PASS, validate_contract --all PASS (108), open check 0 not clean, tag_sync: DD and RSPEC clean. Diff vs backup: only the 2 fields and the 2 mapper rows.

STATUS: COMPLETE

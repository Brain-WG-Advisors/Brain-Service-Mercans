# Colombia SCOPE LOCK-IN VALIDATION

You are validating the scope_manifest.json produced by the CCG agent.
This is a BLOCKING gate. The pipeline cannot continue unless validation passes.

## READ
1. Manifest: ~/mercans-pipeline/CO-compliance/scope_manifest.json
2. Schema:   ~/mercans-pipeline/shared/scope_manifest_template.json

## VALIDATE

Check 1 — file exists and is valid JSON.

Check 2 — every required section is present and non-empty:
  - employment_types (in_scope, out_of_scope, rationale)
  - authority_filings (in_scope with all required fields, out_of_scope with reasons)
  - wage_type_categories
  - option_mapper_scope
  - integrations (outbound, inbound, both)

Check 3 — every authority_filings.in_scope entry has:
  - filing_id, authority, frequency, format
  - integration_type (must be one of: inbound, outbound, both)
  - product_mapping_required (must be true or false, not null)

Check 4 — every integrations.inbound entry has product_mapping_required set.
WARN if any inbound integration has product_mapping_required=false (F8 risk).

Check 5 — no code appears in both in_scope and out_of_scope for the same mapper.

Check 6 — known_failure_patterns_to_check is populated with F1-F15.

## OUTPUT
Print PASS or FAIL: <reason> as the FINAL LINE of your response.
If FAIL, list every problem found.
Save full report to: ~/mercans-pipeline/CO-compliance/07-qa-crosscheck/scope_validation.md

v2.8 (B7): in scope_validation.md, record EACH scope decision as a row —
DECISION | IN-SCOPE | OWNED-UPSTREAM | INBOUND-DATA-CONTRACT | REVERSIBLE(Y/N) | BASIS.
For any covered income type, missing non-resident handling is a blocking finding (B1).

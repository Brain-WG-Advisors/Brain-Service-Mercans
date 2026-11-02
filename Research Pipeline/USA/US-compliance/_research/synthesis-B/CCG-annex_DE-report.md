# Synthesis B report — CCG / annex_DE (Delaware)

- Date: 2026-11-02
- Facts written: 69
- Unresolved: 9 (blocking 1)
- Files: `_research/CCG-annex_DE-facts.json`, `_research/CCG-annex_DE-research-pack.md`
- Validator: `python ~/mercans-pipeline/shared/schemas/validate_contract.py facts _research/CCG-annex_DE-facts.json` → rc=0

```
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_DE-facts.json   [facts.schema.json]
PASS  (1 file)
```

## Register ids consumed (append `CCG/annex_DE` to consumed_by at final merge) — 31

US-DEP52-001; US-DEP52-002; US-DEL-001; US-DEL-002; US-DEL-003; US-DEP7-001; US-DEP9L-001; US-DEP9V-001; US-DES5-001; US-DES5-002; US-DES5-003; US-DES5-004; US-DES5-005; US-DES5-006; US-DES5-007; US-DES5-008; US-DES5-009; US-DES5-010; US-DES5-011; US-DES5-012; US-DES5-013; US-DES5-014; US-DES5-015; US-DES5-016; US-DES5-017; US-DES5-018; US-DES5-019; US-DES5-020; US-DES5-021; US-DES5-022; US-MULTI-019

## Number-in-row warnings (value not found literally in the row text; reviewed by the worker)

- de.sui.employee.rate=0 not literally in US-DES5-011: Quarterly UI: Forms UC-8 (tax report) and UC-8A (wage report) each quarter, gross and taxable wages, due by the end of the month after the quarter with payment;

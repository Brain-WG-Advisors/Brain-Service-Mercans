# Synthesis-B report - CCG annex_NJ (New Jersey)

Worker MN-WY, 2026-11-02.

- Facts written: 60 (`_research/CCG-annex_NJ-facts.json`)
- Facts pending only because of the register_id pattern defect: 13 (`_facts_pending_register_id_pattern`)
- Unresolved: 12 (1 blocking)
- Research pack: `_research/CCG-annex_NJ-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-NJR3-003=MANUAL, US-NJS5-013=partial

## Register ids consumed (for the merge worker: append `CCG/annex_NJ` to consumed_by)

US-NJ-P5-1-001; US-NJ-P5-1-002; US-NJ-P5-1-004; US-NJ-P5-1-007; US-NJP6-001; US-NJP6-002; US-NJP8-001; US-NJS5-001; US-NJS5-003; US-NJS5-004; US-NJS5-006; US-NJS5-007; US-NJS5-008; US-NJS5-009; US-NJS5-010; US-NJS5-011; US-NJS5-012; US-NJS5-015; US-NJS5-017; US-NJS5-018; US-NJS5-020; US-NJS5-021; US-NJS5-022; US-NJS5-023; US-NJS5-024

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_NJ-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_NJ-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

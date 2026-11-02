# Synthesis-B report - CCG annex_ND (North Dakota)

Worker MN-WY, 2026-11-02.

- Facts written: 56 (`_research/CCG-annex_ND-facts.json`)
- Facts pending only because of the register_id pattern defect: 4 (`_facts_pending_register_id_pattern`)
- Unresolved: 6 (1 blocking)
- Research pack: `_research/CCG-annex_ND-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): none

## Register ids consumed (for the merge worker: append `CCG/annex_ND` to consumed_by)

US-ND-P5-1-003; US-ND-P5-2-001; US-ND-P5-2-002; US-NDS5-001; US-NDS5-002; US-NDS5-004; US-NDS5-005; US-NDS5-006; US-NDS5-007; US-NDS5-008; US-NDS5-009; US-NDS5-012; US-NDS5-013; US-NDS5-014; US-NDS5-015; US-NDS5-016; US-NDS5-017

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_ND-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_ND-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

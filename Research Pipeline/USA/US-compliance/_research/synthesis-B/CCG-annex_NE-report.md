# Synthesis-B report - CCG annex_NE (Nebraska)

Worker MN-WY, 2026-11-02.

- Facts written: 43 (`_research/CCG-annex_NE-facts.json`)
- Facts pending only because of the register_id pattern defect: 12 (`_facts_pending_register_id_pattern`)
- Unresolved: 8 (2 blocking)
- Research pack: `_research/CCG-annex_NE-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-NES5-008=partial, US-NES5-015=partial

## Register ids consumed (for the merge worker: append `CCG/annex_NE` to consumed_by)

US-NEP51-001; US-NEP51-002; US-NEP51-003; US-NEP51-004; US-NEP52-001; US-NEP52-002; US-NES5-001; US-NES5-002; US-NES5-003; US-NES5-004; US-NES5-006; US-NES5-007; US-NES5-009; US-NES5-010; US-NES5-011; US-NES5-012; US-NES5-013; US-NES5-014; US-NES5-017; US-NES5-018; US-NES5-019

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_NE-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_NE-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

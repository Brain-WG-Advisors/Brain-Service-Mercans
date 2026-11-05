# Synthesis-B report - CCG annex_NY (New York)

Worker MN-WY, 2026-11-02.

- Facts written: 58 (`_research/CCG-annex_NY-facts.json`)
- Facts pending only because of the register_id pattern defect: 1 (`_facts_pending_register_id_pattern`)
- Unresolved: 14 (3 blocking)
- Research pack: `_research/CCG-annex_NY-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-NY-011=superseded, US-NYS5-018=partial, US-NYS5-022=MANUAL, US-NYS5-023=MANUAL

## Register ids consumed (for the merge worker: append `CCG/annex_NY` to consumed_by)

US-NY-001; US-NY-008; US-NY-010; US-NY-013; US-NYP51-002; US-NYP8-001; US-NYP9V-001; US-NYS5-001; US-NYS5-002; US-NYS5-003; US-NYS5-004; US-NYS5-006; US-NYS5-007; US-NYS5-009; US-NYS5-010; US-NYS5-011; US-NYS5-012; US-NYS5-015; US-NYS5-016; US-NYS5-017; US-NYS5-019

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_NY-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_NY-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

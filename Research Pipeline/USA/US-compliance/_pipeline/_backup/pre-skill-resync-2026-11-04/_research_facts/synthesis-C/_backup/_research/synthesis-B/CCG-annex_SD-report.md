# Synthesis-B report - CCG annex_SD (South Dakota)

Worker MN-WY, 2026-11-02.

- Facts written: 30 (`_research/CCG-annex_SD-facts.json`)
- Facts pending only because of the register_id pattern defect: 4 (`_facts_pending_register_id_pattern`)
- Unresolved: 7 (1 blocking)
- Research pack: `_research/CCG-annex_SD-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-SD-002=superseded, US-SD-P5-2-002=superseded, US-SDS5-009=partial, US-SDS5-019=partial

## Register ids consumed (for the merge worker: append `CCG/annex_SD` to consumed_by)

US-SD-001; US-SD-P5-1-002; US-SD-P5-1-003; US-SD-P5-2-001; US-SDS5-001; US-SDS5-002; US-SDS5-003; US-SDS5-006; US-SDS5-007; US-SDS5-008; US-SDS5-011; US-SDS5-012; US-SDS5-013; US-SDS5-017; US-SDS5-018

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_SD-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_SD-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

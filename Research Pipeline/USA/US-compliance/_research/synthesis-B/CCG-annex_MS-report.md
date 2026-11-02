# Synthesis-B report - CCG annex_MS (Mississippi)

Worker MN-WY, 2026-11-02.

- Facts written: 45 (`_research/CCG-annex_MS-facts.json`)
- Facts pending only because of the register_id pattern defect: 2 (`_facts_pending_register_id_pattern`)
- Unresolved: 8 (1 blocking)
- Research pack: `_research/CCG-annex_MS-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-MSP51-006=MANUAL, US-MSP52-004=MANUAL, US-MSP52-006=MANUAL

## Register ids consumed (for the merge worker: append `CCG/annex_MS` to consumed_by)

US-MSP51-001; US-MSP51-004; US-MSP10-001; US-MSP9L-001; US-MSS5-001; US-MSS5-002; US-MSS5-003; US-MSS5-004; US-MSS5-005; US-MSS5-006; US-MSS5-008; US-MSS5-009; US-MSS5-010; US-MSS5-011; US-MSS5-012; US-MSS5-015; US-MSS5-016; US-MSS5-017; US-MSS5-018; US-MSS5-019

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_MS-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_MS-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

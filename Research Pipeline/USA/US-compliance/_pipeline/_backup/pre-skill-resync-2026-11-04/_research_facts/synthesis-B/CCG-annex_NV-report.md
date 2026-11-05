# Synthesis-B report - CCG annex_NV (Nevada)

Worker MN-WY, 2026-11-02.

- Facts written: 39 (`_research/CCG-annex_NV-facts.json`)
- Facts pending only because of the register_id pattern defect: 6 (`_facts_pending_register_id_pattern`)
- Unresolved: 9 (1 blocking)
- Research pack: `_research/CCG-annex_NV-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): none

## Register ids consumed (for the merge worker: append `CCG/annex_NV` to consumed_by)

US-NVP51-001; US-NVP51-002; US-NVR3-002; US-NVS5-001; US-NVS5-003; US-NVS5-004; US-NVS5-005; US-NVS5-006; US-NVS5-007; US-NVS5-008; US-NVS5-010; US-NVS5-011; US-NVS5-013; US-NVS5-014; US-NVS5-017; US-NVS5-019

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_NV-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_NV-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

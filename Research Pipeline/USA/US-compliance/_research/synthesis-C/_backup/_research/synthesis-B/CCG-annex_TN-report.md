# Synthesis-B report - CCG annex_TN (Tennessee)

Worker MN-WY, 2026-11-02.

- Facts written: 24 (`_research/CCG-annex_TN-facts.json`)
- Facts pending only because of the register_id pattern defect: 3 (`_facts_pending_register_id_pattern`)
- Unresolved: 11 (1 blocking)
- Research pack: `_research/CCG-annex_TN-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-TNR3-001=superseded, US-TNS5-015=MANUAL, US-TNS5-016=MANUAL

## Register ids consumed (for the merge worker: append `CCG/annex_TN` to consumed_by)

US-TN-001; US-TN-P5-1-002; US-TN-P5-2-001; US-TNR3-003; US-TNS5-001; US-TNS5-002; US-TNS5-003; US-TNS5-004; US-TNS5-005; US-TNS5-006; US-TNS5-007; US-TNS5-008; US-TNS5-009; US-TNS5-010; US-TNS5-011; US-TNS5-012

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_TN-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_TN-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

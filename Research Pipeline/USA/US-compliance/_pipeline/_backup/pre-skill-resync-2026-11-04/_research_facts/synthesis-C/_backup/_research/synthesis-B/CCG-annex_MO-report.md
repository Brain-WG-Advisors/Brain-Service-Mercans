# Synthesis-B report - CCG annex_MO (Missouri)

Worker MN-WY, 2026-11-02.

- Facts written: 45 (`_research/CCG-annex_MO-facts.json`)
- Facts pending only because of the register_id pattern defect: 11 (`_facts_pending_register_id_pattern`)
- Unresolved: 9 (1 blocking)
- Research pack: `_research/CCG-annex_MO-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-MOS5-014=partial

## Register ids consumed (for the merge worker: append `CCG/annex_MO` to consumed_by)

US-MO-P5-2-001; US-MO-P5-2-002; US-MO-P5-2-003; US-MO-P5-2-005; US-MO-P5-2-006; US-MOR3-001; US-MOS5-001; US-MOS5-002; US-MOS5-003; US-MOS5-004; US-MOS5-005; US-MOS5-006; US-MOS5-007; US-MOS5-009; US-MOS5-010; US-MOS5-011; US-MOS5-013; US-MOS5-016; US-MOS5-017; US-MOS5-020

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_MO-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_MO-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

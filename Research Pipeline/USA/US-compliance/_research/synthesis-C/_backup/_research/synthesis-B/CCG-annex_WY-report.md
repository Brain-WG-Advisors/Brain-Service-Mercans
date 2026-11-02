# Synthesis-B report - CCG annex_WY (Wyoming)

Worker MN-WY, 2026-11-02.

- Facts written: 24 (`_research/CCG-annex_WY-facts.json`)
- Facts pending only because of the register_id pattern defect: 9 (`_facts_pending_register_id_pattern`)
- Unresolved: 5 (2 blocking)
- Research pack: `_research/CCG-annex_WY-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-WYP9W-001=partial, US-WYP9W-002=partial, US-WYS5-010=partial

## Register ids consumed (for the merge worker: append `CCG/annex_WY` to consumed_by)

US-WY-P5-1-001; US-WY-P5-1-002; US-WY-P5-1-004; US-WY-P5-1-005; US-WY-P5-1-006; US-WY-P5-2-001; US-WYP9W-001; US-WYS5-001; US-WYS5-002; US-WYS5-003; US-WYS5-005; US-WYS5-006; US-WYS5-008; US-WYS5-009; US-WYS5-011; US-WYS5-012; US-WYS5-013; US-WYS5-014; US-WYS5-015; US-WYS5-016

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_WY-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_WY-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

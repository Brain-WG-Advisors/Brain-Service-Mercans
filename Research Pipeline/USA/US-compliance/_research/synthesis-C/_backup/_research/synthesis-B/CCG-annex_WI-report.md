# Synthesis-B report - CCG annex_WI (Wisconsin)

Worker MN-WY, 2026-11-02.

- Facts written: 43 (`_research/CCG-annex_WI-facts.json`)
- Facts pending only because of the register_id pattern defect: 13 (`_facts_pending_register_id_pattern`)
- Unresolved: 7 (1 blocking)
- Research pack: `_research/CCG-annex_WI-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-WIR3-005=MANUAL

## Register ids consumed (for the merge worker: append `CCG/annex_WI` to consumed_by)

US-MULTI-006; US-WI-P5-1-001; US-WI-P5-2-001; US-WI-P5-2-002; US-WIR3-001; US-WIR3-003; US-WIR3-004; US-WIS5-001; US-WIS5-002; US-WIS5-003; US-WIS5-004; US-WIS5-005; US-WIS5-006; US-WIS5-008; US-WIS5-009; US-WIS5-010; US-WIS5-011; US-WIS5-012; US-WIS5-013; US-WIS5-014; US-WIS5-016; US-WIS5-018; US-WIS5-019

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_WI-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_WI-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

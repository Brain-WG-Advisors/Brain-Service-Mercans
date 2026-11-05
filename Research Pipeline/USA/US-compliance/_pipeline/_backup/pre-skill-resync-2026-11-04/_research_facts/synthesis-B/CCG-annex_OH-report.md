# Synthesis-B report - CCG annex_OH (Ohio)

Worker MN-WY, 2026-11-02.

- Facts written: 50 (`_research/CCG-annex_OH-facts.json`)
- Facts pending only because of the register_id pattern defect: 2 (`_facts_pending_register_id_pattern`)
- Unresolved: 13 (2 blocking)
- Research pack: `_research/CCG-annex_OH-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-OH-014=gated, US-OHP51-002=superseded, US-OHP51-004=MANUAL, US-OHP52-001=superseded, US-OHS5-023=partial

## Register ids consumed (for the merge worker: append `CCG/annex_OH` to consumed_by)

US-MULTI-005; US-OH-002; US-OH-008; US-OH-009; US-OHP51-001; US-OHP52-006; US-OHP7-001; US-OHR3-002; US-OHS5-001; US-OHS5-002; US-OHS5-003; US-OHS5-004; US-OHS5-005; US-OHS5-006; US-OHS5-007; US-OHS5-008; US-OHS5-009; US-OHS5-010; US-OHS5-011; US-OHS5-012; US-OHS5-013; US-OHS5-015; US-OHS5-016; US-OHS5-017; US-OHS5-020; US-OHS5-021

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_OH-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_OH-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

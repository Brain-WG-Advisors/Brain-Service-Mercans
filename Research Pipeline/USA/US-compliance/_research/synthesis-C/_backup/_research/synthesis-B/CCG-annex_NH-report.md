# Synthesis-B report - CCG annex_NH (New Hampshire)

Worker MN-WY, 2026-11-02.

- Facts written: 41 (`_research/CCG-annex_NH-facts.json`)
- Facts pending only because of the register_id pattern defect: 1 (`_facts_pending_register_id_pattern`)
- Unresolved: 9 (1 blocking)
- Research pack: `_research/CCG-annex_NH-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-NHS5-012=MANUAL

## Register ids consumed (for the merge worker: append `CCG/annex_NH` to consumed_by)

US-NH-006; US-NH-P5-1-001; US-NHP7-001; US-NHP8-001; US-NHP9W-001; US-NHS5-001; US-NHS5-002; US-NHS5-003; US-NHS5-004; US-NHS5-006; US-NHS5-007; US-NHS5-008; US-NHS5-009; US-NHS5-010; US-NHS5-011; US-NHS5-013; US-NHS5-015

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_NH-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_NH-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

# Synthesis-B report - CCG annex_VA (Virginia)

Worker MN-WY, 2026-11-02.

- Facts written: 48 (`_research/CCG-annex_VA-facts.json`)
- Facts pending only because of the register_id pattern defect: 1 (`_facts_pending_register_id_pattern`)
- Unresolved: 8 (3 blocking)
- Research pack: `_research/CCG-annex_VA-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-VAP9W-001=partial

## Register ids consumed (for the merge worker: append `CCG/annex_VA` to consumed_by)

US-VASUI-001; US-VAR3-001; US-VAR3-002; US-VAR3-003; US-VAS5-001; US-VAS5-002; US-VAS5-003; US-VAS5-004; US-VAS5-005; US-VAS5-006; US-VAS5-007; US-VAS5-008; US-VAS5-010; US-VAS5-011; US-VAS5-013; US-VAS5-014; US-VAS5-015; US-VAS5-016; US-VAS5-018; US-VAS5-019; US-VAS5-021; US-VAS5-022

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_VA-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_VA-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

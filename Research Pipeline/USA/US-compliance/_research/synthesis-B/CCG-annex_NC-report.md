# Synthesis-B report - CCG annex_NC (North Carolina)

Worker MN-WY, 2026-11-02.

- Facts written: 46 (`_research/CCG-annex_NC-facts.json`)
- Facts pending only because of the register_id pattern defect: 3 (`_facts_pending_register_id_pattern`)
- Unresolved: 10 (2 blocking)
- Research pack: `_research/CCG-annex_NC-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-NCP51-005=MANUAL, US-NCW1B-002=superseded, US-NCS5-019=partial, US-NCS5-027=partial, US-NCS5-030=partial

## Register ids consumed (for the merge worker: append `CCG/annex_NC` to consumed_by)

US-NC-001; US-NC-002; US-NCP51-001; US-NCP51-004; US-NCW1B-003; US-NCP9V-001; US-NCS5-001; US-NCS5-002; US-NCS5-003; US-NCS5-005; US-NCS5-006; US-NCS5-008; US-NCS5-010; US-NCS5-011; US-NCS5-014; US-NCS5-015; US-NCS5-016; US-NCS5-018; US-NCS5-020; US-NCS5-021; US-NCS5-022; US-NCS5-025; US-NCS5-028; US-NCS5-029

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_NC-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_NC-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

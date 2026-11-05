# Synthesis-B report - CCG annex_WV (West Virginia)

Worker MN-WY, 2026-11-02.

- Facts written: 36 (`_research/CCG-annex_WV-facts.json`)
- Facts pending only because of the register_id pattern defect: 6 (`_facts_pending_register_id_pattern`)
- Unresolved: 11 (4 blocking)
- Research pack: `_research/CCG-annex_WV-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-WV-LAB-001=superseded, US-WV-P5-1-004=MANUAL, US-WV-P5-1-008=superseded, US-WV-P5-2-001=superseded, US-WV-P5-2-002=superseded, US-WV-P5-2-007=partial, US-WV-PIT-002=MANUAL, US-WVP7-001=partial, US-WVP7-003=MANUAL, US-WVR3-003=MANUAL, US-WVS5-015=partial

## Register ids consumed (for the merge worker: append `CCG/annex_WV` to consumed_by)

US-WIR3-004; US-WV-P5-1-005; US-WV-P5-1-009; US-WV-P5-2-004; US-WV-UI-001; US-WVR3-001; US-WVR3-002; US-WVS5-001; US-WVS5-002; US-WVS5-003; US-WVS5-004; US-WVS5-005; US-WVS5-006; US-WVS5-007; US-WVS5-008; US-WVS5-009; US-WVS5-010; US-WVS5-011; US-WVS5-012; US-WVS5-013; US-WVS5-015; US-WVS5-016

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_WV-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_WV-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

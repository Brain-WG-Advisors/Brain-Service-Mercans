# Synthesis-B report - CCG annex_PA (Pennsylvania)

Worker MN-WY, 2026-11-02.

- Facts written: 44 (`_research/CCG-annex_PA-facts.json`)
- Facts pending only because of the register_id pattern defect: 3 (`_facts_pending_register_id_pattern`)
- Unresolved: 11 (2 blocking)
- Research pack: `_research/CCG-annex_PA-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-PAP51-005=superseded, US-PAP52-001=MANUAL, US-PAS5-015=partial, US-PAS5-016=partial

## Register ids consumed (for the merge worker: append `CCG/annex_PA` to consumed_by)

US-PA-001; US-PA-009; US-PAP51-001; US-PAP51-003; US-PAP52-002; US-PAL-002; US-PAP7-005; US-PAS5-001; US-PAS5-002; US-PAS5-003; US-PAS5-005; US-PAS5-007; US-PAS5-008; US-PAS5-009; US-PAS5-010; US-PAS5-011; US-PAS5-013; US-PAS5-014; US-PAS5-015; US-PAS5-017; US-PAS5-019; US-PAS5-021; US-PAS5-022

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_PA-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_PA-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

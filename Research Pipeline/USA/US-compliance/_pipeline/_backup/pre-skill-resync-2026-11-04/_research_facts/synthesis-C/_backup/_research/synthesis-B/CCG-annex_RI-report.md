# Synthesis-B report - CCG annex_RI (Rhode Island)

Worker MN-WY, 2026-11-02.

- Facts written: 52 (`_research/CCG-annex_RI-facts.json`)
- Facts pending only because of the register_id pattern defect: 4 (`_facts_pending_register_id_pattern`)
- Unresolved: 8 (2 blocking)
- Research pack: `_research/CCG-annex_RI-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-RI-001=superseded, US-RI-002=gated, US-RI-006=superseded, US-RIS5-008=partial, US-RIS5-021=partial

## Register ids consumed (for the merge worker: append `CCG/annex_RI` to consumed_by)

US-RI-P5-1-002; US-RI-P5-1-003; US-RI-P5-2-001; US-RI-P5-2-003; US-RIP7-001; US-RIP9V-001; US-RIS5-001; US-RIS5-002; US-RIS5-003; US-RIS5-004; US-RIS5-005; US-RIS5-006; US-RIS5-007; US-RIS5-009; US-RIS5-010; US-RIS5-012; US-RIS5-013; US-RIS5-016; US-RIS5-017; US-RIS5-018; US-RIS5-019; US-RIS5-020

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_RI-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_RI-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

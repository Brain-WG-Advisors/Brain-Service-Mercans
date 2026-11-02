# Synthesis-B report - CCG annex_UT (Utah)

Worker MN-WY, 2026-11-02.

- Facts written: 22 (`_research/CCG-annex_UT-facts.json`)
- Facts pending only because of the register_id pattern defect: 22 (`_facts_pending_register_id_pattern`)
- Unresolved: 10 (2 blocking)
- Research pack: `_research/CCG-annex_UT-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-UTP52-006=MANUAL, US-UTPIT-001=MANUAL, US-UTPIT-004=superseded, US-UTL-001=gated

## Register ids consumed (for the merge worker: append `CCG/annex_UT` to consumed_by)

US-UTP51-001; US-UTP52-005; US-UTPIT-003; US-UTSUI-001; US-UTP6-001; US-UTR3-002; US-UTS5-001; US-UTS5-002; US-UTS5-003; US-UTS5-004; US-UTS5-005; US-UTS5-007; US-UTS5-011; US-UTS5-012; US-UTS5-013; US-UTS5-014

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_UT-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_UT-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

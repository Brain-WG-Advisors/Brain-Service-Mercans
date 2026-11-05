# Synthesis-B report - CCG annex_TX (Texas)

Worker MN-WY, 2026-11-02.

- Facts written: 29 (`_research/CCG-annex_TX-facts.json`)
- Facts pending only because of the register_id pattern defect: 4 (`_facts_pending_register_id_pattern`)
- Unresolved: 8 (2 blocking)
- Research pack: `_research/CCG-annex_TX-research-pack.md`
- Non-active ids cited in the stage-5 findings (not used for numbers): US-TXLAB-001=MANUAL, US-TXPIT-001=superseded, US-TXSUI-002=superseded, US-TXSUI-003=superseded

## Register ids consumed (for the merge worker: append `CCG/annex_TX` to consumed_by)

US-TXP52-001; US-TXSUI-001; US-TXSUI-006; US-TXR3-002; US-TXR3-003; US-TXS5-001; US-TXS5-002; US-TXS5-003; US-TXS5-004; US-TXS5-005; US-TXS5-006; US-TXS5-007; US-TXS5-008; US-TXS5-009; US-TXS5-011; US-TXS5-012; US-TXS5-013; US-TXS5-014; US-TXS5-019

## Validator output

```
$ python validate_contract.py facts _research/CCG-annex_TX-facts.json
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_TX-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

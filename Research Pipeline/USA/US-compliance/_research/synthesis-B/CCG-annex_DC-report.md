# Synthesis B report — CCG / annex_DC (District of Columbia)

- Date: 2026-11-02
- Facts written: 48
- Unresolved: 12 (blocking 2)
- Files: `_research/CCG-annex_DC-facts.json`, `_research/CCG-annex_DC-research-pack.md`
- Validator: `python ~/mercans-pipeline/shared/schemas/validate_contract.py facts _research/CCG-annex_DC-facts.json` → rc=0

```
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_DC-facts.json   [facts.schema.json]
PASS  (1 file)
```

## Register ids consumed (append `CCG/annex_DC` to consumed_by at final merge) — 40

US-DCP51-001; US-DCP51-002; US-DCP51-004; US-DCP51-006; US-DCP51-007; US-DCP51-014; US-DCP52-001; US-DCP52-003; US-DCP52-004; US-DCP52-005; US-DCP7-001; US-DCP7-003; US-DCR3-001; US-DCR3-002; US-DCS5-001; US-DCS5-002; US-DCS5-003; US-DCS5-004; US-DCS5-005; US-DCS5-006; US-DCS5-007; US-DCS5-008; US-DCS5-009; US-DCS5-010; US-DCS5-011; US-DCS5-012; US-DCS5-013; US-DCS5-014; US-DCS5-015; US-DCS5-016; US-DCS5-017; US-DCS5-018; US-DCS5-019; US-DCS5-020; US-DCS5-021; US-DCS5-022; US-DCS5-023; US-DCS5-024; US-DCS5-025; US-MULTI-016

## Number-in-row warnings (value not found literally in the row text; reviewed by the worker)

- dc.sui.employee.rate=0 not literally in US-DCS5-017: Table VI (used when the Fund is not above 0.8% of payrolls): 1.9% (reserve >= 8.0%) up to 4.4% (reserve 0.0-1.5%), then 6.2%, 6.5%, 6.8%, 7.1%, 7.4% (reserve <=
- dc.garn.creditor.weekly_threshold=736 not literally in US-DCS5-006: Creditor wage attachment limited to 25% of the amount by which weekly disposable wages exceed 40 x DC minimum hourly wage (CCPA uses 30 x federal minimum; DC pr

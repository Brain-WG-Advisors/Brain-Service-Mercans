# Synthesis B report — CCG / annex_MI (Michigan)

- Date: 2026-11-02
- Facts written: 55
- Unresolved: 9 (blocking 1)
- Files: `_research/CCG-annex_MI-facts.json`, `_research/CCG-annex_MI-research-pack.md`
- Validator: `python ~/mercans-pipeline/shared/schemas/validate_contract.py facts _research/CCG-annex_MI-facts.json` → rc=0

```
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_MI-facts.json   [facts.schema.json]
PASS  (1 file)
```

## Register ids consumed (append `CCG/annex_MI` to consumed_by at final merge) — 49

US-FED-011; US-MIP51-001; US-MIP51-002; US-MIP51-003; US-MIP51-004; US-MIP51-005; US-MIP51-006; US-MIP52-001; US-MIP52-002; US-MIP52-004; US-MIP52-005; US-MIP52-011; US-MIPIT-001; US-MIL-001; US-MIL-002; US-MIP9L-001; US-MIP9V-001; US-MIP9W-001; US-MIP9W-002; US-MIR3-001; US-MIR3-002; US-MIR3-003; US-MIS5-001; US-MIS5-002; US-MIS5-003; US-MIS5-004; US-MIS5-005; US-MIS5-006; US-MIS5-007; US-MIS5-008; US-MIS5-009; US-MIS5-010; US-MIS5-011; US-MIS5-012; US-MIS5-013; US-MIS5-014; US-MIS5-015; US-MIS5-016; US-MIS5-017; US-MIS5-018; US-MIS5-019; US-MIS5-020; US-MIS5-021; US-MIS5-022; US-MIS5-023; US-MIS5-024; US-MIS5-025; US-MIS5-026; US-MULTI-010

## Number-in-row warnings (value not found literally in the row text; reviewed by the worker)

- mi.wh.exemption.biweekly=226.92 not literally in US-MIS5-019: State certificate MI-W4 required; federal W-4 cannot substitute. Line 6 number of personal and dependency exemptions (cannot exceed MI-1040 entitlement); line 7
- mi.oracle.state.biweekly_2000_1ex=75.36 not literally in US-MIS5-019: State certificate MI-W4 required; federal W-4 cannot substitute. Line 6 number of personal and dependency exemptions (cannot exceed MI-1040 entitlement); line 7
- mi.oracle.detroit.resident_biweekly_2000=47.45 not literally in US-MIR3-002: Detroit 2026: employers with a location or doing business in Detroit withhold for Detroit residents (wherever they work) and for nonresidents whose predominant 
- CITED US-MIP51-008 status=MANUAL (narrative only)

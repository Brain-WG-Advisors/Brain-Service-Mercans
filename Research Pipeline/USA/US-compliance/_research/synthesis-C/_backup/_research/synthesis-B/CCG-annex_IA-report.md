# Synthesis B report — CCG / annex_IA (Iowa)

- Date: 2026-11-02
- Facts written: 45
- Unresolved: 9 (blocking 0)
- Files: `_research/CCG-annex_IA-facts.json`, `_research/CCG-annex_IA-research-pack.md`
- Validator: `python ~/mercans-pipeline/shared/schemas/validate_contract.py facts _research/CCG-annex_IA-facts.json` → rc=0

```
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_IA-facts.json   [facts.schema.json]
PASS  (1 file)
```

## Register ids consumed (append `CCG/annex_IA` to consumed_by at final merge) — 43

US-IA-001; US-IA-002; US-IA-P5-1-001; US-IA-P5-1-002; US-IA-P5-1-003; US-IA-P5-1-004; US-IA-P5-1-005; US-IA-P5-2-001; US-IA-P5-2-002; US-IAL-001; US-IAL-002; US-IAP9L-001; US-IAP9L-002; US-IAP9V-001; US-IAP9W-001; US-IAS5-001; US-IAS5-002; US-IAS5-003; US-IAS5-004; US-IAS5-005; US-IAS5-006; US-IAS5-009; US-IAS5-010; US-IAS5-011; US-IAS5-012; US-IAS5-013; US-IAS5-014; US-IAS5-015; US-IAS5-016; US-IAS5-017; US-IAS5-018; US-IAS5-019; US-IAS5-020; US-IAS5-021; US-IAS5-022; US-IAS5-023; US-IAS5-024; US-IAS5-025; US-IAS5-026; US-IAS5-027; US-IAS5-028; US-IAS5-029; US-MULTI-018

## Number-in-row warnings (value not found literally in the row text; reviewed by the worker)

- ia.sui.employee.rate=0 not literally in US-IAS5-024: Quarterly contribution and payroll report (Form 65-5300) with quarterly wage detail by SSN, filed electronically; contributions due the last day of the month fo
- ia.oracle.formula.example6.withholding=114.92 not literally in US-IAS5-005: T1 = G - D; T2 = T1 x 3.80%; T3 = T2 - W/P; T4 = T3 + A. D per period (2024+ IA W-4): col A Other / MFJ spouse with earned income / missing: annual 13,000 (week
- CITED US-IA-P5-2-004 status=MANUAL (narrative only)

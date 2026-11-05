# Synthesis B report — CCG / annex_AK (Alaska)

- Date: 2026-11-02
- Facts written: 48
- Unresolved: 9 (blocking 0)
- Files: `_research/CCG-annex_AK-facts.json`, `_research/CCG-annex_AK-research-pack.md`
- Validator: `python ~/mercans-pipeline/shared/schemas/validate_contract.py facts _research/CCG-annex_AK-facts.json` → rc=0

```
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_AK-facts.json   [facts.schema.json]
PASS  (1 file)
```

## Register ids consumed (append `CCG/annex_AK` to consumed_by at final merge) — 33

US-AK-P5-1-003; US-AK-P5-1-005; US-AK-P5-1-006; US-AK-P5-2-001; US-AK-P5-2-002; US-AK-WT-001; US-AK-WT-002; US-AKL-001; US-AKP7-001; US-AKP7-002; US-AKP9L-001; US-AKP9W-001; US-AKR3-001; US-AKR3-002; US-AKR3-003; US-AKS5-001; US-AKS5-002; US-AKS5-003; US-AKS5-004; US-AKS5-005; US-AKS5-006; US-AKS5-007; US-AKS5-008; US-AKS5-009; US-AKS5-010; US-AKS5-011; US-AKS5-012; US-AKS5-013; US-AKS5-014; US-AKS5-015; US-AKS5-016; US-AKS5-017; US-AKS5-018

## Number-in-row warnings (value not found literally in the row text; reviewed by the worker)

- ak.exempt.salary.weekly_min=1040.0 not literally in US-AKS5-001: Min wage 13.00 from 2025-07-01, 14.00 from 2026-07-01, 15.00 from 2027-07-01, then CPI-U Anchorage indexation calculated each 30 Sep for prior calendar year, ro
- ak.exempt.salary.weekly_min=1120.0 not literally in US-AKS5-001: Min wage 13.00 from 2025-07-01, 14.00 from 2026-07-01, 15.00 from 2027-07-01, then CPI-U Anchorage indexation calculated each 30 Sep for prior calendar year, ro
- ak.exempt.salary.weekly_min=1200.0 not literally in US-AKS5-001: Min wage 13.00 from 2025-07-01, 14.00 from 2026-07-01, 15.00 from 2027-07-01, then CPI-U Anchorage indexation calculated each 30 Sep for prior calendar year, ro

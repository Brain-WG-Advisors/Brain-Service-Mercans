# Synthesis B report — CCG / annex_KY (Kentucky)

- Date: 2026-11-02
- Facts written: 43
- Unresolved: 12 (blocking 1)
- Files: `_research/CCG-annex_KY-facts.json`, `_research/CCG-annex_KY-research-pack.md`
- Validator: `python ~/mercans-pipeline/shared/schemas/validate_contract.py facts _research/CCG-annex_KY-facts.json` → rc=0

```
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_KY-facts.json   [facts.schema.json]
PASS  (1 file)
```

## Register ids consumed (append `CCG/annex_KY` to consumed_by at final merge) — 43

US-KY-001; US-KY-002; US-KY-003; US-KY-P5-1-002; US-KY-P5-2-001; US-KY-P5-2-002; US-KY-P5-2-004; US-KYP7-001; US-KYP8-001; US-KYP8-002; US-KYP9L-001; US-KYP9V-001; US-KYP9W-001; US-KYP9W-002; US-KYR3-001; US-KYR3-002; US-KYR3-003; US-KYS5-001; US-KYS5-002; US-KYS5-003; US-KYS5-004; US-KYS5-005; US-KYS5-006; US-KYS5-007; US-KYS5-008; US-KYS5-009; US-KYS5-010; US-KYS5-011; US-KYS5-012; US-KYS5-013; US-KYS5-014; US-KYS5-015; US-KYS5-016; US-KYS5-017; US-KYS5-018; US-KYS5-019; US-KYS5-020; US-KYS5-021; US-KYS5-022; US-KYS5-023; US-KYS5-024; US-KYS5-025; US-MULTI-009

## Number-in-row warnings (value not found literally in the row text; reviewed by the worker)

- ky.payslip.deduction_statement.employer_threshold=10 not literally in US-KYP8-001: Employers with ten or more employees that make deductions must state each deduction specifically and, at payment, furnish a paper or electronic statement giving
- ky.records.retention_years=1 not literally in US-KYP8-002: Employer records of amount paid each pay period and hours worked each day and week; kept at least one year after entry; open to the commissioner. No language cl
- ky.oracle.formula.biweekly_1500.annual=1247.4 not literally in US-KY-002: Standard deduction 3,360; 3.5%; worked examples (oracle). Bi-weekly example prints 35,730 where 35,640 expected; monthly result shown in cents (104.65), bi-week
- CITED US-KYS5-026 status=MANUAL (narrative only)
- CITED US-KY-P5-1-001 status=MANUAL (narrative only)

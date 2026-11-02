# Synthesis B report — CCG / annex_CT (Connecticut)

- Date: 2026-11-02
- Facts written: 61
- Unresolved: 9 (blocking 1)
- Files: `_research/CCG-annex_CT-facts.json`, `_research/CCG-annex_CT-research-pack.md`
- Validator: `python ~/mercans-pipeline/shared/schemas/validate_contract.py facts _research/CCG-annex_CT-facts.json` → rc=0

```
engine: jsonschema 4.26.0
ok    C:\Users\instituto\Documents\brain-service\Research Pipeline\USA\US-compliance\_research\CCG-annex_CT-facts.json   [facts.schema.json]
PASS  (1 file)
```

## Register ids consumed (append `CCG/annex_CT` to consumed_by at final merge) — 46

US-CT-P5-1-005; US-CT-P5-2-002; US-CTL-001; US-CTL-002; US-CTP10-001; US-CTP7-001; US-CTP9L-001; US-CTP9V-001; US-CTP9W-001; US-CTP9W-002; US-CTS5-001; US-CTS5-002; US-CTS5-003; US-CTS5-004; US-CTS5-005; US-CTS5-006; US-CTS5-007; US-CTS5-008; US-CTS5-009; US-CTS5-010; US-CTS5-011; US-CTS5-012; US-CTS5-013; US-CTS5-014; US-CTS5-015; US-CTS5-016; US-CTS5-017; US-CTS5-018; US-CTS5-019; US-CTS5-020; US-CTS5-021; US-CTS5-022; US-CTS5-023; US-CTS5-024; US-CTS5-025; US-CTS5-026; US-CTS5-027; US-CTS5-028; US-CTS5-029; US-CTS5-030; US-CTS5-031; US-CTS5-032; US-CTS5-033; US-CTS5-034; US-CTS5-035; US-MULTI-020

## Number-in-row warnings (value not found literally in the row text; reviewed by the worker)

- ct.tipped.max_tip_credit.hotel_restaurant=10.56 not literally in US-CTS5-002: Tipped hotel/restaurant employees (non-bartenders): employer share 6.38 USD/h; bartenders: 8.23 USD/h (tip credit = minimum fair wage minus employer share); oth
- ct.minwage.minor.hourly=14.4 not literally in US-CTS5-001: Statutory floor 15.00 USD/h from 2023-06-01; indexed every 1 January by the % change in the ECI (wages and salaries, all civilian workers) over the 12 months en
- ct.sui.employee.rate=0 not literally in US-CTS5-031: Local copy (md5 5707bd7eb7bea69f7e580194c5b1e161) replacing the MANUAL row. Quarterly Tax and Wage Report filed and paid electronically via ReEmployCT (manual e
- ct.oracle.ip2026_1.ex8.withholding=17.65 not literally in US-CTS5-011: Form CT-W4 (Rev. 12/25) codes A/B/C/D/E/F by filing status and income; no CT-W4 -> withhold flat 6.99% without exemption; Code E (exempt) certificates expire 15
- ct.oracle.ip2026_1.ex9.withholding=39.97 not literally in US-CTS5-011: Form CT-W4 (Rev. 12/25) codes A/B/C/D/E/F by filing status and income; no CT-W4 -> withhold flat 6.99% without exemption; Code E (exempt) certificates expire 15
- ct.oracle.ip2026_1.ex10.withholding=78.82 not literally in US-CTS5-011: Form CT-W4 (Rev. 12/25) codes A/B/C/D/E/F by filing status and income; no CT-W4 -> withhold flat 6.99% without exemption; Code E (exempt) certificates expire 15

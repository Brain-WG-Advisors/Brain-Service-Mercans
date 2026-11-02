# Synthesis B report — CCG / annex_FED

- Date: 2026-11-02 (worker: CCG annexes FED+MULTI)
- Facts written: 281 in `facts[]`
- Unresolved: 10 (blocking 0)
- Files: `_research/CCG-annex_FED-facts.json`, `_research/CCG-annex_FED-research-pack.md`; generator scripts in `_research/synthesis-B/annex-FED-MULTI-work/`
- Validator: `python ~/mercans-pipeline/shared/schemas/validate_contract.py facts _research/CCG-annex_FED-facts.json`

```
engine: jsonschema 4.26.0
ok    CCG-annex_FED-facts.json   [facts.schema.json]
PASS  (1 file)
rc=0
```

## Notes

- Supersession already applied by SYNTHESIS-A and relied on: US-FEDS5-028 supersedes US-FEDP6-001 / US-FEDR3-004 (IWO approved 2026-08-25, expiry 2029-08-31).
- Partial rows cited with the partial flag carried in `note`: US-FEDS5-009 (FUTA 2025 final credit reductions), US-FEDS5-012 (ACA, TY2025 instructions), US-FEDS5-031 (Form 940/941/944 mechanics, 2025 i940).
- Not emitted as facts: FUTA 2026 potential credit reductions (CA 5.3%, USVI 4.8%) - live until 2026-11-10; Step-2-checked schedule column C (not compared with the publication).
- FEIE cited on US-FED-025 (pattern-compliant, same Rev. Proc. figure) instead of US-FED-P5-2-002, whose id fails the schema pattern.
- Federal oracle facts (Pub. 15-T NRA 526.90 -> 31; tribal 6,000 -> 584.09, US-FED-027) are in this file; the State worked examples belong to the State annexes and to CCG m12_worked_examples (owned by the CCG modules worker).

## Register ids consumed (append `CCG/annex_FED` to consumed_by at final merge) — 48

US-FED-001; US-FED-003; US-FED-007; US-FED-008; US-FED-018; US-FED-019; US-FED-022; US-FED-023; US-FED-024; US-FED-025; US-FED-026; US-FED-027; US-FED-030; US-FED-P5-1-013; US-FEDR3-005; US-FEDR3-006; US-FEDS5-001; US-FEDS5-002; US-FEDS5-003; US-FEDS5-004; US-FEDS5-005; US-FEDS5-006; US-FEDS5-007; US-FEDS5-008; US-FEDS5-009; US-FEDS5-010; US-FEDS5-011; US-FEDS5-012; US-FEDS5-013; US-FEDS5-014; US-FEDS5-015; US-FEDS5-016; US-FEDS5-017; US-FEDS5-018; US-FEDS5-019; US-FEDS5-020; US-FEDS5-021; US-FEDS5-022; US-FEDS5-023; US-FEDS5-024; US-FEDS5-025; US-FEDS5-026; US-FEDS5-027; US-FEDS5-028; US-FEDS5-029; US-FEDS5-030; US-FEDS5-031; US-FEDS5-032

## Number-in-row warnings

- none

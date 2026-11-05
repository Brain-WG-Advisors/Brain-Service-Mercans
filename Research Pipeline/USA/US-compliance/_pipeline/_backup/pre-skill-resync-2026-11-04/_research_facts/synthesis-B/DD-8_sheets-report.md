# Synthesis-B report - DD 8_sheets

Worker RSPEC+DD, 2026-11-02. No fetching; inputs: stage5/{JUR}.md section 5 (+ special populations, open questions), register rows active/partial at tier A, MANDATE US-OWN-005/006.

- Facts file: `_research/DD-8_sheets-facts.json` - facts (schema-valid `facts[]`): 88; verified but held in `_facts_pending_register_id_pattern` (multi-segment register ids rejected by the facts schema pattern): 15; total 103.
- Unresolved: 3 (0 blocking).
- Research pack: `_research/DD-research-pack.md`.
- Numeric G-SPOT: every numeric fact (82 across RSPEC+DD) was found literally in its register row text or in the row's local source file (PyMuPDF/HTML text search, 2026-11-02). Five stage-5 citations were re-pointed to the row that actually carries the figure: AL EFT 750 -> US-ALS5-001; IN EFT 5,000 -> US-INS5-012; KY 26 -> US-KYS5-013; MI 480,000 -> US-MIS5-021; NJ base week 310 -> US-NJS5-010. AR UI e-file threshold 250 (stage-5 AR) is in neither US-ARP9V-001 nor its file: moved to unresolved, not written as a value.
- Verification method: register rows marked "derived arithmetically" derive withholding figures, not filing thresholds; facts drawn from them are recorded as "quoted from authority page".
- Oracle examples: RSPEC and DD own no calculation examples; the worked-example oracle set belongs to the CCG m12 / WTC workers.

## Register ids consumed (for the merge worker: append `DD/8_sheets` to consumed_by)

US-AKS5-014; US-ALS5-005; US-ARS5-009; US-AZP51-001; US-CAS5-015; US-COP52-001; US-COL-001; US-COS5-012; US-CTS5-011; US-CTS5-018; US-CTS5-019; US-DCS5-013; US-DES5-006; US-DES5-013; US-FEDS5-006; US-FEDS5-007; US-FEDS5-012; US-FEDS5-016; US-FEDS5-024; US-FLS5-010; US-FLS5-021; US-FLS5-024; US-GAS5-010; US-GAS5-012; US-HIS5-026; US-IAP52-001; US-IAS5-012; US-IAS5-029; US-IDS5-013; US-ILS5-010; US-INS5-014; US-INS5-016; US-INS5-021; US-KSS5-025; US-KY-001; US-KYP9W-001; US-LAPIT-001; US-LAS5-010; US-MAS5-014; US-MAS5-018; US-MDP51-001; US-MDS5-016; US-MDS5-018; US-MES5-011; US-MIP51-002; US-MIS5-019; US-MNPIT-001; US-MNS5-015; US-MOS5-013; US-MOS5-020; US-MSPIT-001; US-MSS5-006; US-MTP51-002; US-MULTIS5-001; US-MULTIS5-003; US-MULTIS5-005; US-MULTIS5-010; US-MULTIS5-013; US-MULTIS5-014; US-MULTIS5-017; US-MULTIS5-021; US-MULTIS5-024; US-NC-001; US-NDS5-001; US-NEP51-001; US-NES5-011; US-NJS5-017; US-NJS5-018; US-NJS5-024; US-NMP52-001; US-NY-001; US-NY-003; US-NYP9L-001; US-NYS5-010; US-OH-002; US-OHP52-003; US-OHS5-019; US-OHS5-020; US-OKS5-021; US-ORS5-004; US-ORS5-010; US-ORS5-012; US-PAS5-013; US-PAS5-017; US-RIS5-019; US-SCS5-003; US-TXS5-008; US-UTS5-013; US-VAS5-021; US-VTS5-007; US-VTS5-029; US-WAS5-013; US-WAS5-027; US-WIP51-001; US-WVUI-001; US-WVS5-011; US-WYS5-002

## Rows consumed without a valid effective_from (Stage 9 flags these; merge worker / scaffolder)

Facts from these rows carry `_effective_from_basis` (publication_date, or 2026-01-01 as in-force date): US-AKS5-014; US-COL-001; US-CTS5-018; US-CTS5-019; US-FLS5-021; US-FLS5-024; US-HIS5-026; US-INS5-021; US-LAS5-010; US-MAS5-014; US-MAS5-018; US-MDS5-018; US-MNS5-015; US-MULTIS5-017; US-MULTIS5-024; US-NJS5-017; US-NJS5-018; US-NJS5-024; US-NYP9L-001; US-TXS5-008; US-VTS5-007; US-VTS5-029; US-WAS5-013; US-WAS5-027; US-WVUI-001

## Partial rows used (confidence low on the fact)

US-FEDS5-012; US-IDS5-013

## Validator output

```
$ python ~/mercans-pipeline/shared/schemas/validate_contract.py facts _research/DD-8_sheets-facts.json
engine: jsonschema 4.26.0
ok    _research/DD-8_sheets-facts.json   [facts.schema.json]
PASS  (1 file)
exit 0
```

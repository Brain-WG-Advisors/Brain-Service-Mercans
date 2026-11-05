# Synthesis B report — CCG / annex_MULTI

- Date: 2026-11-02 (worker: CCG annexes FED+MULTI)
- Facts written: 125 in `facts[]`; 37 held in `_facts_pending_register_id_pattern`
- Unresolved: 38 (blocking 0)
- Files: `_research/CCG-annex_MULTI-facts.json`, `_research/CCG-annex_MULTI-research-pack.md`; generator scripts in `_research/synthesis-B/annex-FED-MULTI-work/`
- Validator: `python ~/mercans-pipeline/shared/schemas/validate_contract.py facts _research/CCG-annex_MULTI-facts.json`

```
engine: jsonschema 4.26.0
ok    CCG-annex_MULTI-facts.json   [facts.schema.json]
PASS  (1 file)
rc=0
```

## Notes

- Facts pending only because of the register_id pattern defect: see `_facts_pending_register_id_pattern` (ids of the form US-XX-P5-n-nnn, US-AZ-WH-003, US-FED-P5-n-nnn). Contract decision for the scaffolder/owner.
- Corrections to MULTI.md: MS resident withholding rule (US-MSS5-004/-019); LA rule adopted LR 52:358 (US-LAS5-002, supersedes US-MULTIS5-022); AR convenience closed on Act 1019 (US-ARS5-006); ND/MN/WI/MS nonresident rules added from State units.
- Number-in-row warning reviewed: multi.nonresident.vt.threshold_days=30 - row US-VT-P5-2-003 writes 'thirty days' (word); value confirmed by reading.
- AR SUI other-State credit not emitted: US-ARP9V-001 does not carry the clause in figure_or_rule_carried (unresolved entry asks the merge worker to append it).
- SUI other-State wage credit coverage: YES 25 States, ID conditional, NO IA/MT; open after search CO, DC, LA, MD, MO, NM, UT, AR; not answered in the State unit AZ, GA, IL, IN, MA, MN, NJ, NY, OH, PA, TN, TX, VA, WA, WI (parallel per-State lookups: one statute read each).

## Register ids consumed (append `CCG/annex_MULTI` to consumed_by at final merge) — 124

US-AKS5-005; US-ALS5-003; US-ALS5-009; US-AR-P5-1-002; US-AR-P5-2-001; US-ARP9V-001; US-ARS5-006; US-AZ-WH-003; US-CO-P5-1-002; US-CTP10-001; US-CTS5-016; US-CTS5-035; US-DC-P5-1-006; US-DC-P5-1-007; US-DCS5-007; US-DES5-004; US-DES5-010; US-DES5-012; US-FED-P5-1-009; US-FED-P5-2-006; US-FLS5-020; US-GA-P5-2-003; US-GAS5-004; US-HI-P5-1-002; US-HIS5-012; US-IAS5-024; US-ID-P5-2-002; US-IDS5-021; US-IL-P5-1-001; US-ILS5-014; US-IN-002; US-KS-P5-1-003; US-KSS5-020; US-KYS5-018; US-LA-P5-1-001; US-LAS5-002; US-MAS5-023; US-MDS5-019; US-ME-P5-2-003; US-ME-P5-2-004; US-ME-P5-2-005; US-MES5-020; US-MES5-025; US-MIS5-010; US-MNS5-010; US-MOS5-001; US-MS-P5-2-002; US-MSS5-004; US-MSS5-011; US-MSS5-019; US-MT-P5-1-003; US-MT-P5-1-004; US-MTS5-025; US-MULTI-004; US-MULTI-005; US-MULTI-006; US-MULTI-007; US-MULTI-008; US-MULTI-009; US-MULTI-010; US-MULTI-011; US-MULTI-012; US-MULTI-013; US-MULTI-014; US-MULTI-015; US-MULTI-016; US-MULTI-017; US-MULTI-018; US-MULTI-019; US-MULTI-020; US-MULTIS5-001; US-MULTIS5-002; US-MULTIS5-003; US-MULTIS5-004; US-MULTIS5-005; US-MULTIS5-006; US-MULTIS5-007; US-MULTIS5-008; US-MULTIS5-009; US-MULTIS5-010; US-MULTIS5-011; US-MULTIS5-013; US-MULTIS5-014; US-MULTIS5-016; US-MULTIS5-017; US-MULTIS5-018; US-MULTIS5-019; US-MULTIS5-020; US-MULTIS5-021; US-MULTIS5-023; US-MULTIS5-024; US-MULTIS5-025; US-NC-P5-1-002; US-NCS5-015; US-NDS5-004; US-NDS5-009; US-NE-P5-1-002; US-NES5-011; US-NHS5-007; US-NM-P5-2-002; US-NVS5-006; US-NY-013; US-OH-P5-2-004; US-OH-P5-2-006; US-OK-P5-2-002; US-OKS5-005; US-OKS5-010; US-ORS5-014; US-ORS5-015; US-RI-P5-2-002; US-RIS5-013; US-RIS5-016; US-SCR3-001; US-SCR3-003; US-SCR3-004; US-SCS5-014; US-SDS5-002; US-UT-P5-1-002; US-VT-P5-1-003; US-VT-P5-2-003; US-VTS5-010; US-WIS5-011; US-WVS5-001; US-WYS5-003

## Number-in-row warnings

- multi.nonresident.vt.threshold_days=30 not literally in US-VT-P5-2-003

# Synthesis B report: SIR / unit `third_party_provider_handoff`

Worker: SIR+PSL synthesis worker, 2026-11-02. No fetching. Inputs: stage5 sections 4, 5, 12 (53 files), MANDATE (US-MQ-03, US-MQ-09, US-MQ-12; US-OWN-005/006), register (2,533 rows), `00-filing-terceiros/PROCESSO-FILING-TERCEIROS.md`. Generator scripts: `_research/synthesis-B/_scratch-SIR-PSL/` (gen_common.py pulls tier, authority, url, effective dates and status from the register; nothing hand-copied).

## Outputs
- `_research/SIR-facts.json` (artifact SIR, unit `third_party_provider_handoff`)
- `_research/SIR-research-pack.md`

## Counts
- Facts in the validated array: 223
- Facts parked under `_facts_blocked_by_register_id_pattern` (active rows, multi-segment ids rejected by the 1.4.0 pattern): 70
- Unresolved: 15 (blocking: 1)
- Facts with confidence medium/low: 30
- Facts whose row has no full effective_from (default 2026-01-01 with `_effective_from_basis`): 108

## Validator output
```
engine: jsonschema 4.26.0
ok    _research/SIR-facts.json   [facts.schema.json]
PASS  (1 file)
```

## Contract defect to route to the orchestrator
facts.schema.json 1.4.0 `register_id` pattern `^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$` rejects this build's multi-segment ids (US-AKP51-006, US-AKWT-001, US-ALP52-002, US-ARP51-002, US-ARP52-003, US-AZP52-001, US-AZP52-002, US-AZP52-005, US-CAEDD-006, US-COP51-006, US-COP52-001, US-COP52-003 ...). Options: PATCH-bump the pattern (looser pattern, e.g. `^[A-Z]{2}(-[A-Z0-9]{1,12})+-[0-9]{3,4}$`) or have the merge worker issue compliant alias ids. Until then those facts are outside the validated array but bound to active rows.

## Register ids consumed (for the merge worker to append `SIR/third_party_provider_handoff` to consumed_by)
US-AKP51-006;US-AKWT-001;US-AKS5-005;US-AKS5-007;US-AKS5-013;US-AKS5-014;US-ALP52-002;US-ALS5-001;US-ALS5-006;US-ALS5-007;US-ALS5-008;US-ALS5-017;US-ARP51-002;US-ARP52-003;US-ARP9V-001;US-AZP52-001;US-AZP52-002;US-AZP52-005;US-AZS5-012;US-AZS5-025;US-CAEDD-006;US-CAS5-002;US-CAS5-018;US-COP51-006;US-COP52-001;US-COP52-003;US-COS5-006;US-COS5-013;US-CTP51-007;US-CTP52-002;US-CTS5-013;US-CTS5-019;US-CTS5-022;US-CTS5-032;US-DCP51-014;US-DCP52-003;US-DCS5-014;US-DCS5-015;US-DCS5-018;US-DCS5-022;US-DEP52-001;US-DEP52-002;US-DES5-005;US-DES5-008;US-DES5-011;US-DES5-013;US-FED-008;US-FED-009;US-FED-028;US-FEDP51-002;US-FEDP51-016;US-FEDS5-004;US-FEDS5-007;US-FEDS5-024;US-FIL-001;US-FIL-002;US-FIL-006;US-FIL-007;US-FIL-008;US-FIL-010;US-FIL-011;US-FIL-012;US-FL-001;US-FL-005;US-FLS5-006;US-FLS5-008;US-FLS5-022;US-FLS5-023;US-GAW1B-001;US-GAW1B-003;US-GAS5-002;US-GAS5-003;US-GAS5-005;US-GAS5-012;US-HIP51-004;US-HIP52-003;US-HIS5-005;US-HIS5-006;US-HIS5-012;US-HIS5-021;US-IAP51-003;US-IAP51-004;US-IAS5-012;US-IAS5-016;US-IAS5-017;US-IAS5-024;US-IDR3-001;US-IDR3-002;US-IDS5-009;US-IDS5-010;US-IDS5-015;US-IDS5-021;US-IL-004;US-ILP52-010;US-ILS5-011;US-ILS5-013;US-ILS5-017;US-ILS5-018;US-INR3-003;US-INR3-004;US-INS5-010;US-INS5-011;US-INS5-014;US-INS5-016;US-KSP51-005;US-KSP52-003;US-KSS5-007;US-KSS5-019;US-KSS5-022;US-KSS5-026;US-KYP52-002;US-KYS5-013;US-KYS5-019;US-KYS5-020;US-LAP52-005;US-LAS5-003;US-LAS5-007;US-LAS5-009;US-LAS5-010;US-MAP51-007;US-MAS5-013;US-MAS5-015;US-MAS5-016;US-MAS5-018;US-MAS5-019;US-MDP51-001;US-MDS5-016;US-MDS5-017;US-MDS5-018;US-MDS5-021;US-MEP52-002;US-MES5-011;US-MES5-016;US-MES5-021;US-MES5-024;US-MIP52-005;US-MIP52-011;US-MIPIT-001;US-MIS5-018;US-MIS5-022;US-MNP52-005;US-MNP6-003;US-MNS5-010;US-MNS5-015;US-MNS5-016;US-MNS5-018;US-MOP52-008;US-MOS5-001;US-MOS5-008;US-MOS5-013;US-MSP52-005;US-MSS5-005;US-MSS5-006;US-MSS5-013;US-MSS5-019;US-MTS5-005;US-MTS5-012;US-MTS5-025;US-MULTIS5-006;US-MULTIS5-011;US-NC-001;US-NCP51-003;US-NCS5-020;US-NCS5-025;US-NCS5-028;US-NDP51-002;US-NDS5-002;US-NDS5-011;US-NDS5-013;US-NEP51-004;US-NES5-010;US-NES5-011;US-NES5-014;US-NES5-017;US-NH-006;US-NHP6-001;US-NHS5-006;US-NHS5-013;US-NJP51-001;US-NJP6-001;US-NJR3-004;US-NJR3-005;US-NJS5-017;US-NJS5-018;US-NMP51-004;US-NMP52-005;US-NMP6-001;US-NMS5-010;US-NMS5-012;US-NMS5-016;US-NVP51-001;US-NVR3-003;US-NVS5-007;US-NVS5-008;US-NVS5-009;US-NY-003;US-NYS5-010;US-OH-009;US-OHP52-003;US-OHP52-005;US-OHR3-001;US-OKP51-004;US-OKP51-005;US-OKS5-007;US-OKS5-010;US-OKS5-020;US-ORP51-005;US-ORS5-010;US-ORS5-016;US-ORS5-024;US-PAP51-004;US-PAS5-008;US-PAS5-010;US-PAS5-017;US-RIP51-004;US-RIS5-010;US-RIS5-017;US-RIS5-018;US-SCP52-001;US-SCR3-008;US-SCS5-002;US-SCS5-006;US-SCS5-011;US-SCS5-016;US-SDP51-001;US-SDS5-001;US-SDS5-007;US-SDS5-013;US-TNR3-002;US-TNS5-005;US-TNS5-008;US-TXP52-008;US-TXSUI-006;US-TXS5-001;US-TXS5-008;US-TXS5-016;US-UTP6-002;US-UTP6-003;US-UTS5-003;US-UTS5-004;US-UTS5-013;US-UTS5-014;US-VAP51-007;US-VAP6-001;US-VAS5-006;US-VAS5-009;US-VAS5-013;US-VAS5-014;US-VTP51-012;US-VTP51-013;US-VTS5-007;US-VTS5-014;US-VTS5-017;US-WAP51-001;US-WAS5-013;US-WAS5-018;US-WIP51-002;US-WIP52-003;US-WIS5-011;US-WIS5-012;US-WIS5-013;US-WIS5-016;US-WVP51-006;US-WVP52-006;US-WVUI-001;US-WVS5-010;US-WVS5-013;US-WVS5-016;US-WYP51-001;US-WYR3-001;US-WYS5-006;US-WYS5-009;US-WYS5-019

## Value checks run
- Every numeric fact's value was searched in the cited row's `figure_or_rule_carried`. Misses were re-pointed (AK retention -> US-AKS5-001; TX new hire -> US-TXS5-016), confirmed in the registered local file (AR 125 employees e-file, AR 6-year retention: DFA Withholding Tax Instructions, local PDF read with PyMuPDF), or moved to unresolved (NC 10-year retention). Word-form numbers (three/ten/two/one) accepted.
- Every cited row is `active` or `partial` (partial -> confidence low + note). No superseded/MANUAL/gated row carries a fact; those are listed in `unresolved`.

## Not done here (by design)
- Oracle worked examples (brief rule): none belong to SIR/PSL; they go to the artifact that owns calculation examples (WTC).
- `consumed_by` not written to the register (merge worker only).

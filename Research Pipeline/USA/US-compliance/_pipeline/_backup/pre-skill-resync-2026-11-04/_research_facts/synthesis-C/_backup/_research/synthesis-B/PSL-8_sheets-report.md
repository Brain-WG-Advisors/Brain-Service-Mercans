# Synthesis B report: PSL / unit `8_sheets`

Worker: SIR+PSL synthesis worker, 2026-11-02. No fetching. Inputs: stage5 sections 4, 5, 12 (53 files), MANDATE (US-MQ-03, US-MQ-09, US-MQ-12; US-OWN-005/006), register (2,533 rows), `00-filing-terceiros/PROCESSO-FILING-TERCEIROS.md`. Generator scripts: `_research/synthesis-B/_scratch-SIR-PSL/` (gen_common.py pulls tier, authority, url, effective dates and status from the register; nothing hand-copied).

## Outputs
- `_research/PSL-facts.json` (artifact PSL, unit `8_sheets`)
- `_research/PSL-research-pack.md`

## Counts
- Facts in the validated array: 136
- Facts parked under `_facts_blocked_by_register_id_pattern` (active rows, multi-segment ids rejected by the 1.4.0 pattern): 29
- Unresolved: 12 (blocking: 0)
- Facts with confidence medium/low: 17
- Facts whose row has no full effective_from (default 2026-01-01 with `_effective_from_basis`): 73

## Validator output
```
engine: jsonschema 4.26.0
ok    _research/PSL-facts.json   [facts.schema.json]
PASS  (1 file)
```

## Contract defect to route to the orchestrator
facts.schema.json 1.4.0 `register_id` pattern `^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$` rejects this build's multi-segment ids (US-AL-P5-2-001, US-AR-P5-1-002, US-AR-P5-2-006, US-CO-P5-1-005, US-CT-P5-1-005, US-HI-P5-2-001, US-IA-P5-1-002, US-ID-P5-1-002, US-KS-P5-2-001, US-MA-P5-1-008, US-MD-P5-1-005, US-MO-P5-2-002 ...). Options: PATCH-bump the pattern (looser pattern, e.g. `^[A-Z]{2}(-[A-Z0-9]{1,12})+-[0-9]{3,4}$`) or have the merge worker issue compliant alias ids. Until then those facts are outside the validated array but bound to active rows.

## Register ids consumed (for the merge worker to append `PSL/8_sheets` to consumed_by)
US-AKS5-001;US-AKS5-016;US-AL-P5-2-001;US-AR-P5-1-002;US-AR-P5-2-006;US-AZL-001;US-AZS5-001;US-AZS5-006;US-AZS5-011;US-CAP6-001;US-CAS5-005;US-CAS5-011;US-CAS5-018;US-CO-P5-1-005;US-COL-001;US-COP9L-001;US-COS5-001;US-CT-P5-1-005;US-CTL-001;US-CTS5-027;US-CTS5-028;US-DCS5-010;US-DEL-001;US-DES5-001;US-DES5-002;US-FED-010;US-FED-020;US-FEDR3-010;US-FEDS5-003;US-FEDS5-007;US-FEDS5-021;US-FEDS5-022;US-FLL-001;US-FLL-002;US-GAP9L-001;US-GAS5-005;US-HI-P5-2-001;US-HIS5-007;US-HIS5-028;US-IA-P5-1-002;US-IAS5-027;US-ID-P5-1-002;US-IDS5-006;US-ILS5-024;US-INP6-001;US-INS5-001;US-KS-P5-2-001;US-KSS5-011;US-KYP8-001;US-KYP8-002;US-LAR3-002;US-MA-P5-1-008;US-MAL-002;US-MAS5-005;US-MD-P5-1-005;US-MDS5-007;US-MDS5-008;US-MDS5-013;US-MES5-006;US-MES5-025;US-MIL-001;US-MIS5-009;US-MIS5-013;US-MNP6-001;US-MNS5-011;US-MNS5-020;US-MO-P5-2-002;US-MO-P5-2-003;US-MOS5-016;US-MSP9L-001;US-MSS5-019;US-MT-P5-1-006;US-MTS5-005;US-MULTIS5-011;US-MULTIS5-018;US-NC-W1B-003;US-NCS5-016;US-NCS5-024;US-NDS5-007;US-NE-P5-1-004;US-NES5-013;US-NH-P5-1-001;US-NHS5-003;US-NJP8-001;US-NJP9M-001;US-NJS5-022;US-NMP8-001;US-NMS5-002;US-NVR3-001;US-NVS5-001;US-NY-P5-1-003;US-NYS5-006;US-NYS5-009;US-OH-P5-1-001;US-OHS5-004;US-OKS5-003;US-OKS5-008;US-OKS5-014;US-ORL-001;US-ORS5-019;US-ORS5-022;US-ORS5-026;US-PA-P5-1-001;US-PAS5-020;US-RI-P5-1-002;US-RIS5-020;US-SC-P5-2-006;US-SCS5-009;US-SDS5-001;US-TNS5-001;US-TXP9M-001;US-TXS5-003;US-TXS5-013;US-UTP6-001;US-UTS5-012;US-VAS5-003;US-VTL-001;US-VTP9-001;US-VTS5-015;US-VTS5-030;US-WAS5-004;US-WAS5-005;US-WAS5-030;US-WI-P5-2-001;US-WIS5-002;US-WVS5-008;US-WY-P5-1-005;US-WYS5-001

## Value checks run
- Every numeric fact's value was searched in the cited row's `figure_or_rule_carried`. Misses were re-pointed (AK retention -> US-AKS5-001; TX new hire -> US-TXS5-016), confirmed in the registered local file (AR 125 employees e-file, AR 6-year retention: DFA Withholding Tax Instructions, local PDF read with PyMuPDF), or moved to unresolved (NC 10-year retention). Word-form numbers (three/ten/two/one) accepted.
- Every cited row is `active` or `partial` (partial -> confidence low + note). No superseded/MANUAL/gated row carries a fact; those are listed in `unresolved`.

## Not done here (by design)
- Oracle worked examples (brief rule): none belong to SIR/PSL; they go to the artifact that owns calculation examples (WTC).
- `consumed_by` not written to the register (merge worker only).

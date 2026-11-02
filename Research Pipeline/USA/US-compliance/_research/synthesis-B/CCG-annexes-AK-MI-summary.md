# Synthesis B — CCG jurisdiction annexes AK..MI (23 units): summary for the merge worker

Worker: Synthesis-B CCG annexes AK-MI, 2026-11-02. No fetching. Every facts file validates (`validate_contract.py facts` → PASS, jsonschema 4.26.0). Per-unit reports: `_research/synthesis-B/CCG-annex_{JUR}-report.md`; packs `_research/CCG-annex_{JUR}-research-pack.md`; facts `_research/CCG-annex_{JUR}-facts.json` (facts.schema allows `{ARTIFACT}-{unit}-facts.json`). Builder scripts: `_research/synthesis-B/_scratch-CCG-annexes-AK-MI/` (build.py + spec_{JUR}.py).

Totals: **1204 facts**, **265 unresolved** (27 blocking), **842 register ids consumed**, 24 numeric oracle facts. Post-check: every fact register_id is active/partial, tier A.1-A.3, key prefixed with the jurisdiction code; violations found: 0.

| JUR | facts | unresolved | blocking | legacy-id items |
|---|---|---|---|---|
| AK | 48 | 9 | 0 | 1 |
| AL | 62 | 6 | 1 | 0 |
| AR | 47 | 16 | 1 | 8 |
| AZ | 47 | 11 | 2 | 2 |
| CA | 94 | 11 | 2 | 0 |
| CO | 50 | 14 | 2 | 7 |
| CT | 61 | 9 | 1 | 0 |
| DC | 48 | 12 | 2 | 3 |
| DE | 69 | 9 | 1 | 1 |
| FL | 35 | 8 | 1 | 2 |
| GA | 43 | 11 | 2 | 2 |
| HI | 85 | 11 | 1 | 2 |
| IA | 45 | 9 | 0 | 0 |
| ID | 37 | 13 | 2 | 2 |
| IL | 49 | 12 | 2 | 2 |
| IN | 45 | 9 | 0 | 0 |
| KS | 53 | 8 | 0 | 1 |
| KY | 43 | 12 | 1 | 1 |
| LA | 31 | 16 | 2 | 3 |
| MA | 57 | 18 | 2 | 3 |
| MD | 48 | 14 | 0 | 2 |
| ME | 52 | 18 | 1 | 5 |
| MI | 55 | 9 | 1 | 1 |

## Key convention
Keys are `{jur}.{domain}.{concept}...` with the lowercase jurisdiction code (e.g. `ca.sui.wage_base`, `ny.` for NY). One key = one meaning country-wide. The MN-WY worker should use the same prefix rule; recurring concepts use the same tail (`.minwage.hourly`, `.sui.wage_base`, `.sui.new_employer.rate`, `.sui.employee.rate`, `.wh.supplemental.rate`, `.newhire.report_days`, `.final_pay.rule`, `.payslip.items`, `.oracle.*`).

## FINDING for the orchestrator/merge: legacy register ids fail the facts.schema pattern
590 register ids (e.g. `US-AKWT-001`, `US-ARP51-002`, `US-COP51-003`, `US-MIPIT-001`) contain a second hyphen and fail `register_id` pattern `^[A-Z]{2}-[A-Z0-9]{2,12}-[0-9]{3,4}$`. A fact citing them cannot validate. Where an S5-pattern row carried the same figure, the fact cites it; otherwise the value is listed in the pack as a "legacy id, NOT a fact" line and in `unresolved[]` (non-blocking) with close = "register an S5-pattern alias row (supersedes the legacy id) or re-key; then emit". No new research is needed for these. Items:

- AK: `ak.prevailing_wage.threshold`
- AR: `ar.wh.supplemental.rate`
- AR: `ar.wh.texarkana.exemption`
- AR: `ar.pay_frequency.rule`
- AR: `ar.report.wh.monthly`
- AR: `ar.report.w2.efile_threshold_employees`
- AR: `ar.records.withholding.retention_years`
- AR: `ar.payslip.state_statute.exists`
- AR: `ar.prevailing_wage.state_law.exists`
- AZ: `az.report.wh.deposit_schedule`
- AZ: `az.prevailing_wage.state_mandate.exists`
- CO: `co.wh.method`
- CO: `co.sui.wage_base`
- CO: `co.sui.wage_base.next_year`
- CO: `co.sui.new_employer.rate.total`
- CO: `co.famli.rate.total.2026`
- CO: `co.payslip.items`
- CO: `co.prevailing_wage.threshold`
- DC: `dc.pit.rate_schedule`
- DC: `dc.wh.notice_2022_08`
- DC: `dc.nonres.taxable`
- DE: `de.local.wilmington.eit.rate`
- FL: `fl.sdi_pfml.exists`
- FL: `fl.prevailing_wage.state_law.exists`
- GA: `ga.sui.wage_base`
- GA: `ga.prevailing_wage.state_law.exists`
- HI: `hi.nonres.exempt_days`
- HI: `hi.prevailing_wage.threshold`
- ID: `id.sui.new_employer.rate`
- ID: `id.sui.employer.rate.range`
- IL: `il.local_wage_tax.exists`
- IL: `il.sdi_pfml.exists`
- KS: `ks.prevailing_wage.state_law.exists`
- KY: `ky.prevailing_wage.state_law.exists`
- LA: `la.sui.employer.rate.min`
- LA: `la.wh.supplemental.method`
- LA: `la.local_income_tax.exists`
- MA: `ma.wh.supplemental.rule`
- MA: `ma.final_pay.rule`
- MA: `ma.prevailing_wage.rule`
- MD: `md.sui.wage_base`
- MD: `md.payslip.items`
- ME: `me.wh.bracket.single.1.ceiling`
- ME: `me.wh.bracket.single.2.ceiling`
- ME: `me.report.wh.semiweekly_threshold`
- ME: `me.sui.new_employer.rate.total`
- ME: `me.sui.employer.rate.combined.range`
- MI: `mi.reciprocity.states`

## FINDING: period values on superseded rows
- ID: zero bracket 15,000/30,000 for 2026-01-01..07-22 sits on US-IDS5-012 (superseded) — `id.wh.zero_bracket.h1_2026` blocking.
- IN: county LIT chart R46 for 2026-01-01..09-30 sits on US-IN-001 / US-INP51-001 (superseded) — `in.local.lit.chart.2026_01_to_09`.
The brief forbids numbers from superseded rows; a register status for "historical, in force for a closed period" would let these be emitted with effective_to.

## Brief traps — how they were handled
- MA PFML split date (Ch. 101 s.45 vs DFML): DECIDED for DFML (swap from 2027-01-01), recorded as fact `ma.pfml.split.decision` citing US-MAS5-012 with US-MAS5-026 in the note. Employee/employer totals (0.46% / 0.42%) are identical under both readings, so no 2026 amount changes.
- MI tips/overtime deduction: `mi.pit.tips_overtime_deduction` level = assessment only; tier-B "stop withholding on tips" flagged as unsupported.
- KS tables vs statutory brackets: `ks.wh.method` note — table thresholds (26,605 / 54,240) = standard deduction + statutory band (23,000 / 46,000).
- DC 2026 method unpublished: `dc.wh.method` blocking unresolved; Notice 2022-08 kept as a legacy line (inference only).
- CT tables vs rules: decision record in the CT pack; oracle facts are the table-based DRS examples with rule residuals in notes; engine method choice is `ct.wh.tables.per_period` (blocking).
- IA rounding: to the cent (`ia.wh.rounding`), superseding the whole-dollar clause in US-IA-001 and the MANDATE currency block (scaffolder to amend US-MQ-01).
- ME: withholding standard deduction 12,450/27,750 (not 15,300/30,600); pay statement IS required (26 MRSA 665(1)).
- AZ state minimum wage 2026/2027 (15.15/15.65) stays unresolved (MANUAL tier C) — not emitted.

## Oracle facts (for the m12_worked_examples / C37 owner)
| JUR | key | value | register_id | derivation |
|---|---|---|---|---|
| AL | `al.oracle.example.1.withholding` | 29.59 | US-ALS5-001 | Booklet example re-derived in Python: 850x52=44,200; deductions 5,000+1,830 (35.19x52=1,829.88 rounded by booklet)+3,000+2,000=11,830; taxab |
| AR | `ar.oracle.example.1.withholding` | 36.5 | US-ARS5-001 | Reproduced in Python: 25,524 - 2,470 = 23,054 -> midpoint 23,050 x 3.4% - 287.97 = 495.73 -> 496 - 58 = 438 / 12 = 36.50. |
| CA | `ca.oracle.de44.example_f.withholding_monthly` | 7.17 | US-CAS5-001 | DE 44 Method B example F: annual 57,000 married 4 allowances; 57,000 - 11,412 = 45,588 -> 243.74 + 2.2% x 23,430 = 759.20 - 673.20 = 86.00/y |
| CA | `ca.oracle.de44.example_e.withholding_semimonthly` | 4.13 | US-CAS5-001 | DE 44 Method B example E, reproduced in Python. Single cumulative bases also re-derive (121.87 ... 114,220.27); 34,084.81 derives as 34,084. |
| CT | `ct.oracle.ip2026_1.ex8.withholding` | 17.65 | US-CTS5-011 | IP 2026(1) Ex. 8: code F, 700 weekly (table-based). TPG-211 rules give 17.79 (residual 0.14). |
| CT | `ct.oracle.ip2026_1.ex9.withholding` | 39.97 | US-CTS5-011 | Ex. 9: code A, 1,000 weekly (tables). Rules give 39.86 (residual 0.11). |
| CT | `ct.oracle.ip2026_1.ex10.withholding` | 78.82 | US-CTS5-011 | Ex. 10: code B, 2,300 biweekly (tables). Rules give 79.30 (residual 0.48). |
| DE | `de.oracle.guide.example1.withholding_weekly` | 13.88 | US-DES5-006 | Guide example 1: single, 1 allowance, 25,000 annual -> tax 832.00; weekly 13.88. Reproduced in Python. |
| DE | `de.oracle.guide.example2.supplemental` | 269.63 | US-DES5-006 | Guide example 2: 500/week + 5,000 bonus, single, 1 allowance -> 269.625, shown 269.63 (half-up to cent). |
| GA | `ga.oracle.guide.example1.withholding` | 27.03 | US-GAS5-001 | MFJ, semimonthly 2,000, 1 dependent: (2,000 - 1,250 - 208.33) x 0.0499 = 27.029 -> 27.03. Table check: Single weekly band 276-294: (294 - 28 |
| HI | `hi.oracle.booklet_a.part1.withholding_weekly` | 9.58 | US-HIS5-004 | Single, 3 allowances, 500/week: 26,000 - 3,432 - 4,350 = 18,218; 288 + 3,818 x 5.5% = 497.99; /52 = 9.58. Re-derived exactly. |
| IA | `ia.oracle.formula.example6.withholding` | 114.92 | US-IAS5-005 | Formula PDF example 6 (monthly 5,000, HoH, W = 160) printed WITHOUT its final figure; derived 114.92 = (5,000 - 1,625) x 3.8% - 160/12. The  |
| ID | `id.oracle.stc.single_biweekly.withholding` | 31 | US-IDS5-008 | Single, biweekly 1,212: 5.3% x (1,212 - 619) = 31.43 -> 31; matches 07-23-2026 table. |
| ID | `id.oracle.stc.married_weekly.withholding` | 20 | US-IDS5-008 | Married weekly 1,000: (52,000 - 32,000) x 5.3% / 52 = 20.38 -> 20 as published; the example uses 32,000, matching neither table (32,200 / 30 |
| IL | `il.oracle.il700t.example1.withholding` | 8.38 | US-ILR3-001 | IL-700-T: 300 weekly, 2 + 1 allowances. |
| IL | `il.oracle.il700t.example2.withholding` | 32.13 | US-ILR3-001 | 800 weekly, 2 + 2 allowances: 7,850/52 = 150.96; 649.04 x .0495 = 32.13. |
| IN | `in.oracle.dn1.example.state` | 13.96 | US-INS5-007 | Weekly 800; constants A5 96.15 + B3 86.54 + B1 28.85 + C2 115.38 = 326.92; taxable 473.08 x 0.0295 = 13.96. |
| IN | `in.oracle.dn1.example.county` | 4.73 | US-INS5-007 | 473.08 x 0.01 = 4.73. |
| KY | `ky.oracle.formula.monthly_3270` | 104.65 | US-KY-002 | Monthly 3,270: (39,240 - 3,360) x 3.5% = 1,255.80 / 12 = 104.65. |
| KY | `ky.oracle.formula.biweekly_1500.annual` | 1247.4 | US-KY-002 | Bi-weekly 1,500: (39,000 - 3,360) = 35,640 x 3.5% = 1,247.40 (sheet prints 35,730 - typo); /26 = 47.98, sheet shows 47 (rounding unexplained |
| LA | `la.oracle.r1306.example1.withholding` | 13.98 | US-LAS5-001 | (700 - 12,875/52) x 0.0309 = 13.9793 -> 13.98. |
| LA | `la.oracle.r1306.example2.withholding` | 111.54 | US-LAS5-001 | (4,600 - 25,750/26) x 0.0309 = 111.5371 -> 111.54. |
| MI | `mi.oracle.state.biweekly_2000_1ex` | 75.36 | US-MIS5-019 | (2,000 - 226.92) x 0.0425 = 75.36. Official oracle: Treasury withholding calculator (michigan.gov/taxes/business-taxes/withholding/tax-calcu |
| MI | `mi.oracle.detroit.resident_biweekly_2000` | 47.45 | US-MIR3-002 | (2,000 - 23.08) x 0.024 = 47.45. |

## Register ids consumed (append `CCG/annex_{JUR}` per unit report; union below)

US-AKP51-003; US-AKP51-005; US-AKP51-006; US-AKP52-001; US-AKP52-002; US-AKWT-001; US-AKWT-002; US-AKL-001; US-AKP7-001; US-AKP7-002; US-AKP9L-001; US-AKP9W-001; US-AKR3-001; US-AKR3-002; US-AKR3-003; US-AKS5-001; US-AKS5-002; US-AKS5-003; US-AKS5-004; US-AKS5-005; US-AKS5-006; US-AKS5-007; US-AKS5-008; US-AKS5-009; US-AKS5-010; US-AKS5-011; US-AKS5-012; US-AKS5-013; US-AKS5-014; US-AKS5-015; US-AKS5-016; US-AKS5-017; US-AKS5-018; US-ALP51-001; US-ALP52-001; US-ALP52-002; US-ALL-001; US-ALL-002; US-ALP7-002; US-ALP9L-001; US-ALR3-001; US-ALR3-002; US-ALR3-003; US-ALS5-001; US-ALS5-002; US-ALS5-003; US-ALS5-004; US-ALS5-005; US-ALS5-006; US-ALS5-007; US-ALS5-008; US-ALS5-009; US-ALS5-010; US-ALS5-011; US-ALS5-012; US-ALS5-013; US-ALS5-014; US-ALS5-015; US-ALS5-016; US-ALS5-017; US-ALS5-018; US-ALS5-019; US-ALS5-020; US-ALS5-021; US-ARP51-001; US-ARP51-002; US-ARP51-004; US-ARP52-001; US-ARP52-002; US-ARP52-006; US-ARL-001; US-ARP9L-001; US-ARP9V-001; US-ARP9V-002; US-ARP9V-003; US-ARS5-001; US-ARS5-002; US-ARS5-003; US-ARS5-005; US-ARS5-006; US-ARS5-007; US-ARS5-008; US-ARS5-009; US-ARS5-010; US-ARS5-011; US-ARS5-013; US-ARS5-014; US-AZP51-001; US-AZP51-002; US-AZP51-003; US-AZP52-001; US-AZP52-002; US-AZP52-003; US-AZP52-004; US-AZP52-005; US-AZWH-002; US-AZWH-003; US-AZL-001; US-AZL-002; US-AZP9L-002; US-AZP9M-001; US-AZP9V-001; US-AZR3-001; US-AZR3-002; US-AZR3-003; US-AZR3-004; US-AZR3-005; US-AZR3-006; US-AZS5-001; US-AZS5-002; US-AZS5-003; US-AZS5-004; US-AZS5-005; US-AZS5-006; US-AZS5-008; US-AZS5-009; US-AZS5-010; US-AZS5-011; US-AZS5-012; US-AZS5-013; US-AZS5-014; US-AZS5-015; US-AZS5-016; US-AZS5-017; US-AZS5-018; US-AZS5-019; US-AZS5-020; US-AZS5-021; US-AZS5-022; US-AZS5-023; US-AZS5-024; US-AZS5-025; US-AZS5-026; US-AZS5-027; US-CAEDD-001; US-CAEDD-004; US-CAEDD-005; US-CAEDD-006; US-CALAB-001; US-CAPW-001; US-CAP6-001; US-CAP7-001; US-CAP7-002; US-CAP7-003; US-CAS5-001; US-CAS5-002; US-CAS5-003; US-CAS5-004; US-CAS5-005; US-CAS5-006; US-CAS5-007; US-CAS5-008; US-CAS5-009; US-CAS5-010; US-CAS5-011; US-CAS5-012; US-CAS5-013; US-CAS5-014; US-CAS5-015; US-CAS5-016; US-CAS5-017; US-CAS5-018; US-CAS5-019; US-CAS5-020; US-CAS5-021; US-CAS5-022; US-COFAMLI-001; US-COP51-001; US-COP51-002; US-COP51-003; US-COP51-004; US-COP51-005; US-COP51-006; US-COP52-001; US-COP52-002; US-COP52-003; US-COL-001; US-COL-002; US-COP7-004; US-COP7-005; US-COP9L-001; US-COS5-001; US-COS5-002; US-COS5-003; US-COS5-004; US-COS5-005; US-COS5-006; US-COS5-007; US-COS5-008; US-COS5-009; US-COS5-010; US-COS5-012; US-COS5-013; US-COS5-014; US-COS5-015; US-COS5-016; US-CTP51-005; US-CTP52-002; US-CTL-001; US-CTL-002; US-CTP10-001; US-CTP7-001; US-CTP9L-001; US-CTP9V-001; US-CTP9W-001; US-CTP9W-002; US-CTS5-001; US-CTS5-002; US-CTS5-003; US-CTS5-004; US-CTS5-005; US-CTS5-006; US-CTS5-007; US-CTS5-008; US-CTS5-009; US-CTS5-010; US-CTS5-011; US-CTS5-012; US-CTS5-013; US-CTS5-014; US-CTS5-015; US-CTS5-016; US-CTS5-017; US-CTS5-018; US-CTS5-019; US-CTS5-020; US-CTS5-021; US-CTS5-022; US-CTS5-023; US-CTS5-024; US-CTS5-025; US-CTS5-026; US-CTS5-027; US-CTS5-028; US-CTS5-029; US-CTS5-030; US-CTS5-031; US-CTS5-032; US-CTS5-033; US-CTS5-034; US-CTS5-035; US-DCP51-001; US-DCP51-002; US-DCP51-004; US-DCP51-006; US-DCP51-007; US-DCP51-014; US-DCP52-001; US-DCP52-003; US-DCP52-004; US-DCP52-005; US-DCP7-001; US-DCP7-003; US-DCR3-001; US-DCR3-002; US-DCS5-001; US-DCS5-002; US-DCS5-003; US-DCS5-004; US-DCS5-005; US-DCS5-006; US-DCS5-007; US-DCS5-008; US-DCS5-009; US-DCS5-010; US-DCS5-011; US-DCS5-012; US-DCS5-013; US-DCS5-014; US-DCS5-015; US-DCS5-016; US-DCS5-017; US-DCS5-018; US-DCS5-019; US-DCS5-020; US-DCS5-021; US-DCS5-022; US-DCS5-023; US-DCS5-024; US-DCS5-025; US-DEP52-001; US-DEP52-002; US-DEL-001; US-DEL-002; US-DEL-003; US-DEP7-001; US-DEP9L-001; US-DEP9V-001; US-DES5-001; US-DES5-002; US-DES5-003; US-DES5-004; US-DES5-005; US-DES5-006; US-DES5-007; US-DES5-008; US-DES5-009; US-DES5-010; US-DES5-011; US-DES5-012; US-DES5-013; US-DES5-014; US-DES5-015; US-DES5-016; US-DES5-017; US-DES5-018; US-DES5-019; US-DES5-020; US-DES5-021; US-DES5-022; US-FED-011; US-FEDP52-006; US-FEDS5-010; US-FL-001; US-FL-002; US-FL-005; US-FLP52-001; US-FLP52-002; US-FLP52-003; US-FLP52-004; US-FLL-001; US-FLL-002; US-FLL-003; US-FLS5-001; US-FLS5-002; US-FLS5-003; US-FLS5-004; US-FLS5-005; US-FLS5-006; US-FLS5-007; US-FLS5-008; US-FLS5-009; US-FLS5-010; US-FLS5-011; US-FLS5-012; US-FLS5-013; US-FLS5-014; US-FLS5-015; US-FLS5-016; US-FLS5-017; US-FLS5-018; US-FLS5-019; US-FLS5-020; US-FLS5-021; US-FLS5-022; US-FLS5-023; US-FLS5-025; US-FLS5-026; US-FLS5-027; US-GA-001; US-GAP51-002; US-GAP52-003; US-GAW1B-001; US-GAW1B-003; US-GAP9L-001; US-GAP9L-003; US-GAP9W-001; US-GAP9W-002; US-GAP9W-003; US-GAS5-001; US-GAS5-002; US-GAS5-003; US-GAS5-004; US-GAS5-005; US-GAS5-006; US-GAS5-007; US-GAS5-008; US-GAS5-009; US-GAS5-010; US-GAS5-011; US-GAS5-012; US-GAS5-013; US-GAS5-014; US-GAS5-015; US-GAS5-016; US-GAS5-017; US-GAS5-019; US-GAS5-020; US-GAS5-021; US-GAS5-022; US-GAS5-023; US-HI-002; US-HI-003; US-HIP51-001; US-HIP51-002; US-HIP51-003; US-HIP52-001; US-HIP52-002; US-HIL-001; US-HIL-002; US-HIL-003; US-HIP7-002; US-HIP7-003; US-HIP9L-001; US-HIP9L-002; US-HIP9V-001; US-HIP9V-002; US-HIS5-001; US-HIS5-002; US-HIS5-003; US-HIS5-004; US-HIS5-005; US-HIS5-006; US-HIS5-007; US-HIS5-008; US-HIS5-009; US-HIS5-010; US-HIS5-011; US-HIS5-012; US-HIS5-013; US-HIS5-014; US-HIS5-015; US-HIS5-016; US-HIS5-017; US-HIS5-018; US-HIS5-019; US-HIS5-020; US-HIS5-021; US-HIS5-022; US-HIS5-023; US-HIS5-024; US-HIS5-025; US-HIS5-026; US-HIS5-027; US-HIS5-028; US-HIS5-029; US-HIS5-031; US-IA-001; US-IA-002; US-IAP51-001; US-IAP51-002; US-IAP51-003; US-IAP51-004; US-IAP51-005; US-IAP52-001; US-IAP52-002; US-IAL-001; US-IAL-002; US-IAP9L-001; US-IAP9L-002; US-IAP9V-001; US-IAP9W-001; US-IAS5-001; US-IAS5-002; US-IAS5-003; US-IAS5-004; US-IAS5-005; US-IAS5-006; US-IAS5-009; US-IAS5-010; US-IAS5-011; US-IAS5-012; US-IAS5-013; US-IAS5-014; US-IAS5-015; US-IAS5-016; US-IAS5-017; US-IAS5-018; US-IAS5-019; US-IAS5-020; US-IAS5-021; US-IAS5-022; US-IAS5-023; US-IAS5-024; US-IAS5-025; US-IAS5-026; US-IAS5-027; US-IAS5-028; US-IAS5-029; US-IDP51-001; US-IDP51-002; US-IDP52-001; US-IDP52-002; US-IDP52-003; US-IDP52-004; US-IDP52-005; US-IDP7-001; US-IDP9M-001; US-IDR3-001; US-IDR3-002; US-IDR3-003; US-IDS5-001; US-IDS5-002; US-IDS5-003; US-IDS5-004; US-IDS5-005; US-IDS5-006; US-IDS5-007; US-IDS5-008; US-IDS5-009; US-IDS5-010; US-IDS5-011; US-IDS5-013; US-IDS5-014; US-IDS5-015; US-IDS5-016; US-IDS5-017; US-IDS5-018; US-IDS5-019; US-IDS5-020; US-IDS5-021; US-IDS5-022; US-IDS5-023; US-IDS5-024; US-IDS5-025; US-IL-002; US-IL-004; US-ILP51-001; US-ILP52-001; US-ILP52-002; US-ILP52-003; US-ILP52-004; US-ILP9L-001; US-ILR3-001; US-ILR3-002; US-ILS5-001; US-ILS5-002; US-ILS5-003; US-ILS5-004; US-ILS5-005; US-ILS5-006; US-ILS5-007; US-ILS5-008; US-ILS5-009; US-ILS5-010; US-ILS5-011; US-ILS5-012; US-ILS5-013; US-ILS5-014; US-ILS5-015; US-ILS5-016; US-ILS5-017; US-ILS5-018; US-ILS5-019; US-ILS5-020; US-ILS5-021; US-ILS5-022; US-ILS5-023; US-ILS5-024; US-ILS5-025; US-ILS5-026; US-IN-002; US-IN-003; US-INP6-001; US-INP7-001; US-INP9L-001; US-INR3-001; US-INR3-002; US-INR3-005; US-INR3-006; US-INR3-008; US-INS5-001; US-INS5-002; US-INS5-003; US-INS5-004; US-INS5-005; US-INS5-006; US-INS5-007; US-INS5-008; US-INS5-009; US-INS5-010; US-INS5-011; US-INS5-012; US-INS5-014; US-INS5-015; US-INS5-016; US-INS5-017; US-INS5-018; US-INS5-020; US-INS5-021; US-KSP51-003; US-KSP51-005; US-KSP52-001; US-KSP52-002; US-KSP52-003; US-KSP9L-002; US-KSP9V-001; US-KSP9V-002; US-KSS5-001; US-KSS5-002; US-KSS5-003; US-KSS5-004; US-KSS5-005; US-KSS5-006; US-KSS5-007; US-KSS5-008; US-KSS5-009; US-KSS5-010; US-KSS5-011; US-KSS5-012; US-KSS5-013; US-KSS5-014; US-KSS5-015; US-KSS5-016; US-KSS5-017; US-KSS5-018; US-KSS5-019; US-KSS5-020; US-KSS5-021; US-KSS5-022; US-KSS5-023; US-KSS5-024; US-KSS5-025; US-KSS5-026; US-KSS5-027; US-KSS5-028; US-KSS5-029; US-KY-001; US-KY-002; US-KY-003; US-KYP51-002; US-KYP52-001; US-KYP52-002; US-KYP52-004; US-KYP7-001; US-KYP8-001; US-KYP8-002; US-KYP9L-001; US-KYP9V-001; US-KYP9W-001; US-KYP9W-002; US-KYR3-001; US-KYR3-002; US-KYR3-003; US-KYS5-001; US-KYS5-002; US-KYS5-003; US-KYS5-004; US-KYS5-005; US-KYS5-006; US-KYS5-007; US-KYS5-008; US-KYS5-009; US-KYS5-010; US-KYS5-011; US-KYS5-012; US-KYS5-013; US-KYS5-014; US-KYS5-015; US-KYS5-016; US-KYS5-017; US-KYS5-018; US-KYS5-019; US-KYS5-020; US-KYS5-021; US-KYS5-022; US-KYS5-023; US-KYS5-024; US-KYS5-025; US-LAP51-001; US-LAP51-002; US-LAP52-001; US-LAP52-002; US-LAP52-004; US-LAP52-005; US-LAPIT-001; US-LASUI-001; US-LAL-001; US-LAL-002; US-LAP6-001; US-LAP9M-001; US-LAP9V-001; US-LAP9V-002; US-LAR3-001; US-LAR3-002; US-LAS5-001; US-LAS5-002; US-LAS5-003; US-LAS5-004; US-LAS5-005; US-LAS5-006; US-LAS5-007; US-LAS5-009; US-LAS5-010; US-LAS5-012; US-LAS5-013; US-LAS5-014; US-LAS5-015; US-LAS5-016; US-MAP51-003; US-MAP51-005; US-MAP51-008; US-MAP51-009; US-MAL-002; US-MAP7-001; US-MAP7-002; US-MAP9W-004; US-MAR3-001; US-MAR3-002; US-MAR3-003; US-MAS5-001; US-MAS5-002; US-MAS5-003; US-MAS5-004; US-MAS5-005; US-MAS5-006; US-MAS5-007; US-MAS5-008; US-MAS5-009; US-MAS5-010; US-MAS5-011; US-MAS5-012; US-MAS5-013; US-MAS5-014; US-MAS5-015; US-MAS5-016; US-MAS5-017; US-MAS5-018; US-MAS5-019; US-MAS5-020; US-MAS5-021; US-MAS5-022; US-MAS5-023; US-MAS5-024; US-MAS5-025; US-MAS5-026; US-MAS5-028; US-MDP51-001; US-MDP51-002; US-MDP51-005; US-MDP51-006; US-MDL-001; US-MDP9L-001; US-MDP9L-002; US-MDP9V-001; US-MDP9V-002; US-MDS5-001; US-MDS5-003; US-MDS5-004; US-MDS5-005; US-MDS5-006; US-MDS5-007; US-MDS5-008; US-MDS5-009; US-MDS5-010; US-MDS5-011; US-MDS5-012; US-MDS5-013; US-MDS5-014; US-MDS5-015; US-MDS5-016; US-MDS5-017; US-MDS5-018; US-MDS5-019; US-MDS5-020; US-MDS5-021; US-MEP51-001; US-MEP52-001; US-MEP52-002; US-MEP52-003; US-MEP52-004; US-MEP52-005; US-MEP52-009; US-MEL-001; US-MEP6-001; US-MEP7-001; US-MEP7-002; US-MEP9L-001; US-MEP9V-001; US-MER3-001; US-MER3-002; US-MES5-001; US-MES5-002; US-MES5-003; US-MES5-004; US-MES5-006; US-MES5-007; US-MES5-008; US-MES5-010; US-MES5-011; US-MES5-012; US-MES5-013; US-MES5-014; US-MES5-015; US-MES5-016; US-MES5-017; US-MES5-018; US-MES5-019; US-MES5-020; US-MES5-021; US-MES5-022; US-MES5-024; US-MES5-025; US-MES5-026; US-MES5-027; US-MES5-028; US-MIP51-001; US-MIP51-002; US-MIP51-003; US-MIP51-004; US-MIP51-005; US-MIP51-006; US-MIP52-001; US-MIP52-002; US-MIP52-004; US-MIP52-005; US-MIP52-011; US-MIPIT-001; US-MIL-001; US-MIL-002; US-MIP9L-001; US-MIP9V-001; US-MIP9W-001; US-MIP9W-002; US-MIR3-001; US-MIR3-002; US-MIR3-003; US-MIS5-001; US-MIS5-002; US-MIS5-003; US-MIS5-004; US-MIS5-005; US-MIS5-006; US-MIS5-007; US-MIS5-008; US-MIS5-009; US-MIS5-010; US-MIS5-011; US-MIS5-012; US-MIS5-013; US-MIS5-014; US-MIS5-015; US-MIS5-016; US-MIS5-017; US-MIS5-018; US-MIS5-019; US-MIS5-020; US-MIS5-021; US-MIS5-022; US-MIS5-023; US-MIS5-024; US-MIS5-025; US-MIS5-026; US-MULTI-008; US-MULTI-009; US-MULTI-010; US-MULTI-016; US-MULTI-018; US-MULTI-019; US-MULTI-020; US-MULTIS5-021; US-OWN-007

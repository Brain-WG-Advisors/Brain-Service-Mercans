# Chad design v4 — what changed from v3

v4 keeps every statutory position of v3 (BIK capped, family allowances fully exempt, TFE / TAFP on the Art. 189 base, non-resident base net of Art. 45, TFE / TAFP relief) and applies the answers given in the 16 Oct 2026 design call, plus the accounts the seven Chad report specs read.

| # | Change | Rule |
|---|---|---|
| 1 | **Status in the global flag 58218**: 0 resident · 1 non-resident · 2 disabled · 3 young graduate · 4 diplomatic. Residents routed with `LESS($58218;1)`. 58201 no longer used | 58218 is the global residency flag; 58201 is reserved for advanced reconciliation |
| 2 | **Young-graduate months in 58205** (replaces the five-year flag 58208); exemption while 58205 ≤ 60 | The IRPP-TS report reads 58205 |
| 3 | **TFE / TAFP relief in 58206** (replaces 58209): 0 none · 1 exempt · 2 50% | Flag meaning as in the catalogue; plan social moves to 58210 |
| 4 | **`retro_` back** on every regulation with a floor, a ceiling or a progressive table (see ASSUMPTIONS A11) | Default unless the law forbids retro or there is no ceiling, floor or table. v2 had removed it by copying production |
| 5 | **Derived limits in their own regulations, applied as ceiling accounts**: 9148014 (transport 30% → 58171, Art. 47 3.5% → 58172) and 9148015 (the nine Art. 46 caps → 58161–58169, one band each). The transport, retirement and nine BIK regulations now read the limit through `ceilingAccount` instead of a `MIN()` formula | A limit that depends on another value is computed in a regulation and enters as a ceiling account; a fixed limit stays in the band's floor / ceiling |
| 6 | **`_$$`** on the employee deductions that enter the gross-up: CNPS (9148053), IRPP resident (9148073) and non-resident (9148075) | `_$$` marks the value as gross-up eligible |
| 7 | **Accounts the report specs read**: 58105 cash gross (was 58102) · 58008 IRPP gross (was 58121) · 58104 transport exempt (was 58103) · 58108 family exempt (was 58104) · 58120–58128 capped BIK (were 58111–58119, now in the DAS order: housing, vehicle, food, furnishings, domestic, electricity, water, telephone, gas) · 58130 CNPS gross (was 58131) · 58552 IRPP taxable income (was 58151) | The development team configures the design from the report specs before designing |
| 8 | **New reporting values**: 9148013 Annual Reporting Limit (58106 = 60,000 a month, DAS) · band 6 of 9148053 writes the total CNPS rate 20 in 58131 (Récapitulatif) · flag 58212 dependent children (DAS) | Everything a report asks for, including percentages, lives in the design |
| 9 | Base salary moved to 58109 (was 58101); plan-social exemption to 58113 (was 58105) | Free the numbers the reports use |
| 10 | Matrices unchanged: code by code against the WTC | Confirmed on 16 Oct |

Results: the 10 scenarios executed give the same EE CNPS, IRPP, TFE, TAFP and net pay as v3 (VALIDATION.md).

# V11 research fixes: facts changes (2026-11-06, source-hunter)

Origin: `../validacao-estados/compare/VERIFY-S1.md` (V-01..V-04) and `FINDINGS.md` (V-09, V-13). Facts edited under `_research/facts.lock`. Backups are in `_pipeline/_backup/v11-facts-2026-11-06/`. Register shard: `00-official-sources/_register-shards/S7-V11.csv`, merged into `legal-basis-register.csv` (2,707 → 2,712 rows, no id collisions).

## Register rows

| id | instrument | status | effective |
|---|---|---|---|
| US-GAV7-001 | GA DOR Employer's Withholding Tax Guide 2026, rev. Dec 2025, Table E (5.19%); Wayback 2026-01-16 | superseded | 2026-01-01..2026-05-10 |
| US-GAV7-002 | GA DOR guide updated June 2026, What's New (HB 463 transition: keep 5.19% until 2026-05-11); Wayback 2026-09-13 | active | from 2026-05-11 (supersedes US-GAV7-001) |
| US-NYV7-001 | NYS-50-T-NYS (1/26) Method II Tables A-C, Annual Tax Rate Schedules; Method III | active | 2026 |
| US-NYV7-002 | NYS-50-T-NYC (1/26) Method II Tables A-C, Annual Tax Rate Schedules | active | 2026 |
| US-NYV7-003 | NYS-50-T-Y (1/26) resident surcharge Method II/III; nonresident Methods VII/VIII | active | 2026 |

Other register edits: US-GAS5-001 `supersedes` = US-GAV7-001. Entries appended to `consumed_by`: US-GAS5-001 += WTC/country_specific; US-FEDS5-001 += CCG/annex_FED; US-NYP8-001 and US-NYB5-001 += CCG/annex_NY. GA guide texts were copied into `00-official-sources/ccg-sources/GA/`; the PDFs stay in `validacao-estados/oracle/_src_live/`.

## Fix 1: GA (V-04, S1)

| file | key | old | new | source | register |
|---|---|---|---|---|---|
| CCG-annex_GA-facts.json | `ga.wh.method` | 4.99% formula from 2026-01-01 (open) | 5.19% / Table E Dec-2025 formula 2026-01-01..2026-05-10 [US-GAV7-001]; 4.99% formula from 2026-05-11 [US-GAS5-001] | GA DOR guide Dec-2025 p.46; Jun-2026 p.3 | US-GAV7-001; US-GAS5-001 |
| CCG-annex_GA-facts.json | `ga.wh.std_deduction.mfj` | 30000 from 2026-01-01 (open) | 24000 2026-01-01..2026-05-10 [US-GAV7-001]; 30000 from 2026-05-11 [US-GAS5-001] | GA DOR guide Dec-2025 Table E; Jun-2026 What's New | US-GAV7-001; US-GAS5-001 |
| CCG-annex_GA-facts.json | `ga.wh.std_deduction.single` | 15000 from 2026-01-01 (open) | 12000 2026-01-01..2026-05-10 [US-GAV7-001]; 15000 from 2026-05-11 [US-GAS5-001] | GA DOR guide Dec-2025 Table E; Jun-2026 What's New | US-GAV7-001; US-GAS5-001 |
| CCG-annex_GA-facts.json | `ga.wh.dependent_allowance` | 5000 from 2026-01-01 (open) | 4000 2026-01-01..2026-05-10 [US-GAV7-001]; 5000 from 2026-05-11 [US-GAS5-001] | GA DOR guide Dec-2025 Table E; Jun-2026 What's New | US-GAV7-001; US-GAS5-001 |
| WTC-country_specific-facts.json | `ga.wh.std_deduction.single` | 15000 from 2026-01-01 (open) | 12000 2026-01-01..2026-05-10 [US-GAV7-001]; 15000 from 2026-05-11 [US-GAS5-001] | GA DOR guide Dec-2025 Table E; Jun-2026 What's New | US-GAV7-001; US-GAS5-001 |
| WTC-country_specific-facts.json | `ga.wh.std_deduction.mfj` | 30000 from 2026-01-01 (open) | 24000 2026-01-01..2026-05-10 [US-GAV7-001]; 30000 from 2026-05-11 [US-GAS5-001] | GA DOR guide Dec-2025 Table E; Jun-2026 What's New | US-GAV7-001; US-GAS5-001 |
| WTC-country_specific-facts.json | `ga.wh.dependent_allowance` | 5000 from 2026-01-01 (open) | 4000 2026-01-01..2026-05-10 [US-GAV7-001]; 5000 from 2026-05-11 [US-GAS5-001] | GA DOR guide Dec-2025 Table E; Jun-2026 What's New | US-GAV7-001; US-GAS5-001 |
| WTC-country_specific-facts.json | `ga.sit.method` | 4.99% formula from 2026-01-01 (open) | 5.19% / Table E Dec-2025 formula 2026-01-01..2026-05-10 [US-GAV7-001]; 4.99% formula from 2026-05-11 [US-GAS5-001] | GA DOR guide Dec-2025 p.46; Jun-2026 p.3 | US-GAV7-001; US-GAS5-001 |

- The `ga.wh.rate` split already existed: 5.19 for 2026-01-01..05-10 [US-GA-001] and 4.99 from 2026-05-11 [US-GAS5-009]. It is unchanged in CCG-annex_GA, CCG-m06_tax and WTC-country_specific.
- `ga.wh.std_deduction.mfs` and `.hoh` do not exist as keys. MFS and HoH equal the Single column in both guides (12,000 → 15,000), as recorded in the notes. No new key was added.
- DD-8_sheets and PSL facts carry no GA withholding keys, so there was nothing to split there.
- G-DERIVE: all 21 Dec-2025 per-period values equal annual / periods, half-up to the cent (Python).
- Downstream to re-sync (agent 3): `01-ccg/annexes/annex_GA.md` L6 and L33-35, the `m06` §6.1 "Flat rate" line, and the WTC US-1xx GA rows (PROPAGATION-LEDGER).

## Fix 2: NY Method II (V-01..V-03, S2)

All added to `CCG-annex_NY-facts.json`, 2026-01-01..2026-12-31, tier A.2, `quoted from authority page`. Old value = absent.

| key | new value | register |
|---|---|---|
| `ny.pfl.employee.max_annual.accumulation` | calendar-year accumulator per employee: apply the PFL rate to wages each pay period unt... | US-NYB5-001 |
| `ny.pfl.employee.max_annual.accumulation` | calendar-year accumulator per employee: apply the PFL rate to wages each pay period unt... | US-NYP8-001 |
| `ny.wh.method2.single.bracket.1.floor` | 0 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.1.rate` | 3.9 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.1.base` | 0 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.2.floor` | 8500 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.2.rate` | 4.4 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.2.base` | 332 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.3.floor` | 11700 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.3.rate` | 5.15 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.3.base` | 472 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.4.floor` | 13900 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.4.rate` | 5.4 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.4.base` | 586 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.5.floor` | 80650 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.5.rate` | 5.9 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.5.base` | 4190 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.6.floor` | 96800 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.6.rate` | 7.03 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.6.base` | 5143 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.7.floor` | 107650 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.7.rate` | 7.53 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.7.base` | 5906 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.8.floor` | 157650 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.8.rate` | 6.4 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.8.base` | 9673 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.9.floor` | 215400 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.9.rate` | 11.44 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.9.base` | 13369 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.10.floor` | 265400 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.10.rate` | 7.35 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.bracket.10.base` | 19091 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.single.deduction_allowance` | 7400 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method3.single.threshold` | 1077550 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method3.single.bracket.1.floor` | 1077550 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method3.single.bracket.1.rate` | 10.45 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method3.single.bracket.2.floor` | 5000000 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method3.single.bracket.2.rate` | 11.1 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method3.single.bracket.3.floor` | 25000000 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method3.single.bracket.3.rate` | 11.7 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.1.floor` | 0 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.1.rate` | 3.9 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.1.base` | 0 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.2.floor` | 8500 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.2.rate` | 4.4 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.2.base` | 332 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.3.floor` | 11700 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.3.rate` | 5.15 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.3.base` | 472 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.4.floor` | 13900 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.4.rate` | 5.4 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.4.base` | 586 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.5.floor` | 80650 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.5.rate` | 5.9 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.5.base` | 4190 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.6.floor` | 96800 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.6.rate` | 6.57 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.6.base` | 5143 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.7.floor` | 107650 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.7.rate` | 7.07 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.7.base` | 5855 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.8.floor` | 157650 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.8.rate` | 8.01 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.8.base` | 9388 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.9.floor` | 211550 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.9.rate` | 6.4 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.9.base` | 13708 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.10.floor` | 323200 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.10.rate` | 13.49 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.10.base` | 20854 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.11.floor` | 373200 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.11.rate` | 7.35 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.11.base` | 27600 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.12.floor` | 1077550 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.12.rate` | 7.65 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.bracket.12.base` | 79369 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.married.deduction_allowance` | 7950 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method3.married.threshold` | 2155350 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method3.married.bracket.1.floor` | 2155350 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method3.married.bracket.1.rate` | 10.45 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method3.married.bracket.2.floor` | 5000000 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method3.married.bracket.2.rate` | 11.1 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method3.married.bracket.3.floor` | 25000000 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method3.married.bracket.3.rate` | 11.7 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.exemption_allowance` | 1000 [2026-01-01..2026-12-31] | US-NYV7-001 |
| `ny.wh.method2.annualisation` | Method II: net wages = wages - Table A allowance for the payroll period; apply the per-... | US-NYV7-001 |
| `ny.wh.method3.annualisation` | Method III: annualized wages = Method II net wages x payroll periods per year (e.g. 52,... | US-NYV7-001 |
| `ny.local.nyc.method2.single.bracket.1.floor` | 0 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.1.rate` | 2.05 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.1.base` | 0 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.2.floor` | 8000 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.2.rate` | 2.8 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.2.base` | 164 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.3.floor` | 8700 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.3.rate` | 3.25 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.3.base` | 184 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.4.floor` | 15000 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.4.rate` | 3.95 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.4.base` | 388 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.5.floor` | 25000 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.5.rate` | 4.15 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.5.base` | 783 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.6.floor` | 60000 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.6.rate` | 4.25 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.bracket.6.base` | 2236 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.single.deduction_allowance` | 5000 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.1.floor` | 0 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.1.rate` | 2.05 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.1.base` | 0 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.2.floor` | 8000 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.2.rate` | 2.8 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.2.base` | 164 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.3.floor` | 8700 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.3.rate` | 3.25 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.3.base` | 184 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.4.floor` | 15000 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.4.rate` | 3.95 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.4.base` | 388 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.5.floor` | 25000 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.5.rate` | 4.15 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.5.base` | 783 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.6.floor` | 60000 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.6.rate` | 4.25 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.bracket.6.base` | 2236 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.married.deduction_allowance` | 5500 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.exemption_allowance` | 1000 [2026-01-01..2026-12-31] | US-NYV7-002 |
| `ny.local.nyc.method2.annualisation` | Same steps as NYS Method II with the NYC Tables A-C and NYC schedules; NYC has no Metho... | US-NYV7-002 |
| `ny.local.yonkers.resident.surcharge.rate` | 16.75 [2026-01-01..2026-12-31] | US-NYV7-003 |
| `ny.local.yonkers.resident.surcharge.method` | Compute the New York State withholding with NYS Method II (NYS Tables A-C and NYS annua... | US-NYV7-003 |
| `ny.local.yonkers.nonresident.earnings_tax.rate` | 0.5 [2026-01-01..2026-12-31] | US-NYV7-003 |
| `ny.local.yonkers.nonresident.earnings_tax.method` | Method VII per-period exclusion tables, or Method VIII: annualize gross wages (x 260/52... | US-NYV7-003 |
| `ny.local.yonkers.nonresident.method8.bracket.1.floor` | 0 [2026-01-01..2026-12-31] | US-NYV7-003 |
| `ny.local.yonkers.nonresident.method8.bracket.2.floor` | 3999.99 [2026-01-01..2026-12-31] | US-NYV7-003 |
| `ny.local.yonkers.nonresident.method8.bracket.2.exclusion` | 3000 [2026-01-01..2026-12-31] | US-NYV7-003 |
| `ny.local.yonkers.nonresident.method8.bracket.3.floor` | 10000 [2026-01-01..2026-12-31] | US-NYV7-003 |
| `ny.local.yonkers.nonresident.method8.bracket.3.exclusion` | 2000 [2026-01-01..2026-12-31] | US-NYV7-003 |
| `ny.local.yonkers.nonresident.method8.bracket.4.floor` | 20000 [2026-01-01..2026-12-31] | US-NYV7-003 |
| `ny.local.yonkers.nonresident.method8.bracket.4.exclusion` | 1000 [2026-01-01..2026-12-31] | US-NYV7-003 |
| `ny.local.yonkers.nonresident.method8.bracket.5.floor` | 30000 [2026-01-01..2026-12-31] | US-NYV7-003 |
| `ny.local.yonkers.nonresident.method8.bracket.5.exclusion` | 0 [2026-01-01..2026-12-31] | US-NYV7-003 |
| `ny.local.yonkers.nonresident.no_withholding.below` | 4000 [2026-01-01..2026-12-31] | US-NYV7-003 |

- Unresolved added: `ny.wh.method2.rounding` (non-blocking). The publication prints no rounding instruction, so none is encoded; it references RQ-263.
- The new allowance keys coincide with the existing `ny.sit.deduction_allowance.{single,married}.annual` and `ny.pit.exemption.annual`. It is the same mechanism under two keys; neither was renamed.
- Cross-check: an independent parse of the source text matched all 34 bracket floor/rate/base triples (NYS 10+12, NYC 6+6) with 0 mismatches.

## S3 notes

- V-09: added `fed.fit.pre2020_w4.filing_status_mapping` to CCG-annex_FED (2026). Pub. 15-T (2026) pp.5-6 computational bridge items 1-4 and Worksheet 1A Step 2 "Don't use the Head of Household table if the Form W-4 is from 2019 or earlier". Register US-FEDS5-001.
- V-13: added `ny.pfl.employee.max_annual.accumulation` to CCG-annex_NY, as two dated facts: 2026 [US-NYP8-001, cap 411.91] and from 2027 [US-NYB5-001, cap 451.81]. Both DFS decisions state that contributions stop once they reach the annual maximum within the calendar year.

## Validation

- `validate_contract.py facts` on CCG-annex_GA, CCG-annex_NY, CCG-annex_FED, WTC-country_specific and CCG-m06_tax: PASS. `--all .`: PASS (118 files).
- `research_checks.py --checks C40,C41` (F43/F44): C40 PASS (18/18), C41 PASS. The new GA facts ending 2026-05-10 are accepted as superseded in the build year (successor starts 2026-05-11).

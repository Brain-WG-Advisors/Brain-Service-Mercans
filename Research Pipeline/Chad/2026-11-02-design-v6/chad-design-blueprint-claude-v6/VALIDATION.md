# Chad v6 — validation (2026-11-02, after the v6 QA rounds 1 and 2)

v6 = the v5 rules in the form of the Dev design (CHANGELOG.md), plus the matrix fixes of rounds 2 and 3 (QA V1, W1, W2 and the full sweep) — defects that **v5 also has**. Test: the 12 scenarios and 20 extra checks of v5 plus E21–E26, run on the v6 regulations as written (`../_build_v6.py`), compared (1) with hand-computed expected values (EE CNPS, IRPP, TFE, TAFP, PSA, net), no tolerance, and (2) with the v5 engine (read only) account by account on 39 accounts plus the 58110/58111 check.

## Result
- **12 / 12 scenarios and 26 / 26 extra checks equal to the expected values.**
- **v6 = v5 on every account of every case except the six explicit ones** (1,540 values compared, 0 unexpected differences):

| Case | Fix | v5 → v6 |
|---|---|---|
| 5 Individual severance 900,000 | r3 W2: severance in the TF base (Art. 189-1°) | TFE base 300,000 → 1,200,000; TFE 22,500 → **90,000** |
| E21 Car fuel arrears 65521 50,000 | r2 V1: 6552% | IRPP 23,214 → **26,364**; TFE 22,500 → 26,250; TAFP 3,600 → 4,200 |
| E23 Medical insurance 62610 50,000 | r3 W1: 6261% | EE CNPS 10,500 → 12,250; IRPP 23,398 → **28,464**; TFE 22,500 → 26,250; TAFP 3,600 → 4,200 |
| E24 Social allowance 62651 20,000 | r3 W1: 6265% | EE CNPS 10,500 → 11,200; IRPP 23,398 → **25,424**; TFE 22,500 → 24,000; TAFP 3,600 → 3,840 |
| E25 Statutory EOS gratuity 62900 100,000 | r3 W2: termination payments out of the TA | TAFP 4,800 → **3,600** |
| E26 Phone cash benefit 65610 20,000 | r3 sweep: 6561x in TF/TA | TFE 22,500 → 24,000; TAFP 3,600 → 3,840 |

Hand checks: scenario 5 TFE = 1,200,000 × 7.5% = 90,000. E23: 350,000 − 12,250 = 337,750 → 28,464. E24: 320,000 − 11,200 = 308,800 → (3,705,600 − 800,000) × 10.5% / 12 = 25,424. E25: 400,000 − 10,500 = 389,500 → 406,770 / 12 = 33,897.5 → 33,898; TAFP on 300,000 = 3,600. E26: TF 320,000 × 7.5% = 24,000.

## Sweep of every WTC V3.0 Earning code (QA W1)
554 Earning codes run through the engine (300,000 + 10,000 of the code; `sweep()`, raw list in `../SWEEP-run.txt`). **In no base: 4** — 62560–62563 relocation 2 (reimbursement with receipts, A22). **Different from the WTC columns: 122 codes**, all in these documented groups:

| Series (WTC V3.0) | v6 IRPP/CNPS/TA/TF | WTC | Decision |
|---|---|---|---|
| 62180–62182 Severance | Y/N/N/Y | N/N/N/N | IRPP Art. 44-I (only plan social exempt, 45-10°); TF Art. 189-1°; TA Art. 173 (A20) |
| 62300–62305 Annual leave pay, 62310–62362 Expat allowance | Y/Y/Y/Y | Y/Y/N/Y | TA: salary, not a gratification (Art. 173; A30) |
| 62510–62523 Transport | Y/N/Y/Y | Y/Y/Y/Y | CNPS: whole transport out (guide p. 8; D1, front decision pending the user’s ok) |
| 62550–62552 Leave ticket, 62570 / 65570–65582 Per diem | Y/N/Y/Y | N/N/N/N | IRPP with the Art. 45-15° / 45-2° exempt parts; TF/TA « indemnités diverses »; CNPS out (guide p. 8) |
| 62560–62563 Relocation 2 | N/N/N/N | N/N/N/N | Reimbursement with receipts — in no base (A22) |
| 62640–62649 Pensions | N/N/N/Y | Y/Y/Y/Y | IRPP exempt Art. 45-1°; TF Arts. 187, 189-1° « pensions »; not pay for CNPS / TA |
| 62740–62742 Schooling allowance 4 | Y/Y/Y/Y | N/N/N/N | Cash allowance, not a « bourse » (Art. 45-9° a contrario; R19) |
| 62780–62782 Family allowance | Y/N/Y/Y | Y/Y/Y/Y | Family allowances out of CNPS (guide p. 8); IRPP above the Art. 45-4° cap |
| 62900–62909, 62910–62935 EOS gratuities | Y/N/N/Y | Y/Y-N/Y/Y | CNPS « dédommagement » (Dec. 1635 art. 3); TA out (Art. 173) |
| 654xx, 655xx, 656xx, 6585x benefits in kind | Y/Y/Y/Y | N/Y/Y/Y | IRPP at the capped value of Art. 46-III (the WTC "Tax No" means "not at real value") |
| 65630 Health Insurance Benefit | Y/Y/Y/Y | N/N/N/N | Verdict 25 — no Art. 45 exemption (R18) |
| 65800–65809 School Scholarship | N/Y/Y/Y | N/N/N/N | IRPP exempt Art. 45-9°; TF/TA and CNPS in (R19) |

## `retro_` (A11) and E22
Arrears of 100,000 for a month paid 300,000, paid in a month of 900,000 → IRPP 147,375 on the payment basis (v6, Dev) vs 132,507 if the original month were re-run; EE CNPS 17,500 vs 21,000. E22: arrears 62101 of 100,000 on 450,000 → EE 17,500, IRPP 50,375, TFE 41,250, TAFP 6,600.

## Raw output
```
## 12 scenarios
| Scenario | EE CNPS | IRPP | TFE | TAFP | PSA | Net | status |
| 1 Active baseline 350,000 | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | OK |
| 2 Zero salary | 0 | 0 | 0 | 0 | 0 | 0 | OK |
| 3 13th month | 17,500 | 75,750 | 52,500 | 8,400 | 400 | 606,350 | OK |
| 4 Housing real 50,000 under a 120,000 cap | 17,500 | 65,750 | 48,750 | 7,800 | 400 | 516,350 | OK |
| 5 Individual severance 900,000 | 10,500 | 208,600 | 90,000 | 3,600 | 400 | 980,500 | OK |
| 6 Compulsory supplementary pension 30,000 (cap 14,000) | 14,000 | 32,060 | 30,000 | 4,800 | 400 | 323,540 | OK |
| 7 Transport 120,000, granted to all (CNPS: transport out in full) | 10,500 | 26,548 | 31,500 | 5,040 | 400 | 382,552 | OK |
| 8 Family allowance 30,000, 0 children | 10,500 | 26,548 | 24,750 | 3,960 | 400 | 292,552 | OK |
| 9 Entity with 50% relief | 12,250 | 28,464 | 13,125 | 2,100 | 400 | 308,886 | OK |
| 10 Young graduate, month 30, age 30, real-regime entity | 12,250 | 0 | 0 | 0 | 400 | 337,350 | OK |
| 11 Non-resident 800,000 (all CNPS branches, progressive scale) | 17,500 | 97,375 | 60,000 | 9,600 | 400 | 684,725 | OK |
| 12 Family allowance 30,000, 6 children | 10,500 | 23,398 | 24,750 | 3,960 | 400 | 295,702 | OK |
## extra checks of the v5 changes
| Scenario | EE CNPS | IRPP | TFE | TAFP | PSA | Net | status |
| E1 Family 30,000, 6 children, CNPS pays 7,300 | 10,500 | 24,164 | 24,750 | 3,960 | 400 | 294,936 | OK |
| E2 School scholarship 6580x 50,000 | 12,250 | 23,214 | 26,250 | 4,200 | 400 | 264,136 | OK |
| E3 Meal allowance 62860 40,500 (in CNPS; TFE 25,537.5 paid 25,538) | 11,918 | 27,501 | 25,538 | 4,080 | 400 | 300,681 | OK |
| E4 Function allowance 6287x 101,000 (15% cap 60,150) | 10,500 | 27,687 | 30,075 | 4,810 | 400 | 362,413 | OK |
| E5 Worker (ouvrier) aged 25, month 30, real-regime entity -> IRPP, TF, TA exempt | 12,250 | 0 | 0 | 0 | 400 | 337,350 | OK |
| E6 Same worker, entity not under the real regime -> all due | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | OK |
| E7 Voluntary pension 2164x 30,000 (Art. 47-II: not deductible) | 14,000 | 33,530 | 30,000 | 4,800 | 400 | 322,070 | OK |
| E8 Leave ticket 6255x 200,000, annual limit 150,100 | 10,500 | 28,637 | 37,500 | 6,000 | 400 | 460,463 | OK |
| E9 Per diem 62570 50,000 + function allowance 6287x 51,000 (one 15% cap) | 10,500 | 27,687 | 30,075 | 4,810 | 400 | 362,413 | OK |
| E10 Non-resident 800,000 seconded under a convention (CNPS branches off) | 0 | 101,750 | 60,000 | 9,600 | 400 | 697,850 | OK |
| E11 Schooling allowance 6274x 50,000 (taxable everywhere) | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | OK |
| E12 Young graduate aged 36 at recruitment (now 38), real regime, month 30 -> all due | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | OK |
| E13 Young graduate under 35, entity not under the real regime -> all due | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | OK |
| E14 Worker aged 25, month 61 -> IRPP due, TF/TA still exempt | 12,250 | 28,464 | 0 | 0 | 400 | 308,886 | OK |
| E15 One-time bonus 6222x 100,000 -> out of the TAFP base only | 14,000 | 33,530 | 30,000 | 3,600 | 400 | 352,070 | OK |
| E16 Car & transportation allowance 6251x 120,000 -> same as scenario 7 | 10,500 | 26,548 | 31,500 | 5,040 | 400 | 382,552 | OK |
| E17 Pension 6264x 50,000 -> out of IRPP, CNPS, TA; in TF | 10,500 | 23,398 | 26,250 | 3,600 | 400 | 315,702 | OK |
| E18 Worker aged 45, real regime, NO exemption start date (58205 = 0) -> all due | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | OK |
| E19 Worker aged 40 at recruitment (now 42), real regime, month 30 -> all due (restrictive reading, A34) | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | OK |
| E20 Young graduate under 35, real regime, NO start date -> IRPP due; TF/TA exempt (Arts. 188-10, 174-3 need no date) | 12,250 | 28,464 | 0 | 0 | 400 | 308,886 | OK |
| E21 Arrears of car fuel benefit 65521 50,000 -> vehicle cap 30,000 in IRPP; real value in TF/TA and CNPS (v6 r2, QA V1) | 12,250 | 26,364 | 26,250 | 4,200 | 400 | 260,986 | OK |
| E22 Arrears of base salary 62101 100,000 on base 450,000 -> taxed in the month paid (no retro_, QA V2) | 17,500 | 50,375 | 41,250 | 6,600 | 400 | 481,725 | OK |
| E23 Medical insurance 62610 50,000 -> taxable everywhere (verdict 25; v6 r3, QA W1) | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | OK |
| E24 Social allowance 62651 20,000 -> taxable everywhere (Art. 44-I; v6 r3, QA W1) | 11,200 | 25,424 | 24,000 | 3,840 | 400 | 282,976 | OK |
| E25 Statutory EOS gratuity 62900 100,000 -> IRPP and TF; out of CNPS and TA (v6 r3, QA W2) | 10,500 | 33,898 | 30,000 | 3,600 | 400 | 355,202 | OK |
| E26 Phone cash benefit 65610 20,000 -> IRPP, CNPS, TF and TA (v6 r3, sweep) | 11,200 | 25,424 | 24,000 | 3,840 | 400 | 262,976 | OK |
S11: 58552 = 782,500 · 58592 = 782,500 · 2592 = 97,375 · 2552 = 0 · 58563 = 800,000 · 58534 = 800,000
S12: 58107 = 30,000 · 58108 = -30,000 · 58552 = 289,500
ALL EXPECTED (exact, every column)
v6 vs v5 engine: 38 cases x 39 accounts (+ 58110/58111 checks) = 1540 values compared, 0 unexpected differences
expected differences (QA V1 fix, v5 also affected): 5 58563: v5 300,000 -> v6 1,200,000; 5 2563: v5 22,500 -> v6 90,000; E21 58112: v5 23,214 -> v6 26,364; E21 58008: v5 300,000 -> v6 330,000; E21 58563: v5 300,000 -> v6 350,000; E21 58534: v5 300,000 -> v6 350,000; E21 58552: v5 287,750 -> v6 317,750; E21 58121: v5 0 -> v6 30,000; E21 2552: v5 23,214 -> v6 26,364; E21 2563: v5 22,500 -> v6 26,250; E21 2534: v5 3,600 -> v6 4,200; E23 58112: v5 23,398 -> v6 28,464; E23 58105: v5 300,000 -> v6 350,000; E23 58008: v5 300,000 -> v6 350,000; E23 58130: v5 300,000 -> v6 350,000; E23 58550: v5 300,000 -> v6 350,000; E23 58563: v5 300,000 -> v6 350,000; E23 58534: v5 300,000 -> v6 350,000; E23 58100: v5 -10,500 -> v6 -12,250; E23 58552: v5 289,500 -> v6 337,750; E23 2551: v5 10,500 -> v6 12,250; E23 2550: v5 22,500 -> v6 26,250; E23 2537: v5 15,000 -> v6 17,500; E23 2560: v5 12,000 -> v6 14,000; E23 2552: v5 23,398 -> v6 28,464; E23 2563: v5 22,500 -> v6 26,250; E23 2534: v5 3,600 -> v6 4,200; E24 58112: v5 23,398 -> v6 25,424; E24 58105: v5 300,000 -> v6 320,000; E24 58008: v5 300,000 -> v6 320,000; E24 58130: v5 300,000 -> v6 320,000; E24 58550: v5 300,000 -> v6 320,000; E24 58563: v5 300,000 -> v6 320,000; E24 58534: v5 300,000 -> v6 320,000; E24 58100: v5 -10,500 -> v6 -11,200; E24 58552: v5 289,500 -> v6 308,800; E24 2551: v5 10,500 -> v6 11,200; E24 2550: v5 22,500 -> v6 24,000; E24 2537: v5 15,000 -> v6 16,000; E24 2560: v5 12,000 -> v6 12,800; E24 2552: v5 23,398 -> v6 25,424; E24 2563: v5 22,500 -> v6 24,000; E24 2534: v5 3,600 -> v6 3,840; E25 58534: v5 400,000 -> v6 300,000; E25 2534: v5 4,800 -> v6 3,600; E26 58563: v5 300,000 -> v6 320,000; E26 58534: v5 300,000 -> v6 320,000; E26 2563: v5 22,500 -> v6 24,000; E26 2534: v5 3,600 -> v6 3,840
retro_ effect (arrears 100,000 for a 300,000 month, paid in a 900,000 month): IRPP payment basis 147,375 vs re-run of the original month 132,507; EE CNPS 17,500 vs 21,000
regulations: v6 36 · v5 35
sweep of the WTC V3.0 Earning codes: 554 codes, 4 in no base (relocation 2 / 6256x reimbursements, A22), 122 different from the WTC columns (SWEEP-run.txt)
```

## What is not validated
Not loaded into an engine: arrears without `retro_` (A11), `$period_divisor` and the `simple_tax_monthly` differential, BIK caps inside `MIN()`, equal band limits (A21), 58205 in the month of hire (A13), 58106 with an empty matrix (A16).

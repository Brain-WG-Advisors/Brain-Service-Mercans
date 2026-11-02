# Chad v5 — validation (round 4, after QA round 2, 2026-11-01)

Results come from executing the regulations as written (`../_build_v5.py`: it generates SKILL.md from the same data it executes; raw output in `../VALIDATION-run.txt`). **Expected** values were computed by hand from the CGI 2026 (DGI edition), the CNPS decrees 1635/1636 of 2009 and the CNPS employer guide 2019, and typed into the script; they are not produced by the engine. **No tolerance:** a scenario passes only if every column equals the hand value. Net = cash pay (62xxx) − EE CNPS − IRPP − PSA − 21xxx deductions. Defaults: resident, every CNPS branch, transport granted to all, real-regime entity (58215 = 1), age 30 (28 at recruitment), not a worker, 0 children.

Round 3 fixed the QA findings (`../QA-REVIEW.md`): band limits at the round figure, TFE paid to the franc, Art. 3-4° (age, real regime, workers), TAFP base per Art. 173, 6251x in the transport exemption, WTC V3.0 accounts. Round 4 fixed QA round 2: Art. 3-4° needs a start date (58205 > 0), workers also under 35 at recruitment (restrictive reading, 60%, A34), decisions labelled as the front's (pending the user's ok).

## 12 scenarios — expected × obtained

| # | Scenario | EE CNPS | IRPP | TFE | TAFP | PSA | Net | Result |
|---|---|---|---|---|---|---|---|---|
| 1 | Active baseline 350,000 | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | ✅ |
| 2 | Zero salary | 0 | 0 | 0 | 0 | 0 | 0 | ✅ |
| 3 | 13th month (350,000 + 350,000) ¹ | 17,500 | 75,750 | 52,500 | 8,400 | 400 | 606,350 | ✅ |
| 4 | Housing real 50,000 under a 120,000 cap | 17,500 | 65,750 | 48,750 | 7,800 | 400 | 516,350 | ✅ |
| 5 | Individual severance 900,000 ¹ | 10,500 | 208,600 | 22,500 | 3,600 | 400 | 980,500 | ✅ |
| 6 | Compulsory supplementary pension 30,000 (cap 14,000) ² | 14,000 | 32,060 | 30,000 | 4,800 | 400 | 323,540 | ✅ |
| 7 | Transport 120,000, granted to all — CNPS: transport out in full (front decision D1, pending the user's ok) | 10,500 | 26,548 | 31,500 | 5,040 | 400 | 382,552 | ✅ |
| 8 | Family allowance 30,000, 0 children (all taxable) | 10,500 | 26,548 | 24,750 | 3,960 | 400 | 292,552 | ✅ |
| 9 | Entity with 50% relief | 12,250 | 28,464 | 13,125 | 2,100 | 400 | 308,886 | ✅ |
| 10 | Young graduate, month 30, 28 at recruitment, real-regime entity | 12,250 | 0 | 0 | 0 | 400 | 337,350 | ✅ |
| 11 | Non-resident 800,000 — every CNPS branch, progressive scale | 17,500 | 97,375 | 60,000 | 9,600 | 400 | 684,725 | ✅ |
| 12 | Family allowance 30,000, 6 children (cap 30,000) | 10,500 | 23,398 | 24,750 | 3,960 | 400 | 295,702 | ✅ |

**12 of 12 exact.** With the band limits at the round figure (`incomeTo` 800,000 = next `incomeFrom`), 7, 8 and 12 give the literal table value: 26,547.5 → 26,548 and 23,397.5 → 23,398 (FLOOR(x+0.5), technical convention).

¹ **Depends on the withholding method (ASSUMPTIONS A26).** The month is annualised × 12 with the irregular payment inside, as v4 and the Dev do. Under a cumulative (YTD) method the severance month of scenario 5 would withhold ≈ 117,898 (≈ 90,700 less) and the 13th-month of scenario 3 ≈ 64,663 (≈ 11,100 less). The DGI barème of Art. 847 (R23) decides; no CGI article prescribes either.
² 21600 stands for a compulsory-scheme code that the WTC V3.0 does not have yet (R16).

Accounts checked: S11 58552 = 782,500, 58592 = 782,500 (report copy), 2592 = 97,375, 2552 = 0, 58563 = 58534 = 800,000 · S12 58107 = 30,000, 58108 = −30,000, 58552 = 289,500.

## Extra checks of the v5 changes (20)

| # | Check | EE CNPS | IRPP | TFE | TAFP | PSA | Net | Result |
|---|---|---|---|---|---|---|---|---|
| E1 | Family 30,000, 6 children, CNPS pays 7,300 → exempt 22,700 | 10,500 | 24,164 | 24,750 | 3,960 | 400 | 294,936 | ✅ |
| E2 | Scholarship 6580x 50,000 → out of IRPP; in TFE/TAFP and CNPS | 12,250 | 23,214 | 26,250 | 4,200 | 400 | 264,136 | ✅ |
| E3 | Meal allowance 62860 40,500 → in CNPS; TFE 25,537.5 **paid 25,538** | 11,918 | 27,501 | 25,538 | 4,080 | 400 | 300,681 | ✅ |
| E4 | Function allowance 6287x 101,000 → exempt 60,150 (15% of 401,000) | 10,500 | 27,687 | 30,075 | 4,810 | 400 | 362,413 | ✅ |
| E5 | **Worker** aged 25 (28 at recruitment), month 30, real regime → IRPP (Art. 3-4°), TF, TA exempt | 12,250 | 0 | 0 | 0 | 400 | 337,350 | ✅ |
| E6 | Same worker, entity **not** under the real regime → all due | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | ✅ |
| E7 | Voluntary pension 2164x 30,000 → not deductible (Art. 47-II) | 14,000 | 33,530 | 30,000 | 4,800 | 400 | 322,070 | ✅ |
| E8 | Leave ticket 6255x 200,000, annual limit 150,100 ¹ | 10,500 | 28,637 | 37,500 | 6,000 | 400 | 460,463 | ✅ |
| E9 | Per diem 62570 50,000 + 6287x 51,000 → one 15% cap (= E4) | 10,500 | 27,687 | 30,075 | 4,810 | 400 | 362,413 | ✅ |
| E10 | Non-resident 800,000 seconded under a convention (CNPS branches off) | 0 | 101,750 | 60,000 | 9,600 | 400 | 697,850 | ✅ |
| E11 | Schooling allowance 6274x 50,000 → taxable everywhere | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | ✅ |
| E12 | Young graduate **36 at recruitment** (now 38), real regime, month 30 → all due | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | ✅ |
| E13 | Young graduate under 35, entity **not** real regime → all due | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | ✅ |
| E14 | Worker aged 25, **month 61** → IRPP due; TF/TA still exempt (no period in Arts. 188-10°, 174-3°) | 12,250 | 28,464 | 0 | 0 | 400 | 308,886 | ✅ |
| E15 | One-time bonus 6222x 100,000 → out of the TAFP base only (Art. 173) | 14,000 | 33,530 | 30,000 | 3,600 | 400 | 352,070 | ✅ |
| E16 | Car & transportation allowance 6251x 120,000 → same as scenario 7 | 10,500 | 26,548 | 31,500 | 5,040 | 400 | 382,552 | ✅ |
| E17 | Pension 6264x 50,000 → out of IRPP (45-1°), CNPS and TA; in TF (Arts. 187, 189-1°) | 10,500 | 23,398 | 26,250 | 3,600 | 400 | 315,702 | ✅ |
| E18 | Worker aged 45, real regime, **no exemption start date** (58205 = 0) → all due (QA N1) | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | ✅ |
| E19 | Worker **recruited at 40** (now 42), real regime, month 30 → all due (restrictive reading, A34; alternative: IRPP 0) | 12,250 | 28,464 | 26,250 | 4,200 | 400 | 308,886 | ✅ |
| E20 | Young graduate under 35, real regime, **no start date** → IRPP due; TF/TA exempt (Arts. 188-10°, 174-3° need no date) | 12,250 | 28,464 | 0 | 0 | 400 | 308,886 | ✅ |

## v5 × Dev (`../simulacao/`)

`comparar.py` and `sim_dev.py` are byte-identical copies of the 30/10 simulation (md5 `0e3709fe…`, `12d1108d…`). `rodar_comparar_v5.py` runs them against `_build_v5.py`, changing in memory only the path line and, since round 3, our account on the two deduction lines (58100 / 58101, the WTC V3.0 accounts); it fills the causes `comparar.py` does not know (scenarios 2, 7, 8, 10, 11, 12). Its net does **not** subtract the PSA (the Dev has none). `comparar.py` runs our scenario 11 with the CNPS branches off (= E10 here).

| Scenario | v4 × Dev (30/10) | v5 × Dev (round 3) | What still differs (v5 position, source) |
|---|---|---|---|
| 1 Baseline | equal | equal | — |
| 2 Zero salary | 9 lines | 10 lines | Dev applies the CNPS floor with no pay (guide p. 7); v5 writes the 58131 rate only with insurable salary |
| 3 13th month | equal | equal | — (both annualise; A26) |
| 4 Housing | 5 lines | 5 lines | Dev: forfait on 58105 incl. benefits; v5: MIN(real; 20%) on cash (Art. 46-I/II/III) — Dev IRPP +16,000 |
| 5 Individual severance | 4 lines | 4 lines | Dev exempts it from IRPP; v5 taxes it (Art. 44-I; 45-10° only for plan social) |
| 6 Pension | 4 lines | 4 lines | Dev: 2164x deductible with no cap; v5: 3.5% cap, compulsory only (Art. 47-I/II) |
| 7 Transport | 5 lines | 15 lines | CNPS: v5 transport out in full (guide p. 8), Dev only the exempt 30% · TFE/TAFP: Dev takes exempt transport out, v5 keeps it (Arts. 173, 189) · IRPP Dev −111 |
| 8 Family, 0 children | 9 lines (Dev IRPP +3,150) | 7 lines (Dev IRPP −1) | TFE/TAFP: Dev takes 6276x out, v5 keeps it (Art. 189-1°) · IRPP 1 XAF: Dev band limits `x.99` |
| 9 50% relief | 3 lines | 3 lines | Dev has no 50% relief and no TAFP relief (Art. 158) |
| 10 Young graduate | equal | 5 lines | v5 exempts TF/TA on that payroll share (Arts. 188-10°, 174-3°); Dev does not |
| 11 Non-resident | 12 lines | 9 lines (branches off) | IRPP: v5 scale, Dev 18% · CNPS equal with the v5 defaults |
| 12 Family, 6 children | 5 lines | 7 lines (Dev IRPP −1) | TFE/TAFP as 8 · IRPP 1 XAF: Dev band limits `x.99` |

Exact on every line (1–10): 2 of 10 (1 and 3). IRPP equal to the Dev in 5 of 12 (1, 2, 3, 9, 10); the 1-XAF differences in 8 and 12 come from the Dev's `x.99` limits; 4, 5, 6 are positions the CGI supports (Arts. 46, 44-I/45-10°, 47); 7 follows from the CNPS transport decision; 11 from the non-resident decision.

## Not re-run in v5
Mid-month hire and exit, backdated hire, retro increase, future-dated termination, post-termination payment, unpaid leave, plan-social final pay, the **December CNPS regularisation** (A23) and the **cumulative withholding alternative** (A26) depend on proration, YTD and retro behaviour; they cannot be run in this local engine.

## What is not validated
Not loaded into an engine. Ceiling accounts (A10), `retro_` (A11), `_$$` (A12), a formula-type limit regulation (9148016), `_$$_monthly` (9148091), a DD value as ceiling account (58223) and equal band limits (A21) must be confirmed in the acceptance environment. `preflight_check.py` not found on this machine, not run.

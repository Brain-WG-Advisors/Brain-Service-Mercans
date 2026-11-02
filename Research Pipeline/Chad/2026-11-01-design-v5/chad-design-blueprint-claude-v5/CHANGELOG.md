# Chad design v5 — what changed from v4

v5 = v4 (2026-10-29) plus the statutory verdicts read in the **CGI 2026, DGI edition** (`raw/docs/oficiais/TD/2026-11-01-CGI-TCHAD-2026-FINAL-dgi.pdf`, md5 `139d5326…`; "p." = PDF page) and the **WTC V3.0** export of 2026-11-01 (md5 `04e06a49…`), and the engine structures where the Dev design (CT-A-588 / `td.json`) is better. Everything not listed is unchanged from v4.

| # | Change | Before (v4) → after (v5) | Article / source |
|---|---|---|---|
| 1 | **Family allowance cap** | Fully exempt → exempt up to **5,000 XAF per child per month, less the CNPS family allowance**; excess taxable IRPP. New 9148016 writes the limit in 58107 (formula `MAX(5000 × 58212 − 58213; 0)`, Dev structure and WTC V3.0 account); 9148022 caps by ceiling account 58107. Codes 6275x, 6276x + **6278x** (Family allowance) + **62866** (Birth allowance). New flag 58213 (CNPS allowance, DD field); 58212 = children, not dependants | CGI Art. 45-4°, p. 29 (LF 2026 Art. 8, p. 15): « ne peut excéder mensuellement par enfant la somme de 5.000 Francs sur laquelle viennent… s'imputer les allocations versées par la CNPS » |
| 2 | **Non-resident TFE / TAFP** | Not computed (pre-condition excluded 58218 = 1) → computed; only diplomatic and the Art. 188-10° share are out | TF Art. 187, p. 60 (tax on whoever pays salaries, no residence condition); TA Art. 173, p. 59 (« payés par les entreprises ») |
| 3 | **6286x series** | Only 62867 in the cash gross → whole 6286% in the cash gross (IRPP) and TFE/TAFP base: 62860–62865 meal/food, 62868–62869 gift. 62866 relieved by the Art. 45-4° cap (#1). 62867 death allowance stays taxable, ⚠️ PENDENTE-DECISÃO P4 (may be capital décès, Art. 45-11°). CNPS matrix not changed (P1) | Art. 44-I (« gratifications »), Art. 45 1°–18° exempt none of them, p. 29–30; WTC V3.0 names |
| 4 | **Scholarship 6580x** | Taxable IRPP → **out of IRPP gross** (6580% No in 9148041), **kept in the TFE/TAFP base** | Art. 45-9°, p. 30 (« bourses d'enseignement ou de perfectionnement »); Art. 189-1° and Art. 173 have no Art. 45 carve-out; WTC V3.0 "School Scholarship" |
| 5 | **TFE rounding** | `FLOOR(x+0.5)` → none (Dev structure). TAFP keeps its rounding | Art. 190, p. 61 (7.5%, no rounding rule); only Art. 177 (TAFP) rounds |
| 6 | **TFE / TAFP exemption for young graduates, disabled persons and workers under 35** | None → derived flag **58219**; TFE and TAFP bases do not run when 1 (real-regime entity 58215 and: disabled 58218 = 2, or young graduate 58218 = 3 under 35, or worker 58217 = 1 under 35; age 58216). New fields: entity tax regime, worker category, date of birth | Art. 188-10°, p. 61 (TF); Art. 174-3°, p. 59 (TA): « sur la part de la masse salariale versée ». No five-year limit in these two articles |
| 7 | **PSA (food security levy)** | Not built → new 9148091: **400 XAF a month, employee deduction**, every status except diplomatic, only in a month with cash pay; liability 2570 (new WTC code) | Arts. 837–839, p. 166 (LF 2024 Art. 21): « fixé à 400 FCFA/mois et par employé »; recovered « comme en matière d'IRPP » |
| 8 | **15% exemption of function expense allowances** | Not built (A4) → 9148015 band 10 writes 58173 = 15% of 58105; new 9148024 exempts 6287x up to 58173 into 58114; 58114 enters 58552 and the non-resident base, not TFE/TAFP | Art. 45-2°, p. 29: « n'excède pas un pourcentage de 15 % calculé sur la masse globale des salaires et desdites allocations » |
| 9 | **Supplementary retirement only if compulsory** | 216%% deductible up to 3.5% → same cap, but **2164x (Voluntary Contribution, WTC V3.0) = No** | Art. 47-II, p. 30: « doivent revêtir un caractère obligatoire » |
| 10 | **"30% professional expenses"** | Not present in v4 (checked: no such deduction in `_build_v4.py` or SKILL.md) → still none; note added in 9148024 | Art. 47, p. 30 deducts only compulsory pension (3.5%) and social security; no 30% abatement on salaries |
| 11 | **CNPS accounts** | Unchanged on purpose: EE → 2610 / 2551; ER → 6037 / 2537, 6020 / 2550, 6040 / 2560. The Dev's inversion (EE 3.5% on 6020/2550, ER 7.5% on 2610/2551) is **not** copied | WTC V3.0: 2551 "TD CNPS Contribution EE"; 2537, 2550, 2560 "TD CNPS Contribution ER" |
| 12 | Open points of round 1 (CNPS, non-resident method, IRPP rounding) | parametrised as PENDENTE-DECISÃO in round 1 | **decided in round 2** (rows R2-1 to R2-8 below); only P4 (62867) stays open | LEI-VEREDITOS.md § Revisão 2026-11-01 (b) |
| 13 | Citations updated | Disabled → **Art. 45-18°** (the old Art. 3-3° was repealed by LF 2026); young graduate → Art. 3-4°; diplomatic → Art. 3-2°; IRPP scale → Art. 1-IV (LF 2026 Art. 3, confirmed); 9148015 renamed "TD Limits on Cash Remuneration" | CGI 2026 p. 14–15, 30 |

## Round 2 (2026-11-01) — decisions of `LEI-VEREDITOS.md` § "Revisão 2026-11-01 (b)"

New sources: Dec. 1635/PR/PM/MFPT/2009 and Dec. 1636/PR/PM/MFPT/2009 (full text, droit-afrique), CNPS *Guide de l’employeur* 2019 (cnps-tchad.com via Wayback), CNPS official list of texts (09/2026) — `raw/docs/oficiais/TD/2026-11-01-*`.

| # | Change | Before (round 1) → after | Source |
|---|---|---|---|
| R2-1 | **CNPS rates and limits** | PENDENTE-DECISÃO (v4 values) → confirmed: PVID 3.5% EE + 5% ER, PFM 7.5% ER, AT/MP 4% ER (total 20%), from 2009-12-04; ceiling 500,000 a month in the 3 branches (6,000,000 a year, annual — December regularisation, A23); floor 60,000 only in a month with pay | Dec. 1636 arts. 1, 3; Dec. 1635 arts. 1–2, 4; Dec. 1634/2009 (via guide p. 8); guide p. 7, 9, 12; Dec. 1111/2011 |
| R2-2 | **CNPS base** | v4 matrix → benefits in kind in; 6286x meal/food **in**; 6274x and 6580x in; family allowances 6275x/6276x/**6278x** out; meal cash 6566x **out**; severance out; leave ticket, per diem, relocation, 6287x out; **transport 6251x/6252x out in full** (58104 no longer in the CNPS matrix) — ⚠️ A CONFIRMAR COM O USUÁRIO (contradicts `correcoes.md` 2026-07-07) | Dec. 1635 art. 3, Dec. 1636 art. 2; guide p. 7–8 |
| R2-3 | **Non-resident CNPS** | by branch flags, scenario with branches off → every branch by default (flags default 1); 2 only for a seconded employee under a convention (CIPRES) | guide p. 6 (« quelle que soit… leur nationalité ») |
| R2-4 | **Non-resident IRPP** | 18% on 58592 (P2) → **progressive scale** on 58552 with Arts. 45–47, like residents (9148072); 9148074 now copies 58552 into 58592 for the report; 9148075 posts the scale result to 2592. Flag 58221 removed | Arts. 44-II-2° (p. 29), 847 (p. 168); Art. 116 (p. 43) only for Art. 2-VI and Art. 60 |
| R2-5 | **Leave ticket** | out of every base → 6255x in the cash gross and TFE/TAFP; exempt up to the annual ticket limit (new DD field 58223) in new 9148025 → 58115 | Art. 45-15° (p. 30); Arts. 189-1°, 173 |
| R2-6 | **Per diem / fixed function allowance** | per diem out of every base → 62570, 6557x, 6558x in the cash gross and TFE/TAFP, sharing the 15% cap of 9148024 with 6287x; reimbursements with receipts stay out (6256x) | Art. 45-2° (p. 29), Art. 44-I; Arts. 189-1°, 173 |
| R2-7 | **IRPP rounding** | flag 58222 (P3) → FLOOR(x+0.5) fixed, marked "technical convention, no rule in the CGI"; flag removed | CGI 2026: no IRPP rounding rule; Art. 847 (DGI barème not obtained) |
| R2-8 | 6274x / 6580x | already as decided (6274x taxable everywhere; 6580x out of IRPP, in TFE/TAFP) → CNPS confirmed in for both | Art. 45-9°; Dec. 1635 art. 3 |

## Round 3 (2026-11-01) — fixes after the independent QA review (`../QA-REVIEW.md`, FAIL: 2 blocker, 7 major, 13 minor)

| # | QA finding | Before (round 2) → after | Source |
|---|---|---|---|
| R3-1 | m1 band limits | `incomeTo` 800,000.99 / 6,000,000.99… → **800,000 / 6,000,000 / 7,500,000 / 9,000,000 / 12,000,000**, each equal to the next `incomeFrom`; scenarios 7, 8, 12 now exact (26,548; 26,548; 23,398). Validation tolerance (EDGE) removed: every column must match | Art. 1-IV (p. 14) |
| R3-2 | B1 TFE fraction of a franc | no rounding (E3 = 25,537.5) → **paid to the whole franc, FLOOR(x+0.5), documented as technical payment convention, not statutory rounding** (E3 = 25,538) | Art. 190 (no rule); XAF has no subunit |
| R3-3 | B2 open marks in SKILL.md | 3 `PENDENTE-DECISÃO` + 2 `A CONFIRMAR` → **0**. Technical decisions of the front (pending the user's ok; corrected in round 4 — first written as "user decisions"): transport out of CNPS in full (guide p. 8; the decrees do not name transport); 62867 taxable (alternative and its effect in ASSUMPTIONS D2, RESEARCH_GAPS R28) | user, 1 Nov |
| R3-4 | M1 annualisation of irregular payments | not flagged → explicit ASSUMPTION A26 with the cumulative-method proposal and its effect (scenario 5 ≈ 90,700 less withheld; scenario 3 ≈ 11,100 less); scenarios 3, 5 and E8 marked as method-dependent; DGI barème added (R23) | Arts. 1-I/1-IV, 847 |
| R3-5 | M2 Art. 3-4° | only "young graduate ≤ 60 months" → derived flag **58226**: real-regime entity, ≤ 60 months, and young graduate under 35 at recruitment (new 58225) **or worker**; tests E5, E12–E14 | Art. 3-4° (p. 15) |
| R3-6 | M3 accounts × WTC V3.0 | own intermediates → V3.0 ones reused: 58141 → **58100**, 58142 → **58101**, 58171 → **58103**, 58152 → **58112**; complete list of what is new in ASSUMPTIONS A14 and RESEARCH_GAPS R27 | WTC V3.0 |
| R3-7 | M4 TAFP base | same base as TFE → own matrix `TAFP_BASE`: one-time / discretionary bonuses 6222x out; pensions 6264x not in the TA (in the TF only) | Art. 173 « gratifications servies régulièrement »; Arts. 187, 189-1° « pensions » |
| R3-8 | M5 6251x | out of CNPS but not in the 30% exemption → **6251x and 6252x share the 30% exemption** (9148021) and are both out of CNPS | Art. 45-13°; guide p. 8 |
| R3-9 | M6 confidence | CONFERENCIA 95% on the non-resident and leave ticket / per diem → 85% (non-resident) and 75% (leave ticket / per diem), as LEI-VEREDITOS B1 | LEI-VEREDITOS items 9/10, 26 |
| R3-10 | M7 RESEARCH_GAPS | SMIG/floor, DGI barème, Dec. 1634, valuation arrêté, CNPS circulars missing → R22–R26 (+ R27–R30) | LEI-VEREDITOS B3 |
| R3-11 | minors | m3: 58131 rate written only when 58550 > 0 · m4: 58205 renamed, catalogue sentence corrected · m5: pensions 6264x in the TF base · m6: 6278x and 6259x added to R19 · m7: scope note on the Art. 45-4° cap (A29) · m2: Art. 177 per employee (A31) · m8: diplomatic exclusion without source (A32, R30) · m9: count of extra checks · m10: simulation header · m11/m12: D1/D2 · m13: CNPS date cited to the guide p. 8 (R29) | QA-REVIEW.md |

## Round 4 (2026-11-01) — fixes after QA round 2 (`../QA-REVIEW.md` § Rodada 2: 0 blocker, 3 major, 1 minor)

| # | QA finding | Before → after | Source |
|---|---|---|---|
| R4-1 | N1 worker / young graduate without start date exempt forever | `LESS($58205;61)` only → **`GREATER($58205;0)` added**; start date mandatory in the DD (R31); E18 (worker without date → IRPP 28,464), E20 (young graduate without date → IRPP due) | Art. 3-4° (five-year period needs a start) |
| R4-2 | N2 worker age | no age limit for workers → **under 35 at recruitment for workers too** (restrictive reading, 60%, alternative in A34); E19 (worker recruited at 40 → IRPP 28,464) | Art. 3-4° (p. 15) × Arts. 188-10°, 174-3° |
| R4-3 | N3 attribution | "user decision" → **"technical decision of the Chade front (source …), pending the user's ok"** for transport outside CNPS and 62867 taxable, in every file | user mandate of 1 Nov ("pesquisar e decidir") |
| R4-4 | N4 reference | 9148012 note pointed to A28 → ASSUMPTIONS D2 / RESEARCH_GAPS R28 | — |

Results: the 12 scenarios and 20 extra checks, expected (hand-computed from the CGI) × obtained, are in VALIDATION.md, with the v5 × Dev comparison.

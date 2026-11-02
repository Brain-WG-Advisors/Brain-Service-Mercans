# Chad design v6 — what changed from v5 (form only)

v6 = the v5 rules (2026-11-01, after two QA rounds) written in the form of the development team's td_2026 design (`td.json` = CT-A-588). Rule: where the law does not oblige a difference, the Dev form is copied; where it does, the v5 rule is kept and the regulation note says **Deliberate divergence (law)**. **No value changes on the v5 cases:** the 12 scenarios and 20 extra checks give the same result as v5 on 39 accounts each (VALIDATION.md). The only value change is the matrix-series fix of round 2 (car fuel arrears, test E21), a defect v5 also has.

## What was copied from the Dev
- **Regulation IDs, names and ordinals** (9148009 … 9148261, ID = 9148000 + ordinal): 30 of the 31 Dev regulations have a v6 regulation with the same ID, name, ordinal, tax group (`income_tax` / `social_security`) and taxation type; 28 of 30 also have the same tax rule group (the two others, 9148181 and 9148261, need `_post_formula` for the 3.5% cap and the 50% relief).
- **Granularity:** the IRPP chain split as the Dev — 9148191 taxable income → 9148201 annualised (×`$period_divisor`, 58110) → 9148211 annual scale (`simple_tax_monthly`, 58111) → 9148221 period tax (÷`$period_divisor`, 58112) → 9148231 / 9148241 withholding. The transport limit and the family limit in their own regulations (9148021, 9148032), as the Dev.
- **Formula conventions:** limits inside `MIN($band_amount_raw;…)` (transport, family, BIK, 15%, leave ticket, retirement), BIK caps as `MULTIPLY($58105;rate)` inside the formula, `FLOOR(ADD(x;0.5))`, `$period_divisor`, pre-conditions by 58218, CNPS band order of the Dev.
- **Accounts:** 58103 (transport limit), 58107, 58108, 58110, 58111, 58112, 58100, 58101, 58104, 58105, 58106, 58008, 58120–58128, 58130, 58131, 58534, 58550, 58552, 58563, 58592, liabilities and GL as the Dev. v5-only intermediates removed: 58109 (base salary), 58161–58169 (BIK limits), 58173 (15% limit). Kept (no Dev equivalent): 58113, 58114, 58115, 58172, 2570.
- **Flags:** 58218 = `$hr.employee_type` and 58205 = the Dev formula (`CEIL(MULTIPLY(YEARS_BETWEEN(…);12))`). The retro_ rule groups of v4/v5 dropped (the Dev uses none) — assessed in round 2: payment basis per CNPS guide p. 7 and CGI Art. 189-1° (ASSUMPTIONS A11).
- **Not copied (error):** the CNPS employee band on 6020/2550 and the employer PFM band on 2610/2551 — v6 keeps EE 2610/2551 and PFM 6020/2550 (WTC V3.0: 2551 = EE).

## Regulation by regulation (v5 → v6)
| v6 regulation | v5 source | Dev | Form taken from the Dev | Deliberate divergence (law) |
|---|---|---|---|---|
| 9148009 TD Annual Reporting Limit | 9148013 | Dev pair | ID, name, ordinal; `simple_tax_monthly` / flat | — |
| 9148010 TD Gross Salary | 9148012 | Dev pair | ID, name, ordinal; `simple_tax` / flat | cash-only matrix (Art. 46-I/II, 45-1°) |
| 9148021 TD Transport Allowance Exemption | 9148014 (band 1) | Dev pair | ID, name, ordinal; `simple_tax` / flat | — |
| 9148031 TD Transport Allowance - Exempt | 9148021 | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | all-staff condition, 6251x (Art. 45-13°) |
| 9148032 TD Family Allowance Exemption | 9148016 | Dev pair | ID, name, ordinal; `simple_tax` / formula | per child, CNPS imputed (Art. 45-4°) |
| 9148033 TD Family Allowance final Exemption | 9148022 | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | — |
| 9148034 TD Plan-Social Severance Exemption | 9148023 | Additional (no Dev pair) | Dev pattern: `simple_tax` / flat | only plan social exempt (Arts. 44-I, 45-10°) |
| 9148035 TD Function Allowance Exemption | 9148015 (band 10) + 9148024 | Additional (no Dev pair) | Dev pattern: `simple_tax_post_formula` / flat | Art. 45-2° 15% exemption |
| 9148036 TD Leave Ticket Exemption | 9148025 | Additional (no Dev pair) | Dev pattern: `simple_tax_post_formula` / flat | Art. 45-15° leave ticket |
| 9148041 TD Housing Capped Value for Tax | 9148015 (band 1) + 9148031 | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | cap, not forfait (Art. 46-III/V) |
| 9148051 TD Vehicle Capped Value for Tax | 9148015 (band 2) + 9148032 | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | cap, not forfait (Art. 46-III/V) |
| 9148061 TD Food Capped Value for Tax | 9148015 (band 3) + 9148033 | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | cap, not forfait (Art. 46-III/V) |
| 9148071 TD Interior furnishings Capped Value for Tax | 9148015 (band 4) + 9148034 | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | cap, not forfait (Art. 46-III/V) |
| 9148081 TD Domestic help / security staff Capped Value for Tax | 9148015 (band 5) + 9148035 | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | cap, not forfait (Art. 46-III/V) |
| 9148091 TD Electricity Capped Value for Tax | 9148015 (band 6) + 9148036 | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | cap, not forfait (Art. 46-III/V) |
| 9148101 TD Water Capped Value for Tax | 9148015 (band 7) + 9148037 | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | cap, not forfait (Art. 46-III/V) |
| 9148111 TD Phone Capped Value for Tax | 9148015 (band 8) + 9148038 | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | cap, not forfait (Art. 46-III/V) |
| 9148121 TD Gas Capped Value for Tax | 9148015 (band 9) + 9148039 | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | cap, not forfait (Art. 46-III/V) |
| 9148131 TD Gross Taxable Salary | 9148041 | Dev pair | ID, name, ordinal; `simple_tax` / flat | severance, 6274x, 65630 in; 6580x out (Arts. 44-I, 45-9°) |
| 9148141 TD Apprenticeship Base | 9148082 | Dev pair | ID, name, ordinal; `simple_tax_post_formula_period` / flat | Art. 173 base, Art. 174-3° exemption |
| 9148151 TD Employer Lump-Sum Tax Base | 9148081 | Dev pair | ID, name, ordinal; `simple_tax_period` / flat | Art. 189 base, Art. 188-10° exemption |
| 9148155 TD CNPS Insurable Salary without capping | 9148051 | Dev pair | ID, name, ordinal; `simple_tax` / flat | CNPS base (Dec. 1635 art. 3; guide p. 7–8) |
| 9148161 TD CNPS Insurable Salary | 9148052 | Dev pair | ID, name, ordinal; `simple_tax_period` / flat | floor only with pay (guide p. 7) |
| 9148171 TD CNPS Contribution EE and ER | 9148053 | Dev pair | ID, name, ordinal; `simple_tax_$$_post_formula` / flat | branch flags (guide p. 6); EE/ER accounts per WTC |
| 9148175 TD Retirement Contribution Limit | 9148014 (band 2) | Additional (no Dev pair) | Dev pattern: `simple_tax` / flat | 3.5% cap (Art. 47-I) |
| 9148181 TD Voluntary Contribution | 9148061 | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | 3.5% cap, compulsory only (Art. 47-I/II) |
| 9148191 TD Taxable Income | 9148071 | Dev pair | ID, name, ordinal; `simple_tax` / flat | 58113-58115 (Arts. 45-2°, 45-10°, 45-15°) |
| 9148192 TD Non-Resident Tax Base | 9148074 | Additional (no Dev pair) | Dev pattern: `simple_tax_period` / flat | non-resident on the scale (Arts. 44-II-2°, 847, 116) |
| 9148201 TD Taxable Income - Annualised | 9148072 (split) | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | — |
| 9148211 TD Taxable Income - Annual Tax | 9148072 (split) | Dev pair | ID, name, ordinal; `simple_tax_monthly` / differential | band limits per Art. 1-IV |
| 9148221 TD Taxable Income - Period Tax | 9148072 (split) | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | — |
| 9148231 TD Taxable Income - Period Tax - Resident | 9148073 | Dev pair | ID, name, ordinal; `simple_tax_$$_post_formula` / flat | Art. 3-4° conditions |
| 9148241 TD Taxable Income - Period Tax - Non-Resident | 9148075 | Dev pair | ID, name, ordinal; `simple_tax_$$_post_formula` / flat | non-resident on the scale |
| 9148251 TD Apprenticeship Tax | 9148084 | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | TA relief (Art. 158) |
| 9148261 TD Lump Sum Tax | 9148083 | Dev pair | ID, name, ordinal; `simple_tax_post_formula` / flat | TF 50% relief (Art. 158) |
| 9148271 TD Food Security Levy (PSA) | 9148091 | Additional (no Dev pair) | Dev pattern: `simple_tax_$$_monthly` / flat | PSA (Arts. 837–839) |

Dev regulation without a v6 pair: **9148011 TD Non-Resident Tax Base** — Deliberate divergence (law): the non-resident is taxed on the scale on the taxable income 58552, which exists only after 9148191; 58592 is written by the additional 9148192.

## Deliberate divergences (law), in one place
Cash-only 58105 (Art. 46-I/II) · transport only if paid to all staff, 6251x included (Art. 45-13°) · family cap per child less the CNPS allowance (Art. 45-4°) · plan-social severance only (Arts. 44-I, 45-10°) · 15% function allowance (Art. 45-2°) · leave ticket (Art. 45-15°) · BIK MIN(real; cap) (Art. 46-III/V) · IRPP gross with individual severance, 6274x, 65630; scholarship out (Arts. 44-I, 45-9°) · TF/TA gross bases and the Arts. 188-10° / 174-3° exemptions · CNPS base per the decrees and the guide, floor only with pay, branch flags · retirement 3.5% cap and compulsory only (Art. 47) · band limits at the round figure (Art. 1-IV) · Art. 3-4° conditions · non-resident on the scale (Arts. 44-II-2°, 847, 116) · TF/TA 50% relief (Art. 158) · PSA (Arts. 837–839) · flags 58206 (0/1/2) and 58212 (children) keep the Dev number with the field the law needs.

## v6 round 2 (2026-11-02) — after the v6 QA review (`../QA-REVIEW.md`: 0 blocker, 2 major, 4 minor)

| # | QA finding | Before → after | Effect on values |
|---|---|---|---|
| r2-1 | V1 car fuel arrears out of IRPP / TF / TA | `65520` exact → **`6552%`** (Car Fuel Benefit 65520–65523) in 9148051 and in the TF/TA benefit list, as the Dev. Same check series by series against the WTC V3.0: `62670`/`62680` exact → **`6267%` / `6268%`** (Benefits plan 1 and 2 with their arrears, adjustments and other lines) in 58105-based bases, IRPP gross, TF/TA and CNPS; CNPS gratuities `62910`/`62920`/`62930` exact → **`6291%` / `6292%` / `6293%`** No, and **62909** No like 62900. **v5 also affected** (same matrices; not corrected there — v5 is kept as delivered) | Only new test E21 changes: 65521 of 50,000 → IRPP 23,214 → **26,364**, TFE 22,500 → 26,250, TAFP 3,600 → 4,200 (v5 → v6). None of the 32 earlier cases uses those codes |
| r2-2 | V2 `retro_` removed without assessment | Kept without `retro_` (as the Dev) — decided on the texts (CNPS guide p. 7, CGI Art. 189-1°: payment basis; Art. 847); A11 rewritten with the effect; test E22 (arrears 62101) | none on the 32 cases; E22 new |
| r2-3 | m1 58110–58112 ≠ 0 for the exempt | 9148201 pre-condition `SCALE` (was NOT_DIPLO, as the Dev) — 58110–58112 = 0 for the exempt, as v5 | none on liabilities; 58110–58112 now 0 for the exempt |
| r2-4 | m1 comparison too narrow | v6 × v5 now on 39 accounts (+58103, 58172, 58112) and a 58110/58111 consistency check | — |
| r2-5 | m2 old references | ASSUMPTIONS A10, A12 and RESEARCH_GAPS R15, R27 on v6 IDs / accounts | — |
| r2-6 | m3 58205 in the month of hire | Kept the Dev formula; effect recorded in A13 (hire on the last day → 1 day taxed) | — |
| r2-7 | m4 58106 without pay | Recorded in A16 (same as the Dev; reporting only; pre-condition impossible at ordinal 9) | — |

## v6 round 3 (2026-11-02) — after the v6 QA round 2 (`../QA-REVIEW.md` § Rodada 2: 1 major, 3 minor)

| # | QA finding | Before → after | Effect on values (v5 → v6) |
|---|---|---|---|
| r3-1 | W1 medical insurance 6261x out of every base | `6261%` Yes in the cash gross (→ IRPP, TF, TA) and in the CNPS base. Verdict 25 of LEI-VEREDITOS: no Art. 45 exemption for health cover; Art. 9-I « la valeur des profits et avantages en nature »; Art. 44-I. Confidence 80%. **v5 also affected** | E23 (62610 50,000): IRPP 23,398 → 28,464, TFE 22,500 → 26,250, TAFP 3,600 → 4,200, EE CNPS 10,500 → 12,250 |
| r3-2 | W1 social allowance 62651–62653 out of every base | `6265%` Yes in the cash gross and the CNPS base (62650 was the only one in). CGI 2026 Art. 44-I (p. 29): « traitements, indemnités, allocations… et émoluments » are income; Art. 45 (1°–18°, p. 29–30) has no social-raise exemption; CNPS: « tous autres avantages versés » (guide p. 7). 62651 is named "pre-tax deduction" but is an Earning in the WTC — treated as pay (A36). Confidence 85%. **v5 also affected** | E24 (62651 20,000): IRPP 23,398 → 25,424, TFE 22,500 → 24,000, TAFP 3,600 → 3,840, EE CNPS 10,500 → 11,200 |
| r3-3 | W1 full sweep | Every WTC V3.0 Earning code (554) run through the engine (`sweep()` in `_build_v6.py`, `../SWEEP-run.txt`). Found and fixed: cash-in-lieu **6561x Phone cash and 6566x Meal cash** were kept out of the TF/TA by exact "No" rules in the benefit list — removed. In no base after the fix: only 62560–62563 (relocation 2, reimbursements with receipts, A22). **v5 also affected** | E26 (65610 20,000): TFE 22,500 → 24,000, TAFP 3,600 → 3,840 |
| r3-4 | W2 6218x out of TF/TA × 629xx in | Aligned on the articles: **TF** — severance 6218x **in**, as the EOS gratuities 629xx (Art. 189-1° « indemnités diverses »; closes A20, verdict N5); **TA** — all termination payments **out**: 6218x, 62900, 62909, 6291x–6293x (Art. 173 taxes « appointements, salaires, avantages en nature et rétributions quelconques, y compris les gratifications servies régulièrement »; a termination payment is neither pay nor a regular gratification). Confidence TF 75%, TA 60% | Scenario 5: TFE 22,500 → **90,000** (1,200,000 × 7.5%). E25 (62900 100,000): TAFP 4,800 → 3,600 |
| r3-5 | W3 workbook | Cause "PSA exists only in v5" → "only in v5 and v6"; "Legal accuracy" renamed and qualified; row of defects found by QA after the score | — |

---

# History (v4 → v5)


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

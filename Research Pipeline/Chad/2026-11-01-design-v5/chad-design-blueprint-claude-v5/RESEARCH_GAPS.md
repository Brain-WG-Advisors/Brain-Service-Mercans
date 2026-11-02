# Chad — research gaps for the compliance team (v5)

Gaps 1–14 come from v3/v4; their status is updated with the CGI 2026 (DGI edition) and the CNPS decrees / employer guide read on 1 Nov 2026. 15–30 are new in v5 (22–30 added in round 3, after the QA review).

| # | Artefact | Gap | Fix | Status (v5) |
|---|---|---|---|---|
| 1 | CCG / all | IRPP scale unconfirmed | — | **Closed**: Art. 1-IV, p. 14 (LF 2026 Art. 3) = 0 / 10.5 / 15 / 20 / 25 / 30% |
| 2 | CCG 7.1, tables | v4 said "remove the 5,000 XAF per-child cap (Congo wording)" | **Reversed**: keep the cap — 5,000 XAF per child per month, CNPS allowance imputed (Art. 45-4°, p. 29). `correcoes.md` 2026-07-07 and the hub decision are wrong on this point | Open (CCG and `correcoes.md` to align) |
| 3 | CCG 7.2 / DD | Benefit base | Art. 46-I/II: cash remuneration (no « net des cotisations » in 2026) | Fix in CCG/DD |
| 4 | CCG TFE/TAFP table | Family allowances and exempt transport shown outside TFE/TAFP | Include them (Arts. 173, 189) | Open |
| 5 | CCG Scenarios C and D | v4 values | as v4 | Open |
| 6 | DD | Resident 20% abatement | Remove | Open |
| 7 | WTC | "Yes-No" rows | — | Superseded by WTC V3.0 (Yes/No only) |
| 8 | WTC | No TFE / TAFP columns | — | **Closed** in WTC V3.0 (Apprenticeship, Lump-Sum columns) |
| 9 | WTC | `TD-` research codes | — | Closed in V3.0 (Global codes) |
| 10 | DD | Fields for plan social, transport granted to all, TFE/TAFP relief; v5 adds CNPS family allowance amount, entity tax regime (réel), date of birth, worker category | Add | Open |
| 11 | CCG | Food-security levy | Add: 400 FCFA a month, borne by the employee (Arts. 837–839, p. 166) | Who bears it now confirmed; CCG to update |
| 12 | CCG 7.3 | Garnishment decree | Keep court-order handling | Open |
| 13 | Report Specs 005/006/007 | EE/ER CNPS mapped to 2550/2551 the wrong way round | Swap: WTC V3.0 confirms 2551 = EE, 2550 = ER | Open |
| 14 | Report Spec DGI-001 vs DGI-004 | Label of 58552 | Align | Open |
| 15 | WTC V3.0 | No wage type for the Art. 45-2° function expense allowance | Create 6287x "Function expense allowance (Art. 45-2°)", Tax Yes (exempt part computed by 9148024), CNPS No (expense allowance, Dec. 1635 art. 3; guide p. 7–8), TF/TA Yes | New |
| 16 | WTC V3.0 | Only 2164x "Voluntary Contribution" exists; a compulsory supplementary pension has no code | Create a 216xx compulsory-scheme code if a client has one (Art. 47-I/II) | New |
| 17 | WTC V3.0 / Report Specs | No PSA code; no report reads it | Create 2570 "TD PSA EE" (Tax category); add to the IRPP-TS/DAS remittance (Art. 838: recovered as IRPP) | New |
| 18 | WTC V3.0 (outside the design) | Severance 6218x Tax No (Art. 44-I says taxable unless plan social); health insurance 65630 Tax No (no Art. 45 exemption); family allowance 6275x/6276x Tax Yes in full (Art. 45-4° caps the exemption) | Align the WTC with the CGI 2026 | New |
| 19 | WTC V3.0 (outside the design) | CNPS column: 6580x and 6274x marked No (decided: in, Dec. 1635 art. 3); TF/TA: 6580x No (Arts. 173, 189: in); 6255x / 62570 / 6557x / 6558x Tax, TF, TA No (decided: in, with the Art. 45-15° / 45-2° exempt parts) ; also 6278x Family allowance CNPS Yes (decided: out, family allowances), 6222x / 62300 / 623xx Apprenticeship No (Art. 173: only non-regular gratifications are out — A30), and 6259x Birth and Marriage Allowance to split (birth → Art. 45-4° cap; A33) | Align the WTC with the decisions of 1 Nov | New (round 2, completed round 3) |
| 20 | `correcoes.md` 2026-07-07 / hub | "Transport excess over 30% subject to CNPS" — the CNPS guide p. 8 takes the whole transport allowance out | Technical decision of the front (source: CNPS guide p. 8; the decrees do not name transport): out in full, pending the user's ok. Correct `correcoes.md` and the hub only after that ok | New (round 2); front decision round 3 |
| 21 | Report Spec DGI-001 IRPP-TS | Non-resident line (2592 / 58592) built for an 18% withholding; non-residents are now on the scale | Relabel the non-resident line (scale, not 18%) | New (round 2) |
| 22 | CNPS floor (SMIG) | The 60,000 floor = SMIG 59,995 of Dec. 1111/2011, cited only by the CNPS guide of 2019; no 2026 source | Current SMIG decree from the Journal Officiel or the Ministry of Labour (level A); confirm with the CNPS list of texts | New (round 3) — source hunter |
| 23 | IRPP withholding barème (Art. 847) | « barème fourni par l'Administration » not obtained (dgi.td 403) — decides the rounding convention and the irregular-payment method (A26) | Official DGI barème / circular for salary withholding | New (round 3) — source hunter |
| 24 | Dec. 1634/PR/PM/MFPT/2009 (AT/MP 4%) | Text not obtained; the 4% rests on the CNPS guide p. 8 only | Full text (Journal Officiel) | New (round 3) — source hunter |
| 25 | Arrêté on the valuation of benefits in kind for CNPS (Dec. 1635 art. 5) | Not obtained; v5 uses the real value (same as TF, Art. 189-2°) | Text of the arrêté | New (round 3) — source hunter |
| 26 | CNPS circulars 2025 (n° 023, 077, 107) | Only the titles are on the CNPS page | Contents (CNPS) | New (round 3) — source hunter |
| 27 | WTC V3.0 / global catalogue | New accounts and flags used by v5 (ASSUMPTIONS A14): 58106, 58109, 58113, 58114, 58115, 58161–58169, 58172, 58173, 2570; flags 58202–58204, 58207, 58210, 58213, 58215–58217, 58219, 58223, 58225, 58226. Rename requests: 58101 ("TD Voluntary Contribution" → compulsory retirement deduction), 58131 ("TD CNPS Contribution EE" → total CNPS rate for the Récapitulatif), 58205 ("Young Graduate Start Date" → Art. 3-4° months) | Create / rename in the WTC and check against the global catalogue | New (round 3) |
| 28 | 62867 Death allowance | Technical decision of the front, pending the user's ok: taxable. If a client pays a true « capital décès » (lump sum on death), it is IRPP-exempt (Art. 45-11°) but stays in TFE/TAFP (Arts. 189-1°, 173) and CNPS (Dec. 1635 art. 3) — needs its own code | Create a "Capital décès (Art. 45-11°)" code: Tax No, CNPS Yes, TF/TA Yes | New (round 3) |
| 29 | CNPS effective date | « 2009-12-04 » appears only in the CNPS guide p. 8; the decree texts (droit-afrique, level B) say « de 2009 » | Journal Officiel publication of Decs. 1634–1636/2009 | New (round 3) — source hunter |
| 30 | Diplomatic status outside CNPS and TF/TA | No primary source (Art. 188-5° exempts embassies as payers; the CNPS exclusion is only in the skill) | CNPS law / Vienna convention position; confirm or remove the exclusion | New (round 3) — source hunter |
| 31 | DD | Art. 3-4° exemption start date (`young_graduate_employee_exemption_start_date`) optional; without it the exemption cannot be checked | Make it mandatory when status = young graduate (58218 = 3) or worker (58217 = 1); without it the employee is taxed (v5 rule `58205 > 0`) | New (round 4) |
| 32 | DGI circular on Art. 3-4° | Whether « âgés de moins de 35 ans » also limits « ouvriers » (A34, 60%) | DGI circular / instruction on the LFI 2025 Art. 23 measure | New (round 4) — source hunter |

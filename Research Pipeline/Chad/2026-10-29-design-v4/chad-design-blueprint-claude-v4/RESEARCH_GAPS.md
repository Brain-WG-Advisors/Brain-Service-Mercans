# Chad — research gaps for the compliance team (v4)

Found while building the v3 design (1–12) and the v4 design (13–14). Positions follow the Chad statutory research (July) and the October deep research.

| # | Artefact | Gap | Fix |
|---|---|---|---|
| 1 | CCG / all | IRPP scale 0 / 10.5 / 15 / 20 / 25 / 30% unconfirmed; a 2020 employer guide reconciles only with 0 / 10 / 20 / 30% and income rounded to the thousand | Confirm against the 2026 CGI and LF 2026 |
| 2 | CCG 7.1, tables | 5,000 XAF per-child cap on family allowances — no Chadian source (wording of Congo-Brazzaville CGI Art. 38-2°) | Remove the cap |
| 3 | CCG 7.2 / DD | Benefit base: CCG says gross, DD says base salary; LF 2019 Art. 46-I says cash remuneration net of social contributions | Align on Art. 46-I |
| 4 | CCG TFE/TAFP table | Family allowances and exempt transport shown outside TFE/TAFP; Art. 189 has no Art. 45 carve-out | Include them; exclude severance |
| 5 | CCG Scenarios C and D | C uses a cumulative method Module 6 rejects; D uses approximations | C: IRPP 75,750, net 606,750. D: CNPS 17,500, IRPP 161,500, net 1,838,500 |
| 6 | DD | Resident 20% abatement — abolished by the 2018 reform | Remove |
| 7 | WTC | 26 "Yes-No" rows without a condition | State Yes, No or the condition |
| 8 | WTC | No TFE / TAFP columns | Add, on the Art. 189 base |
| 9 | WTC | `TD-` research codes are not system pay elements | Map to Global WTC codes |
| 10 | DD | No fields for plan-social / voluntary departure, transport granted to all, TFE / TAFP relief (CGI Art. 158: 50% or 100%) | Add |
| 11 | CCG | Food-security levy, 400 FCFA a month (LF 2024 Art. 21–23) missing | Add; confirm who bears it |
| 12 | CCG 7.3 | Garnishment decree (Labour Code Art. 277) not public | Keep court-order handling |
| 13 | Report Specs 005 Appel Mensuel, 006 DNTS, 007 Récapitulatif | PVID employee share mapped to SUM(2550) and PFM to SUM(2551) — the reverse of the coherent pair confirmed on 16 Oct (2551 employee, 2550 employer) | Swap the two mappings in the three specs |
| 14 | Report Spec DGI-001 IRPP-TS vs DGI-004 DAS | DGI-001 labels 58552 "Total Gross Salaries"; DGI-004 labels the same account "Net Taxable Base" (it is the taxable income, after CNPS and exemptions) | Align the label and explanation in DGI-001 |

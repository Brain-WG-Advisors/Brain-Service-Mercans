# Chad v4 — what is still not settled

| # | Topic | Position taken | Why it is open |
|---|---|---|---|
| A1 | IRPP scale | CCG scale: 0 / 10.5 / 15 / 20 / 25 / 30% | A 2020 Chad employer guide's worked example reconciles only with 0 / 10 / 20 / 30% and income rounded to the thousand. The 2026 text was not retrieved |
| A2 | Base of the benefit caps | Cash remuneration (58102) | LF 2019 Art. 46-I says « net des cotisations sociales »; the CCG says gross |
| A3 | "Yes-No" WTC rows (education, stock options, health insurance, maternity) | Taxable and insurable, as Art. 44 | No condition given in the WTC |
| A4 | Expense allowances, 15% (Art. 45-2°) | Not built | No wage type identified |
| A5 | Garnishment (Labour Code Art. 277) | Not built | The decree tranches are not public |
| A6 | Non-resident employees and CNPS / TFE / TAFP | CNPS per branch-eligibility flags; TFE / TAFP not computed | CCG Scenario B is a consultant |
| A7 | TAFP truncation | Per employee | The CCG cites Art. 177; the text was not retrieved |
| A8 | Food-security levy, 400 FCFA a month (LF 2024) | Not built | Who bears it is not confirmed |
| A9 | New fields | Plan social (employee), transport granted to all, TFE / TAFP relief (entity) | Not in the DD |
| A10 | Ceiling accounts (58171, 58172, 58161–58169) | The account's value is a period amount and is applied as is, not divided by the period count | No precedent in our designs or in the Chad export; confirm in the acceptance test |
| A11 | `retro_` scope | Added where the regulation has a floor, a ceiling or a progressive table: 9148013–15, 9148021, 9148031–39, 9148052, 9148061, 9148072. Not on pure sums or flat rates (9148053, 9148073, 9148075, TFE / TAFP) | Rule as stated on 16 Oct; whether the flat steps downstream of a retro base also need it is not stated |
| A12 | `_$$` | Written as production does (`simple_tax_$$_post_formula`) on 9148053, 9148073 and 9148075; on 9148053 it also covers the employer bands | The mark is per regulation, not per band |
| A13 | Young-graduate months (58205) | `DAYS_BETWEEN / 30.4375`, rounded down, plus the current month | A DD counter field would be exact; the report reads 58205 |
| A14 | Flag numbers 58202–58204, 58207, 58210 | Free numbers | Not checked against the global catalogue (not available locally) |
| A15 | Total CNPS rate (58131 = 20) | Written for every employee, as production does | An employee outside a branch would get an overstated "expected contribution" in the Récapitulatif |
| A16 | Reporting limit (58106) | 60,000 a month, Floor = Ceiling, `_monthly`, as production | The DAS compares annual sums; confirm the threshold is meant monthly |

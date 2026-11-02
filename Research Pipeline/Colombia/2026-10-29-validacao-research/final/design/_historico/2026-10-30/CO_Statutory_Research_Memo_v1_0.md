# CO — Statutory Research Memo: Recommended Positions

**Companion to:** `CO_Regulation_Design_v1_0.md` (57 regulations) and `CO_Taxability_Matrices_v1_0.md`
**Basis:** CO-CCG-001 v1.5, CO-WTC-001 v1.7 and CO-DD-001 v1.4, with the primary sources cited per item.
**Purpose:** the items that are **statutory research**, not engine-capability questions. Each carries a recommended position rather than an open question.
**Separate from:** the engine-capability questions for the dev team (`CEILING`, history reads, the art. 383 table construct — design Part 6 items 1 and 4, Part 4 `9170061`). Nothing here needs the dev team.

---

## Item 1 — Art. 114-1 exoneration: what is tested against 10 minimum wages? — ✅ Salary payments of the month AND the IBC

**Position.** The test counts only the **salary payments of the month** (Labour Code art. 127); non-salary payments, vacation pay, social benefits and indemnities are left out (DIAN Conceptos 8380 of 2024 and 7196 of 2025; Consejo de Estado, Sección Cuarta, exp. 25302 of 2022, followed in exp. 26984 of 2024). The literal "totalidad de lo devengado" of Decree 1828 of 2013 art. 7 is not followed. Second condition: when the IBC (salary + Law 1393 excess) reaches 10 minimum wages, the contribution return does not accept the exonerated mark (PILA Technical Annex 2 v30 field 76), so the employer pays.

**Design effect:** `9170025`; gates of `9170041`, `9170045`, `9170046`.
**Confidence:** 90%.

---

## Item 2 — All-inclusive salary with pacted non-salary payments — ✅ 70% of the salary + the full Law 1393 excess

**Position.** IBC = 70% × all-inclusive salary (Law 100 of 1993 art. 18) **plus** the excess of pacted non-salary payments over 40% of total remuneration, the excess **not** reduced to 70% (Consejo de Estado SU exp. 25185 of 9 December 2021, rule 3; exp. 25907 of 2022). Total remuneration for the 40% test = all-inclusive salary at 100% + pacted non-salary. Example: 30,000,000 + 25,000,000 pacted → 21,000,000 + 3,000,000 = 24,000,000.

**Design effect:** `9170019`–`9170021`.
**Confidence:** 80% (no DIAN/UGPP doctrine on the order for the all-inclusive case; the reading follows the unification ruling and matches the provider payroll).

---

## Item 3 — Law 1393 excess: which funds? — ✅ Health, pension and occupational risk only

**Position.** Law 1393 of 2010 art. 30 applies "for the purposes of articles 18 and 204 of Law 100" (pension and health); occupational risk follows the IBC (Decree-Law 1295 of 1994 art. 17). The payroll levies use Law 21 of 1982 art. 17 (salary + paid rest), so the excess never reaches CCF, SENA or ICBF. The UGPP worked example (ABC Empleadores 2025: salary 5,000,000 + pacted 4,000,000 → IBC 5,400,000, CCF base 5,000,000) confirms it.

**Design effect:** `58104` feeds `58106`/`58112`/`58113`/`58114`, never `58108`.
**Confidence:** 95%.

---

## Item 4 — Which non-salary payments enter the 40% test? — ✅ Only the pacted ones

**Position.** The 40% limit applies to payments that remunerate the service but were excluded from salary by written pact (Labour Code art. 128; Law 344 of 1996 art. 17). Payments non-salary by nature (transport allowance, occasional per diem, tools, work clothing, liberality) are outside the numerator and the total (CE SU 25185/2021, rule 1). Where the nature is unclear, the payment is treated as pacted (WTC class `Non-Salary - pacted`).

**Design effect:** matrix K split; `9170017`.
**Confidence:** 85%.

---

## Item 5 — 72 UVT per dependant and the 40% / 1,340 UVT cap in the monthly withholding — ✅ 72 UVT out; cap in

**Position.** The 72 UVT per dependant (Tax Code art. 336 num. 3) belong to the annual return only: art. 388 (withholding base) refers to art. 387, not art. 336 (DIAN Concepto 011383 of 2024, chapter IV question 2). The monthly withholding keeps the art. 387 deduction (10% of gross labour income, max 32 UVT). The 40% and 1,340 UVT cap **does** apply in the monthly withholding: Decree 1625 of 2016 art. 1.2.4.1.6 par. 3, as modified by Decree 2231 of 2023, says so expressly, and a decree prevails over doctrine.

Voluntary contributions to the mandatory individual pension account (RAIS) are non-taxable income (Tax Code art. 55: up to 25% of labour income and 2,500 UVT a year) and are **outside** the 40% / 1,340 UVT cap; voluntary-pension / AFC savings (arts. 126-1, 126-4) are exempt income **inside** it.

**Design effect:** `9170052`, `9170054`, `9170057`, `9170059`; no 72-UVT regulation.
**Confidence:** 95%.

---

## Item 6 — Dismissal indemnity withholding — ✅ Outside the monthly base

**Position.** 20% of the indemnity where the employee's income exceeds 204 UVT (Tax Code art. 401-3; Decree 1625 of 2016 art. 1.2.4.1.13); otherwise the table percentage of the average monthly taxable payments of the previous 12 months (Decree 1625 art. 1.2.4.1.8). The 204-UVT test is applied to the monthly income — a reading, since the provision does not define the income measured.

**Design effect:** `9170064`.
**Confidence:** 85% on the rule; 70% on the measured income.

---

## Item 7 — Non-resident employees — ✅ Flat 20% on the gross payment

**Position.** A non-resident on a Colombian payroll is withheld at 20% on the gross payment (Tax Code arts. 408–415), not on the art. 383 table, until tax residence is acquired (DIAN Concepto 011108 of 29 June 2026, item 10). Severance savings of a non-resident: 20% on the nominal amount is our position; there is no DIAN doctrine.

**Design effect:** `9170063`; design open item 10.
**Confidence:** 90% (salary); 60% (severance savings).

---

## Item 8 — Hours divisor and rest-day surcharge in 2026 — ✅ Two different dates

**Position.** Divisor 220 to 14 July 2026, 210 from 15 July 2026 (Law 2101 of 2021 art. 3; Labour Code art. 161 as amended by Law 2466 of 2025 art. 11). Rest-day / holiday surcharge 80% from 1 July 2025, 90% from 1 July 2026, 100% from 1 July 2027 (Labour Code art. 179 transitional paragraph, Law 2466 of 2025 art. 14). Hourly value and surcharge are read on the date worked.

**Design effect:** constants `52504`, `52505`; `9170012`.
**Confidence:** 95%.

---

## Item 9 — Transport allowance — ✅ Up to 2 minimum wages inclusive, prorated to days

**Position.** Due when the salary is up to 2 minimum wages inclusive (Decree 1470 of 2025; Law 15 of 1959 art. 2), prorated to the days worked (Decree 1258 of 1959 art. 5): 249,095 × 21 / 30 = 174,366.50 in a month with absences. Not salary: out of the IBC and the levy base, in the service-bonus and severance-savings base.

**Design effect:** `9170013`, `9170081`.
**Confidence:** 95%.

---

## Item 10 — Vacation compensated in cash — ✅ Salary ÷ 30 × days during employment; ÷ 720 only on termination

**Position.** During employment, at most half of the entitlement may be paid in cash (Labour Code art. 189 num. 1) and it is paid as salary ÷ 30 × business days. The ÷ 720 formula is for the proportional vacation on termination. Vacation paid in cash is out of the IBC (CE S4 exp. 26941 of 2024) and out of the service-bonus and severance base (Labour Code arts. 189, 253, 306), but in the levy base (Law 21 of 1982 art. 17).

**Design effect:** `9170085`, `9170086`; matrices I, J, G.
**Confidence:** 85% on the cash formula and on the IBC / benefit-base exclusion; 70% on the inclusion in the payroll-levy base (UGPP practice diverges).

---

## Item 11 — Occupational risk on leave days — ✅ Not due

**Position.** No occupational-risk contribution for vacation taken, incapacity, maternity, paternity or parental leave days (Decree 1072 of 2015 art. 2.2.4.2.1.6; PILA Technical Annex 2 v30 field 26). Health and pension continue.

**Design effect:** separate IBC `58114` (matrix F).
**Confidence:** 92%.

---

## Item 12 — Apprentices — ✅ Support by phase; base never below 1 minimum wage

**Position.** Maintenance support 75% (classroom) or 100% (practical / dual) of the minimum wage (Labour Code art. 81, Law 2466 of 2025 art. 21). The contribution base is in every case at least 1 minimum wage and the employee deductions are computed on it (Decree 0223 of 2026 art. 2.2.6.3.3.4 par. 2). Classroom phase: health and occupational risk; practical phase: all rights of an employment contract.

**Design effect:** `9170096`; open item 7 (phase field, transport allowance).
**Confidence:** 85%.

---

## Item 13 — Occupational-risk class V maximum — ✅ 6.960% initial; 8.700% top of the range

**Position.** Class initial rates 0.522% / 1.044% / 2.436% / 4.350% / 6.960%; class ranges from 0.348% to 8.700% (Decree 1772 of 1994 art. 13).

**Design effect:** `52520`.
**Confidence:** 98%.

---

## Item 14 — Base of the art. 64 indemnity — ✅ Art. 127 salary, variable averaged, no transport allowance

**Position.** The daily salary of art. 64 is the salary of Labour Code art. 127, variable parts included: fixed salary → last salary; variable salary → average actually earned in the last year of effective service, suspensions excluded (art. 253 by analogy; Supreme Court, Labour Chamber, SL1659-2025). The transport allowance is not salary and stays out. The same base selects the tier (< or ≥ 10 minimum wages).

**Design effect:** `9170091`.
**Confidence:** 85%.

---

## Item 15 — Illness benefit floor — ✅ Never below the minimum wage

**Position.** 2/3 of the salary (days 1–2 employer, from day 3 health insurer; 1/2 from day 91), never below the minimum-wage equivalent (Labour Code art. 227; Constitutional Court C-543 of 2007, resolutive part). Concepto MinSalud 202311602174531 of 20 October 2023 applies the 2/3 to the employer's days 1–2. 100% by agreement is lawful (Labour Code art. 13).

**Design effect:** `9170093`, constant `52544`.
**Confidence:** 90%.

---

## Summary

| Item | Position | Needs |
|---|---|---|
| 1 — Art. 114-1 test | Salary payments of the month AND IBC < 10 SMMLV | Nothing |
| 2 — All-inclusive + pacted NS | 70% of salary + full excess | Nothing (80%) |
| 3 — Excess scope | Health, pension, ARL; never levies | Nothing |
| 4 — 40% test scope | Pacted non-salary only | Nothing |
| 5 — Dependants / cap | 72 UVT annual only; cap kept monthly; RAIS voluntary outside the cap | Nothing |
| 6 — Indemnity withholding | 20% above 204 UVT, else 12-month table % | Measured income (open item 11) |
| 7 — Non-resident | Flat 20% | Severance savings (open item 10) |
| 8 — Hours | Divisor 210 from 15 Jul; surcharge 90% from 1 Jul 2026 | Nothing |
| 9 — Transport allowance | ≤ 2 SMMLV, prorated | Nothing |
| 10 — Vacation in cash | ÷ 30 during employment; ÷ 720 on termination | Nothing |
| 11 — ARL on leave days | Not due | Nothing |
| 12 — Apprentices | Support by phase, 1-SMMLV base | Phase field (open item 7) |
| 13 — ARL class rates | Initial rates per Decree 1772 | Nothing |
| 14 — Indemnity base | Art. 127 salary, variable averaged, no transport allowance | 12-month history read |
| 15 — Illness floor | Minimum wage, configurable | Nothing |

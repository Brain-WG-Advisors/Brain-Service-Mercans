# CO — Statutory Research Memo: Recommended Positions

**Companion to:** `CO_Regulation_Design_v2_0.md` (79 regulations, `co_design_v2.json`) and `CO_Taxability_Matrices_v2_0.md`
**Basis:** CO-CCG-001 v1.7, CO-WTC-001 v1.9 and CO-DD-001 v1.6 (issue of 2 November 2026), with the primary sources cited per item.
**Purpose:** the items that are **statutory research**, not engine-capability questions. Each carries a recommended position rather than an open question.
**Separate from:** the engine-capability questions for the dev team (`CEILING`, history reads, the art. 383 table construct — `ASSUMPTIONS.md` A7, `RESEARCH_GAPS.md` R3, regulation `9170084`). Nothing here needs the dev team.

---

## Item 1 — Art. 114-1 exoneration: what is tested against 10 minimum wages? — ✅ Salary payments of the month AND the IBC

**Position.** The test counts only the **salary payments of the month** (Labour Code art. 127); non-salary payments, vacation pay, social benefits and indemnities are left out (DIAN Conceptos 8380 of 2024 and 7196 of 2025; Consejo de Estado, Sección Cuarta, exp. 25302 of 2022, followed in exp. 26984 of 2024). The literal "totalidad de lo devengado" of Decree 1828 of 2013 art. 7 is not followed. Second condition: when the IBC (salary + Law 1393 excess) reaches 10 minimum wages, the contribution return does not accept the exonerated mark (PILA Technical Annex 2 v30 field 76), so the employer pays.

**Design effect:** `9170048`; gates of the employer band of `9170056`, `9170062`, `9170063`.
**Confidence:** 90%.

---

## Item 2 — All-inclusive salary with pacted non-salary payments — ✅ 70% of the salary + the full Law 1393 excess

**Position.** IBC = 70% × all-inclusive salary (Law 100 of 1993 art. 18) **plus** the excess of pacted non-salary payments over 40% of total remuneration, the excess **not** reduced to 70% (Consejo de Estado SU exp. 25185 of 9 December 2021, rule 3; exp. 25907 of 2022). Total remuneration for the 40% test = all-inclusive salary at 100% + pacted non-salary. Example: 30,000,000 + 25,000,000 pacted → 21,000,000 + 3,000,000 = 24,000,000.

**Design effect:** `9170044`, `9170045`.
**Confidence:** 80% (no DIAN/UGPP doctrine on the order for the all-inclusive case; the reading follows the unification ruling).

---

## Item 3 — Law 1393 excess: which funds? — ✅ Health, pension and occupational risk only

**Position.** Law 1393 of 2010 art. 30 applies "for the purposes of articles 18 and 204 of Law 100" (pension and health); occupational risk follows the IBC (Decree-Law 1295 of 1994 art. 17). The payroll levies use Law 21 of 1982 art. 17 (salary + paid rest), so the excess never reaches CCF, SENA or ICBF. The UGPP worked example (ABC Empleadores 2025: salary 5,000,000 + pacted 4,000,000 → IBC 5,400,000, CCF base 5,000,000) confirms it.

**Design effect:** `58104` feeds `58106`/`58112`/`58113`/`58114`, never `58108`.
**Confidence:** 95%.

---

## Item 4 — Which non-salary payments enter the 40% test? — ✅ Only the pacted ones

**Position.** The 40% limit applies to payments that remunerate the service but were excluded from salary by written pact (Labour Code art. 128; Law 344 of 1996 art. 17). Payments non-salary by nature (transport allowance, occasional per diem, tools, work clothing, liberality) are outside the numerator and the total (CE SU 25185/2021, rule 1). Where the nature is unclear, the payment is treated as pacted (WTC class `Non-Salary - pacted`).

**Design effect:** WTC column V; `9170042`.
**Confidence:** 85%.

---

## Item 5 — 72 UVT per dependant and the 40% / 1,340 UVT cap in the monthly withholding — ✅ 72 UVT out; cap in, annual caps year-to-date

**Position.** The 72 UVT per dependant (Tax Code art. 336 num. 3) belong to the annual return only: art. 388 (withholding base) refers to art. 387, not art. 336 (DIAN Concepto 011383 of 2024, chapter IV question 2). The monthly withholding keeps the art. 387 deduction (10% of gross labour income, max 32 UVT). The 40% and 1,340 UVT cap **does** apply in the monthly withholding: Decree 1625 of 2016 art. 1.2.4.1.6 par. 3, as modified by Decree 2231 of 2023, says so expressly, and a decree prevails over doctrine.

The 790-UVT cap of the 25% exempt income, the 1,340-UVT cap and the 3,800-UVT cap of voluntary pension funds and AFC / AVC accounts (shared by the two vehicles) are **annual and tracked year-to-date** per employee, with no monthly apportionment: each month the relief is limited to the part of the annual cap not yet used in the calendar year. The Consejo de Estado (Sección Cuarta, rad. 24047 of 28 October 2021) annulled the monthly equivalent written into Decree 1625 art. 1.2.4.1.6 par. 3, and Decree 2231 of 2023 art. 9 restated the limit as "1.340 UVT anuales"; the 3,800 UVT follow Decree 1625 art. 1.2.1.22.43. A one-off bonus is therefore fully exempt at 25% while the year's unused cap covers it (CCG v1.7 Module 6.3: September 2026 retention bonus, withholding 3,947,554.80 — reproduced by the engine).

Voluntary contributions to the mandatory individual pension account (RAIS) are non-taxable income (Tax Code art. 55: up to 25% of labour income and 2,500 UVT a year) and are **outside** the 40% / 1,340 UVT cap; voluntary-pension / AFC savings (arts. 126-1, 126-4) are exempt income **inside** it.

**Design effect:** `9170075`, `9170077`, `9170080`–`9170083` (year-to-date reads); no 72-UVT regulation.
**Confidence:** 95% (72 UVT out, cap in); 90% (annual caps tracked year-to-date).

---

## Item 6 — Dismissal indemnity withholding — ✅ Outside the monthly base

**Position.** 20% of the indemnities derived from the employment relationship — the art. 64 indemnity, the early-termination indemnity of a fixed-term or work contract and the indemnity for dismissal during protected status (WTC R339, R343, R344) — where the employee's income exceeds 204 UVT (Labour Code art. 65 late-payment indemnity R340 included: "como indemnización"; Tax Code art. 401-3: "Las indemnizaciones derivadas de una relación laboral … a una tarifa del veinte por ciento (20%) para trabajadores que devenguen ingresos superiores al equivalente de doscientas cuatro (204) UVT"; Decree 1625 of 2016 art. 1.2.4.1.13); otherwise the table percentage of the average monthly taxable payments of the previous 12 months, divided by the months of service if fewer than 12 (Decree 1625 art. 1.2.4.1.8 lit. a). The retirement bonus (WTC R345) is always withheld by that percentage ("bonificaciones por retiro definitivo del trabajador", art. 1.2.4.1.8); the 20% of art. 401-3 covers indemnities only. The 204-UVT test reads the monthly salary, as the CCG v1.7 worked example (termination payments out). The 204-UVT test is applied to the monthly income — a reading, since the provision does not define the income measured.

**Design effect:** `9170088`–`9170090` (outside the monthly read `9170072`).
**Confidence:** 85% on the rule; 70% on the measured income.

---

## Item 7 — Non-resident employees — ✅ Flat 20% on the gross payment

**Position.** A non-resident on a Colombian payroll is withheld at 20% on the gross payment (Tax Code arts. 408–415), not on the art. 383 table, until tax residence is acquired (DIAN Concepto 011108 of 29 June 2026, item 10). The base is WTC column P (pensions and end-of-service gratuities included; employer voluntary pension contributions and the occasional per diem excluded). Severance savings and their interest are **not** withheld, for a non-resident as for a resident: Law 100 of 1993 art. 135 par. 3 ("en ningún caso" subject to withholding), whose limitation to payments "por parte de la Nación" was struck down by the Constitutional Court (C-397 of 1994), Decree 1625 of 2016 art. 1.2.4.1.11 and DIAN Oficios 8899 of 2015 and 4358 of 2019; a non-resident who must file applies the art. 206 exemptions in the return (DIAN Concepto 577 of 2020: Tax Code art. 26 with arts. 178 and 235-2).

**Design effect:** `9170132` "CO Income Tax Flat" (ID, name and ordinal of the development team's draft; severance rows false in columns N and P).
**Confidence:** 90% (salary); 92% (severance savings not withheld).

---

## Item 8 — Hours divisor and rest-day surcharge in 2026 — ✅ Two different dates

**Position.** Divisor 220 to 14 July 2026, 210 from 15 July 2026 (Law 2101 of 2021 art. 3; Labour Code art. 161 as amended by Law 2466 of 2025 art. 11). Rest-day / holiday surcharge 80% from 1 July 2025, 90% from 1 July 2026, 100% from 1 July 2027 (Labour Code art. 179 transitional paragraph, Law 2466 of 2025 art. 14). Hourly value and surcharge are read on the date worked.

**Design effect:** constants `52504`, `52505` read at the date of each hours line; `9170012`.
**Confidence:** 95%.

---

## Item 9 — Transport allowance — ✅ Up to 2 minimum wages inclusive, prorated to days

**Position.** Due when the salary is up to 2 minimum wages inclusive (Decree 1470 of 2025; Law 15 of 1959 art. 2), prorated to the days worked (Decree 1258 of 1959 art. 5): 249,095 × 21 / 30 = 174,366.50 in a month with absences. Not salary: out of the IBC and the levy base, in the service-bonus and severance-savings base — once, through its WTC row (W304 = Yes).

**Design effect:** `9170013`, `9170020`.
**Confidence:** 95%.

---

## Item 10 — Vacation compensated in cash — ✅ Salary ÷ 30 × days during employment; ÷ 720 only on termination

**Position.** During employment, at most half of the entitlement may be paid in cash (Labour Code art. 189 num. 1) and it is paid as salary ÷ 30 × business days. The ÷ 720 formula is for the proportional vacation on termination. Vacation paid in cash is out of the IBC (CE S4 exp. 26941 of 2024) and out of the service-bonus and severance base (Labour Code arts. 189, 253, 306), but in the levy base: it is paid rest ("descanso remunerado") under Law 21 of 1982 art. 17 (Consejo de Estado, Sala de Consulta, concepto 2027 of 2010; Consejo de Estado, Sección Cuarta, exp. 27226 of 11 May 2023; UGPP ABC Empleadores 2025 p. 7); cash compensation of vacation is not salary but a kind of indemnity (Supreme Court SL467-2019).

**Design effect:** `9170016`, `9170017`, `9170019`; WTC columns W, X, T.
**Confidence:** 85% on the cash formula and on the IBC / benefit-base exclusion; 94% on the inclusion in the payroll-levy base.

---

## Item 11 — Occupational risk on leave days — ✅ Not due

**Position.** No occupational-risk contribution for vacation taken, incapacity, maternity, paternity or parental leave days (Decree 1072 of 2015 art. 2.2.4.2.1.6; PILA Technical Annex 2 v30 field 26). Health and pension continue.

**Design effect:** separate IBC `58114` (matrix F).
**Confidence:** 92%.

---

## Item 12 — Apprentices — ✅ Support by phase; base never below 1 minimum wage

**Position.** Maintenance support 75% (classroom) or 100% (practical / dual) of the minimum wage (Labour Code art. 81, Law 2466 of 2025 art. 21). The contribution base is in every case at least 1 minimum wage and the employee deductions are computed on it (Decree 0223 of 2026 art. 2.2.6.3.3.4 par. 2). Classroom phase: health and occupational risk; practical phase: all rights of an employment contract.

**Design effect:** `9170011`; `RESEARCH_GAPS.md` R2 (phase field, practical-phase levy split).
**Confidence:** 85%.

---

## Item 13 — Occupational-risk class V maximum — ✅ 6.960% initial; 8.700% top of the range

**Position.** Class initial rates 0.522% / 1.044% / 2.436% / 4.350% / 6.960%; class ranges from 0.348% to 8.700% (Decree 1772 of 1994 art. 13).

**Design effect:** `9170055`.
**Confidence:** 98%.

---

## Item 14 — Base of the art. 64 indemnity — ✅ Art. 127 salary, variable averaged, no transport allowance

**Position.** The daily salary of art. 64 is the salary of Labour Code art. 127, variable parts included: fixed salary → last salary; variable salary → average actually earned in the last year of effective service, suspensions excluded (art. 253 by analogy; Supreme Court, Labour Chamber, SL1659-2025). The transport allowance is not salary and stays out. The same base selects the tier (< or ≥ 10 minimum wages).

**Design effect:** `9170031`, `9170032`.
**Confidence:** 85%.

---

## Item 15 — Illness benefit floor — ✅ Never below the minimum wage

**Position.** 2/3 of the salary (days 1–2 employer, from day 3 health insurer; 1/2 from day 91), never below the minimum-wage equivalent per day, in every segment (Labour Code art. 227; Constitutional Court C-543 of 2007, resolutive part: the art. 227 benefit "no podrá ser inferior al salario mínimo legal vigente"). For a salary below 2 SMMLV the floor binds on days 91–180 (3,000,000: 58,363.50 a day instead of 50,000). Concepto MinSalud 202311602174531 of 20 October 2023 applies the 2/3 to the employer's days 1–2. 100% by agreement is lawful (Labour Code art. 13).

**Design effect:** `9170024`–`9170028`.
**Confidence:** 93%.

---

## Item 16 — Payroll levies on incapacity and leave — ✅ Not due

**Position.** The incapacity benefit is not salary and is excluded from the SENA / ICBF / CCF base (Consejo de Estado, Sección Cuarta, 19 August 2021, exp. 23856); maternity, paternity, parental and childcare leave are paid by the health insurer, not by the employer, so no payroll levies are due on them (Superintendencia del Subsidio Familiar, Concepto 2-2018-083606). UGPP ABC Empleadores 2025 (p. 7) tells employers to include them, while its own table on p. 6 lists these events only for social security; the guide has no normative force.

**Design effect:** WTC column T = No on R123, R326–R333; the levy base `9170047` leaves them out (sweep: 0 differences).
**Confidence:** 92%.

---

## Item 17 — Retroactive pay: which regulations re-run the past period? — ✅ Social security yes, income tax no

**Position.** Withholding under Procedure 1 applies the table to "la totalidad de dichos pagos que se hagan al trabajador … durante el respectivo mes" (Decree 1625 of 2016 art. 1.2.4.1.3): a retroactive amount is withheld in the month it is paid, as the development team's draft (9170132, `simple_tax_post_formula`). Contributions belong to the period earned: a retroactive salary adjustment is re-filed for that period (PILA Technical Annex 2 v30, planilla N: record A original, record C corrected IBC). Social-security regulations therefore keep `retro_`.

**Design effect:** taxRuleGroup of every regulation (`co_design_v2.json`).
**Confidence:** 92%.

---

## Item 18 — Pay periods shorter than 30 days — ✅ Optional projection

**Position.** Under Procedure 1 only, the employer may project the payments of a period shorter than 30 days to 30 days, take the table percentage of the projected amount and apply it to the real payments (Decree 1625 of 2016 art. 1.2.4.1.3 lits. a and b: "su retención podrá calcularse así"). It is optional; entity option, off by default.

**Design effect:** `9170074` (flag `58214`; Procedure 1 only).
**Confidence:** 95%.

---

## Item 19 — Contribution rounding and the non-taxable contributions — ✅ One rounding per contributor and fund; contributions withheld

**Position.** "El valor de los aportes liquidados por cada cotizante … deberá aproximarse al múltiplo de 100 superior más cercano" (Decree 780 of 2016 art. 3.2.1.5 num. 2, as substituted by Decree 1990 of 2016 art. 1); the contribution return validates field 47 as IBC × total pension rate with that rounding (PILA AT2 v30). The total of each fund is therefore rounded once; the employee share is rounded up and the employer pays the residue (the split itself is not regulated). The withholding base excludes "los aportes obligatorios que efectúen los trabajadores" (Tax Code arts. 55, 56): the contributions actually withheld.

**Design effect:** `9170056`, `9170057`, `9170064` (employee and employer bands); `9170075`.
**Confidence:** 95% (rounding of the total); 85% (split); 90% (non-taxable amount).

---

## Summary

| Item | Position | Needs |
|---|---|---|
| 1 — Art. 114-1 test | Salary payments of the month AND IBC < 10 SMMLV | Nothing |
| 2 — All-inclusive + pacted NS | 70% of salary + full excess | Nothing (80%) |
| 3 — Excess scope | Health, pension, ARL; never levies | Nothing |
| 4 — 40% test scope | Pacted non-salary only | Nothing |
| 5 — Dependants / cap | 72 UVT annual only; 40% / 1,340 UVT cap kept in the monthly withholding; 790 / 1,340 / 3,800 UVT caps annual, tracked year-to-date; RAIS voluntary outside the cap | Year-to-date reads (`RESEARCH_GAPS.md` R3) |
| 6 — Indemnity withholding | 20% above 204 UVT of monthly salary on R339 / R340 / R343 / R344; retirement bonus R345 and the rest by the table % of the 12-month average (÷ months of service if fewer) | Measured income (R7) |
| 7 — Non-resident | Flat 20% on column P; severance savings and interest not withheld | Nothing |
| 8 — Hours | Divisor 210 from 15 Jul; surcharge 90% from 1 Jul 2026 | Nothing |
| 9 — Transport allowance | ≤ 2 SMMLV, prorated | Nothing |
| 10 — Vacation in cash | ÷ 30 during employment; ÷ 720 on termination | Nothing |
| 11 — ARL on leave days | Not due | Nothing |
| 12 — Apprentices | Support by phase, 1-SMMLV base | Phase field and split (`RESEARCH_GAPS.md` R2) |
| 13 — ARL class rates | Initial rates per Decree 1772 | Nothing |
| 14 — Indemnity base | Art. 127 salary, variable averaged, no transport allowance | 12-month history read |
| 15 — Illness floor | Minimum wage per day, every segment | Nothing |
| 16 — Levies on incapacity and leave | Not due | Nothing |
| 17 — Rule groups | Income tax without retro_; social security with retro_ | Nothing |
| 18 — Periods < 30 days | Optional projection, Procedure 1 only | Nothing |
| 19 — Rounding and non-taxable contributions | One rounding per contributor and fund; contributions withheld out of the base | Split of the rounded total (A2) |

**Change log.** v2.0 (2 November 2026): basis CCG v1.7, WTC v1.9, DD v1.6; regulation references to the v2.0 IDs; item 6 (all employment indemnities), item 7 (column P; C-397 of 1994; Concepto 577 of 2020; 92%), item 10 (levy base 94%), item 15 (floor in every segment); items 16–19 added; items 6, 7 and 18 revised after the independent review (retirement bonus, months of service, R340, Procedure 1 only). v1.0 (30 October 2026): first release (CCG v1.5, WTC v1.7, DD v1.4). v1.2 (2 November 2026): basis updated to CCG v1.6, WTC v1.8, DD v1.5; item 5 (790 / 1,340 / 3,800 UVT caps annual, tracked year-to-date) and item 7 (severance savings not withheld for non-residents) updated.

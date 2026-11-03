# Colombia QA Report - statutory validation of 30 October and 2 November 2026

What was validated in the Colombia research before the issues of 30 October and 2 November 2026, how, with what result, and
what stays open. Read it before giving a value that touches an item in section 5 or 6. Fiscal year 2026; currency COP.

## Navigation index

| Line | Section |
|---|---|
| 20 | 1. Artifacts in force (issue of 2 November 2026) |
| 37 | 2. How the research was validated |
| 62 | 3. Results |
| 77 | 4. Rules confirmed or corrected by the validation |
| 109 | 5. Open configuration items (14) |
| 130 | 6. Other open points and lower-confidence positions |
| 155 | 7. Not validated |

---

## 1. Artifacts in force (issue of 2 November 2026)

| Artifact | Version | File | MD5 |
|---|---|---|---|
| Country Configuration Guide | CO-CCG-001 v1.7 | `CO-CCG-001-v1.7.docx` | `a966714cdb7272770cfc7b81f9b7fded` |
| Wage Type Catalogue | CO-WTC-001 v1.9 | `CO-WTC-001-v1.9.xlsx` | `374f4545d144fd2d424f73604aa03e1a` |
| Data Dictionary | CO-DD-001 v1.6 | `CO-DD-001-v1.6.xlsx` | `3a017f0efea12d34ff467affd25b8058` |
| Report Spec - electronic payroll | CO-DIAN-001 v1.2 | `CO-DIAN-001-NominaElectronica-Spec.xlsx` | `7cfd6c3e348a4e902ab9a25287f7f88f` |
| Report Spec - Form 350 | CO-DIAN-002 v1.1 | `CO-DIAN-002-Formulario350-Spec.xlsx` | `97e1fae0ae350553568ef432d096b1b2` |
| Report Spec - PILA employees | CO-PILA-003 v1.2 | `CO-PILA-003-AportesSeguridadSocial-Spec.xlsx` | `ecd9b7131696ff7b1edf008fd2edbd7c` |
| Report Spec - Form 220 | CO-DIAN-004 v1.3 | `CO-DIAN-004-Formulario220-Spec.xlsx` | `52af10ae69042e6a2188731a89ff8198` |
| Report Spec - Format 2276 | CO-DIAN-005 v1.2 | `CO-DIAN-005-Formato2276-Spec.xlsx` | `5c9c306d8e4aedd4ac5f192902ca385d` |
| Report Spec - severance-savings deposit | CO-CESANTIAS-006 v1.2 | `CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx` | `08db9ccdcde0ee68c6f24c17bf8aead9` |
| Report Spec - PILA pensioners | CO-PILA-007 v1.1 | `CO-PILA-007-AportesPensionados-Spec.xlsx` | `eae9a7955d23ddea574503de6b573243` |
| Payslip Generator | v1.3 | `CO_Compliance_Payslip_Generator.xlsx` | `619c1410c70775c0aa8b09cc0555f99d` |
| Statutory Integrations Register | CO-SIR-001 v1.4 | Google Doc; v1.4 export `CO-SIR-001-v1.4-export-2026-11-02.txt` | `40c4c5492be05be2c57f10f820a3307b` |

## 2. How the research was validated

Same method as the France validation: an independent calculation engine, written from the statutes before the research was read,
is run on a suite of cases and compared line by line with what the research tells a payroll engine to compute. Every difference is
settled against the primary source, and the artifact is corrected or the difference is explained.

- **Independent law engine:** 98 statutory cases (minimum wage, all-inclusive salary, the 4 / 10 / 16-20 / 25 minimum-wage
  thresholds, overtime and rest-day premiums across the July 2026 dates, service bonus, severance savings and interest, vacation,
  leave, termination, withholding Procedure 1 and 2, non-resident, apprentices, contributor type 51), 17 cases rebuilt from the
  research's own worked examples, and 5 boundary cases added for the corrected rules. Self-check of the engine on boundary values
  (-1 / exact / +1): 45 of 45.
- **Real payroll (Test 4):** a client's September 2026 payroll from its payroll provider, masked before reading (no names,
  identifiers or individual salaries kept), recomputed by the law engine.
- **Primary-source research (30 October 2026):** 54 open points decided on official text (statutes, decrees, DIAN and Ministry
  doctrine, Consejo de Estado and Corte Constitucional, PILA Technical Annexes 2 v30 and 3 v15 as amended by Res. MSPS 1529 de 2026).
- **Independent final review:** a reviewer who had not edited the artifacts re-read all finals against the decisions and
  the official sources, swept every amount of six digits or more against multiples of the minimum wage and the UVT, and recomputed
  the main worked examples.
- **Second pass on primary sources (2 November 2026):** the points left open on 30 October re-researched on official text
  (Consejo de Estado S4 rad. 24047 of 2021, Decreto 2231 de 2023, Ley 100 art. 135, DIAN Oficios 8899 de 2015 and 4358 de 2019,
  Form 220 instructions, Anexo Técnico NE v1.0, AT2 v30, Res. MinTrabajo 2708 de 2026). The law engine was rerun with the annual
  UVT caps tracked year-to-date, and the worked examples of the CCG and the payslip were recalculated with the premise written.
- **Release cross-check:** every final compared with its approved draft; the only text differences are the declared edits; no final
  cites another artifact at a version other than the one in force.

## 3. Results

| Check | Result |
|---|---|
| Research against the law engine (tolerance COP 1) | 89 items: 69 equal; 20 different - all 20 were values of the previous versions and are corrected in the finals (19 take the engine value; 1 is an engine limitation: the research correctly applies the 1-minimum-wage incapacity floor) |
| Test 4, September 2026 payroll | 5,958 lines: 4,530 equal, 342 within tolerance, 342 without data, 742 different, 2 without effect - **0 differences attributed to the research**; all 742 are provider errors (art. 64 indemnity, withholding reliefs not applied, art. 114-1 exoneration, ARL class, employer base below the IBC, incapacity paid at 100%) |
| Simulation workbooks (30 October) | 2,137 lines compared with the law engine, 0 differences (computed before the second pass; in the tabs where the 790 / 1,340 UVT caps bind, rule 18 governs) |
| Primary-source research (30 October) | 54 points: 46 changed an artifact, 5 confirmed with a note; the remaining points were settled as stated positions |
| Independent final review | 15 statements corrected; 6 further items and 7 doubts decided on primary sources and applied |
| Second pass (2 November) | 8 decisions changed the finals (rules 18 and 20 to 25, and rule 8 applied to the remaining Circular 101 citations), plus the shared 3,800-UVT cap (rule 19); 5 positions confirmed unchanged with a stronger source (section 6) |
| Law engine, annual caps year-to-date | 51 monthly cases with withholding rerun; 18 of them change (the cap had bound on a monthly basis). CCG examples recalculated: retention-bonus example (September 2026) withholding 3,947,554.80; habitual bonus (October 2026) 1,763,832.00, and 1,899,912.00 with a non-salary pact; all-inclusive salary 3,243,282.00; payslip example (August 2026) 1,993,152.00 - engine and finals equal |
| Release cross-check | PASS, 0 failures, on all 12 finals (issue of 2 November 2026, including the cross-reference check) |

The baseline (engine, cases, results) is frozen: a future change to the research is checked as a regression against it.

## 4. Rules confirmed or corrected by the validation

Positions written into the finals, with the source and the confidence of the decision.

| # | Rule (2026) | Source | Confidence |
|---|---|---|---|
| 1 | **Art. 114-1 exoneration** (employer health 8.5%, SENA 2%, ICBF 3%): only the **salary payments of the month** are tested against 10 SMMLV (non-salary, vacation pay, benefits and indemnities out), **and** the health IBC must be below 10 SMMLV - PILA field 76 refuses the exonerated mark otherwise | ET art. 114-1; DIAN Conceptos 8380 de 2024 and 7196 de 2025; Consejo de Estado S4 exp. 25302 de 2022; AT2 v30 field 76 | 90% |
| 2 | **All-inclusive salary:** IBC = 70% of the salary **plus** the full Ley 1393 excess (not reduced to 70%); the 40% test uses the salary at 100% | Ley 100 art. 18; CE SU 25185 de 2021; exp. 25907 de 2022 | 80% |
| 3 | **Ley 1393 excess** enters health, pension and occupational risk only - never CCF, SENA or ICBF | Ley 1393 de 2010 art. 30; Decreto-Ley 1295 de 1994 art. 17; Ley 21 de 1982 art. 17 | 95% |
| 4 | **40% test** applies only to payments desalarised by written pact (CST art. 128); payments non-salary by nature are outside the numerator, the total and the IBC | CE SU 25185 de 2021 | 85% |
| 5 | **Withholding depuration:** the 72 UVT per dependant (ET art. 336 num. 3) belong to the annual return only; the monthly withholding keeps the art. 387 dependants deduction (10%, max 32 UVT) and **keeps the 40% / 1,340 UVT cap**; voluntary contributions to the mandatory RAIS account are non-taxable up to 25% / 2,500 UVT and outside the cap | DIAN Concepto 011383 de 2024 IV.2; DUR 1625 de 2016 art. 1.2.4.1.6 par. 3 (Decreto 2231 de 2023); ET art. 55 | 95% |
| 6 | **Art. 64 indemnity:** base = art. 127 salary with the variable part (average of the last year), **without** the transport allowance; the year fraction is paid proportionally; the same base selects the < / ≥ 10 SMMLV tier | CST arts. 64, 127; CSJ SL1659-2025 | 85% |
| 7 | **Rest-day / holiday surcharge:** 80% from 1 July 2025, **90% from 1 July 2026**, 100% from 1 July 2027; hours divisor 220 to 14 July 2026, **210 from 15 July 2026** | CST art. 179 transitional par. (Ley 2466 de 2025 art. 14); Ley 2101 de 2021 art. 3; CST art. 161 | 95% |
| 8 | **Ministry of Labour Circular 101 de 2025 is revoked** (Resolution 2708 de 2026); the rules rest on the statute (CCG v1.7: rest-day substitution, hourly divisors, piece-rate workers, overtime maxima) | Vigency note of the Circular; Res. MinTrabajo 2708 de 2026 | 90% |
| 9 | **Transport allowance** prorated to days worked (249,095 × 21 / 30 = 174,366.50) | Ley 15 de 1959 art. 2; Decreto 1258 de 1959 art. 5 | 95% |
| 10 | **Vacation paid in cash during employment:** salary ÷ 30 × days (÷ 720 only on termination); out of the IBC and of the benefit base, in the levy base | CST arts. 186, 189; CSJ SL467-2019 | 90% |
| 11 | **No occupational-risk contribution** on vacation, incapacity, maternity, paternity and parental-leave days | Decreto 1072 de 2015 art. 2.2.4.2.1.6; AT2 v30 field 26 | 92% |
| 12 | **Occupational-risk class IV maximum 6.960%** (class initial rates 0.522 / 1.044 / 2.436 / 4.350 / 6.960%) | Decreto 1772 de 1994 art. 13 | 98% |
| 13 | **Electronic payroll carries no negative amount**; individual withholding is not rounded (only the forms round to COP 1,000) | DIAN Concepto 014745 de 2025; DUR 1625 art. 1.6.1.11.11 | 95% |
| 14 | **Minimum wage instrument:** COP 1,750,905 under Decreto 1469 de 2025 (provisional suspension revoked on 9 July 2026; Decreto 0159 de 2026 left without effect by ordinal 3 of that order); transport allowance under Decreto 1470 de 2025 | CCG v1.7 Module 4.1 | 94% |
| 15 | **Non-resident:** flat 20% on the gross payment (ET art. 408) until tax residence is acquired; residence over two calendar years starts in the second year | ET arts. 10, 408; DIAN Concepto 011108 de 29 June 2026 | 90% |
| 16 | **Form 350 correction period** 3 years | ET art. 588 (Ley 2010 de 2019 art. 107) | 98% |
| 17 | **PILA (CO-PILA-003 / 007):** Res. MSPS 1529 de 2026 applied - worker type 75 (retirement date field 81 mandatory), contributor type 51 (IBC by day bands) and sub-types 3/4/12 (no PA/CD document) | AT2 v30, AT3 v15, Res. MSPS 1529 de 2026 | 90% |
| 18 | **The 790-UVT cap (25% exempt income) and the 1,340-UVT cap (with the 40% limit) are annual, tracked year-to-date per employee**: each month the exemption is limited to the part of the annual cap not yet used in the year; no monthly limit (790 UVT = COP 41,375,460; 1,340 UVT = COP 70,181,160) | Consejo de Estado S4 rad. 24047 of 28 October 2021 (annulled the monthly equivalent in DUR 1625 art. 1.2.4.1.6 par. 3); Decreto 2231 de 2023 art. 9 ("1.340 UVT anuales"); ET arts. 206 num. 10, 336 num. 3 | 90% |
| 19 | **The 3,800-UVT cap** (COP 199,021,200) of voluntary pension funds and AFC / AVC accounts is **annual, shared** by the two vehicles with the 30%-of-labour-income limit, and tracked year-to-date | ET arts. 126-1, 126-4; DUR 1625 de 2016 art. 1.2.1.22.43; CE S4 rad. 24047 de 2021 | decided with rule 18 |
| 20 | **Severance savings and their interest are not subject to withholding at source for any employee**, resident or non-resident; the 20% for non-residents is only a configurable conservative option, off by default (WTC rows 120-122, 321-322) | Ley 100 de 1993 art. 135 par. 3 (all payers: Corte Constitucional C-397 de 1994); DUR 1625 art. 1.2.4.1.11; DIAN Oficios 8899 de 2015 and 4358 de 2019; DIAN Concepto 577 de 2020 (non-resident return) | 92% |
| 21 | **Form 220 casilla 59 / Format 2276 six-month average** for the severance-savings exemption: the six months of the year before the deposit, salary only, no service bonus (worked examples: 12,000,000) | Form 220 instructions (Res. DIAN 22 de 2024), casilla 59; DIAN Concepto 1302 de 2019 | 88% |
| 22 | **Electronic payroll validation rules:** Anexo Técnico NE v1.0 §6 lists 519 rules (437 for the payroll documents) | Anexo Técnico NE v1.0 §6, pp. 182-232 | 90% |
| 23 | **Electronic payroll element of pacted allowances** (WTC column Y, e.g. rows 255-264): AuxilioNS (NIE142) where non-salary under the pact, otherwise AuxilioS (NIE141); third-party meal payments (row 346) are `Non-Salary - pacted` | Anexo Técnico NE v1.0 pp. 32-39; CST arts. 127, 128 | 92% |
| 24 | **PILA occupational-risk rate (T2R2-061)** written as a decimal with a point, zero-filled to nine positions (0.0052200), like the other rate fields | AT2 v30 (ARL output field 28 "Tarifa. En decimales", from field 61) | 80% |
| 25 | **Electronic payroll bank fields** (bank name, account type, account number) only for account-crediting payment methods of the DD Payment Method mapper: 42, 45, 47, 98 (CATS; added to the mapper); cards 48 / 49 only where linked to a salary account; same list in CO-DIAN-001 NIE066 | Anexo Técnico NE v1.0 NIE064-NIE068; tables 5.3.3.1 / 5.3.3.2 | 85% |

## 5. Open configuration items (14)

Items the engine configuration must settle; none changes a statutory value in the artifacts.

| # | Item | Severity | Detail |
|---|---|---|---|
| 1 | Round-up function | Blocking | The IBC rounds **up** to the peso and each contribution **up** to COP 100 (Decreto 780 de 2016 art. 3.2.1.5). A ceiling function, or an equivalent tested on boundary values, must exist in the engine |
| 2 | Split of the PILA-rounded total | Medium | The rounding is per contributor and fund (employee + employer together); no source states how the rounded total is split between the payslip deduction and the employer cost. Each share is rounded separately; difference at most COP 100 per fund |
| 3 | History reads | Medium | Procedure 2 percentage (12 months, ET art. 386), indemnity withholding percentage (12 months, DUR 1625 art. 1.2.4.1.8), severance-savings exemption (6-month average ≤ 350 UVT, ET art. 206 num. 4) and the art. 64 variable-salary average need reads of 6 or 12 prior periods |
| 4 | IBC of absence days | Medium | Vacation: health and pension on the IBC before the vacation (Decreto 780 art. 3.2.5.1); incapacity / licence: IBC = benefit value; unpaid licence: day reduction. Needs a per-change-event day split, not one monthly base |
| 5 | Occupational-risk rate by work centre | Medium | The insurer-notified rate per work centre (0.348%-8.700%) must override the class initial rate; the DD links class to work centre, not yet to the employee |
| 6 | Apprentice phase field | Medium | The DD has contract type 4 but no phase field; transport allowance due in the practical phase (CST art. 81), not stated for the classroom phase |
| 7 | Year-to-date accumulators for the annual UVT caps | Medium | 790, 1,340 and 3,800 UVT are annual and tracked year-to-date (rules 18 and 19): the engine needs, per employee, the exemption and deductions already used in the calendar year (including the months before a mid-year go-live). Also open: how the 25% budget is shared between the salary and the service-bonus reads in the same month |
| 8 | Multi-employer ceiling | Medium | The 25-SMMLV ceiling applies to the sum across employers; not modelled (flag for reporting only) |
| 9 | Optional 20% on non-resident severance savings | Medium | No withholding is the rule (rule 20); a client that wants the conservative position may switch on the 20% (ET art. 408) for non-residents - off by default |
| 10 | 204-UVT test basis | Medium | The indemnity 20% test (ET art. 401-3) is applied to the monthly income; the provision does not define the income measured |
| 11 | Indemnity variants | Medium | Fixed-term (salaries for the remaining term), specific work, probation (CST arts. 76-80), Ley 789 de 2002 art. 28 transitional table: not in the core indemnity regulation |
| 12 | `Yes/No` wage types | Medium | 17 withholding rows and 5 social-security rows (R6, R37, R227, R338, R358) of the WTC v1.9 need an exempt / subject split at configuration; the 54 `Non-Salary - pacted` rows are handled by the Ley 1393 excess |
| 13 | Solidarity fund under Ley 2381 de 2024 | Medium | New bands from 1 April 2027 (Corte Constitucional C-264 de 2026): effective-date the band table; not a 2026 rule |
| 14 | High-risk pension | Medium | +10 points employer (26% total, Decreto-Ley 2090 de 2003); confirm the split with the PILA configuration |

## 6. Other open points and lower-confidence positions

- **Rest-day percentages in the electronic payroll (`@Porcentaje`, codes 4-7): decided** (post-release review, 30 October 2026).
  Report the statutory percentage, not the annex literal (DIAN Concepto 013840 int. 1568 of 1 October 2025): code 5 = 80 / 90 / 100;
  codes 4 / 6 / 7 = 105-115-125 / 155-165-175 / 115-125-135 (from 1 July 2025 / 2026 / 2027). CCG v1.7 Module 4.4 and CO-DIAN-001
  v1.2 Field Options rows 61-65 agree. Not yet round-tripped through the DIAN validator (95%).
- **Format 2276 XML** element names are DERIVED: the DIAN technical annex / XSD for format 2276 v4 was not obtained.
- **Mercans codes:** the WTC `CO-` codes are mnemonic; no numeric range assigned. Do not state a numeric code.
- **SIR Google Doc:** sections 0 and 2 still describe six filings and do not describe the pensioners PILA flow (CO-PILA-007).
- **WTC sheet Employer Sick Pay** (aligned with CCG Module 8 on 30 October 2026): two thirds for days 1-2 (CST art. 227;
  Concepto MinSalud 202311602174531 de 2023), never below the minimum wage (Corte Constitucional C-543 de 2007), 100% lawful by
  agreement; Mercans default configurable. PILA fields 57-60 are blank / zero (AT2 v30); EPS recovery runs outside the PILA.
- **Ley 2381 de 2024 solidarity bands (2027):** the CCG follows the law (2.8% from 19 to 20 SMMLV inclusive; 3.0% above 20); the
  PILA annex already charges 3.0% at exactly 20 SMMLV. Information only for 2026 (reconfirmed 2 November 2026 with C-264 de 2026, 95%).
- **Confirmed on 2 November 2026 with a stronger source (no change to the finals):**
  - payroll levies on incapacity and leave days not due, including the employer days 1-2 (85%; Ley 21 de 1982 art. 17; UGPP
    practice differs);
  - vacation paid in cash out of the service-bonus and severance base (90%; CSJ SL467-2019);
  - the car-allowance family as `Non-Salary - pacted` (85%; CSJ SL5159-2018; a fixed amount of free use may still be judged salary).
- **Positions at 80% confidence or below** (say so when quoting them):
  - electronic-payroll incapacity type labels 2 "Profesional" / 3 "Laboral" read as occupational disease / accident (75%; the
    annex gives no definition; only a formal DIAN consultation closes it);
  - all-inclusive salary + Ley 1393 order (80%). Raised to 92% on 2 November 2026 (primary sources reread):
    severance savings without withholding for non-residents; PILA occupational-risk rate format (decimal with a point).

## 7. Not validated

- **No filing has been round-tripped through an authority portal or operator.** Every spec is derived from the official source,
  not production-proven.
- No official calculation engine exists for DIAN withholding, PILA or UGPP that could be run as a reference; the independent
  engine was written from the statutes.
- Sector collective agreements and client-specific pacts are per-client configuration and are not enumerated.

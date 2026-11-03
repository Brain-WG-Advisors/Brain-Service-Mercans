---
name: payroll-compliance-colombia
description: Colombia (CO) private-sector payroll compliance for fiscal year 2026 (calendar year), currency COP - retención en la fuente on the ET art. 383 UVT table (Procedimiento 1 and 2, depuration, 25% exempt income and the 40% / 1,340 UVT cap, non-resident 20%), social security on the IBC (health, pension, solidarity fund, ARL), payroll levies CCF / SENA / ICBF with the art. 114-1 exoneration, the Ley 1393 40% test, salario integral, prima, cesantías, vacation, incapacity and the art. 64 indemnity. Covers the seven filings (nómina electrónica, Formulario 350, PILA employees and pensioners, Formulario 220, Formato 2276, annual cesantías deposit), the 405-row Wage Type Catalogue, the Data Dictionary, the integrations register and the payslip. Use for any question about Colombian payroll rates, thresholds, bases, filings, wage types, field mappings or payslip content.
---

# Colombia payroll compliance - router

You are an expert on Colombia payroll compliance for **fiscal year 2026** (calendar year), private-sector employees under the
*Código Sustantivo del Trabajo* (CST). The complete reference set lives in `references/`, converted verbatim from the approved
Colombia artifacts issued on **2 November 2026** (**CO-CCG-001 v1.7, CO-WTC-001 v1.9, CO-DD-001 v1.6**, Report Specs
**CO-DIAN-004 v1.3**, **CO-DIAN-001, CO-DIAN-005, CO-CESANTIAS-006 and CO-PILA-003 v1.2**, **CO-DIAN-002 and CO-PILA-007 v1.1**, Payslip
Generator **v1.3**, **CO-SIR-001 v1.4**), validated on 30 October 2026 against an independent calculation from the statutes, a
real September 2026 payroll (Test 4) and the official sources, with a second pass on primary sources on 2 November 2026
(`references/07-qa-report.md`).

**ALWAYS use the Read tool on the relevant reference file BEFORE answering. Do NOT answer Colombian rates, thresholds, UVT /
SMMLV multiples, XML element names, code values or deadlines from general knowledge.**

Colombia 2026 changes parameters **mid-year on two different dates**: the rest-day / holiday surcharge steps from 80% to **90% on
1 July 2026**, and the hours divisor from 220 to **210 on 15 July 2026**. A July 2026 payroll spans both. A figure recalled rather
than read is a figure attached to the wrong date.

The reference files are large. Each opens with a **line-numbered navigation index** - read with `offset` / `limit`, or Grep for
the article, field ID, wage type or Module number, rather than pulling a whole file.

---

## Routing - read the right file FIRST

| Topic | Read |
|---|---|
| SMMLV, UVT, transport allowance, thresholds in SMMLV / UVT, salary components, proration, overtime, surcharges, bonuses, salary vs non-salary, the 40% test | `references/01-ccg.md` (Module 4) |
| Gross-to-net flow; the three bases (IBC, payroll-levy base, withholding base) | `references/01-ccg.md` (Module 3) |
| Health, pension, solidarity fund, ARL, CCF / SENA / ICBF, IBC, art. 114-1 exoneration, PILA change events, pensioners | `references/01-ccg.md` (Module 5) |
| Retención en la fuente: table, depuration, Procedimiento 1 / 2, residents vs non-residents | `references/01-ccg.md` (Module 6; reliefs in Module 7) |
| Vacation, incapacity, maternity / paternity, other leave | `references/01-ccg.md` (Module 8) |
| Termination, cesantías and interest, art. 64 indemnity, retroactive payments | `references/01-ccg.md` (Module 9) |
| Pay frequencies, deadlines, holidays, rounding; master data; reporting, payslip, year-end | `references/01-ccg.md` (Modules 1, 2, 10) |
| Worked gross-to-net examples | `references/01-ccg.md` (Module 12) |
| Wage type treatment (tax, health, FSP, ARL, levies, pension, salary class, benefit base, NE element) | `references/02-wtc.md` |
| Channels, authentication, M2M vs portal, penalties, deadlines by authority | `references/03-sir.md` |
| Report fields, XML / flat-file layout, code lists, validation, worked examples | `references/04-reports-spec.md` |
| Master data fields, M / CM / O, option mappers, document types | `references/05-data-dictionary.md` |
| Payslip content, EN / ES labels, line list | `references/06-payslip.md` |
| What was validated, confidence of each position, open configuration items | `references/07-qa-report.md` |

### Which CCG module

Mod 1 fiscal year, pay cycles, holidays, rounding · Mod 2 employer and employee master data, residence · Mod 3 gross-to-net and
the three bases · Mod 4 minimum wage, components, proration, overtime, bonuses, wage classification · Mod 5 contributions, IBC,
exoneration, PILA change events · Mod 6 withholding · Mod 7 reliefs, benefits in kind, garnishments · Mod 8 leave · Mod 9
termination and irregular payments · Mod 10 reporting, integrations, payslip, year-end · Mod 11 special scenarios and groups ·
Mod 12 worked examples · Mod 13 business practices.

### Which report spec (seven workbooks in `04-reports-spec.md`: CO-DIAN-004 at v1.3, four at v1.2, CO-DIAN-002 and CO-PILA-007 at v1.1)

**CO-DIAN-001** nómina electrónica (SOAP 1.2, monthly, one document per employee) · **CO-DIAN-002** Formulario 350 (Muisca
portal, monthly) · **CO-PILA-003** PILA employees (operador de información, monthly) · **CO-DIAN-004** Formulario 220
(certificate issued to the employee, **not** filed) · **CO-DIAN-005** Formato 2276 (exógena, annual) · **CO-CESANTIAS-006**
annual severance-savings deposit (fund via operator, by 14 February) · **CO-PILA-007** PILA for pensioners paid by the employer.

---

## How to answer

1. **Identify the reference file(s) from the routing table, and Read them BEFORE drafting.** Never answer a rate, threshold,
   date, field name, code or legal citation from memory.
2. **Quote verbatim - no rounding.** COP 1,750,905, not "about 1.75 million". Say which number format you use: the CCG prints
   `1,750,905`; Colombian print is `1.750.905`; the XML uses `1750905.00`.
3. **Cite artifact + location and the legal basis**: e.g. "CCG v1.7 Module 5.1.1", "WTC v1.9 row 324 column Q", "CO-PILA-003 PILA
   Spec row 156", plus the article: **CST** (labour), **ET** (tax), **Ley 100 de 1993** (social security), **Ley 21 de 1982** /
   **Ley 89 de 1988** (levies), **Ley 1393 de 2010 art. 30**, **Ley 2466 de 2025** (labour reform), **Decreto 780 de 2016**
   (PILA), **DUR 1625 de 2016** (tax), **Res. DIAN 000227 de 2025** (electronic payroll and exógena). "Colombian law" is not a citation.
4. **Give the date a parameter applies from**, and the side of 1 July / 15 July 2026 for any hourly or surcharge figure.
5. **Preserve Spanish terms**, glossing where it helps: SMMLV, UVT, IBC, retención en la fuente, prima de servicios, cesantías,
   auxilio de transporte, salario integral, parafiscales, exoneración, nómina electrónica, CUNE, PILA, devengados / deducciones.
6. **Re-verify time-varying values** (SMMLV, UVT, transport allowance, filing calendars, ARL rate of the work centre) before use
   in a live configuration - say so when you quote them.
7. **State the confidence and any open point** from `07-qa-report.md` sections 5-6 that touches the value you give.
8. **Say plainly when something is not covered** and name the authority: **DIAN** (withholding, nómina electrónica, exógena),
   **UGPP** (contribution audits), **MinTrabajo** (labour rules), **MinSalud** (PILA), the employee's **EPS / AFP / fondo de
   cesantías**, the employer's **ARL / CCF**.

### 2026 parameters (read the CCG for the full table)

SMMLV **COP 1,750,905** (Decreto 1469 de 2025; the provisional suspension was revoked on 9 July 2026 and Decreto 0159 de 2026, which
re-fixed the same amount meanwhile, was left without effect by ordinal 3 of the same order) · UVT **COP 52,374** (Res. DIAN 000238 de 2025) · transport allowance **COP 249,095**
up to 2 SMMLV inclusive (Decreto 1470 de 2025) · 10 SMMLV **17,509,050** · 25 SMMLV (IBC ceiling) **43,772,625** · salario integral
minimum 13 SMMLV **22,761,765**.

### Rules validated on 30 October and 2 November 2026 - give the rule below

Older material and payroll providers often get these wrong (all in the finals; source and confidence in `07-qa-report.md` §4):

- **Art. 114-1 exoneration** (employer health 8.5%, SENA 2%, ICBF 3% - never pension, ARL or CCF): test only the **salary payments
  of the month** against 10 SMMLV (non-salary payments, vacation pay, benefits and indemnities out; DIAN Conceptos 8380/2024 and
  7196/2025), **and** the health IBC must also be below 10 SMMLV - PILA field 76 refuses the exonerated mark otherwise. Strictly
  below; per employee, per month; a natural-person employer with fewer than two employees has no exoneration.
- **Ley 1393 de 2010 art. 30 (40% test)** applies **only to payments desalarised by written pact** (CST art. 128). Payments
  non-salary by nature (transport allowance, occasional per diem, tools, work clothing, mere liberality) are outside the test and
  outside the IBC (Consejo de Estado SU 25185 de 2021). WTC class `Non-Salary - pacted` vs `Non-Salary - non-remunerative`.
- **The Ley 1393 excess enters health, pension and ARL only** - never CCF, SENA or ICBF (the levy base is Ley 21 de 1982 art. 17).
- **Salario integral:** IBC = **70%** of the salary **plus the full Ley 1393 excess** (not reduced to 70%); the 40% test uses the
  salary at 100% (Ley 100 art. 18; CE SU 25185 de 2021, exp. 25907 de 2022). Confidence 80%.
- **Withholding depuration:** the **72 UVT per dependant** (ET art. 336 num. 3) are for the **annual return only** - not in the
  monthly withholding (DIAN Concepto 011383 de 2024); the monthly withholding keeps the art. 387 dependants deduction (10%, max 32
  UVT) and **keeps the 40% / 1,340 UVT cap** (DUR 1625 art. 1.2.4.1.6 par. 3, Decreto 2231 de 2023). The 25% exempt income
  (ET art. 206 num. 10, 790 UVT a year) is computed on the figure after deductions. Voluntary contributions to the mandatory RAIS
  account are non-taxable up to 25% / 2,500 UVT and **outside** the cap (ET art. 55).
- **The 790-UVT, 1,340-UVT and 3,800-UVT caps are annual, tracked year-to-date per employee** - there is **no monthly limit of
  one twelfth**: each month the exemption / deduction is limited to the part of the annual cap not yet used in the calendar year
  (Consejo de Estado S4 rad. 24047 of 28 October 2021, which annulled the monthly equivalent in DUR 1625 art. 1.2.4.1.6 par. 3;
  Decreto 2231 de 2023 art. 9, "1.340 UVT anuales"). The **3,800 UVT** cap (COP 199,021,200) is **shared** by voluntary pension
  funds and AFC / AVC accounts, with the 30%-of-labour-income limit (ET arts. 126-1, 126-4; DUR 1625 art. 1.2.1.22.43). A one-off
  bonus is fully exempt at 25% while the year's unused cap covers it (CCG v1.7 Module 6, worked examples with the premise
  written). Confidence 90%.
- **Severance savings (cesantías) and their interest are never subject to withholding at source** - for **any** employee,
  resident or non-resident (Ley 100 de 1993 art. 135 par. 3, extended to every payer by Corte Constitucional C-397 de 1994; DUR 1625
  art. 1.2.4.1.11; DIAN Oficios 8899 de 2015 and 4358 de 2019); the ET art. 408 flat 20% does not reach them. A non-resident who must
  file applies the art. 206 exemption in the return (DIAN Concepto 577 de 2020). Withholding 20% for non-residents is only a
  configurable conservative option, off by default (WTC v1.9 rows 120-122 and 321-322). Confidence 92%.
- **Art. 64 indemnity:** base = the CST art. 127 salary **including the variable part** (average of the last year; CSJ SL1659-2025),
  **without** the transport allowance; the year fraction is paid **proportionally**; the same base picks the < / ≥ 10 SMMLV tier.
  Withholding: 20% where income exceeds 204 UVT (ET art. 401-3; DUR art. 1.2.4.1.13), outside the monthly base.
- **Rest-day / holiday surcharge 80% to 30 June 2026, 90% from 1 July 2026**, 100% from 1 July 2027 (CST art. 179 transitional
  paragraph, Ley 2466 art. 14). **Divisor 220 to 14 July 2026, 210 from 15 July 2026** (Ley 2101 de 2021 art. 3; CST art. 161).
  Night window 19:00-06:00, night premium 35%.
- **Ministry of Labour Circular 101 de 2025 is revoked** (Resolution 2708 de 2026). Do not cite it; cite the statute.
- **Electronic payroll (CO-DIAN-001) carries no negative amount** (DIAN Concepto 014745 de 2025) - corrections go by adjustment note.
  The individual withholding is **not rounded**; only the DIAN forms round to COP 1,000.
- **Three rounding regimes:** PILA - IBC up to the peso, each contribution **up** to the next COP 100 (Decreto 780 art. 3.2.1.5);
  NE XML - round half to even, ±2.00 tolerance; DIAN forms - nearest COP 1,000. Never unify them.
- **Transport allowance** is prorated to days worked (249,095 × 21 / 30 = 174,366.50); out of the IBC and the levy base; in the
  prima and cesantías base.
- **Vacation paid in cash during employment** = salary ÷ 30 × days (÷ 720 only on termination); out of the IBC. **Vacation taken:**
  health and pension on the IBC before the vacation, no ARL.
- **No ARL contribution** on vacation, incapacity, maternity, paternity or parental-leave days (Decreto 1072 art. 2.2.4.2.1.6).
- **ARL class initial rates** 0.522 / 1.044 / 2.436 / 4.350 / 6.960%; class IV maximum **6.960%** (Decreto 1772 de 1994 art. 13).
- **Solidarity fund (FSP)**, employee only, from IBC ≥ 4 SMMLV: solidarity 0.5% + subsistence 0.5%, subsistence +0.2 / 0.4 / 0.6 /
  0.8 / 1.0% from 16 to above 20 SMMLV (Ley 100 arts. 20 and 27, as amended by Ley 797 arts. 7 and 8).
- **Non-resident:** flat **20%** on the gross payment (ET art. 408) until tax residence is acquired (DIAN Concepto 011108 de 2026);
  when the 183 days span two calendar years, residence starts in the second year (ET art. 10 num. 1). Severance savings and their
  interest are outside the 20% (see above).
- **PILA occupational-risk rate (T2R2-061)** is written as a decimal with a point, zero-filled to nine positions (class I
  0.522% = `0.0052200`), like the other PILA rate fields (AT2 v30 field 28 "Tarifa. En decimales"; AT3 v15 "0.02000"; CO-PILA-003 v1.2). Confidence 92%.
- **Electronic payroll element of pacted allowances** (WTC v1.9 column Y, e.g. rows 201-206, 230-237, 253-264, 348-350): **AuxilioNS (NIE142)** where the
  payment is non-salary under a written CST art. 128 pact, otherwise **AuxilioS (NIE141)** (Anexo Técnico NE v1.0 pp. 32-39).
- **Bank fields of the electronic payroll** (bank name, account type, account number) are populated **only for account-crediting
  payment methods** of the DD Payment Method mapper: 42, 45, 47 and 98 (CATS: Nequi, Daviplata); cards 48 / 49 only where linked to
  a salary account; empty for 10 (cash), 20 (cheque), 71 (bonds) and 72 (vouchers) (Anexo Técnico NE v1.0 NIE064-NIE068, tables
  5.3.3.1 / 5.3.3.2; DD v1.6 ID Information rows 7-9, mapper rows 95-104 (code 46 is account-based like 47 if a client adds it); CO-DIAN-001 v1.2 NIE066 and Population Rules).
  Confidence 85%.
- **Incapacity:** two thirds of salary (CST art. 227), days 1-2 paid by the employer, **never below the minimum wage** (Corte
  Constitucional C-543 de 2007: the benefit "no podrá ser inferior al salario mínimo legal vigente"), in proportion to the days;
  100% is lawful by agreement. Mercans default 66.67%, configurable. Payroll levies (SENA / ICBF / CCF) are not due on incapacity
  (Consejo de Estado S4 exp. 23856 of 2021) or on maternity / paternity / parental / childcare leave paid by the EPS
  (Superintendencia del Subsidio Familiar Concepto 2-2018-083606) - WTC v1.9 rows 123 and 330. Confidence 92%.
- **Pension reform (Ley 2381 de 2024) does not apply to any 2026 period**; the guide dates it at 1 April 2027 (C-264 de 2026).

### Open points you must carry

- **14 configuration items** for the engine (round-up function, PILA rounding split, history reads, IBC of absence days, ARL rate
  by work centre, apprentice phase field, year-to-date accumulators for the annual UVT caps, multi-employer ceiling, optional
  20% on non-resident severance savings, 204-UVT basis, indemnity variants, `Yes/No` wage-type splits, 2027 FSP bands, high-risk pension split) - `07-qa-report.md` §5.
  Say the point is a configuration choice, not a settled statutory value.
- **Rest-day percentages in the electronic payroll `@Porcentaje`: report the statutory percentage**, not the annex table 5.5.5
  literal (100 / 75 / 150 / 110): DIAN Concepto 013840 (int. 1568) of 1 October 2025. Code 5 = 80 / 90 / 100; codes 4 / 6 / 7 =
  105-115-125 / 155-165-175 / 115-125-135, from 1 July 2025 / 2026 / 2027 (CCG v1.7 Module 4.4; CO-DIAN-001 v1.2 Field Options
  rows 61-65). Not yet round-tripped through the DIAN validator (no filing has been).
- **Formato 2276 XML element names are DERIVED** (no DIAN XSD for format 2276 v4 obtained).
- **WTC `CO-` codes have no numeric Mercans code** - do not state one.
- **Positions below 80% confidence** (electronic-payroll incapacity type labels 2 / 3, 75%; the annex gives no definition):
  say so (`07-qa-report.md` §6).
- **No filing has been round-tripped through an authority portal or operator.** Every spec is official-source-derived.

---

## Scope and limits

- **Colombia only, fiscal year 2026, private-sector employees** under the CST, plus pensions an employer pays directly
  (CO-PILA-007). For another country, use that country's skill.
- **Out of scope:** directors paid only by fees (a corporate mandate, not employment), independent workers and service
  contractors, and the MinTrabajo disability-hiring report (HR scope).
- **Currency COP.** Rounding rules are in `01-ccg.md` Module 1.5 - read them before reproducing a computed amount.
- **Language: Spanish.** The electronic payroll and its graphical representation must be in Spanish and COP; another language or
  currency may be added, never substituted (Res. DIAN 000227 de 2025). The payslip ships as `Colombia (EN)` and `Colombia (ES)`.
- **Colombia has no Labour Code article on payslip content**: the binding content is that of the electronic payroll document (Res.
  DIAN 000227 de 2025 art. 1.5.3.3.1); the graphical representation is optional but, if issued, carries that content and the QR code.
  Separately, Ley 1393 de 2010 art. 32 obliges the employer to inform the employee of the contributions paid or let the employee
  check them; itemising them on the payslip is one way to meet it (CCG Module 10.3; Payslip `Colombia (EN)` A78).
- **Monthly cesantías deposit** (Ley 2466 art. 64 par. 1) is not operable until its implementing rule exists; the annual deposit
  does not go through the PILA.
- **Collective agreements and client pacts** (CST art. 128 pacts, extra-legal benefits) are per-client configuration; the
  artifacts do not enumerate them.

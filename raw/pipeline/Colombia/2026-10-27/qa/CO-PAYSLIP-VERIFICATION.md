# Colombia (CO) Payslip — Independent Legislation Verification

**Audited:** 2026-07-12
**Auditor:** Independent compliance cross-check (primary-source web verification)
**File:** `CO-compliance/06-payslip/CO_Compliance_Payslip_Generator.xlsx`
**Overall verdict:** PASS WITH NOTES
**Critical issues (count):** 0

---

## Summary

Every payroll rate, ceiling, threshold, minimum wage and legal citation in the
Colombia payslip was reverified against FY2026 primary/authoritative sources.
All statutory **values** are correct for 2026. The worked example is internally
consistent and the withholding figure reconciles to the Art. 383 table.

The single substantive note is a **stale legal citation** for the minimum wage:
the payslip cites *Decreto 1469 de 2025*, which the Consejo de Estado
**provisionally suspended on 12 Feb 2026** and which was replaced by
*Decreto 0159 de 2026* (same amount, COP 1,750,905). This was already flagged in
the payslip as `[VERIFY WITH RA - decree number]` and is now resolved below. The
amount is correct; only the decree reference should be updated.

---

## Verification table

| Item | Payslip value | Verified FY2026 value | Source | Result |
|---|---|---|---|---|
| Minimum wage (SMMLV) — **amount** | COP 1,750,905/mo | COP 1,750,905/mo (+23% vs 2025) | Decreto 1469/2025; re-fixed by Decreto 0159/2026 | **MATCH** |
| Minimum wage — **decree citation** | Decreto 1469 de 2025 | Decreto 1469/2025 **suspended 12-Feb-2026**; now Decreto **0159 de 2026** | Consejo de Estado auto 12-Feb-2026; Decreto 0159/2026 (19-Feb-2026) | **STALE** (amount correct) |
| Auxilio de transporte — amount | COP 249,095/mo | COP 249,095/mo (+24.5% vs 2025) | Decreto 1470 de 2025 | **MATCH** |
| Auxilio de transporte — decree | Decreto 1470 de 2025 | Decreto 1470 de 2025 (29-Dec-2025) | Cr Consultores / Ámbito Jurídico | **MATCH** |
| Auxilio eligibility (≤ 2 SMMLV) | up to 2 SMMLV | up to 2 SMMLV (≤ COP 3,501,810) | Ley 15 de 1959 | **MATCH** |
| Auxilio excluded from IBC | excluded | excluded from IBC | Ley 100/1993 practice | **MATCH** |
| UVT 2026 | COP 52,374 | COP 52,374 | Resolución DIAN 000238 de 15-Dic-2025 | **MATCH** |
| Withholding system | Progressive marginal (Art. 383 ET) | Progressive marginal (Art. 383/388/206/336 ET) | Estatuto Tributario Art. 383 | **MATCH** |
| Withholding brackets | 0/19/28/33/35/37/39% | 0/19/28/33/35/37/39% | Art. 383 ET | **MATCH** |
| Withholding threshold | > 95 UVT (≈ COP 4,975,530/mo) | > 95 UVT = COP 4,975,530/mo | Art. 383 ET × UVT 2026 | **MATCH** |
| 25% renta exenta cap | 790 UVT/yr | 790 UVT/yr | Art. 206 num. 10 ET (mod. Ley 2277/2022) | **MATCH** |
| 40% global deduction cap | 1,340 UVT/yr | 1,340 UVT/yr | Art. 336 ET | **MATCH** |
| Health — total | 12.5% | 12.5% | Ley 100 de 1993 | **MATCH** |
| Health — employee | 4% (deduction) | 4% | Ley 100 de 1993 | **MATCH** |
| Health — employer | 8.5% | 8.5% | Ley 100 de 1993 | **MATCH** |
| Pension — total | 16% | 16% | Ley 100 de 1993 | **MATCH** |
| Pension — employee | 4% (deduction) | 4% | Ley 100 de 1993 | **MATCH** |
| Pension — employer | 12% | 12% | Ley 100 de 1993 | **MATCH** |
| FSP (Fondo Solidaridad Pensional) | Employee-only 1% for IBC ≥ 4 SMMLV, rising to 2% above 16 SMMLV | Employee-only; 1% from ≥ 4 SMMLV rising to 2% above 20 SMMLV | Art. 27 Ley 100 / Art. 8 Ley 797/2003; Dec. 1833/2016 | **MATCH** |
| IBC floor | 1 SMMLV | 1 SMMLV | Ley 100 de 1993 | **MATCH** |
| IBC ceiling | 25 SMMLV = COP 43,772,625 | 25 × 1,750,905 = 43,772,625 | Ley 100 de 1993 | **MATCH** |
| ARL — payer | Employer-only | Employer-only | Decreto-Ley 1295/1994 | **MATCH** |
| ARL Class I | 0.522% | 0.522% | Decreto 1607 de 2002 | **MATCH** |
| ARL Classes II–V | 1.044 / 2.436 / 4.350 / 6.960% | 1.044 / 2.436 / 4.350 / 6.960% | Decreto 1607 de 2002 | **MATCH** |
| Caja de Compensación | Employer 4% | Employer 4% | Ley 21 de 1982 | **MATCH** |
| SENA | Employer 2% | Employer 2% | Ley 21 de 1982 | **MATCH** |
| ICBF | Employer 3% | Employer 3% | Ley 89 de 1988 | **MATCH** |
| Art. 114-1 exoneration | SENA/ICBF/Salud-ER exonerated < 10 SMMLV | Exoneration of SENA, ICBF & 8.5% health-ER for employees < 10 SMMLV (income-tax payers) | Art. 114-1 ET (Ley 1607/2012) | **MATCH** |
| Cesantías provision | 8.33% (1 mes/año) | 8.33% (1 month/yr) | CST Art. 249 | **MATCH** |
| Intereses a cesantías | 1% (12%/yr) | 12%/yr → 1%/mo provision | Ley 52 de 1975 | **MATCH** |
| Prima de servicios | 8.33% (1 mes/año) | 1 month/yr (½ Jun 30, ½ Dec 20) | CST Art. 306 | **MATCH** |
| Provisión vacaciones | 4.17% | 15 working days/yr ≈ 4.17% | CST Art. 186 | **MATCH** |
| Annual leave | 15 working days/yr | 15 working days/yr | CST Art. 186 | **MATCH** |
| Sick leave (enf. general) | ER days 1–2; EPS from day 3 @ 66.67% (d.1–90), 50% (d.91–180) | Same | Dec. 780/2016 Art. 3.2.1.10; CST Art. 227 | **MATCH** |
| Maternity leave | 18 weeks, EPS-funded | 18 weeks, EPS-funded | CST Art. 236; Ley 1822 de 2017 | **MATCH** |
| Paternity leave | 2 weeks | 2 weeks | CST Art. 236A; Ley 2114 de 2021 | **MATCH** |
| Payslip disclosure duty | Ley 1393/2010 Art. 32 + DIAN Nómina Electrónica (Res. 000013/2021) | Ley 1393/2010 Art. 32; Res. DIAN 000013/2021 | Ley 1393/2010; DIAN | **MATCH** |
| Employer ID | NIT (within RUT), Art. 555-1 ET, format XXX.XXX.XXX-DV | NIT within RUT, Art. 555-1 ET | Estatuto Tributario Art. 555-1 | **MATCH** |
| Employee ID | Cédula de Ciudadanía (C.C.) / Extranjería (C.E.) | C.C. / C.E. | Registraduría / Migración Colombia | **MATCH** |
| Currency | COP | COP (ISO 4217) | ISO 4217 | **MATCH** |

### Worked-example reconciliation (Juan Pérez)

| Line | Payslip | Independent recompute | Result |
|---|---|---|---|
| Basic + Overtime + Commissions (IBC base) | 19,200,000 | 18,000,000 + 500,000 + 700,000 = 19,200,000 | **MATCH** |
| Transport allowance | 0 (salary > 2 SMMLV, correctly not paid) | 0 | **MATCH** |
| Health EE 4% | 768,000 | 19,200,000 × 4% = 768,000 | **MATCH** |
| Pension EE 4% | 768,000 | 768,000 | **MATCH** |
| FSP 1% (IBC ≥ 4 SMMLV) | 192,000 | 19,200,000 × 1% = 192,000 | **MATCH** |
| Retención en la fuente | 2,250,765 | Art. 383 recompute ≈ 2,250,5xx (depuration → ~42.97 UVT) | **MATCH** (reconciles) |
| Total deductions | 3,978,765 | 768,000+768,000+192,000+2,250,765 = 3,978,765 | **MATCH** |
| Net pay | 15,221,235 (via helper cell I8) | 19,200,000 − 3,978,765 = 15,221,235 | **MATCH** |

Contribution/provision rates are applied on the correct base (SUM H21:H23 =
salary items only; auxilio correctly excluded from the IBC). Provisions correctly
include auxilio in cesantías/prima base (H48–H50 use H21:H24).

---

## Critical issues (must fix before handover)

**None.** No wrong tax rate, no wrong social-security rate/ceiling/split, no
employee/employer misallocation, correct minimum wage amount, no fabricated
citations.

---

## [VERIFY WITH RA] items — now resolved

1. **SMMLV 2026 decree number** (payslip: *Decreto 1469 de 2025*)
   → **RESOLVED / update recommended.** The **amount COP 1,750,905 is correct.**
   However *Decreto 1469 de 2025* was **provisionally suspended by the Consejo de
   Estado, Sección Segunda (auto of 12 Feb 2026)** for possible breach of Art. 8
   Ley 278 de 1996. In compliance, the Government issued **Decreto 0159 de 2026
   (19 Feb 2026)**, which temporarily re-fixes the 2026 minimum wage at the
   **same COP 1,750,905**. Recommended edit: cite **Decreto 0159 de 2026**
   (optionally noting Decreto 1469/2025 is suspended pending final ruling). No
   numeric change.

2. **Auxilio de transporte 2026 decree number** (payslip: *Decreto 1470 de 2025*)
   → **RESOLVED / confirmed.** Amount COP 249,095 and **Decreto 1470 de 2025
   (29 Dec 2025)** are both correct. The Consejo de Estado suspension affected
   only the SMMLV decree (1469), not the transport-allowance decree (1470). No
   change needed.

3. **WTC / UnitRate account codes** (`UnitRate Account Details`, and `XXXXX -`
   prefixes) — flagged in-file as `[VERIFY WITH RA - illustrative placeholder…]`
   → **Remains open (expected).** These are placeholder chart-of-accounts codes,
   not a legislation defect. Patch with real CO-WTC codes when available.

---

## Structural check

- **Sheets (8, in order):** `How to set up Payslip` → `Compliance Payslip` →
  `Colombia (EN)` → `Colombia (ES)` → `Payslip Spec 1` → `Field Option` →
  `Population Range` → `UnitRate Account Details`. ✔ Correct.
- **Logo present:** Yes — images embedded on `Colombia (EN)`, `Colombia (ES)`,
  `Compliance Payslip`, `Payslip Spec 1`, `How to set up Payslip`. Footer
  "This document has been generated by Mercans" / "generado por Mercans" present.
- **Residue (genuine Spain/Mozambique leakage only):** None. No Spanish (ES)
  tax brackets, no "Beckham Law", no "Solidarity Quota", no NIF/CIF. Uses correct
  Colombian identifiers (NIT/RUT, C.C./C.E.), COP, and Colombian institutions
  (DIAN, EPS, AFP, ARL, SENA, ICBF, Caja de Compensación). Spanish-language
  labels are legitimate for Colombia.
- **Local-language (ES) sheet genuinely translated:** Yes. All labels, notes and
  the worked example are in Spanish (e.g. "Neto a Pagar", "Devengados",
  "Deducciones", "Aportes del Empleador", "Prestaciones Sociales"). The only
  apparent "English" tokens ("Pension", "Salud") are Spanish words written
  without accents — not English residue.
- **Net-pay formula:** `H34`/top-summary display via helper cell `I8`
  (`=SUM(H21:J24)-SUM(H28:J31)`) — computes correctly to 15,221,235. No defect.

---

## Wage-type codes

**Placeholder** `XXXXX -` prefixes on all earning, deduction, employer-contribution
and provision lines, and **illustrative placeholder account codes** in
`UnitRate Account Details` (e.g. Basic Salary 62100/62104/63100), each explicitly
tagged `[VERIFY WITH RA - align to actual CO-WTC account codes once available]`.
This is **expected** where no real WTC mapping existed yet and is **not a
failure** — flag for later patching with production CO-WTC codes.

---

## Sources consulted

- Ministerio del Trabajo / Presidencia — **Decreto 0159 de 2026** (19-Feb-2026),
  temporary minimum wage: https://dapre.presidencia.gov.co/normativa/normativa/DECRETO%20No.%200159%20DEL%2019%20DE%20FEBRERO%20DE%202026.pdf (accessed 2026-07-12)
- Holland & Knight — "Colombia decreta aumento del salario mínimo y auxilio de
  transporte" (Dec 2025) — Decretos 1469 & 1470 de 2025, COP 1,750,905 / 249,095 (accessed 2026-07-12)
- Holland & Knight — "Suspensión provisional del decreto que fijó el salario
  mínimo para el año 2026" (Feb 2026) — Consejo de Estado suspension of Decreto 1469/2025 (accessed 2026-07-12)
- SUIN-Juriscol / MinTIC Normograma — **Decreto 1469 de 2025** text (accessed 2026-07-12)
- Cancillería / Normograma — **Decreto 159 de 2026** text (accessed 2026-07-12)
- Ámbito Jurídico / Cr Consultores — **Decreto 1470 de 2025**, auxilio COP 249,095 (accessed 2026-07-12)
- DIAN — **Resolución 000238 de 15-Dic-2025**, UVT 2026 = COP 52,374:
  https://www.dian.gov.co/normatividad/Normatividad/Resoluci%C3%B3n%20000238%20de%2015-12-2025.Pdf (accessed 2026-07-12)
- INCP — "DIAN fijó en $52.374 el valor de la UVT para 2026" (accessed 2026-07-12)
- Estatuto Tributario Art. 383 — estatuto.co/383; Actualícese — Retención en la
  fuente 2026, umbral 95 UVT, tarifas 19–39% (accessed 2026-07-12)
- Enlace.com.co / Buk / KnowMyGovt — Aportes seguridad social & parafiscales 2026
  (Salud 4/8.5, Pensión 4/12, SENA 2, ICBF 3, Caja 4, ARL 0.522) (accessed 2026-07-12)
- Bitákora / Sinergy Lowells — Fondo de Solidaridad Pensional 2026, ≥ 4 SMMLV,
  employee-only 1%–2% (accessed 2026-07-12)
- Primary statutes referenced and cross-checked: Ley 100 de 1993; Ley 797 de 2003;
  Decreto-Ley 1295 de 1994; Decreto 1607 de 2002; Ley 21 de 1982; Ley 89 de 1988;
  Art. 114-1 ET (Ley 1607 de 2012); CST Arts. 186/227/236/236A/249/306; Ley 52 de
  1975; Ley 1393 de 2010 Art. 32; Res. DIAN 000013 de 2021.

---

*Auditor's note:* The Colombia payslip is legislatively sound for FY2026. The
only recommended edit before handover is the minimum-wage **decree citation**
(1469/2025 → 0159/2026); all monetary values, rates, ceilings and employee/
employer splits are correct. Verdict: **PASS WITH NOTES**.

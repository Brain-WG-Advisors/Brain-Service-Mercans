# Colombia - Payslip - COMPLETE REFERENCE

**Source artifact:** `06-payslip/CO_Compliance_Payslip_Generator.xlsx` (8 sheets, Mercans reference format,
palette matched cell-for-cell to `shared/REFERENCE_Payslip_Spain.xlsx`)
**Jurisdiction:** Colombia (CO) - **Currency:** COP - **Fiscal year:** 2026
**Sheets:** `How to set up Payslip` - `Compliance Payslip` - `Colombia (EN)` - `Colombia (ES)` -
`Payslip Spec` - `Field Option` - `Population Range` - `Unit Rate Details`

---

## 1. Mandatory payslip content - the legal position

**Colombia has NO statutory payslip-content article in its labour code.** The Substantive Labour Code
(*Codigo Sustantivo del Trabajo*, Decreto 2663 de 1950) was grep-tested across its full consolidated text for
the seven Spanish terms used for a payslip - *desprendible*, *comprobante de pago*, *colilla*,
*volante de pago*, *recibo de pago*, *constancia de pago* and *detalle de la liquidacion* - with **zero hits**.
Ley 2466 de 2025 added none.

**The operative itemisation rule is tax law, not labour law: Resolucion DIAN 000013 de 2021 art. 5**, which
lists the mandatory content of the electronic payroll support document, read with **art. 24**, which makes the
graphical representation *permissive* but requires it to carry that content if it is issued.

A separate, genuinely labour-law duty exists and is narrower: **Ley 1393 de 2010** obliges the employer to
inform the worker of the social-security contributions paid on the worker's behalf.

### Resolucion DIAN 000013 de 2021 art. 5 - the 13 mandatory items, and their status in this generator

| # | Item | Present in the generator |
|---|---|---|
| 1 | Employer's or issuer's surnames and names, or corporate name, and tax identification number | YES - rows 7, 9 |
| 2 | Employee's or beneficiary's surnames and names, and identity document number | YES - rows 12, 16 |
| 3 | Identification of the document - a unique consecutive number preceded by the authorised prefix | **NO** - only a static `REF-CO-2026` footer |
| 4 | Generation date (*fecha de generacion*) | **NO** |
| 5 | Payment or credit date (*fecha de pago o abono*) | **NO** |
| 6 | Accrued payroll values (*valores devengados de nomina*), itemised by concept | YES - rows 21-25 |
| 7 | Deducted payroll values (*valores deducidos de nomina*), itemised by concept | YES - rows 28-32 |
| 8 | Total difference between accrued and deducted | YES - row 34 |
| 9 | Payment or credit period | PARTIAL - `Tax Month` / `Days in Month`, no explicit period start/end |
| 10 | Payment method and medium (*forma y medio de pago*) | PARTIAL - banking block, no payment-method code |
| 11 | Country, department and municipality of origin | PARTIAL - free-text employer address |
| 12 | Content of the authorised technical annex | - |
| 13 | **CUNE** - *Codigo Unico de Nomina Electronica* | **NO** |
| - | Technical Annex 13.1: **QR code at least 2 cm x 2 cm on EVERY page**, encoding the DIAN document-search URL with the CUNE as key | **NO** |

> **[QA MAJOR-02]** Grepping the entire workbook for `CUNE`, `QR`, `prefij`, `consecutiv`,
> `Fecha de generacion` and `Generation date` returns **zero hits in all 8 sheets**. If a client issues the
> graphical representation, the document as templated does not carry the art. 5 content that art. 24 requires -
> and the CUNE + QR are precisely what make the paper document traceable to the validated XML.
> **Fix:** add a header block for `Prefijo + Consecutivo`, `Fecha de generacion`, `Fecha de pago`,
> `Periodo de pago (desde/hasta)`, `Forma y medio de pago`, `Pais / Departamento / Municipio de origen`, a
> `CUNE` field, and a placeholder image anchor sized >= 2 cm x 2 cm for the QR. The DD fields already exist:
> `Electronic Payroll Document Prefix`, `Place of Work Country/Department/Municipality Code`, `Payment Form`,
> `Payment Method`.

### Additional mandatory formal requirements where a graphical representation is issued

| Requirement | Rule |
|---|---|
| **Language** | **Spanish**, mandatory. Another language may be **added**, never substituted (Res. DIAN 000013 de 2021 art. 26) |
| **Currency** | **Colombian pesos**, mandatory. Another currency may be added (art. 26) |
| **QR code** | At least **2 cm x 2 cm on every page**, encoding the DIAN document-search URL with the CUNE as the key (Anexo Tecnico 13.1) |
| **Legal status** | The paper or PDF document is a **representation** of the electronic document, not the document itself. Its legal validity derives from the validated XML |

The bilingual design of this generator - `Colombia (ES)` fully in Spanish plus `Colombia (EN)` in English -
satisfies art. 26: Spanish is mandatory and any other language is additive.

### Mercans practice - good practice, not legally required

- itemisation of **employer contributions** for transparency (never a deduction from the employee);
- the **statutory benefit accruals** (*prestaciones sociales*) and balances;
- the **vacation balance**;
- the **hourly divisor and rest-day premium percentage applied**, given the two mid-2026 cut-overs
  (divisor 220 -> 210 on 15 Jul 2026; rest-day premium 80% -> 90% on 1 Jul 2026);
- contract type, hire date and pay frequency;
- year-to-date totals.

### A rounding rule that must not be blended

The payslip carries the **XML** figures - two decimals, round-half-to-even. It must **not** display the
PILA contribution figures (rounded **up** to the nearest 100) as if they were the deduction, nor the
Formulario 350 figure (rounded to the nearest 1,000). Where the client requires the contribution-return figure
to be shown, it must appear as a **separate, labelled line**.

*Legal basis: Resolucion DIAN 000013 de 11 febrero 2021 arts. 5, 24, 26 and Anexo Tecnico 13.1; Ley 1393 de
2010; Codigo Sustantivo del Trabajo (Decreto 2663 de 1950), full consolidated text - no payslip-content
article.*

---

## 2. Line-by-line payslip layout, EN and ES labels side by side

Row numbers are the actual worksheet rows of `Colombia (EN)` and `Colombia (ES)` (identical geometry).
Amounts are the delivered worked example: monthly gross **19,200,000 COP**, net **15,221,235 COP**.

| Row | Section | Label - Colombia (EN) | Label - Colombia (ES) | Rate | Amount (COP) |
|---|---|---|---|---|---|

| 3 | Title | Colombia Payslip (Desprendible de Pago) | Nomina - Colombia (Desprendible de Pago) |  |  |
| 6 | Net pay banner | Net Pay: | Neto a Pagar: |  |  |
| 7 | Employer details | Employer Name | Nombre del Empleador |  |  |
| 8 | Employer details | Employer Address | Direccion del Empleador |  |  |
| 9 | Employer details | NIT (Employer Tax ID) | NIT del Empleador |  |  |
| 10 | Employer details | ARL Risk Class | Clase de Riesgo ARL |  |  |
| 12 | Employee details | Employee Name | Nombre del Trabajador |  |  |
| 13 | Employee details | Employee Code | Codigo del Empleado |  |  |
| 14 | Employee details | Completed Years in Service | Anos Completos de Servicio |  |  |
| 15 | Employee details | Tax Month | Mes de Liquidacion |  |  |
| 16 | Employee details | Days in Month | Dias del Periodo |  |  |
| 17 | Employee details | EPS (Health) / AFP (Pension) | EPS (Salud) / AFP (Pension) |  |  |
| 19 | Earnings (Devengados) | Salary Detail (Devengados) | Detalle Salarial (Devengados) |  |  |
| 20 | Earnings (Devengados) | Payment Item | Concepto | Rate | Amount |
| 21 | Earnings (Devengados) | XXXXX - Basic Salary (Salario Basico) | XXXXX - Salario Basico |  | 18000000 |
| 22 | Earnings (Devengados) | XXXXX - Overtime & Surcharges (Horas Extra y Recargos) | XXXXX - Horas Extra y Recargos |  | 500000 |
| 23 | Earnings (Devengados) | XXXXX - Commissions & Bonuses (Comisiones y Bonificaciones) | XXXXX - Comisiones y Bonificaciones |  | 700000 |
| 24 | Earnings (Devengados) | XXXXX - Transport Allowance (Auxilio de Transporte - only up to 2 SMMLV) | XXXXX - Auxilio de Transporte (solo hasta 2 SMMLV) |  | 0 |
| 25 | Earnings (Devengados) | Total Earnings (Total Devengado) | Total Devengado |  | `=CONCATENATE(TEXT(SUM(H21:J24),"#,##0")," ",G7)` |
| 27 | Deductions (Deducciones) | Deduction Item (Deducciones) | Deducciones | Rate | Amount |
| 28 | Deductions (Deducciones) | XXXXX - Health Contribution - Employee (Salud - Empleado) | XXXXX - Aporte a Salud - Empleado | 4% | `=ROUND(SUM($H$21:$H$23)*0.04,0)` |
| 29 | Deductions (Deducciones) | XXXXX - Pension Contribution - Employee (Pension - Empleado) | XXXXX - Aporte a Pension - Empleado | 4% | `=ROUND(SUM($H$21:$H$23)*0.04,0)` |
| 30 | Deductions (Deducciones) | XXXXX - Solidarity Pension Fund FSP (Fondo de Solidaridad Pensional) | XXXXX - Fondo de Solidaridad Pensional (FSP) | 1% | `=ROUND(SUM($H$21:$H$23)*0.01,0)` |
| 31 | Deductions (Deducciones) | XXXXX - Income Tax Withholding (Retencion en la Fuente) | XXXXX - Retencion en la Fuente |  | 2250765 |
| 32 | Deductions (Deducciones) | Total Deductions (Total Deducciones) | Total Deducciones |  | `=CONCATENATE(TEXT(SUM(H28:J31),"#,##0")," ",G7)` |
| 34 | Net pay | Net Pay (Neto a Pagar): | Neto a Pagar: |  | `=CONCATENATE(TEXT(SUM(I8),"#,##0")," ",G7)` |
| 36 | Employer contributions (Aportes del Empleador) | Employer Contributions (Aportes del Empleador) | Aportes del Empleador |  |  |
| 37 | Employer contributions (Aportes del Empleador) | Contribution Item | Concepto | Rate | Amount |
| 38 | Employer contributions (Aportes del Empleador) | XXXXX - Health Contribution - Employer (Salud - Empleador) | XXXXX - Aporte a Salud - Empleador | 8.5% | `=ROUND(SUM($H$21:$H$23)*0.085,0)` |
| 39 | Employer contributions (Aportes del Empleador) | XXXXX - Pension Contribution - Employer (Pension - Empleador) | XXXXX - Aporte a Pension - Empleador | 12% | `=ROUND(SUM($H$21:$H$23)*0.12,0)` |
| 40 | Employer contributions (Aportes del Empleador) | XXXXX - Occupational Risk (Riesgos Laborales - ARL, Class I) | XXXXX - Riesgos Laborales (ARL, Clase I) | 0.522% | `=ROUND(SUM($H$21:$H$23)*0.00522,0)` |
| 41 | Employer contributions (Aportes del Empleador) | XXXXX - Family Compensation Fund (Caja de Compensacion Familiar) | XXXXX - Caja de Compensacion Familiar | 4% | `=ROUND(SUM($H$21:$H$23)*0.04,0)` |
| 42 | Employer contributions (Aportes del Empleador) | XXXXX - SENA Training Levy (Aporte SENA) | XXXXX - Aporte SENA | 2% | `=ROUND(SUM($H$21:$H$23)*0.02,0)` |
| 43 | Employer contributions (Aportes del Empleador) | XXXXX - ICBF Family Welfare (Aporte ICBF) | XXXXX - Aporte ICBF | 3% | `=ROUND(SUM($H$21:$H$23)*0.03,0)` |
| 44 | Employer contributions (Aportes del Empleador) | Total Employer Contributions (Total Aportes Empleador) | Total Aportes del Empleador |  | `=CONCATENATE(TEXT(SUM(H38:J43),"#,##0")," ",G7)` |
| 46 | Benefit provisions (Prestaciones Sociales) | Social Benefit Provisions (Prestaciones Sociales - Provisiones) | Prestaciones Sociales (Provisiones) |  |  |
| 47 | Benefit provisions (Prestaciones Sociales) | Contribution Item | Concepto | Rate | Amount |
| 48 | Benefit provisions (Prestaciones Sociales) | XXXXX - Severance (Cesantias) | XXXXX - Cesantias | 8.33% | `=ROUND(SUM($H$21:$H$24)*0.0833,0)` |
| 49 | Benefit provisions (Prestaciones Sociales) | XXXXX - Interest on Severance (Intereses a las Cesantias) | XXXXX - Intereses a las Cesantias | 1% | `=ROUND(SUM($H$21:$H$24)*0.01,0)` |
| 50 | Benefit provisions (Prestaciones Sociales) | XXXXX - Service Bonus (Prima de Servicios) | XXXXX - Prima de Servicios | 8.33% | `=ROUND(SUM($H$21:$H$24)*0.0833,0)` |
| 51 | Benefit provisions (Prestaciones Sociales) | XXXXX - Paid Leave Accrual (Provision de Vacaciones) | XXXXX - Provision de Vacaciones | 4.17% | `=ROUND(SUM($H$21:$H$23)*0.0417,0)` |
| 52 | Benefit provisions (Prestaciones Sociales) | Total Provisions (Total Provisiones) | Total Provisiones |  | `=CONCATENATE(TEXT(SUM(H48:J51),"#,##0")," ",G7)` |
| 54 | Banking details | Banking Details | Datos Bancarios |  |  |
| 55 | Banking details | Beneficiary Name | Nombre del Titular | Bank | Currency |
| 56 | Banking details | Juan Perez | Juan Perez | Bancolombia S.A. | COP |
| 58 | Contribution & provision summary | Contribution & Provision Summary (Resumen de Aportes) | Resumen de Aportes y Provisiones |  |  |
| 59 | Contribution & provision summary | Contribution Base / IBC (Base de Cotizacion) | Base de Cotizacion (IBC) |  | `=SUM(H21:H23)` |
| 60 | Contribution & provision summary | Total Employee Contributions (Salud + Pension + FSP) | Total Aportes del Trabajador (Salud + Pension + FSP) |  | `=SUM(H28:H30)` |
| 61 | Contribution & provision summary | Total Employer Contributions & Parafiscales | Total Aportes del Empleador y Parafiscales |  | `=SUM(H38:H43)` |
| 62 | Contribution & provision summary | Total Social Benefit Provisions (Prestaciones) | Total Provisiones (Prestaciones Sociales) |  | `=SUM(H48:H51)` |
| 63 | Contribution & provision summary | Total Employer Cost (Contributions + Provisions) | Costo Total del Empleador (Aportes + Provisiones) |  | `=SUM(H38:H43)+SUM(H48:H51)` |
| 65 | Year-to-date (Acumulados) | Year-to-Date (Acumulados del Ano) | Acumulados del Ano (YTD) |  |  |
| 66 | Year-to-date (Acumulados) | YTD Gross Earnings | Acumulado Devengado |  | 134400000 |
| 67 | Year-to-date (Acumulados) | YTD Employee Contributions | Acumulado Aportes Trabajador |  | 12096000 |
| 68 | Year-to-date (Acumulados) | YTD Income Tax Withheld | Acumulado Retencion en la Fuente |  | 15755355 |
| 69 | Year-to-date (Acumulados) | YTD Net Pay | Acumulado Neto Pagado |  | 106548645 |
| 71 | Statutory notes | Statutory Notes - Fiscal Year 2026 | Notas Legales - Ejercicio Fiscal 2026 |  |  |
| 81 | Footer | This document has been generated by Mercans | Este documento ha sido generado por Mercans |  |  |
| 82 | Footer | This document has been generated by Mercans | Este documento ha sido generado por Mercans |  |  |
| 83 | Footer | REF-CO-2026 | REF-CO-2026 |  |  |

> **[QA MAJOR-01]** Every wage-type code on both language sheets is an `XXXXX` placeholder
> (rows 21-24, 28-31, 38-43, 48-51 = 18 lines x 2 sheets = **36 cells**). The WTC contains exact matches for
> all 18 lines. Substitute the real codes:
> `CO-SALARIO-BASICO`, `CO-AUX-TRANSPORTE`, `CO-COMISIONES`, `CO-DED-SALUD`, `CO-DED-PENSION`,
> `CO-DED-FSP-SOLIDARIDAD`, `CO-RETENCION-FUENTE`, `CO-ER-SALUD`, `CO-ER-PENSION`, `CO-ER-ARL`, `CO-ER-CCF`,
> `CO-ER-SENA`, `CO-ER-ICBF`, `CO-PROV-CESANTIAS`, `CO-PROV-INTERESES-CESANTIAS`, `CO-PROV-PRIMA`,
> `CO-PROV-VACACIONES`. Rows 22 (*Overtime & Surcharges*) and 23 (*Commissions & Bonuses*) each bundle
> multiple wage types - split them or label them with an explicit multi-code list.

---

## 3. The calculation - every formula in the generator, and the arithmetic re-derived

| Cell | Line | Formula (verbatim) |
|---|---|---|
| `I8` | Employer Address | `=SUM(H21:J24)-SUM(H28:J31)` |
| `H25` | Total Earnings (Total Devengado) | `=CONCATENATE(TEXT(SUM(H21:J24),"#,##0")," ",G7)` |
| `H28` | XXXXX - Health Contribution - Employee (Salud - Empleado) | `=ROUND(SUM($H$21:$H$23)*0.04,0)` |
| `H29` | XXXXX - Pension Contribution - Employee (Pension - Empleado) | `=ROUND(SUM($H$21:$H$23)*0.04,0)` |
| `H30` | XXXXX - Solidarity Pension Fund FSP (Fondo de Solidaridad Pensional) | `=ROUND(SUM($H$21:$H$23)*0.01,0)` |
| `H32` | Total Deductions (Total Deducciones) | `=CONCATENATE(TEXT(SUM(H28:J31),"#,##0")," ",G7)` |
| `H34` | Net Pay (Neto a Pagar): | `=CONCATENATE(TEXT(SUM(I8),"#,##0")," ",G7)` |
| `H38` | XXXXX - Health Contribution - Employer (Salud - Empleador) | `=ROUND(SUM($H$21:$H$23)*0.085,0)` |
| `H39` | XXXXX - Pension Contribution - Employer (Pension - Empleador) | `=ROUND(SUM($H$21:$H$23)*0.12,0)` |
| `H40` | XXXXX - Occupational Risk (Riesgos Laborales - ARL, Class I) | `=ROUND(SUM($H$21:$H$23)*0.00522,0)` |
| `H41` | XXXXX - Family Compensation Fund (Caja de Compensacion Familiar) | `=ROUND(SUM($H$21:$H$23)*0.04,0)` |
| `H42` | XXXXX - SENA Training Levy (Aporte SENA) | `=ROUND(SUM($H$21:$H$23)*0.02,0)` |
| `H43` | XXXXX - ICBF Family Welfare (Aporte ICBF) | `=ROUND(SUM($H$21:$H$23)*0.03,0)` |
| `H44` | Total Employer Contributions (Total Aportes Empleador) | `=CONCATENATE(TEXT(SUM(H38:J43),"#,##0")," ",G7)` |
| `H48` | XXXXX - Severance (Cesantias) | `=ROUND(SUM($H$21:$H$24)*0.0833,0)` |
| `H49` | XXXXX - Interest on Severance (Intereses a las Cesantias) | `=ROUND(SUM($H$21:$H$24)*0.01,0)` |
| `H50` | XXXXX - Service Bonus (Prima de Servicios) | `=ROUND(SUM($H$21:$H$24)*0.0833,0)` |
| `H51` | XXXXX - Paid Leave Accrual (Provision de Vacaciones) | `=ROUND(SUM($H$21:$H$23)*0.0417,0)` |
| `H52` | Total Provisions (Total Provisiones) | `=CONCATENATE(TEXT(SUM(H48:J51),"#,##0")," ",G7)` |
| `H59` | Contribution Base / IBC (Base de Cotizacion) | `=SUM(H21:H23)` |
| `H60` | Total Employee Contributions (Salud + Pension + FSP) | `=SUM(H28:H30)` |
| `H61` | Total Employer Contributions & Parafiscales | `=SUM(H38:H43)` |
| `H62` | Total Social Benefit Provisions (Prestaciones) | `=SUM(H48:H51)` |
| `H63` | Total Employer Cost (Contributions + Provisions) | `=SUM(H38:H43)+SUM(H48:H51)` |

### Re-derivation (independently verified by the stage-07 QA cross-check - exact)

| Line | Basis | Value (COP) |
|---|---|---|
| Basic salary (`H21`) | contractual | 18,000,000 |
| Overtime & surcharges (`H22`) | worked example | 500,000 |
| Commissions & bonuses (`H23`) | worked example | 700,000 |
| Transport allowance (`H24`) | nil - salary is far above 2 SMMLV | 0 |
| **Total earnings** | 18,000,000 + 500,000 + 700,000 + 0 | **19,200,000** |
| IBC (contribution base, `H59`) | `SUM(H21:H23)` - excludes the auxilio de transporte | 19,200,000 |
| Health - employee 4% (`H28`) | IBC 19,200,000, below the 25-SMMLV cap of 43,772,625 | 768,000 |
| Pension - employee 4% (`H29`) | idem | 768,000 |
| FSP 1% (`H30`) | IBC is above the 4-SMMLV trigger of 7,003,620 | 192,000 |
| **Retencion en la fuente** (`H31`) | see the depuration below | **2,250,765** |
| Total deductions | 768,000 + 768,000 + 192,000 + 2,250,765 | 3,978,765 |
| **Net pay** (`I8` -> `H34`) | `SUM(H21:J24) - SUM(H28:J31)` | **15,221,235** |

**Withholding depuration, ET arts. 383 / 388 (re-derived to the peso):**

```
gross                                    19,200,000
- employee contributions (4+4+1%)         1,728,000   ET arts. 55, 56 (non-taxable income)
= subtotal                               17,472,000
- 25% exempt income, capped 790 UVT/yr    3,447,955   ET art. 206 num. 10; 790 UVT / 12 = 65.8333 UVT
= taxable base                           14,024,045   = 267.76732 UVT  (UVT 2026 = 52,374)
ET art. 383 band 150-360 UVT:  0.28 x (267.76732 - 150) + 10 = 42.97485 UVT
42.97485 UVT x 52,374                   = 2,250,765   <- the exact figure on the payslip
```

The **40% / 1,340-UVT** caps of ET art. 388 were tested and are **not binding** on this example.

**Employer block (`H38:H43`)** - Salud 8.5% - Pension 12% - ARL 0.522% (risk class I) - CCF 4% - SENA 2% -
ICBF 3%, all on `SUM(H21:H23)`.

**Provisions (`H48:H51`)** - Cesantias 8.33% - Intereses a las cesantias 1% - Prima de servicios 8.33% -
Provision de vacaciones 4.17% = **21.83%** total (agreeing with the WTC's 21.8333%).

**The base split is deliberate and correct:** the **cesantias, intereses and prima** provisions run on
`SUM($H$21:$H$24)` and therefore **include the auxilio de transporte** (CST art. 253 / Ley 15 de 1959 art. 7),
while the **vacation** provision runs on `SUM($H$21:$H$23)` and **excludes** it (CST art. 192). This is the
counter-intuitive Colombian distinction and the generator implements it rather than glossing it.

> **[QA MINOR-05]** `H51` (vacation provision) includes row 22, which bundles *Overtime & Surcharges*. Per
> CST art. 192 - and per WTC column X, which sets `CO-HED` / `CO-HEN` / `CO-RECARGO-DOMINICAL` to vacation base
> **No** while `CO-RECARGO-NOCTURNO` is **Yes** - overtime and rest-day work must be **excluded** from the
> vacation base while the night premium is **included**. The bundled demo line makes the two inseparable.
> **Fix:** split row 22 into an overtime line (excluded from `H51`) and a premium line (included).

**Year-to-date block (7 months):** gross 134,400,000 - employee contributions 12,096,000 - income tax
15,755,355 - net **106,548,645**. YTD net / 7 = 15,221,235, exactly the monthly net, so the YTD and monthly
blocks are mutually consistent.

> **[QA MINOR-06]** The `Colombia (EN)` / `(ES)` sheets use only the grey family (`FFDCDCDC`, `FFA9A9A9`,
> `FFF5F5F5`). This **matches `shared/REFERENCE_Payslip_Spain.xlsx` exactly**, which itself has no navy and no
> green - so the build faithfully mirrors the reference. The v2.4 check nonetheless calls for a navy/grey
> palette with a green net-pay highlight (`FF1F4E78` navy on the section header rows 19, 27, 36, 46, 54, 58,
> 65, 71; `FFC6EFCE` green on `A34:H34`). Cosmetic; should be raised against the shared Spain reference rather
> than fixed only in Colombia.

---

---

# 4. Sheet `Payslip Spec` - field list, local labels and HRB mapping (verbatim)


## 4.1 Full spec table


Header Details


| Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) |
|---|---|---|---|
| Payslip Title | Titulo de la Nomina | Static text "Colombia Payslip (Desprendible de Pago)" | Display title at top. Identifies Colombia and document type. |
| Company Logo | Logo de la Empresa | Static Mercans corporate logo | Mercans corporate logo in top banner. |
| Net Pay Summary Label | Etiqueta Neto a Pagar | column calculated value "Net Pay" | Label for net pay summary shown top-right. |


Employer Fields


| Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) | Query to RA |
|---|---|---|---|---|
| Employer Legal Name | Razon Social del Empleador | $legal_entity_hr.company_legal_name | Employer legal name (razon social). |  |
| Employer Address | Domicilio del Empleador | CONCAT($legal_entity_hr.company_street_name;' ';$legal_entity_hr.company_address_number;' ';$legal_entity_hr.company_town_city;' ';$legal_entity_hr.company_department) | Full registered address in Colombia. |  |
| Employer NIT | NIT del Empleador | $legal_entity_hr.company_tax_id | Employer tax ID (NIT) issued by DIAN within the RUT. Format XXX.XXX.XXX-DV. |  |
| ARL Risk Class | Clase de Riesgo ARL | $legal_entity_hr.arl_risk_class | Occupational-risk class (I-V) by CIIU code; drives the employer ARL rate. |  |
| Pay Period | Periodo Liquidado | CONCAT(DATE_FORMAT($period.begin_date;'dd-MM-yyyy');' - ';DATE_FORMAT($period.end_date;'dd-MM-yyyy')) | Remuneration period (from/to). |  |
| Pay Date | Fecha de Pago | $entry.payroll_payment_date | Date salary is credited to the employee bank account. |  |


Employee Fields


| Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) | Query to RA |
|---|---|---|---|---|
| Employee Full Name | Nombre Completo del Trabajador | CONCAT($person.first_name;' ';$person.middle_name;' ';$person.last_name) | Full name as in HR master data. |  |
| Employee Code | Codigo del Empleado | $employee.reference_code | Internal payroll reference code. |  |
| Job Title | Cargo | $employee.position | Job title / position. |  |
| Employee Department | Departamento / Centro de Costo | $employee.department | Department or cost centre. |  |
| Employee Hire Date | Fecha de Ingreso | $employee.hire_date | Date of employment commencement. |  |
| Employee Last Working Date | Fecha de Retiro | $employee.last_working_date | Populated on termination only. |  |
| Completed Years in Service | Anos Completos de Servicio | FLOOR(YEARS_BETWEEN($employee.hire_date;$period.end_date)) | Complete years from hire date; drives prima/cesantias/vacaciones accruals. |  |
| ID Document (C.C./C.E.) | Documento de Identidad (C.C./C.E.) | CONCAT($person.national_id_type;' ';$person.national_id) | Cedula de Ciudadania (C.C.) for nationals or Cedula de Extranjeria (C.E.) for foreigners. |  |
| Days in Month | Dias del Periodo | $entry.paid_days | Actual paid days in the period (Colombia commonly bases the month on 30 days). |  |
| EPS / AFP Affiliation | Afiliacion EPS / AFP | CONCAT($hr.eps_name;' / ';$hr.pension_fund_name) | Health provider (EPS) and pension fund (AFP) the employee is affiliated to. |  |
| Contract Type | Tipo de Contrato | $employee.contract_type::orLabel | Termino indefinido / termino fijo / obra o labor / salario integral. |  |


Earning


| Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) | Query to RA |
|---|---|---|---|---|
| Earning Wage Account | Concepto de Devengo | Formula:<br>CONCAT($entry.account;' - ';$entry.account_name)<br><br>Series: (62100:62999)<br>Series: (65500:65899)<br>Series: (79401:79499)<br>[VERIFY WITH RA - align to actual CO-WTC account codes once available] | All earning codes (devengados). Shows code, description and amount. |  |
| Unit | Unidad | Show the unit account code for the respective earning wage code per the UnitRate Account Details worksheet.<br>[VERIFY WITH RA - align to actual CO-WTC account codes once available] | Unit column for earnings (hours, days). |  |
| Rate | Tarifa | Show the rate account code for the respective earning wage code per the UnitRate Account Details worksheet.<br>[VERIFY WITH RA - align to actual CO-WTC account codes once available] | Unit price of the earning; only for unit-based concepts (e.g. hourly overtime). Blank for fixed monthly Salario Basico. |  |
| Amount | Valor | Show the amount for each earning account wage code. | Monetary value of each earning line in COP. |  |
| Total Earnings | Total Devengado | Show the summed value of all earnings. | Sum of all earning lines (gross). Basis (minus auxilio de transporte) for the IBC. |  |


Deductions & Net Field


| Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) | Query to RA |
|---|---|---|---|---|
| Deduction Wage Account | Concepto de Deduccion | Formula:<br>CONCAT($entry.account;' - ';$entry.account_name)<br><br>Series: (21100:21999)<br>Series: (25500:25899)<br>[VERIFY WITH RA - align to actual CO-WTC account codes once available] | All employee deduction codes: Salud 4%, Pension 4%, FSP, Retencion en la fuente. |  |
| Unit | Unidad (Base) | Show the contribution base (IBC) account for each social-security deduction.<br>[VERIFY WITH RA - align to actual CO-WTC account codes once available] | For SS deductions the unit is the IBC (Ingreso Base de Cotizacion). |  |
| Percentage | Tarifa / Porcentaje | Show the employee percentage: Salud 4%, Pension 4%, FSP 1% (>=4 SMMLV). Leave blank for Retencion en la fuente (progressive).<br>[VERIFY WITH RA - align to actual CO-WTC account codes once available] | Rate column. Fixed-rate lines show the %; progressive lines (retencion, FSP tiers) leave blank and show amount only. |  |
| Deduction Amount | Valor Deduccion | Show the amount for each deduction account wage code. | Monetary amount per deduction in COP. |  |
| Total Deductions | Total Deducciones | Show the summed value of all deductions. | Sum of all employee deductions. |  |


Net Pay


| Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) |
|---|---|---|---|
| Net Pay | Neto a Pagar | Total Devengado - Total Deducciones | Final net pay credited to the employee. |


Employer Contribution


| Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) | Query to RA |
|---|---|---|---|---|
| Employer Contribution Account | Concepto Aporte Empleador | Formula:<br>CONCAT($entry.account;' - ';$entry.account_name)<br><br>Series: (23550:23900)<br>[VERIFY WITH RA - align to actual CO-WTC account codes once available] | Employer contributions: Salud 8.5%, Pension 12%, ARL, Caja 4%, SENA 2%, ICBF 3%. |  |
| Unit | Unidad (Base) | Show the IBC (contribution base) account for each employer contribution.<br>[VERIFY WITH RA - align to actual CO-WTC account codes once available] | Unit for employer contributions = IBC. |  |
| Percentage | Tarifa Aporte Empleador | Show the employer percentage: Salud 8.5%, Pension 12%, ARL 0.522%-6.960% (by class), Caja 4%, SENA 2%, ICBF 3%.<br>[VERIFY WITH RA - align to actual CO-WTC account codes once available] | Rate column. Note Art. 114-1 ET exoneration (Salud-ER/SENA/ICBF) for employees under 10 SMMLV. |  |
| Employer Contribution Amount | Valor Aporte Empleador | Show the amount for each employer contribution account. | Monetary amount per employer contribution in COP. |  |
| Total Employer Contributions | Total Aportes Empleador | Show the summed value of all employer contributions. | Sum of employer SS + parafiscales. Informational. |  |
| Social Benefit Provisions | Prestaciones Sociales (Provisiones) | Formula:<br>CONCAT($entry.account;' - ';$entry.account_name)<br><br>Series: (26100:26999)<br>[VERIFY WITH RA - align to actual CO-WTC account codes once available] | Employer accruals: Cesantias 8.33%, Intereses 1%, Prima 8.33%, Vacaciones 4.17%. |  |


Banking Details


| Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) | Query to RA |
|---|---|---|---|---|
| Beneficiary Name | Nombre del Titular | $primary_employee_bank_account.beneficiary_name | Account holder name matching the employee legal name. |  |
| Account Number | Numero de Cuenta | CONCAT($primary_employee_bank_account.account_type;' ';$primary_employee_bank_account.account_number) | Colombian bank account: type (ahorros/corriente) + account number (10-11 digits). |  |
| Bank | Banco | $primary_employee_bank_account.bank_name | Name of the Colombian bank. |  |
| Banking Currency | Moneda | $primary_employee_bank_account.account_currency | COP - Colombian Peso. |  |


Footer Details


| Field Name | Field Local Name | HRB Mapping | Field Explanation (RA) |
|---|---|---|---|
| Generated By Note | Nota de Generacion | This document has been generated by Mercans | System note: This document has been generated by Mercans. |
| Reference Code | Codigo de Referencia | REF-CO-2026 | Document reference code. |
| Copyright Note | Nota de Derechos Reservados | All rights reserved | Copyright footer: All rights reserved. |


---

# 5. Statutory notes printed on the payslip (verbatim, both languages)

## 5.1 `Colombia (EN)` - Statutory Notes - Fiscal Year 2026

```
Statutory Notes - Fiscal Year 2026

* Payslip disclosure: Colombia's Codigo Sustantivo del Trabajo (CST) has no single formatted-payslip article; the binding duty to disclose social-security contributions paid on the worker's behalf is Ley 1393 de 2010, Art. 32. The desprendible de nomina must itemise devengados, deducciones and neto for each pay period. DIAN Nomina Electronica (Resolucion 000013 de 2021) requires a structured monthly payroll support document, transmitted within the first 10 days of the following month.

* Social Security (Ley 100 de 1993): Health/Salud 12.5% (employee 4% + employer 8.5%); Pension 16% (employee 4% + employer 12%). Contribution base (IBC) floor 1 SMMLV, ceiling 25 SMMLV (2026 = COP 43,772,625). FSP (Art. 27 Ley 100, mod. Art. 8 Ley 797 de 2003): employee-only surcharge 1% for IBC >= 4 SMMLV, rising 1.2%-2.0% above 16 SMMLV. Auxilio de transporte is excluded from the IBC.

* Occupational Risk / ARL (Decreto-Ley 1295 de 1994; Decreto 1607 de 2002): employer-only, five risk classes by CIIU activity code - I 0.522%, II 1.044%, III 2.436%, IV 4.350%, V 6.960%. Nothing is deducted from the employee.

* Parafiscales (employer): SENA 2%, ICBF 3%, Caja de Compensacion Familiar 4%. Exoneration under Art. 114-1 Estatuto Tributario (originated Ley 1607 de 2012): income-tax-paying employers are exonerated from SENA, ICBF and the 8.5% employer health contribution for each employee earning under 10 SMMLV; the 4% Caja de Compensacion, pension and ARL are never exonerated.

* Income Tax Withholding / Retencion en la fuente (Arts. 383, 388, 206 & 336 Estatuto Tributario; UVT 2026 = COP 52,374 per DIAN Resolucion 000238 de 2025): progressive marginal table 0/19/28/33/35/37/39%, starting above 95 UVT (approx. COP 4,975,530/month). Depuration allows 25% exempt income capped at 790 UVT/year (Art. 206 num. 10, mod. Ley 2277 de 2022) subject to a 40% global cap of deductions/exemptions, max 1,340 UVT/year (Art. 336).

* Minimum wage SMMLV 2026 = COP 1,750,905/month (Decreto 1469 de 2025, reinstated by Consejo de Estado auto of 9-Jul-2026 after provisional suspension). Auxilio de transporte 2026 = COP 249,095/month (Decreto 1470 de 2025), payable to workers earning up to 2 SMMLV (Ley 15 de 1959); excluded from the IBC but included in the base for prima and cesantias.

* Leave: annual leave 15 working days/year (CST Art. 186); sick leave (enfermedad general) - employer pays days 1-2, EPS pays from day 3 at 66.67% for the first 90 days then 50% for days 91-180 (Decreto 780 de 2016 Art. 3.2.1.10; CST Art. 227); maternity 18 weeks funded by EPS (CST Art. 236, Ley 1822 de 2017); paternity 2 weeks (CST Art. 236A, Ley 2114 de 2021).

* Prestaciones sociales (employer): prima de servicios one month's salary/year (CST Art. 306, paid half by 30 Jun and half by 20 Dec); cesantias one month's salary/year deposited to the fund by 14 Feb (CST Art. 249); intereses a las cesantias 12%/year paid to the employee by 31 Jan (Ley 52 de 1975). Identifiers: employer NIT within the RUT (DIAN, Art. 555-1 ET); employee documento de identidad - Cedula de Ciudadania (C.C.) or Cedula de Extranjeria (C.E.). Currency COP (ISO 4217). Sources: Estatuto Tributario | CST | Ley 100 de 1993 | DIAN | Ministerio del Trabajo | Mercans CO-2026.

This document has been generated by Mercans

This document has been generated by Mercans

REF-CO-2026

```

## 5.2 `Colombia (ES)` - Notas Legales - Ejercicio Fiscal 2026

```
Notas Legales - Ejercicio Fiscal 2026

* Divulgacion de nomina: el Codigo Sustantivo del Trabajo (CST) no contiene un articulo unico que exija un formato de nomina; la obligacion vinculante de informar al trabajador los aportes a seguridad social pagados a su nombre esta en la Ley 1393 de 2010, Art. 32. El desprendible de nomina debe detallar devengados, deducciones y neto en cada periodo de pago. La Nomina Electronica de la DIAN (Resolucion 000013 de 2021) exige un documento soporte de pago de nomina mensual y estructurado, transmitido dentro de los primeros 10 dias del mes siguiente.

* Seguridad Social (Ley 100 de 1993): Salud 12,5% (trabajador 4% + empleador 8,5%); Pension 16% (trabajador 4% + empleador 12%). Base de cotizacion (IBC) con piso de 1 SMMLV y tope de 25 SMMLV (2026 = COP 43.772.625). FSP (Art. 27 Ley 100, mod. Art. 8 Ley 797 de 2003): aporte adicional solo del trabajador, 1% para IBC >= 4 SMMLV, aumentando de 1,2% a 2,0% por encima de 16 SMMLV. El auxilio de transporte se excluye del IBC.

* Riesgos Laborales / ARL (Decreto-Ley 1295 de 1994; Decreto 1607 de 2002): a cargo exclusivo del empleador, cinco clases de riesgo segun el codigo CIIU de la actividad - I 0,522%, II 1,044%, III 2,436%, IV 4,350%, V 6,960%. No se deduce nada al trabajador.

* Parafiscales (empleador): SENA 2%, ICBF 3%, Caja de Compensacion Familiar 4%. Exoneracion del Art. 114-1 del Estatuto Tributario (origen Ley 1607 de 2012): los empleadores contribuyentes del impuesto de renta estan exonerados de SENA, ICBF y del aporte patronal de salud del 8,5% por cada trabajador que devengue menos de 10 SMMLV; la Caja de Compensacion del 4%, la pension y la ARL nunca se exoneran.

* Retencion en la fuente (Arts. 383, 388, 206 y 336 del Estatuto Tributario; UVT 2026 = COP 52.374 segun Resolucion DIAN 000238 de 2025): tabla marginal progresiva 0/19/28/33/35/37/39%, que inicia por encima de 95 UVT (aprox. COP 4.975.530/mes). La depuracion permite una renta exenta del 25% limitada a 790 UVT/ano (Art. 206 num. 10, mod. Ley 2277 de 2022), sujeta al limite global del 40% de deducciones y rentas exentas, maximo 1.340 UVT/ano (Art. 336).

* Salario minimo SMMLV 2026 = COP 1.750.905/mes (Decreto 1469 de 2025, reinstaurado por auto del Consejo de Estado del 9-jul-2026 tras suspension provisional). Auxilio de transporte 2026 = COP 249.095/mes (Decreto 1470 de 2025), pagadero a quienes devenguen hasta 2 SMMLV (Ley 15 de 1959); se excluye del IBC pero se incluye en la base de prima y cesantias.

* Licencias: vacaciones 15 dias habiles/ano (CST Art. 186); incapacidad por enfermedad general - el empleador paga los dias 1-2 y la EPS desde el dia 3 al 66,67% durante los primeros 90 dias y al 50% entre los dias 91-180 (Decreto 780 de 2016 Art. 3.2.1.10; CST Art. 227); licencia de maternidad 18 semanas a cargo de la EPS (CST Art. 236, Ley 1822 de 2017); licencia de paternidad 2 semanas (CST Art. 236A, Ley 2114 de 2021).

* Prestaciones sociales (empleador): prima de servicios un salario mensual/ano (CST Art. 306, mitad antes del 30 jun y mitad antes del 20 dic); cesantias un salario mensual/ano consignado al fondo antes del 14 feb (CST Art. 249); intereses a las cesantias 12%/ano pagados al trabajador antes del 31 ene (Ley 52 de 1975). Identificadores: NIT del empleador dentro del RUT (DIAN, Art. 555-1 ET); documento de identidad del trabajador - Cedula de Ciudadania (C.C.) o Cedula de Extranjeria (C.E.). Moneda COP (ISO 4217). Fuentes: Estatuto Tributario | CST | Ley 100 de 1993 | DIAN | Ministerio del Trabajo | Mercans CO-2026.

Este documento ha sido generado por Mercans

Este documento ha sido generado por Mercans

REF-CO-2026

```

---

# 6. Remaining sheets


## 6.1 Sheet `Field Option`


| Field Name | Option Value | Option Description | Usage Context |
|---|---|---|---|
| CURRENCY | COP | Colombian Peso | Displayed currency in payslip summary and banking section |


## 6.2 Sheet `Population Range`


| Worker Situation | Include? (YES/NO) | Notes |
|---|---|---|
| Active employees (full-time) | YES | Generate desprendible de pago for all active full-time employees on termino indefinido or termino fijo contracts. Full salary, social security and prestaciones sociales apply. |
| Active employees (part-time / part-period) | YES | Same layout with actual worked time. IBC and contributions computed on actual salary (floor 1 SMMLV per full-time equivalent). Prestaciones prorated. |
| New hires during period | YES | Prorate salary, social security and prestaciones to days worked from the hire date. Auxilio de transporte prorated where applicable (salary up to 2 SMMLV). |
| Terminations during period | YES | Populate Fecha de Retiro. Include liquidacion definitiva: cesantias + intereses, vacaciones acumuladas, prima proporcional, and indemnizacion por despido sin justa causa if applicable (CST Art. 64). |
| Sick leave - enfermedad general | YES | Employer pays days 1-2; EPS pays from day 3 at 66.67% of IBC for the first 90 days, then 50% for days 91-180 (Decreto 780 de 2016; CST Art. 227). Show the incapacidad as an income line. |
| Maternity / paternity leave | YES | Maternity 18 weeks and paternity 2 weeks, funded by the EPS at 100% of IBC (CST Arts. 236 & 236A; Ley 1822 de 2017; Ley 2114 de 2021). Show EPS benefit as an income line where the employer advances it. |
| Unpaid leave (licencia no remunerada) | CONDITIONAL | Generate a record when payroll issues one. Salary suspended; social-security contributions are generally suspended by agreement, but the affiliation must be handled per EPS/AFP rules. |
| Salario integral employees | YES | Colombia-specific: salary >= 13 SMMLV agreed as integral. IBC = 70% of the integral salary (factor prestacional 30%). No separate prima/cesantias/prima lines (already included). |
| Apprentices (contrato de aprendizaje - SENA) | CONDITIONAL | Colombia-specific: apprentices receive an apoyo de sostenimiento (not salary), affiliated to health and ARL only, no pension/parafiscales. Include only if payroll processes the apoyo. |
| Foreign workers (Cedula de Extranjeria) | YES | Same template. Identify with C.E. Same social security and retencion en la fuente as nationals unless covered by a bilateral totalization agreement for pension. |
| Board members / directors | CONDITIONAL | Include if bound by an employment contract (subordination). Statutory representatives with an employment relationship: standard nomina. Pure honorarios (fees) are billed separately. |
| Contractors / self-employed (prestacion de servicios) | NO | Do not include. Independent contractors invoice via cuenta de cobro / factura and pay their own social security on 40% of income. Verify contribution before payment; not part of nomina. |


## 6.3 Sheet `Unit Rate Details` - earning / rate / unit account codes

> **[VERIFY WITH RA]** The sheet itself is headed *"illustrative placeholder account codes; align to actual CO-WTC once available"*. These 5-digit numbers are **not** the WTC codes and must be reconciled to the WTC (or to the Mercans numeric range once assigned for Colombia) at configuration time.


|  | Earning | Rate | Unit | [VERIFY WITH RA - illustrative placeholder account codes; align to actual CO-WTC once available] |
|---|---|---|---|---|
| Basic Salary (Salario Basico) | 62100 | 62104 | 63100 |  |
| Salary Advance (Anticipo de Salario) | 62103 |  | 63103 |  |
| Overtime - Daytime (Hora Extra Diurna 25%) | 62110 | 62105 | 63110 |  |
| Overtime - Night (Hora Extra Nocturna 75%) | 62111 | 62106 | 63111 |  |
| Night Surcharge (Recargo Nocturno 35%) | 62120 | 62107 | 63120 |  |
| Sunday/Holiday Surcharge (Recargo Dominical y Festivo 75%) | 62121 | 62108 | 63121 |  |
| Sunday/Holiday Overtime (Hora Extra Dominical/Festiva 100%) | 62122 | 62109 | 63122 |  |
| Commission (Comisiones) | 62200 |  | 63200 |  |
| Bonus - salary (Bonificacion Constitutiva de Salario) | 62210 |  | 63210 |  |
| Bonus - non-salary (Bonificacion No Constitutiva) | 62211 |  | 63211 |  |
| Transport Allowance (Auxilio de Transporte) | 62300 |  | 63300 |  |
| Connectivity Allowance (Auxilio de Conectividad) | 62301 |  | 63301 |  |
| Food Allowance (Auxilio de Alimentacion) | 62302 |  | 63302 |  |
| Per-diem / Subsistence (Viaticos) | 62310 |  | 63310 |  |
| Service Bonus (Prima de Servicios) | 65500 |  | 75500 |  |
| Severance (Cesantias) | 65510 |  | 75510 |  |
| Interest on Severance (Intereses a las Cesantias) | 65511 |  | 75511 |  |
| Annual Leave Pay (Vacaciones) | 65520 | 65521 | 75520 |  |
| Annual Leave Cash-out (Vacaciones Compensadas) | 65522 |  | 75522 |  |
| Sick Leave - general illness (Incapacidad Enfermedad General) | 79408 |  | 79008 |  |
| Work-injury Leave (Incapacidad de Origen Laboral - ARL) | 79409 |  | 79009 |  |
| Maternity Leave (Licencia de Maternidad) | 79406 |  | 79006 |  |
| Paternity Leave (Licencia de Paternidad) | 79407 |  | 79007 |  |
| Paid Statutory Leave (Licencia Remunerada) | 79420 |  | 79020 |  |
| Unpaid Leave (Licencia No Remunerada) | 79435 |  | 79035 |  |
| Public Holiday Pay (Dia Festivo) | 79411 |  | 79011 |  |
| Severance Indemnity (Indemnizacion por Despido - CST Art. 64) | 65650 |  | 75650 |  |
| Integral Salary (Salario Integral) | 62150 |  | 63150 |  |


## 6.4 Sheet `Compliance Payslip` (the Mercans reference template, unmodified)


Example Payslip

Net Pay:


| Employer Name | Mercans Estonia |  |  |
|---|---|---|---|
| Employer Address | Väike-Tähe 20, Tartu, Tartumaa, 51010 |  | MZN |
| Country | MZN |  |  |
| Period | 01/10/2023 - 31/10/2023 |  |  |
| Employee name | John Doe | Email | jdoe@mercan.com |
| Employee ID | EID-1337 | Hire date | 01/10/2019 |
| Employee Position | Operational Support | Payment Method | Bank |
| Basic Salary (EUR) | 2000 | Custom Field | XXXXX |
| Daily (EUR) | 100 | Custom Field | XXXXX |
| Hourly (EUR) | 12.5 | Custom Field | XXXXX |


Details


| Earnings | Rate | Unit | Amount |
|---|---|---|---|
| XXXXX - Earning Pay Element |  |  | 3210 |
| XXXXX - Earning Pay Element |  |  | 200 |
| XXXXX - Earning Pay Element |  |  | 10 |


Total Gross


| Deductions | Rate | Unit | Amount |
|---|---|---|---|
| XXXXX - Deduction Pay Element |  |  | 800 |
| XXXXX - Deduction Pay Element |  |  | 100 |


Total Deductions

Net Pay:


| Employer Contributions | Amount |
|---|---|
| XXXXX - Employer Contribution Pay Element | 400 |


Total Employer Contributions

Banking details


| Bank name | SWIFT | Beneficiary name | Acc. Number | Account currency | Type |
|---|---|---|---|---|---|
| Swed Bank AS | SW121212 | Jhon Doe | EE121212121212 | EUR | Primary |


This document has been generated by Mercans


| REF-P26-663 | © All rights reserved |
|---|---|


## 6.5 Sheet `How to set up Payslip` (template instructions, unmodified)


Create new sheet for your country, copy the payslip from  "Compliance Payslip" sheet and then make changes
Example Payslip
When creating report make sure to use the Normal margins
Page Layout -> Margins -> Normal   this will show if the content will fit on your page or not

Net Pay:


| This section contains employer-related information. To add an extra row, simply select Row 10, right-click, and choose ‘Insert Row’ from the menu. | Employer <br>Details | Employer Name | Mercans Estonia |  |  |  |
|---|---|---|---|---|---|---|
|  |  | Employer Address | Väike-Tähe 20, Tartu, Tartumaa, 51010 | EUR | 1,350.00 | 1. Finalize Your Worksheet: |
|  |  | Country | Estonia |  |  | • Ensure all desired changes are made to your worksheet. |
|  |  | Period | 01/10/2023 - 31/10/2023 |  |  | 2. Access the ‘Save As’ Function: |


• Click on the File tab in the top-left corner.


| This section contains employee-related information. If a field is not applicable, you can either remove it or replace it with one relevant to the country. Additionally, you have the option to delete or add extra rows as needed. | Employee<br>Details | Employee name | John Doe | Email | jdoe@mercan.com | • Select Save As from the menu. |
|---|---|---|---|---|---|---|
|  |  | Employee ID | EID-1337 | Hire date | 01/10/2019 | 3. Choose PDF as the File Format: |
|  |  | Employee Position | Operational Support | Payment Method | Bank | • In the ‘Save As’ dialog box, click the dropdown menu labeled File format. |


• Select PDF (*.pdf) from the list of file formats.


| This section is for countries that require additional details on the payslip. If not needed, you can simply delete it.” | Extra Information | Basic Salary (EUR) | 2,000.00 | Custom Field | XXXXX | 4. Specify the Content to Export: |
|---|---|---|---|---|---|---|
|  |  | Daily (EUR) | 100.00 | Custom Field | XXXXX | • Click on the Sheet option |
|  |  | Hourly (EUR) | 12.50 | Custom Field | XXXXX | • Ensure the Option is set to Best for Printing |


5. Save the PDF:


| Here, you can add or remove wage types by inserting or deleting rows. If the provided columns are not applicable to the country, rename or merge them with other fields.<br>Don't delete the columns otherwise it messes up the design. | Details | Details |  |  |  |  |  |  |  | • Choose your desired file location and name. |
|---|---|---|---|---|---|---|---|---|---|---|
|  |  | Earnings |  |  | Unit | Amount |  | Year-to-date |  | • Click Save to generate the PDF. |
|  |  | XXXXX - Earning Pay Element |  |  |  | 2,000.00 |  | 20,000.00 |  |  |
|  |  | XXXXX - Earning Pay Element |  |  | 5 (Hrs) | 200.00 |  | 2,000.00 |  |  |
|  |  | XXXXX - Earning Pay Element |  |  |  | 10.00 |  | 100.00 |  |  |
|  |  | Total Gross |  |  |  | 2,250.00 |  | EUR |  |  |
| Here, you can add or remove wage types by inserting or deleting rows. If the provided columns are not applicable to the country, rename or merge them with other fields.<br>Don't delete the columns otherwise it messes up the design. | Details | Deductions |  |  | Unit | Amount |  | Year-to-date |  |  |
|  |  | XXXXX - Deduction Pay Element |  |  |  | 800.00 |  | 8,000.00 |  |  |
|  |  | XXXXX - Deduction Pay Element |  |  |  | 100.00 |  | 1,000.00 |  |  |
|  |  | Total Deductions |  |  |  | 900.00 |  | EUR |  |  |
|  |  |  |  |  |  | Net Pay: |  | 1,350.00 |  |  |
| Here, you can add Bank info by inserting row if there is also Secoundary bank account. If the provided columns are not applicable to the country, rename or merge them with other fields.<br>Don't delete the columns otherwise it messes up the design. | Details | Employer Contributions |  |  |  | Amount |  | Year-to-date |  |  |
|  |  | XXXXX - Employer Contribution Pay Element |  |  |  | 400.00 |  | 4,000.00 |  |  |
|  |  | Total Employer Contributions |  |  |  | 400.00 |  | EUR |  |  |
| Here, you can add Bank info by inserting row if there is also Secoundary bank account. If the provided columns are not applicable to the country, rename or merge them with other fields.<br>Don't delete the columns otherwise it messes up the design. | Bank Info | Banking details |  |  |  |  |  |  |  |  |
|  |  | Bank name | SWIFT | Beneficiary name |  | Acc. Number | Account currency |  | Type |  |
|  |  | Swed Bank AS | SW121212 | Jhon Doe |  | EE121212121212 | EUR |  | Primary |  |
| This is a filler section designed to ensure the template fills the entire page and the footer remains in the correct position. If you add or delete rows in other sections, make sure to adjust this filler section by adding or removing the same number of rows. For example, if you add two rows in the ‘Earnings’ section, you should delete two rows from the ‘Filler’ section. | Filler |  |  |  |  |  |  |  |  |  |


This document has been generated by Mercans


| REF-P26-663 | © All rights reserved |
|---|---|


---

# 7. Payslip readiness summary

| Item | Status |
|---|---|
| 8-sheet Mercans standard, reference order | PASS |
| Grey palette matched to `REFERENCE_Payslip_Spain.xlsx` | PASS (navy/green absent - MINOR-06) |
| Spanish sheet fully translated (Res. DIAN 000013 art. 26) | PASS - the only residual English tokens are Spanish-English cognates (*Pension*, *Base*, *Total*) |
| Arithmetic (gross, IBC, three employee contributions, withholding, net, YTD, employer block, provisions) | **PASS - re-derived exactly** |
| CST art. 192 vs art. 253 base distinction | PASS (implemented) |
| Wage-type codes wired to the WTC | **FAIL - `XXXXX` placeholders (MAJOR-01)** |
| Res. DIAN 000013 art. 5 header block, CUNE, QR | **FAIL - absent (MAJOR-02)** |
| Vacation base excludes bundled overtime | **PARTIAL (MINOR-05)** |
| `Unit Rate Details` account codes | **Placeholder - [VERIFY WITH RA]** |

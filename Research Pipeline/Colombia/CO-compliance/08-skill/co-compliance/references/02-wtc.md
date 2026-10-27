# Colombia - Wage Type Catalogue (WTC) - COMPLETE REFERENCE

**Source artifact:** `02-wtc/CO-WTC-001-v1.0.xlsx` (v1.0, 2026-09-04, Mercans Compliance Regulations Team)
**Structure:** 6 sheets - Wage Type Catalogue **402 rows x 28 columns** - **300 of 300** Global WTC baseline
codes included (0 excluded) + **102** Colombia-specific `CO-` codes.
**Currency:** COP - **Fiscal year:** 2026 - **SMMLV** 1,750,905 - **UVT** 52,374.

> **DERIVED flag (disclosed in the source artifact):** the Mercans code numbers for the 102 Colombia-specific
> rows are **DERIVED** - no Mercans numeric code range has been assigned for Colombia, so mnemonic `CO-` codes
> are used and **must be renumbered at system-configuration time**.

## Column legend (verbatim header text of the Wage Type Catalogue)

| Col | Header (verbatim) |
|---|---|
| A | Mercans Code |
| B | Wage Type Name in English |
| C | Wage Type Name in Local Language (Spanish) |
| D | Wage Type Explanation |
| E | Category |
| F | Formula |
| G | Tax Code |
| H | Calculation Type |
| I | Prorating Method |
| J | Occurrence |
| K | Ignore If 0 |
| L | Enforce Setting |
| M | In Period Reconciliation |
| N | Subject to Tax (Retencion en la Fuente) |
| O | Table Tax (ET art. 383 progressive table 0/19/28/33/35/37/39%) |
| P | Special Tax (Non-resident flat 20% on gross, ET art. 408) |
| Q | Subject to Health - Salud EPS (EE 4% + ER 8.5%; IBC, cap 25 SMMLV 43,772,625) |
| R | Subject to Solidarity Pension Fund - FSP (EE 1% + 0.2-1.0%; IBC >= 4 SMMLV 7,003,620) |
| S | Subject to Occupational Risk - ARL (ER only 0.348-8.7%; IBC) |
| T | Subject to Payroll Levies - CCF 4% / SENA 2% / ICBF 3% (Ley 21/1982 base, NO ceiling) |
| U | Subject to Pension - Pension Obligatoria (EE 4% + ER 12%; IBC, cap 25 SMMLV) |
| V | Salary or Non-Salary (CST arts. 127 / 128) - hard flag for the nomina electronica S / NS elements |
| W | Statutory-Benefit Base (prima de servicios / cesantias / intereses) |
| X | Vacation Base (CST art. 192 - excludes overtime and rest-day work only) |
| Y | Nomina Electronica Element (Res. DIAN 000013 de 2021, Anexo Tecnico v1.0) |
| Z | Tax Code Source (C9 - official reference) |
| AA | YTD Load (Yes/ No) |
| AB | YTD Remarks |

The **five social-insurance subjection columns Q-U** (instead of one) and the **three Colombia-specific base
columns V-X** are deliberate: Colombia has eight mandatory contributions across three insurance branches, three
payroll levies and one employee-only solidarity surcharge, and **they do not share a base**. See Sheet 5 -
Global WTC Coverage, items 7-9.

---

## Sheet 1 - Version Control

| Version | Effective Date | Change Description | Status | Updated By |
|---|---|---|---|---|
| 1 | 2026-09-04 00:00:00 | Initial Colombia Wage Type Catalogue for FY2026. All 300 global baseline codes configured fresh for Colombia (CST arts. 127/128 salary classification, the THREE separate bases, the Ley 1393/2010 40% clamp, the ET art. 114-1 exoneration cliff, the ET art. 388 depuration and the art. 383 table) plus 102 Colombia-specific wage types. Social-insurance column expanded into five per-fund columns (Salud / FSP / ARL / Parafiscales / Pension) and three Colombia-specific base columns added (salary flag / statutory-benefit base / vacation base). Includes the Global WTC Coverage sheet and the Form Reference Guide (C17); every tax code defined and sourced to a Colombian authority publication (C9). Wage-type code numbers for Colombia-specific rows are DERIVED (no Mercans code range has been assigned for Colombia). | Released | Mercans Compliance (build_co_wtc.py) |
| 2 | 2025-09-09 00:00:00 | Wage codes Mapping | Released | Devshree Vyas |
| Business Analyst |  |  |  |  |
| Regulation Analyst |  |  |  |  |

> **[QA MINOR-01]** Row 14 of the source Version Control sheet (`2.0 | 2025-09-09 | Wage codes Mapping |
> Released | Devshree Vyas`) is **un-cleaned CZ template residue**, confirmed identical to row 14 of
> `shared/_CZ_Wage_Type_Catalogue_V2_0.xlsx`. It makes the change log read as if v2.0 predates v1.0 by a year.
> Ignore it: the only genuine Colombia entry is **v1 of 2026-09-04**. Fix = delete the row, or replace it with
> the v1.1 DD-to-spec alignment-patch entry that the DD and all six report specs already carry.

---

## Sheet 2 - Wage Type Catalogue: subjection and configuration matrix (all 402 rows)

Columns A-C, E, G-Y, AA. The four long-text columns - **D** *Wage Type Explanation*, **F** *Formula*,
**Z** *Tax Code Source* and **AB** *YTD Remarks* - are reproduced in full, per code, in
"Sheet 2 (continued)" below.

Legend for the subjection columns: **N** Subject to Tax - **O** Table Tax (ET art. 383) - **P** Special Tax
(non-resident flat 20%, ET art. 408) - **Q** Salud EPS - **R** FSP (Fondo de Solidaridad Pensional) -
**S** ARL - **T** Parafiscales (CCF 4% / SENA 2% / ICBF 3%) - **U** Pension Obligatoria -
**V** Salary / Non-Salary (CST arts. 127 / 128) - **W** Statutory-Benefit Base - **X** Vacation Base (CST art. 192).

| Code | Name (EN) | Name (ES) | Category | Tax Code | Calc Type | Prorating | Occurrence | Ign0 | Enforce | InPerRec | N | O | P | Q | R | S | T | U | V | W | X | Nomina Electronica element | YTD Load |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 21100 | Basic salary deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21102 | Adjustment - Basic salary deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21103 | Advance - Basic salary deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21108 | Sick leave - Basic salary deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21109 | Unpaid LOA - Basic salary deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21110 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21111 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21112 | Adjustment - Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21113 | Advance - Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21114 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21115 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21116 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21117 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21118 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21119 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21120 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21121 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21122 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21123 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21124 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21125 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21127 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21140 | Salary addition deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21141 | Salary addition deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21142 | Salary addition deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21143 | Salary addition deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21144 | Salary addition deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21145 | Salary addition deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21146 | Salary addition deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21147 | Salary addition deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21148 | Salary addition deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21149 | Salary addition deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21150 | Premium pay (i.e. Shift premium) deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21151 | Premium pay (i.e. Shift premium) deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21152 | Premium pay (i.e. Shift premium) deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21190 | Long Term Disability deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Lump Sum |  | Additional | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / Reintegro (NIE184) | No |
| 21210 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21211 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21212 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21213 | Overtime deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21400 | Housing allowance deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21520 | Transportation allowance deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21610 | Health insurance & Life insurance contributions | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / Salud (NIE161, NIE163) | No |
| 21611 | Health insurance & Life insurance contributions | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / Salud (NIE161, NIE163) | No |
| 21640 | Pensions & Pension Contributions (pre-tax deduction) | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / FondoPension (NIE164, NIE166); PensionVoluntaria (NIE198); AFC (NIE179) | No |
| 21641 | Pensions & Pension Contributions (pre-tax deduction) | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / FondoPension (NIE164, NIE166); PensionVoluntaria (NIE198); AFC (NIE179) | No |
| 21642 | Pensions & Pension Contributions (pre-tax deduction) | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / FondoPension (NIE164, NIE166); PensionVoluntaria (NIE198); AFC (NIE179) | No |
| 21645 | Pensions & Pension Contributions (pre-tax deduction) | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / FondoPension (NIE164, NIE166); PensionVoluntaria (NIE198); AFC (NIE179) | No |
| 21670 | Benefits plan 1 deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / PlanComplementarios (NIE182) | No |
| 21800 | Expense reimbursement deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Lump Sum |  | Additional | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / Anticipos (NIE196) | No |
| 21810 | Parking deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21820 | Donation deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Lump Sum |  | Additional | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21890 | Stock options and grants deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Lump Sum |  | Additional | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| 21900 | Custom Social Security (employee) | (codigo global - ver la explicacion para el tratamiento colombiano) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / FondoSP (NIE167-NIE170) | No |
| 23640 | Pensions & Pension Contributions (employer, no-recon) | (codigo global - ver la explicacion para el tratamiento colombiano) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | PILA T2R2-046, T2R2-047, T2R2-050; not a nomina electronica element | No |
| 23670 | Benefits plan 1 deduction | (codigo global - ver la explicacion para el tratamiento colombiano) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Devengados / Auxilio (AuxilioNS, NIE142) for the employee-side value | No |
| 23671 | Company contribution liability | (codigo global - ver la explicacion para el tratamiento colombiano) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | PILA T2R2-046 to T2R2-073; not a nomina electronica element | No |
| 23672 | Company contribution liability | (codigo global - ver la explicacion para el tratamiento colombiano) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | PILA T2R2-046 to T2R2-073; not a nomina electronica element | No |
| 23673 | Company contribution liability | (codigo global - ver la explicacion para el tratamiento colombiano) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | PILA T2R2-046 to T2R2-073; not a nomina electronica element | No |
| 62100 | Basic salary | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070) | Yes |
| 62101 | Arrears - Basic salary | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070) | Yes |
| 62102 | Adjustment - Basic salary | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070) | Yes |
| 62103 | Advance - Basic salary | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070) | Yes |
| 62104 | Basic salary (rate) | (codigo global - ver la explicacion para el tratamiento colombiano) | Percentage | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Derived - feeds every hour-type Pago element | No |
| 62108 | Historic Pay | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070) | Yes |
| 62109 | Unpaid LOA - Basic salary | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070) | Yes |
| 62110 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62111 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62112 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62113 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62114 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62115 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62116 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62117 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62118 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62119 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62120 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62121 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62122 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62123 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62124 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62125 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62126 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62127 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62128 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62129 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62130 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62131 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62132 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62133 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62134 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62135 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62136 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62137 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62138 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62139 | Overtime | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) | Yes |
| 62140 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62141 | Arrears - Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62142 | Adjustment - Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62143 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62144 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62145 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62146 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62147 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62148 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62149 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62150 | Premium pay (i.e. Shift premium) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / HRN (NIE084-NIE088), HRDDF (NIE094-NIE098), HRNDF (NIE104-NIE108) | Yes |
| 62151 | Premium pay (i.e. Shift premium) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / HRN (NIE084-NIE088), HRDDF (NIE094-NIE098), HRNDF (NIE104-NIE108) | Yes |
| 62152 | Premium pay (i.e. Shift premium) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / HRN (NIE084-NIE088), HRDDF (NIE094-NIE098), HRNDF (NIE104-NIE108) | Yes |
| 62153 | Premium pay (i.e. Shift premium) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / HRN (NIE084-NIE088), HRDDF (NIE094-NIE098), HRNDF (NIE104-NIE108) | Yes |
| 62154 | Premium pay (i.e. Shift premium) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / HRN (NIE084-NIE088), HRDDF (NIE094-NIE098), HRNDF (NIE104-NIE108) | Yes |
| 62155 | Premium pay (i.e. Shift premium) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / HRN (NIE084-NIE088), HRDDF (NIE094-NIE098), HRNDF (NIE104-NIE108) | Yes |
| 62160 | Holiday Allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Primas - PagoNS (NIE119) or Bonificacion (NIE139 / NIE140) | Yes |
| 62161 | Arrears - Holiday Allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Primas - PagoNS (NIE119) or Bonificacion (NIE139 / NIE140) | Yes |
| 62162 | Adjustment - Holiday Allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Primas - PagoNS (NIE119) or Bonificacion (NIE139 / NIE140) | Yes |
| 62170 | On-call duty | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / OtroConcepto - ConceptoS (NIE147) | Yes |
| 62171 | Arrears - On-call duty | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / OtroConcepto - ConceptoS (NIE147) | Yes |
| 62172 | Adjustment - On-call duty | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / OtroConcepto - ConceptoS (NIE147) | Yes |
| 62180 | Severance & Seniority | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-02 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | No | Yes | No | No | No | No | No | Non-Salary | NA | NA | Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122) | Yes |
| 62181 | Severance & Seniority | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-02 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | No | Yes | No | No | No | No | No | Non-Salary | NA | NA | Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122) | Yes |
| 62182 | Severance & Seniority | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-02 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | No | Yes | No | No | No | No | No | Non-Salary | NA | NA | Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122) | Yes |
| 62190 | Long Term Disability | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Non-Salary | Yes | No | Devengados / Incapacidad - Tipo (NIE126), Pago (NIE127) | Yes |
| 62200 | Bonus (annual, referral, etc) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) | Yes |
| 62201 | Bonus (annual, referral, etc) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) | Yes |
| 62202 | Bonus (annual, referral, etc) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) | Yes |
| 62203 | Bonus (annual, referral, etc) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) | Yes |
| 62204 | Bonus (annual, referral, etc) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) | Yes |
| 62205 | Bonus (annual, referral, etc) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) | Yes |
| 62206 | Bonus (annual, referral, etc) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) | Yes |
| 62207 | Bonus (annual, referral, etc) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) | Yes |
| 62208 | Bonus (annual, referral, etc) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) | Yes |
| 62209 | Bonus (annual, referral, etc) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) | Yes |
| 62210 | Bonus - profit sharing | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62211 | Bonus - profit sharing | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62212 | Bonus - profit sharing | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62213 | Bonus - profit sharing | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62214 | Bonus - profit sharing | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62215 | Bonus - profit sharing | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62216 | Bonus - profit sharing | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62217 | Bonus - profit sharing | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62218 | Bonus - profit sharing | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62219 | Bonus - profit sharing | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62220 | Bonuses - discretionary or one-time | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62221 | Bonuses - discretionary or one-time | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62222 | Bonuses - discretionary or one-time | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62223 | Bonuses - discretionary or one-time | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62224 | Bonuses - discretionary or one-time | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62225 | Bonuses - discretionary or one-time | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62226 | Bonuses - discretionary or one-time | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62227 | Bonuses - discretionary or one-time | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62228 | Bonuses - discretionary or one-time | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62229 | Bonuses - discretionary or one-time | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62300 | Annual leave pay | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Paid Rest | Yes | NA | Devengados / VacacionesComunes (NIE109-NIE112) | Yes |
| 62302 | Adjustment - Annual leave pay | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Paid Rest | Yes | NA | Devengados / VacacionesComunes (NIE109-NIE112) | Yes |
| 62305 | Annual leave payout | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Paid Rest | Yes | NA | Devengados / VacacionesCompensadas (NIE115, NIE116) | Yes |
| 62310 | Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62311 | Arrears - Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62312 | Adjustment - Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62320 | Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62321 | Arrears - Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62322 | Adjustment - Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62330 | Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62331 | Arrears - Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62332 | Adjustment - Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62334 | Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62335 | Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62340 | Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62341 | Arrears - Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62342 | Adjustment - Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62350 | Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62351 | Arrears - Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62352 | Adjustment - Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62360 | Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62361 | Arrears - Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62362 | Adjustment - Expat allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) | Yes |
| 62400 | Housing allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62401 | Arrears - Housing allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62402 | Adjustment - Housing allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62403 | Advance - Housing allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62410 | Housing allowance 2 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62411 | Arrears - Housing allowance 2 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62412 | Adjustment - Housing allowance 2 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62420 | Housing allowance 3 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62421 | Arrears - Housing allowance 3 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62422 | Adjustment - Housing allowance 3 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62430 | Housing & Rent allowance 1 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62431 | Arrears - Housing & Rent allowance 1 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62432 | Adjustment - Housing & Rent allowance 1 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62440 | Housing & Rent allowance 2 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62441 | Arrears - Housing & Rent allowance 2 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62450 | Housing & Rent allowance 3 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62451 | Arrears - Housing & Rent allowance 3 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62460 | Housing & Rent allowance 4 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62470 | Housing & Rent allowance 5 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62471 | Arrears - Housing & Rent allowance 5 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62472 | Adjustment - Housing & Rent allowance 5 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62480 | Housing & Rent allowance 6 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62481 | Arrears - Housing & Rent allowance 6 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62482 | Adjustment - Housing & Rent allowance 6 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62500 | Car allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62501 | Arrears - Car allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62502 | Adjustment - Car allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62503 | Advance - Car allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62504 | Car maintenance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62505 | Car fuel | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62510 | Car & Transportation allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | Yes | No | Devengados / Transporte - AuxilioTransporte (NIE071) | Yes |
| 62511 | Arrears - Car & Transportation allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | Yes | No | Devengados / Transporte - AuxilioTransporte (NIE071) | Yes |
| 62512 | Adjustment - Car & Transportation allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | Yes | No | Devengados / Transporte - AuxilioTransporte (NIE071) | Yes |
| 62520 | Transportation allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | Yes | No | Devengados / Transporte - AuxilioTransporte (NIE071) | Yes |
| 62521 | Arrears - Transportation allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | Yes | No | Devengados / Transporte - AuxilioTransporte (NIE071) | Yes |
| 62522 | Adjustment - Transportation allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | Yes | No | Devengados / Transporte - AuxilioTransporte (NIE071) | Yes |
| 62523 | Advance - Transportation allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | Yes | No | Devengados / Transporte - AuxilioTransporte (NIE071) | Yes |
| 62530 | Car Maintenance Allowance 2 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62531 | Arrears - Car Maintenance Allowance 2 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62532 | Adjustment - Car Maintenance Allowance 2 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) | Yes |
| 62540 | Relocation allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| 62541 | Arrears - Relocation allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| 62542 | Adjustment - Relocation allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| 62550 | Travel ticket allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| 62551 | Arrears - Travel ticket allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| 62552 | Adjustment - Travel ticket allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| 62560 | Relocation allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| 62561 | Arrears - Relocation allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| 62562 | Adjustment - Relocation allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| 62563 | Advance - Relocation allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| 62570 | Per diem allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | Yes/No | Yes/No | Conditional | Yes/No | Yes/No | Devengados / Transporte - ViaticoManuAlojS (NIE072) / ViaticoManuAlojNS (NIE073) | Yes |
| 62590 | Birth and Marriage Allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62591 | Birth and Marriage Allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion (BonificacionNS, NIE140) | Yes |
| 62599 | COVID-19 Allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Auxilio (AuxilioNS, NIE142) | Yes |
| 62610 | Medical insurance / Medical Care | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Auxilio (AuxilioNS, NIE142) | Yes |
| 62611 | Arrears - Medical insurance / Medical Care | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Auxilio (AuxilioNS, NIE142) | Yes |
| 62612 | Adjustment - Medical insurance / Medical Care | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Auxilio (AuxilioNS, NIE142) | Yes |
| 62615 | Medical insurance / Medical Care | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Auxilio (AuxilioNS, NIE142) | Yes |
| 62616 | Medical insurance / Medical Care | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Auxilio (AuxilioNS, NIE142) | Yes |
| 62618 | Medical insurance / Medical Care | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Auxilio (AuxilioNS, NIE142) | Yes |
| 62619 | Medical insurance / Medical Care | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Auxilio (AuxilioNS, NIE142) | Yes |
| 62630 | Personal Allowance 2 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62631 | Arrears - Personal Allowance 2 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62632 | Adjustment - Personal Allowance 2 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62640 | Pensions & Pension Refunds | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-10 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | Yes/No | Yes | NA | NA | NA | NA | NA | Non-Salary | NA | NA | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 | Yes |
| 62641 | Pensions & Pension Refunds | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-10 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | Yes/No | Yes | NA | NA | NA | NA | NA | Non-Salary | NA | NA | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 | Yes |
| 62642 | Pensions & Pension Refunds | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-10 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | Yes/No | Yes | NA | NA | NA | NA | NA | Non-Salary | NA | NA | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 | Yes |
| 62643 | Pensions & Pension Refunds | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-10 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | Yes/No | Yes | NA | NA | NA | NA | NA | Non-Salary | NA | NA | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 | Yes |
| 62645 | Pensions & Pension Refunds | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-10 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | Yes/No | Yes | NA | NA | NA | NA | NA | Non-Salary | NA | NA | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 | Yes |
| 62646 | Pensions & Pension Refunds | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-10 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | Yes/No | Yes | NA | NA | NA | NA | NA | Non-Salary | NA | NA | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 | Yes |
| 62647 | Pensions & Pension Refunds | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-10 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | Yes/No | Yes | NA | NA | NA | NA | NA | Non-Salary | NA | NA | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 | Yes |
| 62648 | Pensions & Pension Refunds | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-10 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | Yes/No | Yes | NA | NA | NA | NA | NA | Non-Salary | NA | NA | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 | Yes |
| 62650 | Social raise / Social allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / OtroConcepto - ConceptoS (NIE147) | Yes |
| 62660 | Personal Allowance 1 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62661 | Arrears - Personal Allowance 1 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62662 | Adjustment - Personal Allowance 1 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62670 | Benefits plan 1 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Auxilio (AuxilioNS, NIE142) | Yes |
| 62680 | Benefits plan 2 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Auxilio (AuxilioNS, NIE142) | Yes |
| 62700 | Education allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt | Yes |
| 62710 | Schooling allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt | Yes |
| 62711 | Arrears - Schooling allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt | Yes |
| 62720 | Education & Schooling allowance 2 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt | Yes |
| 62721 | Arrears - Education & Schooling allowance 2 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt | Yes |
| 62730 | Education & Schooling allowance 3 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt | Yes |
| 62740 | Education & Schooling allowance 4 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt | Yes |
| 62741 | Arrears - Education & Schooling allowance 4 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt | Yes |
| 62750 | Education & Schooling allowance 5 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt | Yes |
| 62751 | Arrears - Education & Schooling allowance 5 | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt | Yes |
| 62760 | Family allowance (MLA, Children) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Not a nomina electronica element (fund-paid benefit) | Yes |
| 62762 | Adjustment - Family allowance (MLA, Children) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Not a nomina electronica element (fund-paid benefit) | Yes |
| 62770 | Recognition Award | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) | Yes |
| 62870 | Special allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62871 | Special allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62872 | Special allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62873 | Special allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62875 | Special allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62876 | Special allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62877 | Special allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62878 | Special allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62879 | Special allowance | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62880 | Post-termination payment | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | No | No | Devengados / Indemnizacion (NIE160); BonifRetiro (NIE159) for a settlement bonus | Yes |
| 62881 | Post-termination payment | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | No | No | Devengados / Indemnizacion (NIE160); BonifRetiro (NIE159) for a settlement bonus | Yes |
| 62882 | Post-termination payment | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | No | No | Devengados / Indemnizacion (NIE160); BonifRetiro (NIE159) for a settlement bonus | Yes |
| 62883 | Post-termination payment | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | No | No | Devengados / Indemnizacion (NIE160); BonifRetiro (NIE159) for a settlement bonus | Yes |
| 62890 | Stock options and grants | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| 62900 | Statutory Gratuity, EOS | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-02 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | No | Yes | No | No | No | No | No | Non-Salary | NA | NA | Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122) | Yes |
| 62901 | Supplemental basic (i.e. 13th or 14th months salary) | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-03 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | NA | NA | Devengados / Primas - Cantidad (NIE117), Pago (NIE118), PagoNS (NIE119) | Yes |
| 62910 | Gratuity, EOS, Post-termination, etc. | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-02 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | No | Yes | No | No | No | No | No | Non-Salary | NA | NA | Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122) | Yes |
| 62920 | Gratuity, EOS, Post-termination, etc. | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-02 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | No | Yes | No | No | No | No | No | Non-Salary | NA | NA | Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122) | Yes |
| 62930 | Gratuity, EOS, Post-termination, etc. | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-02 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | No | Yes | No | No | No | No | No | Non-Salary | NA | NA | Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122) | Yes |
| 62960 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62961 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62962 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62963 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62964 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62965 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62966 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62967 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62968 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62969 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62980 | Salary addition | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) | Yes |
| 62990 | Stock options and grants | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| 62991 | Stock options and grants | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| 62993 | Stock options and grants | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| 62994 | Stock options and grants | (codigo global - ver la explicacion para el tratamiento colombiano) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / OtroConcepto (NIE146-NIE148) | Yes |
| CO-SALARIO-BASICO | Basic salary | Salario Basico | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070) | Yes |
| CO-SALARIO-INTEGRAL | All-inclusive salary | Salario Integral | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | No | Yes | Trabajador / SalarioIntegral flag (NIE056); Sueldo (NIE062); PILA T2R2-041 | Yes |
| CO-AUX-TRANSPORTE | Statutory transport allowance | Auxilio de Transporte | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | Yes | No | Devengados / Transporte - AuxilioTransporte (NIE071) | Yes |
| CO-AUX-CONECTIVIDAD | Connectivity allowance (teleworkers) | Auxilio de Conectividad Digital | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | Yes | No | Devengados / Transporte - AuxilioTransporte (NIE071); Teletrabajo (NIE158) | Yes |
| CO-HED | Day overtime (+25%) | Hora Extra Diurna (25%) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HED - Cantidad (NIE076), Porcentaje (NIE077), Pago (NIE078) | Yes |
| CO-HEN | Night overtime (+75%) | Hora Extra Nocturna (75%) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HEN - Cantidad (NIE081), Porcentaje (NIE082), Pago (NIE083) | Yes |
| CO-RECARGO-NOCTURNO | Night premium (35%) | Recargo Nocturno (35%) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / HRN - Cantidad (NIE086), Porcentaje (NIE087), Pago (NIE088) | Yes |
| CO-RECARGO-DOMINICAL | Obligatory rest-day / holiday premium (80% / 90%) | Recargo Dominical y Festivo (80% hasta 30-jun-2026 / 90% desde 1-jul-2026) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HRDDF - Cantidad (NIE096), Porcentaje (NIE097), Pago (NIE098) | Yes |
| CO-HEDDF | Day overtime on a rest day / holiday (+105% / +115%) | Hora Extra Diurna Dominical y Festiva | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HEDDF - Cantidad (NIE091), Porcentaje (NIE092), Pago (NIE093) | Yes |
| CO-HENDF | Night overtime on a rest day / holiday (+155% / +165%) | Hora Extra Nocturna Dominical y Festiva | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | No | Devengados / HENDF - Cantidad (NIE101), Porcentaje (NIE102), Pago (NIE103) | Yes |
| CO-HRNDF | Night premium on a rest day / holiday (+115% / +125%) | Recargo Nocturno Dominical y Festivo | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / HRNDF - Cantidad (NIE106), Porcentaje (NIE107), Pago (NIE108) | Yes |
| CO-DESCANSO-REMUNERADO | Paid weekly rest day and paid public holidays | Descanso Dominical y Festivo Remunerado | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Paid Rest | Yes | Yes | Devengados / Basico - SueldoTrabajado (NIE070); LicenciaR (NIE132-NIE135) where itemised | Yes |
| CO-COMISIONES | Commissions and sales percentages | Comisiones y Porcentajes sobre Ventas | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Comisiones - Comision (NIE155) | Yes |
| CO-BONIF-HABITUAL | Habitual bonus (salary) | Bonificacion Habitual (Salarial) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Bonificacion - BonificacionS (NIE139) | Yes |
| CO-BONIF-NOSALARIAL | Extra-statutory bonus under a written non-salary pact | Bonificacion Extralegal No Salarial (Pacto CST art. 128) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion - BonificacionNS (NIE140) | Yes |
| CO-GRATIF-OCASIONAL | Occasional gratuity (mera liberalidad) | Gratificacion Ocasional | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Bonificacion - BonificacionNS (NIE140) | Yes |
| CO-SALARIO-ESPECIE | Salary in kind | Salario en Especie | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / OtroConcepto - ConceptoS (NIE147) | Yes |
| CO-PRIMA-SERVICIOS | Statutory service bonus | Prima de Servicios | Earning | CO-TX-03 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | NA | NA | Devengados / Primas - Cantidad (NIE117), Pago (NIE118), PagoNS (NIE119) | Yes |
| CO-CESANTIAS | Severance savings | Auxilio de Cesantias | Earning | CO-TX-02 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | No | Yes | No | No | No | No | No | Non-Salary | NA | NA | Devengados / Cesantias - Pago (NIE120); Consignacion Cesantias T14 | Yes |
| CO-INTERESES-CESANTIAS | Interest on severance savings | Intereses a las Cesantias | Earning | CO-TX-02 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | No | Yes | No | No | No | No | No | Non-Salary | NA | NA | Devengados / Cesantias - Porcentaje (NIE121), PagoIntereses (NIE122) | Yes |
| CO-VACACIONES | Annual leave taken | Vacaciones Disfrutadas | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Paid Rest | Yes | NA | Devengados / VacacionesComunes - FechaInicio (NIE109), Cantidad (NIE111), Pago (NIE112) | Yes |
| CO-VACACIONES-COMPENSADAS | Vacation compensated in cash | Compensacion en Dinero de Vacaciones | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Paid Rest | Yes | NA | Devengados / VacacionesCompensadas - Cantidad (NIE115), Pago (NIE116) | Yes |
| CO-DOTACION | Work clothing and footwear | Dotacion de Labor (Calzado y Vestido) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Devengados / Dotacion (NIE156) | Yes |
| CO-INCAP-EG-EMPLEADOR | Sickness incapacity, days 1-2 (employer) | Incapacidad por Enfermedad General - Dias 1 y 2 (Empleador) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Non-Salary | Yes | No | Devengados / Incapacidad - Tipo (NIE126) = enfermedad general, Pago (NIE127); PILA T2R2-025 | Yes |
| CO-INCAP-EG-EPS | Sickness incapacity from day 3 (EPS) | Incapacidad por Enfermedad General - desde el Dia 3 (EPS) | Earning | CO-TX-07 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | Yes/No | Yes | Yes | Yes | Yes | No | Yes | Non-Salary | No | No | Devengados / Incapacidad - Cantidad (NIE125), Pago (NIE127); PILA T2R2-057, T2R2-058 | Yes |
| CO-INCAP-IRL | Occupational accident or disease incapacity (ARL) | Incapacidad de Origen Laboral (ARL) | Earning | CO-TX-07 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | Yes/No | Yes | Yes | Yes | Yes | No | Yes | Non-Salary | No | No | Devengados / Incapacidad - Tipo (NIE126) = riesgos laborales; PILA T2R2-030, T2R2-093, T2R2-094 | Yes |
| CO-LIC-MATERNIDAD | Maternity leave (18 weeks) | Licencia de Maternidad (18 semanas) | Earning | CO-TX-07 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | Yes/No | Yes | Yes | Yes | Yes | No | Yes | Non-Salary | No | No | Devengados / LicenciaMP - Cantidad (NIE130), Pago (NIE131); PILA T2R2-059, T2R2-060 | Yes |
| CO-LIC-PATERNIDAD | Paternity leave (2 weeks) | Licencia de Paternidad (2 semanas) | Earning | CO-TX-07 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | Yes/No | Yes | Yes | Yes | Yes | No | Yes | Non-Salary | No | No | Devengados / LicenciaMP - Cantidad (NIE130), Pago (NIE131) | Yes |
| CO-LIC-PARENTAL-COMPARTIDA | Shared and flexible parental leave | Licencia Parental Compartida y Flexible | Earning | CO-TX-07 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | Yes/No | Yes | Yes | Yes | Yes | No | Yes | Non-Salary | No | No | Devengados / LicenciaMP - Cantidad (NIE130), Pago (NIE131) | Yes |
| CO-LIC-REMUNERADA | Statutory paid leave (CST art. 57 num. 6) | Licencia Remunerada Legal (CST art. 57 num. 6) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Paid Rest | Yes | Yes | Devengados / LicenciaR - Cantidad (NIE134), Pago (NIE135); PILA T2R2-027 (VAC-LR) | Yes |
| CO-LIC-LUTO | Bereavement leave (5 working days) | Licencia de Luto (5 dias habiles) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Paid Rest | Yes | Yes | Devengados / LicenciaR - Cantidad (NIE134), Pago (NIE135) | Yes |
| CO-LIC-NO-REMUNERADA | Unpaid leave / contract suspension | Licencia No Remunerada / Suspension del Contrato (SLN) | Earning | CO-NA | Lump Sum |  | Additional | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Devengados / LicenciaNR (NIE136-NIE138); PILA T2R2-024, T2R2-083, T2R2-084 | Yes |
| CO-HUELGA-LEGAL | Legal strike days | Huelga Legal | Earning | CO-NA | Lump Sum |  | Additional | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Devengados / HuelgaLegal - FechaInicio (NIE143), Cantidad (NIE145) | Yes |
| CO-APOYO-APRENDIZ | Apprentice maintenance support | Apoyo de Sostenimiento del Aprendiz | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes/No | Yes | Yes/No | Yes/No | Conditional | Yes/No | Yes/No | Devengados / ApoyoSost (NIE157); Decreto 0223 de 2026 art. 2.2.6.3.3.4 | Yes |
| CO-INDEM-DESPIDO | Indemnity for dismissal without just cause | Indemnizacion por Despido sin Justa Causa (CST art. 64) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | No | No | Devengados / Indemnizacion (NIE160) | Yes |
| CO-INDEM-MORATORIA | Late-payment penalty | Indemnizacion Moratoria (CST art. 65) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | No | No | Devengados / Indemnizacion (NIE160) | Yes |
| CO-SANCION-CESANTIAS | Penalty for non-deposit of severance savings | Sancion por No Consignacion de Cesantias | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | No | No | Devengados / Indemnizacion (NIE160) | Yes |
| CO-SANCION-INTERESES | Penalty for unpaid severance interest | Sancion por No Pago de Intereses a las Cesantias | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | No | No | Devengados / Indemnizacion (NIE160) | Yes |
| CO-INDEM-FIJO-OBRA | Indemnity for early termination of a fixed-term or work-or-task contract | Indemnizacion por Terminacion Anticipada de Contrato a Termino Fijo u Obra o Labor | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | No | No | Devengados / Indemnizacion (NIE160) | Yes |
| CO-INDEM-PROTECCION | Indemnity for dismissal during protected status | Indemnizacion por Despido en Estado de Proteccion (Fuero) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | No | No | Devengados / Indemnizacion (NIE160) | Yes |
| CO-BONIF-RETIRO | Retirement or mutual-termination settlement bonus | Bonificacion por Retiro / Acuerdo de Terminacion | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | No | No | No | No | No | Non-Salary | No | No | Devengados / BonifRetiro (NIE159) | Yes |
| CO-PAGO-ALIMENTACION-3P | Third-party meal payments | Pagos de Alimentacion a Terceros | Earning | CO-TX-05 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes/No | Yes/No | Yes/No | No | No | No | No | No | Non-Salary | No | No | Devengados / BonoEPCTV - PagoAlimentacionS (NIE153) / PagoAlimentacionNS (NIE154) | Yes |
| CO-BONO-EPCTV | Voucher, card or non-cash instrument payment | Pago con Bonos Electronicos o de Papel, Cheques, Tarjetas o Vales | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / BonoEPCTV - PagoS (NIE151) / PagoNS (NIE152) | Yes |
| CO-MEDICINA-PREPAGADA-ER | Employer-paid prepaid health / supplementary health plan | Medicina Prepagada o Plan Complementario Pagado por el Empleador | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Auxilio - AuxilioNS (NIE142); Deducciones / PlanComplementarios (NIE182) | Yes |
| CO-APORTE-PENSION-VOL-ER | Employer contribution to a voluntary pension fund | Aporte Patronal a Fondo de Pensiones Voluntarias | Earning | CO-TX-09 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes/No | Yes/No | No | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Auxilio - AuxilioNS (NIE142); Formulario 220 casilla 56 / Formato 2276 N26 | Yes |
| CO-APORTE-RAIS-VOL-ER | Employer voluntary contribution to the individual pension account | Cotizacion Voluntaria al RAIS pagada por el Empleador | Earning | CO-TX-04 | Pro Rata |  | Recurring | No | No | Regular (System default) | No | No | No | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Auxilio - AuxilioNS (NIE142); PILA T2R2-028, T2R2-049; Formato 2276 N25 | Yes |
| CO-ACCIONES | Equity and share-incentive awards | Acciones e Incentivos en Acciones | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / OtroConcepto - ConceptoS or ConceptoNS (NIE146-NIE148) | Yes |
| CO-VIATICOS-PERMANENTES | Permanent per diem - board and lodging portion (salary) | Viaticos Permanentes - Manutencion y Alojamiento (Salarial) | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Salary | Yes | Yes | Devengados / Transporte - ViaticoManuAlojS (NIE072) | Yes |
| CO-VIATICOS-OCASIONALES | Occasional per diem, and the transport / representation portion | Viaticos Accidentales y Porcion de Transporte y Representacion (No Salarial) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Devengados / Transporte - ViaticoManuAlojNS (NIE073) | Yes |
| CO-TELETRABAJO | Telework allowance | Auxilio de Teletrabajo | Earning | CO-TX-01 | Pro Rata |  | Recurring | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / Teletrabajo (NIE158) | Yes |
| CO-PROPINAS | Tips | Propinas | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Not a nomina electronica devengado (not an employer payment) | Yes |
| CO-COMPENSACION-COOP | Cooperative associated-work compensation | Compensacion Ordinaria y Extraordinaria del Trabajo Asociado Cooperativo | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Devengados / Compensacion - CompensacionO (NIE149) / CompensacionE (NIE150) | Yes |
| CO-PAGO-TERCERO | Third-party payment (accrued) | Pago a Terceros (Devengado) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes | Yes | Yes | Yes/No | Yes/No | Yes/No | No | Yes/No | Non-Salary | No | No | Devengados / PagosTerceros - PagoTercero (NIE193) | Yes |
| CO-ANTICIPO-NOMINA | Payroll advance (accrued) | Anticipo de Nomina (Devengado) | Earning | CO-TX-01 | Lump Sum |  | Additional | No | No | Regular (System default) | Yes/No | Yes/No | Yes/No | Yes/No | Yes/No | Yes/No | Yes/No | Yes/No | Conditional | Yes/No | Yes/No | Devengados / Anticipos - Anticipo (NIE194) | Yes |
| CO-REINTEGRO | Reimbursement to the employee (accrued) | Reintegro (Devengado) | Earning | CO-TX-06 | Lump Sum |  | Additional | No | No | Regular (System default) | No | No | No | No | No | No | No | No | Non-Salary | No | No | Devengados / Reintegro (NIE201); Deducciones / Reintegro (NIE184) | Yes |
| CO-DED-SALUD | Health contribution (employee) 4% | Aporte a Salud - Empleado (4%) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / Salud - Porcentaje (NIE161), Deduccion (NIE163); PILA T2R2-054, T2R2-055 | No |
| CO-DED-PENSION | Mandatory pension contribution (employee) 4% | Aporte a Pension Obligatoria - Empleado (4%) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / FondoPension - Porcentaje (NIE164), Deduccion (NIE166); PILA T2R2-046, T2R2-047 | No |
| CO-DED-FSP-SOLIDARIDAD | Solidarity pension fund - solidarity sub-account 1% | Fondo de Solidaridad Pensional - Subcuenta de Solidaridad (1%) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / FondoSP - Porcentaje (NIE167), DeduccionSP (NIE168); PILA T2R2-051 | No |
| CO-DED-FSP-SUBSISTENCIA | Solidarity pension fund - subsistence sub-account 0.2%-1.0% | Fondo de Solidaridad Pensional - Subcuenta de Subsistencia (0,2%-1,0%) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / FondoSP - PorcentajeSub (NIE169), DeduccionSub (NIE170); PILA T2R2-052 | No |
| CO-RETENCION-FUENTE | Income tax withholding on work income (resident) | Retencion en la Fuente sobre Rentas de Trabajo | Tax | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / RetencionFuente (NIE177); Formulario 350 casillas 77 and 93 | Yes |
| CO-RETENCION-NO-RESIDENTE | Income tax withholding - non-resident (flat 20%) | Retencion en la Fuente a No Residentes (20% - ET art. 408) | Tax | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / RetencionFuente (NIE177); Formulario 350 casillas 109-112 and hoja 2 casillas 141-155 | Yes |
| CO-DED-PENSION-VOLUNTARIA | Voluntary pension fund contribution (employee) | Aporte Voluntario a Fondo de Pensiones Voluntarias | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / PensionVoluntaria (NIE198) | No |
| CO-DED-AFC-AVC | AFC / AVC long-term savings contribution (employee) | Aporte a Cuentas AFC / AVC | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / AFC (NIE179) | No |
| CO-DED-RAIS-VOLUNTARIO | Voluntary contribution to the individual pension account (employee) | Cotizacion Voluntaria al Regimen de Ahorro Individual (RAIS) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197); PILA T2R2-028, T2R2-048, T2R2-053 | No |
| CO-DED-SINDICATO | Union dues | Cuota Sindical | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / Sindicato - Porcentaje (NIE171), Deduccion (NIE172) | No |
| CO-DED-COOPERATIVA | Cooperative and employee savings-fund dues | Aportes a Cooperativas y Fondos de Empleados | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / Cooperativa (NIE180) | No |
| CO-DED-SANCION-DISCIPLINARIA | Disciplinary sanction | Sancion Disciplinaria | Deduction | CO-NA | Lump Sum |  | Additional | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / Sancion - SancionPublic (NIE173) / SancionPriv (NIE174) | No |
| CO-DED-SABES | Higher-education solidarity contribution | Contribucion Solidaria a la Educacion Superior (Contribucion Sabes) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / Educacion (NIE183) or OtrasDeducciones (NIE197) | No |
| CO-DED-LIBRANZA | Payroll lending repayment | Libranza (Ley 1527 de 2012) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / Libranza - Descripcion (NIE175), Deduccion (NIE176) | No |
| CO-DED-PRESTAMO | Employer loan and advance recovery | Prestamo y Anticipo del Empleador (CST art. 151) | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / Anticipos (NIE196) or Deuda (NIE185) | No |
| CO-DED-EMBARGO | Judicial or tax attachment | Embargo Judicial o Fiscal | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / EmbargoFiscal (NIE181) | No |
| CO-DED-ALIMENTOS | Maintenance / child-support garnishment | Embargo por Alimentos | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / EmbargoFiscal (NIE181) or PagosTerceros (NIE195) | No |
| CO-DED-MEDICINA-PREPAGADA | Prepaid health / supplementary plan (employee share) | Medicina Prepagada y Plan Complementario - Empleado | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / PlanComplementarios (NIE182) | No |
| CO-DED-OTRAS | Other authorised deduction | Otras Deducciones Autorizadas | Deduction | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Deducciones / OtrasDeducciones (NIE197) | No |
| CO-ER-SALUD | Health contribution (employer) 8.5% | Aporte a Salud - Empleador (8,5%) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | PILA T2R2-054, T2R2-055; A1-033; T2R2-076 | No |
| CO-ER-PENSION | Mandatory pension contribution (employer) 12% | Aporte a Pension Obligatoria - Empleador (12%) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | PILA T2R2-046, T2R2-047, T2R2-050 | No |
| CO-ER-ARL | Occupational risk contribution (employer) | Aporte a Riesgos Laborales - ARL (0,348%-8,7%) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | PILA T2R2-061, T2R2-062, T2R2-063, T2R2-077, T2R2-078 | No |
| CO-ER-CCF | Family compensation fund levy 4% | Aporte a Caja de Compensacion Familiar - CCF (4%) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | PILA T2R2-045 (IBC CCF), T2R2-064, T2R2-065; T2R2-035 (CCF code); T2R2-039 (CCF days) | No |
| CO-ER-SENA | Apprenticeship training levy 2% | Aporte al SENA (2%) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | PILA T2R2-095, T2R2-066, T2R2-067 | No |
| CO-ER-ICBF | Family welfare levy 3% | Aporte al ICBF (3%) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | PILA T2R2-095, T2R2-068, T2R2-069 | No |
| CO-ER-PENSION-ALTO-RIESGO | Additional employer pension contribution - high-risk activity | Aporte Patronal Adicional de Pension de Alto Riesgo | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | PILA T2R2-079; Trabajador / AltoRiesgoPension (NIE043) | No |
| CO-PROV-PRIMA | Service bonus accrual (employer) | Provision de Prima de Servicios (8,3333%) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Not a PILA or nomina electronica field - an accounting provision | No |
| CO-PROV-CESANTIAS | Severance-savings accrual (employer) | Provision de Cesantias (8,3333%) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Consignacion Cesantias planilla T14; MA02 / MA03 for the monthly advance | No |
| CO-PROV-INTERESES-CESANTIAS | Severance-interest accrual (employer) | Provision de Intereses a las Cesantias (1,0000%) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Interes de cesantias IN01 / IN02 / IN03 (not a file field) | No |
| CO-PROV-VACACIONES | Vacation accrual (employer) | Provision de Vacaciones (4,1667%) | Employer Contribution | CO-NA | Pro Rata |  | Recurring | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Not a PILA or nomina electronica field - an accounting provision | No |
| CO-BASE-IBC | Social-security contribution base | Ingreso Base de Cotizacion (IBC) | Base | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | PILA T2R2-042 (IBC pension), T2R2-043 (IBC salud), T2R2-044 (IBC riesgos laborales) | No |
| CO-BASE-PARAFISCAL | Payroll-levy base | Base de Aportes Parafiscales (Nomina Mensual de Salarios) | Base | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | PILA T2R2-045 (IBC CCF), T2R2-095 (IBC otros parafiscales), T2R1-020 (valor total de la nomina) | No |
| CO-BASE-RETENCION | Withholding tax base | Base Gravable de Retencion (ET art. 388) | Base | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Formulario 350 casilla 77; Deducciones / RetencionFuente (NIE177) | No |
| CO-BASE-PRESTACIONAL | Statutory-benefit base | Base Prestacional (Prima, Cesantias e Intereses) | Base | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Derived - feeds Devengados / Primas (NIE117-NIE119) and Cesantias (NIE120-NIE122) | No |
| CO-BASE-VACACIONES | Vacation base | Base de Vacaciones (CST art. 192) | Base | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Derived - feeds Devengados / VacacionesComunes (NIE112) and VacacionesCompensadas (NIE116) | No |
| CO-INT-CLAMP40 | Non-salary excess forced back into the contribution base | Excedente No Salarial Reintegrado al IBC (Ley 1393 de 2010 art. 30) | Intermediary | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Derived - feeds PILA T2R2-042, T2R2-043, T2R2-044 | No |
| CO-RATE-HORA-ORDINARIA | Ordinary hour value | Valor de la Hora Ordinaria | Percentage | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Derived - feeds every hour-type Porcentaje / Pago element | No |
| CO-PCT-RETENCION-PROC2 | Procedure 2 fixed withholding percentage | Porcentaje Fijo de Retencion (Procedimiento 2) | Percentage | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Derived - feeds Deducciones / RetencionFuente (NIE177) | No |
| CO-REDONDEO | Rounding residual (electronic payroll) | Redondeo | Notional | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NominaIndividual / Redondeo (NIE186), DevengadosTotal (NIE187), DeduccionesTotal (NIE188), ComprobanteTotal (NIE189) | No |
| CO-FLAG-SALARIO-INTEGRAL | All-inclusive salary flag | Indicador de Salario Integral | Flag | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Trabajador / SalarioIntegral (NIE056); Sueldo (NIE062); PILA T2R2-041 | No |
| CO-FLAG-EXONERACION-114-1 | ET art. 114-1 exoneration flag | Indicador de Exoneracion de Aportes (ET art. 114-1) | Flag | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | PILA A1-033, T2R2-076; Formulario 350 casilla 27 | No |
| CO-FLAG-RESIDENCIA-FISCAL | Tax residence flag with effective date | Indicador de Residencia Fiscal con Fecha de Efecto | Flag | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Trabajador / LugarTrabajoPais (NIE050); Formulario 350 hoja 2 casillas 141, 144 | No |
| CO-FLAG-ALTO-RIESGO-PENSION | High-risk pension activity flag | Indicador de Actividad de Alto Riesgo Pensional | Flag | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Trabajador / AltoRiesgoPension (NIE043); PILA T2R2-079 | No |
| CO-FLAG-PACTO-NO-SALARIAL | Written non-salary pact flag | Indicador de Pacto de Exclusion Salarial (CST art. 128) | Flag | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Drives every paired S / NS element (NIE139/140, NIE141/142, NIE147/148, NIE151/152, NIE153/154, NIE072/073) | No |
| CO-FLAG-PENSIONADO-ACTIVO | Employed old-age pensioner flag | Indicador de Pensionado en Activo | Flag | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Trabajador / SubTipoTrabajador (NIE042); PILA T2R2-005, T2R2-006 | No |
| CO-FLAG-PROCEDIMIENTO-RETENCION | Withholding procedure election flag | Indicador de Procedimiento de Retencion (1 o 2) | Flag | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Not reported - a configuration flag driving Deducciones / RetencionFuente (NIE177) | No |
| CO-FLAG-DEPENDIENTES | Dependants declaration flag and count | Indicador y Numero de Dependientes Economicos | Flag | CO-NA | Lump Sum |  | NA | No | No | Regular (System default) | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | NA | Formulario 220 casillas 79-82; Formato 2276 numeral N34 | No |

**Row count: 402 wage types.**

---

## Sheet 2 (continued) - Explanation, Formula, Tax Code Source and YTD Remarks, per code

One block per wage type, in catalogue order. Nothing is summarised: columns **D**, **F**, **Z** and **AB**
appear here in full.


### `21100` - Basic salary deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21102` - Adjustment - Basic salary deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21103` - Advance - Basic salary deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21108` - Sick leave - Basic salary deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21109` - Unpaid LOA - Basic salary deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21110` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21111` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21112` - Adjustment - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21113` - Advance - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21114` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21115` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21116` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21117` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21118` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21119` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21120` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21121` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21122` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21123` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21124` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21125` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21127` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21140` - Salary addition deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21141` - Salary addition deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21142` - Salary addition deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21143` - Salary addition deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21144` - Salary addition deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21145` - Salary addition deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21146` - Salary addition deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21147` - Salary addition deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21148` - Salary addition deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21149` - Salary addition deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21150` - Premium pay (i.e. Shift premium) deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21151` - Premium pay (i.e. Shift premium) deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21152` - Premium pay (i.e. Shift premium) deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21190` - Long Term Disability deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Recovery counterpart of the long-term disability earnings line, typically where the EPS or the pension administrator subsequently pays the certified benefit that the employer advanced. |
| Formula (col F) | Reversal / recovery of an employer-paid disability top-up |
| Nomina Electronica element (col Y) | Deducciones / Reintegro (NIE184) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21210` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21211` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21212` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21213` - Overtime deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction mechanism, not remuneration. Subject to CST art. 149: no deduction without the employee's written order for each case or a court order, and none may breach the SMMLV floor or the non-attachable portion. Every subjection column NA. |
| Formula (col F) | Negative recovery / adjustment counterpart of the matching earnings code (absence, overpayment, advance recovery); prorated S x days / 30 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21400` - Housing allowance deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction counterpart. NOTE for the transport allowance: it is not payable for days of unpaid leave, sickness incapacity or maternity / paternity leave (no travel occurs), so the recovery line is a routine monthly event, prorated on the 30-day commercial month. |
| Formula (col F) | Negative counterpart of the housing / transport allowance earnings line (non-entitlement, absence or overpayment recovery) |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21520` - Transportation allowance deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Deduction counterpart. NOTE for the transport allowance: it is not payable for days of unpaid leave, sickness incapacity or maternity / paternity leave (no travel occurs), so the recovery line is a routine monthly event, prorated on the 30-day commercial month. |
| Formula (col F) | Negative counterpart of the housing / transport allowance earnings line (non-entitlement, absence or overpayment recovery) |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21610` - Health insurance & Life insurance contributions - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Employee health withholding line, or a private health / life insurance premium deducted on the employee's written authorisation for each case (CST art. 149 num. 1). The mandatory 4% is NON-TAXABLE INCOME to the employee (ET art. 56) and is subtracted at step (B) of the art. 388 depuration. Subjection columns NA - this is the deduction, not an earning. |
| Formula (col F) | Employee mandatory health = IBC x 4.00%, rounded UP to the next multiple of 100 (Decreto 1990 de 2016 art. 1); or a private health / life premium by written authorisation |
| Nomina Electronica element (col Y) | Deducciones / Salud (NIE161, NIE163) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21611` - Health insurance & Life insurance contributions - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Employee health withholding line, or a private health / life insurance premium deducted on the employee's written authorisation for each case (CST art. 149 num. 1). The mandatory 4% is NON-TAXABLE INCOME to the employee (ET art. 56) and is subtracted at step (B) of the art. 388 depuration. Subjection columns NA - this is the deduction, not an earning. |
| Formula (col F) | Employee mandatory health = IBC x 4.00%, rounded UP to the next multiple of 100 (Decreto 1990 de 2016 art. 1); or a private health / life premium by written authorisation |
| Nomina Electronica element (col Y) | Deducciones / Salud (NIE161, NIE163) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21640` - Pensions & Pension Contributions (pre-tax deduction) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Employee pension withholding, and voluntary pension / long-term-savings deductions. The mandatory 4% is NON-TAXABLE INCOME (ET art. 55); voluntary pension fund and AFC/AVC amounts are EXEMPT INCOME inside the 40% and 1,340-UVT caps (ET arts. 126-1, 126-4), and voluntary contributions to the individual pension account are non-taxable income within 25% of annual labour income / 2,500 UVT. No pension contribution is due from an employed old-age pensioner (PILA worker sub-type 01). |
| Formula (col F) | Employee mandatory pension = IBC x 4.00% (rounded UP to the next multiple of 100); voluntary pension fund / AFC-AVC contributions on written authorisation |
| Nomina Electronica element (col Y) | Deducciones / FondoPension (NIE164, NIE166); PensionVoluntaria (NIE198); AFC (NIE179) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21641` - Pensions & Pension Contributions (pre-tax deduction) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Employee pension withholding, and voluntary pension / long-term-savings deductions. The mandatory 4% is NON-TAXABLE INCOME (ET art. 55); voluntary pension fund and AFC/AVC amounts are EXEMPT INCOME inside the 40% and 1,340-UVT caps (ET arts. 126-1, 126-4), and voluntary contributions to the individual pension account are non-taxable income within 25% of annual labour income / 2,500 UVT. No pension contribution is due from an employed old-age pensioner (PILA worker sub-type 01). |
| Formula (col F) | Employee mandatory pension = IBC x 4.00% (rounded UP to the next multiple of 100); voluntary pension fund / AFC-AVC contributions on written authorisation |
| Nomina Electronica element (col Y) | Deducciones / FondoPension (NIE164, NIE166); PensionVoluntaria (NIE198); AFC (NIE179) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21642` - Pensions & Pension Contributions (pre-tax deduction) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Employee pension withholding, and voluntary pension / long-term-savings deductions. The mandatory 4% is NON-TAXABLE INCOME (ET art. 55); voluntary pension fund and AFC/AVC amounts are EXEMPT INCOME inside the 40% and 1,340-UVT caps (ET arts. 126-1, 126-4), and voluntary contributions to the individual pension account are non-taxable income within 25% of annual labour income / 2,500 UVT. No pension contribution is due from an employed old-age pensioner (PILA worker sub-type 01). |
| Formula (col F) | Employee mandatory pension = IBC x 4.00% (rounded UP to the next multiple of 100); voluntary pension fund / AFC-AVC contributions on written authorisation |
| Nomina Electronica element (col Y) | Deducciones / FondoPension (NIE164, NIE166); PensionVoluntaria (NIE198); AFC (NIE179) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21645` - Pensions & Pension Contributions (pre-tax deduction) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Employee pension withholding, and voluntary pension / long-term-savings deductions. The mandatory 4% is NON-TAXABLE INCOME (ET art. 55); voluntary pension fund and AFC/AVC amounts are EXEMPT INCOME inside the 40% and 1,340-UVT caps (ET arts. 126-1, 126-4), and voluntary contributions to the individual pension account are non-taxable income within 25% of annual labour income / 2,500 UVT. No pension contribution is due from an employed old-age pensioner (PILA worker sub-type 01). |
| Formula (col F) | Employee mandatory pension = IBC x 4.00% (rounded UP to the next multiple of 100); voluntary pension fund / AFC-AVC contributions on written authorisation |
| Nomina Electronica element (col Y) | Deducciones / FondoPension (NIE164, NIE166); PensionVoluntaria (NIE198); AFC (NIE179) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21670` - Benefits plan 1 deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Post-tax benefits-plan deduction. A prepaid-medicine or health-insurance premium separately generates an ET art. 387 lits. a) and b) DEDUCTION of up to 16 UVT per month (COP 837,984) against the withholding base, provided the provider is supervised by the National Health Superintendence or the Financial Superintendence. |
| Formula (col F) | Employee share of an employer benefits plan (prepaid medicine, complementary health plan, group life), on written authorisation for each case |
| Nomina Electronica element (col Y) | Deducciones / PlanComplementarios (NIE182) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21800` - Expense reimbursement deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Recovery line for an unsubstantiated expense advance. Requires the employee's written authorisation (CST art. 149 num. 1) and may not take pay below the SMMLV or into the non-attachable portion without a court order (art. 149 num. 2). |
| Formula (col F) | Recovery of an expense advance not supported by documentation |
| Nomina Electronica element (col Y) | Deducciones / Anticipos (NIE196) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21810` - Parking deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Voluntary post-tax deduction. Written order signed for each case (CST art. 149 num. 1); protected by the SMMLV floor. |
| Formula (col F) | Employee parking charge, on written authorisation |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21820` - Donation deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Voluntary post-tax deduction; no withholding effect. Written authorisation required. |
| Formula (col F) | Employee-authorised donation (e.g. to an employee welfare fund) |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21890` - Stock options and grants deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Offsetting deduction against the equity earnings line, so that net cash pay is unchanged while the withholding on the taxable spread is correctly computed (CCG Module 7.2). |
| Formula (col F) | Employee-borne exercise price / share-purchase amount recovered through payroll |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `21900` - Custom Social Security (employee) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Solidarity pension fund - an EMPLOYEE-ONLY surcharge ADDITIONAL to the 4% pension, which must NEVER be merged into the pension line: the nomina electronica carries FOUR separate attributes (solidarity percentage and amount, subsistence percentage and amount). It is non-taxable income (ET art. 55), grouped with the pension contribution on Formato 2276 numeral N24. Not exonerable, employer share nil. |
| Formula (col F) | Fondo de Solidaridad Pensional = IBC x 1.00% where IBC >= 4 SMMLV (7,003,620), PLUS the subsistence sub-account 0.2/0.4/0.6/0.8/1.0% by SMMLV band from 16 SMMLV |
| Nomina Electronica element (col Y) | Deducciones / FondoSP (NIE167-NIE170) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `23640` - Pensions & Pension Contributions (employer, no-recon) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Employer pension liability. The 12% is never relieved by the ET art. 114-1 exoneration - only employer health 8.5%, SENA 2% and ICBF 3% are. Rounded UP to the next multiple of 100. A high-risk-activity employee (Decreto Ley 2090 de 2003) carries an ADDITIONAL employer pension contribution: the Resolucion 2388 de 2016 rate table shows a 26% total against the standard 16%, implying +10 percentage points employer-borne - see CO-ER-PENSION-ALTO-RIESGO, an open item carried in the QA report. |
| Formula (col F) | Employer pension = IBC x 12.00% (NEVER exonerated); employer voluntary pension fund contribution on the employee's behalf within 30% of labour income / 3,800 UVT |
| Nomina Electronica element (col Y) | PILA T2R2-046, T2R2-047, T2R2-050; not a nomina electronica element |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `23670` - Benefits plan 1 deduction - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Employer-borne benefit cost. Structured as NON-SALARY under a written CST art. 128 pact in market practice, which keeps it out of the IBC, the levy base and the statutory-benefit base - subject always to the 40% clamp. It is nonetheless a TAXABLE benefit to the employee (see CO-MEDICINA-PREPAGADA-ER). No fringe-benefits tax exists in Colombia. |
| Formula (col F) | Employer share of a benefits plan (prepaid medicine, complementary health plan, group life) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioNS, NIE142) for the employee-side value |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `23671` - Company contribution liability - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Employer contribution / accrual line, computed IN PARALLEL with the employee gross-to-net and never touching net pay. Employer health 8.5%, SENA 2% and ICBF 3% are EXONERATED where the employee earns STRICTLY LESS THAN 10 SMMLV (17,509,050) and the employer is an income-tax-filing legal person (ET art. 114-1); pension 12%, ARL and CCF 4% are never exonerated. Each amount rounds UP to the next multiple of 100. |
| Formula (col F) | Employer-borne contribution liability: health 8.5% + pension 12% + ARL 0.348-8.7% on the IBC; CCF 4% + SENA 2% + ICBF 3% on the Ley 21/1982 levy base (no ceiling); plus the statutory benefit accruals 8.3333% + 8.3333% + 1.0000% + 4.1667% = 21.8333% |
| Nomina Electronica element (col Y) | PILA T2R2-046 to T2R2-073; not a nomina electronica element |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `23672` - Company contribution liability - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Employer contribution / accrual line, computed IN PARALLEL with the employee gross-to-net and never touching net pay. Employer health 8.5%, SENA 2% and ICBF 3% are EXONERATED where the employee earns STRICTLY LESS THAN 10 SMMLV (17,509,050) and the employer is an income-tax-filing legal person (ET art. 114-1); pension 12%, ARL and CCF 4% are never exonerated. Each amount rounds UP to the next multiple of 100. |
| Formula (col F) | Employer-borne contribution liability: health 8.5% + pension 12% + ARL 0.348-8.7% on the IBC; CCF 4% + SENA 2% + ICBF 3% on the Ley 21/1982 levy base (no ceiling); plus the statutory benefit accruals 8.3333% + 8.3333% + 1.0000% + 4.1667% = 21.8333% |
| Nomina Electronica element (col Y) | PILA T2R2-046 to T2R2-073; not a nomina electronica element |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `23673` - Company contribution liability - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Employer contribution / accrual line, computed IN PARALLEL with the employee gross-to-net and never touching net pay. Employer health 8.5%, SENA 2% and ICBF 3% are EXONERATED where the employee earns STRICTLY LESS THAN 10 SMMLV (17,509,050) and the employer is an income-tax-filing legal person (ET art. 114-1); pension 12%, ARL and CCF 4% are never exonerated. Each amount rounds UP to the next multiple of 100. |
| Formula (col F) | Employer-borne contribution liability: health 8.5% + pension 12% + ARL 0.348-8.7% on the IBC; CCF 4% + SENA 2% + ICBF 3% on the Ley 21/1982 levy base (no ceiling); plus the statutory benefit accruals 8.3333% + 8.3333% + 1.0000% + 4.1667% = 21.8333% |
| Nomina Electronica element (col Y) | PILA T2R2-046 to T2R2-073; not a nomina electronica element |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `62100` - Basic salary - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Salario basico - the agreed remuneration for the ordinary working day, by unit of time, task, piece or output (CST art. 132 num. 1). Salary under CST art. 127, so it enters ALL THREE BASES: the IBC (floor 1 SMMLV pro-rated to contributory days, ceiling 25 SMMLV = 43,772,625, rounded UP to the whole peso), the Ley 21/1982 payroll-levy base (NO ceiling), and the ET art. 388 withholding base. Also the base of the statutory benefits and of the CST art. 64 indemnity scale. NOT prorated: the 1-SMMLV contribution-base floor, so a low-paid part-month still contributes on the pro-rated minimum wage. For a NON-RESIDENT this is withheld at the flat 20% on the gross under ET art. 408 with no depuration (DIAN Concepto 011108 de 2026); the switch to the art. 383 table is prospective from the payment following the 183rd day of presence. |
| Formula (col F) | Salario basico: full month = S; partial month = S x days worked / 30 (30-day commercial month, so February and a 31-day month are both 30 payroll days); minimum 1,750,905/month |
| Nomina Electronica element (col Y) | Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62101` - Arrears - Basic salary - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Salario basico - the agreed remuneration for the ordinary working day, by unit of time, task, piece or output (CST art. 132 num. 1). Salary under CST art. 127, so it enters ALL THREE BASES: the IBC (floor 1 SMMLV pro-rated to contributory days, ceiling 25 SMMLV = 43,772,625, rounded UP to the whole peso), the Ley 21/1982 payroll-levy base (NO ceiling), and the ET art. 388 withholding base. Also the base of the statutory benefits and of the CST art. 64 indemnity scale. NOT prorated: the 1-SMMLV contribution-base floor, so a low-paid part-month still contributes on the pro-rated minimum wage. For a NON-RESIDENT this is withheld at the flat 20% on the gross under ET art. 408 with no depuration (DIAN Concepto 011108 de 2026); the switch to the art. 383 table is prospective from the payment following the 183rd day of presence. |
| Formula (col F) | Salario basico: full month = S; partial month = S x days worked / 30 (30-day commercial month, so February and a 31-day month are both 30 payroll days); minimum 1,750,905/month |
| Nomina Electronica element (col Y) | Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62102` - Adjustment - Basic salary - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Salario basico - the agreed remuneration for the ordinary working day, by unit of time, task, piece or output (CST art. 132 num. 1). Salary under CST art. 127, so it enters ALL THREE BASES: the IBC (floor 1 SMMLV pro-rated to contributory days, ceiling 25 SMMLV = 43,772,625, rounded UP to the whole peso), the Ley 21/1982 payroll-levy base (NO ceiling), and the ET art. 388 withholding base. Also the base of the statutory benefits and of the CST art. 64 indemnity scale. NOT prorated: the 1-SMMLV contribution-base floor, so a low-paid part-month still contributes on the pro-rated minimum wage. For a NON-RESIDENT this is withheld at the flat 20% on the gross under ET art. 408 with no depuration (DIAN Concepto 011108 de 2026); the switch to the art. 383 table is prospective from the payment following the 183rd day of presence. |
| Formula (col F) | Salario basico: full month = S; partial month = S x days worked / 30 (30-day commercial month, so February and a 31-day month are both 30 payroll days); minimum 1,750,905/month |
| Nomina Electronica element (col Y) | Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62103` - Advance - Basic salary - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Salario basico - the agreed remuneration for the ordinary working day, by unit of time, task, piece or output (CST art. 132 num. 1). Salary under CST art. 127, so it enters ALL THREE BASES: the IBC (floor 1 SMMLV pro-rated to contributory days, ceiling 25 SMMLV = 43,772,625, rounded UP to the whole peso), the Ley 21/1982 payroll-levy base (NO ceiling), and the ET art. 388 withholding base. Also the base of the statutory benefits and of the CST art. 64 indemnity scale. NOT prorated: the 1-SMMLV contribution-base floor, so a low-paid part-month still contributes on the pro-rated minimum wage. For a NON-RESIDENT this is withheld at the flat 20% on the gross under ET art. 408 with no depuration (DIAN Concepto 011108 de 2026); the switch to the art. 383 table is prospective from the payment following the 183rd day of presence. |
| Formula (col F) | Salario basico: full month = S; partial month = S x days worked / 30 (30-day commercial month, so February and a 31-day month are both 30 payroll days); minimum 1,750,905/month |
| Nomina Electronica element (col Y) | Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62104` - Basic salary (rate) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Percentage |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Rate driver, not a paid amount. THE HOURLY DIVISOR IS THE SINGLE BIGGEST 2026 CALCULATION CHANGE: the 42-hour week starts on 15 JULY 2026 (Ley 2101 de 2021 art. 3; CST art. 161 as substituted by Ley 2466 de 2025 art. 11), taking the divisor from 220 to 210. A July 2026 payroll spans BOTH divisors and must be split at 15 July. The legacy divisor of 240 is obsolete and understates every premium by about 14.3%. |
| Formula (col F) | Ordinary hour value = monthly salary / D, where D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 (MinTrabajo Circular Externa 101 de 22 septiembre 2025) |
| Nomina Electronica element (col Y) | Derived - feeds every hour-type Pago element |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `62108` - Historic Pay - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Salario basico - the agreed remuneration for the ordinary working day, by unit of time, task, piece or output (CST art. 132 num. 1). Salary under CST art. 127, so it enters ALL THREE BASES: the IBC (floor 1 SMMLV pro-rated to contributory days, ceiling 25 SMMLV = 43,772,625, rounded UP to the whole peso), the Ley 21/1982 payroll-levy base (NO ceiling), and the ET art. 388 withholding base. Also the base of the statutory benefits and of the CST art. 64 indemnity scale. NOT prorated: the 1-SMMLV contribution-base floor, so a low-paid part-month still contributes on the pro-rated minimum wage. For a NON-RESIDENT this is withheld at the flat 20% on the gross under ET art. 408 with no depuration (DIAN Concepto 011108 de 2026); the switch to the art. 383 table is prospective from the payment following the 183rd day of presence. |
| Formula (col F) | Salario basico: full month = S; partial month = S x days worked / 30 (30-day commercial month, so February and a 31-day month are both 30 payroll days); minimum 1,750,905/month |
| Nomina Electronica element (col Y) | Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62109` - Unpaid LOA - Basic salary - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Salario basico - the agreed remuneration for the ordinary working day, by unit of time, task, piece or output (CST art. 132 num. 1). Salary under CST art. 127, so it enters ALL THREE BASES: the IBC (floor 1 SMMLV pro-rated to contributory days, ceiling 25 SMMLV = 43,772,625, rounded UP to the whole peso), the Ley 21/1982 payroll-levy base (NO ceiling), and the ET art. 388 withholding base. Also the base of the statutory benefits and of the CST art. 64 indemnity scale. NOT prorated: the 1-SMMLV contribution-base floor, so a low-paid part-month still contributes on the pro-rated minimum wage. For a NON-RESIDENT this is withheld at the flat 20% on the gross under ET art. 408 with no depuration (DIAN Concepto 011108 de 2026); the switch to the art. 383 table is prospective from the payment following the 183rd day of presence. |
| Formula (col F) | Salario basico: full month = S; partial month = S x days worked / 30 (30-day commercial month, so February and a 31-day month are both 30 payroll days); minimum 1,750,905/month |
| Nomina Electronica element (col Y) | Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62110` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62111` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62112` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62113` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62114` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62115` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62116` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62117` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62118` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62119` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62120` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62121` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62122` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62123` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62124` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62125` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62126` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62127` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62128` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62129` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62130` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62131` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62132` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62133` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62134` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62135` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62136` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62137` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62138` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62139` - Overtime - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Overtime is SALARY by express statutory definition - CST art. 127 lists 'el valor del trabajo suplementario o de las horas extras' - so it is fully in the IBC and fully in the payroll-levy base, and in the prima / cesantias / interest base. IT IS EXCLUDED FROM THE VACATION BASE: CST art. 192 excludes ONLY 'el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras'. Fully taxable - there is no preferential rate and no exempt overtime allowance in Colombia. CST art. 168 num. 4 is critical: each premium 'se produce de manera exclusiva, es decir, sin acumularse con ningun otro', so the night, day-overtime and night-overtime premiums are ALTERNATIVES; only the art. 179 rest-day premium is added to them. Volume limit: 2 hours per day and 12 per week (CST art. 22 of Ley 50 de 1990 as substituted by Ley 2466 de 2025 art. 13), so 56 total weekly hours to 14 July 2026 and 54 from 15 July. Ministry authorisation was abolished by Ley 2466 art. 12 and replaced by a mandatory supplementary-work REGISTER; failure to keep it lets inspectors suspend all overtime for six months. Reported with quantity, start and end time, percentage and amount per hour type. |
| Formula (col F) | Day overtime = (S / D) x 1.25 x H; night overtime = (S / D) x 1.75 x H; on an obligatory rest day add the art. 179 premium (+80% to 30 Jun 2026, +90% from 1 Jul 2026). D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED (NIE074-078), HEN (NIE079-083), HEDDF (NIE089-093), HENDF (NIE099-103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62140` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62141` - Arrears - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62142` - Adjustment - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62143` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62144` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62145` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62146` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62147` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62148` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62149` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62150` - Premium pay (i.e. Shift premium) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | THE NIGHT WINDOW MOVED. CST art. 160 as substituted by Ley 2466 de 2025 art. 10: day work is 06:00-19:00 and night work is 19:00-06:00. Art. 160 par. 2 delayed entry into force by six months from the 25 June 2025 sanction, so the 19:00 boundary has applied SINCE 25 DECEMBER 2025 and governs the whole of 2026 - two extra hours a day now attract the 35% premium compared with the pre-reform 21:00 boundary. The night premium is salary, fully contributory, and UNLIKE overtime it STAYS IN THE VACATION BASE (CST art. 192 excludes only rest-day work and supplementary overtime hours). No night premium and no rest-day premium apply on the 6-hour / 36-hour-week successive shift system (CST arts. 161(d) and 168 num. 1). |
| Formula (col F) | Recargo nocturno = (S / D) x 0.35 x H for hours in the 19:00-06:00 window; rest-day / holiday premium = (S / D) x 0.80 x H to 30 Jun 2026 and x 0.90 from 1 Jul 2026. D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HRN (NIE084-NIE088), HRDDF (NIE094-NIE098), HRNDF (NIE104-NIE108) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62151` - Premium pay (i.e. Shift premium) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | THE NIGHT WINDOW MOVED. CST art. 160 as substituted by Ley 2466 de 2025 art. 10: day work is 06:00-19:00 and night work is 19:00-06:00. Art. 160 par. 2 delayed entry into force by six months from the 25 June 2025 sanction, so the 19:00 boundary has applied SINCE 25 DECEMBER 2025 and governs the whole of 2026 - two extra hours a day now attract the 35% premium compared with the pre-reform 21:00 boundary. The night premium is salary, fully contributory, and UNLIKE overtime it STAYS IN THE VACATION BASE (CST art. 192 excludes only rest-day work and supplementary overtime hours). No night premium and no rest-day premium apply on the 6-hour / 36-hour-week successive shift system (CST arts. 161(d) and 168 num. 1). |
| Formula (col F) | Recargo nocturno = (S / D) x 0.35 x H for hours in the 19:00-06:00 window; rest-day / holiday premium = (S / D) x 0.80 x H to 30 Jun 2026 and x 0.90 from 1 Jul 2026. D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HRN (NIE084-NIE088), HRDDF (NIE094-NIE098), HRNDF (NIE104-NIE108) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62152` - Premium pay (i.e. Shift premium) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | THE NIGHT WINDOW MOVED. CST art. 160 as substituted by Ley 2466 de 2025 art. 10: day work is 06:00-19:00 and night work is 19:00-06:00. Art. 160 par. 2 delayed entry into force by six months from the 25 June 2025 sanction, so the 19:00 boundary has applied SINCE 25 DECEMBER 2025 and governs the whole of 2026 - two extra hours a day now attract the 35% premium compared with the pre-reform 21:00 boundary. The night premium is salary, fully contributory, and UNLIKE overtime it STAYS IN THE VACATION BASE (CST art. 192 excludes only rest-day work and supplementary overtime hours). No night premium and no rest-day premium apply on the 6-hour / 36-hour-week successive shift system (CST arts. 161(d) and 168 num. 1). |
| Formula (col F) | Recargo nocturno = (S / D) x 0.35 x H for hours in the 19:00-06:00 window; rest-day / holiday premium = (S / D) x 0.80 x H to 30 Jun 2026 and x 0.90 from 1 Jul 2026. D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HRN (NIE084-NIE088), HRDDF (NIE094-NIE098), HRNDF (NIE104-NIE108) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62153` - Premium pay (i.e. Shift premium) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | THE NIGHT WINDOW MOVED. CST art. 160 as substituted by Ley 2466 de 2025 art. 10: day work is 06:00-19:00 and night work is 19:00-06:00. Art. 160 par. 2 delayed entry into force by six months from the 25 June 2025 sanction, so the 19:00 boundary has applied SINCE 25 DECEMBER 2025 and governs the whole of 2026 - two extra hours a day now attract the 35% premium compared with the pre-reform 21:00 boundary. The night premium is salary, fully contributory, and UNLIKE overtime it STAYS IN THE VACATION BASE (CST art. 192 excludes only rest-day work and supplementary overtime hours). No night premium and no rest-day premium apply on the 6-hour / 36-hour-week successive shift system (CST arts. 161(d) and 168 num. 1). |
| Formula (col F) | Recargo nocturno = (S / D) x 0.35 x H for hours in the 19:00-06:00 window; rest-day / holiday premium = (S / D) x 0.80 x H to 30 Jun 2026 and x 0.90 from 1 Jul 2026. D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HRN (NIE084-NIE088), HRDDF (NIE094-NIE098), HRNDF (NIE104-NIE108) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62154` - Premium pay (i.e. Shift premium) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | THE NIGHT WINDOW MOVED. CST art. 160 as substituted by Ley 2466 de 2025 art. 10: day work is 06:00-19:00 and night work is 19:00-06:00. Art. 160 par. 2 delayed entry into force by six months from the 25 June 2025 sanction, so the 19:00 boundary has applied SINCE 25 DECEMBER 2025 and governs the whole of 2026 - two extra hours a day now attract the 35% premium compared with the pre-reform 21:00 boundary. The night premium is salary, fully contributory, and UNLIKE overtime it STAYS IN THE VACATION BASE (CST art. 192 excludes only rest-day work and supplementary overtime hours). No night premium and no rest-day premium apply on the 6-hour / 36-hour-week successive shift system (CST arts. 161(d) and 168 num. 1). |
| Formula (col F) | Recargo nocturno = (S / D) x 0.35 x H for hours in the 19:00-06:00 window; rest-day / holiday premium = (S / D) x 0.80 x H to 30 Jun 2026 and x 0.90 from 1 Jul 2026. D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HRN (NIE084-NIE088), HRDDF (NIE094-NIE098), HRNDF (NIE104-NIE108) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62155` - Premium pay (i.e. Shift premium) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | THE NIGHT WINDOW MOVED. CST art. 160 as substituted by Ley 2466 de 2025 art. 10: day work is 06:00-19:00 and night work is 19:00-06:00. Art. 160 par. 2 delayed entry into force by six months from the 25 June 2025 sanction, so the 19:00 boundary has applied SINCE 25 DECEMBER 2025 and governs the whole of 2026 - two extra hours a day now attract the 35% premium compared with the pre-reform 21:00 boundary. The night premium is salary, fully contributory, and UNLIKE overtime it STAYS IN THE VACATION BASE (CST art. 192 excludes only rest-day work and supplementary overtime hours). No night premium and no rest-day premium apply on the 6-hour / 36-hour-week successive shift system (CST arts. 161(d) and 168 num. 1). |
| Formula (col F) | Recargo nocturno = (S / D) x 0.35 x H for hours in the 19:00-06:00 window; rest-day / holiday premium = (S / D) x 0.80 x H to 30 Jun 2026 and x 0.90 from 1 Jul 2026. D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HRN (NIE084-NIE088), HRDDF (NIE094-NIE098), HRNDF (NIE104-NIE108) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62160` - Holiday Allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | There is NO statutory vacation bonus in Colombia - only the 15 working days of paid vacation and the prima de servicios. An extra-statutory prima de vacaciones is contractual: SALARY where it is habitual (CST art. 127 'primas, sobresueldos, bonificaciones habituales'), and therefore contributory and in every base, UNLESS the parties have expressly agreed IN WRITING that it does not constitute salary under art. 128, in which case reclassify to CO-BONIF-NOSALARIAL. Configured here as the conservative default - salary. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Prima de vacaciones extralegal - a contractual amount paid on taking leave (commonly a proportion of one month's salary); no statutory entitlement exists |
| Nomina Electronica element (col Y) | Devengados / Primas - PagoNS (NIE119) or Bonificacion (NIE139 / NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62161` - Arrears - Holiday Allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | There is NO statutory vacation bonus in Colombia - only the 15 working days of paid vacation and the prima de servicios. An extra-statutory prima de vacaciones is contractual: SALARY where it is habitual (CST art. 127 'primas, sobresueldos, bonificaciones habituales'), and therefore contributory and in every base, UNLESS the parties have expressly agreed IN WRITING that it does not constitute salary under art. 128, in which case reclassify to CO-BONIF-NOSALARIAL. Configured here as the conservative default - salary. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Prima de vacaciones extralegal - a contractual amount paid on taking leave (commonly a proportion of one month's salary); no statutory entitlement exists |
| Nomina Electronica element (col Y) | Devengados / Primas - PagoNS (NIE119) or Bonificacion (NIE139 / NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62162` - Adjustment - Holiday Allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | There is NO statutory vacation bonus in Colombia - only the 15 working days of paid vacation and the prima de servicios. An extra-statutory prima de vacaciones is contractual: SALARY where it is habitual (CST art. 127 'primas, sobresueldos, bonificaciones habituales'), and therefore contributory and in every base, UNLESS the parties have expressly agreed IN WRITING that it does not constitute salary under art. 128, in which case reclassify to CO-BONIF-NOSALARIAL. Configured here as the conservative default - salary. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Prima de vacaciones extralegal - a contractual amount paid on taking leave (commonly a proportion of one month's salary); no statutory entitlement exists |
| Nomina Electronica element (col Y) | Devengados / Primas - PagoNS (NIE119) or Bonificacion (NIE139 / NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62170` - On-call duty - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | On-call / standby remuneration is direct consideration for the service, so SALARY under CST art. 127, entering the IBC, the payroll-levy base, the statutory-benefit base and the vacation base, and fully taxable. Colombia has no statutory on-call rate - the amount is contractual. Hours actually worked during the on-call window attract the ordinary, night, overtime or rest-day treatment on their own facts. |
| Formula (col F) | Recargo por disponibilidad / astreinte per contract or collective agreement; hours actually worked while on call are paid as ordinary or overtime hours with their own premia |
| Nomina Electronica element (col Y) | Devengados / OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62171` - Arrears - On-call duty - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | On-call / standby remuneration is direct consideration for the service, so SALARY under CST art. 127, entering the IBC, the payroll-levy base, the statutory-benefit base and the vacation base, and fully taxable. Colombia has no statutory on-call rate - the amount is contractual. Hours actually worked during the on-call window attract the ordinary, night, overtime or rest-day treatment on their own facts. |
| Formula (col F) | Recargo por disponibilidad / astreinte per contract or collective agreement; hours actually worked while on call are paid as ordinary or overtime hours with their own premia |
| Nomina Electronica element (col Y) | Devengados / OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62172` - Adjustment - On-call duty - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | On-call / standby remuneration is direct consideration for the service, so SALARY under CST art. 127, entering the IBC, the payroll-levy base, the statutory-benefit base and the vacation base, and fully taxable. Colombia has no statutory on-call rate - the amount is contractual. Hours actually worked during the on-call window attract the ordinary, night, overtime or rest-day treatment on their own facts. |
| Formula (col F) | Recargo por disponibilidad / astreinte per contract or collective agreement; hours actually worked while on call are paid as ordinary or overtime hours with their own premia |
| Nomina Electronica element (col Y) | Devengados / OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62180` - Severance & Seniority - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-02 |
| Wage Type Explanation (col D) | Cesantias and the interest on them are STATUTORY BENEFITS excluded from salary by CST art. 128, so out of the IBC and out of the payroll-levy base. They are EXCLUDED FROM THE MONTHLY WITHHOLDING BASE ENTIRELY under BOTH procedures (ET arts. 385 and 386) - not merely exempt - and the ET art. 206 num. 4 exemption is applied when the payment is made: exempt in full where the average monthly income of the last 6 months is <= 350 UVT (18,330,900), then tapering 90/80/60/40/20/0%. The 25% exemption of art. 206 num. 10 does NOT apply (art. 206 par. 2). Liquidated at 31 December and DEPOSITED TO THE EMPLOYEE'S FUND BY 14 FEBRUARY; late deposit costs one day's salary per day of delay. The interest is paid TO THE EMPLOYEE during January, not to the fund. Ley 2466 de 2025 art. 64 permits an 8.33% monthly advance deposit by agreement. |
| Formula (col F) | Auxilio de cesantias = (monthly salary + auxilio de transporte) x days of service / 360; interest = cesantias balance x 12% x days / 360 |
| Nomina Electronica element (col Y) | Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122) |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 4 and par. 2, 385, 386; Ley 50 de 1990 art. 99; Ley 52 de 1975 art. 1; Ley 2466 de 2025 art. 64 (8.33% monthly advance deposit). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62181` - Severance & Seniority - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-02 |
| Wage Type Explanation (col D) | Cesantias and the interest on them are STATUTORY BENEFITS excluded from salary by CST art. 128, so out of the IBC and out of the payroll-levy base. They are EXCLUDED FROM THE MONTHLY WITHHOLDING BASE ENTIRELY under BOTH procedures (ET arts. 385 and 386) - not merely exempt - and the ET art. 206 num. 4 exemption is applied when the payment is made: exempt in full where the average monthly income of the last 6 months is <= 350 UVT (18,330,900), then tapering 90/80/60/40/20/0%. The 25% exemption of art. 206 num. 10 does NOT apply (art. 206 par. 2). Liquidated at 31 December and DEPOSITED TO THE EMPLOYEE'S FUND BY 14 FEBRUARY; late deposit costs one day's salary per day of delay. The interest is paid TO THE EMPLOYEE during January, not to the fund. Ley 2466 de 2025 art. 64 permits an 8.33% monthly advance deposit by agreement. |
| Formula (col F) | Auxilio de cesantias = (monthly salary + auxilio de transporte) x days of service / 360; interest = cesantias balance x 12% x days / 360 |
| Nomina Electronica element (col Y) | Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122) |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 4 and par. 2, 385, 386; Ley 50 de 1990 art. 99; Ley 52 de 1975 art. 1; Ley 2466 de 2025 art. 64 (8.33% monthly advance deposit). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62182` - Severance & Seniority - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-02 |
| Wage Type Explanation (col D) | Cesantias and the interest on them are STATUTORY BENEFITS excluded from salary by CST art. 128, so out of the IBC and out of the payroll-levy base. They are EXCLUDED FROM THE MONTHLY WITHHOLDING BASE ENTIRELY under BOTH procedures (ET arts. 385 and 386) - not merely exempt - and the ET art. 206 num. 4 exemption is applied when the payment is made: exempt in full where the average monthly income of the last 6 months is <= 350 UVT (18,330,900), then tapering 90/80/60/40/20/0%. The 25% exemption of art. 206 num. 10 does NOT apply (art. 206 par. 2). Liquidated at 31 December and DEPOSITED TO THE EMPLOYEE'S FUND BY 14 FEBRUARY; late deposit costs one day's salary per day of delay. The interest is paid TO THE EMPLOYEE during January, not to the fund. Ley 2466 de 2025 art. 64 permits an 8.33% monthly advance deposit by agreement. |
| Formula (col F) | Auxilio de cesantias = (monthly salary + auxilio de transporte) x days of service / 360; interest = cesantias balance x 12% x days / 360 |
| Nomina Electronica element (col Y) | Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122) |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 4 and par. 2, 385, 386; Ley 50 de 1990 art. 99; Ley 52 de 1975 art. 1; Ley 2466 de 2025 art. 64 (8.33% monthly advance deposit). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62190` - Long Term Disability - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An employer-paid top-up is taxable and fully contributory (it is an employer payment in consideration of the relationship). The CERTIFIED BENEFIT ITSELF is paid by the EPS to day 180 (66.67% to day 90, 50% days 91-180) and thereafter by the pension administrator, is exempt within the statutory minimum (ET art. 206 nums. 1-2 and par. 1), and contributions CONTINUE on the base throughout (PILA change event IGE). Occupational incapacity is paid by the ARL at 100% of the IBC from the day after the event (change event IRL). |
| Formula (col F) | Employer-paid disability top-up beyond the certified EPS or pension-administrator benefit |
| Nomina Electronica element (col Y) | Devengados / Incapacidad - Tipo (NIE126), Pago (NIE127) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62200` - Bonus (annual, referral, etc) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Non-statutory bonuses are entirely contractual. They are SALARY if habitual - CST art. 127 expressly lists 'primas, sobresueldos, bonificaciones habituales' - and therefore contributory and in every base, UNLESS the parties have expressly agreed in writing that they do not constitute salary, subject always to the 40% clamp. Configured here as the conservative default - salary. Tax: no preferential bonus rate, no separate annualisation and no tax-free bonus allowance exists; the bonus enters the ordinary monthly base under both procedures (only the STATUTORY MINIMUM prima de servicios gets the separate art. 385 table read). A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Contractual bonus (performance, sign-on, retention, referral) per the scheme; SALARY where habitual, non-salary only under an express written CST art. 128 pact |
| Nomina Electronica element (col Y) | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62201` - Bonus (annual, referral, etc) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Non-statutory bonuses are entirely contractual. They are SALARY if habitual - CST art. 127 expressly lists 'primas, sobresueldos, bonificaciones habituales' - and therefore contributory and in every base, UNLESS the parties have expressly agreed in writing that they do not constitute salary, subject always to the 40% clamp. Configured here as the conservative default - salary. Tax: no preferential bonus rate, no separate annualisation and no tax-free bonus allowance exists; the bonus enters the ordinary monthly base under both procedures (only the STATUTORY MINIMUM prima de servicios gets the separate art. 385 table read). A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Contractual bonus (performance, sign-on, retention, referral) per the scheme; SALARY where habitual, non-salary only under an express written CST art. 128 pact |
| Nomina Electronica element (col Y) | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62202` - Bonus (annual, referral, etc) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Non-statutory bonuses are entirely contractual. They are SALARY if habitual - CST art. 127 expressly lists 'primas, sobresueldos, bonificaciones habituales' - and therefore contributory and in every base, UNLESS the parties have expressly agreed in writing that they do not constitute salary, subject always to the 40% clamp. Configured here as the conservative default - salary. Tax: no preferential bonus rate, no separate annualisation and no tax-free bonus allowance exists; the bonus enters the ordinary monthly base under both procedures (only the STATUTORY MINIMUM prima de servicios gets the separate art. 385 table read). A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Contractual bonus (performance, sign-on, retention, referral) per the scheme; SALARY where habitual, non-salary only under an express written CST art. 128 pact |
| Nomina Electronica element (col Y) | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62203` - Bonus (annual, referral, etc) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Non-statutory bonuses are entirely contractual. They are SALARY if habitual - CST art. 127 expressly lists 'primas, sobresueldos, bonificaciones habituales' - and therefore contributory and in every base, UNLESS the parties have expressly agreed in writing that they do not constitute salary, subject always to the 40% clamp. Configured here as the conservative default - salary. Tax: no preferential bonus rate, no separate annualisation and no tax-free bonus allowance exists; the bonus enters the ordinary monthly base under both procedures (only the STATUTORY MINIMUM prima de servicios gets the separate art. 385 table read). A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Contractual bonus (performance, sign-on, retention, referral) per the scheme; SALARY where habitual, non-salary only under an express written CST art. 128 pact |
| Nomina Electronica element (col Y) | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62204` - Bonus (annual, referral, etc) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Non-statutory bonuses are entirely contractual. They are SALARY if habitual - CST art. 127 expressly lists 'primas, sobresueldos, bonificaciones habituales' - and therefore contributory and in every base, UNLESS the parties have expressly agreed in writing that they do not constitute salary, subject always to the 40% clamp. Configured here as the conservative default - salary. Tax: no preferential bonus rate, no separate annualisation and no tax-free bonus allowance exists; the bonus enters the ordinary monthly base under both procedures (only the STATUTORY MINIMUM prima de servicios gets the separate art. 385 table read). A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Contractual bonus (performance, sign-on, retention, referral) per the scheme; SALARY where habitual, non-salary only under an express written CST art. 128 pact |
| Nomina Electronica element (col Y) | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62205` - Bonus (annual, referral, etc) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Non-statutory bonuses are entirely contractual. They are SALARY if habitual - CST art. 127 expressly lists 'primas, sobresueldos, bonificaciones habituales' - and therefore contributory and in every base, UNLESS the parties have expressly agreed in writing that they do not constitute salary, subject always to the 40% clamp. Configured here as the conservative default - salary. Tax: no preferential bonus rate, no separate annualisation and no tax-free bonus allowance exists; the bonus enters the ordinary monthly base under both procedures (only the STATUTORY MINIMUM prima de servicios gets the separate art. 385 table read). A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Contractual bonus (performance, sign-on, retention, referral) per the scheme; SALARY where habitual, non-salary only under an express written CST art. 128 pact |
| Nomina Electronica element (col Y) | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62206` - Bonus (annual, referral, etc) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Non-statutory bonuses are entirely contractual. They are SALARY if habitual - CST art. 127 expressly lists 'primas, sobresueldos, bonificaciones habituales' - and therefore contributory and in every base, UNLESS the parties have expressly agreed in writing that they do not constitute salary, subject always to the 40% clamp. Configured here as the conservative default - salary. Tax: no preferential bonus rate, no separate annualisation and no tax-free bonus allowance exists; the bonus enters the ordinary monthly base under both procedures (only the STATUTORY MINIMUM prima de servicios gets the separate art. 385 table read). A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Contractual bonus (performance, sign-on, retention, referral) per the scheme; SALARY where habitual, non-salary only under an express written CST art. 128 pact |
| Nomina Electronica element (col Y) | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62207` - Bonus (annual, referral, etc) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Non-statutory bonuses are entirely contractual. They are SALARY if habitual - CST art. 127 expressly lists 'primas, sobresueldos, bonificaciones habituales' - and therefore contributory and in every base, UNLESS the parties have expressly agreed in writing that they do not constitute salary, subject always to the 40% clamp. Configured here as the conservative default - salary. Tax: no preferential bonus rate, no separate annualisation and no tax-free bonus allowance exists; the bonus enters the ordinary monthly base under both procedures (only the STATUTORY MINIMUM prima de servicios gets the separate art. 385 table read). A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Contractual bonus (performance, sign-on, retention, referral) per the scheme; SALARY where habitual, non-salary only under an express written CST art. 128 pact |
| Nomina Electronica element (col Y) | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62208` - Bonus (annual, referral, etc) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Non-statutory bonuses are entirely contractual. They are SALARY if habitual - CST art. 127 expressly lists 'primas, sobresueldos, bonificaciones habituales' - and therefore contributory and in every base, UNLESS the parties have expressly agreed in writing that they do not constitute salary, subject always to the 40% clamp. Configured here as the conservative default - salary. Tax: no preferential bonus rate, no separate annualisation and no tax-free bonus allowance exists; the bonus enters the ordinary monthly base under both procedures (only the STATUTORY MINIMUM prima de servicios gets the separate art. 385 table read). A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Contractual bonus (performance, sign-on, retention, referral) per the scheme; SALARY where habitual, non-salary only under an express written CST art. 128 pact |
| Nomina Electronica element (col Y) | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62209` - Bonus (annual, referral, etc) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Non-statutory bonuses are entirely contractual. They are SALARY if habitual - CST art. 127 expressly lists 'primas, sobresueldos, bonificaciones habituales' - and therefore contributory and in every base, UNLESS the parties have expressly agreed in writing that they do not constitute salary, subject always to the 40% clamp. Configured here as the conservative default - salary. Tax: no preferential bonus rate, no separate annualisation and no tax-free bonus allowance exists; the bonus enters the ordinary monthly base under both procedures (only the STATUTORY MINIMUM prima de servicios gets the separate art. 385 table read). A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Contractual bonus (performance, sign-on, retention, referral) per the scheme; SALARY where habitual, non-salary only under an express written CST art. 128 pact |
| Nomina Electronica element (col Y) | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62210` - Bonus - profit sharing - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 128 expressly excludes 'la participacion de utilidades' and solidarity-economy surpluses from salary, so profit sharing is out of the statutory-benefit and vacation bases - but it is FULLY TAXABLE employment income and, as a 'pago laboral no constitutivo de salario', it counts in the Ley 1393 de 2010 art. 30 40% clamp test. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Participacion de utilidades / excedentes per the company scheme; no statutory profit-sharing entitlement exists in Colombia |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62211` - Bonus - profit sharing - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 128 expressly excludes 'la participacion de utilidades' and solidarity-economy surpluses from salary, so profit sharing is out of the statutory-benefit and vacation bases - but it is FULLY TAXABLE employment income and, as a 'pago laboral no constitutivo de salario', it counts in the Ley 1393 de 2010 art. 30 40% clamp test. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Participacion de utilidades / excedentes per the company scheme; no statutory profit-sharing entitlement exists in Colombia |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62212` - Bonus - profit sharing - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 128 expressly excludes 'la participacion de utilidades' and solidarity-economy surpluses from salary, so profit sharing is out of the statutory-benefit and vacation bases - but it is FULLY TAXABLE employment income and, as a 'pago laboral no constitutivo de salario', it counts in the Ley 1393 de 2010 art. 30 40% clamp test. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Participacion de utilidades / excedentes per the company scheme; no statutory profit-sharing entitlement exists in Colombia |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62213` - Bonus - profit sharing - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 128 expressly excludes 'la participacion de utilidades' and solidarity-economy surpluses from salary, so profit sharing is out of the statutory-benefit and vacation bases - but it is FULLY TAXABLE employment income and, as a 'pago laboral no constitutivo de salario', it counts in the Ley 1393 de 2010 art. 30 40% clamp test. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Participacion de utilidades / excedentes per the company scheme; no statutory profit-sharing entitlement exists in Colombia |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62214` - Bonus - profit sharing - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 128 expressly excludes 'la participacion de utilidades' and solidarity-economy surpluses from salary, so profit sharing is out of the statutory-benefit and vacation bases - but it is FULLY TAXABLE employment income and, as a 'pago laboral no constitutivo de salario', it counts in the Ley 1393 de 2010 art. 30 40% clamp test. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Participacion de utilidades / excedentes per the company scheme; no statutory profit-sharing entitlement exists in Colombia |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62215` - Bonus - profit sharing - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 128 expressly excludes 'la participacion de utilidades' and solidarity-economy surpluses from salary, so profit sharing is out of the statutory-benefit and vacation bases - but it is FULLY TAXABLE employment income and, as a 'pago laboral no constitutivo de salario', it counts in the Ley 1393 de 2010 art. 30 40% clamp test. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Participacion de utilidades / excedentes per the company scheme; no statutory profit-sharing entitlement exists in Colombia |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62216` - Bonus - profit sharing - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 128 expressly excludes 'la participacion de utilidades' and solidarity-economy surpluses from salary, so profit sharing is out of the statutory-benefit and vacation bases - but it is FULLY TAXABLE employment income and, as a 'pago laboral no constitutivo de salario', it counts in the Ley 1393 de 2010 art. 30 40% clamp test. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Participacion de utilidades / excedentes per the company scheme; no statutory profit-sharing entitlement exists in Colombia |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62217` - Bonus - profit sharing - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 128 expressly excludes 'la participacion de utilidades' and solidarity-economy surpluses from salary, so profit sharing is out of the statutory-benefit and vacation bases - but it is FULLY TAXABLE employment income and, as a 'pago laboral no constitutivo de salario', it counts in the Ley 1393 de 2010 art. 30 40% clamp test. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Participacion de utilidades / excedentes per the company scheme; no statutory profit-sharing entitlement exists in Colombia |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62218` - Bonus - profit sharing - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 128 expressly excludes 'la participacion de utilidades' and solidarity-economy surpluses from salary, so profit sharing is out of the statutory-benefit and vacation bases - but it is FULLY TAXABLE employment income and, as a 'pago laboral no constitutivo de salario', it counts in the Ley 1393 de 2010 art. 30 40% clamp test. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Participacion de utilidades / excedentes per the company scheme; no statutory profit-sharing entitlement exists in Colombia |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62219` - Bonus - profit sharing - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 128 expressly excludes 'la participacion de utilidades' and solidarity-economy surpluses from salary, so profit sharing is out of the statutory-benefit and vacation bases - but it is FULLY TAXABLE employment income and, as a 'pago laboral no constitutivo de salario', it counts in the Ley 1393 de 2010 art. 30 40% clamp test. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Participacion de utilidades / excedentes per the company scheme; no statutory profit-sharing entitlement exists in Colombia |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62220` - Bonuses - discretionary or one-time - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An occasional and purely gratuitous sum is excluded from salary by CST art. 128 num. 1, so out of the statutory-benefit and vacation bases, but FULLY TAXABLE. THE HABITUALITY TEST IS THE RISK: CST art. 127 brings 'bonificaciones habituales' INTO salary, and a payment repeated year on year will not survive a UGPP contribution audit as occasional. Where the payment is habitual but the parties have an EXPRESS WRITTEN art. 128 pact, use CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | One-off discretionary amount (mera liberalidad), not habitual and not contractually owed |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62221` - Bonuses - discretionary or one-time - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An occasional and purely gratuitous sum is excluded from salary by CST art. 128 num. 1, so out of the statutory-benefit and vacation bases, but FULLY TAXABLE. THE HABITUALITY TEST IS THE RISK: CST art. 127 brings 'bonificaciones habituales' INTO salary, and a payment repeated year on year will not survive a UGPP contribution audit as occasional. Where the payment is habitual but the parties have an EXPRESS WRITTEN art. 128 pact, use CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | One-off discretionary amount (mera liberalidad), not habitual and not contractually owed |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62222` - Bonuses - discretionary or one-time - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An occasional and purely gratuitous sum is excluded from salary by CST art. 128 num. 1, so out of the statutory-benefit and vacation bases, but FULLY TAXABLE. THE HABITUALITY TEST IS THE RISK: CST art. 127 brings 'bonificaciones habituales' INTO salary, and a payment repeated year on year will not survive a UGPP contribution audit as occasional. Where the payment is habitual but the parties have an EXPRESS WRITTEN art. 128 pact, use CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | One-off discretionary amount (mera liberalidad), not habitual and not contractually owed |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62223` - Bonuses - discretionary or one-time - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An occasional and purely gratuitous sum is excluded from salary by CST art. 128 num. 1, so out of the statutory-benefit and vacation bases, but FULLY TAXABLE. THE HABITUALITY TEST IS THE RISK: CST art. 127 brings 'bonificaciones habituales' INTO salary, and a payment repeated year on year will not survive a UGPP contribution audit as occasional. Where the payment is habitual but the parties have an EXPRESS WRITTEN art. 128 pact, use CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | One-off discretionary amount (mera liberalidad), not habitual and not contractually owed |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62224` - Bonuses - discretionary or one-time - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An occasional and purely gratuitous sum is excluded from salary by CST art. 128 num. 1, so out of the statutory-benefit and vacation bases, but FULLY TAXABLE. THE HABITUALITY TEST IS THE RISK: CST art. 127 brings 'bonificaciones habituales' INTO salary, and a payment repeated year on year will not survive a UGPP contribution audit as occasional. Where the payment is habitual but the parties have an EXPRESS WRITTEN art. 128 pact, use CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | One-off discretionary amount (mera liberalidad), not habitual and not contractually owed |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62225` - Bonuses - discretionary or one-time - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An occasional and purely gratuitous sum is excluded from salary by CST art. 128 num. 1, so out of the statutory-benefit and vacation bases, but FULLY TAXABLE. THE HABITUALITY TEST IS THE RISK: CST art. 127 brings 'bonificaciones habituales' INTO salary, and a payment repeated year on year will not survive a UGPP contribution audit as occasional. Where the payment is habitual but the parties have an EXPRESS WRITTEN art. 128 pact, use CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | One-off discretionary amount (mera liberalidad), not habitual and not contractually owed |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62226` - Bonuses - discretionary or one-time - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An occasional and purely gratuitous sum is excluded from salary by CST art. 128 num. 1, so out of the statutory-benefit and vacation bases, but FULLY TAXABLE. THE HABITUALITY TEST IS THE RISK: CST art. 127 brings 'bonificaciones habituales' INTO salary, and a payment repeated year on year will not survive a UGPP contribution audit as occasional. Where the payment is habitual but the parties have an EXPRESS WRITTEN art. 128 pact, use CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | One-off discretionary amount (mera liberalidad), not habitual and not contractually owed |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62227` - Bonuses - discretionary or one-time - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An occasional and purely gratuitous sum is excluded from salary by CST art. 128 num. 1, so out of the statutory-benefit and vacation bases, but FULLY TAXABLE. THE HABITUALITY TEST IS THE RISK: CST art. 127 brings 'bonificaciones habituales' INTO salary, and a payment repeated year on year will not survive a UGPP contribution audit as occasional. Where the payment is habitual but the parties have an EXPRESS WRITTEN art. 128 pact, use CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | One-off discretionary amount (mera liberalidad), not habitual and not contractually owed |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62228` - Bonuses - discretionary or one-time - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An occasional and purely gratuitous sum is excluded from salary by CST art. 128 num. 1, so out of the statutory-benefit and vacation bases, but FULLY TAXABLE. THE HABITUALITY TEST IS THE RISK: CST art. 127 brings 'bonificaciones habituales' INTO salary, and a payment repeated year on year will not survive a UGPP contribution audit as occasional. Where the payment is habitual but the parties have an EXPRESS WRITTEN art. 128 pact, use CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | One-off discretionary amount (mera liberalidad), not habitual and not contractually owed |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62229` - Bonuses - discretionary or one-time - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An occasional and purely gratuitous sum is excluded from salary by CST art. 128 num. 1, so out of the statutory-benefit and vacation bases, but FULLY TAXABLE. THE HABITUALITY TEST IS THE RISK: CST art. 127 brings 'bonificaciones habituales' INTO salary, and a payment repeated year on year will not survive a UGPP contribution audit as occasional. Where the payment is habitual but the parties have an EXPRESS WRITTEN art. 128 pact, use CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | One-off discretionary amount (mera liberalidad), not habitual and not contractually owed |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62300` - Annual leave pay - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | VACATION IS NOT A STATUTORY BENEFIT - IT IS PAID REST, and the consequences are counter-intuitive and must be configured deliberately. Vacation pay ENTERS THE IBC (contributions continue during leave, PILA change event VAC/LR) and ENTERS THE PAYROLL-LEVY BASE, because Ley 21 de 1982 art. 17 expressly covers 'los verificados por descansos remunerados de ley y convencionales o contractuales'. Its own calculation base excludes overtime and rest-day work ONLY (CST art. 192), so the night premium and commissions STAY IN. The auxilio de transporte is NOT in the vacation base. An ALL-INCLUSIVE SALARY DOES NOT ABSORB VACATION (CST art. 132 num. 2 expressly excepts it), so vacation is owed on the FULL 100% while contributions run on 70%. Fully taxable. |
| Formula (col F) | Vacaciones = (ordinary salary EXCLUDING overtime and rest-day work) x working days of vacation / 30; variable pay -> average of the immediately preceding year; accrual 15 working days / 360 |
| Nomina Electronica element (col Y) | Devengados / VacacionesComunes (NIE109-NIE112) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62302` - Adjustment - Annual leave pay - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | VACATION IS NOT A STATUTORY BENEFIT - IT IS PAID REST, and the consequences are counter-intuitive and must be configured deliberately. Vacation pay ENTERS THE IBC (contributions continue during leave, PILA change event VAC/LR) and ENTERS THE PAYROLL-LEVY BASE, because Ley 21 de 1982 art. 17 expressly covers 'los verificados por descansos remunerados de ley y convencionales o contractuales'. Its own calculation base excludes overtime and rest-day work ONLY (CST art. 192), so the night premium and commissions STAY IN. The auxilio de transporte is NOT in the vacation base. An ALL-INCLUSIVE SALARY DOES NOT ABSORB VACATION (CST art. 132 num. 2 expressly excepts it), so vacation is owed on the FULL 100% while contributions run on 70%. Fully taxable. |
| Formula (col F) | Vacaciones = (ordinary salary EXCLUDING overtime and rest-day work) x working days of vacation / 30; variable pay -> average of the immediately preceding year; accrual 15 working days / 360 |
| Nomina Electronica element (col Y) | Devengados / VacacionesComunes (NIE109-NIE112) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62305` - Annual leave payout - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | VACATION IS NOT A STATUTORY BENEFIT - IT IS PAID REST, and the consequences are counter-intuitive and must be configured deliberately. Vacation pay ENTERS THE IBC (contributions continue during leave, PILA change event VAC/LR) and ENTERS THE PAYROLL-LEVY BASE, because Ley 21 de 1982 art. 17 expressly covers 'los verificados por descansos remunerados de ley y convencionales o contractuales'. Its own calculation base excludes overtime and rest-day work ONLY (CST art. 192), so the night premium and commissions STAY IN. The auxilio de transporte is NOT in the vacation base. An ALL-INCLUSIVE SALARY DOES NOT ABSORB VACATION (CST art. 132 num. 2 expressly excepts it), so vacation is owed on the FULL 100% while contributions run on 70%. Fully taxable. |
| Formula (col F) | Compensacion en dinero de vacaciones - up to HALF the accrued leave, on the employee's PRIOR WRITTEN request (CST art. 189 num. 1) |
| Nomina Electronica element (col Y) | Devengados / VacacionesCompensadas (NIE115, NIE116) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62310` - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62311` - Arrears - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62312` - Adjustment - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62320` - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62321` - Arrears - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62322` - Adjustment - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62330` - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62331` - Arrears - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62332` - Adjustment - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62334` - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62335` - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62340` - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62341` - Arrears - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62342` - Adjustment - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62350` - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62351` - Arrears - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62352` - Adjustment - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62360` - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62361` - Arrears - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62362` - Adjustment - Expat allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia applies NO separate expatriate contribution regime: a resident or non-resident foreign national employed under a Colombian contract carries FULL health, pension, occupational-risk and levy obligations at the ordinary rates. THE ONE DIVERGENCE IS TAX, AND IT IS THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: until tax residence is acquired the withholding is a FLAT 20% ON THE GROSS under ET art. 408 with no depuration, no 25% exemption and no tax-free band, switching PROSPECTIVELY to the art. 383 table from the payment following the 183rd day of presence (DIAN Concepto 011108 de 29 junio 2026, which rejected applying art. 383 from day one in anticipation of residence). On COP 8,000,000 that is COP 1,600,000 of withholding against COP 92,049 for a resident - a 17-fold difference. ONE PENSION RELIEF EXISTS: a foreign employee who PROVES affiliation to a pension system abroad may opt out of Colombian pension affiliation on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). |
| Formula (col F) | Expatriate / assignment allowance per the assignment letter; taxable and contributory on the same rates as a local employee |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62400` - Housing allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62401` - Arrears - Housing allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62402` - Adjustment - Housing allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62403` - Advance - Housing allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62410` - Housing allowance 2 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62411` - Arrears - Housing allowance 2 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62412` - Adjustment - Housing allowance 2 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62420` - Housing allowance 3 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62421` - Arrears - Housing allowance 3 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62422` - Adjustment - Housing allowance 3 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62430` - Housing & Rent allowance 1 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62431` - Arrears - Housing & Rent allowance 1 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62432` - Adjustment - Housing & Rent allowance 1 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62440` - Housing & Rent allowance 2 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62441` - Arrears - Housing & Rent allowance 2 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62450` - Housing & Rent allowance 3 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62451` - Arrears - Housing & Rent allowance 3 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62460` - Housing & Rent allowance 4 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62470` - Housing & Rent allowance 5 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62471` - Arrears - Housing & Rent allowance 5 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62472` - Adjustment - Housing & Rent allowance 5 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62480` - Housing & Rent allowance 6 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62481` - Arrears - Housing & Rent allowance 6 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62482` - Adjustment - Housing & Rent allowance 6 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A cash housing allowance is ordinary salary under CST art. 127 and enters every base. Housing supplied IN KIND is salary in kind under art. 129 - 'alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia' - which 'debe valorarse expresamente en todo contrato de trabajo', with expert appraisal in default of agreement, and which may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage. Where the parties have an EXPRESS WRITTEN art. 128 non-salary pact over housing, reclassify to CO-BONIF-NOSALARIAL. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash housing / rent allowance per contract; employer-provided housing in kind is salary in kind valued contractually, capped at 50% of total salary (30% at the SMMLV) |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62500` - Car allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Cash car, fuel and maintenance allowances are ordinary salary (CST art. 127) and enter the IBC, the payroll-levy base, the statutory-benefit base and the vacation base. A COMPANY CAR provided in kind for private use is instead salary in kind under art. 129, valued CONTRACTUALLY - Colombia has NO published company-car valuation scale, and art. 129 num. 2 routes an unvalued benefit to expert appraisal (estimacion pericial), not to a table. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash car / fuel / maintenance allowance per contract |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62501` - Arrears - Car allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Cash car, fuel and maintenance allowances are ordinary salary (CST art. 127) and enter the IBC, the payroll-levy base, the statutory-benefit base and the vacation base. A COMPANY CAR provided in kind for private use is instead salary in kind under art. 129, valued CONTRACTUALLY - Colombia has NO published company-car valuation scale, and art. 129 num. 2 routes an unvalued benefit to expert appraisal (estimacion pericial), not to a table. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash car / fuel / maintenance allowance per contract |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62502` - Adjustment - Car allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Cash car, fuel and maintenance allowances are ordinary salary (CST art. 127) and enter the IBC, the payroll-levy base, the statutory-benefit base and the vacation base. A COMPANY CAR provided in kind for private use is instead salary in kind under art. 129, valued CONTRACTUALLY - Colombia has NO published company-car valuation scale, and art. 129 num. 2 routes an unvalued benefit to expert appraisal (estimacion pericial), not to a table. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash car / fuel / maintenance allowance per contract |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62503` - Advance - Car allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Cash car, fuel and maintenance allowances are ordinary salary (CST art. 127) and enter the IBC, the payroll-levy base, the statutory-benefit base and the vacation base. A COMPANY CAR provided in kind for private use is instead salary in kind under art. 129, valued CONTRACTUALLY - Colombia has NO published company-car valuation scale, and art. 129 num. 2 routes an unvalued benefit to expert appraisal (estimacion pericial), not to a table. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash car / fuel / maintenance allowance per contract |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62504` - Car maintenance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Cash car, fuel and maintenance allowances are ordinary salary (CST art. 127) and enter the IBC, the payroll-levy base, the statutory-benefit base and the vacation base. A COMPANY CAR provided in kind for private use is instead salary in kind under art. 129, valued CONTRACTUALLY - Colombia has NO published company-car valuation scale, and art. 129 num. 2 routes an unvalued benefit to expert appraisal (estimacion pericial), not to a table. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash car / fuel / maintenance allowance per contract |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62505` - Car fuel - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Cash car, fuel and maintenance allowances are ordinary salary (CST art. 127) and enter the IBC, the payroll-levy base, the statutory-benefit base and the vacation base. A COMPANY CAR provided in kind for private use is instead salary in kind under art. 129, valued CONTRACTUALLY - Colombia has NO published company-car valuation scale, and art. 129 num. 2 routes an unvalued benefit to expert appraisal (estimacion pericial), not to a table. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash car / fuel / maintenance allowance per contract |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62510` - Car & Transportation allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | THE COUNTER-INTUITIVE COLOMBIAN LINE. The statutory transport allowance is NOT salary and is therefore OUT of the IBC and OUT of the Ley 21/1982 payroll-levy base - but it IS in the statutory-benefit base, so it enters the prima de servicios, the cesantias and the interest on them. It is NOT in the vacation base. It is taxable income (usually within the 0% band). Not payable for days of unpaid leave, sickness incapacity or maternity / paternity leave. Prorated on the 30-day commercial month. A teleworker earning less than 2 SMMLV receives the auxilio de conectividad INSTEAD, never both (Ley 2466 de 2025 art. 53). |
| Formula (col F) | Auxilio de transporte = 249,095 x days worked / 30, where the employee earns up to 2 SMMLV (3,501,810) and public transport is available (Decreto 1470 de 2025 art. 1) |
| Nomina Electronica element (col Y) | Devengados / Transporte - AuxilioTransporte (NIE071) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62511` - Arrears - Car & Transportation allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | THE COUNTER-INTUITIVE COLOMBIAN LINE. The statutory transport allowance is NOT salary and is therefore OUT of the IBC and OUT of the Ley 21/1982 payroll-levy base - but it IS in the statutory-benefit base, so it enters the prima de servicios, the cesantias and the interest on them. It is NOT in the vacation base. It is taxable income (usually within the 0% band). Not payable for days of unpaid leave, sickness incapacity or maternity / paternity leave. Prorated on the 30-day commercial month. A teleworker earning less than 2 SMMLV receives the auxilio de conectividad INSTEAD, never both (Ley 2466 de 2025 art. 53). |
| Formula (col F) | Auxilio de transporte = 249,095 x days worked / 30, where the employee earns up to 2 SMMLV (3,501,810) and public transport is available (Decreto 1470 de 2025 art. 1) |
| Nomina Electronica element (col Y) | Devengados / Transporte - AuxilioTransporte (NIE071) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62512` - Adjustment - Car & Transportation allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | THE COUNTER-INTUITIVE COLOMBIAN LINE. The statutory transport allowance is NOT salary and is therefore OUT of the IBC and OUT of the Ley 21/1982 payroll-levy base - but it IS in the statutory-benefit base, so it enters the prima de servicios, the cesantias and the interest on them. It is NOT in the vacation base. It is taxable income (usually within the 0% band). Not payable for days of unpaid leave, sickness incapacity or maternity / paternity leave. Prorated on the 30-day commercial month. A teleworker earning less than 2 SMMLV receives the auxilio de conectividad INSTEAD, never both (Ley 2466 de 2025 art. 53). |
| Formula (col F) | Auxilio de transporte = 249,095 x days worked / 30, where the employee earns up to 2 SMMLV (3,501,810) and public transport is available (Decreto 1470 de 2025 art. 1) |
| Nomina Electronica element (col Y) | Devengados / Transporte - AuxilioTransporte (NIE071) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62520` - Transportation allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | THE COUNTER-INTUITIVE COLOMBIAN LINE. The statutory transport allowance is NOT salary and is therefore OUT of the IBC and OUT of the Ley 21/1982 payroll-levy base - but it IS in the statutory-benefit base, so it enters the prima de servicios, the cesantias and the interest on them. It is NOT in the vacation base. It is taxable income (usually within the 0% band). Not payable for days of unpaid leave, sickness incapacity or maternity / paternity leave. Prorated on the 30-day commercial month. A teleworker earning less than 2 SMMLV receives the auxilio de conectividad INSTEAD, never both (Ley 2466 de 2025 art. 53). |
| Formula (col F) | Auxilio de transporte = 249,095 x days worked / 30, where the employee earns up to 2 SMMLV (3,501,810) and public transport is available (Decreto 1470 de 2025 art. 1) |
| Nomina Electronica element (col Y) | Devengados / Transporte - AuxilioTransporte (NIE071) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62521` - Arrears - Transportation allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | THE COUNTER-INTUITIVE COLOMBIAN LINE. The statutory transport allowance is NOT salary and is therefore OUT of the IBC and OUT of the Ley 21/1982 payroll-levy base - but it IS in the statutory-benefit base, so it enters the prima de servicios, the cesantias and the interest on them. It is NOT in the vacation base. It is taxable income (usually within the 0% band). Not payable for days of unpaid leave, sickness incapacity or maternity / paternity leave. Prorated on the 30-day commercial month. A teleworker earning less than 2 SMMLV receives the auxilio de conectividad INSTEAD, never both (Ley 2466 de 2025 art. 53). |
| Formula (col F) | Auxilio de transporte = 249,095 x days worked / 30, where the employee earns up to 2 SMMLV (3,501,810) and public transport is available (Decreto 1470 de 2025 art. 1) |
| Nomina Electronica element (col Y) | Devengados / Transporte - AuxilioTransporte (NIE071) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62522` - Adjustment - Transportation allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | THE COUNTER-INTUITIVE COLOMBIAN LINE. The statutory transport allowance is NOT salary and is therefore OUT of the IBC and OUT of the Ley 21/1982 payroll-levy base - but it IS in the statutory-benefit base, so it enters the prima de servicios, the cesantias and the interest on them. It is NOT in the vacation base. It is taxable income (usually within the 0% band). Not payable for days of unpaid leave, sickness incapacity or maternity / paternity leave. Prorated on the 30-day commercial month. A teleworker earning less than 2 SMMLV receives the auxilio de conectividad INSTEAD, never both (Ley 2466 de 2025 art. 53). |
| Formula (col F) | Auxilio de transporte = 249,095 x days worked / 30, where the employee earns up to 2 SMMLV (3,501,810) and public transport is available (Decreto 1470 de 2025 art. 1) |
| Nomina Electronica element (col Y) | Devengados / Transporte - AuxilioTransporte (NIE071) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62523` - Advance - Transportation allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | THE COUNTER-INTUITIVE COLOMBIAN LINE. The statutory transport allowance is NOT salary and is therefore OUT of the IBC and OUT of the Ley 21/1982 payroll-levy base - but it IS in the statutory-benefit base, so it enters the prima de servicios, the cesantias and the interest on them. It is NOT in the vacation base. It is taxable income (usually within the 0% band). Not payable for days of unpaid leave, sickness incapacity or maternity / paternity leave. Prorated on the 30-day commercial month. A teleworker earning less than 2 SMMLV receives the auxilio de conectividad INSTEAD, never both (Ley 2466 de 2025 art. 53). |
| Formula (col F) | Auxilio de transporte = 249,095 x days worked / 30, where the employee earns up to 2 SMMLV (3,501,810) and public transport is available (Decreto 1470 de 2025 art. 1) |
| Nomina Electronica element (col Y) | Devengados / Transporte - AuxilioTransporte (NIE071) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62530` - Car Maintenance Allowance 2 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Cash car, fuel and maintenance allowances are ordinary salary (CST art. 127) and enter the IBC, the payroll-levy base, the statutory-benefit base and the vacation base. A COMPANY CAR provided in kind for private use is instead salary in kind under art. 129, valued CONTRACTUALLY - Colombia has NO published company-car valuation scale, and art. 129 num. 2 routes an unvalued benefit to expert appraisal (estimacion pericial), not to a table. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash car / fuel / maintenance allowance per contract |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62531` - Arrears - Car Maintenance Allowance 2 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Cash car, fuel and maintenance allowances are ordinary salary (CST art. 127) and enter the IBC, the payroll-levy base, the statutory-benefit base and the vacation base. A COMPANY CAR provided in kind for private use is instead salary in kind under art. 129, valued CONTRACTUALLY - Colombia has NO published company-car valuation scale, and art. 129 num. 2 routes an unvalued benefit to expert appraisal (estimacion pericial), not to a table. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash car / fuel / maintenance allowance per contract |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62532` - Adjustment - Car Maintenance Allowance 2 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Cash car, fuel and maintenance allowances are ordinary salary (CST art. 127) and enter the IBC, the payroll-levy base, the statutory-benefit base and the vacation base. A COMPANY CAR provided in kind for private use is instead salary in kind under art. 129, valued CONTRACTUALLY - Colombia has NO published company-car valuation scale, and art. 129 num. 2 routes an unvalued benefit to expert appraisal (estimacion pericial), not to a table. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Cash car / fuel / maintenance allowance per contract |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62540` - Relocation allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | CST art. 128 excludes sums given 'no para su beneficio, ni para enriquecer su patrimonio, sino para desempenar a cabalidad sus funciones'. Outside EVERY base - withholding, IBC, payroll-levy, statutory-benefit and vacation. Relocation and travel-ticket costs paid in the employer's interest and evidenced by documentation are reimbursements; a round, undocumented or habitual cash payment is instead ordinary salary and must be reclassified. |
| Formula (col F) | Genuine reimbursement of documented employer expenditure, or an amount given to enable the work (means of transport, work tools, representation expenses) - not remuneration |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62541` - Arrears - Relocation allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | CST art. 128 excludes sums given 'no para su beneficio, ni para enriquecer su patrimonio, sino para desempenar a cabalidad sus funciones'. Outside EVERY base - withholding, IBC, payroll-levy, statutory-benefit and vacation. Relocation and travel-ticket costs paid in the employer's interest and evidenced by documentation are reimbursements; a round, undocumented or habitual cash payment is instead ordinary salary and must be reclassified. |
| Formula (col F) | Genuine reimbursement of documented employer expenditure, or an amount given to enable the work (means of transport, work tools, representation expenses) - not remuneration |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62542` - Adjustment - Relocation allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | CST art. 128 excludes sums given 'no para su beneficio, ni para enriquecer su patrimonio, sino para desempenar a cabalidad sus funciones'. Outside EVERY base - withholding, IBC, payroll-levy, statutory-benefit and vacation. Relocation and travel-ticket costs paid in the employer's interest and evidenced by documentation are reimbursements; a round, undocumented or habitual cash payment is instead ordinary salary and must be reclassified. |
| Formula (col F) | Genuine reimbursement of documented employer expenditure, or an amount given to enable the work (means of transport, work tools, representation expenses) - not remuneration |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62550` - Travel ticket allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | CST art. 128 excludes sums given 'no para su beneficio, ni para enriquecer su patrimonio, sino para desempenar a cabalidad sus funciones'. Outside EVERY base - withholding, IBC, payroll-levy, statutory-benefit and vacation. Relocation and travel-ticket costs paid in the employer's interest and evidenced by documentation are reimbursements; a round, undocumented or habitual cash payment is instead ordinary salary and must be reclassified. |
| Formula (col F) | Genuine reimbursement of documented employer expenditure, or an amount given to enable the work (means of transport, work tools, representation expenses) - not remuneration |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62551` - Arrears - Travel ticket allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | CST art. 128 excludes sums given 'no para su beneficio, ni para enriquecer su patrimonio, sino para desempenar a cabalidad sus funciones'. Outside EVERY base - withholding, IBC, payroll-levy, statutory-benefit and vacation. Relocation and travel-ticket costs paid in the employer's interest and evidenced by documentation are reimbursements; a round, undocumented or habitual cash payment is instead ordinary salary and must be reclassified. |
| Formula (col F) | Genuine reimbursement of documented employer expenditure, or an amount given to enable the work (means of transport, work tools, representation expenses) - not remuneration |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62552` - Adjustment - Travel ticket allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | CST art. 128 excludes sums given 'no para su beneficio, ni para enriquecer su patrimonio, sino para desempenar a cabalidad sus funciones'. Outside EVERY base - withholding, IBC, payroll-levy, statutory-benefit and vacation. Relocation and travel-ticket costs paid in the employer's interest and evidenced by documentation are reimbursements; a round, undocumented or habitual cash payment is instead ordinary salary and must be reclassified. |
| Formula (col F) | Genuine reimbursement of documented employer expenditure, or an amount given to enable the work (means of transport, work tools, representation expenses) - not remuneration |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62560` - Relocation allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | CST art. 128 excludes sums given 'no para su beneficio, ni para enriquecer su patrimonio, sino para desempenar a cabalidad sus funciones'. Outside EVERY base - withholding, IBC, payroll-levy, statutory-benefit and vacation. Relocation and travel-ticket costs paid in the employer's interest and evidenced by documentation are reimbursements; a round, undocumented or habitual cash payment is instead ordinary salary and must be reclassified. |
| Formula (col F) | Genuine reimbursement of documented employer expenditure, or an amount given to enable the work (means of transport, work tools, representation expenses) - not remuneration |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62561` - Arrears - Relocation allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | CST art. 128 excludes sums given 'no para su beneficio, ni para enriquecer su patrimonio, sino para desempenar a cabalidad sus funciones'. Outside EVERY base - withholding, IBC, payroll-levy, statutory-benefit and vacation. Relocation and travel-ticket costs paid in the employer's interest and evidenced by documentation are reimbursements; a round, undocumented or habitual cash payment is instead ordinary salary and must be reclassified. |
| Formula (col F) | Genuine reimbursement of documented employer expenditure, or an amount given to enable the work (means of transport, work tools, representation expenses) - not remuneration |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62562` - Adjustment - Relocation allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | CST art. 128 excludes sums given 'no para su beneficio, ni para enriquecer su patrimonio, sino para desempenar a cabalidad sus funciones'. Outside EVERY base - withholding, IBC, payroll-levy, statutory-benefit and vacation. Relocation and travel-ticket costs paid in the employer's interest and evidenced by documentation are reimbursements; a round, undocumented or habitual cash payment is instead ordinary salary and must be reclassified. |
| Formula (col F) | Genuine reimbursement of documented employer expenditure, or an amount given to enable the work (means of transport, work tools, representation expenses) - not remuneration |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62563` - Advance - Relocation allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | CST art. 128 excludes sums given 'no para su beneficio, ni para enriquecer su patrimonio, sino para desempenar a cabalidad sus funciones'. Outside EVERY base - withholding, IBC, payroll-levy, statutory-benefit and vacation. Relocation and travel-ticket costs paid in the employer's interest and evidenced by documentation are reimbursements; a round, undocumented or habitual cash payment is instead ordinary salary and must be reclassified. |
| Formula (col F) | Genuine reimbursement of documented employer expenditure, or an amount given to enable the work (means of transport, work tools, representation expenses) - not remuneration |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado where a true reimbursement; otherwise Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62570` - Per diem allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 130, verbatim: 'Los viaticos permanentes constituyen salario en aquella parte destinada a proporcionar al trabajador manutencion y alojamiento; pero no en lo que solo tenga por finalidad proporcionar los medios de transporte o los gastos de representacion. Siempre que se paguen debe especificarse el valor de cada uno de estos conceptos. Los viaticos accidentales no constituyen salario en ningun caso.' The value of EACH concept must therefore be specified on payment, and the nomina electronica enforces the split with PAIRED elements ViaticoManuAlojS (NIE072) and ViaticoManuAlojNS (NIE073). Configure two wage types, not one - see CO-VIATICOS-PERMANENTES and CO-VIATICOS-OCASIONALES. |
| Formula (col F) | Viaticos: the part destined to MANUTENCION and ALOJAMIENTO is salary; the part for TRANSPORT and REPRESENTATION EXPENSES is not. Occasional viaticos are never salary (CST art. 130) |
| Nomina Electronica element (col Y) | Devengados / Transporte - ViaticoManuAlojS (NIE072) / ViaticoManuAlojNS (NIE073) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62590` - Birth and Marriage Allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An occasional, purely gratuitous payment is excluded from salary by CST art. 128 num. 1, so it is out of the statutory-benefit base and the vacation base - but it is FULLY TAXABLE employment income, and being a 'pago laboral no constitutivo de salario' it is counted in the Ley 1393 de 2010 art. 30 40% clamp test. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | One-off birth / marriage payment (mera liberalidad) |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62591` - Birth and Marriage Allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An occasional, purely gratuitous payment is excluded from salary by CST art. 128 num. 1, so it is out of the statutory-benefit base and the vacation base - but it is FULLY TAXABLE employment income, and being a 'pago laboral no constitutivo de salario' it is counted in the Ley 1393 de 2010 art. 30 40% clamp test. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | One-off birth / marriage payment (mera liberalidad) |
| Nomina Electronica element (col Y) | Devengados / Bonificacion (BonificacionNS, NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62599` - COVID-19 Allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An extraordinary, non-recurring aid payment is an occasional purely gratuitous sum under CST art. 128 num. 1, so out of the statutory-benefit and vacation bases, but FULLY TAXABLE. No Colombian statute exempts emergency aid from employment income. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Extraordinary health-emergency aid (auxilio extraordinario), one-off and gratuitous |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioNS, NIE142) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62610` - Medical insurance / Medical Care - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Employer-paid prepaid health is NOT a statutory exclusion in Colombia - it is a TAXABLE benefit to the employee, reported as an earnings line and withheld in the ordinary monthly base. The employee separately obtains an ET art. 387 lits. a) and b) DEDUCTION of up to 16 UVT per month, on a provider certificate, where the provider is supervised by the National Health Superintendence or the Financial Superintendence. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Employer-paid prepaid medicine (medicina prepagada) or complementary health plan premium; employee may deduct up to 16 UVT/month (COP 837,984) against the withholding base |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioNS, NIE142) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62611` - Arrears - Medical insurance / Medical Care - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Employer-paid prepaid health is NOT a statutory exclusion in Colombia - it is a TAXABLE benefit to the employee, reported as an earnings line and withheld in the ordinary monthly base. The employee separately obtains an ET art. 387 lits. a) and b) DEDUCTION of up to 16 UVT per month, on a provider certificate, where the provider is supervised by the National Health Superintendence or the Financial Superintendence. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Employer-paid prepaid medicine (medicina prepagada) or complementary health plan premium; employee may deduct up to 16 UVT/month (COP 837,984) against the withholding base |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioNS, NIE142) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62612` - Adjustment - Medical insurance / Medical Care - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Employer-paid prepaid health is NOT a statutory exclusion in Colombia - it is a TAXABLE benefit to the employee, reported as an earnings line and withheld in the ordinary monthly base. The employee separately obtains an ET art. 387 lits. a) and b) DEDUCTION of up to 16 UVT per month, on a provider certificate, where the provider is supervised by the National Health Superintendence or the Financial Superintendence. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Employer-paid prepaid medicine (medicina prepagada) or complementary health plan premium; employee may deduct up to 16 UVT/month (COP 837,984) against the withholding base |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioNS, NIE142) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62615` - Medical insurance / Medical Care - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Employer-paid prepaid health is NOT a statutory exclusion in Colombia - it is a TAXABLE benefit to the employee, reported as an earnings line and withheld in the ordinary monthly base. The employee separately obtains an ET art. 387 lits. a) and b) DEDUCTION of up to 16 UVT per month, on a provider certificate, where the provider is supervised by the National Health Superintendence or the Financial Superintendence. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Employer-paid prepaid medicine (medicina prepagada) or complementary health plan premium; employee may deduct up to 16 UVT/month (COP 837,984) against the withholding base |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioNS, NIE142) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62616` - Medical insurance / Medical Care - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Employer-paid prepaid health is NOT a statutory exclusion in Colombia - it is a TAXABLE benefit to the employee, reported as an earnings line and withheld in the ordinary monthly base. The employee separately obtains an ET art. 387 lits. a) and b) DEDUCTION of up to 16 UVT per month, on a provider certificate, where the provider is supervised by the National Health Superintendence or the Financial Superintendence. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Employer-paid prepaid medicine (medicina prepagada) or complementary health plan premium; employee may deduct up to 16 UVT/month (COP 837,984) against the withholding base |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioNS, NIE142) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62618` - Medical insurance / Medical Care - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Employer-paid prepaid health is NOT a statutory exclusion in Colombia - it is a TAXABLE benefit to the employee, reported as an earnings line and withheld in the ordinary monthly base. The employee separately obtains an ET art. 387 lits. a) and b) DEDUCTION of up to 16 UVT per month, on a provider certificate, where the provider is supervised by the National Health Superintendence or the Financial Superintendence. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Employer-paid prepaid medicine (medicina prepagada) or complementary health plan premium; employee may deduct up to 16 UVT/month (COP 837,984) against the withholding base |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioNS, NIE142) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62619` - Medical insurance / Medical Care - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Employer-paid prepaid health is NOT a statutory exclusion in Colombia - it is a TAXABLE benefit to the employee, reported as an earnings line and withheld in the ordinary monthly base. The employee separately obtains an ET art. 387 lits. a) and b) DEDUCTION of up to 16 UVT per month, on a provider certificate, where the provider is supervised by the National Health Superintendence or the Financial Superintendence. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Employer-paid prepaid medicine (medicina prepagada) or complementary health plan premium; employee may deduct up to 16 UVT/month (COP 837,984) against the withholding base |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioNS, NIE142) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62630` - Personal Allowance 2 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62631` - Arrears - Personal Allowance 2 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62632` - Adjustment - Personal Allowance 2 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62640` - Pensions & Pension Refunds - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-10 |
| Wage Type Explanation (col D) | OUT OF SCOPE per scope_manifest - pension payments are made by the pension administrator, not by the employer, and the bono pensional is a transfer between regimes. Retained for global-code completeness. Where an employer does pay pension income it is taxable only above 1,000 UVT per month (ET art. 206 num. 5), the ET art. 388 40% limit expressly does not apply to pensions, pension substitution indemnities or refunds of pension savings, and the payment is reported at Formulario 220 casilla 50 and Formato 2276 numeral N21. A withdrawal of a voluntary individual-account contribution that fails the qualifying conditions is withheld at 35%. |
| Formula (col F) | Pension or refund of pension savings paid by the pension administrator; taxable only on the monthly amount exceeding 1,000 UVT (COP 52,374,000) |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 5 and par. 3, 383 (first paragraph, which brings pensions into the same table), 388 final sentence; Formulario 220 casilla 50; Formato 2276 v4 numeral N21. |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62641` - Pensions & Pension Refunds - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-10 |
| Wage Type Explanation (col D) | OUT OF SCOPE per scope_manifest - pension payments are made by the pension administrator, not by the employer, and the bono pensional is a transfer between regimes. Retained for global-code completeness. Where an employer does pay pension income it is taxable only above 1,000 UVT per month (ET art. 206 num. 5), the ET art. 388 40% limit expressly does not apply to pensions, pension substitution indemnities or refunds of pension savings, and the payment is reported at Formulario 220 casilla 50 and Formato 2276 numeral N21. A withdrawal of a voluntary individual-account contribution that fails the qualifying conditions is withheld at 35%. |
| Formula (col F) | Pension or refund of pension savings paid by the pension administrator; taxable only on the monthly amount exceeding 1,000 UVT (COP 52,374,000) |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 5 and par. 3, 383 (first paragraph, which brings pensions into the same table), 388 final sentence; Formulario 220 casilla 50; Formato 2276 v4 numeral N21. |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62642` - Pensions & Pension Refunds - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-10 |
| Wage Type Explanation (col D) | OUT OF SCOPE per scope_manifest - pension payments are made by the pension administrator, not by the employer, and the bono pensional is a transfer between regimes. Retained for global-code completeness. Where an employer does pay pension income it is taxable only above 1,000 UVT per month (ET art. 206 num. 5), the ET art. 388 40% limit expressly does not apply to pensions, pension substitution indemnities or refunds of pension savings, and the payment is reported at Formulario 220 casilla 50 and Formato 2276 numeral N21. A withdrawal of a voluntary individual-account contribution that fails the qualifying conditions is withheld at 35%. |
| Formula (col F) | Pension or refund of pension savings paid by the pension administrator; taxable only on the monthly amount exceeding 1,000 UVT (COP 52,374,000) |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 5 and par. 3, 383 (first paragraph, which brings pensions into the same table), 388 final sentence; Formulario 220 casilla 50; Formato 2276 v4 numeral N21. |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62643` - Pensions & Pension Refunds - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-10 |
| Wage Type Explanation (col D) | OUT OF SCOPE per scope_manifest - pension payments are made by the pension administrator, not by the employer, and the bono pensional is a transfer between regimes. Retained for global-code completeness. Where an employer does pay pension income it is taxable only above 1,000 UVT per month (ET art. 206 num. 5), the ET art. 388 40% limit expressly does not apply to pensions, pension substitution indemnities or refunds of pension savings, and the payment is reported at Formulario 220 casilla 50 and Formato 2276 numeral N21. A withdrawal of a voluntary individual-account contribution that fails the qualifying conditions is withheld at 35%. |
| Formula (col F) | Pension or refund of pension savings paid by the pension administrator; taxable only on the monthly amount exceeding 1,000 UVT (COP 52,374,000) |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 5 and par. 3, 383 (first paragraph, which brings pensions into the same table), 388 final sentence; Formulario 220 casilla 50; Formato 2276 v4 numeral N21. |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62645` - Pensions & Pension Refunds - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-10 |
| Wage Type Explanation (col D) | OUT OF SCOPE per scope_manifest - pension payments are made by the pension administrator, not by the employer, and the bono pensional is a transfer between regimes. Retained for global-code completeness. Where an employer does pay pension income it is taxable only above 1,000 UVT per month (ET art. 206 num. 5), the ET art. 388 40% limit expressly does not apply to pensions, pension substitution indemnities or refunds of pension savings, and the payment is reported at Formulario 220 casilla 50 and Formato 2276 numeral N21. A withdrawal of a voluntary individual-account contribution that fails the qualifying conditions is withheld at 35%. |
| Formula (col F) | Pension or refund of pension savings paid by the pension administrator; taxable only on the monthly amount exceeding 1,000 UVT (COP 52,374,000) |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 5 and par. 3, 383 (first paragraph, which brings pensions into the same table), 388 final sentence; Formulario 220 casilla 50; Formato 2276 v4 numeral N21. |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62646` - Pensions & Pension Refunds - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-10 |
| Wage Type Explanation (col D) | OUT OF SCOPE per scope_manifest - pension payments are made by the pension administrator, not by the employer, and the bono pensional is a transfer between regimes. Retained for global-code completeness. Where an employer does pay pension income it is taxable only above 1,000 UVT per month (ET art. 206 num. 5), the ET art. 388 40% limit expressly does not apply to pensions, pension substitution indemnities or refunds of pension savings, and the payment is reported at Formulario 220 casilla 50 and Formato 2276 numeral N21. A withdrawal of a voluntary individual-account contribution that fails the qualifying conditions is withheld at 35%. |
| Formula (col F) | Pension or refund of pension savings paid by the pension administrator; taxable only on the monthly amount exceeding 1,000 UVT (COP 52,374,000) |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 5 and par. 3, 383 (first paragraph, which brings pensions into the same table), 388 final sentence; Formulario 220 casilla 50; Formato 2276 v4 numeral N21. |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62647` - Pensions & Pension Refunds - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-10 |
| Wage Type Explanation (col D) | OUT OF SCOPE per scope_manifest - pension payments are made by the pension administrator, not by the employer, and the bono pensional is a transfer between regimes. Retained for global-code completeness. Where an employer does pay pension income it is taxable only above 1,000 UVT per month (ET art. 206 num. 5), the ET art. 388 40% limit expressly does not apply to pensions, pension substitution indemnities or refunds of pension savings, and the payment is reported at Formulario 220 casilla 50 and Formato 2276 numeral N21. A withdrawal of a voluntary individual-account contribution that fails the qualifying conditions is withheld at 35%. |
| Formula (col F) | Pension or refund of pension savings paid by the pension administrator; taxable only on the monthly amount exceeding 1,000 UVT (COP 52,374,000) |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 5 and par. 3, 383 (first paragraph, which brings pensions into the same table), 388 final sentence; Formulario 220 casilla 50; Formato 2276 v4 numeral N21. |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62648` - Pensions & Pension Refunds - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-10 |
| Wage Type Explanation (col D) | OUT OF SCOPE per scope_manifest - pension payments are made by the pension administrator, not by the employer, and the bono pensional is a transfer between regimes. Retained for global-code completeness. Where an employer does pay pension income it is taxable only above 1,000 UVT per month (ET art. 206 num. 5), the ET art. 388 40% limit expressly does not apply to pensions, pension substitution indemnities or refunds of pension savings, and the payment is reported at Formulario 220 casilla 50 and Formato 2276 numeral N21. A withdrawal of a voluntary individual-account contribution that fails the qualifying conditions is withheld at 35%. |
| Formula (col F) | Pension or refund of pension savings paid by the pension administrator; taxable only on the monthly amount exceeding 1,000 UVT (COP 52,374,000) |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado; Formulario 220 casilla 50 / Formato 2276 N21 |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 5 and par. 3, 383 (first paragraph, which brings pensions into the same table), 388 final sentence; Formulario 220 casilla 50; Formato 2276 v4 numeral N21. |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62650` - Social raise / Social allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring supplement of a remunerative character is salary under CST art. 127 - the article expressly names 'primas, sobresueldos' - and enters the IBC, the payroll-levy base, the statutory-benefit base and the vacation base. Note that the PUBLIC-SECTOR prima especial and prima de costo de vida sit OUTSIDE the 40% and 1,340-UVT tax caps (ET art. 206 par. 4) but are out of Mercans private-sector scope; the engine must nonetheless carry the flag so it does not silently clamp them if such an employee is loaded. |
| Formula (col F) | Recurring social / cost-of-living supplement (sobresueldo) per contract or collective agreement |
| Nomina Electronica element (col Y) | Devengados / OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62660` - Personal Allowance 1 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62661` - Arrears - Personal Allowance 1 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62662` - Adjustment - Personal Allowance 1 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62670` - Benefits plan 1 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A benefits-plan value delivered as a habitual or occasional BENEFIT OR ALLOWANCE (food, housing, clothing) can validly be pacted non-salary in writing under CST art. 128 - the Colombian workhorse. Three tests for a valid pact: it must be (a) EXPRESS, (b) WRITTEN, and (c) attached to a benefit or allowance, not to consideration for the service itself. A 'non-salary' label on what is plainly remuneration for work will not survive a UGPP contribution audit. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Employer-funded flexible-benefits value, typically structured as non-salary under a written CST art. 128 pact |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioNS, NIE142) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62680` - Benefits plan 2 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A benefits-plan value delivered as a habitual or occasional BENEFIT OR ALLOWANCE (food, housing, clothing) can validly be pacted non-salary in writing under CST art. 128 - the Colombian workhorse. Three tests for a valid pact: it must be (a) EXPRESS, (b) WRITTEN, and (c) attached to a benefit or allowance, not to consideration for the service itself. A 'non-salary' label on what is plainly remuneration for work will not survive a UGPP contribution audit. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Employer-funded flexible-benefits value, typically structured as non-salary under a written CST art. 128 pact |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioNS, NIE142) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62700` - Education allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia has NO statutory education or schooling exemption. A habitual cash education allowance is salary under CST art. 127 and enters every base; an EXPRESS WRITTEN art. 128 pact moves it to non-salary for labour purposes, subject to the 40% clamp, with NO tax effect. Distinguish 'apoyos economicos educativos financiados con recursos publicos', which are reported separately (Formulario 220 casilla 51 / Formato 2276 numeral N16) and are outside private-sector payroll. |
| Formula (col F) | Cash education / schooling allowance per contract or collective agreement |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62710` - Schooling allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia has NO statutory education or schooling exemption. A habitual cash education allowance is salary under CST art. 127 and enters every base; an EXPRESS WRITTEN art. 128 pact moves it to non-salary for labour purposes, subject to the 40% clamp, with NO tax effect. Distinguish 'apoyos economicos educativos financiados con recursos publicos', which are reported separately (Formulario 220 casilla 51 / Formato 2276 numeral N16) and are outside private-sector payroll. |
| Formula (col F) | Cash education / schooling allowance per contract or collective agreement |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62711` - Arrears - Schooling allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia has NO statutory education or schooling exemption. A habitual cash education allowance is salary under CST art. 127 and enters every base; an EXPRESS WRITTEN art. 128 pact moves it to non-salary for labour purposes, subject to the 40% clamp, with NO tax effect. Distinguish 'apoyos economicos educativos financiados con recursos publicos', which are reported separately (Formulario 220 casilla 51 / Formato 2276 numeral N16) and are outside private-sector payroll. |
| Formula (col F) | Cash education / schooling allowance per contract or collective agreement |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62720` - Education & Schooling allowance 2 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia has NO statutory education or schooling exemption. A habitual cash education allowance is salary under CST art. 127 and enters every base; an EXPRESS WRITTEN art. 128 pact moves it to non-salary for labour purposes, subject to the 40% clamp, with NO tax effect. Distinguish 'apoyos economicos educativos financiados con recursos publicos', which are reported separately (Formulario 220 casilla 51 / Formato 2276 numeral N16) and are outside private-sector payroll. |
| Formula (col F) | Cash education / schooling allowance per contract or collective agreement |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62721` - Arrears - Education & Schooling allowance 2 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia has NO statutory education or schooling exemption. A habitual cash education allowance is salary under CST art. 127 and enters every base; an EXPRESS WRITTEN art. 128 pact moves it to non-salary for labour purposes, subject to the 40% clamp, with NO tax effect. Distinguish 'apoyos economicos educativos financiados con recursos publicos', which are reported separately (Formulario 220 casilla 51 / Formato 2276 numeral N16) and are outside private-sector payroll. |
| Formula (col F) | Cash education / schooling allowance per contract or collective agreement |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62730` - Education & Schooling allowance 3 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia has NO statutory education or schooling exemption. A habitual cash education allowance is salary under CST art. 127 and enters every base; an EXPRESS WRITTEN art. 128 pact moves it to non-salary for labour purposes, subject to the 40% clamp, with NO tax effect. Distinguish 'apoyos economicos educativos financiados con recursos publicos', which are reported separately (Formulario 220 casilla 51 / Formato 2276 numeral N16) and are outside private-sector payroll. |
| Formula (col F) | Cash education / schooling allowance per contract or collective agreement |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62740` - Education & Schooling allowance 4 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia has NO statutory education or schooling exemption. A habitual cash education allowance is salary under CST art. 127 and enters every base; an EXPRESS WRITTEN art. 128 pact moves it to non-salary for labour purposes, subject to the 40% clamp, with NO tax effect. Distinguish 'apoyos economicos educativos financiados con recursos publicos', which are reported separately (Formulario 220 casilla 51 / Formato 2276 numeral N16) and are outside private-sector payroll. |
| Formula (col F) | Cash education / schooling allowance per contract or collective agreement |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62741` - Arrears - Education & Schooling allowance 4 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia has NO statutory education or schooling exemption. A habitual cash education allowance is salary under CST art. 127 and enters every base; an EXPRESS WRITTEN art. 128 pact moves it to non-salary for labour purposes, subject to the 40% clamp, with NO tax effect. Distinguish 'apoyos economicos educativos financiados con recursos publicos', which are reported separately (Formulario 220 casilla 51 / Formato 2276 numeral N16) and are outside private-sector payroll. |
| Formula (col F) | Cash education / schooling allowance per contract or collective agreement |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62750` - Education & Schooling allowance 5 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia has NO statutory education or schooling exemption. A habitual cash education allowance is salary under CST art. 127 and enters every base; an EXPRESS WRITTEN art. 128 pact moves it to non-salary for labour purposes, subject to the 40% clamp, with NO tax effect. Distinguish 'apoyos economicos educativos financiados con recursos publicos', which are reported separately (Formulario 220 casilla 51 / Formato 2276 numeral N16) and are outside private-sector payroll. |
| Formula (col F) | Cash education / schooling allowance per contract or collective agreement |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62751` - Arrears - Education & Schooling allowance 5 - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Colombia has NO statutory education or schooling exemption. A habitual cash education allowance is salary under CST art. 127 and enters every base; an EXPRESS WRITTEN art. 128 pact moves it to non-salary for labour purposes, subject to the 40% clamp, with NO tax effect. Distinguish 'apoyos economicos educativos financiados con recursos publicos', which are reported separately (Formulario 220 casilla 51 / Formato 2276 numeral N16) and are outside private-sector payroll. |
| Formula (col F) | Cash education / schooling allowance per contract or collective agreement |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141); Deducciones / Educacion (NIE183) for an employee debt |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62760` - Family allowance (MLA, Children) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | OUT OF SCOPE per scope_manifest: the family subsidy is a CCF fund benefit paid to the employee by the fund, not a payment run through employer gross-to-net. Retained for global-code completeness and configured outside every base. The employer's related obligation is the CCF 4% levy on the Ley 21/1982 base, which is NEVER exonerated - see CO-ER-CCF. |
| Formula (col F) | Subsidio familiar paid BY the Caja de Compensacion Familiar to the employee - not an employer payroll payment (the employer's obligation is the 4% CCF levy) |
| Nomina Electronica element (col Y) | Not a nomina electronica element (fund-paid benefit) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62762` - Adjustment - Family allowance (MLA, Children) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | OUT OF SCOPE per scope_manifest: the family subsidy is a CCF fund benefit paid to the employee by the fund, not a payment run through employer gross-to-net. Retained for global-code completeness and configured outside every base. The employer's related obligation is the CCF 4% levy on the Ley 21/1982 base, which is NEVER exonerated - see CO-ER-CCF. |
| Formula (col F) | Subsidio familiar paid BY the Caja de Compensacion Familiar to the employee - not an employer payroll payment (the employer's obligation is the 4% CCF levy) |
| Nomina Electronica element (col Y) | Not a nomina electronica element (fund-paid benefit) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62770` - Recognition Award - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Non-statutory bonuses are entirely contractual. They are SALARY if habitual - CST art. 127 expressly lists 'primas, sobresueldos, bonificaciones habituales' - and therefore contributory and in every base, UNLESS the parties have expressly agreed in writing that they do not constitute salary, subject always to the 40% clamp. Configured here as the conservative default - salary. Tax: no preferential bonus rate, no separate annualisation and no tax-free bonus allowance exists; the bonus enters the ordinary monthly base under both procedures (only the STATUTORY MINIMUM prima de servicios gets the separate art. 385 table read). A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Contractual bonus (performance, sign-on, retention, referral) per the scheme; SALARY where habitual, non-salary only under an express written CST art. 128 pact |
| Nomina Electronica element (col Y) | Devengados / Bonificacion - BonificacionS (NIE139) / BonificacionNS (NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62870` - Special allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62871` - Special allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62872` - Special allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62873` - Special allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62875` - Special allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62876` - Special allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62877` - Special allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62878` - Special allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62879` - Special allowance - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62880` - Post-termination payment - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Termination payments are FULLY TAXABLE ordinary employment income entering the ordinary monthly base, and are OUT of the IBC and the payroll-levy base. Colombia has NO concessional cap on termination payments: only the statutory-minimum indemnities of ET art. 206 nums. 1-3 are exempt and even those only up to the legal minimum amount (art. 206 par. 1). A negotiated mutual-termination bonus and a payment in lieu of notice are frequently and WRONGLY assumed exempt - they are not. Employees with 10 or more years of continuous service at the entry into force of Ley 789 de 2002 retain the earlier Ley 50 de 1990 art. 6 scale. Note the CST art. 65 par. 1 gate: the employer must evidence payment of the last three months' contributions within 60 days of the termination, failing which the termination HAS NO EFFECT. For a NON-RESIDENT this is withheld at the flat 20% on the gross under ET art. 408 with no depuration (DIAN Concepto 011108 de 2026); the switch to the art. 383 table is prospective from the payment following the 183rd day of presence. |
| Formula (col F) | Indemnizacion CST art. 64: below 10 SMMLV -> 30 days' salary for the first year + 20 days per subsequent year and pro rata; at or above 10 SMMLV (17,509,050) -> 20 days + 15 days |
| Nomina Electronica element (col Y) | Devengados / Indemnizacion (NIE160); BonifRetiro (NIE159) for a settlement bonus |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62881` - Post-termination payment - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Termination payments are FULLY TAXABLE ordinary employment income entering the ordinary monthly base, and are OUT of the IBC and the payroll-levy base. Colombia has NO concessional cap on termination payments: only the statutory-minimum indemnities of ET art. 206 nums. 1-3 are exempt and even those only up to the legal minimum amount (art. 206 par. 1). A negotiated mutual-termination bonus and a payment in lieu of notice are frequently and WRONGLY assumed exempt - they are not. Employees with 10 or more years of continuous service at the entry into force of Ley 789 de 2002 retain the earlier Ley 50 de 1990 art. 6 scale. Note the CST art. 65 par. 1 gate: the employer must evidence payment of the last three months' contributions within 60 days of the termination, failing which the termination HAS NO EFFECT. For a NON-RESIDENT this is withheld at the flat 20% on the gross under ET art. 408 with no depuration (DIAN Concepto 011108 de 2026); the switch to the art. 383 table is prospective from the payment following the 183rd day of presence. |
| Formula (col F) | Indemnizacion CST art. 64: below 10 SMMLV -> 30 days' salary for the first year + 20 days per subsequent year and pro rata; at or above 10 SMMLV (17,509,050) -> 20 days + 15 days |
| Nomina Electronica element (col Y) | Devengados / Indemnizacion (NIE160); BonifRetiro (NIE159) for a settlement bonus |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62882` - Post-termination payment - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Termination payments are FULLY TAXABLE ordinary employment income entering the ordinary monthly base, and are OUT of the IBC and the payroll-levy base. Colombia has NO concessional cap on termination payments: only the statutory-minimum indemnities of ET art. 206 nums. 1-3 are exempt and even those only up to the legal minimum amount (art. 206 par. 1). A negotiated mutual-termination bonus and a payment in lieu of notice are frequently and WRONGLY assumed exempt - they are not. Employees with 10 or more years of continuous service at the entry into force of Ley 789 de 2002 retain the earlier Ley 50 de 1990 art. 6 scale. Note the CST art. 65 par. 1 gate: the employer must evidence payment of the last three months' contributions within 60 days of the termination, failing which the termination HAS NO EFFECT. For a NON-RESIDENT this is withheld at the flat 20% on the gross under ET art. 408 with no depuration (DIAN Concepto 011108 de 2026); the switch to the art. 383 table is prospective from the payment following the 183rd day of presence. |
| Formula (col F) | Indemnizacion CST art. 64: below 10 SMMLV -> 30 days' salary for the first year + 20 days per subsequent year and pro rata; at or above 10 SMMLV (17,509,050) -> 20 days + 15 days |
| Nomina Electronica element (col Y) | Devengados / Indemnizacion (NIE160); BonifRetiro (NIE159) for a settlement bonus |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62883` - Post-termination payment - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Termination payments are FULLY TAXABLE ordinary employment income entering the ordinary monthly base, and are OUT of the IBC and the payroll-levy base. Colombia has NO concessional cap on termination payments: only the statutory-minimum indemnities of ET art. 206 nums. 1-3 are exempt and even those only up to the legal minimum amount (art. 206 par. 1). A negotiated mutual-termination bonus and a payment in lieu of notice are frequently and WRONGLY assumed exempt - they are not. Employees with 10 or more years of continuous service at the entry into force of Ley 789 de 2002 retain the earlier Ley 50 de 1990 art. 6 scale. Note the CST art. 65 par. 1 gate: the employer must evidence payment of the last three months' contributions within 60 days of the termination, failing which the termination HAS NO EFFECT. For a NON-RESIDENT this is withheld at the flat 20% on the gross under ET art. 408 with no depuration (DIAN Concepto 011108 de 2026); the switch to the art. 383 table is prospective from the payment following the 183rd day of presence. |
| Formula (col F) | Indemnizacion CST art. 64: below 10 SMMLV -> 30 days' salary for the first year + 20 days per subsequent year and pro rata; at or above 10 SMMLV (17,509,050) -> 20 days + 15 days |
| Nomina Electronica element (col Y) | Devengados / Indemnizacion (NIE160); BonifRetiro (NIE159) for a settlement bonus |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62890` - Stock options and grants - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Equity and share-incentive awards are TAXABLE EMPLOYMENT INCOME AT EXERCISE OR VESTING, on the spread, entering the ordinary monthly base and the ET art. 383 table. The subsequent disposal is a separate capital transaction outside payroll. Generally non-salary (an occasional, non-consideration benefit) so out of the statutory-benefit and vacation bases, but A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. For a non-resident, ET art. 408 applies at 20% where the underlying service was performed in Colombia; where the service was performed abroad the income is foreign-source and not taxable. |
| Formula (col F) | Taxable spread = market value at exercise or vesting less the exercise price paid |
| Nomina Electronica element (col Y) | Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62900` - Statutory Gratuity, EOS - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-02 |
| Wage Type Explanation (col D) | Cesantias and the interest on them are STATUTORY BENEFITS excluded from salary by CST art. 128, so out of the IBC and out of the payroll-levy base. They are EXCLUDED FROM THE MONTHLY WITHHOLDING BASE ENTIRELY under BOTH procedures (ET arts. 385 and 386) - not merely exempt - and the ET art. 206 num. 4 exemption is applied when the payment is made: exempt in full where the average monthly income of the last 6 months is <= 350 UVT (18,330,900), then tapering 90/80/60/40/20/0%. The 25% exemption of art. 206 num. 10 does NOT apply (art. 206 par. 2). Liquidated at 31 December and DEPOSITED TO THE EMPLOYEE'S FUND BY 14 FEBRUARY; late deposit costs one day's salary per day of delay. The interest is paid TO THE EMPLOYEE during January, not to the fund. Ley 2466 de 2025 art. 64 permits an 8.33% monthly advance deposit by agreement. |
| Formula (col F) | Auxilio de cesantias = (monthly salary + auxilio de transporte) x days of service / 360; interest = cesantias balance x 12% x days / 360 |
| Nomina Electronica element (col Y) | Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122) |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 4 and par. 2, 385, 386; Ley 50 de 1990 art. 99; Ley 52 de 1975 art. 1; Ley 2466 de 2025 art. 64 (8.33% monthly advance deposit). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62901` - Supplemental basic (i.e. 13th or 14th months salary) - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-03 |
| Wage Type Explanation (col D) | The statutory service bonus is Colombia's 13th-month equivalent. CST art. 307: 'La prima anual no es salario, ni se computara como factor del salario en ningun caso' - so it is OUT of the IBC and OUT of the payroll-levy base. TAX TREATMENT DIVERGES SHARPLY BY PROCEDURE and is one of the most commonly mis-implemented rules in Colombian payroll: under PROCEDURE 1 the statutory minimum bonus is withheld SEPARATELY on its own read of the art. 383 table (ET art. 385) and is NOT added to the month's salary; under PROCEDURE 2 it is folded into the ordinary monthly base, the 13 divisor of art. 386 having already prorated its effect. Any excess above the statutory minimum goes to the ordinary monthly base under both. Contractual and Christmas bonuses are set off against it (CST art. 308). Absorbed by an all-inclusive salary. |
| Formula (col F) | Prima de servicios = (monthly salary + auxilio de transporte) x days in the semester / 360, i.e. 30 days' salary per year - half by 30 June, half by 20 December |
| Nomina Electronica element (col Y) | Devengados / Primas - Cantidad (NIE117), Pago (NIE118), PagoNS (NIE119) |
| Tax Code Source - C9 (col Z) | ET arts. 385 and 386; CST arts. 306 (as amended by Ley 1788 de 2016 art. 1), 307 and 308. |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62910` - Gratuity, EOS, Post-termination, etc. - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-02 |
| Wage Type Explanation (col D) | Cesantias and the interest on them are STATUTORY BENEFITS excluded from salary by CST art. 128, so out of the IBC and out of the payroll-levy base. They are EXCLUDED FROM THE MONTHLY WITHHOLDING BASE ENTIRELY under BOTH procedures (ET arts. 385 and 386) - not merely exempt - and the ET art. 206 num. 4 exemption is applied when the payment is made: exempt in full where the average monthly income of the last 6 months is <= 350 UVT (18,330,900), then tapering 90/80/60/40/20/0%. The 25% exemption of art. 206 num. 10 does NOT apply (art. 206 par. 2). Liquidated at 31 December and DEPOSITED TO THE EMPLOYEE'S FUND BY 14 FEBRUARY; late deposit costs one day's salary per day of delay. The interest is paid TO THE EMPLOYEE during January, not to the fund. Ley 2466 de 2025 art. 64 permits an 8.33% monthly advance deposit by agreement. |
| Formula (col F) | Auxilio de cesantias = (monthly salary + auxilio de transporte) x days of service / 360; interest = cesantias balance x 12% x days / 360 |
| Nomina Electronica element (col Y) | Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122) |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 4 and par. 2, 385, 386; Ley 50 de 1990 art. 99; Ley 52 de 1975 art. 1; Ley 2466 de 2025 art. 64 (8.33% monthly advance deposit). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62920` - Gratuity, EOS, Post-termination, etc. - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-02 |
| Wage Type Explanation (col D) | Cesantias and the interest on them are STATUTORY BENEFITS excluded from salary by CST art. 128, so out of the IBC and out of the payroll-levy base. They are EXCLUDED FROM THE MONTHLY WITHHOLDING BASE ENTIRELY under BOTH procedures (ET arts. 385 and 386) - not merely exempt - and the ET art. 206 num. 4 exemption is applied when the payment is made: exempt in full where the average monthly income of the last 6 months is <= 350 UVT (18,330,900), then tapering 90/80/60/40/20/0%. The 25% exemption of art. 206 num. 10 does NOT apply (art. 206 par. 2). Liquidated at 31 December and DEPOSITED TO THE EMPLOYEE'S FUND BY 14 FEBRUARY; late deposit costs one day's salary per day of delay. The interest is paid TO THE EMPLOYEE during January, not to the fund. Ley 2466 de 2025 art. 64 permits an 8.33% monthly advance deposit by agreement. |
| Formula (col F) | Auxilio de cesantias = (monthly salary + auxilio de transporte) x days of service / 360; interest = cesantias balance x 12% x days / 360 |
| Nomina Electronica element (col Y) | Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122) |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 4 and par. 2, 385, 386; Ley 50 de 1990 art. 99; Ley 52 de 1975 art. 1; Ley 2466 de 2025 art. 64 (8.33% monthly advance deposit). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62930` - Gratuity, EOS, Post-termination, etc. - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-02 |
| Wage Type Explanation (col D) | Cesantias and the interest on them are STATUTORY BENEFITS excluded from salary by CST art. 128, so out of the IBC and out of the payroll-levy base. They are EXCLUDED FROM THE MONTHLY WITHHOLDING BASE ENTIRELY under BOTH procedures (ET arts. 385 and 386) - not merely exempt - and the ET art. 206 num. 4 exemption is applied when the payment is made: exempt in full where the average monthly income of the last 6 months is <= 350 UVT (18,330,900), then tapering 90/80/60/40/20/0%. The 25% exemption of art. 206 num. 10 does NOT apply (art. 206 par. 2). Liquidated at 31 December and DEPOSITED TO THE EMPLOYEE'S FUND BY 14 FEBRUARY; late deposit costs one day's salary per day of delay. The interest is paid TO THE EMPLOYEE during January, not to the fund. Ley 2466 de 2025 art. 64 permits an 8.33% monthly advance deposit by agreement. |
| Formula (col F) | Auxilio de cesantias = (monthly salary + auxilio de transporte) x days of service / 360; interest = cesantias balance x 12% x days / 360 |
| Nomina Electronica element (col Y) | Devengados / Cesantias - Pago (NIE120), Porcentaje (NIE121), PagoIntereses (NIE122) |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 4 and par. 2, 385, 386; Ley 50 de 1990 art. 99; Ley 52 de 1975 art. 1; Ley 2466 de 2025 art. 64 (8.33% monthly advance deposit). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62960` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62961` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62962` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62963` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62964` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62965` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62966` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62967` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62968` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62969` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62980` - Salary addition - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A recurring cash allowance of a remunerative character is salary under CST art. 127 and enters all three bases and the vacation base. Only two routes take it out of the IBC: an EXPRESS WRITTEN art. 128 non-salary pact over a genuine benefit or allowance (subject to the 40% clamp, no tax effect), or the art. 128 exclusion for amounts given to enable the work. A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. |
| Formula (col F) | Recurring cash allowance / salary supplement per contract; SALARY where it is consideration for the service |
| Nomina Electronica element (col Y) | Devengados / Auxilio (AuxilioS, NIE141) or OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62990` - Stock options and grants - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Equity and share-incentive awards are TAXABLE EMPLOYMENT INCOME AT EXERCISE OR VESTING, on the spread, entering the ordinary monthly base and the ET art. 383 table. The subsequent disposal is a separate capital transaction outside payroll. Generally non-salary (an occasional, non-consideration benefit) so out of the statutory-benefit and vacation bases, but A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. For a non-resident, ET art. 408 applies at 20% where the underlying service was performed in Colombia; where the service was performed abroad the income is foreign-source and not taxable. |
| Formula (col F) | Taxable spread = market value at exercise or vesting less the exercise price paid |
| Nomina Electronica element (col Y) | Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62991` - Stock options and grants - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Equity and share-incentive awards are TAXABLE EMPLOYMENT INCOME AT EXERCISE OR VESTING, on the spread, entering the ordinary monthly base and the ET art. 383 table. The subsequent disposal is a separate capital transaction outside payroll. Generally non-salary (an occasional, non-consideration benefit) so out of the statutory-benefit and vacation bases, but A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. For a non-resident, ET art. 408 applies at 20% where the underlying service was performed in Colombia; where the service was performed abroad the income is foreign-source and not taxable. |
| Formula (col F) | Taxable spread = market value at exercise or vesting less the exercise price paid |
| Nomina Electronica element (col Y) | Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62993` - Stock options and grants - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Equity and share-incentive awards are TAXABLE EMPLOYMENT INCOME AT EXERCISE OR VESTING, on the spread, entering the ordinary monthly base and the ET art. 383 table. The subsequent disposal is a separate capital transaction outside payroll. Generally non-salary (an occasional, non-consideration benefit) so out of the statutory-benefit and vacation bases, but A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. For a non-resident, ET art. 408 applies at 20% where the underlying service was performed in Colombia; where the service was performed abroad the income is foreign-source and not taxable. |
| Formula (col F) | Taxable spread = market value at exercise or vesting less the exercise price paid |
| Nomina Electronica element (col Y) | Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `62994` - Stock options and grants - *(codigo global - ver la explicacion para el tratamiento colombiano)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Equity and share-incentive awards are TAXABLE EMPLOYMENT INCOME AT EXERCISE OR VESTING, on the spread, entering the ordinary monthly base and the ET art. 383 table. The subsequent disposal is a separate capital transaction outside payroll. Generally non-salary (an occasional, non-consideration benefit) so out of the statutory-benefit and vacation bases, but A valid written CST art. 128 non-salary pact keeps this out of the IBC ONLY up to the Ley 1393 de 2010 art. 30 40% clamp; the excess over 40% of total remuneration is forced BACK into the health, pension, solidarity-fund and occupational-risk base while remaining non-salary for the statutory benefits. The clamp does NOT reach the CCF/SENA/ICBF levy base, which has its own Ley 21 de 1982 art. 17 definition. A non-salary pact has NO tax effect whatsoever. For a non-resident, ET art. 408 applies at 20% where the underlying service was performed in Colombia; where the service was performed abroad the income is foreign-source and not taxable. |
| Formula (col F) | Taxable spread = market value at exercise or vesting less the exercise price paid |
| Nomina Electronica element (col Y) | Devengados / OtroConcepto (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-SALARIO-BASICO` - Basic salary - *Salario Basico*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Salario basico, fixed or variable (CST arts. 127 and 132 num. 1). Enters ALL THREE BASES: the IBC (floor 1 SMMLV pro-rated to contributory days, ceiling 25 SMMLV = 43,772,625, rounded UP to the whole peso), the Ley 21/1982 payroll-levy base (NO ceiling), and the ET art. 388 withholding base. Prorated on a 30-day COMMERCIAL month irrespective of calendar days - February and a 31-day month are both 30 payroll days, and a hire on the 31st counts as day 30. The 2026 amount was fixed by Decreto 1469 de 29 diciembre 2025, provisionally suspended by the Council of State on 12 February 2026, re-fixed identically by Decreto 0159 de 2026, and restored when the suspension was revoked on 9 July 2026; the AMOUNT has been continuously in force since 1 January 2026 and has never been in dispute. |
| Formula (col F) | full month = S; partial month = S x days worked / 30; minimum 1,750,905/month (Decreto 1469 de 2025 art. 1) |
| Nomina Electronica element (col Y) | Devengados / Basico - DiasTrabajados (NIE069), SueldoTrabajado (NIE070) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-SALARIO-INTEGRAL` - All-inclusive salary - *Salario Integral*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Salario integral (CST art. 132 nums. 2-3, written agreement required). It compensates in advance the statutory benefits, premia and allowances - night work, overtime, rest-day and holiday work, statutory and extra-statutory bonuses, cesantias and their interest, subsidies and in-kind supplies - EXCEPT VACATION. Contributions are calculated on 70% (Ley 797 de 2003 art. 5 substituting Ley 100 art. 18: 'Las cotizaciones de los trabajadores cuya remuneracion se pacte bajo la modalidad de salario integral, se calculara sobre el 70% de dicho salario'), and the payroll levies are likewise reduced by 30% (CST art. 132 num. 3), with occupational risk following the same base (Decreto 1072 de 2015 art. 2.2.4.3.3). THE TRAP: vacation is still owed IN FULL, 15 working days on the WHOLE all-inclusive salary, while contributions run on 70%. At the 13-SMMLV floor the IBC is 15,933,235.50 rounded up. The former tax exemption of the benefit factor was replaced by the 25% exempt-income deduction (ET art. 206 par. 2). |
| Formula (col F) | S >= 13 SMMLV = 22,761,765 (10 SMMLV ordinary + a benefit factor of at least 30%); IBC and payroll-levy base BOTH = 70% x S; vacation on the FULL 100% |
| Nomina Electronica element (col Y) | Trabajador / SalarioIntegral flag (NIE056); Sueldo (NIE062); PILA T2R2-041 |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-AUX-TRANSPORTE` - Statutory transport allowance - *Auxilio de Transporte*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Mandatory where the employee earns up to 2 SMMLV. NOT salary (Ley 15 de 1959), so OUT of the IBC and OUT of the Ley 21/1982 payroll-levy base - but IN the statutory-benefit base, so it enters the prima de servicios, the cesantias and the 12% interest. NOT in the vacation base. Taxable income, though normally within the 0% withholding band. Not payable for days of unpaid leave, sickness incapacity or maternity / paternity leave. Uniform nationally - there is no departmental, sectoral or rural variant. The 2026 combined minimum cash entitlement of wage + allowance is exactly COP 2,000,000. |
| Formula (col F) | 249,095 x days worked / 30, where salary <= 2 SMMLV (3,501,810) and public transport is available (Decreto 1470 de 2025 art. 1) |
| Nomina Electronica element (col Y) | Devengados / Transporte - AuxilioTransporte (NIE071) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-AUX-CONECTIVIDAD` - Connectivity allowance (teleworkers) - *Auxilio de Conectividad Digital*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Ley 2466 de 2025 art. 53 adds art. 6A to Ley 1221 de 2008: 'El empleador debera otorgar el reconocimiento de un auxilio de conectividad para teletrabajadores y teletrabajadoras que devenguen menos de dos (2) salarios minimos legales mensuales vigentes, en reemplazo del auxilio de transporte. En todo caso, los teletrabajadores y teletrabajadoras, solo tendran derecho a recibir uno de estos auxilios, independientemente de la modalidad de teletrabajo otorgado.' NEVER PAID TOGETHER WITH THE TRANSPORT ALLOWANCE - the engine must enforce mutual exclusion on the telework flag. Expressly does not constitute salary, so out of the IBC and the levy base, but in the statutory-benefit base for employees up to 2 SMMLV. Taxable income. |
| Formula (col F) | 249,095 x days worked / 30, for a teleworker earning LESS THAN 2 SMMLV (3,501,810), IN PLACE OF the transport allowance (Ley 2466 de 2025 art. 53) |
| Nomina Electronica element (col Y) | Devengados / Transporte - AuxilioTransporte (NIE071); Teletrabajo (NIE158) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-HED` - Day overtime (+25%) - *Hora Extra Diurna (25%)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 168 num. 2. Salary, fully in the IBC and the payroll-levy base, in the prima / cesantias / interest base, and EXCLUDED FROM THE VACATION BASE (CST art. 192). Fully taxable, no preferential rate. Premia arise exclusively and are not cumulated with one another (art. 168 num. 4); only the art. 179 rest-day premium is added. Volume limit 2 hours/day and 12/week (Ley 2466 art. 13). |
| Formula (col F) | (S / D) x 1.25 x H for hours 06:00-19:00 beyond the ordinary day; D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HED - Cantidad (NIE076), Porcentaje (NIE077), Pago (NIE078) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-HEN` - Night overtime (+75%) - *Hora Extra Nocturna (75%)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 168 num. 3. Same base treatment as day overtime: in the IBC, the levy base and the statutory-benefit base, OUT of the vacation base, fully taxable. The 19:00 boundary applies since 25 December 2025 (CST art. 160 as substituted by Ley 2466 de 2025 art. 10, par. 2 deferring entry into force by six months from the 25 June 2025 sanction). |
| Formula (col F) | (S / D) x 1.75 x H for hours 19:00-06:00 beyond the ordinary day; D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HEN - Cantidad (NIE081), Porcentaje (NIE082), Pago (NIE083) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-RECARGO-NOCTURNO` - Night premium (35%) - *Recargo Nocturno (35%)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 168 num. 1 - a premium for the fact of night work, on ordinary hours, distinct from overtime. UNLIKE OVERTIME IT STAYS IN THE VACATION BASE: CST art. 192 excludes only rest-day work and supplementary overtime hours, so the night premium and commissions remain. Salary, fully contributory, fully taxable. Does NOT apply on the 6-hour / 36-hour-week successive shift system (CST arts. 161(d) and 168 num. 1). Two extra hours a day attract it since the window moved from 21:00 to 19:00 on 25 December 2025. |
| Formula (col F) | (S / D) x 0.35 x H for ORDINARY hours falling in the 19:00-06:00 window; D = 220 to 14 Jul 2026 / 210 from 15 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HRN - Cantidad (NIE086), Porcentaje (NIE087), Pago (NIE088) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-RECARGO-DOMINICAL` - Obligatory rest-day / holiday premium (80% / 90%) - *Recargo Dominical y Festivo (80% hasta 30-jun-2026 / 90% desde 1-jul-2026)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 179 as substituted by Ley 2466 de 2025 art. 14, transitional paragraph verified verbatim: '...80%. A partir del primero de julio de 2026, se incrementara el recargo por laborar en dia de descanso obligatorio a 90%. A partir del primero de julio de 2027, se dara plena aplicacion al recargo ... sin perjuicio de que ... el empleador se acoja al recargo del 100%.' THE THREE-VALUE STRUCTURE (MinTrabajo Circular 101 de 2025 SS4): working an obligatory rest day generates THREE independent payment obligations - (1) the paid rest day itself at one day's ordinary salary (CST art. 173), (2) the hours actually worked, (3) this additional premium. An engine that pays only the hours plus the premium UNDERPAYS BY ONE DAY. Occasional = up to 2 rest days in a calendar month; 3 or more is habitual and gives the employee the choice of a compensatory rest day or the remuneration (arts. 179 par. 1, 180). OUT of the vacation base. TWO 2026 CUT-OVERS TWO WEEKS APART: this premium steps on 1 JULY, the 42-hour week and the 210 divisor on 15 JULY - never collapse them. A DEFECT RECORDED FOR TRACEABILITY: Circular 101 SS5.1 states a 75% premium (the pre-reform figure) after correctly stating the 80/90/100 phase-in in SS4; the SS4 schedule governs and the 75% reference must not be configured. Likewise the electronic-payroll Technical Annex v1.0 hard-codes the pre-reform 100/75/150/110 percentages - DIAN Concepto 013840 (int. 1568) de 1 octubre 2025 resolves that the annex percentage 'must be read in accordance with the rules in force for each specific case', so the engine reports the real statutory percentage. |
| Formula (col F) | (S / D) x 0.80 x H to 30 June 2026; x 0.90 from 1 July 2026; x 1.00 from 1 July 2027 - IN ADDITION TO the paid rest day itself and the hours actually worked |
| Nomina Electronica element (col Y) | Devengados / HRDDF - Cantidad (NIE096), Porcentaje (NIE097), Pago (NIE098) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-HEDDF` - Day overtime on a rest day / holiday (+105% / +115%) - *Hora Extra Diurna Dominical y Festiva*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | The art. 168 overtime premium and the art. 179 rest-day premium ARE cumulated with each other (art. 168 num. 4 bars cumulation only among the art. 168 premia themselves). Combined 2026 uplift: +105% January-June, +115% July-December. Salary, fully contributory, OUT of the vacation base, fully taxable. |
| Formula (col F) | (S / D) x (1 + 0.25 + 0.80) x H to 30 Jun 2026 = 205%; (1 + 0.25 + 0.90) = 215% from 1 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HEDDF - Cantidad (NIE091), Porcentaje (NIE092), Pago (NIE093) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-HENDF` - Night overtime on a rest day / holiday (+155% / +165%) - *Hora Extra Nocturna Dominical y Festiva*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Night overtime worked on an obligatory rest day or public holiday. Combined 2026 uplift: +155% January-June, +165% July-December. Salary, fully contributory, OUT of the vacation base, fully taxable. |
| Formula (col F) | (S / D) x (1 + 0.75 + 0.80) x H to 30 Jun 2026 = 255%; (1 + 0.75 + 0.90) = 265% from 1 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HENDF - Cantidad (NIE101), Porcentaje (NIE102), Pago (NIE103) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-HRNDF` - Night premium on a rest day / holiday (+115% / +125%) - *Recargo Nocturno Dominical y Festivo*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | The night premium on ORDINARY hours worked at night on an obligatory rest day or holiday. Being a night premium and not overtime, it STAYS IN THE VACATION BASE in respect of its 35% night component; the art. 179 rest-day component is excluded by CST art. 192. Configure the two components as separate wage types where the vacation base must be struck exactly. |
| Formula (col F) | (S / D) x (0.35 + 0.80) x H to 30 Jun 2026 = 115%; (0.35 + 0.90) = 125% from 1 Jul 2026 |
| Nomina Electronica element (col Y) | Devengados / HRNDF - Cantidad (NIE106), Porcentaje (NIE107), Pago (NIE108) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-DESCANSO-REMUNERADO` - Paid weekly rest day and paid public holidays - *Descanso Dominical y Festivo Remunerado*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | PAID REST, AND THE ONE ITEM THE PAYROLL-LEVY BASE NAMES EXPRESSLY. Ley 21 de 1982 art. 17, verified verbatim: the monthly salary payroll is 'la totalidad de los pagos hechos por concepto de los diferentes elementos integrantes del salario en los terminos de la ley laboral, cualquiera que sea su denominacion y ademas, los verificados por descansos remunerados de ley y convencionales o contractuales.' So paid rest days are IN the CCF / SENA / ICBF base by name. Also in the IBC and the statutory-benefit and vacation bases, and fully taxable. Foreign-currency payments enter the levy payroll converted at the official rate on the LAST DAY OF THE MONTH. |
| Formula (col F) | One day's ordinary salary per obligatory rest day and per statutory public holiday (CST arts. 172, 173, 177); already inside a monthly salary, itemised for daily-rated and piece-rate workers |
| Nomina Electronica element (col Y) | Devengados / Basico - SueldoTrabajado (NIE070); LicenciaR (NIE132-NIE135) where itemised |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-COMISIONES` - Commissions and sales percentages - *Comisiones y Porcentajes sobre Ventas*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | SALARY BY EXPRESS STATUTORY DEFINITION - CST art. 127 names 'porcentajes sobre ventas y comisiones'. In the IBC, the payroll-levy base, the statutory-benefit base AND THE VACATION BASE (art. 192 excludes only rest-day work and supplementary overtime hours, so commissions remain). Not prorated for a part month - paid as earned. Fully taxable. A large commission month can push the employee across the 4-SMMLV solidarity-fund trigger (7,003,620), across the 10-SMMLV exoneration line (17,509,050) or into a higher withholding band, all tested on that month's actual figures. Reported on its own nomina electronica element and on Formulario 220 casilla 41 / Formato 2276 numeral N11. |
| Formula (col F) | Contractual percentage of sales or output; enters the base of the period in which it falls due; variable pay enters the vacation base at the average of the immediately preceding year |
| Nomina Electronica element (col Y) | Devengados / Comisiones - Comision (NIE155) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-BONIF-HABITUAL` - Habitual bonus (salary) - *Bonificacion Habitual (Salarial)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 127 brings 'bonificaciones habituales' INTO salary, so a habitual bonus without a written non-salary pact enters every base. The habituality test is the audit risk: a payment repeated year on year will not survive a UGPP contribution audit as an occasional gratuity. Fully taxable in the ordinary monthly base under both procedures. |
| Formula (col F) | Contractual or customary amount paid habitually |
| Nomina Electronica element (col Y) | Devengados / Bonificacion - BonificacionS (NIE139) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-BONIF-NOSALARIAL` - Extra-statutory bonus under a written non-salary pact - *Bonificacion Extralegal No Salarial (Pacto CST art. 128)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | THE COLOMBIAN WORKHOUSE AND ITS LIMIT. Ley 1393 de 2010 art. 30, verified verbatim: 'Sin perjuicio de lo previsto para otros fines, para los efectos relacionados con los articulos 18 y 204 de la Ley 100 de 1993, los pagos laborales no constitutivos de salario de los trabajadores particulares no podran ser superiores al 40% del total de la remuneracion.' A valid pact removes the payment from the labour-law salary base PERMANENTLY - it never enters the statutory-benefit base or the overtime base - but removes it from the CONTRIBUTION base only up to 40%. The excess is added back for health, pension, the solidarity fund and occupational risk while remaining non-salary for the benefits: TWO DIVERGENT BASES, PERMANENTLY. The clamp reaches arts. 18 and 204 of Ley 100 ONLY - it does not reach the CCF / SENA / ICBF levies, which have their own Ley 21/1982 base. AND IT HAS NO TAX EFFECT WHATSOEVER: the payment remains fully taxable employment income. Any engine that treats a non-salary flag as a tax exclusion will systematically under-withhold. See also Resolucion MinProteccion 2641 de 2011. |
| Formula (col F) | Contractual amount under an EXPRESS WRITTEN non-salary pact; excluded from the IBC only up to 40% of total remuneration (Ley 1393 de 2010 art. 30), the excess forced back in |
| Nomina Electronica element (col Y) | Devengados / Bonificacion - BonificacionNS (NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-GRATIF-OCASIONAL` - Occasional gratuity (mera liberalidad) - *Gratificacion Ocasional*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 128 excludes 'las sumas que ocasionalmente y por mera liberalidad recibe el trabajador del empleador' from salary, so out of the statutory-benefit and vacation bases - but FULLY TAXABLE, and counted in the 40% clamp test as a pago laboral no constitutivo de salario. |
| Formula (col F) | One-off gratuitous amount, not habitual and not contractually owed |
| Nomina Electronica element (col Y) | Devengados / Bonificacion - BonificacionNS (NIE140) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-SALARIO-ESPECIE` - Salary in kind - *Salario en Especie*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 129, verified verbatim: 'Constituye salario en especie toda aquella parte de la remuneracion ordinaria y permanente que reciba el trabajador como contraprestacion directa del servicio, tales como alimentacion, habitacion o vestuario que el empleador suministra al trabajador o a su familia... El salario en especie debe valorarse expresamente en todo contrato de trabajo. A falta de estipulacion o de acuerdo sobre su valor real se estimara pericialmente, sin que pueda llegar a constituir y conformar mas del cincuenta por ciento (50%) de la totalidad del salario. No obstante, cuando un trabajador devengue el salario minimo legal, el valor por el concepto de salario en especie no podra exceder del treinta por ciento (30%).' Fully in the IBC, the payroll-levy base, the statutory-benefit base and the vacation base, and fully taxable. COLOMBIA HAS NO PUBLISHED BENEFIT-IN-KIND VALUATION SCALE - no company-car table, no accommodation scale, no notional-value list; the absence is principled, because art. 129 num. 2 routes an unvalued benefit to expert appraisal, not to a table. The engine therefore REQUIRES a contractual value on every in-kind wage type. There is no fringe-benefits tax and no separate benefits return. Mechanically the benefit produces a positive earnings line plus an offsetting deduction line, so net cash pay is unchanged while the withholding and contributions are correct. |
| Formula (col F) | Value stated EXPRESSLY IN THE EMPLOYMENT CONTRACT, or by expert appraisal in default of agreement; may not exceed 50% of total salary, or 30% where the employee earns the legal minimum wage |
| Nomina Electronica element (col Y) | Devengados / OtroConcepto - ConceptoS (NIE147) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-PRIMA-SERVICIOS` - Statutory service bonus - *Prima de Servicios*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-03 |
| Wage Type Explanation (col D) | CST art. 306 as amended by Ley 1788 de 2016 art. 1, universal for every private-sector employee and expressly including domestic-service employees, family-service drivers, day workers and farm workers. CST art. 307: 'La prima anual no es salario, ni se computara como factor del salario en ningun caso' - so OUT of the IBC and OUT of the payroll-levy base. Base = salary PLUS the auxilio de transporte; variable pay enters at the semester average. Set off against contractual or Christmas bonuses (CST art. 308), so an employer already paying a 13th-month equivalent does not pay twice. Absorbed by an all-inclusive salary. TAX: separate art. 383 table read under Procedure 1 for the statutory minimum; folded into the ordinary base under Procedure 2. |
| Formula (col F) | (monthly salary + auxilio de transporte) x days worked in the semester / 360 = 30 days' salary per year, 15 per semester; half by 30 JUNE and half by 20 DECEMBER; monthly accrual 8.3333% |
| Nomina Electronica element (col Y) | Devengados / Primas - Cantidad (NIE117), Pago (NIE118), PagoNS (NIE119) |
| Tax Code Source - C9 (col Z) | ET arts. 385 and 386; CST arts. 306 (as amended by Ley 1788 de 2016 art. 1), 307 and 308. |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-CESANTIAS` - Severance savings - *Auxilio de Cesantias*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-02 |
| Wage Type Explanation (col D) | Statutory benefit under CST Titles VIII-IX, excluded from salary by art. 128, so out of the IBC and the payroll-levy base. EXCLUDED FROM THE MONTHLY WITHHOLDING BASE ENTIRELY under both procedures (ET arts. 385, 386) - not merely exempt. Exempt in full where the average monthly income of the last six months is <= 350 UVT (18,330,900), then tapering 90 / 80 / 60 / 40 / 20 / 0% through 650 UVT (ET art. 206 num. 4); the 25% exemption of art. 206 num. 10 does NOT apply (art. 206 par. 2). LATE DEPOSIT COSTS ONE DAY'S SALARY PER DAY OF DELAY (Ley 50 de 1990 art. 99 num. 3). Ley 2466 de 2025 art. 64 adds a paragraph to Ley 50 art. 99 permitting the employer to deposit 8.33% of the base monthly as an ADVANCE DEPOSIT - verified verbatim: 'En ningun caso la consignacion anticipada podra entenderse como pago parcial de la cesantia, pues el trabajador solo tendra acceso a la cesantia anticipada en los terminos que asi lo determine la Ley o a la terminacion del contrato de trabajo.' Reported on three SEPARATE lines of the information return - paid to the employee (N18), deposited to the fund (N19) and recognised under the traditional regime (N20). |
| Formula (col F) | (monthly salary + auxilio de transporte) x days of service / 360 = one month's salary per year; monthly accrual 8.3333%; liquidated at 31 December and DEPOSITED TO THE FUND BY 14 FEBRUARY |
| Nomina Electronica element (col Y) | Devengados / Cesantias - Pago (NIE120); Consignacion Cesantias T14 |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 4 and par. 2, 385, 386; Ley 50 de 1990 art. 99; Ley 52 de 1975 art. 1; Ley 2466 de 2025 art. 64 (8.33% monthly advance deposit). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-INTERESES-CESANTIAS` - Interest on severance savings - *Intereses a las Cesantias*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-02 |
| Wage Type Explanation (col D) | Ley 52 de 1975 art. 1. Statutory benefit, out of the IBC and the payroll-levy base, and excluded from the monthly withholding base under both procedures, carrying the same art. 206 num. 4 exemption and taper as the principal. PAID TO THE EMPLOYEE DIRECTLY, NOT TO THE FUND - unlike the principal. Failure to pay it costs an indemnity equal to the interest owed, once only. |
| Formula (col F) | cesantias balance at 31 December x 12% per year x days / 360; monthly accrual 1.0000%; PAID TO THE EMPLOYEE DURING JANUARY (optionally monthly at 1% by written agreement, Ley 2466 de 2025 art. 64) |
| Nomina Electronica element (col Y) | Devengados / Cesantias - Porcentaje (NIE121), PagoIntereses (NIE122) |
| Tax Code Source - C9 (col Z) | ET arts. 206 num. 4 and par. 2, 385, 386; Ley 50 de 1990 art. 99; Ley 52 de 1975 art. 1; Ley 2466 de 2025 art. 64 (8.33% monthly advance deposit). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-VACACIONES` - Annual leave taken - *Vacaciones Disfrutadas*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | VACATION IS NOT A PRESTACION SOCIAL - IT IS PAID REST, and every consequence is counter-intuitive. It ENTERS THE IBC (contributions continue during leave; PILA change event VAC/LR) and ENTERS THE PAYROLL-LEVY BASE (Ley 21/1982 art. 17 covers descansos remunerados by name). Its own base excludes overtime and rest-day work ONLY - CST art. 192, verified verbatim: 'solo se excluiran para la liquidacion de vacaciones el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras' - so the NIGHT PREMIUM AND COMMISSIONS STAY IN. The auxilio de transporte is NOT in the vacation base. AN ALL-INCLUSIVE SALARY DOES NOT ABSORB IT (CST art. 132 num. 2 expressly excepts vacation), so vacation is owed on the FULL 100% while contributions run on 70%. Fully taxable. Accrual suspended during unpaid leave. |
| Formula (col F) | (ordinary salary EXCLUDING overtime and rest-day work) x working days of vacation / 30; entitlement 15 WORKING days per year of service; accrual = salary x days / 720; variable pay -> average of the immediately preceding year |
| Nomina Electronica element (col Y) | Devengados / VacacionesComunes - FechaInicio (NIE109), Cantidad (NIE111), Pago (NIE112) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-VACACIONES-COMPENSADAS` - Vacation compensated in cash - *Compensacion en Dinero de Vacaciones*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Cash compensation of vacation is paid rest on the same footing as leave actually taken: IN the IBC and IN the payroll-levy base, fully taxable. It is THE MOST COMMONLY MISSED CONTRIBUTORY LINE IN A TERMINATION SETTLEMENT - accrued vacation paid in cash on termination is contributory, whereas the accrued prima, cesantias, interest and the dismissal indemnity are not. Requires the employee's prior written request; the employer may not impose it. |
| Formula (col F) | Up to HALF the accrued leave, on the employee's PRIOR WRITTEN REQUEST (CST art. 189 num. 1); same base as vacation taken |
| Nomina Electronica element (col Y) | Devengados / VacacionesCompensadas - Cantidad (NIE115), Pago (NIE116) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-DOTACION` - Work clothing and footwear - *Dotacion de Labor (Calzado y Vestido)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | CST art. 230 as modified by Ley 11 de 1984 art. 7, verified verbatim: 'Todo empleador que habitualmente ocupe uno (1) o mas trabajadores permanentes, debera suministrar cada cuatro (4) meses, en forma gratuita, un (1) par de zapatos y un (1) vestido de labor al trabajador, cuya remuneracion mensual sea hasta dos (2) meses el salario minimo mas alto vigente. Tiene derecho a esta prestacion el trabajador que en las fechas de entrega de calzado y vestido haya cumplido mas de tres (3) meses al servicio del empleador.' Delivery dates from art. 232. Provided to enable the work, so NOT salary, NOT taxable, and outside every base - the one item on the payslip that is genuinely nil across all five columns. The nomina electronica gives it a DEDICATED informational element. Where owed but undelivered and settled in cash on termination it remains non-taxable. |
| Formula (col F) | One pair of shoes and one work outfit FREE OF CHARGE every four months (three deliveries a year) to employees whose monthly remuneration is up to 2 SMMLV (3,501,810) and who have more than three months' service; delivered on 30 APRIL, 31 AUGUST and 20 DECEMBER |
| Nomina Electronica element (col Y) | Devengados / Dotacion (NIE156) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-INCAP-EG-EMPLEADOR` - Sickness incapacity, days 1-2 (employer) - *Incapacidad por Enfermedad General - Dias 1 y 2 (Empleador)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Decreto 2943 de 2013 art. 1, compiled at Decreto 780 de 2016 art. 3.2.1.10, allocates 'las prestaciones economicas correspondientes a los dos (2) primeros dias de incapacidad originada por enfermedad general' to the EMPLOYER but does NOT state the rate. CST art. 227 sets the auxilio at two thirds for the first 90 days and market practice applies 66.67% for days 1-2 on that basis; a minority practice pays 100%. MERCANS DEFAULT 66.67%, CONFIGURABLE - an open item carried in the QA report, together with the minimum-wage top-up floor where 66.67% of salary falls below one SMMLV, whose primary regulatory source was not retrieved this pass. Not salary, but IN the IBC, IN the payroll-levy base and IN the statutory-benefit base, and taxable. The auxilio de transporte is NOT paid for sick days. |
| Formula (col F) | S / 30 x 0.6667 x d for the first two days, floored at the minimum-wage equivalent (Mercans default 66.67%, configurable) |
| Nomina Electronica element (col Y) | Devengados / Incapacidad - Tipo (NIE126) = enfermedad general, Pago (NIE127); PILA T2R2-025 |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-INCAP-EG-EPS` - Sickness incapacity from day 3 (EPS) - *Incapacidad por Enfermedad General - desde el Dia 3 (EPS)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-07 |
| Wage Type Explanation (col D) | Paid by the EPS, in practice ADVANCED by the employer through payroll and recovered from the insurer. Not employer salary, so OUT of the payroll-levy base - but CONTRIBUTIONS CONTINUE ON THE BASE (PILA change event IGE), so it is in the IBC column. Exempt within the statutory minimum (ET art. 206 nums. 1-2 and par. 1, which limits the exemption to 'las cantidades que correspondan al minimo legal' and taxes the excess). The PILA carries the incapacity authorisation number and value (T2R2-057, T2R2-058) so the employer can offset the recovery. |
| Formula (col F) | IBC / 30 x 0.6667 x d for days 3-90 and x 0.50 for days 91-180, floored at the minimum-wage equivalent; variable salary -> average of the year of service preceding the incapacity (CST art. 228) |
| Nomina Electronica element (col Y) | Devengados / Incapacidad - Cantidad (NIE125), Pago (NIE127); PILA T2R2-057, T2R2-058 |
| Tax Code Source - C9 (col Z) | ET art. 206 nums. 1, 2, 3 and par. 1; CST arts. 227, 236; Decreto 780 de 2016 art. 3.2.1.10 (Decreto 2943 de 2013 art. 1, employer days 1-2). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-INCAP-IRL` - Occupational accident or disease incapacity (ARL) - *Incapacidad de Origen Laboral (ARL)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-07 |
| Wage Type Explanation (col D) | Paid by the ARL at 100% of the IBC from the day after the event - there is no employer-borne waiting period as there is for general illness. Not employer salary, out of the payroll-levy base, contributions continue on the base (PILA change event IRL), exempt within the statutory minimum. NOTE the coverage gate: occupational-risk cover starts the CALENDAR DAY AFTER affiliation (Decreto 1072 de 2015 art. 2.2.4.2.5.4) and a new hire must be reported to the ARL no later than the business day following the start date (art. 2.2.4.3.6) - an employee who starts work before affiliation is uninsured and THE EMPLOYER BEARS THE BENEFIT DIRECTLY. |
| Formula (col F) | IBC / 30 x 1.00 x d from the DAY AFTER the event, at 100% of the contribution base |
| Nomina Electronica element (col Y) | Devengados / Incapacidad - Tipo (NIE126) = riesgos laborales; PILA T2R2-030, T2R2-093, T2R2-094 |
| Tax Code Source - C9 (col Z) | ET art. 206 nums. 1, 2, 3 and par. 1; CST arts. 227, 236; Decreto 780 de 2016 art. 3.2.1.10 (Decreto 2943 de 2013 art. 1, employer days 1-2). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-LIC-MATERNIDAD` - Maternity leave (18 weeks) - *Licencia de Maternidad (18 semanas)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-07 |
| Wage Type Explanation (col D) | CST art. 236. Paid by the EPS, advanced by the employer and recovered. Not employer salary, out of the payroll-levy base, contributions CONTINUE on the base (PILA change event LMA), exempt within the statutory minimum (ET art. 206 num. 2 and par. 1). The auxilio de transporte is not payable. Dismissal during the protected period without labour-inspector authorisation costs 180 days' salary (art. 239). |
| Formula (col F) | S / 30 x 126 calendar days, at the salary earned when the leave begins; variable salary -> average of the last year |
| Nomina Electronica element (col Y) | Devengados / LicenciaMP - Cantidad (NIE130), Pago (NIE131); PILA T2R2-059, T2R2-060 |
| Tax Code Source - C9 (col Z) | ET art. 206 nums. 1, 2, 3 and par. 1; CST arts. 227, 236; Decreto 780 de 2016 art. 3.2.1.10 (Decreto 2943 de 2013 art. 1, employer days 1-2). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-LIC-PATERNIDAD` - Paternity leave (2 weeks) - *Licencia de Paternidad (2 semanas)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-07 |
| Wage Type Explanation (col D) | CST art. 236 par. 1. Paid by the EPS, advanced and recovered. Documentation is exacting - art. 236 par. 2 requires the CIVIL REGISTRATION OF BIRTH, to be delivered to the EPS within 30 days of the birth. Not employer salary, out of the payroll-levy base, contributions continue, exempt within the statutory minimum. |
| Formula (col F) | S / 30 x 14 calendar days at full salary; the leave expands by one week per percentage point of structural-unemployment reduction, capped at 5 weeks |
| Nomina Electronica element (col Y) | Devengados / LicenciaMP - Cantidad (NIE130), Pago (NIE131) |
| Tax Code Source - C9 (col Z) | ET art. 206 nums. 1, 2, 3 and par. 1; CST arts. 227, 236; Decreto 780 de 2016 art. 3.2.1.10 (Decreto 2943 de 2013 art. 1, employer days 1-2). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-LIC-PARENTAL-COMPARTIDA` - Shared and flexible parental leave - *Licencia Parental Compartida y Flexible*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-07 |
| Wage Type Explanation (col D) | CST art. 236 pars. 6-7. Paid by the EPS on the same footing as maternity and paternity leave: not employer salary, out of the payroll-levy base, contributions continue on the base, exempt within the statutory minimum. The engine must carry the parental election and the transferred week count, since the leave moves BETWEEN two employees who may be at different employers. |
| Formula (col F) | Transferred weeks of the maternity entitlement, paid on the transferring or receiving parent's own salary base as the election provides |
| Nomina Electronica element (col Y) | Devengados / LicenciaMP - Cantidad (NIE130), Pago (NIE131) |
| Tax Code Source - C9 (col Z) | ET art. 206 nums. 1, 2, 3 and par. 1; CST arts. 227, 236; Decreto 780 de 2016 art. 3.2.1.10 (Decreto 2943 de 2013 art. 1, employer days 1-2). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-LIC-REMUNERADA` - Statutory paid leave (CST art. 57 num. 6) - *Licencia Remunerada Legal (CST art. 57 num. 6)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 57 num. 6 as modified by Ley 2466 de 2025 art. 15 - paid leave for exercising the vote, holding a transitory official post of compulsory acceptance, grave domestic calamity, attending a union commission, medical and dental appointments, school obligations of the employee's children, judicial summonses, and the bicycle-commuting rest day. PAID REST, so IN the IBC, IN the payroll-levy base (descansos remunerados de ley, Ley 21/1982 art. 17), IN the statutory-benefit base and IN the vacation base, and fully taxable. Employer-borne, not EPS-borne. |
| Formula (col F) | S / 30 x days of leave, at full ordinary salary |
| Nomina Electronica element (col Y) | Devengados / LicenciaR - Cantidad (NIE134), Pago (NIE135); PILA T2R2-027 (VAC-LR) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-LIC-LUTO` - Bereavement leave (5 working days) - *Licencia de Luto (5 dias habiles)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 57 num. 10 (Ley 1280 de 2009): five WORKING days on the death of a spouse or permanent partner, or a relative within the second degree of consanguinity, the first of affinity or the first civil. Employer-borne paid rest: in the IBC, the payroll-levy base, the statutory-benefit base and the vacation base, and fully taxable. |
| Formula (col F) | S / 30 x 5 working days, at full ordinary salary |
| Nomina Electronica element (col Y) | Devengados / LicenciaR - Cantidad (NIE134), Pago (NIE135) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-LIC-NO-REMUNERADA` - Unpaid leave / contract suspension - *Licencia No Remunerada / Suspension del Contrato (SLN)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Reported with the SLN change event, which reduces the contributory days. The Resolucion 2388 de 2016 rate table shows health moving to 8.5% or 0% and pension to 12% or 16% depending on the variant, and THE PAYROLL LEVIES FALLING TO 0%. Statutory-benefit and vacation accrual are SUSPENDED, though CST art. 53 lets the employer count the period for cesantias and pension purposes if it pays the corresponding contributions, and the period is charged against vacation. The month's taxable payments fall, so the withholding follows automatically. |
| Formula (col F) | -(S x unpaid days / 30); the auxilio de transporte is likewise not payable for those days |
| Nomina Electronica element (col Y) | Devengados / LicenciaNR (NIE136-NIE138); PILA T2R2-024, T2R2-083, T2R2-084 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-HUELGA-LEGAL` - Legal strike days - *Huelga Legal*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | A lawful strike suspends the contract, so the days are unpaid and accrual is suspended on the same footing as unpaid leave. The nomina electronica carries a dedicated HuelgaLegal block with start date, end date and day count, so the days must be tracked separately from ordinary unpaid leave. |
| Formula (col F) | Unpaid for the duration of the lawful strike; days reported for the period |
| Nomina Electronica element (col Y) | Devengados / HuelgaLegal - FechaInicio (NIE143), Cantidad (NIE145) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-APOYO-APRENDIZ` - Apprentice maintenance support - *Apoyo de Sostenimiento del Aprendiz*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 81 as substituted by Ley 2466 de 2025 art. 21, verified verbatim: 'Si es una formacion dual, el aprendiz recibira como minimo durante el primer ano el equivalente al setenta y cinco por ciento (75%) de un (1) salario minimo legal mensual vigente y durante el segundo ano el equivalente al cien por ciento (100%)... Si es formacion tradicional, el aprendiz recibira como minimo en la fase lectiva el equivalente al setenta y cinco por ciento (75%)... y en la parte practica, el apoyo del sostenimiento sera equivalente al cien por ciento (100%).' NOT the minimum wage as such - a maintenance support payment expressed as a percentage of it. SPECIAL CONTRIBUTION REGIME: Decreto 0223 de 5 marzo 2026 art. 2.2.6.3.3.4 par. 2 provides that 'en todo caso la base de cotizacion debe ser [de] un (1) salario minimo legal mensual vigente', so an apprentice on 75% of the SMMLV nonetheless contributes on a FULL minimum wage. The CLASSROOM phase carries health and occupational risk ONLY; the PRACTICAL or DUAL phase carries the full IBC, the payroll-levy base, the statutory-benefit base and the vacation base. Taxable. Medical-intern remuneration under CST art. 81A (Ley 2466 art. 22) is paid by the health system resource administrator and is OUT OF SCOPE per scope_manifest. |
| Formula (col F) | DUAL training: 75% of SMMLV = 1,313,178.75 in year 1, 100% = 1,750,905 in year 2. TRADITIONAL training: 75% in the classroom phase, 100% in the practical phase. University student: 100% minimum |
| Nomina Electronica element (col Y) | Devengados / ApoyoSost (NIE157); Decreto 0223 de 2026 art. 2.2.6.3.3.4 |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-INDEM-DESPIDO` - Indemnity for dismissal without just cause - *Indemnizacion por Despido sin Justa Causa (CST art. 64)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 64 as amended by Ley 789 de 2002 art. 28. FULLY TAXABLE ordinary employment income entering the ordinary monthly base - ET art. 206 nums. 1-3 exempt only accident, illness and maternity-protection indemnities and art. 206 par. 1 limits even those to the statutory minimum amount, so an art. 64 indemnity has NO tax-free portion and Colombia has NO concessional cap on termination payments. OUT of the IBC, the payroll-levy base, the statutory-benefit base and the vacation base. Employees with 10 or more years of continuous service at the entry into force of Ley 789 de 2002 retain the earlier Ley 50 de 1990 art. 6 literals b), c) and d) scale. THE EASILY MISSED GATE - CST art. 65 par. 1: the employer must inform the employee in writing within 60 days of the termination of the payment status of the contributions on the last three months' salaries, attaching the receipts, and 'si el empleador no demuestra el pago de dichos aportes, la terminacion del contrato no producira efecto'; the employer may still pay within a further 60 days with default interest. CST art. 66 requires the cause to be stated AT THE MOMENT of termination. |
| Formula (col F) | Salary BELOW 10 SMMLV (< 17,509,050): 30 days' salary for the first year, PLUS 20 days for each subsequent year and pro rata. Salary AT OR ABOVE 10 SMMLV: 20 days, PLUS 15 days |
| Nomina Electronica element (col Y) | Devengados / Indemnizacion (NIE160) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-INDEM-MORATORIA` - Late-payment penalty - *Indemnizacion Moratoria (CST art. 65)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 65 as amended by Ley 789 de 2002 art. 29, payable where salaries and statutory benefits are unpaid at termination. FULLY TAXABLE, out of every social-security base. NOTE THE SPLIT: the 24-month cap and the subsequent default interest apply to employees earning one SMMLV or more; those earning LESS remain on the uncapped pre-2002 rule, which can produce a materially larger liability. |
| Formula (col F) | One day's salary for each day of delay, up to 24 months, then default interest at the maximum free-allocation credit rate; employees earning LESS THAN 1 SMMLV stay on the UNCAPPED original rule (CST art. 65 par. 2) |
| Nomina Electronica element (col Y) | Devengados / Indemnizacion (NIE160) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-SANCION-CESANTIAS` - Penalty for non-deposit of severance savings - *Sancion por No Consignacion de Cesantias*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | A distinct statutory penalty from the CST art. 65 moratoria and cumulable with it. Fully taxable, out of every social-security base. Triggered by failure to deposit the 31 December cesantias balance to the employee's chosen fund by 14 February - one of the two hard year-end dates in Colombian payroll. |
| Formula (col F) | One day's salary for each day of delay beyond 14 February (Ley 50 de 1990 art. 99 num. 3) |
| Nomina Electronica element (col Y) | Devengados / Indemnizacion (NIE160) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-SANCION-INTERESES` - Penalty for unpaid severance interest - *Sancion por No Pago de Intereses a las Cesantias*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Ley 52 de 1975 art. 1: where the employer fails to pay the 12% interest it must pay the employee, 'a titulo de indemnizacion y por una sola vez', an amount equal to the interest owed. Fully taxable, out of every social-security base. The interest itself is paid TO THE EMPLOYEE during January, not to the fund - the most common cause of this penalty is treating it like the principal. |
| Formula (col F) | An amount EQUAL TO the interest owed, payable ONCE ONLY (Ley 52 de 1975 art. 1) |
| Nomina Electronica element (col Y) | Devengados / Indemnizacion (NIE160) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-INDEM-FIJO-OBRA` - Indemnity for early termination of a fixed-term or work-or-task contract - *Indemnizacion por Terminacion Anticipada de Contrato a Termino Fijo u Obra o Labor*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 64. Fully taxable ordinary employment income, out of every social-security base. The 15-day floor on a work-or-task contract is absolute and applies however short the remaining term. |
| Formula (col F) | Fixed-term: the salaries for the remaining term. Work or task: the remaining term of the work, NEVER LESS THAN 15 DAYS |
| Nomina Electronica element (col Y) | Devengados / Indemnizacion (NIE160) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-INDEM-PROTECCION` - Indemnity for dismissal during protected status - *Indemnizacion por Despido en Estado de Proteccion (Fuero)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Fully taxable, out of every social-security base. Distinct from and additional to the art. 64 indemnity. The disability protection carries REINSTATEMENT as well as the indemnity, so the engine must be able to reverse a termination and restore contributions retroactively. |
| Formula (col F) | 180 days' salary for a pregnant or nursing employee (CST art. 239); 180 days' salary PLUS reinstatement for an employee with a disability dismissed without labour-inspector authorisation (Ley 361 de 1997 art. 26) |
| Nomina Electronica element (col Y) | Devengados / Indemnizacion (NIE160) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-BONIF-RETIRO` - Retirement or mutual-termination settlement bonus - *Bonificacion por Retiro / Acuerdo de Terminacion*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | An occasional, gratuitous sum under CST art. 128, so out of every social-security base - but FULLY TAXABLE, and FREQUENTLY AND WRONGLY ASSUMED EXEMPT. A payment in lieu of notice is on the same footing (there is no statutory employer notice period in Colombia). A non-compete payment is generally not salary but is likewise fully taxable. The nomina electronica gives the retirement bonus a dedicated element, separate from Indemnizacion. |
| Formula (col F) | Negotiated contractual amount; no statutory retirement gratuity exists in Colombia |
| Nomina Electronica element (col Y) | Devengados / BonifRetiro (NIE159) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-PAGO-ALIMENTACION-3P` - Third-party meal payments - *Pagos de Alimentacion a Terceros*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-05 |
| Wage Type Explanation (col D) | ET art. 387-1. Payments made by the employer TO A THIRD PARTY for the food of the employee or the employee's family - spouse or permanent partner, children and parents - including the purchase of meal vouchers or tickets. TWO INDEPENDENT CONDITIONS, BOTH MUST HOLD: the salary ceiling AND payment to a third party. CASH PAID TO THE EMPLOYEE FOR FOOD IS SALARY AND GETS NONE OF THIS TREATMENT. Within the limit it is income to the third party supplying the food, not to the employee. Not salary, so out of every social-security base. Representation expenses are expressly outside this rule. The information return reports the within-limit amount and the excess on SEPARATE numerals (N32 and N08), so the engine must carry two accumulators, not one. |
| Formula (col F) | NOT income up to 41 UVT/month = 2,147,334 where the employee's salary does NOT exceed 310 UVT = 16,235,940; the EXCESS over 41 UVT is taxable employment income |
| Nomina Electronica element (col Y) | Devengados / BonoEPCTV - PagoAlimentacionS (NIE153) / PagoAlimentacionNS (NIE154) |
| Tax Code Source - C9 (col Z) | ET art. 387-1; Formato 2276 v4 numerals N08 (excess) and N32 (within-limit amount), which report the two portions separately; Formulario 220 casillas 37 and 38. |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-BONO-EPCTV` - Voucher, card or non-cash instrument payment - *Pago con Bonos Electronicos o de Papel, Cheques, Tarjetas o Vales*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | The nomina electronica carries PAIRED salary and non-salary voucher elements, so the engine must set the salary flag at configuration and must not derive it at reporting time. Where the instrument delivers FOOD through a third party the ET art. 387-1 regime applies instead (see CO-PAGO-ALIMENTACION-3P); where it delivers anything else it is remuneration, taxable in full, and salary unless a valid written art. 128 pact applies. Reported at Formulario 220 casilla 37 / Formato 2276 numeral N07. |
| Formula (col F) | Face value of the instrument; salary or non-salary according to the CST art. 127 / 128 classification of the underlying payment |
| Nomina Electronica element (col Y) | Devengados / BonoEPCTV - PagoS (NIE151) / PagoNS (NIE152) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-MEDICINA-PREPAGADA-ER` - Employer-paid prepaid health / supplementary health plan - *Medicina Prepagada o Plan Complementario Pagado por el Empleador*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | NOT a statutory exclusion - a TAXABLE benefit to the employee, reported as an earnings line and withheld in the ordinary monthly base, with an offsetting deduction line so net cash pay is unchanged. The employee separately obtains the art. 387 deduction of up to 16 UVT per month on a provider certificate, where the provider is supervised by the NATIONAL HEALTH SUPERINTENDENCE (prepaid medicine) or the FINANCIAL SUPERINTENDENCE (health insurance). Market practice structures the employer premium as non-salary under a written art. 128 pact, which keeps it out of the IBC up to the 40% clamp. It does NOT replace the compulsory 12.5% health contribution. |
| Formula (col F) | Premium paid by the employer; the employee may deduct up to 16 UVT/month = COP 837,984 against the withholding base (ET art. 387 lits. a and b) |
| Nomina Electronica element (col Y) | Devengados / Auxilio - AuxilioNS (NIE142); Deducciones / PlanComplementarios (NIE182) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-APORTE-PENSION-VOL-ER` - Employer contribution to a voluntary pension fund - *Aporte Patronal a Fondo de Pensiones Voluntarias*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-09 |
| Wage Type Explanation (col D) | EXEMPT INCOME to the employee, subtracted at step (E) of the art. 388 depuration INSIDE the 40% and 1,340-UVT caps. Treated as the employee's own contribution for cap purposes. Deductible for the employer up to 3,800 UVT per employee (art. 126-1 first paragraph). NO OCCUPATIONAL PENSION SCHEME EXISTS IN COLOMBIA in the defined-benefit or defined-contribution sense - the mandatory system is universal and the voluntary fund is an individual product to which an employer may contribute, not an employer-sponsored plan with its own trustees. |
| Formula (col F) | Amount contributed, within the SHARED cap of the lower of 30% of labour income or 3,800 UVT per year = COP 199,021,200 (ET arts. 126-1 and 126-4, shared with AFC / AVC) |
| Nomina Electronica element (col Y) | Devengados / Auxilio - AuxilioNS (NIE142); Formulario 220 casilla 56 / Formato 2276 N26 |
| Tax Code Source - C9 (col Z) | ET arts. 126-1 and 126-4; ET art. 388 num. 2; Formulario 220 casillas 56, 57 and 58; Formato 2276 v4 numerals N26, N27 and N28. |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-APORTE-RAIS-VOL-ER` - Employer voluntary contribution to the individual pension account - *Cotizacion Voluntaria al RAIS pagada por el Empleador*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-04 |
| Wage Type Explanation (col D) | NON-TAXABLE INCOME (ingreso no constitutivo de renta ni ganancia ocasional) under ET art. 55, subtracted at step (B) of the depuration - BEFORE the 40% cap reference figure is struck, which makes it MATERIALLY MORE VALUABLE than exempt income. Distinguish it carefully from the voluntary pension FUND contribution of art. 126-1, which is exempt income inside the caps. A withdrawal that does not meet the qualifying conditions is WITHHELD AT 35%. Reported on the PILA as the AVP change event. |
| Formula (col F) | Amount contributed, within the lower of 25% of annual labour income or 2,500 UVT per year = COP 130,935,000 (ET art. 55) |
| Nomina Electronica element (col Y) | Devengados / Auxilio - AuxilioNS (NIE142); PILA T2R2-028, T2R2-049; Formato 2276 N25 |
| Tax Code Source - C9 (col Z) | ET arts. 55 and 56; ET art. 388 num. 1; Formato 2276 v4 numerals N23 and N24 (which group the pension and solidarity-fund contributions on a single line). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-ACCIONES` - Equity and share-incentive awards - *Acciones e Incentivos en Acciones*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | TAXABLE EMPLOYMENT INCOME AT EXERCISE OR VESTING, on the spread, in the ordinary monthly base and the art. 383 table. The subsequent disposal is a separate capital transaction outside payroll. Generally non-salary, so out of the statutory-benefit and vacation bases, but counted in the 40% clamp test. Colombia has no notional valuation scale, so the market value must be evidenced. For a non-resident, ET art. 408 applies at 20% where the underlying service was performed in Colombia; where performed abroad the income is foreign-source and not taxable in Colombia. |
| Formula (col F) | Taxable spread = market value at exercise or vesting LESS the exercise price paid by the employee |
| Nomina Electronica element (col Y) | Devengados / OtroConcepto - ConceptoS or ConceptoNS (NIE146-NIE148) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-VIATICOS-PERMANENTES` - Permanent per diem - board and lodging portion (salary) - *Viaticos Permanentes - Manutencion y Alojamiento (Salarial)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CST art. 130 as modified by Ley 50 de 1990 art. 17, verified verbatim: 'Los viaticos permanentes constituyen salario en aquella parte destinada a proporcionar al trabajador manutencion y alojamiento; pero no en lo que solo tenga por finalidad proporcionar los medios de transporte o los gastos de representacion. Siempre que se paguen debe especificarse el valor de cada uno de estos conceptos.' This portion is SALARY: in the IBC, the payroll-levy base, the statutory-benefit base and the vacation base, and fully taxable. The nomina electronica enforces the split with paired elements, so configure TWO wage types and never one. Reported at Formulario 220 casilla 43 / Formato 2276 numeral N13. |
| Formula (col F) | The part of a PERMANENT per diem destined to provide the employee MANUTENCION and ALOJAMIENTO; the value of each concept must be specified whenever paid (CST art. 130) |
| Nomina Electronica element (col Y) | Devengados / Transporte - ViaticoManuAlojS (NIE072) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-VIATICOS-OCASIONALES` - Occasional per diem, and the transport / representation portion - *Viaticos Accidentales y Porcion de Transporte y Representacion (No Salarial)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | CST art. 130 final paragraph: 'Los viaticos accidentales no constituyen salario en ningun caso. Son viaticos accidentales aquellos que solo se dan con motivo de un requerimiento extraordinario, no habitual o poco frecuente.' Neither salary nor taxable income where it is a genuine reimbursement of employer expenditure - outside every base. Representation expenses are also expressly outside the ET art. 387-1 meal rule and are deductible for the employer. |
| Formula (col F) | Occasional per diem paid on an extraordinary, non-habitual or infrequent requirement, and the portion of any per diem destined only to transport or representation expenses |
| Nomina Electronica element (col Y) | Devengados / Transporte - ViaticoManuAlojNS (NIE073) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-TELETRABAJO` - Telework allowance - *Auxilio de Teletrabajo*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | Where the payment REIMBURSES documented telework costs incurred in the employer's interest it falls under CST art. 128 as an amount given to enable the work and is outside every base. Where it is a round, undocumented monthly amount it is remuneration - salary unless a valid written art. 128 pact applies, and taxable either way. Configured here as a pacted non-salary allowance, the market default. Distinguish the STATUTORY auxilio de conectividad for teleworkers earning less than 2 SMMLV, which replaces the transport allowance (see CO-AUX-CONECTIVIDAD). The telework mode - autonomous, mobile or supplementary - must be declared in the telework agreement. |
| Formula (col F) | Contractual amount toward the cost of the telework arrangement (energy, internet, workstation), distinct from the statutory auxilio de conectividad |
| Nomina Electronica element (col Y) | Devengados / Teletrabajo (NIE158) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-PROPINAS` - Tips - *Propinas*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | CST art. 131, verified verbatim: 'Las propinas que recibe el trabajador no constituye salario. No puede pactarse como retribucion del servicio prestado por el trabajador lo que este reciba por propinas.' Tips are not an employer payment at all, so they are outside every base and outside employer payroll. Retained as an informational line because a hospitality-sector client will report them, and because an attempt to treat tips as part of the contractual salary is unlawful and must be blocked at configuration. |
| Formula (col F) | Amounts received by the employee from customers; may NOT be stipulated as remuneration for the service |
| Nomina Electronica element (col Y) | Not a nomina electronica devengado (not an employer payment) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-COMPENSACION-COOP` - Cooperative associated-work compensation - *Compensacion Ordinaria y Extraordinaria del Trabajo Asociado Cooperativo*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | OUT OF SCOPE of an employment payroll: an associated worker of a cooperative is not an employee and there is no employment contract, so CST arts. 127 / 128 do not apply and the contribution regime is the independent-worker one. Retained because the nomina electronica carries dedicated elements and the information return a dedicated numeral (N15 / Formulario 220 casilla 45), and because a client operating a cooperative will present the concept. Configured outside every employment base. |
| Formula (col F) | Ordinary and extraordinary compensation fixed by the cooperative's own compensation regime |
| Nomina Electronica element (col Y) | Devengados / Compensacion - CompensacionO (NIE149) / CompensacionE (NIE150) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-PAGO-TERCERO` - Third-party payment (accrued) - *Pago a Terceros (Devengado)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | The nomina electronica carries PagoTercero in BOTH the devengados (NIE193) and the deducciones (NIE195) blocks, so the two legs net to zero in net pay while the accrued value is correctly reported. The underlying payment must still be classified on its own facts under CST arts. 127 / 128 and taxed accordingly - the third-party route changes the payment mechanics, not the classification. A meal payment to a third party has its own ET art. 387-1 regime. |
| Formula (col F) | Amount the employer pays to a third party on the employee's behalf and reports as accrued |
| Nomina Electronica element (col Y) | Devengados / PagosTerceros - PagoTercero (NIE193) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-ANTICIPO-NOMINA` - Payroll advance (accrued) - *Anticipo de Nomina (Devengado)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-01 |
| Wage Type Explanation (col D) | CONDITIONAL BY DESIGN. An advance OF the period's salary is salary and enters every base in the period to which it relates; a recoverable advance or loan is not remuneration at all, and the paired devengado / deduccion elements let the two legs net to zero. CST art. 151 requires the instalment and amortisation period to be agreed in writing and bars unilateral variation; art. 149 num. 2 bars any recovery that would breach the SMMLV floor or the non-attachable portion without a court order, in which case the instalment must be SUSPENDED and carried forward with the arrears made visible on the payslip - never silently rescheduled. |
| Formula (col F) | Advance of the period's pay, or a recoverable advance repaid by deduction under a written CST art. 151 agreement stating the instalment and the amortisation period |
| Nomina Electronica element (col Y) | Devengados / Anticipos - Anticipo (NIE194) |
| Tax Code Source - C9 (col Z) | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-REINTEGRO` - Reimbursement to the employee (accrued) - *Reintegro (Devengado)*

| Attribute | Value |
|---|---|
| Category (col E) | Earning |
| Tax Code (col G) | CO-TX-06 |
| Wage Type Explanation (col D) | A reimbursement is not remuneration and is outside every base. WHERE IT REVERSES AN OVER-WITHHELD TAX the route is Decreto 1625 de 2016 art. 1.2.4.16: on the employee's WRITTEN REQUEST with evidence, the employer reimburses the excess and DEDUCTS THE REIMBURSED AMOUNT FROM THE WITHHOLDINGS OF THE FOLLOWING PERIOD, carrying any surplus forward until absorbed, and must keep the written request. Where it reverses an over-paid contribution, Mercans practice is to reimburse the employee promptly on the employer's authority and pursue recovery from the receiving entity separately, because the correction planilla is structurally built for under-declaration (the C-record bases and day counts must be >= the A-record ones). |
| Formula (col F) | Amount returned to the employee for a prior over-deduction or an expense borne on the employer's behalf |
| Nomina Electronica element (col Y) | Devengados / Reintegro (NIE201); Deducciones / Reintegro (NIE184) |
| Tax Code Source - C9 (col Z) | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-DED-SALUD` - Health contribution (employee) 4% - *Aporte a Salud - Empleado (4%)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Ley 100 de 1993 art. 204 as substituted by Ley 1122 de 2007 art. 10 (total 12.5%: employee 4% + employer 8.5%). Base = the IBC, floor 1 SMMLV (1,750,905), ceiling 25 SMMLV (43,772,625), so the maximum monthly amount is 1,750,905. NON-TAXABLE INCOME to the employee (ET art. 56), subtracted at step (B) of the art. 388 depuration BEFORE the 40% cap reference figure is struck. Payable by every employee, including an employed old-age pensioner. Rounds UP to the next multiple of 100 - one of the THREE ROUNDING REGIMES coexisting in a single Colombian payroll month, alongside the nomina electronica's round-half-to-even with a +/-2.00 tolerance and the DIAN forms' rounding to the nearest 1,000 (ET art. 577). Never unify them. |
| Formula (col F) | IBC x 4.00%, rounded UP to the next multiple of 100 (Decreto 1990 de 2016 art. 1) |
| Nomina Electronica element (col Y) | Deducciones / Salud - Porcentaje (NIE161), Deduccion (NIE163); PILA T2R2-054, T2R2-055 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-PENSION` - Mandatory pension contribution (employee) 4% - *Aporte a Pension Obligatoria - Empleado (4%)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Ley 100 de 1993 art. 20 as substituted by Ley 797 de 2003 art. 7 (total 16%: employee 4% + employer 12%). Ceiling verified verbatim in Ley 797 art. 5: 'El limite de la base de cotizacion sera de veinticinco (25) salarios minimos legales mensuales vigentes para trabajadores del sector publico y privado.' NON-TAXABLE INCOME (ET art. 55). NOT PAYABLE by an employed old-age pensioner - neither the 4% employee nor the 12% employer share is due, and the employee is reported with PILA worker sub-type 01, while health, occupational risk and the levies continue. A foreign employee who PROVES affiliation to a pension system abroad may opt out on written election with evidence (Decreto 1072 de 2015 art. 2.2.1.2.1.4; PILA field T2R2-007 'extranjero no obligado a cotizar a pensiones'). Where the employee has two or more employers the contributions are proportional to each remuneration and accumulate against the SHARED 25-SMMLV ceiling, and health must use the same base (Ley 100 art. 18 par. 1). NEWEST-LAW CHECK: Ley 2381 de 2024 replaces the whole pension architecture, but its entry into force was suspended by Constitutional Court Auto 841 de 18 junio 2025 and deferred to 1 APRIL 2027 by Judgment C-264 de 25 agosto 2026 - NO PART OF IT MAY BE CONFIGURED AS LIVE FOR ANY 2026 PERIOD. It leaves the 16% total and the 12/4 split unchanged in any event (expressed as 75% / 25% of the total contribution). |
| Formula (col F) | IBC x 4.00%, rounded UP to the next multiple of 100; 0% for an employed old-age pensioner |
| Nomina Electronica element (col Y) | Deducciones / FondoPension - Porcentaje (NIE164), Deduccion (NIE166); PILA T2R2-046, T2R2-047 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-FSP-SOLIDARIDAD` - Solidarity pension fund - solidarity sub-account 1% - *Fondo de Solidaridad Pensional - Subcuenta de Solidaridad (1%)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Ley 100 de 1993 art. 20 as substituted by Ley 797 de 2003 art. 7. EMPLOYEE-ONLY and ADDITIONAL to the 4% pension - it must NEVER be merged into the pension line. Tested on the MONTHLY IBC, so a variable-pay employee can legitimately cross the trigger in different directions in successive months. NON-TAXABLE INCOME (ET art. 55), confirmed by Formato 2276 numeral N24, which groups the pension and solidarity contributions on one line. Subject to the same 25-SMMLV ceiling. The nomina electronica requires FOUR separate attributes for the fund - solidarity percentage and amount, subsistence percentage and amount. This two-account structure is REPLACED by a single five-band 1.5%-3.0% scale on 1 April 2027 under Ley 2381 de 2024 art. 20 nums. 1-5 - the one employee-facing deduction that reform changes - and is NOT live for any 2026 period. |
| Formula (col F) | IBC x 1.00% where the IBC is >= 4 SMMLV (7,003,620), rounded UP to the next multiple of 100 |
| Nomina Electronica element (col Y) | Deducciones / FondoSP - Porcentaje (NIE167), DeduccionSP (NIE168); PILA T2R2-051 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-FSP-SUBSISTENCIA` - Solidarity pension fund - subsistence sub-account 0.2%-1.0% - *Fondo de Solidaridad Pensional - Subcuenta de Subsistencia (0,2%-1,0%)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Ley 100 de 1993 art. 20 as substituted by Ley 797 de 2003 art. 7. EMPLOYEE-ONLY, additional to both the 4% pension and the 1% solidarity account, so the total employee solidarity surcharge runs from 1.0% at 4 SMMLV to 2.0% above 20 SMMLV (35,018,100), taking the total employee burden from 8.0% to 10.0%. Non-taxable income (ET art. 55). Reported as its own pair of nomina electronica attributes and its own PILA field, separate from the solidarity sub-account. |
| Formula (col F) | IBC x 0.2% / 0.4% / 0.6% / 0.8% / 1.0% for an IBC in the 16-17 / 17-18 / 18-19 / 19-20 / above-20 SMMLV band; trigger 16 SMMLV = 28,014,480; rounded UP to the next multiple of 100 |
| Nomina Electronica element (col Y) | Deducciones / FondoSP - PorcentajeSub (NIE169), DeduccionSub (NIE170); PILA T2R2-052 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-RETENCION-FUENTE` - Income tax withholding on work income (resident) - *Retencion en la Fuente sobre Rentas de Trabajo*

| Attribute | Value |
|---|---|
| Category (col E) | Tax |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | THE ONLY PAYROLL WITHHOLDING IN COLOMBIA - there is no employer payroll tax on income and no local, municipal, departmental, church or solidarity surcharge on employment income. NON-CUMULATIVE: each month stands alone under Procedure 1, and there is NO employer year-end true-up of any kind - the employee reconciles in their own annual return. TWO ORDERING RULES DOMINATE: (1) the 25% exempt income of art. 206 num. 10 is computed LAST, on the figure net of non-taxable income, the art. 387 deductions and other exempt income - computing 25% of GROSS overstates it and under-withholds; (2) the 72-UVT-per-dependant deduction of art. 336 num. 3 sits OUTSIDE the 40% and 1,340-UVT caps. Caps: (D+E) <= 40% of (C = A - B) AND <= 1,340 UVT/year (5,848,430/month as apportioned), with the 25% exemption itself capped at 790 UVT/year (3,447,955/month). CESANTIAS AND THEIR INTEREST NEVER ENTER THE MONTHLY BASE under either procedure. A SUB-30-DAY PERIOD IS A PERCENTAGE RULE, NOT AN AMOUNT RULE: divide the payments by the days, multiply by 30, read the table PERCENTAGE, then apply that percentage to the actual smaller payment (art. 385) - reading the table for an AMOUNT on the grossed-up figure would grossly over-withhold. The employee may request a HIGHER rate in writing, effective from the month AFTER the request (art. 383 par. 3); it overrides upward only, never downward. Where an identifier or an employee declaration is missing there is NO penalty rate - the employee simply loses the deduction and is over-withheld. |
| Formula (col F) | PROCEDURE 1 (ET art. 385): read the art. 383 table on the month's art. 388 depurated base - 0% to 95 UVT (4,975,530), then 19% / 28% / 33% / 35% / 37% / 39% above 95 / 150 / 360 / 640 / 945 / 2,300 UVT. PROCEDURE 2 (art. 386): fixed % = table(sum of the preceding 12 months' taxable payments / 13), recomputed each JUNE and DECEMBER and applied to the month's depurated base |
| Nomina Electronica element (col Y) | Deducciones / RetencionFuente (NIE177); Formulario 350 casillas 77 and 93 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-RETENCION-NO-RESIDENTE` - Income tax withholding - non-resident (flat 20%) - *Retencion en la Fuente a No Residentes (20% - ET art. 408)*

| Attribute | Value |
|---|---|
| Category (col E) | Tax |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | ET art. 408. THE SINGLE LARGEST CONFIGURATION RISK IN COLOMBIAN EXPATRIATE PAYROLL: on COP 8,000,000 the withholding is COP 1,600,000 against COP 92,049 for a resident - a 17-fold difference on the same salary. THE RESIDENCE SWITCH IS PROSPECTIVE, NEVER RETROACTIVE: DIAN Concepto 011108 de 29 junio 2026, upholding Concepto 1789 int. 14595 de 2025, rejected the argument that a foreign employee on a contract exceeding 183 days may be withheld under art. 383 from day one in anticipation of future residence. Withholding is determined AT THE MOMENT OF EACH PAYMENT on the status then held, and the switch to the art. 383 table takes effect FROM THE PAYMENT FOLLOWING the date the 183-day test of art. 10 is met, with NO true-up of the earlier months through payroll. Where the service is performed ENTIRELY OUTSIDE COLOMBIA by a non-resident the income is foreign-source and there is NO WITHHOLDING AT ALL (DIAN Oficio 28380 de 2019). Non-residents are IN SCOPE for Mercans Colombia payroll - a foreign national employed under a Colombian contract before acquiring residence is a common case - so the engine must carry a residence flag with an effective date and support the mid-year switch. Treaty relief is a CLIENT DECISION requiring a residence certificate and is applied only on written client instruction. |
| Formula (col F) | gross payment x 20%, with NO art. 388 depuration, NO art. 387 deductions, NO 25% exempt income and NO tax-free band - 20% from the first peso |
| Nomina Electronica element (col Y) | Deducciones / RetencionFuente (NIE177); Formulario 350 casillas 109-112 and hoja 2 casillas 141-155 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | Yes |
| YTD Remarks (col AB) |  |

### `CO-DED-PENSION-VOLUNTARIA` - Voluntary pension fund contribution (employee) - *Aporte Voluntario a Fondo de Pensiones Voluntarias*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | ET art. 126-1. EXEMPT INCOME, subtracted at step (E) of the depuration INSIDE the 40% and 1,340-UVT caps - so it is LESS valuable than a voluntary contribution to the individual pension account, which is non-taxable income deducted before the cap reference figure is struck. Employer contributions on the employee's behalf count toward the SAME cap and are exempt income in the employee's hands. Requires the employee's written authorisation and a fund certificate. Reported at Formulario 220 casilla 56 / Formato 2276 numeral N26. |
| Formula (col F) | Amount authorised in writing, within the SHARED cap of the lower of 30% of labour income or 3,800 UVT per year = COP 199,021,200 (shared with AFC / AVC) |
| Nomina Electronica element (col Y) | Deducciones / PensionVoluntaria (NIE198) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-AFC-AVC` - AFC / AVC long-term savings contribution (employee) - *Aporte a Cuentas AFC / AVC*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | ET art. 126-4 - construction-savings (AFC) and long-term-savings (AVC) accounts. EXEMPT INCOME inside the 40% and 1,340-UVT caps, sharing ONE combined annual limit with the voluntary pension fund, so the engine must maintain a SINGLE shared accumulator across both vehicles, not two. Evidenced by a financial-institution certificate. Reported at Formulario 220 casillas 57 and 58 / Formato 2276 numerals N27 and N28, which are separate lines for the two account types. |
| Formula (col F) | Amount authorised in writing, within the SAME shared 30% / 3,800-UVT annual cap as the voluntary pension fund |
| Nomina Electronica element (col Y) | Deducciones / AFC (NIE179) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-RAIS-VOLUNTARIO` - Voluntary contribution to the individual pension account (employee) - *Cotizacion Voluntaria al Regimen de Ahorro Individual (RAIS)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | ET art. 55. NON-TAXABLE INCOME, deducted at step (B) BEFORE the 40% cap reference figure is struck, which makes it MATERIALLY MORE VALUABLE than exempt income and the single most efficient voluntary vehicle in the Colombian depuration. Available to employees affiliated to the private individual-account regime. A WITHDRAWAL THAT DOES NOT MEET THE QUALIFYING CONDITIONS IS WITHHELD AT 35%. Evidenced by a pension administrator certificate; reported on the PILA as the AVP change event and at Formulario 220 casilla 55 / Formato 2276 numeral N25. |
| Formula (col F) | Amount authorised in writing, within the lower of 25% of annual labour income or 2,500 UVT per year = COP 130,935,000 |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197); PILA T2R2-028, T2R2-048, T2R2-053 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-SINDICATO` - Union dues - *Cuota Sindical*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | CST art. 150 - one of the deductions requiring NO individual written order from the employee. Post-tax, with no withholding effect. May NOT reduce pay below the SMMLV or into the non-attachable portion (art. 149 num. 2), so it ranks behind mandatory social security, withholding tax and court-ordered garnishments and must be SUSPENDED for the period where the protected floor is reached, with the arrears made visible on the payslip. The nomina electronica carries both a percentage and an amount attribute. |
| Formula (col F) | Percentage or amount fixed by the union's statutes, deducted at the union's request for its members |
| Nomina Electronica element (col Y) | Deducciones / Sindicato - Porcentaje (NIE171), Deduccion (NIE172) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-COOPERATIVA` - Cooperative and employee savings-fund dues - *Aportes a Cooperativas y Fondos de Empleados*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | CST art. 150 - no individual written order required where the cooperative or savings fund is legally authorised. Post-tax, no withholding effect, protected by the SMMLV floor. NOTE THE ASYMMETRY: a cooperative DEBT enforced by court order falls within the CST art. 156 exception and may reach up to 50% OF THE WHOLE SALARY including the minimum-wage portion, whereas an ordinary voluntary cooperative due may not breach the floor at all. |
| Formula (col F) | Amount fixed by the cooperative or fund, where legally authorised |
| Nomina Electronica element (col Y) | Deducciones / Cooperativa (NIE180) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-SANCION-DISCIPLINARIA` - Disciplinary sanction - *Sancion Disciplinaria*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | CST art. 150 permits the deduction with NO individual written order, but ONLY where the sanction is imposed under a DULY APPROVED set of work rules - the engine must therefore carry a flag confirming that an approved reglamento exists, because without one the deduction is unlawful. Post-tax, no withholding effect, protected by the SMMLV floor. The nomina electronica distinguishes a PUBLIC sanction (SancionPublic) from a PRIVATE one (SancionPriv). |
| Formula (col F) | Amount fixed by the duly approved reglamento interno de trabajo |
| Nomina Electronica element (col Y) | Deducciones / Sancion - SancionPublic (NIE173) / SancionPriv (NIE174) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-SABES` - Higher-education solidarity contribution - *Contribucion Solidaria a la Educacion Superior (Contribucion Sabes)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Added to the CST art. 150 list of permitted deductions by LEY 1911 DE 2018 ART. 22, so it requires NO individual written order. IT IS A DEDUCTION, NOT A TAX - it must not be aggregated with the retencion en la fuente on Formulario 350, which is the most common misclassification of this line. Post-tax, no withholding effect, protected by the SMMLV floor. |
| Formula (col F) | Amount fixed under the scheme for a beneficiary of the higher-education credit programme |
| Nomina Electronica element (col Y) | Deducciones / Educacion (NIE183) or OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-LIBRANZA` - Payroll lending repayment - *Libranza (Ley 1527 de 2012)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Ley 1527 de 2012. Requires the employee's written authorisation, after which the employer MUST deduct and remit the instalment to the lender - CST art. 149 num. 3 makes the employer LIABLE IN DAMAGES ('responsable de los perjuicios') for failing to make an authorised, lawful deduction in good time, so an employer that quietly drops a libranza can be sued by the lender. Competing libranzas are applied in DATE ORDER OF THE AUTHORISATIONS. Post-tax, no withholding effect. Two floors bind simultaneously: the art. 149 num. 2 SMMLV / non-attachable floor and the Ley 1527 50%-of-net floor. |
| Formula (col F) | Instalment fixed in the libranza authorisation; the AGGREGATE of libranza deductions must leave the employee at least 50% OF NET SALARY after all statutory deductions |
| Nomina Electronica element (col Y) | Deducciones / Libranza - Descripcion (NIE175), Deduccion (NIE176) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-PRESTAMO` - Employer loan and advance recovery - *Prestamo y Anticipo del Empleador (CST art. 151)*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | CST art. 151 permits written agreements on loans, advances and set-offs. THE EMPLOYER MAY NOT UNILATERALLY RESCHEDULE - art. 151 requires the instalment and the amortisation period to be agreed in writing, and unilateral variation entitles the employee to go to the labour inspector. Where the protected floor is reached the instalment must be SUSPENDED for the period and carried forward, notified on the payslip as an explicit informational line so the arrears are visible; the shortfall may never be recovered by set-off in a later period without a fresh written authorisation, and never at a rate that breaches the floor again. Post-tax, no withholding effect. |
| Formula (col F) | Instalment agreed IN WRITING, stating the instalment amount and the amortisation period |
| Nomina Electronica element (col Y) | Deducciones / Anticipos (NIE196) or Deuda (NIE185) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-EMBARGO` - Judicial or tax attachment - *Embargo Judicial o Fiscal*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | CST art. 154 makes salary UNATTACHABLE as the general rule; art. 155 opens only the excess over the minimum wage, and only to one fifth of that excess. A TAX LEVY BY DIAN counts as a court order for CST art. 149 purposes because the tax authority holds jurisdictional powers under ET arts. 823 et seq. and may issue an attachment order without going to court; UGPP social-security enforcement is treated the same way. Competing ordinary attachments share the art. 155 headroom IN DATE ORDER OF SERVICE on the employer. WHERE COMPETING ORDERS EXCEED THE CEILING the employer applies them in priority to the cap and NOTIFIES the court or authority whose order cannot be satisfied, stating the competing orders and the amounts applied - it must NOT apportion pro rata on its own initiative and must NOT exceed the ceiling to satisfy all orders. Post-tax, no withholding effect. |
| Formula (col F) | Up to 20% (ONE FIFTH) of the EXCESS OVER THE SMMLV - CST art. 155. On COP 3,000,000 the excess is 1,249,095 and the maximum attachable is 249,819 |
| Nomina Electronica element (col Y) | Deducciones / EmbargoFiscal (NIE181) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-ALIMENTOS` - Maintenance / child-support garnishment - *Embargo por Alimentos*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | CST art. 156 is the one broad exception to Colombia's otherwise robust salary protection: for MAINTENANCE obligations and debts owed to COOPERATIVES, up to half the whole salary is attachable, minimum wage included. Maintenance ranks FIRST among garnishments - the obligation is of constitutional rank (Political Constitution art. 44, the prevailing rights of the child) - and it may lawfully take net pay BELOW the minimum wage, which no voluntary deduction ever can. Served by judicial order from a family judge, or a conciliation agreement approved by a family commissioner or the ICBF, on receipt of which the employer becomes a RETAINING AGENT and must acknowledge the order, apply it from the next payroll falling due after service, remit to the specified account, report any termination, unpaid leave or salary change affecting it, and keep the order and remittance evidence for the retention period. THE TWO CEILINGS ARE NOT CUMULATIVE ALLOWANCES: art. 156 (50% of the whole) and art. 155 (20% of the excess) are different ceilings for different claim types - apply the maintenance order first within its own 50% ceiling, then the commercial attachment only to the extent that the art. 155 headroom on the excess over the SMMLV remains unused. |
| Formula (col F) | Up to 50% OF THE WHOLE SALARY, INCLUDING THE MINIMUM-WAGE PORTION - CST art. 156 |
| Nomina Electronica element (col Y) | Deducciones / EmbargoFiscal (NIE181) or PagosTerceros (NIE195) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-MEDICINA-PREPAGADA` - Prepaid health / supplementary plan (employee share) - *Medicina Prepagada y Plan Complementario - Empleado*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | A POST-TAX PAYROLL DEDUCTION requiring the employee's written authorisation for each case (CST art. 149), which SEPARATELY generates a withholding-base deduction under ET art. 387 lits. a) and b) on a provider certificate, provided the provider is supervised by the National Health Superintendence (prepaid medicine) or the Financial Superintendence (health insurance). The two are distinct mechanisms and BOTH must be configured: the cash deduction from net pay, and the reduction of the taxable base. It does not replace the compulsory 12.5% health contribution. |
| Formula (col F) | Premium authorised in writing; separately generates an ET art. 387 DEDUCTION of up to 16 UVT/month = COP 837,984 against the withholding base |
| Nomina Electronica element (col Y) | Deducciones / PlanComplementarios (NIE182) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-DED-OTRAS` - Other authorised deduction - *Otras Deducciones Autorizadas*

| Attribute | Value |
|---|---|
| Category (col E) | Deduction |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Catch-all for employee-authorised voluntary deductions - insurance premiums other than qualifying health cover, employee purchases of the employer's goods and services, funeral funds and welfare funds. CST art. 149 num. 1 is the controlling rule: the employer 'no puede deducir, retener o compensar suma alguna del salario, sin orden suscrita por el trabajador para cada caso, o sin mandamiento judicial'. Post-tax, no withholding effect, protected by the SMMLV floor. |
| Formula (col F) | Amount authorised in writing by the employee for each case (CST art. 149 num. 1) |
| Nomina Electronica element (col Y) | Deducciones / OtrasDeducciones (NIE197) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-ER-SALUD` - Health contribution (employer) 8.5% - *Aporte a Salud - Empleador (8,5%)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Ley 100 de 1993 art. 204 (total 12.5%). EXONERATED where the employee earns STRICTLY LESS THAN 10 SMMLV (17,509,050) and the employer is an income-tax-filing legal person - a natural-person employer qualifies only if it employs two or more workers (ET art. 114-1). THE EXONERATION IS TESTED PER EMPLOYEE, PER MONTH, on what the employee devenga that month, so an overtime or commission month can lose it, and where a mid-month increase takes the MONTH TOTAL across the line the exoneration is lost for the WHOLE month - the test is on the month, not on the segment. AT EXACTLY 10 SMMLV THE EXONERATION IS LOST, costing the employer approximately COP 2,363,800 per month and taking the employer cost factor from about 1.3836 to about 1.52 - the single largest step-change in Colombian employer cost. Reported on the PILA with the exoneration flags A1-033 (employer level) and T2R2-076 (contributor level). |
| Formula (col F) | IBC x 8.50%, rounded UP to the next multiple of 100; ZERO where the ET art. 114-1 exoneration applies |
| Nomina Electronica element (col Y) | PILA T2R2-054, T2R2-055; A1-033; T2R2-076 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-ER-PENSION` - Mandatory pension contribution (employer) 12% - *Aporte a Pension Obligatoria - Empleador (12%)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Ley 100 de 1993 art. 20 as substituted by Ley 797 de 2003 art. 7 (total 16%). NEVER RELIEVED by the ET art. 114-1 exoneration - only employer health 8.5%, SENA 2% and ICBF 3% are exonerable. Not due for an employed old-age pensioner. The employer pays its own share and withholds the employee's share at the moment of payment (Ley 100 art. 22). Ley 2381 de 2024 leaves both the 16% total and the 12/4 split unchanged when it takes effect on 1 April 2027. |
| Formula (col F) | IBC x 12.00%, rounded UP to the next multiple of 100; NEVER exonerated |
| Nomina Electronica element (col Y) | PILA T2R2-046, T2R2-047, T2R2-050 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-ER-ARL` - Occupational risk contribution (employer) - *Aporte a Riesgos Laborales - ARL (0,348%-8,7%)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Decreto 1772 de 1994 art. 13, compiled in Decreto 1072 de 2015 arts. 2.2.4.3.4 and 2.2.4.3.5. EMPLOYER-ONLY - the employee rate is 0.00%. NEVER exonerated. 'Todo empleador que se afilie por primera vez al Sistema General de Riesgos Laborales cotizara por el valor correspondiente al valor inicial de la clase de riesgo que le corresponda', and the initial rates are independently corroborated by the Resolucion 2388 de 2016 rate tables. THE CLASS VARIES BY WORK CENTRE, NOT BY GEOGRAPHY, so one company can legitimately carry two classes and two rates; where a person performs several occupations they contribute at the HIGHEST class (Decreto 1072 art. 2.2.4.2.5.6). A DEFECT IN AN OFFICIAL DOCUMENT, RECORDED FOR TRACEABILITY: Decreto 1072 art. 2.2.4.3.5 prints the CLASS IV MAXIMUM AS 6.060%, while some secondary transcriptions state 6.960% - which is in fact class V's INITIAL rate and no class IV figure at all; the correct class IV maximum is 6.060%, verified against the government compilation of Decreto 1772 de 1994 art. 13. DO NOT CONFUSE TABLES: the 11-column minimum/maximum table at art. 2.2.4.2.5.7 applies ONLY to the voluntary affiliation of independent workers under Decreto 1563 de 2016, never to employees. |
| Formula (col F) | IBC x the work centre's class rate. Class INITIAL rates: I 0.522%, II 1.044%, III 2.436%, IV 4.350%, V 6.960%. Global bounds 0.348% to 8.700%. Rounded UP to the next multiple of 100 |
| Nomina Electronica element (col Y) | PILA T2R2-061, T2R2-062, T2R2-063, T2R2-077, T2R2-078 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-ER-CCF` - Family compensation fund levy 4% - *Aporte a Caja de Compensacion Familiar - CCF (4%)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Ley 21 de 1982 arts. 9 and 12. NEVER EXONERATED - the ET art. 114-1 relief reaches employer health, SENA and ICBF only, so the CCF 4% is payable on every employee at every salary level. TWO DIFFERENCES FROM THE IBC THAT THE ENGINE MUST MODEL SEPARATELY: the levy base has NO 25-SMMLV ceiling, and it EXPRESSLY INCLUDES statutory and contractual PAID REST DAYS. The fund is organised by department so the receiving institution code differs, but the 4% rate does not. The subsidio familiar the fund then pays to the employee is a fund benefit, not an employer payment, and is out of scope. Ley 1429 de 2010 provides a graduated scale for qualifying micro and small enterprises with a special regime for AMAZONAS, GUAINIA AND VAUPES, visible in the Resolucion 2388 rate tables as contributor classes C and D - not applicable to standard corporate payroll. |
| Formula (col F) | PAYROLL-LEVY BASE x 4.00% (Ley 21 de 1982 art. 17 nomina mensual de salarios, INCLUDING paid rest days), NO CEILING AT ALL; rounded UP to the next multiple of 100 |
| Nomina Electronica element (col Y) | PILA T2R2-045 (IBC CCF), T2R2-064, T2R2-065; T2R2-035 (CCF code); T2R2-039 (CCF days) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-ER-SENA` - Apprenticeship training levy 2% - *Aporte al SENA (2%)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Ley 21 de 1982 art. 9. EXONERATED where the employee earns strictly less than 10 SMMLV (17,509,050) and the employer is an income-tax-filing legal person (ET art. 114-1), tested per employee per month. Computed on the Ley 21/1982 art. 17 base - the same base as the CCF and the ICBF, which includes paid rest days and has NO ceiling - and NOT on the IBC. The PILA carries a separate 'IBC otros parafiscales diferentes a CCF' field (T2R2-095) precisely because the two levy bases can diverge where one levy is exonerated and the CCF is not. |
| Formula (col F) | PAYROLL-LEVY BASE x 2.00%, NO CEILING; ZERO where the ET art. 114-1 exoneration applies; rounded UP to the next multiple of 100 |
| Nomina Electronica element (col Y) | PILA T2R2-095, T2R2-066, T2R2-067 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-ER-ICBF` - Family welfare levy 3% - *Aporte al ICBF (3%)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Ley 89 de 1988 art. 1, which raised the levy from 2% to 3%. EXONERATED on the same ET art. 114-1 terms as employer health and SENA. Same Ley 21/1982 art. 17 base as the CCF and SENA - paid rest days included, no ceiling. Together the three levies are 9% of the levy base, of which 5% is exonerable and the CCF's 4% never is. During unpaid leave (SLN) the payroll levies fall to 0%. |
| Formula (col F) | PAYROLL-LEVY BASE x 3.00%, NO CEILING; ZERO where the ET art. 114-1 exoneration applies; rounded UP to the next multiple of 100 |
| Nomina Electronica element (col Y) | PILA T2R2-095, T2R2-068, T2R2-069 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-ER-PENSION-ALTO-RIESGO` - Additional employer pension contribution - high-risk activity - *Aporte Patronal Adicional de Pension de Alto Riesgo*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Decreto-Ley 2090 de 2003 establishes the high-risk activities that carry an additional employer pension contribution and a reduced retirement age, and the nomina electronica carries a REQUIRED AltoRiesgoPension flag (NIE043) with the PILA carrying a special-pension-rate indicator (T2R2-079). OPEN ITEM: the 2026 confirmation of the additional rate and its precise base was not obtained from a primary regulatory source this pass - the 26% total is read from the Resolucion 2388 rate table, not from the implementing decree. CONFIGURE ONLY AGAINST THE CURRENT IMPLEMENTING DECREE and confirm with the Regulation Analyst before go-live; carried in the QA report. |
| Formula (col F) | IBC x an additional employer-borne rate above the standard 12%: the Resolucion 2388 de 2016 rate table shows a TOTAL pension rate of 26% for a high-risk contributor against the standard 16%, implying +10 percentage points employer-borne |
| Nomina Electronica element (col Y) | PILA T2R2-079; Trabajador / AltoRiesgoPension (NIE043) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-PROV-PRIMA` - Service bonus accrual (employer) - *Provision de Prima de Servicios (8,3333%)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Statutory-benefit accrual, computed IN PARALLEL with the employee gross-to-net and never touching net pay. THE TRANSPORT ALLOWANCE IS IN THIS BASE even though it is out of the IBC and out of the payroll-levy base. Paid in two instalments - half by 30 June and half by 20 December. Absorbed by an all-inclusive salary. Together with cesantias 8.3333%, interest 1.0000% and vacation 4.1667% the total statutory benefit accrual is 21.8333% of pay. |
| Formula (col F) | 8.3333% (30 / 360) of (monthly salary + auxilio de transporte) |
| Nomina Electronica element (col Y) | Not a PILA or nomina electronica field - an accounting provision |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-PROV-CESANTIAS` - Severance-savings accrual (employer) - *Provision de Cesantias (8,3333%)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Statutory-benefit accrual. The transport allowance is IN this base. Liquidated at 31 December and deposited to the employee's chosen fund BY 14 FEBRUARY; late deposit costs one day's salary per day of delay (Ley 50 de 1990 art. 99 num. 3). Ley 2466 de 2025 art. 64 permits an 8.33% MONTHLY ADVANCE DEPOSIT to the fund by written agreement, which is expressly NOT a partial payment of the cesantias. Absorbed by an all-inclusive salary. |
| Formula (col F) | 8.3333% (30 / 360) of (monthly salary + auxilio de transporte) |
| Nomina Electronica element (col Y) | Consignacion Cesantias planilla T14; MA02 / MA03 for the monthly advance |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-PROV-INTERESES-CESANTIAS` - Severance-interest accrual (employer) - *Provision de Intereses a las Cesantias (1,0000%)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Statutory-benefit accrual for the 12% annual interest of Ley 52 de 1975 art. 1. PAID TO THE EMPLOYEE DURING JANUARY - not to the fund, unlike the principal. Optionally monthly at 1% by written agreement (Ley 2466 de 2025 art. 64). Absorbed by an all-inclusive salary. |
| Formula (col F) | 1.0000% per month (12% per year) of the cesantias base |
| Nomina Electronica element (col Y) | Interes de cesantias IN01 / IN02 / IN03 (not a file field) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-PROV-VACACIONES` - Vacation accrual (employer) - *Provision de Vacaciones (4,1667%)*

| Attribute | Value |
|---|---|
| Category (col E) | Employer Contribution |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | Statutory accrual for the 15 working days of annual leave. THE TRANSPORT ALLOWANCE IS EXCLUDED from this base, unlike the prima and cesantias bases - the single most common accrual error in Colombian payroll. NOT ABSORBED BY AN ALL-INCLUSIVE SALARY (CST art. 132 num. 2 expressly excepts vacation), and owed on the FULL 100% of an all-inclusive salary while contributions run on 70%. Accrual suspended during unpaid leave. |
| Formula (col F) | 4.1667% (15 working days / 360) of salary EXCLUDING the auxilio de transporte, overtime and rest-day work; accrual = salary x days / 720 |
| Nomina Electronica element (col Y) | Not a PILA or nomina electronica field - an accounting provision |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-BASE-IBC` - Social-security contribution base - *Ingreso Base de Cotizacion (IBC)*

| Attribute | Value |
|---|---|
| Category (col E) | Base |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | BASE 1 OF THREE, AND THE ORDER OF THE FOUR ADJUSTMENTS MATTERS: applying the ceiling before the 40% clamp gives a different and wrong answer. Ley 100 de 1993 art. 18 as substituted by Ley 797 de 2003 art. 5. The SAME base serves health (art. 204 par. 1), pension, the solidarity fund and occupational risk (Decreto 1072 de 2015 art. 2.2.4.3.3). ACTUAL salary, not notional - Colombia has no banded, class or scheduled contribution wage, so a variable-pay employee has a different IBC every month and can legitimately cross the 4-SMMLV solidarity trigger, the 10-SMMLV exoneration line and the 25-SMMLV ceiling in different directions in successive months. Where actual pay falls below the floor the base is RAISED to one SMMLV pro-rated to contributory days, so the employee still contributes 4% + 4% of the raised base even though the salary was lower. Note the asymmetry the engine must implement: the SMMLV floor protects NET PAY against voluntary deductions, while the IBC is SEPARATELY floored at one SMMLV - two different floors doing two different jobs. |
| Formula (col F) | SUM salary-constituting payments (transport / connectivity allowance, prima, cesantias and interest EXCLUDED; vacation INCLUDED) -> apply the 40% clamp -> all-inclusive salary = 70% -> FLOOR 1 SMMLV (1,750,905) pro-rated to contributory days -> CEILING 25 SMMLV (43,772,625) -> round UP to the whole peso |
| Nomina Electronica element (col Y) | PILA T2R2-042 (IBC pension), T2R2-043 (IBC salud), T2R2-044 (IBC riesgos laborales) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-BASE-PARAFISCAL` - Payroll-levy base - *Base de Aportes Parafiscales (Nomina Mensual de Salarios)*

| Attribute | Value |
|---|---|
| Category (col E) | Base |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | BASE 2 OF THREE - AND IT IS NOT THE IBC. Ley 21 de 1982 art. 17, verified verbatim against the gazette: the nomina mensual de salarios means 'la totalidad de los pagos hechos por concepto de los diferentes elementos integrantes del salario en los terminos de la ley laboral, cualquiera que sea su denominacion y ademas, los verificados por descansos remunerados de ley y convencionales o contractuales. Los pagos hechos en moneda extranjera deberan incluirse en la respectiva nomina, liquidados al tipo de cambio oficial y vigente el ultimo dia del mes al cual corresponde el pago.' TWO DIFFERENCES FROM THE IBC: it has NO CEILING at all - nothing is capped at 25 SMMLV - and paid rest days are included BY NAME. The Ley 1393/2010 art. 30 40% clamp does NOT reach this base, because art. 30 bites only 'para los efectos relacionados con los articulos 18 y 204 de la Ley 100 de 1993'. Serves the CCF 4%, SENA 2% and ICBF 3%; falls to zero for the days of an SLN unpaid-leave event. |
| Formula (col F) | SUM all salary elements PLUS statutory and contractual PAID REST DAYS; all-inclusive salary = 70%; NO FLOOR AND NO CEILING; round UP to the whole peso |
| Nomina Electronica element (col Y) | PILA T2R2-045 (IBC CCF), T2R2-095 (IBC otros parafiscales), T2R1-020 (valor total de la nomina) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-BASE-RETENCION` - Withholding tax base - *Base Gravable de Retencion (ET art. 388)*

| Attribute | Value |
|---|---|
| Category (col E) | Base |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | BASE 3 OF THREE - neither gross pay nor the IBC. ET art. 388 added by Ley 1819 de 2016 art. 18, with the absolute annual cap added by Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 as modified by Decreto 2231 de 2023 art. 9. Cesantias and their interest NEVER enter it. OPEN ITEM: the 790-UVT and 1,340-UVT caps are stated ANNUALLY yet withholding is monthly; market practice, which Mercans follows, apportions them at one twelfth - 65.8333 UVT = 3,447,955 and 111.6667 UVT = 5,848,430 - and tests each month against the apportioned figure. No regulation prescribes the apportionment expressly; carried in the QA report. The CURRENT year's UVT applies to the annual caps (DIAN Concepto 015007 int. 973 de 13 septiembre 2023). NOT DEDUCTIBLE AGAINST WITHHOLDING: the 1% / 240-UVT invoice-based deduction of ET art. 336 num. 5, expressly excluded and confirmed by the same Concepto - it is available only in the employee's own annual return. ALSO OUTSIDE THE CAPS BUT OUTSIDE MERCANS SCOPE: ET art. 206 par. 4 places nums. 6 to 9, the prima especial and the prima de costo de vida outside the 40% and 1,340-UVT limits; these attach to military, judicial, diplomatic and public university staff, but the engine must carry the flag so it does not silently clamp them if such an employee is loaded. |
| Formula (col F) | (A) taxable payments - (B) non-taxable income - (D) art. 387 deductions - (E) exempt income, where (D+E) <= 40% of (C = A - B) AND <= 1,340 UVT/year, with the 25% exemption computed LAST and capped at 790 UVT/year, LESS the 72-UVT-per-dependant deduction which sits OUTSIDE the caps |
| Nomina Electronica element (col Y) | Formulario 350 casilla 77; Deducciones / RetencionFuente (NIE177) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-BASE-PRESTACIONAL` - Statutory-benefit base - *Base Prestacional (Prima, Cesantias e Intereses)*

| Attribute | Value |
|---|---|
| Category (col E) | Base |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | The base of the prima de servicios, the cesantias and the 12% interest. ITS DEFINING ODDITY: it INCLUDES the auxilio de transporte, which is excluded from BOTH the IBC and the payroll-levy base, and it EXCLUDES the prima, cesantias and interest themselves. A valid written CST art. 128 non-salary pact removes a payment from this base PERMANENTLY - unlike the IBC, where the 40% clamp can force the excess back in. Overtime and rest-day work ARE in this base, unlike the vacation base. |
| Formula (col F) | monthly salary PLUS the auxilio de transporte or auxilio de conectividad; variable pay at the semester or annual average as the particular benefit requires |
| Nomina Electronica element (col Y) | Derived - feeds Devengados / Primas (NIE117-NIE119) and Cesantias (NIE120-NIE122) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-BASE-VACACIONES` - Vacation base - *Base de Vacaciones (CST art. 192)*

| Attribute | Value |
|---|---|
| Category (col E) | Base |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | CST art. 192, verified verbatim: 'Durante el periodo de vacaciones el trabajador recibira el salario ordinario que este devengando el dia en que comience a disfrutar de ellas. En consecuencia, SOLO se excluiran para la liquidacion de vacaciones el valor del trabajo en dias de descanso obligatorio y el valor del trabajo suplementario en horas extras.' The word 'solo' is doing the work: THE NIGHT PREMIUM AND COMMISSIONS STAY IN, and only those two things come out. The auxilio de transporte is not in this base either. An all-inclusive salary does NOT absorb vacation, so the base is the FULL 100% of it while contributions run on 70%. |
| Formula (col F) | ordinary salary being earned on the day leave begins, EXCLUDING ONLY the value of work on obligatory rest days and the value of supplementary overtime hours; variable salary -> average of the immediately preceding year |
| Nomina Electronica element (col Y) | Derived - feeds Devengados / VacacionesComunes (NIE112) and VacacionesCompensadas (NIE116) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-INT-CLAMP40` - Non-salary excess forced back into the contribution base - *Excedente No Salarial Reintegrado al IBC (Ley 1393 de 2010 art. 30)*

| Attribute | Value |
|---|---|
| Category (col E) | Intermediary |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | THE INTERMEDIARY THAT MAKES TWO BASES DIVERGE PERMANENTLY. Ley 1393 de 2010 art. 30, verified verbatim against the gazette: 'Sin perjuicio de lo previsto para otros fines, para los efectos relacionados con los articulos 18 y 204 de la Ley 100 de 1993, los pagos laborales no constitutivos de salario de los trabajadores particulares no podran ser superiores al 40% del total de la remuneracion.' WORKED ILLUSTRATION (CCG Module 6.3): salary 8,000,000 plus a 20,000,000 retention bonus under a valid non-salary pact gives total remuneration 28,000,000, of which non-salary is 71.4%; permitted non-salary is 40% x 28,000,000 = 11,200,000, so 8,800,000 is FORCED BACK IN and the IBC becomes 8,000,000 + 8,800,000 = 16,800,000 - while the whole 20,000,000 remains non-salary for the prima, cesantias, interest and vacation, and fully taxable for withholding. The clamp reaches Ley 100 arts. 18 and 204 only, so it does not touch the CCF / SENA / ICBF levy base. See also Resolucion MinProteccion 2641 de 2011. UGPP audit exposure sits squarely on this line: it cross-matches tax-authority data against filed contribution returns. |
| Formula (col F) | IF total non-salary payments > 40% x total remuneration THEN excess = non-salary total - (0.40 x total remuneration), added to the IBC; ELSE 0. Computed BEFORE the 70% all-inclusive reduction, the floor and the ceiling |
| Nomina Electronica element (col Y) | Derived - feeds PILA T2R2-042, T2R2-043, T2R2-044 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-RATE-HORA-ORDINARIA` - Ordinary hour value - *Valor de la Hora Ordinaria*

| Attribute | Value |
|---|---|
| Category (col E) | Percentage |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | THE SINGLE BIGGEST 2026 CALCULATION CHANGE. Circular 101 publishes the gradual path: 47h/235 from 15 July 2023, 46h/230 from 15 July 2024, 44h/220 from 15 July 2025 and 42h/210 FROM 15 JULY 2026 (Ley 2101 de 2021 art. 3; CST art. 161 as substituted by Ley 2466 de 2025 art. 11, verified verbatim: 'una jornada maxima de cuarenta y dos (42) horas a la semana', distributable by agreement over five or six days, always preserving the rest day and WITHOUT REDUCING SALARY). THE LEGACY DIVISOR OF 240 IS OBSOLETE AND UNDERSTATES EVERY PREMIUM BY ABOUT 14.3%. A JULY 2026 PAYROLL SPANS BOTH DIVISORS and must be split at 15 July - and separately at 1 July for the rest-day premium step from 80% to 90%. Two cut-overs, two weeks apart; never collapse them. Where the week is distributed over five days with Saturday and/or Sunday rest, the ordinary daily shift may be extended by up to two hours WITHOUT paying supplementary work (CST art. 164; Circular 101 SS2.1). |
| Formula (col F) | monthly salary / D, where D = 220 to 14 July 2026 and 210 from 15 July 2026 (MinTrabajo Circular Externa 101 de 22 septiembre 2025). Minimum hourly value: 7,958.66 then 8,337.64 |
| Nomina Electronica element (col Y) | Derived - feeds every hour-type Porcentaje / Pago element |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-PCT-RETENCION-PROC2` - Procedure 2 fixed withholding percentage - *Porcentaje Fijo de Retencion (Procedimiento 2)*

| Attribute | Value |
|---|---|
| Category (col E) | Percentage |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | ET art. 386. THE DIVISOR IS 13, NOT 12 - art. 386 says 'dividir por 13' - because the 13 prorates the 13th-month effect of the prima de servicios, which under Procedure 2 sits INSIDE the ordinary base rather than receiving the separate art. 385 table read; using 12 over-withholds by roughly 8%. A BACKWARD-LOOKING ACCUMULATOR, NOT A PROJECTION: Colombia is not an annualised or cumulative withholding system, so there is no annual estimate, no notional annual salary, no projected bonus and no year-end catch-up. CESANTIAS AND THEIR INTEREST ARE EXPRESSLY EXCLUDED from the accumulator; everything else is included - salary, overtime, the night and rest-day premia, commissions, habitual bonuses, the prima de servicios, salary in kind, the transport allowance, vacation pay and cash-compensated vacation. Art. 387 par. 1 requires the art. 387 deductions to be used BOTH in computing the fixed percentage AND in computing the monthly base it is applied to. A new hire has no 12-month history so no fixed percentage exists: read the table on the month's own taxable payments until the first semi-annual calculation, whose divisor is then the ACTUAL months of service, not 13. A large mid-year increase produces under-withholding for the rest of the semester and THE EMPLOYER MAY NOT UNILATERALLY RAISE THE FIXED PERCENTAGE MID-SEMESTER - the employee's only remedy is a written request for a higher rate under art. 383 par. 3. |
| Formula (col F) | fixed % = table(sum of the preceding 12 months' taxable payments / 13) expressed as a percentage of that average; recomputed each JUNE and DECEMBER and applied to each of the FOLLOWING SIX MONTHS' depurated bases |
| Nomina Electronica element (col Y) | Derived - feeds Deducciones / RetencionFuente (NIE177) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-REDONDEO` - Rounding residual (electronic payroll) - *Redondeo*

| Attribute | Value |
|---|---|
| Category (col E) | Notional |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | THREE ROUNDING REGIMES COEXIST IN ONE COLOMBIAN PAYROLL MONTH AND MUST NEVER BE UNIFIED: the PILA rounds UP - the IBC to the whole peso and each contribution to the next multiple of 100 (Decreto 1990 de 2016 art. 1, substituting Decreto 780 de 2016 art. 3.2.1.5); the nomina electronica uses ROUND-HALF-TO-EVEN with a +/-2.00 tolerance and carries this EXPLICIT Redondeo element for the residual; and the DIAN return forms round to the NEAREST 1,000 (ET art. 577). Net pay itself is not separately rounded to any statutory rule - it is the arithmetic residue after each deduction has already been rounded under its own regime. |
| Formula (col F) | residual difference such that total accrued - total deducted +/- redondeo = total payable, within a tolerance of +/-2.00, using ROUND-HALF-TO-EVEN |
| Nomina Electronica element (col Y) | NominaIndividual / Redondeo (NIE186), DevengadosTotal (NIE187), DeduccionesTotal (NIE188), ComprobanteTotal (NIE189) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-FLAG-SALARIO-INTEGRAL` - All-inclusive salary flag - *Indicador de Salario Integral*

| Attribute | Value |
|---|---|
| Category (col E) | Flag |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | A REQUIRED field of the nomina electronica (NIE056) and of the PILA (T2R2-041). Requires an ORDINARY salary above 10 SMMLV plus a benefit factor of at least 30%, agreed IN WRITING (CST art. 132 num. 2). Drives the 70% reduction of BOTH the IBC (Ley 100 art. 18 final paragraph) and the payroll-levy base (CST art. 132 num. 3: 'los aportes se disminuiran en un treinta por ciento (30%)') - but NEVER of vacation, which stays at 100% because art. 132 num. 2 expressly excepts it. |
| Formula (col F) | TRUE where a WRITTEN all-inclusive salary agreement exists and the salary is >= 13 SMMLV (22,761,765); drives IBC = 70% and payroll-levy base = 70%, but vacation at 100% |
| Nomina Electronica element (col Y) | Trabajador / SalarioIntegral (NIE056); Sueldo (NIE062); PILA T2R2-041 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-FLAG-EXONERACION-114-1` - ET art. 114-1 exoneration flag - *Indicador de Exoneracion de Aportes (ET art. 114-1)*

| Attribute | Value |
|---|---|
| Category (col E) | Flag |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | TESTED PER EMPLOYEE, PER MONTH, on what the employee devenga - not on the contractual salary, and not on a segment of the month, so a mid-month increase that takes the MONTH TOTAL across the line loses the exoneration for the WHOLE month. AT EXACTLY 10 SMMLV THE EXONERATION IS LOST - the statute says 'menos de diez (10) salarios minimos', so the test is strictly less than - costing approximately COP 2,363,800 per month and taking the employer cost factor from about 1.3836 to about 1.52. PENSION 12%, OCCUPATIONAL RISK AND THE CCF 4% ARE NEVER EXONERATED. Carried on the PILA at both employer level (A1-033) and contributor level (T2R2-076), and on Formulario 350 casilla 27 for the related self-withholding configuration. |
| Formula (col F) | TRUE where the employer is an income-tax-filing legal person (or a natural person employing 2 or more workers) AND the employee's month earnings are STRICTLY LESS THAN 10 SMMLV (17,509,050); suppresses employer health 8.5%, SENA 2% and ICBF 3% |
| Nomina Electronica element (col Y) | PILA A1-033, T2R2-076; Formulario 350 casilla 27 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-FLAG-RESIDENCIA-FISCAL` - Tax residence flag with effective date - *Indicador de Residencia Fiscal con Fecha de Efecto*

| Attribute | Value |
|---|---|
| Category (col E) | Flag |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | THE MOST CONSEQUENTIAL FLAG IN COLOMBIAN PAYROLL - a 17-fold withholding difference on the same salary. Must be RE-EVALUATED EVERY PAYROLL PERIOD and switched PROSPECTIVELY from the payment FOLLOWING the date the test is met; never applied retroactively through payroll (DIAN Concepto 011108 de 29 junio 2026). Where the 183-day period straddles two years, residence attaches to the year in which the 183rd day falls. A SECOND CONDITION SITS BESIDE IT: where the service is performed entirely outside Colombia by a non-resident the income is foreign-source and there is no withholding at all (DIAN Oficio 28380 de 2019), so the engine also needs a place-of-service flag - the nomina electronica carries LugarTrabajoPais (NIE050) for exactly this. |
| Formula (col F) | TRUE where the employee is a Colombian tax resident AT THE DATE OF THIS PAYMENT (ET art. 10: more than 183 calendar days, continuous or not, in any 365-day period, or the diplomatic or nationality-plus-connection tests); drives the art. 383 table versus the art. 408 flat 20% |
| Nomina Electronica element (col Y) | Trabajador / LugarTrabajoPais (NIE050); Formulario 350 hoja 2 casillas 141, 144 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-FLAG-ALTO-RIESGO-PENSION` - High-risk pension activity flag - *Indicador de Actividad de Alto Riesgo Pensional*

| Attribute | Value |
|---|---|
| Category (col E) | Flag |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | A REQUIRED field of the nomina electronica (NIE043) with a matching PILA special-pension-rate indicator (T2R2-079). The FLAG itself is mandatory and must be populated for EVERY employee, high-risk or not, or the XML fails validation. OPEN ITEM as to the 2026 additional RATE - see CO-ER-PENSION-ALTO-RIESGO and the QA report. |
| Formula (col F) | TRUE where the employee performs an activity listed in Decreto-Ley 2090 de 2003; drives the additional employer pension contribution and a reduced retirement age |
| Nomina Electronica element (col Y) | Trabajador / AltoRiesgoPension (NIE043); PILA T2R2-079 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-FLAG-PACTO-NO-SALARIAL` - Written non-salary pact flag - *Indicador de Pacto de Exclusion Salarial (CST art. 128)*

| Attribute | Value |
|---|---|
| Category (col E) | Flag |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | THREE TESTS FOR A VALID PACT: it must be (a) EXPRESS, (b) WRITTEN, and (c) attached to a BENEFIT OR ALLOWANCE, not to consideration for the service itself. A 'non-salary' label on what is plainly remuneration for work will not survive a UGPP contribution audit. THE FLAG IS A HARD CONFIGURATION VALUE, NOT A RUNTIME DERIVATION: the nomina electronica separates salary from non-salary AT ELEMENT LEVEL with paired S / NS element names - bonus, allowance, generic concept, generic payment, voucher payment, meal payment and travel/accommodation allowance - so the engine must carry the flag on every wage type and must not attempt to derive it at reporting time. NOTE THE TWO ASYMMETRIES: the pact removes the payment from the labour-law bases PERMANENTLY but from the IBC only up to 40%, and IT HAS NO TAX EFFECT AT ALL. Colombian benefit structuring is a social-security optimisation, never a tax optimisation; any engine that treats a non-salary flag as a tax exclusion will systematically under-withhold. THERE IS NO SALARY-SACRIFICE REGIME IN COLOMBIAN LAW - CST art. 13 makes the minimum labour rights irrenounceable. |
| Formula (col F) | TRUE where an EXPRESS, WRITTEN, SIGNED CST art. 128 pact exists over a genuine benefit or allowance; drives the salary / non-salary element split and the 40% clamp computation |
| Nomina Electronica element (col Y) | Drives every paired S / NS element (NIE139/140, NIE141/142, NIE147/148, NIE151/152, NIE153/154, NIE072/073) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-FLAG-PENSIONADO-ACTIVO` - Employed old-age pensioner flag - *Indicador de Pensionado en Activo*

| Attribute | Value |
|---|---|
| Category (col E) | Flag |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | PENSION CONTRIBUTION CEASES ENTIRELY for an employed old-age pensioner - neither share is due - while health, occupational risk and the payroll levies continue. Reported with PILA worker sub-type 01. REACHING RETIREMENT AGE DOES NOT BY ITSELF STOP THE CONTRIBUTION: being a PENSIONER IN ACTIVE SERVICE does. Retirement age (57 for women, 62 for men in the public defined-benefit regime) affects entitlement and the point at which the contribution ceases, never the rate - there is NO gender-differentiated rate, base, floor, ceiling or trigger anywhere in the eight Colombian contributions, and CST art. 143 as amended by Ley 1496 de 2011 expressly forbids salary differences by gender. |
| Formula (col F) | TRUE where the employee is an old-age pensioner in active service; suppresses BOTH the 4% employee and the 12% employer pension contribution |
| Nomina Electronica element (col Y) | Trabajador / SubTipoTrabajador (NIE042); PILA T2R2-005, T2R2-006 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-FLAG-PROCEDIMIENTO-RETENCION` - Withholding procedure election flag - *Indicador de Procedimiento de Retencion (1 o 2)*

| Attribute | Value |
|---|---|
| Category (col E) | Flag |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | ELECTED BY THE EMPLOYER, PER EMPLOYEE. Once Procedure 2 is elected it applies for the whole six-month period following the June or December calculation, and market practice is to change procedure only at a semester boundary. THE ELECTION MATERIALLY CHANGES JUNE AND DECEMBER NET PAY: under Procedure 1 the statutory minimum prima gets its own table read and is frequently withheld at 0%, while under Procedure 2 it is folded into a single larger base, usually producing higher withholding in that month offset by lower withholding in others. Worked comparison in CCG Module 4.5: on a COP 8,000,000 salary with a COP 4,000,000 first-half prima, Procedure 1 yields COP 92,049.30 for June (the prima read alone falling in the 0% band) against a materially higher single-base result under Procedure 2. |
| Formula (col F) | 1 = ET art. 385 monthly table read, with the statutory minimum prima withheld SEPARATELY; 2 = ET art. 386 fixed percentage set each June and December, binding for the following six months |
| Nomina Electronica element (col Y) | Not reported - a configuration flag driving Deducciones / RetencionFuente (NIE177) |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

### `CO-FLAG-DEPENDIENTES` - Dependants declaration flag and count - *Indicador y Numero de Dependientes Economicos*

| Attribute | Value |
|---|---|
| Category (col E) | Flag |
| Tax Code (col G) | CO-NA |
| Wage Type Explanation (col D) | TWO DEDUCTIONS, AND AN EMPLOYEE MAY TAKE BOTH FOR THE SAME DEPENDANT. Decreto 2231 de 2023 art. 3: 'el mismo dependiente solo dara lugar a una de estas dos deducciones, EXCEPTO cuando el contribuyente tenga ingresos por rentas de trabajo provenientes de una relacion laboral o legal y reglamentaria, en cuyo caso podran aplicarse ambas deducciones por el mismo dependiente.' The art. 387 deduction is 10% OF GROSS REGARDLESS OF THE NUMBER OF DEPENDANTS - it does not multiply; the art. 336 deduction is per dependant AND SITS OUTSIDE THE 40% AND 1,340-UVT CAPS ('en adicion al limite establecido en el inciso anterior'). WHO QUALIFIES (ET art. 387 par. 2, nums. 2 and 3 as amended by Ley 2411 de 2024 art. 2): children up to 18; children 18-25 whose higher or technical education the taxpayer finances; children over 18 in a certified state of physical or psychological dependence; a spouse or permanent partner dependent by absence of income or with annual income below 260 UVT (COP 13,617,240) certified by a public accountant, or by certified dependence; and parents and siblings on the same conditions. THE DEPENDANT'S IDENTITY DOCUMENT IS REQUIRED, not merely a count - the information return demands the document (numeral N34) and the deduction is not sustainable on audit without it. |
| Formula (col F) | Count of qualifying dependants with each dependant's identity document; drives BOTH the ET art. 387 deduction of 10% of gross capped at 32 UVT/month (COP 1,675,968) AND the art. 336 num. 3 deduction of 72 UVT per dependant per year (COP 3,770,928 each, maximum 4 dependants = 6 UVT = COP 314,244 per dependant per month) |
| Nomina Electronica element (col Y) | Formulario 220 casillas 79-82; Formato 2276 numeral N34 |
| Tax Code Source - C9 (col Z) | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |
| YTD Load (col AA) | No |
| YTD Remarks (col AB) |  |

---

## Sheet 3 - Employer Sick Pay and the incapacity cascade (2026)

```
COLOMBIA - EMPLOYER SICK PAY AND THE INCAPACITY CASCADE (2026)

Colombia has NO employer sick-pay scheme of the Czech kind. Cash sickness benefit is a social-security
benefit, and the employer bears only the FIRST TWO DAYS of a general-illness incapacity.

WHO PAYS WHAT
  General illness, days 1-2 .......... EMPLOYER          66.67% (Mercans default, configurable)
  General illness, days 3-90 ......... EPS (health insurer)   66.67% of the contribution base
  General illness, days 91-180 ....... EPS                    50.00% of the contribution base
  Occupational accident or disease ... ARL (risk insurer)    100.00% of the contribution base,
                                                            from the DAY AFTER the event
  Maternity leave, 18 weeks .......... EPS   salary earned when the leave begins
  Paternity leave, 2 weeks ........... EPS   full salary (expands 1 week per point of structural
                                             unemployment reduction, capped at 5 weeks)

FORMULAE
  Employer days 1-2 ............. S / 30 x 0.6667 x d, floored at the minimum-wage equivalent
  EPS days 3-90 ................. IBC / 30 x 0.6667 x d, floored at the minimum-wage equivalent
  EPS days 91-180 ............... IBC / 30 x 0.5000 x d, floored at the minimum-wage equivalent
  ARL, occupational ............. IBC / 30 x 1.0000 x d
  Maternity ..................... S / 30 x 126 calendar days
  Paternity ..................... S / 30 x 14 calendar days
  Variable salary ............... average of the year of service preceding the incapacity, or of the
                                  whole period if under a year (CST art. 228)

OPEN ITEM 1 - THE RATE FOR THE EMPLOYER'S FIRST TWO DAYS.
  Decreto 2943 de 2013 art. 1, compiled at Decreto 780 de 2016 art. 3.2.1.10, allocates 'las
  prestaciones economicas correspondientes a los dos (2) primeros dias de incapacidad originada por
  enfermedad general' to the EMPLOYER but does NOT state the rate. CST art. 227 sets the auxilio at two
  thirds for the first 90 days, and market practice applies 66.67% for days 1-2 on that basis; a
  minority practice pays 100%. MERCANS DEFAULT: 66.67%, configurable. Carried in the QA report.

OPEN ITEM 2 - THE MINIMUM-WAGE FLOOR ON INCAPACITY PAYMENTS.
  Where 66.67% of salary falls below one SMMLV (1,750,905), market practice and settled
  administrative doctrine top the payment up to one minimum wage. The primary regulatory source for
  that floor was not retrieved this pass. MERCANS DEFAULT: apply the floor, configurable. Carried in
  the QA report.

PAYROLL TREATMENT (the counter-intuitive part)
  Employer days 1-2 ....... NOT salary, but IN the IBC, IN the Ley 21/1982 payroll-levy base and IN
                            the statutory-benefit base; TAXABLE.
  EPS / ARL benefits ...... NOT employer salary, so OUT of the payroll-levy base - but CONTRIBUTIONS
                            CONTINUE ON THE BASE (PILA change events IGE, IRL, LMA). Exempt within
                            the statutory minimum (ET art. 206 nums. 1-2 and par. 1, which limits the
                            exemption to 'las cantidades que correspondan al minimo legal' and taxes
                            the excess). Advanced by the employer through payroll and recovered from
                            the insurer; the PILA carries the authorisation number and value
                            (T2R2-057 to T2R2-060) so the recovery can be offset.
  Auxilio de transporte ... NOT PAYABLE for sick days - no travel occurs.
  Overtime and premia ..... Not applicable during incapacity.
  Benefit accrual ......... Continues (the incapacity payment is in the statutory-benefit base for the
                            employer's two days); SUSPENDED only for unpaid leave (CST art. 53).

Sources: CST arts. 227, 228, 236, 239; Decreto 2943 de 2013 art. 1; Decreto 780 de 2016 art. 3.2.1.10;
ET art. 206 nums. 1-2 and par. 1; Ley 361 de 1997 art. 26; Resolucion MSPS 2388 de 2016 Anexo Tecnico 2;
Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0.

```

---

## Sheet 4 - Tax Credit (Colombia has NONE - the equivalent mechanisms are deductions and exempt income)

```
COLOMBIA - TAX CREDITS: NOT APPLICABLE. THE EQUIVALENT MECHANISMS ARE DEDUCTIONS AND EXEMPT INCOME.

Colombia has NO tax credit against the payroll withholding - no personal credit, no child credit, no
disability credit and no non-refundable family credit of the kind the CZ template contemplates. Relief
is delivered instead by SUBTRACTING amounts from the base, in THREE legally distinct classes whose
class determines where each item sits in the ET art. 388 depuration and which caps it consumes.
Getting the class wrong is the most common source of withholding error in Colombia.

UVT (tax unit) 2026 = COP 52,374   (Resolucion DIAN 000238 de 15 diciembre 2025 art. 1; the 2026
uprating was certified at 5.17%, taking the unit from COP 49,799). Every tax parameter is indexed to
the UVT and NO tax threshold is expressed in minimum wages - that is the one-caliber discipline:
minimum wage for social security and labour, UVT for tax. The two are never mixed.

CLASS A - NON-TAXABLE INCOME (ingresos no constitutivos de renta ni ganancia ocasional)
  Subtracted at step (B), BEFORE the 40% cap reference figure is struck, so it does NOT consume the cap.
  A1  Mandatory pension contribution ......... 4% of the IBC .................... ET art. 55
  A2  Solidarity pension fund ............... 1% + 0.2-1.0% of the IBC .......... ET art. 55
  A3  Mandatory health contribution ......... 4% of the IBC .................... ET art. 56
  A4  Voluntary contributions to the individual pension account (RAIS):
        the lower of 25% of annual labour income and 2,500 UVT = COP 130,935,000 . ET art. 55
        (a non-qualifying withdrawal is withheld at 35%)
  A5  Third-party meal payments: not income up to 41 UVT/month = 2,147,334,
        where the employee's salary does not exceed 310 UVT = 16,235,940 ..... ET art. 387-1

CLASS B - DEDUCTIONS AND EXEMPT INCOME (deducciones y rentas exentas)
  Subtracted at steps (D) and (E), INSIDE the 40% and 1,340-UVT caps.
  B1  Housing-loan interest and monetary correction ... 100 UVT/month = COP 5,237,400 . ET arts. 119, 387
  B2  Prepaid medicine / health insurance ............  16 UVT/month = COP   837,984 . ET art. 387 lits. a, b
        (the provider must be supervised by the National Health Superintendence or the
         Financial Superintendence)
  B3  Dependants: 10% of the month's gross labour income, capped 32 UVT = COP 1,675,968 . ET art. 387
        NOTE: 10% OF GROSS REGARDLESS OF THE NUMBER OF DEPENDANTS - it does not multiply.
  B4  Voluntary pension funds + AFC / AVC long-term savings: the lower of 30% of labour
        income and 3,800 UVT/year = COP 199,021,200, SHARED between the two vehicles . ET arts. 126-1, 126-4
  B5  THE 25% EXEMPT-INCOME DEDUCTION ................ 790 UVT/year = COP 41,375,460 . ET art. 206 num. 10
        COMPUTED LAST, on the figure net of non-taxable income, the art. 387 deductions and all other
        exempt income: 'El calculo de esta renta exenta se efectuara una vez se detraiga del valor
        total de los pagos laborales recibidos por el trabajador, los ingresos no constitutivos de
        renta, las deducciones y las demas rentas exentas diferentes a la establecida en el presente
        numeral.' Computing 25% of GROSS overstates it and under-withholds.
        Monthly apportionment used: 65.8333 UVT = 3,447,955.
  B6  Cesantias and their interest: exempt in full where the average monthly income of the last six
        months is <= 350 UVT = 18,330,900; then tapering 90 / 80 / 60 / 40 / 20 / 0%
        through 410 / 470 / 530 / 590 / 650 UVT ......................... ET art. 206 num. 4
        They are EXCLUDED from the monthly base entirely under both procedures, and the 25%
        exemption does NOT apply to them (art. 206 par. 2).
  B7  Pension income: taxable only above 1,000 UVT/month = COP 52,374,000 ...... ET art. 206 num. 5
  B8  Accident, illness and maternity-protection indemnities and burial expenses: exempt ONLY up to
        the statutory minimum amount ................................. ET art. 206 nums. 1-3, par. 1

CLASS C - OUTSIDE THE CAPS ENTIRELY
  C1  Additional dependants deduction: 72 UVT per dependant per year = COP 3,770,928 each,
        maximum 4 dependants = COP 15,083,712/year, i.e. 6 UVT = COP 314,244 per dependant
        per month ..................................... ET art. 336 num. 3, second paragraph
        'en adicion al limite establecido en el inciso anterior' - it is applied AFTER and OUTSIDE
        the 40% and 1,340-UVT caps.
  STACKING: an EMPLOYEE may take BOTH B3 and C1 FOR THE SAME DEPENDANT. Decreto 2231 de 2023 art. 3:
        'el mismo dependiente solo dara lugar a una de estas dos deducciones, excepto cuando el
        contribuyente tenga ingresos por rentas de trabajo provenientes de una relacion laboral o
        legal y reglamentaria, en cuyo caso podran aplicarse ambas deducciones por el mismo
        dependiente.'

THE COMBINED CAP
  (D + E) <= 40% of (C = A - B)   AND   (D + E) <= 1,340 UVT/year = COP 70,181,160
  Monthly apportionment used: 111.6667 UVT = 5,848,430.
  OPEN ITEM: the 790-UVT and 1,340-UVT caps are stated ANNUALLY yet withholding is monthly. Market
  practice, which Mercans follows, apportions them at one twelfth and tests each month against the
  apportioned figure. No regulation prescribes the apportionment expressly. Carried in the QA report.
  The CURRENT year's UVT applies to the annual caps (DIAN Concepto 015007 int. 973 de 13 septiembre 2023).

NOT AVAILABLE AGAINST WITHHOLDING
  The 1% / 240-UVT invoice-based deduction of ET art. 336 num. 5 is expressly excluded - 'no se tendra
  en cuenta para el calculo de la retencion en la fuente' - confirmed by DIAN Concepto 015007 int. 973
  de 13 septiembre 2023. It is available only in the employee's own annual return.

NOT A CREDIT, AND NOT A TAX
  The Contribucion Solidaria a la Educacion Superior (Contribucion Sabes) is a CST art. 150 permitted
  DEDUCTION added by Ley 1911 de 2018 art. 22, not a tax and not a credit - it must never be
  aggregated with the retencion en la fuente on Formulario 350.

DECLARATIONS THE EMPLOYEE MUST MAKE (no relief is automatic except the 25%)
  Housing-loan interest ... lender certificate.  Prepaid health ... provider certificate.
  Dependants .............. number, EACH DEPENDANT'S IDENTITY DOCUMENT, relationship and basis of
                            dependency; for a dependent spouse, parent or sibling, a public
                            accountant's certificate of annual income below 260 UVT (COP 13,617,240)
                            or a certified state of physical or psychological dependence.
  Voluntary pension / AFC / AVC / RAIS ... fund or administrator certificates.
  Higher withholding rate ... written request, effective the month AFTER it is made (ET art. 383 par. 3).
  WHO QUALIFIES AS A DEPENDANT (ET art. 387 par. 2 nums. 2-3 as amended by Ley 2411 de 2024 art. 2):
    children up to 18; children 18-25 whose higher or technical education the taxpayer finances;
    children over 18 in a certified state of dependence; a spouse or permanent partner dependent by
    absence of income or with annual income below 260 UVT; parents and siblings on the same conditions.

OUT OF MERCANS SCOPE BUT FLAGGED SO THE ENGINE DOES NOT SILENTLY CLAMP THEM
  ET art. 206 par. 4 and Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 place art. 206 nums. 6-9, the
  prima especial and the prima de costo de vida OUTSIDE the 40% and 1,340-UVT limits. These attach to
  military, judicial, diplomatic and public university staff - out of private-sector scope.

NON-RESIDENTS GET NONE OF THE ABOVE
  ET art. 408: a flat 20% on the GROSS payment, with no depuration, no art. 387 deductions, no 25%
  exempt income and no tax-free band. DIAN Concepto 011108 de 29 junio 2026.
```

---

## Sheet 5 - Global WTC Coverage

| # | Item | Detail |
|---|---|---|
| 1 | Global baseline file | shared/Global_WTC_V1_0.xlsx |
| 2 | Global codes in the baseline | 300 |
| 3 | Global codes included in the Colombia WTC | 300 - ALL of them. None excluded. Every code configured FRESH for Colombia 2026 against CO-CCG-001 Modules 3-7 and the primary law in 00-official-sources/pdfs/. |
| 4 | Global codes excluded | 0 |
| 5 | Colombia-specific additions | 102 CO-prefixed wage types: 55 earnings (core pay, the six premium hour types, the statutory benefits, the leave cascade, the termination heads), 19 employee deductions, 11 employer contributions and accruals, 17 bases / intermediaries / rates / flags. |
| 6 | Total rows in the Wage Type Catalogue | 402 |
| 7 | SS-fund column expansion (why five, not one) | Colombia has EIGHT mandatory contributions across THREE insurance branches, THREE payroll levies and ONE employee-only solidarity surcharge, and they do NOT share a base. Q1 = Salud (EE 4% + ER 8.5%, IBC, cap 25 SMMLV, ER exonerable). Q2 = Fondo de Solidaridad Pensional (EE only, 1% from 4 SMMLV plus 0.2-1.0% from 16 SMMLV, IBC). Q3 = Riesgos Laborales / ARL (ER only, 0.348-8.7% by work centre, IBC). Q4 = Parafiscales CCF 4% + SENA 2% + ICBF 3% on the LEY 21 DE 1982 ART. 17 BASE WITH NO CEILING. R = Pension (EE 4% + ER 12%, IBC, cap 25 SMMLV, never exonerable). Collapsing Q4 into the others would silently cap the levies at 25 SMMLV and would drop paid rest days from their base. |
| 8 | Three Colombia-specific base columns added (S, T, U) | S = the HARD CST art. 127 / 128 salary flag, which the nomina electronica demands at ELEMENT LEVEL through paired S / NS element names and which must never be derived at reporting time. T = the statutory-benefit base (prima / cesantias / intereses), which INCLUDES the auxilio de transporte even though the IBC and the levy base exclude it. U = the vacation base of CST art. 192, which excludes ONLY rest-day work and supplementary overtime hours, so the night premium and commissions stay in. Values: Salary / Non-Salary / Paid Rest / Conditional / NA for S; Yes / No / Yes-No / NA for T and U. |
| 9 | Column meaning adopted (N, O, P) | N = subject to retencion en la fuente at all. O = subject to the ET art. 383 progressive table (0 / 19 / 28 / 33 / 35 / 37 / 39% on the art. 388 depurated base). P = SPECIAL TAX is used for the NON-RESIDENT flat 20% on gross of ET art. 408 - the treatment that produces a 17-fold withholding difference on the same salary and is the single largest configuration risk in Colombian expatriate payroll. |
| 10 | Yes-No entries and their justification | Every Yes-No (rendered 'Yes/No') marks a genuine statutory conditionality, and column D carries the explanation in every case, as the v2.5 C3 guard requires. The recurring reasons are: (a) the LEY 1393/2010 ART. 30 40% CLAMP, which excludes a validly pacted non-salary payment from the IBC only up to 40% of total remuneration and forces the excess back in; (b) the ET art. 387-1 meal thresholds; (c) the ET art. 206 num. 4 cesantias taper; (d) the ET art. 206 par. 1 statutory-minimum limit on EPS / ARL benefit exemptions; (e) the apprentice's phase-dependent regime; (f) the CST art. 130 viaticos split; and (g) the conditional character of an anticipo. |
| 11 | 2026 parameters used, and their verification | SMMLV 1,750,905 (Decreto 1469 de 2025 art. 1 - VERIFIED in the source PDF, which also records that the Council of State suspended the decree on 12 February 2026, that Decreto 0159 de 2026 re-fixed the identical amount, and that the suspension was revoked on 9 July 2026, so the AMOUNT was never in dispute). UVT 52,374 (Resolucion DIAN 000238 de 15-12-2025 art. 1 - VERIFIED in the source PDF). Auxilio de transporte 249,095 (Decreto 1470 de 2025 art. 1 - the decree itself is not in 00-official-sources; the figure is carried from CO-CCG-001 and is corroborated by the exact COP 2,000,000 combined minimum cash entitlement). IBC ceiling 25 SMMLV = 43,772,625 and salario integral at 70% (Ley 797 de 2003 art. 5 - VERIFIED verbatim). 40% clamp (Ley 1393 de 2010 art. 30 - VERIFIED verbatim). Levy base including paid rest days (Ley 21 de 1982 art. 17 - VERIFIED verbatim). Rest-day premium 80% -> 90% on 1 July 2026 (Ley 2466 de 2025 art. 14 - VERIFIED verbatim). Night window 19:00-06:00 (Ley 2466 art. 10 - VERIFIED verbatim). 42-hour week (Ley 2466 art. 11 - VERIFIED verbatim). Salary in kind 50% / 30% (CST art. 129 - VERIFIED verbatim). Vacation base (CST art. 192 - VERIFIED verbatim). Viaticos (CST art. 130 - VERIFIED verbatim). Tips (CST art. 131 - VERIFIED verbatim). Dotacion every four months (CST arts. 230, 232 - VERIFIED verbatim). Apprentice 75% / 100% (Ley 2466 art. 21 - VERIFIED verbatim). Connectivity allowance (Ley 2466 art. 53 - VERIFIED verbatim). Cesantias 8.33% monthly advance (Ley 2466 art. 64 - VERIFIED verbatim). |
| 12 | Newest-law check (control C2) | LEY 2381 DE 2024, the complete replacement of the Colombian pension architecture, is the newest pension law on the statute book and it does NOT govern any 2026 payroll period. Its own art. 94 set entry into force at 1 July 2025; Constitutional Court Auto 841 de 18 junio 2025 SUSPENDED that entry into force; and Judgment C-264 de 25 agosto 2026 upheld art. 94 on the understanding that the upheld provisions take effect on 1 APRIL 2027. Every 2026 period therefore runs on Ley 100 de 1993 as amended by Ley 797 de 2003, and NO part of Ley 2381 is configured as live. What changes in 2027: only the solidarity-fund surcharge, which becomes a single five-band 1.5% / 1.8% / 2.5% / 2.8% / 3.0% scale - the 16% total, the 12 / 4 split and the 25-SMMLV ceiling are unchanged. Recorded as a 2027 change-control item. |
| 13 | Configuration source | Configured fresh for Colombia from CO-CCG-001 v1.0 Modules 3-10, the 04-reports-spec files, and the primary law in 00-official-sources/pdfs/ (CST Decreto 2663 de 1950, Ley 100 de 1993, Ley 797 de 2003, Ley 1122 de 2007, Ley 1393 de 2010, Ley 21 de 1982, Ley 89 de 1988, Ley 2101 de 2021, Ley 2381 de 2024, Ley 2466 de 2025, Decreto 1469 de 2025, Decreto 0223 de 2026, Decreto 1990 de 2016, Decreto Ley 624 de 1989, Decreto Ley 2090 de 2003, Resoluciones DIAN 000227 y 000238 de 2025, Resolucion 2388 de 2016 y Anexo 2, Circular MinTrabajo 0101 de 2025, Oficio DIAN 13840 de 2025). NOT copied from Czechia, Cote d'Ivoire or any other country. |
| 14 | DERIVED flags | (1) The Mercans code numbers for the 102 Colombia-specific rows are DERIVED - no Mercans numeric code range has been assigned for Colombia, so mnemonic CO- codes are used and must be renumbered at system configuration. (2) The auxilio de transporte amount is carried from the CCG because Decreto 1470 de 2025 is not in 00-official-sources. (3) The additional high-risk pension rate is read from the Resolucion 2388 rate table (26% total against 16% standard, implying +10 pp employer-borne), NOT from the implementing decree - see the open items below. |
| 15 | Open items carried to the QA report | (1) The rate for the employer's first two sick days - Decreto 780 de 2016 art. 3.2.1.10 allocates the days but not the rate; Mercans default 66.67%, configurable. (2) The minimum-wage floor on incapacity payments - primary source not retrieved; Mercans default applies the floor, configurable. (3) The additional employer pension contribution for Decreto Ley 2090 de 2003 high-risk activities - the 2026 rate and base not confirmed from a primary regulatory source. (4) The monthly apportionment of the annual 790-UVT and 1,340-UVT tax caps - no regulation prescribes it expressly; Mercans applies one twelfth. |
| 16 | Egypt F20 guards | COMMISSION IS PRESENT as a first-class wage type (CO-COMISIONES) with its own nomina electronica element, and the global commission-bearing codes are configured, not dropped. EVERY tax code in column G is drawn from the Colombian legend below (CO-TX-01 to CO-TX-10 and CO-NA) and the validator rejects any code that does not start with 'CO-'. NO Yes-No appears in a taxability or subjection column without an explanation in column D. |

### Tax code legend (control C9 - every code defined and sourced to a Colombian authority publication)

*TAX CODE LEGEND (C9 - every code defined and sourced to a Colombian authority publication)*

| Tax Code | Meaning | Official Source |
|---|---|---|
| CO-TX-01 | Ordinary taxable work income - RESIDENT. Enters the total taxable payments of the month, is depurated under ET art. 388 (non-taxable income, art. 387 deductions, exempt income, the 40% cap and the 1,340-UVT annual cap) and is withheld on the ET art. 383 progressive table (0/19/28/33/35/37/39%) under Procedure 1 (art. 385) or at the fixed percentage under Procedure 2 (art. 386). No preferential rate and no tax-free allowance exists for any individual earning type. | Estatuto Tributario (Decreto-Ley 624 de 1989) arts. 383 (table as replaced by Ley 2010 de 2019 art. 42), 385, 386, 387, 388; Decreto 1625 de 2016 art. 1.2.4.1.6 par. 3 (as modified by Decreto 2231 de 2023 art. 9); Resolucion DIAN 000238 de 15 diciembre 2025 art. 1 (UVT 52,374). |
| CO-TX-02 | Severance savings and the interest on them (cesantias e intereses). EXCLUDED from the monthly withholding base under BOTH procedures - they never enter the monthly table read. Exempt IN FULL where the average monthly income of the last 6 months is <= 350 UVT (18,330,900); above that the untaxed portion tapers 90/80/60/40/20/0% through 650 UVT. The 25% exemption of art. 206 num. 10 does NOT apply to them (art. 206 par. 2). | ET arts. 206 num. 4 and par. 2, 385, 386; Ley 50 de 1990 art. 99; Ley 52 de 1975 art. 1; Ley 2466 de 2025 art. 64 (8.33% monthly advance deposit). |
| CO-TX-03 | Statutory minimum service bonus (prima de servicios legal). Under Procedure 1 it is withheld SEPARATELY, on its own read of the ET art. 383 table, and is NOT added to the month's salary. Under Procedure 2 it is folded into the ordinary monthly base (the 13 divisor of art. 386 already prorates its effect). Any excess above the statutory minimum bonus goes to the ordinary monthly base. | ET arts. 385 and 386; CST arts. 306 (as amended by Ley 1788 de 2016 art. 1), 307 and 308. |
| CO-TX-04 | Non-taxable income - ingreso no constitutivo de renta ni ganancia ocasional. Subtracted at step (B) of the ET art. 388 depuration, i.e. BEFORE the 40% cap reference figure is struck, which makes it more valuable than exempt income. Covers the employee mandatory pension 4%, the solidarity pension fund 1% + 0.2-1.0%, the mandatory health 4%, and voluntary contributions to the individual pension account within 25% of annual labour income / 2,500 UVT. | ET arts. 55 and 56; ET art. 388 num. 1; Formato 2276 v4 numerals N23 and N24 (which group the pension and solidarity-fund contributions on a single line). |
| CO-TX-05 | Conditionally not income - third-party meal payments (pagos de alimentacion a terceros). NOT income to the employee where BOTH conditions hold: the employee's salary does not exceed 310 UVT (16,235,940) AND the payment is made to a THIRD PARTY. Where the month's payments exceed 41 UVT (2,147,334) the EXCESS is taxable employment income. Cash paid to the employee for food is salary and gets none of this treatment. | ET art. 387-1; Formato 2276 v4 numerals N08 (excess) and N32 (within-limit amount), which report the two portions separately; Formulario 220 casillas 37 and 38. |
| CO-TX-06 | Not income and not remuneration - amounts given not to enrich the employee but to enable the work: statutory work clothing (dotacion), work tools, protective equipment, means of transport, representation expenses, occasional viaticos for transport, and genuine documented business-expense reimbursement. Outside EVERY base - tax, contribution, payroll-levy, statutory-benefit and vacation. | CST arts. 128 and 230 (art. 230 as modified by Ley 11 de 1984 art. 7); CST arts. 130 and 232; ET art. 387-1 final paragraph (representation expenses expressly outside the meal rule). |
| CO-TX-07 | Exempt income LIMITED TO THE STATUTORY MINIMUM AMOUNT - accident and illness indemnities, maternity-protection indemnities and employee burial expenses, and by extension the sickness, maternity, paternity and occupational-injury cash benefits paid by the EPS or the ARL. ET art. 206 par. 1 is explicit that the exemption 'operates only on the amounts corresponding to the statutory minimum' and that the excess is not exempt. | ET art. 206 nums. 1, 2, 3 and par. 1; CST arts. 227, 236; Decreto 780 de 2016 art. 3.2.1.10 (Decreto 2943 de 2013 art. 1, employer days 1-2). |
| CO-TX-08 | NON-RESIDENT flat withholding - 20% ON THE GROSS PAYMENT, with NO art. 388 depuration, NO 25% exempt income, NO art. 387 deductions and NO tax-free band, for Colombian-source work income. Determined at the moment of EACH payment on the status then held; the switch to the art. 383 table is PROSPECTIVE from the payment following the 183rd day, never retroactive. Where the service is performed entirely outside Colombia the income is foreign-source and there is NO withholding. | ET arts. 10, 408-415; DIAN Concepto 011108 de 29 junio 2026 (upholding Concepto 1789 int. 14595 de 2025); DIAN Oficio 28380 de 2019; Formulario 350 casillas 109-112 and hoja 2 casillas 141-155. |
| CO-TX-09 | Exempt income - renta exenta - for voluntary pension fund contributions (art. 126-1) and construction-savings / long-term-savings account contributions (arts. 126-4 AFC/AVC), employee or employer-paid on the employee's behalf. Subtracted at step (E) INSIDE the 40% and 1,340-UVT caps, within a single shared annual limit of the lower of 30% of labour income or 3,800 UVT (COP 199,021,200 for 2026). | ET arts. 126-1 and 126-4; ET art. 388 num. 2; Formulario 220 casillas 56, 57 and 58; Formato 2276 v4 numerals N26, N27 and N28. |
| CO-TX-10 | Pension income and refunds of pension savings. A retirement, invalidity, old-age, survivor or occupational-risk pension is taxable only on the monthly amount exceeding 1,000 UVT (COP 52,374,000). The 40% limit of art. 388 expressly does not apply to pension payments, pension substitution indemnities or refunds of pension savings. Paid by the pension administrator, so OUT OF SCOPE of employer gross-to-net per scope_manifest; retained for completeness and for Formulario 220 casilla 50 / Formato 2276 numeral N21. | ET arts. 206 num. 5 and par. 3, 383 (first paragraph, which brings pensions into the same table), 388 final sentence; Formulario 220 casilla 50; Formato 2276 v4 numeral N21. |
| CO-NA | Not a remuneration line - an employee deduction, an employer contribution or accrual, a calculation base, an intermediary, a notional, a rate or a configuration flag. Every taxability and subjection column is NA because the row is a mechanism, not a payment to the employee. | N/A - mechanism line. Reported, where reported at all, in the Deducciones block of the nomina electronica (Resolucion DIAN 000013 de 2021 Anexo Tecnico v1.0) or in the PILA settlement record (Resolucion MSPS 2388 de 2016 Anexo Tecnico 2). |

> **[QA MINOR-09]** `CO-TX-08` (non-resident flat 20%, ET art. 408) is fully defined in the legend but is
> assigned to **zero** of the 402 catalogue rows. This is **not an omission**: non-residency is a
> *residency-driven overlay* applied per employee through **column P (Special Tax)**, not a per-wage-type
> assignment. Assignment distribution across the catalogue: `CO-TX-01` 249 - `CO-NA` 109 - `CO-TX-06` 17 -
> `CO-TX-02` 9 - `CO-TX-10` 8 - `CO-TX-07` 5 - `CO-TX-03` 2 - `CO-TX-04` / `CO-TX-05` / `CO-TX-09` 1 each -
> `CO-TX-08` 0.


---

## Sheet 6 - Form Reference Guide (control C17)

| Wage Type Category | Spec File | Sheet Name | Row Number | Notes |
|---|---|---|---|---|
| Basic salary (CO-SALARIO-BASICO, global 62100-62109) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 84-85 (NIE069, NIE070) | DiasTrabajados and SueldoTrabajado. Days on the 30-day commercial month. |
| Basic salary -> annual salary certificate | CO-DIAN-004-Formulario220-Spec.xlsx | Formulario 220 Spec | Row 27 (casilla 36) | 'Pagos por salarios'. Also Formato 2276 numeral N05 (row 9). |
| Basic salary -> contribution bases | CO-PILA-003-AportesSeguridadSocial-Spec.xlsx | PILA Spec | Rows 106-111 (T2R2-040 to T2R2-045) | Salario basico, salario integral flag, then IBC pension / salud / ARL / CCF. T2R2-095 (row 112) carries the separate base for parafiscals other than the CCF. |
| All-inclusive salary flag (CO-SALARIO-INTEGRAL) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 65 (NIE056) | SalarioIntegral. PILA row 107 (T2R2-041). Drives IBC and levy base at 70%. |
| Transport / connectivity allowance (CO-AUX-TRANSPORTE, CO-AUX-CONECTIVIDAD, global 62520-62523) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 86 (NIE071) | AuxilioTransporte. OUT of the IBC and the levy base, so it appears in no PILA base field; IN the statutory-benefit base, so it feeds the Primas and Cesantias amounts. |
| Per diem - board and lodging portion (CO-VIATICOS-PERMANENTES) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 87 (NIE072) | ViaticoManuAlojS - the SALARY portion under CST art. 130. F220 casilla 43 (row 34). |
| Per diem - transport / representation and occasional (CO-VIATICOS-OCASIONALES) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 88 (NIE073) | ViaticoManuAlojNS - the NON-SALARY portion. Paired element; never merge the two. |
| Day overtime (CO-HED, global overtime codes) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 90-94 (NIE074-NIE078) | HED block: start time, end time, quantity, percentage, amount. Percentage reported at the real statutory rate per DIAN Concepto 013840 de 2025, not the annex literal. |
| Night overtime (CO-HEN) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 95-99 (NIE079-NIE083) | HEN block. |
| Night premium (CO-RECARGO-NOCTURNO) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 100-104 (NIE084-NIE088) | HRN block. 19:00-06:00 window since 25 December 2025. |
| Day overtime on a rest day (CO-HEDDF) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 105-109 (NIE089-NIE093) | HEDDF block. |
| Rest-day / holiday premium (CO-RECARGO-DOMINICAL) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 110-114 (NIE094-NIE098) | HRDDF block. 80% to 30 Jun 2026, 90% from 1 Jul 2026 - the annex's legacy 75/100/150/110 literals must not be configured. |
| Night overtime on a rest day (CO-HENDF) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 115-119 (NIE099-NIE103) | HENDF block. |
| Night premium on a rest day (CO-HRNDF) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 120-124 (NIE104-NIE108) | HRNDF block. |
| Vacation taken (CO-VACACIONES) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 126-129 (NIE109-NIE112) | VacacionesComunes. IN the IBC and the levy base - PILA change event VAC/LR at rows 90, 164-165. |
| Vacation compensated in cash (CO-VACACIONES-COMPENSADAS) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 130-131 (NIE115, NIE116) | VacacionesCompensadas. Contributory - the most commonly missed line in a termination settlement. |
| Service bonus (CO-PRIMA-SERVICIOS, global 62901) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 132-134 (NIE117-NIE119) | Primas, with PAIRED salary (Pago) and non-salary (PagoNS) amounts. F220 casilla 42 'prestaciones sociales' (row 33) / 2276 numeral N12 (row 16). |
| Severance savings and interest (CO-CESANTIAS, CO-INTERESES-CESANTIAS) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 135-137 (NIE120-NIE122) | Cesantias: Pago, Porcentaje, PagoIntereses. |
| Severance savings -> THREE separate certificate lines | CO-DIAN-004-Formulario220-Spec.xlsx | Formulario 220 Spec | Rows 38-40 (casillas 47, 48, 49) | Paid to the employee / traditional CST regime / deposited to the fund. Formato 2276 numerals N18, N20, N19 (rows 23-25). Never collapse the three. |
| Severance savings -> annual deposit planilla | CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx | Consignacion Cesantias Spec | Rows 25-30 (T09-T14) | Fund code, days worked, basic salary of the last month, and the cesantias value. Deposit by 14 February; MA01-MA05 (rows 39-43) cover the Ley 2466/2025 art. 64 monthly advance. |
| Sickness / occupational incapacity (CO-INCAP-EG-EMPLEADOR, CO-INCAP-EG-EPS, CO-INCAP-IRL) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 139-143 (NIE123-NIE127) | Incapacidad block with a Tipo discriminator. PILA IGE (row 88) and IRL (row 93); authorisation number and value at PILA rows 126-127 (T2R2-057, T2R2-058) for the employer's recovery. |
| Maternity / paternity / shared parental leave (CO-LIC-MATERNIDAD, CO-LIC-PATERNIDAD, CO-LIC-PARENTAL-COMPARTIDA) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 144-147 (NIE128-NIE131) | LicenciaMP. PILA LMA (row 89); authorisation number and value at PILA rows 128-129. |
| Statutory paid leave and bereavement (CO-LIC-REMUNERADA, CO-LIC-LUTO, CO-DESCANSO-REMUNERADO) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 148-151 (NIE132-NIE135) | LicenciaR. Paid rest, so IN the Ley 21/1982 levy base by name. |
| Unpaid leave (CO-LIC-NO-REMUNERADA) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 152-154 (NIE136-NIE138) | LicenciaNR. PILA SLN at rows 87, 158-159 - the levies fall to 0% for those days. |
| Legal strike (CO-HUELGA-LEGAL) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 155-157 (NIE143-NIE145) | HuelgaLegal block. |
| Bonuses - salary and non-salary (CO-BONIF-HABITUAL, CO-BONIF-NOSALARIAL, CO-GRATIF-OCASIONAL, global 62200-62229) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 159-160 (NIE139, NIE140) | BonificacionS / BonificacionNS. The salary flag is a hard configuration value, never derived at reporting time. |
| Allowances - salary and non-salary (global 62400-62880, CO-TELETRABAJO, CO-MEDICINA-PREPAGADA-ER) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 161-162 (NIE141, NIE142) | AuxilioS / AuxilioNS. |
| Salary in kind, equity, and any other concept (CO-SALARIO-ESPECIE, CO-ACCIONES) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 163-165 (NIE146-NIE148) | OtroConcepto with a mandatory description and paired ConceptoS / ConceptoNS amounts. No valuation scale exists in Colombia - a contractual value is required on every in-kind wage type. |
| Cooperative compensation (CO-COMPENSACION-COOP) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 166-167 (NIE149, NIE150) | CompensacionO / CompensacionE. Out of employment-payroll scope; F220 casilla 45 / 2276 numeral N15. |
| Voucher and meal payments (CO-BONO-EPCTV, CO-PAGO-ALIMENTACION-3P) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 168-171 (NIE151-NIE154) | BonoEPCTV: PagoS / PagoNS and PagoAlimentacionS / PagoAlimentacionNS. The ET art. 387-1 within-limit and excess portions are reported on SEPARATE information-return numerals - 2276 N32 (row 41) and N08 (row 12); F220 casillas 37 and 38 (rows 28-29). |
| Commissions (CO-COMISIONES) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 172 (NIE155) | Comision - its own dedicated element. F220 casilla 41 (row 32) / 2276 numeral N11 (row 15). |
| Third-party payments and advances (CO-PAGO-TERCERO, CO-ANTICIPO-NOMINA) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 173-174 (NIE193, NIE194) | PagoTercero and Anticipo in the DEVENGADOS block, paired with rows 200-201 (NIE195, NIE196) in the DEDUCCIONES block so the two legs net to zero. |
| Work clothing (CO-DOTACION) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 175 (NIE156) | Dotacion - a dedicated non-taxable, non-contributory informational element. |
| Apprentice maintenance support (CO-APOYO-APRENDIZ) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 176 (NIE157) | ApoyoSost. Contribution base floored at 1 SMMLV per Decreto 0223 de 2026 art. 2.2.6.3.3.4 par. 2. |
| Telework allowance (CO-TELETRABAJO) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 177 (NIE158) | Teletrabajo. |
| Retirement / settlement bonus (CO-BONIF-RETIRO) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 178 (NIE159) | BonifRetiro - separate from Indemnizacion. |
| Termination indemnities and penalties (CO-INDEM-DESPIDO, CO-INDEM-MORATORIA, CO-SANCION-CESANTIAS, CO-SANCION-INTERESES, CO-INDEM-FIJO-OBRA, CO-INDEM-PROTECCION) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 179 (NIE160) | Indemnizacion. Fully taxable, out of every social-security base. |
| Reimbursement (CO-REINTEGRO) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 180 (NIE201) | Reintegro in devengados, paired with row 207 (NIE184) in deducciones. |
| Employee health 4% (CO-DED-SALUD) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 182-183 (NIE161, NIE163) | Salud percentage and amount. PILA rows 123-124 (T2R2-054, T2R2-055). Non-taxable income at F220 casilla 53 / 2276 numeral N23. |
| Employee pension 4% (CO-DED-PENSION) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 184-185 (NIE164, NIE166) | FondoPension percentage and amount. PILA rows 114-115. F220 casilla 54 / 2276 numeral N24 group the pension and solidarity contributions on ONE line. |
| Solidarity pension fund (CO-DED-FSP-SOLIDARIDAD, CO-DED-FSP-SUBSISTENCIA) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 186-189 (NIE167-NIE170) | FondoSP with FOUR attributes - solidarity percentage and amount, subsistence percentage and amount. MUST NOT be merged into the pension line. PILA rows 119-120 (T2R2-051, T2R2-052). |
| Income tax withheld (CO-RETENCION-FUENTE, CO-RETENCION-NO-RESIDENTE) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 190 (NIE177) | RetencionFuente. |
| Income tax withheld -> monthly return | CO-DIAN-002-Formulario350-Spec.xlsx | Formulario 350 Spec | Rows 22-23 (casillas 77 and 93) | Rentas de trabajo: base sujeta a retencion and retenciones. Pension income at casillas 78 / 94 (rows 24-25). NON-RESIDENT payments at casillas 109-112 (rows 31-34) with the hoja-2 annex at casillas 141-155 (rows 36-50). |
| Income tax withheld -> annual certificate and information return | CO-DIAN-004-Formulario220-Spec.xlsx | Formulario 220 Spec | Row 52 (casilla 60) | Retencion on labour and pension income. Formato 2276 numeral N29 (row 37). The six-month average labour income for the cesantias taper sits at F220 casilla 59 (row 51) / 2276 numeral N33 (row 42). |
| Voluntary pension, AFC / AVC and RAIS contributions (CO-DED-PENSION-VOLUNTARIA, CO-DED-AFC-AVC, CO-DED-RAIS-VOLUNTARIO, CO-APORTE-PENSION-VOL-ER, CO-APORTE-RAIS-VOL-ER) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 192-193 (NIE198, NIE179) | PensionVoluntaria and AFC. F220 casillas 55-58 (rows 47-50) / 2276 numerals N25-N28 (rows 32-35) distinguish all four vehicles. PILA AVP at rows 91, 116-117, 121. |
| Union dues (CO-DED-SINDICATO) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 194-195 (NIE171, NIE172) | Sindicato percentage and amount. |
| Disciplinary sanctions (CO-DED-SANCION-DISCIPLINARIA) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 196-197 (NIE173, NIE174) | SancionPublic / SancionPriv. Lawful only under a duly approved reglamento interno. |
| Payroll lending (CO-DED-LIBRANZA) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 198-199 (NIE175, NIE176) | Libranza description and amount. Must leave at least 50% of net salary (Ley 1527 de 2012). |
| Cooperative dues (CO-DED-COOPERATIVA) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 203 (NIE180) | Cooperativa. |
| Garnishments (CO-DED-EMBARGO, CO-DED-ALIMENTOS) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 204 (NIE181) | EmbargoFiscal. Art. 155 20%-of-excess and art. 156 50%-of-whole ceilings are different ceilings for different claim types, tested independently. |
| Prepaid health / complementary plan (CO-DED-MEDICINA-PREPAGADA) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 205 (NIE182) | PlanComplementarios. Separately generates the 16-UVT/month art. 387 deduction. |
| Education debt and Contribucion Sabes (CO-DED-SABES) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Row 206 (NIE183) | Educacion. A DEDUCTION, not a tax - never aggregate it with the retencion on Formulario 350. |
| Employer loans, advances and other deductions (CO-DED-PRESTAMO, CO-DED-OTRAS) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 201-202, 208 (NIE196, NIE197, NIE185) | Anticipo, OtraDeduccion and Deuda. |
| Employer health 8.5% and the exoneration test (CO-ER-SALUD, CO-FLAG-EXONERACION-114-1) | CO-PILA-003-AportesSeguridadSocial-Spec.xlsx | PILA Spec | Rows 123-124, 36, 150 (T2R2-054, T2R2-055, A1-033, T2R2-076) | Employer-level and contributor-level exoneration flags. Not a nomina electronica element - employer contributions never appear there. |
| Employer pension 12% and high-risk uplift (CO-ER-PENSION, CO-ER-PENSION-ALTO-RIESGO) | CO-PILA-003-AportesSeguridadSocial-Spec.xlsx | PILA Spec | Rows 114-118, 152 (T2R2-046 to T2R2-050, T2R2-079) | Rate, mandatory contribution, voluntary member and employer amounts, total, and the special-rate indicator. Nomina electronica AltoRiesgoPension flag at row 54 (NIE043). |
| Occupational risk (CO-ER-ARL) | CO-PILA-003-AportesSeguridadSocial-Spec.xlsx | PILA Spec | Rows 131-135 (T2R2-061, T2R2-062, T2R2-063, T2R2-077, T2R2-078) | Rate, work centre, contribution, ARL code and risk class. Class varies by WORK CENTRE, not geography. |
| Payroll levies CCF / SENA / ICBF (CO-ER-CCF, CO-ER-SENA, CO-ER-ICBF) | CO-PILA-003-AportesSeguridadSocial-Spec.xlsx | PILA Spec | Rows 137-142 (T2R2-064 to T2R2-069) | Rate and value per levy. Bases at rows 111-112: T2R2-045 for the CCF and T2R2-095 for the other parafiscals, which diverge when SENA and ICBF are exonerated and the CCF is not. ESAP and MEN (rows 143-146) are public-sector only. |
| Contributory days per subsystem | CO-PILA-003-AportesSeguridadSocial-Spec.xlsx | PILA Spec | Rows 101-104 (T2R2-036 to T2R2-039) | Pension / health / occupational risk / CCF days, reported per subsystem because a change event can reduce them for one and not another. |
| Change events (novedades) driving every base | CO-PILA-003-AportesSeguridadSocial-Spec.xlsx | PILA Spec | Rows 78-93 (T2R2-015 to T2R2-030) | ING, RET, TDE/TAE, TDP/TAP, VSP/VST, SLN, IGE, LMA, VAC-LR, AVP, VCT, IRL, with the paired date fields at rows 155-170. |
| Statutory benefit accruals (CO-PROV-PRIMA, CO-PROV-CESANTIAS, CO-PROV-INTERESES-CESANTIAS, CO-PROV-VACACIONES) | DERIVED - no statutory filing | n/a | DERIVED | Accounting provisions totalling 21.8333%. They feed the Primas, Cesantias and Vacaciones amounts when the benefit is actually paid, but no return reports the provision itself. |
| Rounding residual (CO-REDONDEO) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 210-213 (NIE186-NIE189) | Redondeo, DevengadosTotal, DeduccionesTotal, ComprobanteTotal. Round-half-to-even with a +/-2.00 tolerance - distinct from the PILA's round-up-to-100 and the DIAN forms' nearest-1,000. |
| Tax residence and place of service (CO-FLAG-RESIDENCIA-FISCAL) | CO-DIAN-001-NominaElectronica-Spec.xlsx | Nomina Electronica Spec | Rows 61-64 (NIE050-NIE053) | LugarTrabajoPais and the rest of the place-of-work block. PILA 'colombiano en el exterior' (row 70) and 'extranjero no obligado a cotizar a pensiones' (row 69) carry the related flags. |
| Dependants declaration (CO-FLAG-DEPENDIENTES) | CO-DIAN-004-Formulario220-Spec.xlsx | Formulario 220 Spec | Rows 68-71 (casillas 79-82) | Document type, number, names and relationship per dependant. Formato 2276 numeral N34 (row 43) requires the DOCUMENT, not merely a count. |
| Withholding procedure election (CO-FLAG-PROCEDIMIENTO-RETENCION) | DERIVED - no statutory filing | n/a | DERIVED | Elected by the employer per employee; no return discloses the election. It nonetheless changes the reported withholding in June and December materially. |
| Bases (CO-BASE-IBC, CO-BASE-PARAFISCAL, CO-BASE-RETENCION, CO-BASE-PRESTACIONAL, CO-BASE-VACACIONES) and the 40% clamp intermediary (CO-INT-CLAMP40) | CO-PILA-003-AportesSeguridadSocial-Spec.xlsx | PILA Spec | Rows 108-112 (T2R2-042 to T2R2-045, T2R2-095) | The IBC columns are where the 40% clamp lands. The withholding base surfaces at Formulario 350 casilla 77; the statutory-benefit and vacation bases are DERIVED and surface only through the benefit amounts they produce. |

**65 entries.** Validated mechanically: every target file exists, every sheet name resolves and every row number is in range - **0 broken pointers**. Two entries are honestly marked `DERIVED - no statutory filing` (benefit accruals; withholding-procedure election).

---

## Catalogue statistics (from the QA cross-check, 2026-09-07)

| Metric | Value |
|---|---|
| Global baseline file | `shared/Global_WTC_V1_0.xlsx` |
| Global codes in the baseline | 300 |
| Global codes included in the Colombia WTC | **300 (100.0%)** |
| Global codes excluded | **0** |
| Colombia-specific additions (`CO-` prefixed) | **102** |
| Total Wage Type Catalogue rows | **402** |
| Blank cells across the 11 subjection columns | **0** (all 402 rows) |
| `Yes/No` conditional entries | 246 - **all 246** carry a substantive column-D justification (control C3) |
| Tax codes defined and sourced | 11 (`CO-TX-01`...`CO-TX-10` + `CO-NA`), all with Colombian authority citations (control C9) |

**Colombia-specific additions by category:** Earnings (core pay, six premium hour types, statutory benefits,
leave cascade, termination heads) **55** - Employee deductions **19** - Employer contributions and accruals
**11** - Calculation bases **5** - Configuration flags **8** - Taxes **2** - Rates / percentages **2** -
Intermediary / notional **2** - total **102** (of which 8 flags + 5 bases + 2 rates + 2 notional = 17
non-monetary).

**Catalogue-wide category distribution:** Earning 295 - Deduction 71 - Employer Contribution 16 - Flag 8 -
Base 5 - Percentage 3 - Tax 2 - Intermediary 1 - Notional 1.

## 2026 mid-year cut-overs encoded in the Formula column (do NOT simplify)

| Change | Before | From | Legal basis |
|---|---|---|---|
| Sunday / holiday rest-day premium (recargo dominical y festivo) | **80%** | **90% from 1 July 2026** (then 100% from 1 July 2027) | Ley 2466 de 2025 |
| Compounded rest-day overtime `CO-HEDDF` | 205% | **215%** from 1 Jul 2026 | idem |
| Compounded rest-day overtime `CO-HENDF` | 255% | **265%** from 1 Jul 2026 | idem |
| Compounded rest-day night premium `CO-HRNDF` | 115% | **125%** from 1 Jul 2026 | idem |
| Monthly hourly divisor | **220** | **210 from 15 July 2026** | Ley 2101 de 2021 (progressive working-week reduction) |

> The WTC explicitly warns that the nomina electronica technical annex's **legacy `75 / 100 / 150 / 110`
> literals must NOT be configured**. Use the dual-dated statutory values above.

---

## Payslip-to-WTC wiring gap (QA MAJOR-01)

The payslip generator carries `XXXXX` placeholders instead of real WTC codes on 36 cells (18 lines x 2 language
sheets). The correct codes, all of which exist in this catalogue, are:

`CO-SALARIO-BASICO` - `CO-AUX-TRANSPORTE` - `CO-COMISIONES` - `CO-DED-SALUD` - `CO-DED-PENSION` -
`CO-DED-FSP-SOLIDARIDAD` - `CO-RETENCION-FUENTE` - `CO-ER-SALUD` - `CO-ER-PENSION` - `CO-ER-ARL` -
`CO-ER-CCF` - `CO-ER-SENA` - `CO-ER-ICBF` - `CO-PROV-CESANTIAS` - `CO-PROV-INTERESES-CESANTIAS` -
`CO-PROV-PRIMA` - `CO-PROV-VACACIONES`.

Payslip lines *Overtime & Surcharges* and *Commissions & Bonuses* each bundle multiple wage types and must be
split into their constituent codes (or labelled with an explicit multi-code list) - see also QA MINOR-05 on the
CST art. 192 vacation base.

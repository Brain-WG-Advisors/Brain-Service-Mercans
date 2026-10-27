# RA: PMI employer-paid pensioners and PILA (Anexo Técnico 3) - 2026-10-21

**Analyst:** Compliance Regulation Analyst (Mercans, Colombia). Primary sources only, all read on 2026-10-21.
**Client facts (from the caller, not verified here):** PMI pays 454 pensioners directly (WT 62154, run "CO - Pensionaries") and 21 retirees (WT 62151, run "CO - Retirees"). It deducts the pensioners' health contribution at 4% / 10% / 12%.

## Sources used
| # | Source | Version / date | Where |
|---|---|---|---|
| S1 | MinSalud, Anexo Técnico 3 "Aportes a Seguridad Social de Pensionados" (Res. 2388/2016) | **AT3 v15, 24-07-2026**, 133 pp. | `raw/docs/oficiais/CO/2026-10-21-MinSalud-Anexo-Tecnico-3-PILA-pensionados.pdf` (md5 cf0bf837e8027e85cbfe4276b0d676ba). Downloaded from https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/OT/anexo-tecnico3-pensionados.pdf |
| S2 | MinSalud, Anexo Técnico 2 "Aportes a Seguridad Social de Activos" | AT2 v30, 24-07-2026 | `raw/docs/oficiais/CO/2026-10-21-MinSalud-Anexo-Tecnico-2-PILA-consolidado.pdf` |
| S3 | Res. MSPS 2388/2016, art. 1 (as amended by Res. 728/2023) | compiled text | https://normativa.colpensiones.gov.co/compilacion/docs/resolucion_minsaludps_2388_2016.htm |
| S4 | Res. MSPS 1271/2023 (14 Aug 2023), which amends AT1, AT2 and AT3 | DO 52.488 | `raw/docs/oficiais/CO/2026-10-21-Res-MSPS-1271-2023-colpensiones.htm` |
| S5 | Ley 100/1993, arts. 143, 157, 204 par. 5, 280 | FuncionPublica | `raw/docs/oficiais/CO/2026-10-21-Ley-100-1993-FuncionPublica.html` |
| S6 | Decreto 780/2016 (DUR Salud), arts. 2.1.9.7, 2.2.1.1.2.1, 3.2.1.1, 3.2.2.1, 3.2.3.9 | FuncionPublica | `raw/docs/oficiais/CO/2026-10-13-Decreto-780-2016-FuncionPublica.html` |
| S7 | Ley 797/2003, art. 8 (new Ley 100 art. 27) | Secretaría del Senado | http://www.secretariasenado.gov.co/senado/basedoc/ley_0797_2003.html |
| S8 | Res. DIAN 000227/2025, art. 1.5.3.2.3 | p. 246 | `frentes/pipeline/mercans-pipeline/CO-compliance/00-official-sources/pdfs/Resolución 000227 de 23-09-2025.pdf` (md5 819beb815d965ddbc679a6f6a8374910) |
| S9 | Mercans spec CO-PILA-003 (read-only) and CO-DIAN-001 | kit 05-final | `Research Pipeline/Colombia/co-report-crosscheck/05-final/` |

Housekeeping: `raw/docs/oficiais/CO/2026-10-21-Res-MSPS-1271-2023-PILA-pensionados.pdf` is **not a PDF**. It is a saved UGPP "Página no encontrada" (404) HTML page. Use the `.htm` file (S4). Nothing in `raw/` was changed.

---

## Q1. Is an employer that pays pensions directly obliged to self-settle and pay its pensioners' health contribution (and FSP / CCF) through PILA?

**Verdict: OBLIGATED** for health. **OBLIGATED** for FSP where the pension is above 10 SMMLV. **NOT OBLIGATED (optional)** for CCF.

1. **Pensioners are contributing members of the contributory health regime.** Ley 100 art. 157 A.1 (S5): *"Los afiliados al Sistema mediante el régimen contributivo son las personas vinculadas a través de contrato de trabajo, los servidores públicos, los pensionados y jubilados y los trabajadores independientes con capacidad de pago."*
2. **The pensioner bears the contribution.** Ley 100 art. 143 inc. 2 (S5): *"La cotización para salud establecida en el Sistema General de Salud para los pensionados está, en su totalidad, a cargo de éstos"*. The base is the pension payment: Decreto 780 art. 2.2.1.1.2.1 (S6): *"Para los pensionados las cotizaciones se calcularán con base en la mesada pensional."*
3. **The rate** is set by Ley 100 art. 204 par. 5 (S5). From 2022: 1 SMLMV → 4%; >1 to 2 SMLMV → 10%; >2 SMLMV → 12%. The inciso added by Ley 2294/2023 art. 78 reads *"El aporte a salud a cargo de los pensionados que devengan entre 2 y 3 salarios mínimos se reducirá del 12% al 10%, el cual regirá a partir de la vigencia de 2024 previa reglamentación del Gobierno nacional"*.
   - Res. 1271/2023 art. 1 (S4) added to AT1 a table *"A partir del año 2024"*: 1 SMLMV 4%; >1 SMLMV and up to 3 SMLMV 10%; >3 SMLMV 12%.
   - But AT3 v15 (S1, ch. 4 §9, pp. 112-113) still shows, for employer pensioner types 5 and 6, *"1 de enero de 2022 en adelante … 4% 10% 12%"*, with no row for 2024.
   - **The 2-3 SMMLV band is NOT LOCATED / CONFLICTING.** To close it: the current AT1 (Glosario) version from MinSalud, plus any decree or MinSalud circular that issues the "reglamentación" of Ley 2294 art. 78.
4. **The pension payer settles and pays through PILA.**
   - Decreto 780 art. 3.2.3.9 num. 1 (S6): *"Los aportantes y los pagadores de pensiones cuyo número de cotizantes y/o pensionados se encuentren en la siguiente tabla, deberán autoliquidar y pagar sus aportes utilizando la Planilla Integrada de Liquidación de Aportes - PILA, mediante la modalidad de planilla electrónica"*. With 20 or more, the electronic planilla has been mandatory since 6 March 2017. With 454 pensioners, PMI must file electronically.
   - The payer's liability is also stated in Decreto 780 art. 2.1.9.7 (S6): *"Cuando el pagador de pensiones incurra en mora en el pago de los aportes a cargo de los pensionados … Las EPS deberán adelantar las acciones de cobro frente a los aportantes en mora."*
   - The deadlines in art. 3.2.2.1 apply to *"Todos los aportantes"*.
5. **The PILA rules apply to employers as pension payers.**
   - Res. 2388/2016 art. 1 (S3) adopts the PILA annexes *"a reportar por aportantes, pagadores de pensiones y operadores de información"*. Among them: *"Anexo Técnico 3. Aportes a Seguridad Social de Pensionados. En este anexo se reporta la información de los pensionados"*.
   - AT3 v15 §1.2.4 campo 27 (S1, p. 13): *"01- Empleador: Debe ser utilizado por las empresas públicas o privadas o personas naturales que tienen a su cargo el pago de pensiones de sus trabajadores."*
   - AT3 §1.2.3 (p. 12): *"J. Jurídica: Persona ficticia de creación legal responsable del pago de aportes al Sistema de Seguridad Social Integral y Parafiscales de sus pensionados."*
6. **FSP (Fondo de Solidaridad Pensional).**
   - Ley 797/2003 art. 8, new Ley 100 art. 27 num. 2 lit. d (S7): *"Los pensionados que devenguen una mesada superior a diez (10) salarios mínimos legales mensuales vigentes y hasta veinte (20) contribuirán para el Fondo de Solidaridad Pensional para la subcuenta de subsistencia en un 1%, y los que devenguen más de veinte (20) salarios mínimos contribuirán en un 2%"*.
   - Ley 100 art. 280 (S5) makes the solidarity contributions *"obligatorios en todos los casos y sin excepciones"*.
   - In AT3 the FSP is AT3 campo 47 (§2.2.2.21, p. 61): *"Este campo es obligatorio para mesadas superiores a 10 SMLMV."*
   - Campos 45 and 46 (the 4-SMMLV solidarity / subsistence points, pp. 59-61) apply to pensioners who still contribute to pensions.
7. **CCF.** AT3 ch. 4 §6, table 9 "R6 - Tipo de pensión vs Subsistema al que aporta" (S1, pp. 107-108) marks CCF **"O" (Opcional)** for every pension type. Ley 1643 de 2013 is cited by AT3 for this (campo 27 type 04, p. 13), but its text was **not read** here.
8. **Pension contribution** is not owed on an ordinary jubilación or convencional pension. R6 shows PEN blank for types 10 and 13. It applies only to shared or "para compartir" types (11, 14: PEN = X) and is optional for 12, 20 and 21.
   - AT3 campo 10 "Pensión compartida" (p. 22) covers *"cuando el pensionado a cargo del empleador ya o…"*.
   - Whether PMI's pensions are shared with Colpensiones is a **client fact still to be obtained**.

## Q2. Which file / planilla, which version, structure and key fields?

**Verdict: OBLIGATED. The file is Res. 2388/2016 Anexo Técnico 3, AT3 v15 dated 24-07-2026** (S1). It was downloaded to `raw/docs/oficiais/CO/2026-10-21-MinSalud-Anexo-Tecnico-3-PILA-pensionados.pdf`.

The latest amending acts on the cover (pp. 1-2) are Res. 1271/2023, 221/2024, 467/2025 and 1529/2026. The latest implementation item, ch. 5 §5.32 (p. 133), applies to payments from 1 Oct 2026 (identification-number validations).

**Structure** (S1, ch. 1):

| File / record | Content | Size |
|---|---|---|
| Archivo tipo 1 "Datos generales del pagador de pensiones" (p. 7) | Payer data | 27 fields, positions 1-482 |
| Archivo tipo 2, registro tipo 1 "Encabezado" (pp. 14-16) | Header | 18 fields, positions 1-285 |
| Archivo tipo 2, registro tipo 2 "Liquidación detallada de aportes" (pp. 21-38) | One per pensioner per pension type | 63 fields, positions 1-519 |
| Registros tipo 3-7 (ch. 2, pp. 65-72) | Totals for pensions, FSP subsistencia, health, CCF and grand total | Generated by the **operador**, not by the payer |

**Key fields for PMI:**

Archivo tipo 1:
- **Campo 7 "Clase de pagador de pensiones":** *"A. Pagador de pensiones con 200 o más pensionados"* (p. 12). PMI, with 454, is class A.
- **Campo 27 "Tipo de pagador de pensiones"** = **01 Empleador** (p. 13).

Header (registro tipo 1):
- **Campo 14:** número total de pensionados.
- **Campo 15:** valor total de la nómina, equal to the sum of campo 58 (p. 15).
- **Campo 18 "Tipo de planilla pensionado"** (pp. 15-20): **P** *"Planilla pago normal pagadores de pensiones: Es considerada como la planilla principal y se utiliza por todos los tipos de pagadores de pensiones para el pago de los aportes mensuales"*. The other types are R (retroactivo), L (reliquidación before Jan 2020), V (reliquidación from Jan 2020) and C (territorial entities, not applicable).
- Precondition for P (p. 16): *"el pagador de pensiones debe estar relacionado en el archivo 'INFORMACIÓN PAGADORES DE PENSIONES' dispuesto mensualmente por este Ministerio"*. If it is not listed, the payer must ask MinSalud's Subdirección de Pensiones to be added.

Registro tipo 2, pensioner identification:
- Campos 3-6: names. Campo 7: document type (as amended by Res. 1271/2023 art. 3, S4). Campo 8: número de identificación del pensionado.
- **Campo 9 "Tipo de pensión":** e.g. 1 Vejez, 10 Jubilación, 11 Jubilación para compartir, 13 Convencional, 14 Convencional para compartir.
- Campo 10: pensión compartida S/N.
- **Campo 17 "Tipo de pensionado":** **05** *"Pensionado por el empleador con tope de pensión máxima de 25 SMMLV"* or **06** *"Pensionado por el empleador sin tope de pensión máxima de 25 SMMLV … el aporte al Sistema General de Seguridad Social en Salud debe ser hasta 25 SMLMV"* (p. 48). Types 05 and 06 are valid with payer type 01 (R01, p. 101).
- Campo 18: pensionado en el exterior (X means no health contribution, p. 49).

Registro tipo 2, mesada and IBC:
- **Campo 58 "Valor de mesada pensional"** is mandatory and may exceed 25 SMMLV. It is the base for FSP and CCF (p. 64).
- **Campo 63 "Valor total de mesada pensional"** drives the health-rate selection under Ley 100 art. 204 par. 5 (p. 64).
- **Campo 39 IBC.**
- Novedades: campo 22 ING, 23 RET, 28 VSP, 29 SUS. Day counts: campos 35-38.

Registro tipo 2, health:
- **Campo 32:** código EPS.
- **Campo 48 "Tarifa de aportes a Salud"**: *"A partir del periodo de enero de 2020 … la tarifa a reportar se determinará según lo establecido en el parágrafo 5 del artículo 204 de la Ley 100 de 1993"*. The operador validates it against campo 63 (p. 63).
- **Campo 49 "Cotización obligatoria a salud"** = campo 48 × campo 39 (p. 63).

Registro tipo 2, FSP:
- **Campos 45 / 46 / 47** (pp. 59-62). Campo 47 is mandatory above 10 SMLMV: 1% for >10-20, 2% for >20.

Registro tipo 2, CCF:
- **Campos 34 / 51 / 52** (optional, p. 63).

Registro tipo 2, pension (shared types only):
- Campos 30 and 40-41.

## Q3. Does CO-PILA-003 already cover it?

**Verdict: NOT COVERED. AT3 is a different file and layout from AT2.**

- The spec was searched for "pensionad", "pensioner", "Anexo Técnico 3", "AT3", "pagador de pensiones", "retiree" and "planilla".
  - It cites only **AT2 v30** ("Res. MSPS 2388 de 2016 Technical Annex 2", sheet File Structure B5). There is no hit for AT3 or for "pagador de pensiones".
  - Its pensioner content is about **employees**. It covers the "Employed old-age pensioner in active service" (sub-type 01, Payroll Scope Summary row 17, and row 45). Field Options C127/C128/C133 list the AT2 sub-types 1, 2 and 9 (pensioners who are **active contributors**).
  - Row 22, "Pensioner whose pension is paid by a fund, not by the employer", is marked **NO**. The spec has **no row for a pensioner whose pension is paid by the employer**.
- **Different file.** AT2 is *"Aportes a Seguridad Social de Activos. Contiene la información que deben reportar los cotizantes activos"*. AT3 is *"Aportes a Seguridad Social de Pensionados"* (S3, art. 1). They differ in five ways:
  - **Submitting party.** AT3 is filed by the *pagador de pensiones*, with its own archivo tipo 1 (27 fields, 482 positions).
  - **Planilla types.** AT3 uses P/R/L/V/C. AT2 uses E/Y/A/I/N/…
  - **Detail record.** The AT3 detail record has 63 fields and 519 positions, with pensioner-specific fields: tipo de pensión, tipo de pensionado, causante, pensión compartida, mesada (58), mesada total (63), FSP 45-47 and UPC adicional.
  - **No ARL, SENA or ICBF** in AT3.
  - **Its own validation tables** (ch. 4 R01-R6) and **its own output files** to the administradoras (ch. 3).
- So the pensioners' PILA is a **separate monthly planilla**. It is not an extra set of records inside the employees' AT2 file.

## Q4. Retirees (21) paid WT 62151 "not a pension": any PILA obligation?

**Verdict: NOT OBLIGATED, on the facts given. Only the pensioners need PILA.**

- AT3 covers *"la información de los pensionados"* (S3, art. 1). Every AT3 detail record needs a campo 9 tipo de pensión and campo 58 mesada pensional (S1). A payment that is not a pension has no AT3 record.
- AT2 covers *"cotizantes activos"* (S3). The retirees are former employees, so no employment relationship exists in the period. For employees the health and pension base is *"el salario mensual que aquellos devenguen"* (Decreto 780 art. 2.2.1.1.2.1, S6). A post-employment instalment of a voluntary-retirement-plan bonus is not wages of an active contributor, so there is no AT2 record either.
- **Condition.** This depends on WT 62151 really being a bonus paid in instalments, as BAU answer Q19 says (recorded in `HANDOFF-2026-10-21.md` line 39). If any of the 21 actually receive a periodic **extralegal / convencional retirement pension** from PMI, they become AT3 pensioners: tipo de pensión 10 Jubilación or 13 Convencional *"de acuerdo con la ley o la convención colectiva"* (AT3 p. 40), tipo de pensionado 05/06.
- **No primary text was located that names this specific payment**, so the verdict is a derivation from the scope of AT2 and AT3. To close it: the plan document or the client's confirmation that 62151 is not a life or periodic pension.

## Q5. Does the Nómina Electrónica cover pensioners paid by the employer?

**Verdict: OBLIGATED. The NE covers them, and the CO-DIAN-001 spec covers them only partially.**

- Res. DIAN 000227/2025 art. 1.5.3.2.3 (S8, p. 246): *"Los sujetos obligados a generar y transmitir para validación el documento soporte de pago de nómina … son aquellos contribuyentes del impuesto sobre la renta y complementarios, que realizan pagos o abonos en cuenta que se deriven de una vinculación, por una relación laboral o legal y reglamentaria y por pagos a los pensionados a cargo del empleador, que requieran soportar los costos y deducciones en el impuesto sobre la renta"*.
- Art. 1.5.3.2.2 (same page) refers to *"pagos … de pensiones, correspondiente a las liquidaciones de nómina realizadas en el mes inmediatamente anterior"*.
- **CO-DIAN-001 today:**
  - The text knows the rule. Payroll Scope Summary row 21 cites *"pensions borne by the employer (Res. DIAN 000227 de 2025 art. 1.5.3.2.1)"*. The RetencionFuente element (Nomina Electronica Spec M191) includes withholding WTs 21140 and 21155 *"on the pensions the employer pays itself"*.
  - But it has **no scope row "Pensioner whose pension is paid by the employer = YES"**. Only row 17 (employed pensioner) and row 22 (fund-paid pensioner = NO) exist.
  - **Mapping not checked:** how a pensioner's mesada and the health deduction (Salud at 4/10/12%, not 4%) are mapped to the NE elements. This RA did not look at that mapping in the annex.
- Note also that the art. 1.5.3.2.1 cited in row 21 should be checked against 1.5.3.2.2 / 1.5.3.2.3. The text quoted above is in 1.5.3.2.3.

---

## Decision basis

PMI pays pensions directly to 454 pensioners, so it is a **pagador de pensiones (tipo 01 Empleador)**.

Under Ley 100 arts. 143, 157 and 204 par. 5, Decreto 780 arts. 2.1.9.7 and 3.2.3.9, and Res. 2388/2016 art. 1 with Anexo Técnico 3 (v15, 24-07-2026), it must every month self-settle and pay, through an electronic PILA, these contributions withheld from the mesadas:
- the pensioners' health contribution;
- the FSP subsistence contribution on mesadas above 10 SMMLV (Ley 797/2003 art. 8);
- pension contributions only for shared or "para compartir" pensions.

It files on **planilla type P under AT3**, and PMI must appear in MinSalud's "INFORMACIÓN PAGADORES DE PENSIONES" file.

This is a **mandatory statutory social-security report of PMI, distinct from the employees' PILA**. It has a different annex, file layout, planilla types, detail record and validation rules, and it is not covered by CO-PILA-003, which is built on AT2 and, for pensioners, scopes in only employed pensioners. It therefore falls within the agreed scope "social security (PILA …)" of 15 Oct 2026 as a **separate spec** (an AT3 "PILA pensionados" spec), not as an amendment to CO-PILA-003.

The 21 retirees paid WT 62151 are outside PILA unless the client confirms the payment is in fact a periodic pension.

Open points:
- the 2-3 SMMLV health band from 2024 (Res. 1271/2023 AT1 vs AT3 v15 table 9);
- whether PMI's pensions are shared with Colpensiones (campo 10, pension fields);
- whether PMI pays the optional CCF contribution;
- the NE scope row and mapping for employer-paid pensioners in CO-DIAN-001.

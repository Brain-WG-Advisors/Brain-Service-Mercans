# RA answers - Q14, Q16, Q17 (PMI Colombia report specs)

Date: 2026-10-21. Author: Compliance researcher (RA). Method: primary official sources only. Each quote was read in the source itself. Secondary sites were used only to find documents and are not cited.

Sources downloaded today (all in `raw/docs/oficiais/CO/`):
- `2026-10-21-MinSalud-Anexo-Tecnico-2-PILA-consolidado.pdf`: Res. 2388/2016 Anexo Técnico 2, consolidated, **"CÓDIGO: AT2 VERSIÓN: 30 FECHA: 24-07-2026"** (last act listed: Res. 1529 de 2026). Source URL: https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/OT/anexo-tecnico2-cotizantes.pdf
- `2026-10-21-UGPP-Empleadores-IBC-2021.pdf`: UGPP, "Ingreso base de cotización - Empleadores". Source URL: https://www.ugpp.gov.co/sites/default/files/Parafiscales/Empleadores-IBC-2021.pdf
- `2026-10-21-Ley-1393-2010-SecretariaSenado.html`, `2026-10-21-Ley-789-2002-SecretariaSenado.html`, `2026-10-21-CST-pr006-SecretariaSenado.html` (secretariasenado.gov.co)
- `2026-10-21-UGPP-Res-205-2024-modifica-Res-1702-2021.pdf`: checked and **not relevant**. It covers the standards for collecting overdue contributions (cobro de cartera morosa), not IBC parameters.

Sources already on the machine:
- Res. MSPS 467/2025 (`2026-10-13-Res-MSPS-467-2025-PILA.pdf`)
- Ley 21/1982 (`2026-10-13-Ley-21-1982-SENA.htm`, SENA compilation)
- Ley 100/1993 (`2026-10-21-Ley-100-1993-FuncionPublica.html`)
- DUR 780/2016 and DUR 1072/2015 (FunciónPública copies)
- DIAN Caja de Herramientas Nómina Electrónica V1.0 (`Research Pipeline/Colombia/CO-compliance/integration-sources/dian-ne/caja/...`), which contains the Anexo Técnico V1.0 (Res. 000013/2021) and XSD v1.0.6.

---

## Q14. Termination notified after the month's PILA was already paid (30 days, no RET)

**Answer**

1. **Planilla type: `N - Planilla correcciones`.** Correction lines go in pairs, using campo 22 "Correcciones":
   - **A** = the original record, loaded by the operator;
   - **C** = the correct record, supplied by the contributor.

   The operator settles only the difference C minus A. The return must go through the **same operator** that settled the original planilla.
2. A RET novelty that was left out of the original planilla falls under **numeral 2** of planilla N. It is allowed **only for the same settlement period**, and the planilla N must be filed **by the last business day of the month in which payment is due**. In that case no mora interest is charged.
3. **Hard limit:**
   - Planilla N accepts only novelties where the C record reports values **equal to or greater than** the A record.
   - The sum of IBC and the sum of days in the C records must each be at least those in the A records.
   - Planilla N "No se puede utilizar para correcciones que impliquen devolución de valores pagados en exceso".

   Reporting RET after a 30-day line has been paid **lowers the days, and normally the IBC**. That fails the C ≥ A test, so **this case cannot be corrected through planilla N or any other PILA planilla.** The contributor must request the **refund ("devolución o reintegro") directly from each administradora** that received the contributions (Circular 009 of 24-01-2011 of the Ministerio de la Protección Social). PILA "no es el medio para compensar dineros, ni realizar devoluciones".
4. Planilla N stays available when the correction does **not** reduce days or IBC. Examples: RET with the exit date on day 30, or final-settlement amounts that raise the IBC for the same period. If filed after the deadline in numeral 2, mora interest applies ("Los valores liquidados a través de este tipo de planilla deberán incluir los intereses de mora a que haya lugar").

**Quotes**

Res. 2388/2016 Anexo Técnico 2, AT2 v30 (24-07-2026), §2.1.1.2.2 "Campo 8. Tipo de planilla", pp. 38-39. The same wording is in Res. MSPS 467/2025 art. 2 num. 3, hojas 8-9.

> "N. Planilla correcciones. Es utilizada en los siguientes casos:
> 1. Cuando el aportante deba corregir el Ingreso Base de Cotización – IBC; la tarifa; el tipo de cotizante; el subtipo de cotizante; la cotización; las novedades; [...] o días reportados en la planilla inicial de periodos ya vencidos o para el mismo periodo de liquidación. No se puede utilizar para correcciones que impliquen devolución de valores pagados en exceso.
> 2. Para reportar las novedades de retiro, variación permanente de salario, [...] que fueron omitidas en la planilla inicial y que correspondan al mismo periodo de liquidación, siempre y cuando la presentación de esta planilla se realice a más tardar el último día hábil del mes en que debe realizar el pago y no habrá lugar al pago de intereses de mora.
> En estos casos, solo se permitirán aquellas novedades que en el registro "C" reporten valores iguales o mayores a los reportados en el registro "A". Cuando el aportante necesite reportar novedades que implique la devolución de aportes lo deberá hacer a través de cada una de las administradoras y solicitar la devolución o reintegro de aportes ante las respectivas entidades a las cuales se les giraron los aportes a Seguridad Social y Parafiscales de acuerdo con lo establecido en la Circular 009 de fecha 24 de enero de 2011 expedida por el Ministerio de Protección Social, teniendo en cuenta que la Planilla Integrada de Liquidación de Aportes - PILA, no es el medio para compensar dineros, ni realizar devoluciones a los aportantes."

AT2 v30, "Disposiciones comunes a la Planilla N – planilla correcciones", pp. 45-46:

> "Este tipo de planilla solo puede ser liquidada a través del operador de información con el cual se liquidó la planilla inicial [...]"
> "Los valores liquidados a través de este tipo de planilla deberán incluir los intereses de mora a que haya lugar de acuerdo con los períodos de que se trate."
> "La sumatoria del IBC de los registros C debe ser mayor o igual a la sumatoria del IBC de los registros A y la sumatoria de los días de los registros C debe ser mayor o igual a la sumatoria de días de los registros A. La sumatoria de los días reportados en los registros tipo C debe ser igual a 30, a menos de que exista una novedad de ingreso o retiro."

AT2 v30, §2.1.2.3.9 "Campo 22 – Correcciones", p. 144:

> "Solo aplica para la planilla tipo N – Planilla Correcciones [...] A Cuando se usa este valor, se indica que la información contenida en el respectivo registro es la que corresponde a la liquidación original [...] C [...] es la que corresponde a la liquidación correcta [...] El operador de información debe calcular el valor correcto de los aportes con base en la información contenida en los registros marcados con C [...] y restar los valores ya liquidados y pagados contenidos en los registros marcados con A [...]"

- **Sources:** MinSalud, Anexo Técnico 2 AT2 v30 (URL above; local PDF), pp. 38-39, 45-46, 144. Res. MSPS 467/2025 art. 2 num. 3 (local PDF, hojas 8-9, 14-15).
- **Confidence:** **High.** The rule is quoted from the consolidated annex in force, and the 2025 amending resolution says the same.
- **Not verified:** the text of Circular 009/2011 (the refund procedure itself). The annex only refers to it.

---

## Q16. Nómina Electrónica - data type of `Cantidad` in VacacionesCompensadas / VacacionesComunes

**Answer**

- In the XSD both attributes are **`xsd:integer`** and `use="required"`. **They cannot carry decimals.**
  - `47.75` is rejected by schema validation.
  - So is `47.0`, because `xs:integer` has no decimal point.
- Annex V1.0 marks the field as type **N** with no size. Table 3 defines N as accepting the decimal point. This **is less strict than the XSD**, but it does not override it: the document is validated against the XSD. The validation rules (NIE111 / NIE115) say only "Se debe colocar la cantidad de Dias".
- For comparison, `Pago` is `xsd:decimal`.
- The adjustment note (NominaIndividualDeAjuste XSD v1.0.6) uses the same `xsd:integer` type for Cantidad.

**Mechanical test** (lxml, run with `python -I` on a copy of the XSD set; the instance was DIAN's own sample `Nomina Individual Electronica V1.0.2.xml`, with only `VacacionesCompensadas/@Cantidad` changed):
- `47` → no error on Cantidad.
- `47.75` → "attribute 'Cantidad': '47.75' is not a valid value of the atomic type 'xs:integer'".
- `47.0` → same error.

The ajuste XSD gave the same result. DIAN's sample is not fully schema-valid for unrelated reasons (placeholders), so only the Cantidad-specific errors are reported.

**Quotes**

`NominaIndividualElectronicaXSDV1.0.6.xsd` ("<!--Version #1.0.6-->"), lines 516-543:
```xml
<xsd:element name="VacacionesComunes" minOccurs="0" maxOccurs="unbounded">
  ... <xsd:attribute name="Cantidad" type="xsd:integer" use="required" />
      <xsd:attribute name="Pago" type="xsd:decimal" use="required" />
<xsd:element name="VacacionesCompensadas" minOccurs="0" maxOccurs="unbounded">
  ... <xsd:attribute name="Cantidad" type="xsd:integer" use="required" />
      <xsd:attribute name="Pago" type="xsd:decimal" use="required" />
```

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica, Versión 1.0 (Res. DIAN 000013 of 11-02-2021), field table:
- p. 31: VacacionesComunes/@Cantidad: "Número de días que el trabajador estuvo inactivo durante el mes por vacaciones." | T: A | F: N | Padre: VacacionesComunes | Oc: 1-1 | Obs.: "Cantidad de Dias" | V 1.0
- p. 32: VacacionesCompensadas/@Cantidad: "Número de días que el trabajador estuvo activo durante el mes sin disfrutar sus vacaciones. (Vacaciones NO disfrutadas)" | T: A | F: N | Padre: VacacionesCompensadas | Oc: 1-1 | Obs.: "Cantidad de Dias" | V 1.0
- p. 10, Tabla 3: "N Numérico: solamente son aceptados los números "0" a "9", el punto de separación decimal, y las señales "+" y "-"."
- p. 192, validation rules: "NIE111 R Cantidad - Cantidad de Dias - Se debe colocar la cantidad de Dias"; "NIE115 R Cantidad - Cantidad de Dias - Se debe colocar la cantidad de Dias".

- **Sources:**
  - XSD: `Research Pipeline/Colombia/CO-compliance/integration-sources/dian-ne/caja/Caja-de-Herramientas-Nomina-Electronica-V1-0/XSD/NominaIndividualElectronicaXSDV1.0.6.xsd` and `...DeAjusteElectronicaXSDV1.0.6.xsd`. These come from DIAN's Caja de Herramientas: https://www.dian.gov.co/impuestos/factura-electronica/Documents/Caja-de-Herramientas-Nomina-Electronica-V1-0.zip
  - Annex: `.../Anexo Tecnico/Anexo Tecnico Documento Soporte de Pago de Nómina Electrónica - V1.0.pdf` (text in `.../dian-ne/_txt/anexo-tecnico-v1.0.txt`).
  - The local snapshot of DIAN's technical-documentation page links only Res. 000013/2021 + annex and Caja V1.0. No later XSD version was found on the machine.
- **Confidence:** **High.** The XSD type was read directly and confirmed by the validation test.
- **Not located:** any DIAN rule on **how to report a fractional day count** (rounding or truncation). Only a DIAN statement (concepto / FAQ / annex note) would settle that. Without one, the only thing that can be stated is that the value must be a whole number.

---

## Q17. Vacation compensated in cash on termination: part of the IBC?

### (b) Parafiscales (CCF, SENA, ICBF): **YES** (statute + UGPP)

**Quotes**

Ley 21 de 1982, art. 17:
> "Para efectos de la liquidación de los aportes al régimen del Subsidio Familiar, Servicio Nacional de Aprendizaje, SENA, Escuela Superior de Administración Pública, (ESAP), Escuela Industrial e Institutos Técnicos, se entiende por nómina mensual de salarios la totalidad de los pagos hechos por concepto de los diferentes elementos integrantes del salario en los términos de la Ley Laboral, cualquiera que sea su denominación y además, los verificados por descansos remunerados de Ley y convencionales o contractuales."

UGPP, "Ingreso base de cotización - Empleadores" (2021):
- p. 23:
  > "Incluir en el IBC el valor pagado de las vacaciones disfrutadas, compensadas en dinero o pagadas por liquidación de contrato, para el cálculo de los aportes parafiscales (Ley 21 de 1982, artículo 17)."
- pp. 16 and 22 (diagram): "IBC PARAF = Total pagos salariales + Total pagado por Vacaciones".

**Assessment**
- The statute includes "descansos remunerados de Ley". The UGPP, the authority that audits these contributions, reads that phrase as **expressly covering vacation compensated in cash and vacation paid on contract liquidation**.
- Art. 17 names Subsidio Familiar (CCF) and SENA. The ICBF base is the "nómina mensual de salarios" of Ley 89/1988 art. 1, which was **not downloaded** in this round. The UGPP document groups ICBF in the same IBC PARAF.

- **Sources:** Ley 21/1982 art. 17 (`raw/docs/oficiais/CO/2026-10-13-Ley-21-1982-SENA.htm`); UGPP PDF (URL above; local copy `2026-10-21-UGPP-Empleadores-IBC-2021.pdf`).
- **Confidence:** **Medium-High.** The statute is clear about "descansos remunerados", and the UGPP's official reading names compensated vacation explicitly. That UGPP document is official guidance, not a resolution. ICBF: Medium, pending Ley 89/1988 art. 1.

### (a) Health and pension: **NOT LOCATED as an express primary rule.** The official signals point to exclusion.

**What the primary sources say**
- **Ley 100/1993 art. 18** (as now worded): "La base para calcular las cotizaciones [...] será el salario mensual. El salario mensual base de cotización para los trabajadores particulares será el que resulte de aplicar lo dispuesto en el Código Sustantivo del Trabajo."
- **Art. 204 par. 1:** the health base "será la misma contemplada en el Sistema General de Pensiones".
- **Ley 1393/2010 art. 30:** "[...] para los efectos relacionados con los artículos 18 y 204 de la Ley 100 de 1993, los pagos laborales no constitutivos de salario de las trabajadores particulares no podrán ser superiores al 40% del total de la remuneración."
- **DUR 780/2016 art. 3.2.5.1** deals only with vacation **enjoyed**: "Las cotizaciones durante vacaciones y permisos remunerados se causarán en su totalidad y el pago de los aportes se efectuará sobre el último salario base de cotización reportado con anterioridad a la fecha en la cual el trabajador hubiere iniciado el disfrute de las respectivas vacaciones o permisos."
- **CST art. 189** (num. 1 per Ley 1429/2010 art. 20; num. 3) and **Ley 789/2002 art. 27** cover the right to compensation and its base ("se tomará como base el último salario devengado"). **Neither says whether the payment is salary or part of the IBC.**
- **UGPP (same 2021 document):**
  - p. 18: "total remunerado", the denominator of the 40% rule, is the "totalidad de pagos salariales y pagos no salariales [...] excluyendo las prestaciones sociales de los títulos VIII y IX del CST, **los pagos por vacaciones** y las indemnizaciones".
  - pp. 16/22/23: "IBC SGSS" = "Calculo de novedades del periodo + Total pagos salariales + Total pagos no salariales que exceden el 40% total remunerado". Vacation enters SGSS only as an enjoyed-vacation novelty (Decreto 806/1998 art. 70, now DUR 780 art. 3.2.5.1).

**Assessment**
- Taken together, the UGPP treats vacation payments as **neither salary nor a "non-salary payment"** for the 40% test. Compensated vacation therefore stays **outside the IBC for health and pension and outside the 40% computation**.
- However, **no law, decree or resolution was found that says this in so many words.** It is an inference from Ley 100 art. 18 (salary per the CST) plus UGPP guidance.

**What would close it**

One of these, read in the original:
- a UGPP resolution or concepto, or a CSJ / Consejo de Estado ruling, stating that compensated vacation is not part of the IBC for SGSS; or
- the current UGPP "protocolo de parámetros" (see the note below).

**Confidence:** **NOT LOCATED (express rule).** Direction from the official sources: excluded (Low-Medium).

**Note on "Res. UGPP 1740/2019":** the consolidated AT2 v30 (p. 1, list of incorporating acts) shows **Res. 1740 de 2019 is a MinSalud resolution**: "Por la cual se modifican los Anexos Técnicos 2, 3 y 5 de la Resolución 2388 de 2016, relacionados con la Planilla Integrada de Liquidación de Aportes". It is **not** a UGPP parameters protocol. A UGPP act adopting a "protocolo de parámetros" was **not located** on ugpp.gov.co in this round.

The UGPP Acuerdo 1035/2015, Sección II, which listed non-salary payments, is cited by the UGPP document but has **no vacation-compensation rule** in the text read (normativa.colpensiones.gov.co copy). Arts. 2-3 of that Acuerdo are reported annulled by the Consejo de Estado. The ruling itself was not read, so this is unconfirmed.

---

## Effect on the specs (05-final; read only, not edited)

**Q14: CO-PILA-003.** The current text states only part of the rule.
- `Payroll Scope Summary!C41`: "PILA: a return type N (correcciones) or M (mora)." The type is correct.
- `PILA Spec!M79` (RET): "For a dependent employee the value is X (withdrawal from all the systems settled) in the period in which the termination date falls, and blank in every other period". This agrees with the annex.
- **Missing:** the spec does not state the AT2 v30 limits on planilla N:
  - it is the same-period route for an omitted RET only if filed by the last business day of the month in which payment is due;
  - the C records must be ≥ the A records in IBC and in days;
  - it may not be used for anything that leads to a refund, which must be claimed from each administradora outside PILA.

  As written, the spec could be read as "a late RET is fixed with planilla N", which **differs** from the annex when the RET lowers days or IBC.

**Q16: CO-DIAN-001.** The spec already states the same rule.
- `Nomina Electronica Spec!J129` (NIE111, VacacionesComunes Cantidad): "N (integer days)".
- `Nomina Electronica Spec!J131` (NIE115, VacacionesCompensadas Cantidad): "N (integer days)".

Both match the XSD `xsd:integer`. The spec has no rule for fractional counts (e.g., 47.75); no primary source was located for one (see Q16).

**Q17: CO-DIAN-001 and CO-PILA-003.** Partly the same, partly different.
- **(a) Health/pension.** Both specs **already say** compensated vacation is excluded from the social-security base:
  - CO-DIAN-001 `Payroll Scope Summary!C27`: "enjoyed vacation is in the contribution base, compensated vacation is not."
  - CO-DIAN-001 `Nomina Electronica Spec!M131`: "compensated vacation is NOT part of the social-security contribution base while enjoyed vacation is".

  This matches the official direction (UGPP guidance), but no **express primary** rule was located. The cells are stated as settled law without a citation, so they currently go further than the evidence.
- **(b) Parafiscales.** The CO-PILA-003 text **differs in part** from Ley 21/1982 art. 17 and the UGPP reading.
  - `Payroll Scope Summary!C27` ("Paid rest days"): "In the PARAFISCAL base (Ley 21 de 1982 art. 17) - campo T2R2-095 - which is why that base differs from the four contribution bases."
  - `PILA Spec!M111` (campo 45, IBC CCF): "campo 45 is the base for the CCF contribution, campo 95 the base for SENA, ICBF, ESAP and MEN, which under Ley 21 de 1982 art. 17 includes paid rest days".
  - `Population Rules!C4`: "The fourth is the IBC CCF of campo 45: the monthly salary payroll of Ley 21 de 1982 art. 17 [...] The fifth is the PARAFISCAL base of campo 95 [...] it INCLUDES paid rest days".

  Art. 17 defines the base for the **Subsidio Familiar (CCF)** and SENA alike, including "descansos remunerados de Ley". The UGPP (p. 23) includes compensated and liquidation vacation for "aportes parafiscales", with IBC PARAF covering CCF, SENA and ICBF. The spec places paid rest days **only** in campo 95 and leaves them out of campo 45 (CCF). **That is a difference to resolve.** The SENA/ICBF side (campo 95) matches.

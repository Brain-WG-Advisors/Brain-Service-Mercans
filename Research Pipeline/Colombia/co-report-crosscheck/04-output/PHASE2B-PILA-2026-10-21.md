# Phase 2b - CO-PILA-003 (campo 45 / campo 95; planilla N limits)

Date: 2026-10-21. Status: PROPOSED map, not applied. Map: `04-output/final-prep/CO-PILA-003-phase2b-map.json` (11 edits, `current` read live from [[Research Pipeline/Colombia/co-report-crosscheck/05-final/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx|CO-PILA-003-AportesSeguridadSocial-Spec.xlsx]]; every `proposed` checked against `WORDS` in `scripts/make_final.py`, zero hits; no T/U cell, no Version Control cell).

Sources read for this note (all local, page numbers are the PDF page numbers printed in the footer):
- [[raw/docs/oficiais/CO/2026-10-21-MinSalud-Anexo-Tecnico-2-PILA-consolidado.pdf|2026-10-21-MinSalud-Anexo-Tecnico-2-PILA-consolidado.pdf]]: AT2 version 30, 24-07-2026.
- `raw/docs/oficiais/CO/2026-10-21-Ley-21-1982-FuncionPublica.html`: **downloaded today** from https://www.funcionpublica.gov.co/eva/gestornormativo/norma.php?i=4827. The Secretaría del Senado URLs `ley_0021_1982.html` and `ley_21_1982.html` return 404. The text matches the SENA copy `2026-10-13-Ley-21-1982-SENA.htm`.
- [[raw/docs/oficiais/CO/2026-10-21-UGPP-Empleadores-IBC-2021.pdf|2026-10-21-UGPP-Empleadores-IBC-2021.pdf]], p.23. Used only for the point marked NOT LOCATED in A.3.
- Circular 009/2011 was **not opened** and is not cited in any proposed text.

---

## A. Campo 45 vs campo 95

### Quotes
- **AT2 v30 p.92, record tipo 2 layout, campo 45** "IBC CCF" (positions 229-237, N): "Es un campo obligatorio para los tipos de cotizante 1, 2, 18, 22, 30, 51 y 55. Lo suministra el aportante. Para el caso del tipo de cotizante 31 no es obligatorio cuando la cooperativa o precooperativa de trabajo asociado este exceptuada por el Ministerio del Trabajo."
- **AT2 v30 p.101, campo 95** "IBC otros parafiscales diferentes a CCF" (positions 665-673, N): "Es un campo obligatorio para los tipos de cotizante 1, 18, 20, 22, 30, 31, y 55. Lo suministra el aportante."
- **AT2 v30 p.30, §2.1.1.1 campo 20** "Valor total de la nómina": "corresponde a la sumatoria de los valores reportados en la planilla en el campo '45 – IBC CCF' del registro tipo 2 del archivo tipo 2, para los tipos de cotizantes diferentes a independientes. Para los tipos de cotizantes no obligados a aportar a Cajas de Compensación Familiar este valor debe ser cero."
- **AT2 v30 p.161, §2.1.2.3.30 campo 65** (CCF): "multiplicando el valor del campo 45 - 'IBC CCF' [...] por el valor del campo 64 - 'Tarifa de aportes CCF'".
- **AT2 v30 pp.162-164, §§2.1.2.3.32, .34, .36, .38** (campos 67 SENA, 69 ICBF, 71 ESAP, 73 MEN): each value is "multiplicando el valor del campo 95 - 'IBC - Otros parafiscales diferentes a CCF' [...]" by its rate. Same pattern in the settlement rules on pp.280-281.
- **AT2 v30 on vacation/rest days:** nowhere does the annex say which payments make up campo 45 or campo 95. "Descanso" does not appear. "Vacaciones" appears only as a novelty: the VAC-LR flag; planilla N numeral 2 on p.38; the ARL IBC exception on p.47 (campo 44, not 45/95); and type 21 students on p.110.
- **Ley 21/1982 art. 17:** "Para efectos de la liquidación de los aportes al Régimen del Subsidio Familiar, Servicio Nacional de Aprendizaje (SENA), Escuela Superior de Administración (ESAP), Escuelas Industriales e Institutos Técnicos, se entiende por nómina mensual de salarios la totalidad de los pagos hechos por concepto de los diferentes elementos integrantes del salario en los términos de la Ley Laboral, cualquiera que sea su denominación y además, los verificados por descansos remunerados de ley y convencionales o contractuales."

### Decision
1. **Paid rest days (vacation enjoyed, other remunerated statutory/conventional/contractual rest): BOTH campo 45 and campo 95.**
   - Art. 17 gives one definition of the base for the Subsidio Familiar (the CCF, which AT2 settles on campo 45) and for SENA/ESAP (which AT2 settles on campo 95), and that definition expressly includes "descansos remunerados".
   - The spec places them in campo 95 only. That conflicts with the statute → edits to C27, M111, C4 and D21.
2. **ICBF:** art. 17 does not name the ICBF. AT2 uses a single campo 95 for SENA, ICBF, ESAP and MEN, so the value in campo 95 is the same for all four. The ICBF's own base (Ley 89/1988 art. 1) was **not read**, and no proposed text attributes the ICBF base to Ley 21.
3. **Vacation compensated in cash / paid on termination: NOT LOCATED in AT2 v30 or in the text of Ley 21 art. 17.**
   - Art. 17 says "pagos [...] verificados por descansos remunerados" and does not say whether cash paid instead of rest falls inside it.
   - The UGPP guide (p.23) says it does: "Incluir en el IBC el valor pagado de las vacaciones disfrutadas, compensadas en dinero o pagadas por liquidación de contrato, para el cálculo de los aportes parafiscales (Ley 21 de 1982, artículo 17)."
   - That is guidance, not AT2 or the statute. Per the brief, **no change is proposed on this point**. The spec keeps "paid rest days" without naming compensated or liquidation vacation.
   - Decision for Wallisson: whether to add it on the strength of UGPP p.23.
4. **Header campo 20:** File Structure!B35 calls it "the PARAFISCAL base sum". AT2 p.30 makes it the sum of campo 45 → edit B35. PILA Spec M58, Population Rules C9/D4, Example Analysis C18/D18 and Sample File A76-A77 already state the AT2 rule.

### Cells checked and left unchanged (A)
- `Payroll Scope Summary!C28`, `Population Rules!D20`: ceiling rules are consistent.
- `PILA Spec!M112`: the inclusion of rest days in campo 95 is correct. Its phrase "populated under their own AT2 v30 rules" is loose, because AT2 gives no content rule for either field ("Lo suministra el aportante"). It was left alone (minimal edits); if wanted, align it with the M111 wording.
- `Example Analysis!D22`, `Report Matrix!A32`, `PILA Spec!M58/M137-M142`, `Population Rules!C13`, `Field Options!D163/D164`: consistent.
- `PILA Spec!M90/M164/M165`: compensated vacation (WT 79003) does not raise VAC-LR. This is about the novelty, not the bases, so no conflict.

---

## B. Planilla N limits (Q14)

### Quotes
- **AT2 v30 §2.1.1.2.2 campo 8, type N, pp.38-39:**
  > "N. Planilla correcciones. Es utilizada en los siguientes casos: 1. Cuando el aportante deba corregir el Ingreso Base de Cotización – IBC; la tarifa; el tipo de cotizante; el subtipo de cotizante; la cotización; las novedades; la exoneración de pago de aportes patronales en salud, SENA e ICBF; la condición de colombiano en el exterior; la condición de extranjero no obligado a cotizar a pensión o días reportados en la planilla inicial de periodos ya vencidos o para el mismo periodo de liquidación. No se puede utilizar para correcciones que impliquen devolución de valores pagados en exceso.
  > 2. Para reportar las novedades de retiro, variación permanente de salario, variación transitoria de salario, suspensión de contrato de trabajo por licencia no remunerada o comisión de servicios, incapacidad temporal por enfermedad general, licencia de maternidad o paternidad, vacaciones, licencia remunerada, incapacidad por accidente de trabajo o enfermedad laboral que fueron omitidas en la planilla inicial y que correspondan al mismo periodo de liquidación, siempre y cuando la presentación de esta planilla se realice a más tardar el último día hábil del mes en que debe realizar el pago y no habrá lugar al pago de intereses de mora.
  > En estos casos, solo se permitirán aquellas novedades que en el registro 'C' reporten valores iguales o mayores a los reportados en el registro 'A'. Cuando el aportante necesite reportar novedades que implique la devolución de aportes lo deberá hacer a través de cada una de las administradoras y solicitar la devolución o reintegro de aportes ante las respectivas entidades a las cuales se les giraron los aportes a Seguridad Social y Parafiscales de acuerdo con lo establecido en la Circular 009 [...], teniendo en cuenta que la Planilla Integrada de Liquidación de Aportes - PILA, no es el medio para compensar dineros, ni realizar devoluciones a los aportantes."
- **AT2 v30 "Disposiciones comunes a la Planilla N", pp.45-46:**
  > "Este tipo de planilla solo puede ser liquidada a través del operador de información con el cual se liquidó la planilla inicial, salvo cuando la Superintendencia Financiera haya autorizado su desmonte [...]"
  > "Los valores liquidados a través de este tipo de planilla deberán incluir los intereses de mora a que haya lugar de acuerdo con los períodos de que se trate."
  > "[...] por cotizante se deberá reportar un grupo de registros A e inmediatamente después un grupo de registros C. La sumatoria del IBC de los registros C debe ser mayor o igual a la sumatoria del IBC de los registros A y la sumatoria de los días de los registros C debe ser mayor o igual a la sumatoria de días de los registros A. La sumatoria de los días reportados en los registros tipo C debe ser igual a 30, a menos de que exista una novedad de ingreso o retiro."
- **AT2 v30 §2.1.2.3.9 campo 22 "Correcciones", p.144:**
  > "A Cuando se usa este valor, se indica que la información contenida en el respectivo registro es la que corresponde a la liquidación original y que se desea corregir o aplicarle algún tipo de variación. Este registro debe ser cargado por el operador de información con el cual se liquidó la planilla inicial. C [...] es la que corresponde a la liquidación correcta [...] Esta información debe ser suministrada por el aportante. [...] El operador de información debe calcular el valor correcto de los aportes con base en la información contenida en los registros marcados con C en este campo 22, y restar los valores ya liquidados y pagados contenidos en los registros marcados con A en este campo 22."
- **AT2 v30 section 16 "Manejo de planilla tipo N", item h, p.284 (full):**
  > "Siempre que se utilice el tipo de planilla 'N – Planilla Correcciones' los operadores de información deberán liquidar los intereses de mora a que haya lugar de acuerdo con la normativa vigente, a excepción del pago de retroactivos salariales; o del reporte de la novedad de retiro cuando se realice en los plazos establecidos en las disposiciones aplicables o cuando los empleadores o los trabajadores independientes o dependientes realicen el pago de los montos faltantes de las cotizaciones al Sistema General de Pensiones correspondientes a los períodos de cotización de los meses de abril y mayo del año 2020, desde el 1 de junio de 2021 hasta el 31 de mayo de 2024, al que hace referencia el artículo 2.2.3.5.2. del Decreto 1833 de 2016, adicionado por el artículo 1° del Decreto 376 de 2021."
- **AT2 v30 §2.1.1.2.2 campo 8, type M, p.37:**
  > "M. Planilla mora: Es utilizada para el pago de aportes de períodos respecto de los cuales se encuentra ausencia total del pago para el o los sistemas de seguridad social [...] No podrá incluirse en este tipo de planilla otro sistema respecto del cual se esté realizando una corrección para incrementar un valor, aunque corresponda a la misma persona, pues ese tipo de corrección debe hacerse mediante la Planilla tipo N."
- **AT2 v30 §2.1.1.1 campos 9 and 10, pp.27-28:**
  > "Debe dejarse en blanco cuando el tipo de planilla sea E, A, I, M, S, Y, H, T, X, K, Q o B" / "se incluirá el número de la planilla del período correspondiente cuando el tipo de planilla sea N, F o W".

### Decisions
- **M79** is the rule cell. It now carries:
  - the same operador;
  - C ≥ A in IBC and days;
  - no use for refunds;
  - no interest for a same-period omitted RET filed by the last business day of the payment month (num. 2 + item h);
  - a RET that lowers days or IBC is outside PILA, with the refund claimed from each administradora.
- **C41** loses "or M (mora)" as a correction route (type M is total absence of payment; p.37) and states the N limits.
- **C49** limits the associated return number and date to type N (campos 9/10 blank for M).
- **M85 and Field Options D143** state the opposite of AT2 campo 22 ("A adds a contributor omitted"). They are rewritten to the annex definition.
- **Field Options D78** keeps its interest wording, which matches item h, and adds the C ≥ A and no-refund limits.
- `PILA Spec!M46/M47/M48/G85`, `File Structure!B32/B38`, `Field Options!D139`: consistent; no change.

---

## NOT LOCATED / outside this map
1. **Vacation compensated in cash or paid on termination in campo 45/95:** not settled by AT2 v30 or by the Ley 21 art. 17 text. UGPP p.23 says yes. No change proposed; Wallisson decides (see A.3).
2. **ICBF base (Ley 89/1988 art. 1):** not read.
3. **Circular 009/2011** (refund procedure): not opened. It is referred to only through AT2 and not cited in the spec.
4. **`File Structure!B51`:** "rejected contributor records [...] re-filed on a correction return (type N)". AT2 type N covers corrections to a paid planilla inicial. Nothing read here settles which planilla type re-files a rejected record, so there is no change and this goes to OPEN-POINTS.
5. **`Payroll Scope Summary!C49`:** type M in AT2 p.37 is worded for "periodos vencidos, anteriores a periodo salud marzo de 2014". Whether M is still the late-payment route for a current private employer was not assessed. The proposed C49 only fixes the campo 9/10 point.
6. **`PILA Spec!M112`:** the loose phrase "under their own AT2 v30 rules" was left as is (see A).

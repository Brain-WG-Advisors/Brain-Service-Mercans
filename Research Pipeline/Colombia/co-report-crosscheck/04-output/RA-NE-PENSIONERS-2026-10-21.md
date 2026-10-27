# RA-NE-PENSIONERS — Employer-paid pensioners in the DIAN electronic payroll support document (DSPNE)

- **Date:** 2026-10-21
- **Country / instrument:** Colombia — Documento Soporte de Pago de Nómina Electrónica (DSPNE), Res. DIAN 000227/2025 Title 1.5.3 (ex Res. DIAN 000013/2021)
- **Question:** Res. 000227/2025 brings "los pensionados a cargo del empleador" into the DSPNE, but Anexo Técnico v1.0 table 5.5.3 has no pensioner code. How does DIAN tell an employer to report a pensioner whose pension it pays (TipoTrabajador / SubTipoTrabajador / TipoContrato; which Devengados element carries the mesada; how health, FSP and withholding are reported; whether FechaIngreso / Sueldo apply)? Is there a newer Anexo than v1.0?
- **Sources:** primary DIAN only (Res. 000227/2025, Anexo Técnico v1.0 + XSD v1.0.6, DIAN micrositio, normograma.dian.gov.co doctrine, DIAN Abecé and free-solution manual). Blogs and vendors were used only as leads.

## Bottom line

1. **Scope is confirmed. The technical instruction is NOT LOCATED.** DIAN's resolution and doctrine say several times that pensioners paid by the employer belong in the DSPNE. No DIAN source we found (Anexo v1.0, XSD v1.0.6, the micrositio, the Abecé, the free-solution manual, or 9 oficios/conceptos on normograma) explains **how** to code a pensioner. Nothing official covers TipoTrabajador/SubTipoTrabajador/TipoContrato for a pensioner, the Devengados element for the mesada, or how FechaIngreso/Sueldo/DiasTrabajados apply.
2. **The XSD forces fields that were designed for employees.** These are mandatory for every document: `FechaIngreso`, `TipoTrabajador`, `SubTipoTrabajador`, `TipoContrato`, `Sueldo`, `Devengados/Basico` (`DiasTrabajados` + `SueldoTrabajado`), `Deducciones/Salud` and `Deducciones/FondoPension`. Any pensioner mapping is therefore a convention, with no DIAN text behind it.
3. **There is no newer Anexo than v1.0.** On 2026-10-21 the micrositio still publishes only `Caja-de-Herramientas-Nomina-Electronica-V1-0.zip`. Its SHA-256 matches our local copy byte for byte. Res. 000227/2025 itself (23-09-2025) adopts "versión 1.0".

## Findings

### F1 — Pensioners are in scope (CONFIRMED, primary)

Res. DIAN 000227 de 23-09-2025, "Resolución Única en Materia Tributaria, Aduanera y Cambiaria". Local copy: `frentes/pipeline/mercans-pipeline/CO-compliance/00-official-sources/pdfs/Resolución 000227 de 23-09-2025.pdf`. Page numbers below are the printed "PÁGINA N DE 449".

| Article | Page | Quote |
|---|---|---|
| 1.5.3.1.1 num. 5 | 243 | "5. Beneficiario del pago: Se entiende como beneficiario del pago, a las personas naturales vinculadas mediante una relación laboral o legal y reglamentaria y los pensionados a cargo del empleador, en relación con estas actividades." |
| 1.5.3.1.1 num. 15 | 244 | "…que realizan pagos o abonos en cuenta que se derivan de una vinculación por una relación laboral o legal y reglamentaria y por pagos a los pensionados a su cargo, que requieran soportar los costos y deducciones…" |
| 1.5.3.2.1 | 245 | "…que se desprenden de una relación laboral o legal y reglamentaria y los pensionados a cargo del empleador, y que está compuesto por los valores devengados de nómina, los valores deducidos de nómina y el valor total diferencia de los mismos." |
| 1.5.3.2.2 | 245–246 | "…derivados de la relación laboral o legal y reglamentaria o de pensiones, correspondiente a las liquidaciones de nómina realizadas en el mes inmediatamente anterior…" |
| 1.5.3.2.3 | 246 | "…y por pagos a los pensionados a cargo del empleador, que requieran soportar los costos y deducciones…" Followed by: "Lo anterior cumpliendo las condiciones, términos y mecanismos técnicos y tecnológicos, establecidos en el 'Anexo técnico documento soporte de pago de Nómina Electrónica'…" |

Every one of these carries the source tag "(Artículo N, Resolución 13 de 2021)". The pensioner wording therefore dates from 2021 and was in force when Anexo v1.0 was adopted. The 2025 compilation did not add it.

DIAN doctrine repeats the scope and adds nothing technical:

- **Oficio 901476 de 17-02-2022** (100208192-213, addressed to "Sujetos obligados"; published 09-05-2022). "…el documento soporte de pago de nómina electrónica se origina por los pagos o abonos en cuenta relacionados con la nómina, entendidos ellos como aquellos que se desprenden de una relación laboral o legal y reglamentaria, así como por los pagos a pensionados a cargo del empleador." It also says that amounts recognised annually, such as prestaciones, "deberán incluirse por el total reconocido (por pago o abono en cuenta, lo que suceda primero)". https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_901476_2022.htm
- **Oficio 901867 de 09-03-2022** (100208192-298); https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_901867_2022.htm
- **Oficio 902370 de 23-03-2022**; https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_902370_2022.htm
- **Oficio/Concepto 912416 de 06-10-2021** (100208192-253). "…se derivan de los pagos que se realizan en virtud de una relación laboral o legal y reglamentaria y de los pagos a los pensionados a cargo del empleador." https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_912416_2021.htm
- **Oficio 914809 de 03-12-2021** (100208192-494); https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_914809_2021.htm
- **Res. DIAN 0028 de 28-02-2022**, art. 1. "…o que tienen pensionados a cargo, que requieran soportar los costos y deducciones…" https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0028_2022.htm
- **DIAN Abecé DSPNE**, p. 2. "…se deriva de los pagos o abonos en cuenta relacionados con la nómina que se desprenden de una relación laboral, de pensiones o legal y reglamentaria." https://www.dian.gov.co/impuestos/factura-electronica/Documents/Abece-documento-soporte-de-pago-nomina-electronica.pdf

### F2 — Anexo v1.0 has no pensioner code in TipoTrabajador or TipoContrato (CONFIRMED, primary)

Anexo Técnico Documento Soporte de Pago de Nómina Electrónica – Versión 1.0 (Res. 000013 de 11-02-2021). Local copy: `.../00-official-sources/pdfs/AnexoTecnico-NominaElectronica-V1.0.pdf`.

- **p. 179, 5.5.2 TipoContrato:** "1 Termino Fijo / 2 Término Indefinido / 3 Obra o Labor / 4 Aprendizaje / 5 Prácticas o Pasantías". No pension code.
- **p. 179, 5.5.3 TipoTrabajador:** codes 01, 02, 04, 12, 18, 19, 21, 22, 23, 30, 31, 47, 51, 54 ("Pre pensionado de entidad en liquidación."), 56 ("Pre pensionado con aporte voluntario a salud") and 58. None of them covers a retiree receiving an employer-paid pension.
- **p. 179, 5.5.4 SubTipoTrabajador:** "00 No Aplica / 01 Dependiente pensionado por vejez activo". Code 01 is a pensioner **who still works** as an employee, not a pensioner paid by the employer.
- **p. 21, TipoTrabajador (NIE):** "Corresponde a la clasificación de PILA para conocer en que calidad se realizan las cotizaciones a la seguridad social. Se debe colocar el Codigo de la tabla 5.5.3". The field mirrors the PILA *cotizante* type for **activos**. Its description reads "Código del tipo de trabajador del Ministerio de salud. Aportes a Seguridad Social de Activos." Employer-paid pensioners are reported in PILA on a different planilla (PILA Anexo Técnico 3, pensionados). The DSPNE has no equivalent table.

### F3 — Mandatory fields in XSD v1.0.6 (CONFIRMED, mechanical read)

File: `NominaIndividualElectronicaXSDV1.0.6.xsd` (Caja V1-0).

- `Periodo/@FechaIngreso`: `type="xsd:date" use="required"` (l. 50–52).
- `Trabajador/@TipoTrabajador` and `@SubTipoTrabajador`: `xsd:integer`, `use="required"`, **no enumeration**, so the schema accepts any integer (l. 212–217). Only the Anexo validation rule checks the code ("Se debe colocar el Codigo de la tabla 5.5.3", rule list p. 187).
- `Trabajador/@TipoContrato` and `@Sueldo`: required (l. 253–258). Anexo validation p. 188: "Se debe colocar el Sueldo Base que el Trabajdor tiene en la empresa".
- `Devengados/Basico`: `minOccurs="1"`, with `DiasTrabajados` and `SueldoTrabajado` required (l. 298–307). Anexo p. 25 defines SueldoTrabajado as "…contraprestación por el trabajo realizado…".
- `Deducciones/Salud` and `Deducciones/FondoPension`: `minOccurs="1"`, with Porcentaje and Deduccion required (l. 844–858). `FondoSP` is `minOccurs="0"` (l. 868). Anexo p. 44 (NIE163, Salud) ties the field to the employee rate: "…La cotización por salud que corresponde al 12.5% … la empresa aporta el 8.5%, y el empleado debe aportar el 4% restante."
- `Deducciones/RetencionFuente`: optional decimal (XSD l. 982; NIE rule list p. 197).
- `Devengados/OtrosConceptos/OtroConcepto` (0-N, with `DescripcionConcepto`, `ConceptoS` and `ConceptoNS`; Anexo p. 38–39) is the only free-text devengado. Its definition is about remuneration "como contraprestación directa del servicio" (S) or "por mera liberalidad … para desempeñar a cabalidad sus funciones" (NS). Neither fits a mesada pensional, and DIAN has not said to use it for one.

### F4 — No newer Anexo version (CONFIRMED, primary)

- **Micrositio, "Documentación Técnica: Soporte de Pago Nomina Electrónica"**, fetched 2026-10-21: https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/documentacion-tecnica-soporte-de-pago-nomina-electronica/. It lists only "Resolución 000013 del 2021 y Anexo Técnico" and "Caja de herramientas…". The only package linked is `https://www.dian.gov.co/impuestos/factura-electronica/Documents/Caja-de-Herramientas-Nomina-Electronica-V1-0.zip`. Downloaded today: SHA-256 `0b2d0f8405d144989e5e36bdb50bb04a57c564dc1217971f43f98861c50a5ee3`, 5,528,509 bytes. This is **identical** to our local `integration-sources/dian-ne/Caja-de-Herramientas-Nomina-Electronica-V1-0.zip` (SHA256SUMS.txt).
- **Res. 000227/2025, art. 1.5.3.7.1 parágrafo, p. 253:** "Por medio de la presente resolución se adopta el 'Anexo técnico documento soporte de pago de Nómina Electrónica' versión 1.0, el cual forma parte integral de la presente resolución." Art. 1.5.3.7.2 says annexes and their changes are published on the micrositio, and the micrositio shows only V1-0.
- **Res. 000238 de 15-12-2025** only replaces art. 1.2.1 (UVT 2026). It does not touch Title 1.5.3.
- A vendor page (docs.matias-api.com) claims "Nómina Electrónica v3.0, Resolución 0000040/2024". The page returned HTTP 500 and normograma has no `resolucion_dian_0040_2024`. It is **not corroborated** and conflicts with F4. Treat it as noise.

### F5 — Pensioner coding instruction: NOT LOCATED

We searched for an official answer and found none in any of these:

- Anexo v1.0: the full text was searched for "pension" and "pensionad". The only hits are AltoRiesgoPension, FondoPension, FondoSP, PensionVoluntaria and codes 54/56/subtipo 01.
- XSD v1.0.6 and the Ejemplificaciones XML (v1.0.2).
- Micrositio pages: documentación técnica; lo que deberías saber; soporte de pago; preguntas y respuestas de proveedores tecnológicos. The last one has FE content only, with no DSPNE FAQ.
- The DIAN Abecé.
- The DIAN free-solution manual "Paso a paso Solución Gratuita Nómina Electrónica" (both the dian.gov.co and storagecdndian versions). "pensionad" does not appear.
- Normograma doctrine: Oficios 908125/2021, 912416/2021, 914809/2021, 915463/2021, 900657/2022, 900734/2022, 901476/2022, 901867/2022, 902370/2022 and Concepto 3932/2023. All of them restate the scope; none of them codes a pensioner.

Closest analogue, which does **not** answer the question: **Oficio 915463 de 17-12-2021** (100208192-589). DIAN was asked "¿qué código debe utilizarse en el anexo técnico…?" for apprentices. It answered on scope instead: "…no deberán ser soportados con el documento soporte de pago de nómina electrónica." It did not give a code. https://normograma.dian.gov.co/dian/compilacion/docs/oficio_dian_915463_2021.htm

Leads only (vendors, not authority): minomina.com, "¿Cuál es el subtipo de trabajador que se debe asociar a un pensionado por invalidez?", and alegra.com on FSP. These show that vendors apply their own conventions. They are **not** to be cited.

## What would close it

1. **Derecho de petición / consulta to the DIAN Subdirección de Normativa y Doctrina** (or through PQSR to the Subdirección de Factura Electrónica y Soluciones Operativas). Ask, for a pensioner paid directly by the employer: (a) the TipoTrabajador/SubTipoTrabajador/TipoContrato codes; (b) the Devengados element for the mesada, mesada 13/14 included; (c) FechaIngreso, Sueldo, Basico/DiasTrabajados and SueldoTrabajado; (d) Salud (pensioner rate) and FondoPension when there is no contribution, i.e. Porcentaje/Deduccion = 0; (e) FSP on mesadas; (f) RetencionFuente on pensions (ET art. 206 num. 5). The answer would come back as an oficio published on normograma.
2. **Test it ourselves in the DIAN habilitación environment.** Send a test DSPNE with TipoTrabajador 01, SubTipo 00, TipoContrato 2, FechaIngreso = pension start date, mesada in Basico or OtroConcepto, and FondoPension 0/0, and see whether it is rejected or returns notifications. This shows only what the validator accepts; it does not tell us the right answer.
3. **Monitor the micrositio** for any change to the Caja beyond V1-0 (hash above) and normograma for any oficio on "pensionados nómina electrónica".

Until one of these is done, the DD/Spec should mark the pensioner mapping as `⚠️ no DIAN instruction — convention`, not as a DIAN rule.

## Files saved (raw/docs/oficiais/CO/, prefix 2026-10-21-)

DIAN-Abece-DSPNE.pdf; DIAN-micrositio-documentacion-tecnica-nomina.html; DIAN-micrositio-soporte-pago-nomina.html; DIAN-Oficio-{900657,901476,901867,902370}-2022-normograma.htm; DIAN-Oficio-{908125,912416,914809,915463}-2021-normograma.htm; Res-DIAN-0028-2022-normograma.htm; DIAN-Paso-a-paso-Solucion-Gratuita-Nomina-v-dian.gov.co.pdf; DIAN-Paso-a-paso-Solucion-Gratuita-Nomina-v-micrositio.pdf. The Caja zip was not saved again because it is hash-identical to `integration-sources/dian-ne/`.

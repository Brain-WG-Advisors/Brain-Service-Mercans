# 06 — Mandatory Payslip Content: Colombia (CO), fiscal year 2026

> **Status of this file (recompiled 28 Oct 2026).** The Payslip Generator has no new version (CO
> Compliance Payslip Generator **v1.1 DRAFT**, 24 Sep 2026, no Version Control), so the content below is the
> payslip reference of the 5 Oct 2026 skill, kept unchanged except for the citation updates in this note.
>
> **Citations of Resolución DIAN 000013 de 2021 (hub item F6-20261027-CO-C19 — pending validation).**
> Res. 000013/2021 is now compiled in **Resolución DIAN 000227 de 2025** (Resolución Única), arts.
> 1.5.3.1.1 to 1.5.3.9.8; the Spanish text quoted below is the text of the former articles. CCG v1.4
> (Modules 1.1 and 10.3) gives the compiled numbers **art. 1.5.3.3.1** (former art. 5, content),
> **art. 1.5.3.8.3** (former art. 24, graphical representation) and **art. 1.5.3.8.5** (former art. 26,
> language and currency); the third-party rule (former art. 22) is **art. 1.5.3.8.1** (SIR v1.1 mapping).
> The correspondence for the former arts. 5, 24 and 26 is **not yet confirmed** against the official
> concordance — cite "Res. DIAN 000227 de 2025 art. 1.5.3.3.1 (formerly Res. 000013/2021 art. 5)" and say it
> is pending validation. The former arts. 15, 17, 20 and 23 have no confirmed compiled number.
>
> **Conflict found at recompilation (not resolved here).** The 13-item list in §2.1 below is the verbatim
> Spanish text of the former art. 5. CCG v1.4 Module 10.3 prints a different English 13-item list (it adds
> "payment or credit date", "payment or credit period", "country, department and municipality of origin",
> and omits "denominado expresamente", "firma digital" and the technology provider). The two lists do not
> match; until the article is re-read in Res. 000227/2025, quote the verbatim list below and flag the
> divergence.
>
> The Payslip Generator v1.1 DRAFT still cites Res. 000013/2021 (sheets `Colombia (EN)`/`(ES)` A78); its
> A83 note follows CCG v1.4 on the SMMLV instrument (Decree 1469/2025 back in force after the 9 Jul 2026
> revocation). See SKILL.md open items C19 and C21.


## 1. The headline finding: Colombia has NO statutory payslip-content article in its labour code

The Código Sustantivo del Trabajo contains **no provision prescribing the content of a pay statement**.
This was **grep-tested** against the full consolidated CST (Senate compilation, last updated 15 August
2026, ~365 KB of text covering all twelve chapters):

| Search term | Hits in the CST |
|---|---|
| `desprendible` | **0** |
| `comprobante de pago` | **0** |
| `colilla` | **0** |
| `volante de pago` | **0** |
| `recibo de pago` | **0** |
| `constancia de pago` | **0** |
| `detalle de la liquidación` | **0** |

The commonly used Colombian words for a payslip — *desprendible de pago*, *comprobante de nómina*,
*colilla de pago* — appear **nowhere** in the labour code. **Ley 2466 de 2025**, the 2025 labour reform,
did not add one either: its art. 15 rewrote CST art. 57 (*obligaciones especiales del empleador*) and
added five new numerals, none of which mentions a pay statement.

**What the CST does regulate** is the *mechanics* of paying salary, not its documentation:

| Article | Rule |
|---|---|
| **CST art. 134 num. 1** | *"El salario en dinero debe pagarse por **períodos iguales y vencidos, en moneda legal**. El período de pago para los **jornales** no puede ser mayor de **una semana**, y para **sueldos** no mayor de **un mes**."* |
| **CST art. 134 num. 2** | *"El pago del **trabajo suplementario o de horas extras** y el del **recargo por trabajo nocturno** debe efectuarse **junto con el salario ordinario del período en que se han causado, o a más tardar con el salario del período siguiente**."* |
| **CST art. 135** | Salary stipulated in foreign currency: the employee may demand payment in Colombian pesos at the official rate of the day payment is due |
| **CST art. 136** | Payment in goods, tokens or similar means is prohibited, except for the part supplied as lodging, clothing and food for the employee and family |
| **CST art. 138 num. 1** | *"Salvo convenio por escrito, el pago debe efectuarse **en el lugar donde el trabajador presta sus servicios**, durante el trabajo o inmediatamente después de que este cese."* |
| **CST art. 138 num. 2** | Payment made in vice centres, recreation venues, or shops selling goods or alcohol is prohibited and treated as not made |
| **CST art. 139** | *"El salario se paga **directamente al trabajador** o a la persona que él autorice **por escrito**."* |
| **CST art. 133** | *jornal* = salary stipulated per day; *sueldo* = stipulated for longer periods |
| **CST art. 143** (Ley 1496 de 2011 art. 7) | Equal pay for work of equal value; no differences by age, gender, sex, nationality, race, religion, political opinion or union activity; **any pay differential is presumed unjustified until the employer proves objective differentiating factors** |
| **CST art. 148** | Fixing the minimum wage **automatically amends** any employment contract stipulating less |
| **CST art. 57 num. 7** | On request at contract expiry, a certificate of **time of service, nature of the work and salary earned** |

**CST art. 134 num. 2 is the one payslip-adjacent obligation with a hard deadline:** overtime and the
night surcharge must be paid with the ordinary salary of the period in which they arose, or **at the
latest with the following period's salary**. A one-period lag is lawful; a two-period lag is not.

---

## 2. The de-facto content mandate: the DIAN nómina electrónica

Because the labour code is silent, the operative itemisation requirement in Colombia is **tax law**, not
labour law. **Resolución DIAN 000227 de 2025 art. 1.5.3.3.1** (formerly Resolución DIAN 000013 de 11 de
febrero de 2021 art. 5) prescribes the minimum content of the *Documento Soporte de Pago de Nómina
Electrónica*, and **art. 1.5.3.8.3** (formerly art. 24) makes the printable/digital
version of that document — the thing an employee actually receives — carry that same content.

### 2.1 Mandatory content — Res. 000227/2025 art. 1.5.3.3.1 (formerly Res. 000013/2021 art. 5; text VERIFIED verbatim on the former article)

> *"El documento soporte de pago de nómina electrónica deberá contener como mínimo la siguiente
> información:*
> *1. Estar **denominado expresamente** como documento soporte de pago de nómina electrónica.*
> *2. **Apellidos y nombre o razón social y Número de Identificación Tributaria - NIT** del sujeto de que
> trata el artículo 4 de esta resolución.*
> *3. **Apellidos y nombre(s) y Número de Identificación del beneficiario** del pago.*
> *4. El **código único** de documento soporte de pago de nómina electrónica - **CUNE**.*
> *5. Llevar un **número** que corresponda a un sistema interno de **numeración consecutiva**, asignado
> por el sujeto de que trata el artículo 4 de esta resolución.*
> *6. **Contenido y valores de los conceptos que corresponden al valor devengado de nómina**; conforme a
> lo establecido en el «Anexo técnico documento soporte de pago de NÓMINA ELECTRÓNICA».*
> *7. **Contenido y valores de los conceptos que corresponden a los valores deducidos de nómina**;
> conforme a lo establecido en el «Anexo técnico …».*
> *8. El **valor total diferencia**, que corresponde a la diferencia del valor total devengado de nómina
> menos el valor total deducido de nómina.*
> *9. El contenido del «Anexo técnico …» establecido en el artículo 20 de esta resolución, en relación
> con la información y contenido de que trata el presente artículo.*
> *10. El **medio de pago**, que el sujeto de que trata el artículo 4 de esta resolución, utiliza para
> hacer la entrega de la contraprestación económica de los servicios prestados por el beneficiario del
> pago, conforme a lo establecido en el «Anexo técnico …».*
> *11. **Fecha y hora de generación.***
> *12. La **firma digital** del sujeto de que trata el artículo 4 de esta resolución, de acuerdo con las
> normas vigentes y la política de firma establecida por la … DIAN, al momento de la generación como
> elemento para garantizar **autenticidad, integridad y no repudio** del documento de nómina
> electrónica.*
> *13. **Apellidos y nombre o razón social y Número de Identificación Tributaria -NIT, del proveedor de
> soluciones tecnológicas, y la identificación del software**."*

### 2.2 The graphical representation — Res. 000227/2025 art. 1.5.3.8.3 (formerly Res. 000013/2021 art. 24; text VERIFIED verbatim on the former article)

> *"Los sujetos obligados …, **si lo requieren, podrán expedir representaciones gráficas** del documento
> soporte de pago de nómina electrónica y las notas de ajuste …, en formato **digital o impreso**, para lo
> cual, deberán contener **como mínimo la información establecida en los artículos 5 o 17** de la
> presente resolución según corresponda, e **incluir el Código de respuesta rápida -Código QR-**, a través
> del cual se podrá acceder a la consulta de los documentos validados, de conformidad con las
> condiciones, términos y mecanismos técnicos y tecnológicos establecidos por la … DIAN, en el «Anexo
> Técnico de la factura electrónica de venta»."*

**Critical reading:** issuing a graphical representation is **permissive** (*"si lo requieren, podrán"*),
**not** mandatory. Colombia therefore has:

- a **mandatory** electronic document, filed to the tax authority, containing a prescribed itemisation;
- **no** statutory obligation to hand the employee a payslip at all; but
- if the employer does issue one — as essentially every Colombian employer does — it must carry the
  art. 5 content **plus the QR code**.

The practical answer to "what must a Colombian payslip contain" is therefore: **the art. 5 list, plus the
QR, plus whatever the employer chooses to add.**

### 2.3 QR code requirements — Anexo Técnico §13.1 (VERIFIED verbatim)

> *"La representación gráfica debe incluir el código QR **en todas las páginas** de los formatos digitales
> y de la impresión en papel del Documento Soporte de Pago de Nómina Electrónica y Nota de Ajuste …"*

URL format:
```
Producción:     https://catalogo-vpfe.dian.gov.co/document/searchqr?documentkey=<CUNE>
Habilitación:   https://catalogo-vpfe-hab.dian.gov.co/document/searchqr?documentkey=<CUNE>
```

The QR must encode the following data set:

| Token | Content and format |
|---|---|
| `NumNIE` | Document number |
| `FecNIE` | Document date |
| `HorNIE` | Document time **with GMT offset** |
| `NitNIE` | Issuer NIT, **no dots, no hyphens** |
| `DocEmp` | Employee identification number, **no dots, no hyphens** |
| `ValDev` | Total devengado — **decimal point, two decimals, no thousands separator, no peso symbol** |
| `ValDed` | Total deducido — same format |
| `ValTol` | Document total — same format |
| `CUNE` | The 96-character SHA-384 hex |
| `QRCode` | The URL made available by DIAN |

Worked example from the annex:
```
NumNIE: 323200000129
FecNIE: 2019-16-01
HorNIE: 10:53:10-05:00
NitNIE: 700085371
DocEmp: 800199436
ValDev: 1500000.00
ValDed:  285000.00
ValTol: 1785000.00
CUNE:   e5bac48e354bc907bccff0ea7d45fbf784f0a8e7243b58337361e1fbd430489d
```
*(Note: the annex's own example prints `FecNIE: 2019-16-01`, which is not a valid date in any ordering —
another editorial defect in the annex's worked examples. See `07-qa-report.md` item Q-9.)*

**Minimum QR size — Anexo Técnico §13.1** (VERIFIED verbatim):
> *"**Tamaño:** El tamaño mínimo que debe tener el código bidimensional QR es de **2cm** para facilitar la
> lectura por los diferentes dispositivos."*

### 2.4 Legal status of the paper/PDF payslip — Anexo Técnico §13.1 (VERIFIED verbatim)

> *"La representación gráfica **siempre será 'una representación, una imagen'** de la información
> consignada en el formato XML de los perfiles de la DIAN. Esto significa que **el documento electrónico
> siempre será el que tenga valor legal** para las autoridades nacionales. Si cualquier persona requiere
> validar la autenticidad de una representación gráfica, entonces deberá acceder al sitio web que la DIAN
> disponga para ello…"*

And on format freedom:
> *"La representación gráfica puede ser **diseñada de acuerdo con las necesidades del Emisor** …; como la
> generación está en formato XML, entonces **cualquier herramienta informática de conversión de este
> formato a .pdf, .docx, u otros formatos digitales podrá ser utilizada**, en todo caso deberá tener el
> código bidimensional QR tal como ya se indicó."*

**Engine consequence:** the XML is the legal instrument; the payslip is a rendering of it. Any figure on
the payslip that does not reconcile to the validated XML is, legally, wrong — including rounding
differences, which is exactly why the XML carries the explicit `Redondeo` element.

---

## 3. Language

**Res. 000227/2025 art. 1.5.3.8.5** (formerly Res. 000013/2021 art. 26; text VERIFIED verbatim on the former article):
> *"**Idioma y moneda** en el contenido de la nómina electrónica: Se debe utilizar el **idioma español** y
> el **peso colombiano** en la generación del documento soporte de pago de nómina electrónica y las notas
> de ajuste …, **sin perjuicio** de que además de expresar el respectivo valor en pesos colombianos pueda
> expresarse en **otra moneda y en un idioma distinto al español**."*

- **Spanish and COP are mandatory.**
- A second language and a second currency are permitted **in addition**, never instead.
- Where a second currency is shown, the XML must carry `InformacionGeneral/@TRM` (the representative
  market rate) to convert to pesos.
- The XSD also carries `LugarGeneracionXML/@Idioma` (`use="required"`), coded per **ISO 639**
  (Anexo §5.3.1) — set to Spanish for a Colombian payroll.

So a bilingual Spanish/English payslip is compliant; an English-only payslip is not.

---

## 4. Recommended payslip layout

The following layout satisfies Res. 000227/2025 arts. 1.5.3.3.1 and 1.5.3.8.3 (formerly Res. 000013/2021 arts. 5 and 24), makes the three rounding regimes
auditable, and surfaces the 2026-specific rules that an auditor will look for. Items marked **[art. 5]**
are legally required if a graphical representation is issued; items marked **[good practice]** are not
required by any Colombian rule but are needed for the employee to reconcile the figure.

### Header — **[art. 5 items 1, 2, 3, 4, 5, 11, 13]**

```
DOCUMENTO SOPORTE DE PAGO DE NÓMINA ELECTRÓNICA        [art. 5 item 1 - exact wording]
Número: <Prefijo><Consecutivo>                          [item 5]
CUNE: <96-char SHA-384>                                 [item 4]
Fecha y hora de generación: AAAA-MM-DD HH:MM:SS-05:00   [item 11]
                                                        [QR code - art. 24, EVERY page]
EMPLEADOR                            TRABAJADOR
Razón social / Nombre               Apellidos y nombres        [item 3]
NIT: <9-10 dígitos>  DV: <1>        Tipo doc: <13/22/...>      [item 2 / item 3]
Dirección, Municipio, Departamento  Documento: <número>
                                     Cargo, Centro de trabajo
PROVEEDOR TECNOLÓGICO                                          [item 13]
Razón social · NIT · DV · SoftwareID
```

### Period and contract block — **[good practice; sourced from XSD required attributes]**

```
Periodo de liquidación: AAAA-MM-DD a AAAA-MM-DD
Periodo de nómina: Mensual (5)          Fecha de ingreso: AAAA-MM-DD
Tipo de contrato: Término indefinido (2) Fecha de retiro: —
Días trabajados: 30                     Salario integral: No
Sueldo contractual: $ 8.000.000         Alto riesgo pensión: No
```

### Devengados — **[art. 5 item 6]** — each concept on its own line, per the annex taxonomy

Figures below are for an **August 2026** payroll on a monthly salary of **$8.000.000** — so the ordinary
hour is `8.000.000 ÷ 210 = 38.095,24` (divisor **210** from 15 July 2026) and the *día de descanso
obligatorio* surcharge is **90%** (from 1 July 2026).

```
CONCEPTO                                            CANT.   %        VALOR
Salario básico (30 días)                               30          8.000.000,00
Auxilio de transporte (salario > 2 SMMLV)                                  0,00
Hora extra diurna              (38.095,24 x 1,25)     4,0  25,00     190.476,19
Recargo nocturno               (38.095,24 x 0,35)     6,0  35,00      80.000,00
Recargo día de descanso obligatorio (x 0,90)          8,0  90,00     274.285,71
Comisiones                                                                 0,00
Prima de servicios                                                         0,00
Cesantías / Intereses a las cesantías                                      0,00
Vacaciones                                                                 0,00
Incapacidad común (días 1-2, a cargo del empleador)                        0,00
Licencia de maternidad / paternidad                                        0,00
Bonificación (salarial / no salarial)                                      0,00
Auxilio (salarial / no salarial)                                           0,00
Dotación                                                                   0,00
                                                 TOTAL DEVENGADO   8.544.761,90
```

**Do not bundle.** The annex gives each concept its own XML element with its own attributes; a payslip
line that merges, say, all overtime types into "horas extras" cannot be reconciled to the validated XML
and defeats art. 5 item 6 (*"Contenido y valores de los conceptos"*). For hour-based lines, show
**quantity, percentage and amount** — the XSD makes all three `use="required"`.

### Deducciones — **[art. 5 item 7]**

IBC = 8.544.761,90 rounded **up** to the peso = **8.544.762**; each contribution rounded **up** to the
nearest 100.

```
CONCEPTO                                          %          VALOR
Salud (empleado)                                4,00       341.800,00
Fondo de pensión (empleado)                     4,00       341.800,00
Fondo de solidaridad pensional - solidaridad    1,00        85.500,00
Fondo de solidaridad pensional - subsistencia   0,00             0,00
Retención en la fuente                                     162.681,12
Cuota sindical                                                   0,00
Libranza <descripción>                                           0,00
Cooperativa / Fondo de empleados                                 0,00
Embargo fiscal                                                   0,00
Plan complementario de salud                                     0,00
Pensión voluntaria / AFC / AVC                                   0,00
Anticipos / Deuda                                                0,00
                                             TOTAL DEDUCIDO  931.781,12
```

*Retención derivation:* INCRNGO = 341.800 + 341.800 + 85.500 = 769.100 → subtotal
8.544.761,90 − 769.100 = 7.775.661,90 → 25% renta exenta = 1.943.915,48 (below both the 40% limit of
3.110.264,76 and the monthly 790/12 UVT cap of 3.447.955) → base gravable **5.831.746,42 = 111,3481 UVT**
→ band > 95 to 150 UVT at 19% → (5.831.746,42 − 4.975.530) × 19% = **162.681,12**.

**Two lines that are commonly and wrongly merged:**
1. **`FondoSP` solidaridad and subsistencia are separate.** The XSD gives them four attributes on one
   element (`@Porcentaje`/`@DeduccionSP` and `@PorcentajeSub`/`@DeduccionSub`) precisely because
   Ley 100 art. 20 creates two sub-accounts. Show both, even when subsistencia is zero.
2. **The FSP is not part of the pension line.** It is an additional employee-borne surcharge on the same
   base, not a component of the 4%.

### Totals — **[art. 5 item 8]**

```
TOTAL DEVENGADO                         8.544.761,90
TOTAL DEDUCIDO                            931.781,12
REDONDEO                                        0,00     <- the XML Redondeo element
NETO A PAGAR (valor total diferencia)   7.612.980,78
```

Art. 5 item 8 requires the **valor total diferencia** explicitly = total devengado − total deducido.

### Payment method — **[art. 5 item 10]**

```
Forma de pago: Contado (1)
Medio de pago: Transferencia crédito bancario (45)
Banco: <nombre>   Tipo de cuenta: Ahorros   Cuenta: <número>
Fecha(s) de pago: AAAA-MM-DD
```

### Employer contributions — **[good practice, NOT required]**

The employer's own contributions (pensión 12%, salud 8,5%, ARL, CCF, SENA, ICBF) have **no element in
the nómina-electrónica XSD** and are **not** part of the art. 5 content. Showing them is informative but
must be clearly labelled as employer cost, not as an employee deduction, or the payslip becomes
misleading. If shown, show the **exoneration** explicitly:

```
APORTES A CARGO DEL EMPLEADOR (informativo - no se deduce al trabajador)
Pensión 12,00%                                    1.025.400
Salud    8,50%   EXONERADO - Art. 114-1 E.T.              0    (devengado < 10 SMMLV)
ARL clase I 0,522%                                   44.700
CCF      4,00%                                      341.800    (nunca exonerado)
SENA     2,00%   EXONERADO - Art. 114-1 E.T.              0
ICBF     3,00%   EXONERADO - Art. 114-1 E.T.              0
```

*(On the same IBC of 8.544.762, each rounded up to the nearest 100. CCF is computed on the Ley 21 de 1982
art. 17 nómina de salarios, which here coincides with the IBC because all the period's payments are
salary-constituting and the figure is well under the 25-SMMLV IBC ceiling.)*

### Footer — **[art. 5 item 12 + art. 24]**

```
Documento validado por la DIAN - <fecha/hora de la respuesta>
Firma digital XAdES-EPES del sujeto obligado
El documento electrónico (XML) es el que tiene valor legal.
Verifique en: catalogo-vpfe.dian.gov.co  [QR]
```

---

## 5. Formatting and rounding conventions on the payslip

### 5.1 Number format

| Convention | Value |
|---|---|
| Decimal separator on the printed payslip | **comma** (`,`) — Colombian convention |
| Thousands separator on the printed payslip | **dot** (`.`) |
| Decimal separator **in the XML** | **dot** (`.`) — `xsd:decimal` |
| Thousands separator in the XML | **none** |
| Currency symbol in the XML | **none** |
| Decimals in the XML | **two** |
| Currency shown on the payslip | **COP** (peso symbol `$` is conventional) |

So `8.000.000,00` on the printed payslip is `8000000.00` in the XML. The **CUNE** inputs must use the XML
format (*"con punto decimal, con decimales truncados a dos (2) dígitos, sin separadores de miles, ni
símbolo pesos"*) — a locale-formatted string will produce a wrong hash.

### 5.2 Rounding — three regimes, and the payslip must not blend them

| Where | Rule | Source |
|---|---|---|
| **Social-security and parafiscal amounts (PILA)** | IBC **up** to the nearest whole peso; contributions and interest **up** to the nearest **multiple of 100** | Decreto 780/2016 art. 3.2.1.5, substituted by Decreto 1990/2016 art. 1 |
| **Every monetary value in the XML** | **round-half-to-even** (banker's rounding), tolerance **±2,00**, residual reported in `Redondeo` | Anexo Técnico §1.1.1.1, NTC 3711 / JIS Z 8401 |
| **Values on DIAN return forms (Form 350)** | **nearest multiple of 1.000** (below 500 down, 500 and above up) | ET art. 577 |

**Practical rule for the payslip:** print the **PILA-rounded** figure for salud, pensión and FSP (because
that is the amount actually remitted and the amount the employee can verify against their PILA
certificate), print the **exact computed** retención en la fuente to two decimals, and let the
`Redondeo` line absorb any residual so that
`TOTAL DEVENGADO − TOTAL DEDUCIDO ± REDONDEO = NETO` holds exactly.

### 5.3 Dates and times

| Field | Format |
|---|---|
| Dates in the XML | `xsd:date` → `AAAA-MM-DD` |
| Times in the XML | `xsd:time` → `HH:MM:SS-05:00` (Colombia is UTC−05:00 year-round; **no DST**) |
| `HoraGen` in the CUNE | **must include the GMT offset** |
| Hour blocks | `@HoraInicio` / `@HoraFin` are `xsd:dateTime` — date **and** time, not time alone |

---

## 6. Retention and delivery

| Obligation | Rule |
|---|---|
| Retain the XML and the DIAN validation message | Formerly Res. 000013/2021 arts. 15 and 23 (*Conservación*), compiled in Res. 000227/2025 (number not confirmed) — for the legal period applicable to tax supporting documents |
| Retain the third-party generation mandate | Res. 000227/2025 art. 1.5.3.8.1 (formerly Res. 000013/2021 art. 22) — both parties, for the legal period, produced on DIAN request |
| Deliver a payslip to the employee | **No statutory obligation.** Res. 000227/2025 art. 1.5.3.8.3 (formerly Res. 000013/2021 art. 24) makes the graphical representation permissive |
| Deliver **Formulario 220** to the employee | **Mandatory** — annually, by the **last business day of March** (ET art. 378; DUR 1625 art. 1.6.1.13.2.40) |
| Deliver social-security payment evidence for the last 3 months | **Mandatory** on termination — within **60 days**, to the last registered address, with proof; otherwise *"la terminación del contrato no producirá efecto"* (CST art. 65 par. 1) |
| Certificate of service on request | CST art. 57 num. 7 — time of service, nature of the work, salary earned |

---

## 7. Confidence statement

| Element | Confidence | Basis |
|---|---|---|
| **Absence of a statutory payslip-content article in the CST** | **~97%** | Grep-tested to zero hits across the full consolidated CST for seven distinct Colombian terms for a payslip; Ley 2466 de 2025 art. 15 read in full and confirmed to add no such obligation |
| Res. 000227/2025 art. 1.5.3.3.1 (formerly Res. 000013/2021 art. 5) mandatory content (13 items) — compiled number pending validation | **~98%** | Read verbatim from the resolution PDF |
| Res. 000227/2025 art. 1.5.3.8.3 (formerly Res. 000013/2021 art. 24) permissive graphical representation + QR — compiled number pending validation | **~98%** | Read verbatim |
| Res. 000227/2025 art. 1.5.3.8.5 (formerly Res. 000013/2021 art. 26) Spanish + COP — compiled number pending validation | **~98%** | Read verbatim |
| QR data set and URL format | **~95%** | Read verbatim from Anexo Técnico §13.1 |
| Three rounding regimes | **~95%** | Each read verbatim from its own instrument |
| CST arts. 133–148 payment mechanics | **~97%** | Read verbatim from the consolidated CST |
| Minimum QR print size (**2 cm**) | **~95%** | Read verbatim from Anexo Técnico §13.1 (*"El tamaño mínimo que debe tener el código bidimensional QR es de 2cm"*) — initially unresolved, closed on a second pass |
| Whether any *sectoral* or *collective-agreement* payslip requirement exists | **NOT SEARCHED** | Colombian *convenciones colectivas* can impose payslip content contractually; no attempt was made to survey them, and none would be nationally applicable |

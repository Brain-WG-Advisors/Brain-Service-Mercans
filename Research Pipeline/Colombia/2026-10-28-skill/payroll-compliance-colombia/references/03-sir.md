# 03 — Statutory Integrations Register: Colombia (CO), fiscal year 2026

> **Status of this file (recompiled 28 Oct 2026).** The SIR in force is **CO-SIR-001 v1.1** (Google Doc on
> Drive `19 - Staturory Integration`, 21 Oct 2026; earlier file name `CO-SIR-INDEX-001`, which CCG v1.4
> Module 10 still uses). Its Version history records a single change from v1.0: *"Citations of Res. DIAN
> 000013 de 2021 updated to Res. DIAN 000227 de 2025"*. The Google Doc could not be downloaded for this
> compilation, so this file is the integrations reference of the 5 Oct 2026 skill with that one change
> applied, using the SIR v1.1 mapping (former Res. 000013/2021 art. 1 → Res. 000227/2025 art. 1.5.3.1.1;
> art. 3 → 1.5.3.2.2; art. 4 → 1.5.3.2.3; art. 8 → 1.5.3.4.1.1; art. 22 → 1.5.3.8.1). The former arts. 5
> and 24 are given the numbers printed in CCG v1.4 Module 10.3 (1.5.3.3.1 and 1.5.3.8.3), **pending
> validation** (hub F6-20261027-CO-C19); the former arts. 6 and 20 have no mapped number.
>
> **Identifiers.** The `CO-SIR-00n` headings below are this file's own section labels, not Drive
> documents. The matching report specs are CO-DIAN-001 (§001), CO-DIAN-002 (§002), CO-PILA-003 (§003,
> plus CO-PILA-007 for pensioners paid by the employer), CO-DIAN-004 (§004), CO-DIAN-005 (§005) and
> CO-CESANTIAS-006 (§006) — see `04-reports-spec.md`. §007 (MinTrabajo disability-hiring report) is **out
> of scope** of the payroll build (CCG v1.4 Module 10.1: "None (out of scope)", HR scope; hub
> F6-20261027-CO-C29, pending validation); it is kept for reference only.
>
> **Known defects of the DIAN Technical Annex beyond D-1 to D-4** (hub F6-20261027-CO-C27, pending
> validation): §9.7 names `SendBillSync` while the text and the WSDL use `SendNominaSync` (the WSDL
> governs); `NumeroDocumento` is `xsd:integer` (a passport number does not fit); `SegundoApellido` is
> required. Treat these as alerts until the XSD v1.0.6 is re-read.

**Purpose.** For each Colombian authority a payroll engine must interact with: the channel, the direction,
the authentication mechanism, and — critically — whether the channel is **genuine machine-to-machine
(M2M)** or a **portal round-trip** (a human, or a robot impersonating one, must log into a web session).

**Headline finding — Colombia inverts the usual pattern.** In the CEMAC/GCC jurisdictions covered
elsewhere in this pipeline the default is portal round-trip. Colombia is **split**, and the split is
counter-intuitive:

- The **payslip-equivalent document (nómina electrónica) IS a genuine M2M web service** — SOAP 1.2,
  certificate-authenticated, synchronous, one call per employee per month. This is the *deepest*
  integration of the three and the one most jurisdictions do not have.
- The **income-tax withholding declaration (Formulario 350) is a portal round-trip.**
- The **social-security remittance (PILA) is a portal round-trip through a licensed private
  intermediary** — the employer never talks to the government directly at all.

So an implementation cannot pick one posture for the country; it needs an M2M client **and** two
portal/file paths.

---

## CO-SIR-001 — DIAN · Documento Soporte de Pago de Nómina Electrónica

| Attribute | Value |
|---|---|
| **Authority** | Dirección de Impuestos y Aduanas Nacionales (DIAN) |
| **Instrument** | **Resolución DIAN 000227 de 2025** (Resolución Única), arts. 1.5.3.1.1 to 1.5.3.9.8, which compile Resolución DIAN 000013 de 11 de febrero de 2021 (37 articles; formerly the standalone instrument, as modified by Res. 000037 de 2021, Res. 000063 de 2021, Res. 000151 de 2021, Res. 000028 de 2022) |
| **Technical annex** | *Anexo Técnico Documento Soporte de Pago de Nómina Electrónica* — **Versión 1.0**, 269 pages, adopted under Res. 000227/2025 (formerly Res. 000013/2021 art. 20; the compiled article number was not mapped in SIR v1.1) |
| **Schemas** | `NominaIndividualElectronicaXSDV1.0.6.xsd`, `NominaIndividualDeAjusteElectronicaXSDV1.0.6.xsd`, plus the UBL 2.1 common modules and XAdES 1.3.2 / 1.4.1 schemas |
| **Direction** | **Outbound** (employer → DIAN), with a **synchronous inbound** validation response |
| **Frequency** | **Monthly**, one document per beneficiary per month (Res. 000227/2025 art. 1.5.3.2.2, formerly Res. 000013/2021 art. 3) |
| **Deadline** | Within the **first 10 days of the month following** the payment (Res. 000227/2025 art. 1.5.3.4.1.1, formerly Res. 000013/2021 art. 8) |
| **Channel** | **GENUINE M2M — SOAP 1.2 web service** |
| **Authentication** | **X.509 digital certificate** issued by a root CA accredited by **ONAC** in Colombia, used both for TLS client authentication and for the XAdES-EPES document signature |
| **Round-trip?** | **No** — fully machine-to-machine |

### Transport contract

From the *Anexo Técnico* §9.3–§9.5 (verbatim extracts):

> *"Los Proveedores Tecnológicos realizarán la transmisión de los documentos electrónicos consumiendo
> el servicio WEB que expone la DIAN **sin operar intermediarios** en dicha transmisión."*
> *"Para la transmisión de los DE deberán desarrollar un **software cliente independiente del lenguaje
> de programación**."*
> *"El lenguaje XML de los archivos de intercambio de información será el de **UBL 2.1** para el proceso
> de firmado y las demás secciones del documento serán la estructura propia detallada en el presente
> Anexo Técnico."*
> *"Con el fin de garantizar la seguridad en la comunicación, el software cliente deberá **autenticarse
> ante la DIAN utilizando certificado digital**."*
> *"…será realizado mediante el estándar **SOAP versión 1.2**, con intercambio de mensajes XML en el
> estándar **Style/Encoding: Document/Literal**."*

**Request envelope** (annex §9.5, verbatim):

```xml
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
               xmlns:wcf="http://wcf.dian.colombia">
  <soap:Header/>
  <soap:Body>
    <wcf:SendNominaSync>
      <wcf:contentFile>
        <!-- Área de Dato: archivo Nomina.zip en base 64 que contiene un documento XML
             que atiende al formato definido para la operación de nómina -->
      </wcf:contentFile>
    </wcf:SendNominaSync>
  </soap:Body>
</soap:Envelope>
```

**Payload:** a **ZIP containing the XML**, then **base64-encoded** into `contentFile`. Not the raw XML.

**Response:** synchronous. Annex §9.2: *"Posterior a las validaciones se genera respuesta (Response)
**síncrona** con el detalle de la evaluación del documento, que incluye dentro de sus elementos un
**ApplicationResponse codificado en Base64** con la respuesta de validación de la DIAN."*

**Endpoint URL:** *not published in the annex*. Annex §14.5, note: *"la URL del Web Service 'WS' estará
expuesta en el **catálogo de participante** (habilitación ó producción) sobre la opción **Participantes,
Emisor de Nómina**."* The endpoint is therefore obtained **after habilitación**, from inside the DIAN
participant catalogue — an implementation cannot hard-code it from public documentation.

**Environments** (annex §5.1.1 — `InformacionGeneral/@Ambiente`):

| Code | Environment | QR consultation host |
|---|---|---|
| **1** | **Producción** — *"producen efectos para todas las finalidades legales: tributarios, financieros, económicos, comerciales y de del derecho del consumidor"* | `https://catalogo-vpfe.dian.gov.co` |
| **2** | **Pruebas** (habilitación) — *"no producen ningún tipo de efecto"* | `https://catalogo-vpfe-hab.dian.gov.co` |

### Connection-level validation rules (annex §6.2)

| ID | Rule | Class | Message |
|---|---|---|---|
| ZA01 | XML file size above **500 KB** | **R** (reject) | *"Tamaño del mensaje superior al límite establecido [Máximo: 500 KB]"* |
| ZA02 | Service momentarily stopped | N (notify) | *"Servicio parado momentáneamente [corto plazo]"* |
| ZA03 | Service stopped with no forecast | N | *"Servicio parado sin previsión"* |
| ZB01 | XML schema incorrect | **R** | *"Fallo en el esquema XML del archivo"* |
| ZB02 | Editing characters at the start/end of the message or between tags | **R** | *"No es permitida la presencia de caracteres de edición en el inicio/fin o entre los tags del mensaje"* |
| ZB03 | Encoding other than **UTF-8** | **R** | *"XML con codificación diferente de UTF-8"* |
| ZB04 | DIAN namespace-prefix customisations | — | — |

Document-level rules: **~240 rules** with IDs `NIE001`–`NIE2xx` (NominaIndividual), `NIAE0xx`–`NIAE2xx`
(NominaIndividualDeAjuste) and `DC01`–`DC56` (digital signature). Class **R** = the document is rejected;
class **N** = notification only, the document is still stamped *validado*. Three global rules worth
building explicit engine guards for:

| ID | Rule | Class |
|---|---|---|
| 90 | *"Solo se podrá transmitir una **única vez** el Número del documento para el trabajador."* → *"Documento procesado anteriormente"* | **R** |
| 92 | *"El Emisor del Documento debe encontrarse **habilitado** en la plataforma de emisión de Nómina Electrónica."* | **R** |
| VLR01 | *"Los valores monetarios/porcentajes deben corresponder a valores **positivos**."* | **R** |

### Digital signature

- **Format: XAdES-EPES** (`ds:Signature` inside `ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent`).
  The XSD's own annotation states: *"Se está utilizando el método de firma digital **XAdES - EPES**, ya
  conocido por los contribuyentes de la DIAN en Colombia."*
- **Certificate authority (rule DC46, class R):** *"El SerialNumber debe pertenecer a una entidad raíz
  certificadora abierta **avalada por la ONAC** en Colombia."*
- **Signer role (rule DC56, class R):** *"El valor del rol debe ser **`thirdparty`** ó **`supplier`**."*
  → a payroll provider signing on the employer's behalf must assert `thirdparty`.
- **Signature policy** (rules DC47–DC51): `SignaturePolicyIdentifier` / `SignaturePolicyId` /
  `SigPolicyId` / `Identifier` must carry **the identifier defined by DIAN**, and `SigPolicyHash` must
  match. Each is class **R**.

### Software fingerprint and document identifiers

**SoftwareSecurityCode** (annex §8.3):
```
SoftwareSecurityCode := SHA-384 ( IdSoftware + PIN + NroDocumento )
```
where `IdSoftware` is the activation identifier DIAN assigns when the software is activated in the NE
system, and `PIN` is the value the obligado assigned at activation. The annex stresses that both must be
kept confidential. Carried in `ProveedorXML/@SoftwareSC`; `ProveedorXML/@SoftwareID` carries the
plain identifier and must correspond to *"un software autorizado para este Emisor"* (rule NIE019, R).

**CUNE — Código Único de Documento Soporte de Pago de Nómina Electrónica** (annex §8.1):
```
CUNE := SHA-384 ( NumNE + FecNE + HorNE + ValDev + ValDed + ValTolNE
                  + NitNE + DocEmp + TipoXML + Software-Pin + TipAmb )
```

| Token | Definition | XPath |
|---|---|---|
| `NumNE` | Document number = `Prefijo` concatenated with `Consecutivo` | `/NominaIndividual/NumeroSecuenciaXML/@Numero` |
| `FecNE` | Generation date | `/NominaIndividual/InformacionGeneral/@FechaGen` |
| `HorNE` | Generation time **including GMT offset** | `/NominaIndividual/InformacionGeneral/@HoraGen` |
| `ValDev` | Total devengados — decimal point, **two decimals truncated**, no thousands separator, no currency symbol | `/NominaIndividual/DevengadosTotal` |
| `ValDed` | Total deducciones — same format | `/NominaIndividual/DeduccionesTotal` |
| `ValTolNE` | Total paid (devengado − deducciones) — same format | `/NominaIndividual/ComprobanteTotal` |
| `NitNE` | Issuer NIT, **no dots, no hyphens, no verification digit** | `/NominaIndividual/Empleador/@NIT` |
| `DocEmp` | Employee identification number, no dots or hyphens, no verification digit | `/NominaIndividual/Trabajador/@NumeroDocumento` |
| `TipoXML` | XML type code (102 or 103) | `/NominaIndividual/InformacionGeneral/@TipoXML` |
| `Software-Pin` | **Not present in the XML** — *"Valor reservado, de circulación restringida, asignado por quien obtuvo el Código de Activación del software"* | — |
| `TipAmb` | Environment code (1 or 2) | `/NominaIndividual/InformacionGeneral/@Ambiente` |

⚠ **The annex's worked example of the CUNE does not reproduce.** Using the printed inputs
(`NumNE=N00001`, `FecNE=2020-01-16`, `HorNE=10:53:10-05:00`, `ValDev=3500000.00`,
`ValDed=1000000.00`, `ValTolNE=2500000.00`, `NitNE=700085371`, `DocEmp=800199436`, `TipoXML=102`,
`Software-Pin=693`, `TipAmb=1`) the published SHA-384
`16560dc8956122e84ffb743c817fe7d494e058a44d9ca3fa4c234c268b4f766003253fbee7ea4af9682dd57210f3bac2`
was **not** reproduced under **16 plausible readings** tested this session (including the annex's own
printed concatenation string, which is itself internally inconsistent — it renders `HorNE` as
`1053:10-05:00`, one colon short of the stated input). Do **not** use the annex example as a
conformance test; validate CUNE generation against the habilitación environment instead.
See `07-qa-report.md` item Q-9.

### Graphical representation (the payslip the employee receives)

**Res. 000227/2025 art. 1.5.3.8.3 (formerly Res. 000013/2021 art. 24; compiled article number taken from CCG v1.4 Module 10.3, correspondence pending validation — hub item F6-20261027-CO-C19):** issuing a graphical representation is **optional** (*"si lo requieren, podrán
expedir"*), in digital or printed format, and if issued it must contain **at minimum the content of Res. 000227/2025 art. 1.5.3.3.1** (formerly Res. 000013/2021 art. 5; same pending-validation note)
plus the **QR code**. Annex §13.1: the QR must appear **on every page** of every digital format and of the
paper print, and its URL is
`https://catalogo-vpfe.dian.gov.co/document/searchqr?documentkey=<CUNE>`.
Annex §13.1 also fixes what the QR encodes: `NumNIE`, `FecNIE`, `HorNIE` (with GMT), `NitNIE`,
`DocEmp`, `ValDev`, `ValDed`, `ValTol`, `CUNE`, `QRCode`.

Annex §13.1: *"La representación gráfica siempre será 'una representación, una imagen' de la
información consignada en el formato XML … Esto significa que **el documento electrónico siempre será el
que tenga valor legal** para las autoridades nacionales."*

### Third-party (payroll provider) operation

**Res. 000227/2025 art. 1.5.3.8.1 (formerly Res. 000013/2021 art. 22):** where the obligado generates and transmits through a third party, *"el
citado tercero deberá estar **previamente habilitado** por la … DIAN; de conformidad con dispuesto en
los artículos 572 y 573 del Estatuto Tributario."* Transitional paragraph: the third party must register
that capacity in the **RUT**. Both parties must keep the accrediting document for the legal period.

### Implementation calendar (historical, all groups now live)

Formerly **Res. 000013/2021 art. 6**, as modified by Res. 000037/2021 and Res. 000063/2021 (now compiled in Res. 000227/2025; the compiled article number was not mapped in SIR v1.1), phased by headcount:

| Group | Employees | Habilitación from | First period reported | Report by |
|---|---|---|---|---|
| 1 | More than 250 | 18 August 2021 | Sept 2021 | Oct 2021 (max 29 Oct 2021) |
| 2 | 101–250 | Oct 2021 | Nov 2021 | |
| 3 | 11–100 | Nov 2021 | Dec 2021 | |
| 4 | 1–10 | Dec 2021 | May 2022 | |

Res. 000151 de 2021 and Res. 000028 de 2022 set the special deadline for 1–10-employee employers and
for employers not obliged to issue electronic sales invoices.

### Adjustment notes

`NominaIndividualDeAjuste` (`TipoXML` = **103**), with `TipoNota` from annex §5.5.8:

| Code | Type | Annex definition |
|---|---|---|
| **1** | **Reemplazar** | *"cuando se requiera realizar ajustes sobre Documentos Soporte de Pago de Nómina Electrónica o Notas de Ajuste …, por errores aritméticos, contables o de contenido"* |
| **2** | **Eliminar** | *"cuando se requiera eliminar el Documento … para los casos en los cuales se haya transmitido un documento por errores contables o de procedimiento"* |

Annex note on code 2: *"solo **invalida** los documentos enviados por error, no obstante los mismos
seguirán existiendo en la base de datos pero quedarán marcados con esta observación."* — a deletion is a
logical, not physical, removal. Adjustment notes share the ten-day deadline of Res. 000227/2025 art. 1.5.3.4.1.1 (formerly Res. 000013/2021 art. 8).

### Consultation service

Annex §13 — read-only lookup via the QR URL (production and habilitación hosts above). The annex also
ships a SOAP UI walkthrough (§14) for consuming the web service, including keystore configuration —
confirming that certificate-based mutual authentication is the intended mechanism.

---

## CO-SIR-002 — DIAN · Formulario 350, Declaración mensual de retenciones en la fuente

| Attribute | Value |
|---|---|
| **Authority** | DIAN |
| **Instrument** | ET art. 382; DUR 1625 de 2016 art. 1.6.1.13.2.33 (deadlines set by **Decreto 2229 de 2023**, in business days); form prescribed by **Resolución DIAN 000031 de febrero de 2024**, in force from 1 August 2024 |
| **Direction** | Outbound (employer → DIAN), declaration + payment |
| **Frequency** | Monthly |
| **Deadline** | **7th to 16th business day** of the following month, by the **last digit of the NIT** (see `01-ccg.md` §12.2) |
| **Channel** | **Portal round-trip** — DIAN's *Servicios Informáticos Electrónicos* (MUISCA), *Diligenciar / Presentar / Pagar declaraciones* |
| **Authentication** | DIAN portal credentials + the taxpayer's **Instrumento de Firma Electrónica (IFE)** for signature-obliged filers |
| **Round-trip?** | **Yes** |
| **Confidence** | **~85%.** The legal basis, form version and deadline table were read from primary sources (DIAN normograma text of Decreto 2229 de 2023; DIAN press release *Comunicado No. 128* of 26 December 2025). The *absence* of a published M2M filing API for Form 350 is asserted from the negative: DIAN publishes web-service contracts for the *sistema de facturación electrónica* family (invoice, nómina, RADIAN, documento equivalente) and none for declaration forms. Not proven by a retrieved DIAN statement. |

**Notable 2024+ change:** the current Formulario 350 requires withholdings on **legal persons** and on
**natural persons** to be disclosed **separately** — an engine must partition its withholding ledger by
counterparty type, not just by concept.

**Rounding:** ET art. 577 — all values entered on the form are rounded to the **nearest multiple of
1.000** (fractions below 500 down, 500 and above up).

---

## CO-SIR-003 — Social security and parafiscales · PILA

| Attribute | Value |
|---|---|
| **Authorities (ultimate recipients)** | EPS (salud), AFP / Colpensiones (pensión), ARL (riesgos laborales), CCF, SENA, ICBF; **UGPP** as the audit and collection authority |
| **Instrument** | Decreto 780 de 2016 Libro 3 Parte 2, arts. 3.2.1.5, 3.2.2.1, 3.2.3.9–3.2.3.11, as modified/substituted by **Decreto 1990 de 2016**; Ley 828 de 2003 art. 10; Ley 1753 de 2015 art. 135 |
| **Direction** | Outbound (employer → operador de información → administradoras) |
| **Frequency** | Monthly, **paid a month in arrears** (*"por períodos mensuales completos y se pagará mes vencido"* — Decreto 1072/2015 art. 2.2.4.2.5.6) |
| **Deadline** | **2nd to 16th business day** of the following month, by the **last two digits of the NIT** (see `01-ccg.md` §12.1) |
| **Channel** | **Portal round-trip via a licensed private intermediary** — an *operador de información* |
| **Authentication** | Credentials issued by the chosen operador de información; no government PKI |
| **Round-trip?** | **Yes**, and with an extra hop: the employer never transacts with the government directly |
| **Confidence** | **~90%** on the legal framework and calendar (Decreto 1990 de 2016 read verbatim). **~70%** on the operator interface: Decreto 1990 establishes the *planilla electrónica* / *planilla asistida* duality and the operator's role, but the actual file layout is set by **Resolución MinSalud 2388 de 2016** and its amendments, which was **not retrieved this session**. See `07-qa-report.md` item Q-10. |

**Two modalities** (Decreto 780/2016 art. 3.2.3.9, as added by Decreto 1990 de 2016 art. 3):

- **Planilla electrónica** — mandatory above the headcount thresholds (originally phased from 20+
  cotizantes down to 3+ in municipalities not of categories 5 and 6). This is the flat-file / structured
  upload path, and it is what a payroll engine targets.
- **Planilla asistida** — available only to employers with **fewer than 3 cotizantes**; data captured
  interactively.

Headcount for the threshold is *"la sumatoria de todos los cotizantes vinculados a una misma persona
natural o jurídica, **incluyendo los vinculados a sus sucursales y agencias**, que operen bajo una misma
razón social"* (par.) — a multi-branch employer cannot fragment itself into sub-3-cotizante units.

**Rounding at the interface** (Decreto 780/2016 art. 3.2.1.5, substituted by Decreto 1990/2016 art. 1):
IBC **up to the nearest whole peso**; contribution amounts and interest **up to the nearest multiple of
100**. Any engine that submits nearest-rounded or truncated figures will produce operator-side
mismatches.

**Novedades.** Decreto 1072 de 2015 art. 2.2.4.3.6 requires a new hire to be reported to the ARL *"a más
tardar el día hábil siguiente al que se produjo dicho ingreso"*; other novedades may be reported
monthly with the autoliquidación. Coverage begins *"el día calendario siguiente al de la afiliación"*
(art. 2.2.4.2.5.4) — so a same-day-start employee has an uninsured first day unless affiliated the day
before.

**UGPP as counterparty.** Created by **Ley 1151 de 2007 art. 156** (Ministry of Finance), with
determination and collection powers over social-protection parafiscales, reinforced by Ley 1607 de 2012
and Decretos 169 de 2008, 5021 de 2009 and 575 de 2013. The UGPP cross-matches DIAN data (including
the nómina electrónica and exógena datasets) against PILA and opens *procesos de fiscalización* where
the declared income and the contributed IBC diverge. **Engine consequence:** the IBC an engine reports
in PILA and the *devengados* it reports in the nómina electrónica are **cross-checked against each other
by a third authority**. They must be reconcilable by construction — in particular the CST art. 128 /
Ley 1393 art. 30 non-salary split must be identical on both sides.

---

## CO-SIR-004 — DIAN · Formulario 220, Certificado de Ingresos y Retenciones

| Attribute | Value |
|---|---|
| **Authority** | DIAN (form prescriber); the **recipient is the employee**, not DIAN |
| **Instrument** | ET arts. 378 and 379; DUR 1625 art. 1.6.1.13.2.40; form prescribed by **Resolución DIAN 000022 de 20 de febrero de 2024** for tax year 2023 onwards |
| **Direction** | **Employer → employee** (no filing to DIAN) |
| **Frequency** | Annual, for the immediately preceding tax year |
| **Deadline** | *"a más tardar el **último día hábil del mes de marzo** por el año gravable que corresponda"* |
| **Channel** | Employer-issued document (PDF or paper); DIAN also pre-populates a version in the employee's *Servicios Informáticos* account |
| **Authentication** | ET art. 379 literal i requires the **signature of the payer or withholding agent**, certifying that the data are true, that no other payment or compensation exists for the period, and that the payments and withholdings were made in accordance with the applicable rules |
| **Round-trip?** | N/A — not a filing |

**ET art. 378:** *"Los agentes de retención en la fuente deberán expedir **anualmente** a los asalariados,
un Certificado de Ingresos y Retenciones correspondiente al año gravable inmediatamente anterior,
según el formato que prescriba la Dirección General de Impuestos Nacionales."*

Content is fixed by **ET art. 379** — see `04-reports-spec.md` CO-DIAN-004.

---

## CO-SIR-005 — DIAN · Información exógena, Formato 2276

| Attribute | Value |
|---|---|
| **Authority** | DIAN |
| **Instrument** | ET art. 631-3; **Resolución DIAN 000227 de 23 de septiembre de 2025** (*Resolución Única en Materia Tributaria, Aduanera y Cambiaria*, Diario Oficial 53.254 of 25 September 2025) arts. **1.3.7.1.1** (content) and **1.3.9.1** (deadlines) |
| **Format** | **Formato 2276 — Versión 4**, "Información de ingresos y retenciones por rentas de trabajo y de pensiones" |
| **Direction** | Outbound (employer → DIAN) |
| **Frequency** | Annual, for the preceding tax year |
| **Deadline** | Grandes contribuyentes: 17th–18th business day of April and 1st–8th business day of May, by the **last digit** of the NIT. Personas jurídicas y naturales: 9th business day of May to 9th business day of June, by the **last two digits** of the NIT (full table in `04-reports-spec.md`) |
| **Channel** | **Portal round-trip** — DIAN *Servicios Informáticos Electrónicos*, "Presentación de Información por Envío de Archivos", XML upload validated against the DIAN-published XSD for the format |
| **Authentication** | DIAN portal credentials + **Instrumento de Firma Electrónica (IFE)** |
| **Round-trip?** | **Yes** |
| **Confidence** | **~90%** on the legal basis, field list, version and deadline tables (all read verbatim from Res. 000227 de 2025). **~70%** on the upload mechanics and the XSD structure for Formato 2276 v4, which were **not** retrieved — the DIAN *especificaciones técnicas* document for the format was not obtained this session. See `07-qa-report.md` item Q-11. |

**Res. 000227/2025 art. 1.3.9.1 par. 1:** *"La información se debe reportar dentro de los plazos señalados
en el presente artículo **de acuerdo con la calidad de Gran Contribuyente, persona jurídica o persona
natural que se posea en el momento de informar**"* — the bracket is determined at filing time, not at
year-end.

**Note on year-specific extensions.** Deadlines are routinely moved by a subsequent resolution — for the
2025 tax year, **Resolución DIAN 000012 de abril de 2026** extended the dates for grandes contribuyentes
whose NIT ends in 1, 2 and 3. An engine must not hard-code calendar dates; it must read the resolution
in force for the filing year.

---

## CO-SIR-006 — Fondo de Cesantías · annual deposit

| Attribute | Value |
|---|---|
| **Counterparty** | A private *sociedad administradora de fondos de cesantías* **chosen by the employee** |
| **Instrument** | **Ley 50 de 1990 art. 99 num. 3** |
| **Direction** | Outbound (employer → fund), cash transfer plus an allocation file |
| **Frequency** | Annual |
| **Deadline** | Liquidated at **31 December**; deposited **before 15 February** of the following year (i.e. by **14 February**) |
| **Channel** | Banking transfer + the fund's own web portal or file interface — **no government channel and no standard national format** |
| **Authentication** | Per-fund credentials |
| **Round-trip?** | **Yes**, per fund; and an employer may face **as many interfaces as its employees have chosen funds** |
| **Penalty** | **One day's salary per day of delay** |

**Ley 2466 de 2025 art. 15** added **CST art. 57 par. 4**: a demonstrable **direct payment to the
employee** is *liberatorio* and does not attract the non-deposit penalty, *"salvo que se demuestre que el
pago no se realizó en condiciones de libertad y que no fue utilizado en fines autorizados por la ley. No
obstante, **la afiliación a Fondo de Cesantías es obligatoria**."*
→ affiliation remains compulsory even where the employer pays directly.

**Engine consequence:** the *fondo de cesantías* is employee-elected master data (see
`05-data-dictionary.md`), separate from the employee-elected AFP and EPS and from the
employer-elected ARL and CCF. Four independent institution codes per employee, three chosen by the
employee and one by the employer.

---

## CO-SIR-007 — MinTrabajo · disability-hiring contract report

| Attribute | Value |
|---|---|
| **Authority** | Ministerio del Trabajo |
| **Instrument** | **Ley 2466 de 2025 art. 15**, adding a numeral to CST art. 57 |
| **Direction** | Outbound (employer → MinTrabajo) |
| **Trigger** | Signature of an employment contract with a person with a disability |
| **Deadline** | *"dentro de los **quince días siguientes a su celebración**"* |
| **Channel** | *"a través del **sitio electrónico** del Ministerio del Trabajo, quien llevará un registro
actualizado de lo anterior, debiendo mantener **reserva** de dicha información"* → **portal round-trip** |
| **Round-trip?** | **Yes** |
| **Confidence** | **~80%.** The obligation and the 15-day deadline are verbatim from Ley 2466 art. 15. The specific MinTrabajo portal module and its field set were **not** identified this session; the implementing regulation was not located. See `07-qa-report.md` item Q-12. |

Related quota, same article: employers with **up to 500** employees must employ at least **two persons
with a disability per 100** on the permanent headcount; from **501** employees, one additional per
100-employee tranche. Certification is issued per MinSalud rules. Par. 3: the values/percentages are
**optional in the first year** of the law and mandatory from the second — the law was sanctioned
25 June 2025, so mandatory application starts **26 June 2026**. Par. 2: where it is not possible to hire
persons with a disability in a given role or economic sector, that must be reported to MinTrabajo.

---

## Channel summary

| Ref | Authority / counterparty | Direction | Frequency | M2M? | Auth |
|---|---|---|---|---|---|
| CO-SIR-001 | DIAN — nómina electrónica | Out + sync in | Monthly | **YES — SOAP 1.2** | X.509 (ONAC CA) + XAdES-EPES |
| CO-SIR-002 | DIAN — Formulario 350 | Out | Monthly | No — portal | Portal creds + IFE |
| CO-SIR-003 | PILA (via operador de información) | Out | Monthly | No — portal via private intermediary | Operator credentials |
| CO-SIR-004 | Formulario 220 (to the **employee**) | Employer → employee | Annual | N/A | Withholding agent's signature |
| CO-SIR-005 | DIAN — Formato 2276 exógena | Out | Annual | No — portal file upload | Portal creds + IFE |
| CO-SIR-006 | Fondo de cesantías (private, employee-elected) | Out | Annual | No — per-fund portal | Per-fund credentials |
| CO-SIR-007 | MinTrabajo — disability contract report | Out | Event-driven | No — portal | Portal credentials |

## Design note — the reconciliation obligation nobody legislates

Three separate datasets describe the same payroll month, are filed to two different authorities on two
different calendars in two different rounding conventions, and are **cross-matched by a third
authority**:

| Dataset | Filed to | Calendar | Rounding | Salary/non-salary basis |
|---|---|---|---|---|
| PILA (IBC) | Operador → administradoras | 2nd–16th business day | **Up** to 100 | IBC after the Ley 1393 art. 30 40% clamp |
| Nómina electrónica (devengados / deducciones) | DIAN, M2M | First 10 days | **Half-to-even**, ±2,00 | Explicit `S` / `NS` element split |
| Formulario 350 (retención) | DIAN, portal | 7th–16th business day | **Nearest 1.000** | Gravable base after ET art. 388 depuration |

The **UGPP** reconciles column 1 against columns 2–3. No statute defines the reconciliation rules, so an
engine must guarantee consistency by construction: one salary/non-salary decision per wage type, applied
identically to the IBC, the XML element choice and the tax base, with the rounding difference isolated in
the `Redondeo` element rather than absorbed into a substantive line.

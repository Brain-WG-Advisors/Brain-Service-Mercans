# P3 — Outbound Payload Specification

**CO / DIAN-NE** · `NominaIndividual` and `NominaIndividualDeAjuste`, XSD **v1.0.6**
Structure below is read directly from the shipped XSDs, not paraphrased from the annex.

---

## 1. The two document types

| `TipoXML` | Root element | Namespace | Purpose |
|---|---|---|---|
| **102** | `NominaIndividual` | `dian:gov:co:facturaelectronica:NominaIndividual` | The monthly payroll support document |
| **103** | `NominaIndividualDeAjuste` | `dian:gov:co:facturaelectronica:NominaIndividualDeAjuste` | Adjustment note over a previously validated document |

Both use `elementFormDefault="qualified"` and declare exactly one top-level element and one
complexType. Field carriers (elements + attributes):

| Schema | Elements | Attributes | Required attributes | Total carriers |
|---|---|---|---|---|
| `NominaIndividualElectronicaXSDV1.0.6.xsd` | 96 | 166 | 103 | **262** |
| `NominaIndividualDeAjusteElectronicaXSDV1.0.6.xsd` | 107 | 205 | 131 | **312** |

Note the design idiom: **almost all data lives in XML attributes, not element text.** Only a
handful of leaves (`CodigoQR`, `Notas`, `Dotacion`, `ApoyoSost`, `Teletrabajo`, `BonifRetiro`,
`Indemnizacion`, `Reintegro`, the deduction scalars, `Redondeo`, and the three totals) are element
values. A mapper written on the assumption of element-per-field will need reworking.

## 2. `NominaIndividual` — top-level structure

```
NominaIndividual  @SchemaLocation (required)
├── ext:UBLExtensions                  0..1   ← XAdES-EPES ds:Signature lives here
├── Novedad                            0..1   @CUNENov
├── Periodo                            1..1   @FechaIngreso @FechaRetiro? @FechaLiquidacionInicio
│                                             @FechaLiquidacionFin @TiempoLaborado @FechaGen
├── NumeroSecuenciaXML                 1..1   @CodigoTrabajador? @Prefijo? @Consecutivo @Numero
├── LugarGeneracionXML                 1..1   @Pais @DepartamentoEstado @MunicipioCiudad @Idioma
├── ProveedorXML                       1..1   @NIT @DV @SoftwareID @SoftwareSC (+ name fields)
├── CodigoQR                           1..1
├── InformacionGeneral                 1..1   @Version @Ambiente @TipoXML @CUNE @EncripCUNE
│                                             @FechaGen @HoraGen @PeriodoNomina @TipoMoneda @TRM?
├── Notas                              0..n
├── Empleador                          1..1   @NIT @DV @Pais @DepartamentoEstado
│                                             @MunicipioCiudad @Direccion (+ name fields)
├── Trabajador                         1..1   @TipoTrabajador @SubTipoTrabajador @AltoRiesgoPension
│                                             @TipoDocumento @NumeroDocumento @PrimerApellido
│                                             @SegundoApellido @PrimerNombre @OtrosNombres?
│                                             @LugarTrabajo{Pais,DepartamentoEstado,MunicipioCiudad,Direccion}
│                                             @SalarioIntegral @TipoContrato @Sueldo @CodigoTrabajador?
├── Pago                               1..1   @Forma @Metodo @Banco? @TipoCuenta? @NumeroCuenta?
├── FechasPagos                        1..1   └── FechaPago 1..n
├── Devengados                         1..1   (see §3)
├── Deducciones                        1..1   (see §4)
├── Redondeo                           0..1
├── DevengadosTotal                    1..1
├── DeduccionesTotal                   1..1
└── ComprobanteTotal                   1..1
```

`Trabajador` is `1..1` — **one document per employee.** There is no employee collection.

## 3. `Devengados` (accruals)

`Basico` is the only mandatory child. Everything else is optional.

| Node | Card. | Attributes / type |
|---|---|---|
| `Basico` | 1..1 | `@DiasTrabajados` (int), `@SueldoTrabajado` (dec) |
| `Transporte` | 0..n | `@AuxilioTransporte`, `@ViaticoManuAlojS`, `@ViaticoManuAlojNS` |
| `HEDs/HED` · `HENs/HEN` · `HRNs/HRN` · `HEDDFs/HEDDF` · `HRDDFs/HRDDF` · `HENDFs/HENDF` · `HRNDFs/HRNDF` | 0..1 / 0..n | `@HoraInicio?` `@HoraFin?` `@Cantidad` `@Porcentaje` `@Pago` |
| `Vacaciones` | 0..1 | `VacacionesComunes` 0..n (`@FechaInicio?` `@FechaFin?` `@Cantidad` `@Pago`); `VacacionesCompensadas` 0..n (`@Cantidad` `@Pago`) |
| `Primas` | 0..1 | `@Cantidad` `@Pago` `@PagoNS?` |
| `Cesantias` | 0..1 | `@Pago` `@Porcentaje` `@PagoIntereses` |
| `Incapacidades` | 0..1 | `Incapacidad` 0..n: `@FechaInicio?` `@FechaFin?` `@Cantidad` `@Tipo` `@Pago` |
| `Licencias` | 0..1 | `LicenciaMP` / `LicenciaR` (`…@Cantidad @Pago`); `LicenciaNR` (`…@Cantidad`, **no `@Pago`**) |
| `Bonificaciones` | 0..1 | `Bonificacion` 0..n: `@BonificacionS?` `@BonificacionNS?` |
| `Auxilios` | 0..1 | `Auxilio` 0..n: `@AuxilioS?` `@AuxilioNS?` |
| `HuelgasLegales` | 0..1 | `HuelgaLegal` 0..n: `@FechaInicio?` `@FechaFin?` `@Cantidad` (unpaid) |
| `OtrosConceptos` | 0..1 | `OtroConcepto` 0..n: `@DescripcionConcepto` `@ConceptoS?` `@ConceptoNS?` |
| `Compensaciones` | 0..1 | `Compensacion` 0..n: `@CompensacionO` `@CompensacionE` |
| `BonoEPCTVs` | 0..1 | `BonoEPCTV` 0..n: `@PagoS?` `@PagoNS?` `@PagoAlimentacionS?` `@PagoAlimentacionNS?` |
| `Comisiones` | 0..1 | `Comision` 0..n (decimal) |
| `PagosTerceros` | 0..1 | `PagoTercero` 0..n (decimal) |
| `Anticipos` | 0..1 | `Anticipo` 0..n (decimal) |
| `Dotacion`, `ApoyoSost`, `Teletrabajo`, `BonifRetiro`, `Indemnizacion`, `Reintegro` | 0..1 each | decimal scalars |

**The `S` / `NS` suffix is the salary-constitutive flag** — `S` = *salarial* (forms part of salary,
therefore social-security base), `NS` = *no salarial*. This distinction drives IBC and is the most
common source of mapping error. It must come from the WTC classification, not be inferred.

## 4. `Deducciones`

`Salud` and `FondoPension` are both mandatory — **even at zero.** A document for an employee with
no health/pension deduction in the month still needs both nodes present.

| Node | Card. | Attributes / type |
|---|---|---|
| `Salud` | **1..1** | `@Porcentaje` `@Deduccion` |
| `FondoPension` | **1..1** | `@Porcentaje` `@Deduccion` |
| `FondoSP` | 0..1 | `@Porcentaje?` `@DeduccionSP?` `@PorcentajeSub?` `@DeduccionSub?` (solidarity fund + subsistence sub-account) |
| `Sindicatos` | 0..1 | `Sindicato` 0..n: `@Porcentaje` `@Deduccion` |
| `Sanciones` | 0..1 | `Sancion` 0..n: `@SancionPublic` `@SancionPriv` |
| `Libranzas` | 0..1 | `Libranza` 0..n: `@Descripcion` `@Deduccion` |
| `PagosTerceros` / `Anticipos` / `OtrasDeducciones` | 0..1 | 0..n decimal children |
| `PensionVoluntaria`, `RetencionFuente`, `AFC`, `Cooperativa`, `EmbargoFiscal`, `PlanComplementarios`, `Educacion`, `Reintegro`, `Deuda` | 0..1 each | decimal scalars |

## 5. CUNE — and a defect that will cost you a day

### Specification (Anexo §8.1.1.1)

```
CUNE = SHA-384( NumNE + FecNE + HorNE + ValDev + ValDed + ValTolNE
                + NitNE + DocEmp + TipoXML + Software-Pin + TipAmb )
```

`+` is string concatenation. Component sourcing:

| Component | XPath (NominaIndividual) | Format |
|---|---|---|
| `NumNE` | `/NominaIndividual/NumeroSecuenciaXML/@Numero` | Prefijo concatenated with Consecutivo |
| `FecNE` | `…/InformacionGeneral/@FechaGen` | `YYYY-MM-DD` |
| `HorNE` | `…/InformacionGeneral/@HoraGen` | time **including GMT offset** |
| `ValDev` | `/NominaIndividual/DevengadosTotal` | decimal point, **truncated** to 2 dp, no thousands separator, no currency symbol |
| `ValDed` | `/NominaIndividual/DeduccionesTotal` | as above |
| `ValTolNE` | `/NominaIndividual/ComprobanteTotal` | as above (= Devengado − Deducciones) |
| `NitNE` | `/NominaIndividual/Empleador/@NIT` | no dots, no dashes, **no check digit** |
| `DocEmp` | `/NominaIndividual/Trabajador/@NumeroDocumento` | no dots, no dashes, no check digit |
| `TipoXML` | `…/InformacionGeneral/@TipoXML` | `102` or `103` |
| `Software-Pin` | **not in the XML** — reserved secret from habilitación | see P2 §6 |
| `TipAmb` | `…/InformacionGeneral/@Ambiente` | `1` or `2` |

For the **Reemplazar** variant, substitute the `/NominaIndividualDeAjuste/Reemplazar/…` paths.

For the **Eliminar** variant the annex overrides three components with **literal constants**, since
a deletion note carries no monetary content and no `Trabajador` node:

```
ValDev = "0.00"   ValDed = "0.00"   ValTol = "0.00"   DocEmp = "0"
```

`EncripCUNE` is the algorithm identifier and takes the literal value **`CUNE-SHA384`**.

### ⚠ The published worked example does not reproduce

Anexo §8.1.1.3 supplies a complete input set — including the normally-secret PIN — and a published
result:

```
NumNE N00001 · FecNE 2020-01-16 · HorNE 10:53:10-05:00
ValDev 3500000.00 · ValDed 1000000.00 · ValTolNE 2500000.00
NitNE 700085371 · DocEmp 800199436 · TipoXML 102 · Pin 693 · TipAmb 1

published CUNE.SHA384 =
16560dc8956122e84ffb743c817fe7d494e058a44d9ca3fa4c234c268b4f766003253fbee7ea4af9682dd57210f3bac2
```

Hashing the specified concatenation gives:

```
SHA-384("N000012020-01-1610:53:10-05:003500000.001000000.002500000.007000853718001994361026931")
  = dae35b4dfdf10939502c96278feb97be1af6cd5653bd662ca29b5c9cdf2729464b51d272ba0008586cf153b46f87a2bd
```

Not a match. The annex's own printed concatenation string is *also* internally inconsistent — it
renders the hour as `1053:10-05:00`, dropping a colon — and that variant does not match either
(`b8f9b6c2…`).

**A 1,344-variant search was run** over: 7 hour formats (with/without GMT, with/without colons,
combined date-time), 4 document-number formats, zero-padded PIN, zero-padded `Ambiente`,
parenthesised and newline-terminated strings, and UTF-8 / UTF-16LE / Latin-1 encodings — plus
SHA-512/256/1/MD5 as algorithm alternatives. **No variant reproduces the published value.**

Two corroborating signals that the example, not the formula, is at fault: the annex cites
`http://www.sha1-online.com/` as its reference tool for a SHA-384 computation, and the same section
contains other transcription damage.

**Implications and mitigation.** Do not use §8.1.1.3 as a unit-test fixture — it will send you
hunting a bug that is not in your code. The formula itself is well specified and internally
consistent, and is corroborated by DIAN's own `SendNominaSync` sample response, whose
`XmlDocumentKey` is 96 hex characters — exactly SHA-384. The correct path is:

1. Implement to the formula as written.
2. Treat the CUNE as **empirically unverifiable until habilitación**. The habilitación environment
   is the oracle: submit and read back `XmlDocumentKey` (P4 §2).
3. Freeze the first accepted document as your golden fixture and regression-test against that.
4. Budget explicit habilitación iterations for CUNE convergence — reflected in the P6 schedule and
   the P5 risk register.

## 6. `SoftwareSC` (software security code)

```
SoftwareSC = SHA-384( SoftwareID + PIN + NroDocumento )
```

where `NroDocumento` = `…/NumeroSecuenciaXML/@Numero` (the `Reemplazar` or `Eliminar` path for
adjustment notes). Note this is **per document**, not a constant — it varies with the sequence
number, so it must be recomputed for every employee every month.

No worked example is published for `SoftwareSC`, so it carries the same
verify-at-habilitación status as the CUNE.

## 7. Code tables (Anexo §5)

**`Ambiente`** (§5.1.1) — `1` Producción · `2` Pruebas. Test-environment documents produce no legal
effect; production documents produce full tributary, financial, economic, commercial and
consumer-law effect.

**`EncripCUNE`** (§5.1.2) — literal `CUNE-SHA384`.

**`TipoDocumento`** (§5.2.1) — `11` Registro civil · `12` Tarjeta de identidad · `13` Cédula de
ciudadanía · `21` Tarjeta de extranjería · `22` Cédula de extranjería · `31` NIT · `41` Pasaporte ·
`42` Documento de identificación extranjero · `47` PEP · `50` NIT de otro país · `91` NUIP.
**`91` may be used only for the employee**, because NUIP is not a RUT document type.

**`PeriodoNomina`** (§5.5.1) — `1` Semanal · `2` Decenal · `3` Catorcenal · `4` Quincenal ·
`5` Mensual · `6` Otro. *This describes the employer's actual pay cycle; it does not change the
monthly transmission obligation (P1 §3).*

**`TipoContrato`** (§5.5.2) — `1` Término fijo · `2` Término indefinido · `3` Obra o labor ·
`4` Aprendizaje · `5` Prácticas o pasantías.

**`TipoTrabajador`** (§5.5.3) — 17 values: `01` Dependiente · `02` Servicio doméstico ·
`04` Madre comunitaria · `12` Aprendices SENA etapa lectiva · `18` Funcionarios públicos sin tope
máximo de IBC · `19` Aprendices SENA etapa productiva · `21` Estudiantes de postgrado en salud ·
`22` Profesor de establecimiento particular · `23` Estudiantes aportes solo riesgos laborales ·
`30` Dependiente entidades/universidades públicas con régimen especial en salud ·
`31` Cooperados o pre-cooperativas de trabajo asociado · `47` Trabajador dependiente de entidad
beneficiaria del SGP – aportes patronales · `51` Trabajador de tiempo parcial ·
`54` Pre-pensionado de entidad en liquidación · `56` Pre-pensionado con aporte voluntario a salud ·
`58` Estudiantes de prácticas laborales en el sector público.
**These are the PILA `tipo de cotizante` codes** — see INTERLINKAGES §3.

**`SubTipoTrabajador`** (§5.5.4) — `00` No aplica · `01` Dependiente pensionado por vejez activo.

**`Porcentaje`** for overtime/surcharge (§5.5.5) — the code *and* its mandated percentage:

| Code | Type | % |
|---|---|---|
| 1 | Hora extra diurna | 25.00 |
| 2 | Hora extra nocturna | 75.00 |
| 3 | Hora recargo nocturno | 35.00 |
| 4 | Hora extra diurna dominical y festivos | 100.00 |
| 5 | Hora recargo diurno dominical y festivos | 75.00 |
| 6 | Hora extra nocturna dominical y festivos | 150.00 |
| 7 | Hora recargo nocturno dominical y festivos | 110.00 |

> The XSD element names (`HED`, `HEN`, `HRN`, `HEDDF`, `HRDDF`, `HENDF`, `HRNDF`) map 1:1 onto codes
> 1–7 in that order. The `@Porcentaje` attribute carries the **percentage value**, not the code.
> Cross-check these seven rates against the CO CCG overtime section before go-live — the annex
> hard-codes 2021 statutory rates and any subsequent labour-law change makes the annex stale while
> the schema stays valid.

**`Tipo` de incapacidad** (§5.5.6) — `1` Común · `2` Profesional · `3` Laboral.

**`TipoXML`** (§5.5.7) — `102` NominaIndividual · `103` NominaIndividualDeAjuste.

**`TipoNota`** (§5.5.8) — `1` Reemplazar · `2` Eliminar. See §8.

**`Forma` de pago** (§5.3.3.1) — `1` Contado. **`Metodo` de pago** (§5.3.3.2) — the full UN/ECE 4461
payment-means list (~80 codes); in payroll practice `42` Consignación bancaria, `45` Transferencia
crédito bancario, `10` Efectivo and `20` Cheque cover essentially all cases.

**Geography** — `Pais` ISO 3166-1 alpha-2; `DepartamentoEstado` ISO 3166-2:CO numeric; `MunicipioCiudad`
DANE 5-digit municipal code (annex §5.4 carries the full table, e.g. `76`/`76001` Valle del Cauca /
Cali). `Idioma` ISO 639-1 two-letter. `TipoMoneda` ISO 4217; `TRM` required only when the currency is
not COP.

## 8. `NominaIndividualDeAjuste` (adjustment notes)

```
NominaIndividualDeAjuste  @SchemaLocation
├── ext:UBLExtensions       0..1
├── TipoNota                1..1        1 = Reemplazar, 2 = Eliminar
├── Reemplazar              0..1
│   ├── ReemplazandoPredecesor  1..1    ← identifies the document being replaced
│   └── (full NominaIndividual payload: Periodo … ComprobanteTotal)
└── Eliminar                0..1
    ├── EliminandoPredecesor    1..1
    ├── NumeroSecuenciaXML, LugarGeneracionXML, ProveedorXML,
        CodigoQR, InformacionGeneral, Notas, Empleador
```

- **Reemplazar** (code 1) — for arithmetic, accounting or content errors. Carries a **complete
  restatement** of the payload, not a delta. There is no partial-amendment mechanism.
- **Eliminar** (code 2) — for documents transmitted in error. Carries only the header block: **no
  `Trabajador`, no `Devengados`, no `Deducciones`, no totals**. That is precisely why the CUNE
  formula substitutes constants for those components (§5).
- Per Res. DIAN 000227 de 2025 art. 1.5.3.5.1.9, the note must reference the number and the CUNE-generation date of the document
  it adjusts, and carry its own internal consecutive number.
- Deletion **invalidates but does not remove**: the annex states the original documents continue to
  exist in DIAN's database, flagged with the deletion. Retention obligations therefore still apply.

## 9. Numbering, rounding and sign conventions

- **Numbering** (`NumeroSecuenciaXML`): `@Prefijo` + `@Consecutivo`, with `@Numero` carrying the
  concatenation. Unlike e-invoicing, **there is no DIAN-authorised numbering range** for payroll —
  `GetNumberingRange` is an e-invoicing operation and is out of scope (P2 §2). The consecutive is
  the issuer's own internal series. Adjustment notes carry their own separate series (art. 1.5.3.5.1.9 num. 2).
- **Uniqueness** — global rule **90**: a document number may be transmitted **only once per
  worker**. Re-sending is rejected as "Documento procesado anteriormente", not treated as
  idempotent. See P5 §3 — this is the most important operational consequence in the whole
  integration.
- **Rounding** (Anexo §1.1.1) — monetary values to 2 decimal places; the CUNE inputs are
  **truncated**, not rounded, to 2 dp. The optional `Redondeo` element carries an explicit rounding
  adjustment so that `DevengadosTotal − DeduccionesTotal = ComprobanteTotal` holds exactly.
- **Signs** (Anexo §1.1.3, rule `VLR01`) — all monetary values and percentages **must be positive**.
  A negative net (deductions exceeding accruals) cannot be expressed as a negative
  `ComprobanteTotal`; it must be resolved in the payroll engine before document generation.
- **Time worked** (`@TiempoLaborado`, Anexo §8.3.1) — expressed in days on a **commercial calendar**:
  1 year = 360 days, 1 month = 30 days. Worked example: 5 years + 3 months + 18 days →
  (5 × 360) + (3 × 30) + 18 = **1908**.

## 10. Reference instances — what is and is not available

The toolkit's `Ejemplificaciones/` folder contains two XML files, and it is important to understand
what they are not.

They are **structural skeletons, not worked examples**. Every string attribute is `"A"`, every
numeric is `0`, every date is `9999-12-31`, and — critically — `<ext:UBLExtensions>` is **empty**,
carrying no `ds:Signature` at all.

Consequence: **DIAN publishes no signed reference instance.** The XAdES-EPES profile — canonicalisation
choice, reference set, transform order, `SignaturePolicyId` hash, `SigningCertificate` digest — cannot
be validated byte-for-byte against a known-good artefact before habilitación. Combined with the
unverifiable CUNE (§5), this means **two of the three cryptographic controls in this integration have
no offline oracle.** Both must be resolved empirically in habilitación, which is why P6 allocates
iteration budget rather than a single certification pass, and why P5 flags signature rejections as
the highest-likelihood early failure mode.

The skeletons remain useful for exactly one purpose: confirming element order and namespace
declarations, since XSD sequence order is strict.

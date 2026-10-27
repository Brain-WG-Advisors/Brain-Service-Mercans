# INTERLINKAGES — DIAN-NE

How DIAN-NE depends on the CO payroll engine, and how it relates to Colombia's other three
payroll-data authorities. **Cross-reference only** — no runbooks exist for the other three, because
all three carry `integration: false`.

---

## 1. Position in the CO landscape

| Authority | Integration | Channel | Runbook |
|---|---|---|---|
| **DIAN-NE** | **true** | M2M SOAP 1.2 (`SendNominaSync`) | **this folder** |
| DIAN-MUISCA | false | Portal round-trip (Muisca + IFE) | none |
| PILA-OI | false | Private *operador de información* portal / file upload | none |
| FONDOS-CESANTIAS | false | *Operador de información* portal / file upload | none |

**DIAN-NE is Colombia's only machine-to-machine payroll statutory channel.** Everything else is a
portal round-trip. That asymmetry is the most important planning fact in the country: engineering
effort concentrates entirely here, while the operational-risk exposure sits mostly in the other
three (see §5).

## 2. Upstream dependencies on the CO payroll engine

DIAN-NE consumes the payroll result. These are the engine-side capabilities it *requires* — several
are not needed by any other CO filing, so they will not exist unless built deliberately.

**(a) Monthly accumulation across sub-monthly cycles — the big one.**
Res. art. 3 mandates one document per employee per month *regardless of pay frequency*. A client
paying weekly, decenal, catorcenal or quincenal (`PeriodoNomina` 1–4) needs the month's liquidations
**aggregated** into a single document. This is an active transformation, not a pass-through, and it
is the single most likely source of a systematic defect. It also interacts with mid-month starters
and leavers. Flagged as the highest-risk archetype in the P6 §6 coverage matrix.

**(b) Salary-constitutive (`S`) vs non-constitutive (`NS`) classification.**
`Bonificacion`, `Auxilio`, `OtroConcepto`, `BonoEPCTV` and `Primas` all carry paired `S`/`NS`
attributes (P3 §3). This must come from the **WTC** classification (`02-wtc/`). It must not be
inferred from wage-type naming, and it must be consistent with the IBC used for PILA — see §3.

**(c) Concept-level granularity.**
The schema wants concepts, not a net figure: seven distinct overtime/surcharge buckets, vacation
split common/compensated, three incapacity types, three licence types, `Cesantias` with interest,
`FondoSP` split into solidarity and subsistence sub-accounts. If the engine stores only aggregated
totals, DIAN-NE cannot be populated. Reconcile the schema's leaf set against `02-wtc/` and
`05-data-dictionary/` early — this is a data-model question, not a mapping question.

**(d) Identifiers and reference data.**
`Empleador/@NIT` + `@DV`; `Trabajador/@TipoDocumento` + `@NumeroDocumento`; DANE department/municipality
codes for both employer and place of work; ISO 3166-1 alpha-2, ISO 639-1, ISO 4217.

**(e) A durable document-numbering series.**
`Prefijo` + `Consecutivo`, transactional, per issuer, unique per worker (rule 90 — P5 §3). Adjustment
notes need their own separate series (Res. art. 17). Note this is *not* a DIAN-authorised range:
unlike e-invoicing there is no `GetNumberingRange` for payroll (P3 §9).

**(f) Exact totals reconciliation.**
`DevengadosTotal − DeduccionesTotal = ComprobanteTotal`, with `Redondeo` available to absorb rounding.
All values positive (`VLR01`).

**(g) 360-day service-time convention.**
`@TiempoLaborado` uses 1 year = 360 days, 1 month = 30 days (P3 §9).

## 3. Relationship to PILA-OI — the reconciliation that should exist

PILA and DIAN-NE are the two monthly payroll obligations, and they are **not connected by any
system** — but they describe the same facts.

- **`TipoTrabajador` is the PILA `tipo de cotizante` code set** (17 values, P3 §7). The same
  classification feeds both. A worker typed one way in PILA and another way in DIAN-NE is
  internally inconsistent and visible to UGPP.
- The `S`/`NS` split (§2b) determines the **IBC** reported to PILA and the salary-constitutive
  amounts in DIAN-NE. These must agree.
- `Salud` and `FondoPension` deductions appear in DIAN-NE; the corresponding contributions are
  settled through PILA.
- `AltoRiesgoPension` and `SalarioIntegral` affect both.

**Recommendation:** build a monthly DIAN-NE ↔ PILA reconciliation, even though neither authority
requires one. **UGPP** is an enforcement and audit body that receives no periodic filing but *does*
cross-examine — and DIAN-NE, being structured, signed, per-employee and permanently retained, is the
most machine-readable description of Colombian payroll that exists. Divergence between the two is
exactly the signal an audit looks for. The reconciliation is cheap to build alongside the DIAN-NE
run and is the highest-value optional item in the CO programme.

Note the deadline mismatch: DIAN-NE is due by the **10th**; PILA is due on the **2nd–16th business
day** by NIT last-two-digits. They will not land on the same day.

## 4. Relationship to DIAN-MUISCA — same authority, different posture

Same legal entity, entirely separate channel. The electronic-payroll web service **does not carry**
Form 350 (monthly withholding return), Formato 2276 (annual employment-income información exógena)
or Form 220 (income-and-withholding certificate). Those go through Muisca with the DIAN-issued
Instrumento de Firma Electrónica (IFE).

Two consequences worth stating plainly:

- **Do not attempt to reuse the DIAN-NE certificate or endpoint for Muisca filings.** Different
  credential (ONAC-accredited X.509 vs DIAN-issued IFE), different channel, no overlap.
- **Beware commercial "DIAN API" offerings.** The landscape research found that vendor products
  marketed as DIAN APIs are commercial wrappers around this same e-invoicing/payroll SOAP service.
  They are not authority-published, and they do **not** cover Form 350 or exógena. Do not model them
  as a statutory channel.

There is a genuine data relationship though: `RetencionFuente` reported per employee in DIAN-NE and
the aggregate withholding declared on Form 350 describe the same withholding. Worth reconciling
monthly for the same audit-consistency reason as §3.

## 5. Where the risk actually sits

DIAN-NE carries the **engineering** effort. It does not carry the largest **operational** risk.

**FONDOS-CESANTIAS** does: annual severance deposit by **14 February** (Ley 50/1990 art. 99 num. 3),
where late deposit costs **one day's salary per day of delay, per employee, uncapped**. There is no
integration to build and therefore no runbook — but that is precisely the problem. A manual,
once-a-year, uncapped-penalty process with no system support is the most expensive failure mode in
the Colombian payroll year. For accrual year 2026 the deadline falls on Sunday 14 February 2027, so
the operative date is **Friday 12 February 2027**.

Flagging it here because a reader of this runbook set could otherwise conclude that "the integration
work is DIAN-NE" means "the risk is DIAN-NE". It does not. Delivery planning should carry
FONDOS-CESANTIAS as a tracked manual control with calendar alerting, notwithstanding the absence of
a runbook.

## 6. Pipeline cross-references

| Artefact | Relationship |
|---|---|
| `01-ccg/CO-CCG-001` | Statutory rules behind the amounts. **Overtime percentages (P3 §7) must be cross-checked against it** — the annex hard-codes 2021 rates. |
| `02-wtc/` | Wage-type catalogue → source of truth for `S`/`NS` and concept mapping (§2b, §2c) |
| `04-reports-spec/` | `CO-DIAN-NE-MONTHLY-001` is the filing this integration carries |
| `05-data-dictionary/` | Field-level definitions feeding the 262-carrier document (P3 §1) |
| `06-payslip/` | Same concept set, different presentation; the payslip and DIAN-NE should not disagree on a concept's classification |
| `integration-landscape.json` | Discovery output; verdict `HAS_INTEGRATIONS` |
| `CO-SIR-INDEX-001-v1.0.docx` | Index across all four authorities |

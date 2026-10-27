# P5 — Validation Rules & Error Handling

**CO / DIAN-NE** · Anexo Técnico §6 (rules) + Res. 000013/2021 arts. 13, 14, 17

---

## 1. Rule inventory

The annex publishes **433 individually identified validation rules**, machine-counted from the rule
tables (annex pp. 182–231), plus three global rules. This is the dominant scope driver in the build
— see `effort-estimates.md`.

| Prefix | Applies to | Rejection (R) | Notification (N) | Total |
|---|---|---|---|---|
| `NIE` | `NominaIndividual` | 187 | 9 | **196** (+ `NIE901`) |
| `NIAE` | `NominaIndividualDeAjuste` | 219 | 18 | **237** |
| **Total** | | **406** | **27** | **433** |

Plus three global rules stated separately in §6:

| ID | Y | Condition | Message |
|---|---|---|---|
| **90** | R | A document number may be transmitted **only once per worker** | *Documento procesado anteriormente* |
| **92** | R | Issuer must be **enabled** on the electronic-payroll platform (both document types) | *El Emisor del Documento no se encuentra Habilitado en la Plataforma* |
| **VLR01** | R | Monetary values and percentages must be **positive** | *Los valores monetarios/porcentajes deben corresponder a valores positivos* |

The adjustment-note schema carries **41 more rules** than the base document (237 vs 196), which is
counter-intuitive and worth planning for: notes are not a lighter-weight path. They re-validate the
entire restated payload *and* add predecessor-linkage checks.

## 2. R / N semantics

From annex §6:

- **`R` = rechazo (rejection).** A document receives the "validado" seal **only if it fails no `R`
  rule**.
- **`N` = notificación.** A document can be sealed "validado" **regardless of how many `N` rules it
  fails**.

Message format is the concatenation of ID, verdict and text:

```
NIE022 – (R) Debe ir el literal: "V1.0: Documento Soporte de Pago de Nómina Electrónica"
NIE013 – (R) Se debe colocar el Codigo alfa-2 correspondiente
```

Parse `ErrorMessage[]` into `(id, verdict, text)` with a regex on that shape, and key your
remediation catalogue on the **ID**, not the message text. The text is Spanish prose, contains
inconsistent spacing and accents, and is the part most likely to change between annex versions.

**Do not discard `N` messages.** They pass validation today but signal data-quality drift, and DIAN
has historically promoted notification rules to rejection rules in later annex versions of the
sibling e-invoicing regime. Log them, trend them, and treat a rising `N` count as a leading
indicator. See P7 §4.

Where the same element occurs in several places, the message includes the full XPath — the rule
tables mark these with `<Xpath>` in the message column. Where one element can fail several ways,
the ID is suffixed with a letter (`a`, `b`, …). Your catalogue key must therefore be the full ID
string, not a parsed integer.

## 3. Rule 90 — the operational constraint that shapes everything

> *Solo se podrá transmitir una única vez el Número del documento para el trabajador.*

**The transmission is not idempotent.** This single rule drives four design decisions:

1. **No blind retries.** A timeout is not a licence to resend. Disambiguate with `GetStatus`
   (P4 §5) before any resubmission.
2. **Rejected documents burn their number.** After an `R` failure, correct and resubmit under a
   **new `Consecutivo`** for the same worker and period. Do not reuse the number.
3. **The consecutive series must be durable and gap-tolerant.** Allocate from a persistent,
   transactional sequence — never from an in-memory counter or a row count. Gaps are expected and
   acceptable; collisions are fatal.
4. **Concurrency control is required.** Parallel workers processing the same employee-month must
   not both allocate. Since volume is one call per employee (P1 §3), parallelism is the natural
   throughput strategy, and this is where it bites.

## 4. Failure taxonomy and remediation

| Layer | Detected by | Typical cause | Remediation |
|---|---|---|---|
| **Container** | DIAN, pre-schema | Empty ZIP, corrupt ZIP, >1 entry, >500 KB, non-UTF-8 | Fix packaging (P2 §5). No number consumed if rejected before registration — confirm with `GetStatus`. |
| **Signature** | DIAN | Missing `ds:Signature`, SHA-1 digest, bad `SignaturePolicyId` hash, wrong `ClaimedRole`, expired certificate | Fix signing config (P2 §4). **Highest-likelihood early failure** — no signed reference instance exists (P3 §10). |
| **Schema** | DIAN | Element order, missing required attribute, wrong datatype | Fix mapper. XSD sequence order is strict — validate locally against the v1.0.6 XSD first. |
| **Business (`R`)** | DIAN, 406 rules | Bad code-table value, totals not reconciling, negative value, date inconsistency | Fix source data or mapping; resubmit under a new consecutive. |
| **Business (`N`)** | DIAN, 27 rules | Data-quality warnings | Document validates. Log and trend. |
| **Global 90** | DIAN | Number reuse | Allocate a new consecutive (§3). |
| **Global 92** | DIAN | Issuer not enabled | Habilitación incomplete — P6. Blocks **all** traffic, not one document. |
| **`VLR01`** | DIAN | Negative amount or percentage | Resolve in the payroll engine before generation (P3 §9). |

**Validate locally before transmitting.** Everything in the container, signature and schema layers
is detectable offline with the shipped XSDs and a XAdES verifier. Given that each rejected
transmission consumes a document number, a local pre-flight gate is not an optimisation — it is
part of the correctness design.

## 5. Statutory contingency — the 48-hour rules

Res. 000013/2021 provides two symmetric contingency windows. Both matter for retry policy, because
they define the legal deadline that your backoff must respect.

**Art. 13 — DIAN-side technological problems.** Where DIAN's service is unavailable and prevents
transmission, the obligated party must transmit **within a maximum of 48 hours counted from the day
following restoration** of the electronic service.

**Art. 14 — issuer-side technological problems.** Where the obligated party's own systems prevent
transmission, the same **48 hours from the day following** the problem being overcome applies.

Design consequences:

- Retry/backoff may extend across days; it must not silently exhaust and drop a document.
- **Log outage windows.** The 48-hour clock starts from restoration, so the compliance position
  depends on evidence of when the outage began and ended. Capture start, end, and the observed
  error, per tenant.
- A document caught by contingency is still late against the art. 8 ten-day deadline unless the
  contingency is evidenced. Alerting must distinguish *outage* from *engine failure* — they have
  different legal consequences.

## 6. Correction flow

Two distinct situations, often conflated:

**A — Rejected (never validated).** No valid document exists. Fix and submit a **new
`NominaIndividual`** under a new consecutive. Do **not** issue an adjustment note: there is nothing
to adjust.

**B — Validated but wrong.** A valid document exists and must be corrected via a
`NominaIndividualDeAjuste`:

- `TipoNota = 1` (**Reemplazar**) — arithmetic, accounting or content errors. Carries a **complete
  restatement**, plus `ReemplazandoPredecesor`. There is no partial amendment.
- `TipoNota = 2` (**Eliminar**) — document transmitted in error. Header-only; `EliminandoPredecesor`
  identifies the target. Per the annex, deletion **invalidates but does not remove** — the original
  persists in DIAN's database flagged as deleted, so retention still applies.

Per art. 17 the note must carry its own internal consecutive number and reference the number and
the CUNE-generation date of the document it adjusts. Notes are themselves subject to the art. 8
deadline.

Adjustment notes re-run the full 237-rule `NIAE` set (§1) — a note can itself be rejected, and then
needs its own new consecutive.

## 7. Risk register

| # | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| 1 | **CUNE composition wrong**; published example unverifiable (P3 §5) | High | High | Converge in habilitación against `XmlDocumentKey`; permanent production assertion (P4 §2) |
| 2 | **XAdES profile wrong**; no signed reference instance published (P3 §10) | High | High | Budget habilitación iterations; verify with an independent XAdES validator |
| 3 | **Auth model misread** — mutual TLS vs message-level (P2 §3) | Medium | Medium | Build to the WSDL; test both in habilitación; same certificate serves either |
| 4 | **Rule-90 collision** from retry-on-timeout | Medium | High | `GetStatus`-before-resubmit; transactional consecutive allocation |
| 5 | `S`/`NS` salary-constitutive misclassification (P3 §3) | Medium | High | Drive from WTC, never infer; reconcile against PILA IBC (INTERLINKAGES §3) |
| 6 | Overtime percentages in annex go stale vs labour law (P3 §7) | Medium | Medium | Cross-check the seven rates against the CO CCG each year |
| 7 | Throughput at high headcount — one call per employee | Medium | Medium | Parallelism + rate-limit discovery in habilitación (P7 §2) |
| 8 | Certificate expiry mid-cycle | Low | High | Expiry monitoring with lead time (P7 §4) |
| 9 | Annex superseded by a new version | Low | Medium | Version watch on the micrositio (P7 §4) |

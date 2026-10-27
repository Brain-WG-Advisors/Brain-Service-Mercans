# Effort Estimates — DIAN-NE

Engineering effort to build, certify and operate the Colombian electronic-payroll integration.
Estimates are in **person-days** for one experienced integration engineer familiar with SOAP and
XML signing but new to DIAN. They assume the CO payroll engine already produces correct payroll
results — DIAN-NE consumes payroll, it does not compute it.

**Basis:** all artefacts are in hand (P1 §7), so there is **no discovery or artefact-chasing
effort** in these numbers. That is a material saving over a typical statutory integration and is
already reflected below.

---

## Summary

| Phase | Deliverable | Low | Likely | High |
|---|---|---|---|---|
| P1 | Authority profile, scope confirmation | 1 | 2 | 3 |
| P2 | Connectivity, WS-Security, XAdES-EPES signing | 6 | 10 | 18 |
| P3 | Payload mapping, code tables, CUNE, `SoftwareSC` | 12 | 18 | 28 |
| P4 | Response handling, `ApplicationResponse`, persistence | 4 | 6 | 9 |
| P5 | Validation-rule catalogue, error handling, correction flow | 8 | 13 | 20 |
| P6 | Habilitación, test matrix, certification | 8 | 14 | 25 |
| P7 | Operations, monitoring, scheduling | 4 | 6 | 9 |
| | **Build total** | **43** | **69** | **112** |
| | Project management, review, documentation (~15%) | 6 | 10 | 17 |
| | **TOTAL** | **49** | **79** | **129** |

**Plan to ≈ 79 person-days (~16 weeks at 1 FTE).** The high case is not a padding exercise — it is
what happens if the two unverifiable cryptographic controls (§"Risk loading") each take several
habilitación cycles to converge.

## Drivers by phase

### P2 — Connectivity & security · 10 d
The WSDL is standard WCF and a client generates cleanly, so transport is cheap. Cost is
concentrated in **XAdES-EPES signing**: signature policy identifier, `SigningCertificate` digest,
`ClaimedRole`, correct canonicalisation and reference set. Add the thumbprint-reference requirement
(`sp:RequireThumbprintReference`) which several SOAP stacks do not do by default.

Loaded by: no signed reference instance exists to diff against (P3 §10), and the auth model is
ambiguous between the annex and the WSDL (P2 §3). Both are resolved empirically in P6, not here —
which is why P2 can finish "done" and still be wrong.

### P3 — Payload mapping · 18 d · **largest single item**
262 field carriers in the base document, 312 in the adjustment note (P3 §1). Drivers:

- **Concept-level mapping** — seven overtime buckets, three incapacity types, three licence types,
  `S`/`NS` pairs across five accrual families, `FondoSP` two-sub-account split.
- **Monthly accumulation** across sub-monthly pay cycles (INTERLINKAGES §2a) — a real
  transformation, not a mapping, and the one most likely to need rework.
- **Code tables** — 17 `TipoTrabajador`, 11 `TipoDocumento`, 5 `TipoContrato`, 6 `PeriodoNomina`,
  ~80 `Metodo` de pago, full DANE municipality set, ISO 3166-2:CO.
- **CUNE and `SoftwareSC`** — trivial to code, but see risk loading.
- **Attribute-centric design** — most data is in attributes, which trips mappers written for
  element-per-field.

### P5 — Validation rules · 13 d
**433 published rules** (406 rejection, 27 notification) plus three global rules. The estimate is
*not* for reimplementing all 433 — DIAN enforces them server-side. It covers:

- A remediation catalogue keyed on rule ID (~2–3 d to transcribe and classify the tables).
- Local pre-flight validation for the container/signature/schema layers, which is genuinely
  worthwhile because every rejection consumes a document number (rule 90).
- The **rule-90 non-idempotency design**: transactional consecutive allocation,
  `GetStatus`-before-resubmit, concurrency safety. This is small in code and large in consequence.
- Correction flow: rejected-vs-validated branching, Reemplazar/Eliminar notes (P5 §6).

### P6 — Habilitación · 14 d · **highest variance**
Split roughly: 3 d administrative (RUT, art. 22 mandate, software registration, certificate
procurement lead time is *elapsed*, not effort), 3 d test-harness build, **8 d convergence**.

The convergence figure is the honest one. Two of three cryptographic controls have no offline
oracle (P6 §4), so this phase is a loop, not a gate. If CUNE and signature both land first time,
this is 6 d; if both need several cycles, 25 d.

### P4, P7 · 6 d each
Response parsing is a small, well-specified type. Persistence and retention are straightforward
once the byte-exactness requirement is understood. Operations is scheduling, monitoring and
alerting on a monthly cycle.

## Risk loading

The three items that move the estimate, in order:

1. **CUNE unverifiable offline** (P3 §5). The published worked example does not reproduce across a
   1,344-variant search. The natural unit-test fixture is unusable. **+0 to +5 d**, and it lands in
   P6 where it is most expensive because each iteration is a round trip.
2. **No signed reference instance** (P3 §10). The XAdES-EPES profile cannot be validated
   byte-for-byte before habilitación. **+0 to +6 d.**
3. **Auth model ambiguity** (P2 §3). Message-level vs mutual TLS. Cheap to test both since one
   certificate serves either. **+0 to +2 d.**

Secondary: throughput at high headcount (one synchronous call per employee, no published rate
limit) may force a scheduling redesign after the P6 §5 step-13 probe — **+0 to +4 d**.

## Per-tenant onboarding (recurring, after the build)

| Activity | Effort |
|---|---|
| RUT / art. 22 mandate / software registration | 1–2 d (mostly elapsed, client-dependent) |
| Certificate procurement from an ONAC-accredited CA | 0.5 d effort, **1–3 weeks elapsed** |
| Habilitación test set for the tenant | 1–3 d |
| Client-specific coverage matrix (P6 §6) | 1–2 d |
| **Per tenant** | **4–8 d**, with certificate lead time on the critical path |

Start certificate procurement at engagement kick-off. It is the longest pole and it is pure
waiting.

## Steady-state run cost

| Activity | Frequency | Effort |
|---|---|---|
| Monthly run monitoring + exception handling | monthly | 0.5–2 d per tenant, scaling with headcount and data quality |
| Adjustment notes | as needed | included above |
| Certificate renewal | ~annual | 0.5 d + procurement lead time |
| Annex/WSDL version watch (P7 §6) | quarterly | 0.25 d, all tenants |
| Overtime-rate cross-check vs CCG | annual | 0.25 d |

## What is *not* in these numbers

- Payroll computation itself (CCG/WTC scope).
- The other three CO authorities — all manual, no runbooks. Note in particular that
  **FONDOS-CESANTIAS carries the largest operational risk in the CO year** despite requiring zero
  integration effort (INTERLINKAGES §5); it needs a tracked manual control, not engineering days.
- The DIAN-NE ↔ PILA reconciliation recommended in INTERLINKAGES §3 — **+3 to 5 d** if adopted.
  Recommended: it is the highest-value optional item in the CO programme.

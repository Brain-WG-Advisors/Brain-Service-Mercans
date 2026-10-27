# P6 — Test & Certification (Habilitación)

**CO / DIAN-NE** · Res. 000013/2021 arts. 9, 22 · Anexo Técnico §9.2.1, §14

---

## 1. What habilitación is

**Habilitación** is DIAN's enablement procedure (Res. art. 9). It is a **portal-based, one-time,
per-issuer administrative process** — it is not part of the transmission path and it is not a
technical channel. Once complete, all traffic is unattended machine-to-machine.

Its enforcement point in the runtime is blunt: **global rule 92 rejects every document from a
non-enabled issuer**. Habilitación is therefore a hard go-live gate for the tenant, not a
nice-to-have. It blocks all traffic, not individual documents.

**This is the one genuinely gated item in the whole integration.** Everything technical is public
and downloaded (P1 §7). What cannot be obtained in advance is the *output* of habilitación:

| Item | Nature | Why it cannot be pre-obtained |
|---|---|---|
| `SoftwareID` | Identifier | Issued by DIAN against a named registered software, per taxpayer |
| Software **PIN** | Secret | Chosen by the issuer in the DIAN portal at activation |
| ONAC-accredited X.509 certificate | Credential | Purchased from an accredited CA against a legal entity's identity |
| Production enablement flag | Authority state | Set by DIAN on completion of the test set |

These are **per-tenant credentials, not artefacts**, and they require an authenticated portal
session by the taxpayer or its representative. Consistent with the research constraints, no login
was attempted and no account was created.

## 2. Prerequisites checklist

**Legal / administrative**

- [ ] Taxpayer registered in the **RUT** with the appropriate responsibility codes.
- [ ] Where Mercans generates or transmits on the client's behalf (Res. **art. 22**):
  - [ ] The third party is **previously enabled by DIAN**, per ET arts. 572–573.
  - [ ] That capacity is **registered in the RUT** (art. 22 transitional paragraph, effective once
        DIAN completes the necessary system changes).
  - [ ] **Both parties retain the mandate document** evidencing the arrangement, for the statutory
        period.
- [ ] Decision recorded: **own software** vs **proveedor tecnológico** registration. This changes
      who holds the `SoftwareID`/PIN and whose certificate signs, and it changes the
      `ClaimedRole` in the XAdES signature (`supplier` vs `thirdparty` — P2 §4).

**Technical**

- [ ] X.509 certificate from an **ONAC-accredited** CA, installed in a keystore/HSM.
- [ ] Egress to `vpfe-hab.dian.gov.co:443` allow-listed.
- [ ] Local XSD validation against `NominaIndividual…V1.0.6.xsd` passing.
- [ ] Local XAdES-EPES signing implemented and independently verifiable.
- [ ] CUNE and `SoftwareSC` implemented to the formulae (P3 §5, §6).
- [ ] NTP-synchronised clock (P2 §7).

## 3. Test environment

| | |
|---|---|
| Endpoint | `https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc` |
| WSDL | `https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc?singleWsdl` |
| `Ambiente` in payload | **`2`** (Pruebas) |
| Legal effect | **None.** Annex §5.1.1: test-environment documents produce no effect of any kind. |

The habilitación WSDL is **byte-identical to production apart from the hostname** (verified
2026-09-04 by normalised diff — see P1 §5). There is no separate contract, no test-only operation,
and no schema divergence to accommodate. A single client implementation targets both; environment
is a configuration value in two places (host + `Ambiente`), and they must agree.

Annex §9.2.1 confirms the service is available in "los ambientes de producción (Habilitación y
Operación)".

## 4. Why this phase needs iteration budget, not a single pass

Two of the three cryptographic controls in this integration have **no offline oracle**:

1. **The CUNE** — the only published worked example does not reproduce, across a 1,344-variant
   search (P3 §5).
2. **The XAdES-EPES signature** — the shipped sample XMLs are skeletons with an **empty**
   `ext:UBLExtensions` and no `ds:Signature` at all (P3 §10). No signed reference instance exists.

The third, `SoftwareSC`, has no worked example either.

The practical consequence: **habilitación is where these are proven, not where they are
confirmed.** Plan it as a convergence loop with several cycles, not as a certification event.
Specifically:

- Treat the first accepted document as the golden fixture and freeze it for regression.
- Compare computed CUNE against returned `XmlDocumentKey` on **every** habilitación submission
  (P4 §2), and keep that assertion in production.
- Resolve the authentication ambiguity (P2 §3) here: try message-level WS-Security first; if the
  handshake is refused, add the TLS client certificate. The same certificate serves both, so the
  experiment is cheap.

## 5. Test sequence

| Step | Action | Success criterion |
|---|---|---|
| 1 | Retrieve the habilitación WSDL; generate the client | Client builds; only `SendNominaSync` + `GetStatus` exposed (P2 §2) |
| 2 | Connectivity smoke test with WS-Security header | No transport/security fault |
| 3 | Submit one minimal valid `NominaIndividual` (`Ambiente=2`) | `IsValid=true`, `StatusCode=00` |
| 4 | **Assert computed CUNE == `XmlDocumentKey`** | Exact match — *the key checkpoint* |
| 5 | Decode and validate the returned `ApplicationResponse`; confirm `ResponseCode=02` | Signed response parses |
| 6 | `GetStatus` on that CUNE | Status returned and consistent |
| 7 | Deliberate rejection (e.g. bad code-table value) | `IsValid=false`; `ErrorMessage[]` parses to `(ID, R, text)` |
| 8 | Resubmit the **same** document number for the same worker | Rejected with **rule 90**, confirming non-idempotency (P5 §3) |
| 9 | Corrected resubmission under a **new consecutive** | `IsValid=true` |
| 10 | `NominaIndividualDeAjuste` `TipoNota=1` (Reemplazar) over a validated document | `IsValid=true`; predecessor linkage accepted |
| 11 | `NominaIndividualDeAjuste` `TipoNota=2` (Eliminar) | `IsValid=true`; header-only payload accepted |
| 12 | Coverage sweep across employee archetypes (§6) | All accepted |
| 13 | Volume/throughput probe at expected peak concurrency | No rate-limiting or degradation; record observed limits for P7 §2 |
| 14 | DIAN test set for enablement | Production enablement granted |

Steps 8 and 9 are worth running deliberately even though they produce a failure: rule-90 behaviour
is the single most consequential runtime constraint (P5 §3) and confirming it empirically is
cheaper than discovering it in a production month-end.

## 6. Coverage matrix

Exercise at minimum one document per archetype — these are the combinations most likely to expose
mapping defects:

- **Contract types** — all five `TipoContrato` values (1–5).
- **Worker types** — at least `01` Dependiente, plus every `TipoTrabajador` present in the client's
  population (17 possible; these are the PILA cotizante codes — INTERLINKAGES §3).
- **`SalarioIntegral`** true and false.
- **`AltoRiesgoPension`** true and false.
- **All seven overtime/surcharge types** (`HED`…`HRNDF`), including the `@Porcentaje` values.
- **`S` vs `NS`** salary-constitutive variants on `Bonificacion`, `Auxilio`, `OtroConcepto`,
  `BonoEPCTV`, `Primas` — the highest-risk mapping area (P5 §7 risk 5).
- **Absence types** — `Incapacidad` types 1/2/3; `LicenciaMP`, `LicenciaR`, `LicenciaNR`
  (remember `LicenciaNR` has **no** `@Pago`).
- **Terminations** — `Periodo/@FechaRetiro` populated, with `Indemnizacion`, `BonifRetiro`,
  `Cesantias`, `VacacionesCompensadas`.
- **New starters** mid-month; `@TiempoLaborado` on the 360-day convention (P3 §9).
- **Sub-monthly pay cycles** — `PeriodoNomina` 1/2/3/4 accumulated into one monthly document
  (P1 §3). *This is the archetype most likely to be wrong, because it is the one the payroll engine
  has to actively aggregate rather than pass through.*
- **`Redondeo`** exercised so `Devengados − Deducciones = ComprobanteTotal` holds exactly.
- **Non-COP currency** with `TRM` populated, if in scope for the client.

## 7. Tooling

Annex **§14** is a SOAP UI walkthrough: create a SOAP project from the WSDL (§14.4), configure the
**Keystore** (§14.6), **WS-Security Signature** (§14.7) and **Timestamp** (§14.8), then WS-A
addressing (§14.9).

Use it for the *security configuration*, which is where it is genuinely helpful and which
corroborates the message-level reading of the auth model (P2 §3). **Ignore its request examples** —
§14.10–14.12 still show `GetStatus` and `SendBillAsync` inherited verbatim from the e-invoicing
annex, and were never updated for payroll (P1 §8 defect 4).

## 8. Go-live gate

- [ ] All §5 steps passed, including the deliberate rule-90 test.
- [ ] §6 coverage matrix complete for the client's actual population.
- [ ] CUNE assertion (computed == `XmlDocumentKey`) green across the full matrix.
- [ ] Golden fixture frozen; regression suite runs in CI.
- [ ] Authentication model settled and documented (P2 §3 resolved empirically).
- [ ] DIAN production enablement confirmed — otherwise **rule 92 blocks everything**.
- [ ] Art. 22 mandate document executed and retained by both parties.
- [ ] Production certificate installed; expiry monitoring live (P7 §4).
- [ ] `Ambiente` flipped to `1` **and** endpoint switched to `vpfe.dian.gov.co` — both, together.
- [ ] Observed throughput limits from step 13 fed into the P7 §2 schedule.

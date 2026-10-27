# P4 — Inbound Response Handling

**CO / DIAN-NE** · `SendNominaSyncResult` (`DianResponse`) + embedded `ApplicationResponse`

---

## 1. Why the inbound leg is not optional

DIAN-NE is a **both-directions** integration in a single synchronous call, and the inbound half
carries the business value. Under Res. DIAN 000227 de 2025 art. 1.5.3.2.3 the document exists to *support costs and
deductions in the income-tax return*. A document that was generated and transmitted but not
**validated** does not do that job.

So the response is not a delivery receipt to be logged and discarded. The engine must parse it,
persist the validation verdict and the CUNE, and drive correction or retry from it. An
implementation that fires `SendNominaSync` and ignores the return value is not merely incomplete —
it silently produces non-deductible payroll cost.

## 2. `DianResponse` — the synchronous envelope

Type `DianResponse` in namespace `http://schemas.datacontract.org/2004/07/DianResponse`, returned as
`SendNominaSyncResult`. Full member list, read from the WSDL:

| Element | Type | Meaning |
|---|---|---|
| `ErrorMessage` | `ArrayOfstring` | Validation-failure messages. Empty on success. Each entry is `ID – (R\|N) message` (P5 §2). |
| `IsValid` | `boolean` | **Primary verdict.** `true` = validated. |
| `StatusCode` | `string` | Processing status, e.g. `00`. |
| `StatusDescription` | `string` | e.g. `Procesado Correctamente`. |
| `StatusMessage` | `string` | e.g. `Documento Nomina 689, ha sido autorizada.` |
| `XmlBase64Bytes` | `base64Binary` | **The signed `ApplicationResponse`** — the legal evidence. Persist this. |
| `XmlBytes` | `base64Binary` | Nil in the payroll flow (`i:nil="true"` in DIAN's own sample). |
| `XmlDocumentKey` | `string` | **The CUNE** as recorded by DIAN — 96 hex chars (SHA-384). |
| `XmlFileName` | `string` | e.g. `Nomina (1)-firmado-SHA256`. |

DIAN's published success response (Anexo §9.7.2), condensed:

```xml
<SendNominaSyncResult>
  <b:ErrorMessage/>
  <b:IsValid>true</b:IsValid>
  <b:StatusCode>00</b:StatusCode>
  <b:StatusDescription> Procesado Correctamente </b:StatusDescription>
  <b:StatusMessage> Documento Nomina 689, ha sido autorizada.</b:StatusMessage>
  <b:XmlBase64Bytes>PD94bWwgdmVyc2lvbj0iMS4wIi…</b:XmlBase64Bytes>
  <b:XmlBytes i:nil="true"/>
  <b:XmlDocumentKey>660ebb7fdd77b6d67a00448e7afde2959992c53ad1bf14b9a394272c56ee8cc64b75dc08940625e39390a0af3d8d7cb9</b:XmlDocumentKey>
  <b:XmlFileName>Nomina (1)-firmado-SHA256</b:XmlFileName>
</SendNominaSyncResult>
```

Two parsing notes that will bite:

- **`StatusDescription` and `StatusMessage` are whitespace-padded** in DIAN's own example
  (`" Procesado Correctamente "`). Trim before comparing.
- **Every member is `minOccurs="0" nillable="true"`.** Treat all of them as optional and handle nil.
  Branch on `IsValid`, not on the presence or text of `StatusDescription`.

### Using `XmlDocumentKey` as the CUNE oracle

`XmlDocumentKey` is DIAN's own record of the document's CUNE. Because the locally computed CUNE
cannot be verified offline (P3 §5), this field is the practical oracle:

> During habilitación, compare the locally computed `InformacionGeneral/@CUNE` against the returned
> `XmlDocumentKey` on every submission. A mismatch on an otherwise-accepted document is the signal
> that the CUNE composition is wrong. Keep this comparison as a **permanent production assertion**,
> not just a test-phase check — it is a free, continuous integrity check on the hash inputs, and it
> is how you will detect a silent format regression (e.g. a locale change altering decimal
> formatting) before it becomes a mass rejection.

## 3. `ApplicationResponse` — the evidentiary document

`XmlBase64Bytes` decodes to an **`ApplicationResponse` signed by DIAN** (Anexo §3.7). This, not the
SOAP envelope, is the retainable proof of validation. It follows the same event model as
pre-validation e-invoicing.

Event codes carried in
`/ApplicationResponse/cac:DocumentResponse/cac:Response/cbc:ResponseCode` (with the human-readable
text in the sibling `cbc:Description`):

| Code | Event | Annex section |
|---|---|---|
| **02** | Documento validado por la DIAN | §3.7.3.1 |
| **04** | Documento rechazado por la DIAN | §3.7.3.2 |

Codes 02 and 04 are **mutually exclusive**: annex Table 7 (§3.7.2) records that each blocks the
other on the same electronic document.

> Caveat on Table 7: in the published PDF both event-name cells render as *"¡Error! No se encuentra
> el origen de la referencia."* — unresolved Word cross-references (P1 §8 defect 4). The code values
> `02` and `04` and the mutual-exclusion matrix are legible; the event *labels* come from §3.7.3.1
> and §3.7.3.2 rather than from the table itself.

**Persist `XmlBase64Bytes` verbatim.** Do not re-serialise, re-indent or re-encode it — it is
signed by DIAN and any byte change destroys the signature and with it the evidential value under
Res. DIAN 000227 de 2025 art. 1.5.3.8.2 / Ley 527/1999 arts. 12–13. Store the exact base64 or its exact decoded bytes.

## 4. Persistence contract

Minimum per-document record. Everything here is either legally required or needed for
reconciliation:

| Field | Source | Why |
|---|---|---|
| Employee ID, period (YYYY-MM) | engine | Business key |
| `Prefijo`, `Consecutivo`, `Numero` | outbound document | Uniqueness under rule 90 (P5 §3) |
| CUNE (computed) | outbound document | Local record |
| CUNE (returned) | `XmlDocumentKey` | Oracle; must equal the computed value |
| `IsValid` | response | Deductibility verdict |
| `StatusCode`, `StatusDescription`, `StatusMessage` | response | Diagnostics |
| `ErrorMessage[]` | response | Rule-level failure detail |
| `ApplicationResponse` (raw bytes) | `XmlBase64Bytes` | **Statutory evidence** |
| Signed outbound XML (raw bytes) | outbound | **Statutory evidence** |
| Transmit timestamp, environment (`Ambiente`) | engine | Audit, deadline proof |
| Link to superseding/superseded document | adjustment flow | Amendment chain |

Retention per Res. DIAN 000227 de 2025 art. 1.5.3.8.2 → ET art. 632 and Ley 962/2005 art. 46 (as amended by Ley 1819/2016
art. 304): retain for the statutory period with the information **accessible for later
consultation**. Archive-to-cold-storage is acceptable; archive-to-unreadable is not. See P7 §3.

## 5. `GetStatus` — the reconciliation path

`GetStatus` was extended to cover payroll documents (Res. DIAN 000013 de 2021, compiled in Res. DIAN 000227 de 2025). It takes the CUNE (the
"trackId" in e-invoicing terms) and returns the recorded status.

Use it for:

- **Ambiguous outcomes.** A timeout, connection reset or truncated response leaves the engine not
  knowing whether DIAN processed the document. Because rule 90 makes blind resubmission unsafe
  (P5 §3), `GetStatus` is the *only* correct disambiguation step.
- **Periodic reconciliation.** Sweep documents recorded as sent-but-unconfirmed and settle them.
- **Pre-deadline assurance.** Before the 10th, confirm every employee-month is `02`.

There is also a **public, unauthenticated lookup** for spot checks and for supplying evidence to a
client:

```
https://catalogo-vpfe.dian.gov.co/document/searchqr?documentkey=<CUNE>
```

This is the target the `CodigoQR` element points at. Useful for support; not a substitute for
`GetStatus` in an automated flow.

## 6. Response-handling decision logic

```
send(SendNominaSync)
 ├─ transport/SOAP fault, timeout, or no response
 │     → DO NOT resubmit blindly (rule 90)
 │     → GetStatus(CUNE)
 │          ├─ found & validated  → record 02, done
 │          ├─ found & rejected   → treat as rejection branch below
 │          └─ not found          → safe to resubmit same document
 │
 └─ DianResponse received
      ├─ IsValid = true
      │     → assert computed CUNE == XmlDocumentKey  (alert on mismatch)
      │     → persist ApplicationResponse + signed XML
      │     → mark employee-month VALIDATED (deductible)
      │
      └─ IsValid = false
            → parse ErrorMessage[] into (ID, R|N, text)
            → all-(N) with IsValid=true cannot occur; (N) alone never blocks validation
            → correct the source data or the mapping
            → resubmit under a NEW Consecutivo  (rule 90 — see P5 §3)
```

The last line is the one most often got wrong. A rejected document has still consumed its document
number for that worker. Correction is a **new document with a new consecutive**, not a retry of the
same one.

# P7 — Operations, Monitoring & Maintenance

**CO / DIAN-NE** · steady-state running of the electronic-payroll integration

---

## 1. The operating cycle

| | |
|---|---|
| Frequency | **Monthly**, always (Res. DIAN 000227 de 2025 art. 1.5.3.2.2) — irrespective of the client's pay cycle |
| Unit | **One document per employee per month** (art. 1.5.3.5.1.4: transmitted one by one) |
| Deadline | Within the **first 10 days** of the month following payment/credit (art. 1.5.3.4.1.1) |
| Volume | = active headcount, plus adjustment notes |

There is no batch operation, so the monthly run is *N* synchronous calls where *N* is headcount.

**Schedule to finish well before the 10th.** The deadline is a hard statutory date and the failure
modes ahead of it — rejections needing correction and resubmission under new consecutives (P5 §3),
DIAN-side outages triggering the 48-hour contingency (P5 §5) — all consume calendar time. A run
starting on the 9th has no recovery room. Target completion by roughly the 5th and treat the 6th–10th
as remediation window.

## 2. Throughput

Design inputs:

- One `SendNominaSync` per employee; synchronous, so latency is on the critical path.
- Payload ≤ 500 KB, typically far smaller.
- No published rate limit. **Measure it in habilitación** (P6 §5 step 13) and record the observed
  ceiling here at go-live.

Guidance:

- Parallelise across employees, but see the constraint below.
- **Bound concurrency by the consecutive-allocation transaction, not by CPU.** Rule 90 makes number
  reuse fatal, so allocation must be transactional and collision-free (P5 §3). This is the real
  limit on parallelism.
- Make each employee-month an independently retryable unit of work. Never batch several employees
  into one transaction — a partial failure then forces you to reason about which numbers were
  consumed.
- Back-pressure and jittered backoff on transport errors, honouring the 48-hour rule rather than a
  fixed retry count.

## 3. Retention

Res. DIAN 000227 de 2025 art. 1.5.3.8.2 → ET art. 632, Ley 962/2005 art. 46 (as amended by Ley 1819/2016 art. 304), and
Ley 527/1999 arts. 12–13.

Retain, per document, with the information **accessible for later consultation**:

- The **signed outbound XML**, byte-exact.
- The **`ApplicationResponse`** decoded from `XmlBase64Bytes`, byte-exact.
- The CUNE, the document number, and the validation verdict.
- The full adjustment chain — original, Reemplazar notes, Eliminar notes.

Two things worth being explicit about:

- **Byte-exactness is the whole point.** Both documents are signed; re-serialising, re-indenting or
  re-encoding destroys the signature and with it the evidential value. Store raw bytes or exact
  base64, never a parsed-and-rewritten DOM.
- **Deleted documents must still be retained.** Per the annex, `TipoNota=2` invalidates but does not
  remove — the original persists in DIAN's database flagged as deleted. Purging your copy because it
  was "cancelled" leaves you unable to evidence the chain.

## 4. Monitoring

**Per-run**

- Documents expected vs generated vs transmitted vs **validated** (`IsValid=true`). The last column
  is the one that matters — the others are progress, only validated documents support the deduction.
- Rejections by rule ID, trended month over month. A new ID appearing is a mapping regression or an
  authority-side change.
- **`N`-rule (notification) counts.** These pass validation, so nothing breaks — which is exactly why
  they need active surveillance. Treat a rising trend as a leading indicator of data-quality drift,
  and note that DIAN has form for promoting notification rules to rejection rules in later annex
  versions of the sibling e-invoicing regime.
- **CUNE assertion failures** — computed vs returned `XmlDocumentKey` (P4 §2). Should be identically
  zero. Any non-zero count is a hash-input regression (a locale change altering decimal formatting,
  a date-format change, a PIN rotation) and is urgent: it means documents are being registered under
  a key you did not predict.
- Deadline burn-down against the 10th.

**Continuous**

- Endpoint availability. Distinguish **DIAN outage** (art. 1.5.3.5.1.5) from **own-system failure**
  (art. 1.5.3.5.1.6) — different legal clocks, both 48 hours, both needing evidence (P5 §5). Log outage start
  and end per tenant.
- **Certificate expiry**, with generous lead time. Expiry mid-cycle stops all transmission for the
  tenant. Alert at 90/60/30 days. Renewal is a procurement action with an ONAC-accredited CA and is
  not instant.
- Consecutive-series health: monotonicity, no duplicates. Gaps are fine.

**Alerting thresholds** — page on: any rule-92 rejection (issuer enablement lost, blocks
everything); any CUNE mismatch; rejection rate above baseline; unvalidated documents remaining after
day 7.

## 5. Contingency

| Scenario | Response |
|---|---|
| DIAN service down | Queue; resume within **48 h of the day following restoration** (art. 1.5.3.5.1.5). Evidence the window. |
| Own systems down | Same 48-hour rule from the day following resolution (art. 1.5.3.5.1.6). |
| Certificate expired | Transmission stops entirely. No workaround — renew. Prevent via §4 monitoring. |
| Enablement lost (rule 92) | All traffic blocked. Escalate to DIAN; this is administrative, not technical. |
| Ambiguous outcome (timeout) | **`GetStatus` before any resubmission** (P4 §5). Never blind-retry. |
| Sustained inability to transmit | DIAN's free web solution exists for small employers but is manual and does not scale — realistic only as a last resort for a very small population. |

## 6. Version watch

Static as at 2026-09-04: **Anexo Técnico v1.0**, XSD **v1.0.6**, sample XML v1.0.2. Probing
confirmed no `V1-1`/`V1.1`/`V1-2`/`V1-0-1` toolkit exists (P1 §7).

Watch quarterly:

- `https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/documentacion-tecnica-soporte-de-pago-nomina-electronica/`
  — the toolkit ZIP URL is stable, so **diff the ZIP by SHA-256** against
  `SHA256SUMS.txt` rather than eyeballing the page.
- DIAN normatividad for resolutions amending Res. DIAN 000227 de 2025 (nómina electrónica, arts. 1.5.3.x).
- Re-fetch both WSDLs and diff — a new operation or a changed policy is the earliest technical signal
  of a regime change.

Also watch **outside** DIAN, because two things in the annex can go stale without the annex changing:

- **Overtime and surcharge percentages** (P3 §7) are hard-coded 2021 statutory rates. A labour-law
  change makes the annex wrong while the schema stays valid — cross-check the seven rates against the
  CO CCG annually.
- **`TipoTrabajador`** mirrors the PILA cotizante codes, which are maintained by MinSalud on a
  different cycle (INTERLINKAGES §3).

## 7. Runbook quick reference

| Symptom | First check |
|---|---|
| All documents rejected | Rule 92 (enablement); certificate validity; `Ambiente` vs endpoint |
| One document rejected, `IsValid=false` | Parse `ErrorMessage[]`; map ID → remediation; resubmit under a **new** consecutive |
| "Documento procesado anteriormente" | Rule 90 — number reused. Allocate new consecutive. Check for a retry loop. |
| Timeout / no response | `GetStatus(CUNE)` before anything else |
| CUNE ≠ `XmlDocumentKey` | Hash-input regression — check decimal truncation, date/time format, PIN, `Ambiente` |
| Security fault at transport | Clock skew (`wsu:Timestamp`); thumbprint reference; `To` header signed? |
| Signature rejected | XAdES profile — digest not SHA-1, `SignaturePolicyId` hash, `ClaimedRole` |

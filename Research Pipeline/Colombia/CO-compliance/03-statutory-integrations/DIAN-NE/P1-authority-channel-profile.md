# P1 — Authority & Channel Profile

**CO / DIAN-NE** · Documento Soporte de Pago de Nómina Electrónica (DSPNE)
Research date 2026-09-04 · all facts below traced to a downloaded artefact.

---

## 1. The authority and what it receives

**DIAN** (Unidad Administrativa Especial Dirección de Impuestos y Aduanas Nacionales) is Colombia's
national tax and customs authority. The **Servicio de Validación de Nómina Electrónica** is not a
standalone system: it is the pre-validation e-invoicing platform (`WcfDianCustomerServices`) with
one added operation and one extended operation.

What DIAN receives is the **Documento Soporte de Pago de Nómina Electrónica** — one signed XML
document per employee per month, carrying that employee's full accrual and deduction detail.

**Critical framing:** this is *not* a tax return and *not* a remittance. It is a **deductibility
instrument**. Under Res. DIAN 000227 de 2025 art. 1.5.3.2.3, the obligated parties are income-tax payers who need
to *support costs and deductions* in the income tax return (and discountable VAT where applicable).
A payroll cost that was never validated by DIAN is not supportable. That makes the inbound
validation leg a hard business dependency, not a receipt — see P4.

## 2. Legal basis

| Instrument | Role |
|---|---|
| **Resolución DIAN 000227 de 23 Sep 2025 (Resolución Única), arts. 1.5.3.1.1 to 1.5.3.9.8** | Nómina electrónica rules compiled from Res. DIAN 000013 de 2021: the document, obligated parties, periodicity, deadlines, habilitación, adjustment notes, retention. |
| **Anexo Técnico DSPNE Versión 1.0** | Issued under art. 1.5.3.7.1 of the resolution. 269 pp. Binding technical spec: field tables, code tables, CUNE, signature, web service, 433 validation rules. |
| **Estatuto Tributario arts. 572, 573** | Basis for third-party representation (art. 1.5.3.8.1 of the resolution). |
| **ET art. 632; Ley 962/2005 art. 46 (as amended by Ley 1819/2016 art. 304); Ley 527/1999 arts. 12–13** | Retention and evidential-value regime (art. 1.5.3.8.2). |
| **ONAC Circular 03-2016** | Digital-certificate accreditation regime referenced by the signature policy. |

## 3. Obligation scope, periodicity, deadline

- **Obligated parties** (art. 1.5.3.2.3) — income-tax contributors making payments or credits arising from
  an employment or statutory/regulatory relationship, and payments to pensioners borne by the
  employer, where they need to support costs/deductions.
- **Periodicity** (art. 1.5.3.2.2) — **monthly, always.** One document per beneficiary per month
  *regardless of actual pay frequency*. Where the employer pays weekly, biweekly or semi-monthly,
  the month's liquidations are **accumulated** into a single monthly document per employee. This is
  the single most important scoping fact for the payroll engine — see INTERLINKAGES §2.
- **Deadline** (art. 1.5.3.4.1.1) — within the **first ten (10) days of the month following** the payment or
  credit in account.
- **Granularity** (art. 1.5.3.5.1.4) — transmitted **one by one**, per beneficiary. There is no batch
  operation. Volume = headcount per month.

## 4. Channel

| Attribute | Value | Evidence |
|---|---|---|
| Channel type | Genuine machine-to-machine SOAP web service | WSDL, live retrieval |
| Protocol | SOAP 1.2, document/literal, WS-Addressing | WSDL `soap12:binding`; Anexo §9.3–9.4 |
| Service | `WcfDianCustomerServices` (WCF) | WSDL `wsdl:service` |
| Binding | `WSHttpBinding_IWcfDianCustomerServices` | WSDL |
| Payroll operations | `SendNominaSync` (transmit), `GetStatus` (query) | WSDL; Anexo §9.1 |
| Payload | base64 of a **ZIP containing exactly one** signed XML | Anexo §9.2 |
| Size limit | 500 KB | Anexo (container constraint) |
| Encoding | UTF-8 only | Anexo |
| Portal in the path? | **No.** Transmission is fully unattended. | Anexo §9.1 |

The service exposes 15 operations in total; 13 are e-invoicing-only and must not be called by the
payroll engine. See P2 §2 for the full list and the do-not-call boundary.

## 5. Endpoints

| Environment | Endpoint |
|---|---|
| Production (Operación) | `https://vpfe.dian.gov.co/WcfDianCustomerServices.svc` |
| Production WSDL | `https://vpfe.dian.gov.co/WcfDianCustomerServices.svc?singleWsdl` |
| Test (Habilitación) | `https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc` |
| Test WSDL | `https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc?singleWsdl` |
| Public document lookup (QR) | `https://catalogo-vpfe.dian.gov.co/document/searchqr?documentkey=<CUNE>` |

**Verified 2026-09-04:** both WSDLs returned HTTP 200, `text/xml`, ~61.7 KB, with no
authentication. The two WSDLs are **byte-identical apart from the hostname** — confirmed by
normalised diff. The live *service operations* were not invoked.

Note that `Ambiente` is *also* a field inside the document (`1` = Producción, `2` = Pruebas). The
environment is therefore selected in two places — endpoint host and payload attribute — and they
must agree. Mismatch is a common and avoidable rejection.

## 6. Onboarding gate (not a technical channel)

Before production transmission the issuer must complete **habilitación** in the DIAN portal:
register its own software or a proveedor tecnológico, obtain the `SoftwareID` and secret `PIN`, and
pass the test set in the habilitación environment. **Global rule 92 rejects any document from a
non-enabled issuer.** Where Mercans generates or transmits on a client's behalf, art. 1.5.3.8.1
additionally requires the third party to be enabled by DIAN, to register that capacity in the RUT,
and both parties to retain the mandate document. This is an administrative precondition to go-live,
handled in P6 — it is not an engineering blocker and does not sit in the transmission path.

**Fallback:** DIAN publishes a free web solution for electronic payroll aimed at small employers
(`https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/solucion-gratuita-de-nomina-electronica/`).
Irrelevant to an engine build, but relevant to contingency design — see P7 §5.

## 7. Artefact manifest

Downloaded to `CO-compliance/integration-sources/dian-ne/`. 23 files, 20,387,117 bytes.
SHA-256 for every file in `SHA256SUMS.txt`.

| Artefact | Path | Size | Gated? |
|---|---|---|---|
| Caja de Herramientas Nómina Electrónica V1-0 (toolkit ZIP) | `Caja-de-Herramientas-Nomina-Electronica-V1-0.zip` | 5,528,509 | public |
| Anexo Técnico DSPNE V1.0 (269 pp) | `caja/.../Anexo Tecnico/...V1.0.pdf` | 6,865,293 | public |
| ↳ text extract (`pdftotext -layout`) | `_txt/anexo-tecnico-v1.0.txt` | 1,303,975 | derived |
| `NominaIndividualElectronicaXSDV1.0.6.xsd` | `caja/.../XSD/` | 38,809 | public |
| `NominaIndividualDeAjusteElectronicaXSDV1.0.6.xsd` | `caja/.../XSD/` | 48,160 | public |
| UBL 2.1 + XAdES v1.3.2/v1.4.1 + xmldsig schema set (10 XSD) | `caja/.../Schemes/` | 346,761 | public |
| Sample XML — NominaIndividual V1.0.2 | `caja/.../Ejemplificaciones/` | 7,968 | public |
| Sample XML — NominaIndividualDeAjuste V1.0.2 | `caja/.../Ejemplificaciones/` | 9,775 | public |
| WSDL production | `wsdl/WcfDianCustomerServices-prod.wsdl` | 61,719 | public |
| WSDL habilitación | `wsdl/WcfDianCustomerServices-hab.wsdl` | 61,727 | public |
| Resolución 000013 de 11-02-2021 | `normativa/Resolucion-000013-de-11-02-2021.pdf` | 4,273,548 | public |
| ↳ text extract | `_txt/resolucion-000013-2021.txt` | 1,403,552 | derived |
| Micrositio — documentación técnica (link source) | `portal/micrositio-documentacion-tecnica-nomina.html` | 218,556 | public |
| Micrositio — solución gratuita (fallback ref) | `portal/solucion-gratuita-nomina.html` | 218,765 | public |

**Version closure.** The micrositio publishes exactly two payroll artefacts — the V1-0 toolkit and
Res. 000013/2021 — and nothing else. Probing for `Caja-de-Herramientas-Nomina-Electronica-{V1-1,
V1.1, V1-2, V1-0-1}.zip` returned 404 on all four; only `V1-0` (case-insensitive) returns 200.
**V1.0 is the current and only published version of the Anexo Técnico** as at 2026-09-04. Note the
internal version skew is normal and not an error: Anexo v1.0, XSD v1.0.6, sample XML v1.0.2.

## 8. Documentation defects found in the published artefacts

Recorded here so implementers do not lose time reconciling them. Four defects, one of them costly.

1. **CUNE worked example is not reproducible.** Anexo §8.1.1.3 gives a complete set of inputs and a
   published SHA-384 result. It does not reproduce. See **P3 §5**, which documents the
   1,344-variant search that failed and gives the mitigation. *This is the highest-value finding in
   this runbook* — the example is the natural unit-test fixture and it is wrong.
2. **`SendBillSync` vs `SendNominaSync`.** Anexo §9.7's bullet list says "Método: SendBillSync"
   while the surrounding prose, the request envelope and the WSDL all say `SendNominaSync`. **The
   WSDL is authoritative: `SendNominaSync`.**
3. **Authentication is described two different ways.** Anexo §9.3/§9.4 state TLS 1.2 *with mutual
   authentication via digital certificates*; the WSDL policy declares
   `sp:HttpsToken RequireClientCertificate="false"` and carries the X.509 as a message-level
   endorsing token. These are not the same thing. Resolved in **P2 §3**.
4. **Broken cross-references and inherited content.** Anexo §3.7.2 Table 7 renders as
   "¡Error! No se encuentra el origen de la referencia." for both event names — an unresolved Word
   field in the published PDF. Anexo §14 is a SOAP UI walkthrough still showing `GetStatus` and
   `SendBillAsync` examples inherited verbatim from the e-invoicing annex.

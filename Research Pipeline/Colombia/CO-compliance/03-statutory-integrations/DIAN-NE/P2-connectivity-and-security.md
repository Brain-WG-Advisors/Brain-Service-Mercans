# P2 — Connectivity & Security

**CO / DIAN-NE** · SOAP 1.2 / WS-Security / XAdES-EPES
All binding facts below are read from the **live WSDL retrieved 2026-09-04**, which is authoritative
over the prose in the Anexo Técnico wherever the two disagree.

---

## 1. Transport and binding

| Layer | Setting | Source |
|---|---|---|
| Transport | HTTPS, TLS 1.2 | Anexo §9.3, §9.4 |
| SOAP version | **1.2** (`http://www.w3.org/2003/05/soap-envelope`) | WSDL `soap12:binding` |
| Style / encoding | `document` / `literal` | WSDL `soap12:operation style="document"`, `soap12:body use="literal"` |
| Addressing | **WS-Addressing required** (`wsaw:UsingAddressing`) | WSDL policy |
| Binding name | `WSHttpBinding_IWcfDianCustomerServices` | WSDL |
| Port | `WSHttpBinding_IWcfDianCustomerServices` | WSDL |
| Service | `WcfDianCustomerServices` | WSDL |
| Target namespace | `http://wcf.dian.colombia` | WSDL |

**SOAP actions for the two payroll operations:**

```
http://wcf.dian.colombia/IWcfDianCustomerServices/SendNominaSync
http://wcf.dian.colombia/IWcfDianCustomerServices/SendNominaSyncResponse
```

The `To` WS-Addressing header must carry the environment endpoint and — per the policy — **must be
signed** (see §3).

## 2. Operation surface and the do-not-call boundary

The service exposes **15** operations. Only **2** are in scope for payroll.

**In scope:**

| Operation | Purpose |
|---|---|
| `SendNominaSync` | Synchronous transmit + validate of one DSPNE or one nota de ajuste |
| `GetStatus` | Query validation status of a transmitted document by CUNE |

**Out of scope — e-invoicing only. The payroll engine must never call these:**
`SendBillSync`, `SendBillAsync`, `SendBillAttachmentAsync`, `SendTestSetAsync`,
`SendEventUpdateStatus`, `GetStatusZip`, `GetStatusEvent`, `GetXmlByDocumentKey`,
`GetNumberingRange`, `GetAcquirer`, `GetDocumentInfo`, `GetExchangeEmails`, `GetReferenceNotes`.

> Guard this in code, not in convention. Because payroll rides on the e-invoicing service, a
> generated WCF/JAX-WS client will expose all 15 methods on one proxy class. Wrap the proxy and
> expose only the two, or a copy-paste from an e-invoicing sample will silently call `SendBillSync`
> — which is exactly the mistake Anexo §9.7 makes in its own text (P1 §8 defect 2).

### `SendNominaSync` message contract

```xml
<xs:element name="SendNominaSync">
  <xs:complexType><xs:sequence>
    <xs:element minOccurs="0" name="contentFile" nillable="true" type="xs:base64Binary"/>
  </xs:sequence></xs:complexType>
</xs:element>

<xs:element name="SendNominaSyncResponse">
  <xs:complexType><xs:sequence>
    <xs:element minOccurs="0" name="SendNominaSyncResult" nillable="true" type="DianResponse"/>
  </xs:sequence></xs:complexType>
</xs:element>
```

One input part: `contentFile`, base64 of the ZIP. Response handling is P4.

## 3. Authentication — resolving the spec/WSDL conflict

This is the single most important configuration decision in the integration, and the two published
artefacts do not agree.

**What the Anexo says** (§9.3, §9.4): *"El medio de comunicación es internet con la utilización del
protocolo TLS versión 1.2 con autenticación mutua a través de certificados digitales"* — i.e. mutual
TLS. It then adds, correctly, that the model follows *"WS-Security 1.0 Oasis, con autenticación
X.509 Certificate Token Profile 1.1"*.

**What the WSDL declares** (verbatim from the retrieved policy):

```xml
<sp:TransportBinding>
  <sp:TransportToken><wsp:Policy>
    <sp:HttpsToken RequireClientCertificate="false"/>   <!-- NOT mutual TLS -->
  </wsp:Policy></sp:TransportToken>
  <sp:AlgorithmSuite><wsp:Policy><sp:Basic256Sha256Rsa15/></wsp:Policy></sp:AlgorithmSuite>
  <sp:Layout><wsp:Policy><sp:Strict/></wsp:Policy></sp:Layout>
  <sp:IncludeTimestamp/>
</sp:TransportBinding>

<sp:EndorsingSupportingTokens>
  <sp:X509Token sp:IncludeToken=".../IncludeToken/AlwaysToRecipient">
    <wsp:Policy>
      <sp:RequireThumbprintReference/>
      <sp:WssX509V3Token10/>
    </wsp:Policy>
  </sp:X509Token>
  <sp:SignedParts>
    <sp:Header Name="To" Namespace="http://www.w3.org/2005/08/addressing"/>
  </sp:SignedParts>
</sp:EndorsingSupportingTokens>

<sp:Wss11><wsp:Policy><sp:MustSupportRefThumbprint/></wsp:Policy></sp:Wss11>
<sp:Trust10><wsp:Policy>
  <sp:MustSupportIssuedTokens/><sp:RequireClientEntropy/><sp:RequireServerEntropy/>
</wsp:Policy></sp:Trust10>
<wsaw:UsingAddressing/>
```

**Resolution — build to the WSDL.** The client certificate is presented as a **message-level
WS-Security endorsing token**, not as a TLS client certificate. Concretely:

- `RequireClientCertificate="false"` — do **not** configure a TLS client certificate on the socket.
  Server-authenticated TLS 1.2 only.
- Place a `<wsse:BinarySecurityToken>` (`WssX509V3Token10`) in the SOAP `Security` header, and
  reference it **by thumbprint** — `RequireThumbprintReference` plus `Wss11/MustSupportRefThumbprint`
  means a `SecurityTokenReference/KeyIdentifier` with
  `ValueType=".../oasis-200401-wss-soap-message-security-1.0#ThumbprintSHA1"`. A subject-key-identifier
  or direct BST reference will be rejected by a strict-layout WCF endpoint.
- Sign, at minimum, the WS-Addressing `To` header and the `wsu:Timestamp`
  (`sp:IncludeTimestamp` is set; `Layout=Strict`).
- Algorithm suite `Basic256Sha256Rsa15` — AES-256 symmetric, SHA-256 digest, RSA-1.5 key wrap.

The Anexo's "mutual TLS" sentence is best read as loose drafting inherited from the e-invoicing
annex. Two things corroborate the WSDL reading: the endorsing-token policy is unambiguous, and
Anexo §14 — DIAN's own SOAP UI walkthrough — instructs the reader to configure a **Keystore**, a
**WS-Security Signature** and a **Timestamp** (§14.6–14.8), which is message-level configuration,
not transport-level.

**Recommendation:** implement message-level first. If the habilitación environment rejects the
handshake, add the TLS client certificate as a fallback — the same certificate serves both, so the
cost of testing both is low. Confirm empirically during P6; do not resolve it by reading alone.

## 4. Certificates

Two distinct uses of X.509, often conflated:

| Use | Where | Requirement |
|---|---|---|
| **Transport/channel auth** | WS-Security header, `BinarySecurityToken` | X.509 v3, thumbprint-referenced |
| **Document signature** | Inside the XML, `ds:Signature` in `ext:UBLExtensions` | XAdES-EPES, `ClaimedRole` ∈ {`supplier`, `thirdparty`} |

In practice **one certificate** issued by a certification authority accredited by **ONAC** (the
Colombian national accreditation body, regime per Circular 03-2016) serves both roles.

**Document signature profile** (Anexo §6.1.3, §7):

- Format **XAdES-EPES** (signature policy identifier present), enveloped in
  `/NominaIndividual/ext:UBLExtensions/ext:UBLExtension/ext:ExtensionContent/ds:Signature`.
- The signature policy hash references the ONAC Circular 03-2016 document.
- Digest algorithm: SHA-256 or stronger. The annex explicitly rejects
  `http://www.w3.org/2000/09/xmldsig#sha1` — a rule fires if SHA-1 is used.
- `xades:SigningTime` must be a real signing time; `xades:SigningCertificate/xades:Cert/xades:CertDigest`
  must be populated.
- The UBL 2.1 vocabulary is used **only** for the signature envelope. Every other section of the
  document uses DIAN's own non-UBL structure (Anexo §9 opening). Do not attempt to model the payroll
  body as UBL.

**Certificate lifecycle** is an operational risk, not a build task — see P7 §4.

## 5. Message packaging

```
NominaIndividual.xml  (UTF-8, XAdES-EPES signed)
        │
        ├─ ZIP  (exactly ONE entry; ≤ 500 KB; must not be empty or corrupt)
        │
        └─ base64  →  <wcf:contentFile>
```

Constraints, all enforced by DIAN before schema validation (Anexo §9.2.1):

- ZIP must not be **empty**.
- ZIP must not be **corrupt**.
- ZIP must contain **exactly one** signed XML. There is no multi-document container.
- Total **≤ 500 KB**.
- **UTF-8 only.** No BOM issues have been documented, but the shipped sample XML carries a UTF-8
  BOM — mirror it only if habilitación testing shows it is tolerated; prefer emitting without.

Because one document = one employee = one call, a 5,000-employee client generates 5,000
`SendNominaSync` calls per month. Throughput design is P7 §2.

## 6. Secrets inventory

| Secret | Issued by | Where used | Notes |
|---|---|---|---|
| `SoftwareID` | DIAN at habilitación | `ProveedorXML/@SoftwareID`; input to `SoftwareSC` | Per registered software |
| Software **PIN** | Chosen by issuer at habilitación | Input to `SoftwareSC` **and to the CUNE** | **Never appears in the XML.** Reserved, restricted circulation. |
| X.509 private key | ONAC-accredited CA | WS-Security header + XAdES signature | HSM or sealed keystore |

The PIN deserves particular care: it is an input to the CUNE hash but is *not* carried in the
document, which is precisely what makes the CUNE unforgeable by a third party who holds the XML.
Leaking the PIN undermines the control. Store it with the same handling as the private key —
per-tenant, encrypted at rest, never logged, never in a CI fixture. Note that P3 §5's remediation
path involves hashing with the real PIN; keep those test vectors out of shared repositories.

## 7. Network and infrastructure checklist

- [ ] Egress to `vpfe.dian.gov.co:443` and `vpfe-hab.dian.gov.co:443` allow-listed.
- [ ] TLS 1.2 with the server's chain trusted; no client certificate on the socket (see §3).
- [ ] Per-tenant keystore provisioned; thumbprint reference verified against the WSDL requirement.
- [ ] Clock synchronised to NTP — `wsu:Timestamp` is mandatory and `Layout=Strict`; skew causes
      hard failures. DIAN's own sample shows a **5-minute** Created→Expires window.
- [ ] WS-Addressing `To`/`Action` populated and `To` signed.
- [ ] SOAP client wrapper exposes only `SendNominaSync` and `GetStatus` (§2).
- [ ] Outbound retry/backoff policy defined, honouring the statutory 48-hour rule (P5 §5).

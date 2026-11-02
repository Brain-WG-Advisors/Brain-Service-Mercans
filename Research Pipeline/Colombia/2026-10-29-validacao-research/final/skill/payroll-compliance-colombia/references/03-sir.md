# Colombia Statutory Integrations Register (SIR) - CO-SIR-001 v1.3

The Colombia statutory-integration register: for each authority a payroll engine must interact with, the channel, direction, authentication, technical format, error classes, penalties and deadlines - and whether the channel is machine-to-machine (only the DIAN electronic payroll web service) or a portal / operator round-trip (Form 350, Format 2276, PILA, severance funds).


## Provenance

| Source artifact | Bytes | MD5 |
|---|---|---|
| `CO-SIR-001-v1.3-texto-final.md (v1.3 text, 15 blocks)` | 5,538 | `79b7f2df8bfaf7ec04992b7390ea4736` |
| `CO-SIR-001-v1.2-texto-final.md (v1.2 text; its version-history line)` | 5,457 | `e8669140302efe07b2ae15f41b585bd2` |
| `CO-SIR-001 v1.1 Google Doc, text capture of 2026-10-29 (base of v1.2)` | 6,163 | `27e3807ed33a9d8f72c200a70f18474a` |
| `CO-SIR-INDEX-001-v1.0.docx (authority index)` | 41,172 | `3144b46eff327c56fa5f4c20a355624a` |

CO-SIR-001 exists only as a Google Doc; versions 1.2 (issued 2026-10-30) and 1.3 (issued 2026-11-02) were released as 15 replacement blocks over version 1.1. Part 1 is therefore the v1.1 content (from the read-only text capture, restated in English) with the 15 blocks of the v1.3 text inserted **verbatim**; a block is marked ⟦v1.3⟧ where it changed in v1.3 and ⟦v1.2⟧ where it is unchanged since v1.2. Where Part 1 and Part 2 differ, Part 1 governs. Part 2 is a verbatim conversion of the index docx.


## Reading notes (added at compilation, 2026-11-02)

- **Electronic payroll as support for costs and deductions:** Res. DIAN 000227 de 2025 art. **1.5.3.2.1** (formerly Res. 000013
  de 2021 art. 2). Art. 1.5.3.2.3 only defines the obligated parties - do not cite it for deductibility.
- **Validation rules:** Anexo Técnico NE v1.0 §6 lists **519** rules (437 for the payroll documents); the split is in Part 1 §4.
- **NE contingency:** transmit within 48 hours counted from the day after the service is restored (art. 1.5.3.5.1.5).
- **Not in the SIR text:** sections 0 and 2 of the Google Doc still speak of six in-scope filings and do not describe the
  pensioners flow (CO-PILA-007); this file adds that flow in Part 1 §0 and §2 from the report specs.
- Detailed NE transport, signature, CUNE and code tables: `04-reports-spec.md` CO-DIAN-001 (File Structure, Field Options).


## Navigation index

Read with `offset` / `limit` rather than opening the whole file.

| Line | Section |
|---|---|
| 49 | Part 1 - CO-SIR-001 v1.3 (Statutory Integration Register) |
| 51 | &nbsp;&nbsp;&nbsp;&nbsp;Document control |
| 73 | &nbsp;&nbsp;&nbsp;&nbsp;0. Purpose and scope |
| 94 | &nbsp;&nbsp;&nbsp;&nbsp;1. Inbound |
| 100 | &nbsp;&nbsp;&nbsp;&nbsp;2. Outbound |
| 115 | &nbsp;&nbsp;&nbsp;&nbsp;3. Authentication |
| 127 | &nbsp;&nbsp;&nbsp;&nbsp;4. Technical specifications |
| 135 | &nbsp;&nbsp;&nbsp;&nbsp;5. Errors |
| 144 | &nbsp;&nbsp;&nbsp;&nbsp;6. Deadlines |
| 156 | &nbsp;&nbsp;&nbsp;&nbsp;Appendix A - sources cited by the SIR |
| 163 | Part 2 - Authority index (CO-SIR-INDEX-001 v1.0, 2026-09-04) |

---

## Part 1 - CO-SIR-001 v1.3 (Statutory Integration Register)

### Document control

| Field | Value |
|---|---|
| Document ID | CO-SIR-001 |
| Version | v1.3 ⟦v1.3⟧ |
| Country | Colombia (CO) |
| Jurisdictions | National - DIAN (tax); Ministerio de Salud y Protección Social via licensed operadores de información (PILA); Fondos de Cesantías via operador |
| Tax year | 2026 |
| Currency | COP |
| Status | Issued |
| Related deliverables | CO-CCG-001 v1.6 (Module 10); the seven Report Specs (five at v1.2; CO-DIAN-002 and CO-PILA-007, the pensioners PILA flow, at v1.1); CO-DD-001 v1.5; CO Payslip Generator v1.3; DIAN-NE Configuration Runbook (P1–P7) ⟦v1.3⟧ |

Version history:

| Version | Date | Change |
|---|---|---|
| v1.0 | 2026-09-04 | Initial issue |
| v1.1 | 2026-10-21 | Citations of Res. DIAN 000013 de 2021 updated to Res. DIAN 000227 de 2025. |
| v1.2 | 2026-10-30 | Statutory validation against the primary sources: related deliverables and Appendix A updated (CO-CCG-001 v1.5, the seven Report Specs v1.1 including CO-PILA-007, CO-DD-001 v1.4, Payslip Generator v1.2; PILA Technical Annexes 2 v30 and 3 v15 as amended by Resolución MSPS 1529 de 2026); the electronic payroll document as the support for costs and deductions (Res. DIAN 000227 de 2025 art. 1.5.3.2.1); Format 2276 calendar; NE contingency (48 hours from the day after the service is restored); PILA penalties and deadlines; interest on severance savings; severance-fund file formats; NE validation-rule count. ⟦v1.2⟧ |
| v1.3 | 2026-11-02 | Statutory validation, second pass: NE validation-rule count (Anexo Técnico NE v1.0 §6: 519 rules); related deliverables and Appendix A updated (CO-CCG-001 v1.6, Report Specs v1.2, CO-DD-001 v1.5, Payslip Generator v1.3). ⟦v1.3⟧ |

### 0. Purpose and scope

- Discovery verdict **HAS_INTEGRATIONS**: 4 authorities; 1 system-to-system channel. Of the in-scope filings, the electronic payroll
  document is carried system-to-system; the others are manual (portal or operator upload). The seventh filing, PILA for pensioners
  paid by the employer (CO-PILA-007), rides on the same operator channel as the employees' PILA.
- Integration inventory:

| ID | Authority / channel | Direction | Integration |
|---|---|---|---|
| CO-OUT-NE-001 | DIAN - Servicio de Validación de Nómina Electrónica | Outbound | Yes |
| CO-IN-NE-APPRESPONSE | DIAN - ApplicationResponse / GetStatus | Inbound | Yes |
| CO-OUT-MUISCA-001 | DIAN - Muisca (Form 350) | Outbound | No |
| CO-OUT-PILA-001 | PILA via operador de información | Outbound | Yes (file generation only) |
| CO-IN-PILA-001 | PILA settlement return | Inbound | No |
| CO-OUT-CESANTIAS-001 | Fondos de Cesantías via operador | Outbound | Yes (file generation only) |
| CO-IN-CESANTIAS-CONFIRMATION | Severance-fund confirmation | Inbound | No |

- Electronic payroll sources: Res. DIAN 000227 de 2025 (which compiles Res. DIAN 000013 de 2021), Anexo Técnico del Documento Soporte de
  Pago de Nómina Electrónica v1.0 (269 pp.), XSD v1.0.6 and the WSDL (obtained 2026-09-04). Where the annex and the WSDL diverge,
  the WSDL governs.

### 1. Inbound

- The NE is the supporting document for costs and deductions: Res. DIAN 000227/2025 art. 1.5.3.2.1 (formerly art. 2 of Res. DIAN 000013/2021), ET art. 771-2 inc. 3, ET art. 616-1 par. 6 and DUR art. 1.6.1.4.27; the ApplicationResponse must be retained. ⟦v1.2⟧
- Inbound register: CO-IN-NE-APPRESPONSE (SendNominaSync response + GetStatus by CUNE; mandatory) · CO-IN-PILA-001 (operational) ·
  CO-IN-CESANTIAS-CONFIRMATION (records E10, E11, E90, E91, E93; operational).

### 2. Outbound

| Channel | Report spec | Frequency | Format |
|---|---|---|---|
| CO-OUT-NE-001 | CO-DIAN-001 | Monthly | SOAP 1.2; base64 ZIP holding exactly one signed XML; UTF-8; 500 KB maximum |
| CO-OUT-MUISCA-001 | CO-DIAN-002 | Monthly | Portal entry, no file |
| CO-OUT-PILA-001 | CO-PILA-003 (employees), CO-PILA-007 (pensioners) | Monthly | Fixed-width TXT (Archivo Tipo 1 + Archivo Tipo 2) |
| CO-OUT-CESANTIAS-001 | CO-CESANTIAS-006 | Annual | Fixed TXT, XLS 97-2003 or CSV, per operator |

Content per channel: NE - per employee: salary, overtime, allowances, bonuses, severance savings and interest, vacation; health,
pension, solidarity fund, withholding, garnishments, third-party payments · Form 350 - withholding aggregated by concept · PILA -
IBC by subsystem, days, change events (novedades), health, pension, solidarity fund, ARL, CCF, SENA, ICBF · Cesantías - annual
liquidation at 31 December, fund, contact, start date · Form 220 - issued to the employee, not filed with DIAN · Format 2276 -
income and withholding per beneficiary for the year.

### 3. Authentication

- **NE:** the annex (§9.3/§9.4) describes mutual TLS, while the WSDL policy has `sp:HttpsToken RequireClientCertificate="false"`:
  TLS 1.2 server-side only, with WS-Security 1.0 message security (X.509 Token Profile 1.1, Basic256Sha256Rsa15, timestamp) and
  WS-Addressing (signed `To`). Document signature XAdES-EPES (SHA-1 rejected); certificate from an ONAC-accredited authority;
  habilitación (SoftwareID, PIN, test set; global rule 92). Third-party transmitter: Res. 227/2025 art. 1.5.3.8.1 (enabled third
  party, registered in the RUT, mandate).
- **Muisca (Form 350, Format 2276):** interactive session with the Instrumento de Firma Electrónica (IFE); no machine credential.
- **PILA:** operator credentials (Aportes en Línea, Enlace Operativo, MiPlanilla, Asopagos, SOI, ...); no government-published
  authentication.
- **Cesantías:** operator login. The "APIS PILA" developer portal of one operator was only a shell on 2026-09-04 and is not used.

### 4. Technical specifications

- **NE:** SOAP 1.2 document/literal; operations SendNominaSync and GetStatus (2 of the 15 operations in scope); production host
  `vpfe.dian.gov.co`, habilitación host `vpfe-hab.dian.gov.co` (`/WcfDianCustomerServices.svc`); XSD v1.0.6; Anexo Técnico NE v1.0 §6 lists 519 validation rules: 437 for the payroll documents (NominaIndividual 198 = 189 R + 9 N; NominaIndividualDeAjuste 239 = 219 R + 20 N), 56 for the digital signature (54 R; 2 without a flag), 23 for the connection (21 R + 2 N) and 3 general rules (R). R = rejection, N = notification. ⟦v1.3⟧; 500 KB;
  no batch (one document per beneficiary).
- **Muisca:** portal. **PILA:** two fixed-width TXT files; government layout plus operator pre-validation.
- **Cesantías:** Severance funds: the file format (TXT 258 positions / XLS / CSV) is each severance fund's own rule; no government schema is published. The annual deposit does not go through the PILA (AT2 v30 has no severance record); Ley 2466/2025 art. 64 par. 1 tasks the Ministry of Health with a PILA rule only for the optional monthly advance deposit, not yet reflected in AT2 v30. ⟦v1.2⟧

### 5. Errors

- Seven classes: Container, Signature, Schema, Business (R), Business (N), global rule 90 (document number reused), global rule 92
  (issuer not enabled).
- No idempotent retry: query GetStatus by CUNE before resending; corrections by adjustment note; ApplicationResponse 02 = validated,
  04 = rejected.
- Penalties: NE (not deductible; Res. 227/2025 art. 1.5.3.2.1; ET 771-2, ET 616-1 and 651) ⟦v1.2⟧ · Form 350 (ET 641, 634) · PILA (late-payment interest at the income-tax default rate, Ley 100/1993 art. 23; UGPP penalties for omission, late filing and inaccuracy, Ley 1607/2012 art. 179 as modified by Ley 1819/2016 art. 314, num. 3 as modified by Ley 2010/2019 art. 121) ⟦v1.2⟧ · Cesantías (one day's salary per day of delay, uncapped; Ley
  50/1990 art. 99 num. 3).

### 6. Deadlines

- NE: first 10 days of the month following payment; one document per employee per month (Res. 227/2025 arts. 1.5.3.2.2 and
  1.5.3.4.1.1).
- Form 350: 7th to 16th business day, by the last digit of the NIT (DUR 1625/2016 art. 1.6.1.13.2.33).
- PILA: from the 2nd to the 16th business day, by the last two digits of the NIT / identity document (00–07 = 2nd … 94–99 = 16th), Decreto 780/2016 art. 3.2.2.1 (as substituted by Decreto 1990/2016 art. 2). ⟦v1.2⟧
- Cesantías: before 15 February (Ley 50/1990 art. 99 num. 3).
- Format 2276: May to June of the following year, by NIT (Res. 227/2025 art. 1.3.9.1.3): by the last digit of the NIT for large taxpayers (grandes contribuyentes) and by the last two digits for legal entities (personas jurídicas); exact dates are set in the annual DIAN due-date resolution. ⟦v1.2⟧
- Form 220: by the last business day of March; not filed with DIAN (DUR 1625/2016 art. 1.6.1.13.2.40).
- Interest on severance savings (12% a year): paid to the employee in January, or on termination / within the month after a partial severance settlement (Ley 52/1975 art. 1; Decreto 1072/2015 art. 2.2.1.3.4). ⟦v1.2⟧
- SendNominaSync is synchronous; no published SLA; contingency: transmit within 48 hours counted from the day after the service is restored (Res. 227/2025 art. 1.5.3.5.1.5); keep the supporting documents (soportes) of the payroll document. ⟦v1.2⟧

### Appendix A - sources cited by the SIR

CCG Module 10 (CO-CCG-001 v1.6) ⟦v1.3⟧ · 7 Report Specs (v1.2; CO-DIAN-002 and CO-PILA-007 v1.1; including CO-PILA-007, pensioners PILA flow) ⟦v1.3⟧ · DIAN-NE Configuration Runbook (P1-P7) · Res. DIAN 000227/2025 arts. 1.5.3.1.1 to 1.5.3.9.8 ·
Anexo Técnico DSPNE v1.0 · XSD v1.0.6 · WSDL · PILA — Resolución 2388 de 2016, Anexo Técnico 2 (v30) and Anexo Técnico 3 (v15), as amended by Resolución MSPS 1529 de 2026 ⟦v1.2⟧ · severance-fund operator manual · operator portal ·
integration landscape (2026-09-04).


## Part 2 - Authority index (CO-SIR-INDEX-001 v1.0, 2026-09-04)

The discovery index the SIR was built on: one row per authority, with the channel, direction and developer portal. Verbatim,
except three provenance phrases naming internal working files. Read it with Part 1: the filing count is now **seven** (CO-PILA-007,
pensioners, rides on the PILA operator channel), and the deductibility citation is the one in Part 1 §1.


```
Colombia
Statutory Integration Register -- Authority Index
```

CO-SIR-INDEX-001  v1.0

Mercans Compliance Regulations Team

Jurisdiction: Colombia (CO)  |  Currency: COP  |  Tax Year 2026

Scope: private-sector salaried population (6 in-scope filings at v1.0)

Discovery verdict: HAS_INTEGRATIONS  |  Generated 2026-09-04

Version Control

| Version | Date | Author | Notes |
|---|---|---|---|
| v1.0 | 2026-09-04 | Mercans Compliance Regulations Team | Initial issue. Authority index generated from the integration discovery record. |

1. Authority Index

One row per authority identified in the Colombian payroll statutory landscape. 4 authorities in total: 1 with a genuine system-to-system channel, 3 manual. Of the 6 in-scope filings, 1 is carried system-to-system and 5 are manual.

| Authority | Integration | Channel | Direction(s) | Developer portal | Runbook location |
|---|---|---|---|---|---|
| DIAN-NE <br> DIAN -- Servicio de Validacion de Nomina Electronica <br> Unidad Administrativa Especial Direccion de Impuestos y Aduanas Nacionales (DIAN) <br> Carries: CO-DIAN-NE-MONTHLY-001 (monthly, one document per employee, within the first 10 days of the following month) | YES | Machine-to-machine SOAP 1.2 web service over HTTPS (WS-Addressing, WS-Security timestamp). Operation SendNominaSync on WcfDianCustomerServices, plus GetStatus. Payload is base64 of a ZIP holding one XAdES-EPES-signed UBL 2.1 XML, max 500 KB, UTF-8 only. Authenticated by an X.509 certificate from an ONAC-accredited CA. No portal step in the transmission path; habilitacion (SoftwareID + PIN) is a one-time portal-gated onboarding prerequisite, not a channel. | OUTBOUND + INBOUND -- both legs in one synchronous call. Outbound: signed NominaIndividual / NominaIndividualDeAjuste. Inbound: base64 ApplicationResponse (IsValid, StatusCode, XmlDocumentKey). The inbound leg is a hard dependency, not a receipt -- the CUNE and validation status must be persisted, since deductibility of the payroll cost depends on validation. | https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/documentacion-tecnica-soporte-de-pago-nomina-electronica/ <br> Artefacts BUILD-READY: WSDL, XSD v1.0.6, UBL/XAdES schema set, samples and the 269-page annex, all public with no login. | 03-statutory-integrations/DIAN-NE/ |
| DIAN-MUISCA <br> DIAN -- Servicios Informaticos Electronicos / Muisca <br> Unidad Administrativa Especial Direccion de Impuestos y Aduanas Nacionales (DIAN) <br> Carries: CO-DIAN-F350-MONTHLY-002, CO-DIAN-EXO2276-ANNUAL-005, CO-DIAN-F220-ANNUAL-004 | NO | Portal round-trip (browser). Form 350 is keyed or loaded in the Muisca web form; Formato 2276 v4 is prepared offline in the prevalidador and uploaded as XML through the informacion exogena service. Authenticated by the DIAN Instrumento de Firma Electronica (IFE), which is issued to a natural person and exercised interactively -- the structural reason no M2M path exists. Same legal entity as DIAN-NE, entirely different posture: the electronic payroll web service does not carry these filings. | OUTBOUND only. | None published by the authority. <br> No SOAP, REST or SFTP filing surface exists. Vendor-marketed "DIAN APIs" are commercial wrappers around the e-invoicing service and do not cover Form 350 or exogena -- do not model them as a statutory channel. | Not applicable -- manual authority. |
| PILA-OI <br> PILA -- Planilla Integrada de Liquidacion de Aportes, via a licensed operador de informacion <br> Ministerio de Salud y Proteccion Social (system owner); collection intermediated by private operadores de informacion supervised by the Superintendencia Financiera <br> Carries: CO-PILA-MONTHLY-003 (monthly; 2nd to 16th business day of the following month, by the last two digits of the employer NIT). SENA, ICBF and Cajas de Compensacion ride on this same planilla. | NO | Portal round-trip through a licensed private operador de informacion (SOI/ACH Colombia, Simple S.A., SuAporte/ARUS, Aportes en Linea, Mi Planilla, Asopagos, Compensar). Under Res. MSPS 2388 de 2016 the modalidad electronica is keying the planilla online or uploading a fixed-width flat file (.txt/.csv) to the electronic means made available by the operator; the operator settles, collects and forwards to each administradora. Operator account credentials only -- no certificate, no signature. The employer never transacts directly with the government and there is no government-facing endpoint to integrate with. | OUTBOUND + INBOUND. Outbound: Archivo Tipo 1 (34 fields / 567 positions) and Archivo Tipo 2 (header 22 fields / 359 positions, one Registro Tipo 2 per contributor), fixed-width. Inbound: the operator's settlement/payment output, which must be reconciled (planilla number, payment date, per-contributor rejections) -- operator-specific, with no published layout. | None published by the authority. <br> See note (a) below on the ARUS/SuAporte "Portal Desarrolladores APIS PILA" (https://www.suaporte.com.co/portal-apis/) -- a private commercial offering, deliberately not scored as an integration. | Not applicable -- manual authority. |
| FONDOS-CESANTIAS <br> Fondos de Cesantias -- annual severance-savings deposit allocation <br> Private severance-savings funds (Porvenir, Proteccion, Colfondos, Skandia, FNA), reached through a licensed operador de informacion <br> Carries: CO-CESANTIAS-DEPOSIT-ANNUAL-006 (annual; by 14 February following the 31 December liquidation -- for accrual year 2026, deposit by Friday 12 February 2027) | NO | Portal round-trip through an operador de informacion, in two selectable modes: online form (Planilla En Linea) or file upload (Envio de Archivo Unificado de Cesantias), .txt/.csv (zipped above 1 MB) or XLS 97-2003 (16 columns A-P, no header row). Operator account credentials only. Explicitly not machine-to-machine: no XSD, no SOAP, no digital signature, no certificate. | OUTBOUND + INBOUND. Outbound: the deposit allocation file. Inbound: planilla number, comprobante PDF and the fund's deposit certificate evidencing compliance with the February deadline. | None published by the authority. <br> Record layouts are nevertheless public, from two independent operator manuals (ACH/SOI and Simple S.A.), and are the basis of CO-CESANTIAS-006. | Not applicable -- manual authority. |

(a)  One operator, ARUS / Enlace Operativo, markets "APIS PILA" and runs a developer portal at https://www.suaporte.com.co/portal-apis/. Fetched on 2026-09-04 it returned only a welcome shell -- no API catalogue, no endpoints, no OpenAPI or WSDL, no authentication description. It is a private commercial offering from one intermediary, available under contract, with no public specification and no statutory standing; it does not generalise across operators and cannot be built from public artefacts. PILA is therefore scored integration=false.

2. Configuration Runbooks

Per-authority Configuration Runbooks are produced only for authorities carrying integration=true. In Colombia that is a single authority, DIAN-NE, whose runbook is filed at 03-statutory-integrations/DIAN-NE/. The authorities scored integration=false -- DIAN-MUISCA, PILA-OI and FONDOS-CESANTIAS -- are manual channels: the obligation is discharged by a human in a browser (a DIAN Muisca web form under a personal IFE, or a file upload to a private operador de informacion), so there is no connection to configure and no runbook is produced for them. Their record layouts, deadlines and validation rules are still fully specified, but they belong to the report specifications in 04-reports-spec rather than to this register. The absence of a runbook for a manual authority is a deliberate scoping decision recorded here, not an omission.

Delivery note: the cesantias deposit has no integration, and late deposit costs one day's salary per day of delay per employee, uncapped (Ley 50 de 1990 art. 99 num. 3). The manual posture therefore concentrates operational risk on the single most expensive Colombian year-end failure, and warrants an explicit controlled manual procedure in delivery planning even though no runbook is written.

Channel types absent from the Colombian landscape entirely: SFTP, REST API published by an authority, AS2 / AS4, government-published message queue.


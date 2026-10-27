# Colombia - Statutory Integration Register (SIR) - COMPLETE REFERENCE

**Source artifacts:**
- `03-statutory-integrations/CO-SIR-INDEX-001-v1.0.docx` (v1.0, 2026-09-04) - the authority index
- `03-statutory-integrations/integration-landscape.json` - the si-discovery landscape (Agent 3 / STAGE 6a)
- `03-statutory-integrations/DIAN-NE/` - the single Configuration Runbook, phases **P1-P7** + `INTERLINKAGES.md`
  + `effort-estimates.md`

**Jurisdiction:** Colombia (CO) - **Currency:** COP - **Tax year:** 2026
**Discovery verdict:** `HAS_INTEGRATIONS`
**Posture:** 4 authorities - **1 genuine machine-to-machine** (DIAN-NE) and **3 manual**. Of the 6 in-scope
filings, **1 is carried system-to-system and 5 are manual.**

> **[QA MAJOR-03 - naming correction]** CCG Module 10 refers to a register `CO-SIR-001 to CO-SIR-007`.
> **No such artifact family exists.** The register is **`CO-SIR-INDEX-001`**, an authority index over 4
> authorities, plus **one** runbook (DIAN-NE) organised as **7 phases P1-P7**. The "007" is a
> mis-transcription of the 7-phase runbook structure.

**Channel types absent from the Colombian landscape entirely:** SFTP - REST API published by an authority -
AS2 / AS4 - government-published message queue.

---

# Part A - Authority Index (CO-SIR-INDEX-001 v1.0, verbatim)


Colombia
Statutory Integration Register -- Authority Index
CO-SIR-INDEX-001  v1.0
Mercans Compliance Regulations Team
Jurisdiction: Colombia (CO)  |  Currency: COP  |  Tax Year 2026
Scope: private-sector salaried population per scope_manifest v1.0 (6 in-scope filings, 7 descoped)
Source: 03-statutory-integrations/integration-landscape.json  |  Discovery verdict: HAS_INTEGRATIONS  |  Generated 2026-09-04
Version Control

| Version | Date | Author | Notes |
|---|---|---|---|
| v1.0 | 2026-09-04 | Mercans Compliance Regulations Team | Initial issue. Authority index generated from integration-landscape.json (produced by si-discovery (Agent 3 / STAGE 6a)). |

1. Authority Index
One row per authority identified in the Colombian payroll statutory landscape. 4 authorities in total: 1 with a genuine system-to-system channel, 3 manual. Of the 6 in-scope filings, 1 is carried system-to-system and 5 are manual.

| Authority | Integration | Channel | Direction(s) | Developer portal | Runbook location |
|---|---|---|---|---|---|
| DIAN-NE DIAN -- Servicio de Validacion de Nomina Electronica Unidad Administrativa Especial Direccion de Impuestos y Aduanas Nacionales (DIAN) Carries: CO-DIAN-NE-MONTHLY-001 (monthly, one document per employee, within the first 10 days of the following month) | YES | Machine-to-machine SOAP 1.2 web service over HTTPS (WS-Addressing, WS-Security timestamp). Operation SendNominaSync on WcfDianCustomerServices, plus GetStatus. Payload is base64 of a ZIP holding one XAdES-EPES-signed UBL 2.1 XML, max 500 KB, UTF-8 only. Authenticated by an X.509 certificate from an ONAC-accredited CA. No portal step in the transmission path; habilitacion (SoftwareID + PIN) is a one-time portal-gated onboarding prerequisite, not a channel. | OUTBOUND + INBOUND -- both legs in one synchronous call. Outbound: signed NominaIndividual / NominaIndividualDeAjuste. Inbound: base64 ApplicationResponse (IsValid, StatusCode, XmlDocumentKey). The inbound leg is a hard dependency, not a receipt -- the CUNE and validation status must be persisted, since deductibility of the payroll cost depends on validation. | https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/documentacion-tecnica-soporte-de-pago-nomina-electronica/ Artefacts BUILD-READY: WSDL, XSD v1.0.6, UBL/XAdES schema set, samples and the 269-page annex, all public with no login. | 03-statutory-integrations/DIAN-NE/ |
| DIAN-MUISCA DIAN -- Servicios Informaticos Electronicos / Muisca Unidad Administrativa Especial Direccion de Impuestos y Aduanas Nacionales (DIAN) Carries: CO-DIAN-F350-MONTHLY-002, CO-DIAN-EXO2276-ANNUAL-005, CO-DIAN-F220-ANNUAL-004 | NO | Portal round-trip (browser). Form 350 is keyed or loaded in the Muisca web form; Formato 2276 v4 is prepared offline in the prevalidador and uploaded as XML through the informacion exogena service. Authenticated by the DIAN Instrumento de Firma Electronica (IFE), which is issued to a natural person and exercised interactively -- the structural reason no M2M path exists. Same legal entity as DIAN-NE, entirely different posture: the electronic payroll web service does not carry these filings. | OUTBOUND only. | None published by the authority. No SOAP, REST or SFTP filing surface exists. Vendor-marketed "DIAN APIs" are commercial wrappers around the e-invoicing service and do not cover Form 350 or exogena -- do not model them as a statutory channel. | Not applicable -- manual authority. |
| PILA-OI PILA -- Planilla Integrada de Liquidacion de Aportes, via a licensed operador de informacion Ministerio de Salud y Proteccion Social (system owner); collection intermediated by private operadores de informacion supervised by the Superintendencia Financiera Carries: CO-PILA-MONTHLY-003 (monthly; 2nd to 16th business day of the following month, by the last two digits of the employer NIT). SENA, ICBF and Cajas de Compensacion ride on this same planilla. | NO | Portal round-trip through a licensed private operador de informacion (SOI/ACH Colombia, Simple S.A., SuAporte/ARUS, Aportes en Linea, Mi Planilla, Asopagos, Compensar). Under Res. MSPS 2388 de 2016 the modalidad electronica is keying the planilla online or uploading a fixed-width flat file (.txt/.csv) to the electronic means made available by the operator; the operator settles, collects and forwards to each administradora. Operator account credentials only -- no certificate, no signature. The employer never transacts directly with the government and there is no government-facing endpoint to integrate with. | OUTBOUND + INBOUND. Outbound: Archivo Tipo 1 (34 fields / 567 positions) and Archivo Tipo 2 (header 22 fields / 359 positions, one Registro Tipo 2 per contributor), fixed-width. Inbound: the operator's settlement/payment output, which must be reconciled (planilla number, payment date, per-contributor rejections) -- operator-specific, with no published layout. | None published by the authority. See note (a) below on the ARUS/SuAporte "Portal Desarrolladores APIS PILA" (https://www.suaporte.com.co/portal-apis/) -- a private commercial offering, deliberately not scored as an integration. | Not applicable -- manual authority. |
| FONDOS-CESANTIAS Fondos de Cesantias -- annual severance-savings deposit allocation Private severance-savings funds (Porvenir, Proteccion, Colfondos, Skandia, FNA), reached through a licensed operador de informacion Carries: CO-CESANTIAS-DEPOSIT-ANNUAL-006 (annual; by 14 February following the 31 December liquidation -- for accrual year 2026, deposit by Friday 12 February 2027) | NO | Portal round-trip through an operador de informacion, in two selectable modes: online form (Planilla En Linea) or file upload (Envio de Archivo Unificado de Cesantias), .txt/.csv (zipped above 1 MB) or XLS 97-2003 (16 columns A-P, no header row). Operator account credentials only. Explicitly not machine-to-machine: no XSD, no SOAP, no digital signature, no certificate. | OUTBOUND + INBOUND. Outbound: the deposit allocation file. Inbound: planilla number, comprobante PDF and the fund's deposit certificate evidencing compliance with the February deadline. | None published by the authority. Record layouts are nevertheless public, from two independent operator manuals (ACH/SOI and Simple S.A.), and are the basis of CO-CESANTIAS-006. | Not applicable -- manual authority. |

(a)  One operator, ARUS / Enlace Operativo, markets "APIS PILA" and runs a developer portal at https://www.suaporte.com.co/portal-apis/. Fetched on 2026-09-04 it returned only a welcome shell -- no API catalogue, no endpoints, no OpenAPI or WSDL, no authentication description. It is a private commercial offering from one intermediary, available under contract, with no public specification and no statutory standing; it does not generalise across operators and cannot be built from public artefacts. PILA is therefore scored integration=false.
2. Configuration Runbooks
Per-authority Configuration Runbooks are produced only for authorities carrying integration=true. In Colombia that is a single authority, DIAN-NE, whose runbook is filed at 03-statutory-integrations/DIAN-NE/. The authorities scored integration=false -- DIAN-MUISCA, PILA-OI and FONDOS-CESANTIAS -- are manual channels: the obligation is discharged by a human in a browser (a DIAN Muisca web form under a personal IFE, or a file upload to a private operador de informacion), so there is no connection to configure and no runbook is produced for them. Their record layouts, deadlines and validation rules are still fully specified, but they belong to the report specifications in 04-reports-spec rather than to this register. The absence of a runbook for a manual authority is a deliberate scoping decision recorded here, not an omission.
Delivery note: the cesantias deposit has no integration, and late deposit costs one day's salary per day of delay per employee, uncapped (Ley 50 de 1990 art. 99 num. 3). The manual posture therefore concentrates operational risk on the single most expensive Colombian year-end failure, and warrants an explicit controlled manual procedure in delivery planning even though no runbook is written.
Channel types absent from the Colombian landscape entirely: SFTP, REST API published by an authority, AS2 / AS4, government-published message queue.


---

# Part B - Integration landscape (`integration-landscape.json`, verbatim)

| Key | Value |
|---|---|
| `country` | Colombia |
| `code` | CO |
| `country_code` | CO |
| `currency` | COP |
| `year` | 2026 |
| `generated` | 2026-09-04 |
| `produced_by` | si-discovery (Agent 3 / STAGE 6a) |
| `verdict` | HAS_INTEGRATIONS |

**Verdict rationale:**

> Colombia has exactly ONE genuine system-to-system statutory channel for payroll: the DIAN electronic payroll validation web service (SOAP 1.2, operation SendNominaSync on WcfDianCustomerServices). This was verified live on 2026-09-04, not inferred: the production WSDL at https://vpfe.dian.gov.co/WcfDianCustomerServices.svc?singleWsdl and the habilitacion WSDL at https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc?singleWsdl both returned HTTP 200 without authentication (61,719 and 61,727 bytes) and both declare wsdl:operation name="SendNominaSync" alongside GetStatus; and the DIAN 'Caja de Herramientas' ZIP downloaded HTTP 200 (5,528,509 bytes) containing NominaIndividualElectronicaXSDV1.0.6.xsd, NominaIndividualDeAjusteElectronicaXSDV1.0.6.xsd, the UBL 2.1 and XAdES schema set, the 269-page technical annex and two sample XMLs. EVERY OTHER Colombian payroll obligation is portal or paper. This is a one-integration country, and the honest reading is that the M2M posture is the exception, not the rule: 3 of the 4 authority channels below are manual, and 5 of the 6 in-scope filings are manual.

**Schema note (verbatim):**

> Agent-schema reconstruction note: the referenced agent definition file .claude/agents/si-discovery.md is NOT present in this pipeline checkout (shared/si-runbook was never installed), so the field set below is derived from the only authoritative consumer of this file - STAGE 6 of mercans_pipeline_v2_9.sh, which reads top-level 'verdict' and iterates 'authorities' selecting entries where integration is boolean true and 'code' is non-empty, and whose index prompt requires per authority: integration yes/no, channel, direction(s), dev portal, runbook location.

**Inputs read:**

- `CO-compliance/scope_manifest.json (scope_version 1.0, 6 in-scope filings, 7 descoped)`
- `CO-compliance/01-ccg/CO-CCG-001-v1.0.docx (Module 10.1 / 10.2)`
- `CO-compliance/_txt/ne_anexo.txt (DIAN Anexo Tecnico Nomina Electronica v1.0, 269 pp, ss. 9.1-9.8)`
- `CO-compliance/_txt/res227.txt (Resolucion DIAN 000227 de 23 Sep 2025, Cap. 12)`
- `CO-compliance/_txt/soi_cesantias.txt (ACH Colombia SOI instructivo cesantias)`
- `CO-compliance/_txt/pagosimple_cesantias.txt (Simple S.A. Manual Cesantias)`
- `CO-compliance/_txt/pila_anexo2.txt (Resolucion MSPS 2388 de 2016, Anexo Tecnico 2)`

## B.1 Summary

| Metric | Value |
|---|---|
| authorities total | **4** |
| authorities with system to system | **1** |
| authorities manual only | **3** |
| in scope filings total | **6** |
| in scope filings via system to system | **1** |
| in scope filings manual | **5** |
| integration postures present | machine-to-machine signed SOAP web service (DIAN electronic payroll only) - government portal round-trip authenticated by a personal electronic signature instrument (DIAN Muisca) - private-intermediary portal round-trip - the employer never reaches the government at all (PILA, cesantias) |
| no channel type found anywhere | SFTP - REST API published by an authority - AS2 / AS4 - government-published message queue |

## B.2 Authorities - full record for each of the 4


### DIAN-NE - DIAN - Servicio de Validacion de Nomina Electronica (Electronic Payroll Validation Service)

- **authority_legal_name**: Unidad Administrativa Especial Direccion de Impuestos y Aduanas Nacionales (DIAN)
- **integration**: True
- **channel_type**: m2m_soap_web_service
- **channel**: Genuine machine-to-machine SOAP 1.2 web service. The electronic payroll document rides on DIAN's existing pre-validation e-invoicing service WcfDianCustomerServices, which exposes the dedicated operation SendNominaSync for synchronous transmission of ONE signed XML document inside a .zip container (max 500 KB, UTF-8 only), plus GetStatus extended to query electronic payroll documents. There is no portal step in the transmission path.
- **directions**:
  - outbound
  - inbound
- **direction_detail**: BOTH, in a single call. Outbound = the signed NominaIndividual / NominaIndividualDeAjuste XML. Inbound = a base64 ApplicationResponse returned synchronously in SendNominaSyncResult (elements IsValid, StatusCode, StatusDescription, StatusMessage, XmlBase64Bytes, XmlDocumentKey). The inbound leg is a HARD dependency, not a receipt: a payroll cost is tax-deductible only where the document was validated, so the engine must parse the response, persist the validation status and the CUNE, and retry or correct rejections.
- **protocol**: SOAP 1.2 (soap12) over HTTPS, WS-Addressing, WS-Security with timestamp; WCF service
- **message_format**: base64 of a ZIP containing one UBL 2.1-signed XML; max 500 KB; UTF-8 only
- **authentication**: Client authenticates with an X.509 digital certificate issued by a certification authority accredited by ONAC (the national accreditation body). The document carries a XAdES-EPES signature with ClaimedRole in {thirdparty, supplier}. The WSDL policy declares sp:TransportBinding + sp:HttpsToken + sp:WssX509... + sp:EndorsingSupportingTokens + sp:IncludeTimestamp.
- **endpoints**:
  - **production**: https://vpfe.dian.gov.co/WcfDianCustomerServices.svc
  - **production_wsdl**: https://vpfe.dian.gov.co/WcfDianCustomerServices.svc?singleWsdl
  - **test_habilitacion**: https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc
  - **test_habilitacion_wsdl**: https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc?singleWsdl
  - **document_lookup_qr**: https://catalogo-vpfe.dian.gov.co/document/searchqr?documentkey=<CUNE>
  - **_endpoint_verification**: WSDLs retrieved 2026-09-04, HTTP 200, no authentication required. Live service endpoints were NOT called.
- **operations_relevant_to_payroll**:
  - **name**: SendNominaSync; **purpose**: Synchronous transmission and validation of one electronic payroll document or adjustment note; **verified_in_wsdl**: True
  - **name**: GetStatus; **purpose**: Query the validation status of a transmitted document (extended by Res. 000013/2021 to cover payroll documents); **verified_in_wsdl**: True
- **operations_present_but_e_invoicing_only**:
  - SendBillSync
  - SendBillAsync
  - SendBillAttachmentAsync
  - SendTestSetAsync
  - SendEventUpdateStatus
  - GetStatusZip
  - GetStatusEvent
  - GetXmlByDocumentKey
  - GetNumberingRange
  - GetAcquirer
  - GetDocumentInfo
  - GetExchangeEmails
  - GetReferenceNotes
- **dev_portal**: https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/documentacion-tecnica-soporte-de-pago-nomina-electronica/
- **public_artefacts**:
  - **name**: Caja de Herramientas Nomina Electronica V1-0 (ZIP); **url**: https://www.dian.gov.co/impuestos/factura-electronica/Documents/Caja-de-Herramientas-Nomina-Electronica-V1-0.zip; **public**: True; **login_required**: False; **verified**: downloaded 2026-09-04, HTTP 200, 5,528,509 bytes, 19 entries
  - **name**: NominaIndividualElectronicaXSDV1.0.6.xsd; **url**: inside Caja de Herramientas /XSD/; **public**: True; **login_required**: False; **verified**: present, 38,799 bytes, targetNamespace dian:gov:co:facturaelectronica:NominaIndividual
  - **name**: NominaIndividualDeAjusteElectronicaXSDV1.0.6.xsd; **url**: inside Caja de Herramientas /XSD/; **public**: True; **login_required**: False; **verified**: present, 48,150 bytes, targetNamespace dian:gov:co:facturaelectronica:NominaIndividualDeAjuste
  - **name**: UBL 2.1 + XAdES v1.3.2 / v1.4.1 + xmldsig schema set (10 xsd); **url**: inside Caja de Herramientas /Schemes/; **public**: True; **login_required**: False; **verified**: present
  - **name**: Sample XML: Nomina Individual Electronica V1.0.2.xml and Nomina Individual De Ajuste Electronica V1.0.2.xml; **url**: inside Caja de Herramientas /Ejemplificaciones/; **public**: True; **login_required**: False; **verified**: present
  - **name**: Anexo Tecnico Documento Soporte de Pago de Nomina Electronica V1.0 (269 pp, incl. ss. 9.1-9.8 web-service spec and the NIE validation-rule tables); **url**: inside Caja de Herramientas /Anexo Tecnico/; **public**: True; **login_required**: False; **verified**: present; also already extracted to CO-compliance/_txt/ne_anexo.txt
  - **name**: Resolucion DIAN 000013 de 11 Feb 2021; **url**: https://www.dian.gov.co/normatividad/Normatividad/Resoluci%C3%B3n%20000013%20de%2011-02-2021.pdf; **public**: True; **login_required**: False; **verified**: URL published on the DIAN micrositio
  - **name**: WSDL (production and habilitacion); **url**: https://vpfe.dian.gov.co/WcfDianCustomerServices.svc?singleWsdl; **public**: True; **login_required**: False; **verified**: HTTP 200 on 2026-09-04, both environments
- **artefact_gaps**:

- **artefact_readiness**: BUILD-READY. The complete artefact set - WSDL, XSD v1.0.6, UBL/XAdES schemas, sample XML and the 269-page annex with the validation-rule tables - is publicly downloadable with no login, no certificate and no CAPTCHA.
- **onboarding_gating**: Portal-gated, one-time, and NOT a technical channel: habilitacion. The issuer must complete the enablement process in the DIAN portal (register own software or a proveedor tecnologico, obtain the SoftwareID and the secret PIN, pass the test set in the habilitacion environment) before transmitting in production; global validation rule 92 rejects any document from a non-enabled issuer. Where Mercans generates or transmits on the client's behalf, Res. 000013/2021 art. 22 additionally requires the provider to be enabled, registered in the RUT, and both parties to retain the mandate document. This is a contractual and administrative precondition to go-live, not an engineering blocker.
- **manual_alternative_exists**: Yes - DIAN publishes a free web solution for electronic payroll (https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/solucion-gratuita-de-nomina-electronica/) aimed at small employers. Irrelevant to an engine implementation, but relevant to fallback and contingency design.
- **filings_carried**:
  - CO-DIAN-NE-MONTHLY-001
- **frequency**: monthly, one document per employee per month regardless of pay frequency (Res. 000013/2021 art. 3)
- **deadline**: within the first 10 days of the month following payment or credit (art. 8)
- **runbook_location**: 03-statutory-integrations/DIAN-NE/
- **evidence**:
  - Anexo Tecnico s. 9.1: 'La DIAN expone sobre el mismo servicio web actual de Factura Electronica en Validacion Previa (WcfDianCustomerServices) una nueva la operacion llamada SendNominaSync para la transmision sincrona de 1 documento electronico ... XML en contenedor .zip y la modificacion de la operacion actual llamada GetStatus'.
  - Anexo Tecnico s. 9.2.1: 'El software cliente realiza la conexion autenticando por medio de certificado digital.'
  - Anexo Tecnico s. 9.7.1: 'Posterior a las validaciones se genera respuesta (Response) sincrona con el detalle de la evaluacion del documento, que incluye dentro de sus elementos un ApplicationResponse codificado en Base64 con la respuesta de validacion de la DIAN.'
  - Anexo Tecnico s. 9.7.2: request and response envelopes reproduced verbatim; action http://wcf.dian.colombia/IWcfDianCustomerServices/SendNominaSyncResponse.
  - Live WSDL retrieval 2026-09-04 (both environments) confirms wsdl:operation name="SendNominaSync" and soap12:address location matching the endpoints above.
- **notes**: One documentation defect worth carrying forward: Anexo Tecnico s. 9.7 states 'Metodo: SendBillSync' in its bullet list while the surrounding section, the request envelope and the WSDL all say SendNominaSync. The WSDL is authoritative - SendNominaSync is the correct operation. Section 14 of the annex is a SOAP UI walkthrough that likewise still shows GetStatus and SendBillAsync examples inherited from the e-invoicing annex.

### DIAN-MUISCA - DIAN - Servicios Informaticos Electronicos / Muisca (tax returns and information returns)

- **authority_legal_name**: Unidad Administrativa Especial Direccion de Impuestos y Aduanas Nacionales (DIAN)
- **integration**: False
- **channel_type**: portal_round_trip
- **channel**: Portal round-trip. Returns and information returns are filed 'en forma virtual a traves de los servicios informaticos electronicos de la DIAN, haciendo uso del Instrumento de Firma Electronica (IFE) emitido por la DIAN'. Form 350 is keyed or loaded in the Muisca web form; Formato 2276 v4 is prepared offline (prevalidador) and uploaded as XML through the informacion exogena service. Same legal entity as DIAN-NE, entirely different posture - the electronic payroll web service does not carry these filings.
- **directions**:
  - outbound
- **protocol**: HTTPS web portal (browser). No SOAP, no REST, no SFTP published for filing.
- **authentication**: Instrumento de Firma Electronica (IFE) - a personal electronic signature instrument issued by DIAN to a NATURAL PERSON (the legal representative, or a person registered under RUT responsabilidad 22, 'Obligados a cumplir deberes formales a nombre de terceros'). Because the IFE binds to a human and is exercised interactively, it cannot be driven unattended; this is the structural reason there is no M2M path here.
- **endpoints**:
  - **portal**: https://muisca.dian.gov.co/
  - **form_350_entry**: https://muisca.dian.gov.co/WebDilIngresoFormReteFuente350/
- **dev_portal**: None
- **public_artefacts**:
  - **name**: Resolucion DIAN 000227 de 23 Sep 2025 (Resolucion Unica en Materia Tributaria, Aduanera y Cambiaria); **url**: already extracted to CO-compliance/_txt/res227.txt; **public**: True; **login_required**: False; **verified**: art. 1.3.12.1 read verbatim
  - **name**: Prevalidador for the informacion exogena formats; **url**: published by DIAN per reporting year; **public**: True; **login_required**: False; **verified**: referenced in Res. 000227/2025 (Prevalidadores, art. 1.1.6.3 pattern); the year-specific build was not pinned this pass
- **artefact_gaps**:
  - No machine-readable layout is published for the Form 350 web form - the form design is a PDF/instructivo, which is why CO-DIAN-002 is spec'd from the form design rather than from a schema.
  - Formato 2276 v4 XML: the field list is prescribed in Res. 000227/2025, but DIAN does not publish a standalone public XSD for exogena formats in the way it does for e-invoicing; the prevalidador is the de facto validator.
- **artefact_readiness**: N/A - no integration to build. Artefacts are needed for the report specifications (04-reports-spec), not for a connection.
- **filings_carried**:
  - CO-DIAN-F350-MONTHLY-002
  - CO-DIAN-EXO2276-ANNUAL-005
  - CO-DIAN-F220-ANNUAL-004
- **filings_note**: CO-DIAN-F220-ANNUAL-004 (Certificado de Ingresos y Retenciones) is listed here for authority attribution only. It is not transmitted to DIAN at all - the employer ISSUES it to each employee and retains it (ET arts. 378-380). Its channel is 'to the employee', so it is neither an integration nor a portal filing.
- **runbook_location**: None
- **evidence**:
  - Resolucion DIAN 000227 de 2025 art. 1.3.12.1 (verbatim): 'La informacion a que se refiere la presente resolucion debe ser presentada en forma virtual a traves de los servicios informaticos electronicos de la Unidad Administrativa Especial Direccion de Impuestos y Aduanas Nacionales (DIAN), haciendo uso del Instrumento de Firma Electronica (IFE) emitido por la DIAN.'
  - Res. 000227/2025 art. 1.3.12.2 sets the pre-filing procedure as RUT registration plus IFE issuance/activation - an identity-and-portal onboarding, with no technical channel registration of any kind.
  - Res. 000227/2025 art. 1.3.12.3 contingency is 'no disponibilidad de los servicios informaticos electronicos', i.e. portal downtime, with an 8-business-day extension - the drafting assumes an interactive service.
  - The same 'servicios informaticos electronicos + IFE' formula recurs across the resolution for every declaration type (e.g. art. 1.2.2.11), confirming it is DIAN's general filing posture, not a quirk of one form.
  - CO-CCG-001 Module 10.1 posture table: 'Form 350 monthly withholding return; Form 220; the information return | Portal round-trip - prepared and submitted through the tax authority's electronic filing portal.'
- **notes**: Searched specifically for a DIAN M2M/API path for declarations; every published DIAN developer surface found is the e-invoicing / payroll validation service. The third-party 'DIAN APIs' marketed by Colombian vendors (MATIAS API, Facturalatam and similar) are commercial wrappers around that same e-invoicing SOAP service - they are not an authority-published API and they do not cover Form 350 or exogena. Do not model them as a statutory channel.

### PILA-OI - PILA - Planilla Integrada de Liquidacion de Aportes, filed through a licensed operador de informacion

- **authority_legal_name**: Ministerio de Salud y Proteccion Social (system owner); collection intermediated by private operadores de informacion supervised by the Superintendencia Financiera
- **integration**: False
- **channel_type**: private_intermediary_portal_file_upload
- **channel**: Portal round-trip through a licensed private operador de informacion. The employer NEVER transacts directly with the government for social security. Under Res. MSPS 2388 de 2016 the 'modalidad electronica' is the contributor using the internet either to key the planilla online or to upload a flat file to the electronic means made available BY THE OPERATOR; the operator settles, collects and forwards to each administradora. There is no government-facing endpoint for the employer to integrate with, and no MinSalud-published API, SFTP or web service.
- **directions**:
  - outbound
  - inbound
- **direction_detail**: Outbound = Archivo Tipo 1 (employer, 34 fields / 567 positions) and Archivo Tipo 2 (header 22 fields / 359 positions plus one Registro Tipo 2 per contributor), fixed-width. Inbound = the operator's settlement/payment output, which the engine must reconcile (planilla number, payment date, per-contributor rejections). The inbound leg is operator-specific and has no published layout.
- **protocol**: HTTPS web portal with browser file upload (.txt / .csv, size-limited, zipped if larger). No published authority protocol.
- **authentication**: Operator account credentials (a commercial relationship), not a government credential. No certificate, no signature on the file.
- **endpoints**:
  - **note**: Operator-specific. Principal licensed operators: ACH Colombia S.A. (SOI, https://www.nuevosoi.com.co and https://www.soi.com.co), Simple S.A. (https://www.pagosimple.com), ARUS / Enlace Operativo (SuAporte, https://www.suaporte.com.co), Aportes en Linea, Mi Planilla, Asopagos, Compensar.
- **dev_portal**: https://www.suaporte.com.co/portal-apis/ (ARUS/SuAporte 'Portal Desarrolladores APIS PILA' - see commercial_api_caveat)
- **commercial_api_caveat**: HONEST FINDING, DELIBERATELY NOT SCORED AS AN INTEGRATION. One operator, ARUS / Enlace Operativo, markets 'APIS PILA' on https://enlace.com.co/pila-empresa/ ('Puedes integrar la plataforma de SUAPORTE con tu software de nomina, para automatizar estos procesos') and runs a 'Portal Desarrolladores APIS PILA' at https://www.suaporte.com.co/portal-apis/. That portal was fetched on 2026-09-04 and returned only a welcome shell - no API catalogue, no endpoints, no OpenAPI or WSDL, no authentication description. This is therefore a PRIVATE COMMERCIAL offering from one intermediary, available under contract, with no public specification and no statutory standing. It is not the statutory channel, it does not generalise across operators, it would change if the client switches operator, and it cannot be built from public artefacts. Scoring PILA integration=true on this basis would fabricate a buildable integration. Recommendation: treat as a CLIENT-SPECIFIC OPTIMISATION to be scoped only once the client's operator is fixed and that operator supplies its contract.
- **public_artefacts**:
  - **name**: Resolucion MSPS 2388 de 2016 and Anexo Tecnico 2 (record layouts); **url**: https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/DIJ/resolucion-2388-2016.pdf; **public**: True; **login_required**: False; **verified**: already extracted to CO-compliance/_txt/pila_anexo2.txt
  - **name**: Decreto 1990 de 2016 (deadlines, rounding, obligated parties); **url**: already extracted to CO-compliance/_txt/Decreto_1990_de_2016.txt; **public**: True; **login_required**: False; **verified**: True
- **artefact_gaps**:
  - No published inbound settlement-response layout from any operator - the return leg is operator-specific and not publicly documented.
  - Byte-exact positions of Archivo Tipo 2 Registro Tipo 2 not confirmed this pass (already recorded as a known gap in scope_manifest).
- **artefact_readiness**: N/A for connection purposes - there is nothing to connect to. The outbound record layout IS public and is the basis of CO-PILA-003.
- **filings_carried**:
  - CO-PILA-MONTHLY-003
- **frequency**: monthly
- **deadline**: 2nd to 16th business day of the following month, by the last two digits of the employer NIT
- **runbook_location**: None
- **evidence**:
  - Res. MSPS 2388 de 2016: the 'modalidad Electronica' is the contributor paying via internet, online or by uploading flat files, through the electronic means provided by the operador de informacion; operadores are private entities authorised under Superintendencia Financiera supervision that settle and forward to the administradoras.
  - CO-CCG-001 Module 10.1 posture table: 'Integrated social-security contribution return | Portal round-trip through a licensed private information operator. The employer never reaches the government directly for social security.'
  - scope_manifest CO-PILA-MONTHLY-003 channel field states the same, independently.
- **notes**: The three payroll levies (SENA, ICBF, Cajas de Compensacion) ride on this same planilla, so there is no separate parafiscal channel to discover. UGPP is an enforcement and audit body, not a filing recipient, and receives nothing from payroll on a periodic basis.

### FONDOS-CESANTIAS - Fondos de Cesantias - annual severance-savings deposit allocation

- **authority_legal_name**: Private severance-savings funds (Porvenir, Proteccion, Colfondos, Skandia, FNA), reached through a licensed operador de informacion
- **integration**: False
- **channel_type**: private_intermediary_portal_file_upload
- **channel**: Portal round-trip through an operador de informacion, in two selectable modes: online form (Planilla En Linea) or file upload (Envio de Archivo Unificado de Cesantias). Explicitly NOT machine-to-machine: no XSD, no SOAP, no digital signature, no certificate. The channel returns a planilla number, a comprobante PDF and post-payment reports; the fund itself issues the deposit certificate.
- **directions**:
  - outbound
  - inbound
- **direction_detail**: Outbound = the deposit allocation file. Inbound = planilla number, comprobante and the fund's deposit confirmation evidencing compliance with the February deadline.
- **protocol**: HTTPS web portal with browser file upload; permitted formats .txt and .csv (SOI, zipped above 1 MB), or XLS 97-2003 (16 columns A-P), no header row.
- **authentication**: Operator account credentials. No certificate, no signature.
- **endpoints**:
  - **note**: Operator-specific: SOI (ACH Colombia S.A.) https://www.nuevosoi.com.co, Simple S.A. https://www.pagosimple.com, and the other licensed operators.
- **dev_portal**: None
- **public_artefacts**:
  - **name**: ACH Colombia S.A. - SOI instructivo cesantias DDS-DES-INS-008 v2; **url**: already extracted to CO-compliance/_txt/soi_cesantias.txt; **public**: True; **login_required**: False; **verified**: s. 2.1.4 'Liquidacion Por Archivo' read - browser Examinar upload, .txt/.cvs, zip above 1 MB, on-screen Excel error report
  - **name**: Simple S.A. - Manual Cesantias ss. 3.1-3.2 (20 fields / 258 positions fixed-width; 16-column XLS); **url**: already extracted to CO-compliance/_txt/pagosimple_cesantias.txt; **public**: True; **login_required**: False; **verified**: True
  - **name**: Ley 50 de 1990 art. 99; Ley 2466 de 2025 art. 64; **url**: already extracted to CO-compliance/_txt/ley2466.txt; **public**: True; **login_required**: False; **verified**: True
- **artefact_gaps**:
  - No published layout for the fund's inbound deposit confirmation - fund-specific.
- **artefact_readiness**: N/A for connection purposes. The outbound layout IS public (two independent operator manuals) and is the basis of CO-CESANTIAS-006.
- **filings_carried**:
  - CO-CESANTIAS-DEPOSIT-ANNUAL-006
- **frequency**: annual
- **deadline**: by 14 February of the year following the 31 December liquidation (Ley 50 de 1990 art. 99 num. 3). For accrual year 2026 the last day is Sunday 14 February 2027 - deposit by Friday 12 February 2027.
- **runbook_location**: None
- **evidence**:
  - SOI instructivo s. 2.1.4: the file is loaded with a browser 'Examinar' button from the machine the user logged in from; formats .txt and .cvs; files over 1 MB must be zipped; structural errors are returned as an on-screen Excel report to be corrected and re-uploaded. That is an interactive portal upload, not an M2M channel.
  - scope_manifest CO-CESANTIAS-DEPOSIT-ANNUAL-006 channel field, independently verified against two operator manuals: 'Not machine-to-machine: no XSD, no SOAP, no signature, no certificate.'
- **notes**: Late deposit costs one day's salary per day of delay per employee, uncapped. The absence of an integration therefore raises operational risk on the single most expensive Colombian year-end failure - worth calling out in delivery planning even though there is no runbook to write.

## B.3 Non-authority flows excluded from the verdict

| ID | Name | Counterparty | Why excluded |
|---|---|---|---|
| CO-OUT-BANKFILE | Bank payment file | The client's paying bank | A commercial bank is not a statutory authority and receives no statutory payroll data. Format is bank-specific; the bank-entity code catalogue must be obtained per client. Colombia does not use IBAN. Owned upstream by the client's bank (CCG control B7). |
| CO-IN-EPS-ARL-BENEFIT | EPS / ARL benefit determinations | Health insurers (EPS) and occupational-risk insurers (ARL) | Inbound and in scope for the ENGINE (product_mapping_required true), but there is no integration to discover: recognition is an act of the insurer, there are dozens of EPS and several ARL, and not one publishes a file format, schema or column layout. Retrieval is per-insurer portal export. Revisit only if a client standardises on one EPS/ARL and supplies that institution's layout. |
| CO-IN-LIBRANZA-SCHEDULE | Libranza instalment schedule | Private payroll lenders (entidades operadoras de libranza, Ley 1527 de 2012) | Not a government-to-employer flow. Lender-specific format, no published schema, owned upstream by the lender. |
| CO-OUT-PAYSLIP | Graphical representation of the payroll document (payslip) to the employee | The employee | Not an authority. Permissive under Res. 000013/2021 art. 24; if issued it must carry the art. 5 content and a QR of at least 2 cm on every page. |

## B.4 Out-of-scope authorities

| Code | Name | Channel | Integration | Status |
|---|---|---|---|---|
| MINTRABAJO | Ministerio del Trabajo - disability-hiring contract report (within 15 days of signature) | Portal | False | OUT OF SCOPE per scope_manifest (CO-MINTRABAJO-DISCAPACIDAD-REPORT, HR-scope: needs MinSalud disability certification and a permanent-headcount census by 100-employee tranche; more than 50% of fields originate in the HRMS). Appears in CO-CCG-001 as CO-RPT-007; the manifest governs. No integration in any case. |
| SENA-CUOTA | SENA - apprentice quota determination and monetisation | Portal | False | OUT OF SCOPE per scope_manifest (HR-scope; the quota is fixed by SENA on headcount by occupation, and monetisation is a treasury payment). The apprentice's maintenance support and contributions ARE in scope and ride on PILA-OI and DIAN-NE. |
| RUAF-ND | RUAF-ND vital-events registry | Portal | False | OUT OF SCOPE per scope_manifest (HR-scope; sourced from civil-registry documents, reported by health providers and HR). |

## B.5 Research method

- **primary_sources_read_verbatim**: True
- **live_verification_performed**:
  - GET https://vpfe.dian.gov.co/WcfDianCustomerServices.svc?singleWsdl -> HTTP 200, 61,719 bytes, SendNominaSync present
  - GET https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc?singleWsdl -> HTTP 200, 61,727 bytes, SendNominaSync present
  - GET https://www.dian.gov.co/impuestos/factura-electronica/Documents/Caja-de-Herramientas-Nomina-Electronica-V1-0.zip -> HTTP 200, 5,528,509 bytes, XSD v1.0.6 confirmed inside
  - GET https://enlace.com.co/pila-empresa/ -> 'APIS PILA' marketing section confirmed
  - GET https://www.suaporte.com.co/portal-apis/ -> welcome shell only, no public API catalogue
- **live_service_endpoints_called**: False
- **logins_accounts_certificates_captchas_used**: False
- **negative_findings_searched_for**:
  - DIAN M2M/API path for Form 350 or informacion exogena - none found; the only authority-published developer surface is the e-invoicing / payroll SOAP service
  - MinSalud or government-published PILA API/SFTP/web service - none found; the statute routes the employer through a private operator
  - Asofondos or fund-published cesantias web service - none found; two independent operator manuals describe browser file upload
  - SFTP anywhere in the Colombian payroll statutory landscape - none found

## B.6 Open questions

- Whether any licensed PILA operador besides ARUS/SuAporte offers a contractual API, and what the ARUS 'APIS PILA' catalogue actually contains - the developer portal renders no public content. Closeable only with an operator commercial contact, and only worth doing once the client's operator is fixed.
- Whether DIAN publishes a standalone XSD for Formato 2276 v4 in the reporting-year prevalidador release, or whether the prevalidador remains the only validator. Affects 04-reports-spec fidelity, not the integration verdict.

## B.7 Sources (15)

| Title | URL | Type | Retrieved |
|---|---|---|---|
| DIAN WcfDianCustomerServices WSDL (production) | https://vpfe.dian.gov.co/WcfDianCustomerServices.svc?singleWsdl | primary | 2026-09-04 |
| DIAN WcfDianCustomerServices WSDL (habilitacion) | https://vpfe-hab.dian.gov.co/WcfDianCustomerServices.svc?singleWsdl | primary | 2026-09-04 |
| DIAN Caja de Herramientas Nomina Electronica V1-0 (annex + XSD v1.0.6 + UBL/XAdES + samples) | https://www.dian.gov.co/impuestos/factura-electronica/Documents/Caja-de-Herramientas-Nomina-Electronica-V1-0.zip | primary | 2026-09-04 |
| DIAN micrositio - documentacion tecnica soporte de pago de nomina electronica | https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/documentacion-tecnica-soporte-de-pago-nomina-electronica/ | primary | 2026-09-04 |
| Resolucion DIAN 000013 de 11 Feb 2021 and Anexo Tecnico v1.0 (269 pp) | https://www.dian.gov.co/normatividad/Normatividad/Resoluci%C3%B3n%20000013%20de%2011-02-2021.pdf | primary | prior pass, extracted to _txt/ne_anexo.txt |
| Resolucion DIAN 000227 de 23 Sep 2025 - Resolucion Unica, Cap. 12 arts. 1.3.12.1-1.3.12.5 | https://www.dian.gov.co/normatividad/Paginas/ResolucionUnica.aspx | primary | prior pass, extracted to _txt/res227.txt |
| Resolucion MSPS 2388 de 2016 and Anexo Tecnico 2 (PILA layouts) | https://www.minsalud.gov.co/sites/rid/Lists/BibliotecaDigital/RIDE/DE/DIJ/resolucion-2388-2016.pdf | primary | prior pass, extracted to _txt/pila_anexo2.txt |
| ACH Colombia S.A. - SOI instructivo cesantias DDS-DES-INS-008 v2 | https://www.nuevosoi.com.co/ | primary | prior pass, extracted to _txt/soi_cesantias.txt |
| Simple S.A. - Manual Cesantias ss. 3.1-3.2 | https://www.pagosimple.com/ | primary | prior pass, extracted to _txt/pagosimple_cesantias.txt |
| DIAN Muisca - Form 350 entry point | https://muisca.dian.gov.co/WebDilIngresoFormReteFuente350/ | primary | 2026-09-04 |
| DIAN - solucion gratuita de nomina electronica | https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/solucion-gratuita-de-nomina-electronica/ | primary | 2026-09-04 |
| ARUS / Enlace Operativo - PILA empresa, 'APIS PILA' section | https://enlace.com.co/pila-empresa/ | commercial | 2026-09-04 |
| ARUS / SuAporte - Portal Desarrolladores APIS PILA (no public catalogue) | https://www.suaporte.com.co/portal-apis/ | commercial | 2026-09-04 |
| CO-CCG-001 v1.0 Module 10.1 / 10.2 | CO-compliance/01-ccg/CO-CCG-001-v1.0.docx | internal | 2026-09-04 |
| CO scope_manifest.json v1.0 | CO-compliance/scope_manifest.json | internal | 2026-09-04 |


---

# Part C - DIAN-NE Configuration Runbook (the only integrable authority), phases P1-P7

Reproduced in full from `03-statutory-integrations/DIAN-NE/`. This is the **only** Configuration Runbook
produced for Colombia: DIAN-MUISCA, PILA-OI and FONDOS-CESANTIAS all carry `integration: false` and are
manual channels, so there is no connection to configure. That absence is a deliberate scoping decision,
not an omission.



---

## C.0 Phase index and readiness statement

<!-- source: 03-statutory-integrations\DIAN-NE\_phase-index.md -->

### CO / DIAN-NE — Statutory Integration Configuration Runbook

**Country:** Colombia (CO) · **Authority code:** DIAN-NE
**Authority:** DIAN — Servicio de Validación de Nómina Electrónica (Electronic Payroll Validation Service)
**Legal name:** Unidad Administrativa Especial Dirección de Impuestos y Aduanas Nacionales (DIAN)
**Directions:** outbound + inbound (both, in a single synchronous call)
**Mode:** structural
**Research date:** 2026-09-04
**Artefact readiness:** **BUILD-READY** — 0 technical artefact gaps

---

#### Readiness statement

Every artefact needed to build this integration is in hand and was downloaded from public DIAN
endpoints with **no login, no certificate, no CAPTCHA**: the live WSDL for both environments, the
two payroll XSDs (v1.0.6), the full UBL 2.1 / XAdES schema set, the 269-page Anexo Técnico
containing the web-service specification and all 433 validation rules, and the governing
resolution. There are **no `[[NEEDS-ARTEFACT]]` markers in this runbook.**

The only items not in hand are **per-tenant secrets issued during onboarding** — the `SoftwareID`,
the software `PIN`, and the ONAC-accredited X.509 signing certificate. These are credentials, not
artefacts: they are issued to a named taxpayer at habilitación time and cannot exist before a
client engagement. They are tracked in P6, not as artefact gaps.

#### Phase deliverables

| Phase | File | Covers |
|---|---|---|
| **P1** | `P1-authority-channel-profile.md` | Authority, legal basis, obligation scope, filing calendar, endpoints, artefact manifest |
| **P2** | `P2-connectivity-and-security.md` | SOAP 1.2 binding, TLS, WS-Security/X.509, XAdES-EPES signing, secret handling |
| **P3** | `P3-outbound-payload-spec.md` | `NominaIndividual` / `NominaIndividualDeAjuste` structure, code tables, CUNE, SoftwareSC, ZIP packaging |
| **P4** | `P4-inbound-response-handling.md` | `DianResponse`, base64 `ApplicationResponse`, status codes, CUNE persistence, `GetStatus` |
| **P5** | `P5-validation-rules-and-error-handling.md` | 433 validation rules, R/N semantics, correction via notas de ajuste, statutory contingency |
| **P6** | `P6-test-and-certification-habilitacion.md` | Habilitación onboarding, test environment, go-live gate, third-party mandate |
| **P7** | `P7-operations-monitoring-maintenance.md` | Volumes, scheduling, reconciliation, retention, monitoring, version watch |
| — | `INTERLINKAGES.md` | Dependencies on CO payroll engine and cross-references to the other three CO authorities |
| — | `effort-estimates.md` | Build effort by phase, with drivers and risk loading |

#### Source artefacts

All under `CO-compliance/integration-sources/dian-ne/` — 23 files, 20,387,117 bytes,
SHA-256 recorded in `SHA256SUMS.txt`. See P1 §7 for the annotated manifest.

#### Scope

Scoped to **DIAN-NE only**. Colombia's other three payroll-data authorities (DIAN-MUISCA, PILA-OI,
FONDOS-CESANTIAS) all carry `integration: false` in the landscape and are cross-referenced in
`INTERLINKAGES.md` only — no runbooks are produced for them.

#### Provenance note on this runbook's structure

The pipeline invokes this work through `.claude/agents/si-runbook-research.md`, backed by
`shared/si-runbook/`. **That shared module is not installed in this checkout** — neither the agent
definition nor `si_scope_check.py` exists, and no prior country in the pipeline has a per-authority
P1–P7 runbook set to copy. The seven-phase decomposition above is therefore **reconstructed**, from
the stage-6 contract in `mercans_pipeline_v2_9.sh` and from the natural build sequence of a
validated-document integration. If the canonical `si-runbook` module is later installed and defines
different phase boundaries, the *content* here maps across cleanly, but the *file names* will need
renaming and `si_scope_check.py` should be re-run against this folder.


---

## C.1 P1 - Authority and channel profile

<!-- source: 03-statutory-integrations\DIAN-NE\P1-authority-channel-profile.md -->

### P1 — Authority & Channel Profile

**CO / DIAN-NE** · Documento Soporte de Pago de Nómina Electrónica (DSPNE)
Research date 2026-09-04 · all facts below traced to a downloaded artefact.

---

#### 1. The authority and what it receives

**DIAN** (Unidad Administrativa Especial Dirección de Impuestos y Aduanas Nacionales) is Colombia's
national tax and customs authority. The **Servicio de Validación de Nómina Electrónica** is not a
standalone system: it is the pre-validation e-invoicing platform (`WcfDianCustomerServices`) with
one added operation and one extended operation.

What DIAN receives is the **Documento Soporte de Pago de Nómina Electrónica** — one signed XML
document per employee per month, carrying that employee's full accrual and deduction detail.

**Critical framing:** this is *not* a tax return and *not* a remittance. It is a **deductibility
instrument**. Under Res. 000013/2021 art. 4, the obligated parties are income-tax payers who need
to *support costs and deductions* in the income tax return (and discountable VAT where applicable).
A payroll cost that was never validated by DIAN is not supportable. That makes the inbound
validation leg a hard business dependency, not a receipt — see P4.

#### 2. Legal basis

| Instrument | Role |
|---|---|
| **Resolución DIAN 000013 de 11 Feb 2021** | Creates the document, defines obligated parties, periodicity, deadlines, habilitación, adjustment notes, retention. 37 articles. |
| **Anexo Técnico DSPNE Versión 1.0** | Issued under art. 20 of the resolution. 269 pp. Binding technical spec: field tables, code tables, CUNE, signature, web service, 433 validation rules. |
| **Estatuto Tributario arts. 572, 573** | Basis for third-party representation (art. 22 of the resolution). |
| **ET art. 632; Ley 962/2005 art. 46 (as amended by Ley 1819/2016 art. 304); Ley 527/1999 arts. 12–13** | Retention and evidential-value regime (art. 23). |
| **ONAC Circular 03-2016** | Digital-certificate accreditation regime referenced by the signature policy. |

#### 3. Obligation scope, periodicity, deadline

- **Obligated parties** (art. 4) — income-tax contributors making payments or credits arising from
  an employment or statutory/regulatory relationship, and payments to pensioners borne by the
  employer, where they need to support costs/deductions.
- **Periodicity** (art. 3) — **monthly, always.** One document per beneficiary per month
  *regardless of actual pay frequency*. Where the employer pays weekly, biweekly or semi-monthly,
  the month's liquidations are **accumulated** into a single monthly document per employee. This is
  the single most important scoping fact for the payroll engine — see INTERLINKAGES §2.
- **Deadline** (art. 8) — within the **first ten (10) days of the month following** the payment or
  credit in account.
- **Granularity** (art. 12) — transmitted **one by one**, per beneficiary. There is no batch
  operation. Volume = headcount per month.

#### 4. Channel

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

#### 5. Endpoints

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

#### 6. Onboarding gate (not a technical channel)

Before production transmission the issuer must complete **habilitación** in the DIAN portal:
register its own software or a proveedor tecnológico, obtain the `SoftwareID` and secret `PIN`, and
pass the test set in the habilitación environment. **Global rule 92 rejects any document from a
non-enabled issuer.** Where Mercans generates or transmits on a client's behalf, art. 22
additionally requires the third party to be enabled by DIAN, to register that capacity in the RUT,
and both parties to retain the mandate document. This is an administrative precondition to go-live,
handled in P6 — it is not an engineering blocker and does not sit in the transmission path.

**Fallback:** DIAN publishes a free web solution for electronic payroll aimed at small employers
(`https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/solucion-gratuita-de-nomina-electronica/`).
Irrelevant to an engine build, but relevant to contingency design — see P7 §5.

#### 7. Artefact manifest

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

#### 8. Documentation defects found in the published artefacts

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


---

## C.2 P2 - Connectivity and security

<!-- source: 03-statutory-integrations\DIAN-NE\P2-connectivity-and-security.md -->

### P2 — Connectivity & Security

**CO / DIAN-NE** · SOAP 1.2 / WS-Security / XAdES-EPES
All binding facts below are read from the **live WSDL retrieved 2026-09-04**, which is authoritative
over the prose in the Anexo Técnico wherever the two disagree.

---

#### 1. Transport and binding

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

#### 2. Operation surface and the do-not-call boundary

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

##### `SendNominaSync` message contract

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

#### 3. Authentication — resolving the spec/WSDL conflict

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

#### 4. Certificates

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

#### 5. Message packaging

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

#### 6. Secrets inventory

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

#### 7. Network and infrastructure checklist

- [ ] Egress to `vpfe.dian.gov.co:443` and `vpfe-hab.dian.gov.co:443` allow-listed.
- [ ] TLS 1.2 with the server's chain trusted; no client certificate on the socket (see §3).
- [ ] Per-tenant keystore provisioned; thumbprint reference verified against the WSDL requirement.
- [ ] Clock synchronised to NTP — `wsu:Timestamp` is mandatory and `Layout=Strict`; skew causes
      hard failures. DIAN's own sample shows a **5-minute** Created→Expires window.
- [ ] WS-Addressing `To`/`Action` populated and `To` signed.
- [ ] SOAP client wrapper exposes only `SendNominaSync` and `GetStatus` (§2).
- [ ] Outbound retry/backoff policy defined, honouring the statutory 48-hour rule (P5 §5).


---

## C.3 P3 - Outbound payload specification

<!-- source: 03-statutory-integrations\DIAN-NE\P3-outbound-payload-spec.md -->

### P3 — Outbound Payload Specification

**CO / DIAN-NE** · `NominaIndividual` and `NominaIndividualDeAjuste`, XSD **v1.0.6**
Structure below is read directly from the shipped XSDs, not paraphrased from the annex.

---

#### 1. The two document types

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

#### 2. `NominaIndividual` — top-level structure

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

#### 3. `Devengados` (accruals)

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

#### 4. `Deducciones`

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

#### 5. CUNE — and a defect that will cost you a day

##### Specification (Anexo §8.1.1.1)

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

##### ⚠ The published worked example does not reproduce

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

#### 6. `SoftwareSC` (software security code)

```
SoftwareSC = SHA-384( SoftwareID + PIN + NroDocumento )
```

where `NroDocumento` = `…/NumeroSecuenciaXML/@Numero` (the `Reemplazar` or `Eliminar` path for
adjustment notes). Note this is **per document**, not a constant — it varies with the sequence
number, so it must be recomputed for every employee every month.

No worked example is published for `SoftwareSC`, so it carries the same
verify-at-habilitación status as the CUNE.

#### 7. Code tables (Anexo §5)

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

#### 8. `NominaIndividualDeAjuste` (adjustment notes)

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
- Per Res. art. 17, the note must reference the number and the CUNE-generation date of the document
  it adjusts, and carry its own internal consecutive number.
- Deletion **invalidates but does not remove**: the annex states the original documents continue to
  exist in DIAN's database, flagged with the deletion. Retention obligations therefore still apply.

#### 9. Numbering, rounding and sign conventions

- **Numbering** (`NumeroSecuenciaXML`): `@Prefijo` + `@Consecutivo`, with `@Numero` carrying the
  concatenation. Unlike e-invoicing, **there is no DIAN-authorised numbering range** for payroll —
  `GetNumberingRange` is an e-invoicing operation and is out of scope (P2 §2). The consecutive is
  the issuer's own internal series. Adjustment notes carry their own separate series (art. 17 ¶2).
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

#### 10. Reference instances — what is and is not available

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


---

## C.4 P4 - Inbound response handling

<!-- source: 03-statutory-integrations\DIAN-NE\P4-inbound-response-handling.md -->

### P4 — Inbound Response Handling

**CO / DIAN-NE** · `SendNominaSyncResult` (`DianResponse`) + embedded `ApplicationResponse`

---

#### 1. Why the inbound leg is not optional

DIAN-NE is a **both-directions** integration in a single synchronous call, and the inbound half
carries the business value. Under Res. 000013/2021 art. 4 the document exists to *support costs and
deductions in the income-tax return*. A document that was generated and transmitted but not
**validated** does not do that job.

So the response is not a delivery receipt to be logged and discarded. The engine must parse it,
persist the validation verdict and the CUNE, and drive correction or retry from it. An
implementation that fires `SendNominaSync` and ignores the return value is not merely incomplete —
it silently produces non-deductible payroll cost.

#### 2. `DianResponse` — the synchronous envelope

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

##### Using `XmlDocumentKey` as the CUNE oracle

`XmlDocumentKey` is DIAN's own record of the document's CUNE. Because the locally computed CUNE
cannot be verified offline (P3 §5), this field is the practical oracle:

> During habilitación, compare the locally computed `InformacionGeneral/@CUNE` against the returned
> `XmlDocumentKey` on every submission. A mismatch on an otherwise-accepted document is the signal
> that the CUNE composition is wrong. Keep this comparison as a **permanent production assertion**,
> not just a test-phase check — it is a free, continuous integrity check on the hash inputs, and it
> is how you will detect a silent format regression (e.g. a locale change altering decimal
> formatting) before it becomes a mass rejection.

#### 3. `ApplicationResponse` — the evidentiary document

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
Res. art. 23 / Ley 527/1999 arts. 12–13. Store the exact base64 or its exact decoded bytes.

#### 4. Persistence contract

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

Retention per Res. art. 23 → ET art. 632 and Ley 962/2005 art. 46 (as amended by Ley 1819/2016
art. 304): retain for the statutory period with the information **accessible for later
consultation**. Archive-to-cold-storage is acceptable; archive-to-unreadable is not. See P7 §3.

#### 5. `GetStatus` — the reconciliation path

`GetStatus` was extended by Res. 000013/2021 to cover payroll documents. It takes the CUNE (the
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

#### 6. Response-handling decision logic

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


---

## C.5 P5 - Validation rules and error handling

<!-- source: 03-statutory-integrations\DIAN-NE\P5-validation-rules-and-error-handling.md -->

### P5 — Validation Rules & Error Handling

**CO / DIAN-NE** · Anexo Técnico §6 (rules) + Res. 000013/2021 arts. 13, 14, 17

---

#### 1. Rule inventory

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

#### 2. R / N semantics

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

#### 3. Rule 90 — the operational constraint that shapes everything

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

#### 4. Failure taxonomy and remediation

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

#### 5. Statutory contingency — the 48-hour rules

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

#### 6. Correction flow

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

#### 7. Risk register

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


---

## C.6 P6 - Test, certification and habilitacion

<!-- source: 03-statutory-integrations\DIAN-NE\P6-test-and-certification-habilitacion.md -->

### P6 — Test & Certification (Habilitación)

**CO / DIAN-NE** · Res. 000013/2021 arts. 9, 22 · Anexo Técnico §9.2.1, §14

---

#### 1. What habilitación is

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

#### 2. Prerequisites checklist

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

#### 3. Test environment

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

#### 4. Why this phase needs iteration budget, not a single pass

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

#### 5. Test sequence

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

#### 6. Coverage matrix

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

#### 7. Tooling

Annex **§14** is a SOAP UI walkthrough: create a SOAP project from the WSDL (§14.4), configure the
**Keystore** (§14.6), **WS-Security Signature** (§14.7) and **Timestamp** (§14.8), then WS-A
addressing (§14.9).

Use it for the *security configuration*, which is where it is genuinely helpful and which
corroborates the message-level reading of the auth model (P2 §3). **Ignore its request examples** —
§14.10–14.12 still show `GetStatus` and `SendBillAsync` inherited verbatim from the e-invoicing
annex, and were never updated for payroll (P1 §8 defect 4).

#### 8. Go-live gate

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


---

## C.7 P7 - Operations, monitoring and maintenance

<!-- source: 03-statutory-integrations\DIAN-NE\P7-operations-monitoring-maintenance.md -->

### P7 — Operations, Monitoring & Maintenance

**CO / DIAN-NE** · steady-state running of the electronic-payroll integration

---

#### 1. The operating cycle

| | |
|---|---|
| Frequency | **Monthly**, always (Res. art. 3) — irrespective of the client's pay cycle |
| Unit | **One document per employee per month** (art. 12: transmitted one by one) |
| Deadline | Within the **first 10 days** of the month following payment/credit (art. 8) |
| Volume | = active headcount, plus adjustment notes |

There is no batch operation, so the monthly run is *N* synchronous calls where *N* is headcount.

**Schedule to finish well before the 10th.** The deadline is a hard statutory date and the failure
modes ahead of it — rejections needing correction and resubmission under new consecutives (P5 §3),
DIAN-side outages triggering the 48-hour contingency (P5 §5) — all consume calendar time. A run
starting on the 9th has no recovery room. Target completion by roughly the 5th and treat the 6th–10th
as remediation window.

#### 2. Throughput

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

#### 3. Retention

Res. art. 23 → ET art. 632, Ley 962/2005 art. 46 (as amended by Ley 1819/2016 art. 304), and
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

#### 4. Monitoring

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

- Endpoint availability. Distinguish **DIAN outage** (art. 13) from **own-system failure**
  (art. 14) — different legal clocks, both 48 hours, both needing evidence (P5 §5). Log outage start
  and end per tenant.
- **Certificate expiry**, with generous lead time. Expiry mid-cycle stops all transmission for the
  tenant. Alert at 90/60/30 days. Renewal is a procurement action with an ONAC-accredited CA and is
  not instant.
- Consecutive-series health: monotonicity, no duplicates. Gaps are fine.

**Alerting thresholds** — page on: any rule-92 rejection (issuer enablement lost, blocks
everything); any CUNE mismatch; rejection rate above baseline; unvalidated documents remaining after
day 7.

#### 5. Contingency

| Scenario | Response |
|---|---|
| DIAN service down | Queue; resume within **48 h of the day following restoration** (art. 13). Evidence the window. |
| Own systems down | Same 48-hour rule from the day following resolution (art. 14). |
| Certificate expired | Transmission stops entirely. No workaround — renew. Prevent via §4 monitoring. |
| Enablement lost (rule 92) | All traffic blocked. Escalate to DIAN; this is administrative, not technical. |
| Ambiguous outcome (timeout) | **`GetStatus` before any resubmission** (P4 §5). Never blind-retry. |
| Sustained inability to transmit | DIAN's free web solution exists for small employers but is manual and does not scale — realistic only as a last resort for a very small population. |

#### 6. Version watch

Static as at 2026-09-04: **Anexo Técnico v1.0**, XSD **v1.0.6**, sample XML v1.0.2. Probing
confirmed no `V1-1`/`V1.1`/`V1-2`/`V1-0-1` toolkit exists (P1 §7).

Watch quarterly:

- `https://micrositios.dian.gov.co/sistema-de-facturacion-electronica/documentacion-tecnica-soporte-de-pago-nomina-electronica/`
  — the toolkit ZIP URL is stable, so **diff the ZIP by SHA-256** against
  `SHA256SUMS.txt` rather than eyeballing the page.
- DIAN normatividad for resolutions amending 000013/2021.
- Re-fetch both WSDLs and diff — a new operation or a changed policy is the earliest technical signal
  of a regime change.

Also watch **outside** DIAN, because two things in the annex can go stale without the annex changing:

- **Overtime and surcharge percentages** (P3 §7) are hard-coded 2021 statutory rates. A labour-law
  change makes the annex wrong while the schema stays valid — cross-check the seven rates against the
  CO CCG annually.
- **`TipoTrabajador`** mirrors the PILA cotizante codes, which are maintained by MinSalud on a
  different cycle (INTERLINKAGES §3).

#### 7. Runbook quick reference

| Symptom | First check |
|---|---|
| All documents rejected | Rule 92 (enablement); certificate validity; `Ambiente` vs endpoint |
| One document rejected, `IsValid=false` | Parse `ErrorMessage[]`; map ID → remediation; resubmit under a **new** consecutive |
| "Documento procesado anteriormente" | Rule 90 — number reused. Allocate new consecutive. Check for a retry loop. |
| Timeout / no response | `GetStatus(CUNE)` before anything else |
| CUNE ≠ `XmlDocumentKey` | Hash-input regression — check decimal truncation, date/time format, PIN, `Ambiente` |
| Security fault at transport | Clock skew (`wsu:Timestamp`); thumbprint reference; `To` header signed? |
| Signature rejected | XAdES profile — digest not SHA-1, `SignaturePolicyId` hash, `ClaimedRole` |


---

## C.8 Interlinkages - payroll-engine dependencies and the other three authorities

<!-- source: 03-statutory-integrations\DIAN-NE\INTERLINKAGES.md -->

### INTERLINKAGES — DIAN-NE

How DIAN-NE depends on the CO payroll engine, and how it relates to Colombia's other three
payroll-data authorities. **Cross-reference only** — no runbooks exist for the other three, because
all three carry `integration: false`.

---

#### 1. Position in the CO landscape

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

#### 2. Upstream dependencies on the CO payroll engine

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

#### 3. Relationship to PILA-OI — the reconciliation that should exist

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

#### 4. Relationship to DIAN-MUISCA — same authority, different posture

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

#### 5. Where the risk actually sits

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

#### 6. Pipeline cross-references

| Artefact | Relationship |
|---|---|
| `01-ccg/CO-CCG-001` | Statutory rules behind the amounts. **Overtime percentages (P3 §7) must be cross-checked against it** — the annex hard-codes 2021 rates. |
| `02-wtc/` | Wage-type catalogue → source of truth for `S`/`NS` and concept mapping (§2b, §2c) |
| `04-reports-spec/` | `CO-DIAN-NE-MONTHLY-001` is the filing this integration carries |
| `05-data-dictionary/` | Field-level definitions feeding the 262-carrier document (P3 §1) |
| `06-payslip/` | Same concept set, different presentation; the payslip and DIAN-NE should not disagree on a concept's classification |
| `integration-landscape.json` | Discovery output; verdict `HAS_INTEGRATIONS` |
| `CO-SIR-INDEX-001-v1.0.docx` | Index across all four authorities |


---

## C.9 Build effort estimates

<!-- source: 03-statutory-integrations\DIAN-NE\effort-estimates.md -->

### Effort Estimates — DIAN-NE

Engineering effort to build, certify and operate the Colombian electronic-payroll integration.
Estimates are in **person-days** for one experienced integration engineer familiar with SOAP and
XML signing but new to DIAN. They assume the CO payroll engine already produces correct payroll
results — DIAN-NE consumes payroll, it does not compute it.

**Basis:** all artefacts are in hand (P1 §7), so there is **no discovery or artefact-chasing
effort** in these numbers. That is a material saving over a typical statutory integration and is
already reflected below.

---

#### Summary

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

#### Drivers by phase

##### P2 — Connectivity & security · 10 d
The WSDL is standard WCF and a client generates cleanly, so transport is cheap. Cost is
concentrated in **XAdES-EPES signing**: signature policy identifier, `SigningCertificate` digest,
`ClaimedRole`, correct canonicalisation and reference set. Add the thumbprint-reference requirement
(`sp:RequireThumbprintReference`) which several SOAP stacks do not do by default.

Loaded by: no signed reference instance exists to diff against (P3 §10), and the auth model is
ambiguous between the annex and the WSDL (P2 §3). Both are resolved empirically in P6, not here —
which is why P2 can finish "done" and still be wrong.

##### P3 — Payload mapping · 18 d · **largest single item**
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

##### P5 — Validation rules · 13 d
**433 published rules** (406 rejection, 27 notification) plus three global rules. The estimate is
*not* for reimplementing all 433 — DIAN enforces them server-side. It covers:

- A remediation catalogue keyed on rule ID (~2–3 d to transcribe and classify the tables).
- Local pre-flight validation for the container/signature/schema layers, which is genuinely
  worthwhile because every rejection consumes a document number (rule 90).
- The **rule-90 non-idempotency design**: transactional consecutive allocation,
  `GetStatus`-before-resubmit, concurrency safety. This is small in code and large in consequence.
- Correction flow: rejected-vs-validated branching, Reemplazar/Eliminar notes (P5 §6).

##### P6 — Habilitación · 14 d · **highest variance**
Split roughly: 3 d administrative (RUT, art. 22 mandate, software registration, certificate
procurement lead time is *elapsed*, not effort), 3 d test-harness build, **8 d convergence**.

The convergence figure is the honest one. Two of three cryptographic controls have no offline
oracle (P6 §4), so this phase is a loop, not a gate. If CUNE and signature both land first time,
this is 6 d; if both need several cycles, 25 d.

##### P4, P7 · 6 d each
Response parsing is a small, well-specified type. Persistence and retention are straightforward
once the byte-exactness requirement is understood. Operations is scheduling, monitoring and
alerting on a monthly cycle.

#### Risk loading

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

#### Per-tenant onboarding (recurring, after the build)

| Activity | Effort |
|---|---|
| RUT / art. 22 mandate / software registration | 1–2 d (mostly elapsed, client-dependent) |
| Certificate procurement from an ONAC-accredited CA | 0.5 d effort, **1–3 weeks elapsed** |
| Habilitación test set for the tenant | 1–3 d |
| Client-specific coverage matrix (P6 §6) | 1–2 d |
| **Per tenant** | **4–8 d**, with certificate lead time on the critical path |

Start certificate procurement at engagement kick-off. It is the longest pole and it is pure
waiting.

#### Steady-state run cost

| Activity | Frequency | Effort |
|---|---|---|
| Monthly run monitoring + exception handling | monthly | 0.5–2 d per tenant, scaling with headcount and data quality |
| Adjustment notes | as needed | included above |
| Certificate renewal | ~annual | 0.5 d + procurement lead time |
| Annex/WSDL version watch (P7 §6) | quarterly | 0.25 d, all tenants |
| Overtime-rate cross-check vs CCG | annual | 0.25 d |

#### What is *not* in these numbers

- Payroll computation itself (CCG/WTC scope).
- The other three CO authorities — all manual, no runbooks. Note in particular that
  **FONDOS-CESANTIAS carries the largest operational risk in the CO year** despite requiring zero
  integration effort (INTERLINKAGES §5); it needs a tracked manual control, not engineering days.
- The DIAN-NE ↔ PILA reconciliation recommended in INTERLINKAGES §3 — **+3 to 5 d** if adopted.
  Recommended: it is the highest-value optional item in the CO programme.
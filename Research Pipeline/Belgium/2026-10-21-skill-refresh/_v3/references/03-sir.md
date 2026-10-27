# Belgium — Statutory Integration Requirements (SIR) — BE-SIR-001 v1.0

Belgium Statutory Integration Register — BE-SIR-001 v1.0

Statutory Integration Register

Income year 2026 — assessment year 2027

Currency: EUR  |  Country code: BE

Mercans Compliance Regulations Team

Version 1.0 — 14 August 2026, revised 17 August 2026

Source of business content: BE-CCG-001 v1.0, read in full. Technical content is sourced to the authorities' own published documentation and dated in Section 7.

Built as Stage 6 ahead of Stage 3. Stage 3 has since completed: BE-compliance/04-reports-spec/ holds nine Report Specifications at version 1.2, and Section 2.3 carries the resolved Related Report Spec mapping for all nineteen outbound integrations.

<!-- nav-index -->
## Navigation — line numbers in this file

*Read this file with `offset`/`limit` rather than whole; it is large.*

- L79: Table of Contents
- L83: Document Control and How to Read This Register
  - L85: Purpose
  - L89: Build order — read this first
  - L95: Source discipline
  - L107: Completeness verification against the rest of the CCG
  - L128: Product Mapping Required — what the flag means
  - L138: Currency of the sources
- L142: 1. Inbound Integrations
  - L154: 1.1 Inbound register — identification and mapping
  - L178: 1.2 Inbound register — report spec, frequency and format
- L202: 2. Outbound Integrations
  - L210: 2.1 Outbound register — identification and mapping
  - L234: 2.2 Outbound register — frequency and format
  - L258: 2.3 Related Report Spec — all outbound integrations
  - L288: 2.4 Registered, but not an integration of the payroll engine
- L301: 3. Authentication Requirements
  - L307: 3.1 The four NSSO channel families
  - L345: 3.2 FPS Finance channels
  - L352: 3.3 Other channels
  - L364: 3.4 Per-integration authentication lookup
- L382: 4. Technical Specifications
  - L384: 4.1 The NSSO batch channel — the spine of Belgian payroll integration
  - L452: 4.2 DmfA — OUT-02, OUT-03
  - L464: 4.3 Dimona — OUT-01, IN-01
  - L475: 4.4 Finprof — wage withholding tax return, OUT-04
  - L495: 4.5 Belcotax-on-web — 281.10 and 325.10, OUT-05
  - L511: 4.6 SEPA payment files — OUT-09, OUT-10, OUT-11
  - L526: 4.7 Presence registration — OUT-18
  - L535: 4.8 Flows with no published technical specification
- L547: 5. Error Handling
  - L549: 5.1 The NSSO anomaly model
  - L645: 5.2 Belcotax-on-web
  - L690: 5.3 Finprof
  - L707: 5.4 Dimona REST
  - L719: 5.5 SEPA
  - L723: 5.6 Summary  where an error model exists and where it does not
- L734: 6. SLA and Deadlines
  - L738: 6.1 Filing and payment deadlines
  - L776: 6.2 Published response-time SLAs
  - L791: 6.3 Correction windows
  - L800: 6.4 Time-boxed items to diarise
- L815: 7. Source Register
  - L819: 7.1 Internal artefacts
  - L828: 7.2 National Social Security Office (NSSO / RSZ / ONSS)
  - L853: 7.3 FPS Finance
  - L865: 7.4 Other counterparties
- L878: 8. Open Gaps
  - L882: 8.1 Gaps at an authority — closeable by direct inquiry
  - L908: 8.2 Gaps at a commercial counterparty — closeable per client, not per country
  - L920: 8.3 Pipeline gap — the reason this register was built out of order
  - L926: 8.4 What this register does not claim

---

## Table of Contents

Right-click and select 'Update Field' to build the table of contents.

## Document Control and How to Read This Register

### Purpose

This is the Statutory Integration Register (SIR) for Belgium. It registers every data flow between the payroll engine and an external system — a Belgian authority, a paying institution, the client's bank, or a commercial third party — that Belgian payroll depends on. For each flow it records the identifying fields, the authentication mechanism, the technical specification, the error-handling model and the deadlines and response times.

### Build order — read this first

This register was originally built as Stage 6 of the pipeline, ahead of Stage 3 (Report Specifications), which was a deliberate, confirmed sequencing decision. At that time BE-compliance/04-reports-spec/ was empty, and every outbound integration carried a placeholder in its Related Report Spec field rather than a guessed filename.

Stage 3 has since completed and this register has been updated accordingly. BE-compliance/04-reports-spec/ now holds nine Report Specifications, all at version 1.2 with effective date 16 August 2026. Section 2.3 carries the resolved mapping: eleven of the nineteen outbound flows are governed by one of those nine specifications — BE-FEBELFIN-001 governs three of them, OUT-09, OUT-10 and OUT-11, because they are one message with three variants — and the remaining eight record why no Report Specification exists or is required. No report-spec filename has been guessed or invented at any point; each was taken from the specification's own SIR cross-reference statement. Section 2.3 remains the single place to update.

### Source discipline

Three classes of statement appear in this register and they are not interchangeable.

| Class | Where it comes from | How it is marked |
| --- | --- | --- |
| Business and legal content — what integrates, why it is mandatory, filing deadlines | BE-CCG-001 v1.0, read in full from the current document, principally Modules 1.2, 10.1, 10.2, 10.3, 10.4 and 10.5 | Cited as "CCG Module x.y" |
| Technical content — authentication, protocol, file format, error codes, response times | Primary technical documentation published by the authority itself, or its own technical annexes | Cited to the named document with its version and date in Section 7 |
| Absent content | A genuine search returned no published source | Written as NOT FOUND - requires direct inquiry to the authority, never filled with a plausible-sounding value |

An honestly-labelled gap is a correct answer in this register. An invented technical detail is not. Section 8 lists every gap in one place so that it can be closed by direct inquiry rather than rediscovered.

### Completeness verification against the rest of the CCG

The inventory of flows was taken from CCG Module 10.2, which supplies eleven mandatory inbound flows and nine mandatory outbound flows. That list was then verified — not re-derived — against Module 1.2 (filing and payment deadlines), Module 10.1 (the full statutory reporting table), Module 10.3 (payslip) and Module 10.4 (other compliance). The verification found the following, all of which are additions to the Module 10.2 inventory rather than corrections to it.

| Found in | Flow | Why it is not in Module 10.2 | Action |
| --- | --- | --- | --- |
| Modules 1.2 and 10.1 | Dimona, DmfA, the wage withholding tax return and the Belcotax-on-web annual filing | Module 10.2 asks for integrations beyond standard reporting, so the four core declarations are deliberately outside its scope | Registered as OUT-01 to OUT-05. A register of integrations that omitted the declarations themselves would be unusable |
| Module 10.1 | Limosa declaration (NSSO, per posting, before the posted worker starts) | Not carried in either Module 10.2 table | Registered as OUT-08 and then descoped: the declaration is filed by the foreign posting employer, not by the Belgian payroll client (Programmawet/Loi-programme (I) du 27 décembre 2006, arts. 139 and 155). The ID is retained for contiguity; the only Belgian-side duty, the art. 141 verify-and-report-if-missing check, is HR scope. See Section 2.1 OUT-08 and Section 2.4 |
| Module 10.1 | Social balance sheet (National Bank of Belgium, with the annual accounts) | Module 10.1 records it as partly out of payroll scope | Registered as OUT-17, product mapping limited to the payroll-derived sections |
| Module 10.1 | DB2P declarations to Sigedis | Module 10.1 states these are "filed by the pension institution, not by payroll" | Registered as OUT-19 with product mapping false, so that the upstream ownership is recorded rather than silently absent |
| Module 10.1 | Individual account; work rules deposit with FPS Employment | Neither is a machine-to-machine flow | Recorded in Section 2.4 as registered-but-not-an-integration |
| Module 10.3 and the Law of 3 June 2007 | Electronic payslip and electronic social-document delivery | Module 10.2 treats the payslip as an output, not an integration | Registered as OUT-16 |
| Module 10.4 | Checkinandcheckout in construction; the registered cash register in hotels and catering | Module 10.4 correctly notes these are attendance and turnover systems, not payroll certification | Presence registration is registered as OUT-18 because it is a mandatory electronic flow in scope sectors. The registered cash register is recorded in Section 2.4 as out of payroll scope |
| Module 10.2 inbound, expanded | The NSSO batch response set contains more than one message: the reception acknowledgement, the content notification, the technical identification keys file and the corrective contribution notice | Module 10.2 groups these as "DmfA validation report" | Split into IN-02 and IN-03, because they arrive at different times and drive different downstream actions |
| This register's own Section 2 rule, applied to itself | The return legs of OUT-06, OUT-07, OUT-08, OUT-09, OUT-14 and OUT-18 | Module 10.2 registers the outbound obligation and treats the response as part of it. This register's Section 2 preamble requires the inbound leg to be registered separately so it can be scheduled and monitored on its own, and that rule had not been applied to these six | Registered as IN-15, IN-16, IN-17, IN-14, IN-18 and IN-19 respectively. OUT-09's leg is the most consequential: it is the message that reports a failed net-pay transfer. IN-17 is the exception and is now descoped: OUT-08's receipt is returned to the foreign declarant, not to the Belgian client, so it was never a return leg of anything this engine sends — see IN-17 and Section 2.4 |
| scope_manifest.json inbound inventory | The attachment or wage-assignment order served on the employer (BE-IN-GARNISHMENT-ORDER) | Not an integration in Module 10.2's sense, and this register had folded it into the OUT-12 direction cell — which describes a second outbound obligation, not an inbound flow | Registered as IN-13 in its own right, and OUT-12's direction corrected from both to outbound |

Nothing in Module 10.2 was dropped. Every one of its twenty flows appears in this register.

Direction discipline. Every outbound flow marked both now names its inbound leg by ID, and every named leg is a defined row in Section 1. Where a flow was marked both because it carries a second outbound duty rather than a response — OUT-12, the declaration of garnishee — the direction is recorded as outbound and the duty is scheduled as such in Section 6.1.

### Product Mapping Required — what the flag means

The column answers one question: does the Mercans product need a configured mapping layer — wage type to field, code list to code list, or entity to entity — for this flow to work? It is not a scope flag and it is not an importance flag.

- true means a mapping must be built and maintained, and a change in the authority's code list is a product change.

- false means the flow is either a status or a monetary instruction that carries no payroll-element semantics, or it is owned upstream and the engine only consumes or emits an already-agreed structure.

Every row states its rationale inline. Section 2.4 records the flows that are registered but explicitly owned outside payroll, in line with control B7 of CCG Module 10.2: scope decisions are first-class and reversible, and each carries the inbound data contract it implies.

### Currency of the sources

The technical sources behind Sections 3 to 6 were read on 14 August 2026. Where an authority publishes a version number, it is given. Two of them are materially older than the business content of the CCG and this is flagged where it matters: the general NSSO anomaly code list was read at version 2024/1, and the FPS Finance FinProf XML file description is dated 26 September 2011 and remains the currently published specification. The DmfA glossary itself is at 2026/2.

## 1. Inbound Integrations

Nineteen inbound flows are registered. Eleven are the mandatory inbound flows of CCG Module 10.2; IN-03 is the split of the NSSO batch response set explained in the document control section.

The remaining seven, IN-13 to IN-19, are registered so that the rule stated in the Section 2 preamble is actually honoured. That rule is that where an outbound channel returns an acknowledgement or a validation report, the direction is recorded as both and the inbound leg is registered separately in this section so that it can be scheduled and monitored on its own. Six outbound flows were marked both while naming no inbound leg, and their return legs are now registered as IN-14 to IN-19. IN-13 is different in kind: it is not a return leg at all but an originating inbound flow — the attachment order served on the employer, which the scope manifest locks in scope as BE-IN-GARNISHMENT-ORDER and which is the trigger for OUT-12 rather than a response to it.

An inbound leg that is described in the technical sections but never registered here cannot be scheduled, cannot carry a product-mapping decision and cannot be monitored. That is the specific failure this section now closes.

CCG Module 10.2 states the governing principle for this section: "Belgian payroll cannot run correctly on outbound declarations alone; several inbound flows are mandatory in the sense that the process fails or becomes non-compliant without them." Every one of these is in scope for the pipeline unless the scope manifest records an explicit descoping decision with its rationale.

One does: IN-17. The Limosa-1 receipt is not an inbound flow of this product — the Limosa portal returns it to the foreign declarant, not to the Belgian payroll client — so it is registered here with the determination on its face rather than removed, which would break the contiguity this section exists to guarantee. scope_manifest.json descopes it as BE-NSSO-LIMOSA-L1-VERIFY and no longer carries a matching entry in its own inbound inventory. See IN-17, OUT-08 and Section 2.4.

### 1.1 Inbound register — identification and mapping

| ID | Authority / System | Direction | Product Mapping Required | Description |
| --- | --- | --- | --- | --- |
| IN-01 | National Social Security Office (NSSO / RSZ / ONSS) | Inbound (response leg of OUT-01) | true — the returned Dimona number and accepted period are keys, not status. They must be stored against the employment and replayed into the DmfA occupation line, and the DmfA is validated against them | Dimona acknowledgement carrying the Dimona reference number and the accepted period. CCG Module 10.2: a rejected Dimona blocks the quarterly declaration |
| IN-02 | NSSO | Inbound (response leg of OUT-02 and OUT-03) | true — each anomaly is reported as a zone identifier plus an anomaly code, so the engine must map NSSO zone numbers back to its own fields to route a correction to the right wage type or master-data field | DmfA reception acknowledgement (ACRF) followed by the notification carrying the acceptance or rejection result and the anomaly report. CCG Module 10.2: anomalies must be corrected before the deadline |
| IN-03 | NSSO | Inbound | true — the corrective notice restates contribution amounts the NSSO itself calculated. These must be reconciled against the engine's own figures, which is a field-level mapping, not a status read | The remainder of the NSSO batch response set: the PID file of technical identification keys returned on an initial DmfA, and the DMNO modification notification / corrective contribution notice sent when the NSSO's control system alters an accepted declaration |
| IN-04 | NSSO, Directorate of Collection | Inbound | false — the amounts are a treasury instruction. They are not per-employee and carry no wage-type semantics; they drive OUT-10 and the general ledger, both of which already have their own mapping | NSSO contribution statement, monthly provision (advance) notice and debit notice. CCG Module 10.2: the advances are calculated by the NSSO, not by the employer. CCG Module 1.2 fixes the trigger at contributions above EUR 6,197.34 in quarter K-2 |
| IN-05 | NSSO — Student@work | Inbound | true — the consumed-hours figure selects the contribution set. Below the quota the student solidarity contributions of 2.71% employee and 5.42% employer apply; from the 651st hour ordinary contributions apply. That is a wage-type and worker-code switch, so it is a mapping | Student quota counter: hours already consumed of the 650-hour annual quota. CCG Modules 5.1, 5.2 and 7.1 |
| IN-06 | FPS Finance — Belcotax-on-web | Inbound (response leg of OUT-05) | false — the return is a sending status and an error list against the submitted file, not payroll data. The error list is consumed by the correction process, which reuses the OUT-05 mapping | Belcotax reception acknowledgement (ontvangstmelding) and processing message (verwerkingsbericht) accepting or rejecting the 281.10 filing. CCG Module 10.2: determines whether the annual obligation is discharged |
| IN-07 | FPS Finance — Finprof | Inbound (response leg of OUT-04) | false — evidence of filing and a declaration status. No payroll element is returned | Finprof acknowledgement of the wage withholding tax return. CCG Module 10.2: evidence of filing |
| IN-08 | Previous employer | Inbound | true — the certificate amounts must be deducted when the new employer pays holiday pay or grants leave, which is a wage-type-level offset against the departure holiday pay already settled | Holiday certificate (vakantieattest) stating holiday pay already settled and days already taken. CCG Modules 2.2, 8.1 and 9.1: without it the new employer over-pays holiday |
| IN-09 | National Annual Holidays Office (RJV / ONVA) and the sectoral holiday funds | Inbound | true — the amount paid by the fund must appear on the blue-collar payslip and drive the leave administration, so it maps to presentation wage types and to the leave counter | Holiday fund data for blue-collar workers: the holiday pay paid to the worker, 15.38% of the gross of the service year at 108% (CCG Module 8.1) |
| IN-10 | The leasing company or fleet provider | Inbound | true — the same record drives two different calculations with different rules: the taxable benefit in kind (catalogue value, CO2, age coefficient) and the employer CO2 solidarity contribution (CO2, fuel type, order date, days of availability). Mapping is unavoidable | Fleet data: catalogue value, CO2 value, fuel type, first registration date, order date, availability dates, personal contribution. CCG Modules 2.2, 7.2 and 10.1 |
| IN-11 | The meal and eco voucher issuer | Inbound | true — the confirmed count per employee reconciles the employee part withheld from net (at least EUR 1.09 per voucher) and the employer part. A mismatch requalifies the voucher as wage in full (CCG Module 4.2) | Confirmation of vouchers actually issued per employee. CCG Module 10.2: reconciles the deduction from net |
| IN-12 | The client's time and attendance system | Inbound | true — days and hours must land on the correct DmfA service code, which drives both benefit entitlement and holiday accrual, and separately on proration, overtime and the meal voucher count. This is the heaviest mapping in the register | Time and attendance: days and hours, overtime, absences. CCG Modules 4.3, 8.1 and 10.1 |
| IN-13 | Court, bailiff (gerechtsdeurwaarder / huissier de justice), or the administration for tax and social security debts | Inbound (the trigger for OUT-12, not its response leg) | true — the order states the instrument type, and that selects between the treatments CCG Module 7.3 distinguishes: attachment (beslag), wage assignment (loonoverdracht), and administrative attachment for tax and social security debts, which do not share protected-band and priority rules. The creditor, the debt and the principal amount must be mapped onto the garnishment wage type in BE-WTC-001 for the deduction to be computed and shown on the payslip | Attachment or wage-assignment order served on the employer. Carries the creditor, the debt, the instrument type and the date of service, which starts the fifteen-day declaration-of-garnishee clock scheduled in Section 6.1. Locked in scope by scope_manifest.json as BE-IN-GARNISHMENT-ORDER. Without it the Article 1409 computation has no inputs and the OUT-12 clock has no start date |
| IN-14 | The client's bank | Inbound (response leg of OUT-09, and of the OUT-10 and OUT-11 payments, which travel in the same message) | true — a reject is not a status to display but a payroll event: the net pay of a named employee did not arrive. The report must be matched back on the EndToEndId to the employee and the pay run, which is precisely why that field must carry a payroll-meaningful key, and a rejected salary transfer must be re-issued | SEPA Payment Status Report. ISO 20022, per the Febelfin XML Message for Payment Status Report, 2025 version 1.0. Reports acceptance or rejection of the credit transfer file and of individual transactions. This is the leg that tells payroll a salary payment failed; without it a rejected net-pay transfer is invisible to the engine |
| IN-15 | NSSO and the paying institutions — National Employment Office, health insurance funds, holiday funds | Inbound (response leg of OUT-06) | true — the anomaly report identifies the failure by zone identifier plus anomaly code, so the engine must map NSSO zone numbers back onto its own fields to route a correction. Identical in mechanism to IN-02 | DRS / ASR reception acknowledgement (ACRF) and the notification carrying acceptance, rejection and the anomaly report, for the unemployment, indemnity and related scenarios. Section 5.6 groups OUT-06 with the DmfA as sharing the 498-code NSSO error model; this row is the leg that model is consumed through |
| IN-16 | The employer's work accident insurer, and Fedris | Inbound (response leg of OUT-07) | true — same zone-plus-anomaly-code mapping as IN-15, the AOAT scenario of the same DRS family. The insurer's acceptance also returns the claim reference against which any later medical or wage-basis correction is filed | Work accident declaration acknowledgement and notification, returned through the DRS channel with application code AOAT, or through the insurer's own channel. Section 5.6 groups OUT-07 with the NSSO 498-code error model |
| IN-17 | NSSO — Limosa | NOT AN INBOUND FLOW OF THIS PRODUCT — descoped. Registered to keep IN-01..IN-19 contiguous and to record the determination. It is not the response leg of an outbound flow this engine makes | false — and no interface exists to map. The receipt is not transmitted to the Belgian payroll client at all: the Limosa portal returns it to the foreign declarant, in that declarant's own authenticated session | Limosa-1 receipt (Limosa-1 ontvangstbewijs / accusé de réception), returned to the foreign employer on submission of its own posting declaration. The Belgian side never receives it as data. Under art. 141 of the Programmawet/Loi-programme (I) du 27 décembre 2006 the person for whom the work is carried out must verify that the declaration was made and be able to produce the acknowledgement — in practice by sighting the copy the posted worker presents — and must report to the NSSO only where it cannot be produced. That is a physical or PDF document check at onboarding, owned by HR, not a machine-to-machine flow. Descoped as BE-NSSO-LIMOSA-L1-VERIFY in scope_manifest.json, which for the same reason no longer carries BE-IN-LIMOSA-RECEIPT in its inbound inventory. See OUT-08 and Section 2.4 |
| IN-18 | The insurer or pension fund | Inbound (response leg of OUT-14) | true — the accepted premium per affiliate is the figure the 8.86% special employer contribution and the 4.4% insurance premium tax are actually owed on, so a premium the insurer rejected or adjusted must be reconciled against what payroll charged. All three are separate wage types in BE-WTC-001 | Acknowledgement and accepted-premium confirmation for the supplementary pension premium file. NOT FOUND - requires direct inquiry to the insurer or pension fund: no format, schema or transport is published, exactly as for the outbound leg (Section 4.8, gap G24) |
| IN-19 | NSSO — Checkinatwork / Check In and Out at Work | Inbound (response leg of OUT-18) | false — a presence-registration outcome. CCG Module 10.4 is explicit that Checkinatwork is not payroll certification, so the response drives an attendance reconciliation rather than a pay calculation | Presence-registration response: the per-presence result of the presenceRegistration service. Because registerInBulk accepts up to 200 presences per request, the response is the only way to establish which presences within a batch were accepted |

### 1.2 Inbound register — report spec, frequency and format

| ID | Related Report Spec | Frequency | File format / protocol |
| --- | --- | --- | --- |
| IN-01 | Not applicable — inbound flow | Per event, following each Dimona | REST: HTTP 200 on GET /dimona/v2/declarations/{dimonaNbr}, application/json. Batch: XML response file in the OUT directory over SFTP or FTP |
| IN-02 | Not applicable — inbound flow | Quarterly, following each DmfA submission | XML. FO.ACRF reception acknowledgement then the notification file, both retrieved from the OUT / OUTTEST / OUTTEST-S directory over SFTP or FTP. The notification carries an <AnomalyReport> block |
| IN-03 | Not applicable — inbound flow | Per event, on an initial DmfA (PID) or when the NSSO corrects an accepted declaration (DMNO) | XML. FO.DMPI for the technical identification keys; FO.DMNO for the corrective contribution notice, carrying <WRDclPart> (declared) and <WRCorrectedPart> (corrected) |
| IN-04 | Not applicable — inbound flow | Monthly for the provisions; quarterly for the statement and debit notice | Letter from the NSSO for employers that are not a provincial or local authority and are not affiliated to a recognised social secretariat. For provincial and local authorities, a letter in the e-Box. For social service providers, an online service holding the advance documents, debit notices and amendment notices. No machine-readable structured feed is published for private-sector employers |
| IN-05 | Not applicable — inbound flow | Per engagement, and on renewal within the quota | Secured web application on the social security portal, or entry of the access code from the student's Attestation for the future employer. No batch or web-service channel found |
| IN-06 | Not applicable — inbound flow | Annual, following each Belcotax sending; and per corrective sending | E-mail to the address in record zone 0.023 (e-mail address of the contact person at the sender). An error.txt file is written locally by the validation module. The response is e-mail only; there is no published pull API |
| IN-07 | Not applicable — inbound flow | Monthly, or quarterly for small employers | Consultation in the FinProf application: the Zoeken function retrieves sendings and their status, and declarations with a detail per declaration |
| IN-08 | Not applicable — inbound flow | Per new joiner, and on leaving for the outbound copy | Paper or PDF document issued by the previous employer. No statutory electronic interchange format exists for the white-collar holiday certificate |
| IN-09 | Not applicable — inbound flow | Annual, normally between May and June (CCG Module 8.1) | RJV/ONVA Mijn vakantierekening is a citizen-facing online service; the worker downloads the holiday-duration attestation, account extract and tax certificate. No employer-facing machine interface found; sectoral funds vary |
| IN-10 | Not applicable — inbound flow | Monthly, and per event on allocation, change or return of a vehicle | Commercial file or portal export, per leasing company. No public or sector-standard interchange format found |
| IN-11 | Not applicable — inbound flow | Monthly, following the voucher order | Commercial API, SFTP connector or import file, per issuer. No public technical specification found |
| IN-12 | Not applicable — inbound flow | Per pay period, at the cut-off (CCG Module 1.2: between the 10th and the 20th for monthly white-collar staff) | Client-specific. No statutory format; the contract is set by the implementation |
| IN-13 | Not applicable — inbound flow | Per attachment served, and on each variation or release of the order | Bailiff's writ, registered post, or delivery against receipt. No electronic interchange format exists (Section 4.8, gap G21) — the same finding as for the outbound declaration of garnishee. scope_manifest.json records the format of BE-IN-GARNISHMENT-ORDER as CSV; that is a per-client import convention for capturing the order into the engine, not a statutory interchange format, and it is recorded here as such rather than reproduced as though the authorities published it |
| IN-14 | Not applicable — inbound flow | Per submitted payment file, and per status change until the file is settled. The bank determines the schedule | ISO 20022 Payment Status Report, per the Febelfin XML Message for Payment Status Report 2025 version 1.0, retrieved through the client's banking channel. Reason codes are the ISO 20022 external code set; the bank determines which subset it returns. NOT FOUND at standard level — there is no Belgian-specific reject code list and no standard retry policy; both are set per bank in the channel agreement (gap G25) |
| IN-15 | Not applicable — inbound flow | Per DRS submission | XML. FO.ACRF reception acknowledgement then the notification file, retrieved from the OUT / OUTTEST / OUTTEST-S directory over SFTP or FTP, per scenario application code — WECH, ZIMA, TWCT. The notification carries an <AnomalyReport> block |
| IN-16 | Not applicable — inbound flow | Per work accident declared | XML through the DRS channel, application code AOAT, retrieved from the OUT directory over SFTP or FTP; or the online service on the social security portal; or the insurer's own channel. The insurer's own channel format is insurer-specific and not published |
| IN-17 | Not applicable — inbound flow | No schedule — descoped, and nothing arrives here. The receipt is issued per posting declared, to the foreign declarant | Returned by the Limosa portal to the foreign declarant on submission of its web declaration. Printable or downloadable receipt; no batch or web-service retrieval channel found, and none is required — the Belgian side sights the worker's copy rather than retrieving data |
| IN-18 | Not applicable — inbound flow | Per the plan, normally monthly or annually, following each premium file | Insurer-specific. No public technical specification found (gap G24) |
| IN-19 | Not applicable — inbound flow | Per presence-registration request, in scope sectors | Response of the REST presenceRegistration service on the social security API Gateway, secured with OAuth 2.0 / OpenID. For registerInBulk, one result per presence in a request of up to 200 |

## 2. Outbound Integrations

Nineteen outbound flows are registered: the nine mandatory outbound flows of CCG Module 10.2, the four core statutory declarations that Module 10.2 deliberately leaves out because it asks only about integrations beyond standard reporting, and six further flows found by verifying Module 10.2 against Modules 10.1, 10.3 and 10.4.

Eighteen of the nineteen are flows of the Belgian payroll engine. OUT-08 is not, and its row says so. The Limosa declaration is filed by the foreign posting employer, not by the Belgian payroll client, and the population it covers is not on Belgian payroll at all. The ID is retained rather than withdrawn so that the register stays contiguous at OUT-01..OUT-19 and so that a reader looking for Limosa finds the determination instead of a silent gap. What OUT-08 now registers is the narrow exception-based duty that does fall on the Belgian side — see the row, and Section 2.4.

Where a channel returns an acknowledgement or a validation report, the direction is recorded as both, and the inbound leg is registered separately in Section 1 so that it can be scheduled and monitored on its own.

### 2.1 Outbound register — identification and mapping

| ID | Authority / System | Direction | Product Mapping Required | Description |
| --- | --- | --- | --- | --- |
| OUT-01 | NSSO | Both (IN-01 is the response leg) | true — the declaration carries worker type, joint committee, working-time regime and contract type, each of which is an NSSO code list the engine must map its own master data onto | Dimona, the immediate declaration of employment. Opens and closes the employment relationship in real time and is the key against which the DmfA is validated (CCG Module 10.1) |
| OUT-02 | NSSO | Both (IN-02, IN-03) | true — this is the largest mapping in the register: gross per remuneration code, days and hours per service code, one occupation line per determining characteristic, contribution and deduction blocks per contribution type, and special contribution blocks per vehicle and per scheme (CCG Module 10.1) | DmfA original quarterly declaration. One consolidated grid covering all social security contributions, all reductions and all special contributions, per employee, per occupation line |
| OUT-03 | NSSO | Both (IN-02, IN-03) | true — same mapping as OUT-02, plus the rule that the corrective declaration must restate the original quarter at the rates and reductions of that quarter (CCG Module 9.2) | DmfA modification declaration. The correction route for a wrong wage, days or contribution; the NSSO recalculates and issues a debit or credit (CCG Module 10.5) |
| OUT-04 | FPS Finance — Finprof | Both (IN-07 is the response leg) | true — the return is filed per nature of income code and separately reports the withholding exemptions claimed for overtime, shift and night work and student work, so payroll must map its wage types onto the FPS Finance income-nature codes | Wage withholding tax return (form 274). Filed separately from the DmfA, with a different authority and on a different cycle (CCG Module 10.1) |
| OUT-05 | FPS Finance — Belcotax-on-web | Both (IN-06 is the response leg) | true — every 281.10 box is a distinct mapping target: gross, withholding, benefits in kind by type, exceptional payments by type, departure holiday pay, termination indemnity and the period it covers (CCG Module 10.1) | Annual employee income certificate 281.10. The summary statement 325.10 is derived by FPS Finance from the 281.10 data and is not separately submitted. Explicitly not generated from the twelve monthly withholding tax returns — it is an independent filing built from the payroll ledger and must be reconciled against them (CCG Module 10.1) |
| OUT-06 | NSSO and the paying institutions — National Employment Office, health insurance funds, Fedris, holiday funds | Both (IN-15 is the response leg — an ACRF and a notification are returned) | true — each scenario has its own form and data set, and the DmfA service codes and the employer-funded periods feed them. Without the correct mapping the employee receives no benefit (CCG Module 10.2) | Electronic declarations of social risk (DRS / ASR): unemployment scenarios including scenario 1, which replaces the C4 forms; indemnity scenarios for incapacity, maternity, birth, adoption and parental care; and the work accident scenario |
| OUT-07 | The employer's work accident insurer, and Fedris | Both (IN-16 is the response leg) | true — the declaration draws the wage basis and the working-time regime from payroll, so the reference wage must be mapped to the insurer's declaration fields | Work accident declaration. Due within 8 days of the accident (CCG Module 10.1). Filed as a DRS scenario through the social security portal or directly to the insurer |
| OUT-08 | NSSO — Limosa | Outbound, and exception-only. Not both: the Limosa-1 receipt is returned to the foreign declarant, never to the Belgian client, so there is no inbound leg into this product. IN-17 is reclassified accordingly in Section 1 | false — and no mapping arises at all, because the payroll engine does not produce this flow. Earlier versions of this register read "false — a master-data extract", which conceded the wrong point: it implied the engine builds the declaration from assignment data and merely maps nothing. It does not build it | NOT A PAYROLL DECLARATION — THE ROUTINE FILING IS A THIRD PARTY'S OBLIGATION AND IS OUT OF SCOPE. The Limosa prior notification is filed by the foreign posting employer or posted self-employed person, or their representative, before the posting starts — Programmawet/Loi-programme (I) van/du 27 december/décembre 2006, Title IV, Ch. VIII, art. 139 (posted workers) and art. 155 (posted self-employed), MB/BS 28 December 2006, executed by the Royal Decree of 20 March 2007; confirmed on the NSSO's own Working in Belgium / Limosa portal, on socialsecurity.be and by Securex. The posted population stays on its home-country payroll under an A1 and is not processed through Belgian payroll, so the Belgian payroll client is not the filer and holds none of the source data. What OUT-08 registers instead is the one narrow Belgian-side duty: art. 141 obliges the person for whom the work is carried out to verify that the prior declaration was made and to be able to produce the acknowledgement of receipt, and to report the worker's identification data electronically to the NSSO only where the Limosa-1 cannot be produced. That is an exception-triggered compliance report, not a payroll-cycle declaration: it fires on a missing document, not on a pay run, and carries no pay element. Descoped in scope_manifest.json as BE-NSSO-LIMOSA-009 (the filing — third-party obligation) and BE-NSSO-LIMOSA-L1-VERIFY (the verification duty — HR/onboarding scope). Found by verification against Module 10.1; not present in either Module 10.2 table |
| OUT-09 | The client's bank | Both (IN-14 is the response leg — a payment status report is returned) | true — the file is built from the net pay line and the employee IBAN, and the salary category purpose must be set correctly, so a mapping from the payroll result to the message structure is required | SEPA credit transfer file for net pay. CCG Module 10.2: mandatory in practice, wages must be paid by transfer. CCG Module 1.2: where the fixed pay date is not a banking day the payment is executed on the preceding banking day, never deferred |
| OUT-10 | NSSO, through the client's bank | Outbound | false — a single instructed amount with a structured communication. The amount is set by the NSSO advance notice (IN-04) and by the DmfA balance, neither of which is a payroll element mapping | SEPA payment of social security contributions: the monthly advances by the 5th day following each month of the quarter where due, and the balance by the DmfA deadline (CCG Module 1.2) |
| OUT-11 | FPS Finance, through the client's bank | Outbound | false — a single instructed amount. The structured communication is derived arithmetically from the employer reference number and the period code, not from a mapping table | SEPA payment of the wage withholding tax, due on the same date as the return (CCG Module 1.2) |
| OUT-12 | The bailiff, the creditor, or the administration for tax and social security debts | Outbound — and deliberately not both. This flow carries two outbound obligations, the remittance and the declaration of garnishee, which Section 6.1 schedules as such; a second outbound duty is not a return leg. The inbound side of this domain is the order itself, registered separately as IN-13 | true — the attachable amount is computed from the Article 1409 protected bands on the period's net, with the dependent-child supplement, and remitted per creditor. The garnishment amount is itself a wage type in BE-WTC-001 and must be shown on the payslip (CCG Modules 7.3 and 10.3) | Remittance of the attachable portion for garnishments and wage assignments, and the employer's declaration as garnishee. The employer withholds a single global attachable amount and remits it to the bailiff, who distributes it; the employer does not adjudicate between creditors (CCG Module 7.3) |
| OUT-13 | The meal and eco voucher issuer | Both (IN-11 is the confirmation leg) | true — the order is per employee per day actually worked, derived from the attendance record, and it drives the employee part withheld from net | Meal and eco voucher order file. Mandatory where the benefit is granted (CCG Module 10.2) |
| OUT-14 | The insurer or pension fund | Both (IN-18 is the response leg) | true — the premium base drives the 8.86% special employer contribution and the 4.4% insurance premium tax, and the personal contribution withheld from net generates the 30% withholding reduction. All three are separate wage types in BE-WTC-001 | Supplementary pension premium file. Mandatory where a plan exists (CCG Module 10.2) |
| OUT-15 | The client's accounting system | Outbound | true — the posting file is the classic per-client mapping: every wage type to a general ledger account and cost centre. CCG Module 1.1 adds that a client whose financial year is not the calendar year needs its postings mapped to its own accounting periods | General ledger posting file. Contractual, not statutory (CCG Module 10.2) |
| OUT-16 | The employee, through an electronic social-document provider | Outbound | true — the payslip layout must be configurable per joint committee because sectoral CBAs add items, and the language follows the employer's seat of operation. A bilingual payslip is not permitted (CCG Module 10.3) | Electronic payslip and electronic social-document delivery, permitted where the employee's consent and the conditions of the Law of 3 June 2007 are met (CCG Module 10.3). Found by verification against Module 10.3 |
| OUT-17 | National Bank of Belgium, through the client's accountant | Outbound | false for the flow, true for the extract — payroll supplies figures into a filing another party makes. The extract itself needs a mapping, but the engine does not build or file the XBRL document | Payroll data required for the social balance sheet, filed with the annual accounts. Module 10.1 places the training and workforce-structure sections out of payroll scope because they require data held in the HR information system. Found by verification against Module 10.1 |
| OUT-18 | NSSO — Checkinatwork / Check In and Out at Work | Both (IN-19 is the response leg) | false — a presence event carrying a person, a place and a timestamp. It is an attendance system, not a payroll calculation, and CCG Module 10.4 is explicit that it is not payroll certification | Electronic presence registration, mandatory in construction and in the meat sector, and for posted-worker presences under Limosa. Sector-conditional. Found by verification against Module 10.4 |
| OUT-19 | Sigedis — DB2P | Outbound | false — Module 10.1 states it is "filed by the pension institution, not by payroll". Registered so that the upstream ownership and the implied data contract are recorded rather than silently absent | DB2P declarations for supplementary pensions, per event and annual. Owned upstream. The engine's obligation is to supply OUT-14 accurately enough for the pension institution to declare |

### 2.2 Outbound register — frequency and format

| ID | Frequency | File format / protocol |
| --- | --- | --- |
| OUT-01 | Per event. Before the employee starts work; end of employment by the first working day after (CCG Module 1.2) | XML over SFTP or FTP with application code DIMN; or REST v2 POST /dimona/v2/declarations, application/json; or the secured online service, the Dimona Mobile app, or the unsecured web form |
| OUT-02 | Quarterly. Last day of the month following the quarter — 30 April, 31 July, 31 October, 31 January (CCG Module 1.2) | XML validated against the NSSO XSD. Batch over SFTP or FTP with application code DMFA; or the DmfA online service, which is limited to declarations concerning up to 49 employees |
| OUT-03 | Per correction event, allocated to the original quarter | XML over SFTP or FTP with application code DMWA; or the Modify a declaration function of the online service |
| OUT-04 | Monthly, or quarterly for small employers. The 15th of the month following the period (CCG Module 1.2) | XML file per schema Finprof.xsd, encoding ISO-8859-1; or online entry in the FinProf application |
| OUT-05 | Annual. 28 February of the year following the income year (CCG Module 1.2) | XML validated against belcotax-2025.xsd, converted by the validation module into the encoded .bow format before sending; or online entry through Verzending per codering |
| OUT-06 | Per event, on the triggering event (CCG Module 10.1); monthly for the recurring scenarios | XML over SFTP or FTP with the scenario's application code — WECH unemployment, ZIMA indemnities, AOAT work accidents, TWCT temporary unemployment; or the online service; paper remains available |
| OUT-07 | Per event, within 8 days of the accident (CCG Module 10.1) | DRS work accident scenario, application code AOAT in batch; or the online service on the social security portal; or the insurer's own channel |
| OUT-08 | Not a payroll cycle at all. The routine declaration is per posting, before the posted worker starts (CCG Module 10.1) — but it is filed by the foreign employer, not by this engine. The Belgian-side duty registered here fires per posted worker who cannot produce a Limosa-1, which is an exception, not a schedule | The foreign employer's declaration is a web declaration on the Limosa portal, returning the Limosa-1 receipt to that declarant. The Belgian-side exception report is an electronic notification of the worker's identification data to the NSSO through socialsecurity.be (art. 141). No file format is published for either, and no machine interface is needed for the exception report at the volumes it implies |
| OUT-09 | Per pay run (CCG Module 1.2: monthly for white-collar staff; at least twice monthly for hourly-paid staff) | ISO 20022 pain.001.001.09, per the Febelfin Belgian implementation guidelines. Transmitted through the client's banking channel |
| OUT-10 | Monthly for the advances, by the 5th day following each month of the quarter; quarterly for the balance | pain.001.001.09 or the bank's own channel, with the NSSO structured communication |
| OUT-11 | Monthly, or quarterly for small employers; by the 15th | pain.001.001.09 or the bank's own channel, with the 12-digit structured communication defined by the FinProf specification |
| OUT-12 | Per pay period while an attachment is in force. The declaration of garnishee is due within 15 days of service (CCG Module 7.3) | The payment is an ordinary credit transfer. The declaration of garnishee is sent to the creditor or bailiff by registered post or against receipt. No electronic statutory format found |
| OUT-13 | Monthly, in the month following the worked days (CCG Module 4.2) | Commercial API, SFTP connector or import file, per issuer. No public technical specification found |
| OUT-14 | Per the plan, normally monthly or annually | Insurer-specific file. No public technical specification found |
| OUT-15 | Per pay run and per accounting period | Client-specific. No statutory format |
| OUT-16 | Per pay period, with each definitive payment (CCG Module 10.3) | PDF or an electronic archive at a qualified provider, under the Law of 3 June 2007. No statutory file format is prescribed |
| OUT-17 | Annual, with the annual accounts | XBRL — or PDF — filed by the accountant through the National Bank of Belgium Filing application. Payroll supplies the underlying figures, not the XBRL document |
| OUT-18 | Per presence event, in scope sectors | REST web service presenceRegistration; the registerInBulk method accepts up to 200 presences per request. Also available as a web application and a mobile app |
| OUT-19 | Per event and annual | XML per the DB2P XSD over an SFTP channel on the social security extranet. Filed by the pension institution |

### 2.3 Related Report Spec — all outbound integrations

Stage 3 has since completed. BE-compliance/04-reports-spec/ holds nine Report Specifications, all at version 1.2 with effective date 16 August 2026. Each filename below was taken from the Report Specifications as built, matched on the specification's own SIR cross-reference statement in its Version Control sheet rather than inferred from the integration ID.

Ten of the nineteen outbound flows are governed by a live Report Specification. Eight are not, and that is itself the answer the field must carry rather than an omission. The nineteenth is OUT-08: a Report Specification file exists for it on disk but is descoped, and the row below says so rather than listing it as though it governed a live flow — the arithmetic is 10 live + 1 descoped + 8 none. Note that BE-FEBELFIN-001 governs three flows — it declares in terms that OUT-09, OUT-10 and OUT-11 are "not three file layouts" but one pain.001.001.09 message differing only in creditor, category purpose and structured communication.

| ID | Related Report Spec |
| --- | --- |
| OUT-01 | BE-NSSO-001-Dimona-Spec.xlsx v1.2 |
| OUT-02 | BE-NSSO-002-DmfA-Spec.xlsx v1.2 |
| OUT-03 | BE-NSSO-003-DmfAModification-Spec.xlsx v1.2 |
| OUT-04 | BE-FIN-001-Finprof274-Spec.xlsx v1.2 |
| OUT-05 | BE-FIN-002-Belcotax28110-Spec.xlsx v1.2 |
| OUT-06 | BE-NSSO-004-DRS-Spec.xlsx v1.2. The work accident scenario of the same DRS family is specified separately as OUT-07 |
| OUT-07 | BE-FEDRIS-001-WorkAccident-Spec.xlsx v1.2. A DRS scenario technically identical in envelope to OUT-06, specified separately because this register registers it as its own integration |
| OUT-08 | `BE-NSSO-005-Limosa-Spec.xlsx` exists on disk but is DESCOPED — do not implement from it. It was built at v1.0–v1.2 as a full nine-sheet in-scope specification, before the scope determination recorded in the OUT-08 row above. Its own Report Matrix and Payroll Scope Summary sheets now carry that determination at v1.3, and scope_manifest.json records the file as a descoped artefact. It is retained, not deleted, because it documents a real obligation and its own field-level gaps honestly, and because deleting it would destroy the record of why Limosa is out of scope. It is not a build target |
| OUT-09 | BE-FEBELFIN-001-SEPACreditTransfer-Spec.xlsx v1.2 — the net pay variant (SALA, unstructured remittance information) |
| OUT-10 | BE-FEBELFIN-001-SEPACreditTransfer-Spec.xlsx v1.2 — the NSSO contribution variant (structured communication mandatory) |
| OUT-11 | BE-FEBELFIN-001-SEPACreditTransfer-Spec.xlsx v1.2 — the FPS Finance withholding tax variant (TAXS, the 12-digit FinProf structured communication) |
| OUT-12 | No Report Spec — none can be built. The remittance travels as an ordinary credit transfer within BE-FEBELFIN-001; the declaration of garnishee itself has no electronic statutory format (Section 2.2, gap G21) |
| OUT-13 | No Report Spec — not a statutory report specification. A commercial voucher-issuer interface with no public technical specification |
| OUT-14 | No Report Spec — not a statutory report specification. An insurer-specific premium file with no public technical specification |
| OUT-15 | No Report Spec — not a statutory report specification. A contractual general ledger posting file; no statutory format exists |
| OUT-16 | No Report Spec — not a statutory report specification. No statutory file format is prescribed for the payslip. Its content is specified in the Belgium payslip artefact, not in a Report Spec |
| OUT-17 | No Report Spec — the filing is not built by the engine. The XBRL document is filed by the client's accountant with the National Bank of Belgium; payroll supplies the underlying figures only |
| OUT-18 | No Report Spec — not a statutory report specification. A presence-registration REST service, an attendance system rather than a payroll declaration (CCG Module 10.4) |
| OUT-19 | No Report Spec — owned upstream. Filed by the pension institution, not by payroll |

This table remains the single place to update. Do not infer a filename from the integration ID; take it from the Report Specifications as built. Where a flow has no Report Spec, the reason is recorded above rather than left blank.

### 2.4 Registered, but not an integration of the payroll engine

Control B7 of CCG Module 10.2 requires that a scope decision record three things: what is in scope, what is explicitly owned upstream, and the inbound data contract this implies. The following are recorded here so that a later reversal is a contained change rather than a search across four artefacts.

| Item | Source | Why it is not registered as an integration | Inbound data contract if it were reversed into scope |
| --- | --- | --- | --- |
| Limosa prior notification — the declaration itself (registered as OUT-08 above so the ID stays contiguous, and recorded here because it belongs in this table rather than in the live register) | CCG Modules 10.1 and 11.2; Programmawet/Loi-programme (I) du 27 décembre 2006, Title IV Ch. VIII, arts. 137–141 and 155, executed by the Royal Decree of 20 March 2007; NSSO Working in Belgium / Limosa portal; socialsecurity.be; Securex | The filer is a third party. Art. 139 places the declaration on the foreign posting employer or its representative, and art. 155 on the posted self-employed person. The Belgian host company is never the filer. The population is not on Belgian payroll — it remains under its home social security scheme on an A1 — so the engine holds neither the obligation nor the data. The Belgian-side duty under art. 141 is to verify the Limosa-1 and to report to the NSSO only if it cannot be produced: a document check at onboarding, owned by HR, exception-triggered, with no payroll input and no payroll output | If ever reversed: the foreign employer's own posting and identity master data, which this engine does not hold today and would have to receive from the posting entity — plus a per-posted-worker flag recording whether the Limosa-1 was sighted, which is the only element of it a payroll product would plausibly store. Reversing it would mean taking on a client type this build does not serve, not adding a report |
| Individual account (individuele rekening) | CCG Module 10.1 | Kept by the employer and produced to inspection on request. There is no authority channel and no counterparty system. Closed within two months of the end of the year | None — the engine already holds every element; only a rendering and archiving obligation would arise |
| Work rules (arbeidsreglement) deposit with FPS Employment | CCG Module 10.1 | An HR document, deposited on adoption or amendment. It contains the fixed pay date (CCG Module 1.2) but no payroll data | The fixed pay date and the proration method, which the engine already needs from the work rules as configuration input |
| Registered cash register (geregistreerd kassasysteem) in hotels and catering | CCG Module 10.4 | A turnover system, not payroll. It matters only because it raises the overtime relief ceiling (CCG Module 4.4) | A flag per employer stating whether a registered cash register is in use, which selects the applicable overtime relief ceiling |
| Social balance sheet — training and workforce-structure sections | CCG Module 10.1 | Excluded because more than half of the data does not exist in payroll: headcount by qualification, training hours by type, workforce composition | None into payroll. Payroll's contribution is registered as OUT-17 |
| Analytical reporting to the joint committee, occupational health reporting, diversity reporting | CCG Module 10.1 | HR and prevention-service obligations; the data is not held in payroll | None |

## 3. Authentication Requirements

This section and the three that follow are the genuinely-new research: the CCG does not cover them. Every statement is cited to the authority's own technical documentation, listed with version and date in Section 7. Where a search returned nothing, the cell says so.

The single most important finding for Belgium is that the authentication method depends on the channel, not on the declaration. The same DmfA is authenticated by a citizen identity through CSAM on the web channel and by a technical user with an SSH key pair plus a qualified certificate signature on the batch channel. A payroll provider will use the second and must not plan against the first.

### 3.1 The four NSSO channel families

| Channel family | Identification of the caller | Signature or second factor | Where the channel is configured |
| --- | --- | --- | --- |
| Social security portal, secured web services — DmfA online service, Dimona secured, Student@work, e-Box Enterprise | CSAM login: eID, itsme or eIDAS. eIDAS is the European cross-border scheme allowing access with authorised ID keys from a selection of EU countries | The identity itself is the factor. eID requires the card, a reader and the PIN | Access Management on the portal. The Chief Access Manager grants the role for each online service |
| Batch over SFTP — DmfA, DmfA modification, Dimona, DRS/ASR, temporary unemployment, single works declaration | Technical user name in the form UMxxxxxx or EXPxxxxxx, authenticated by an SSH public/private key pair. RSA only, SSH protocol version 2 only (version 1 is rejected), key length greater than 2048 and less than 4096 bits, OpenSSH or SSH key formats. The private key should itself be protected by a passphrase | A separate qualified digital certificate is required, and is not the SSH key. Every declaration file (FI) must be accompanied by a signature file (FS) produced from that certificate | Chaman, the technical channel management service on the portal. The certificate's public key (.cer) is uploaded when the channel is created |
| Batch over FTP — same applications | Technical user name and password on ftp.socialsecurity.be, port 21 | Same qualified certificate and same FS signature file requirement | Chaman. The qualified certificate's public key is uploaded when the FTP channel is created |
| REST web services — Dimona v2, Check In and Out at Work (presenceRegistration) | OAuth 2.0 Client Credentials. An access token is obtained from the social security OAuth server; the client application authenticates to obtain it. The generated OAuth Client ID takes the form self_service_expeditor_X | An X.509 authentication certificate in the company's name, uploaded in Chaman | Chaman, by the Chief Access Manager or a delegated Technical Manager. The documentation is explicit that despite being technical work, only those two roles can perform it |

#### 3.1.1 The qualified certificate used for the batch signature file (FS)

This is the detail most often got wrong in a Belgian implementation, so it is set out exactly as the NSSO publishes it.

| Question | Answer |
| --- | --- |
| Which certificates are accepted? | Two, and only two are named: the signature certificate of the Belgian electronic identity card (eID), and a qualified digital certificate from GlobalSign — PersonalSign 3 Pro |
| Can an Isabel card be used? | No. The NSSO states plainly that building a signature file from an Isabel card is not possible because the private key cannot be exported, that it cannot supply a manual or technique for doing so, and that the Isabel helpdesk cannot help either |
| What is the signature format? | A detached S/MIME / PKCS#7 signature. The published OpenSSL procedure is smime -sign -in <FI file> -signer <cert>.pem -inkey <key>.key -outform PEM -out <FS file>, after which the -----BEGIN PKCS7----- and -----END PKCS7----- lines must be deleted and no trailing blank line may remain |
| Which certificate can be used with the OpenSSL procedure? | Only one whose private key can be exported — in practice only a GlobalSign certificate. The procedure does not work for a certificate held on an eID or an Isabel smart card |
| How is an eID signature produced instead? | Through the Cryptonit procedure published in the NSSO's supplementary document library. It requires the eID holder to be physically present: the card must be in the reader and the PIN entered for every signature file. If the holder is absent, another eID must be used and its public key loaded into the channel parameters beforehand |
| Is the FS file always required? | Required in the production environment. Not required in the test or simulation environments, but if one is supplied there it will be checked |

The operational consequence for a payroll provider is direct: an eID-based signature cannot be automated, so a production batch channel is built on a GlobalSign PersonalSign 3 Pro certificate.

#### 3.1.2 The X.509 certificate used for the REST channel

The REST channel uses a different certificate with different rules, and it is not required to be qualified.

| Parameter | Published requirement |
| --- | --- |
| Issuer | Either a self-signed certificate generated by the company, or a certificate from a recognised certification authority — GlobalSign, DigiCert, QuoVadis, Verisign, Certipost and others |
| Key algorithm and length | RSA at 2048, 3072 or 4096 bits, or EC at P-384 or P-521 |
| Digest algorithm | SHA-256, SHA-384 or SHA-512 |
| Key usage | Digital Signature |
| Reuse | An existing certificate may be reused across several channels or REST accounts |
| Validity period | NOT FOUND — the Chaman documentation states no minimum or maximum validity |
| Token lifetime | NOT FOUND — the OAuth token lifetime is not published in the Chaman or REST documentation. Requires direct inquiry to the NSSO |

### 3.2 FPS Finance channels

| Channel | Identification of the caller | Notes |
| --- | --- | --- |
| Finprof (OUT-04, IN-07) | Either the Belgian electronic identity card, or authentication by a qualified certificate issued by one of the certification authorities FPS Finance accepts — GlobalSign, Isabel or Certipost. Once authenticated, the declarant identifies itself by the KBO/BCE enterprise number or by a national register number | Note the contrast with the NSSO batch channel: FPS Finance accepts an Isabel certificate for Finprof authentication, whereas the NSSO cannot accept one for the batch signature file. The two must not be assumed interchangeable |
| Belcotax-on-web (OUT-05, IN-06) | The income-year 2025 brochure states that access requires a Belgian electronic identity card. The FPS Finance access page additionally offers itsme®. Acting for a company is a role, not a mandate: the legal representative assigns Belcotax-on-web roles through the Mijn Beheer van eGov-rollen service, and the user then selects in the name of a company. A person without an enterprise number requests access from belcotax@minfin.fed.be, supplying an identity-card copy, and receives a reference number to identify with | The brochure's wording is narrower than the access page's. Both are recorded because the brochure is the technical specification and the access page is the current operational instruction. FPS Finance imposes one binding rule across the two applications: for withholding tax fiches the same identification — national register number or reference number — must be used in Belcotax-on-web as in Finprof |

### 3.3 Other channels

| Integration | Authentication | Source status |
| --- | --- | --- |
| OUT-18 Checkinatwork technical channel — and OUT-08 Limosa only as the foreign declarant's own channel, since OUT-08 is descoped (Section 2.1) | A GlobalSign certificate and a technical user, requested through the secure-access request form for the social security portal. The REST presenceRegistration service is a secured service on the social security API Gateway using OAuth 2.0 / OpenID | The OAuth/OpenID statement is from the NSSO's own service documentation. The GlobalSign-plus-technical-user statement is from the Working in Belgium portal, which is government-operated but is a guidance page rather than a technical specification. Treated as confirmed for planning, to be re-verified at implementation |
| OUT-09, OUT-10, OUT-11 SEPA | NOT FOUND at authority level — and correctly so. There is no Belgian authority that authenticates a payment file. Authentication is set by the client's bank and its channel (a banking portal, Isabel 6, EBICS, or a host-to-host link), and differs per bank. Febelfin publishes the message standard, not an access or authentication standard | Confirmed absence, not a gap. The implementation contract is with the bank, per client |
| IN-09 Holiday fund (RJV/ONVA) | The Mijn vakantierekening service authenticates the worker, by the itsme® app, an eID card reader, a security code on a smartphone, or eIDAS. No employer-facing authenticated interface was found | Confirmed. The flow is employee-mediated |
| OUT-17 Social balance sheet (NBB Filing) | Accessed through the National Bank's personal workspace. Filed by the client's accountant, not by payroll | Out of the engine's authentication perimeter |
| OUT-19 DB2P (Sigedis) | An SFTP channel on the social security extranet, filed by the pension institution | Out of the engine's authentication perimeter |
| IN-10 Fleet data, IN-11 and OUT-13 voucher issuers, OUT-14 pension premium file | NOT FOUND - requires direct inquiry to the provider. These are commercial counterparties. Issuers publish that they offer an API, SFTP connectors and import files and that they connect to the major Belgian payroll providers, but no public technical or authentication specification is published | Genuine gap; see Section 8 |
| IN-12 time and attendance, OUT-15 general ledger | Client-specific by definition; set in the implementation contract | Not an authority matter |

### 3.4 Per-integration authentication lookup

| ID | Authentication mechanism |
| --- | --- |
| OUT-01 / IN-01 Dimona | Batch: technical user + SSH RSA key pair, plus a qualified certificate for the FS signature. REST v2: OAuth 2.0 Client Credentials + X.509 certificate in Chaman. Web: CSAM — eID, itsme or eIDAS |
| OUT-02, OUT-03 / IN-02, IN-03 DmfA | Batch: as Dimona batch. Online service (≤ 49 employees): CSAM — eID, itsme or eIDAS |
| IN-04 NSSO contribution and provision notices | No caller authentication — the NSSO pushes a letter or an e-Box message. Reading the e-Box requires CSAM |
| IN-05 Student@work | CSAM on the secured portal, or the student's access code from the Attestation for the future employer |
| OUT-04 / IN-07 Finprof | Belgian eID, or a qualified certificate from GlobalSign, Isabel or Certipost |
| OUT-05 / IN-06 Belcotax-on-web | Belgian eID (brochure); itsme® also offered on the access page. Company access by eGov role assignment |
| OUT-06 / IN-15 DRS / ASR, OUT-07 / IN-16 work accident | Batch: as DmfA batch, with the scenario's application code — the response is collected from the same authenticated OUT directory. Web: CSAM. The insurer's own channel for IN-16 is insurer-specific and NOT FOUND |
| OUT-08 / IN-17 Limosa — descoped; these credentials are the foreign declarant's, not the Belgian client's | Web declaration. The Limosa-1 receipt is returned in the same authenticated web session — the foreign employer's session — so no credential arises on the Belgian payroll side and none needs provisioning for this build. Technical channel for that declarant: GlobalSign certificate + technical user. The Belgian-side art. 141 exception report is made through socialsecurity.be under the client's ordinary social-security-portal access, which is already provisioned for the in-scope filings |
| OUT-09, OUT-10, OUT-11 / IN-14 SEPA | Set by the client's bank; no authority-level standard. The payment status report is retrieved over the same bank channel and under the same credentials as the payment file |
| OUT-12 garnishment, IN-13 attachment order | None — no electronic channel exists in either direction. The order is served by bailiff's writ, registered post or delivery against receipt, and the declaration of garnishee returns the same way. Authentication is physical service, not a credential |
| OUT-13 / IN-11 vouchers, IN-10 fleet, OUT-14 / IN-18 pension premium | NOT FOUND - requires direct inquiry to the provider |
| OUT-16 electronic payslip | Employee consent under the Law of 3 June 2007; provider-specific access control |
| OUT-18 / IN-19 Checkinatwork | OAuth 2.0 / OpenID on the social security API Gateway; GlobalSign certificate + technical user for the channel. The presence-registration response returns on the same authenticated call |

## 4. Technical Specifications

### 4.1 The NSSO batch channel — the spine of Belgian payroll integration

Every NSSO declaration a payroll provider files — DmfA, DmfA modification, Dimona, the DRS/ASR scenarios, temporary unemployment, the single works declaration — travels down the same batch channel with the same file mechanics. Building it once serves all of them.

#### 4.1.1 Transport

| Parameter | SFTP | FTP |
| --- | --- | --- |
| Host | sftp.socialsecurity.be | ftp.socialsecurity.be |
| Port | 8022 — the firewall must permit SFTP traffic to this port | 21 |
| Authentication | Technical user (UMxxxxxx / EXPxxxxxx) + SSH key pair | Technical user + password |
| Maximum file size | 200 MB per file, a limit the NSSO attributes explicitly to the requirements of signature validation | 200 MB per file |
| Transport advice published by the NSSO | A stable connection is critical; uploading over a wireless connection is advised against because small disturbances break the transfer. Sufficient bandwidth must be available during the transfer | Same |

#### 4.1.2 The four-file submission set

A submission is not one file. It is a set placed in the inbound directory in a fixed order.

| File | Role | Required in production | Required in test / simulation |
| --- | --- | --- | --- |
| FI | The declaration file, in XML. Identical in form for all channels | Yes | Yes |
| FS | The detached PKCS#7 signature over the FI file | Yes | No, but it is validated if supplied |
| GO | An empty file whose arrival is the signal that the set is complete and processing may start. It must always be placed last | Yes | Yes — the GO file is mandatory even in simulation |
| TD | An empty file meaning To Delete: the FI and FS already placed must not be processed. Used when the placed files are known to be wrong | Only when cancelling | Only when cancelling |

A declaration may be split into a maximum of 9 parts. Each part needs its own FI and its own FS, but the set takes one GO file (or one TD file). DRS and temporary unemployment declarations cannot be split, and their file names therefore have no parts component.

#### 4.1.3 File naming

FI.XXXX.123456.20120213.00001.R.1.1

FS.XXXX.123456.20120213.00001.R.1.1

GO.XXXX.123456.20120213.00001.R.1

TD.XXXX.123456.20120213.00001.R.1

| Position | Meaning |
| --- | --- |
| 1 | FI declaration, FS signature, GO start processing, TD cancel processing |
| 2 | Application code — DMFA original DmfA, DMWA DmfA modification, DMRQ DmfA consultation, DIMN Dimona, WECH DRS unemployment, ZIMA DRS indemnities, AOAT DRS work accidents, TWCT temporary unemployment, DDTN works declaration, PFRQ personnel file consultation, VBLV validation book |
| 3 | Sender number, allocated when the first channel is created for that capacity |
| 4 | File creation date, YYYYMMDD |
| 5 | A unique sequence number of the sender's choosing, unique per creation date and per environment. Any alphanumeric characters |
| 6 | Environment: `R` production, `T` circuit test, `S` DmfA declaration test |
| 7 | Total number of parts (absent for DRS and temporary unemployment) |
| 8 | The part number (absent for DRS and temporary unemployment) |

#### 4.1.4 Directories and environments

| Environment | Inbound directory | Outbound directory | What it exercises |
| --- | --- | --- | --- |
| Production, extension R | IN | OUT | Everything |
| Circuit test, extension T | INTEST | OUTTEST | The whole control circuit as in production, with a check of the worker identification data but without the Sigedis identification check. Returns notifications, PID and DMNO. A positive notification saves the declaration in the simulation environment, and — as in production — the circuit test is limited to one accepted declaration per NSSO-number-and-quarter combination |
| Declaration test, extension S (DmfA only) | INTEST-S | OUTTEST-S | All reception and content controls, but no check of the worker identification data. Returns a notification but no DMNO and no PID. Because nothing is saved, the same declaration can be tested repeatedly |

The choice between T and S is a real design decision. S is the environment for iterating on a DmfA build; T is the environment for a single end-to-end rehearsal.

Output files are not retained indefinitely. The NSSO instructs senders to copy the files from OUT to their own storage and then delete them from the NSSO server, because space must be reserved for all senders. No retention period is published.

#### 4.1.5 Compression and encoding on the NSSO batch channel

| Question | Answer |
| --- | --- |
| Is client-side compression required? | No compression requirement is published for the sender. The 200 MB limit is stated as a per-file limit |
| Is compression referenced anywhere? | Yes, but on the NSSO's own side: anomaly code 509, "Taille totale des fichiers FI et FS supérieure à la limite imposée après compression" — the combined size of FI and FS exceeds the imposed limit after compression. This is the failure mode to design against by splitting into parts |
| Character encoding of the FI file | NOT FOUND in the channel documentation. The SFTP and FTP manuals specify naming, size and signature but not the XML encoding. It is governed by the XSD and the glossary of each application, held in the NSSO TechLib. Requires confirmation against the application XSD at build time |

### 4.2 DmfA — OUT-02, OUT-03

| Parameter | Value |
| --- | --- |
| Format | XML validated against an XSD defined by the NSSO |
| Structure | Functional blocks, each with numbered zones. The DmfA glossary extract held in 00-official-sources/spec-sources/dmfa_glossary.json carries 213 zones across 32 functional blocks. Each zone has a number, an xml_label, a type, a length, a presence rule and its own anomaly list — for example zone 00082 CODE TRAVAILLEUR COTISATION, xml_label ContributionWorkerCode, numeric, length 3, presence Indispensable, appearing in blocks 90001 WorkerContribution and 90337 ComplIndemnityContribution |
| Current version | Glossary and structured annexes at 2026/2. An erratum to the 2026/2 structured annex Codes travailleurs was published on 25 June 2026 |
| Batch application codes | DMFA original, DMWA modification, DMRQ consultation |
| Web channel limit | The DmfA online service is for declarations concerning up to 49 employees. Above that, batch |
| Submission window | Quarterly. There is no published intraday cutoff; the deadline is the last day of the month following the quarter (CCG Module 1.2). A demo version of the online service is published for dummy declarations and needs no access procedure |
| Test facility | The S and T environments described in 4.1.4, plus the published DmfA demo for the online service |

### 4.3 Dimona — OUT-01, IN-01

| Channel | Specification |
| --- | --- |
| Batch | XML over SFTP/FTP, application code DIMN, same FI/FS/GO mechanics. Cannot be split into parts |
| REST v2 | POST /dimona/v2/declarations with application/json; responses application/json;charset=UTF-8. On success `201 Created`, with the declaration identifier returned in the `Location` header, from which the Dimona number is read. Retrieval is GET /declarations/{dimonaNbr} |
| REST status codes | 201 received, 400 invalid request parameter, 403 not permitted to declare for this employer, 500 internal server error. On the GET: 200 found, 403 forbidden, *`404` not found or not yet processed***, 500 internal server error |
| Version history | v2 in production from 13 June 2024 (simulation 8 May 2024). v1 was valid until 30 June 2025 and is decommissioned — a v1 integration is out of support |
| Other channels | Personnel file (secured web), Dimona Mobile app, unsecured web form |
| Encoding | UTF-8 on the REST channel, stated in the response media type |

### 4.4 Finprof — wage withholding tax return, OUT-04

The published file description is BESTANDSBESCHRIJVING SS274EUR-XML, FPS Finance, Direct Taxes, Directorate VI/4, dated 26 September 2011. It remains the currently published specification.

| Parameter | Value |
| --- | --- |
| Schema | Finprof.xsd |
| Encoding | ISO-8859-1 (ISO Latin 1) — note that this is not UTF-8, and differs from both the SEPA and the Belcotax conventions |
| Root element | Declaration274, with attribute CreationDate in the form YYYY-MM-DD |
| Envelope | CoreHeader, imposed by the UME2 communication standard. MessageType must be REQUEST, Origin must be FINPROF, DocumentType must be Multiple_PRP_Declaration |
| Capacity | One file may contain from one to several thousand declarations. The multiple declaration is only applicable where an institution files on behalf of several employers |
| Sorting rule | SingleDeclaration elements must be sorted ascending on District, Office, Language, ReferenceNumber, Year, Period, Year325, RevenuNature. Where all of those are equal, the declaration is only admitted if TaxableRevenu or Prepayment differ, and positive Prepayment amounts must precede negative ones |
| Amounts | TaxableRevenu and Prepayment, maximum 13 digits, expressed in eurocents, with a leading - for a negative amount |
| Period codes | 0100–1200 for the months. Then five period codes that are easy to mis-pair and are set out here in full: `0103` first quarter, `0406` second quarter, `0709` third quarter, `1011` advance on the fourth quarter, `1012` fourth quarter, and `1215` the first 15 days of December filing by debtors declaring more than EUR 2,500,000. Note in particular that 1011 and 1012 are two different obligations, and that 1215 is not the fourth-quarter advance |
| Income-nature codes (RevenuNature) | 10 ordinary remuneration, 20 directors' remuneration, 30 attendance fees and miscellaneous, plus the exemption codes — including `06` shift and night premiums, `44` and `45` overtime under Article 275/1 ITC 92, 05/07/09/31/32/33 scientific research, 46 profit sector, 47 social maribel, 70 Flemish reduction. These are the codes onto which the CCG Module 10.1 intermediate "withholding tax exemptions claimed (overtime, shift and night work, student work)" must be mapped |
| Payment reference | A 12-digit structured communication: 7 digits from the stem of the employer reference number, 3 digits of period code (numeric and greater than 600), then a 2-digit check digit equal to the remainder of the preceding 10 digits divided by 97, with 00 replaced by 97 |
| Social secretariat | ThirdDeclarer / SecretariatCode; where the debtor is not affiliated to a recognised social secretariat, the value `9998` must be placed in the field |
| File size limit | NOT FOUND — no limit is stated in the file description |
| Submission window | A Test bestand xml facility is published on the FinProf page. The channel for an income year closes after 31 August of the following year; for income year 2025 the application accepted submissions until 4 September 2026, 16:00 through FinProf Legacy |

### 4.5 Belcotax-on-web — 281.10 and 325.10, OUT-05

| Parameter | Value |
| --- | --- |
| Format | XML, validated against `belcotax-2025.xsd` for income year 2025. The technical documentation page carries the schema as Belcotax 2025 XSD (ZIP, 42.38 KB), version 2, dated 29 January 2026 |
| Pre-send preparation | An offline validation module — validatiemodule inkomsten 2025, dated 15 January 2026 — is downloaded and run locally. It requires Java 8. It performs a first validation and then encodes the file into the proprietary .bow format, which is what is actually uploaded |
| File composition | *Only one verzending (sending) part is permitted per XML file.* Multiple declarations within it remain possible |
| Amounts | In eurocents, containing neither a comma nor a decimal point |
| Dates | DD-MM-JJJJ |
| Field lengths | The lengths in the brochure's tag table are maxima across all fiche types; the exact maximum for a given fiche type is defined in the XSD, which is authoritative |
| Derived filing | Only the 281 fiches are submitted. FPS Finance derives the 325 statements from the 281 data — the summary statement is not separately built or sent |
| National register number | Mandatory on a 281.20; its absence causes rejection of the whole sending. On a 281.10 its absence produces a waivable error rather than a rejection |
| Encoding | NOT FOUND — the brochure prescribes amounts, dates and structure but does not state an XML character encoding. It must be taken from belcotax-2025.xsd at build time |
| File size limit | NOT FOUND — no limit is published |
| Paper | Accepted only with explicit authorisation from the regional withholding-tax management team. Absolute prohibition on paper fiches used to correct data already filed through Belcotax |

### 4.6 SEPA payment files — OUT-09, OUT-10, OUT-11

| Parameter | Value |
| --- | --- |
| Message | ISO 20022 `pain.001.001.09`, Credit Transfer Initiation |
| Belgian implementation guidelines | Febelfin, XML Message for Credit Transfer Initiation, 2025 version 1.3, aligned to the EPC SEPA Credit Transfer Customer-to-PSP Implementation Guidelines 2025 v1.0 |
| Namespace | urn:iso:std:iso:20022:tech:xsd:pain.001.001.09 |
| Encoding | UTF-8 is mandatory, and the Latin character set must be used. References, identifications and identifiers additionally must not start or end with a single / and must not contain // |
| Salary payments | The message is explicitly intended, among others, for "an entity administering the salary payments of a company's employees". Category Purpose `SALA` identifies a salary payment |
| Batch booking | For Belgian payment service providers, when <BtchBookg> is absent the default is `true` — the payments are booked as a single aggregate. This must be set deliberately, because it changes what the employee's counterparty sees and what the client's statement shows |
| Feedback message | Payment Status Report, per the Febelfin XML Message for Payment Status Report 2025 version 1.0 |
| 2026 change to configure | Hybrid addresses may be used from 5 October 2025, and unstructured addresses will be forbidden from 15 November 2026. A payroll SEPA file built with an unstructured creditor address will stop being accepted inside the 2026 income year |
| File size / transaction count limit | NOT FOUND in the Febelfin guidelines. These are set per bank and per channel |
| Cutoff times | NOT FOUND at standard level — cutoffs are bank-specific. The binding payroll rule is the CCG Module 1.2 rule that a pay date falling on a non-banking day is brought forward to the preceding banking day, never deferred |

### 4.7 Presence registration — OUT-18

| Parameter | Value |
| --- | --- |
| Protocol | REST web service presenceRegistration, secured on the social security API Gateway. A SOAP variant also exists |
| Bulk capacity | The registerInBulk method creates one or more presences, up to 200 per request |
| Integration pattern | The NSSO states the service is designed to be integrated into an existing planning, track-and-trace or registration system |
| Documentation | Gebruikershandleiding REST Webservice presenceRegistration, published in successive versions; version 1.3 was current at the time of research |

### 4.8 Flows with no published technical specification

| ID | What is published | What is not |
| --- | --- | --- |
| IN-10 fleet data | Nothing at interchange level. Renta Solutions operates SaaS platforms for the leasing federation's members, and Renta publishes the Renta Norm 2026 — but that is a vehicle return condition standard, not a data interchange format | NOT FOUND - requires direct inquiry to the leasing company. The data contract must be agreed per client and per lessor: catalogue value, CO2, fuel type, first registration date, order date, availability dates, personal contribution |
| IN-11 and OUT-13 vouchers | Issuers state publicly that they offer an API, SFTP connectors and automatic import files, and that they connect to the major Belgian payroll providers | NOT FOUND - requires direct inquiry to the issuer. No format, no schema, no endpoint is published |
| OUT-14 pension premium file | Nothing | NOT FOUND - requires direct inquiry to the insurer or pension fund |
| OUT-12 garnishment | The Judicial Code procedure and the 15-day declaration-of-garnishee obligation | NOT FOUND — no electronic interchange format. The declaration goes by registered post or against receipt |
| IN-04 NSSO provision notice | The calculation basis and the delivery route | NOT FOUND — no machine-readable structured feed is published for a private-sector employer. Social service providers have an online service holding the advance documents, debit notices and amendment notices, but no file specification is published for it |
| IN-08 holiday certificate | The legal content requirement (CCG Modules 2.2 and 9.1) | NOT FOUND — no statutory electronic interchange format for the white-collar holiday certificate |
| OUT-16 electronic payslip | The legal conditions of the Law of 3 June 2007 | No statutory file format is prescribed. This is a design freedom, not a gap |

## 5. Error Handling

### 5.1 The NSSO anomaly model

This is the most fully documented error model of the four authorities, and it is worth building to precisely because the same model governs DmfA, Dimona and every DRS scenario.

#### 5.1.1 The response sequence

| Message | What it is | What it means |
| --- | --- | --- |
| ACRF  accusé de réception de fichier | The reception acknowledgement. One ACRF is sent per file received | Positive: the file's structure is sound and the NSSO can proceed to process it. It does not mean the declaration is accepted. Negative: the system found problems in the structure of the file, and nothing is processed |
| Notification | The result of the content control | Carries a ticket number uniquely identifying the declaration, a handling result code  `1` accepted, `0` rejected  and an <AnomalyReport> block listing the anomalies found. It may also carry <NewValue> fields where the system itself supplied a corrected value |
| PID | Technical identification keys | Returned only on an initial DmfA |
| DMNO  avis rectificatif de cotisations | The corrective contribution notice | Sent when the NSSO's control system applies an automatic correction after acceptance. Carries <WRDclPart>  what was declared  and <WRCorrectedPart>  the corrected blocks |

#### 5.1.2 Anomaly code structure

An anomaly is reported as a five-position zone number, a hyphen, and a three-position error type, followed by a severity letter.

00082-035  B     zone 00082 CODE TRAVAILLEUR COTISATION

anomaly 035 "Incompatibilité trimestre - catégorie employeur"

severity B - blocking

The severity letter is the operational instruction and there are three values.

| Severity | Meaning | Consequence |
| --- | --- | --- |
| B  blocking | A structural or definitional breach | A single B anomaly rejects the entire declaration |
| P  percentage | A cumulative anomaly | Counted. Once the count exceeds a threshold percentage, the entire declaration is rejected. A handful is tolerated; a systematic mapping error is not |
| NP  non-percentage | Informational | Never counted, never causes a rejection |

The distinction between B and P is the one that matters in design. A B anomaly is a hard gate to be caught before submission. A P anomaly will pass in small numbers and then fail the whole quarter once a mapping defect scales across the population  which is exactly the failure mode that surfaces at go-live rather than in a pilot.

#### 5.1.3 The code list

| Property | Value |
| --- | --- |
| Source document | NSSO, Annexe 30 : Liste générale des codes anomalies |
| Version read | 2024/1 |
| Number of codes | 498 distinct codes |
| Numeric range | 001 to 536, with 38 numbers unused in that range where codes have been withdrawn or never allocated. Each code carries a start and an end date of validity |

Representative codes across the range, quoted exactly:

| Code | Label (FR) | What it tells you |
| --- | --- | --- |
| 001 | Non présent | The generic mandatory field missing |
| 002 | Non numérique | Type violation |
| 007 | Total calculé différent du total déclaré | The declared total does not match the sum  the classic no-netting breach of CCG Module 10.1 |
| 030 | Incompatibilité code travailleur | The NSSO worker code does not fit the rest of the line |
| 031 | Incompatibilité entre le nom et le NISS | Identity mismatch against the authentic source |
| 038 | La signature Isabel n'est pas correcte | Signature failure |
| 039 | L'utilisateur Isabel n'est pas autorisé à expédier en réel | The sender is not authorised for the production environment |
| 070 | NISS inconnu à la source authentique | The national register number is not known |
| 088 / 089 / 090 / 091 / 092 / 093 | Schéma inconnu / Root inconnu / Erreur de cardinalité / Erreur de séquence / Elément inconnu / Longueur incorrecte | The XSD-level failures |
| 103 | Syntaxe XML incorrecte | Malformed XML |
| 102 / 104 | Expéditeur non autorisé pour ce matricule / Expéditeur non autorisé | Channel authorisation failure  the sender is not mandated for that employer |
| 108 | La structure du nom d'un fichier GO n'est pas correcte | File naming failure on the GO file |
| 270 | Délai d'introduction non respecté | The submission deadline was missed |
| 280 | Fichier ZIP Invalide | Container failure |
| 410 | Différence avec les données déclarées en DmfA(PPL) | Cross-declaration inconsistency |
| 420 | Le nombre de jours déclaré dépasse le nombre de jours que compte la période | Service-code days exceed the period |
| 430 | Le(s) fichier(s) posant problème lors de l'envoi initial a/ont été supprimé(s) | The confirmation returned after a TD cancellation |
| 502 | Différence heures en DmfA - heures planifiées en Dimona avec cotisations réduites | The DmfA-versus-Dimona reconciliation the CCG describes in Module 10.2 |
| 509 | Taille totale des fichiers FI et FS supérieure à la limite imposée après compression | The size ceiling |
| 518 | Données deuxième pilier pension manquantes | Missing second-pillar data  the 8.86% and Wijninckx blocks of CCG Module 5 |
| 528 | Base de calcul de la cotisation spéciale prime Corona ou prime pouvoir d'achat trop élevée | Ceiling breach on a special premium |
| 535 / 536 | Flexijob pas de cumul avec une autre relation de travail / Pas dans le champ d'application Flexijob | The flexi-job eligibility rules of CCG Module 7.1 |

#### 5.1.4 Which anomalies attach to which field

The anomaly list is not global  each DmfA zone declares in advance which anomalies can be raised against it, and at what severity. The glossary extract held locally shows the shape and the scale of this.

| Measure | Value |
| --- | --- |
| Zones carrying a declared anomaly list | 213 |
| Zone-anomaly pairs at severity B | 1,344 |
| Zone-anomaly pairs at severity P | 148 |

Worked example  zone 00082 CODE TRAVAILLEUR COTISATION declares, among others: 00082-001 Non présent B, 00082-002 Non numérique B, 00082-008 Pas dans le domaine de définition B, 00082-030 Incompatibilité code travailleur B, 00082-020 Incompatibilité avec la commission paritaire B, 00082-026 Incompatibilité code FFE P, 00082-061 Travailleur trop jeune P.

This is directly buildable: the engine can carry the zone-to-anomaly-to-severity table and pre-validate against it rather than discovering the rejection after the deadline.

#### 5.1.5 Retry and correction

| Situation | Route |
| --- | --- |
| The FI/FS files placed are known to be wrong, before the GO file is placed | Place a TD file instead. The sender receives an ACRF with ResultCode 0, ErrorID ACRF-430, and the deletion date and time appended to the file name  for example TD.DMFA.123456.20120213.00001.T.1_20120213_102735 |
| Negative ACRF | The file was not processed. Correct the structure and resubmit as a new sending with a new sequence number |
| Notification with result code 0 (rejected) | Nothing is stored. Correct the anomalies and resubmit the original declaration type |
| Notification with result code 1 (accepted), but wrong content | File a DmfA modification declaration (DMWA) for the original quarter, not for the current one. The NSSO recalculates and issues a debit or credit (CCG Module 10.5). The rates, thresholds and reductions of the original quarter apply, not those in force at the time of correction (CCG Module 9.2) |
| Automatic correction applied by the NSSO | A DMNO arrives. Reconcile <WRDclPart> against <WRCorrectedPart> and carry the difference into the ledger |
| Published retry policy  automatic retries, back-off, maximum attempts | NOT FOUND - requires direct inquiry to the authority. The NSSO publishes the correction routes above but does not publish a retry policy for the channel itself |

CCG Module 10.5 supplies the rule that governs all of this and that must not be engineered around: corrections cascade. A corrective DmfA changes the quarterly wage, which can change the special social security contribution band and the social work bonus, which changes the net, which changes the taxable base and therefore the 281.10. The engine must be able to re-run the affected quarter end to end rather than patching a single figure.

### 5.2 Belcotax-on-web

#### 5.2.1 Three classes of anomaly

The offline validation module classifies every finding into one of three types, and the classification determines whether the file can even be sent.

| Class (NL) | Class (EN) | Effect |
| --- | --- | --- |
| Blokkerende fouten | Blocking errors | The file is not converted into the encoded .bow format and therefore cannot be sent at all |
| "Omzeilbare" fouten | Waivable errors | Encoding and conversion do happen, so the file can be sent  but it is in principle refused. The sender is invited by e-mail to request a lifting of the problematic validation from the Belcotax service at belcotax@minfin.fed.be. The file is only processed and accepted if that service gives express permission. The request must quote the sending number and everything FPS Finance needs for a reasoned decision, in particular a copy of the error list |
| Waarschuwingen | Warnings | Reported; do not prevent processing |

#### 5.2.2 Error message structure

The first 100 errors are shown on screen and written to a local file named error.txt. Where the errors are not blocking, the same error list is attached to the acknowledgement e-mail.

Tag: Lijn: 5 kolom: 20, v0010_bestandtype :

Het veld «v0010_Bestandtype» moet de vermelding Belcotax bevatten

Lijn gives the line, Kolom the position on the line, Tag the field name, followed by the description of the error.

#### 5.2.3 The two-phase status model

| Phase | Check | Resulting status |
| --- | --- | --- |
| Phase 1  on receipt, whatever the sending method. Identical to the offline validation module's checks: format and coherence of the data | Format and coherence | Gevalideerd (validated) if no waivable errors; Wachten op autorisatie (awaiting authorisation) if waivable errors were found; Geweigerd (refused) if the Administration refused the waivable errors |
| Phase 2  only if phase 1 found no anomaly. Detects: wrong KBO numbers; double use; wrong or unrecognised social secretariat numbers; absence of the correct identification of a fiche to be corrected or cancelled | Content and identity | Goedgekeurd (approved) if nothing was found; Validatie 3 OK if the social secretariat or agency is not competent; `Geëxplodeerde fout` for a double declaration, or where a correction or cancellation could not be matched to an original fiche |

If the result is validated, all the data is in the FPS Finance database  but the brochure is explicit that this does not mean the amounts on the fiches are validated from a tax point of view. If the result is file refused, no data is recorded.

#### 5.2.4 Correction and resubmission

| Step | Rule |
| --- | --- |
| Channel | Data filed through Belcotax must be corrected through Belcotax, either by the screens or by a corrective file. Paper corrective fiches for data already filed through Belcotax are prohibited and will be returned |
| Marking a grouped-correction file | Value `1` in zone `0.025` |
| Identifying the sending being corrected | The sending number in zone `0.026`, taken from the acknowledgement of the original file |
| Identifying the fiche | The FPS-imposed fiche number  281.xx plus sequence, zones 2.008 and 2.009  and, where completed, the sender's own fiche number in zone 2.010 |
| Action | Zone `2.028`: 1 correct, 2 add, 3 cancel |
| Ordering | Cancellation first, then addition. Explicitly flagged in the brochure |
| Identity or address change | Accepted only where the national register number was present in both the original and the corrective sending. Where a fiche was filed without a national register number or with a wrong one, the only route is to cancel the fiche and add a new one |
| Sequencing | Where two successive modifications add fiches to the same sending, wait for the result of the first processing before sending the second |
| Timing | Modifications and cancellations should preferably be made before 1 August. From 1 August they raise a late-correction warning  the waivable error having been lifted  and are still processed automatically. A reduction in the amount of withholding tax will never give rise to a refund to the debtor of the income |

### 5.3 Finprof

FPS Finance publishes a sanction regime rather than an anomaly code list. It is reproduced because it is the operative consequence of an integration failure.

| Failure | Sanction |
| --- | --- |
| Late payment | Late-payment interest, and an administrative fine on top  introduced because some employers were waiting for the assessment before remitting |
| Non-filing, or incomplete or incorrect filing coupled with non-payment or insufficient payment | A tax increase of 10% up to a maximum of 200% |
| Non-filing or late filing | A fine of EUR 50 to a maximum of EUR 1,250 |
| Non-payment or late payment | A fine of 10% of the unpaid or late-paid amount, or of the balance, with a minimum of EUR 50 and a maximum of EUR 1,250, rounded down to the lower multiple of EUR 10. EUR 0 on a first offence |

Since 2016 the Documentation Centre applies these systematically to missing declarations, incomplete declarations and failure to pay.

Reconciliation control. FPS Finance issues each debtor an annual comparison document between the 325 statements (Belcotax) and the 274 declarations (Finprof). After the FinProf closing date for the income year  which falls after 31 August  FPS Finance sends the definitive result and no further correction is possible for the closed fiscal year. Three outcomes are possible: no discrepancy; the 325 exceeds the 274, in which case the difference must be paid; or the 325 is lower than the 274, in which case the difference is refunded only if the debtor can justify the reason for the discrepancy. This is the concrete mechanism behind the CCG Module 10.5 requirement to reconcile the twelve monthly returns against the 281.10 totals before the Belcotax deadline.

A published anomaly code list for Finprof itself was NOT FOUND - requires direct inquiry to the authority (info.finprof@minfin.fed.be).

### 5.4 Dimona REST

| Code | Meaning | Handling |
| --- | --- | --- |
| 201 Created | Declaration received. The identifier is in the Location header | Store the Dimona number against the employment (IN-01) |
| 400 | Invalid request parameter | Correct and resend |
| 403 | Not permitted to declare for this employer | A mandate or channel problem, not a data problem |
| 404 on the GET | Declaration not found or not yet processed | The two cases are not distinguished by the status code. Poll, then escalate on a timeout |
| 500 | Internal server error | Retry |

No retry policy, back-off schedule or idempotency guarantee is published. A 201 followed by a network failure leaves the caller unable to distinguish a duplicate from a loss without a subsequent GET, so the integration must be built to reconcile on the Dimona number rather than to blind-retry.

### 5.5 SEPA

Feedback is the ISO 20022 Payment Status Report, registered as IN-14 in Section 1 so that it can be scheduled and monitored on its own, per the Febelfin XML Message for Payment Status Report, 2025 version 1.0. Reason codes are the ISO 20022 external code set; the bank determines which subset it returns and on what schedule. NOT FOUND at standard level: there is no Belgian-specific reject code list, and no standard retry policy  both are set per bank in the channel agreement.

### 5.6 Summary  where an error model exists and where it does not

| Integration | Documented error codes | Documented correction route | Documented retry policy |
| --- | --- | --- | --- |
| OUT-01/02/03/06/07 NSSO | Yes  498 codes, per-zone severity | Yes  TD, resubmission, modification declaration | No |
| OUT-05 Belcotax | Yes  three anomaly classes, six statuses, structured error text | Yes  fully specified, by zone | Not applicable; resend after correction |
| OUT-04 Finprof | No code list found  a sanction regime instead | Yes  within the published correction windows, then the channel closes | No |
| OUT-01 Dimona REST | HTTP status codes only | Correct and resend | No |
| OUT-09/10/11 SEPA | ISO 20022 external codes, bank-selected | Per bank | Per bank |
| IN-10, IN-11, OUT-13, OUT-14 commercial | NOT FOUND | NOT FOUND | NOT FOUND |

## 6. SLA and Deadlines

Two different things are held in this section and they must not be conflated. Filing deadlines are statutory, are already confirmed in the CCG, and are restated here so that the register is usable on its own. Response-time SLAs are what the authority undertakes to give back, and they are the genuinely-new research — which for Belgium mostly means finding that they are not published.

### 6.1 Filing and payment deadlines

Restated from CCG Modules 1.2 and 10.1. These are confirmed content; the CCG is the source of truth.

| ID | Obligation | Periodicity | Deadline |
| --- | --- | --- | --- |
| OUT-01 | Dimona | Per event | Before the employee starts work. End of employment by the first working day after |
| OUT-02 | DmfA | Quarterly | The last day of the month following the quarter — 30 April, 31 July, 31 October, 31 January |
| OUT-10 | Social security balance payment | Quarterly | The same date as the DmfA deadline |
| OUT-10 | Social security monthly advances | Monthly, where due | The 5th day following each month of the quarter. Compulsory where the contributions due for quarter K-2 exceeded EUR 6,197.34 |
| OUT-04, OUT-11 | Wage withholding tax return and payment — standard | Monthly | The 15th of the month following the month of payment |
| OUT-04, OUT-11 | Wage withholding tax return and payment — small employers | Quarterly | The 15th of the month following the quarter. Permitted only where the total withholding of the reference year did not exceed the Article 412 ITC 92 threshold; the reference amount used to set the 2026 periodicity was EUR 50,240 |
| OUT-05 | Forms 281.10 and 325.10 through Belcotax-on-web | Annual | 28 February of the year following the income year |
| OUT-02 | Fourth-quarter DmfA, including the Wijninckx contribution | Annual | 31 January |
| OUT-06 | DRS / ASR scenario declarations | Per event | On the triggering event |
| OUT-07 | Work accident declaration | Per event | Within 8 days of the accident |
| OUT-08 | Limosa declaration — not scheduled here: filed by the foreign posting employer, descoped (Section 2.1, Section 2.4) | Per posting, for that third party | Before the posted worker starts. This deadline binds the foreign employer, not the Belgian payroll client, and is listed only so that a reader who expects to find Limosa on this calendar finds the reason it is absent. The Belgian-side art. 141 duty has no periodic deadline — it triggers on a Limosa-1 that cannot be produced |
| OUT-12 | Declaration of garnishee | Per attachment served | Within 15 days of service |
| OUT-16 | Payslip | Per pay period | With each definitive wage payment |
| — | Individual account (Section 2.4) | Annual | Closed within two months of the end of the year |

The two rules that most often break an integration schedule, both from CCG Module 1.2:

1. Filing deadlines falling on a Saturday, Sunday or public holiday are postponed to the next working day.

1. Wage payment dates are not. The Article 9 deadline is absolute, so a pay date falling on a Saturday, Sunday or public holiday is brought forward to the preceding banking day. OUT-09 must be scheduled against the preceding banking day, never the following one.

#### 6.1.1 Two deadline variants found in the FinProf documentation and not carried in the CCG

Both are edge cases outside the CCG's standard-employer scope, and both are registered here because they change the OUT-04 and OUT-11 schedule for the employers they touch.

| Population | Rule |
| --- | --- |
| Debtors who owed less than EUR 25,000 before indexation of withholding tax in the preceding year | File and pay quarterly, within fifteen days following the end of the quarter, and additionally declare and pay by 15 December an advance on the fourth-quarter withholding tax equal to 66% of the withholding tax due for the second quarter of the same year. The FinProf XML specification carries the dedicated period code `1011` for that advance, distinct from `1012` for the fourth quarter itself |
| Debtors who owed at least EUR 2,500,000 of withholding tax in the preceding year | The withholding on income paid or granted during the first fifteen days of December must be declared and paid by 24 December. The FinProf XML specification carries the dedicated period code `1215` for it |

The EUR 25,000 pre-indexation figure and the CCG's EUR 50,240 figure are the same threshold expressed before and after indexation; they are consistent, and this is recorded as a cross-check rather than as a new claim.

### 6.2 Published response-time SLAs

| Integration | Published response time | Status |
| --- | --- | --- |
| IN-06 Belcotax-on-web | 48 hours. "In elk geval ontvangt u binnen de 48 uur na de definitieve verzending per e-mail een verwerkingsbericht met het definitieve resultaat (aanvaard of geweigerd) van de verwerking." — in every case a processing message with the definitive result, accepted or refused, is sent by e-mail within 48 hours of the final sending. FPS Finance adds an escalation rule: a sending must always be followed by an acknowledgement and a processing message; if there is no reply after one week, contact the Belcotax service, especially where the status is awaiting loading or in quarantine | PUBLISHED SLA — the only one found in this register |
| IN-02, IN-03 NSSO batch | No SLA is published. The NSSO's own flow scenarios show the pattern: the ACRF is created on the day the parts are received, and the notification file the next day. One scenario for a modification declaration shows the notification two days after receipt. These are worked examples in the flow documentation, not an undertaking | NO PUBLISHED SLA. The D+1 pattern is a planning assumption drawn from the authority's own examples and must be labelled as such, not quoted to a client as a commitment |
| IN-01 Dimona, REST | No SLA is published. The API returns 404 on the GET while the declaration is not found or not yet processed, which implies asynchronous processing but sets no bound on it | NOT FOUND - requires direct inquiry to the authority |
| IN-07 Finprof | No acknowledgement SLA published. Status is retrieved by the Zoeken function on demand rather than pushed | NOT FOUND - requires direct inquiry to the authority (info.finprof@minfin.fed.be) |
| IN-04 NSSO provisions and debit notices | Not an SLA but a published calendar: employers that are not a provincial or local authority and are not affiliated to a recognised social secretariat receive a letter from the NSSO every month. Provincial and local authorities receive a letter in their e-Box each quarter, on the 15th of the month preceding the start of the quarter | Delivery calendar published; no response-time SLA applies |
| OUT-09, OUT-10, OUT-11 SEPA | No authority-level SLA. Execution times are set by the Payment Services Directive regime and by the bank's cutoff times, per bank and per channel | NOT FOUND at standard level — set per bank in the channel agreement |
| OUT-18 Checkinatwork | NOT FOUND | Requires direct inquiry to the NSSO |
| IN-10 fleet, IN-11 and OUT-13 vouchers, OUT-14 pension premium | NOT FOUND - requires direct inquiry to the provider. Commercial counterparties; any SLA is contractual and per client | Genuine gap |

Summary: one published response-time SLA exists across the whole Belgian register — the Belcotax 48 hours. Everything else is either unpublished or contractual. Any implementation plan that assumes an authority response-time commitment for the NSSO or FPS Finance channels is assuming something Belgium does not publish.

### 6.3 Correction windows

| Integration | Window |
| --- | --- |
| OUT-03 corrective DmfA | No general deadline, but corrections beyond the three-year limitation period are subject to the prescription rules (CCG Module 10.5) |
| OUT-04 withholding tax corrections | Within the published correction windows. For income year 2025: corrections relating to withholding exemptions by 15 May 2026, other corrections by 10 July 2026, and the Finprof channel for that income year closed on 31 August 2026 (CCG Module 10.5). The FinProf application accepted income-year-2025 submissions until 4 September 2026, 16:00 through FinProf Legacy. After the closing date no correction is possible for the closed fiscal year |
| OUT-05 Belcotax corrections | As soon as identified (CCG Module 10.5). Operationally: preferably before 1 August; from 1 August a late-correction warning is raised and the correction is still processed automatically |
| OUT-05 first and second sendings | FPS Finance schedules a first Belcotax filing at the end of January and a second at the end of March, so that all elements are in before the September FinProf closing for the income year |

### 6.4 Time-boxed items to diarise

These expire, and each one silently breaks an integration when it does.

| Item | Expiry or change date | Consequence |
| --- | --- | --- |
| Dimona REST v1 | Valid until 30 June 2025; decommissioned thereafter. v2 in production since 13 June 2024 | A v1 integration is already out of support |
| SEPA unstructured addresses | Forbidden from 15 November 2026 | An OUT-09/10/11 file built with an unstructured creditor address stops being accepted inside income year 2026. Hybrid addresses have been permitted since 5 October 2025 |
| Student@work access code (IN-05) | Valid in the month the attestation was created and the two following months | A cached access code goes stale within a quarter |
| NSSO batch qualified certificate (FS signature) | Per the certificate's own expiry date | On expiry, a new certificate must be loaded to the channel and new .pem and .key files regenerated. Every FS file fails until this is done |
| Belcotax XSD and validation module | Reissued per income year — belcotax-2025.xsd v2 dated 29 January 2026; validation module for income 2025 dated 15 January 2026 | The schema changes annually and the module must be re-downloaded each year. A new, more intuitive Belcotax-on-web version is announced for February 2027, covering income year 2026 |
| NSSO glossaries and structured annexes | Reissued per quarter — currently 2026/2, with an erratum to the Codes travailleurs annex published 25 June 2026 | Code lists move quarterly; a mapping frozen at one version drifts |
| NSSO anomaly code list | Read at version 2024/1 | Confirm the current version before relying on the code range in Section 5.1.3 |
| NSSO OUT directory | Files are not kept indefinitely; no retention period is published | Response files must be collected and deleted promptly, or they are lost |

## 7. Source Register

All technical sources were consulted on 14 August 2026. The Read column distinguishes a document read in full from a page whose content is reported through a search summary. Anything marked summary is a planning input to be re-verified at implementation, not a specification to build against.

### 7.1 Internal artefacts

| # | Artefact | Version | Used for | Read |
| --- | --- | --- | --- | --- |
| A1 | BE-compliance/01-ccg/BE-CCG-001-v1.0.docx | v1.0, 12 August 2026 | All business and legal content: the integration inventory (Module 10.2), the reporting table (Module 10.1), filing deadlines (Module 1.2), payslip requirements (Module 10.3), other compliance (Module 10.4), year-end and correction routes (Module 10.5) | Full, live, in the current document |
| A2 | BE-compliance/02-wtc/BE-WTC-001-v1.0.xlsx, sheet Wage Type Catalogue | v1.0 | Cross-referencing wage types to integrations — the CO2 solidarity contribution, the 8.86% and 4.4% supplementary pension levies, the Wijninckx contribution, the garnishment and wage assignment wage types, the student solidarity contributions, the holiday fund contribution and the 108% uplift | Sheet read and searched |
| A3 | BE-compliance/00-official-sources/spec-sources/dmfa_glossary.json | Derived from the NSSO DmfA glossary | Zone and block structure: 213 zones, 32 functional blocks; per-zone anomaly lists with B/P severities | Full |
| A4 | BE-compliance/00-official-sources/spec-sources/dimona_glossary.json | Derived from the NSSO Dimona glossary | 57 zones, 16 functional blocks | Structure |

### 7.2 National Social Security Office (NSSO / RSZ / ONSS)

| # | Document or page | Version / date | Used for | Read |
| --- | --- | --- | --- | --- |
| S1 | Brochure DmfA online service — socialsecurity.be/site_en/employer/applics/dmfa/documents/pdf/brochure_dmfa.pdf | 17 October 2024 | Web channel limit of 49 employees; batch channel by FTP/SFTP; CSAM login by eID, itsme or eIDAS; e-Box Enterprise feedback; the Dimona / DmfA / DRS relationship; the demo version | Full (local copy) |
| S2 | MANUEL D'UTILISATEUR — Mettre en place un canal SFTP — .../general/helpcentre/batch/document/pdf/manuel_d_utilisateur_sftp_F.pdf | Version 14 | The whole batch mechanic: qualified certificate choice, GlobalSign PersonalSign 3 Pro, eID via Cryptonit, the Isabel impossibility, the SSH key pair, port 8022, FI/FS/GO/TD naming and semantics, application codes, R/T/S environments, IN/OUT directories, the OpenSSL S/MIME signature procedure, OUT directory housekeeping | Full (downloaded and converted locally) |
| S3 | Startup guide du canal de transfert SFTP — .../batch/document/pdf/startup_sftp_F.pdf | Version 10 | Channel setup | Downloaded; not required beyond S2 |
| S4 | FAQ: SFTP voor gestructureerde berichten — .../helpcentre/batch/sftp/faq.htm | Live page | sftp.socialsecurity.be, port 8022, technical user UMxxxxxx/EXPxxxxxx, RSA only, SSH v2 only, key length 2048–4096, 200 MB per file, directory structure | Full |
| S5 | FAQ: gestructureerde berichten via FTP — .../helpcentre/batch/transfer/faq_ftp.htm | Live page | ftp.socialsecurity.be, port 21, technical user and password, qualified certificate public key in Chaman, 200 MB limit attributed to signature verification | Full |
| S6 | DmfA - via batch : Aperçu des processus — .../employer/applics/dmfa/batch/outline.htm | Live page | ACRF positive/negative semantics, notification with ticket number and result code 1/0, <AnomalyReport>, <NewValue>, DMNO with <WRDclPart> and <WRCorrectedPart> | Full |
| S7 | DmfA - via batch : Résultat d'un envoi — .../dmfa/batch/result.htm | Live page | The response set: ACRF, notification, modification notification, PID, DMNO | Full |
| S8 | Scénarios de flux pour la DmfA — .../helpcentre/batch/files/fluxdmfa.htm | Live page | The worked timing examples: ACRF same day, notification next day, D+2 in one modification scenario | Full |
| S9 | Annexe 30 : Liste générale des codes anomalies — socialsecurity.be/portail/glossaires/acr.nsf/.../AN2024-1-FR30.pdf | Version 2024/1 | 498 anomaly codes, range 001–536, with validity dates and exact French labels | Full (downloaded and converted locally) |
| S10 | Dimona via web service — .../dimona/introduction/webservice.htm | Live page | REST v2 in production 13 June 2024, simulation 8 May 2024; v1 valid to 30 June 2025; Chaman channel, access token; OpenAPI YAML published | Full |
| S11 | Dimona API Document — .../dimona/introduction/rest/apidoc_fr.html | Live page | POST /declarations, GET /declarations/{dimonaNbr}, application/json, application/json;charset=UTF-8, status codes 201/400/403/404/500, Location header | Full |
| S12 | REST Documentation — rest-documentation.socialsecurity.be | Live portal | OAuth 2.0 Client Credentials against the social security OAuth server; certificate requirement; the five published REST APIs including Dimona and CIAO | Full |
| S13 | Activating and managing your REST channel in Chaman — rest-documentation.socialsecurity.be/documentation/activating-and-managing-your-rest-channel-in-chaman.html | Live page | X.509 certificate: self-signed or from GlobalSign/DigiCert/QuoVadis/Verisign/Certipost; RSA 2048/3072/4096 or EC P-384/P-521; SHA-256/384/512; key usage Digital Signature; OAuth Client ID self_service_expeditor_X; Chief Access Manager and Technical Manager roles | Full |
| S14 | Dimona — Déclaration immédiate index — .../dimona/index.htm | Live page | The five channels: personnel file, Dimona Mobile, unsecured web form, batch, REST | Full |
| S15 | DRS - La DRS en bref — .../drs/general/about.htm | Live page | Three DRS channels: web, FTP/SFTP for high volumes, paper | Full |
| S16 | NSSO administrative instructions, De verplichtingen > Betaling van de bijdragen > Voorschotten | 2026/2 | Provision calculation; monthly letter to employers; quarterly e-Box letter to provincial and local authorities on the 15th of the preceding month; the Directorate of Collection contact route | Full |
| S17 | DRS - Chômage scenario list — .../drs/onem/index.htm and .../batch/files/fluxdrs3.htm | Live pages | Unemployment scenarios 1, 2, 3, 5, 6, 9, 11 and their paper predecessors (C4, C3.2, C131A, C131B, C103); indemnity scenarios 1 and 2 | Summary |
| S18 | Student@work employer pages — .../employer/applics/studentatwork/index.htm | Live pages | Employer consultation; the Attestation for the future employer; the access code and its validity in the month of creation plus two | Summary |
| S19 | Gebruikershandleiding REST Webservice presenceRegistration — .../check-in-and-out-at-work/documents/pdf/handleiding_ciao-rest_nl_1.7.pdf | Version 1.3 | registerInBulk up to 200 presences per request; secured SOAP and REST on the social security API Gateway with OAuth 2.0 / OpenID | Summary |
| S20 | DmfA TechLib and Nouveau ce trimestre | 2026/2, with an erratum to the structured annex Codes travailleurs dated 25 June 2026 | Current glossary, schema and annex version | Summary |

### 7.3 FPS Finance

| # | Document or page | Version / date | Used for | Read |
| --- | --- | --- | --- | --- |
| F1 | BESTANDSBESCHRIJVING SS274EUR-XML — financien.belgium.be/sites/default/files/downloads/finprof-specification-xmln.pdf | 26 September 2011 | The complete FinProf XML specification: Finprof.xsd, ISO-8859-1, Declaration274, UME2 CoreHeader, Multiple_PRP_Declaration, sorting rules, eurocent amounts, period codes including 1215, the RevenuNature code list, the 12-digit payment reference and its mod-97 check digit, SecretariatCode default 9998 | Full (downloaded and converted locally) |
| F2 | SSGPI, Aangifte bedrijfsvoorheffing langs elektronische weg | 11 September 2024 | FinProf authentication by eID or a qualified certificate from GlobalSign, Isabel or Certipost; identification by KBO number; the 15-day rule and the two threshold variants (EUR 25,000 pre-indexation, EUR 2,500,000); the sanction regime; the annual 325-versus-274 comparison and its three outcomes; the post-31-August closing; the end-January and end-March Belcotax filings | Full (local copy). Provenance note: this is an SSGPI manual written for police zones. Its description of the FinProf application, the FPS Finance deadlines and the sanction regime is general; anything specific to the 2PAY payroll engine or to police zones has been excluded |
| F3 | Finprof e-service page — financien.belgium.be/nl/E-services/FinProf | Live page | Mandatory filing via FinProf since 1 January 2009 (Royal Decree of 3 June 2007); the Test bestand xml facility; the income-year 2025 cutoff of 4 September 2026 at 16:00 through FinProf Legacy | Full |
| F4 | Belcotax-on-web brochure, income year 2025 — .../161-belcotax-on-web-brochure-2025-20260114-1-nl.pdf | 14 January 2026 | Filing deadlines for income year 2025; eID access; the validation module requiring Java 8; the three anomaly classes; .bow encoding; the two-phase status model; error.txt and the first 100 errors; the error message structure; the 48-hour processing message; the correction procedure and zones 0.025 / 0.026 / 2.008 / 2.009 / 2.010 / 2.028; the 1 August warning; belcotax-2025.xsd; eurocent amounts; DD-MM-JJJJ dates; one verzending per file; the 325 derivation | Full (downloaded and converted locally) |
| F5 | Belcotax-on-web brochure, income year 2024 — .../161-belcotax-on-web-brochure-2024-20241206.pdf | 6 December 2024 | Prior-year comparison; confirms the process text is stable year on year | Full (local copy) |
| F6 | Technische documentatie - BOW — financien.belgium.be/nl/E-services/Belcotaxonweb/technische-documentatie | Live page | Belcotax 2025 XSD (ZIP, 42.38 KB), version 2, 29 January 2026; validation module for income 2025, 15 January 2026 | Full |
| F7 | Hoe toegang krijgen tot Belcotax-on-web? | Live page | eID with card reader and PIN, or itsme®; eGov role assignment for company access; the reference-number route for individuals; the rule that the same identification must be used as in Finprof | Full |

### 7.4 Other counterparties

| # | Source | Version / date | Used for | Read |
| --- | --- | --- | --- | --- |
| O1 | Febelfin, XML Message for Credit Transfer Initiation — Implementation Guidelines for pain.001.001.09 | 2025 version 1.3 | Namespace; mandatory UTF-8; the Latin character set and the / rules; salary-payment scope; Category Purpose SALA; <BtchBookg> defaulting to true for Belgian PSPs; hybrid addresses from 5 October 2025 and unstructured addresses forbidden from 15 November 2026; alignment to the EPC 2025 v1.0 guidelines | Full (downloaded and converted locally) |
| O2 | Febelfin, XML Message for Payment Status Report | 2025 version 1.0 | The feedback message for OUT-09/10/11 | Summary |
| O3 | Fedris, Déclaration d'un accident du travail – secteur privé | Live pages | The 8-day deadline; the DRS scenario route; the benign-accident exception and the first-aid register | Summary |
| O4 | Working in Belgium / Limosa portal | Live pages | The Limosa-1 receipt; the Checkinatwork web service; GlobalSign certificate and technical user for the technical channel; the declaration capacity limits | Summary |
| O5 | National Bank of Belgium, Central Balance Sheet Office — Filing | Live pages | XBRL or PDF filing; bulk filing; the separate social balance sheet filing obligation | Summary |
| O6 | Sigedis / DB2P — declaration instructions and push-flux technical specification | Live pages and PDFs | XML per the DB2P XSD; SFTP on the social security extranet; filed by the pension institution | Summary |
| O7 | RJV / ONVA — Mijn vakantierekening | Live pages | Worker-authenticated service (itsme, eID reader, smartphone security code, eIDAS); downloadable holiday-duration attestation, account extract and tax certificate; no employer-facing interface | Summary |
| O8 | Meal and eco voucher issuers; Renta Solutions and the Renta Norm 2026 | Live pages | Establishing the absence of a published interchange specification. Renta Norm 2026 was checked and is a vehicle return-condition standard, not a data format | Summary |

## 8. Open Gaps

Every cell in this register that reads NOT FOUND is collected here, with the enquiry that would close it. A gap in this list is a known unknown with an owner, not an omission.

### 8.1 Gaps at an authority — closeable by direct inquiry

| # | Integration | What is missing | Category | Who to ask |
| --- | --- | --- | --- | --- |
| G1 | OUT-02, OUT-03 DmfA batch | The XML character encoding of the FI declaration file. The channel manuals specify naming, size and signature but not encoding; it is governed by each application's XSD in the NSSO TechLib | Technical spec | NSSO — confirm against the DmfA XSD at build time. Low risk; resolvable from the schema without an enquiry |
| G2 | All NSSO REST channels | The OAuth access token lifetime, and whether refresh is supported | Authentication | NSSO / Smals, via the Chaman channel support route |
| G3 | All NSSO REST channels | The required validity period of the X.509 authentication certificate, if any | Authentication | NSSO, Chaman documentation owner |
| G4 | All NSSO channels | Any retry policy — automatic retries, back-off, maximum attempts, idempotency guarantees. The correction routes are published; the retry behaviour is not | Error handling | NSSO |
| G5 | OUT-01 Dimona REST | Whether POST /declarations is idempotent, and how a caller distinguishes a duplicate from a loss after a network failure following a 201 | Error handling | NSSO |
| G6 | IN-01 Dimona | Any response-time SLA. The 404 on the GET covers both not found and not yet processed, with no bound published | SLA | NSSO |
| G7 | IN-02, IN-03 NSSO batch | Any published response-time SLA. The D+1 pattern used in Section 6.2 comes from the NSSO's own worked flow examples and is not an undertaking | SLA | NSSO |
| G8 | NSSO OUT directories | The retention period for response files. The NSSO states only that files are not kept indefinitely and must be collected and deleted | Technical spec | NSSO |
| G9 | S9 anomaly code list | Whether a version later than 2024/1 of Annexe 30 has been published, given that the DmfA glossary is at 2026/2 | Error handling | NSSO glossary publication |
| G10 | OUT-04 Finprof | A file size or declaration-count limit for the SS274EUR-XML file | Technical spec | info.finprof@minfin.fed.be |
| G11 | OUT-04, IN-07 Finprof | An anomaly or validation code list. FPS Finance publishes a sanction regime but no error code structure | Error handling | info.finprof@minfin.fed.be |
| G12 | IN-07 Finprof | Any acknowledgement SLA. Status is pulled through the Zoeken function, not pushed | SLA | info.finprof@minfin.fed.be |
| G13 | OUT-04 Finprof | Whether the 26 September 2011 file description remains authoritative for income year 2026, and whether an updated schema exists | Technical spec | info.finprof@minfin.fed.be |
| G14 | OUT-05 Belcotax | The XML character encoding and any file size limit. The brochure prescribes amounts, dates and structure but not encoding | Technical spec | Resolvable from belcotax-2025.xsd; otherwise belcotax@minfin.fed.be |
| G15 | OUT-05 Belcotax | The threshold percentage at which accumulated waivable errors trigger refusal, and the criteria the Belcotax service applies when deciding whether to lift a waivable validation | Error handling | belcotax@minfin.fed.be |
| G16 | OUT-18 Checkinatwork | Any response-time SLA | SLA | NSSO |
| G17 | IN-04 NSSO provisions | Whether any machine-readable structured feed of the provision notice, debit notice and contribution statement exists for a private-sector employer or its mandated provider, beyond the social service provider online service | Technical spec | NSSO, Directorate of Collection |
| G18 | IN-05 Student@work | Whether a batch or web-service channel exists for the quota consultation, or whether it is web-only. A web-only quota check is an operational constraint on high-volume student employers | Technical spec | NSSO |
| G19 | IN-08 holiday certificate | Whether any electronic interchange format exists or is planned for the white-collar holiday certificate | Technical spec | NSSO / FPS Employment |
| G20 | IN-09 holiday fund | Whether the RJV/ONVA or the sectoral funds offer an employer-facing data channel, as opposed to the worker-authenticated Mijn vakantierekening | Technical spec | RJV / ONVA and the relevant sectoral funds |
| G21 | OUT-12 garnishment | Whether any electronic channel exists for the declaration of garnishee, or whether registered post and delivery against receipt remain the only routes | Technical spec | National Chamber of Judicial Officers |

### 8.2 Gaps at a commercial counterparty — closeable per client, not per country

These are not authority gaps and will not close by research. They close in the implementation contract, and each needs a data contract agreed per client, per provider.

| # | Integration | What is missing | Data contract to agree |
| --- | --- | --- | --- |
| G22 | IN-10 fleet data | Format, schema, transport, authentication, SLA. The only published Renta standard is a vehicle return-condition standard, not an interchange format | Catalogue value, CO2 value, fuel type, first registration date, order date (which selects the CO2 minimum contribution and the multiplier), availability start and end dates, personal contribution |
| G23 | IN-11 and OUT-13 vouchers | Format, schema, transport, authentication, SLA, error codes. Issuers publish that APIs, SFTP connectors and import files exist, and no more | Per employee per month: days actually worked, face value, employer part, employee part; and the confirmation of vouchers actually issued |
| G24 | OUT-14 supplementary pension premium file | Format, schema, transport, authentication, SLA | Per affiliate: employer premium (base for the 8.86% and the 4.4%), personal contribution withheld from net (base for the 30% withholding reduction), and the pension reserve movement for the Wijninckx contribution |
| G25 | OUT-09, OUT-10, OUT-11 SEPA | Authentication, cutoff times, file size and transaction limits, reject code subset, retry policy — all bank-specific. Febelfin standardises the message, not the channel | Per client: the bank, the channel (portal, Isabel 6, EBICS, host-to-host), the cutoff, and the status report format returned |
| G26 | IN-12 time and attendance, OUT-15 general ledger | No statutory format; by design | Per client, in the implementation |

### 8.3 Pipeline gap — the reason this register was built out of order

| # | Item | Status |
| --- | --- | --- |
| G27 | Related Report Spec for all nineteen outbound integrations | CLOSED. Stage 3 completed and delivered nine Report Specifications in BE-compliance/04-reports-spec/, all at version 1.2 effective 16 August 2026. Section 2.3 now carries the resolved mapping: eleven flows (OUT-01 to OUT-11) are governed by a specification, and the eight remaining flows (OUT-12 to OUT-19) record why none exists or is required. Each filename was taken from the specification's own SIR cross-reference statement, not inferred from the integration ID |

### 8.4 What this register does not claim

For the avoidance of doubt at the next stage gate:

- It does not claim any authority response-time commitment other than the Belcotax 48 hours.

- It does not claim an encoding for the DmfA or Belcotax XML files; both must be taken from their schemas.

- It does not claim a retry policy for any authority channel.

- It names a Belgium report-spec filename only where that specification exists on disk and declares the corresponding integration ID itself. No filename is guessed or inferred from an integration ID, and the eight flows without a specification say so explicitly rather than being left blank.

- Where a source is an authority guidance page rather than a technical specification — notably the GlobalSign-plus-technical-user statement for the Limosa and Checkinatwork technical channel — it is marked as such in Section 3.3 and must be re-verified at implementation.

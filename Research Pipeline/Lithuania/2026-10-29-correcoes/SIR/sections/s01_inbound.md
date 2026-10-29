# 1. Inbound Integrations

Four inbound flows are registered. IN-01 and IN-02 are the return legs of the outbound filings: the status of a document submitted to Sodra and the confirmation and declaration state of a file uploaded to VMI. IN-01 is the return leg of NP-SD2 only if DataService accepts NP-SD2 (G5). IN-03 is the input to the leave integration: the sickness-certificate information the employer needs before it can file NP-SD2. IN-04 is the VMI error and deficiency notice, which reaches people rather than the system. No machine channel for IN-03 or IN-04 was located, and the rows say so.

## 1.1 Inbound register — identification and mapping

| ID | Authority / System | Direction | Product Mapping Required | Description |
|---|---|---|---|---|
| IN-01 | Sodra — DataService | Inbound (response to OUT-01; response to OUT-02 only if DataService accepts NP-SD2, G5; otherwise none, the status is read in EDAS) | false — status only | `getDocumentStatus(docUID)` returns `docStatus` and a description: **NST** not submitted, **FNS** executed / accepted, **PRC** processing, **ARC** archived, **ERR** rejected for errors, **DRF** draft (S3 pages 9, 19-20) |
| IN-02 | VMI — EDSWebServiceUploadFile | Inbound (response to OUT-03, OUT-04) | false — status only | `CheckFileState(FileId)` returns the file confirmation state, the declaration state and the declaration actuality. Confirmation: **10** confirmed, **20** not confirmed, **30** removed, **40** no longer confirmable. Declaration: **10** submitted, **21** accepted, **22** accepted with errors, **101** not accepted, **102** rejected, **103** rejected after control, **100** annulled; other values in S7. Actuality (`DeclarationActualityStateCode`): **10** current, **11** current by correction, **20** not current; this is the signal that a declaration was replaced by a correction (S7) |
| IN-03 | Sodra | Inbound | true — feeds NP-SD2 | Sickness-certificate information for the employer. **NOT LOCATED as a machine channel:** DataService has no operation that returns sickness-certificate data to the employer (S3); the NP-SD2 instruction refers to electronic certificates and to *"Pranešimai draudėjui"* but not to a machine channel (S4 point 68) |
| IN-04 | VMI — EDS | Inbound (notice on OUT-03, OUT-04) | false — notice; triggers a correction (Section 5.2) | Errors found in a file uploaded or sent by web service are notified after processing to the contacts registered in EDS for the represented payer (S6 §26; S10). Deficiencies found on verification are notified on form FR1025 (S6 §27), and an information notice (*informacinis pranešimas*) requires a corrected return (S5, GPM313 rules §19.1, §20; GPM312 rules §64.1, §66). **NOT LOCATED as a machine channel** (G4) |

## 1.2 Inbound register — report spec, frequency and format

| ID | Related Report Spec | Frequency | File format / protocol |
|---|---|---|---|
| IN-01 | — (status of LT-SODRA-003 submissions; of NP-SD2 submissions only if G5 confirms DataService) | Per submission | SOAP 1.2 over HTTPS (S3) |
| IN-02 | — (status of LT-VMI-001 and LT-VMI-002 submissions) | Per submission | SOAP web service (S7) |
| IN-03 | — | Per certificate | **NOT LOCATED** |
| IN-04 | — (notices on LT-VMI-001 and LT-VMI-002 submissions) | Per event | E-mail or telephone to the EDS contacts (S6 §13, §26; S10); FR1025 notice (S6 §27). Machine-readable format **NOT LOCATED** (G4) |

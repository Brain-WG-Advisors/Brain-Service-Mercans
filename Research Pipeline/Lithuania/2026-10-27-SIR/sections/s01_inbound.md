# 1. Inbound Integrations

Three inbound flows are registered. IN-01 and IN-02 are the return legs of the outbound filings: the status of a document submitted to Sodra and the confirmation and declaration state of a file uploaded to VMI. IN-03 is the input to the leave integration: the sickness-certificate information the employer needs before it can file NP-SD2. No machine channel for IN-03 was located, and the row says so.

## 1.1 Inbound register — identification and mapping

| ID | Authority / System | Direction | Product Mapping Required | Description |
|---|---|---|---|---|
| IN-01 | Sodra — DataService | Inbound (response to OUT-01, OUT-02) | false — status only | `getDocumentStatus(docUID)` returns `docStatus` and a description: **NST** not submitted, **FNS** executed / accepted, **PRC** processing, **ARC** archived, **ERR** rejected for errors, **DRF** draft (S3 pages 9, 19-20) |
| IN-02 | VMI — EDSWebServiceUploadFile | Inbound (response to OUT-03, OUT-04) | false — status only | `CheckFileState(FileId)` returns the file confirmation state and the declaration state. Confirmation: **10** confirmed, **20** not confirmed, **30** removed, **40** no longer confirmable. Declaration: **10** submitted, **21** accepted, **22** accepted with errors, **101** not accepted, **102** rejected, **103** rejected after control, **100** annulled; other values in S7 |
| IN-03 | Sodra | Inbound | true — feeds NP-SD2 | Sickness-certificate information for the employer. **NOT LOCATED as a machine channel:** DataService has no operation that returns sickness-certificate data to the employer (S3); the NP-SD2 instruction refers to electronic certificates and to *"Pranešimai draudėjui"* but not to a machine channel (S4 point 68) |

## 1.2 Inbound register — report spec, frequency and format

| ID | Related Report Spec | Frequency | File format / protocol |
|---|---|---|---|
| IN-01 | — (status of LT-SODRA-003 and NP-SD2 submissions) | Per submission | SOAP 1.2 over HTTPS (S3) |
| IN-02 | — (status of LT-VMI-001 and LT-VMI-002 submissions) | Per submission | SOAP web service (S7) |
| IN-03 | — | Per certificate | **NOT LOCATED** |

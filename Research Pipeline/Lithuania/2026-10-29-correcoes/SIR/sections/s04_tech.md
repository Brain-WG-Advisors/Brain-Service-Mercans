# 4. Technical Specifications

## 4.1 Sodra — SAM and NP-SD2 (OUT-01, OUT-02)

Format: FFData XML built on the Sodra form definition (MXFD). SAM uses form version 07, file `sam-v07.mxfd` (S1). Sodra requires the files to follow its published data-structure description (S2); for SAM this is the data-structure description version 07 (S11): W3C XML 1.0, UTF-8 (S11 page 1).

**Channel A — EDAS account** (`draudejai.sodra.lt`): the notices must be filed through the employer account and signed with a qualified electronic signature; only the head of the company or an authorised person may sign (S2).

**Channel B — DataService web service:** business systems adapted to Sodra's requirements may prepare and submit the notices automatically; signed files must be transmitted through the public web service (S2). Two modes (S3 pages 5-8):

- **Draft mode:** `uploadEdasDraft` sends an unsigned FFDATA file and returns a `signingURL` and a `docUID`; a person then opens the link in EDAS to sign and submit it.
- **Signed mode:** `sendSignedDocument` sends an FFDATA file already signed with a qualified signature and returns a `docUID`.
- Files must be UTF-8 without BOM, sent as `base64Binary` with MTOM (S3 pages 5, 8). `getPossibleDocuments` returns the form codes and versions accepted (S3 page 10).

## 4.2 VMI — GPM313 and GPM312 (OUT-03, OUT-04)

Both returns are filed and amended only electronically through the VMI Electronic Declaration System (EDS) (S5, GPM313 rules §14; GPM312 rules §59). Format: FFData built on the VMI MXFD of each form; no XSD was located (S5; S7).

The EDS rules (VA-72, §21) give three ways to file once logged in: (1) the on-line form in the portal; (2) uploading a file prepared by accounting software, in the format of the published technical requirements, with the *"Persiųsti failą"* function; (3) confirming data transmitted through the web service (S6 §21).

**Web service `EDSWebServiceUploadFile`** (S7): `SubmitFile` sends the `.ffdata` file (or a zip with it) in Base64, with `AppName`, `UserName`, `Password` and `PersonCode` (the payer's code). Success code 900 states the date by which the file must be confirmed in EDS. The status is read back with `CheckFileState(FileId)`. The specification is version 2.01 of 2010; it is still the one offered on the current EDS page, and the published WSDL exposes the same two operations (S7).

**Mandatory human step:** within 3 days of the transmission, a user with the right to file must log in to EDS and confirm the declaration under *"Deklaravimas → Patvirtinti užpildytą formą"* (S8). If it is not confirmed within 3 days, it is deleted and the submission is not counted (S8); the success message of `SubmitFile` (code 900) gives the exact confirmation date (S7).

## 4.3 Side-by-side

| Item | Sodra DataService | VMI EDSWebServiceUploadFile |
|---|---|---|
| Protocol | SOAP 1.2 over HTTPS, document/literal, MTOM (S3 pages 4, 15) | SOAP 1.1 in the 2010 specification; the WSDL also offers SOAP 1.2 (S7) |
| Endpoint | `https://draudejai.sodra.lt/edas-external/services/DataService` (S3 page 15) | `https://deklaravimas.vmi.lt/EDSWebServiceUploadFile/EDSWebServiceUploadFile.asmx` in the 2010 specification; the WSDL published today shows `http://` in `soap:address` (S7) |
| Operations | `uploadEdasDraft`, `getDocumentLink`, `sendSignedDocument`, `getDocumentStatus`, `getPossibleDocuments` (S3) | `SubmitFile`, `CheckFileState` (S7) |
| Payload | FFDATA, UTF-8 without BOM, `base64Binary` (S3) | `.ffdata`, or `.zip` containing `.ffdata`, in Base64 (S7) |
| Form definitions | SAM: `sam-v07.mxfd`, form version 07 (S1) | `GPM313.mxfd` (created 2025-11-04, EDS file version 2025-12-31); `GPM312.mxfd` (created 2026-05-11, EDS file version 2026-06-12) (S5) |
| Documentation | Version 1.0, 2016-01-19 (S3) | Version 2.01, 2010 (S7) |

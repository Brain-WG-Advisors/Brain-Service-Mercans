# Appendix B. Open Gaps

Every cell in this register that reads **NOT LOCATED** is collected here, with the enquiry that would close it. A gap in this list is a known unknown with an owner, not an omission.

## 8.1 Gaps at an authority — closeable by direct inquiry

| # | Integration | What is missing | Category | Who to ask |
|---|---|---|---|---|
| G1 | IN-03 | A machine channel for sickness-certificate information from Sodra to the employer | Inbound channel | Sodra |
| G2 | OUT-01 to OUT-04 | An XSD for the FFData files; only the MXFD form definitions were found | Technical spec | Sodra; VMI |
| G3 | DataService, EDSWebServiceUploadFile | Test environments | Technical spec | Sodra; VMI |
| G4 | IN-04 | A machine-readable channel for VMI notices: errors sent to the EDS contacts (S6 §26), FR1025 deficiency notices (S6 §27) and information notices (*informacinis pranešimas*) | Inbound channel | VMI |
| G6 | OUT-03, OUT-04 | Whether the VMI filing date is the transmission date or the confirmation date of a web-service file | Deadline | VMI |
| G7 | EDS portal | Whether a foreign operator can log in to EDS and do the confirmation after 1 September 2026 | Authentication | VMI |
| G8 | EDSWebServiceUploadFile | Whether the 2010 limits still apply (200 files per day; 30-minute block after 5 wrong passwords; configurable, S7) and whether the endpoint is http or https (S7: specification https, WSDL http) | Technical spec | VMI |
| G9 | MXFD files | Endpoints that appear only as attributes in the MXFD files, without documentation: VMI `EDSMdocUploadService/MdocUploadService.svc` and `PublicServiceREST`; Sodra `AuthServiceWS` (S1, S5) | Technical spec | Sodra; VMI |
| G10 | OUT-01 | Correction of SAM: the SD rules in force (S13) set a PT electronic route (points 86-92; late SAM with reason code 01, points 52, 91.3.1) and a written route with a new SAM marked P35 (points 93-97). From 2010 onward data are corrected only electronically (S13 point 77.1.1), so the PT route is the one to automate. Not confirmed: whether DataService accepts PT requests (`getPossibleDocuments`) | Error handling | Sodra |
| G11 | S3, S7 | Whether the Sodra web-service documentation (2016) and the VMI one (2010) are the latest versions; both are the ones offered on the authorities' current pages (S2, S7) | Source currency | Sodra; VMI |
| G12 | OUT-01, OUT-02 | Any published response-time undertaking for DataService | SLA | Sodra |
| G14 | OUT-01 | The Sodra SAM content-validation catalogue (C23xx codes cited by A1): not archived, codes not re-checked against a Sodra original | Error handling | Sodra |

## 8.2 Open decisions and internal gaps

| # | Integration | What is missing | Category | Who to ask |
|---|---|---|---|---|
| G5 | OUT-02, IN-01 | A Mercans Report Specification for NP-SD2, to be created if the leave integration confirms it; whether DataService accepts NP-SD2 (`getPossibleDocuments`). Until this is confirmed, IN-01 is not the return leg of OUT-02 | Report spec / channel | Mercans Compliance; Sodra |
| G13 | Leave integration | Scope decision pending: whether the 9-SD notice is part of the leave integration, decided together with that integration. If yes, it needs an outbound row, a Report Specification and its channel check | Scope | Mercans Compliance; client |
| G16 | S2, S3 | Sodra originals not archived: the S2 page and the DataService instruction (S3) were read in a browser and are held as extracts only. Archived: the V-243 rules behind S1 and S4 (S13) and, on 30 October 2026, `sam-v07.mxfd` (form definition created 2025-12-31). To close: save the DataService PDF and the S2 page with checksums | Source archiving | Mercans Compliance |

## 8.3 What this register does not claim

- It does not claim any authority response-time commitment other than the VMI 3-day confirmation window and the 5-working-day non-acceptance notice.
- It does not claim that any channel was tested: no login and no call to a production endpoint was made.
- It does not claim that DataService accepts PT requests (G10), or the SAM validation catalogue (G14) beyond what A1 records.

## 8.4 Gaps closed in version 1.2

- G15 (non-working-day deadline): closed. SAM and other SD notices: S13 point 125. GPM313 and GPM312: S14 art. 162(6). See Section 6.1.

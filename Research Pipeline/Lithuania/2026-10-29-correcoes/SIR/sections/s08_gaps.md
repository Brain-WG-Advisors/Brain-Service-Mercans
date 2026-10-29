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
| G10 | OUT-01 | Late filing and correction of SAM: the SAM data-structure description has a revised-notice flag (S11); the 2015 text of the SD rules used PT annexes (S12); A1 records PT annexes and PT reason code 01 for late data. The SD rules in force today were not available, so the current route is not confirmed | Error handling | Sodra |
| G11 | S3, S7 | Whether the Sodra web-service documentation (2016) and the VMI one (2010) are the latest versions; both are the ones offered on the authorities' current pages (S2, S7) | Source currency | Sodra; VMI |
| G12 | OUT-01, OUT-02 | Any published response-time undertaking for DataService | SLA | Sodra |
| G14 | OUT-01 | The Sodra SAM content-validation catalogue (C23xx codes cited by A1): not archived, codes not re-checked against a Sodra original | Error handling | Sodra |
| G15 | OUT-01, OUT-03, OUT-04 | Whether a filing deadline that falls on a non-working day moves to the next working day; the rule is not in the sources read (VMI instructions, SAM instruction), and the general rule (Law on Tax Administration; general SD notice rules) was not available | Deadline | VMI; Sodra |

## 8.2 Open decisions and internal gaps

| # | Integration | What is missing | Category | Who to ask |
|---|---|---|---|---|
| G5 | OUT-02, IN-01 | A Mercans Report Specification for NP-SD2, to be created if the leave integration confirms it; whether DataService accepts NP-SD2 (`getPossibleDocuments`). Until this is confirmed, IN-01 is not the return leg of OUT-02 | Report spec / channel | Mercans Compliance; Sodra |
| G13 | Leave integration | Scope decision pending: whether the 9-SD notice is part of the leave integration, decided together with that integration. If yes, it needs an outbound row, a Report Specification and its channel check | Scope | Mercans Compliance; client |
| G16 | S1 to S4 | Sodra originals not archived: the pages and the DataService instruction were read in a browser and are held as extracts only. To close: save the DataService PDF, `sam-v07.mxfd` and the S2 and S4 pages with checksums | Source archiving | Mercans Compliance |

## 8.3 What this register does not claim

- It does not claim any authority response-time commitment other than the VMI 3-day confirmation window and the 5-working-day non-acceptance notice.
- It does not claim that any channel was tested: no login and no call to a production endpoint was made.
- It does not claim the current Sodra correction route for SAM (G10) or the SAM validation catalogue (G14) beyond what A1 records.
- It does not claim a next-working-day shift for the SAM, GPM313 or GPM312 deadlines (G15).

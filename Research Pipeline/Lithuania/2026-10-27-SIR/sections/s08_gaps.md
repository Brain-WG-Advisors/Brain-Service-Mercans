# 8. Open Gaps

Every cell in this register that reads **NOT LOCATED** is collected here, with the enquiry that would close it. A gap in this list is a known unknown with an owner, not an omission.

| # | Integration | What is missing | Category | Who to ask |
|---|---|---|---|---|
| G1 | IN-03 | A machine channel for sickness-certificate information from Sodra to the employer | Inbound channel | Sodra |
| G2 | OUT-01 to OUT-04 | An XSD for the FFData files; only the MXFD form definitions were found | Technical spec | Sodra; VMI |
| G3 | DataService, EDSWebServiceUploadFile | Test environments | Technical spec | Sodra; VMI |
| G4 | VMI | A machine-readable channel for VMI notices (*informacinis pranešimas*, FR1025) | Inbound channel | VMI |
| G5 | OUT-02 | A Mercans Report Specification for NP-SD2, to be created if the leave integration is confirmed in scope; whether DataService accepts NP-SD2 (`getPossibleDocuments`) | Report spec / channel | Mercans Compliance; Sodra |
| G6 | OUT-03, OUT-04 | Whether the VMI filing date is the transmission date or the confirmation date of a web-service file | Deadline | VMI |
| G7 | EDS portal | Whether a foreign operator can log in to EDS and do the confirmation after 1 September 2026 | Authentication | VMI |
| G8 | EDSWebServiceUploadFile | Whether the 2010 limits still apply (200 files per day; 30-minute block after 5 wrong passwords; configurable, S7) and whether the endpoint is http or https (S7: specification https, WSDL http) | Technical spec | VMI |
| G9 | MXFD files | Endpoints that appear only as attributes in the MXFD files, without documentation: VMI `EDSMdocUploadService/MdocUploadService.svc` and `PublicServiceREST`; Sodra `AuthServiceWS` (S1, S5) | Technical spec | Sodra; VMI |
| G10 | OUT-01 | Late filing and correction of SAM: the SAM spec LT-SODRA-003 records a PT request for late data; not re-checked against the source in this register | Error handling | Sodra |
| G11 | S3, S7 | Whether the Sodra web-service documentation (2016) and the VMI one (2010) are the latest versions; both are the ones offered on the authorities' current pages (S2, S7) | Source currency | Sodra; VMI |
| G12 | OUT-01, OUT-02 | Any published response-time undertaking for DataService | SLA | Sodra |

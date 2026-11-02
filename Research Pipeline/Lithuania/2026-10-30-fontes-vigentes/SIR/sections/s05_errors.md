# 5. Error Handling

## 5.1 Sodra

| Situation | Model | Source |
|---|---|---|
| DataService call fails | Error codes **WSDATA-0 to WSDATA-9**: system error, user not found, wrong credentials, service blocked, no document, draft not saved, invalid signature, document not saved, document not found, action not allowed | S3 page 20 |
| Document rejected after submission | `getDocumentStatus` returns **ERR** (IN-01) | S3 pages 19-20 |
| SAM content validation | Sodra validates SAM content with error codes of the **C23xx** series. The SAM Report Specification cites them field by field from the Sodra validation catalogue (for example C2330 annex flag, C2336 registration number, C2338 and C2347 person counts, C2344 contribution identity). The catalogue itself is not archived and the codes were not re-checked against a Sodra original in this register (G14) | A1 |
| Correction of filed SAM data | The SD rules in force (S13) provide two routes. Electronic: a PT request through EDAS, filed without delay when the employer finds incorrect data or files late (points 87, 88), with the annex PT-SAM3SD, PT-SAM3SD-M (whole calendar year) or PT-SAM3SDP (points 86.6-86.8); a late SAM needs a PT request with reason code 01 (points 52, 91.3.1). Written: a written request with a new SAM marked 'x' in P35 (*"Patikslintas pranešimas"*), the corrected year and month in P14T and P17T, and only the insured persons whose data change (points 93-95; S11 page 10). From 2010 onward data are corrected only electronically (S13 point 77.1.1), so an employer system automates the PT route; whether DataService accepts PT requests is open (G10) | S11 page 10; S13 points 52, 77.1.1, 86.6-86.8, 87, 88, 91.3.1, 93-95; A1 |
| Error found in a filed NP-SD2 | Corrected at once through a **PT** request with the **PT-NP-SD2** annex | S4 point 76 |

## 5.2 VMI

| Situation | Model | Source |
|---|---|---|
| `SubmitFile` fails | Error codes **000 to 501**; success code **900** | S7 |
| `CheckFileState` fails | Error codes **600 to 613**; success code **901** | S7 |
| Declaration technically not accepted | VMI informs the taxpayer or the EDS user through ICT at once and within **5 working days** at the latest. For an on-line form the errors are shown at submission; for a file upload or a web-service file they are sent **after processing to the contacts registered in EDS** (IN-04; Section 3.2) | S6 §26; S10 |
| Deficiencies found on verification | Notice on form FR1025, stating how and by when the deficiencies must be rectified (IN-04) | S6 §27 |
| Correction of a filed return | A complete new return is filed for the same period. It must be filed on receipt of an information notice, within the term stated in the notice (GPM313 rules §19.1, §20; GPM312 rules §64.1, §66). Correcting in GPM312 amounts already declared in GPM313 requires the GPM313 of that month to be corrected too (GPM312 rules §65). The current actuality of a declaration is read with `CheckFileState` (IN-02) | S5, GPM313 rules §18-§20; GPM312 rules §63-§66; S7 |
| Annulment of a filed return | Only in the EDS portal (*"Deklaravimas → Pateikti dokumentai ir formos → Pateiktos formos"*, button *"Anuliuoti"*), sometimes subject to approval by a VMI officer. The web service has no annulment operation: its only operations are `SubmitFile` and `CheckFileState` | S10; S7 |

## 5.3 Summary — where an error model exists and where it does not

| Integration | Error model | Gap |
|---|---|---|
| OUT-01 SAM | Channel errors WSDATA-0 to WSDATA-9 and status ERR (S3); content validation codes C23xx as cited by A1; correction through PT annexes (electronic) or a new SAM with P35 (written), S13 points 86-95; from 2010 only the electronic PT route applies (S13 point 77.1.1); DataService acceptance of PT open | G10, G14 |
| OUT-02 NP-SD2 | Correction by PT with the PT-NP-SD2 annex (S4 point 76); DataService codes and status only if DataService accepts NP-SD2 | G5 |
| OUT-03, OUT-04 GPM313, GPM312 | `SubmitFile` codes 000 to 501, `CheckFileState` codes 600 to 613 (S7); errors after processing to the EDS contacts (S6 §26); FR1025 deficiency notice (S6 §27); correction by a complete new return; annulment only in the EDS portal | G4 (no machine-readable notices) |
| IN-03 | No channel and no error model | G1 |

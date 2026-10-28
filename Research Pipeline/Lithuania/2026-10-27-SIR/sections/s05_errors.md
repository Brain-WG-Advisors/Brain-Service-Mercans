# 5. Error Handling

## 5.1 Sodra

| Situation | Model | Source |
|---|---|---|
| DataService call fails | Error codes **WSDATA-0 to WSDATA-9**: system error, user not found, wrong credentials, service blocked, no document, draft not saved, invalid signature, document not saved, document not found, action not allowed | S3 page 20 |
| Document rejected after submission | `getDocumentStatus` returns **ERR** (IN-01) | S3 pages 19-20 |
| Error found in a filed NP-SD2 | Corrected at once through a **PT** request with the **PT-NP-SD2** annex | S4 point 76 |

## 5.2 VMI

| Situation | Model | Source |
|---|---|---|
| `SubmitFile` fails | Error codes **000 to 501**; success code **900** | S7 |
| `CheckFileState` fails | Error codes **600 to 613**; success code **901** | S7 |
| Declaration technically not accepted | VMI notifies electronically, at once and within **5 working days** at the latest | S6 §26 |
| Correction of a filed return | A complete new return is filed for the same period | S5, GPM313 rules §18; GPM312 rules §63 |

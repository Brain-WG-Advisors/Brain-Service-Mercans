# 2. Outbound Integrations

Four outbound flows are registered: the monthly SAM and the NP-SD2 benefit data to Sodra, and the monthly GPM313 and annual GPM312 income tax returns to VMI.

Where a channel returns a status, the inbound leg is registered separately in Section 1 so that it can be scheduled and monitored on its own: IN-01 for Sodra and IN-02 for VMI.

## 2.1 Outbound register — identification and mapping

| ID | Authority / System | Direction | Product Mapping Required | Description |
|---|---|---|---|---|
| OUT-01 | Sodra (State Social Insurance Fund Board) | Outbound; return leg IN-01 | true — payroll fields to SAM boxes | **SAM** with annexes **SAM3SD** and **SAM3SDP**: monthly contributions per insured person (S1) |
| OUT-02 | Sodra | Outbound; return leg IN-01 | true — absence and pay data to NP-SD2 fields | **NP-SD2**: data for sickness and maternity benefit — the leave integration (S4) |
| OUT-03 | VMI (State Tax Inspectorate) | Outbound; return leg IN-02 | true — payroll fields to GPM313 boxes | **GPM313**: monthly income tax return (S5) |
| OUT-04 | VMI | Outbound; return leg IN-02 | true — payroll fields and income codes to GPM312 fields | **GPM312** with annexes **GPM312L** and **GPM312U**: annual income tax return (S5) |

## 2.2 Outbound register — frequency and format

| ID | Frequency | File format / protocol |
|---|---|---|
| OUT-01 | Monthly, by the **15th of the following month** (S1 point 52) | FFData XML built on the Sodra form definition `sam-v07.mxfd`, form version 07 (S1). Channels: EDAS account (on-line form or FFData file) or the DataService web service (S2, S3) |
| OUT-02 | Sickness: after the end of the incapacity, or for each completed period of at least 14 days when it lasts longer; at least twice a month, by the 15th and the last day of the month (next working day if that day is not a working day). Maternity: within **5 working days** of the employee's request (S4 points 57, 59) | FFData. Channel: EDAS account — S2 lists NP-SD2 among the SD notices that must be filed through the employer account. Whether DataService accepts NP-SD2 is shown only by `getPossibleDocuments` (Section 8) |
| OUT-03 | Monthly, by the **15th of the following month** (S5, GPM313 rules §12) | FFData built on `GPM313.mxfd`. Channels: EDS on-line form, file upload (*"Persiųsti failą"*), or the web service `EDSWebServiceUploadFile` (S6 §21; S7) |
| OUT-04 | Annual, by **15 February** of the following year (S5, GPM312 rules §57) | FFData built on `GPM312.mxfd`. Same channels as OUT-03 |

## 2.3 Related Report Spec — all outbound integrations

| ID | Related Report Spec |
|---|---|
| OUT-01 | LT-SODRA-003-SAM-Spec v1.0 |
| OUT-02 | **No Mercans Report Specification yet** — to be created if the leave integration is confirmed in scope (Section 8) |
| OUT-03 | LT-VMI-001-GPM313-Spec v1.1 |
| OUT-04 | LT-VMI-002-GPM312-Spec v1.1 |

## 2.4 Registered, but not an integration in this register

| Item | Source | Why it is not registered as an integration here |
|---|---|---|
| Other Sodra SD notices: 1-SD, 2-SD, 9-SD, 12-SD, 13-SD | S2 | They use the same Sodra channel as OUT-01 and OUT-02 (S2) but are outside the report set of this document. No Mercans Report Specification exists for them yet |

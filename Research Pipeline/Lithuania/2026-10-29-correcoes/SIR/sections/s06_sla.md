# 6. SLA and Deadlines

Two different things are held in this section and they must not be conflated. **Filing deadlines** are statutory and are restated here so that the register is usable on its own. **Response times** are what the authority undertakes to give back.

## 6.1 Filing deadlines

| ID | Obligation | Periodicity | Deadline | Source |
|---|---|---|---|---|
| OUT-01 | SAM | Monthly | 15th of the following month | S1 point 52 |
| OUT-02 | NP-SD2 — sickness | Per incapacity | After the end of the incapacity, or for each completed period of at least 14 days; at least twice a month, by the 15th and the last day of the month (next working day if that day is not a working day) | S4 points 57, 59 |
| OUT-02 | NP-SD2 — maternity | Per request | Within 5 working days of the employee's request | S4 point 59 |
| OUT-03 | GPM313 | Monthly | 15th of the following month | S5, GPM313 rules §12 |
| OUT-03 | GPM313 — part period | On bankruptcy, restructuring, liquidation or reorganisation | Within 30 days of the start of bankruptcy or restructuring, for the month up to that date; on liquidation or reorganisation, before the end of activity | S5, GPM313 rules §16, §17 |
| OUT-04 | GPM312 | Annual | 15 February of the following year | S5, GPM312 rules §57 |
| OUT-04 | GPM312 — part period | On bankruptcy, restructuring, liquidation or reorganisation | Within 30 days of the start of bankruptcy or restructuring, for the year up to that date; on liquidation or reorganisation, before the end of activity | S5, GPM312 rules §61, §62 |

The VMI instructions and the SAM instruction state the deadline as a calendar day. Whether a deadline that falls on a non-working day moves to the next working day for OUT-01, OUT-03 and OUT-04 is not stated in the sources read for this register (G15); only the NP-SD2 instruction states it (S4 point 57).

## 6.2 Response times and confirmation windows

| Integration | Published time | Source |
|---|---|---|
| OUT-03, OUT-04 via web service | The upload must be confirmed in EDS within **3 days**, or it is deleted and not counted | S8 |
| OUT-03, OUT-04 | Technical non-acceptance is notified at once and within **5 working days** at the latest; for uploads and web-service files, after processing, to the EDS contacts (IN-04) | S6 §26 |
| OUT-01, OUT-02 | **NOT LOCATED** — no response-time undertaking was found in the DataService instruction | S3 |

No source states whether the VMI filing date is the transmission date or the confirmation date (S6 §24 only says it is set by the EDS software), so web-service files should be confirmed well before the deadline (G6).

## 6.3 Correction windows

| Integration | Window | Source |
|---|---|---|
| OUT-03, OUT-04 web-service file | A file not confirmed in EDS within 3 days is deleted and must be sent again | S8 |
| OUT-03, OUT-04 corrected return | On an information notice: within the term stated in the notice. On the payer's own initiative: GPM313 rules §20 refers to the terms of the Law on Tax Administration, which was not read for this register | S5, GPM313 rules §20; GPM312 rules §66 |
| OUT-02 NP-SD2 | An error is corrected at once by a PT request with the PT-NP-SD2 annex | S4 point 76 |
| OUT-01 SAM | Not established: current correction route open (G10) | S11; S12 |

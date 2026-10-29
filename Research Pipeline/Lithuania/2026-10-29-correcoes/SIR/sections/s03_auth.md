# 3. Authentication Requirements

Every statement in this section and the three that follow is cited to the authority's own documentation, listed in Appendix A. Where a search returned nothing, the cell says so.

The single most important finding for Lithuania is that **the VMI web service never completes a filing on its own.** A person with filing rights must log in to EDS and confirm each uploaded declaration within 3 days (S8). Sodra, by contrast, accepts a file already signed with a qualified signature through DataService (S3).

## 3.1 Sodra channels

| Channel | Identification of the caller | Signature | Who | Source |
|---|---|---|---|---|
| EDAS account | Login via `draudejai.sodra.lt`, e-banking or `epaslaugos.lt` | Qualified electronic signature on every notice | The head of the company or an authorised person signs | S2 |
| DataService web service | WS-Security UsernameToken: the EDAS user name and a service password set in EDAS (*"Naudotojo nustatymai"*; 10 to 14 characters, at least 1 special character and 1 digit). Five failed attempts in a row block the service | Draft mode: none (a person signs in EDAS). Signed mode: the FFDATA file is already signed with a qualified signature | An EDAS user who has enabled the service in the EDAS user settings | S3 page 4 |

## 3.2 VMI channels

| Channel | Identification of the caller | Who | Source |
|---|---|---|---|
| EDS portal | From **1 September 2026**, login only through the e-government gateway means (S9 news). The EDS help page says a foreign person without VMI registration can request VMI access means (the request is not needed with a Lithuanian residence permit) or declare a qualified e-signature certificate issued in Lithuania; whether this still works after 1 September is not stated (G7) | Representatives with EDS representation rights for the payer | S9; S6 §7; S8 |
| EDSWebServiceUploadFile | A separate user name and password created in EDS (*"Nustatymai → Mano duomenys"*). Only representatives of a legal-entity taxpayer can enable it; the user must have the right to file for the `PersonCode` | The software, plus an EDS user who confirms within 3 days | S7; S8 |
| EDS contact details (error notices) | Errors in a file uploaded or sent by web service are notified after processing to the contacts (e-mail, telephone) registered in EDS for the represented payer, under *"NUSTATYMAI → Atstovavimas → Atstovaujamas asmuo → Atstovaujamo mokesčių mokėtojo ryšio priemonės"*. If no valid contact is registered, VMI may use the payer's contacts held in other VMI systems | Recommended: register a monitored mailbox there for each payer, so that error notices reach the team that files | S6 §13, §14, §26; S10 |

## 3.3 Per-integration authentication lookup

| ID | Authentication mechanism |
|---|---|
| OUT-01 / IN-01 SAM | EDAS account (login via `draudejai.sodra.lt`, e-banking or `epaslaugos.lt`) with a qualified signature on the notice; or DataService with UsernameToken (EDAS user name and service password) and, in signed mode, a qualified signature on the file (S2; S3 page 4) |
| OUT-02 / IN-01 NP-SD2 | EDAS account with a qualified signature (S2). DataService only if it accepts NP-SD2 (G5) |
| IN-03 sickness-certificate information | **NOT LOCATED** (G1) |
| OUT-03, OUT-04 / IN-02 GPM313, GPM312 | EDS portal login through the e-government gateway means (S9); web service with the separate EDS user name and password, plus a confirming EDS user with representation rights for the payer (S6 §7; S7; S8) |
| IN-04 VMI notices | No caller authentication: VMI writes to the EDS contacts of the payer (S6 §26; S10) |

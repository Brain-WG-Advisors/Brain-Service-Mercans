# 3. Authentication Requirements

Every statement in this section and the three that follow is cited to the authority's own documentation, listed in Section 7. Where a search returned nothing, the cell says so.

The single most important finding for Lithuania is that **the VMI web service never completes a filing on its own.** A person with filing rights must log in to EDS and confirm each uploaded declaration within 3 days (S8). Sodra, by contrast, accepts a file already signed with a qualified signature through DataService (S3).

## 3.1 Sodra channels

| Channel | Identification of the caller | Signature | Who | Source |
|---|---|---|---|---|
| EDAS account | Login via `draudejai.sodra.lt`, e-banking or `epaslaugos.lt` | Qualified electronic signature on every notice | The head of the company or an authorised person signs | S2 |
| DataService web service | WS-Security UsernameToken: the EDAS user name and a service password set in EDAS (*"Naudotojo nustatymai"*; 10 to 14 characters, at least 1 special character and 1 digit). Five failed attempts in a row block the service | Draft mode: none (a person signs in EDAS). Signed mode: the FFDATA file is already signed with a qualified signature | Any EDAS user who has enabled the service | S3 page 4 |

## 3.2 VMI channels

| Channel | Identification of the caller | Who | Source |
|---|---|---|---|
| EDS portal | From **1 September 2026**, login only through the e-government gateway means (S9 news). The EDS help page says a foreign person without VMI registration can request VMI access means or declare a qualified electronic-signature certificate issued in Lithuania (not needed with a Lithuanian residence permit); whether this still works after 1 September is not stated (Section 8) | Representatives with filing rights for the payer | S9 |
| EDSWebServiceUploadFile | A separate user name and password created in EDS (*"Nustatymai → Mano duomenys"*). Only representatives of a legal-entity taxpayer can enable it; the user must have the right to file for the `PersonCode` | The software, plus an EDS user who confirms within 3 days | S7; S8 |

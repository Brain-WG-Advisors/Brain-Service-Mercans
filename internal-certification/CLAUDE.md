# Internal Certification – Reports (Mercans) — context for this folder

Read this file before doing anything in this folder.

**Linked to the Brain-Service** (since 2026-10-15): this folder is front 5 "Certificação" of
`C:\Users\instituto\Documents\brain-service`. Open the work from `brain-service\frentes\certificacao` (or
`scripts\abrir_frentes.ps1 -Frentes Certificacao`); state lives in `frentes\certificacao\estado.md`, method/lessons in
`servicos\analise-reports.md`, per-country findings in the "Internal Certification" section of `paises\<País>.md`.
Employee data stays here; only country, client, period, finding and legal basis go to the brain.

## How to work with Wallisson
- Wallisson Gomes, Compliance Regulations Team Lead at Mercans (product: HRBLIZZ). Talk to him in Brazilian Portuguese;
  anything sent to colleagues goes in English.
- Short, direct answers. Check every record, never a sample. Use official primary sources only, and confirm each schema,
  table or rate is the version in force. Mark an inference as an inference.
- Solve only what was asked. Report other findings; do not act on them.
- Never send a message, email or file on Wallisson's behalf without his explicit approval of that specific send.
  Prepare it as a draft and wait for "Aprovado para envio".

## Goal
Validate the statutory reports HRBLIZZ produces for clients in 12 countries, using the files the Primary SBCs send.
We validate and report; we do not regenerate filings. Findings go back to implementation/dev; Compliance confirms the
statutory position, it does not prescribe configuration.

## Folder structure
```
Internal Certification - Reports/
└── <Country>/
    └── <Client> - <YYYY-MM>/
        ├── 01 Received/     files exactly as received (never rename or edit) + received.txt: who, channel, date, files
        └── 02 Validation/   our outputs: findings workbook and evidence
```
Files that arrive later go into the 01 Received folder of the period they belong to.

## Contacts and status (07-Oct-2026)
Source: monday.com board 2072701698 "BAU Master Client List", column Primary SBC, active clients only.
Email sent 07-Oct 14:23 to all 9 SBCs, cc Manju Shetija and Marko Taylor. Individual requests sent on Google Chat ~14:03.

| Country | Primary SBC | Email | Status |
|---|---|---|---|
| Denmark | Rakshitha Nagesh | rnagesh@mercans.com | No reply |
| Norway, Netherlands | Umesh Gaikwad | ugaikwad@mercans.com | Asked "all clients or one random client per country?" Draft reply in Chat (one client per country, most recent closed period) awaiting approval |
| Finland, Estonia, Norway | Marju Martinson | mmartinson@mercans.com | No reply. Her Norway client (reMarkable) is still in Implementation |
| Netherlands, Sweden | Athul Satheesh | asatheesh@mercans.com | No reply |
| Netherlands | Suresh Jalihal | sjalihal@mercans.com | Asked which entity and what "authority receipt" means. Draft reply awaiting approval. His client Delrin is a Special Project |
| United Kingdom | Srikanth Kondam | skondam@mercans.com | Sent `Sept26_MMCL UK reprots.zip` (McDermott UK, Sept 2026, closed payroll) on Chat 14:23. Draft thank-you awaiting approval |
| United Kingdom | Christina Surpogi | csurpogi@mercans.com | Said she would send in a few minutes; nothing received yet |
| Ukraine | Nataliia Hahan | nahahan@mercans.com | Sent Altium files on Chat (see below). Asked chat or email; draft reply (chat is fine; asks for August GL, bank file, master data, receipts) awaiting approval |
| Russia, Azerbaijan, Kazakhstan | Sadaf Nishat | snishat@mercans.com | No reply |
| Ireland | none | — | No Primary SBC on the board |

Nataliia's files seen on Chat (check the chat for the full list): September 2026 `Altium_Balance_09-2026_UKR.xls`,
[[internal-certification/Ukraine/Altium - 2026-09/01 Received/Altium_Balance_09-2026_GTN.xlsx|Altium_Balance_09-2026_GTN.xlsx]]; August 2026 `Application_PF_08.xls`, [[internal-certification/Ukraine/Altium - 2026-08/01 Received/Altium_Balance_08-2026_GTN_2.xlsx|Altium_Balance_08-2026_GTN_2.xlsx]],
`Altium_Balance_08-2026_Termination.xls`, [[internal-certification/Ukraine/Altium - 2026-08/01 Received/Altium_Balance_08-2026_UKR_2.xlsx|Altium_Balance_08-2026_UKR_2.xlsx]], `Altium_Unified PIT and SSC report…`,
`Altium_1PV_monthly_08_2026.zip`, `Altium_payslips_08.zip`. She said the September tax report is not prepared yet,
so the August set is the complete one. The Ukrainian G2N is in Ukrainian on purpose (printed and kept for 5 years).

## Files requested from each SBC
Latest closed pay period, all from the same payroll run: statutory report(s) as submitted + authority receipt, G2N,
payslips, GL, bank file, employee master data (+ the previous report if the report carries corrections).

## How to validate (per country / client / period)
Model: the Netherlands validation (skill `nl-payroll-validator`). For Netherlands packs, use that skill directly.
1. Establish the period and year. Load the official references for that year (report schema or field specification,
   code lists, tax tables, rates), downloaded from the authority and confirmed in force.
2. Format: the report against the official schema/field specification, every field, every record.
3. Content against the run: every employee and amount in the report ties to the G2N and the payslips.
   The payslip is the anchor; two files agreeing is not proof that either is right.
4. Statutory recalculation: tax and social contributions per employee with the official tables and rates.
5. Cross-document: G2N net = bank file = payment report = GL net account; GL debit = credit; payslip cumulatives roll forward.
6. Authority consistency rules. Use an authority test service only with Wallisson's OK (credentials, data protection).
7. Output workbook in `02 Validation`: Cover, Executive Summary (qualified, never "all correct"), Assumptions,
   Findings Register (ID, severity, area, finding, evidence, impact, statutory basis, status), Coverage, Reconciliation,
   Not Tested (reason and what would unblock it), Sources. Every check ends as Pass, Finding, Not tested or Out of scope.

Country references: start from the `payroll-compliance-<country>` skills (Denmark, Norway, Finland, Netherlands,
Estonia, United Kingdom, Sweden, Ireland), but always confirm against the official source in force. Ukraine: the Mercans
project artifacts. Russia, Azerbaijan, Kazakhstan: no base yet, research the official sources first.

## Collecting files from Google Chat
Use Claude in Chrome: Gmail > Chat > the direct message with the SBC. Download the attachments into the right
`01 Received` folder and log who sent them and when in `received.txt`.

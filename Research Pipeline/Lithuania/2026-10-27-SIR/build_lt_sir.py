# Builds LT-SIR-001-v1.0.docx (Statutory Integration Requirements, Lithuania).
# Every statement cites a source key (S1-S9, section 8).
import docx
from docx.shared import Pt, RGBColor
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

D = docx.Document()
st = D.styles['Normal']; st.font.name = 'Arial'; st.font.size = Pt(10)


def shade(cell, hexc):
    tcPr = cell._tc.get_or_add_tcPr(); s = OxmlElement('w:shd')
    s.set(qn('w:val'), 'clear'); s.set(qn('w:color'), 'auto'); s.set(qn('w:fill'), hexc); tcPr.append(s)


def table(head, rows):
    t = D.add_table(rows=1, cols=len(head)); t.style = 'Table Grid'
    for i, h in enumerate(head):
        c = t.rows[0].cells[i]; c.text = ''
        r = c.paragraphs[0].add_run(h); r.bold = True; r.font.color.rgb = RGBColor(255, 255, 255); shade(c, '4472C4')
    for row in rows:
        cs = t.add_row().cells
        for i, v in enumerate(row):
            cs[i].text = str(v)
    D.add_paragraph()


def H(t, l=1):
    D.add_heading(t, l)


def P(t):
    D.add_paragraph(t)


def B(t):
    D.add_paragraph(t, style='List Bullet')


D.add_heading('Lithuania — Statutory Integration Requirements (SIR)', 0)
P('Document ID: LT-SIR-001 · Version 1.0 (draft) · Date: 2026-10-27 · Audience: Configuration team')

H('Document Control')
table(['Version', 'Date', 'Author', 'Change'], [
    ['1.0', '2026-10-27', 'Mercans Global Compliance',
     "Initial version: integration landscape for Sodra and VMI payroll filings (SAM, NP-SD2, GPM313, GPM312), built from the authorities' current published sources."]])

H('0. Purpose, scope and source discipline')
P('Purpose: describe how the payroll system exchanges statutory payroll data with the Lithuanian authorities, so that the '
  'Configuration team can set up the submissions. Calculation rules are out of scope (see the CCG 2026, WTC and DD); '
  'field-level layouts are in the report specs LT-SODRA-003 (SAM), LT-VMI-001 (GPM313) and LT-VMI-002 (GPM312).')
P('Scope: the two integrations named for the Accenture Lithuania implementation: statutory filing (Sodra and VMI) and '
  'leave (sickness and maternity data sent to Sodra on NP-SD2).')
P('Source discipline: every statement cites a source key from section 8 (S1-S9). Anything not found in an official source '
  'is marked NOT LOCATED and listed in section 7. Nothing was tested against the live services: no login and no calls to '
  'production endpoints.')

H('1. Integration register')
table(['ID', 'Authority', 'Report / data', 'Direction', 'Frequency / deadline', 'Channels available', 'Spec'], [
    ['OUT-01', 'Sodra (State Social Insurance Fund Board)', 'SAM with annexes SAM3SD and SAM3SDP: monthly contributions per insured person',
     'Outbound', 'Monthly, by the 15th of the following month (S1 point 52)',
     'EDAS account: on-line form or FFData file; DataService web service (S2, S3)', 'LT-SODRA-003 v1.0'],
    ['OUT-02', 'Sodra', 'NP-SD2: data for sickness and maternity benefit (the "leave integration")', 'Outbound',
     "Sickness: after the end of the incapacity, or for each completed period of at least 14 days when it lasts longer; at least twice a month, by the 15th and the last day of the month (next working day if that day is not a working day). Maternity: within 5 working days of the employee's request (S4 points 57, 59)",
     'EDAS account (S2 lists NP-SD2 among the SD notices that must be filed through the employer account). Whether DataService accepts NP-SD2 is shown only by getPossibleDocuments (see 7)', 'No Mercans spec yet (see 7)'],
    ['OUT-03', 'VMI (State Tax Inspectorate)', 'GPM313: monthly income tax return', 'Outbound',
     'Monthly, by the 15th of the following month (S5, GPM313 rules §12)',
     'EDS: on-line form, file upload ("Persiųsti failą"), web service EDSWebServiceUploadFile (S6 §21; S7)', 'LT-VMI-001 v1.1'],
    ['OUT-04', 'VMI', 'GPM312 with annexes GPM312L and GPM312U: annual income tax return', 'Outbound',
     'Annual, by 15 February of the following year (S5, GPM312 rules §57)', 'Same as OUT-03', 'LT-VMI-002 v1.1'],
    ['IN-01', 'Sodra', 'Status of submitted documents', 'Inbound (response)', 'Per submission', 'DataService getDocumentStatus (S3)', '-'],
    ['IN-02', 'VMI', 'Confirmation and declaration status of uploaded files', 'Inbound (response)', 'Per submission',
     'Web service CheckFileState (S7)', '-'],
    ['IN-03', 'Sodra', 'Sickness-certificate information for the employer (input to NP-SD2)', 'Inbound', 'Per certificate',
     'NOT LOCATED as a machine channel: DataService has no operation that returns sickness-certificate data to the employer (S3); see 7', '-']])
P('Other SD notices (1-SD, 2-SD, 9-SD, 12-SD, 13-SD) use the same Sodra channel (S2) but are outside the report set of this document.')

H('2. Outbound integrations: how each filing reaches the authority')
H('2.1 Sodra: SAM and NP-SD2 (OUT-01, OUT-02)', 2)
P('Format: FFData XML built on the Sodra form definition (MXFD). SAM uses form version 07, file sam-v07.mxfd (S1). '
  "Sodra requires the files to follow its published data-structure description (S2).")
P('Channel A, EDAS account (draudejai.sodra.lt): the notices must be filed through the employer account and signed with a '
  'qualified electronic signature; only the head of the company or an authorised person may sign (S2).')
P("Channel B, DataService web service: business systems adapted to Sodra's requirements may prepare and submit the notices "
  'automatically; signed files must be transmitted through the public web service (S2). Two modes (S3 pages 5-8):')
B('Draft mode: uploadEdasDraft sends an unsigned FFDATA file and returns a signingURL and a docUID; a person then opens the link in EDAS to sign and submit it.')
B('Signed mode: sendSignedDocument sends an FFDATA file already signed with a qualified signature and starts registration; it returns a docUID.')
B('Files must be UTF-8 without BOM, sent as base64Binary with MTOM (S3 pages 5, 8). getPossibleDocuments returns the form codes and versions accepted (S3 page 10).')

H('2.2 VMI: GPM313 and GPM312 (OUT-03, OUT-04)', 2)
P('Both returns are filed and amended only electronically through the VMI Electronic Declaration System (EDS) '
  '(S5, GPM313 rules §14; GPM312 rules §59). Format: FFData built on the VMI MXFD of each form; no XSD was located (S5; S7).')
P('The EDS rules (VA-72, §21) give three ways to file once logged in: (1) the on-line form in the portal; (2) uploading a file '
  'prepared by accounting software, in the format of the published technical requirements, with the "Persiųsti failą" function; '
  '(3) confirming data transmitted through the web service (S6 §21).')
P("Web service EDSWebServiceUploadFile (S7): SubmitFile sends the .ffdata file (or a zip with it) in Base64, with AppName, "
  "UserName, Password and PersonCode (the payer's code). Success code 900 states the date by which the file must be confirmed "
  'in EDS. The status is read back with CheckFileState(FileId). The specification is version 2.01 of 2010; it is still the one '
  'offered on the current EDS page, and the published WSDL exposes the same two operations (S7).')
P('Mandatory human step: within 3 days of the transmission, a user with the right to file must log in to EDS and confirm the '
  'declaration under "Deklaravimas → Patvirtinti užpildytą formą" (S8). If it is not confirmed within 3 days, it is deleted and the '
  'submission is not counted (S8); the success message of SubmitFile (code 900) gives the exact confirmation date (S7). The VMI web service therefore never completes a filing on its own.')

H('3. Inbound integrations')
table(['ID', 'What comes back', 'Values', 'Source'], [
    ['IN-01 (Sodra)', 'getDocumentStatus(docUID): docStatus and description',
     'NST not submitted · FNS executed/accepted · PRC processing · ARC archived · ERR rejected for errors · DRF draft', 'S3 pages 9, 19-20'],
    ['IN-02 (VMI)', 'CheckFileState(FileId): file confirmation state and declaration state',
     'Confirmation: 10 confirmed, 20 not confirmed, 30 removed, 40 no longer confirmable. Declaration: 10 submitted, 21 accepted, '
     '22 accepted with errors, 101 not accepted, 102 rejected, 103 rejected after control, 100 annulled (other values in S7)', 'S7'],
    ['IN-03 (Sodra)', 'Sickness-certificate information for the employer',
     'NOT LOCATED: DataService has no operation that returns sickness-certificate data to the employer; the NP-SD2 instruction refers to electronic certificates and to '
     '"Pranešimai draudėjui" but not to a machine channel', 'S3; S4 point 68']])

H('4. Authentication and roles')
table(['Authority / channel', 'Authentication', 'Who', 'Source'], [
    ['Sodra EDAS account', 'Login via draudejai.sodra.lt, e-banking or epaslaugos.lt; qualified electronic signature on every notice',
     'Head of the company or an authorised person signs', 'S2'],
    ['Sodra DataService', 'WS-Security UsernameToken: EDAS user name and a service password set in EDAS ("Naudotojo nustatymai"; '
     '10-14 characters, at least 1 special character and 1 digit); 5 failed attempts in a row block the service',
     'Any EDAS user who has enabled the service', 'S3 page 4'],
    ['VMI EDS portal', 'From 1 September 2026, login only through the e-government gateway means (S9 news). The EDS help page says a foreign '
     'person without VMI registration can request VMI access means or declare a qualified electronic-signature certificate issued in '
     'Lithuania (not needed with a Lithuanian residence permit); whether this still works after 1 September is not stated (see 7)',
     'Representatives with filing rights for the payer', 'S9'],
    ['VMI web service', 'Separate user name and password created in EDS ("Nustatymai → Mano duomenys"); only representatives of a '
     'legal-entity taxpayer can enable it; the user must have the right to file for the PersonCode',
     'Software, plus an EDS user who confirms within 3 days', 'S7; S8']])

H('5. Technical specifications')
table(['Item', 'Sodra DataService', 'VMI EDSWebServiceUploadFile'], [
    ['Protocol', 'SOAP 1.2 over HTTPS, document/literal, MTOM (S3 pages 4, 15)', 'SOAP 1.1 in the 2010 specification; the WSDL also offers SOAP 1.2 (S7)'],
    ['Endpoint', 'https://draudejai.sodra.lt/edas-external/services/DataService (S3 page 15)',
     'https://deklaravimas.vmi.lt/EDSWebServiceUploadFile/EDSWebServiceUploadFile.asmx in the 2010 specification; the WSDL published today shows http:// in soap:address (S7)'],
    ['Operations', 'uploadEdasDraft, getDocumentLink, sendSignedDocument, getDocumentStatus, getPossibleDocuments (S3)', 'SubmitFile, CheckFileState (S7)'],
    ['Payload', 'FFDATA, UTF-8 without BOM, base64Binary (S3)', '.ffdata, or .zip containing .ffdata, in Base64 (S7)'],
    ['Form definitions', 'SAM: sam-v07.mxfd, form version 07 (S1)', 'GPM313.mxfd (created 2025-11-04, EDS file version 2025-12-31); GPM312.mxfd (created 2026-05-11, EDS file version 2026-06-12) (S5)'],
    ['Documentation', 'Version 1.0, 2016-01-19 (S3)', 'Version 2.01, 2010 (S7)']])

H('6. Error handling, corrections and deadlines')
P('Sodra DataService errors WSDATA-0 to WSDATA-9: system error, user not found, wrong credentials, service blocked, no document, '
  'draft not saved, invalid signature, document not saved, document not found, action not allowed (S3 page 20). NP-SD2 errors are '
  'corrected at once through a PT request with the PT-NP-SD2 annex (S4 point 76).')
P('VMI web service: SubmitFile errors 000-501 and success 900; CheckFileState errors 600-613 and success 901 (S7). VMI notifies '
  'technical non-acceptance electronically, at once and within 5 working days at the latest (S6 §26). Corrections are filed as a '
  'complete new return for the same period (S5, GPM313 rules §18; GPM312 rules §63).')
P('Deadlines: see the register in section 1. No source states whether the VMI filing date is the transmission date or the '
  'confirmation date (S6 §24 only says it is set by the EDS software), so web-service files should be confirmed well before the '
  'deadline (see 7).')

H('7. Gaps and queries (NOT LOCATED)')
B('Machine channel for sickness-certificate information from Sodra to the employer (IN-03).')
B('XSD for the FFData files (only the MXFD form definitions were found).')
B('Test environments for DataService and EDSWebServiceUploadFile.')
B('Machine-readable channel for VMI notices (informacinis pranešimas, FR1025).')
B('Mercans report spec for NP-SD2 (OUT-02), to be created if the leave integration is in scope; whether DataService accepts NP-SD2 (getPossibleDocuments).')
B('Whether the VMI filing date is the transmission date or the confirmation date of a web-service file.')
B('Whether a foreign operator can log in to EDS and do the confirmation after 1 September 2026.')
B('Whether the 2010 limits of the VMI web service still apply (200 files per day; 30-minute block after 5 wrong passwords; configurable, S7) and whether the endpoint is http or https (S7: specification https, WSDL http).')
B('Endpoints that appear only as attributes in the MXFD files, without documentation: VMI EDSMdocUploadService/MdocUploadService.svc and PublicServiceREST; Sodra AuthServiceWS (S1, S5).')
B('Late filing and correction of SAM: the SAM spec LT-SODRA-003 records a PT request for late data; not re-checked against the source in this document.')
B("Whether the Sodra web-service documentation (2016) and the VMI one (2010) are the latest versions: both are the ones offered on the authorities' current pages (S2, S7).")

H('8. Sources (read on 2026-10-27; copies and extracts under raw/docs/oficiais/LT/)')
table(['Key', 'Source'], [
    ['S1', 'Sodra: SAM page, filling instruction (points 48-56) and sam-v07.mxfd (sodra.lt/formos-ir-sablonai/sam-pranesimo-pildymas-ir-pateikimas)'],
    ['S2', 'Sodra: "Elektroninių pranešimų teikimas internetu" (sodra.lt/darbo-procesai/elektroniniu-pranesimu-teikimas-internetu)'],
    ['S3', 'Sodra: "„Sodros“ paskyros draudėjui (DataService) - Naudojimosi instrukcija", v1.0, 2016-01-19, with WSDL and XSD'],
    ['S4', 'Sodra: NP-SD2 filing instruction (points 57-76)'],
    ['S5', 'VMI: GPM313 rules (VA-121 as amended by VA-105, text from 2026) and GPM312 rules (VA-9 as amended by VA-24), with GPM313.mxfd and GPM312.mxfd from EDS'],
    ['S6', 'VMI: EDS usage rules approved by order VA-72 (2021, amended 2022), §21, §24 and §26'],
    ['S7', 'VMI: EDSWebServiceUploadFile specification v2.01 (2010) and the WSDL published on EDS'],
    ['S8', 'VMI EDS page "Žiniatinklio paslauga" (3-day confirmation; legal-entity representatives only)'],
    ['S9', 'VMI EDS news of 2026-08-27 (login only through e-government gateway means from 1 September) and help page for foreign persons']])

D.save('LT-SIR-001-v1.0.docx')
print('ok')

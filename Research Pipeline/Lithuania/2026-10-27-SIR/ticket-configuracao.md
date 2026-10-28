# Rascunho — ticket do SIR para o time de Configuração (Gmail, sem destinatário, não enviado)

Base: [[CONFERENCIA]] desta pasta. Hub: [[Lituania]].

---

**Subject:** Lithuania – Statutory Integration Requirements (SIR) LT-SIR-001 v1.0: Sodra and VMI filing set-up

Hi team,

Please find attached the Statutory Integration Requirements for Lithuania (LT-SIR-001 v1.0), covering the two integrations for the Accenture Lithuania implementation: statutory filing and leave.

- Sodra: SAM (monthly) and NP-SD2 (sickness and maternity data). Both are filed through the employer EDAS account with a qualified electronic signature. Sodra also offers the DataService web service (SOAP), with two modes: upload a draft for signing in EDAS, or send a document that is already signed.
- VMI: GPM313 (monthly) and GPM312 (annual), filed only electronically through EDS, as an on-line form, a file upload, or the EDSWebServiceUploadFile web service. A file sent by web service must be confirmed in EDS by an authorised user within 3 days; otherwise it is deleted and not treated as filed.
- Status read-back: Sodra getDocumentStatus and VMI CheckFileState.
- Open points are listed in section 7. The main one: no machine channel was found for receiving sickness-certificate information from Sodra.

Field layouts are in the report specs sent separately (SAM LT-SODRA-003 v1.0, GPM313 LT-VMI-001 v1.1, GPM312 LT-VMI-002 v1.1).

Thanks,

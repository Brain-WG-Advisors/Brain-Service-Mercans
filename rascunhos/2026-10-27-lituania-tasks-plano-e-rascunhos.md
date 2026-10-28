# Lituânia — plano de ação e rascunhos (tasks, e-mail ao Mohit, resposta ao Kevin)

Status: **rascunho para análise do usuário. Nada foi gravado no YouTrack nem no Gmail.**
**Passo 1 (Drive), feito em 27/10 — só arquivos novos ao lado dos originais; nenhum original alterado (aguarda aval):**
- `05 - Payroll Regulation Guide/2026 Regulation guide/Lithuania Payroll Regulation Guide_2026_v1.1.docx` (md5 4f7dd54b…)
- `09 - Alerts/2026/Lithuania_Changes in Tax Rates & social security Rates - 1st January 2026_v1.1.docx` (o Google Doc oficial, ligado à CT-4285, **não foi editado**: aplicar as correções nele só depois do aval)
- `03 - WTC/Lithuania  WTC V3.1.xlsx` (md5 59311d1d…) · `02 - DD/Lithuania Data Dictionary V3.1.xlsx` (md5 150faf46…)
- `18 - Statutory Reports/LT-VMI-001-GPM313-Spec_v1.1.xlsx` e `LT-VMI-002-GPM312-Spec_v1.1.xlsx` (para o usuário importar nas planilhas `.gsheet`, depois do aval)
- `19 - Statutory Integrations/LT-SIR-001-v1.0.docx` (pasta nova, padrão da Bélgica "17 - Statutory Integrations"; na Lituânia o 17 é Payslip)
- md5 de todas as cópias = arquivos locais. Links web do Drive: completar no passo 2.
**27/10, 22h (ok do usuário):** Google Doc oficial do Alerta corrigido; **A gravado como draftComment na CT-4285** (texto curto, só o Alerta; conferido pela API = texto aprovado; não publicado); **G gravado no Gmail** (sem destinatário, 6 anexos: CCG 2026, WTC V3.1, DD V3.1, GPM313/GPM312 v1.1, SIR v1.0; não enviado). Datas do G corrigidas pela ata do SteerCo de 27/10 (PR1 fev/2027, GLD 1º/06/2027; o rascunho dizia jan e maio). Os 5 rascunhos antigos do Gmail já não estavam na pasta. B, C e D gravados como draftComment em SR-419/420/421 (conferidos, não publicados). Pendentes: E (opcional), F (task do SIR) e H (Suporte).
Base: [[Research Pipeline/Lithuania/2026-10-27-atualizacao-2026/CONFERENCIA]] · [[Research Pipeline/Lithuania/2026-10-27-reports/CONFERENCIA]] · [[Research Pipeline/Lithuania/2026-10-27-SIR/CONFERENCIA]] · Hub [[Lituania]].
Tasks lidas na API em 27/10 (cópias em `raw/tickets/api/2026-10-27-LT/`).

## Plano de ação (cada passo só começa com o seu ok)

| # | Passo | Quem | Depende de | Checagem antes de seguir |
|---|---|---|---|---|
| 1 | **Drive:** copiar CCG 2026, WTC V3.1, DD V3.1 e LT-SIR-001 v1.0 para as pastas do país; corrigir o Alerta no próprio Google Doc (pelo navegador); você importa as specs GPM313/GPM312 v1.1 nas planilhas `.gsheet` (eu não sobrescrevo `.gsheet`) | eu + você (import) | seu ok | md5 da cópia = arquivo local; Alerta: texto exportado igual ao corrigido; links de cada arquivo anotados |
| 2 | Completar os links do Drive nos rascunhos abaixo (onde está `<link Drive>`) | eu | passo 1 | nenhum `<link Drive>` sobrando |
| 3 | **YouTrack — atualizar tasks existentes:** gravar os comentários A–E como **draftComment** (não publicados) | eu | passo 2 + seu ok no texto | GET de cada draft confere o texto |
| 4 | **YouTrack — task nova do SIR (F):** você abre a task com o texto F (o YouTrack não tem rascunho de task nova) | você | passo 2 | — |
| 5 | **Gmail:** um e-mail só ao Mohit (G), com a lista das tasks; apagar os 5 rascunhos antigos | eu (rascunho) / você (envio) | passos 3–4 (números das tasks) | um único rascunho; links abrem |
| 6 | **Kevin (HRBS-15253):** resposta H como draftComment — pela janela Suporte (dona dos tickets) | Suporte / você publica | passos 3–5 | — |

---

## Rascunhos

### A — CT-4285 "Lithuania_ Statutory alert Jan 2026 [ACCEPTANCE]" (Mohit, Open) — comentário

> Hi @mjain,
>
> The 2026 compliance artifacts for Lithuania have been reviewed against the official sources and updated. Please implement the 2026 rules from the files below (changes highlighted in light blue):
> - Statutory alert Jan 2026 (this ticket's document): <link Drive>
> - Payroll Regulation Guide 2026 (CCG): <link Drive>
> - WTC V3.1: <link Drive>
> - Data Dictionary V3.1: <link Drive>
>
> Corrections to the alert linked in this ticket:
> 1. Annual brackets: 20% up to €83,237.40; 25% from €83,237.40 to €138,729; 32% above (36 and 60 × VDU €2,312.15). The alert had €82,962 / €138,270 and 0% for the first bracket.
> 2. Rates apply by reference to each payment on its own (in practice 20%); on the employee's request, by reference to the total annual payments from the employer.
> 3. Sodra annual ceiling: €138,729 (60 × VDU); not applicable to health insurance (PSD).
>
> Other 2026 changes in the CCG, WTC and DD:
> 4. NPD: single formula, €747 − 0.49 × (monthly employment income − €1,153), minimum 0 (zero above €2,677.49). The former formula no longer applies.
> 5. Employer-paid voluntary health insurance: non-taxable up to €350 per year within the 25% cap; the excess is taxable and subject to Sodra (WTC 65630; wording also updated on 23610, 65810 and 65835).
> 6. Accidents at work, Group II: 0.49%.
> 7. Pay below the minimum wage: the employer also pays the employee and employer Sodra contributions on the difference up to €1,153 (exceptions apply).
> 8. DD: Elective Tax Rate description and Incapacity Level note.
>
> Sources: Law on Personal Income Tax (arts. 4, 6, 17, 20, 23(7)); Law XV-632 (arts. 3, 4); Law on State Social Insurance I-1336 (arts. 10(7), 10(9), 11); Law on Health Insurance I-1343 (art. 17(2)); Government Resolution No. 700/2025.

### B — SR-419 "LT-SODRA-003-SAM-Spec" (Mohit) — comentário

> Hi @mjain,
>
> LT-SODRA-003 (SAM) v1.0 was re-checked on 27/10/2026 against the current Sodra filling instruction (points 48–56) and the form definition sam-v07.mxfd. All fields match, so there is no change to the spec.

### C — SR-420 "LT-VMI-001-GPM313-Spec" (Mohit) — comentário

> Hi @mjain,
>
> LT-VMI-001 (GPM313) is updated to v1.1: <link Drive>
>
> Only the electronic format changed. The 2026 rules are unchanged:
> - Column H: XML field names of the VMI FFData form (B_MM_ID, B_MM_Pavadinimas, B_ML_Metai, B_ML_Menuo, G5–G12).
> - Column I: field lengths from the form definition (payer name 116; amounts 14).
> - Month without a leading zero (1–12).
> - Filing channels: EDS on-line form, FFData upload, or the EDS web service (EDS rules VA-72 §21).
>
> Source: VMI form definition GPM313.mxfd (EDS file version 31/12/2025).

### D — SR-421 "LT-VMI-002-GPM312-Spec" (Mohit) — comentário

> Hi @mjain,
>
> LT-VMI-002 (GPM312) is updated to v1.1: <link Drive>
>
> Only the electronic format changed. The 2026 rules (VA-24) were already in v1.0:
> - Column H: XML field names (B_MM_ID, B_MM_Pavad, G4–G7, LapoNr, L1-n…L13-n, U1-n…U15-n).
> - Column I: field lengths from the form definition (e.g. L3/U3 34, U15 68).
> - GPM312L has 10 lines per page and GPM312U has 5.
> - U12 is a date (YYYY-MM-DD).
> - Rates from 2026: L9 0/5/15/20/25/32; U9 0/5/7.5/10/15/20/25/32 (7.5 and 10 only for code 62).
>
> Source: VMI form definition GPM312.mxfd (EDS file version 12/06/2026).

### E — CT-3703 / CT-3704 / CT-3705 (reports, Brenet) — comentário curto, um em cada

> Hi @boispuu,
>
> The spec for this report was re-checked against the current official sources on 27/10/2026. Current version: [SR-420 GPM313 v1.1 | SR-421 GPM312 v1.1 | SR-419 SAM v1.0, no change]. Integration channels are described in the Lithuania SIR (<new SR task>).

### F — Task nova (você abre) — modelo SR-469 / SR-470

- **Projeto:** SR · **Título:** `LT: Lithuania Statutory Integration`
- **País:** LT · **Research Analyst:** Wallisson Gomes (ata do SteerCo 27/10: pesquisa da Lituânia é do Wallisson) · **Assignee:** Shyam Narayan Tripathi · **Phase:** Development Phase - Developer (igual SR-469/470) · **Due Date:** 11/11/2026 (sugestão: BO-35 e LT-01 vencem 11/11 na ata) · **Prioridade:** Normal
- **Descrição:**
> [LT-SIR-001-v1.0](https://drive.google.com/file/d/1PY-7fiZ1IMUBFLLi8gHOrOclS_xrw88g/view)
>
> Statutory Integration Requirements for Lithuania, covering Sodra (SAM, NP-SD2; EDAS account and DataService web service) and VMI (GPM313, GPM312; EDS on-line, FFData upload and EDSWebServiceUploadFile web service, which requires confirmation in EDS within 3 days). Open points are in section 7.

### G — E-mail único ao Mohit (substitui os 5 rascunhos)

**Subject:** Lithuania – 2026 rules, report specs and SIR: updated tasks

> Hi Mohit,
>
> The Lithuania compliance artifacts were reviewed against the official sources and updated. The details are in each task:
>
> - **CT-4285** (2026 rules): corrected alert and CCG 2026, WTC V3.1 and DD V3.1. Please implement the 2026 rules from these files. The current build still uses 2025 rules (raised by Accenture Lithuania in HRBS-15253).
> - **SR-420** GPM313 spec v1.1 and **SR-421** GPM312 spec v1.1: electronic format only (XML field names, lengths).
> - **SR-419** SAM spec v1.0: re-checked, no change.
> - **SR-[new]** Lithuania Statutory Integration (LT-SIR-001 v1.0): filing channels for Sodra and VMI.
>
> The client's parallel run starts in January 2027 (go-live May 2027).
>
> Thanks,

### H — HRBS-15253, resposta ao Kevin (draftComment pela janela Suporte)

> Hi @kgunawan,
>
> Following our call, the Lithuania updates are with the Development team:
> - 2026 calculation rules: CT-4285.
> - Statutory reports: GPM313 and GPM312 specs v1.1 (SR-420, SR-421); SAM unchanged (SR-419). The specs define the XML (FFData) file uploaded to the tax portals.
> - Integration with Sodra and VMI: SR-479 (Lithuania SIR).
> - 2027: the minimum wage (€1,245) is published; the 2027 average wage, which sets the tax brackets and the Sodra ceiling, will be added once approved.
>
> The event-driven Sodra forms (1-SD, 2-SD, 9-SD, 12-SD, 13-SD, PT) are not specified yet.

---

## Para você decidir antes de eu seguir
1. Autoriza o passo 1 (Drive)? Você importa as specs v1.1 nas planilhas?
2. Os comentários E (tasks CT-3703/04/05 do Brenet) entram ou bastam os das SR?
3. Task nova do SIR: Research Analyst, Assignee/Phase e Due Date.
4. H: o Kevin pediu planejamento (cronograma); a resposta remete às tasks do Development, sem prometer data. Ok assim?

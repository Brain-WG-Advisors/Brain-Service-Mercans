# Triagem de e-mails desde 2026-10-09 (feita em 2026-10-13, ~11h30)

Fonte: Gmail wgomes@mercans.com, 79 conversas (busca `after:2026/10/09 -in:sent`).
Separado em duas partes: **A. Gmail** (e-mails de pessoas — foco agora) e **B. YouTrack** (notificações de tickets).

---

# PRIORIDADE: Lily, Mohit, Ruchi (atualizado 13/10 ~12h)
Contexto: na reunião "Product Compliance Development" de hoje (notas Gemini), a Lily relatou atrasos de até 4 dias nas respostas (Espanha e Ucrânia) e ficou de levantar exemplos; Manju vai conversar sobre tempo de resposta.

| Pessoa | Item | Situação |
|---|---|---|
| Lily | SR-162 (follow-up 13/10 13:50 UTC: xsi:nil + 3 campos no DD) | **ÚNICO ABERTO.** Rascunho: `rascunhos/2026-10-11-youtrack-drafts/SR-162-2026-10-13-followup.md` (falta incluir os campos no DD e preencher as linhas). |
| Lily | SR-414, SR-415, SR-432 | Respondidos por mim hoje (última msg é minha). |
| Lily | Gmail Spain Migration (ponto 3, base codes) | Respondido em 09/10. Última msg dela é para Nabil/Christina. |
| Mohit + Ruchi | G1 Regular vs YTD (Canadá) | Draft pronto no Gmail. Call amanhã 14/10 10h. Mohit OOO hoje. |
| Ruchi | CA Tax Residency | Respondido em 09/10. |
| Mohit | Bahrain → enviar design do Chade | Compromisso meu (09/10), sem data. |
| Mohit | Ericsson 47 WTs | Prazo 21/10 (Compliance team). |
| Mohit | Congo CAMU, Roadmap Q4 | Sem ação minha. |

---

# A. GMAIL

## A1. Meu — aguardando minha resposta
| # | Assunto | Quem pede | Desde | O que falta |
|---|---|---|---|---|
| G1 | Regular vs YTD Method (Canadá, T4127) | Mohit Jain / Ruchi Gupta | 12/10 | Dizer qual método é o mais usado no mercado. Call "CA Clarifications" amanhã 14/10 10h. |
| G2 | Internal Certification of Statutory Reports – Kazakhstan | Malika Iskakova (cc Sadaf) | 12/10 | Acusar recebimento; explicar "GL" (General Ledger); relatórios estatutários são trimestrais. |
| G3 | Internal Certification of Statutory Reports – Azerbaijan | Pari (pazizzade, cc Sadaf) | 12/10 | Acusar recebimento; zip criptografado: pedir senha se necessário. |
| G4 | Fwd: Ericsson ME Payroll – AR3 forms (Líbano) | Manju Shetija (só para mim) | 13/10 | Rascunho dela para o Marko (AR/3 é da Jordânia; Líbano = R6). Validar e encaminhar ao Marko. |
| G5 | BE-CCG-001-v1.0 (comentários Google Docs) | Suman Rai | 09/10 e 13/10 | Action item: qual taxa aplicar (24,92%: pensions 8,86%, medical 3,80%, sickness 2,35%...); e "blue-collar within a scope of payroll?". Responder no próprio documento. |
| G6 | Google Chat – Suresh Jalihal (Netherlands) | Suresh Jalihal | 13/10 | "I am not getting it" — não entendeu o pedido da entidade NL. Responder no Chat. |

### Status dos drafts (2026-10-13)
- G1, G2, G3, G4: rascunhos criados no Gmail (pasta Drafts). Não enviados.
- G3: o anexo do Pari não precisa de senha pedida — "Parol MC01Payroll" no corpo do e-mail é a senha.
- G5 e G6: não são e-mail; textos abaixo para colar no Docs / Chat.

**G5 — resposta ao comentário da Suman no BE-CCG-001-v1.0 ("24.92% or 25%?")**
> Neither, as written. 24.92% is the basic employer contribution in force since Q1 2015 (DmfA instructions, "Les cotisations" › "Le pourcentage de cotisation globalisé"). From Q1 2018, for category 1 and 3 workers the rate is 19.88% ("Conséquence du tax-shift"), plus the wage moderation contribution, at most 5.12% ("La cotisation de modération salariale"): about 25.00% in total. The branch breakdown in the cell (pensions 8.86%, medical care 3.80%...) is the split of the 19.88%.
Fonte: socialsecurity.be/employer/instructions/dmfa/fr/latest/instructions/socialsecuritycontributions/contributions.html (lida em 2026-10-13). ⚠️ Possível erro no CCG (taxa 2026 = 24,92%) → candidato a `correcoes.md`.

**G6 — resposta ao Suresh no Google Chat (Holanda, correção de folha do ano anterior)**
> Hi Suresh, yes. Errors in a 2025 payroll tax return are corrected with a correction message (correctiebericht). Once the filing deadline for the last 2025 period (December / period 13) has passed, it is sent as a separate correction for 2025, within 8 weeks of finding the error. The Belastingdienst then issues an additional assessment or a refund for the difference (Handboek Loonheffingen, §14.2.4).
⚠️ Citação §14.2.4 vem de fonte secundária (Salaris Vanmorgen, citando o Handboek Loonheffingen 2025); não consegui abrir a página oficial da Belastingdienst.

## A2. Meu — compromissos e prazos
| # | Assunto | Prazo | Situação |
|---|---|---|---|
| G7 | Ericsson ME Payroll – feedback em 47 wage types (3 criar, 20 flags, 24 confirmar) | qua 21/10 | Pedido ao Compliance team; Marko enviou a pasta de WTCs ao Mohit. |
| G8 | Bahrain design — review before our next call | — | Prometi em 09/10 enviar o design do Chade para validação do time do Mohit. |
| G9 | Review Completed: Colombia SS and Income Tax Automation | fim de out. | Manju cobrando a Cinthya; ata registra revisão dos cálculos por mim e Cinthya até o fim do mês. |
| G10 | Fwd: Requesting access to Mercans Staging Environment | — | Manju pediu a todos instalar (VPN + HRB Admin) e avisar. |
| G11 | Delivery Status Notification – client_folder_managers | — | Meu e-mail de hoje não chegou ao grupo; reenviar para endereço válido. |
| G12 | AI-Generated Alerts Are Live – Content Review | — | Minha resposta (09/10) bloqueada para complianceteam@; Usema deve ter recebido. |

## A3. Já respondido por mim
- Ukraine – 1C to HRB migration – Escalation (13/10 9:57).
- Congo (Baker Hughes): reopening HRBS-14055 (09/10 16:50).

## A4. FYI — sem ação minha
- Congo: CAMU exemption — Mohit respondeu ao Daniel (mapear flag 58238 na entidade).
- Fwd: Spain Migration Progress — Lily informa campos AFI configurados (para Nabil/Christina).
- Re: Spain BIK for Gross-Up — 4212x substituído por 68460–68464 no WTC.
- Angola – IRPS 2027 — publicado.
- Ukraine Migration Project Plan | Checkpoint (Mohamed Nabil) — YTD jan/2025 carregado, pedido para Nataliia e Lily.
- Agenda, notas Gemini/Tactiq, licença aprovada, User Access Requests, marketing.

---

# B. YOUTRACK (tratar depois)
| # | Ticket | Quem pede | Desde | O que falta |
|---|---|---|---|---|
| Y1 | HRBS-15864 McDermott UK off-cycle | Romano Fusana | 12/10 | "Unable to reach Wallisson" (feriado). Dar retorno. |
| Y2 | HRBS-14055 Congo | Daniel Balogun | 11/10 | Código de dedução da Occupancy Tax (TOL). SLA. |
| Y3 | SR-162 UA D5-001 | Lily Li | 13/10 | xsi:nil nos "Blank" (linhas 49 e 51); Region/District/STI Code no DD; Region Code = Oblast? |
| Y4 | SR-432 ES AFI Outbound | Lily Li | 13/10 | Confirmar Work Center CCC como campo de empregado. |
| Y5 | SR-414 / SR-415 UA Form 1-PV | Lily Li | 09/10 (SR-415 overdue) | Amostra XML + elementos; coluna V em vermelho. Rascunhos em `rascunhos/2026-10-09-UA-SR-162-414-415-respostas.md`. |
| Y6 | HRBS-14255 UA Advance Payroll | Vaishnavi Mane | 12/10 | Pediu presença na call de 12/10 (já passou). |
| — | Sem ação minha | — | — | SR-160, SR-163, SR-30, SR-211, SR-316, SR-82, SR-79, SR-161. |

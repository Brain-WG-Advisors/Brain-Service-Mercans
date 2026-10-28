# Automation status pack — for Samuel (27/10/2026)

Montado pelo Vini a partir do cérebro, da DM do Muhammad, do Gmail (notas do Gemini e BRDs) e do Google Chat. Sem dados de funcionários de clientes nem credenciais.

## Como usar
1. Abrir o chat das automações no claude.ai (projeto **MERCANS**, que tem os BRDs; anexar também o **BRD_User_Stories_v2.0.docx** de lá).
2. Colar este arquivo inteiro.
3. Colar o pedido da seção "Pedido ao Claude" no fim.
4. Antes de mandar ao Marko, conferir com o Vini os pontos marcados "to confirm".

---

Pedido: call Wallisson × Vini × Samuel, 27/10 (`raw/reunioes/2026-10-27-call-wallisson-lituania-espanha.txt`, 01:36:51–01:39:20). O Marko, via Manju, quer saber quanto já foi feito, o que falta para finalizar e rodar e quando termina. A Manju pediu o plano para 28/10 (`raw/reunioes/2026-10-27-research-team-weekly.txt`, 16:24–17:42). Segundo ela, o Marko falou em 60–70% para o Andre. O Vini junta o material e passa ao Samuel no chat do Claude das automações. O Samuel gera o documento.


## As 2 automações
Confirmado pelo usuário em 27/10: a automação de alertas é a SCA.

| | Automação 1: Ticket → Artifact Redline | Automação 2: Statutory Change Alert (SCA) |
|---|---|---|
| O que faz | Ticket resolvido no YouTrack → pesquisa no dispositivo legal → alteração numa cópia (tracked change) → aprovação no reviewer app → publica (Drive, Archived, Monday, comentário e ticket Resolved) | Monitora mudanças estatutárias (faixas de imposto, tetos de SS, salário mínimo…) e gera tickets completos para a Engenharia, com gate e aprovação humana |
| Quem constrói hoje | Muhammad Muneeb Tahir | Ninguém designado; construção não iniciada (ver lacunas, item 3) |
| Quem cuidava antes | Kriztian Eris Labatete (Senior Internal Apps Developer). Saiu para outro projeto em 15/10 (notas do Gemini, "Redline automation followup") | Kriztian estava em cópia no BRD da SCA (31/08) |
| Documentos | Ticket_to_Artifact_Redline_BRD + System Requirements (Kriztian, 10/09); BRD_User_Stories_v1.2 (05/10); Compliance_Automation_Consolidated_BRD v1.0 (11/09) e v1.1 (08/10) | BRD-SCA-001 v1.2, User Stories v1.3, fluxograma v1.4 (31/08); incorporado ao Consolidated BRD v1.0 (11/09, seção 6) |
| Onde roda | Cluster Kubernetes + PostgreSQL da Mercans (Andre, 10/09) | Mesmos componentes do BRD consolidado (seção 8); ordem de construção: um loop de ponta a ponta antes dos outros (seção 11) |

Não precisa de chat específico: tudo o que é preciso está neste arquivo.

---



| Data | Quem | O quê | Fonte |
|---|---|---|---|
| até 07/07 | Wallisson + Kriztian | drift-sync funcionando de ponta a ponta (ticket resolvido → CCG → redline no Drive), provado no HRBS-1534 (NL); decidido trigger por ferramenta externa (n8n/Zapier) | raw/chats/2026-10-01-compliance-research.md (l. 11, 43) |
| 31/08 | Wallisson → Marko, Martin, Manju, Enaakshi, Illia, Kriztian | BRD da SCA (Statutory Change Alert) enviado para feedback: BRD-SCA-001 v1.2, User Stories v1.3, fluxograma | Gmail "SCA Automation — BRD ready for review" |
| 07/09 | Martin/Marko/Andre | Pedido de um BRD consolidado com os 3 loops | Gmail 11/09 (texto do e-mail) |
| 10/09 | Kriztian → Andre (cc Marko, Martin, Yojana, Wallisson) | BRD + System Requirements do Ticket→Redline; Andre: usar o Kubernetes e o PostgreSQL existentes | Gmail "Compliance Automation Workflow" |
| 11/09 | Wallisson → Martin, Marko, Andre, Manju | Consolidated BRD v1.0 (3 loops, mesmos componentes, ordem de construção, 8 decisões pendentes na seção 12) | Gmail "Consolidated BRD v1.0 (all three loops)" |
| 05/10 | Kriztian → aprovação | BRD_User_Stories_v1.2: Martin Rudi aprovou; Andre rejeitou ("This is not a Google document") | Gmail "Approval request for BRD_User_Stories_v1.2.docx" |
| 05/10 | Muhammad ↔ Wallisson | Estrutura de pastas do Drive; versão ativa = maior número de versão + link no Monday | DM Google Chat |
| 08/10 | Wallisson → Muhammad | S4: o ticket traz o link do Monday; sem link ou link diferente, não redige. Formato Word/Excel. BRD v1.1 enviado | DM Google Chat |
| 13/10 | Muhammad → Wallisson | Pipeline até o reviewer app funciona contra serviços reais; dúvida de desenho S3. Resposta: leitura 2 (Skill File aponta, resposta vem da fonte oficial), com 3 condições | DM Google Chat |
| 14/10 | Muhammad | Ticket de teste do Canadá roda inteiro até o reviewer app; pede tickets reais. Enviados HRBS-14331, HRBS-14055 e HRBS-11806 | DM Google Chat |
| 14/10 | Research Team Bi-Weekly | "Mohammed successfully ran the first set of automation tests. Targeting automation deployment by the end of the month" | Gmail, notas do Gemini 14/10 |
| 15/10 | Call "Redline automation followup" | Demo com UI mínima; Christian/Kriztian saiu, Wallisson vira ponto de contato; PDFs dos tickets enviados (Test.zip) | Gmail, notas do Gemini 15/10; DM |
| 19–20/10 | Muhammad | Token da API do Monday; board TEST criado (18436036437); escrita liberada como owner | DM; raw/chats/2026-10-19…, 2026-10-20… |
| 21/10 | Muhammad | Ciclo completo funcionando (publica no Drive, Archived, Monday, ticket Resolved). Decisão: aceitar as alterações na publicação | DM; raw/chats/2026-10-21-muhammad-redline-publicacao-tracked.md |
| 21/10 | Research Team Bi-Weekly | Suporte vai para assistente de IA (Arbites); ligar a base de compliance ao ticketing (Manju + Wallisson) | Gmail, notas do Gemini 21/10 |
| 27/10 07:58 | Muhammad | Publicação limpa; REDLINE_HRBS-9_… em Archived; comentário de fechamento com ID, link, dispositivo e aprovador | DM |
| 27/10 08:07 | Muhammad | Pergunta S24: checar também a coluna Owner do Monday? Resposta enviada em 27/10: só o tipo de documento | DM |

---


Sem % inventado: só conta como "feito" o que tem prova com data.

## Automação 1: Ticket → Artifact Redline (Muhammad)

| Etapa | Estado | Prova |
|---|---|---|
| BRD e requisitos | ✅ feito (Consolidated BRD v1.1, 08/10) | DM 08/10 |
| Infraestrutura (Kubernetes + PostgreSQL existentes) | ✅ decidido | Gmail 10/09 (Andre) |
| Ler ticket do YouTrack + Skill File + roteamento | ✅ funciona contra serviços reais | DM 13/10 |
| Pesquisa na fonte oficial (S3, leitura 2) | ✅ funciona (Canadá s.184) | DM 14/10 |
| Achar o documento pelo link do Monday (S4) | ✅ regra definida e implementada | DM 08/10, 27/10 |
| Redigir tracked change numa cópia | ✅ funciona (documento de teste) | DM 14/10 |
| Reviewer app (aprovação e registro de quem aprovou) | ✅ funciona | DM 13/10, 21/10 |
| Publicar: Drive, Archived, Monday, comentário, Resolved | ✅ funciona (board TEST, HRBS-9) | DM 21/10, 27/10 |
| Publicação limpa + cópia redlined em Archived | ✅ feito 27/10 | DM 27/10 |
| S24: dono do documento (coluna Owner) | ✅ decidido: só o tipo de documento | DM 27/10 (resposta enviada) |
| Rodar com tickets reais (HRBS-14331, 14055, 11806) | ❓ resultado não visto | DM 14/10 (pedido), 15/10 (PDFs) |
| Escrita no board **real** do Monday (7997825425) | ❓ não liberada; o usuário disse que não é necessária | log.md 20/10 |
| Trigger automático (n8n/scheduler) | ❓ não confirmado | — |
| Go-live / deploy | ⏳ meta "fim de outubro" | Notas do Gemini 14/10 |

## Automação 2: SCA (Statutory Change Alert)

| Etapa | Estado | Prova |
|---|---|---|
| BRD-SCA-001 v1.2 + User Stories v1.3 + fluxograma | ✅ feito, enviado ao Marko em 31/08 | Gmail 31/08 |
| Feedback do Marko | ❓ sem resposta no fio | Gmail 31/08 |
| Incorporado ao Consolidated BRD (destinos do alerta, seção 6) | ✅ feito | Gmail 11/09 |
| 8 decisões da seção 12 | ❓ não se sabe quais foram tomadas | Gmail 11/09 |
| Hoje (manual) | ✅ o Alerta por país é gerado por prompt manual "Statutory Change Alert" (desde dez/2025) | Google Chat, RA Team/Manju, 16/12/2025–08/01/2026 |
| Construção da automação | ❌ não iniciada, pelo que achei: sem construtor designado; pela seção 11, primeiro um loop de ponta a ponta (o de tickets) | Gmail 11/09; notas do Gemini 07/09 |
| Detecção de mudanças (parte afim) | 🔄 existe fora do nosso time: sistema com LLM do Mohsin Khan, com revisão humana, voltado a publicação | Notas do Gemini 09/09 |

---



| # | O que falta saber | De quem | Achado na varredura de 27/10 |
|---|---|---|---|
| 1 | Qual é o chat do Claude das automações | Usuário | Candidato: projeto **MERCANS** no claude.ai. Tem os BRDs (BRD_User_Stories v1.1, v1.2, v1.7, v2.0; Ticket_to_Artifact_Redline_BRD; Process_Overview_Plain_Language; notas "BRD - Plan" de 14/08). A conversa "Process automation" (26/09) está nele, mas tratou de teste de skill. O projeto **Compliance Research** (compartilhado com a org) é a casa original (instruções, AUTOMATION_ROADMAP, drift-sync), com conversas de jul e da pipeline. Confirmar qual |
| 2 | ~~A automação de alertas é a SCA?~~ | — | Sim, confirmado pelo usuário em 27/10 |
| 3 | Quem constrói a SCA e se a construção começou | Usuário | **Ninguém designado, pelo que achei.** Origem: prompt manual "Statutory Change Alert" (RA Team/Manju, dez/2025 e jan/2026), que ainda gera os Alertas por país. BRD da SCA em 31/08 sem resposta. Notas de 07/09: o "compliance monitoring engine" seria um microsserviço próprio; o primeiro loop a ser construído foi o de suporte (DevOps provisionando, cerca de 4 semanas). Relacionado: o **Mohsin Khan** mantém um sistema com LLM que captura atualizações estatutárias em sites oficiais, com revisão humana (Manju/Enaakshi), para publicação/marketing (notas de 09/09). Não é a SCA, mas cobre a parte de detecção |
| 4 | Resultado dos 3 tickets reais (HRBS-14331, 14055, 11806) | Muhammad | — |
| 5 | Data de go-live (meta de 14/10: fim de outubro) e o que falta para o board real | Muhammad | — |
| 6 | Resposta à S24 (coluna Owner) | — | Enviada em 27/10: só o tipo de documento |
| 7 | Quais das 8 decisões da seção 12 do BRD consolidado foram tomadas | Usuário | BRD v2.0 no projeto MERCANS pode responder |
| 8 | Ligação com o assistente de IA do suporte (Arbites), notas de 21/10 | Manju / usuário | — |
| 9 | Os 6 prints do Muhammad de 27/10 | Abrir no Chat | — |

---

## Pedido ao Claude (colar no chat)

Using only the material above (and the attached BRD v2.0), write a one-page status for Marko Taylor (English, presentation-ready) on the two compliance automations: (1) Ticket → Artifact Redline and (2) Statutory Change Alert (SCA). For each: what it does, what is done (with date), what is left to go live, risks, and next step with owner and date. Show progress as completed stages out of total stages, not as a guessed percentage. Mark anything not proven in the material as "to confirm". Add one simple chart: stages done vs remaining per automation. Also produce a 3-slide version (status, timeline, next steps) for the global team meeting.

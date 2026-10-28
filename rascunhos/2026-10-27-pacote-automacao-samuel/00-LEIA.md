# Pacote: status das automações para o Marko (via Samuel) — ENVIADO 2026-10-28 (e-mail ao Marko, cc Muhammad e Manju)

Pedido: call Wallisson × Vini × Samuel, 27/10 (`raw/reunioes/2026-10-27-call-wallisson-lituania-espanha.txt`, 01:36:51–01:39:20). O Marko, via Manju, quer saber quanto já foi feito, o que falta para finalizar e rodar e quando termina. A Manju pediu o plano para 28/10 (`raw/reunioes/2026-10-27-research-team-weekly.txt`, 16:24–17:42). Segundo ela, o Marko falou em 60–70% para o Andre. O Vini junta o material e passa ao Samuel no chat do Claude das automações. O Samuel gera o documento.

Arquivos: [[MENSAGEM-PRONTA-MARKO]] (o Samuel só envia) · [[linha-do-tempo]] · [[estado-por-etapa]] · [[lacunas]] · [[mensagem-samuel]]. Hub: [[suporte]].

## As 2 automações
Confirmado pelo usuário em 27/10: a automação de alertas é a SCA.

| | Automação 1: Ticket → Artifact Redline | Automação 2: Statutory Change Alert (SCA) |
|---|---|---|
| O que faz | Ticket resolvido no YouTrack → pesquisa no dispositivo legal → alteração numa cópia (tracked change) → aprovação no reviewer app → publica (Drive, Archived, Monday, comentário e ticket Resolved) | Monitora mudanças estatutárias (faixas de imposto, tetos de SS, salário mínimo…) e gera tickets completos para a Engenharia, com gate e aprovação humana |
| Quem constrói hoje | Muhammad Muneeb Tahir | Ninguém designado; construção não iniciada |
| Quem cuidava antes | Kriztian Eris Labatete (Senior Internal Apps Developer). Saiu para outro projeto em 15/10 (notas do Gemini, "Redline automation followup") | Kriztian estava em cópia no BRD da SCA (31/08) |
| Documentos | Ticket_to_Artifact_Redline_BRD + System Requirements (Kriztian, 10/09); BRD_User_Stories_v1.2 (05/10); Compliance_Automation_Consolidated_BRD v1.0 (11/09) e v1.1 (08/10) | BRD-SCA-001 v1.2, User Stories v1.3, fluxograma v1.4 (31/08); incorporado ao Consolidated BRD v1.0 (11/09, seção 6) |
| Onde roda | Cluster Kubernetes + PostgreSQL da Mercans (Andre, 10/09) | Mesmos componentes do BRD consolidado (seção 8); ordem de construção: um loop de ponta a ponta antes dos outros (seção 11) |

O "chat do Claude onde as automações rodam" não foi identificado (ver [[lacunas]]).

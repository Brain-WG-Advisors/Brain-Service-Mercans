# Estado por etapa (RASCUNHO 2026-10-27)

Volta para [[00-LEIA]]. Sem % inventado: só conta como "feito" o que tem prova com data.

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

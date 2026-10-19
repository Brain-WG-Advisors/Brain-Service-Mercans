# Plano: modelo de construção do Brain Service

> Índice: [[00-INDEX]] · Regras: [[CLAUDE]] · Reescrito em 2026-10-19 (versões anteriores no histórico do git e em [[log]])
> **Toda sessão começa aqui:** ler o Painel de progresso (seção 8), escolher **uma** fase ou fonte e seguir o Protocolo de sessão (seção 6).

## 1. Objetivo
Um cérebro que **melhora a nossa entrega**: mais acertos do que erros nos artefatos e nas respostas, antes do handover para os outros times. Ele não trabalha por nós, mas impede que a gente repita erro e responda sem fonte.

**Como sabemos que funcionou:** o **teste de exatidão** (seção 5) rodado no **claude.ai** antes e depois. O resultado é algo como "acertava X/30, agora acerta Y/30" e não tem nenhum erro já registrado em [[correcoes]] se repetindo.

## 2. Arquitetura
```
FONTES ───────────► OFICINA (esta pasta) ───────────► USO DIÁRIO (claude.ai)
monday              raw/        → material bruto       Skills payroll-compliance-*
YouTrack/HRBlizz    cartões     → extração filtrada      (valores e regras corrigidos)
Chats do claude.ai  hubs/notas  → conhecimento         Projeto "Brain Service"
Reuniões            correcoes   → erros e o correto      (estado, decisões, histórico,
Drive               testes/     → teste de exatidão       correções, fronteiras)
```
- **Oficina** = esta pasta, mantida pelo Claude Code. Só nós mexemos nela.
- **Uso diário** = claude.ai. O chefe e o time **não mudam de ferramenta**.
- Conhecimento que fica só na oficina **não conta como entregue**. Todo ciclo termina com publicação no claude.ai (Fase 4).

## 3. Princípios
1. **Filtrar, não despejar.** De cada fonte sai só o que muda a resposta certa: **erro + causa**, **decisão**, **versão final**, **alerta**, **pendência**. O resto fica em `raw/` e não é ingerido.
2. **Uma fonte por vez, até o fim do ciclo**: coletar → extrair → ingerir → teste → publicar.
3. **Fonte sempre citada.** Item sem fonte é marcado `⚠️ sem fonte` (regra 1 do [[CLAUDE]]).
4. **Sem dados pessoais** (regra 3). Docs nominais de funcionário (ex.: "Nome | País | ID" no monday) não são coletados.
5. **Sensível fica local.** `raw/reunioes/` e `raw/drive/` não vão para o git.
6. **Não duplicar skills** (regra 4). O que é estatutário corrigido vai **para a skill**, e o brain guarda só o registro.

## 4. Fases

| Fase | O que é | Entrega | Critério de saída |
|---|---|---|---|
| **0. Preparação** | Decisões e acessos (lista abaixo) | Itens de 0.1 a 0.8 respondidos | Nenhum bloqueio aberto para a Fase 1 |
| **1. Linha de base** | Teste de exatidão v1 com 30 perguntas tiradas de [[correcoes]] | `testes/exatidao.md` + nota no claude.ai **antes** | 30 perguntas rodadas e registradas |
| **2. Coleta** | Um ciclo por fonte, na ordem da seção 4.2 | `raw/<fonte>/` + `extracoes/AAAA-MM-DD-<fonte>.md` + notas atualizadas | Critério da fonte (4.2) cumprido |
| **3. Consolidação** | Propostas de **risco alto** de [[revisoes/2026-10-05-revisao]] + contradições + "revisa o cérebro" | Hubs sem contradição nos itens de risco alto | Zero proposta de risco alto em aberto |
| **4. Publicação** | Levar para o claude.ai: (a) correções estatutárias → skills; (b) pacote do brain → Projeto "Brain Service" | Skills atualizadas + projeto configurado | Os dois destinos atualizados com a data |
| **5. Medição** | Rodar de novo o teste no claude.ai | Nota **depois** + análise dos erros restantes | Meta atingida (0.8) ou plano de correção |
| **6. Rotina** | Manutenção semanal (seção 7) | Uma linha de [[log]] por semana | Contínuo |

Ordem: 0 → 1 → 2 (fonte por fonte) → 3 → 4 → 5 → 6. As Fases 2 a 5 podem girar em ciclos curtos, uma fonte de cada vez já publicada e medida.

### 4.1 Fase 0: decisões e acessos
| # | Item | Responsável | Status |
|---|---|---|---|
| 0.1 | Ok do chefe para coletar transcrições e Drive pelo Claude in Chrome | Usuário | ⏳ |
| 0.2 | Repositório `ViniCerqueira/brain-service` (privado, conta pessoal) pode ficar lá ou vai para uma conta da Mercans? | Usuário / chefe | ⏳ |
| 0.3 | Quem publica e atualiza as skills `payroll-compliance-*` no claude.ai da Mercans? | Usuário | ⏳ |
| 0.4 | A integração do GitHub está liberada nos Projetos do claude.ai? (Projeto → Add content → GitHub). Se não, o pacote entra por upload | Usuário | ⏳ |
| 0.5 | Extensão Claude in Chrome instalada e logada no Google da Mercans; `/chrome` conectando no Claude Code | Usuário | ⏳ |
| 0.6 | Nome da variável do token do YouTrack no `.env` (só o nome) | Usuário | ⏳ |
| 0.7 | Onde estão o pipeline (`mercans_pipeline_vX.sh`) e as saídas das execuções (repositório? Drive? outra máquina?) | Usuário | ⏳ |
| 0.8 | Meta de exatidão. Proposta: ≥ 27/30 (90%) e zero erro repetido de [[correcoes]] | Usuário / chefe | ⏳ proposta |

### 4.2 Fase 2: catálogo de fontes (nesta ordem)
| # | Fonte | O que coletar | O que **não** coletar | Caminho | Destino bruto | Critério de saída |
|---|---|---|---|---|---|---|
| F1 | **monday** | Boards: Root Cause Analysis Tracker (18396554143), Compliance Statutory Alerts Tracking [2025-2026] (18227732675), Compliance Artifacts (7997825425), Compliance Research: 2026 Change Management (18392983583), Compliance Roadmap (8084527463), Global Statutory Filings Tracker (9920776371) | Docs nominais de funcionários; BAU Master Client List; On-Call Directory | Conector monday (já funciona) | `raw/monday/AAAA-MM-DD-<board>.md` | Todos os itens de RCA e alertas avaliados (virou cartão ou foi descartado com motivo) |
| F2 | **YouTrack / HRBlizz** | Tickets resolvidos desde 2026-01-01 (HRBS-, CT-, SR-) | Tickets já ingeridos (04/08 a 29/09) | `scripts/youtrack_fetch.ps1` (API) | `raw/tickets/api/AAAA-MM-DD/` | Todos os tickets resolvidos do período com cartão ou descarte |
| F3 | **Chats do claude.ai** | Conversas dos projetos Mercans (Compliance, Research, Design & Dev) a partir de 2026-09, ou desde o início se nunca extraídas | Conversas pessoais e fora de Mercans | Claude in Chrome + [prompts/extracao-conversa.md](prompts/extracao-conversa.md) | `raw/chats/AAAA-MM-DD-<conversa>.md` | Todas as conversas do período listadas e extraídas |
| F4 | **Reuniões** | Transcrições e "Notes by Gemini" do time de compliance/research/design/liderança desde 2026-01-01 | Reuniões de outros times; 1:1 pessoais | Claude in Chrome (Drive/Meet) + [prompts/coleta-chrome.md](prompts/coleta-chrome.md) | `raw/reunioes/` (fora do git) | Lista de reuniões do período, cada uma baixada ou descartada |
| F5 | **Drive "Compliance Team"** | Por país: Version Control/changelog de CCG, WTC, DD e Specs; QA reports; listas de pendências | Artefatos completos (o conteúdo está nas skills) | Claude in Chrome + [prompts/coleta-chrome.md](prompts/coleta-chrome.md) | `raw/drive/<Pais>/` (fora do git) | Versão vigente de cada artefato confirmada nos hubs |
| F6 | **Pipeline** | Saídas das execuções (versões, `07-qa-report.md`, audit) | Scripts e config com chaves | Depende de 0.7 | `raw/pipeline/<Pais>/AAAA-MM-DD/` | Estado de cada país no hub conferido com a última execução |

**Ciclo de cada fonte:**
1. **Coletar** para `raw/` (imutável).
2. **Extrair** cartões para `extracoes/AAAA-MM-DD-<fonte>.md` usando [modelos/extracao.md](modelos/extracao.md): um cartão por item, com tipo, país, fonte e o que muda.
3. **Ingerir** os cartões nas notas: hub do país, [[correcoes]], `servicos/`, [[fronteiras]]. Cartão sem destino claro fica como pendência e vai para pergunta ao usuário.
4. **Testar**: cada correção nova vira pergunta em `testes/exatidao.md` ([modelos/teste-exatidao.md](modelos/teste-exatidao.md)).
5. **Registrar**: linha em [[log]], painel (seção 8) atualizado e commit.

## 5. Teste de exatidão
- **Onde:** `testes/exatidao.md` ([modelos/teste-exatidao.md](modelos/teste-exatidao.md)).
- **O que é:** perguntas reais, cada uma com a **resposta correta e a fonte**, saídas de [[correcoes]] e dos cartões.
- **Como roda:** colar a pergunta **no claude.ai** (onde o time trabalha), sem dar a resposta, e marcar ✅ certo / ⚠️ parcial / ❌ errado.
- **Quando:** Fase 1 (antes), Fase 5 (depois) e mensalmente na rotina.
- **Regra:** pergunta errada no teste vira ação, seja corrigir a skill, o projeto ou a nota. Não basta anotar.

## 6. Protocolo de sessão
**Início:**
1. Ler [[CLAUDE]], este plano (painel na seção 8) e [[correcoes]].
2. Dizer qual fase/fonte será trabalhada e o critério de saída dela.

**Durante:**
- Uma fase ou fonte por sessão. Assunto novo que aparecer vira item em Pendências (seção 9), não desvio.
- Na dúvida, perguntar (regra 5).

**Fim:**
1. Linha em [[log]].
2. Painel (seção 8) atualizado.
3. Commit + push do que mudou (sem `raw/reunioes/` nem `raw/drive/`).
4. Resumo ao usuário: o que entrou, o que ficou em dúvida, qual é o próximo passo.

## 7. Rotina (Fase 6, ~15 min/semana)
- Rodar o YouTrack desde a última data → ingerir os resolvidos.
- Ler no monday os itens novos de RCA e alertas.
- Cada ticket fechado: "fechei o ticket X" (registro KCS).
- Correção nova → skill/projeto no claude.ai + pergunta nova no teste.
- Mensal: rodar o teste de exatidão e "revisa o cérebro".

## 8. Painel de progresso
| Fase / fonte | Status | Última sessão | Próximo passo |
|---|---|---|---|
| 0. Preparação | ⏳ | — | Responder de 0.1 a 0.8 |
| 1. Linha de base | ⏳ | — | Montar as 30 perguntas a partir de [[correcoes]] |
| 2. F1 monday | ⏳ | — | Ler RCA + Alerts |
| 2. F2 YouTrack | ⏳ | — | Depende de 0.6 |
| 2. F3 Chats claude.ai | ⏳ | — | Depende de 0.5 |
| 2. F4 Reuniões | ⏳ | — | Depende de 0.1 e 0.5 |
| 2. F5 Drive | ⏳ | — | Depende de 0.1 e 0.5 |
| 2. F6 Pipeline | ⏳ | — | Depende de 0.7 |
| 3. Consolidação | ⏳ | — | Propostas de risco alto de 05/10 |
| 4. Publicação | ⏳ | — | Depende de 0.3 e 0.4 |
| 5. Medição | ⏳ | — | Depois da Fase 4 |
| 6. Rotina | ⏳ | — | Depois da Fase 5 |

**Já feito (base para as fases acima):** estrutura e regras (2026-10-01); carga de 3 projetos do Claude + 58 tickets → 49 hubs e 67 correções (2026-10-02); fichas de 38 skills (2026-10-02); revisão de 2026-10-05 com 37 propostas e 33 perguntas; repositório git privado (2026-10-08); pastas `raw/reunioes/` e `raw/drive/` fora do git (2026-10-19).

## 9. Pendências fora do roteiro
- Validação com **third-party payroll software** (critério do checklist CT-4321) e **alertas legislativos**: registrar como itens de qualidade em [[research-pipeline]] / [[design]] depois da F1 (o board de alertas está no monday). Perguntas abertas: qual software, em que etapa, qual saída.
- Cadeia para frente (artefatos → Dev → Implementation): uma linha em [[research-pipeline]] e o limite em [[fronteiras]].
- Abrir a pasta como vault no Obsidian (opcional).

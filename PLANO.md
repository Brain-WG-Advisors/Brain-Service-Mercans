# Plano: modelo de construção do Brain Service

> Índice: [[00-INDEX]] · Regras: [[CLAUDE]] · Versão 2, de 2026-10-19 (versões anteriores no git e em [[log]])
> **Toda sessão começa por [prompts/abrir-sessao.md](prompts/abrir-sessao.md)** → Painel (seção 10) → **uma** fase ou fonte → Protocolo (seção 8).
> **Escopo temporal: 2026-01-01 até a data da coleta, em todas as fontes.**

## 1. Objetivo
Um cérebro que **melhora a nossa entrega**: mais acertos do que erros nos artefatos e nas respostas, antes do handover para os outros times. Ele não trabalha por nós, mas impede que a gente repita erro e responda sem fonte.

**Prova:** o teste de exatidão (seção 7), rodado **no claude.ai** antes e depois, com respostas guardadas na íntegra para auditoria.

## 2. Arquitetura
```
FONTES (2026-01-01 → hoje)     OFICINA (esta pasta, Claude Code)           USO DIÁRIO (claude.ai)
monday ─────────┐              raw/          material bruto, imutável     Skills payroll-compliance-*
YouTrack/HRBS ──┤   inventário inventarios/  lista completa por fonte       (valores e regras corrigidos)
Chats claude.ai ┼──────────►   extracoes/    cartões com nível de evidência Projeto "Brain Service"
Reuniões ───────┤   validação  hubs/notas    conhecimento consolidado        (instruções + pacote de notas)
Drive ──────────┤   humana     correcoes.md  erros e o correto
Pipeline ───────┘              testes/       teste de exatidão + respostas ──► mede antes × depois
```
- **Oficina** = esta pasta, mantida no Claude Code. **Uso diário** = claude.ai. O chefe e o time não mudam de ferramenta.
- Conhecimento que fica só na oficina **não conta como entregue**. Ele precisa chegar ao claude.ai (Fase 4).

## 3. Padrão de dado sólido
Cada cartão (`modelos/extracao.md`) recebe **um nível de evidência**:

| Nível | O que é | Exemplos | Pode sustentar |
|---|---|---|---|
| **A** | Fonte primária oficial | Lei, decreto, portaria, site/manual da autoridade (AEAT, TGSS, NSSO...), schema oficial | Valor estatutário, regra legal, formato de filing |
| **B** | Documento interno versionado ou fechado | Artefato com Version Control, ticket **resolvido** com resposta aceita, RCA **Closed**, release note | Versão vigente, mapeamento, decisão de produto, erro confirmado |
| **C** | Declaração | Fala em reunião, mensagem em chat, comentário de ticket aberto | Decisão (com **quem** e **quando**), pendência, contexto |
| **D** | Inferência, sem fonte, "acho que" | Deduções, blogs, memória | **Nada.** Vira pendência ou pergunta ao usuário |

**Regras:**
1. **Valor estatutário só entra com nível A.** Pode chegar por um documento B que cite A, mas então o A é registrado como fonte.
2. **Conflito entre fontes:** A > B > C. No mesmo nível, vale o mais recente. Se não der para resolver, vira pendência no hub com as duas versões e as fontes. Nunca escolher em silêncio.
3. **Chave de deduplicação:** `PAÍS | ARTEFATO | ITEM` (ex.: `ES | WTC | 62983`, `UA | 4DF | código 128`). Antes de criar um cartão, buscar a chave em [[correcoes]], no hub e em `extracoes/`. Se já existir, o cartão **complementa** (fonte nova, confirmação) em vez de duplicar.
4. **Rastreabilidade:** todo cartão aponta para o arquivo em `raw/` e para o local exato (ticket + comentário, item do board, minuto ou trecho da transcrição, aba do arquivo).
5. **Sem dados pessoais** (regra 3 do [[CLAUDE]]). Cliente só quando for necessário para entender o caso.

## 4. Inventário antes da coleta (completude)
Nenhuma fonte é extraída sem antes ter a **lista completa do período**, em `inventarios/<fonte>.md` ([modelos/inventario.md](modelos/inventario.md)). Cada item do inventário termina num destes três estados: **cartão** (ID), **descartado** (motivo) ou **pendente** (por quê).

**Métricas por fonte**, registradas no inventário e no painel:

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura | (cartão + descartado) ÷ itens do inventário | **100%** |
| Rastreabilidade | cartões com caminho em `raw/` ÷ cartões | **100%** |
| Confirmação humana | cartões confirmados na amostra ÷ amostra | **≥ 95%** (abaixo disso, reextrair a fonte) |
| Incerteza | cartões [INCERTO] ÷ cartões | Acompanhar; cada um vira pergunta |

**Validação humana antes de ingerir:** o usuário confere **100% dos cartões de risco alto** (valor estatutário, correção de erro, versão vigente) e **10% sorteados** dos demais.

## 5. Fases, passos e critérios

### Fase 0: Preparação
| # | Item | Responsável | Status |
|---|---|---|---|
| 0.1 | Ok do chefe para coletar transcrições e Drive pelo Claude in Chrome | Usuário | ✅ decidido pelo usuário em 2026-10-19 (confirmar com o chefe) |
| 0.2 | O repositório `ViniCerqueira/brain-service` (privado, conta pessoal) fica lá ou vai para uma conta da Mercans? | Usuário / chefe | ⏳ |
| 0.3 | Quem publica e atualiza as skills `payroll-compliance-*` no claude.ai da Mercans? | Usuário | ⏳ |
| 0.4 | A integração do GitHub está liberada nos Projetos do claude.ai? (Projeto → Add content → GitHub) | Usuário | ⏳ |
| 0.5 | Extensão Claude in Chrome instalada e logada no Google da Mercans; `/chrome` conecta no Claude Code | Usuário | ⏳ |
| 0.6 | Nome da variável do token do YouTrack no `.env` (só o nome) | Usuário | ⏳ |
| 0.7 | Onde estão o pipeline e as saídas das execuções | Usuário | ⏳ |
| 0.8 | Meta de exatidão. Proposta: Conjunto A ≥ 27/30 e Conjunto B ≥ 80%, com zero erro repetido de [[correcoes]] | Usuário / chefe | ⏳ proposta |
| 0.9 | **Escopo de países:** o board Compliance Artifacts tem ~80 grupos de país e o brain tem 49 hubs. Quais são nossos? (ex.: Argélia, Angola, Tanzânia, Brasil, Iraque, Iêmen, Quênia...) | Usuário | ⏳ |
| 0.10 | O board de alertas `18227732675` parou em 2026-06-06. Existe um board ou planilha mais nova ("Alerts 2026 Link")? | Usuário | ⏳ |

**Saída:** 0.3, 0.5, 0.6 e 0.9 respondidos (os outros podem seguir em paralelo).

### Fase 1: Linha de base
Prompt: [prompts/fase-1-linha-de-base.md](prompts/fase-1-linha-de-base.md)
1. Gerar o **Conjunto A**: 30 perguntas estratificadas a partir de [[correcoes]], com gabarito e critério de acerto.
2. O usuário revisa as perguntas e o gabarito.
3. O usuário roda as 30 perguntas no claude.ai **sem** o pacote do brain e salva as respostas.
4. Corrigir contra o gabarito e registrar a nota da rodada 1.

**Saída:** `testes/exatidao.md` com a rodada 1 registrada e as respostas em `testes/rodadas/`.

### Fase 2: Coleta (uma fonte por ciclo, nesta ordem)
| # | Fonte | Prompt | Volume conhecido | Destino bruto |
|---|---|---|---|---|
| F1 | monday | [prompts/extracao-monday.md](prompts/extracao-monday.md) | RCA 91 itens; Alerts 42; Artifacts 712; + Change Mgmt, Roadmap, Filings | `raw/monday/` |
| F2 | YouTrack / HRBlizz | [prompts/extracao-youtrack.md](prompts/extracao-youtrack.md) | A medir no DryRun (58 já ingeridos de 04/08 a 29/09) | `raw/tickets/api/` |
| F3 | Chats do claude.ai | [prompts/coleta-chrome.md](prompts/coleta-chrome.md) §F3 + [prompts/extracao-conversa.md](prompts/extracao-conversa.md) | A medir no inventário | `raw/chats/conversas/` |
| F4 | Reuniões | [prompts/coleta-chrome.md](prompts/coleta-chrome.md) §F4 | A medir | `raw/reunioes/` (fora do git) |
| F5 | Drive | [prompts/coleta-chrome.md](prompts/coleta-chrome.md) §F5 (alvos vindos do board Artifacts) | A medir | `raw/drive/` (fora do git) |
| F6 | Pipeline | A escrever depois de 0.7 | — | `raw/pipeline/` |

**Ciclo de cada fonte (sempre igual):**
1. **Inventário** do período → `inventarios/<fonte>.md`.
2. **Coleta** para `raw/` (imutável).
3. **Extração** de cartões → `extracoes/AAAA-MM-DD-<fonte>.md`, com nível de evidência e chave de deduplicação.
4. **Validação humana** (seção 4) → cartões marcados como ✔ confirmado ou ✘ rejeitado.
5. **Ingestão** dos cartões confirmados: hub, [[correcoes]], `servicos/`, [[fronteiras]].
6. **Perguntas novas** → **Conjunto B** do teste (correções novas, que não estavam em [[correcoes]] na Fase 1).
7. **Fechamento:** métricas no inventário, [[log]], painel e commit.

**Saída de cada fonte:** cobertura de 100%, confirmação ≥ 95% e ingestão feita.

### Fase 3: Consolidação
1. Aplicar as **propostas de risco alto** de [revisoes/2026-10-05-revisao.md](revisoes/2026-10-05-revisao.md) que ainda valem depois da Fase 2.
2. Rodar "revisa o cérebro" e resolver as contradições.
3. Para cada país, **lista de correções que ainda não estão na skill** (insumo da Fase 4).

**Saída:** zero contradição aberta em item de risco alto; lista por país pronta.

### Fase 4: Publicação no claude.ai
Prompt: [prompts/fase-4-publicacao.md](prompts/fase-4-publicacao.md). Instruções do projeto: [prompts/projeto-claude-ai.md](prompts/projeto-claude-ai.md)
1. Montar o **Projeto "Brain Service"** no claude.ai: instruções + pacote de notas (GitHub ou upload).
2. Gerar os **pacotes de correção por skill** e entregar a quem publica (0.3).
3. Fazer um **teste de fumaça**: 5 perguntas no projeto, para confirmar que ele lê as correções e cita a fonte.

**Saída:** projeto ativo, pacotes entregues e fumaça aprovada.

### Fase 5: Medição
1. Rodar o **Conjunto A** (30) e o **Conjunto B** no claude.ai **com** o projeto e as skills atualizadas.
2. Comparar com a rodada 1. Analisar cada ❌ e ⚠️: falta no brain, falta na skill ou erro do modelo?
3. Cada ❌ vira ação, com dono e data.

**Saída:** meta 0.8 atingida, ou plano de correção com nova rodada marcada. Relatório de uma página para o chefe.

### Fase 6: Rotina (~15 a 20 min por semana)
- YouTrack desde a última data → ciclo F2 reduzido.
- monday: itens novos ou alterados no RCA e nos alertas.
- "fechei o ticket X" a cada entrega (KCS).
- Correção nova → skill/projeto + pergunta nova no Conjunto B.
- Mensal: rodar o teste e "revisa o cérebro".

## 6. Cronograma (proposta, ajustar na Fase 0)
| Fase | Sessões estimadas | Data-alvo |
|---|---|---|
| 0. Preparação | — (decisões do usuário) | 2026-10-21 |
| 1. Linha de base | 2 | 2026-10-23 |
| 2. F1 monday | 2–3 | 2026-10-28 |
| 2. F2 YouTrack (jan–out) | 4–6 (depende do volume) | 2026-11-06 |
| 2. F3 Chats | 3–5 | 2026-11-13 |
| 2. F4 Reuniões | 2–4 | 2026-11-19 |
| 2. F5 Drive | 3–4 | 2026-11-26 |
| 2. F6 Pipeline | 1–2 | depende de 0.7 |
| 3. Consolidação | 2 | 2026-12-02 |
| 4. Publicação | 2 | 2026-12-08 |
| 5. Medição | 1–2 | 2026-12-11 |

Depois de F1 e F2, se o usuário quiser, dá para fazer uma **publicação parcial** (Fase 4 só com as correções até ali) e começar a colher resultado mais cedo.

## 7. Teste de exatidão
- **Conjunto A (linha de base):** 30 perguntas tiradas de [[correcoes]] (Fase 1). Mede se o claude.ai repete erros já conhecidos.
- **Conjunto B (controle):** perguntas das correções **novas** da Fase 2. Elas não existiam quando o teste foi desenhado, então medem se o brain generaliza.
- **Protocolo:** chat novo no claude.ai, pergunta colada sem dica, resposta **salva na íntegra** em `testes/rodadas/AAAA-MM-DD/T-xxx.md` e correção contra o gabarito (✅ / ⚠️ / ❌) pelos critérios escritos antes da rodada.
- **Regra:** um ❌ não é só anotado; ele vira ação com dono.
- Detalhe: [prompts/fase-1-linha-de-base.md](prompts/fase-1-linha-de-base.md) e [modelos/teste-exatidao.md](modelos/teste-exatidao.md).

## 8. Protocolo de sessão
**Início:** colar [prompts/abrir-sessao.md](prompts/abrir-sessao.md). O Claude lê [[CLAUDE]], este plano e [[correcoes]], mostra o painel e confirma a fase/fonte e o critério de saída.

**Durante:**
- Uma fase ou fonte por sessão.
- Assunto novo vira Pendência (seção 11), não desvio.
- Na dúvida, perguntar.
- Tarefas mecânicas (leitura em lote, formatação) vão para subagentes Sonnet/Haiku; o modelo principal coordena e revisa.

**Fim:**
1. Métricas no inventário.
2. Linha em [[log]].
3. Painel atualizado.
4. Commit + push (sem `raw/reunioes/` e `raw/drive/`).
5. Resumo ao usuário: o que entrou, o que ficou em dúvida, próximo passo.

## 9. Riscos e como tratamos
| Risco | Mitigação |
|---|---|
| Volume grande (YouTrack desde jan, 712 itens no Artifacts) | Inventário primeiro; lotes por país/mês; subagentes para leitura |
| Extração errada por IA (~15% de erro histórico em pesquisa estatutária) | Nível de evidência + validação humana de 100% dos de risco alto + reextração se confirmação < 95% |
| Duplicação entre fontes (o mesmo caso em ticket, chat e RCA) | Chave `PAÍS | ARTEFATO | ITEM` |
| Dados pessoais e de cliente | Não coletar docs nominais; `raw/reunioes` e `raw/drive` fora do git |
| Alterar algo nas ferramentas da Mercans | Todas as coletas são **só leitura** (monday, Chrome, YouTrack) |
| Brain que ninguém usa | Fase 4 obrigatória; medição no claude.ai |

## 10. Painel de progresso
| Fase / fonte | Status | Cobertura | Confirmação | Última sessão | Próximo passo |
|---|---|---|---|---|---|
| 0. Preparação | 🔄 | — | — | 2026-10-19 | Responder 0.2–0.10 |
| 1. Linha de base | ⏳ | — | — | — | Gerar o Conjunto A |
| 2. F1 monday | ⏳ | 0/? | — | — | Inventário dos 6 boards |
| 2. F2 YouTrack | ⏳ | 0/? | — | — | Depende de 0.6 |
| 2. F3 Chats | ⏳ | 0/? | — | — | Depende de 0.5 |
| 2. F4 Reuniões | ⏳ | 0/? | — | — | Depende de 0.5 |
| 2. F5 Drive | ⏳ | 0/? | — | — | Depende de 0.5 e F1 (alvos) |
| 2. F6 Pipeline | ⏳ | — | — | — | Depende de 0.7 |
| 3. Consolidação | ⏳ | — | — | — | — |
| 4. Publicação | ⏳ | — | — | — | Depende de 0.3 e 0.4 |
| 5. Medição | ⏳ | — | — | — | — |
| 6. Rotina | ⏳ | — | — | — | — |

**Já feito (base):** estrutura e regras (2026-10-01); carga de 3 projetos do Claude + 58 tickets → 49 hubs e 67 correções (2026-10-02); fichas de 38 skills (2026-10-02); revisão de 2026-10-05 (37 propostas, 33 perguntas); repositório git privado (2026-10-08); modelo de construção v2, prompts de todas as fases e estrutura dos boards do monday levantada (2026-10-19).

## 11. Pendências fora do roteiro
- **Third-party payroll software** (critério do checklist CT-4321) e **alertas legislativos**: viram itens de qualidade em [[research-pipeline]]/[[design]] depois de F1. Perguntas: qual software, em que etapa, qual saída.
- **Cadeia para frente** (o board Artifacts usa as fases Research → Design → Development → Deployment): uma linha em [[research-pipeline]] e o limite em [[fronteiras]].
- O script do YouTrack usa `for: me` por padrão; para o histórico do time, ver [prompts/extracao-youtrack.md](prompts/extracao-youtrack.md).
- Abrir a pasta como vault no Obsidian (opcional).

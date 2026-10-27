# Plano: modelo de construção do Brain Service

> Índice: [[00-INDEX]] · Regras: [[CLAUDE]] · **Versão 3, de 2026-10-20** (anteriores no git e em [[log]])
> **Toda sessão começa por [prompts/abrir-sessao.md](prompts/abrir-sessao.md)** → Painel (§12) → **uma** fase ou fonte → Protocolo (§10).
> **Escopo temporal: 2026-01-01 até a data da coleta, em todas as fontes.**

## 1. Objetivo
Um cérebro que **melhora a nossa entrega**: mais acertos do que erros nos artefatos e nas respostas, antes do handover para os outros times. Ele não trabalha por nós, mas impede que a gente repita erro e responda sem fonte.

**Prova:** medição em três camadas (§7), sempre no **claude.ai**, com linha de base antes e resultado depois.

## 2. Arquitetura
```
FONTES (2026-01-01 → hoje)     OFICINA (esta pasta, Claude Code)           USO DIÁRIO (claude.ai)
monday ─────────┐              raw/          material bruto, imutável     Skills payroll-compliance-*
YouTrack/HRBS ──┤   inventário inventarios/  lista completa por fonte       (valores e regras corrigidos)
Chats claude.ai ┼──────────►   extracoes/    cartões com nível de evidência Projeto "Brain Service"
Reuniões ───────┤   validação  hubs/notas    conhecimento consolidado        (instruções + pacote de notas)
Drive ──────────┤   humana     correcoes.md  erros e o correto              ▲ publicado desde o MVP (Fase 2)
Pipeline ───────┘              testes/       medição (A, B, C + KPIs) ───────┘ e a cada fonte concluída
```
- **Oficina** = esta pasta, mantida no Claude Code. **Uso diário** = claude.ai. O chefe e o time não mudam de ferramenta.
- Conhecimento que fica só na oficina **não conta como entregue**. Desde o MVP, toda fonte concluída é publicada.

## 3. Governança
**Autorização:** a empresa autoriza o projeto e as coletas descritas aqui (confirmado pelo usuário em 2026-10-22). Não há etapa de aprovação formal.

| Atividade | Liderança | Dono do brain (usuário) | Claude Code | Dono das skills (0.3) |
|---|---|---|---|---|
| Definir escopo, metas e uso de dados | I | **A/R** | C | I |
| Coletar, inventariar, extrair, consolidar | I | A | **R** | — |
| Validar cartões | — | **A/R** | C | — |
| Publicar o Projeto no claude.ai | I | **A/R** | C | — |
| Aplicar pacotes de correção nas skills | I | C | C | **A/R** |
| Rodar a medição e reportar | I (recebe relatório) | **A/R** | R (corrige e analisa) | — |
| Manter na ausência do dono | — | Define backup | — | — |

R = executa · A = responde pelo resultado · C = consultado · I = informado.

**Limites de uso de dados:** coleta sempre só leitura; sem dados pessoais de funcionários de clientes; `raw/reunioes/`, `raw/drive/` e `publicar/` não vão para o git.

## 4. Padrão de dado sólido
Cada cartão (`modelos/extracao.md`) recebe **um nível de evidência**:

| Nível | O que é | Exemplos | Pode sustentar |
|---|---|---|---|
| **A** | Fonte primária oficial | Lei, decreto, portaria, site/manual da autoridade (AEAT, TGSS, NSSO...), schema oficial | Valor estatutário, regra legal, formato de filing |
| **B** | Documento interno versionado ou fechado | Artefato com Version Control, ticket **resolvido** com resposta aceita, RCA **Closed**, release note | Versão vigente, mapeamento, decisão de produto, erro confirmado |
| **C** | Declaração | Fala em reunião, mensagem em chat, comentário de ticket aberto | Decisão (com **quem** e **quando**), pendência, contexto |
| **D** | Inferência, sem fonte, "acho que" | Deduções, blogs, memória | **Nada.** Vira pendência ou pergunta ao usuário |

**Regras:**
1. **Valor estatutário só entra com nível A** (pode chegar por um B que cite o A; registrar o A como fonte).
2. **Conflito:** A > B > C. No mesmo nível, vale o mais recente. Se não der para resolver, vira pendência no hub com as duas versões. Nunca escolher em silêncio.
3. **Chave de deduplicação:** `PAÍS | ARTEFATO | ITEM` (ex.: `ES | WTC | 62983`). Buscar em [[correcoes]], no hub e em `extracoes/` antes de criar. Se já existir, o cartão complementa.
4. **Rastreabilidade:** todo cartão aponta para o arquivo em `raw/` e o local exato.
5. **Sem dados pessoais** (regra 3 do [[CLAUDE]]).

## 5. Inventário, validação e limite de fila
Nenhuma fonte é extraída sem a **lista completa do período** em `inventarios/<fonte>.md` ([modelos/inventario.md](modelos/inventario.md)). Cada item termina como **cartão**, **descartado** (com motivo) ou **pendente**, ou fica em **quarentena C** (ver §7).

| Métrica | Fórmula | Meta |
|---|---|---|
| Cobertura | (cartão + descartado + quarentena) ÷ itens | **100%** |
| Rastreabilidade | cartões com caminho em `raw/` ÷ cartões | **100%** |
| Confirmação humana | ✔ ÷ amostra validada | **≥ 95%** (abaixo disso, reextrair a fonte) |
| Incerteza | [INCERTO] ÷ cartões | Acompanhar; cada um vira pergunta |

**Validação:** o usuário confere **100% dos cartões de risco alto** e **10% sorteados** dos demais.
- **Lotes de no máximo 40 cartões** (~1 h): risco alto ~3 min por cartão, demais ~1 min.
- **Limite de fila:** se houver mais de **2 lotes** esperando validação, a coleta da próxima fonte para até a fila baixar. O seu tempo é o gargalo, e acumular cartões sem validar só gera retrabalho.

## 6. Fases, passos e critérios

### Fase 0: Preparação e aprovação
| # | Item | Dono | Status |
|---|---|---|---|
| 0.0 | Autorização do projeto | Empresa | ✅ autorizado (usuário, 2026-10-22) |
| 0.1 | Ok para coletar transcrições e Drive pelo Claude in Chrome | Empresa | ✅ autorizado (usuário, 2026-10-22) |
| 0.2 | Onde fica a base | Usuário | ✅ padrão: repositório privado `ViniCerqueira/brain-service` (2026-10-22; mudar se a empresa pedir) |
| 0.3 | Quem publica e atualiza as skills `payroll-compliance-*` no claude.ai da Mercans | Usuário | ✅ **o próprio usuário** (2026-10-22): os pacotes de skill da Fase 4 são aplicados por ele |
| 0.4 | A integração do GitHub está liberada nos Projetos do claude.ai? | Usuário | ✅ **não disponível** (2026-10-22): o pacote do Projeto entra por **upload** (`publicar/AAAA-MM-DD/`) |
| 0.5 | Extensão Claude in Chrome instalada e logada; `/chrome` conecta no Claude Code | Usuário | ✅ extensão instalada (2026-10-22). A conexão é confirmada na primeira sessão de F3 |
| 0.6 | Nome da variável do token do YouTrack no `.env` (só o nome) | Usuário | ✅ `YOUTRACK_TOKEN` (2026-10-22), que é o padrão do script |
| 0.7 | Onde estão o pipeline e as saídas das execuções | Usuário | ✅ (2026-10-22) Os scripts estão "dentro do Claude" (skills `mercans-pipeline-methodology`/`mercans-compliance-workflow`) e no Drive. O pipeline roda numa máquina e grava localmente (`~/mercans-pipeline/<CC>-compliance/01-ccg … 07-qa-crosscheck`); depois o resultado é **enviado à mão para o Drive**. Nesta máquina há só execuções de teste (YY, ZZ, 2026-09-11) e um pacote antigo v2.4 em Downloads; a versão atual (v2.9) e as saídas reais ficam na outra máquina. **F6 = cenário 2 (Drive) para o que já foi enviado + cenário 3 (cópia da outra máquina) para o que não foi.** **Atualizada em 2026-10-27 (migração):** o brain agora está na máquina do pipeline, então o **cenário 3 é local**: `C:\Users\instituto\mercans-pipeline`, script `mercans_pipeline_v2_12.sh` (não mais v2.9), saídas reais de BE, CO e FR em `<CC>-compliance/`, failure log F1–F74. Leitura direta do disco, sem pen drive. O cenário 2 continua para conferir máquina × Drive (as versões vigentes da Colômbia estão no Drive e no brain, não no pipeline). Inventário em [inventarios/pipeline.md](inventarios/pipeline.md). |
| 0.8 | Metas (§7) | Usuário | ✅ padrão: as metas propostas no §7 (2026-10-22; ajustáveis) |
| 0.9 | Escopo de países | Usuário | ✅ padrão: os 49 países com hub; país novo entra quando aparecer em ticket ou no monday (2026-10-22; ajustável) |
| 0.10 | O board de alertas `18227732675` parou em 2026-06-06. Existe um mais novo? | Usuário | ✅ não: o acompanhamento de alertas parou em 2026-06-06 (2026-10-22). Lacuna registrada no §13 |
| 0.11 | Backup do dono do brain | Usuário | ✅ padrão: sem backup por enquanto; prompts e protocolo escritos permitem retomar (2026-10-22) |

**Saída:** ✅ concluída em 2026-10-22.

### Fase 1: Linha de base
Prompt: [prompts/fase-1-linha-de-base.md](prompts/fase-1-linha-de-base.md)
1. Gerar o **Conjunto A** (30 perguntas a partir de [[correcoes]], estratificadas, com gabarito e critérios). O usuário revisa.
2. Rodar no claude.ai **sem** o projeto, **2 vezes cada pergunta**, e salvar as respostas.
3. Corrigir e registrar a nota da rodada 1.
4. **KPIs operacionais, primeira leitura:** K1 (RCA) pelo monday. K2 a K4 entram com retroativo quando a F2 terminar (§7).

**Saída:** `testes/exatidao.md` com a rodada 1; `testes/kpis.md` com o K1.

### Fase 2: MVP, publicar o que já existe (até 1 semana depois da Fase 1)
Prompts: [prompts/publicacao.md](prompts/publicacao.md) + [prompts/projeto-claude-ai.md](prompts/projeto-claude-ai.md) + [prompts/fase-5-medicao.md](prompts/fase-5-medicao.md) Partes 1–2 (rodada 2 do A)
1. Corrigir o que for bloqueante no pacote atual (67 correções, 49 hubs, serviços, fronteiras): dado sensível, links para `raw/`, contradição de risco alto.
2. Montar o **Projeto "Brain Service"** no claude.ai (instruções + pacote) e passar no **teste de fumaça** (5/5).
3. **Rodada 2 do Conjunto A** com o projeto. Primeiro resultado para a liderança.
4. **A data do MVP vira a data de corte do Conjunto C** (§7).
5. Liberar o uso pelo time e pela liderança.

**Saída:** projeto em uso, rodada 2 registrada e relatório curto à liderança ([modelos/relatorio-lideranca.md](modelos/relatorio-lideranca.md)).

### Fase 3: Coleta (uma fonte por ciclo, nesta ordem)
| # | Fonte | Prompt | Volume conhecido | Destino bruto | Bloqueio |
|---|---|---|---|---|---|
| F1 | monday | [prompts/extracao-monday.md](prompts/extracao-monday.md) | RCA 91; Alerts 42; Artifacts 712; + Change Mgmt, Roadmap, Filings | `raw/monday/` | — |
| F2 | YouTrack / HRBlizz | [prompts/extracao-youtrack.md](prompts/extracao-youtrack.md) | A medir (58 já ingeridos de 04/08 a 29/09) | `raw/tickets/api/` | 0.6 |
| F3 | Chats do claude.ai | [prompts/coleta-chrome.md](prompts/coleta-chrome.md) §F3 | A medir | `raw/chats/conversas/` | — |
| F4 | Reuniões | [prompts/coleta-chrome.md](prompts/coleta-chrome.md) §F4 | A medir | `raw/reunioes/` (fora do git) | — |
| F5 | Drive | [prompts/coleta-chrome.md](prompts/coleta-chrome.md) §F5 (alvos do F1) | A medir | `raw/drive/` (fora do git) | — |
| F6 | Pipeline | [prompts/extracao-pipeline.md](prompts/extracao-pipeline.md) (cenário 3 local + 2 para conferência, conforme a 0.7) | [inventarios/pipeline.md](inventarios/pipeline.md) | `raw/pipeline/` | 0.7 ✅ |

**Ciclo de cada fonte:**
1. Inventário.
2. Coleta.
3. Extração em cartões.
4. Validação em lotes de até 40 (§5).
5. Ingestão.
6. **Publicação incremental** no Projeto (sync/upload) e **pacote de skill** quando houver correção estatutária.
7. Perguntas novas para o **Conjunto B**.
8. Fechamento: métricas no inventário, horas reais × estimadas (§9), [[log]], painel e commit.

**Saída de cada fonte:** cobertura de 100%, confirmação ≥ 95%, ingerido **e publicado**.

### Fase 4: Consolidação (depois de F2 e no fim da coleta)
Prompt: [prompts/fase-4-consolidacao.md](prompts/fase-4-consolidacao.md)
1. Propostas de risco alto de [revisoes/2026-10-05-revisao.md](revisoes/2026-10-05-revisao.md) que ainda valem.
2. "Revisa o cérebro" e resolução das contradições.
3. Lista, por país, das correções que ainda não estão na skill → pacotes ([prompts/publicacao.md](prompts/publicacao.md) Passo 3).

### Fase 5: Medição final
Prompt: [prompts/fase-5-medicao.md](prompts/fase-5-medicao.md) · Relatório: [modelos/relatorio-lideranca.md](modelos/relatorio-lideranca.md)
1. Rodar A, B e C (2 vezes cada pergunta) com o projeto e as skills atualizadas.
2. KPIs K1 a K4: período posterior ao MVP × linha de base de jan–out/2026.
3. Cada ❌ ou ⚠️ instável: causa (falta no brain / falta na skill / erro do modelo / gabarito) → ação com dono e data.
4. **Relatório de uma página** para a liderança, com a decisão: manter e escalar / ajustar / encerrar.

### Fase 6: Rotina (~20 min por semana)
Prompt: [prompts/rotina.md](prompts/rotina.md) (semanal e mensal)
- YouTrack desde a última data → ciclo F2 reduzido. Tickets novos alimentam o Conjunto C enquanto ele não tiver 20 perguntas.
- monday: itens novos ou alterados no RCA e nos alertas.
- "fechei o ticket X" (KCS) a cada entrega.
- Correção nova → projeto/skill + pergunta no B.
- Mensal: KPIs, uma rodada do teste e "revisa o cérebro".

## 7. Medição em três camadas
| Camada | O que mede | Como | Risco que cobre |
|---|---|---|---|
| **Conjunto A** (30) | O claude.ai ainda repete erros que já conhecemos? | Perguntas de [[correcoes]]; rodadas 1 (sem projeto), 2 (MVP) e final | Erro repetido |
| **Conjunto B** (cresce na Fase 3) | O conhecimento novo chegou ao claude.ai? | Perguntas das correções novas de cada fonte | Publicação falha |
| **Conjunto C** (~20, **cego**) | O brain **generaliza** para casos que nunca viu? | Perguntas de tickets **resolvidos depois da data do MVP**, escolhidos ~2 por semana. Esses tickets ficam em **quarentena C**: só são ingeridos depois da medição final | **Vício do teste**: A e B estão dentro do projeto, então melhoram por definição. O C não está |
| **KPIs operacionais** | A entrega ficou mais robusta? | Ver abaixo, com linha de base jan–out/2026 | Exatidão sem efeito no trabalho |

**Protocolo de todas as rodadas:**
- Chat novo para cada pergunta, sem dica.
- **Cada pergunta roda 2 vezes.** Duas ✅ = ✅. Respostas divergentes = ⚠️ **instável**, que conta como não acerto.
- Respostas salvas na íntegra em `testes/rodadas/AAAA-MM-DD/`.
- Critérios escritos **antes** da rodada.
- O gabarito nunca sobe para o projeto.

**KPIs operacionais** (`testes/kpis.md`, mensal):

| # | KPI | Fonte | Fórmula | Direção |
|---|---|---|---|---|
| K1 | RCAs atribuídos a Compliance | monday RCA (Department = Compliance & Research ou CAPA de Compliance) | nº por mês | ↓ |
| K2 | Defeitos pós-handover em artefato nosso | YouTrack (cartões "erro+causa" apontados por BA/Dev em SR-/CT-) | nº por mês | ↓ |
| K3 | Retrabalho de resposta | YouTrack (autocorreção nossa ou ticket reaberto) | ÷ tickets respondidos no mês | ↓ |
| K4 | Tempo até a primeira resposta nossa | YouTrack (tickets HRBS de compliance) | mediana em dias úteis | ↓ |

**Metas** (0.8, padrão adotado em 2026-10-22):
- A ≥ 27/30.
- B ≥ 85%.
- C ≥ 75%.
- Zero erro repetido de [[correcoes]].
- K2 e K3 com queda de 30% em relação à linha de base em até 3 meses depois do MVP.

## 8. Cronograma (com 20% de folga incluída; recalibrar depois de cada inventário)
| Fase | Data-alvo |
|---|---|
| 0. Preparação | ✅ 2026-10-22 |
| 1. Linha de base (A rodada 1, K1) | 2026-10-28 |
| **2. MVP publicado + A rodada 2 (corte do C)** | **2026-11-04** |
| 3. F1 monday | 2026-11-13 |
| 3. F2 YouTrack (jan–out) + K2 a K4 retroativos | 2026-11-27 |
| 4. Consolidação intermediária | 2026-12-02 |
| 3. F3 Chats | 2026-12-11 |
| 3. F4 Reuniões | 2026-12-18 |
| 3. F5 Drive | 2027-01-15 (recesso de fim de ano considerado) |
| 3. F6 Pipeline | 0.7 resolvida e inventário aprovado em 2026-10-27; próximo: Passo 2 |
| 4. Consolidação final | 2027-01-20 |
| 5. Medição final + relatório | 2027-01-27 |

## 9. Capacidade (horas do usuário; o trabalho do Claude Code não entra)
| Fase / fonte | Atividades do usuário | Estimativa | Real |
|---|---|---|---|
| 0 | Decisões | 2 h | ~1 h |
| 1 | Revisar 30 perguntas (1 h) + rodar 60 chats (2 h) | 3 h | |
| 2 MVP | Montar o projeto, fumaça, rodada 2 (60 chats) | 3–4 h | |
| F1 monday | Aprovar inventário + validar ~80–150 cartões | 4–6 h | |
| F2 YouTrack | Aprovar consulta + validar ~150–250 cartões | 8–12 h | |
| F3 Chats | Aprovar inventário + validar | 6–10 h | |
| F4 Reuniões | Aprovar inventário + validar | 4–8 h | |
| F5 Drive | Aprovar inventário + validar | 4–6 h | |
| 4 Consolidação | Decidir propostas e contradições | 3 h | |
| 5 Medição final | ~140 chats (A + B + C, 2 vezes) + relatório | 5–6 h | |
| **Total** | | **≈ 42–60 h em ~14 semanas ≈ 3–4,5 h/semana** | |

**Regra:** se as horas reais de uma fonte passarem de 130% da estimativa, recalibrar as próximas e avisar a liderança sobre a nova data. Não cortar validação para recuperar prazo.

## 10. Protocolo de sessão
**Início:** colar [prompts/abrir-sessao.md](prompts/abrir-sessao.md). O Claude lê [[CLAUDE]], este plano e [[correcoes]], mostra o painel e confirma a fase/fonte, o critério de saída e os bloqueios.

**Durante:**
- Uma fase ou fonte por sessão.
- Assunto novo vira Pendência (§13).
- Na dúvida, perguntar.
- Tarefas mecânicas vão para subagentes Sonnet/Haiku; o modelo principal coordena e revisa.

**Fim:**
1. Métricas no inventário.
2. Horas reais (§9).
3. [[log]].
4. Painel.
5. Commit + push (sem `raw/reunioes/`, `raw/drive/`, `publicar/`).
6. Resumo ao usuário: o que entrou, o que ficou em dúvida, próximo passo.

## 11. Riscos e como tratamos
| Risco | Mitigação |
|---|---|
| **Adoção:** ninguém usa o brain | MVP no claude.ai em 2 semanas; relatório com números à liderança |
| **Capacidade:** validação maior que o tempo do usuário | Estimativa por fonte, lotes de 40, limite de fila (2 lotes), recalibração em 130% |
| **Vício do teste** (A/B dentro do projeto) | Conjunto C cego com quarentena + KPIs operacionais |
| Variação do modelo | 2 rodadas por pergunta; divergência = instável |
| Volume grande (YouTrack desde jan, 712 itens no Artifacts) | Inventário primeiro; lotes por país/mês; subagentes |
| Extração errada por IA (~15% histórico) | Níveis de evidência + validação de 100% do risco alto + reextração abaixo de 95% |
| Duplicação entre fontes | Chave `PAÍS | ARTEFATO | ITEM` |
| Dados pessoais e da Mercans fora do controle | Bloqueios 0.1 e 0.2; `raw/reunioes`, `raw/drive` e `publicar/` fora do git; só leitura nas ferramentas |
| Dependência de uma pessoa | Backup definido (0.11); protocolo e prompts escritos |

## 12. Painel de progresso
| Fase / fonte | Status | Cobertura | Confirmação | Horas (est./real) | Última sessão | Próximo passo |
|---|---|---|---|---|---|---|
| 0. Preparação | ✅ | — | — | 2 / ~1 | 2026-10-22 | — |
| 1. Linha de base | ⏳ **próxima** | — | — | 3 / | — | Gerar o Conjunto A |
| 2. MVP | ⏳ | — | — | 3–4 / | — | Depois da Fase 1 |
| 3. F1 monday | ⏳ | 0/? | — | 4–6 / | — | Inventário dos 6 boards |
| 3. F2 YouTrack | ⏳ | 0/? | — | 8–12 / | — | Depende da 0.6 |
| 3. F3 Chats | ⏳ | 0/? | — | 6–10 / | — | Depois da F2 |
| 3. F4 Reuniões | ⏳ | 0/? | — | 4–8 / | — | Depois da F3 |
| 3. F5 Drive | ⏳ | 0/? | — | 4–6 / | — | Depois da F4 (alvos vêm do F1) |
| 3. F6 Pipeline | 🔄 inventário aprovado | 0/4 | — | — | 2026-10-27 | Passo 2: coletar os relatórios para raw/pipeline/ |
| 4. Consolidação | ⏳ | — | — | 3 / | — | — |
| 5. Medição final | ⏳ | — | — | 5–6 / | — | — |
| 6. Rotina | ⏳ | — | — | 20 min/sem | — | — |

**Já feito (base):** estrutura e regras (2026-10-01); carga de 3 projetos do Claude + 58 tickets → 49 hubs e 67 correções (2026-10-02); fichas de 38 skills (2026-10-02); revisão de 2026-10-05 (37 propostas, 33 perguntas); repositório git privado (2026-10-08); modelo v2 com prompts de todas as fases e estrutura dos boards do monday (2026-10-19); modelo v3 com governança, MVP, medição em três camadas e capacidade, (2026-10-20); prompts das Fases 4, 5 e 6 e da F6 e modelo de relatório (2026-10-21); Fase 0 concluída, sem termo formal porque a empresa já autoriza (2026-10-22) → **todas as fases têm prompt**.

## 13. Pendências fora do roteiro
- **Saídas do pipeline só na máquina local até alguém enviar ao Drive** (0.7): risco de o Drive ficar com uma versão mais velha do que a gerada, ou de saídas se perderem. Na F6, cruzar as versões da máquina × Drive × monday; avaliar um passo fixo "enviar ao Drive" no fim de cada execução. **2026-10-27:** confirmado na Colômbia (pipeline com CCG v1.2/WTC v1.4/DD v1.0; vigentes no Drive e no brain: v1.4/v1.6/v1.3). O repo `~/mercans-pipeline` não tem remote (única cópia).
- **Alertas legislativos sem acompanhamento desde 2026-06-06** (0.10): o único board parou. A F1 coleta os 42 itens existentes, e a lacuna de jun–out precisa de um processo novo (proposta depois da F1: rotina de alertas por país, com o pipeline/Stage 1 como motor, ver a pendência abaixo).
- **Third-party payroll software** (critério do checklist CT-4321) e **alertas legislativos**: viram itens de qualidade em [[research-pipeline]]/[[design]] depois do F1. Perguntas: qual software, em que etapa, qual saída.
- **Cadeia para frente** (o board Artifacts usa as fases Research → Design → Development → Deployment): uma linha em [[research-pipeline]] e o limite em [[fronteiras]].
- O script do YouTrack usa `for: me` por padrão; para o histórico do time, ver [prompts/extracao-youtrack.md](prompts/extracao-youtrack.md).
- Abrir a pasta como vault no Obsidian (opcional).

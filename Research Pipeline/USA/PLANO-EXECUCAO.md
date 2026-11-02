# EUA: plano de execução até o resultado final (rascunho, 29/10/2026)

> Frente EUA ([[frentes/eua/estado|estado]]). Base: [[Research Pipeline/USA/PROPOSTA-ESTRUTURA|PROPOSTA-ESTRUTURA]], [[Research Pipeline/USA/PRIORIDADE-ESTADOS|PRIORIDADE-ESTADOS]], [[Research Pipeline/USA/US-compliance/BLOQUEIOS-CHROME|BLOQUEIOS-CHROME]], skill `country-build`.

## 1. Resultado final (o que é "pronto")
Pacote único EUA em `US-compliance/10-release/`, cada artefato aprovado pelo auditor (qa_pass):
- **CCG**: módulo federal + módulo multi-estado + 1 anexo por estado (51).
- **Scope manifest**, **Report Specs** (941, 940, W-2/W-3 EFW2; por estado: retenção, reconciliação anual, UI trimestral, W-2 estadual, local onde houver), **DD**, **WTC** (colunas de tributação federal e por estado), **SIR** (processo do provedor terceiro), **Payslip**, **skill `payroll-compliance-usa`**, **Design**.
- Fora do pacote, para o time: `USA-ESTADOS-MATRIZ.xlsx` (51 linhas, valores com vigência e fonte) e `USA-TABELAS/` (as tabelas a manter e subir todo ano).
- Validação: nenhum estado fora (US-MQ-11). Calculadora oficial onde existir; senão, re-derivação pelas tabelas oficiais (Stage 9b).

## 2. Caminhos de acesso às fontes (todos, em ordem)
| # | Caminho | Serve para | Situação |
|---|---|---|---|
| 1 | Busca/leitura direta (WebFetch) | Sites que não bloqueiam | Funciona |
| 2 | Claude in Chrome (aba própria, só leitura) | Sites que bloqueiam robô mas abrem para pessoa | Funciona; **falta liberar ~20 domínios** na extensão (sessão de 5 min com o usuário) |
| 3 | Wayback Machine (cópia 2025/2026 do arquivo oficial) | Sites bloqueados por país | Funciona; **limite de ritmo** (429) → 1 pedido a cada 10 s, retomar no dia seguinte |
| 4 | VPN com saída nos EUA | Bloqueio por país sem cópia no Wayback | **Espera a TI** (pergunta enviada à Manette em 29/10) |
| 5 | Colega nos EUA baixa | O que sobrar | Lista pronta: `LINKS-PARA-BAIXAR.md` |

Proibido em todos: script na página, alterar texto para passar filtro, resolver CAPTCHA, login.

## 3. Fases
| Fase | O que | Como | Saída | Depende de |
|---|---|---|---|---|
| **A. Destravar** (dia 1, manhã) | Liberar domínios na extensão; resposta da TI sobre VPN | Usuário + eu (abrir os domínios um a um) | Caminhos 2 e 4 ativos | Usuário, TI |
| **B. Onda 1 — fechar** | Partes que faltam nos 10 estados | 2 agentes × 5 estados, caminhos 1→5 | 6/6 partes por estado | A |
| **C. Onda 2** | 15 estados | 3 agentes × 5 estados + 1 rodada de fechamento | 6/6 partes | A (ritmo do Wayback) |
| **D. Onda 3** | 26 estados | 5 agentes × ~5 estados + 1 rodada de fechamento | 6/6 partes | A |
| **E. Federal + multi-estado + filing** | US-MQ-02, 03, 05, 09, 10, 12; EFW2 2026; POA/lote dos 51 | 2 agentes | Perguntas federais fechadas | — (corre em paralelo a B–D) |
| **F. Selar o mandato** | Consolidar shards em `legal-basis-register.csv`; scaffolder sela | 1 agente + validador de contrato | `mandate_status = sealed` | B–E |
| **G. Pesquisa dos 13 domínios** (Step 5) | O que o mandato não cobre: férias/licenças, rescisão, benefícios em espécie, penhoras, proteção de dados, mudança legislativa, etc., federal + por estado | 1 agente por domínio + por estado onde a lei varia; shards; síntese única → packs + facts por artefato; varredura de boletins 2026 | `_research/*-facts.json` validados | F |
| **H. Artefatos** | CCG → Scope → Specs → DD → WTC → SIR → Payslip → Skill → Design | Builder; **auditor ao fim de cada um** (máx. 3 rodadas); CCG em paralelo (federal, multi, 51 anexos) | Cada artefato `qa_pass` | G |
| **I. Fechamento** | Exemplos recalculados (C38), suíte externa (C37), Teste 0 ≥ 95% (C39), checks v2.12, release limpo | Auditor + scripts do pipeline (só leitura em `~/mercans-pipeline`) | `10-release/` + QA report | H |
| **J. Entrega** | Matriz xlsx, tabelas, hub `paises/EUA.md`, proposta de appends ao `shared/` da Pipeline | Eu | Resultado final | I; Drive/monday só com ok |

## 4. "Sem parar": como rodar de ponta a ponta
- **Autorização de execução contínua**: o método para depois do mandato selado (checkpoint humano do Step 4) e em toda escalada. Para não parar, o usuário precisa autorizar explicitamente o modo contínuo (`--uninterrupted`). Mesmo assim o pipeline **para** se: o auditor reprovar 3 vezes o mesmo artefato; um valor depender de decisão de negócio (ex.: provedor terceiro); algo exigir Drive, monday, ticket, e-mail ou envio.
- **Orquestração**: rodar como **Workflow** (vários agentes coordenados, retomável se cair) em vez de agentes soltos. Precisa do ok explícito do usuário ("use a workflow").
- **Máquina**: desligar a suspensão (Modern Standby derruba execuções longas sem deixar rastro) e deixar o Chrome aberto com a extensão logada.
- **Retomada**: o estado fica todo em disco (`build-manifest.json`, shards, `RUN-JOURNAL.md`); se cair, retoma do ponto, sem refazer.

## 5. Estimativa (inferência, não medição)
- Fases B–E: 3 a 4 dias de execução (o gargalo é o ritmo do Wayback e os bloqueios por país).
- Fases F–I: 3 a 5 dias (51 anexos de CCG e as Specs por estado são o grosso).
- Total: **cerca de 6 a 9 dias úteis** de execução, com o usuário acionado só nas paradas da seção 4.
- Custo: alto em tokens (dezenas de agentes por fase). Subagentes Sonnet na coleta; modelo forte só para coordenar e auditar.

## 6. Decisões do usuário para começar
1. Autoriza o modo contínuo (sem o checkpoint do Step 4)?
2. Autoriza rodar como Workflow?
3. Sessão de liberação dos domínios na extensão: quando?
4. Provedor terceiro: levar ao Marko o `PROCESSO-FILING-TERCEIROS.md` com as 6 perguntas da cotação (a escolha é dele)?

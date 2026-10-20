# Prompt: F1, extração do monday

> Usar no Claude Code (conector monday, **só leitura**: nunca criar, editar, mover ou comentar itens).
> Escopo: itens criados ou atualizados de 2026-01-01 até a data da coleta. Plano: [[PLANO]] §4, §5, §6 Fase 3 (F1). Também gera o KPI K1 (§7).
> Estrutura dos boards levantada em 2026-10-19 (pode ter mudado; conferir com `get_board_info` no início).

## Boards, nesta ordem

| # | Board (ID) | Itens (2026-10-19) | Para o brain | Colunas-chave |
|---|---|---|---|---|
| 1 | **Root Cause Analysis Tracker** (18396554143), workspace QCRM | 91 | Erros confirmados + causa + CAPA → [[correcoes]] | `name` (resumo), `dropdown_mm851w7v` Category (Internal Audit/RCA), `dropdown_mkzvjavw` Department, `text_mkztd606` Country, `text_mkztt6mq` Client, `date4` Date of Reporting, `status` (WIP/Open/CAPA In Progress/Closed), `color_mkztmvnb` Priority, `dropdown_mkzv753f` Risk Type, `link_mkzt8g9p` RCA Link, `long_text_mkzv2fp5` Email/Tickets, `long_text_mkzzb3hy` Remarks, `long_text_mm0dc4gy` Additional info. **Subitens = ações CAPA**: Owner, Action Item, Status, Department, Target Date, Evidence |
| 2 | **Compliance Statutory Alerts Tracking [2025-2026]** (18227732675) | 42 | Mudanças legislativas → hub (alerta) + [[research-pipeline]] | `name`, `status` Research Status, `color_mkyy9nh8` Development Status, `data` Date, `link_mkwxn9zk` Mercans Alert Link, `link_mkxqtp1m` Alerts 2026 Link, `link_mkxqt96v` YouTrack Task, `text_mkyxmjbm` Payroll Regulation Guide, `text_mkyyr47b` Release Note, `text_mkwx3g5j` Comments |
| 3 | **Compliance Artifacts** (7997825425) | 712, em ~80 grupos de país | Inventário de artefatos: fase, status e link → hubs "Artefatos entregues" + **alvos da F5 (Drive)** | Grupo = país; `status` Phase (Research/Design/Development/Deployment/From ICE), `status__1` Status, `link__1` Link, `text__1` Comments, `person` Owner. Subitens: Report Code, Status (incl. "Pending with Product", "Not possible"), ETA, Link |
| 4 | Compliance Research: 2026 Change Management (18392983583) | ? | Mudanças de 2026 por país | levantar no início |
| 5 | Compliance Roadmap (8084527463) | ? | Prioridade e prazos por país → painel do [[00-INDEX]] | levantar no início |
| 6 | Global Statutory Filings Tracker (9920776371) | ? | Prazos de filing → só se faltar na skill | levantar no início |

**Não coletar:** docs nominais de funcionários (ex.: "Nome | País | ID"), BAU Master Client List, On-Call Contact Directory, a sandbox "Compliance Artifacts - TEST".

## Prompt

```
F1 do PLANO: monday. Só leitura. Escopo 2026-01-01 → hoje.

PASSO 0. Estrutura
- get_board_info (columns only) nos 6 boards; registre em inventarios/monday.md qualquer diferença em relação à
  tabela de prompts/extracao-monday.md.

PASSO 1. Inventário (antes de qualquer extração)
- Para cada board, liste TODOS os itens do período (get_board_items_page com paginação, incluindo subitens
  quando o board tiver): ID, nome, grupo, status, data, país.
- RCA: marque relevância. RELEVANTE se Department = "Compliance & Research" OU algum subitem com Department
  "Compliance"/"Compliance Development" OU o resumo cita CCG/WTC/DD/spec/research/statutory/regulation.
  Os demais entram no inventário como "descartado: outro departamento" (não somem).
- Artifacts: um bloco por grupo-país. Marque os países que NÃO têm hub em paises/ (decisão 0.9 do PLANO).
- Salve em inventarios/monday.md (modelos/inventario.md). Mostre os totais e PARE para eu confirmar o escopo.

PASSO 2. Coleta bruta
- Grave o conteúdo de cada item relevante (todas as colunas + subitens + updates/comentários, via get_updates)
  em raw/monday/AAAA-MM-DD-<board>.md, um bloco por item, com o ID do item e o link.
- Os nomes de pessoas da Mercans podem ficar no raw. Nome de funcionário de cliente: substitua por [omitido].

PASSO 3. Extração em cartões (modelos/extracao.md) → extracoes/AAAA-MM-DD-monday.md
- RCA → tipo "erro+causa": o que falhou, causa raiz, o correto, ação CAPA e status. Nível B se Closed;
  C se Open/WIP. Destino: correcoes.md (se o erro foi nosso, de Compliance) ou o hub (Pendências) se não foi.
  Se o RCA Link apontar para doc do Drive, anote como alvo da F5.
- Alerts → tipo "alerta": país, legislação/mudança, vigência, status de research e de dev, PRG e release note.
  Cruze com o hub do país e com a skill: o alerta já está refletido no artefato vigente? (sim/não/[INCERTO])
- Artifacts → tipo "versão final": por país, artefato, fase, status e link. Cruze com a tabela "Artefatos
  entregues" do hub: anote as divergências (versão, status), sem corrigir ainda. Gere a lista de links
  como "alvos F5" em inventarios/drive-alvos.md.
- Change Mgmt / Roadmap / Filings → decisão, pendência ou prazo, só o que não estiver na skill.
- Chave PAÍS | ARTEFATO | ITEM em cada cartão. Antes de criar, procure a chave em correcoes.md, no hub e em
  extracoes/. Se existir, o cartão complementa ("já registrado: confirmação/fonte nova").
- Use subagentes Sonnet por board (ou por lote de países, no Artifacts). Você revisa e unifica.

PASSO 4. Validação
- Liste para mim: 100% dos cartões de risco alto (correção, valor estatutário, versão vigente divergente)
  + 10% sorteados dos demais. Espere eu marcar ✔/✘.

PASSO 5. Ingestão (só os confirmados) e fechamento
- Atualize hubs, correcoes.md, servicos/ e fronteiras conforme o destino de cada cartão (regra 2: não
  sobrescrever; a linha antiga recebe data de fim).
- Correção nova → pergunta para o Conjunto B em testes/exatidao.md.
- Métricas (cobertura, rastreabilidade, confirmação, incerteza) em inventarios/monday.md e no painel do PLANO.
- Linha no log.md, commit + push. Resumo: o que entrou · divergências · perguntas para mim.
```

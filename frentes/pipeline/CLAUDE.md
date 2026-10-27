# Frente 4 — Research Pipeline - Mercans

Esta pasta é a janela **Pipeline**. Vale tudo do `CLAUDE.md` da raiz do cérebro; aqui só o que é desta frente.

**Raiz do cérebro:** `C:\Users\instituto\Documents\brain-service` (`../..` daqui). Os caminhos abaixo são relativos à raiz, salvo `estado.md` (nesta pasta).

## Onde está o material (ligado, não copiado)
| O quê | Onde |
|---|---|
| Builds de país trabalhados à mão (Colombia, França) | `C:\Users\instituto\Documents\Research Pipeline\<País>\` |
| Pipeline (script, failure log F1–F47, checks, `<CC>-compliance`) | `C:\Users\instituto\mercans-pipeline\` (`IMPROVEMENT_LOG.md`, `shared/country_failure_log.md`) |
| Agentes e skill do pipeline | `~/.claude/agents/` (scaffolder, source-hunter, artifact-builder, qa-auditor); skill `country-build` |
| Versão vigente dos artefatos | Drive `G:\Drives compartilhados\Compliance Team\Country Folders\<País>` (linhagem do Drive prevalece sobre o pipeline) |
| Lições e backlog P0–P2 | `revisoes/2026-10-15-licoes-aprendidas/00-LICOES-CONSOLIDADAS.md` (+ `detalhado/`) |
| Padrões propostos F48–F66 | `revisoes/2026-10-09-catalogo-erros-tickets-v2.md` |
| Serviço e padrões de artefato | `servicos/research-pipeline.md` |

## Abrir a sessão (substitui o "Abrir a sessão" da raiz)
1. Ler `correcoes.md`, `frentes/pipeline/estado.md` e as últimas linhas de `log.md`.
2. Conferir no fim de `~/mercans-pipeline/IMPROVEMENT_LOG.md` e nos `.done/`/`HANDOFF.md` dos países em andamento se algo mudou desde o `estado.md`.
3. Entregar um painel curto: em andamento / esperando o usuário (decisões) / próximo do backlog.

## Trabalho
- Método: skills `mercans-pipeline-methodology` e `country-build` (build/rebuild/regressão); `mercans-artifact-toolkit` antes de mexer em xlsx/docx.
- Antes de gerar versão nova de artefato: achar a maior versão no Drive/Downloads e partir dela.
- Conhecimento de país (valor, regra, fonte com vigência) → hub `paises/<País>.md`. Erro nosso → `correcoes.md`. Lição de pipeline → atualizar `revisoes/2026-10-15-licoes-aprendidas/00-LICOES-CONSOLIDADAS.md` (backlog) e, quando aprovado, o failure log do pipeline.
- Ticket é da janela Suporte: se um ajuste de pipeline mexer em ticket, anotar em "Esperando" e avisar o usuário.

## O que esta janela escreve
- Só o seu `estado.md`, os arquivos de build em `Research Pipeline\` e `~/mercans-pipeline\`, e as revisões de lições.
- Compartilhados (`log.md`, `correcoes.md`, hubs de país, `00-INDEX.md`): seguir "Janelas paralelas" na raiz (reler antes, Edit pontual, log só no fim).
- Nada vai para o Drive, Monday ou e-mail sem ok do usuário.
- "Fecha a sessão": nota `sessoes/AAAA-MM-DD-pipeline.md` e reescrita só do `estado.md` desta pasta. Sem commit (só a janela geral commita).

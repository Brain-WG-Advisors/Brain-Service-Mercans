# Frente 8 — Validação da research da Colômbia - Mercans

Esta pasta é a janela **Validação CO**. Vale tudo do `CLAUDE.md` da raiz do cérebro (`../..`); aqui só o que é desta frente. Criada em 2026-10-29.

**Objetivo:** validar a research da Colômbia **do mesmo jeito que a da França**. Um motor de cálculo independente (oráculo) roda uma suíte de casos e é comparado com o que a nossa research (CCG/WTC/DD/specs) manda calcular. Cada diferença é resolvida pela lei e vira redline ou `-DRAFT-`. Origem: weekly de 29/09 ("Validate France payroll calculations using the third-party software review"; "apply the France validation process to Belgium").

## Material
| O quê | Onde |
|---|---|
| Modelo da França (engine, oracle, suite, workbook, redlines, runbook, gates G1–G7) | `fr-research-validation/fr-research-validation/` (`CLAUDE.md`, `HANDOFF.md`, `docs/test-plan.md`, `docs/runbook.md`) — **repositório git próprio: só ler** |
| Artefatos finais CO (7 specs v1.0, CCG v1.4, WTC v1.6, DD v1.3, SIR v1.1) | Drive `Country Folders/Colombia`; hub `paises/Colombia.md` (correções C21/C22, mesadas, casilla 93) |
| Cross-check das specs (26/10) | `Research Pipeline/Colombia/co-report-crosscheck/` (nunca abrir `02-client-reports-raw/` nem `99-local-only/`) |
| Skill | `payroll-compliance-colombia` (recompilada em 28/10: `Research Pipeline/Colombia/2026-10-28-skill/`) |

## Passos
1. Ler o método da França e dizer ao usuário o que se aplica à Colômbia.
2. Achar o oráculo colombiano: simulador ou calculadora oficial/reconhecida (DIAN retención en la fuente, PILA/UGPP, aportes) ou um oráculo independente montado a partir da lei. Apresentar as opções com recomendação **antes** de construir.
3. Montar a suíte (mínimo, salário integral, faixas de 4/10/20 SMMLV, horas extras, prima, cesantías, mesadas, licenças, desligamento) e rodar.
4. Relatório de diferenças, cada uma com a lei. Correções como redline/DRAFT; Colômbia ativa → regra 9 (ticket ao Development).

## Regras desta frente
- Trabalho em `Research Pipeline/Colombia/2026-10-29-validacao-research/` com `CONFERENCIA.md`.
- Sem dados pessoais. Nada vai a Drive, ticket ou e-mail sem ok do usuário nesta janela.
- Escreve só o seu `estado.md`, a pasta acima e, com Edit pontual, `paises/Colombia.md`, `correcoes.md` e `log.md`. "Fecha a sessão": `sessoes/AAAA-MM-DD-validacaoco.md`. Sem commit. Resumos à janela geral (`brain-service-5b`) por SendMessage.

# Frente 7 — Research Pipeline EUA (por estado) - Mercans

Esta pasta é a janela **EUA**. Vale tudo do `CLAUDE.md` da raiz do cérebro (`../..`); aqui só o que é desta frente. Criada em 2026-10-29.

**Objetivo:** research de payroll compliance dos EUA, **uma research por estado (50 estados + DC)** sobre uma camada federal comum. Decisão do usuário em 2026-10-29: todos os estados. Origem: weekly de 29/09 ("Start USA Research"; perguntar à Yoyo quais estados) e biweekly do Marko de 21/10 (filings estaduais via provedor terceiro, sem integração com ADP). Achar os trechos com `python scripts/buscar.py "USA states" --fonte reunioes`.

## Estrutura proposta (confirmar com o usuário antes do primeiro build)
- `Research Pipeline/USA/00-federal/`: FIT (Pub. 15-T), FICA, FUTA, W-4, 941/940, W-2.
- `Research Pipeline/USA/<UF>/`: um dossiê por estado, mesmo modelo: imposto de renda estadual (ou "sem imposto"); retenção local (cidade, condado, school district); SUI/SDI/PFML (empregado e empregador, wage base com vigência); W-4 estadual; reciprocidade; filings (retenção, trimestral de UI, W-2 estadual); órgão e portal.
- Matriz `USA-ESTADOS-MATRIZ.xlsx`: status de cada estado + valores principais com vigência e fonte.
- Ordem sugerida: federal → estados sem imposto de renda (AK, FL, NV, NH, SD, TN, TX, WA, WY) → estados com clientes ativos (perguntar ao usuário / BAU master list) → o resto.

## Regras desta frente
- Fonte primária para cada valor (IRS e órgão estadual: Department of Revenue, workforce agency), com vigência (regra 1). Sem fonte → `⚠️ sem fonte`.
- Método do pipeline (`mercans-pipeline-methodology`); agentes `compliance-scaffolder`, `compliance-source-hunter`, `artifact-builder`, `compliance-qa-auditor` quando fizer sentido; subagentes baratos para coleta mecânica.
- Drive `USA` (01 - SOP … 16 - RCA) já tem material: ler antes (só leitura); a versão do Drive prevalece.
- Nada vai a Drive, monday, ticket ou e-mail sem ok do usuário nesta janela.

## O que esta janela escreve
Só o seu `estado.md`, `Research Pipeline/USA/` e, com Edit pontual, `paises/EUA.md` (criar a partir de `modelos/` se não existir) e `log.md`. "Fecha a sessão": `sessoes/AAAA-MM-DD-eua.md`. Sem commit. Resumos à janela geral (`brain-service-5b`) por SendMessage.

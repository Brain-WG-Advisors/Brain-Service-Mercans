# Prompt: F6, extração do pipeline (saídas das execuções)

> Usar no Claude Code. Plano: [[PLANO]] §4, §5, §6 Fase 3 (F6). **Pré-requisito: decisão 0.7** (onde estão o pipeline e as saídas).
> O que interessa: **o resultado das execuções** (versão de cada artefato gerado, `07-qa-report.md`, resultado do audit C1–C22 e do QA cross-check, lacunas e falhas de stage). Os scripts **não** entram no brain; o método já está na skill `mercans-pipeline-methodology`.
> **Nunca copiar** `.env`, chaves de API, tokens ou config com segredo. Se a pasta tiver esses arquivos, listar só o nome e pular.

## Antes: qual cenário vale (resposta da 0.7)
| Cenário | Onde estão as saídas | Como coletar | Destino bruto |
|---|---|---|---|
| **1. Repositório git** | GitHub/GitLab (conta ou org) | `git clone` (só leitura) para `Documents\mercans-pipeline\`, fora do brain; depois `git pull` na rotina | `raw/pipeline/<Pais>/<AAAA-MM-DD>/` (cópia só dos relatórios) |
| **2. Drive** | Pasta do país no Drive "Compliance Team" | Claude in Chrome (regras de [coleta-chrome.md](coleta-chrome.md)) | `raw/drive/<Pais>/pipeline/` (fora do git) |
| **3. Outra máquina** | Disco local (ex.: `DESKTOP-TKRQLF7`) | O usuário copia a pasta de saída de cada execução para um pen drive ou pasta compartilhada; o Claude lê a cópia | `raw/pipeline/<Pais>/<AAAA-MM-DD>/` |

Antes do Passo 1, registrar o cenário em `inventarios/pipeline.md`.

## Prompt

```
F6 do PLANO: saídas do pipeline. Cenário <1|2|3>. Só leitura. Escopo: execuções de 2026-01-01 → hoje.

PASSO 1. Inventário
- Liste cada execução: país, data, versão do pipeline (vX.Y), stages concluídos (1–11), stage em que parou
  (se parou), e os arquivos de saída (CCG, WTC, DD, Specs, SIR, Payslip, 07-qa-report.md, audit, skill).
- Arquivos com segredo (.env, *key*, *token*, credentials): só o nome, marcados "pulado: segredo".
- Gravar em inventarios/pipeline.md. PARE para eu aprovar.

PASSO 2. Coleta
- Copiar para raw/ só: 07-qa-report.md, relatório do audit (C1–C22 e fixer), QA cross-check, logs de falha de stage
  e o Version Control de cada artefato gerado (não o artefato inteiro).

PASSO 3. Extração em cartões (modelos/extracao.md)
- "versão final": país, artefato, versão gerada, data e execução. Cruzar com o hub e com o monday (Artifacts).
  A versão do pipeline só é a vigente se for a de maior número (regra 8) E tiver sido promovida (sem -DRAFT).
- "erro+causa": checks que falharam e foram corrigidos pelo fixer ou à mão, falsos positivos confirmados
  (ex.: C20), notas do QA "NEEDS PATCHES" e o que foi corrigido. Nível B.
- "pendência": lacunas abertas do 07-qa-report.md que não estão no hub; stages mortos sem nova execução.
- Atualizar a "Ficha do país (da skill)" só se a skill compilada (Stage 11) for mais nova que a data de leitura da ficha.

PASSO 4. Validação (100% risco alto + 10%) → PASSO 5. Ingestão, publicação incremental, métricas, log, commit.

ROTINA (depois da primeira coleta): a cada execução nova, o ciclo reduzido (inventário da execução → cartões → validação).
No cenário 1, o "git pull" com o resumo dos commits entra na rotina semanal (prompts/rotina.md).
```

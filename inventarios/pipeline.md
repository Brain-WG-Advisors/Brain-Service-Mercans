# Inventário: F6 Pipeline

> Arquivo: `inventarios/pipeline.md`. Lista **completa** do período, feita **antes** da extração ([[PLANO]] §5, §6 F6; prompt [prompts/extracao-pipeline.md](../prompts/extracao-pipeline.md), Passo 1).
> Todo item termina como **cartão** (ID), **descartado** (motivo), **pendente** (por quê) ou **quarentena C**.
> Levantado em 2026-10-27 na sessão de migração (janela geral), **só leitura** fora do brain: nada foi aberto, movido ou copiado de `~/mercans-pipeline`.

## Escopo
- Fonte: `C:\Users\instituto\mercans-pipeline` (**cenário 3 local**: o pipeline e as saídas estão nesta máquina; decisão 0.7 atualizada em 2026-10-27) · Período: 2026-01-01 → 2026-10-27
- Critério de inclusão: execuções de país (`<CC>-compliance/`) e o `shared/` (failure log, checks, templates) · Critério de exclusão: scripts avulsos da raiz (~150 `fix_*`, `check_*`, `investigate_*` de ago–set), zips de transporte, `.bak`, `__pycache__`; o método já está na skill `mercans-pipeline-methodology`
- Consulta/filtro exato usado: `find <CC>-compliance/0*-* -maxdepth 2 -type f (xlsx|docx|SKILL.md)`, sem `.bak`/archive; data = arquivo mais recente
- Aprovado pelo usuário em: 2026-10-27 (Passo 1 ✅; próximo: Passo 2, coleta dos relatórios para `raw/pipeline/`)

## Pipeline nesta máquina
| Item | Valor |
|---|---|
| Pasta | `C:\Users\instituto\mercans-pipeline` (repo git próprio, **sem remote**: única cópia) |
| Script vigente | `mercans_pipeline_v2_12.sh` (2026-10-17). Antigos: `_backup/script-history/`, `_backup/v2.11-2026-10-17/`, `_backup/v2.12-pre-portability-2026-10-17/`, `Downloads\mercans_pipeline_v2_4.sh` e `v2_9.sh` |
| Último commit | `6b6cffb` Pipeline v2.12: correções da validação FR (P0–P2), portabilidade e pacote para o time |
| Sem commit | 13 alterações em `dist/v2.12/` (ANNOUNCEMENT.md, chat/Automation, chat/mercans-compliance-workflow, SKILL.md e battle-tested-lessons.md editados, 2 zips de chat apagados) |
| Failure log | `shared/country_failure_log.md`: 61 entradas `F<n>`, última **F74** (o PLANO/MIGRACAO citavam F1–F37) |
| shared/ | Global_WTC_V1_0, CZ DD V2_0, CZ WTC V2_0, REFERENCE_CCG_Bulgaria, REFERENCE_Payslip Mozambique/Tunisia, scope_manifest_template, fact-keys.yaml; guias PRESUBMISSION_AUDIT, QA_METHODOLOGY_BAKE_IN, CCG-Playbook-Learnings, CCG_TEMPLATE_QUESTIONS, SHARED_TEMPLATES_GUIDE_v2_1, country_portal_registry; pastas de checks, validators, schemas, spec-builder, templates, pilot, release, `_test-runs` |
| Outros | `IMPROVEMENT_LOG.md` (2026-10-17), `PIPELINE_IMPROVEMENT_PROMPT.md`, `pipeline.config.example`, `dist/v2.12/`, `skills-build/` |
| Claude Code | `.claude/settings.local.json` (não aberto); sem CLAUDE.md. Memória do projeto (5 notas) copiada em `raw/memoria-claude-code/mercans-pipeline/` (2026-10-26) |
| Segredo (pulado) | `FR-compliance/integration-sources/dgfip-edi/_raw/.../*.pem` (4 arquivos de chave do pacote técnico DGFiP EDI): só o nome. Os `P2-enrolment-access-credentials.md` (DGFIP-EDI, NETENT-DSN, URSSAF-DPAE) são capítulos de spec, a conferir no Passo 2 antes de copiar |

## Métricas
| Métrica | Valor | Meta |
|---|---|---|
| Itens no inventário | 4 | — |
| Cobertura ((cartão + descartado) ÷ itens) | 0% | 100% |
| Rastreabilidade (cartões com caminho em raw ÷ cartões) | — | 100% |
| Confirmação humana (✔ ÷ amostra) | — | ≥ 95% |
| Incerteza ([INCERTO] ÷ cartões) | — | acompanhar |

## Itens
| # | ID/link | Título | Data | País | Estado na fonte | Arquivo em raw/ | Resultado | Cartão / motivo |
|---|---|---|---|---|---|---|---|---|
| 1 | `BE-compliance/` | Build Bélgica: CCG v1.2, WTC v1.1, SIR v1.0, 8 specs (NSSO 001–005, FIN 001–002, FEDRIS 001), DD v1.4, Payslip Generator, skill; QA `BE-QA-REPORT-FINAL2-2026-08-24.md` | 2026-09-29 | BE | stages 00–08 com saída; stages 9.5–12b em notas da raiz (`BE_stage*.md`, PROPAGATION-LEDGER) | `raw/pipeline/Belgica/2026-10-27/` (qa 22, logs 66, notas 12, VC 12/14) | pendente | Passo 3 (cartões) |
| 2 | `CO-compliance/` | Build Colômbia: CCG v1.2, WTC v1.4, SIR-INDEX v1.0, 6 specs (DIAN 001/002/004/005, PILA 003, CESANTIAS 006), DD v1.0, Payslip v1.1, skill; QA `CO-QA-REPORT.md`; `colombia-artifacts-20261026-1016.zip` (origem a confirmar) | 2026-10-26 | CO | stages 00–08 com saída; as versões vigentes (CCG v1.4, WTC v1.6, DD v1.3) estão no brain (`Research Pipeline/Colombia/`) e no Drive, **não** aqui | `raw/pipeline/Colombia/2026-10-27/` (qa 5, logs 21, VC 12/13) | pendente | Passo 3 (cartões); divergência máquina × Drive (PLANO §13) |
| 3 | `FR-compliance/` | Build França: CCG v1.0, WTC v1.0, SIR-INDEX v1.0, 8 specs (DSN 001–003, URSSAF 001–004, DGFIP 003), DD v1.0, Payslip Generator, skill, 09-design; QA `FR-QA-REPORT-v4-20260903.md`; `_validation/`, `PROMOTION-LOG-2026-10-06/09` | 2026-10-09 | FR | stages 00–09 com saída; finais promovidos (D6: finais FR = arquivos do pipeline); DD final de 2026-10-26 veio de `fr-research-validation/` | `raw/pipeline/Franca/2026-10-27/` (qa 12, logs 32, notas 2, VC 19/20) | pendente | Passo 3 (cartões) |
| 4 | `shared/country_failure_log.md` | Failure log F1–F74 (61 entradas) | 2026-10-17 | — | v2.12 | `raw/pipeline/_shared/2026-10-27/country_failure_log.md` | pendente | Passo 3 (cartões); erros/causas → `correcoes.md` (Fase 4) |

### Coleta (Passo 2, 2026-10-27)
- Copiado só: relatórios e revisões de QA (`07-qa-crosscheck/*.md|*.json`, sem `.bak`), resultados do audit (FR: `c1_result`, `c1b_result`, `audit_recheck_artifactfix`), `logs/` (inclui `FACT-CONFLICTS`), notas de stage/promoção da raiz e o **Version Control** de cada artefato (`version-control/`, extraído; não o artefato). 172 cópias + failure log, todas com md5 igual à origem (`MANIFEST-coleta.md` de cada país). Origem não alterada (`git status` do pipeline igual: 13).
- Sem Version Control: os 3 **Payslip Generators** (não têm aba de versão) e o **BE-CCG-001-v1.2** (sem tabela; só a linha "Version 1.2 — 16 September 2026 (supersedes version 1.1 of 21 August 2026)"). Achado para o Passo 3.
- Não copiado: artefatos inteiros, `_work/`, `_final_qa/corpus/`, `_align/`, backups, scripts, `integration-sources/` (inclui os `.pem`) e os `P2-enrolment-access-credentials.md` (fora da lista do Passo 2).

Saídas dos testes YY/ZZ (2026-09-11) e do Canadá (Mac) não estão nesta máquina.

## Pendências do inventário
- ~~Aprovar este inventário (Passo 1)~~ aprovado em 2026-10-27.
- Origem do `CO-compliance/colombia-artifacts-20261026-1016.zip`.
- Repo `~/mercans-pipeline` sem remote e com 13 alterações sem commit: registrado (2026-10-27), sem ação por ora.
- ~~Conferir os `P2-enrolment-access-credentials.md` da FR antes do Passo 2~~: não copiados (fora da lista do Passo 2).
- Passo 3: cartões "versão final", "erro+causa" e "pendência" ([modelos/extracao.md](../modelos/extracao.md)), cruzando com hubs e monday.

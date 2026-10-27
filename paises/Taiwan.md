---
tipo: pais
codigo: "TW"
etapa_research: "aguardando"
etapa_research_data: 
etapa_design: "em andamento"
etapa_design_data: 2026-10-27
etapa_producao: 
etapa_suporte: "6 aberto(s): SR-105, SR-106, SR-107, SR-108, SR-109, SR-110"
etapa_suporte_data: 2026-10-27
ccg: 
ccg_data: 
wtc: v2.8
wtc_data: 
dd: v3.3
dd_data: 
report_specs: "SR-105/106/107 v1.1; SR-108 v1.2; SR-110 v1.3"
report_specs_data: 2026-10-27
sir: 
sir_data: 
payslip: "v1.2"
skill: 
tickets_abertos: 6
tickets_conferidos_em: 2026-10-27
versoes_fonte: "nome do arquivo no Drive (Country Folders/Taiwan), lido em 2026-10-27; sem data de versão"
atualizado_em: 2026-10-27
---
# Taiwan

> Hub do país. Índice: [[00-INDEX]] · Skill: não há · Correções: [[correcoes]] · Fronteiras: [[fronteiras]]

Hub criado em 2026-10-27 (Fase R, revisão do grafo) a partir das conferências dos SR-105 a SR-110. Ainda não tem ficha da skill nem histórico anterior a 2026-10.

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ⏳ | | sem registro no cérebro |
| [[design]] | 🔄 | 2026-10-27 | Specs de relatório revisadas (SR-105 a SR-110), Draft local, nada publicado |
| Produção (outro time) | — | | |
| [[suporte]] | 🔄 | 2026-10-27 | API 27/10: abertos: SR-105 Open, SR-106 Open, SR-107 Open, SR-108 In Review, SR-109 In Review, SR-110 In Review. Antes (2026-10-27): SR-105 a SR-110 resolvidos e arquivados, sem publicar |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| Specs LI/NHI/LP 3-em-1 (SR-105/106/107) | v1.1 Draft | 2026-10-27 | `Research Pipeline/Taiwan/2026-10-27-SR-105-106-107-3in1/` | só local |
| Spec SNHI (SR-108) | v1.2 Draft | 2026-10-27 | `Research Pipeline/Taiwan/2026-10-27-SR-108-SNHI/` | só local |
| Spec Payslip (SR-109) | v1.2 Draft | 2026-10-27 | `Research Pipeline/Taiwan/2026-10-27-SR-109-Payslip/` | só local |
| Tax Report Spec (SR-110) | v1.3 Draft | 2026-10-27 | `Research Pipeline/Taiwan/2026-10-27-SR-110-TaxReport/` | só local |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| | | | | |

## Decisões
- 2026-10-27: SR-105 a SR-110 resolvidos e arquivados localmente; nada no Drive nem no ticket até o ok do usuário ([[log]]).

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| 2026-10-27 | SR-105, SR-106, SR-107 | Revisão das specs 3-em-1 (LI/NHI/LP) contra o formato oficial (pedido do Mohit de 15/09: "Spec Review only and fill the gaps") | v1.1 Draft local | sim (Draft) |
| 2026-10-27 | SR-108 | SNHI, bônus (NHIA tipo 62) | v1.2 Draft local | sim (Draft) |
| 2026-10-27 | SR-109 | Payslip | v1.2 Draft local | sim (Draft) |
| 2026-10-27 | SR-110 | Tax Report | v1.3 Draft local | sim (Draft) |

## Entregas (conferências)
- 2026-10-27 · SR-105/106/107 · specs 3-em-1 v1.1: [[Research Pipeline/Taiwan/2026-10-27-SR-105-106-107-3in1/CONFERENCIA|conferência]]
- 2026-10-27 · SR-108 · SNHI v1.2: [[Research Pipeline/Taiwan/2026-10-27-SR-108-SNHI/CONFERENCIA|conferência]]
- 2026-10-27 · SR-109 · Payslip v1.2: [[Research Pipeline/Taiwan/2026-10-27-SR-109-Payslip/CONFERENCIA|conferência]]
- 2026-10-27 · SR-110 · Tax Report v1.3: [[Research Pipeline/Taiwan/2026-10-27-SR-110-TaxReport/CONFERENCIA|conferência]]

## Pendências
Achados fora do pedido, registrados nas conferências (não foram para os tickets):
- [ ] **WTC V2.8, 58009:** soma as séries 6222x e 6221x e deixa fora a 6220x (bônus anual). Se o 2558 seguir o 58009, o 年終獎金 não paga suplementar. Fonte: [[Research Pipeline/Taiwan/2026-10-27-SR-108-SNHI/CONFERENCIA|SR-108]].
- [ ] **WTC V2.8 sem PE para alguns casos** (fonte: [[Research Pipeline/Taiwan/2026-10-27-SR-109-Payslip/CONFERENCIA|SR-109]]):
  - trabalho em 例假 ou folga suspensa por emergência;
  - horas de 補休 vencidas pagas em dinheiro;
  - PEs 621xx de overtime genéricos;
  - a faixa 65500:65859 inclui benefícios nocionais no Total Gross.
- [ ] **Erro nosso:** a análise de 23/10 citou LSA art. 38 §4 para o registro de 特休. O certo é o **§5**. Entra em [[correcoes]] no fechamento da sessão da janela Suporte (fonte: SR-109).
- [ ] **Teste do Jani (29/01/2026):** foi feito numa entidade da Índia. Retestar na entidade de Taiwan (SR-109).
- [ ] **Achados do SR-110** (fonte: [[Research Pipeline/Taiwan/2026-10-27-SR-110-TaxReport/CONFERENCIA|SR-110]]):
  - a mudança de não residente para residente no mesmo ano não está prevista na spec;
  - DD V3.3, Identity Type: os rótulos EN das keys 4 e 6 estão errados;
  - o SOP Taiwan 1.1 traduz o campo 9 como "tax exemption", o que está errado;
  - o prazo do 扣繳憑單 é 10/02, ou **15/02** se janeiro tiver 3 ou mais feriados (ITA art. 92).

## Correções ligadas
- _(links para entradas de [[correcoes]])_

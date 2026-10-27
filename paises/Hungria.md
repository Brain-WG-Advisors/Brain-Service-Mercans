---
tipo: pais
codigo: "HU"
etapa_research: "em andamento"
etapa_research_data: 2026-06-30
etapa_design: "concluida"
etapa_design_data: 2026-06-25
etapa_producao: 
etapa_suporte: "sem ticket no hub"
etapa_suporte_data: 
ccg: v1.0
ccg_data: 
wtc: v1.0
wtc_data: 
dd: v1.0
dd_data: 
report_specs: "sem versão no hub"
report_specs_data: 2026-06-25
sir: v1.0
sir_data: 
payslip: v2.0
skill: 
tickets_abertos: 
tickets_conferidos_em: 
payslip_data: 
versoes_fonte: "nome do arquivo no Drive (Country Folders/Hungary), lido em 2026-10-27; sem data de versão"
obs_versoes: "WTC vazio→v1.0 (HU-WTC-001-v1_0.gsheet; versão com sublinhado, 2ª leitura do Drive)"
atualizado_em: 2026-10-27
---
# Hungria

> Hub do país. Índice: [[00-INDEX]] · Skill: não há

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | 🔄 | 2026-06-30 | Artefatos de integração (SIR) aguardando feedback do Ilia (Integration/Config Factory); Manju vai gerar artefatos de integração da Hungria |
| [[design]] | ✅ | ~2026-06-25 | Design do dev team (Suman Rai) finalizado; report specs em andamento (Suman); design "new track pattern" (Wallisson) pedido em 2026-07-10, a fazer |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | sem tickets nas fontes |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| Design HU (dev team, Suman Rai; regs 9348011–061) | — | ~2026-06-25 | SR-A-1 | Finalizado |
| SR-A-5 (SR-A-1 convertida ao formato artigo) | — | upload 2026-09-10 | SR-A-5 | [INCERTO] status; diverge da SR-A-1 |
| Report specifications HU | — | 2026-06-25 | — | Em andamento (Suman) |
| Artefatos de integração (SIR) | — | 2026-06-30 | — | Aguardando feedback do Ilia |
| Design "new track pattern" (Wallisson) | — | pedido 2026-07-10 | — | A fazer, para a Manju comparar |

## Valores-chave (com vigência)
> Valores registrados nos docs/transcrições (chat: design-dev-kb); ⚠️ sem fonte legal explícita, vigência 2026 (hu_2026).

| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| PIT / SS EE / Szocho | 15% / 18,5% (pensionista 8,5%) / 13% ER, inclusive sobre BIK | 2026 | | SR-A-1/SR-A-5; reunião 2026-05-29 |
| Composição dos 18,5% | [INCERTO] "pension ~10 + health ~7 + 1,5" (27/05) vs "15 + 4 aprox." (29/05) | — | | transcrições |
| Tetos de isenção | <25 anos 8.589.180; deficiência 1.291.200; 1º casamento 400.020; healthcare 147.600 | 2026 | | SR-A-5 |
| Family allowance por dependente | solo 133.340 / 266.660 / 440.000; conjunto 66.670 / 133.330 / 220.000 | 2026 | | SR-A-1/SR-A-5 |
| Family allowance (transcrição) | [INCERTO] 10.000 / 20.000 / 33.000 por filho, "a verificar" (conflita com SR-A) | — | | reunião 2026-05-29 |
| SZÉP / habitação / EMJ | BKJ 450.000; Aktív 120.000; habitação <35 anos 1.800.000; EMJ base x1,18 | 2026 | | SR-A-1/SR-A-5 |
| Piso SS | 96.840 (30% do mínimo, por dia) | 2026 | | SR-A-5 |
| Crédito Szocho | 503.568 / 251.784; trabalhador não qualificado 50% | 2026 | | SR-A-1 |
| 3º filho (isenção 3+ filhos) | nascido a partir de 2025-10-01 | 2025-10-01 | | reunião 2026-05-26..29 |

## Decisões
- 2026-05-26: ID `9348xxx`; começa com Gross Salary em 58008; flag Mother<30 em 58205; idade contra `$period.begin_date` — padrão universal — Suman/Mohit (chat: design-dev-kb)
- 2026-05-26: isenções complexas por declaração (empregado declara, empregador aprova, sistema aplica); só o término é automatizado — Manju, "authoritative" (chat: design-dev-kb)
- 2026-05-27: dependente no dependent screen conta como declarado; flags 0/1 em ordinais anteriores; isenção credita contra 58008; under-25 com idade no fim do período — Suman/Manju (chat: design-dev-kb)
- antes de 2026-05-27: módulo de pagamento de benefício de SS pelo empregador (100+ empregados) não será construído; entra como input de gross — escopo do produto — Marko Taylor + compliance (chat: design-dev-kb; ver [[fronteiras]])
- 2026-05-29: nacionalidade/residência numa flag única reusada (`$58218`, igual ES); under-25 aplicado por padrão com flag de opt-out — Suman/Manju (chat: design-dev-kb)
- 2026-07-10: Wallisson faz design HU "new track pattern" para a Manju comparar (chat: design-dev-kb)

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| — | _(nenhum ticket HU nas fontes)_ | | | |

## Pendências
- [ ] Gerar artefatos de integração da Hungria e retornar o feedback do Ilia — Manju/Wallisson — (chat: compliance-research)
- [ ] Definir a data do portão de idade (`$legal_entity.tax_yearend_date` vs 31/12 fixo) e Under-40 — Mohit — (chat: design-dev-kb)
- [ ] Flag vs inline; nacionalidade + residência (CCG p.38); validar isenção de 3 filhos; verificar valores de family allowance — Suman/Mohit — (chat: design-dev-kb)
- [ ] Workflow de aprovação de declarações (fronteira HRB x engine) e se o componente de pensão de 10% depende de config do cliente — Aberto — (chat: design-dev-kb)
- [ ] Reconciliar SR-A-1 com SR-A-5 (bandas riscadas 9348055; bandas 8 de 9348021 e 7 de 9348059; regs 9348044–046 GYED; contas 6035/2535 vs 6037/2537; "MUTLIPLY" em 9348053; 58130 com dois usos) — (SR-A-1, SR-A-5) [INCERTO]
- [ ] Ajustar as report specs — Suman — (chat: design-dev-kb)
- [ ] Design "new track" — Wallisson — (chat: design-dev-kb)
- [ ] Under-25 (Szja tv. 29/F (3)): a isenção vale até o mês do 25º aniversário inclusive (NAV nº 73, 2026-03-19); o design com idade na `end_date` (entrada de 2026-05-27) tira esse mês → corrigir o regulation design. Ver [[correcoes]] 2026-10-27.

## Correções ligadas
- [[correcoes]]: design HU com under-25 por idade no begin_date, nacionalidade só com `CONTAINS` e `$employee.years_worked` como idade; correto end_date, nacionalidade e residência (`$58218`) em flag única e `$person.birth_date` (T-2026-05-27/29)

## Fontes
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- raw/chats/2026-10-01-compliance-research.md

---
tipo: pais
codigo: "IN"
etapa_research: "aguardando"
etapa_research_data: 
etapa_design: "em andamento"
etapa_design_data: 2026-08-20
etapa_producao: 
etapa_suporte: "sem ticket no hub"
etapa_suporte_data: 
ccg: v1.0
ccg_data: 
wtc: v3.7
wtc_data: 
dd: v2.3
dd_data: 
report_specs: 
report_specs_data: 
sir: v1.0
sir_data: 
payslip: 
skill: 
tickets_abertos: 
tickets_conferidos_em: 
versoes_fonte: "nome do arquivo no Drive (Country Folders/India), lido em 2026-10-27; sem data de versão"
atualizado_em: 2026-10-27
---
# Índia

> Hub do país. Índice: [[00-INDEX]] · Skill: não há · Correções: [[correcoes]] · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ⏳ | | [INCERTO] sem pesquisa IN registrada |
| [[design]] | 🔄 | ~2026-08-20 | Global WTC Taxability Display (566 PEs x 10 regulations) entregue; 9356204 a confirmar; design IN (CT-A-632) citado nas lacunas |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | sem tickets; 1 dúvida de design pendente com o cliente |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| Global WTC Taxability Display | 2 cópias, só a formatação muda | ~2026-08-20 | Global_WTC_Taxability_Display | 566 PEs x 10 regulations; Tax 9356046 (566 PEs) / 9356051 (60); SS 9356631 ESI (111); pre-tax 9356071, 136, 156, 176, 196, 201, 204 |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| HRA | MIN(HRA; aluguel − 10% do salário; 40% / 50% metro) | ⚠️ vigência? | | ⚠️ sem fonte (reunião 2026-05-22) |
| "Wages" (base do PF) | Inclui básico, DA, retaining allowance e demais allowances; exclui, entre outros: (d) conveyance/travelling concession (LTA), (e) despesas especiais do trabalho, (f) HRA, (h) overtime, (i) comissão. 1º proviso: excluídos (a)–(i) acima de 50% da remuneração total voltam para wages | Code em vigor desde 2025-11-21 ⚠️ data só em fonte secundária (Taxmann) | | Code on Social Security 2020, s. 2(88) (`raw/docs/oficiais/IN/2026-10-28-Code-on-Social-Security-2020_Act36_PRS.pdf`, p. 12–13) |
| PF: contribuição | 10% do empregador + 10% do empregado; 12% nos estabelecimentos notificados; EPS até 8,33% dos wages | ⚠️ vigência = a do Code | | Code on Social Security 2020, s. 16(1)(a)–(b) (mesmo PDF) |
| PF: wage ceiling | INR 25.000/mês (antes 15.000) | 2026-09-17 | | ⚠️ só fonte secundária: S.O. 5109(E) citada por KPMG; EPFO bloqueado do Brasil |

## Decisões
- 2026-05-22: HRA calculado como MIN(HRA; aluguel − 10% do salário; 40% / 50% metro) — discutido no design — time de design (T-2026-05-22) [INCERTO quem decidiu]

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| ~2026-08-20 | — | 9356204 Food Allowance referencia 58167, que não existe no Global WTC | Confirmar com o cliente; pendente | Pendente |
| 2026-10-28 | HRBS-16568 (Omnicom, Ankit/Crina; não é nosso ticket) | PF sobre arrears não calculado: 58573 roda no input stage, arrears só existem no cálculo; 62551/62631/62701/62751 sem "Apply Arrears" (análise do Talgat) | Engine/config → time do Mohit (fronteiras l. 9, 11, 13, 14). À Crina só o escopo; a posição legal foi retirada porque o design atual (Drive `07 - Design/Regulations_Specific_IDs_Articles.md`, 18/08/2026) põe todos os arrears (incl. LTA 62551, helper 62631, books 62701, uniform 62751) em 58103, que vira a base do EPF em 9356244 (58100 < 15.000 e 58200 = 1, teto 15.000 × 63954) — afirmar "LTA não é PF wage" contradiria o design em pleno incidente | Não |

## Pendências
- [ ] Confirmar com o cliente a referência 58167 do 9356204 Food Allowance — Cliente/Design — (chat: design-dev-kb)
- [ ] Consolidar as duas cópias quase idênticas do WTC Display — a definir — (chat: design-dev-kb)
- [ ] Conferir o design do PF sobre arrears contra o Code on Social Security, s. 2(88): 9356021 (58103) soma LTA, helper, books & periodicals e uniform, e 9356244 usa 58103 inteiro como base do EPF (até o teto) para quem tem básico < 15.000; a lei exclui travelling concession (d) e despesas do trabalho (e), salvo o proviso dos 50%. Também: tetos 15.000 nas bandas (lidos no export de 18/08) × 25.000 desde 17/09/2026 (⚠️ fonte secundária; FAQ da EPFO está no Drive `14 - Legislation/EPFO_Wage_Ceiling_FAQs.pdf`). Levar ao Mohit depois do incidente HRBS-16568 — Wallisson — (HRBS-16568, 2026-10-28)

## Correções ligadas
- _(nenhuma)_

## Fontes
- raw/chats/2026-10-01-mercans-design-dev-kb.md

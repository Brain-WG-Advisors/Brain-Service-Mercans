---
tipo: pais
codigo: "BG"
etapa_research: "concluida"
etapa_research_data: "2026-08"
etapa_design: "concluida"
etapa_design_data: 
etapa_producao: 
etapa_suporte: "sem ticket no hub"
etapa_suporte_data: 
ccg: "sem versão no hub"
ccg_data: 
wtc: "v2.2"
wtc_data: "2026-08"
dd: "v2.1"
dd_data: 
report_specs: 
report_specs_data: 
sir: 
sir_data: 
payslip: 
skill: 
tickets_abertos: 
tickets_conferidos_em: 
atualizado_em: 2026-10-27
---
# Bulgária

> Hub do país. Índice: [[00-INDEX]] · Skill: não há

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | snapshot 2026-08 | WTC V2.2 (códigos de renda Art.73 preenchidos); CCG BG-CCG-001 é o "padrão-ouro" de CCG. Parâmetros do orçamento 2026 ainda transitórios. |
| [[design]] | ✅ | — | BG_Design.xlsx + bg.json (28 regs, 9100xxx) em produção; país de referência para o formato artigo + JSON |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | sem tickets nas fontes |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| CCG BG-CCG-001 | sem versão citada | — | — | Padrão-ouro de CCG (13 módulos) (chat: mercans-compliance) |
| WTC BG | V2.2 (vigente: maior versão) | snapshot 2026-08 | — | Códigos de renda Art.73 preenchidos. Histórico: o design foi feito sobre a V2.1 |
| DD BG | V2.1 (base do design) | — | — | |
| BG_Design.xlsx + bg.json | — | — | KB_Bulgaria_Design_* | 28 regs, 9100xxx; Produção |
| Análise de padrões BG (P1–P11) | — | — | KB_Bulgaria_Design_Pattern_Analysis | Referência de design |

## Valores-chave (com vigência)
> Conteúdo completo: não há skill BG. Valores abaixo vêm do design (chat: design-dev-kb) e podem estar transitórios.

| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| Taxa fixa do Euro | 1,95583 BGN/EUR | 2026-01-01 | | ⚠️ sem fonte (chat: mercans-compliance) |
| Base segurável | piso 620,20; teto 2.111,64/mês | ⚠️ vigência? (2026) | | KB_Bulgaria_Design_BG_Design_and_JSON |
| Máx. segurável do orçamento 2026 | EUR 2.352 | pendente | | [INCERTO] "ainda pendente" no snapshot 08-2026; parâmetros transitórios (2025 convertidos); +2% pensão também pendente |
| Contribuições | DOO 6,58/8,22 (cat. 3: 2,20/2,80); PPF ER 12% / 7%; Teachers 4,3%; UPF 2,20/2,80; GDM 1,40/2,10; desemprego 0,40/0,60; NHIF 3,20/4,80; TZPB 0,40–1,10%; GVRF 0% | ⚠️ vigência? (2026) | | KB_Bulgaria_Design_BG_Design_and_JSON |
| PIT e alívios | PIT 10%; por filho 3.067,75 (6.135,50 com deficiência); voluntário até 10% | ⚠️ vigência? (2026) | | KB_Bulgaria_Design_BG_Design_and_JSON |
| Deficiência (alívio) | [INCERTO] 3.930 (design) vs 660/mês = 7.920/ano (análise) | — | | KB_Bulgaria_Design_Pattern_Analysis |
| Arredondamento SS | 2 casas por componente | ⚠️ vigência? | | CCG 1.5 |

## Decisões
- antes de 2026-08: Apêndice 9 (e-bolnichni) e Apêndice 10 (UP-2) fora de escopo — benchmark com SAP SF, Workday, Papaya, Remote, Playroll, Leinonen: nenhum trata como output de folha — Team Lead (chat: mercans-compliance)
- 2026-05-22: 1 regulation step = 1 artigo YouTrack, convertível em JSON; matriz embutida no artigo de gross taxable; BG é a referência — Mohit/Dev (chat: design-dev-kb)
- Padrão: pesquisa em cirílico rende mais (chat: mercans-compliance). Juros de hipoteca de famílias jovens e doações ficam fora da folha (chat: design-dev-kb; ver [[fronteiras]])

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| — | _(nenhum ticket BG nas fontes)_ | | | |

## Pendências
- [ ] Criar o PE 52531 — a definir — (chat: design-dev-kb)
- [ ] Piso e teto do TZPB variam por empregado? — Wallisson — (chat: design-dev-kb)
- [ ] GVRF 6031/2531 (sobreposto ao GDM) — a definir — (chat: design-dev-kb)
- [ ] Parâmetros do orçamento 2026: máx. segurável EUR 2.352 e +2% pensão pendentes — Research — (chat: mercans-compliance)
- [ ] [INCERTO] Pattern #7 cita 52980 como taxa do TZPB; os docs indicam 52560; teto voluntário `$21640` (conta ou valor?)
- [ ] [INCERTO] alívio de deficiência 3.930 vs 7.920/ano

## Correções ligadas
- [[correcoes]]: Pattern #7 citava 52980 como taxa do TZPB; correto 52560 (demais itens a verificar) (KB_Bulgaria_Design_*)

## Fontes
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- raw/chats/2026-10-01-mercans-compliance.md

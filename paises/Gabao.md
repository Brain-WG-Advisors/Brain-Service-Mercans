---
tipo: pais
codigo: "GA"
etapa_research: "em andamento"
etapa_research_data: 2026-09-23
etapa_design: "aguardando"
etapa_design_data: 2026-08-25
etapa_producao: 
etapa_suporte: "sem tickets abertos"
etapa_suporte_data: 2026-10-27
ccg: 
ccg_data: 
wtc: "v3.1"
wtc_data: 2026-09-23
dd: 
dd_data: 
report_specs: 
report_specs_data: 
sir: 
sir_data: 
payslip: "sem versão no hub"
skill: 
tickets_abertos: 0
tickets_conferidos_em: 2026-10-27
atualizado_em: 2026-10-27
---
# Gabão (Gabon)

> Hub do país. Índice: [[00-INDEX]] · Skill: não há · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | 🔄 | 2026-09-23 | WTC GA-WTC-001 v3.1 DRAFT (HRBS-14978); pesquisa estatutária registrada no chat; sem skill [INCERTO se CCG/DD existem] |
| [[design]] | ⏳ | 2026-08-25 | Design novo (Manju) pedido em 2026-08-25, "a fazer" (chat: design-dev-kb) |
| Produção (outro time) | — | | |
| [[suporte]] | ✅ | 2026-10-27 | API 27/10: 3 fechado(s): HRBS-12472, HRBS-14943, HRBS-14978. Antes (2026-09-23): HRBS-14978 (WTC v3.1 DRAFT), HRBS-14943 (resposta, sem mudança), HRBS-12472 (payslip) |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| WTC Gabão | v3.1 DRAFT | 2026-09-23 | `GA-WTC-001-v3.1-DRAFT-HRBS-14978-2026-09-23.xlsx` | v3.0 sem o bloco de deduções Global 21100–21900 e de ER 23640–23673 (59 códigos); adicionados na v3.1. Filtro salvo na coluna A (só 8 códigos) limpo; VC ganhou a linha 3.1 (chat: mercans-compliance) |
| Payslip Gabão | — | ~2026-08-10 | — | Exibirá estado civil e nº de partes; nº de filhos não (HRBS-12472) |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| CNSS: PVID 16% (EE 5% / ER 11%), PF 5% ER, AT/MP 2% ER; ER total 18%; teto 1.500.000 XAF/mês | ver coluna | 2026-01-01 | — | Décret n°0487/PR/MASI de 2025-12-18 (chat: mercans-compliance) |
| CNAMGS | EE 2% / ER 4,1%; teto 2.500.000 XAF/mês | ⚠️ vigência? ("vigente") | — | CLEISS 2026; decreto de 2016-12-22 (chat: mercans-compliance) |
| TCS | 5% sobre a base após dedução de 150.000 XAF | ⚠️ vigência? ("vigente") | — | Business Consulting Gabon (chat: mercans-compliance) |
| Base de IRPP | Bruto − CNSS − CNAMGS − TCS; abatimento de 20% com teto de 10 milhões XAF/ano | ⚠️ vigência? ("vigente") | — | PwC WWTS (2026-08-06) (chat: mercans-compliance) |
| CFP (training levy), ônus do empregador | 0,50% do bruto até 1.500.000 XAF (máx. 7.500 XAF/mês) | 2017-01-01 | — | Loi n°026/2016 (LF 2017) arts. 5–12 (chat: mercans-compliance) |
| FNH | 2% ER (pré-LFR 2026) | ⚠️ vigência? | 2026-06 [INCERTO] | CGI arts. 401–404 |
| FNH, LFR 2026 | 3% sobre a remuneração CNSS até o teto; split e início dependem de texto regulamentar | 2026-07 (LFR 2026) | — | Loi n°002/2026; CGI arts. 401–404 (chat: mercans-compliance) |

## Decisões
- 2026-09-23: separar o CNSS ER em três elementos (PVID 11% / PF 5% / AT-MP 2%), para cada linha do cliente ter um elemento; os 18% combinados já estavam conformes; números de código são proposta do time, a confirmar na plataforma — Team Lead (HRBS-14978; chat: mercans-compliance)
- 2026-09-23: 21640–21645 (pensão voluntária EE) tratados como pós-imposto, pois não foi encontrado alívio de IRPP — decisão a confirmar (chat: mercans-compliance)
- 2026-09-23 (HRBS-14978): deduções Global são obrigatórias; BIK precisa de dedução não-caixa; ajustes são operacionais; Parts 1/2/3 = três ramos CNSS ER — fontes Décret 0487/2025; CLEISS; PwC (chat: mercans-compliance)
- ~2026-09 (HRBS-14943): a linha "OPRAG/FNE Training Levy 1%" do cliente não existe no Gabão; a linha correta é o CFP 0,5% (OPRAG = autoridade portuária; FNE 1% é de Camarões). Sem mudança de artefato — Loi 026/2016; Loi 90/050 (CM) (chat: mercans-compliance)
- ~2026-08-10: payslip do Gabão mostrará estado civil e nº de partes; nº de filhos não é mencionado nem exigido, e a justificativa do cliente foi pedida — Manju Shetija (HRBS-12472)
- 2026-08-25: Gabão entra na leva de designs novos (Manju); automação de design começa por países pequenos — Manju/Mohit (chat: design-dev-kb)

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| 2026-09-23 | HRBS-14978 | Faltam códigos de dedução (normal/BIK), ajuste e "SS Company part 3" | Parts 1/2/3 = três ramos CNSS ER; deduções Global obrigatórias; WTC v3.1 DRAFT | Sim: WTC v3.1 DRAFT |
| ~2026-09 [INCERTO data] | HRBS-14943 | "OPRAG/FNE Training Levy 1%" (blocker) | Não existe no Gabão; é o CFP 0,5% | Não |
| ~2026-08-10 | HRBS-12472 | Payslips Congo e Gabão: estado civil, nº de filhos, nº de partes | Gabão: exibirá estado civil e partes; filhos não exigido, justificativa pedida (ver [[Congo]]) | Não (decisão de exibição) |

## Pendências
- [ ] Taxa e split do FNH, quando sair o texto regulamentar da LFR 2026 — Compliance (chat: mercans-compliance)
- [ ] 62890 Stock options com No/No/No (PwC trata como tributável) — Compliance (chat: mercans-compliance)
- [ ] Confirmar na plataforma os números de código novos da v3.1 — Compliance (chat: mercans-compliance)
- [ ] Confirmar o tratamento pós-imposto de 21640–21645 — Compliance (chat: mercans-compliance)
- [ ] WTC do cliente (Google Sheet) não estava legível; Drive precisa de re-auth — (chat: mercans-compliance)
- [x] Justificativa do cliente para incluir nº de filhos no payslip — não necessária: Manju Shetija (10/08) e Wallisson (11/08) decidiram exibir estado civil e nº de parts, sem nº de filhos (HRBS-12472, Resolved 2026-08-12) — _fechada em 27/10 (HRBS-12472): Manju Shetija (10/08/2026): Gabão exibe estado civil e nº de parts, nº de filhos não é exigido; Wallisson (11/08): nº de filhos é só insumo do quociente familiar (Art. 116 A-F, LF 2026), nada a acrescentar. Ticket Resolved 12/08.…_
- [ ] Design do Gabão — Manju (chat: design-dev-kb)
- [x] Observação: o ticket HRBS-14996 (CI) tem colunas "CNAMGS" e "FNH" no registro do cliente da CI, que são órgãos gaboneses; Wallisson confirmou no ticket (2026-09-22) que não existem na CI (são AT/MP 3% e PF+AM 5,75%); ver [[Costa-do-Marfim]] — _fechada em 27/10 (HRBS-14996): Wallisson (22/09/2026) no HRBS-14996: as colunas 'CNAMGS' e 'FNH' no registro do cliente são órgãos gaboneses que não existem na CI; os valores são AT/MP 3% e PF+AM 5,75%. A observação está registrada no ticket (Resolved 29/09)._

## Correções ligadas
- [[correcoes]]: WTC Gabão v3.0 sem o bloco de deduções Global 21100–21900 e de ER 23640–23673 (59 códigos), filtro salvo na coluna A e VC sem linha 3.1; corrigido na v3.1 DRAFT (2026-09-23).
- Cliente (não é nosso): "OPRAG/FNE Training Levy 1%" não existe, é o CFP 0,5% (HRBS-14943).

## Fontes
- raw/tickets/extracao/2026-10-02-tickets-AF.md
- raw/chats/2026-10-01-mercans-compliance.md
- raw/chats/2026-10-01-mercans-design-dev-kb.md

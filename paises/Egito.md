---
tipo: pais
codigo: "EG"
etapa_research: "concluida"
etapa_research_data: 2026-08-27
etapa_design: "aguardando"
etapa_design_data: 
etapa_producao: 
etapa_suporte: "sem ticket no hub"
etapa_suporte_data: 
ccg: 
ccg_data: 
wtc: 
wtc_data: 
dd: 
dd_data: 
report_specs: 
report_specs_data: 
sir: 
sir_data: 
payslip: 
skill: "payroll-compliance-egypt"
tickets_abertos: 
tickets_conferidos_em: 
atualizado_em: 2026-10-27
---
# Egito

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-egypt` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-08-27 (pesquisa, relatório QA) | skill compilada |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-egypt`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano fiscal 2026 (jan-dez), setor privado, moeda EGP. Fora: servidores, setores público e de negócios públicos, militares, domésticos, empregadores e autônomos.
- **Órgãos:** ETA (imposto sobre salários, sistema de payroll REST/JSON), NOSI (seguro social), UHIA (seguro-saúde universal), Ministry of Labour e National Wages Council.
- **Relatórios principais:** formulário de cálculo mensal (EG-RPT-01, por pagamento, via ETA); formulário de pagamento mensal (RPT-02); Form 2 Salaries (RPT-03); Form 4 Salaries trimestral (jan/abr/jul/out); Form 9 Settlements anual; Martyrs' Fund (RPT-06); selo proporcional (RPT-07); levy do Training and Rehabilitation Fund anual (RPT-14). Imposto retido recolhido até dia 15 do mês seguinte; NOSI vence no início do mês seguinte com tolerância de 15 dias.
- **Confiança da skill:** "READY FOR REVIEW", sem tier; piso de 95%, 8 seções abaixo dele. Núcleo de cálculo forte (matriz do art. 8 lida da Gazette, 99%); `EG-*` wage types são derivados (sem WTC Global); layouts de Form 2 (60%) e Form 4 (65%) derivados.

**Armadilhas confirmadas** (correções da skill)
1. Art. 8 é uma matriz (6 colunas x 7 alíquotas), não escada: faixas inferiores somem ao passar 600k/700k/800k/900k/1,2 mi (engine) → `01-ccg.md` §6.3
2. Imposto por anualização: base acumulada x 360 ÷ dias, arredondada para baixo a EGP 10, recalculado a cada pagamento (engine) → `01-ccg.md`
3. Os 11% do empregado = 9% pensão + 1% doença + 1% Reward System (não desemprego, que é 1% só do empregador); 18,75% patronal inclui 1% de acidente repassado à saúde (engine) → `01-ccg.md` §4.3
4. Base do seguro social (lista fechada de 16 itens) diverge da base do imposto; representação (بدل التمثيل) entra no seguro (engine) → Lei 148/2019 art. 1(8)
5. Benefícios in natura nunca afetam o líquido, só a base fiscal (carro 20%, celular 20%, empréstimo 7%) (engine) → `02-wtc.md` §6
6. Benefícios coletivos isentos não são lançados; o equivalente em dinheiro é tributável (engine) → Lei 91/2005 art. 13(5)
7. Seguro-saúde universal do empregado: 1% + 3% por cônjuge sem renda + 1% por dependente (engine) → `01-ccg.md` §5
8. 10% para empregador não original é "por conta" (art. 72 bis, Lei 30/2023), não definitivo; o rótulo "قطعية" do ETA é histórico (engine) → `01-ccg.md`
9. Aumento anual obrigatório = max(3% do salário de seguro, EGP 250) na data de aniversário individual (Lei Trabalhista 14/2025 art. 12; antes 7%) (engine) → `01-ccg.md` §9
10. Imposto assumido pelo empregador é benefício tributável: gross-up deve iterar (engine) → `02-wtc.md`
11. Pagamento de férias acumuladas durante o contrato não é diluído; atrasados salariais são, com tax treatment 8 (engine) → art. 10
12. Teto de penhora 25%/50% calculado após imposto, seguro e empréstimo (art. 114) (engine) → `01-ccg.md`
13. Não existe declaração retificadora; períodos devem ser enviados em ordem; correções vão ao mês seguinte ou ao acerto anual → `04-reports-spec.md`
14. ETA é M2M só pela metade: JSON envia rascunho; cálculo e submissão são no portal; sem token ou selo; NOSI e UHIA não integrados → `03-sir.md`
15. Contradições com o workbook de payslip anterior (EG-compliance/06-payslip): NOSI como fundo único e "7 faixas" de imposto estão errados → `07-qa-report.md` §6

**O que mais dá errado** (do QA)
- Lacunas em quatro pontos: layouts que a ETA não publica, detalhe operacional dos dois levies menores, portarias ministeriais da Lei 14/2025 após set/2025, itens vivos.
- Valores que nunca devem ser fixados: taxa de crédito/desconto do CBE (multa = taxa + 2%), taxa média de T-bills (adicional NOSI = taxa + 2%), salário mínimo do setor privado, feriados.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- §3.1 quais componentes do seguro social o UHI substitui (72%); §3.2 lista de governadorias do UHI (78%).
- §3.3 levy do Training Fund: operação (40%); §3.4 Martyrs' Fund no setor privado (80%) — **resolvido em 2026-10-22: vale para o setor privado** (ver Correções ligadas).
- §3.5 feriados públicos (35%); §3.6 seguro social de estrangeiros (65%); §3.8 tributação de indenização por demissão ilícita (50%).
- §3.9 prazos de retenção de registros (35%); §3.10 portaria posterior a set/2025 sobre conteúdo do payslip (50%); §3.11 host de produção da API (60%, só pré-produção publicado).
- §3.7 pareamento código-rótulo DTE/DAE/NAD (75% nas linhas marcadas); §4.1 ausência de mudança no art. 8 em 2025/2026 (93%).
- §4.2 salário mínimo privado: último decidido EGP 7.000; passo para EGP 8.000 pendente em 2026-08-27. §4.3 dia do mês da declaração trimestral não estabelecido. §4.4 duas leituras da base do Training Fund.

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Seguro social (piso/teto de salário de contribuição) | EGP 2.700 / 16.700 | 2026-01-01 | Anúncio do NOSI de 2025-11-30 |
| Seguro social, taxas | empregado 11%, empregador 18,75% | 2026 (próximo degrau 2027-01-01) | Lei 148/2019 arts. 19, 36, 46, 70, 86 |
| Imposto sobre salário | matriz do art. 8 | 2024-03-01 | Lei 91/2005 conforme Lei 7/2024 (Gazette nº 7 bis (a), 2024-02-21) |
| Isenção pessoal | EGP 20.000 (proporcional ao período) | 2024-03-01 | Lei 7/2024 art. 13(1) |
| Salário mínimo privado | EGP 7.000 (não fixar; passo de 8.000 pendente) | 2025-03-01 | Ministério do Planejamento, reunião de 2025-02-09 `[A-]` |
| Seguro-saúde universal (empregador) | 4%, mínimo EGP 50 | 2026 | Lei 2/2018 art. 40; UHIA FAQ |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| | | | | |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| | | | | |

## Decisões
- AAAA-MM-DD: decisão, por quê, quem decidiu

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| 2026-10-22 | Ericsson ME (planilha "Compliance feedback list", pedido da Manju por chat) | WT 1026/1027 adiantamentos, 1043 aviso prévio, 1125 LTA | Respondido na planilha com fonte primária (Lei 91/2005 arts. 9, 12; Decreto 991/2005 art. 11(3); Lei 148/2019 art. 1(8); ETA FAQ v4; Lei 4/2021). Rascunho: `rascunhos/2026-10-22-ericsson-me-respostas-LB-JO-EG.md` | Não |

- [[rascunhos/2026-10-22-ericsson-me-respostas-LB-JO-EG|2026-10-22-ericsson-me-respostas-LB-JO-EG]]: Respostas Compliance Ericsson ME para Líbano, Jordânia e Egito (7 linhas)

## Pendências
- [x] Corrigir a skill `payroll-compliance-egypt` (`01-ccg.md` §8.2 e linha 54; SKILL.md escopo; `07-qa-report.md` §3.4): Fundo dos Mártires vale para o setor privado (2026-10-22). **Feito em 2026-10-22:** v2 publicada para a organização no claude.ai (também RPT-06 e DD); pacote em `Research Pipeline/Egypt/2026-10-22-skill-fundo-martires/`.
- [ ] Ler o art. 53 do Regulamento 2437/2021 (bdl excluídos ≤ 30% do salário de contribuição): citado, não conferido pessoalmente. PDF em [[raw/docs/oficiais/EG/2026-10-22-decreto-pm-2437-2021-regulamento-lei-148-gazette.pdf|2026-10-22-decreto-pm-2437-2021-regulamento-lei-148-gazette.pdf]].
- [ ] Lei 11/2026 (art. 111 da Lei 148/2019, segundo a imprensa): sem texto oficial obtido.
- [ ] Circular MoF 14/2021: só há cópia em host não oficial (aliateck); buscar cópia oficial.

## Entregas (conferências)
- 2026-10-22 · — · Skill payroll-compliance-egypt: Fundo dos Mártires no setor privado: [[Research Pipeline/Egypt/2026-10-22-skill-fundo-martires/CONFERENCIA|conferência]]
- 2026-10-25 · HRBS-15790 · Seguro social a partir de 01/01/2027: [[Research Pipeline/Egypt/2026-10-25-HRBS-15790-SI-2027/CONFERENCIA|conferência]]

## Correções ligadas
- 2026-10-22: Fundo dos Mártires no setor privado ([[correcoes]]).

## Fontes
- skill payroll-compliance-egypt (lida em 2026-10-02)
- Fontes oficiais baixadas em 2026-10-22: `raw/docs/oficiais/EG/` (índice em `2026-10-22-fontes.md`). Lei 91/2005: 21 leis de alteração (lista da ETA), nenhuma muda arts. 9 e 12; art. 11 revogado pela Lei 30/2023 art. 8. Lei 148/2019: alterada pelas Leis 25/2020, 18/2023, 8/2024, nenhuma no art. 1(8).

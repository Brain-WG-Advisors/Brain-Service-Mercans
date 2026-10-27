---
tipo: pais
codigo: "PT"
etapa_research: "concluida"
etapa_research_data: 
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
skill: "payroll-compliance-portugal"
tickets_abertos: 
tickets_conferidos_em: 
atualizado_em: 2026-10-27
---
# Portugal

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-portugal` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | [data?] | skill compilada (QA: READY FOR REVIEW, 4 seções abaixo do piso de 95%) |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-portugal`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano fiscal 2026, setor privado (inclui membros de órgãos estatutários, MOE), EUR. Três territórios de retenção: Continente, Açores, Madeira (conforme o local de trabalho). Fora: emprego público, militares e forças de segurança, independentes (recibos verdes), seguro social voluntário, serviço doméstico.
- **Órgãos:** AT (IRS), Segurança Social (ISS/IGFSS), ACT e DGERT (trabalho), GEP.
- **Relatórios principais (9):** AT: DMR-AT, Modelo 10, Modelo 30, declaração ao trabalhador até 20 de janeiro. Segurança Social: Declaração de Remunerações (legado, em extinção), confirmação SCC, comunicação de admissão, comunicação de cessação/suspensão. ACT/GEP: Relatório Único.
- **Confiança da skill:** pesquisa do zero, READY FOR REVIEW, 2 autocorreções (ver abaixo). Abaixo do piso de 95%: payload da mensagem SCC (55%), layouts do Modelo 10 e Modelo 30 (não especificados), anexos e formato do Relatório Único (50%), regra do dígito de controle do NISS (75%); taxas contributivas setoriais (65%, quase fora de escopo). Códigos `PT-*` do WTC são derivados (sem mapeamento ao Global WTC); os códigos oficiais são os "Tipo de rendimento" do DMR-AT e as letras da Declaração de Remunerações. As 21 tabelas de retenção (Continente, Açores, Madeira I-VII) estão completas e reconciliadas.

**Armadilhas confirmadas** (SKILL.md "Design clarifications"; engine = muda valor calculado)
1. Perguntar o território antes de qualquer retenção: salário mínimo Continente 920, Açores 966, Madeira 980; tabelas independentes (Açores III tem 10 linhas contra 12 no Continente, com limiares sem equivalente); nunca escalar nem interpolar; sequência de Madeira é não monotônica (30,28% depois 28,02%, verificado) → `01-ccg.md` §4 (engine)
2. "Taxa marginal máxima" não é a taxa de retenção: `Retenção = R x Taxa - Parcela a abater - (Parcela adicional x dependentes)`, piso zero; nas primeiras linhas a parcela é uma fórmula com R → `01-ccg.md` §4.1 (engine)
3. SS do empregado NÃO é deduzida da base da retenção de IRS (as tabelas operam sobre o bruto; o alívio já está na parcela); subtrair os 11% antes subretém → `01-ccg.md` (engine)
4. Retenção por componente, não por recibo: horas extras a 50% da taxa efetiva calculada do mês (Despacho 233-A/2026 n.º 5 f; CIRS 99.º-C n.º 8); subsídios de férias e de Natal têm taxa efetiva própria (n.º 10; CIRS 99.º n.º 9); 14 remunerações por ano → `01-ccg.md` (engine)
5. Prêmios de trabalho têm defaults estatutários: horas extras dobram acima de 100 h acumuladas por ano (CT 268.º, Lei 13/2023); trabalho noturno +25% (CT 266.º n.º 1; CCT só pode substituir); exige contador anual de horas extras → `01-ccg.md` Parte V (engine)
6. Indenização segmentada em 2023-05-01 (Lei 13/2023; 14 dias/ano só para o tempo posterior; antes 12 dias ou escada da Lei 69/2013); multiplicador de 14 sobre toda a antiguidade superestima → `01-ccg.md` Parte V (engine)
7. Dois divisores corretos: hora = (Rm x 12) / (52 x n) (divisor 2.080 para 40 h; CT 271.º); dia para indenização = (retribuição base + diuturnidades) / 30; nenhum é 173,33 → `01-ccg.md` (engine)
8. Pagamento de férias e subsídio de férias têm bases diferentes (CT 264.º n.º 1 vs n.º 2); a base do subsídio é mais estreita que "uma remuneração mensal inteira" → `01-ccg.md` (engine)
9. Subsídio de refeição 2026 mudou retroativamente (Portaria 51-B/2026/1, publicada em 2026-01-30, efeitos 2026-01-01): 6,15 em dinheiro e 10,455 em cartão (3 casas, +70%) → `01-ccg.md` (engine)
10. Sem teto de SS e sem contribuições separadas de saúde/pensão/desemprego/formação: taxa única 11% / 23,75% / 34,75% sobre o bruto; membros de órgãos de gestão pagam a mesma taxa total → `01-ccg.md` §8-11 (engine)
11. Declaração de Remunerações em extinção: desde 2026-01-01 (DL 127/2025) a SS calcula e o empregador confirma até o dia 20; silêncio = aceitação → `03-sir.md`
12. PT é M2M real: PSi é REST (HTTP Basic NISS:password ou Bearer JWT, sem certificado de cliente); DMR-AT por webservice → `03-sir.md`
13. Rendimento isento também se declara (A21 refeição, A22 ajudas de custo, A27 teletrabalho, A34, A40, A41); DMR é provisória por 30 dias (Portaria 33/2024 art. 2.º n.º 3-4), sem correção fica sem efeito → `04-reports-spec.md`
14. Sem pagamento estatutário de doença/parentalidade pelo empregador (paga a SS; doença a partir do 4.º dia); mínimo diário de doença é 9,20 = 30% da RMMG (não IAS); paternidade 28 dias + 7 opcionais em dias corridos; mãe 42 dias consecutivos; FCT/FGCT extintos desde 2024-01-01; seguro de acidentes nunca é dedução do empregado (Lei 98/2009) → `01-ccg.md` §14
15. Reforma "Trabalho XXI" foi REJEITADA (2026-06-19); nada é lei; vale Lei 7/2009 até Lei 32/2025 → `07-qa-report.md` §4.1

**O que mais dá errado** (do QA)
- Autocorreção 1: a skill dizia que não existe prêmio noturno geral; está errado (CT 266.º n.º 1, +25%).
- Autocorreção 2: benefício mínimo diário de doença era 5,37 (30% do IAS); correto 9,20 (30% da RMMG), subestimava ~71%.
- Fonte desatualizada: o Código do Trabalho anotado da ACT (base 2020) é anterior à Lei 13/2023; checar licenças parentais contra a Lei 13/2023.
- Defeito do instrumento: Açores Tabela VII linha 4 imprime taxa efetiva 9,8% inatingível (usar taxa e parcela, ignorar a coluna) (§4.10); `pdftotext` atribui errado a coluna "Parcela a abater" (§4.11); inconsistência interna da coluna "Taxa efetiva" no n.º 4 do Despacho 233-A/2026 (§4.6).

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- Payload SCC (55%), layouts Modelo 10/30, Relatório Único (50%), dígito de controle do NISS (75%, NIF 95%).
- Se a limitação temporal do art. 35.º n.º 2 da Lei 13/2023 alcança a taxa de 24 dias dos arts. 344.º/345.º (80%); composição da base da regra de 50% de horas extras (90%); permissão de recibo eletrônico (85%).
- Página de taxas do seg-social.pt ilegível por fetch automático (§4.9).

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Contribuições SS (empregado / empregador / total) | 11% / 23,75% / 34,75%, sem teto | 2026 | Código dos Regimes Contributivos (CRC, Lei 110/2009) |
| Salário mínimo (RMMG) | Continente 920; Açores 966; Madeira 980 | 2026 | skill (SKILL.md); `01-ccg.md` |
| Subsídio de refeição | 6,15 em dinheiro; 10,455 em cartão | 2026-01-01 | Portaria 51-B/2026/1 |
| Faixas anuais de IRS | 9 escalões (CIRS art. 68.º) | 2026 | OE2026 (Lei 73-A/2025) |
| Mínimo diário de subsídio de doença | 9,20 | 2026 | ISS, Guia Prático 5001 v4.55 (2026-07-14) |
| Indenização por cessação | 14 dias/ano só para serviço após 2023-05-01 | 2023-05-01 | Lei 13/2023, CT art. 366.º e art. 35.º n.º 2 |

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
| | | | | |

## Pendências
- [ ]

## Correções ligadas
- _(links para entradas de [[correcoes]])_

## Fontes
- skill payroll-compliance-portugal (lida em 2026-10-02)

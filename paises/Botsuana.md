# Botsuana (Botswana, BW)

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-botswana` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | — | CCG v1.0 (fev/2026, autor Wallisson), WTC v3.0, DD v3.1 (chat: design-dev-kb) |
| [[design]] | ✅ | — | Design CT-A-507 + tabela CT-A-508 (Mohit; 12 regs, 9072xxx), em produção (chat: design-dev-kb). Pendente: verificar band de 15% |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | — | Sem tickets nas fontes |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-botswana`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano fiscal 2026-27 (2026-07-01 a 2027-06-30; o ano leva o nome do ano em que termina), setor privado, moeda BWP. Fora: servidores, forças armadas, autônomos, ministros/parlamentares, diplomatas.
- **Órgãos:** BURS (imposto) e Commissioner of Labour (emprego e retorno de não cidadãos).
- **Relatórios principais:** ITW 7A/7B (remessa/declaração mensal de PAYE), ITW 8 (certificado do empregado), ITW 10/10A, ITW 5, ITW 4A; retorno anual de não cidadãos (Cap. 47:02 s. 18). BURS é portal, não M2M.
- **Confiança da skill:** veredito SHIP. Núcleo tributário 97% (traça ao texto primário, aritmética conferida). Abaixo de 95%: layouts de campo das ITW (55-60%, DERIVADOS, sem imagem oficial dos formulários), momento do ITW 8 (70%), formatos bancários (70%), relatório de acidente (75%), dígito de sexo do Omang (80%), taxa de severance, data efetiva do salário mínimo, training levy e calendário de feriados (85-90%). Dois layouts a 0% (retorno de não cidadãos; registros trabalhistas do s. 92 da Employment Act). Não usa a nomenclatura TIER-B.

**Armadilhas confirmadas** (esclarecimentos da skill; prevalecem sobre `references/`)
1. Prazo mensal do PAYE = fim do mês + 14 dias corridos (ITA 2026 s. 138(1), s. 2(2)), não dia 15; rola para o próximo dia útil pagamento e entrega (TAA s. 75); multa maior entre P500/dia ou 10%, juros de 1,5%/mês nunca dispensados → SKILL.md item 1
2. Custo patronal estatutário de folha = zero, sem linha de previdência; training levy é 0,2% do faturamento anual do empregador, cobrado na declaração de VAT, não por empregado; "Skills Development Levy 0,2% da folha" é falso → item 2; `07-qa-report.md` §4.1
3. ITA s. 16(5) prevalece sobre a lista tributável do BURS: reembolso de despesas médicas/prêmios, passagem de realocação, gratuity/severance investido direto em fundo aprovado (100% isento), contribuição patronal a fundo e bolsas de treinamento ficam fora do rendimento; o eixo é allowance × reembolso → item 3
4. Employment Act s. 2(3) desliga a Parte VIII para gerentes, executivos e profissionais (sem hora extra 1,5×, 15 dias de férias, feriado pago, 20 dias de doença estatutários); `EMPLOYEE_CATEGORY` não tem default seguro → item 4
5. Três divisores de hora extra: 22 (5 dias), 24 (5,5 dias), 26 (6 dias); nunca ÷30 nem ÷21,67; H = 9 na semana de 5 dias → item 5
6. Severance e pensão/gratuity são mutuamente exclusivos, inclusive direito futuro (s. 27 proviso (ii)) → item 6
7. Terminal pay em três vias: 100% isento se investido em fundo aprovado; senão 50% isento, calculado como o MENOR entre lump sum e espalhamento retroativo (menor de prazo do contrato ou 3 anos) → item 7
8. s. 16(6) desliga todo o regime do s. 17 para partes relacionadas: pagamento totalmente tributável → item 8
9. Existe método opcional de média cumulativa (BURS Example 11 + Spread Back Sheet); não afirmar que Botsuana não tem → item 9
10. Bruto em dinheiro ≠ renda tributável: somar benefícios não monetários e subtrair só a contribuição a fundo aprovado (teto 15%); sem dedução pessoal, crédito, estado civil ou dependentes → item 10
11. `MARKET_LENDING_RATE` = taxa de política do Banco de Botswana em 1º de julho, congelada no ano; benefício de veículo é por disponibilidade, sem diário de km nem % de uso de negócio → item 11
12. P74.050 é rendimento do trabalho; P74.650 é ganho de capital (faixa nula do ganho começa em P36.000); na tabela mensal usar 33.333,33 / 6.170,83 → item 12
13. Não há payslip estatutário; o documento obrigatório é o ITW 8; ainda assim itemizar descontos conforme o s. 80(1) → item 13
14. O site do BURS está defasado (limiar "P2500/mês", "31 dias" para o retorno anual, que é 28 dias pelo s. 139(1)); valem as leis e a Tax Table → item 14

**O que mais dá errado** (do QA, ranking de dano)
- Prazo no dia 15 em vez de 14 (atraso de 1 dia todo mês)
- Exclusões do s. 16(5) omitidas (tributa em excesso verbas rotineiras)
- Aplicar regras da Parte VIII a todos sem separar categoria; divisores de hora extra errados
- Acumular severance para quem tem pensão (provisão a maior)
- Defeitos nas fontes oficiais: tabela de grossing-up de não residente do Example 13 está errada (derivar do schedule); cópia da Employment Act hospedada pelo governo está defasada (doença 14 dias, sem s. 27(1A))

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- ITW 8 (s. 137) é mensal ou anual: o maior item aberto, não tratar como resolvido
- ITW 7A é "income tax return" ou "other document" para a multa do s. 101 (~50%, variação de 4×); se o waiver de 12 meses da reg. 33 alcança PAYE (premissa operacional: não)
- Layouts de campo das ITW (derivados); retorno de não cidadãos e registros do s. 92 (0%)
- Se existe teto prescrito pelo Ministro (s. 16(2)) para as verbas excluídas; Income Tax Regulations 2026 completas não recuperadas
- Salário mínimo (S.I. 7 de 2024, P9,06/h geral, P1.500/mês doméstico e agrícola; revisão e data efetiva em disputa); calendário de feriados do Gazette (alimenta o s. 75)

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| PAYE residente | seis faixas; faixa nula até P48.000/ano; topo 27,5% acima de P400.000 (74.050 + 27,5%) | 2026-07-01 | ITA 2026 Sch. 1 Parte I |
| PAYE não residente | 5% desde o primeiro Pula (diferença de P200,00/mês no topo da faixa de 25%) | 2026-07-01 | ITA 2026 Sch. 1 |
| Prazo mensal PAYE | fim do mês + 14 dias corridos, com rolagem do TAA s. 75 | 2026-07-01 | ITA 2026 s. 138(1); TAA s. 75 |
| Previdência e custo patronal | nenhum; training levy 0,2% do faturamento (isento abaixo de P250.000) | 2026 | Vocational Training Act; skill item 2 |
| Salário mínimo | P9,06/hora geral; P1.500/mês doméstico e agrícola | 2024 (data efetiva em disputa) | S.I. 7 de 2024 |
| Divisores de hora extra | 22 / 24 / 26 | vigente | Employment Act s. 95(8) |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| CCG | v1.0 | 2026-02 | KB_Botswana_Full_Package.md | Autor Wallisson |
| WTC | v3.0 | — | idem | Colunas azuis (research) e laranja (dev); objetivo de preencher as laranjas por regras determinísticas |
| DD | v3.1 | — | idem | |
| Design CT-A-507 + CT-A-508 | — | — | YouTrack KB | Mohit; 12 regs 9072xxx; fonte do design de produção |

## Valores-chave (com vigência)
Valores do chat design-dev-kb (de KB_Botswana_Full_Package.md). Ver a skill, que reflete o reset legal de 2026-07-01 (Income Tax Act 2026) [INCERTO se estes valores já foram atualizados].
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| Ano fiscal | 1/jul–30/jun | ⚠️ vigência? | — | KB_Botswana_Full_Package |
| PAYE residente | 0% até 48.000; 5% até 84.000; 1.800 + 12,5% até 120.000; 6.300 + 18,75% até 156.000; 13.050 + 25% acima | ⚠️ vigência? | [INCERTO] | ⚠️ sem fonte legal no chat; conferir com a skill (esquema novo de seis faixas, até 27,5%, a partir de 2026-07-01) |
| PAYE não residente | 5% até 84.000; 4.200 + 12,5%; 8.700 + 18,75%; 15.450 + 25% | ⚠️ vigência? | [INCERTO] | idem |
| Pensão | MIN(real; 15%) pré-tax; gratuity 1/3 isento; sem SS (BOTA 52534, WC 52564); anualização YTD × 12 / meses | ⚠️ vigência? | — | KB_Botswana_Full_Package |

## Decisões
- 2026-06-11: datas comparadas sempre como `yyyyMMdd`, nunca `MMdd` — falso positivo entre anos; ano fiscal fora do calendário (BW) — Ruchi; Mohit confirmou (chat: design-dev-kb)
- s.d.: WTC (BW): colunas laranja (dev) preenchidas a partir das azuis (research) por regras determinísticas; vale também para o DD — objetivo de automação — Wallisson (chat: design-dev-kb)
- s.d.: anualização `DIVIDE(MULTIPLY(x;$period_divisor);$58206)`; sem SS; ceiling account; semeadura P16; gate por flag (BW-1..7) (chat: design-dev-kb)

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| | | Sem tickets nas fontes | | |

## Pendências
- [ ] Divergência hub × skill: o PAYE do hub tem cinco faixas até 25% (13.050 + 25% acima de 156.000, residente e não residente); a skill traz seis faixas, com 74.050 + 27,5% acima de P400.000 (residente) e 76.450 + 27,5% (não residente) desde 2026-07-01 — verificar se o design CT-A-507/508 já tem a faixa de 27,5% (skill lida em 2026-10-02)
- [ ] Divergência hub × skill: o hub registra "gratuity 1/3 isento"; a skill diz terminal pay 100% isento se investido em fundo aprovado, senão 50% isento (ITA 2026 s. 16(5)(c) e s. 17) — verificar (skill lida em 2026-10-02)
- [ ] Divergência hub × skill: o hub guarda a pensão como MIN(real; 15%) pré-tax sem detalhar; a skill limita a dedução a 15% da renda tributável do ano (ITA s. 28(4)/(5)) e é a única dedução que reduz a base — verificar a formulação no design (skill lida em 2026-10-02)
- [ ] Verificar a band de 15% em 58101 (ordinal 11, "needs verification") e os dois débitos da 9072011 — (chat: design-dev-kb)
- [ ] Conferir se os valores de PAYE acima já refletem o Income Tax Act 2026 (vigência 2026-07-01) — Compliance [INCERTO]
- [ ] Próximos países sugeridos pelo pacote: CO, AU V2.0, NL, NO — (chat: design-dev-kb)

## Correções ligadas
- _(nenhuma correção registrada)_ — ver [[correcoes]]

## Fontes
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- skill payroll-compliance-botswana (lida em 2026-10-02)

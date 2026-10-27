---
tipo: pais
codigo: "MZ"
etapa_research: "concluida"
etapa_research_data: 2026-09-11
etapa_design: "aguardando"
etapa_design_data: 
etapa_producao: 
etapa_suporte: "sem ticket no hub"
etapa_suporte_data: 
ccg: v1.2
ccg_data: 
wtc: v2.0
wtc_data: 
dd: v2.0
dd_data: 
report_specs: 
report_specs_data: 
sir: 
sir_data: 
payslip: 
skill: "payroll-compliance-mozambique"
tickets_abertos: 
tickets_conferidos_em: 
versoes_fonte: "nome do arquivo no Drive (Country Folders/Mozambique), lido em 2026-10-27; sem data de versão"
atualizado_em: 2026-10-27
---
# Moçambique

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-mozambique` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-09-11 | skill compilada (build de pesquisa direta, ano-parâmetro 2026) |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-mozambique`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** folha do setor privado em 2026, moeda MZN (redenominada 1.000:1 em 2006-07-01). Fora: setor público, INSS de autônomos, IRPC, IVA, mineração/petróleo, zonas francas, empregados domésticos.
- **Órgãos:** AT (imposto), INSS (previdência), MITESS (trabalho), e a seguradora do seguro de acidentes de trabalho (quarta contraparte obrigatória).
- **Relatórios principais:** INSS Declaração de Remunerações (entre o dia 20 do mês de referência e o dia 10 do seguinte) + Guia de Pagamento; cópia à seguradora (mensal, dia 15); IRPS Modelo 19 (mensal, dia 20); declaração anual do empregado / Modelo 10 (obrigatório para todos desde 2026); Modelo 20H e e-FRN (janela 1/abr a 31/mai, snapshot de 31/mar). Nenhum tem schema de arquivo nem API.
- **Confiança da skill:** etiquetas `[P]` (lido no instrumento primário), `[P-bill]` (lido no projeto de lei), `[S]` (corroborado, instrumento não lido), `[S!]` (contestado), `[D]` (derivado). Muito alta nos arts. do Código do Trabalho (Lei 13/2023) e na regulamentação do INSS; alta nos valores da tabela do art. 65-A, mas média no texto (só o projeto de lei foi lido). Não usa a nomenclatura TIER-B.

**Armadilhas confirmadas** (esclarecimentos da skill; vários são engine)
1. Retenção de IRPS é lookup de tabela + coeficiente (art. 65-A: fixo + coeficiente × excesso sobre o piso da faixa), não taxa × salário; na tabela `-` (sem imposto e sem coeficiente) ≠ `0,00` (fixo zero, coeficiente se aplica) → item 1
2. "32%" é só a faixa de topo (escala 10/15/20/25/32%); aplicar 32% chapado superestima em MZN 16.371/mês no exemplo de 121.550 → item 2
3. Abatimento anual da faixa de 25% = 35.700, não 37.500 (erro de publicador internacional; provado por continuidade) → item 3
4. Dependentes deslocam o limiar de isenção (20.250 / 20.750 / 21.000 / 21.250 / 21.750 para 0/1/2/3/4+), não são crédito → item 4
5. Retenção mensal incide sobre o bruto sem deduzir INSS; a apuração anual deduz INSS e quotas sindicais; desde a Lei 11/2025 a retenção deixou de ser definitiva e o Modelo 10 é obrigatório → item 5
6. Seguro de acidentes de trabalho é apólice comercial obrigatória separada (Lei 13/2023 art. 235; Decreto 62/2013), sem taxa estatutária; explica o "5% do empregador" que não fecha com os 4% do INSS; base ligada à declaração INSS, e sub-declarar deixa o empregador responsável pela diferença; multa de 5 a 10 salários mínimos do setor por trabalhador → itens 6-8
7. Salário mínimo são 18 taxas em 8 setores, tabela de 2025 morta: Diplomas Ministeriais 34-41/2026, retroativos a 2026-04-01 (Kapenta não mudou: 4.991,09) → item 9
8. Severance usa o salário mínimo do PRÓPRIO setor do empregado (art. 141(3): 30/15/5 dias por ano) e base só de salário base + bônus de antiguidade (art. 118(3)); setor é dado mestre da folha; severance não é tributável → itens 10-12
9. INSS 7% (ER 4% / EE 3%) sem teto; base é lista enumerada (art. 11) com itens condicionados à "regularidade" por tipo de salário → itens 13-14
10. Férias: 12 dias no primeiro ano e 30 dias corridos depois (art. 108); doença é benefício do INSS (70% após 6 meses de carência), não obrigação do empregador; maternidade 100% INSS → itens 17-18
11. Art. 125(1) (hora extra) traz erro de redação no gazette ("20 horas"): construir +50% até 24:00 e +100% depois, configurável, e sinalizar → item 19
12. Nove feriados; só domingo desloca para o dia seguinte (art. 105); descontos limitados a 1/3 da remuneração mensal e pagamento em espécie a 25% (arts. 124(4), 123(1)(a)) → itens 20, 22
13. Qualquer limiar de IRPS em milhões é moeda pré-2006 (MZM): não usar a fonte → item 23

**O que mais dá errado** (QA, "cinco coisas mais prováveis de errar")
- Tributar a severance
- Calcular a faixa de severance com base ou setor errados
- Tratar `-` e `0,00` como iguais na tabela de retenção
- Deduzir INSS antes de aplicar a tabela de retenção
- Esquecer a seguradora (quarto calendário, quarta contraparte)

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- at.gov.mz inacessível durante todo o build: fatos da AT são de segunda mão, sem layouts de formulário nem schema de e-declaração
- Texto promulgado da Lei 11/2025 não obtido (tabela 65-A é `[P-bill]`; o projeto trazia 5% liberatório no art. 57(5), a lei promulgada é relatada como 10%)
- Diploma conjunto ministerial que fixa 4%/3% do INSS não localizado (art. 15 diz que existe)
- Mínimo não tributável atual (art. 56), teto de ajudas de custo, escalas de valoração de espécie e definição legal de "regularidade": sem fonte; a skill construiu regras e as sinalizou
- Quatro instrumentos citados não lidos; sem schema/API para SISSMO, e-FRN, e-declaração AT; teste de residência perdeu a regra de 180 dias (determinações de expatriados anteriores a 2026-01-01 estão obsoletas)

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| IRPS anual | 10/15/20/25/32%; abatimentos 0 / 2.100 / 10.500 / 35.700 / 141.540; topo acima de MZN 1.512.000 | 2026 | Código do IRPS art. 54 `[S]` |
| IRPS retenção mensal | isento abaixo de 20.250 (0 dependentes) a 21.750 (4+); tabela de 50 células | 2026 | Código do IRPS art. 65-A `[P-bill]` (Lei 11/2025) |
| INSS | 7% (ER 4% / EE 3%), sem teto | ⚠️ vigência? | site do INSS `[P]`; instrumento fixador não localizado |
| Salário mínimo | 18 taxas por setor; ex.: Setor 1 MZN 7.072; Indústria Transformadora MZN 10.622,50 | 2026-04-01 | Diplomas Ministeriais 34-41/2026, de 20/mai |
| Severance | 30 / 15 / 5 dias por ano conforme múltiplos do mínimo do setor (1-7× / >7-18× / >18×) | 2023 | Lei 13/2023 art. 141(3) |
| Férias | 12 dias (1º ano), 30 dias corridos depois | 2023 | Lei 13/2023 art. 108 |

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
- skill payroll-compliance-mozambique (lida em 2026-10-02)

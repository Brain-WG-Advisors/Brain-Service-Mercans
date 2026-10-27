# Belarus

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-belarus` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-08-27 (relatório QA) | skill compilada |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-belarus`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano fiscal 2026, empregadores do setor privado, moeda BYN; empregados com contrato de trabalho e contratos civis de obra/serviço. Fora: servidores, militares, autônomos/empresários individuais, trabalho no exterior.
- **Órgãos:** MNS (imposto de renda), FSZN (contribuições e contabilidade personificada), Belgosstrakh (seguro de acidentes), Ministry of Labour and Social Protection.
- **Relatórios principais:** 4-фонд (FSZN, dia 20); ПУ-1, ПУ-2 (eventos), ПУ-3 (trimestral, dentro do mês seguinte ao trimestre), ПУ-6 (previdência profissional, só postos especiais); declaração do agente fiscal ao MNS; relatório anual da Belgosstrakh. Todos os 3 órgãos são portais (cabinet + ЭЦП ГосСУОК), sem M2M.
- **Confiança da skill:** "PASS WITH NOTES" (2026-08-27), sem tier; 2 seções abaixo de 95% (média de ganhos ~88%, integrações ~93%). DERIVED: layout da declaração MNS (~60%), ПУ-6 (~70%), relatório Belgosstrakh além da linha 18 (~75%). Listas de códigos do FSZN não existem em lei publicada.

**Armadilhas confirmadas** (correções da skill)
1. Faixas de 25%/30% não são retenção do empregador para residentes: retém só 13% (calculado pelo MNS, art. 214 §1.2) (engine) → `01-ccg.md` §3
2. Exceção: estrangeiros não residentes permanentes, para quem o agente retém 25% acima de BYN 350.000 e 30% acima de 600.000 (engine) → Tax Code art. 214 §1.2, §1.3
3. Imposto sobre o bruto; o 1% do empregado não reduz a base (engine) → Tax Code art. 199 §3
4. Teto FSZN muda todo mês: 5x salário médio nacional do mês anterior (ex.: junho 3.104,10, teto 15.520,50 para jul/2026) (engine) → Lei 118-Z art. 4 §1
5. Belgosstrakh não tem teto; "34,6%" quebra para altos salários (engine) → Decreto 108 §192.18
6. Piso FSZN é piso da contribuição, proporcional (salário mínimo BYN 858,00 desde 2026-01-01); não vale para contratos civis (engine) → Lei 118-Z art. 9
7. Um só pote anual (BYN 3.910,00/ano no local principal, 259,00 em outros) vale para IR, FSZN e Belgosstrakh (engine) → Tax Code art. 208 §23; Perechen 115 §13
8. Dedução padrão de BYN 216,00 é degrau: some acima de BYN 1.308,00 de renda mensal (custo 28,08) (engine) → Tax Code art. 209 §1.1
9. Previdência adicional voluntária reduz os 28% do empregador (engine) → Decreto 367 §3.4
10. Auxílio-doença é tributável e entra no agregado do adicional; os demais benefícios são isentos (engine) → Tax Code art. 208 §1, art. 199 §8²
11. Auxílio-doença: ganho médio diário vem do FSZN (2 dias para pedir, 3 para resposta); ПУ-3 do trimestre anterior em 3 dias úteis (engine) → Reg. 569 §21; Regras 742 §17
12. Recolhimento do IR é por transação (no dia do saque/transferência), não calendário; adiantamento da 1ª quinzena pode não reter (engine) → Tax Code art. 216 §6, §4
13. Colisão de prazos em sentidos opostos: FSZN volta ao dia útil anterior; Belgosstrakh avança ao seguinte → Lei 118-Z art. 8 §5
14. Citações superadas: decretos 530/531 mortos (vale o Decreto 108 de 2025-03-18); Regras 837/1997 revogadas (vale a Resolução 742 de 2025-12-20, vigência 2026-01-08)
15. Não extrair sexo/data de nascimento do número de identificação (esquema mudou em 2012) → `05-data-dictionary.md`
16. Correções ao material interno anterior (12/07/2026): auxílio material, citação Belgosstrakh, teto FSZN e retenção dos adicionais → `07-qa-report.md`

**O que mais dá errado** (do QA)
- Tratar o adicional de 25%/30% como retenção do empregador para residentes.
- Escorregar o mês do teto 5x (usar o salário médio do próprio mês).
- Prazo do ПУ-3 (mês seguinte ao trimestre) confundido com o dia 20 do 4-фонд.
- Aplicar uma só regra de colisão de prazos.
- Hora extra: o piso legal é adicional sobre o salário já pago, não multiplicador (U-11).

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- U-1 layout da declaração do agente fiscal ao MNS (Resolução MNS 3 de 2026-01-20 não obtida, ~60%); não citar números de campo.
- U-2 Instrução 47 sobre ganho médio (~88%); divisor 29,6.
- U-3 operação FSZN (ssf.gov.by inacessível, ~93%); U-4 estrutura interna do УНП; U-5 relatório Belgosstrakh além da linha 18.
- U-6 pareamento rótulo-código do 4-фонд Tabela 4 (~85%); U-7 ПУ-6 não transcrito (~70%).
- U-8 listas de códigos do FSZN (categoria, demissão, tipo de contrato, abaixo do mínimo, atividade) e formato do arquivo ДПУ: delegadas ao conselho do Fundo; requisito para implementar.
- U-9 migração para ЕПЭУ (canal de declaração ~90%); U-10 Lei 127-Z de 2025-12-30 sem diff.

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Imposto de renda | 13% retido pelo empregador; 25% acima de BYN 350.000 e 30% acima de 600.000 (autoliquidação do residente; retenção para estrangeiro não residente permanente) | 2026 | Tax Code (Parte Especial) 71-Z arts. 199, 214 |
| FSZN empregador | 28% pensão + 6% social; empregado 1% | 2026 | Lei 118-Z |
| Teto FSZN | 5x salário médio nacional do mês anterior (valor móvel) | 2026 | Lei 118-Z art. 4 §1 |
| Belgosstrakh | 0,6% empregador, sem teto, coeficiente por empregador 0,5-2,0 | 2026 | Decreto 108 de 2025-03-18 |
| Salário mínimo | BYN 858,00 | 2026-01-01 | Lei 118-Z art. 9 |
| Dedução padrão | BYN 216,00 (se renda mensal tributável ≤ 1.308,00) | 2026 | Tax Code art. 209 §1.1 |

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
- skill payroll-compliance-belarus (lida em 2026-10-02)

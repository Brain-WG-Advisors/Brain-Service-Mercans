# Suécia

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-sweden` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-08-24 | skill compilada (data da pesquisa no QA da skill) |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-sweden`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano de renda 2026, setor privado, SEK. Fora: setor público, militares, F-skatt/egenavgifter, socialavgiftsavtal. Camada de acordos coletivos (kollektivavtal) não construída (ITP/SAF-LO ~75%; Collectum e Fora não pesquisados).
- **Órgãos:** Skatteverket, Försäkringskassan, Arbetsmiljöverket, Medlingsinstitutet.
- **Relatórios principais:** arbetsgivardeklaration på individnivå (AGI) mensal = huvuduppgift + individuppgift + frånvarouppgift (111 códigos FK, XSD da Skatteverket); pedido de reembolso växa-stöd (novo em 2026); kontrolluppgifter remanescentes (31 jan); FOS/CSR (fråga om skatteavdrag).
- **Confiança da skill:** "PASS WITH NOTES": 0 defeitos críticos, 3 defeitos em publicações da própria Skatteverket, 11 itens abertos (6 abaixo do piso de 95%). A maioria dos módulos 95–99%. Abaixo do piso: jobbskatteavdrag maxima (~55%), bilförmån recálculo no meio do ano (~50%), kontrolluppgifter (~70%), FOS/CSR API (60%), pensão de acordo coletivo (~75%), växa (93%); formulário växa e Collectum/Fora: não disponíveis.

**Armadilhas confirmadas**
1. Total 31,42% não mudou, mas 4 dos 7 componentes sim (föräldraförsäkring 2,00, efterlevande 0,30, arbetsskada 0,10, löneavgift 12,62); empregador estrangeiro 19,80% → 18,80% (engine) → `01-ccg.md` Módulo 5
2. Allmän pensionsavgift (7%) nunca é dedução do payslip; já está na tabela e tem crédito de 100% (engine) → `01-ccg.md` Módulo 5.2
3. Taxa jovem é 20,81% (truncar cada componente), não 20,82%; nascidos 2003–2007, até 25 000 kr/mês, 1 abr 2026–30 set 2027 (engine) → `01-ccg.md` Módulo 5.3
4. Três idades: coluna da tabela de retenção 66; contribuição patronal 67; förhöjt grundavdrag 67 só a partir de 2027; `Alder_1` muda de forma em 1 abr 2026 (engine) → `01-ccg.md`, `04-reports-spec.md` §2.3
5. Retenção é por tabela (29–42); KI = N − 1,16 (engine) → `01-ccg.md` Módulo 6
6. Oito direções de arredondamento num só cálculo; valores do AGI em coroas inteiras (engine) → `01-ccg.md` Módulo 1/6
7. Växa-stöd virou reembolso em 2026: declarar 31,42% cheio; FK062/FK063 expiraram em 202512 (engine) → `01-ccg.md` Módulo 5.6
8. Grandes empregadores (base de IVA > 40 M kr) pagam no dia 12 e declaram no dia 26; teste é de IVA, não de headcount (engine/tesouraria) → `01-ccg.md` Módulo 11
9. AGI não pode ser enviado sem humano: assinatura com e-legitimation em Mina sidor; HTTP 200 + inlamningId não é entrega; payload com erro é descartado em 24h → `03-sir.md`
10. Drivmedelsförmån tem duas bases (×1,2 imposto; ×1,0 contribuições); juros de bilförmån usam 70% da SLR (não 75%); SLR 2026 = 2,55% (engine) → `01-ccg.md` Módulo 10
11. Karensavdrag é um valor (20% da sjuklön de uma semana média), não um dia; limite de 10 ocasiões/12 meses e regra de recorrência de 5 dias (engine) → `01-ccg.md` Módulo 8
12. Semestertillägg é por dia pago (0,43% do salário mensal; 1,82% do semanal); variáveis 12% (engine) → `01-ccg.md` Módulo 7
13. SINK é 22,5% em 2026 (20% em 2027), sem grundavdrag e sem isenção de ajuda de custo; sjöinkomst 15% (engine) → `01-ccg.md` Módulo 6.13
14. Não existem: salário mínimo legal, prêmio legal de hora extra, lei de conteúdo do payslip (SFL 10 kap. 19 § exige só o valor do skatteavdrag), indenização legal, extrato anual → `01-ccg.md` Módulo 4/12, `06-payslip.md`
15. Nunca fixar: statslåneränta de 30 nov e o conjunto anual de tabelas (novo SKVFS por ano) → `01-ccg.md`

**O que mais dá errado** (do QA, traps T1–T23)
- Re-versionar o mapeamento de GL por componente mesmo com o total igual (T1); pensão geral como dedução (T2); calendário "paga quando declara" 14 dias atrasado (T3/T4).
- Frånvarouppgift é por DATA e por tipo de ausência (T15); campos `KRYSS` por presença, `false` é erro (T16); FOS/CSR em ISO-8859-1, o resto UTF-8 (T18); jämkning é sempre percentual (T19); hemortskommun congelada em 1 nov do ano anterior (T21); engångsbelopp usa salário anual esperado (T22); sem informação de imposto = tabela + 10% (T23).
- Arquivo de folha arquivado na Suécia por padrão; exceção UE exige notificar a Skatteverket (T20).

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- U1: máximos anuais de jobbskatteavdrag (53 147 / 37 313) não reproduzíveis; usar a fórmula legal. Sem impacto na retenção.
- U4: taxas compostas de convenções de segurança social: valores verbatim, derivação desconhecida; não projetar para 2027.
- U5: formulário de reembolso växa não publicado.
- U6: kontrolluppgifter (SFL 15 e 22–23 kap. não lidos a nível de campo).
- U7: API FOS/CSR não verificada (portal 93%, API 60%).
- U9: ITP/SAF-LO/Collectum/Fora (não estatutário; canais não pesquisados).
- U11: regra de recálculo da bilförmån se SLR de 31 maio variar ≥2 pp (não achada em IL 61 kap. 5 §).
- Menores: U8 (forskarskatt 25%, 70%), U10 (tetos SGI de föräldrapenning), U12 (faixa de tabelas 29–42), U13 (tabelas de sjukpenning/sjömän: valores 0%), U14 (feriados).

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Arbetsgivaravgifter | 31,42% (18,80% socialavgifter + 12,62% allmän löneavgift) | 2026-01-01 | SAL 2 kap. 26 §; Lag 1994:1920 3 § |
| Faixa jovem | 20,81% (até 25 000 kr/mês) | 2026-04-01 | Lag (2026:100) 2 § |
| Empregador estrangeiro sem fast driftställe | 18,80% (era 19,80%) | 2026-01-01 | Skatteverket (chave P_005) |
| Allmän pensionsavgift | 7% (crédito de 100%; máx. 47 100 kr/ano) | 2026-01-01 | IL 67 kap. 4 §; Lag 1994:1744 |
| SINK | 22,5% | 2026-01-01 | Lag (2025:1355) |
| Basbelopp / SLR | PBB 59 200; IBB 83 400; SLR 2,55% | 2026-01-01 | SKV 433 / Belopp och procentsatser 2026 |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| | | | | |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| | | | | |

## Decisões
- 

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| | | | | |

## Internal Certification (Análise de Reports)
> Frente 5: `frentes/certificacao/estado.md` · Método: [[analise-reports]] · Pasta: `internal-certification/Sweden`

| Pacote | Período | Pass / Finding / NT | Recibo | Situação |
|---|---|---|---|---|
| One Identity Sweden AB (559400-9267) | set/26 | 19 / 6 / 6 | Não | Validado 2026-10-14 com ressalva |

- O zip veio da pasta "Quest Software"; o Kvittens e o master são da **Quest Software AB (556602-0433)**, não da One Identity → recibo, master e banco = Not tested (C-04).
- AGI válida no XSD 1.1, amarra G2N/GL/contracheques; arbetsgivaravgift 31,42% ok.
- **High:** payout de férias acumuladas retido pela tabela mensal, não por engångsbelopp (SFL 11 kap. 17 §) → A-04, aguarda decisão D-02.

## Pendências
- [ ]

## Correções ligadas
- _(links para entradas de [[correcoes]])_

## Fontes
- skill payroll-compliance-sweden (lida em 2026-10-02)

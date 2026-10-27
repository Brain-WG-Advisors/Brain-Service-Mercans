# Malásia

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-malaysia` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | [data?] | skill compilada |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-malaysia`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano-calendário 2026, setor privado, MYR. Employment Act 1955 vale só para Malásia Peninsular e Labuan (Sabah e Sarawak têm Labour Ordinances próprias); EPF, SOCSO, EIS, HRD e MTD são federais.
- **Órgãos:** LHDN/IRBM (MTD/PCB), KWSP (EPF), PERKESO (SOCSO/EIS/SKBBK), HRD Corp (levy), JTKSM (trabalho).
- **Relatórios principais:** CP39 (MTD, mensal, txt), Form E/C.P.8D (anual), Form EA, TP1/TP3, EPF Form A (mensal), arquivo combinado PERKESO SOCSO+EIS v2.0 (mensal), HRD Form 2 (mensal). MTD, EPF, SOCSO, EIS e HRD vencem todos no dia 15 do mês seguinte.
- **Confiança da skill:** nenhuma seção de cálculo abaixo de 95% (maioria 95-99%). Layouts de relatório 50-99%: CP39 e arquivo PERKESO verificados byte a byte; TP3, E/C.P.8D, EA, EPF Form A e HRD Form 2 são DERIVED (50-85%). `06-payslip` 95%, `05-data-dictionary` 90%.

**Armadilhas confirmadas** (correções marcadas na skill)
1. SKBBK não é mais universal: obrigatório para estrangeiros, voluntário para locais desde 8/jul/2026, mas o padrão é descontar (silêncio até 31/ago/2026 inscreve); junho/2026 foi obrigatório e não reembolsável; opt-out é irreversível (engine) → `01-ccg.md` §4.2.1
2. Quatro bases salariais separadas e não aninhadas (EPF, SOCSO/EIS, HRD, tributável); hora extra fora do EPF e dentro do SOCSO/EIS; bônus anual o inverso (engine) → `02-wtc.md` §11
3. EPF é consulta à tabela de faixas (Third Schedule) até RM20.000, não `taxa × salário`; acima disso, percentual exato com total arredondado para cima (engine) → `01-ccg.md` §3.3
4. Divisores: taxa ordinária = mensal ÷ 26; mês incompleto = dias elegíveis ÷ dias corridos (s.18A) (engine) → `01-ccg.md` §11
5. Rescisão (severance): dia = média verdadeira dos 12 meses, não ÷26; paga em 7 dias (engine) → `01-ccg.md` §12, QA C-1
6. MTD abate EPF automaticamente (teto RM4.000/ano) e nunca SOCSO/EIS (só via TP1 C14, máx. RM350/ano) (engine) → `01-ccg.md` §7
7. Arredondamento do MTD: truncar a 2 casas e depois subir a múltiplo de 5 sen; piso RM10 testado antes do zakat (engine) → `01-ccg.md` §7.6
8. Teto RM4.000 do EA é limiar de provisão, não de cobertura → `01-ccg.md` §9
9. Holerite é obrigação das Employment Regulations 1957 reg 9 (12 itens), não da EA s.25A → `06-payslip.md` §2
10. Arquivo PERKESO v2.0: campo SKBBK posições 239-244, tamanho 278 inalterado; v1.0 gera arquivo do tamanho certo com 6 brancos; zero-fill, nunca branco (engine) → `04-reports-spec.md` §8.2, QA §7
11. Todos os canais são portal, não M2M (MyInvois não cobre renda de emprego) → `03-sir.md` §11
12. Base EPF Part F (não cidadão) = máx(salário, salário mínimo, hoje RM1.700) (engine) → `01-ccg.md`
13. Bônus que passa de RM5.000 não reduz a taxa do empregador (continua 13%; Part C 6,5%) (engine) → Third Schedule Part A

**O que mais dá errado** (do QA)
- Posições 239-244 do arquivo PERKESO; flag de participação SKBBK; EPF por faixa; dia de rescisão; divisor s.18A; teto anual RM4.000 do EPF; quatro acumuladores; TP1 não aparece no holerite/EA; arredondamento MTD.
- Carência de multa PERKESO até o mês de contribuição de novembro/2026 (Q31): arquivo malformado não gera sinal de fiscalização.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- O-1: arredondamento EPF Part F (total vs. cada parte) — fontes oficiais conflitam; seguir Third Schedule e conciliar no i-Akaun.
- O-2: SKBBK — lei diz obrigatório, PERKESO diz voluntário para locais; sem gazette de alteração; revisar antes de qualquer build 2027.
- O-3: e-payslip sem aceite satisfaz reg 5(c)(12)?
- O-4: arrears de SKBBK de junho/2026 sem mecanismo de reporte publicado.
- O-5: aviso prévio indenizado (PILON) no SOCSO/EIS não verificado em fonte primária.
- O-6: base de headcount do HRD levy ("employees" vs. "Malaysian employees").
- O-7 a O-10: formatos de identificadores. O-11: valoração de moradia (PR 3/2005) fora da skill. O-12: P.U.(B) 195/2026 e 196/2026 citados, não recuperados.
- PERKESO Borang 117 sem conteúdo/prazo verificados; EPF Late Payment Charge não deve ser fixado (muda todo ano).

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| SKBBK (LINDUNG 24 Jam), só empregado | 0,75% | mês salarial jun/2026 (voluntário p/ locais desde 2026-07-08) | Act A1788; P.U.(A) 206/2026; PERKESO FAQ 13/jul/2026 |
| Teto SOCSO | RM6.000 | 2026 | Act 4 / Act A1724 (via skill) |
| EPF: tabela de faixas até | RM20.000 | 2026 | EPF Act 452, Third Schedule |
| Piso EPF Part F (salário mínimo) | RM1.700 | 2026 | Minimum Wages Order (P.U.(A) 376/2024) |
| Isenção HRD (educação) | 2026-01-15 a 2026-12-31 | 2026-01-15 | P.U.(A) 13/2026 |
| Prazo mensal MTD/EPF/SOCSO/EIS/HRD | dia 15 do mês seguinte | 2026 | skill (SKILL.md item 12) |

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

## Pendências
- [ ]

## Correções ligadas
- _(links para entradas de [[correcoes]])_

## Fontes
- skill payroll-compliance-malaysia (lida em 2026-10-02)

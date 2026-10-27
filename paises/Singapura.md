# Singapura

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-singapore` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | [data?] | skill compilada |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-singapore`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano CPF/folha 2026 e ano de renda 2026 (YA 2027), setor privado com contrato de trabalho, SGD. Fora: servidores, militares, marítimos, domésticos, autônomos, platform workers (regime próprio).
- **Órgãos:** CPF Board, IRAS, MOM (Ministry of Manpower), SWDA (SDL), MSF (licenças pagas pelo governo).
- **Relatórios principais:** CPF EZPay (mensal, web/ESI/FTP), IR8A + Appendix 8A/8B via AIS-API 2.0 (anual, até 1 de março), IR21 (tax clearance de não cidadãos), notificação de retrenchment ao MOM (5 dias úteis).
- **Confiança da skill:** "READY" com 2 seções abaixo de 95% e 11 itens abertos; demais seções 88-99%. Abaixo do piso: layout da Mandatory Retrenchment Notification (~70%) e rota de integração do IR21 (~90%). Regra DERIVED: long service award (CPF).

**Armadilhas confirmadas** (correções marcadas na skill)
1. Não há retenção mensal de imposto de renda: não emitir linha de imposto (engine) → `01-ccg.md` §1
2. CPF do empregador é resíduo (total − parte do empregado); total arredondado ao dólar, parte do empregado sempre truncada (engine) → `01-ccg.md` §2.6
3. CPF sobre OW e AW calculado e arredondado separadamente, depois somado (engine) → `01-ccg.md` §2
4. Teto AW de $102.000 congelado em 17 × $6.000; recalcular em dezembro ou no último mês (engine) → `01-ccg.md` §2.7
5. Faixa etária muda no 1º dia do mês seguinte ao do aniversário; nascidos em 29/fev, em 1º de março (engine) → `01-ccg.md` §2.6
6. Vencimento legal do CPF é o último dia do mês; dia 14 é tolerância e usado no teste OW/AW → `01-ccg.md` §2.9, Open Item 1
7. Declarar salários reais sem teto ao CPF Board (engine) → `01-ccg.md` §2
8. Quatro bases salariais (CPF-OW, CPF-AW, SDL, SHG) que não andam juntas (engine) → `02-wtc.md` §11
9. MBMF por religião, não raça do NRIC; tabela MBMF salta de $6,50 para $15,00 em $3.000 (engine) → `01-ccg.md` §3.2
10. "Basic rate" x "gross rate of pay" diferem só em allowances; divisor de hora extra 52 × 44 = 2.288 (engine) → `01-ccg.md` §6
11. Mês incompleto usa dias de trabalho exigidos (dia de até 5 h conta meio dia), não dias corridos (engine) → EA s.20A
12. CPF do empregado conta no teto de 50% de descontos (EA s.32); retrenchment sem CPF e sem imposto, aviso indenizado sem CPF mas tributável; sem fórmula legal de severance (engine) → `01-ccg.md` §6
13. IR8A: ganhos ESOP/ESOW (d7ii) fora de Others Income e Total Income; AIS-API arredonda renda para baixo e dedução para cima; Appendix 8A decimais descartados no item d8 (engine) → `04-reports-spec.md` SG-RPT-001/004
14. IRAS AIS é M2M, mas o token Corppass exige consentimento interativo; CPF Board, MOM e IR21 são portal → `03-sir.md`
15. Holerite: 11 itens (Third Schedule S 148/2016), itemização obrigatória, exigido mesmo com líquido zero; sem exigência de idioma → `06-payslip.md`
16. Idade de aposentadoria por coorte (62/63/64); reemprego 69 desde 1/jul/2026 → `01-ccg.md` §6.10

**O que mais dá errado** (do QA)
- Ordem de revisão: regra do resíduo do CPF e dois arredondamentos; acumulador AW e recálculo de dezembro; ausência de linha de imposto; mapeamento basic x gross rate; tensão due date x OW (Open Item 1).
- Erro de CPF afeta cota de trabalhadores estrangeiros e portanto o nível da FWL; make-up pay de NS (MINDEF) dentro da base CPF e fora do IR8A.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- OI 1: CPF Regulations 1987 não recuperadas; due date x teste OW (usar dia 14 e declarar a tensão).
- OI 2: layout do Mandatory Retrenchment Notification (~70%); OI 5: especificação do IR21 #SFFS não publicada.
- OI 3: regra de long service award é DERIVED; OI 4: código de pagamento do SDL no CPF EZPay FTP desconhecido (06-09 e 11 sem rótulo).
- OI 6: dois valores só por trecho de busca (teto de relief $80.000 etc.); OI 7: algoritmo de check-digit NRIC/FIN não é público.
- OI 8: taxas de levy de Work Permit da construção não obtidas; OI 9: proibição de recuperar FWL do empregado não verificada; OI 10: item 8 do payslip no MOM; OI 11: melhorias do National Day Rally 2026 sem data, não construir.
- Reverificar ao vivo: per-diem do IRAS e tabelas do PWM. Datados: aumento de CPF de seniores e salários mínimos EP/S Pass em 1/jan/2027, Shared Parental Leave 6 para 10 semanas (filhos nascidos desde 1/abr/2026).

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Teto Ordinary Wage (CPF) | $8.000/mês | 2026 (definitivo) | CPF Act 1953, First Sch. para 5(ea)(iv), S 599/2023 |
| Teto Additional Wage | $102.000 − OW sujeito a CPF no ano | 2026 | CPF Act First Sch. para 5(da) |
| Annual Limit CPF | $37.740 | 2026 | CPFB (via skill) |
| SDL | max(base × 0,25%, $2), base até $4.500; piso $2, teto $11,25 | 2026 | Skills Development Levy Act 1979 s.3 |
| Prazo IR8A/AIS | 1 de março | YA 2027 | ITA 1947 s.68(2) |
| LQS (condição de contratação de estrangeiros) | $1.800/mês | 2026 | MOM Local Qualifying Salary |

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

## Entregas (conferências)
- 2026-10-27 · HRBS-16029 · 62866 Childbirth Allowance sujeito a CPF: [[Research Pipeline/Singapore/2026-10-27-HRBS-16029-62866-CPF/CONFERENCIA|conferência]]

## Correções ligadas
- _(links para entradas de [[correcoes]])_

## Fontes
- skill payroll-compliance-singapore (lida em 2026-10-02)

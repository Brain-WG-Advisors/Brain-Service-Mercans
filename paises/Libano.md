# Líbano

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-lebanon` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-09-11 (relatório QA) | skill compilada |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-lebanon`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** payroll 2026, setor privado, moeda LBP (câmbio de referência 89.500 LBP/USD, paridade de 1.507,5 abandonada). Fora: setor público, militares, autônomos, IVA/IRPJ, domésticos/agrícolas (valores do art. 72 não obtidos), Lei 319 (não está em vigor).
- **Órgãos:** NSSF/CNSS (previdência) e Ministry of Finance (imposto sobre salários): duas inscrições e duas trilhas independentes.
- **Relatórios principais:** NSSF: admissão/desligamento (A-02/A-03, desligamento em 15 dias), declaração periódica de contribuições (A-06), declaração nominal anual de salários (A-08), compensação do salário-família (A-09). MoF: R10 trimestral de retenção (B-02), R5, R7 (fim de ano, desligados).
- **Confiança da skill:** auto-auditoria de 2026-09-11, sem tier. Primário em árabe: Lei NSSF (Decreto 13955/1963) e Código do Trabalho; `[S]` taxas dos ramos (corroboradas x4, decreto da divisão 8%/3% não localizado); `[D]` exemplos, payslip (construído) e valores derivados; `[S!]` parâmetros da Lei 319. Layouts de arquivo: não obtidos.

**Armadilhas confirmadas** (correções da skill)
1. NSSF tem 3 ramos e 3 tetos; total patronal 22,5%, não 25,5% (o 11% S&M combinado é empregador 8% + empregado 3%) (engine) → `01-ccg.md` §0.2
2. Teto S&M é LBP 120.000.000 desde 2025-08-01 (Decreto 887); 140.000.000 nunca vigorou, 90.000.000 antes (engine) → `01-ccg.md` §0.1.2
3. Decreto 887 quebrou a regra de "5x salário mínimo": manter constante datada (engine) → `01-ccg.md` §0.1.2
4. Teto anual é a soma dos tetos mensais, não 12x o do fim do ano (engine) → `04-reports-spec.md` §2.2
5. Lei 67/2026 não tem relação com o teto (trata de aposentados) → `07-qa-report.md` §5.3
6. Decreto 2923 é de 2026-04-24 (Gazeta 30/04, vigência 01/05, Memo 831 de 04/05) → `01-ccg.md` §0.1.3
7. Teto de LBP 7.875.000 do salário-família é derivado; modelar valores por cabeça e limite de 5 filhos (engine) → `01-ccg.md` §0.1.3
8. Pacote misto LBP/USD vira uma só cifra em LBP antes de qualquer base (engine) → `01-ccg.md` §12.3
9. Contribuições NSSF calculadas em LBP, mas pagas em "fresh" USD a partir de 2026-09-01 (Memo 844) → `01-ccg.md` §1.2.4
10. Alíquota efetiva patronal só é 22,5% no salário mínimo; decai para 8,5% (engine) → `02-wtc.md` §11.1
11. Indenização de fim de serviço sobre o salário do art. 68(1), não básico; comissionados 1/12 dos últimos 12 meses (engine) → NSSF art. 51(1)(a)
12. Redução do art. 52 tem degrau aos 20 anos (100%) (engine) → `01-ccg.md` §12.5
13. Salário-família não é custo do empregador e a compensação expira em 1 ano (art. 48(3)) (engine) → `04-reports-spec.md` §4.4
14. Sírios não pagam os 8,5% de EOSI (custo patronal 14%); estrangeiros pagam S&M e Família integralmente (engine) → `05-data-dictionary.md` §3.3
15. Lei 319 não está em vigor: manter 8,5% e fórmula do art. 51 → `01-ccg.md` Módulo 7
16. Só 1 de maio e 22 de novembro são feriados legais no setor privado; afeta vale-transporte por dia (engine) → `01-ccg.md` §1.6
17. "200% em feriado" vale para 1 de maio em farmácias, padarias e restaurantes; hora extra geral é +50% → `07-qa-report.md` §5.7
18. Salário mínimo não paga imposto (dedução mensal de 37.500.000 vs mínimo de 28.000.000); imposto aparecendo = dedução de 2022 (engine) → `01-ccg.md` §6.2
19. Auxílio-escola triplicou (Decreto 3402 de 2026-07-13, substitui o 964); tetos de filhos diferentes (3 escola, 5 família, 5 dedução) → `01-ccg.md` §4.4
20. Inscrição NSSF e MoF são distintas; desligado gera 2 obrigações → `03-sir.md` §0
21. Imposto retido mensalmente mas declarado trimestralmente (R10); "R3/R4" mensal sem base primária, não modelado → `03-sir.md` §3.2
22. "Digitalização do NSSF" não é portal de filing; sem API/schema público → `03-sir.md` §9
23. Licença-maternidade de 7 semanas está desatualizada há 12 anos → `07-qa-report.md` §5.8

**O que mais dá errado** (do QA)
- Declarar só o componente LBP de pacote misto (~LBP 24,96 mi/mês por empregado) (engine).
- Um teto único para os 3 ramos.
- 22,5% como taxa patronal fixa.
- Indenização sobre o básico (subestima 25%).
- Tratar salário-família como custo do empregador.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- 4.21 decreto da divisão S&M 8%/3% (art. 73(2)) não localizado; PwC diverge no EOSI (5% vs 8,5%).
- 4.1 art. 68(3) vs EOSI sem teto; 4.4 divisor de horas para hora extra (208 construído).
- 4.3 valorização de benefícios em espécie (regulamento interno NSSF); 4.5 valores do art. 72; 4.9 multas atuais do art. 80; 4.14 termos do rebate da Lei 47.
- 4.8 se a suspensão da Lei 46 suspende a janela de 1 ano do salário-família (tratar como correndo).
- 4.19 sem norma expressa de contribuição NSSF sobre total convertido (construir como exigido).
- 4.20/4.15/4.16 sem layout, API ou formato de nº NSSF/TIN; 4.11 limites de penhora; 4.12 convênios coletivos; 4.10 refugiados palestinos.
- Payslip é construído (sem layout legal).

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| NSSF S&M | 8% empregador + 3% empregado, teto LBP 120.000.000 | 2025-08-01 | Decreto 887 (14/08/2025), Memo 805; taxas `[S]` |
| NSSF Família | 6% empregador, teto LBP 28.000.000 | 2026 | skill `01-ccg.md` §0.2 |
| NSSF EOSI | 8,5% empregador, sem teto | 2026 | NSSF Lei; `[S]` (PwC diverge, 5%) |
| Salário mínimo | LBP 28.000.000 | 2026 | `01-ccg.md` §0.1.1 |
| Dedução pessoal mensal | LBP 37.500.000 (450.000.000/ano) | Lei do Orçamento 2024 | `01-ccg.md` §6.2 |
| Auxílio-escola | público 12.000.000 / privado 36.000.000 por filho (máx. 3) | 2026-07-13 | Decreto 3402 |

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
| 2026-10-22 | Ericsson ME (planilha "Compliance feedback list", pedido da Manju por chat) | WT 1026/1027 adiantamentos, 1043 aviso prévio, 1041 indenização, 1042 gratuity, 1044 licença | Respondido na planilha com fonte primária (NSSF Code art. 68(1), 68(3), 51(1)(a); DL 144/1959 arts. 46, 49). Nenhuma norma NSSF exclui esses pagamentos da base; nota anterior "severance outside NSSF" retirada. Rascunho: `rascunhos/2026-10-22-ericsson-me-respostas-LB-JO-EG.md` | Não |

- [[rascunhos/2026-10-22-ericsson-me-respostas-LB-JO-EG|2026-10-22-ericsson-me-respostas-LB-JO-EG]]: Respostas Compliance Ericsson ME para Líbano, Jordânia e Egito (7 linhas)

## Pendências
- [ ] Ericsson ME, coluna Detail v1.7: "advance = neither taxable nor insurable" e "severance outside NSSF" sem fonte primária (o art. 68(1) não exclui nenhum dos dois). Vale também para a Jordânia (adiantamento; sem hub). Achado de 2026-10-22, fora do pedido.

## Correções ligadas
- _(links para entradas de [[correcoes]])_

## Fontes
- skill payroll-compliance-lebanon (lida em 2026-10-02)

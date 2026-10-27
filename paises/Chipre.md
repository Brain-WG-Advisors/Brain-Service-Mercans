---
tipo: pais
codigo: "CY"
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
skill: "payroll-compliance-cyprus"
tickets_abertos: 
tickets_conferidos_em: 
atualizado_em: 2026-10-27
---
# Chipre

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-cyprus` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | [data?] | skill compilada |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-cyprus`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano fiscal 2026, empregadores do setor privado, moeda EUR, só áreas controladas pela República. Fora: servidores/setor público, militares, autônomos (GHS 4,00%, SI 16,6%), contribuintes voluntários.
- **Órgãos:** Tax Department (TFA: T.D.7, PAYE, D.A.S.), Social Insurance Services/ΥΚΑ (SISnet e Ergani), Health Insurance Organisation/ΟΑΥ (GHS), Department of Labour Relations, HRDA/ΑνΑΔ.
- **Relatórios principais:** declaração mensal de PAYE (CY-RPT-01); T.D.7 empregador anual; T.D.63/63A certificado de remuneração; remessa mensal dos 6 fundos via SISnet (CY-RPT-04); Ergani (admissão, rescisão, termos de emprego); D.A.S. não residentes (RPT-08); payslip (RPT-09). Tudo é portal com CY Login pessoal, sem M2M.
- **Confiança da skill:** "READY FOR REVIEW", sem tier; 6 seções abaixo do piso de 95% (só 1 passada, sem segundo revisor). Núcleo (faixas, 6 fundos, tetos, algoritmo PAYE) rastreado a fontes oficiais. Derivado: layouts T.D.7, declaração mensal e remessa mensal (~55-60%); códigos `CY-*` são provisórios. T.D.63A (~92%) transcrito do modelo oficial.

**Armadilhas confirmadas** (correções da skill)
1. Faixas 2026 são 0 / 22.000 / 32.000 / 42.000 / 72.000 (0/20/25/30/35%), não os rascunhos circulantes (N. 244(I)/2025) (engine) → `01-ccg.md`
2. Contribuição de 8% ao Central Holiday Fund integra as remunerações e eleva a base dos outros 5 fundos, inclusive deduções do empregado (engine) → `01-ccg.md` §5.3, Módulo 11
3. Três tetos no mesmo payslip: SI/CHF/RF/HRDA EUR 5.742/mês; Social Cohesion sem teto; GHS EUR 180.000/ano agregado (engine) → `01-ccg.md`
4. Teto semanal começa em 2026-01-05, mensal em 01-01; máximo anual difere por frequência (68.900 vs 68.904) (engine) → `01-ccg.md`
5. PAYE anualizado, apartado, depois ÷13 (com 13º) ou ÷12 ou ÷52 (engine) → T.D.59A linha C3
6. Teto de 1/5 das deduções mede-se sobre B6 do T.D.59A, não sobre o bruto (engine) → Lei 118(I)/2002 art. 14A(2)
7. Não há prêmio legal de hora extra (Lei 63(I)/2002 só limita duração); não usar 1,5x → `01-ccg.md`
8. Não há subsídio em dinheiro isento; única exceção é uso de carro próprio em serviço → BIK guide §1.14
9. BIK: PAYE sobre dinheiro + BIK, descontado só da parte em dinheiro (engine) → BIK guide §2.2
10. SI de 22,8% inclui 5,2% do Estado; empregador + empregado = 17,6% (8,80%/8,80%); com plano de pensão patronal sem contribuição do empregado vira 4,45%/13,15% (engine) → `01-ccg.md`
11. Payslip deve mostrar 5 contribuições patronais (SI, Social Cohesion, Redundancy, HRDA, GHS); CHF é item condicional → Lei 35(I)/2007
12. Indenização por redundância sai do Redundancy Fund (empregador paga levy de 1,2%); tabela 2 a 4 semanas por ano, limite 25 anos (engine) → Termination Law, 4º Anexo
13. Pagamentos de longo período (13º, comissão) são testados contra o teto do próprio período (engine) → `01-ccg.md`
14. Sem T.D.59A: só admitir deduções B7 e B8 (engine) → T.D.59A nota 15
15. Cyprus é portal round-trip, sem M2M → `03-sir.md`
16. Correções do build: frequência de pagamento (art. 9(1)), deduções permitidas (art. 10), payslip em 5 dias úteis, taxas GHS de 1,70%/1,65% são históricas (2026: 2,65%/2,90%), TIC não é número de IVA → `07-qa-report.md` §4.8

**O que mais dá errado** (do QA)
- Esquecer a pergunta "empregador isento do CHF?": dá duas respostas (custo patronal 15,40% vs 23,40% + gross-up; no exemplo de EUR 4.000, EUR 25,65 a menos de líquido e EUR 369,28 a mais de custo).
- Fontes comerciais contradizem a primária em hora extra e faixas.
- Inconsistência de data do salário mínimo nas páginas da própria autoridade (§4.1); prazo do T.D.7 inconsistente no calendário oficial (§4.6).

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- §3.1 tabelas I e II do Central Holiday Fund (férias acima de 4 semanas, ~60%); só 8% confirmado, não interpolar.
- §3.2 valoração de BIK que não seja carro (~55%): não afirmar valor de moradia/empréstimo.
- §3.3 licenças paternidade, parental, cuidadores, força maior (~35%); §3.4 detalhe de auxílio-doença (~40%); §3.5 feriados obrigatórios (~50%).
- §3.6 tributação de pagamentos de rescisão (~40%, deixado condicional); §3.10 retenção de registros (~30%); §3.11 idioma do payslip (~60%; grego ou bilíngue é seguro).
- §3.7 layouts T.D.7 e declaração mensal derivados (60%/55%); §3.8 XSD de admissão do Ergani não obtido; §3.9 formatos de identificadores (TIC ~75%; SI number, ERN, ID: desconhecidos, não implementar validações).
- Não encontrados: prazo de rescisão no Ergani, prazo do T.D.63, form do carro ponto a ponto, lista de BIK não tributável, mecânica de delegação TFA/SISnet; TFA coexiste com TAXISnet (§4.5, ~70%); elegibilidade BIK para insurable (~70%).

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Faixas de IRS | 0% até 22.000; 20% até 32.000; 25% até 42.000; 30% até 72.000; 35% acima | 2026-01-01 | Lei 118(I)/2002, 2º Anexo (1)(γ), N. 244(I)/2025 (Gazette 5070, 31.12.2025) |
| Seguro social | 8,80% empregado / 8,80% empregador; teto EUR 5.742/mês (1.325/semana) | 2026 (degrau em 2029) | Social Insurance Law e Regulamentos 2010-2025 |
| GHS | 2,65% empregado / 2,90% empregador; teto EUR 180.000/ano | 2026 | GHS Law art. 24 |
| Redundancy Fund / HRDA / Social Cohesion | 1,20% / 0,50% / 2,00% (empregador); Cohesion sem teto | 2026 | Employer's Guide (ΥΚΑ) |
| Central Holiday Fund | 8% empregador (se não isento, formulário ΥΚΑ 1-005) | 2026 | Employer's Guide (ΥΚΑ) |
| Reliefs de expatriado | art. 8(21A) 20%/EUR 8.550; art. 8(23A) 50%/EUR 55.000 | 2026 | `01-ccg.md` §6.3.4 |

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
- skill payroll-compliance-cyprus (lida em 2026-10-02)

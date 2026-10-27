---
tipo: pais
codigo: "BH"
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
skill: "payroll-compliance-bahrain"
tickets_abertos: 
tickets_conferidos_em: 
atualizado_em: 2026-10-27
---
# Bahrein

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-bahrain` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | [data?] | skill compilada (relatório QA de 2026-08-27, veredito "SHIP WITH DISCLOSED GAPS") |
| [[design]] | ⏳ | | |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-bahrain`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** payroll 2026, setor privado, moeda BHD (3 casas decimais). Fora: servidores públicos, forças armadas, autônomos; domésticos são escopo parcial (WPS, 30 dias de férias, gratificação art. 116, sem SIO/EOSB).
- **Órgãos:** SIO (Social Insurance Organization), Ministry of Labour, LMRA (WPS v2, work permits), bancos/BENEFIT, CBB; NBR só para VAT/DMTT (nada de payroll). Sem imposto de renda pessoal.
- **Relatórios principais:** SIO Form 2 registro (BH-SIO-001); SIO Form 3 demonstrativo mensal + movimentação (BH-SIO-002); SIO Form 3 anual base janeiro, vence 1º de janeiro (BH-SIO-003); LMRA WPS arquivo mensal de salários (BH-WPS-001) e justificativa de não pagamento/pagamento parcial (BH-WPS-002). Nada ao NBR.
- **Confiança da skill:** sem tier; veredito "SHIP WITH DISCLOSED GAPS". Seções ao nível de ~95%: CCG, SIR, payslip; abaixo do piso: WTC (~93%), reports spec (~85%), data dictionary (~92%). TIER-B/derivado: layouts SIO Forms 1-5 (derivados, ~70-75%), regime GCC (~70%).

**Armadilhas confirmadas** (correções da skill)
1. Base contributiva SIO fixada em janeiro para o ano todo; admitido depois usa o mês de admissão (engine) → `01-ccg.md`, SI Law art. 17
2. Quatro bases salariais distintas (A básico, B salário, C contributivo SIO, D EOSB) (engine) → `01-ccg.md` §1.1–1.4
3. 1% de desemprego do empregador é pago pelo Labour Fund: total patronal 2026 = 18% (15% + 3%), não 19%; expatriado também paga o 1% do empregado (engine) → Decreto 78/2006
4. Nenhuma norma traz 15%: vem do escalonamento (Lei 14/2022 art. 4: 13% em 2024, 14% em 2025, 15% em 2026, 16%, 17% em 2028); usar tabela por ano (engine) → `01-ccg.md`
5. Mês de entrada/saída tudo-ou-nada em 15 dias úteis; arredondamento no total do empregador a 100 fils (engine) → SI Law arts. 25, 26
6. Bônus anual qualificado entra como bônus ÷ 12 no janeiro seguinte, limitado a um mês de básico (engine) → Order 2/2006 art. 1(5); corrige o WTC anterior
7. Comissão tem duas janelas (média do ano anterior para SIO; últimos 3 meses para gratificação/férias) (engine) → Order 2/2006 art. 1(2)-(3); LL art. 47
8. Trabalho em descanso/feriado = 250% do dia (salário + 150% adicional), não 150%; a tradução inglesa do art. 57 omite o primeiro limbo (engine) → LL arts. 57(b), 64
9. Não há payslip estatutário; regra da folha assinada foi revogada (Decreto 59/2018, pagamento via WPS) → `06-payslip.md`
10. Conformidade WPS é medida só sobre Salário Fixo + Social Allowance (engine) → `03-sir.md`, manual LMRA WPS v2
11. Cota do empregado SIO não descontada nunca pode ser recuperada; sem linha retroativa no payslip (engine) → SI Law art. 28
12. Sem imposto de renda nem salário mínimo privado; não criar campo/linha de imposto zero → `01-ccg.md` §3, §5.4
13. SIO e WPS são portais (eKey), sem M2M do lado do empregador → `03-sir.md`
14. Expatriado não-GCC: pensão suspensa (Order 3/1981 art. 1); só 3% acidente (empregador) + 1% desemprego (empregado), mais EOSB do empregador 4,2%/8,4% em base mais estreita (Res. 109/2023) → `01-ccg.md` §2.5, §4
15. Contribuição sobre base antes de qualquer desconto (faltas, multas); obrigatória mesmo com contrato suspenso (arts. 22, 23) (engine)

**O que mais dá errado** (do QA)
- Confundir base C (SIO) com base D (EOSB) em expatriados, o erro mais caro.
- Presumir teto de BHD 4.000 no EOSB (a skill aplica sem teto, ~80%).
- Defeitos em documentos oficiais: art. 57 em inglês (D1), Res. 109/2023 art. 10 (D2), 14 vs 15 dias entre duas publicações LMRA (D3).

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- U1 Sistema Unificado GCC (~70%): texto primário não obtido; empregado arca com a diferença.
- U2 EOSB: teto BHD 4.000 e base D (~80%/85%); U6 gratificação acima do teto.
- U4 prêmio 250% vs 150% (~85%); U5 fixação em janeiro obrigatória ou permissiva (~90%).
- U8 ordem de consumo do teto de 100% de allowances (~75%); U9 horas extras de categorias isentas (~70%); U10 bônus gate vs cap (~80%).
- U11 janela WPS 14 ou 15 dias; U12 códigos de justificativa WPS (~40%); U13 layout físico do arquivo WPS (~75%); U14 líquido vs bruto na comparação WPS (~70%).
- U15 dígito verificador do CPR (~60%); layouts SIO Forms 1-5 derivados.
- Feeds ao vivo (nunca fixar): alíquota patronal OAD, feriados, bancos WPS, taxas LMRA.

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| Pensão (OAD) bareinita | empregador 15% + empregado 7% | 2026-01-01 | Lei 14/2022 art. 4 (escalonamento +1 p.p. a cada 1º jan até 17% em 2028) |
| Acidente de trabalho | 3% empregador | 2026 | SI Law (skill) |
| Desemprego | 1% empregado; 1% patronal pago pelo Labour Fund | 2026 | Decreto 78/2006 art. 6(2) |
| Teto salarial contributivo | BHD 4.000,000 | 2026 | SI Law art. 17 |
| EOSB expatriado | 4,2% / 8,4% só do empregador | março/2024 (ver skill; transitório art. 13) | Res. PM 109/2023 |
| WPS v2 | obrigatório | 2026-01 | Res. 68/2019 e 22/2021; manual LMRA WPS v2 |

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
- skill payroll-compliance-bahrain (lida em 2026-10-02)

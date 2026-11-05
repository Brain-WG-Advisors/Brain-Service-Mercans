---
tipo: pais
codigo: "NA"
etapa_research: "concluida"
etapa_research_data: "2026-07"
etapa_design: "em andamento"
etapa_design_data: 2026-09-18
etapa_producao: "outro time (Baker Hughes Namibia em implementação, HRBS-12074)"
etapa_suporte: "1 aberto(s): HRBS-16649"
etapa_suporte_data: 2026-11-02
ccg: "sem versão no hub"
ccg_data: 
wtc: v2.5
wtc_data: 
dd: v2.1
dd_data: 
report_specs: "sem versão no hub (SSC Form Ten, PAYE 5, ETX)"
report_specs_data: 
sir: 
sir_data: 
payslip: "configurado, em revisão de Compliance (HRBS-14605); sem versão no hub"
skill: 
tickets_abertos: 1
tickets_conferidos_em: 2026-10-27
versoes_fonte: "nome do arquivo no Drive (Country Folders/Namibia), lido em 2026-10-27; sem data de versão"
atualizado_em: 2026-11-02
---
# Namíbia (Namibia)

> Hub do país. Índice: [[00-INDEX]] · Skill: não há · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | ~2026-07 [INCERTO] | CCG, WTC e Report Specs (SSC Form Ten, PAYE 5, ETX) existem segundo os tickets; versões não citadas; sem skill. Chats citam a Namíbia só de passagem ("toques leves") |
| [[design]] | 🔄 | 2026-09-18 | Relatórios (Monthly PAYE Return, G2N, SSC Contribution Return) em configuração, previstos até 2026-09-25, depois revisão de Compliance; Payslip configurado, em revisão de Compliance (HRBS-14605) |
| Produção (outro time) | — | | Entidade Baker Hughes Namibia em implementação (HRBS-12074, fora do nosso escopo) |
| [[suporte]] | ✅ | 2026-10-27 | API 27/10: 6 fechado(s): HRBS-12072, HRBS-12101, HRBS-12111, HRBS-12483, HRBS-13602, HRBS-14605. Antes (2026-10-27): Os 6 tickets da Baker Hughes Namibia estão Resolved (consulta à API em 2026-10-27; o status anterior, "6 sem resposta", vinha da carga de 2026-10-02 e estava desatualizado). Ver [[#Cliente Baker Hughes (África)]] |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| Compliance WTC | sem versão citada | — | Google Sheets (link nos tickets) | Pension flag = Yes em 62100, 62146–62149, 62961 (em questão, HRBS-12483); combinação SSNC=No/ECF=Yes/Pension=No existe (HRBS-12072) |
| CCG | sem versão citada | — | Google Docs | Posição: WT 2551 = MSD EE Contribution, não é dedução pré-imposto (Mohit, 2026-08-24) |
| Report Specs (SSC Form Ten, PAYE 5, ETX) | sem versão citada | — | Drive | Só specs, sem samples (HRBS-12101) |
| Payslip | — | 2026-09-18 | — | Configurado, em revisão de Compliance (HRBS-14605) |
| VET Levy Return, IT12E (IT14E) | não existem | 2026-09-18 | — | "Só temos esses relatórios" (Mohit, HRBS-14605) |

## Valores-chave (com vigência)
Valores do cliente/implementação estão marcados ⚠️ sem fonte. As linhas SSC com fonte oficial entraram em 2026-10-08 (pesquisa em `rascunhos/2026-10-08-pesquisa-NA-SSC-PAYE.md`).
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| Teto SS do empregado (WT 2551) | NAD 99/mês | ⚠️ vigência? | 2026-02-28 (ver linhas SSC com fonte) | ⚠️ sem fonte (alegação do solicitante, HRBS-13602) |
| Alíquota marginal usada no exemplo | 30% | ⚠️ vigência? | — | ⚠️ sem fonte (HRBS-13602) |
| SSC EE/ER | 0,9% / 0,9% de insurable earnings, teto ~NAD 11.000/mês (cliente diz haver fontes conflitantes) | ⚠️ vigência? | 2026-02-28 (ver linhas SSC com fonte) | ⚠️ sem fonte, [INCERTO] não confirmado (HRBS-14605) |
| SSC (MSD Fund) EE / ER | 0,9% / 0,9% do basic wage | 1995 | | Social Security Act 34/1994; GN 198/1995 reg. 8 (lac.org.na/laws/1995/1181.pdf) |
| SSC: base mensal mín./máx.; contribuição máx. por lado | NAD 500 / 11.000; NAD 99 | 2025-03-01 | 2026-02-28 | GN 275/2024, GG 8461 (lac.org.na/laws/2024/8461.pdf) |
| SSC: base mensal mín./máx.; contribuição máx. por lado | NAD 500 / 12.500; NAD 112,50 | 2026-03-01 [INCERTO: PwC/Sage dizem adiado para 2026-09-01 por Public Notice SSC de 2026-08-07, não achado em fonte primária] | | GN 236/2026, GG 8975 de 2026-07-15 ("with effect from 1 March 2026"; lac.org.na/laws/2026/8975.pdf) |
| SSC: teto da base mensal (futuro) | NAD 14.000 / 15.000 / 16.000 | 2027-03-01 / 2028-03-01 / 2029-03-01 | | GN 236/2026 (tabela; leitura do PDF desalinhada, conferir) |
| Deduções do empregado no PAYE | Só pension/provident (s.17(1)(n)), retirement annuity (q), apólice de educação (qA) e (w); teto conjunto NAD 150.000/ano. **Contribuição SSC não é dedutível** | ano de avaliação a partir de 2022-03-01 | | Income Tax Act 24/1981 s.17(1) e 17(2) (texto anotado LAC, atualizado até Act 4/2024; conferido em 2026-10-08); brochura NamRA "Taxation of Individuals who earn a Salary" |
| Prazo do Monthly PAYE Return | 20 dias após o fim do mês | ⚠️ vigência? | — | ⚠️ sem fonte (cliente, HRBS-14605) |
| Ano fiscal | março a fevereiro | ⚠️ vigência? | — | ⚠️ sem fonte (cliente, HRBS-14605) |
| VET Levy | 1%, só empregador, acima de limite de folha | ⚠️ vigência? | — | ⚠️ sem fonte (cliente, HRBS-14605) |
| Prazo IT12E / IT14E | 30 de junho após o fim do ano fiscal | ⚠️ vigência? | — | ⚠️ sem fonte (cliente, HRBS-14605) |

## Decisões
- 2026-08-24: pela informação disponível, o WT 2551 (SS Employee Share) = MSD EE Contribution e NÃO é dedução pré-imposto; reatribuído ao Wallisson para verificar e resolver. A decisão final do Wallisson está pendente — Mohit Jain, citando o CCG (HRBS-13602)
- ~2026-07-28: a combinação SSNC=No / ECF=Yes / Pension=No já existe na WTC; a combinação Tax=Yes / SSNC=Yes / Pension=No provavelmente não existe, a confirmar com o Wallisson — Mohit Jain (HRBS-12072)
- 2026-10-08: base legal confirma a posição do CCG: o WT 2551 (MSD EE) NÃO reduz a base do PAYE (WT 2552). O Income Tax Act 24/1981 s.17 só admite pension/provident, retirement annuity e apólice de educação (teto NAD 150.000); SSC não consta, e o Social Security Act s.42 isenta só a Comissão/fundos — pesquisa Claude, citações conferidas (HRBS-13602; `rascunhos/2026-10-08-pesquisa-NA-SSC-PAYE.md`)
- ~2026-09-18: só existem Monthly PAYE Return, G2N e SSC Contribution Return (+ Payslip); não existem VET Levy Return nem IT12E — Mohit Jain (HRBS-14605)

## Suporte (tickets)
Todos de Baker Hughes (Baker Hughes Namibia), pedidos por Daniel Kelvin Balogun.
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| 2026-11-02 | HRBS-16649 (Baker Hughes Energy Services Namibia, UAT; Live/BAU) | Daniel pede confirmação do método de PAYE do HRB (anualização + true-up YTD) em 6 perguntas: projeção do recorrente e pagamento único, fórmula "anual − retido ÷ meses restantes", admissão no meio do ano, verbas recorrentes/códigos de ajuste, mudança salarial, falta de TIN | Publicado 18:42 UTC (448 car.): Q6 = alíquota máxima sem o certificado de registro (Act 24/1981, Sch. 2 §12(2)); Q1–5 dependem das tabelas de dedução da NamRA e da forma de aplicá-las (§9(1)) → pedimos ao Daniel as tabelas que ele usou. Base lida: s.1 "gross income"; Sch. 2 §§9(1), 10, 12(2), 12A (acerto anual só p/ quem está desde 1/3). namra.org.na fora do ar em 02/11 (API, Chrome e Wayback). Act em `raw/docs/oficiais/NA/`. Pendente: responder Q1–5 com as tabelas | Não |
| ~2026-09-24 | HRBS-14605 | Confirmação de configuração dos relatórios estatutários | Resolved 2026-10-08: fechado pelo suporte (Pradeep) por falta de resposta do cliente. A confirmação de SSC e a revisão dos relatórios não aconteceram no ticket | Não |
| 2026-08-24 | HRBS-13602 | WT 2551 não reduz a base do Payroll Tax (2552) | Resolved 2026-08-24. Mohit: não é pré-imposto; nossa confirmação em 24/08 (fonte: NamRA, "Tax on Individuals", Allowable Deductions). Cliente citou outros problemas (anualização, faixas desatualizadas) | Não |
| ~2026-07-30 | HRBS-12483 | Pension flag dos códigos 62100, 62146–62149, 62961 (Compliance = Yes, cliente = No) | Resolved 2026-09-16 (Mohit fechou sem resposta do cliente). Nossa resposta de 04/08: o WTC de compliance fica como está; Baker Hughes configura pelo WTC do próprio fundo (No nesses códigos); 62961 já é "No (Typically)". Pedimos confirmação de que os valores vieram do administrador do fundo — sem resposta | Não |
| ~2026-07-28 | HRBS-12072 | Mais pay elements (duas combinações de flags) | Resolved 2026-08-10: fechado pelo suporte por falta de resposta do cliente | Não |
| ~2026-07-26 | HRBS-12101 | Samples dos relatórios SSC Form Ten, PAYE 5, ETX | Resolved 2026-08-12 com nossa resposta: ETX tem sample (Template Version 2 da NamRA); SSC Form 10 é ação no portal mySSC, sem arquivo; PAYE 5 não é fornecido pela NamRA, é gerado pelo empregador | Não |
| ~2026-07-22 | HRBS-12111 | Revisão da Report Matrix da Namíbia | Resolved 2026-08-10 com nossa revisão e arquivo corrigido: ETX adicionado; SSC corrigida para N$99 (GN 8461) nos códigos 2551/2550; PAYE em 2552; Taxable Total 58008; moeda NAD. ⚠️ Ver Pendências: o teto usado (N$99) pode já estar superado pela GN 236/2026 | Sim (Report Matrix do cliente) |

- [[rascunhos/2026-10-08-pesquisa-NA-SSC-PAYE|2026-10-08-pesquisa-NA-SSC-PAYE]]: Pesquisa HRBS-13602: contribuição SSC (WT 2551) como dedução pré-PAYE na Namíbia

## Pendências
- [x] (04/11, gmail) E-mail "Fwd: Wave 2 Namibia change on SS cap" (Daniel, Baker Hughes; HRBS-16791): respondido pelo usuário em 03/11 22:51 BRT, só a parte nossa: "NAD 112.50 per employee and per employer is the correct cap from 1 September 2026, as we confirmed in HRBS-14605." Lei: GN 236/2026, GG 8975 (teto NAD 12.500 "with effect from 1 March 2026"; PDF em raw/docs/oficiais/NA/2026-11-03-GG-8975-GN-236-2026-SSC.pdf); 01/09/2026 = comunicado da SSC (só em fontes secundárias). Se o sistema aplica: L2 (Ankit) no HRBS-16791. Artefatos nossos com o teto antigo: item abaixo.
- [x] HRBS-13602: respondido em 2026-08-24 (2551 não é pré-imposto; fonte NamRA). Ticket Resolved. Ainda vale conferir se o WTC de compliance marca 2551 como redutor da base (se sim, é erro nosso → [[correcoes]]) — Wallisson
- [ ] Identificar os tickets citados de "metodologia de anualização" e "constante de faixas desatualizada" — Compliance [INCERTO] (HRBS-13602)
- [x] Decidir se 62100, 62146–62149, 62961 são pensionáveis: respondido em 2026-08-04 (configurar pelo WTC do fundo do cliente); ticket fechado em 2026-09-16 (HRBS-12483)
- [ ] Confirmar se a combinação Tax=Yes / SSNC=Yes / Pension=No existe — ticket HRBS-12072 fechado em 2026-08-10 sem essa confirmação; reabrir só se o cliente voltar
- [x] Samples de SSC Form Ten, PAYE 5 e ETX: respondido em 2026-08-12 (HRBS-12101)
- [x] Revisar a Report Matrix: feito em 2026-08-10 (HRBS-12111)
- [ ] (03/11, gmail) **Mapa dos artefatos com o teto MSD/SSC antigo (lido no Drive em 03/11, só leitura):** com N$11.000/N$99 → CCG "Namibian Payroll Configuration Research" (tabela de contribuições + fluxo "N$11,000 Ceiling (from 1 Mar 2025)"); CSOP "Namibia Payroll CSOP" (N$11.000, N$99 EE e ER); Payslip "NA_Compliance_Payslip_Generator" (Namibia (EN): SSC 99,00 e "capped NAD 11,000"; Population Range); Reg Flow "Namibia Reg Flow" (07 - Design, NA Reg Flow: "Ceiling Amount: 11000"); simulações de pesquisa "Namibia_G2N_Payroll" (gsheet e xlsx, Ref Data 11000; G2N N$99) e "Namibia Summary" (.xlsx ×2, 99); Tax Calculator "Namibia_G2N_Payroll_FY2024-25.xlsx" (nota "ceiling=11000"); simulações de produto "NA_Simulation Template" e "NA_Simulations Acceptance Testing" (Ceiling on Base 11.000; de quem são: confirmar). Sem valor de teto: WTC V2.5, DD V2.1, Form 10/10A spec, NA_SSC_mySSC_Form10A_Mapping, ETX mapping, NA_Specific_Gross_to_Net, Draft Regulations (Dev, CT-4271), Pension pretax. Arquivados (não mexer): DD antigo, CCG "Theopolina", Report Booklet. Mudança = 01/09/2026 N$500/N$12.500, N$4,50/N$112,50 por lado; futuros 14.000 (01/03/2027), 15.000 (2028), 16.000 (2029). Fazer com ok do usuário + ticket ao Dev (Live).
- [ ] (03/11, gmail) **Confirmado: a CCG da Namíbia (Google Doc "Namibian Payroll Configuration Research", export txt lido em 03/11) ainda traz só MSD até 28/02/2025 (N$9.000/N$81) e a partir de 01/03/2025 (N$500/N$11.000; N$4,50/N$99); falta a linha de 01/09/2026 (N$12.500; N$112,50 por lado) e os tetos futuros (14.000/15.000/16.000 em 01/03/2027-29). O WTC V2.5 (2550/2551) não traz valor de teto.** Baker Hughes (Leticia, via Daniel, 03/11) precisa do 112,50 no parallel run; HRBS-16791 (L2, Ankit, Live/BAU). Ação: CCG versão nova + ticket de alteração ao Dev (regra 9; ticket = janela Suporte), com ok do usuário.
- [ ] **Possível erro nosso (HRBS-12111):** a revisão de 10/08 fixou a SSC em N$99 (teto NAD 11.000, GN 8461), mas a GN 236/2026 (GG 8975, publicada em 2026-07-15) já elevava o teto para NAD 12.500 / N$112,50 a partir de 2026-03-01 (ou 2026-09-01, ver [INCERTO] em Valores-chave). Conferir na fonte primária e, se confirmado, registrar em [[correcoes]] e avisar o cliente — Wallisson
- [ ] Confirmar taxa e teto da SSC aplicados — Compliance (HRBS-14605). Fonte oficial já registrada em Valores-chave; falta só decidir a data do teto NAD 12.500 (2026-03-01 no Gazette × 2026-09-01 segundo fontes secundárias)
- [ ] Revisão de Compliance dos relatórios (após 25/09) e do payslip — Compliance (HRBS-14605)
- [ ] Decidir sobre VET Levy Return, IT12E e IT14E, que não existem — Mohit/Compliance (HRBS-14605)
- [x] Fila sem resposta e com SLA negativo (HRBS-12072, 12101, 12111, 12483; Congo 12110 e 14055): conferido em 2026-10-27, todos Resolved exceto o HRBS-12110 do Congo (In Progress). Ver [[#Cliente Baker Hughes (África)]]

## Cliente Baker Hughes (África)
Mesmo cliente e mesmo solicitante na Namíbia e no [[Congo]] (entidades em implementação, "Legal Entity Phase: Implementation"). Estado conferido na API em 2026-10-27 (`raw/tickets/api/2026-10-27/`):
- Namíbia: HRBS-12072, 12101, 12111, 12483, 13602, 14605: todos Resolved.
- Congo: HRBS-12472, 13841, 14054, 14055: Resolved; **HRBS-12110 (Report Matrix do Congo): In Progress**, nossa pergunta de 2026-10-20 ao cliente sobre o que ele precisa agora, sem resposta.
- Padrão: as duas Report Matrix foram abertas na mesma semana (21–22/07); vários tickets foram fechados pelo suporte por falta de resposta do cliente, não por solução confirmada.
## Correções ligadas
- _(nenhuma correção confirmada; a divergência sobre o WT 2551 entre cliente e CCG segue aberta, ver Pendências)_ — ver [[correcoes]]

## Fontes
- raw/tickets/extracao/2026-10-02-tickets-AF.md
- raw/chats/2026-10-01-mercans-compliance.md (menção de passagem)

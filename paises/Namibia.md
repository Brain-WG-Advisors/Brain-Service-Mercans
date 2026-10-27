# Namíbia (Namibia)

> Hub do país. Índice: [[00-INDEX]] · Skill: não há · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | ~2026-07 [INCERTO] | CCG, WTC e Report Specs (SSC Form Ten, PAYE 5, ETX) existem segundo os tickets; versões não citadas; sem skill. Chats citam a Namíbia só de passagem ("toques leves") |
| [[design]] | 🔄 | 2026-09-18 | Relatórios (Monthly PAYE Return, G2N, SSC Contribution Return) em configuração, previstos até 2026-09-25, depois revisão de Compliance; Payslip configurado, em revisão de Compliance (HRBS-14605) |
| Produção (outro time) | — | | Entidade Baker Hughes Namibia em implementação (HRBS-12074, fora do nosso escopo) |
| [[suporte]] | 🔄 | 2026-09-24 | 7 tickets da Baker Hughes; 6 sem resposta de Compliance; SLA negativo |

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
| ~2026-09-24 | HRBS-14605 | Confirmação de configuração dos relatórios estatutários | Open. Em desenvolvimento (Katrin Rudi, até 25/09); sem VET Levy nem IT12E; sem resposta do Wallisson sobre SSC | Não |
| 2026-08-24 | HRBS-13602 | WT 2551 não reduz a base do Payroll Tax (2552) | Open. Mohit: não é pré-imposto; reatribuído ao Wallisson, sem resposta. Cliente cita outros problemas (anualização, faixas desatualizadas) | Não |
| ~2026-07-30 | HRBS-12483 | Pension flag dos códigos 62100, 62146–62149, 62961 (Compliance = Yes, cliente = No) | Open, sem resposta; só "Kindly check this" ao Wallisson | Não |
| ~2026-07-28 | HRBS-12072 | Mais pay elements (duas combinações de flags) | SLA Exempt; resposta parcial de Mohit; falta confirmação do Wallisson | Não |
| ~2026-07-26 | HRBS-12101 | Samples dos relatórios SSC Form Ten, PAYE 5, ETX | Open, sem resposta (SLA estourado) | Não |
| ~2026-07-22 | HRBS-12111 | Revisão da Report Matrix da Namíbia | Open, só acknowledgement; SLA negativo | Não |

## Pendências
- [ ] HRBS-13602: base legal encontrada (2551 não é pré-imposto). Falta: revisar e enviar o rascunho em inglês (`rascunhos/2026-10-08-pesquisa-NA-SSC-PAYE.md`); conferir se o WTC de compliance marca 2551 como redutor da base (se sim, é erro nosso → [[correcoes]]) — Wallisson
- [ ] Identificar os tickets citados de "metodologia de anualização" e "constante de faixas desatualizada" — Compliance [INCERTO] (HRBS-13602)
- [ ] Decidir se 62100, 62146–62149, 62961 são pensionáveis — Wallisson (HRBS-12483)
- [ ] Confirmar se a combinação Tax=Yes / SSNC=Yes / Pension=No existe — Wallisson (HRBS-12072)
- [ ] Fornecer samples de SSC Form Ten, PAYE 5 e ETX — Compliance/Wallisson (HRBS-12101)
- [ ] Revisar a Report Matrix, principalmente os relatórios estatutários — Wallisson/Manju (HRBS-12111)
- [ ] Confirmar taxa e teto da SSC aplicados — Compliance (HRBS-14605). Fonte oficial já registrada em Valores-chave; falta só decidir a data do teto NAD 12.500 (2026-03-01 no Gazette × 2026-09-01 segundo fontes secundárias)
- [ ] Revisão de Compliance dos relatórios (após 25/09) e do payslip — Compliance (HRBS-14605)
- [ ] Decidir sobre VET Levy Return, IT12E e IT14E, que não existem — Mohit/Compliance (HRBS-14605)
- [ ] Fila sem resposta e com SLA negativo: HRBS-12072, 12101, 12110 (Congo, ver [[Congo]]), 12111, 12483 (e 14055, Congo) — Wallisson

## Correções ligadas
- _(nenhuma correção confirmada; a divergência sobre o WT 2551 entre cliente e CCG segue aberta, ver Pendências)_ — ver [[correcoes]]

## Fontes
- raw/tickets/extracao/2026-10-02-tickets-AF.md
- raw/chats/2026-10-01-mercans-compliance.md (menção de passagem)

# Reino Unido

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-unitedkingdom` · Fronteiras: [[fronteiras]]

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | 🔄 | 2026-06-18 | Artigo de KB "Directors' NI" em desenvolvimento no pipeline; Board de validação por IA UK com prazo 2026-11-23 (prioridade High), Not Started |
| [[design]] | 🔄 | 2026-05-27 | Country Data Dictionary GB v3.0 publicado (102 campos; 14 mappers), com defeitos listados |
| Produção (outro time) | — | | |
| [[suporte]] | ⏳ | | sem tickets nas fontes |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-unitedkingdom`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** GB, ano fiscal 2026-27 (2026-04-06 a 2027-04-05), setor privado, GBP. Três jurisdições de imposto (Inglaterra/NI, Escócia com 6 faixas, País de Gales); NIC é única. Fora: servidores públicos, forças armadas, polícia, marinheiros mercantes, pescadores, autônomos reais. Off-payroll dentro do IR35 está no escopo com conjunto de flags próprio.
- **Órgãos:** HMRC (imposto, NIC, student loans, CIS, RTI), The Pensions Regulator, Fair Work Agency e Acas, Scottish Government (taxas devolvidas).
- **Relatórios principais:** FPS e EPS (RTI, M2M), P60, P45, P11D/P11D(b), CIS300, Gender Pay Gap, relatório de employment intermediary (só prazos, sem layout).
- **Confiança da skill:** pesquisa do zero (2026-08-21); PASS WITH NOTES, 0 defeitos críticos, 6 itens abaixo de 95%: benefícios em espécie / grade de carro da empresa (82%), exemplo escocês (80%), relatório de employment intermediary (60%), e parciais (WTC 93%, DD 94%, payslip 90%). Códigos `GB-nnnn` do WTC são construção da Mercans. Nenhum estatuto citado literalmente (legislation.gov.uk bloqueado).

**Armadilhas confirmadas** (SKILL.md "Design clarifications")
1. AMAP é 55p, não 45p, retroativo a 2026-04-06; imposto: 55p nas primeiras 10.000 milhas e 25p depois; NIC: 55p em todas as milhas, sem redução → `01-ccg.md` §10.4; `02-wtc.md` GB-1410/1411 (engine)
2. SSP = menor entre 123,25 e 80% da média semanal, desde o dia 1 (ERA 2025, 2026-04-06); sem LEL e sem dias de espera; sem recuperação → `01-ccg.md` (engine)
3. PAYE, NIC e student loan têm bases diferentes: net pay arrangement reduz só PAYE; relief at source nenhum; salary sacrifice ambos; Payroll Giving só PAYE → `01-ccg.md` (engine)
4. Base do student loan = ganhos NICáveis secundários, arredondados para baixo; Plano 5 (`05`) é novo no FPS 2026-27 → `04-reports-spec.md` (engine)
5. ST do empregador £5.000/ano vs PT do empregado £12.570; relief Freeport/IZ limita em £25.000 (FUST/IZUST) → `01-ccg.md` (engine)
6. NIC por período para empregados, anual para diretores (FPS 84A `AN`/`AL`); nunca anualizar-e-dividir → `01-ccg.md` (engine)
7. Escócia: `SD0` = 21%, não 40%; faixa superior a £43.663 vs UEL £50.270 gera 42% + 8% = 50%; `S`/`C` em FPS item 55A → `01-ccg.md`; `04-reports-spec.md` (engine)
8. Salário tributável arredonda para baixo, limites de faixa para cima; free pay vem das Tables A (1257L mês 1 = £1.048,26) → `01-ccg.md` (engine)
9. Limite regulatório de 50% sobre a dedução PAYE, ignorado para K code com ativo facilmente conversível → `01-ccg.md` (engine)
10. Vouchers são Class 1, não 1A; payrolling de benefício só cobre o imposto, 1A segue anual em 2026-27 (payrolling obrigatório em 2027-04-06) → `01-ccg.md` (engine)
11. Class 1A em termination awards > £30.000 em tempo real no FPS (item 209); PENP com PAYE e Class 1 dos dois lados → `01-ccg.md` (engine)
12. EPS: grupo De Minimis State Aid removido em 2026-27 (erros 7940-7942, 7947-7950); namespaces `…/26-27/1` → `04-reports-spec.md`
13. RTI é M2M real (HTTPS POST GovTalk, submit-poll-delete, Level 1); DPS (P6/P9, SL1/SL2, PGL1/2) é consultado por polling → `03-sir.md`
14. ERA 2025 não cria unfair dismissal desde o dia 1: sobe a 6 meses em 2027-01-01 (cronograma DBIST de 2026-08-07) → `01-ccg.md`
15. Desde 2026-04-06 a agência (ou cliente final) responde pelo PAYE correto de trabalhadores de umbrella; NMW muda em 1 abr e o imposto em 6 abr → `01-ccg.md`

**O que mais dá errado** (do QA)
- Free pay: Tables A dá £1.048,26 e a fórmula fechada £1.048,25 (O-1); sequência de arredondamento do student loan (O-2); página GOV.UK contraditória sobre a taxa de SMP, £194,32 é o correto (O-3).
- Não achado: algoritmo PAYE fechado do HMRC; tabelas SL3 2026-27; layout do employment intermediary report; multiplicador £29.200 de fonte primária.
- Reverificar ao vivo: official rate of interest (3,75% desde 2026-04-06), advisory fuel rates (conjunto de 2026-06-01), taxas do HMRC e escocesas.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- Grade de percentuais de CO2 do carro da empresa (O-4): não declarar percentual; apontar para *480* Appendix 2. Fechar antes de produzir P11D.
- Layout do relatório de employment intermediary (O-8); XSDs do RIM 2027 não abertos (estrutura XML 70%) (O-7).
- Prefixos NINO não usados são DERIVED (O-9); texto do ERA 1996 não recuperado (O-10); exemplo escocês é ilustrativo (O-5).

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| AMAP | 55p (imposto: primeiras 10.000 milhas; NIC: todas) | 2026-04-06 | Taxation (Energy and Vehicles) Bill; ITEPA s.230(2) |
| SSP | menor de £123,25 ou 80% da média semanal | 2026-04-06 | Employment Rights Act 2025 |
| Secondary Threshold / Primary Threshold | £5.000 / £12.570 por ano | 2026-04-06 | HMRC (rates page) |
| UEL de NIC | £50.270 por ano | 2026-04-06 | HMRC (rates page) |
| Escócia, faixa superior | começa em £43.663 | 2026-04-06 | HMRC / gov.scot |
| LEL | £129/semana (£559/mês; £6.708/ano) | 2026-04-06 | `01-ccg.md` |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| Country Data Dictionary GB | 3.0 (arquivos v3 e "v31" idênticos) | 2026-05-27 | GB_Country_Data_Dictionary_v3/v31.xlsx | 102 campos (36 obrigatórios); 14 mappers; seções HR-friendly + colunas técnicas (Display Code `$entity.code`) |
| Directors' NI (artigo de KB) | — | 2026-06-18 | — | Desenvolvimento no pipeline |
| Skill `payroll-compliance-unitedkingdom` | n/a | n/a | skill Mercans | Existe |

## Valores-chave (com vigência)
> Valores do DD GB (chat: design-dev-kb); conteúdo estatutário completo: skill.

| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| Ano fiscal | 06/04/2026 a 05/04/2027 | 2026-04-06 | 2027-04-05 | GB DD v3 |
| LEL default | 542 | ⚠️ vigência? | | [INCERTO] vs GBP 125 semanal; ⚠️ sem fonte |
| Levy | 0,5% com allowance de 15.000 | 2026-04-06 | | skill `01-ccg.md` §5.8 (Apprenticeship Levy 0,5%, só se folha anual > £3m; allowance anual de £15.000) (GB DD v3) |
| Recovery | 1,03 / 0,92 | 2026-04-06 | | ⚠️ sem fonte (GB DD v3) |
| Auto-enrolment | EE 5% / ER 3% | 2026-04-06 | | skill `01-ccg.md` §8.2 (mínimos ER 3% / EE 5% sobre qualifying earnings; DWP, DEP2025-0866); defaults estavam invertidos no DD (ver Correções) |
| Tax code | 1257L | 2026-04-06 | | confirmado: skill `01-ccg.md` (códigos de emergência desde 2026-04-06: 1257L W1/M1/X); a nota "2025/26" no DD é a defasagem a corrigir |
| NI | letra H só <25; forçar C aos 66+; 17 letras NI | 2026-04-06 | | ⚠️ sem fonte (GB DD v3) |
| Student loan | planos 1/2/4 (+5) | 2026-04-06 | | skill `01-ccg.md` §5 (Planos 1, 2, 4 e 5; Plano 5 novo no FPS 2026-27) (GB DD v3) |

## Decisões
- 2026-05-27: layout do GB DD com seções HR-friendly + colunas técnicas (Display Code `$entity.code`); 102 campos (36 obrigatórios) (chat: design-dev-kb)

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| — | _(nenhum ticket GB nas fontes)_ | | | |

## Internal Certification (Análise de Reports)
> Frente 5: `frentes/certificacao/estado.md` · Método: [[analise-reports]] · Pasta: `internal-certification/United Kingdom`

| Pacote | Período | Pass / Finding / NT | Recibo | Situação |
|---|---|---|---|---|
| McDermott UK | set/26 | 50 / 4 / 17 | ACKs HMRC FPS/EPS recebidos 09/10 (IRmarks batem) | Validado |

- F-01: senha do Government Gateway em texto aberto nos arquivos do pacote (decisão do usuário sobre como tratar).
- Master recebido 09/10 tem 73 empregados × 69 no FPS/G2N: não conferido.
- 2º cliente (Christina Surpogi): opcional.

## Pendências
- [ ] Divergência hub × skill: Valores-chave registra LEL default 542 (e "vs GBP 125 semanal"); a skill traz LEL £129/semana (£559/mês, £6.708/ano) em 2026-27 — verificar (skill lida em 2026-10-02)
- [ ] Divergência hub × skill: Valores-chave diz "17 letras NI"; a skill descreve 16 category letters de NIC — verificar (skill lida em 2026-10-02)
- [ ] DD GB: LEL (542 vs GBP 125), Fuel Code (mapper A/D/F), campo "ID", "Maintained By", tax code 2026/27, v3 vs v31 — a definir — (chat: design-dev-kb)
- [ ] DD GB: Tax Basis default W1/M1 com exemplo Cumulative; mapper "Boolean" faltando; dropdowns prometidos no Cover e ausentes; campo "Password" — a corrigir — (chat: design-dev-kb)
- [ ] Desenvolver artigo Directors' NI no pipeline — Wallisson — (chat: design-dev-kb)

## Correções ligadas
- [[correcoes]]: DD GB com defaults de auto-enrolment invertidos (EE 3 / ER 5); correto EE 5% / ER 3% (demais itens a confirmar)

## Fontes
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- skill payroll-compliance-unitedkingdom (lida em 2026-10-02)

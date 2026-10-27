# Irlanda

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-ireland`

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2025 (base) | Base: CCG 2025, WTC v3.6, DD v3.4 (chat: design-dev-kb). Irlanda usada como baseline das sessões de gap-filling de acurácia (2026-06-30, Manju) (chat: compliance-research). |
| [[design]] | ✅ | 2026-06-24 | Regulation Design do Claude v1.0 (31 regs, 9372xxx) comparado ao da produção (CT-A-192, 52 regs): ~72%; 6 open items |
| Produção (outro time) | — | | Omnicom em Live/BAU |
| [[suporte]] | 🔄 | 2026-08-27 | HRBS-13860 (NAERSA falhando) em L2, sem envolvimento de Compliance no snapshot |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-ireland`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano fiscal 2026 (ano-calendário), setor privado, EUR, República da Irlanda (Irlanda do Norte = skill do Reino Unido). Fora: setor público (PRSI B/C/D/H), Class S/K, CE (A8/A9), SEO/ERO não enumerados, SARP/FED/shadow payroll, 2027+ não pesquisado.
- **Órgãos:** Revenue Commissioners; Dept. of Social Protection (PRSI, redundância); NAERSA (My Future Fund); Workplace Relations Commission.
- **Relatórios principais:** Payroll submission à Revenue (PAYE Modernisation, tempo real, assíncrono); ERR (s.897C); declaração/pagamento mensal (Variable Direct Debit); arquivo de contribuição e AEPN do NAERSA (portal, separado da Revenue).
- **Confiança da skill:** CCG 97%, WTC 95%, SIR Revenue 98%, reports Revenue/ERR 97%, DD 96%, payslip 96%. TIER-B/abaixo do piso de 95%: canal NAERSA (formato do arquivo/AEPN, ~70%, U3).

**Armadilhas confirmadas**
1. Cinco bases de pagamento (Gross, Pay for Income Tax, Pay for USC, Pay for EE PRSI, Pay for ER PRSI); pensão do empregado alivia só o imposto de renda (engine) → `01-ccg.md`, `02-wtc.md`, QA U8
2. PRSI muda em 1 out 2026, pela data de pagamento: EE 4,20%→4,35%; ER A1 11,25%→11,40%; faixa baixa 9,00%→9,15% (engine) → `01-ccg.md` §5.2
3. Limite da faixa baixa do ER é €552/semana (não €527/€441/€424); €424 é a divisa AX/AL e fim do PRSI Credit (engine) → `01-ccg.md`
4. My Future Fund: 1,5% do empregado sem nenhum alívio (IR, USC, PRSI); sai do líquido (engine) → `01-ccg.md` §6
5. Teto AE de €80.000 é acumulado no ano (só empregos não isentos), não €80.000÷12 (engine) → `01-ccg.md` §6
6. Elegibilidade AE: idade ≥23 e <60; quem decide é o NAERSA (AEPN), não o empregador (engine) → `01-ccg.md` §6
7. AE é declarado ao NAERSA, não à Revenue; duas remessas e dois pagamentos na mesma data (engine) → `03-sir.md`
8. NTFL de 1% já está dentro da taxa PRSI do empregador; não somar (engine) → `01-ccg.md`
9. Rescisão (redundância, ex-gratia, PILON) é PRSI Class M, nil; recibo final pode ter duas classes (engine) → `02-wtc.md`
10. Redundância estatutária não entra em nenhum campo de lump sum (itens 48/49) → `02-wtc.md` §8
11. USC reduzido: precipício em €60.000, vale o ano todo, 0,5% até €12.012 e 2% no resto; não existe status "REDUCED" (engine) → `01-ccg.md`
12. USC de emergência é 8% fixo sem cut-off; sem PPSN, IR 40% sobre tudo (engine) → `01-ccg.md`
13. Sem prêmio legal de hora extra nem de domingo (OWTA s.14, "razoável"); sem tabela de bônus (engine) → `02-wtc.md`
14. Sick leave legal = 5 dias (escalonamento p/ 7 e 10 abandonado); menor entre €110 e 70% → `01-ccg.md` §10–11
15. Payslip: exige só valor bruto e natureza/valor de cada dedução, itemizadas (inclui My Future Fund) → `06-payslip.md`
16. Revenue é M2M (HTTP Signatures rsa-sha512, digest, janela ±90 min, assíncrono; 200 ACKNOWLEDGED não = aceito); NAERSA é portal → `03-sir.md`

**O que mais dá errado** (do QA)
- Canal NAERSA (formato desconhecido, U3); depois a mudança de PRSI de 1 out 2026; depois o split de cinco bases.
- Fontes secundárias erradas: ER 9,15% até €441; A1 11,05% mantido em 2026; passos uniformes de 0,1pp; Small Benefit "dois vouchers" (são cinco, €1.500); Orçamento 2026 não mudou faixas/créditos (só a faixa USC 2%, para €28.700).

**Lacunas abertas / não confirmado**
- U3: formato do arquivo NAERSA e transporte do AEPN (~70%).
- U1: posição do My Future Fund na ordem de prioridade de deduções.
- U4: PRSA/PEPP do empregador acima do limite de 100%.
- U6: formato do PPSN (duas specs da Revenue divergem).
- U9: limite de subclasse ER para folhas não semanais (faixa de arredondamento).
- U5 (postura de enforcement do ERR 2026), U2 (suprimir licença por violência doméstica no payslip é guidance), U11 (referência "USC in week 53").

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| PRSI Class A empregado | 4,20% (4,35% desde 1 out 2026) | 2026-01-01 | SW 14 2026 |
| PRSI ER A1 / faixa baixa | 11,25% / 9,00% (11,40% / 9,15% desde 1 out 2026) | 2026-01-01 | SW 14 2026 |
| Limite faixa baixa ER | €552/semana (€1.104 quinzenal, €2.392 mensal) | 2026-01-01 | SW 14 2026 |
| USC faixas | 0,5% até €12.012; 2% até €28.700; 3% até €70.044 | 2026-01-01 | Revenue (USC thresholds) |
| My Future Fund | 1,5% empregado nos anos 1–3 (+0,5% Estado); teto €80.000 | 2026-01-01 | AE Act 2024 s.58(3), s.61 |
| Sick leave | 5 dias; menor de €110 ou 70% | 2024-01-01 | S.I. 10/2024 |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| CCG IE | 2025 (versão não citada) | — | — | Base do design |
| WTC IE | v3.6 | — | — | Base do design |
| DD IE | v3.4 | — | — | Sem campo para Advance Holiday Pay |
| Regulation Design IE (Claude) | v1.0 | — | IE_Regulation_Design_v1.0 | 31 regs, 9372xxx, 6 open items |
| Comparação Claude vs Dev (CT-A-192) | — | 2026-06-24 | IE_Design_Comparison_Claude_vs_DevTeam | ~72% (ponto médio entre lógica 84% e contagem 60%); produção tem 52 regs |
| Skill `payroll-compliance-ireland` | n/a | n/a | skill Mercans | Existe |
| Board de validação estatutária por IA | — | prazo 2027-02-08 (prioridade Low) | Monday | Not Started |

## Valores-chave (com vigência)
> Conteúdo estatutário completo: skill `payroll-compliance-ireland`. Abaixo, o que consta no design.

| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| PAYE / USC | taxas via RPN; PAYE 20/40% (emergência: 110 = 20/40; 120/130 = 40% fixo); USC 0,5/2/3/8% (8% acima de 42.662) | ⚠️ vigência? (2026) | | IE_Regulation_Design_v1.0 (Revenue, via RPN) |
| PRSI | EE 4,1%; subclasses AO ≤352 / AX / AL / A1 >527; crédito MAX(0; 12 − (sem − 352)/6); ER 8,9% / 11,15% / 0,6% | ⚠️ vigência? | | IE_Regulation_Design_v1.0 |
| Pensão / PHBS | pensão até 115.000 × % por idade (15–40%); PHBS 10% | ⚠️ vigência? | | IE_Regulation_Design_v1.0 |

## Decisões
- 2026-06-30: Chad e Ireland como baseline das sessões de gap-filling de acurácia — Manju (chat: compliance-research)
- 2026-07-02: decompor imposto progressivo em Threshold/Base/Amount era específico do RPN; usar uma reg `Differential` (Learning #2 corrigido) — Mohit/cross-training (chat: design-dev-kb)
- Padrão de design IE: taxas via RPN em 52/53xxx; triplet; regs Paid; reconciliação no ordinal 0 e no fim (chat: design-dev-kb)
- Fronteira: taxas PAYE/USC vêm da Revenue via RPN (fora do engine) (chat: design-dev-kb; ver [[fronteiras]])

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| 2026-08-27 | HRBS-13860 | Omnicom (Clavis Technologies Ltd e OMG): submissão NAERSA de agosto falhou; classes PRSI incorretas; processos 8211/8212 errored | Só acknowledgment e dados de processo (Romano Fusana, L2); sem Compliance; In Progress · **HRBS-13860 Resolved em 2026-10-05** (API, 27/10) | Não |
| 2026-06 | CT-A-192 | Comparação do design Claude vs dev | ~72%; 6 open items | Sim (aprendizados no design) |

## Internal Certification (Análise de Reports)
> Frente 5: `frentes/certificacao/estado.md` · Método: [[analise-reports]] · Pasta: `internal-certification/Ireland`

- Sem Primary SBC no board; definir com Manju/Marko (C-13). Report principal a confirmar: PSR + RPN.

## Pendências
- [ ] Classes PRSI em leavers (HRBS-13860): correção manual feita no employee card em 31/08 (Romano Fusana); a correção permanente do motor (leaver/closing herda a classe PRSI do último período ativo, em vez de J0/branco; 45 leavers A1 enviados como J0) não está confirmada no ticket (Resolved 05/10 sem comentário final) — verificar com L2/Dev; override 'PRSI Class Subclass' existe (oculto para Omnicom) _(reescrita em 27/10 a partir do HRBS-13860)_
- [ ] Advance Holiday Pay sem campo no DD v3.4 — a definir — (chat: design-dev-kb)
- [ ] `$hr.state_pension_contributory` na 58202 — a definir — (chat: design-dev-kb)
- [ ] Aplicar os learnings para chegar a 85–90% de acurácia no design — Wallisson — (chat: design-dev-kb)
- [x] Pontuação do design: tabela soma ~84% (lógica) e contagem ~60%; o ~72% é o ponto médio entre os dois (confirmado: chat design-dev-kb, tabela de correções, linha IE; revisão 2026-10-05)

- [ ] Divergência hub × skill: Valores-chave do hub (PRSI EE 4,1%; ER 8,9%/11,15%; subclasses com A1 >527; USC 8% acima de 42.662) não batem com a skill (EE 4,20%→4,35%; ER 11,25%→11,40% / 9,00%→9,15%; A1 >552; USC 3% até 70.044 e 8% acima) — verificar (skill lida em 2026-10-02)

## Correções ligadas
- [[correcoes]]: design IE do Claude (31 regs) sem triplet, regs Paid (9372611–661), Flag Reconciliation MTD (9372001), reconciliações 671/681, 3 bases de relevant earnings e 3 créditos; produção tem 52 regs
- [[correcoes]]: Learning #2 (decompor imposto progressivo em Threshold/Base/Amount) era específico do RPN; usar `Differential`

## Fontes
- raw/tickets/extracao/2026-10-02-tickets-AF.md (seção HRBS-13860)
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- raw/chats/2026-10-01-compliance-research.md
- skill payroll-compliance-ireland (lida em 2026-10-02)

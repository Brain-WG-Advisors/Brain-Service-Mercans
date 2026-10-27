---
tipo: pais
codigo: "CL"
etapa_research: "concluida"
etapa_research_data: "2026-05"
etapa_design: "em andamento"
etapa_design_data: "2026-06"
etapa_producao: 
etapa_suporte: "2 aberto(s): SR-221, SR-232"
etapa_suporte_data: 2026-10-27
ccg: "v1.1"
ccg_data: "2026-05"
wtc: "v1.0"
wtc_data: "2026-05"
dd: "v1.0"
dd_data: "2026-05"
report_specs: "CL-DT-001 sem versao; CL-PRV-001 sem versao"
report_specs_data: 2026-09-15
sir: 
sir_data: 
payslip: 
skill: "payroll-compliance-chile"
tickets_abertos: 2
tickets_conferidos_em: 2026-10-27
atualizado_em: 2026-10-27
---
# Chile

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-chile`

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | mai/2026 | CCG CL-CCG-001 v1.1, WTC CL-WTC-001 v1.0, DD CL-DD-001 v1.0; skill CL-SKILL-001 publicada com 7 discrepâncias de taxa em aberto |
| [[design]] | 🔄 | jun/2026 | Regulation Design v1.1 (9152xxx, 36 regs); Q1 e Q5 abertas |
| Produção (outro time) | — | | |
| [[suporte]] | 🔄 | 2026-09-28 | SR-221 e SR-232 (Report Specs) em Product Mapping com a BA; pedido de coluna de report code no WTC |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-chile`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano calendário 2026, só setor privado (não cobre público, militar/policial, autônomo filiado), moeda CLP.
- **Órgãos:** SII, DT (Dirección del Trabajo), Previred, Superintendencia de Pensiones, Superintendencia de Salud, SUSESO, Banco Central (UF); também AFP, FONASA/Isapre, AFC e Mutuales.
- **Relatórios principais:** LRE (Libro de Remuneraciones, DT, mensal), Previred Planilla Mensual (mensal), MPR (movimentos retroativos), F29 (mensal), DJ 1887 e DJ 1879 (anuais), Certificado Anual, LME (inbound de licença médica) e DS 67 (inbound de tasa adicional).
- **Confiança da skill:** não há CL-QA-REPORT canônico; o `07-qa-report.md` agrega o que existe. Handover v2.4 READY_FOR_HANDOVER (CCG 96/96 perguntas do template, payslip 5 abas, spec do payslip ~76 campos); scope lock-in PASS; WTC com 539 wage types. Sem % de TIER-B publicado.

**Armadilhas confirmadas** (o que o QA registra como correção)
1. Mapeadores de opção do DD desalinhados das Report Specs: 38 divergências corrigidas (DD v1.1 e specs v1.1) → `07-qa-report.md` (Alignment Patch, F1)
2. Códigos fora de escopo vazando (Isalud, Fundación, Gabriela Mistral, ISL como código de Mutual, Isapre de Codelco) → `07-qa-report.md` (F2)
3. Campos de Employer/Employee mal classificados em DJ 1887, DJ 1879, Certificado Anual e DS 67 → `07-qa-report.md` (F3)
4. "a todo evento" (Art. 164 CdT) é termo legal, não marcador "TODO" de pendência; falso positivo do audit C8 → `07-qa-report.md` (Handover v2.4)
5. Códigos de CCAF: legado `05 Gabriela Mistral` removido, 4 CCAFs em escopo → `07-qa-report.md` (Outstanding Items)

**O que mais dá errado** (do QA)
- Mapeamento DD ↔ wire format do Previred: o DD tem código canônico interno e `Movement Code (Tabla N°7)` separado; a camada de conversão precisa existir na integração.
- Valores que mudam (UTM, UF, IMM, comissão AFP) devem ser rechecados no feed oficial (SII, Banco Central, Previred) antes do uso.

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- Formato do MPR: spec cita `Guia MPR v3` da Previred, não revalidada; se sair v4, rever Movement Codes e Payer RUT.
- Tabla N°18 (CCAF): nova CCAF licenciada em 2026 exigiria atualizar DD e aba 6 do Previred.
- Tabla N°11 (instituições APV): DD e Previred têm só subconjunto (~14 de ~50); carregar a lista completa na integração outbound.
- C12 informativo: 3 de 16 palavras-chave do schema de colunas não batem em cada spec (variações de terminologia, não colunas faltando).

**Valores-âncora** (2026; fonte: `01-ccg.md`, conforme SKILL.md/QA; skill pede reverificar nos feeds)
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| UF / UTM (âncora jan/2026) | 39.706 / 69.265 | 2026-01 | `01-ccg.md` (Previred/SII) |
| Tetos imponíveis | 89,9 UF (AFP/Salud/Mutual); 135,1 UF (AFC) | 2026 | `01-ccg.md` |
| IUSC | isento até 13,5 UTM; topo 40% acima de 310 UTM/mês | 2026 | `01-ccg.md` (Art. 43 LIR) |
| Cap Gratificación Art. 50 | CLP 213.479/mês (4,75 × IMM 539.000 ÷ 12) | 2026 | `01-ccg.md` |
| Jornada | 42 h a partir de 2026-04-01; 40 h a partir de 2028-04-01 | 2026-04-01 | `01-ccg.md` (Ley 21.561) |
| F29 vencimento | dia 12 (papel) / dia 20 (eletrônico) | 2026 | `04-reports-spec.md` |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| CCG CL-CCG-001 | v1.1 | mai/2026 | — | Base do design (chat: design-dev-kb) |
| WTC CL-WTC-001 | v1.0 | mai/2026 | — | Pedido de nova coluna "report code" (SR-221/SR-232), pendente |
| DD CL-DD-001 | v1.0 | mai/2026 | — | |
| Report Spec CL-DT-001 (LRE) | sem versão | ~2026-05/06; link atualizado ~2026-09-15 | SR-221 | In Progress; Due 2026-07-31 (vencido). Versão anterior foi apagada (ver Correções) |
| Report Spec CL-PRV-001 (Previred Planilla Mensual) | sem versão | link atualizado ~2026-09-15 (Google Sheets) | SR-232 | Open; Due 2026-07-31 (vencido) |
| Regulation Design CL | v1.1 (vigente: maior versão) | jun/2026 | — | 36 regs, prefixo 9152; Q1 e Q5 abertas. Histórico: arquivo nomeado v1.0 |
| Design Decisions (respostas da Ruchi por GChat) | — | 2026-06-03 | KB_Chile_Design_Decisions | 5 bloqueios resolvidos |
| Skill CL-SKILL-001 | — | n/a | skill | Publicada; 7 discrepâncias de taxa em aberto (AFP Uno, Honorarios PPM, Ley 21.735) |

## Valores-chave (com vigência)
> Valores decididos/discutidos nos chats; conteúdo completo: skill `payroll-compliance-chile`.

| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| UF / UTM / IMM | 39.706 / 69.265 / 539.000 (IMM pode ter 2º degrau em jul/2026) | 2026-01 | | BC / SII / Ley 21.578 (chat: design-dev-kb) |
| Tetos | SS 89,9 UF; AFC 135,1 UF | 2026 | | skill `01-ccg.md` (cap mensal 89,9 UF AFP/Salud/SIS/Mutual/SANNA; 135,1 UF AFC; Indicadores Previsionales Previred jan/2026) (chat: design-dev-kb) |
| Comissões AFP | Uno 0,46; Modelo 0,58; PlanVital 1,16; Habitat 1,27; Cuprum/Capital 1,44; ProVida 1,45 | 2026 | | skill `01-ccg.md` (tabela de contribuições; mesmos valores); "AFP Uno" é uma das 7 discrepâncias em aberto (chat: mercans-compliance) |
| IUSC (UTM) | 0% até 13,5; 4%; 8%; 13,5%; 23%; 30,4%; 35%; 40% acima de 310 | 2026 | | Art. 43 LIR (chat: design-dev-kb) |
| Gratificación Art. 50 | MIN(25%; 4,75 IMM ÷ 12) ≈ 213.479/mês | 2026 | | LIR/CdT (chat: design-dev-kb) |
| Jornada | 44 h → 42 h em 2026-04-01 → 40 h em 2028 | 2026-04-01 | | Ley 21.561 (chat: design-dev-kb) |
| Previred / F29 / LRE | Previred dia 10/13; F29 dia 12/20; LRE dia 15 | 2026 | | skill `01-ccg.md` (Módulo de obrigações: Previred 10 papel/13 eletrônico; F29 12 papel/20 eletrônico; LRE 15; vence no dia útil seguinte, Art. 50 Código Tributário) (chat: design-dev-kb) |

## Decisões
- 2026-06-03: Comissão AFP em 1 regulação com 7 bands, assertion por código de AFP, sem 52xxx e sem 58212 — uma AFP por empregado — Ruchi Gupta (chat: design-dev-kb)
- 2026-06-03: Reliquidação Art. 46 manual em steps (sem suporte nativo do engine); vale para qualquer bônus multi-mês — Ruchi (chat: design-dev-kb)
- 2026-06-03: UF/UTM/IMM digitados todo mês em HR field da legal entity (`$legal_entity_hr.uf_eom/utm/imm`), sem integração — Ruchi (chat: design-dev-kb)
- 2026-06-03: `gratificacion_method` na legal entity (1 = Art. 50, 2 = Art. 47), dois caminhos por assertion — escolha do empregador — Ruchi (chat: design-dev-kb)
- 2026-06-03: APV-B: SS sobre o bruto; APV-B + contribuições EE em intermediária 58xxx que reduz só o IUSC — padrão existente — Ruchi (chat: design-dev-kb)
- jun/2026: IUSC em 3 passos (BTM→UTM 58121; lookup 58122/58123; posting 2552), sem `differential`; excesso ISAPRE em 1 reg com 2 bands (9152081); Art. 47 com 1 step YTM — orientação do dev — Ruchi (chat: design-dev-kb)
- 2026-07-10: Retro: SS parcial, tax 100% (falta testar) — Ruchi + Mohit (chat: design-dev-kb)
- 2026-09-28: BA pede coluna no WTC CL com o report code aplicável a cada WT — Ruchi Gupta (SR-221, SR-232)
- Fronteira de design: UF/UTM/IMM (publicados por BC/SII), DS67 (por empregador), Art. 55 bis (certificado do banco), asignación (via Previred), crédito de zona (Form 1902 SII) ficam fora do engine (chat: design-dev-kb; ver [[fronteiras]])

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| 2026-09-28 | SR-221 | Spec LRE (CL-DT-001); BA pediu coluna de report code no WTC | Link atualizado ~2026-09-15; coluna pendente; In Progress | Pendente (WTC) |
| 2026-09-28 | SR-232 | Spec Previred (CL-PRV-001); mesmo pedido de coluna | Link atualizado ~2026-09-15; Open | Pendente (WTC) |
| 2026-06-03 | GChat Q1–Q5 | AFP, Art. 46, UF, Art. 50/47, APV-B | Resolvidos (ver Decisões) | Sim (design CL) |
| jun/2026 | Design Q2/Q3/Q4 | YTM da reliquidação; faixas IUSC; excesso ISAPRE | Resolvidas | Sim (v1.1) |

## Pendências
- [ ] Adicionar coluna "report code" ao WTC CL — Wallisson — (SR-221, SR-232)
- [ ] Concluir revisão dos campos amarelos da spec LRE — Wallisson/Ruchi — (SR-221) [INCERTO se concluída]
- [ ] Specs SR-221/SR-232 com Due Date vencido (2026-07-31) — Wallisson — (SR-221, SR-232)
- [ ] Resolver as 7 discrepâncias de taxa na skill (AFP Uno, Honorarios PPM, Ley 21.735) — Wallisson — (chat: mercans-compliance)
- [ ] Q1: ordinal da gratificación (15 ou 281) e Q5: asignación usa 58101 ou 58100 — Mohit/Ruchi — (chat: design-dev-kb)
- [ ] 9152011: 3 sub-regs ou 1 com 3 bands?; Previred v82 entra no escopo v1?; fórmula da 9152321 é só conceito e conta da 9152311 indefinida — a definir — (chat: design-dev-kb)
- [ ] Testar o retro (SS parcial / tax 100%) e atualizar KB_Chile_Design_Decisions — Ruchi/Mohit — (chat: design-dev-kb)
- [ ] [INCERTO] Parte 2 do design ainda lista 8 regs de IUSC; assertion 9152301 com `MULTIPLY(1.439668;1000)` (escala?); 58212 listada mas "não necessária" (chat: design-dev-kb)

## Correções ligadas
- [[correcoes]]: não apagar versão anterior de artefato em que a BA já trabalhou; versionar (SR-221)
- [[correcoes]]: design com dependência circular na gratificación (ordinal 15 vs 281) — linearizar (chat: design-dev-kb)
- [[correcoes]]: design com IUSC em 8 regs por faixa e reliquidação com 12 acumuladores — corrigido para 3 passos e 1 step YTM (v1.0 para v1.1)

## Fontes
- raw/tickets/extracao/2026-10-02-tickets-OUT.md
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- raw/chats/2026-10-01-mercans-compliance.md
- skill payroll-compliance-chile (lida em 2026-10-02)

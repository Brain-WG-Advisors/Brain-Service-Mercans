# República do Congo (Congo-Brazzaville, CG)

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-congo`
> Atenção: não confundir com a RD Congo (skill `payroll-compliance-drcongo`).

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ | 2026-06-30 | Pesquisa concluída (Wallisson); skill file entregue e atualizado (chat: compliance-research; mercans-compliance) |
| [[design]] | 🔄 | 2026-08-28 | Regulation Design clean-room comparado com CT-A-590: 77%, cobertura funcional 26/26; perguntas Q1–Q11 ao Mohit abertas (chat: design-dev-kb) |
| Produção (outro time) | — | | |
| [[suporte]] | 🔄 | 2026-09-02 | Baker Hughes Congo: 12110, 12472, 13841, 14054, 14055 (vários sem resposta) |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-congo`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** FY2026, setor privado sob o Code du Travail (residentes e expatriados), moeda XAF (inteiros, sem subunidade). Fora: autônomos, servidores públicos, quem recebe só jetons de présence.
- **Órgãos:** DGID (ITS, TUS, NIU; e-Taxe), CNSS (PVID/PF/AT-MP, CAMU; e-déclaration), Inspection du Travail.
- **Relatórios principais:** CG-CNSS-001 bordereau mensal; CG-DGID-001 declaração mensal ITS+TUS; CG-DAS-001 declaração anual de salários (DAS), arquivo separado, não derivado dos 12 mensais.
- **Confiança da skill:** QA de 2026-06-25, nota 92/100, veredito NEEDS PATCHES (1 MAJOR + 3 MINOR); alinhamento CCG/WTC/DD/Report Specs ≈100%. Alíquotas, tetos, barème, quociente, forfaits AEN e split do TUS CONFIRMADOS na lei (LF 2026). DERIVADOS (precisam de RA): códigos de campo, posições de arquivo, máscara do NIU, template de upload, modelo da DAS3 e prazo da DAS (31/mar; minoria cita 31/jan). Acurácia estimada das specs: CNSS ≈80%, DGID ≈82%, DAS ≈70%.

**Armadilhas confirmadas** (esclarecimentos de julho/2026 com Compliance; prevalecem sobre o resto da skill)
1. CAMU solidariedade 0,5% incide sobre o bruto acima de 500.000 XAF (não sobre a base líquida do ITS) → SKILL.md, esclarecimento 1
2. A solidariedade é do empregado, retida pelo empregador e repassada à DGID; separada da CAMU principal (ER 4,55% + EE 2,27%) que passa pela CNSS → esclarecimento 2
3. TUS: 7,5% único, só empregador, todos os setores; remessa dividida 5,475% CNSS + 2,025% DGID (obrigatório desde 2026-01-01) → esclarecimento 3
4. Abonos especiais forfaitários: isentos de ITS só até 15% do bruto total; excesso volta à base do ITS e do TUS; a isenção não vale para CNSS/CAMU → esclarecimento 4
5. Arredondamento: truncar para o milhar de baixo só na base líquida do ITS (art. 116); todo o resto, inclusive o ITS final retido, arredonda ao XAF mais próximo → esclarecimento 5
6. +1 parte da criança adulta com deficiência é cumulativa; teto de 6,5 partes continua → esclarecimento 6
7. Viúvo(a) sem filho em 2 anos após o óbito = casado sem filho (2 partes), não soma com o ÷1,5; teto 2 partes → esclarecimento 7
8. Payslip, aba Unit Rate Details: 16 de 22 códigos de ganho colidem com tipos de salário da WTC (ex.: Housing em 62300 = Annual leave) → `07-qa-report.md` MAJOR-1

**O que mais dá errado** (do QA)
- Mapeamento de GL do payslip errado (MAJOR-1) gera lançamentos contábeis trocados; a exibição EN/FR não é afetada
- Rótulos "(EUR)" restantes nas abas master/setup do payslip; linha-modelo sobrando no Version Control da WTC; "Employee Full Name" não está no DD do país (é campo global)

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- Layouts exatos das 3 declarações (ficam atrás do login e-déclaration CNSS e e-Taxe/SYSTAF); códigos e posições são derivados
- Prazo da DAS: 31/mar × 31/jan
- Taxas do décret da CAMU ainda pendentes de OCR literal (flag da skill)
- Modelo ministerial da DAS3

**Valores-âncora**
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| SMIG | 70.400 XAF/mês | 2026 | Décret n°2024-2762 |
| PVID | ER 8% / EE 4%, teto 1.200.000 | 2026 | Loi 31-2011; Décret 99-284 |
| PF / AT-MP (ER) | 10,03% / 2,25%, teto 600.000 | 2026 | Loi 31-2011; Décret 99-284 |
| CAMU | ER 4,55% / EE 2,27% + 0,5% acima de 500.000 (solidariedade) | 2026 | Décret n°2024-133 |
| TUS | 7,5% ER (5,475% CNSS + 2,025% DGID) | 2026-01-01 | LF 2026 (loi n°42-2025) |
| ITS (barème) | 1.200 FCFA / 10% / 15% / 20% / 30% (30% a partir de 5.000.001 por parte); abatimento 20% após PVID EE 4%; teto 6,5 partes | 2026 | loi n°42-2025 arts. 114-116 |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| Skill `payroll-compliance-congo` | [INCERTO] | — | skill | "Entregue e atualizado" (chat: mercans-compliance) |
| Artefatos de pesquisa (CCG, WTC, report specs) | sem versão citada | 2026-06-30 | Monday | Pesquisa concluída; versões [INCERTO] (chat: compliance-research) |
| Regulation Design CG (clean-room) | — | 2026-08-28 | FR-pack | 77% vs CT-A-590; inclui dimensão de executabilidade na pontuação (chat: design-dev-kb) |
| Report Matrix (cliente) | — | ~2026-07-21 | anexo do HRBS-12110 | Em revisão, sem resposta |

## Valores-chave (com vigência)
| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| CAMU, contribuição empregador | 4,55% | FY2026 (skill; data de início não informada) | — | CAMU Congo (camu-congo.fr), citado por Wallisson (HRBS-13841); Décret n°2024-133 de 2024-03-27 (confirmado: skill, SKILL.md esclarecimento 2 e item 3 das regras; taxas do décret ainda sem OCR literal, flag da skill) |
| CAMU, contribuição empregado | 2,27% | FY2026 (skill; data de início não informada) | — | CAMU Congo (camu-congo.fr) (HRBS-13841); Décret n°2024-133 (confirmado: skill) |
| CAMU combinado | 6,82% (4,55% + 2,27%) | FY2026 (skill; data de início não informada) | — | CAMU Congo (camu-congo.fr) (HRBS-13841); Décret n°2024-133 (soma conferida com a skill) |
| Contribution de solidarité nationale (CAMU solidarité) | 0,5% sobre a fração do salário acima de 500.000 XAF/mês; do empregado, retida e repassada à DGID | FY2026 (skill; data de início não informada) | — | CAMU Congo (camu-congo.fr) (HRBS-13841); confirmado: skill, SKILL.md esclarecimentos 1 e 2 (julho/2026), Décret 2024-131 para o reversement |
| Limiar de solidariedade na regulação do design | 500.000 (valor em fórmula, não é dividido); a versão anualizada 6.000.000 estava errada | 2026-08-28 | — | FR-pack (chat: design-dev-kb) |
| TUS | 7,5% do Taxable Total (só empregador; remessa 5,475% CNSS + 2,025% DGID) | 2026-01-01 (split obrigatório; FY2026) | — | LF 2026 (loi n°42-2025) (confirmado: skill, SKILL.md esclarecimento 3); declarado pelo solicitante no HRBS-14054 |
| Car allowance líquido garantido (política do cliente) | 500.000 / 625.000 / 750.000 por grade (moeda [INCERTO], provavelmente XAF) | — | — | política do cliente (HRBS-14054) |
| TOL (taxe d'occupation des locaux à usage d'habitation), assalariados | 1.000 FCFA/mês retidos na fonte pelo empregador, como adiantamento do imposto anual; regularização pelo empregado até 20/04 (casados no mesmo imóvel, centro-ville, etc.). Tarifa anual habitação: centro-ville 60.000 / periferia 12.000 FCFA | 2015-01-01 (LF 2015) | — | Loi 34-2013 (LF 2014) art. 14, redação da Loi 48-2014 (LF 2015) art. 8: JO éd. spéc. n°1-2015 p. 17; tarifa: Loi 34-2013 art. 13 a), JO éd. spéc. n°5-2013 p. 22. PDFs em raw/docs/oficiais/CG/. Nenhuma LF 2016–2026 encontrada altera o valor (LF 2020, 2021 e 2023 não verificadas) |

## Decisões
- 2026-08-27: o item "CAMU Health Insurance (Employee)" do cliente (~0,5% dos ganhos regulares) é a CAMU solidarité (0,5% acima de 500.000 XAF), não a CAMU empregado 2,27%; são dois fluxos distintos segundo a autoridade CAMU — Wallisson (HRBS-13841)
- 2026-08-28: no design CG, usar `$period_divisor`, `simple_tax_monthly`, wildcards (65%%%, 794%%, 6286/7/8%) e 58204 = "No Child" (0,5 parte), que falta no CCG CG — design CG (chat: design-dev-kb)
- ~2026-08-10: payslip do Congo: confirmação dos campos estado civil, nº de filhos e nº de partes atribuída ao Wallisson (sem resposta) — Manju Shetija (HRBS-12472)

## Suporte (tickets)
| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| ~2026-09-02 | HRBS-14054 | TUS subestimado: car allowance sem gross-up no G2N do cliente; pergunta se o gross-up entra na base do TUS | Open, sem resposta nossa (erro é do G2N do cliente, segundo o autor) | Não |
| 2026-09-02 | HRBS-14055 | Occupancy tax e Region tax são regulatórios? | Open, sem resposta no snapshot | Não |
| ~2026-08-31 | HRBS-13841 | CAMU não consta na WTC de compliance | Wallisson (27/08): item do cliente = CAMU solidarité 0,5% acima de 500.000; follow-up (31/08) sobre os 4,55%/2,27% sem resposta; Pending on reporter | Não [INCERTO se a solidarité entra na WTC] |
| ~2026-08-10 | HRBS-12472 | Payslips Congo e Gabão: estado civil, nº de filhos, nº de partes | Gabão respondido (ver [[Gabao]]); Congo atribuído ao Wallisson, sem resposta | Não |
| ~2026-07-21 | HRBS-12110 | Revisão da Report Matrix do Congo (Baker Hughes) | Open, só repasse ao Wallisson; SLA negativo | Não |

## Pendências
- [ ] Responder se 4,55%/2,27% da CAMU são estatutários e por que o cliente não os aplica (o G2N do HRB tem) — Wallisson (HRBS-13841)
- [ ] Decidir se a CAMU solidarité 0,5% entra na WTC de compliance — Compliance [INCERTO] (HRBS-13841)
- [ ] Responder se o gross-up do car allowance entra na base do TUS — Wallisson (HRBS-14054)
- [ ] Responder se occupancy tax e Region tax são regulatórios — Wallisson (HRBS-14055)
- [ ] Revisar a Report Matrix e dizer se pode ir ao cliente — Wallisson (HRBS-12110)
- [ ] Confirmar campos do payslip do Congo (estado civil, nº de filhos, nº de partes) — Wallisson (HRBS-12472)
- [ ] Roteamento da solidarité: DGID × Décret 2024-131 — Compliance (chat: mercans-compliance)
- [ ] Design CG: perguntas Q1–Q11 ao Mohit (atomização, mapper, `_period` × cauda, nº de matrizes, Tax Group, `_$$`, bandas 2,4/9,6, registro 58xxx, `.99`, FLOOR, rubrica) — Wallisson → Mohit; incluir o relief "No Child" no CCG CG — RA (chat: design-dev-kb)
- [ ] Atualizar Congo no Monday — Wallisson (chat: compliance-research)
- [ ] Taxa regional/départementale: o CGI consolidado do finances.gouv.cg (edição ~2002–2003) traz no art. 327 b o précompte do empregador no salário de janeiro; a LF 2015 trocou "taxe régionale" por "taxe départementale ou communale" no art. 250 e a LF 2017 tirou a taxe régionale do art. 407. Nenhuma lei encontrada revoga ou mantém os arts. 321–327. Os "2.000 FCFA anuais pagos pelo contribuinte" do comentário de 09/10 (HRBS-14055) não têm fonte primária (só PwC: departmental tax XAF 2.000). Falta: CGI 2025/2026 consolidado da DGID; lista TPPE da DGID (citada em 09/10, não localizada). (2026-10-13)

## Consolidado da sessão 2026-10-13
- **Fontes primárias conferidas** (PDFs em `raw/docs/oficiais/CG/`): CAMU 4,55% ER / 2,27% EE (Décret 2024-133, art. 2); CAMU paga **direto à CAMU** em até 5 dias após o fim do mês, com declaração nominativa 10 dias antes do vencimento (Décret 2024-131, arts. 15–16); TUS 7,5% a cargo do empregador (loi 8-2012, art. 6), dividida 73% CNSS / 27% Estado a partir de 2026 (LF 2026, loi 42-2025, art. 47, p. 23); DAS (DAS1/2/3) "dans le courant du mois de janvier" (CGI art. 176), DAS3 pela LF 2026 art. 116 I e Arrêté 1560 de 10/07/2026; solidarité 0,5% acima de 500.000 XAF (LFR 2021, loi 37-2021, art. 42); língua oficial francês (Constituição 2015, art. 4). Erros da skill registrados em [[correcoes]].
- **HRBS-12110** (Report Matrix): nada a responder em 13/10 — a pergunta original foi respondida em 13/08 e não há pedido novo a nós. Revisão completa da matriz em `rascunhos/2026-10-09-HRBS-12110-revisao-matriz-Congo.md`. Em 20/10 (14:25 UTC), depois do "still need" do Daniel (07/10), perguntamos o que ele precisa (matriz nova, um dos 5 pontos de 13/08 ou outro tema); aguardando resposta.

## Correções ligadas
- [[correcoes]]: design CG (clean-room) com limiar de solidariedade anualizado 6.000.000, divisor fixo 12, `_monthly` ausente, wildcards faltando, 58204 como flag bilateral; corrigido conforme FR-pack (2026-08-28).
- Nota sobre HRBS-13841: a comparação do cliente com a CAMU 2,27% era imprecisa (o item é a CAMU solidarité); não é erro nosso.

## Fontes
- raw/tickets/extracao/2026-10-02-tickets-AF.md
- raw/tickets/extracao/2026-10-02-tickets-OUT.md (seção HRBS-14054)
- raw/chats/2026-10-01-compliance-research.md
- raw/chats/2026-10-01-mercans-compliance.md
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- skill payroll-compliance-congo (lida em 2026-10-02)

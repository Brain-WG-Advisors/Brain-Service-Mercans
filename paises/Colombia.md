# Colômbia

> Hub do país. Índice: [[00-INDEX]] · Skill: `payroll-compliance-colombia`

## Situação
| Etapa | Status | Data | Observação |
|---|---|---|---|
| [[research-pipeline]] | ✅ (concluída) | 2026-10-26 | PMI: pesquisa encerrada em 26/10. No Drive (com links no Monday e na CT-4593): 7 specs v1.0 (17 - Statutory Report), CCG v1.4, WTC v1.6, DD v1.3, SIR v1.1. Delta ao design e e-mail de encerramento (thread "PMI Review") enviados pelo Wallisson em 26/10. Ficam com terceiros, sem bloquear: saúde/FSP nas mesadas adicionais e fatos da PILA-007 (cliente/BAU), consulta à DIAN sobre código do pensionado e dias fracionados (decisão da Manju). Kit e trackers: `Research Pipeline/Colombia/co-report-crosscheck/04-output/PENDING-2026-10-21.md`; confirmação: `CONFIRMACAO-PROCESSOS-CO-2026-10-26.xlsx`. Histórico: pesquisa CO "na fila depois da Bélgica" (chat: mercans-compliance); Mohit: CO exige "redesign ou ao menos grande correção de gaps" (~2026-08-29). |
| [[design]] | ⏳ | 2026-10-22 | PMI: início do design do time do Mohit estimado em 20/11 (e-mail de 22/10, sem confirmação). Antes: Colômbia citada como país sugerido para o próximo design (chat: design-dev-kb). |
| Produção (outro time) | — | | PMI em produção/BAU; transição para Instaroll em curso (outro time) |
| [[suporte]] | 🔄 | ~2026-09-03 | 5 tickets PMI sem resposta nossa no snapshot de 2026-09-16 |

## Ficha do país (da skill)
> Resumo do que mais importa para o serviço. Fonte: skill `payroll-compliance-colombia`, lida em 2026-10-02. Valores exatos e tabelas: ler a skill. Se divergir, vale a skill.

- **Escopo:** ano fiscal 2026, empregados do setor privado (CST), COP. Fora: servidores públicos, militares/polícia, independentes e contratistas.
- **Órgãos:** DIAN (retención, nómina electrónica, exógena), UGPP, MinTrabajo, MinSalud (PILA); EPS/AFP/fondos de cesantías, ARL e CCF.
- **Relatórios principais:** nómina electrónica (CO-RPT-001, SOAP/M2M, por período), Formulario 350 (retención, mensal), PILA (mensal, por operador privado), Formulario 220, Formato 2276 v4 (exógena, anual), depósito de cesantías (CO-RPT-006) e relatório MinTrabajo (CO-RPT-007).
- **Confiança da skill:** pesquisa de 2026-08-27, build do zero; veredito READY WITH DOCUMENTED GAPS; 15 itens abertos (1 fechado). Maioria das seções 92-97%; abaixo do piso de 95%: PILA 55%, Form. 350 60%, aprendizes 45%, reforma de pensão 70%, cesantías/MinTrabajo 25-30%. Listas de códigos de instituições (EPS/AFP/ARL/CCF) e bancos: 0%, não obtidas.

**Armadilhas confirmadas** (correções da skill)
1. SMMLV $1.750.905 vale pelo Decreto 0159 de 19-02-2026 (transitório), não pelo 1469/2025 (suspenso pelo Consejo de Estado) (engine) → `01-ccg.md`
2. Divisor da hora ordinária: 220 até 14-07-2026 e 210 desde 15-07-2026; 240 é obsoleto; folha de julho cobre os dois (engine) → `01-ccg.md` §5
3. Dominical/festivo sobe de 80% para 90% em 2026-07-01; semana de 42 h/divisor 210 só em 07-15; não juntar (engine) → `01-ccg.md` §5
4. Janela noturna começa às 19:00, não 21:00, desde 2025-12-25 (engine) → `01-ccg.md`
5. Exoneração ET art. 114-1: estritamente MENOS de 10 SMMLV; em $17.509.050 perde; CCF 4% e pensão 12% nunca exonerados (engine) → `01-ccg.md`
6. Três bases, três tetos: IBC (1 a 25 SMMLV = $43.772.625), base parafiscal (sem teto) e base de retención; não reusar (engine) → `01-ccg.md`
7. Pacto não salarial: limite de 40% (Ley 1393 art. 30) só para seguridade social; excesso volta ao IBC (engine) → `01-ccg.md`
8. Renta exenta de 25% calculada por último, depois do limite combinado 40%/1.340 UVT; 72 UVT/dependente fica fora do limite (engine) → `01-ccg.md`
9. FSP é linha própria do empregado (1% desde 4 SMMLV + subcuenta 0,2-1,0% desde 16 SMMLV), não parte dos 4% de pensão (engine) → `01-ccg.md`
10. Três regimes de arredondamento no mesmo mês (PILA, XML da nómina, formulários DIAN); isolar resíduo em `Redondeo` (engine) → `01-ccg.md` §11
11. Vacaciones não são prestação social; entram no IBC e na base parafiscal; salario integral não absorve vacaciones (engine) → `01-ccg.md`
12. Enum de horas extras do Anexo Técnico DIAN (§5.5.5) está desatualizado (dominical 100/75/150/110) e é obrigatório: conflito não resolvido (engine) → `07-qa-report.md` Q-3
13. Reforma de pensão (Ley 2381/2024) não vale em 2026 (Auto 841/2025 suspendeu); não fixar a data de 2027-04-01, só imprensa → `07-qa-report.md` Q-24
14. Não há artigo do CST sobre conteúdo do payslip; vale Res. DIAN 000013/2021 arts. 5 e 24 (13 itens; QR ≥ 2 cm se emitir) → `06-payslip.md`
15. ARL Classe IV máximo é 6,060% (6,960% é o valor inicial da Classe V) → `07-qa-report.md` D-1

**O que mais dá errado** (do QA)
- Quatro defeitos em documentos oficiais: ARL IV (D-1), exemplo de CUNE do Anexo Técnico não reproduz (D-2), data impossível no exemplo de QR (D-3), enum de horas extras desatualizado (D-4). Não usar os exemplos do Anexo como teste de conformidade.
- Riscos vivos de cálculo: divisor 210 (Q-19, ~88%, doutrina administrativa lida em espelho) e enum DIAN (Q-3).

**Lacunas abertas / não confirmado** (candidatos a ticket ou nova pesquisa)
- Não dá para gerar arquivo PILA (Q-10) nem declaração Formulario 350 (Q-23); aprendizes (Q-5, 45%) e `AltoRiesgoPension` (Q-14) não configuráveis.
- Q-2: apropriação mensal dos tetos anuais de 790 e 1.340 UVT é DERIVADA (÷ 12, ~75%).
- Q-4: sem código de documento para PPT; Q-6 e Q-7: tarifa dos 2 primeiros dias de incapacidade e piso mínimo; Q-8: aportes em licença não remunerada.
- Q-11 (Formato 2276 encoding, 70%) e Q-12 (relatório MinTrabajo, 25%); códigos de EPS/AFP/ARL/CCF e bancos não obtidos.
- Q-21: auxilio de transporte na base de prestaciones é prática consolidada, não lei (~90%).

**Valores-âncora** (2026; fonte: SKILL.md e `01-ccg.md`)
| Item | Valor | A partir de | Fonte |
|---|---|---|---|
| SMMLV | $1.750.905 (transitório) | 2026 | Decreto 0159 de 2026-02-19 |
| UVT | $52.374 | 2026-01-01 | Res. DIAN 000238 de 2025 |
| Auxilio de transporte | $249.095 (até 2 SMMLV) | 2026 | Decreto 1470 de 2025 |
| Saúde / pensão | 12,5% (4/8,5) / 16% (4/12); IBC 1 a 25 SMMLV | 2026 | Ley 100 arts. 18, 20, 204; Ley 797/2003; Ley 1122/2007 |
| Parafiscales | CCF 4%, SENA 2%, ICBF 3% | 2026 | Ley 21/1982; Ley 89/1988 |
| Dominical/festivo | 80% até 2026-06-30; 90% desde 2026-07-01 | 2026-07-01 | CST art. 179 par. trans.; Ley 2466 art. 14 |

## Artefatos entregues
| Artefato | Versão | Data | Arquivo/local | Observação |
|---|---|---|---|---|
| Skill `payroll-compliance-colombia` | n/a | n/a | skill Mercans | Existe (uso como consulta) |
| WTC CO | sem versão citada | — | — | WTs citados nos tickets: 63123, 62837, 52552, 21125, 64993, 2552–2556, 21330, 22110, 22112. Redesign/gap fixing pendente. |
| CO-WTC-001 | **v1.5** (vigente de 2026-10-21 a 2026-10-25) | 2026-10-21 | Google Sheet `03 - WTC\CO-WTC-001-v1` (importado com Replace em 22/10; o xlsx v1.5, md5 383e37317708a99b0a2f6806b013c19f, foi removido da pasta); cópia local em `Research Pipeline/Colombia/2026-10-21-alinhamento-WTC/` | Base: export do Google Sheet de 21/10. As edições de 19–20/10 sem linha no Version Control são da Heidy (BAU), pelo histórico de versões do Sheet (22/10); a v1.5 as manteve. Res. 13/2021 → 227/2025 em 112 células; verificador PASS |
| CO-CCG-001 | **v1.3** (vigente de 2026-10-21 a 2026-10-25) | 2026-10-21 | Google Doc novo `05 - Payroll Regulation Guide\CO-CCG-001_v1.3` (convertido do docx md5 abd9e2595675df3ea8e96cca4d21e4cb em 22/10; docx removido); o Doc v1.2 foi para `05 - Payroll Regulation Guide\Archived`; Monday aponta para o Doc v1.3 | 87 sugestões pendentes da v1.2 decididas com fonte primária (2 rejeitadas → Pendências, HRBS-12487); Res. 13 → 227; saúde dos pensionados 4/10/12%; piso C-543 no exemplo de licença médica; férias fora do IBC de saúde, pensão e ARL; verificador em 3 rodadas → PASS |
| CO-DD-001 | **v1.2** (vigente de 2026-10-21 a 2026-10-25) | 2026-10-21 | Google Sheet `02- DD\CO-DD-001-v1` (importado com Replace em 22/10; xlsx md5 db3b8dc6ff95fd2b1cd86b1afabb8f3c removido) | Origem da data de desligamento (registro "Termination"); Res. 13 → 227; "placeholder" → "substitute value"; verificador PASS |
| Report Specs (7): CO-DIAN-001, -002, -004, -005, CO-PILA-003, CO-CESANTIAS-006 e **CO-PILA-007 (nova)** | 1.0 (Version Control de linha única, padrão do kit) | 2026-10-22 | Google Sheets em `17 - Statutory Report` (só os `.gsheet`; os xlsx foram importados com Replace e removidos); finais locais em `co-report-crosscheck/05-final/` | Rodada 5, fases 2A–2D de 21/10. CO-PILA-007 = PILA dos pensionados pagos pelo empregador (Res. 2388/2016, Anexo Técnico 3 v15). 22/10: CO-DIAN-001 M183 (saúde do subtipo 01 e dos pensionados) com a regra correta — ver [[correcoes]] 2026-10-22 |
| CO-CCG-001 | **v1.4** (vigente a partir de 2026-10-26) | 2026-10-26 | Google Doc novo `05 - Payroll Regulation Guide\CO-CCG-001_v1.4` (convertido do docx md5 8b087e4d… em 26/10; docx removido); Doc v1.3 em `Archived`; Monday aponta para o Doc v1.4; local `Research Pipeline/Colombia/2026-10-22-auditoria-lote1/` | Módulo 5, novidades PILA VAC/LR e IGE (22/10); 26/10: denominador dos 40% pela UGPP ABC Empleadores 2025 (S23) — [[correcoes]] 2026-10-22 e 2026-10-26 |
| CO-WTC-001 | **v1.6** (vigente a partir de 2026-10-26) | 2026-10-26 | Google Sheet novo `03 - WTC\CO-WTC-001_v1.6` (xlsx md5 05b839bb… removido); Sheet `CO-WTC-001-v1` (v1.5) em `03 - WTC\Archived`; Monday atualizado; local na mesma pasta | Férias em dinheiro fora de saúde/FSP/ARL/pensão (156, 324); sem o adiantamento mensal de cesantías; 26/10: denominador dos 40% (V1, F395), base do IBC com a regra das férias (F390), linha 317 = Non-Salary - pacted |
| CO-DD-001 | **v1.3** (vigente a partir de 2026-10-26) | 2026-10-26 | Google Sheet novo `02- DD\CO-DD-001_v1.3` (xlsx md5 f5a14676… removido); Sheet `CO-DD-001-v1` (v1.2) em `02- DD\Archived`; Monday atualizado | Tipos de planilha PILA, aprendizes, sem o adiantamento mensal; 26/10: W37 com a fonte do denominador dos 40% |
| Report Specs (7) — lotes 1 e 2 da auditoria + 40% (26/10) | 1.0 (linha única) | 2026-10-26 | finais locais em `co-report-crosscheck/05-final/`. No Drive (26/10, Replace, conferidos aba a aba): as 7. Em CO-DIAN-001 e CO-CESANTIAS-006 a coluna M de mapeamento do Ram Sakthi (design) foi reinserida e os valores dele devolvidos aos mesmos campos (PENDING #61; valores das linhas MA removidas guardados em `04-output/ram-sakthi-colM/`) | Lote 1: tipos de planilha PILA e aprendizes; 2276 M32/M33. Lote 2: 229 edições. 26/10: 40% só sobre não salariais pactados (CO-DIAN-001 M89/M161; CO-PILA-003 A25/C25/M108/C19) |
| CO-WTC-001 (histórico) | **v1.4** (vigente até 2026-10-20). Histórico da linhagem do Drive: v1.0 em 24/09; v1.2 draft em 05/10 (Non-Salary, Ley 1393); v1.3 em 05/10 (FSP) | 2026-10-13 | `~/mercans-pipeline/CO-compliance/02-wtc/CO-WTC-001-v1.4.xlsx`, montada sobre a export v1.3 (Downloads, 06/10). ⚠️ Cópia para `G:\...\Colombia\03 - WTC\CO-WTC-001_v1.4.xlsx` pendente (bloqueada pela permissão) | Follow-up da revisão Cinthya/Manju: tributação das incapacidades e licenças; ARL = No na incapacidade e nas férias; dias 1–2 fora da base das prestações; linha nova para incapacidade acima de 180 dias; eleitor/jurado; retención contingente. Azul `FFDDEBF7`. Nessa linhagem a coluna D (explicação) é vazia, então as bases legais foram para a coluna Z. ⚠️ O `.gsheet` foi editado em 13/10 16:49, depois da export v1.3: comparar com uma export nova |
| CO-CCG-001 (histórico) | **v1.2** (vigente até 2026-10-20; v1.1 de 06/10 = histórico) | 2026-10-13 | `~/mercans-pipeline/CO-compliance/01-ccg/CO-CCG-001-v1.2.docx`, montada sobre a v1.1 do Drive (Downloads, 06/10), com controle de alterações (autor "Claude", 13/10). ⚠️ Cópia para o Drive pendente | Mesmas correções (m04, m05, m08). Mantém as alterações pendentes de 05/10 (FSP; "0.6667" → "2/3"). ⚠️ O `.gdoc` foi editado em 13/10 13:32: comparar. Os `modules/*.md` do pipeline estão defasados: não regerar a partir deles |
| scope_manifest CO | 1.0 + `CO-OUT-RETCONT` + nota de correção | 2026-10-13 | `CO-compliance/scope_manifest.json` | A taxa a partir do dia 541 foi resolvida (valor reconhecido pela EPS), sem gap aberto |
| SIR landscape CO | + `CO-OUT-RETCONT` (fluxo não-autoridade) | 2026-10-13 | `CO-compliance/03-statutory-integrations/integration-landscape.json` | |
| Versões descartadas | WTC "v1.2" e CCG "v1.2" montadas sobre a v1.1 do pipeline | 2026-10-13 | scratchpad da sessão (`superseded-pipeline-lineage/`) | Base errada (não era a export mais recente do Drive). Não usar |
| Board de validação estatutária por IA | — | prazo 2026-12-21 (prioridade Medium) | Monday | Status "Not Started" (chat: design-dev-kb) |

## Valores-chave (com vigência)
> Os valores dos tickets foram **declarados pelo solicitante (PMI)**, não validados por nós. Conteúdo estatutário geral: ver a skill.

| Item | Valor | A partir de | Até | Fonte |
|---|---|---|---|---|
| Taxa máxima ARL Classe IV | 6,060% | ⚠️ vigência? ("vigente") | | normograma.mintic.gov.co (chat: mercans-compliance) |
| UVT | COP 52.374 | 2026-01-01 (ano fiscal 2026) | | DIAN Resolução 000238 de 15/12/2025 (HRBS-13627, citada pelo solicitante) |
| SMMLV | COP 1.750.905 | 2026 | | skill (Decreto 0159 de 2026-02-19, transitório; Decreto 1469/2025 suspenso) (declarado em HRBS-12491) |
| Limite vacation bonus para SS + retenção | 95 UVT | 2026 (offcycle sem. 31/2026) | | ⚠️ sem fonte (HRBS-12487) |
| Fórmula do bônus de férias | ROUND(Total Días × 2,8 × salário base mensal / 30; 0); Total Días = Days Taken + Cash Out | ⚠️ vigência? | | regra do cliente/sistema, ⚠️ sem fonte legal (HRBS-12487) |
| Embargo (garnishment) | 1/5 do excedente sobre o SMMLV, após deduzir 2552/2553/2554/2556; base ≤ SMMLV = 0 | ⚠️ vigência? | | ⚠️ sem fonte legal (HRBS-12491) |
| Pagamentos não salariais | máx. 40% da remuneração total; excesso entra no IBC | ⚠️ vigência? | | Lei 1393/2010 (citada, HRBS-12492) |
| IBC mín./máx. | 1 SMLMV / 25 SMLMV | 2026 | | skill (Ley 100 de 1993 arts. 18/20/204; Ley 797 de 2003; Ley 1122 de 2007; IBC 1 a 25 SMMLV) (HRBS-12492, citado pelo solicitante) |
| Saúde | 12,5% (EE 4% / ER 8,5%); ER exonerado até 10 SMLMV | 2026 | | skill (Ley 100 arts. 18/20/204; Ley 1122/2007; exoneração: ET art. 114-1; ver Pendências, divergência 1) (HRBS-12492) |
| Saúde do pensionado pago pelo empregador | sobre a mesada: 4% (1 SMLMV), 10% (>1 até 3 SMLMV), 12% (>3 SMLMV) | 2024-01-01 | | Ley 100 art. 204 par. 5 (inciso da Ley 2294/2023 art. 78); Res. MinSalud 1271/2023 art. 1; base = mesada: Decreto 780/2016 art. 2.2.1.1.2.1 (conferido 2026-10-22, verificador) |
| Saúde do pensionado que trabalha (NE subtipo 01) | 4% do empregado sobre o salário; só a contribuição de pensão é 0 | 2026 | | Ley 100 arts. 157, 204 (Ley 1122/2007 art. 10); Decreto 780/2016 art. 2.2.1.1.2.1 e parágrafo; pensão: Ley 100 art. 17 (Ley 797/2003 art. 4) (conferido 2026-10-22) |
| Pensão | 16% (EE 4% / ER 12%) | 2026 | | skill (Ley 100 de 1993; Ley 797 de 2003) (HRBS-12492) |
| Parafiscales | Caja 4%, ICBF 3%, SENA 2% (ICBF/SENA exonerados até 10 SMLMV) | 2026 | | skill (Ley 21 de 1982; Ley 89 de 1988; exoneração: ET art. 114-1; ver Pendências, divergência 1) (HRBS-12492) |
| IBC nas férias | salário do mês anterior ao início das férias | ⚠️ vigência? | | Art. 3 Decreto 1072/2015 e guias PILA (citados, HRBS-12492) |
| Isenções/deduções de retención | auxílio alimentação 41 UVT/mês (Art. 387-1); juros moradia 100 UVT; medicina pré-paga 16 UVT; dependentes máx. 32 UVT; AFC+VFP 30% (Art. 126-1); renda isenta 25% = 790 UVT/ano (Art. 206-10); limite global 40% / 1.340 UVT/ano (Art. 388) | 2026 | | E.T., citados pelo solicitante (HRBS-13627) |
| Tabela Art. 383 | 0–95 UVT 0%; até 150 19%; até 360 28%; até 640 33%; até 945 35%; até 2.300 37%; acima 39% | 2026 | | Art. 383 E.T. (HRBS-13627) |
| Expat / não residente | 20% sobre total tributável (configuração do cliente) | ⚠️ vigência? | | ⚠️ sem fonte legal (HRBS-13627) |
| Cesantías / intereses | 1 mês por ano; juros 12% a.a. (cesantías × 12% × dias/360); base variável conforme Art. 253 CST | ⚠️ vigência? | | Art. 253 CST (citado); resto ⚠️ sem fonte (HRBS-13692) |

## Decisões
- ~2026-08-29: Colômbia "requires a redesign or at least a major gap fixing work" — Mohit Jain, Head of Compliance Product (HRBS-12487..13692)
- ~2026-09-03: os 5 tickets PMI de transição Instaroll vão para a gap analysis da pesquisa CO, atribuídos ao Wallisson — Mohit Jain, após conversa com Manju (HRBS-12487..13692)
- 2026-10-15: escopo dos relatórios = só os estatutários (imposto de renda: 350, 220, 2276; seguridade: PILA, cesantías; Nómina Electrónica); relatórios operacionais do cliente fora — checkpoint call 15/10
- 2026-10-21: spec nova CO-PILA-007 (PILA dos pensionados pagos pelo empregador, AT3 v15) e pensionados pagos pelo empregador no escopo da NE — Wallisson (fase 2D)
- 2026-10-22 (checkpoint call): todos os relatórios estatutários no escopo, incluindo o acrescentado (PILA-007); relatórios não estatutários numa aba separada do plano (Andy); teste paralelo numa **entidade nova e limpa**, não réplica da PMI (Marko); meta de conclusão em meados de dezembro; Wallisson alinha a data com o Mohit (Gemini notes 22/10)
- 2026-10-22: e-mail ao Mohit só com datas (sem falar de documentos, a pedido do gestor): pesquisa até o fim de outubro, início estimado do time dele em 20/11 — Wallisson
- 2026-10-22: decisões do PENDING (recomendações aceitas): manter o layout das specs (#30); saúde dos pensionados só no CCG, sem linha nova no WTC, avisar a Config (#36); código da NE para pensionados fica aberto, consulta à DIAN é decisão da Manju (#41); linha 12 do plano (relatórios de bônus e juros) fechada: regras legais cobertas nos artefatos, relatórios são operacionais (fora do escopo de 15/10) — Wallisson

## Suporte (tickets)
Contexto comum: lista "PMI Instaroll Transition Tracker" (ELT); cliente PMI (Compañía Colombiana de Tabaco SAS, REF-LE-00-505). Nenhuma resposta nossa em nenhum dos cinco (snapshot 2026-09-16).

| Data | Ticket | Assunto | Resolução | Mudou artefato? |
|---|---|---|---|---|
| ~2026-09-03 | HRBS-12487 | Automação do vacation bonus offcycle acima de 95 UVT (WTs 63123/62837/52552) | Sem resposta nossa; Pending on reporter; gap analysis | Não |
| ~2026-09-03 | HRBS-12491 | Explicação do cálculo de embargo (itens 21125, 64993) | Sem resposta; Romano perguntou nº de embargos por período, sem retorno | Não |
| ~2026-09-03 | HRBS-12492 | Regras de contribuição de SS (40% Lei 1393, exonerações, IBC nas férias) | Sem resposta; Pending on reporter | Não |
| ~2026-09-03 | HRBS-13627 | Explicação do cálculo de retención en la fuente (2552, 21330) | Sem resposta; Open, resolução estourada (−20d) | Não |
| ~2026-09-03 | HRBS-13692 | Provisões de cesantías e intereses (22110, 22112) + relatório de consolidação | Sem resposta; Open, resolução estourada (−19d) | Não (novo report sem spec) |

## Pendências
- [x] **Fechamento PMI** — concluído 2026-10-26: Drive/Monday (7 specs, WTC v1.6, DD v1.3, CCG v1.4); delta ao design (com a regra da trava dos 40%) e e-mail de encerramento enviados pelo Wallisson; registros postados no chat "Research Pipeline II"; YouTrack CT-4593 (links) e SR-470 (rótulo SIR v1.1) pedidos à janela Suporte com ok do usuário (PENDING #16, #59) — Compliance (2026-10-26)
- [ ] Depois do fechamento: datas do design na timeline do Andy quando o Mohit confirmar; skill `payroll-compliance-colombia` instalar/atualizar (#17) — Wallisson (2026-10-26)
- [ ] Com terceiros (não bloqueia): cliente/BAU — saúde/FSP nas mesadas adicionais (#55) e fatos da PILA-007 (#54); Manju — consulta à DIAN (#41, #51); design — dúvidas nas colunas T/U das specs (suporte) (2026-10-26)
- [ ] Sem fonte oficial (registrados no PENDING do kit): código TipoTrabajador/SubTipo da NE para pensionado pago pelo empregador (#41; prática do provedor: 01/01, mesada como OtroConcepto); saúde e FSP sobre as mesadas adicionais de junho/dezembro (#55; parâmetro a confirmar com o cliente); arredondamento de dias fracionados na NE (#51) — Compliance (2026-10-23). Fechados em 23/10: #33 (nenhuma spec afirma), #38 (cláusula LMA retirada da PILA M110)
- [x] Decisões #56/#57 (flags do WTC; denominador dos 40%) — decididas pelas fontes e aplicadas em 26/10 (UGPP ABC Empleadores 2025 p. 5; CE SU 25185/2021 regra 3; Decreto 780 art. 3.2.5.1; CST art. 128) — Compliance (2026-10-26)
- [ ] Achados da NE de setembro, só registro (sem mudança de spec): férias na rescisão como OtroConcepto "Vacaciones Definitivas"; WT 62151 como OtroConcepto; aprendizes coerentes com a spec; 37 empregados com Sueldo 0,00; nenhum arquivo semanal (todos PeriodoNomina 5) — vão no delta (2026-10-23)
- [x] **Revisão cruzada das Report Specs contra os relatórios do cliente (PMI), rodada 5** — concluída 2026-10-21/22 (fases 2A–2D; fase 3 = revisão dos 871 arquivos da NE, 22/10; ver `PENDING-2026-10-21.md`). Texto original: (design fecha em 2026-10-31): kit em `Research Pipeline/Colombia/co-report-crosscheck/`, estado em `HANDOFF-2026-10-21.md` (seções 5 e 6). Antes de mudar qualquer spec: WT 21330 é "Theoretical" no mapa do cliente (`Conceptos cir 2025.xlsx`, fora da casilla 60 do 220), mas foi tratado como retenção real na rodada 3, que fechou setembro em 1.618,3 milhões; perguntar à BAU. Pedir acesso à pasta "September 2026 Payroll Validation Files" da Heidy. Registrar cada etapa no chat claude.ai "Research Pipeline II" — Wallisson / frente Pipeline (2026-10-21)
- [ ] Gap analysis dos 5 tickets PMI dentro da pesquisa CO — Wallisson — (HRBS-12487, 12491, 12492, 13627, 13692)
- [ ] HRBS-12487 (bônus de férias, WT 62837/62838): duas sugestões do CCG v1.2 (S86/S87, de 18/09) avaliavam a spec de automação do cliente. Elas saíram do CCG v1.3 porque classificam verbas do cliente. O texto delas, palavra por palavra, está em `Research Pipeline/Colombia/2026-10-21-alinhamento-CCG/REJECTED-S86-S87.md`: a spec do cliente aplica faixas de 8%/9%/10% direto sobre o bônus, e isso não corresponde a nenhuma contribuição real — Compliance (2026-10-21)
- [ ] Acumulado anual do limite de 1.340 UVT: o validador do cliente aplica 1.340 ÷ 12 por mês, risco de sub-retenção — Wallisson/Compliance — (HRBS-13627)
- [ ] Confirmar se o sistema calcula o IBC de férias sobre o bruto do mês (observação do Support, 4 dias de férias) — Compliance/Dev — (HRBS-12492) [INCERTO]
- [ ] Spec de report de consolidação de cesantías (inexistente) — Compliance/Reports — (HRBS-13692)
- [ ] Validar os valores declarados pelo cliente contra fonte oficial/skill antes de usar como confirmados — Wallisson — (todos)
- [ ] Pesquisa CO "na fila depois da Bélgica" no pipeline — Wallisson — (chat: mercans-compliance)
- [ ] Divergência hub × skill: Valores-chave diz "ER exonerado até 10 SMLMV" (saúde, SENA, ICBF); a skill diz estritamente MENOS de 10 SMMLV (ET art. 114-1; em $17.509.050 perde a exoneração) — verificar (skill lida em 2026-10-02)
- [ ] Divergência hub × skill: Valores-chave lista dependentes "máx. 32 UVT" (declarado pelo PMI); a skill traz também 72 UVT/dependente (ET art. 336 num. 3, máx. 4, fora do limite 40%/1.340 UVT) além do art. 387 (10%, máx. 32 UVT/mês) — verificar (skill lida em 2026-10-02)
- [ ] Divergência hub × skill: Pendência sobre 1.340 UVT ÷ 12 do validador do cliente como risco de sub-retenção; a skill adota ÷ 12 como convenção do engine, mas DERIVADA (~75%, Q-2), sem regra mensal no DUR 1625 — verificar (skill lida em 2026-10-02)
- [ ] Divergência hub × skill: IBC das férias "salário do mês anterior" (HRBS-12492) e fórmula do embargo (HRBS-12491), bônus de férias 95 UVT (HRBS-12487) e cesantías base variável não aparecem na skill (SKILL.md/QA; embargo só como "inembargable" no CCG) — verificar (skill lida em 2026-10-02)
- [ ] Divergência hub × skill: Situação mostra Research 🔄 "na fila"; a skill traz pesquisa CO concluída em 2026-08-27 (READY WITH DOCUMENTED GAPS) — verificar (skill lida em 2026-10-02)

- [x] Taxa a partir do dia 541: nenhuma norma fixa o valor; a EPS liquida e paga ao empregador (Decreto 780 art. 2.2.3.4.3), então a folha usa o valor reconhecido (2026-10-13)
- [x] Base das prestações: dias 1–2 fora da base; os dias contam e o valor sai da média (CSJ SL1659-2025 p. 28). ⚠️ A p. 26 da mesma sentença é ambígua (2026-10-13)
- [x] ARL: não incide na incapacidade (novedad 1.2) nem nas férias gozadas (1.3) (Decreto 1072/2015 art. 2.2.4.2.1.6). Corrigido no WTC v1.4. Licenças remuneradas e maternidade não estão no artigo e não foram alteradas (2026-10-13)
- [x] Parafiscales dos dias 1–2 (empregador): fora da base (Ley 21/1982 art. 17). Corrigido no WTC v1.4 e na CCG v1.2 (2026-10-13)
- [x] Licença para cuidado da criança: no WTC v1.4 e na CCG v1.2 (Decreto 780 arts. 2.2.3.2.11–12; Res. MSPS 467/2025, PILA IGE "L", sem ARL). Salud/pensión = Yes: a licença é reportada como novidade IGE, e o IBC da IGE segue o Decreto 780 art. 3.2.1.10 (Res. 467/2025) (2026-10-13)
- [ ] CO-GAP-15: linha WTC da licença por perda gestacional (CST 237; Decreto 780 art. 2.2.3.2.15). Falta a novidade PILA e a regra de contribuição em fonte MinSalud — Wallisson
- [x] G1 pensionados: escopo. Resumo em [[2026-10-13-CO-G1-pensionados-brief]] — resolvido 2026-10-21/22: pensionados pagos pelo empregador na NE e na PILA-007 (AT3); BAU 22/10: sem pensões compartilhadas com a Colpensiones e sem CCF para pensionados
- [x] Comparação com as exports atuais do Drive (13/10 às 23h08 e 23h10): o `CO-WTC-001-v1.gsheet` e o `CO-CCG-001-v1.gdoc` são iguais às bases usadas (WTC v1.3 e CCG v1.1), mas **sem a correção do FSP de 05/10**, que nunca chegou ao Drive. A v1.4 e a v1.2 não desfazem nenhuma edição e trazem o FSP. A CCG no Drive não tem comentários da Cinthya, só um nosso de 05/10. Existe também um `CO-CCG-001-v1.0.gdoc` antigo (24/09) na mesma pasta: arquivar
- [x] WTC v1.4 e CCG v1.2 copiados para o Drive em 13/10 às 23h16 (`03 - WTC/CO-WTC-001_v1.4.xlsx`, `05 - Payroll Regulation Guide/CO-CCG-001_v1.2.docx`). Superado em 22/10: WTC v1.5 importado no Sheet e CCG v1.3 como Google Doc novo
- [x] Enviar a resposta na conversa (rascunho [[2026-10-13-CO-email-Manju-Cinthya]]) — enviada em 14/10 (thread "Review Completed")
- [x] Achados da Cinthya na CCG e no SIR: SIR — Res. 13/2021 compilada na Res. 227/2025 (e-mail de 14/10), aplicado no SIR v1.1; CCG — as sugestões pendentes foram resolvidas na v1.3 (2026-10-21)
- [ ] Levar à skill `payroll-compliance-colombia` a tributação das incapacidades (DIAN 27408), a ARL (Decreto 1072 art. 2.2.4.2.1.6) e a retención contingente

## Correções ligadas
- [[correcoes]] 2026-10-13: incapacidades e licenças de maternidade/paternidade estavam como renda isenta "within the statutory minimum" (ET 206 nums. 1–2); são tributáveis (DIAN Oficio 27408/2019 itens 7.1–7.4). Corrigido no WTC v1.4 e na CCG v1.2.
- [[correcoes]]: taxa máxima ARL Classe IV estava errada em batch anterior; correto 6,060% (normograma.mintic.gov.co) (chat: mercans-compliance)
- [[correcoes]] 2026-10-22: CO-DIAN-001 M183 dizia saúde 0,00 para o pensionado que trabalha (subtipo 01); o correto é 4% sobre o salário (só a pensão é 0), e para o pensionado pago pelo empregador a faixa 4/10/12% sobre a mesada. Achado nos 871 arquivos da NE de setembro; corrigido e no Drive em 22/10.

## Fontes
- raw/tickets/extracao/2026-10-02-tickets-OUT.md
- raw/chats/2026-10-01-mercans-compliance.md
- raw/chats/2026-10-01-mercans-design-dev-kb.md
- skill payroll-compliance-colombia (lida em 2026-10-02)

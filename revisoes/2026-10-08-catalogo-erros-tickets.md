# Catálogo de erros e soluções dos tickets: 2026-10-08

> Índice: [[00-INDEX]] · Correções: [[correcoes]] · Pipeline: `~/mercans-pipeline/shared/country_failure_log.md` (F1–F47, v2.11)
> Consolida os 6 arquivos de análise `raw/tickets/extracao/2026-10-08-erros-solucoes-{UA-A,UA-B,ES-A,ES-B,AF,OUT}.md` (detalhe por ticket: linha do tempo, erro, causa raiz, solução, o que ficou aberto).
> **Nada foi aplicado no pipeline.** As seções 4 e 5 são propostas e precisam de aprovação.

## 1. Escopo e limitações
- **60 tickets distintos** (125 snapshots, 04/08 a 08/10/2026): UA 18, ES 16, África 14 (+ KB CT-A-620), Colômbia 5, Chile 2, China, Holanda, Irlanda, Lituânia, Singapura.
- Fonte: PDFs exportados à mão. **A API do YouTrack não está conectada nesta cópia** (o `.env` não veio no clone do GitHub). Faltam os tickets de jan–jul/2026 e as respostas depois do último snapshot de cada ticket. Quando o token voltar: `scripts/youtrack_fetch.ps1` e completar este catálogo.
- Planilhas, imagens e anexos dos tickets não entram no texto: o que mudou célula a célula não consta.
- Inferências dos agentes estão marcadas `[INCERTO]` nos arquivos de grupo.

## 2. Números

**Situação no último snapshot:** 1 resolvido (HRBS-12181), 26 parciais, 32 não resolvidos, 1 n.a. (KB).

**Tipos de erro** (um ticket pode ter vários):

| Código | Tipo | Tickets |
|---|---|---|
| T11 | Pedido de informação / sample / explicação | 33 |
| T12 | Fonte ou base legal ausente/contraditória | 27 |
| T8 | Versão / sincronização entre artefatos | 24 |
| T6 | Escopo (dentro/fora indevidamente) | 23 |
| T5 | Spec de relatório (layout, formato, população) | 21 |
| T7 | Fórmula / método de cálculo | 21 |
| T3 | Código ou rótulo de WT errado/faltando | 18 |
| T4 | Campo do DD faltando/errado | 18 |
| T10 | Divergência cliente × artefato (sem erro nosso) | 18 |
| T1 | Valor estatutário errado/desatualizado | 13 |
| T2 | Tratamento tributário/contributivo do WT | 11 |
| T9 | Payslip | 5 |

**Padrões do pipeline que já existiam e deixaram o erro passar** (citações nos 60 tickets): F45 (16), F43 (15), F41 (11), F6 (9), F5 (8), F27 (8), F1/F4/F7/F20 (7 cada), F40/F42/F46 (6 cada).

## 3. Leitura: o que os tickets dizem do pipeline
1. **O pipeline protege o build, não o pós-entrega.** F45 (consistência entre artefatos) e F27 (re-sync após correção) são os mais citados porque **a correção feita via ticket não passa pelo pipeline**: corrige-se o WTC na mão e as specs, o DD e o CCG ficam para trás (SR-342, SR-85, SR-415, UA 4DF, HRBS-10563).
2. **F41 (oráculo independente) não chega às specs de arquivo.** Todos os erros de posição/tag/formato (M190, M111, M296, CERTIFICA, D1/4DF/D5/D6, BASES) apareceram só na rejeição do portal ou no QC manual da BA. O teste do Dev contra a nossa própria spec é circular.
3. **F43 (populações especiais) não cobre ciclos de pagamento.** Off-cycle, advance payroll, licença que atravessa meses, ordem de runs e acumuladores YTD (CO, SG, UA, ES) caíram fora.
4. **Tributação de WT sem base legal por flag.** UA (seguro de vida, presentes, civil contractor, 128), Namíbia (pensão), Congo (CAMU/solidarité): decisão por analogia. F7/F20 checam código, não a fundamentação.
5. **Nossas próprias respostas viraram fonte de erro.** Sick leave 6 × 12 meses (UA), "65816 now has the formula" sem fórmula, código 157 contraditório, 79432 = B.01 e 65815 contestados com cópia antiga do WTC, mesma amostra AFI usada para inbound e outbound.
6. **Processo de suporte** (não é falha do pipeline, vai para [[suporte]]): 32 tickets sem resolução, SLA estourado em boa parte; HRBS-14331 fechado com 4+ perguntas abertas; duplicado HRBS-14714 × 14996; HRBS-14675 passou por 5 pessoas.

## 4. Propostas para o `country_failure_log.md`

### 4.1 Reforço de padrões existentes
| F | Por que escapou | Reforço proposto |
|---|---|---|
| F27 / F45 | Só roda no build; correção via ticket não dispara re-sync | Toda correção de ticket que muda WTC/DD/CCG abre uma rodada de propagação (C29/C45) no país afetado antes de responder "done" |
| F41 | Oráculo só para research numérico | Estender para specs: diff contra leiaute/XSD oficial e amostra real (ver F48, F55) |
| F43 | Lista de populações, não de ciclos | Acrescentar eixo "ciclos": off-cycle, advance, retroativo, licença entre meses, ordem de runs (ver F58) |
| F7 / F20 | Checam se o código existe, não a base | Coluna de base legal por flag (ver F50) |
| F6 | Pendências ficam no artefato e no ticket | Ticket não pode ir para Resolved com pergunta aberta; TBC/[VERIFY] bloqueia entrega (C29 já pega marcadores, estender a "TBC", "Check WTC", "[VERIFY WITH RA]") |

### 4.2 Padrões novos (F48–F59)
| Novo | Título | Tickets de origem | Check proposto |
|---|---|---|---|
| F48 | Spec de arquivo oficial sem diff contra leiaute/XSD | SR-79, 82, 83, 85, 160–163, 432, CERTIFICA (13757) | C48: toda tag/posição do XSD ou Diseño Lógico tem linha na spec; limites, padding, enums e zeros obrigatórios conferidos |
| F49 | Código de WT renomeado/retirado sem varredura | SR-82, 85, 342, 83, 415; HRBS-10563 (79416) | C49: todo código de WT citado em spec/DD/CCG existe no WTC vigente com o mesmo rótulo |
| F50 | Flag tributário/contributivo do WT sem base legal (decidido por analogia) | HRBS-12181, 14331, 12483, 12072, 13602, 13841 | C50: coluna "base legal" por flag no WTC; combinações de flags documentadas por país |
| F51 | Limite anual/acumulador sem definição (anual ÷12, YTD calculado × pago, 12× em pisos) | HRBS-13627, 15630, 14996, CT-A-620 | C51: todo limite declara período, acumulador, status (calculado/pago) e teste por banda |
| F52 | Resposta de ticket não consolidada no artefato (sem fonte única de verdade) | UA sick leave 6×12, 65816, 157; SR-85 (cópia antiga do WTC) | Regra: resposta cita versão vigente do artefato; fato novo de ticket entra no CCG/WTC antes de responder |
| F53 | Mesmo nome para arquivos oficiais diferentes / direção inbound×outbound | SR-80, 432, HRBS-12839, CT-4321 | C53: título da spec = nome oficial + direção; tabela única arquivo × direção × spec × amostra |
| F54 | Lista de relatórios cobertos/não cobertos não publicada nem reconciliada com o cliente | HRBS-12101, 12110, 12111, 14605, 15253, 14675 | Scaffolder emite matriz de cobertura (S/C/M/N) por país; relatório sem dono = fora de escopo explícito |
| F55 | Aceite sem amostra real (e testes com exercício em curso) | SR-83, 144, 160–163 (true XML sample), 13757 | C55: aceite exige comparação com amostra real A3/portal e exercício fechado |
| F56 | Campo exigido por spec/WTC inexistente no DD | SR-414, HRBS-13389, 15216, `accrual_period_year` (SR-83/342) | C56: todo campo-fonte de spec existe no DD (rastreabilidade spec → DD) |
| F57 | Payslip sem campos legais / template divergente da Payslip Spec | SR-340, HRBS-12472, 13757, SR-316 | C57: checklist de campos legais do payslip por país; template × Payslip Spec 1 |
| F58 | Ciclos especiais não cobertos (off-cycle, advance, licença entre meses, ordem de runs) | HRBS-12487, 14255, 15630, 10563 | Eixo de ciclos no F43 / coverage matrix |
| F59 | Rótulo de versão/changelog não bate com o arquivo; versão apagada em vez de versionada | UA (4 ocorrências), SR-221 | C59: nome do arquivo, Version Control e conteúdo citam a mesma versão; versão revisada nunca é apagada |

## 5. Erros nossos confirmados ou prováveis, ainda abertos (agir)
| # | País | Ticket | Erro | Próximo passo |
|---|---|---|---|---|
| 1 | UA | HRBS-14331 | Respondemos período-base do sick leave = 6 meses; demais fontes dizem 12 | Confirmar Postanova 1266 p. 4 e corrigir a resposta (revisão 05/10, proposta 3) |
| 2 | UA | HRBS-12181 | "65816 now has the formula" com coluna Formula vazia | Conferir WTC vigente |
| 3 | UA | HRBS-12181 / 14331 | Código 157: "não é de empregado" e depois configurado no 62942 | Decidir e registrar em [[correcoes]] |
| 4 | UA | HRBS-14331 | Correções possivelmente feitas no catálogo do cliente, não no WTC master | Conferir master |
| 5 | UA | SR-160–163 | HBOS/HBUH ausentes nas 4 specs J05; 12 tags de cabeçalho em D5/D6 | Confirmar se a v3 corrigiu tudo |
| 6 | ES | SR-80 × SR-432 | Mesma amostra `A26S0003.AFI` validou inbound e outbound | Abrir a amostra e decidir (revisão 05/10, pergunta 4) |
| 7 | ES | CT-A-485 | Pisos 1.424,50 / 1.929 / 1.599,60 / 1.391,70 sem fonte e contraditórios | Revisão 05/10, propostas 1 e 2 |
| 8 | ES | SR-79 | Root `Bases` sem namespace (08/10); 4212x; 563 com duas fórmulas | Seguir no ticket |
| 9 | CI | HRBS-14996 | GTN de empregado acima do teto com valores da linha "apprentice" (flag 58216?) `[INCERTO]` | Conferir flag e banda no design |
| 10 | NA | HRBS-14605 | Lista de relatórios entregue ≠ lista esperada pelo cliente | Publicar coberto/não coberto |
| 11 | NA | HRBS-13602 | CCG × WTC sobre WT 2551 pré-imposto | Ler a lei (ITA Namíbia) e alinhar |

## 6. Próximos passos
1. **Você:** aprovar/rejeitar F48–F59 e os reforços da seção 4.1 (ex.: "aprovo F48, F49, F52; rejeito F58").
2. **Eu, após aprovação:** acrescentar as entradas aprovadas ao `country_failure_log.md` (v2.12, com `.bak`), e os checks C48+ ao `PRESUBMISSION_AUDIT.md` como especificação (implementação dos scripts é outra etapa).
3. **Eu, após aprovação:** levar os erros da seção 5 para [[correcoes]] e hubs de país.
4. **Você:** restaurar o `.env` com `YOUTRACK_TOKEN` → eu rodo a API desde 2026-01-01 e completo este catálogo com jan–jul.

---

## Anexo: texto pronto para o `country_failure_log.md` (inglês, formato do log)

> Só entra no pipeline após aprovação. Fonte comum: "Support tickets Aug–Oct 2026 (brain-service catalogue 2026-10-08)".

### F48 — Official-file spec never diffed against the official layout/XSD (v2.12 NEW)
**Source:** ES M190/M111/M296/CERTIFICA/BASES (SR-79, 82, 83, 85, HRBS-13757); UA J05 forms D1/4DF/D5/D6 (SR-160–163).
**Observed:** Positions shifted, Type 2 records missing, numeric fields blank where zero is mandatory, no padding, HBOS/HBUH and 12 header tags absent. Found only when the portal rejected the file or the BA ran manual QC.
**Root cause:** The Dev tests the generated file against our own spec (circular). No step compares the spec with the authority's layout/XSD.
**Mitigation:** Check C48: every XSD element / layout position has a spec row; lengths, padding, enums and mandatory zeros compared mechanically.

### F49 — Wage type code renamed or retired without a sweep (v2.12 NEW)
**Source:** ES 57176/58176/58177 → 58552/58572, 65815, 79429/79430/79432 (SR-82, 85, 342, 83); UA 4DF codes (SR-415); ES 79416 (HRBS-10563).
**Observed:** Each artefact corrected separately; specs kept retired codes; opposite rename directions across reviewers.
**Root cause:** WTC change treated as local; no reverse lookup from WTC to specs/DD/CCG.
**Mitigation:** Check C49: every WT code cited in specs/DD/CCG exists in the current WTC with the same label.

### F50 — Tax/contribution flag on a wage type without a legal basis (v2.12 NEW)
**Source:** UA (HRBS-12181, 14331), NA (HRBS-12483, 12072, 13602), CG (HRBS-13841).
**Observed:** Flags set by analogy (life insurance like medical; gifts; civil contractors; pension flags) and later reversed by the client.
**Root cause:** The WTC has no column linking each flag to an instrument.
**Mitigation:** Check C50: a legal-basis column per flag; flag combinations documented per country.

### F51 — Annual limit or accumulator undefined (v2.12 NEW)
**Source:** CO 1,340 UVT ÷ 12 (HRBS-13627); SG CPF AW ceiling YTD calculated vs paid (HRBS-15630); CI 12× floors/ceilings (CT-A-620, HRBS-14996).
**Observed:** The engine applies annual limits monthly, or mixes calculated and paid amounts.
**Root cause:** Limits are stated without period, accumulator and status.
**Mitigation:** Check C51: each limit declares its period, accumulator, calculated/paid status and a per-band test.

### F52 — Ticket answer not consolidated into the artefact (v2.12 NEW)
**Source:** UA sick-leave base period 6 vs 12 months, 65816 formula, code 157 (HRBS-12181, 12631, 13392, 14324, 14331); ES answers from an old WTC copy (SR-85, SR-83).
**Observed:** The same fact was redefined across tickets; answers contradicted the artefact in force.
**Root cause:** Support answers bypass the pipeline; there is no single source of truth.
**Mitigation:** An answer cites the artefact version in force; a new fact from a ticket goes into CCG/WTC (with F27 propagation) before the reply.

### F53 — One name for different official files, or inbound/outbound confused (v2.12 NEW)
**Source:** ES "AFI" (SR-80, SR-432, HRBS-12839, CT-4321).
**Mitigation:** Check C53: spec title = official name + direction; a single table of file × direction × spec × sample.

### F54 — Report coverage list neither published nor reconciled with the client (v2.12 NEW)
**Source:** NA (HRBS-12101, 12111, 14605), CG (HRBS-12110), LT (HRBS-15253), NL (HRBS-14675).
**Mitigation:** The scaffolder emits a per-country coverage matrix (S/C/M/N); a report without an owner is explicitly out of scope.

### F55 — Acceptance without a real sample, or testing with the open fiscal year (v2.12 NEW)
**Source:** ES SR-83, SR-144, HRBS-13757; UA "true XML sample" (SR-160–163).
**Mitigation:** Check C55: acceptance requires a comparison with a real A3/portal sample, using a closed fiscal year.

### F56 — Field required by a spec or the WTC missing from the DD (v2.12 NEW)
**Source:** UA SR-414, HRBS-13389 (Insurance Record), 15216 (SSC Rate); ES `accrual_period_year` (SR-83, SR-342).
**Mitigation:** Check C56: every spec source field resolves to a DD field (spec → DD traceability).

### F57 — Payslip missing legal fields, or template diverging from Payslip Spec (v2.12 NEW)
**Source:** UA SR-340, CG/GA HRBS-12472, ES HRBS-13757, CN SR-316.
**Mitigation:** Check C57: per-country checklist of legal payslip fields; template diffed against Payslip Spec 1.

### F58 — Special pay cycles not covered (v2.12 NEW)
**Source:** CO off-cycle bonus (HRBS-12487), UA advance payroll (HRBS-14255), SG run order (HRBS-15630), ES leave spanning months (HRBS-10563).
**Mitigation:** Add a "cycles" axis to the F43 coverage matrix: off-cycle, advance, retro, leave across months, run order.

### F59 — Version label/changelog not matching the file; revised version deleted (v2.12 NEW)
**Source:** UA (v3.5 named V3.4, DD "v3.7" attached as "V3.8", changelog entries with no change); CL SR-221 (revised spec deleted).
**Mitigation:** Check C59: file name, Version Control and content cite the same version; a revised version is never deleted (complements F47).

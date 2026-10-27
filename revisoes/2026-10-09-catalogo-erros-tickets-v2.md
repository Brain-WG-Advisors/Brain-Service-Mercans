# Catálogo de erros e soluções: v2 (2026-10-09)

> Índice: [[00-INDEX]] · Correções: [[correcoes]] · v1 (só PDFs): `revisoes/2026-10-08-catalogo-erros-tickets.md` · Pipeline: `~/mercans-pipeline/shared/country_failure_log.md`
> **Nada foi aplicado no pipeline.** As seções 4 e 5 são propostas e precisam de aprovação.

## 1. Fontes
| Arquivo (`raw/tickets/extracao/`) | Conteúdo |
|---|---|
| `2026-10-08-erros-solucoes-{UA-A,UA-B,ES-A,ES-B,AF,OUT}.md` | 60 tickets lidos dos PDFs (snapshots de 04/08 a 08/10) |
| `2026-10-09-desfecho-{UA,ES,AF-OUT}.md` | Desfecho real dos 58 tickets acima, pela API (comentários posteriores ao snapshot, solução final, correções à análise de 10-08) |
| `2026-10-09-erros-solucoes-NOVOS-{A,B}.md` | 79 tickets atribuídos a nós que não tínhamos (2024-05 a 2026-10), com seção "Soluções reutilizáveis" |

Tickets brutos: `raw/tickets/api/2026-10-09/` (137 arquivos, **fora do git**: contêm dados pessoais e uma senha colada pelo cliente no HRBS-14714).

## 2. Retrato

| | Tickets | Resolvidos | Parciais | Abertos | Cancelados/rejeitados |
|---|---|---|---|---|---|
| Já analisados (desfecho pela API) | 58 | ~25 | ~20 | ~13 | — |
| Novos (2024–2026) | 79 (69 com conteúdo) | 49 | 9 | 3 | 5 |

**Lição da v1 → v2:** os PDFs davam 32 tickets "não resolvidos"; pela API, 35 dos 58 já estavam Resolved/Done. Snapshots exportados à mão não servem para medir desfecho; a API sim.

**Tipos de erro nos 79 novos:** T11 pedido/explicação (30), T6 escopo (20), T12 fonte ausente/contraditória (19), T7 cálculo (16), T2 tratamento do WT (12), T10 cliente × artefato (12). **Padrões mais citados:** F54 cobertura de relatórios (20), F52 resposta não consolidada (10), F50 flag sem base legal (9), F43 (8), F57 payslip (7), F44/F41 (7).

## 3. O que os tickets dizem (ano inteiro)
1. **Metade do trabalho de suporte é definir escopo e explicar cobertura** (T11 + T6). Sem uma lista publicada por país do que é coberto/não coberto (F54), cada cliente pergunta de novo: samples, payslip local, relatórios custom × estatutários, SAFF, PAYE 5, VET, IT12E.
2. **Nossas respostas mudam de posição dentro do mesmo ticket** (F52): TR seguro de vida (3 versões), NL 58552 (fixo anual → período + acumulado, sem decisão), UA sick leave 6 → 12 meses (nunca retirado por escrito), ES AFI (amostra errada). A correção quase sempre veio da BA ou do cliente.
3. **Flags de WT decididos sem lei** (F50) e **WT de ajuste sem as flags do WT principal** (SA GOSI 62102/62402, EG Martyrs Fund): erro recorrente em países sem dossiê completo (Golfo, Norte da África, Holanda).
4. **Specs de arquivo oficial falham no portal, não no QC** (F48/F55): ES M190/M111/M296/CRA, UA J05, NL XML Retro. O teste do Dev contra a nossa spec é circular.
5. **Tickets fechados sem solução**: 8 tickets fechados em lote em 2025-12-29; HRBS-9807 (defeito real no DD da Holanda) e HRBS-2489 ("assumo resolvido") fechados por inatividade; HRBS-12839 fechado com resposta errada.

## 4. Padrões para o pipeline

### 4.1 F48–F59 (v1): ajustes após o desfecho
| F | Ajuste |
|---|---|
| F50 | Perde HRBS-13602 e 13841 (não eram erro nosso); ganha HRBS-1272, 1534, 8399, 8650, CT-3648, CT-4322 |
| F51 | Perde HRBS-15630 (comportamento correto: teto anual de AW menos OW do ano); mantém CO 1.340 UVT, CI 12× |
| F54 | Passa a ser o padrão mais frequente (20 tickets novos); prioridade alta |
| F58 | Enfraquece (HRBS-12487 resolvido por redesenho; 15630 não era defeito) |
| — | "Duplicado HRBS-14714 × 14996" da v1 estava errado: são perguntas diferentes |

### 4.2 Novos (F60–F66), dos 79 tickets novos
| Novo | Título | Origem | Check proposto |
|---|---|---|---|
| F60 | WT de ajuste/correção sem as flags e a base do WT principal | HRBS-8303 (SA), 8650 (EG) | C60: todo WT de ajuste herda as flags do principal ou declara a exceção com fonte |
| F61 | Contribuição existente no catálogo não ativada na entidade | HRBS-8439 (TN, TFP 2%) | C61: toda contribuição do CCG tem WT ativo no setup da entidade |
| F62 | Definição fiscal produzida por IA sem oráculo independente | HRBS-1535 (NL 58552) | Regra: definição de base fiscal exige fonte oficial citada; reforço de F41 |
| F63 | Fonte secundária (portal/site) contradiz a lei citada sem reconciliação | HRBS-1629 (JO) | Regra: divergência portal × lei vira pergunta registrada, não escolha silenciosa |
| F64 | Convenção de sinal/arredondamento não especificada (G2N, PILA) | HRBS-6847 (QA), HRBS-182 + CT-617 (CO) | C64: CCG declara sinal, arredondamento e unidade de cada contribuição |
| F65 | Competência × pagamento (retro, pagamento após desligamento) sem regra | HRBS-2278 (AU), HRBS-2489/2621 (NL) | Eixo "competência" no F43/F58 |
| F66 | Handover sem folha de configuração (WT → códigos de entrada/saída) | HRBS-7074 (TN), CT-3661 (CZ) | C66: handover inclui a tabela de configuração por WT |

## 5. Os 11 erros nossos da v1: desfecho
| # | Erro | Desfecho | Falta |
|---|---|---|---|
| 1 | UA sick leave 6 × 12 meses | **12 meses** (Postanova 1266); adotado no Guia em 09-21 | Conferir coluna K do WTC V3.9; o "6 meses" nunca foi retirado por escrito no ticket |
| 2 | UA "65816 now has the formula" | Retirado por nós em 08-11; gross-up é regra do motor | Dev confirmar o motor; decidir o PE 58134 nunca construído |
| 3 | UA código 157 | **Resolvido**: 157 = contratado civil FOP, WT 62942, PIT/ML/USC Não | — |
| 4 | UA correções no catálogo do cliente | Provavelmente no master ("Finalized WTC") [INCERTO] | Abrir as duas planilhas |
| 5 | UA HBOS/HBUH nas specs J05 | **Corrigido nas v3**; HBOS é obrigatório no D6 (nossa resposta de 08-24 estava errada) | Conferir D1/4DF/D5; linhas "Blank" do D5 (Lily, 10-09) |
| 6 | ES amostra A26S0003.AFI | **Resolvido**: amostra do SR-80 era errada, trocada em 09-15 (SR-80 v2.1, DD v5.0) | Corrigir a resposta no HRBS-12839 (fechado errado); renomear título do SR-80 |
| 7 | ES pisos do CT-A-485 | Corrigido no cérebro (10-08) | KB e fórmulas dos WTs de piso (Design/Dev) |
| 8 | ES SR-79 | Namespace e gatilho 68460-68464 em acceptance (10-09) | WT 563: fórmula SUM(79415;79416) em produção × 58151 com gate |
| 9 | CI GTN (banda apprentice / 58216) | **Aberto**, e mais urgente: Stop Tax ligado em 09-29 | Abrir ticket dos defeitos do GTN |
| 10 | NA lista de relatórios | Parcial: IT12E/IT14E não são do empregador; VET existe (folha ≥ N$1 mi) sem relatório | Publicar coberto/não coberto; decidir VET |
| 11 | NA WT 2551 pré-imposto | **Resolvido; não era erro nosso** (resposta de 08-24) | — |

**Erros nossos novos, já corrigidos** (levar a [[correcoes]]): UA 62180/62181 ESV e 4DF; 65700–65712 ESV; 79406 código 128 → 101; 65808 4DF 126 → 125; TR seguro de vida (limites cumulativos → só o teto anual é cumulativo); CG WTC SS patronal (3 linhas com a mesma fórmula → v1.1 por ramo).

**Erros novos ainda abertos:** IE HRBS-13860 (classe PRSI de leavers vira J0 no motor; correção manual); NA WTs 2550/2551 ainda com teto N$99 em agosto (SSC aplica N$12.500 desde 2026-09-01); NL HRBS-9807 (DD Contract Type 5 × 2 opções, fechado por inatividade); NL HRBS-1535 (58552 sem decisão); ES payouts 79417–79424 delegado × directo; CG HRBS-12110 (matriz com conteúdo do Senegal e ITS ~10× errado).

## 6. Conhecimento reutilizável (onde está)
Seção "Soluções reutilizáveis" de cada arquivo `2026-10-09-erros-solucoes-NOVOS-*.md` e "Conhecimento a absorver" dos `2026-10-09-desfecho-*.md`. Destaques: TR dedução de seguro de vida; CG CNSS por ramo (PVID 8%/1,2 mi; PF 10,03%/600 mil; AT-MP 2,25%/600 mil); MY EPF para não cidadãos; AU flags do WTC 3.2 e escopo; IE opt-out do auto-enrolment; NL XML Retro (2559 fora, 2554 dentro), 30% ruling, UWV com 8% embutido, betalingskenmerk; TN CNSS/TFP/FOPROLOS; SA GOSI e EG Martyrs Fund; CO embargo, IBC, retención (CCG/WTC v1.1); UA faixas do sick leave 50/60/70/100 (Lei 1105 art. 17), código 128 só maternidade PFU.

## 7. Próximos passos
1. **Você:** aprovar/rejeitar F48–F66 (seções 4.1 e 4.2 desta v2 e 4.2 da v1).
2. **Eu, após aprovação:** levar os padrões aprovados ao `country_failure_log.md` (v2.12, com `.bak`) e os checks ao `PRESUBMISSION_AUDIT.md`.
3. **Eu, agora (regra do cérebro):** registrar em [[correcoes]] os erros nossos já corrigidos (seção 5) e nos hubs de país o conhecimento da seção 6.
4. **Você:** pedir a remoção da senha colada no HRBS-14714; corrigir a resposta do HRBS-12839.

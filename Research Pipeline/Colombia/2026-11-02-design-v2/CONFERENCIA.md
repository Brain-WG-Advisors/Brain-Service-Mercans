# Colômbia — design v2.0 (conferência)

> Hub: [[Colombia]] · Base: [[Research Pipeline/Colombia/2026-10-29-validacao-research/final/design/README|design v1_2]] · Modelo: [[Research Pipeline/Chad/2026-11-02-design-v6/CONFERENCIA|Chade v6]] · Decisões: [[TABELA-RODADA6]], [[TABELA-RODADA5]]
> Rascunho local, 2026-11-02. **Não vai ao Drive nem ao Dev sem ok do usuário.** `final/design/` (v1_2) não foi alterado.

## Fonte
- Regras: design v1_2 (`final/design/CO_Regulation_Design_v1_2.md`, 57 regulações), atualizado para os finais da rodada 6 (CCG v1.7, WTC v1.9, DD v1.6, SIR v1.4).
- Forma: esquema do Dev (td.json do Chade: ordinal, taxGroup, taxRuleGroup, taxationType, assertion, bands com fórmula e contas, taxabilityRules). Para a Colômbia o Dev só tem uma linha (planilha "CO Draft Regulations", 25/11/2025): `9170132` "CO Income Tax Flat", flat, income_tax, `simple_tax_post_formula`, ordinal 132, assertion `EQUALS($64552;2)`.
- Referência dos cenários: cálculo independente da lei (`oracle/oracle_v2.py`, só lido), com os tetos de 790 / 1.340 UVT pelo acumulado do ano (mesmo método de `revisao/rodada5/scripts/oracle_r5_ytd.py`).

## Arquivos
| Arquivo | O que é |
|---|---|
| `co_design_v2.json` | 79 regulações no esquema do Dev (rodada 3, md5 `e029d8b9…`) |
| `oracle_r3/` | cópia ajustada do cálculo independente (original intacto) |
| `co_engine.py` | motor que executa o JSON (semântica S1–S16, porta do `sim_dev.py` do Chade) |
| `_build_v2.py` | gera o JSON e roda as checagens (a)–(d); `VALIDATION-run.txt`, `SWEEP-run.txt`, `_run-summary.json` |
| `_write_blueprint.py` | escreve o pacote a partir do JSON e da execução |
| `scripts/gen_matrices.py` | cópia do gerador do v1_2 com pacote `v2_0` |
| `co-design-blueprint-v2/` | Regulation_Design v2_0, Memo v2_0, Matrizes + CSV v2_0 (do WTC v1.9), ASSUMPTIONS, RESEARCH_GAPS, VALIDATION, CHANGELOG (inglês, sem referência interna: varredura 0) |

## Decisões
1. **Forma do Dev onde a lei não obriga diferença:** ID = 9170000 + ordinal; o IR do não residente é exatamente o `9170132` "CO Income Tax Flat" do Dev (flat 20%, `simple_tax_post_formula`, ordinal 132); totais depois dele (139, 141). Assertion lê `58205` (DD) em vez de `$64552`, mesma codificação 2 = não residente → confirmar a conta com o Dev (ASSUMPTIONS A5).
2. **`retro_` decidido pela lei:**
   - IR sem `retro_`, como o Dev: Proc. 1 aplica a tabela à "totalidad de dichos pagos que se hagan al trabajador … durante el respectivo mes" (DUR 1625 art. 1.2.4.1.3, lido em `raw/docs/oficiais/CO/2026-10-13-DUR-1625-2016-DIAN.htm`). 92%.
   - Seguridade social com `retro_` — **Deliberate divergence (law)**: correção de período passado vai na planilla N (AT2 v30, "Disposiciones comunes a la Planilla N": registro A original, registro C IBC corrigido; lido no `.txt` do AT2 v30). 92%.
3. **Ordem:** pagamentos que alimentam as bases (férias, prima, cesantías, incapacidade, licença, indenização, aprendiz) passaram para antes das bases (ordinais 9–32).
4. **Regras novas, todas com fonte primária lida nesta tarefa:**
   - piso C-543/2007 em todos os segmentos da incapacidade, inclusive dias 91–180 (parte resolutiva: o auxílio do art. 227 "no podrá ser inferior al salario mínimo legal vigente") — 93%;
   - retenção das indenizações sobre R339 + R343 + R344 (ET 401-3 "Las indemnizaciones derivadas de una relación laboral…"; DUR 1.2.4.1.13) — 85% (R341/R342 ficaram como lacuna R8);
   - prima com leitura própria da tabela (DUR 1.2.4.1.3 Proc. 1: "el valor a retener es el que figure frente al intervalo al cual corresponda la respectiva prima") — 95%; a divisão do teto anual entre a leitura do salário e a da prima é opção configurável (A1, 80%);
   - projeção de período < 30 dias como opção desligada (DUR 1.2.4.1.3 lits. a–b, "podrá") — 95%.
5. Textos da rodada 6 no pacote: C-397/1994 e Concepto 577/2020 (cesantías de não residente), Decreto 1469 com o 0159 "left without effect", C-543, incapacidade e licenças fora de SENA/ICBF/CCF, código 46 (lado dos relatórios).

## Antes → depois (defeitos do v1_2 achados pelo motor, variante fiel ao v1_2)
1. 47 leituras antes de a conta ser lançada (ex.: IBC lia férias/incapacidade/licença lançadas nos ordinais 85–94; retenção da indenização lia a indenização do ordinal 91).
2. Auxílio de transporte duas vezes na base da prima e das cesantías (linha R304 com W = Yes + 52503 pela fórmula): P01 1.749.095 em vez de 1.624.548.
3. Base do não residente pela coluna N; a coluna P difere em 15 linhas (aposentadorias, gratificações de fim de contrato).
4. Prima e indenização dentro da leitura mensal da tabela.
5. Retenção da indenização só sobre a do art. 64.
6. Texto de conferência do v1_2 errado no piso da incapacidade (I03 dias 91–100: 583.635, não 500.000).
Tabela regulação a regulação: `co-design-blueprint-v2/CHANGELOG.md`.

## Conferência (`python -I _build_v2.py`)
- **Reprodução do método:** o mesmo motor sobre a variante v1_2 reproduz o cálculo independente na cadeia mensal (59 casos, 2.153 valores; 11 diferenças = 4 de um centavo no C23 + 7 do RC01, porque a opção de projeção < 30 dias não existia no v1_2).
- **(a) Ordem v2:** 0 defeitos (v1_2: 47).
- **(b) Cenários v2:** 112 casos, 2.293 valores, 12 diferenças, todas explicadas:
  - I03/I04 (6): piso C-543 nos dias 91–180 — o desenho segue a parte resolutiva; o cálculo independente não aplica o piso;
  - L15/L21 (2): total da pensão tipo 51 com 1 peso — arredondamento por parcela × total (A2, aberto);
  - C23 (4): 1 centavo — o cálculo independente acumula o consumo do teto anual arredondado ao centavo.
- **Conferências do desenho (conta à mão pela lei):** 11/11 exatas, inclusive os 4 exemplos do CCG v1.7 com tetos anuais pelo acumulado (3.947.554,80; 1.763.832,00; 1.899.912,00; 3.243.282,00).
- **(c) Varredura:** 298 linhas ativas do WTC v1.9 × 9 bases = 2.682 checagens, 0 diferenças; 21 linhas `Yes/No` ficam falsas até o split de wage type (lista em RESEARCH_GAPS R1). Na variante v1_2: 16 diferenças (12 da coluna P, 4 do roteamento prima/indenização).
- Matrizes e CSV regenerados do WTC v1.9: CSV com o mesmo md5 do v1_2 (`4e5f8fd1…`), porque as colunas N–X não mudaram na rodada 6.
- QA independente: **não rodado** (fica para outro agente, por instrução).

## Rodada 2 (pós-QA r1: `QA-REVIEW-r1.md`, FAIL 0 blocker / 5 major / 9 minor)
Fontes relidas nesta rodada: DUR 1625 art. 1.2.4.1.8 ("indemnizaciones por despido injustificado y bonificaciones por retiro definitivo"; "dividiendo por doce (12), o por el número de meses de vinculación si es inferior a doce"); Decreto 780 art. 3.2.1.5 num. 2 / Decreto 1990/2016 art. 1 ("El valor de los aportes liquidados por cada cotizante … múltiplo de 100 superior"); AT2 v30 campo 47 (IBC × tarifa, com a regra de arredondamento); ET arts. 55 e 56 ("los aportes obligatorios que efectúen los trabajadores"); CST art. 65 ("como indemnización"); td.json do Dev (banda patronal em `employerRate`, mesma regulação da banda do empregado); CCG v1.7 (Módulo 6: prima "folded into the ordinary monthly base" no Proc. 2; Módulo 9: indenização e bonificação por retiro fora da base mensal, exemplo de 4.500.000 com o teste dos 204 UVT sobre o salário).

| Achado | O que mudou | Prova |
|---|---|---|
| Q1 | `9170073` põe a prima (R320) na base mensal do Proc. 2 | X12 = 1.057.500 |
| Q2 | R345 fora da leitura mensal; `9170090` retém pela % da tabela da média (art. 1.2.4.1.8); os 20% do 401-3 ficam só para indenização | X13 = 0 (antes 2.343.432) |
| Q3 | `9170088`: média ÷ MIN(12; meses de vínculo) — input novo `58259` | X14 = 194.649 (antes 0) |
| Q4 | uma regulação por fundo com banda do empregado (`employeeRate`) e do empregador (`employerRate` / `employerRateAccount`), como o td.json; motor lê os dois campos e marca a parcela | checagem 0 erros; cópia com a banda patronal de saúde trocada: pega (1 erro) |
| Q5 | fator de projeção = 1 fora do Proc. 1 (`9170074`) | X15 = 341.250 com a opção ligada |
| m1 | R340 (CST 65 "como indemnización") roteada com as indenizações; R341/R342 seguem lacuna R8 | sweep N roteado |
| m2 | 9170132 lê `$64552` como o Dev (flag de residência inteiro em 64552); chaves `regulationId` e `systemTaxYearIds` (`co_2026`, A10) | JSON |
| m3 | CHANGELOG: item 7 (17 regulações de IR `retro_` → `simple_tax*`) e seção da rodada 2 | CHANGELOG |
| m4 | arredondamento único por cotizante e fundo; EE arredondado, ER = total − EE (A2 decidido, divisão 85%); INCRNGO pelos aportes descontados (A9, 90%) | X17 = 218.900 / 280.200 |
| m5 | bruto sem cesantías consignadas (`9170039` soma no desligamento), deduções com valor negativo (S18); líquido − espécie R319 − 58257 − 58258 | X18–X20 |
| m6 | checagem da coluna O ligada; VALIDATION diz que a varredura testa o mecanismo; casos X12–X20 | O = 0 |
| m7 | Memo: sem "provider payroll", sem opção de 20% nas cesantías, refs R2/R3, item 18 e item 19 na tabela, sem pasta do Drive; matrizes: "split" sem ⚠ | varredura de texto 0 |
| m8 | R2 ampliado: pensão, FSP, CCF e prestações da fase prática ficam 0 até o split | RESEARCH_GAPS R2 |
| m9 | teste dos 204 UVT sobre o salário mensal `$64992` (exemplo do CCG) | X16 = 937.813 |
| Fora do pedido | registrados em RESEARCH_GAPS R12 (CCG l. 1688 × l. 1972, teto da base de parafiscais do integral) e R13 (AT2 v30 × CCG, vigência da Ley 2381) | — |

**Conferência rodada 2** (`python -I _build_v2.py`, 79 regulações; JSON md5 `f8b1f49b…`):
- Ordem: 0 defeitos (S17: banda pode ler banda anterior da mesma regulação).
- Cenários com a convenção de arredondamento do cálculo independente (variante "parcelas"): 112 casos, 2.293 valores, 12 diferenças — as mesmas da rodada 1 (I03/I04 piso C-543; L15/L21 1 peso; C23 1 centavo).
- Cenários com o arredondamento do desenho: 238 diferenças = 30 parcela patronal (resíduo do total arredondado) + 198 linhas de retenção (INCRNGO pelos aportes descontados) + as 10 de cima (C23, I03/I04); L15/L21 agora batem no total (210.109).
- Conferências à mão: 20/20 exatas (X1–X20). Varredura: 2.682 checagens, 0. Coluna O: 0. Troca EE/ER: pega.
- Variante v1_2: ordem 47, 34 diferenças, varredura 18 (12 coluna P, 6 roteamento).
- Confiança: 95% nos casos testados; decisões A2 (divisão do total, 85%) e A9 (INCRNGO descontado, 90%) declaradas.

## Rodada 3 (pós-QA r2: `QA-REVIEW-r2.md`, PASS com 5 minor)
| Achado | O que mudou | Prova |
|---|---|---|
| n1 | parte do empregado = 4% ao peso (Ley 100 arts. 20 e 204); patronal = total do fundo arredondado ao múltiplo de 100 (Decreto 780 art. 3.2.1.5 num. 2) − parte do empregado; onde o empregado paga o fundo todo (saúde exonerada, FSP) a parte dele leva o arredondamento; A2 reescrito (92%) | X17: saúde 218.900, pensão 280.200 |
| n2 | banda patronal escrita a partir da base (`$58106`, `$58112`, `$58197`), sem ler a banda irmã; verificação de ordem estrita (sem exceção S17) | ordem 0; troca EE/ER pega |
| n3 | tabela "Consumed by" das Matrizes com os IDs do v2 (e `9170044` no texto do excesso) | Matrizes v2_0 |
| n4 | pacote em inglês sem rodadas nem códigos de revisão (CHANGELOG "Changes after the independent review"; casos X12–X20 pelo assunto; A2 sem "round"); histórico só aqui | varredura de texto 0 |
| n5 | nota da `9170072` com R320, R339, R340, R343, R344, R345; defeito 4 lido por `9170089`–`9170093` (+ `9170073` no Proc. 2); itens 6/7 e A1–A10 em ordem | CHANGELOG / ASSUMPTIONS |
| Cálculo independente | cópia ajustada `oracle_r3/oracle_v2_r3.py` (+ `params.json`); o original `oracle/oracle_v2.py` intacto (md5 `c09f0e6f…`). Ajustes: R3-1 aporte arredondado uma vez por fundo, parte do empregado ao peso, patronal = total − empregado; R3-2 INCRNGO = aportes descontados | 112 casos, 2.293 valores: **6 diferenças**, todas I03/I04 (piso C-543); o centavo do C23 sumiu |

**Conferência rodada 3** (79 regulações; JSON md5 `e029d8b9…`): ordem 0; convenção antiga (parcelas): 12 (as mesmas); contra o cálculo independente original: 293 = 42 parte do empregado ao peso + 43 resíduo patronal + 198 retenção (aportes descontados) + 10 já explicadas; **contra a cópia ajustada: 6 (C-543)**; conferências à mão 20/20; varredura 2.682 / 0; coluna O 0; troca EE/ER pega; variante v1_2 inalterada (47 / 34 / 18).

## Bloco de prova
- **Pedido → resposta:** JSON no esquema do Dev (1); motor (2); ordem, cenários, varredura e forma do Dev (3); pacote em inglês (4); esta conferência (5).
- **Fontes lidas nesta tarefa:** DUR 1625 art. 1.2.4.1.3 (Proc. 1, prima, projeção); ET 401-3 e DUR 1.2.4.1.13; C-543/2007 parte resolutiva; AT2 v30 planilla N; td.json do Chade (esquema); "CO Draft Regulations" (linha 9170132). Demais regras: as do v1_2 e da rodada 6, com as fontes já registradas lá.
- **Teste:** `VALIDATION-run.txt` e `SWEEP-run.txt` gerados pela execução; varredura de referências internas do pacote: 0.
- **Confiança:** 95% de que o desenho executado = cálculo independente nos casos testados (diferenças explicadas acima). A aceitação da semântica do motor (S1–S16, CEILING, DAYS360) depende do motor real.

## Quem mexeu
| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | validacaoco (fork) | design v2.0 criado: JSON no esquema do Dev, motor, checagens (a)–(d), pacote; v1_2 intocado |
| 2026-11-02 | validacaoco (fork) | rodada 2 pós-QA r1: Q1–Q5, m1–m9; QA-REVIEW.md renomeado para QA-REVIEW-r1.md |
| 2026-11-02 | validacaoco (fork) | rodada 3 pós-QA r2: n1–n5; cópia ajustada do cálculo independente em `oracle_r3/`; QA-REVIEW.md renomeado para QA-REVIEW-r2.md |

## Subida ao Drive (2026-11-02, ok do usuário)
- `07 - Design`: CO_Regulation_Design_v2_0.md, CO_Statutory_Research_Memo_v2_0.md, CO_Taxability_Matrices_v2_0.md, CO_Taxability_Perimeters_Extract_v2_0.csv; subpasta `CO_Design_v2_0_supporting/`: ASSUMPTIONS, RESEARCH_GAPS, VALIDATION, CHANGELOG e co_design_v2.json (`e029d8b9…`). md5 dos 9 = local. Os 4 do v1_2 → `07 - Design/Archived/`. `co_engine.py` ficou só local (a documentação cita caminhos internos).

| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | validacaoco | Design v2_0 no Drive (07 - Design); v1_2 → Archived |

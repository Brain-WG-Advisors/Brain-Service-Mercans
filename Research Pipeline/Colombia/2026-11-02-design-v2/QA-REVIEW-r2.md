# Colômbia — design v2.0: revisão independente de QA (rodada 2)

> Hub: [[Colombia]] · Revisado: [[Research Pipeline/Colombia/2026-11-02-design-v2/CONFERENCIA|CONFERENCIA do v2.0]] (seção "Rodada 2") · Rodada 1: [[Research Pipeline/Colombia/2026-11-02-design-v2/QA-REVIEW-r1|QA-REVIEW-r1]] · Padrão: [[Research Pipeline/Chad/2026-11-02-design-v6/QA-REVIEW|QA do Chade v6]]
> Revisor: QA adversarial independente (não construiu o v2.0). Data: 2026-11-02. Modo: **só leitura**. Este é o único arquivo gravado na pasta.

## Veredito: **PASS** (0 blocker, 0 major, 5 minor)

Os 14 achados da rodada 1 (Q1–Q5, m1–m9) estão fechados, e confirmei cada um por probe próprio e por conta à mão. Não há regressão nos valores.

Das 238 diferenças contra o cálculo independente, 228 são novas e vêm do arredondamento. Nelas, **o desenho está certo e o cálculo independente está errado**, pelas fontes primárias. Há um ponto em que os dois lados erram igual: a parte do empregado arredondada para cima em COP 100, sem fonte (n1).

Os 5 minors são de texto do pacote e de uma premissa do motor. Nenhum muda valor de hoje.

O PASS vale para o **design local**. Continuam fora do artefato:
- o aceite da semântica no motor real (S1–S18, `CEILING`, `DAYS360`, leitura de histórico R3);
- o split das 21 linhas `Yes/No` (R1, R2);
- a regra 9: Colômbia ativa exige ticket ao Development antes de qualquer alteração em produção.

## Como conferi
- **Reexecução:** a pasta nova foi copiada para o scratchpad, com junction só de leitura para `2026-10-29-validacao-research`. `python -I -B _build_v2.py`: rc 0. Os 4 produtos saíram **idênticos** (md5) aos da pasta:
  - `co_design_v2.json` `f8b1f49b…`
  - `VALIDATION-run.txt` `51892e3b…`
  - `SWEEP-run.txt` `56d661e4…`
  - `_run-summary.json` `af97d465…`

  Resultados da execução:
  - 79 regulações;
  - ordem 0;
  - variante "parcelas": 12 diferenças;
  - arredondamento do desenho: 238 diferenças;
  - X1–X20: 20/20;
  - varredura: 2.682 checagens, 0 diferenças;
  - coluna O: 0;
  - Q4: 0 erros no desenho, e 1 erro na cópia com a banda patronal trocada (a checagem pega a troca).
- **Diff** do `_build_v2.py` e do `co_engine.py` contra a rodada 1. Mudaram:
  - `INDEMN` passou a incluir R340, e entrou o `BONUS` (R345);
  - `$64552`, `regulationId` e `systemTaxYearIds`;
  - novas 9170039, 9170073, 9170088 e 9170090;
  - contribuições por fundo com banda EE e banda ER (`ebandr`, `ER_REST`);
  - 58151 sobre os aportes descontados;
  - fator de projeção só no Proc. 1;
  - teste dos 204 UVT sobre `$64992`;
  - líquido em caixa;
  - S5, S10, S17 e S18 no motor;
  - casos X12–X20, `share_check` e checagem da coluna O.

  As constantes 52501–52542 e a tabela do art. 383 **não mudaram**.
- **Meu verificador de ordem** (o mesmo da rodada 1, agora com `regulationId`):
  - 0 leitura de conta lançada por regulação posterior;
  - IDs = 9170000 + ordinal nas 79;
  - sem duplicatas.

  Ele aponta 6 leituras **dentro da mesma regulação**: na 9170056, 9170057 e 9170064, a banda ER lê `$58121/58122/58127` e os `_raw` da banda EE. Isso é a premissa S17 (n2).
- **WTC v1.9 inteiro:** 405 linhas contra as 9 matrizes (14 X, 20 W, 45 Q, 47 T, 49 U, 50 R, 51 S, 72 N com R320/R339/R340/R343/R344/R345 roteadas, 132 P). Resultado: **0 divergências**. A 9170072 tem 257 linhas true e 41 false.
- **Fontes primárias relidas** (`raw/docs/oficiais/CO/`):
  - Decreto 1990/2016 art. 1, que dá o novo texto do art. 3.2.1.5 do Decreto 780;
  - AT2 v30 campo 47;
  - ET arts. 55 e 56 (`2026-10-30-ET-pr002-art55`);
  - DUR 1625 arts. 1.2.4.1.3, 1.2.4.1.6 e 1.2.4.1.8;
  - `td.json` do Chade (bandas CNPS).

## 1) Achados da rodada 1: situação
| ID | Situação | Prova (probe meu e conta à mão) |
|---|---|---|
| Q1 | ✅ fechado | 9170073 (`acc('R320')`, assertion P2, debit 58150). Proc. 2 a 10%, 10.000.000 + prima 5.000.000. À mão: IBC 10.000.000 → 400.000 + 400.000 + FSP 50.000 + 50.000 = 900.000; (15.000.000 − 900.000) × 0,75 = 10.575.000 × 10% = **1.057.500**. Motor: 58150 = 15.000.000, 58162 = 1.057.500. Proc. 1 sem mudança: 58150 = 10.000.000, 58161 = 351.399, 58165 = 0 |
| Q2 | ✅ fechado | R345 false em 9170072; a 9170090 aplica `58243`. À mão: 58.500.000 ÷ 12 = 4.875.000 = 93,08 UVT ≤ 95 → 0%. Motor: 58150 = 4.500.000, 58168 = **0**, 58169 = 0 (antes, 2.343.432) |
| Q3 | ✅ fechado | 9170088 divide por `MIN(12;MAX($58259;1))`. À mão: 36.000.000 ÷ 6 = 6.000.000; (6.000.000 − 95 × 52.374) × 0,19 = **194.649**. Motor: 194.649 |
| Q4 | ✅ fechado | Uma regulação por fundo, com banda EE em `employeeRate` e banda ER em `employerRate`/`employerRateAccount` nas 9 contas patronais (58141–58146, 58137–58139). É a forma da «TD CNPS Contribution EE and ER» do `td.json` (EE 3,5 em `employeeRate`; 7,5/4/5 em `employerRate`). O S5 lê os dois campos e grava a parcela. `share_check`: 0 erros, e a cópia com a banda patronal de saúde trocada dá 1 erro |
| Q5 | ✅ fechado | 9170074: `EQUALS($58206;1)` no fator. À mão, Proc. 2 a 10%, 15 dias: 5.000.000 − 450.000 = 4.550.000 × 0,75 × 10% = **341.250**. Motor com a opção ligada: fator 1, 58162 = 341.250. Proc. 1 com a opção ligada: fator 2, 58161 = 175.700 (351.399 ÷ 2), certo |
| m1 | ✅ | R340 roteada. Probe: salário 9.000.000 + R340 5.000.000 → 0,093781 × 5.000.000 = 468.907 (motor 468.907), fora da leitura mensal |
| m2 | ✅ | 9170132 com `EQUALS($64552;2)`, igual ao Dev; `regulationId` e `systemTaxYearIds` (A10 declara `co_2026` por analogia) |
| m3 | ✅ | CHANGELOG item 7 e coluna "rule group retro_ → simple_tax (item 7)" nas linhas de IR |
| m4 | ✅ (ver §2 e n1) | X17: saúde 70.100 + 148.800 = 218.900 = ⌈12,5% × 1.750.905⌉₁₀₀; pensão 70.100 + 210.100 = 280.200 = ⌈16%⌉₁₀₀. Tipo 51: 52.527 + 157.582 = 210.109, igual ao AT2 campo 47. Alto risco, 33.000.000: 1.320.000 + 7.260.000 = 26% × 33.000.000 |
| m5 | ✅ | 9170040 sem R321/R322 e 9170039 só no desligamento. X18: líquido = 5.300.000 − 300.000 (espécie) − EE − retenção − 200.000. X19: 6.120.000. X20: R6 −1.000.000 → 58101 = 4.000.000. Não residente com cesantía 1.000.000: líquido 8.700.000 = 12.000.000 − 900.000 − 2.400.000 |
| m6 | ✅ | Checagem da coluna O ligada (0). O VALIDATION diz que a varredura testa o mecanismo. Casos X12–X20 incluídos |
| m7 | ✅ | Memo sem «provider payroll», sem a opção de 20% nas cesantías, sem «open item 7/8», com os itens 18 e 19 na tabela e sem pasta do Drive. Matrizes: 0 "⚠" |
| m8 | ✅ | R2 ampliado (pensão, FSP, CCF, prestações e férias da fase prática). Probe: fase prática com 58122 = 0, como declarado |
| m9 | ✅ | 9170089: `GREATER(DIVIDE($64992;$52502);204)`. À mão (X16): 9.000.000 = 171,84 UVT < 204 → média 108.000.000 ÷ 12 = 9.000.000 → (171,8410 − 150) × 0,28 + 10 = 16,11548 UVT → 9,3781% × 10.000.000 = **937.813**. Motor: 937.813. Antes, com 58150 = 11.000.000 = 210 UVT, davam-se 20% = 2.000.000 |

## 2) As 238 diferenças: quem está certo
| Grupo | Exemplo | Fonte primária | Veredito |
|---|---|---|---|
| **30 na parte patronal** (salud_emp 10, pension_emp 20) | C01 pensão: EE ⌈70.036,20⌉₁₀₀ = 70.100. Desenho: ER = ⌈280.144,80⌉₁₀₀ − 70.100 = **210.100**, total 280.200. Cálculo independente: ER = ⌈210.108,60⌉₁₀₀ = 210.200, total 280.300 | Decreto 780 art. 3.2.1.5 num. 2 (Decreto 1990/2016 art. 1): «El valor de los aportes liquidados **por cada cotizante** … deberá aproximarse al múltiplo de 100 superior más cercano». AT2 v30 campo 47: «multiplicando el valor del campo 42 – "IBC Pensión" … por el valor del campo 46 – "Tarifa de aportes a pensiones"», **um** valor por cotizante e fundo, arredondado uma vez | **Desenho certo.** O total do cálculo independente (280.300) não é o que a PILA liquida (280.200). No tipo 51, o desenho agora dá 210.109, igual ao campo 47 |
| **198 na retenção** (6 linhas × 29 casos + 14 + 14 valores retidos) | C23: 16.855.321 (desenho) × 16.855.453 (cálculo indep.). A diferença vem só da INCRNGO, que no desenho soma ≈ 237,50 a mais por mês (4% 1.750.905 → 1.751.000; 4%; FSP 218.863,125 → 218.900; 656.589,375 → 656.600) | ET art. 55: «Los aportes obligatorios **que efectúen los trabajadores** … no harán parte de la base para aplicar la retención en la fuente». ET art. 56: o mesmo texto para saúde. DUR 1.2.4.1.6, caput: «podrán detraerse **los pagos efectivamente realizados** por los siguientes conceptos», nums. 2 e 3.1 | **Desenho certo.** O empregado tem descontado o valor arredondado (58121 = 70.100, e o cálculo independente desconta o mesmo, pois `salud_trab` não diverge). A INCRNGO é esse valor. O cálculo independente subtrai o valor antes do arredondamento, o que é incoerente com o próprio desconto |
| **10 antigas** | I03/I04 (6, piso C-543) e C23 (4, centavo) | (rodada 1) | desenho certo (rodada 1) |
| **Erro dos dois lados** | os dois arredondam a parte do empregado **para cima** em COP 100 (70.036,20 → 70.100) | Lei 100 arts. 20 e 204 fixam 4%. A regra de arredondamento do Decreto 780 é para o aporte **por cotizante e fundo** (o total), não para a parte do empregado | Nem o Decreto 780 nem o AT2 dizem como dividir o total. Arredondar a parte EE para cima cobra do trabalhador até COP 99 acima dos 4% por fundo. O A2 declara isso (85%). Ver n1 |

Conclusão: as 228 diferenças novas **não são defeito do desenho**. O cálculo independente (`oracle_v2.py`) deveria ser ajustado nos dois pontos para voltar a ser referência: total por fundo e INCRNGO descontada. Isso é fora deste design.

## 3) Regressões
- **Ordem:** 0 defeitos (o meu verificador e o do construtor). As únicas leituras na mesma ordinal são as da S17 (n2).
- **WTC × matrizes:** 405/405, 0 divergências. Coluna O coerente com N (N = Yes ↔ O = Yes em todas as 263).
- **Constantes:** sem mudança. SMMLV 1.750.905, UVT 52.374, auxílio 249.095, divisor 220/210 e adicional 0,80/0,90 por data, 18 semanas. Tabela do art. 383 igual.
- **Probes repetidos da rodada 1, todos certos:**
  - CCG 8.000.000 → 92.049,30;
  - 114-1: 17.509.050 → não exonera (8,5% = 1.488.300; SENA 350.200); 17.509.049 → exonera;
  - auxílio de transporte em 2 SMMLV e em 2 SMMLV + 1;
  - FSP 33.000.000 → 165.000 + 363.000;
  - aprendiz em aula: saúde EE 70.100 sobre 1 SMMLV, ARL 9.200;
  - não residente 20% sobre a coluna P: 10.000.000 + prima 2.000.000 → 2.400.000, cesantía fora.
- **Variante v1_2:** ordem 47, 34 diferenças, varredura 18 (12 da coluna P, 6 do roteamento).

## Achados novos
| ID | Sev. | Local | Evidência | Correção | Rota |
|---|---|---|---|---|---|
| n1 | minor | `_build_v2.py` `UP100` nas bandas EE (58121, 58122, 58123, 58124); `ASSUMPTIONS.md` A2 | A parte EE é arredondada **para cima** em COP 100, e o total por fundo uma vez. A Lei 100 (arts. 20 e 204) dá 4%. O Decreto 780 art. 3.2.1.5 num. 2 arredonda o aporte «por cada cotizante» (o total do fundo). Nenhuma fonte lida manda arredondar a parte do empregado. O cálculo independente faz o mesmo, então é erro dos dois lados. O A2 declara, a 85% | Ou EE = `ROUND` ao peso (4% exatos ao peso) e ER = ⌈total⌉₁₀₀ − EE, o que mantém o total da PILA e não cobra arredondamento do trabalhador; ou manter e escrever no A2 que é convenção, sem fonte, com o efeito «até COP 99 por fundo a cargo do empregado». A INCRNGO (A9) acompanha a escolha | builder |
| n2 | minor | 9170056, 9170057, 9170064 (banda ER: `ER_REST`, `…$58121_raw…$58121`); `co_engine.py` S17 | A banda ER lê a conta e o `_raw` da banda EE **da mesma regulação**. No `td.json` do Dev não há nenhuma banda que leia outra banda da própria regulação; as quatro bandas da CNPS leem só `$band_amount_raw`. Se o motor real avaliar as bandas sobre o estado de entrada, `$58121` vale 0 e a parte patronal vira o total inteiro (saúde 218.900 em vez de 148.800). A S17 está entre as premissas, mas a correção do Q4 depende dela | Escrever a banda ER sem ler a banda irmã, usando a base da regulação. Saúde: `SUBTRACT(MULTIPLY(CEILING(DIVIDE(MULTIPLY($58106;0.125);100);1);100);MULTIPLY(CEILING(DIVIDE(MULTIPLY($58106;0.04);100);1);100))`; análogo na pensão com `ADD(4;$52516)` e no tipo 51. Ou pôr a S17 na lista de aceite do motor como bloqueante | builder |
| n3 | minor | `CO_Taxability_Matrices_v2_0.md:8–22` (tabela "Consumed by") e `:125` | A tabela cita os IDs do **v1_2**: N → `9170051`, `9170061`–`9170065`; P → `9170063`; W → `9170081`–`9170084`; X → `9170085`, `9170086`; T → `9170023`, `9170044`–`9170046`. No v2, esses IDs são outras regulações (9170063 = ICBF; 9170085 = imposto do Proc. 1; 9170086 = retenção Proc. 1; 9170023 = juros de cesantías). O certo seria N → 9170072/9170073; P → 9170132; W → 9170020; X → 9170014; Q → 9170045; T → 9170047; U → 9170049; R → 9170050; S → 9170051; V → 9170041/9170042. **Já estava na rodada 1 e eu não peguei** (o gerador é cópia do v1_2). O título «🔴 Structural finding» também ficou | Regenerar a tabela com os IDs do v2 (o `gen_matrices.py` pode ler o JSON) | builder |
| n4 | minor | `CHANGELOG.md:15–20` («## Round 2 (independent review…)», «Round 1 left it out», «Q1…m9»); linhas da tabela com «(Q4)», «(m4)», «(m5)», «new (Q1)»; `ASSUMPTIONS.md:42` («Decided in round 2»); `VALIDATION.md:140–162` («[Q4]», «X12 Q1», «X16 m9») | O pacote vai ao Dev, e a regra é não ter rodadas nem códigos de revisão internos | Trocar por descrição do conteúdo, por exemplo "## Changes after the independent review", e citar os itens pelo assunto (Procedure 2 service bonus, retirement bonus, …); nos casos, X12–X20 sem o código de achado | builder (direto) |
| n5 | minor | `CO_Regulation_Design_v2_0.md:755` («with R320, R339, R343, R344 false … 257 rows true, 41 false»); `CHANGELOG.md:10` (defeito 4: «read by `9170087`–`9170090`»); `CHANGELOG.md` itens 7 antes do 6; `ASSUMPTIONS.md` A9/A10 antes de A3 | A contagem 257/41 já inclui R340 e R345, mas o texto lista só quatro linhas. No v2, o defeito 4 é lido por 9170089–9170093 (9170087 é a retenção do Proc. 2). A numeração fora de ordem é só cosmética | Listar R320, R339, R340, R343, R344 e R345; corrigir os IDs; reordenar | builder (direto) |

## 4) Conferido e aprovado
- Reprodução bit a bit (md5) dos 4 produtos; 20/20 conferências; varredura 0; coluna O 0; troca EE/ER detectada.
- Q1, Q2, Q3, Q5 e m9 refeitos à mão pela lei (tabela do §1), todos iguais ao motor.
- Forma do Dev na Q4: EE em `employeeRate` e ER em `employerRate`/`employerRateAccount` na mesma regulação, como na «TD CNPS Contribution EE and ER». A 9170132 tem o nome, ordinal, taxGroup, taxRuleGroup, taxationType e assertion (`$64552`) do Dev.
- `retro_`: 54 regulações SS com «Deliberate divergence (law)» e fonte (AT2 v30, tipo N); 25 regulações de IR sem `retro_`, como o Dev.
- As 238 diferenças estão classificadas com fonte (§2). As 12 da variante "parcelas" são as mesmas da rodada 1, menos L15/L21, que agora batem no total.
- RESEARCH_GAPS: R7 com o teste dos 204 UVT sobre o salário, R8 com R340 roteada, R2 ampliado, R12/R13 (os dois "fora do pedido" da rodada 1), tudo coerente com o JSON. ASSUMPTIONS A2/A9/A10 coerentes com o JSON (ver n1).
- Pacote em inglês sem pipeline, agent, oracle, COVAL, Claude, provider, Drive ou nome de cliente. As exceções de rodada estão no n4.

## Próximo passo
Rodada 3 é opcional (os 5 minors não bloqueiam): n1 e n2 pedem decisão de forma (recomendo a fórmula sem leitura de banda irmã e EE ao peso); n3–n5 são texto. Fora do design: ajustar o `oracle_v2.py` (total por fundo e INCRNGO descontada) para que volte a ser referência.

| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | QA independente (frente validacaoco) | rodada 1: FAIL (0/5/9), em `QA-REVIEW-r1.md` |
| 2026-11-02 | QA independente (frente validacaoco) | rodada 2: **PASS** (0 blocker, 0 major, 5 minor); Q1–Q5 e m1–m9 fechados por probe e conta à mão; 238 diferenças julgadas pela fonte (desenho certo; EE arredondado para cima sem fonte nos dois lados) |

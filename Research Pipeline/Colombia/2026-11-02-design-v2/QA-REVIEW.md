# Colômbia — design v2.0: revisão independente de QA (rodada 3, confirmação final)

> Hub: [[Colombia]] · Revisado: [[Research Pipeline/Colombia/2026-11-02-design-v2/CONFERENCIA|CONFERENCIA do v2.0]] (seção "Rodada 3") · Rodadas anteriores: [[Research Pipeline/Colombia/2026-11-02-design-v2/QA-REVIEW-r1|r1]] (FAIL 0/5/9), [[Research Pipeline/Colombia/2026-11-02-design-v2/QA-REVIEW-r2|r2]] (PASS 0/0/5)
> Revisor: QA adversarial independente (não construiu o v2.0). Data: 2026-11-02. Modo: **só leitura**. Este é o único arquivo gravado na pasta.

## Veredito: **PASS** (0 blocker, 0 major, 0 minor)

Os 5 minors da rodada 2 (n1–n5) estão fechados. A cópia do cálculo independente muda **só** as duas convenções de arredondamento, e as 6 diferenças restantes são todas do piso da C-543 (I03/I04), em que o desenho segue a lei. Não há regressão.

O PASS vale para o **design local**. Continuam fora do artefato:
- o aceite da semântica no motor real (S1–S18, `CEILING`, `DAYS360`, leituras de histórico R3);
- o split das 21 linhas `Yes/No` (R1/R2);
- a regra 9: Colômbia ativa exige ticket ao Development antes de levar à produção.

## Como conferi
- **Reexecução:** a pasta da rodada 3 foi copiada para o scratchpad (junction só de leitura para `2026-10-29-validacao-research`). Antes, confirmei que o script grava só dentro da própria pasta (`_build_v2.py:830, 884–891`). `python -I -B _build_v2.py`: rc 0.
  - Os 4 produtos são **idênticos** (md5) aos da pasta: `co_design_v2.json` `e029d8b9…`, `VALIDATION-run.txt` `6c7d8440…`, `SWEEP-run.txt` `56d661e4…` e `_run-summary.json` `2cc00741…`.
  - Resultados da execução:

    | Checagem | Resultado |
    |---|---|
    | regulações | 79 |
    | ordem | 0 |
    | convenção antiga (parcelas) | 12 diferenças |
    | contra o cálculo independente original | 293 diferenças |
    | **contra a cópia ajustada** | **6 diferenças** |
    | X1–X20 | 20/20 |
    | varredura | 2.682 checagens, 0 diferenças |
    | coluna O | 0 |
    | codificação EE/ER | 0 erros, e a cópia trocada dá 1 erro |
- **Meu verificador de ordem**, estrito, que conta também leituras dentro da mesma regulação: **0** leituras de conta lançada na mesma ordinal ou depois. As 6 leituras de banda irmã que apontei na rodada 2 sumiram. IDs = 9170000 + ordinal nas 79; sem duplicatas.
- **WTC v1.9:** 405 linhas contra as 9 matrizes (14 X, 20 W, 45 Q, 47 T, 49 U, 50 R, 51 S, 72 N roteada, 132 P): **0 divergências**. Coluna O coerente com N.
- **Constantes e tabela do art. 383:** o bloco `CONST` e a `TABLE` são idênticos aos da rodada 1 (diff vazio).
- **`co_engine.py`:** contra a rodada 2, muda só o texto da S17 (diff ignorando o fim de linha). O motor não mudou.

## 1) n1–n5: situação
| ID | Situação | Prova |
|---|---|---|
| n1 | ✅ fechado | **Parte do empregado ao peso:** 58121 = `ROUND($band_amount_raw)` e 58122 = `ROUND(...)`. **Patronal:** ⌈total do fundo⌉₁₀₀ − `ROUND(4%)`. Quando a saúde é exonerada, o empregado paga o fundo inteiro e o EE leva o arredondamento: `IF(GREATER($58215;1);ROUND;CEILING100)`. A FSP (58123/58124) fica em ⌈⌉₁₀₀.<br>**Fontes:** Decreto 780 art. 3.2.1.5 num. 2 (Decreto 1990/2016 art. 1): «El valor de los aportes liquidados por cada cotizante … múltiplo de 100 superior». AT2 v30 campo 47 (pensão = IBC × tarifa) e campo 55 (cotização de saúde): **um** valor por fundo. AT2 v30 campo 51 (FSP solidaridad): «multiplicar … "42 – IBC Pensión" … por 0.5% … El valor incluido en este campo debe cumplir las reglas de redondeo». Como a FSP e a saúde exonerada não têm parte patronal, o valor arredondado da PILA é o próprio desconto do empregado. **Confirmado.** A divisão do total entre empregado e empregador não está regulada; o A2 diz isso (92%).<br>**Probes:**<br>• 1 SMMLV não exonerado: EE 70.036 + ER 148.864 = 218.900 = ⌈218.863,125⌉₁₀₀; pensão 70.036 + 210.164 = 280.200 = ⌈280.144,80⌉₁₀₀; INCRNGO 140.072.<br>• 1 SMMLV exonerado: saúde EE 70.100 (fundo inteiro), sem ER.<br>• 9.000.000: 360.000 / 360.000 / 45.000 / 45.000, INCRNGO 810.000.<br>• Alto risco 33.000.000: 1.320.000 + 7.260.000 = 26%.<br>• Tipo 51, 15 dias: 52.527 + 157.582 = 210.109, igual ao campo 47 |
| n2 | ✅ fechado | Bandas patronais escritas a partir da base, sem ler a banda irmã:<br>• 58141: `⌈$58106 × 0,125⌉₁₀₀ − ROUND($58106 × 0,04)`;<br>• 58142: `⌈$58112 × (4 + $52516)/100⌉₁₀₀ − ROUND($58112 × 0,04)`;<br>• 58137: `ROUND($58197 × 0,16) − ROUND($58197 × 0,04)`.<br>`$58106`, `$58112` e `$58197` são lançadas nas ordinais 45, 49 e 52, antes. Meu verificador estrito dá 0. Parte patronal em `employerRate`/`employerRateAccount` e parte do empregado em `employeeRate`, como na «TD CNPS Contribution EE and ER» do Dev. A troca EE/ER continua sendo pega (1 erro na cópia) |
| n3 | ✅ fechado | "Consumed by" das Matrizes com os IDs do v2:<br>• N → 9170072 (com R320, R339, R340, R343, R344, R345 false) e 9170073;<br>• P → 9170132; Q → 9170045/56; R → 9170050/58/59; S → 9170051/60;<br>• T → 9170047, 9170061–63; U → 9170049/57;<br>• W → 9170020–23; X → 9170014–19; V → 9170041/42.<br>Todos conferidos contra o JSON. Sem «🔴» |
| n4 | ✅ fechado | A varredura do pacote em inglês não acha pipeline, agent, oracle, COVAL, Claude, fork, provider, Drive, «round N», nem códigos Q/m/n entre parênteses ou entre colchetes. Os títulos ficaram «## Changes after the independent review» (CHANGELOG) e «revised after the independent review» (Memo l. 209), referência neutra e aceitável. Os casos X12–X20 aparecem só pelo assunto, e o A2 não fala mais em "round" |
| n5 | ✅ fechado | Regulation_Design l. 755: «R320, R339, R340, R343, R344, R345 false … 257 rows true, 41 false», igual ao JSON. CHANGELOG defeito 4: «read by `9170089`–`9170093`; under Procedure 2 … `9170073`». Itens 4–7 em ordem; A1–A10 em ordem |

## 2) Cópia do cálculo independente (`oracle_r3/oracle_v2_r3.py`)
- **Original intacto:** `oracle/oracle_v2.py`, md5 `c09f0e6f…`, igual ao citado na CONFERENCIA.
- **Diff contra o original.** Fora o cabeçalho de comentário, há só três blocos:
  1. depois do arredondamento por subsistema: se não exonera, `salud_trab = peso(raw)` e `salud_emp = ceil100(trab + emp) − trab`; sempre, `pension_trab = peso(raw)` e `pension_emp = ceil100(trab + emp) − trab` (convenção R3-1);
  2. `incrngo` passa a somar os valores descontados (`o[...]`) em vez dos `raw` (convenção R3-2);
  3. no tipo 51, `pension_emp = tot − pension_trab` em vez do 12% arredondado à parte (R3-1, campo 47).
- **`params.json`:** idêntico ao original (diff vazio depois de normalizar o JSON).
- Nenhuma outra regra mudou (tabela, tetos, pisos, prestações, incapacidade, rescisão, tipo 51 fora da pensão).
- **As 6 diferenças restantes** são I03 (dias 91–180 = 583.635 contra 500.000; total e IBC) e I04 (5.252.715 contra 4.500.000; total 11.252.715; IBC 11.252.715 contra 10.505.430). É **só** o piso da C-543, em que o desenho está certo pela parte resolutiva («no podrá ser inferior al salario mínimo legal vigente»). Também sumiram o centavo do C23 e o peso de L15/L21.

## 3) Regressões (probes meus)
| Ponto | Resultado |
|---|---|
| CCG 8.000.000 | 92.049,30 ✅ |
| Proc. 2 + prima 5.000.000 | 1.057.500 ✅ |
| Contribuições | n1 acima ✅ |
| X1–X20 (incluem Q2, Q3, Q5, m9, m5) | 20/20 ✅ |

Os probes de Q2/Q3/Q5/m9/114-1/não residente da rodada 2 não dependem do arredondamento das contribuições, a não ser pela INCRNGO. O X12 (1.057.500) e o X15 (341.250) continuam exatos porque o IBC deles é múltiplo de 25 e as contribuições são exatas.

## Observação (não é achado)
Na 58141, o 0,125 e o 0,04 estão escritos dentro da fórmula, e o `employerRate` 8,5 fica só para a forma (o `$band_amount_raw` da banda patronal não é usado). Se a alíquota mudar, há dois lugares para atualizar. A pensão já lê `$52516`. Sugestão para uma versão futura: ler a alíquota de uma conta, como o 52516.

## 4) Conferido e aprovado
- Reprodução bit a bit (md5) dos 4 produtos. Ordem 0 no verificador estrito. 405 linhas × 9 matrizes sem divergência. Constantes e tabela iguais à rodada 1.
- n1–n5 fechados, com a fonte primária relida para o n1 (Decreto 780 art. 3.2.1.5 num. 2; AT2 v30 campos 47, 51 e 55).
- Cópia do cálculo independente limitada às duas convenções. As 6 diferenças restantes são só C-543.
- Pacote em inglês sem referências internas. CHANGELOG, ASSUMPTIONS (A1–A10, S17 reescrita) e RESEARCH_GAPS (R1–R13) coerentes com o JSON.
- Os achados das rodadas 1 e 2 (Q1–Q5, m1–m9, n1–n5) estão todos fechados.

| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | QA independente (frente validacaoco) | rodada 1: FAIL (0/5/9), em `QA-REVIEW-r1.md` |
| 2026-11-02 | QA independente (frente validacaoco) | rodada 2: PASS (0/0/5), em `QA-REVIEW-r2.md` |
| 2026-11-02 | QA independente (frente validacaoco) | rodada 3 (final): **PASS (0/0/0)**; n1–n5 fechados; cópia do cálculo independente só com as duas convenções; 6 diferenças restantes = C-543 |

# Chade — design v6: revisão independente de QA (rodada 1)

> Hub: [[Chade]] · Revisado: [[CONFERENCIA]] (v6) · Base aprovada: [[2026-11-01-design-v5/QA-REVIEW|QA do v5]] (PASS na rodada 3)
> Revisor: compliance-qa-auditor (instância independente; não construiu o v6). Data: 2026-11-02. Modo: **só leitura**. Este é o único arquivo gravado.

## Veredito: **FAIL** (0 blocker, 2 major, 4 minor)

A forma do Dev foi aplicada com fidelidade, e nenhum erro do Dev foi copiado. Os valores estatutários são os mesmos do v5 que eu aprovei. Dois pontos impedem o PASS: (1) um defeito de matriz que já estava no v5 e que eu não peguei, que o Dev não tem e que o v6 não copiou do Dev; (2) a retirada de todo `retro_`, que muda comportamento sem avaliação e contradiz o ASSUMPTIONS.

## Como conferi
- **Reexecução:** `_build_v6.py` copiado para o scratchpad, junto com o `_build_v5.py` (md5 `87089bcc…`, o mesmo que aprovei na rodada 3 do v5). `python -I -B`: rc 0; 12/12 e 20/20 exatos; "1.152 valores, 0 diferenças" contra o v5. `SKILL.md` gerado **idêntico** ao da pasta.
- **Dev:** `td.json` (Drive `Chad/07-design`, md5 `bb62f014…`, 31 regulações), comparado **regulação a regulação nas 30 que têm par** (não por amostra): nome, ordinal, taxGroup, taxRuleGroup, taxationType, assertion, cada banda (contas, taxas, fórmula, assertion, piso/teto, faixas) e a matriz inteira.
- **Probes no motor do v6:** a cadeia do IRPP conta a conta, um isento, salário zero e um código de arrears de benefício.

## 1) Nenhuma mudança de valor estatutário em relação ao v5
Taxas, tetos, pisos, faixas, 15%, 30%, 5.000/filho, 3,5%, BIK %, 75.000, PSA 400 e CNPS 3,5/5/7,5/4, 60.000/500.000: os mesmos do v5 (`_build_v6.py:21–25`, 172–296). Refeitos à mão:

| # | Conta | CNPS EE | IRPP | TFE | TAFP | Líquido | v6 |
|---|---|---|---|---|---|---|---|
| 1 | 337.750×12 = 4.053.000 → (−800.000)×10,5% = 341.565/12 = 28.463,75 | 12.250 | 28.464 | 26.250 | 4.200 | 308.886 | = |
| 4 | moradia MIN(50.000; 600.000×0,20 = 120.000) = 50.000; 58008 = 650.000; CNPS 500.000 teto; 632.500×12 → 789.000/12 | 17.500 | 65.750 | 48.750 | 7.800 | 516.350 | = |
| 7 | transporte MIN(120.000; 58103 = 90.000); 319.500×12 = 3.834.000 → 318.570/12 = 26.547,5 → 26.548 | 10.500 | 26.548 | 31.500 | 5.040 | 382.552 | = |
| 11 | 58552 782.500 → 58110 9.390.000 → 58111 546.000+225.000+300.000+97.500 = 1.168.500 → 58112 97.375 → 2592 | 17.500 | 97.375 | 60.000 | 9.600 | 684.725 | = |
| E1 | 58107 = MAX(30.000 − 7.300; 0) = 22.700; MIN(30.000; 22.700); 296.800×12 → 289.968/12 | 10.500 | 24.164 | 24.750 | 3.960 | 294.936 | = |
| E4 | MIN(101.000; 401.000×0,15 = 60.150); 330.350×12 → 332.241/12 = 27.686,75; TAFP 401.000 → 4.812 → 4.810 | 10.500 | 27.687 | 30.075 | 4.810 | 362.413 | = |
| E8 | MIN(200.000; 150.100); 339.400×12 → 343.644/12 = 28.637 | 10.500 | 28.637 | 37.500 | 6.000 | 460.463 | = |

PSA 400 em todos. As contas do motor no S11 conferem: 58110 = 9.390.000, 58111 = 1.168.500, 58112 = 97.375, 2552 = 0.

## 2) O que o v6 diz copiar do Dev bate com o `td.json`? (30 de 30 pares conferidos)
- **Nome, ordinal, taxGroup e taxationType:** iguais nos 30 pares. **taxRuleGroup:** igual em 28; diferem só 9148181 e 9148261, como declarado. ✅
- **Iguais ao Dev, banda e fórmula:** 9148201 e 9148221 (idênticas por completo); 9148021, 9148031 (`MIN($band_amount_raw;$58103)`), 9148033 (`MIN(…;$58107)`), 9148141 (truncamento a 1.000), 9148151, 9148155, 9148161 (piso 720.000 / teto 6.000.000), 9148191 e 9148231 (`FLOOR(ADD(x;0.5))`). Nessas, as diferenças estão só nas matrizes, nos pré-requisitos e nas assertions de banda declarados como divergência de lei. ✅
- **Diferenças não declaradas:** nenhuma, exceto as do item 3. A 9148171 tem a mesma ordem de bandas do Dev (3,5 EE · 7,5 PFM · 4 · 5 · 3,5 dedução · 20), com as contas corrigidas. ✅
- **9148009:** a matriz agora são os códigos de pagamento (a mesma do 58105), sem ler o 58105 antes do ordinal 10. ✅ Correção certa. A matriz do Dev inclui `65%%%` (espécie) e `626%%` (pensões); o v6 não copiou, coerente com o art. 46-I/II.

## 3) Erros do Dev que o v6 não copiou (todos conferidos no `td.json`)
| Erro do Dev | Dev (`td.json`) | v6 |
|---|---|---|
| Inversão das contas da CNPS | 3,5% EE em 6020/2550; 7,5% PFM em 2610/2551 | EE 2610/2551, PFM 6020/2550 ✅ |
| Piso da CNPS com salário zero | 9148161 só `NOT(EQUALS($58218;4))` | `AND(…;GREATER($58130;0))` ✅ |
| 18% para não residente | 9148241 `employeeRate 18` sobre 58592 | 100% de 58112 (tabela) ✅ |
| Indenização fora do IRPP | 9148131 `6218%` No | 621%% em 58105 → 58008; só o plano social sai (9148034) ✅ |
| BIK por forfait | `MULTIPLY($58105;0.20)` | `MIN(real; MULTIPLY($58105;0.20))` ✅ |
| Aposentadoria voluntária dedutível, sem teto | 9148181 `2164%` Yes, sem MIN | `2164%` No, `MIN(…;$58172)` ✅ |
| Base da TF/TA sem transporte isento, 6276x, bolsa e seguro-saúde | 58104 Yes, 6276%/6580%/6563% No em 141/151 | base bruta ✅ |
| TF/TA lançadas como taxa do **empregado** | 9148251 e 9148261 `employeeRate` 1,2 / 7,5 | `employerRate` ✅ |
| Teto do abono por dependente e sem a CNPS | `MULTIPLY(5000;$58212)` | `MAX(5000×filhos − 58213; 0)` ✅ |
| Faixas `x.99` | 800.000,99… | limites redondos ✅ |

## 4) Cadeia nova do IRPP (191 → 201 → 211 → 221 → 231/241)
191 (58552) → 201 (`×$period_divisor` → 58110) → 211 (`simple_tax_monthly`, diferencial, faixas sem divisão → 58111) → 221 (`÷$period_divisor` → 58112) → 231/241 (`FLOOR(x+0,5)` → 2552/2592). Ordinais em ordem; equivale à 9148072 do v5 (S11 conta a conta acima). O arredondamento fica só no fim. ✅ Ver m1 sobre o 58112 de quem é isento.

## Achados
| ID | Sev. | Local | Evidência | Correção | Rota |
|---|---|---|---|---|---|
| V1 | **major** | `_build_v6.py:110` (BIK veículo: `6550%` + `65520`); `_build_v6.py:84–86` (`BIK_REAL`); 9148131 | WTC V3.0: 65521 « Arrears – Car Fuel Benefit », 65522 « Adjustment – Car Fuel Benefit », 65523 « Addition – Car Fuel Benefit ». O v6 só pega 65520. Probe com 300.000 + 65521 de 50.000: 58121 = 0, 58008 = 300.000, 58563 = 58534 = 300.000. Ou seja, **fora do IRPP, da TF e da TA** (só a CNPS pega, por `655%%`): IRPP 23.214, quando seria ≈ 26.364. O Dev usa `6552%`. O defeito **já estava no v5** (mesmo probe no `_build_v5.py`, mesmo resultado) e passou nas minhas três rodadas do v5 | Trocar `('65520','','Yes')` por `('65529','6552%','Yes')` na BIK de veículo e no `BIK_REAL` (forma do Dev). Acrescentar um extra com 65521 | builder |
| V2 | **major** | `CHANGELOG.md:9` ("The retro_ rule groups of v4/v5 dropped (the Dev uses none)") × `ASSUMPTIONS.md:24` (A11 "`retro_` scope: v4 scope + 9148022, 9148024, 9148025 · Rule as stated on 16 Oct") | O v6 retira todo `retro_` (v5: 9148013–9148025, 9148031–39, 9148061, 9148072). Isso é mudança de **comportamento** em recálculo retroativo (limites, tetos de BIK e o 3,5%), e o motor local não exerce isso. Por isso "No value changes" só vale para os 32 casos sem retro. O A11 ainda descreve o escopo `retro_` do v5 com IDs que não existem no v6 | Decidir com base no material de 16/10, que pedia `retro_`: ou repor `retro_` onde o v5 tinha, ou reescrever o A11 ("v6 sem retro_, como o Dev; efeito em pagamento retroativo não testado") e pôr o ponto na lista do aceite do motor | builder |
| m1 | minor | `_build_v6.py:228–236` (9148211 sem pré-requisito; 201/221 só `NOT_DIPLO`); `_build_v6.py:458–460` (`KEYS`) | Para isento (deficiente, jovem graduado do 3-4°), o v6 grava 58110 = 4.053.000, 58111 = 341.565 e **58112 = 28.463,75** (probe S10). No v5, a 9148072 tinha o `SCALE` como pré-requisito, e o valor era 0. O passivo 2552 fica certo (0). A comparação "0 diferenças" não pega isso porque `KEYS` não tem 58110–58112 nem 58103/58172 | Pôr `SCALE` como pré-requisito na 9148201 (ou confirmar que nenhum relatório lê o 58112) e acrescentar 58103, 58110, 58111, 58112 e 58172 ao `KEYS` | builder |
| m2 | minor | `ASSUMPTIONS.md:3, 23, 25`; `RESEARCH_GAPS.md:3, 23, 35` | O cabeçalho diz que os nomes seguem o v6, mas A10 ainda lista 58173 e 58161–58169 como contas-teto; A12 cita 9148053/073/075/091; R15 cita 9148024; R27 pede a criação de 58109, 58161–58169 e 58173, que o v6 não usa mais | Trocar para os IDs/contas do v6 (A10: 58103, 58107, 58172, 58223 e os MIN nas fórmulas; A12: 9148171, 9148231, 9148241, 9148271; R15: 9148035; R27 sem as contas retiradas) | builder (direto) |
| m3 | minor | `_build_v6.py:36–38` (58205 = `CEIL(MULTIPLY(YEARS_BETWEEN(início;fim do período);12))`) | Fórmula do Dev; YEARS_BETWEEN devolve decimal (KB de fórmulas: "Years (decimal)", 7,23). Com início igual ao fim do período (contratação no último dia do mês), o resultado é 0, e com o `GREATER($58205;0)` do v5 o empregado **perde a isenção no 1º mês**. A fórmula do v5 (`FLOOR(DIAS/30,4375)+1`) dava 1. Os casos de validação recebem o 58205 pronto, então não testam a fórmula | Aceitar com nota no A13, ou usar `ADD(CEIL(…);0)` com piso 1 quando a data existe. Testar no aceite do motor | builder |
| m4 | minor | `_build_v6.py:155–160` (9148009 sem pré-requisito) | No motor real, o piso pode valer com base vazia (S4 do Dev, conversa de 16/10). Nesse caso o 58106 fica 60.000 para quem não recebeu. É o mesmo comportamento do Dev, e só afeta relatório | Pré-requisito `GREATER(...)` não é possível (o 58105 ainda não existe); anotar no A16 como ponto do aceite | builder |

## 5) Marcas e referências
`SKILL.md`: 0 marcas ⚠️/PENDENTE/A CONFIRMAR/TODO/TBD; 36 regulações. As referências da tabela v5 → v6 do CHANGELOG apontam IDs do v5 de propósito (coluna "v5 source"), o que está certo. As referências velhas no ASSUMPTIONS e no RESEARCH_GAPS estão no m2. O caminho `V5_BUILD` (`_build_v6.py:17`) depende da pasta irmã do v5 (só leitura), o que está correto.

## Próximo passo
Rodada 2 com o builder: V1, V2, m1–m4. Como o V1 também está no v5, registrar no CONFERENCIA do v5 que o defeito foi achado depois do PASS e corrigir também lá, se o v5 continuar como referência. Teto: 3 rodadas.

| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | QA independente (frente Chade) | revisão do v6, rodada 1: FAIL (0 blocker, 2 major, 4 minor); forma do Dev conferida nas 30 regulações com par; nenhum erro do Dev copiado |
| 2026-11-02 | QA independente (frente Chade) | v6 rodada 2: FAIL (0 blocker, 1 major, 3 minor); V1, V2, m1–m4 fechados; varredura de todos os códigos Earning da WTC |

---

# Rodada 2 (2026-11-02, depois da "v6 r2" do construtor)

## Veredito: **FAIL** (0 blocker, 1 major, 3 minor; todos novos)

Os achados V1, V2 e m1–m4 da rodada 1 estão fechados. As séries pedidas (6552%, 6267%/6268%, 6291–6293%, 62909) conferem com a WTC V3.0. Mas a varredura de **todos** os códigos Earning da WTC pelo motor do v6 achou mais duas séries fora de todas as bases (W1). É o mesmo tipo de defeito do V1, e o A35 diz que as séries foram "checked series by series". Esta é a rodada 2 de 3.

## Como conferi
- Diff entre o `_build_v6.py` da rodada 1 e o atual: muda a BIK de veículo, o `BIK_REAL`, a 9148131, o `CNPS_GROSS`, o pré-requisito da 9148201, o `KEYS`, os casos E21/E22 e o `retro_effect()`. Reexecução no scratchpad: rc 0; 12/12 e 22/22 exatos; "1.386 valores, 0 diferenças inesperadas"; as únicas diferenças v5 → v6 são as 9 contas do E21. `SKILL.md` e `VALIDATION-run.txt` idênticos aos da pasta. 0 marcas.
- **Varredura completa:** cada código `Earning` da WTC V3.0 passou pelo motor do v6 (300.000 + código 10.000), com a variação de 58008, 58130, 58534 e 58563 comparada às colunas Tax/CNPS/TA/TF da WTC. Toda divergência foi conferida contra as decisões documentadas (R18, R19, A20, A30, A35, D1).
- Planilha `2026-11-02-planilha-comparacao/TD_Design_Comparison_v4_v5_v6_vs_Dev.xlsx`: fórmulas e valores em cache lidos com openpyxl, e recontados à mão.

## Refeitos à mão
| # | Conta | CNPS EE | IRPP | TFE | TAFP | Líquido | v6 |
|---|---|---|---|---|---|---|---|
| E21 | 300.000 + 65521 50.000: veículo MIN(50.000; 10% × 300.000 = 30.000) → 58008 330.000; CNPS 350.000 (655%%); 317.750×12 = 3.813.000 → 316.365/12 = 26.363,75; TF/TA no valor real 350.000 | 12.250 | 26.364 | 26.250 | 4.200 | 260.986 | = |
| E22 | 450.000 + arrears 62101 100.000, pagos no mês: CNPS teto 500.000; 532.500×12 = 6.390.000 → 546.000 + 58.500 = 604.500/12; TF 550.000 × 7,5%; TA 550.000 → 6.600 | 17.500 | 50.375 | 41.250 | 6.600 | 481.725 | = |
| 10 | jovem graduado isento: 58552 = 337.750, **58110 = 58111 = 58112 = 0** (SCALE na 9148201), 2552 = 0 | 12.250 | 0 | 0 | 0 | 337.350 | = |
| 11 | 58110 9.390.000 → 58111 1.168.500 → 58112 97.375 → 2592 | 17.500 | 97.375 | 60.000 | 9.600 | 684.725 | = |

Efeito do `retro_` no A11, refeito à mão. Pagamento único de 1.000.000 → IRPP 147.375. Reprocessando o mês original, o IRPP sobe 10.132 (400.000 dá 33.530 contra 23.398 dos 300.000 originais), e o mês corrente de 900.000 dá 122.375: total 132.507. Na CNPS EE, o pagamento único dá 17.500; reprocessando, 14.000 − 10.500 + 17.500 = 21.000. Bate com o VALIDATION.

## Achados da rodada 1: situação
| ID | Situação | Evidência |
|---|---|---|
| V1 | ✅ fechado | `6552%` na BIK de veículo e no `BIK_REAL` (`_build_v6.py:84, 106`); E21 |
| V2 | ✅ fechado | A11 reescrito: v6 sem `retro_` por decisão, com base no guia p. 7 (« quelle que soit la période ») e no art. 189-1° (« sans qu'il y ait lieu de distinguer la période »). Efeito medido (147.375 × 132.507; 17.500 × 21.000), 70% no IRPP, a confirmar no motor |
| m1 | ✅ fechado | 9148201 com `SCALE` (`_build_v6.py:228`): 58110–58112 = 0 para isento (probe S10 e deficiente); `KEYS` com 58103, 58112 e 58172, e checagem de 58110/58111 |
| m2 | ✅ fechado | A10 e A12, R15 → 9148035, R27 sem 58109/58161–58169/58173; cabeçalhos atualizados |
| m3 | ✅ aceito | A13: o 1º mês de quem é contratado no último dia fica tributado; o piso de 1 foi recusado com razão (data vazia tem de continuar sem isenção) |
| m4 | ✅ aceito | A16: ponto do aceite do motor |

## Regressões pedidas
| Ponto | Resultado |
|---|---|
| 6552% | 65520–65523 « Car Fuel Benefit » (Tax No / CNPS, TA, TF Yes na V3.0) → IRPP capado, TF/TA/CNPS no real ✅ |
| 6267% / 6268% | 62670–62671 « Benefits plan 1 », 62680–62689 « Benefits plan 2 »: todos Yes na V3.0 e todos dentro de 58008, TF/TA e CNPS ✅ |
| CNPS 6291%/6292%/6293% No e 62909 No | 62910, 62920–62925, 62930–62935 « Gratuity, EOS, Post-termination »: **CNPS No na V3.0** ✅. 62909 « Statutory Gratuity, EOS » como 62900: coerente com a exclusão das « indemnités ayant un caractère de dédommagement » (Dec. 1635 art. 3) ✅. 62901 (13º) e 62905 continuam na CNPS ✅ |
| 9148201 só para quem paga IRPP | `SCALE` = residente, não residente ou jovem graduado, menos quem tem 58226 = 1; deficiente e diplomata fora ✅ |

## Achados novos
| ID | Sev. | Local | Evidência | Correção | Rota |
|---|---|---|---|---|---|
| W1 | **major** | `_build_v6.py:72–77` (`CASH_GROSS`: só `6263%`, `62650`, `6266%` no bloco 626xx); `ASSUMPTIONS.md:48` (A35 "checked series by series") | Na varredura, **62610–62612 e 62615–62619 « Medical insurance / Medical Care »** e **62651–62653 « Social raise / Social allowance » (pre-tax, Adjustment, Advance)** ficam **fora de IRPP, CNPS, TF e TA**. A WTC V3.0 marca Yes em todas as colunas. Não há decisão documentada. Para o seguro-saúde, isso contradiz o veredito 25 da LEI-VEREDITOS (« não há isenção no art. 45 », 65630 tributável, decisão que o v6 aplica em 9148131). O Dev pega toda a série com `626%%`. Já estava no v5 (mesma `CASH_GROSS`) | Acrescentar `('62619','6261%','Yes')` e `('62659','6265%','Yes')` à `CASH_GROSS` (o que leva os códigos também à TF/TA) e as mesmas linhas à `CNPS_GROSS`, ou documentar a exclusão com fonte. O 62651 "pre-tax deduction" merece nota (nome de dedução numa série Earning). Acrescentar um extra | builder |
| W2 | minor | `_build_v6.py:87` (`TFE_BASE`: 62180–62182 No) × `CASH_GROSS[1:]` (`629%%` Yes) | A indenização 6218x fica fora da TF/TA (A20), mas as gratificações de fim de contrato 62900/62909/6291–6293x, também de natureza rescisória, ficam **dentro** da TF/TA. Pelo art. 189-1° (« indemnités diverses »), ambas entram. A incoerência não está documentada no A20 nem no A35 | Alinhar: ou tirar 6290x–6293x da TF/TA, ou (melhor, pela lei) pôr 6218x dentro e fechar o A20 | builder |
| W3 | minor | planilha: `Results!O23, O24, O65…` (39 células, `build_comparacao.py:239`); `Summary!C11:D11` | (a) Coluna "Cause" diz « PSA exists only in v5 », mas o v6 também tem o PSA (H695 = 400). (b) "Legal accuracy" de 100% para v5 e v6 conta 34/34 temas como "Ours/Both", incluindo itens decididos com 60–75% (A34, D1) e ignorando os defeitos de matriz V1 e W1. A linha ponderada (C12/D12 = 89%) é a medida honesta | (a) « PSA exists only in v5 and v6 ». (b) Nota em G11 dizendo que é a contagem de temas e não exatidão do design, ou usar a ponderada como manchete | builder |

## Planilha: células conferidas
| Célula | Valor | Conferência |
|---|---|---|
| `Summary!D6` | 0,6415 (64%) | recontei Results!N5:N718: 458 "Same" em 714 → 0,6415 ✅ |
| `Summary!B18` | "Yes" | máx. de abs(G − H) fora do E21 = 0 ✅ |
| `Summary!C18` | 9 | linhas do E21 com abs(G − H) ≥ 0,5: 678, 681, 682, 687, 688, 689, 690, 696, 697 = 9 ✅ |
| `Results!G688` / `H688` (IRPP, E21) | 23.214 / 26.364 | v5: 287.750 → 23.213,75; v6: conta acima ✅. **Coluna v5 ≠ v6 no E21 confirmada** |
| `Results!H696` (líquido v6, E21) | 260.986 | 300.000 − 12.250 − 26.364 − 400 ✅ |
| `Results!E688` (IRPP Dev, E21) | 26.889 | Dev: 58105 350.000 (65%%%) → forfait 35.000 → 58008 335.000 → 322.750×12 com faixas `x.99` → 26.888,7 ✅ |

## Próximo passo
Rodada 3 (a última): W1 (major), W2, W3. Se a rodada 3 falhar, o caso sobe para uma pessoa. Como o W1 também está no v5, vale a mesma nota do V1: registrar no CONFERENCIA do v5.

---

# Rodada 3 (final, 2026-11-02, depois da "v6 r3" do construtor)

## Veredito: **PASS** (0 blocker, 0 major, 1 minor novo)

W1, W2 e W3 estão fechados, e não achei regressão. O minor X1 é de rastreio e não muda valor; tem de ser resolvido antes de fechar a rodada com o usuário, não antes do PASS. O PASS vale para o **design local**. Continuam fora do artefato: ok do usuário em D1/D2/A20/A34, barème da DGI (A26/R23), aceite no motor real (A10–A13, A16, A21, A23) e o v5, que ainda tem os defeitos de matriz V1/W1 (o v6 os corrige; o VALIDATION do v6 registra "v5 also has").

## Como conferi
- Diff do `_build_v6.py` contra a rodada 2: muda a `CASH_GROSS` (+`6261%`, +`6265%`), o `CNPS_GROSS` (idem), o `BIK_REAL` (sem os "No" exatos de 65610–65612 / 65660–65662), a `TFE_BASE` (6218x dentro), a `TAFP_BASE` (6218x, 62900, 62909, 6291–6293% fora), notas, cenário 5, E23–E26, `V1_CASES` e `sweep()`.
- Reexecução no scratchpad, com a WTC copiada para o caminho relativo: rc 0; 12/12 e 26/26 exatos; "1.540 valores, 0 diferenças inesperadas". As diferenças v5 → v6 aparecem só nos casos 5, E21, E23, E24, E25 e E26. `SKILL.md` e `SWEEP-run.txt` idênticos aos da pasta. 0 marcas. `_build_v5.py` sem mudança (md5 `87089bcc…`).
- Artigos relidos no CGI 2026 `.txt`: art. 189-1° (l. 6560–6570: « montant brut des traitements, salaires, pensions, émoluments, **indemnités diverses**, allocations, gratifications ») e art. 173 (l. 6287: « appointements, salaires, avantages en nature et rétributions quelconques, y compris les gratifications **servies régulièrement** »).

## Refeitos à mão
| # | Conta | CNPS EE | IRPP | TFE | TAFP | Líquido | v6 |
|---|---|---|---|---|---|---|---|
| 5 | 300.000 + indenização 900.000: CNPS sem a indenização → 10.500; IRPP 1.189.500×12 = 14.274.000 → 2.503.200/12; **TF 1.200.000 × 7,5% = 90.000** (art. 189-1°); TA só 300.000 → 3.600 | 10.500 | 208.600 | 90.000 | 3.600 | 980.500 | = |
| E23 | 62610 « Medical insurance » 50.000 em todas as bases = baseline de 350.000 | 12.250 | 28.464 | 26.250 | 4.200 | 308.886 | = |
| E24 | 62651 20.000: CNPS 320.000 → 11.200; 308.800×12 = 3.705.600 → 305.088/12 = 25.424; TF 24.000; TA 320.000 → 3.840 | 11.200 | 25.424 | 24.000 | 3.840 | 282.976 | = |
| E25 | 62900 EOS 100.000: fora da CNPS e da TA; 389.500×12 = 4.674.000 → 406.770/12 = 33.897,5 → 33.898; TF 400.000 → 30.000; TA 300.000 → 3.600 | 10.500 | 33.898 | 30.000 | 3.600 | 355.202 | = |
| E26 | 65610 « Phone cash benefit » 20.000: no caixa (6561%), CNPS (656%%), TF e TA (sem o "No" exato que saiu do `BIK_REAL`) → mesmos impostos do E24; líquido só com 62xxx (convenção do script) = 300.000 − 11.200 − 25.424 − 400 | 11.200 | 25.424 | 24.000 | 3.840 | 262.976 | = |

## W1–W3: situação
| ID | Situação | Evidência |
|---|---|---|
| W1 | ✅ fechado | `6261%` e `6265%` na `CASH_GROSS` (`_build_v6.py:79`) e na `CNPS_GROSS` (`:98`); E23, E24; 62651 "pre-tax deduction" com nota (A36) e pergunta ao dono da WTC (R33). Na varredura, só 4 códigos ficam fora de todas as bases: 62560–62563, o reembolso de relocation 2 (A22), igual à WTC N/N/N/N |
| W2 | ✅ fechado | A20 reescrito: rescisórias **dentro da TF** (art. 189-1° « indemnités diverses », 75%) e **fora da TA** (art. 173 só remuneração e gratificação regular, 60%). 6218x e 629xx agora com o mesmo tratamento. A leitura da TA é discutível (« rétributions quelconques »), mas está declarada com confiança e alternativa implícita; aceita |
| W3 | ✅ fechado | Planilha: 0 células "PSA exists only in v5". Summary A11 virou "Themes where our position matches **our reading** of the law", e G11 ressalva que não é a exatidão do design. A manchete é a ponderada (A12, 89%). Nova linha A19–E19 "Defects found by QA after the score" (v4 7, v5 7, v6 0) lista as séries. O "100%" agora vem com ressalva ✅ |

## Varredura: amostra de 12 códigos contra a WTC V3.0 (motor rodado por mim, não pelo `sweep()`)
| Código | WTC (Tax/CNPS/TA/TF) | v6 | Documentado em | ok |
|---|---|---|---|---|
| 62180 Severance | N/N/N/N | Y/N/N/Y | R18, A20 | ✅ |
| 62300 Annual leave pay | Y/Y/N/Y | Y/Y/Y/Y | A30, R19 | ✅ |
| 62520 Transportation | Y/Y/Y/Y | Y/N/Y/Y | D1 | ✅ |
| 62610 Medical insurance | Y/Y/Y/Y | Y/Y/Y/Y | igual | ✅ |
| 62651 Social raise | Y/Y/Y/Y | Y/Y/Y/Y | igual (A36) | ✅ |
| 62900 Statutory gratuity | Y/Y/Y/Y | Y/N/N/Y | A20, A35 | ✅ |
| 62910 Gratuity EOS | Y/N/Y/Y | Y/N/N/Y | A20 | ✅ |
| 62901 13º | Y/Y/Y/Y | Y/Y/Y/Y | igual | ✅ |
| 65521 Car fuel arrears | N/Y/Y/Y | Y/Y/Y/Y (IRPP capado) | art. 46-III | ✅ |
| 65610 Phone cash | Y/Y/Y/Y | Y/Y/Y/Y | igual | ✅ |
| 65660 Meal cash | Y/N/Y/Y | Y/N/Y/Y | igual | ✅ |
| 65800 Scholarship | N/N/N/N | N/Y/Y/Y | R19 | ✅ |

Agrupei as 122 divergências do `SWEEP-run.txt` por série (33 grupos). Cada grupo tem uma decisão documentada: R18, R19, D1, A20, A22, A30, A35, art. 46-III (BIK capado no IRPP) e 6563x (veredito 25). Nenhum grupo ficou sem explicação.

## Planilha `TD_Design_Comparison_v4_v5_v6_vs_Dev.xlsx`: 4 células de Results
| Célula | Valor (Dev / v4 / v5 / v6) | Conferência |
|---|---|---|
| `Results!H101` (cenário 5, TFE) | 22.500 / 22.500 / 22.500 / **90.000** | 1.200.000 × 7,5% ✅; causa em O101 cita art. 189-1° (75%) ✅ |
| `Results!H730` (E23, IRPP) | 28.464 / 23.397 / 23.398 / **28.464** | baseline 350.000 ✅ (v5 23.398 = sem o 62610) |
| `Results!H774` (E25, TAFP) | 4.800 / 4.800 / 4.800 / **3.600** | TA só sobre 300.000 ✅ |
| `Results!H794` (E26, TFE) | 24.000 / 22.500 / 22.500 / **24.000** | 320.000 × 7,5% ✅ |
Também: `Summary!B18` = "Yes" e `C18` = 54 (linhas dos 6 casos de correção), coerentes com o "0 unexpected differences" do script.

## Achado novo
| ID | Sev. | Local | Evidência | Correção | Rota |
|---|---|---|---|---|---|
| X1 | minor | `ASSUMPTIONS.md:33` (A20); `CONFERENCIA.md` | O A20 fecha "indenização **dentro** da TF". Isso inverte uma decisão registrada em `correcoes.md` (2026-07-07, linha 60: « severance ordinária tributável no IRPP **e fora da TFE** »), e nem o A20 nem a CONFERENCIA citam o conflito ou o ok do usuário. Com o D1 (transporte), a mesma situação foi tratada como "decisão técnica da frente, pendente do ok do usuário" | Marcar o A20 como "decisão técnica da frente (art. 189-1°, 75%), pendente do ok do usuário; substituiria `correcoes.md` 2026-07-07" e pôr na lista de decisões da CONFERENCIA | builder |

| 2026-11-02 | QA independente (frente Chade) | v6 rodada 3 (final): PASS; W1–W3 fechados; amostra de 12 códigos da varredura e 4 células de Results conferidas; 1 minor de rastreio (X1, A20 × correcoes 07/07) |

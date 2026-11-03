# Colômbia — design v2.0: revisão independente de QA (rodada 1)

> Hub: [[Colombia]] · Revisado: [[Research Pipeline/Colombia/2026-11-02-design-v2/CONFERENCIA|CONFERENCIA do v2.0]] · Padrão: [[Research Pipeline/Chad/2026-11-02-design-v6/QA-REVIEW|QA do Chade v6]]
> Revisor: QA adversarial independente (não construiu o v2.0). Data: 2026-11-02. Modo: **só leitura**. Este é o único arquivo gravado na pasta.

## Veredito: **FAIL** (0 blocker, 5 major, 9 minor)

A execução se reproduz bit a bit. A ordem está limpa: 0 leituras antes do lançamento, no verificador do construtor e no meu. As 405 linhas do WTC v1.9 conferem com as 9 matrizes, sem nenhuma divergência. As constantes 2026 batem com o CCG v1.7, e as 12 diferenças contra o cálculo independente estão bem explicadas.

Cinco defeitos impedem o PASS:
1. Um do método de retenção que o v2 **introduziu** (Procedimento 2).
2. Dois de lei na retenção da rescisão (bonificação por retiro e divisor do art. 1.2.4.1.8).
3. Um de forma do Dev (contribuições patronais como `employeeRate`).
4. Um vazamento da projeção < 30 dias para o Procedimento 2.

Nenhum deles aparece nos testes, porque nenhum caso exerce o Procedimento 2, a bonificação R345, um vínculo de menos de 12 meses ou o campo `employerRate`.

## Como conferi
- **Reexecução:** a pasta foi copiada para o scratchpad, com uma junction só de leitura para `2026-10-29-validacao-research`. `python -I -B _build_v2.py`: rc 0. `co_design_v2.json` (`84308c53…`), `VALIDATION-run.txt` (`0b3a5559…`), `SWEEP-run.txt` (`c74b85cc…`) e `_run-summary.json` (`57f19e8c…`) saem **idênticos** (md5) aos da pasta. Nada foi escrito na pasta do design.
- **Verificador próprio de ordem** sobre o JSON. Para cada leitura (assertion, fórmula, `employeeRateAccount`, matriz `isTaxable`), o verificador marca qualquer lançamento da conta com ordinal ≥ o da leitora, inclusive leitura parcial (lançada antes **e** depois). Resultado: **0**. IDs = 9170000 + ordinal nos 78; nenhum ordinal ou ID repetido. Contas lançadas e nunca lidas: 58149, 58170, 58178, 58194, 58195, 58196 e 58217, todas informativas ou de relatório, o que está coerente com o R4.
- **WTC v1.9 inteiro** (não por amostra): 405 linhas × matrizes 14 (X), 20 (W), 45 (Q), 47 (T), 49 (U), 50 (R), 51 (S), 72 (N) e 132 (P). Contra o flag N–X, com o roteamento R320/R339/R343/R344 em N: **0 divergências**. Linhas NA ficam fora da matriz; `Yes/No` fica false. Classes cobertas: Yes, No, Yes/No (17 em N, 58 em Q), NA (107), pacted (54), non-remunerative (79), Paid Rest (2) e Conditional (3).
- **Probes no motor do v2:** Procedimento 2 com e sem prima; Procedimento 2 com a projeção ligada; R345 e R343 de 15.000.000; indenização com 6 meses de vínculo; aprendiz nas duas fases; FSP com 33.000.000; limite do art. 114-1 (10 SMMLV e 10 SMMLV − 1); limite do auxílio de transporte (2 SMMLV e 2 SMMLV + 1).
- **Fontes primárias relidas** (`raw/docs/oficiais/CO/`):
  - DUR 1625 arts. 1.2.4.1.3, 1.2.4.1.4, 1.2.4.1.8, 1.2.4.1.11 e 1.2.4.1.13;
  - ET art. 401-3;
  - C-543/2007, parte resolutiva;
  - AT2 v30: tipo N, campo 22 (A/C) e campo 47;
  - Decreto 1990/2016 art. 1 (art. 3.2.1.5 do Decreto 780).
- **Finais e Dev:**
  - CCG v1.7 extraído do `.docx`: linhas 63, 325, 348, 457, 655, 751, 784–800, 899, 941, 1166, 1306, 1688, 1972, 2254, 2313–2314;
  - `td.json` do Chade, para o esquema e o uso de `employerRate`.

## 1) Refeitos à mão (passe 4)
| # | Conta pela lei | Desenho | Cálculo indep. | Veredito |
|---|---|---|---|---|
| I03 | diária 100.000; dias 1–2: 2/3 = 66.666,67 × 2 = 133.333; dias 3–90: 88 × 66.666,67 = 5.866.667; dias 91–100: MAX(50.000; 1.750.905/30 = 58.363,50) × 10 = **583.635**; total 6.583.635 | 583.635 / 6.583.635 | 500.000 / 6.500.000 | desenho certo (C-543: «no podrá ser inferior al salario mínimo legal vigente»); a explicação **procede** |
| I04 | dias 91–180: 90 × 58.363,50 = 5.252.715; total 11.252.715; IBC MAX(11.252.715; 1.750.905 × 180/30 = 10.505.430) | 5.252.715 / 11.252.715 / 11.252.715 | 4.500.000 / 10.500.000 / 10.505.430 | idem, **procede** |
| L15 | tipo 51, 15 dias → 3 semanas: IBC 1.750.905 × 3/4 = 1.313.178,75; EE 4% = 52.527,15 → 52.527; ER 12% = 157.581,45 → 157.581; soma 210.108. AT2 v30 campo 47 = IBC × tarifa (16%) = 210.108,60 → **210.109** | 210.108 | 210.109 | explicação procede como origem, mas o AT2 campo 47 fecha o A2 a favor do cálculo independente (m4) |
| L21 | 21 dias → 3 semanas: mesmas contas | 210.108 | 210.109 | idem |
| C23 | integral 70.036.200 → 70% = 49.025.340 > teto 43.772.625; INCRNGO 4% + 4% + FSP 2% (0,5 + 1,5) = 4.377.262,50; 58152 = 65.658.937,50; 25% = 16.414.734,375/mês; março: sobra 790 UVT = 41.375.460 − 2 × 16.414.734,375 = **8.545.991,25**; base 57.112.946,25 → (57.112.946,25 − 945 × 52.374) × 0,37 + 268 × 52.374 = **16.855.453,0125** | 8.545.991,25 / 16.855.453,01 | …,24 / …,02 | desenho **exato**; o cálculo independente arredonda o consumo ao centavo. **Procede** |
| CCG 8M | 8.000.000 − 720.000 = 7.280.000; × 0,75 = 5.460.000 = 104,2502 UVT → 9,2502 × 0,19 × 52.374 = 92.049,30 | 92.049,30 → 92.049 | = | ✅ (CCG l. 869–871) |
| P01 | (3.000.000 + 249.095) × 180/360 = 1.624.547,50 → 1.624.548 | 1.624.548 | = | ✅ (sem o auxílio duplicado do v1_2) |
| RC01 | 2.400.000 × 20/30 = 1.600.000; auxílio 166.063,33; 58150 = 1.766.063,33 × 30/20 = 2.649.095; INCRNGO 128.000 × 1,5 = 192.000; 25% = 614.273,75; base 1.842.821,25 = 35,2 UVT → 0 | = | = | ✅ |
| X1 | DAYS360(10/01/2024; 30/06/2026) = 891; dias 20 + 15 × 531/360 = 42,125; 20.000.000/30 × 42,125 = 28.083.333; 381,9 UVT > 204 → 20% = 5.616.667 | = | — | ✅ |
| X6 | 10 × 3.000.000/220 × 1,25 + 10 × 3.000.000/210 × 1,25 = 170.454,55 + 178.571,43 = 349.025,97 | = | — | ✅ (Lei 2101 art. 3: 42 h a partir de 15/07/2026) |
| FSP 33M | M = 18,85 → solidariedade 0,5% = 165.000; subsistência 0,5 + 0,6 = 1,1% = 363.000 | 165.000 / 363.000 | — | ✅ (Lei 100 art. 27, Lei 797 art. 8) |
| 114-1 | 17.509.050 (= 10 SMMLV) → não exonera (“menos de diez”); 17.509.049 → exonera | 58215 = 2 / 1 | — | ✅ |
| Auxílio | 3.501.810 → 249.095; 3.501.811 → 0 | = | — | ✅ |
| **P2 + prima** | Proc. 2, 10%, salário 10.000.000 + prima 5.000.000: base pela lei 15.000.000 − 900.000 = 14.100.000; 25% = 3.525.000 (< 40%); 10.575.000 × 10% = **1.057.500** | **682.500** (= sem a prima) | — | ❌ Q1 |
| **R345** | salário 4.500.000 + bonificação por retiro 15.000.000; média de 12 meses 58.500.000/12 = 4.875.000 = 93,08 UVT → 0% → **0** (art. 1.2.4.1.8; mesmo exemplo do CCG l. 1306) | **2.343.432** (leitura mensal) | — | ❌ Q2 |
| **6 meses** | indenização 6.000.000; pagamentos de 6 meses 36.000.000 ÷ **6** = 6.000.000 = 114,56 UVT → (6.000.000 − 95 × 52.374) × 0,19 = **194.649** | **0** (÷ 12 = 57,3 UVT) | — | ❌ Q3 |

## 2) Fidelidade à lei (passe 2): decisões novas
| Decisão | Fonte primária relida | Desenho | Confiança |
|---|---|---|---|
| IR sem `retro_` | DUR 1.2.4.1.3, Proc. 1: «la totalidad de dichos pagos que se hagan al trabajador … durante el respectivo mes» | certo | 92% |
| Seguridade social com `retro_` (Deliberate divergence (law)) | AT2 v30 l. 2136–2143 (tipo N para «corregir el IBC … de periodos ya vencidos»), l. 8059–8085 (registro A original, C correto, o operador paga a diferença) | certo; marca e fonte presentes em cada regulação SS | 92% (falta o registro no CHANGELOG: m3) |
| Piso C-543 em todos os segmentos | C-543/2007, RESUELVE: «el auxilio monetario por enfermedad no profesional no podrá ser inferior al salario mínimo legal vigente» | certo (dias 1–2, 3–90 e 91–180) | 95% |
| Retenção de indenizações 20% > 204 UVT sobre R339/R343/R344 | ET 401-3 e DUR 1.2.4.1.13: «Las indemnizaciones derivadas de una relación laboral … 20% para trabajadores que devenguen ingresos superiores … 204 UVT» | certo para as três; **faltam** R345 (Q2) e R340 (m1); divisor da média errado (Q3); medida dos 204 UVT diverge do exemplo do CCG (m9) | 90% nas três; 0% em R345 |
| Prima com leitura própria | DUR 1.2.4.1.3, Proc. 1: «Cuando se trate de la prima mínima legal de servicios … el "valor a retener" es el que figure frente al intervalo al cual corresponda la respectiva prima» | certo no **Proc. 1**; no Proc. 2 a prima some (Q1) | 95% (Proc. 1) |
| Projeção < 30 dias opcional | DUR 1.2.4.1.3, Proc. 1: «su retención **podrá** calcularse así: a) … b)» | certo como opção desligada; vaza para o Proc. 2 (Q5) | 95% |
| Tetos anuais 790/1.340/3.800 pelo acumulado | CCG v1.7 l. 704, 757, 800 (Decreto 2231/2023 art. 9 «1.340 UVT anuales»; CE S4 rad. 24047/2021). **A sentença 24047 não está em `raw/`**, por isso a confiança vem do CCG | certo: `_ytd` de 58157 + 58166, 58159 + 58167 e 58156; C23 exato | 85% |
| Cesantías sem retenção (inclusive não residente) | DUR 1.2.4.1.11: «en ningún caso los pagos efectuados por concepto de cesantías o intereses sobre las mismas, estarán sujetos a retención» | certo (R321/R322 N = P = No; X3) | 97% |
| Art. 114-1 | CCG l. 561; Memo item 1 | certo (probe no limite) | 90% |
| Lei 1393 | CCG l. 531–532; Memo itens 2–4 | certo (58104 só em 58106/58112/58113/58114; fora de 58108) | 90% |
| Incapacidade e licenças fora de SENA/ICBF/CCF | WTC T = No em R326, R327 e R330; CCG l. 2300+ (CE S4 exp. 23856/2021) | certo | 90% |

## 3) Consistência com os finais (passe 3)
- **Constantes 2026** (`_build_v2.py:37–44`) × CCG v1.7: SMMLV 1.750.905 (l. 348), UVT 52.374 (l. 751), auxílio 249.095 (l. 457). Tabela do art. 383 (0/19/28/33/35/37/39; 95/150/360/640/945/2.300; +10/69/162/268/770) e tetos 790/1.340/3.800 (l. 784–789). Alíquotas: saúde 4/8,5; pensão 4/12 (+10 de alto risco); FSP 0,5 + 0,5…1,5; CCF 4, SENA 2, ICBF 3. ARL inicial 0,522/1,044/2,436/4,35/6,96 (Decreto 1772 art. 13). ✅
- **Matrizes × WTC:** 405/405 linhas, 9/9 matrizes, 0 divergências (ver "Como conferi"). As 21 linhas `Yes/No` false estão listadas no R1. ✅
- **CSV** v2_0 com md5 `4e5f8fd1…`, igual ao do v1_2 (colunas N–X sem mudança na rodada 6). ✅
- **Aprendiz:** fase de aula com saúde EE 4% sobre 1 SMMLV e ARL (CCG l. 655, 2313) ✅. Na fase prática, ver m8.

## Achados
| ID | Sev. | Local | Evidência | Correção | Rota |
|---|---|---|---|---|---|
| Q1 | **major** | `_build_v2.py:243–244` (`NOWH` aplicado a 9170072 para todos); 9170086; 9170088–90 (só `P1`); `CHANGELOG.md` linha 9170086 ("same rule") | DUR 1.2.4.1.3, Proc. 2: «el "valor a retener" … es el que resulte de aplicar a la **totalidad de tales pagos gravables** [distintos de la cesantía y de los intereses]». CCG v1.7 l. 325 e 2254: «Under Procedure 2 … the service bonus is folded into the ordinary monthly base». O v1_2 (l. 335) dizia o mesmo. No v2, R320 é false no 58150 de todos, e as regulações 88–90 só rodam no Proc. 1. **A prima de quem está no Proc. 2 não é retida.** Probe: 10.000.000 + prima 5.000.000, 10% → 58162 = 682.500 (igual ao mês sem prima); pela lei, 1.057.500. **Regressão** introduzida pela correção do defeito 4 do v1_2 | Pôr R320 na base do Proc. 2: uma regulação antes da 74 (flat, `acc('R320')`, assertion `AND(EQUALS($58205;1);EQUALS($58206;2))`, debit 58150), ou duas leituras mensais por procedimento. Corrigir a linha 9170086 do CHANGELOG e acrescentar um caso Proc. 2 com prima | builder |
| Q2 | **major** | `_build_v2.py:64` (`INDEMN` sem R345); 9170072 (R345 = true); 9170087; Memo item 6; CHANGELOG defeito 5 | DUR 1.2.4.1.8: «La retención … aplicable a las indemnizaciones por despido injustificado **y bonificaciones por retiro definitivo del trabajador**, se efectuará así: a) … promedio … b) … porcentaje … se aplica al valor de la bonificación o indemnización». CCG l. 899 e 1317: «A dismissal indemnity **and a retirement bonus** are outside the ordinary monthly base». WTC R345 «Bonificacion por Retiro / Acuerdo de Terminacion». No v2, R345 fica na leitura mensal. Probe: salário 4.500.000 + R345 15.000.000 → 58161 = **2.343.432**; pelo art. 1.2.4.1.8 (média de 4.875.000 = 93,08 UVT), **0** | Ler R345 fora do mês, com o método do art. 1.2.4.1.8 (percentual da tabela sobre a média). Os 20% do art. 401-3 são só para indenização; dizer se valem para a bonificação (hoje o CCG l. 899 trata as duas iguais). R345 false em 9170072; atualizar Memo item 6 e CHANGELOG | builder |
| Q3 | **major** | `_build_v2.py:280` (`AVG = DIVIDE(DIVIDE($58255;12);$52502)`); 9170087; input 58255 | DUR 1.2.4.1.8 lit. a: «dividiendo por doce (12), **o por el número de meses de vinculación si es inferior a doce (12)**». CCG l. 899 diz o mesmo. O v2 divide sempre por 12. Probe: 6 meses de vínculo, 36.000.000, indenização 6.000.000 → 0; pela lei, 194.649 (média 6.000.000 = 114,56 UVT). Subretenção para todo vínculo de menos de 12 meses. O R3 não cita o divisor | Novo input "meses de vínculo nos 12 meses anteriores" (ou `MIN(12; meses)`), usado como divisor. Caso de vínculo curto na validação | builder |
| Q4 | **major** | `_build_v2.py:110–113` (`band()`: `employerRate` sempre None); 9170062–68 e 9170070 (`employeeRate` 8,5/4/2/3/12/4); 9170063/64 (`employeeRateAccount` 52516/52519) | No `td.json` do Dev, a parte patronal vai em `employerRate`: «TD CNPS Contribution EE and ER»: `employerRate` 7,5 / 4,0 / 5,0, crédito em 2551/2560/2537. O QA do Chade v6 tratou a mesma troca como **erro do Dev a não copiar** ("TF/TA lançadas como taxa do empregado → v6 `employerRate` ✅"). No v2, as nove contribuições patronais (saúde, pensão, ARL, CCF, SENA e ICBF do empregador, e as do tipo 51) estão como taxa do **empregado**. O motor (S5) só lê `employeeRate`, então nenhum teste pega. O líquido local está certo porque é recalculado (58170), mas no motor real a classificação define dedução × custo | `employerRate` / `employerRateAccount` nas bandas ER; estender o S5 do `co_engine.py` para ler as duas e conferir que nenhuma ER entra no líquido | builder |
| Q5 | **major** | 9170073 (assertion `EQUALS($58205;1)`, sem o procedimento); 9170086 (não divide por `$58240`) | A projeção existe só no texto do Proc. 1 (DUR 1.2.4.1.3 lits. a–b). Com a opção 58214 = 1, o fator entra em 58151/58152/58160 também para o Proc. 2, e a 9170086 aplica o percentual à base projetada. Probe: Proc. 2, 10%, 10.000.000, 15 dias → **682.500** com a opção ligada contra **341.250** desligada (retenção × 30/15). A opção é por entidade, então basta ligar uma vez para afetar todos os funcionários do Proc. 2 em meses de admissão ou saída | Assertion da 9170073 = `P1` (ou `IF(EQUALS($58206;1);…;1)`), e caso Proc. 2 + 58214 = 1 na validação | builder |
| m1 | minor | `_build_v2.py:64`; `RESEARCH_GAPS.md:12` (R8 só R341/R342) | WTC R340 «Indemnizacion Moratoria (CST art. 65)» é «indemnización» no texto e deriva da relação de trabalho (ET 401-3). Fica na leitura mensal, e o R8 não a cita | Rotear R340 com R339/R343/R344 ou incluí-la no R8 com a razão | builder |
| m2 | minor | 9170132 (assertion `EQUALS($58205;2)`); campo `divergence` da 9170132; chaves do JSON | O Dev lê `$64552`. A troca para 58205 não tem razão de lei e não leva a marca "Deliberate divergence (law)" (o A5 só pede confirmação), o que contraria a decisão 1 da CONFERENCIA ("forma do Dev onde a lei não obriga diferença"). Além disso, o JSON usa `id` em vez de `regulationId` e não tem `systemTaxYearIds` (chaves do `td.json`) | Usar `$64552` (mapeando o 58205 para ele) ou marcar a divergência como de dados, com o A5; renomear `id` → `regulationId` e incluir `systemTaxYearIds` (ou dizer no A-list que ficam para o Dev) | builder |
| m3 | minor | `CHANGELOG.md` (todas as linhas income_tax 9170072–9170141: "same rule") | No v1_2 (l. 175–191), as 17 regulações de IR tinham `retro_simple_tax*`; no v2, nenhuma tem. A decisão está certa e documentada (Regulation_Design l. 247, Memo item 17), mas o CHANGELOG não registra a mudança de grupo, como no V2 do Chade. Também não registra a mudança de comportamento do Proc. 2 (Q1) | Uma linha "rule group retro_ → simple_tax* (law: DUR 1.2.4.1.3)" por regulação de IR, ou um item 7 em "Defects/changes" | builder |
| m4 | minor | `ASSUMPTIONS.md` A2; `_build_v2.py` `UP100` nas bandas EE/ER; 9170060/68; 9170074 (`$58121_raw`…) | (a) Decreto 780 art. 3.2.1.5 num. 2 (Decreto 1990/2016): «El valor de los aportes liquidados **por cada cotizante** … aproximarse al múltiplo de 100 superior». AT2 v30 campo 47: «multiplicando … "IBC Pensión" … por … "Tarifa de aportes a pensiones"», com o arredondamento. É **um** valor por cotizante e fundo. Arredondar cada parte separadamente dá até COP 100 a mais (1 SMMLV: 70.100 + 210.200 = 280.300 contra PILA 280.200) e 1 peso no tipo 51 (L15/L21). As fontes fecham o A2. (b) A INCRNGO usa a contribuição **antes** do arredondamento (`_raw`), não o valor descontado do empregado (58121…), e não cita fonte para isso | Lançar o total por fundo arredondado e ER = total − EE; INCRNGO sobre as contas descontadas, ou fonte para o `_raw` | builder |
| m5 | minor | 9170040 (`matrix(None)`: toda linha ativa = true); 9170141 | O bruto 58100 soma as linhas **Deduction** ativas R6 «Unpaid LOA – Basic salary deduction» e R37 «Long Term Disability deduction» com sinal positivo, o salário em espécie R319 e as cesantías R321/R322 (consignadas no fundo até 15/02, Lei 50 art. 99 num. 3; CCG l. 1240). O líquido não desconta 58257/58258 (descontos em folha). Resultado: líquido em dinheiro superestimado | Matriz do bruto em caixa (sem espécie, sem cesantías consignadas, deduções com sinal) e líquido − 58257 − 58258 | builder |
| m6 | minor | `_build_v2.py:669` (`… and False`); `sweep()` | A checagem da coluna O está desligada (`and False`, lista sempre vazia). A varredura compara matrizes geradas das mesmas colunas N–X com essas colunas: confirma o mecanismo (base, piso, excesso 1393), mas é tautológica para a matriz. Por isso Q1–Q5 escaparam: nenhum caso com Proc. 2, R345, vínculo < 12 meses, Proc. 2 + projeção, aprendiz prático ou `employerRate` | Reativar ou remover a checagem de O e dizer no VALIDATION que a varredura só testa o mecanismo; acrescentar os seis casos | builder |
| m7 | minor | `CO_Statutory_Research_Memo_v2_0.md:24, 70, 184, 191, 198` e tabela-resumo; `CO_Taxability_Matrices_v2_0.md` (71 "⚠") | (a) l. 24 «matches the provider payroll»: referência a uma comparação interna, não citável. (b) l. 70 promete uma «configuration option, off by default» para reter 20% da cesantía do não residente: **não existe flag no JSON**, e a opção contrariaria o «en ningún caso» do DUR 1.2.4.1.11. (c) l. 184/191 «open item 8/7» é numeração do v1_2 (no v2, a Part 6 só aponta para RESEARCH_GAPS). (d) A tabela-resumo vai até o item 17 e falta o 18. (e) l. 198 cita «the Drive folder 07 - Design». (f) "⚠split" é marcador residual pelo lint C29 | Tirar (a) e (e); (b) tirar a frase ou criar e documentar o flag (recomendo tirar); (c) apontar R2/R3; (d) acrescentar o item 18; (f) trocar por "split" | builder (direto) |
| m8 | minor | R338 `Yes/No` em R/T/U/W/X; `RESEARCH_GAPS.md` R2 | O probe do aprendiz na fase prática dá pensão 0, FSP 0, CCF 0 e base de prestações 0. CCG l. 2314 e Memo item 12: «practical phase: all rights of an employment contract». O R2 cita só a base de parafiscais | Ampliar o R2: pensão (U), FSP (R), prestações (W) e férias (X) da fase prática ficam false até o split | builder (direto) |
| m9 | minor | 9170087 (`DIVIDE($58150;$52502)`); `RESEARCH_GAPS.md` R7 | O teste dos 204 UVT lê o 58150 do mês da rescisão, que inclui o pagamento de férias R156 e outros pagamentos da liquidação. No exemplo do CCG v1.7 (l. 1306), o teste é feito sobre o salário mensal (4.500.000 = 85,92 UVT) e a liquidação fica fora. Exemplo: salário 9.000.000 + férias 2.000.000 = 11.000.000 > 204 UVT → 20% no desenho, tabela pela leitura do CCG | Alinhar com o CCG (base = salário do mês, por exemplo 58101) ou registrar no R7 a diferença em relação ao exemplo do CCG | builder |

## 4) Conferido e aprovado
- Reprodução bit a bit dos 4 produtos (md5) e dos números do VALIDATION/SWEEP: 112 casos, 2.293 valores, 12 diferenças; 11/11 conferências; 2.682 checagens, 0 diferenças; v1_2 com 47 defeitos de ordem, 34 diferenças e 16 na varredura.
- Ordem: 0 defeitos pelo meu verificador, inclusive leitura parcial e `_raw`/`_ytd`.
- Os 6 defeitos do v1_2 no CHANGELOG procedem. Refiz P01 (auxílio duplicado), I03 (texto do piso), coluna P (R241–R248, R282, R284–R286 entram; R349, R350 e R353 saem) e a ordem.
- As 12 diferenças estão explicadas: I03/I04 (o desenho segue a C-543), C23 (o desenho é exato) e L15/L21 (origem certa; a decisão está no m4).
- Prima no Proc. 1, piso C-543, cesantías fora da retenção do não residente, tetos anuais pelo acumulado, 114-1, Lei 1393 e incapacidade fora de SENA/ICBF/CCF: certos (tabela do passe 2).
- `retro_`: marca "Deliberate divergence (law)" com fonte em todas as 56 regulações SS; as 22 de IR seguem o Dev (9170132).
- A 9170132 tem o nome, ordinal, taxGroup, taxRuleGroup e taxationType do Dev. A base P exclui R321/R322.
- Pacote em inglês: nenhuma ocorrência de pipeline, agent, rodada, COVAL, oracle, Claude ou nome de cliente. "draft" aparece só como nome da planilha do Dev («CO Draft Regulations»), o que é aceitável. As exceções estão no m7.

## Fora do pedido (não incluí nos achados)
- CCG v1.7 l. 1688 diz que a base de **parafiscais** do salário integral fica limitada a 43.772.625. A l. 1972 (e a Lei 21/1982 art. 17) diz «No ceiling at all». O desenho segue a l. 1972, o que está certo. A contradição é do CCG e vai para o hub.
- AT2 v30 l. 8278+ menciona a distribuição dos aportes pela Lei 2381 «a partir del periodo … julio de 2025», enquanto o CCG v1.7 dá a Lei 2381 como vigente só em 1/4/2027 (C-264/2026). A decisão é do CCG; vale reconferir antes de 2027.

## Próximo passo
Rodada 2 com o builder: Q1–Q5 e m1–m9. Q1, Q2, Q3 e Q5 mudam valores; Q4 é só forma. Para cada um, um caso novo na validação. Teto: 3 rodadas.

| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | QA independente (frente validacaoco) | revisão do v2.0, rodada 1: FAIL (0 blocker, 5 major, 9 minor); execução reproduzida (md5), ordem 0, WTC 405 × 9 matrizes 0 divergências, 15 casos refeitos à mão |

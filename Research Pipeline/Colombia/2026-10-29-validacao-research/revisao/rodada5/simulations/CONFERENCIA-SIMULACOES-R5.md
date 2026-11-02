# Conferência das simulações — rodada 5 (A-1: tetos anuais pelo acumulado)

Ligado a [[CONFERENCIA-R5]], [[CONFERENCIA]] (pasta `2026-10-29-validacao-research`) e [[Colombia]]. Data: 2026-11-02. Nada foi para Drive, ticket ou e-mail.

**Resultado: PASS.**

## Decisão aplicada
- **790 UVT** (25% isento, ET 206 num. 10) e **1.340 UVT** (teto conjunto de 40%, ET 336 num. 3; DUR 1625 art. 1.2.4.1.6 par. 3) são **anuais**. Na retenção mensal eles são controlados pelo **acumulado do ano**, e não por 1/12 (65,8333 e 111,6667 UVT/mês).
- **3.800 UVT** (AFC/AVP, ET 126-1/126-4; DUR 1.2.1.22.43): também anual e controlado pelo acumulado.
- Fontes:
  - CE Sección Cuarta, rad. 24047 (28/10/2021), anulou o limite mensal;
  - Decreto 2231/2023 art. 9 ("UVT anuales");
  - DUR 1625 art. 1.2.1.22.43.
- Fórmula nas planilhas: **limite do mês = mín(% do mês, saldo anual)**, onde saldo anual = teto anual − consumo de janeiro até o mês anterior.

## O que mudou
| Arquivo | Mudança |
|---|---|
| `CO_Simulation_2026_11_02_V1.1.xlsx` (antes V1.0) | **Abas mensais (49):** <br>• As linhas AFC, 25% e teto 40%/1.340 (68–70 nas abas C/R/D; nas abas H, nas linhas equivalentes) passam a ler o saldo anual. <br>• Novo bloco **YEAR-TO-DATE ANNUAL CAPS** em R:T, com: meses anteriores (`MONTH(D9)-1`); premissa escrita (mesmo pagamento desde 1/1/2026, como no CCG); consumo e saldo de 3.800, 790 e 1.340 UVT. <br>• As reliefs dos meses anteriores respeitam os 40% de cada mês e o saldo de 790 UVT. <br>• Coluna E (texto da fórmula) igual à F; colunas H/L (regra do oráculo e norma) atualizadas. <br>• Coluna I (oráculo): 128 células trocadas, em 16 abas × 8 linhas (25%, teto, reliefs, base, base UVT, imposto UVT, retenção, líquido). <br>**Outras abas:** <br>• Parameters: B50, B52 e B54 sem "/12"; fontes E50, E52 e E54 atualizadas. <br>• Checks index: nota da norma, coluna F. <br>• Formula comparison: linhas 26–28. <br>• Read me: A1, B5, B9 e B14. <br>• Títulos de R07 e R08 com nota: R07 → em março quem limita são os 40%, e o teto de 1.340 UVT limita a partir de maio; R08 → os 790 UVT limitam a partir de outubro. |
| `Tax Simulations - Colombia.xlsx` | **14 abas de depuração:** <br>• E/I 50–52 leem o saldo anual. <br>• Novo bloco **7. YEAR-TO-DATE ANNUAL CAPS** nas linhas 86–99, com a entrada E88 "salário de cada mês anterior" (em branco = mesmo pagamento). <br>• NON-SALARY BONUS (RC05 = T105): E88 = 8.000.000 (meses jan–ago só com o salário, premissa do CCG). <br>• J50–52 e N55/N57/N59 sem "/12". <br>• Coluna F (oráculo): 32 células, em 4 abas × 8 linhas. <br>**Outras abas:** <br>• SERVICE BONUS SEPARATE READ (PB): E12/E13 = mín(%, teto anual − já usado), com entradas E21/E22 = 0 (premissa: prêmio lido sozinho, como no exemplo da pesquisa); resultado igual (187.500; 300.000; retenção 0). B18 diz que o ponto aberto deixou de existir. <br>• READ ME: B5, B7, B10 (ponto aberto 2 fechado) e B11. |
| `Colombia Simulations - Law vs Provider.xlsx` | **Não recalculado com o teto anual**, por limitação (ver abaixo). <br>• LAW SIMULATION C28: nota "não rerodado com o teto anual". <br>• PROVIDER RESULT J28: nota de limitação, e o texto antigo "3.447.955,50" foi corrigido para 3.447.955,00 (790 × 52.374 / 12). <br>• READ ME B8: limitação acrescentada. <br>• Contagens: sem alteração. |

## Conferência com o oráculo
- **Oráculo:** `oracle/oracle_v2.py`, sem alteração de código, rodado mês a mês desde janeiro com o saldo anual pelo script `scripts/oracle_sim_r5.py`. Ele usa o mesmo método de `revisao/rodada5/scripts/oracle_r5_ytd.py` e o resultado está em `oracle-sim-r5.json`.
- **Bate com `oracle-r5-ytd.json`:** 18 casos afetados; os valores coincidem nos 18.
- **Os 16 + 4 casos abaixo:** são os que estão nas planilhas. RC07, o exemplo do Payslip, não tem aba.
- **Colunas da tabela:**
  - "antes" = retenção da V1.0 (1/12);
  - "depois" = valor recalculado no Excel;
  - "oráculo" = valor do oráculo com o acumulado;
  - diferença = depois − oráculo.
- **Retenção:** valores em COP, arredondados ao peso como na linha 58161.

| Arquivo | Aba | Caso | Consumo do 25% jan–mês anterior | 25% isento: antes → depois | Retenção antes | Retenção depois | Oráculo | Diferença | Resultado |
|---|---|---|---|---|---|---|---|---|---|
| CO_Simulation | C09 Mar | C09 | 12.746.587,94 | 3.447.955,00 → 6.373.293,97 | 4.666.698 | 3.701.336 | 3.701.336 | 0 | PASS |
| CO_Simulation | C10 Mar | C10 | 12.718.573,92 | 3.447.955,00 → 6.359.286,96 | 4.648.208 | 3.687.469 | 3.687.469 | 0 | PASS |
| CO_Simulation | C11 Mar | C11 | 13.513.484,78 | 3.447.955,00 → 6.756.742,39 | 5.172.850 | 4.080.950 | 4.080.950 | 0 | PASS |
| CO_Simulation | C12 Mar | C12 | 13.483.719,86 | 3.447.955,00 → 6.741.859,93 | 5.153.205 | 4.066.216 | 4.066.216 | 0 | PASS |
| CO_Simulation | C13 Mar | C13 | 15.003.505,40 | 3.447.955,00 → 7.501.752,70 | 6.156.263 | 4.818.510 | 4.818.510 | 0 | PASS |
| CO_Simulation | C14 Mar | C14 | 15.793.163,10 | 3.447.955,00 → 7.896.581,55 | 6.677.437 | 5.209.391 | 5.209.391 | 0 | PASS |
| CO_Simulation | C15 Mar | C15 | 15.758.145,44 | 3.447.955,00 → 7.879.072,72 | 6.654.326 | 5.192.057 | 5.192.057 | 0 | PASS |
| CO_Simulation | C16 Mar | C16 | 7.966.617,30 | 3.447.955,00 → 3.983.308,65 | 1.819.910 | 1.670.011 | 1.670.011 | 0 | PASS |
| CO_Simulation | C17 Mar | C17 | 7.966.617,76 | 3.447.955,00 → 3.983.308,88 | 1.819.911 | 1.670.011 | 1.670.011 | 0 | PASS |
| CO_Simulation | C19 Mar | C19 | 19.697.681,24 | 3.447.955,00 → 9.848.840,62 | 9.334.405 | 7.142.127 | 7.142.127 | 0 | PASS |
| CO_Simulation | C20 Mar | C20 | 20.197.681,24 | 3.447.955,00 → 10.098.840,62 | 9.684.405 | 7.389.627 | 7.389.627 | 0 | PASS |
| CO_Simulation | C21 Mar | C21 | 24.074.943,76 | 3.447.955,00 → 12.037.471,88 | 12.398.488 | 9.392.157 | 9.392.157 | 0 | PASS |
| CO_Simulation | C22 Mar | C22 | 10.663.886,88 | 3.447.955,00 → 5.331.943,44 | 3.330.381 | 2.802.864 | 2.802.864 | 0 | PASS |
| CO_Simulation | C23 Mar | C23 | 32.829.468,76 | 3.447.955,00 → 8.545.991,25 | 18.741.726 | 16.855.453 | 16.855.453 | 0 | PASS |
| CO_Simulation | R07 Mar | R07 | 12.162.016,00 | 3.447.955,00 → 6.081.008,00 | 7.341.793 | 4.519.775 | 4.519.775 | 0 | PASS |
| CO_Simulation | R08 Mar | R08 | 9.100.000,00 | 3.447.955,00 → 4.550.000,00 | 2.454.605 | 2.146.032 | 2.146.032 | 0 | PASS |
| Tax Simulations | 1340 UVT CAP BINDING | R07 | 12.162.016,00 | 3.447.955,00 → 6.081.008,00 | 7.341.793 | 4.519.775 | 4.519.775 | 0 | PASS |
| Tax Simulations | 25 PCT EXEMPT 790 UVT CAP | R08 | 9.100.000,00 | 3.447.955,00 → 4.550.000,00 | 2.454.605 | 2.146.032 | 2.146.032 | 0 | PASS |
| Tax Simulations | ALL-INCLUSIVE SALARY | C22 | 10.663.886,88 | 3.447.955,00 → 5.331.943,44 | 3.330.381 | 2.802.864 | 2.802.864 | 0 | PASS |
| Tax Simulations | NON-SALARY BONUS | RC05 (= T105) | 14.560.000,00 | 3.447.955,00 → 6.622.000,00 | 4.994.990 | 3.947.555 | 3.947.555 | 0 | PASS |

### Linhas intermediárias
- **O que foi comparado:** 25%, reliefs aplicadas e base gravável, em todos os 20 casos acima.
- **Diferença máxima:** |dif| ≤ 0,01 COP. A causa é o oráculo gravar 2 casas decimais. O pior caso é C23: 25% 8.545.991,25 × 8.545.991,24 (0,01).
- **Retenção bruta e arredondada:** iguais ao oráculo nos 20 casos.

### RC05 / T105 (set/2026; salário 8.000.000 desde 1/1 + prêmio pactuado de 20.000.000 só em setembro)
| Passo | Valor |
|---|---|
| Consumo jan–ago | 1.820.000 × 8 = 14.560.000 |
| Saldo dos 790 UVT | 41.375.460 − 14.560.000 = 26.815.460 |
| 25% isento | 6.622.000 |
| Base | 19.866.000 |
| Imposto em UVT | 75,3724138 |
| Retenção | **3.947.554,80** (bruta = imposto em UVT × 52.374), arredondada a 3.947.555 |

Bate com o oráculo, com o CCG v1.6-DRAFT-R5 (T105) e com a conta passo a passo da [[CONFERENCIA-R5]].

### Teste mecânico (Excel, CalculateFull, `final/simulations/scripts/recalc.ps1`)
| Arquivo | Erros de fórmula | OK | DIFF | n/a | Antes (V1.0) |
|---|---|---|---|---|---|
| CO_Simulation V1.1 | 0 | 1.670 | 0 | 115 | 1.670 / 0 / 115 |
| Tax Simulations | 0 | 467 | 0 | 82 | 467 / 0 / 82 |
| Law vs Provider | 0 | — | — | — | — |

Conferências adicionais (`scripts/check_sim_r5.py` → `check-sim-r5.json`):
- **"/12" nos tetos:** nenhuma fórmula de 790, 1.340 ou 3.800 UVT ainda usa "/12" nos dois arquivos. O que sobrou é a linha informativa de 72 UVT por dependente, que só entra na declaração anual e não é deduzida.
- **Texto da fórmula:** coluna E (CO_Simulation) e coluna I (Tax) iguais à fórmula da célula de resultado.
- **Retenção que mudou:** só nas 16 abas e nos 4 payslips esperados. As outras 33 + 10 ficaram com valor idêntico, porque nelas o 1/12 não limitava; logo o acumulado também não limita no mês simulado.
- **AFC:** nenhum caso da suíte é limitado pelo 3.800/12 do oráculo. A troca para o saldo anual não muda nenhum valor e o oráculo continua válido nessa linha.
- **Robustez da lógica das fórmulas em todos os meses:**
  - Método: emulação do bloco YTD de jan a dez para os 17 casos afetados com mesmo pagamento: 204 meses × oráculo mês a mês.
  - Inclui o ramo em que o saldo de 790 UVT acaba no meio do ano (C23 a partir de abril; R07 a partir de junho).
  - Resultado: diferença máxima de 0,05 COP nas reliefs aplicadas, vinda do arredondamento do oráculo a 2 casas decimais acumulado.

## Limitações
1. **Premissa do consumo.**
   - Regra geral: mesmo pagamento do mês simulado desde 1/1/2026, sem outro empregador nem outra renda isenta ou dedução no ano (premissa do CCG).
   - RC05: meses anteriores só com o salário.
   - Fora dessas premissas, o consumo real tem de vir do histórico da folha. As planilhas não têm histórico; nos Tax, a entrada E88 permite informar o salário dos meses anteriores.
   - O prêmio de serviços de junho não entra no consumo (mesma premissa de `oracle_r5_ytd.py`). No T105 ele não muda o resultado (conta na [[CONFERENCIA-R5]], passo 5).
2. **AFC/AVP (3.800 UVT).** A fórmula da planilha usa o saldo anual. O oráculo usa 3.800/12, mas ele nunca limita na suíte, então não há caso que prove a diferença.
3. **Law vs Provider.**
   - O consumo de jan–ago por empregado não está nos agregados. Não foi inventado: C28 e J28 ficaram com nota de limitação e as contagens da linha 28 e das retenções dependentes seguem as de 1/12.
   - Elas não são veredito sobre o fornecedor.
   - Para fechar, é preciso rerodar a partir das entradas do Test 4, fora desta pasta e sem abrir dado de cliente aqui.
4. **PB (prêmio lido à parte).** "Já usado no ano" = 0 por premissa, porque o exemplo da pesquisa lê o prêmio sozinho. Numa folha real, entra o 25% já usado pelas leituras de salário.
5. **Títulos dos casos R07 e R08.** O nome do caso no oráculo continua "1,340 UVT cap binding" / "790 UVT cap". No mês simulado (março) esses tetos não limitam mais; os títulos levam a nota com o mês em que passam a limitar.

## Arquivos e md5
| Arquivo | md5 |
|---|---|
| `CO_Simulation_2026_11_02_V1.1.xlsx` | `c4075b22541a63f9a7d7bceca60eecb7` |
| `Tax Simulations - Colombia.xlsx` | `bf47180409210658e62e64c458d03de4` |
| `Colombia Simulations - Law vs Provider.xlsx` | `d3e2ce248eb5dddce290836105bbe28c` |
| `oracle-sim-r5.json` | `91be925195ce0669976babf57ae92693` |
| `scripts/oracle_sim_r5.py` | `b923e05518511c0c3d860ca0b7bd1fda` |
| `scripts/apply_sim_r5.py` | `b5a2f78681b326eb0e7132cc4b2b3acb` |
| `scripts/check_sim_r5.py` | `a301dc3d03bcd5a3f84f2922f6fb44d1` |

Os três `.xlsx` foram copiados para `final/simulations/` (versão única em `final/`). Os de 30/10 foram movidos para `final/_historico/2026-10-30/simulations/`.

## Registro
| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | validacaoco | A-1 nas simulações: tetos anuais pelo acumulado (790, 1.340, 3.800 UVT), recálculo no Excel, conferência com o oráculo YTD (20 casos, PASS), Law vs Provider com nota de limitação. |

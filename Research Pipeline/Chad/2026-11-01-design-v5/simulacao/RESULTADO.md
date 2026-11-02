# Simulacao Chade: motor do Dev (td_2026) x nosso v5 (10 cenarios do v4 + 2 extras)

> Gerado em 2026-11-01 (frente Chade, v5 rodada 3; texto-base de 2026-10-30). Calculo local; nada foi carregado no HRBlizz. Dev = `td.json` (igual ao CT-A-588), executado por `sim_dev.py`; nosso = `_build_v5.py` como esta (`run()`). Gerado por `comparar.py`; dados em `resultado.csv`.
> Diferenca = Dev menos nosso, em XAF. Causa = regulacao do Dev (ID 9148xxx) e item da [[COMPARACAO]] (B1 #n / C#). Siglas: IRPP, TFE, TAFP, CNPS EE (empregado) / ER (empregador).

## Suposicoes do engine que mais pesam (lista completa no topo de `sim_dev.py`)
- **S2 matriz**: conta exata vence padrao; entre padroes vence o mais especifico (afeta 65400 em `65%%%` x `6540%`, 62180 em `621%%` x `6218%`).
- **S3**: regulacao com base 0 nao roda. Se rodasse, as 9 regs de forfait (41..121) lancariam % de 58105 para todo empregado (ver sensibilidade).
- **S4**: piso da CNPS vale com matriz vazia (Suman 16/10). Define o cenario 2 (salario zero).
- **S5/S8**: piso/teto anuais divididos por 12; IRPP anualiza x12, aplica a tabela e divide por 12; FLOOR(x+0,5) so no fim.
- **S9**: TFE (reg 261, sem formula) arredondada ao XAF inteiro.
- **Dados**: 58206 no Dev e 0/1, entao a "reducao 50%" do cenario 9 entra como 0 (nao existe no Dev). Cenario 6: o codigo 21600 do v4 nao casa com `2164%` do Dev; usado 21640 (mesmo valor). Cenario 8: 0 dependentes (como no v4); o cenario 12 (extra) repete com 6.
- **CNPS EE**: o Dev lanca os 3,5% do empregado em 2550/6020 e os 7,5% PFM em 2551/2610 (C1). As linhas comparam por papel (3,5% = EE), nao por conta.
- **v5:** o Liquido desta tabela NAO desconta o PSA de 400 (comparar.py inalterado); o liquido do v5 com PSA esta em `../chad-design-blueprint-claude-v5/VALIDATION.md`. O PSA nao existe no Dev.
- Liquido = remuneracao em dinheiro (62xxx) - CNPS EE - IRPP - deducoes 21xxx (mesma conta do v4). Custo da empresa = 62xxx + beneficios 65xxx/79xxx + CNPS ER (PFM, PVID, AT/MP) + TFE + TAFP.

## Cenario 1 Base 350.000
**Bate ao franco em todas as 22 linhas** (bases, IRPP, TFE, TAFP, CNPS EE/ER, deducoes, liquido, custo da empresa).

| Linha | Nosso | Dev |
| --- | ---: | ---: |
| IRPP (2552+2592) | 28.464 | 28.464 |
| TFE | 26.250 | 26.250 |
| TAFP | 4.200 | 4.200 |
| CNPS EE 3,5% (v5 conta 2551 / Dev conta 2550) | 12.250 | 12.250 |
| Liquido | 309.286 | 309.286 |
| Custo da empresa | 438.200 | 438.200 |

## Cenario 2 Salario zero
10 de 22 linhas diferem; as outras bateram.

| Linha | Nosso | Dev | Dif. (Dev - nosso) | Causa |
| --- | ---: | ---: | ---: | --- |
| Base 58550 (CNPS segurado) | 0 | 60.000 | 60.000 | reg 9148161 sem condicao 58130>0: o piso da CNPS vale com salario zero (COMPARACAO B1 #16) |
| Deducao CNPS EE no IRPP (v5 58141 / Dev 58100) | 0 | -2.100 | -2.100 | reg 9148161 sem condicao 58130>0: o piso da CNPS vale com salario zero (COMPARACAO B1 #16) |
| IRPP (2552+2592) | 0 | 0 | 0 |  |
| TFE | 0 | 0 | 0 |  |
| TAFP | 0 | 0 | 0 |  |
| CNPS EE 3,5% (v5 conta 2551 / Dev conta 2550) | 0 | 2.100 | 2.100 | reg 9148161 sem condicao 58130>0: o piso da CNPS vale com salario zero (COMPARACAO B1 #16) |
| CNPS ER PFM 7,5% (v5 2550 / Dev 2551) | 0 | 4.500 | 4.500 | reg 9148161 sem condicao 58130>0: o piso da CNPS vale com salario zero (COMPARACAO B1 #16) |
| CNPS ER PVID 5% (2537) | 0 | 3.000 | 3.000 | reg 9148161 sem condicao 58130>0: o piso da CNPS vale com salario zero (COMPARACAO B1 #16) |
| CNPS ER AT/MP 4% (2560) | 0 | 2.400 | 2.400 | reg 9148161 sem condicao 58130>0: o piso da CNPS vale com salario zero (COMPARACAO B1 #16) |
| 58106 limite de reporte | 0 | 60.000 | 60.000 | reg 9148161 sem condicao 58130>0: o piso da CNPS vale com salario zero (COMPARACAO B1 #16) |
| 58131 taxa total CNPS | 0 | 20 | 20 | v5 9148053 banda 6: taxa 20 em 58131 so com salario segurado (58550 > 0) |
| Liquido | 0 | -2.100 | -2.100 | reg 9148161 sem condicao 58130>0: o piso da CNPS vale com salario zero (COMPARACAO B1 #16) |
| Custo da empresa | 0 | 9.900 | 9.900 | reg 9148161 sem condicao 58130>0: o piso da CNPS vale com salario zero (COMPARACAO B1 #16) |

## Cenario 3 13o salario
**Bate ao franco em todas as 22 linhas** (bases, IRPP, TFE, TAFP, CNPS EE/ER, deducoes, liquido, custo da empresa).

| Linha | Nosso | Dev |
| --- | ---: | ---: |
| IRPP (2552+2592) | 75.750 | 75.750 |
| TFE | 52.500 | 52.500 |
| TAFP | 8.400 | 8.400 |
| CNPS EE 3,5% (v5 conta 2551 / Dev conta 2550) | 17.500 | 17.500 |
| Liquido | 606.750 | 606.750 |
| Custo da empresa | 843.400 | 843.400 |

## Cenario 4 Moradia real 50.000 (teto 120.000)
5 de 22 linhas diferem; as outras bateram.

| Linha | Nosso | Dev | Dif. (Dev - nosso) | Causa |
| --- | ---: | ---: | ---: | --- |
| Base 58105 (caixa bruto) | 600.000 | 650.000 | 50.000 | regs 9148041..121: forfait % x 58105 em vez de MIN(real; teto) (B1 #20); 58105 inclui 65%%% (B1 #22, D1) |
| Base 58008 (bruto IRPP) | 650.000 | 730.000 | 80.000 | regs 9148041..121: forfait % x 58105 em vez de MIN(real; teto) (B1 #20); 58105 inclui 65%%% (B1 #22, D1) |
| Base 58552 (renda tributavel IRPP) | 632.500 | 712.500 | 80.000 | regs 9148041..121: forfait % x 58105 em vez de MIN(real; teto) (B1 #20); 58105 inclui 65%%% (B1 #22, D1) |
| IRPP (2552+2592) | 65.750 | 81.750 | 16.000 | regs 9148041..121: forfait % x 58105 em vez de MIN(real; teto) (B1 #20); 58105 inclui 65%%% (B1 #22, D1) |
| TFE | 48.750 | 48.750 | 0 |  |
| TAFP | 7.800 | 7.800 | 0 |  |
| CNPS EE 3,5% (v5 conta 2551 / Dev conta 2550) | 17.500 | 17.500 | 0 |  |
| Liquido | 516.750 | 500.750 | -16.000 | regs 9148041..121: forfait % x 58105 em vez de MIN(real; teto) (B1 #20); 58105 inclui 65%%% (B1 #22, D1) |
| Custo da empresa | 789.050 | 789.050 | 0 |  |

## Cenario 5 Indenizacao individual 900.000
4 de 22 linhas diferem; as outras bateram.

| Linha | Nosso | Dev | Dif. (Dev - nosso) | Causa |
| --- | ---: | ---: | ---: | --- |
| Base 58008 (bruto IRPP) | 1.200.000 | 300.000 | -900.000 | reg 9148131: 6218% fora do IRPP sempre (B1 #7); v4 tributa a individual |
| Base 58552 (renda tributavel IRPP) | 1.189.500 | 289.500 | -900.000 | reg 9148131: 6218% fora do IRPP sempre (B1 #7); v4 tributa a individual |
| IRPP (2552+2592) | 208.600 | 23.397 | -185.203 | reg 9148131: 6218% fora do IRPP sempre (B1 #7); v4 tributa a individual |
| TFE | 22.500 | 22.500 | 0 |  |
| TAFP | 3.600 | 3.600 | 0 |  |
| CNPS EE 3,5% (v5 conta 2551 / Dev conta 2550) | 10.500 | 10.500 | 0 |  |
| Liquido | 980.900 | 1.166.103 | 185.203 | reg 9148131: 6218% fora do IRPP sempre (B1 #7); v4 tributa a individual |
| Custo da empresa | 1.275.600 | 1.275.600 | 0 |  |

## Cenario 6 Aposentadoria compl. 30.000 (teto 14.000)
4 de 22 linhas diferem; as outras bateram.

| Linha | Nosso | Dev | Dif. (Dev - nosso) | Causa |
| --- | ---: | ---: | ---: | --- |
| Deducao aposentadoria (v5 58142 / Dev 58101) | -14.000 | -30.000 | -16.000 | reg 9148181: 2164% dedutivel sem teto de 3,5% (B1 #8) |
| Base 58552 (renda tributavel IRPP) | 372.000 | 356.000 | -16.000 | reg 9148181: 2164% dedutivel sem teto de 3,5% (B1 #8) |
| IRPP (2552+2592) | 32.060 | 30.380 | -1.680 | reg 9148181: 2164% dedutivel sem teto de 3,5% (B1 #8) |
| TFE | 30.000 | 30.000 | 0 |  |
| TAFP | 4.800 | 4.800 | 0 |  |
| CNPS EE 3,5% (v5 conta 2551 / Dev conta 2550) | 14.000 | 14.000 | 0 |  |
| Liquido | 323.940 | 325.620 | 1.680 | reg 9148181: 2164% dedutivel sem teto de 3,5% (B1 #8) |
| Custo da empresa | 500.800 | 500.800 | 0 |  |

## Cenario 7 Transporte 120.000 a todos
15 de 22 linhas diferem; as outras bateram.

| Linha | Nosso | Dev | Dif. (Dev - nosso) | Causa |
| --- | ---: | ---: | ---: | --- |
| Base 58130 (bruto CNPS) | 300.000 | 330.000 | 30.000 | v5 9148051: transporte inteiro fora da CNPS (guia CNPS p. 8; a confirmar com o usuario); o Dev tira so a parte isenta (58104) |
| Base 58550 (CNPS segurado) | 300.000 | 330.000 | 30.000 | v5 9148051: transporte inteiro fora da CNPS (guia CNPS p. 8; a confirmar com o usuario); o Dev tira so a parte isenta (58104) |
| Base 58563 (TFE) | 420.000 | 330.000 | -90.000 | regs 9148141/151 incluem 58104 (transporte isento sai da base TFE/TAFP) (B1 #28); v4 mantem o transporte (Art. 189) |
| Base 58534 (TAFP) | 420.000 | 330.000 | -90.000 | regs 9148141/151 incluem 58104 (transporte isento sai da base TFE/TAFP) (B1 #28); v4 mantem o transporte (Art. 189) |
| Deducao CNPS EE no IRPP (v5 58141 / Dev 58100) | -10.500 | -11.550 | -1.050 | v5 9148051: transporte inteiro fora da CNPS (guia CNPS p. 8; a confirmar com o usuario); o Dev tira so a parte isenta (58104) |
| Base 58552 (renda tributavel IRPP) | 319.500 | 318.450 | -1.050 | v5 9148051: transporte inteiro fora da CNPS (guia CNPS p. 8; a confirmar com o usuario); o Dev tira so a parte isenta (58104) |
| IRPP (2552+2592) | 26.548 | 26.437 | -111 | v5 9148051: transporte inteiro fora da CNPS (guia CNPS p. 8; a confirmar com o usuario); o Dev tira so a parte isenta (58104) |
| TFE | 31.500 | 24.750 | -6.750 | regs 9148141/151 incluem 58104 (transporte isento sai da base TFE/TAFP) (B1 #28); v4 mantem o transporte (Art. 189) |
| TAFP | 5.040 | 3.960 | -1.080 | regs 9148141/151 incluem 58104 (transporte isento sai da base TFE/TAFP) (B1 #28); v4 mantem o transporte (Art. 189) |
| CNPS EE 3,5% (v5 conta 2551 / Dev conta 2550) | 10.500 | 11.550 | 1.050 | v5 9148051: transporte inteiro fora da CNPS (guia CNPS p. 8; a confirmar com o usuario); o Dev tira so a parte isenta (58104) |
| CNPS ER PFM 7,5% (v5 2550 / Dev 2551) | 22.500 | 24.750 | 2.250 | v5 9148051: transporte inteiro fora da CNPS (guia CNPS p. 8; a confirmar com o usuario); o Dev tira so a parte isenta (58104) |
| CNPS ER PVID 5% (2537) | 15.000 | 16.500 | 1.500 | v5 9148051: transporte inteiro fora da CNPS (guia CNPS p. 8; a confirmar com o usuario); o Dev tira so a parte isenta (58104) |
| CNPS ER AT/MP 4% (2560) | 12.000 | 13.200 | 1.200 | v5 9148051: transporte inteiro fora da CNPS (guia CNPS p. 8; a confirmar com o usuario); o Dev tira so a parte isenta (58104) |
| Liquido | 382.952 | 382.013 | -939 | v5 9148051: transporte inteiro fora da CNPS (guia CNPS p. 8; a confirmar com o usuario); o Dev tira so a parte isenta (58104) |
| Custo da empresa | 506.040 | 503.160 | -2.880 | v5 9148051: transporte inteiro fora da CNPS (guia CNPS p. 8; a confirmar com o usuario); o Dev tira so a parte isenta (58104) | regs 9148141/151 incluem 58104 (transporte isento sai da base TFE/TAFP) (B1 #28); v4 mantem o transporte (Art. 189) |

## Cenario 8 Abono familiar 30.000 (0 dependentes)
7 de 22 linhas diferem; as outras bateram.

| Linha | Nosso | Dev | Dif. (Dev - nosso) | Causa |
| --- | ---: | ---: | ---: | --- |
| Base 58563 (TFE) | 330.000 | 300.000 | -30.000 | regs 9148141/151: 6276% fora da TFE/TAFP (B1 #28); v4 inclui |
| Base 58534 (TAFP) | 330.000 | 300.000 | -30.000 | regs 9148141/151: 6276% fora da TFE/TAFP (B1 #28); v4 inclui |
| IRPP (2552+2592) | 26.548 | 26.547 | -1 | faixas do IRPP do Dev com limite x.99: 1 XAF a menos quando o IRPP cai em meio franco; v5 grava 800.000 (art. 1-IV) |
| TFE | 24.750 | 22.500 | -2.250 | regs 9148141/151: 6276% fora da TFE/TAFP (B1 #28); v4 inclui |
| TAFP | 3.960 | 3.600 | -360 | regs 9148141/151: 6276% fora da TFE/TAFP (B1 #28); v4 inclui |
| CNPS EE 3,5% (v5 conta 2551 / Dev conta 2550) | 10.500 | 10.500 | 0 |  |
| Liquido | 292.952 | 292.953 | 1 | faixas do IRPP do Dev com limite x.99: 1 XAF a menos quando o IRPP cai em meio franco; v5 grava 800.000 (art. 1-IV) |
| Custo da empresa | 408.210 | 405.600 | -2.610 | regs 9148141/151: 6276% fora da TFE/TAFP (B1 #28); v4 inclui |

## Cenario 9 Entidade com reducao 50% TFE/TAFP
3 de 22 linhas diferem; as outras bateram.

| Linha | Nosso | Dev | Dif. (Dev - nosso) | Causa |
| --- | ---: | ---: | ---: | --- |
| IRPP (2552+2592) | 28.464 | 28.464 | 0 |  |
| TFE | 13.125 | 26.250 | 13.125 | reg 9148261/251: so isencao total da TFE (58206=1); sem 50% e sem reducao da TAFP (B1 #30) |
| TAFP | 2.100 | 4.200 | 2.100 | reg 9148261/251: so isencao total da TFE (58206=1); sem 50% e sem reducao da TAFP (B1 #30) |
| CNPS EE 3,5% (v5 conta 2551 / Dev conta 2550) | 12.250 | 12.250 | 0 |  |
| Liquido | 309.286 | 309.286 | 0 |  |
| Custo da empresa | 422.975 | 438.200 | 15.225 | reg 9148261/251: so isencao total da TFE (58206=1); sem 50% e sem reducao da TAFP (B1 #30) |

## Cenario 10 Jovem graduado, mes 30
5 de 22 linhas diferem; as outras bateram.

| Linha | Nosso | Dev | Dif. (Dev - nosso) | Causa |
| --- | ---: | ---: | ---: | --- |
| Base 58563 (TFE) | 0 | 350.000 | 350.000 | v5 9148081/082: parte da folha do jovem diplomado < 35 fora da TF/TA (art. 188-10, 174-3; flag 58219); o Dev nao tem |
| Base 58534 (TAFP) | 0 | 350.000 | 350.000 | v5 9148081/082: parte da folha do jovem diplomado < 35 fora da TF/TA (art. 188-10, 174-3; flag 58219); o Dev nao tem |
| IRPP (2552+2592) | 0 | 0 | 0 |  |
| TFE | 0 | 26.250 | 26.250 | v5 9148081/082: parte da folha do jovem diplomado < 35 fora da TF/TA (art. 188-10, 174-3; flag 58219); o Dev nao tem |
| TAFP | 0 | 4.200 | 4.200 | v5 9148081/082: parte da folha do jovem diplomado < 35 fora da TF/TA (art. 188-10, 174-3; flag 58219); o Dev nao tem |
| CNPS EE 3,5% (v5 conta 2551 / Dev conta 2550) | 12.250 | 12.250 | 0 |  |
| Liquido | 337.750 | 337.750 | 0 |  |
| Custo da empresa | 407.750 | 438.200 | 30.450 | v5 9148081/082: parte da folha do jovem diplomado < 35 fora da TF/TA (art. 188-10, 174-3; flag 58219); o Dev nao tem |

## Cenario 11 (extra) Nao residente 800.000
9 de 22 linhas diferem; as outras bateram.

| Linha | Nosso | Dev | Dif. (Dev - nosso) | Causa |
| --- | ---: | ---: | ---: | --- |
| Deducao CNPS EE no IRPP (v5 58141 / Dev 58100) | 0 | -17.500 | -17.500 | reg 9148171 sem flags 58202-58204: NR paga todos os ramos (B1 #12, C2) |
| Base 58552 (renda tributavel IRPP) | 800.000 | 782.500 | -17.500 | reg 9148171 sem flags 58202-58204: NR paga todos os ramos (B1 #12, C2) |
| IRPP (2552+2592) | 101.750 | 144.000 | 42.250 | reg 9148171 sem flags 58202-58204: NR paga todos os ramos (B1 #12, C2) | e: v5 tributa o nao residente pela tabela progressiva (CGI art. 44-II-2, 847); o Dev usa 18% (art. 116). Aqui o comparar.py roda o nosso com os ramos da CNPS desligados (flags do v4); no v5 o padrao e todos os ramos (VALIDATION cenario 11) |
| TFE | 60.000 | 60.000 | 0 |  |
| TAFP | 9.600 | 9.600 | 0 |  |
| CNPS EE 3,5% (v5 conta 2551 / Dev conta 2550) | 0 | 17.500 | 17.500 | reg 9148171 sem flags 58202-58204: NR paga todos os ramos (B1 #12, C2) |
| CNPS ER PFM 7,5% (v5 2550 / Dev 2551) | 0 | 37.500 | 37.500 | reg 9148171 sem flags 58202-58204: NR paga todos os ramos (B1 #12, C2) |
| CNPS ER PVID 5% (2537) | 0 | 25.000 | 25.000 | reg 9148171 sem flags 58202-58204: NR paga todos os ramos (B1 #12, C2) |
| CNPS ER AT/MP 4% (2560) | 0 | 20.000 | 20.000 | reg 9148171 sem flags 58202-58204: NR paga todos os ramos (B1 #12, C2) |
| Liquido | 698.250 | 638.500 | -59.750 | reg 9148171 sem flags 58202-58204: NR paga todos os ramos (B1 #12, C2) | e: v5 tributa o nao residente pela tabela progressiva (CGI art. 44-II-2, 847); o Dev usa 18% (art. 116). Aqui o comparar.py roda o nosso com os ramos da CNPS desligados (flags do v4); no v5 o padrao e todos os ramos (VALIDATION cenario 11) |
| Custo da empresa | 869.600 | 952.100 | 82.500 | reg 9148171 sem flags 58202-58204: NR paga todos os ramos (B1 #12, C2) |

## Cenario 12 (extra) Abono familiar 30.000 com 6 dependentes
7 de 22 linhas diferem; as outras bateram.

| Linha | Nosso | Dev | Dif. (Dev - nosso) | Causa |
| --- | ---: | ---: | ---: | --- |
| Base 58563 (TFE) | 330.000 | 300.000 | -30.000 | regs 9148141/151: 6276% fora da TFE/TAFP (B1 #28); v4 inclui |
| Base 58534 (TAFP) | 330.000 | 300.000 | -30.000 | regs 9148141/151: 6276% fora da TFE/TAFP (B1 #28); v4 inclui |
| IRPP (2552+2592) | 23.398 | 23.397 | -1 | faixas do IRPP do Dev com limite x.99: 1 XAF a menos quando o IRPP cai em meio franco; v5 grava 800.000 (art. 1-IV) |
| TFE | 24.750 | 22.500 | -2.250 | regs 9148141/151: 6276% fora da TFE/TAFP (B1 #28); v4 inclui |
| TAFP | 3.960 | 3.600 | -360 | regs 9148141/151: 6276% fora da TFE/TAFP (B1 #28); v4 inclui |
| CNPS EE 3,5% (v5 conta 2551 / Dev conta 2550) | 10.500 | 10.500 | 0 |  |
| Liquido | 296.102 | 296.103 | 1 | faixas do IRPP do Dev com limite x.99: 1 XAF a menos quando o IRPP cai em meio franco; v5 grava 800.000 (art. 1-IV) |
| Custo da empresa | 408.210 | 405.600 | -2.610 | regs 9148141/151: 6276% fora da TFE/TAFP (B1 #28); v4 inclui |

## Resumo

- Cenarios 1 a 10 que batem ao franco em todas as linhas: **2 de 10**.

| Cenario | Dif. IRPP | Dif. liquido | Maior diferenca (linha, XAF) |
| --- | ---: | ---: | --- |
| 1 Base 350.000 | 0 | 0 | - |
| 2 Salario zero | 0 | -2.100 | 58106 limite de reporte: 60.000 |
| 3 13o salario | 0 | 0 | - |
| 4 Moradia real 50.000 (teto 120.000) | 16.000 | -16.000 | IRPP (2552+2592): 16.000 |
| 5 Indenizacao individual 900.000 | -185.203 | 185.203 | IRPP (2552+2592): -185.203 |
| 6 Aposentadoria compl. 30.000 (teto 14.000) | -1.680 | 1.680 | Deducao aposentadoria (v5 58142 / Dev 58101): -16.000 |
| 7 Transporte 120.000 a todos | -111 | -939 | TFE: -6.750 |
| 8 Abono familiar 30.000 (0 dependentes) | -1 | 1 | Custo da empresa: -2.610 |
| 9 Entidade com reducao 50% TFE/TAFP | 0 | 0 | Custo da empresa: 15.225 |
| 10 Jovem graduado, mes 30 | 0 | 0 | Custo da empresa: 30.450 |
| 11 (extra) Nao residente 800.000 | 42.250 | -59.750 | Custo da empresa: 82.500 |
| 12 (extra) Abono familiar 30.000 com 6 dependentes | -1 | 1 | Custo da empresa: -2.610 |

## Sensibilidade (so o Dev; cenarios 1 e 2)

| Suposicao alterada | Cenario | 58105 | 58008 | IRPP | CNPS EE | TFE |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| S3 desligada (regulacao com base 0 executa) | 1 Base 350.000 | 350.000 | 584.500 | 56.337 | 12.250 | 26.250 |
| S3 desligada (regulacao com base 0 executa) | 2 Salario zero | 0 | 0 | 0 | 2.100 | 0 |
| S4 desligada (piso nao vale com matriz vazia) | 1 Base 350.000 | 350.000 | 350.000 | 28.464 | 12.250 | 26.250 |
| S4 desligada (piso nao vale com matriz vazia) | 2 Salario zero | 0 | 0 | 0 | 0 | 0 |

Com S3 desligada o Dev tributaria forfait de moradia, veiculo etc. para quem nao tem beneficio; a configuracao so e viavel se o engine pula regulacao com base zero (ponto a confirmar com o Ram). Com S4 desligada o cenario 2 deixa de gerar CNPS e passa a bater com o nosso.

## O que a simulacao nao cobre
- Proporcionalidade, retro e gross-up (`$$`), igual ao VALIDATION do v4. Nao e o engine real: o resultado vale sob as suposicoes S1..S12.
- Nao decide quem esta certo; cada diferenca aponta a regra a resolver pela lei (ver COMPARACAO.md).

## Bloco de prova
- **Pedido -> resposta:** 10 cenarios (+2 extras) x linhas de base, imposto, CNPS, liquido e custo nos dois motores; valor, diferenca e causa por linha; resumo acima.
- **Fontes:** `td.json` (Drive; igual ao CT-A-588 conforme COMPARACAO secao A), `_build_v5.py`, `COMPARACAO.md`. Nenhuma lei lida.
- **Teste:** o motor do v4 reproduz os resultados do `VALIDATION.md`; o motor do Dev reproduz 28.464 de IRPP no cenario 1, igual ao v4.
- **Confianca:** cerca de 85% nos numeros do Dev (dependem das suposicoes S1..S12, nao confirmadas no engine); 98% nos do v4.

## Quem mexeu
| Data | Frente | O que |
| --- | --- | --- |
| 2026-10-30 | chade | simulacao criada (`sim_dev.py`, `comparar.py`) |
| 2026-11-01 | chade | rodado contra o v5 (`rodar_comparar_v5.py`; comparar.py e sim_dev.py copias identicas) |

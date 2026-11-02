# Conferência dos DRAFT-R5 (rodada 5), Colômbia — 2026-11-02

Ligado a [[CONFERENCIA]], [[TABELA-RODADA5]] e [[mudancas-RODADA5]]. Gerado por `revisao/rodada5/scripts/r5_crosscheck.py` em 2026-11-02 09:46 (adaptado de `final/scripts/release_crosscheck.py`). Base de comparação: os finais de 30/10 (desde o release de 02/11 em `final/_historico/2026-10-30/`, md5 no `MD5-FINAIS.txt` de lá), só lidos.

## O que foi provado

1. Cada DRAFT abre (openpyxl só leitura / python-docx) e o zip tem as mesmas partes do final; só `styles.xml` e as abas editadas (xlsx) ou `document.xml` e `settings.xml` (docx) diferem; fora das células a estrutura das abas não mudou.
2. Diff célula a célula (valor e fórmula de todas as células de todas as abas): nenhuma célula fora da lista mudou e cada célula da lista tem o texto declarado. CCG: parágrafos do DRAFT com as alterações aceitas × final; só mudam os parágrafos declarados, a linha nova do Version Control e o parágrafo apagado declarado.
3. Formatação: célula fora da lista com o mesmo estilo; célula da lista com fundo `FFDDEBF7` e o resto da formatação igual. CCG: todas as alterações controladas são do autor "Wallisson Gomes".
4. Zero erros de fórmula. 5. Cada valor novo está no DRAFT. 6. Finais intactos (md5 antes e depois).

## Resultado

| Artefato | DRAFT-R5 | Final de partida | Mudanças | Medidas | Falhas | Veredito |
|---|---|---|---|---|---|---|
| WTC | `CO-WTC-001-v1.8-DRAFT-R5.xlsx` | `final/CO-WTC-001-v1.7.xlsx` | 65 | abas 6; partes iguais byte a byte 29; células declaradas conferidas 65; erros de fórmula 0; células comparadas 67660; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | PASS |
| DD | `CO-DD-001-v1.5-DRAFT-R5.xlsx` | `final/CO-DD-001-v1.4.xlsx` | 12 | abas 8; partes iguais byte a byte 44; células declaradas conferidas 12; erros de fórmula 0; células comparadas 65690; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | PASS |
| NE | `CO-DIAN-001-NominaElectronica-Spec-v1.2-DRAFT-R5.xlsx` | `final/specs/CO-DIAN-001-NominaElectronica-Spec.xlsx` | 9 | abas 9; partes iguais byte a byte 12; células declaradas conferidas 9; erros de fórmula 0; células comparadas 54598; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | PASS |
| F220 | `CO-DIAN-004-Formulario220-Spec-v1.2-DRAFT-R5.xlsx` | `final/specs/CO-DIAN-004-Formulario220-Spec.xlsx` | 27 | abas 9; partes iguais byte a byte 27; células declaradas conferidas 27; erros de fórmula 0; células comparadas 55032; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | PASS |
| F2276 | `CO-DIAN-005-Formato2276-Spec-v1.2-DRAFT-R5.xlsx` | `final/specs/CO-DIAN-005-Formato2276-Spec.xlsx` | 22 | abas 9; partes iguais byte a byte 10; células declaradas conferidas 22; erros de fórmula 0; células comparadas 54770; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | PASS |
| CES006 | `CO-CESANTIAS-006-ConsignacionAnual-Spec-v1.2-DRAFT-R5.xlsx` | `final/specs/CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx` | 7 | abas 9; partes iguais byte a byte 32; células declaradas conferidas 7; erros de fórmula 0; células comparadas 54870; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | PASS |
| PILA003 | `CO-PILA-003-AportesSeguridadSocial-Spec-v1.2-DRAFT-R5.xlsx` | `final/specs/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx` | 14 | abas 9; partes iguais byte a byte 10; células declaradas conferidas 14; erros de fórmula 0; células comparadas 54637; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | PASS |
| PAYSLIP | `CO_Compliance_Payslip_Generator-v1.3-DRAFT-R5.xlsx` | `final/CO_Compliance_Payslip_Generator.xlsx` | 14 | abas 8; partes iguais byte a byte 34; células declaradas conferidas 14; erros de fórmula 0; células comparadas 21724; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | PASS |
| CCG | `CO-CCG-001-v1.6-DRAFT-R5.docx` | `final/CO-CCG-001-v1.5.docx` | 80 | alterações controladas (w:ins/w:del) 205; parágrafos (final / DRAFT aceito) 7975 / 7978; edições declaradas conferidas 80 | 0 | PASS |
| SIR | `CO-SIR-001-v1.3-DRAFT-R5-texto.md` | `final/CO-SIR-001-v1.2-texto-final.md` | 2 | linhas dos blocos 15; linhas mudadas 2 | 0 | PASS |

Finais intactos: sim (md5 = MD5-FINAIS.txt).

**Veredito: PASS** (0 falhas).

## Falhas

Nenhuma.

## Oráculo (A-1: tetos anuais pelo acumulado)

`revisao/rodada5/scripts/oracle_r5_ytd.py` roda o `oracle/oracle_v2.py` **sem alterar o código**: troca, só durante a chamada, o limite mensal lido do parâmetro (790 e 1.340 UVT ÷ 12) pelo saldo anual não usado. Premissa: mesmo pagamento mensal desde 1/1/2026, sem outra renda isenta nem deducao; prima de servicos nao incluida no consumo. Casos `monthly` com retenção rodados: 51; limitados pelo 1/12: 18; sem efeito: 33.

| Caso | Limite que agia | Retenção 1/12 | Retenção acumulado (mês 1) | Mês da simulação | Retenção acumulado nesse mês | Mês em que o teto anual passa a limitar |
|---|---|---|---|---|---|---|
| C09 | 790/12 | 4,666,697.69 | 3,701,335.83 | 3 | 3,701,335.83 | 7 |
| C10 | 790/12 | 4,648,208.44 | 3,687,468.89 | 3 | 3,687,468.89 | 7 |
| C11 | 790/12 | 5,172,849.61 | 4,080,949.77 | 3 | 4,080,949.77 | 7 |
| C12 | 790/12 | 5,153,204.76 | 4,066,216.13 | 3 | 4,066,216.13 | 7 |
| C13 | 790/12 | 6,156,263.21 | 4,818,509.97 | 3 | 4,818,509.97 | 6 |
| C14 | 790/12 | 6,677,437.30 | 5,209,390.53 | 3 | 5,209,390.53 | 6 |
| C15 | 790/12 | 6,654,325.65 | 5,192,056.80 | 3 | 5,192,056.80 | 6 |
| C16 | 790/12 | 1,819,910.29 | 1,670,011.26 | 3 | 1,670,011.26 | 11 |
| C17 | 790/12 | 1,819,910.54 | 1,670,011.46 | 3 | 1,670,011.46 | 11 |
| C19 | 790/12 | 9,334,404.62 | 7,142,127.02 | 3 | 7,142,127.02 | 5 |
| C20 | 790/12 | 9,684,404.62 | 7,389,627.02 | 3 | 7,389,627.02 | 5 |
| C21 | 790/12 | 12,398,488.38 | 9,392,157.47 | 3 | 9,392,157.47 | 4 |
| C22 | 790/12 | 3,330,381.25 | 2,802,864.49 | 3 | 2,802,864.49 | 8 |
| C23 | 790/12 | 18,741,726.43 | 13,988,283.09 | 3 | 16,855,453.02 | 3 |
| R07 | 790/12 1340/12 | 7,341,792.90 | 4,519,774.80 | 3 | 4,519,774.80 | 7 |
| R08 | 790/12 | 2,454,604.60 | 2,146,032.00 | 3 | 2,146,032.00 | 10 |
| RC05 | 790/12 | 4,994,989.65 | 92,049.30 | 9 | 3,947,554.80 | — |
| RC07 | 790/12 | 2,250,764.60 | 1,993,152.00 | 8 | 1,993,152.00 | 10 |

Exemplos do CCG recalculados pelo oráculo (premissa escrita no CCG; bônus só no mês do exemplo):

| Exemplo | 1/12 (hoje) | Acumulado (DRAFT) | 25% isento | Consumo antes do mês |
|---|---|---|---|---|
| T105 (Ex. 4, set/2026: 8.000.000 + bonus 20.000.000 com pacto) | 4,994,989.65 | 3,947,554.80 | 6,622,000.00 | 14,560,000.00 |
| T180 (out/2026: 6.000.000 + bonus habitual 12.000.000) | 1,945,004.60 | 1,763,832.00 | 4,095,000.00 | 12,420,000.00 |
| T183 C3 (mesmo caso com pacto nao salarial) | 2,126,444.60 | 1,899,912.00 | 4,257,000.00 | 12,420,000.00 |
| T239 (integral 25.000.000, mes de jan a jul) | 3,984,199.65 | 3,243,282.00 | 5,856,250.00 | 35,137,500.00 |

RC05 = exemplo T105 do CCG; RC07 = exemplo do Payslip (ago/2026). Os valores do oráculo batem com as contas do `apply_r5.py` (assert) e com os DRAFTs: T105 3.947.554,80; T180 1.763.832,00; T183 (pacto) 1.899.912,00; T239 3.243.282,00; Payslip 1.993.152,00.

A-2 (cesantías de não residente): o oráculo não modela retenção de não residente (não há ET 408 no código) — não aplicável.

## Contas de A-1 refeitas (passo a passo; conferidas por assert no `apply_r5.py` e pelo oráculo)

UVT 2026 = 52.374 (CCG T215 "Tax unit COP 52,374"; Res. DIAN 000238/2025). 790 UVT = 41,375,460; 1.340 UVT = 70,181,160. Tabela ET 383: >150–360 UVT: (base − 150 UVT) × 28% + 10 UVT; >360–640: (base − 360 UVT) × 33% + 69 UVT.

**T105 (Exemplo 4, set/2026; salário 8.000.000 desde 1/1 + bônus 20.000.000 com pacto).**
1. (C) do mês = 28.000.000 − 9% × 16.800.000 (IBC após o clamp de 40%) = 26.488.000; 25% = 6.622.000.
2. Consumo jan–ago: (8.000.000 − 9% × 8.000.000) × 25% = 1.820.000 por mês × 8 = 14.560.000.
3. Saldo do teto anual = 41.375.460 − 14.560.000 = 26.815.460 ≥ 6.622.000 → isenção 6.622.000. 40%: 10.595.200 ≥ 6.622.000. 1.340 UVT: 14.560.000 + 6.622.000 = 21.182.000 ≤ 70.181.160.
4. Base = 26.488.000 − 6.622.000 = 19.866.000 = 379.3103 UVT → faixa 33%. Retenção = (19.866.000 − 360 × 52.374) × 33% + 69 × 52.374 = 1.011.360 × 0,33 + 3.613.806 = **3,947,554.80** (igual ao lote A). Hoje: 4.994.989,65 (−1.047.434,85).
5. Se o prêmio de serviços de junho (≈ 4.000.000, retido à parte) entrar no consumo: +1.000.000; saldo 25.815.460 ainda ≥ 6.622.000 → mesmo resultado.

**T180 (out/2026; salário 6.000.000 desde 1/1 + bônus habitual 12.000.000).**
1. (C) do mês = 18.000.000 − 9% × 18.000.000 = 16.380.000; 25% = 4.095.000.
2. Consumo jan–set: o salário de 6.000.000 fica abaixo de 4 SMMLV (7.003.620), então **não há FSP** nesses meses: (6.000.000 − 8% × 6.000.000) × 25% = 1.380.000 × 9 = **12.420.000**. O lote A usou 9 × 25% × 5.460.000 = 12.285.000 (FSP de 1% indevido nos meses sem bônus): diverge no consumo, não no resultado. Prevalece 12.420.000 (é o que está no DRAFT).
3. Saldo = 41.375.460 − 12.420.000 = 28.955.460 ≥ 4.095.000 → isenção 4.095.000. 40%: 6.552.000. 1.340 UVT: 16.515.000 ≤ 70.181.160.
4. Base = 16.380.000 − 4.095.000 = 12.285.000 = 234.5630 UVT → faixa 28%. Retenção = (12.285.000 − 7.856.100) × 28% + 523.740 = 4.428.900 × 0,28 + 523.740 = **1,763,832.00** (igual ao lote A). Hoje: 1.945.004,60 (−181.172,60). Líquido (T181) = 18.000.000 − 1.620.000 − 1.763.832 = 14.616.168,00.

**Achados na varredura (mesma decisão, fora da lista do lote A):** T183 C3 (mesmo caso com pacto: contribuições 972.000; (C) 17.028.000; isenção 4.257.000; base 12.771.000) = 1.899.912,00 (hoje 2.126.444,60); T239/T240 (integral 25.000.000, (C) 23.425.000; de janeiro a julho a isenção é 5.856.250; base 17.568.750, faixa 28%) = 3.243.282,00, líquido 20.181.718,00 (hoje 3.984.199,65 / 19.440.800,35; em agosto sobra 381.710 do teto e de setembro a dezembro a isenção é zero); Payslip (ago/2026, 19.200.000 todo mês; consumo jan–jul 7 × 4.368.000 = 30.576.000; isenção 4.368.000; base 13.104.000) = 1.993.152,00, líquido 15.478.848,00 (hoje 2.250.764,60 / 15.221.235,40).

## Simulações que mudariam (não alteradas; `final/simulations/` só lido)

**A-1 (tetos anuais pelo acumulado)** — o oráculo indica os casos em que o 1/12 limitava; nas abas de março o consumo é de 2 meses:
- `CO_Simulation_2026_10_30_V1.0.xlsx`: abas **C09–C17, C19–C23, R07 e R08** (linhas 69 isenção 25%, 70 teto 40%/1.340, benefícios aplicados, base gravável, base em UVT, imposto em UVT, retenção, líquido; mais o resumo/Checks/Formula comparison dessas abas). Fórmulas `p_RET_E25_UVT*p_UVT/12` e `p_RET_CAP_UVT*p_UVT/12` (linhas 69–70 de todas as 49 abas mensais) e a nota L69 ("operating convention") mudam em todas, mas o valor só muda nas listadas. Parameters B52 e B54 ("monthly = /12, operating convention"). README, ressalva 2.
- `Tax Simulations - Colombia.xlsx`: abas **1340 UVT CAP BINDING (R07), 25 PCT EXEMPT 790 UVT CAP (R08), ALL-INCLUSIVE SALARY (C22)** e **NON-SALARY BONUS (RC05 = T105, set/2026: 4.994.989,65 → 3.947.554,80, com o consumo jan–ago só do salário)**; linhas 51 e N57/N59 (rótulos "monthly = /12") de todas as abas de depuração; SERVICE BONUS SEPARATE READ (PB) e READ ME B5/B10 (o ponto aberto 2 — divisão do 790/12 entre salário e prêmio — deixa de existir: o teto é um só no ano); SUMMARY (linhas de R07, R08, C22, RC05).
- `Colombia Simulations - Law vs Provider.xlsx`: LAW SIMULATION C28 ("min(25% x residue, 790 UVT / 12)") e PROVIDER RESULT J28 (tolerância 3.447.953 × 3.447.955,50); a linha 28 e as dependentes (base, retenção) da folha de setembro precisam do consumo jan–ago de cada empregado — dado que não está nos agregados (regerar a partir do Test 4, sem abrir dado de cliente aqui).

**A-2 (cesantías sem retenção)** — nenhuma simulação tem não residente com cesantías: sem efeito.

## Decisões técnicas desta rodada (reversíveis) e o que ficou de fora

- WTC Y114–116: **BonificacionS (NIE139)** (o lote C dava ConceptoS ou BonificacionS sem motivo decisivo; ficou o padrão pedido). Y124–133 também BonificacionS.
- WTC V1: em vez de condicionar os dois valores ao pacto (texto do lote C), 'non-remunerative' → NS sempre; 'pacted' → NS com pacto, S sem pacto (o lote, ao pé da letra, faria o não remuneratório depender de pacto).
- WTC 346: além de V e da nota AB346, Q/R/S/U = Yes/No e Y condicional (PagoAlimentacionNS/S), como na família do carro; T/W/X já eram No.
- WTC A-2: N também → No (N1 = retenção), nota em D (explicação, com o 20% como opção desligada) e Z alinhado à citação de C22.
- DD H7: lista positiva sem os códigos 2 e 3 (o lote B não diz o que são); G95 e G106 ("bank-mediated") ficaram. A linha nova 98 ocupa a linha 104, que era a separação em branco antes do bloco seguinte.
- Payslip: incluído (não estava na lista de finais), porque o exemplo usava o 790/12 e a retenção muda (2.250.764,60 → 1.993.152,00).
- Fora da lista do lote, mesma decisão (A-1/A-2), aplicados para o DRAFT não se contradizer: CCG P1047, P1049, P1311, T169, T175, T181, T183, T202, T215, T219, T228, T239, T240; NE C21; 004 Population Rules C21, Example A33/C33/D33, K51 e linhas do Sample File; 005 Report Matrix A35, Population Rules D22, Example A33/C33/D33, K42 e Sample File; PILA-003 D17, Example A33, Sample File A86 (posições 381–389, mesmo comprimento) e A113.
- Res. 2708: a numeração de tabelas/parágrafos do lote B está uma acima da do python-docx (T12→T11, T35→T34, T34→T33, T52→T51, P416→P415, P433→P432); P432 (assunto morto) apagado com alteração controlada.
- Passo 0 (decidido pelo usuário em 2026-11-02, fonte DUR 1625 art. 1.2.1.22.43 e CE S4 rad. 24047/2021): o teto de 3.800 UVT de fundos voluntários e AFC/AVC (ET 126-1/126-4) é anual, pelo acumulado, sem ÷ 12. Varredura de "3,800", "199,021,200", "16,585,100", "÷ 12"/"/12" em todos os DRAFT-R5: só o CCG T228R5C1 dividia por 12; aplicados CCG T228R5C1, CCG P602 (regra e fonte) e WTC Tax Credit A34 (A33 é só a primeira metade da frase, sem ÷ 12; nada nas specs, DD e Payslip). Mais as descrições do Version Control (WTC D20, linha nova do CCG).
- Não feito (fora do decidido): CCG T112R3 (juros de moradia, 100 UVT/mês do ET 387 — regra mensal própria); skill `references/02-wtc.md` (10 linhas Y255–264, fora da lista de finais); base da exclusão para residentes em CCG T86R4C1 (fora do pedido no lote A).

# final/design — pacote para o time de Design (Colômbia, modelo da França)

Ligado a [[CONFERENCIA]] (pasta `2026-10-29-validacao-research`) e [[Colombia]]. Gerado em 2026-10-30 para o início do Design (~20/11). Em inglês, sem referências internas. Nada foi para Drive, ticket ou e-mail.

## Arquivos (versão vigente: v1_2, 2026-11-02)
| Arquivo | Equivale na França | Conteúdo | md5 |
|---|---|---|---|
| `CO_Regulation_Design_v1_2.md` | `FR_Regulation_Design_v1_0.md` | Partes 0–7: categorias especiais (9), flags/campos HR (DD v1.5) e constantes 2026 com norma, registro de contas, sequência de **57 regulações** (prefixo `9170`), detalhe com fórmula + norma + conferência por caso, matrizes, itens abertos, auto-revisão. v1.1: tetos de 790/1.340/3.800 UVT pelo acumulado do ano (`9170057`–`9170059`, leituras `_ytd`), cesantías sem retenção (item 10 fechado), matrizes do WTC v1.8, pontos de relatório (AuxilioNS/AuxilioS, tarifa ARL decimal na PILA, campos bancários por meio de pagamento); teto de 2.500 UVT do RAIS voluntário pelo acumulado (`58151`, resíduos de 02/11). | `f6482bac94af629c7bab05429c76b3d2` |
| `CO_Statutory_Research_Memo_v1_2.md` | `FR_Statutory_Research_Memo_v1_0.md` | 15 posições estatutárias com norma e confiança. v1.1: item 5 (tetos anuais pelo acumulado, 90%) e item 7 (cesantías de não residente sem retenção, 80%; 20% opcional desligado). | `bc527996fd86f8661c97969a3be77915` |
| `CO_Taxability_Matrices_v1_2.md` | `FR_Taxability_Matrices_v1_0.md` | 10 matrizes (A–J) + K classe salarial; achado estrutural `Yes/No`; registro consolidado das 298 linhas ativas. Gerado do WTC v1.8. | `5e27db3fd5d602590aa07f66bc392868` |
| `CO_Taxability_Perimeters_Extract_v1_2.csv` | `FR_Taxability_Perimeters_Extract_v1_0.csv` | Extração bruta das 405 linhas do WTC v1.8 (colunas N–X + classe V). | `4e5f8fd1a2721743ce870094e4975177` |
| `scripts/gen_matrices.py` | — | Gerador mecânico das matrizes e do CSV (`python -I gen_matrices.py <WTC> <outdir>`; versão do WTC lida do nome do arquivo; pacote `v1_1`). | — |
| `_historico/2026-10-30/` | — | Os quatro arquivos v1_0 de 30/10, só para comparação: Design `c5607b6a6170040d9d2779058e85ed80`, Memo `21ebdac18b8d3d97fdfb9ee553132a57`, Matrizes `8372dca77124fae27892ebd0d8b9175e`, CSV `dbfd07f1c4e424e3713fdc37cca67b63`. | — |

## Fontes
- **WTC v1.7 final** `final/CO-WTC-001-v1.7.xlsx` (md5 atual `d83d0e3c75b908f3e9d2e710b2c3eec2`; ver a última seção) — matrizes e CSV regenerados dele. Comparado com o DRAFT (`c71f0d35…`): colunas N–X idênticas (só textos das colunas D/F mudaram em 7 células, correções do Test 0) → CSV com o mesmo md5 e matrizes iguais, salvo a linha do md5 da fonte.
- **CCG v1.5 final** (`e6bea61992da…`, alterações aceitas, texto extraído inteiro inclusive tabelas e runs inseridos), DD v1.4 final (`8aa158e43bae…`), SIR v1.2, Payslip v1.2, specs v1.1; `final/test0/TEST0.md`; decisões `pesquisa-2026-10-30/TABELA-CONSOLIDADA.md`.

## Conferência
- Matrizes e CSV gerados por script a partir do WTC (sem transcrição manual).
- Cada fórmula da Parte 4 do design existe como fórmula viva em `final/simulations` e bate com o oráculo (2.137 linhas, 0 diferenças); os exemplos citados no design (C05, C22, D02, R06, T04/T06, T-A, I04, L08…) foram conferidos contra os resultados do oráculo.
- Varredura de texto: nenhuma menção a pipeline, agentes, rodadas, outros países, DRAFT ou à Circular 101/2025 (revogada) nos 4 arquivos do design.

## Reconferência contra os finais (30/10, depois do Test 0)
| Ponto | Situação |
|---|---|
| Circular 101/2025 revogada (T0-01) | Design não a cita; horas por Ley 2101 art. 3 e CST 161/179 |
| Dominical 80/90% (T0-02) | Já 80% → 90% em 1/7/2026 (constante `52505`) |
| FSP Ley 797 arts. 7–8 (T0-03) | Citação corrigida para "Law 100 arts. 20 and 27 (Law 797 arts. 7 and 8)" no design e nas simulações |
| RAIS voluntário fora do teto, ET 55 (T0-04) | **Acrescentado**: `9170052` / constante `52538`; regra 6 da depuração; memo item 5 |
| 114-1 com as duas condições (T0-12/14) | Já no design (`9170025`) |
| Integral + excesso Ley 1393 (T0-07/13) | Já no design (`9170020`/`21`) |
| Auxílio fora da base do art. 64 (T0-16) e variável pela média do último ano | **Fechado** item 13: base = salário do art. 127, variável pela média (CST 253 por analogia; CSJ SL1659-2025) |
| Piso da incapacidade | **Fechado** item 14: C-543/2007 e Concepto MinSalud 2023; piso padrão ligado, configurável |
| Piso da base de parafiscais | **Fechado** item 3: CCG diz sem piso nem teto |
| Auxílio do aprendiz na fase prática | Fechado (CST 81: todos os auxílios); fase lectiva segue sem regra |
| T0-09/10/11 (reclassificação de linhas do WTC: 175–176, 201–217, 226, 228–229, 267, U260–U264) | **Decisão do usuário pendente**: as matrizes refletem o WTC como está; se reclassificar, rodar `scripts/gen_matrices.py` de novo |

## Achados que o Design precisa ver
1. **Tabela do art. 383 não é marginal pura** (degraus para baixo em 150/360/640/945/2.300 UVT): montar como lookup por faixa com valor fixo, não como Differential.
2. **WTC v1.7 sem Mercans Code** na coluna A: matrizes chaveadas por linha do WTC; re-chavear quando os códigos forem atribuídos.
3. `Yes/No`: 58 linhas de seguridade com `Yes/No`; as 53 de não salarial pactado entram via excesso da Ley 1393 (regulação 9170019); as outras 5 de seguridade (R6, R37, R227, R338, R358) e as 22 de retenção precisam de split de wage type.
4. `CEILING` (arredondar para cima) não confirmado no vocabulário do motor (item aberto 1, bloqueante).

## Revisor independente
Subagente revisor (independente, só leitura), 30/10:
- **Matrizes × WTC:** as 405 linhas do WTC conferidas (amostra pedida ≥ 30 coberta: 31 linhas, 310 células), **4.050/4.050 células do CSV iguais** ao WTC; posição em cada uma das 10 matrizes (Seção 1 / Seção 2 / ausente se NA) e registro consolidado (298 linhas) **sem divergência**. Confiança 98%. Não conferido: texto da Matriz K.
- Correções necessárias: nenhuma.

## Regeneration after the post-release review (2026-10-30)
WTC v1.7 final changed (reclassifications T0-09/10/11, rows 175–176, 201–217, 226, 228–229, 260–264, 267; md5 `44f8b66148169c9b25a67c73592a77ec`). Matrices regenerated with `scripts/gen_matrices.py`: CSV `dbfd07f1c4e424e3713fdc37cca67b63`, matrices `2200f69b60334c3be51e1895a11fa58a`.

## Segunda passada pós-release (2026-10-30, consistência CCG × specs / WTC / Payslip)
- WTC v1.7 final mudou só fora das colunas N–X (aba Employer Sick Pay, Global WTC Coverage, Tax Credit, Form Reference Guide, coluna Y das linhas 327 e 330; IDs PR-02 a PR-05 em `final/test0/CONSISTENCIA-DECISOES.md`); md5 `d83d0e3c75b908f3e9d2e710b2c3eec2`. Matrizes regeneradas com `scripts/gen_matrices.py`: CSV igual (`dbfd07f1c4e424e3713fdc37cca67b63`), matrizes `8372dca77124fae27892ebd0d8b9175e` (md5 da fonte e exemplos das 5 linhas condicionais, agora listadas pelo próprio gerador).
- Contagens atuais (do CSV): 405 linhas, 298 ativas, 107 `NA`; `Yes/No` por perímetro N 22, O 13, P 2, Q 57, R 58, S 55, T 4, U 57, W 3, X 3; seguridade 58 linhas = 53 pactadas + 5 condicionais. Corrigidas no design: Parte 5 (ponto estrutural) e Parte 6 item 15.
- Memo item 10: a confiança de 70% é da inclusão das férias pagas em dinheiro na base de parafiscais (85% na fórmula e na exclusão do IBC). Piso da incapacidade atribuído só à C-543/2007 (o Concepto MinSalud 2023 trata dos 2/3 dos dias 1–2, não do piso) no design (constante `52544`, `9170093`, item 14) e no memo item 15.

## Regeneração para a emissão de 2026-11-02 (v1_1)
Fontes: finais de 02/11 (`final/MD5-FINAIS.txt`): CCG v1.6, **WTC v1.8** (`8e05d1c4306a55331c93190af3316747`), DD v1.5, SIR v1.3, Payslip v1.3, specs DIAN-001/004/005, CESANTIAS-006, PILA-003 v1.2 e DIAN-002, PILA-007 v1.1; decisões `pesquisa-2026-11-02/TABELA-RODADA5.md` e `revisao/rodada5/CONFERENCIA-R5.md`.
- **Matrizes e CSV:** `python -I scripts/gen_matrices.py ../CO-WTC-001-v1.8.xlsx .` (gerador ajustado: versão do WTC pelo nome do arquivo, nomes `v1_1`, parágrafo da retenção sem as cesantías). Rodado duas vezes: mesmo md5. Diferenças do CSV contra a v1_0 (6 linhas, todas decisões da 2ª passada): R120–R122 e R321–R322 N `Yes/No` → `No` e P `Yes` → `No` (cesantías e juros sem retenção, inclusive não residente); R346 classe `Non-Salary - non-remunerative` → `Non-Salary - pacted` e Q/R/S/U `No` → `Yes/No`. Contagens: `Yes/No` N 17, O 13, P 2, Q 58, R 59, S 56, T 4, U 58, W 3, X 3; seguridade 59 linhas = 54 pactadas + 5 condicionais (R6, R37, R227, R338, R358).
- **Regulation Design e Memo → v1_1** (conteúdo mudou): base e versões; constantes `52533`–`52535` anuais pelo acumulado; fórmulas `58156`–`58158` sem `÷ 12` (saldo anual não usado, leituras `$58156_ytd`, `$58157_ytd`, `$58159_ytd`); regra 4 da depuração reescrita com os exemplos recalculados (3.947.554,80; 1.763.832,00 / 1.899.912,00; 3.243.282,00; payslip 1.993.152,00); R07 refeito (teto anual não limita no mês; 4.519.774,80); `9170063` sem cesantías; Parte 5 com as contagens novas (U × R diferem só em R37; a v1_0 dizia seis linhas, defasado desde 30/10) e os pontos de relatório; Parte 6 itens 8 (acumulado), 10 (fechado) e 15 (54 / 17); change log. Memo: itens 5 e 7 e o resumo.
- **Varredura:** nenhuma citação de versão defasada fora dos change logs; Circular 101 não citada; `÷ 12` só no limite de 2.500 UVT do RAIS voluntário (ET 55, `58151`, fora das decisões da 2ª passada) e na média de 12 meses da indenização.
- `final/simulations/` não foi alterado (abas que ainda limitam 790/1.340 por mês: listadas em `revisao/rodada5/CONFERENCIA-R5.md`); o design diz que, nelas, vale a Parte 4.

| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | validacaoco | Pacote v1_1: matrizes/CSV regenerados do WTC v1.8; Regulation Design e Memo atualizados (rodada 5); v1_0 em `_historico/2026-10-30/` |

## Resíduos corrigidos antes da subida ao Drive (2026-11-02)
- **Teto de 2.500 UVT do RAIS voluntário (ET art. 55):** a lei limita "el veinticinco por ciento (25%) del ingreso laboral o tributario anual, limitado a 2.500 UVT" (ET art. 55, texto da Ley 2010 de 2019 art. 31; local `raw/docs/oficiais/CO/2026-10-30-ET-pr002-art55-SecretariaSenado.html`; mesma redação no DUR 1625 arts. 1.2.1.12.9 e 1.2.4.1.6 num. 3.2, local `2026-10-13-DUR-1625-2016-DIAN.htm`). Teto anual → decisão A-1 por analogia (pelo acumulado, sem `÷ 12`; CE S4 rad. 24047/2021). `CO_Regulation_Design_v1_2.md`: `58151` de `DIVIDE(MULTIPLY(2500;52502);12)` para `MAX(SUBTRACT(MULTIPLY(2500;52502);$rais_nci_ytd);0)`; leitura `$rais_nci_ytd` acrescentada na Parte 2 (Accumulation), regra 6 da Parte 4 e item 8 da Parte 6; change log v1.1. Os 25% seguem sobre os pagamentos do mês (como os 30% de `58156`). Nenhum final dividia 2.500 UVT por 12 (WTC: "2,500 UVT per year"), então só o design mudou.
- **Campos bancários (Parte 5, ponto 3):** lista alinhada aos finais corrigidos (DD v1.5 e CO-DIAN-001 v1.2): 42, 45, 47 e 98; 48/49 só com cartão ligado a conta.
- Memo, Matrizes e CSV: sem mudança (o Memo item 5 já diz "2,500 UVT a year" e o efeito no design já cita `9170052` com leituras acumuladas). Cópia anterior do Design em `_historico/2026-11-02-antes-residuos/` (`0b7ce6f27c64b409f8c1505d37fac852`).
- Varredura depois: `÷ 12` / `DIVIDE(...;12)` só na média de 12 meses da indenização (`58164`); nenhuma lista bancária com 46 ou 30/31.

| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | validacaoco | Resíduos antes da subida ao Drive: `58151` com o teto de 2.500 UVT pelo acumulado; campos bancários 42/45/47/98 |

| 2026-11-02 | validacaoco | Pacote renomeado de v1_1 para **v1_2** antes da subida: a pasta do Drive `07 - Design` já tem um pacote v1_1 (5/10, linhagem anterior), que vai para `Archived/`. Conteúdo igual; só nomes, título e linha do change log. |

### md5 após a renomeação para v1_2 (2026-11-02, valem estes)
| Arquivo | md5 |
|---|---|
| CO_Regulation_Design_v1_2.md | 7e6dcb790ad18f30c90858c4c3e09a30 |
| CO_Statutory_Research_Memo_v1_2.md | 4ae8ada64c3d9bb572baeab0909b8e62 |
| CO_Taxability_Matrices_v1_2.md | c98868b33de5221f3155c9c685412f68 |
| CO_Taxability_Perimeters_Extract_v1_2.csv | 4e5f8fd1a2721743ce870094e4975177 |

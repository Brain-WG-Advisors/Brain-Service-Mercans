# Chade — planilha de comparação v5 × Dev (conferência)

> Hub: [[Chade]] · Design: [[2026-11-01-design-v5/CONFERENCIA|CONFERENCIA v5]] · Vereditos: [[LEI-VEREDITOS]] · Comparação anterior: [[COMPARACAO]]
> Rascunho local, 2026-11-02. **Não vai ao Drive, ao Dev nem ao chat sem ok do usuário.** Nada fora desta pasta foi alterado.

## Entrega
- `TD_Design_Comparison_v5_vs_Dev.xlsx` (inglês), gerado por `build_comparacao.py` (`python -I build_comparacao.py`).
- Layout, fontes (Arial 9/10/12, fórmulas em Courier New 8), cores (cinza D9D9D9 no cabeçalho; Same E2EFDA, Different FFF2CC, Only theirs FCE4D6, Only ours DDEBF7), colunas e fórmulas vivas copiados de `modelos/TD_Design_Comparison_Ours_vs_Dev.xlsx`; coluna "Question for the call" com ★ copiada de `modelos/BH_Design_Comparison_Dev_vs_Ours.xlsx`.

## Abas
| Aba | Conteúdo |
|---|---|
| Summary | Semelhança (resultados, só os 12 cenários, estrutura, matrizes, geral), **Legal accuracy** (temas resolvidos pela lei, contagem e % de cada lado, por linha de regulação e ponderado pela confiança), matrizes de duas formas, semelhança por bloco, contagem de perguntas. Tudo por fórmula. |
| Regulation Comparison | 37 linhas: as 31 regulações do Dev (peso 1) × as 35 do v5 (6 só nossas, peso 0). Fórmula extraída de cada design (td.json e `_build_v5.py`), Status, Cause (a–e), Adherence, Difference, Weight + **Legal basis**, **Who is right per the law**, **Confidence**, **Question for the call** (31 perguntas, 12 ★). |
| Results | 32 casos (12 cenários + 20 extras) × 21 saídas = 672 linhas: bases, isenções, deduções, IRPP, TFE, TAFP, CNPS EE e ER por ramo, PSA, líquido, custo. Difference e Status por fórmula; causa e "Closer to the law" por linha que difere. |
| Matrices | 21 perímetros (bases, isenções, 9 BIK, 15%, passagem) sobre os 579 elementos de pagamento da WTC V3.0; contagens por COUNTIF sobre a aba "Matrix Detail". |
| Matrix Detail | Código a código (579 × 21): Both / Only theirs / Only ours / —. |
| Legal Themes | 40 temas (34 da LEI-VEREDITOS + 6 do v5), com quem está certo pela lei, confiança e artigo. |
| Open points | Decisões técnicas pendentes (transporte/CNPS, 62867, operário < 35, pagamento irregular, regularização anual da CNPS, limites de faixa) e fontes que faltam. |

## Números do Summary (recalculados no Excel)
- Semelhança: resultados 63% (672 valores), só cenários 70%, estrutura 62%, matrizes 84,1% (concordância em todos os códigos: 94,8%). **Geral: 70%.**
- Legal accuracy: 34 temas resolvidos pela lei. O v5 está certo em 34 (100%; 89% ponderado pela confiança); o Dev em 13 (38%; 36% ponderado). 3 temas abertos. Por linha de regulação: v5 100%, Dev 9% (33 linhas com veredito).
- Perguntas para a call: 31 linhas com pergunta; 12 ★.

## Decisões técnicas
1. Dev rodado com `sim_dev.py` (suposições S1–S12) e v5 com `run()` do `_build_v5.py`, ambos importados só para leitura (sem bytecode). Ajustes de entrada iguais aos do `comparar.py`: código 21600 → 21640 do lado do Dev; flag 58206 = 2 vira 0 no Dev (o flag dele é 0/1).
2. Matrizes: um código conta quando entra direto ou por conta intermediária que o perímetro soma (ex.: 58105 dentro do bruto do IRPP). Sem essa expansão, o bruto do IRPP dava 12,5% só por diferença de arquitetura. Ficaram fora do universo as contas 58xxx e as de imposto de 4 dígitos. Restam 579 de 618 linhas da WTC.
3. A Legal accuracy usa os vereditos da LEI-VEREDITOS, relidos para o v5 (temas 35–40 novos). Os vereditos são a **nossa** leitura da lei. Por isso há a linha ponderada pela confiança, e os itens "No rule" e "Not law" ficam fora da contagem.
4. A seção "Score" do modelo de out/2026 não foi copiada: era autoavaliação. Fica no lugar a Legal accuracy pedida.

## Conferência
- **Fórmulas:** aberto no Excel 16 (COM, só leitura), `CalculateFull`. **1.552 fórmulas, 0 erros.** Arquivo fechado sem salvar.
- **Results × VALIDATION do v5:** o script compara, nos 32 casos, EE CNPS, IRPP, TFE, TAFP, PSA e líquido com a tupla esperada do `_build_v5.py`, e para se houver diferença. Conferido à mão contra `VALIDATION.md`:
  - cenário 1, IRPP: 28.464;
  - cenário 7, IRPP: 26.548;
  - cenário 11, IRPP: 97.375;
  - cenário 12, líquido: 295.702;
  - E3, TFE: 25.538;
  - E19, IRPP: 28.464.

  Os seis batem.
- **Cobertura:** o script exige que cada regulação do Dev apareça uma vez e as 35 do v5 ao menos uma vez.
- **Pasta v5:** sem alteração e sem `__pycache__`.

## Bloco de prova
- **Pedido → resposta:**
  1. Summary com semelhança e Legal accuracy por fórmula.
  2. Regulation Comparison com as 3 colunas novas (Legal basis, Who is right per the law com confiança, Question for the call com ★).
  3. Results com 12 + 20 casos nos dois motores, Difference e causa.
  4. Matrices código a código sobre a WTC V3.0.
  5. Open points.
- **Fontes:**
  - `td.json` do Drive (= CT-A-588) via `sim_dev.py`;
  - `_build_v5.py` e `VALIDATION.md` do v5;
  - WTC V3.0 export (md5 `04e06a49…`);
  - artigos citados na LEI-VEREDITOS (CGI 2026 DGI; Dec. 1635/1636; guia da CNPS).
- **Teste:** recálculo no Excel com 0 erros; asserção dos 32 casos contra o v5; seis linhas conferidas à mão.
- **Confiança:** 95% nos números (motores e fórmulas). Nos vereditos, a confiança é a de cada linha (60–100%). Os números do Dev dependem das suposições do `sim_dev.py` (cerca de 85%).

## Planilha 2 — `TD_Design_Comparison_v4_v5_v6_vs_Dev.xlsx` (2026-11-02)
Gerada pelo mesmo `build_comparacao.py`, função `build_multi()` (padrão ao rodar o script). A planilha v5_vs_Dev antiga só é regerada com `--v5-only`; o script não a tocou. Data no disco: 07:46. Há uma trava `~$` dela de 09:21: alguém está com o arquivo aberto no Excel.

**Abas, com as três versões nossas lado a lado contra o Dev**
- Summary:
  - colunas v4 | v5 | v6 | Change v4→v5→v6 | Dev;
  - medidas: resultados (32 casos e só 12 cenários), estrutura, matrizes, geral, legal accuracy (simples e ponderada), contagens;
  - linha "Change v4→v5→v6" e teste "v6 = v5".

  Tudo por fórmula.
- Regulation Comparison:
  - Dev | v4 | v5 | v6, com regulação, fórmula, status e aderência de cada um;
  - Legal basis, Who is right, Confidence, Question for the call (31 perguntas, 12 ★).
- Results: 672 linhas, com Dev | v4 | v5 | v6, as diferenças contra o Dev e o status de cada versão.
- Matrices e Matrix Detail: 21 perímetros × 3 versões sobre 579 códigos.
- Legal Themes: veredito v4 × Dev, v5 × Dev e v6 × Dev (o v6 é igual ao v5, por fórmula).
- Open points: com a posição do v4.

**Summary (Excel)**
| Medida | v4 | v5 | v6 | Dev |
|---|---|---|---|---|
| Resultados (672 valores) | 75% | 63% | 63% | |
| Só os 12 cenários | 81% | 70% | 70% | |
| Estrutura (9 checagens por regulação) | 50% | 52% | 87% | |
| Matrizes | 82% | 84% | 84% | |
| **Geral** | **69%** | **66%** | **78%** | |
| Legal accuracy | 62% (21/34) | 100% (34/34) | 100% | 38% (13/34) |
| Ponderada pela confiança | 57% | 89% | 89% | 36% |

**Diferença de método em relação à planilha 1:** a estrutura aqui é medida de forma mecânica e igual para as três versões. São 9 checagens: ID, nome, rule group, taxation type, pré-condição, contas, taxas, fórmulas e regras da matriz. Na planilha 1, a aderência era avaliada à mão pelo sentido da regra. Por isso o v5 dá 52% aqui e 62% lá.

**Conferência**
- Excel 16 via COM: Open, CalculateFull e Save. **4.401 fórmulas, 0 erros.**
- O script também confere sozinho:
  - v6 = v5 em todas as linhas de Results;
  - toda regulação do v4, do v5 e do v6 aparece na Regulation Comparison.
- Cinco valores conferidos à mão:
  1. Cenário 1, IRPP: 28.464 nas quatro colunas (337.750 × 12 − 800.000 = 3.253.000 × 10,5% ÷ 12 = 28.463,75).
  2. Cenário 5, base da TAFP: 300.000 nas quatro (a indenização fica fora da TF/TA).
  3. Cenário 12, bruto do IRPP: 330.000.
  4. E9, bruto em dinheiro:
     - Dev 350.000 (salário + diária);
     - v4 351.000 (salário + 6287x);
     - v5 e v6 401.000.
  5. E11, custo do empregador, v5/v6: 438.200 = 350.000 + 57.750 de CNPS patronal + 26.250 de TFE + 4.200 de TAFP.

## Planilha 2, regerada depois da rodada 2 do QA da v6 (2026-11-02)
- Agora são 34 casos: os 32 do v5 mais o E21 (atrasado do combustível do carro) e o E22 (atrasado de salário-base). Results tem 714 linhas.
- **v6 = v5 em todas as linhas, menos as 9 do E21**, que são o efeito explícito da correção das séries da matriz (o v5 também tinha o defeito). Nesse caso o IRPP é 23.214 no v4 e no v5, 26.364 no v6 e 26.889 no Dev.
- Summary (Excel):
  - geral: v4 69%, v5 66%, v6 79%;
  - estrutura: 50%, 52%, 86%;
  - matrizes: 82%, 84%, 86%;
  - legal: 62%, 100%, 100% (Dev 38%).
- Defeito achado e corrigido no `build_multi()`: a coluna v5 de Results mostrava o valor do v6. Conferido de novo no E21.
- Excel: **4.654 fórmulas, 0 erros.** Conferido à mão:
  - cenário 1, IRPP: 28.464 em todas as colunas;
  - E21, IRPP do v6: 317.750 × 12 → 316.365 ÷ 12 = 26.364;
  - E21, TFE do v6: 350.000 × 7,5% = 26.250;
  - E22, IRPP: 50.375 em todas as colunas;
  - E21, bruto do IRPP do v6: 330.000.

## Planilha 2, regerada depois da rodada 3 da v6 (QA r2: W1–W3), 2026-11-02
- Agora são 38 casos (E23–E26 novos) e 798 linhas em Results. **v6 = v5 em todas as linhas, menos as 54 dos 6 casos das correções de matriz** (5, E21, E23–E26). O v4 e o v5 têm os mesmos defeitos.
- **W3:**
  - a causa passou a ser « PSA exists only in v5 and v6 (not in v4 or the Dev) » (0 células com o texto antigo);
  - a medida "Legal accuracy" virou **"Themes where our position matches our reading of the law"**, com ressalva no texto;
  - a manchete agora é a medida **ponderada pela confiança**;
  - linha nova **"Defects found by QA after the score"**: v4 7, v5 7, v6 0 (pendente do QA rodada 3), com a lista.
- Summary (Excel):

  | Medida | v4 | v5 | v6 |
  |---|---|---|---|
  | Geral | 68% | 65% | 80% |
  | Estrutura | 50% | 52% | 86% |
  | Matrizes | 82% | 84% | 88% |
  | Temas | 62% | 100% | 100% |
  | Ponderada | 57% | 89% | 89% |

  Dev: 38% nos temas e 36% na ponderada.
- Excel: **5.158 fórmulas, 0 erros.** Conferido à mão:
  - cenário 5, TFE do v6: 90.000;
  - E23, IRPP do v6: 28.464 (o Dev também dá 28.464);
  - E24, IRPP do v6: 25.424;
  - E25, TAFP do v6: 3.600 (Dev 4.800);
  - E26, TFE do v6: 24.000.

## Quem mexeu
| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | frente Chade | planilha de comparação v5 × Dev criada (`build_comparacao.py`) |
| 2026-11-02 | frente Chade | planilha v4/v5/v6 × Dev (`build_multi()`), v6 criado em `../2026-11-02-design-v6/` |
| 2026-11-02 | frente Chade | planilha 2 regerada após a rodada 2 do QA da v6 (E21, E22; correção da coluna v5) |
| 2026-11-02 | frente Chade | planilha 2 regerada após a rodada 3 da v6 (E23–E26; W3: PSA, medida legal honesta, defeitos do QA) |

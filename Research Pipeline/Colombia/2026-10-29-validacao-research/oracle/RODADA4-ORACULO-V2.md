# Oráculo v2 — rodada 4 (2026-10-30)

Ligado a [[TABELA-CONSOLIDADA]] (`../pesquisa-2026-10-30/`), [[DECISOES-TEST4]], [[RELATORIO-TEST4]] e [[CONFERENCIA]]. Sem dados pessoais: empregados só como índice mascarado (E001…).

## O que mudou no código (`oracle_v2.py`; `oracle.py`, `oracle_v1_frozen.py` e `params.json` intactos)
| ID | Antes (oracle.py) | Depois (oracle_v2.py) | Fonte |
|---|---|---|---|
| T4-2 | Integral: IBC = 70% × salário (excesso ignorado) | IBC = 70% × salário integral + excesso Ley 1393 (excesso sem redutor); total da remuneração = integral 100% + NS pactado | Ley 100 art. 18; CE SU 25185/2021; CE 25907/2022 |
| T4-4 | `para_base = max(ibc_raw, piso)` (com excesso) | `para_base = max(salário [×70% integral], piso)`, sem excesso; ARL segue com o IBC (com excesso) | Ley 1393 art. 30; DL 1295/1994 art. 17; Ley 21/1982 art. 17 |
| T4-5 | Todo NS entra no teste de 40% | Campo novo `nonsalary_kind` (`pacted` = default, mantém os casos antigos; `natural` fica fora do IBC, do numerador e do total); `nonsalary_natural` opcional só na renda tributável | CE SU 25185/2021 regra 1; CE 25907/2022 |
| T4-1 | Exonera se salário < 10 SMMLV | Exonera se salário < 10 SMMLV **e** IBC saúde < 10 SMMLV; `exon_travada_campo76` marca revisão manual | DIAN 8380/2024 e 7196/2025; AT2 v30 campo 76 |
| A-08 | 72 UVT/dependente abatidos na retenção mensal | Fora da retenção (valor só informativo em `ret_dep72_so_declaracao_anual`); teto 40% / 1.340 UVT **mantido** | DIAN 11383/2024 IV.2; DUR 1.2.4.1.6 par. 3 |

## Suíte (mesmos casos, sem alterar `cases*.json`)
Referência: `results-v2-20261029-173702.json` e `results-research-20261029-173702.json` (saída do `oracle.py` atual). Novos: `results-v2r4-20261030-133546.json`, `results-research-v2r4-20261030-133546.json`. Diff: `diff_v1_v2r4.py`.
- `cases.json` (98 casos, 7 pendentes): mudaram só **C25** (CCF 120.100 → 120.000) e **C26** (CCF 144.000 → 120.000): o excesso saiu da base de CCF. SENA/ICBF já eram 0 (exonerados). C24/C27 só ganham o rótulo `nonsalary_kind`. Integrais C22/C23 sem NS: iguais.
- `cases_research.json` (17 casos): **RC03** (CCG 6.3 Ex.2) base gravável 3.739.512 → **4.368.000** (83,40 UVT), retenção continua **0**: é o recálculo do A-08 que o CCG precisa refletir. **RC05** (CCG 6.3 Ex.4, bônus não salarial) CCF 672.000 → **320.000** (base = salário 8.000.000; o IBC de saúde/pensão/ARL segue 16.800.000).
- Casos novos (`cases_v2r4.json` → `results-v2r4-novos-20261030-133546.json`): V01 exemplo UGPP ABC 2025 (IBC SS 5.400.000; CCF sobre 5.000.000) bate; V02 exemplo do ponto 2 (integral 30 M + NS 25 M) dá **24.000.000**; V03 NS por natureza fica fora (IBC 5.000.000); V04 salário 17 M + NS 20 M → IBC 22,2 M, **trava campo 76** (não exonera); V05 salário 17 M sem NS → exonerado.

## Test 4 (folha set/2026) com o v2 (`scripts/comparar_v2.py` → `resultados-v2.json`; `resultados.json` intacto)
| Classe | v1 | v2 |
|---|---|---|
| Bate | 4.526 | 4.530 |
| Tolerância | 342 | 342 |
| Sem dado | 342 | 342 |
| Divergência | 739 | 742 |
| Lacuna do oráculo | 7 | **0** |
| Sem efeito | 2 | 2 |
- **#1 exoneração 114-1 (8 empregados):** os 8 seguem divergentes nas 3 linhas (saúde 8,5%, ICBF, SENA). Em nenhum deles o IBC de saúde passa de 10 SMMLV: **0 travam pelo campo 76; os 8 continuam erro do provedor** (soma das diferenças na saúde patronal ≈ 10,6 M COP; ICBF ≈ 4,1 M e SENA ≈ 2,8 M, somas que já incluem o E251 abaixo).
- **Novo achado (E251, +3 divergências):** salário < 10 SMMLV, mas IBC de saúde ≥ 10 SMMLV; o provedor exonera e o v2 cobra (trava campo 76: a PILA não aceita "S"). Revisão manual. A trava acende em 10 empregados; nos outros 9 o provedor também cobra (bate).
- **4 integrais com excesso Ley 1393:** lacuna fechada, os 4 passam a **bate** (provedor = 70% × integral + excesso, como o v2).
- **3 linhas de CCF:** lacuna fechada, as 3 passam a **bate** (base sem excesso).
- Retenção, licenças e indenização: sem mudança.

## Bloco de prova
- **Pedido → resposta:** v2 com as 5 mudanças (comentadas no código com a fonte); suíte rerodada e comparada; Test 4 rerodado; destino dos 8, dos 4 integrais e das 3 CCF.
- **Fontes:** TABELA-CONSOLIDADA e DECISOES-TEST4 (pesquisa de 30/10); exemplos numéricos da UGPP ABC 2025 e do ponto 2 reproduzidos pelo v2.
- **Teste:** diff linha a linha v1 × v2 (115 casos); 5 casos novos com resultado esperado conferido à mão; comparação linha a linha `resultados.json` × `resultados-v2.json` (5.958 linhas, mesma chave emp/bloco/linha). Entradas geradas em scratchpad, fora da pasta.
- **Confiança:** 95% na implementação; as regras herdam a confiança da pesquisa (T4-2 80%, T4-5 85%, T4-1 90%, T4-4 e A-08 95%).

# Linha de base da validação CO (congelada em 2026-10-30)

Ligada a [[CONFERENCIA]], [[RELEASE-CROSSCHECK]], [[RODADA4-ORACULO-V2]] e [[RELATORIO-TEST4]]. Mesmo papel do `baseline/baseline.json` da França (runbook, gate G3): é o estado aceito; numa rodada futura, **regressão** = um check que passa aqui e passa a falhar.

## O que foi congelado
| Item | Arquivo (nesta pasta) | md5 |
|---|---|---|
| Oráculo | `engine/oracle_v2.py` (cópia idêntica de `oracle/oracle_v2.py`) | `c09f0e6fe72eb02ffa8e236ca16e6273` |
| Parâmetros | `engine/params.json` | `6c733bfde934edcd709c60402b4922c3` |
| Suíte da lei | `engine/cases.json` (98 casos, 7 pendentes de lei) | `6181780df089717296dbd9998f92a356` |
| Suíte dos exemplos da research | `engine/cases_research.json` (17 casos, 1 pendente) | `a56ab1b3c162c7813d26421161b5e193` |
| Casos novos da rodada 4 | `engine/cases_v2r4.json` (5 casos) | `ed5561320bfc771d94720c1040696eeb` |
| Comparação research × oráculo | `engine/compare.py` (valores dos artefatos v1.4 / v1.0 congelados no código) | `058db5fb5e4e56f763506b5e319fb570` |
| Autoverificação | `engine/selfcheck.py` | `baca3785f8ae9c8d72e1a1525b262471` |
| Resultados | `engine/results-v2-20261030-baseline.json` / `results-research-…` / `results-v2r4novos-…` | `dd71dec0…` / `0cb2a1d7…` / `4fece9f3…` |
| Comparação | `engine/compare-results.json`; `engine/selfcheck-results.json` | `9fdaf58b…`; `309bd6e9…` |
| Test 4 v2 (folha de set/2026, mascarada) | `test4-resultados-v2-baseline.json` (só diferença e classe por linha; empregados como E001…) | `623f7d7210a63f085c2137e99c0f7ab0` |

Scripts do Test 4 usados (não copiados, md5): `test4-folha-setembro/scripts/leitor.py` `22f3f223…`, `comparar_v2.py` `200a24f9…`. Entradas lidas só de `co-report-crosscheck/03-client-reports-masked/`; o JSON intermediário ficou no scratchpad, fora do cérebro.

**Reprodução (2026-10-30):** os três resultados do oráculo são idênticos linha a linha aos da rodada 4 (`diff_v1_v2r4.py`: 98, 17 e 5 casos, 0 com mudança). O Test 4 deu as mesmas classes de `test4-folha-setembro/resultados-v2.json`.

Comandos (em `engine/`): `python -I oracle_v2.py cases.json results-v2-<ts>.json`; idem `cases_research.json` → `results-research-<ts>.json` e `cases_v2r4.json`; `python -I selfcheck.py`; `python -I compare.py`. Test 4: `python -I leitor.py <03-client-reports-masked> <entradas.json>` e `python -I comparar_v2.py <entradas.json> <saida.json>`.

## Números
| Bloco | Resultado |
|---|---|
| Autoverificação do oráculo (bordas −1 / exato / +1) | **45 / 45 OK** |
| Suíte da lei | 98 casos (91 executados, 7 pendentes de lei: X01–X07), 2.118 linhas calculadas |
| Exemplos da research | 17 casos (16 executados, 1 pendente: pensionados), 394 linhas |
| Casos novos da rodada 4 (UGPP ABC 2025, integral + NS, NS por natureza, trava do campo 76) | 5 casos, 139 linhas; resultado esperado conferido à mão na rodada 4 |
| Research × oráculo (`compare.py`, tolerância COP 1) | **89 itens: 69 PASS, 20 FAIL** — os 20 são os valores dos artefatos **antes** da validação (v1.4 / v1.0 / Payslip v1.1); todos ligados abaixo |
| Test 4 v2 | 5.958 linhas: **4.530 bate**, 342 tolerância (≤ 100 COP), 342 sem dado, **742 divergência**, 0 lacuna do oráculo, 2 sem efeito |

## Cada FAIL da comparação research × oráculo
O `compare.py` traz no código os valores dos artefatos de antes da validação. Cada FAIL é um achado já decidido; a última coluna mostra o valor nos finais de 2026-10-30.

| Item | Local (artefato antes) | Antes | Oráculo | Achado | Nos finais |
|---|---|---|---|---|---|
| CCG-21 | CCG §6.3 Ex. 2: 72 UVT × 2 ÷ 12 | 628.488 | 0 | **A-08** (72 UVT só na declaração anual; DIAN 11383/2024 IV.2) | CCG v1.5 P3867: dedução fora da retenção |
| CCG-22 | CCG §6.3 Ex. 2: base gravável | 3.739.512 | 4.368.000 | **A-08** | CCG v1.5 P3849–P3855: 4.368.000; retenção 0 |
| CCG-43 | CCG §8.1 mês misto: auxílio de transporte | 215.882,33 | 174.366,50 | **SIM-06** (Ley 15/1959; Decreto 1258/1959) | CCG v1.5 P5076: 174.366,50 |
| CCG-44 | CCG §8.1: incapacidade 4 dias | 233.454 | 213.333,33 | **Limitação do oráculo** (sem o piso de 1 SMLDV): a research está certa, C-543/2007 (achados/VERIFICADO-1) | inalterado (233.454) |
| SPEC-05 | NE Example Analysis A39/C39 | 617.000 | 617.232 | **SIM-03** (retenção individual não se arredonda; DUR 1.6.1.11.11 só formulários) | NE v1.1: 617.232 |
| SPEC-06 | NE C40 DeduccionesTotal | 1.697.000 | 1.697.232 | **SIM-03** | NE v1.1: 1.697.232 |
| SPEC-07 | NE C43 ComprobanteTotal | 10.303.000 | 10.302.768 | **SIM-03** | NE v1.1: 10.302.768 |
| SPEC-12 | Form. 220 C27 casilla 60 | 7.404.000 | 7.406.784 | **SIM-03** | 220 v1.1: 7.406.784 → 7.407.000 no formulário; 2276 v1.1 N29 7.406.784 |
| SPEC-15 | Form. 220 C26 casilla 59 / 2276 N33 | 13.120.000 | 13.000.000 | **SIM-07 / F-04** | 220 e 2276 v1.1: 13.000.000 (nota de composição) |
| SPEC-17 | Form. 220 C21 casilla 52 | 157.440.000 | 169.440.000 | **SIM-02 / F-01** | 220 e 2276 v1.1: 169.440.000 |
| PAY-03, 04, 07, 08, 13 | Payslip (EN) H36, H37, H46, H47, H54 vazias | 0 | 192.000; 2.250.764,60; 100.300; 768.000; 1.600.000 | **SIM-01 / PS-07** | Payslip v1.2: os mesmos valores do oráculo |
| PAY-14 | Payslip H55 juros sobre cesantías | 0 | 19.200 (convenção do `compare.py`) | **SIM-01**, convenção decidida na rodada 2: 12% a.a. sobre a cesantía do mês = 192.000 (CCG / WTC L322) | Payslip v1.2: 192.000 |
| PAY-11, 12 | Payslip H56, H57 (8,33% e 4,17%) | 1.599.360; 790.215 | 1.600.000; 789.583 | **SIM-05** (1/12 e 15/360) | Payslip v1.2: 1.600.000; 789.583 |
| PAY-15 | Payslip I8 neto | 17.664.000 | 15.221.235,40 | **SIM-01** | Payslip v1.2: 15.221.235,40 |
| PAY-16 | Payslip H67 aportes do empregador | 4.896.000 | 5.764.300 | **SIM-01** | Payslip v1.2: 5.764.300 |

Resultado contra os finais: 19 dos 20 FAIL fecham com o valor do oráculo; o CCG-44 fica como limitação conhecida do oráculo (a research aplica o piso legal). PAY-14 fecha pela convenção aprovada, não pela linha do `compare.py`.

## Cada divergência do Test 4 v2 (742 linhas)
| Bloco | Mecanismo | Linhas / empregados | Ligação | Classe |
|---|---|---|---|---|
| D-Indenização | dias: tabela acima do CST art. 64 | 190 / 190 | Test 4 #6 | erro do provedor a favor do empregado (CST art. 13): sem efeito na research |
| D-Indenização | tabela acima do art. 64 + valor só sobre o salário básico | 190 / 190 | Test 4 #6 + #8; **T4-3** (base = salário do art. 127 com a parte variável, WTC F277:F280) | erro do provedor |
| D-Indenização | fração de ano truncada em dias inteiros | 159 / 150 | Test 4 #7 (art. 64: "proporcionalmente por fracción") | erro do provedor |
| D-Indenização | fração truncada + valor só sobre o básico | 141 / 141 | Test 4 #7 + #8; **T4-3** | erro do provedor |
| D-Indenização | valor só sobre o salário básico | 4 / 4 | Test 4 #8; **T4-3** | erro do provedor |
| C-Retenção | base sem nenhum benefício (25%, dependentes, AFC/APV) | 14 / 5 | Test 4 #2 (ET 206 num. 10, 336, 387) | erro do provedor |
| B-Aportes | ARL: taxa implícita ≠ classe do Master Data | 10 / 10 | Test 4 #3; **DD-24** (centro de trabalho ↔ classe de risco) | erro do provedor; research corrigida no DD v1.4 |
| B-Aportes | exoneração 114-1: provedor cobra saúde 8,5%, SENA e ICBF de quem ganha < 10 SMMLV | 8 + 9 + 9 / 9 | Test 4 #1; **T4-1** (DIAN 8380/2024 e 7196/2025) | erro do provedor |
| B-Aportes | exoneração 114-1: provedor exonera com IBC de saúde ≥ 10 SMMLV (trava do campo 76) | 1 / 1 | **T4-1** (AT2 v30 campo 76) | erro do provedor; revisão manual |
| B-Aportes | aporte do empregador sobre a base 64990, menor que o IBC do trabalhador | 4 / 2 | Test 4 #4 (Ley 100 arts. 18 e 20) | erro do provedor |
| E-Licenças | incapacidade dos dias 1–2 / EPS paga a 100% | 3 / 2 | Test 4 #5; CCG: padrão 66,67% configurável | erro do provedor a favor do empregado: sem efeito na research |
| **Total** | | **742** | | **0 divergências atribuídas à research** |

As 4 lacunas do integral com o excesso da Ley 1393 (T4-2) e as 3 da base de CCF (T4-4) que existiam no v1 fecharam no v2 e passaram a "bate".

## Bloco de prova
- **Pedido → resposta:** suíte rodada com o `oracle_v2.py`; Test 4 v2 rodado; congelado com data e md5; cada FAIL e cada divergência ligado a um achado ou a erro do provedor (tabelas acima).
- **Fontes:** `achados/SIMULACAO.md` (SIM-01…10), `achados/VERIFICADO-1.md` (CCG-44), `pesquisa-2026-10-30/TABELA-CONSOLIDADA.md` (A-08, T4-1…5), `test4-folha-setembro/RELATORIO-TEST4.md` (#1–#8), `oracle/RODADA4-ORACULO-V2.md`.
- **Teste:** reprodução linha a linha contra a rodada 4 (0 casos com mudança em 120); classes do Test 4 idênticas às de `resultados-v2.json`; valores dos finais lidos nas células e parágrafos citados.
- **Confiança:** 95% na ligação; a confiança jurídica de cada achado é a da TABELA-CONSOLIDADA.

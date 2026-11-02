# final/simulations — pacote de simulações da Colômbia (modelo da França)

Ligado a [[CONFERENCIA]] (pasta `2026-10-29-validacao-research`), [[CONFERENCIA-SIMULACOES-R5]] e [[Colombia]]. Gerado em 2026-10-30; **atualizado em 2026-11-02 (rodada 5, decisão A-1)**. Nada foi para Drive, ticket ou e-mail.

## Atualização 2026-11-02 (rodada 5, A-1: tetos anuais pelo acumulado)
- **Decisão.** Os tetos de 790 UVT (25% isento, ET 206 num. 10), 1.340 UVT (40%, ET 336 num. 3 / DUR 1.2.4.1.6 par. 3) e 3.800 UVT (AFC/AVP, DUR 1.2.1.22.43) são anuais e controlados pelo **acumulado do ano** na retenção mensal, e não por 1/12.
  - Fontes: CE Sección Cuarta rad. 24047 (28/10/2021) e Decreto 2231/2023 art. 9.
  - Fórmula: limite = mín(% do mês, teto anual − consumo jan–mês anterior).
- **Consumo.** Vem de um bloco explícito em cada aba:
  - CO_Simulation: colunas R:T;
  - Tax: linhas 86–99.
  - Premissa: mesmo pagamento desde 1/1/2026, como no CCG. No RC05/T105, os meses anteriores têm só o salário.
- **O que mudou de valor.** 16 abas do CO_Simulation (C09–C17, C19–C23, R07, R08) e 4 payslips do Tax (R07, R08, C22, RC05). RC05/T105: retenção 4.994.989,65 → **3.947.554,80**.
- **Law vs Provider.** Não rerodado. O consumo jan–ago por empregado não está nos agregados; C28 e J28 ficaram com nota de limitação.
- **Conferência.**
  - Excel CalculateFull, 0 erros.
  - CO_Simulation: 1.670 OK, 0 DIFF, 115 n/a.
  - Tax: 467 OK, 0 DIFF, 82 n/a.
  - 20 casos afetados batem com o oráculo YTD (`revisao/rodada5/simulations/oracle-sim-r5.json`): **PASS**.
  - Detalhe em `revisao/rodada5/simulations/CONFERENCIA-SIMULACOES-R5.md`.
- **Versões de 30/10.** Movidas para `final/_historico/2026-10-30/simulations/`, junto com o README de 30/10.
- **Scripts da rodada 5.** Estão em `revisao/rodada5/simulations/scripts/`: `oracle_sim_r5.py`, `apply_sim_r5.py` e `check_sim_r5.py`.

## Arquivos
| Arquivo | Equivale na França | Conteúdo | md5 |
|---|---|---|---|
| `CO_Simulation_2026_11_02_V1.1.xlsx` (V1.0 de 30/10 no histórico) | `FR_Simulation_2026_10_06_V1.0.xlsx` | 62 abas: Scenario, Read me, Summary, Parameters (nomes `p_*`, fonte primária por valor), 49 abas mensais (C01–C27, R01–R10, H01–H07, D01–D05), 7 abas de módulo (Withholding table, Benefits, Vacation, Leave, Termination, PILA type 51, Apprentice), Checks index, Formula comparison. 103 casos + 7 pendentes (X01–X07) listados com o motivo. | `c4075b22541a63f9a7d7bceca60eecb7` |
| `Tax Simulations - Colombia.xlsx` | `Tax Simulations - France.xlsx` | Layout de holerite: 14 casos de depuração (25%/790 UVT, teto 40%/1.340 UVT, dependentes art. 387, 72 UVT só na declaração anual, AFC, prepagada, moradia, integral, não salarial), indenização 20% > 204 UVT (T-B) e média de 12 meses (TI), leitura separada da prima (PB), fronteiras da tabela do art. 383 (T01–T18). Parâmetros à direita de cada aba (nomes `p_*` por aba). | `bf47180409210658e62e64c458d03de4` |
| `Colombia Simulations - Law vs Provider.xlsx` | `France Simulations - Official vs Internal.xlsx` | Folha real set/2026 × lei, **só agregados**: LAW SIMULATION e PROVIDER RESULT com as mesmas linhas (36), BY MECHANISM (13 linhas, 8 mecanismos; somas suprimidas quando < 3 empregados), OFFICIAL EXAMPLES (exemplo UGPP ABC 2025 reproduzido; nenhum simulador oficial online usado). Sem IDs, nomes, salários nem nome do cliente. | `d3e2ce248eb5dddce290836105bbe28c` |
| `scripts/` | — | Geradores da V1.0 (a rodada 5 editou as cópias com `revisao/rodada5/simulations/scripts/apply_sim_r5.py`, não com os geradores) (`gen_sim.py`, `gen_tax.py`, `gen_lvp.py`, `colib.py`, `casedesc.py`), `recalc.ps1` (Excel COM CalculateFull) e `check_wb.py`. | — |

## Fontes
- Oráculo: `oracle/oracle_v2.py` (md5 `c09f0e6f…`), `params.json` (`6c733bfd…`), casos `cases.json` (`6181780d…`, 98 casos) e `cases_v2r4.json` (`ed556132…`, D01–D05), resultados `results-v2r4-20261030-133546.json` (`60125780…`), `results-research-v2r4-…` (RC03, RC05). Casos novos da aba de imposto (TI, PB) rodados direto nas funções `terminacion()` e `retencion()` do oráculo.
- Regras (verdade de conteúdo): DRAFTs aprovados em `revisao/` — CCG v1.5 (`2f419776…`), WTC v1.7 (`c71f0d35…`), DD v1.4 (`c777c91f…`); decisões `pesquisa-2026-10-30/TABELA-CONSOLIDADA.md`.
- Test 4: `test4-folha-setembro/resultados-v2.json` (`4d7d4c3d…`), agregado por linha e mecanismo.
- Valores 2026 (aba Parameters): SMMLV 1.750.905 (Decreto 1469/2025), UVT 52.374 (Res. DIAN 000238/2025), auxílio 249.095 (Decreto 1470/2025), demais com norma por linha.

## Conferência
- **Mecânica:** os 3 arquivos recalculados no Excel (CalculateFull), **0 erros de fórmula**.
- **Pesquisa × oráculo:** `CO_Simulation` 1.670 linhas OK, 0 DIFF, 115 n/a (linhas sem contraparte no oráculo: líquido arredondado, custo do empregador, aprendiz); `Tax Simulations` 467 OK, 0 DIFF, 82 n/a (inclui a retenção sobre indenização, conferida à mão: 5.616.667 e 0). Total **2.137 linhas, 0 diferenças**.
- **Law vs Provider:** totais reconciliam com o relatório do Test 4 (5.958 linhas; 4.530 bate, 342 tolerância, 742 divergência, 342 sem dado, 2 sem efeito).
- **Revisor independente:** ver seção abaixo.

## Ressalvas (não mudam linha comparada)
1. Divisão do total arredondado da PILA entre empregado e empregador não está em fonte lida (SIM-08) — linha "net with PILA rounding" fica n/a.
2. ~~Rateio mensal 1/12 dos limites anuais em UVT é convenção operacional (parâmetro).~~
   - Substituída em 02/11 (A-1): os tetos anuais são controlados pelo acumulado.
   - Nova ressalva: o consumo jan–mês anterior vem da premissa escrita na aba (mesmo pagamento desde 1/1/2026; RC05 só o salário), porque não há histórico de folha nas planilhas.
   - O oráculo ainda usa 3.800/12 para AFC, mas isso não limita nenhum caso da suíte.
   - Law vs Provider: as linhas de retenção seguem com 1/12 (limitação, ver J28).
3. Aprendiz e retenção sobre indenização não existem no oráculo: conferidos à mão contra o CCG v1.5 final (fase prática com auxílio de transporte 249.095, CST 81).
4. Base de parafiscais: a pesquisa não tem piso; o oráculo aplica o piso do IBC — nenhum caso da suíte diferencia.

## Reconferência contra os finais (30/10, depois do Test 0)
- Regras conferidas contra o CCG v1.5 final (`e6bea61992da…`) e o WTC v1.7 final (`0523f34b…`; colunas N–X iguais ao DRAFT).
- Alterado: citação do FSP para Ley 797 arts. 7 e 8 (T0-03) em Parameters, nas linhas de FSP e na Law vs Provider; piso da incapacidade passa a regra citada (C-543/2007; MinSalud 2023), sem efeito nos casos I01–I04; linha de auxílio de transporte do aprendiz na fase prática (AP2).
- Sem efeito nas simulações: Circular 101 (não citada), dominical 80/90% (já), 114-1 com dois limites (já), integral + excesso (já). RAIS voluntário (ET 55) e base variável do art. 64 não têm caso na suíte; ficaram no design.
- Recalculado no Excel: 0 erros; 1.670 + 467 OK, 0 DIFF.

## Revisor independente
Subagente revisor (independente, só leitura), 30/10:
- **Simulação × oráculo:** oráculo_v2 rerodado do zero em 94 casos; 1.663 linhas comparadas (coluna F e coluna I contra a saída nova = 3.326 checagens), **0 divergências**; inclui C05, C22, C25, R07, H04, D02, P04, V03, T-A, I04, L08, T06 (≥ 10 pedidos). Férias e maternidade conferidas à mão (V01, V04, V05, M01). Não automatizadas: líquido arredondado, custo do empregador, aprendiz (n/a). Confiança 97%.
- **Varredura:** 0 valores de erro nos 3 arquivos; 0 ocorrência de ID de empregado (E001…) ou padrão de nome.
- Correções necessárias: nenhuma.

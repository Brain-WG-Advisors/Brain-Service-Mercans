# Conferência — Chade design v6 no formato do Dev (conjunto de teste)

Ligações: [[Chade]] · [[2026-11-02-design-v6/CONFERENCIA|conferência do v6]] · [[2026-10-29-teste-design-hrblizz/2026-10-30-export-ram/COMPARACAO|comparação com o export do Dev]]

**Objetivo:** o nosso design v6 (36 regulações) escrito no mesmo formato do export do Dev (CT-A-580..588 em .md), para o Mohit carregar como conjunto separado na entidade de teste. **Nada foi enviado** (chat, e-mail, Drive, ticket, HRBlizz): só arquivos locais.

## Fonte
| O quê | Onde | Uso |
|---|---|---|
| Dados do v6 (FLAGS, R, matrizes, bandas, notas) | `../2026-11-02-design-v6/_build_v6.py` (md5 `9b17bdb7ae1bb3e2f7464f4f1daeff23`, só leitura; QA PASS r3) | importado pelo gerador, nada copiado à mão |
| Formato-alvo | `../2026-10-29-teste-design-hrblizz/2026-10-30-export-ram/x/` (9 .md do Dev) | cabeçalhos, ordem das colunas, ordinal `09`, matrizes ordenadas por conta, Tax Table |
| Modelo do motor do Dev | `../2026-10-29-teste-design-hrblizz/2026-10-30-export-ram/simulacao/sim_dev.py` (S1–S12) | só informativo no roundtrip |
| Nomes das contas (coluna de comentário das matrizes) | `CHAD-WTC_V3.0-export-2026-11-01.xlsx` | nome da 1ª conta da série |

## Arquivos
| Arquivo | O que é | md5 |
|---|---|---|
| `x-v6/1  CT-A-580-v6.md` | TD Specifications — Compliance v6 (test set): 17 flags, notionals, HR fields, tabela Design (36 linhas), lista NEW/REMOVED | `b4d52f3776bb7abaa6e3642733f62d01` |
| `x-v6/2  CT-A-588-v6.md` | TD: New Design — uma seção por regulação no layout do CT-A-588 + linha `> **Test set:**` (SAME/CHANGED/NEW + nota) | `cdcc2c91805cfe03a48b4b7a0669ca4e` |
| `x-v6/3  CT-A-587-v6.md` | TD: Cash Gross Salary (9148009, 9148010) | `321ca6690559784cd53be74a72b7302b` |
| `x-v6/4  CT-A-581-v6.md` | TD: Taxable Gross (9148131) | `1bc234ec3a17a34efb7f91beaeba96e2` |
| `x-v6/5  CT-A-586-v6.md` | TD: CNPS Salary (9148155) | `595f2d1fd5742f3e86d005081991fe44` |
| `x-v6/6  CT-A-585-v6.md` | TD Employer Lump-Sum Tax Base (9148151) | `b6a14c22cf3d62c7e45f661be0640033` |
| `x-v6/7  CT-A-584-v6.md` | TD: Apprenticeship Base (9148141) | `e0094aba167f555cda8877b958d7d446` |
| `x-v6/8  CT-A-583-v6.md` | TD: Non-Resident Tax Base (9148192, só 58552) | `06202b3493b5df8ee3c5fbfd1c3104e3` |
| `x-v6/9  CT-A-582-v6.md` | TD: Tax Table (9148211) | `a7df851456a46a38ff98904ebb755274` |
| `_export_v6_dev.py` | gerador (importa `_build_v6.py`) | — |
| `_leitor_dev_md.py` | leitor dos .md (independente do gerador; lê também o export do Dev) | — |
| `_roundtrip_v6_dev.py` | roundtrip + diff → `ROUNDTRIP-run.txt`, `DIFF-vs-Dev.md` | — |

Rodar: `python -I _export_v6_dev.py` e depois `python -I _roundtrip_v6_dev.py` (sai com código 0 só se tudo bater).

## Decisões (técnicas, reversíveis)
1. **Nomes dos arquivos:** padrão do Dev + sufixo `-v6` (`1  CT-A-580-v6.md`…); títulos com "— Compliance v6 (test set)". Matrizes citadas na tabela Design como `CT-A-587-v6 TD: Cash Gross Salary` etc.
2. **IDs 9148xxx do v6 mantidos.** Novas (sem par no Dev): 9148034, 9148035, 9148036, 9148175, 9148192, 9148271 — marcadas na linha `Test set: NEW` de cada seção e listadas no fim do spec. 9148011 do Dev não existe no conjunto (substituída por 9148192).
3. **Notas em inglês neutro:** a nota de cada regulação vem do `_build_v6.py` com troca de termos internos ("the Dev" → "the current design", "decisão técnica da frente, pendente do ok" → "open point, pending sign-off"; sem referências a ASSUMPTIONS, correcoes.md, rodadas de QA). O gerador falha se sobrar Claude/Dev/v5/front/user/ASSUMPTIONS; o roundtrip confere de novo nos 9 arquivos.
4. **Matrizes** em ordem crescente de conta (como o Dev); a ordem não muda o resultado (conta exata vence padrão; padrão mais específico vence) — provado pelo roundtrip.
5. **Tabela Design:** débito/crédito por faixa quando diferem (como o Dev em 9148171); `Band Assertion:` para a condição da faixa; linhas com `Is Taxable = No` aparecem com `(No)` na célula resumida (a matriz completa está no New Design).
6. **HR Fields:** os campos lidos pelas fórmulas das flags, marcados `new field` quando o Dev não os tem; `::key` indica campo de lista.

## Conferência
- **Roundtrip** (`ROUNDTRIP-run.txt`): 14/14 checagens OK — 36/36 regulações relidas = v6 (id, ordinal, nome, grupos, tipo, pré-condição, 46 faixas, 268 linhas de matriz); 17/17 fórmulas de flag; tabela Design = New Design; 6/6 arquivos de matriz = matriz inline; Tax Table = bandas de 9148211; nenhuma palavra interna.
- **Números:** motor do v6 rodando as regulações **lidas dos .md**: **12/12 cenários e 26/26 checagens extras** idênticos ao v6 conta a conta (2.072 valores, igualdade exata) e iguais aos valores esperados calculados à mão.
- **Informativo (modelo do motor do Dev, sim_dev S1–S12):** 37/38 casos iguais em todas as contas; 1 diferença — cenário 2 (salário zero): 58106 = 60.000 no modelo do Dev × 0 no v6 (ver "não representável" 4). Não afeta imposto nem contribuição.
- Pasta `2026-11-02-design-v6/` não alterada (md5 do `_build_v6.py` acima; sem `__pycache__`, `sys.dont_write_bytecode`).
- **Diff** (`DIFF-vs-Dev.md`): por ID, SAME 1 (9148221) · CHANGED 29 · NEW 6 · REMOVED 1 (9148011); matrizes, Tax Table e flags detalhadas.

## Não representável no formato do Dev (registrado, não forçado)
1. **Start Date / End Date da faixa** (v6: `01-01-2026`) e **creditAmount** (vazio em todo o v6): o layout do Dev não tem essas colunas. Sem perda: o ano fiscal `td_2026` dá a vigência; creditAmount não é usado.
2. **Base legal / nota por regulação:** o Dev não tem campo. Foi como linha `> **Test set:** …` depois da seção 4 (o leitor ignora). Se o carregador do Mohit não aceitar linhas extras, apagar essas linhas não muda nada no cálculo.
3. **Flags derivadas 58219 e 58226:** escritas como fórmula sobre outras flags (58215, 58216, 58217, 58218, 58205, 58225). Exigem que o engine calcule as flags em ordem de dependência, antes das regulações — não confirmado no HRBlizz.
4. **Piso só com pagamento (9148009):** no v6 o 58106 (60.000) só é gravado quando há salário em dinheiro; no formato, isso não se escreve sem pré-condição, e 58105 só existe depois (ordinal 10). Pelo modelo do Dev (S4, piso com matriz vazia) o 58106 sai 60.000 num mês sem pagamento. Só afeta o relatório DAS.
5. **Notionals:** o v6 não define nenhum (os 64550–64554 do Dev não são lidos por regulação do conjunto). **`$hr.pay_frequency`:** não faz parte do v6 (validado só mensal, `$period_divisor` = 12).
6. **Dependências fora do arquivo:** campos novos de DD/entidade (listas `N/Y`, `100/50`, `REEL`, `OUVRIER`; datas; valores 58213, 58223) e códigos de WTC a criar (6287x, 6288x, 62890 sem nome no WTC V3.0; passivo 2570 da PSA; código de regime obrigatório de previdência) precisam existir no HRBlizz para o conjunto rodar.

## Abertas (o arquivo traz a posição técnica atual, pendente do ok do usuário — não decididas aqui)
| Id | Ponto | Onde está no arquivo |
|---|---|---|
| D1 | Transporte 6251x/6252x fora do CNPS por inteiro (guia CNPS p. 8) | matriz CT-A-586-v6 (6251% No, 6252% No); nota de 9148155 |
| D2 | 62867 (auxílio-funeral) tributável no IRPP | matriz CT-A-587-v6 (série 6286% Yes); nota de 9148010 |
| A20 | Indenização 6218x e gratificações de fim de contrato 629xx na base da TFE (Art. 189-1°; inverte a posição antiga de `correcoes.md` 2026-07-07) | matriz CT-A-585-v6; nota de 9148151 |
| A34 | Limite de idade (< 35 anos) aplicado também a ouvriers no Art. 3-4° | flag 58226 (`LESS($58225;35)` para 58218 = 3 **e** 58217 = 1) |

## Bloco de prova
- **Pedido → resposta:** (1) pasta + gerador que importa o v6 + 9 .md no formato do Dev ✔; (2) leitor + roundtrip 12/12 e 26/26 ✔ `ROUNDTRIP-run.txt`; (3) diff ✔ `DIFF-vs-Dev.md`; (4) esta conferência com D1, D2, A20, A34 abertas ✔; (5) `python -I`, sem dados pessoais ✔.
- **Fontes:** dados = `_build_v6.py` (md5 acima); formato = os 9 .md do Dev em `export-ram/x/`.
- **Teste:** roundtrip mecânico (estrutura + 2.072 valores, igualdade exata); modelo do motor do Dev só informativo.
- **Confiança:** 100% em "os .md reproduzem o v6"; o comportamento real do engine no HRBlizz (flags derivadas, piso com matriz vazia, linhas de nota) não foi testado — depende do carregamento pelo Mohit.

## Histórico
| Data | Frente | O quê |
|---|---|---|
| 2026-11-03 | frente Chade | export v6 no formato do Dev |
| 2026-11-03 | frente Chade | spec: seção 'Prerequisites not yet in the system' (campos, contas, flags, WTC a criar); roundtrip refeito 100% |

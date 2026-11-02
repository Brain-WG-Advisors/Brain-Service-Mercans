# final/skill — skill `payroll-compliance-colombia` gerada dos finais (30/10/2026)

Ligado a [[CONFERENCIA]] (pasta `2026-10-29-validacao-research`), [[BASELINE]], [[TEST0]] e [[Colombia]]. Passo 7 do fechamento no modelo da França (commits do repositório FR "references regenerated from the approved finals; router updated to v1.1 and the 2026-10-06 validation" e "references regenerated from the final specs"). Só arquivos locais: nada foi ao Drive, a `~/mercans-pipeline`, a `~/.claude/skills` nem ao claude.ai.

## Saída
| Arquivo | O que é | Bytes | md5 |
|---|---|---|---|
| `payroll-compliance-colombia/SKILL.md` | Roteador (inglês), data 2026-10-30: versões vigentes, roteamento, como responder, parâmetros 2026, regras validadas em 30/10, pontos abertos, escopo | 15.410 | `a83685b79e9dbf6211f0bdcd67e12acd` |
| `references/01-ccg.md` | CCG v1.5 integral (docx: títulos, parágrafos e as tabelas na ordem) | 482.019 | `24a0be2a012532a7029bed53d724f4c3` |
| `references/02-wtc.md` | WTC v1.7, as 6 abas célula a célula | 365.564 | `902ee10e84eafb501f530bcf33df6de4` |
| `references/03-sir.md` | SIR v1.2: conteúdo da v1.1 (captura de 29/10, em inglês) com os 15 blocos da v1.2 literais (marcados ⟦v1.2⟧) + índice de autoridades CO-SIR-INDEX-001 v1.0 literal (sem 3 menções a arquivos internos) | 20.656 | `78698b90947e88b477cbe23f7ba057a7` |
| `references/04-reports-spec.md` | 7 specs v1.1, todas as abas | 1.116.384 | `efcfec46d2674dd35999f3e814b42ab6` |
| `references/05-data-dictionary.md` | DD v1.4, as 8 abas | 218.616 | `a14415fced0f558073a2067d9bd6ba2b` |
| `references/06-payslip.md` | Payslip Generator v1.2, as 8 abas | 47.498 | `8210303d7c45e5e57794ea3045db8f71` |
| `references/07-qa-report.md` | Novo: artefatos e md5, método e resultados da validação de 30/10 (linha de base, Test 4, pesquisa oficial, Test 0, cross-check), 17 regras confirmadas com fonte e confiança, os 14 itens de configuração do design, outros pontos abertos e posições < 80% | 15.244 | `85fcc3d18281460e0d7e580c70b6f3f9` |
| `payroll-compliance-colombia.zip` | Mesma estrutura do .zip da França (`payroll-compliance-colombia/SKILL.md` + `references/`); inclui o 07, a pedido | 597.118 | `dc0430b277d320315689ec5f1347a895` |
| `scripts/` | `conv.py` (docx/xlsx → md), `assemble2.py` (01, 02, 04, 05, 06), `build_sir.py` (03), `verify2.py` (completude), `make_zip.py` | — | — |

## Fontes (finais de 30/10, conferidos com `MD5-FINAIS.txt`: 12/12 OK)
| Artefato | Versão | md5 |
|---|---|---|
| `CO-CCG-001-v1.5.docx` | 1.5 | `3b605ff32f5ad0bb674c0aa6aff7e9ee` |
| `CO-WTC-001-v1.7.xlsx` | 1.7 | `d83d0e3c75b908f3e9d2e710b2c3eec2` |
| `CO-DD-001-v1.4.xlsx` | 1.4 | `6557f7615a6b2e030c0e1165de224a28` |
| `specs/CO-DIAN-001-NominaElectronica-Spec.xlsx` | 1.1 | `3cf3dc717406696615a07cbbdc396aa4` |
| `specs/CO-DIAN-002-Formulario350-Spec.xlsx` | 1.1 | `97e1fae0ae350553568ef432d096b1b2` |
| `specs/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx` | 1.1 | `482c793f1bbac1d2ae3c3236cc797e6f` |
| `specs/CO-DIAN-004-Formulario220-Spec.xlsx` | 1.1 | `1321e85f1e95402e055d1b0ca5d76ef9` |
| `specs/CO-DIAN-005-Formato2276-Spec.xlsx` | 1.1 | `8ff54cc914c8cc86f9298213ad950b31` |
| `specs/CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx` | 1.1 | `8170ff99cce984124361e0ce9f5b8123` |
| `specs/CO-PILA-007-AportesPensionados-Spec.xlsx` | 1.1 | `eae9a7955d23ddea574503de6b573243` |
| `CO_Compliance_Payslip_Generator.xlsx` | 1.2 | `7be64fec306c72725bd193973c6d4bec` |
| `CO-SIR-001-v1.2-texto-final.md` | 1.2 | `e8669140302efe07b2ae15f41b585bd2` |
| Base do SIR: `linha-de-base/CO-SIR-001-v1.1-captura-2026-10-29.md` | 1.1 | `27e3807ed33a9d8f72c200a70f18474a` |
| Índice do SIR: `Research Pipeline/Colombia/CO-compliance/03-statutory-integrations/CO-SIR-INDEX-001-v1.0.docx` | 1.0 | `3144b46eff327c56fa5f4c20a355624a` |

Para o 07 e o SKILL.md: `baseline/BASELINE.md`, `test0/TEST0.md`, `test0/RESIDUOS-DECISOES.md`, `RELEASE-CROSSCHECK.md`, `design/` (PART 1 e PART 6 do Regulation Design; Research Memo), `simulations/README.md`, `pesquisa-2026-10-30/TABELA-CONSOLIDADA.md`.

## Método (igual ao da França)
- 01, 02, 04, 05, 06: conversão literal por script (python-docx; openpyxl `read_only`, `data_only`), nº da linha do Excel na 1ª coluna, cabeçalho com proveniência (bytes, md5), notas de leitura e **índice de navegação com nº de linha** (conferido por `assert`: cada linha do índice aponta para o título).
- Única alteração no texto dos artefatos: o nome do cliente trocado por `[client]` (5 ocorrências: WTC 1, specs 4).
- 03: o SIR só existe como Google Doc; a v1.2 foi emitida como 15 blocos sobre a v1.1. O arquivo junta a v1.1 (captura) e os 15 blocos literais; o script confere que os 15 estão no arquivo.
- 07 e SKILL.md: escritos a partir dos finais e dos documentos de decisão; sem nome do cliente, sem IDs internos de achado, sem referência a agentes ou rodadas.

## Conferência
- **Completude** (`verify2.py`: cada célula/parágrafo não vazio do final procurado no .md): WTC 8.385 células, 0 faltando; DD 4.853, 0; Payslip 923, 0; specs 1.549 + 5.059 + 2.001 + 2.010 + 1.559 + 4.211 + 2.652, 0 faltando; CCG 7.549 parágrafos, 113 sem correspondência literal = entradas do sumário (com nº de página) e fluxogramas de várias linhas (presentes em bloco de código; 1 conferido por normalização de espaços).
- **Varredura de termos:** 0 ocorrência do nome do cliente, de "COVAL", "oracle", IDs internos de achado, "subagent", "RESEARCH-GAP", "TODO/TBD/FIXME" nos 8 arquivos. Ficam, por serem texto literal dos artefatos: "draft" no sentido de decreto em minuta; nomes de quem atualizou nas linhas de Version Control (WTC VC 1.4).
- **Frontmatter:** `name: payroll-compliance-colombia`; `description` com 869 caracteres (< 1.024).
- **Revisor independente** (subagente, só leitura, 30/10): 60 afirmações de valor/regra do SKILL.md, 07, 03 e notas de leitura conferidas contra os finais (texto extraído por ele do docx/xlsx), MD5-FINAIS (md5 recalculados) e os documentos de decisão. **56 OK, 1 errado, 3 não conferíveis**; confiança 93%.
  - Errado (corrigido): 07 §5 item 12 dizia "45 linhas pactuadas / 16 de seguridade" (número da PART 6 do design, defasado); o WTC v1.7 tem **53** linhas `Non-Salary - pacted` (recontado por mim) e 22 linhas de retenção `Yes/No`.
  - Não conferível 1 (mantido): subtipos 3/4/12 sem PA/CD — conferido por mim no texto da CO-PILA-003 ("For sub-types 3, 4 and 12 the contributor document type must differ from PA (passport) and CD").
  - Não conferível 2 (mantido): regra do Formato 2276 por último dígito / dois últimos é texto literal do bloco aprovado do SIR v1.2.
  - Não conferível 3 (resolvido): o Payslip A78 cita a Ley 1393 art. 32 para divulgar aportes e o CCG não; ressalva acrescentada no SKILL.md.
  - Rótulos ajustados: "Test 0" → "independent final review"; "oracle" retirado; 3 menções a arquivos internos (`scope_manifest`, `integration-landscape.json`) tiradas da Parte 2 do 03. "Test 4" mantido (nome pedido).
- Depois das correções: zip refeito (`testzip` OK, 8 arquivos), md5 acima.

## Achados fora do pedido (resolvidos na 2ª passada pós-release de 30/10; ver abaixo)
1. **Conflito entre finais no `@Porcentaje` dominical da NE:** CCG v1.5 Módulo 4.4 (Concepto DIAN 013840/2025 → reportar 80/90%) × CO-DIAN-001 v1.1 Field Options linha 65 (mantém 100/75/150/110 até posição escrita da DIAN). A skill registra os dois lados.
2. WTC v1.7 aba Employer Sick Pay ainda traz "OPEN ITEM 1/2" e "fonte primária do piso não recuperada", enquanto o CCG v1.5 Módulo 8 já cita C-543/2007 e o Concepto MinSalud 2023.
3. Capa do CCG v1.5 com "Date 21 October 2026" (emissão = linha 1.5, 30/10).
4. PART 6 item 15 e README do `design/` com a contagem antiga (45/16) de linhas `Yes/No`; Research Memo item 10 põe os 70% de confiança na base de parafiscais, enquanto a TABELA (D9) e o WTC os põem na base de prima/cesantías.
5. Google Doc do SIR: seções 0 e 2 ainda falam em seis relatórios e não descrevem a CO-PILA-007 (já registrado no texto final do SIR).

| Data | Frente | O quê |
|---|---|---|
| 2026-10-30 | validacaoco | Skill regenerada dos finais (passo 7 do modelo França): references 01–07, SKILL.md v. 2026-10-30, zip; revisor independente 60 afirmações (1 corrigida) |

## Regeneração depois da 2ª passada pós-release (30/10)
- Os três achados acima foram decididos com fonte primária e corrigidos nos finais (IDs PR-01, PR-02 e PR-08 em `final/test0/CONSISTENCIA-DECISOES.md`), junto com PR-03 a PR-07 (alto risco, campos 57–60 da PILA, referências internas do WTC, Ley 1393 art. 32 no Payslip e no CCG, piso da incapacidade). Finais novos: CCG `3b605ff3…`, WTC `d83d0e3c…`, NE `3cf3dc71…`, Payslip `7be64fec…` (demais iguais; `MD5-FINAIS.txt`).
- Regeneradas com os scripts desta pasta (`conv.py` → `assemble2.py`): 01, 02, 04, 06 (05 saiu byte a byte igual, prova de que o método reproduz). Notas de leitura do 01 (data da capa) e do 02 (Employer Sick Pay, PILA 57–60) atualizadas em `assemble2.py`. SKILL.md (dominical e Ley 1393 art. 32) e 07 (§1 md5, §5 item 12, §6 dominical e Employer Sick Pay) editados à mão, sem mudar a numeração de linhas do índice do 07.
- `verify2.py`: WTC 8.385 / DD 4.853 / Payslip 923 / specs 0 faltando; CCG 113 sem correspondência literal (sumário e fluxogramas, como antes). Varredura: 0 nome do cliente, COVAL, oracle. Zip refeito (`testzip` OK, 8 arquivos).

## Regeneração para a emissão de 2026-11-02 (versão vigente)
Fontes: finais de 02/11 (`final/MD5-FINAIS.txt`, inclusive o DD com as referências cruzadas, `326f3e1d…`): CCG v1.6, WTC v1.8, DD v1.5, specs DIAN-001/004/005, CESANTIAS-006, PILA-003 v1.2 e DIAN-002, PILA-007 v1.1, Payslip v1.3, SIR v1.3 (texto) + texto v1.2 (linha do histórico). Decisões: `pesquisa-2026-11-02/TABELA-RODADA5.md`, `revisao/rodada5/CONFERENCIA-R5.md`.
- **Método reproduzido antes:** `conv.py` + `assemble2.py` / `build_sir.py` sobre os finais de 30/10 (`_historico/2026-10-30/`) deram 01–06 com o md5 de 30/10, byte a byte. Depois, cópias com versões e notas atualizadas: `scripts/assemble3.py` (01, 02, 04, 05, 06), `scripts/build_sir3.py` (03: blocos da v1.3 marcados ⟦v1.3⟧ onde mudaram, ⟦v1.2⟧ onde não), `scripts/verify3.py`. `out/` intermediário apagado depois.
- **Notas de leitura novas:** 01 (v1.6, capa ainda com 30/10; tetos anuais pelo acumulado; Exemplo 4 do Módulo 12 ainda diz "within the monthly cap" = parte não usada do teto anual); 02 (coluna Y AuxilioNS/AuxilioS nas linhas 255–264; cesantías sem retenção; Tax Credit sem 1/12); 04 (cinco v1.2 / duas v1.1, mudanças da v1.2); 05 (meios de pagamento, linha 104); 06 (v1.3, líquido 15.478.848, retenção 1.993.152).
- **SKILL.md** (à mão): versões vigentes; regras novas (tetos de 790/1.340/3.800 UVT anuais pelo acumulado, 3.800 compartilhado; cesantías sem retenção inclusive não residente, 20% opcional desligado; ARL da PILA decimal 0.0052200; AuxilioNS/AuxilioS; campos bancários por meio de pagamento); itens de configuração 7 e 9 reescritos; posições < 80% atualizadas. **07** reescrito: §1 versões e md5 de 02/11; §2 2ª passada; §3 resultados (51 casos, 18 mudam; exemplos recalculados); §4 regras 18–25; §5 itens 7, 9, 12 (17 linhas de retenção `Yes/No`, 54 pactadas); §6 posições reconfirmadas.
- **Conferência:** `verify3.py` — WTC 8.396 / DD 4.862 / Payslip 927 / specs 1.554 + 5.064 + 2.001 + 2.015 + 1.564 + 4.216 + 2.652 células, 0 faltando; CCG 7.552 parágrafos, 113 sem correspondência literal (sumário e fluxogramas, como em 30/10). Versões citadas: todas vigentes (fora proveniência e linhas de histórico). Nenhuma frase aplica `÷ 12` / "one twelfth" aos tetos (só negativas). Varredura: 0 nome do cliente, COVAL, oracle, rodada, DRAFT-R5. `description` 869 caracteres.
- **Revisor independente** (subagente, só leitura, 02/11): 30 afirmações conferidas contra os finais (extração própria) e os documentos de decisão: **29 OK, 1 errado, 0 não conferível**. Errado (corrigido): 07 regra 8 com 95% → 90% (TABELA-RODADA5, Res. 2708). Observação dele, fora da skill: o mapper Payment Method do DD (linhas 95–104) não tem 46 nem 30/31, e a CO-DIAN-001 NIE066 ainda diz "bank-mediated (42, 45, 46, 47, 48, 49…)", sem o 98.

| Arquivo | Bytes | md5 |
|---|---|---|
| `payroll-compliance-colombia/SKILL.md` | 17.814 | `4ae67c251070e280de16d588b28f3445` |
| `references/01-ccg.md` (CCG v1.6) | 485.835 | `08e546bde9d33306fcb509a445354ff7` |
| `references/02-wtc.md` (WTC v1.8) | 371.123 | `29cba24adf5f4a5fc764b8ce180c06a6` |
| `references/03-sir.md` (SIR v1.3) | 21.435 | `08809bb897dadcbc83313429ab7dc4ca` |
| `references/04-reports-spec.md` | 1.121.303 | `10d3017162fd40962b744ce05770dcd9` |
| `references/05-data-dictionary.md` (DD v1.5) | 219.837 | `c80c423b2c509a4f967341f5c699f70e` |
| `references/06-payslip.md` (v1.3) | 48.490 | `abab9963e5f5c82cecb648a27839f191` |
| `references/07-qa-report.md` | 19.787 | `302f97dd62274cd2c6c9c321ca2d1287` |
| `payroll-compliance-colombia.zip` (`testzip` OK, 8 arquivos) | 604.946 | `ac4cdac0747d9c8b67dde2686ca1f411` |

As tabelas "Saída" e "Fontes" acima são da emissão de 30/10 (histórico).

| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | validacaoco | Skill regenerada dos finais de 02/11 (01–07, SKILL.md, zip); revisor independente 30 afirmações (1 corrigida) |

## Regeneração depois dos resíduos corrigidos antes da subida ao Drive (2026-11-02)
Fontes: finais corrigidos (`final/MD5-FINAIS.txt` das 10:23; prova em `final/RELEASE-CROSSCHECK-R5.md`, seção "Resíduos"): CCG `8d0f35c3…` (capa 2 November 2026; Módulo 12 Exemplo 4 linha (E) com o teto anual de 790 UVT pelo acumulado), DD `3967d232…` (ID Information!H7: 42, 45, 47, 98), CO-DIAN-001 `15c97ce2…` (NIE066 e Population Rules com a mesma lista; linha v1.2 do Version Control). Demais finais iguais.
- **Regeneradas** com `scripts/conv.py` + `scripts/assemble4.py` (cópia do `assemble3.py`; notas de leitura do 01 sem a ressalva da capa e do Exemplo 4, do 04 com a lista bancária da NE e do 05 com a lista do mapper): 01, 04, 05. **02 e 06 saíram byte a byte iguais** (prova de que o método reproduz). `out/` intermediário apagado depois. Diferenças do 01/04/05 contra a versão anterior: só proveniência (bytes, md5), as notas de leitura citadas, os números de linha do índice (deslocados por 1 a 2 linhas de nota; conferidos pelo `assert` do script) e as células/parágrafos corrigidos.
- **SKILL.md** (à mão): regra dos campos bancários (42, 45, 47, 98; 48/49 só com cartão ligado a conta; vazio para 10, 20, 71, 72). **07** (à mão, sem mudar a numeração de linhas): §1 md5 do CCG, DD e CO-DIAN-001; regra 25.
- **Conferência:** `verify3.py` — WTC 8.396 / DD 4.862 / Payslip 927 / specs 1.554 + 5.064 + 2.001 + 2.015 + 1.564 + 4.216 + 2.652 células, 0 faltando; CCG 7.552 parágrafos, 113 sem correspondência literal (sumário e fluxogramas, como antes). Varredura: 0 nome do cliente, COVAL, oracle, DRAFT-R5; "monthly cap" só nos tetos mensais do art. 387 (juros de moradia, dependentes). Zip refeito (`testzip` OK, 8 arquivos).

| Arquivo | Bytes | md5 |
|---|---|---|
| `payroll-compliance-colombia/SKILL.md` | 17.940 | `32c529d66d40be1ed023042c14c4037d` |
| `references/01-ccg.md` (CCG v1.6) | 485.825 | `265d2cce6f87c27af9786f5a538bc9f1` |
| `references/02-wtc.md` (WTC v1.8, igual) | 371.123 | `29cba24adf5f4a5fc764b8ce180c06a6` |
| `references/03-sir.md` (SIR v1.3, igual) | 21.435 | `08809bb897dadcbc83313429ab7dc4ca` |
| `references/04-reports-spec.md` | 1.121.769 | `450bbdfcea9e93f699a481e461398a86` |
| `references/05-data-dictionary.md` (DD v1.5) | 219.790 | `bed1d77f059b7e12f425a2edb6d260e5` |
| `references/06-payslip.md` (v1.3, igual) | 48.490 | `abab9963e5f5c82cecb648a27839f191` |
| `references/07-qa-report.md` | 19.854 | `cdeafbab644b2f264412b9d9c4288e98` |
| `payroll-compliance-colombia.zip` (`testzip` OK, 8 arquivos) | 605.148 | `c8b409d05db28ca2d88fc4db6610a770` |

A tabela da seção anterior (emissão de 02/11, 10:12) vira histórico.

| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | validacaoco | Skill regenerada depois dos resíduos (01, 04, 05, SKILL.md, 07, zip); 02, 03 e 06 iguais |

## Regeneração depois do segundo lote de resíduos (coerência, 2026-11-02)
Fontes: finais corrigidos (`final/MD5-FINAIS.txt` regravado pelo `release_crosscheck_r5.py`; prova em `final/RELEASE-CROSSCHECK-R5.md`, seção "Resíduos de coerência, segundo lote"): CCG `7c3e6b25…` (Módulo 7, B1, linha Limit: teto mensal de 100 UVT dos juros de moradia como regra legal, DUR 1625 art. 1.2.4.1.27; Módulo 2, linha Payment method com o 98 CATS), CO-DIAN-001 `7cfd6c3e…` (Field Options A78 e D88: 98 CATS no subconjunto realista). Demais finais iguais.
- **Regeneradas** com `scripts/conv.py` + `scripts/assemble4.py` (sem mudança no script; notas de leitura já coerentes: "monthly in the rule itself" para os 100 UVT): 01, 04. **02, 05 e 06 saíram byte a byte iguais** (prova de que o método reproduz). `out/` intermediário apagado depois. Diferenças do 01/04 contra a versão anterior: só proveniência (bytes, md5) e as 2 linhas corrigidas de cada (01: linhas 656 e 2812; 04: linhas 708 e 718); números de linha do índice inalterados.
- **07** (à mão, sem mudar a numeração de linhas): §1 md5 do CCG e do CO-DIAN-001. SKILL.md e 03 sem mudança. Zip refeito (`testzip` OK, 8 arquivos).

| Arquivo | Bytes | md5 |
|---|---|---|
| `payroll-compliance-colombia/SKILL.md` (igual) | 17.940 | `32c529d66d40be1ed023042c14c4037d` |
| `references/01-ccg.md` (CCG v1.6) | 485.965 | `3fa92baf0b91724129d61ce440150573` |
| `references/02-wtc.md` (igual) | 371.123 | `29cba24adf5f4a5fc764b8ce180c06a6` |
| `references/03-sir.md` (igual) | 21.435 | `08809bb897dadcbc83313429ab7dc4ca` |
| `references/04-reports-spec.md` | 1.121.974 | `7e199ac4ec62c365e8dc39e86f885231` |
| `references/05-data-dictionary.md` (igual) | 219.790 | `bed1d77f059b7e12f425a2edb6d260e5` |
| `references/06-payslip.md` (igual) | 48.490 | `abab9963e5f5c82cecb648a27839f191` |
| `references/07-qa-report.md` | 19.854 | `47c7827a1d361e4eb19e0da0d1bf2bb6` |
| `payroll-compliance-colombia.zip` (`testzip` OK, 8 arquivos) | 605.294 | `4e5db61c041d93baf74f5c33a6256e96` |

A tabela da seção anterior (resíduos, 10:27) vira histórico.

| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | validacaoco | Skill regenerada depois do segundo lote de resíduos (01, 04, 07, zip); 02, 03, 05, 06 e SKILL.md iguais |

# Revalidação independente: specs GPM313 v1.2 e GPM312 v1.2 (Lituânia)

> Hub [[Lituania]] · Validação anterior: [[Research Pipeline/Lithuania/2026-10-28-validacao/VAL-GPM313-GPM312|VAL-GPM313-GPM312]] · Changelog do construtor: [[Research Pipeline/Lithuania/2026-10-29-correcoes/CHANGELOG-GPM-v1.2|CHANGELOG-GPM-v1.2]]

- **Data:** 2026-10-29.
- **Revisor:** auditor independente e adversarial. Não construiu os arquivos e não alterou nenhum deles; escreveu só este relatório.
- **Arquivos auditados** (md5 conferido, igual ao do changelog):
  - `LT-VMI-001-GPM313-Spec_v1.2.xlsx` `4fc13b96ae089eee911acbbec1465653`
  - `LT-VMI-002-GPM312-Spec_v1.2.xlsx` `81148366488d4fa10b773677fe23c9fc`
- **Bases:**
  - v1.1: `2026-10-27-reports/*_v1.1.xlsx` (`3ee4f2db…`, `4a13365c…`).
  - v1.0: `specs-drive/`, usada para conferir os fills devolvidos.
- **Fontes primárias**, lidas nesta sessão em `raw/docs/oficiais/LT/` (só leitura):
  - `GPM313.mxfd` (ScriptModule com 342 linhas) e `GPM312.mxfd` (3 981 linhas). As linhas citadas abaixo são do ScriptModule, contadas a partir de 1.
  - `IN_GPM313_nuo_2026.docx` e `IN_GPM312.docx`, com texto extraído por python-docx.
  - `GPMI-IX-1007-suvestine-2026-06-11_2026-12-31.pdf`, com texto extraído por pypdf.
- **Método:**
  - Escrevi do zero um verificador próprio. O `check_gpm.py` do construtor não foi usado nem lido.
  - Os scripts ficam no scratchpad desta sessão, `…/scratchpad/reval/`:
    - `reval_gpm.py` (md5 `179273c6…`): porte do VBScript.
    - `diff_wb.py`: diff célula a célula.
    - `unit.py`: testes de unidade e de mutação.

## Veredito

**FAIL, por 1 achado MAJOR que não é regressão.**

**O que passou:**
- Os 3 BLOCKER e os 6 MAJOR da validação de 28/10 estão fechados.
- Não há regressão em relação à v1.1.
- Todos os exemplos das duas specs passam no porte do script do MXFD, com 0 erro.
- Os totais das caixas batem com a soma das linhas.

**Por que FAIL:**
- A linha U de exemplo (U7 = `U`, trabalho no exterior) mostra GPM de 20 % retido: 19 200,00.
- Pelo GPMI art. 2(16)(4) e art. 5(4)(5), essa renda não é objeto do imposto do não residente. A própria spec diz isso em GPM312 Spec!M37.
- A validação de 28/10 deixou o ponto como "não verificável", e a v1.2 o manteve. Com o GPMI local ele passou a ser verificável (achado R1).
- A correção é pequena (U9 = U10 = 0,00; caixa 5 = 16 660,00) e o meu verificador confirma que a linha corrigida passa no MXFD.

**Confiança: 90 %.**
- Mecânico a 100 %: nomes, tamanhos, dígitos verificadores, somas, diff, fills e "=".
- R1 a 90 %: a leitura é do texto da lei, sem parecer da VMI sobre o U7 = U.
- Continua fora do alcance local: a serialização real no FFData (separador decimal) e as validações do servidor EDS.

## Achados desta revalidação

| ID | Arquivo!Aba!Célula | Problema | Fonte | Sev. |
|---|---|---|---|---|
| R1 | GPM312!Sample File!B35 (U9 `20,00`, U10 `19200,00`); GPM312 Spec!K39, K40; Spec!K7 e Sample!B10 (caixa 5 = 35 860,00 inclui os 19 200,00) | A linha U7 = U / U5 = 01 ("trabalho realizado no exterior", regra 48.5.1) aparece tributada a 20 %. Isso contradiz a própria GPM312 Spec!M37 ("outside the GPMI art. 5(4) tax object"). Esperado: U9 = `0,00` e U10 = `0,00` (regra 50.2.1: zero para pagamento não tributável) e caixa 5 = `16660,00` em K7 e B10. A caixa 4 não muda, porque o U8 continua declarado (regra 49, último §: declara-se "nesvarbu, ar … objektas"). Teste: a linha corrigida passa no MXFD. U9 = 0 com U5 = 01 está na lista m0 (l. 2946), e o b9_5/b9_10 do U tem a mensagem comentada (l. 3442–3443). | GPMI (`GPMI-…-2026-06-11_2026-12-31.pdf`), art. 2(16)(4): renda de entidades LT é de fonte LT "išskyrus nenuolatinių Lietuvos gyventojų iš veiklos užsienio valstybėse gautas pajamas"; art. 5(4)(5): para o não residente só é objeto a renda de emprego "kurių šaltinis yra Lietuvoje". IN_GPM312, regras 48.5.1, 49 (último §) e 50.2.1. | MAJOR |
| R2 | GPM312!GPM312 Spec!A2, A10, A27 | Células alteradas na v1.2 (o "===" virou "—") sem o fill `FFDDEBF7`. Mantiveram o cinza `FFD6DCE4` "por instrução", e isso conflita com a regra "toda célula alterada em azul". Version Control!E4 diz "Blue marks v1.2 changes only", o que é quase verdadeiro (3 exceções não declaradas no próprio arquivo). | Diff célula a célula (`diff_wb.py`): 88 alteradas, 85 azuis, e as 3 restantes são estas | MINOR |
| R3 | GPM313 e GPM312!Version Control!C4 | Data `29-Oct-26`, enquanto as linhas 2–3 usam o ISO `2026-08-21` / `2026-10-27`. Formato inconsistente na mesma coluna. A E4 do GPM312 tem 646 caracteres e cita o `check_gpm.py` (ferramenta interna). O conteúdo é verdadeiro (conferido item a item), mas a linha não é curta. | Version Control linhas 2–4 | MINOR |
| R4 | GPM312!GPM312 Spec!K31, K32 × Sample File!B35 | O mesmo John Smith aparece com U1 = `LT100000000014` / U2 = 3 (código PVM) na coluna K e com U1/U2 vazios na amostra. As duas formas passam no script (PVM_kodas ok; vazio aceito, l. 2538–2540), mas o exemplo é incoerente entre abas. Era a alternativa que o VAL B2 deixou em aberto. | GPM312.mxfd l. 3657–3688, 2538–2540; IN_GPM312, regra 42, último § | MINOR |
| R5 | GPM312!Sample File!B22 | Rita: salário 01 de 38 000,00 todo "em espécie" (L6 = N), e nenhuma linha em dinheiro. É implausível como exemplo de payroll. Pela regra 28, N = qualquer pagamento em espécie fora o uso de carro (A). Só gera aviso (l. 2274). Já vinha da v1.1 e o construtor o declarou. Sugestão: L6 vazio nessa linha. | IN_GPM312, regra 28 (§§ 1–2); GPM312.mxfd l. 2274 | MINOR |
| R6 | GPM312!Population Rules!C15 | "LT is accepted only with U2 = 6 and U5 = 26, 62 or 67 (l. 3272-3279)" está certo para a l. 3276, mas em 2026 a l. 2569 rejeita U2 = 6 com 26. Na prática, para 2026, sobram só 62/67. A frase anterior ressalva "dividends only on the 2025 return", então é imprecisão, não erro. | GPM312.mxfd l. 3272–3279 e 2566–2570 | MINOR |
| R7 | GPM312!GPM312 Spec!K25 | O exemplo vazio está escrito como o texto `(empty)`. Na coluna K, os outros exemplos vazios (K19, K20, K36) ficam em branco. Um gerador que leia a coluna K pode emitir o literal. | Coluna K da própria spec | MINOR |

Pendências que continuam abertas (não são achado novo; vêm do VAL e o construtor as declarou):
- **m3:** prazo de 15/08/2026 (sábado) e a Lei de Administração Tributária, que não está nas fontes locais.
- **M3 (resíduo):** a forma real no FFData.
- **Validações do servidor EDS.**
- **Propagação ao SIR, ao DD e à SAM:** fora do escopo desta auditoria.

## Status dos achados da validação de 28/10

| Achado | Status | Evidência (célula na v1.2) |
|---|---|---|
| B1 código do pagador | **Fechado** | `302123442` em GPM313 K3, Example Analysis A2, Sample B6 e em GPM312 K3, K12, K29, Example Analysis A2, Sample B6, B16, B30. O porte do JAR/ID_formatas_simple_f dá soma 101, mod 11 = 2 = último dígito, então passa. `302123456` não aparece em nenhuma célula. |
| B2 PVM do U1 | **Fechado** (incoerência residual em R4) | K31 = `LT100000000014`: 14 caracteres, "LT" + 12 dígitos, 13º = "1", passa no PVM_kodas (l. 3657–3688). |
| B3 linha U de dividendos 2026 | **Fechado** | Sample B38/B39 vazias. "AB Brokeris" não aparece em nenhuma célula. Teste de mutação com a linha antiga reproduz os 3 erros (l. 2525, 2558, 2570). |
| M1 U12/U15 | **Fechado** | F42 = C e F45 = C. G42/G45, M42/M45 e Population Rules C15 batem com as l. 3237–3243 (erro: U12 e/ou U13 se U14 ≠ LT e U2 ≠ 6), 2555–2558 (proibidos com U2 = 6) e 3336–3348/3426 (U15 vazio só gera aviso). IsRequired = false no MXFD. |
| M2 caixas 4/5 | **Fechado** | K6 = B9 = `200600,00` = ΣL8 (104 600) + ΣU8 (96 000). K7 = B10 = `35860,00` = ΣL10 (16 660) + ΣU10 (19 200). G6 = G7 = 0. Conferido pelo porte do `setcheckvalue` (l. 1265–1311). O valor de K7/B10 muda se R1 for corrigido. |
| M3 vírgula decimal | **Fechado** (resíduo FFData aberto) | Todos os exemplos Decimal da coluna K, Example Analysis e Sample usam vírgula. A coluna J declara o separador ",". K22/K39 `20,00` estão na ListItems de L9/U9. |
| M4 códigos pessoais | **Fechado** | `39001010109`, `48505054322` (4 = feminino, Rita) e `37712120987` (3 = masculino, Petras) passam no AK_tikrinimas portado. Os antigos `39001010101` e `47712120987` falham no mesmo porte (teste negativo). |
| M5 domínio U2 = 6 | **Fechado** | Field Options E70, Population Rules C4/D4 e Example Analysis D17: 62/67/51/52, l. 2566–2570 conferidas. Códigos 51 = esporte e 52 = atlético-artístico (2 priedas 2.8.9/2.8.10). Regras 36-1, 37 (2º §) e 38 conferidas no texto da IN. |
| M6 regra 21 IN GPM313 | **Fechado** | GPM313 Population Rules C5 e C11 descrevem a regra 21 fielmente: mês posterior do mesmo período, declaração retificadora do mês do pagamento, as importâncias passam a não tributáveis e saem da declaração (IN_GPM313_nuo_2026, par. 93 do docx). |
| m1 9/10/11 dígitos | **Fechado** | GPM313 J3 cita a l. 20 do GPM313 (correto); GPM312 J3/J12/J29 citam a l. 1204 (correto); J14 cita as l. 1465–1480. |
| m2 B_FormNr/B_FormVerNr | **Fechado** | GPM313 File Structure C8 e GPM312 File Structure C10. MXFD: B_FormNr com 6 células (GPM313, GPM312) e 7 (GPM312L/U); B_FormVerNr com 2; IsRequired = false. |
| m3 prazo em sábado | **Parcial** (declarado em aberto) | Example Analysis D5 marca o ponto como aberto; Sample B4 continua `2026-08-15`. A fonte não está no repositório. |
| m4 código 92 | **Fechado** | Sample B25: `VL123456`, L2 = 2. Passa no verslo_nr (l. 3576–3611). Bate com a regra 23, 2º § ("pirmieji aštuoni simboliai"). |
| m5 código 44 com M | **Fechado** | Sample B24: 77 / B / M, L9 = L10 = 0. Base: regra 29.2 (exemplo M → código 77), 2 priedas 2.8.17 ("B klasė – mažosios bendrijos išmokėtos savo nariui") e regra 31.2.2 (B sem retenção → 0). |
| m6 T6/T31/T37 | **Fechado** | Linhas citadas conferidas: 1273–1276 e 1290–1293 (exclusão do C), 2538–2540 (U1/U2) e 2863–2864 (U só a partir de 2026). |
| m7 log da v1.1 | **Fechado** | Version Control!E3 das duas specs lista o que a v1.1 de fato mudou. Não há mais "No change to the content rules". |
| m8 azul sem alteração | **Fechado** | Nenhuma célula azul sem alteração nas duas specs. Os fills da v1.1 voltaram exatamente ao da v1.0 (0 divergências). |
| m9 "four groups" | **Fechado** | GPM312 File Structure C9 = "three groups". |
| Drive `#ERROR!` | **Fechado** | 0 células começam com "=" nas duas specs (as 5 que quebravam: Spec A2/A10/A27, Sample B14/B28). As 4 linhas "-----" já estavam no Drive sem erro (CONFERENCIA 28/10: só 5 `#ERROR!`). |
| N1 (do construtor) L12 = DE com taxa | **Fechado** e correto | Com K25 = DE, K22 = 20 e K23 = 8 400, o porte acusa erro (l. 2121–2127 e 2287). O teste negativo na v1.1 reproduz o erro. Ver R7 sobre o literal `(empty)`. |

## Regressões (v1.1 × v1.2)

Nenhuma regressão encontrada.
- **Abas:** as mesmas 9 e na mesma ordem. Congelamento e larguras iguais.
- **Estilo:** fonte, borda, alinhamento e formato numérico iguais em todas as células. A única diferença é a linha 4 nova da Version Control, que copia o estilo da linha 3.
- **Células alteradas:**
  - GPM313: 35, todas azuis.
  - GPM312: 88, das quais 85 azuis; as 3 sem azul são o achado R2.
  - O conjunto alterado coincide com a tabela do changelog.
- **Fórmulas:** 0 células com fórmula ou começando com "=".
- **Campos × MXFD:**
  - GPM313: 12/12 nomes da coluna H existem no MXFD e a coluna I = células × linhas.
  - GPM312: 41/41, idem.
  - 0 divergências, então nomes e tamanhos continuam iguais ao MXFD.
- **Restos dos valores antigos:** nenhuma célula tem `302123456`, `LT100001234567`, `39001010101`, `47712120987`, `38505054321`, "AB Brokeris", "four groups" ou "hard requirement".

## Afirmações novas do construtor, conferidas na fonte

| Afirmação (célula) | Resultado | Fonte |
|---|---|---|
| Linha MB 77 / classe B / M, L9 = 0 (Sample B24) | Correta | IN_GPM312, regra 29.2 e exemplo seguinte (par. 96–97: "M raide … kodu 77"); 2 priedas 2.8.17 (par. 379); regra 31.2.2 (par. 115). Script: 77 está na lista B de 2026 (l. 1619); M/C dispensam a checagem de classe (l. 1645); o teto de 100 000 € é acumulado (l. 2219–2238), e 15 000 fica abaixo dele. |
| Regra 21 IN GPM313 (Population Rules C5/C11) | Correta | IN_GPM313_nuo_2026, par. 93 do docx. |
| Regra 36-1 e domínio U2 = 6 de 2026 (E70, C4, D4, D17) | Correta | IN_GPM312 par. 143 (36¹), par. 144–145 (37 e 2º §) e par. 146 (38); script l. 2566–2570. |
| U12/U15 condicionais (F/G/M 42 e 45, C15) | Correta | l. 3237–3243 (erro), 2555–2558 (erro) e 3334–3349/3426 (aviso); as checagens isoladas de U12/U15 (l. 3231–3233, 3268–3270) estão comentadas. C15 tem a imprecisão R6. |
| T6/T31/T37 respondidas pelo script | Corretas | Linhas acima. |
| Regra 23, 2º §, e L2 = 2 (Sample B25) | Correta | IN_GPM312, par. 74; script l. 1485–1495 e verslo_nr. |
| "personal codes are fictitious and pass the check-digit functions" (Sample B2, Example C4) | Correta | Porte do AK_tikrinimas: os 3 passam. Sexo × 1º dígito coerente. |
| "boxes 4-7 equal the sums of the annex lines" (Sample B2) | Correta aritmeticamente | Porte do setcheckvalue. Ver R1, que muda o valor correto da caixa 5. |

## Saída do verificador (`reval_gpm.py 12`)

```
ancoras do script GPM312 (l.1556, 1617, 2604, 2946, 3073, 2569, 2558, 3243, 2287, 2864): todas ok
GPM313: 12 campos da coluna H conferidos com o MXFD (nome, tamanho=celulas x linhas); divergencias 0
GPM312: 41 campos da coluna H conferidos com o MXFD (nome, tamanho=celulas x linhas); divergencias 0
GPM313 K / Example Analysis / Sample File: B_MM_ID 302123442, Metai 2026, Menuo 7, G5 184250,00, G6 31322,50, G7 0,00, G8 12000,00, G9 2400,00, G10 0,00, G11/G12 vazios (as 3 fontes iguais)
GPM312 Sample File: 6 linhas L (B20-B25) e 1 linha U (B35/B36) lidas por posicao sob o rotulo
  [GPM312 Sample File] G4: declarado '200600,00' / soma das linhas 200600.00 -> ok   (l.1265-1311 setcheckvalue)
  [GPM312 Sample File] G5: declarado '35860,00' / soma das linhas 35860.00 -> ok
  [GPM312 Sample File] G6: declarado '0,00' / soma das linhas 0.00 -> ok
  [GPM312 Sample File] G7: declarado '0,00' / soma das linhas 0.00 -> ok
== AVISOS (el_warning, nao bloqueiam) ==
  [GPM313 Spec K / Example Analysis / Sample File] campos 5-12 vazios: G11, G12   (l.86)
  [GPM312 Sample File] periodo corrente (aviso fixo desta versao do MXFD)   (l.1247)
  [GPM312 Sample File!B22] PASITIKRINKITE ISMOKAS NATURA (L6=N)   (l.2274)
  [GPM312 Sample File!B25] codigo 92 sem L7: se pago pelo empregador, L7=D   (l.2276)
  [GPM312 Sample File!B35/B36] Pasitikrinkite U1/U13/U12/U15 (algum vazio)   (l.3426)
  [GPM312 Sample File] aviso fixo portal TIN da UE (pagina U)   (l.2376)
  (+2 linhas informativas: LapoNr com DecimalSeparator '.', campo de sistema)
== ERROS ==
RESULTADO v1.2: PASS - 0 erro(s), 10 aviso(s)
```

A linha L da coluna K (K14–K26), a linha U da coluna K (K31–K45) e a linha L montada a partir do Example Analysis (A4–A15) também foram validadas, com 0 erro.

**Teste negativo** (o mesmo verificador sobre a v1.1): `FAIL - 55 erro(s)`. Reproduz:
- B1, o pagador, em todas as abas;
- B2, o PVM;
- M3, o ponto decimal, inclusive `20.00` fora da ListItems de L9/U9;
- N1, o L12 = DE com taxa;
- M2, as caixas divergentes.

Nas linhas da amostra da v1.1 os erros são de desalinhamento, porque o leiaute antigo não punha cada valor sob o seu rótulo.

**Testes de unidade e de mutação** (`unit.py`):
- `jar9('302123442')` = ok e `jar9('302123456')` = falha.
- AK: `39001010109`, `48505054322` e `37712120987` passam; `39001010101` e `47712120987` falham.
- PVM: `LT100000000014` passa e `LT100001234567` falha.
- verslo_nr: `VL123456` passa.
- A linha antiga U2 = 6 / U5 = 26 gera os 3 erros (l. 2525, 2558, 2570).
- A linha U corrigida de R1 (U9 = U10 = 0) passa sem erro.

**Limites do porte:**
- Não portei:
  - os ramos de anos < 2025;
  - as checagens de duplicidade, que estão comentadas no script;
  - a l. 1448 (aviso L11).
- As listas de códigos e taxas são lidas do próprio script, na linha citada (âncoras conferidas).

## Dados pessoais

- Os códigos pessoais são fictícios e foram construídos para passar o dígito verificador: datas 1990-01-01, 1985-05-05 e 1977-12-12.
- Os nomes são genéricos (Jonas Jonaitis, Rita Ritaite, Petras Petraitis, Ona Onaite, John Smith).
- O TIN alemão `DE12345678901` e o endereço "Musterstrasse 1" são placeholders.
- Não há dado de funcionário de cliente.
- Ressalva inevitável: um código com dígito válido pode coincidir com o de uma pessoa real. Não há como verificar isso localmente.

## Bloco de prova

- **Pedido → resposta:**
  1. Porte e execução sobre todos os exemplos e somas: feito, ver "Saída".
  2. Status de cada B/M/m do VAL: ver a tabela de status.
  3. Regressões, fills, "=", Version Control e nomes/tamanhos: ver "Regressões", R2 e R3.
  4. Afirmações novas do construtor: ver a tabela de afirmações.
  5. Dados pessoais: ver a seção própria.
- **Fontes:**
  - script MXFD, com as linhas citadas;
  - IN_GPM312 e IN_GPM313_nuo_2026, com o parágrafo do docx;
  - GPMI art. 2(16)(4) e art. 5(4)(5).
- **Teste:**
  - porte próprio: v1.2 = 0 erro e v1.1 = 55 erros;
  - diff célula a célula com estilo;
  - md5 dos arquivos;
  - mutações.
- **Confiança: 90 %.** Falta: parecer ou prática da VMI sobre o U7 = U (R1), um FFData real e as validações do servidor EDS.

## Frentes

| Data | Frente | O quê |
|---|---|---|
| 2026-10-29 | pipeline (auditor independente) | Revalidação das specs GPM v1.2. Só leitura, nenhum arquivo alterado além deste relatório. |

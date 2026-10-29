# REVAL-SAM — revalidação independente da spec LT-SODRA-003 (SAM) v1.1

- **Artefato:** `2026-10-29-correcoes/LT-SODRA-003-SAM-Spec_v1.1.xlsx` (md5 `f3ce3b9db77c2543423049ca4310ee1c`). Base: `2026-10-27-reports/specs-drive/LT-SODRA-003-SAM-Spec.xlsx` (v1.0, md5 `b6a8074989c7be3948e1a6f43db39d64`, conferido inalterado).
- **Achados que a v1.1 devia fechar:** [[Research Pipeline/Lithuania/2026-10-28-validacao/VAL-SAM|VAL-SAM]] S1–S16. Changelog do construtor ([[Research Pipeline/Lithuania/2026-10-29-correcoes/CHANGELOG-SAM-v1.1|CHANGELOG-SAM-v1.1]]) usado só como referência. O `check_sam.py` do construtor **não** foi usado.
- **Revisor:** auditor independente (não construiu a v1.1). Data: 2026-10-29. Só leitura: nenhum arquivo existente foi alterado.
- **Hub:** [[Lituania]]

## Veredito

**PASS com ressalvas: 0 BLOCKER, 0 MAJOR, 7 MINOR. Confiança: 92 %.**

Os três BLOCKER da v1.0 foram fechados: S1 (envelope FFData), S2 (vírgula decimal) e S3 (marcas 0/1). Meu verificador conferiu o Sample File contra o FFData oficial e contra a DSA. Elementos, atributos, nomes de campo, ordem de campo por página, Count 27/63/48 e todas as contas batem. Os cinco MAJOR também foram tratados: S4–S6 fechados; S7 e S8 com resíduo que depende de fonte ainda não lida, declarado na spec como item em aberto. Sobram sete MINOR: uma divergência de tamanho com a DSA que a spec não registra (TaxRate do SAM3SDP), uma propagação incompleta de S15, uma afirmação sem fonte sobre o teto e quatro inconsistências de texto ou de formato. Nenhuma delas impede o Development de gerar um arquivo válido.

## Achados novos ou remanescentes

| ID | Aba!Célula | Problema | Fonte | Sev. |
|---|---|---|---|---|
| R1 | `SAM Spec!I69`, `J69`, `M69` | TaxRate do SAM3SDP tem tamanho 5 na spec. A DSA §7 (p. 11) dá **11** ("P3 TaxRate_IDX … Skaičius 11"); a §6 (p. 11) e o MXFD dão 5. A spec não registra a divergência: `M69` diz "5 cells" e `J69` perdeu o comprimento ("Number, 2 dp, decimal comma"), enquanto `J46` diz "5 characters". Por isso a checagem "67/67 = DSA" dá **66/67**. O valor 21,27 cabe nos dois tamanhos. O changelog cita o ponto, mas a planilha não. | DSA §6–§7 p. 11 | MINOR |
| R2 | `Example Analysis!C6`, `D6` | S15 foi corrigido só em `SAM Spec!M7`/`T7`. A Example Analysis ainda diz "NAME/CONTENT MISMATCH … Raised as a Query to RA" e cita o comentário 'Draudejo adresas', sem a citação da DSA que fecha a query. | DSA §5 p. 9 ("InsurerAddress – Draudėjo el. pašto adresas") | MINOR |
| R3 | `Population Rules!D7` | "where only PSD 6,98 continues above the ceiling": **⚠️ sem fonte** para o Garantinis fondas, o Ilgalaikio darbo išmokų fondas e o +3 %. O art. 10(9) da I-1336 zera acima de 60 VDU as contribuições "pagal … rodiklių patvirtinimo įstatymu patvirtintus tarifus" (exceto PSD). As taxas do GF e do ILDIF não estão na XV-632 (o extrato confirma) e foram lidas só na página da Sodra. Não há fonte lida que diga se elas param no teto. (`SAM Spec!M47`, "0 % above it except PSD", está correto para a VSD.) | I-1336 art. 10(9) (extrato 2026-10-27); XV-632 art. 3 (extrato) | MINOR |
| R4 | `Field Options!E45:E60` | "budget institutions and the Bank of Lithuania do not pay them": a lista de quem não paga o **GF** está incompleta. A página da Sodra lista também partidos políticos, sindicatos e comunidades religiosas. Para o ILDIF, a lista está certa. | `2026-10-27-sodra-tarifas-2026-PSD-fundos_extrato.md` | MINOR |
| R5 | `Version Control!C3`, `E3` | `C3` = "29-Oct-26", fora do formato de `C2` ("2026-08-21"). `E3` é verdadeira (conferi item a item), mas tem 738 caracteres, o que não é uma linha curta. Sugestão: "Corrections VAL-SAM S1–S16: FFData envelope per DSA (V-624), decimal comma, checkmarks 0/1, month 1–12, DocDate/DocNumber empty, 2026 P3 rates, 60 VDU/MMA edge cases, examples recomputed." | — | MINOR |
| R6 | `Field Options!E25`, `E26` | Ainda dizem "0-9999 pages", enquanto `File Structure!C5`/`C7` (v1.1) dizem "unlimited (DSA section 4)". O MXFD tem MaxOccur 9999 e a DSA §4 diz "Neribojama". Os dois valores têm base, mas a spec se contradiz. | DSA §4 p. 9 | MINOR |
| R7 | `Example Analysis!C11`; `SAM Spec!K30`, `Sample File!B50` | `C11` ainda escreve "EUR 3,000.00", enquanto `C13`/`C14` (v1.1) usam "3 000,00". "Rita Ritaite" está sem diacrítico (Ritaitė), e a própria spec (`M44`, `M63`) manda preservar os diacríticos. Ambos vêm da v1.0 e são cosméticos. | spec `M44`/`M63` | MINOR |

Nenhum achado BLOCKER ou MAJOR.

## Status S1–S16

| Achado | Status | Evidência (célula) |
|---|---|---|
| S1 envelope FFData | **Fechado** | `Sample File!B3:B176`: `FFData(Version, CreatedByApp, CreatedByLogin, CreatedOn) > Form(FormDefId, FormLocation) > DocumentPages/Group "Forma" > ListPages + Group "Priedas SAM3SD"/"Priedas SAM3SDP" aninhados + Pages Count=3 > Page(PageDefName, PageNumber) > Fields Count 27/63/48 > Field Name`. Atributos, nomes e ordem iguais ao FFData oficial (SAM, SAM3SD) e ao exemplo da DSA p. 8–9 (SAM3SDP). `File Structure!C2`, `C4`, `C5`, `C7` reescritos. |
| S2 vírgula decimal | **Fechado** | Nenhum ponto decimal no XML nem na coluna K. `J20`, `J21`, `J25`, `J26`, `J45:J49`, `J68:J72` dizem "decimal comma". |
| S3 marcas 0/1 | **Fechado** | `K13`=0, `K17`=1, `K22`=1; `O13`/`O17`/`O22`="0;1"; `Field Options!B28`/`B29`=1, `B43`/`B44`=0; XML `RevisedDocument` 0, `Appendixes2`/`Appendixes3` 1. |
| S4 mês 1–12 | **Fechado** | `K12`=7; `O12`/`O15`="1;…;12"; `Field Options!B12:B23`=1..12; `Example Analysis!A7`=7; XML `CycleMonth`=7. |
| S5 DocDate/DocNumber | **Fechado** | `F8`, `F9`, `F37`, `F38`, `F56`, `F57`=N; `K8`, `K9`, `K37`, `K38`, `K56`, `K57` vazios; XML vazio nas três páginas; `M8` registra que o eFormFiller preenche o campo (o FFData oficial traz os dois preenchidos). |
| S6 taxa 39,58 | **Fechado** | `K46`=21,27; `K47`=638,10; `Example Analysis!A12:A13` refeitos; nenhum "39,58"/"39.58"/"1187" restante. |
| S7 taxas P3 2026 | **Parcial (resíduo legítimo)** | `Field Options!A45:E60` tem as 16 linhas, todas refeitas (ver verificador). A query "one side only" foi fechada como total (`T46`). Ficam em aberto, declarados em `T46`, `T69`, `E30` e `Report Matrix!J2`: o +3 %, a base legal do GF/ILDIF e a composição dos códigos 06/09/10. Nenhuma fonte primária lida responde a esses pontos. |
| S8 teto 60 VDU / MMA | **Parcial (resíduo legítimo)** | `Population Rules!C7`/`D7` e `SAM Spec!M47` trazem €138 729,00 e €1 153 com fonte. Continua aberto como a Sodra quer A11/P3/A12 preenchidos nesses casos (declarado). Ver R3. |
| S9 afirmação negativa / 93 % | **Fechado** | `Report Matrix!J2` retira os 93 %; `Sample File!B2` e `File Structure!C2` citam a DSA; "largest open item" removido de `Population Rules!C13`. `Version Control!E2` foi mantido como histórico, o que é aceitável. |
| S10 contas 128/22 | **Fechado** | `K18`=`K35`=22=⌈128/6⌉; `K20`=384000,00; `K21`=81676,80=128×638,10; `K27`=23; `Example Analysis!A9`/`C9`/`D10` coerentes. |
| S11 códigos pessoais | **Fechado** | `K40`=38507159910 e `K59`=37603099979 válidos; os 7 códigos do XML são válidos e o 1º dígito confere com o gênero. |
| S12 FormVersion 2 | **Fechado** | `I32`, `I51`, `I74`=2 (DSA "Tekstas 2"). Ver R1 para o TaxRate do SAM3SDP. |
| S13 "ponto 1488" | **Fechado** | Frase retirada de `Population Rules!C13`/`D13`; nenhuma ocorrência de "1488". |
| S14 canal / BOM / assinatura | **Fechado** | `Report Matrix!G2`/`H2`, `Population Rules!C13`/`D13`, `File Structure!C2`: DataService, endpoint, operações, "UTF-8 without BOM", assinatura qualificada. Tudo confere com o extrato EDAS-DataService. |
| S15 box 7 = e-mail | **Parcial** | `SAM Spec!M7` corrigido e `T7` limpo, mas `Example Analysis!C6`/`D6` estão desatualizados (R2). |
| S16 diacríticos ReasonText | **Fechado** | `K65` e XML: "civilinę sutartį". |

Placar: 12 fechados, 4 parciais (S7 e S8 por falta de fonte, declarados na spec; S15 por propagação; S12 fechado, mas com a lacuna R1 ao lado).

## Valores estatutários reabertos na fonte

| Valor na v1.1 | Fonte lida nesta revalidação | Resultado |
|---|---|---|
| Empregado 12,52 = 8,72 + 1,99 + 1,81 | XV-632 art. 3(4) (extrato e-TAR 2026-10-27) | Confere. Vigência a partir de 2026-01-01. |
| PSD 6,98 | I-1343 art. 17(2) (extrato no arquivo de tarifas Sodra 2026) | Confere |
| Desemprego 1,31 / 2,03 | XV-632 art. 3(1) | Confere |
| Acidentes I 0,14 / II 0,49 / III 0,70 / IV 1,40 | XV-632 art. 3(3) | Confere |
| GF 0,16 + ILDIF 0,16 | Página de tarifas da Sodra 2026 (fonte oficial da autoridade; a lei não foi lida) | Confere com a página; a base legal está declarada como aberta na spec (`T46`) |
| +3 % de acumulação | Página de tarifas da Sodra ("papildomai priskaičiuojama 3 proc. įmoka") | O valor confere. A inclusão no P3 está marcada como NOT VERIFIED na spec (`E53:E60`), o que está correto. |
| 16 taxas de 21,27 a 26,25 | Soma refeita pelo verificador | 16/16 conferem. 21,27 também é o `TaxRate_1` do FFData oficial. |
| Teto 60 VDU = €138 729,00 | I-1336 art. 10(9) + XV-632 art. 4 ("2 312,15 euro") | Confere (60 × 2 312,15) |
| MMA €1 153 | Nutarimas 700 de 2025-10-16, p. 1 ("minimaliąją mėnesinę algą – 1153 eurai") | Confere (2026) |
| Base mínima MMA, 5 exceções, rateio por dias úteis | I-1336 art. 10(7)–(8) (extrato) | `Population Rules!C7` confere |
| Regras de formato | DSA §1 (UTF-8, 1 arquivo = 1 notificação), §2.1–2.10 p. 1–6, §3 p. 6–9, §4 p. 9, §5–§7 p. 9–12 (PDF lido por pypdf, md5 `1db02c71…`) | Conferem (exceto R1) |
| UTF-8 sem BOM, DataService, assinatura qualificada | Extrato EDAS-DataService (p. 4–15 da instrução; página da Sodra) | Confere |

Valor sem fonte: só o de R3 ("only PSD continues above the ceiling", para GF/ILDIF/+3 %).

## Regressões contra a v1.0 e forma

- **Nomes e tamanhos:** 67 campos lógicos. Contra a v1.0, só mudaram `I32`, `I51` e `I74` (10 → 2), como pedido em S12; nenhum nome de campo mudou. Contra a DSA: 66/67, com a divergência R1.
- **Fill:** 522 células alteradas, todas com `FFDDEBF7`; nenhuma célula inalterada com `FFDDEBF7`.
- **"=":** nenhuma célula começa com "=" e não há fórmula.
- **Abas:** 9, na mesma ordem da v1.0. O pacote zip tem 35 partes, as mesmas da v1.0, e `testzip` passa.
- **Version Control:** existe a linha 3 (v1.1); ver R5.

## Dados pessoais

- O login de autor do FFData oficial **não aparece** na v1.1 (busca por palavra inteira; o valor não foi impresso). Os nomes, códigos, telefones e e-mails do FFData oficial também não aparecem. A única coincidência foi o placeholder de anonimização "NAME", igual à palavra inglesa "NAME" já presente na v1.0, e foi descartada como falso positivo.
- `SAM_2024_11 (1) - Client Example.pdf`: busquei números de 7 a 11 dígitos, e-mails e sobrenomes lituanos do PDF na v1.1. Só vieram rótulos de formulário ("Patikslintas"/"Ataskaitinis"); nenhum dado do cliente foi copiado.
- Todos os dados de exemplo são fictícios: códigos pessoais gerados com dígito de controle válido, "UAB PAVYZDYS", `pavyzdys.lt`, `CreatedByLogin="username"` (como no exemplo da DSA 2.1), código de empresa 302123442 com mod 11 válido.

## Saída do verificador

Verificador próprio, escrito do zero: `reval_sam.py`, no scratchpad da sessão (md5 `8379e5ec09b18afa2fc4affe4d6d4cbe`). Comando: `python -I reval_sam.py <v1.1.xlsx> <v1.0.xlsx> "<SAM-V07 SAMPLE (1).ffdata>" <texto da DSA extraído por pypdf>`.

O que ele faz:
- extrai o XML de `Sample File!B3:B176`;
- compara com o FFData oficial: só nomes de atributo, estrutura e nomes de campo, sem imprimir valores;
- compara com a DSA: tamanhos da §5–§7 e ordem da §3;
- refaz todas as contas em Decimal com arredondamento half-up;
- aplica o `ID_formatas_simple_f` do GPM313.mxfd: 11 dígitos com pesos 1-9,1 / 3-9,1-3 e validação da data; 9 dígitos com pesos 1–8;
- recompõe as 16 taxas a partir das parcelas da lei.

```
OK    9 abas, mesma ordem da v1.0
OK    nenhuma celula comeca com "=" (0)
OK    nenhuma formula (0)
OK    522 celulas alteradas; todas com fill FFDDEBF7 (sem fill: 0)
OK    nenhuma celula inalterada com FFDDEBF7 (0)
OK    Version Control B3 = 1.1
FAIL  Version Control E3 curta (<=400 car.): 738 car.                      -> R5
FAIL  Version Control C3 no formato de C2: C2=2026-08-21 C3=29-Oct-26      -> R5
OK    nomes da tabela DSA presentes no texto extraido do PDF
OK    DSA: 27 + 18 + 22 = 67 campos logicos
OK    SAM Spec: 67 campos logicos na coluna H
FAIL  nomes e tamanhos 67/67 = DSA; divergencias: ['SAM3SDP/TaxRate spec I69=5 x DSA=11']  -> R1
INFO  H/I alterados vs v1.0: FormVersion I32/I51/I74: 10->2
OK    Sample File sem BOM; declaracao XML UTF-8; coluna A 1..174 sem buraco
OK    FFData: mesmos NOMES de atributo do oficial; Version=1; CreatedOn AAAA-MM-DD; CreatedByLogin generico
OK    um unico <Form>; atributos e FormDefId {963BF380-...} = oficial = DSA 2.2
OK    Form > DocumentPages, Pages (DSA 2.2)
INFO  FFData oficial: Form tem tambem FormErrors (log do eFormFiller; nao consta da DSA)
OK    DocumentPages: Forma > ListPages(SAM) + Group "Priedas SAM3SD" aninhado = oficial
OK    DocumentPages: Group "Priedas SAM3SDP" aninhado em Forma (DSA p. 6)
OK    Pages Count=3 = 3 Page; PageNumber 1..3; ordem SAM, SAM3SD, SAM3SDP
OK    SAM:     atributos de Page; Fields Count=27=27; nomes unicos; Field so Name; nomes E ordem = FFData oficial; conjunto = DSA; tamanhos <= DSA
OK    SAM3SD:  atributos de Page; Fields Count=63=63; nomes unicos; Field so Name; nomes E ordem = FFData oficial; conjunto = DSA; tamanhos <= DSA
OK    SAM3SDP: atributos de Page; Fields Count=48=48; nomes unicos; Field so Name; nomes e ordem = exemplo DSA p. 8-9; conjunto = DSA; tamanhos <= DSA
OK    decimais com virgula e 2 casas; nenhum ponto decimal no XML
OK    marcas 0/1: RevisedDocument 0, Appendixes2 1, Appendixes3 1
OK    CycleMonth=7 (1-12 sem zero); P14T/P17T vazios com P35=0; datas AAAA-MM-DD
OK    SAM/SAM3SD/SAM3SDP: DocDate/DocNumber vazios; FormCode/FormVersion 07 como Field
OK    SAM3SD linhas 1-6: A11 3000.00 x P3 21.27 % = 638.10 = A12 (6/6); RowNumber 1..6
OK    SAM3SD: P7 18000,00 = soma A11; P8 3828,60 = soma A12; InsurerCode = titulo; PageTotal 1 = folhas do anexo
OK    SAM3SDP linha 1: A11 1500.00 x 21.27 % = 319.05 = A12; linhas 2-3 vazias por inteiro
OK    SAM3SDP: P7 1500,00; P8 319,05; InsurerCode = titulo; PageTotal 1
OK    P20.2-.5: folhas 1, pessoas 6, renda 18000,00, contrib 3828,60 = anexo; P20.1 = 1
OK    P21.2-.5: folhas 1, pessoas 1, renda 1500,00, contrib 319,05 = anexo; P21.1 = 1
OK    P23 2 = P20.2 + P21.2
OK    7 codigos pessoais (6 SAM3SD + 1 SAM3SDP): digito de controle e data validos; 1o digito coerente com o genero
OK    SAM Spec K40 38507159910 e K59 37603099979: digito valido
OK    JuridicalPersonCode 302123442: mod 11 pesos 1-8 valido; = SAM Spec K5 = Example Analysis A5
OK    controle: v1.0 302123456 era invalido
OK    K47 = K45 x K46 (638.10); K48 = 6 x K45; K49 = 6 x K47
OK    K18 = K35 = ceil(128/6) = 22; K20 = 384000.00; K21 = 81676.80; K27 23 = K18 + K23
OK    K25/K26 = K68,K71 / K70,K72; K70 = K68 x K69
OK    K12=7; K13/K17/K22 = 0/1/1; coluna K sem ponto decimal
OK    K8,K9,K37,K38,K56,K57 vazios; F8,F9,F37,F38,F56,F57 = N; I32/I51/I74 = 2
OK    Example Analysis A11-A14 = K45-K48; A9/A10 = K27/K19; A18 = 1500 x A17
FAIL  Example Analysis D6 sem a query de box 7 (S15 propagado)              -> R2
OK    XV-632 art. 3(4): 8,72 + 1,99 + 1,81 = 12,52
OK    Field Options B45..B60: 16/16 = 12,52 + 6,98 + desemprego + acidentes + 0,32 (+3)
OK    16 linhas; min 21.27 max 26.25
OK    teto 60 x 2312,15 = 138729,00
INFO  1 valor do FFData oficial e placeholder de anonimizacao ("NAME"), excluido da busca
OK    nenhum login/dado de identificacao do FFData oficial na v1.1 (0 ocorrencias; valores nao impressos)

RESUMO: 140 OK, 4 FAIL   (os 4 FAIL = R1, R2, R5, todos MINOR)
```

Linhas idênticas foram agrupadas acima; a saída bruta tem uma linha por checagem.

## Não verificável nesta sessão

- O MXFD vigente (FormDef 2021-12-22) no original: há só o extrato. O tamanho 5 do TaxRate vem do MXFD de 2018 e do extrato.
- A base legal do GF e do ILDIF, e se elas e o +3 % entram no P3 ou param no teto (R3, S7).
- Como a Sodra quer o A11/P3/A12 no mês do teto e na complementação até o MMA (S8).
- A aceitação real do arquivo pelo EDAS/DataService: não houve envio de teste.
- A numeração fina da V-243 consolidada (56.x, 86.x, 91.3.1 etc.), já listada na VAL-SAM.

## Bloco de prova

- **Pedido → resposta:**
  1. Verificador próprio: feito, 140 OK / 4 FAIL, todos MINOR.
  2. S1–S16: 12 fechados, 4 parciais (S7, S8, S15, e S12 com a lacuna R1 ao lado).
  3. Valores reabertos: todos conferem com a fonte (artigo e página acima). Um sem fonte (R3).
  4. Regressões: nenhuma nos nomes; o tamanho difere da DSA em 1 campo, sem registro (R1); fill 522/522; nenhum "="; 9 abas; Version Control com linha v1.1 verdadeira, mas longa e com data fora do padrão (R5).
  5. Dados pessoais: nenhum.
- **Fontes:** DSA V-624 §1–§7 p. 1–12 (`SAM specifications - Lithuanian.pdf`, md5 `1db02c71a74cc0bed1b5c5f2cd01d53b`); FFData oficial (md5 `59d62cc2f1414a5c3462d8c2b84e7940`, só estrutura); I-1336 art. 10(7)–(9); XV-632 art. 3(1)–(4) e art. 4; I-1343 art. 17(2); Nutarimas 700/2025 p. 1; página de tarifas Sodra 2026; extrato EDAS-DataService; GPM313.mxfd `ID_formatas_simple_f`.
- **Teste mecânico:** verificador próprio (acima); md5 dos arquivos; diff célula a célula v1.0 × v1.1; `zipfile.testzip`; busca de dados pessoais por palavra inteira, sem impressão dos valores.
- **Confiança: 92 %.** O que falta para 100 %: o MXFD de 2021 no original, a base legal do GF/ILDIF e um envio de teste ao EDAS.

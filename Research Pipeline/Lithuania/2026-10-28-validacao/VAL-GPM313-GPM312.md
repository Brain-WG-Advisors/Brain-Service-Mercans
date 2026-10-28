# Validação independente: specs GPM313 e GPM312 v1.1 (Lituânia)

- **Data:** 2026-10-28
- **Revisor:** compliance-qa-auditor (independente; não construiu os arquivos; artefatos não foram alterados)
- **Arquivos revisados:**
  - `Research Pipeline/Lithuania/2026-10-27-reports/LT-VMI-001-GPM313-Spec_v1.1.xlsx`
  - `Research Pipeline/Lithuania/2026-10-27-reports/LT-VMI-002-GPM312-Spec_v1.1.xlsx`
  - Base de comparação: `specs-drive/LT-VMI-001-GPM313-Spec.xlsx` e `specs-drive/LT-VMI-002-GPM312-Spec.xlsx` (v1.0)
- **Fontes primárias (locais, VMI):** `raw/docs/oficiais/LT/2026-10-27-VMI-reports/`
  - `GPM313.mxfd`: FormDef 2025-11-04; versão EDS 2025-12-31; md5 do conteúdo = zip.
  - `GPM312.mxfd`: FormDef 2026-05-11; versão EDS 2026-06-12; md5 do conteúdo = zip.
  - `IN_GPM313_nuo_2026.docx` (VA-121, redação VA-105) e `IN_GPM312.docx` (VA-9, redação VA-24).
  - `GPMI-IX-1007-suvestine-2026-06-11_2026-12-31.pdf`.
  - `XV-632-...-rodikliai_extrato.txt` (VDU 2026).
- **Método:** tudo foi medido nesta sessão, sem reaproveitar número de terceiros.
  - Parse do XML dos dois MXFD (FieldDataDefs com nome, tipo, células × linhas, decimais, mínimo, IsRequired e ListItems) e extração do ScriptModule VBScript das validações (3.981 linhas no GPM312, 342 no GPM313).
  - Texto das IN extraído por python-docx.
  - Diff célula a célula v1.0 × v1.1 com leitura do preenchimento.
  - Algoritmos de dígito verificador do próprio MXFD (`JAR_tikrinimas`, `AK_tikrinimas`, `PVM_kodas`) reimplementados e aplicados às amostras.

## Veredito

**FAIL (reprovado).** O formato eletrônico (nomes XML, tamanhos, listas) está correto e completo. Mesmo assim, o pacote não pode ser entregue como pronto porque os **exemplos e as amostras** falham nas validações do próprio formulário da VMI:

- o código do pagador `302123456`, nos dois reports;
- o código PVM do U1;
- a linha U2 = 6 de dividendos em 2026.

Além disso, há **2 regras de obrigatoriedade erradas no GPM312 (U12/U15)** e **totais da amostra GPM312 que não fecham**.

**Confiança: 90%.**
- Os achados mecânicos (nomes, tamanhos, listas, dígitos verificadores, somas, diff) estão a 100%.
- O restante depende de pontos não verificáveis localmente: a representação exata no FFData (separador decimal) e a validação no servidor EDS além do script do MXFD.

## Achados

Severidade:
- **BLOCKER:** impede a entrega.
- **MAJOR:** corrigir antes de o Development construir.
- **MINOR:** corrigir antes de fechar.

| ID | Local (arquivo!aba!célula) | O que a spec diz | O que a fonte diz (local exato) | Sev. |
|---|---|---|---|---|
| B1 | GPM313!GPM313 Spec!K3; Example Analysis!A2; Sample File!B6. GPM312!GPM312 Spec!K3, K12, K29; Example Analysis!A2; Sample File!B6, B16, B30 | Exemplo do NIF do pagador `302123456` (9 dígitos) | O MXFD valida o código de 9 dígitos assim: Σ dígito(i)×i para i = 1..8, mod 11; se o resultado for ≥ 10, dá **erro**. Para 302123456 a soma é 109, e 109 mod 11 = 10, então o EDS rejeita. Fontes: GPM313.mxfd ScriptModule `ID_formatas_simple_f` (case 9) e GPM312.mxfd `JAR_tikrinimas`, chamada na verificação do B_MM_ID ("1 laukelyje įrašytas neteisingas mokesčių mokėtojo identifikacinis numeris"). Trocar por um código que passe, p. ex. `302123442` (conferido com o algoritmo). | BLOCKER |
| B2 | GPM312!GPM312 Spec!K31 e K32 | U1 = `LT100001234567`, U2 = `3` (código PVM) | A função `PVM_kodas` do GPM312.mxfd exige 14 caracteres, "LT" + 12 dígitos e o 13º caractere = "1". Aqui o 13º é "6", o que gera **erro** "U1 laukelyje nurodytas neteisingas PVM mokėtojo kodas". Há também incoerência interna: a Sample File (linha U de não residente, B35) deixa U1/U2 vazios. Usar um código PVM válido (p. ex. `LT100000000014`, que passa no algoritmo) ou deixar U1/U2 vazios, como na amostra (regra 42, último parágrafo). | BLOCKER |
| B3 | GPM312!Sample File!B38, B39; Example Analysis!A17/D17 | Linha U de 2026 com U1 `LT100001234567`, U2 = 6, U5 = 26 (dividendos), U14 = LT e U15 preenchido | O script do GPM312.mxfd gera **3 erros** nessa linha. Ela não passa no EDS. Para 2026, retirar o exemplo de dividendos (U2 = 6 só vale para 62/67/51/52) e deixar U12, U13 e U15 vazios. (1) Para período > 2025, U2 = 6 só é aceito com U5 ∈ {62, 67, 52, 51}: "U2 laukelyje pasirinkta kodo rūšis naudojama tik U5 laukelyje nurodžius atlikėjo ar sporto veiklos, dividendų, honorarų ar palūkanų išmokas". A IN_GPM312, regra 37, 2º parágrafo, limita os dividendos a intermediário ao "2025 metų Deklaracijos U priedas". (2) Com U2 = 6, "nepildomi U12, U13, U15 laukeliai" (erro), e a amostra preenche U15. (3) Com U2 = 6, U14 = LT e U5 = 26, o U1 tem de ter 9 ou 10 dígitos e passar no JAR/TIN, senão dá erro "U1 laukelyje nurodytas neteisingas kodas". | BLOCKER |
| M1 | GPM312!GPM312 Spec!F42 (U12) e F45 (U15); Population Rules!C15 | U12 e U15 com Mandatory = `Y`; C15: "U12 ... must be treated as a hard requirement" | O GPM312.mxfd tem IsRequired = false. Pelo script, U12/U13/U15 são **proibidos** quando U2 = 6 (erro citado em B3). U12 só é exigido se U13 estiver vazio, U14 ≠ LT e U2 ≠ 6: "turi būti užpildyti U12 ir / ar U13 laukeliai". A falta de U15 só gera aviso. Esperado: F42 e F45 = `C`, com a condição na coluna G, e C15 reescrito. | MAJOR |
| M2 | GPM312!Sample File!B9, B10 e GPM312 Spec!K6, K7 | Caixa 4 = 2211000,00; caixa 5 = 392000,00 | A amostra tem 1 página L e 1 página U. ΣL8 + ΣU8 = 104 600,00 + 346 000,00 = **450 600,00**; ΣL10 + ΣU10 = 19 660,00 + 56 700,00 = **76 360,00** (regras 14 e 15 da IN_GPM312). O próprio MXFD recalcula G4 e G5 (`setcheckvalue sumLU8/sumLU10`, script linhas 1265–1311). As caixas 4–5 (e K6/K7) devem ser iguais às somas das linhas mostradas. | MAJOR |
| M3 | GPM313!GPM313 Spec!K9–K15; GPM312!GPM312 Spec!K6–K9, K21–K26, K38–K41; GPM312!Example Analysis!A12–A15 (A13 = `20.00`, alterada na v1.1) | Valores com ponto decimal (`184250.00`, `20.00`); a coluna J diz só "Decimal, 2 dp" | Todos os campos Decimal dos dois MXFD declaram `<DecimalSeparator>,</DecimalSeparator>`, e o script faz `Form.SetDefaultDecimalSeparator ","`. As listas L9/U9 são `20,00`, `25,00` etc. (UseListOnly). Um gerador que siga K/J emitindo `20.00` arrisca falhar a lista. Esperado: J declara o separador "," e os exemplos usam vírgula, ou se registra que a forma no FFData está confirmada por amostra real. A alegação do CONFERENCIA ("20,00 × 20.00 corrigido") normalizou para ponto, ao contrário do MXFD. | MAJOR |
| M4 | GPM312!GPM312 Spec!K14; Example Analysis!A4; Sample File!B20, B21, B24 | L1 = `39001010101` e `47712120987` | Pelo `AK_tikrinimas` do GPM312.mxfd (pesos 1..9,1; segunda volta 3..9,1,2,3; mod 11), o dígito correto de 39001010101 é 9 e o de 47712120987 é 8, então os dois **falham**. O EDS dá aviso "Pasitikrinkite L1 laukelyje įrašytą asmens kodą". Trocar por códigos que passem (p. ex. `39001010109`). O 1º dígito também deve bater com o sexo do nome fictício (3 = masculino 1900–1999, 4 = feminino): B22 usa um nome feminino com 3…, e B24 um nome masculino com 4…. | MAJOR |
| M5 | GPM312!Field Options!E70; Population Rules!C4, D4; Example Analysis!D17 | U2 = 6 "used for the rules 37-38 cases where interest, dividends or royalties were paid…" | Para 2026, o script aceita U2 = 6 só com U5 62, 67, 52 e 51. Isso inclui o novo caso da regra 36-1 (artista ou desportista pago a terceiro, códigos 51/52). Exclui os dividendos (26), que pela regra 37 valem só para o período 2025-01-01..06-30. Esperado: texto com o domínio de 2026 (62/67/51/52) e citação da regra 36-1. | MAJOR |
| M6 | GPM313!Population Rules!A11–D11 (e spec em geral) | Retificação: só as regras 18, 19.2 e 20 | A IN_GPM313, regra 21, prevê retificar a declaração do mês do pagamento quando o imposto estrangeiro sobre salário de trabalho em país com tratado é pago num mês posterior do mesmo período. Essas importâncias passam a não tributáveis e saem da caixa 5. A regra não aparece em nenhuma célula (busca por "rule 21" = 0). Esperado: incluir o caso em Population Rules A11/C5 (expatriados). | MAJOR |
| m1 | GPM313!GPM313 Spec!J3; GPM312!GPM312 Spec!J3, J12, J29; GPM312!GPM312 Spec!J14 | "Numeric, 9 or 11 digits"; L1 "Numeric 11…" | GPM313.mxfd script linha 20 e GPM312.mxfd linha 1204: B_MM_ID aceita **9, 10 ou 11** dígitos (10 = código atribuído pela VMI). Com L2 = 1, o L1 aceita 10 ou 11 dígitos (`TIN_tikrinimas`/`AK_tikrinimas`, linhas 1466–1480). | MINOR |
| m2 | GPM313!File Structure!C8; GPM312!File Structure!C10 (e coluna H) | Lista só os campos de dados | Os dois MXFD têm ainda `B_FormNr` (6/7 células) e `B_FormVerNr` (2) em cada página (GPM313, GPM312, GPM312L, GPM312U), com IsRequired = false. Esperado: citá-los como campos de sistema da forma, não preenchidos pelo payroll. | MINOR |
| m3 | GPM313!Sample File!B4; Example Analysis!D5 | "Pateikimo terminas: 2026-08-15" / "due by 15 August 2026" | 2026-08-15 é sábado (e feriado). A própria spec GPM312 (GPM312 Spec!T37) aplica a prorrogação ao dia útil seguinte ("2025 return deadline of 2026-02-16"; 15/02/2026 = domingo). Há incoerência entre as specs. O texto da IN_GPM313, regra 12, diz só "iki kito mėnesio 15 dienos", e a regra de prorrogação (Lei de Administração Tributária) não está nas fontes locais, então a confirmação vai para o source-hunter. | MINOR |
| m4 | GPM312!Sample File!B25 | Código 92 (verslo liudijimas) com L1 = passaporte, L2 = 5 | IN_GPM312, regra 23, 2º parágrafo: para pagamento a titular de verslo liudijimas, o L1 é obrigatoriamente os 8 primeiros caracteres do certificado (L2 = 2). O passaporte é o último recurso (regra 23, último parágrafo), incoerente com o código 92. | MINOR |
| m5 | GPM312!Sample File!B24 | Código 44 (tantjemos) com L7 = M | IN_GPM312, regra 29.2: M marca pagamentos da MB ao próprio membro por contrato civil. Os exemplos da regra são os códigos 77, 23, 24, 58, 35, 92 e 93; o 44 (tantjemos de valdyba/stebėtojų taryba) não está entre eles. Trocar por 77. | MINOR |
| m6 | GPM312!GPM312 Spec!T6, T31, T37 | Perguntas abertas ao RA | O MXFD já responde a três delas. **T6:** o script exclui as linhas `C` da caixa 4 (`If L7 <> "C" Then sumL8 = …`, linhas 1273–1275 e 1290–1292). **T31:** U1 e U2 vazios são aceitos juntos; o erro só ocorre se um estiver preenchido e o outro não (linhas 2537–2540). **T37:** o marcador `U` só existe para período > 2025 (linhas 682–688). As respostas devem ser registradas e as perguntas fechadas. | MINOR |
| m7 | GPM313!Version Control!E3; GPM312!Version Control!E3 | "No change to the content rules"; o log lista só H/I/File Structure/Report Matrix | O diff mostra outras mudanças fora do log. **GPM313:** F9–F11 de Y→C, G9–G11 novos, mês 07→7 (J7, K7, O7, Field Options B2–B10, Example A5, Sample B9). **GPM312:** F6–F8 de Y→C, listas L9/U9 (J22, K22, J39, K39), Field Options E90/E91, Population Rules C5/D15, Example A13/A18/D18, Sample B2/B35/B36. A obrigatoriedade e os valores aceitos mudaram. O log deve listá-los. | MINOR |
| m8 | GPM313!Field Options!B11, B12, B13 | Destacadas em FFDDEBF7 | Valores iguais aos da v1.0 (`10`, `11`, `12`). É destaque sem alteração; retirar o preenchimento. | MINOR |
| m9 | GPM312!File Structure!C9 | "63 codes in four groups:" seguido de 3 grupos | O 2 priedas da IN_GPM312 tem 3 seções (1, 2 e 3). Corrigir para "three groups". | MINOR |

## Checagens que passaram (com evidência)

1. **Campos × MXFD (script):**
   - GPM313: 12/12 nomes da coluna H existem no MXFD, com a coluna I igual a células × linhas (B_MM_ID 11; B_MM_Pavadinimas 58×2 = 116; Metai 4; Menuo 2; G5–G12 14).
   - GPM312: 41/41 iguais (Pavad 116; G4–G7 14; LapoNr 7; L1/U1 20; L2/U2 1; L3/U3 34; L4–L7/U4–U7 1/2; L8/U8 12; L9/U9 5; L10/L11/L13/U10/U11 11; L12/U14 2; U12 Date 10; U13 24; U15 68).
   - Nenhum campo de dados do MXFD falta na spec (só os de sistema citados em m2).
2. **Listas:**
   - Mês 1–12 sem zero (ListItems e erro "4 laukelyje neegzistuojantis mėnesis").
   - L2 1–5 e U2 1–6 (regras 24 e 43).
   - L4/U4 A/B, L6/U6 A/N, L7 D/M/P/C e U7 D/M/P/C/U (script: `U` só > 2025, regra 48.5).
   - L9 de 2026 = 0/5/15/20/25/32 e U9 = +7,5/10, ambos só com o código 62. O 27% não tem código em 2026 (listas por taxa no script, linhas 1898–2051 e 2945–3148).
   - Linhas por página: L 10 e U 5 (L1-1…L13-10; U1-1…U15-5).
   - U12 Date AAAA-MM-DD (`SetDefaultDateFormat DF_YearMonthDay, "-"`).
3. **Códigos do 2 priedas:**
   - 63 códigos na IN_GPM312 = 63 na lista do script para ≥ 2026 = 63 na Field Options. Nenhum a mais, nenhum a menos.
   - O 06 está na lista estática do MXFD, mas fica fora para 2026 por script.
   - A classe A, B ou A/B bate com o anexo nos 63 códigos.
4. **Regras estatutárias conferidas no texto:**
   - Prazo GPM313 "iki kito mėnesio 15 dienos" (IN313 regra 12; GPMI art. 24(2)).
   - Prazo GPM312 "iki kito mokestinio laikotarpio vasario 15 d." (IN312 regra 57; GPMI arts. 24(2) e 33(2)).
   - Divisão pela data de pagamento até / depois do dia 15 (IN313 regras 9.2–9.3 e 10.2–10.3; GPMI art. 23(3), que fixa o pagamento até o dia 15 ou até o último dia do mês).
   - Alíquotas 20/25/32 sobre 36/60 VDU (IN313 regras 9.5.1–9.5.3; GPMI art. 6(1)).
   - 15% sobre benefícios (IN313 regra 9.4; GPMI art. 6(6)(2)).
   - Regras 10.4.1–10.4.4 (15; 20/25/32; 5/20/25/32; 15/20/25/32), conferidas com GPMI arts. 6(2), 6(6) e 6(7).
   - VDU 2026 = EUR 2 312,15 (Lei XV-632, art. 4).
   - Regras 4, 5, 15–20 (GPM313) e regras 14–17, 22, 26, 29, 41, 42–56 e 61–65 (GPM312).
   - 1 priedas: pontos 1 (200 EUR, até 6 vezes) e 2 (2 500 EUR), e código 45.
5. **Diff v1.0 × v1.1:**
   - GPM313: 52 células alteradas, todas destacadas.
   - GPM312: 105 alteradas, todas destacadas; destaque = alteração (105/105).
   - A v1.0 não tinha nenhum FFDDEBF7.
   - A linha 1.1 está presente na Version Control das duas specs (precisão do texto em m7).
6. **Lint de resíduos:**
   - 0 ocorrências de "no FFData", "notional", "YYYYMMDD", placeholder, TBD, TODO, FIXME, XXX, "to be confirmed" e "to be verified" nas duas specs.
   - Os "2025" restantes são datas de instrumentos e da regra de jogo (2025-11-01), não valores velhos.
7. **`validate_workbook.py --artifact RSPEC`:**
   - GPM313: PASS (9 abas, blocker = 0, major = 0, minor = 0).
   - GPM312: PASS (9 abas, 0/0/0).
8. **Coerência entre abas:**
   - Report Matrix H2, File Structure (3.0 e nível 3), coluna H e Version Control citam o mesmo MXFD e a mesma versão EDS.
   - L7 com 4 valores e U7 com 5, iguais no core, na Field Options e nas Population Rules.
9. **Proveniência:**
   - md5 dos MXFD extraídos = conteúdo dos zips (dd3200bb… e 0ea0d014…).
   - Versões EDS 2025-12-31 e 2026-06-12 conferidas na listagem EDS salva.

## O que não foi possível conferir

- **Forma do valor no arquivo FFData** (separador decimal, data): não há XSD nem FFData real de amostra. Fechar com um FFData exportado do EDS (afeta M3).
- **Validações do lado servidor EDS** além do script do MXFD.
- **Textos consolidados no e-TAR** (VA-105, VA-24) e suas datas de entrada em vigor.
- **Numeração "§21" das regras EDS VA-72:** a lista é numerada automaticamente e o número se perde na extração. O conteúdo dos três canais (on-line, "Persiųsti failą", web service) foi confirmado no capítulo IV.
- **Regra de prorrogação de prazo** em dia não útil (Lei de Administração Tributária): não está nas fontes locais (m3). Vai para o source-hunter.
- **Tributação, em 2026, do salário de não residente por trabalho no exterior** (U7 = U com U9 = 20 e U10 = 19 200 na amostra GPM312 B35): GPMI art. 5(4)(5) fala em renda de fonte lituana, e a definição de fonte não foi lida. Pode exigir U9 = 0 (regra 50.2.1). Vai para o source-hunter.
- **GPMI art. 27(4), Lei das Pequenas Sociedades art. 7(4) e Lei de Jogos:** não lidos.
- **Textos descritivos dos 63 códigos** na Field Options: comparados só código e classe.
- **Conteúdo da lista de países** (L12/U14) contra a ISO 3166.

## Encaminhamento

- **artifact-builder (rodada 2):**
  - B1–B3, M1–M5, m1, m2, m4–m9.
  - Corrigir na fonte da spec e regenerar; não editar a cópia do Drive à mão.
- **source-hunter:**
  - m3 (prorrogação de prazo);
  - tributação U7 = U (amostra);
  - representação do FFData (M3).
- **Propagação:**
  - Se B1 mudar o código do pagador de exemplo, conferir as outras specs LT (SAM) e o LT-SIR-001, que podem usar o mesmo exemplo.
  - Se M1 mudar a obrigatoriedade de U12/U15, conferir o LT-SIR-001 e o DD (campos de não residente).

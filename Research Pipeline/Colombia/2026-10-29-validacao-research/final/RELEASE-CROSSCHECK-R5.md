# Release cross-check R5, finais da Colômbia (emissão 2026-11-02)

Ligado a [[CONFERENCIA]], [[CONFERENCIA-R5]] e [[RELEASE-CROSSCHECK]] (emissão anterior). Gerado por `final/scripts/release_crosscheck_r5.py` em 2026-11-02 10:35. Compara cada final com o seu DRAFT-R5 (`revisao/rodada5/`, md5 em `revisao/rodada5/MD5-DRAFTS-R5.txt`). Finais substituídos (30/10) em `final/_historico/2026-10-30/`.

## O que a ferramenta prova

1. **Conteúdo:** a única diferença de texto entre DRAFT-R5 e final são as edições declaradas em `final/scripts/release_r5_edits.py` (Version Control da versão emitida, com "Released 2026-11-02 — approved by Wallisson Gomes"; versão no cabeçalho e no rodapé do CCG; referências cruzadas de `XREF` e resíduos de `RESID` / `RESID_DOCX`, ver as seções próprias) (xlsx: valor e fórmula de todas as células de todas as abas; docx: todos os parágrafos do DRAFT com as alterações controladas aceitas). Cada edição declarada produziu exatamente o texto declarado.
2. **Formatação:** toda célula mantém a formatação do DRAFT, exceto o fundo de destaque `FFDDEBF7`, que nenhuma célula mantém. A estrutura das abas fora das células (colunas, mesclagens, alturas, painéis) e todas as outras partes do zip são idênticas byte a byte.
3. **Marcadores:** lint C29 (placeholder, TODO, TBD, FIXME, XXX, VERIFY No., to be confirmed / verified) e marcadores internos (COVAL, DRAFT, confiança, "Position -", rodada, IDs de achado, ferramentas internas, pipeline, outros países, frases de retrabalho). Ocorrências legítimas aparecem contadas, não escondidas.
4. **Metadados e estrutura:** sem alterações controladas, comentários no docx, rsids, controle de alterações ligado, propriedades personalizadas; criação = modificação = data de emissão, revisão 1, autor.
5. **Abre e calcula:** cada xlsx abre (openpyxl só leitura) e o docx abre (python-docx); zero erros de fórmula; nenhum estilo de linha/coluna com o azul; `validate_workbook.py` PASS em cada xlsx.
6. **Uma versão de cada final:** `final/` só tem os finais desta emissão e as duas specs inalteradas (md5 igual ao de 30/10).

## Resultado

| Artefato | Final | Versão | Edições declaradas conferidas | Outras medidas | Falhas | md5 final | md5 DRAFT |
|---|---|---|---|---|---|---|---|
| CCG | `CO-CCG-001-v1.6.docx` | 1.6 | 8 | declared footer edits verified 1; opens (python-docx) yes; paragraphs 7978 | 0 | `7c3e6b251431` | `a9dfa2b9f826` |
| WTC | `CO-WTC-001-v1.8.xlsx` | 1.8 | 5 | highlight removed 65; sheets 6; formula errors 0; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | `8e05d1c4306a` | `e96ff7e7ee06` |
| DD | `CO-DD-001-v1.5.xlsx` | 1.5 | 12 | highlight removed 12; sheets 8; formula errors 0; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | `3967d2327e3e` | `142af8a9209f` |
| NE | `specs/CO-DIAN-001-NominaElectronica-Spec.xlsx` | 1.2 | 10 | highlight removed 9; sheets 9; formula errors 0; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | `7cfd6c3e348a` | `eaceb7dd3aef` |
| F220 | `specs/CO-DIAN-004-Formulario220-Spec.xlsx` | 1.2 | 6 | highlight removed 27; sheets 9; formula errors 0; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | `ff2f90b8e6e2` | `9bba239c49ab` |
| F2276 | `specs/CO-DIAN-005-Formato2276-Spec.xlsx` | 1.2 | 6 | highlight removed 22; sheets 9; formula errors 0; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | `5c9c306d8e4a` | `457f6b3249d3` |
| CES006 | `specs/CO-CESANTIAS-006-ConsignacionAnual-Spec.xlsx` | 1.2 | 6 | highlight removed 7; sheets 9; formula errors 0; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | `08db9ccdcde0` | `c52cee0c1904` |
| PILA003 | `specs/CO-PILA-003-AportesSeguridadSocial-Spec.xlsx` | 1.2 | 6 | highlight removed 14; sheets 9; formula errors 0; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | `ecd9b7131696` | `b82308fc5c15` |
| PAYSLIP | `CO_Compliance_Payslip_Generator.xlsx` | 1.3 | 4 | highlight removed 14; sheets 8; formula errors 0; validate_workbook VERDICT   PASS  (blocker=0 major=0 minor=0) (exit 0) | 0 | `619c1410c707` | `31bc96a35998` |
| SIR | `CO-SIR-001-v1.3-texto-final.md` | 1.3 | - | blocks to paste 15; block lines changed (declared) 4 | 0 | `79b7f2df8bfa` | `c322875428a5` |
| =CO-DIAN-002-Fo | `specs/CO-DIAN-002-Formulario350-Spec.xlsx` | 1.1 | - | unchanged (md5 = issue 2026-10-30) yes | 0 | `97e1fae0ae35` | `97e1fae0ae35` |
| =CO-PILA-007-Ap | `specs/CO-PILA-007-AportesPensionados-Spec.xlsx` | 1.1 | - | unchanged (md5 = issue 2026-10-30) yes | 0 | `eae9a7955d23` | `eae9a7955d23` |

## Referências cruzadas

Citações de versão de outro artefato que ficaram velhas depois da emissão (CO-PILA-003 e CO-CESANTIAS-006 passaram a v1.2), corrigidas no final emitido por `final/scripts/release_xref.py` (edições declaradas em `XREF` de `release_r5_edits.py`; edição limpa, sem azul nem alteração controlada; linhas de Version Control não tocadas). A ferramenta prova: (a) o final difere da cópia do final emitido às 09:44 (`final/_historico/2026-11-02-antes-xref/`) só nas células declaradas (demais partes do zip byte a byte; demais células com valor, fórmula e estilo iguais); (b) nenhuma citação de versão de outro artefato diverge da vigente em nenhum final (fora Version Control; no SIR, só o texto dos blocos que vai para o Doc, sem a linha do Version history).

Vigentes: CCG v1.6, WTC v1.8, DD v1.5, SIR v1.3, DIAN-001 v1.2, DIAN-004 v1.2, DIAN-005 v1.2, CESANTIAS-006 v1.2, PILA-003 v1.2, DIAN-002 v1.1, PILA-007 v1.1, Payslip v1.3.

| Artefato | Célula | Antes | Depois |
|---|---|---|---|
| DD | Country Fields!W112 | CO-PILA-003 v1.1 | CO-PILA-003 v1.2 |
| DD | Country Fields!W113 | CO-PILA-003 v1.1 | CO-PILA-003 v1.2 |
| DD | Country Fields!W36 | CO-PILA-003 v1.1 | CO-PILA-003 v1.2 |
| DD | Country Fields!W38 | CO-PILA-003 v1.1 | CO-PILA-003 v1.2 |
| DD | Country Fields!W61 | CO-PILA-003 v1.1 | CO-PILA-003 v1.2 |
| DD | Country Fields!W99 | CO-CESANTIAS-006 v1.1 | CO-CESANTIAS-006 v1.2 |

Citações de versão conferidas por final: CCG 2, DD 6, SIR 5; divergentes da vigente: 0.
Resultado: PASS (0 falhas).

## Resíduos corrigidos antes da subida ao Drive (2026-11-02)

Resíduos achados depois da emissão, corrigidos no final emitido por `final/scripts/release_residuos.py` (edições declaradas em `RESID` e `RESID_DOCX` de `release_r5_edits.py`; log `final/scripts/release_residuos_log.json`; edição limpa por cirurgia no XML, sem azul nem alteração controlada). Cópia de cada final antes da correção em `final/_historico/2026-11-02-antes-residuos/` (md5 = `MD5-FINAIS.txt` das 10:12).

1. **CCG, Módulo 12, Exemplo 4, linha (E):** "within the monthly cap" → teto anual de 790 UVT pelo acumulado (decisão A-1; CE S4 rad. 24047/2021). Varredura do CCG inteiro por "monthly cap/limit", "per month" e "÷ 12" ligados aos tetos de 790/1.340/3.800/2.500 UVT: nenhum outro. Os tetos mensais que ficam são mensais na norma: juros de moradia 100 UVT (DUR 1625 art. 1.2.4.1.27: "sin que exceda de cien Unidades de Valor (100) UVT mensuales"), medicina prepagada 16 UVT e dependentes 32 UVT (ET art. 387; DUR 1625 art. 1.2.4.1.6 nums. 4.2 e 4.3: "dieciséis (16) Unidades de Valor (UVT) mensuales", "treinta y dos (32) Unidades de Valor (UVT) mensuales"). A nota do CCG (Módulo 7) que chamava de "market practice" o rateio mensal dos juros de moradia foi corrigida no segundo lote (abaixo). Capa: 30 → 2 November 2026.
2. **Meios de pagamento:** DD `ID Information`!H7 e CO-DIAN-001 (NIE066 e Population Rules) citam só códigos do mapper Payment Method do DD (linhas 95–104). Em conta: 42, 45, 47, 98. Saíram 46, 30/31, 23/25/26 e ZZZ (fora do mapper); 48/49 só com cartão ligado a conta (Anexo Técnico NE v1.0, NIE064–NIE068 e tabelas 5.3.3.1/5.3.3.2). A linha v1.2 do Version Control da NE passou a citar a regra. H8/H9 não citam códigos (remetem ao H7): sem mudança.
3. **Teto de 2.500 UVT (ET art. 55):** a lei limita "el veinticinco por ciento (25%) del ingreso laboral o tributario anual, limitado a 2.500 UVT" (texto da Ley 2010 de 2019 art. 31), ou seja, um teto anual. Nenhum final divide 2.500 UVT por 12 (WTC: "2,500 UVT per year"); só o design mudou (`58151`).

A ferramenta prova: (a) só as partes do zip esperadas mudaram (docx: `word/document.xml`; xlsx: as abas editadas, e nelas nada fora das células); (b) só as células e parágrafos declarados mudaram, com o texto declarado, mantendo fórmula e estilo; (c) cada edição declarada foi usada uma vez. As provas das seções de cima (DRAFT-R5 → final, abre, zero erro de fórmula, `validate_workbook` PASS, marcadores, metadados, versões citadas) foram rodadas de novo sobre os finais corrigidos, com os resíduos declarados.

| Artefato | Onde | Antes | Depois |
|---|---|---|---|
| CCG | P28 | 30 October 2026 | 2 November 2026 |
| CCG | P7429 | 25% × 3,469,095 = 867,273.75; within the monthly cap | 25% × 3,469,095 = 867,273.75; within the 790-unit annual cap (COP 41,375,460), tracked year-to-date |
| DD | ID Information!H7 | Partial list. Bank name, account type and account number are populated only for account-crediting payment methods (Anexo Tecnico NE v1.0 table 5.3.3.2): 42 (Consignacion bancaria), 45 (Transferencia Credito Bancario), 46 (Transferencia Debito Interbancario), 47 (Transferencia Debito Bancaria) and 98 (CATS: Nequi, Daviplata), and 30 / 31 (Transferencia Credito / Debito) if used; left empty for 10 (Efectivo), 20, 23, 25 and 26 (cheques), 71 (Bonos), 72 (Vales) and ZZZ (Acuerdo mutuo). Cards (48, 49) count as account-based only where the client pays salary to a card linked to an account (an interpretation). The annex makes the three attributes optional (0-1, NIE066-NIE068); requiring all three for account-crediting methods is an engine rule. Must be absent or empty where Payment Method = 10 (cash). The bank / non-bank classification of each code is an interpretation; confirm with DIAN. | Partial list. Bank name, account type and account number are populated only for account-crediting payment methods of the Payment Method mapper (Anexo Tecnico NE v1.0 table 5.3.3.2): 42 (Consignacion bancaria), 45 (Transferencia Credito Bancario), 47 (Transferencia Debito Bancaria) and 98 (CATS: Nequi, Daviplata); left empty for 10 (Efectivo), 20 (Cheque), 71 (Bonos) and 72 (Vales). Cards (48, 49) count as account-based only where the client pays salary to a card linked to an account (an interpretation). The annex makes the three attributes optional (0-1, NIE066-NIE068); requiring all three for account-crediting methods is an engine rule. Must be absent or empty where Payment Method = 10 (cash). The bank / non-bank classification of each code is an interpretation; confirm with DIAN. |
| NE | Nomina Electronica Spec!G73 | Populated where 'Payment method' (NIE065) is a bank-mediated medium (42, 45, 46, 47, 48, 49 and similar). Must be absent or empty where NIE065 = 10 Efectivo. Bidirectional pair with NIE065 and with 'Account number' (NIE068). Also bidirectional with 'Account type' (NIE067), which is populated in the same cases. | Populated where 'Payment method' (NIE065) is a bank-mediated medium (42, 45, 47 and 98; 48 and 49 only where the card is linked to a salary account). Must be absent or empty where NIE065 = 10 Efectivo. Bidirectional pair with NIE065 and with 'Account number' (NIE068). Also bidirectional with 'Account type' (NIE067), which is populated in the same cases. |
| NE | Population Rules!C30 | Where the payment method is a bank-mediated medium (42, 45, 46, 47, 48, 49), the bank, account type and account number must all be present. Where it is 10 (Efectivo), all three must be absent. | Where the payment method is a bank-mediated medium (42, 45, 47 and 98; 48 and 49 only where the card is linked to a salary account), the bank, account type and account number must all be present. Where it is 10 (Efectivo), all three must be absent. |
| NE | Version Control!D15 | Statutory validation, second pass: the 790-UVT and 1,340-UVT caps tracked year-to-date, with no monthly one-twelfth limit (Population Rules, Example Analysis); severance savings and their interest not withheld for non-residents (Population Rules). Released 2026-11-02 — approved by Wallisson Gomes. | Statutory validation, second pass: the 790-UVT and 1,340-UVT caps tracked year-to-date, with no monthly one-twelfth limit (Population Rules, Example Analysis); severance savings and their interest not withheld for non-residents (Population Rules); bank attributes for the account-crediting payment methods 42, 45, 47 and 98 (Nomina Electronica Spec NIE066, Population Rules). Released 2026-11-02 — approved by Wallisson Gomes. |

Resultado: PASS (0 falhas; 6 edições conferidas).

## Resíduos de coerência, segundo lote (2026-11-02)

Ajustes de coerência achados depois do primeiro lote de resíduos, corrigidos no final por `final/scripts/release_residuos2.py` (edições declaradas em `RESID2` e `RESID2_DOCX` de `release_r5_edits.py`; log `final/scripts/release_residuos2_log.json`; mesmo método: cirurgia no XML, edição limpa, sem azul nem alteração controlada). Cópia de cada final antes deste lote em `final/_historico/2026-11-02-antes-residuos2/` (md5 = `MD5-FINAIS.txt` das 10:24). A prova do primeiro lote passou a comparar `antes-residuos` com essa cópia (cadeia antes-residuos → antes-residuos2 → final).

1. **CCG, Módulo 7, B1 (juros de moradia), linha Limit:** o teto mensal de 100 UVT deixa de ser chamado de "market practice" e passa a regra legal: DUR 1625 de 2016 art. 1.2.4.1.27 ("sin que exceda de cien (100) Unidades de Valor (UVT) mensuales", trecho conferido em `raw/docs/oficiais/CO/2026-10-13-DUR-1625-2016-DIAN.htm`); limite anual de 1.200 UVT do ET art. 119 mantido. Sai a remissão ao relatório de QA.
2. **CCG, linha Payment method:** a lista 42/45/47/10/20/48/49 passa a incluir 98 (CATS: Nequi, Daviplata), como o mapper Payment Method do DD (10, 20, 42, 45, 47, 48, 49, 71, 72, 98); o sentido da frase (meios de pagamento usuais) foi mantido.
3. **CO-DIAN-001, Field Options, bloco Medio de pago (linhas 79–87):** não há linha livre (linha 88 = lista completa; linha 89 = cabeçalho do bloco seguinte, mesclado A89:D89). Inserir linha deslocaria mesclagens, linhas seguintes e as referências por célula das provas; por isso o 98 entrou de forma explícita na célula D88 (código, sigla, nome e regra dos atributos bancários NIE066–NIE068, como nas linhas 79–87), e o cabeçalho A78 deixou de limitar o subconjunto aos códigos 1–97. M72 (valores realistas 42, 45, 10, 20) mantido.

A ferramenta prova, como no primeiro lote: só as partes do zip esperadas mudaram; só as células e parágrafos declarados mudaram, com o texto declarado, mantendo fórmula e estilo; cada edição declarada usada uma vez. As provas DRAFT-R5 → final, abre, zero erro de fórmula, `validate_workbook` PASS, marcadores, metadados e versões citadas foram rodadas de novo com este lote declarado.

| Artefato | Onde | Antes | Depois |
|---|---|---|---|
| CCG | P1046 | 42 bank deposit · 45 bank credit transfer · 47 bank debit transfer · 10 cash · 20 cheque · 48/49 credit/debit card | 42 bank deposit · 45 bank credit transfer · 47 bank debit transfer · 98 CATS simplified savings account (Nequi, Daviplata) · 10 cash · 20 cheque · 48/49 credit/debit card |
| CCG | P4097 | Monthly cap 100 tax units = COP 5,237,400 (the monthly figure is derived from the annual 1,200-unit limit of Tax Code art. 119; the monthly apportionment is market practice — see the QA report) | Monthly cap 100 tax units = COP 5,237,400 (statutory monthly limit: Decree 1625 of 2016 art. 1.2.4.1.27 — the monthly deductible amount may not exceed 100 tax units, "sin que exceda de cien (100) Unidades de Valor (UVT) mensuales"; annual limit 1,200 units, Tax Code art. 119) |
| NE | Field Options!A78 | ═══ MEDIO DE PAGO (ANEXO TABLE 5.3.3.2, NIE65) - REALISTIC PAYROLL SUBSET OF THE 1-97 LIST ═══ | ═══ MEDIO DE PAGO (ANEXO TABLE 5.3.3.2, NIE65) - REALISTIC PAYROLL SUBSET OF THE ANNEX LIST ═══ |
| NE | Field Options!D88 | The complete UN/EDIFACT 4461 medium-of-payment catalogue, codes 1 to 97, plus 98 (Cuentas de Ahorro de Tramite Simplificado - CATS: Nequi, Daviplata, etc.) and ZZZ (Acuerdo mutuo), is printed at Annex table 5.3.3.2. Metodo is xsd:string in XSD 1.0.6, so ZZZ is schema-valid. Only the subset above is realistic for Colombian payroll. | Also in the realistic payroll subset: 98 - CATS - Cuentas de Ahorro de Tramite Simplificado (Nequi, Daviplata, etc.) - simplified savings account credited directly; the Banco, TipoCuenta and NumeroCuenta attributes (NIE066-NIE068) are filled as for 42, 45 and 47. The complete UN/EDIFACT 4461 medium-of-payment catalogue, codes 1 to 97, plus 98 and ZZZ (Acuerdo mutuo), is printed at Annex table 5.3.3.2. Metodo is xsd:string in XSD 1.0.6, so ZZZ is schema-valid. Only the subset above, with code 98, is realistic for Colombian payroll. |

Resultado: PASS (0 falhas; 4 edições conferidas).

**Veredito: PASS** (0 falhas).

## Ocorrências legítimas (não são marcador)

- CCG: 1 × Version Control history of earlier issued versions (unchanged)
- CCG: 15 × country / language named in the legal content (treaty lists, language rule, nationality example)
- CCG: 3 × deduction labels (D1)-(D3) of the CCG worked example
- WTC: 1 × country / language named in the legal content (treaty lists, language rule, nationality example)
- DD: 8 × ISO country list
- NE: 2 × country / language named in the legal content (treaty lists, language rule, nationality example)

## Falhas

Nenhuma.

## Fora do escopo desta ferramenta

- Comentários do time herdados das versões vigentes no WTC e no DD: são do Google Sheets, idênticos aos dos finais de 30/10, e foram mantidos.
- Os estilos azuis acrescentados nos DRAFT-R5 continuam definidos em `styles.xml`, mas nenhuma célula, linha ou coluna os usa (como no release de 30/10).
- O texto jurídico: é conferido pelo Test 0 (revisor independente), não por esta ferramenta.

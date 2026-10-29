# CHANGELOG — LT-SODRA-003 SAM Spec v1.0 → v1.1

- **Arquivo:** `Research Pipeline/Lithuania/2026-10-29-correcoes/LT-SODRA-003-SAM-Spec_v1.1.xlsx` (local; **não** foi para o Drive). md5 no fim.
- **Base:** `2026-10-27-reports/specs-drive/LT-SODRA-003-SAM-Spec.xlsx` (v1.0 = export do .gsheet; md5 `b6a8074989c7be3948e1a6f43db39d64`, conferido sem alteração depois do build).
- **Achados corrigidos:** [[Research Pipeline/Lithuania/2026-10-28-validacao/VAL-SAM|VAL-SAM]] S1–S16. Hub: [[Lituania]].
- **Data:** 2026-10-29 (frente Pipeline).

## Como foi editado
- `inspect_workbook.py` na base: 9 abas, sem imagens nem comentários, mas o pacote tem 9 `xl/drawings/drawing*.xml` (vazios, herança do Google Sheets) e `xl/persons/person.xml`. Por isso a edição foi **XML+zip** (sem `openpyxl.save`): todas as 35 partes do pacote foram preservadas.
- Células alteradas: texto gravado como `inlineStr`; estilo clonado do original com fill `FFDDEBF7` (7 estilos novos em `styles.xml`). Células cujo valor não mudou não foram tocadas.
- **Destaque antigo:** a v1.0 não tinha destaque de versão. As cores `FFBDD7EE` (técnico), `FFFFEB9C` (payroll), `FFC6EFCE` (constante/YES), `FFD6DCE4` (seção) e `FFFFC7CE` são as cores de categoria do padrão Spain (toolkit) e foram mantidas; só a célula alterada troca a cor de categoria pelo azul-claro da v1.1.
- Nenhuma célula de texto começa com "=" (a v1.0 também não tinha títulos `=== X ===`; nada a trocar).
- Estrutura: 9 abas mantidas, na mesma ordem. Linhas acrescentadas: Version Control linha 3 (v1.1); Field Options linhas 43–60; Sample File linhas 77–176.
- Código pessoal de exemplo: **todos fictícios**, gerados com dígito de controle válido (mod 11 lituano: pesos 1-9,1; se resto 10, pesos 3-9,1-3; se de novo 10, dígito 0) e 1º dígito coerente com o gênero (3 = homem, 4 = mulher, nascidos em 1900–1999). Ex.: SAM3SD `38507159910` (Jonas Jonaitis), SAM3SDP `37603099979` (Petras Petraitis). Nenhum dado do FFData oficial nem do exemplo de cliente foi copiado (o FFData foi lido só por nomes de elementos/atributos).

## Fontes
- **[DSA]** *Elektroninio pranešimo apie apdraustuosius už ataskaitinį laikotarpį SAM formos duomenų struktūros aprašas (versija 07)*, aprovado pela V-243 na redação V-624 de 2018-12-07. Arquivo `SAM specifications - Lithuanian.pdf` (12 p., md5 `1db02c71a74cc0bed1b5c5f2cd01d53b`), Drive `Lithuania/12- Country Report Codes/SODRA - Social Security/`, cópia local em `Documents/youtrack_tickets/drive/2026-10-10-Lithuania/…`. Lido por pypdf nesta sessão. Trechos usados: §1 (UTF-8, 1 arquivo = 1 notificação), §2–2.10 p. 1–6 (FFData > Form > DocumentPages/Group/ListPages/ListPage + Pages/Page/Fields/Field; "Fields rinkinyje turi būti visi laukeliai"; "Skaičius – … su lietuvišku dešimtainių dalių skirtuku (,)"; "Žyma – „0“ (nepažymėta) arba „1“ (pažymėta)"), §3 p. 6–9 (exemplo completo), §4 p. 9 (páginas e quantidades), §5–§7 p. 9–12 (atributos; DocDate/DocNumber "Elektroninėje pranešimo formoje šis atributas nepildomas"; FormVersion "Tekstas 2"; P17 "Skaičius 2"; InsurerAddress "Draudėjo el. pašto adresas").
- **[FFD]** `SAM-V07 SAMPLE (1).ffdata` (md5 `59d62cc2f1414a5c3462d8c2b84e7940`), mesma pasta. Usado só como estrutura: atributos de FFData/Form/Page/Field, Groups, `Fields Count` 27/63, nomes dos campos, `TaxRate_1` = `21,27`, decimais com vírgula, marcas `1`/`0`. O login do autor e os dados da empresa **não** foram lidos para a saída nem copiados.
- **[TAR]** `raw/docs/oficiais/LT/2026-10-27-I-1336-art10-9_e_XV-632-art3_extrato.md` (I-1336 art. 10(9); XV-632 art. 3(1)–(4)); `2026-10-27-I-1336-art10-7-8_MMA_extrato.md` (art. 10(7)–(8)); `Nutarimas-700-2025-10-16-MMA-2026_extrato.txt` (MMA 2026 = €1 153); `XV-632-…-2026-rodikliai_extrato.txt` (art. 4: VDU 2026 = €2 312,15); `2026-10-27-Sodra-SAM/2026-10-27-sodra-tarifas-2026-PSD-fundos_extrato.md` (página de tarifas da Sodra 2026: GF 0,16; ILDIF 0,16; +3 % acumulação; I-1343 art. 17(2) PSD 6,98).
- **[EDAS]** `raw/docs/oficiais/LT/2026-10-27-Sodra-SAM/2026-10-27-sodra-EDAS-DataService_extrato.md` (assinatura qualificada; DataService SOAP 1.2/MTOM, endpoint, operações; "UTF-8 without BOM", p. 8).
- **[EXT]** `raw/docs/oficiais/LT/2026-10-27-Sodra-SAM/2026-10-27-sodra-SAM-v07-instrucao-e-MXFD_extrato.md` (p. 55.5: tarifa total; MXFD: CycleMonth 1–12; uma tarifa por segurado).

## Taxa P3 de 2026 (composição usada nos exemplos e na Field Options)
| Parcela | % | Fonte |
|---|---|---|
| Empregado: pensão 8,72 + doença 1,99 + maternidade 1,81 | 12,52 | XV-632 art. 3(4) |
| PSD (saúde) | 6,98 | I-1343 art. 17(2) |
| Desemprego (empregador) | 1,31 indeterminado / 2,03 determinado | XV-632 art. 3(1) |
| Acidentes de trabalho, grupo I / II / III / IV | 0,14 / 0,49 / 0,70 / 1,40 | XV-632 art. 3(3) |
| Garantinis fondas + Ilgalaikio darbo išmokų fondas | 0,16 + 0,16 | página de tarifas da Sodra 2026 (lei não lida) |
| Acumulação de pensão (opcional) | +3,00 | página de tarifas da Sodra 2026; inclusão no P3 **não verificada** |

Mínimo 12,52 + 6,98 + 1,31 + 0,14 + 0,32 = **21,27** (= `TaxRate_1` do FFData oficial); máximo com +3 % = **26,25**. Teto 2026: 60 × 2 312,15 = **€138 729,00**. MMA 2026: **€1 153**.

## Alterações célula a célula
| Aba!Célula | Antes (v1.0) | Depois (v1.1) | Fonte | Achado |
|---|---|---|---|---|
| Version Control!A3 | (vazio) | LT-SODRA-003 | linha nova v1.1 | S9 |
| Version Control!B3 | (vazio) | 1.1 | linha nova v1.1 | S9 |
| Version Control!C3 | (vazio) | 29-Oct-26 | linha nova v1.1 | S9 |
| Version Control!D3 | (vazio) | Mercans Global Compliance (W. Gomes) | linha nova v1.1 | S9 |
| Version Control!E3 | (vazio) | Corrections from the 28-Oct-26 independent validation (VAL-SAM S1-S16). Source added: SAM v07 data structure d… | linha nova v1.1 | S9 |
| Report Matrix!G2 | Electronic document submitted through EDAS, the electronic employer service system (points 8 and 249). The sub… | Electronic document submitted through the employer's Sodra account (EDAS) (points 8 and 249), either uploaded … | Sodra, página 'Elektroninių pranešimų teikimas internetu' + instrução DataService p. 4–15 (extrato EDAS-DataService) | S14 |
| Report Matrix!H2 | FFData XML (form definition distributed as .mxfd; form SAM version 07) | FFData XML, UTF-8 without BOM (DataService instruction p. 8), one notification per file; structure per the SAM… | DSA (SAM v07, V-624) §1–2.2 p. 1–2; DataService p. 8 ('UTF-8 without BOM') | S14, S1 |
| Report Matrix!J2 | Structural accuracy 93 %. CONFIRMED AGAINST KNOWN STATE: FormVersion 07 is confirmed - the literal '07' appear… | v1.1 RE-ASSESSMENT. The v1.0 figure of 93 % is withdrawn as overstated: v1.0 compared field names only and rec… | DSA (SAM v07, V-624) p. 1–12; FFData oficial; VAL-SAM | S9, S7 |
| SAM Spec!M7 | NAME/CONTENT MISMATCH, flagged deliberately. The MXFD calls this element InsurerAddress with the comment 'Drau… | XML element InsurerAddress. Content = the employer's E-MAIL address: the SAM v07 data structure description (D… | DSA (SAM v07, V-624) §5 p. 9 (InsurerAddress = 'Draudėjo el. pašto adresas') | S15 |
| SAM Spec!T7 | Confirm box 7 carries the e-mail address and not a postal address, given the MXFD element is named InsurerAddr… | (vazio) | DSA (SAM v07, V-624) §5 p. 9 (InsurerAddress = 'Draudėjo el. pašto adresas') | S15 |
| SAM Spec!F8 | Y | N | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!G8 | (vazio) | DSA section 5, box 9: 'Elektroninėje pranešimo formoje šis atributas nepildomas' (not filled in the electronic… | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!K8 | 2026-08-10 | (vazio) | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!F9 | Y | N | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!G9 | (vazio) | DSA section 5, box 10: 'Elektroninėje pranešimo formoje šis atributas nepildomas' (not filled in the electroni… | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!K9 | SAM-2026-07-001 | (vazio) | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!L8 | Generated by the submission builder | Not populated - empty <Field Name="DocDate"/> | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!L9 | Generated by the submission builder | Not populated - empty <Field Name="DocNumber"/> | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!M8 | XML element DocDate, DataType Date, 10 cells. The employer's own registration date for the notification docume… | XML element DocDate, DataType Date, 10 characters. The SAM v07 data structure description (DSA, V-243 in the V… | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!M9 | XML element DocNumber, DataType Text, 16 cells. The employer's own reference number for the notification, repe… | XML element DocNumber, Text, 16 characters. Per the SAM v07 data structure description (DSA, V-243 in the V-62… | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!J12 | MM (01-12), no separator | Number, 1-12, no leading zero (DSA section 5: Skaičius 2; MXFD Decimal, MinValue 1, MaxValue 12) | DSA (SAM v07, V-624) §5 p. 10 (P17/P17T 'Skaičius 2'); MXFD MinValue 1/MaxValue 12 | S4 |
| SAM Spec!K12 | 07 | 7 | DSA (SAM v07, V-624) §5 p. 10 (P17/P17T 'Skaičius 2'); MXFD MinValue 1/MaxValue 12 | S4 |
| SAM Spec!M12 | XML element CycleMonth. LEGACY COMMENT: the MXFD comments this field 'Ataskaitinis ketvirtis' - reporting QUAR… | XML element CycleMonth. LEGACY COMMENT: the MXFD comments this field 'Ataskaitinis ketvirtis' (reporting QUART… | DSA (SAM v07, V-624) §5 p. 10 (P17/P17T 'Skaičius 2'); MXFD MinValue 1/MaxValue 12 | S4 |
| SAM Spec!O12 | 01;02;03;04;05;06;07;08;09;10;11;12 | 1;2;3;4;5;6;7;8;9;10;11;12 | DSA (SAM v07, V-624) §5 p. 10 (P17/P17T 'Skaičius 2'); MXFD MinValue 1/MaxValue 12 | S4 |
| SAM Spec!T12 | Confirm CycleMonth is validated as 01-12 and not 1-4, given the MXFD comment and the 2-cell width both date fr… | (vazio) | DSA (SAM v07, V-624) §5 p. 10 (P17/P17T 'Skaičius 2'); MXFD MinValue 1/MaxValue 12 | S4 |
| SAM Spec!J13 | Checkmark (x) | Checkmark: 1 = marked, 0 = unmarked (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 ('Žyma – „0“ arba „1“') | S3 |
| SAM Spec!K13 | (vazio) | 0 | DSA (SAM v07, V-624) §2.10 p. 6 ('Žyma – „0“ arba „1“') | S3 |
| SAM Spec!O13 | x | 0;1 | DSA (SAM v07, V-624) §2.10 p. 6 ('Žyma – „0“ arba „1“') | S3 |
| SAM Spec!J15 | MM (01-12), no separator | Number, 1-12, no leading zero (DSA section 5: Skaičius 2; MXFD Decimal, MinValue 1, MaxValue 12) | DSA (SAM v07, V-624) §5 p. 10 (P17/P17T 'Skaičius 2'); MXFD MinValue 1/MaxValue 12 | S4 |
| SAM Spec!M15 | XML element RevisedCycleMonth, commented 'Tikslinamo laikotarpio' in the MXFD with the word for month omitted.… | XML element RevisedCycleMonth, commented 'Tikslinamo laikotarpio' in the MXFD with the word for month omitted.… | DSA (SAM v07, V-624) §5 p. 10 (P17/P17T 'Skaičius 2'); MXFD MinValue 1/MaxValue 12 | S4 |
| SAM Spec!O15 | 01;02;03;04;05;06;07;08;09;10;11;12 | 1;2;3;4;5;6;7;8;9;10;11;12 | DSA (SAM v07, V-624) §5 p. 10 (P17/P17T 'Skaičius 2'); MXFD MinValue 1/MaxValue 12 | S4 |
| SAM Spec!G17 | Marked with 'x' where the SAM3SD annex is submitted (point 54.1.1). Left unmarked where no SAM3SD annex accomp… | Set to 1 where the SAM3SD annex is submitted (point 54.1.1; the paper form is marked 'x', the electronic form … | DSA (SAM v07, V-624) §2.10 p. 6 ('Žyma – „0“ arba „1“') | S3 |
| SAM Spec!J17 | Checkmark (x) | Checkmark: 1 = marked, 0 = unmarked (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 ('Žyma – „0“ arba „1“') | S3 |
| SAM Spec!K17 | x | 1 | DSA (SAM v07, V-624) §2.10 p. 6 ('Žyma – „0“ arba „1“') | S3 |
| SAM Spec!M17 | XML element Appendixes2, DataType Checkmark, in column S1 of the printed grid. Point 54.1.1: 'x' is entered wh… | XML element Appendixes2, DataType Checkmark, in column S1 of the printed grid. Point 54.1.1: the box is marked… | DSA (SAM v07, V-624) §2.10 p. 6 ('Žyma – „0“ arba „1“') | S3 |
| SAM Spec!O17 | x | 0;1 | DSA (SAM v07, V-624) §2.10 p. 6 ('Žyma – „0“ arba „1“') | S3 |
| SAM Spec!K18 | 3 | 22 | conta refeita: ceil(128/6)=22; 128×3000,00; 128×638,10; P23=22+1 | S10 |
| SAM Spec!K20 | 384000.00 | 384000,00 | conta refeita: ceil(128/6)=22; 128×3000,00; 128×638,10; P23=22+1 | S10 |
| SAM Spec!K21 | 152064.00 | 81676,80 | conta refeita: ceil(128/6)=22; 128×3000,00; 128×638,10; P23=22+1 | S10 |
| SAM Spec!J20 | Decimal, 12 cells, 2 dp | Number, 12 characters, 2 dp, Lithuanian decimal comma (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 (vírgula decimal) | S2 |
| SAM Spec!J21 | Decimal, 12 cells, 2 dp | Number, 12 characters, 2 dp, Lithuanian decimal comma (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 (vírgula decimal) | S2 |
| SAM Spec!G22 | Marked with 'x' where the SAM3SDP annex is submitted (point 54.1.2). Left unmarked where no SAM3SDP annex acco… | Set to 1 where the SAM3SDP annex is submitted (point 54.1.2; 'x' on paper, 1 in the FFData file, DSA 2.10). Se… | DSA (SAM v07, V-624) §2.10 p. 6 ('Žyma – „0“ arba „1“') | S3 |
| SAM Spec!J22 | Checkmark (x) | Checkmark: 1 = marked, 0 = unmarked (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 ('Žyma – „0“ arba „1“') | S3 |
| SAM Spec!K22 | (vazio) | 1 | DSA (SAM v07, V-624) §2.10 p. 6 ('Žyma – „0“ arba „1“') | S3 |
| SAM Spec!M22 | XML element Appendixes3, DataType Checkmark, in column S1. Point 54.1.2: 'x' is entered where the SAM3SDP anne… | XML element Appendixes3, DataType Checkmark, in column S1. Point 54.1.2: marked where the SAM3SDP annex is sub… | DSA (SAM v07, V-624) §2.10 p. 6 ('Žyma – „0“ arba „1“') | S3 |
| SAM Spec!O22 | x | 0;1 | DSA (SAM v07, V-624) §2.10 p. 6 ('Žyma – „0“ arba „1“') | S3 |
| SAM Spec!K23 | (vazio) | 1 | conta refeita: ceil(128/6)=22; 128×3000,00; 128×638,10; P23=22+1 | S10 |
| SAM Spec!K24 | (vazio) | 1 | conta refeita: ceil(128/6)=22; 128×3000,00; 128×638,10; P23=22+1 | S10 |
| SAM Spec!K25 | (vazio) | 1500,00 | conta refeita: ceil(128/6)=22; 128×3000,00; 128×638,10; P23=22+1 | S10 |
| SAM Spec!K26 | (vazio) | 319,05 | conta refeita: ceil(128/6)=22; 128×3000,00; 128×638,10; P23=22+1 | S10 |
| SAM Spec!J25 | Decimal, 12 cells, 2 dp | Number, 12 characters, 2 dp, Lithuanian decimal comma (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 (vírgula decimal) | S2 |
| SAM Spec!J26 | Decimal, 12 cells, 2 dp | Number, 12 characters, 2 dp, Lithuanian decimal comma (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 (vírgula decimal) | S2 |
| SAM Spec!K27 | 3 | 23 | conta refeita: ceil(128/6)=22; 128×3000,00; 128×638,10; P23=22+1 | S10 |
| SAM Spec!I32 | 10 | 2 | DSA (SAM v07, V-624) §5–§7 p. 9–11 (FormVersion 'Tekstas 2') | S12 |
| SAM Spec!I51 | 10 | 2 | DSA (SAM v07, V-624) §5–§7 p. 9–11 (FormVersion 'Tekstas 2') | S12 |
| SAM Spec!I74 | 10 | 2 | DSA (SAM v07, V-624) §5–§7 p. 9–11 (FormVersion 'Tekstas 2') | S12 |
| SAM Spec!M32 | XML element FormVersion with MXFD comment '07', matching the '07 versija' printed at the top right of every pa… | XML element FormVersion with MXFD comment '07', matching the '07 versija' printed at the top right of every pa… | DSA (SAM v07, V-624) §5–§7 p. 9–11 (FormVersion 'Tekstas 2') | S12 |
| SAM Spec!M51 | XML element FormVersion with MXFD comment '07', matching the '07 versija' printed on SAM-form.pdf page 2. All … | XML element FormVersion with MXFD comment '07', matching the '07 versija' printed on SAM-form.pdf page 2. All … | DSA (SAM v07, V-624) §5–§7 p. 9–11 (FormVersion 'Tekstas 2') | S12 |
| SAM Spec!M74 | XML element FormVersion with MXFD comment '07', matching the '07 versija' printed on SAM-form.pdf page 3. All … | XML element FormVersion with MXFD comment '07', matching the '07 versija' printed on SAM-form.pdf page 3. All … | DSA (SAM v07, V-624) §5–§7 p. 9–11 (FormVersion 'Tekstas 2') | S12 |
| SAM Spec!K35 | 3 | 22 | conta refeita: ceil(128/6)=22; 128×3000,00; 128×638,10; P23=22+1 | S10 |
| SAM Spec!F37 | Y | N | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!G37 | (vazio) | DSA section 6, box 9: not filled in the electronic notification form ('nepildomas'). Emit the <Field> element … | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!K37 | 2026-08-10 | (vazio) | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!L37 | Copy of SAM title page box 9 | Not populated - empty field; if a tool fills it, copy of SAM title page box 9 | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!F38 | Y | N | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!G38 | (vazio) | DSA section 6, box 10: not filled in the electronic notification form ('nepildomas'). Emit the <Field> element… | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!K38 | SAM-2026-07-001 | (vazio) | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!L38 | Copy of SAM title page box 10 | Not populated - empty field; if a tool fills it, copy of SAM title page box 10 | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!F56 | C | N | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!G56 | Present only where the SAM3SDP annex is submitted. A strict copy of title page box 9. | DSA section 7, box 9: not filled in the electronic notification form ('nepildomas'). Emit the <Field> element … | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!K56 | 2026-08-10 | (vazio) | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!L56 | Copy of SAM title page box 9 | Not populated - empty field; if a tool fills it, copy of SAM title page box 9 | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!F57 | C | N | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!G57 | Present only where the SAM3SDP annex is submitted. A strict copy of title page box 10. | DSA section 7, box 10: not filled in the electronic notification form ('nepildomas'). Emit the <Field> element… | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!K57 | SAM-2026-07-001 | (vazio) | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!L57 | Copy of SAM title page box 10 | Not populated - empty field; if a tool fills it, copy of SAM title page box 10 | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!M37 | XML element DocDate, carried with no MXFD comment on the annex pages because it repeats the title page value. … | XML element DocDate on the SAM3SD page. Not filled in the electronic form (DSA section 6); emitted empty. If a… | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!M38 | XML element DocNumber, uncommented on the annex pages because it repeats the title page value. Validation erro… | XML element DocNumber on the SAM3SD page. Not filled in the electronic form (DSA section 6); emitted empty. If… | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!M56 | XML element DocDate, uncommented on the annex pages because it repeats the title page value. Validation error … | XML element DocDate on the SAM3SDP page. Not filled in the electronic form (DSA section 7); emitted empty. If … | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!M57 | XML element DocNumber, uncommented on the annex pages. Validation error C2336 rejects differing registration n… | XML element DocNumber on the SAM3SDP page. Not filled in the electronic form (DSA section 7); emitted empty. I… | DSA (SAM v07, V-624) §5 p. 9, §6 p. 10, §7 p. 11 ('atributas nepildomas'); §2.9 p. 5 | S5 |
| SAM Spec!K40 | 39001010101 | 38507159910 | algoritmo mod 11 do código pessoal LT (fictícios gerados) | S11 |
| SAM Spec!J45 | Decimal, 11 cells, 2 dp | Number, 11 characters, 2 dp, Lithuanian decimal comma (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 (vírgula decimal) | S2 |
| SAM Spec!K45 | 3000.00 | 3000,00 | DSA (SAM v07, V-624) §2.10 p. 6; FFData oficial ('728,00') | S2 |
| SAM Spec!J46 | Decimal, 5 cells, 2 dp (percentage) | Number, 5 characters, 2 dp, decimal comma (percentage, e.g. 21,27) | DSA (SAM v07, V-624) §2.10 p. 6 (vírgula decimal) | S2 |
| SAM Spec!K46 | 39.58 | 21,27 | XV-632 art. 3(1),(3),(4); I-1343 art. 17(2); Sodra tarifas 2026; FFData oficial TaxRate_1=21,27 | S6, S2 |
| SAM Spec!M46 | XML elements TaxRate_1 to TaxRate_6, DataType Decimal, DecimalPlaces 2, 5 cells. Point 55.5: the general contr… | XML elements TaxRate_1 to TaxRate_6, Number, 2 dp, 5 characters. Point 55.5: the general (total) contribution … | XV-632 art. 3; I-1343 art. 17(2); Sodra tarifas 2026; instrução p. 55.5 (extrato) | S7 |
| SAM Spec!O46 | See Field Options - rate depends on the insured category; not enumerated in the order | See Field Options - 'General contribution rate (P3) - 2026' | XV-632 art. 3; I-1343 art. 17(2); Sodra tarifas 2026; instrução p. 55.5 (extrato) | S7 |
| SAM Spec!T46 | Confirm the current combined VSD and PSD rates per insured category for the reporting year, and whether P3 is … | Residual only: confirm whether the 3 % pension-accumulation contribution (employees in the additional accumula… | XV-632 art. 3; I-1343 art. 17(2); Sodra tarifas 2026; instrução p. 55.5 (extrato) | S7 |
| SAM Spec!J47 | Decimal, 11 cells, 2 dp | Number, 11 characters, 2 dp, Lithuanian decimal comma (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 (vírgula decimal) | S2 |
| SAM Spec!K47 | 1187.40 | 638,10 | XV-632 art. 3(1),(3),(4); I-1343 art. 17(2); Sodra tarifas 2026; FFData oficial TaxRate_1=21,27 | S6, S2 |
| SAM Spec!M47 | XML elements PaymentSum_1 to PaymentSum_6, DataType Decimal, DecimalPlaces 2, 11 cells. Point 55.2: the contri… | XML elements PaymentSum_1 to PaymentSum_6, Number, 2 dp, 11 characters. Point 55.2: the contribution amount ca… | I-1336 art. 10(7)–(9); XV-632 art. 4; Nutarimas 700/2025 | S8 |
| SAM Spec!J48 | Decimal, 11 cells, 2 dp | Number, 11 characters, 2 dp, Lithuanian decimal comma (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 (vírgula decimal) | S2 |
| SAM Spec!K48 | 18000.00 | 18000,00 | DSA (SAM v07, V-624) §2.10 p. 6; FFData oficial ('728,00') | S2 |
| SAM Spec!J49 | Decimal, 11 cells, 2 dp | Number, 11 characters, 2 dp, Lithuanian decimal comma (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 (vírgula decimal) | S2 |
| SAM Spec!K49 | 7124.40 | 3828,60 | XV-632 art. 3(1),(3),(4); I-1343 art. 17(2); Sodra tarifas 2026; FFData oficial TaxRate_1=21,27 | S6, S2 |
| SAM Spec!K59 | 47712120987 | 37603099979 | algoritmo mod 11 do código pessoal LT (fictícios gerados) | S11 |
| SAM Spec!K65 | MB vadovo pagal civiline sutarti gautos pajamos | MB vadovo pagal civilinę sutartį gautos pajamos | ortografia lituana; spec M44/M63 | S16 |
| SAM Spec!J68 | Decimal, 11 cells, 2 dp | Number, 11 characters, 2 dp, Lithuanian decimal comma (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 (vírgula decimal) | S2 |
| SAM Spec!K68 | 1500.00 | 1500,00 | DSA (SAM v07, V-624) §2.10 p. 6; FFData oficial ('728,00') | S2 |
| SAM Spec!J69 | Decimal, 5 cells, 2 dp (percentage) | Number, 2 dp, decimal comma (percentage, e.g. 21,27) | DSA (SAM v07, V-624) §2.10 p. 6 (vírgula decimal) | S2 |
| SAM Spec!K69 | 21.27 | 21,27 | XV-632 art. 3(1),(3),(4); I-1343 art. 17(2); Sodra tarifas 2026; FFData oficial TaxRate_1=21,27 | S6, S2 |
| SAM Spec!O69 | See Field Options - rate depends on the insured category; not enumerated in the order | See Field Options - 'General contribution rate (P3) - 2026' | XV-632 art. 3; I-1343 art. 17(2); Sodra tarifas 2026; instrução p. 55.5 (extrato) | S7 |
| SAM Spec!T69 | Confirm the combined rates for reason codes 09 (pension plus PSD) and 10 (no PSD obligation), since the distin… | Confirm the P3 composition for reason codes 06 (small-partnership manager under a civil contract), 09 (office … | XV-632 art. 3; I-1343 art. 17(2); Sodra tarifas 2026; instrução p. 55.5 (extrato) | S7 |
| SAM Spec!J70 | Decimal, 11 cells, 2 dp | Number, 11 characters, 2 dp, Lithuanian decimal comma (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 (vírgula decimal) | S2 |
| SAM Spec!K70 | 319.05 | 319,05 | XV-632 art. 3(1),(3),(4); I-1343 art. 17(2); Sodra tarifas 2026; FFData oficial TaxRate_1=21,27 | S6, S2 |
| SAM Spec!J71 | Decimal, 11 cells, 2 dp | Number, 11 characters, 2 dp, Lithuanian decimal comma (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 (vírgula decimal) | S2 |
| SAM Spec!K71 | 1500.00 | 1500,00 | DSA (SAM v07, V-624) §2.10 p. 6; FFData oficial ('728,00') | S2 |
| SAM Spec!J72 | Decimal, 11 cells, 2 dp | Number, 11 characters, 2 dp, Lithuanian decimal comma (DSA 2.10) | DSA (SAM v07, V-624) §2.10 p. 6 (vírgula decimal) | S2 |
| SAM Spec!K72 | 319.05 | 319,05 | XV-632 art. 3(1),(3),(4); I-1343 art. 17(2); Sodra tarifas 2026; FFData oficial TaxRate_1=21,27 | S6, S2 |
| File Structure!C2 | Point 8: SD notifications are submitted by sending an electronic document through EDAS. Point 250: the notific… | One FFData file holds one notification (DSA 1), UTF-8 (DataService: without BOM). Structure per the SAM v07 da… | DSA (SAM v07, V-624) §2.1–2.10 p. 1–6, §3 p. 6–9, §4 p. 9; FFData oficial | S1, S9, S14 |
| File Structure!C4 | Exactly one occurrence. 27 fields. FormCode literal 'SAM', FormVersion literal '07'. Carries the employer data… | Exactly one occurrence, <Page PageDefName="SAM" PageNumber="1"> with <Fields Count="27">. FormCode 'SAM', Form… | DSA (SAM v07, V-624) §2.1–2.10 p. 1–6, §3 p. 6–9, §4 p. 9; FFData oficial | S1, S9, S14 |
| File Structure!C5 | Zero to 9,999 pages. FormCode literal 'SAM3SD'. 18 distinct fields: 9 repeated across SIX detail rows (RowNumb… | Zero to unlimited pages (DSA section 4), each <Page PageDefName="SAM3SD"> with <Fields Count="63">: 9 fields x… | DSA (SAM v07, V-624) §2.1–2.10 p. 1–6, §3 p. 6–9, §4 p. 9; FFData oficial | S1, S9, S14 |
| File Structure!C7 | Zero to 9,999 pages. FormCode literal 'SAM3SDP'. 22 distinct fields: 13 repeated across THREE detail rows (the… | Zero to unlimited pages (DSA section 4), each <Page PageDefName="SAM3SDP"> with <Fields Count="48">: 13 fields… | DSA (SAM v07, V-624) §2.1–2.10 p. 1–6, §3 p. 6–9, §4 p. 9; FFData oficial | S1, S9, S14 |
| Field Options!B12 | 01 | 1 | DSA (SAM v07, V-624) §5 p. 10; MXFD MinValue 1 | S4 |
| Field Options!B13 | 02 | 2 | DSA (SAM v07, V-624) §5 p. 10; MXFD MinValue 1 | S4 |
| Field Options!B14 | 03 | 3 | DSA (SAM v07, V-624) §5 p. 10; MXFD MinValue 1 | S4 |
| Field Options!B15 | 04 | 4 | DSA (SAM v07, V-624) §5 p. 10; MXFD MinValue 1 | S4 |
| Field Options!B16 | 05 | 5 | DSA (SAM v07, V-624) §5 p. 10; MXFD MinValue 1 | S4 |
| Field Options!B17 | 06 | 6 | DSA (SAM v07, V-624) §5 p. 10; MXFD MinValue 1 | S4 |
| Field Options!B18 | 07 | 7 | DSA (SAM v07, V-624) §5 p. 10; MXFD MinValue 1 | S4 |
| Field Options!B19 | 08 | 8 | DSA (SAM v07, V-624) §5 p. 10; MXFD MinValue 1 | S4 |
| Field Options!B20 | 09 | 9 | DSA (SAM v07, V-624) §5 p. 10; MXFD MinValue 1 | S4 |
| Field Options!B28 | x | 1 | DSA (SAM v07, V-624) §2.10 p. 6 | S3 |
| Field Options!E28 | Points 54.1.1 and 54.1.2: 'x' is entered where the corresponding annex is submitted. Derived from the annex pa… | Points 54.1.1 and 54.1.2: the box is marked where the corresponding annex is submitted - 'x' on the paper form… | DSA (SAM v07, V-624) §2.10 p. 6 | S3 |
| Field Options!B29 | x | 1 | DSA (SAM v07, V-624) §2.10 p. 6 | S3 |
| Field Options!E29 | Marks the notification as revising a previously submitted period, in which case P14T and P17T identify that pe… | Value 1 in the FFData file ('x' on paper; DSA 2.10) marks the notification as revising a previously submitted … | DSA (SAM v07, V-624) §2.10 p. 6 | S3 |
| Field Options!B30 | (variable) | (see 2026 table below) | XV-632 art. 3(1),(3),(4); I-1343 art. 17(2); Sodra tarifas 2026 (GF/ILDIF, +3 %) | S7 |
| Field Options!E30 | NOT ENUMERATED IN THE ORDER. Point 55.5 fixes the SAM3SD rate as the one applicable at the START OF THE CALEND… | P3 is ONE total rate per insured person (instruction point 55.5; the MXFD and DSA have no employee/employer sp… | XV-632 art. 3(1),(3),(4); I-1343 art. 17(2); Sodra tarifas 2026 (GF/ILDIF, +3 %) | S7 |
| Population Rules!C2 | Populate the employer block first: point 53.1 requires the points 13.2-13.9 employer data to be completed befo… | Populate the employer block first: point 53.1 requires the points 13.2-13.9 employer data to be completed befo… | DSA (SAM v07, V-624) §5–§7 | S5, S15 |
| Population Rules!C3 | Set P14 to the calendar year and P17 to the calendar MONTH, 01-12, of the reporting period. Ignore the quarter… | Set P14 to the calendar year and P17 to the calendar MONTH as a number 1-12 without leading zero (July = 7): D… | DSA (SAM v07, V-624) §5 p. 10 | S4 |
| Population Rules!C5 | Derive the whole grid from the annexes after they are built, never from configuration. Point 54.1: mark P20.1 … | Derive the whole grid from the annexes after they are built, never from configuration. Point 54.1: P20.1 and P… | DSA (SAM v07, V-624) §2.10 | S3, S2 |
| Population Rules!C7 | Populate A11 with the income computed for the CALENDAR MONTH on which contributions are calculated (point 55.1… | Populate A11 with the income computed for the CALENDAR MONTH on which contributions are calculated (point 55.1… | I-1336 art. 10(7)–(9); XV-632 art. 4; Nutarimas 700/2025 | S8 |
| Population Rules!D7 | Negative retro adjustment exceeding the month's insurable income, which the rules do not contemplate and the M… | Month in which cumulative income crosses EUR 138 729,00 (2026), where only PSD 6,98 continues above the ceilin… | idem | S8 |
| Population Rules!C13 | Points 8 and 249: SD notifications are submitted as an electronic document through EDAS. Point 250: the notifi… | Points 8 and 249: SD notifications are submitted as an electronic document through the employer's Sodra accoun… | DataService p. 4–15; página Sodra EDAS; DSA (SAM v07, V-624) | S9, S13, S14 |
| Population Rules!D13 | FFData structure description not obtainable, blocking the interface; electronic signature certificate expiring… | Electronic signature certificate expiring before the deadline; deadline falling on a weekend or public holiday… | idem | S13, S14 |
| Example Analysis!A7 | 07 | 7 | DSA (SAM v07, V-624) §5 p. 10 | S4 |
| Example Analysis!C7 | Reporting month July, expressed as 01-12. | Reporting month July, written as the number 7 (no leading zero). | DSA (SAM v07, V-624) §5 p. 10 | S4 |
| Example Analysis!D7 | The MXFD comments this field 'Ataskaitinis ketvirtis' (reporting QUARTER) and gives it 2 cells, but point 53.2… | DSA section 5 types P17 as Number; the MXFD sets MinValue 1 / MaxValue 12. The MXFD comment 'Ataskaitinis ketv… | DSA (SAM v07, V-624) §5 p. 10 | S4 |
| Example Analysis!A8 | x | 1 | DSA (SAM v07, V-624) §2.10 | S3 |
| Example Analysis!D8 | Point 54.1.1. Derived from the annex page count, not configured; error C2330 fires where the annex is present … | Point 54.1.1 ('x' on paper, 1 in the FFData file; DSA 2.10). Derived from the annex page count, not configured… | DSA (SAM v07, V-624) §2.10 | S3 |
| Example Analysis!A9 | 3 | 23 | conta refeita | S10 |
| Example Analysis!C9 | Three annex pages in the document in total: three SAM3SD pages (P20.2) and none SAM3SDP (P21.2). | 23 annex pages in the document in total: 22 SAM3SD pages (P20.2) and 1 SAM3SDP page (P21.2). | conta refeita | S10 |
| Example Analysis!D10 | Point 54.4. With six detail rows per page, 128 persons occupy 22 pages - so this example's page count of 3 bel… | Point 54.4. With six detail rows per page, 128 persons occupy 22 SAM3SD pages (21 full pages + 2 lines on page… | conta refeita | S10 |
| Example Analysis!A11 | 3000.00 | 3000,00 | DSA (SAM v07, V-624) §2.10 | S2 |
| Example Analysis!A12 | 39.58 | 21,27 | XV-632 art. 3; I-1343 art. 17(2); Sodra tarifas | S6 |
| Example Analysis!C12 | A combined contribution rate of 39.58 % applicable to this insured person at the start of the calendar month. | A total contribution rate of 21,27 % applicable to this insured person at the start of the calendar month. | XV-632 art. 3; I-1343 art. 17(2); Sodra tarifas | S6 |
| Example Analysis!D12 | ILLUSTRATIVE RATE ONLY. Point 55.5 fixes the rate as at the month start. The order publishes no rates; they mu… | 2026 rate for an indefinite-term employment contract, accident group I, no pension accumulation: 12,52 + 6,98 … | XV-632 art. 3; I-1343 art. 17(2); Sodra tarifas | S6 |
| Example Analysis!A13 | 1187.40 | 638,10 | XV-632 art. 3; I-1343 art. 17(2); Sodra tarifas | S6 |
| Example Analysis!C13 | EUR 1,187.40 of contributions - exactly 3,000.00 x 39.58 %. | EUR 638,10 of contributions - exactly 3 000,00 x 21,27 %. | XV-632 art. 3; I-1343 art. 17(2); Sodra tarifas | S6 |
| Example Analysis!A14 | 18000.00 | 18000,00 | DSA (SAM v07, V-624) §2.10 | S2 |
| Example Analysis!C14 | EUR 18,000.00 of insurable income on this page - six lines at EUR 3,000.00 each. | EUR 18 000,00 of insurable income on a full page - six lines at EUR 3 000,00 each (P8 on that page = 6 x 638,1… | DSA (SAM v07, V-624) §2.10 | S2 |
| Example Analysis!A17 | 21.27 | 21,27 | idem; vírgula decimal | S2, S7 |
| Example Analysis!C17 | A combined rate of 21.27 % applicable during the A21-A22 period. | A total rate of 21,27 % applicable during the A21-A22 period. | idem; vírgula decimal | S2, S7 |
| Example Analysis!D17 | ILLUSTRATIVE RATE ONLY. Point 56.10 ties the rate to the PERIOD, unlike point 55.5 which ties the SAM3SD rate … | ILLUSTRATIVE for reason code 06: 21,27 is the ordinary-employee rate; the composition for codes 06, 09 and 10 … | idem; vírgula decimal | S2, S7 |
| Example Analysis!A18 | 319.05 | 319,05 | idem; vírgula decimal | S2, S7 |
| Example Analysis!C18 | EUR 319.05 of contributions - exactly 1,500.00 x 21.27 %. | EUR 319,05 of contributions - exactly 1 500,00 x 21,27 %. | idem; vírgula decimal | S2, S7 |
| Field Options!A43:E44 (2 linhas novas) | (vazio) | código 0 = não marcado (anexo; P35) | DSA (SAM v07, V-624) §2.10 p. 6 | S3 |
| Field Options!A45:E60 (16 linhas novas) | (vazio) | tabela P3 2026: 21,27 / 21,62 / 21,83 / 22,53 (indeterminado, grupos I–IV); 21,99 / 22,34 / 22,55 / 23,25 (determinado); +3,00 com acumulação (24,27 … 26,25) | XV-632 art. 3(1),(3),(4); I-1343 art. 17(2); Sodra tarifas 2026 | S7 |
| Sample File!B2 | NOTE: no sample FFData file exists in the sources folder, and the Electronic SD Notification data structure de… | Built from the SAM v07 data structure description (DSA, V-243 in the V-624 wording) (sections 2-3 and 5-7) and… | DSA (SAM v07, V-624) | S9, S11 |
| Sample File!B3:B176 e A77:A176 (273 células) | XML v1.0: `<FFData Version="1"><Form FormCode="SAM" FormVersion="07"><InsurerName>…`, 3 `<Form>` (um por página), ponto decimal, `x`, `07`, DocDate/DocNumber preenchidos, códigos 39001010101/47712120987 inválidos, 'civiline sutarti' | XML conforme DSA: `FFData(Version,CreatedByApp,CreatedByLogin,CreatedOn) > Form(FormDefId,FormLocation) > DocumentPages/Group/ListPages/ListPage + Pages Count=3 > Page(PageDefName,PageNumber) > Fields Count=27/63/48 > Field Name=…`; 6 segurados no SAM3SD e 1 linha no SAM3SDP; vírgula; 0/1; mês 7; DocDate/DocNumber vazios; códigos fictícios válidos; 'civilinę sutartį' | DSA (SAM v07, V-624) §2–§3 p. 1–9; FFData oficial | S1, S2, S3, S4, S5, S11, S16 |
| SAM Spec!K5 | 302123456 | 302123442 | GPM313.mxfd `ID_formatas_simple_f` (código de pessoa jurídica, 9 dígitos, controle mod 11) | B1 propagado (das GPM) |
| Example Analysis!A5 | 302123456 | 302123442 | GPM313.mxfd `ID_formatas_simple_f` (código de pessoa jurídica, 9 dígitos, controle mod 11) | B1 propagado (das GPM) |
| Sample File!B28 (dentro de `<Field Name="JuridicalPersonCode">`) | 302123456 | 302123442 | GPM313.mxfd `ID_formatas_simple_f` (código de pessoa jurídica, 9 dígitos, controle mod 11) | B1 propagado (das GPM) |

## O que ficou sem corrigir (e por quê)
| Achado | Situação | Motivo |
|---|---|---|
| S7 (parte) | Tabela P3 2026 enumerada (16 linhas). **Aberto:** (a) se a contribuição de 3 % da acumulação de pensão entra no P3; (b) base legal das taxas do Garantinis fondas e do Ilgalaikio darbo išmokų fondas (lidas só na página de tarifas da Sodra); (c) composição do P3 para os códigos 06, 09 e 10 do SAM3SDP. | Nenhuma fonte primária lida diz isso. Vai ao source-hunter. O exemplo do SAM3SDP (código 06, 21,27) ficou marcado como ilustrativo em `SAM Spec!T69` e `Example Analysis!D17`. `SAM Spec!T46` ficou só com a parte residual; a pergunta "empregado + empregador ou um lado só" foi fechada como **total** (p. 55.5; MXFD/DSA com uma tarifa por pessoa). |
| S8 (parte) | Teto de 60 VDU e base mínima do MMA entraram como casos-limite (`Population Rules!C7,D7`, `SAM Spec!M47`), com valores de 2026 e fonte. **Aberto:** como a Sodra quer A11/P3/A12 preenchidos no mês em que o teto é atingido e quando há complemento até o MMA. | Nem a instrução (extrato) nem a DSA tratam disso. Vai ao source-hunter. |
| S9 (parte) | `Version Control!E2` (log da v1.0) **não** foi reescrito: é histórico. A linha v1.1 registra a nova fonte. `Report Matrix!J2` foi reescrito e **retira os 93 %** sem pôr número novo. | Não há método documentado para o percentual; preferi não inventar um número. |
| S13 | Frase do "ponto 1488 / cinco dias úteis" **retirada** de `Population Rules!C13` (e o caso-limite correspondente de `D13`). | O número correto do ponto não pôde ser verificado (e-TAR e sodra.lt bloqueiam script; a redação local de 2015 não tem o ponto). |
| Numeração fina da V-243 (56.x, 86.6–86.8, 91.3.1, 249/250, 84.1 etc.) | Mantida como na v1.0. | Já listada como NOT VERIFIED na VAL-SAM; fora dos achados S1–S16. |
| "Data-structure versija 03" | Continua não confirmada (`Report Matrix!J2`). | A DSA se chama "versija 07" e não traz outro número de versão de estrutura. |

**Observações novas (fora de S1–S16, não alteradas):**
- DSA §7 (p. 11) dá `TaxRate` do SAM3SDP com comprimento 11, enquanto §6 e o MXFD dão 5. Mantido 5 (MXFD); vale perguntar à Sodra se houver rejeição.
- DSA §6–§7 descreve `PageTotal` como "Bendras lapų skaičius pranešime" (total de páginas da notificação), mas o exemplo da própria DSA (3 páginas, `PageTotal` 1) e o FFData oficial (2 páginas, `PageTotal` 1) usam o número de páginas **do anexo**. A spec segue os exemplos (= P20.2/P21.2).
- O FFData oficial do eFormFiller tem um atributo `Text` em cada `Field` (espelho do valor) e um elemento `FormErrors` (log de validação do programa). Nenhum dos dois consta da DSA; não foram reproduzidos no Sample File (registrado em `File Structure!C2`).
- O exemplo da DSA (p. 7) traz `Appendixes2`=0 com `Apdx2PageCount`=1: é o modelo de estrutura, não de valores.
- `SAM_2024_11 (1) - Client Example.pdf` não foi necessário (a DSA e o FFData oficial bastaram) e não foi aberto.

## Revalidação REVAL-SAM (2026-10-29): R1–R7 e S15

[[Research Pipeline/Lithuania/2026-10-29-correcoes/REVAL-SAM-v1.1|REVAL-SAM-v1.1]] deu PASS com 7 MINOR. Corrigido na mesma planilha (XML+zip, 35 células, todas em `FFDDEBF7`):

| Aba!Célula | Antes | Depois | Fonte | Achado |
|---|---|---|---|---|
| SAM Spec!J69 | Number, 2 dp, decimal comma (percentage, e.g. 21,27) | Number, 5 characters (MXFD; DSA section 7 lists 11), 2 dp, decimal comma (percentage, e.g. 21,27) | DSA (SAM v07, V-624) §6–§7 p. 11 (11 no SAM3SDP, 5 no SAM3SD); SAM-v07.mxfd 2018-12-20 (md5 7356515f…), PageDef 3, TaxRate_1..3 CellsInRowCount 5 | R1 |
| SAM Spec!M69 | XML elements TaxRate_1 to TaxRate_3, DataType Decimal, DecimalPlaces 2, 5 cells. Point 56.10: the general cont… | XML elements TaxRate_1 to TaxRate_3, DataType Decimal, DecimalPlaces 2. LENGTH DIVERGENCE BETWEEN THE TWO OFFI… | DSA (SAM v07, V-624) §6–§7 p. 11 (11 no SAM3SDP, 5 no SAM3SD); SAM-v07.mxfd 2018-12-20 (md5 7356515f…), PageDef 3, TaxRate_1..3 CellsInRowCount 5 | R1 |
| SAM Spec!M34 | XML element PageNumber, printed as the 'Lapas' part of 'Lapas ... is ...' at the top of the annex. The MXFD gi… | XML element PageNumber, printed as the 'Lapas' part of 'Lapas ... is ...' at the top of the annex. DSA section… | DSA (SAM v07, V-624) §4 p. 9 ('Neribojama') | R6 |
| SAM Spec!M53 | XML element PageNumber. The MXFD gives the SAM3SDP PageDef MinOccur 0 and MaxOccur 9999, the same range as SAM… | XML element PageNumber. DSA section 4: SAM3SDP pages from 0 to unlimited, the same range as SAM3SD, but the pa… | DSA (SAM v07, V-624) §4 p. 9 ('Neribojama') | R6 |
| SAM Spec!K30 | Rita Ritaite, +37052345679, rita@pavyzdys.lt | Rita Ritaitė, +37052345679, rita@pavyzdys.lt | spec M44/M63 (diacríticos); formato LT | R7 |
| Example Analysis!C6 | The employer's E-MAIL address, despite the XML element being named InsurerAddress and commented 'Draudejo adre… | The employer's E-MAIL address (box 7, XML element InsurerAddress). | DSA (SAM v07, V-624) §5 p. 9 | R2/S15 |
| Example Analysis!D6 | NAME/CONTENT MISMATCH: the printed form legend defines box 7 as 'el. pasto adresas' while the MXFD element nam… | DSA section 5 (p. 9) defines InsurerAddress as 'Draudėjo el. pašto adresas' (employer e-mail address), Text 68… | DSA (SAM v07, V-624) §5 p. 9 | R2/S15 |
| Example Analysis!C11 | EUR 3,000.00 of insurable income computed for the insured person for the whole calendar month. | EUR 3 000,00 of insurable income computed for the insured person for the whole calendar month. | spec M44/M63 (diacríticos); formato LT | R7 |
| Population Rules!D7 | Month in which cumulative income crosses EUR 138 729,00 (2026), where only PSD 6,98 continues above the ceilin… | Month in which cumulative income crosses EUR 138 729,00 (2026): above it a 0 % rate applies to the contributio… | I-1336 art. 10(9); XV-632 art. 3–4 (extratos 2026-10-27) | R3 |
| Population Rules!C7 | Populate A11 with the income computed for the CALENDAR MONTH on which contributions are calculated (point 55.1… | Populate A11 with the income computed for the CALENDAR MONTH on which contributions are calculated (point 55.1… | I-1336 art. 10(9); XV-632 art. 3–4 (extratos 2026-10-27) | R3 |
| Population Rules!D13 | Electronic signature certificate expiring before the deadline; deadline falling on a weekend or public holiday… | Electronic signature certificate expiring before the deadline; deadline falling on a weekend or public holiday… | raw/.../redakcija-2015-09-17_lrs494520.html p. 111 | V-243 |
| Field Options!E25 | Contributions annex for the insured excluding leavers. 0-9999 pages, 6 detail rows per page. | Contributions annex for the insured excluding leavers. 0 to unlimited pages (DSA section 4), 6 detail rows per… | DSA (SAM v07, V-624) §4 p. 9 ('Neribojama') | R6 |
| Field Options!E26 | Periods and contributions annex. 0-9999 pages, 3 detail rows per page. | Periods and contributions annex. 0 to unlimited pages (DSA section 4), 3 detail rows per page. | DSA (SAM v07, V-624) §4 p. 9 ('Neribojama') | R6 |
| Version Control!C3 | 29-Oct-26 | 2026-10-29 | — | R5 |
| Version Control!E3 | Corrections from the 28-Oct-26 independent validation (VAL-SAM S1-S16). Source added: SAM v07 data structure d… | Corrections VAL-SAM S1-S16: FFData per DSA (V-624), decimal comma, checkmarks 0/1, month 1-12, DocDate/DocNumb… | — | R5 |
| File Structure!B5 | PageDef 2 - SAM3SD annex. MinOccur 0, MaxOccur 9999, DefOccur 1 | PageDef 2 - SAM3SD annex. 0 to unlimited pages (DSA section 4) | DSA (SAM v07, V-624) §4 p. 9 ('Neribojama') | R6 |
| File Structure!B7 | PageDef 3 - SAM3SDP annex. MinOccur 0, MaxOccur 9999, DefOccur 1 | PageDef 3 - SAM3SDP annex. 0 to unlimited pages (DSA section 4) | DSA (SAM v07, V-624) §4 p. 9 ('Neribojama') | R6 |
| Sample File!B50 |       <Field Name="PreparatorDetails">Rita Ritaite, +37052345679, rita@pavyzdys.lt</Field> |       <Field Name="PreparatorDetails">Rita Ritaitė, +37052345679, rita@pavyzdys.lt</Field> | spec M44/M63 (diacríticos); formato LT | R7 |
| Report Matrix!I2 | Law on State Social Insurance No. I-1336 (consolidated redaction in force from 2026-07-01); SODRA Director's o… | Law on State Social Insurance No. I-1336 (consolidated redaction in force from 2026-07-01); SODRA Director's o… | e-TAR/e-seimas HTTP 403 em 2026-10-29; raw/.../2026-10-27_LRS_V-243_…_redakcija-2015-09-17_lrs494520.html p. 103.6–103.7, 104.2, 111 | V-243 |
| Field Options!E45:E60 (16 células) | …budget institutions and the Bank of Lithuania do not pay them… | …GF não é pago por Bank of Lithuania, budget institutions, political parties, trade unions, religious communities; ILDIF por Bank of Lithuania e budget institutions… | Sodra, tarifas 2026 (extrato) | R4 |

- **R1:** o MXFD em disco (`Archieved/Social security report specs/2-SD-v09(1)/sam/SAM-v07.mxfd`, FormDef 2018-12-20) dá 5 posições ao TaxRate do SAM3SDP. Mantive `I69` = 5 e registrei a divergência com as duas fontes em `J69`/`M69`, sem alinhar à DSA.
- **R3:** saiu a afirmação "só o PSD continua acima do teto". Fica **aberto**: se o GF, o ILDIF e os 3 % da acumulação de pensão param no teto de 60 VDU (nenhuma fonte lida diz).
- **V-243 / V-683:** **não li** a redação V-683 nem a consolidada vigente em nenhum arquivo. Essas citações (e os pontos 8, 52, 84.1, 86.6–86.8, 88, 91.3.1, 92.4, 95.4, 96.4, 249, 250) vêm da v1.0, que citava `SAM-V243-consolidado.pdf`, arquivo que não existe em disco. Tentei baixar o texto consolidado em 2026-10-29: e-TAR (`TAR.34A6775CE75B`, `/asr`, `/rs/actualedition/`) e e-seimas (`TAIS.376373/asr`) devolveram **HTTP 403**. Por isso nada foi salvo em `raw/docs/oficiais/LT/2026-10-29-Sodra-V243/` (pasta não criada) e as citações **foram mantidas**. `Report Matrix!I2` agora diz que a fonte não está arquivada. Em disco só existe a redação de 2015-09-17 (`raw/docs/oficiais/LT/2026-10-27-Sodra-SAM/2026-10-27_LRS_V-243_2010-06-04_redakcija-2015-09-17_lrs494520.html`), que é anterior à V-683 e tem outra numeração: anexos PT-SAM3SD/PT-SAM3SDP = p. 103.6–103.7; entrega atrasada = p. 104.2; prazo em dia não útil = p. 111. Não existe "PT-SAM3SD-M" nela.
- **Fonte a arquivar** (citam a V-243 vigente sem texto em disco; não alteradas, salvo I2): Report Matrix I2, F2, G2; Payroll Scope Summary B22; SAM Spec M13, T13, M29; Field Options E29, A31–A34, E33; Population Rules C4, D4, C13.
- **D13:** troquei "o ponto 52 não trata do fim de semana" porque a redação de 2015, p. 111, passa o prazo para o dia útil seguinte. A numeração vigente continua não arquivada.

Testes depois do patch: validate RSPEC **PASS (0/0/0)**; `check_sam.py` **106 OK / 0 FAIL**; nenhuma célula começa com "="; lint C29 limpo.

## validate_workbook.py --artifact RSPEC
```
FILE      C:/Users/instituto/Documents/brain-service/Research Pipeline/Lithuania/2026-10-29-correcoes/LT-SODRA-003-SAM-Spec_v1.1.xlsx
ARTIFACT  RSPEC
CONTRACT  Report Spec (Spain 9-sheet standard)  [measured from report-spec-template/ES-M296-001_ResumenAnual_Spec.xlsx]
SHEETS    (9) ['Version Control', 'Report Matrix', 'Payroll Scope Summary', 'SAM Spec', 'File Structure', 'Field Options', 'Population Rules', 'Example Analysis', 'Sample File']
VERDICT   PASS  (blocker=0 major=0 minor=0)
```

## check_sam.py
Comando: `python -I check_sam.py LT-SODRA-003-SAM-Spec_v1.1.xlsx "<pasta>/SAM-V07 SAMPLE (1).ffdata"` (saída 0).
```
OK    nenhuma celula de texto comeca com '=' (0 ocorrencias)
OK    9 abas: ['Version Control', 'Report Matrix', 'Payroll Scope Summary', 'SAM Spec', 'File Structure', 'Field Options', 'Population Rules', 'Example Analysis', 'Sample File']
OK    Sample File: sem BOM; 174 linhas XML
OK    declaracao XML UTF-8
OK    raiz FFData
OK    atributos de FFData iguais ao oficial (nomes): ['CreatedByApp', 'CreatedByLogin', 'CreatedOn', 'Version']
OK    FFData Version="1"
OK    um unico <Form>
OK    atributos de Form iguais ao oficial (nomes): ['FormDefId', 'FormLocation']
OK    FormDefId igual ao oficial
OK    Form > DocumentPages + Pages (DSA 2.2)
OK    oficial: Form > DocumentPages + Pages
INFO  FFData oficial traz tambem ['FormErrors'] (log de validacao do eFormFiller; nao consta da DSA 2.2, nao reproduzido)
OK    DocumentPages: Forma/ListPages/ListPage SAM + Group 'Priedas SAM3SD' iguais ao oficial
OK    DocumentPages: Group 'Priedas SAM3SDP' presente (DSA 2.3/3)
OK    Pages[Count]
OK    Pages Count=3 = 3 paginas
OK    Page PageNumber sequencial a partir de 1 (DSA 2.8)
OK    atributos de Page iguais ao oficial: {('PageDefName', 'PageNumber')}
OK    Field usa so o atributo Name (DSA 2.10)
INFO  FFData oficial (eFormFiller) usa em Field os atributos [('Name', 'Text')]; 'Text' espelha o valor e nao consta da DSA 2.10
OK    SAM p.1: Fields Count=27 = 27 Field
OK    SAM: nomes de Field unicos na pagina (DSA 2.10)
OK    SAM3SD p.2: Fields Count=63 = 63 Field
OK    SAM3SD: nomes de Field unicos na pagina (DSA 2.10)
OK    SAM3SDP p.3: Fields Count=48 = 48 Field
OK    SAM3SDP: nomes de Field unicos na pagina (DSA 2.10)
OK    SAM: os 27 nomes de campo = FFData oficial
OK    SAM3SD: os 63 nomes de campo = FFData oficial
OK    SAM3SDP: 48 nomes = DSA secao 7 (13 x 3 + 9)
OK    SAM: coluna H da 'SAM Spec' (27) = campos do Sample File
OK    SAM3SD: coluna H da 'SAM Spec' (63) = campos do Sample File
OK    SAM3SDP: coluna H da 'SAM Spec' (48) = campos do Sample File
OK    valores decimais com virgula e 2 casas (DSA 2.10) 
OK    nenhum ponto decimal
OK    marcas 0/1 (DSA 2.10): {'RevisedDocument': '0', 'Appendixes2': '1', 'Appendixes3': '1'}
OK    CycleMonth=7: numero 1-12 sem zero
OK    SAM: DocDate e DocNumber vazios (DSA 5-7 'nepildomas')
OK    SAM: FormCode/FormVersion 07 como Field
OK    SAM3SD: DocDate e DocNumber vazios (DSA 5-7 'nepildomas')
OK    SAM3SD: FormCode/FormVersion 07 como Field
OK    SAM3SDP: DocDate e DocNumber vazios (DSA 5-7 'nepildomas')
OK    SAM3SDP: FormCode/FormVersion 07 como Field
OK    datas AAAA-MM-DD: ['2026-07-01', '2026-07-31']
OK    7 codigos pessoais (ficticios) com digito de controle valido
OK    1o digito do codigo coerente com o genero do sobrenome (-is/-as masc.; -ė fem.)
OK    ReasonCode no dominio 01-10
OK    ReasonText com diacriticos, <= 65
OK    SAM3SD linha 1: A12 638.10 = A11 3000.00 x P3 21.27 %
OK    SAM3SD linha 2: A12 638.10 = A11 3000.00 x P3 21.27 %
OK    SAM3SD linha 3: A12 638.10 = A11 3000.00 x P3 21.27 %
OK    SAM3SD linha 4: A12 638.10 = A11 3000.00 x P3 21.27 %
OK    SAM3SD linha 5: A12 638.10 = A11 3000.00 x P3 21.27 %
OK    SAM3SD linha 6: A12 638.10 = A11 3000.00 x P3 21.27 %
OK    SAM3SD: P7 18000,00 = soma A11 18000.00
OK    SAM3SD: P8 3828,60 = soma A12 3828.60
OK    P20.4 = soma do anexo SAM3SD
OK    P20.5 = soma do anexo SAM3SD
OK    P20.3 = 6 segurados
OK    SAM3SD: paginas = P2x.2 = PageTotal = 1
OK    Appendixes2 coerente com a existencia do anexo
OK    SAM3SD: InsurerCode = pagina SAM (C2334)
OK    SAM3SDP linha 1: A12 319.05 = A11 1500.00 x P3 21.27 %
OK    SAM3SDP: P7 1500,00 = soma A11 1500.00
OK    SAM3SDP: P8 319,05 = soma A12 319.05
OK    P21.4 = soma do anexo SAM3SDP
OK    P21.5 = soma do anexo SAM3SDP
OK    P21.3 = 1 segurados
OK    SAM3SDP: paginas = P2x.2 = PageTotal = 1
OK    Appendixes3 coerente com a existencia do anexo
OK    SAM3SDP: InsurerCode = pagina SAM (C2334)
OK    P23 = P20.2 + P21.2
OK    SAM Spec K47 638,10 = K45 x K46
OK    K48/K49 = pagina cheia (6 linhas)
OK    K18 = K35 = ceil(128/6) = 22 folhas
OK    K20 384000,00 = 128 x A11
OK    K21 81676,80 = 128 x A12
OK    K27 P23 = K18 + K23
OK    SAM3SDP: K25/K26 = K68,K71/K70,K72
OK    K70 = K68 x K69
OK    K12 mes 7; K13/K17/K22 marcas 0/1
OK    K40 38507159910 e K59 37603099979 com digito valido
OK    I32/I51/I74 FormVersion = 2
OK    F8,F9,F37,F38,F56,F57 = N (DocDate/DocNumber)
OK    nenhum exemplo da coluna K com ponto decimal 
OK    Example Analysis A13 = A11 x A12
OK    Example Analysis A14 = 6 x A11
OK    Example Analysis A9/A10 = SAM Spec K27/K19
OK    Example Analysis A7 mes 7, A8 marca 1
OK    Example Analysis A18 = 1500 x A17
OK    Field Options B45 21,27 = Indefinite / gr. I
OK    Field Options B46 21,62 = Indefinite / gr. II
OK    Field Options B47 21,83 = Indefinite / gr. III
OK    Field Options B48 22,53 = Indefinite / gr. IV
OK    Field Options B49 21,99 = Fixed-term / gr. I
OK    Field Options B50 22,34 = Fixed-term / gr. II
OK    Field Options B51 22,55 = Fixed-term / gr. III
OK    Field Options B52 23,25 = Fixed-term / gr. IV
OK    Field Options B53 24,27 = Indefinite / gr. I +3%
OK    Field Options B54 24,62 = Indefinite / gr. II +3%
OK    Field Options B55 24,83 = Indefinite / gr. III +3%
OK    Field Options B56 25,53 = Indefinite / gr. IV +3%
OK    Field Options B57 24,99 = Fixed-term / gr. I +3%
OK    Field Options B58 25,34 = Fixed-term / gr. II +3%
OK    Field Options B59 25,55 = Fixed-term / gr. III +3%
OK    Field Options B60 26,25 = Fixed-term / gr. IV +3%
OK    16 taxas, min 21,27 / max 26,25
OK    Field Options B12:B23 = 1..12
INFO  teto 2026: 60 x 2312,15 = 138729.00; MMA 2026 = 1153

RESUMO: 106 OK, 0 FAIL
```

## md5
- `LT-SODRA-003-SAM-Spec_v1.1.xlsx`: `1447d6b08e180eaab035f3f16b286ae1` (depois da revalidação R1–R7; antes `f3ce3b9db77c2543423049ca4310ee1c` após o JuridicalPersonCode, e `54e60eb15e4efd972a5bb9a6c66e4002` no build). validate RSPEC PASS e check_sam.py 106 OK / 0 FAIL repetidos com o arquivo final.
- Base v1.0 (inalterada): `b6a8074989c7be3948e1a6f43db39d64`

## Bloco de prova
- **Pedido → resposta:** S1–S6 e S10–S12, S14–S16 corrigidos; S7, S8, S9 corrigidos com resíduo listado acima; S13 frase retirada. Version Control v1.1; 9 abas; destaque `FFDDEBF7`; nenhuma célula com "=".
- **Fontes:** DSA §1–§7 p. 1–12; FFData oficial (estrutura); XV-632 art. 3–4; I-1343 art. 17(2); I-1336 art. 10(7)–(9); Nutarimas 700/2025; página de tarifas Sodra 2026; instrução DataService p. 4–15.
- **Teste:** validate_workbook RSPEC PASS (0/0/0); check_sam.py 106 OK / 0 FAIL (estrutura × FFData oficial, campos × DSA §7 × coluna H, vírgula, 0/1, mês, DocDate/DocNumber, dígito de controle, todas as contas).
- **Confiança:** 95% no que foi corrigido. Fica abaixo de 100% pelos resíduos de S7/S8 (precisam de fonte que ainda não temos) e porque o arquivo não foi testado no envio real (EDAS/DataService).

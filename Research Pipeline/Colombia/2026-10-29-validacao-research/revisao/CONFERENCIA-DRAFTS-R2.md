# Conferência independente dos DRAFTs COVAL, rodada 2 (IEEE 1012 V&V), 2026-10-29

Esta conferência foi feita por um verificador independente, que não fez as edições. Ela confere a rodada 2 de correção contra os problemas de [[CONFERENCIA-DRAFTS]], as decisões de [[DECISOES-RODADA2]] e as regras de [[REGRAS-EDICAO]]. Nenhum DRAFT, base ou achado foi alterado. Os scripts e diffs estão em `revisao/_check2/` (um diff JSON base × DRAFT por artefato, `CCG_hunks.txt`, `CCG_accept.txt`, `ne_draft.xml`, `r1r2.py`, `grepx.py`).

**Método**
1. md5 das 11 bases.
2. Diff próprio base × DRAFT refeito do zero:
   - xlsx: valor ou fórmula de toda célula de todas as abas, com openpyxl só leitura, e as entradas do zip byte a byte;
   - docx: texto de "rejeitar tudo" e de "aceitar tudo".
3. Diff rodada 1 × rodada 2: diff anterior em `_check/` × diff novo, isolando as células e os parágrafos que mudaram na rodada 2.
4. Cada mudança da rodada 2 cruzada com a seção "Rodada 2" do CHANGELOG e relida na fonte primária local.
5. Contas refeitas.
6. Testes mecânicos:
   - `validate_workbook.py` nos 10 xlsx;
   - `validate.py` do docx, com `--original` e `--author`;
   - XSD 1.0.6 na amostra da NE;
   - comprimento dos segmentos PILA.
7. Busca de resíduos em todos os DRAFTs: "2.2.1.2.1.4", "waiver", "2381", "617,000", "7,404,000", "868", "nearest 1,000".

**Critério do veredito**
- **PASS:** integridade íntegra e nenhum problema S1–S3.
- **PASS COM RESSALVA:** sobram só S4, ou S3 já existente na base que nenhuma decisão da rodada 2 cobriu.
- **FAIL:** há S1/S2, ou a rodada 2 introduziu um problema S3.

---

## Veredito por artefato

| Artefato | Veredito | Resumo |
|---|---|---|
| CCG v1.5 | **PASS** | Todos os 9 problemas do CCG foram resolvidos. A rodada 2 não introduziu erro. |
| WTC v1.7 | **PASS** | B229 = nome do Global WTC (62591). DD-14 ficou NÃO APLICADA por decisão. |
| DD v1.4 | **PASS COM RESSALVA** | Os problemas da rodada 1 foram resolvidos. Sobra G11, texto antigo de "waiver" (S3, já na base), e quatro S4. |
| PILA-003 / 007 v1.1 | **PASS COM RESSALVA** | P-02, A-16, L107/L152 e J47 foram resolvidos. Só S4: o Version Control não cita os IDs da rodada 2. |
| NE v1.1 | **PASS COM RESSALVA** | NE-05 foi aplicada e o XSD continua VÁLIDO. Sobra Population Rules C21 com arredondamento a 1.000 pelo ET 868 (S3, já na base) e dois S4. |
| FORMS (002, 004, 005, 006) | **FAIL** | SIM-03 foi aplicada, mas a 004 ficou incoerente consigo mesma: as casillas 60 e 75 agora valem 7.406.784, e a própria spec manda aproximar todas as casillas ao múltiplo de 1.000 (S3, introduzido na rodada 2). Também sobra a 002 Population Rules C5 (S3, já na base). |
| Payslip v1.2 | **PASS** | H55 = 192.000. Líquido, aportes e custo total conferem. SIM-08 foi revertida e marcada NÃO APLICADA. VC e marcadores foram corrigidos. Os 2 blockers C29 já estavam na base. |
| SIR v1.2 (redline) | **PASS** | Versões CCG v1.5, DD v1.4, specs v1.1 e Payslip v1.2 corretas. "inc. 3" confere com a fonte. |

---

## Checagem 1: cada problema de CONFERENCIA-DRAFTS.md

| # | Problema (rodada 1) | Situação | Evidência |
|---|---|---|---|
| 1 | CCG A-16: "art. 15 num. 1" (S2) | **Resolvido** | "Aceitar tudo": nenhuma ocorrência de "2.2.1.2.1.4", "waive/waiver", "elects in writing", "proves affiliation" ou "pension system abroad". As 11 posições citam "Law 100 of 1993 art. 15 num. 2 (as amended by Law 797 of 2003 art. 3)". O texto bate com a Ley 100 local (FuncionPublica): "2. En forma voluntaria: … Los extranjeros que en virtud de un contrato de trabajo permanezcan en el país y no estén cubiertos por algún régimen de su país de origen o de cualquier otro". A redação não afirma regra além do texto. |
| 2 | PILA-003 M120 P-02 (S2) | **Resolvido** | M120 agora diz que a regra ACCAI vale "to this field as well as to campo 51" (p.158, §2.1.2.3.19; p.157, §2.1.2.3.18). Relido no AT2 v30 local: a regra está na p.157, fim do campo 51, e na p.158, fim do campo 52; o 2.1.2.3.20 começa na p.159. |
| 3 | DD × WTC DD-14 (S2) | **Resolvido (decisão 3)** | DD W115: "Housing-interest deduction wage type: pending creation in the Global WTC (no code available)". A menção a uma verba inexistente no WTC saiu. No WTC: NÃO APLICADA, por decisão. |
| 4 | NE-05 (S3) | **Resolvido** | B23, B24, B39, B43, B51, B69, B92 e B112 = Novedad, Periodo, Empleador, Trabajador, Pago, Cesantias, Deducciones e Redondeo. Todos os nomes existem no XSD 1.0.6. Ressalva S4 na tabela final (Replace/Delete). |
| 5 | FORMS SIM-03 (S3) | **Aplicado, com efeito colateral** | 004: K52, K63, A27, A30, A36, C27, D33 e Sample A79/A90 = 7.406.784. 005: K37, A27, D33 e Sample A77. 002: C15/D15 citam o DUR 1.6.1.11.11 e a NE com 617.232,00. Contas: 12 × 617.232 = 7.406.784; 33.888.000 / 7.406.784 = 4,575 → "4.58"; 7.406.784 / 169.440.000 = 4,371% → "4.37%". **Novo S3** na 004, ver a tabela final. |
| 6 | CCG A-04 (S3) | **Resolvido** | T25R4: "Until the income-tax return … becomes final (Tax Code art. 632; Law 962 of 2005 art. 46, as modified by Law 1819 of 2016 art. 304)". Conferido nas fontes locais: Res. DIAN 13/2021 ("artículo 46 de la Ley 962 de 2005, modificado por el artículo 304 de la Ley 1819 de 2016") e DUR 1625 (conciliação fiscal: "término de firmeza … artículo 632 … modificado por el artículo 46 de la Ley 962 de 2005 y el artículo 304 de la Ley 1819 de 2016"). |
| 7 | CCG A-01: premissas (S3) | **Resolvido** | P3669: "The 204-tax-unit test is applied to the employee's monthly income, and the final settlement … is not counted … (operating readings …)". Read 3 repete as premissas: 4.500.000 = 85,92 UVT; 4.875.000 = 93,0805 UVT. |
| 8 | CCG P5810 "no averaging" (S3) | **Resolvido** | "…except that a dismissal indemnity or retirement bonus is withheld outside the monthly base (… art. 401-3 … DUR 1.2.4.1.8)". P5515 também foi ajustado. |
| 9 | CCG × PILA-003, Ley 2381 (S3) | **Resolvido** | 003 G120/M120 e 007 M104: "applies only from the date Ley 2381/2024 is in force; until then, Ley 797/2003 table". O CCG mantém "Not yet in force … 2027", e o CCG não aplica a tabela. A 007 M98 ficou sem a condição, com motivo válido (descreve o que o operador faz, sem aplicar tabela). NE Field Options D108 e WTC "Global WTC Coverage" C13 dizem o mesmo. |
| 10 | WTC B229 (S3) | **Resolvido** | B229 = "Birth and Marriage Allowance". Global_WTC_V1_0.xlsx (md5 49c36334…), linha 229 = 62591 "Birth and Marriage Allowance". D229 guarda a frase original da v1.6. |
| 11 | Payslip H55 (S3) | **Resolvido** | `=ROUND(H54*0.12,0)` = 192.000 (12% × 1.600.000 = 1% × 19.200.000; Ley 52/1975 art. 1). H58/H68 = 4.181.583; H69 = 9.945.883. |
| 12 | DD × NE, tipo 75 (S3) | **NÃO APLICADA, motivo válido** | O Anexo da NE não traz regra para o tipo 75. Fica como lacuna aberta, registrada no CHANGELOG da NE. |
| 13 | DD × PILA-003 L107/L152 (S3) | **Resolvido** | L107 = `Employee.PILA_Salary_Type`; L152 = `Employee.PILA_Special_Pension_Rate_Indicator` (DD l.112/113). Ressalva S4 na tabela final. |
| 14 | Citação do Decree 1072 na PILA-003 e no DD (S3) | **Resolvido** | 003 A36, M69 e C22 (e C46) e DD G61 citam a Ley 100 art. 15 num. 2. Nenhuma ocorrência de "2.2.1.2.1.4" em nenhum DRAFT. Resíduo sem citação no DD G11 (abaixo). |
| 15 | SIR, versões (S3) | **Resolvido** | D8a/D8b citam CCG v1.5, specs v1.1, DD v1.4 e Payslip v1.2. Nenhum "v1.4", "v1.3" ou "par. 3" nas linhas novas. |
| 16 | Payslip SIM-08 (S4) | **Resolvido** | H34, H35, H44, H45, H48 e H49 idênticos à base. Status: NÃO APLICADA, com motivo. |
| 17 | Payslip: VC, marcadores, UVT (S4) | **Resolvido** | VC em Payslip Spec B83:E85. Marcadores trocados por "Illustrative…". O log corrigido diz 42,9748 (confere: 267,7673 − 150 = 117,7673 × 0,28 + 10). |
| 18 | DD W99 (S4) | **Resolvido** | Cita a 006 v1.1 L10 (Company.Cesantias_Fund_Code). |
| 19 | DD F36/F37 (S4) | **Resolvido** | AT2 v30 local: campo 2 na p.9 (PE vedado a partir de set/2023); campo 3 na p.10 (PE com 15 dígitos, PT até 8). Confere. |
| 20 | DD: 70 células sem azul (S4) | **Resolvido** | Diff: 864 células, todas FFDDEBF7. |
| 21–24 | CCG T86R5, T150R4, T48R1, "May be waived" (S4) | **Resolvidos** | "the sum of the taxable payments … divided by 12"; "Fully taxable — withheld outside…"; "(30-day month convention: day 31 is not counted)"; "Voluntary option". |
| 25 | SIR "inc. 3" (S4) | **Resolvido** | A Res. DIAN 13/2021 local diz "el inciso 3 del artículo 771-2 del Estatuto Tributario". |
| 26 | PILA J47 (S4) | **Resolvido** | "ZERO-filled … when populated; BLANK (10 spaces, positions 228-237)…", coerente com G47. |
| 27 | 002 K20 (S4) | **Resolvido** | K20 vazia, com fundo azul. A explicação continua em M20. |

## Checagem 2: a rodada 2 introduziu erro?

| Artefato | Resultado |
|---|---|
| CCG | Não. A frase nova de A-01 em P3669 confere: 204 × 52.374 = 10.684.296. A-04 tem fonte local. "Aceitar tudo": 91 blocos, todos de IDs do log (rodadas 1 e 2). |
| PILA | Não. As frases novas conferem com o AT2 v30 pp.157-158. |
| Payslip | Não. Contas refeitas abaixo. |
| SIR | Não. |
| WTC | Não. |
| DD | Não. F36/F37 conferem com o AT2. |
| 004 | **Sim (S3).** As casillas 60/75 passaram a 7.406.784. A justificativa do log: o certificado não é declaração, e o DUR 1.6.1.11.11 só alcança declarações e recibos de pago (leitura plausível do texto local). Mas 35 regras da própria 004 não mudaram: J27–J67 "N (whole pesos, nearest 1,000…)", P27–P67, Population Rules A12/C12, Sample A16. A 005 File Structure B27 também diz que o Form. 220 aproxima a 1.000. O artefato ficou contraditório. |

**Contas (rodada 2).** Payslip:
- Líquido: 19.200.000 − 768.000 − 768.000 − 192.000 − 2.250.764,60 = **15.221.235,40** (cache I8 = 15221235.4).
- Juros: 12% × 1.600.000 = **192.000** (cache H55).
- Aportes do empregador: 1.632.000 + 2.304.000 + 100.300 + 768.000 + 384.000 + 576.000 = **5.764.300** (H67).
- Provisões: 1.600.000 + 192.000 + 1.600.000 + 789.583 = **4.181.583** (H68).
- Custo total do empregador: **9.945.883** (H69).

SIM-03: (8.190.000 − 7.856.100) × 0,28 + 523.740 = **617.232**; × 12 = **7.406.784**.

## Checagem 3: diff base → DRAFT = CHANGELOG (rodada 1 + rodada 2)

| Artefato | Células/blocos base × DRAFT | Rodada 2 isolada (diff r1 × r2) | = log? |
|---|---|---|---|
| CCG | "rejeitar tudo" = texto da v1.4 nos 7.970 parágrafos (idêntico); 91 blocos | A-16, A-04, A-01 (P3669, Read 3, P5810, P3359), T150R4, T48R1, rótulos de "waiver" | Sim |
| WTC | 16 | B229 | Sim |
| DD | 864 | G61, W115, W99, F36, F37 (+ fill nos 70 cabeçalhos) | Sim |
| PILA-003 | 61 | A36, C46, J47, M69, L107, G120, M120, L152, C22 | Sim |
| PILA-007 | 7 | M104 | Sim |
| NE | 71 | B23, B24, B39, B43, B51, B69, B92, B112 | Sim |
| 002 | 17 | C15, D15, K20 | Sim |
| 004 | 29 | K52, K63, A27, A30, A36, C27, D33, A79, A90 | Sim |
| 005 | 61 | K37, A27, D33, A77 | Sim |
| 006 | 10 | nenhuma | Sim |
| Payslip | 112 | H55, A85, C13, I13 (EN/ES), H34, H35, H44, H45, H48, H49 revertidas, Payslip Spec E81 e B83:E85 | Sim |
| SIR | redline md5 8f186e65… | D8a, D8b, S-02a | Sim |

## Checagem 4: integridade

| Artefato | Resultado |
|---|---|
| CCG | md5 base 8b087e4d… (original e `_base`). Só `word/document.xml` mudou. 127 `w:ins` + 122 `w:del`, todos de "Mercans Compliance (COVAL)" com data 2026-10-29T00:00:00Z. `validate.py --original --author`: "All validations PASSED!" (7970 → 7976 parágrafos). Abre no python-docx. |
| xlsx (todos) | md5 das bases conforme o PLANO §3. Todos abrem em openpyxl `read_only`. Nenhuma entrada de drawings, media ou comments mudou (`protected_changed` vazio nos 10). Todas as células alteradas com FFDDEBF7, exceto Payslip `Colombia (EN/ES)!H3`, esvaziadas na rodada 1 (já aceito antes). |
| NE | Amostra `Sample File` A55:A161 VÁLIDA contra `NominaIndividualElectronicaXSDV1.0.6.xsd`. |
| PILA | Segmentos 003 17/17 e 007 18/18 com o comprimento exato. |
| `validate_workbook.py` | PASS nos 9 workbooks. O Payslip dá FAIL com os mesmos 2 blockers C29 da base (Payslip Spec!E12, Unit Rate Details!G2), conferidos rodando a v1.1. Nenhum novo. |

## Checagem 5: consistência entre artefatos

| Tema | Resultado |
|---|---|
| Citação da Ley 100 art. 15 num. 2 | Está em todas as posições que citavam o Decree 1072: CCG (11), PILA-003 (A36, M69, C22) e DD G61. **Resíduos sem citação:** DD G11 ("together with proof of affiliation to a foreign pension system, the foreign-national pension-waiver flag") e DD W61 ("Requires documentary proof on file"). |
| Ley 2381 | A condição tem a mesma redação no CCG, na 003 G120/M120 e na 007 M104; NE D108 e WTC C13 são coerentes. Observação, não erro: o AT2 v30 já operacionaliza o "N" desde jul/2025 (pp.157-158). A condição de vigência é decisão do usuário (item 2) e deve ser revista quando a Corte decidir. |
| SIR | Referências: CCG v1.5, DD v1.4, specs v1.1, Payslip v1.2. Confere. |
| Arredondamento da retenção | NE (617.232,00), 002 (617.000 só no formulário) e 005 (sem aproximar) coerentes entre si. Ainda dizem "aproximar cada empregado a 1.000 (ET 868)": NE Population Rules C21 e 002 Population Rules C5. A 004 está contraditória consigo mesma (acima). |
| DD × PILA-003 | A PILA usa os campos novos. O DD W36 e o W38 (flags antigas) ainda dizem que alimentam a "CO-PILA-003 (T2R2-041/079)". Os campos novos (W112/W113) não trazem o nome `Employee.PILA_*` usado na spec. |

---

## Problemas restantes

| Artefato | Local | Problema | Correção sugerida | Gravidade |
|---|---|---|---|---|
| FORMS 004 (e 005) | 004 Formulario 220 Spec!J27:J67 e P27:P67, Population Rules!A12/C12, Sample File!A16; 005 File Structure!B27 | Introduzido na rodada 2: as casillas 60/75 (K52, K63, Sample A79/A90, Example A27/A30/A36) valem 7.406.784, mas a própria spec manda aproximar toda casilla a 1.000 ("as the instruction guide (Res. 000022/2024) directs"). A regra de 1.000 do Form. 220 não tem fonte local legível: a Res. 22/2024 local não traz o instrutivo. | Decidir com fonte. **Se** o instrutivo do 220 não exigir aproximação (o DUR 1.6.1.11.11 só cita declarações e recibos), reescrever J/P27-67, C12, A16 e 005 B27. **Senão**, voltar as casillas a 7.407.000 e manter 7.406.784 só no texto de C27/A36. | S3 |
| FORMS 002 | Population Rules!C5 | "Each employee's withholding is itself already approximated to the nearest 1,000 under ET art. 868; accumulate those approximated figures…". Contradiz SIM-03 e a própria C15/D15: com vários empregados, a casilla 93 sai diferente. Já estava na base. | "Accumulate the unrounded withholding of every employee and approximate the total to the nearest 1,000 (DUR 1625 de 2016 art. 1.6.1.11.11)". | S3 |
| NE | Population Rules!C21 | "…convert back to pesos, and approximate to the nearest 1,000 under ET art. 868". Contradiz Example C39 (617.232,00 sem arredondar) e o SIM-03. Já estava na base. | "…convert back to pesos (two decimals; no approximation to 1,000 in the payroll document, DUR 1.6.1.11.11 applies only to forms)". | S3 |
| DD | Country Fields!G11 | O Document Type ainda descreve "proof of affiliation to a foreign pension system" e um "pension-waiver flag": é a lógica antiga, oposta à do art. 15 num. 2 aplicada em G61. | Trocar pela redação de G61 ("foreign national … not covered by a pension regime …; voluntary affiliation, option per employee"). | S3 |
| DD | Country Fields!W61 | "Requires documentary proof on file" e "suppresses the pension contribution", resíduos da regra de dispensa. | Alinhar a G61 (opção por empregado, com a citação); retirar a exigência de prova sem fonte. | S4 |
| DD | Country Fields!W36, W38, W112, W113 | W36/W38 dizem que as flags antigas alimentam a CO-PILA-003 T2R2-041/079, mas a PILA agora usa os campos novos. W112/W113 não trazem o nome `Employee.PILA_Salary_Type` / `Employee.PILA_Special_Pension_Rate_Indicator`. | Em W36/W38, retirar a referência à PILA-003. Em W112/W113, escrever "Spec ref: Employee.PILA_Salary_Type - CO-PILA-003 (T2R2-041…)" e o equivalente para T2R2-079. | S4 |
| NE | File Structure!B119, B121 | O ramo da NominaIndividualDeAjuste ainda diz "Replace"/"Delete". O XSD de ajuste 1.0.6 usa `Reemplazar`/`Eliminar` (mesmo motivo do NE-05). | `Reemplazar` / `Eliminar`. | S4 |
| NE, 002, 004, 005, PILA-003, PILA-007, DD | Version Control (última linha) | A linha de VC não cita os IDs aplicados na rodada 2: NE-05; SIM-03 (002/004/005); A-16 (003, DD); P-02 (007). Regra 8. | Acrescentar os IDs da rodada 2 à linha v1.x DRAFT existente. | S4 |

**Observações (não são problema de edição):**
- Payslip: o arredondamento é misto. H34/35/44/45/48/49 usam `ROUND(...,0)` (v1.1); H36/H46/H47/H65 (SIM-01) usam `ROUNDUP(...,-2)`. Os valores do exemplo não mudam. Rever junto com SIM-08 quando houver regra de rateio.
- Ley 2381: a condição de vigência foi decisão do usuário; o AT2 v30 já trata o "N" desde jul/2025.
- WTC D229 ("This bonus is granted at the employer's discretion…") é o texto original movido. Combina com "mera liberalidad" (F229).

## Bloco de prova
- **Pedido → resposta:**

  | Pedido | Onde está |
  |---|---|
  | (1) | Tabela da checagem 1 (27 itens) |
  | (2) | Checagem 2 e contas |
  | (3) | Checagem 3 |
  | (4) | Checagem 4 |
  | (5) | Checagem 5 |
  | Veredito por artefato | Tabela no início |
  | Problemas restantes | Tabela final |

- **Fontes lidas nesta conferência (locais):**
  - Ley 100/1993 art. 15 (FuncionPublica);
  - AT2 v30 pp.9-10, 12 e 157-159 (txt);
  - DUR 1625: arts. 1.6.1.11.11, menções à Ley 962 art. 46 e à Ley 1819 art. 304;
  - Res. DIAN 13/2021: conservação (art. 23) e o "inciso 3 del artículo 771-2";
  - Res. DIAN 22/2024 (sem o instrutivo);
  - Global_WTC_V1_0.xlsx (linha 229);
  - XSDs 1.0.6 da NE (individual e de ajuste).
- **Teste mecânico:**
  - md5 das 11 bases (= PLANO §3);
  - diff célula a célula e por entrada do zip nos 10 xlsx;
  - "rejeitar tudo" = v1.4 no docx;
  - `validate.py` do docx: PASSED;
  - XSD: VÁLIDO;
  - PILA: 35/35 segmentos;
  - `validate_workbook.py`: 9 PASS e Payslip com 2 blockers da base;
  - contas acima, em aritmética exata.
- **Confiança: 92%.** O que falta:
  - não li o instrutivo do Form. 220, que decide o S3 da 004;
  - o texto do art. 304 da Ley 1819 e o ET 714 não foram lidos na íntegra (a citação vem da Res. 13/2021 e do DUR locais);
  - não houve render visual do Payslip.

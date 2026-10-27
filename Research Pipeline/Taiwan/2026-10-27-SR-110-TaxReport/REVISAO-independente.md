# SR-110 Taiwan Tax Report Spec v1.3: revisão independente (2026-10-27, revisor ≠ construtor, só leitura)

**Veredito: FAIL, rodada 1.** Não há BLOCKER, mas 3 achados MAJOR precisam ser corrigidos antes de devolver ao Mohit. Medido ao vivo: md5 `50a250e8…` (v1.3) e `8b19384f…` (base).
**Conferido e OK:**
- **Fonte:** o 要點 1141210 é do 財政部財政資訊中心 ("中華民國114年12月修正", modDate do PDF 2025-12-09). A página da FIA lista 1141210 e o 草案 1141113. Não existe edição 115. A diferença entre 112 e 114 no campo 20 e no prazo +5 dias do não residente foi confirmada.
- **Escopo:** na minha comparação célula a célula (valor, fill, fonte, borda, formato), mudaram só 48 células (VC 5, RM 10, Spec 33), todas com `FFDDEBF7`. Testing, Testing1 e Options têm 0 diferença. Mesclagens e validações estão iguais. Nenhuma fórmula. Todo o XML está bem formado. As contagens de styles (fills 10, cellXfs 108) batem. Não há dado pessoal: a Testing1 só tem valores de teste.
- **Campos:** 32 campos, "|", UTF-8, nome do arquivo (操作實務 p.5), campo 9 = 扣繳稅額, campo 20 = 2517, país/tratado/TIN por tipo de ID ("NOTIN"), período YYYMMYYYMM e campo 31 batem com o 要點 114 (itens 2, 9, 14–17, 18(1), 22, 23, 25, 26). RM B5 bate com o ITA art. 92.
- **Issues do Mohit:** as 3 estão refletidas: H10/H11/H22/H18/H33 por status, B11 e H11, H21. Todos os PEs existem no WTC V2.8 (2517, 2552, 2572, 2582, 2592–2594, 58008, 58009, 62180–2, 62200–9) e o 58105 não existe. As variáveis do DD existem (`residential_status` 0/1, `identity_type`, `employee_postcode`, `taiwan_city`, `district`, `company_registration_number`). As que faltam estão marcadas "TO BE CONFIRMED BY MOHIT/BA".

**Achados:**
1. **MAJOR. Spec!H4:** o residente `LPAD($row_number;8;'0')` gera "00000001", o mesmo serial do não residente `CONCAT('00';…)` no mesmo UBN. A regra é "申報單位統一編號相同時流水號不可重複" (要點 114 item 2). Correção: o residente não usa o prefixo "00" (ou um contador único por UBN no ano), com TBC.
2. **MAJOR. Spec!H20 (e H19):** a regra diz "all full-width or all half-width", mas o CONCAT junta o CEP (DD Number, meia largura) com cidade/distrito em chinês e linhas de endereço. Isso gera largura mista, o que viola a nota 2 do 參.三.(三). Correção: dizer explicitamente que a conversão é para full-width (a amostra G20 já usa "２") ou marcar TBC para a função.
3. **MAJOR. Spec!H7:** o campo 5 (所得格式, M) continua sem mapeamento. A regra 50 × 93 (6218x) só existe em prosa (J7, RM B9), e H10, H11 e H22 dependem dela. Correção: incluir uma expressão em H7, por exemplo "93 se houver 62180:62182 no registro, senão 50".
4. **MINOR. Version Control!E14:** "Draft" está fora da validação E13:E23 ("In Progress, Under Review, Approved"), então o Sheets marca a célula como inválida. Usar "Under Review".
5. **MINOR. Spec!I22:** o texto "Applies to retirement payments only" contradiz H22/J22 (só formato 50, salário).
6. **MINOR. Spec!L10/L11:** o texto "Non-resident: Monthly…" não foi marcado como superado e contradiz a regra "por data de pagamento" (K10/K11 foram marcados).
7. **MINOR. Spec!G31:** a amostra "TW" não está no anexo 42 e contradiz o novo padrão em branco de H31.
8. **MINOR. Spec!D18, D21, D28, D33:** os tipos estão como "Numeric", mas o oficial é X (要點 114, tabela de campos). Em D33 (MMDD), um tipo numérico perde o zero inicial. A correção aplicada em D13 ficou inconsistente com essas células.
9. **MINOR. Spec!J5/J8:** ainda citam páginas do 112 ("page 181/179"), enquanto B16 declara a edição 114.

**Entregabilidade:** a spec pode ser testada pelo Mohit com residente taiwanês. O não residente e o estrangeiro dependem de 7 variáveis TBC e da decisão U8 × IMX (RM B16). Corrigir os itens 1–3 e reenviar para a rodada 2.

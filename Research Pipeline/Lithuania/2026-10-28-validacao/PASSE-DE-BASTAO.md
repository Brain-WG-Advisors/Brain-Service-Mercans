# Passe de bastão: Pipeline → janela Lituânia (29/10)

> [[Research Pipeline/Lithuania/2026-10-28-validacao/CONFERENCIA]] · Hub [[Lituania]] · [[correcoes]] (2026-10-28)

Decisão do usuário em 29/10: tudo da Lituânia sai da janela Pipeline e vai para a janela "Lituania - Mercans" (`frentes/lituania`). O usuário disse **"sim" às correções locais**: SAM v1.1, GPM313/312 v1.2 e SIR v1.1, mais a revalidação. Drive, tickets e Kevin continuam pedindo ok.

## 1. O que reprovou (cada falha com arquivo e célula)
Cada achado tem a célula exata, o que está escrito, a fonte e a correção esperada nos relatórios de validação:

| Artefato | Relatório | Contagem |
|---|---|---|
| GPM313 v1.1 e GPM312 v1.1 (`2026-10-27-reports/LT-VMI-001-GPM313-Spec_v1.1.xlsx`, `LT-VMI-002-GPM312-Spec_v1.1.xlsx`) | [[Research Pipeline/Lithuania/2026-10-28-validacao/VAL-GPM313-GPM312\|VAL-GPM313-GPM312]] (tabela, l. 44–52 e seguintes) | 3 BLOCKER (B1–B3), 6 MAJOR (M1–M6), 9 MINOR |
| SAM v1.0 (`specs-drive/LT-SODRA-003-SAM-Spec.xlsx`) | [[Research Pipeline/Lithuania/2026-10-28-validacao/VAL-SAM\|VAL-SAM]] (l. 28–43) | 3 BLOCKER (S1–S3), 5 MAJOR (S4–S8), 6+ MINOR (S9–S16) |
| SIR v1.0 (`2026-10-27-SIR/LT-SIR-001-v1.0.docx` + `sections/s00–s08`) | [[Research Pipeline/Lithuania/2026-10-28-validacao/VAL-SIR\|VAL-SIR]] (l. 23–42) | 0 BLOCKER, 6 MAJOR (F01–F06), 14 MINOR (F07–F20) |

Os principais:
- **B1:** pagador `302123456` em GPM313 Spec!K3, Example Analysis!A2 e Sample File!B6, e em GPM312 Spec!K3/K12/K29 e Sample File!B6/B16/B30. Falha o mod 11 do `ID_formatas_simple_f`. Um valor válido é `302123442`.
- **B2:** GPM312 Spec!K31/K32. O PVM `LT100001234567` falha o `PVM_kodas`, porque o 13º caractere tem que ser "1".
- **B3:** GPM312 Sample File!B38/B39. A linha U com U2=6 e U5=26 gera 3 erros no script em 2026.
- **M1:** GPM312 Spec!F42 e F45 e Population Rules!C15. U12 e U15 têm que ser condicionais, não `Y`.
- **M2:** as caixas 4 e 5 da amostra devem somar 450 600,00, pela soma das linhas.
- **M3:** os exemplos usam ponto decimal. O FFData usa vírgula.
- **M4:** os códigos pessoais em L1 têm o dígito errado.
- **M6:** falta a regra 21 da IN GPM313.
- **S1:** o envelope do SAM Sample File!B4:B76 é diferente do FFData oficial.
- **S2:** a SAM usa ponto decimal, e o oficial usa vírgula.
- **S3:** as marcas da SAM são "x", e o oficial usa 0/1.
- **S4:** o mês aparece como `07` e deve ser `7`.
- **S5:** DocDate e DocNumber estão como obrigatórios.
- **S6:** a P3 de 39,58% é impossível em 2026.
- **S7:** as taxas de 2026 ficaram como pergunta ao RA.
- **S8:** falta o teto de 60 VDU, €138 729, e a base mínima (MMA).
- **F01–F06 (SIR):** IN-01/NP-SD2, 9-SD em aberto, contatos de erro do EDS (VA-72 §26), catálogo C23xx e correção do SAM, bloco Document Control do BE-SIR-001 e originais da Sodra não arquivados.
- **Drive:** o `.gsheet` do GPM312 tem 5 células `#ERROR!`, causadas por títulos que começam com "=".

## 2. Fontes oficiais usadas
- **VMI MXFD:**
  - `raw/docs/oficiais/LT/2026-10-27-VMI-reports/x_GPM313_mxfd/GPM313.mxfd`;
  - `raw/docs/oficiais/LT/2026-10-27-VMI-reports/x_GPM312_mxfd/GPM312.mxfd`.

  O script VBScript dentro de cada arquivo tem as funções `ID_formatas_simple_f`, `PVM_kodas` e `AK_tikrinimas`.
- **Sodra:**
  - descrição oficial `SAM specifications - Lithuanian.pdf`;
  - amostra `SAM-V07 SAMPLE (1).ffdata`.

  Estão em `C:\Users\instituto\Documents\youtrack_tickets\drive\2026-10-10-Lithuania\Lithuania\12- Country Report Codes\SODRA - Social Security\`, que é a cópia do Drive `Lithuania › 12- Country Report Codes › SODRA - Social Security`. **O ffdata tem o login de quem o criou, que é dado pessoal: não copiar nem citar.**
- **Leis:** XV-632 art. 3 (taxas de 2026), I-1336 art. 10(9) (teto) e VA-72 §21/§26/§27 (EDS). As citações estão nos relatórios.
- **Planilhas no Drive:**
  - GPM313 `1WoyBgcc-LJiTdGDk_zOh40lcQ5PZC67zC5RvpkULbgo`;
  - GPM312 `1Y02iqrFzs0qiYPaB5Up0_Wugax8DWX39BPhfJ_lgDZQ`.

  Para conferir, exportar cada aba com `export?format=csv&gid=…` (os gids estão na seção 4).

## 3. O que já foi gravado
- [[correcoes]], entrada de 2026-10-28 (Lituânia): o "no change" e o "alinhado" de 27/10 estavam errados, porque a conferência comparou só nomes e tamanhos de campo. O comentário na SR-419 já foi publicado com "no change".
- [[Research Pipeline/Lithuania/2026-10-28-validacao/CONFERENCIA]].
- Hub [[Lituania]], primeira linha das Pendências: validação de 28/10.
- Nada foi alterado em Drive, tickets ou e-mail.

## 4. Pedido ao BAU
- O rascunho está em [[rascunhos/2026-10-28-lituania-validacao-BAU]]: seções A–C, perguntas B1–B5 e o e-mail v1 ao Kevin, com Cc ao Khoi. **Não foi gravado.**
- A seção A descreve a v1.1 com erro e precisa ser refeita depois da correção.
- A iniciativa é nossa. Ninguém pediu (confirmado pela janela geral), então o texto deve dizer "para estarmos alinhados".
- Canal recomendado: a HRBS-15253, que é o ticket do Kevin. O usuário ainda não escolheu o canal.
- A janela Gmail tinha uma mensagem aberta ao Kevin, não gravada.

## 5. Ordem sugerida
1. SAM v1.1, GPM313/312 v1.2 e SIR v1.1, em local. Rodar `achar_versao.py` antes. As alterações vão em azul `FFDDEBF7`. Nenhuma célula pode começar com "=".
2. Revalidar: rodar as funções do MXFD por script sobre todos os exemplos e fazer uma segunda revisão independente.
3. Com ok do usuário: importar com Replace nos `.gsheet`, publicar o SIR v1.1 como versão nova com link na SR-479 e no monday, e a janela Suporte grava os comentários nas SR-419/420/421/479 e na CT-4285. A regra 9 se aplica, porque o país está ativo.
4. Refazer o pedido ao Kevin.

Ficam três pontos que só a fonte original resolve:
- os originais da Sodra (o site responde 403);
- o texto do V-243 nos pontos PT;
- a regra de adiar o prazo para o dia útil seguinte.

**gids (aba → gid):**
- GPM313:
  - VC 1130349186;
  - Report Matrix 2064371964;
  - PSS 1900840468;
  - Spec 1650267029;
  - File Structure 792375170;
  - Field Options 1768045524;
  - Population Rules 1668953042;
  - Example Analysis 736162719;
  - Sample File 252341644.
- GPM312:
  - VC 414018931;
  - Report Matrix 613352086;
  - PSS 2112574730;
  - Spec 1079508202;
  - File Structure 25634963;
  - Field Options 16590113;
  - Population Rules 83602944;
  - Example Analysis 129732338;
  - Sample File 350752344.

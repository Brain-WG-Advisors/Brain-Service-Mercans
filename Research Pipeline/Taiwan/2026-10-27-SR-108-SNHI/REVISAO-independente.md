# Revisão independente: SR-108 TW SNHI spec v1.2 (rodada 1, 2026-10-27)

**Veredito: FAIL (rodada 1).** As correções são pequenas: 1 BLOCKER de forma e 2 MAJOR de conteúdo. O resto foi conferido e está correto. Arquivo revisado: [[Research Pipeline/Taiwan/2026-10-27-SR-108-SNHI/TW - SNHI report specification_v1.2.xlsx|TW - SNHI report specification_v1.2.xlsx]] (md5 `ec6d02d6…`), contra a base de 27/10 (md5 `143efdc6…`). Apenas leitura: nada foi editado.

| # | Aba!célula | Problema | Fonte | Correção | Sev. |
|---|---|---|---|---|---|
| 1 | Spec(TXT)!I18, I21, I24, I25, I26, I39; Version Control!D15 | Há 7 marcadores "TO BE CONFIRMED" e o placeholder `<payment date>` (I18) dentro da coluna de mapeamento. O próprio gate (`validate_workbook.log`) dá FAIL C29 | C29 | Levar as 3 perguntas para a coluna K (Questions), que já é usada para isso (K16/K17/K20). Na coluna I fica só a proposta | BLOCKER |
| 2 | Spec(TXT)!I20 (vs F20, G20, E20) | "'1' por padrão; '2','3'…" vem do layout **CSV**. O layout **TXT** diz, no campo 39–68: 「由申報單位自行編號，以英數字為限，不得重覆，不足位數右補空白」. Com essa regra, todos os empregados recebem '1'. Isso contradiz F20/G20 ("no duplicates") e a amostra E20 `0862840762000001` | PDF TXT tipo 62 (二.8); CSV item 1 vs 2 | Numeração própria única por linha, como a amostra oficial: `CONCAT(UBN;'62';serial 9)`, alinhada à esquerda e completada com espaços até 30. Atende ao TXT e à opção 2 do CSV | MAJOR |
| 3 | Spec(TXT)!I4, I14 (e I33) | Pelo DD V3.3, `company_registration_number` é do tipo **Number**, "Maximum 8 digits". Um UBN com zero à esquerda (amostra `08628407`) sai com 7 caracteres e desloca a linha inteira, que é o mesmo sintoma da aba Testing. O SR-106 v1.1 (F9) já usa PREPAD | DD Country Fields r59; base E14 = 8628407.0 | `PREPAD($legal_entity_hr.company_registration_number; 8; '0')`. Fazer o mesmo em I24: `PREPAD(health_insure_id; 9; '0')` | MAJOR |
| 4 | Report Matrix!B16 | O filtro "2558 > 0" é uma inferência (a própria CONFERENCIA, lacuna 1, diz que não foi provada), mas não está marcado como inferência. Também diverge da lógica de I5 (58133+58009+58132 > 0) | Regs. art. 10 | Marcar como proposta e incluir na pergunta 1 ao Mohit | MINOR |
| 5 | Spec(TXT)!I6, I7 | F6/F7 dizem ROC yyymm, mas o mapeamento continua sem conversão: o dev pode gerar yyyymm | PDF TXT (一.4/5) | Mesma fórmula ROC de I8, com `'MM'` | MINOR |
| 6 | Spec(TXT)!I8 | ROC sem `PREPAD(…;3;'0')`, ao contrário do SR-106 v1.1 (F40/F60) feito hoje. Não muda nada em 2026 | consistência | Alinhar o padrão | MINOR |
| 7 | Report Matrix!B23 item 3 | Diz "ASCII **or** BIG5", enquanto B8 e a fonte dizem 「ASCII 及 BIG5」 | PDF TXT, nota 3 | Trocar por "ASCII and BIG5" | MINOR |
| 8 | comentario.md, item 3 | Diz "Income Payment Date… mapped", mas I18 está em aberto (pergunta 3) | — | Trocar por "proposed (engine variable to confirm)" | MINOR |

**Conferido e OK (medido por mim):**
- Comparação célula a célula própria (valor + preenchimento, 5 abas): 49 diferenças, todas na lista da análise e todas em `FFDDEBF7`. Nenhuma diferença fora do escopo. Testing e Options intactas.
- Comprimentos A/B/C = 200/200/200 e bloco 93–132 = 40, campo a campo contra o PDF TXT, incluindo tipos N/C.
- Totais C (contagem, soma de 69–82 e soma de 83–92) conferidos na amostra NHIA: 4 / 286942 / 2101. E36/E37/E38 batem com a amostra.
- B10 (nome do arquivo DPR) confere. 2,11%, 31/01 → 05/02 e leaver (art. 6) conferem com as fontes. "Category 1" confere (resumo 115, linha 62).
- `health_insure_id` (9), `64550` (= `$hr.nhi_grade::orLabel`), `representative` e `company_phone_number` existem no DD/WTC. `58139` não existe. As inferências estão marcadas como TBC.
- Sem fórmulas; XML bem formado; validações de dados preservadas (B6 = "Period" e B12 estão na lista); nenhum dado pessoal.

**Entregabilidade:** depois de corrigir 1–3, a spec pode voltar ao Mohit como **revisão com 3 perguntas**. Ainda não dá para testar ponta a ponta: I18 (variável da data de pagamento) depende da resposta dele.

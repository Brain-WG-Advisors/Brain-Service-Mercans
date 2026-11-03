# CRA v2.5 + WTC V4.9 — indenização alinhada à CCG v1.8 (2026-11-02)

> Hub: [[Espanha]] · Correções: [[correcoes]] · Ligado a [[Research Pipeline/Spain/2026-11-02-CCG-v1.8-descendentes-indenizacao/CONFERENCIA|CCG v1.8]] · País ativo → regra 9: ticket ao Development

## Origem
Usuário (janela Gmail, 02/11): alinhar os arquivos ligados à mudança da CCG v1.8 (9.1, excesso da indenização na base de SS) e antecipar as perguntas da Lily.

## Base
- `base/ES-CRA-001_ConceptosRetributivos_Spec-export-2026-11-02.xlsx`: export do gsheet atual (id 1ZvYflko…, Drive Spain/17/Social Security), 02/11 17:37, md5 b3bb6ff1…; versão 2,4 (In Progress, 04/09).
- `base/Spain_Wage_Type_Catalogue_V4.8-export-2026-11-02.xlsx`: export do gsheet V4.8 (id 1RWOFryO…, 02/11 07:00, Lily, Under Review), md5 3b108396….
- Script: `build.py` (openpyxl; células alteradas em azul claro FFDDEBF7).

## Fontes (lidas)
- TGSS, Manual CRA "Actualizado a 1 de julio de 2026", "CRA 0051 a 0054" e "Inclusión en un Fichero CRA … a más de un periodo": `raw/docs/oficiais/ES/2026-11-02-TGSS-Manual-CRA-01jul2026.txt` (md5 do PDF 615c8e70…). "deberán incluir tanto la parte excluida … –E- … como la parte … incluida … –I-. En ambos casos los importes a incluir se prorratearán a lo largo de los doce meses anteriores…".
- LGSS art. 147.2.c (todos os parágrafos); RD 2064/1995 art. 23.2.B; LIRPF art. 7.e (teto €180.000; conciliação) e art. 18.2 (30%).
- ES-BASES-001 v3.4 (Lily Query Resolved C34/C38): excesso 58188 em 500/601, rateado (L03).

## Antes → depois
| Arquivo | Célula | Antes | Depois |
|---|---|---|---|
| CRA v2.5 | Pay Elements F10 (58188) | E | **I** |
| CRA v2.5 | H10 (58188) | "indicator E is correct … ALL severance … outside the SS contribution base" | correção datada: I; rateio 12 meses; C/D espelham o WTC do mês do desligamento; texto antigo mantido abaixo |
| CRA v2.5 | H8, H9 (58184/58186) | E confirmado | correção datada: E certo, mas rateado nos 12 meses anteriores |
| CRA v2.5 | Population Rules C13 | split I/E | + "do valor isento do art. 147.2.c" + rateio 12 meses |
| CRA v2.5 | Version Control linha 19 | — | 2.5, 02-Nov-26, In Progress, Wallisson Gomes |
| WTC V4.9 | D132 (58188, explicação) | "BCCC/BCCP=Yes here is right … Subject to Tax=No contradicts …" (desatualizado) | explicação nova; **marcações inalteradas** (BCCC/BCCP = No, Tax = Yes, Irregular = Yes) |
| WTC V4.9 | Version Control linha 31 | — | 4.9, 02-Nov-26, Under Review, Wallisson Gomes |

## Conferência
- Diferença célula a célula com os exports: só as células acima (CRA 10; WTC 6). Merges, imagens e validações iguais.
- Cada frase nova relida contra a fonte (lista acima).

## Pendente
- Drive (cópia `_v2.5.xlsx` / `V4.9.xlsx`) e import nos gsheets: só com ok do usuário.
- Ticket ao Development: itens CRA (58188 → I; rateio 12 meses de 58184/58186/58188) e WTC (texto) → janela Suporte.
- Fora do pedido (não alterado): 62180/62181 ("Severance", 0054/E) e 62983 (0054/E) — composição não documentada; o rateio de 12 meses também se aplica a eles se forem 0054. Perguntar à Lily.
- Confirmar com a Lily: o motor reporta o 58188 rateado nas L03 (Bases) apesar de BCCC = No no WTC (a spec Bases v3.4 diz que sim).

## Frentes que mexeram
| Data | Frente | O quê |
|---|---|---|
| 2026-11-02 | gmail | exports, CRA v2.5 e WTC V4.9 montados e conferidos; não copiados ao Drive |
| 2026-11-03 | gmail | Lily (e-mail 03/11 08:22): texto do D132 (58188) levado para a V4.8 (gsheet); V4.9 .xlsx arquivada ("Excel format, against company policy"). Conferido no export csv do gsheet: D132 da V4.8 = texto da V4.9. WTC vigente = V4.8; o `Spain_Wage_Type_Catalogue_V4.9.xlsx` daqui é só histórico. Aberto: D132 cita ES-CRA-001 v2.5, ainda não importada no gsheet do CRA (v2.4) |

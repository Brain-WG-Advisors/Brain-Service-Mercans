# SG — 62866 Childbirth Allowance sujeito a CPF (HRBS-16029), 2026-10-27

**Pedido:** HRBS-16029 (Hayat, 16/10): "can you update 62866 component as CPF-able in the compliance WTC?" + pergunta original: SDL só sobre componentes CPF-able está certo? Análise: `rascunhos/2026-10-23-shruti/HRBS-16029-singapura-SDL-62866.md`.
**Situação:** pronto e arquivado no cérebro; **nada no Drive nem no ticket** (decisão do usuário 27/10: resolver tudo e aguardar a Manju).

**Fonte (relida pessoalmente em 27/10, cópias em `raw/docs/oficiais/SG/`):**
- SDL Act 1979 s.2 "wages" e CPF Act 1953 s.2 "wages": texto idêntico.
- CPF Act, First Schedule para 5(d)(i) (AW = remuneração que não é OW) e 5(e) (OW do mês = "wholly or exclusively in respect of employment during that month").
- CPFB, "Which allowances and payments attract CPF contributions?" (28/07/2025): "Gifts in kind to employees on their marriage or birth of their children — NO".

**Decisões (27/10):** escopo = só o 62866 (o que foi pedido); classificação AW (pagamento único, Lump Sum/Additional no próprio WTC), contrariando o "monthly wage" do Hayat, com a razão no comentário. 62878, 62983, IR8A > $200 e Remarks × coluna N: fora do pedido → hub [[Singapura]].

## Arquivos
| Arquivo | Base | Alterações |
|---|---|---|
| [[Research Pipeline/Singapore/2026-10-27-HRBS-16029-62866-CPF/Singapore Wage Type Catalogue V4.3.xlsx\|Singapore Wage Type Catalogue V4.3.xlsx]] (md5 `96b5e1b492fc013cbb8bc0db7edf6361`) | [[raw/docs/drive-exports/2026-10-27/SG_WTC_ativo.xlsx\|SG_WTC_ativo.xlsx]] (export do arquivo ativo no Monday, id `1faPACgj…`; md5 `f2b8554c…`; conteúdo igual ao export de 23/10) | 8 células |

Script: `aplicar_wtc.py` (XML + cópia byte a byte das demais partes). Log: `conferencia-wtc-log.txt`.

## Antes → depois
- Wage Type Catalogue N685 (Subject to CPF): No → **Yes**
- Wage Type Catalogue Q685 (OW/AW): NA → **Additional Wages**
- Wage Type Catalogue T685 (Remarks): vazio → "Cash payment through payroll is wages for CPF and SDL (CPF Act s.2; SDL Act s.2). One-off payment: Additional Wages (CPF Act, First Schedule para 5(d)). HRBS-16029."
- Version control linha 32: 4.3 · 2026-10-27 · "62866 Childbirth Allowance: Subject to CPF No -> Yes; Ordinary/Additional Wage NA -> Additional Wages (HRBS-16029)" · Under Review · Wallisson Gomes

## Conferência
1. Só `sheet1.xml`, `sheet2.xml`, `sharedStrings.xml` e `styles.xml` mudaram; demais partes byte a byte; XML válido em todas.
2. Comparação célula a célula (valor, preenchimento, fonte, borda, formato): exatamente as 8 células acima; todas em azul-claro `FFDDEBF7`.

## Pendências
- Drive (`03 - WTC`, Singapore) como [[Research Pipeline/Singapore/2026-10-27-HRBS-16029-62866-CPF/Singapore Wage Type Catalogue V4.3.xlsx|Singapore Wage Type Catalogue V4.3.xlsx]]: só com ordem do usuário; trocar `[link]` no comentário.
- V4.2 ainda "Under Review" (Mohit/Ruchi): confirmar antes de soltar a V4.3.
- Composição da base 58534 (SDL Base) na engine: não verificada.

## Frentes que mexeram
| Data | Frente | O quê |
|---|---|---|
| 2026-10-27 | Suporte | V4.3 gerada (8 células) e conferida; comentário pronto (aba do painel); nada publicado. |
